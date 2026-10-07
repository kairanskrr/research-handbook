# 证明

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本篇的道理适用于一切以证明为主要成果的研究，例子和具体做法以计算机为例；和数学、哲学不同的地方，文中单独指出。

如果你想写的核心主张是"在条件 C 下，X **一定**成立"，而不是"在我们测过的数据上，X 成立"，你的项目走的就是"证明"这条研究套路。本篇帮你想清楚四件事：这类研究产出什么，什么证据才够，具体做法去哪里学，它怎样改变项目每个阶段要做的事。

怎样选题、推进证明、写结构化证明、自查错误，计算机篇的[理论研究](../07_fields/computer-science/practices/theoretical_research.md)已经一步步写了，本篇不重复，只在需要时链接过去。主张、证据、研究套路、研究方法这些词的意思，见[核心术语](../00_start-here/key-concepts.md)。

---

## 1. 这类研究产生什么知识

证明产出的是**在写明的假设下必然成立的结论**：只要假设成立，结论就对所有情况成立，不必再拿数据去"看看是不是这样"。验证方式必须和成果类型相配：一个形式化模型要靠严格的推导和证明来支撑，而不是一两个简单的例子[^shaw2003writing-e9]。

常见的成果有四类 `[本项目分析]`：

| 成果 | 计算机例子（大模型与智能合约安全） | 回答的问题 |
|---|---|---|
| 上界（算法和它的分析） | "我们的检测算法对任意合约都会终止，运行时间不超过合约长度的平方" | 能做到多好？ |
| 下界、不可能性结果 | "任何满足条件 C 的静态检测方法，都必然在某类合约上漏报" | 最好也只能多好？什么根本做不到？ |
| 模型和定义 | 给"合约没有重入漏洞"一个精确的形式定义 | 该用什么概念描述这个问题？ |
| 形式化保证 | "在给定的以太坊虚拟机语义模型下，凡是工具判为'无重入'的合约，都不会被重入攻击"，并用机器检查过的证明支撑 | 在明确假设下，系统一定满足某个性质吗？ |

一个真实的形式化保证：seL4 是一个操作系统内核，有 8,700 行 C 代码和 600 行汇编[^klein2009sel4-e4]。它的研究团队用机器检查过的证明说明，内核的 C 实现始终严格符合它的抽象规约（对内核应有行为的精确描述）[^klein2009sel4-e8]。这个结论带着明确的前提：编译器、汇编代码、启动代码、缓存管理和硬件被假定为正确，其余部分全部证明[^klein2009sel4-e1]；只要这些假设成立，内核就不会崩溃或出现意外行为[^klein2009sel4-e3]。

**和其他套路的区别** `[本项目分析]`：

| | 证明 | 构建改进 | 比较评估 |
|---|---|---|---|
| 主要证据 | 证明 | 造出来的东西 + 实验 | 在统一任务上的测量 |
| 结论的范围 | 满足假设的所有情况 | 实验覆盖的情况 | 评测覆盖的情况 |
| 最大的风险 | 证明有错；假设离实际太远 | 实验不公平、不可复现 | 评测集不代表实际 |

很多计算机论文是混合的：提出一个新工具（构建改进），同时证明它的某个性质。这时按核心主张定主要套路，证明部分按本篇的标准要求，实验部分按[构建改进](build_improve.md)的标准要求 `[本项目分析]`。

**写下来：** 把你的核心主张写成"在假设 A、B、C 下，结论 X 成立"的形式。写不出假设，或者结论里出现"大多数""通常"这类词，它可能不是一个证明式主张。

## 2. 什么样的证据才够

读一篇证明论文，审稿人和读者会追问下面五件事，每一件都要有交代 `[本项目分析]`。

**（1）假设都写出来了吗？** 定理陈述里很容易藏着没写出的假设：Lamport（分布式系统和形式化方法研究者）举过的一个定理，就默认了 a < b 却没写出来[^lamport2012how-e6]。他还指出，漏掉"集合非空"这样的假设，在数学定理里只是小疏忽，放到算法里可能就是严重的缺陷[^lamport2012how-e9]。做法是像 seL4 那样，把"假定正确、不证明"的部分逐条列出[^klein2009sel4-e1]，并在定理陈述里写全所有假设 `[本项目分析]`。

**（2）证明完整吗？** Lamport 的经验是，大多数错误来自证明没有展开到足够的层次[^lamport1995how-e5]；他的经验法则是展开到最底层每句话都显然成立，然后再多展开一层[^lamport1995how-e6]。证明概要（几句话说明思路）有用，但它不是证明[^lamport2012how-e13]。怎样写成分层、可逐步检查的证明，见理论研究的[第 3 步](../07_fields/computer-science/practices/theoretical_research.md#第-3-步把证明写得可以检查-数学通用)。

**（3）别人能检查吗？** 数学家 Thurston 观察到，人不太擅长逐条检查证明的形式正确性，却很擅长发现证明中可能的薄弱处[^thurston1994proof-e9]；在他看来，数学结果的可靠性主要来自数学家仔细、批判地思考其中的想法[^thurston1994proof-e11]。所以他主张把证明写得清楚、尽量简单，让薄弱处容易被发现[^thurston1994proof-e10]。期刊审稿也把正确性放在前面：美国数学会的伦理准则要求，编辑只在合理确信论文正确时才接收[^ams2022ethical-e9]。但没人挑出错，不等于没错：Lamport 引述过一种传闻性的说法，数学期刊上多达三分之一的论文含有错误的定理或证明[^lamport1995how-e1]（这是传闻，不是统计）。

**（4）需要机器检查吗？** 机器检查指用证明助手（能逐步检查形式化证明的软件）来核对每一步。Lamport 认为，把数学形式化不难，难的是写出机器能检查的证明[^lamport2012how-e8]。seL4 这一个项目可以让你感受代价和回报的量级，但这些数字只属于它，不是一般规律：

- 代价：它的证明共约 20 万行 Isabelle（一种证明助手）脚本，这个行数包括框架、库和自动生成的证明；整个证明的投入约 20 人年[^klein2009sel4-e4]。
- 回报：正式验证开始前，内部学生项目和移植工作在实现里发现了 16 个缺陷；形式化验证又发现了 144 个[^klein2009sel4-e6]。
- 附带的好处：作者反复发现，为了能被验证，设计者被迫寻找最简单、最清晰的做法，这带来了更好的设计[^klein2009sel4-e7]。

Lamport 还指出，算法的证明往往数学上不深，但很繁杂，有大量细节要检查[^lamport2012how-e10]。所以，细节繁多、漏一个假设就会变成漏洞的证明（并发算法、协议、内核、合约分析工具），更值得用机器检查；普通的定理不一定需要 `[本项目分析]`。证明里用到符号计算时，一份关于计算数学可复现性的研讨会报告（Stodden 等 2013）在检查清单里建议，用两个不同的软件互相核对，因为再好的软件也有缺陷[^stodden2013setting-e5]。

**（5）假设和现实差多远？** 证明再严密，也只对它的假设和规约负责。seL4 的作者自己承认：实现正确性证明不保证规约描述的就是用户期望的行为[^klein2009sel4-e2]。放到合约例子里 `[本项目分析]`：你证明了"在虚拟机语义模型 M 下，工具判为安全的合约不会被重入"，审稿人就会问，模型 M 是否覆盖了真实链上的调用方式？你对"重入安全"的定义，是不是和社区通用的一样？假设偏强、结论偏弱的地方，数学家 Tao 建议诚实写出来，例如"我们不知道假设 H 是否必要"[^taowriting-e4]。

**写下来：** 列出你的定理依赖的每一条假设，在旁边写一句"它在真实合约里成立吗？依据是什么？"。答不上来的，就是你在"局限"一节要交代的内容。

## 3. 常用的研究方法

套路说"要产生什么知识"，方法说"怎么拿到证据"。走证明套路时，常用的方法有这几种：

| 方法 | 什么时候用 | 去哪里看 |
|---|---|---|
| 手工证明（定理与证明） | 复杂度上下界、算法正确性、不可能性结果、新定义的性质 | [理论研究](../07_fields/computer-science/practices/theoretical_research.md)：选题、推进证明、结构化地写证明、检查自己的错误 |
| 机器检查的证明（交互式定理证明：人引导、证明助手逐步检查） | 细节繁多、出错代价大的系统和算法 | [理论研究](../07_fields/computer-science/practices/theoretical_research.md#第-4-步检查自己的证明-数学通用机器检查部分为计算机)的机器检查部分 |
| 计算机辅助证明、实验数学 | 用计算探索猜想，或让计算成为证明的一部分 | [数学领域概况](../07_fields/mathematics/README.md#本领域的规范)的"本领域的规范"一节 |

按 seL4 论文的说法，交互式定理证明需要人的介入和创造力来构造和引导证明；好处是不像静态分析、模型检测（由程序自动遍历系统的可能状态、检查某个性质）这类更自动的验证方法那样，只能处理特定性质或有限的状态空间[^klein2009sel4-e5]。计算机辅助证明方面，前面提到的研讨会报告建议期刊要求：做出重要论断的论文（例如用计算机证明一个长期未解的数学结果），要做严格验证，并完整公开计算细节[^stodden2013setting-e4]。

**证明常和实验搭配。** 软件工程领域的 ACM SIGSOFT 实证研究标准，把"为关键的理论贡献（定理、复杂度分析、数学证明）给出正确性论证"列为工程研究的加分项[^ralph2020empirical-e88]；"理论保证"也可以是新工具胜过已有工具的那个维度[^ralph2020empirical-e95]。Vandewalle 等指出，信号处理里定理常配上数值仿真，帮助读者直观理解结果[^vandewalle2009reproducible-e12]。

**和哲学论证对照。** 哲学家处理的论证大多也是（或自称是）演绎论证，数学证明正是这类论证的典型[^pryor2025terms-e3]。差别在前提：哲学论证的前提很少绝对无可置疑，所以即使推理有效，通常也不能一锤定音[^pryor2025terms-e12]。因此哲学论文的大部分功夫花在为前提辩护、回应反驳上，一般归入[解读论证](interpret_argue.md)套路，具体做法见[哲学论证研究](../07_fields/philosophy-ethics-religion/research-types/philosophical_argument.md) `[本项目分析]`。

不要拿错验证方式：Shaw 在讨论软件工程研究时指出，用实地研究去验证一个形式化模型是否正确，和对一套经验法则做形式化验证一样不合适[^shaw2003writing-e14]。

## 4. 它怎样影响整个项目

走证明套路时，各阶段要多做或换着做的事如下表 `[本项目分析]`。表中推进和自查的做法，多来自数学家 Tao 的职业建议和理论计算机学者 Aaronson 列的"错误突破信号"，是个人经验，不是学科规定；展开的做法见[理论研究的第 1、2 步](../07_fields/computer-science/practices/theoretical_research.md#2-怎么做)。

| 阶段 | 走证明套路时特别要做的 |
|---|---|
| [收敛成项目](../01_from-interest-to-project/03_converge.md) | 把主张写成定理的形式。新手先做可行的问题：著名难题几乎从不是凭空解决的[^taocareer-e13]，Tao 建议把大部分时间放在更可行的问题上，积累经验和信誉[^taocareer-e14] |
| [进入领域、探索文献](../01_from-interest-to-project/01_enter-a-field.md) | 找到关键论文后查谁引用了它[^taocareer-e16]，确认问题还开着；特别要查相关的下界和不可能性结果，Aaronson 把"和已知不可能性结果冲突却不提"列为错误突破的信号[^aaronson2008ten-e3] |
| [从研究问题到证据清单](../02_from-project-to-study/01_question-to-evidence.md)、[选定研究套路和方法](../02_from-project-to-study/02_choose-strategy-and-method.md) | 定下用手工证明还是机器检查；把定义和标准文献逐字对照，记号也尽量和已有文献一致[^taowriting-e8] |
| [效度与局限](../02_from-project-to-study/03_validity-and-limits.md) | 证明没有抽样误差，但有"假设和规约是否贴近现实"的问题[^klein2009sel4-e2] |
| [先做小规模试验，排除最大风险](../02_from-project-to-study/04_pilot-and-derisk.md) | 先试着找反例：找到了省下大量时间，反例本身也可能值得发表；找不到，遇到的障碍会提示证明该怎么做[^taocareer-e2]。先分离出简化的特殊情形来做[^taocareer-e5] |
| [执行与迭代](../03_conduct-and-analyze/01_run-and-iterate.md) | 重视部分进展，它是完全解决问题的关键垫脚石[^taocareer-e6]，很多中间步骤本身就是可发表的论文[^taocareer-e22]；有意思的论证写成草稿，详细到日后能恢复[^taocareer-e18] |
| [分析与解读](../03_conduct-and-analyze/02_analyze-and-interpret.md) | "分析"变成查错：这个方法会不会也"证明"出已知为假的更强结论[^taocareer-e1]？每个关键假设都实质用到了吗[^taowriting-e13]？ |
| [讲清故事，写成论文](../04_write-and-publish/01_story-and-paper.md) | 按 Lamport 的建议，靠分层结构和给每一步命名（编号）让证明好懂[^lamport2012how-e1]；每个主要证明前给一段概要，作为读者的路线图[^lamport1995how-e2]；结果不说小也不说大[^taowriting-e3] |
| [选择发表渠道与投稿](../04_write-and-publish/02_venue-and-submission.md) | 计算机理论方向看重会议，也有把会议论文补全后再投期刊的传统[^cra1999evaluating-e4]；数学研究大多发表在有审稿的期刊上[^amsculture2006rates-e1] |
| [审稿意见、修改与被拒之后](../04_write-and-publish/03_review-and-revision.md) | 别把一次拒稿看得太重：近一半哥德尔奖（理论计算机的最佳论文奖）获奖论文最初被顶级理论会议拒过，或根本没在那里发表[^fortnow2009time-e8] |

**写下来：** 在你的项目计划里加一行"先找反例"的任务，写明打算在哪些小例子、特殊情形上试。

## 5. 哪些学科常用

只列本文资料能支持的学科：

- **数学**：Thurston 观察到，数学家除了想知道定理成立，还想理解它的证明[^thurston1994proof-e2]。学科规矩见[数学领域概况](../07_fields/mathematics/README.md)。
- **理论计算机**：算法证明细节繁多（见第 2 节），有专门授予最佳理论论文的哥德尔奖[^fortnow2009time-e8]。具体做法见[理论研究](../07_fields/computer-science/practices/theoretical_research.md)。
- **软件工程、系统、安全中的形式化方向**：形式化模型要靠证明支撑[^shaw2003writing-e9]；软件工程的评审标准把定理和复杂度分析列为工程研究的加分项[^ralph2020empirical-e88]；seL4 内核有从抽象规约到 C 实现的机器检查证明[^klein2009sel4-e8]。
- **电子工程（信号处理）**：Vandewalle 等认为信号处理介于理论科学和实验科学之间，定理常和数值仿真一起出现[^vandewalle2009reproducible-e12]。
- **哲学**：也用演绎论证[^pryor2025terms-e3]，但因为前提可争议，主要归入[解读论证](interpret_argue.md)套路（见第 3 节）。

物理、经济学等学科里的理论推导和模型证明，本文资料未涉及。

## 6. 常见错误

下面只列套路层面的错误；写证明、自查时的错误（隐含假设、证明"太强"、某个假设没用到、把概要当证明等），见[理论研究的常见错误](../07_fields/computer-science/practices/theoretical_research.md#4-常见错误)。

| 错误 | 为什么是问题 |
|---|---|
| 证明的命题和真正要问的问题不一样（定义不同、模型不同） | Aaronson 把"作者没弄懂问题本身"列为错误突破的信号[^aaronson2008ten-e1]；结论看似成立，回答的却不是原问题 `[本项目分析]` |
| 只证明实现符合规约，就宣称系统"安全" | 证明不保证规约描述的就是用户期望的行为[^klein2009sel4-e2] |
| 假设偏强、结论偏弱，却不写出来 | Tao 建议把这些坦白写出[^taowriting-e4]；否则读者会把结论的适用范围想得太大 `[本项目分析]` |
| 摘要说"我们证明了"，结尾变成"看起来可行" | 证明退化成了"有道理的论证"，Aaronson 把这列为错误的信号[^aaronson2008ten-e4] |
| 用一两个例子"验证"形式化模型 | 形式化模型要靠严格推导和证明[^shaw2003writing-e9] |
| 新手一上来就死磕著名难题 | 著名难题几乎从不是凭空解决的[^taocareer-e13] |

## 7. 延伸阅读

- **[理论研究](../07_fields/computer-science/practices/theoretical_research.md)**：本套路在计算机里的完整做法，从选题、推进、写证明到自查。它的延伸阅读列了 Lamport、Tao、Aaronson 的原文。
- **[数学领域概况](../07_fields/mathematics/README.md)**：数学怎样运转，适合打算在数学期刊发表的人。
- **Thurston 1994，On proof and progress in mathematics**：数学家实际上怎样理解、交流和检查证明。
- **Klein 等 2009，seL4: Formal Verification of an OS Kernel**：一个完整的形式化验证项目，写清了假设、代价和证明发现的缺陷。适合考虑做机器检查证明的人。
- **[解读论证](interpret_argue.md)** 和 **[哲学论证研究](../07_fields/philosophy-ethics-religion/research-types/philosophical_argument.md)**：对照阅读，看演绎论证在前提可争议时怎么做。

[^shaw2003writing-e9]: Shaw 2003，§4.1。[证据](../../sources/notes/shaw2003writing.md#e9)
[^shaw2003writing-e14]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e14)
[^klein2009sel4-e1]: Klein 等 2009，§1。[证据](../../sources/notes/klein2009sel4.md#e1)
[^klein2009sel4-e2]: Klein 等 2009，§4.5。[证据](../../sources/notes/klein2009sel4.md#e2)
[^klein2009sel4-e3]: Klein 等 2009，§4.5。[证据](../../sources/notes/klein2009sel4.md#e3)
[^klein2009sel4-e4]: Klein 等 2009，摘要、§5.2。[证据](../../sources/notes/klein2009sel4.md#e4)
[^klein2009sel4-e5]: Klein 等 2009，§2.3。[证据](../../sources/notes/klein2009sel4.md#e5)
[^klein2009sel4-e6]: Klein 等 2009，§5.2。[证据](../../sources/notes/klein2009sel4.md#e6)
[^klein2009sel4-e7]: Klein 等 2009，§3.5。[证据](../../sources/notes/klein2009sel4.md#e7)
[^klein2009sel4-e8]: Klein 等 2009，摘要。[证据](../../sources/notes/klein2009sel4.md#e8)
[^lamport2012how-e1]: Lamport 2012，§1。[证据](../../sources/notes/lamport2012how.md#e1)
[^lamport2012how-e6]: Lamport 2012，§3 脚注 1。[证据](../../sources/notes/lamport2012how.md#e6)
[^lamport2012how-e8]: Lamport 2012，§4.5。[证据](../../sources/notes/lamport2012how.md#e8)
[^lamport2012how-e9]: Lamport 2012，§5。[证据](../../sources/notes/lamport2012how.md#e9)
[^lamport2012how-e10]: Lamport 2012，§5。[证据](../../sources/notes/lamport2012how.md#e10)
[^lamport2012how-e13]: Lamport 2012，§6。[证据](../../sources/notes/lamport2012how.md#e13)
[^lamport1995how-e1]: Lamport 1995，§1。[证据](../../sources/notes/lamport1995how.md#e1)
[^lamport1995how-e2]: Lamport 1995，§2.1。[证据](../../sources/notes/lamport1995how.md#e2)
[^lamport1995how-e5]: Lamport 1995，§4.2。[证据](../../sources/notes/lamport1995how.md#e5)
[^lamport1995how-e6]: Lamport 1995，§4.2。[证据](../../sources/notes/lamport1995how.md#e6)
[^taowriting-e3]: Tao，On writing："Describe the results accurately"。[证据](../../sources/notes/taowriting.md#e3)
[^taowriting-e4]: Tao，On writing："Describe the results accurately"。[证据](../../sources/notes/taowriting.md#e4)
[^taowriting-e8]: Tao，On writing："Use good notation"。[证据](../../sources/notes/taowriting.md#e8)
[^taowriting-e13]: Tao，On writing："On local and global errors in mathematical papers"。[证据](../../sources/notes/taowriting.md#e13)
[^taocareer-e1]: Tao，Career advice："Be sceptical of your own work"。[证据](../../sources/notes/taocareer.md#e1)
[^taocareer-e2]: Tao，Career advice："Be sceptical of your own work"。[证据](../../sources/notes/taocareer.md#e2)
[^taocareer-e5]: Tao，Career advice："Be sceptical of your own work"。[证据](../../sources/notes/taocareer.md#e5)
[^taocareer-e6]: Tao，Career advice："On the importance of partial progress"。[证据](../../sources/notes/taocareer.md#e6)
[^taocareer-e13]: Tao，Career advice："Don't base career decisions on glamour or fame"。[证据](../../sources/notes/taocareer.md#e13)
[^taocareer-e14]: Tao，Career advice："Don't prematurely obsess on a single big problem or big theory"。[证据](../../sources/notes/taocareer.md#e14)
[^taocareer-e16]: Tao，Career advice："Learn and relearn your field"。[证据](../../sources/notes/taocareer.md#e16)
[^taocareer-e18]: Tao，Career advice："Write down what you've done"。[证据](../../sources/notes/taocareer.md#e18)
[^taocareer-e22]: Tao，Career advice："Be sceptical of your own work"。[证据](../../sources/notes/taocareer.md#e22)
[^thurston1994proof-e2]: Thurston 1994，§1。[证据](../../sources/notes/thurston1994proof.md#e2)
[^thurston1994proof-e9]: Thurston 1994，§4。[证据](../../sources/notes/thurston1994proof.md#e9)
[^thurston1994proof-e10]: Thurston 1994，§4。[证据](../../sources/notes/thurston1994proof.md#e10)
[^thurston1994proof-e11]: Thurston 1994，§4。[证据](../../sources/notes/thurston1994proof.md#e11)
[^aaronson2008ten-e1]: Aaronson 2008，第 2 条。[证据](../../sources/notes/aaronson2008ten.md#e1)
[^aaronson2008ten-e3]: Aaronson 2008，第 4 条。[证据](../../sources/notes/aaronson2008ten.md#e3)
[^aaronson2008ten-e4]: Aaronson 2008，第 5 条。[证据](../../sources/notes/aaronson2008ten.md#e4)
[^ams2022ethical-e9]: AMS 伦理准则，IV. Publications。[证据](../../sources/notes/ams2022ethical.md#e9)
[^amsculture2006rates-e1]: AMS 2006，第 2 段。[证据](../../sources/notes/amsculture2006rates.md#e1)
[^stodden2013setting-e4]: Stodden 等 2013（ICERM 报告），Journals 一节。[证据](../../sources/notes/stodden2013setting.md#e4)
[^stodden2013setting-e5]: Stodden 等 2013，Appendix C。[证据](../../sources/notes/stodden2013setting.md#e5)
[^ralph2020empirical-e88]: ACM SIGSOFT 实证研究标准，Engineering Research，Desirable Attributes。[证据](../../sources/notes/ralph2020empirical.md#e88)
[^ralph2020empirical-e95]: ACM SIGSOFT 实证研究标准，Engineering Research，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e95)
[^vandewalle2009reproducible-e12]: Vandewalle 等 2009，How to do reproducible research? — Components。[证据](../../sources/notes/vandewalle2009reproducible.md#e12)
[^pryor2025terms-e3]: Pryor，Philosophical Terms and Methods，Different Flavors of Argument。[证据](../../sources/notes/pryor2025terms.md#e3)
[^pryor2025terms-e12]: Pryor，Philosophical Terms and Methods，Conclusive or Not?。[证据](../../sources/notes/pryor2025terms.md#e12)
[^cra1999evaluating-e4]: Patterson、Snyder & Ullman 1999（CRA 备忘录），Structure of The Field。[证据](../../sources/notes/cra1999evaluating.md#e4)
[^fortnow2009time-e8]: Fortnow 2009，正文。[证据](../../sources/notes/fortnow2009time.md#e8)
