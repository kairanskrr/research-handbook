# Benchmarking: comparing systems, tools, or models with an automated, repeatable procedure

This page is about **benchmarking**: using a standard workload or task set (a **benchmark**) and an automated, repeatable procedure to measure and compare how several software systems, tools, or models perform, for example in speed, reliability, security, or accuracy.

**Scope** `[Our analysis]`: this is a computer science practice, and the examples and standards come mainly from systems, programming languages, security, software testing, and machine learning. It most often serves the [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md) research strategy; when you check whether the benchmark itself can be trusted, it also touches on [Measurement](../../../05_research-strategies/measure.md). What makes a comparison fair and when a difference is real apply to every field and are covered on the strategy pages; this page covers only what is specific to benchmarking.

Benchmarking is often part of another kind of study: you propose a new method or tool (engineering research), then use benchmarking to show that it is better. What this page describes applies in both cases. For multiple runs and random seeds, see [Comparative evaluation: is the difference real?](../../../05_research-strategies/compare_evaluate.md#is-the-difference-real); for statistics in general, see [Analysis and interpretation: report how big the difference is and how certain, not just the p-value](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value); for how to write about threats to validity in general, see [Validity and limitations](../../../02_do-the-project/04_validity-and-limits.md).

**After reading this page, you should be able to:**

- judge whether your question is one that benchmarking can answer;
- choose representative benchmarks and configure every system you compare fairly;
- design the measurement procedure: warm-up, repetition, and control of environmental noise;
- analyze results with confidence intervals and effect sizes, and summarize scores across benchmarks correctly;
- write a report others can reproduce, and judge whether the benchmark itself measures what you want it to;
- recognize and avoid the common "benchmarking crimes".

---

## 1. What this research is, and when to use it

The ACM SIGSOFT (Association for Computing Machinery Special Interest Group on Software Engineering) Empirical Standards define benchmarking as using a standard tool (the benchmark) for the **competitive evaluation and comparison** of methods, techniques, or systems[^ralph2020empirical-e143]. Two conditions apply: it studies software systems in a defined environment with an **automated, repeatable procedure**, and it studies how they perform under a **specific workload or usage scenario**[^ralph2020empirical-e144].

A benchmark has four parts[^ralph2020empirical-e147]:

1. **The quality being measured**: performance, availability, scalability, security, and so on
2. **The metric**: the number that quantifies that quality
3. **The measurement method**: how that number is measured
4. **The workload**: what the system under test is doing during measurement, for example which programs it runs, which requests it handles, which questions it answers

In machine learning, a "benchmark" is usually a dataset plus a scoring method (often called an eval), and the thing being tested is a model; the same logic applies `[Our analysis]`.

**How it differs from related kinds of study:**

| | Benchmarking | Engineering research | Experiments with human participants | Quantitative simulation |
|---|---|---|---|---|
| What is studied | The software systems, tools, or models themselves | A new method or tool you propose | People (for example, developers using a tool) | A model of a system |
| Where the evidence comes from | Automated runs and measurements on the benchmark | Evaluating the new tool through benchmarking, experiments, case studies, and so on | Participants complete tasks and their performance is measured | Running the model in an artificial environment |
| Typical question | Under workload W, which is faster or more accurate, system A or B? | Does my new tool solve the problem, and is it better than existing approaches? | Are people who use this tool more productive? | What happens if the network grows tenfold? |

Based on: the scope of the SIGSOFT benchmarking standard[^ralph2020empirical-e145] and the engineering research standard[^ralph2020empirical-e160][^ralph2020empirical-e161]; the comparison across columns is our own `[Our analysis]`.

**How to choose:**

- **What you study is the software system itself, and it can be run automatically and measured repeatedly**: use benchmarking[^ralph2020empirical-e145]. If the results depend on how people use it, you need an experiment with human participants; if you are studying a model of the system rather than the system itself, it is simulation `[Our analysis]`.
- **You have proposed a new tool**: this is engineering research. Engineering research must compare the new tool empirically against state-of-the-art alternatives or benchmarks[^ralph2020empirical-e161], and benchmarking is one common way to do it[^ralph2020empirical-e160].
- **Benchmarking can also be the contribution in itself**: a systematic comparison of a set of existing tools, or a new benchmark. A good benchmark sets the direction for a whole field: evals are incentives for the research community, and breakthroughs are often tied to big gains on some benchmark[^wei2024evals-e1].

If your main contribution is a new method that you show works using benchmarks, see [Engineering research](engineering_research.md); for the other computer science practices, see [Research practices specific to computer science](README.md).

---

## 2. How to do it

Benchmarking goes wrong rarely because authors mean to cheat, and mostly because they don't take measurement seriously enough[^vanderkouwe2019sok-e25]. But the problems are very widespread: a survey of system defense papers at top security conferences found an average of five benchmarking flaws per paper, and only one paper in the sample had none[^vanderkouwe2019sok-e1]; among the programming language and systems papers Kalibera & Jones surveyed that used execution time as their main metric, 71 gave no measure of variation at all (such as variance or a confidence interval)[^kalibera2013rigorous-e1]. The steps follow.

### Step 1: State the claim and choose the right metrics

**How:**

1. **First write down the claim you want to support**, for example "on a multicore server, A has higher throughput than B, with no more than 10% memory overhead". For how to state a claim clearly, and why you must justify using a proxy metric in place of what you really care about, see [From research questions to an evidence plan](../../../02_do-the-project/01_question-to-evidence.md).
2. **Measure the costs too.** A method that improves performance has to show two things: it clearly improves where you care, and it doesn't clearly make things worse elsewhere[^heiserbenchmarking-e3]. Measure all important effects and show the system's real costs[^blackburn2018sigplan-e21]; measuring only run time and not other important performance characteristics makes the evaluation incomplete[^vanderkouwe2019sok-e20].
3. **List every dimension that could be affected.** Think first about which aspects your approach might affect (CPU, concurrency, memory, I/O, system calls, and so on), and include at least one suitable benchmark for each[^vanderkouwe2019sok-e11].

**Why:** Heiser says that evaluating only the scenarios that favor you is deceptive[^heiserbenchmarking-e3].

**Where people go wrong:** a metric looks reasonable but actually measures the wrong thing. In fuzzing (automatically generating random inputs to find bugs in a program), many papers don't count real bugs but use heuristics to count "unique crashes"; these heuristics can greatly overcount bugs, or wrongly merge them and undercount, so the apparent improvement may be tiny or even spurious[^klees2018evaluating-e4].

### Step 2: Choose benchmarks, and don't cherry-pick subsets

**How:**

1. **Prefer recognized standard benchmarks, and explain why you chose them**, for example because they are relevant to your problem and not outdated[^ralph2020empirical-e146][^blackburn2018sigplan-e16]. Use them where they fit: you can't study parallel performance with a single-threaded benchmark suite[^blackburn2018sigplan-e16].
2. **If you use a non-standard benchmark (trimmed or home-grown), give your reasons and its limitations**, and explain why a standard benchmark would be worse[^blackburn2018sigplan-e17].
3. **If you build a new benchmark**, spell out the four parts described above[^ralph2020empirical-e147].
4. **Run the whole suite.** Run every sub-benchmark that can reasonably be run, and explain individually why any were left out[^vanderkouwe2019sok-e17][^heiserbenchmarking-e4]. If you ran only a subset, you must **never** report an overall score for the whole suite (such as mean speedup)[^heiserbenchmarking-e4].
5. **When you pick from a large pool of candidates, say how you picked**: random selection is fine; "arbitrary" selection is not[^heiserbenchmarking-e5].
6. **If you claim benefits for real applications, measure on real applications.** A microbenchmark that measures one operation does not represent overall performance; you need macro-benchmarks (complete applications or workloads that represent real use)[^blackburn2018sigplan-e20][^heiserbenchmarking-e7].
7. **Cover the realistic range of parameters.** Vary key parameters over a range to see how sensitive the results are to them[^blackburn2018sigplan-e24]. Heiser points out that parameter ranges are often chosen to make the system look good rather than to represent real workloads[^heiserbenchmarking-e6]. If throughput keeps scaling linearly with concurrency, the range you tested is often too narrow[^vanderkouwe2019sok-e18].
8. **Data you used during development can't be used again for evaluation** (for why, see [Comparative evaluation: keep some data for the final test only](../../../05_research-strategies/compare_evaluate.md#keep-some-data-for-the-final-test-only)). In benchmarking, the workloads used to tune or calibrate a method and the workloads used to evaluate it must not overlap at all[^heiserbenchmarking-e12].
9. **Where results depend on the input, use several sets of inputs.** In fuzzing, AFLFast did well on the target programs chosen in its original paper, but on two targets used by other papers it was no better than AFL (a widely used fuzzer that AFLFast builds on)[^klees2018evaluating-e18]. In machine learning, evaluating models on several datasets is more reliable[^lones2021avoid-e17].

**Why:** using a biased set of benchmarks to "prove" a point that a more complete evaluation might overturn is "the mother of all benchmarking crimes"[^heiserbenchmarking-e2]. It is also common: in the security survey above, 69% of papers trimmed benchmark suites without justification, second only to giving no measure of variation (80%)[^vanderkouwe2019sok-e15].

**Where people go wrong:**

- Writing "we picked a representative subset" or "we show typical results here". Heiser's answer: there is no such thing as a "representative subset" of SPEC CPU (the CPU benchmark suite from the Standard Performance Evaluation Corporation)[^heiserbenchmarking-e5].
- Tailoring a benchmark to your own method, or hiding the method's weaknesses behind benchmark experiments irrelevant to the problem. The SIGSOFT standard lists both as antipatterns[^ralph2020empirical-e157].

> **Where sources disagree: do standard benchmarks make everyone chase leaderboards?**
> - Klees et al. warn that once a fixed set of benchmarks is widely used, tools may start adopting heuristics and strategies that work especially well on those benchmark programs but bring no fundamental benefit, that is, **overfitting** to the benchmark (fitting one dataset so closely that the method fails on other data)[^klees2018evaluating-e7].
> - Lones warns that in machine learning, when a whole community keeps comparing models on the same test set, the best one may simply have happened to overfit that test set[^lones2021avoid-e15].
> - The authors of the SIGPLAN (ACM Special Interest Group on Programming Languages) checklist have heard this concern too, but in the papers they reviewed, trimming benchmark suites and cherry-picking particular programs were more common[^blackburn2018sigplan-e18].
>
> In practice `[Our analysis]`: both risks are real, and which matters more depends on the research area. Guard against cherry-picking subsets first, and also watch for overfitting to benchmarks: use several benchmarks or datasets, and don't read too much into small gains on public benchmarks[^lones2021avoid-e15][^lones2021avoid-e17].

### Step 3: Choose the systems to compare, and configure each one fairly

For how to choose baselines and why you must compare against strong ones, see [Building and improving](../../../05_research-strategies/build_improve.md#get-the-baseline-running-early) and [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md#was-every-competitor-treated-equally). In benchmarking, also pay particular attention to the points below.

**Choose the right baseline:**

- **Be clear about what the "baseline" actually is.** Often it is the state of the art; it can also be the theoretical optimum or the hardware limit[^heiserbenchmarking-e13]. In systems security research, the right baseline is usually the original system with default settings and no defense enabled; don't add non-default compiler flags or emulation to the baseline, slowing it down and hiding your overhead in it[^vanderkouwe2019sok-e19].
- **Don't compare only against your own earlier version**; compare against a recognized standard[^heiserbenchmarking-e14].
- **When the state of the art changes, the baseline changes with it.** The new state of the art is the baseline that later work must use[^heiserbenchmarking-e16].

**Configure fairly:**

1. **The different configurations under test compete on their merits, without artificial handicaps**[^ralph2020empirical-e149].
2. **Tune everyone equally.** You tuned your own system as far as it will go; did you put the same effort into the competitors[^heiserbenchmarking-e15]? Compiling the competitor at the lowest optimization level (-O0) and your own at the highest (-O3), for example, is unfair[^blackburn2018sigplan-e15]. The same logic applies elsewhere (such as hyperparameter tuning in machine learning); see [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md#was-every-competitor-treated-equally).
3. **When in doubt, ask the competitor's authors.** Heiser's own system was once benchmarked by others in a configuration with debugging enabled by default[^heiserbenchmarking-e15].
4. **The platform must match the claim.** A claim about phone performance can't be tested only on a server[^blackburn2018sigplan-e23].
5. **When a method has several components, measure each component's contribution separately** (an ablation study; see [Building and improving](../../../05_research-strategies/build_improve.md#2-what-evidence-is-enough)). Otherwise the system may be faster only because the implementation is better written, not because the new design does anything[^vanderkouwe2019sok-e20].

### Step 4: Design the measurement procedure

**How:**

1. **Keep the environment quiet.** Make sure the system is idle before the experiment starts[^heiserbenchmarking-e20]; turn off system services that could interfere with measurement[^kalibera2013rigorous-e10].
2. **Warm up first, then time.** Many systems are slower in the first few iterations: caches aren't filled yet, just-in-time compilation (compiling hot code to machine code at run time) hasn't finished, connections aren't set up. Run enough untimed warm-up iterations first[^heiserbenchmarking-e24], and leave the first iteration out of the average[^hoefler2015scientific-e12]. Distinguish **startup performance** from **steady-state performance**, which are measured differently: for startup performance, restart the program each time and run one iteration; for steady-state performance, run many iterations after each start and collect data only once steady state is reached[^georges2007statistically-e3]. Also decide whether caches should be "cold" or "warm", whichever is closer to real use[^hoefler2015scientific-e12].
3. **Repeat, and repeat at the right level.** The number of repetitions and the run length must be enough to assess how stable the results are[^ralph2020empirical-e150]. Variation can come from different levels: compilation, each program launch, each iteration. Repeat at least at the **highest level where random variation occurs**, for example by recompiling or relaunching the program, not just by looping more within one run[^kalibera2013rigorous-e6]. To find out how many repetitions you need, run a small pilot first and work backward from the confidence interval[^hoefler2015scientific-e17].
4. **Watch for measurement bias.** Seemingly irrelevant factors can systematically favor one system. As reported by Kalibera & Jones, Mytkowicz et al. found that the total size of Unix environment variables and the order of object files at link time can both cause significant measurement bias[^kalibera2013rigorous-e3]; but when Kalibera & Jones repeated this with SPEC's full-size reference inputs, they found that the effects, though present, were very small[^kalibera2013rigorous-e4]. How large the bias is depends on the platform and the benchmark, and you can't know it in advance `[Our analysis]`. The remedy is to identify variables that affect the results but are outside your control, and make them either controlled or randomized, for example by randomizing link order[^kalibera2013rigorous-e5]; randomize any environment parameters you can't control[^hoefler2015scientific-e10].
5. **Shuffle the order and interleave measurements.** Measure the same data point several times in a row and also at separated times[^heiserbenchmarking-e22]; repeating the measurements in reverse order can reveal interference between them[^heiserbenchmarking-e21].
6. **Mind the timing itself.** Reading a timer has overhead; make sure it is only a small fraction of the measured duration (under 5% is recommended)[^hoefler2015scientific-e13]; use many iterations to remove the effect of clock resolution[^heiserbenchmarking-e24].
7. **For randomized algorithms, seeds and run length are experimental parameters.** Methods such as fuzzing and machine learning are inherently random. Fuzzing performance varies a lot with the initial seed inputs, yet most papers choose them arbitrarily and don't report them[^klees2018evaluating-e13]; timeouts shorter than 5 to 6 hours can lead to misleading conclusions[^klees2018evaluating-e12]. The timeout setting is itself part of the benchmark[^blackburn2018sigplan-e19]. Klees et al. recommend for fuzzing: multiple trials with statistical tests, timeouts of at least 24 hours (or a justification for shorter ones), and plots of performance over time[^klees2018evaluating-e16].
8. **(Systems) Use an open-loop load generator.** Open loop means requests are sent on a predetermined schedule, without waiting for the system under test to finish the previous one. When testing transaction-oriented systems such as servers, the rate at which requests are generated should not depend on how fast the system under test is[^blackburn2018sigplan-e25].
9. **Check that the results are correct.** Read back data written to disk or the network and compare it[^heiserbenchmarking-e21]. Fast but wrong doesn't count as fast.
10. **Keep all the raw data and analyze it offline afterward.** Collecting only aggregated numbers (such as averages) is an antipattern[^ralph2020empirical-e158].

**Why:** performance on modern systems is inherently nondeterministic, and with too few trials you may mistake noise for signal[^blackburn2018sigplan-e27]. According to Mytkowicz et al.'s figures, as cited by Kalibera & Jones, the median performance improvement reported in programming languages and systems is about 10%, which could easily fall within measurement error[^kalibera2013rigorous-e2].

### Step 5: Analyze the results

For why you can't report only the mean, how to do significance tests, and what an effect size is, see [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value). In benchmarking, watch for the following:

1. **Don't report only the best run.** Current practice is all over the place: some report the mean of several runs, some the best run, some the worst[^georges2007statistically-e1]. Looking only at the best run, you might conclude that one garbage collector is clearly faster; looking at confidence intervals, they actually overlap, and the difference is quite likely just random variation[^georges2007statistically-e2].
2. **Which measure of variation to report.** Confidence intervals help you tell whether a difference is random variation or real[^georges2007statistically-e4]. When measured values are uncertain, report confidence intervals[^hoefler2015scientific-e5]; at the very least, report the standard deviation[^heiserbenchmarking-e10].
3. **Don't assume a normal distribution; check first**[^hoefler2015scientific-e6]. When comparing two systems, use statistically sound methods, such as checking whether confidence intervals overlap, or analysis of variance (ANOVA)[^hoefler2015scientific-e7]. To compare randomized algorithms you can use the Mann-Whitney U test, which makes no assumptions about the distribution[^klees2018evaluating-e14].
4. **Say "how much better", not just "whether better"**[^klees2018evaluating-e15]. Kalibera & Jones recommend reporting performance changes as confidence intervals for the effect size: this gives the size of the change, the margin of error, and the level of confidence at once[^kalibera2013rigorous-e8]. Even a large speedup should come with an estimate of measurement error[^kalibera2013rigorous-e9].
5. **Think about which statistic to report.** If you care about worst-case latency, neither the mean nor the median is enough; report higher percentiles[^hoefler2015scientific-e8].
6. **Get relative numbers right**:
   - The denominator must be the baseline. If the baseline takes 60 seconds and the new system 45, say it is "25% faster", not that "the original system is 33% slower"[^heiserbenchmarking-e9].
   - Distinguish percentages from percentage points[^heiserbenchmarking-e9]. Overhead going from 10% to 20% is not "10% more" but 100% more[^vanderkouwe2019sok-e24].
   - (Systems) A throughput drop of x% does not mean an overhead of x%. When the CPU isn't fully loaded, extra overhead is absorbed by idle time; when comparing throughput you must also compare CPU load[^heiserbenchmarking-e8].
7. **Don't report more precision than your error allows.** If the error is plus or minus 1%, don't report "49.9%"[^blackburn2018sigplan-e30].

**Significance tests or effect sizes?** For the two views and what to do in practice, see [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value). In benchmarking, Klees et al. recommend using statistical tests to confirm an improvement is not due to chance[^klees2018evaluating-e10] and then estimating the effect size[^klees2018evaluating-e15]; Kalibera & Jones argue instead that significance tests conflate sample size with practical importance, and advocate reporting confidence intervals for the effect size directly[^kalibera2013rigorous-e7][^kalibera2013rigorous-e8].

> **Where sources disagree: how should results across several benchmarks be combined into one number?** (**Geometric mean**: multiply n numbers together and take the nth root; **harmonic mean**: the reciprocal of the average of the reciprocals, often used for rates `[Our analysis]`)
> - Heiser, van der Kouwe et al.: once scores are normalized (for example, divided by the baseline), the arithmetic mean is meaningless; use the geometric mean[^heiserbenchmarking-e11][^vanderkouwe2019sok-e22].
> - Hoefler & Belli: avoid averaging ratios where possible; instead summarize the costs behind them (such as run time, with the arithmetic mean) or the rates (such as operations per second, with the harmonic mean); use the geometric mean only when those aren't available[^hoefler2015scientific-e4].
> - The SIGPLAN checklist: use the geometric mean only for values on different scales, the harmonic mean for rates, and give the median when there are outliers[^blackburn2018sigplan-e28].
>
> In practice `[Our analysis]`: whichever you use, state which mean it is and why[^vanderkouwe2019sok-e21], and also give the result for each sub-benchmark[^heiserbenchmarking-e18].

### Step 6: Write the report

**How:**

1. **Describe the platform and the software.** Give every platform characteristic that could affect the results, such as CPU model, number of cores, clock speed, memory size, and caches, plus the network card if networking is involved; for software, give the versions of the operating system, hypervisor, compiler, and other tools[^heiserbenchmarking-e17]. Report every parameter, including default values[^blackburn2018sigplan-e22]. "Run on supercomputer X" is not enough: systems get upgraded, and others may not know its specifications[^hoefler2015scientific-e11]. Record every factor that varied and the values it took[^hoefler2015scientific-e9]. These items are the easiest to fix: you already have the information, so just write it down[^vanderkouwe2019sok-e21].
2. **Give results for every sub-benchmark**, not just the overall score. With only the overall score, at worst it hides problems, and at best it loses information[^heiserbenchmarking-e18].
3. **Give absolute numbers, not just ratios**[^heiserbenchmarking-e19]. Absolute numbers let readers sanity-check your results; and overhead looks smaller when the baseline is slow, which absolute numbers let readers see[^vanderkouwe2019sok-e23]. When reporting a speedup, give the absolute performance of the base case[^hoefler2015scientific-e2].
4. **Report all results, not just the best ones**[^hoefler2015scientific-e3] (for why you can't report only the "best improvement", see [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value)). Use data selectively, for example by removing outliers, only if you really know what you are doing, and say so explicitly in the paper[^heiserbenchmarking-e23].
5. **Where possible, give performance bounds** (such as the hardware's theoretical peak), to help readers see how far the results are from the "ceiling"[^hoefler2015scientific-e14].
6. **Draw honest figures.** An axis that doesn't start at zero exaggerates differences; ratios (such as speedups) should be plotted on a log scale, or normalized to the lowest (or highest) value[^blackburn2018sigplan-e29]. Connect measurement points with lines only when showing a trend[^hoefler2015scientific-e15].
7. **Report honestly any problems you hit while running**, for example benchmarks that crashed or timed out[^ralph2020empirical-e152].

**Why:** even when others can't fully reproduce your experiment, the report should give enough information for readers to understand the experiment, draw their own conclusions, and judge how certain the conclusions are[^hoefler2015scientific-e1].

### Step 7: Release artifacts so others can reproduce the work

An **artifact** is the code, data, and scripts that accompany a paper. For how to organize them so every number can be traced, see [Organizing your research materials](../../../08_throughout/organizing_materials.md).

1. **Release supplementary material**: data and analysis scripts, plus detailed documentation if it is a new benchmark[^ralph2020empirical-e151]. Ideally release the experiments' source code; at least release the input data and the programs that generated it[^hoefler2015scientific-e9].
2. **Make the benchmark ready to use**, so others can reproduce the work independently; use or create open-source benchmarks where possible[^ralph2020empirical-e151][^ralph2020empirical-e152].
3. **Put your benchmarking setup into your regression tests**[^heiserbenchmarking-e20]. That way it reruns every time the code changes, and you catch performance changes early `[Our analysis]`.
4. Many computer science conferences have **artifact evaluation**: after the paper is accepted, a committee checks whether the paper's claims and evidence are consistent with the submitted code and data[^blackburn2018sigplan-e31]. Prepare your materials to the standard that would pass artifact evaluation; for ACM's badges and what they mean, see [Artifact evaluation and badges](../README.md#artifact-evaluation-and-badges) in the field overview.

---

## 3. Is the benchmark itself valid?

So far this page has been about how to use a benchmark well. There is a more fundamental question: **does this benchmark measure what you want to measure?** The SIGSOFT standard lists this as something you must discuss, under the name construct validity[^ralph2020empirical-e100]. The overall requirements are that measurement is fair, repeated experiments give consistent results, the "right" aspects are measured, the benchmark is realistic, and the workload is representative[^ralph2020empirical-e155]. van der Kouwe et al. put it similarly: an evaluation must be complete (test every claimed contribution, and also show how large the negative effects are) and sound (every number measures what it is meant to, with reasonable precision and repeatability)[^vanderkouwe2019sok-e16].

**Common ways of measuring the wrong thing:**

- **The benchmark doesn't match the claim.** Using several copies of uniprocessor programs that don't communicate with each other to measure multiprocessor scalability: these programs make almost no system calls and do no cross-processor communication, so they should scale linearly anyway; a real scalability test needs workloads that communicate across processors and use system calls[^heiserbenchmarking-e26].
- **Measuring on a simplified simulated system.** If you have to use simulation, make sure the simulation model's simplifying assumptions don't affect the aspect of performance you are looking at, and tell your readers[^heiserbenchmarking-e25].
- **The metric is a heuristic stand-in.** See the fuzzing example in Step 1. The advantage of synthetic benchmark suites (sets of programs with deliberately injected known bugs) is that they are defined independently of any particular algorithm and their bugs can be counted reliably[^klees2018evaluating-e18].

**(Machine learning) What a good eval looks like.** Jason Wei points out that it is easier to make a bad eval than a good one[^wei2024evals-e12], and lists the features of a good eval: enough examples, ideally at least 1,000, or the results are noisy[^wei2024evals-e2]; high quality, with few errors in the reference answers[^wei2024evals-e3] and extremely accurate grading[^wei2024evals-e7]; a single-number metric[^wei2024evals-e4]; easy to run[^wei2024evals-e5]; a meaningful task[^wei2024evals-e6]; and not saturated too quickly[^wei2024evals-e8]. Also note that how prompts are written and how answers are parsed both affect scores[^wei2024evals-e11]; and for evals in which people compare model outputs pairwise, it is unclear what exactly is being measured, for example how much style counts[^wei2024evals-e10].

**(Machine learning) Data contamination.** The worst kind of data contamination is when a large language model has seen a benchmark's test set during training and is then evaluated on that same benchmark[^sainz2023nlp-e1]. This overestimates the model's performance[^sainz2023nlp-e2]. The consequences depend on the degree of contamination: if the model has seen the evaluation set's annotations, the experiment is completely invalid; if it has seen only the training split, comparisons with models developed on the same data are unaffected, but claims about "zero-shot" (doing the task with no examples) or "few-shot" (with only a few examples) performance no longer hold[^sainz2023nlp-e3]. Once a good eval is published, its questions spread all over the internet[^wei2024evals-e9]; when you use a foundation model (a general-purpose model pretrained on large-scale data and then used for many downstream tasks), its training data may already include the test sets of community benchmarks[^lones2021avoid-e16].

What to do: for models with public training data, check what share of the benchmark can be found in the training data[^sainz2023nlp-e4]; for models without public training data, see whether the model can reproduce benchmark examples verbatim[^sainz2023nlp-e5]. When building an eval, prepare both a public and a private test set, and monitor whether a model performs very differently on the two[^wei2024evals-e9]. When reporting, say whether you checked for contamination and how; where possible, use data created after the model was trained `[Our analysis]`.

---

## 4. Checklist

This checklist is based mainly on the SIGSOFT benchmarking standard, supplemented with the SIGPLAN checklist and the recommendations of Heiser and of van der Kouwe et al.

**Essential**

- [ ] When using an existing benchmark, justify the choice; when building a new one, specify the quality measured, the metric, the measurement method, and the workload[^ralph2020empirical-e146][^ralph2020empirical-e147]
- [ ] The experimental environment and workload are described in enough detail for others to reproduce them independently[^ralph2020empirical-e148]
- [ ] The different configurations under test compete on their merits, without artificial handicaps[^ralph2020empirical-e149]
- [ ] Enough repetitions and long enough runs to assess the stability of the results[^ralph2020empirical-e150]
- [ ] Discuss construct validity: whether the benchmark measures what it is meant to[^ralph2020empirical-e100]
- [ ] Disclose the main limitations[^ralph2020empirical-e18]
- [ ] Give measures of variation (standard deviation or confidence intervals), state the method used to average across benchmarks, and state the hardware platform and software versions[^vanderkouwe2019sok-e21]
- [ ] Run the whole suite, or explain individually why any parts were not run; if you used a subset, don't report an overall score[^vanderkouwe2019sok-e17][^heiserbenchmarking-e4]

**Desirable**

- [ ] Provide supplementary material (datasets, analysis scripts, detailed documentation for a new benchmark), and provide the benchmark in a ready-to-use form[^ralph2020empirical-e151]
- [ ] Use or create open-source benchmarks; report honestly any problems encountered while running the benchmarks[^ralph2020empirical-e152]
- [ ] Report that the results have been independently reproduced, that the benchmark has a sizable user community, and that it is maintained by an independent organization[^ralph2020empirical-e153]

**Extraordinary**

- [ ] Provide empirical evidence of the benchmark's relevance (for example, a systematic review) and usability (for example, action research or a case study)[^ralph2020empirical-e154]

**Acceptable deviations (not flaws)**[^ralph2020empirical-e156]

- The benchmark requires special hardware (such as a quantum computer) that makes it hard for others to reproduce
- When replicating published work, the experimental environment may be described briefly
- When prior research has shown that a single run is enough, one or a few runs are acceptable

**Common but invalid reviewer criticisms**[^ralph2020empirical-e159]: you don't need to worry about these. A new benchmark doesn't have to be popular from the start; a "prototype benchmark" created by a small group of researchers can in itself spark discussion and start building consensus.

- "Few people use this benchmark"
- "No independent replication results are reported"
- "No independent organization maintains this benchmark"

---

## 5. Common mistakes

These mistakes are often called "benchmarking crimes": "crimes" because they undermine the integrity of the scientific process[^heiserbenchmarking-e1]. The table lists only those not already covered by the checklist.

| Mistake | Why it's a problem |
|---|---|
| Testing only scenarios that favor you, and not measuring costs | You can't see whether things got worse elsewhere[^heiserbenchmarking-e3][^vanderkouwe2019sok-e20] |
| Choosing only the parameter range that makes the system look good | That range doesn't represent real workloads[^heiserbenchmarking-e6] |
| Using microbenchmarks to stand for overall performance | They measure one operation and don't represent real workloads[^heiserbenchmarking-e7] |
| Using the same data for calibration and evaluation | The workloads for calibration and evaluation must not overlap at all[^heiserbenchmarking-e12] |
| Slowing down the baseline, or comparing only against your own earlier version | Overhead gets hidden in the baseline, or there is no recognized reference point[^vanderkouwe2019sok-e19][^heiserbenchmarking-e14] |
| Running only once, or reporting only the best run | You may mistake random variation for a real difference[^klees2018evaluating-e11][^georges2007statistically-e2] |
| Confusing percentages with percentage points, or using the wrong denominator | Doubled overhead gets described as a small increase[^heiserbenchmarking-e9][^vanderkouwe2019sok-e24] |
| Reporting only ratios, not absolute numbers | Readers can't sanity-check the results[^heiserbenchmarking-e19][^vanderkouwe2019sok-e23] |
| Keeping only aggregated numbers | You can't reanalyze or check them later[^ralph2020empirical-e158] |
| (Machine learning) Not checking whether the model has seen the test set | Data contamination overestimates performance and can even invalidate the experiment[^sainz2023nlp-e2][^sainz2023nlp-e3] |

---

## 6. Further reading

- **A list of mistakes you can check against directly**: Heiser's Systems Benchmarking Crimes web page, with examples for each item and, at the end, his rules of measurement practice for his students.
- **How common these mistakes are**: van der Kouwe et al. 2019, which organizes Heiser's list into 22 flaws, with survey data and the ones most worth fixing first. Other areas have similar surveys: Klees et al. examined 32 fuzzing papers and found problems in the evaluation of every one[^klees2018evaluating-e2]; Hoefler & Belli's survey of 120 papers from three top parallel computing conferences shows that the state of performance reporting is lacking[^hoefler2015scientific-e16].
- **A self-check list for evaluations**: the SIGPLAN Empirical Evaluation Checklist, one page, good for going through item by item before you submit.
- **Details of measurement and statistics**: Hoefler & Belli 2015's 12 rules (from parallel computing; most rules apply generally); Georges et al. 2007 (how to measure startup and steady-state performance); Kalibera & Jones 2013 (at which level to repeat, how many times, and how to report confidence intervals for effect sizes); Klees et al. 2018 (using fuzzing as the example: multiple runs of randomized tools, statistical tests, seeds, and timeouts).
- **Machine learning evaluation**: Lones's guide to common pitfalls in machine learning (fair comparison, problems with community benchmarks); Jason Wei's blog post on good evals; Sainz et al. 2023 on data contamination.
- **Measurement bias**: Mytkowicz et al. 2009; this page cites it only as reported by Kalibera & Jones.

Links to all sources are in the [source list](../../../../sources/README.md).

[^ralph2020empirical-e143]: SIGSOFT Benchmarking standard, Definition. [Evidence](../../../../sources/notes/ralph2020empirical.md#e143)
[^ralph2020empirical-e144]: SIGSOFT Benchmarking standard, Application. [Evidence](../../../../sources/notes/ralph2020empirical.md#e144)
[^ralph2020empirical-e145]: SIGSOFT Benchmarking standard, Application. [Evidence](../../../../sources/notes/ralph2020empirical.md#e145)
[^ralph2020empirical-e146]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e146)
[^ralph2020empirical-e147]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e147)
[^ralph2020empirical-e148]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e148)
[^ralph2020empirical-e149]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e149)
[^ralph2020empirical-e150]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e150)
[^ralph2020empirical-e100]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e151]: SIGSOFT Benchmarking standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e151)
[^ralph2020empirical-e152]: SIGSOFT Benchmarking standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e152)
[^ralph2020empirical-e153]: SIGSOFT Benchmarking standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e153)
[^ralph2020empirical-e154]: SIGSOFT Benchmarking standard, Extraordinary Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e154)
[^ralph2020empirical-e155]: SIGSOFT Benchmarking standard, General Quality Criteria. [Evidence](../../../../sources/notes/ralph2020empirical.md#e155)
[^ralph2020empirical-e156]: SIGSOFT Benchmarking standard, Acceptable Deviations. [Evidence](../../../../sources/notes/ralph2020empirical.md#e156)
[^ralph2020empirical-e157]: SIGSOFT Benchmarking standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e157)
[^ralph2020empirical-e158]: SIGSOFT Benchmarking standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e158)
[^ralph2020empirical-e159]: SIGSOFT Benchmarking standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e159)
[^ralph2020empirical-e160]: SIGSOFT Engineering Research standard, Definition and Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e160)
[^ralph2020empirical-e161]: SIGSOFT Engineering Research standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e161)
[^heiserbenchmarking-e1]: Heiser, Benchmarking Crimes, opening. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e1)
[^heiserbenchmarking-e2]: Heiser, Selective benchmarking. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e2)
[^heiserbenchmarking-e3]: Heiser, Not evaluating potential performance degradation. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e3)
[^heiserbenchmarking-e4]: Heiser, Benchmark sub-setting. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e4)
[^heiserbenchmarking-e5]: Heiser, Benchmark sub-setting. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e5)
[^heiserbenchmarking-e6]: Heiser, Selective data set hiding deficiencies. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e6)
[^heiserbenchmarking-e7]: Heiser, Pretending micro-benchmarks represent overall performance. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e7)
[^heiserbenchmarking-e8]: Heiser, Throughput degraded by x% ⇒ overhead is x%. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e8)
[^heiserbenchmarking-e9]: Heiser, Downplaying overheads. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e9)
[^heiserbenchmarking-e10]: Heiser, No indication of significance of data. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e10)
[^heiserbenchmarking-e11]: Heiser, Arithmetic mean for averaging across benchmark scores. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e11)
[^heiserbenchmarking-e12]: Heiser, Same dataset for calibration and validation. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e12)
[^heiserbenchmarking-e13]: Heiser, No proper baseline. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e13)
[^heiserbenchmarking-e14]: Heiser, Only evaluate against yourself. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e14)
[^heiserbenchmarking-e15]: Heiser, Unfair benchmarking of competitors. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e15)
[^heiserbenchmarking-e16]: Heiser, Inflating gains by not comparing against the state of the art. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e16)
[^heiserbenchmarking-e17]: Heiser, Missing specification of evaluation platform. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e17)
[^heiserbenchmarking-e18]: Heiser, Missing sub-benchmark results. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e18)
[^heiserbenchmarking-e19]: Heiser, Relative numbers only. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e19)
[^heiserbenchmarking-e20]: Heiser, Benchmarking Best Practice › General rules. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e20)
[^heiserbenchmarking-e21]: Heiser, Benchmarking Best Practice › Test data and results. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e21)
[^heiserbenchmarking-e22]: Heiser, Benchmarking Best Practice › Test data and results. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e22)
[^heiserbenchmarking-e23]: Heiser, Benchmarking Best Practice › Statistics. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e23)
[^heiserbenchmarking-e24]: Heiser, Benchmarking Best Practice › Timing. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e24)
[^heiserbenchmarking-e25]: Heiser, Benchmarking of simplified simulated system. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e25)
[^heiserbenchmarking-e26]: Heiser, Inappropriate and misleading benchmarks. [Evidence](../../../../sources/notes/heiserbenchmarking.md#e26)
[^blackburn2018sigplan-e15]: SIGPLAN checklist, Comparison is unfair. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e15)
[^blackburn2018sigplan-e16]: SIGPLAN checklist, Inappropriate suite. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e16)
[^blackburn2018sigplan-e17]: SIGPLAN checklist, Unjustified use of non-standard suite(s). [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e17)
[^blackburn2018sigplan-e18]: SIGPLAN checklist, Notes › Unjustified Use of Non-Standard Suite(s). [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e18)
[^blackburn2018sigplan-e19]: SIGPLAN checklist, Notes › Unjustified Use of Non-Standard Suite(s). [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e19)
[^blackburn2018sigplan-e20]: SIGPLAN checklist, Kernels instead of full applications. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e20)
[^blackburn2018sigplan-e21]: SIGPLAN checklist, Fails to measure all important effects. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e21)
[^blackburn2018sigplan-e22]: SIGPLAN checklist, Insufficient information to repeat. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e22)
[^blackburn2018sigplan-e23]: SIGPLAN checklist, Unreasonable platform. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e23)
[^blackburn2018sigplan-e24]: SIGPLAN checklist, Ignores key design parameters. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e24)
[^blackburn2018sigplan-e25]: SIGPLAN checklist, Gated workload generator. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e25)
[^blackburn2018sigplan-e27]: SIGPLAN checklist, Insufficient number of trials. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e27)
[^blackburn2018sigplan-e28]: SIGPLAN checklist, Notes › Inappropriate Summary Statistics. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e28)
[^blackburn2018sigplan-e29]: SIGPLAN checklist, Inappropriately truncated axes / Ratios plotted incorrectly. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e29)
[^blackburn2018sigplan-e30]: SIGPLAN checklist, Inappropriate level of precision. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e30)
[^blackburn2018sigplan-e31]: SIGPLAN checklist, FAQ › artifact evaluation. [Evidence](../../../../sources/notes/blackburn2018sigplan.md#e31)
[^vanderkouwe2019sok-e1]: van der Kouwe et al. 2019, Abstract. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e1)
[^vanderkouwe2019sok-e15]: van der Kouwe et al. 2019, §IV. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e15)
[^vanderkouwe2019sok-e16]: van der Kouwe et al. 2019, §II. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e16)
[^vanderkouwe2019sok-e11]: van der Kouwe et al. 2019, §VI. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e11)
[^vanderkouwe2019sok-e17]: van der Kouwe et al. 2019, §VI and §II-A. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e17)
[^vanderkouwe2019sok-e18]: van der Kouwe et al. 2019, §II-A. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e18)
[^vanderkouwe2019sok-e19]: van der Kouwe et al. 2019, §II-D and §VI. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e19)
[^vanderkouwe2019sok-e20]: van der Kouwe et al. 2019, §II-E. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e20)
[^vanderkouwe2019sok-e21]: van der Kouwe et al. 2019, §VI. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e21)
[^vanderkouwe2019sok-e22]: van der Kouwe et al. 2019, §II-B. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e22)
[^vanderkouwe2019sok-e23]: van der Kouwe et al. 2019, §II-F. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e23)
[^vanderkouwe2019sok-e24]: van der Kouwe et al. 2019, §II-B. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e24)
[^vanderkouwe2019sok-e25]: van der Kouwe et al. 2019, §I. [Evidence](../../../../sources/notes/vanderkouwe2019sok.md#e25)
[^klees2018evaluating-e10]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e10)
[^klees2018evaluating-e11]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e11)
[^klees2018evaluating-e12]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e12)
[^klees2018evaluating-e13]: Klees et al. 2018, §1. [Evidence](../../../../sources/notes/klees2018evaluating.md#e13)
[^klees2018evaluating-e14]: Klees et al. 2018, §4. [Evidence](../../../../sources/notes/klees2018evaluating.md#e14)
[^klees2018evaluating-e15]: Klees et al. 2018, §4. [Evidence](../../../../sources/notes/klees2018evaluating.md#e15)
[^klees2018evaluating-e16]: Klees et al. 2018, §9. [Evidence](../../../../sources/notes/klees2018evaluating.md#e16)
[^klees2018evaluating-e18]: Klees et al. 2018, §9. [Evidence](../../../../sources/notes/klees2018evaluating.md#e18)
[^hoefler2015scientific-e1]: Hoefler & Belli 2015, §1. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e1)
[^hoefler2015scientific-e2]: Hoefler & Belli 2015, Rule 1. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e2)
[^hoefler2015scientific-e3]: Hoefler & Belli 2015, Rule 2. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e3)
[^hoefler2015scientific-e4]: Hoefler & Belli 2015, Rules 3 and 4. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e4)
[^hoefler2015scientific-e5]: Hoefler & Belli 2015, Rule 5. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e5)
[^hoefler2015scientific-e6]: Hoefler & Belli 2015, Rule 6. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e6)
[^hoefler2015scientific-e7]: Hoefler & Belli 2015, Rule 7. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e7)
[^hoefler2015scientific-e8]: Hoefler & Belli 2015, Rule 8. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e8)
[^hoefler2015scientific-e9]: Hoefler & Belli 2015, Rule 9. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e9)
[^hoefler2015scientific-e10]: Hoefler & Belli 2015, §4.1.1. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e10)
[^hoefler2015scientific-e11]: Hoefler & Belli 2015, §4.1.2. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e11)
[^hoefler2015scientific-e12]: Hoefler & Belli 2015, §4.1.2. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e12)
[^hoefler2015scientific-e13]: Hoefler & Belli 2015, §4.2.1. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e13)
[^hoefler2015scientific-e14]: Hoefler & Belli 2015, Rule 11. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e14)
[^hoefler2015scientific-e15]: Hoefler & Belli 2015, Rule 12. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e15)
[^hoefler2015scientific-e16]: Hoefler & Belli 2015, Abstract. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e16)
[^hoefler2015scientific-e17]: Hoefler & Belli 2015, §4.2.2. [Evidence](../../../../sources/notes/hoefler2015scientific.md#e17)
[^georges2007statistically-e1]: Georges et al. 2007, §1. [Evidence](../../../../sources/notes/georges2007statistically.md#e1)
[^georges2007statistically-e2]: Georges et al. 2007, §1. [Evidence](../../../../sources/notes/georges2007statistically.md#e2)
[^georges2007statistically-e3]: Georges et al. 2007, §1. [Evidence](../../../../sources/notes/georges2007statistically.md#e3)
[^georges2007statistically-e4]: Georges et al. 2007, §1. [Evidence](../../../../sources/notes/georges2007statistically.md#e4)
[^kalibera2013rigorous-e1]: Kalibera & Jones 2013, §1. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e1)
[^kalibera2013rigorous-e2]: Kalibera & Jones 2013, §1. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e2)
[^kalibera2013rigorous-e3]: Kalibera & Jones 2013, §2 (summarizing Mytkowicz et al. 2009). [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e3)
[^kalibera2013rigorous-e4]: Kalibera & Jones 2013, §2. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e4)
[^kalibera2013rigorous-e5]: Kalibera & Jones 2013, §3. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e5)
[^kalibera2013rigorous-e6]: Kalibera & Jones 2013, §3. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e6)
[^kalibera2013rigorous-e7]: Kalibera & Jones 2013, §4. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e7)
[^kalibera2013rigorous-e8]: Kalibera & Jones 2013, §4. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e8)
[^kalibera2013rigorous-e9]: Kalibera & Jones 2013, §1. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e9)
[^kalibera2013rigorous-e10]: Kalibera & Jones 2013, §5. [Evidence](../../../../sources/notes/kalibera2013rigorous.md#e10)
[^wei2024evals-e1]: Wei 2024, para. 1. [Evidence](../../../../sources/notes/wei2024evals.md#e1)
[^wei2024evals-e2]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e2)
[^wei2024evals-e3]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e3)
[^wei2024evals-e4]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e4)
[^wei2024evals-e5]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e5)
[^wei2024evals-e6]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e6)
[^wei2024evals-e7]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e7)
[^wei2024evals-e8]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e8)
[^wei2024evals-e9]: Wei 2024, test set contamination. [Evidence](../../../../sources/notes/wei2024evals.md#e9)
[^wei2024evals-e10]: Wei 2024, pairwise human comparison. [Evidence](../../../../sources/notes/wei2024evals.md#e10)
[^wei2024evals-e11]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e11)
[^wei2024evals-e12]: Wei 2024. [Evidence](../../../../sources/notes/wei2024evals.md#e12)
[^lones2021avoid-e15]: Lones, §5.5. [Evidence](../../../../sources/notes/lones2021avoid.md#e15)
[^lones2021avoid-e16]: Lones, §5.5. [Evidence](../../../../sources/notes/lones2021avoid.md#e16)
[^lones2021avoid-e17]: Lones, §6.2. [Evidence](../../../../sources/notes/lones2021avoid.md#e17)
[^sainz2023nlp-e1]: Sainz et al. 2023, Abstract. [Evidence](../../../../sources/notes/sainz2023nlp.md#e1)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e3]: Sainz et al. 2023, §3. [Evidence](../../../../sources/notes/sainz2023nlp.md#e3)
[^sainz2023nlp-e4]: Sainz et al. 2023, §5.1. [Evidence](../../../../sources/notes/sainz2023nlp.md#e4)
[^sainz2023nlp-e5]: Sainz et al. 2023, §5.2. [Evidence](../../../../sources/notes/sainz2023nlp.md#e5)
[^ralph2020empirical-e18]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e18)
[^klees2018evaluating-e2]: Klees et al. 2018, Abstract. [Evidence](../../../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e4]: Klees et al. 2018, §9. [Evidence](../../../../sources/notes/klees2018evaluating.md#e4)
[^klees2018evaluating-e7]: Klees et al. 2018, §8. [Evidence](../../../../sources/notes/klees2018evaluating.md#e7)
