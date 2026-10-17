# 综合

> 本篇讲的是一种研究套路，道理适用于各学科；例子和具体做法以计算机为例，医学等学科的做法在相应地方点出。

你读了几十篇"大模型与智能合约安全"的论文，越读越觉得：这些工作各说各的，没人把它们放在一起看过。于是你想，能不能把已有研究本身当成研究对象，写一篇让整个方向看清自己的论文？

这就是**综合**这种研究套路：不自己去收集新的实验数据，而是系统地收集、评价、汇总别人已经发表的研究，回答一个单篇研究回答不了的问题。研究套路的总体介绍见[核心术语](../00_start-here/key-concepts.md#研究套路)。

## 1. 这类研究产生什么知识

综合产生的是**关于已有知识的整体图景**：这个方向研究了什么、证据合起来说明了什么、哪里还是空白、哪里做错了。

同一个方向，综合也可以有好几种主张。主张不同，要做的综述类型就不同 `[本项目分析]`：

| 你想说的主张（例子） | 适合的综述类型 | 它产出的东西 |
|---|---|---|
| "这一方向的研究可以分成四类，存在三个空白" | 映射研究（在软件工程以外常叫范围综述）[^ralph2022paving-e3] | 分类和计数，一张"研究地图" |
| "现有证据表明，提示漏洞模式能提高检出率" | 系统综述：找出、评价、解读与一个具体问题有关的全部研究[^kitchenham2007guidelines-e2] | 针对这个问题的证据结论 |
| "把各项实验的检出率合起来，提升幅度是多少" | 元分析：用统计方法把多项研究的结果合并成一个效应量[^murad2016new-e7] | 一个合并后的数值 |
| "已发表的审计案例里，做了某件事的团队更少出事" | 案例调查：把已发表案例研究里的文字描述转换成数据，再做分析[^ralph2020empirical-e291] | 从许多案例归纳出的结论 |
| "这一方向多数论文的评测方法有同一个毛病" | 批判性综述：分析一批研究，用来支撑一个论点或一项批评[^ralph2022paving-e12] | 对研究做法的具体批评和建议 |
| "理解这个方向，可以用这样一个框架" | 综述论文：对文献分类、形成对领域的视角、评估趋势[^acm2026csurguidelines-e1] | 分类框架和对领域的判断 |

还有一种常见的综述，就是每篇论文里的"相关工作"：作者有目的地挑一些文献来讨论[^ralph2022paving-e1]。它适合用来发展理论、寻找有前景的选题，但因为是挑出来的，有抽样偏差、无法复现，撑不起"X 导致 Y"这类实证结论[^ralph2022paving-e2]。

由此得出一条贯穿全篇的规则 `[本项目分析]`：**你想下的结论越硬，综述就要做得越系统。**

还有一类是把多项定性研究的发现综合起来，例如元民族志、叙事综合[^ralph2020empirical-e292]。本文资料没有讲它的具体做法。

**写下来：** 用上表的格式，写出你想说的那句主张，并对照右边两栏，判断它属于哪一类综述。

## 2. 什么样的证据才够

综合的证据，是你**找到了哪些研究、为什么收它们、从中提取了什么、怎样把它们合起来**。读者能不能相信你的结论，就看这四件事经不经得起检查。

几条基本功对所有系统的综述都适用：一步步写清检索过程和筛选标准[^ralph2020empirical-e4]；开始检索前先写好研究方案，防止自己按预期去挑论文、做分析[^kitchenham2007guidelines-e7]；从提取的数据到问题的答案要有清楚的证据链，逐篇罗列"A 发现 X，B 发现 Y"不算综合[^ralph2020empirical-e6][^ralph2020empirical-e16]；用事先定好的标准评估每项研究的质量，不拿会议或期刊的档次代替[^ralph2020empirical-e10][^ralph2020empirical-e16]。每一步具体怎么做，见方法篇[综述研究](../06_methods/review_study.md)里的[系统综述怎么做](../06_methods/review_study.md#2-系统综述怎么做)和[检查清单](../06_methods/review_study.md#5-检查清单)。

本篇要你多想一步的是：**不同类型的综述，"够"的标准不一样。** 用错标准，要么白费力气，要么被挑出硬伤 `[本项目分析]`。审稿人也可能用错，例如拿"找全所有研究""排除低质量研究"去要求批判性综述[^ralph2022paving-e20]。

| 综述类型 | 要不要找全 | 要不要评每篇质量 | 关键要求 |
|---|---|---|---|
| 映射研究 | 检索与系统综述类似[^ralph2022paving-e4]；对"全"的要求低于元分析[^ralph2020empirical-e9] | 一般不评[^petersen2008systematic-e4] | 分类和计数清楚 |
| 系统综述 | 尽量找全[^kitchenham2007guidelines-e2] | 要[^kitchenham2007guidelines-e13] | 从数据到答案的证据链清楚[^ralph2020empirical-e6] |
| 元分析 | 要求高于宽泛主题的映射研究[^ralph2020empirical-e9] | 要，重点评结果的偏倚风险[^higgins2024cochrane-e21] | 研究足够相似才能合并[^higgins2024cochrane-e15] |
| 案例调查 | 可复现地检索已发表案例[^ralph2020empirical-e293] | 加分项[^ralph2020empirical-e301] | 事先定好编码方案[^ralph2022paving-e7][^ralph2020empirical-e295]，需要大量案例[^ralph2022paving-e10] |
| 批判性综述 | 不必，从顶级期刊和会议随机抽样就够[^ralph2022paving-e15] | 不按"排除低质量研究"要求[^ralph2022paving-e20] | 不止描述，要提出具体批评[^ralph2022paving-e16] |

所以，第一件事是在论文里**说明自己做的是哪一类综述**[^ralph2020empirical-e3]，并论证检索的严格程度和你的目标相称[^ralph2020empirical-e9]。

> **不同的看法：只做分类和计数的映射研究，值不值得单独做？**
> - 值得：映射研究和系统综述的目标、范围、效度问题都不同，两者应当互相补充；映射研究适用的场合比通常认为的更广[^petersen2008systematic-e7]。
> - 不够：以描述为主的范围综述（即映射研究）通常综合不够，回答不了重要的实证问题[^ralph2022paving-e4]；两位作者针对软件工程说，以描述为主的范围综述"本质上是还在进行中的工作"，应该放到研讨会、海报或短文栏目；如果文献足够做综合，它更像正式系统综述前的预研[^ralph2022paving-e5]。
>
> 对你的影响 `[本项目分析]`：映射研究本身有用，但如果目标是正式会议或期刊，最好在分类和计数之外，往"综合出结论"多走一步。

**写下来：** 写出你选的综述类型，并按上表逐列写下你打算做到什么程度：查哪些来源、评不评质量、关键要求怎么满足。

## 3. 常用的研究方法

具体怎么做，见下面的方法文件：

- [综述研究：系统综述、映射研究与综述论文](../06_methods/review_study.md)：讲研究方案、检索、筛选、提取、报告的完整步骤。
- [案例调查](../06_methods/case_survey.md)：把已发表的案例研究编码成数据集。
- [方法论研究与元科学](../06_methods/meta_science.md)：批判性综述属于学界内部"怎么做研究"的讨论，也就是元科学[^ralph2022paving-e14]。
- [系统综述与元分析（健康领域）](../06_methods/meta_analysis.md)：效应指标、固定效应和随机效应模型、异质性、证据确定性分级的具体做法。

元分析的统计部分**不要一上来就做**：如果问题界定、纳入标准、检索筛选、数据收集、偏倚评价没做好，合并出的结果可能非常误导人[^higgins2024cochrane-e14]。系统综述也不一定要有元分析，研究结果差异很大时，报一个平均效应反而可能误导[^higgins2024cochrane-e16]。

## 4. 它怎样影响整个项目

选了综合这条路，项目的每个阶段都会和其他套路不太一样 `[本项目分析]`：

| 阶段 | 综合项目的特点 |
|---|---|
| [收敛成项目](../01_find-a-problem/05_converge.md) | 先确认这篇综述确实需要做[^kitchenham2007guidelines-e5]，例如查查有没有人做过类似的；有的话，想清楚你能补上什么，例如新的时间段或不同的问题 |
| [形成研究计划](../02_do-the-project/03_research-plan.md) | 研究问题是规划阶段最重要的一步[^kitchenham2007guidelines-e6]；研究方案是系统综述的关键[^kitchenham2007guidelines-e9]。高质量的系统综述往往费力又费时[^higgins2024cochrane-e4]，排时间别太乐观 |
| [从研究问题到证据清单](../02_do-the-project/01_question-to-evidence.md) | 证据就是文献本身，研究问题直接决定检索词、筛选标准和要提取的数据 |
| [最小可跑版本](../02_do-the-project/05_pilot-and-derisk.md) | 筛选标准定好后，先在一小批论文上试用[^kitchenham2007guidelines-e8]；先做预检索，看相关研究大概有多少 |
| [执行与迭代](../02_do-the-project/06_run-and-iterate.md) | 工作量主要在筛选和提取；第一轮筛选要宽松[^kitchenham2007guidelines-e11]，一个人做时请导师抽一部分论文也提取一遍，交叉核对[^kitchenham2007guidelines-e15] |
| [分析与解读](../02_do-the-project/07_analyze-and-interpret.md) | 把结果放回已有研究中，指出空白和方向；清楚区分有证据的结果和自己的推测[^ralph2020empirical-e13] |
| [讲清故事，写成论文](../03_write-and-publish/01_story-and-paper.md) | 按报告规范写出完整检索式、画出从检索到纳入的流程图[^page2021prisma-e3][^page2021prisma-e4]；公开研究方案、检索结果、数据和脚本[^ralph2020empirical-e7] |
| [选择发表渠道与投稿](../03_write-and-publish/02_venue-and-submission.md) | 综述期刊可能有篇幅上限，例如 ACM Computing Surveys 的长综述含参考文献不超过 35 页[^acm2026csurguidelines-e4]；只有分类计数的映射研究，见上文"不同的看法" |

还有一个常被忽略的用处：综合项目常常是其他项目的起点。映射研究能找出研究扎堆和空白的地方，为后续的系统综述和新研究指明方向[^kitchenham2007guidelines-e3]。在医学领域，Cochrane 手册的说法是，开始新的原始研究之前一般应先做系统综述[^higgins2024cochrane-e3]。

**写下来：** 估一下你的检索大概会返回多少篇论文、你一周能筛多少篇，算出筛选阶段要几周。

## 5. 哪些学科常用

只写本文资料能支持的：

- **医学与公共卫生**：有专门讲干预效果系统综述的方法手册（Cochrane 手册）[^higgins2024cochrane-e12]，研究的干预既有临床的，也有公共卫生和政策层面的[^higgins2024cochrane-e11]；报告有 PRISMA 2020 的 27 项清单[^page2021prisma-e1]。传统的证据金字塔把系统综述和元分析放在顶端[^murad2016new-e1]，但也有人主张把它从顶端拿掉，当作审视其他研究的"透镜"[^murad2016new-e6]：同样是元分析，合并低偏倚风险的随机对照试验，和合并高偏倚风险的观察性研究，不能等同看待[^murad2016new-e5]。
- **软件工程**：美国计算机协会软件工程分会的实证研究标准里，有专门的系统综述标准[^ralph2020empirical-e1]和案例调查标准[^ralph2020empirical-e291]。
- **管理学和信息系统**：案例调查用得很广；在软件工程里还少见[^ralph2022paving-e9]。
- **法学**：规范研究（对法律条文、判例的分析）不只是文献综述[^hutchinson2012defining-e8]，见[法学概况](../07_fields/law/README.md)。

其他学科（例如人文学科的研究综述）怎样看待综合，本文资料未涉及。

## 6. 常见错误

下面是套路层面的错误；检索、筛选、提取中的常见错误见[综述研究的常见错误](../06_methods/review_study.md#6-常见错误)。

| 错误 | 为什么是问题 |
|---|---|
| 没说清自己做的是哪类综述 | 读者和审稿人不知道该用哪套标准评价[^ralph2020empirical-e3] |
| 用挑选式的综述支撑"X 比 Y 好" | 挑出来的文献有偏差，撑不起实证结论[^ralph2022paving-e2] |
| 用计票法下结论 | 只数显著和不显著的篇数，方法有严重缺陷[^higgins2024cochrane-e18] |
| 把差异很大的研究硬合并成一个数 | 对象、做法、结局不够相似时，合并结果可能误导[^higgins2024cochrane-e15] |
| 在高质量研究很少的领域做系统综述 | 得不出可靠结论[^ralph2020empirical-e16]，不如先做映射研究[^kitchenham2007guidelines-e3] |
| 批判性综述里点名批评具体论文 | 增加的可信度抵不上对学术群体关系的损害，可以用假设的例子[^ralph2022paving-e19][^ralph2020empirical-e312] |
| 把案例调查里的相关当成因果 | 这是案例调查的反面模式[^ralph2020empirical-e304] |

## 7. 延伸阅读

- **综述类型的全貌**：Ralph 和 Baltes 2022，梳理了七类文献综述。先读这篇，再决定做哪一类。
- **系统综述的完整步骤**：Kitchenham 和 Charters 2007，软件工程领域的系统综述指南。
- **映射研究**：Petersen 等人 2008。
- **滚雪球检索**：Wohlin 2014。
- **报告规范**：系统综述和元分析的报告规范 PRISMA 2020（Page 等人 2021），含清单和流程图模板。
- **元分析**：Cochrane 手册（Higgins 等人 2024），先读第 1 章和第 10 章。
- **质量标准**：美国计算机协会软件工程分会（ACM SIGSOFT）实证研究标准中的系统综述、案例调查、元科学三项标准。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^acm2026csurguidelines-e1]: ACM Computing Surveys 作者指南，Long Survey Paper。[证据](../../sources/notes/acm2026csurguidelines.md#e1)
[^acm2026csurguidelines-e4]: ACM Computing Surveys 作者指南，Paper Length。[证据](../../sources/notes/acm2026csurguidelines.md#e4)
[^higgins2024cochrane-e3]: Cochrane 手册，第 1 章 §1.1。[证据](../../sources/notes/higgins2024cochrane.md#e3)
[^higgins2024cochrane-e4]: Cochrane 手册，第 1 章 §1.1。[证据](../../sources/notes/higgins2024cochrane.md#e4)
[^higgins2024cochrane-e11]: Cochrane 手册，第 1 章 §1.1。[证据](../../sources/notes/higgins2024cochrane.md#e11)
[^higgins2024cochrane-e12]: Cochrane 手册，第 1 章 §1.1。[证据](../../sources/notes/higgins2024cochrane.md#e12)
[^higgins2024cochrane-e14]: Cochrane 手册，第 10 章 §10.1。[证据](../../sources/notes/higgins2024cochrane.md#e14)
[^higgins2024cochrane-e15]: Cochrane 手册，第 10 章 §10.10.1。[证据](../../sources/notes/higgins2024cochrane.md#e15)
[^higgins2024cochrane-e16]: Cochrane 手册，第 10 章 §10.10.3。[证据](../../sources/notes/higgins2024cochrane.md#e16)
[^higgins2024cochrane-e18]: Cochrane 手册，第 12 章 Key Points。[证据](../../sources/notes/higgins2024cochrane.md#e18)
[^higgins2024cochrane-e21]: Cochrane 手册，第 7 章 Key Points。[证据](../../sources/notes/higgins2024cochrane.md#e21)
[^hutchinson2012defining-e8]: Hutchinson & Duncan 2012，§III B 1。[证据](../../sources/notes/hutchinson2012defining.md#e8)
[^kitchenham2007guidelines-e2]: Kitchenham & Charters 2007，§2。[证据](../../sources/notes/kitchenham2007guidelines.md#e2)
[^kitchenham2007guidelines-e3]: Kitchenham & Charters 2007，§2.5.1。[证据](../../sources/notes/kitchenham2007guidelines.md#e3)
[^kitchenham2007guidelines-e5]: Kitchenham & Charters 2007，§5.1。[证据](../../sources/notes/kitchenham2007guidelines.md#e5)
[^kitchenham2007guidelines-e6]: Kitchenham & Charters 2007，§5.3.1。[证据](../../sources/notes/kitchenham2007guidelines.md#e6)
[^kitchenham2007guidelines-e7]: Kitchenham & Charters 2007，§5.4。[证据](../../sources/notes/kitchenham2007guidelines.md#e7)
[^kitchenham2007guidelines-e8]: Kitchenham & Charters 2007，§5.4。[证据](../../sources/notes/kitchenham2007guidelines.md#e8)
[^kitchenham2007guidelines-e9]: Kitchenham & Charters 2007，§5.5。[证据](../../sources/notes/kitchenham2007guidelines.md#e9)
[^kitchenham2007guidelines-e11]: Kitchenham & Charters 2007，§6.2.2。[证据](../../sources/notes/kitchenham2007guidelines.md#e11)
[^kitchenham2007guidelines-e13]: Kitchenham & Charters 2007，§6.3。[证据](../../sources/notes/kitchenham2007guidelines.md#e13)
[^kitchenham2007guidelines-e15]: Kitchenham & Charters 2007，§6.4.3。[证据](../../sources/notes/kitchenham2007guidelines.md#e15)
[^murad2016new-e1]: Murad 等人 2016。[证据](../../sources/notes/murad2016new.md#e1)
[^murad2016new-e5]: Murad 等人 2016。[证据](../../sources/notes/murad2016new.md#e5)
[^murad2016new-e6]: Murad 等人 2016。[证据](../../sources/notes/murad2016new.md#e6)
[^murad2016new-e7]: Murad 等人 2016。[证据](../../sources/notes/murad2016new.md#e7)
[^page2021prisma-e1]: PRISMA 2020（Page 等人 2021）。[证据](../../sources/notes/page2021prisma.md#e1)
[^page2021prisma-e3]: PRISMA 2020，第 7 项。[证据](../../sources/notes/page2021prisma.md#e3)
[^page2021prisma-e4]: PRISMA 2020，第 16a 项。[证据](../../sources/notes/page2021prisma.md#e4)
[^petersen2008systematic-e4]: Petersen 等人 2008，§3.2。[证据](../../sources/notes/petersen2008systematic.md#e4)
[^petersen2008systematic-e7]: Petersen 等人 2008，摘要与 §1。[证据](../../sources/notes/petersen2008systematic.md#e7)
[^ralph2020empirical-e1]: SIGSOFT 系统综述标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e1)
[^ralph2020empirical-e3]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e3)
[^ralph2020empirical-e4]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e4)
[^ralph2020empirical-e6]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e6)
[^ralph2020empirical-e7]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e7)
[^ralph2020empirical-e9]: SIGSOFT 系统综述标准，加分项及脚注 3。[证据](../../sources/notes/ralph2020empirical.md#e9)
[^ralph2020empirical-e10]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e10)
[^ralph2020empirical-e13]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e13)
[^ralph2020empirical-e16]: SIGSOFT 系统综述标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e16)
[^ralph2020empirical-e291]: SIGSOFT 案例调查标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e291)
[^ralph2020empirical-e292]: SIGSOFT 案例调查标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e292)
[^ralph2020empirical-e293]: SIGSOFT 案例调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e293)
[^ralph2020empirical-e295]: SIGSOFT 案例调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e295)
[^ralph2020empirical-e301]: SIGSOFT 案例调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e301)
[^ralph2020empirical-e304]: SIGSOFT 案例调查标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e304)
[^ralph2020empirical-e312]: SIGSOFT 元科学标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e312)
[^ralph2022paving-e1]: Ralph & Baltes 2022，§2.1。[证据](../../sources/notes/ralph2022paving.md#e1)
[^ralph2022paving-e2]: Ralph & Baltes 2022，§2.1。[证据](../../sources/notes/ralph2022paving.md#e2)
[^ralph2022paving-e3]: Ralph & Baltes 2022，§2.2.5。[证据](../../sources/notes/ralph2022paving.md#e3)
[^ralph2022paving-e4]: Ralph & Baltes 2022，§2.2.5。[证据](../../sources/notes/ralph2022paving.md#e4)
[^ralph2022paving-e5]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e5)
[^ralph2022paving-e7]: Ralph & Baltes 2022，§2.2.3。[证据](../../sources/notes/ralph2022paving.md#e7)
[^ralph2022paving-e9]: Ralph & Baltes 2022，§2.2.3。[证据](../../sources/notes/ralph2022paving.md#e9)
[^ralph2022paving-e10]: Ralph & Baltes 2022，§3。[证据](../../sources/notes/ralph2022paving.md#e10)
[^ralph2022paving-e12]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e12)
[^ralph2022paving-e14]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e14)
[^ralph2022paving-e15]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e15)
[^ralph2022paving-e16]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e16)
[^ralph2022paving-e19]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e19)
[^ralph2022paving-e20]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e20)
