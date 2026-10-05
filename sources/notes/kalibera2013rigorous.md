# Kalibera & Jones 2013：Rigorous Benchmarking in Reasonable Time

- 资料：`kalibera2013rigorous`，[原文（肯特大学机构库）](https://kar.kent.ac.uk/33611/)
- 版本：ISMM 2013，作者接受稿（Author's Accepted Manuscript）。

### E1

- 位置：§1 Introduction
- 原文："71 failed to provide any measure of variation (such as variance or a confidence interval) for their results."
- 要点：2011 年几个编程语言和系统顶会、期刊中以运行时间为主要指标的 90 篇论文里，71 篇没有给出任何波动指标（如方差或置信区间）。

### E2

- 位置：§1 Introduction
- 原文："Advances in performance in our field are often small (Mytkowicz et al [20] report a median of 10%) and so can fall within the bounds of measurement error."
- 要点：这个领域的性能提升往往不大（中位数约 10%），可能落在测量误差范围之内。

### E3

- 位置：§2 Related Work
- 原文："Mytkowicz et al [20] found a number of sources of significant measurement bias, i.e. a systematic error in the measurement of systems that might favour one system over another. These included the Unix environment size and the link order"
- 要点：转述 Mytkowicz 等人的发现：存在显著的测量偏差，即可能偏向某个系统的系统性误差，来源包括 Unix 环境变量的大小和链接顺序。

### E4

- 位置：§2 Related Work
- 原文："However, our experimental methodology made it feasible to consider SPEC's full `reference' sizes, where we found that, although there was variation, it was very small"
- 要点：作者重做实验，确认了链接顺序在小规模训练输入下的影响；但在 SPEC 正式规模输入下，这种变化很小。

### E5

- 位置：§3 The Challenge of Reasonable Repetition
- 原文："Uncontrolled variables happen to be fixed for most or all of an experiment, but are beyond our control. If these impact the results, they cause bias and mislead." / "For example, randomising link order turns an uncontrolled variable into a random one."
- 要点：不受控变量在实验中恰好固定、又不由你控制，会造成偏差；实验者的第一个任务是把它们变成受控变量或随机变量，例如随机化链接顺序。

### E6

- 位置：§3 The Challenge of Reasonable Repetition
- 原文："At the very least, repetition must be done at the highest level that has random variation to avoid bias"
- 要点：变化可能来自编译、每次执行、每次迭代等多个层次；至少要在有随机变化的最高层次上重复，才能避免偏差。

### E7

- 位置：§4 The Challenge of Summarising Results
- 原文："statistical significance methods confuse sample size and practical relevance"
- 要点：计算机实验很容易产生大量样本，样本一大，再小的差异也会"统计显著"；显著性检验混淆了样本量和实际意义。

### E8

- 位置：§4 The Challenge of Summarising Results
- 原文："Such a statement is more natural than those derived from significance testing and less open to misinterpretation: it quantifies the size of the change, gives its error bound and indicates how certain this result is." / "RECOMMENDATION: Analysis of results should be statistically rigorous and in particular should quantify any variation. Report performance changes with effect size confidence intervals."
- 要点：建议用效应量的置信区间报告性能变化，例如"有 95% 的把握认为 A 比 B 快 5.5% ± 2.5%"：给出变化大小、误差范围和确定程度，比显著性检验更不容易被误读。

### E9

- 位置：§1 Introduction
- 原文："Even if reported speedups are relatively large, a rigorous study should estimate the measurement error."
- 要点：即使报告的加速比比较大，严谨的研究也应估计测量误差。

### E10

- 位置：§5 Benchmarks and Platforms
- 原文："We disable all system services that might interfere with measurements."
- 要点：作者在实验平台上关闭了所有可能干扰测量的系统服务。
