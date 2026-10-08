# 环境工程：学科概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-08

本文讲环境工程（水和废水处理、大气质量、固体废物、污染场地修复等）研究里的几件具体事：采样前怎样做计划，测量怎样做质量控制，低浓度结果怎样报告，和水厂、社区合作要注意什么。和地球与环境科学重叠的内容（野外观测、环境过程）见[地球与环境科学篇](../earth-environmental-sciences/README.md)；化工过程的研究方式和生命周期评价的更多用法见[化学工程篇](../chemical-engineering/README.md)；各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里的主线各章和[贯穿全程](../../08_throughout/README.md)。这里只写本学科特有的东西。本学科常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)；具体做法见[本学科常用的研究方法](#本学科常用的研究方法)。

本文引用的规范几乎都来自美国：美国环境保护署、美国地质调查局、美国土木工程师学会的文件，以及美国化学会的一本期刊。它们只是例子，不是全世界通用的规矩；在中国或其他国家做研究，以当地主管部门、资助方和目标期刊的规定为准 `[本项目分析]`。

**读完本文，你应该能：**

- 说清本领域的研究在实验室、中试、现场和模型之间怎样分工；
- 在采样前按"数据质量目标"做计划，知道质量保证项目计划里要写什么；
- 说出空白样、平行样、加标样各检查什么，知道检出限是怎么定的、低于检出限的数据怎样处理；
- 在和水厂、社区合作时，知道要注意哪些伦理和信任问题；
- 知道生命周期评价是什么、容易错在哪里。

---

## 本领域研究怎样运转

### 研究对象：污染控制技术和受污染的环境

美国环境保护署（Environmental Protection Agency，EPA）在 2002 年的一份指南里，把"环境技术"定义为一大类东西：污染控制设备和系统、废物处理和储存设施、场地修复技术，例如处理废气的湿式洗涤器、土壤淋洗、处理水的颗粒活性炭装置[^epa2002qapp-e17]。本领域的研究大致围绕两件事：开发和改进这类技术；测量、预测污染物在水、气、土中的浓度和去向 `[本项目分析]`。

一个技术类课题可能要经过几个尺度。下表是本项目的归纳 `[本项目分析]`：

| 尺度 | 做什么 | 要注意什么 |
|---|---|---|
| 实验室小试 | 在烧杯、柱子或小型反应器里，用配制的水样或真实水样试验 | 条件容易控制，但可能和真实环境差很远（见下文期刊要求） |
| 中试 | 在水厂、污水厂或场地上搭较大的装置，用真实进水连续运行 | 要和运营方协调，周期长，进水水质会波动 |
| 现场采样 | 到河流、管网、场地上采样，送实验室分析 | 要事先做采样计划和质量控制（见下文） |
| 建模 | 用模型预测处理效果或污染物迁移 | EPA 指南要求写清：是应用已有模型（先评估它能不能用），还是因为没有合适的模型而开发新模型[^epa2002qapp-e5] |

有的期刊明确要求研究走出"理想条件"。以美国化学会（American Chemical Society，ACS）的期刊《Environmental Science & Technology》（简称 ES&T）为例，它的作者指南要求：

- 在符合实际环境的条件和浓度下评估，浓度报告**实测值**，不报告名义值（配制时打算加多少）[^estauthorguidelines-e6]；
- 新材料（如吸附剂、催化剂）至少在一种环境条件下、用有实际意义的污染物浓度测试过[^estauthorguidelines-e9]；
- 新测量技术尽可能用真实环境样品验证[^estauthorguidelines-e3]；
- 环境监测研究的结论，要能适用于采样地点和时间以外[^estauthorguidelines-e7]。

这些是一本期刊的要求，别的期刊未必这样规定。但它提示你：只在实验室理想条件下做出的结果，投这类期刊时说服力有限 `[本项目分析]`。

### 发表：以 ES&T 为例

下面以 ES&T 的作者指南（2026 年 10 月读取）为例，说明投稿时会遇到哪些要求。期刊规定会更新，其他期刊的规则也可能不同，以目标期刊当时的要求为准：

- **新意是第一道门槛。** ES&T 写明，新意不足是常见的拒稿原因[^estauthorguidelines-e1]；只报告常规数据、或研究的问题已经很清楚的稿件不予考虑[^estauthorguidelines-e2]；只描述标准实验室或现场测试结果、或商业产品表现的研究也不适合[^estauthorguidelines-e4]。
- **投稿信很重要。** ES&T 说，相当一部分投稿没有送审，因为编辑认为它在新意、科学价值或环境重要性上不够；投稿信是说服编辑的机会[^estauthorguidelines-e12]。
- **偏化学工程、催化剂合成或分析化学的稿件，要简要论证它对环境领域有首要意义**，并在适当时和最先进的方法比较[^estauthorguidelines-e8]。
- **篇幅**：研究论文上限 7000 词[^estauthorguidelines-e10]；紧迫的初步发现可以投姊妹刊 ES&T Letters[^estauthorguidelines-e11]。
- **数据要存进公共数据库。** ES&T 要求所有发表的论文把材料、数据和实验方案存入公共数据库[^estauthorguidelines-e14]；代码是论文核心部分时，要写清语言、编译器或解释器、操作系统的具体版本[^estauthorguidelines-e15]。
- **预印本可以发**：录用前发到 ChemRxiv、bioRxiv、arXiv 等有 DOI（数字对象标识符，一种永久链接）的平台，但要在稿件中引用[^estauthorguidelines-e16]。
- **学位论文要注意**：投稿内容用在学位论文里的，要么把学位论文放进有 DOI 的公开仓库，要么在论文正式发表前推迟或撤下学位论文的网上版本[^estauthorguidelines-e17]。

本领域以期刊还是会议发表为主、署名顺序惯例、审稿周期，本文资料未涉及，以导师和目标期刊的要求为准。

---

## 和其他领域不同的地方

下表是本项目的归纳，用来帮你快速定位差别，不是严格的学科划分 `[本项目分析]`。

| | 环境工程 | 计算机领域 |
|---|---|---|
| 数据从哪来 | 实物样品：水、气、土、污泥，要采集、保存、运输、分析 | 多为代码、系统和数据集上的实验 |
| 误差主要在哪 | EPA 指南认为，一般来说采样误差远大于测量误差[^epa2006dqo-e7] | 随机种子、数据划分、实现细节等（见[计算机篇](../computer-science/README.md)） |
| 质量控制 | 有成套的正式做法：质量保证项目计划、空白样、平行样、加标样（见下文） | 主要靠公开代码和制品评估 |
| "测不到"怎么办 | 有检出限和报告限，低于它们的数据要专门处理（见下文） | 很少遇到 |
| 结果给谁用 | 可能被监管部门、水厂、社区拿来做决定，也可能作为法庭证据[^epa2002qapp-e8] | 主要是学术同行和业界 |
| 要打交道的人 | 可能有水厂、污水厂、场地业主、社区居民 | 较少涉及；涉及人的研究见对应的研究方法 |

---

## 本领域的规范和报告标准

### 采样前先做计划：EPA 的数据质量目标流程

环境数据可能被用来判断"是否达标"，或估计"污染物平均浓度是多少"。EPA 推荐在这类情况下用**数据质量目标**（Data Quality Objectives）流程做计划[^epa2006dqo-e2]，理由是：采样前不做计划，收来的数据满足不了项目需要的可能性会高得不可接受[^epa2006dqo-e1]。EPA 2006 年的指南把这个流程分成七步，可以反复进行[^epa2006dqo-e4]。括号里是本项目的简要解释 `[本项目分析]`：

1. 说明问题；
2. 确定研究目标（数据要回答什么问题）；
3. 确定需要哪些信息；
4. 划定研究边界（研究对象、空间和时间范围）；
5. 确定分析方法（用什么统计量、怎样得出结论）；
6. 规定性能或验收标准（能容忍多大的错误）；
7. 制定获取数据的计划（采多少、在哪采、用什么方法测）。

这份指南里几条值得记住的要点：

- **先定义"一个样品代表什么"。** 研究对象是空气、水、土壤这类连续介质时，必须把采样单元定义成一定的面积、体积或质量[^epa2006dqo-e6]。
- **资源多投在采样上，不只追求测得更准。** 指南说，一般来说采样误差远大于测量误差，需要投入更多资源去控制[^epa2006dqo-e7]；预计空间或时间上变化很大时，可以考虑用便宜、精度低一些的分析方法，换取更多地点和时间的样品[^epa2006dqo-e9]。
- **错误决定只能控制，不能消除。** 用数据做统计检验，永远无法完全排除做错决定的可能[^epa2006dqo-e8]；所以第 6 步要事先定好性能或验收标准[^epa2006dqo-e4]。
- **用别人的数据，先查它的质量保证和质量控制信息**，看它能不能满足你的需要[^epa2006dqo-e10]。
- **计划写多细、多严，要和数据的用途、手头的资源相称**[^epa2006dqo-e11]。
- **把用数据的人拉进来。** 指南说，做计划的团队通常包括项目负责人、技术人员、数据使用者和利益相关方[^epa2006dqo-e5]。
- **可以边采边调整。** EPA 技术创新项目开发的 Triad 方法，就是让早期采样的结果指导后续采样[^epa2006dqo-e3]。

### 把计划写下来：EPA 的质量保证项目计划

**质量保证项目计划**（Quality Assurance Project Plan）把项目的技术规划结果写在一处：数据工作怎样做、质量目标是什么、关键人员是谁[^epa2002qapp-e1]。EPA 2002 年的指南要求它在项目开始前完成并获批[^epa2002qapp-e2]。

适用范围要看清：这是 **EPA 对它资助的项目**的政策。凡是 EPA 资助、要收集、评价、使用或报告环境数据（包括用已有数据和建模），或涉及环境技术设计、建造、运行的工作，都要有获批的计划[^epa2002qapp-e3]。不是 EPA 资助的项目，是否要写、写成什么样，以你的资助方和单位规定为准；没人要求时，按它的结构写一份简化版，也能帮你在动手前把问题想清楚 `[本项目分析]`。按 EPA 的"分级"原则，某一项不适用时，写明为什么不适用即可[^epa2002qapp-e4]。

### 质量控制样品：空白、平行样、加标

先理解质量控制的目的：**不是消除误差，而是测量或估计误差的影响**[^epa2002qapp-e9]。EPA 的质量保证项目计划指南要求对每项测量写明做哪些质量控制检查、多久做一次[^epa2002qapp-e13]。该指南提到的几类：

| 质量控制样品 | 是什么 | 检查什么 |
|---|---|---|
| 空白样（blank） | 不含目标物的"干净"样品 | 采样和测定各阶段带入的污染[^epa2002qapp-e10] |
| 现场空白（field blank） | 带到采样现场、暴露于采样条件，再带回实验室按环境样品处理[^epa2002qapp-e14] | 采样现场和运输环节带入的污染（本项目从定义推出） `[本项目分析]` |
| 平行样、分样 | 重复测同一样品，或把一个样品分成几份分别测 | 随机误差，即精密度[^epa2002qapp-e12] |
| 同点样（collocated samples），也叫现场平行样 | 同一时间、同一地点采的两份以上、可视为相同的样品[^epa2002qapp-e16] | 平行样可用来说明测量或采样环节的精密度[^epa2002qapp-e12] |
| 标准样、基质加标样（matrix spike） | 已知浓度的样品；或往真实样品里加入已知量的目标物[^epa2002qapp-e15] | 系统误差，即偏差[^epa2002qapp-e11]；基质对回收率的影响[^epa2002qapp-e15] |

论文里要报告这些结果：ES&T 要求适用时报告不确定度评估或敏感性分析，以及充分的质量保证和质量控制[^estauthorguidelines-e5]。

### 检出限和"测不到"的数据

**方法检出限**（Method Detection Limit）在美国 EPA 的定义是：能报告的最低测得浓度，报告它时有 99% 的把握认为它和方法空白的结果不同[^epa2016mdl-e2]。下面的测定程序来自美国联邦法规中《清洁水法》分析方法的附录[^epa2016mdl-e1]；其他国家和其他类型的检测有各自的标准 `[本项目分析]`。它的要求说明，检出限要由实验室按自己的全部流程实测：

- 必须包含实验室处理样品的**全部步骤**[^epa2016mdl-e3]；
- 至少 7 个加标样和 7 个方法空白，分至少 3 批、在 3 个不同日期制备和分析[^epa2016mdl-e4]；
- 初次测定时**不要用统计方法剔除离群值**，因为数据少，而且这个程序就是要反映方法日常的波动[^epa2016mdl-e5]；
- 用加标样和方法空白分别算一个值，取较大的[^epa2016mdl-e6]；
- 至少每 13 个月重新计算一次[^epa2016mdl-e7]。

另一个常见的词是**报告限**：低于这个浓度，实验室就没有把握给出具体数值[^helsel2020statistical-e6]。报告为"低于报告限"的数据，在统计上叫**删失数据**[^helsel2020statistical-e1]。

怎样分析删失数据，Helsel 等人为美国地质调查局（United States Geological Survey）编写的教材《水资源统计方法》（2020 年版）给了明确提醒：

- **不要随手把"未检出"替换成报告限的一半。** 这样替换后再做 t 检验，在水资源领域很常见，但可能漏掉真实存在的差别，也可能找出不存在的差别[^helsel2020statistical-e2]。
- **更好的办法**：比较两组哪组偏高时，可以把低于最高报告限的数据都当作并列的秩，做秩和检验，不用编造数值[^helsel2020statistical-e4]；这样不会假装知道每个未检出值的确切数值[^helsel2020statistical-e3]。
- **影响有多大看比例。** 在趋势分析中，把删失值都替换成任意值，会让斜率估计有偏；但"小于"值很少（约 5% 以下）时，影响可能不大[^helsel2020statistical-e5]。

所以论文里要写清：检出限和报告限是多少、怎么定的，有多少数据低于它们，统计时怎样处理 `[本项目分析]`。

### 样品编号和监管链

以下做法出自 EPA 的质量保证项目计划指南：

- **每个样品一个唯一编号**，全程追踪，避免样品被弄混[^epa2002qapp-e6]。
- **监管链**（chain of custody）：记录样品从采集到实验室分析，每一步由谁持有、怎样处理[^epa2002qapp-e7]。做法可能包括样品标签、每个经手人签字的记录、用封条密封的容器；数据可能作为法庭证据时，项目可能会要求这样做[^epa2002qapp-e8]。

学术研究不一定需要法律意义上的监管链；但如果你的数据可能被监管部门、诉讼或公众争议用到，最好从一开始就按这个标准记录 `[本项目分析]`。样品和数据的通用整理方法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。

### 和水厂、社区合作；环境正义

本领域的研究可能要在别人的设施里、别人的家里做：水厂、污水厂、场地业主、居民 `[本项目分析]`。职业伦理准则可以作为参考。以美国土木工程师学会（American Society of Civil Engineers，ASCE）给会员定的伦理准则为例（2020 年 10 月最近一次更新）[^asce2020code-e10]：

- 首先保护公众的健康、安全和福祉[^asce2020code-e2]，这一条高于其他一切责任[^asce2020code-e1]；
- 只在有充分知识和真实信念时如实发表专业意见[^asce2020code-e3]，只在自己胜任的领域工作[^asce2020code-e8]；
- 讲清实际的、潜在的或可能被认为存在的利益冲突[^asce2020code-e6]；对客户和雇主指明的专有信息保密[^asce2020code-e7]；
- 承认社区在历史、社会和文化上的不同需要，并把这些考虑纳入工作[^asce2020code-e4]。

和水厂合作时，数据能否公开、以什么形式公开，最好在开始前就书面谈好 `[本项目分析]`。研究涉及居民的样品或数据时，ES&T 要求写明批准的伦理委员会和批件编号，并声明是在知情同意下获得的[^estauthorguidelines-e18]；通用原则见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)。

**环境正义**是一个相关概念。美国 EPA 网站 2024 年的定义是：在政府机构决策和其他影响健康与环境的联邦活动中，所有人不分收入、种族、肤色、国籍、部落归属或残障，都得到公正对待并能有意义地参与[^epa2024environmentaljustice-e1]；并免受不成比例的健康和环境不利影响，包括多种负担的累积影响[^epa2024environmentaljustice-e2]。要注意三点：本项目 2026 年 10 月访问时，这个页面已经下线，只能通过 Internet Archive 2024 年 5 月的快照读到；这个定义来自当时的美国联邦政策，此后美国的相关政策已有变化，本文资料没有展开；这里只用它说明概念，其他国家有各自的说法 `[本项目分析]`。

一个例子是美国密歇根州弗林特市的饮用水铅污染。下面的内容来自参与其中的弗吉尼亚理工大学团队成员 Roy 和 Edwards 2019 年写的回顾。这是当事团队一方的叙述，不是中立的调查；文中被批评的个人和组织不一定认同 `[本项目分析]`。

- 据作者说，2015 年，弗林特居民、弗吉尼亚理工大学团队等人的合作最先揭露了供水污染[^roy2019citizen-e1]。大学出技术方案、分析和经费，居民出本地知识、把自己家当采样点[^roy2019citizen-e2]；由居民协调的全市采样最终覆盖了 269 户家庭[^roy2019citizen-e3]。
- 作者认为，科学家忽视有本地知识的人，后果可能是灾难性的[^roy2019citizen-e5]。
- 作者也记录了后来的问题，例如有人收集没有代表性的数据，让居民对洗澡用水产生了没有根据的恐慌[^roy2019citizen-e6]。作者引用 Freitag 等人提出的提高可信度的策略，其中包括培训参与者、质量保证程序、和专业人员的数据交叉比对[^roy2019citizen-e4]。

从这个例子可以看到：社区合作可以发现被忽视的问题；采样代表性和质量控制，在社区合作里同样不能少 `[本项目分析]`。

### 生命周期评价

**生命周期评价**（Life Cycle Assessment）是"从摇篮到坟墓"的评估：从开采原材料开始，到所有材料回归自然为止[^epa2006lca-e1]。按 EPA 2006 年的入门报告，它分四部分：确定目标和范围、清单分析、影响评价、结果解释[^epa2006lca-e2]。化工过程中的用法见[化学工程篇](../chemical-engineering/README.md)。

它的价值在于看整个产品系统，避免只盯一个环节造成的"局部最优"[^epa2006lca-e3]。例如方案 1 固体废物少，看起来更环保；做完生命周期评价，可能发现它在空气、水、土地三方面的总影响反而更大[^epa2006lca-e4]。

这份报告提醒的几个容易出错的地方：

- **比较的基准不对。** 要仔细选**功能单位**，即用来衡量和展示结果的基准[^epa2006lca-e7]。比较两种墙体保温材料，要按同一功能（减少热流的能力）来比[^epa2006lca-e8]。
- **不写假设。** 不写明假设，结果可能被断章取义或误读[^epa2006lca-e9]。
- **忽视数据的限制。** 能拿到什么数据，会大大影响结果的准确性[^epa2006lca-e5]。
- **把"哪个更好"当成客观结论。** 按国际标准 ISO 14042，判断哪个方案更好，涉及哪类影响更重要，这是主观判断[^epa2006lca-e10]。
- **以为它能回答一切。** 它不能告诉你哪个方案最省钱、效果最好[^epa2006lca-e6]。

---

## 本学科常用的研究方法

跨学科的方法见下面的链接，这里只写本学科额外要注意的地方；实验室和中试研究、生命周期评价目前没有单独的做法页，见上文。

- [野外观测研究](../../06_methods/field_study.md)、[纵向研究](../../06_methods/longitudinal_study.md)：现场监测和长期重复监测同一地点。按数据质量目标做计划，配齐质量控制样品（见上文）。
- [定量仿真](../../06_methods/simulation_study.md)：水质模型、大气扩散模型、地下水迁移模型。要写清是应用已有模型还是开发新模型[^epa2002qapp-e5]。
- [数据科学](../../06_methods/data_science.md)：分析已有的监测数据。先查数据的质量保证和质量控制信息[^epa2006dqo-e10]，并正确处理低于报告限的数据[^helsel2020statistical-e2]。
- [案例研究](../../06_methods/case_study.md)、[访谈研究](../../06_methods/interview_study.md)、[问卷调查](../../06_methods/questionnaire_survey.md)：研究污染事件、社区经历和公众认知时会用到。涉及人时要经过伦理委员会批准，ES&T 要求在论文里写明[^estauthorguidelines-e18]。

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，按核心主张来定，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表列出环境工程常用的四种套路，以及每种通常靠什么证据、按什么标准评判。

表的分组和"在环境工程里的样子"一栏是本项目的归纳；标准多出自美国环境保护署的指南和 ES&T 一本期刊的作者指南，只代表脚注里的出处。解释因果、综合等其他套路在本学科怎样用，本文资料未涉及 `[本项目分析]`。

| 套路 | 在环境工程里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md) | 开发和改进"环境技术"：污染控制设备、废物处理设施、场地修复技术等[^epa2002qapp-e17]，常从实验室小试走到中试 | ES&T 要求在符合实际的条件和浓度下评估，报告实测浓度[^estauthorguidelines-e6]；新材料至少在一种环境条件下、用有实际意义的浓度测过[^estauthorguidelines-e9]；偏催化剂合成、化学工程的稿件，适当时要和最先进的方法比较[^estauthorguidelines-e8]；只描述标准测试或商业产品表现的研究不够[^estauthorguidelines-e4] | 本学科没有单独的做法页；思路可参考[工程研究](../computer-science/practices/engineering_research.md)（计算机）、[定量仿真](../../06_methods/simulation_study.md) |
| [观察描述](../../05_research-strategies/observe_describe.md) | 现场监测，例如估计某种污染物的平均浓度[^epa2006dqo-e2] | 采样前按[数据质量目标流程](#采样前先做计划epa-的数据质量目标流程)做计划[^epa2006dqo-e1]；采样误差一般远大于测量误差[^epa2006dqo-e7]；ES&T 要求监测研究的结论能适用于采样地点和时间以外[^estauthorguidelines-e7] | [野外观测研究](../../06_methods/field_study.md)、[纵向研究](../../06_methods/longitudinal_study.md)、[数据科学](../../06_methods/data_science.md) |
| [测量](../../05_research-strategies/measure.md) | 开发新的测量技术；测定方法检出限 | ES&T 要求新测量技术尽可能用真实环境样品验证[^estauthorguidelines-e3]；方法检出限要包含样品处理的全部步骤[^epa2016mdl-e3]，分至少 3 批测定[^epa2016mdl-e4] | [实验测量研究](../../06_methods/experimental_measurement.md)、上文[检出限](#检出限和测不到的数据) |
| [比较评估](../../05_research-strategies/compare_evaluate.md) | 用生命周期评价比较几种产品或方案的总环境影响[^epa2006lca-e4] | 按同一功能比较[^epa2006lca-e8]；写明假设[^epa2006lca-e9]；判断哪个方案更好涉及主观判断[^epa2006lca-e10] | 上文[生命周期评价](#生命周期评价) |

怎么用这张表 `[本项目分析]`：先按核心主张找到你的套路，再读对应的套路页和做法页。很多课题是混合的，例如开发一种新吸附剂（构建改进），同时为它建一套检测方法（测量）；这时按核心主张定主要套路，其他部分按各自的标准要求。

---

## 给新手的建议

1. **采样之前先写计划。** 按数据质量目标的七步，至少写清问题、研究边界、验收标准[^epa2006dqo-e4]。做计划的通用方法见主线章节[形成研究计划](../../01_from-interest-to-project/04_research-plan.md)。
2. **把采样当作误差的大头。** 多花心思在采几个点、什么时候采，不要只追求测得更准[^epa2006dqo-e7][^epa2006dqo-e9]。
3. **事先定好质量控制。** 对每项测量，写明做哪些检查（空白、平行样、加标等）、多久做一次[^epa2002qapp-e13]。
4. **弄清你用的检出限是怎么来的**[^epa2016mdl-e3]。论文里写清低于报告限的数据有多少、怎样处理；不要随手替换成报告限的一半[^helsel2020statistical-e2]。
5. **从第一个样品起就编号、记录经手人。** 出了问题才能追溯[^epa2002qapp-e6][^epa2002qapp-e7]。
6. **实验室结果要在真实条件下检验。** 例如 ES&T 要求新材料至少在一种环境条件下、用有实际意义的浓度测试过[^estauthorguidelines-e9]。
7. **和水厂、社区合作前，谈好数据怎样用、能不能公开、结果先告诉谁** `[本项目分析]`。ASCE 准则把保护公众健康放在第一位[^asce2020code-e2]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不做空白样 | 无法知道采样和测定中带入了多少污染[^epa2002qapp-e10] |
| 只报告名义浓度 | ES&T 要求报告实测浓度[^estauthorguidelines-e6] |
| 照抄仪器说明书上的检出限 | EPA 的方法检出限要包含样品处理的全部步骤，并分多批测定[^epa2016mdl-e3][^epa2016mdl-e4] |
| 把"未检出"一律替换成报告限的一半，再做 t 检验 | 可能漏掉真实差别，也可能找出不存在的差别[^helsel2020statistical-e2] |
| 样品标签只写"1、2、3"，没有交接记录 | 样品容易弄混；数据要作为证据时，无法说清经手过程[^epa2002qapp-e6][^epa2002qapp-e8] |
| 在社区采样，数据没有代表性就公开下结论 | 据 Roy 和 Edwards 2019 年的记述，弗林特出现过这类数据造成的无根据恐慌[^roy2019citizen-e6] |

---

## 延伸阅读

- **EPA QA/G-4，Guidance on Systematic Planning Using the Data Quality Objectives Process（2006）**：数据质量目标七步的完整说明。做第一个采样项目前读。
- **EPA QA/G-5，Guidance for Quality Assurance Project Plans（2002）**：质量保证项目计划每一项写什么，附录有质量控制样品等术语的解释。
- **EPA，Definition and Procedure for the Determination of the Method Detection Limit, Revision 2（2016）**：篇幅很短，讲清方法检出限怎样测定。
- **Helsel 等，Statistical Methods in Water Resources（USGS，2020）**：美国地质调查局出版的水资源数据统计教材，可免费阅读，含删失数据的处理。分析监测数据前读相关章节。
- **EPA，Life Cycle Assessment: Principles and Practice（2006）**：生命周期评价的入门读物。
- **ES&T 作者指南**：投 ES&T 前读，尤其是 Journal Scope 一节的要求清单。
- **ASCE Code of Ethics**：三页，讲美国土木工程师学会会员对社会、环境、客户和同行等的责任。
- **Roy 和 Edwards 2019**：弗林特事件中社区合作的当事人回顾，适合想做社区合作研究的人；读时注意这是当事团队一方的说法。

[^epa2002qapp-e1]: EPA 2002（QA/G-5），Chapter 1，PDF 第 9 页。[证据](../../../sources/notes/epa2002qapp.md#e1)
[^epa2002qapp-e2]: EPA 2002（QA/G-5），Chapter 1，PDF 第 10 页。[证据](../../../sources/notes/epa2002qapp.md#e2)
[^epa2002qapp-e3]: EPA 2002（QA/G-5），Chapter 1，PDF 第 10 页。[证据](../../../sources/notes/epa2002qapp.md#e3)
[^epa2002qapp-e4]: EPA 2002（QA/G-5），Chapter 1，PDF 第 13 页。[证据](../../../sources/notes/epa2002qapp.md#e4)
[^epa2002qapp-e5]: EPA 2002（QA/G-5），Element A6，PDF 第 25 页。[证据](../../../sources/notes/epa2002qapp.md#e5)
[^epa2002qapp-e6]: EPA 2002（QA/G-5），Element B3，PDF 第 36 页。[证据](../../../sources/notes/epa2002qapp.md#e6)
[^epa2002qapp-e7]: EPA 2002（QA/G-5），Element B3，PDF 第 36 页。[证据](../../../sources/notes/epa2002qapp.md#e7)
[^epa2002qapp-e8]: EPA 2002（QA/G-5），Element B3，PDF 第 36 页。[证据](../../../sources/notes/epa2002qapp.md#e8)
[^epa2002qapp-e9]: EPA 2002（QA/G-5），Element B5，PDF 第 39 页。[证据](../../../sources/notes/epa2002qapp.md#e9)
[^epa2002qapp-e10]: EPA 2002（QA/G-5），Element B5，PDF 第 39 页。[证据](../../../sources/notes/epa2002qapp.md#e10)
[^epa2002qapp-e11]: EPA 2002（QA/G-5），Element B5，PDF 第 39 页。[证据](../../../sources/notes/epa2002qapp.md#e11)
[^epa2002qapp-e12]: EPA 2002（QA/G-5），Element B5，PDF 第 39 页。[证据](../../../sources/notes/epa2002qapp.md#e12)
[^epa2002qapp-e13]: EPA 2002（QA/G-5），Element B5，PDF 第 39 页。[证据](../../../sources/notes/epa2002qapp.md#e13)
[^epa2002qapp-e14]: EPA 2002（QA/G-5），Appendix B 术语表，PDF 第 71 页。[证据](../../../sources/notes/epa2002qapp.md#e14)
[^epa2002qapp-e15]: EPA 2002（QA/G-5），Appendix B 术语表，PDF 第 72 页。[证据](../../../sources/notes/epa2002qapp.md#e15)
[^epa2002qapp-e16]: EPA 2002（QA/G-5），Appendix B 术语表，PDF 第 69 页。[证据](../../../sources/notes/epa2002qapp.md#e16)
[^epa2002qapp-e17]: EPA 2002（QA/G-5），Appendix B 术语表，PDF 第 71 页。[证据](../../../sources/notes/epa2002qapp.md#e17)
[^epa2006dqo-e1]: EPA 2006（QA/G-4），Introduction，PDF 第 11 页。[证据](../../../sources/notes/epa2006dqo.md#e1)
[^epa2006dqo-e2]: EPA 2006（QA/G-4），Introduction，PDF 第 16 页。[证据](../../../sources/notes/epa2006dqo.md#e2)
[^epa2006dqo-e3]: EPA 2006（QA/G-4），Introduction，PDF 第 16 页。[证据](../../../sources/notes/epa2006dqo.md#e3)
[^epa2006dqo-e4]: EPA 2006（QA/G-4），Introduction，Figure 2。[证据](../../../sources/notes/epa2006dqo.md#e4)
[^epa2006dqo-e5]: EPA 2006（QA/G-4），Chapter 1，PDF 第 26 页。[证据](../../../sources/notes/epa2006dqo.md#e5)
[^epa2006dqo-e6]: EPA 2006（QA/G-4），Chapter 4，PDF 第 41 页。[证据](../../../sources/notes/epa2006dqo.md#e6)
[^epa2006dqo-e7]: EPA 2006（QA/G-4），Chapter 6，PDF 第 57 页。[证据](../../../sources/notes/epa2006dqo.md#e7)
[^epa2006dqo-e8]: EPA 2006（QA/G-4），Chapter 6，PDF 第 60 页。[证据](../../../sources/notes/epa2006dqo.md#e8)
[^epa2006dqo-e9]: EPA 2006（QA/G-4），Chapter 7，PDF 第 83 页。[证据](../../../sources/notes/epa2006dqo.md#e9)
[^epa2006dqo-e10]: EPA 2006（QA/G-4），Chapter 3，PDF 第 38 页。[证据](../../../sources/notes/epa2006dqo.md#e10)
[^epa2006dqo-e11]: EPA 2006（QA/G-4），Introduction，PDF 第 12 页。[证据](../../../sources/notes/epa2006dqo.md#e11)
[^epa2016mdl-e1]: EPA 2016（MDL Revision 2），封面说明。[证据](../../../sources/notes/epa2016mdl.md#e1)
[^epa2016mdl-e2]: EPA 2016（MDL Revision 2），Definition。[证据](../../../sources/notes/epa2016mdl.md#e2)
[^epa2016mdl-e3]: EPA 2016（MDL Revision 2），Scope and Application。[证据](../../../sources/notes/epa2016mdl.md#e3)
[^epa2016mdl-e4]: EPA 2016（MDL Revision 2），Procedure (2)(b)。[证据](../../../sources/notes/epa2016mdl.md#e4)
[^epa2016mdl-e5]: EPA 2016（MDL Revision 2），Procedure (2)(b)。[证据](../../../sources/notes/epa2016mdl.md#e5)
[^epa2016mdl-e6]: EPA 2016（MDL Revision 2），Procedure (2)(e)。[证据](../../../sources/notes/epa2016mdl.md#e6)
[^epa2016mdl-e7]: EPA 2016（MDL Revision 2），Procedure (4)(a)。[证据](../../../sources/notes/epa2016mdl.md#e7)
[^helsel2020statistical-e1]: Helsel 等 2020（USGS），§1.1。[证据](../../../sources/notes/helsel2020statistical.md#e1)
[^helsel2020statistical-e2]: Helsel 等 2020（USGS），§5.5。[证据](../../../sources/notes/helsel2020statistical.md#e2)
[^helsel2020statistical-e3]: Helsel 等 2020（USGS），§5.5。[证据](../../../sources/notes/helsel2020statistical.md#e3)
[^helsel2020statistical-e4]: Helsel 等 2020（USGS），§5.3.5。[证据](../../../sources/notes/helsel2020statistical.md#e4)
[^helsel2020statistical-e5]: Helsel 等 2020（USGS），§12.7。[证据](../../../sources/notes/helsel2020statistical.md#e5)
[^helsel2020statistical-e6]: Helsel 等 2020（USGS），§15.3。[证据](../../../sources/notes/helsel2020statistical.md#e6)
[^epa2006lca-e1]: EPA 2006（LCA: Principles and Practice），Chapter 1。[证据](../../../sources/notes/epa2006lca.md#e1)
[^epa2006lca-e2]: EPA 2006（LCA: Principles and Practice），Chapter 1。[证据](../../../sources/notes/epa2006lca.md#e2)
[^epa2006lca-e3]: EPA 2006（LCA: Principles and Practice），Chapter 1。[证据](../../../sources/notes/epa2006lca.md#e3)
[^epa2006lca-e4]: EPA 2006（LCA: Principles and Practice），Chapter 1。[证据](../../../sources/notes/epa2006lca.md#e4)
[^epa2006lca-e5]: EPA 2006（LCA: Principles and Practice），Chapter 1，Limitations。[证据](../../../sources/notes/epa2006lca.md#e5)
[^epa2006lca-e6]: EPA 2006（LCA: Principles and Practice），Chapter 1，Limitations。[证据](../../../sources/notes/epa2006lca.md#e6)
[^epa2006lca-e7]: EPA 2006（LCA: Principles and Practice），Chapter 2。[证据](../../../sources/notes/epa2006lca.md#e7)
[^epa2006lca-e8]: EPA 2006（LCA: Principles and Practice），Chapter 2，功能单位的例子。[证据](../../../sources/notes/epa2006lca.md#e8)
[^epa2006lca-e9]: EPA 2006（LCA: Principles and Practice），Chapter 2。[证据](../../../sources/notes/epa2006lca.md#e9)
[^epa2006lca-e10]: EPA 2006（LCA: Principles and Practice），Chapter 4。[证据](../../../sources/notes/epa2006lca.md#e10)
[^estauthorguidelines-e1]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e1)
[^estauthorguidelines-e2]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e2)
[^estauthorguidelines-e3]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e3)
[^estauthorguidelines-e4]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e4)
[^estauthorguidelines-e5]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e5)
[^estauthorguidelines-e6]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e6)
[^estauthorguidelines-e7]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e7)
[^estauthorguidelines-e8]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e8)
[^estauthorguidelines-e9]: ES&T 作者指南，Journal Scope。[证据](../../../sources/notes/estauthorguidelines.md#e9)
[^estauthorguidelines-e10]: ES&T 作者指南，Article Types。[证据](../../../sources/notes/estauthorguidelines.md#e10)
[^estauthorguidelines-e11]: ES&T 作者指南，Article Types。[证据](../../../sources/notes/estauthorguidelines.md#e11)
[^estauthorguidelines-e12]: ES&T 作者指南，Cover Letter。[证据](../../../sources/notes/estauthorguidelines.md#e12)
[^estauthorguidelines-e14]: ES&T 作者指南，Research Data Policy。[证据](../../../sources/notes/estauthorguidelines.md#e14)
[^estauthorguidelines-e15]: ES&T 作者指南，Research Data Policy，Computer Codes。[证据](../../../sources/notes/estauthorguidelines.md#e15)
[^estauthorguidelines-e16]: ES&T 作者指南，Prior Publication Policy。[证据](../../../sources/notes/estauthorguidelines.md#e16)
[^estauthorguidelines-e17]: ES&T 作者指南，Theses/Dissertations。[证据](../../../sources/notes/estauthorguidelines.md#e17)
[^estauthorguidelines-e18]: ES&T 作者指南，Ethical Use of Animals or Human Participants in Research。[证据](../../../sources/notes/estauthorguidelines.md#e18)
[^asce2020code-e1]: ASCE 伦理准则，Preamble。[证据](../../../sources/notes/asce2020code.md#e1)
[^asce2020code-e2]: ASCE 伦理准则，1a。[证据](../../../sources/notes/asce2020code.md#e2)
[^asce2020code-e3]: ASCE 伦理准则，1c。[证据](../../../sources/notes/asce2020code.md#e3)
[^asce2020code-e4]: ASCE 伦理准则，1g。[证据](../../../sources/notes/asce2020code.md#e4)
[^asce2020code-e6]: ASCE 伦理准则，4b。[证据](../../../sources/notes/asce2020code.md#e6)
[^asce2020code-e7]: ASCE 伦理准则，4e。[证据](../../../sources/notes/asce2020code.md#e7)
[^asce2020code-e8]: ASCE 伦理准则，4f。[证据](../../../sources/notes/asce2020code.md#e8)
[^asce2020code-e10]: ASCE 官网 Code of Ethics 介绍页。[证据](../../../sources/notes/asce2020code.md#e10)
[^epa2024environmentaljustice-e1]: EPA 环境正义网页（2024 年快照），定义段。[证据](../../../sources/notes/epa2024environmentaljustice.md#e1)
[^epa2024environmentaljustice-e2]: EPA 环境正义网页（2024 年快照），定义段。[证据](../../../sources/notes/epa2024environmentaljustice.md#e2)
[^roy2019citizen-e1]: Roy & Edwards 2019，Introduction。[证据](../../../sources/notes/roy2019citizen.md#e1)
[^roy2019citizen-e2]: Roy & Edwards 2019，Uncovering the Flint Water Crisis through Citizen Science。[证据](../../../sources/notes/roy2019citizen.md#e2)
[^roy2019citizen-e3]: Roy & Edwards 2019，Uncovering the Flint Water Crisis through Citizen Science。[证据](../../../sources/notes/roy2019citizen.md#e3)
[^roy2019citizen-e4]: Roy & Edwards 2019，Characteristics of quality citizen science projects。[证据](../../../sources/notes/roy2019citizen.md#e4)
[^roy2019citizen-e5]: Roy & Edwards 2019，Persistent attacks on merited expertise。[证据](../../../sources/notes/roy2019citizen.md#e5)
[^roy2019citizen-e6]: Roy & Edwards 2019，Abstract。[证据](../../../sources/notes/roy2019citizen.md#e6)
