#!/usr/bin/env python3
"""Measure repeated-failure behaviour across every model in the Totem logs.

Incident 001 documents one model failing one way for 42 hours. Its own
"Scope and limits" section says that establishes what *can* happen, not
what usually happens, and that showing a pattern needs many records. This
is those records: OpenCode/Totem sessions spanning DeepSeek, Qwen, GPT-5.5,
Gemini, Claude, GLM, Nemotron and others, all driven by the same person on
the same machine over the same weeks.

The question it answers is narrow and checkable: **when a tool call fails,
does the model try the identical call again?** That is the mechanical core
of the behaviour - not "was it unhelpful", which is unfalsifiable, but "did
it repeat a failing action verbatim", which is a string comparison.

Definitions, kept deliberately strict so a sceptic can re-derive them:

  retry      an identical (tool name + exact input) call issued again later
             in the same session, where an earlier instance had errored
  streak     the largest count of identical failing calls in one session
  loop       a session with a streak of 3 or more; three exceeds ordinary
             human trial-and-error

Sessions are attributed to a model by the `model` column on the session
row, falling back to the most common per-message model where that is null.
Read-only: the database is opened with mode=ro and never written.
"""
import collections
import hashlib
import json
import os
import pathlib
import sqlite3
import sys

#: The OpenCode/Totem session database. OPENCODE_DB points somewhere else.
DB = os.environ.get("OPENCODE_DB") or str(pathlib.Path.home() / ".local/share/opencode/opencode.db")
OUT = pathlib.Path(__file__).with_name("crossmodel-raw.json")


def shown(path):
    """A path as written into the output: home becomes ~, so a re-run never
    records whose machine it ran on."""
    p, home = str(path), str(pathlib.Path.home())
    return "~" + p[len(home):] if p == home or p.startswith(home + "/") else p


LOOP_THRESHOLD = 3


def model_name(raw):
    """Turn the stored model blob into a readable name."""
    if not raw:
        return None
    try:
        j = json.loads(raw) if isinstance(raw, str) else raw
    except Exception:
        return str(raw)[:40]
    return str(j.get("id") or j.get("modelID") or "?")


def family(name):
    """Group variants so the table compares vendors, not build numbers."""
    if not name:
        return "unknown"
    n = name.lower()
    for key, fam in (("deepseek", "DeepSeek"), ("qwen", "Qwen"),
                     ("gpt-", "GPT"), ("gemini", "Gemini"),
                     ("claude", "Claude"), ("glm", "GLM"),
                     ("nemotron", "Nemotron"), ("ring-", "Ring"),
                     ("big-pickle", "big-pickle"), ("grok", "Grok"),
                     ("llama", "Llama"), ("mistral", "Mistral")):
        if key in n:
            return fam
    return name[:22]


def main():
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

    sessions = {}
    for sid, raw_model, created, updated, cost, tin, tout in con.execute(
            "SELECT id, model, time_created, time_updated, cost, "
            "tokens_input, tokens_output FROM session"):
        sessions[sid] = {
            "model": model_name(raw_model), "created": created,
            "updated": updated, "cost": cost or 0,
            "tokens_out": tout or 0, "tokens_in": tin or 0,
        }

    # Per-message model, used as a fallback where the session row is null.
    per_session_models = collections.defaultdict(collections.Counter)
    for sid, data in con.execute("SELECT session_id, data FROM message"):
        try:
            m = (json.loads(data).get("model") or {})
        except Exception:
            continue
        mid = m.get("modelID")
        if mid:
            per_session_models[sid][mid] += 1

    for sid, s in sessions.items():
        if not s["model"] and per_session_models.get(sid):
            s["model"] = per_session_models[sid].most_common(1)[0][0]

    # Walk every tool call in order. A call is keyed by tool name plus a
    # hash of its exact input, so "the same call" means byte-identical
    # arguments, not merely the same tool being used twice.
    calls = collections.defaultdict(list)
    for sid, data in con.execute(
            "SELECT session_id, data FROM part ORDER BY time_created"):
        try:
            j = json.loads(data)
        except Exception:
            continue
        if j.get("type") != "tool":
            continue
        st = j.get("state") or {}
        inp = json.dumps(st.get("input"), sort_keys=True)[:4000]
        key = f"{j.get('tool')}:{hashlib.sha1(inp.encode()).hexdigest()[:12]}"
        calls[sid].append((key, st.get("status"), j.get("tool")))

    per_model = collections.defaultdict(lambda: {
        "sessions": 0, "sessions_with_tools": 0, "tool_calls": 0,
        "errors": 0, "repeat_fails": 0, "looped_sessions": 0,
        "worst_streak": 0, "cost": 0.0, "tokens_out": 0, "examples": [],
    })

    for sid, seq in calls.items():
        s = sessions.get(sid)
        if not s:
            continue
        agg = per_model[family(s["model"])]

        seen_fail = collections.Counter()
        errors = 0
        for key, status, _tool in seq:
            if status not in ("completed", "running", None):
                errors += 1
                seen_fail[key] += 1
        worst = max(seen_fail.values(), default=0)
        repeats = sum(v - 1 for v in seen_fail.values() if v > 1)

        agg["sessions_with_tools"] += 1
        agg["tool_calls"] += len(seq)
        agg["errors"] += errors
        agg["repeat_fails"] += repeats
        agg["worst_streak"] = max(agg["worst_streak"], worst)
        if worst >= LOOP_THRESHOLD:
            agg["looped_sessions"] += 1
            if len(agg["examples"]) < 3:
                top = max(seen_fail, key=seen_fail.get)
                tool_name = next((t for k, _, t in seq if k == top), "?")
                agg["examples"].append({"session": sid, "tool": tool_name,
                                        "identical_failures": worst})

    for sid, s in sessions.items():
        agg = per_model[family(s["model"])]
        agg["sessions"] += 1
        agg["cost"] += s["cost"] or 0
        agg["tokens_out"] += s["tokens_out"] or 0

    con.close()

    result = {
        "source": shown(DB),
        "loop_threshold": LOOP_THRESHOLD,
        "sessions_total": len(sessions),
        "models": dict(sorted(per_model.items(),
                              key=lambda kv: -kv[1]["sessions"])),
    }
    OUT.write_text(json.dumps(result, indent=2))

    print(f"{len(sessions)} sessions across {len(per_model)} model families\n")
    hdr = (f"{'model':<14}{'sess':>5}{'w/tools':>8}{'calls':>7}"
           f"{'errors':>7}{'repeats':>8}{'looped':>7}{'worst':>6}{'cost':>9}")
    print(hdr)
    print("-" * len(hdr))
    tot = collections.Counter()
    for fam, a in result["models"].items():
        if not a["sessions"]:
            continue
        print(f"{fam:<14}{a['sessions']:>5}{a['sessions_with_tools']:>8}"
              f"{a['tool_calls']:>7}{a['errors']:>7}{a['repeat_fails']:>8}"
              f"{a['looped_sessions']:>7}{a['worst_streak']:>6}"
              f"{a['cost']:>9.2f}")
        for k in ("sessions", "sessions_with_tools", "tool_calls", "errors",
                  "repeat_fails", "looped_sessions"):
            tot[k] += a[k]
        tot["cost"] += a["cost"]
    print("-" * len(hdr))
    print(f"{'TOTAL':<14}{tot['sessions']:>5}{tot['sessions_with_tools']:>8}"
          f"{tot['tool_calls']:>7}{tot['errors']:>7}{tot['repeat_fails']:>8}"
          f"{tot['looped_sessions']:>7}{'':>6}{tot['cost']:>9.2f}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    sys.exit(main())
