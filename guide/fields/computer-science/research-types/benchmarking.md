# 基准评测：用自动化、可重复的流程比较系统、工具或模型

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本文讲**基准评测**（benchmarking）：用一套标准的工作负载或任务集（叫作**基准**，benchmark），通过自动化、可重复的流程，测量并比较多个软件系统、工具或模型的表现，例如速度、可靠性、安全性或准确率。

基准评测常常是另一类研究的一部分：你提出了一个新方法或新工具（工程研究），再用基准评测证明它更好。本文的做法对两种情况都适用。"怎样选基线、怎样对待随机性和统计、怎样写效度威胁"这些各类研究共通的内容，见通用篇的[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)；本文只讲基准评测特有的部分。

**读完本文，你应该能：**

- 判断自己的问题是否适合用基准评测回答；
- 选出有代表性的基准，公平地配置每个被比较的系统；
- 设计测量流程：预热、重复、控制环境干扰；
- 用置信区间和效应量分析结果，正确地汇总多个基准的分数；
- 写出别人能复现的报告，并判断基准本身是否测到了你想测的东西；
- 认出并避开常见的"基准评测罪行"。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准这样定义：基准评测是用一个标准工具（即基准）对方法、技术或系统做**竞争性的评估和比较**[^ralph2020empirical-e143]。它有两个条件：在确定的环境中，用**自动化、可重复的流程**研究软件系统；研究的是系统在**特定工作负载或使用场景**下的表现[^ralph2020empirical-e144]。

一个基准由四部分组成[^ralph2020empirical-e147]：

1. **要测的质量**：性能、可用性、可扩展性、安全性……
2. **指标**：用什么数字量化这个质量
3. **测量方法**：这个数字怎么测
4. **工作负载**：测量时被测系统在做什么，例如运行哪些程序、处理哪些请求、回答哪些题目

在机器学习中，"基准"通常是一个数据集加一种评分方法（常叫 eval，评测集），被测对象是模型；道理相同 `[本项目分析]`。

**和相近类型的区别：**

| | 基准评测 | 工程研究 | 有人参与的实验 | 定量仿真 |
|---|---|---|---|---|
| 研究对象 | 软件系统、工具或模型本身 | 自己提出的新方法、新工具 | 人（例如使用某个工具的开发者） | 系统的模型 |
| 证据怎么来 | 在基准上自动运行并测量 | 用基准评测、实验、案例研究等方式评估新工具 | 让参与者完成任务，测量他们的表现 | 在人工环境中运行模型 |
| 典型问题 | 在负载 W 下，系统 A 和 B 谁更快、更准？ | 我的新工具解决了问题吗，比现有方法好吗？ | 用这个工具的人效率更高吗？ | 如果网络规模扩大十倍会怎样？ |

依据：SIGSOFT 基准评测标准的适用范围[^ralph2020empirical-e145]，工程研究标准[^ralph2020empirical-e160][^ralph2020empirical-e161]。

**怎么选：**

- **研究对象是软件系统本身，可以自动运行、重复测量**：用基准评测。如果结果取决于人怎么用，就要做有人参与的实验；如果研究的是系统的模型而不是系统本身，就是仿真[^ralph2020empirical-e145]。
- **你提出了新工具**：这是工程研究。工程研究必须把新工具和最先进的替代方案或基准做实证比较（或说明为什么无法比较）[^ralph2020empirical-e161]，而这一步通常就是一次基准评测[^ralph2020empirical-e160]。
- **基准评测本身也可以是贡献**：系统地比较一批现有工具，或者构建一个新基准。好的基准会成为整个领域的"指挥棒"：评测基准是研究社区的激励，突破往往和某个基准上的大幅提升联系在一起[^wei2024evals-e1]。

如果你的主要贡献是提出新方法并用基准证明它有效，见[工程研究](engineering_research.md)；其他研究类型见[领域篇目录](../../README.md#计算机领域篇)。

---

## 2. 怎么做

基准评测出错，很少是因为作者想造假，大多只是对测量不够重视[^vanderkouwe2019sok-e25]。但问题非常普遍：对安全顶会 50 篇系统防御论文的调查发现，平均每篇有五个基准评测缺陷，只有一篇一个都没有[^vanderkouwe2019sok-e1]；对 32 篇模糊测试论文的调查发现，没有一篇把评估的所有步骤都做对[^klees2018evaluating-e19]；对 120 篇并行计算顶会论文的调查也发现，性能报告的现状有欠缺[^hoefler2015scientific-e16]；2011 年以运行时间为主要指标的 90 篇编程语言和系统论文中，71 篇没有给出任何波动指标[^kalibera2013rigorous-e1]。下面按步骤写。

### 第一步：写清主张，选对指标

**怎么做：**

1. **先写清你要证明的主张**，例如"在多核服务器上，A 的吞吐量比 B 高，且内存开销不超过 10%"。怎样写清主张，见通用篇的[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)。
2. **指标要直接测你关心的东西。** 用间接指标代替（例如用缓存未命中次数代表整体性能），必须明确说明理由[^blackburn2018sigplan-e13]。
3. **把代价也测出来。** 一个改进性能的方法要同时证明两件事：关心的地方确实明显变好了；其他地方没有明显变差[^heiserbenchmarking-e3]。例如编译优化让程序变快，但可能大幅增加编译时间，编译时间也要测[^blackburn2018sigplan-e21]；只测运行时间、不测内存等其他开销，评估是不完整的[^vanderkouwe2019sok-e20]。
4. **列出所有可能受影响的维度。** 先想清楚你的方案可能影响哪些方面（处理器、并发、内存、输入输出、系统调用……），每个方面至少放一个合适的基准[^vanderkouwe2019sok-e11]。

**为什么**：只评估对自己有利的场景，Heiser 直接称之为欺骗[^heiserbenchmarking-e3]。

**容易错在哪**：指标看似合理，实际测偏了。在模糊测试（自动随机生成输入来找程序缺陷）中，许多论文用"唯一崩溃数"这类启发式指标代替真实缺陷数，而这种启发式可能大大多算缺陷，也可能漏算[^klees2018evaluating-e17]。

### 第二步：选基准，不挑子集

**怎么做：**

1. **优先用公认的标准基准，并说明为什么选它**，例如它和你的问题相关、没有过时[^ralph2020empirical-e146][^blackburn2018sigplan-e16]。要用在合适的场合：不能用单线程的基准套件研究并行性能[^blackburn2018sigplan-e16]。
2. **用非标准基准（裁剪过的或自己搭的）要给出理由和局限**，说明为什么用标准基准会更差[^blackburn2018sigplan-e17]。
3. **自建新基准**，要写清上面说的四个组成部分，说明设计理由，并尽量复用已有基准的设计[^ralph2020empirical-e147]。
4. **套件要跑全。** 能合理运行的子基准都要跑，没跑的逐个说明原因[^vanderkouwe2019sok-e17][^heiserbenchmarking-e4]。只跑了子集，就**绝不能**报告整个套件的总体分数（如"平均加速 15%"）[^heiserbenchmarking-e4]。
5. **要从大量候选中挑选时，说清怎么挑。** 例如要从上千个驱动程序里选几十个：随机挑可以，"随意"挑不行[^heiserbenchmarking-e5]。
6. **主张"对实际应用有好处"，就要在实际应用上测。** 只测某个操作的微基准（microbenchmark）不能代表整体性能，需要代表真实负载的宏基准[^blackburn2018sigplan-e20][^heiserbenchmarking-e7]。
7. **参数要覆盖真实的范围。** 关键参数要在一个范围内变化，看结果对它多敏感[^blackburn2018sigplan-e24]。Heiser 举过一个真实的例子：某数据库论文只测到每个处理器核一个客户端，吞吐量看起来随负载线性增长；但真正有意义的负载区间恰好在图的范围之外，那里的可扩展性很差[^heiserbenchmarking-e6]。如果吞吐量随并发数一直线性增长，往往说明你测的范围太窄了[^vanderkouwe2019sok-e18]。
8. **开发时用过的数据，不能再用来评估。** 用来调整、校准方法的工作负载和用来评估的工作负载必须完全不重叠[^heiserbenchmarking-e12]。例如一个静态分析工具，不能只在开发时参考过的程序上评估[^blackburn2018sigplan-e26]。
9. **结果依赖输入的领域，多用几组输入。** 在模糊测试中，AFLFast（一种模糊测试工具）在原论文选的目标程序上表现很好，换成其他论文用的两个目标，就并不比 AFL 好[^klees2018evaluating-e18]。在机器学习中，用多个数据集评估模型更可靠[^lones2021avoid-e17]。

**为什么**：用有偏的一组基准"证明"一个观点，而更全面的评测可能推翻它，这是"所有基准评测罪行之母"[^heiserbenchmarking-e2]。它也最常见：上面那项安全论文调查中，69% 的论文无正当理由地裁剪了基准套件[^vanderkouwe2019sok-e15]。

**容易错在哪**：

- 写"我们挑了有代表性的子集""这里展示典型结果"。Heiser 的回答是：SPEC CPU（标准性能评估公司 Standard Performance Evaluation Corporation 发布的处理器基准套件）不存在"有代表性的子集"[^heiserbenchmarking-e5]。
- 为自己的方法量身定做基准，或用和问题无关的基准实验掩盖方法的弱点。SIGSOFT 标准把这两种都列为反面模式[^ralph2020empirical-e157]。

> **不同的看法：标准基准会不会让大家"刷榜"？**
> - SIGPLAN（美国计算机协会程序设计语言分会）清单的作者听到过这种担忧：用标准基准可能让研究过拟合到基准上。但他们的经验是，编程语言领域更常见的是相反的问题：裁剪基准、挑选特定程序[^blackburn2018sigplan-e18]。
> - Lones 提醒，在机器学习中，整个社区反复在同一个测试集上比较模型，最好的那个可能只是碰巧过拟合了这个测试集[^lones2021avoid-e15]。
>
> 实际操作中 `[本项目分析]`：两种风险都存在，侧重点因方向而异。系统、编程语言方向，首先要防止挑子集；机器学习方向，还要警惕社区对测试集的过拟合：多用几个数据集，不要把公开基准上的小幅提升看得太重[^lones2021avoid-e15][^lones2021avoid-e17]。

### 第三步：选被比较的系统，公平地配置每一个

基线怎么选、为什么要和强基线比，通用篇已经讲过。基准评测里还要特别注意下面几点。

**选对基线：**

- **想清楚"基线"到底是什么。** 常常是最先进的方案；也可以是理论最优解或硬件极限；有时是"没被改动过的系统"。例如比较两种虚拟化方案，真正的基线是不用虚拟化的原生系统[^heiserbenchmarking-e13]。在系统安全研究中，正确的基线通常是使用默认设置、不开防御的原系统；不要给基线加非默认的编译选项或模拟手段，把基线拖慢、把开销藏进基线里[^vanderkouwe2019sok-e19]。
- **不能只和自己的旧版本比**，要和公认的标准比[^heiserbenchmarking-e14]。
- **最先进的方案变了，基线就要跟着变。** 论文 X 已经比旧基线快 20%，后来的论文 Y 比旧基线快 22%，Y 只能说自己比 X 快约 2%[^heiserbenchmarking-e16]。

**公平地配置：**

1. **每个系统都能凭实力竞争，不受人为限制**[^ralph2020empirical-e149]。
2. **同等调优。** 你把自己的系统调到了最好，对手是否也花了同样的功夫[^heiserbenchmarking-e15]？例如对手用最低优化级别编译、自己用最高级别，就不公平[^blackburn2018sigplan-e15]。在机器学习中，一个模型用默认超参数、另一个精心调过，比较也不公平；应当把每个模型优化到同样程度[^lones2021avoid-e13][^lones2021avoid-e14]。
3. **写清对手的全部配置。** 你的结果和对手已发表的数据对不上时要格外小心；拿不准就联系对手的作者确认[^heiserbenchmarking-e15]。Heiser 自己的系统就曾被别人用开着调试功能的默认配置评测[^heiserbenchmarking-e15]。
4. **平台要和主张相符。** 关于手机性能的主张，不能只在服务器上测[^blackburn2018sigplan-e23]。
5. **方法由多个组件组成时，单独测每个组件的贡献。** 否则系统更快可能只是因为实现写得更好，而不是新设计起了作用[^vanderkouwe2019sok-e20]。

### 第四步：设计测量流程

**怎么做：**

1. **让环境安静。** 开始实验前确认系统处于空闲状态[^heiserbenchmarking-e20]；关掉可能干扰测量的系统服务[^kalibera2013rigorous-e10]。
2. **先预热，再计时。** 很多系统前几轮更慢：缓存还没装满、即时编译（运行时把热点代码编译成机器码）还没完成、连接还没建立。先跑足够多不计时的预热轮[^heiserbenchmarking-e24]，第一轮不计入平均[^hoefler2015scientific-e12]。要分清**启动性能**和**稳态性能**，两者测法不同：测启动性能，每次重新启动程序、只跑一轮；测稳态性能，每次启动后跑多轮，只收集进入稳态后的数据[^georges2007statistically-e3]。缓存是"冷"还是"热"也要想清楚，哪种更接近真实使用[^hoefler2015scientific-e12]。
3. **重复，而且在对的层次上重复。** 重复次数和运行时长要足够评估结果的稳定性[^ralph2020empirical-e150]。波动可能来自编译、每次启动、每轮迭代等不同层次；至少要在**有随机变化的最高层次**上重复，例如重新编译或重新启动程序，而不只是在一次运行里多循环几轮[^kalibera2013rigorous-e6]。需要多少次，可以先做小实验，再用置信区间反推[^hoefler2015scientific-e17]。
4. **警惕测量偏差。** 看似无关的因素可能系统性地偏向某个系统。据 Kalibera & Jones 转述，Mytkowicz 等人发现，Unix 环境变量的总大小、链接时目标文件的顺序，都会造成显著的测量偏差[^kalibera2013rigorous-e3]。办法是找出影响结果、又不受你控制的变量，把它变成受控的或随机的，例如随机化链接顺序[^kalibera2013rigorous-e5]；控制不了的环境参数，就随机化[^hoefler2015scientific-e10]。
5. **打乱顺序，交叉测量。** 同一数据点既连续测几次、又隔开测几次[^heiserbenchmarking-e22]；把测量顺序倒过来再测一遍，可以发现测量之间的相互干扰[^heiserbenchmarking-e21]。
6. **注意计时本身。** 读计时器有开销，要确保它只占测量时长的一小部分（建议小于 5%）[^hoefler2015scientific-e13]；用大量迭代消除时钟精度的影响[^heiserbenchmarking-e24]。
7. **随机算法：种子和时长都是实验参数。** 模糊测试、机器学习等方法本身带随机性。初始输入不同，模糊测试的性能差异很大，但多数论文随意选择、也不交代[^klees2018evaluating-e13]；少于 5～6 小时的超时可能给出误导的结论[^klees2018evaluating-e12]。超时设置本身就是基准的一部分[^blackburn2018sigplan-e19]。Klees 等人对模糊测试的建议是：多次试验加统计检验，至少 24 小时的超时（或说明更短的理由），并画出性能随时间的变化[^klees2018evaluating-e16]。
8. **（系统方向）负载生成器要开环。** 测服务器这类事务系统时，请求的产生速度不应受被测系统快慢的影响[^blackburn2018sigplan-e25]。
9. **检查结果是对的。** 写入磁盘或网络的数据要读回来比对[^heiserbenchmarking-e21]。快但算错了，不算快。
10. **保存全部原始数据，事后离线分析。** 只收集汇总后的数字（如平均值）是反面模式[^ralph2020empirical-e158]。

**为什么**：现代系统的性能本来就不确定，试验次数不够，就可能把噪声当成信号[^blackburn2018sigplan-e27]。计算机领域的性能提升往往不大（中位数约 10%），完全可能落在测量误差之内[^kalibera2013rigorous-e2]。

> **不同的看法：测量偏差有多严重？**
> - 据 Kalibera & Jones 转述，Mytkowicz 等人发现环境变量大小、链接顺序会造成显著偏差[^kalibera2013rigorous-e3]。
> - Kalibera & Jones 重做了实验：在小规模的训练输入上确认了链接顺序的影响，但在 SPEC 正式规模的输入上，这种变化很小[^kalibera2013rigorous-e4]。
>
> 实际操作中 `[本项目分析]`：偏差有多大取决于平台和基准，事先无法知道。在自己的环境里做一次小实验：改变环境变量、链接顺序，重启机器，看结果变化多大，再决定要随机化哪些因素、重复多少次。

### 第五步：分析结果

怎样做显著性检验、什么是效应量，见通用篇的[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)。基准评测里要注意：

1. **报告波动，不要只报最好的一次。** 现有做法五花八门：有人报多次运行的平均，有人报最好的一次，有人报最差的一次[^georges2007statistically-e1]。只报 30 次中最好的一次，可能得出"一个垃圾回收器明显更快"的结论；看置信区间，两者其实重叠，差异很可能只是随机波动[^georges2007statistically-e2]。置信区间能帮你判断差异是随机波动还是真实差异[^georges2007statistically-e4]。测量值不确定时，报告置信区间[^hoefler2015scientific-e5]，只报平均数或中位数会误导读者[^blackburn2018sigplan-e8]；至少报告标准差。系统很稳定时，一句"所有标准差都低于 1%"也可以[^heiserbenchmarking-e10]。
2. **不要想当然地假设正态分布**，先检查[^hoefler2015scientific-e6]。比较两个系统时，用统计上可靠的方法，例如看置信区间是否重叠，或做方差分析[^hoefler2015scientific-e7]。比较随机化算法时，可以用 Mann-Whitney U 检验，它不对分布做假设[^klees2018evaluating-e14]。
3. **说清"好多少"，不只是"是否更好"**[^klees2018evaluating-e15]。Kalibera & Jones 建议用效应量的置信区间报告，例如"有 95% 的把握认为 A 比 B 快 5.5% ± 2.5%"[^kalibera2013rigorous-e8]。加速比再大，也应估计测量误差[^kalibera2013rigorous-e9]。
4. **想清楚该报哪个统计量。** 关心最坏情况延迟时，平均数和中位数都不够，要报更高的百分位数[^hoefler2015scientific-e8]。
5. **相对数要算对**：
   - 分母必须是基线。基线 60 秒、新系统 45 秒，应说"快了 25%"，不能说"原系统慢 33%"[^heiserbenchmarking-e9]。
   - 分清百分比和百分点。开销从 6% 涨到 13%，不是"多了 7%"，而是翻了一倍多[^heiserbenchmarking-e9]；从 10% 到 20% 是多了 100%[^vanderkouwe2019sok-e24]。
   - （系统方向）吞吐量下降 x% 不等于开销是 x%。处理器没跑满时，额外开销会被空闲时间吸收；比较吞吐量时必须同时比较处理器负载[^heiserbenchmarking-e8]。
6. **精度别超过误差。** 误差是正负 1%，就不要报"49.9%"[^blackburn2018sigplan-e30]。

> **不同的看法：显著性检验还是效应量？**
> - Klees 等人认为评估应当用统计检验确认改进不是偶然[^klees2018evaluating-e10]，再估计效应量[^klees2018evaluating-e15]；Heiser 建议拿不准时用 t 检验[^heiserbenchmarking-e10]。
> - Kalibera & Jones 认为计算机实验很容易产生大量样本，样本一大，再小的差异也会"显著"，显著性检验混淆了样本量和实际意义；他们主张直接报告效应量的置信区间[^kalibera2013rigorous-e7][^kalibera2013rigorous-e8]。
>
> 实际操作中 `[本项目分析]`：两者可以一起报。用置信区间说清差异有多大、有多确定；需要时再用检验说明差异不太可能来自偶然。不要只写"显著"两个字。

> **不同的看法：怎样把多个基准的结果汇总成一个数？**
> - Heiser、van der Kouwe 等人：分数归一化（例如除以基线）之后，算术平均没有意义，应当用几何平均[^heiserbenchmarking-e11][^vanderkouwe2019sok-e22]。
> - Hoefler & Belli：尽量不要对比值求平均，而是汇总比值背后的成本（如运行时间，用算术平均）或速率（如每秒处理量，用调和平均）；只有拿不到这些时才用几何平均[^hoefler2015scientific-e4]。
> - SIGPLAN 清单：几何平均只用于量程不同的数值，速率用调和平均，有离群值时给中位数[^blackburn2018sigplan-e28]。
>
> 实际操作中：不管用哪种，都写明用的是哪种平均、为什么，并同时给出每个子基准的结果[^heiserbenchmarking-e18]。

### 第六步：写报告

**怎么做：**

1. **写清平台和软件。** 硬件：处理器型号、核数、主频、内存大小、缓存，涉及网络时写网卡和交换机；软件：操作系统、虚拟机监控器、编译器和其他工具的版本[^heiserbenchmarking-e17]。所有参数都要写，包括默认值[^blackburn2018sigplan-e22]。只写"在某某超级计算机上运行"不够，系统会升级，别人也不一定知道它的参数[^hoefler2015scientific-e11]。所有变化的因素和取值都要记录[^hoefler2015scientific-e9]。这几项最容易补上：手头已有，写进去就行[^vanderkouwe2019sok-e21]。
2. **给出每个子基准的结果**，不只是总分。只给总分，坏的情况会掩盖问题，好的情况也损失了信息[^heiserbenchmarking-e18]。
3. **给出绝对数，不只是比值。** 只看比值，读者没法做合理性检查[^heiserbenchmarking-e19]；报加速比时，要给出基准情形的绝对性能[^hoefler2015scientific-e2]。基线慢时开销会显得更小，绝对数能让读者看出这一点[^vanderkouwe2019sok-e23]。
4. **报告全部结果，不只是最好的**[^hoefler2015scientific-e3]。不要把 4%、6%、7%、49% 概括成"最高提升 49%"，要报告完整分布[^blackburn2018sigplan-e9]。剔除离群值要先做正式的检测，并在论文中写明[^heiserbenchmarking-e23]。
5. **可能的话，给出性能上限**（例如硬件的理论峰值），帮助读者判断结果离"天花板"有多远[^hoefler2015scientific-e14]。
6. **图要画得诚实。** 坐标轴不从零开始会夸大差异；比值（如加速比）应画在对数坐标上，否则 2.0 和 0.5 看起来不对称[^blackburn2018sigplan-e29]。只有表示趋势时才把测量点连成线[^hoefler2015scientific-e15]。
7. **如实报告运行中遇到的问题**，例如某些基准崩溃或超时[^ralph2020empirical-e152]。

**为什么**：即使别人无法完全复现你的实验（例如用的是独一无二的超级计算机），报告也应当提供足够的信息，让读者理解实验、得出自己的结论、判断结论有多确定[^hoefler2015scientific-e1]。

### 第七步：公开制品，让别人能复现

1. **公开补充材料**：数据、分析脚本；如果是新基准，还要有详细文档[^ralph2020empirical-e151]。理想情况下公开实验的源代码，至少公开输入数据和生成它们的程序[^hoefler2015scientific-e9]。
2. **让基准能直接用起来**，方便别人独立复现；尽量使用或创建开源基准[^ralph2020empirical-e151][^ralph2020empirical-e152]。
3. **把基准测试装置纳入回归测试**[^heiserbenchmarking-e20]。这样每次改代码都能重跑一遍，及早发现性能变化 `[本项目分析]`。
4. 很多计算机会议设有**制品评审**（artifact evaluation）：论文接收后，检查论文中的主张和证据与提交的代码、数据是否一致[^blackburn2018sigplan-e31]。按能通过制品评审的标准准备材料。

怎样组织代码、数据和结果，让每个数字都能追溯，见通用篇的[整理科研材料](../../../general/2_during/03_organizing_materials.md)。

---

## 3. 基准本身有效吗

前面讲的是"怎样用好一个基准"。还有一个更根本的问题：**这个基准测到了你想测的东西吗？** SIGSOFT 标准把它列为必须讨论的内容，叫构造效度（construct validity）[^ralph2020empirical-e100]。总体要求是：测量公平，重复实验能得到一致的结果，测的是"对的"方面，基准真实、工作负载有代表性[^ralph2020empirical-e155]。van der Kouwe 等人的说法类似：评估要完整（验证所有声称的贡献，也展示负面影响有多大），要可靠（每个数字都以合理的精度和可重复性测到了想测的东西），还要相关、可复现[^vanderkouwe2019sok-e16]。

**常见的"测错了东西"：**

- **基准和主张不对应。** 用多份互不通信的单处理器程序测多处理器可扩展性，这些程序几乎不做系统调用、也不跨处理器通信，本来就该线性扩展；真正的可扩展性测试要跑跨处理器通信、使用系统调用的负载[^heiserbenchmarking-e26]。
- **在简化的仿真系统上测。** 不得不用仿真时，必须确保仿真模型的简化假设不影响你要看的那个性能方面，并向读者说明[^heiserbenchmarking-e25]。
- **指标是启发式的替代品。** 见第一步模糊测试的例子。合成的基准套件（人为植入已知缺陷的程序集）的好处是独立于具体算法定义、缺陷能可靠计数[^klees2018evaluating-e18]。

**（机器学习方向）好的评测集是什么样的。** Jason Wei 从大语言模型研究者的角度总结过[^wei2024evals-e12]：

- 样本足够多，最好至少 1000 个，否则结果噪声大[^wei2024evals-e2]；
- 质量高，标准答案的错误要少[^wei2024evals-e3]，评分要极其准确[^wei2024evals-e7]；
- 有一个单一数字的指标[^wei2024evals-e4]，运行起来不费事[^wei2024evals-e5]；
- 任务本身有意义[^wei2024evals-e6]，而且不会太快被"做满"[^wei2024evals-e8]。

还要注意：提示词怎么写、答案怎么解析，都会影响分数[^wei2024evals-e11]；让人两两比较模型输出的评测，不确定到底测的是什么，例如风格占了多大比重[^wei2024evals-e10]。

**（机器学习方向）数据污染。** 最严重的数据污染是：大语言模型训练时见过某个基准的测试集，又在同一基准上评测[^sainz2023nlp-e1]。这会高估模型的表现[^sainz2023nlp-e2]。污染程度不同，后果也不同：模型见过评测集的标注，实验完全无效；只见过训练集，不影响和用同样数据开发的模型比较，但"零样本""少样本"的结论不再成立[^sainz2023nlp-e3]。好的评测发布后，题目会扩散到网上各处[^wei2024evals-e9]；用基础模型时，它的训练数据可能已经包含了社区基准的测试集[^lones2021avoid-e16]。

怎么办：

- 训练数据公开的模型，检查基准有多大比例能在训练数据里找到[^sainz2023nlp-e4]；不公开的，可以看模型能否逐字背出基准中的样本[^sainz2023nlp-e5]。
- 构建评测集时，同时准备公开和私有两份测试集，监测模型在两者上的表现是否明显不同[^wei2024evals-e9]。
- 报告时写明是否检查过污染、怎么检查的；尽量使用模型训练之后才产生的数据 `[本项目分析]`。

**新基准不必一开始就很流行。** "这个基准用的人不多""没有独立组织维护""没有独立复现"都不是成立的批评：一小组研究者先做出的"原型基准"，本身就可以推动讨论、启动共识[^ralph2020empirical-e159]。

---

## 4. 检查清单

下面主要依据 SIGSOFT 基准评测标准，并用 SIGPLAN 清单、Heiser 和 van der Kouwe 等人的建议补充。

**必须做到**

- [ ] 选用现有基准时说明理由；自建新基准时写清要测的质量、指标、测量方法和工作负载，并说明设计理由[^ralph2020empirical-e146][^ralph2020empirical-e147]
- [ ] 实验环境和工作负载描述到足以让别人独立复现[^ralph2020empirical-e148]
- [ ] 每个被比较的系统都能凭实力竞争，没有人为限制[^ralph2020empirical-e149]
- [ ] 重复次数和运行时长足够评估结果稳定性[^ralph2020empirical-e150]
- [ ] 讨论构造效度：基准是否测到了要测的东西[^ralph2020empirical-e100]
- [ ] 披露主要局限[^ralph2020empirical-e103]
- [ ] 给出波动指标（标准差或置信区间），写明跨基准的平均方法，写明硬件平台和软件版本[^vanderkouwe2019sok-e21]
- [ ] 套件跑全，或逐个说明没跑的原因；用了子集就不报总分[^vanderkouwe2019sok-e17][^heiserbenchmarking-e4]

**做到更好**

- [ ] 提供补充材料：数据集、分析脚本，新基准的详细文档[^ralph2020empirical-e151]
- [ ] 以可直接使用的形式提供基准[^ralph2020empirical-e151]
- [ ] 使用或创建开源基准[^ralph2020empirical-e152]
- [ ] 如实报告运行基准时遇到的问题[^ralph2020empirical-e152]
- [ ] 报告结果被独立复现过、基准有较大的使用者社区、有独立组织维护[^ralph2020empirical-e153]

**做得出色**

- [ ] 用实证证据（例如系统综述）说明基准的相关性[^ralph2020empirical-e154]
- [ ] 用实证证据（例如行动研究、案例研究）说明基准好用[^ralph2020empirical-e154]

**这些情况可以不做，不算缺陷**[^ralph2020empirical-e156]

- 基准需要特殊硬件（例如量子计算机），别人难以复现
- 复现已发表工作时，实验环境可以简述
- 已有研究表明一次运行就够时，可以只跑一次或几次

**审稿时常见、但不成立的批评**[^ralph2020empirical-e159]：你不必为此担心

- "这个基准用的人不多"
- "没有报告独立复现的结果"
- "没有独立组织维护这个基准"

---

## 5. 常见错误

这些错误常被称为"基准评测罪行"（benchmarking crimes）：叫"罪行"，是因为它们破坏了科学过程的诚信[^heiserbenchmarking-e1]。

| 错误 | 为什么是问题 |
|---|---|
| 只跑基准套件的一部分，还报总分 | 没跑的可能正是表现差的，总分失去意义[^heiserbenchmarking-e4][^vanderkouwe2019sok-e17] |
| 只测对自己有利的场景，不测代价 | 看不到其他地方是否变差[^heiserbenchmarking-e3][^vanderkouwe2019sok-e20] |
| 参数范围只取让系统好看的区间 | 真正有意义的负载可能在范围之外[^heiserbenchmarking-e6] |
| 用微基准代表整体性能 | 只测了一个操作，不代表真实负载[^heiserbenchmarking-e7] |
| 校准和评估用同一批数据 | 只能说明模型拟合了已有数据，说明不了预测能力[^heiserbenchmarking-e12] |
| 对手用默认配置，自己精心调优 | 比较不公平，夸大了优势[^heiserbenchmarking-e15][^lones2021avoid-e13] |
| 基线被拖慢，或只和自己的旧版本比 | 开销被藏进基线，或缺少公认的参照[^vanderkouwe2019sok-e19][^heiserbenchmarking-e14] |
| 只跑一次，或只报最好的一次 | 可能把随机波动当成真实差异[^klees2018evaluating-e11][^georges2007statistically-e2] |
| 不给标准差或置信区间 | 读者无法判断差异是否只是噪声；这是最常见的缺陷[^vanderkouwe2019sok-e15] |
| 对归一化的分数求算术平均 | 结果取决于选谁作基线，没有意义[^heiserbenchmarking-e11][^vanderkouwe2019sok-e22] |
| 混淆百分比和百分点，或分母选错 | 把翻倍的开销说成"多了 7%"[^heiserbenchmarking-e9] |
| 只报比值，不报绝对数 | 读者无法做合理性检查[^heiserbenchmarking-e19][^vanderkouwe2019sok-e23] |
| 不写平台、软件版本和参数 | 别人无法复现，也无法比较[^heiserbenchmarking-e17][^blackburn2018sigplan-e22] |
| 只保存汇总后的数字 | 事后无法重新分析或核查[^ralph2020empirical-e158] |
| （机器学习）不检查测试集是否被模型见过 | 数据污染会高估表现，甚至让实验无效[^sainz2023nlp-e2][^sainz2023nlp-e3] |

---

## 6. 延伸阅读

- **一份可直接对照的错误清单**：Heiser 的 Systems Benchmarking Crimes 网页，每条都有例子，最后还有他给学生的测量操作守则。
- **这些错误有多普遍**：van der Kouwe 等人 2019，把 Heiser 的清单整理成 22 种缺陷，附调查数据和最值得优先修正的几条。
- **评估自查清单**：SIGPLAN Empirical Evaluation Checklist，一页纸，适合投稿前逐项对照。
- **测量和统计的细节**：Hoefler & Belli 2015 的 12 条规则（并行计算方向，多数规则通用）；Georges 等人 2007（启动性能和稳态性能怎么测）；Kalibera & Jones 2013（在哪个层次重复、重复多少次，怎样报告效应量的置信区间）。
- **随机化工具的评估**：Klees 等人 2018，以模糊测试为例，讲多次运行、统计检验、种子和超时。
- **机器学习评测**：Lones 的机器学习常见陷阱指南（公平比较、社区基准的问题）；Jason Wei 关于好评测集的博客；Sainz 等人 2023 关于数据污染。
- **测量偏差**：Mytkowicz 等人 2009 的原文本项目没有找到合法公开的全文，本文只引用了 Kalibera & Jones 的转述 `[待确认]`。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^ralph2020empirical-e143]: SIGSOFT 基准评测标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e143)
[^ralph2020empirical-e144]: SIGSOFT 基准评测标准，Application。[证据](../../../../sources/notes/ralph2020empirical.md#e144)
[^ralph2020empirical-e145]: SIGSOFT 基准评测标准，Application。[证据](../../../../sources/notes/ralph2020empirical.md#e145)
[^ralph2020empirical-e146]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e146)
[^ralph2020empirical-e147]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e147)
[^ralph2020empirical-e148]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e148)
[^ralph2020empirical-e149]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e149)
[^ralph2020empirical-e150]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e150)
[^ralph2020empirical-e100]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e151]: SIGSOFT 基准评测标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e151)
[^ralph2020empirical-e152]: SIGSOFT 基准评测标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e152)
[^ralph2020empirical-e153]: SIGSOFT 基准评测标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e153)
[^ralph2020empirical-e154]: SIGSOFT 基准评测标准，优秀项。[证据](../../../../sources/notes/ralph2020empirical.md#e154)
[^ralph2020empirical-e155]: SIGSOFT 基准评测标准，总体质量标准。[证据](../../../../sources/notes/ralph2020empirical.md#e155)
[^ralph2020empirical-e156]: SIGSOFT 基准评测标准，可接受的偏离。[证据](../../../../sources/notes/ralph2020empirical.md#e156)
[^ralph2020empirical-e157]: SIGSOFT 基准评测标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e157)
[^ralph2020empirical-e158]: SIGSOFT 基准评测标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e158)
[^ralph2020empirical-e159]: SIGSOFT 基准评测标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e159)
[^ralph2020empirical-e160]: SIGSOFT 工程研究标准，定义与必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e160)
[^ralph2020empirical-e161]: SIGSOFT 工程研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e161)
[^ralph2020empirical-e103]: SIGSOFT General Standard，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e103)
[^heiserbenchmarking-e1]: Heiser，Benchmarking Crimes 开头。[证据](../../../../sources/notes/heiserbenchmarking.md#e1)
[^heiserbenchmarking-e2]: Heiser，Selective benchmarking。[证据](../../../../sources/notes/heiserbenchmarking.md#e2)
[^heiserbenchmarking-e3]: Heiser，Not evaluating potential performance degradation。[证据](../../../../sources/notes/heiserbenchmarking.md#e3)
[^heiserbenchmarking-e4]: Heiser，Benchmark sub-setting。[证据](../../../../sources/notes/heiserbenchmarking.md#e4)
[^heiserbenchmarking-e5]: Heiser，Benchmark sub-setting。[证据](../../../../sources/notes/heiserbenchmarking.md#e5)
[^heiserbenchmarking-e6]: Heiser，Selective data set hiding deficiencies。[证据](../../../../sources/notes/heiserbenchmarking.md#e6)
[^heiserbenchmarking-e7]: Heiser，Pretending micro-benchmarks represent overall performance。[证据](../../../../sources/notes/heiserbenchmarking.md#e7)
[^heiserbenchmarking-e8]: Heiser，Throughput degraded by x% ⇒ overhead is x%。[证据](../../../../sources/notes/heiserbenchmarking.md#e8)
[^heiserbenchmarking-e9]: Heiser，Downplaying overheads。[证据](../../../../sources/notes/heiserbenchmarking.md#e9)
[^heiserbenchmarking-e10]: Heiser，No indication of significance of data。[证据](../../../../sources/notes/heiserbenchmarking.md#e10)
[^heiserbenchmarking-e11]: Heiser，Arithmetic mean for averaging across benchmark scores。[证据](../../../../sources/notes/heiserbenchmarking.md#e11)
[^heiserbenchmarking-e12]: Heiser，Same dataset for calibration and validation。[证据](../../../../sources/notes/heiserbenchmarking.md#e12)
[^heiserbenchmarking-e13]: Heiser，No proper baseline。[证据](../../../../sources/notes/heiserbenchmarking.md#e13)
[^heiserbenchmarking-e14]: Heiser，Only evaluate against yourself。[证据](../../../../sources/notes/heiserbenchmarking.md#e14)
[^heiserbenchmarking-e15]: Heiser，Unfair benchmarking of competitors。[证据](../../../../sources/notes/heiserbenchmarking.md#e15)
[^heiserbenchmarking-e16]: Heiser，Inflating gains by not comparing against the state of the art。[证据](../../../../sources/notes/heiserbenchmarking.md#e16)
[^heiserbenchmarking-e17]: Heiser，Missing specification of evaluation platform。[证据](../../../../sources/notes/heiserbenchmarking.md#e17)
[^heiserbenchmarking-e18]: Heiser，Missing sub-benchmark results。[证据](../../../../sources/notes/heiserbenchmarking.md#e18)
[^heiserbenchmarking-e19]: Heiser，Relative numbers only。[证据](../../../../sources/notes/heiserbenchmarking.md#e19)
[^heiserbenchmarking-e20]: Heiser，Benchmarking Best Practice › General rules。[证据](../../../../sources/notes/heiserbenchmarking.md#e20)
[^heiserbenchmarking-e21]: Heiser，Benchmarking Best Practice › Test data and results。[证据](../../../../sources/notes/heiserbenchmarking.md#e21)
[^heiserbenchmarking-e22]: Heiser，Benchmarking Best Practice › Test data and results。[证据](../../../../sources/notes/heiserbenchmarking.md#e22)
[^heiserbenchmarking-e23]: Heiser，Benchmarking Best Practice › Statistics。[证据](../../../../sources/notes/heiserbenchmarking.md#e23)
[^heiserbenchmarking-e24]: Heiser，Benchmarking Best Practice › Timing。[证据](../../../../sources/notes/heiserbenchmarking.md#e24)
[^heiserbenchmarking-e25]: Heiser，Benchmarking of simplified simulated system。[证据](../../../../sources/notes/heiserbenchmarking.md#e25)
[^heiserbenchmarking-e26]: Heiser，Inappropriate and misleading benchmarks。[证据](../../../../sources/notes/heiserbenchmarking.md#e26)
[^blackburn2018sigplan-e13]: SIGPLAN 清单，Indirect or inappropriate proxy metric。[证据](../../../../sources/notes/blackburn2018sigplan.md#e13)
[^blackburn2018sigplan-e15]: SIGPLAN 清单，Comparison is unfair。[证据](../../../../sources/notes/blackburn2018sigplan.md#e15)
[^blackburn2018sigplan-e16]: SIGPLAN 清单，Inappropriate suite。[证据](../../../../sources/notes/blackburn2018sigplan.md#e16)
[^blackburn2018sigplan-e17]: SIGPLAN 清单，Unjustified use of non-standard suite(s)。[证据](../../../../sources/notes/blackburn2018sigplan.md#e17)
[^blackburn2018sigplan-e18]: SIGPLAN 清单，Notes › Unjustified Use of Non-Standard Suite(s)。[证据](../../../../sources/notes/blackburn2018sigplan.md#e18)
[^blackburn2018sigplan-e19]: SIGPLAN 清单，Notes › Unjustified Use of Non-Standard Suite(s)。[证据](../../../../sources/notes/blackburn2018sigplan.md#e19)
[^blackburn2018sigplan-e20]: SIGPLAN 清单，Kernels instead of full applications。[证据](../../../../sources/notes/blackburn2018sigplan.md#e20)
[^blackburn2018sigplan-e21]: SIGPLAN 清单，Fails to measure all important effects。[证据](../../../../sources/notes/blackburn2018sigplan.md#e21)
[^blackburn2018sigplan-e22]: SIGPLAN 清单，Insufficient information to repeat。[证据](../../../../sources/notes/blackburn2018sigplan.md#e22)
[^blackburn2018sigplan-e23]: SIGPLAN 清单，Unreasonable platform。[证据](../../../../sources/notes/blackburn2018sigplan.md#e23)
[^blackburn2018sigplan-e24]: SIGPLAN 清单，Ignores key design parameters。[证据](../../../../sources/notes/blackburn2018sigplan.md#e24)
[^blackburn2018sigplan-e25]: SIGPLAN 清单，Gated workload generator。[证据](../../../../sources/notes/blackburn2018sigplan.md#e25)
[^blackburn2018sigplan-e26]: SIGPLAN 清单，Tested on training set。[证据](../../../../sources/notes/blackburn2018sigplan.md#e26)
[^blackburn2018sigplan-e27]: SIGPLAN 清单，Insufficient number of trials。[证据](../../../../sources/notes/blackburn2018sigplan.md#e27)
[^blackburn2018sigplan-e8]: SIGPLAN 清单，No data distribution reported。[证据](../../../../sources/notes/blackburn2018sigplan.md#e8)
[^blackburn2018sigplan-e9]: SIGPLAN 清单，Misleading summary of results。[证据](../../../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e28]: SIGPLAN 清单，Notes › Inappropriate Summary Statistics。[证据](../../../../sources/notes/blackburn2018sigplan.md#e28)
[^blackburn2018sigplan-e29]: SIGPLAN 清单，Inappropriately truncated axes / Ratios plotted incorrectly。[证据](../../../../sources/notes/blackburn2018sigplan.md#e29)
[^blackburn2018sigplan-e30]: SIGPLAN 清单，Inappropriate level of precision。[证据](../../../../sources/notes/blackburn2018sigplan.md#e30)
[^blackburn2018sigplan-e31]: SIGPLAN 清单，FAQ › artifact evaluation。[证据](../../../../sources/notes/blackburn2018sigplan.md#e31)
[^vanderkouwe2019sok-e1]: van der Kouwe 等人 2019，摘要。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e1)
[^vanderkouwe2019sok-e15]: van der Kouwe 等人 2019，§IV。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e15)
[^vanderkouwe2019sok-e16]: van der Kouwe 等人 2019，§II。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e16)
[^vanderkouwe2019sok-e11]: van der Kouwe 等人 2019，§VI。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e11)
[^vanderkouwe2019sok-e17]: van der Kouwe 等人 2019，§VI 与 §II-A。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e17)
[^vanderkouwe2019sok-e18]: van der Kouwe 等人 2019，§II-A。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e18)
[^vanderkouwe2019sok-e19]: van der Kouwe 等人 2019，§II-D 与 §VI。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e19)
[^vanderkouwe2019sok-e20]: van der Kouwe 等人 2019，§II-E。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e20)
[^vanderkouwe2019sok-e21]: van der Kouwe 等人 2019，§VI。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e21)
[^vanderkouwe2019sok-e22]: van der Kouwe 等人 2019，§II-B。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e22)
[^vanderkouwe2019sok-e23]: van der Kouwe 等人 2019，§II-F。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e23)
[^vanderkouwe2019sok-e24]: van der Kouwe 等人 2019，§II-B。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e24)
[^vanderkouwe2019sok-e25]: van der Kouwe 等人 2019，§I。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e25)
[^klees2018evaluating-e10]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e10)
[^klees2018evaluating-e11]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e11)
[^klees2018evaluating-e12]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e12)
[^klees2018evaluating-e13]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e13)
[^klees2018evaluating-e14]: Klees 等人 2018，§4。[证据](../../../../sources/notes/klees2018evaluating.md#e14)
[^klees2018evaluating-e15]: Klees 等人 2018，§4。[证据](../../../../sources/notes/klees2018evaluating.md#e15)
[^klees2018evaluating-e16]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e16)
[^klees2018evaluating-e17]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e17)
[^klees2018evaluating-e18]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e18)
[^klees2018evaluating-e19]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e19)
[^hoefler2015scientific-e1]: Hoefler & Belli 2015，§1。[证据](../../../../sources/notes/hoefler2015scientific.md#e1)
[^hoefler2015scientific-e2]: Hoefler & Belli 2015，Rule 1。[证据](../../../../sources/notes/hoefler2015scientific.md#e2)
[^hoefler2015scientific-e3]: Hoefler & Belli 2015，Rule 2。[证据](../../../../sources/notes/hoefler2015scientific.md#e3)
[^hoefler2015scientific-e4]: Hoefler & Belli 2015，Rule 3 与 Rule 4。[证据](../../../../sources/notes/hoefler2015scientific.md#e4)
[^hoefler2015scientific-e5]: Hoefler & Belli 2015，Rule 5。[证据](../../../../sources/notes/hoefler2015scientific.md#e5)
[^hoefler2015scientific-e6]: Hoefler & Belli 2015，Rule 6。[证据](../../../../sources/notes/hoefler2015scientific.md#e6)
[^hoefler2015scientific-e7]: Hoefler & Belli 2015，Rule 7。[证据](../../../../sources/notes/hoefler2015scientific.md#e7)
[^hoefler2015scientific-e8]: Hoefler & Belli 2015，Rule 8。[证据](../../../../sources/notes/hoefler2015scientific.md#e8)
[^hoefler2015scientific-e9]: Hoefler & Belli 2015，Rule 9。[证据](../../../../sources/notes/hoefler2015scientific.md#e9)
[^hoefler2015scientific-e10]: Hoefler & Belli 2015，§4.1.1。[证据](../../../../sources/notes/hoefler2015scientific.md#e10)
[^hoefler2015scientific-e11]: Hoefler & Belli 2015，§4.1.2。[证据](../../../../sources/notes/hoefler2015scientific.md#e11)
[^hoefler2015scientific-e12]: Hoefler & Belli 2015，§4.1.2。[证据](../../../../sources/notes/hoefler2015scientific.md#e12)
[^hoefler2015scientific-e13]: Hoefler & Belli 2015，§4.2.1。[证据](../../../../sources/notes/hoefler2015scientific.md#e13)
[^hoefler2015scientific-e14]: Hoefler & Belli 2015，Rule 11。[证据](../../../../sources/notes/hoefler2015scientific.md#e14)
[^hoefler2015scientific-e15]: Hoefler & Belli 2015，Rule 12。[证据](../../../../sources/notes/hoefler2015scientific.md#e15)
[^hoefler2015scientific-e16]: Hoefler & Belli 2015，摘要。[证据](../../../../sources/notes/hoefler2015scientific.md#e16)
[^hoefler2015scientific-e17]: Hoefler & Belli 2015，§4.2.2。[证据](../../../../sources/notes/hoefler2015scientific.md#e17)
[^georges2007statistically-e1]: Georges 等人 2007，§1。[证据](../../../../sources/notes/georges2007statistically.md#e1)
[^georges2007statistically-e2]: Georges 等人 2007，§1。[证据](../../../../sources/notes/georges2007statistically.md#e2)
[^georges2007statistically-e3]: Georges 等人 2007，§1。[证据](../../../../sources/notes/georges2007statistically.md#e3)
[^georges2007statistically-e4]: Georges 等人 2007，§1。[证据](../../../../sources/notes/georges2007statistically.md#e4)
[^kalibera2013rigorous-e1]: Kalibera & Jones 2013，§1。[证据](../../../../sources/notes/kalibera2013rigorous.md#e1)
[^kalibera2013rigorous-e2]: Kalibera & Jones 2013，§1。[证据](../../../../sources/notes/kalibera2013rigorous.md#e2)
[^kalibera2013rigorous-e3]: Kalibera & Jones 2013，§2（转述 Mytkowicz 等人 2009）。[证据](../../../../sources/notes/kalibera2013rigorous.md#e3)
[^kalibera2013rigorous-e4]: Kalibera & Jones 2013，§2。[证据](../../../../sources/notes/kalibera2013rigorous.md#e4)
[^kalibera2013rigorous-e5]: Kalibera & Jones 2013，§3。[证据](../../../../sources/notes/kalibera2013rigorous.md#e5)
[^kalibera2013rigorous-e6]: Kalibera & Jones 2013，§3。[证据](../../../../sources/notes/kalibera2013rigorous.md#e6)
[^kalibera2013rigorous-e7]: Kalibera & Jones 2013，§4。[证据](../../../../sources/notes/kalibera2013rigorous.md#e7)
[^kalibera2013rigorous-e8]: Kalibera & Jones 2013，§4。[证据](../../../../sources/notes/kalibera2013rigorous.md#e8)
[^kalibera2013rigorous-e9]: Kalibera & Jones 2013，§1。[证据](../../../../sources/notes/kalibera2013rigorous.md#e9)
[^kalibera2013rigorous-e10]: Kalibera & Jones 2013，§5。[证据](../../../../sources/notes/kalibera2013rigorous.md#e10)
[^wei2024evals-e1]: Wei 2024，第 1 段。[证据](../../../../sources/notes/wei2024evals.md#e1)
[^wei2024evals-e2]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e2)
[^wei2024evals-e3]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e3)
[^wei2024evals-e4]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e4)
[^wei2024evals-e5]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e5)
[^wei2024evals-e6]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e6)
[^wei2024evals-e7]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e7)
[^wei2024evals-e8]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e8)
[^wei2024evals-e9]: Wei 2024，测试集污染。[证据](../../../../sources/notes/wei2024evals.md#e9)
[^wei2024evals-e10]: Wei 2024，人工两两评比。[证据](../../../../sources/notes/wei2024evals.md#e10)
[^wei2024evals-e11]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e11)
[^wei2024evals-e12]: Wei 2024。[证据](../../../../sources/notes/wei2024evals.md#e12)
[^lones2021avoid-e13]: Lones，§5.1。[证据](../../../../sources/notes/lones2021avoid.md#e13)
[^lones2021avoid-e14]: Lones，§5.1。[证据](../../../../sources/notes/lones2021avoid.md#e14)
[^lones2021avoid-e15]: Lones，§5.5。[证据](../../../../sources/notes/lones2021avoid.md#e15)
[^lones2021avoid-e16]: Lones，§5.5。[证据](../../../../sources/notes/lones2021avoid.md#e16)
[^lones2021avoid-e17]: Lones，§6.2。[证据](../../../../sources/notes/lones2021avoid.md#e17)
[^sainz2023nlp-e1]: Sainz 等人 2023，摘要。[证据](../../../../sources/notes/sainz2023nlp.md#e1)
[^sainz2023nlp-e2]: Sainz 等人 2023，摘要。[证据](../../../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e3]: Sainz 等人 2023，§3。[证据](../../../../sources/notes/sainz2023nlp.md#e3)
[^sainz2023nlp-e4]: Sainz 等人 2023，§5.1。[证据](../../../../sources/notes/sainz2023nlp.md#e4)
[^sainz2023nlp-e5]: Sainz 等人 2023，§5.2。[证据](../../../../sources/notes/sainz2023nlp.md#e5)
