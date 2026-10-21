# aicase

**What AI coding tools are sold as, next to what they did.** Receipts only.

aicase is the source for an evidence site, [fuai.alola.lol](https://fuai.alola.lol).
On one side are the vendors' own marketing claims, copied word for word with
URL and date. On the other is a fully documented incident, counted from session
logs. Both sides sit beside the published research and the law that would
apply.

There are no opinions about whether AI is good. Every number is produced by a
script in this repo that you can re-run against your own logs. Where something
could not be verified, it says so. Measurements that failed to show what was
expected are kept and labelled as failures, not deleted.

## Why

AI coding agents are sold as fast, autonomous and reliable, on a subscription,
by the hour. When one spends two days confidently failing at something that
was impossible from the first minute, the customer pays for all of it.
Complaints without proof change nothing. A transcript, a token count and the
vendor's own words next to each other are harder to wave away. The full reason
is in [posts/why-this-exists.md](posts/why-this-exists.md).

## What's in it

| Path | What it is |
| --- | --- |
| `evidence/claims/*.json` | 80 marketing claims from 8 vendors, verbatim, with URL, page title, access date and context. Plus 16 that could not be verified, with the reason |
| `evidence/incidents/incident-001.md` | **Exhibit A**: a paid agent spent 42 hours and 336,627 output tokens on one task, kept going through 25 objections, and produced nothing |
| `evidence/incidents/measure*.py` | the scripts that count every figure, from Claude Code transcripts and an OpenCode session database |
| `evidence/incidents/*-raw.json` | their output: the counted numbers, with no interpretation |
| `research/published-findings.md` | 18 verified papers on agents that don't stop, sycophancy, developer productivity and benchmark validity. Six that couldn't be confirmed are listed as unverified |
| `research/legal-framework.md` | what a false-advertising claim would have to prove, the FTC record, and why a class action is the weakest route |
| `posts/*.md` | the site's articles, built from the files above |
| `build_claims_index.py` | writes `posts/every-claim.md` from the claims JSON, so that page can't drift from the evidence |
| `publish.py` | publishes everything to a Ghost blog. Re-running updates posts in place |

## Re-run the numbers

Python 3.9+ and nothing else; every script uses the standard library only.

```sh
git clone https://github.com/nviiiivn/aicase.git
cd aicase

python3 build_claims_index.py                         # rebuild posts/every-claim.md

# measurements: all read-only, they never change your logs
python3 evidence/incidents/measure_claude_projects.py # repeat failures across all Claude Code projects
python3 evidence/incidents/measure_persistence.py     # failing streaks, and what happened after objections
python3 evidence/incidents/measure_crossmodel.py      # the same question across models in an OpenCode db
python3 evidence/incidents/measure.py                 # incident 001 itself
```

Each script writes its `*-raw.json` next to it and prints a summary. Paths
default to the usual places and can be changed:

| Variable | Default |
| --- | --- |
| `CLAUDE_PROJECTS` | `~/.claude/projects` |
| `INCIDENT_PROJECT` | the Claude Code project folder for `~/www/dashbored` |
| `OPENCODE_DB` | `~/.local/share/opencode/opencode.db` |

Your home folder is written as `~` in the output, so a re-run doesn't record
whose machine it ran on.

## Publish

`publish.py` signs in to Ghost's Admin API, turns each Markdown file into
HTML with a small built-in converter (quotes pass through unchanged), and
creates or updates one post per file. Settings come from the environment;
copy [.env.example](.env.example) to `.env` and fill it in:

```sh
set -a; . ./.env; set +a
python3 publish.py
```

## Add a case

One incident is an anecdote. Ten is a pattern. If you have logs of your own,
open an issue or a pull request with:

- the product, model, plan and dates
- what was asked, and what was produced
- numbers counted by a script, not remembered (the scripts here are a starting point)
- what the numbers do **not** show

## Status

Live and growing. Incident 001 is complete and measured. The claims set was
collected 2026-09-23; pages change, so re-check a claim against its URL before
quoting it. The cross-model and persistence measurements are first passes:
what each one does and does not measure is at the top of its script, and the
limits of the incident itself are in section 6 of `incident-001.md`.

## License

The code is under [PolyForm Noncommercial 1.0.0](LICENSE): free to use,
change and share for any noncommercial purpose. Nobody gets to sell it.
Vendor claims are quoted verbatim for commentary and criticism, and remain
their owners' words.
