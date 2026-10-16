# Arcuri & Briand 2014: A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms in Software Engineering

- Source: `arcuri2014hitchhiker`, [author archive copy (University of Luxembourg repository ORBilu)](https://orbilu.uni.lu/bitstream/10993/1071/1/paper_stvr_icse_2012.pdf)
- Version: Author's accepted manuscript, published in Software Testing, Verification and Reliability 24(3), 2014. Extended version of the ICSE 2011 paper `arcuri2011practical`. Section numbers follow the original; the original PDF has review line numbers, which are removed from the excerpts.

### E1

- Location: §1 Introduction
- Quote: "At a high level, a randomized algorithm is an algorithm that has one or more of its components based on randomness. Therefore, running twice the same randomized algorithm on the same problem instance may yield different results."
- Key point: A randomized algorithm has one or more components based on randomness, so running the same algorithm twice on the same problem instance can give different results.

### E2

- Location: abstract
- Quote: "This paper features a systematic review regarding recent publications in 2009 and 2010 showing that, overall, empirical analyses involving randomized algorithms in software engineering tend to not properly account for the random nature of these algorithms."
- Key point: The authors' systematic review of 2009-2010 papers shows that empirical analyses of randomized algorithms in software engineering generally do not properly account for their random nature.

### E3

- Location: §3 (discussion of the systematic review results)
- Quote: "in the award winning paper at ICSE 2009, a search algorithm (i.e., Genetic Programming) was used and was run 100 times on each artifact in the case study" / "the total number of ﬁtness evaluations was 400 (a population size of 40 individuals that is evolved for 10 generations). This sounds like a very low number" / "in half of the subject artifacts in the case study, the average number of ﬁtness evaluations per run is at most 41, thus implying that, on average, appropriate patches are found in the random initialization of the ﬁrst population before the actual evolutionary search even starts."
- Key point: A cautionary example: in an award-winning ICSE 2009 paper on automated bug repair, genetic programming used only 400 fitness evaluations in total; for half the subjects a suitable patch was found already in the randomly generated first population, before any evolutionary search took place. This shows why the search budget must be reported and why comparison with random search is needed.

### E4

- Location: §3
- Quote: "a search algorithm should always be compared against at least random search in order to check that success is not due to the search problem (or case study) being easy."
- Key point: A search algorithm should always be compared at least against random search, to check that success is not due to the problem (or chosen case study) being easy.

### E5

- Location: §4 Statistical Difference
- Quote: "To enable statistical analysis, one should run both A and B a large enough number (n) of times, in an independent way, to collect information on the probability distribution of M for each algorithm."
- Key point: For statistical analysis, run both algorithms independently a large enough number of times to learn the probability distribution of each one's performance measure.

### E6

- Location: §4 Statistical Difference
- Quote: "The focus of such experiments should rather be on whether a given technique brings any practically signiﬁcant advantage, usually measured in terms of an estimated effect size and its conﬁdence interval" / "In practice, the selection of an algorithm would depend on the p-value of effectiveness comparisons, the effectiveness effect size, and the cost difference among algorithms (e.g., in terms of user-provided inputs or execution time)."
- Key point: Experiments should focus on whether the new technique brings a practically significant advantage, measured by an estimated effect size and its confidence interval; choosing an algorithm in practice also depends on the p-value and on cost differences (e.g., required user input, execution time).

### E7

- Location: §7 Effect Size
- Quote: "But for distributions with high skewness (as in the geometric distribution and as it is often the case for search algorithms), the results of scaling the mean difference by the standard deviation “would not be valid”" / "In this case, a non-parametric effect size should be preferred."
- Key point: Search algorithm results are often highly skewed; then effect sizes that scale the mean difference by the standard deviation (the d family) are not valid, and a non-parametric effect size should be preferred.

### E8

- Location: §7 Effect Size
- Quote: "given a performance measure M , Aˆ12 measures the probability that running algorithm A yields higher M values than running another algorithm B. If the two algorithms are equivalent, then Aˆ12 = 0.5." / "For example, Aˆ12 = 0.7 entails one would obtain better results 70% of the time with A."
- Key point: Vargha-Delaney Â12 measures the probability that running A yields a higher value of the measure than running B; 0.5 means the two are equivalent, and 0.7 means A gives better results 70% of the time.

### E9

- Location: §8 Number of Runs
- Quote: "For most problems in software engineering, thousands of randomized algorithm runs should be feasible" / "However, with thousands of runs, one would detect statistically signiﬁcant differences on practically any experiment (Section 4). It is hence essential to complement such analyses with a study of the effect size"
- Key point: For most software engineering problems thousands of runs are feasible, but with thousands of runs almost any difference is statistically significant, so effect sizes must be analyzed as well.

### E10

- Location: §8 Number of Runs
- Quote: "In other words, it is advisable to use size measures that are consistent with the differences being tested by the selected statistical test."
- Key point: Use effect sizes consistent with what the chosen test compares (e.g., a rank-based effect size with a rank test).

### E11

- Location: §10.1 Choice of the Artifacts
- Quote: "When assessing randomized algorithms, the choice of artifacts to which these algorithms are applied (e.g., source code or executable programs) is of paramount importance as it usually has a strong bearing on the evaluation results."
- Key point: The choice of artifacts (e.g., programs) the algorithms are applied to is of paramount importance, as it strongly affects the evaluation results.

### E12

- Location: §11 Practical Guidelines
- Quote: "When randomized algorithms are analyzed, clearly specify the number of runs and employed statistical tests."
- Key point: When analyzing randomized algorithms, clearly state the number of runs and the statistical tests used.

### E13

- Location: §11 Practical Guidelines
- Quote: "On each artifact in the case study, run each randomized algorithm at least n = 1,000 times. If this is not possible, explain the reasons and report the total amount of time it took to run the entire case study."
- Key point: The authors recommend running each algorithm at least 1,000 times on each artifact; if that is not possible, explain why and report how long the whole case study took.

### E14

- Location: §11 Practical Guidelines
- Quote: "it is advisable to execute less runs per artifact (though at least n = 10) and use more artifacts (rather than having n = 1,000 but only few artifacts, see Section 10.1). The objective is to strike a balance between generalization and statistical power."
- Key point: When many artifacts are available but time is limited, run fewer times per artifact (at least 10) on more artifacts, balancing generalization against statistical power.

### E15

- Location: §11 Practical Guidelines
- Quote: "Even if obtaining such artifacts is usually not possible, it is important to always clarify how they were chosen."
- Key point: Large sets of unbiased, representative artifacts are hard to obtain, but always explain how yours were chosen.

### E16

- Location: §11 Practical Guidelines
- Quote: "For detecting statistical differences, use the two-tailed non-parametric Mann-Whitney U-test for interval-scale results and the Fisher exact test for dichotomous results"
- Key point: To detect differences, use the two-tailed non-parametric Mann-Whitney U-test for interval-scale results and the Fisher exact test for dichotomous (success/failure) results.

### E17

- Location: §11 Practical Guidelines
- Quote: "Report all the obtained p-values, whether they are smaller than α or not, and not just whether differences are signiﬁcant."
- Key point: Report all p-values, whether or not they are below the significance level, not just whether differences are "significant."

### E18

- Location: §11 Practical Guidelines
- Quote: "Always report standardized effect size measures." / "It is also strongly advised to report effect size conﬁdence intervals, e.g., by using a bootstrapping technique."
- Key point: Always report standardized effect sizes, and preferably their confidence intervals (e.g., computed by bootstrapping).

### E19

- Location: §11 Practical Guidelines
- Quote: "When analyzing more than two randomized algorithms, use pairwise comparisons including pairwise statistical tests and effect size measures."
- Key point: When comparing more than two algorithms, use pairwise comparisons, with a statistical test and an effect size for each pair.

### E20

- Location: §11 Practical Guidelines
- Quote: "Though one would expect exceptions, given the current state of practice [...] the authors of this paper believe that it is important to provide practical guidance that will be valid in most cases and enable higher quality studies to be reported. It is recommendable that practitioners follow these guidelines and justify any necessary deviation."
- Key point: The authors expect exceptions; the guidelines target most cases, and deviations from them should be justified.

### E21

- Location: §10.2 Analysis of Multiple Artifacts
- Quote: "Consider a case with ﬁve artifacts and the following Aˆ12 measures {0.6, 0.6, 0.6, 0.6, 0.1}." / "If one averages those values on the entire case study, he would obtain Aˆ12 = 0.5, thus suggesting there is no difference among the two algorithms!" / "In general, researchers should report the performance of the algorithms on each problem instance separately and attempt, as discussed above, to explain differences."
- Key point: With Â12 values of 0.6, 0.6, 0.6, 0.6, and 0.1 on five artifacts, the average is 0.5 and suggests "no difference," yet one algorithm is better on four artifacts and much worse on one. In general, report performance on each problem instance separately and try to explain the differences.
