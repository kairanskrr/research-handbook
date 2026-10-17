# Johari、Pekelis & Walsh 2015：Always Valid Inference: Continuous Monitoring of A/B Tests

- 资料：`johari2015always`，[原文（arXiv）](https://arxiv.org/abs/1512.04922)
- 版本：arXiv 1512.04922 第 3 版（2019 年 7 月）。作者来自斯坦福大学，工作时在商业 A/B 测试平台 Optimizely 任职或担任顾问。位置只写章节。

### E1

- 位置：摘要
- 原文："A/B tests are typically analyzed via frequentist p-values and confidence intervals; but these inferences are wholly unreliable if users endogenously choose samples sizes by continuously monitoring their tests."
- 要点：A/B 测试通常用 p 值和置信区间分析；如果实验者一边持续盯着结果、一边决定样本量（什么时候停），这些推断就完全不可靠。

### E2

- 位置：§1 Introduction
- 原文："No correction for continuous monitoring is typically made in industrial practice." / "Even with 10,000 samples (a sample size which is quite common in online A/B testing), Type I error can easily increase fivefold."
- 要点：业界通常不为持续监控做校正；即使只有一万个样本（在线 A/B 测试中很常见），第一类错误率也很容易涨到五倍。

### E3

- 位置：§1 Introduction
- 原文："First, Type I error is controlled under any data-dependent rule the user might choose to stop the experiment (i.e., any stopping time for the data). Continuous monitoring does not inflate Type I error."
- 要点：作者提出的"始终有效"的 p 值和置信区间，不管实验者按什么依赖数据的规则停下，都能控制第一类错误；持续监控不会抬高假阳性率。
