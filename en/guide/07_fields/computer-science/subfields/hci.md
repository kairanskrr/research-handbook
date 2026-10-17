# Human-computer interaction

> This page covers only the practices specific to this area. For practices common to all research, see the chapters of Parts 1 and 2 and the research strategies; for conventions shared across computer science, see the [computer science field overview](../README.md).

## What this area studies

Human-computer interaction (HCI) studies how people use computing technology, and designs and evaluates new ways of interacting with it. It recognizes many kinds of contribution. The 2026 guidelines of the area's flagship conference, CHI (the ACM Conference on Human Factors in Computing Systems; ACM is the Association for Computing Machinery), list the criteria reviewers can use, organized by contribution type[^chi2026papers-e32]. The types include: development or refinement of interface artifacts or interaction techniques; understanding users; systems and tools; methodology; theory; innovation and vision; argument; and validation and replication[^chi2026papers-e40].

Two typical questions:

- **Is a new technique easier to use?** For example, a new menu designed to reduce selection errors usually calls for a careful experiment comparing its error rate with other menus[^chi2026papers-e37].
- **How do people work in a given situation?** For example, in an experiment Mark et al. published at CHI in 2008, 48 participants handled email in a simulated office environment in the lab and were interrupted every two minutes[^mark2008cost-e2]. They found that people completed interrupted tasks faster, but at the cost of more stress and frustration[^mark2008cost-e1].

So within a single area, some people build things, some run experiments, and some do interviews and ethnography. To judge whether a paper is good enough, first work out what kind of contribution it makes.

## Main venues and timeline

The example below is CHI 2026. These are one conference's rules for one year, not those of every conference in the area; they change every year, so **go by the guidelines of the conference you are submitting to, for that year**.

| Item | What CHI 2026 does |
|---|---|
| Size | As of 2025, it expected more than 5,000 submissions[^chi2026papers-e33]; the submission guide says about 75% are usually rejected[^chi2026papers-e2] |
| Deadlines | Abstract and metadata due September 4, 2025; full paper due September 11; decisions on January 15, 2026[^chi2026papers-e35] |
| Author list | Cannot be changed after the abstract deadline[^chi2026papers-e36] |
| Length | Measured in words: short papers up to 5,000 words, standard papers 5,000–12,000 words[^chi2026papers-e5] |
| Over length | Papers over 12,000 words without a valid justification are rejected outright[^chi2026papers-e5] |
| Appendices | Reviewers and area chairs are not required to read appendices or supplementary material[^chi2026papers-e6] |
| Subcommittees | Choose at most two topical subcommittees[^chi2026papers-e10] |
| Review process | "Revise and Resubmit", which replaced the earlier author rebuttal[^chi2026papers-e3] |
| Second round | Papers that pass the first-round bar get 5 weeks to revise, but up to half may still be rejected in the second round[^chi2026papers-e4] |
| Presentation | Authors of accepted papers must present at the conference[^chi2026papers-e34] |

CHI papers are essentially reviewed as submitted; papers that need major changes are rejected[^chi2026papers-e21]. For the general rules on double-blind review and preprints, see [Field overview: double-blind review and preprints](../README.md#double-blind-review-and-preprints). CHI 2026 specifically warns that describing too precisely where a user study was run or where it got ethics approval, or showing authors' faces in figures, can reveal who you are[^chi2026papers-e29]. CHI does not object to posting a paper in non-archival form before or during review, but acknowledges that this makes full anonymity harder[^chi2026papers-e28]. Non-archival formats such as workshop presentations and posters do not count as prior publication[^chi2026papers-e26].

## Common strategies and standards of evidence

The table below is our own summary, based on the CHI 2026 guidelines and other human-computer interaction sources; each standard speaks only for the source in its footnote.

| Strategy | What it looks like in this area | Evidence this area particularly values | How to do it |
|---|---|---|---|
| [Building and improving](../../../05_research-strategies/build_improve.md) | New interaction techniques, interfaces, systems, or tools | Convincing validation showing that the improvement matters in practice[^chi2026papers-e23]; a description detailed enough for others to replicate[^chi2026papers-e38]; a systems paper doesn't necessarily need a user study, but does need appropriate validation[^chi2026papers-e22] | [Engineering research](../practices/engineering_research.md) |
| [Causal explanation](../../../05_research-strategies/explain_causality.md) | Controlled experiments with people, comparing how different interfaces affect them | Be aware that controlled experiments are inherently biased toward tools that can be learned quickly[^ko2015practical-e22] | [Controlled experiments](../../../06_methods/controlled_experiment.md) |
| [Description](../../../05_research-strategies/observe_describe.md) | Understanding users: interviews, field studies, ethnography | Say who was studied and how diverse they were[^chi2026papers-e24]; state the researchers' positionality[^chi2026papers-e16]; make clear how themes emerged from the data[^chi2026papers-e17] | [Interview studies](../../../06_methods/interview_study.md), [Case study and ethnography](../../../06_methods/case_study.md), [Grounded theory](../../../06_methods/grounded_theory.md) |
| [Measurement](../../../05_research-strategies/measure.md) | Measuring users' perceptions with questionnaires and scales | Don't ask "was it useful?" directly; use validated scales[^ko2015practical-e29] | [Questionnaire surveys](../../../06_methods/questionnaire_survey.md), [Scale development](../../../06_methods/scale_development.md) |
| [Interpretation and argument](../../../05_research-strategies/interpret_argue.md) | Argument papers, theoretical contributions | Solid arguments backed by facts, with balanced consideration of other viewpoints[^chi2026papers-e39] | |

Interviews are very common in this area: of the 251 qualitative papers McDonald et al. analyzed, 71.3% used interviews[^mcdonald2019reliability-e3]. Replication is recognized too: CHI's reviewing guide says a constructive replication can be an important contribution in itself[^chi2026papers-e25]; for how to do one, see [Replication studies](../../../06_methods/replication.md).

## Conventions specific to this area

### Reviewers look at the contribution first

The CHI 2026 review form asks reviewers to assess significance, originality, research quality, clarity of presentation, and related work[^chi2026papers-e11][^chi2026papers-e41]. Research quality is judged by the subfield's own definition of rigor[^chi2026papers-e11]; for example, design papers are judged by the standards of the design community, not those of the computational interaction community[^chi2026papers-e7]. Of all these, the contribution and its significance matter most[^chi2026papers-e12].

Two kinds of reviewer comment come up often: the research lacks a theoretical grounding[^chi2026papers-e14], and design choices are not justified[^chi2026papers-e43]. So don't just write what you did; write why you did it that way[^chi2026papers-e14]. Reviewers often reject papers on grounds of quality[^chi2026papers-e42], so think about how you will demonstrate quality at the planning stage, not at the end[^chi2026papers-e13].

CHI 2026 also added an "assisted desk reject": papers that are out of scope, or far below the bar for acceptance, can be rejected without external review[^chi2026papers-e44]. Reasons include data that falls far short of supporting the claims, and a contribution too small for the paper's length[^chi2026papers-e30].

### Match the evaluation to the question

> **Where sources disagree: does every design need a usability evaluation?**
> - **Yes, evaluate**: for interface artifacts and techniques, CHI 2026 expects rigorous, convincing validation, such as empirical studies, usability studies, or field studies[^chi2026papers-e23]. Zhai's view is that, whatever their problems, evaluation methods are better than nothing[^greenberg2008usability-e7]. Even the critics Greenberg and Buxton accept that usability evaluation is valuable in many situations, and that the community should keep doing it in most (but not all) cases[^greenberg2008usability-e6].
> - **Not necessarily**: Greenberg and Buxton argued in 2008 that the choice of evaluation method, and even whether to evaluate at all, must follow from the specific research question[^greenberg2008usability-e1]. Usability evaluation early in design can quash creative ideas that don't fit current conventions[^greenberg2008usability-e2]. Finding one scenario in which a new technique does better is just seeking confirmatory evidence, which is weak validation[^greenberg2008usability-e3]. As they describe it, UIST (the ACM User Interface Software and Technology Symposium) at the time wanted evaluation, but did not insist on it when a design was inspiring and well argued[^greenberg2008usability-e8].
>
> CHI 2026 itself says that how you demonstrate quality depends on the type of contribution: an improvement to a known technique usually calls for a careful experiment, while a system that supports a new way of collaborating might be evaluated under real-world conditions[^chi2026papers-e37]. Greenberg and Buxton's advice: for a truly novel innovation, an "existence proof" may be enough; for mainstream systems or small changes to established ideas, run tests that could prove it wrong[^greenberg2008usability-e4].
>
> In practice: first work out which kind of contribution you are making, then choose a validation that fits it, and explain in the paper why you chose it.

### Transparency and sharing materials

These are requirements from the CHI 2026 submission guide:

- Technical contributions and quantitative studies are expected to be verifiable and reproducible[^chi2026papers-e15].
- Qualitative studies should explain the decisions made and the researchers' positionality[^chi2026papers-e16], and make clear how themes emerged from the data and whether conclusions come from a few striking examples or from general trends[^chi2026papers-e17].
- For studies that ask participants questions, readers should be able to see what was asked and in what exact words[^chi2026papers-e20].
- Code, data, interview guides, and similar materials should preferably go into a public repository with a persistent identifier[^chi2026papers-e18]; if you can't share everything, share as much as you can and explain why the rest can't be shared[^chi2026papers-e19].

### Qualitative research doesn't always compute inter-rater reliability

Inter-rater reliability is a statistic for how far multiple coders agree in their judgments. McDonald et al. sampled publications from CSCW (Computer-Supported Cooperative Work) and human-computer interaction from 2016–2018; only about one in nine of the qualitative papers computed it[^mcdonald2019reliability-e17]. They argue that how you establish reliability should be consistent with the epistemological tradition the researchers work in[^mcdonald2019reliability-e9]. For whether to compute it and how to report it, see [Interview studies: making the analysis credible](../../../06_methods/interview_study.md#step-6-make-your-analysis-trustworthy).

### Research with people, and ethics

- **Ethics review**: CHI 2026 requires research involving human participants to have passed whatever ethics review the authors' research setting requires; since requirements differ from place to place, include a short statement for reviewers[^chi2026papers-e8]. Above the conference there is also an ACM-wide rule: the Policy on Research Involving Human Participants and Subjects, approved by the ACM Publications Board in 2021[^acm2021humanparticipants-e1], which applies to all ACM publications, including conferences ACM sponsors or co-sponsors[^acm2021humanparticipants-e3]. It requires research to be planned, conducted, and reported in line with both local laws and regulations and the general principles the policy lists, such as informed consent[^acm2021humanparticipants-e2]. Where local rules require ethics review, authors must have their research reviewed and be ready to show ACM written proof at any time[^acm2021humanparticipants-e4]. Individual ACM journals or conferences may set stricter requirements[^acm2021humanparticipants-e5]. Papers found to violate the policy may, depending on severity, receive a "Note of Concern" or be retracted[^acm2021humanparticipants-e6]. For general practice, see [Research integrity and ethics](../../../08_throughout/integrity_and_ethics.md).
- **Who was included**: pay attention to who your study included and who it left out, and keep the scope of your claims consistent with that[^chi2026papers-e31].
- **Participants try to please the researcher**: don't just ask "is my tool easy to use?"; for why, and what to do instead, see [Controlled experiments: deciding how to measure](../../../06_methods/controlled_experiment.md#step-5-decide-how-to-measure).
- **Large language models**: CHI 2026 requires any text generated by a large language model to be marked as such whenever the model is used for more than editing the authors' own text[^chi2026papers-e9]. For general practice, see [Research integrity and ethics: when you use large language models and other tools, you are still responsible](../../../08_throughout/integrity_and_ethics.md#6-when-you-use-large-language-models-and-other-tools-you-are-still-responsible).

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Showing a new technique is better in just one scenario that favors it | That is only confirmatory evidence, and weak validation[^greenberg2008usability-e3] |
| Running formal usability tests on early sketches | It can quash unconventional creative ideas[^greenberg2008usability-e2] |
| Leaving evaluation until just before submission | Reviewers often reject papers on grounds of quality[^chi2026papers-e42] |
| Writing what you did but not why you designed it that way | Reviewers often criticize design choices that are not justified[^chi2026papers-e43] |
| Putting key details only in the appendix | CHI 2026 reviewers are not required to read appendices[^chi2026papers-e6] |
| Reporting only percent agreement in a qualitative study | It doesn't account for chance agreement and is widely considered unacceptable[^mcdonald2019reliability-e4] |
| Naming in the methods section the university where you got ethics approval | It reveals who you are[^chi2026papers-e29] |
| Studying a small group of people but claiming the results apply to all users | The scope of your claims must match who your study included[^chi2026papers-e31] |
| Remembering to add an author after the abstract deadline | At CHI 2026 the author list can't be changed after that deadline[^chi2026papers-e36] |

## Further reading

- **The Guide to a Successful Submission and Contributions to CHI for the CHI you are submitting to**: the first explains how reviewers read papers and how to write transparently; the second lists the questions reviewers ask for each contribution type. Read them before you start writing.
- **Greenberg & Buxton 2008, Usability Evaluation Considered Harmful (Some of the Time)**: on when not to use usability evaluation. The CHI 2026 reviewing guide lists it as a reference for the debate over what makes a good CHI paper[^chi2026papers-e45].
- **McDonald, Schoenebeck & Forte 2019, Reliability and Inter-rater Reliability in Qualitative Research**: when to compute inter-rater reliability and when not to. Read it before doing qualitative research.
- **Ko, LaToza & Burnett 2015**: how to design experiments that evaluate tools with human participants, from recruitment to pilot studies.
- Other areas in the same field: [Machine learning](machine_learning.md), [Software engineering](software_engineering.md), [Security](security.md), [Systems](systems.md), [Theory](theory.md), [Programming languages](programming_languages.md).

[^chi2026papers-e32]: CHI 2026, Contributions to CHI. [Evidence](../../../../sources/notes/chi2026papers.md#e32)
[^chi2026papers-e40]: CHI 2026, Contributions to CHI, headings for each contribution type. [Evidence](../../../../sources/notes/chi2026papers.md#e40)
[^chi2026papers-e37]: CHI 2026, Guide to a Successful Submission, Ensuring High-Quality Research. [Evidence](../../../../sources/notes/chi2026papers.md#e37)
[^mark2008cost-e2]: Mark et al. 2008, Experimental Design and Procedure. [Evidence](../../../../sources/notes/mark2008cost.md#e2)
[^mark2008cost-e1]: Mark et al. 2008, Abstract. [Evidence](../../../../sources/notes/mark2008cost.md#e1)
[^chi2026papers-e33]: CHI 2026 call for papers, Select a Subcommittee. [Evidence](../../../../sources/notes/chi2026papers.md#e33)
[^chi2026papers-e2]: CHI 2026, Guide to a Successful Submission, opening. [Evidence](../../../../sources/notes/chi2026papers.md#e2)
[^chi2026papers-e35]: CHI 2026 call for papers, Important Dates. [Evidence](../../../../sources/notes/chi2026papers.md#e35)
[^chi2026papers-e36]: CHI 2026 call for papers, Complete Submission. [Evidence](../../../../sources/notes/chi2026papers.md#e36)
[^chi2026papers-e5]: CHI 2026 call for papers, Important Facts. [Evidence](../../../../sources/notes/chi2026papers.md#e5)
[^chi2026papers-e6]: CHI 2026 call for papers, Important Facts. [Evidence](../../../../sources/notes/chi2026papers.md#e6)
[^chi2026papers-e10]: CHI 2026 call for papers, Select a Subcommittee. [Evidence](../../../../sources/notes/chi2026papers.md#e10)
[^chi2026papers-e3]: CHI 2026, Guide to a Successful Submission, The Review Process. [Evidence](../../../../sources/notes/chi2026papers.md#e3)
[^chi2026papers-e4]: CHI 2026, Papers Review Process, Round 1. [Evidence](../../../../sources/notes/chi2026papers.md#e4)
[^chi2026papers-e34]: CHI 2026 call for papers, Your Paper at the Conference. [Evidence](../../../../sources/notes/chi2026papers.md#e34)
[^chi2026papers-e21]: CHI 2026, Guide to a Successful Submission, Describing the Work Clearly and Concisely. [Evidence](../../../../sources/notes/chi2026papers.md#e21)
[^chi2026papers-e29]: CHI 2026, Anonymization Policy. [Evidence](../../../../sources/notes/chi2026papers.md#e29)
[^chi2026papers-e28]: CHI 2026, Anonymization Policy. [Evidence](../../../../sources/notes/chi2026papers.md#e28)
[^chi2026papers-e26]: CHI 2026, Guide to Reviewing Papers, Prior Publication. [Evidence](../../../../sources/notes/chi2026papers.md#e26)
[^chi2026papers-e23]: CHI 2026, Contributions to CHI, Interface Artifacts or Techniques. [Evidence](../../../../sources/notes/chi2026papers.md#e23)
[^chi2026papers-e38]: CHI 2026, Contributions to CHI, Interface Artifacts or Techniques. [Evidence](../../../../sources/notes/chi2026papers.md#e38)
[^chi2026papers-e22]: CHI 2026, Contributions to CHI, Systems, Tools, Architectures, and Infrastructure. [Evidence](../../../../sources/notes/chi2026papers.md#e22)
[^ko2015practical-e22]: Ko et al. 2015, §4.4. [Evidence](../../../../sources/notes/ko2015practical.md#e22)
[^chi2026papers-e24]: CHI 2026, Contributions to CHI, Understanding Users. [Evidence](../../../../sources/notes/chi2026papers.md#e24)
[^chi2026papers-e16]: CHI 2026, Guide to a Successful Submission, Transparency. [Evidence](../../../../sources/notes/chi2026papers.md#e16)
[^chi2026papers-e17]: CHI 2026, Guide to a Successful Submission, Transparency. [Evidence](../../../../sources/notes/chi2026papers.md#e17)
[^ko2015practical-e29]: Ko et al. 2015, §6.3. [Evidence](../../../../sources/notes/ko2015practical.md#e29)
[^chi2026papers-e39]: CHI 2026, Contributions to CHI, Argument. [Evidence](../../../../sources/notes/chi2026papers.md#e39)
[^mcdonald2019reliability-e3]: McDonald et al. 2019, §4.3. [Evidence](../../../../sources/notes/mcdonald2019reliability.md#e3)
[^chi2026papers-e25]: CHI 2026, Guide to Reviewing Papers, Replicating Work. [Evidence](../../../../sources/notes/chi2026papers.md#e25)
[^chi2026papers-e11]: CHI 2026, Guide to a Successful Submission, The Review Form. [Evidence](../../../../sources/notes/chi2026papers.md#e11)
[^chi2026papers-e41]: CHI 2026, Guide to a Successful Submission, The Review Form. [Evidence](../../../../sources/notes/chi2026papers.md#e41)
[^chi2026papers-e7]: CHI 2026 call for papers, Research Quality. [Evidence](../../../../sources/notes/chi2026papers.md#e7)
[^chi2026papers-e12]: CHI 2026, Guide to a Successful Submission, Making a Significant Contribution. [Evidence](../../../../sources/notes/chi2026papers.md#e12)
[^chi2026papers-e14]: CHI 2026, Guide to a Successful Submission, Ensuring High-Quality Research. [Evidence](../../../../sources/notes/chi2026papers.md#e14)
[^chi2026papers-e43]: CHI 2026, Guide to a Successful Submission, Ensuring High-Quality Research. [Evidence](../../../../sources/notes/chi2026papers.md#e43)
[^chi2026papers-e42]: CHI 2026, Guide to a Successful Submission, Ensuring High-Quality Research. [Evidence](../../../../sources/notes/chi2026papers.md#e42)
[^chi2026papers-e13]: CHI 2026, Guide to a Successful Submission, Ensuring High-Quality Research. [Evidence](../../../../sources/notes/chi2026papers.md#e13)
[^chi2026papers-e44]: CHI 2026, Papers Review Process, Assisted Desk Reject. [Evidence](../../../../sources/notes/chi2026papers.md#e44)
[^chi2026papers-e30]: CHI 2026, Papers Review Process, Assisted Desk Reject. [Evidence](../../../../sources/notes/chi2026papers.md#e30)
[^greenberg2008usability-e7]: Greenberg & Buxton 2008, Related Work (paraphrasing Zhai). [Evidence](../../../../sources/notes/greenberg2008usability.md#e7)
[^greenberg2008usability-e6]: Greenberg & Buxton 2008, Introduction. [Evidence](../../../../sources/notes/greenberg2008usability.md#e6)
[^greenberg2008usability-e1]: Greenberg & Buxton 2008, Abstract. [Evidence](../../../../sources/notes/greenberg2008usability.md#e1)
[^greenberg2008usability-e2]: Greenberg & Buxton 2008, Abstract. [Evidence](../../../../sources/notes/greenberg2008usability.md#e2)
[^greenberg2008usability-e3]: Greenberg & Buxton 2008, Usability Evaluation as Weak Science. [Evidence](../../../../sources/notes/greenberg2008usability.md#e3)
[^greenberg2008usability-e8]: Greenberg & Buxton 2008, What To Do. [Evidence](../../../../sources/notes/greenberg2008usability.md#e8)
[^greenberg2008usability-e4]: Greenberg & Buxton 2008, What To Do. [Evidence](../../../../sources/notes/greenberg2008usability.md#e4)
[^chi2026papers-e15]: CHI 2026, Guide to a Successful Submission, Transparency. [Evidence](../../../../sources/notes/chi2026papers.md#e15)
[^chi2026papers-e20]: CHI 2026, Guide to a Successful Submission, Sharing research material. [Evidence](../../../../sources/notes/chi2026papers.md#e20)
[^chi2026papers-e18]: CHI 2026, Guide to a Successful Submission, Sharing research material. [Evidence](../../../../sources/notes/chi2026papers.md#e18)
[^chi2026papers-e19]: CHI 2026, Guide to a Successful Submission, Sharing research material. [Evidence](../../../../sources/notes/chi2026papers.md#e19)
[^mcdonald2019reliability-e17]: McDonald et al. 2019, Abstract. [Evidence](../../../../sources/notes/mcdonald2019reliability.md#e17)
[^mcdonald2019reliability-e9]: McDonald et al. 2019, §2.3. [Evidence](../../../../sources/notes/mcdonald2019reliability.md#e9)
[^chi2026papers-e8]: CHI 2026 call for papers, Policy on Research Involving Human Participants and Subjects. [Evidence](../../../../sources/notes/chi2026papers.md#e8)
[^acm2021humanparticipants-e1]: ACM 2021 Policy on Research Involving Human Participants, below the title. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e1)
[^acm2021humanparticipants-e2]: ACM 2021 Policy on Research Involving Human Participants, Policy Statement. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e2)
[^acm2021humanparticipants-e3]: ACM 2021 Policy on Research Involving Human Participants, Scope of Policy. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e3)
[^acm2021humanparticipants-e4]: ACM 2021 Policy on Research Involving Human Participants, Roles and Responsibilities (Authors). [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e4)
[^acm2021humanparticipants-e5]: ACM 2021 Policy on Research Involving Human Participants, Policy Statement. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e5)
[^acm2021humanparticipants-e6]: ACM 2021 Policy on Research Involving Human Participants, Violations and Penalties. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e6)
[^chi2026papers-e31]: CHI 2026, Guide to a Successful Submission, Maximizing Impact. [Evidence](../../../../sources/notes/chi2026papers.md#e31)
[^chi2026papers-e9]: CHI 2026 call for papers, Policy on Use of Large Language Models. [Evidence](../../../../sources/notes/chi2026papers.md#e9)
[^mcdonald2019reliability-e4]: McDonald et al. 2019, §2.2. [Evidence](../../../../sources/notes/mcdonald2019reliability.md#e4)
[^chi2026papers-e45]: CHI 2026, Guide to Reviewing Papers, References. [Evidence](../../../../sources/notes/chi2026papers.md#e45)
