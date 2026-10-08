# 理论

> 本页只写这个方向特有的做法；通用做法见主线和研究套路，计算机共通的规矩见[计算机学科概况](../README.md)。证明怎样做、怎样写、怎样自查，见[理论研究](../practices/theoretical_research.md)，本页不重复。

## 这个方向研究什么

理论计算机研究计算本身：什么能高效地算、什么根本算不了、要付出多少代价 `[本项目分析]`。以 STOC 2026（Symposium on Theory of Computing，ACM 计算理论研讨会）的征稿为例，典型主题包括算法与数据结构、计算复杂性、计算中的随机性、近似算法、密码学、计算学习理论、优化、经济与计算、并行与分布式算法、量子计算等[^stoc2026cfp-e10]。STOC 由 SIGACT 主办，即 ACM（美国计算机协会）的算法与计算理论分会。

几个典型问题 `[本项目分析]`：

- **上界**：某个问题能不能找到更快的算法，最坏情况下要多少时间？
- **下界和不可能性**：任何算法最少要花多少代价？什么根本做不到？
- **模型和定义**：该用什么概念描述一个新问题？STOC 2026 也鼓励扩展计算理论边界、或提出能从理论分析中受益的重要问题的论文[^stoc2026cfp-e1]。

理论研究的主要成果是**定理和证明**，而不是实验数据。证明产生什么知识、什么样的证明才够，见[证明](../../../05_research-strategies/prove.md)；怎样选题、推进、写和检查证明，见[理论研究](../practices/theoretical_research.md)。本页只讲理论方向在发表和评审上的惯例。

## 主要发表处和节奏

**会议和期刊都重要。** 理论界也看重会议，但有把会议论文补全、扩展后再投期刊的长期传统，见[计算机学科概况](../README.md#会议是主要的发表渠道)[^cra1999evaluating-e4]。

下表列出三个理论会议**各自某一年**的规则，只作为例子，不是整个方向的惯例。**规则每年都会变，投稿前以当年的征稿启事为准。** FOCS 2025（Symposium on Foundations of Computer Science，计算机科学基础研讨会）由 IEEE 计算机学会的计算的数学基础技术委员会主办[^focs2025cfp-e1]；SODA 2025 是 ACM 和 SIAM（工业与应用数学学会）合办的离散算法研讨会[^soda2025cfp-e1]。三列的年份不一样：STOC 用 2026 年，FOCS 和 SODA 用 2025 年（SODA 2026 的投稿页本文没能读到）。表中没列的其他理论会议，本文资料未涉及。

| 环节 | STOC 2026 | FOCS 2025 | SODA 2025 |
|---|---|---|---|
| 截稿 | 2025 年 11 月 4 日，没有单独的摘要截止[^stoc2026cfp-e11] | 2025 年 4 月 3 日[^focs2025cfp-e2] | 2024 年 7 月 5 日，没有单独的摘要截止[^soda2025cfp-e2] |
| 投稿篇幅 | **没有页数上限**，鼓励直接投"完整版"[^stoc2026cfp-e2] | 没有页数上限，鼓励投完整版[^focs2025cfp-e3] | 没有页数上限，鼓励投完整版[^soda2025cfp-e3] |
| 开头几页 | 前 12 页讲清价值和关键想法，写给广泛的理论读者[^stoc2026cfp-e3] | 前 10 页讲清价值和关键想法[^focs2025cfp-e3] | 前 10 页讲清价值，写给理论计算机和离散数学的广泛读者[^soda2025cfp-e3] |
| 证明 | 必须能完整核验主要结论[^stoc2026cfp-e4] | 必须能完整核验主要数学结论[^focs2025cfp-e3] | 必须能完整核验主要数学结论[^soda2025cfp-e3] |
| 匿名 | 双盲，但不能为了匿名削弱论文[^stoc2026cfp-e5] | 双盲，同样不能为了匿名削弱论文[^focs2025cfp-e4] | "相当轻量"的双盲，同样不能为了匿名削弱论文[^soda2025cfp-e4] |
| 录用后 | 定稿限 12 页[^stoc2026cfp-e8]；完整版要公开到预印本平台[^stoc2026cfp-e6] | 定稿截止前公开带证明的完整版[^focs2025cfp-e5]；定稿页数本文资料未涉及 | 本文资料未涉及 |
| 一稿多投 | 按 SIGACT 的政策不允许[^stoc2026cfp-e7] | 按 SIGACT 的政策不允许[^focs2025cfp-e6] | 不能同时投另一个有论文集的会议[^soda2025cfp-e5] |

表里几格的展开，只属于 STOC 2026：

- **前 12 页**指标题页之后的前 12 页。要讲清论文在已有工作中有多重要，主要结论靠哪些关键的技术想法和概念想法；要写给广泛的理论计算机研究者，而不只是小方向的专家[^stoc2026cfp-e3]。
- **其余部分**：摘要、目录和前 12 页之外的内容，委员会自行决定读不读[^stoc2026cfp-e4]。
- **预印本**：双盲期间，作者仍可在网上和 arXiv（免费的预印本网站）发草稿、做报告[^stoc2026cfp-e5]。录用后，要在定稿截止前把带证明的完整版放到 arXiv、ECCC（Electronic Colloquium on Computational Complexity，计算复杂性电子论坛，一个预印本平台）或类似平台[^stoc2026cfp-e6]。
- **一稿多投**：不能把相同或基本相同的内容同时投给另一个有论文集的会议；唯一例外是 Science 和 Nature 上的发表[^stoc2026cfp-e7]。

从这张表能看出两点 `[本项目分析]`：

- **审稿人主要读开头 10–12 页。** 证明可以很长，但论文的价值和关键想法必须在前面讲清，而且要让非本小方向的人看懂。三个会议在这一点上的写法几乎一样。
- **完整证明必须有，而且最终要公开。** 正文放思路和关键证明，完整证明放在后面或预印本的完整版里，但不能省略。

**理论论文也会投到应用方向的会议。** 例如密码学和安全协议的证明会投安全会议。IEEE S&P 2026（IEEE 安全与隐私研讨会）和 ACM CCS 2025（计算机与通信安全会议）都要求理论论文令人信服地说明结果和实践的关系[^ieeesp2026cfp-e2][^ccs2025cfp-e2]。这些会议的其他规定见[安全](security.md)。

## 常用套路与证据标准

下表的分组和概括是本项目的归纳，每条标准只代表脚注里那篇文献或那个会议 `[本项目分析]`。

| 套路 | 在这个方向的样子 | 证据和评判标准 | 具体做法 |
|---|---|---|---|
| [证明](../../../05_research-strategies/prove.md)（上界、下界） | 设计算法并分析复杂度；证明下界或不可能性 | 证明能让人完整核验[^stoc2026cfp-e4]；方法不能顺带推出已知为假的更强结论[^aaronson2008ten-e2] | [理论研究：检查自己的证明](../practices/theoretical_research.md#第-4-步检查自己的证明-数学通用机器检查部分为计算机) |
| [证明](../../../05_research-strategies/prove.md)（模型和定义） | 提出新的计算模型、安全定义或问题 | 说清它在已有工作中的位置[^stoc2026cfp-e3]；先确认真的懂了问题[^aaronson2008ten-e1] | [理论研究：选题](../practices/theoretical_research.md#第-1-步选题并确认问题还开着定义没选错-数学通用) |
| [证明](../../../05_research-strategies/prove.md)（机器检查） | 用证明助手做形式化验证，例如 seL4 内核[^klein2009sel4-e8] | 写清证明依赖哪些假设[^klein2009sel4-e1] | [证明：什么样的证据才够](../../../05_research-strategies/prove.md#2-什么样的证据才够)、[系统](systems.md) |
| [证明](../../../05_research-strategies/prove.md)（应用理论） | 密码学、安全协议、学习理论 | 投应用会议时说明和实践的关系[^ieeesp2026cfp-e2][^ccs2025cfp-e2] | [安全](security.md)、[机器学习](machine_learning.md) |

怎么用这张表 `[本项目分析]`：理论论文的核心套路几乎都是证明，区别在于证明的对象和读者。有的论文还配实验，例如验证算法的实际表现；实验部分按[比较评估](../../../05_research-strategies/compare_evaluate.md)的标准要求。

## 这个方向特有的规矩

**正文讲思路，完整证明放后面，但不能省。** STOC 2026 的要求是：前 12 页讲清价值和关键想法[^stoc2026cfp-e3]，同时必须提供能完整核验主要结论的证明[^stoc2026cfp-e4]。Lamport 也建议准备详细和简略两个版本的证明，见[理论研究](../practices/theoretical_research.md#第-5-步直觉和形式一起给-数学通用)。两者思路一致 `[本项目分析]`。

**证明出错并不少见，所以要让证明"能检查"。** 已发表证明的出错情况和 Thurston 关于"人怎样检查证明"的观察，见[证明：什么样的证据才够](../../../05_research-strategies/prove.md#2-什么样的证据才够)；投稿前可以拿 Aaronson 的"错误突破信号"自查，见[理论研究](../practices/theoretical_research.md#第-4-步检查自己的证明-数学通用机器检查部分为计算机)。

**"写到多细才算证明"，要靠读和交流学会。** 下面三条来自数学家 Thurston 1994 年的文章，**原文讲的是数学界**，不是理论计算机：

- 他读研时也不明白"证明"到底是什么，是通过参加讨论班、读论文、和其他研究生交流慢慢明白的[^thurston1994proof-e6]。
- 看领域里其他论文不加证明就引用哪些事实、引用哪些文献，就能知道这个领域公认的基础是什么[^thurston1994proof-e7]。
- 在同一个子领域里，一个重要定理被证明后，解法常常（但不总是）几分钟就能从一个人讲给另一个人[^thurston1994proof-e4]。

把这些用到理论计算机上，是本项目的判断 `[本项目分析]`：不同小方向默认的细节程度不一样，本文资料里没有一份通用标准；多读目标方向近年的论文、多去讨论班，是学会这个尺度的办法。如果你讲不清自己的证明思路，先别急着投稿。

**机器检查的证明也有边界。** seL4 的作者承认，实现正确性证明只说明实现符合规约，不保证规约描述的就是用户想要的行为[^klein2009sel4-e2]。所以论文里要把规约和假设写出来，让读者判断 `[本项目分析]`。这类工作的代价和做法见[证明](../../../05_research-strategies/prove.md#2-什么样的证据才够)。

**引用和署名的习惯。**

- STOC 2026 请作者引用时不要用"et al."（"等人"），而是平等列出所有作者的姓[^stoc2026cfp-e9]。
- 美国数学会 2004 年的声明说，**数学家**传统上按姓氏字母顺序排列合作论文的作者[^amsculture2004joint-e3]。
- 理论计算机有没有成文的规定，本文资料未涉及；只有一份统计可以参考。Waltman 2012 年统计了 Web of Science 收录的多作者论文[^waltman2012empirical-e2]，按期刊学科分类比较[^waltman2012empirical-e3]。2007–2011 年，"计算机科学，理论与方法"这一类期刊的论文里，48.6% 的论文作者是按姓氏字母顺序排的；扣除碰巧按字母排的情况后，估计约 32.6% 是有意这样排的[^waltman2012empirical-e5]。"有意"的比例是用模型估计的，不是直接数出来的[^waltman2012empirical-e4]。同一时期"数学"类的这两个数是 83.3% 和 73.3%[^waltman2012empirical-e6]。
- 怎么读这份统计 `[本项目分析]`：它只看期刊分类，不单独看 STOC、FOCS 这类会议的论文；数据也是十几年前的。它能说明的只是：理论计算机里按字母排作者不少见，但不像数学那样占绝大多数。你所在的方向怎么排，问导师，或看目标会议近年的论文。

**不要把一次拒稿看得太重。** 会议程序委员会靠共识做决定，容易偏向稳妥的增量工作[^fortnow2009time-e3]；理论方向的具体例子（哥德尔奖论文最初被拒）见[理论研究](../practices/theoretical_research.md#第-6-步投稿会议与期刊-计算机)。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 前 12 页堆满技术细节，没讲清意义和关键想法 | STOC 2026 要求前 12 页写给广泛的理论读者[^stoc2026cfp-e3]；之后的内容不一定有人读[^stoc2026cfp-e4] |
| 投稿只给证明概要，完整证明"留待完整版" | STOC 2026 要求能完整核验[^stoc2026cfp-e4]；概要不是证明[^lamport2012how-e13] |
| 录用后不公开完整版 | STOC 2026 要求定稿前放到预印本平台[^stoc2026cfp-e6] |
| 为了匿名删掉关键引用 | STOC 2026 写明不能为了匿名削弱论文[^stoc2026cfp-e5] |
| 把同一结果同时投两个有论文集的会议 | 违反 SIGACT 的政策[^stoc2026cfp-e7] |
| 没查相关的下界和不可能性结果 | 和已知结果冲突却不提，是错误的典型信号[^aaronson2008ten-e3] |
| 投安全等应用会议时只给定理，不讲实践意义 | IEEE S&P 2026、CCS 2025 都要求说明结果和实践的关系[^ieeesp2026cfp-e2][^ccs2025cfp-e2] |
| 把数学界的惯例直接当成理论计算机的惯例 | 本页引的 Thurston 和美国数学会讲的是数学；理论计算机的做法要看目标方向的论文和会议 `[本项目分析]` |

## 延伸阅读

- **你要投的会议当年的征稿启事**，例如 STOC、FOCS、SODA。特别注意前若干页的写法要求、证明要求和一稿多投政策。
- **Thurston 1994，On Proof and Progress in Mathematics**：数学家怎样理解、交流和检查证明。讲的是数学，适合想了解理论共同体怎样运转的人。
- **Fortnow 2009，Time for Computer Science to Grow Up**：一位理论计算机学者对会议文化的批评。
- 证明的写法和自查清单（Lamport、Aaronson 等），见[理论研究](../practices/theoretical_research.md)的延伸阅读。
- 相关方向：[安全](security.md)、[系统](systems.md)、[程序语言](programming_languages.md)、[机器学习](machine_learning.md)。

[^stoc2026cfp-e10]: STOC 2026 征稿启事，开头（主题）。[证据](../../../../sources/notes/stoc2026cfp.md#e10)
[^stoc2026cfp-e1]: STOC 2026 征稿启事，开头。[证据](../../../../sources/notes/stoc2026cfp.md#e1)
[^cra1999evaluating-e4]: CRA 1999，Structure of The Field。[证据](../../../../sources/notes/cra1999evaluating.md#e4)
[^stoc2026cfp-e11]: STOC 2026 征稿启事，Dates and other relevant information。[证据](../../../../sources/notes/stoc2026cfp.md#e11)
[^stoc2026cfp-e2]: STOC 2026 征稿启事，Submission format。[证据](../../../../sources/notes/stoc2026cfp.md#e2)
[^stoc2026cfp-e3]: STOC 2026 征稿启事，Submission format。[证据](../../../../sources/notes/stoc2026cfp.md#e3)
[^stoc2026cfp-e4]: STOC 2026 征稿启事，Submission format。[证据](../../../../sources/notes/stoc2026cfp.md#e4)
[^stoc2026cfp-e5]: STOC 2026 征稿启事，Submission format（双盲）。[证据](../../../../sources/notes/stoc2026cfp.md#e5)
[^stoc2026cfp-e8]: STOC 2026 征稿启事，Camera-ready versions。[证据](../../../../sources/notes/stoc2026cfp.md#e8)
[^stoc2026cfp-e6]: STOC 2026 征稿启事，Submission Instructions。[证据](../../../../sources/notes/stoc2026cfp.md#e6)
[^stoc2026cfp-e7]: STOC 2026 征稿启事，Prior and Simultaneous Submissions。[证据](../../../../sources/notes/stoc2026cfp.md#e7)
[^ieeesp2026cfp-e2]: IEEE S&P 2026 征稿启事，开头。[证据](../../../../sources/notes/ieeesp2026cfp.md#e2)
[^ccs2025cfp-e2]: ACM CCS 2025 征稿启事，开头。[证据](../../../../sources/notes/ccs2025cfp.md#e2)
[^aaronson2008ten-e2]: Aaronson 2008，第 3 条。[证据](../../../../sources/notes/aaronson2008ten.md#e2)
[^aaronson2008ten-e1]: Aaronson 2008，第 2 条。[证据](../../../../sources/notes/aaronson2008ten.md#e1)
[^klein2009sel4-e8]: Klein 等人 2009，摘要。[证据](../../../../sources/notes/klein2009sel4.md#e8)
[^klein2009sel4-e1]: Klein 等人 2009，§1。[证据](../../../../sources/notes/klein2009sel4.md#e1)
[^thurston1994proof-e6]: Thurston 1994，§4。[证据](../../../../sources/notes/thurston1994proof.md#e6)
[^thurston1994proof-e7]: Thurston 1994，§4。[证据](../../../../sources/notes/thurston1994proof.md#e7)
[^thurston1994proof-e4]: Thurston 1994，§3。[证据](../../../../sources/notes/thurston1994proof.md#e4)
[^klein2009sel4-e2]: Klein 等人 2009，§4.5。[证据](../../../../sources/notes/klein2009sel4.md#e2)
[^stoc2026cfp-e9]: STOC 2026 征稿启事，Recommended Best Practices for References。[证据](../../../../sources/notes/stoc2026cfp.md#e9)
[^amsculture2004joint-e3]: 美国数学会 2004，第 3 段。[证据](../../../../sources/notes/amsculture2004joint.md#e3)
[^focs2025cfp-e1]: FOCS 2025 征稿启事，Overview and Call for Papers。[证据](../../../../sources/notes/focs2025cfp.md#e1)
[^focs2025cfp-e2]: FOCS 2025 征稿启事，Important dates。[证据](../../../../sources/notes/focs2025cfp.md#e2)
[^focs2025cfp-e3]: FOCS 2025 征稿启事，Submission format。[证据](../../../../sources/notes/focs2025cfp.md#e3)
[^focs2025cfp-e4]: FOCS 2025 征稿启事，Submission format（双盲）。[证据](../../../../sources/notes/focs2025cfp.md#e4)
[^focs2025cfp-e5]: FOCS 2025 征稿启事，Submission instructions。[证据](../../../../sources/notes/focs2025cfp.md#e5)
[^focs2025cfp-e6]: FOCS 2025 征稿启事，Prior and simultaneous submission。[证据](../../../../sources/notes/focs2025cfp.md#e6)
[^soda2025cfp-e1]: SODA 2025 投稿页，页面标题。[证据](../../../../sources/notes/soda2025cfp.md#e1)
[^soda2025cfp-e2]: SODA 2025 投稿页，Important Submission Information。[证据](../../../../sources/notes/soda2025cfp.md#e2)
[^soda2025cfp-e3]: SODA 2025 投稿页，Submission Format。[证据](../../../../sources/notes/soda2025cfp.md#e3)
[^soda2025cfp-e4]: SODA 2025 投稿页，Anonymous Submissions。[证据](../../../../sources/notes/soda2025cfp.md#e4)
[^soda2025cfp-e5]: SODA 2025 投稿页，Simultaneous Submissions。[证据](../../../../sources/notes/soda2025cfp.md#e5)
[^waltman2012empirical-e2]: Waltman 2012，§3。[证据](../../../../sources/notes/waltman2012empirical.md#e2)
[^waltman2012empirical-e3]: Waltman 2012，§3.2。[证据](../../../../sources/notes/waltman2012empirical.md#e3)
[^waltman2012empirical-e4]: Waltman 2012，§2。[证据](../../../../sources/notes/waltman2012empirical.md#e4)
[^waltman2012empirical-e5]: Waltman 2012，§3.2 表 1。[证据](../../../../sources/notes/waltman2012empirical.md#e5)
[^waltman2012empirical-e6]: Waltman 2012，§3.2 表 1。[证据](../../../../sources/notes/waltman2012empirical.md#e6)
[^fortnow2009time-e3]: Fortnow 2009，正文。[证据](../../../../sources/notes/fortnow2009time.md#e3)
[^lamport2012how-e13]: Lamport 2012，§6。[证据](../../../../sources/notes/lamport2012how.md#e13)
[^aaronson2008ten-e3]: Aaronson 2008，第 4 条。[证据](../../../../sources/notes/aaronson2008ten.md#e3)
