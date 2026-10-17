# Computer science: field overview

This page explains how research actually works in computer science: publishing that centers on conferences, preprints, artifact evaluation, and the rhythm and conventions that come with them. For what applies in every field (choosing a topic, planning, writing, peer review and responding to reviews, research ethics), see the chapters of Part 1, Part 2, and Writing and publishing, as well as [Throughout the project](../../08_throughout/README.md); the full table of contents is in the [The handbook](../../README.md). This page doesn't repeat them. For the research strategies computer science commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence); for how to carry out a particular kind of study, see [Kinds of research](#kinds-of-research) at the end.

**After reading this page, you should be able to:**

- explain the steps a computer science paper goes through from submission to publication;
- understand the place of conferences, preprints, and artifact evaluation in this field, and the debates around them;
- know which special conventions your own research area has, and where to look them up;
- name the research strategies computer science commonly uses, and what evidence and standards each one is judged by;
- avoid the mistakes newcomers make most often with deadlines, anonymity, preprints, and artifacts.

---

## How research works in this field

### Conferences are the main publication venue

In most fields, "publishing" means publishing in a journal. Computer science is different: conference proceedings are the main publication venue, and a paper at a top conference is a full research output, not a "conference abstract" `[Our analysis]`. Moshe Vardi, editor-in-chief of *Communications of the ACM* (CACM; ACM is the Association for Computing Machinery), wrote that, as far as he knew, computer science is the only field that treats conference publication as its primary means of publishing[^vardi2009conferences-e1]. A 1999 memo from the Computing Research Association (CRA) states plainly that the field gives more weight to conference publication[^cra1999evaluating-e1]; in experimental areas, top conferences are usually harder to get into than top journals[^cra1999evaluating-e3].

Theory is an exception: theoreticians value conferences too, but there is a long tradition of completing and expanding conference papers into journal versions[^cra1999evaluating-e4].

Computer science has one more underlying feature: many of the things it studies are built by people. Building something new is not a contribution in itself; **you must show that it is better**[^cra1999evaluating-e6]. So most papers in the field answer "how is the new method better than existing ones, and by how much?", and how well the evaluation is done decides the paper's fate `[Our analysis]`. For how to make a fair comparison, see [Comparative evaluation](../../05_research-strategies/compare_evaluate.md#2-what-evidence-is-enough).

### The life of a conference paper

The process is much the same across conferences. The examples below use USENIX Security (the top security conference run by the USENIX Association) and NeurIPS (Conference on Neural Information Processing Systems) in machine learning. Dates and rules change every year, so **always go by the current year's call for papers of the conference you are submitting to**:

| Step | What happens | Example |
|---|---|---|
| Call for papers (CFP) | Announces the deadlines, page limits, anonymity rules, and ethics and artifact requirements | NeurIPS limits the main text to 9 pages, including figures and tables[^neurips2025cfp-e2] |
| Deadline | Often you register the title and abstract first and submit the full paper a few days later; deadlines are usually "Anywhere on Earth" (AoE) | NeurIPS 2025: abstracts due May 11, full papers May 15[^neurips2025cfp-e1] |
| Program committee (PC) review | Committee members review the papers; large conferences also have area chairs (ACs), who synthesize the reviews and take part in the decision `[Our analysis]` | Some conferences send "early rejection" notices first[^usenixsec2026cfp-e1] |
| Author response (rebuttal) | After seeing the initial reviews, authors reply in writing within a very short window | NeurIPS allows one week[^neurips2025cfp-e8] |
| Decision and camera-ready | If accepted, you revise according to the reviews and submit the final version | |
| Artifact evaluation (some areas) | After acceptance you separately submit code, data, and so on; a dedicated committee evaluates them and awards badges | See below |
| Presentation | You present the paper at the conference and talk with peers in person | |

Some conferences have several submission cycles a year. USENIX Security 2026, for example, has two cycles, each with its own fixed dates for the deadline, early rejection, the author response period, and so on[^usenixsec2026cfp-e1].

The rebuttal is an important step at computer science conferences. Its readers are not only the reviewers but also the area chair, who may read only the reviews and your response[^parikh2020rebuttals-e2]. For how to write one, see [Reviews, revision, and what to do after rejection](../../03_write-and-publish/03_review-and-revision.md).

### Double-blind review and preprints

Many conferences use **double-blind review**: reviewers don't know who the authors are, and authors don't know who the reviewers are. A submission must not contain anything that could reveal the authors' identity[^neurips2025cfp-e4]; when you cite your own earlier work, cite it in the third person, as if it were someone else's[^usenixsec2026cfp-e4]. Lance Fortnow lists improvements conferences have tried, including hiding author names and letting authors respond to initial reviews[^fortnow2009time-e4].

At the same time, posting papers on arXiv (a free preprint server) is widespread in the field. Double-blind review and preprints look contradictory; most conferences handle this by **allowing preprints, as long as you don't deliberately reveal your identity**:

- NeurIPS: posting a non-anonymous preprint on arXiv or elsewhere will not get a paper rejected, and reviewers are asked not to go looking for it[^neurips2025cfp-e5]; but the public version should not say anything like "under review at NeurIPS"[^neurips2025cfp-e6].
- USENIX Security: during review, authors may still give talks, post preprints, and disclose vulnerabilities[^usenixsec2026cfp-e3].
- The ACM SIGSOFT (ACM Special Interest Group on Software Engineering) Empirical Standards (review criteria for papers, organized by research method, from the software engineering community): a preprint does not count as "published"[^ralph2020empirical-e141].

Watch where "published" begins: NeurIPS accepts papers that were presented at a workshop, as long as they did not appear in formal proceedings[^neurips2025cfp-e7]. Submitting the same work to several venues at once is dishonest[^usenixsec2026cfp-e11].

### Artifact evaluation and badges

Experimental computer science has an important tradition: share what you build with other researchers whenever possible[^cra1999evaluating-e5]. An **artifact** here means the code, data, systems, proof scripts, and so on behind a paper. ACM's position is that an experimental result is not fully established until it can be independently reproduced[^acm2020artifact-e9].

To support this, ACM defines three independent kinds of badge[^acm2020artifact-e11]:

| Badge | What it means |
|---|---|
| Artifacts Evaluated | Two levels. **Functional**: documented, consistent with the paper, complete, exercisable, and including appropriate evidence of verification and validation[^acm2020artifact-e2]; **Reusable**: on top of that, carefully documented and well structured, so others can easily reuse and repurpose it[^acm2020artifact-e12] |
| Artifacts Available | Placed in a publicly accessible archival repository, with a DOI (Digital Object Identifier, a permanent link) or a link with a unique identifier; a personal web page does not count[^acm2020artifact-e4][^acm2020artifact-e13] |
| Results Validated | Two kinds. **Reproduced**: someone other than the authors obtained the paper's main results, partly using the artifacts you provided; **Replicated**: someone other than the authors obtained the main results independently, without your artifacts[^acm2020artifact-e5]. The numbers need not match exactly, only agree within the tolerance acceptable for that kind of experiment[^acm2020artifact-e14] |

Artifact evaluation is usually **voluntary**[^acm2020artifact-e10]. In systems, it mostly happens after the paper is accepted[^sysartifactsguide-e1], and the criterion is whether the artifact meets the expectations the paper itself sets[^sysartifactsguide-e4]. Participation is already common: at OSDI 2023 (the USENIX Symposium on Operating Systems Design and Implementation, a top systems conference), 64% of accepted papers took part in artifact evaluation[^sysartifactsguide-e3]. Some conferences go further: USENIX Security 2026 requires artifacts to be available during review, and if you can't provide them you must explain why[^usenixsec2026cfp-e12]; NeurIPS encourages accepted papers to submit code and data as well[^neurips2025cfp-e10].

---

## How this field differs from others

### Conferences or journals: a long-running debate

The main differences between the two `[Our analysis, based on the sources below]`:

| | Conferences | Journals |
|---|---|---|
| Review | Fixed schedule, one decision; the author response window is short (one week at NeurIPS)[^neurips2025cfp-e8], and usually you get only one chance to respond `[Our analysis]` | Multiple rounds of revision possible |
| Speed | Fast (7 months, by CRA's 1999 figures)[^cra1999evaluating-e2] | Slow (same source: 1 to 2 years) |
| Length | Strict page limits, less time to polish[^cra1999evaluating-e7] | More flexible |
| Status in the field | Most research areas center on top conferences | Theory often expands conference papers into journal versions[^cra1999evaluating-e4] |

> **Where sources disagree: is a conference-centered system a good thing?**
> - **For**: the 1999 CRA memo argues that, for experimental areas, conference publication is faster (7 months versus 1 to 2 years at the time), lets you present to peers in person, and gets each paper more reviews (4 or 5 versus 2 or 3)[^cra1999evaluating-e2]; the only drawbacks are strict page limits and less time to polish[^cra1999evaluating-e7].
> - **Against**: Vardi argues that program committees review under enormous pressure of time and workload, and cannot achieve careful scrutiny[^vardi2009conferences-e2]; journal versions of conference papers are expected, but only a small fraction ever appear[^vardi2009conferences-e3]. Fast dissemination doesn't require conferences either: physicists achieve it with arXiv preprints[^vardi2009conferences-e4]. Fortnow proposes using preprint servers for fast dissemination and journals for evaluating researchers[^fortnow2009time-e7].
>
> For a newcomer, the debate doesn't change reality: in hiring, people look first at which conferences a candidate has published in[^fortnow2009time-e6]. In practice: **submit according to your research area's conventions**, stay aware of the limits of conference review, and don't read too much into any single acceptance or rejection.

### Deadlines set the pace, at a cost

Conferences have fixed deadlines, and the whole field's rhythm revolves around them. That brings efficiency, and side effects. Fortnow points out that:

- the conference model pushes research toward short-term, deadline-driven work[^fortnow2009time-e1];
- people submit when the deadline comes rather than when the research is ready, and many publish only the "least publishable unit"[^fortnow2009time-e2];
- program committees decide by consensus, which favors safe incremental work over papers that open new directions[^fortnow2009time-e3];
- the outcome for very good and very bad papers is fairly predictable; the trouble is the large group of solid papers in the middle, whose outcomes are the hardest to predict[^fortnow2009time-e5]. Nearly half of Gödel Prize winners (the prize for outstanding papers in theoretical computer science) were originally rejected by, or never appeared in, the top theory conferences[^fortnow2009time-e8].

### Conventions differ across research areas

Research areas in computer science differ a lot. To judge whether a paper is good enough, you need to know the standards of the target conference and its community[^hicks2014reviewing-e9]. The venues, reviewing priorities, and standards of evidence specific to each area are on the area pages under [Areas of computer science](subfields/README.md).

The table below gives one example for each. Most are one conference's rules for one year, not general rules for the whole area; **always go by the current year's call for papers of the conference you are submitting to**.

| Area | A convention worth knowing (example) |
|---|---|
| [Theory](subfields/theory.md) | Theoreticians value conferences too, but there is a long tradition of completing and expanding conference papers into journal versions[^cra1999evaluating-e4] |
| [Systems](subfields/systems.md) | At OSDI 2024 (the Symposium on Operating Systems Design and Implementation), for example, the time between acceptance and artifact submission was very short, so you should prepare your artifact while the paper is still under review[^sysartifactsguide-e2] |
| [Security](subfields/security.md) | USENIX Security 2026 requires every submission to discuss research ethics[^usenixsec2026cfp-e2]; for vulnerability disclosure, see below |
| [Machine learning](subfields/machine_learning.md) | At NeurIPS 2025, for example: posting a non-anonymous preprint will not get a paper rejected[^neurips2025cfp-e5]; submissions must fill in the paper checklist[^neurips2025cfp-e3]; reviews and discussions of accepted papers are made public[^neurips2025cfp-e9] |
| [Software engineering](subfields/software_engineering.md) | The SIGSOFT Empirical Standards hold that there is no universal quality standard: different research methods have different review criteria[^ralph2020empirical-e142] |
| [Programming languages](subfields/programming_languages.md) | The empirical evaluation checklist from SIGPLAN (ACM Special Interest Group on Programming Languages) says that artifact evaluation usually happens after paper review and checks whether the paper's claims and evidence are consistent with the artifact[^blackburn2018sigplan-e31] |
| [Human-computer interaction](subfields/hci.md) | Among the qualitative papers McDonald et al. surveyed, only about one in nine calculated inter-rater reliability (how far several coders agree)[^mcdonald2019reliability-e2] |

### Ethics issues specific to this field

For general ethical principles, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md). In computer science, especially in security and network measurement, a few points need particular attention:

- **Disclose vulnerabilities privately first, then publicly.** Going public before you have told the responsible party and the vulnerability has been fixed can cause harm[^usenixsec2026cfp-e5]; the paper should say whom you disclosed to and what came of it[^usenixsec2026cfp-e6].
- **Institutional review board (IRB) approval does not mean there are no ethical issues.** An IRB may not know the norms of computer security research; even with approval, you still need to do your own analysis[^usenixsec2026cfp-e7].
- **Use the Menlo Report as a framework for analysis.** It sets out ethical principles for information and communication technology research, and USENIX Security recommends that authors be familiar with it[^usenixsec2026cfp-e10]. Its four principles are summarized in [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first).
- **Think about ethics as early as possible**[^usenixsec2026cfp-e9]. Sometimes the most ethical choice is not to do the research, or not to publish it once done[^usenixsec2026cfp-e8].
- **Clearly flag artifacts that could cause damage**, so evaluators can take precautions in advance[^sysartifactsguide-e7].

The software engineering empirical standards also list acknowledging and mitigating the potential risks and harms of the research as an essential attribute[^ralph2020empirical-e65].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by its central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists the seven strategies common in computer science research (the eighth, Interpretation and argument, is mostly found in the humanities and social sciences and is left out here), along with the evidence each usually relies on and the standards reviewers judge it by.

The grouping in the table and the summaries in the "What it looks like in computer science" column are our own; each standard speaks only for the research area named in its footnote (mostly software engineering, machine learning, and security), and our sources do not cover other areas `[Our analysis]`.

| Strategy | What it looks like in computer science | Typical evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Propose a new method, tool, or system. At ICSE (International Conference on Software Engineering), the top software engineering conference, the most common kind of paper reports a new technique[^shaw2003writing-e26] | The software engineering review criteria require an empirical comparison against the best current alternatives, or a justification if that isn't possible[^ralph2020empirical-e85]; in machine learning, proposing many changes at once without ablation studies makes it impossible to tell where the gains come from[^lipton2019troubling-e4]; ideally, release the source code and input data[^ralph2020empirical-e87]; some areas also have [artifact evaluation](#artifact-evaluation-and-badges) | [Engineering research](practices/engineering_research.md), [Optimization studies](practices/optimization_study.md) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Compare existing methods, tools, or systems on a common benchmark. The software engineering review criteria treat this separately as "benchmarking"[^ralph2020empirical-e143] | The configurations being tested compete on their merits, without artificial handicaps[^ralph2020empirical-e149]; discuss whether the benchmark measures what it is meant to measure[^ralph2020empirical-e100]; run tools with randomness enough times and use statistical tests to confirm differences are not due to chance (from fuzzing research)[^klees2018evaluating-e10] | [Benchmarking](practices/benchmarking.md) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Software engineering often asks whether a tool or technique improves quality or speed[^easterbrook2008selecting-e57] | The strongest empirical papers in machine learning often include error analysis, ablation studies, and robustness checks[^lipton2019troubling-e8]; before claiming causation from observational data, the software engineering standards require establishing covariation and temporal order, ruling out third variables, and proposing at least one causal mechanism[^ralph2020empirical-e203] | [Controlled experiments](../../06_methods/controlled_experiment.md), [Data science](../../06_methods/data_science.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Describe what a phenomenon or population is like. For example, a questionnaire survey describing a phenomenon or population in detail[^ralph2020empirical-e234]; repository mining showing that most projects on GitHub are personal and inactive[^kalliamvakou2014promises-e1] | The software engineering standard for repository mining requires validated measures, or a check of construct validity yourself[^ralph2020empirical-e112]; manual labeling should use multiple raters and assess inter-rater agreement[^ralph2020empirical-e111] | [Mining software repositories](practices/repository_mining.md), [Questionnaire surveys](../../06_methods/questionnaire_survey.md) |
| [Measurement](../../05_research-strategies/measure.md) | Check whether benchmarks and metrics themselves can be trusted | Benchmarking must discuss construct validity[^ralph2020empirical-e100]; in machine learning, check for data contamination, which overestimates model performance[^sainz2023nlp-e2] | [Benchmarking: is the benchmark itself valid?](practices/benchmarking.md#3-is-the-benchmark-itself-valid) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Systematic reviews, mapping studies, case surveys. The software engineering review criteria have dedicated standards for systematic reviews[^ralph2020empirical-e1] and case surveys[^ralph2020empirical-e291] | Describe the search process and selection criteria step by step and reproducibly[^ralph2020empirical-e4]; show a clear chain of evidence from the extracted data to the answers to the questions[^ralph2020empirical-e6] | [Review studies](../../06_methods/review_study.md), [Case survey](../../06_methods/case_survey.md) |
| [Proof](../../05_research-strategies/prove.md) | Theoretical computer science, and the formal-methods side of software engineering, systems, and security | A formal model must be backed by rigorous derivation and proof, not by one or two simple examples[^shaw2003writing-e9]; systems where errors are costly can get machine-checked proofs: the seL4 kernel, for example, was verified by machine-checked proof all the way from its abstract specification to its C implementation[^klein2009sel4-e8] | [Theoretical research](practices/theoretical_research.md) |

How to use this table `[Our analysis]`:

- **First find your strategy from your central claim**, then read the matching strategy page and practice page. Many computer science papers are mixed, for example proposing a new tool and also proving one of its properties. In that case, let the central claim determine the main strategy, and hold each of the other parts to its own strategy's standards.
- **For the same strategy, "good enough" differs across research areas.** The software engineering review criteria say explicitly that there is no universal quality standard: each study should be judged by the standards of the method that suits it[^ralph2020empirical-e142]; to judge whether a paper is good enough, you also need to know the standards of the target conference and its community[^hicks2014reviewing-e9]. For the specific conventions of each area, see [Conventions differ across research areas](#conventions-differ-across-research-areas) above.

---

## Advice for newcomers

1. **Read your target conference's call for papers from start to finish.** Page limits, anonymity rules, preprint policy, ethics discussion, artifact requirements: every conference differs, so write to your target conference's call. Also read the existing guidelines for your kind of study; starting without reading them is an antipattern the software engineering empirical standards name explicitly[^ralph2020empirical-e26].
2. **Plan backward from the deadline.** Conference deadlines are fixed and won't move for you. For how to schedule backward, leave time for your advisor to read drafts, and set internal group deadlines, see [Planning and daily routines](../../08_throughout/planning_and_routines.md) and [Writing a research plan](../../02_do-the-project/03_research-plan.md).
3. **Start preparing your artifact while the paper is still under review.** The time between acceptance and artifact submission is very short[^sysartifactsguide-e2]. If there are complex dependencies, package them in a container or virtual machine[^sysartifactsguide-e6]; follow your own instructions once in a fresh environment[^sysartifactsguide-e5]. For general practice in organizing code and data, see [Organizing your research materials](../../08_throughout/organizing_materials.md).
4. **Check the policy before posting a preprint, and don't break anonymity once you have.** Don't write "under review at conference X" in the public version[^neurips2025cfp-e6], and cite your own work in the third person in the submitted version[^usenixsec2026cfp-e4].
5. **Treat the rebuttal as a formal step and prepare for it.** The response window is often only about a week[^neurips2025cfp-e8], and the area chair reads it too; for how to write it, see [Reviews, revision, and what to do after rejection](../../03_write-and-publish/03_review-and-revision.md).
6. **Don't let deadlines push you into submitting half-finished work.** When the research isn't ready, waiting for the next deadline is often better than forcing a submission[^fortnow2009time-e2] `[Our analysis]`.
7. **Rejection is normal; don't judge the value of your work by a single outcome.** For solid papers in the middle tier, outcomes are the hardest to predict[^fortnow2009time-e5].

---

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Writing to another conference's format without reading the call for papers | Page limits, anonymity, ethics discussion, and other requirements all differ; follow your target conference's call |
| Writing "our previous work [5]" in a submission, or linking to a code repository under your own name | Violates the anonymity requirements[^neurips2025cfp-e4][^usenixsec2026cfp-e4] |
| Writing "under review at NeurIPS" on a preprint | The conference explicitly forbids it[^neurips2025cfp-e6] |
| Submitting the same work to two conferences at once | It is dishonest[^usenixsec2026cfp-e11] |
| Starting to clean up your code only after acceptance, and missing artifact evaluation | The time between acceptance and artifact submission is very short[^sysartifactsguide-e2] |
| Treating an artifact on your personal web page as "publicly available" | Doesn't meet the long-term archiving requirement of the Available badge[^acm2020artifact-e13] |
| Publishing a vulnerability before notifying the vendor | Going public before a fix can harm users[^usenixsec2026cfp-e5] |
| Assuming IRB approval means you don't need an ethics analysis | IRB approval is no substitute for an ethics analysis[^usenixsec2026cfp-e7] |
| Judging a paper from one research area by another area's standards | There is no universal quality standard; different research methods have different review criteria[^ralph2020empirical-e142] |

---

## Kinds of research

The specific approaches computer science research uses fall into two groups: research practices used only in computer science live in this section on computer science; research methods other fields also use live in the [Research types](../../06_methods/README.md) section. For which strategy each one serves, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) above.

The same approach can have different requirements in different research areas (see [Conventions differ across research areas](#conventions-differ-across-research-areas) above); for each area's own rules, see [Areas of computer science](subfields/README.md).

### Research practices specific to computer science

For an overview, see [Research practices specific to computer science](practices/README.md).

- [Engineering research](practices/engineering_research.md): propose and evaluate a new method, tool, or system
- [Optimization studies](practices/optimization_study.md): frame a problem as an optimization problem and solve it with search or similar methods
- [Benchmarking](practices/benchmarking.md): compare systems, tools, or models with an automated, repeatable procedure
- [Mining software repositories](practices/repository_mining.md): analyze software development data such as code repositories and bug reports
- [Theoretical research](practices/theoretical_research.md): proofs and formal analysis

### Research types shared with other fields

**Working with the literature**
- [Review studies](../../06_methods/review_study.md): systematic reviews, mapping studies, and review papers
- [Case survey](../../06_methods/case_survey.md): code a large number of published cases as data, then analyze them quantitatively
- [Methodology research and meta-science](../../06_methods/meta_science.md): study research methods themselves and make recommendations about them

**Working with existing data**
- [Data science](../../06_methods/data_science.md): draw conclusions from existing data with predictive or statistical models
- [Longitudinal studies](../../06_methods/longitudinal_study.md): observe the same subjects repeatedly over a long period

**Research involving people**
- [Controlled experiments](../../06_methods/controlled_experiment.md): experiments with human participants
- [Questionnaire surveys](../../06_methods/questionnaire_survey.md): collect data from many people with a questionnaire
- [Interview studies](../../06_methods/interview_study.md): in-depth interviews, followed by identifying themes
- [Case study and ethnography](../../06_methods/case_study.md): study a few cases in depth in their real setting
- [Grounded theory](../../06_methods/grounded_theory.md): build theory step by step from the data
- [Action research](../../06_methods/action_research.md): the researcher takes part in improving a real organization, researching while improving it

**Simulation and cross-cutting methods**
- [Quantitative simulation](../../06_methods/simulation_study.md): use a computational model to simulate a system or process
- [Replication studies](../../06_methods/replication.md): redo a published study in a planned way
- [Mixed methods](../../06_methods/mixed_methods.md): use two or more methods on the same question

---

## Further reading

- **CRA 1999, Evaluating Computer Scientists and Engineers for Promotion and Tenure**: short, and explains clearly why the field centers on conferences and why it values artifacts. For anyone who wants to know where the field's publishing culture came from.
- **Vardi 2009 and Fortnow 2009 (CACM)**: two well-known critiques of conference culture. For anyone who wants to understand the limits of conference review and the cost of deadline-driven research.
- **ACM Artifact Review and Badging**: the formal definitions of the badges, and the difference between the terms repeatable, reproducible, and replicable. Read it before preparing for artifact evaluation.
- **The packaging guide at sysartifacts.github.io**: a hands-on guide to artifact evaluation in systems, covering choice of format, tools, and tips.
- **The call for papers of the conference you are submitting to**, for example USENIX Security's ethics guidelines or NeurIPS's preprint and double-blind policy. Reread it before every submission.

[^cra1999evaluating-e1]: Computing Research Association (CRA) 1999 (Patterson, Snyder, Ullman), opening. [Evidence](../../../sources/notes/cra1999evaluating.md#e1)
[^cra1999evaluating-e2]: Computing Research Association (CRA) 1999, Structure of The Field. [Evidence](../../../sources/notes/cra1999evaluating.md#e2)
[^cra1999evaluating-e3]: Computing Research Association (CRA) 1999, Structure of The Field. [Evidence](../../../sources/notes/cra1999evaluating.md#e3)
[^cra1999evaluating-e4]: Computing Research Association (CRA) 1999, Structure of The Field. [Evidence](../../../sources/notes/cra1999evaluating.md#e4)
[^cra1999evaluating-e5]: Computing Research Association (CRA) 1999, Structure of The Field. [Evidence](../../../sources/notes/cra1999evaluating.md#e5)
[^cra1999evaluating-e6]: Computing Research Association (CRA) 1999, Structure of The Field (quoting Fred Brooks). [Evidence](../../../sources/notes/cra1999evaluating.md#e6)
[^cra1999evaluating-e7]: Computing Research Association (CRA) 1999, Structure of The Field. [Evidence](../../../sources/notes/cra1999evaluating.md#e7)
[^vardi2009conferences-e1]: Vardi 2009, main text, para. 2. [Evidence](../../../sources/notes/vardi2009conferences.md#e1)
[^vardi2009conferences-e2]: Vardi 2009, main text, para. 6. [Evidence](../../../sources/notes/vardi2009conferences.md#e2)
[^vardi2009conferences-e3]: Vardi 2009, main text, para. 6. [Evidence](../../../sources/notes/vardi2009conferences.md#e3)
[^vardi2009conferences-e4]: Vardi 2009, main text, para. 7. [Evidence](../../../sources/notes/vardi2009conferences.md#e4)
[^fortnow2009time-e1]: Fortnow 2009, abstract paragraph. [Evidence](../../../sources/notes/fortnow2009time.md#e1)
[^fortnow2009time-e2]: Fortnow 2009, main text. [Evidence](../../../sources/notes/fortnow2009time.md#e2)
[^fortnow2009time-e3]: Fortnow 2009, main text. [Evidence](../../../sources/notes/fortnow2009time.md#e3)
[^fortnow2009time-e4]: Fortnow 2009, main text. [Evidence](../../../sources/notes/fortnow2009time.md#e4)
[^fortnow2009time-e5]: Fortnow 2009, main text. [Evidence](../../../sources/notes/fortnow2009time.md#e5)
[^fortnow2009time-e6]: Fortnow 2009, main text. [Evidence](../../../sources/notes/fortnow2009time.md#e6)
[^fortnow2009time-e7]: Fortnow 2009, abstract paragraph. [Evidence](../../../sources/notes/fortnow2009time.md#e7)
[^fortnow2009time-e8]: Fortnow 2009, main text. [Evidence](../../../sources/notes/fortnow2009time.md#e8)
[^acm2020artifact-e9]: ACM Artifact Review and Badging v1.1, opening. [Evidence](../../../sources/notes/acm2020artifact.md#e9)
[^acm2020artifact-e10]: ACM Artifact Review and Badging v1.1, opening. [Evidence](../../../sources/notes/acm2020artifact.md#e10)
[^acm2020artifact-e11]: ACM Artifact Review and Badging v1.1, Badging. [Evidence](../../../sources/notes/acm2020artifact.md#e11)
[^acm2020artifact-e2]: ACM Artifact Review and Badging v1.1, Artifacts Evaluated – Functional. [Evidence](../../../sources/notes/acm2020artifact.md#e2)
[^acm2020artifact-e12]: ACM Artifact Review and Badging v1.1, Artifacts Evaluated – Reusable. [Evidence](../../../sources/notes/acm2020artifact.md#e12)
[^acm2020artifact-e4]: ACM Artifact Review and Badging v1.1, Artifacts Available. [Evidence](../../../sources/notes/acm2020artifact.md#e4)
[^acm2020artifact-e5]: ACM Artifact Review and Badging v1.1, Results Validated. [Evidence](../../../sources/notes/acm2020artifact.md#e5)
[^acm2020artifact-e13]: ACM Artifact Review and Badging v1.1, Artifacts Available. [Evidence](../../../sources/notes/acm2020artifact.md#e13)
[^acm2020artifact-e14]: ACM Artifact Review and Badging v1.1, Results Validated. [Evidence](../../../sources/notes/acm2020artifact.md#e14)
[^sysartifactsguide-e1]: sysartifacts, OSDI '24 Call for Artifacts, Benefits and Goals. [Evidence](../../../sources/notes/sysartifactsguide.md#e1)
[^sysartifactsguide-e2]: sysartifacts, OSDI '24 Call for Artifacts, Overview. [Evidence](../../../sources/notes/sysartifactsguide.md#e2)
[^sysartifactsguide-e3]: sysartifacts, OSDI '24 Call for Artifacts, Overview. [Evidence](../../../sources/notes/sysartifactsguide.md#e3)
[^sysartifactsguide-e4]: sysartifacts, OSDI '24 Call for Artifacts, Criteria. [Evidence](../../../sources/notes/sysartifactsguide.md#e4)
[^sysartifactsguide-e5]: sysartifacts, packaging guide, Tools and tips. [Evidence](../../../sources/notes/sysartifactsguide.md#e5)
[^sysartifactsguide-e6]: sysartifacts, packaging guide, Formats. [Evidence](../../../sources/notes/sysartifactsguide.md#e6)
[^sysartifactsguide-e7]: sysartifacts, packaging guide, Formats. [Evidence](../../../sources/notes/sysartifactsguide.md#e7)
[^usenixsec2026cfp-e1]: USENIX Security '26 call for papers, Important Dates. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e1)
[^usenixsec2026cfp-e2]: USENIX Security '26 call for papers, Executive Summary. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e2)
[^usenixsec2026cfp-e3]: USENIX Security '26 call for papers, Anonymous Submission. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e3)
[^usenixsec2026cfp-e4]: USENIX Security '26 call for papers, Anonymous Submission. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e4)
[^usenixsec2026cfp-e5]: USENIX Security '26 ethics guidelines, Disclosures. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e5)
[^usenixsec2026cfp-e6]: USENIX Security '26 ethics guidelines, Disclosures. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e7]: USENIX Security '26 ethics guidelines, the IRB question. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e7)
[^usenixsec2026cfp-e8]: USENIX Security '26 ethics guidelines. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e8)
[^usenixsec2026cfp-e9]: USENIX Security '26 ethics guidelines, when to start thinking about ethics. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e9)
[^usenixsec2026cfp-e10]: USENIX Security '26 ethics guidelines. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e10)
[^usenixsec2026cfp-e11]: USENIX Security '26 call for papers, Simultaneous Submission and Plagiarism. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e11)
[^usenixsec2026cfp-e12]: USENIX Security '26 call for papers, Executive Summary. [Evidence](../../../sources/notes/usenixsec2026cfp.md#e12)
[^neurips2025cfp-e1]: NeurIPS 2025 Call for Papers, date list. [Evidence](../../../sources/notes/neurips2025cfp.md#e1)
[^neurips2025cfp-e2]: NeurIPS 2025 Call for Papers, Paper Formatting Instructions. [Evidence](../../../sources/notes/neurips2025cfp.md#e2)
[^neurips2025cfp-e3]: NeurIPS 2025 Call for Papers, Paper Checklist. [Evidence](../../../sources/notes/neurips2025cfp.md#e3)
[^neurips2025cfp-e4]: NeurIPS 2025 Call for Papers, Double-blind Reviewing. [Evidence](../../../sources/notes/neurips2025cfp.md#e4)
[^neurips2025cfp-e5]: NeurIPS 2025 Call for Papers, Preprints. [Evidence](../../../sources/notes/neurips2025cfp.md#e5)
[^neurips2025cfp-e6]: NeurIPS 2025 Call for Papers, Preprints. [Evidence](../../../sources/notes/neurips2025cfp.md#e6)
[^neurips2025cfp-e7]: NeurIPS 2025 Call for Papers, Dual Submissions. [Evidence](../../../sources/notes/neurips2025cfp.md#e7)
[^neurips2025cfp-e8]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../../sources/notes/neurips2025cfp.md#e8)
[^neurips2025cfp-e9]: NeurIPS 2025 Call for Papers, Publication of Accepted Submissions. [Evidence](../../../sources/notes/neurips2025cfp.md#e9)
[^neurips2025cfp-e10]: NeurIPS 2025 Call for Papers, Publication of Accepted Submissions. [Evidence](../../../sources/notes/neurips2025cfp.md#e10)
[^ralph2020empirical-e141]: SIGSOFT General Standard, Initial Checks. [Evidence](../../../sources/notes/ralph2020empirical.md#e141)
[^ralph2020empirical-e142]: SIGSOFT General Standard, General Quality Criteria. [Evidence](../../../sources/notes/ralph2020empirical.md#e142)
[^ralph2020empirical-e65]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e65)
[^ralph2020empirical-e26]: SIGSOFT General Standard, Antipatterns. [Evidence](../../../sources/notes/ralph2020empirical.md#e26)
[^hicks2014reviewing-e9]: Hicks 2014, Interesting or useful? [Evidence](../../../sources/notes/hicks2014reviewing.md#e9)
[^parikh2020rebuttals-e2]: Parikh et al. 2020, who reads the rebuttal. [Evidence](../../../sources/notes/parikh2020rebuttals.md#e2)
[^shaw2003writing-e26]: Shaw 2003, §3.2. [Evidence](../../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e9]: Shaw 2003, §4.1. [Evidence](../../../sources/notes/shaw2003writing.md#e9)
[^ralph2020empirical-e85]: SIGSOFT Engineering Research standard, Essential Attributes (methods). [Evidence](../../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e87]: SIGSOFT Engineering Research standard, Desirable Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e87)
[^ralph2020empirical-e143]: SIGSOFT Benchmarking standard, Definition. [Evidence](../../../sources/notes/ralph2020empirical.md#e143)
[^ralph2020empirical-e149]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e149)
[^ralph2020empirical-e100]: SIGSOFT Benchmarking standard, Essential Attributes (discussion). [Evidence](../../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e203]: SIGSOFT Data Science standard, Antipatterns. [Evidence](../../../sources/notes/ralph2020empirical.md#e203)
[^ralph2020empirical-e234]: SIGSOFT Questionnaire Surveys standard, Variations. [Evidence](../../../sources/notes/ralph2020empirical.md#e234)
[^ralph2020empirical-e112]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e112)
[^ralph2020empirical-e111]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e111)
[^ralph2020empirical-e1]: SIGSOFT Systematic Reviews standard, Definition. [Evidence](../../../sources/notes/ralph2020empirical.md#e1)
[^ralph2020empirical-e291]: SIGSOFT Case Survey standard, Definition. [Evidence](../../../sources/notes/ralph2020empirical.md#e291)
[^ralph2020empirical-e4]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e4)
[^ralph2020empirical-e6]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../../sources/notes/ralph2020empirical.md#e6)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019, §3.2, p. 3. [Evidence](../../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../../sources/notes/lipton2019troubling.md#e8)
[^klees2018evaluating-e10]: Klees et al. 2018, §1. [Evidence](../../../sources/notes/klees2018evaluating.md#e10)
[^easterbrook2008selecting-e57]: Easterbrook et al. 2008, §2.0. [Evidence](../../../sources/notes/easterbrook2008selecting.md#e57)
[^kalliamvakou2014promises-e1]: Kalliamvakou et al. 2014, Abstract. [Evidence](../../../sources/notes/kalliamvakou2014promises.md#e1)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../../sources/notes/sainz2023nlp.md#e2)
[^klein2009sel4-e8]: Klein et al. 2009, Abstract. [Evidence](../../../sources/notes/klein2009sel4.md#e8)
[^blackburn2018sigplan-e31]: SIGPLAN Empirical Evaluation Checklist, FAQ (relation to artifact evaluation). [Evidence](../../../sources/notes/blackburn2018sigplan.md#e31)
[^mcdonald2019reliability-e2]: McDonald et al. 2019, Abstract. [Evidence](../../../sources/notes/mcdonald2019reliability.md#e2)
