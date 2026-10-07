# 案例调查：把已发表的案例研究编码成数据集

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲**案例调查**（case survey，又称案例元分析，case meta-analysis）：把别人已经发表的大量案例研究收集起来，用统一的编码方案把其中的定性描述转换成数据，再做定量分析。

如果你要亲自深入研究一个或几个案例，见[案例研究](case_study.md)；如果你要综述的是实验等其他类型的研究，见[综述研究](review_study.md)。

**适用范围** `[本项目分析]`：本文的规范和例子主要来自软件工程：检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，误用的分析来自对软件工程论文的调查。这种方法的经典方法论文发表在管理学期刊上（见延伸阅读），它在管理学和信息系统领域用得更多（见第 1 节）。其他学科做同类研究时，先看本学科的方法文献和规范。

**常服务的套路**：[综合](../05_research-strategies/synthesize.md)。

**读完本文，你应该能：**

- 判断自己的问题适不适合用案例调查，以及它和单个案例研究、系统综述的区别；
- 按步骤完成一项案例调查：找案例、设计编码方案、多人编码、分析；
- 认出这类研究最常见的误用；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为：把已发表案例研究中的定性描述系统地转换成定量数据并加以分析，以期对一个复杂现象得出可推广结论的研究[^ralph2020empirical-e291]。它想兼得两种方法的长处：调查研究的可推广性，和案例研究的深度[^melegati2020case-e1]。

这里的"案例研究"取最广义的理解：对某些事件的学术性记述；经验报告和灰色文献（没有经过正式出版渠道发表的材料）要不要纳入，取决于研究目的[^ralph2022paving-e6]。它的思路接近元分析（用统计方法合并多项研究的结果）：通常从事先定好的假设和编码方案出发，最后得到一个可以做假设检验的数据集[^ralph2022paving-e7]。和元分析一样，它综合许多研究的结果，回答关于现实世界的具体实证问题，这些问题常常是因果问题[^ralph2022paving-e11]，例如"开回顾会议的团队，项目是不是更容易成功？" `[本项目分析]`

**问题是因果的，证据却是相关的，要分清这两层**：研究者关心的往往是"A 会不会导致 B"，但案例调查手里的数据只能显示"有 A 的案例里 B 是否更常见"，也就是相关。案例不是在受控条件下得到的，其他因素无法排除 `[本项目分析]`；而且数据稀疏，通常只能做简单的两变量相关[^ralph2022paving-e8]。所以，因果问题可以作为研究的出发点和假设，但写结论时要说"A 与 B 相关"，不能说"A 导致 B" `[本项目分析]`；把相关写成因果，是标准明确列出的反面模式[^ralph2020empirical-e304]。

**和相近类型的区别**（表中没有脚注的格子为 `[本项目分析]`）：

| | 案例研究 | 多案例研究 | 系统综述 | 案例调查 |
|---|---|---|---|---|
| 数据来源 | 自己收集的一手数据 | 自己收集的一手数据 | 已发表的各类研究 | 已发表的案例研究 |
| 案例数 | 一个 | 几个，受精力限制[^melegati2020case-e10] | 不适用 | 越多越好，统计检验需要大量案例[^melegati2020case-e4] |
| 分析 | 以定性为主 | 以定性为主，可做跨案例比较 | 描述性综合或元分析 | 编码后做定量统计[^melegati2020case-e3] |
| 典型问题 | "这里发生了什么、为什么？" | "几个案例有什么异同？" | "关于问题 X，现有证据说明了什么？" | "在大量案例中，因素 A 和结果 B 有没有关联？" |

几点说明：

- **和多案例研究的区别**：多案例研究也能做跨案例分析，但它投入很大，案例数通常达不到统计分析的要求；而且所有案例由同一个人用同样的目的、视角、方法和理论框架完成[^melegati2020case-e10]。案例调查用的是不同作者、出于不同目的写的案例。
- **和系统综述的区别**：两者都以综合证据为目标；但系统综述可以纳入各种方法的研究，案例调查只分析描述案例的研究，并且只用编码后的定量数据做分析[^melegati2020case-e11]。综述实验等其他研究，用系统综述的标准；把多个定性研究综合成主题（如元民族志、叙事综合），也不属于案例调查[^ralph2020empirical-e292]。
- **不是"自己调查很多实例"**：自己用问卷或访谈从大量实例收集一手数据，不是案例调查[^ralph2020empirical-e292]，应按问卷调查或定性调查的要求来做。

**什么时候用**：当一个主题已经积累了**大量**已发表的案例研究，而你想检验某个因素和某个结果之间是否有规律时。因为编码得到的数据很稀疏，案例调查需要很多案例才做得起来[^ralph2022paving-e10]。

案例调查在管理学和信息系统领域用得很广，在软件工程里还少见；Ralph & Baltes 认为，软件工程里案例研究很多，所以这种方法很有潜力[^ralph2022paving-e9]。在计算机的其他方向，例如系统和安全领域公开的事故分析报告，原则上也可以作为"案例"来编码，但这类材料是否够得上"学术性记述"、信息是否足够，要逐一判断 `[本项目分析]`。

**一个常见的误用**：Melegati & Wang 调查了 12 篇自称做了案例调查的软件工程论文，发现它们大多没有按方法原本的定义来做[^melegati2020case-e2]。最常见的情况是：把每份问卷答案或每篇博客文章当成一个"案例"；其余的是案例数较多的多案例研究[^melegati2020case-e12]。一份问卷答案或一篇博客通常只来自一个人，深度和广度都不够，也没有多个来源可以相互印证，算不上一个案例[^melegati2020case-e13]。

---

## 2. 怎么做

Larsson 1993 把方法概括为四步：选一组已有的案例研究；设计编码方案；由多名编码者编码；统计分析[^melegati2020case-e3]。下面按这个顺序展开。

### 第一步：写清研究问题和假设

案例调查可以用来检验假设，也可以用来探索，但选什么案例要有理论依据[^melegati2020case-e4]。通常在动手前就写好假设，再从假设推出要编码哪些变量[^ralph2022paving-e7]。

**容易错在哪**：先读一堆案例，再看能挖出什么相关性。这样做出的"发现"很可能是偶然的；先定假设，等于提前约束自己 `[本项目分析]`。探索和验证的区别，见[从研究问题到证据清单：分清你是在检验，还是在探索](../02_from-project-to-study/01_question-to-evidence.md#5-分清你是在检验还是在探索)。

### 第二步：找案例、选案例

**检索**：检索过程要一步步写清、可以复现；案例不必来自同行评审的刊物[^ralph2020empirical-e293]。要组合几种检索方式减轻抽样偏差和发表偏差[^ralph2020empirical-e294]，具体做法（关键词检索、滚雪球、查预印本和学位论文等）和系统综述一样，见[综述研究](review_study.md#2-系统综述怎么做)。

**纳入标准看"报告了多少信息"，不看"发在哪里"**[^melegati2020case-e4]。标准中的例子是：至少报告了编码方案中的两个变量[^ralph2020empirical-e293]。Larsson 研究企业并购时，要求每个案例至少有两页描述业务和人员方面的问题[^melegati2020case-e5]。

**容易错在哪**：

- 不审视信息是否够用，把找到的案例全部纳入[^ralph2020empirical-e304]；
- 纳入根本不是案例研究的材料，例如问卷、只有一两句话的报道[^ralph2020empirical-e304]。

### 第三步：设计编码方案

编码方案规定怎样把定性描述转换成定量变量[^ralph2020empirical-e295]，可以把它看作一份由研究者对照案例来填写的问卷 `[本项目分析]`。变量常常是简单的是/否题，例如"团队开没开回顾会议？"[^ralph2022paving-e8]

设计时要在两头之间权衡：简单的方案省力、编码结果更可靠；复杂的方案信息更丰富[^melegati2020case-e6][^ralph2020empirical-e295]。

几个要求：

- 在正文详细描述编码方案，或者放进补充材料[^ralph2020empirical-e295]；最好说明为什么这样设计[^ralph2020empirical-e298]。
- **事先想好缺失值怎么处理**，并在论文里写清[^ralph2020empirical-e296]。很多案例不会提到你关心的所有变量；"没提到"该编码成"否"、编码成"缺失"，还是排除这个案例，会直接影响结果 `[本项目分析]`。
- 先用几个案例试编码，修改含糊的题目和判定规则，再正式编码 `[本项目分析]`。

### 第四步：多人独立编码，检验一致性

- 至少两名、最好三名编码者[^melegati2020case-e7]，各自独立编码，并分析编码者之间的一致性（不同编码者对同一案例的判断有多一致）[^ralph2020empirical-e299]。一致性统计量的选法和常见错误，见计算机实践篇[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md#第六步人工标注并检验一致性)。
- 一致性是衡量编码质量的关键指标，但不必过度纠结于它[^melegati2020case-e7]。
- 说明分歧怎么解决：讨论达成一致、投票、请一名裁决人，或咨询原作者[^ralph2020empirical-e299]。
- **可以请原作者帮忙。** 原作者接触过一手数据，有些信息可能因为篇幅限制没写进论文[^melegati2020case-e8]。联系原作者获取信息、核对编码，是加分项[^ralph2020empirical-e300]；请原作者直接参与编码，是优秀项[^ralph2020empirical-e303]。

### 第五步：分析

- **用定量方法分析，并真正做综合。** 用定性方法分析案例，或者逐个描述案例而不综合，都是反面模式[^ralph2020empirical-e304]。结论要建立在编码得到的变量上[^ralph2020empirical-e296]。
- **方法要和数据相称。** 编码得到的数据集常常太稀疏，做不了回归建模，研究者通常用简单的两变量相关来检验假设[^ralph2022paving-e8]。
- **结论写成相关，不写成因果**[^ralph2020empirical-e304]。即使研究问题本身是因果问题，这种数据也只能支持相关，理由见上文[这是什么研究，什么时候用](#1-这是什么研究什么时候用) `[本项目分析]`。
- **检查原始研究的特征是否影响了编码**，例如研究设计、发表刊物、发表年份[^melegati2020case-e9][^ralph2020empirical-e303]。
- 用事先定好的方案评估原始研究的质量，并把质量作为调节变量（可能改变因素与结果之间关系强弱的变量）放进分析，看它是否改变结论[^ralph2020empirical-e301]；不要用发表刊物的档次代替质量评估[^ralph2020empirical-e304]。

### 第六步：报告

公开研究方案、检索词、筛选结果、编码方案、编码示例、判定规则、完整数据集和分析脚本[^ralph2020empirical-e298]；用表格和图汇总结果，附 PRISMA 流程图（系统综述常用的筛选流程图，见[综述研究](review_study.md)）；把有证据的结果和你的解读、推测分开写[^ralph2020empirical-e302]。

---

## 3. 局限：你的数据只是别人写下的东西

案例调查的每一个数据点，都来自别人为别的目的写的报告。这带来几个躲不开的局限，要在论文里写清[^ralph2020empirical-e18]：

- **报告里没写，不等于没发生。** 有些信息可能因为篇幅限制没写进报告[^melegati2020case-e8]。这就是为什么缺失值的处理要事先定好、写清[^ralph2020empirical-e296]。
- **案例不代表总体。** 被写成论文的案例，往往是作者能接触到、又觉得值得写的案例 `[本项目分析]`。必须讨论纳入的案例和你想推论的总体可能有哪些不同[^ralph2020empirical-e297]。
- **原始研究质量参差不齐。** 所以要评估质量，并检验它是否影响结论[^ralph2020empirical-e301]。

**审稿时常见、但不成立的批评**[^ralph2020empirical-e305]：

- "原始研究没有在同行评审的刊物上发表"
- "原始研究的设计各不相同"
- "案例不是该现象的随机样本"

---

## 4. 检查清单

下面依据 ACM SIGSOFT 的案例调查标准，它是为软件工程写的。

**必须做到**

- [ ] 一步步、可复现地描述检索过程[^ralph2020empirical-e293]
- [ ] 给出明确的案例纳入和排除标准[^ralph2020empirical-e293]
- [ ] 组合几种检索方式，减轻抽样偏差和发表偏差[^ralph2020empirical-e294]
- [ ] 定义编码方案，在正文描述或放进补充材料[^ralph2020empirical-e295]
- [ ] 说清缺失值怎么处理[^ralph2020empirical-e296]
- [ ] 结论建立在编码得到的定量变量上[^ralph2020empirical-e296]
- [ ] 讨论纳入的案例和目标总体可能有什么不同[^ralph2020empirical-e297]

**做到更好**

- [ ] 公开方案、检索结果、编码方案、示例、数据和脚本；说明编码方案的设计理由[^ralph2020empirical-e298]
- [ ] 两人以上独立编码，分析一致性，说明分歧怎么解决[^ralph2020empirical-e299]
- [ ] 联系原作者获取信息或核对编码[^ralph2020empirical-e300]
- [ ] 评估原始研究质量，并作为变量放进分析[^ralph2020empirical-e301]
- [ ] 用图表汇总结果，附 PRISMA 流程图；区分证据和推测[^ralph2020empirical-e302]

**做得出色**[^ralph2020empirical-e303]

- [ ] 用理论指导案例的选择和抽样
- [ ] 为选中的案例补充其他来源的数据
- [ ] 请原作者参与编码或确认解读
- [ ] 分析研究设计、发表刊物、年份等是否影响编码

---

## 5. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 把问卷答案、博客文章当成"案例" | 信息太浅、来源单一，算不上案例研究[^melegati2020case-e13][^ralph2020empirical-e304] |
| 把几个自己做的案例叫作案例调查 | 这是多案例研究，案例数也撑不起统计分析[^melegati2020case-e10][^melegati2020case-e12] |
| 不看信息是否够用，找到就纳入 | 标准列为反面模式[^ralph2020empirical-e304]；大量变量只能编成缺失 `[本项目分析]` |
| 编码后又回到定性分析，或逐个介绍案例 | 失去了这种方法的意义：没有定量综合[^ralph2020empirical-e304] |
| 只有一个人编码 | 编码可靠性无从判断[^ralph2020empirical-e299] |
| 用发表刊物的档次代替质量评估 | 刊物档次不等于单篇研究的质量[^ralph2020empirical-e304] |
| 把相关写成因果 | 标准列为反面模式[^ralph2020empirical-e304]；问题可以是因果的，但这种数据只能支持相关 `[本项目分析]` |
| 自称案例调查，却不按方法要求来做 | 偏离方法又不反思后果，结论的效度会受到质疑[^melegati2020case-e14] |

---

## 6. 延伸阅读

- **先读这篇**：Melegati & Wang 2020。梳理了案例调查的经典定义和步骤，并分析了软件工程中的误用。
- **在各种综述里的位置**：Ralph & Baltes 2022 §2.2.3，简要说明案例调查和元分析、元综合的区别。
- **软件工程的专门指南**：Petersen 2020，*Guidelines for Case Survey Research in Software Engineering*（Springer 出版的 *Contemporary Empirical Methods in Software Engineering* 一书的一章）。本项目没有读到可合法获取的全文 `[待确认]`。
- **经典方法论文**：Larsson 1993（*Academy of Management Journal*），本文对它的介绍转引自 Melegati & Wang，没有读原文 `[待确认]`。
- **检查清单的来源**：ACM SIGSOFT 案例调查标准，附有管理学和信息系统领域的范例论文。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e291]: SIGSOFT 案例调查标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e291)
[^ralph2020empirical-e292]: SIGSOFT 案例调查标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e292)
[^ralph2020empirical-e293]: SIGSOFT 案例调查标准，必要项及脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e293)
[^ralph2020empirical-e294]: SIGSOFT 案例调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e294)
[^ralph2020empirical-e295]: SIGSOFT 案例调查标准，必要项及脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e295)
[^ralph2020empirical-e296]: SIGSOFT 案例调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e296)
[^ralph2020empirical-e297]: SIGSOFT 案例调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e297)
[^ralph2020empirical-e298]: SIGSOFT 案例调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e298)
[^ralph2020empirical-e299]: SIGSOFT 案例调查标准，加分项及脚注 4。[证据](../../sources/notes/ralph2020empirical.md#e299)
[^ralph2020empirical-e300]: SIGSOFT 案例调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e300)
[^ralph2020empirical-e301]: SIGSOFT 案例调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e301)
[^ralph2020empirical-e302]: SIGSOFT 案例调查标准，加分项及脚注 5。[证据](../../sources/notes/ralph2020empirical.md#e302)
[^ralph2020empirical-e303]: SIGSOFT 案例调查标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e303)
[^ralph2020empirical-e304]: SIGSOFT 案例调查标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e304)
[^ralph2020empirical-e305]: SIGSOFT 案例调查标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e305)
[^ralph2020empirical-e18]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e18)
[^ralph2022paving-e6]: Ralph & Baltes 2022，§2.2.3。[证据](../../sources/notes/ralph2022paving.md#e6)
[^ralph2022paving-e7]: Ralph & Baltes 2022，§2.2.3。[证据](../../sources/notes/ralph2022paving.md#e7)
[^ralph2022paving-e8]: Ralph & Baltes 2022，§2.2.3。[证据](../../sources/notes/ralph2022paving.md#e8)
[^ralph2022paving-e9]: Ralph & Baltes 2022，§2.2.3。[证据](../../sources/notes/ralph2022paving.md#e9)
[^ralph2022paving-e10]: Ralph & Baltes 2022，§3。[证据](../../sources/notes/ralph2022paving.md#e10)
[^ralph2022paving-e11]: Ralph & Baltes 2022，§3 与 §3.1。[证据](../../sources/notes/ralph2022paving.md#e11)
[^melegati2020case-e1]: Melegati & Wang 2020，摘要。[证据](../../sources/notes/melegati2020case.md#e1)
[^melegati2020case-e2]: Melegati & Wang 2020，摘要。[证据](../../sources/notes/melegati2020case.md#e2)
[^melegati2020case-e3]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e3)
[^melegati2020case-e4]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e4)
[^melegati2020case-e5]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e5)
[^melegati2020case-e6]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e6)
[^melegati2020case-e7]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e7)
[^melegati2020case-e8]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e8)
[^melegati2020case-e9]: Melegati & Wang 2020，§2。[证据](../../sources/notes/melegati2020case.md#e9)
[^melegati2020case-e10]: Melegati & Wang 2020，§2.1。[证据](../../sources/notes/melegati2020case.md#e10)
[^melegati2020case-e11]: Melegati & Wang 2020，§2.1。[证据](../../sources/notes/melegati2020case.md#e11)
[^melegati2020case-e12]: Melegati & Wang 2020，§6。[证据](../../sources/notes/melegati2020case.md#e12)
[^melegati2020case-e13]: Melegati & Wang 2020，§5。[证据](../../sources/notes/melegati2020case.md#e13)
[^melegati2020case-e14]: Melegati & Wang 2020，§5。[证据](../../sources/notes/melegati2020case.md#e14)
