# Optimization studies: formulate the problem as optimization and solve it by search

This page covers **optimization studies**: you formulate a computing problem as "find the best among many candidate solutions", solve it with optimization techniques such as search or evolutionary algorithms, and show experimentally how well the solving works. **Search-Based Software Engineering** (SBSE), for example automatically generating test cases, is the typical case in software engineering.

**Scope** `[Our analysis]`: this is how it is done in computer science; the examples and standards come mainly from search-based software engineering. When you propose a new search method, the work belongs to the [Building and improving](../../../05_research-strategies/build_improve.md) research strategy; when you compare several algorithms to see which is better, it belongs to [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md). The parts of these strategies that hold in every field (what evidence you need, how to compare fairly) are on the strategy pages; this page covers only what is specific to optimization studies.

An optimization study is often also a piece of [Engineering research](engineering_research.md) (you propose a new method), and its evaluation also looks like a [Benchmarking](benchmarking.md) study. "How to configure competitors fairly and how to control the measurement environment" is covered under benchmarking; the basic ideas of significance testing and effect size are in [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

**After reading this page, you should be able to:**

- write your problem as a clear optimization problem: how solutions are represented, how they are scored, and what the constraints are;
- choose suitable baselines, including at least random search;
- deal with the algorithm's randomness: run it repeatedly and compare with the Mann-Whitney U test and the Â12 effect size;
- set parameters and search budgets fairly and report them clearly;
- check your own study against the checklist at the end.

---

## 1. What this kind of research is, and when to use it

The ACM SIGSOFT Empirical Standards (from the Association for Computing Machinery's Special Interest Group on Software Engineering) define it this way: an optimization study formulates a problem as a search problem and solves it with optimization techniques[^ralph2020empirical-e374]. It has two ingredients:

- **Fitness function** (also called the objective function): a numeric function that scores each candidate solution; the score says how good the solution is[^ralph2020empirical-e375]. For test case generation, the score might be how many code branches are covered.
- **Solution method**: an algorithm that pushes this score as high (or as low) as possible, such as a metaheuristic (genetic algorithms, simulated annealing, and so on), a numerical optimizer, or a constraint solver. Some of these are stochastic[^ralph2020empirical-e376].

The standard was written for software engineering, but the same idea is common across computing, for example automatic tuning of compiler flags, cluster job scheduling, and hyperparameter search in machine learning `[Our analysis]`.

**How it differs from similar kinds of study** `[Our analysis]`:

| | Optimization study | Benchmarking | Quantitative simulation |
|---|---|---|---|
| Core question | Can we find better solutions? Which search method works better? | How do existing systems perform under a given workload? | What would happen if the system ran this way? |
| Main output | A formulation of the problem, a solution method, and how well they work | Comparison results across systems | Inferences about system behavior |
| Typical example | Using a genetic algorithm to generate test cases with higher branch coverage | Comparing the throughput of several databases | Simulating cluster throughput under different scheduling policies |

**When to use it**: optimization is worth it only when there are too many candidate solutions for people to handle manually in reasonable time, or too many combinations to enumerate. The standard lists "explain why the problem cannot be solved manually or by exhaustive search in reasonable time" as the first essential item[^ralph2020empirical-e377].

---

## 2. How to do it

### Step 1: Formulate the problem clearly

**How:** write down four things[^ralph2020empirical-e378][^ralph2020empirical-e381]:

1. **What a solution is**: what one solution stands for, for example a test suite.
2. **How a solution is represented and changed**: which data structure represents it (such as a vector or a tree), and how the algorithm modifies it (such as crossover and mutation).
3. **The fitness function**: which objective you optimize, and the formula for computing it.
4. **The search space and constraints**: what the variables are, what values each can take, and what constraints apply.

**Why:** the formulation decides what the algorithm can find. If readers can't see your formulation, they can't tell whether the results come from a good algorithm or from a clever (or excessive) simplification of the problem `[Our analysis]`.

**Where people go wrong:**

- **Oversimplifying.** Simplifications and constraints should be realistic and modest; if you simplify the problem until every solution can be enumerated, you no longer need optimization[^ralph2020empirical-e378].
- **An unrealistic option space.** Attribute values should be ones that could occur in reality, not drawn from an arbitrary distribution[^ralph2020empirical-e386].
- **Forcing several objectives into one score.** When you have several conflicting objectives (such as coverage and test duration), simply combining them into one weighted score hides the trade-offs between them `[Our analysis]`. The SIGSOFT standards point out that when evaluating multi-objective methods, what matters more is the Pareto front (a set of solutions in which none can be improved on one objective without getting worse on another) and the corresponding quality indicators[^ralph2020empirical-e395].

### Step 2: Choose the algorithm and the baselines

**How:**

1. **Explain why you chose this algorithm.** For a new problem, few people know which algorithm is best; but at least draw on algorithms used for similar problems and make an informed judgment[^ralph2020empirical-e379].
2. **Always compare against random search.** Random search simply keeps generating random solutions and keeps the best one `[Our analysis]`. For a new problem, compare at least against random search; for a problem others have already tackled, compare against the current state of the art[^ralph2020empirical-e380].
3. **Also compare against simpler methods.** A method that looks sophisticated should be compared against simpler alternatives[^menzies2019bad-e7].

**Why compare against random search**: it is the only way to confirm that success is not because the problem (or the instances you picked) is simply too easy[^arcuri2014hitchhiker-e4]. Arcuri & Briand give an example: an award-winning paper at ICSE 2009 (the International Conference on Software Engineering) used genetic programming (a kind of evolutionary algorithm) to generate patches that fix bugs, with only 400 fitness evaluations per run in total (a population of 40 over 10 generations); on half of the subjects, on average, a suitable patch was already found when the first generation was randomly generated, before the evolutionary search had really started[^arcuri2014hitchhiker-e3].

### Step 3: Set parameters and budgets fairly

**How:**

1. **State every parameter of every method and its value**, such as population size, crossover rate, and mutation rate[^ralph2020empirical-e382], and explain why you set them that way[^ralph2020empirical-e387].
2. **Tune everyone equally.** Carefully tuning your own method while leaving competitors on default settings is particularly bad practice: such a comparison only shows that "a well-tuned new method beats a badly tuned other method"[^menzies2019bad-e5][^menzies2019bad-e6]. How to tune everyone equally is in [Step 3](benchmarking.md#step-3-choose-the-systems-to-compare-and-configure-each-one-fairly) of the benchmarking page.
3. **Give every method the same search budget**, such as the same number of fitness evaluations or the same running time, and state it in the paper `[Our analysis]`. The 400-evaluation example above shows that readers need to know how big the budget was to judge how much the search actually contributed[^arcuri2014hitchhiker-e3].
4. **Report costs.** When choosing an algorithm in practice, besides effectiveness and p-values you also need to look at differences in cost, such as execution time and how much input the user must provide[^arcuri2014hitchhiker-e6].
5. **Preferably don't use the problem instances you tuned on for the final evaluation as well.** Otherwise the parameters may just happen to suit those instances `[Our analysis]`; the reasoning is the same as the rule in [Building and improving](../../../05_research-strategies/build_improve.md#effects-on-later-stages) that examples consulted during development can't be reused for evaluation.

Going further, you can systematically analyze the effect of different parameter choices and explain how the final parameters were selected; the standard lists this as Extraordinary[^ralph2020empirical-e390].

### Step 4: Run repeatedly to deal with randomness

A stochastic algorithm run twice on the same problem instance may give different results[^arcuri2014hitchhiker-e1]. Arcuri & Briand's systematic review of papers from 2009 to 2010 found that empirical analyses involving randomized algorithms in software engineering, overall, often did not handle this properly[^arcuri2014hitchhiker-e2].

**How:**

1. **Identify every source of randomness**: randomness in the algorithm itself; fitness functions that measure random quantities in the environment (for example, scoring by execution time, which differs every time you measure it); and data sampling or cross-validation[^ralph2020empirical-e384].
2. **Run each method independently many times**, so you get a distribution of results rather than a single number[^arcuri2014hitchhiker-e5][^ralph2020empirical-e384].
3. **Record the random seeds.** Without the seeds, nobody can reproduce your results exactly[^menzies2019bad-e8]. How fixing seeds relates to repeating with different seeds is covered in [Comparative evaluation: is the difference real?](../../../05_research-strategies/compare_evaluate.md#is-the-difference-real).
4. **State how many runs you did and which statistical tests you used**[^arcuri2014hitchhiker-e12].

> **Where sources disagree: how many runs?**
> - Arcuri & Briand recommend at least 1000 runs of each algorithm on each problem instance; if you can't, explain why and report how long the whole experiment took. Their reasoning is that for most software engineering problems, a few thousand runs is feasible[^arcuri2014hitchhiker-e13][^arcuri2014hitchhiker-e9]. They also acknowledge there will be exceptions; deviating is fine as long as you justify it[^arcuri2014hitchhiker-e20].
> - The SIGSOFT standards set no number: when experiments are very time-consuming or involve people, a limited number of runs is acceptable, but you must disclose the limitation and discuss the effect of randomness[^ralph2020empirical-e391].
>
> In practice: first estimate how long one run takes. If you can afford more runs, do more; if you can't, honestly report the number of runs, the total time, and your reasons `[Our analysis]`. If you have many problem instances and limited time, Arcuri & Briand suggest doing fewer runs per instance (at least 10) and using more instances[^arcuri2014hitchhiker-e14].

### Step 5: Compare with appropriate statistics

**How:** for each pair of methods on each problem instance, report two things together[^arcuri2014hitchhiker-e16][^arcuri2014hitchhiker-e18]:

**1. Mann-Whitney U test: is the difference due to chance?**

Arcuri & Briand recommend a two-tailed Mann-Whitney U test for numeric results (such as coverage), and Fisher's exact test (a test comparing the number of successes in two groups) for binary found/not-found results[^arcuri2014hitchhiker-e16].

In plain terms `[Our analysis]`: pool the runs from A and B, sort them from smallest to largest, and see whether one group systematically ranks higher. It looks only at ranks and does not require the results to be normally distributed. That matters, because the results of search algorithms are often highly skewed[^arcuri2014hitchhiker-e7].

Report every p-value, whether or not it falls below the significance level, rather than just saying "significant"[^arcuri2014hitchhiker-e17].

**2. Vargha-Delaney Â12 effect size: how much better is A than B?**

Â12 is the probability that one random run of A gives a higher result than one random run of B. When the two are equivalent, Â12 = 0.5; Â12 = 0.7 means A gives the higher result 70% of the time[^arcuri2014hitchhiker-e8].

Example `[Our analysis]`: suppose three runs of A give {42, 11, 7} and three runs of B give {1, 20, 5}. Pair each result of A with each result of B: 3 × 3 = 9 pairs. A is higher in 7 pairs (42 wins 3 pairs, 11 and 7 win 2 each, both losing to 20), with no ties, so Â12 = 7/9 ≈ 0.78 (each tie would count as half a pair). Watch the direction: when lower is better for the metric (such as running time), A is better only when Â12 is below 0.5 `[Our analysis]`.

**Why you need both**: a significance test answers "can we tell them apart?"; an effect size answers "is the difference big enough to care about?"[^ralph2020empirical-e396]. With thousands of runs, almost any difference becomes significant[^arcuri2014hitchhiker-e9], so reporting only the test and not the effect size is an antipattern listed in the standard[^ralph2020empirical-e392]. Match the effect size to the test: with a rank-based test, use a rank-based effect size (such as Â12), not "difference in means divided by standard deviation"[^arcuri2014hitchhiker-e10][^arcuri2014hitchhiker-e7].

**Also:**

- **Report the whole distribution, not just the mean or median**, for example with box plots[^ralph2020empirical-e388][^ralph2020empirical-e392].
- **Give confidence intervals for effect sizes**, for example with the bootstrap (estimating uncertainty by repeatedly resampling, with replacement, from the results you have)[^arcuri2014hitchhiker-e18].
- **When comparing more than two methods, compare them pairwise**, with a test and an effect size for every pair[^arcuri2014hitchhiker-e19]; whether to correct for multiple comparisons when there are many is covered in [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 6: Choose problem instances and see how far results generalize

**How:**

1. **Explain how the instances were chosen.** Which programs and datasets you pick strongly affects the results[^arcuri2014hitchhiker-e11]. It is hard to get a large, unbiased, representative set of instances, but you must say how yours were selected[^arcuri2014hitchhiker-e15][^ralph2020empirical-e385].
2. **Describe the instances' characteristics and "difficulty"**, and discuss what makes each one hard[^ralph2020empirical-e385].
3. **If you use synthetic data, justify it**: why real data couldn't be used, and how far the conclusions apply to reality[^ralph2020empirical-e386].
4. **Report each instance separately, not just an overall average.** Arcuri & Briand's example: Â12 values of 0.6, 0.6, 0.6, 0.6, and 0.1 on five instances average to 0.5, which looks like "no difference"; in fact one method is better on four instances and much worse on one. Report them separately and try to explain the differences[^arcuri2014hitchhiker-e21].

### Step 7: Report and release

- Release the data, or explain why you can't (for example, a non-disclosure agreement)[^ralph2020empirical-e383].
- Provide a replication package: source code for the method, the solution representation, and the fitness computation; the experimental input data; and the output logs and generated solutions[^ralph2020empirical-e389].
- In the results section, write only results backed by evidence; put interpretation and speculation in the discussion[^ralph2020empirical-e388].

---

## 3. Checklist

This checklist follows mainly the SIGSOFT optimization studies standard.

**Essential**

- [ ] Explain why the problem can't be solved manually or by exhaustive search in reasonable time[^ralph2020empirical-e377]
- [ ] Describe the search space; simplifications and constraints are realistic and don't reduce the problem to one you could enumerate[^ralph2020empirical-e378]
- [ ] Clearly define what a solution means, how it is represented and modified, and all fitness functions[^ralph2020empirical-e381]
- [ ] Explain why you chose this algorithm[^ralph2020empirical-e379]
- [ ] Compare against reasonable baselines: for a new problem at least random search, otherwise the state of the art[^ralph2020empirical-e380]
- [ ] State each method's techniques, heuristics, parameters, and parameter values[^ralph2020empirical-e382]
- [ ] Explain how the datasets were collected and prepared; release the data or explain why not[^ralph2020empirical-e383]
- [ ] Identify every source of randomness; run stochastic methods many times, or explain why you couldn't[^ralph2020empirical-e384]

**Desirable**

- [ ] Explain how instances were chosen; describe their characteristics and difficulty[^ralph2020empirical-e385]
- [ ] Justify the parameter values[^ralph2020empirical-e387]
- [ ] Compare distributions with appropriate statistics, not just means[^ralph2020empirical-e388]
- [ ] Separate evidence-backed results from speculation[^ralph2020empirical-e388]
- [ ] Provide a replication package[^ralph2020empirical-e389]

**Extraordinary**

- [ ] Analyze the effect of different parameter choices and explain how the final parameters were selected[^ralph2020empirical-e390]
- [ ] Analyze the fitness landscape (how good and bad solutions are distributed across the solution space)[^ralph2020empirical-e390]

**Acceptable deviations (not flaws)**

- Running only a limited number of trials when experiments are very time-consuming or involve people, provided you disclose the limitation and discuss the effect of randomness[^ralph2020empirical-e391]

**Common but invalid reviewer criticisms**: you don't need to worry about these

- "Only uses old algorithms": an old algorithm can serve as one of many comparison methods, as a performance "floor", or as an experimental platform in which you change one thing and keep everything else the same[^ralph2020empirical-e393]
- "Didn't compare against method X", when that method is unsuitable or no usable implementation is available[^ralph2020empirical-e394]
- "The multi-objective method wasn't compared against optimizing each objective separately"[^ralph2020empirical-e394]
- "Too few subjects", when the paper gives a reasonable justification[^ralph2020empirical-e394]

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Not comparing against random search | You can't rule out "the problem itself is too easy"[^arcuri2014hitchhiker-e4] |
| Not reporting the search budget | Readers can't judge how much the search actually contributed[^arcuri2014hitchhiker-e3] |
| Tuning your own method but leaving competitors on default parameters | It only shows that "a well-tuned A beats a badly tuned B"[^menzies2019bad-e6] |
| Running a stochastic method only once | The result may just be luck[^arcuri2014hitchhiker-e1][^ralph2020empirical-e384] |
| Reporting only significance tests, not effect sizes | With many runs almost everything is significant, and you can't see how big the difference is[^ralph2020empirical-e392][^arcuri2014hitchhiker-e9] |
| Reporting only means or medians, with no spread | It hides the variation between trials[^ralph2020empirical-e392] |
| Using "difference in means divided by standard deviation" as the effect size for skewed results | That effect size breaks down when distributions are skewed[^arcuri2014hitchhiker-e7] |
| Reporting only the average effect size across all instances | It can hide cases where a method is much worse on particular instances[^arcuri2014hitchhiker-e21] |
| Not explaining how instances were chosen | Readers can't judge how far the results generalize[^arcuri2014hitchhiker-e15] |

---

## 5. Further reading

- **ACM SIGSOFT Empirical Standards, Optimization Studies**: the checklist for optimization studies, including the criticisms that are not valid in review. The original is in the submodule `repos/acmsigsoft__EmpiricalStandards/docs/standards/OptimizationStudies.md`.
- **Arcuri & Briand 2014, "A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms in Software Engineering"**: a detailed guide to comparing randomized algorithms: number of runs, tests, effect sizes, and analysis across multiple subjects. Section 11 contains practical recommendations you can follow directly. An author-archived version is in the University of Luxembourg's institutional repository. It is the extended version of the ICSE 2011 paper `arcuri2011practical`.
- **Menzies & Shepperd 2019, "'Bad smells' in software analytics papers"**: common problems in data-driven research, including not tuning and not comparing against simple methods.
- Related practices in the computer science section: [Benchmarking](benchmarking.md) (fair configuration, measurement procedure) and [Engineering research](engineering_research.md) (proposing and evaluating a new method).

[^ralph2020empirical-e374]: SIGSOFT Optimization Studies standard, Definition and Application. [Evidence](../../../../sources/notes/ralph2020empirical.md#e374)
[^ralph2020empirical-e375]: SIGSOFT Optimization Studies standard, footnote 3. [Evidence](../../../../sources/notes/ralph2020empirical.md#e375)
[^ralph2020empirical-e376]: SIGSOFT Optimization Studies standard, footnote 1. [Evidence](../../../../sources/notes/ralph2020empirical.md#e376)
[^ralph2020empirical-e377]: SIGSOFT Optimization Studies standard, Essential Attributes and footnote 4. [Evidence](../../../../sources/notes/ralph2020empirical.md#e377)
[^ralph2020empirical-e378]: SIGSOFT Optimization Studies standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e378)
[^ralph2020empirical-e379]: SIGSOFT Optimization Studies standard, Essential Attributes and footnote 6. [Evidence](../../../../sources/notes/ralph2020empirical.md#e379)
[^ralph2020empirical-e380]: SIGSOFT Optimization Studies standard, Essential Attributes and footnote 7. [Evidence](../../../../sources/notes/ralph2020empirical.md#e380)
[^ralph2020empirical-e381]: SIGSOFT Optimization Studies standard, Essential Attributes and footnotes 8 and 9. [Evidence](../../../../sources/notes/ralph2020empirical.md#e381)
[^ralph2020empirical-e382]: SIGSOFT Optimization Studies standard, Essential Attributes and footnote 10. [Evidence](../../../../sources/notes/ralph2020empirical.md#e382)
[^ralph2020empirical-e383]: SIGSOFT Optimization Studies standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e383)
[^ralph2020empirical-e384]: SIGSOFT Optimization Studies standard, Essential Attributes and footnotes 12 and 13. [Evidence](../../../../sources/notes/ralph2020empirical.md#e384)
[^ralph2020empirical-e385]: SIGSOFT Optimization Studies standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e385)
[^ralph2020empirical-e386]: SIGSOFT Optimization Studies standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e386)
[^ralph2020empirical-e387]: SIGSOFT Optimization Studies standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e387)
[^ralph2020empirical-e388]: SIGSOFT Optimization Studies standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e388)
[^ralph2020empirical-e389]: SIGSOFT Optimization Studies standard, Desirable Attributes and footnote 14. [Evidence](../../../../sources/notes/ralph2020empirical.md#e389)
[^ralph2020empirical-e390]: SIGSOFT Optimization Studies standard, Extraordinary Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e390)
[^ralph2020empirical-e391]: SIGSOFT Optimization Studies standard, Acceptable Deviations. [Evidence](../../../../sources/notes/ralph2020empirical.md#e391)
[^ralph2020empirical-e392]: SIGSOFT Optimization Studies standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e392)
[^ralph2020empirical-e393]: SIGSOFT Optimization Studies standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e393)
[^ralph2020empirical-e394]: SIGSOFT Optimization Studies standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e394)
[^ralph2020empirical-e395]: SIGSOFT Optimization Studies standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e395)
[^ralph2020empirical-e396]: SIGSOFT Optimization Studies standard, Notes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e396)
[^arcuri2014hitchhiker-e1]: Arcuri & Briand 2014, §1. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e1)
[^arcuri2014hitchhiker-e2]: Arcuri & Briand 2014, Abstract. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e2)
[^arcuri2014hitchhiker-e3]: Arcuri & Briand 2014, §3. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e3)
[^arcuri2014hitchhiker-e4]: Arcuri & Briand 2014, §3. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e4)
[^arcuri2014hitchhiker-e5]: Arcuri & Briand 2014, §4. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e5)
[^arcuri2014hitchhiker-e6]: Arcuri & Briand 2014, §4. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e6)
[^arcuri2014hitchhiker-e7]: Arcuri & Briand 2014, §7. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e7)
[^arcuri2014hitchhiker-e8]: Arcuri & Briand 2014, §7. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e8)
[^arcuri2014hitchhiker-e9]: Arcuri & Briand 2014, §8. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e9)
[^arcuri2014hitchhiker-e10]: Arcuri & Briand 2014, §8. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e10)
[^arcuri2014hitchhiker-e11]: Arcuri & Briand 2014, §10.1. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e11)
[^arcuri2014hitchhiker-e12]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e12)
[^arcuri2014hitchhiker-e13]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e13)
[^arcuri2014hitchhiker-e14]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e14)
[^arcuri2014hitchhiker-e15]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e15)
[^arcuri2014hitchhiker-e16]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e16)
[^arcuri2014hitchhiker-e17]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e17)
[^arcuri2014hitchhiker-e18]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e18)
[^arcuri2014hitchhiker-e19]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e19)
[^arcuri2014hitchhiker-e20]: Arcuri & Briand 2014, §11. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e20)
[^arcuri2014hitchhiker-e21]: Arcuri & Briand 2014, §10.2. [Evidence](../../../../sources/notes/arcuri2014hitchhiker.md#e21)
[^menzies2019bad-e5]: Menzies & Shepperd 2019, §4.10. [Evidence](../../../../sources/notes/menzies2019bad.md#e5)
[^menzies2019bad-e6]: Menzies & Shepperd 2019, §4.10. [Evidence](../../../../sources/notes/menzies2019bad.md#e6)
[^menzies2019bad-e7]: Menzies & Shepperd 2019, §4.11. [Evidence](../../../../sources/notes/menzies2019bad.md#e7)
[^menzies2019bad-e8]: Menzies & Shepperd 2019, §4.4. [Evidence](../../../../sources/notes/menzies2019bad.md#e8)
