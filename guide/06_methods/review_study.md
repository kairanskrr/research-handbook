# 综述研究：系统综述、映射研究与综述论文

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲**以综述本身为成果的研究**：把别人已发表的研究收集起来，汇总、分析，最后写成一篇独立的论文。

如果你想了解的是"做自己的研究之前怎么读文献、怎么写相关工作"，那是每项研究都有的一个环节，见[进入领域、探索文献](../01_from-interest-to-project/01_enter-a-field.md)。

**适用范围** `[本项目分析]`：本文的规范和例子主要来自计算机，尤其是软件工程：系统综述的做法依据 Kitchenham & Charters 为软件工程写的指南，检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，综述论文的要求依据 ACM Computing Surveys 的作者指南；报告规范 PRISMA 源自医学。其他学科做综述时，先看本学科的规范。健康领域的系统综述与元分析（效应指标、异质性、证据分级等）见[系统综述与元分析（健康领域）](../07_fields/health-sciences/research-types/meta_analysis.md)。

**常服务的套路**：[综合](../05_research-strategies/synthesize.md)；文献里可能已有答案时，也服务[观察描述](../05_research-strategies/observe_describe.md)。

**读完本文，你应该能：**

- 分清三种常见的综述，并为自己的问题选对一种；
- 按步骤完成一篇系统综述或映射研究；
- 写出一篇有价值的综述论文，而不是一份论文清单；
- 用文末的检查清单检查自己的综述。

---

## 1. 先选对类型

计算机领域常见三种综述。它们的区别不在"读了多少篇"，而在**要回答什么问题、要多严格**。

| | 综述论文（survey paper） | 映射研究（mapping study） | 系统综述（systematic review） |
|---|---|---|---|
| 回答的问题 | 这个领域有哪些重要工作，该怎么理解它们？ | 这个领域有哪些研究，分布在哪里，哪里还是空白？ | 关于某个具体问题，现有证据说明了什么？ |
| 怎么找论文 | 作者有目的地挑选 | 按事先定好的方案检索，尽量找全 | 按事先定好的方案检索，尽量找全 |
| 评估每篇论文的质量吗 | 一般不 | 一般不 | 要 |
| 主要产出 | 分类框架、对领域的视角、趋势判断 | 分类和计数，画出"研究地图" | 基于证据的结论和建议 |

依据：综述论文的定义见 ACM Computing Surveys[^csur-e1]；映射研究与系统综述的区别见 Petersen 等人[^pe-e3][^pe-e4]。"有目的地挑选"指 Ralph & Baltes 所说的非系统综述（ad hoc review）：作者挑选有用、相关或支持自己观点的文献[^rb-e1]；综述论文通常属于这一类。`[本项目分析]`

**怎么选** `[本项目分析，依据下列资料]`：

- **想给一个领域画张全景图、给读者一个理解框架**：写综述论文。这是计算机领域最常见的综述形式。
- **领域很宽，或者还不清楚有多少相关研究**：先做映射研究。证据很少或主题很宽时，Kitchenham（Barbara Kitchenham，软件工程系统综述指南的作者）建议先做映射研究，找出研究扎堆和空白的地方[^kc-e3]。
- **要回答一个具体问题，例如"方法 A 是否比方法 B 更能发现缺陷"**：做系统综述。这类实证结论需要系统检索、并评估每篇研究质量的综述来支撑，例如系统综述，或元分析（用统计方法把多项研究的数值结果合并起来）；挑选式的综述撑不起来[^kc-e2][^rb-e2]。

这三种并不是截然分开的。映射研究读得越深，就越像系统综述，两者可以看作一条连续谱上的不同位置[^pe-e6]。

> **不同的看法：映射研究值不值得做？**
> - Petersen 等人认为映射研究和系统综述目标不同，应当互相补充，映射研究的适用面比通常认为的更广[^pe-e7]。
> - Ralph & Baltes 对范围综述（scoping review，与映射研究相近[^rb-e3]）的看法是：以描述和计数为主的范围综述通常回答不了重要的实证问题，"本质上是半成品"，更适合 workshop（依附于大型会议的研讨会，录用门槛较低）或短文；如果文献足够做综合，它更像是正式系统综述前的预研[^rb-e4][^rb-e5]。
>
> 实际操作中可以这样理解：映射研究本身是有用的，但**只有分类和计数是不够的**。能往综合和结论方向多走一步，价值就大很多。

---

## 2. 系统综述怎么做

按软件工程的系统综述指南，系统综述的核心要求是**全面、公正、可复现**。Kitchenham & Charters 的这份指南开宗明义：文献综述如果不全面、不公正，就没有多少科学价值[^kc-e1]。整个过程分为三个阶段：规划、执行、报告[^kc-e4]。

### 第一阶段：规划

**1. 确认值得做。** 动手之前先确认这个综述确实需要做，例如查一查有没有人已经做过类似的综述[^kc-e5]。有的话，想清楚你的综述能补上什么，例如覆盖新的时间段，或回答不同的问题。`[本项目分析]`

**2. 写清研究问题。** 这是规划阶段最重要的一步[^kc-e6]，后面的检索词、筛选标准、要提取的数据，都从研究问题推出来。

**3. 写研究方案（protocol）。** 在开始检索之前，把下面这些写下来[^kc-e7]：

- 背景：为什么要做这个综述
- 研究问题
- 检索策略：用哪些检索词，查哪些数据库、期刊和会议
- 纳入和排除标准，以及筛选流程（几个人筛、分歧怎么解决）
- 质量评估标准
- 要提取哪些数据，怎么综合
- 时间安排

> **为什么一定要先写方案？** 没有方案，你很可能不自觉地按自己的预期去挑论文、做分析[^kc-e7]。先写方案，等于提前约束自己。

**4. 试用并评审方案。** 筛选标准先在一小批论文上试一试[^kc-e8]。方案是系统综述的关键[^kc-e9]，所以最好请导师或同行看一遍。`[本项目分析]`

### 第二阶段：执行

**1. 检索：组合几种方式，不要只靠一个数据库。**

只用一种检索方式，容易漏掉论文，还会带来发表偏差：正面结果比负面结果更容易发表[^kc-e10]。可以从下面选几种组合使用，不需要全部用上[^sig-e8]：

- 在数据库里用关键词检索，同时手工翻阅重要的期刊和会议
- 滚雪球（见下文）
- 查看领域内高产作者的论文列表
- 正式数据库（如 ACM Digital Library）加上 Google Scholar
- 学位论文、预印本（如 arXiv）
- 联系领域内的作者

检索要做到多严格，取决于综述的目标：元分析要求尽量找全，宽泛主题的映射研究可以松一些[^sig-e9]。一个参考：有研究重做了一篇系统综述，把数据库检索和滚雪球结合起来，比原综述只用数据库检索多找到了 30% 的相关研究[^w22-e1]。

**滚雪球检索怎么做：**

- **向后滚雪球**：查一篇论文的参考文献；**向前滚雪球**：查有哪些论文引用了它[^w14-e1]。
- **起始论文集要多样**：覆盖不同的研究社区、出版社、年份和作者；从研究问题的关键词出发，并考虑同义词。否则可能只找到一群互相引用的论文，漏掉与它们没有引用关系的另一群[^w14-e3]。起始集可以用 Google Scholar 找，避免偏向某一家出版社[^w14-e2]。
- **判断参考文献要不要读**：先按语言、年份、发表类型等基本条件排除，再去掉已经看过的；剩下的，看它在原文中被引用的位置和上下文，再决定要不要读[^w14-e5]。
- **确定纳入后，才能拿去做下一轮**：一篇论文要读完全文、确定纳入，才能用它继续滚雪球。否则它后来被排除时，从它找到的论文都要退回重来[^w14-e4]。
- **何时停止**：向后、向前都找不到新论文时停止[^w14-e6]。

**2. 筛选：先宽后严。**

- 第一轮只看标题和摘要，标准要放宽：只要不能明确排除，就去找全文[^kc-e11]。
- 软件工程论文的摘要常常写得不好，不能只凭摘要下结论，还要看看结论部分[^kc-e11]。
- 多人筛选时，用 Cohen's Kappa（一种衡量两人判断有多一致的统计量）衡量一致性。一个人做时，可以隔一段时间再重新判断一批随机抽取的论文，看前后是否一致[^kc-e12]。

**3. 评估每篇研究的质量。**

除了纳入/排除标准，还要评估每篇研究做得好不好[^kc-e13]。用事先定好的标准来评，例如在软件工程里，用 SIGSOFT 为对应研究方法制定的实证研究标准。低质量的研究可以排除，更好的做法是把质量纳入分析，看它是否影响结论[^sig-e10]。

注意两点：

- **论文没写，不等于没做。** 拿不准时联系原作者[^kc-e14]。
- **不要用发表会议或期刊的档次代替质量评估**[^sig-e16]。

**4. 提取数据。**

提前设计好提取表，表里的每一项都要对应某个研究问题[^sig-e5]。条件允许时，两人独立提取再核对；一个人做时（例如博士生），可以请导师对随机抽取的一部分论文也提取一遍，交叉核对[^kc-e15]。

**5. 综合。**

综合就是把纳入研究的结果汇总起来，回答研究问题。最基本的是描述性综合：把提取的信息按研究问题整理成表；条件允许时，再用统计方法做定量综合，也就是元分析[^kc-e16]。

最常见的错误是**逐篇罗列**："A 发现了 X，B 发现了 Y……"。这不是综合[^sig-e16]。好的综合要从数据到结论有一条清楚的证据链[^sig-e6]，还要清楚区分哪些是有证据的结果，哪些是你的解读和推测[^sig-e13]。做元分析时，不要用"计票法"，也就是只数支持和反对的研究各有几篇[^sig-e12]。

### 第三阶段：报告

推荐按 PRISMA 2020 写报告。PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）是源自医学、已被软件工程等领域广泛采用的系统综述报告规范，2020 版是一份 27 项的清单[^pr-e1]，规范的是"怎么报告"而不是"怎么做"；但最好在规划时就看一遍，确保该记录的东西都记下来[^pr-e2]。几个容易漏掉的地方：

- 给出所有数据库的**完整检索式**，包括过滤条件[^pr-e3]；
- 用**流程图**报告每一步各剩多少篇、排除了多少篇[^pr-e4]；
- 说明每篇文献**由几个人筛选、是否独立**，以及是否用了自动化工具[^pr-e5]；
- 公开研究方案、检索结果、筛选记录、提取的数据和分析脚本[^sig-e7]。

---

## 3. 映射研究怎么做

映射研究的检索和筛选与系统综述类似，主要区别是**一般不评估单篇论文的质量**，因此能覆盖更多论文、梳理更大的领域[^pe-e4]。它分五步[^pe-e1]：

1. 确定研究问题，例如"这个领域研究了哪些子方向，各有多少论文"
2. 检索
3. 筛选
4. 给摘要标注关键词，建立分类方案
5. 按分类方案提取数据，画出映射图，例如用气泡图展示各类别交叉处的论文数量[^pe-e8]

**分类方案怎么建**[^pe-e2]：先读每篇论文的摘要，找出反映它贡献的关键词；再把所有论文的关键词合并、聚类，形成类别。摘要信息不够时，看引言或结论。

**注意**：如果只收用某种研究方法的论文，比如只收做了实验的，再拿来描述整个领域，会有偏差[^pe-e5]。

---

## 4. 综述论文怎么写

综述论文不要求像系统综述那样找全，也不要求评估每篇论文的质量。但这不代表"读一堆论文、逐篇介绍一遍"就够了。

**好的综述论文要做到三件事**[^csur-e1]：

1. **对已有文献分类**：提出一个清楚的分类框架（taxonomy），让读者一眼看懂这个领域由哪几块组成。
2. **形成对领域的视角**：不只是介绍每篇论文做了什么，还要说明它们之间是什么关系、各自解决了什么、留下了什么问题。
3. **评估趋势**：这个领域正在往哪里走，哪些方向值得做。

**综述论文不是教程。** 教程面向外行，讲基本概念、举具体例子；综述假定读者已有基本了解，重点在分类和视角[^csur-e2]。写之前先想清楚读者是谁。

**它的局限要心里有数。** 综述论文的论文是作者挑的，有抽样偏差，也无法复现，容易只挑支持自己观点的证据[^rb-e2]。所以：

- Ralph & Baltes 认为，这类综述适合用来发展理论、寻找有前景的选题、为资格考试做准备[^rb-e2]；给领域画全景、提出理解框架，也属于这类用途 `[本项目分析]`；
- 它**不适合**用来支撑"X 比 Y 更好"这类实证结论。要下这类结论，就需要系统综述[^rb-e2]。

**实用建议** `[本项目分析]`：

- **说明论文是怎么找来的。** 即使不做系统检索，也写清楚你从哪里找、按什么标准选、覆盖到哪一年。这能大大降低"只挑自己喜欢的论文"的嫌疑，而且几乎不增加工作量。这是借用系统综述对"可复现"的要求[^kc-e1][^sig-e4]。
- **用分类框架组织正文，而不是按论文逐篇介绍。** 逐篇罗列是系统综述的反面模式[^sig-e16]，对综述论文同样成立。
- **每一类末尾写小结**：这一类方法的共同思路、各自的优缺点、还没解决的问题。

---

## 5. 检查清单

下面主要依据 ACM SIGSOFT 制定的系统综述标准，它是为软件工程写的。映射研究和综述论文可以按需选用；其他学科以本学科的规范为准。

**必须做到**

- [ ] 说明自己做的是哪一类综述[^sig-e3]
- [ ] 一步步、可复现地描述检索过程，包括检索词[^sig-e4]
- [ ] 给出明确的纳入和排除标准[^sig-e4]
- [ ] 说明从每篇论文提取哪些数据、和研究问题的关系，以及怎样提取、怎样综合[^sig-e5]
- [ ] 从数据到结论有清楚的证据链[^sig-e6]
- [ ] 给出面向实践者或非专业读者的结论或建议[^sig-e6]
- [ ] 披露主要局限，结论不超出证据[^sig-e18]

**做到更好**

- [ ] 组合多种检索方式，减少遗漏和发表偏差[^sig-e8]
- [ ] 用事先定好的标准评估每篇研究的质量[^sig-e10]
- [ ] 两人以上独立筛选和提取，报告一致性和分歧的解决方式（以实证主义取向为主的综述）[^sig-e11]
- [ ] 附 PRISMA 流程图[^sig-e12]
- [ ] 公开研究方案、检索结果、筛选记录、数据和脚本[^sig-e7]
- [ ] 把结果放回已有研究中，指出空白和未来方向；区分证据和推测[^sig-e13]

**做得出色**

- [ ] 确定检索词前，两人以上独立做预检索[^sig-e14]
- [ ] 联系原作者确认解读，或获取论文里没有的数据[^sig-e14]

**这些情况可以不做，不算缺陷**[^sig-e15]

- 专门研究某个会议或期刊时，可以不处理发表偏差
- 论文多到数千篇时，可以随机抽样

**审稿时常见、但不成立的批评**[^sig-e17]：你不必为此担心

- "各个数据库的检索式不完全一样"
- "分析应该更定性一些"或"更定量一些"

---

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不写研究方案就开始检索 | 容易按自己的预期挑论文[^kc-e7] |
| 只用一个数据库 | 漏掉论文，加重发表偏差[^kc-e10][^sig-e8] |
| 滚雪球的起始论文都来自同一个圈子 | 只找到一群互相引用的论文[^w14-e3] |
| 只凭标题和摘要就轻易排除 | 漏掉相关论文；摘要常常信息不足，拿不准时要看全文[^kc-e11] |
| 用会议或期刊的档次代替质量评估 | 档次不等于单篇研究的质量[^sig-e16] |
| 逐篇罗列"A 发现 X，B 发现 Y" | 没有综合，读者得不到结论[^sig-e16] |
| 在高质量研究很少的领域硬做系统综述 | 得不出可靠结论，不如先做映射研究[^sig-e16][^kc-e3] |
| 用综述论文支撑"X 比 Y 好" | 挑选的论文有偏差，撑不起实证结论[^rb-e2] |
| 映射研究只有分类和计数 | 价值有限，最好往综合方向多走一步[^rb-e5] |

---

## 7. 延伸阅读

- **系统综述的完整指南**：Kitchenham & Charters 2007，包括质量评估清单和大量例子。
- **映射研究**：Petersen 等人 2008；更新版 Petersen 等人 2015 还没有读到全文，待补充 `[待确认]`。
- **综述类型的全貌**：Ralph & Baltes 2022 梳理了多种文献综述，除本文提到的几种外，还讨论了元分析、元综合、案例调查、快速综述等[^rb-e5]。
- **报告规范**：PRISMA 2020 的完整清单和流程图模板。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^csur-e1]: ACM Computing Surveys 作者指南，Long Survey Paper。[证据](../../sources/notes/acm2026csurguidelines.md#e1)
[^csur-e2]: ACM Computing Surveys 作者指南，Tutorial Paper。[证据](../../sources/notes/acm2026csurguidelines.md#e2)
[^kc-e1]: Kitchenham & Charters 2007，§1。[证据](../../sources/notes/kitchenham2007guidelines.md#e1)
[^kc-e2]: Kitchenham & Charters 2007，§2。[证据](../../sources/notes/kitchenham2007guidelines.md#e2)
[^kc-e3]: Kitchenham & Charters 2007，§2.5.1。[证据](../../sources/notes/kitchenham2007guidelines.md#e3)
[^kc-e4]: Kitchenham & Charters 2007，§4。[证据](../../sources/notes/kitchenham2007guidelines.md#e4)
[^kc-e5]: Kitchenham & Charters 2007，§5.1。[证据](../../sources/notes/kitchenham2007guidelines.md#e5)
[^kc-e6]: Kitchenham & Charters 2007，§5.3.1。[证据](../../sources/notes/kitchenham2007guidelines.md#e6)
[^kc-e7]: Kitchenham & Charters 2007，§5.4。[证据](../../sources/notes/kitchenham2007guidelines.md#e7)
[^kc-e8]: Kitchenham & Charters 2007，§5.4。[证据](../../sources/notes/kitchenham2007guidelines.md#e8)
[^kc-e9]: Kitchenham & Charters 2007，§5.5。[证据](../../sources/notes/kitchenham2007guidelines.md#e9)
[^kc-e10]: Kitchenham & Charters 2007，§6.1.2。[证据](../../sources/notes/kitchenham2007guidelines.md#e10)
[^kc-e11]: Kitchenham & Charters 2007，§6.2.2。[证据](../../sources/notes/kitchenham2007guidelines.md#e11)
[^kc-e12]: Kitchenham & Charters 2007，§6.2.3。[证据](../../sources/notes/kitchenham2007guidelines.md#e12)
[^kc-e13]: Kitchenham & Charters 2007，§6.3。[证据](../../sources/notes/kitchenham2007guidelines.md#e13)
[^kc-e14]: Kitchenham & Charters 2007，§6.3.4。[证据](../../sources/notes/kitchenham2007guidelines.md#e14)
[^kc-e15]: Kitchenham & Charters 2007，§6.4.3。[证据](../../sources/notes/kitchenham2007guidelines.md#e15)
[^kc-e16]: Kitchenham & Charters 2007，§6.5。[证据](../../sources/notes/kitchenham2007guidelines.md#e16)
[^pe-e1]: Petersen 等人 2008，§2。[证据](../../sources/notes/petersen2008systematic.md#e1)
[^pe-e2]: Petersen 等人 2008，§2.4。[证据](../../sources/notes/petersen2008systematic.md#e2)
[^pe-e3]: Petersen 等人 2008，§3.2。[证据](../../sources/notes/petersen2008systematic.md#e3)
[^pe-e4]: Petersen 等人 2008，§3.2。[证据](../../sources/notes/petersen2008systematic.md#e4)
[^pe-e5]: Petersen 等人 2008，§3.2。[证据](../../sources/notes/petersen2008systematic.md#e5)
[^pe-e6]: Petersen 等人 2008，§4。[证据](../../sources/notes/petersen2008systematic.md#e6)
[^pe-e7]: Petersen 等人 2008，摘要与 §1。[证据](../../sources/notes/petersen2008systematic.md#e7)
[^pe-e8]: Petersen 等人 2008，§2.5。[证据](../../sources/notes/petersen2008systematic.md#e8)
[^rb-e1]: Ralph & Baltes 2022，§2.1。[证据](../../sources/notes/ralph2022paving.md#e1)
[^rb-e2]: Ralph & Baltes 2022，§2.1。[证据](../../sources/notes/ralph2022paving.md#e2)
[^rb-e3]: Ralph & Baltes 2022，§2.2.5。[证据](../../sources/notes/ralph2022paving.md#e3)
[^rb-e4]: Ralph & Baltes 2022，§2.2.5。[证据](../../sources/notes/ralph2022paving.md#e4)
[^rb-e5]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e5)
[^w14-e1]: Wohlin 2014，§1。[证据](../../sources/notes/wohlin2014guidelines.md#e1)
[^w14-e2]: Wohlin 2014，§3.1。[证据](../../sources/notes/wohlin2014guidelines.md#e2)
[^w14-e3]: Wohlin 2014，§3.1。[证据](../../sources/notes/wohlin2014guidelines.md#e3)
[^w14-e4]: Wohlin 2014，§3.2。[证据](../../sources/notes/wohlin2014guidelines.md#e4)
[^w14-e5]: Wohlin 2014，§3.2.1。[证据](../../sources/notes/wohlin2014guidelines.md#e5)
[^w14-e6]: Wohlin 2014，§3.3。[证据](../../sources/notes/wohlin2014guidelines.md#e6)
[^w22-e1]: Wohlin 等人 2022，摘要。[证据](../../sources/notes/wohlin2022successful.md#e1)
[^pr-e1]: PRISMA 2020（Page 等人 2021）。[证据](../../sources/notes/page2021prisma.md#e1)
[^pr-e2]: PRISMA 2020（Page 等人 2021）。[证据](../../sources/notes/page2021prisma.md#e2)
[^pr-e3]: PRISMA 2020，第 7 项。[证据](../../sources/notes/page2021prisma.md#e3)
[^pr-e4]: PRISMA 2020，第 16a 项。[证据](../../sources/notes/page2021prisma.md#e4)
[^pr-e5]: PRISMA 2020，与 2009 版相比的变化。[证据](../../sources/notes/page2021prisma.md#e5)
[^sig-e3]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e3)
[^sig-e4]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e4)
[^sig-e5]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e5)
[^sig-e6]: SIGSOFT 系统综述标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e6)
[^sig-e7]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e7)
[^sig-e8]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e8)
[^sig-e9]: SIGSOFT 系统综述标准，加分项及脚注 3。[证据](../../sources/notes/ralph2020empirical.md#e9)
[^sig-e10]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e10)
[^sig-e11]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e11)
[^sig-e12]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e12)
[^sig-e13]: SIGSOFT 系统综述标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e13)
[^sig-e14]: SIGSOFT 系统综述标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e14)
[^sig-e15]: SIGSOFT 系统综述标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e15)
[^sig-e16]: SIGSOFT 系统综述标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e16)
[^sig-e17]: SIGSOFT 系统综述标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e17)
[^sig-e18]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e18)
