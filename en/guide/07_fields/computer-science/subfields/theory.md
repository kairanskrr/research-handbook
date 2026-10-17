# Theory

> This page covers only what is specific to this area. For general practice, see the chapters of Parts 1 and 2 and the research strategies. For the conventions shared across computer science, see the [computer science field overview](../README.md). For how to do, write, and check proofs, see [Theoretical research](../practices/theoretical_research.md); this page does not repeat it.

## What this area studies

Theoretical computer science studies computation itself: what can be computed efficiently, what cannot be computed at all, and what it costs. Take the call for papers of STOC 2026 (the ACM Symposium on Theory of Computing): typical topics include algorithms and data structures, computational complexity, randomness in computing, approximation algorithms, cryptography, computational learning theory, optimization, economics and computation, parallel and distributed algorithms, and quantum computing[^stoc2026cfp-e10]. STOC is sponsored by SIGACT, the Special Interest Group on Algorithms and Computation Theory of ACM (the Association for Computing Machinery).

Some typical questions:

- **Upper bounds**: Is there a faster algorithm for a problem? How much time does it need in the worst case?
- **Lower bounds and impossibility**: What is the least any algorithm must pay? What cannot be done at all?
- **Models and definitions**: What concepts should you use to describe a new problem? STOC 2026 also encourages papers that extend the frontiers of the theory of computing or raise important problems that could benefit from theoretical analysis[^stoc2026cfp-e1].

The main results of theoretical research are **theorems and proofs**, not experimental data. For what kind of knowledge a proof produces and what proof is enough, see [Proof](../../../05_research-strategies/prove.md). For how to choose a problem, make progress, and write and check proofs, see [Theoretical research](../practices/theoretical_research.md). This page covers only the area's conventions for publishing and review.

## Main venues and timeline

**Both conferences and journals matter.** Theorists value conferences too, but there is a long tradition of completing and extending a conference paper and then submitting it to a journal; see the [computer science field overview](../README.md#conferences-are-the-main-publication-venue)[^cra1999evaluating-e4].

The table gives the rules of three theory conferences **each for one particular year**, as examples only. They are not conventions of the whole area. **The rules change every year; before you submit, go by that year's call for papers.** FOCS 2025 (the Symposium on Foundations of Computer Science) is sponsored by the IEEE Computer Society Technical Committee on Mathematical Foundations of Computing[^focs2025cfp-e1]. SODA 2025 is the Symposium on Discrete Algorithms, held jointly by ACM and SIAM (the Society for Industrial and Applied Mathematics)[^soda2025cfp-e1]. The columns are from different years: STOC is 2026, while FOCS and SODA are 2025 (we could not read the SODA 2026 submission page). Our sources do not cover theory conferences not listed in the table.

| Step | STOC 2026 | FOCS 2025 | SODA 2025 |
|---|---|---|---|
| Deadline | November 4, 2025; no separate abstract deadline[^stoc2026cfp-e11] | April 3, 2025[^focs2025cfp-e2] | July 5, 2024; no separate abstract deadline[^soda2025cfp-e2] |
| Submission length | **No page limit**; submitting the "full version" directly is encouraged[^stoc2026cfp-e2] | No page limit; full versions encouraged[^focs2025cfp-e3] | No page limit; full versions encouraged[^soda2025cfp-e3] |
| Opening pages | The first 12 pages must make clear the paper's value and key ideas, written for a broad theory audience[^stoc2026cfp-e3] | The first 10 pages must make clear the value and key ideas[^focs2025cfp-e3] | The first 10 pages must make clear the value, written for a broad audience in theoretical computer science and discrete mathematics[^soda2025cfp-e3] |
| Proofs | Must allow the main results to be fully verified[^stoc2026cfp-e4] | Must allow the main mathematical results to be fully verified[^focs2025cfp-e3] | Must allow the main mathematical results to be fully verified[^soda2025cfp-e3] |
| Anonymity | Double-blind, but the paper must not be weakened for the sake of anonymity[^stoc2026cfp-e5] | Double-blind; likewise, don't weaken the paper for anonymity[^focs2025cfp-e4] | "Fairly lightweight" double-blind; likewise, don't weaken the paper for anonymity[^soda2025cfp-e4] |
| After acceptance | Camera-ready version limited to 12 pages[^stoc2026cfp-e8]; the full version must be posted on a preprint server[^stoc2026cfp-e6] | Post the full version with proofs before the camera-ready deadline[^focs2025cfp-e5] | Go by that year's submission page |
| Simultaneous submission | Not allowed, per SIGACT policy[^stoc2026cfp-e7] | Not allowed, per SIGACT policy[^focs2025cfp-e6] | May not be submitted at the same time to another conference with published proceedings[^soda2025cfp-e5] |

Some cells in more detail, for STOC 2026 only:

- **The first 12 pages** means the first 12 pages after the title page. They must explain how important the paper is relative to existing work and which key technical and conceptual ideas the main results rest on, and they must be written for theoretical computer scientists broadly, not just experts in the narrow area[^stoc2026cfp-e3].
- **The rest**: the committee reads the abstract, table of contents, and anything beyond the first 12 pages at its own discretion[^stoc2026cfp-e4].
- **Preprints**: during double-blind review, authors may still post drafts online and on arXiv (a free preprint site) and give talks[^stoc2026cfp-e5]. After acceptance, the full version with proofs must be posted on arXiv, ECCC (the Electronic Colloquium on Computational Complexity, a preprint server), or a similar site before the camera-ready deadline[^stoc2026cfp-e6].
- **Simultaneous submission**: you may not submit the same or substantially the same content to another conference with published proceedings at the same time; the only exception is publication in *Science* or *Nature*[^stoc2026cfp-e7].

Two things stand out in the table:

- **Reviewers mainly read the first 10–12 pages.** Proofs can be long, but the paper's value and key ideas must be clear up front, and readable by people outside your narrow area. The three conferences word this almost identically.
- **Complete proofs are required and must eventually be public.** The main text carries the ideas and key proofs; the complete proofs go later in the paper or in the full version on a preprint server, but they cannot be left out.

**Theory papers also go to applied conferences.** For example, proofs in cryptography and security protocols are submitted to security conferences. IEEE S&P 2026 (the IEEE Symposium on Security and Privacy) and ACM CCS 2025 (the Conference on Computer and Communications Security) both require theory papers to make a convincing case for how their results relate to practice[^ieeesp2026cfp-e2][^ccs2025cfp-e2]. For these conferences' other rules, see [Security](security.md).

## Common strategies and standards of evidence

The grouping and summaries in this table are our own. Each standard speaks only for the paper or conference in its footnote.

| Strategy | What it looks like here | Evidence and how it is judged | How to do it |
|---|---|---|---|
| [Proof](../../../05_research-strategies/prove.md) (upper and lower bounds) | Designing algorithms and analyzing their complexity; proving lower bounds or impossibility | The proof can be fully verified[^stoc2026cfp-e4]; the technique must not also imply a stronger result that is known to be false[^aaronson2008ten-e2] | [Theoretical research: checking your own proofs](../practices/theoretical_research.md#step-4-check-your-own-proof-all-proof-based-work-the-machine-checking-part-is-computer-science) |
| [Proof](../../../05_research-strategies/prove.md) (models and definitions) | Proposing new models of computation, security definitions, or problems | Make clear where it sits relative to existing work[^stoc2026cfp-e3]; first make sure you really understand the problem[^aaronson2008ten-e1] | [Theoretical research: choosing a problem](../practices/theoretical_research.md#step-1-choose-a-problem-and-confirm-it-is-still-open-and-your-definitions-are-right-all-proof-based-work) |
| [Proof](../../../05_research-strategies/prove.md) (machine-checked) | Formal verification with a proof assistant, for example the seL4 kernel[^klein2009sel4-e8] | State which assumptions the proof depends on[^klein2009sel4-e1] | [Proof: what evidence is enough](../../../05_research-strategies/prove.md#2-what-evidence-is-enough), [Systems](systems.md) |
| [Proof](../../../05_research-strategies/prove.md) (applied theory) | Cryptography, security protocols, learning theory | When submitting to an applied conference, explain the relation to practice[^ieeesp2026cfp-e2][^ccs2025cfp-e2] | [Security](security.md), [Machine learning](machine_learning.md) |

How to use this table: the core strategy of a theory paper is almost always proof; what differs is what is being proved and who the readers are. Some papers also include experiments, for example to check how an algorithm performs in practice; hold that part to the standards of [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md).

## Conventions specific to this area

**Ideas in the main text, complete proofs later, but never omitted.** STOC 2026 requires the first 12 pages to make clear the value and key ideas[^stoc2026cfp-e3], and also requires proofs that allow the main results to be fully verified[^stoc2026cfp-e4]. Lamport likewise recommends preparing a detailed and a brief version of a proof; see [Theoretical research](../practices/theoretical_research.md#step-5-give-both-intuition-and-formality-all-proof-based-work). As we read them, the two pieces of advice point the same way.

**Errors in proofs are not rare, so make your proofs checkable.** For how often published proofs turn out wrong, and Thurston's observations on how people actually check proofs, see [Proof: what evidence is enough](../../../05_research-strategies/prove.md#2-what-evidence-is-enough). Before you submit, you can check yourself against Aaronson's "signs that a claimed breakthrough is wrong"; see [Theoretical research](../practices/theoretical_research.md#step-4-check-your-own-proof-all-proof-based-work-the-machine-checking-part-is-computer-science).

**How much detail counts as a proof is learned by reading and talking.** The three points below come from a 1994 essay by the mathematician Thurston. **The original is about mathematics**, not theoretical computer science:

- As a graduate student he did not understand what a "proof" really was either. He came to understand it gradually by attending seminars, reading papers, and talking with other graduate students[^thurston1994proof-e6].
- By watching which facts other papers in the field use without proof, and which references they cite, you can learn what the field takes as its accepted foundation[^thurston1994proof-e7].
- Within the same subfield, once an important theorem has been proved, the solution can often (but not always) be passed from one person to another in a few minutes[^thurston1994proof-e4].

Applying these to theoretical computer science is our own judgment: different areas assume different levels of detail, and our sources contain no general standard. Reading recent papers in your target area and going to seminars are how you learn the right level. If you cannot explain the idea of your proof clearly, don't rush to submit.

**Machine-checked proofs have limits too.** The seL4 authors acknowledge that the proof of implementation correctness shows only that the implementation matches the specification; it does not guarantee that the specification describes the behavior users actually want[^klein2009sel4-e2]. So spell out the specification and assumptions in the paper and let readers judge. For what this kind of work costs and how it is done, see [Proof](../../../05_research-strategies/prove.md#2-what-evidence-is-enough).

**Habits around citation and authorship.**

- STOC 2026 asks authors not to use "et al." in citations, but to list all authors' surnames equally[^stoc2026cfp-e9].
- A 2004 statement by the American Mathematical Society says that **mathematicians** traditionally list the authors of joint papers in alphabetical order by surname[^amsculture2004joint-e3].
- Our sources do not say whether theoretical computer science has a written rule; there is only one set of statistics to go on. Waltman (2012) counted multi-author papers indexed in Web of Science[^waltman2012empirical-e2] and compared them by journal subject category[^waltman2012empirical-e3]. For 2007–2011, in journals in the category "Computer science, theory & methods", 48.6% of papers listed authors in alphabetical order by surname; after removing papers that are alphabetical by chance, an estimated 32.6% did so intentionally[^waltman2012empirical-e5]. The "intentional" share is a model estimate, not a direct count[^waltman2012empirical-e4]. For "Mathematics" in the same period, the two figures were 83.3% and 73.3%[^waltman2012empirical-e6].
- How to read these numbers: they cover only journal categories, not conference papers such as those at STOC or FOCS, and the data are over a decade old. All they show is that alphabetical author order is common in theoretical computer science, but not the overwhelming norm it is in mathematics. For how your own area orders authors, ask your advisor or look at recent papers at your target conference.

**Don't take a single rejection too hard.** Conference program committees decide by consensus and tend to favor safe, incremental work[^fortnow2009time-e3]. For a concrete example from theory (Gödel Prize papers that were first rejected), see [Theoretical research](../practices/theoretical_research.md#step-6-submitting-conferences-and-journals-computer-science).

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Filling the first 12 pages with technical detail without making clear the significance and key ideas | STOC 2026 requires the first 12 pages to be written for a broad theory audience[^stoc2026cfp-e3]; what comes after may not be read[^stoc2026cfp-e4] |
| Submitting only a proof sketch, with the complete proof "deferred to the full version" | STOC 2026 requires full verifiability[^stoc2026cfp-e4]; a sketch is not a proof[^lamport2012how-e13] |
| Not posting the full version after acceptance | STOC 2026 requires posting it on a preprint server before the camera-ready deadline[^stoc2026cfp-e6] |
| Deleting key citations to stay anonymous | STOC 2026 states that the paper must not be weakened for the sake of anonymity[^stoc2026cfp-e5] |
| Submitting the same result to two conferences with proceedings at the same time | Violates SIGACT policy[^stoc2026cfp-e7] |
| Not checking for relevant lower bounds and impossibility results | Conflicting with known results without addressing them is a classic sign of an error[^aaronson2008ten-e3] |
| Giving only theorems, without practical significance, when submitting to an applied conference such as security | IEEE S&P 2026 and CCS 2025 both require explaining how the results relate to practice[^ieeesp2026cfp-e2][^ccs2025cfp-e2] |
| Treating the conventions of mathematics as those of theoretical computer science | The Thurston and American Mathematical Society sources on this page are about mathematics; for theoretical computer science, look at the papers and conferences of your target area |

## Further reading

- **The call for papers of the conference you are targeting, for that year**, for example STOC, FOCS, or SODA. Pay particular attention to the requirements for the opening pages, proofs, and simultaneous submission.
- **Thurston 1994, On Proof and Progress in Mathematics**: how mathematicians understand, communicate, and check proofs. It is about mathematics, and suits anyone who wants to understand how a theory community works.
- **Fortnow 2009, Time for Computer Science to Grow Up**: a theoretical computer scientist's critique of conference culture.
- For how to write proofs and checklists for checking them (Lamport, Aaronson, and others), see the further reading in [Theoretical research](../practices/theoretical_research.md).
- Related areas: [Security](security.md), [Systems](systems.md), [Programming languages](programming_languages.md), [Machine learning](machine_learning.md).

[^stoc2026cfp-e10]: STOC 2026 call for papers, opening (topics). [Evidence](../../../../sources/notes/stoc2026cfp.md#e10)
[^stoc2026cfp-e1]: STOC 2026 call for papers, opening. [Evidence](../../../../sources/notes/stoc2026cfp.md#e1)
[^cra1999evaluating-e4]: Computing Research Association (CRA) 1999, Structure of The Field. [Evidence](../../../../sources/notes/cra1999evaluating.md#e4)
[^stoc2026cfp-e11]: STOC 2026 call for papers, Dates and other relevant information. [Evidence](../../../../sources/notes/stoc2026cfp.md#e11)
[^stoc2026cfp-e2]: STOC 2026 call for papers, Submission format. [Evidence](../../../../sources/notes/stoc2026cfp.md#e2)
[^stoc2026cfp-e3]: STOC 2026 call for papers, Submission format. [Evidence](../../../../sources/notes/stoc2026cfp.md#e3)
[^stoc2026cfp-e4]: STOC 2026 call for papers, Submission format. [Evidence](../../../../sources/notes/stoc2026cfp.md#e4)
[^stoc2026cfp-e5]: STOC 2026 call for papers, Submission format (double-blind). [Evidence](../../../../sources/notes/stoc2026cfp.md#e5)
[^stoc2026cfp-e8]: STOC 2026 call for papers, Camera-ready versions. [Evidence](../../../../sources/notes/stoc2026cfp.md#e8)
[^stoc2026cfp-e6]: STOC 2026 call for papers, Submission Instructions. [Evidence](../../../../sources/notes/stoc2026cfp.md#e6)
[^stoc2026cfp-e7]: STOC 2026 call for papers, Prior and Simultaneous Submissions. [Evidence](../../../../sources/notes/stoc2026cfp.md#e7)
[^ieeesp2026cfp-e2]: IEEE S&P 2026 call for papers, opening. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e2)
[^ccs2025cfp-e2]: ACM CCS 2025 call for papers, opening. [Evidence](../../../../sources/notes/ccs2025cfp.md#e2)
[^aaronson2008ten-e2]: Aaronson 2008, item 3. [Evidence](../../../../sources/notes/aaronson2008ten.md#e2)
[^aaronson2008ten-e1]: Aaronson 2008, item 2. [Evidence](../../../../sources/notes/aaronson2008ten.md#e1)
[^klein2009sel4-e8]: Klein et al. 2009, Abstract. [Evidence](../../../../sources/notes/klein2009sel4.md#e8)
[^klein2009sel4-e1]: Klein et al. 2009, §1. [Evidence](../../../../sources/notes/klein2009sel4.md#e1)
[^thurston1994proof-e6]: Thurston 1994, §4. [Evidence](../../../../sources/notes/thurston1994proof.md#e6)
[^thurston1994proof-e7]: Thurston 1994, §4. [Evidence](../../../../sources/notes/thurston1994proof.md#e7)
[^thurston1994proof-e4]: Thurston 1994, §3. [Evidence](../../../../sources/notes/thurston1994proof.md#e4)
[^klein2009sel4-e2]: Klein et al. 2009, §4.5. [Evidence](../../../../sources/notes/klein2009sel4.md#e2)
[^stoc2026cfp-e9]: STOC 2026 call for papers, Recommended Best Practices for References. [Evidence](../../../../sources/notes/stoc2026cfp.md#e9)
[^amsculture2004joint-e3]: American Mathematical Society 2004, para. 3. [Evidence](../../../../sources/notes/amsculture2004joint.md#e3)
[^focs2025cfp-e1]: FOCS 2025 call for papers, Overview and Call for Papers. [Evidence](../../../../sources/notes/focs2025cfp.md#e1)
[^focs2025cfp-e2]: FOCS 2025 call for papers, Important dates. [Evidence](../../../../sources/notes/focs2025cfp.md#e2)
[^focs2025cfp-e3]: FOCS 2025 call for papers, Submission format. [Evidence](../../../../sources/notes/focs2025cfp.md#e3)
[^focs2025cfp-e4]: FOCS 2025 call for papers, Submission format (double-blind). [Evidence](../../../../sources/notes/focs2025cfp.md#e4)
[^focs2025cfp-e5]: FOCS 2025 call for papers, Submission instructions. [Evidence](../../../../sources/notes/focs2025cfp.md#e5)
[^focs2025cfp-e6]: FOCS 2025 call for papers, Prior and simultaneous submission. [Evidence](../../../../sources/notes/focs2025cfp.md#e6)
[^soda2025cfp-e1]: SODA 2025 submission page, page title. [Evidence](../../../../sources/notes/soda2025cfp.md#e1)
[^soda2025cfp-e2]: SODA 2025 submission page, Important Submission Information. [Evidence](../../../../sources/notes/soda2025cfp.md#e2)
[^soda2025cfp-e3]: SODA 2025 submission page, Submission Format. [Evidence](../../../../sources/notes/soda2025cfp.md#e3)
[^soda2025cfp-e4]: SODA 2025 submission page, Anonymous Submissions. [Evidence](../../../../sources/notes/soda2025cfp.md#e4)
[^soda2025cfp-e5]: SODA 2025 submission page, Simultaneous Submissions. [Evidence](../../../../sources/notes/soda2025cfp.md#e5)
[^waltman2012empirical-e2]: Waltman 2012, §3. [Evidence](../../../../sources/notes/waltman2012empirical.md#e2)
[^waltman2012empirical-e3]: Waltman 2012, §3.2. [Evidence](../../../../sources/notes/waltman2012empirical.md#e3)
[^waltman2012empirical-e4]: Waltman 2012, §2. [Evidence](../../../../sources/notes/waltman2012empirical.md#e4)
[^waltman2012empirical-e5]: Waltman 2012, §3.2 Table 1. [Evidence](../../../../sources/notes/waltman2012empirical.md#e5)
[^waltman2012empirical-e6]: Waltman 2012, §3.2 Table 1. [Evidence](../../../../sources/notes/waltman2012empirical.md#e6)
[^fortnow2009time-e3]: Fortnow 2009, main text. [Evidence](../../../../sources/notes/fortnow2009time.md#e3)
[^lamport2012how-e13]: Lamport 2012, §6. [Evidence](../../../../sources/notes/lamport2012how.md#e13)
[^aaronson2008ten-e3]: Aaronson 2008, item 4. [Evidence](../../../../sources/notes/aaronson2008ten.md#e3)
