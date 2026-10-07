# 访谈研究：深度访谈一批人，归纳主题

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲**访谈研究**：对一批人做半结构化或开放式的深度访谈，再用定性分析从访谈记录中归纳主题。ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把这类研究叫作"定性调查"（qualitative survey）。

如果你要的是用问卷收集大量人的回答、再做统计，那是[问卷调查](questionnaire_survey.md)，不是本文的内容。研究涉及人时的一般伦理要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)，本文只讲访谈特有的部分。

本文是三篇定性研究文档中讲**抽样与饱和、访谈、编码和主题分析、定性质量标准**的一篇；[案例研究](case_study.md)和[扎根理论](grounded_theory.md)用到这些内容时链接到这里。

**适用范围** `[本项目分析]`：本文的审稿标准和多数例子来自软件工程（SIGSOFT 标准、Runeson 和 Höst 的案例研究指南、Baltes 和 Ralph 的抽样指南），编码一致性的讨论来自人机交互和协同工作方向（McDonald 等人）；主题分析和访谈提纲的做法分别出自心理学（Braun 和 Clarke）和护理学（Kallio 等人）的方法文献。其他学科做访谈研究时，先看本学科的规范。历史学用访谈留下关于过去的记录，做法和这里不同，见[口述历史](../07_fields/history-archaeology/research-types/oral_history.md)。

**常服务的套路**：[观察描述](../05_research-strategies/observe_describe.md)。

**读完本文，你应该能：**

- 判断自己的问题适不适合用访谈研究来回答；
- 选好受访者，设计访谈提纲，做好访谈和转录；
- 用主题分析从转录稿中归纳出主题，并说清自己的分析为什么可信；
- 明白定性研究的质量标准和定量研究不同，不被不合适的批评带偏。

---

## 1. 这是什么研究，什么时候用

SIGSOFT 标准给出的适用条件是：研究者和参与者一对一实时交谈；研究者提开放式问题，参与者回答；回答以某种方式记录下来；再对回答做某种定性分析[^ralph2020empirical-e345]。

**它擅长回答的问题** `[本项目分析]`：

- **"怎么样"和"为什么"**：开发者为什么不用某个工具，安全工程师怎样决定先修哪个漏洞，机器学习从业者怎样处理有问题的数据；
- **人的经历和看法**：某个群体遇到了哪些困难，他们怎样理解一件事；
- **还没人系统研究过的现象**：先通过访谈弄清有哪些因素，再决定后续做问卷或实验去测量什么。

它回答不了"有多少人这样做""A 是否导致 B"这类问题，这些要靠问卷、仓库挖掘或实验。`[本项目分析]` 在计算机领域，访谈在人机交互和协同工作方向很常见：McDonald 等人分析的 251 篇该方向定性论文中，179 篇（71.3%）用了访谈[^mcdonald2019reliability-e3]。软件工程、安全（如可用安全）、机器学习实践等方向也常用。`[本项目分析]`

**和相近方法的区别**：

| | 访谈研究 | 案例研究 | 扎根理论 | 问卷调查 |
|---|---|---|---|---|
| 数据 | 一批人的访谈 | 一个或几个场景中的多种数据 | 访谈等数据，与分析反复交替 | 大量人的标准化回答 |
| 受访者 | 来自不同地方 | 常来自同一组织 | 按正在形成的理论去找 | 尽量有代表性 |
| 主要产出 | 主题、概念、分类 | 对一个场景的深入理解 | 一套新理论 | 比例、相关关系 |

依据：受访者都来自同一组织时，应考虑案例研究标准；数据收集和分析反复交替时，应考虑扎根理论标准[^ralph2020empirical-e346]；访谈研究的访谈数量一般比案例研究多，案例研究靠多种数据互相印证[^ralph2020empirical-e347]。把访谈研究说成扎根理论或案例研究，是 SIGSOFT 标准列出的反面模式[^ralph2020empirical-e362]。问卷调查一列和"主要产出"一行为 `[本项目分析]`。

### 先记住：定性研究的质量标准和定量研究不同

这是做访谈研究最需要先弄明白的一点。SIGSOFT 标准写道：访谈研究应满足合适的定性质量标准；内部效度、构念效度、可推广性、信度等定量质量标准**一般不适用**[^ralph2020empirical-e348]。常用的定性标准有下面四条（定义出自 SIGSOFT 术语表）[^ralph2020empirical-e349]，[案例研究](case_study.md)和[扎根理论](grounded_theory.md)的标准也用它们：

| 标准 | 意思 |
|---|---|
| 可信度（credibility） | 结论有丰富的、来自多方声音的证据支持 |
| 共鸣（resonance） | 结论对参与者来说讲得通 |
| 有用性（usefulness） | 能给研究者、实践者或教育者可操作的建议 |
| 可迁移性（transferability） | 结果有可能适用于其他场景、人群或情况 |

背后的原因是研究立场不同（定性研究要不要谈"效度"的两种看法，见[效度与局限](../02_from-project-to-study/03_validity-and-limits.md)末尾的"不同的看法"）。许多定性研究者干脆不用"效度""信度"这些词，而用可信度、可迁移性等概念[^mcdonald2019reliability-e6]。用定量标准去评价定性研究，是一种常见错误[^mcdonald2019reliability-e7]；SIGSOFT 也把"因为诠释主义研究不符合实证主义规范而攻击它"列为不成立的批评[^ralph2020empirical-e373]。

---

## 2. 怎么做

### 第一步：选受访者

**怎么做：**

- **按目的去选，而不是谁方便就访谈谁。** 目的抽样（purposive sampling）是按某种逻辑或策略、仔细但非随机地选择对象，目标是找到信息丰富、能让你了解研究主题的人[^baltes2022sampling-e23]。"谁愿意谈就访谈谁"属于便利抽样[^baltes2022sampling-e25]；探索性研究应优先用目的抽样[^ralph2020empirical-e372]。
- **有意追求差异。** 按差异而不是相似性选受访者[^runeson2009guidelines-e14]，例如覆盖不同角色、不同性格的人[^runeson2009guidelines-e47]。参与者高度多样是 SIGSOFT 的加分项[^ralph2020empirical-e355]。在计算机领域，可以有意覆盖不同规模的公司、开源和商业项目、不同经验年限的人。`[本项目分析]`
- **随着分析调整要找的人。** 理论抽样（theoretical sampling）是根据正在形成的概念决定接下来找谁[^baltes2022sampling-e26]；要构建理论时，应优先用它[^ralph2020empirical-e372]。具体做法见[扎根理论](grounded_theory.md#第-6-步理论抽样根据分析决定下一步找谁)。
- **访谈到饱和为止。** 人数要在研究过程中决定，一个常用标准是"饱和"：新的受访者不再带来新信息或新观点[^runeson2009guidelines-e14]。SIGSOFT 把"提供饱和的证据，并说明怎样达到饱和"列为必要项[^ralph2020empirical-e352]。例如，可以记录每次访谈后新增了多少编码，说明最后几次访谈基本没有新编码。`[本项目分析]` 扎根理论说的"理论饱和"要求更高：新数据不再引起理论的修改，见[扎根理论](grounded_theory.md#第-7-步判断理论饱和然后停止)。
- **说清选人的理由。** 定性研究要让读者看懂你为什么选这些人[^baltes2022sampling-e7]。目的抽样本质上是主观的[^baltes2022sampling-e24]，所以更要把选人逻辑写出来，让读者判断。

**为什么：** 访谈研究的目的通常不是从样本推广到总体，而是找到能讲清问题的人。没有概率抽样、没有统计意义上的代表性，在 SIGSOFT 看来不是缺陷，除非你的研究明确以代表性为目标[^ralph2020empirical-e363]。

**容易错在哪：** 只访谈少数相似的人，会造成观点趋同、"已经饱和"的假象[^ralph2020empirical-e362]。比如只访谈自己实验室合作公司的五位工程师，他们说法一致，很可能只是因为背景相同。`[本项目分析]`

### 第二步：设计访谈提纲

**怎么做：**

1. **从研究问题推出访谈问题，但不要照搬研究问题的措辞**[^runeson2009guidelines-e6]。研究问题是写给研究者看的，受访者需要的是具体、好回答的问题。`[本项目分析]`
2. **用半结构化的形式**：事先列好问题，但不必按顺序问，允许临场发挥和深入探索[^runeson2009guidelines-e7]。
3. **以开放问题为主。** 开放问题欢迎各种回答，封闭问题只给几个选项[^runeson2009guidelines-e8]。例如问"说说你上次排查线上故障的经过"，而不是"你排查故障时会看日志吗"。`[本项目分析]`
4. **每个话题配好追问（probe）。** 提纲有两层：主要话题和追问[^kallio2016systematic-e1]。追问可以事先设计，让不同访谈者覆盖的内容更一致；也可以临场请对方就某一点多讲一些[^kallio2016systematic-e3]。追问的方式包括复述对方的话、用附和表示兴趣，或者干脆保持沉默，让对方边想边说[^kallio2016systematic-e4]。
5. **安排好顺序。** 可以从开放问题开始，逐步转向具体问题（"漏斗式"）[^runeson2009guidelines-e11]；话题从轻松的开始，再过渡到更深入的[^kallio2016systematic-e2]。
6. **先预试。** 可以在团队内部互相试，请外部专家看，或者找一两位潜在受访者实地试[^kallio2016systematic-e5]。内部预试能帮你去掉含糊的问题和诱导性问题[^kallio2016systematic-e6]。

**容易错在哪：** 诱导性问题，例如"你是不是觉得这个工具太难用了"，会把你的预期塞进对方嘴里。`[本项目分析]` 另外，有些伦理审查委员会要求事先审查每个访谈问题，而临场追问做不到这一点[^kallio2016systematic-e7]；申请伦理审查时，最好写明追问的大致范围。`[本项目分析]`

### 第三步：做访谈

- **开场**：说明访谈目的和数据怎么用，再问几个容易回答的背景问题[^runeson2009guidelines-e9]。
- **敏感问题放后面**：要等建立信任之后再问。**结尾**时总结你听到的要点，请对方确认或纠正，避免误解[^runeson2009guidelines-e10]。
- **录音**（征得同意后）：只靠笔记很难记下所有细节，而且访谈当时无法知道什么重要[^runeson2009guidelines-e12]。
- **知情同意和报酬**：说明怎样取得自由、个人、知情的同意，给了什么报酬，怎样避免强迫[^ralph2020empirical-e369]（一般要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)）。

**留意权力关系**（[案例研究](case_study.md)进入组织时同样适用）。如果通过公司领导、导师等"把关人"（gatekeeper）招募受访者，对方可能并不是自愿参与，例如雇主可能强迫员工参加[^ralph2020empirical-e370]。这时要说明怎样减轻把关人和受访者之间的权力关系，保证同意是自由的[^ralph2020empirical-e186]。同理，访谈自己的学生或下属时，对方可能不敢说真话，也不敢拒绝。`[本项目分析]` SIGSOFT 把"描述研究者和参与者之间的关系与互动"列为加分项[^ralph2020empirical-e355]。访谈方式也可以变通：例如研究聋人开发者时，用文字消息访谈是可以接受的[^ralph2020empirical-e364]。

### 第四步：转录

- **尽量自己转录。** 转录费时，但常常在转录中冒出新想法，所以 Runeson & Höst 建议研究者自己做[^runeson2009guidelines-e13]。转录也不只是把声音变成文字，它本身就是一种诠释[^braun2006using-e5]。
- **别人或软件转录时，一定对照录音检查**，并多花时间熟悉数据[^braun2006using-e6]。自动转录工具对专业术语、口音和多人交谈常常出错。`[本项目分析]`
- **可以请受访者审阅转录稿**，纠正说错或记错的地方[^runeson2009guidelines-e13]。

### 第五步：编码和主题分析

下面以主题分析（thematic analysis）为例：它是在数据中识别、分析和报告模式（"主题"）的方法[^braun2006using-e1]。**先分清编码和主题：** 编码（code）是给一小段话贴的标签，比如"文档过时""怕被同事评判"；主题（theme）更宽，是把许多编码归拢后形成的、和研究问题相关的模式[^braun2006using-e9]。

**Braun & Clarke 的六个阶段**[^braun2006using-e8]：

1. **熟悉数据**：反复读转录稿，边读边记下想法[^braun2006using-e7]；
2. **生成初始编码**：系统地给整个数据集编码；
3. **寻找主题**：把编码归拢成候选主题；
4. **复查主题**：同一主题内的数据要聚得起来，不同主题之间要分得开[^braun2006using-e11]；
5. **定义和命名主题**：检验办法是看能否用几句话说清每个主题的范围和内容[^braun2006using-e12]；
6. **撰写报告**。

**归纳还是演绎，二选一并写清楚。** 归纳编码让编码方案从数据中产生，目标是提出新的概念或理论；演绎编码用基于已有理论的预设编码方案，目标是检验已有理论[^ralph2020empirical-e357]。归纳式的主题和数据本身贴得更紧；演绎式对数据整体的描述少，对某个方面分析得细[^braun2006using-e2][^braun2006using-e3]。但即使归纳，研究者也无法摆脱自己的理论立场[^braun2006using-e2]。

**几个实用做法：**

- **建一份编码手册（codebook）**：写下每个编码的名称、定义、什么情况下用、什么情况下不用，并附一两个例子。手册会随分析不断修改。`[本项目分析]` 多人编码时，分歧正好能帮你把手册改得更好[^mcdonald2019reliability-e14]。
- **写分析备忘（memo）**：随时记下对编码之间关系、可能的主题和自己疑问的想法。写备忘、反思和复查，正是为单人研究设计的做法[^mcdonald2019reliability-e13]。备忘录在扎根理论中是核心步骤，写法见[扎根理论](grounded_theory.md#第-5-步写备忘录)。
- **整理成表格**：行是编码，列是受访者，可以一眼看出哪些人提到了什么[^runeson2009guidelines-e17]。
- **边访谈边分析**：分析中产生的新认识，可能要求你调整后面的访谈问题[^runeson2009guidelines-e15]。如果你大量地在收集和分析之间来回迭代，就更接近扎根理论，应参考它的标准[^ralph2020empirical-e346]。
- **保留"唱反调"的说法**，不要只编码符合主流的部分[^braun2006using-e10]。
- **主题不是数出来的。** 一个主题最好在数据中多次出现，但出现次数多不等于更重要，什么算主题需要研究者判断[^braun2006using-e4]。

### 第六步：让分析可信

定性研究不靠"换一个人做能得到同样结果"来证明自己，而是靠下面这些做法 `[本项目分析，依据下列资料]`。它们对[案例研究](case_study.md)和[扎根理论](grounded_theory.md)同样适用：

- **反身性（reflexivity）**：反思自己可能的偏见，以及自己和受访者、社群的关系可能带来的影响[^ralph2020empirical-e350]。这是 SIGSOFT 的必要项[^ralph2020empirical-e353]。例如，你自己就是某个工具的开发者，去访谈它的用户，就要说明这一点，并说明你怎样防止自己只听到想听的话。`[本项目分析]`
- **参与者核查（member checking）**：把分析结果拿给受访者看。参与者不一定要同意结论，但这样做能提高研究的效度[^runeson2009guidelines-e18]。SIGSOFT 列出的验证方式还有：对话式访谈、请没参与研究的实践者反馈、请导师或其他研究者审查编码[^ralph2020empirical-e358]。
- **主动找其他解释**：考虑数据的其他明显解读，以及叙述中的差异和矛盾[^braun2006using-e17][^ralph2020empirical-e359]。
- **公开研究过程**：除了参与者核查，再次访谈、与其他数据来源互相印证（三角验证，详见[案例研究](case_study.md#第六步从多个来源收集数据相互印证)）、公开研究过程、说明研究者的立场，都是体现可靠性的做法[^mcdonald2019reliability-e5]。

> **不同的看法：要不要多人编码并计算一致性？**
>
> 编码者间信度（inter-rater reliability，简称 IRR）是衡量两名以上编码者判断有多一致的统计量，常用的有 Cohen's Kappa（一种衡量两人判断有多一致的统计量）、Krippendorff's Alpha 等。它源于实证主义的定量传统，用在定性研究上一直有争议[^mcdonald2019reliability-e1]。
>
> - **主张计算的理由**：多人编码能减少个人偏见[^mcdonald2019reliability-e15][^runeson2009guidelines-e16]；SIGSOFT 把"多人编码并分析一致性"列为优秀项[^ralph2020empirical-e361]。下列情形尤其适合计算：多人分头编码不同部分的数据、套用已有的编码手册、要报告定量结果[^mcdonald2019reliability-e11]。如果结论依赖频次统计（例如"X 出现的次数是 Y 的三倍"），就有充分理由计算[^mcdonald2019reliability-e12]。
> - **主张不必计算的理由**：SIGSOFT 的一致性补充标准本身就不适用于诠释主义的定性分析，因为在这种立场下，不同分析者本来就会有不同看法[^ralph2020empirical-e365]。编码本身是分析过程的一部分、只有一位研究者、编码几乎不需要解读时，也不适合计算[^mcdonald2019reliability-e10]。多人套用预设编码方案给材料编码，比多人对 2000 页访谈稿做归纳编码现实得多[^ralph2020empirical-e366]。统计量不能代替对数据的解读[^mcdonald2019reliability-e8]。McDonald 等人分析的定性论文中，只有约九分之一计算了它[^mcdonald2019reliability-e2]。
>
> 实际操作中可以这样做：**让做法和你的研究立场、分析目标一致**[^mcdonald2019reliability-e9]。归纳式、诠释取向的分析，可以由一人主编码，再请第二人审查、讨论分歧，并在论文里说明理由；演绎式编码、多人分工或要报告频次时，就计算一致性。`[本项目分析]` 不管哪种，都不要只算百分比一致率，因为它没考虑碰巧一致的可能[^mcdonald2019reliability-e4]；也不要算好几种指标、只报最好看的[^ralph2020empirical-e368]。

### 第七步：写报告

- **描述受访者和访谈者。** 这是必要项：受访者的人口学特征、工作角色，以及访谈者的经验和视角[^ralph2020empirical-e351]。常见做法是一张受访者表，每人一个编号（P1、P2……），列出角色、经验年限、组织类型等。`[本项目分析]`
- **从原话到结论，给出清楚的证据链**[^ralph2020empirical-e352]。大量使用直接引语支持关键观点[^ralph2020empirical-e356]；选生动、能抓住要点的引文，并把它们嵌在你的分析叙述中[^braun2006using-e13]。
- **说清方法细节**：问了哪些核心问题、问题是开放还是封闭的[^ralph2020empirical-e354]，用什么方式记录、怎样转录[^ralph2020empirical-e356]。最好把访谈提纲、编码方案、编码示例作为补充材料公开[^ralph2020empirical-e354]。
- **说清是谁做的分析。** 不要写"主题从数据中浮现"，这否认了研究者在识别和选择主题中的主动作用[^braun2006using-e18]；方法部分多用主动语态，被动语态会掩盖研究者的作用[^mcdonald2019reliability-e16]。**说的和做的要一致**[^braun2006using-e19]。

**保护受访者。** 匿名化的一般要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)。访谈研究里最常见的漏洞是"某公司＋某职位"这类背景信息，拼起来就可能锁定一个人[^ralph2020empirical-e253]。如果是小团队或敏感话题，引语里的细节、受访者表里的组合信息都要斟酌。`[本项目分析]` 在敏感研究中，为保护参与者而省略受访者详细描述和直接引语，是可以接受的[^ralph2020empirical-e364]。不公开完整转录稿也不算缺陷[^ralph2020empirical-e363]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 的访谈研究（Qualitative Surveys）标准，它是软件工程领域的审稿标准；其他学科以本学科的规范为准 `[本项目分析]`。

**必须做到**

- [ ] 说明受访者是怎么选出来的[^ralph2020empirical-e351]
- [ ] 描述受访者（如人口学特征、工作角色）和访谈者（如经验、视角）[^ralph2020empirical-e351]
- [ ] 从受访者原话到研究发现有清楚的证据链[^ralph2020empirical-e352]
- [ ] 明确回答研究问题[^ralph2020empirical-e352]
- [ ] 提供饱和的证据，说明怎样达到饱和[^ralph2020empirical-e352]
- [ ] 反思研究者自己可能的偏见[^ralph2020empirical-e353]
- [ ] 说明怎样取得知情同意、给了什么报酬、怎样避免强迫[^ralph2020empirical-e369]

**做到更好**

- [ ] 描述核心问题的内容和形式（开放还是封闭），公开访谈提纲、编码方案、编码示例、判定规则[^ralph2020empirical-e354]
- [ ] 参与者高度多样；描述研究者和参与者的关系[^ralph2020empirical-e355]
- [ ] 大量使用直接引语；说明记录和转录方式[^ralph2020empirical-e356]
- [ ] 明确用演绎编码检验已有理论，或用归纳编码提出新理论[^ralph2020empirical-e357]
- [ ] 用参与者核查、外部反馈或编码审查验证结果[^ralph2020empirical-e358]
- [ ] 讨论可迁移性、与已有研究的关系、其他可能的解释[^ralph2020empirical-e359]
- [ ] 说明激励和伦理流程[^ralph2020empirical-e360]

**做得出色**：用多种分析方法互相印证；纵向设计（同一受访者访谈多次）；概率抽样并统计分析回应偏差；多人编码并分析一致性[^ralph2020empirical-e361]

**这些情况可以不做，不算缺陷**：受访者有特殊需要时改用文字等方式访谈；敏感研究中为保护参与者，省略受访者详细描述和直接引语[^ralph2020empirical-e364]

**审稿时常见、但不成立的批评**（SIGSOFT 标准列出的，针对软件工程的投稿）：你不必为此担心，但最好在论文里主动说明立场

- "缺少定量数据、因果分析、客观性、内部效度、信度或可推广性"[^ralph2020empirical-e363]
- "不可重复""没有公开转录稿"[^ralph2020empirical-e363]
- "没有概率抽样、没有代表性"（除非研究明确以代表性为目标）[^ralph2020empirical-e363]
- 不考虑选人方式和饱和论证，就说"样本太小"[^ralph2020empirical-e371]
- "只有一个编码者"，而多人编码不现实或与研究立场不符[^ralph2020empirical-e367]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只访谈少数相似的人，就宣称饱和 | 造成观点趋同、已经饱和的假象[^ralph2020empirical-e362] |
| 提纲里有诱导性问题 | 把你的预期塞给对方，应在预试时去掉[^kallio2016systematic-e6] |
| 只记笔记，不录音 | 漏掉细节，而且当时无法判断什么重要[^runeson2009guidelines-e12] |
| 自动转录后不对照录音检查 | 转录稿应当对照原始录音检查[^braun2006using-e6] |
| 把访谈提纲里的问题直接当作主题 | 等于没有做分析[^braun2006using-e15] |
| 把引文串起来，几乎不加分析 | 这不是主题分析[^braun2006using-e14] |
| 一两个例子就撑起一个主题 | 把个例说成了贯穿全体的主题[^braun2006using-e16] |
| 用定量的效度、信度、可推广性来要求自己 | 用错了标准[^ralph2020empirical-e348] |
| 把访谈研究说成扎根理论或案例研究 | SIGSOFT 列出的反面模式[^ralph2020empirical-e362] |
| 用"公司＋职位"描述受访者 | 受访者可能被认出来[^ralph2020empirical-e253] |

---

## 5. 延伸阅读

- **主题分析入门**：Braun & Clarke 2006，讲六个阶段、常见陷阱和好的主题分析应满足什么，出自心理学，是常用的主题分析入门文献。
- **访谈提纲怎么设计**：Kallio 等人 2016，综述了半结构化访谈提纲的设计步骤，包括追问和预试。出自护理学，但做法通用。
- **在软件工程中做访谈**：Runeson & Höst 2009 的访谈一节，讲访谈的阶段、提问方式、录音和转录。它是案例研究指南，沿用效度、信度等说法，阅读时注意和本文的定性质量标准区分 `[本项目分析]`。
- **要不要算一致性**：McDonald 等人 2019，给出了何时需要、何时不需要计算编码者间信度的建议。
- **标准原文**：SIGSOFT 的 Qualitative Surveys 标准，以及编码者一致性、涉及人的伦理、抽样三份补充标准；抽样方法详见 Baltes & Ralph 2022。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e345]: SIGSOFT 访谈研究标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e345)
[^ralph2020empirical-e346]: SIGSOFT 访谈研究标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e346)
[^ralph2020empirical-e347]: SIGSOFT 访谈研究标准，Notes。[证据](../../sources/notes/ralph2020empirical.md#e347)
[^ralph2020empirical-e348]: SIGSOFT 访谈研究标准，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e348)
[^ralph2020empirical-e349]: SIGSOFT Glossary。[证据](../../sources/notes/ralph2020empirical.md#e349)
[^ralph2020empirical-e350]: SIGSOFT Glossary，Reflexivity。[证据](../../sources/notes/ralph2020empirical.md#e350)
[^ralph2020empirical-e351]: SIGSOFT 访谈研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e351)
[^ralph2020empirical-e352]: SIGSOFT 访谈研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e352)
[^ralph2020empirical-e353]: SIGSOFT 访谈研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e353)
[^ralph2020empirical-e354]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e354)
[^ralph2020empirical-e355]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e355)
[^ralph2020empirical-e356]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e356)
[^ralph2020empirical-e357]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e357)
[^ralph2020empirical-e358]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e358)
[^ralph2020empirical-e359]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e359)
[^ralph2020empirical-e360]: SIGSOFT 访谈研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e360)
[^ralph2020empirical-e361]: SIGSOFT 访谈研究标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e361)
[^ralph2020empirical-e362]: SIGSOFT 访谈研究标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e362)
[^ralph2020empirical-e363]: SIGSOFT 访谈研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e363)
[^ralph2020empirical-e364]: SIGSOFT 访谈研究标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e364)
[^ralph2020empirical-e365]: SIGSOFT 编码者一致性补充标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e365)
[^ralph2020empirical-e366]: SIGSOFT 编码者一致性补充标准，Practicality。[证据](../../sources/notes/ralph2020empirical.md#e366)
[^ralph2020empirical-e367]: SIGSOFT 编码者一致性补充标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e367)
[^ralph2020empirical-e368]: SIGSOFT 编码者一致性补充标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e368)
[^ralph2020empirical-e369]: SIGSOFT 涉及人的伦理补充标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e369)
[^ralph2020empirical-e186]: SIGSOFT 涉及人的伦理补充标准，脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e186)
[^ralph2020empirical-e370]: SIGSOFT Glossary，Gatekeeper。[证据](../../sources/notes/ralph2020empirical.md#e370)
[^ralph2020empirical-e253]: SIGSOFT 涉及人的伦理补充标准，脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e253)
[^ralph2020empirical-e371]: SIGSOFT 抽样补充标准，反面模式与不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e371)
[^ralph2020empirical-e372]: SIGSOFT 抽样补充标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e372)
[^ralph2020empirical-e373]: SIGSOFT General Standard，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e373)
[^baltes2022sampling-e23]: Baltes & Ralph 2022，§2.1.2。[证据](../../sources/notes/baltes2022sampling.md#e23)
[^baltes2022sampling-e24]: Baltes & Ralph 2022，§2.1.2。[证据](../../sources/notes/baltes2022sampling.md#e24)
[^baltes2022sampling-e25]: Baltes & Ralph 2022，§2.4。[证据](../../sources/notes/baltes2022sampling.md#e25)
[^baltes2022sampling-e26]: Baltes & Ralph 2022，§2.4。[证据](../../sources/notes/baltes2022sampling.md#e26)
[^baltes2022sampling-e7]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e7)
[^braun2006using-e1]: Braun & Clarke 2006，What is thematic analysis?。[证据](../../sources/notes/braun2006using.md#e1)
[^braun2006using-e2]: Braun & Clarke 2006，Inductive vs theoretical thematic analysis。[证据](../../sources/notes/braun2006using.md#e2)
[^braun2006using-e3]: Braun & Clarke 2006，Inductive vs theoretical thematic analysis。[证据](../../sources/notes/braun2006using.md#e3)
[^braun2006using-e4]: Braun & Clarke 2006，What counts as a theme?。[证据](../../sources/notes/braun2006using.md#e4)
[^braun2006using-e5]: Braun & Clarke 2006，Phase 1，Transcription of verbal data。[证据](../../sources/notes/braun2006using.md#e5)
[^braun2006using-e6]: Braun & Clarke 2006，Phase 1，Transcription of verbal data。[证据](../../sources/notes/braun2006using.md#e6)
[^braun2006using-e7]: Braun & Clarke 2006，Phase 1。[证据](../../sources/notes/braun2006using.md#e7)
[^braun2006using-e8]: Braun & Clarke 2006，Table 1。[证据](../../sources/notes/braun2006using.md#e8)
[^braun2006using-e9]: Braun & Clarke 2006，Phase 2。[证据](../../sources/notes/braun2006using.md#e9)
[^braun2006using-e10]: Braun & Clarke 2006，Phase 2。[证据](../../sources/notes/braun2006using.md#e10)
[^braun2006using-e11]: Braun & Clarke 2006，Phase 4。[证据](../../sources/notes/braun2006using.md#e11)
[^braun2006using-e12]: Braun & Clarke 2006，Phase 5。[证据](../../sources/notes/braun2006using.md#e12)
[^braun2006using-e13]: Braun & Clarke 2006，Phase 6。[证据](../../sources/notes/braun2006using.md#e13)
[^braun2006using-e14]: Braun & Clarke 2006，Potential pitfalls。[证据](../../sources/notes/braun2006using.md#e14)
[^braun2006using-e15]: Braun & Clarke 2006，Potential pitfalls。[证据](../../sources/notes/braun2006using.md#e15)
[^braun2006using-e16]: Braun & Clarke 2006，Potential pitfalls。[证据](../../sources/notes/braun2006using.md#e16)
[^braun2006using-e17]: Braun & Clarke 2006，Potential pitfalls。[证据](../../sources/notes/braun2006using.md#e17)
[^braun2006using-e18]: Braun & Clarke 2006，What is thematic analysis?。[证据](../../sources/notes/braun2006using.md#e18)
[^braun2006using-e19]: Braun & Clarke 2006，What makes good thematic analysis?。[证据](../../sources/notes/braun2006using.md#e19)
[^kallio2016systematic-e1]: Kallio 等人 2016，Results。[证据](../../sources/notes/kallio2016systematic.md#e1)
[^kallio2016systematic-e2]: Kallio 等人 2016，Results。[证据](../../sources/notes/kallio2016systematic.md#e2)
[^kallio2016systematic-e3]: Kallio 等人 2016，Results。[证据](../../sources/notes/kallio2016systematic.md#e3)
[^kallio2016systematic-e4]: Kallio 等人 2016，Results。[证据](../../sources/notes/kallio2016systematic.md#e4)
[^kallio2016systematic-e5]: Kallio 等人 2016，Results，Pilot testing。[证据](../../sources/notes/kallio2016systematic.md#e5)
[^kallio2016systematic-e6]: Kallio 等人 2016，Results，Pilot testing。[证据](../../sources/notes/kallio2016systematic.md#e6)
[^kallio2016systematic-e7]: Kallio 等人 2016，Discussion。[证据](../../sources/notes/kallio2016systematic.md#e7)
[^mcdonald2019reliability-e1]: McDonald 等人 2019，§1、§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e1)
[^mcdonald2019reliability-e2]: McDonald 等人 2019，摘要。[证据](../../sources/notes/mcdonald2019reliability.md#e2)
[^mcdonald2019reliability-e3]: McDonald 等人 2019，§4.3。[证据](../../sources/notes/mcdonald2019reliability.md#e3)
[^mcdonald2019reliability-e4]: McDonald 等人 2019，§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e4)
[^mcdonald2019reliability-e5]: McDonald 等人 2019，§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e5)
[^mcdonald2019reliability-e6]: McDonald 等人 2019，§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e6)
[^mcdonald2019reliability-e7]: McDonald 等人 2019，§2.3。[证据](../../sources/notes/mcdonald2019reliability.md#e7)
[^mcdonald2019reliability-e8]: McDonald 等人 2019，§2.3。[证据](../../sources/notes/mcdonald2019reliability.md#e8)
[^mcdonald2019reliability-e9]: McDonald 等人 2019，§2.3。[证据](../../sources/notes/mcdonald2019reliability.md#e9)
[^mcdonald2019reliability-e10]: McDonald 等人 2019，§1。[证据](../../sources/notes/mcdonald2019reliability.md#e10)
[^mcdonald2019reliability-e11]: McDonald 等人 2019，§1。[证据](../../sources/notes/mcdonald2019reliability.md#e11)
[^mcdonald2019reliability-e12]: McDonald 等人 2019，§5.3.4。[证据](../../sources/notes/mcdonald2019reliability.md#e12)
[^mcdonald2019reliability-e13]: McDonald 等人 2019，§5.1.2。[证据](../../sources/notes/mcdonald2019reliability.md#e13)
[^mcdonald2019reliability-e14]: McDonald 等人 2019，§5.2.3。[证据](../../sources/notes/mcdonald2019reliability.md#e14)
[^mcdonald2019reliability-e15]: McDonald 等人 2019，§5.3.6。[证据](../../sources/notes/mcdonald2019reliability.md#e15)
[^mcdonald2019reliability-e16]: McDonald 等人 2019，§5.4.2。[证据](../../sources/notes/mcdonald2019reliability.md#e16)
[^runeson2009guidelines-e6]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e6)
[^runeson2009guidelines-e7]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e7)
[^runeson2009guidelines-e8]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e8)
[^runeson2009guidelines-e9]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e9)
[^runeson2009guidelines-e10]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e10)
[^runeson2009guidelines-e11]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e11)
[^runeson2009guidelines-e12]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e12)
[^runeson2009guidelines-e13]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e13)
[^runeson2009guidelines-e14]: Runeson & Höst 2009，§4.2。[证据](../../sources/notes/runeson2009guidelines.md#e14)
[^runeson2009guidelines-e15]: Runeson & Höst 2009，§5.2。[证据](../../sources/notes/runeson2009guidelines.md#e15)
[^runeson2009guidelines-e16]: Runeson & Höst 2009，§5.2。[证据](../../sources/notes/runeson2009guidelines.md#e16)
[^runeson2009guidelines-e17]: Runeson & Höst 2009，§5.2.1。[证据](../../sources/notes/runeson2009guidelines.md#e17)
[^runeson2009guidelines-e18]: Runeson & Höst 2009，§3.3。[证据](../../sources/notes/runeson2009guidelines.md#e18)
[^runeson2009guidelines-e47]: Runeson & Höst 2009，§4.2，第 147 页。[证据](../../sources/notes/runeson2009guidelines.md#e47)
