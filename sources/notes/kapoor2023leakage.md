# Kapoor & Narayanan 2023：Leakage and the reproducibility crisis in machine-learning-based science

- 资料：`kapoor2023leakage`，[原文](https://doi.org/10.1016/j.patter.2023.100804)
- 版本：Patterns 4(9), 100804，2023；CC BY 4.0 开放获取。本次读取的是 PubMed Central 全文 PMC10499856。
- 说明：调查 17 个领域中由数据泄漏引起的可复现性问题，提出 8 种泄漏的分类和"模型信息表"，并以内战预测为例做复现研究。

### E1

- 位置：Summary
- 原文："we find 17 fields where leakage has been found, collectively affecting 294 papers and, in some cases, leading to wildly overoptimistic conclusions."
- 要点：在 17 个领域发现了数据泄漏问题，共涉及 294 篇论文，有些得出了严重过于乐观的结论。

### E2

- 位置：Results，Data leakage causes irreproducible results
- 原文："we do not present our results as a systematic meta-review of leakage from a coherent sample of papers but rather as a lower bound of reproducibility issues in ML-based science." / "the code might have errors that are not apparent from reading the papers."
- 要点：这个数字只是下限：多数综述只看论文正文，而代码中的错误读论文是看不出来的。

### E3

- 位置：Results，Leakage in modeling competitions
- 原文："In contrast, in most ML-based science, the researcher has access to the entire dataset while creating the ML models. Leakage often occurs because of the researcher having access to the entire dataset during the modeling process."
- 要点：和比赛由第三方保管测试集不同，科研中研究者建模时能接触全部数据，这正是泄漏常发生的原因。

### E4

- 位置：Taxonomy，[L1.3]
- 原文："Feature selection on the entire dataset results in using information about which feature performs well on the test set to make a decision about which features should be included in the model."
- 要点：在全部数据上做特征选择，等于利用了"哪些特征在测试集上表现好"的信息。

### E5

- 位置：Taxonomy，[L3.1] Temporal leakage
- 原文："When an ML model is used to make predictions about a future outcome of interest, the test set should not contain any data from a date before the training set."
- 要点：时间泄漏：要预测未来时，测试集中不能有早于训练集的数据，否则模型用到了"来自未来"的信息。

### E6

- 位置：Taxonomy，[L3.2]
- 原文："Nonindependence between training and test samples constitutes leakage, unless the scientific claim is about a distribution that has the same dependence structure."
- 要点：训练样本和测试样本不独立（如来自同一批人）就构成泄漏，除非科学主张针对的分布本身就有同样的依赖结构。

### E7

- 位置：Taxonomy，[L3.3] Sampling bias in test distribution
- 原文："One example of sampling bias is spatial bias, which refers to choosing the test data from a geographic location but making claims about model performance in other geographic locations."
- 要点：测试数据的抽样偏差也算泄漏，例如只用一个地区的数据测试，却声称模型在其他地区也有这样的表现。

### E8

- 位置：Summary；A case study of civil war prediction
- 原文："When the errors are corrected, complex ML models do not perform substantively better than decades-old LR models." / "We found errors in 4 of the 12 papers—exactly the 4 papers that claimed superior performance of complex ML models over baseline LR models for predicting civil war."
- 要点：在内战预测的 12 篇论文中，有错误的 4 篇恰好是声称复杂模型优于逻辑回归基线的那 4 篇；改正泄漏后，复杂模型并不比几十年前的逻辑回归好多少。

### E9

- 位置：Model info sheets
- 原文："The burden of proof for ensuring the correctness of these arguments is on the researcher making the scientific claims."
- 要点：证明"没有泄漏"的责任在提出科学主张的研究者身上。

### E10

- 位置：Summary
- 原文："We propose that researchers test for each type of leakage by filling out model info sheets, which we introduce."
- 要点：建议研究者填写"模型信息表"，逐类检查有没有泄漏。

### E11

- 位置：A case study of civil war prediction
- 原文："We found that 9 of the 12 papers for which complete code and data were available included no significance tests or uncertainty quantification for classifier performance comparison"
- 要点：12 篇提供了完整代码和数据的论文中，9 篇比较分类器时没有做显著性检验，也没有量化不确定性。
