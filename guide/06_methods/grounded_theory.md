# 扎根理论：从数据中逐步归纳出理论

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**扎根理论**（grounded theory）研究：不先提出假设，而是一边收集数据、一边分析，根据分析结果决定下一步找谁、看什么，最后从数据中归纳出一个理论。

扎根理论的数据多来自访谈。访谈本身怎么设计、怎么做，以及定性研究共用的质量标准和验证做法，见[访谈研究](interview_study.md)；如果你只是想深入描述一个具体的组织或项目，见[案例研究](case_study.md)。本文只讲扎根理论特有的部分：流派、理论抽样、持续比较、备忘录、理论饱和和产出理论。

**读完本文，你应该能：**

- 判断自己的问题适不适合用扎根理论，以及选哪个流派；
- 按"收集—分析—再抽样"的循环推进研究，知道什么时候可以停；
- 分清"产出了理论"和"只整理出几个主题"；
- 避免最常见的问题：只借用了编码技巧，却声称"用了扎根理论"。

---

## 1. 这是什么研究，什么时候用

扎根理论是**从数据中归纳生成理论**的方法[^stol2016grounded-e2]。它的目标是生成理论，而不是检验已有理论；适合回答"这里到底发生了什么"这类问题[^stol2016grounded-e1]。这里的"理论"，指由概念和概念之间的关系构成、能解释某种现象的一套说法[^stol2016grounded-e17]。

**适合用的情况** `[本项目分析，依据下列资料]`：

- 你关心的是人和组织：开发者、团队、用户怎么做事、为什么这样做。软件工程越来越重视软件开发中社会、文化和人的因素，扎根理论被认为很适合研究这些方面[^stol2016grounded-e25]。资料都来自软件工程；在系统、安全、机器学习等方向，只要研究对象是人的实践（例如运维团队如何处理故障、机器学习工程师如何调试模型），道理相同。扎根理论本身起源于社会学，在护理学、管理学等领域也常用来研究人怎样应对某种处境。`[本项目分析]`
- 这个领域还没有现成的理论可用，你想先弄清"发生了什么"。
- 你能接受研究问题在过程中变化：SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把扎根理论界定为探索一个宽泛领域、**没有事先定好的具体研究问题**的研究[^ralph2020empirical-e316]。

**不适合的情况**：

- 已经有明确假设要检验，例如"引入结对编程能减少缺陷"。扎根理论不检验理论[^stol2016grounded-e1]，这时应做实验或其他验证性研究。
- 打算先把访谈全部做完再分析，或者不打算根据分析结果决定下一步找谁。SIGSOFT 标准建议这样的定性研究参考[案例研究](case_study.md)或[访谈研究](interview_study.md)的标准[^ralph2020empirical-e316]。扎根理论不是分析定性数据的唯一合法方法[^stol2016grounded-e22]，把访谈研究包装成扎根理论并不会让它更好。

### 先选一个流派，并始终一致

扎根理论至少有三个主要流派[^stol2016grounded-e3]，它们在三件事上分歧最大[^stol2016grounded-e4][^stol2016grounded-e5][^stol2016grounded-e6][^stol2016grounded-e8][^stol2016grounded-e9]：

| | 经典扎根理论（Glaser） | Strauss 版扎根理论（Strauss & Corbin） | 建构主义扎根理论（Charmaz） |
|---|---|---|---|
| 特点 | 强调一切从数据中"自然浮现" | 规定了一系列细小步骤 | 强调理解，承认解读取决于研究者视角 |
| 研究问题 | 只从一个"感兴趣的领域"出发；事先定问题被视为"强加" | 可以事先定一个宽泛、开放的问题 | 从"初始研究问题"开始，在研究中演变 |
| 文献 | 理论浮现之后再做全面综述 | 全程都可以查阅 | 承认推迟综述的理由，也承认它不现实；按研究目的裁剪 |
| 编码 | 开放编码、选择性编码、理论编码 | 开放编码、轴心编码、选择性编码 | 初始编码、聚焦编码、理论编码 |

注意：同一个术语在不同流派里意思不同。例如"选择性编码"，经典版指只保留与核心变量相关的编码，Strauss 版指确定一个所有主要类别都能连上的中心类别[^stol2016grounded-e9]。

**选定一个，并在设计、分析和写作中保持一致。** Stol 等人审查了 52 篇声称用扎根理论的软件工程期刊论文，39 篇根本没提到存在不同流派，还有论文声称用经典版却用了 Strauss 版的轴心编码[^stol2016grounded-e26]。SIGSOFT 标准把"写明用了哪个流派"列为必须做到的项[^ralph2020empirical-e317]；偏离或组合了流派的，要说明怎样偏离、为什么[^ralph2020empirical-e321]。

下文的步骤用**建构主义扎根理论**的术语。它允许带着初始研究问题开始，也允许按需要读文献[^stol2016grounded-e5][^stol2016grounded-e6]，对需要写开题报告的研究生更容易落地 `[本项目分析]`。选其他流派的，按上表换成对应的做法。

---

## 2. 怎么做

扎根理论不是一条直线，而是一个循环：**收集一点数据 → 马上分析 → 根据分析决定下一步收集什么**，直到理论饱和[^stol2016grounded-e10]。下面按这个循环里的几件事分开讲。

### 第 0 步：动手之前先读方法书

**怎么做**：在决定用扎根理论之前，先读几本该流派的专著[^stol2016grounded-e21]。

**为什么**：扎根理论看上去只是"读材料、贴标签"，其实复杂得多，而且各流派的指导互相冲突[^stol2016grounded-e21]。它必须从研究一开始就按它的方式设计，**不能到写论文时才"包装"成扎根理论**[^stol2016grounded-e20]。

### 第 1 步：从一个领域或初始问题出发，想清楚怎么对待文献

**怎么做**：

- 写下你感兴趣的领域和初始研究问题，例如"开源项目的维护者如何决定接受还是拒绝外部贡献"。`[本项目分析]`
- 按所选流派决定读多少文献、什么时候读[^stol2016grounded-e6]。无论哪个流派，都**不要从文献里拿一套现成的分类来给数据归类**。

**为什么**：限制阅读文献，是为了防止你不知不觉在检验已有理论，或用现成概念去想问题[^stol2016grounded-e7]。先从文献里定好初步类别、再"结合扎根理论方法"的做法非常可疑[^stol2016grounded-e27]；从"种子类别"或预设框架出发分析的，就不是扎根理论[^stol2016grounded-e19]。

文献调研的一般做法见通用篇[读文献与文献调研](../01_from-interest-to-project/01_enter-a-field.md)。

### 第 2 步：收集第一批数据，马上开始分析

**怎么做**：做最初几次访谈（或收集最初几份文档、观察记录），**拿到就分析**，不要等全部收集完[^stol2016grounded-e10]。

**数据可以是什么**：多为访谈转录、文档、现场笔记，也可以是结构化文本、图表，甚至定量数据[^stol2016grounded-e2]。在软件开发场景中，数据又多又杂（代码、提交记录、缺陷报告、聊天记录……）。一个办法是选定一个主要数据源，例如访谈，再按它提供的线索从其余数据中有选择地取材[^stol2016grounded-e23]。

**容易错在哪里**：先把所有访谈做完再统一分析。这是 SIGSOFT 标准列出的第一条反面模式："先收集、后分析，只用了扎根理论的分析技巧"[^ralph2020empirical-e325]。

### 第 3 步：编码

建构主义扎根理论有三种编码[^stol2016grounded-e8]。Stol 等人指出，把编码说成三个截然分开的阶段，并不是 Glaser 或 Strauss 的本意[^stol2016grounded-e28]；建构主义的三种编码同样会交替进行，后面的编码会随着新数据回头修改前面的结果 `[本项目分析]`：

1. **初始编码**：逐词、逐行或逐个事件地读数据，给每一小段贴上描述它在说什么的标签，尽量不掺入自己的假设[^stol2016grounded-e8]。
2. **聚焦编码**：从最常见或最重要的编码中挑出类别，用它们去归类更多数据[^stol2016grounded-e8]。
3. **理论编码**：说明类别之间的关系，把它们整合成一个连贯的理论[^stol2016grounded-e8]。

**容易错在哪里**：

- 把数据归入事先定好的编码方案[^stol2016grounded-e11]。
- 只数词频、数编码出现了多少次，而不做解读[^ralph2020empirical-e325]。

### 第 4 步：持续比较

**怎么做**：从研究一开始，就不断地把新数据和旧数据比、把编码和编码比、把类别和数据比、把备忘录和类别比[^stol2016grounded-e13]。例如：新受访者说的"拒绝贡献是因为维护成本"，和已有类别"担心代码质量"是同一回事，还是另一个类别？`[本项目分析]`

**为什么**：类别和对数据的解读都是在反复比较中逐渐成形的[^stol2016grounded-e13]。

### 第 5 步：写备忘录

**怎么做**：随时记下你对类别的想法：这个类别是什么意思、有哪些属性、和其他类别有什么关系、还缺什么数据。形式不限，笔记、图、草图都可以[^stol2016grounded-e12]。

**为什么**：备忘录是从编码走向理论的主要工具。Stol 等人引述的说法是：跳过这一步，就不是在做扎根理论[^stol2016grounded-e12]。论文中最好说明备忘录是怎样推动研究的[^ralph2020empirical-e319]。

### 第 6 步：理论抽样——根据分析决定下一步找谁

**怎么做**：理论抽样是**根据正在形成的理论、概念或类别，选择下一步收集什么数据**[^ralph2020empirical-e328]：哪里有空缺、哪个概念还不清楚，就去找能补上它的人或材料[^stol2016grounded-e10]。例如，分析中出现了"维护者的时间压力"这个类别，下一步就专门去找全职和业余维护者各几位来比较。`[本项目分析]`

**容易错在哪里**：

- 事先选好几家公司或几类人，然后称之为"理论抽样"。有论文就是这样做的，这并不是理论抽样[^stol2016grounded-e18]。
- 只访谈一群相似的人。样本小而同质，会造成"已经收敛、已经饱和"的假象；只访谈 20 个相似的人，很难得出完整的理论[^ralph2020empirical-e326]。数据最好覆盖多样的人或事物[^ralph2020empirical-e319]。
- 只靠访谈，不用文档、观察等其他证据核对[^ralph2020empirical-e326]。人们事后对自己为什么这样做的解释，不如他们对当下困扰的描述可靠；在软件场景中，代码、提交记录、项目管理数据都可以用来核对受访者的说法[^stol2016grounded-e23]。三角验证的做法见[案例研究](case_study.md#第六步从多个来源收集数据相互印证)。

### 第 7 步：判断理论饱和，然后停止

**怎么做**：当理论的各个部分都有充分支持、新数据不再引起理论的修改或重新解释时，就达到了**理论饱和**，可以停止收集[^stol2016grounded-e14]。它比访谈研究常说的"新受访者不再带来新信息"（见[访谈研究](interview_study.md#第一步选受访者)）要求更高：看的是理论有没有变，而不只是有没有新说法。`[本项目分析]`

**论文里要写清**：是否达到了饱和、**怎样判断的**[^ralph2020empirical-e317]，以及何时停止收集[^stol2016grounded-e24]。"访谈到第 N 个人时没有新内容了"只是一句话，最好说明最后几轮数据分别检验了理论的哪些部分、为什么没有引起修改。`[本项目分析]`

### 第 8 步：产出理论，而不是一组主题

这是扎根理论和一般定性分析最大的区别。研究者要超越表面的类别，发展出一个连贯的理论[^stol2016grounded-e15]：

- **结果要用概念来表述，赋予数据意义，而不只是描述数据**[^ralph2020empirical-e318]；
- **说明概念之间的关系**，推进到理论，而不是停在一组互不相连的主题[^ralph2020empirical-e319]；
- 最好用一张图概括主要概念和它们的关系[^ralph2020empirical-e320]。

Stol 等人举的一个例子：一项研究得出敏捷团队成员承担的几种角色，这些角色合在一起解释了团队是怎样自组织的，所以超出了单纯的角色分类[^stol2016grounded-e17]。

现实中这一步常常没做到：52 篇声称用扎根理论的论文中[^stol2016grounded-e16]，只有 8 篇明确给出了由概念和关系构成的理论；只产出"一组主题"的研究，往往只是零散借用了扎根理论的做法[^stol2016grounded-e17]。

### 第 9 步：检验和写作

- **检验结果**：参与者核查、请没参与研究的从业者提意见、请导师或同行审查编码，都是加分项[^ralph2020empirical-e319]；做法见[访谈研究](interview_study.md#第六步让分析可信)。
- **写具体做法，不写教程**：说明你自己怎么做的，包括偏离了流派指南的地方，而不是介绍扎根理论的原理[^stol2016grounded-e20][^ralph2020empirical-e325]。
- **把重要概念落到原始数据上**，例如给出引语[^ralph2020empirical-e318]；条件允许时提供访谈提纲、编码方案、编码示例[^ralph2020empirical-e320]。
- **和已有研究对话**：把理论与已有理论比较或整合[^ralph2020empirical-e320]，说明文献在研究中起了什么作用[^ralph2020empirical-e321]。
- **讨论可迁移性**：理论在多大程度上可能适用于其他地点、人群或情境[^ralph2020empirical-e318][^ralph2020empirical-e329]；反思你自己的偏见可能怎样影响了分析[^ralph2020empirical-e321]。

定性研究的质量标准见[访谈研究](interview_study.md#先记住定性研究的质量标准和定量研究不同)，证据链见[案例研究](case_study.md#第七步分析时保持证据链)；写作的一般做法见通用篇[写作](../04_write-and-publish/01_story-and-paper.md)。

---

## 3. 检查清单

下面依据 SIGSOFT 的扎根理论标准。

**必须做到**

- [ ] 写明用了哪个流派[^ralph2020empirical-e317]
- [ ] 描述数据：参与者的背景、文档类型、现场笔记的性质等[^ralph2020empirical-e317]
- [ ] 说明数据收集（理论抽样）和分析（持续比较）是怎样交替进行的[^ralph2020empirical-e317]
- [ ] 说明是否以及怎样判断达到了理论饱和[^ralph2020empirical-e317]
- [ ] 说明关键类别是通过哪些步骤得到的[^ralph2020empirical-e317]
- [ ] 结果用赋予数据意义的概念来表述，而不只是描述数据[^ralph2020empirical-e318]
- [ ] 重要概念明确扎根于原始数据，例如给出引语[^ralph2020empirical-e318]
- [ ] 讨论理论的可迁移性[^ralph2020empirical-e318]，披露主要局限[^ralph2020empirical-e103]

**做到更好**

- [ ] 结果包含概念之间的关系，并用图概括[^ralph2020empirical-e319][^ralph2020empirical-e320]
- [ ] 用表格展示类别到底层编码、概念到观察的对应[^ralph2020empirical-e320]
- [ ] 说明备忘录怎样推动了研究[^ralph2020empirical-e319]
- [ ] 数据覆盖多样的人或事物[^ralph2020empirical-e319]
- [ ] 用参与者核查、同行审查编码等方式检验结果[^ralph2020empirical-e319]
- [ ] 说明偏离流派之处、文献的作用，反思自己的偏见[^ralph2020empirical-e321]
- [ ] 提供访谈提纲、编码方案等补充材料[^ralph2020empirical-e320]

**做得出色**

- [ ] 用大量定量数据（如问卷）做三角验证[^ralph2020empirical-e322]
- [ ] 由研究团队完成，并说明各人的角色[^ralph2020empirical-e322]

**这些情况可以不做，不算缺陷**

- 为保护参与者（例如涉及骚扰等敏感话题），省略受访者的详细描述和直接引语[^ralph2020empirical-e324]

**审稿时常见、但不成立的批评**[^ralph2020empirical-e327]：你不必为此担心

- "缺少定量数据、因果分析、客观性、可推广性"
- "不可复现"或"没有公开访谈转录"
- "样本不具代表性"，例如"研究土耳其程序员的结论怎么推广到美国？"
- "结果应该呈现为另一套关系或另一个理论"

评价扎根理论研究应看可信度、共鸣、有用性（含义见[访谈研究](interview_study.md#先记住定性研究的质量标准和定量研究不同)），以及是否扩展了已有知识；内部效度、可复现性等定量研究的标准一般不适用[^ralph2020empirical-e323]。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只用了编码技巧，却写"我们用了扎根理论" | 这叫"方法混用"（method slurring）。只借用技巧的，直接说用了哪些技巧即可[^stol2016grounded-e20]；在 98 篇提到扎根理论的论文中，46 篇其实只用了它的技巧[^stol2016grounded-e16] |
| 先做完所有访谈再分析 | 没有收集与分析的交替，就没有理论抽样[^ralph2020empirical-e325][^stol2016grounded-e19] |
| 从文献中拿一套类别给数据归类 | 这是在套用已有框架，不是扎根理论[^stol2016grounded-e19][^stol2016grounded-e27] |
| 事先选好访谈对象，称之为"理论抽样" | 理论抽样是根据分析中的空缺决定下一步找谁[^stol2016grounded-e18] |
| 访谈了十几个相似的人就宣布"饱和" | 小而同质的样本会造成饱和的假象[^ralph2020empirical-e326] |
| 只产出几个互不相连的主题 | 扎根理论的产出应是概念和关系构成的理论[^ralph2020empirical-e319][^stol2016grounded-e17] |
| 方法部分写成扎根理论教程 | 读者需要知道的是你具体怎么做的[^ralph2020empirical-e325][^stol2016grounded-e20] |
| 不写流派，或声称一个流派却用另一个流派的步骤 | 各流派对研究问题、文献和编码的要求不同[^stol2016grounded-e26] |
| 写论文时才把研究"包装"成扎根理论 | 扎根理论必须从设计阶段就开始[^stol2016grounded-e20] |

---

## 5. 延伸阅读

- **扎根理论在软件工程中的用法和常见问题**：Stol, Ralph & Fitzgerald 2016。对比了三个流派，总结了核心做法，图 5 是一份很实用的"写作前自问清单"。
- **审稿标准**：SIGSOFT 实证研究标准中的扎根理论标准，附有推荐读物和范例论文。
- **各流派原著**：Stol 等人建议动手前先读几本所选流派的入门专著[^stol2016grounded-e21]，例如经典版的 Glaser & Strauss、Strauss 版的 Corbin & Strauss、建构主义版的 Charmaz。书目为 `[本项目分析]`，本项目没有读到这些专著的全文。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^stol2016grounded-e1]: Stol 等人 2016，§1。[证据](../../sources/notes/stol2016grounded.md#e1)
[^stol2016grounded-e2]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e2)
[^stol2016grounded-e3]: Stol 等人 2016，§2.3。[证据](../../sources/notes/stol2016grounded.md#e3)
[^stol2016grounded-e4]: Stol 等人 2016，§2.3。[证据](../../sources/notes/stol2016grounded.md#e4)
[^stol2016grounded-e5]: Stol 等人 2016，表 1"研究问题"一行。[证据](../../sources/notes/stol2016grounded.md#e5)
[^stol2016grounded-e6]: Stol 等人 2016，表 1"文献的作用"一行。[证据](../../sources/notes/stol2016grounded.md#e6)
[^stol2016grounded-e7]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e7)
[^stol2016grounded-e8]: Stol 等人 2016，表 1"编码步骤"一行（建构主义）。[证据](../../sources/notes/stol2016grounded.md#e8)
[^stol2016grounded-e9]: Stol 等人 2016，表 1"编码步骤"一行（经典与 Strauss 版）。[证据](../../sources/notes/stol2016grounded.md#e9)
[^stol2016grounded-e10]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e10)
[^stol2016grounded-e11]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e11)
[^stol2016grounded-e12]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e12)
[^stol2016grounded-e13]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e13)
[^stol2016grounded-e14]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e14)
[^stol2016grounded-e15]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e15)
[^stol2016grounded-e16]: Stol 等人 2016，摘要。[证据](../../sources/notes/stol2016grounded.md#e16)
[^stol2016grounded-e17]: Stol 等人 2016，§4.4。[证据](../../sources/notes/stol2016grounded.md#e17)
[^stol2016grounded-e18]: Stol 等人 2016，§4.2。[证据](../../sources/notes/stol2016grounded.md#e18)
[^stol2016grounded-e19]: Stol 等人 2016，§5.1。[证据](../../sources/notes/stol2016grounded.md#e19)
[^stol2016grounded-e20]: Stol 等人 2016，§5.2。[证据](../../sources/notes/stol2016grounded.md#e20)
[^stol2016grounded-e21]: Stol 等人 2016，§5.2。[证据](../../sources/notes/stol2016grounded.md#e21)
[^stol2016grounded-e22]: Stol 等人 2016，§5.1。[证据](../../sources/notes/stol2016grounded.md#e22)
[^stol2016grounded-e23]: Stol 等人 2016，§5.3。[证据](../../sources/notes/stol2016grounded.md#e23)
[^stol2016grounded-e24]: Stol 等人 2016，图 5。[证据](../../sources/notes/stol2016grounded.md#e24)
[^stol2016grounded-e25]: Stol 等人 2016，§1 与 §6。[证据](../../sources/notes/stol2016grounded.md#e25)
[^stol2016grounded-e26]: Stol 等人 2016，§4.3。[证据](../../sources/notes/stol2016grounded.md#e26)
[^stol2016grounded-e27]: Stol 等人 2016，§4.1。[证据](../../sources/notes/stol2016grounded.md#e27)
[^stol2016grounded-e28]: Stol 等人 2016，§4.2。[证据](../../sources/notes/stol2016grounded.md#e28)
[^ralph2020empirical-e316]: SIGSOFT 扎根理论标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e316)
[^ralph2020empirical-e317]: SIGSOFT 扎根理论标准，必要项（方法）。[证据](../../sources/notes/ralph2020empirical.md#e317)
[^ralph2020empirical-e318]: SIGSOFT 扎根理论标准，必要项（结果与讨论）。[证据](../../sources/notes/ralph2020empirical.md#e318)
[^ralph2020empirical-e319]: SIGSOFT 扎根理论标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e319)
[^ralph2020empirical-e320]: SIGSOFT 扎根理论标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e320)
[^ralph2020empirical-e321]: SIGSOFT 扎根理论标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e321)
[^ralph2020empirical-e322]: SIGSOFT 扎根理论标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e322)
[^ralph2020empirical-e323]: SIGSOFT 扎根理论标准，质量标准。[证据](../../sources/notes/ralph2020empirical.md#e323)
[^ralph2020empirical-e324]: SIGSOFT 扎根理论标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e324)
[^ralph2020empirical-e325]: SIGSOFT 扎根理论标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e325)
[^ralph2020empirical-e326]: SIGSOFT 扎根理论标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e326)
[^ralph2020empirical-e327]: SIGSOFT 扎根理论标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e327)
[^ralph2020empirical-e328]: SIGSOFT 标准术语表，Theoretical sampling。[证据](../../sources/notes/ralph2020empirical.md#e328)
[^ralph2020empirical-e329]: SIGSOFT 标准术语表，Credibility、Resonance、Transferability。[证据](../../sources/notes/ralph2020empirical.md#e329)
[^ralph2020empirical-e103]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e103)
