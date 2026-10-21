# The numbers they advertise, and who measured them

Vague claims are legally safe. "The world's most powerful AI" is puffery —
courts treat it as opinion and nobody can sue over it.

Numbers are different. A number is a representation of fact. It can be
substantiated or it cannot. **30 of the 80 marketing claims collected for
this site carry a hard number**, and those are the ones that matter.

Here they are, verbatim, with the paid tier they are attached to.

## Productivity claims

> **"developers who used GitHub Copilot completed the task significantly
> faster–55% faster than the developers who didn't use GitHub Copilot"**
> — [github.blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

> **"up to 55% more productive at writing code without sacrifice to quality"**
> — [github.com/features/copilot/plans](https://github.com/features/copilot/plans), Copilot Pro, $10/user/month

> **"developers who use GitHub Copilot report up to 75% higher satisfaction
> with their jobs than those who don't"**
> — same pricing page

> **"94% said they considered themselves more productive overall thanks to
> Copilot"**
> — [github.com customer story](https://github.com/customer-stories/grupoboticario)

> **"The group that used GitHub Copilot had a higher rate of completing the
> task (78%, compared to 70%)"** — github.blog

**Who ran that study: GitHub.** About GitHub Copilot. Published on GitHub's
blog. That is not a disqualification — vendors are allowed to study their own
products — but it is a material fact about the evidence, and the $10/month
pricing page cites the number without it.

Note also what the 55% figure actually measured. Not a quarter of shipped
work. Not a codebase. **One task**, in a controlled setting, timed. The
marketing copy carries the number forward without the task.

Note the third claim too. "94% **said they considered themselves** more
productive" is a measurement of belief, not of output. It is quoted here
exactly as written because the wording is the point.

## Benchmark claims

> **Google:** "Gemini 3 Pro significantly outperforms 2.5 Pro on **every**
> major AI benchmark." · "It tops the LMArena Leaderboard with a breakthrough
> score of 1501 Elo." · "It greatly outperforms 2.5 Pro on SWE-bench Verified
> (76.2%)" — [blog.google](https://blog.google/products-and-platforms/products/gemini/gemini-3/)

> **OpenAI:** "On Humanity's Last Exam... scores a new pass@1 SOTA at 41.6."
> · "On BrowseComp... set a new SOTA with 68.9%"
> — [openai.com](https://openai.com/index/introducing-chatgpt-agent/)

> **Anthropic:** "Set to a medium effort level, Opus 4.5 matches Sonnet 4.5's
> best score on SWE-bench Verified, but uses 76% fewer output tokens."
> · "Opus 4.5 stays on track over the long haul earning 29% more than
> Sonnet 4.5 on Vending-Bench."
> — [anthropic.com](https://www.anthropic.com/news/claude-opus-4-5)

> **Amazon:** "agentic capabilities have achieved the highest scores on the
> SWE-Bench Leaderboard and Leaderboard Lite."
> — [aws.amazon.com](https://aws.amazon.com/q/developer/), Pro tier, $19/user/month

Every one of these is a real, checkable number. None of them is puffery. And
none of them measures the thing a subscriber is actually buying, which is
whether the product finishes their work.

**The gap that matters:** a benchmark task is scored on whether the final
answer is right. It is not scored on whether the system spends 42 hours and
336,627 tokens discovering the task was impossible. A model can top SWE-bench
Verified and still have no mechanism for stopping. Those are orthogonal
properties, and only one of them is advertised.

## The multiplier claims

> **Anthropic:** "Choose 5x or 20x more usage than Pro" — Max, from $100/month
> **OpenAI:** "5x or 20x more usage" — Pro, from $200/month
> **Google:** "4x access to Gemini" ($19.99) · "up to 20x access" ($99.99)

Three vendors, the same ladder, the same multipliers. What is sold at the top
of every one of these is **more of the thing running unattended** — which is
only worth paying for if unattended running produces work.

## Why this section exists

Because "it didn't feel useful" is not a legal claim and never will be. "This
page said 55% and attached it to a $10/month subscription" is a
representation of fact, and representations of fact have to be substantiable.

The FTC has stated directly that "AI" is not a magic word exempting claims
from substantiation, and that comparative capability claims need evidence.
That guidance is the reason the numbers matter more than the adjectives.

---

*All 30 quantified claims, with URLs and access dates, are in
`evidence/claims/*.json`. 16 further claims could not be verified from a live
page and are listed there as unverified with reasons — including that
openai.com returns HTTP 403 to automated access, so those claims were taken
from Wayback Machine snapshots and are marked as such.*
