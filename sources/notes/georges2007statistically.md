# Georges, Buytaert & Eeckhout 2007：Statistically Rigorous Java Performance Evaluation

- 资料：`georges2007statistically`，[原文（合作者 Dries Buytaert 主页）](https://dri.es/files/oopsla07-georges.pdf)
- 版本：OOPSLA 2007，作者公开的 PDF。
- 说明：针对 Java 等带托管运行环境（虚拟机、即时编译、垃圾回收）的系统；作者指出许多问题也适用于其他语言和系统。

### E1

- 位置：§1 Introduction
- 原文："Some report the average performance number across multiple runs of the same experiments; others report the best performance number, others report the second best performance number and yet others report the worst."
- 要点：现有做法五花八门：有的报多次运行的平均，有的报最好的一次，有的报第二好的，有的报最差的。

### E2

- 位置：§1 Introduction，Figure 1 讨论
- 原文："Similarly, based on the best method, one would conclude that SemiSpace clearly outperforms GenCopy. The reality though is that the confidence intervals for both garbage collectors overlap and, as a result, the performance difference seen between both garbage collectors is likely due to the random performance variations in the system under measurement."
- 要点：只报 30 次中最好的一次，会得出"一个垃圾回收器明显更快"的结论；看置信区间，两者重叠，差异很可能只是随机波动。

### E3

- 位置：§1 Introduction（贡献）
- 原文："For start-up performance, we advise to: (i) take multiple measurements where each measurement comprises one VM invocation and a single benchmark iteration" / "in each of these measurements, collect performance numbers for different iterations once performance reaches steady-state, i.e., after the start-up phase"
- 要点：启动性能和稳态性能要分开测：测启动性能，每次测量启动一次虚拟机、只跑一轮；测稳态性能，每次启动后跑多轮，只收集进入稳态之后的数据；两种都要在多次启动之间计算置信区间。

### E4

- 位置：§1 Introduction（贡献）
- 原文："statistics, and in particular confidence intervals, enable one to determine whether differences observed in measurements are due to random fluctuations in the measurements or due to actual differences in the alternatives compared against each other."
- 要点：置信区间能帮助判断测到的差异是随机波动，还是被比较方案之间的真实差异。
