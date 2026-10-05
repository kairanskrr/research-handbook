# Lones 2021：How to avoid machine learning pitfalls

- 资料：`lones2021avoid`，[原文](https://arxiv.org/abs/2108.02497)
- 版本：arXiv:2108.02497v5（2024-08-29），本地 PDF `papers/pdf/lones2021avoid.pdf`。页码为 PDF 页脚页码。
- 说明：面向机器学习研究者的指南。这里只摘录能推广到其他学科的原则（基线、检验数据独立、重复评估、多重比较、报告方式）。

### E1

- 位置：§5.2 Do use meaningful baselines，第 21 页
- 原文："Baselines are often simpler than the new approach, and are chosen to demonstrate that any complexity in the new model is necessary."
- 要点：基线（baseline）常常比新方法简单，用来证明新方法多出来的复杂度确有必要。

### E2

- 位置：§5.2，第 21 页
- 原文："In addition to simple baselines, it’s also important to compare against state-of-the-art (SOTA) models."
- 要点：除了简单基线，还要和当前最好的方法比较。

### E3

- 位置：§3.1 Don’t allow test data to leak into the training process，第 8 页
- 原文："The best thing you can do to prevent these issues is to partition off a subset of your data right at the start of your project, and only use this independent test set once to measure the generality of a single model at the end of the project"
- 要点：项目一开始就划出一份独立的测试数据，只在最后用一次，评估最终的那一个模型。

### E4

- 位置：§4.3 Do avoid sequential overfitting，第 15 页
- 原文："Often this is done as an informal process, trying out different models and different hyperparameters until you get good performance on the test set."
- 要点：反复用同一份测试数据试不同方案、直到结果好看，这个过程往往不被记录，却会让结果对这份数据过拟合。

### E5

- 位置：§4.3，第 15 页
- 原文："the more times you use the test set, the more the overfitting that occurs."
- 要点：测试数据用得越多次，过拟合越严重。

### E6

- 位置：§4.4 Do evaluate a model multiple times，第 15 页
- 原文："a single evaluation of a model can be unreliable, and may either underestimate or overestimate the model’s true potential."
- 要点：只评估一次不可靠，可能高估也可能低估真实水平，所以要多次评估。

### E7

- 位置：§5.4 Do correct for multiple comparisons，第 22 页
- 原文："if you do 20 pairwise tests with a confidence level of 95%, one of them is likely to give you the wrong answer."
- 要点：做 20 次 95% 置信水平的两两检验，很可能有一次给出错误结论。比较次数多了要做多重比较校正。

### E8

- 位置：§6.4 Do be careful when reporting statistical significance，第 25 页
- 原文："If you have enough samples, you can always find significant differences, even when the actual difference in performance is miniscule."
- 要点：样本足够多时，再小的差异也能"显著"；要同时报告效应量（effect size），判断差异是否真的重要。

### E9

- 位置：§6 How to report your results，第 23 页
- 原文："In order to effectively contribute to knowledge, you need to provide a complete picture of your work, covering both what worked and what didn’t."
- 要点：要完整报告工作，既包括有效的，也包括无效的。

### E10

- 位置：§6.3 Don’t generalise beyond the data，第 24 页
- 原文："if your model does really well on one data set, this does not mean that it will do well on other data sets."
- 要点：在一个数据集上表现好，不代表在别的数据集上也好；结论不要超出数据能支持的范围。

### E11

- 位置：§5.1 Don’t assume a bigger number means a better model，第 19 页
- 原文："There are various reasons why a higher figure does not imply a better model."
- 要点：数字更高不等于方法更好，例如比较双方用的数据划分不同。

### E12

- 位置：§5.4，第 22 页
- 原文："there are numerous other approaches, and there is also some debate about when and where these corrections should be applied"
- 要点：多重比较校正有多种方法，什么时候该校正本身也有争论。

### E13

- 位置：§5.1 Don’t assume a bigger number means a better model
- 原文："Another reason for unfair comparisons is the failure to carry out the same amount of hyperparameter optimisation" / "if one model has default settings and the other has been optimised, then the comparison won’t be fair."
- 要点：比较不公平的一个原因是超参数优化做得不一样多：一个用默认设置，另一个调过，比较就不公平。

### E14

- 位置：§5.1
- 原文："To be sure of a fair comparison between two approaches, you should freshly implement all the models you’re comparing, optimise each one to the same degree, carry out multiple evaluations"
- 要点：要确保公平比较，应重新实现所有要比较的模型，每个优化到同样程度，做多次评估，再用统计检验判断差异是否显著。

### E15

- 位置：§5.5 Don’t always believe results from community benchmarks
- 原文："if access to the test set is unrestricted, then you can’t assume that people haven’t used it as part of the training process." / "by comparing lots of models on the same test set, it becomes increasingly likely that the best model just happens to over-fit the test set"
- 要点：社区基准的测试集公开时，不能假定没人用它训练过；即使每人只用一次，整个社区反复在同一测试集上比较，最好的模型也可能只是碰巧过拟合了测试集。

### E16

- 位置：§5.5
- 原文："it is possible that their training data included the test sets from community benchmarks."
- 要点：使用基础模型（foundation model）时尤其要小心，它们的训练数据可能包含了社区基准的测试集。

### E17

- 位置：§6.2 Do report performance in multiple ways
- 原文："One way to achieve better rigour when evaluating and comparing models is to use multiple data sets."
- 要点：用多个数据集评估和比较模型，可以弥补单个数据集的缺陷，给出更完整的图景。
