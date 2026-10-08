# Runge 等人 2019：Inferring causation from time series in Earth system sciences

- 资料：`runge2019inferring`，[原文](https://doi.org/10.1038/s41467-019-10105-3)
- 版本：Nature Communications 10: 2553，2019，CC BY 开放获取。原文文本取自 Europe PMC（PMC6572812）。这是一篇观点综述（Perspective），由因果推断方法的开发者和地球系统科学家合写。位置写小标题。

### E1

- 位置：Introduction
- 原文："Discovering physical laws this way is a challenging problem when studying large-scale complex dynamical systems such as the Earth system, because replicated interventional experiments are either infeasible or ethically problematic"
- 要点：研究地球系统这类大尺度复杂系统时，可重复的干预实验要么做不到，要么有伦理问题，所以靠实验发现规律很难。

### E2

- 位置：Introduction
- 原文："While randomized controlled experiments are a standard approach in medicine and the social sciences" / "the main current alternative within most disciplines of Earth sciences are computer simulation experiments."
- 要点：随机对照实验在医学和社会科学里是标准做法，而在地球科学的多数分支，目前主要的替代办法是计算机模拟实验。

### E3

- 位置：Introduction
- 原文："In Earth system sciences, besides simulation experiments, (Pearson) correlation and regression methods are still the most commonly used tools. However, causal inference methods do have the potential to substantially advance the state-of-the-art—if the underlying assumptions and methodological challenges are taken into consideration."
- 要点：地球系统科学里，除了模拟实验，最常用的仍是相关和回归；因果推断方法有潜力大幅推进研究，前提是考虑它们背后的假设和方法上的难点。

### E4

- 位置：Causal inference methods
- 原文："Many causal inference methods for time series are grounded on the assumptions of time-order (causes precede effects), Causal Sufficiency, meaning that all direct common drivers are observed, and the Causal Markov Condition"
- 要点：很多时间序列因果推断方法依赖几条假设：原因发生在结果之前；所有直接的共同驱动因素都被观测到了（因果充分性）；以及因果马尔可夫条件。

### E5

- 位置：Challenges
- 原文："Often, relevant drivers cannot be measured, which requires to consider the possibility of unobserved variables (Fig. 4 , point 8) regarding a causal interpretation of the estimated graph, since they may render detected links spurious"
- 要点：相关的驱动因素常常测不到；对结果做因果解释时要考虑可能存在没观测到的变量，因为它们会让检测到的联系变成假的。

### E6

- 位置：Challenges
- 原文："Arguably, identifying the absence of a causal link, implying that a physical mechanism is unlikely 24 , is a more robust finding, which requires less strong assumptions (no Causal Sufficiency)."
- 要点：确认"没有因果联系"（意味着某个物理机制不太可能存在）是更稳健的发现，需要的假设更弱。

### E7

- 位置：Challenges
- 原文："Time sub-sampling (9) and aggregation (10) can make causal links appear contemporaneous and even cyclic due to insufficient time resolution"
- 要点：时间分辨率不够时（例如抽样间隔太大、做了时间平均），因果联系可能看起来是同时发生的，甚至成了循环。

### E8

- 位置：Validation and a benchmark platform
- 原文："Method development and comparison require benchmark datasets with known causal ground truth for validation."
- 要点：开发和比较因果推断方法，需要已知真实因果关系的基准数据集来验证。
