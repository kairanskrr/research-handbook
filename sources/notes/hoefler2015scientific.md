# Hoefler & Belli 2015：Scientific Benchmarking of Parallel Computing Systems

- 资料：`hoefler2015scientific`，[原文（作者主页）](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf)
- 版本：SC 2015（ACM/IEEE 高性能计算会议），作者主页公开的 PDF。
- 说明：调查三个顶会 120 篇并行计算论文的性能报告方式，提出 12 条规则。例子来自并行计算，多数规则适用于一般的性能测量。

### E1

- 位置：§1 Introduction
- 原文："We call an experiment interpretable if it provides enough information to allow scientists to understand the experiment, draw own conclusions, assess their certainty, and possibly generalize results."
- 要点：提出"可解释性"：即使无法完全复现，实验也应提供足够信息，让别人理解实验、得出自己的结论、评估其确定程度。

### E2

- 位置：§2，Rule 1
- 原文："When publishing parallel speedup, report if the base case is a single parallel process or best serial execution, as well as the absolute execution performance of the base case." / "A simple generalization of this rule implies that one should never report ratios without absolute values."
- 要点：报告加速比时要说明基准情形是什么，并给出它的绝对性能；推广开来：永远不要只报比值而不报绝对值。

### E3

- 位置：§2，Rule 2
- 原文："Specify the reason for only reporting subsets of standard benchmarks or applications or not using all system resources." / "A corollary of this rule is to report all results, not just the best."
- 要点：只报告标准基准的一部分时要说明原因；推论：报告全部结果，而不只是最好的。

### E4

- 位置：§3.1，Rule 3 与 Rule 4
- 原文："Use the arithmetic mean only for summarizing costs. Use the harmonic mean for summarizing rates." / "Avoid summarizing ratios; summarize the costs or rates that the ratios base on instead. Only if these are not available use the geometric mean for summarizing ratios."
- 要点：成本（如时间）用算术平均，速率用调和平均；尽量不要汇总比值，而是汇总比值背后的成本或速率；只有拿不到这些时，才用几何平均汇总比值。

### E5

- 位置：§3.1.2，Rule 5
- 原文："Report if the measurement values are deterministic. For nondeterministic data, report confidence intervals of the measurement."
- 要点：说明测量值是否是确定的；不确定的数据要报告置信区间。

### E6

- 位置：§3.1.2，Rule 6
- 原文："Do not assume normality of collected data (e.g., based on the number of samples) without diagnostic checking."
- 要点：不要不做检查就假设数据服从正态分布（例如以样本多为由）。

### E7

- 位置：§3.2，Rule 7
- 原文："Compare nondeterministic data in a statistically sound way, e.g., using non-overlapping confidence intervals or ANOVA."
- 要点：用统计上可靠的方法比较不确定的数据，例如看置信区间是否不重叠，或用方差分析。

### E8

- 位置：§3.2.3，Rule 8
- 原文："Carefully investigate if measures of central tendency such as mean or median are useful to report. Some problems, such as worst-case latency, may require other percentiles."
- 要点：想清楚平均数、中位数是否真的有用；有些问题（如最坏情况延迟）需要报告其他百分位数。

### E9

- 位置：§4.2，Rule 9
- 原文："Document all varying factors and their levels as well as the complete experimental setup (e.g., software, hardware, techniques) to facilitate reproducibility and provide interpretability." / "Ideally, researchers release the source code used for the experiment or at least the input data and their generators."
- 要点：记录所有变化的因素及其取值和完整的实验环境；理想情况下公开实验源代码，至少公开输入数据及其生成器。

### E10

- 位置：§4.1.1 Measurement Environment
- 原文："If controlling a certain parameter is not possible then we suggest randomization following standard textbook procedures."
- 要点：无法控制的环境参数（如节点分配、进程映射、干扰），按标准教科书的做法随机化。

### E11

- 位置：§4.1.2 Documenting the Setup
- 原文："We observed how several authors assumed that mentioning a well-known system such as NERSC's Hopper or ORNL's Titan is sufficient to describe the experimental setup."
- 要点：只写一个知名系统的名字不足以描述实验环境：软件会升级，别人不一定知道具体参数，隐含假设也不是人人都懂。

### E12

- 位置：§4.1.2，Warmup 与 Warm vs. cold cache
- 原文："to measure the expected time, the first measurement iteration should be excluded from the average computation." / "If small benchmarks are performed repeatedly, then their data may be in cache and thus accelerate computations. This may or may not be representative for the intended use of the code."
- 要点：有的程序按需建立工作状态，第一次迭代不应计入平均；小基准重复运行时数据可能已在缓存里，这不一定代表代码的真实使用情况。

### E13

- 位置：§4.2.1 Measuring Time in Parallel Systems
- 原文："researchers need to ensure that the timer overhead is only a small fraction (we suggest <5%) of the measurement interval."
- 要点：读计时器本身有开销，要确保它只占测量区间的一小部分（建议小于 5%），计时精度也要足够。

### E14

- 位置：§5.1，Rule 11
- 原文："If possible, show upper performance bounds to facilitate interpretability of the measured results."
- 要点：可能的话，给出性能上限（如理论峰值），帮助读者理解测量结果。

### E15

- 位置：§5.2，Rule 12
- 原文："Plot as much information as needed to interpret the experimental results. Only connect measurements by lines if they indicate trends and the interpolation is valid."
- 要点：图中画出解读结果所需的信息；只有表示趋势且插值合理时，才用线连接测量点。

### E16

- 位置：摘要
- 原文："Our investigation of a stratified sample of 120 papers across three top conferences in the field shows that the state of the practice is lacking."
- 要点：对 120 篇顶会论文的调查表明，性能报告的现状有欠缺，例如常常说不清改进是确定的还是偶然观察到的。

### E17

- 位置：§4.2.2 Number of Measurements
- 原文："We now show how the CI can be used to compute the number of measurements needed to achieve a specified error certainty in the result."
- 要点：可以用置信区间反推需要多少次测量，才能达到预定的误差范围。
