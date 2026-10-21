#!/usr/bin/env python3
"""Measure the iOS-build loop from the session transcripts.

Everything in the write-up has to come from the record rather than from
anyone's memory of it - including mine, which has already been wrong about
the duration once (I said "16 hours"; she said two days, and she was
right). So this walks every transcript in the project, pulls out the turns
that touched the iOS build, and counts:

  * wall-clock span, first mention to last
  * how many assistant turns went into it
  * how many DISTINCT error signatures appeared, versus how many times
    each recurred - the central claim is that one wall was renamed, not
    that many walls were hit
  * every point where she said, in her own words, that it was looping
  * tokens, which is the part she paid for

Output is one JSON file; nothing is interpreted here.
"""
import collections
import json
import pathlib
import re
import sys

PROJECT = pathlib.Path("/home/demo/.claude/projects/-home-demo-www-dashbored")
OUT = pathlib.Path(__file__).with_name("loop_evidence.json")

# What counts as "this task". Deliberately broad: the point is to catch
# every turn spent on it, including the ones that called it something else.
TOPIC = re.compile(r"\b(ipa|xcode|xcodebuild|actool|simruntime|simulator runtime|"
                   r"codesign|sideload|altstore|sideloadly|iphoneos|"
                   r"assetcatalog|dkphotogallery|macos-latest|docker-osx)\b", re.I)

# The distinct walls, by their signature in the logs. If the "many errors"
# story is true these should be spread through the timeline; if the "one
# wall, four names" story is true they should each cluster.
SIGNATURES = {
    "xcodebuild hung at 0% CPU": re.compile(r"0\.0%?\s*CPU|hung at 0", re.I),
    "CompileAssetCatalog / DKPhotoGallery": re.compile(r"CompileAssetCatalog|DKPhotoGallery", re.I),
    "AssetCatalogSimulatorAgent handshake": re.compile(r"AssetCatalogSimulatorAgent|Failed to handshake", re.I),
    "missing Foundation symbol": re.compile(r"decimalDigits|Symbol not found", re.I),
    "no simulator runtime available": re.compile(r"No available simulator runtimes|supportedRuntimes=\[\]", re.I),
    "download stalled": re.compile(r"Preparing to download", re.I),
    # Tightened after a first pass: "exhaust" matched ordinary prose and
    # dated this wall to 09-20, three days before the CI runs actually
    # failed. A claim in the write-up is only as good as the regex behind
    # it, so each pattern now has to name the thing itself.
    "CI job died with no steps": re.compile(
        r"died (in|with).{0,20}(no|zero) (steps|logs)|"
        r"minutes (are )?exhausted|allowance", re.I),
    "Apple refused the request": re.compile(
        r"\b403\b.{0,60}(mesu|apple|asset|catalog)|"
        r"(mesu|MobileAsset).{0,60}\b403\b", re.I),
}

# Her, saying it out loud. These are the moments the loop was visible from
# outside and continued anyway.
SHE_FLAGGED = re.compile(
    r"same (thing|problem|error)|over and over|still going|hours|circles|"
    r"again\?|you (said|told me)|repeat|why (is|are) (it|you)|how long|"
    r"gave up|still (don't|dont|no)", re.I)


def is_really_her(msg):
    """True only for words she typed.

    A tool result comes back as a `user` record too, so the first pass
    counted build logs as things she said - it "found" her complaining at
    05:32 on the 20th, when that was a tool result being echoed. Anything
    carrying a tool_result block is the machine talking to itself.
    """
    content = msg.get("content") if isinstance(msg, dict) else msg
    if isinstance(content, str):
        return True
    for block in content or []:
        if isinstance(block, dict) and block.get("type") == "tool_result":
            return False
    return True


def text_of(msg):
    """Flatten a message's content to plain text."""
    if isinstance(msg, str):
        return msg
    if isinstance(msg, dict):
        msg = msg.get("content", "")
    if isinstance(msg, str):
        return msg
    out = []
    for block in msg or []:
        if isinstance(block, dict):
            if block.get("type") == "text":
                out.append(block.get("text", ""))
            elif block.get("type") == "tool_use":
                out.append(json.dumps(block.get("input", ""))[:4000])
            elif block.get("type") == "tool_result":
                c = block.get("content")
                out.append(c if isinstance(c, str) else json.dumps(c)[:4000])
        elif isinstance(block, str):
            out.append(block)
    return "\n".join(out)


def main():
    turns = []
    files = sorted(PROJECT.glob("*.jsonl"))
    print(f"scanning {len(files)} transcripts", flush=True)
    for path in files:
        with path.open(errors="replace") as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") not in ("user", "assistant"):
                    continue
                msg = d.get("message") or {}
                role = msg.get("role") or d.get("type")
                body = text_of(msg)
                if not body:
                    continue
                usage = msg.get("usage") or {}
                hers = role == "user" and is_really_her(msg)
                turns.append({
                    "ts": d.get("timestamp"),
                    "role": role,
                    "hers": hers,
                    "topic": bool(TOPIC.search(body)),
                    "sigs": [k for k, rx in SIGNATURES.items() if rx.search(body)],
                    "flag": bool(hers and SHE_FLAGGED.search(body)
                                 and len(body) < 2000
                                 and not body.startswith("<")),
                    "out_tok": usage.get("output_tokens", 0),
                    "in_tok": usage.get("input_tokens", 0),
                    "cache_tok": usage.get("cache_read_input_tokens", 0),
                    "text": body[:600] if hers and len(body) < 2000 else "",
                })
    turns = [t for t in turns if t["ts"]]
    turns.sort(key=lambda t: t["ts"])
    print(f"{len(turns):,} timestamped turns", flush=True)

    topical = [t for t in turns if t["topic"]]
    sig_times = collections.defaultdict(list)
    for t in turns:
        for s in t["sigs"]:
            sig_times[s].append(t["ts"])

    result = {
        "turns_total": len(turns),
        "turns_on_topic": len(topical),
        "first_on_topic": topical[0]["ts"] if topical else None,
        "last_on_topic": topical[-1]["ts"] if topical else None,
        "session_first": turns[0]["ts"],
        "session_last": turns[-1]["ts"],
        "assistant_turns_on_topic": sum(1 for t in topical if t["role"] == "assistant"),
        "output_tokens_on_topic": sum(t["out_tok"] for t in topical),
        "output_tokens_total": sum(t["out_tok"] for t in turns),
        "input_tokens_total": sum(t["in_tok"] for t in turns),
        "cache_tokens_total": sum(t["cache_tok"] for t in turns),
        "signatures": {
            k: {"count": len(v), "first": min(v), "last": max(v)}
            for k, v in sorted(sig_times.items())
        },
        "her_messages_total": sum(1 for t in turns if t["hers"]),
        "she_flagged": [
            {"ts": t["ts"], "said": " ".join(t["text"].split())}
            for t in turns if t["flag"]
        ][:80],
        # Every raw match, so any number in the write-up can be traced back
        # to the line that produced it rather than taken on trust.
        "signature_hits": {
            k: sorted(v)[:200] for k, v in sig_times.items()
        },
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(f"wrote {OUT}", flush=True)
    print(f"  on-topic turns: {result['turns_on_topic']:,}")
    print(f"  span: {result['first_on_topic']} -> {result['last_on_topic']}")
    for k, v in result["signatures"].items():
        print(f"  {v['count']:>4}x  {k}")
    print(f"  times she flagged it: {len(result['she_flagged'])}")


if __name__ == "__main__":
    sys.exit(main())
