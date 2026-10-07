# 方法论研究与元科学：研究"怎么做研究"

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲**以研究方法本身为对象的研究**：分析某个研究方法问题，或就怎样做研究给出建议。例如一份统计检验指南、一篇调查"某个领域的论文评测做得怎么样"的论文、一篇批评某种研究风气的文章。

如果你想知道的是自己的实验怎样做得严谨，那是每项研究都要做的事，见[效度与局限：设计阶段就想清楚](../02_from-project-to-study/03_validity-and-limits.md)；如果你要综述的是某个技术主题的研究，见[综述研究](review_study.md)。

**适用范围** `[本项目分析]`：本文的规范和例子都来自计算机：检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）为软件工程写的实证研究标准，例子来自软件工程、系统安全、模糊测试和机器学习。其他学科也有方法论研究（见第 1 节末尾），做之前先看本学科的同类论文和期刊要求。

**常服务的套路**：[综合](../05_research-strategies/synthesize.md)（批判性综述）、[测量](../05_research-strategies/measure.md)（系统调查一个领域的测量做得怎么样）。

**读完本文，你应该能：**

- 认出几种常见的方法论研究，知道它们各需要什么样的证据；
- 为自己的方法论论文选对证据：系统抽样的论文、亲手做的演示实验，或论证；
- 批评同行的研究时做到公正，不伤人；
- 用文末的检查清单检查自己的论文。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为：分析某个研究方法问题，或就如何开展研究提出建议的论文[^ralph2020empirical-e306]。它可以有、也可以没有实证数据；可以讨论哲学问题，也可以讨论实际问题；如果它同时是一项实证研究（例如一项案例研究，再据此提出方法建议），还要满足那类研究的标准[^ralph2020empirical-e307]。

这类研究属于**元科学**（meta-science）：一个科学群体内部关于"我们怎样做研究"的讨论[^ralph2022paving-e14]。

**常见的几种** `[本项目分析，依据下列资料]`：

| 类型 | 做什么 | 例子 |
|---|---|---|
| 方法指南 | 系统地说明某种研究方法该怎么做 | SIGSOFT 标准列出的范例包括 Kitchenham & Charters 的系统综述指南、Runeson & Höst 的案例研究指南[^ralph2020empirical-e315] |
| 批判性综述（critical review） | 分析一批论文，支撑一个论点或一项批评，常常针对方法问题[^ralph2022paving-e12]；不止于描述，要提出具体批评[^ralph2022paving-e16] | Stol 等人批评软件工程中的"方法冒用"：声称用了某种方法，实际上没用[^ralph2022paving-e13] |
| 研究实践调查 | 系统检查一批已发表论文的做法，统计问题有多普遍，常配合演示实验 | van der Kouwe 等人调查了 50 篇系统安全论文的基准评测[^vanderkouwe2019sok-e26]；Klees 等人调查了 32 篇模糊测试论文的评估[^klees2018evaluating-e2] |
| 立场与讨论文章 | 指出一种研究风气，引发讨论 | Lipton & Steinhardt 为一个辩论性质的研讨会撰文，批评机器学习论文写作中的几种趋势[^lipton2019troubling-e16]；Ralph & Baltes 也说明自己那篇综述分类文章是元科学而非实证论文[^ralph2022paving-e21] |

**和综述研究的区别**：映射研究（与范围综述相近，见[综述研究](review_study.md)）关注的是实证主题（例如"软件工程中的认知偏差"），而元科学关注的是方法主题（例如"构念效度"，即你测的东西是否真的代表你想研究的概念）[^ralph2022paving-e17]，所以映射研究从一开始就不是为方法批评设计的。批判性综述也不是为了总结某个理论的证据，而是为了评判做法[^ralph2022paving-e14]。

**什么时候值得写**：当你在读论文或审稿时反复看到同一个方法问题，而且能说清它为什么重要、该怎么改。在计算机领域，这类论文在各方向都有：软件工程（研究方法指南）、系统和安全（评测缺陷调查）、机器学习（评测和写作风气批评）。其他学科也有，例如心理学中讨论统计检验误用、研究可重复性的文章 `[本项目分析]`。

---

## 2. 怎么做

### 第一步：选一个对别人有用的问题，并且要给出明确建议

SIGSOFT 标准对这类论文只有三条必要项：提供对其他研究者有用的信息；对今后的研究提出建议；用清楚、成立的论证支撑建议[^ralph2020empirical-e308]。

**容易错在哪**：讨论了一个问题，却没有明确结论，也没给出可操作的指南[^ralph2020empirical-e311]。读者读完只知道"这里有问题"，不知道该怎么办。

**给建议时说清它有多确定。** Lipton & Steinhardt 举的正面例子是一篇训练指南：它没有把建议说成权威结论，而是说明建议应当接受质疑，只是一个好的起点[^lipton2019troubling-e20]。

**做得更好**：做出可以直接用的东西，例如检查清单、模板、测试、工具或一套评判标准[^ralph2020empirical-e309]。Klees 等人的结论就给出了具体建议，例如多次运行并用统计检验比较、运行至少 24 小时或说明更短的理由[^klees2018evaluating-e24]。

### 第二步：选对证据

方法论文的证据主要有三种来源，可以组合使用 `[本项目分析]`。

**1. 系统抽样的一批论文：说明问题有多普遍。**

- 写清怎么选的论文。van der Kouwe 等人选的是四个顶级安全会议在 2010 年和 2015 年发表的、带基准评测结果的**全部**防御论文，并说明选这四个会议是因为它们事实上决定了领域的评测惯例[^vanderkouwe2019sok-e27]。
- 不必找全所有论文。对很多批判性综述来说，纳入全部相关研究既不可能也没必要；因为它不评估因果主张，从若干顶级期刊和会议随机抽样就够了[^ralph2022paving-e15]。审稿人也不应套用"必须找全""必须排除低质量研究"这类系统综述的标准[^ralph2022paving-e20]。
- 没有系统抽样，只靠几个例子，能说明问题存在，但说明不了它在文献中有多普遍[^vanderkouwe2019sok-e33]。

**2. 亲手做的演示实验：说明问题的后果。**

只说"很多论文没做 X"，读者可能觉得无所谓 `[本项目分析]`。Klees 等人做了超过 5 万 CPU 小时的实验，证明偏离推荐做法的实验很容易得出错误结论[^klees2018evaluating-e20]。选哪个对象做演示要有理由：他们选的工具是新近的改进、代码公开、能重跑原实验并改变原作者没改变的参数[^klees2018evaluating-e21]。而且目的不是复现那篇论文，而是拿它当例子检验评估做法[^klees2018evaluating-e22]。SIGSOFT 标准把用定量模拟展示方法问题列为优秀项[^ralph2020empirical-e310]。

**3. 论证：很多方法主张本来就无法用实证检验。**

SIGSOFT 标准认为，"指南没有实证依据"是不成立的批评：元科学主张通常无法用实证检验，审稿人应评价指南表面上是否合理、是否全面、是否有用[^ralph2020empirical-e313]。但这不等于可以随便写：审稿人要更较真地审查论证[^ralph2020empirical-e314]，要避免稻草人（歪曲对方观点再批驳）、诉诸流行等逻辑谬误[^ralph2020empirical-e311]。

> **不同的看法：方法论文一定要有实证研究吗？**
> - SIGSOFT 标准认为不需要，把"包含一项实证研究来引出建议"列为优秀项而不是必要项[^ralph2020empirical-e310][^ralph2020empirical-e313]。Ralph & Baltes 认为，坚持每篇论文都要报告实证研究的审稿风气，束缚了元科学研究[^ralph2022paving-e18]。
> - van der Kouwe 等人则指出，只用例子和自己的测试说明问题的文章，无法判断问题对文献的影响有多大[^vanderkouwe2019sok-e33]。
>
> 实际操作中可以这样理解：如果你的主张是"这个问题很普遍"，就需要系统抽样的数据；如果你的主张是"应该这样做"，论证和演示可以是主要证据 `[本项目分析]`。

### 第三步：给论文"挑错"时，像做研究一样严谨

调查一批论文的做法，本质上是在给论文编码，要求和其他编码研究一样 `[本项目分析]`（一致性检验的做法见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md#第六步人工标注并检验一致性)）：

- **两人独立判断，再讨论分歧。** van der Kouwe 等人由两人独立判断每篇论文的每种缺陷，有分歧的 8 篇（16%）讨论后定稿[^vanderkouwe2019sok-e28]。
- **给"说不清"留一个类别。** 他们的类别是"正确、有缺陷、描述不足、不适用"[^vanderkouwe2019sok-e28]。论文没写清楚，不能直接算成"做错了"。
- **说明信息来源的限制。** 他们只依据论文本身、不联系作者，等于给自己加上和审稿人一样的限制[^vanderkouwe2019sok-e29]。
- **说明样本的局限。** 已发表的论文不一定能代表所有投稿[^vanderkouwe2019sok-e32]。
- **原因只能推测时，就说是推测。** 对缺陷产生的原因，他们明确写"只能推测"[^vanderkouwe2019sok-e34]。

### 第四步：批评要公正，对事不对人

方法论文几乎都要指出别人的问题，这一步最需要用心。

- **不攻击具体的研究或研究者。** SIGSOFT 标准建议用假设的例子，避免引起敌意[^ralph2020empirical-e312]。Ralph & Baltes 认为，阐明一个普遍问题时，没必要点名犯错的具体论文：由此增加的可信度，抵不上对学术群体和未来合作的损害；作者应说明这样做的理由[^ralph2022paving-e19]。
- **不指控动机。** van der Kouwe 等人特意用"缺陷"而不用"罪行"这个说法，并说明他们认为这些缺陷大多不是故意的[^vanderkouwe2019sok-e30]。他们的数据也显示，问题不在少数作者，而在整个领域缺乏重视[^vanderkouwe2019sok-e35]。
- **把自己算进去。** Lipton & Steinhardt 说明批评也针对自己，并举了自己论文中的反面例子[^lipton2019troubling-e17][^lipton2019troubling-e12]。
- **需要真实例子时，保护最弱势的人。** 他们优先选知名研究者和机构的工作，避免点名年轻学生，因为学生被点名可能受影响，也没有对等的回应机会[^lipton2019troubling-e18]。例子要简短、具体，也要给出做得好的正面例子[^lipton2019troubling-e19]。
- **认真对待反方理由。** Lipton & Steinhardt 专门用一节讨论反对自己建议的理由，承认它们成立，并把建议定位为经验法则而不是铁律[^lipton2019troubling-e21]。

> **不同的看法：要不要公开点名？**
> - **匿名**：van der Kouwe 等人不公开哪篇论文有哪些缺陷，认为点名羞辱适得其反；作为补偿，在附录详细写出判定标准，让别人能按同样标准重做调查[^vanderkouwe2019sok-e31]。
> - **公开**：Klees 等人用表格汇总了每篇被调查论文的评估做法[^klees2018evaluating-e23]（表中逐篇列出了论文 `[本项目分析]`），读者可以直接核对。
>
> 实际操作中：公开有利于核对和复现，匿名有利于减少对个人的伤害。指出的是普遍问题时，可以优先匿名，同时公开判定标准 `[本项目分析]`；无论哪种，都只评论论文的做法，不评论作者。

---

## 3. 检查清单

下面依据 ACM SIGSOFT 的方法论与元科学标准，它是为软件工程写的。

**必须做到**[^ralph2020empirical-e308]

- [ ] 提供对其他研究者有用的信息
- [ ] 对今后的研究提出明确建议
- [ ] 用清楚、成立的论证支撑建议

**做到更好**[^ralph2020empirical-e309]

- [ ] 综合相关学科已有的方法讨论
- [ ] 不只转述已有指南，给出所在领域特有的见解
- [ ] 把结论放回已有理论和研究中
- [ ] 做出可直接使用的工具，如检查清单、模板、评判标准

**做得出色**[^ralph2020empirical-e310]

- [ ] 包含一项实证研究（如系统综述）来引出建议
- [ ] 用定量模拟展示方法问题

**审稿时常见、但不成立的批评**[^ralph2020empirical-e313]

- "指南没有实证依据"

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 指出了问题，却不给明确建议 | 读者不知道该怎么做[^ralph2020empirical-e311] |
| 结论超出论证，或者歪曲对方观点再批驳 | 属于过度推论和逻辑谬误[^ralph2020empirical-e311] |
| 点名攻击具体论文或研究者 | 引起敌意，损害学术群体[^ralph2020empirical-e312][^ralph2022paving-e19] |
| 暗示别人故意作弊 | van der Kouwe 等人认为多数缺陷不是故意的，只是重视不够[^vanderkouwe2019sok-e30] |
| 只举几个例子就说"问题很普遍" | 没有系统抽样，判断不了普遍程度[^vanderkouwe2019sok-e33] |
| 把"论文没写"直接算成"做错了" | 应单列"描述不足"[^vanderkouwe2019sok-e28] |
| 把对原因的推测写成结论 | 应明确标为推测[^vanderkouwe2019sok-e34] |
| 只转述已有的方法指南 | 标准期望给出超出已有指南的、所在领域特有的见解[^ralph2020empirical-e309] |

---

## 5. 延伸阅读

- **怎样写一篇研究实践调查**：van der Kouwe 等人 2019（系统安全）和 Klees 等人 2018（模糊测试）。前者示范了系统抽样、两人编码和匿名处理，后者示范了用演示实验说明后果。两篇的评测建议本身见[基准评测](../07_fields/computer-science/practices/benchmarking.md)。
- **怎样批评同行**：Lipton & Steinhardt 2019 的第 2 节（免责说明）和第 6.1 节（反方考虑）。
- **批判性综述的定位**：Ralph & Baltes 2022 §2.2.4 和 §3.1。
- **检查清单的来源**：ACM SIGSOFT 方法论与元科学标准，附有多篇方法指南范例。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e306]: SIGSOFT 方法论与元科学标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e306)
[^ralph2020empirical-e307]: SIGSOFT 方法论与元科学标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e307)
[^ralph2020empirical-e308]: SIGSOFT 方法论与元科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e308)
[^ralph2020empirical-e309]: SIGSOFT 方法论与元科学标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e309)
[^ralph2020empirical-e310]: SIGSOFT 方法论与元科学标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e310)
[^ralph2020empirical-e311]: SIGSOFT 方法论与元科学标准，反面模式及脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e311)
[^ralph2020empirical-e312]: SIGSOFT 方法论与元科学标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e312)
[^ralph2020empirical-e313]: SIGSOFT 方法论与元科学标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e313)
[^ralph2020empirical-e314]: SIGSOFT 方法论与元科学标准，Notes。[证据](../../sources/notes/ralph2020empirical.md#e314)
[^ralph2020empirical-e315]: SIGSOFT 方法论与元科学标准，Exemplars。[证据](../../sources/notes/ralph2020empirical.md#e315)
[^ralph2022paving-e12]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e12)
[^ralph2022paving-e13]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e13)
[^ralph2022paving-e14]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e14)
[^ralph2022paving-e15]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e15)
[^ralph2022paving-e16]: Ralph & Baltes 2022，§2.2.4。[证据](../../sources/notes/ralph2022paving.md#e16)
[^ralph2022paving-e17]: Ralph & Baltes 2022，§3。[证据](../../sources/notes/ralph2022paving.md#e17)
[^ralph2022paving-e18]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e18)
[^ralph2022paving-e19]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e19)
[^ralph2022paving-e20]: Ralph & Baltes 2022，§3.1。[证据](../../sources/notes/ralph2022paving.md#e20)
[^ralph2022paving-e21]: Ralph & Baltes 2022，§3.2。[证据](../../sources/notes/ralph2022paving.md#e21)
[^lipton2019troubling-e16]: Lipton & Steinhardt 2019，§2。[证据](../../sources/notes/lipton2019troubling.md#e16)
[^lipton2019troubling-e17]: Lipton & Steinhardt 2019，§2。[证据](../../sources/notes/lipton2019troubling.md#e17)
[^lipton2019troubling-e18]: Lipton & Steinhardt 2019，§2。[证据](../../sources/notes/lipton2019troubling.md#e18)
[^lipton2019troubling-e19]: Lipton & Steinhardt 2019，§3。[证据](../../sources/notes/lipton2019troubling.md#e19)
[^lipton2019troubling-e12]: Lipton & Steinhardt 2019，§3.1。[证据](../../sources/notes/lipton2019troubling.md#e12)
[^lipton2019troubling-e20]: Lipton & Steinhardt 2019，§3.1。[证据](../../sources/notes/lipton2019troubling.md#e20)
[^lipton2019troubling-e21]: Lipton & Steinhardt 2019，§6.1。[证据](../../sources/notes/lipton2019troubling.md#e21)
[^vanderkouwe2019sok-e26]: van der Kouwe 等人 2019，摘要。[证据](../../sources/notes/vanderkouwe2019sok.md#e26)
[^vanderkouwe2019sok-e27]: van der Kouwe 等人 2019，§I、§III-B。[证据](../../sources/notes/vanderkouwe2019sok.md#e27)
[^vanderkouwe2019sok-e28]: van der Kouwe 等人 2019，§III-A。[证据](../../sources/notes/vanderkouwe2019sok.md#e28)
[^vanderkouwe2019sok-e29]: van der Kouwe 等人 2019，§III-A。[证据](../../sources/notes/vanderkouwe2019sok.md#e29)
[^vanderkouwe2019sok-e30]: van der Kouwe 等人 2019，§I。[证据](../../sources/notes/vanderkouwe2019sok.md#e30)
[^vanderkouwe2019sok-e31]: van der Kouwe 等人 2019，§VII 与附录 A。[证据](../../sources/notes/vanderkouwe2019sok.md#e31)
[^vanderkouwe2019sok-e32]: van der Kouwe 等人 2019，§VII。[证据](../../sources/notes/vanderkouwe2019sok.md#e32)
[^vanderkouwe2019sok-e33]: van der Kouwe 等人 2019，§IX。[证据](../../sources/notes/vanderkouwe2019sok.md#e33)
[^vanderkouwe2019sok-e34]: van der Kouwe 等人 2019，§I。[证据](../../sources/notes/vanderkouwe2019sok.md#e34)
[^vanderkouwe2019sok-e35]: van der Kouwe 等人 2019，§V。[证据](../../sources/notes/vanderkouwe2019sok.md#e35)
[^klees2018evaluating-e2]: Klees 等人 2018，摘要。[证据](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e20]: Klees 等人 2018，§1。[证据](../../sources/notes/klees2018evaluating.md#e20)
[^klees2018evaluating-e21]: Klees 等人 2018，§1。[证据](../../sources/notes/klees2018evaluating.md#e21)
[^klees2018evaluating-e22]: Klees 等人 2018，§3。[证据](../../sources/notes/klees2018evaluating.md#e22)
[^klees2018evaluating-e23]: Klees 等人 2018，Table 1 与 §4。[证据](../../sources/notes/klees2018evaluating.md#e23)
[^klees2018evaluating-e24]: Klees 等人 2018，§9。[证据](../../sources/notes/klees2018evaluating.md#e24)
