# Software engineering

> This page covers only what is specific to this area. For general practice, see the Parts and the research strategies. For the conventions shared across computer science, see the [computer science field overview](../README.md).

## What this area studies

Software engineering research studies how software is developed, analyzed, and maintained, and also the people and teams who build it. Shaw sorts the questions the field tries to answer into a few kinds: methods for developing or analyzing software; the design or evaluation of a particular system; generalizations about a whole class of systems or techniques; and whether something exists or can be done at all[^shaw2003writing-e38].

To see how broad the field is, look at one conference's call for papers. ICSE 2026 (the International Conference on Software Engineering) divided submissions into nine research areas and accepted quantitative, qualitative, and mixed-methods research[^icse2026cfp-e1]. The areas run from "AI for Software Engineering" (using artificial intelligence to support software engineering) and mining data from version repositories and bug trackers to human and social aspects; formal methods and model checking are in scope too[^icse2026cfp-e2].

So papers in this field roughly fall into two kinds `[Our analysis]`:

- **Building new techniques**, for example "does a new test-generation tool find more bugs than existing tools?"
- **Describing how things are**, for example "why do developers leave open-source projects?"

The mix differs by venue. Storey et al. counted papers from 2017: most papers at ICSE proposed solutions (mostly technical ones), while most papers in EMSE (the journal *Empirical Software Engineering*) were descriptive[^storey2020who-e17].

## Main venues and timeline

**Conferences and journals.** The table lists only the venues mentioned in our sources:

| Venue | Type | What our sources say |
|---|---|---|
| ICSE | Conference | Describes itself as the premier venue for presenting the most recent and significant technical research in the field[^icse2026cfp-e14] |
| ESEM (Empirical Software Engineering and Measurement symposium) | Conference | Focuses on empirical methods and also accepts papers on social aspects[^storey2020who-e18] |
| EMSE | Journal | Same as above[^storey2020who-e18] |
| TSE (*IEEE Transactions on Software Engineering*) | Journal | Takes part, with ICSE 2026, in a scheme that reduces duplicate reviewing of journal extensions of conference papers[^icse2026cfp-e11] |
| TOSEM (*ACM Transactions on Software Engineering and Methodology*) | Journal | Same as above[^icse2026cfp-e11] |

What kind of paper is most common at ICSE? Shaw's 2003 analysis: papers reporting a new technique for developing or analyzing software[^shaw2003writing-e26].

**How a paper moves through ICSE 2026.** The table gives only the rules in the ICSE 2026 research track call for papers. They are not conventions of the whole field; other years and other conferences will differ, so **read your target conference's call for papers for that year before you submit**.

| Step | ICSE 2026 rule |
|---|---|
| Submission cycles | Two per year, as since 2024[^icse2026cfp-e3] |
| Author response | 3 days per cycle[^icse2026cfp-e3] |
| Length | At most 10 pages of main text (including figures, tables, and appendices), plus up to 2 pages of references[^icse2026cfp-e7] |
| Anonymity | Double-anonymous review; cite your own work in the third person. You may post an arXiv preprint, but must not say it was submitted to ICSE 2026[^icse2026cfp-e8] |
| Review criteria | Five: novelty, rigor, relevance, verifiability and transparency, and presentation. One reviewer checks any accompanying artifact[^icse2026cfp-e4] |
| Outcomes | Accept, revision, or reject. A revision gets about 4 weeks and is re-reviewed by the original reviewers; a paper that is not fixed well enough can still be rejected[^icse2026cfp-e5] |
| After rejection | Resubmitting a first-cycle rejection to the second cycle is strongly discouraged[^icse2026cfp-e6] |
| Artifacts | Not mandatory, but sharing is the default; if you don't share, explain why[^icse2026cfp-e12] |
| Concurrent submission | You may not submit the paper elsewhere while it is under review[^icse2026cfp-e9] |

One thing a newcomer may want to know: the second cycle of ICSE 2026 had a "shadow program committee", where PhD students, postdocs, and others practiced reviewing under guidance[^icse2026cfp-e13]. For general reviewing practice, see [Being a reviewer](../../../08_throughout/being_a_reviewer.md).

## Common strategies and standards of evidence

The **ACM SIGSOFT Empirical Standards** (review standards for papers, produced by the Special Interest Group on Software Engineering of the Association for Computing Machinery; "the empirical standards" below) are software engineering's own review standards. Their starting point is that there is no universal standard of quality: each study should be judged by the standards that fit its method[^ralph2020empirical-e142]. So they are written separately for each research method; systematic reviews, for example, have a standard of their own[^ralph2020empirical-e1].

The seven strategies common in computer science and the evidence standards for each are in [Computer science field overview: common strategies and standards of evidence](../README.md#common-strategies-and-standards-of-evidence). Most of the standards in that table come from the empirical standards, so we don't repeat them. The table below adds only the one point that needs special care in software engineering. The table is our own summary; the facts in each cell are in the footnotes `[Our analysis]`.

| Strategy | What it looks like in software engineering | Watch out for | How to do it |
|---|---|---|---|
| [Building and improving](../../../05_research-strategies/build_improve.md) | New testing, analysis, or repair techniques or tools | "It works for you" is not enough; you need evidence that it is useful to others too[^shaw2003writing-e11] | [Engineering research](../practices/engineering_research.md) |
| [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md) | Comparing tools on standard benchmarks | A search algorithm should at least be compared with random search[^arcuri2014hitchhiker-e4] | [Benchmarking](../practices/benchmarking.md), [Optimization studies](../practices/optimization_study.md) |
| [Description](../../../05_research-strategies/observe_describe.md) | Mining code repositories and bug records, or describing development practice through questionnaires and interviews | Trace data left behind by development shows only part of people's behavior and intentions[^storey2020who-e1] | [Mining software repositories](../practices/repository_mining.md), [Questionnaire surveys](../../../06_methods/questionnaire_survey.md), [Interview studies](../../../06_methods/interview_study.md) |
| [Causal explanation](../../../05_research-strategies/explain_causality.md) | Whether a tool or technique leads to an improvement | When people try out a tool, asking them directly whether it helped is unlikely to give meaningful data[^ko2015practical-e28] | [Controlled experiments](../../../06_methods/controlled_experiment.md) |
| [Synthesis](../../../05_research-strategies/synthesize.md) | Systematic reviews, mapping studies | Describe the search process and selection criteria step by step, so others can reproduce them[^ralph2020empirical-e4] | [Review studies](../../../06_methods/review_study.md) |
| [Proof](../../../05_research-strategies/prove.md) | Formal methods and model checking | A formal model rests on rigorous derivation and proof, not on one or two examples[^shaw2003writing-e9] | [Theoretical research](../practices/theoretical_research.md) |

## Conventions specific to this area

**1. Find the standard for your kind of study before you start.** The empirical standards are written method by method, so read the one for your kind of study first. Starting a study without reading or using the published guidelines for that kind of study is an antipattern the empirical standards name explicitly[^ralph2020empirical-e26].

**2. Know which criticisms are invalid.** The empirical standards also list "invalid criticisms", for example criticizing a study by the norms of a different research paradigm, or criticizing limitations inherent in a kind of study (such as saying a case study does not generalize well)[^ralph2020empirical-e25]. For how to use this list when responding to reviews, see [Reviews, revision, and what to do after rejection](../../../03_write-and-publish/03_review-and-revision.md#3-decide-what-to-change-and-what-to-argue). For what the standards ask of reviewers (judge credibility first, then importance), see [Being a reviewer](../../../08_throughout/being_a_reviewer.md#3-read-the-paper-like-a-reviewer).

**3. Use the term "case study" correctly.** In the software engineering literature, "case study" is often used to mean a worked example for demonstration, which is something entirely different from the case study as an empirical method[^easterbrook2008selecting-e10]. Evaluating a tool on a toy example and calling it a "case study" is an antipattern listed in the empirical standards[^ralph2020empirical-e93]. For real case studies, see [Case study and ethnography](../../../06_methods/case_study.md).

**4. Don't rely only on evaluating your own tool yourself.** A review by Ko et al. found that 62% of tool evaluations were really the inventors using the tool themselves and reporting their own experience, which says little about whether other people would benefit[^ko2015practical-e7]. For how to have real people try your tool, see [Controlled experiments](../../../06_methods/controlled_experiment.md).

**5. If your research claims to help people, consider involving people.** Among the 2017 papers at ICSE and in EMSE, most claimed their research would ultimately benefit people, but most did not involve people directly[^storey2020who-e16]. The great majority of data-driven papers did not triangulate their conclusions with another strategy (such as questionnaires or interviews)[^storey2020who-e9]. For how to combine the two, see [Mixed methods](../../../06_methods/mixed_methods.md).

**6. Make your artifacts available, and store them in the right place.** The empirical standards recommend depositing supplementary material in an archival repository that guarantees long-term preservation; personal or institutional websites, GitHub, and cloud drives do not count as proper archiving[^ralph2020empirical-e139]. Conversely, not releasing material for a legitimate reason should not be grounds for criticism[^ralph2020empirical-e140]. ICSE 2026 also states that qualitative research does not aim at replicability[^icse2026cfp-e12]. For artifact evaluation and badges in general, see the [computer science field overview](../README.md#artifact-evaluation-and-badges).

**7. Ethics.** For general principles, see [Research integrity and ethics](../../../08_throughout/integrity_and_ethics.md). When human participants are involved, ICSE 2026 requires you to follow ACM's publication policy on research involving human participants[^icse2026cfp-e10]. When you use secondary data such as repositories or Q&A sites, explain why the data is legitimately available to use; using it just because it is technically downloadable is an antipattern[^ralph2020empirical-e135]. For the details, see [Mining software repositories: handling ethics and licensing](../practices/repository_mining.md#step-8-handle-ethics-and-licensing).

**8. You can publish your plan first.** The empirical standards list "two-phase publication: first publish the study plan, then publish the results" as a desirable attribute[^ralph2020empirical-e28].

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Proposing a new tool and comparing it only with weak methods, or not comparing at all | The empirical standards require comparison with the best current alternatives, or an explanation of why that is not possible[^ralph2020empirical-e85] |
| Demonstrating on a small example you made up and calling it a "case study" | Listed as an antipattern in the empirical standards[^ralph2020empirical-e93] |
| Asking users only "is this tool good?" and calling that an evaluation | An evaluation based only on user opinion is an antipattern listed in the empirical standards[^ralph2020empirical-e92] |
| Recruiting only students from your own university and not discussing generalizability | You need to argue why the results apply to industry developers[^easterbrook2008selecting-e74] |
| Running a search algorithm only a few times and drawing conclusions | A review of papers from 2009–2010 found that such studies often did not properly handle the algorithms' randomness[^arcuri2014hitchhiker-e2]; for how to do it, see [Optimization studies](../practices/optimization_study.md) |
| Putting your code on GitHub and calling it "archived" | The empirical standards do not consider GitHub proper archiving[^ralph2020empirical-e139] |
| Scraping public data and using it without discussing ethics | Being technically accessible does not make data legitimately usable[^ralph2020empirical-e135] |
| Listing threats to validity but still stating conclusions with full confidence | Listed as an antipattern in the empirical standards[^ralph2020empirical-e126] |
| Judging a qualitative study by the standards for experiments | Different methods have different review standards[^ralph2020empirical-e142] |

## Further reading

- **ACM SIGSOFT Empirical Standards** (Ralph et al.): review standards written separately for each research method. Read the one for your kind of study before you start.
- **Shaw 2003, Writing Good Software Engineering Research Papers**: what questions, results, and validation ICSE reviewers want to see. Good to read before your first paper.
- **Easterbrook et al. 2008, Selecting Empirical Methods for Software Engineering Research**: which empirical methods in software engineering suit which questions.
- **Ko et al. 2015, A practical guide to controlled experiments of software engineering tools with human participants**: read it when you want real people to try your tool.
- **Storey et al. 2020, The Who, What, How of Software Engineering Research**: how the field's papers are distributed across "whom they study, what they produce, and how", and where the gaps are.
- **The call for papers of the conference you are targeting, for that year**, for example the ICSE research track call and its open science policy.

[^shaw2003writing-e38]: Shaw 2003, §2.1. [Evidence](../../../../sources/notes/shaw2003writing.md#e38)
[^shaw2003writing-e26]: Shaw 2003, §3.2. [Evidence](../../../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e11]: Shaw 2003, §4.3. [Evidence](../../../../sources/notes/shaw2003writing.md#e11)
[^shaw2003writing-e9]: Shaw 2003, §4.1. [Evidence](../../../../sources/notes/shaw2003writing.md#e9)
[^icse2026cfp-e1]: ICSE 2026 Research Track call for papers, Research Areas. [Evidence](../../../../sources/notes/icse2026cfp.md#e1)
[^icse2026cfp-e2]: ICSE 2026 Research Track call for papers, Research Areas, list of areas. [Evidence](../../../../sources/notes/icse2026cfp.md#e2)
[^icse2026cfp-e3]: ICSE 2026 Research Track call for papers, Dual Submission Cycles. [Evidence](../../../../sources/notes/icse2026cfp.md#e3)
[^icse2026cfp-e4]: ICSE 2026 Research Track call for papers, Review Criteria. [Evidence](../../../../sources/notes/icse2026cfp.md#e4)
[^icse2026cfp-e5]: ICSE 2026 Research Track call for papers, Review Criteria and Revisions. [Evidence](../../../../sources/notes/icse2026cfp.md#e5)
[^icse2026cfp-e6]: ICSE 2026 Research Track call for papers, Re-submissions of Rejected Papers. [Evidence](../../../../sources/notes/icse2026cfp.md#e6)
[^icse2026cfp-e7]: ICSE 2026 Research Track call for papers, Submission Process. [Evidence](../../../../sources/notes/icse2026cfp.md#e7)
[^icse2026cfp-e8]: ICSE 2026 Research Track call for papers, Submission Process (double-anonymous review). [Evidence](../../../../sources/notes/icse2026cfp.md#e8)
[^icse2026cfp-e9]: ICSE 2026 Research Track call for papers, Submission Process (concurrent submission). [Evidence](../../../../sources/notes/icse2026cfp.md#e9)
[^icse2026cfp-e10]: ICSE 2026 Research Track call for papers, Submission Process (research involving human participants). [Evidence](../../../../sources/notes/icse2026cfp.md#e10)
[^icse2026cfp-e11]: ICSE 2026 Research Track call for papers, Submission Process (journal extensions). [Evidence](../../../../sources/notes/icse2026cfp.md#e11)
[^icse2026cfp-e12]: ICSE 2026 Research Track call for papers, Open Science Policy. [Evidence](../../../../sources/notes/icse2026cfp.md#e12)
[^icse2026cfp-e13]: ICSE 2026 Research Track call for papers, update note at the top. [Evidence](../../../../sources/notes/icse2026cfp.md#e13)
[^icse2026cfp-e14]: ICSE 2026 Research Track call for papers, opening. [Evidence](../../../../sources/notes/icse2026cfp.md#e14)
[^storey2020who-e1]: Storey et al. 2020, §2. [Evidence](../../../../sources/notes/storey2020who.md#e1)
[^storey2020who-e9]: Storey et al. 2020, §6.4. [Evidence](../../../../sources/notes/storey2020who.md#e9)
[^storey2020who-e16]: Storey et al. 2020, Abstract. [Evidence](../../../../sources/notes/storey2020who.md#e16)
[^storey2020who-e17]: Storey et al. 2020, Abstract. [Evidence](../../../../sources/notes/storey2020who.md#e17)
[^storey2020who-e18]: Storey et al. 2020, §1. [Evidence](../../../../sources/notes/storey2020who.md#e18)
[^ralph2020empirical-e142]: SIGSOFT General Standard, General Quality Criteria. [Evidence](../../../../sources/notes/ralph2020empirical.md#e142)
[^ralph2020empirical-e85]: SIGSOFT Engineering Research standard, Essential Attributes (methods). [Evidence](../../../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e92]: SIGSOFT Engineering Research standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e92)
[^ralph2020empirical-e93]: SIGSOFT Engineering Research standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e93)
[^ralph2020empirical-e1]: SIGSOFT Systematic Reviews standard, Definition. [Evidence](../../../../sources/notes/ralph2020empirical.md#e1)
[^ralph2020empirical-e4]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e4)
[^ralph2020empirical-e26]: SIGSOFT General Standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e26)
[^ralph2020empirical-e25]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e139]: SIGSOFT Open Science Supplement, Desirable Attributes and Notes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e139)
[^ralph2020empirical-e140]: SIGSOFT Open Science Supplement, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e140)
[^ralph2020empirical-e135]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e135)
[^ralph2020empirical-e28]: SIGSOFT General Standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e28)
[^ralph2020empirical-e126]: SIGSOFT General Standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e126)
[^easterbrook2008selecting-e74]: Easterbrook et al. 2008, §5.1. [Evidence](../../../../sources/notes/easterbrook2008selecting.md#e74)
[^easterbrook2008selecting-e10]: Easterbrook et al. 2008, §5.2. [Evidence](../../../../sources/notes/easterbrook2008selecting.md#e10)
[^ko2015practical-e7]: Ko et al. 2015, §3.1. [Evidence](../../../../sources/notes/ko2015practical.md#e7)
[^ko2015practical-e28]: Ko et al. 2015, §6.3. [Evidence](../../../../sources/notes/ko2015practical.md#e28)
[^arcuri2014hitchhiker-e2]: Arcuri & Briand 2014, Abstract. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e2)
[^arcuri2014hitchhiker-e4]: Arcuri & Briand 2014, §3. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e4)
