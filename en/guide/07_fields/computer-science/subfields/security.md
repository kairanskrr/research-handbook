# Security

> This page covers only what is specific to this area. For general practice, see the chapters of Parts 1 and 2 and the research strategies. For the conventions shared across computer science (the conference cycle, double-blind review and preprints, artifact evaluation, ethics basics), see the [computer science field overview](../README.md).

## What this area studies

Security research asks how systems, software, networks, and data get attacked, and how to protect them. Take the call for papers of IEEE S&P 2026 (the IEEE Symposium on Security and Privacy; IEEE is the Institute of Electrical and Electronics Engineers): a paper can cover the theory, design, implementation, analysis, or verification of secure systems, or it can be an empirical evaluation or a measurement study. Topics range widely, from network security and measurement to user studies on security and privacy[^ieeesp2026cfp-e13].

Some typical questions `[Our analysis]`:

- **Defenses**: Which attacks does a new defense stop, and what does it cost in performance?
- **Tools**: Is a new fuzzer (a tool that bombards a program with large numbers of automatically generated inputs to find bugs) really better than existing ones[^klees2018evaluating-e1]?
- **Attacks and measurement**: Does a new attack work? How common is a given security problem in the real world?

**Start by working out what the adversary can do.** Security research faces an adversary who will actively look for ways around your scheme `[Our analysis]`. Take defenses against adversarial examples (inputs crafted specifically to fool a machine learning model). Carlini et al. ask you first to work out which attacks could break the defense, and then to show that those attacks fail. Running off-the-shelf attacks with their default parameters is not enough, even if they are state-of-the-art attacks[^carlini2019evaluating-e1]. Applying this thinking to other kinds of defenses is our own inference `[Our analysis]`.

## Main venues and timeline

The main results in security are published at conferences `[Our analysis]`. When van der Kouwe et al. studied benchmarking flaws, they looked only at papers from the "top four" security conferences, on the grounds that these have the most impact and in practice set the field's evaluation conventions[^vanderkouwe2019sok-e27].

The table below gives the rules of four conferences **each for one particular year**, as found in the sources for this page. They are not conventions of the whole area. **The rules change every year; before you submit, go by that year's call for papers.** In the table, NDSS is the Network and Distributed System Security Symposium and CCS is the ACM Conference on Computer and Communications Security (ACM is the Association for Computing Machinery).

| Conference (year) | Full name | Submission cycle | Page limit (main text) | Chance to revise |
|---|---|---|---|---|
| USENIX Security 2026 | The security symposium run by the USENIX Association | Several submission cycles, each with early rejection and an author response period[^usenixsec2026cfp-e1] | See that year's call | No more "major revision"; at most two weeks of shepherding[^usenixsec2026cfp-e14] |
| IEEE S&P 2026 | See above | Two deadlines[^ieeesp2026cfp-e11] | 13 pages[^ieeesp2026cfp-e8] | No conditional acceptance; papers are reviewed as submitted at the deadline[^ieeesp2026cfp-e12] |
| NDSS 2026 | Network and Distributed System Security Symposium | Summer and fall cycles[^ndss2026cfp-e8] | 13 pages[^ndss2026cfp-e6] | "Major revision" exists; resubmit within six weeks[^ndss2026cfp-e1] |
| ACM CCS 2025 | Conference on Computer and Communications Security | Two cycles[^ccs2025cfp-e1] | 12 pages[^ccs2025cfp-e4] | "Minor revision" exists[^ccs2025cfp-e1] |

A few rules that did not fit in the table, again each for the year shown only:

- **IEEE S&P 2026**: Accepted papers come with a public meta-review that states why the paper was accepted and what concerns the committee still has[^ieeesp2026cfp-e7]. A rejected paper cannot be resubmitted until a full year has passed since the original submission date[^ieeesp2026cfp-e9].
- **NDSS 2026**: A major revision means adding new implementations, experiments, or proofs[^ndss2026cfp-e1].
- **How pages are counted**: IEEE S&P 2026 allows an extra 5 pages for references and appendices[^ieeesp2026cfp-e8]. NDSS 2026 does not count the ethics section, references, or appendices[^ndss2026cfp-e6]. CCS 2025 does not count references, appendices, or supplementary material[^ccs2025cfp-e4].

Two things stand out in the table `[Our analysis]`:

- **Even in the same year, the conferences' rules differ**, so don't just repeat what you did for your last submission.
- **Reviewers may not read your appendices.** IEEE S&P 2026 and CCS 2025 both state that reviewers are not required to read appendices[^ieeesp2026cfp-e8][^ccs2025cfp-e4]. Put the key experiments and arguments in the main text.

**Systematization of Knowledge (SoK) papers** are a dedicated paper type at security conferences. IEEE S&P 2026 solicits them: an SoK paper evaluates, systematizes, and contextualizes existing knowledge. A plain survey without such insight may be rejected without full review. SoK papers are accepted for how they treat existing work and for their value to the community, not for presenting new research results[^ieeesp2026cfp-e1]. NDSS 2026 also accepts SoK papers and asks that they go beyond summarizing: they should analyze existing approaches in depth and identify gaps and limitations[^ndss2026cfp-e5].

**Theory papers** (such as cryptographic proofs) face one extra requirement at both IEEE S&P 2026 and CCS 2025: they must make a convincing case for how the results relate to practice[^ieeesp2026cfp-e2][^ccs2025cfp-e2]. For the theory area's own conventions, see [Theory](theory.md).

## Common strategies and standards of evidence

The grouping and summaries in this table are our own. Each standard speaks only for the paper or conference in its footnote `[Our analysis]`.

| Strategy | What it looks like here | Evidence and how it is judged | How to do it |
|---|---|---|---|
| [Building and improving](../../../05_research-strategies/build_improve.md) | New defenses, new detection systems | Compare against the current state of the art, with a fair configuration for the competitors[^vanderkouwe2019sok-e4]; besides runtime, measure memory, I/O, and binary size[^vanderkouwe2019sok-e6]; systems that make decisions must have their accuracy measured[^vanderkouwe2019sok-e7] | [Engineering research](../practices/engineering_research.md), [Systems](systems.md) |
| [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md) | Comparing tools, for example fuzzers | Multiple runs plus statistical tests[^klees2018evaluating-e10]; count real bugs, not "unique crashes"[^klees2018evaluating-e4] | [Benchmarking](../practices/benchmarking.md) |
| Building and improving (machine learning for security) | Malware detection, intrusion detection | No peeking at the test set, no ignoring time order[^arp2022dos-e4]; check for spurious correlations[^arp2022dos-e12]; mind the base rate when classes are highly imbalanced[^arp2022dos-e8] | [Machine learning](machine_learning.md) |
| [Description](../../../05_research-strategies/observe_describe.md) | Network security measurement, user studies[^ieeesp2026cfp-e13] | If you use data from people (even anonymized), IEEE S&P 2026 requires you to describe your ethics review[^ieeesp2026cfp-e6] | [Questionnaire surveys](../../../06_methods/questionnaire_survey.md), [Controlled experiments](../../../06_methods/controlled_experiment.md) |
| [Synthesis](../../../05_research-strategies/synthesize.md) | SoK papers | Must offer insight, not just a list[^ieeesp2026cfp-e1][^ndss2026cfp-e5] | [Review studies](../../../06_methods/review_study.md) |
| [Proof](../../../05_research-strategies/prove.md) | Security proofs for cryptography and protocols | Explain how the result relates to practice[^ieeesp2026cfp-e2] | [Theoretical research](../practices/theoretical_research.md), [Theory](theory.md) |

A few rows in more detail `[Our analysis]`:

- **Machine learning for security.** Arp et al. give an example: in a malware detection experiment, the URL "play.google.com" turned out to be one of the most important features for classifying an app as benign. The classifier had learned to tell where apps came from, not whether they were malicious[^arp2022dos-e12]. Another example: a 99% true-positive rate with a 1% false-positive rate looks very good, but if benign samples outnumber malicious ones 100 to 1, every 99 true positives come with 100 false positives[^arp2022dos-e8].
- **The classification in an SoK paper has to be reliable.** For example, van der Kouwe et al. had two people judge each paper independently and discussed any disagreements[^vanderkouwe2019sok-e28].
- **Many security papers are mixed**, for example showing a new attack and then proposing a defense. Choose the main strategy from your central claim, and hold each other part to the standards of its own strategy.

## Conventions specific to this area

**An ethics discussion is close to mandatory, but each conference wants it written differently.** For the general practice (think about it as early as possible, the four principles of the Menlo Report, ethics approval does not mean there is no problem), see [Research integrity and ethics](../../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) and the [computer science field overview](../README.md#ethics-issues-specific-to-this-field). Below are only the specific rules of each conference for one year:

| Conference (year) | How to write about ethics | What happens if it falls short |
|---|---|---|
| USENIX Security 2026 | Every paper must discuss research ethics[^usenixsec2026cfp-e2] | See that year's call |
| IEEE S&P 2026 | A separate "Ethics considerations" section at the end; if there are no ethical issues, the section still has to say "None"[^ieeesp2026cfp-e3] | The Research Ethics Committee can recommend rejection on ethical grounds[^ieeesp2026cfp-e4] |
| NDSS 2026 | The "Ethics Considerations" section is optional[^ndss2026cfp-e4]; you must anticipate the consequences of both doing and publishing the research[^ndss2026cfp-e2] | A paper that handles ethics poorly may be rejected however strong its scientific contribution[^ndss2026cfp-e2] |
| CCS 2025 | Convince the reviewers that you followed appropriate procedures (such as ethics review and responsible disclosure) and did your best to minimize harm[^ccs2025cfp-e3] | See that year's call |

Also, NDSS 2026 states that an exemption from an ethics review board does not necessarily show that the ethical issues have been handled[^ndss2026cfp-e3].

If you submit to an ACM conference such as CCS, you must also follow the Policy on Research Involving Human Participants and Subjects, approved by the ACM Publications Board in 2021[^acm2021humanparticipants-e1]. It applies to all ACM publications, including conferences that ACM sponsors or co-sponsors[^acm2021humanparticipants-e3]. Depending on how serious the violation is, a paper found in breach may receive a Note of Concern or be retracted[^acm2021humanparticipants-e6]. For the specific requirements (such as ethics review and written certification), see [Human-computer interaction: research with people, and ethics](hci.md#research-with-people-and-ethics).

**Vulnerability disclosure has concrete deadlines and reporting rules.** For the general principle (tell the responsible party privately first, publish after it is fixed), see [Research integrity and ethics](../../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first). What each conference asks:

- **USENIX Security 2026**: The paper states whom you disclosed to and what came of it[^usenixsec2026cfp-e6]. Submissions are anonymous, but you may still disclose vulnerabilities to vendors or the public during review[^usenixsec2026cfp-e3].
- **IEEE S&P 2026**: The submission must discuss in detail how the vulnerabilities have been or will be handled, and disclosure must be done by the rebuttal deadline at the latest[^ieeesp2026cfp-e5]. Do not include full CVE identifiers (Common Vulnerabilities and Exposures, the standard public IDs for vulnerabilities) in the submitted version, because they could reveal who the authors are[^ieeesp2026cfp-e14].
- **NDSS 2026**: Papers that report high-impact vulnerabilities must report, or at least discuss, their disclosure plan[^ndss2026cfp-e3].

**Prepare your artifacts early, and keep them anonymous.**

- Some conferences want artifacts at review time and ask you to explain if you can't provide them: USENIX Security 2026[^usenixsec2026cfp-e12], CCS 2025[^ccs2025cfp-e5]. NDSS 2026 strongly encourages accepted papers to go through artifact evaluation[^ndss2026cfp-e7].
- IEEE S&P 2026 requires the artifact repository to be anonymous at submission: no author information in the repository or in the artifact itself[^ieeesp2026cfp-e15]. For theory papers, it strongly recommends submitting the proofs as artifacts at submission time[^ieeesp2026cfp-e10].
- Artifacts that do something malicious or destructive (for example malware samples or attack scripts) must be clearly labeled; see the [computer science field overview](../README.md#ethics-issues-specific-to-this-field).

**Report performance numbers the way systems research does.** Defenses and security tools usually have to report their performance overhead. Van der Kouwe et al. surveyed 50 defense papers from top conferences and found on average 5 benchmarking flaws per paper; only one paper had none[^vanderkouwe2019sok-e26]. For how to avoid them, see [Systems](systems.md#conventions-specific-to-this-area) and [Benchmarking](../practices/benchmarking.md#2-how-to-do-it).

**Write for the general security researcher.** CCS 2025 encourages authors to write the abstract and introduction so that a general security researcher can follow them[^ccs2025cfp-e2]. Reviewers weigh importance to real-world security and privacy problems, novelty, quality of execution, and presentation[^ccs2025cfp-e3].

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Running a few off-the-shelf attacks with default parameters and declaring the defense effective | Work on adversarial examples requires showing that attacks aimed at this specific defense also fail[^carlini2019evaluating-e1] |
| Comparing a defense only with your own earlier version | Compare with the current state of the art[^vanderkouwe2019sok-e4] |
| Reporting only runtime overhead | Memory, I/O, and binary size need measuring too[^vanderkouwe2019sok-e6] |
| Running a fuzzer only once and counting "crashes" | The conclusion can flip[^klees2018evaluating-e11], and the metric overcounts bugs[^klees2018evaluating-e4] |
| Tuning parameters or setting thresholds on the test set | It produces overly optimistic results[^arp2022dos-e7] |
| Submitting an ordinary survey as an SoK | IEEE S&P 2026 states that a survey without insight may be rejected outright[^ieeesp2026cfp-e1] |
| Putting key experiments in the appendix | At IEEE S&P 2026 and CCS 2025, reviewers are not required to read appendices[^ieeesp2026cfp-e8][^ccs2025cfp-e4] |
| Including full CVE identifiers in the submitted version | IEEE S&P 2026 considers this a way of revealing the authors[^ieeesp2026cfp-e14] |
| Reusing last year's rules, or another conference's | Major revisions, ethics sections, and artifact requirements can differ by conference and by year; see the tables above `[Our analysis]` |

## Further reading

- **The call for papers and ethics guidelines of the conference you are targeting, for that year**, for example USENIX Security, IEEE S&P, NDSS, or CCS. Reread them before every submission.
- **van der Kouwe et al. 2019, SoK: Benchmarking Flaws in Systems Security**: lists 22 benchmarking flaws. If you work on defenses or systems security, go through them one by one before you submit.
- **Klees et al. 2018, Evaluating Fuzz Testing**: read it when you evaluate a fuzzer or any tool with randomness in it.
- **Arp et al. 2022, Dos and Don'ts of Machine Learning in Computer Security**: common pitfalls when you use machine learning for security.
- **Carlini et al. 2019, On Evaluating Adversarial Robustness**: a guide to evaluating defenses against adversarial examples.
- Related areas: [Systems](systems.md) (conventions for performance evaluation), [Machine learning](machine_learning.md), [Theory](theory.md).

[^ieeesp2026cfp-e13]: IEEE S&P 2026 call for papers, opening and Topics of interest. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e13)
[^klees2018evaluating-e1]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e1)
[^carlini2019evaluating-e1]: Carlini et al. 2019, §2.5. [Evidence](../../../../sources/notes/carlini2019evaluating.md#e1)
[^vanderkouwe2019sok-e27]: van der Kouwe et al. 2019, §I, §III-B. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e27)
[^usenixsec2026cfp-e1]: USENIX Security '26 call for papers, Important Dates. [Evidence](../../../../sources/notes/usenixsec2026cfp.md#e1)
[^usenixsec2026cfp-e14]: USENIX Security '26 call for papers, Summary of main changes. [Evidence](../../../../sources/notes/usenixsec2026cfp.md#e14)
[^ieeesp2026cfp-e11]: IEEE S&P 2026 call for papers, Important Dates. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e11)
[^ieeesp2026cfp-e8]: IEEE S&P 2026 call for papers, Page Limit and Formatting. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e8)
[^ieeesp2026cfp-e12]: IEEE S&P 2026 call for papers, Public Meta-Reviews. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e12)
[^ndss2026cfp-e8]: NDSS 2026 call for papers, Paper Submission Information. [Evidence](../../../../sources/notes/ndss2026cfp.md#e8)
[^ndss2026cfp-e6]: NDSS 2026 call for papers, Paper Formatting. [Evidence](../../../../sources/notes/ndss2026cfp.md#e6)
[^ndss2026cfp-e1]: NDSS 2026 call for papers, Paper Submission Information. [Evidence](../../../../sources/notes/ndss2026cfp.md#e1)
[^ccs2025cfp-e1]: ACM CCS 2025 call for papers, opening. [Evidence](../../../../sources/notes/ccs2025cfp.md#e1)
[^ccs2025cfp-e4]: ACM CCS 2025 call for papers, formatting requirements. [Evidence](../../../../sources/notes/ccs2025cfp.md#e4)
[^ieeesp2026cfp-e7]: IEEE S&P 2026 call for papers, Public Meta-Reviews. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e7)
[^ieeesp2026cfp-e9]: IEEE S&P 2026 call for papers, Submission Deadlines & Decisions. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e9)
[^ieeesp2026cfp-e1]: IEEE S&P 2026 call for papers, Systematization of Knowledge Papers. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e1)
[^ndss2026cfp-e5]: NDSS 2026 call for papers, Areas/Topics of Interest. [Evidence](../../../../sources/notes/ndss2026cfp.md#e5)
[^ieeesp2026cfp-e2]: IEEE S&P 2026 call for papers, opening. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e2)
[^ccs2025cfp-e2]: ACM CCS 2025 call for papers, opening. [Evidence](../../../../sources/notes/ccs2025cfp.md#e2)
[^vanderkouwe2019sok-e4]: van der Kouwe et al. 2019, §II-D. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e6]: van der Kouwe et al. 2019, Appendix E2. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e6)
[^vanderkouwe2019sok-e7]: van der Kouwe et al. 2019, §II-E. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e7)
[^klees2018evaluating-e10]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e10)
[^klees2018evaluating-e4]: Klees et al. 2018, §9. [Evidence](../../../../sources/notes/klees2018evaluating.md#e4)
[^arp2022dos-e4]: Arp et al. 2022, §2, P3. [Evidence](../../../../sources/notes/arp2022dos.md#e4)
[^arp2022dos-e12]: Arp et al. 2022, §4.1. [Evidence](../../../../sources/notes/arp2022dos.md#e12)
[^arp2022dos-e8]: Arp et al. 2022, §2, P8. [Evidence](../../../../sources/notes/arp2022dos.md#e8)
[^ieeesp2026cfp-e6]: IEEE S&P 2026 call for papers, Ethical Considerations for Human Subjects Research. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e6)
[^vanderkouwe2019sok-e28]: van der Kouwe et al. 2019, §III-A. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e28)
[^usenixsec2026cfp-e2]: USENIX Security '26 call for papers, Executive Summary. [Evidence](../../../../sources/notes/usenixsec2026cfp.md#e2)
[^ieeesp2026cfp-e3]: IEEE S&P 2026 call for papers, Ethics Considerations. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e3)
[^ieeesp2026cfp-e4]: IEEE S&P 2026 call for papers, Research Ethics Committee. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e4)
[^ndss2026cfp-e4]: NDSS 2026 call for papers, Ethical Considerations. [Evidence](../../../../sources/notes/ndss2026cfp.md#e4)
[^ndss2026cfp-e2]: NDSS 2026 call for papers, Ethical Considerations. [Evidence](../../../../sources/notes/ndss2026cfp.md#e2)
[^ccs2025cfp-e3]: ACM CCS 2025 call for papers, review criteria. [Evidence](../../../../sources/notes/ccs2025cfp.md#e3)
[^ndss2026cfp-e3]: NDSS 2026 call for papers, Ethical Considerations. [Evidence](../../../../sources/notes/ndss2026cfp.md#e3)
[^acm2021humanparticipants-e1]: ACM 2021 Policy on Research Involving Human Participants, below the title. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e1)
[^acm2021humanparticipants-e3]: ACM 2021 Policy on Research Involving Human Participants, Scope of Policy. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e3)
[^acm2021humanparticipants-e6]: ACM 2021 Policy on Research Involving Human Participants, Violations and Penalties. [Evidence](../../../../sources/notes/acm2021humanparticipants.md#e6)
[^usenixsec2026cfp-e6]: USENIX Security '26 ethics guidelines, Disclosures. [Evidence](../../../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e3]: USENIX Security '26 call for papers, Anonymous Submission. [Evidence](../../../../sources/notes/usenixsec2026cfp.md#e3)
[^ieeesp2026cfp-e5]: IEEE S&P 2026 call for papers, Ethical Considerations for Vulnerability Disclosure. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e5)
[^ieeesp2026cfp-e14]: IEEE S&P 2026 call for papers, Ethical Considerations for Vulnerability Disclosure. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e14)
[^usenixsec2026cfp-e12]: USENIX Security '26 call for papers, Executive Summary. [Evidence](../../../../sources/notes/usenixsec2026cfp.md#e12)
[^ccs2025cfp-e5]: ACM CCS 2025 call for papers, Providing Artifacts at Submission Time. [Evidence](../../../../sources/notes/ccs2025cfp.md#e5)
[^ndss2026cfp-e7]: NDSS 2026 call for papers, Artifact Evaluation. [Evidence](../../../../sources/notes/ndss2026cfp.md#e7)
[^ieeesp2026cfp-e15]: IEEE S&P 2026 call for papers, Anonymous Submission. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e15)
[^ieeesp2026cfp-e10]: IEEE S&P 2026 call for papers, Artifacts. [Evidence](../../../../sources/notes/ieeesp2026cfp.md#e10)
[^vanderkouwe2019sok-e26]: van der Kouwe et al. 2019, Abstract. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e26)
[^klees2018evaluating-e11]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e11)
[^arp2022dos-e7]: Arp et al. 2022, §2, P5. [Evidence](../../../../sources/notes/arp2022dos.md#e7)
