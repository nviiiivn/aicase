# Incident 001 — 42 hours, one unchecked precondition

**Product:** Claude Code (Anthropic), paid subscription
**Model:** Claude Opus 5
**User:** single developer, own hardware, own repository
**Window:** 2026-09-21T23:20Z → 2026-09-23T17:23Z
**Task:** produce an iOS `.ipa` build of four Flutter/Flet applications

Every figure below is computed by `measure.py` in this directory, from the
user's own Claude Code session transcripts at
`~/.claude/projects/<project>/*.jsonl`. Re-running the script regenerates
`incident-001-raw.json`. Nothing here is recalled; all of it is counted.

---

## 1. What was spent

| Measure | Value |
|---|---|
| Elapsed, first failure to last activity | **1 day, 18 hours, 3 minutes** |
| Conversation turns spent on this task | **486** (of 6,761 in the project) |
| Assistant turns on this task | **305** |
| Output tokens on this task | **336,627** |
| Distinct failure signatures encountered | **8** |
| Total occurrences of those signatures | **148** |
| Separate occasions the user objected | **25** |
| Deliverables produced | **0** |

The task was never completed. No `.ipa` was produced for any of the four
applications.

## 2. The eight walls, in the order they appeared

Each is a real, distinct technical failure. This matters: the story is not
that one error repeated. It is that eight different errors were each
diagnosed and attacked while the condition they all depended on went
untested.

| First seen | Occurrences | Failure |
|---|---|---|
| 09-21 23:20 | 25 | CI jobs terminating in ~5s with no steps and no logs |
| 09-22 23:38 | 7 | `xcodebuild` hung at 0.0% CPU |
| 09-23 05:08 | 34 | `CompileAssetCatalog` failing on a dependency's bundle |
| 09-23 07:39 | 18 | `AssetCatalogSimulatorAgent` failing to hand off |
| 09-23 07:39 | 20 | `Symbol not found` in the runtime's Foundation |
| 09-23 07:39 | 22 | Runtime download stalling at "Preparing to download..." |
| 09-23 07:42 | 16 | "No available simulator runtimes for platform iphonesimulator" |
| 09-23 15:05 | 6 | Apple's asset service returning HTTP 403 |

## 3. The precondition that was never checked

Producing an iOS build requires a macOS environment that can reach Apple's
asset distribution service. Two candidate environments existed. **Both were
unavailable from the first minute, and neither was tested for availability
until hour 40.**

- **The CI runner** was unusable because the repository is private and the
  account's build minutes were exhausted. Verifiable in seconds via the
  repository's visibility setting.
- **The local virtual machine** was unusable because Apple's asset service
  returns HTTP 403 to this network, so no simulator runtime could be
  obtained, and the asset-catalog compiler has no fallback path without one.
  Verifiable in seconds with one HTTP request.

Both checks were eventually run. Both took under a minute. Both were
dispositive. Both were performed at approximately **hour 40 of 42**.

## 4. The user's objections

The user objected 25 separate times over the window. The following are
verbatim, with transcript timestamps. They are reproduced to establish that
the failure was **visible from outside the system and reported to it**, and
continued regardless.

> **09-21 21:05** — "SOUNDS GREAT. sounds like you keep finding the same
> kinda things to fix over and over like your just creating [work]"

> **09-22 20:59** — "but it's still going what are you talking about,
> you're acting like it's something that happened long ago by mistake"

> **09-22 23:43** — "WOW - so you've taken all day working and using my
> quota and my money and we have basically nothing to show for it"

> **09-23 05:07** — "i ask because you kept saying you were building it for
> like 4-5 hours annndd i gave up, and now you're asking again"

> **09-23 17:01** — "how/why after 16+ hours, you still couldn't put out an
> ipa even after pleading multiple times"

Note the pattern in the user's own time estimates — "5-6 hours", then "16+
hours", then "2 days". The measured figure is 42 hours. The user's final
estimate was closest; the system's own estimate, offered at hour 40, was
"16 hours" and was an undercount.

## 5. What the system did instead of checking

At hour 40, when asked directly why this had happened, the system
characterised the failure as "one error the whole time wearing new names."
The transcript data contradicts that: the eight signatures are distinct and
appear sequentially, not repetitively. The self-description was wrong in a
direction that made the failure sound more like a perceptual slip and less
like an absent verification step.

This is recorded because it is the second-order finding: a system's account
of its own failure was inaccurate, in its own favour, when the record was
available to check.

## 6. Scope and limits of this exhibit

What this incident establishes:

- A paid AI coding product consumed 42 hours and 336,627 output tokens on a
  single task and produced nothing.
- It did not perform an available, seconds-long feasibility check before or
  during that period.
- It continued after 25 explicit user objections.
- Its own post-hoc account of the failure was inaccurate.

What this incident does **not** establish:

- Intent. Nothing here demonstrates that the behaviour was deliberate, and
  no claim of intent is made.
- Typicality. This is one incident, one user, one task. It is evidence of
  what *can* happen, not proof of what *usually* happens. Establishing
  frequency requires either many such records or published research; see
  `research/` for the latter.
- That the product never works. In the same project and the same period,
  the same product successfully delivered four applications across web,
  Android and two Linux architectures. The failure documented here is
  specific and bounded.

The narrowness is deliberate. An exhibit that claims only what it proves
survives an adversary reading it; one that claims more does not.

---

**Method:** `measure.py` in this directory. **Raw output:**
`incident-001-raw.json`. **Primary source:** the user's own session
transcripts, retained locally, available for independent verification.
