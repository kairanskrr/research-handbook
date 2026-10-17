# Comparative evaluation

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science.

You have several existing approaches in front of you: a few large language models, a few static analysis tools, a few ways of writing prompts. Each paper says its own approach works well, but put them side by side and you can't tell which is better. The study you want to do is to measure them all with the same yardstick.

That is **comparative evaluation**: you don't build anything new; you answer "among existing approaches, which is better, by how much, and under what conditions". For an overview of research strategies, see [Key concepts](../00_start-here/key-concepts.md#research-strategy).

---

## 1. What kind of knowledge this research produces

**The central claim looks like this: "Under conditions C, measured by metric M, approach A is better than B (or about the same)."** Some hypothetical examples from "large language models and smart contract security" (these are not real findings):

- "On contracts actually deployed on-chain, large-language-model detection tools find reentrancy vulnerabilities at about the same rate as static analysis tools, but raise twice as many false positives."
- "The high detection rates reported in the papers disappear on a different set of contracts."
- "Of three prompt styles, the one that explains vulnerability patterns works best on every model."

Each sentence has three parts: **what is being compared** (existing tools or approaches), **with what yardstick** (the task set and metrics), and **how far the conclusion reaches** (the conditions). Leave out any one of them and readers have no way to judge the claim.

**How it differs from neighboring strategies**:

| | Comparative evaluation | [Building and improving](build_improve.md) | [Causal explanation](explain_causality.md) | [Measurement](measure.md) |
|---|---|---|---|---|
| Claim | Existing A is better than B | The new thing I built is better than what exists | Factor X causes outcome Y | This is the right way to measure something |
| Do you have a new artifact of your own? | No; everything compared is someone else's | Yes; the comparison is just one step in showing it is good | Not necessarily | A new measurement instrument or benchmark |
| Question it answers | Which is better, and by how much | Is my method good enough | Why | Is the yardstick accurate |

The line with building and improving: the software engineering empirical standards require engineering research to compare the new artifact empirically against state-of-the-art alternatives[^ralph2020empirical-e161], so in building and improving, comparison is often just one step. If your central claim is about **other people's tools**, it is comparative evaluation.

The line with causal explanation: comparison answers "how well does it work"; once you go on to ask "what made it work, and why"[^lipton2019troubling-e7], you are in causal explanation. For example, finding that prompt style A works best is comparison; changing one component of the prompt while holding everything else fixed, to test which component produced the gain, is causal explanation.

**Why it is worth doing.** The three examples below, from fuzzing, machine learning, and machine-learning-based prediction in political science, show that published comparative conclusions can be overstated:

- In fuzzing (testing programs with large numbers of random inputs to find bugs): the tool AFLFast did well on the target programs chosen in its original paper, but on two programs used in other papers it was no better than the baseline tool AFL[^klees2018evaluating-e3].
- In machine learning: a series of improvements credited to new network architectures turned out to come from better hyperparameter tuning; under equal conditions, the older method actually came first[^lipton2019troubling-e5].
- In research using machine learning to predict civil wars: once the errors were corrected, the complex models did not do noticeably better than logistic regression models from decades earlier[^kapoor2023leakage-e8].

Independent, fair comparisons are exactly what corrects conclusions like these.

**Write it down:** Write your central claim in the form "Under conditions C, measured by metric M, A is … than B." If you can't fill in C or M, you haven't thought the comparison through yet.

## 2. What evidence is enough

Ask yourself: **if I were the author of a tool that lost in my comparison, where would I attack?** Check these five places one by one.

### Was every competitor treated equally?

A typical unfairness is giving one tool more care than the others. A catalog of evaluation flaws in systems security includes "unfair benchmarking of competitors": comparing against competitors, but, for example, using a configuration that is not optimal for them[^vanderkouwe2019sok-e4]. The software engineering benchmarking standard likewise requires that different configurations of the systems under test can compete on their own merits, without artificial constraints[^ralph2020empirical-e149].

How:

- **Give every tool the same tuning budget and running conditions.** Research on adversarial examples (inputs crafted specifically to fool a machine learning model) has a similar requirement: when evaluating a defense, running off-the-shelf attacks with default hyperparameters is not enough, even if they are state-of-the-art attacks[^carlini2019evaluating-e1]. Carrying this over to large language models: the prompt wording and the way the output is parsed are "parameters" too, and every model deserves the same care.
- **If in doubt, ask the original authors.** A guide to benchmarking in systems research recommends contacting the other authors to confirm that your measurements are fair to their system[^heiserbenchmarking-e15].
- **Remember that "optimal conditions" differ from one subject to another.** Catalysis chemistry has a ready example: reaction conditions that suit one catalyst may be clearly suboptimal for another[^bligaard2016benchmarking-e7]. Software tools may be the same way: a single shared setting is not necessarily fair to every tool.

### Are the tasks representative?

The software engineering benchmarking standard lists benchmarking the right aspects and using a realistic benchmark with a representative workload among its general quality criteria[^ralph2020empirical-e155]. When evaluating randomized algorithms, the choice of case studies often strongly affects the results[^arcuri2014hitchhiker-e11].

How:

- **Explain how the tasks were selected.** Unbiased, representative subjects are often unavailable, but you must say how they were chosen[^arcuri2014hitchhiker-e15].
- **Don't cherry-pick subsets.** The advice from systems security: an arbitrary subset picked from a large test suite is unlikely to be representative of the whole; run everything that can reasonably be run, and justify anything you leave out[^vanderkouwe2019sok-e17].
- **Watch out for benchmarks that have been "gamed".** Authors in fuzzing warn that once a fixed benchmark has been used for a long time, tools start making special-purpose optimizations for it that bring no fundamental benefit[^klees2018evaluating-e7]. For large language models there is an extra layer: after a good benchmark is released, its questions spread all over the internet[^wei2024evals-e9]. This means they may already be in the models' training data, so when comparing large-language-model tools, it is best to include contracts that appeared after the models' training cutoff.

### Does the metric measure what you care about?

The software engineering benchmarking standard requires a discussion of the benchmark's construct validity, that is, whether it measures what it is supposed to measure[^ralph2020empirical-e100].

- **Proxy metrics can mislead.** Fuzzing papers often use "unique crashes" in place of the number of real bugs; this metric can badly overcount, and the apparent improvement may be small or nonexistent[^klees2018evaluating-e4].
- **For tools that make judgments, report how accurate they are.** The systems security flaw catalog points out that without knowing how accurate a system is, you can't judge its value[^vanderkouwe2019sok-e7]. Vulnerability detection is exactly this kind of tool, and accuracy means how many false positives and how many false negatives: if you report only the detection rate and not false positives, developers get incomplete information.
- **Count the costs too.** Systems security warns that measuring runtime alone is not enough; look at memory and other overheads as well[^vanderkouwe2019sok-e6]. A guide to evaluating randomized algorithms also says that in practice, choosing an algorithm means considering cost differences too, such as the input required from the user and the execution time[^arcuri2014hitchhiker-e6]. For large-language-model tools, the cost of each call and the running time count too.

### Keep some data for the final test only

The practices below come mainly from the evaluation literature in machine learning and programming languages. When comparing, you will most likely tune things as well: parameters for each tool, prompt wording, output parsing. Data you looked at while tuning can't be used to report the final results.

- **Set aside a held-out test set at the very start.** A methods guide for machine learning recommends splitting off part of the data at the start of the project and using it only once, at the end, to evaluate the single final setup[^lones2021avoid-e3].
- **Examples you consulted during development can't be reused for evaluation.** The empirical evaluation checklist from programming languages research says: if a system is meant to be general but was developed with close reference to specific examples, the evaluation must use data different from those examples[^blackburn2018sigplan-e12].
- **Don't keep trying setups on the test data.** The same machine learning guide says a common practice is to casually try different models and parameters until they do well on the test data[^lones2021avoid-e4]; the more times the test data is used, the more the results are tuned to that particular data[^lones2021avoid-e5].

When information meant for evaluation leaks into development, machine learning calls it "data leakage". One survey found such problems across 17 fields, affecting 294 papers, some of which reached wildly overoptimistic conclusions[^kapoor2023leakage-e1].

In the example of large language models detecting contract vulnerabilities: tune the prompt wording on a small batch of contracts first; once it is final, run it once on a separate batch you have never looked at, and report that run. The principle isn't limited to machine learning: a hypothesis you formed from one batch of samples has to be tested on a different batch.

### Is the difference real?

The practices below come mainly from the evaluation literature in fuzzing, software engineering and machine learning, plus one lesson from replication work in political science.

- **Run many times and look at the distribution.** For tools with randomness, such as fuzzers, run enough trials to characterize the performance distribution, and use statistical tests to confirm the difference isn't due to chance[^klees2018evaluating-e10]. Comparing single runs can give the opposite conclusion: on the same program, in one run AFL found more crashes than AFLFast, but the median over 30 runs had AFLFast finding far more than AFL[^klees2018evaluating-e11]. Large language model outputs are random too, so the same applies.
- **Record the random seed, and repeat with several seeds.** A random seed is the starting point a program uses to generate random numbers; fix it and a "random" process can be reproduced. Software analytics research points out that without the seed, nobody can exactly reproduce an algorithm that uses randomness[^menzies2019bad-e8]; replication experience at a political science journal also recommends setting the seed in your code so that every run produces the results in the paper[^eubank2016lessons-e7]. Experience from training neural networks is to fix the seed while debugging, so that two runs give the same result[^karpathy2019recipe-e4]. For evaluation, you repeat with multiple seeds; the two don't conflict.
- **Report variability, and correct for many tests.** A single evaluation is unreliable; it may overestimate or underestimate[^lones2021avoid-e6]. For how to report variability, effect sizes and multiple comparisons, see [Analysis and interpretation: report how big and how certain, not just p-values](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).
- **Report how big the difference is, not just "significant".** An effect size is a number for how large a difference is. With thousands of runs, almost any difference becomes significant, so you must analyze effect sizes as well[^arcuri2014hitchhiker-e9].
- **Report per subject.** The guide to evaluating randomized algorithms gives an example: effect sizes on five subjects of 0.6, 0.6, 0.6, 0.6 and 0.1 average to 0.5, which looks like "no difference", when in fact one side is better on four subjects and much worse on one[^arcuri2014hitchhiker-e21].

This isn't being fussy. In systems security, the 50 defense papers surveyed from top venues had an average of 5 evaluation flaws each[^vanderkouwe2019sok-e26]; the most common was giving no measure of variance or significance for the data, in 80% of the papers where it applied[^vanderkouwe2019sok-e15]. In fuzzing, every one of the 32 papers examined had problems in its experimental evaluation[^klees2018evaluating-e2].

For a more systematic discussion of validity, see [Validity and limitations](../02_do-the-project/04_validity-and-limits.md).

**Write it down:** List every tool you will compare, and next to each write: what configuration you will use, how much tuning effort it gets, and why that is fair to it.

## 3. Common research methods

The table below is our own summary, except where another source is cited.

| Method | When to use it | Notes |
|---|---|---|
| [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | What you compare is the software, tool or model itself, which can be run automatically and measured repeatedly | The most common method for comparative evaluation in computer science |
| [Controlled experiments with human participants](../06_methods/controlled_experiment.md) | You are comparing how people perform with different tools, e.g. which tool helps developers find vulnerabilities faster | Requires recruiting participants and random assignment |
| [Replication studies](../06_methods/replication.md) | You want to test whether a paper's comparative conclusion still holds under other conditions | Often combined with comparative evaluation |
| [Optimization studies](../07_fields/computer-science/practices/optimization_study.md) | Comparing search and optimization algorithms | A search algorithm should at least be compared against random search, to confirm its success isn't because the problem is simply too easy[^arcuri2014hitchhiker-e4] |
| [Systematic reviews and meta-analysis](../06_methods/meta_analysis.md) | Instead of running experiments yourself, you combine comparative results from published studies | Common in health research |

Methods and strategies are two separate layers: the same method can serve different strategies; see [Choosing a method](../02_do-the-project/02_choose-method.md).

## 4. How it shapes the whole project

The table below is our own summary, except where another source is cited for an item.

| Stage | What to watch for in comparative evaluation |
|---|---|
| Reading the literature | Don't just read the conclusions; also note **how** each paper compared: which subjects, how many runs, which metrics. Put it in a table and you can see whose conclusions hold up. Systematically examining the evaluation practices of a set of papers can be a study in its own right, for example going through the evaluations of 32 papers one by one[^klees2018evaluating-e23] |
| Choosing a topic | Comparisons are worth doing where people need to make a choice and the existing conclusions contradict each other or nobody has compared fairly. The Cochrane Handbook in health research lists the opportunity to "settle controversies arising from conflicting claims" as one benefit of meta-analysis (statistical methods for combining the results of several studies)[^higgins2024cochrane-e13] |
| Design | Before you start, fix the subjects, metrics, number of runs, and how big a difference counts as meaningful. The software engineering empirical standards list hypothesizing after the results are known (HARKing) in confirmatory research and reporting only the statistical tests that come out significant (p-hacking) as antipatterns[^ralph2020empirical-e27] |
| Execution | Keep all raw results, not just summary values[^ralph2020empirical-e158]. Record the version of every tool and model, because the model behind the same large language model interface may be updated |
| Writing | Shared requirements across several computer science evaluation guides: give results for each subject, not just an overall score[^heiserbenchmarking-e18]; give absolute numbers as well as relative ones[^vanderkouwe2019sok-e23]; state the platform and software versions[^vanderkouwe2019sok-e13]; report all p-values, significant or not[^arcuri2014hitchhiker-e17]. For writing in general, see [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md) |

**What if the tool you expected to win loses?**: In comparative evaluation there is no such thing as a "failed" conclusion. "The new tool is no better than the old one on real contracts" is a valuable claim in itself, provided the comparison is fair enough.

## 5. Which fields use it

Below we list only fields where our sources give support; our sources do not cover other fields.

- **Computer science.** The software engineering empirical standards have a dedicated benchmarking category, defined as competitive evaluation and comparison of methods, techniques or systems using standard tools[^ralph2020empirical-e143]. Systems security, software testing and machine learning all have literature specifically on how to make comparisons reliable; see the sections above.
- **Chemistry (catalysis).** The following requirements come from the benchmarking literature in catalysis research and speak only for that area. Metrics such as activity, selectivity and deactivation are used to compare new catalysts with standard ones[^bligaard2016benchmarking-e1]; when reporting a new catalyst, compare it with established or state-of-the-art catalysts under the same conditions[^bligaard2016benchmarking-e17]; to compare the selectivity of several catalysts, measure at the same conversion[^bligaard2016benchmarking-e15].
- **Computational materials science and physics.** The example comes from computational solid-state materials: a community effort compared 15 solid-state codes, evaluating results of the same kind of calculation on 71 elemental crystals[^lejaeghere2016reproducibility-e3]; the conclusion was that recent codes agree with each other very well, while older methods agree less well[^lejaeghere2016reproducibility-e4].
- **Health.** The Cochrane Handbook for Systematic Reviews says that questions about the effects of interventions are usually framed with PICO (population, intervention, comparison, outcome), where C is the comparison[^higgins2024cochrane-e5]. We read this as meaning that in health research, "comparing two treatments" is often also a causal question that calls for causal designs such as randomized trials, so the line between comparative evaluation and causal explanation is not as sharp as in computer science.

## 6. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Carefully tuning your favorite tool while the others run on default settings | What you are comparing is tuning effort, not the tools. In machine learning, improvements credited to new architectures turned out to come from better tuning[^lipton2019troubling-e5] |
| Choosing only tasks that favor one tool | On a different set of tasks the conclusion may flip[^klees2018evaluating-e3]; a systems guide says bluntly that evaluating only favorable cases is deceiving the reader[^heiserbenchmarking-e3] |
| Building a benchmark tailored to one tool | The software engineering benchmarking standard lists this as an antipattern[^ralph2020empirical-e157] |
| Reporting only the detection rate, not false positives | Without knowing the accuracy, you can't judge the tool's value[^vanderkouwe2019sok-e7] |
| Repeatedly checking the test data while tuning | The more times the test data is used, the more the results are tuned to that data[^lones2021avoid-e5] |
| Running each tool only once | A single run can give the opposite conclusion[^klees2018evaluating-e11] |
| Saying only "significant", not how big | With many runs, almost any difference is significant[^arcuri2014hitchhiker-e9] |
| Giving only the average across all tasks | An average can hide one side falling far behind on particular subjects[^arcuri2014hitchhiker-e21] |
| Not stating versions and platforms | Others can't reproduce the results or tell where the difference comes from[^vanderkouwe2019sok-e13] |
| Turning "which is better" straight into "why it is better" | A comparison only answers how well something works; "why" needs a separate test |

## 7. Further reading

- **ACM SIGSOFT Empirical Standards, Benchmarking standard** (the empirical standards of the Association for Computing Machinery's Special Interest Group on Software Engineering): essential attributes, desirable attributes and antipatterns for benchmarking.
- **Klees et al., Evaluating Fuzz Testing**: from fuzzing, with many experiments showing how conclusions flip when comparisons are done wrong.
- **van der Kouwe et al., SoK: Benchmarking Flaws in Systems Security**: from systems security, a catalog of 22 evaluation flaws[^vanderkouwe2019sok-e26] you can check against one by one before submitting.
- **Heiser, Systems Benchmarking Crimes**: a list of benchmarking "crimes" in systems research.
- **Arcuri & Briand, A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms**: when comparing algorithms with randomness, how to choose the number of runs, the statistical tests, and the effect sizes.

[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e100]: ACM SIGSOFT Empirical Standards, Benchmarking standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e143]: ACM SIGSOFT Empirical Standards, Benchmarking standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e143)
[^ralph2020empirical-e149]: ACM SIGSOFT Empirical Standards, Benchmarking standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e149)
[^ralph2020empirical-e155]: ACM SIGSOFT Empirical Standards, Benchmarking standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e155)
[^ralph2020empirical-e157]: ACM SIGSOFT Empirical Standards, Benchmarking standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e157)
[^ralph2020empirical-e158]: ACM SIGSOFT Empirical Standards, Benchmarking standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e158)
[^ralph2020empirical-e161]: ACM SIGSOFT Empirical Standards, Engineering Research standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e161)
[^lipton2019troubling-e5]: Lipton & Steinhardt 2019, §3.2, p. 3. [Evidence](../../sources/notes/lipton2019troubling.md#e5)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../sources/notes/lipton2019troubling.md#e7)
[^kapoor2023leakage-e8]: Kapoor & Narayanan 2023, Summary and the civil war prediction case study section. [Evidence](../../sources/notes/kapoor2023leakage.md#e8)
[^klees2018evaluating-e2]: Klees et al. 2018, Abstract. [Evidence](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e4]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e4)
[^klees2018evaluating-e7]: Klees et al. 2018, §8. [Evidence](../../sources/notes/klees2018evaluating.md#e7)
[^klees2018evaluating-e10]: Klees et al. 2018, §1. [Evidence](../../sources/notes/klees2018evaluating.md#e10)
[^klees2018evaluating-e11]: Klees et al. 2018, §1. [Evidence](../../sources/notes/klees2018evaluating.md#e11)
[^klees2018evaluating-e23]: Klees et al. 2018, Table 1 and §4. [Evidence](../../sources/notes/klees2018evaluating.md#e23)
[^vanderkouwe2019sok-e26]: van der Kouwe et al. 2019, Abstract. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e26)
[^vanderkouwe2019sok-e4]: van der Kouwe et al. 2019, §II-D. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e6]: van der Kouwe et al. 2019, Appendix E2. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e6)
[^vanderkouwe2019sok-e7]: van der Kouwe et al. 2019, §II-E. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e7)
[^vanderkouwe2019sok-e13]: van der Kouwe et al. 2019, §II, Table I. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e13)
[^vanderkouwe2019sok-e15]: van der Kouwe et al. 2019, §IV. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e15)
[^vanderkouwe2019sok-e17]: van der Kouwe et al. 2019, §VI and §II-A. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e17)
[^vanderkouwe2019sok-e23]: van der Kouwe et al. 2019, §II-F. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e23)
[^arcuri2014hitchhiker-e4]: Arcuri & Briand 2014, §3. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e4)
[^arcuri2014hitchhiker-e6]: Arcuri & Briand 2014, §4. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e6)
[^arcuri2014hitchhiker-e9]: Arcuri & Briand 2014, §8. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e9)
[^arcuri2014hitchhiker-e11]: Arcuri & Briand 2014, §10.1. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e11)
[^arcuri2014hitchhiker-e15]: Arcuri & Briand 2014, §11. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e15)
[^arcuri2014hitchhiker-e17]: Arcuri & Briand 2014, §11. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e17)
[^arcuri2014hitchhiker-e21]: Arcuri & Briand 2014, §10.2. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e21)
[^carlini2019evaluating-e1]: Carlini et al. 2019, §2.5. [Evidence](../../sources/notes/carlini2019evaluating.md#e1)
[^heiserbenchmarking-e3]: Heiser, Systems Benchmarking Crimes, Not evaluating potential performance degradation. [Evidence](../../sources/notes/heiserbenchmarking.md#e3)
[^heiserbenchmarking-e15]: Heiser, Systems Benchmarking Crimes, Unfair benchmarking of competitors. [Evidence](../../sources/notes/heiserbenchmarking.md#e15)
[^heiserbenchmarking-e18]: Heiser, Systems Benchmarking Crimes, Missing sub-benchmark results. [Evidence](../../sources/notes/heiserbenchmarking.md#e18)
[^wei2024evals-e9]: Jason Wei 2024, section on test set contamination. [Evidence](../../sources/notes/wei2024evals.md#e9)
[^bligaard2016benchmarking-e1]: Bligaard et al. 2016, Abstract. [Evidence](../../sources/notes/bligaard2016benchmarking.md#e1)
[^bligaard2016benchmarking-e7]: Bligaard et al. 2016, §2.2, p. 2595. [Evidence](../../sources/notes/bligaard2016benchmarking.md#e7)
[^bligaard2016benchmarking-e15]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../sources/notes/bligaard2016benchmarking.md#e15)
[^bligaard2016benchmarking-e17]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../sources/notes/bligaard2016benchmarking.md#e17)
[^lejaeghere2016reproducibility-e3]: Lejaeghere et al. 2016, Abstract. [Evidence](../../sources/notes/lejaeghere2016reproducibility.md#e3)
[^lejaeghere2016reproducibility-e4]: Lejaeghere et al. 2016, Abstract. [Evidence](../../sources/notes/lejaeghere2016reproducibility.md#e4)
[^higgins2024cochrane-e5]: Cochrane Handbook version 6.5, Chapter 1, §1.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e5)
[^higgins2024cochrane-e13]: Cochrane Handbook version 6.5, Chapter 10, Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e13)
[^lones2021avoid-e3]: Lones 2021, §3.1, p. 8. [Evidence](../../sources/notes/lones2021avoid.md#e3)
[^lones2021avoid-e4]: Lones 2021, §4.3, p. 15. [Evidence](../../sources/notes/lones2021avoid.md#e4)
[^lones2021avoid-e5]: Lones 2021, §4.3, p. 15. [Evidence](../../sources/notes/lones2021avoid.md#e5)
[^lones2021avoid-e6]: Lones 2021, §4.4, p. 15. [Evidence](../../sources/notes/lones2021avoid.md#e6)
[^blackburn2018sigplan-e12]: SIGPLAN Empirical Evaluation Checklist, Tested on training set. [Evidence](../../sources/notes/blackburn2018sigplan.md#e12)
[^kapoor2023leakage-e1]: Kapoor & Narayanan 2023, Summary. [Evidence](../../sources/notes/kapoor2023leakage.md#e1)
[^menzies2019bad-e8]: Menzies & Shepperd 2019, §4.4. [Evidence](../../sources/notes/menzies2019bad.md#e8)
[^eubank2016lessons-e7]: Eubank 2016, Randomizations and Simulations. [Evidence](../../sources/notes/eubank2016lessons.md#e7)
[^karpathy2019recipe-e4]: Karpathy 2019, Step 2 (fix random seed). [Evidence](../../sources/notes/karpathy2019recipe.md#e4)
