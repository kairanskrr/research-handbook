# Gundersen & Kjensmo 2018：State of the Art: Reproducibility in Artificial Intelligence

- 资料：`gundersen2018state`，[原文](https://ojs.aaai.org/index.php/AAAI/article/view/11503)
- 版本：AAAI-18 论文集，pp. 1644–1651。AAAI 出版方网站免费提供全文 PDF。调查了 IJCAI 和 AAAI 两个人工智能会议的 400 篇论文，统计它们为可复现记录了多少必要信息。

### E1

- 位置：The Terminology of Reproducibility
- 原文："While researchers in computer science agree that empirical results should be reproducible, what is meant by reproducibility is neither clearly defined nor agreed upon."
- 要点：计算机研究者都同意实证结果应当可复现，但"可复现"到底指什么，既没有明确定义，也没有共识。

### E2

- 位置：Degrees of Reproducibility
- 原文："R1: Experiment Reproducible The results of an experiment are experiment reproducible when the execution of the same implementation of an AI method produces the same results when executed on the same data." / "R2: Data Reproducible The results of an experiment are data reproducible when an experiment is conducted that executes an alternative implementation of the AI method that produces the same results when executed on the same data." / "R3: Method Reproducible The results of an experiment are method reproducible when the execution of an alternative implementation of the AI method produces the same results when executed on different data."
- 要点：可复现的三个程度：R1 同一实现、同一数据；R2 另一实现、同一数据；R3 另一实现、不同数据。

### E3

- 位置：Degrees of Reproducibility
- 原文："R1 reproducible results are less general than R2 reproducible results, which in turn are less general than R3 reproducible results."
- 要点：从 R1 到 R3，被复现的结果越来越具有一般性。

### E4

- 位置：Introduction
- 原文："Out of 402 experimental papers they were able to repeat 32.3% without communicating with the author, rising to 48.3% with communication."
- 要点：转述 Collberg & Proebsting 2016：402 篇实验论文中，不联系作者能重复 32.3%，联系作者后升到 48.3%。

### E5

- 位置：Reproducibility
- 原文："Most importantly, other researchers can be expected to be more objective. They have no interest in inflating the performance of a method they have not developed themselves. More practically, they will not share the same preconceptions and implicit knowledge as the first team reporting the research."
- 要点：独立团队更客观：他们没有动机夸大别人方法的表现，也不共享原团队的先入之见和没写下来的隐性知识。

### E6

- 位置：Reproducibility
- 原文："An independent research team is one that conducts the experiment by only using the documentation made by the original research team."
- 要点：本文对"独立团队"的定义：只依据原团队留下的文档来做实验。

### E7

- 位置：Reproducibility；Degrees of Reproducibility
- 原文："What constitutes the same results depends on to which degree the results are reproduced." / "In order for a result to be R3 reproducible the results of the experiments must support the same hypotheses and thus support the same beliefs."
- 要点：什么算"相同的结果"，取决于复现的程度；R3 程度要求实验结果支持相同的假设。

### E8

- 位置：Degrees of Reproducibility
- 原文："The results when re-running the experiment should be exactly the same, as reported in the original experiment." / "The results that are produced, the performance, using a different implementation should be the same if not exactly the same. Differences in results can be attributed to different implementations and hardware, such as different ways of doing floating point arithmetic."
- 要点：R1（同一实现、同一数据）应得到完全相同的结果；R2（换一个实现）结果应当相同但不一定完全一致，差异可能来自实现和硬件，例如浮点运算方式不同。

### E9

- 位置：Abstract
- 原文："None of the papers document all of the variables. The metrics show that between 20% and 30% of the variables for each factor are documented."
- 要点：被调查的论文没有一篇记录了全部复现所需的信息；方法、数据、实验三类信息各只记录了 20%～30%。
