# Imbens & Lemieux 2008：Regression Discontinuity Designs: A Guide to Practice

- 资料：`imbens2008rd`，[NBER 工作论文版 PDF](https://www.nber.org/system/files/working_papers/w13039/w13039.pdf)；正式版发表于 Journal of Econometrics 142(2)，2008
- 版本：NBER Working Paper 13039（2007 年 4 月）。摘录依据工作论文版；位置写小节号。PDF 转文本时 fi、ff 连字丢失，所以只摘不含这些字母组合的句子。

### E1

- 位置：§8 Conclusion: A Summary Guide to Practice
- 原文："Graph the data (Section 3) by computing the average value of the outcome variable over a set of bins."
- 要点：第一步是画图：把驱动变量分成若干小区间，算出每个区间里结果变量的平均值。

### E2

- 位置：§7 Specification Testing
- 原文："For example, at age 65 individuals become eligible for discounts at many cultural institutions." [...] "The more plausible explanation is that there are other institutional changes"
- 要点：断点回归的一个隐患是同一条分界线上还同时发生了别的变化。例如 65 岁时很多文化场所开始给折扣，但 65 岁时工作时间的跳变，更可能来自同在 65 岁发生的其他制度变化。

### E3

- 位置：§7.1 Tests Involving Covariates
- 原文："In most cases, the reason for the discontinuity in the probability of the treatment does not suggest a discontinuity in the average value of covariates."
- 要点：一般来说，处理概率在分界线上跳变，并不意味着协变量（事先就定下来的个人特征）也会跳变；所以可以拿协变量做检验。

### E4

- 位置：§7.2 Tests of Continuity of the Density
- 原文："Even if such discontinuities are not conclusive evidence of violations of the RD assumptions, at the very least, inspecting this density would be useful to assess whether it exhibits unusual features that may shed light on the plausibility of the design."
- 要点：驱动变量的分布在分界线处跳变，不一定能证明设计失效，但检查这个分布至少能发现异常，帮助判断设计是否可信。

### E5

- 位置：§7.3 Testing for Jumps at Non-discontinuity Points
- 原文："A third set of tests involves estimating jumps at points where there should be no jumps."
- 要点：第三类检验：在本不该有跳变的位置（假的分界线）估计跳变。

### E6

- 位置：§7.5 Sensitivity to the Choice of Bandwidth
- 原文："Irrespective of the manner in which the bandwidth is chosen, one should always investigate the sensitivity of the inferences to this choice, for example, by including results for bandwidths twice (or four times) and half (or a quarter of) the size of the originally chosen bandwidth." / "but if the results are critically dependent on a particular bandwidth choice, they are clearly less credible than if they are robust to such variation in bandwidths."
- 要点：不管带宽怎么选，都要报告结果对带宽的敏感性，例如带宽加倍（或四倍）、减半（或四分之一）时的结果；结果只在某个带宽下成立，就远没有那么可信。

### E7

- 位置：§8 Conclusion: A Summary Guide to Practice
- 原文："running linear regressions on both sides of the"
- 要点：估计效应的做法：在分界线两侧（一定带宽内）分别做线性回归。
