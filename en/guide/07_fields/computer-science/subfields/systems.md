# Systems

> This page covers only what is specific to this area. For general practice, see the chapters of Parts 1 and 2 and the research strategies. For the conventions shared across computer science (the conference cycle, double-blind review and preprints, artifact evaluation and badges), see the [computer science field overview](../README.md).

## What this area studies

Systems research studies how computer systems software is designed, built, and run. Take the call for papers of SOSP 2025 (the ACM Symposium on Operating Systems Principles; ACM is the Association for Computing Machinery): its scope includes operating systems, file and storage systems, distributed systems, cloud computing, mobile and edge systems, secure and reliable systems, and systems issues in big data and machine learning[^sosp2025cfp-e9].

Some typical questions `[Our analysis]`:

- How much does a new storage or scheduling design improve latency, throughput, or resource overhead, and what does it cost?
- What problems did a system deployed at large scale run into in operation, and what lessons came out of it?
- Can a system be proved correct? For example, the seL4 team carried out a machine-checked verification of an operating system kernel, from the abstract specification down to the C implementation[^klein2009sel4-e8]; the paper appeared at SOSP 2009.

**"Build something, then show with experiments that it is good" is the usual shape.** The call for papers of OSDI 2026 (the USENIX Symposium on Operating Systems Design and Implementation) puts it plainly: a good paper poses an important problem, presents a convincing solution, and demonstrates that the solution is practical and beneficial[^osdi2026cfp-e2]. SOSP 2025 also requires the solution to be **implemented**, and the paper to be accessible to the broader systems community[^sosp2025cfp-e2].

## Main venues and timeline

The main results in systems are published at conferences; OSDI and SOSP are the two examples in the sources for this page `[Our analysis]`. The table gives their rules **each for one particular year**. They are not conventions of the whole area. **The rules change every year; before you submit, go by that year's call for papers.**

| | OSDI 2026 | SOSP 2025 |
|---|---|---|
| What it values | Innovative research, plus quantified or insightful experience with design and implementation[^osdi2026cfp-e1] | Work that opens new areas, continues an important research conversation, or reflects on experience with and measurements of state-of-the-art implementations[^sosp2025cfp-e1] |
| Length | At most 12 pages; padded papers get marked down, and papers of 6 pages or less are unlikely to get full consideration[^osdi2026cfp-e3] | At most 12 pages of technical content, references not counted[^sosp2025cfp-e5] |
| Review tracks | A Research track and an Operational Systems track[^osdi2026cfp-e4] | Our sources do not cover this |
| Author response | Dropped[^osdi2026cfp-e5] | Yes, but no new experiments or data[^sosp2025cfp-e4] |
| How papers are accepted | Conditional acceptance, which replaces revise-and-resubmit[^osdi2026cfp-e5] | Conditional acceptance first; final acceptance once the shepherd approves the changes[^sosp2025cfp-e7] |
| Anonymizing the system name | Use an anonymized name[^osdi2026cfp-e6] | If the name has already been made public, you must change it[^sosp2025cfp-e8] |

Some cells in more detail, again each for the year shown only:

- **Conditional acceptance at OSDI 2026**: If the authors do not make the changes the committee requires, the paper is still rejected[^osdi2026cfp-e8].
- **The Operational Systems track at OSDI 2026**: papers on the design, implementation, analysis, and experience of deployed systems[^osdi2026cfp-e4].
- **Author response at SOSP 2025**: You may only correct factual errors in the reviews or directly answer reviewers' questions. You may not describe work done after submission or promise future work[^sosp2025cfp-e4].
- **Preprints at OSDI 2026**: You may make the work public first through technical reports, talks, social media, and so on, but the project or system name in the submission must differ from the one used in public[^osdi2026cfp-e6].

A few things to watch `[Our analysis]`:

- **The system's name must be anonymized too.** Systems papers usually refer to the work by the system's name. If you have posted a preprint or given a talk, rename the system for the submission. SOSP 2025 adds that when you report experience with a system at your own organization, you anonymize the system's name but describe the characteristics readers need to understand the work, such as number of users or request volume[^sosp2025cfp-e6].
- **Nobody is guaranteed to read your supplementary material.** OSDI 2026 states that reviewers are not required to read supplementary material and that the paper must be self-contained[^osdi2026cfp-e7].
- **New directions are judged differently from established ones.** SOSP 2025 encourages work that opens new directions and acknowledges that papers on new problems may be judged by different criteria from papers that continue mature lines of work[^sosp2025cfp-e3].

**Artifact evaluation is widespread in systems.** For participation rates, timing, and what the badges mean, see [Computer science field overview: artifact evaluation and badges](../README.md#artifact-evaluation-and-badges). SOSP 2025 also encourages accepted papers to provide source code and raw data through artifact evaluation[^sosp2025cfp-e7]. Taking OSDI 2024 as an example, the time between acceptance and artifact submission is short, and the conference recommends starting to prepare while the paper is still under review[^sysartifactsguide-e2]. For how to package an artifact, see item 3 of the overview's [advice for newcomers](../README.md#advice-for-newcomers).

## Common strategies and standards of evidence

The grouping and summaries in this table are our own. Each standard speaks only for the paper or conference in its footnote `[Our analysis]`.

| Strategy | What it looks like here | Evidence and how it is judged | How to do it |
|---|---|---|---|
| [Building and improving](../../../05_research-strategies/build_improve.md) | New operating systems, storage, distributed, or cloud systems | Clearly better where you care, and not noticeably worse elsewhere[^heiserbenchmarking-e3]; compare with the state of the art[^heiserbenchmarking-e16] | [Engineering research](../practices/engineering_research.md) |
| [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md) | Measuring performance with benchmark suites and real workloads | No cherry-picked subsets[^heiserbenchmarking-e4]; use macro-benchmarks that represent real workloads[^heiserbenchmarking-e7]; configure competitors with the same care[^heiserbenchmarking-e15] | [Benchmarking](../practices/benchmarking.md) |
| [Measurement](../../../05_research-strategies/measure.md) | Whether the measurements themselves can be trusted | An improvement may fall within measurement error[^kalibera2013rigorous-e2]; the size of the Unix environment and the link order can introduce bias[^kalibera2013rigorous-e3] | [Benchmarking: designing the measurement procedure](../practices/benchmarking.md#step-4-design-the-measurement-procedure) |
| [Description](../../../05_research-strategies/observe_describe.md) | Experience reports and measurements of deployed systems | OSDI 2026 welcomes work that disproves or strengthens existing assumptions, or validates known techniques at new scales or in new environments[^osdi2026cfp-e4] | [Case studies](../../../06_methods/case_study.md) |
| [Proof](../../../05_research-strategies/prove.md) | Formal verification of systems | State the assumptions the proof depends on[^klein2009sel4-e1]; the proof cannot tell you whether the specification itself is right[^klein2009sel4-e2] | [Proof: what evidence is enough](../../../05_research-strategies/prove.md#2-what-evidence-is-enough) |

How to use this table `[Our analysis]`: many systems papers are mainly building and improving, with the evaluation section written to the standards of comparative evaluation and measurement. If there is formal verification, add the requirements of proof.

## Conventions specific to this area

**Performance evaluation has a list of "crimes".** Drawing on his reviewing experience, Heiser compiled the evaluation mistakes common in systems papers and calls them "crimes" because they undermine the integrity of the scientific process[^heiserbenchmarking-e1]. The full steps and examples are in [Benchmarking](../practices/benchmarking.md#2-how-to-do-it); here are only the ones systems papers get questioned on most:

- **Don't benchmark selectively.** Using a biased set of benchmarks to "prove" a point is the mother of all benchmarking crimes[^heiserbenchmarking-e2]. If you run only part of a suite, every missing program needs a convincing reason, and if you used a subset you cannot report an overall figure for the whole suite[^heiserbenchmarking-e4].
- **Measure the cost too.** A fair evaluation shows two things: performance clearly improves where you care, and it does not noticeably degrade elsewhere[^heiserbenchmarking-e3].
- **Pick the right baseline.** The baseline is often the state of the art, but it can also be the theoretical optimum or the hardware limit[^heiserbenchmarking-e13]. Once a new state of the art appears, it becomes the baseline you must use[^heiserbenchmarking-e16].
- **A drop in throughput is not the overhead.** When you compare throughput, you must also compare total processor load[^heiserbenchmarking-e8].
- **Report variation and absolute numbers.** At least report standard deviations[^heiserbenchmarking-e10]; give full results, not just ratios[^heiserbenchmarking-e19].
- **Describe the evaluation platform completely.** Describe every platform feature that could affect the results; compiler and other tool versions often matter too[^heiserbenchmarking-e17].

**Running more times is not the same as repeating correctly.** System performance depends on many factors you may not notice `[Our analysis]`. Kalibera and Jones advise:

- Factors outside your control that happen to stay fixed throughout the experiment introduce bias. First make them controlled or randomized, for example by randomizing the link order[^kalibera2013rigorous-e5].
- Repeat at least at the highest level where random variation occurs, for example recompiling and restarting the program, not just looping more iterations within one run[^kalibera2013rigorous-e6].
- Report a performance change as a confidence interval for the effect size, which tells the reader how big the change is, how big the error is, and how certain you are[^kalibera2013rigorous-e8].

**Parallel and high-performance computing has its own list of rules.** Hoefler and Belli give a set of rules for reporting performance of parallel computing systems, for example never report ratios without the absolute values[^hoefler2015scientific-e2], and give performance upper bounds where possible[^hoefler2015scientific-e14]. They and Heiser disagree on how to summarize scores from several benchmarks into one number[^heiserbenchmarking-e11][^hoefler2015scientific-e4]; both approaches are covered in [Benchmarking](../practices/benchmarking.md#step-5-analyze-the-results).

**These conventions also apply to systems security.** Defense papers in security usually have to report performance overhead; for a survey of their benchmarking flaws, see [Security](security.md).

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Measuring only the scenarios that favor you | You must also show nothing gets noticeably worse elsewhere; otherwise it is deceptive[^heiserbenchmarking-e3] |
| Comparing only with your own system from last year | Compare with accepted standards[^heiserbenchmarking-e14] |
| Tuning your own system to the hilt while running competitors on default settings | Put the same effort into the competitors; if unsure, contact their authors[^heiserbenchmarking-e15] |
| Using micro-benchmark results to claim overall performance | Use macro-benchmarks that represent real workloads[^heiserbenchmarking-e7] |
| Giving only speedups, not absolute performance | Breaks the "don't report only ratios" rule[^hoefler2015scientific-e2][^heiserbenchmarking-e19] |
| Not reporting variation when the improvement is only a few percent | The improvement may fall within measurement error[^kalibera2013rigorous-e2] |
| Measuring under a single compile-and-link setup | The size of the Unix environment and the link order can both bias results toward one system[^kalibera2013rigorous-e3] |
| Keeping an already public system name in the submission | OSDI 2026 and SOSP 2025 both require a different name[^osdi2026cfp-e6][^sosp2025cfp-e8] |
| Putting key experiments in the supplementary material | At OSDI 2026, reviewers are not required to read supplementary material[^osdi2026cfp-e7] |
| Adding new experiments in the SOSP author response | SOSP 2025 explicitly forbids it[^sosp2025cfp-e4] |
| Starting to prepare the artifact only after acceptance | The time between acceptance and artifact submission is short[^sysartifactsguide-e2] |

## Further reading

- **The call for papers and call for artifacts of the conference you are targeting, for that year**, for example OSDI or SOSP. Reread them before every submission.
- **Heiser, Systems Benchmarking Crimes** (web page): a list of common evaluation mistakes in systems papers. Check your evaluation section against it item by item before you write it up.
- **Hoefler and Belli 2015, Scientific Benchmarking of Parallel Computing Systems**: a set of rules for reporting performance; essential if you work on parallel or high-performance computing.
- **Kalibera and Jones 2013, Rigorous Benchmarking in Reasonable Time**: how to plan repeated experiments and how to report performance changes with confidence intervals.
- **Klein et al. 2009, seL4: Formal Verification of an OS Kernel**: read it to see what formal verification of a system costs and what it buys.
- Related areas: [Security](security.md), [Programming languages](programming_languages.md), [Theory](theory.md).

[^sosp2025cfp-e9]: SOSP 2025 call for papers, opening. [Evidence](../../../../sources/notes/sosp2025cfp.md#e9)
[^klein2009sel4-e8]: Klein et al. 2009, Abstract. [Evidence](../../../../sources/notes/klein2009sel4.md#e8)
[^osdi2026cfp-e2]: OSDI '26 Call for Papers, Submitting a Paper. [Evidence](../../../../sources/notes/osdi2026cfp.md#e2)
[^sosp2025cfp-e2]: SOSP 2025 call for papers, Submission Criteria. [Evidence](../../../../sources/notes/sosp2025cfp.md#e2)
[^osdi2026cfp-e1]: OSDI '26 Call for Papers, opening section. [Evidence](../../../../sources/notes/osdi2026cfp.md#e1)
[^sosp2025cfp-e1]: SOSP 2025 call for papers, opening. [Evidence](../../../../sources/notes/sosp2025cfp.md#e1)
[^osdi2026cfp-e3]: OSDI '26 Call for Papers, Deadline and Submission Instructions. [Evidence](../../../../sources/notes/osdi2026cfp.md#e3)
[^sosp2025cfp-e5]: SOSP 2025 call for papers, Formatting requirements. [Evidence](../../../../sources/notes/sosp2025cfp.md#e5)
[^osdi2026cfp-e4]: OSDI '26 Call for Papers, Submission Tracks. [Evidence](../../../../sources/notes/osdi2026cfp.md#e4)
[^osdi2026cfp-e5]: OSDI '26 Call for Papers, opening section (main changes this year). [Evidence](../../../../sources/notes/osdi2026cfp.md#e5)
[^sosp2025cfp-e4]: SOSP 2025 call for papers, Author Response Period. [Evidence](../../../../sources/notes/sosp2025cfp.md#e4)
[^sosp2025cfp-e7]: SOSP 2025 call for papers, Acceptance. [Evidence](../../../../sources/notes/sosp2025cfp.md#e7)
[^osdi2026cfp-e6]: OSDI '26 Call for Papers, Submitting a Paper. [Evidence](../../../../sources/notes/osdi2026cfp.md#e6)
[^sosp2025cfp-e8]: SOSP 2025 call for papers, Anonymity. [Evidence](../../../../sources/notes/sosp2025cfp.md#e8)
[^osdi2026cfp-e8]: OSDI '26 Call for Papers, conditional acceptance. [Evidence](../../../../sources/notes/osdi2026cfp.md#e8)
[^sosp2025cfp-e6]: SOSP 2025 call for papers, Anonymity. [Evidence](../../../../sources/notes/sosp2025cfp.md#e6)
[^osdi2026cfp-e7]: OSDI '26 Call for Papers, supplementary material. [Evidence](../../../../sources/notes/osdi2026cfp.md#e7)
[^sosp2025cfp-e3]: SOSP 2025 call for papers, Submission Criteria. [Evidence](../../../../sources/notes/sosp2025cfp.md#e3)
[^sysartifactsguide-e2]: sysartifacts, OSDI '24 Call for Artifacts, Overview. [Evidence](../../../../sources/notes/sysartifactsguide.md#e2)
[^heiserbenchmarking-e3]: Heiser, Not evaluating potential performance degradation. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e3)
[^heiserbenchmarking-e16]: Heiser, Inflating gains by not comparing against the state of the art. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e16)
[^heiserbenchmarking-e4]: Heiser, Benchmark sub-setting without strong justification. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e4)
[^heiserbenchmarking-e7]: Heiser, Pretending micro-benchmarks represent overall performance. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e7)
[^heiserbenchmarking-e15]: Heiser, Unfair benchmarking of competitors. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e15)
[^kalibera2013rigorous-e2]: Kalibera & Jones 2013, §1. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e2)
[^kalibera2013rigorous-e3]: Kalibera & Jones 2013, §2. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e3)
[^klein2009sel4-e1]: Klein et al. 2009, §1. [Evidence](../../../../sources/notes/klein2009sel4.md#e1)
[^klein2009sel4-e2]: Klein et al. 2009, §4.5. [Evidence](../../../../sources/notes/klein2009sel4.md#e2)
[^heiserbenchmarking-e1]: Heiser, Benchmarking Crimes, opening. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e1)
[^heiserbenchmarking-e2]: Heiser, Selective benchmarking. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e2)
[^heiserbenchmarking-e13]: Heiser, No proper baseline. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e13)
[^heiserbenchmarking-e8]: Heiser, Throughput degraded by x% ⇒ overhead is x%. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e8)
[^heiserbenchmarking-e10]: Heiser, No indication of significance of data. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e10)
[^heiserbenchmarking-e19]: Heiser, Relative numbers only. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e19)
[^heiserbenchmarking-e17]: Heiser, Missing specification of evaluation platform. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e17)
[^kalibera2013rigorous-e5]: Kalibera & Jones 2013, §3. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e5)
[^kalibera2013rigorous-e6]: Kalibera & Jones 2013, §3. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e6)
[^kalibera2013rigorous-e8]: Kalibera & Jones 2013, §4. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e8)
[^hoefler2015scientific-e2]: Hoefler & Belli 2015, §2, Rule 1. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e2)
[^hoefler2015scientific-e14]: Hoefler & Belli 2015, §5.1, Rule 11. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e14)
[^heiserbenchmarking-e11]: Heiser, Arithmetic mean for averaging across benchmark scores. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e11)
[^hoefler2015scientific-e4]: Hoefler & Belli 2015, §3.1, Rules 3 and 4. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e4)
[^heiserbenchmarking-e14]: Heiser, Only evaluate against yourself. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e14)
