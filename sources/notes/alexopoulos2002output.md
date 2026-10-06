# Alexopoulos & Kim 2002：Output Data Analysis for Simulations

- 资料：`alexopoulos2002output`，[原文（Winter Simulation Conference 论文集，informs-sim.org 开放获取）](https://www.informs-sim.org/wsc02papers/012.pdf)
- 版本：Proceedings of the 2002 Winter Simulation Conference，第 85—96 页。

### E1

- 位置：§1 Introduction
- 原文："Unfortunately, a simulation run does not usually produce independent, identically distributed (i.i.d.) observations; therefore “classical” statistical techniques are not directly applicable to the analysis of simulation output."
- 要点：一次仿真运行产生的观测值通常不是独立同分布的，所以经典统计方法不能直接用来分析仿真输出。

### E2

- 位置：§1 Introduction
- 原文："Finite-horizon simulations. In this case the simulation starts in a speciﬁc state and runs until a terminating event occurs." / "Steady-state simulations. The purpose of a steady-state simulation is the study of the long-run behavior of the system of interest."
- 要点：仿真分两类：有限时长（终止型）仿真从特定状态开始、到终止事件结束；稳态仿真研究系统的长期行为。

### E3

- 位置：§2 Finite-Horizon Simulations
- 原文："To overcome this problem, we can run k independent replications of the simulation."
- 要点：一次运行内部的数据相互相关、难以估计方差，解决办法是做多次独立的重复运行。

### E4

- 位置：§3 Initialization Problems for Steady-State Simulations
- 原文："One of the hardest problems in steady-state simulations is the removal of the initialization bias."
- 要点：稳态仿真中最难的问题之一，是消除初始状态带来的偏差。

### E5

- 位置：§3 Initialization Problems for Steady-State Simulations
- 原文："The most commonly used method for eliminating the bias" / "because the initial conditions primarily affect data at the beginning of a run"
- 要点：最常用的办法是截掉运行开头的一段观测值（即预热期），因为初始条件主要影响运行开头的数据。

### E6

- 位置：§3 Initialization Problems for Steady-State Simulations
- 原文："The graphical procedure of Welch (1983) is popular due to its simplicity and generality. This method uses k independent runs" / "the procedure plots the moving averages" / "If the plot is reasonably smooth, then l is chosen to be the value of j beyond which the sequence of moving averages converges."
- 要点：确定截断点（预热期长度）时，Welch 的作图法因简单通用而常用：用多次独立运行的结果求平均，画出移动平均曲线，取曲线开始收敛的位置作为截断点。

### E7

- 位置：§4.1 The Replication/Deletion Approach
- 原文："This approach runs k independent replications, each of length l + n observations, and discards the ﬁrst l observations from each run. One then uses the i.i.d. sample means"
- 要点：重复/删除法：做 k 次独立重复运行，每次丢掉开头的 l 个观测值，再用各次运行的样本均值（彼此独立同分布）做统计。

### E8

- 位置：§4.1 The Replication/Deletion Approach
- 原文："The systematic error in the sample means Yi(l, n) cannot be reduced by increasing the number of replications k."
- 要点：初始状态造成的系统误差，不能靠增加重复次数来减小。
