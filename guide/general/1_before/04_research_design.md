# 研究设计与方法选择

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲动手收集数据之前要想清楚的几件事：研究问题、方法、证据、样本和风险。具体某种方法（实验、问卷调查、案例研究等）的操作细节不在本章。[领域篇](../../07_fields/README.md)按领域整理研究类型文档，目前只有部分类型写好了，例如计算机领域的[综述研究](../../06_methods/review_study.md)。本章关于抽样和预注册的建议，主要来自软件工程领域的资料（ACM SIGSOFT，即美国计算机协会软件工程分会的实证研究标准，以及 Baltes & Ralph 的抽样指南），其他学科可能有自己的规范，可以对照使用。

**读完本章，你应该能：**

- 把一个宽泛的题目改写成能回答的研究问题，并写出你打算提出的主张；
- 按问题选方法，并按这种方法自己的标准判断研究做得好不好；
- 在收集数据之前想清楚，什么证据能说服一个持怀疑态度的读者；
- 分清探索性研究和验证性研究，知道验证性研究为什么要事先写好计划；
- 说明为什么选这些样本，不夸大样本的代表性；
- 用预研究或问题的简化版本，先检验设计中最没把握的部分。

---

## 1. 先把题目变成能回答的研究问题

"研究 X"只是一个方向，不是研究问题。动手之前，先写清你要解决什么问题、回答什么问题，以及它为什么重要[^shaw2003writing-e7][^ralph2020empirical-e22]。

**写下这四个问题的答案**[^shaw2003writing-e5]：

1. 我的贡献到底是什么？
2. 我要回答的是什么问题？
3. 读者为什么要关心？
4. 它关系到哪个更大的问题？

**判断问题属于哪一类。** 研究问题有哪几类、各自对应什么结果，见[什么是研究，什么是好的研究](01_what_is_good_research.md)中"弄清自己要做哪一类贡献"一节。这里只提醒一点：**问题类型一变，需要的结果和证据也跟着变** `[本项目分析]`。

**把预期结论写成一句话，再逐个分句检查。** 每个分句属于下面哪一种[^shaw2003writing-e16]？

| 主张类型 | 例子 | 通常需要的证据 |
|---|---|---|
| 全称主张 | "总是""完全" | 往往需要分析或证明 |
| 有限定的主张 | "提升 25%""对不含环的结构成立" | 可以用评估，或仔细考察实际使用经验 |
| 存在性主张 | "我们找到了一个实例" | 有时一个正面例子就够了 |

Shaw 指导博士生时发现，这样讨论之后，学生常会把主张改写得更准确；讨论得越早，学生越会围绕"能被证明的主张"来规划研究[^shaw2003writing-e17]。

**容易错在哪：** 用"研究了""探索了"描述目标。用表示结果的动词，而不是只表示付出和活动的动词[^shaw2003writing-e18]。把"我研究了 X"改成"我要证明 X 在什么条件下能达到什么效果"，问题就清楚多了 `[本项目分析]`。

## 2. 方法跟着问题走，用方法自己的标准衡量

**怎么做：**

- **方法要适合问题，但不必是最优的**[^ralph2020empirical-e23]。
- **问题、结果和验证方式不能随意搭配。** 用实地研究去验证一个形式化模型的正确性，和对一套经验法则做形式化证明一样不合适[^shaw2003writing-e14]。验证方式要和结果类型、获得结果的方法相匹配：形式化模型要靠严格推导和证明，而不是一两个简单例子[^shaw2003writing-e9]。
- **不要照搬别人的做法。** 盲目照搬别人为完全不同的问题用过的研究范式，会导致严重的不匹配[^shaw2003writing-e15]。
- **动手前先读这类研究的已有指南**，并遵守所选方法自己的规则[^ralph2020empirical-e26][^shaw2003writing-e13]。
- **用一句话写明你的研究立场**（例如实证主义还是诠释主义。粗略地说，实证主义认为现象可以客观测量、用数据检验规律；诠释主义关注人们怎样理解和赋予意义），否则读者或审稿人可能用不合适的标准来评判你[^baltes2022sampling-e6]。

**为什么：** 没有一套适用于所有研究的质量标准。每项研究都应该按适合它的方法的标准来评价；比如，对一项不涉及因果关系的研究，要求它证明因果关系的可靠性（内部效度）就是用错了标准[^ralph2020empirical-e24]。同样，确证的发现、观察和经验法则这几类结果，评判标准也不同，见[什么是研究，什么是好的研究](01_what_is_good_research.md)中"弄清自己要做哪一类贡献"一节。

**ACM SIGSOFT 实证研究标准把下列批评列为审稿时不成立的**[^ralph2020empirical-e25]；其他领域的审稿人未必认同，写作时仍应主动说明：

- 用另一种研究范式的规范来批评你的研究；
- 批评某类研究固有的局限，例如说案例研究"推广性低"；
- 只因为审稿人自己会用别的方法或设计而否定你的研究。

## 3. 收集数据之前，先想好什么证据能说服怀疑者

**先回答三个问题**[^shaw2003writing-e6]：读者凭什么相信你的结果？应该用什么标准评价你的主张？什么具体证据能表明结果满足了主张？

**怎么做：**

- **证据要对准主张。** 你主张性能提升，就要分析性能，而不是易用性或通用性[^shaw2003writing-e12]。定性研究同理 `[本项目分析]`：主张"受访者普遍感到 X"，就要给出足够的访谈材料和反例分析，而不是只引一两句。
- **"对我有效"不够。** 还需要证据表明它对别人也有用[^shaw2003writing-e11]。证据应来自实际经验或系统分析，而不只是说服性的论证或教科书式的例子[^shaw2002makes-e7]。但如果问题本身是"能不能做到"，一个能运行的系统就可能足以回答[^shaw2003writing-e10]。
- **先写草稿，再收集数据。** 实验没做也能写实验部分：写出完整设计，画出带行列标题和说明的空结果表[^eisnerfirst-e5]；诚实地写下来，可能会发现证明论点需要的工作比预想的多[^eisnerfirst-e6]。定性研究可以先列出计划中的发现或主题提纲 `[本项目分析]`。为什么、怎样先写，见[写作](../3_after/01_writing.md)中"尽早动笔，把写作当作研究的一部分"一节。
- **准备好比较的基线。** 在有数值结果的研究里，用简单或现成的方法作基线，它给出可达到效果的下限，复杂的方法常常还不如简单基线[^steinhardt2018stochastic-e7]。

**一个实用的做法** `[本项目分析]`：在收集数据前填一张表，每个主张一行。

| 主张 | 主张类型（全称/限定/存在） | 怀疑者会问什么 | 需要什么证据 | 怎么得到 |
|---|---|---|---|---|

填不出"需要什么证据"的主张，要么改写，要么删掉。

## 4. 分清探索性研究和验证性研究

- **验证性研究**：事先有明确的假设，用数据去检验它[^ralph2020empirical-e30]。
- **探索性研究**：事先不知道会发现什么，目的是摸清现象、产生想法或假设 `[本项目分析]`。

两种研究都有价值，但**不能把探索的结果包装成验证的结果**。在名为验证性的研究里，先看结果再提假设（HARKing，Hypothesizing After the Results are Known），或者只报告显著（统计上显著，即结果不太可能只是偶然造成）的那部分统计检验（p-hacking），都是反面模式[^ralph2020empirical-e27]。

**做验证性研究，先写计划，最好公开。** 预注册（pre-registration）就是在收集数据之前把研究计划公开存档，目的是防止先看结果再提假设、减少分析中无意识的偏差、对抗发表偏差（有"显著"结果的研究更容易发表，使文献整体偏向正面结果）[^ralph2020empirical-e29]。更进一步，可以分两阶段发表：先发表计划，再发表执行计划的结果[^ralph2020empirical-e28]。计划要写到：

- 详细到别人能照着完全重复你的数据收集和分析过程[^ralph2020empirical-e32]；
- 你提出的假设，能用你计划收集的数据来检验[^ralph2020empirical-e32]；
- 最好附上预研究等初步数据，说明所选方法合理[^ralph2020empirical-e35]。

**执行时偏离了计划怎么办？** 研究不可能完全按计划进行。只要有理由，且不是在知道修改会如何影响结果之后才改，偏离就可以接受[^ralph2020empirical-e34]。偏离不能以数据结果为理由；没有事先登记、事后追加的分析，要明确标为探索性的[^ralph2020empirical-e33]。

> **不同的看法：探索性研究要不要预注册？**
> - ACM SIGSOFT 实证研究标准的注册报告部分写明：它适用于检验假设的验证性研究，对诠释主义、定性或探索性研究做预注册"仍有争议"[^ralph2020empirical-e30]。
> - 同一份标准又把"以探索性或定性研究为由拒绝预注册"列为不成立的批评，认为各类研究都可以预注册[^ralph2020empirical-e31]。
>
> 实际操作中 `[本项目分析]`：验证性研究应当事先写好计划，有条件就预注册。探索性研究不一定要预注册，但最好也在开始前写下你打算看什么、怎么看；报告时如实标明哪些分析是事先计划的，哪些是看到数据后追加的。

## 5. 说清为什么选这些样本

先分清三个概念：**总体**是你想把结论推广到的全部对象；**抽样框**是你实际能从中抽取的对象名单；**样本**是你最终研究的那一部分。抽样框通常并不完美[^ralph2020empirical-e42]。

**怎么做：**

1. **写明抽样的目标**：是追求代表性，还是要找特殊案例，或者要达到理论饱和（新数据不再带来新发现）[^ralph2020empirical-e36][^baltes2022sampling-e6]。
2. **说明抽样策略为什么对这个目标合理**，不必最优[^ralph2020empirical-e36]。没有唯一最好的抽样方法，不同目的适合不同方法[^baltes2022sampling-e1]。
3. **说明样本是怎么选出来的**：定性研究要让读者看懂你选择研究对象的理由；定量研究要让读者能重复你的抽样过程[^baltes2022sampling-e7]。
4. **如果追求代表性**，先明确总体：原则上你想把结论推广到谁或什么上[^baltes2022sampling-e11]。
5. **样本量要有依据**：定量研究要大到能检测出预期大小的效应，定性研究要多到能达到饱和[^ralph2020empirical-e38]。反过来，别人随意规定一个最低样本量，既不基于统计功效分析（事先估算样本要多大，才有足够把握检测出预期的效应）也不基于饱和，这种批评不成立[^ralph2020empirical-e40]。

**几个常见误解：**

- **"随机抽的，所以有代表性。"** 代表性是样本和总体之间的关系，不是某种抽样技术自带的属性[^baltes2022sampling-e3]。随机抽样不能保证在你关心的维度上有代表性[^baltes2022sampling-e4]；抽样框本身有偏差时，样本再大也弥补不了[^baltes2022sampling-e5][^ralph2020empirical-e37]。
- **"方便找到的人就够了。"** 便利抽样（按方便拿到来选对象）又快又便宜，但会威胁结论能否推广[^baltes2022sampling-e2]。
- **"不追求代表性就不好意思说。"** 案例研究的目的是深入理解一个场景，不是从样本推广到总体，直接说明即可，不要因为对象是大公司或真实项目就假装它有代表性[^baltes2022sampling-e10]。研究本来就不以代表性为目标时，批评它缺乏代表性是不成立的[^ralph2020empirical-e39]。

**不要夸大样本的代表性**，这既无必要，也不科学[^baltes2022sampling-e8]。尤其不要在局限部分承认抽样偏差，到了结论又把结果写得几乎普遍适用[^baltes2022sampling-e9]。

## 6. 先用预研究或简化版本检验设计

项目里哪一部分最可能失败、为什么要先做它、怎样按信息量排序，见[推进研究](../2_during/01_making_progress.md)中"先做最可能失败的部分"一节。落到研究设计上，有两个常用办法：

- **先想问题的简化版本**，它常能提示或排除原问题的思路[^steinhardt2018stochastic-e8]；
- **做小规模的预研究**（pilot study，正式研究前的小规模试做），用初步数据说明所选方法合理[^ralph2020empirical-e35]。

结果可能让你修改设计，这是正常的：研究不是纯粹自上而下的，实验会反过来让你修改论文和计划[^eisnerfirst-e8]。

> **不同的看法：失败的结果值得发表吗？**
> - Steinhardt 认为，一次失败只覆盖了某个思路的极少数实现，所以他比多数人更不赞成发表负面结果，除非它附带了对失败原因的洞见[^steinhardt2018stochastic-e10][^steinhardt2018stochastic-e11]。
> - ACM SIGSOFT 实证研究标准把"因为报告了负面结果就否定研究"列为不成立的批评[^ralph2020empirical-e41]。
>
> 两者并不完全冲突 `[本项目分析]`：一项设计严谨、事先写明了假设的验证性研究，得到负面结果也是有效的结论；而"我试了一下 X，没成功"则需要说明试了哪些做法、为什么失败，才有参考价值。

---

## 本章检查清单

**问题与主张**

- [ ] 写明了研究问题，以及它为什么重要[^ralph2020empirical-e22]
- [ ] 把预期结论写成一句话，并判断了每个分句是全称、限定还是存在性主张[^shaw2003writing-e16]
- [ ] 用表示结果的动词描述目标，而不是"研究了""探索了"[^shaw2003writing-e18]

**方法与证据**

- [ ] 方法适合问题，并读过这类研究的已有指南[^ralph2020empirical-e23][^ralph2020empirical-e26]
- [ ] 验证方式和结果类型匹配，证据对准主张[^shaw2003writing-e9][^shaw2003writing-e12]
- [ ] 收集数据前，已经写好（或画好）空的结果表，或列出计划中的发现或主题提纲，知道每一项要证明什么[^eisnerfirst-e5]
- [ ] 有合适的比较基线（如适用）[^steinhardt2018stochastic-e7]

**探索与验证**

- [ ] 写明了研究是探索性还是验证性的 `[本项目分析]`
- [ ] 验证性研究在收集数据前写好了计划，有条件时公开存档[^ralph2020empirical-e29]
- [ ] 事后追加的分析标为探索性；偏离计划都有不依赖结果的理由[^ralph2020empirical-e33][^ralph2020empirical-e34]

**样本**

- [ ] 写明了抽样目标、抽样策略和它为什么合理[^ralph2020empirical-e36]
- [ ] 如果追求代表性，写明了总体，并考虑了抽样框的偏差[^baltes2022sampling-e11][^baltes2022sampling-e5]
- [ ] 样本量有依据（统计功效或饱和）[^ralph2020empirical-e38]
- [ ] 结论没有超出样本能支撑的范围[^baltes2022sampling-e9]

**风险**

- [ ] 用预研究或简化版本，先检验了设计中最没把握的部分[^ralph2020empirical-e35][^steinhardt2018stochastic-e8]
- [ ] 在做实验前，把研究计划或论文开头给导师或同行看过[^eisnerfirst-e3]

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只有方向，没有研究问题 | 不知道要什么结果、要什么证据[^shaw2003writing-e7][^shaw2002makes-e1] |
| 照搬上一篇论文的方法 | 问题不同，方法可能严重不匹配[^shaw2003writing-e15] |
| 用一两个例子"验证"一个普遍主张 | 全称主张往往需要分析或证明[^shaw2003writing-e16][^shaw2003writing-e9] |
| 证据和主张对不上 | 主张性能提升却只展示易用性，等于没证明[^shaw2003writing-e12] |
| 用别的方法的标准评判自己或别人的研究 | 没有通用的质量标准，应按方法自己的标准评判[^ralph2020empirical-e24] |
| 看完数据再提假设，当作事先的假设报告 | 这是 HARKing，会让验证性结论失去意义[^ralph2020empirical-e27] |
| 认为随机抽样就有代表性 | 代表性不是抽样技术的属性；抽样框有偏差时随机也无用[^baltes2022sampling-e3][^baltes2022sampling-e5] |
| 局限里承认偏差，结论里写成普遍规律 | 结论超出了证据[^baltes2022sampling-e9] |
| 先做容易的部分，把最不确定的留到最后 | 可能在最后才发现整个计划不可行[^steinhardt2018stochastic-e2] |
| 一次实验失败就放弃整个思路 | 只排除了一种实现，不是整个思路[^steinhardt2018stochastic-e10] |

## 延伸阅读

- **Shaw 2003, Writing Good Software Engineering Research Papers**：用"研究问题—结果—验证"三个维度检查一项研究；§5 的主张拆解方法虽以软件工程为例，思路也可借鉴到其他学科 `[本项目分析]`。
- **Shaw 2002, What Makes Good Research in Software Engineering?**：同一框架的较早版本，另有 Brooks 关于"发现、观察、经验法则"三类结果的讨论。
- **ACM SIGSOFT Empirical Standards**：General Standard 列出所有实证研究的基本要求、反面模式和不成立的批评；Sampling 和 Registered Reports 两个补充文件分别讲抽样和预注册。适合在设计阶段当作清单用。
- **Baltes & Ralph 2022, Sampling in Software Engineering Research**：讲清代表性、随机和抽样框的关系，§6 有可直接照做的建议。
- **Steinhardt 2018, Research as a Stochastic Decision Process**：怎样给项目去风险、怎样安排任务顺序。
- **Eisner 2010, Write the Paper First**：为什么以及怎样在做实验之前先写论文草稿。

各资料的链接见[原始资料列表](../../../sources/README.md)。

[^shaw2003writing-e5]: Shaw 2003，§1。[证据](../../../sources/notes/shaw2003writing.md#e5)
[^shaw2003writing-e6]: Shaw 2003，§1。[证据](../../../sources/notes/shaw2003writing.md#e6)
[^shaw2003writing-e7]: Shaw 2003，§2。[证据](../../../sources/notes/shaw2003writing.md#e7)
[^shaw2003writing-e9]: Shaw 2003，§4.1。[证据](../../../sources/notes/shaw2003writing.md#e9)
[^shaw2003writing-e10]: Shaw 2003，§4.1。[证据](../../../sources/notes/shaw2003writing.md#e10)
[^shaw2003writing-e11]: Shaw 2003，§4.3。[证据](../../../sources/notes/shaw2003writing.md#e11)
[^shaw2003writing-e12]: Shaw 2003，§4.3。[证据](../../../sources/notes/shaw2003writing.md#e12)
[^shaw2003writing-e13]: Shaw 2003，§4.3。[证据](../../../sources/notes/shaw2003writing.md#e13)
[^shaw2003writing-e14]: Shaw 2003，§5。[证据](../../../sources/notes/shaw2003writing.md#e14)
[^shaw2003writing-e15]: Shaw 2003，§5。[证据](../../../sources/notes/shaw2003writing.md#e15)
[^shaw2003writing-e16]: Shaw 2003，§5。[证据](../../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e17]: Shaw 2003，§5。[证据](../../../sources/notes/shaw2003writing.md#e17)
[^shaw2003writing-e18]: Shaw 2003，§3.3。[证据](../../../sources/notes/shaw2003writing.md#e18)
[^shaw2002makes-e1]: Shaw 2002，§1。[证据](../../../sources/notes/shaw2002makes.md#e1)
[^shaw2002makes-e7]: Shaw 2002，§2.3。[证据](../../../sources/notes/shaw2002makes.md#e7)
[^ralph2020empirical-e22]: ACM SIGSOFT（美国计算机协会软件工程分会）实证研究标准，General Standard，必要项。[证据](../../../sources/notes/ralph2020empirical.md#e22)
[^ralph2020empirical-e23]: SIGSOFT General Standard，必要项。[证据](../../../sources/notes/ralph2020empirical.md#e23)
[^ralph2020empirical-e24]: SIGSOFT General Standard，General Quality Criteria。[证据](../../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e25]: SIGSOFT General Standard，不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e26]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e26)
[^ralph2020empirical-e27]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e28]: SIGSOFT General Standard，加分项。[证据](../../../sources/notes/ralph2020empirical.md#e28)
[^ralph2020empirical-e29]: SIGSOFT Registered Reports 补充文件，定义。[证据](../../../sources/notes/ralph2020empirical.md#e29)
[^ralph2020empirical-e30]: SIGSOFT Registered Reports 补充文件，适用范围。[证据](../../../sources/notes/ralph2020empirical.md#e30)
[^ralph2020empirical-e31]: SIGSOFT Registered Reports 补充文件，不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e31)
[^ralph2020empirical-e32]: SIGSOFT Registered Reports 补充文件，RR1 必要项。[证据](../../../sources/notes/ralph2020empirical.md#e32)
[^ralph2020empirical-e33]: SIGSOFT Registered Reports 补充文件，RR2 必要项。[证据](../../../sources/notes/ralph2020empirical.md#e33)
[^ralph2020empirical-e34]: SIGSOFT Registered Reports 补充文件，Justifying Deviations。[证据](../../../sources/notes/ralph2020empirical.md#e34)
[^ralph2020empirical-e35]: SIGSOFT Registered Reports 补充文件，RR1 加分项。[证据](../../../sources/notes/ralph2020empirical.md#e35)
[^ralph2020empirical-e36]: SIGSOFT Sampling 补充文件，必要项。[证据](../../../sources/notes/ralph2020empirical.md#e36)
[^ralph2020empirical-e37]: SIGSOFT Sampling 补充文件，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e37)
[^ralph2020empirical-e38]: SIGSOFT Sampling 补充文件，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e38)
[^ralph2020empirical-e39]: SIGSOFT Sampling 补充文件，不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e39)
[^ralph2020empirical-e40]: SIGSOFT General Standard，不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e40)
[^ralph2020empirical-e41]: SIGSOFT General Standard，不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e42]: SIGSOFT Sampling 补充文件，适用范围。[证据](../../../sources/notes/ralph2020empirical.md#e42)
[^baltes2022sampling-e1]: Baltes & Ralph 2022，§2。[证据](../../../sources/notes/baltes2022sampling.md#e1)
[^baltes2022sampling-e2]: Baltes & Ralph 2022，§2.1.1。[证据](../../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e3]: Baltes & Ralph 2022，§2.6。[证据](../../../sources/notes/baltes2022sampling.md#e3)
[^baltes2022sampling-e4]: Baltes & Ralph 2022，§2.6。[证据](../../../sources/notes/baltes2022sampling.md#e4)
[^baltes2022sampling-e5]: Baltes & Ralph 2022，§2.6。[证据](../../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e6]: Baltes & Ralph 2022，§6。[证据](../../../sources/notes/baltes2022sampling.md#e6)
[^baltes2022sampling-e7]: Baltes & Ralph 2022，§6。[证据](../../../sources/notes/baltes2022sampling.md#e7)
[^baltes2022sampling-e8]: Baltes & Ralph 2022，§6。[证据](../../../sources/notes/baltes2022sampling.md#e8)
[^baltes2022sampling-e9]: Baltes & Ralph 2022，§6。[证据](../../../sources/notes/baltes2022sampling.md#e9)
[^baltes2022sampling-e10]: Baltes & Ralph 2022，§6。[证据](../../../sources/notes/baltes2022sampling.md#e10)
[^baltes2022sampling-e11]: Baltes & Ralph 2022，§6。[证据](../../../sources/notes/baltes2022sampling.md#e11)
[^steinhardt2018stochastic-e2]: Steinhardt 2018，Warm-Up。[证据](../../../sources/notes/steinhardt2018stochastic.md#e2)
[^steinhardt2018stochastic-e7]: Steinhardt 2018，Some further practical ideas。[证据](../../../sources/notes/steinhardt2018stochastic.md#e7)
[^steinhardt2018stochastic-e8]: Steinhardt 2018，Some further practical ideas。[证据](../../../sources/notes/steinhardt2018stochastic.md#e8)
[^steinhardt2018stochastic-e10]: Steinhardt 2018，Exponentially branching search trees。[证据](../../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e11]: Steinhardt 2018，Exponentially branching search trees。[证据](../../../sources/notes/steinhardt2018stochastic.md#e11)
[^eisnerfirst-e3]: Eisner 2010，Is it a good topic?。[证据](../../../sources/notes/eisnerfirst.md#e3)
[^eisnerfirst-e5]: Eisner 2010，What needs to be done?。[证据](../../../sources/notes/eisnerfirst.md#e5)
[^eisnerfirst-e6]: Eisner 2010，What needs to be done?。[证据](../../../sources/notes/eisnerfirst.md#e6)
[^eisnerfirst-e8]: Eisner 2010，The document is like a code specification。[证据](../../../sources/notes/eisnerfirst.md#e8)
