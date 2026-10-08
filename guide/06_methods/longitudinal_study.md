# 纵向研究：长时间重复观察同一批对象

本文讲**纵向研究**（longitudinal study）：在一段时间内，对同一批对象反复测量同样的东西，看它怎样变化。例如跟踪一批项目好几年，看技术债怎样累积和偿还；或者每隔几个月调查同一批开发者，看他们的工作效率怎样变化。

纵向数据很多来自代码仓库的历史，怎样从仓库里抽取和清洗数据，见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)；效度威胁的一般做法，见[效度与局限：设计阶段就想清楚](../02_from-project-to-study/03_validity-and-limits.md)。本文只讲"随时间重复观察"带来的特殊问题。

**适用范围** `[本项目分析]`：本文的检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）为软件工程写的纵向研究标准，仓库数据的陷阱来自软件工程，以人为对象的规划原则来自信息系统领域（Kehr & Kowatsch 2015），例子以软件项目和开发者为主。其他学科做纵向研究时，先看本学科的规范。例如健康领域随时间跟踪人群、比较不同暴露的队列研究，规则更严格，见[观察性流行病学研究](observational_epidemiology.md)。

**常服务的套路**：[观察描述](../05_research-strategies/observe_describe.md)（描述现象随时间怎样变化）。

**读完本文，你应该能：**

- 判断自己的问题需不需要纵向设计，以及两轮测量够不够；
- 定好测量的时点和间隔，选好对象，并预先应对流失和幸存者偏差；
- 认出"把纵向数据当横断面数据分析"等常见错误；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为：关注一个现象随时间变化和演进的研究，对同样的变量（例如生产率、技术债）在一段时间内重复观察；分析代码演化这类随时间变化的数据集也算[^ralph2020empirical-e257]。它有两条硬要求：**至少观测两轮**，并且**每个对象（人或制品）在各轮之间都能对上号**[^ralph2020empirical-e258]。

**它擅长回答的问题**：

- **变化是什么样的**：在增长还是下降，是直线还是先快后慢[^kehr2015quantitative-e7]。
- **有没有变化、为什么变化**[^kehr2015quantitative-e8]：例如引入某个新流程后，缺陷是否减少 `[本项目分析]`。
- **为因果关系提供线索**：原因发生在结果之前[^kehr2015quantitative-e1]。SIGSOFT 标准把"利用纵向数据确定谁先谁后、并在统计上控制第三变量来考察因果"列为加分项[^ralph2020empirical-e264]。SIGSOFT 标准指出，纵向研究正是利用时间来尽量提高内部效度（结论是否真由所说的原因造成）[^ralph2020empirical-e269]。

**和相近类型的区别** `[本项目分析，依据下列资料]`：

| | 横断面研究 | 回溯式调查 | 纵向研究 | 实验 |
|---|---|---|---|---|
| 观测几次 | 一个时间点 | 一次，让人回忆过去 | 至少两轮，对象前后对应 | 通常是操纵前后或不同条件 |
| 研究者是否主动改变变量 | 否 | 否 | 否 | 是 |
| 能说明什么 | 某一时刻的分布和相关 | 依赖记忆，误差大 | 变化的形态，时间先后 | 因果效应 |

只看一个时间点的分析，SIGSOFT 建议参考数据科学标准，主动操纵变量的则参考实验标准[^ralph2020empirical-e258]（本项目对应的文档是[数据科学研究](data_science.md)和[对照实验](controlled_experiment.md)）；让对象回忆过去变化的一次性调查，有人也称作纵向研究，但 Kehr & Kowatsch 不采用这种定义[^kehr2015quantitative-e3]。他们采用的定义是：对**同一批单位**的**同一批结果变量**重复观察[^kehr2015quantitative-e2]。

**两种变体**[^ralph2020empirical-e271]：

- **经验取样**（experience sampling）：在短时间内（通常一到三周）每天测量多次，强调记录当下的状态，而不是事后回想。
- **队列研究**（cohort study）：随时间观察对象，比较暴露程度不同的几组。它有比本文更严格的规则，做之前要读专门的指南，健康领域的做法见[观察性流行病学研究](observational_epidemiology.md)。

**在计算机各方向** `[本项目分析]`：软件工程里常见的是跟踪项目、代码或开发者；系统和安全方向可以跟踪同一批软件在多个版本中的性能或漏洞；机器学习方向可以跟踪同一个部署模型的效果随时间的变化。只要是"同一批对象、多个时点、同样的测量"，本文的要求都适用。

---

## 2. 怎么做

### 第一步：先想清楚要回答哪一类"变化"问题

问题类型决定需要几轮测量：

- **要描述变化的形态**（例如线性增长），至少要三轮；要识别非线性变化，还要更多[^kehr2015quantitative-e7]。
- **只问"有没有变化、为什么变化"**，常用两轮的前测—后测设计[^kehr2015quantitative-e8]。但两轮设计一直被批评容易受测量误差等问题干扰，很难分清变化是真实的还是测量造成的。常见的补救是加一个随机分组、起点条件相同的对照组：测量误差对各组影响相同，真实变化体现为两组变化量的差异[^kehr2015quantitative-e9]。

**容易错在哪**：先收两轮数据，事后却想讲"变化趋势"。两个点连不出曲线。

### 第二步：按现象的节律定时点和间隔

测几轮、隔多久，要根据现象本身变化的快慢来定，SIGSOFT 标准把这列为必要项[^ralph2020empirical-e259]。先从理论或已有研究出发，想清楚结果变量预期会怎样波动，再决定测量次数、间隔和时间尺度[^kehr2015quantitative-e4]。

- **时间尺度不一定是日历时间。** 任何不可逆的量都可以，例如系统使用时长[^kehr2015quantitative-e5]。`[本项目分析]` 研究代码时，常用的时间尺度还有版本号、发布次数或提交数，选哪个要看你的问题。
- **没有现成理论可依**：先做小规模的定性预研究来估计节律，或者按变化最快的那个变量来安排间隔[^kehr2015quantitative-e6]。

**容易错在哪**：间隔和现象的周期不匹配，SIGSOFT 列为反面模式[^ralph2020empirical-e270]。例如按年取样，就看不到每个发布周期内技术债的起落 `[本项目分析]`。

### 第三步：选对象，保证能前后对上号，并警惕幸存者偏差

- **每个对象在各轮之间都要能识别**[^ralph2020empirical-e259]。以人为对象，要有稳定的匿名编号；以项目为对象，要处理改名、迁移和合并 `[本项目分析]`。
- **说清对象怎样选出、怎样过滤。** 以软件仓库为对象时，要说明做了哪些质量控制来保证制品的一致性[^ralph2020empirical-e263]。
- **警惕幸存者偏差。** 只用今天还存在的股市去分析过去 100 年，得到的平均回报会远高于分析 100 年前所有股市的结果[^ralph2020empirical-e266]。在仓库数据里，这个问题很常见：GitHub 接口只给仓库的当前状态，仓库被删除后，它的事件和元数据全部丢失[^kalliamvakou2016indepth-e3]。`[本项目分析]` 所以，从"今天还活跃的项目"出发回看它们的历史，得到的是一批幸存者，项目失败的原因在这样的样本里看不到。更稳妥的做法是在起点时刻定好样本，然后向后跟踪，或者使用事先存档的数据。

### 第四步：预先应对流失，并如实报告

流失（attrition）指对象中途退出：人不再回复问卷，项目停止维护或被删除。它在纵向研究里几乎不可避免，后果有两个：样本变小、统计功效（真有效应时能检测出来的概率）下降；留下的和退出的对象可能有系统性差异[^kehr2015quantitative-e13]。例如接受度低的人都中途退出，平均接受度就会被人为抬高[^kehr2015quantitative-e14]。

- **事先**：招募比所需更多的对象，用激励提高回应率，把测量轮数和间隔控制在合理范围[^kehr2015quantitative-e15]；用统计功效分析论证样本量[^ralph2020empirical-e262]。
- **事后**：报告每一轮流失了多少，说明缺失数据怎样处理[^ralph2020empirical-e262]。
- **不要悄悄删掉不完整的数据。** Kehr & Kowatsch 回顾的 21 项信息系统纵向研究中，20 项没有明确处理流失，只是把不完整的数据删掉[^kehr2015quantitative-e16]。

### 第五步：让测量在各轮之间保持一致

纵向研究比较的是"前后之差"。如果测量方法本身变了，差异可能来自测量，而不是现象。

- 讨论各轮数据是否一致，例如问卷的重测信度（同一批人隔一段时间再答，结果是否稳定）；检查各轮之间数据分布的差异[^ralph2020empirical-e265]。
- **平台和数据的含义也会变。** 例如 GitHub 上"关注者（watchers）"的含义在 2012 年 8 月前后不同[^kalliamvakou2016indepth-e6]；git 历史也可能被改写[^bird2009promises-e2]。仓库数据的这类陷阱见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md#第四步抽取和清洗数据)。
- `[本项目分析]` 用工具计算指标时（例如用静态分析工具估算技术债），各轮要固定同一个工具版本和同一套规则；中途必须升级的，要用新版本把旧数据重算一遍。

### 第六步：用适合相依数据的方法分析

纵向数据前后相依：后一轮的数据在一定程度上可以由前一轮预测。这会违反很多常用统计方法"残差互不相关"的前提[^kehr2015quantitative-e17]，用普通的相关分析可能夸大变量之间的关系[^kehr2015quantitative-e18]。"把纵向数据当横断面数据来分析"是 SIGSOFT 列出的反面模式[^ralph2020empirical-e270]。

- 只关心群体层面的变化：可以用重复测量的方法，例如重复测量方差分析、配对 t 检验；要研究不同对象的变化轨迹有何不同：可以用多层模型（也叫分层线性模型）[^kehr2015quantitative-e19]。
- 要论证为什么选这种分析方法，并说明它适合数据前后相依的特点[^ralph2020empirical-e260]。
- 纵向分析通常涉及很多变量和多次比较，更容易碰巧得到"显著"结果。建议调整显著性阈值，或者使用贝叶斯统计[^ralph2020empirical-e261]。显著性和效应量的一般问题，见[分析与解读：报告差多少、有多确定](../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

### 第七步：小心"时间"本身带来的效度威胁

时间不只带来你想看的变化，也可能掩盖或制造变化：

- **练习效应**：反复测同一批用户，效率提高可能只是因为他们熟悉了、学会绕开问题，而不是产品变好了[^kehr2015quantitative-e10]。
- **记忆和迎合**：被试记得上一轮怎么答的，会为了前后一致而照答，掩盖真实变化；测得越多，越容易猜到研究目的，按研究者的期望作答[^kehr2015quantitative-e11]。
- **期间的外部事件** `[本项目分析]`：跟踪期间团队换了开发流程、编程语言发布了大版本、公司裁员，都可能同时影响所有对象，被误认为是你研究的因素造成的。要记录跟踪期间的重大事件，并在分析中考虑它们。

研究"为什么变化"时，最有力的办法是引入条件相似的对照组[^kehr2015quantitative-e12]。无法用统计控制的混杂因素，要在论文中讨论[^ralph2020empirical-e264]。

### 第八步：报告

除了一般的写作要求（见[讲清故事，写成论文](../04_write-and-publish/01_story-and-paper.md)），纵向研究要特别写清：对象是谁、怎样选出[^ralph2020empirical-e263]；时点和间隔怎样确定；每轮流失多少、缺失怎样处理[^ralph2020empirical-e262]；指标怎样从概念变成测量[^ralph2020empirical-e263]；收集数据的成本和用过的激励[^ralph2020empirical-e267]。公开数据集、采集脚本和分析脚本[^ralph2020empirical-e267]。承认了局限，结论就要真的受它约束[^ralph2020empirical-e103][^ralph2020empirical-e126]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 的纵向研究标准，它是为软件工程写的。

**必须做到**

- [ ] 至少两轮数据收集，对象在各轮之间可识别[^ralph2020empirical-e259]
- [ ] 根据现象的自然节律确定轮数和间隔[^ralph2020empirical-e259]
- [ ] 论证分析方法，且方法适合数据前后相依的特点[^ralph2020empirical-e260]
- [ ] 讨论显著性阈值，或说明贝叶斯先验的依据[^ralph2020empirical-e261]
- [ ] 论证样本量；描述各轮的数据流失；说明缺失数据怎样处理[^ralph2020empirical-e262]
- [ ] 描述研究对象；讨论指标的构念效度[^ralph2020empirical-e263]

**做到更好**

- [ ] 提供数据集、采集脚本或工具、分析脚本和复现说明[^ralph2020empirical-e267]
- [ ] 利用时间先后考察因果，并在统计上控制第三变量；讨论无法控制的混杂因素[^ralph2020empirical-e264]
- [ ] 讨论各轮数据的一致性，检查各轮分布的差异[^ralph2020empirical-e265]
- [ ] 说明数据收集的成本和激励[^ralph2020empirical-e267]
- [ ] 处理幸存者偏差[^ralph2020empirical-e266]

**做得出色**

- [ ] 用多阶段筛选流程确定研究对象；跟踪时间特别长，例如超过五年[^ralph2020empirical-e268]

**审稿时常见、但不成立的批评**：你不必为此担心

- 笼统地说"测量间隔太短"或"太长"；不给理由地说"轮数不够"；不做事后功效计算就说"样本太小"[^ralph2020empirical-e272]
- 比较次数不多，却要求用更保守的显著性阈值或贝叶斯方法；论文已明确承认推广性局限，却仍抱怨推广性[^ralph2020empirical-e273]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只有两轮数据，却讲"变化趋势" | 描述变化形态至少要三轮[^kehr2015quantitative-e7] |
| 间隔凭方便定，不看现象节律 | 可能完全看不到真实的变化形态[^ralph2020empirical-e270][^kehr2015quantitative-e4] |
| 从今天还活跃的项目往回看 | 幸存者偏差，失败的对象被排除在外[^ralph2020empirical-e266][^kalliamvakou2016indepth-e3] |
| 不完整的数据直接删掉，不报告流失 | 退出者可能有系统性差异，结论被扭曲[^kehr2015quantitative-e13][^kehr2015quantitative-e14] |
| 中途换了测量工具或口径 | 前后差异可能来自测量而不是现象[^ralph2020empirical-e265][^kalliamvakou2016indepth-e6] |
| 把纵向数据当横断面数据分析 | 违反独立性前提，可能夸大关系[^ralph2020empirical-e270][^kehr2015quantitative-e18] |
| 把变化都归因于研究的因素 | 练习效应、迎合、外部事件都可能造成变化[^kehr2015quantitative-e10][^kehr2015quantitative-e11] |

---

## 5. 延伸阅读

- **SIGSOFT 纵向研究标准**：完整的检查清单、反面模式，以及软件工程中的范例论文列表，适合动手前和投稿前对照。
- **Kehr & Kowatsch 2015**：面向信息系统领域以人为对象的定量纵向研究，讲了四条规划原则（跟随自然节律、选对轮数、注意内部效度、选对分析方法），并对比了几种常用的统计模型。做问卷或用户研究类纵向研究时最有用。
- **仓库数据的陷阱**：Bird 等人 2009 和 Kalliamvakou 等人 2016，用仓库历史做纵向分析前应该读，要点已整理在[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)中。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e257]: SIGSOFT 纵向研究标准，定义与 Application。[证据](../../sources/notes/ralph2020empirical.md#e257)
[^ralph2020empirical-e258]: SIGSOFT 纵向研究标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e258)
[^ralph2020empirical-e259]: SIGSOFT 纵向研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e259)
[^ralph2020empirical-e260]: SIGSOFT 纵向研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e260)
[^ralph2020empirical-e261]: SIGSOFT 纵向研究标准，必要项脚注 4。[证据](../../sources/notes/ralph2020empirical.md#e261)
[^ralph2020empirical-e262]: SIGSOFT 纵向研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e262)
[^ralph2020empirical-e263]: SIGSOFT 纵向研究标准，必要项及脚注 6、7。[证据](../../sources/notes/ralph2020empirical.md#e263)
[^ralph2020empirical-e264]: SIGSOFT 纵向研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e264)
[^ralph2020empirical-e265]: SIGSOFT 纵向研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e265)
[^ralph2020empirical-e266]: SIGSOFT 纵向研究标准，加分项及脚注 8。[证据](../../sources/notes/ralph2020empirical.md#e266)
[^ralph2020empirical-e267]: SIGSOFT 纵向研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e267)
[^ralph2020empirical-e268]: SIGSOFT 纵向研究标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e268)
[^ralph2020empirical-e269]: SIGSOFT 纵向研究标准，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e269)
[^ralph2020empirical-e270]: SIGSOFT 纵向研究标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e270)
[^ralph2020empirical-e271]: SIGSOFT 纵向研究标准，Variations。[证据](../../sources/notes/ralph2020empirical.md#e271)
[^ralph2020empirical-e272]: SIGSOFT 纵向研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e272)
[^ralph2020empirical-e273]: SIGSOFT 纵向研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e273)
[^ralph2020empirical-e103]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e103)
[^ralph2020empirical-e126]: SIGSOFT General Standard，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e126)
[^kehr2015quantitative-e1]: Kehr & Kowatsch 2015，§1。[证据](../../sources/notes/kehr2015quantitative.md#e1)
[^kehr2015quantitative-e2]: Kehr & Kowatsch 2015，§1。[证据](../../sources/notes/kehr2015quantitative.md#e2)
[^kehr2015quantitative-e3]: Kehr & Kowatsch 2015，§1。[证据](../../sources/notes/kehr2015quantitative.md#e3)
[^kehr2015quantitative-e4]: Kehr & Kowatsch 2015，§4.1。[证据](../../sources/notes/kehr2015quantitative.md#e4)
[^kehr2015quantitative-e5]: Kehr & Kowatsch 2015，§4.1。[证据](../../sources/notes/kehr2015quantitative.md#e5)
[^kehr2015quantitative-e6]: Kehr & Kowatsch 2015，§4.1。[证据](../../sources/notes/kehr2015quantitative.md#e6)
[^kehr2015quantitative-e7]: Kehr & Kowatsch 2015，§4.2。[证据](../../sources/notes/kehr2015quantitative.md#e7)
[^kehr2015quantitative-e8]: Kehr & Kowatsch 2015，§4.2。[证据](../../sources/notes/kehr2015quantitative.md#e8)
[^kehr2015quantitative-e9]: Kehr & Kowatsch 2015，§4.2。[证据](../../sources/notes/kehr2015quantitative.md#e9)
[^kehr2015quantitative-e10]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e10)
[^kehr2015quantitative-e11]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e11)
[^kehr2015quantitative-e12]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e12)
[^kehr2015quantitative-e13]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e13)
[^kehr2015quantitative-e14]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e14)
[^kehr2015quantitative-e15]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e15)
[^kehr2015quantitative-e16]: Kehr & Kowatsch 2015，§4.3。[证据](../../sources/notes/kehr2015quantitative.md#e16)
[^kehr2015quantitative-e17]: Kehr & Kowatsch 2015，§4.4。[证据](../../sources/notes/kehr2015quantitative.md#e17)
[^kehr2015quantitative-e18]: Kehr & Kowatsch 2015，§4.4。[证据](../../sources/notes/kehr2015quantitative.md#e18)
[^kehr2015quantitative-e19]: Kehr & Kowatsch 2015，§4.4。[证据](../../sources/notes/kehr2015quantitative.md#e19)
[^kalliamvakou2016indepth-e3]: Kalliamvakou 等人 2016，§4.8 Peril XII。[证据](../../sources/notes/kalliamvakou2016indepth.md#e3)
[^kalliamvakou2016indepth-e6]: Kalliamvakou 等人 2016，§4.8 Peril XIII。[证据](../../sources/notes/kalliamvakou2016indepth.md#e6)
[^bird2009promises-e2]: Bird 等人 2009，§3 Peril 4。[证据](../../sources/notes/bird2009promises.md#e2)
