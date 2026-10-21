#!/usr/bin/env python3
"""Run the cross-model repeat-failure measurement over the Claude logs.

`measure_crossmodel.py` answered the same question for the Totem/OpenCode
database and found that most non-DeepSeek sessions there were abandoned
after a message or two, so they carry no evidence either way. This covers
the other corpus with real volume: every Claude Code transcript under
~/.claude/projects, across all projects.

The definition of a repeat is identical to the Totem script on purpose, so
the two numbers can sit in the same table without an asterisk:

  a tool call is keyed by tool name + a hash of its exact input
  a call "failed" if its tool_result came back with is_error true
  a repeat is the same key failing again later in the same transcript
  a loop is a transcript where one key failed 3 or more times

Claude's format differs from OpenCode's: the call and its result are in
separate records linked by tool_use_id, so failures have to be joined back
to the call that caused them rather than read off a single row.

Read-only. Streams line by line - the corpus is ~600 MB and one file alone
is 112 MB, so nothing is loaded whole.
"""
import collections
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path("/home/demo/.claude/projects")
OUT = pathlib.Path(__file__).with_name("claude-projects-raw.json")
LOOP_THRESHOLD = 3


def blocks(msg):
    c = msg.get("content") if isinstance(msg, dict) else None
    return c if isinstance(c, list) else []


def scan(path):
    """One transcript -> (calls, failures, repeats, worst, example)."""
    key_of = {}                       # tool_use_id -> key
    fails = collections.Counter()     # key -> failure count
    names = {}                        # key -> tool name
    total = 0

    with path.open(errors="replace") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("type") not in ("assistant", "user"):
                continue
            for b in blocks(d.get("message") or {}):
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "tool_use":
                    inp = json.dumps(b.get("input"), sort_keys=True)[:4000]
                    k = (f"{b.get('name')}:"
                         f"{hashlib.sha1(inp.encode()).hexdigest()[:12]}")
                    key_of[b.get("id")] = k
                    names[k] = b.get("name")
                    total += 1
                elif b.get("type") == "tool_result" and b.get("is_error"):
                    k = key_of.get(b.get("tool_use_id"))
                    if k:
                        fails[k] += 1

    worst = max(fails.values(), default=0)
    repeats = sum(v - 1 for v in fails.values() if v > 1)
    example = None
    if worst >= LOOP_THRESHOLD:
        top = max(fails, key=fails.get)
        example = {"file": path.name, "tool": names.get(top, "?"),
                   "identical_failures": worst}
    return total, sum(fails.values()), repeats, worst, example


def main():
    per_project = collections.defaultdict(lambda: {
        "transcripts": 0, "tool_calls": 0, "failures": 0,
        "repeat_fails": 0, "looped_transcripts": 0, "worst_streak": 0,
        "examples": [],
    })

    files = sorted(ROOT.glob("*/*.jsonl"))
    print(f"scanning {len(files)} transcripts", flush=True)
    for i, path in enumerate(files, 1):
        agg = per_project[path.parent.name]
        try:
            total, failed, repeats, worst, example = scan(path)
        except Exception as e:
            print(f"  skipped {path.name}: {type(e).__name__}", flush=True)
            continue
        agg["transcripts"] += 1
        agg["tool_calls"] += total
        agg["failures"] += failed
        agg["repeat_fails"] += repeats
        agg["worst_streak"] = max(agg["worst_streak"], worst)
        if example:
            agg["looped_transcripts"] += 1
            if len(agg["examples"]) < 3:
                agg["examples"].append(example)
        if i % 50 == 0:
            print(f"  {i}/{len(files)}", flush=True)

    result = {
        "source": str(ROOT), "loop_threshold": LOOP_THRESHOLD,
        "transcripts": len(files),
        "projects": dict(sorted(per_project.items(),
                                key=lambda kv: -kv[1]["tool_calls"])),
    }
    OUT.write_text(json.dumps(result, indent=2))

    hdr = (f"\n{'project':<44}{'files':>6}{'calls':>8}{'fails':>7}"
           f"{'repeats':>8}{'looped':>7}{'worst':>6}")
    print(hdr)
    print("-" * (len(hdr) - 1))
    tot = collections.Counter()
    for proj, a in result["projects"].items():
        print(f"{proj[:43]:<44}{a['transcripts']:>6}{a['tool_calls']:>8}"
              f"{a['failures']:>7}{a['repeat_fails']:>8}"
              f"{a['looped_transcripts']:>7}{a['worst_streak']:>6}")
        for k in ("transcripts", "tool_calls", "failures", "repeat_fails",
                  "looped_transcripts"):
            tot[k] += a[k]
    print("-" * (len(hdr) - 1))
    print(f"{'TOTAL':<44}{tot['transcripts']:>6}{tot['tool_calls']:>8}"
          f"{tot['failures']:>7}{tot['repeat_fails']:>8}"
          f"{tot['looped_transcripts']:>7}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    sys.exit(main())
