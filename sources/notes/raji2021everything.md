# Raji 等人 2021：AI and the Everything in the Whole Wide World Benchmark

- 资料：`raji2021everything`，[原文（arXiv:2111.15366）](https://arxiv.org/abs/2111.15366)
- 版本：arXiv v1（2021 年 11 月 26 日），即 NeurIPS 2021 数据集与基准分会（Track on Datasets and Benchmarks）论文。
- 说明：机器学习方向的立场论文，以 ImageNet 和 GLUE 为例，批评把一个基准当作"通用能力"的度量，讨论其中的构念效度问题。

### E1

- 位置：§2.2 A Brief History of Benchmarking Practice in AI
- 原文："In this paper we describe a benchmark as a particular combination of a dataset or sets of datasets (at least test data, sometimes also training data), and a metric, conceptualized as representing one or more specific tasks or sets of abilities, picked up by a community of researchers as a shared framework for the comparison of methods."
- 要点：基准是数据集（至少有测试数据）加一个指标，被视为代表某些具体任务或能力，并被研究社区当作比较方法的共同框架。

### E2

- 位置：§2.3 Construct Validity
- 原文："in the context of machine learning, how well the benchmark dataset, and associated metrics of evaluation, represents a task"
- 要点：在机器学习中，构念效度指基准数据集及其评测指标在多大程度上代表了要测的任务。

### E3

- 位置：§4.1 Limited Task Design
- 原文："Instead, what we observe looks more like samples of convenience: tasks and collections of tasks arbitrarily built out of what is easily available to the team developing these benchmarks, even if such constructions are theoretically unsound."
- 要点：所谓"通用"基准里的任务，看起来更像方便样本：建基准的团队手头有什么就用什么，即使理论上站不住。

### E4

- 位置：§4.1.1 Arbitrarily Selected Tasks and Collections（引 Wagstaff 2012）
- 原文："Legions of (ML) researchers have chased after the best iris or mushroom classifier. Yet this flurry of effort does not seem to have had any impact on the fields of botany or mycology."
- 要点：大批研究者追逐鸢尾花、蘑菇分类的最好成绩，但这对植物学、真菌学几乎没有影响：基准任务未必对应任何人真正关心的问题。

### E5

- 位置：§4.2 De-contextualized Data and Performance Reporting
- 原文："No dataset is neutral and there are inherent limits to what a benchmark can tell us" / "the claim to generality will often act as cover, allowing those developing the benchmarks to escape the responsibility of reporting details of these limitations."
- 要点：没有中立的数据集，基准能说明的东西有限；宣称"通用"常常成了不报告局限的挡箭牌。

### E6

- 位置：§4.2.2 Benchmark Subjectivity
- 原文："when analyzing country level geo-location data for the 2011 version of the dataset, 45% of the images were found to be sourced from the US, and over 60% from a small selection of Western countries in North America and Europe"
- 要点：ImageNet 2011 版中 45% 的图片来自美国，六成以上来自少数北美和欧洲国家：数据来源的偏向会进入基准。

### E7

- 位置：§4.3.3 Justification for Practical out of Context or Unsafe Applications
- 原文："Poor performance on minority subgroups could possibly be disguised in aggregate and decontextualized "general" benchmarks to justify deployment."
- 要点：只报总体分数，可能掩盖模型在少数子群体上的糟糕表现。

### E8

- 位置：§5 Alternative Roles for Benchmarking and Alternative Evaluation Methods
- 原文："First, we argue that benchmarks should be developed, presented and understood as intended [...] to evaluate concrete, well-scoped and contextualized tasks."
- 要点：基准应当按它本来的用途来开发、介绍和理解：评估具体的、范围清楚、有语境的任务。

### E9

- 位置：§4.2.1 Limited Scope
- 原文："ImageNet authors note the trade-off between annotation quality and size, remarking that "the scale [is] already imposing limits on the manual annotations that are feasible to obtain""
- 要点：ImageNet 作者自己也指出标注质量和规模之间要取舍：规模已经限制了能拿到多少人工标注。

### E10

- 位置：§6 Conclusion
- 原文："Benchmarking, appropriately deployed, is not about winning a contest but more about surveying a landscape"
- 要点：用得恰当的基准评测，不是为了赢比赛，而是为了看清全貌。
