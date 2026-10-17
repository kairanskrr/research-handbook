# Dmitriev 等 2017：A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments

- 资料：`dmitriev2017dirty`，[原文（作者团队网站 PDF）](https://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf)
- 版本：KDD 2017（加拿大哈利法克斯）论文的作者版 PDF，DOI 10.1145/3097983.3098024。作者来自微软分析与实验团队，例子来自必应、MSN、Skype、Xbox 等产品。PDF 页码不清楚，位置只写章节。

### E1

- 位置：§4 Metric Taxonomy，Data Quality Metrics
- 原文："A fundamental requirement in A/B testing is that treatment and control samples are drawn at random from the same population. This means that the number of users in the samples should satisfy the expected ratio. If the actual ratio is different than the expected (a chi-square test can be used), it means something is wrong with the sampling process." / "Most of the time SRM implies a severe selection bias, enough to render the experiment results invalid"
- 要点：处理组和对照组必须从同一总体随机抽取，所以两组人数应符合预期比例；实际比例偏离预期（可用卡方检验判断），说明抽样过程出了问题，这叫样本比例不匹配，多数时候意味着严重的选择偏差，足以让实验结果无效。

### E2

- 位置：§4 Metric Taxonomy，Guardrail Metrics
- 原文："In addition to OEC metrics, we have found that there is a set of metrics which are not clearly indicative of success of the feature being tested, but which we do not want to significantly harm when making a ship decision. We call these metrics Guardrail metrics. For instance, on a web site like Bing or MSN, Page Load Time (PLT) is usually a guardrail metric."
- 要点：护栏指标不直接说明功能是否成功，但决定上线时不能让它们明显变差，例如页面加载时间。

### E3

- 位置：§4 Metric Taxonomy，Data Quality Metrics
- 原文："The first question we answer when looking at the outcome of an experiment is whether we can trust that the experiment was configured and run correctly such that we can trust the experiment results."
- 要点：看实验结果时要回答的第一个问题，是实验有没有被正确配置和运行、结果能不能信。

### E4

- 位置：§5.2 Misinterpretation of Ratio Metrics
- 原文："To detect denominator mismatch in ratio metrics, we recommend to always define count metrics for the numerator and the denominator, and provide those in the result alongside the ratio metric."
- 要点：对点击率这类比率指标，要同时定义并报告分子和分母的计数指标，以便发现分母变了。

### E5

- 位置：§5.3 Telemetry Loss Bias
- 原文："Different rates of telemetry loss between the variants is a common way to bias experiment results."
- 要点：两组的遥测数据（产品自动回传的使用记录）丢失率不同，是让实验结果产生偏差的常见原因。

### E6

- 位置：§5.4 Assuming Underpowered Metrics had no Change
- 原文："Therefore, we cannot assume that we did not impact the underpowered metric." / "To avoid the aforementioned issues, a priori power analysis should be conducted to estimate sufficient sample sizes, at least for the OEC and the Guardrail metrics"
- 要点：功效不足的指标不显著，不能当成"没有影响"；至少要对总体评价指标和护栏指标事先做功效分析，估计足够的样本量。

### E7

- 位置：§5.4 Assuming Underpowered Metrics had no Change
- 原文："If an underpowered metric turns out to be statistically significant, then it is more likely that the observed change of the metric will be exaggerated compared to the true effect size"
- 要点：功效不足的指标如果碰巧显著，观察到的变化更可能夸大了真实效应。

### E8

- 位置：§5.5 Claiming Success with a Borderline Pvalue
- 原文："In the above case, we reran the experiment with double the amount of traffic and observed that there were no statistically significant changes for the same metric." / "We recommended for experimenters to evaluate experiment results by placing emphasis on strongly statistically significant metrics and rerunning with larger traffic when metrics, in particular the OEC metrics, have borderline p-values."
- 要点：一个 p 值为 0.029 的正面结果，用双倍流量重跑后不再显著；建议重视强显著的指标，总体评价指标的 p 值在边界附近时，用更大流量重跑。

### E9

- 位置：§5.6 Continuous Monitoring and Early Stopping
- 原文："Continuously checking the results and stopping as soon as statistical significance is achieved leads to an increase in Type-I error, or the probability of a false positive." / "In our experience, stopping early or extending the experiment are both very common mistakes experiment owners make."
- 要点：不断查看结果、一显著就停，会提高第一类错误（假阳性）的概率；提前停止和临时延长实验都是很常见的错误。

### E10

- 位置：§5.6 Continuous Monitoring and Early Stopping
- 原文："Making experiment owners aware of the pitfall, and establishing the guidelines that require making ship decision only at the pre-defined time point, is one approach to avoid this pitfall. Another approach is to adjust the p-values, to account for extra checking [33]. Finally, in [34] a Bayesian framework is proposed that, unlike NHST, naturally allows for continuous monitoring and early stopping."
- 要点：避免的办法有三种：规定只在事先定好的时间点做上线决定；调整 p 值，把多看的次数考虑进去；或改用允许持续监控和提前停止的贝叶斯框架。

### E11

- 位置：§5.6 Continuous Monitoring and Early Stopping
- 原文："The issue is exacerbated by the fact that in practice continuous experiment monitoring is essentially a requirement to be able to shut down the experiment quickly in case a strong degradation in user experience is observed."
- 要点：实际中又必须持续监控实验，才能在用户体验明显变差时尽快关掉它，这让问题更棘手。

### E12

- 位置：§5.8 Segment Interpretation
- 原文："The key lesson from this example is to ensure that the condition used for defining the segment is not impacted by the treatment." / "Aside from increasing the possibility of encountering a Simpson's paradox, this is also an instance of multiple testing problem [37] and will result in an increased Type-I error."
- 要点：按用户分群分析时，分群条件本身不能受处理影响；一直细分用户直到找到显著结果，既容易碰上辛普森悖论，也是多重检验问题，会提高假阳性率。

### E13

- 位置：§5.10 Novelty and Primacy Effects
- 原文："We also recommend segmenting treatment effect by different days of the experiment, or different user visits, to see if the treatment effect changes over time."
- 要点：建议按实验的不同天、用户的不同次访问分别看处理效应，检查效应是否随时间变化。

### E14

- 位置：§5.12 Failure to Apply Twyman's Law
- 原文："Twyman's law says that any figure that looks interesting or different is usually wrong. Applying it to analyzing the results of online experiments, we can rephrase it as follows: any unexpected metric movement, positive or negative, usually means there is an issue."
- 要点：特怀曼定律：看起来有趣或与众不同的数字通常是错的；用到在线实验上，任何意外的指标变化，无论正负，通常说明有问题。

### E15

- 位置：§5.7 Assuming the Metric Movement is Homogeneous
- 原文："Not being aware of such effects may result in shipping a feature that, while improving user experience overall, substantially hurts experience for a group of users."
- 要点：不注意效应在不同用户群之间的差异，可能上线一个总体有利、却严重伤害某一群用户的功能。

### E16

- 位置：§5.9 Impact of Outliers
- 原文："As the example above shows, however, one needs to ensure that all variants in the experiment are impacted by the outlier filtering logic in the same way."
- 要点：过滤异常值时，要确保各组受过滤规则的影响相同；文中一次实验的处理让一些真实用户活跃到被当成机器人过滤掉。
