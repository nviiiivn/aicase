# "55% faster" — and the study that found 19% slower

GitHub's pricing page sells Copilot Pro at $10/user/month with this number
attached:

> **"up to 55% more productive at writing code without sacrifice to quality"**
> — [github.com/features/copilot/plans](https://github.com/features/copilot/plans)

The number is real. It comes from a real paper: Peng, Kalliamvakou, Cihon and
Demirer, *The Impact of AI on Developer Productivity: Evidence from GitHub
Copilot*, [arXiv:2302.06590](https://arxiv.org/abs/2302.06590). The abstract
says, verbatim:

> "Recruited software developers were asked to implement an HTTP server in
> JavaScript as quickly as possible. The treatment group, with access to the
> AI pair programmer, completed the task **55.8% faster** than the control
> group."

**Read what was measured.** 95 developers. **One task.** Write a single HTTP
server in JavaScript, from scratch, against the clock, auto-graded. The 95%
confidence interval on the speed gain runs from **21% to 89%** — enormous
spread even inside that one task. Three of the four authors were at Microsoft,
GitHub and GitHub respectively, studying GitHub's own product.

None of that is fraud. It is a legitimate study of a narrow thing. The problem
is what happens to the number afterwards: it is lifted onto a pricing page,
stripped of the task, and sold to people doing maintenance work in codebases
they already know.

## What happened when someone measured that instead

METR — an independent nonprofit, not a vendor — ran a randomized controlled
trial on exactly that population.
[arXiv:2507.09089](https://arxiv.org/abs/2507.09089). **16 experienced
developers, 246 real tasks, in mature open-source repositories they averaged
five years of prior experience on.**

Their finding, verbatim from the paper:

> "Before starting tasks, developers forecast that allowing AI will reduce
> completion time by 24%. After completing the study, developers estimate that
> allowing AI reduced completion time by 20%. Surprisingly, we find that
> allowing AI actually **increases completion time by 19%**—AI tooling slowed
> developers down."

They believed they were ~20% faster. They were measurably ~19% slower. **A
39-percentage-point gap between belief and measurement, on the same tasks, by
the same people.**

That is the finding this entire site exists to point at. Not "AI is bad" —
*people cannot tell when it is costing them time.* Which is precisely why "94%
said they considered themselves more productive" is not evidence of anything.
Self-report is the exact instrument the METR trial showed to be unreliable.

**In fairness, and because this site does not hide inconvenient data:** METR's
larger follow-up (57 developers, 143 repositories, 800+ tasks) found **−4%,
CI −15% to +9%** — no longer a clear slowdown. METR also reported it had to
change the design, because "30% to 50% of developers told us that they were
choosing not to submit some tasks because they did not want to do them without
AI." Their own conclusion is that AI likely helps by 2026, but that they can no
longer measure the magnitude reliably. The honest summary: **the vendor's 55%
does not survive contact with real work, and nobody has since produced a
rigorous number that supports it.**

## The benchmarks are worse

Every vendor advertises benchmark scores. Three independent findings:

**SWE-Bench+** ([arXiv:2410.06992](https://arxiv.org/abs/2410.06992)) filtered
solution leakage and weak tests out of SWE-bench and found **32.67% of
"successful" patches came from leaked solutions** and **31.08% from inadequate
tests**. After filtering, SWE-Agent+GPT-4's resolution rate fell from **12.47%
to 3.97%**.

**OpenAI audited its own results.** Of 138 SWE-bench Verified problems its o3
model failed, **59.4% turned out to have broken tests or broken problem
statements** — not model failures. OpenAI subsequently stopped reporting the
benchmark.

**"The SWE-Bench Illusion"**
([arXiv:2506.12286](https://arxiv.org/abs/2506.12286)) found models reproducing
memorised solutions rather than reasoning to them.

So when Google writes "outperforms 2.5 Pro on SWE-bench Verified (76.2%)" and
Amazon writes "highest scores on the SWE-Bench Leaderboard," those numbers are
accurate *and* measure a benchmark whose own publisher walked away from it.

## The behaviour has a name in the literature

It is not only one user's experience:

- **"When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM
  Agents"** — defines the failure as structural: an agentic feedback path that
  repeatedly triggers costly actions with no effective stopping bound. Across
  68 documented failures, **all shared one root cause: the repeated path
  lacked a bound.**
- **MIRAGE-Bench** — observes agents falling into repetitive loops,
  persistently executing the same incorrect action, "whereas humans tend to
  revise their plans after failed attempts."
- **Sharma et al., *Towards Understanding Sycophancy in Language Models***
  ([arXiv:2310.13548](https://arxiv.org/abs/2310.13548)) — five frontier
  assistants from OpenAI, Anthropic and Meta all exhibit sycophancy, traced to
  biases in the human preference data used in training. One documented form:
  reversing a correct answer when the user expresses doubt.

The stopping problem is a known, named, published research area. It appears on
no pricing page.

## What this adds up to

The marketing sells autonomy: *works independently, handles work that runs for
hours or days, complete tasks from start to finish.*

The independent literature says: agents do not reliably stop, benchmarks
overstate capability, developers cannot perceive their own slowdown, and the
one rigorous RCT on experienced developers doing real work measured a
**slowdown**.

Those two descriptions are of the same product.

---

*Full citations, methodology notes, conflicts of interest, and a list of six
sources that could **not** be verified are in
`research/published-findings.md`. 18 sources were confirmed by opening them
directly.*
