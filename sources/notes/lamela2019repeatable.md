# Lamela 等人 2019：Repeatable and Reproducible Wireless Networking Experimentation through Trace-based Simulation

- 资料：`lamela2019repeatable`，[原文](https://arxiv.org/abs/1903.12033)
- 版本：arXiv:1903.12033v2，2019 年 3 月。位置写章节。

### E1

- 位置：I. Introduction
- 原文："Simulations are flexible but usually produce optimistic results, due to many simplifications required to represent complex scenarios such as those related to emerging aerial networks."
- 要点：在无线网络研究中，仿真灵活，但因为必须做很多简化，结果往往偏乐观。

### E2

- 位置：I. Introduction
- 原文："Testbeds, on the other hand, are increasingly costly to maintain and are frequently unavailable; still, they provide realistic results and are an essential step to achieve proper protocol validation and fine tuning."
- 要点：实验平台（testbed）维护成本高、经常用不上，但结果真实，是验证和调优协议必不可少的一步。

### E3

- 位置：I. Introduction
- 原文："The problem is that real wireless testbed experiments in emerging networking scenarios are hardly repeatable. Given the same input, they can produce very different output results, since wireless communications are influenced by external random phenomena such as noise, interference, and multipath"
- 要点：真实的无线实验很难重复：同样的输入，因为噪声、干扰、多径等外部随机因素，结果可能差别很大。

### E4

- 位置：III. Trace-based Simulation Approach
- 原文："The TS approach focuses on capturing traces of the execution conditions of an experiment and enabling the repetition and reproduction of such conditions using the past traces in ns-3."
- 要点：作者提出的折中办法：在真实实验中记录信道质量、节点位置等条件的轨迹，再在仿真器里回放，使实验条件可以重复。
