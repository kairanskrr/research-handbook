# 程序语言

> 本页只写这个方向特有的做法；通用做法见第一部分、第二部分各章和研究套路，计算机共通的规矩见[计算机学科概况](../README.md)。

## 这个方向研究什么

程序语言方向研究怎样设计、实现、分析和验证程序语言，以及用它们写出的程序。范围有多宽，可以看两个会议 2026 年的征稿启事：

- **PLDI**（Programming Language Design and Implementation，程序设计语言设计与实现会议）征集程序语言研究的各个方面，包括设计、实现、理论、应用和性能；新的系统设计、扎实的实证工作、有充分动机的理论结果、新的应用领域都在范围内[^pldi2026cfp-e1]。
- **POPL**（Principles of Programming Languages，程序设计语言原理研讨会）理论和实验论文都收，从形式化框架到经验报告；它要的是对语言的理论、设计、理解、实现或应用有原理性、持久贡献的工作[^popl2026cfp-e1]。

典型问题举例：

- 一个新的类型系统能不能保证某类错误在程序运行前就被排除？这要**证明**。
- 一个新的编译优化能让程序快多少？这要**构建改进**，再做基准评测。
- 一个静态分析工具在真实代码里能找出多少问题、误报多少？这要在开发时没用过的程序上评估。

同一篇论文里，证明和实验常常两样都有。

## 主要发表处和节奏

**发表处。** SIGPLAN（ACM Special Interest Group on Programming Languages，美国计算机协会程序设计语言分会）制定实证评估清单时，抽查的是这几个会议近几年的论文[^blackburn2018sigplan-e32]：

- ASPLOS（Architectural Support for Programming Languages and Operating Systems，程序设计语言和操作系统的体系结构支持会议）
- ICFP（International Conference on Functional Programming，国际函数式编程会议）
- OOPSLA（Object-Oriented Programming, Systems, Languages, and Applications，面向对象编程、系统、语言与应用会议）
- PLDI 和 POPL

可以把它们当作这个方向主要发表处的例子。

**PLDI 和 POPL 2026 的论文发表在期刊上。** PLDI 2026 的论文发表在 PACMPL（Proceedings of the ACM on Programming Languages，ACM 出版的程序语言期刊）的 PLDI 专刊上，作者受邀到会上报告[^pldi2026cfp-e2]。POPL 2026 也一样：为了符合 ACM 对期刊发表的要求，录用的论文都先"有条件录用"，修改够不够由原审稿人确认[^popl2026cfp-e7]。所以这两个会议都有一轮"按审稿意见修改"的环节，和只做一次决定的会议不同。

**以 PLDI 2026 和 POPL 2026 为例。** 下表只是这两份征稿启事里的规定，不是整个方向的惯例；别的年份、别的会议都会不同，**投稿前读目标会议当年的征稿启事**。

| 环节 | PLDI 2026 | POPL 2026 |
|---|---|---|
| 篇幅 | 正文最多 20 页，不含参考文献[^pldi2026cfp-e10] | 正文最多 25 页，不含参考文献[^popl2026cfp-e8] |
| 审稿标准 | 准确性、重要性、原创性、清晰度[^pldi2026cfp-e3] | 重要性、原创性、相关性、正确性、清晰度[^popl2026cfp-e2] |
| 审稿轮次 | 两轮：第一轮后有条件录用一部分、其余拒稿；第二轮由原审稿人查修改，没改好仍会被拒[^pldi2026cfp-e4] | 先有条件录用，修改由原审稿人确认[^popl2026cfp-e7] |
| 作者回复 | 第一轮后有几天，可用来纠正错误、澄清技术疑问[^pldi2026cfp-e5] | 要简洁、针对具体问题，不能提出新的技术结果[^popl2026cfp-e6] |
| 双盲 | 补充材料也要匿名；第二轮后委员会才知道录用论文的作者[^pldi2026cfp-e6] | 有条件录用之后，审稿人才看到被录用论文的作者[^popl2026cfp-e3] |
| 补充材料 | 附录都作为补充材料交，审稿人不必看[^pldi2026cfp-e11] | 可交证明、证明脚本、实现、实验数据，审稿人不必看[^popl2026cfp-e4] |
| 预印本 | 可以投已在 arXiv 上发过的工作[^pldi2026cfp-e8] | 可以发到个人网站、机构库或 arXiv[^popl2026cfp-e5] |
| 制品评估 | 自愿，不影响录用[^pldi2026cfp-e12]；投稿时要说明是否打算交制品[^pldi2026cfp-e13] | 强烈鼓励但自愿，不影响录用[^popl2026cfp-e9] |

**补充材料不能替代正文。** 两个会议 2026 年都允许交补充材料，但都写明审稿人不必看[^pldi2026cfp-e11][^popl2026cfp-e4]。所以支撑核心主张的定理陈述、关键实验结果要放在正文里，补充材料只放细节。

## 常用套路与证据标准

这个方向的实证评估，可以对照 **SIGPLAN 实证评估清单**（SIGPLAN Empirical Evaluation Checklist，下称"SIGPLAN 清单"）。它是程序语言分会为本方向的实证评估写的，PLDI 2026 明确鼓励实证论文的作者按它的七个类别准备投稿[^pldi2026cfp-e3]。清单的定位是辅助判断，不能代替判断[^blackburn2018sigplan-e14]。

计算机共通的套路和证据标准见[计算机学科概况：常用套路与证据标准](../README.md#常用套路与证据标准)。下表只补程序语言里特别要注意的地方，内容是本项目的归纳，每格的事实见脚注。

| 套路 | 在这个方向的样子 | 特别要注意 | 具体做法 |
|---|---|---|---|
| [构建改进](../../../05_research-strategies/build_improve.md) | 新的语言特性、编译优化、程序分析或合成工具 | 不能把很弱的"稻草人"基线说成最先进方法[^blackburn2018sigplan-e4]；静态分析不能只在开发时参考过的程序上评估[^blackburn2018sigplan-e26] | [工程研究](../practices/engineering_research.md) |
| [比较评估](../../../05_research-strategies/compare_evaluate.md)、[测量](../../../05_research-strategies/measure.md) | 运行时间、内存、编译时间 | 性能提升往往不大，可能落在测量误差之内[^kalibera2013rigorous-e2] | [基准评测](../practices/benchmarking.md) |
| [证明](../../../05_research-strategies/prove.md) | 类型系统的可靠性、语言语义、程序验证 | 证明细节和证明脚本可作补充材料交（POPL 2026）[^popl2026cfp-e4]，但定理本身要在正文里 | [理论研究](../practices/theoretical_research.md) |
| [观察描述](../../../05_research-strategies/observe_describe.md) | 真实程序里语言特性怎样被使用，开发者怎样用语言和工具 | 按所用方法的标准评；PLDI 2026 把扎实的实证工作列在范围内[^pldi2026cfp-e1] | [仓库挖掘](../practices/repository_mining.md)、[对照实验](../../../06_methods/controlled_experiment.md) |

很多论文同时有证明和实验，例如先证明一个分析是可靠的，再在真实程序上测它的速度和精度。这时两部分各按各的标准要求。

## 这个方向特有的规矩

**1. 主张要写明确。** 主张写得明确，读者才能判断实验支持不支持它[^blackburn2018sigplan-e1]。只说"显著更快"不够，要说在哪些程序上、和谁比、快多少。

**2. 性能结果报完整的分布和代价。** SIGPLAN 清单的几条要求：

- 只报平均数或中位数会误导读者，尤其是分布有两个峰或波动大时[^blackburn2018sigplan-e8]。
- 把 4%、6%、7%、49% 的加速概括成"最高提升 49%"不行，要报告完整分布[^blackburn2018sigplan-e9]。
- 要测量所有重要的影响，展示系统的真实代价[^blackburn2018sigplan-e21]。例如优化让程序变快、编译却变慢了，编译时间也要报。
- 写出全部参数（包括默认值）、所有软件版本号和硬件平台的完整细节[^blackburn2018sigplan-e22]。

怎样重复测量、怎样防止链接顺序之类的因素悄悄偏向某个系统、怎样处理预热，见[系统](systems.md#这个方向特有的规矩)和[基准评测：设计测量流程](../practices/benchmarking.md#第四步设计测量流程)。

**3. 比较要公平。** 不能对手用最低优化级别编译、自己用最高级别[^blackburn2018sigplan-e15]。从基准套件里只挑几个程序、或裁剪基准，是 SIGPLAN 清单作者在论文里常看到的问题[^blackburn2018sigplan-e18]。

**4. 匿名要认真，但不要因此降低质量。** PLDI 2026 提醒：如果论文首次介绍一个名字广为人知的系统，或系统名字能认出作者，投稿时要换个名字，并可注明是为双盲而改的[^pldi2026cfp-e7]。POPL 2026 则强调，不能为了匿名而降低投稿质量[^popl2026cfp-e5]。

**5. 作者回复不是补实验的地方。** POPL 2026 规定回复里不能提出新的技术结果[^popl2026cfp-e6]。所以论文投出前，就要把关键的证明和实验做完。回复的一般写法见[审稿意见、修改与被拒之后](../../../03_write-and-publish/03_review-and-revision.md#4-写会议的作者回复)。

**6. 制品评估和论文录用分开，但要早准备。** PLDI 2026 和 POPL 2026 的制品评估都自愿参加，不影响论文是否录用[^pldi2026cfp-e12][^popl2026cfp-e9]。它检查的是论文里的主张和证据与制品是否一致[^blackburn2018sigplan-e31]。PLDI 2026 要求投稿时就说明打不打算交制品[^pldi2026cfp-e13]，所以写代码和证明脚本时就要按"别人能跑起来"的标准整理。徽章的含义见[计算机学科概况](../README.md#制品评估与徽章)。

**7. 如实申报利益冲突。** PLDI 2026 写明，为了排除某些审稿人而申报不实的冲突，可能导致拒稿[^pldi2026cfp-e9]。

**8. 按目标会议的标准准备。** 同在这个方向，PLDI 2026 和 POPL 2026 的审稿标准也不完全一样（见上表）。审稿人一般怎样读论文、看哪几件事，见[当审稿人](../../../08_throughout/being_a_reviewer.md#3-像审稿人一样读论文)。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 主张含糊，只说"显著更快" | 读者无法判断实验是否支持它[^blackburn2018sigplan-e1] |
| 性能结果只给一个平均数 | 会误导读者[^blackburn2018sigplan-e8] |
| 写"最高提升 49%" | 要报告完整的结果分布[^blackburn2018sigplan-e9] |
| 基线用最低优化级别，自己的系统精心调过 | 比较不公平[^blackburn2018sigplan-e15] |
| 从基准套件里挑几个效果好的程序 | SIGPLAN 清单作者常看到的问题[^blackburn2018sigplan-e18] |
| 静态分析只在开发时一直用的程序上评估 | 要在开发时没用过的程序上评估[^blackburn2018sigplan-e26] |
| 只报运行变快，不提编译变慢 | 要展示真实代价[^blackburn2018sigplan-e21] |
| 不写软件版本和硬件细节 | 清单要求写全[^blackburn2018sigplan-e22] |
| 系统名字一看就知道是哪个组的，投稿照用 | PLDI 2026 要求换名[^pldi2026cfp-e7] |
| 论文在审时，在本领域主要邮件列表上宣传 | 审稿人很可能看到；PLDI 2026 的双盲问答列为不该做的事[^pldi2026cfp-e8] |
| 打算在作者回复里补实验或证明 | POPL 2026 不允许回复里有新的技术结果[^popl2026cfp-e6] |
| 把关键证明或实验只放在附录里 | PLDI 2026 的附录算补充材料，审稿人不必看[^pldi2026cfp-e11] |

## 延伸阅读

- **SIGPLAN Empirical Evaluation Checklist**（Berger、Blackburn、Hauswirth、Hicks，2018）：一页清单加注释，列出程序语言论文实证评估最常见的问题。做实验前读一遍，投稿前再对照一遍。
- **Kalibera & Jones 2013，Rigorous Benchmarking in Reasonable Time**：怎样在有限时间内把性能实验做严谨，怎样用置信区间报告结果。
- **Georges 等人 2007，Statistically Rigorous Java Performance Evaluation**：带虚拟机、即时编译的系统怎样测性能。
- **本书的[基准评测](../practices/benchmarking.md)和[理论研究](../practices/theoretical_research.md)**：性能实验和证明的具体做法。
- **你要投的会议当年的征稿启事和双盲评审问答**，例如 PLDI、POPL 的征稿启事。

[^pldi2026cfp-e1]: PLDI 2026 征稿启事，开头与 Scope。[证据](../../../../sources/notes/pldi2026cfp.md#e1)
[^pldi2026cfp-e2]: PLDI 2026 征稿启事，开头。[证据](../../../../sources/notes/pldi2026cfp.md#e2)
[^pldi2026cfp-e3]: PLDI 2026 征稿启事，Evaluation Criteria and Process。[证据](../../../../sources/notes/pldi2026cfp.md#e3)
[^pldi2026cfp-e4]: PLDI 2026 征稿启事，Evaluation Criteria and Process。[证据](../../../../sources/notes/pldi2026cfp.md#e4)
[^pldi2026cfp-e5]: PLDI 2026 征稿启事，Evaluation Criteria and Process。[证据](../../../../sources/notes/pldi2026cfp.md#e5)
[^pldi2026cfp-e6]: PLDI 2026 征稿启事，Double-Blind Reviewing。[证据](../../../../sources/notes/pldi2026cfp.md#e6)
[^pldi2026cfp-e7]: PLDI 2026 双盲评审问答，怎样匿名。[证据](../../../../sources/notes/pldi2026cfp.md#e7)
[^pldi2026cfp-e8]: PLDI 2026 双盲评审问答，能否公开论文。[证据](../../../../sources/notes/pldi2026cfp.md#e8)
[^pldi2026cfp-e9]: PLDI 2026 征稿启事，Declaring Conflicts。[证据](../../../../sources/notes/pldi2026cfp.md#e9)
[^pldi2026cfp-e10]: PLDI 2026 征稿启事，Formatting Requirements。[证据](../../../../sources/notes/pldi2026cfp.md#e10)
[^pldi2026cfp-e11]: PLDI 2026 征稿启事，Supplementary Material。[证据](../../../../sources/notes/pldi2026cfp.md#e11)
[^pldi2026cfp-e12]: PLDI 2026 征稿启事，Artifact Evaluation and Artifact Intent。[证据](../../../../sources/notes/pldi2026cfp.md#e12)
[^pldi2026cfp-e13]: PLDI 2026 征稿启事，Artifact Evaluation and Artifact Intent。[证据](../../../../sources/notes/pldi2026cfp.md#e13)
[^popl2026cfp-e1]: POPL 2026 征稿启事，Scope。[证据](../../../../sources/notes/popl2026cfp.md#e1)
[^popl2026cfp-e2]: POPL 2026 征稿启事，Evaluation Criteria。[证据](../../../../sources/notes/popl2026cfp.md#e2)
[^popl2026cfp-e3]: POPL 2026 征稿启事，Double-Blind Reviewing。[证据](../../../../sources/notes/popl2026cfp.md#e3)
[^popl2026cfp-e4]: POPL 2026 征稿启事，Double-Blind Reviewing（补充材料）。[证据](../../../../sources/notes/popl2026cfp.md#e4)
[^popl2026cfp-e5]: POPL 2026 征稿启事，Double-Blind Reviewing（审稿期间的传播）。[证据](../../../../sources/notes/popl2026cfp.md#e5)
[^popl2026cfp-e6]: POPL 2026 征稿启事，Evaluation Process。[证据](../../../../sources/notes/popl2026cfp.md#e6)
[^popl2026cfp-e7]: POPL 2026 征稿启事，Evaluation Process。[证据](../../../../sources/notes/popl2026cfp.md#e7)
[^popl2026cfp-e8]: POPL 2026 征稿启事，Submission Guidelines。[证据](../../../../sources/notes/popl2026cfp.md#e8)
[^popl2026cfp-e9]: POPL 2026 征稿启事，Artifact Evaluation for Accepted Papers。[证据](../../../../sources/notes/popl2026cfp.md#e9)
[^blackburn2018sigplan-e32]: SIGPLAN 实证评估清单，FAQ（条目怎样选出）。[证据](../../../../sources/notes/blackburn2018sigplan.md#e32)
[^blackburn2018sigplan-e4]: SIGPLAN 实证评估清单，Suitable Comparison。[证据](../../../../sources/notes/blackburn2018sigplan.md#e4)
[^blackburn2018sigplan-e15]: SIGPLAN 实证评估清单，Suitable Comparison。[证据](../../../../sources/notes/blackburn2018sigplan.md#e15)
[^blackburn2018sigplan-e8]: SIGPLAN 实证评估清单，Adequate Data Analysis。[证据](../../../../sources/notes/blackburn2018sigplan.md#e8)
[^blackburn2018sigplan-e9]: SIGPLAN 实证评估清单，Appropriate and Clear Experimental Design。[证据](../../../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e26]: SIGPLAN 实证评估清单，Appropriate and Clear Experimental Design。[证据](../../../../sources/notes/blackburn2018sigplan.md#e26)
[^blackburn2018sigplan-e18]: SIGPLAN 实证评估清单，注释（非标准套件）。[证据](../../../../sources/notes/blackburn2018sigplan.md#e18)
[^blackburn2018sigplan-e22]: SIGPLAN 实证评估清单，Appropriate and Clear Experimental Design。[证据](../../../../sources/notes/blackburn2018sigplan.md#e22)
[^blackburn2018sigplan-e31]: SIGPLAN 实证评估清单，FAQ（与制品评估的关系）。[证据](../../../../sources/notes/blackburn2018sigplan.md#e31)
[^blackburn2018sigplan-e14]: SIGPLAN 实证评估清单，标题下说明。[证据](../../../../sources/notes/blackburn2018sigplan.md#e14)
[^blackburn2018sigplan-e1]: SIGPLAN 实证评估清单，Clearly Stated Claims。[证据](../../../../sources/notes/blackburn2018sigplan.md#e1)
[^blackburn2018sigplan-e21]: SIGPLAN 实证评估清单，Appropriate and Clear Experimental Design。[证据](../../../../sources/notes/blackburn2018sigplan.md#e21)
[^kalibera2013rigorous-e2]: Kalibera & Jones 2013，§1。[证据](../../../../sources/notes/kalibera2013rigorous.md#e2)
