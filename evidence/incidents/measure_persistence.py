#!/usr/bin/env python3
"""Measure the behaviour that actually caused the harm.

The first two scripts measured literal repetition - the same tool called
with the same input until it failed again. That metric is clean, and it
came back nearly empty for Claude: 237 transcripts, zero looped. It is the
wrong measurement. The 42 hours in incident 001 were not one call repeated;
they were eight different attempts against a single precondition nobody
tested, which no string comparison will ever catch.

So this measures two things that are closer to the injury and are still
countable rather than interpretive:

  GRIND     the longest run of consecutive tool outcomes in a session where
            at least half failed, measured in calls and wall-clock time.
            "Different things, all failing, for hours" is the signature of
            working on something infeasible.

  AFTER     what happened once the user had already objected. The first
            user message matching an objection pattern is the moment the
            problem became visible from outside the system; everything
            spent after that was spent against an explicit complaint. This
            is the number with moral and legal weight, because it is not
            "the model was wrong", it is "the model was told, and
            continued".

An objection is a short message the user typed - never a tool result, which
arrives in the transcript wearing the same `user` label and would otherwise
count her own build logs as complaints.

Read-only, streaming.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path("/home/demo/.claude/projects")
OUT = pathlib.Path(__file__).with_name("persistence-raw.json")

OBJECTION = re.compile(
    r"same (thing|problem|error)|over and over|still (going|broken|not|no)|"
    r"circles|again\?|stop\b|why (is|are|did|do) (it|you)|how long|"
    r"nothing to show|wasting|waste of|hours|give up|gave up|"
    r"you (said|told me|keep|kept)|not work|doesn'?t work|didn'?t work|"
    r"fucking|wtf|christ|jesus", re.I)

MIN_RUN = 6          # a "grind" has to be at least this many outcomes
FAIL_RATIO = 0.5     # and at least this proportion failing


def is_typed(msg):
    """True only for words the user typed, not a tool result echoed back."""
    c = msg.get("content") if isinstance(msg, dict) else None
    if isinstance(c, str):
        return True
    for b in (c or []):
        if isinstance(b, dict) and b.get("type") == "tool_result":
            return False
    return True


def text_of(msg):
    c = msg.get("content") if isinstance(msg, dict) else msg
    if isinstance(c, str):
        return c
    out = []
    for b in (c or []):
        if isinstance(b, dict) and b.get("type") == "text":
            out.append(b.get("text", ""))
    return "\n".join(out)


def _hours(a, b):
    import datetime as dt
    try:
        pa = dt.datetime.fromisoformat(a.replace("Z", "+00:00"))
        pb = dt.datetime.fromisoformat(b.replace("Z", "+00:00"))
        return round((pb - pa).total_seconds() / 3600, 2)
    except Exception:
        return 0.0


def scan(path):
    events = []
    with path.open(errors="replace") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("type") not in ("assistant", "user"):
                continue
            ts = d.get("timestamp")
            msg = d.get("message") or {}
            c = msg.get("content")
            if d["type"] == "user" and is_typed(msg):
                t = text_of(msg)
                if t and len(t) < 2000 and OBJECTION.search(t):
                    events.append((ts, "objection", " ".join(t.split())[:180]))
            for b in (c if isinstance(c, list) else []):
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "tool_use":
                    events.append((ts, "call", b.get("name")))
                elif b.get("type") == "tool_result":
                    events.append((ts, "fail" if b.get("is_error") else "ok",
                                   b.get("tool_use_id")))

    outcomes = [e for e in events if e[1] in ("fail", "ok")]

    # GRIND: longest window over outcomes where >= FAIL_RATIO failed.
    best = {"calls": 0, "fails": 0, "hours": 0.0}
    n = len(outcomes)
    for i in range(n):
        if outcomes[i][1] != "fail":
            continue
        fails = 0
        for j in range(i, n):
            if outcomes[j][1] == "fail":
                fails += 1
            span = j - i + 1
            if span >= MIN_RUN and fails / span >= FAIL_RATIO and span > best["calls"]:
                best = {"calls": span, "fails": fails,
                        "hours": _hours(outcomes[i][0], outcomes[j][0])}

    objections = [e for e in events if e[1] == "objection"]
    after = {"objections": len(objections), "calls_after": 0,
             "fails_after": 0, "hours_after": 0.0, "first": None}
    if objections:
        t0 = objections[0][0]
        after["first"] = {"at": t0, "said": objections[0][2]}
        last = events[-1][0] if events else t0
        after["calls_after"] = sum(1 for e in events
                                   if e[1] == "call" and e[0] and t0 and e[0] > t0)
        after["fails_after"] = sum(1 for e in events
                                   if e[1] == "fail" and e[0] and t0 and e[0] > t0)
        after["hours_after"] = _hours(t0, last)
    return best, after, sum(1 for e in events if e[1] == "call")


def main():
    files = sorted(ROOT.glob("*/*.jsonl"))
    print(f"scanning {len(files)} transcripts", flush=True)
    rows = []
    for i, p in enumerate(files, 1):
        try:
            grind, after, calls = scan(p)
        except Exception as e:
            print(f"  skipped {p.name}: {type(e).__name__}", flush=True)
            continue
        if calls:
            rows.append({"project": p.parent.name, "file": p.name,
                         "tool_calls": calls, "grind": grind, "after": after})
        if i % 50 == 0:
            print(f"  {i}/{len(files)}", flush=True)

    rows.sort(key=lambda r: -r["grind"]["calls"])
    OUT.write_text(json.dumps({"source": str(ROOT), "sessions": rows}, indent=2))

    print("\n=== WORST GRINDS (consecutive outcomes, >=50% failing) ===")
    print(f"{'project':<32}{'calls':>7}{'fails':>7}{'hours':>7}")
    for r in rows[:10]:
        g = r["grind"]
        if g["calls"]:
            print(f"{r['project'][:31]:<32}{g['calls']:>7}{g['fails']:>7}"
                  f"{g['hours']:>7.1f}")

    told = [r for r in rows if r["after"]["objections"]]
    told.sort(key=lambda r: -r["after"]["calls_after"])
    print("\n=== SPENT AFTER SHE ALREADY OBJECTED ===")
    print(f"{'project':<28}{'objs':>5}{'calls after':>12}{'fails after':>12}{'hours':>7}")
    for r in told[:10]:
        a = r["after"]
        print(f"{r['project'][:27]:<28}{a['objections']:>5}"
              f"{a['calls_after']:>12}{a['fails_after']:>12}{a['hours_after']:>7.1f}")
    tc = sum(r["after"]["calls_after"] for r in told)
    tf = sum(r["after"]["fails_after"] for r in told)
    th = sum(r["after"]["hours_after"] for r in told)
    print(f"\n  {len(told)} sessions contained an objection")
    print(f"  {tc:,} tool calls and {tf:,} failures came AFTER the first one")
    print(f"  {th:,.0f} cumulative hours of session time after the first objection")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    sys.exit(main())
