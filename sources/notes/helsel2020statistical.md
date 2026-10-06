# Helsel 等 2020：Statistical Methods in Water Resources

- 资料：`helsel2020statistical`，[原文 PDF](https://pubs.usgs.gov/tm/04/a03/tm4a3.pdf)
- 版本：美国地质调查局（United States Geological Survey，USGS）Techniques and Methods, book 4, chapter A3，2020 年版（取代 2002 年版）。美国政府出版物，可免费阅读。位置写 PDF 页码（从封面算起）。

### E1

- 位置：§1.1 Characteristics of Water Resources Data，PDF 第 26 页
- 原文："Data reported only as below or above some threshold. In statistics these are known as censored data. Examples include concentrations of a chemical or particles that are reported as being below a laboratory reporting limit"
- 要点：只报告"低于"或"高于"某个阈值的数据，在统计上叫删失数据，例如报告为低于实验室报告限的浓度。

### E2

- 位置：§5.5 Two-group Tests for Data with Nondetects，PDF 第 210 页
- 原文："The two-sample t-test, after substituting one-half the reporting limit for nondetects, has unfortunately been a common procedure in water resources for testing differences between groups. This procedure may not find differences between groups that are there or may find differences that are not there"
- 要点：把未检出值替换成报告限的一半再做 t 检验，在水资源领域很常见，但这样可能漏掉真实存在的差别，也可能找出并不存在的差别。

### E3

- 位置：§5.5 Two-group Tests for Data with Nondetects，PDF 第 210 页
- 原文："Even with recensoring, this is a better procedure than using the t-test after substitution, as it avoids the consequences of falsely stating that the exact value for each nondetect is known."
- 要点：用秩和检验的做法更好，因为它不假装知道每个未检出值的确切数值。

### E4

- 位置：§5.3.5，PDF 第 200 页
- 原文："If the question is whether one group shows higher values than another, all data below the highest reporting limit can be assigned a tied rank and the rank-sum test computed, without making any distributional assumptions or assigning arbitrary values to the data"
- 要点：比较两组哪组偏高时，可以把低于最高报告限的数据都看成并列的秩，再做秩和检验，不需要分布假设，也不用编造数值。

### E5

- 位置：§12.7 Applicability of Trend Tests with Censored Data，PDF 第 637 页
- 原文："Substitution of an arbitrarily chosen value below the reporting limit for all censored values will give biased estimates of the trend slope. Although the amount of bias cannot be stated precisely, the presence of only a few less-than values in a record (less than about five percent) is not likely to affect the accuracy of the trend slope magnitude substantially"
- 要点：把所有删失值都替换成某个任意值，会让趋势斜率的估计有偏；不过如果"小于"值很少（约 5% 以下），影响可能不大。

### E6

- 位置：§15.3 例题中的说明，PDF 第 752 页
- 原文："a reporting limit is a concentration value below which the laboratory lacks confidence to state a specific concentration value"
- 要点：报告限是这样一个浓度：低于它，实验室就没有把握给出具体数值。
