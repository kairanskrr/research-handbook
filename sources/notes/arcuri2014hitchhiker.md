# Arcuri & Briand 2014：A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms in Software Engineering

- 资料：`arcuri2014hitchhiker`，[作者存档版（卢森堡大学机构库 ORBilu）](https://orbilu.uni.lu/bitstream/10993/1071/1/paper_stvr_icse_2012.pdf)
- 版本：作者接受稿，正式发表于 Software Testing, Verification and Reliability 24(3), 2014。是 ICSE 2011 论文 `arcuri2011practical` 的扩展版。章节号按原文；原文 PDF 带审稿用行号，摘录已去掉。

### E1

- 位置：§1 Introduction
- 原文："At a high level, a randomized algorithm is an algorithm that has one or more of its components based on randomness. Therefore, running twice the same randomized algorithm on the same problem instance may yield different results."
- 要点：随机化算法是有一个或多个部分依赖随机性的算法；同一个算法在同一个问题实例上跑两次，结果可能不同。

### E2

- 位置：摘要
- 原文："This paper features a systematic review regarding recent publications in 2009 and 2010 showing that, overall, empirical analyses involving randomized algorithms in software engineering tend to not properly account for the random nature of these algorithms."
- 要点：作者对 2009—2010 年论文的系统综述显示，软件工程中涉及随机化算法的实证分析，总体上没有恰当处理算法的随机性。

### E3

- 位置：§3（系统综述结果的讨论）
- 原文："in the award winning paper at ICSE 2009, a search algorithm (i.e., Genetic Programming) was used and was run 100 times on each artifact in the case study" / "the total number of ﬁtness evaluations was 400 (a population size of 40 individuals that is evolved for 10 generations). This sounds like a very low number" / "in half of the subject artifacts in the case study, the average number of ﬁtness evaluations per run is at most 41, thus implying that, on average, appropriate patches are found in the random initialization of the ﬁrst population before the actual evolutionary search even starts."
- 要点：一个反例：ICSE 2009 一篇获奖论文（自动修复缺陷）的遗传编程总共只做了 400 次适应度评估；在一半的研究对象上，合适的补丁在随机生成第一代种群时就已找到，真正的进化搜索还没开始。说明搜索预算要报告，也说明需要和随机搜索比较。

### E4

- 位置：§3
- 原文："a search algorithm should always be compared against at least random search in order to check that success is not due to the search problem (or case study) being easy."
- 要点：搜索算法至少要和随机搜索比较，以确认成功不是因为问题（或所选实例）本身太简单。

### E5

- 位置：§4 Statistical Difference
- 原文："To enable statistical analysis, one should run both A and B a large enough number (n) of times, in an independent way, to collect information on the probability distribution of M for each algorithm."
- 要点：要做统计分析，两个算法都要独立地运行足够多次，以了解各自性能指标的概率分布。

### E6

- 位置：§4 Statistical Difference
- 原文："The focus of such experiments should rather be on whether a given technique brings any practically signiﬁcant advantage, usually measured in terms of an estimated effect size and its conﬁdence interval" / "In practice, the selection of an algorithm would depend on the p-value of effectiveness comparisons, the effectiveness effect size, and the cost difference among algorithms (e.g., in terms of user-provided inputs or execution time)."
- 要点：实验的重点应是新方法有没有实际意义上的优势，用效应量及其置信区间衡量；实际选算法时，还要看 p 值和各算法的成本差异（如需要用户提供的输入、执行时间）。

### E7

- 位置：§7 Effect Size
- 原文："But for distributions with high skewness (as in the geometric distribution and as it is often the case for search algorithms), the results of scaling the mean difference by the standard deviation “would not be valid”" / "In this case, a non-parametric effect size should be preferred."
- 要点：搜索算法的结果分布常常高度偏斜，此时"均值差除以标准差"这类效应量（d 家族）不再有效，应改用非参数效应量。

### E8

- 位置：§7 Effect Size
- 原文："given a performance measure M , Aˆ12 measures the probability that running algorithm A yields higher M values than running another algorithm B. If the two algorithms are equivalent, then Aˆ12 = 0.5." / "For example, Aˆ12 = 0.7 entails one would obtain better results 70% of the time with A."
- 要点：Vargha-Delaney Â12 衡量"运行 A 得到的指标值高于运行 B"的概率；两者相当时为 0.5；0.7 表示 70% 的情况下 A 更好。

### E9

- 位置：§8 Number of Runs
- 原文："For most problems in software engineering, thousands of randomized algorithm runs should be feasible" / "However, with thousands of runs, one would detect statistically signiﬁcant differences on practically any experiment (Section 4). It is hence essential to complement such analyses with a study of the effect size"
- 要点：多数软件工程问题跑几千次是可行的；但跑几千次时，几乎任何差异都会"显著"，所以必须同时分析效应量。

### E10

- 位置：§8 Number of Runs
- 原文："In other words, it is advisable to use size measures that are consistent with the differences being tested by the selected statistical test."
- 要点：效应量要和所用检验比较的东西一致（例如用秩检验，就配基于秩的效应量）。

### E11

- 位置：§10.1 Choice of the Artifacts
- 原文："When assessing randomized algorithms, the choice of artifacts to which these algorithms are applied (e.g., source code or executable programs) is of paramount importance as it usually has a strong bearing on the evaluation results."
- 要点：选哪些研究对象（如哪些程序）对评估结果影响很大，至关重要。

### E12

- 位置：§11 Practical Guidelines
- 原文："When randomized algorithms are analyzed, clearly specify the number of runs and employed statistical tests."
- 要点：分析随机化算法时，写清运行次数和所用的统计检验。

### E13

- 位置：§11 Practical Guidelines
- 原文："On each artifact in the case study, run each randomized algorithm at least n = 1,000 times. If this is not possible, explain the reasons and report the total amount of time it took to run the entire case study."
- 要点：作者建议每个算法在每个研究对象上至少跑 1000 次；做不到就说明原因，并报告整个实验花了多少时间。

### E14

- 位置：§11 Practical Guidelines
- 原文："it is advisable to execute less runs per artifact (though at least n = 10) and use more artifacts (rather than having n = 1,000 but only few artifacts, see Section 10.1). The objective is to strike a balance between generalization and statistical power."
- 要点：可用的研究对象很多而时间有限时，宁可每个对象少跑几次（至少 10 次）、多用一些对象，在推广性和统计功效之间取得平衡。

### E15

- 位置：§11 Practical Guidelines
- 原文："Even if obtaining such artifacts is usually not possible, it is important to always clarify how they were chosen."
- 要点：很难拿到大量无偏、有代表性的研究对象，但一定要说清楚它们是怎么选出来的。

### E16

- 位置：§11 Practical Guidelines
- 原文："For detecting statistical differences, use the two-tailed non-parametric Mann-Whitney U-test for interval-scale results and the Fisher exact test for dichotomous results"
- 要点：检验差异时，数值型结果用双侧的非参数 Mann-Whitney U 检验，"成功/失败"这类二元结果用 Fisher 精确检验。

### E17

- 位置：§11 Practical Guidelines
- 原文："Report all the obtained p-values, whether they are smaller than α or not, and not just whether differences are signiﬁcant."
- 要点：报告所有 p 值，不论是否小于显著性水平，而不只是说"显著"或"不显著"。

### E18

- 位置：§11 Practical Guidelines
- 原文："Always report standardized effect size measures." / "It is also strongly advised to report effect size conﬁdence intervals, e.g., by using a bootstrapping technique."
- 要点：始终报告标准化效应量，并强烈建议给出效应量的置信区间（例如用自助法 bootstrap 计算）。

### E19

- 位置：§11 Practical Guidelines
- 原文："When analyzing more than two randomized algorithms, use pairwise comparisons including pairwise statistical tests and effect size measures."
- 要点：比较两个以上的算法时，两两比较，每对都做检验并给出效应量。

### E20

- 位置：§11 Practical Guidelines
- 原文："Though one would expect exceptions, given the current state of practice [...] the authors of this paper believe that it is important to provide practical guidance that will be valid in most cases and enable higher quality studies to be reported. It is recommendable that practitioners follow these guidelines and justify any necessary deviation."
- 要点：作者承认会有例外，指南针对的是多数情况；偏离指南时应说明理由。

### E21

- 位置：§10.2 Analysis of Multiple Artifacts
- 原文："Consider a case with ﬁve artifacts and the following Aˆ12 measures {0.6, 0.6, 0.6, 0.6, 0.1}." / "If one averages those values on the entire case study, he would obtain Aˆ12 = 0.5, thus suggesting there is no difference among the two algorithms!" / "In general, researchers should report the performance of the algorithms on each problem instance separately and attempt, as discussed above, to explain differences."
- 要点：五个研究对象上的 Â12 为 0.6、0.6、0.6、0.6、0.1，取平均是 0.5，看起来"没有差别"，其实一个算法在四个对象上更好、在一个对象上差得多。一般应分别报告每个问题实例上的表现，并尝试解释差异。
