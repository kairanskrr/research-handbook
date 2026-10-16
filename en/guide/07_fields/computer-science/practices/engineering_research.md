# Engineering research: proposing and evaluating a new method, tool, or system

This page covers the most common kind of research in computing: **you propose a new technique, algorithm, tool, or system and show that it works**.

**Scope** `[Our analysis]`: this is how the "building and improving" research strategy is done in computer science; the examples and standards come mainly from software engineering, systems, security, and machine learning. The parts that hold in every field are covered in [Building and improving](../../../05_research-strategies/build_improve.md) and not repeated here: what knowledge this kind of research produces, what evidence reviewers want, why you should get baselines running early, and how claims map to evidence. This page covers only what is specific to computing: what the software engineering review standards actually require, how baselines and benchmarks are chosen in different subfields, the conventions for evaluating cost, and how research artifacts are released and evaluated. Other general topics: threats to validity are in [Validity and limitations](../../../02_from-project-to-study/03_validity-and-limits.md); multiple runs and random seeds are in [Comparative evaluation: is the difference real?](../../../05_research-strategies/compare_evaluate.md#is-the-difference-real), and general statistical practice is in [Analysis and interpretation: report how big and how certain, not just a p-value](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value); how to write the paper is in [Telling the story and writing the paper](../../../04_write-and-publish/01_story-and-paper.md); how to organize code and data is in [Organizing your research materials](../../../08_throughout/organizing_materials.md). If you are systematically comparing a set of existing tools or models without proposing a new method, that is [Benchmarking](benchmarking.md).

**After reading this page, you should be able to:**

- tell whether your research is engineering research, and say clearly "what is new, and what it beats";
- write your contributions as testable claims and pick the right kind of validation for each;
- choose defensible baselines and benchmarks, and design an evaluation that covers effectiveness, cost, generality, and whether each component is needed;
- write down the real threats to validity, and release your research artifacts to the standard your community expects;
- check your own paper against the checklist at the end.

---

## 1. What this kind of research is, and when to use it

What knowledge this research produces, what questions it answers, and how it differs from comparative evaluation or an experience report are covered in [Building and improving](../../../05_research-strategies/build_improve.md#1-what-kind-of-knowledge-this-research-produces). This page often cites the ACM SIGSOFT Empirical Standards (the review standards that the software engineering community, through the Association for Computing Machinery's Special Interest Group on Software Engineering, wrote for each research method; "the SIGSOFT standards" below). They call this kind of work "engineering research" and define it as research that invents and evaluates technological artifacts[^ralph2020empirical-e79]. At ICSE (the International Conference on Software Engineering), the top software engineering conference, papers reporting a new technique are the most common kind[^shaw2003writing-e26]. Most papers in systems, security, programming languages, and machine learning also fall into this category `[Our analysis]`.

Reviewers need to see at a glance which of these you did: proposed a new technique and demonstrated it, applied an earlier technique to a new example, or evaluated a mature technique. If they can't tell, the paper isn't clear enough[^shaw2003writing-e31].

> **A note on the name**: you will also see the term "design science". The authors of the SIGSOFT standards argue that information systems research misappropriated the term "design science" around 2004; they prefer "engineering research"[^ralph2020empirical-e98].

---

## 2. How to do it

### Step 1: State the problem, and "what is new, and what it beats"

The general advice (present the problem before the solution, say exactly how you improve on each of the closest pieces of work, novelty is not complexity) is in [Building and improving](../../../05_research-strategies/build_improve.md#2-what-evidence-is-enough). In engineering research you also need to make two things explicit:

1. **What type of result your contribution is.** Is it a technique (which must be an operational procedure, not advice or guidelines), or a tool that embodies a technique[^shaw2003writing-e27]?
2. **On which dimension it beats existing artifacts.** Say which work you build on, what you replace, and how you differ from it[^shaw2003writing-e34]. The SIGSOFT standards give scalability, performance on a certain class of problems, applicability to real systems, and theoretical guarantees as example dimensions[^ralph2020empirical-e95].

How reviewers judge novelty is covered in [Being a reviewer](../../../08_throughout/being_a_reviewer.md#4-judge-it-by-its-own-research-strategy).

**Where people go wrong:** overstating novelty; describing implementation details while leaving out the key idea[^ralph2020empirical-e91]. When you describe the artifact, explain the overall workflow and how the parts fit together, and **clearly mark which parts are new**[^ralph2020empirical-e83].

### Step 2: Write your contributions as testable claims

Claims must be stated clearly enough that readers can judge whether the experiments support them[^blackburn2018sigplan-e1].

**How:** `[Our analysis]` write each contribution as one testable sentence and label which dimension it belongs to. Claims in engineering research usually fall on these dimensions:

| Dimension | Example claim | Evidence needed |
|---|---|---|
| Effectiveness | "Finds 30% more bugs than X" | Comparison with baselines on the same set of evaluation subjects |
| Efficiency and cost | "Runtime overhead below 5%" | Measurements of each cost, such as time and memory |
| Generality | "Works on all kinds of web applications" | Diverse, representative evaluation subjects |
| Necessity of each component | "Component A is what drives the improvement" | Ablation study (remove the method's components one at a time and see how results change) |
| Usability | "Developers finish tasks faster" | An experiment or case study with human participants |

**Then check how strong each claim is, and aim the validation at the claim.** The two rules (the stronger the claim, the harder the evidence must be; if you claim a performance gain, analyze performance) are in [Building and improving](../../../05_research-strategies/build_improve.md#2-what-evidence-is-enough). In systems security, van der Kouwe et al. list claiming to have achieved a goal without empirically checking whether it was reached as a benchmarking flaw[^vanderkouwe2019sok-e5]. How to put claims into the introduction and abstract is covered in [Telling the story and writing the paper](../../../04_write-and-publish/01_story-and-paper.md#4-introduction-five-questions-plus-a-list-of-contributions).

### Step 3: Pick the right kind of validation for each claim

Shaw 2003 sorts the ways software engineering papers validate their results into these kinds:

| Kind | What it is | How convincing |
|---|---|---|
| Analysis | Rigorous derivation, proof, or a carefully designed experiment | Strong[^shaw2003writing-e32] |
| Experience | The result has been used on real examples by **people other than the authors**[^shaw2003writing-e33] | Strong[^shaw2003writing-e32] |
| Evaluation | Measured against criteria stated in advance; includes feasibility studies and pilot projects | Medium `[Our analysis]` |
| Example | Shows how it works on an example | Examples drawn from real systems are fairly convincing; toy examples often are not[^shaw2003writing-e28] |
| Persuasion | "I thought hard about this, and I believe..." | Rarely enough[^shaw2003writing-e10] |
| Blatant assertion | No validation at all | Almost never accepted[^shaw2003writing-e37] |

The SIGSOFT standards require you to evaluate the artifact with an empirical method and to say which one you used[^ralph2020empirical-e84]:

- action research: the researcher takes the artifact into a real organization;
- evaluation against one or more benchmarks;
- some other method, with a clear and convincing justification;
- controlled experiments with human participants, quantitative simulations, and the like are also common forms of empirical evaluation `[Our analysis]`.

You also need to analyze the artifact's strengths, weaknesses, and limitations **conceptually**[^ralph2020empirical-e81]; when there is a theoretical contribution, it is better to give an argument for correctness, such as theorems, complexity analysis, or proofs[^ralph2020empirical-e88].

When the problem itself is "can this be done at all", or the artifact is highly innovative, the expectations for the empirical part differ; these two exceptions are covered in [Building and improving](../../../05_research-strategies/build_improve.md#2-what-evidence-is-enough).

**Where people go wrong:** an evaluation that rests only on users' subjective opinions; performance numbers with no comparison to alternatives; no control and no repetition; evaluating on a toy example and calling it a "case study"[^ralph2020empirical-e92][^ralph2020empirical-e93].

### Step 4: Choose baselines

That you must compare against the best current alternatives, and the minimum kinds of baseline, are covered in [Building and improving](../../../05_research-strategies/build_improve.md#get-the-baseline-running-early); how to give competitors an equally good configuration is in [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md#was-every-competitor-treated-equally). The SIGSOFT standards also say that not comparing against a method you could not obtain or could not run is not a flaw[^ralph2020empirical-e95], but you should say so in the paper. In engineering research, also watch for:

- **Comparing only against your own earlier work doesn't count**; running competitors in a non-optimal configuration is another common flaw[^vanderkouwe2019sok-e4].
- **Get the baseline itself right.** In systems security, when you measure overhead, the right baseline is usually the unmodified system in its default configuration, with no defense added[^vanderkouwe2019sok-e14].
- **Adversaries adapt.** When you evaluate a defense against adversarial examples (or any defense facing an active attacker), ask "what attack could break this?" and show that those attacks fail; running off-the-shelf attacks with default parameters is not enough[^carlini2019evaluating-e1].

### Step 5: Choose benchmarks and evaluation subjects

A **benchmark** is an accepted set of evaluation subjects plus a way of measuring them, such as a set of programs, a dataset, or a workload. [Benchmarking](benchmarking.md) covers choosing benchmarks and taking measurements in more depth; here we list only the points that most often go wrong when you propose a new method.

1. **If you use an existing benchmark, say why you chose it** (is it relevant, is it outdated?)[^ralph2020empirical-e99]. **If you build a new benchmark**, state which quality it measures, with which metrics, under which workload[^ralph2020empirical-e104].
2. **Discuss whether the benchmark measures what you want to measure** (construct validity)[^ralph2020empirical-e100]. Be especially careful with proxy metrics. Fuzzing papers (fuzzing tests a program with large numbers of automatically generated inputs to find bugs) often use "unique crashes" in place of "real bugs", but unique crashes heavily overcount bugs, so an apparent improvement may be small or not exist at all[^klees2018evaluating-e4]. If you introduce a new metric, define it precisely and explain why it is better than existing ones[^shaw2003writing-e36].
3. **Use diverse, representative subjects; don't pick only the ones that favor you.** One published fuzzer did well on the programs its original paper chose, but on two programs used in other papers it was no better than the baseline[^klees2018evaluating-e3]. Arbitrarily picking a subset of a benchmark suite and reporting it as the overall result is a flaw[^vanderkouwe2019sok-e3].
4. **Use realistic subjects.** A microbenchmark that times one specific operation does not tell you how fast the system is in practice[^vanderkouwe2019sok-e9]; in machine learning for security, evaluating only in a lab setting without discussing practical limitations is a common pitfall[^arp2022dos-e2]. Evaluating on widely used open-source projects or with professional developers is better[^ralph2020empirical-e88].
5. **Subjects you used during development can't be reused for evaluation**[^blackburn2018sigplan-e12][^vanderkouwe2019sok-e10]. For the reasoning, see [Comparative evaluation: keep some data for the final test only](../../../05_research-strategies/compare_evaluate.md#keep-some-data-for-the-final-test-only).

**Where people go wrong:** tailoring the benchmark to your own method, or hiding weaknesses behind tests unrelated to the problem[^ralph2020empirical-e101]; once a benchmark suite has been in use for a long time, tools start to be tuned specifically for it, and those tunings bring no fundamental benefit[^klees2018evaluating-e7].

### Step 6: Design the evaluation to answer four questions

**Question 1: Does it work?** Compare against baselines on the same set of evaluation subjects (Steps 4 and 5). If the system makes decisions, you must report its accuracy; without the accuracy, nobody can judge its value[^vanderkouwe2019sok-e7] (for example, when it decides whether behavior is malicious, measure false positives and false negatives `[Our analysis]`).

**Question 2: What does it cost?** First list every performance dimension your approach could affect (CPU, concurrency, memory, disk and network I/O, and so on), and test each with at least one suitable benchmark[^vanderkouwe2019sok-e11]. Measure every operation that could reasonably be expected to be affected[^vanderkouwe2019sok-e2]. Runtime alone is not enough; also measure memory and costs such as binary size and preprocessing time[^vanderkouwe2019sok-e6]. Zeller mocks one recipe: bolt a huge apparatus (say, a machine learning model plus a corpus) onto a simple method, and you can always gain a little, so you call it "better"[^zeller2021devil-e6].

**Question 3: Does it generalize?** Working well on one dataset, or only for you, is not enough; see [Building and improving](../../../05_research-strategies/build_improve.md#2-what-evidence-is-enough). In computing you usually answer this with several benchmarks and several kinds of evaluation subjects (Step 5) `[Our analysis]`.

**Question 4: Is every component necessary?** Answer with an ablation study; see [Building and improving](../../../05_research-strategies/build_improve.md#2-what-evidence-is-enough). One case to watch for in engineering research: if you are faster than others only because your implementation is better, not because of the new design, your novelty is questionable[^vanderkouwe2019sok-e8].

**Don't forget repetitions and run conditions.** You need enough repetitions and long enough runs to check that results are stable[^ralph2020empirical-e99]; keep all raw results, not just summary numbers[^ralph2020empirical-e101]. General practice for the number of repetitions, statistical tests, and effect sizes (how big the difference is, not just whether there is one) is in [Analysis and interpretation](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value); details of the measurement procedure are in [Benchmarking](benchmarking.md#step-4-design-the-measurement-procedure).

> **Example: evaluating fuzzers (security).** Klees et al. point out that proposing a new fuzzing algorithm means choosing a convincing baseline, a set of target programs (a benchmark suite), and meaningful configuration parameters[^klees2018evaluating-e1]. They examined 32 papers and found **problems in the evaluation of every one**[^klees2018evaluating-e2]. Their own experiments showed that repeated runs with the same configuration vary a lot, so a single run can lead to the wrong conclusion[^klees2018evaluating-e9], and that runs that are too short can produce misleading conclusions[^klees2018evaluating-e6]. In other subfields the specific parameters differ, but every engineering research evaluation has to think through the same five choices one by one: baseline, evaluation subjects, metrics, configuration, and randomness `[Our analysis]`.

**How big does the evaluation need to be?** The SIGSOFT standards hold that the empirical part of an engineering paper should not be expected to be as ambitious as a purely empirical paper; having few evaluation subjects is not a flaw if the field simply has few, or if the experiment is only one part of the overall validation[^ralph2020empirical-e94]. Yet surveys of specific subfields show evaluation problems are everywhere: defense papers at top systems security venues have on average 5 benchmarking flaws each, and only 1 paper in the sample had none[^vanderkouwe2019sok-e1]. The two don't contradict each other `[Our analysis]`: you can scale the evaluation to your resources and how innovative the work is (the less innovative, the more rigorous it must be[^ralph2020empirical-e90]), but fair comparison, multiple runs, and justifying your choices are not optional. Many of these flaws take very little extra work to avoid[^vanderkouwe2019sok-e12].

### Step 7: Write down the real limitations and threats to validity

- **Discuss the artifact's strengths, weaknesses, and limitations conceptually.** This is essential[^ralph2020empirical-e81].
- **State all assumptions.** They must be reasonable, consistent with each other, and consistent with the goals of the contribution[^ralph2020empirical-e86].
- **Disclose all major limitations**[^ralph2020empirical-e103]. Listing only trivial ones while leaving out the ones that matter leads readers to draw conclusions that are too strong[^blackburn2018sigplan-e3]. The antipattern is "results in the title, limitations in a footnote"[^zeller2021devil-e3].

Common real threats in engineering research: the implementation has bugs, so what you measured is not the method you designed; the baselines were misconfigured or reproduced incorrectly; the evaluation subjects are not representative or were seen during development; the metrics don't capture the quality you actually care about; the measurement environment introduces noise `[Our analysis]`. How to write threats to validity in general is in [Validity and limitations](../../../02_from-project-to-study/03_validity-and-limits.md).

### Step 8: Release your research artifacts

ACM defines a research **artifact** as a digital object that the authors created for the study or that the experiments produced, such as a software system, scripts that run experiments, input data, raw experimental data, or analysis scripts[^acm2020artifact-e1]. A well-structured, documented artifact lets others build directly on your work[^acm2020artifact-e8]. ACM's three kinds of artifact badges (Artifacts Evaluated, Artifacts Available, Results Validated) make good targets to prepare for; what they mean is in the [computer science field overview](../README.md#artifact-evaluation-and-badges).

- Provide the source code (or a complete description of a non-software artifact) and the input data[^ralph2020empirical-e87].
- Give what someone needs to reproduce the work: hardware platform, software versions, per-benchmark results, and absolute numbers, not only relative ones[^vanderkouwe2019sok-e13]. For methods that depend on initial inputs, such as fuzzing, explain how the seed inputs were obtained, and ideally release them too[^klees2018evaluating-e8]. Recording random seeds is covered in [Analysis and interpretation](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).
- If proprietary parts can't be released, say what they are and how to obtain them[^acm2020artifact-e6]; for anything missing from the replication package, explain the practical or ethical reason[^ralph2020empirical-e87]. With a clear and convincing reason, not providing a replication package is not a flaw[^ralph2020empirical-e97].
- Even when you can't release the artifact publicly, you can still apply for the Artifacts Evaluated badge: it only needs to be made available to the reviewers[^acm2020artifact-e7].

---

## 3. Checklist

This checklist follows mainly the SIGSOFT engineering research standard, with its benchmarking standard added for the evaluation part.

**Essential**

- [ ] Describe the artifact in enough detail, and explain why it is needed[^ralph2020empirical-e81]
- [ ] Explain the overall workflow and clearly mark which parts are new[^ralph2020empirical-e83]
- [ ] Discuss the artifact's strengths, weaknesses, and limitations conceptually[^ralph2020empirical-e81]
- [ ] Evaluate it with an empirical method, and say which one[^ralph2020empirical-e84]
- [ ] Compare it empirically against the best current alternatives, or explain why you couldn't[^ralph2020empirical-e85]
- [ ] State your assumptions; they are reasonable and don't contradict each other[^ralph2020empirical-e86]
- [ ] Explain why you chose this benchmark; discuss whether it measures what you want to measure[^ralph2020empirical-e99][^ralph2020empirical-e100]
- [ ] Let every configuration compete fairly on its merits; use enough repetitions and long enough runs[^ralph2020empirical-e99]
- [ ] Disclose all major limitations[^ralph2020empirical-e103]

**Desirable, and Extraordinary**

- [ ] Provide source code and input data; explain the reason for anything missing[^ralph2020empirical-e87]
- [ ] Discuss the artifact's theoretical basis; give correctness arguments for key theoretical contributions[^ralph2020empirical-e88]
- [ ] Explain the artifact with a running example used throughout the paper[^ralph2020empirical-e88]
- [ ] Evaluate in an industry-relevant setting, such as widely used open-source projects or with professional developers[^ralph2020empirical-e88]
- [ ] Deepen the community's understanding of design principles[^ralph2020empirical-e89]
- [ ] Deliver a breakthrough with clear practical benefits[^ralph2020empirical-e89]

**Not flaws** (criticisms the SIGSOFT standards list as invalid; you don't need to worry about them)

- No explicit research questions: engineering papers often use "problems" or "objectives" instead[^ralph2020empirical-e96]
- Not comparing against methods that could not be obtained or run[^ralph2020empirical-e95]
- Not providing a replication package when there is a clear practical or ethical reason[^ralph2020empirical-e97]
- "The empirical part is less ambitious than a purely empirical paper", "too few evaluation subjects" (when the field simply has few, or the experiment is only one part of the overall validation)[^ralph2020empirical-e94]
- "Not technically complex enough"[^ralph2020empirical-e96]
- "Not many people use this benchmark": a new benchmark can start out being proposed by a small group of researchers[^ralph2020empirical-e102]

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Comparing only against your own earlier work, or running competitors in a non-optimal configuration | It exaggerates the benefit of the new method[^vanderkouwe2019sok-e4] |
| Reporting only the gains, not the costs | Readers can't judge whether it's worth using[^vanderkouwe2019sok-e6][^zeller2021devil-e6] |
| Running only once | Repeated runs with the same configuration vary a lot, so a single run can lead to the wrong conclusion[^klees2018evaluating-e9] |
| Not stating the platform, versions, or seed inputs | Others can't reproduce the work[^vanderkouwe2019sok-e13][^klees2018evaluating-e8] |

---

## 5. Further reading

- **The overall framework**: Shaw 2003, "Writing Good Software Engineering Research Papers", uses three tables (research questions, results, validation) to set out what an engineering paper needs to answer; Shaw 2002 (in STTT, the International Journal on Software Tools for Technology Transfer) discusses what makes good software engineering research along the same three dimensions.
- **Checklists**: the engineering research and benchmarking standards in the SIGSOFT Empirical Standards; the SIGPLAN Empirical Evaluation Checklist (SIGPLAN is ACM's Special Interest Group on Programming Languages; the checklist leans toward programming languages and systems).
- **How a subfield systematically reflects on its own evaluations**: Klees et al. 2018 (fuzzing); van der Kouwe et al. 2019 (systems security, listing 22 kinds of benchmarking flaws); Carlini et al. 2019 (defenses against adversarial examples); Arp et al. 2022 (machine learning for security). Even if you don't work in these areas, read one to see where evaluations go wrong.
- **What not to do in an evaluation**: Zeller 2021, "The Devil's Guide to Incremental Research", an ironic list of tricks for padding out papers.

Links to every source are in the [source list](../../../../sources/README.md).

[^ralph2020empirical-e79]: SIGSOFT Engineering Research standard, Definition. [Evidence](../../../../sources/notes/ralph2020empirical.md#e79)
[^ralph2020empirical-e81]: SIGSOFT Engineering Research standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e81)
[^ralph2020empirical-e83]: SIGSOFT Engineering Research standard, footnote 1. [Evidence](../../../../sources/notes/ralph2020empirical.md#e83)
[^ralph2020empirical-e84]: SIGSOFT Engineering Research standard, Essential Attributes (methods). [Evidence](../../../../sources/notes/ralph2020empirical.md#e84)
[^ralph2020empirical-e85]: SIGSOFT Engineering Research standard, Essential Attributes (methods). [Evidence](../../../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e86]: SIGSOFT Engineering Research standard, Essential Attributes (other). [Evidence](../../../../sources/notes/ralph2020empirical.md#e86)
[^ralph2020empirical-e87]: SIGSOFT Engineering Research standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e87)
[^ralph2020empirical-e88]: SIGSOFT Engineering Research standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e88)
[^ralph2020empirical-e89]: SIGSOFT Engineering Research standard, Extraordinary Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e89)
[^ralph2020empirical-e90]: SIGSOFT Engineering Research standard, General Quality Criteria. [Evidence](../../../../sources/notes/ralph2020empirical.md#e90)
[^ralph2020empirical-e91]: SIGSOFT Engineering Research standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e91)
[^ralph2020empirical-e92]: SIGSOFT Engineering Research standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e92)
[^ralph2020empirical-e93]: SIGSOFT Engineering Research standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e93)
[^ralph2020empirical-e94]: SIGSOFT Engineering Research standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e94)
[^ralph2020empirical-e95]: SIGSOFT Engineering Research standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e95)
[^ralph2020empirical-e96]: SIGSOFT Engineering Research standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e96)
[^ralph2020empirical-e97]: SIGSOFT Engineering Research standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e97)
[^ralph2020empirical-e98]: SIGSOFT Engineering Research standard, footnote 4. [Evidence](../../../../sources/notes/ralph2020empirical.md#e98)
[^ralph2020empirical-e99]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e99)
[^ralph2020empirical-e100]: SIGSOFT Benchmarking standard, Essential Attributes (discussion). [Evidence](../../../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e101]: SIGSOFT Benchmarking standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e101)
[^ralph2020empirical-e102]: SIGSOFT Benchmarking standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e102)
[^ralph2020empirical-e103]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e103)
[^ralph2020empirical-e104]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e104)
[^shaw2003writing-e26]: Shaw 2003, §3.2. [Evidence](../../../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e27]: Shaw 2003, §3.1, Table 3. [Evidence](../../../../sources/notes/shaw2003writing.md#e27)
[^shaw2003writing-e28]: Shaw 2003, §4.1, Table 5. [Evidence](../../../../sources/notes/shaw2003writing.md#e28)
[^shaw2003writing-e10]: Shaw 2003, §4.1, after Table 5. [Evidence](../../../../sources/notes/shaw2003writing.md#e10)
[^shaw2003writing-e31]: Shaw 2003, §2.3. [Evidence](../../../../sources/notes/shaw2003writing.md#e31)
[^shaw2003writing-e32]: Shaw 2003, §4.2. [Evidence](../../../../sources/notes/shaw2003writing.md#e32)
[^shaw2003writing-e33]: Shaw 2003, §4.1, Table 5. [Evidence](../../../../sources/notes/shaw2003writing.md#e33)
[^shaw2003writing-e34]: Shaw 2003, §1. [Evidence](../../../../sources/notes/shaw2003writing.md#e34)
[^shaw2003writing-e36]: Shaw 2003, §3.3. [Evidence](../../../../sources/notes/shaw2003writing.md#e36)
[^shaw2003writing-e37]: Shaw 2003, §4.1, Table 5. [Evidence](../../../../sources/notes/shaw2003writing.md#e37)
[^blackburn2018sigplan-e1]: SIGPLAN Empirical Evaluation Checklist, Clearly Stated Claims. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e1)
[^blackburn2018sigplan-e12]: SIGPLAN Empirical Evaluation Checklist, Tested on training set. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e12)
[^blackburn2018sigplan-e3]: SIGPLAN Empirical Evaluation Checklist, Fails to acknowledge limitations. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e3)
[^zeller2021devil-e6]: Zeller 2021, THE RUBE GOLDBERG. [Evidence](../../../../sources/notes/zeller2021devil.md#e6)
[^zeller2021devil-e3]: Zeller 2021, THE ACHILLES HEEL. [Evidence](../../../../sources/notes/zeller2021devil.md#e3)
[^klees2018evaluating-e1]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e1)
[^klees2018evaluating-e2]: Klees et al. 2018, Abstract. [Evidence](../../../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees et al. 2018, §9. [Evidence](../../../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e4]: Klees et al. 2018, §9. [Evidence](../../../../sources/notes/klees2018evaluating.md#e4)
[^klees2018evaluating-e6]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e6)
[^klees2018evaluating-e7]: Klees et al. 2018, §8. [Evidence](../../../../sources/notes/klees2018evaluating.md#e7)
[^klees2018evaluating-e8]: Klees et al. 2018, §5. [Evidence](../../../../sources/notes/klees2018evaluating.md#e8)
[^klees2018evaluating-e9]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e9)
[^vanderkouwe2019sok-e1]: van der Kouwe et al. 2019, Abstract. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e1)
[^vanderkouwe2019sok-e2]: van der Kouwe et al. 2019, §II-A. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e2)
[^vanderkouwe2019sok-e3]: van der Kouwe et al. 2019, §II-A. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e3)
[^vanderkouwe2019sok-e4]: van der Kouwe et al. 2019, §II-D. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e5]: van der Kouwe et al. 2019, §II-E. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e5)
[^vanderkouwe2019sok-e6]: van der Kouwe et al. 2019, Appendix E2. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e6)
[^vanderkouwe2019sok-e7]: van der Kouwe et al. 2019, §II-E. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e7)
[^vanderkouwe2019sok-e8]: van der Kouwe et al. 2019, §II-E. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e8)
[^vanderkouwe2019sok-e9]: van der Kouwe et al. 2019, §II-B. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e9)
[^vanderkouwe2019sok-e10]: van der Kouwe et al. 2019, §II-C. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e10)
[^vanderkouwe2019sok-e11]: van der Kouwe et al. 2019, §VI. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e11)
[^vanderkouwe2019sok-e12]: van der Kouwe et al. 2019, §I. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e12)
[^vanderkouwe2019sok-e13]: van der Kouwe et al. 2019, Table I. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e13)
[^vanderkouwe2019sok-e14]: van der Kouwe et al. 2019, §II-D. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e14)
[^acm2020artifact-e1]: ACM Artifact Review and Badging policy v1.1, opening. [Evidence](../../../../sources/notes/acm2020artifact.md#e1)
[^acm2020artifact-e6]: ACM Artifact Review and Badging policy v1.1, note on the Functional level. [Evidence](../../../../sources/notes/acm2020artifact.md#e6)
[^acm2020artifact-e7]: ACM Artifact Review and Badging policy v1.1, Artifacts Evaluated. [Evidence](../../../../sources/notes/acm2020artifact.md#e7)
[^acm2020artifact-e8]: ACM Artifact Review and Badging policy v1.1, opening. [Evidence](../../../../sources/notes/acm2020artifact.md#e8)
[^carlini2019evaluating-e1]: Carlini et al. 2019, §2.5. [Evidence](../../../../sources/notes/carlini2019evaluating.md#e1)
[^arp2022dos-e2]: Arp et al. 2022, P9. [Evidence](../../../../sources/notes/arp2022dos.md#e2)
