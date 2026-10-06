# Arp 等人 2022：Dos and Don'ts of Machine Learning in Computer Security

- 资料：`arp2022dos`，[原文](https://arxiv.org/abs/2010.09470)
- 版本：USENIX Security 2022，本地 PDF `papers/pdf/arp2022dos.pdf`。
- 说明：总结机器学习用于计算机安全时的十种常见陷阱（P1–P10）。

### E1

- 位置：§2，P6 Inappropriate Baseline
- 原文："To show to what extent a novel method improves the state of the art, it is vital to compare it with previously proposed methods." / "Instead of focusing solely on complex models for comparison, simple models should also be considered throughout the evaluation."
- 要点：要说明新方法比现有方法好多少，就必须和已有方法比较；除了复杂模型，也要和简单模型比。

### E2

- 位置：§2，P9 Lab-Only Evaluation
- 原文："A learning-based system is solely evaluated in a laboratory setting, without discussing its practical limitations." / "it should be evaluated in a realistic setting whenever possible to transparently assess its capabilities"
- 要点：只在实验室环境中评估、不讨论实际局限，是常见陷阱；只要可能，就应在真实环境中评估。

### E3

- 位置：摘要
- 原文："we analyze the prevalence of these pitfalls in 30 top-tier security papers from the past decade that rely on machine learning" / "To our surprise, each paper suffers from at least three pitfalls; even worse, several pitfalls affect most of the papers, which shows how endemic and subtle the problem is."
- 要点：在 30 篇安全顶会论文中，每篇至少有三个陷阱，有几个陷阱影响了大多数论文，说明问题普遍而隐蔽。

### E4

- 位置：§2，P3 Data Snooping
- 原文："Test snooping occurs when the test set is used for experiments before the ﬁnal evaluation." / "Temporal snooping occurs if time dependencies within the data are ignored." / "selective snooping describes the cleansing of data based on information not available in practice. An example is the removal of outliers based on statistics of the complete dataset"
- 要点：数据窥探分三类：最终评估之前就用测试集做实验；忽略数据中的时间依赖；用实际中拿不到的信息清洗数据（例如基于整个数据集的统计量去除离群值）。

### E5

- 位置：§2，P3 Data Snooping
- 原文："as the characteristics of publicly available datasets are increasingly exposed, methods developed using this data implicitly leverage knowledge from the test data" / "Consequently, experiments on well-known datasets should be complemented with experiments on more recent data from the considered application domain."
- 要点：公开数据集的特点被研究得越来越透，基于它开发的方法会隐含地利用测试数据的知识；所以在知名数据集上的实验，应再配上更新的数据。

### E6

- 位置：§2，P4 Spurious Correlations
- 原文："Spurious correlations result from artifacts that correlate with the task to solve but are not actually related to it, leading to false associations." / "The model may learn to detect a speciﬁc IP range instead of generic attack patterns."
- 要点：虚假相关来自和任务相关、但与任务本身无关的人为痕迹；例如入侵检测数据中大部分攻击来自某个网段，模型可能学会识别这个网段，而不是攻击模式。

### E7

- 位置：§2，P5 Biased Parameter Selection
- 原文："over-optimistic results can be easily produced by tuning hyperparameters or calibrating thresholds on the test data instead of the training data."
- 要点：在测试数据上而不是训练数据上调超参数或定阈值，很容易得到过于乐观的结果。

### E8

- 位置：§2，P8 Base Rate Fallacy
- 原文："Consider the example in Figure 2 where 99 % true positives are possible at 1 % false positives. Yet, if we consider the class ratio of 1:100, this actually corresponds to 100 false positives for every 99 true positives."
- 要点：基础比率谬误：真阳性率 99%、假阳性率 1% 看似很好，但正负样本比为 1:100 时，每 99 个真阳性就伴随 100 个假阳性。

### E9

- 位置：§2，P7 Inappropriate Performance Measures
- 原文："Given the ROC curve alone, the performance appears excellent, yet the low precision reveals the true performance of the classiﬁer"
- 要点：在不平衡数据上，只看 ROC 曲线表现很好，但精确率很低才反映了分类器的真实表现。

### E10

- 位置：§2，P2 Label Inaccuracy
- 原文："this labeling is rarely perfect and researchers must account for uncertainty and noise"
- 要点：标签很少完全准确，研究者必须考虑标签中的不确定性和噪声。

### E11

- 位置：§2，P1 Sampling Bias
- 原文："The collected data does not sufﬁciently represent the true data distribution of the underlying security problem"
- 要点：抽样偏差：收集的数据不能充分代表问题的真实数据分布。

### E12

- 位置：§4.1 Mobile Malware Detection
- 原文："Interestingly, the URL play.google.com turns out to be one of the ﬁve most discriminative features for the benign class, indicating that the classiﬁer has learned to distinguish the origins of Android apps, rather than the difference between malware and benign apps"
- 要点：恶意软件检测实验中，"play.google.com"这个网址成了判定正常应用最重要的特征之一，说明分类器学会的是区分应用来源，而不是区分恶意和正常。
