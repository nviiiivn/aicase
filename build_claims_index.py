#!/usr/bin/env python3
"""Generate the full claims exhibit from the collected JSON.

Written rather than hand-authored so the page cannot drift from the
evidence: every row comes out of evidence/claims/*.json, and the unverified
list is printed with the same weight as the verified one. A collection that
hides what it failed to get is not a collection, it is an argument.
"""
import collections
import html
import json
import pathlib

CASE = pathlib.Path(__file__).resolve().parent
OUT = CASE / "posts" / "every-claim.md"


def esc(s):
    return html.escape(str(s or ""), quote=False)


def main():
    claims, unverified = [], []
    for f in sorted((CASE / "evidence" / "claims").glob("*.json")):
        d = json.loads(f.read_text())
        claims += d.get("claims", [])
        unverified += d.get("unverified", [])

    by_vendor = collections.defaultdict(list)
    for c in claims:
        by_vendor[c.get("vendor", "?")].append(c)

    L = []
    L.append("# Every claim, verbatim\n")
    L.append(f"**{len(claims)} marketing claims** collected from "
             f"**{len(by_vendor)} vendors**, each copied word for word from "
             "the vendor's own page, with the URL and the date it was read. "
             f"**{len(unverified)} further claims could not be verified** and "
             "are listed at the bottom with the reason, rather than quietly "
             "dropped.\n")
    L.append("Nothing here is paraphrased. Where a claim reads oddly, that is "
             "how it is written on the page.\n")

    for vendor in sorted(by_vendor, key=lambda v: -len(by_vendor[v])):
        rows = by_vendor[vendor]
        L.append(f"\n## {esc(vendor)} — {len(rows)} claims\n")
        for c in rows:
            q = " ".join(str(c.get("claim_verbatim", "")).split())
            prod = esc(c.get("product", ""))
            url = c.get("url", "")
            when = str(c.get("date_accessed", ""))[:10]
            L.append(f"> {esc(q)}\n")
            bits = [b for b in (prod, f"read {when}" if when else "") if b]
            tail = " · ".join(bits)
            if url:
                L.append(f"{tail} — [source]({url})\n" if tail
                         else f"[source]({url})\n")
            elif tail:
                L.append(f"{tail}\n")

    if unverified:
        L.append("\n## Could not be verified\n")
        L.append("Listed because an evidence file that shows only its "
                 "successes is not evidence. Each of these was attempted and "
                 "failed, for the stated reason.\n")
        for u in unverified:
            why = " ".join(str(u.get("reason", "")).split())[:230]
            tgt = u.get("url") or u.get("target") or "—"
            L.append(f"- `{esc(str(tgt)[:90])}` — {esc(why)}\n")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(L))
    print(f"wrote {OUT}")
    print(f"  {len(claims)} claims across {len(by_vendor)} vendors, "
          f"{len(unverified)} unverified")
    for v in sorted(by_vendor, key=lambda v: -len(by_vendor[v])):
        print(f"    {v:<12} {len(by_vendor[v])}")


if __name__ == "__main__":
    main()
