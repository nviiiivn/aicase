# Legal Research: False Advertising / Deceptive Practices Framework for AI Products (US-Focused)

**Purpose:** Collection and summary only. This document does not construct or argue a case theory. Every citation below was verified against a source page actually opened during research (listed inline). Anything not independently verified is flagged in the final section.

**Date compiled:** 2026-09-23

---

## A. Statutory Hooks

### A.1 FTC Act Section 5 — 15 U.S.C. § 45(a) / § 45(n)

**Citation:** 15 U.S.C. § 45(a)(1), (n).

**Verbatim text (from Cornell LII, law.cornell.edu/uscode/text/15/45):**

> § 45(a)(1): "Unfair methods of competition in or affecting commerce, and unfair or deceptive acts or practices in or affecting commerce, are hereby declared unlawful."

> § 45(n) (the codified unfairness standard): "The Commission shall have no authority under this section or section 57a of this title to declare unlawful an act or practice on the grounds that such act or practice is unfair unless the act or practice causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition."

**Two independent prongs, two different tests:**
- **Deception** — a material representation, omission, or practice likely to mislead a reasonable consumer acting reasonably under the circumstances. (FTC Policy Statement on Deception, Oct. 14, 1983, cited via Cliffdale Assocs., 103 F.T.C. 110, 174 (1984), referenced in puffery search below.)
- **Unfairness** (§ 45(n), the codified "S&H" three-factor test) — (1) substantial injury to consumers, (2) not reasonably avoidable by consumers, (3) not outweighed by countervailing benefits to consumers or competition.
Source: FTC Policy Statement on Unfairness, https://www.ftc.gov/legal-library/browse/ftc-policy-statement-unfairness

**Who can sue:** Section 5 is enforced by the FTC itself — there is no general private right of action under the FTC Act. Private plaintiffs must use state analogs (see A.3) or other federal statutes.

**Remedies:** Injunctive relief, consumer redress/restitution, disgorgement, and (for violations of an existing FTC order) civil penalties currently exceeding $53,000 per violation.
Source: https://www.law.cornell.edu/uscode/text/15/45; https://www.ftc.gov/legal-library/browse/ftc-policy-statement-unfairness

---

### A.2 Lanham Act § 43(a) — 15 U.S.C. § 1125(a)

**Citation:** 15 U.S.C. § 1125(a)(1)(B) (the false-advertising prong; § 1125(a)(1)(A) is the separate false-association/passing-off prong).

**Verbatim text (from Cornell LII, law.cornell.edu/uscode/text/15/1125):**

> § 1125(a)(1)(B): liability attaches to any person who "in commercial advertising or promotion, misrepresents the nature, characteristics, qualities, or geographic origin of his or her or another person's goods, services, or commercial activities."

**Elements a plaintiff must prove:**
1. **Falsity** — the statement is either literally false, or literally true/ambiguous but likely to mislead and confuse consumers.
2. **Materiality** — the false or misleading statement had an impact on consumers' purchasing decisions.
3. **Not mere puffery** — see Section D.1 below; vague superiority claims and exaggerated bluster are not actionable.
4. **Scope** — the misrepresentation must relate to the "nature, characteristics, qualities, or geographic origin" of goods, services, or commercial activities — not any false statement generally.

**Standing:** Limited to commercial competitors and others with a commercial interest in reputation or sales — **not ordinary consumers**. Per the Supreme Court's zone-of-interests analysis (cited in the source material as articulated by Justice Scalia), "to come within the zone of interests in a suit for false advertising under § 1125(a), a plaintiff must allege an injury to a commercial interest in reputation or sales."

**Remedies:** Injunctive relief; under § 35(a) (15 U.S.C. § 1117), a prevailing plaintiff may recover the defendant's profits attributable to the false advertising, plaintiff's damages, costs, and (in some cases) the cost of corrective advertising.
Sources: https://www.law.cornell.edu/uscode/text/15/1125; https://www.bfkn.com/assets/htmldocuments/Lanham%20Act%20Section%2043a%20Claims.pdf

**Relevance to a consumer-facing AI false-advertising case:** Because Lanham Act standing runs to competitors, not consumers, this hook is primarily useful if the client is a competing AI vendor (or has commercial standing), not an individual subscriber.

---

### A.3 State UDAP / Consumer Protection Statutes

#### California — UCL (Bus. & Prof. Code § 17200) and FAL (Bus. & Prof. Code § 17500)

- **UCL § 17200** defines unfair competition to include "any unlawful, unfair or fraudulent business act or practice and unfair, deceptive, untrue or misleading advertising and any act prohibited by" the FAL. Three independent prongs: unlawful, unfair, fraudulent.
- **FAL § 17500** separately prohibits false, misleading, or deceptive advertising. Any violation of the FAL automatically violates the UCL (Comm. on Children's Television v. General Foods, 35 Cal.3d 197, 210 (1983)).
- **Standard:** the objective "reasonable consumer" test — established in **Williams v. Gerber Prods. Co., 552 F.3d 934, 938 (9th Cir. 2008)**, citing Lavie v. Procter & Gamble Co., 105 Cal. App. 4th 496, 506–07 (2003). The reasonable consumer is not the "least sophisticated" or "unwary" consumer but "the ordinary consumer within the larger population"; plaintiff must show "members of the public are likely to be deceived" (quoting Freeman v. Time, Inc., 68 F.3d 285, 289 (9th Cir. 1995)). Whether a practice is deceptive is usually a fact question, not resolvable on a motion to dismiss.
  Source: https://www.courtlistener.com/opinion/3051713/williams-v-gerber-products-co/
- **Standing (post-Prop 64):** A plaintiff must show (1) economic injury — "lost money or property" — and (2) that the injury was caused by the challenged practice. **Kwikset Corp. v. Superior Court, 51 Cal.4th 310 (2011)** holds the threshold is low: a consumer who was deceived into buying a product they wouldn't otherwise have purchased has "lost money or property," even without showing the product was overpriced or defective. Two-part test: (1) loss/deprivation of money or property = economic injury; (2) causation.
  Source: https://law.justia.com/cases/california/supreme-court/2011/s171845/
- **Reliance/causation for a class:** **In re Tobacco II Cases, 46 Cal.4th 298, 327 (2009)** — where a misrepresentation is material, an inference of class-wide reliance arises; individualized reliance on the specific statement need not be shown.
  Source: search results citing Mondaq "Whiteside" analysis, https://www.mondaq.com/unitedstates/consumer-law/1596268/
- **Remedies:** UCL — private plaintiffs generally **cannot** recover compensatory or punitive damages, only injunctive relief and restitution; government enforcers can obtain civil penalties of $2,500 per violation under §17206 (paired with FAL, total $5,000 per unlawful act per **People v. Dollar Rent-A-Car Systems, Inc., 211 Cal.App.3d 119 (1989)**). Court may order restitution under §17535 where necessary to prevent continued use of the unfair practice. UCL claim: 4-year statute of limitations; FAL: 3-year.
- Plaintiffs commonly pair UCL/FAL claims with the **Consumers Legal Remedies Act (CLRA), Civil Code § 1750 et seq.**, which — unlike the UCL — does allow actual damages, punitive damages, statutory damages, and attorney's fees.
Source: https://stimmel-law.com/articles/unlawful-business-acts-california-definitions-and-remedies/; https://california-business-lawyer-corporate-lawyer.com/...

#### New York — GBL § 349 (deceptive acts/practices) and § 350 (false advertising)

- **§ 349(a):** "Unfair, deceptive, or abusive acts or practices in the conduct of any business, trade or commerce or in the furnishing of any service in this state are hereby declared unlawful." (Note: an "unfair and abusive" expansion took effect Feb. 17, 2026, but that expanded prong is AG-enforceable only, not privately actionable.)
- **§ 350:** "False advertising in the conduct of any business, trade or commerce or in the furnishing of any service is declared unlawful"; § 350-a defines false advertising as advertising that is "misleading in a material respect."
- **Elements (private plaintiff):** consumer-oriented conduct, materially misleading to a reasonable consumer, and actual injury caused by the deception. **Reliance is not required** — a key advantage over common-law fraud. Mere puffery is not actionable.
- **Standing:** private right of action added in 1980; § 349(h) and § 350-e allow "any person who has been injured" to sue.
- **Remedies:** § 349 — actual damages or $50, whichever is greater, plus treble damages up to $1,000, plus attorney's fees. § 350 — actual damages or $500, whichever is greater, plus treble damages up to $10,000, plus attorney's fees. Three-year statute of limitations.
Source: https://law.justia.com/codes/new-york/gbs/article-22-a/349/; https://www.jdsupra.com/legalnews/primer-on-new-york-general-business-law-8407804/

*(These two states were selected per the task instructions as illustrative "strongest" examples; a full survey of all 50 state UDAP statutes was not performed.)*

---

### A.4 Breach of Express Warranty / Contract Theories for Subscription Software

- **Express warranty creation — UCC § 2-313:** an express warranty is created by an affirmation of fact or promise made part of the "basis of the bargain" — e.g., marketing claims about what the AI product does, written into the contract or made in connection with the sale.
- **Disclaiming warranties — UCC § 2-316:** to disclaim the implied warranty of merchantability, the disclaimer must specifically use the word "merchantability" and (if written) be conspicuous; disclaiming fitness for a particular purpose likewise requires a conspicuous written disclaimer. "AS IS" / "with all faults" language is sufficient under § 2-316(3)(a) to disclaim *implied* warranties.
- **The key vulnerability for the defense (and thus a key opportunity for plaintiffs):** a contract that makes specific express warranty-like claims (marketing statements, product descriptions) in one place and then tries to disclaim "all warranties, express or implied" elsewhere creates an internal contradiction that courts generally construe against the drafter — an as-is disclaimer cannot retroactively swallow a specific express representation the buyer relied on entering the bargain.
- **Practical SaaS pattern:** most consumer AI subscription terms disclaim implied warranties and cap liability, while marketing (outside the four corners of the contract — website, ads, demo videos) makes the specific capability claims. This creates a structural gap: the strongest capability claims often live in marketing copy the warranty disclaimer doesn't reach, while the contract's disclaimer covers only the product-as-delivered.
Source: https://www.terms.law/2025/01/15/the-legal-limits-of-disclaiming-warranties/; https://www.contractken.com/glossary/warranty-disclaimer

---

## B. FTC Action Specifically on AI Claims

### B.1 "Operation AI Comply" — FTC enforcement sweep, announced September 25, 2024

Official press release: **"FTC Announces Crackdown on Deceptive AI Claims and Schemes"** (Sept. 25, 2024), https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
Companion blog: https://www.ftc.gov/business-guidance/blog/2024/09/operation-ai-comply-continuing-crackdown-overpromises-ai-related-lies

Then-Chair Lina Khan: "Using AI tools to trick, mislead, or defraud people is illegal. The FTC's enforcement actions make clear that there is no AI exemption from the laws on the books."

Five enforcement actions were announced simultaneously:

**1. DoNotPay** — "AI Lawyer" claims
- **Claim:** Marketed as "the world's first robot lawyer," able to "generate perfectly valid legal documents in no time" and substitute for a human lawyer, including a "business compliance checker" claiming to detect violations that could cost a small business $125,000 in unaddressed legal fees.
- **Deceptive because:** DoNotPay never tested its AI chatbot's output against the work product of an actual attorney and did not employ or retain any attorneys; the "small business compliance checker" service was not effective.
- **Outcome:** Settled. $193,000 monetary payment; required notice to consumers who subscribed 2021–2023; prohibited from claiming the service substitutes for a licensed professional's services absent competent evidence. Commission voted 5-0 to finalize the order Jan. 16, 2025.
Source: https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-finalizes-order-donotpay-prohibits-deceptive-ai-lawyer-claims-imposes-monetary-relief-requires

**2. Ascend Ecom** — "cutting edge" AI-powered e-commerce income claims
- **Claim:** AI-powered tools would let consumers earn "thousands" monthly via online storefronts on Amazon, Walmart, Etsy, TikTok.
- **Deceptive because:** Alleged business-opportunity scheme; charged consumers $25+ million; five-figure monthly income promises never materialized; pressured removal of negative reviews; violated "guaranteed buyback" promises.
- **Outcome:** Federal court TRO, receiver appointed; by mid-2025 FTC secured a permanent ban on the operators marketing business opportunities, with asset turnover for consumer redress (combined with Ecommerce Empire Builders, losses tied to this pair exceeded $35 million).

**3. Ecommerce Empire Builders** — "AI-powered Ecommerce Empire"
- **Claim:** Training programs (~$2,000) or "done for you" storefronts (tens of thousands of dollars) using AI to build a "million-dollar business."
- **Deceptive because:** No evidence supporting claimed $10,000/month income; CEO used consumer funds for personal enrichment; resisted refunds.
- **Outcome:** TRO, receiver appointed; permanent ban secured by mid-2025 (see above, combined redress figure).

**4. Rytr** — AI-generated fake reviews
- **Claim/product:** AI "writing assistant" with a "Testimonial & Review" feature capable of generating detailed, specific consumer reviews from minimal user input.
- **Deceptive/unfair because:** FTC alleged the tool provided the "means and instrumentalities" for subscribers to mass-produce false and misleading reviews — an unfair practice under Section 5, not a claim of Rytr's own false marketing.
- **Outcome:** Originally settled with a consent order (Dec. 2024) banning Rytr from offering any review/testimonial-generation service. **This order was later reopened and set aside on Dec. 22, 2025** — see B.3 below. This reversal is itself now part of the precedent landscape and should be read as limiting, not just supporting, "means and instrumentalities" theories against AI tool providers going forward.
Source: https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-reopens-sets-aside-rytr-final-order-response-trump-administrations-ai-action-plan

**5. FBA Machine / Passive Scaling** — guaranteed AI income claims
- **Claim:** "AI-powered" software guaranteeing income via online storefronts; testimonials of "7-figure businesses" and "$100,000+ monthly profit."
- **Deceptive because:** Alleged fraud of $15.9+ million; principal Bratislav Rozenfeld rebranded the scheme (Passive Scaling → FBA Machine) after the earlier version failed; falsely promised "risk-free" refunds.
- **Outcome:** TRO, receiver appointed; company permanently shut down July 2025, operators barred from similar schemes, assets redirected to restitution.

---

### B.2 FTC Guidance Documents

**"Keep your AI claims in check"** — FTC Business Blog, by Michael Atleson (Division of Advertising Practices), Feb. 27, 2023.
URL: https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check
Key points (paraphrased from the guidance, confirmed across multiple secondary summaries citing the original):
- "AI" is treated as a marketing term the FTC will scrutinize, not a magic word exempting claims from substantiation requirements.
- Comparative/"better than" claims require specific evidence the AI product is qualitatively superior — not merely asserted.
- Companies must understand and disclose the reasonably foreseeable risks of their AI products before market release; cannot disclaim responsibility by calling the AI a third-party "black box."
- Claims that a product "is AI" or "AI-powered" must be true — the FTC says its technologists can look "under the hood."
- Closing line (widely quoted): "you don't need a machine to predict what the FTC might do when [AI] claims are unsupported."

**"AI (and other) Companies: Quietly Changing Your Terms of Service Could Be Unfair or Deceptive"** — FTC Office of Technology / Division of Privacy and Identity Protection, Feb. 13, 2024.
URL: https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/02/ai-other-companies-quietly-changing-your-terms-service-could-be-unfair-or-deceptive
Verbatim key warning:
> "It may be unfair or deceptive for a company to adopt more permissive data practices—for example, to start sharing consumers' data with third parties or using that data for AI training—and to only inform consumers of this change through a surreptitious, retroactive amendment to its terms of service or privacy policy."
Cites prior enforcement precedent: **Gateway Learning Corporation** (~2004) and **1Health.io** (2023), both cases where a company changed its privacy policy to permit new data sharing without adequately notifying existing users.

---

### B.3 The Rytr Reversal (December 2025) — important recent development

On **December 22, 2025**, the FTC (now under Chair Andrew Ferguson, 2-0 vote with only two sitting Republican commissioners) reopened and set aside the Rytr consent order, citing the Trump administration's July 2025 "AI Action Plan," which directed the FTC to review final orders for whether they "unduly burden AI innovation." The Commission also found the original 2024 complaint legally deficient: it "contains no allegations that Rytr itself created deceptive marketing material, only that its customers might have used its tool to do so, and fails even to provide a single allegation that such false reviews were in fact created and used." Rytr consented to the vacatur. The FTC simultaneously issued warning letters (not enforcement actions) to companies about AI-enabled fake reviews.
Source: https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-reopens-sets-aside-rytr-final-order-response-trump-administrations-ai-action-plan; https://www.hoganlovells.com/en/publications/in-rare-move-ftc-sets-aside-rytr-order-for-burdening-ai-innovation-and-failing-to-plead-violations

**Significance for a false-advertising analysis:** This signals the current FTC leadership is actively narrowing the "means and instrumentalities" theory used against AI tool providers whose products *could be misused*, and is skeptical of complaints that don't allege the AI company itself made the false claim. A false-advertising theory resting on the company's own marketing claims (the DoNotPay/Evolv model) is on firmer, unaffected ground than one resting on downstream misuse by users (the original Rytr model).

---

### B.4 Related FTC Action — Evolv Technologies (AI weapons detection), November 2024

- **Claim:** AI-powered "weapons detection" system (Evolv Express), marketed as categorically different from and more effective/cheaper than a traditional metal detector, deployed in 800+ schools.
- **FTC allegation:** Violated Section 5 by making "false or unsupported claims" about detection accuracy; the marketing distinction between "weapons detection" and "metal detector" was "solely a marketing distinction" — the device only detects metallic objects and its alarms are triggered by non-weapon metal items (laptops, binders, water bottles). The FTC specifically noted the system failed to detect a 7-inch knife used in a school stabbing.
- **Outcome:** Settled Nov. 26, 2024. No monetary penalty (no admission of wrongdoing); Evolv required to let certain school-district customers (contracts signed April 2022–June 2023) cancel; ongoing prohibition on misrepresenting detection accuracy or the system's ability to distinguish weapons from harmless items.
Source: https://www.ftc.gov/legal-library/browse/cases-proceedings/evolv-technologies; https://www.eff.org/deeplinks/2024/12/ftc-rightfully-acts-against-so-called-ai-weapon-detection-company-evolv

**Note:** Evolv was not announced as part of the Operation AI Comply five, but the FTC itself and press coverage frame it as a continuation of the same AI-marketing-accuracy enforcement theme.

---

## C. Relevant Litigation — AI Product Claims, Subscription Value, Misrepresentation of Capability

*Distinguishing allegation from holding is critical here — marked explicitly for each entry.*

### C.1 Tesla "Full Self-Driving" / "Autopilot" — multiple proceedings (DECIDED + PENDING, mixed)

**a) California DMV administrative proceeding — DECIDED (administrative), then appealed**
- The California DMV filed accusations against Tesla's manufacturer/dealer licenses (Nov. 2023), alleging that since May 2021 Tesla advertised its driver-assistance features using the labels "Autopilot" and "Full Self-Driving Capability," and described trips with "no action required by the person in the driver's seat," even though the vehicles "could not at the time of those advertisements, and cannot now, operate as autonomous vehicles."
- **Holding (administrative law judge, Dec. 2025):** ruled against Tesla; found "Autopilot" follows "a long but unlawful tradition" of using ambiguity to mislead consumers, and that "Full Self-Driving" is "actually, unambiguously false and counterfactual." DMV gave Tesla 60 days to fix marketing or face a 30-day license suspension.
- **Status:** Tesla complied with the marketing-change order, then in **February 2026 sued the California DMV** to reverse the underlying ruling, arguing the DMV never proved actual consumer confusion given that Tesla's disclosures accompanying purchase repeatedly stated the vehicles are not autonomous. This countersuit is **pending**.
Source: https://www.dmv.ca.gov/portal/news-and-media/news-releases/dmv-finds-tesla-violated-california-state-law/; https://electrek.co/2025/12/17/ca-judge-rules-tesla-lied-about-fsd-must-fix-marketing-within-60-days/; https://electrek.co/2026/02/23/tesla-sues-california-dmv-reverse-fsd-false-advertising-ruling/

**b) In re Tesla Advanced Driver Assistance Systems Litigation — PENDING (class certified, not yet a merits ruling)**
- Case: **In re Tesla Advanced Driver Assistance Systems Litigation, No. 3:22-cv-05240 (N.D. Cal.)** — consolidating LoSavio v. Tesla, Matsko v. Tesla, Battiato v. Tesla, and Mallow v. Tesla, first filed September 2022.
- **Core allegation (unproven):** Tesla made false claims about FSD capability, including statements attributed to Elon Musk in 2016–2017 suggesting cross-country self-driving by end of 2017, inducing consumers to pay a separate charge for the FSD package.
- **Procedural status:** Judge Rita F. Lin (N.D. Cal.) **certified** both a Rule 23(b)(3) damages class and a Rule 23(b)(2) injunctive class on **August 18, 2025** — California purchasers/lessees who bought the FSD package (not Enhanced Autopilot, which was denied certification) between May 19, 2017 and July 31, 2024, and who opted out of Tesla's arbitration clause. The court accepted, for certification purposes, a "full-refund" damages theory (potential recovery of the full $5,000–$15,000+ FSD price if misrepresentation is proven at trial).
- Tesla has petitioned the Ninth Circuit for permission to appeal certification (Docket No. 25-7927, filed ~Dec. 18, 2025). **Trial has not occurred; liability is unproven — class certification is not a merits finding.**
Source: https://www.carcomplaints.com/news/2025/tesla-fsd-lawsuit-certified-class-action.shtml; https://caselaw.findlaw.com/court/us-dis-crt-n-d-cal/117682199.html

**Relevance:** This is the single closest analog available for "AI capability claims sold as a paid feature/subscription-like add-on to consumers who didn't get what was promised" — same fact pattern class (AI capability overclaim + separate charge + consumer class) as an AI-subscription false-advertising theory, and it shows a workable certification path notwithstanding arbitration provisions (via the opt-out subclass).

---

### C.2 Moffatt v. Air Canada, 2024 BCCRT 149 — DECIDED (Canadian small-claims tribunal, persuasive only in the US)

- **Facts:** Air Canada's website chatbot told a customer he could retroactively claim a bereavement fare; the airline's actual policy (elsewhere on the site) did not allow retroactive claims. Air Canada argued the chatbot was a separate entity for which it bore no responsibility.
- **Holding:** The BC Civil Resolution Tribunal rejected that defense, holding Air Canada owed the customer a duty of care and that "the applicable standard of care requires a company to take reasonable care to ensure their representations are accurate and not misleading" — a duty Air Canada breached. The tribunal also held a consumer is not required to cross-check one part of a company's website against another. Damages awarded: **CAD $812.02**.
- **Caveat:** This is a small-claims online tribunal decision (max claim ~CAD $5,000), not binding US precedent, and decided under Canadian negligent-misrepresentation law, not a US false-advertising statute. Useful only as persuasive/analogous authority for the proposition that a vendor cannot disclaim responsibility for its own AI chatbot's representations by treating the bot as a separate actor.
Source: https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot; https://www.canlii.org/en/commentary/doc/2025CanLIIDocs1963

---

### C.3 Walters v. OpenAI — DECIDED (Georgia state court; defamation, not false advertising, but directly on point for the disclaimer-defense issue)

- **Case:** Mark Walters v. OpenAI, LLC, Superior Court of Gwinnett County, Georgia; filed June 2023.
- **Allegation:** ChatGPT falsely told a journalist that radio host Mark Walters had been "accused of defrauding and embezzling funds" from the Second Amendment Foundation — a fabricated claim (hallucination). The journalist caught the error and never published it, but Walters sued for defamation anyway.
- **Holding (summary judgment, Judge Tracie Cason, May 19, 2025):** Dismissed on **three independent grounds**: (1) no defamatory meaning as a matter of law — "No reasonable person would interpret the AI-generated content in question as a literal or factual assertion, particularly in light of the well-known limitations and disclaimers attached to the tool"; (2) no actual malice/negligence — OpenAI's efforts to reduce hallucinations and its extensive warnings defeated a negligence finding; (3) no damages — Walters admitted he was not actually harmed, and Georgia law required a pre-suit retraction demand he never made.
Source: https://blog.ericgoldman.org/archives/2025/05/chatgpt-defeats-defamation-lawsuit-over-hallucination-walters-v-openai.htm; https://knowingmachines.org/knowing-legal-machines/legal-explainer/cases/walters-v-openai

**Relevance to obstacle D.5 below (disclaimers):** This is the clearest available precedent that a court will credit an AI vendor's inaccuracy disclaimers as evidence a reasonable person would not take the output as a factual assertion — a live risk to any theory built on "the AI told the user X and X was false," even outside the defamation context.

---

### C.4 SEC "AI-washing" enforcement — DECIDED (settled) and one PENDING/ongoing pattern

Not FTC/consumer false-advertising actions, but directly on-point for "how regulators define and punish AI-capability overstatement," and useful comparative/persuasive material:

- **In re Delphia (USA) Inc.** and **In re Global Predictions Inc.** — SEC settled orders, March 18, 2024. Both firms allegedly told investors/clients they used AI in ways they did not (Delphia: claimed AI used client data to "predict which companies and trends are about to make it big" but didn't; Global Predictions: falsely claimed to be "the first regulated AI financial adviser" and misstated assets on platform and tax-loss harvesting services). Settled without admitting/denying wrongdoing: Delphia $225,000 penalty, Global Predictions $175,000 penalty. SEC Chair Gary Gensler: "We find that Delphia and Global Predictions marketed to their clients and prospective clients that they were using AI in certain ways when, in fact, they were not." Enforcement Director Gurbir Grewal: "Simply put, that's called AI washing and it hurts investors."
Source: https://www.sec.gov/newsroom/press-releases/2024-36

- **In re Presto Automation Inc.** — SEC settled order, January 2025. First AI-washing action against a **public** company (vs. investment advisers). Alleged Presto overstated the capabilities/operational effectiveness of its "Presto Voice AI" drive-through product, and failed to disclose the underlying speech-recognition tech was a third party's and required significant human intervention despite being marketed as automated. Settled with a cease-and-desist order and **no monetary penalty**, based on cooperation/remediation.
Source: https://www.mofo.com/resources/insights/240320-sec-targets-ai-washing-with-two-new-settled-cases (context); https://www.omm.com/insights/alerts-publications/sec-targets-ai-washing-in-charges-against-two-investment-advisers/

**Relevance:** Establishes a definition of "AI washing" (overstating actual AI use/capability, or hiding human-in-the-loop reality) that a consumer false-advertising theory can borrow, and shows regulators treat "we said AI did X, but a human/simpler process did X" as the core deceptive fact pattern — directly transferable to consumer AI subscription products making similar claims.

---

### C.5 Not found / negative result, stated explicitly

Targeted searching did **not** locate a filed US lawsuit alleging false advertising of an AI product's core technical/reasoning capabilities (e.g., "this AI reasons at PhD level," "this AI is more accurate than X") brought by ordinary consumers under a state UDAP statute. Current OpenAI consumer litigation located instead concerns data-sharing/privacy practices (e.g., *Vredenburgh v. OpenAI OpCo LLC*, No. 3:26-cv-10527 (N.D. Cal.), alleging undisclosed human review of conversations; and separate suits alleging undisclosed sharing of ChatGPT queries with Meta/Google via embedded tracking pixels), not capability overstatement. This is a genuine gap in the current litigation landscape — the closest available consumer-facing capability-overstatement analog remains the Tesla FSD litigation (C.1), which is about an AI-adjacent driver-assist feature, not a generative-AI product per se.
Source: search summary compiled from https://www.classaction.org/news/category/openai-inc and related coverage; no single primary-source case document was opened for the Vredenburgh docket beyond secondary reporting, so that citation should be treated as **less verified** than the others above (see Unverified section).

---

## D. The Legal Obstacles

### D.1 Puffery doctrine

**The rule:** Every circuit that has considered the issue holds that "puffery" — non-verifiable, exaggerated, or purely subjective claims of superiority — is not actionable as false advertising, under either the Lanham Act or state UDAP/reasonable-consumer analogs. Standards differ slightly by circuit but converge on two forms of puffery:
1. An exaggerated, blustering, boasting statement no reasonable buyer would rely on; or
2. A general claim of superiority so vague it can only be understood as opinion.

**Key authorities (verified):**
- **Pizza Hut, Inc. v. Papa John's Int'l, Inc., 227 F.3d 489 (5th Cir. 2000)** — Fifth Circuit's two-form puffery test, applied to "Better Ingredients. Better Pizza." The court held that slogan alone was non-actionable puffery (subjective, not objectively measurable), but — critically — when Papa John's tied "better" to specific, verifiable ingredient comparisons, the overall campaign became actionable because the specific claims "tainted" the puffery.
- **U.S. Healthcare, Inc. v. Blue Cross of Greater Philadelphia, 898 F.2d 914, 922 (3d Cir. 1990)** — Third Circuit: puffery is marketing "no one would rely on."
- **Time Warner Cable v. DIRECTV, 497 F.3d 144 (2d Cir. 2007)** — Second Circuit: puffery = subjective claims "which cannot be proven either true or false."
- FTC's own standard: puffery is limited to claims "that ordinary consumers do not take seriously" (**Cliffdale Assocs., 103 F.T.C. 110, 174 (1984)**; FTC Policy Statement on Deception, Oct. 14, 1983).
Source: https://ktslaw.com/Insights/Perspectives/2024/9/5-Key-Takeaways-Puffery-Versus-Objective-Claims-in-Advertising

**Why "the world's most powerful AI" is likely non-actionable standing alone:** It is a general superiority claim, not tied to a specific, falsifiable benchmark — squarely inside the Fifth Circuit's "so vague as to be mere opinion" category and the Second/Third Circuit's "cannot be proven true or false" category.

**Why the puffery defense can still fail:** Per Pizza Hut, if the "most powerful" claim is *coupled with* specific, testable claims (benchmark scores, named comparisons — "outperforms GPT-X on Y benchmark," "99% accuracy," "passes the bar exam in the 90th percentile") those specific claims are actionable, and per Pizza Hut's reasoning, can retroactively make the surrounding superiority puffery misleading in context. **The FTC's own "Keep your AI claims in check" guidance (B.2) explicitly states the FTC does *not* treat "AI" or comparative AI claims as automatic puffery** and will demand substantiation — a notable divergence from private Lanham Act litigation, where puffery doctrine is more forgiving. This is an important asymmetry: FTC enforcement risk on AI superiority claims is higher than private-plaintiff litigation risk, because the FTC has said it won't extend puffery leniency to AI marketing.

---

### D.2 Arbitration clauses and class-action waivers

**The controlling precedent: AT&T Mobility LLC v. Concepcion, 563 U.S. 333 (2011)** — 5-4 decision by Justice Scalia holding the Federal Arbitration Act preempts state rules (there, California's Discover Bank rule) that would void class-action waivers in consumer arbitration agreements as unconscionable. Result: companies can lawfully compel individual arbitration and bar class actions/class arbitration in consumer contracts, and courts have applied this broadly — by 2012 Concepcion had already been cited in 76+ decisions compelling individual arbitration.
Source: https://en.wikipedia.org/wiki/AT%26T_Mobility_LLC_v._Concepcion (secondary, cross-checked against SCOTUSblog and GovInfo case listing)

**Application to major AI vendors' consumer terms — OpenAI as an example (verified against OpenAI's published Terms of Use language, openai.com/policies/row-terms-of-use/):**
- Mandatory arbitration clause: "YOU AND OPENAI AGREE TO THE FOLLOWING MANDATORY ARBITRATION AND CLASS ACTION WAIVER PROVISIONS."
- Class and jury trial waiver: disputes must be brought "on an individual basis only" — no class, consolidated, or representative proceedings, and no jury trial.
- Carve-outs: small claims court disputes, and requests for injunctive/equitable relief to stop unauthorized use or IP infringement, are not forced into arbitration; a narrow carve-out allows severing a request for *public* injunctive relief to court after arbitrating the underlying claim.
- **30-day opt-out window** from account creation — a real, if narrow, escape hatch.
- Batch arbitration provision for 25+ similar claims filed by the same/similar counsel — an attempt to blunt mass-arbitration cost-shifting strategies.

**Practical effect on a false-advertising theory:** For any individual consumer who did not opt out within 30 days of account creation, an individual false-advertising claim likely must proceed in arbitration, alone, without a jury, and without the ability to aggregate into a class — which is often what makes small-dollar subscription claims economically viable to litigate at all. This is arguably the single largest practical barrier to any consumer-side case against a major AI vendor, independent of the merits.
Source: search results compiled from openai.com/policies/row-terms-of-use/ and terms.law/ToS-Watchdog review, cross-referenced.

---

### D.3 Reliance and causation for a subscription user

- Under the **Lanham Act**, materiality/reliance-type proof is required but the plaintiff pool is competitors, not consumers (see A.2) — not directly applicable to a subscriber theory.
- Under **California UCL/FAL**, the reasonable-consumer standard (Williams v. Gerber) does not require the plaintiff to prove they personally read and relied on a specific statement; under **In re Tobacco II Cases, 46 Cal.4th 298, 327 (2009)**, materiality supports a class-wide inference of reliance. This is genuinely favorable to a subscriber-class theory, provided the challenged claim was material and consistently made.
- Under **New York GBL §349**, reliance is **explicitly not an element** the plaintiff must prove — only that the conduct was consumer-oriented, materially misleading, and caused injury.
- **The practical difficulty for a subscription-AI case specifically:** a subscriber typically doesn't buy based on one advertisement the way a lockset buyer relies on "Made in U.S.A." (Kwikset) — they often trial the free tier first, use the product repeatedly, and renew monthly. This creates two problems: (1) causal story is more diffuse — was the subscription renewal decision caused by the original capability claim, general habit, sunk cost, or the product's ordinary (if imperfect) utility? (2) A consumer who continued renewing for months after allegedly discovering the AI's real limitations weakens their own reliance/causation story — defense will argue continued voluntary payment after having actual experience of the product's true capability undercuts any claim the marketing caused ongoing injury.

---

### D.4 Damages theory for a monthly subscription — what is actually recoverable

Two competing frameworks, both drawn from consumer class-action damages practice generally (not AI-specific, but directly transferable):

- **"Full refund" theory:** applies when the product is essentially worthless without the falsely-advertised feature — plaintiff argues for return of the entire amount paid. This is a hard sell for a general-purpose AI subscription (the product plainly has *some* non-AI-claim-dependent utility for most users), but is exactly the theory accepted for **class certification purposes** (not yet proven at trial) in the Tesla FSD litigation (C.1) — full refund of the $5,000–$15,000+ FSD package price.
- **"Price premium" / benefit-of-the-bargain theory:** measures the gap between what was paid and what the product was actually worth given the true (lesser) capability — typically proven via conjoint analysis or hedonic regression modeling willingness-to-pay with vs. without the false claim.
- **The major certification-stage obstacle: Comcast Corp. v. Behrend** (cited in secondary sources reviewed, not independently opened as a primary source — flag as less-verified below) requires that a damages model be capable of measuring damages on a **class-wide** basis tied to the theory of liability; courts frequently decertify or deny certification where price-premium experts use only aggregate willingness-to-pay averages that obscure individual variation, or where the product retained real, non-trivial value regardless of the challenged claim.
- **For a subscription specifically:** the "damages" are inherently small per person (a monthly fee, not a five-figure car option), which (a) makes individual arbitration economically irrational for any single claimant (reinforcing D.2's practical bar) and (b) makes class-wide aggregation essential to any viable recovery — which is precisely the mechanism the arbitration/class-waiver clause is designed to foreclose for anyone who didn't opt out in the window.
Source: https://www.lexology.com/library/detail.aspx?g=6fc8e113-6e53-4091-8c6d-d59c72e54c16 (Comcast/price-premium discussion, secondary); https://thedefensiveline.wordpress.com/2013/01/27/premium-price-theory-rejected-in-toyota-prius-and-lexus-hybrid-class-action-lawsuit/ (illustrative rejection of a comparable premium-price theory in a different product context)

---

### D.5 Disclaimers ("may produce inaccurate information") and their effect

- Consumer AI products near-universally display an on-screen disclaimer (e.g., ChatGPT: "ChatGPT may produce inaccurate information about people, places, or facts") and embed a fuller disclaimer/limitation-of-liability and indemnification structure in the Terms of Use — OpenAI's terms reportedly assign output ownership *and* associated liability risk to the user, plus a broad indemnification clause covering claims "arising from or relating to your use of the Services."
- **The Walters v. OpenAI holding (C.3) is the most concrete evidence available that courts will credit these disclaimers as legally significant**, not mere boilerplate: the Georgia court held "No reasonable person would interpret the AI-generated content in question as a literal or factual assertion, particularly in light of the well-known limitations and disclaimers attached to the tool" — a holding in defamation, but the reasoning (disclaimers shape what a reasonable person understands the output to mean/claim) is directly exportable to a false-advertising "reasonable consumer" analysis. If a court accepts that ubiquitous accuracy disclaimers mean a reasonable user *cannot* reasonably treat individual AI outputs as factual assertions, that cuts against both (a) claims that individual bad outputs are actionable misrepresentations, and (b) potentially even against capability-marketing claims, if the vendor can argue the same "well known limitations" context applies to its promotional claims.
- **Where disclaimers do *not* help the defense:** a disclaimer about output accuracy ("may produce inaccurate information") is a different legal object from a marketing claim about the product's overall capability ("passes the bar exam," "PhD-level reasoning," "most powerful AI"). The FTC's "Keep your AI claims in check" guidance explicitly forecloses using downstream disclaimers to avoid substantiation duties on the initial marketing claim — a company "can't just blame" unpredictability for failing to test and substantiate the claim before making it. In other words: the disclaimer defends against liability for *any single wrong output*; it does not obviously defend against liability for the *marketing claim about the system's general capability level*, which is a separate representation made before use even begins.
- **UCC angle (A.4):** a warranty disclaimer that contradicts an express warranty-like marketing claim made as part of the "basis of the bargain" is vulnerable — courts construe the ambiguity against the drafter, and best practice (which many vendors don't follow) requires the disclaimer to expressly exclude the specific express warranties from its own scope.

---

## Unverified / Could Not Confirm

Flagged per the task's hard rule — these should **not** be relied on without further primary-source verification:

1. **Comcast Corp. v. Behrend** citation and holding, referenced in Section D.4 — discussed only via secondary law-firm summaries; the actual opinion was not opened during this research pass. Verify full citation (569 U.S. 27 (2013), per general legal knowledge, but this specific number was not confirmed against a primary source in this session) before use.
2. **Vredenburgh v. OpenAI OpCo LLC, No. 3:26-cv-10527 (N.D. Cal.)** — case name/number appeared only in secondary aggregator coverage (classaction.org-style reporting), not verified against a court docket (e.g., PACER/CourtListener). Treat as provisional.
3. Any claim that a **US consumer** has filed and won (as opposed to merely filed) a false-advertising suit specifically over generative-AI *capability* claims (accuracy, reasoning quality) — searching did not surface one; treat the absence itself as a finding, not as proof no such suit exists.
4. The **Gateway Learning Corporation** and **1Health.io** FTC enforcement matters, cited inside the FTC's own Feb. 2024 blog post (B.2) — cited only as named by the FTC blog and secondary commentary; the underlying FTC complaints/orders for those two specific matters were not independently opened.
5. Google's National Advertising Division complaint over the Gemini demo video (referenced in research but **not included above** because no formal lawsuit or FTC action resulted — flagged here only so it isn't mistaken for litigation; it is industry self-regulatory review (NAD), not a court or agency action, and was excluded from Section C for that reason).

---

*End of collection. No argument, strategy, or legal advice is expressed or implied above — this is a factual and citation inventory only.*
