# Programming languages

> This page covers only the practices specific to this area. For practices common to all research, see the chapters of Parts 1 and 2 and the research strategies; for conventions shared across computer science, see the [computer science field overview](../README.md).

## What this area studies

Programming languages research studies how to design, implement, analyze, and verify programming languages, and the programs written in them. To see how broad the area is, look at two conferences' 2026 calls for papers:

- **PLDI** (the Conference on Programming Language Design and Implementation) invites papers on all aspects of programming language research, including design, implementation, theory, applications, and performance; novel system designs, thorough empirical work, well-motivated theoretical results, and new application areas are all in scope[^pldi2026cfp-e1].
- **POPL** (the Symposium on Principles of Programming Languages) accepts both theoretical and experimental papers, from formal frameworks to experience reports; it wants work that makes principled, enduring contributions to the theory, design, understanding, implementation, or application of programming languages[^popl2026cfp-e1].

Examples of typical questions `[Our analysis]`:

- Can a new type system guarantee that a certain class of errors is ruled out before the program runs? That calls for **proof**.
- How much faster does a new compiler optimization make programs? That calls for **building and improving**, followed by benchmarking.
- How many problems does a static analysis tool find in real code, and how many false positives does it report? That calls for evaluation on programs not used during development.

A single paper often has both proofs and experiments.

## Main venues and timeline

**Venues.** When SIGPLAN (the Association for Computing Machinery Special Interest Group on Programming Languages) drew up its empirical evaluation checklist, it sampled recent papers from these conferences[^blackburn2018sigplan-e32]:

- ASPLOS (the Conference on Architectural Support for Programming Languages and Operating Systems)
- ICFP (the International Conference on Functional Programming)
- OOPSLA (the conference on Object-Oriented Programming, Systems, Languages, and Applications)
- PLDI and POPL

You can treat these as examples of the area's main venues `[Our analysis]`.

**PLDI and POPL 2026 papers are published in a journal.** PLDI 2026 papers appear in the PLDI issue of PACMPL (Proceedings of the ACM on Programming Languages, a programming languages journal published by the ACM), and the authors are invited to present at the conference[^pldi2026cfp-e2]. POPL 2026 works the same way: to meet ACM's requirements for journal publication, accepted papers are first "conditionally accepted", and the original reviewers confirm whether the revisions are adequate[^popl2026cfp-e7]. So both conferences have a round of "revise according to the reviews", unlike conferences that make a single decision `[Our analysis]`.

**PLDI 2026 and POPL 2026 as examples.** The table below lists only the rules in these two calls for papers, not conventions for the whole area; other years and other conferences will differ, so **read your target conference's call for papers for the current year before submitting**.

| Item | PLDI 2026 | POPL 2026 |
|---|---|---|
| Length | At most 20 pages of main text, excluding references[^pldi2026cfp-e10] | At most 25 pages of main text, excluding references[^popl2026cfp-e8] |
| Review criteria | Accuracy, significance, originality, clarity[^pldi2026cfp-e3] | Significance, originality, relevance, correctness, clarity[^popl2026cfp-e2] |
| Review rounds | Two rounds: after the first, some papers are conditionally accepted and the rest rejected; in the second, the original reviewers check the revisions, and papers not adequately revised can still be rejected[^pldi2026cfp-e4] | Conditional acceptance first; the original reviewers confirm the revisions[^popl2026cfp-e7] |
| Author response | A few days after the first round, for correcting errors and clarifying technical questions[^pldi2026cfp-e5] | Should be concise and address specific questions; may not present new technical results[^popl2026cfp-e6] |
| Double-blind | Supplementary material must be anonymized too; the committee learns the authors of accepted papers only after the second round[^pldi2026cfp-e6] | Reviewers see the authors of accepted papers only after conditional acceptance[^popl2026cfp-e3] |
| Supplementary material | All appendices are submitted as supplementary material, which reviewers are not required to read[^pldi2026cfp-e11] | You may submit proofs, proof scripts, implementations, and experimental data; reviewers are not required to read them[^popl2026cfp-e4] |
| Preprints | You may submit work already posted on arXiv[^pldi2026cfp-e8] | You may post on a personal website, an institutional repository, or arXiv[^popl2026cfp-e5] |
| Artifact evaluation | Voluntary and does not affect acceptance[^pldi2026cfp-e12]; at submission you must say whether you intend to submit an artifact[^pldi2026cfp-e13] | Strongly encouraged but voluntary, and does not affect acceptance[^popl2026cfp-e9] |

**Supplementary material can't replace the main text.** Both conferences allow supplementary material in 2026, but both say reviewers are not required to read it[^pldi2026cfp-e11][^popl2026cfp-e4]. So the theorem statements and key experimental results that support your central claims belong in the main text; supplementary material is for details `[Our analysis]`.

## Common strategies and standards of evidence

For empirical evaluation in this area, you can check your work against the **SIGPLAN Empirical Evaluation Checklist** (the "SIGPLAN checklist" below). SIGPLAN wrote it for empirical evaluation in this area, and PLDI 2026 explicitly encourages authors of empirical papers to prepare their submissions according to its seven categories[^pldi2026cfp-e3]. The checklist is meant to support judgment, not replace it[^blackburn2018sigplan-e14].

For strategies and standards of evidence shared across computer science, see [Computer science field overview: common strategies and standards of evidence](../README.md#common-strategies-and-standards-of-evidence). The table below adds only what needs particular care in programming languages; it is our own summary, with the facts in each cell supported by the footnotes `[Our analysis]`.

| Strategy | What it looks like in this area | What needs particular care | How to do it |
|---|---|---|---|
| [Building and improving](../../../05_research-strategies/build_improve.md) | New language features, compiler optimizations, program analysis or synthesis tools | Don't present a weak straw-man baseline as the state of the art[^blackburn2018sigplan-e4]; don't evaluate a static analysis only on the programs you consulted while developing it[^blackburn2018sigplan-e26] | [Engineering research](../practices/engineering_research.md) |
| [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md), [Measurement](../../../05_research-strategies/measure.md) | Running time, memory, compile time | Performance gains are often small and may fall within measurement error[^kalibera2013rigorous-e2] | [Benchmarking](../practices/benchmarking.md) |
| [Proof](../../../05_research-strategies/prove.md) | Type soundness, language semantics, program verification | Proof details and proof scripts can go in as supplementary material (POPL 2026)[^popl2026cfp-e4], but the theorems themselves must be in the main text | [Theoretical research](../practices/theoretical_research.md) |
| [Description](../../../05_research-strategies/observe_describe.md) | How language features are used in real programs; how developers use languages and tools | Judged by the standards of the method used; PLDI 2026 lists thorough empirical work as in scope[^pldi2026cfp-e1] | [Mining software repositories](../practices/repository_mining.md), [Controlled experiments](../../../06_methods/controlled_experiment.md) |

Many papers have both proofs and experiments: for example, first proving an analysis sound, then measuring its speed and precision on real programs. In that case each part is held to its own standard `[Our analysis]`.

## Conventions specific to this area

**1. State your claims explicitly.** Only when a claim is stated explicitly can readers judge whether the experiments support it[^blackburn2018sigplan-e1]. "Significantly faster" is not enough: say on which programs, compared with what, and by how much `[Our analysis]`.

**2. Report the full distribution of performance results, and the costs.** Some of the SIGPLAN checklist's requirements:

- Reporting only a mean or median can mislead readers, especially when the distribution is bimodal or highly variable[^blackburn2018sigplan-e8].
- Summarizing speedups of 4%, 6%, 7%, and 49% as "up to 49% faster" is not acceptable; report the full distribution[^blackburn2018sigplan-e9].
- Measure all the important effects, to show the system's true cost[^blackburn2018sigplan-e21]. For example, if an optimization makes programs run faster but makes compilation slower, report compile time too `[Our analysis]`.
- Give all parameters (including defaults), the version numbers of all software, and full details of the hardware platform[^blackburn2018sigplan-e22].

For how to repeat measurements, how to keep factors such as link order from quietly favoring one system, and how to handle warm-up, see [Systems](systems.md#conventions-specific-to-this-area) and [Benchmarking: designing the measurement process](../practices/benchmarking.md#step-4-design-the-measurement-procedure).

**3. Compare fairly.** You can't compile the competitor at the lowest optimization level and your own system at the highest[^blackburn2018sigplan-e15]. Picking only a few programs from a benchmark suite, or trimming benchmarks, is a problem the authors of the SIGPLAN checklist often see in papers[^blackburn2018sigplan-e18].

**4. Take anonymity seriously, but don't let it lower quality.** PLDI 2026 notes that if your paper is the first to introduce a well-known system, or the system's name would identify the authors, you should use a different name in the submission, and you may note that it was changed for double-blind review[^pldi2026cfp-e7]. POPL 2026 stresses that you should not lower the quality of your submission for the sake of anonymity[^popl2026cfp-e5].

**5. The author response is not the place to add experiments.** POPL 2026 says the response may not present new technical results[^popl2026cfp-e6]. So finish the key proofs and experiments before you submit `[Our analysis]`. For how to write a response in general, see [Reviews, revision, and what to do after rejection](../../../03_write-and-publish/03_review-and-revision.md#4-writing-an-author-response-for-a-conference).

**6. Artifact evaluation is separate from acceptance, but prepare early.** At both PLDI 2026 and POPL 2026, artifact evaluation is voluntary and does not affect whether the paper is accepted[^pldi2026cfp-e12][^popl2026cfp-e9]. It checks whether the claims and evidence in the paper are consistent with the artifact[^blackburn2018sigplan-e31]. PLDI 2026 asks you to say at submission whether you intend to submit an artifact[^pldi2026cfp-e13], so organize your code and proof scripts to the standard of "someone else can run this" while you are writing them `[Our analysis]`. For what the badges mean, see the [computer science field overview](../README.md#artifact-evaluation-and-badges).

**7. Declare conflicts of interest honestly.** PLDI 2026 states that declaring false conflicts in order to exclude certain reviewers may lead to rejection[^pldi2026cfp-e9].

**8. Prepare to the standards of your target conference.** Even within this area, the review criteria of PLDI 2026 and POPL 2026 are not quite the same (see the table above). For how reviewers generally read a paper and what they look for, see [Being a reviewer](../../../08_throughout/being_a_reviewer.md#3-read-the-paper-like-a-reviewer).

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Vague claims, such as just "significantly faster" | Readers can't judge whether the experiments support them[^blackburn2018sigplan-e1] |
| Giving only a mean for performance results | It can mislead readers[^blackburn2018sigplan-e8] |
| Writing "up to 49% faster" | You need to report the full distribution of results[^blackburn2018sigplan-e9] |
| Running the baseline at the lowest optimization level while carefully tuning your own system | The comparison is unfair[^blackburn2018sigplan-e15] |
| Picking a few programs from a benchmark suite that show good results | A problem the authors of the SIGPLAN checklist often see[^blackburn2018sigplan-e18] |
| Evaluating a static analysis only on the programs you used throughout development | Evaluate it on programs not used during development[^blackburn2018sigplan-e26] |
| Reporting only that programs run faster, not that compilation got slower | You need to show the true cost[^blackburn2018sigplan-e21] |
| Leaving out software versions and hardware details | The checklist requires them in full[^blackburn2018sigplan-e22] |
| Keeping a system name in the submission that instantly identifies your group | PLDI 2026 requires you to rename it[^pldi2026cfp-e7] |
| Promoting the paper on the area's main mailing lists while it is under review | Reviewers are likely to see it; PLDI 2026's double-blind FAQ lists this as something not to do[^pldi2026cfp-e8] |
| Planning to add experiments or proofs in the author response | POPL 2026 does not allow new technical results in the response[^popl2026cfp-e6] |
| Putting key proofs or experiments only in the appendix | At PLDI 2026 appendices count as supplementary material, which reviewers are not required to read[^pldi2026cfp-e11] |

## Further reading

- **SIGPLAN Empirical Evaluation Checklist** (Berger, Blackburn, Hauswirth, Hicks, 2018): a one-page checklist with annotations, listing the most common problems in the empirical evaluation of programming languages papers. Read it once before running experiments, and check against it again before submitting.
- **Kalibera & Jones 2013, Rigorous Benchmarking in Reasonable Time**: how to make performance experiments rigorous in limited time, and how to report results with confidence intervals.
- **Georges et al. 2007, Statistically Rigorous Java Performance Evaluation**: how to measure the performance of systems with virtual machines and just-in-time compilation.
- **This handbook's [Benchmarking](../practices/benchmarking.md) and [Theoretical research](../practices/theoretical_research.md) pages**: concrete practice for performance experiments and proofs.
- **The call for papers and double-blind review FAQ of the conference you are submitting to, for that year**, such as the PLDI and POPL calls for papers.

[^pldi2026cfp-e1]: PLDI 2026 Call for Papers, opening section and Scope. [Evidence](../../../../sources/notes/pldi2026cfp.md#e1)
[^pldi2026cfp-e2]: PLDI 2026 Call for Papers, opening section. [Evidence](../../../../sources/notes/pldi2026cfp.md#e2)
[^pldi2026cfp-e3]: PLDI 2026 Call for Papers, Evaluation Criteria and Process. [Evidence](../../../../sources/notes/pldi2026cfp.md#e3)
[^pldi2026cfp-e4]: PLDI 2026 Call for Papers, Evaluation Criteria and Process. [Evidence](../../../../sources/notes/pldi2026cfp.md#e4)
[^pldi2026cfp-e5]: PLDI 2026 Call for Papers, Evaluation Criteria and Process. [Evidence](../../../../sources/notes/pldi2026cfp.md#e5)
[^pldi2026cfp-e6]: PLDI 2026 Call for Papers, Double-Blind Reviewing. [Evidence](../../../../sources/notes/pldi2026cfp.md#e6)
[^pldi2026cfp-e7]: PLDI 2026 double-blind review FAQ, how to anonymize. [Evidence](../../../../sources/notes/pldi2026cfp.md#e7)
[^pldi2026cfp-e8]: PLDI 2026 double-blind review FAQ, whether you can post the paper publicly. [Evidence](../../../../sources/notes/pldi2026cfp.md#e8)
[^pldi2026cfp-e9]: PLDI 2026 Call for Papers, Declaring Conflicts. [Evidence](../../../../sources/notes/pldi2026cfp.md#e9)
[^pldi2026cfp-e10]: PLDI 2026 Call for Papers, Formatting Requirements. [Evidence](../../../../sources/notes/pldi2026cfp.md#e10)
[^pldi2026cfp-e11]: PLDI 2026 Call for Papers, Supplementary Material. [Evidence](../../../../sources/notes/pldi2026cfp.md#e11)
[^pldi2026cfp-e12]: PLDI 2026 Call for Papers, Artifact Evaluation and Artifact Intent. [Evidence](../../../../sources/notes/pldi2026cfp.md#e12)
[^pldi2026cfp-e13]: PLDI 2026 Call for Papers, Artifact Evaluation and Artifact Intent. [Evidence](../../../../sources/notes/pldi2026cfp.md#e13)
[^popl2026cfp-e1]: POPL 2026 Call for Papers, Scope. [Evidence](../../../../sources/notes/popl2026cfp.md#e1)
[^popl2026cfp-e2]: POPL 2026 Call for Papers, Evaluation Criteria. [Evidence](../../../../sources/notes/popl2026cfp.md#e2)
[^popl2026cfp-e3]: POPL 2026 Call for Papers, Double-Blind Reviewing. [Evidence](../../../../sources/notes/popl2026cfp.md#e3)
[^popl2026cfp-e4]: POPL 2026 Call for Papers, Double-Blind Reviewing (supplementary material). [Evidence](../../../../sources/notes/popl2026cfp.md#e4)
[^popl2026cfp-e5]: POPL 2026 Call for Papers, Double-Blind Reviewing (dissemination during review). [Evidence](../../../../sources/notes/popl2026cfp.md#e5)
[^popl2026cfp-e6]: POPL 2026 Call for Papers, Evaluation Process. [Evidence](../../../../sources/notes/popl2026cfp.md#e6)
[^popl2026cfp-e7]: POPL 2026 Call for Papers, Evaluation Process. [Evidence](../../../../sources/notes/popl2026cfp.md#e7)
[^popl2026cfp-e8]: POPL 2026 Call for Papers, Submission Guidelines. [Evidence](../../../../sources/notes/popl2026cfp.md#e8)
[^popl2026cfp-e9]: POPL 2026 Call for Papers, Artifact Evaluation for Accepted Papers. [Evidence](../../../../sources/notes/popl2026cfp.md#e9)
[^blackburn2018sigplan-e32]: SIGPLAN Empirical Evaluation Checklist, FAQ (how the items were chosen). [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e32)
[^blackburn2018sigplan-e4]: SIGPLAN Empirical Evaluation Checklist, Suitable Comparison. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e4)
[^blackburn2018sigplan-e15]: SIGPLAN Empirical Evaluation Checklist, Suitable Comparison. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e15)
[^blackburn2018sigplan-e8]: SIGPLAN Empirical Evaluation Checklist, Adequate Data Analysis. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e8)
[^blackburn2018sigplan-e9]: SIGPLAN Empirical Evaluation Checklist, Appropriate and Clear Experimental Design. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e26]: SIGPLAN Empirical Evaluation Checklist, Appropriate and Clear Experimental Design. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e26)
[^blackburn2018sigplan-e18]: SIGPLAN Empirical Evaluation Checklist, Notes (non-standard suites). [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e18)
[^blackburn2018sigplan-e22]: SIGPLAN Empirical Evaluation Checklist, Appropriate and Clear Experimental Design. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e22)
[^blackburn2018sigplan-e31]: SIGPLAN Empirical Evaluation Checklist, FAQ (relation to artifact evaluation). [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e31)
[^blackburn2018sigplan-e14]: SIGPLAN Empirical Evaluation Checklist, note below the title. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e14)
[^blackburn2018sigplan-e1]: SIGPLAN Empirical Evaluation Checklist, Clearly Stated Claims. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e1)
[^blackburn2018sigplan-e21]: SIGPLAN Empirical Evaluation Checklist, Appropriate and Clear Experimental Design. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e21)
[^kalibera2013rigorous-e2]: Kalibera & Jones 2013, §1. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e2)
