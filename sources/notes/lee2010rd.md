# Lee & Lemieux 2010：Regression Discontinuity Designs in Economics

- 资料：`lee2010rd`，[NBER 工作论文版 PDF](https://www.nber.org/system/files/working_papers/w14723/w14723.pdf)；正式版发表于 Journal of Economic Literature 48(2)，2010
- 版本：NBER Working Paper 14723（2009 年 2 月，2009 年 10 月修订）。摘录依据工作论文版；位置写小节号。

### E1

- 位置：§3.1 Valid or Invalid RD?
- 原文："The key word here is "precise", rather than "manipulate". After all, in both examples above, individuals do exert some control over the test score." / "Precise sorting around the threshold is self-selection."
- 要点：关键词是"精确"而不是"操纵"：人们对驱动变量（如考试分数）总有一定影响力；真正破坏设计的，是能精确地把自己放到分界线某一侧，那就是自我选择。

### E2

- 位置：§2.3 RD design as a Local Randomized Experiment
- 原文："the conditions for local randomization are testable in the same way global randomization is testable in a randomized experiment by looking at whether baseline covariates are balanced."
- 要点：分界线附近"近似随机分配"的条件可以检验，办法和检验随机实验一样：看基线协变量在两侧是否平衡。

### E3

- 位置：§4.6 A Recommended "Checklist" for Implementation
- 原文："To assess the possibility of manipulation of the assignment variable, show its distribution."
- 要点：为评估驱动变量是否被操纵，要展示它的分布（直方图）。

### E4

- 位置：§4.4.1 Inspection of the Histogram of the Assignment Variable
- 原文："this test can fail to detect a violation of the RD identification condition if for some individuals there is a "jump" up in the density, offset by jumps "down" for others, making the aggregate density continuous at the threshold."
- 要点：McCrary 的密度检验可能漏判：有人往上跳、有人往下跳，相互抵消后总体分布看起来仍然连续。

### E5

- 位置：§4.6 A Recommended "Checklist" for Implementation
- 原文："Present the main RD graph using binned local averages." / "we recommend against simply presenting a continuum of nonparametric estimates (with a single break at the threshold), as this will naturally tend to give the impression of a discontinuity even if there does not exist one in the population."
- 要点：主图用分区间的局部平均值画；不要只画一条在分界线处断开的平滑曲线，那样即使没有跳变也容易看起来像有。

### E6

- 位置：§4.6 A Recommended "Checklist" for Implementation
- 原文："Explore the sensitivity of the results to a range of bandwidths, and a range of orders to the polynomial." / "report a "typical" point estimate and a range of point estimates."
- 要点：检查结果对一系列带宽和多项式阶数的敏感性，报告一个"典型"估计值和估计值的范围。

### E7

- 位置：§4.6 A Recommended "Checklist" for Implementation
- 原文："Conduct a parallel RD analysis on the baseline covariates."
- 要点：用基线协变量当"结果"，做一遍同样的断点回归。

### E8

- 位置：§4.6 A Recommended "Checklist" for Implementation
- 原文："Nevertheless, we do believe that documenting the sensitivity of the results to these array of tests and alternative specifications — even if they only appear in unpublished, online appendices — is an important component of a thorough RD analysis."
- 要点：受篇幅限制，不必把每种组合都放进正文；但把各项检验和替代设定的结果记录下来（哪怕只放在网上附录里）是完整断点分析的重要部分。

### E9

- 位置：§1 Introduction
- 原文："Our main suggestion in estimation is to not rely on one particular method or specification."
- 要点：作者在估计上的主要建议：不要只依赖某一种方法或设定。

### E10

- 位置：§1 Introduction
- 原文："there is some room for the researcher to construct graphs making it seem as though there are effects when there are none, or hiding effects that truly exist."
- 要点：图有被做出效果的空间：研究者可以把没有效应的画得像有，或把真实效应藏起来。

### E11

- 位置：§3.4.1 Imperfect Compliance: the "Fuzzy" RD
- 原文："The difference between the "sharp" and "fuzzy" RD design is exactly parallel to the difference between the randomized experiment with perfect compliance and the case of imperfect compliance, when only the "intent to treat" is randomized."
- 要点："清晰"断点和"模糊"断点的区别，正好对应随机实验中"完全遵从"和"不完全遵从、只有分配被随机化"的区别。
