# Heiser：Systems Benchmarking Crimes

- 资料：`heiserbenchmarking`，[原文](https://gernot-heiser.org/benchmarking-crimes.html)
- 版本：网页，持续更新；2026-10-05 读取。
- 说明：Gernot Heiser（新南威尔士大学）根据审稿经验整理的系统论文常见基准评测错误。例子多来自操作系统方向，作者说其基本原则普遍适用。

### E1

- 位置：Benchmarking Crimes（开头）
- 原文："I call such cases benchmarking crimes. Not because you can go to jail for them (but probably should?) but because they undermine the integrity of the scientific process."
- 要点：称之为"罪行"，是因为它们破坏了科学过程的诚信。

### E2

- 位置：Selective benchmarking
- 原文："This is the mother of all benchmarking crimes: using a biased set of benchmarks to (seemingly) prove a point, which might be contradicted by a broader coverage of the evaluation space."
- 要点：选择性评测是"所有基准评测罪行之母"：用有偏的一组基准"证明"一个观点，而更全面的评测可能推翻它。

### E3

- 位置：Not evaluating potential performance degradation
- 原文："Progressive criterion: Performance actually does improve significantly in the area of interest" / "Conservative criterion: Performance does not significantly degrade elsewhere" / "If, however, you only evaluate the scenarios where your approach is beneficial, you are being deceptive."
- 要点：公平的评估要同时证明两点：关心的地方性能确实明显提升；其他地方性能没有明显下降。只评估对自己有利的场景是欺骗。

### E4

- 位置：Benchmark sub-setting without strong justification
- 原文："If a subset is used, it must be well justified. There must be convincing explanation for each missing program." / "it is totally unacceptable to quote an overall figure of merit (such as average speedup) for SPEC if a subset is used!"
- 要点：只跑套件的一部分时，要对每个缺失的程序给出令人信服的理由；用了子集，就绝不能报告整个套件的总体指标（如平均加速比）。

### E5

- 位置：Benchmark sub-setting without strong justification
- 原文："There is no such thing as a “representative” subset of SPEC" / "Note that arbitrary is not the same as random, so a random pick would be fine."
- 要点：不存在 SPEC 的"有代表性的子集"；从大量候选中挑选时，随机挑可以，"随意"挑不行。

### E6

- 位置：Selective data set hiding deficiencies
- 原文："Here the range of the input parameter is picked to make the system look good, but the range is not representative of a real workload."
- 要点：输入参数的范围被挑成让系统好看的区间，但这个区间不代表真实负载。原文例子：数据库只测到每核一个客户端，真正有意义的负载区间恰好在图的范围之外。

### E7

- 位置：Pretending micro-benchmarks represent overall performance
- 原文："Macro-benchmarks (representing real-world workloads) must be used to provide a realistic picture of overall performance."
- 要点：微基准只测系统的某个方面；要反映整体性能，必须用代表真实负载的宏基准。

### E8

- 位置：Throughput degraded by x% ⇒ overhead is x%
- 原文："Throughput comparisons must always be accompanied by a comparison of complete CPU load."
- 要点：吞吐量下降 x% 不等于开销是 x%；比较吞吐量时必须同时比较完整的处理器负载。

### E9

- 位置：Downplaying overheads
- 原文："This one is confusing percentage with percentage points" / "The original system is the baseline, and therefore must occur in the denominator when calculating relative performance."
- 要点：常见的算错方式：混淆百分比和百分点（开销从 6% 到 13% 不是"多了 7%"，而是翻了一倍多）；计算相对性能时分母必须是基线系统。

### E10

- 位置：No indication of significance of data
- 原文："In order to indicate significance, it is essential that at least standard deviations are quoted." / "If in doubt use Student's t-test to check the significance."
- 要点：至少要报告标准差；系统很确定时，可以一句话说明"所有标准差都低于 1%"；拿不准时用 t 检验检查显著性。

### E11

- 位置：Arithmetic mean for averaging across benchmark scores
- 原文："In particular the arithmetic mean has no meaning if individual benchmark scores are normalised (e.g. against a baseline system)." / "The proper way to average (i.e. arrive at a single figure of merit) is to use the geometric mean of scores"
- 要点：分数归一化（例如相对基线）后，算术平均没有意义；汇总成一个数应当用几何平均。

### E12

- 位置：Same dataset for calibration and validation
- 原文："the calibration and evaluation workloads must be different! In fact, they must be totally disjoint."
- 要点：用来校准模型的工作负载和用来评估的工作负载必须完全不重叠。

### E13

- 位置：No proper baseline
- 原文："Consider the baseline carefully. Often it is the state-of-the-art solution. Often it is the optimal (or theoretically best) solution or a hardware limit (assuming zero software overhead)."
- 要点：基线要仔细选：常常是最先进方案，也可以是理论最优解或硬件极限；比较虚拟化方案时，真正的基线是原生系统。

### E14

- 位置：Only evaluate against yourself
- 原文："I want to see the significance, and that means comparing against some accepted standard."
- 要点：只和自己去年的系统比不够，要和公认的标准比。

### E15

- 位置：Unfair benchmarking of competitors
- 原文："I'm sure you tweaked your system as well as you could, but did you really go through the same effort with the alternative?" / "If in doubt, contact the authors of that system to confirm that your measurements are fair." / "the default configuration of our open-source release had debugging enabled."
- 要点：自己的系统调到最好，对手是否也花了同样功夫？要写清对手的全部配置；结果和对手已发表数据不符时要格外小心，拿不准就联系对手作者。作者自己的系统曾被别人用默认开启调试的配置评测。

### E16

- 位置：Inflating gains by not comparing against the state of the art
- 原文："Paper X established a new state of the art, and thus the new baseline that must be used."
- 要点：X 已比旧基线快 20%，后来的 Y 比旧基线快 22%，Y 只能声称比 X 快约 2%：新的最先进方案就是必须使用的新基线。

### E17

- 位置：Missing specification of evaluation platform
- 原文："For reproducibility it is essential that the evaluation platform is well-specified, including all characteristics that may influence the results." / "Compiler versions are often also relevant, as may be the version of other tools."
- 要点：要写清可能影响结果的全部平台特征：处理器架构、核数、主频、内存、缓存、网卡；操作系统和虚拟机监控器的版本、编译器和其他工具的版本。

### E18

- 位置：Missing sub-benchmark results
- 原文："Only providing the overall score can at worst hide problems, and at best reduces the insights that can be obtained from the evaluation."
- 要点：运行基准套件时要给出每个子基准的结果；只给总分，往坏处说会掩盖问题，往好处说也减少了能得到的信息。

### E19

- 位置：Relative numbers only
- 原文："Always give complete result, not just ratios (unless the denominator is a standard figure)."
- 要点：始终给出完整结果，而不只是比值；只看比值，读者无法做合理性检查，还可能掩盖结果其实很差或无关紧要。

### E20

- 位置：Benchmarking Best Practice › General rules
- 原文："Make sure that the system is really quiescent when starting an experiment, leave enough time to ensure all previous data is flushed out." / "Make your benchmarking rig part of your regression testing suite."
- 要点：开始实验前确保系统处于空闲状态；把基准测试装置纳入回归测试。

### E21

- 位置：Benchmarking Best Practice › Test data and results
- 原文："Always verify the data you are transferring." / "Invert the order of measurements. This helps to identify interference between measurements."
- 要点：始终检查传输的数据是否正确；把测量顺序倒过来再测一遍，可以发现测量之间的相互干扰。

### E22

- 位置：Benchmarking Best Practice › Test data and results
- 原文："Use a combination of successive and separate runs for the same data point."
- 要点：同一数据点既连续测几次、又隔开测几次，用来发现不该有的缓存效应。

### E23

- 位置：Benchmarking Best Practice › Statistics
- 原文："Always do several runs, and check the standard deviation. Watch out for abnormal variance." / "only use such selective use of data if you really know what you are doing, and also state it explicitly in your paper/report."
- 要点：始终多跑几次并检查标准差，留意异常的波动；剔除最高或最低点只能在做过正式的离群值检测之后，并在论文中明确说明。

### E24

- 位置：Benchmarking Best Practice › Timing
- 原文："Use lots of iterations in order to improve statistics and remove clock granularity." / "Run sufficient warm-up iterations which aren't timed."
- 要点：用大量迭代来改善统计并消除时钟精度的影响；先运行足够多不计时的预热迭代。

### E25

- 位置：Benchmarking of simplified simulated system
- 原文："It is therefore essential to ensure that the simulation model does not make any simplifying assumption which will impact the performance aspect you are looking for."
- 要点：不得不在仿真系统上评测时，必须确保仿真模型的简化假设不影响你要看的性能方面，并向读者说明这一点。

### E26

- 位置：Inappropriate and misleading benchmarks
- 原文："Real scalability tests would run workloads which actually communicate across processors and use system calls."
- 要点：用多份互不通信的单处理器程序测多处理器可扩展性是不合适的基准；真正的可扩展性测试要跑跨处理器通信、使用系统调用的负载。
