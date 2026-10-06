# Menzies & Shepperd 2019："Bad smells" in software analytics papers

- 资料：`menzies2019bad`，[原文](https://arxiv.org/abs/1803.05518)
- 版本：arXiv:1803.05518v3（2019-04-13），本地 PDF `papers/pdf/menzies2019bad.pdf`。
- 说明：针对软件分析（用数据分析研究软件工程问题）论文，列出 12 种"坏味道"，即可能预示深层问题的表面迹象。

### E1

- 位置：§4.4 Inadequate Reporting，第 3 条
- 原文："Non-signiﬁcant and post hoc “uninteresting" results are not reported. This seemingly innocuous behavior, known as reporting bias, can lead to serious overestimation of effect sizes"
- 要点：不报告不显著或"没意思"的结果，即报告偏差（reporting bias），会严重高估效应大小。

### E2

- 位置：§4.6 p < 0.05 and all that!
- 原文："A correlation of r = 0.01 is trivial and to all practical purposes indistinguishable from no correlation."
- 要点：例子中样本量 18000、p = 0.049 的"显著"相关系数只有 0.01，实际上等于没有相关。统计显著不等于实际重要。

### E3

- 位置：§4.6
- 原文："methodologists encourage the notion of the smallest effect size of interest (SESOI). This should be speciﬁed before the research is conducted."
- 要点：研究开始前就定下"最小有意义效应量"，即多大的差异才算有实际意义。

### E4

- 位置：§4.9 Not Exploring Stability
- 原文："So it is important to check if the effect you want to report actually exists, or is just due to noise."
- 要点：要检查想报告的效应是否真的存在，还是只是噪声；做法包括换多个数据集，并同时报告集中趋势和离散程度。

### E5

- 位置：§4.10 Not Tuning
- 原文："One particularly egregious “smell" is to compare a heavily tuned new or pet approach with other benchmarks that are untuned."
- 要点：精心调过参的新方法对比没调参的对手，是特别严重的问题。

### E6

- 位置：§4.10 Not Tuning
- 原文："what we really learn is using the new technique well can outperform using another technique badly."
- 要点：这种比较只说明"好好用新方法能胜过随便用旧方法"，没有什么价值。

### E7

- 位置：§4.11 Not Exploring Simplicity
- 原文："it is wise to compare a seemingly sophisticated method against some simpler alternative."
- 要点：复杂方法要和更简单的替代方案比较，才能说明复杂度是值得的。

### E8

- 位置：§4.4 Inadequate Reporting，第 2 条
- 原文："The work cannot be exactly reproduced because some of the algorithms are stochastic and seeds are not provided."
- 要点：算法带随机性却不提供随机种子，别人就无法精确复现。

### E9

- 位置：§1 Introduction
- 原文："we say that the “smells” listed in this article do not necessarily indicate that the conclusions from the underlying study must be rejected."
- 要点：这些"坏味道"只是警示信号，不代表研究结论一定要被否定。

### E10

- 位置：§1 Introduction
- 原文："Studies are more data-driven than theory-driven. For example, after examining many software projects, certain coding styles could be seen to be more bug prone. Follow up experimentation, by manipulating the coding styles, could lead us to believe there is causality."
- 要点：软件分析研究多由数据驱动；从大量项目中看到某种编码风格更容易出缺陷，只是相关；要相信存在因果关系，还需要主动改变编码风格的后续实验。

### E11

- 位置：§4.3 Using Deprecated or Suspect Data
- 原文："Researchers adopting a heavily data-driven approach, as is the case for software analytics, need to be vigilant regarding data quality."
- 要点：重度依赖数据的研究必须时刻警惕数据质量；过旧的数据、已知有质量问题的数据都是警示信号。

### E12

- 位置：§4.4 Inadequate Reporting，第 1 条
- 原文："The work cannot be reproduced because the descriptions are too incomplete or high level. In addition, not all materials ( data and code) are available"
- 要点：描述太粗、数据和代码没有全部公开，别人就无法复现。

### E13

- 位置：§4.10 Not Tuning
- 原文："Many machine learners, including data miners, have poorly chosen defaults"
- 要点：很多机器学习算法的默认设置选得并不好。

### E14

- 位置：§4.10 Not Tuning
- 原文："As to how to tune, we strongly recommend against the “grid search” i.e., a set of nested for-loops that try a wide range of settings for all tuneable parameters." / "This is a slow approach" / "it has been reported that grid search can miss important optimizations" / "we recommend very simple optimizers (such as differential evolution [103]) can sufﬁce for ﬁnding better tunings"
- 要点：作者强烈反对用网格搜索（嵌套循环遍历所有参数组合）调参：慢，而且格点之间的空隙可能漏掉好的设置；建议用差分进化等简单优化器。

### E15

- 位置：§4.11 Not Exploring Simplicity
- 原文："many SE data sets have very simpler regular structures, so very simple techniques can execute much faster and perform just as well, or better, than Deep Learning."
- 要点：（软件工程数据的例子）很多软件工程数据集结构简单，很简单的方法跑得快得多，效果和深度学习一样甚至更好。

### E16

- 位置：§4.11 Not Exploring Simplicity
- 原文："by ﬁrst running a very simple algorithm, it is easy to quickly obtain baseline results to glean the overall structure of the problem."
- 要点：先跑一个很简单的算法，可以很快得到基线结果，了解问题的大致结构。
