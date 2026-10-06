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

### E7

- 位置：§1.1 Characteristics of Water Resources Data，第 7 条 Autocorrelation
- 原文："One of the consequences of autocorrelation is that the accuracy of any statistical estimates will be overstated if this property is ignored. For example, 100 observations of a random variable should provide a fairly accurate estimate of the population mean, but if the samples collected were spaced very close in time and the serial correlation was strong, the accuracy of the estimate of the population mean may be no better than what could be derived from a set of only 10 uncorrelated observations from that population."
- 要点：忽略自相关，会高估统计估计的准确度。例子：100 个观测本该能较准地估计均值，但如果采样时间挨得很近、序列相关很强，估计的准确度可能只相当于 10 个互不相关的观测。

### E8

- 位置：§1.1，第 7 条 Autocorrelation
- 原文："In the case of spatial data (for example, water levels or chemical concentrations in a set of wells) the term "nearby" indicates geographic proximity. This is the tendency for high values to be near other high values and low values to be near other low values."
- 要点：空间数据里（例如一组井的水位或化学浓度），自相关指高值靠近高值、低值靠近低值的倾向。

### E9

- 位置：§9.4.2.4 Detection of Serial Correlation
- 原文："If we considered a dataset of TDS concentrations and discharges collected at a daily interval for 20 years, we would have about 7,300 samples, but doing any of the computations for significance tests or confidence intervals using an n value of 7,300 would grossly overstate the true degree of certainty in our results."
- 要点：例子：每天采一次、连续 20 年，约有 7300 个溶解性总固体（TDS）浓度和流量数据；如果按 n = 7300 去算显著性检验或置信区间，会严重高估结果的确定程度。

### E10

- 位置：§9.4.2.4 Detection of Serial Correlation
- 原文："It is often the case that what may appear to be serial correlation is actually an artifact of these time or trend components."
- 要点：看起来像序列相关的东西，常常其实是季节、昼夜或趋势等时间成分造成的，要先用图检查残差和时间的关系。
