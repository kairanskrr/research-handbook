# 系统

> 本页只写这个方向特有的做法；通用做法见主线和研究套路，计算机共通的规矩（会议流程、双盲与预印本、制品评估与徽章）见[计算机学科概况](../README.md)。

## 这个方向研究什么

系统方向研究计算机系统软件怎样设计、实现和运行。以 SOSP 2025（Symposium on Operating Systems Principles，ACM 操作系统原理研讨会；ACM 即美国计算机协会）的征稿为例，范围包括操作系统、文件和存储系统、分布式系统、云计算、移动和边缘系统、安全可靠的系统、大数据和机器学习的系统问题等[^sosp2025cfp-e9]。

几个典型问题 `[本项目分析]`：

- 一种新的存储或调度设计，能把延迟、吞吐量或资源开销改进多少，代价是什么？
- 一个已经大规模部署的系统，运行中暴露了什么问题，学到了什么经验？
- 一个系统能否被证明正确？例如 seL4 团队对一个操作系统内核做了从抽象规约到 C 实现的机器检查验证[^klein2009sel4-e8]，论文发表在 SOSP 2009。

**"造一个东西，再用实验说明它好"是常见形态。** OSDI 2026（Operating Systems Design and Implementation，USENIX 操作系统设计与实现研讨会）的征稿写得很直白：好论文要提出重要问题，给出有说服力的方案，并证明方案实用、有好处[^osdi2026cfp-e2]。SOSP 2025 还要求把方案**实现**出来，并让更广的系统社区读得懂[^sosp2025cfp-e2]。

## 主要发表处和节奏

系统方向的主要成果发表在会议上；OSDI 和 SOSP 是本页资料中的两个例子 `[本项目分析]`。下表是它们**各自某一年**的规则，不是整个方向的惯例。**规则每年都会变，投稿前以当年的征稿启事为准。**

| | OSDI 2026 | SOSP 2025 |
|---|---|---|
| 看重什么 | 创新研究，以及量化的或有洞见的设计和实现经验[^osdi2026cfp-e1] | 开拓新领域、延续重要的研究对话，或反思最先进实现的经验和测量[^sosp2025cfp-e1] |
| 篇幅 | 最多 12 页；注水会被压分，6 页及以下难获充分考虑[^osdi2026cfp-e3] | 技术内容最多 12 页，参考文献不计[^sosp2025cfp-e5] |
| 审稿轨道 | 研究轨道和"运行系统"轨道[^osdi2026cfp-e4] | 本文资料未涉及 |
| 作者回复 | 取消[^osdi2026cfp-e5] | 有，但不能加新实验或数据[^sosp2025cfp-e4] |
| 录用方式 | 有条件录用，取代了修改重投[^osdi2026cfp-e5] | 先有条件录用，指导人认可修改后才最终录用[^sosp2025cfp-e7] |
| 系统名匿名 | 要换一个匿名的名字[^osdi2026cfp-e6] | 名字已公开过的，必须换[^sosp2025cfp-e8] |

表里几格的展开，同样只属于标出的那一年：

- **OSDI 2026 的有条件录用**：作者不完成委员会规定的修改，仍会被拒[^osdi2026cfp-e8]。
- **OSDI 2026 的"运行系统"轨道**：写已部署系统的设计、实现、分析和经验[^osdi2026cfp-e4]。
- **SOSP 2025 的作者回复**：只能纠正审稿中的事实错误，或直接回答审稿人的问题；也不能描述投稿后新做的工作、承诺后续工作[^sosp2025cfp-e4]。
- **OSDI 2026 的预印本**：允许先通过技术报告、报告、社交媒体等公开，但投稿里的项目或系统名要和公开时用的不同[^osdi2026cfp-e6]。

几点要注意 `[本项目分析]`：

- **系统名字也要匿名。** 系统论文常以系统名称呼工作，发过预印本或做过报告的，投稿时要改名。SOSP 2025 还要求：报告本单位系统的经验时，系统名匿名，但要描述读者理解工作所需的特征，如用户规模、请求量[^sosp2025cfp-e6]。
- **补充材料不一定有人读。** OSDI 2026 写明审稿人不必读补充材料，论文必须自成一体[^osdi2026cfp-e7]。
- **新方向和老方向的标准不一样。** SOSP 2025 鼓励开创新方向的工作，并承认研究新问题的论文，评价标准可能不同于延续成熟方向的论文[^sosp2025cfp-e3]。

**制品评估在系统方向很普遍。** 参与比例、评估时间和徽章的含义见[计算机学科概况：制品评估与徽章](../README.md#制品评估与徽章)。SOSP 2025 也鼓励录用论文通过制品评估提供源代码和原始数据[^sosp2025cfp-e7]。以 OSDI 2024 为例，录用到提交制品之间时间很短，会议建议论文还在审时就开始准备[^sysartifactsguide-e2]；打包的做法见学科概况的[给新手的建议](../README.md#给新手的建议)第 3 条。

## 常用套路与证据标准

下表的分组和概括是本项目的归纳，每条标准只代表脚注里那篇文献或那个会议 `[本项目分析]`。

| 套路 | 在这个方向的样子 | 证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../../05_research-strategies/build_improve.md) | 新的操作系统、存储、分布式或云系统 | 关心的地方明显变好，其他地方没有明显变差[^heiserbenchmarking-e3]；和最先进方案比[^heiserbenchmarking-e16] | [工程研究](../practices/engineering_research.md) |
| [比较评估](../../../05_research-strategies/compare_evaluate.md) | 用基准套件和真实负载测性能 | 不挑子集[^heiserbenchmarking-e4]；用代表真实负载的宏基准[^heiserbenchmarking-e7]；对手同样认真配置[^heiserbenchmarking-e15] | [基准评测](../practices/benchmarking.md) |
| [测量](../../../05_research-strategies/measure.md) | 测量本身靠不靠得住 | 提升可能落在测量误差之内[^kalibera2013rigorous-e2]；环境变量大小、链接顺序会造成偏差[^kalibera2013rigorous-e3] | [基准评测：设计测量流程](../practices/benchmarking.md#第四步设计测量流程) |
| [观察描述](../../../05_research-strategies/observe_describe.md) | 已部署系统的经验报告和测量 | OSDI 2026 欢迎推翻或加强已有假设、在新规模或新环境下验证已知技术的工作[^osdi2026cfp-e4] | [案例研究](../../../06_methods/case_study.md) |
| [证明](../../../05_research-strategies/prove.md) | 系统的形式化验证 | 写清证明依赖的假设[^klein2009sel4-e1]；规约本身对不对，证明管不了[^klein2009sel4-e2] | [证明：什么样的证据才够](../../../05_research-strategies/prove.md#2-什么样的证据才够) |

怎么用这张表 `[本项目分析]`：很多系统论文以构建改进为主，评估部分按比较评估和测量的标准写；有形式化验证的，再加上证明的要求。

## 这个方向特有的规矩

**性能评测有一份"罪行"清单。** Heiser 根据审稿经验，整理了系统论文常见的评测错误，并称之为"罪行"，因为它们破坏科学过程的诚信[^heiserbenchmarking-e1]。完整的步骤和例子见[基准评测](../practices/benchmarking.md#2-怎么做)，这里只列系统论文最常被追问的几条：

- **不要选择性评测。** 用有偏的一组基准"证明"观点，是所有评测错误之母[^heiserbenchmarking-e2]。只跑一部分时，每个缺失的程序都要有令人信服的理由；用了子集，就不能报整个套件的总体指标[^heiserbenchmarking-e4]。
- **代价也要测出来。** 公平的评估要同时证明两点：关心的地方性能明显提升；其他地方没有明显下降[^heiserbenchmarking-e3]。
- **选对基线。** 基线常常是最先进的方案，也可以是理论最优或硬件极限[^heiserbenchmarking-e13]。新的最先进方案出来后，它就是必须用的新基线[^heiserbenchmarking-e16]。
- **吞吐量下降不等于开销。** 比较吞吐量时，必须同时比较完整的处理器负载[^heiserbenchmarking-e8]。
- **报波动，报绝对数。** 至少报告标准差[^heiserbenchmarking-e10]；给完整结果，不只给比值[^heiserbenchmarking-e19]。
- **把实验平台写全。** 可能影响结果的平台特征都要写，编译器和其他工具的版本也常常相关[^heiserbenchmarking-e17]。

**多跑几次不等于重复得对。** 系统性能受很多你没注意到的因素影响 `[本项目分析]`。Kalibera 和 Jones 的建议：

- 不受你控制、又恰好在整个实验中固定不变的因素会造成偏差；先把它们变成受控的或随机的，例如随机化链接顺序[^kalibera2013rigorous-e5]。
- 至少要在有随机变化的最高层次上重复，例如重新编译、重新启动程序，而不只是一次运行里多循环几轮[^kalibera2013rigorous-e6]。
- 用效应量的置信区间报告性能变化，同时给出变化多大、误差多大、有多确定[^kalibera2013rigorous-e8]。

**并行和高性能计算还有一份规则清单。** Hoefler 和 Belli 针对并行计算系统给出了一套性能报告规则，例如永远不要只报比值而不报绝对值[^hoefler2015scientific-e2]、可能的话给出性能上限[^hoefler2015scientific-e14]。怎样把多个基准的分数汇总成一个数，他们和 Heiser 的说法不同[^heiserbenchmarking-e11][^hoefler2015scientific-e4]，两种做法见[基准评测](../practices/benchmarking.md#第五步分析结果)。

**这些规矩也用在系统安全上。** 安全方向的防御论文常要报性能开销，评测缺陷的调查见[安全](security.md)。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只测对自己有利的场景 | 还要证明其他地方没有明显变差，否则是欺骗[^heiserbenchmarking-e3] |
| 只和自己去年的系统比 | 要和公认的标准比[^heiserbenchmarking-e14] |
| 自己的系统调到最好，对手用默认配置 | 对手也要花同样的功夫；拿不准就联系对手作者[^heiserbenchmarking-e15] |
| 用微基准的结果说整体性能 | 要用代表真实负载的宏基准[^heiserbenchmarking-e7] |
| 只给加速比，不给绝对性能 | 违反"不只报比值"的规则[^hoefler2015scientific-e2][^heiserbenchmarking-e19] |
| 不报波动，提升只有几个百分点 | 提升可能落在测量误差之内[^kalibera2013rigorous-e2] |
| 只在一种编译和链接设置下测 | 环境变量大小、链接顺序都可能造成偏向某个系统的偏差[^kalibera2013rigorous-e3] |
| 投稿里沿用已公开的系统名 | OSDI 2026、SOSP 2025 都要求换名字[^osdi2026cfp-e6][^sosp2025cfp-e8] |
| 把关键实验放进补充材料 | OSDI 2026 的审稿人不必读补充材料[^osdi2026cfp-e7] |
| 在 SOSP 的作者回复里补新实验 | SOSP 2025 明确不允许[^sosp2025cfp-e4] |
| 录用后才开始整理制品 | 录用到提交制品之间时间很短[^sysartifactsguide-e2] |

## 延伸阅读

- **你要投的会议当年的征稿启事和制品征集**，例如 OSDI、SOSP。每次投稿前都要重新读。
- **Heiser，Systems Benchmarking Crimes**（网页）：系统论文常见评测错误的清单，写评估部分前逐条对照。
- **Hoefler 和 Belli 2015，Scientific Benchmarking of Parallel Computing Systems**：一套性能报告规则，做并行和高性能计算的人必读。
- **Kalibera 和 Jones 2013，Rigorous Benchmarking in Reasonable Time**：怎样安排重复实验、怎样用置信区间报告性能变化。
- **Klein 等人 2009，seL4: Formal Verification of an OS Kernel**：想了解系统形式化验证的代价和收获时读。
- 相关方向：[安全](security.md)、[程序语言](programming_languages.md)、[理论](theory.md)。

[^sosp2025cfp-e9]: SOSP 2025 征稿启事，开头。[证据](../../../../sources/notes/sosp2025cfp.md#e9)
[^klein2009sel4-e8]: Klein 等人 2009，摘要。[证据](../../../../sources/notes/klein2009sel4.md#e8)
[^osdi2026cfp-e2]: OSDI '26 征稿启事，Submitting a Paper。[证据](../../../../sources/notes/osdi2026cfp.md#e2)
[^sosp2025cfp-e2]: SOSP 2025 征稿启事，Submission Criteria。[证据](../../../../sources/notes/sosp2025cfp.md#e2)
[^osdi2026cfp-e1]: OSDI '26 征稿启事，开头。[证据](../../../../sources/notes/osdi2026cfp.md#e1)
[^sosp2025cfp-e1]: SOSP 2025 征稿启事，开头。[证据](../../../../sources/notes/sosp2025cfp.md#e1)
[^osdi2026cfp-e3]: OSDI '26 征稿启事，Deadline and Submission Instructions。[证据](../../../../sources/notes/osdi2026cfp.md#e3)
[^sosp2025cfp-e5]: SOSP 2025 征稿启事，格式要求。[证据](../../../../sources/notes/sosp2025cfp.md#e5)
[^osdi2026cfp-e4]: OSDI '26 征稿启事，Submission Tracks。[证据](../../../../sources/notes/osdi2026cfp.md#e4)
[^osdi2026cfp-e5]: OSDI '26 征稿启事，开头（本届主要变化）。[证据](../../../../sources/notes/osdi2026cfp.md#e5)
[^sosp2025cfp-e4]: SOSP 2025 征稿启事，Author Response Period。[证据](../../../../sources/notes/sosp2025cfp.md#e4)
[^sosp2025cfp-e7]: SOSP 2025 征稿启事，录用。[证据](../../../../sources/notes/sosp2025cfp.md#e7)
[^osdi2026cfp-e6]: OSDI '26 征稿启事，Submitting a Paper。[证据](../../../../sources/notes/osdi2026cfp.md#e6)
[^sosp2025cfp-e8]: SOSP 2025 征稿启事，Anonymity。[证据](../../../../sources/notes/sosp2025cfp.md#e8)
[^osdi2026cfp-e8]: OSDI '26 征稿启事，有条件录用。[证据](../../../../sources/notes/osdi2026cfp.md#e8)
[^sosp2025cfp-e6]: SOSP 2025 征稿启事，Anonymity。[证据](../../../../sources/notes/sosp2025cfp.md#e6)
[^osdi2026cfp-e7]: OSDI '26 征稿启事，补充材料。[证据](../../../../sources/notes/osdi2026cfp.md#e7)
[^sosp2025cfp-e3]: SOSP 2025 征稿启事，Submission Criteria。[证据](../../../../sources/notes/sosp2025cfp.md#e3)
[^sysartifactsguide-e2]: sysartifacts，OSDI '24 Call for Artifacts，Overview。[证据](../../../../sources/notes/sysartifactsguide.md#e2)
[^heiserbenchmarking-e3]: Heiser，Not evaluating potential performance degradation。[证据](../../../../sources/notes/heiserbenchmarking.md#e3)
[^heiserbenchmarking-e16]: Heiser，Inflating gains by not comparing against the state of the art。[证据](../../../../sources/notes/heiserbenchmarking.md#e16)
[^heiserbenchmarking-e4]: Heiser，Benchmark sub-setting without strong justification。[证据](../../../../sources/notes/heiserbenchmarking.md#e4)
[^heiserbenchmarking-e7]: Heiser，Pretending micro-benchmarks represent overall performance。[证据](../../../../sources/notes/heiserbenchmarking.md#e7)
[^heiserbenchmarking-e15]: Heiser，Unfair benchmarking of competitors。[证据](../../../../sources/notes/heiserbenchmarking.md#e15)
[^kalibera2013rigorous-e2]: Kalibera & Jones 2013，§1。[证据](../../../../sources/notes/kalibera2013rigorous.md#e2)
[^kalibera2013rigorous-e3]: Kalibera & Jones 2013，§2。[证据](../../../../sources/notes/kalibera2013rigorous.md#e3)
[^klein2009sel4-e1]: Klein 等人 2009，§1。[证据](../../../../sources/notes/klein2009sel4.md#e1)
[^klein2009sel4-e2]: Klein 等人 2009，§4.5。[证据](../../../../sources/notes/klein2009sel4.md#e2)
[^heiserbenchmarking-e1]: Heiser，Benchmarking Crimes 开头。[证据](../../../../sources/notes/heiserbenchmarking.md#e1)
[^heiserbenchmarking-e2]: Heiser，Selective benchmarking。[证据](../../../../sources/notes/heiserbenchmarking.md#e2)
[^heiserbenchmarking-e13]: Heiser，No proper baseline。[证据](../../../../sources/notes/heiserbenchmarking.md#e13)
[^heiserbenchmarking-e8]: Heiser，Throughput degraded by x% ⇒ overhead is x%。[证据](../../../../sources/notes/heiserbenchmarking.md#e8)
[^heiserbenchmarking-e10]: Heiser，No indication of significance of data。[证据](../../../../sources/notes/heiserbenchmarking.md#e10)
[^heiserbenchmarking-e19]: Heiser，Relative numbers only。[证据](../../../../sources/notes/heiserbenchmarking.md#e19)
[^heiserbenchmarking-e17]: Heiser，Missing specification of evaluation platform。[证据](../../../../sources/notes/heiserbenchmarking.md#e17)
[^kalibera2013rigorous-e5]: Kalibera & Jones 2013，§3。[证据](../../../../sources/notes/kalibera2013rigorous.md#e5)
[^kalibera2013rigorous-e6]: Kalibera & Jones 2013，§3。[证据](../../../../sources/notes/kalibera2013rigorous.md#e6)
[^kalibera2013rigorous-e8]: Kalibera & Jones 2013，§4。[证据](../../../../sources/notes/kalibera2013rigorous.md#e8)
[^hoefler2015scientific-e2]: Hoefler & Belli 2015，§2，Rule 1。[证据](../../../../sources/notes/hoefler2015scientific.md#e2)
[^hoefler2015scientific-e14]: Hoefler & Belli 2015，§5.1，Rule 11。[证据](../../../../sources/notes/hoefler2015scientific.md#e14)
[^heiserbenchmarking-e11]: Heiser，Arithmetic mean for averaging across benchmark scores。[证据](../../../../sources/notes/heiserbenchmarking.md#e11)
[^hoefler2015scientific-e4]: Hoefler & Belli 2015，§3.1，Rule 3、4。[证据](../../../../sources/notes/hoefler2015scientific.md#e4)
[^heiserbenchmarking-e14]: Heiser，Only evaluate against yourself。[证据](../../../../sources/notes/heiserbenchmarking.md#e14)
