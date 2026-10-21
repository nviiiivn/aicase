#!/usr/bin/env python3
"""Activate the site theme and publish the evidence posts to Ghost.

Ghost's Admin API wants a session cookie for password auth, so this signs
in once and reuses it. Posts are sent with ?source=html, because Ghost 5
silently drops an `html` field without it - a post created that way
arrives empty, which looks exactly like a publishing failure but is a
parameter mistake.

Idempotent: a post whose slug already exists is updated in place rather
than duplicated, so re-running after an edit is safe.
"""
import json
import os
import pathlib
import re
import urllib.error
import urllib.request

# Settings come from the environment (see .env.example), never from this file.
BASE = os.environ.get("GHOST_URL", "http://127.0.0.1:2368").rstrip("/")
SITE = os.environ.get("GHOST_SITE", "fuai.alola.lol")   # public host Ghost serves
THEME = os.environ.get("GHOST_THEME", "alola-case")     # activated if installed
CASE = pathlib.Path(__file__).resolve().parent

# The login is read at run time, not hard-coded: it was changed once already
# and a stale address here fails as a 404 "no user with that email", which
# reads like a broken endpoint rather than wrong creds. Either set
# GHOST_EMAIL + GHOST_PASSWORD, or point GHOST_CREDS_FILE at a private file
# holding "email: ..." and "password: ..." lines.
email = os.environ.get("GHOST_EMAIL")
password = os.environ.get("GHOST_PASSWORD")
if not (email and password) and os.environ.get("GHOST_CREDS_FILE"):
    _v = pathlib.Path(os.environ["GHOST_CREDS_FILE"]).expanduser().read_text()
    email = email or re.search(r"email:\s*(\S+)", _v).group(1)
    password = password or re.search(r"password:\s*(\S+)", _v).group(1)
if not (email and password):
    raise SystemExit("set GHOST_EMAIL and GHOST_PASSWORD, or GHOST_CREDS_FILE (see .env.example)")
_cookie = None


def call(path, data=None, method=None, source_html=False, quiet404=False,
         raw_body=None):
    url = f"{BASE}{path}" + ("?source=html" if source_html else "")
    body = raw_body if raw_body is not None else (
        json.dumps(data).encode() if data is not None else None)
    req = urllib.request.Request(url, data=body,
                                 method=method or ("POST" if body else "GET"))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept-Version", "v5.0")
    req.add_header("Origin", f"https://{SITE}")
    req.add_header("Host", SITE)
    # Ghost issues its admin session cookie with Secure+SameSite=None, and
    # will not set it at all unless it believes the connection is https.
    # Over plain loopback that means sign-in returns 201 with no cookie and
    # every following call is a 403 "Unable to determine the authenticated
    # user" - which reads as a credentials problem and is not one.
    req.add_header("X-Forwarded-Proto", "https")
    if _cookie:
        req.add_header("Cookie", _cookie)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as e:
        if e.code == 404 and quiet404:
            return None
        detail = e.read()[:400].decode(errors="replace")
        raise SystemExit(f"{method or 'GET'} {path} -> {e.code}: {detail}")


# --- sign in -----------------------------------------------------------
req = urllib.request.Request(
    f"{BASE}/ghost/api/admin/session/",
    data=json.dumps({"username": email, "password": password}).encode(),
    method="POST")
for k, v in (("Content-Type", "application/json"), ("Accept-Version", "v5.0"),
             ("Origin", f"https://{SITE}"), ("Host", SITE),
             ("X-Forwarded-Proto", "https")):
    req.add_header(k, v)
with urllib.request.urlopen(req, timeout=120) as r:
    _cookie = r.headers.get("Set-Cookie", "").split(";")[0]
print("signed in" if _cookie else "NO COOKIE", flush=True)

# --- activate the theme ------------------------------------------------
# Activation is best-effort. This endpoint returns 403 "Unable to determine
# the authenticated user" for the same session cookie that every other
# endpoint accepts - including /users/me/ and the post routes below. The
# theme is already active from a direct call, so a failure here must not
# stop the publish; the error message points at authentication and the
# cause is not authentication.
try:
    out = call(f"/ghost/api/admin/themes/{THEME}/activate/", method="PUT",
               raw_body=b"")
    print("theme active:",
          [t["name"] for t in out.get("themes", []) if t.get("active")]
          or "(none)", flush=True)
except SystemExit as e:
    print(f"theme activate skipped ({str(e)[:60]}...)", flush=True)


def md_to_html(md):
    """Small markdown -> HTML pass covering what the evidence files use.

    Deliberately not a full markdown engine: these documents use headings,
    bold, inline code, links, tables, blockquotes and lists, and a narrow
    converter that handles exactly those is easier to trust than a
    dependency that might reflow a quotation. Quotations here are evidence
    and have to survive the trip unchanged.
    """
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if (ln.startswith("|") and i + 1 < len(lines)
                and set(lines[i + 1].replace("|", "").strip()) <= set("-: ")):
            head = [c.strip() for c in ln.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            t = ["<div class='table-wrap'><table><thead><tr>"]
            t += [f"<th>{c}</th>" for c in head]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        out.append(ln)
        i += 1
    html = "\n".join(out)

    html = re.sub(r"^### (.+)$", r"<h3>\1</h3>", html, flags=re.M)
    html = re.sub(r"^## (.+)$", r"<h2>\1</h2>", html, flags=re.M)
    html = re.sub(r"^# (.+)$", r"<h1>\1</h1>", html, flags=re.M)
    html = re.sub(r"^---$", "<hr>", html, flags=re.M)
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)
    html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', html)

    blocks, buf = [], []
    for ln in html.split("\n"):
        if ln.startswith(("<h", "<hr", "<div class='table-wrap'")):
            if buf:
                blocks.append("\n".join(buf)); buf = []
            blocks.append(ln)
        elif not ln.strip():
            if buf:
                blocks.append("\n".join(buf)); buf = []
        else:
            buf.append(ln)
    if buf:
        blocks.append("\n".join(buf))

    final = []
    for b in blocks:
        if b.startswith(("<h", "<hr", "<div")):
            final.append(b)
        elif b.lstrip().startswith("> "):
            inner = "<br>".join(x.lstrip()[2:] for x in b.split("\n")
                                if x.lstrip().startswith("> "))
            final.append(f"<blockquote><p>{inner}</p></blockquote>")
        elif b.lstrip().startswith(("- ", "* ")):
            items = "".join(f"<li>{x.lstrip()[2:]}</li>" for x in b.split("\n")
                            if x.lstrip()[:2] in ("- ", "* "))
            final.append(f"<ul>{items}</ul>")
        else:
            final.append("<p>" + b.replace("\n", " ") + "</p>")
    return "\n".join(final)


def upsert(slug, title, html, excerpt, tag):
    found = call(f"/ghost/api/admin/posts/slug/{slug}/", quiet404=True)
    existing = (found.get("posts") or [None])[0] if found else None
    payload = {"posts": [{
        "title": title, "slug": slug, "html": html, "status": "published",
        "custom_excerpt": excerpt, "tags": [{"name": tag}],
    }]}
    if existing:
        payload["posts"][0]["updated_at"] = existing["updated_at"]
        out = call(f"/ghost/api/admin/posts/{existing['id']}/", data=payload,
                   method="PUT", source_html=True)
        return "updated", out["posts"][0]["url"]
    out = call("/ghost/api/admin/posts/", data=payload, method="POST",
               source_html=True)
    return "created", out["posts"][0]["url"]


POSTS = [
    ("why-this-exists", "Why this exists",
     CASE / "posts/why-this-exists.md",
     "It takes my money, I am not the only one, and complaints without "
     "proof change nothing. So: receipts only.",
     "About"),
    ("what-the-studies-say", "\"55% faster\" - and the study that found 19% slower",
     CASE / "posts/what-the-studies-say.md",
     "The vendor number came from 95 developers doing one timed task. The "
     "independent RCT on experienced developers doing real work measured a "
     "19% slowdown - while those developers believed they were 20% faster.",
     "Research"),
    ("published-findings", "The research file",
     CASE / "research/published-findings.md",
     "18 verified papers on agent stopping failures, sycophancy, developer "
     "productivity and benchmark validity - with the six that could not be "
     "confirmed listed as unverified.",
     "Research"),
    ("the-numbers", "The numbers they advertise, and who measured them",
     CASE / "posts/the-numbers.md",
     "30 of the 80 collected claims carry a hard number - and a number, "
     "unlike an adjective, is a representation of fact that has to be "
     "substantiable. Including who ran the study.",
     "Evidence"),
    ("every-claim", "Every claim, verbatim",
     CASE / "posts/every-claim.md",
     "All 80 marketing claims from 8 vendors, copied word for word with "
     "source URLs and access dates - plus the 16 that could not be verified, "
     "listed with reasons rather than dropped.",
     "Evidence"),
    ("the-gap", "What they sell, and what happened",
     CASE / "posts/the-gap.md",
     "Five vendors sell the same promise in nearly the same words. Here it "
     "is verbatim, next to a fully documented instance of it not happening "
     "- and an honest account of what that does and does not prove.",
     "Analysis"),
    ("incident-001", "Exhibit A - 42 hours, one unchecked precondition",
     CASE / "evidence/incidents/incident-001.md",
     "A paid AI coding agent spent 42 hours and 336,627 output tokens on one "
     "task, ignored 25 user objections, and produced nothing. Every figure "
     "here is counted from the session logs, not remembered.",
     "Evidence"),
    ("legal-framework", "The law, including the parts that hurt",
     CASE / "research/legal-framework.md",
     "What a false-advertising claim against an AI vendor would have to prove, "
     "the FTC's own enforcement record, and the three obstacles that make a "
     "consumer class action the weakest available route.",
     "Law"),
]

for slug, title, path, excerpt, tag in POSTS:
    if not path.is_file():
        print(f"  MISSING {path}", flush=True)
        continue
    what, url = upsert(slug, title, md_to_html(path.read_text()), excerpt, tag)
    print(f"  {what}: {url}", flush=True)

print("done", flush=True)
