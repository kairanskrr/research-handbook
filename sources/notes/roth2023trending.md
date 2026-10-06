# Roth, Sant'Anna, Bilinski & Poe 2023：What's Trending in Difference-in-Differences?

- 资料：`roth2023trending`，[arXiv 2201.01194](https://arxiv.org/abs/2201.01194)；正式版发表于 Journal of Econometrics 235(2)，2023
- 版本：arXiv v3（2023 年 1 月 9 日）。摘录依据 arXiv 版；位置写小节标题。

### E1

- 位置：§1 Introduction
- 原文："The key identifying assumption is that the average outcome among the treated and comparison populations would have followed "parallel trends" in the absence of treatment. We also assume that the treatment has no causal effect before its implementation (no anticipation)."
- 要点：标准双重差分的两条关键假设：没有处理的话，处理组和对照组的平均结果会平行变化（平行趋势）；处理在实施之前没有效应（无预期效应）。

### E2

- 位置：§2.3 The Parallel Trends Assumption and Identification
- 原文："In other words, parallel trends allows for the presence of selection bias, but the bias from selecting into treatment must be the same in period t = 1 as it is in period t = 2."
- 要点：平行趋势允许两组原本水平不同（存在选择偏差），但这种偏差在前后两期必须一样大。

### E3

- 位置：§1 Introduction
- 原文："In short, TWFE regressions make both "clean" comparisons between treated and not-yet-treated units as well as "forbidden" comparisons between units who are both already-treated. When treatment effects are heterogeneous, these "forbidden" comparisons potentially lead to severe drawbacks such as TWFE coefficients having the opposite sign of all individual-level treatment effects due to "negative weighting" problems."
- 要点：各单位在不同时间先后接受处理时，常规的双向固定效应回归会拿"已经处理过的"单位当对照，作者称为"禁止的比较"；处理效应因单位而异时，系数甚至可能与所有个体效应的符号相反。

### E4

- 位置：§3.5 Recommendations
- 原文："Nevertheless, it is our practical experience that the various heterogeneity-robust DiD estimators typically (although not always) produce similar answers. The first-order consideration is therefore to use an approach that makes clear what the target parameter is and which groups are being compared for identification."
- 要点：几种针对"效应因单位而异"的新估计方法，结果通常（但不总是）相近；首要的是用一个讲清"要估什么、拿谁和谁比"的方法。

### E5

- 位置：§1 Introduction
- 原文："First, the absence of a significant pre-trend does not necessarily imply that parallel trends holds; in fact, these tests often have low power. Second, conditioning the analysis on the result of a pre-test can introduce additional statistical distortions from a selection effect known as pre-test bias."
- 要点：处理前趋势检验"不显著"不等于平行趋势成立，这类检验的检验力往往很低；根据预检验结果决定怎么分析，本身还会带来额外偏差。

### E6

- 位置：§4.6 Recommendations
- 原文："we encourage researchers to continue to plot "event-study plots" that allow for a visual evaluation of pre-existing trends." / "We also think it should become standard practice for researchers to formally assess the extent to which their conclusions are sensitive to violations of parallel trends."
- 要点：作者鼓励继续画事件研究图来直观看处理前的趋势，并主张把"结论对平行趋势被违反有多敏感"的正式评估作为标准做法。

### E7

- 位置：§4.6 Recommendations
- 原文："how big would the post-treatment violation of parallel trends have to be relative to the largest pre-treatment violation to invalidate a particular conclusion?"
- 要点：一个可报告的敏感性指标：处理后的趋势偏离要达到处理前最大偏离的多少倍，结论才会被推翻。

### E8

- 位置：Table 1: A Checklist for DiD Practitioners
- 原文："A good rule of thumb is to cluster at the level at which treatment is independently assigned (e.g. at the state level when policy is determined at the state level)" / "If you have a small number of treated clusters, consider using one of the alternative inference methods described in Section 5.1."
- 要点：经验法则：在处理被独立分配的层级上聚类标准误（政策按州定，就按州聚类）；处理组的聚类很少时，考虑其他推断方法。

### E9

- 位置：§1 Introduction
- 原文："Standard cluster-robust methods assume that there is a large number of both treated and untreated clusters, and thus can perform poorly in this case."
- 要点：常规聚类稳健方法假定处理组和对照组的聚类都很多；处理组聚类很少时表现可能很差。

### E10

- 位置：§5.2 Recommendations
- 原文："If it is difficult to conceptualize a super-population, fear not! Your DiD analysis can likely still be sensible from a finite-population perspective where we think of the treatment assignment as stochastic."
- 要点：如果想象不出"数据从哪个更大的总体里抽出来"（例如样本就是全部 50 个州），也不必担心：把不确定性理解为来自处理分配的随机性，分析通常仍然说得通。

### E11

- 位置：§7 Conclusion
- 原文："Some key themes are that researchers should be clear about the comparison group used for identification, match the estimation and inference methods to the identifying assumptions, and explore robustness to possible violations of those assumptions." / "We emphasize that context-specific knowledge will often be needed to choose the right identifying assumptions and accompanying methods."
- 要点：要点有三：讲清用于识别的对照组；估计和推断方法要与识别假设匹配；检查结论对假设被违反的稳健性。选对假设和方法往往需要对具体情境的了解。

### E12

- 位置：§4.3 Testing for pre-existing trends
- 原文："We caution, however, against using dynamic TWFE specifications like (16) in settings with staggered adoption"
- 要点：处理时间先后不一时，作者提醒不要用常规的动态双向固定效应回归来画事件研究图。

### E13

- 位置：§1 Introduction
- 原文："Table 1, which contains a checklist for a practitioner implementing a DiD analysis, and Table 2, which lists R and Stata packages for implementing many of the methods described in this paper."
- 要点：文中表 1 是给做双重差分的人的检查清单，表 2 列出实现文中多数方法的 R 和 Stata 软件包。
