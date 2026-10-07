# 健康科学：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲健康科学（公共卫生、流行病学、卫生服务研究、营养学、护理学、体育科学、环境与职业健康等）的研究实际怎样运转。它和临床医学共用很多规则：《赫尔辛基宣言》、国际医学期刊编辑委员会（ICMJE）的建议、试验登记、CONSORT 和 STROBE 等报告规范、证据金字塔。这些[临床医学篇](../clinical-medicine/README.md)已经讲过，本文默认你读过，只给链接。各学科共通的做法见[全程地图](../../00_start-here/research-journey.md)里的主线各章和[贯穿全程](../../08_throughout/README.md)。

本文只写健康科学更突出的几件事：研究对象常常是**人群**；很多问题要靠观察性数据回答；不少研究用的是本来不为研究而收集的数据；质性研究有自己的质量标准；伦理除了个人，还要考虑群体和社区。本文资料以流行病学和公共卫生为主。护理学、体育科学等方向的专门规范，本文资料未涉及，以导师或目标期刊要求为准。`[本项目分析]`

**读完本文，你应该能：**

- 说清观察性研究为什么容易被混杂、测量误差和选择偏倚带偏；
- 动手分析前，先说清自己要回答"关联"问题还是"因果"问题；
- 用登记、医保、电子病历这类现成数据做研究时，知道要报告什么；
- 知道人群研究在伦理上还要考虑群体和社区。

---

## 本领域研究怎样运转

### 研究对象常常是人群

公共卫生和流行病学关心的往往是一群人的健康：某种饮食、某项政策、某种环境暴露对人群有什么影响 `[本项目分析]`。例如，Cochrane 系统综述研究的干预，既有临床的，也有公共卫生和政策层面的[^higgins2024cochrane-e11]。伦理准则也反映了这一点：国际医学科学组织理事会（Council for International Organizations of Medical Sciences，CIOMS）是一个国际组织，它 2016 年发布的国际伦理准则把适用范围从"生物医学研究"扩大到"健康相关研究"[^cioms2016ethical-e1]，并把原来分开的生物医学研究准则和流行病学研究准则合成一份[^cioms2016ethical-e3]。

### 很多问题要靠观察性数据回答

随机试验回答不了所有问题，这一点临床医学篇[已经讲过](../clinical-medicine/README.md#常见的研究类型)。Cochrane 手册也说，干预的危害这类证据，常常要来自非随机研究[^higgins2024cochrane-e8]。

有些问题，做试验根本不合伦理。Hernán 举的例子：想知道每天喝一杯葡萄酒对慢性病的长期影响，让人按分组长期喝酒的试验不合伦理，所以观察性分析成了估计这种长期效应的最好机会[^hernan2018cword-e11]。所以新手要先学会识别[观察性研究的三个坑](#观察性研究的三个坑) `[本项目分析]`。

### 很多研究用的是"现成的"数据

**常规收集的健康数据**，指收集时没有事先定好研究问题、后来才拿来做研究的数据[^benchimol2015record-e1]。例如疾病登记、基层医疗数据库、卫生行政数据（比如医保结算记录）、电子病历库、癌症登记和公共卫生报告数据[^benchimol2015record-e2]。用大人群数据库，能研究罕见病；但把人分错类的风险也会被放大[^benchimol2015record-e15]。怎样用好这类数据，见下文[用常规收集的数据](#用常规收集的数据写清编码链接和数据的来历)。

### 发表、预印本和登记

健康科学以期刊发表为主 `[本项目分析]`；ICMJE 建议、署名、利益冲突、数据共享声明见[临床医学篇](../clinical-medicine/README.md#本领域的规范和报告标准)。**预印本**可以发在医学和健康科学的免费预印本平台 medRxiv[^medrxivabout-e1]，发之前要知道三点：

- 它不收病例报告、叙述性综述、范围综述、不含荟萃分析的系统综述等[^medrxivabout-e3]。
- 预印本没有经过同行评审。平台自己说，它不应用来指导临床实践或健康行为，媒体也不应把它当定论报道[^medrxivabout-e2]。
- 发布后不能撤下[^medrxivabout-e4]。先查目标期刊对预印本的政策（见[临床医学篇](../clinical-medicine/README.md#发表以期刊为主规则相对统一)）。

**登记**：观察性研究等非试验设计，ICMJE 鼓励登记但不强制[^icmje2026recommendations-e21]。但公共卫生的干预研究可能算"临床试验"：ICMJE 所说的干预，包括行为治疗、教育项目、饮食干预、质量改进和诊疗流程改变[^icmje2026recommendations-e17]。临床试验什么时候、在哪里登记，见[临床医学篇](../clinical-medicine/README.md#先登记再招募第一位病人)。

---

## 和其他领域不同的地方

下表健康科学一列依据所附脚注；临床医学和计算机两列是本项目对那两篇的概括，细节以原篇为准 `[本项目分析]`：

| | 健康科学 | 临床医学 | 计算机 |
|---|---|---|---|
| 典型研究对象 | 人群、社区、卫生系统 `[本项目分析]` | 病人 | 系统、算法、数据 |
| 证据来源 | 干预危害等问题常要靠非随机研究[^higgins2024cochrane-e8]；常用现成数据[^benchimol2015record-e1] | 试验和观察性研究 | 实验和基准测试 |
| 主要的方法风险 | 混杂、测量误差、错误分类[^vandenbroucke2007strobe-e6] | 偏倚、选择性报告 | 不公平的比较、数据泄漏 |
| 伦理关注 | 个人，加上群体和社区[^cioms2016ethical-e6] | 个人（受试者） | 涉及人时才审 |
| 报告规范 | STROBE 加 RECORD[^benchimol2015record-e3]、COREQ 等[^equatorcoreq-e3] | CONSORT、STROBE 等 | 按会议要求 |

---

## 观察性研究的三个坑

### 坑一：混杂——"有关联"不等于"有作用"

混杂和偏倚的定义见[临床医学篇](../clinical-medicine/README.md#常见的研究类型)。简单说，**混杂**是关联本身是真的，但背后有一个没考虑到的因素同时影响暴露和结局，所以不能解释为因果[^vandenbroucke2007strobe-e5]。Hernán 的例子：假设数据显示，每天喝一杯葡萄酒的人，心脏病风险是不喝的人的 0.8 倍（风险比 0.8）。这**不等于**每天喝一杯能让风险降低 20%[^hernan2018cword-e3]。可能是这类人本来收入更高，吃得起有营养的食物，有时间锻炼，也更容易得到预防保健，所以即使不喝酒，风险也更低[^hernan2018cword-e4]。

### 坑二：暴露测不准，尤其是饮食

饮食、身体活动这类暴露，常常要靠问卷或回忆来测，很难测准 `[本项目分析]`。STROBE 的解释文章说：暴露或结局测量不准、分类错误，可能让真实的因果关系更难发现，也可能制造虚假的关系；混杂因素测不准，会留下"残余混杂"（调整之后仍没消除的混杂）[^vandenbroucke2007strobe-e6]。暴露测得越不准，估计出的效应往往越被拉向"没有关联"[^vandenbroucke2007strobe-e7]。饮食研究还有一个难处：吃什么和很多别的生活方式连在一起。这篇解释文章举例说，"每周吃 2 到 4 个鸡蛋与卵巢癌风险加倍有关"这个结果不能直接相信，因为饮食习惯与大量生活方式因素和社会经济地位相关[^vandenbroucke2007strobe-e8]。

**怎么办**：报告测量方法时，不要只引用一篇验证研究，要给出测量的效度或信度估计值，便于别人做测量误差校正或敏感性分析[^vandenbroucke2007strobe-e10]。

### 坑三：谁参加了研究，本身就可能制造关联

STROBE 的解释文章举过一个例子：一些病例对照研究发现"母亲年轻"与孩子患白血病有关联，后来发现，是因为孩子健康的年轻母亲更不愿意参加研究[^vandenbroucke2007strobe-e11]。参与率低不一定让研究无效，但要如实报告参与情况和不参与的原因[^vandenbroucke2007strobe-e13]。

### 动手前先说清：你要回答关联问题还是因果问题

Hernán 2018 年在《美国公共卫生杂志》（American Journal of Public Health）发表了一篇评论，代表他个人的观点。他认为，不论研究是否随机，因果推断都是科学的核心任务[^hernan2018cword-e2]。他提出的做法是：

1. **把因果问题写成一个"目标试验"。** 用观察性数据做因果分析，可以看作在模拟一个假想的试验[^hernan2018cword-e5]。写出这个试验，会逼你想清楚：关心的干预到底是什么，在哪个时间段发生。例如"55 岁起每天喝一杯、喝 10 年"和"30 岁起喝 20 年"，是两个不同的目标试验，回答不同的因果问题[^hernan2018cword-e6]。
2. **目标决定要不要调整混杂。** 目标是因果，一般要调整混杂；目标纯粹是描述关联，就不需要[^hernan2018cword-e7]。
3. **不要让软件替你挑混杂因素。** 自动筛选变量的方法可能适合预测，但不一定适合因果推断[^hernan2018cword-e8]。STROBE 的解释文章也不建议只凭统计显著性检验挑混杂因素[^vandenbroucke2007strobe-e9]。
4. **结果部分只呈现，不解释。** 他认为论文里唯一不该写"因果效应"的地方是结果部分[^hernan2018cword-e9]。

还有一个相关的区分。Cochrane 手册举例：营养学家关心"每天至少吃五份果蔬"这种饮食本身对健康的影响，这是**病因问题**；公共卫生人员关心"推动人们这样吃"的干预有什么效果，这是**效果问题**[^higgins2024cochrane-e9]。写研究问题时要分清自己问的是哪一种 `[本项目分析]`。

> **不同的看法：观察性研究的论文里能不能写"因果"？**
> - **谨慎派**：Hernán 提到，很多期刊编辑要求作者避免因果语言[^hernan2018cword-e1]。STROBE 清单也要求结合局限、分析次数、类似研究等，对结果做谨慎的整体解释[^vandenbroucke2007strobe-e12]。
> - **Hernán 的看法**：回避"因果"一词有害，因为因果推断本来就是科学的核心任务[^hernan2018cword-e2]。但他也承认，没法保证模型纳入了所有混杂因素，所以估计值不一定能解释为因果[^hernan2018cword-e10]。同一期刊同期登了多篇对这篇评论的回应[^hernan2018cword-e12]，本文资料没有读这些回应。
>
> 实际操作：措辞先按目标期刊的要求；但不管用什么词，方法部分都要说清你想估计的是哪个因果问题、调整了什么、还剩哪些混杂没法排除。`[本项目分析]`

---

## 本领域的规范和报告标准

### 报告规范：在临床医学篇的基础上再加几份

报告规范是什么、怎样在 EQUATOR 网络上找，见[临床医学篇](../clinical-medicine/README.md#报告规范按研究类型选清单)。健康科学还常用下面几份。除 RECORD 外，本文只读了 EQUATOR 网站的 COREQ 条目页，没有读这些规范的原文；用之前请读原文 `[本项目分析]`。

| 研究类型 | 报告规范 | 说明 |
|---|---|---|
| 用常规收集数据的观察性研究 | RECORD | STROBE 的扩展，13 项[^benchimol2015record-e3]；只管怎么报告，不规定研究怎么做[^benchimol2015record-e14] |
| 质性研究 | COREQ、SRQR | EQUATOR 把两者列为质性研究的主要报告规范[^equatorcoreq-e3]；COREQ 是针对访谈和焦点小组的 32 项清单[^equatorcoreq-e1]，原文是 Tong、Sainsbury 和 Craig 2007 年的论文[^equatorcoreq-e2] |
| 质量改进研究 | SQUIRE | EQUATOR 列出的主要报告规范[^equatorcoreq-e4] |
| 经济学评价 | CHEERS | EQUATOR 列出的主要报告规范[^equatorcoreq-e5] |

### 用常规收集的数据：写清编码、链接和数据的来历

RECORD 的作者指出，这类研究常见的报告缺陷是：暴露和结局怎样编码没写清，不同数据源的链接率没写[^benchimol2015record-e4]。按 RECORD，要写清这几件事：

- **数据从哪来、当初为什么收集**，让读者了解数据库的内容和有效性[^benchimol2015record-e13]。
- **全部编码和算法**：用来界定暴露、结局、混杂因素和效应修饰因素的，要完整列出[^benchimol2015record-e5]；用来选研究人群的编码或算法，有验证研究的要引用[^benchimol2015record-e6]。
- **数据怎样链接**：链接了两个以上数据库，要说明在什么层面链接、用什么方法、怎样评估链接质量[^benchimol2015record-e11]。
- **假设是分析前还是分析后提出的**[^benchimol2015record-e7]。这就是主线章节[从研究问题到证据清单](../../02_from-project-to-study/01_question-to-evidence.md#5-分清你是在检验还是在探索)讲的探索性和验证性研究之分 `[本项目分析]`。
- **怎样获取研究方案、原始数据或代码**[^benchimol2015record-e12]。
- **局限**：数据本来不是为你的问题收集的，要讨论错误分类偏倚、未测量的混杂、缺失数据、纳入资格随时间变化等影响[^benchimol2015record-e8]。

两个容易忽视的陷阱：行政数据容易"往高编码"，例如报销按病例复杂程度算时，医院可能多用更复杂的疾病编码[^benchimol2015record-e9]；编码方式变了，数据前后也可能不一致[^benchimol2015record-e10]。所以看到某个病的"发病率"某一年突然变化，先查是不是编码规则变了 `[本项目分析]`。

### 质性健康研究：讲清你是谁、怎样分析

Mays 和 Pope 2000 年在《英国医学杂志》（BMJ）上写道，当时质性方法在健康研究中已广泛使用，但很多卫生服务研究者不清楚怎样判断它的质量[^mays2000assessing-e1]。质性研究该不该用和量化研究一样的标准评价，一直有很大争论[^mays2000assessing-e2]：一派认为质性研究是独特的范式，不应该用效度、信度这些传统标准评判[^mays2000assessing-e3]；Mays 和 Pope 认为可以用"效度"和"相关性"这两个概念，但具体做法要按质性研究的目标调整[^mays2000assessing-e4]。他们说，没有机械的办法能保证质性研究不出错[^mays2000assessing-e10]，但可以这样提高可信度：

- **三角互证**：比较不同数据收集方法（如访谈和观察）或不同数据来源的结果[^mays2000assessing-e5]。
- **反身性**：意识到研究者本人怎样影响了数据[^mays2000assessing-e6]。访谈者的年龄、性别、职业身份（医生、护士等）都会影响数据，要讨论[^mays2000assessing-e7]。
- **找反例**：主动寻找并讨论与你的解释相矛盾的数据[^mays2000assessing-e8]。
- **给足原始资料**，让读者能判断你的解释有没有数据支撑[^mays2000assessing-e11]。
- **请受访者核对**，但它只是减少错误的一个环节，不是最终检验[^mays2000assessing-e9]。
- 访谈怎样设计和编码，方法与研究方法里的[访谈研究](../../06_methods/interview_study.md)相通 `[本项目分析]`。

### 伦理：除了保护个人，还要考虑群体和社区

个人层面的伦理（伦理审查、知情同意）见[临床医学篇](../clinical-medicine/README.md#研究对象是人伦理排在第一位)和贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)。CIOMS 2016 年的准则是国际组织的指南，不是各国法规；具体怎么做，以所在国家和机构的规定为准 `[本项目分析]`。它讲了几件在人群研究里更突出的事：

- **研究要有价值，但价值不能成为亏待人的理由。** 开展涉人健康研究的伦理理由，是它的科学价值和社会价值[^cioms2016ethical-e4]；但价值再大，也不能成为亏待参与者或所在社区的理由[^cioms2016ethical-e5]。
- **结果可能伤害整个群体。** 流行病学、遗传学、社会学的研究结果，可能损害社区、家庭或某个种族、民族群体的利益[^cioms2016ethical-e6]，让一个群体被污名化或遭受歧视[^cioms2016ethical-e7]。发表"某群体某病患病率高"这类结果时，要想到这一点 `[本项目分析]`。
- **让社区及早、持续地参与。** 准则说，要让潜在参与者和社区参与研究的设计、实施、知情同意流程设计、监督和结果传播[^cioms2016ethical-e8]。这能保证研究对社区有意义，也让社区接受这项研究[^cioms2016ethical-e9]。例如社区领袖全是男性时，要主动听取女性的意见[^cioms2016ethical-e10]。交给伦理委员会的材料里，要写社区参与计划[^cioms2016ethical-e11]。
- **用现成数据也有伦理要求。** 用日常诊疗中收集的数据，必须提供知情退出的途径[^cioms2016ethical-e12]。伦理委员会免除个人知情同意，要同时满足三个条件：不免除就做不了；研究有重要的社会价值；风险不超过最低风险[^cioms2016ethical-e13]。数据保管方只能向研究者提供匿名化或编码后的数据[^cioms2016ethical-e14]。在资源匮乏地区收集和保存数据，要与当地卫生部门合作[^cioms2016ethical-e15]。
- **整群随机试验要单独考虑同意问题。** 这类试验随机分配的是社区、医院或科室[^cioms2016ethical-e16]，开始前要判断：要求每个人知情同意、允许拒绝，会不会破坏研究结果[^cioms2016ethical-e17]。
- **拿不准就问。** CIOMS 也承认，社会科学研究、行为研究、公共卫生监测的伦理，和其他研究的伦理之间没有清楚的界线[^cioms2016ethical-e18]。拿不准自己的项目要不要审、怎么审，问所在机构的伦理委员会 `[本项目分析]`。

### 系统综述：Cochrane 手册

Cochrane 手册（Cochrane Handbook for Systematic Reviews of Interventions）讲干预效果的系统综述，具体讲 Cochrane 用的方法[^higgins2024cochrane-e12]。报告按 PRISMA（见[临床医学篇](../clinical-medicine/README.md#报告规范按研究类型选清单)），一般做法见研究方法里的[综述研究](../../06_methods/review_study.md)。本文只读了手册的第 1 章（引言）和第 24 章（纳入非随机研究），其中几点值得新手记住：

- 研究问题和方法事先写进方案，以减少偏倚[^higgins2024cochrane-e1]。问干预效果，一般用 PICO 框架：人群（Population）、干预（Intervention）、对照（Comparison）、结局（Outcome）[^higgins2024cochrane-e5]。
- 开始新的原始研究之前，一般应先做系统综述[^higgins2024cochrane-e3]。
- 团队要既懂专业又懂方法，并且没有潜在利益冲突[^higgins2024cochrane-e6]；会做决策或受决策影响的人，应参与综述的重要决定[^higgins2024cochrane-e2]。
- 纳入非随机研究时，解释结果要始终谨慎[^higgins2024cochrane-e7]；判断这类研究，要看具体设计特征（比如哪些部分是前瞻设计的），不要只看"队列""病例对照"这类标签[^higgins2024cochrane-e10]。
- 高质量的系统综述往往费力又费时[^higgins2024cochrane-e4]，别把它当成轻松的入门项目 `[本项目分析]`。

---

## 常见的研究类型

**本领域的研究类型文档**：[系统综述与元分析（健康领域）](research-types/meta_analysis.md)、[观察性流行病学研究](research-types/observational_epidemiology.md)。

**相关学科的研究类型文档**：[随机对照试验](../clinical-medicine/research-types/randomized_controlled_trial.md)、[准实验与因果识别](../economics/research-types/quasi_experiment.md)。

队列、病例对照、横断面研究，以及系统综述，见[临床医学篇](../clinical-medicine/README.md#常见的研究类型)。健康科学里还常见：

| 类型 | 一句话说明 |
|---|---|
| 用常规收集数据的研究 | 用登记、行政数据、电子病历等现成数据[^benchimol2015record-e2]，按 RECORD 报告。思路和计算机篇的[仓库挖掘研究](../computer-science/practices/repository_mining.md)相通，但健康数据涉及隐私和伦理审批 `[本项目分析]` |
| 整群随机试验 | 随机分配社区、医院或科室，而不是个人[^cioms2016ethical-e16] |
| 质性研究（访谈、焦点小组） | 了解人们的经历和看法 `[本项目分析]`；按 COREQ 或 SRQR 报告[^equatorcoreq-e3] |
| 质量改进研究 | 研究怎样改进医疗服务 `[本项目分析]`；按 SQUIRE 报告[^equatorcoreq-e4] |
| 经济学评价 | 比较干预的成本和效果 `[本项目分析]`；按 CHEERS 报告[^equatorcoreq-e5] |

---

## 给新手的建议

1. **先写一句话说清：你要回答关联问题还是因果问题。** 如果是因果问题，试着写出对应的"目标试验"[^hernan2018cword-e6]。
2. **用现成数据前，先搞清它当初为什么收集**[^benchimol2015record-e13]，**编码规则改过没有**[^benchimol2015record-e10]。
3. **把全部编码、算法和代码整理好**，RECORD 要求列出完整编码并说明怎样获取代码[^benchimol2015record-e5][^benchimol2015record-e12]。
4. **做人群研究，早点找社区谈**，社区参与计划要写进交给伦理委员会的材料[^cioms2016ethical-e11]。
5. **做公共卫生干预研究，先查要不要登记。** 教育、饮食、行为干预都可能算临床试验[^icmje2026recommendations-e17]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 把"喝酒的人心脏病少"写成"喝酒能预防心脏病" | 关联可能来自收入、生活方式等混杂[^hernan2018cword-e4] |
| 只引用一篇验证研究，就说"问卷是有效的" | 应给出效度或信度的估计值[^vandenbroucke2007strobe-e10] |
| 把医保或行政数据里的诊断编码当成真实诊断 | 有"往高编码"和编码规则变化的问题[^benchimol2015record-e9][^benchimol2015record-e10] |
| 发表某个群体"患病率高"的结果，没考虑污名化 | 研究结果可能伤害整个群体[^cioms2016ethical-e7] |
| 以为现成的诊疗数据可以随便拿来用 | CIOMS 要求提供知情退出途径，免除同意要由伦理委员会按条件决定[^cioms2016ethical-e12][^cioms2016ethical-e13] |
| 把病因问题和干预效果问题混为一谈 | "吃五份果蔬的效果"和"推动人们这样吃的效果"是两个问题[^higgins2024cochrane-e9] |

---

## 延伸阅读

- **STROBE 解释文章（Vandenbroucke 等人 2007）**：逐条讲观察性研究怎样报告，例子多，顺带讲清偏倚、混杂、测量误差。做观察性研究时读。
- **RECORD（Benchimol 等人 2015）**：用登记、医保、电子病历数据做研究前读，按清单检查要报告的东西。
- **Hernán 2018，The C-Word**：短评论，讲为什么要先说清因果问题，以及"目标试验"的思路。这是一方观点，同期有多篇回应，可以对照着读。
- **CIOMS 2016 国际伦理准则**：人群研究、社区参与、数据使用、整群随机试验的伦理。可以先读准则 1、4、7、12、21。
- **Cochrane 手册**：做干预效果的系统综述时读。先读第 1 章；纳入非随机研究时读第 24 章。
- **Mays & Pope 2000，Assessing quality in qualitative research**：三页短文，讲怎样判断质性健康研究的质量。

[^cioms2016ethical-e1]: CIOMS 2016，Preface（Scope of the 2016 version）。[证据](../../../sources/notes/cioms2016ethical.md#e1)
[^cioms2016ethical-e3]: CIOMS 2016，Preface。[证据](../../../sources/notes/cioms2016ethical.md#e3)
[^cioms2016ethical-e4]: CIOMS 2016，Guideline 1。[证据](../../../sources/notes/cioms2016ethical.md#e4)
[^cioms2016ethical-e5]: CIOMS 2016，Guideline 1。[证据](../../../sources/notes/cioms2016ethical.md#e5)
[^cioms2016ethical-e6]: CIOMS 2016，Guideline 4 评注（Risks to groups）。[证据](../../../sources/notes/cioms2016ethical.md#e6)
[^cioms2016ethical-e7]: CIOMS 2016，Guideline 4 评注（Risks to groups）。[证据](../../../sources/notes/cioms2016ethical.md#e7)
[^cioms2016ethical-e8]: CIOMS 2016，Guideline 7。[证据](../../../sources/notes/cioms2016ethical.md#e8)
[^cioms2016ethical-e9]: CIOMS 2016，Guideline 7 评注。[证据](../../../sources/notes/cioms2016ethical.md#e9)
[^cioms2016ethical-e10]: CIOMS 2016，Guideline 7 评注。[证据](../../../sources/notes/cioms2016ethical.md#e10)
[^cioms2016ethical-e11]: CIOMS 2016，Guideline 7 评注。[证据](../../../sources/notes/cioms2016ethical.md#e11)
[^cioms2016ethical-e12]: CIOMS 2016，Guideline 12。[证据](../../../sources/notes/cioms2016ethical.md#e12)
[^cioms2016ethical-e13]: CIOMS 2016，Guideline 12。[证据](../../../sources/notes/cioms2016ethical.md#e13)
[^cioms2016ethical-e14]: CIOMS 2016，Guideline 12。[证据](../../../sources/notes/cioms2016ethical.md#e14)
[^cioms2016ethical-e15]: CIOMS 2016，Guideline 12。[证据](../../../sources/notes/cioms2016ethical.md#e15)
[^cioms2016ethical-e16]: CIOMS 2016，Guideline 21 评注。[证据](../../../sources/notes/cioms2016ethical.md#e16)
[^cioms2016ethical-e17]: CIOMS 2016，Guideline 21。[证据](../../../sources/notes/cioms2016ethical.md#e17)
[^cioms2016ethical-e18]: CIOMS 2016，Preface（Scope of the 2016 version）。[证据](../../../sources/notes/cioms2016ethical.md#e18)
[^higgins2024cochrane-e1]: Cochrane 手册 6.5 版，第 1 章 Key Points。[证据](../../../sources/notes/higgins2024cochrane.md#e1)
[^higgins2024cochrane-e2]: Cochrane 手册，第 1 章 Key Points。[证据](../../../sources/notes/higgins2024cochrane.md#e2)
[^higgins2024cochrane-e3]: Cochrane 手册，§1.1。[证据](../../../sources/notes/higgins2024cochrane.md#e3)
[^higgins2024cochrane-e4]: Cochrane 手册，§1.1。[证据](../../../sources/notes/higgins2024cochrane.md#e4)
[^higgins2024cochrane-e5]: Cochrane 手册，§1.2。[证据](../../../sources/notes/higgins2024cochrane.md#e5)
[^higgins2024cochrane-e6]: Cochrane 手册，第 1 章 Key Points。[证据](../../../sources/notes/higgins2024cochrane.md#e6)
[^higgins2024cochrane-e7]: Cochrane 手册，第 24 章 Key Points。[证据](../../../sources/notes/higgins2024cochrane.md#e7)
[^higgins2024cochrane-e8]: Cochrane 手册，§24.1。[证据](../../../sources/notes/higgins2024cochrane.md#e8)
[^higgins2024cochrane-e9]: Cochrane 手册，§24.1。[证据](../../../sources/notes/higgins2024cochrane.md#e9)
[^higgins2024cochrane-e10]: Cochrane 手册，第 24 章 Key Points。[证据](../../../sources/notes/higgins2024cochrane.md#e10)
[^higgins2024cochrane-e11]: Cochrane 手册，§1.1。[证据](../../../sources/notes/higgins2024cochrane.md#e11)
[^higgins2024cochrane-e12]: Cochrane 手册，§1.1。[证据](../../../sources/notes/higgins2024cochrane.md#e12)
[^vandenbroucke2007strobe-e5]: Vandenbroucke 等人 2007（STROBE 解释文章），Box 3。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e5)
[^vandenbroucke2007strobe-e6]: Vandenbroucke 等人 2007，Item 8 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e6)
[^vandenbroucke2007strobe-e7]: Vandenbroucke 等人 2007，Item 19 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e7)
[^vandenbroucke2007strobe-e8]: Vandenbroucke 等人 2007，Item 20 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e8)
[^vandenbroucke2007strobe-e9]: Vandenbroucke 等人 2007，Item 16 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e9)
[^vandenbroucke2007strobe-e10]: Vandenbroucke 等人 2007，Item 8 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e10)
[^vandenbroucke2007strobe-e11]: Vandenbroucke 等人 2007，Item 13 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e11)
[^vandenbroucke2007strobe-e12]: Vandenbroucke 等人 2007，STROBE 清单 Item 20。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e12)
[^vandenbroucke2007strobe-e13]: Vandenbroucke 等人 2007，Item 13 说明。[证据](../../../sources/notes/vandenbroucke2007strobe.md#e13)
[^hernan2018cword-e1]: Hernán 2018，正文开头。[证据](../../../sources/notes/hernan2018cword.md#e1)
[^hernan2018cword-e2]: Hernán 2018，正文开头。[证据](../../../sources/notes/hernan2018cword.md#e2)
[^hernan2018cword-e3]: Hernán 2018，Of course "association is not causation"。[证据](../../../sources/notes/hernan2018cword.md#e3)
[^hernan2018cword-e4]: Hernán 2018，Of course "association is not causation"。[证据](../../../sources/notes/hernan2018cword.md#e4)
[^hernan2018cword-e5]: Hernán 2018，Better causal questions。[证据](../../../sources/notes/hernan2018cword.md#e5)
[^hernan2018cword-e6]: Hernán 2018，Better causal questions。[证据](../../../sources/notes/hernan2018cword.md#e6)
[^hernan2018cword-e7]: Hernán 2018，Better confounding adjustment。[证据](../../../sources/notes/hernan2018cword.md#e7)
[^hernan2018cword-e8]: Hernán 2018，Better confounding adjustment。[证据](../../../sources/notes/hernan2018cword.md#e8)
[^hernan2018cword-e9]: Hernán 2018，Conflating the means and the ends。[证据](../../../sources/notes/hernan2018cword.md#e9)
[^hernan2018cword-e10]: Hernán 2018，Better confounding adjustment。[证据](../../../sources/notes/hernan2018cword.md#e10)
[^hernan2018cword-e11]: Hernán 2018，Conflating the means and the ends。[证据](../../../sources/notes/hernan2018cword.md#e11)
[^hernan2018cword-e12]: Hernán 2018，脚注。[证据](../../../sources/notes/hernan2018cword.md#e12)
[^benchimol2015record-e1]: Benchimol 等人 2015（RECORD），Introduction。[证据](../../../sources/notes/benchimol2015record.md#e1)
[^benchimol2015record-e2]: Benchimol 等人 2015，Introduction。[证据](../../../sources/notes/benchimol2015record.md#e2)
[^benchimol2015record-e3]: Benchimol 等人 2015，Abstract。[证据](../../../sources/notes/benchimol2015record.md#e3)
[^benchimol2015record-e4]: Benchimol 等人 2015，Introduction。[证据](../../../sources/notes/benchimol2015record.md#e4)
[^benchimol2015record-e5]: Benchimol 等人 2015，RECORD item 7.1。[证据](../../../sources/notes/benchimol2015record.md#e5)
[^benchimol2015record-e6]: Benchimol 等人 2015，RECORD item 6.2。[证据](../../../sources/notes/benchimol2015record.md#e6)
[^benchimol2015record-e7]: Benchimol 等人 2015，Introduction 部分的说明。[证据](../../../sources/notes/benchimol2015record.md#e7)
[^benchimol2015record-e8]: Benchimol 等人 2015，RECORD item 19.1。[证据](../../../sources/notes/benchimol2015record.md#e8)
[^benchimol2015record-e9]: Benchimol 等人 2015，Discussion (Limitations) 部分的说明。[证据](../../../sources/notes/benchimol2015record.md#e9)
[^benchimol2015record-e10]: Benchimol 等人 2015，Discussion (Limitations) 部分的说明。[证据](../../../sources/notes/benchimol2015record.md#e10)
[^benchimol2015record-e11]: Benchimol 等人 2015，RECORD item 12.3。[证据](../../../sources/notes/benchimol2015record.md#e11)
[^benchimol2015record-e12]: Benchimol 等人 2015，RECORD item 22.1。[证据](../../../sources/notes/benchimol2015record.md#e12)
[^benchimol2015record-e13]: Benchimol 等人 2015，Methods (Setting) 部分的说明。[证据](../../../sources/notes/benchimol2015record.md#e13)
[^benchimol2015record-e14]: Benchimol 等人 2015，Introduction。[证据](../../../sources/notes/benchimol2015record.md#e14)
[^benchimol2015record-e15]: Benchimol 等人 2015，Methods (Participants) 部分的说明。[证据](../../../sources/notes/benchimol2015record.md#e15)
[^mays2000assessing-e1]: Mays & Pope 2000，Summary points。[证据](../../../sources/notes/mays2000assessing.md#e1)
[^mays2000assessing-e2]: Mays & Pope 2000，Two opposing views。[证据](../../../sources/notes/mays2000assessing.md#e2)
[^mays2000assessing-e3]: Mays & Pope 2000，the antirealist position。[证据](../../../sources/notes/mays2000assessing.md#e3)
[^mays2000assessing-e4]: Mays & Pope 2000，Summary points。[证据](../../../sources/notes/mays2000assessing.md#e4)
[^mays2000assessing-e5]: Mays & Pope 2000，Triangulation。[证据](../../../sources/notes/mays2000assessing.md#e5)
[^mays2000assessing-e6]: Mays & Pope 2000，Reflexivity。[证据](../../../sources/notes/mays2000assessing.md#e6)
[^mays2000assessing-e7]: Mays & Pope 2000，Reflexivity。[证据](../../../sources/notes/mays2000assessing.md#e7)
[^mays2000assessing-e8]: Mays & Pope 2000，Attention to negative cases。[证据](../../../sources/notes/mays2000assessing.md#e8)
[^mays2000assessing-e9]: Mays & Pope 2000，Respondent validation。[证据](../../../sources/notes/mays2000assessing.md#e9)
[^mays2000assessing-e10]: Mays & Pope 2000，Assessing the validity of qualitative research。[证据](../../../sources/notes/mays2000assessing.md#e10)
[^mays2000assessing-e11]: Mays & Pope 2000，Clear exposition of methods。[证据](../../../sources/notes/mays2000assessing.md#e11)
[^equatorcoreq-e1]: EQUATOR Network，COREQ 条目页。[证据](../../../sources/notes/equatorcoreq.md#e1)
[^equatorcoreq-e2]: EQUATOR Network，COREQ 条目页。[证据](../../../sources/notes/equatorcoreq.md#e2)
[^equatorcoreq-e3]: EQUATOR Network，COREQ 条目页侧栏。[证据](../../../sources/notes/equatorcoreq.md#e3)
[^equatorcoreq-e4]: EQUATOR Network，COREQ 条目页侧栏。[证据](../../../sources/notes/equatorcoreq.md#e4)
[^equatorcoreq-e5]: EQUATOR Network，COREQ 条目页侧栏。[证据](../../../sources/notes/equatorcoreq.md#e5)
[^medrxivabout-e1]: medRxiv，About medRxiv。[证据](../../../sources/notes/medrxivabout.md#e1)
[^medrxivabout-e2]: medRxiv，About medRxiv。[证据](../../../sources/notes/medrxivabout.md#e2)
[^medrxivabout-e3]: medRxiv，About medRxiv。[证据](../../../sources/notes/medrxivabout.md#e3)
[^medrxivabout-e4]: medRxiv，About medRxiv。[证据](../../../sources/notes/medrxivabout.md#e4)
[^icmje2026recommendations-e17]: ICMJE 建议，§III.L.1。[证据](../../../sources/notes/icmje2026recommendations.md#e17)
[^icmje2026recommendations-e21]: ICMJE 建议 2026 年 1 月版，§III.L.1。[证据](../../../sources/notes/icmje2026recommendations.md#e21)
