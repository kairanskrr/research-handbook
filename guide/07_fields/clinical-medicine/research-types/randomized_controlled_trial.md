# 随机对照试验

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲怎样设计和实施一项**随机对照试验**（randomized controlled trial）：把受试者随机分到不同干预组，比较他们的结局。伦理审批、试验登记、署名、利益冲突、数据共享这些规则，[临床医学领域概况](../README.md)已经讲过，这里只讲它们落在试验的哪一步。观察性研究（队列、病例对照、横断面）不在本文范围。

**读完本文，你应该能：**
- 用 PICO 把临床问题写成一个试验能回答的问题，并选好主要结局；
- 说清样本量计算要交代哪些假设；
- 分清随机序列、分配隐藏和盲法，各自防的是什么偏倚；
- 知道方案、伦理批准和登记都要在第一位受试者入组之前完成；
- 按意向性分析的原则分析数据，按 CONSORT 2025 写论文。

---

## 1. 这是什么研究，什么时候用

随机对照试验回答**因果问题**："对这类病人，干预 A 比对照 C 更能改善结局 O 吗？"随机分配做得正确时，能消除分组时的选择偏倚，让已知和未知的预后因素在组间均衡[^hopewell2025consortee-e1]。所以设计、实施、分析和报告都恰当的随机试验，一般被认为是评价医疗干预的最高质量证据[^hopewell2025consort-e2]。关键在"都恰当"，下面每一步都是为了守住这一点 `[本项目分析]`。

**和队列研究的区别**（哪些问题更适合观察性研究，见领域概况的[常见的研究类型](../README.md#常见的研究类型)）：

| | 随机对照试验 | 队列研究 |
|---|---|---|
| 谁决定受试者接受什么干预 | 研究者，用随机方法分配 | 不由研究者安排[^icmje2026recommendations-e21] |
| 事前登记 | 必须在招募第一位受试者之前（见第 7 步） | 国际医学期刊编辑委员会（ICMJE）鼓励但不强制[^icmje2026recommendations-e21] |
| 报告规范 | CONSORT 2025（见第 10 步） | STROBE，见[领域概况](../README.md#报告规范按研究类型选清单) |

**和计算机篇的对照实验比。** 两者逻辑相同：主动改变一个因素，随机分组，比较结果。[对照实验](../../../06_methods/controlled_experiment.md)一篇讲过的被试内设计、任务设计、预实验，这里不再重复。临床试验多出来的是下文的分配隐藏、多类人员设盲、入组前登记、独立的数据监查和意向性分析 `[本项目分析]`。

**设计的几种类型。** CONSORT 2025 适用于所有随机试验，但以最常见的两组平行设计为主[^hopewell2025consort-e9]；其他主要设计有多臂平行、交叉、整群和析因设计，各有专门的 CONSORT 扩展版[^hopewell2025consortee-e2]。本文以两组平行设计为例；用其他设计，先找对应的扩展版。

## 2. 怎么做

第 1～6 步是设计决策，全部要写进第 7 步的试验方案。下文大量引用 **CONSORT 2025**（随机试验论文的报告规范）和 **SPIRIT 2025**（试验方案的报告规范）及其解释文章。它们本身不讲怎样设计和实施试验，但点出的关键问题对设计很有帮助[^hopewell2025consort-e10]。它们是报告规范，不是法规；伦理和登记的硬性要求来自《赫尔辛基宣言》、医学期刊的要求和各国规定 `[本项目分析]`。

### 第 1 步：用 PICO 把问题写清楚

**怎么做：**
- 按 **PICO** 写出四个要素：病人人群（Population）、试验干预（Intervention）、对照（Comparator）、结局（Outcome）[^hopewell2025consortee-e3]。例如："对 65 岁以上的社区获得性肺炎住院病人（P），5 天疗程（I）与 10 天疗程（C）相比，30 天内的临床治愈率（O）有没有差别"（本项目举例）。
- **目的用中性的话写**，例如"比较 A 和 B 对 Y 病人结局 X 的效果"，不预设哪个更好[^hopewell2025consortee-e4]。
- **说清要证明什么**：试验干预更好（优效），不比对照差（非劣效），还是两者相当（等效）[^hopewell2025consortee-e5]。这个选择会影响后面的样本量和分析方法 `[本项目分析]`。
- **想好在什么条件下检验**：从理想条件（解释性试验）到常规临床条件（实用性试验），是一条连续谱[^hopewell2025consortee-e6]。
- **选对照时考虑伦理**：世界医学会的《赫尔辛基宣言》要求新干预原则上和已证实最好的干预比较；没有已证实的干预时，才可以用安慰剂或不干预作对照（这是例外之一）[^wma2024helsinki-e14]。

**容易错在哪**：P 写得太宽或太窄，I 和 C 没写到能照着执行的程度 `[本项目分析]`。通用方法见通用篇[先把题目变成能回答的研究问题](../../../general/1_before/04_research_design.md#1-先把题目变成能回答的研究问题)。

### 第 2 步：选结局，定一个主要结局

**怎么做：**
- **定一个主要结局**：事先规定、对病人、医生、决策者和资助方最重要的结局，样本量也按它来算[^hopewell2025consortee-e7]。大多数试验只有一个主要结局；设多个会带来多重比较的解释问题[^hopewell2025consortee-e8]。
- **每个结局写清四件事**：测什么变量、每个人用什么形式的数据（如相对基线的变化）、组内怎样汇总（如均值、比例）、在哪个时间点分析[^hopewell2025consortee-e9]。
- **先查有没有核心结局集**：某个领域所有临床试验至少都应测量和报告的一组公认结局[^hopewell2025consortee-e10]。用了它，结果才方便和别的试验比较 `[本项目分析]`。
- **想好伤害（不良反应）怎么测**。以评价获益为主的试验，可能没有足够把握度检测伤害；但论文仍要说明计划时是否考虑过伤害结局[^hopewell2025consortee-e11]。

**为什么**：结局事先定死，才能防止看了数据再挑结局。登记或方案里的结局和论文里的结局常常对不上，而且常常偏向统计学显著的结果[^hopewell2025consortee-e12]。CONSORT 解释文章引用的一项研究比较了 102 个随机试验的方案和论文：62% 的论文至少有一个主要结局被改动、新增或删掉[^hopewell2025consortee-e13]。

### 第 3 步：算样本量

**怎么做：**
- 按主要结局计算。试验要足够大：如果真有一个事先规定大小、有临床意义的差异，试验有很高的概率检测到它；这个概率叫**把握度**（power，计算机篇叫"功效"）[^hopewell2025consortee-e14]。
- 写明全部假设：依据哪个主要结局和时间点、统计检验、α 值（第一类错误，即假阳性的概率）及是否双侧、把握度，以及每组目标人数[^hopewell2025consortee-e15]。
- 为失访或不依从放大了样本量的，写明细节[^hopewell2025consortee-e16]。方案里还要写明怎样招够人[^chan2025spirit-e1]。

**为什么**：想检测的差异越小，需要的样本越大，而且不是线性关系：很小的差异需要极大的样本[^hopewell2025consortee-e17]。所以目标差异定得过于乐观，样本就会不够 `[本项目分析]`。

**容易错在哪**：结果不显著，再用试验结果反算把握度来解释。这样做没有价值，还可能误导读者[^hopewell2025consortee-e18]。

### 第 4 步：生成不可预测的随机序列

**怎么做：**
- 用随机数字表或计算机随机数生成器生成分配序列，并在论文里写明方法[^hopewell2025consortee-e19]。
- **交替分配、按住院号或出生日期分配都不是随机**，不能叫"随机"，连"准随机"也不能叫[^hopewell2025consortee-e20]。
- **选随机化方式**：几百人以上的试验，简单随机化通常就能让两组人数相近；不到约 200 人的小试验，用某种限制性随机化帮助组间均衡可能有用[^hopewell2025consortee-e21]。常见的限制方式有：
  - **区组随机化**（把受试者按固定人数分成小段，每段内各组人数相等 `[本项目分析]`）：知道区组大小的人能猜出接下来的部分分配；对干预设盲、用更大的区组、随机变换区组大小可以缓解[^hopewell2025consortee-e22]。SPIRIT 2025 建议把区组等细节写在单独文件里，不给负责入组和分配的人看[^chan2025spirit-e2]。
  - **分层随机化**：多中心试验常按中心分层；分层必须配合层内区组之类的限制，否则无效[^hopewell2025consortee-e23]。
- **最小化法**：CONSORT 解释文章称它是随机化唯一可接受的替代方法[^hopewell2025consortee-e24]。具体怎么做，本文资料未涉及，请教试验统计师。

**为什么**：随机化成功靠两步：序列不可预测，并且对负责入组的研究者隐藏[^hopewell2025consortee-e25]。第二步见下一步。

### 第 5 步：做好分配隐藏

**分配隐藏**（allocation concealment）：决定是否纳入一个人、取得他的知情同意时，负责入组的人都不知道下一个分配是什么[^hopewell2025consortee-e26]。

**怎么做：**
- **首选集中分配或第三方分配**，常用药房、中央计算机或电话随机系统[^hopewell2025consortee-e27]。
- **用信封要格外认真**：按顺序编号、不透光、密封；对着光看不透，按顺序拆，先在信封上写好受试者姓名等信息再拆[^hopewell2025consortee-e28]。
- **人员分开**：生成序列、做隐藏的人，与执行分配的人完全分开[^hopewell2025consortee-e29]。

**为什么**：分配隐藏不充分或不清楚的试验，估计出的治疗效果比隐藏充分的试验更大[^hopewell2025consortee-e30]。

**容易错在哪**：把分配隐藏和盲法混为一谈。分配隐藏防选择偏倚，保护分配之前的序列，总能做到；盲法防测量偏倚，保护分配之后的信息，不一定做得到[^hopewell2025consortee-e31]。

### 第 6 步：尽量设盲，说清谁被设盲

**盲法**（blinding，也叫 masking）：对试验中可能受影响的人隐瞒他们分到了哪种干预[^hopewell2025consortee-e32]。

**怎么做：**
- **按角色逐一考虑**：受试者、医护、数据收集者、结局评估者、数据分析者。没设盲的评估者可能对主观结局有差别地评估；没设盲的分析者可能通过挑时间点、挑结局、剔除病人引入偏倚[^hopewell2025consortee-e33]。
- **受试者和医护不能设盲时，至少给评估者设盲**。手术等试验常常做不到前者，但对数据收集者和结局评估者设盲往往做得到，也推荐这样做[^hopewell2025consortee-e34]。
- **写清谁被设盲、用什么手段**，例如外观一致的安慰剂、假干预、假手术[^hopewell2025consortee-e35]；不管能不能设盲，都要写明谁被设盲[^hopewell2025consortee-e56]。
- **事先写好揭盲规则**：什么情况下允许揭盲、怎样揭开某位受试者的分组[^chan2025spirit-e3]。用固定编码（如 A=组 1）会增加破盲风险：揭开一个人就可能揭开多人甚至所有人[^hopewell2025consortee-e36]。

**容易错在哪**：只写"双盲"。一项研究调查了 200 个报告为"双盲"的随机试验的作者，发现实际被设盲的人群有 18 种不同组合；所以要写明每类人员是否设盲[^hopewell2025consortee-e37]。

### 第 7 步：入组第一人之前：写方案、过伦理、做登记

**写方案**：方案是计划方法和实施过程最重要的记录[^chan2025spirit-e4]。按 SPIRIT 2025 写，它有 34 项最低限度条目和一张入组、干预、评估的时间安排图[^chan2025spirit-e5]。第 1～6 步的决定都写进去，还要写明由谁、怎样取得知情同意[^chan2025spirit-e6]；按《赫尔辛基宣言》，临床试验的方案还必须写明试验结束后的安排[^wma2024helsinki-e15]。方案在分配任何受试者之前定稿；完整的统计分析计划在数据库锁定、开始分析之前定稿[^hopewell2025consortee-e38]。

**过伦理**：完整方案必须在入组之前提交研究伦理委员会批准[^chan2025spirit-e7]。知情同意的要求见[领域概况](../README.md#研究对象是人伦理排在第一位)。

**做登记**：《赫尔辛基宣言》要求在招募第一位受试者之前，在公开数据库登记[^wma2024helsinki-e9]；ICMJE 建议医学期刊把"在第一位病人签署入组同意时或之前登记"作为考虑发表的前提[^icmje2026recommendations-e15]。伦理批准不等于登记、事后补登记没用、登记时要写数据共享计划，见领域概况的[先登记，再招募第一位病人](../README.md#先登记再招募第一位病人)和[数据共享声明](../README.md#数据共享声明)。

**去哪登记**：按世界卫生组织（WHO）国际临床试验注册平台的说明，WHO 本身不是登记库，要向 WHO 登记网络中的任一一级登记库提交[^whotrialregistration-e1]；在一个一级登记库或 ICMJE 认可的登记库登记一次即可[^whotrialregistration-e2]。各国对临床试验的监管、法律和伦理要求不同[^whotrialregistration-e3]，以本国规定为准。

**容易错在哪**：方案写得粗。很多方案没写清主要结局、分配方法、盲法、样本量计算、分析方法等，方案有漏洞会导致本可避免的修订[^chan2025spirit-e8]。

### 第 8 步：实施中：监查数据，管好改动

**怎么做：**
- **决定要不要设独立的数据监查委员会**（data monitoring committee）。干预效果特别突出时，出于伦理可能要提前终止；所以宜在数据积累过程中评估结果，最好由独立的委员会来做[^hopewell2025consortee-e39]。方案写明它的组成、职责、是否独立于申办方和资助方；不设的话，解释为什么不需要[^chan2025spirit-e9]。
- **期中分析事先定规则**：期中分析可以看有效、无效和安全性[^hopewell2025consortee-e40]。校正多次查看数据的方法事先写进方案[^hopewell2025consortee-e41]，并写明谁能看期中结果、谁最终决定终止[^chan2025spirit-e10]。
- **安全问题及时上报**：《赫尔辛基宣言》要求，需要监查时，研究者向伦理委员会和/或数据安全监查机构报告，尤其是严重不良事件[^wma2024helsinki-e16]；风险和负担超过潜在获益时，必须评估是继续、修改还是立即停止[^wma2024helsinki-e17]。
- **留住受试者**：事先计划怎样完成随访，包括对中途停止或偏离干预的人仍要收集哪些结局[^chan2025spirit-e11]。
- **改动留痕**：每个方案版本记录修改日期和内容，重要修订及时报告伦理委员会和登记库[^chan2025spirit-e12]；方案修改要经伦理委员会批准[^wma2024helsinki-e16]。论文里报告改动的内容和时间，因为揭盲前后做的改动偏倚风险不同[^hopewell2025consortee-e42]。

**为什么**：反复看数据而不校正，会让结论出错。CONSORT 解释文章举例：做五次期中分析、每次都用 P=0.05 作标准，总的假阳性率会升到接近 19%，而不是预期的 5%[^hopewell2025consortee-e43]。

### 第 9 步：按意向性分析的原则分析

**怎么做：**
- **意向性分析**（intention-to-treat analysis）：所有随机化的受试者都纳入分析，并留在原来分配的组里，不管实际接受了什么干预。这样才能保住随机化的好处，普遍推荐作为首选[^hopewell2025consortee-e44]。
- **写清每项分析纳入了谁、算在哪组**，不要只贴"改良意向性分析""符合方案分析"这类标签；剔除受试者可能破坏随机化，使效果估计有偏[^hopewell2025consortee-e45]。
- **认真处理缺失数据**。很多试验超过 10% 的随机化病人缺失结局[^hopewell2025consortee-e46]；为凑成意向性分析去填补，可能用到"末次观测值结转"这类不恰当的方法[^hopewell2025consortee-e47]。处理方法事先写进统计分析计划，并做敏感性分析 `[本项目分析]`。
- **校正协变量按计划来**：常宜对分层变量做校正；是否校正某个协变量，不应看它在组间有没有显著差异[^hopewell2025consortee-e48]。
- **亚组分析要克制**：一个亚组显著、另一个不显著，不能说明存在亚组差异；看过数据才做的亚组比较，尤其难被后续研究证实[^hopewell2025consortee-e49]。

**容易错在哪**：对基线特征做显著性检验，用来"证明随机化成功"。只要随机化没被破坏，基线差异都是偶然造成的；这种检验不建议做，也不应报告[^hopewell2025consortee-e50]。统计的通用原则见通用篇[认真对待随机性和统计](../../../general/2_during/02_evidence_and_validity.md#5-认真对待随机性和统计)。

### 第 10 步：按 CONSORT 2025 报告

CONSORT（Consolidated Standards of Reporting Trials，临床试验报告统一标准）2025 版有 30 项必报条目和一张受试者流程图[^hopewell2025consort-e1]，取代 2010 版[^hopewell2025consort-e11]。和配套的解释文章一起用[^hopewell2025consort-e12]；投稿时附上填好的清单，注明每一项写在稿件哪里[^hopewell2025consort-e13]。

- **结果写全**：所有计划的主要和次要结局、每个时间点都要报告，不能只报显著的或"有意思"的[^hopewell2025consortee-e51]。道理见通用篇[报告全部结果，包括负面结果](../../../general/4_throughout/02_integrity_and_ethics.md#2-报告全部结果包括负面结果)。
- **报效应量和置信区间**，不要只报 P 值[^hopewell2025consortee-e52]；主要结局是二分类的，相对效应和绝对效应都要报[^hopewell2025consortee-e53]。
- **用流程图交代每个人的去向**：把受试者排除出分析可能得出错误结论，两组排除人数不均衡尤其提示偏倚[^hopewell2025consortee-e54]。
- **和方案、统计分析计划、登记记录对得上**：有没做的或改了的，就写出来[^hopewell2025consort-e8]。
- **讨论不要"美化"结果**：有些讨论部分对结果过分乐观，这叫解释偏倚[^hopewell2025consortee-e55]。

## 3. 检查清单

依据 CONSORT 2025、SPIRIT 2025 及其解释文章整理。CONSORT 不是质量评分表[^hopewell2025consort-e7]：它列的是"要写清楚的事"，下面按"要做到的事"重新组织，分档是本项目的判断 `[本项目分析]`。

**必须做到**
- [ ] 按 PICO 写出研究问题，说明是优效、非劣效还是等效[^hopewell2025consortee-e3][^hopewell2025consortee-e5]
- [ ] 事先规定一个主要结局，写清变量、数据形式、汇总方式和时间点[^hopewell2025consortee-e7][^hopewell2025consortee-e9]
- [ ] 写明样本量计算的全部假设[^hopewell2025consortee-e15]
- [ ] 随机序列不可预测，写明生成方法[^hopewell2025consortee-e19][^hopewell2025consortee-e25]
- [ ] 生成序列、做隐藏的人和执行分配的人分开[^hopewell2025consortee-e29]
- [ ] 写明谁被设盲、怎样设盲[^hopewell2025consortee-e56][^hopewell2025consortee-e35]
- [ ] 入组前：方案获伦理批准[^chan2025spirit-e7]，试验已公开登记[^wma2024helsinki-e9]
- [ ] 写清每项分析纳入了谁、算在哪组[^hopewell2025consortee-e45]
- [ ] 报告所有计划的结局[^hopewell2025consortee-e51]，附效应量的置信区间[^hopewell2025consortee-e52]

**做到更好**
- [ ] 采用本领域的核心结局集[^hopewell2025consortee-e10]
- [ ] 用集中分配或第三方分配[^hopewell2025consortee-e27]
- [ ] 统计分析计划在数据库锁定前定稿[^hopewell2025consortee-e38]
- [ ] 研究结束后 12 个月内把主要结果发布到一级登记库（CONSORT 解释文章转述的世界卫生组织 2015 年声明）[^hopewell2025consortee-e57]

**这些情况可以不做，不算缺陷**
- 受试者和医护无法设盲（如手术试验、实用性试验）[^hopewell2025consortee-e34][^hopewell2025consortee-e58]：写明谁被设盲即可[^hopewell2025consortee-e56]。
- 结局是全因死亡这类客观指标时，数据收集者和评估者是否设盲不太可能有影响[^hopewell2025consortee-e59]。
- 不设数据监查委员会，但在方案里解释了为什么不需要[^chan2025spirit-e9]。
- 没做"盲法检验"（试验结束时问受试者猜自己在哪组）：它的用处本身受到质疑[^hopewell2025consortee-e60]。

**审稿时常见、但不成立的批评**（资料没有统计这些批评有多常见；下面几条是资料明确反对的要求 `[本项目分析]`）
- "两组基线有显著差异，说明随机化失败"：只要随机化没被破坏，基线差异都是偶然造成的，这种检验本就不建议做[^hopewell2025consortee-e50]。
- "某个基线变量组间差异显著，请对它做校正"：是否校正不应按组间是否显著差异来定[^hopewell2025consortee-e48]。
- "结果不显著，请补充事后把握度分析"：用试验结果事后算把握度来解释不显著，没有价值，还可能误导读者[^hopewell2025consortee-e18]。

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 按住院号、出生日期或交替分组，却称为"随机" | 这些不是随机方法，连"准随机"也不能叫[^hopewell2025consortee-e20] |
| 入组的医生能看到随机序列，或信封透光 | 分配隐藏不充分的试验，效果估计偏大[^hopewell2025consortee-e30] |
| 只写"双盲"，不写具体谁被设盲 | 一项 200 个试验的调查发现，"双盲"实际对应 18 种人群组合[^hopewell2025consortee-e37] |
| 设多个主要结局，或事后换主要结局 | 多重比较难以解释[^hopewell2025consortee-e8]；结局改动常偏向显著结果[^hopewell2025consortee-e12] |
| 期中反复看数据，不做校正 | 五次期中分析都用 P=0.05，假阳性率接近 19%[^hopewell2025consortee-e43] |
| 只分析"按方案完成"的人 | 剔除受试者可能破坏随机化[^hopewell2025consortee-e45] |
| 一个亚组显著、另一个不显著，就说"疗效因人群而异" | 不能这样推断亚组差异[^hopewell2025consortee-e49] |

## 5. 延伸阅读

- **CONSORT 2025 声明及其解释文章**（Hopewell 等人 2025；解释文章发表于 BMJ，PubMed Central 有免费全文）：声明是 30 项清单和流程图，写论文时对照用；解释文章是本文主要依据，逐条讲每个条目的含义、理由和实证依据，其中随机化、分配隐藏、盲法、意向性分析几节，设计阶段就值得读。
- **SPIRIT 2025 声明**（Chan 等人 2025）：34 项方案条目，写方案时逐条对照。
- **《赫尔辛基宣言》（世界医学会，2024 年版）、ICMJE 建议（面向医学期刊）、WHO 国际临床试验注册平台网页**：伦理、登记、数据共享的基础文件，见[领域概况](../README.md)；登记前去 WHO 网页查一级登记库。
- 本文资料未涉及：具体的样本量公式和软件、最小化法和缺失数据填补的具体做法、整群和交叉等设计的细节。请看 CONSORT 对应的扩展版，或向试验统计师请教。

[^hopewell2025consortee-e1]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17a，Box 5（Treatment allocation in trials）。[证据](../../../../sources/notes/hopewell2025consortee.md#e1)
[^hopewell2025consortee-e2]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 9（Trial design），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e2)
[^hopewell2025consortee-e3]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 7（Specific objectives），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e3)
[^hopewell2025consortee-e4]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 7，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e4)
[^hopewell2025consortee-e5]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 7，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e5)
[^hopewell2025consortee-e6]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 7，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e6)
[^hopewell2025consortee-e7]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 14（Outcomes），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e7)
[^hopewell2025consortee-e8]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 14，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e8)
[^hopewell2025consortee-e9]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 14，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e9)
[^hopewell2025consortee-e10]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 14，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e10)
[^hopewell2025consortee-e11]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 7（Specific objectives），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e11)
[^hopewell2025consortee-e12]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 14，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e12)
[^hopewell2025consortee-e13]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 10（Changes to trial），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e13)
[^hopewell2025consortee-e14]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16a（Sample size），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e14)
[^hopewell2025consortee-e15]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e15)
[^hopewell2025consortee-e16]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e16)
[^hopewell2025consortee-e17]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e17)
[^hopewell2025consortee-e18]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e18)
[^hopewell2025consortee-e19]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e19)
[^hopewell2025consortee-e20]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e20)
[^hopewell2025consortee-e21]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17b（Type of randomisation），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e21)
[^hopewell2025consortee-e22]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17b，Box 6（Randomisation and minimisation）。[证据](../../../../sources/notes/hopewell2025consortee.md#e22)
[^hopewell2025consortee-e23]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17b，Box 6。[证据](../../../../sources/notes/hopewell2025consortee.md#e23)
[^hopewell2025consortee-e24]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17b，Box 6。[证据](../../../../sources/notes/hopewell2025consortee.md#e24)
[^hopewell2025consortee-e25]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e25)
[^hopewell2025consortee-e26]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 18（Allocation concealment），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e26)
[^hopewell2025consortee-e27]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 18，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e27)
[^hopewell2025consortee-e28]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 18，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e28)
[^hopewell2025consortee-e29]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 19（Implementation），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e29)
[^hopewell2025consortee-e30]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 18，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e30)
[^hopewell2025consortee-e31]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 18，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e31)
[^hopewell2025consortee-e32]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a（Blinding），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e32)
[^hopewell2025consortee-e33]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e33)
[^hopewell2025consortee-e34]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e34)
[^hopewell2025consortee-e35]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e35)
[^hopewell2025consortee-e36]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e36)
[^hopewell2025consortee-e37]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a，Box 7（Blinding terminology）。[证据](../../../../sources/notes/hopewell2025consortee.md#e37)
[^hopewell2025consortee-e38]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 3（Protocol and statistical analysis plan），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e38)
[^hopewell2025consortee-e39]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16b（Interim analyses and stopping），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e39)
[^hopewell2025consortee-e40]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e40)
[^hopewell2025consortee-e41]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e41)
[^hopewell2025consortee-e42]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 10，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e42)
[^hopewell2025consortee-e43]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 16b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e43)
[^hopewell2025consortee-e44]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 21b（Analysis population），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e44)
[^hopewell2025consortee-e45]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 21b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e45)
[^hopewell2025consortee-e46]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 21c（Missing data），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e46)
[^hopewell2025consortee-e47]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 21b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e47)
[^hopewell2025consortee-e48]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 21a（Statistical methods），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e48)
[^hopewell2025consortee-e49]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 21d（Additional analyses），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e49)
[^hopewell2025consortee-e50]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 25（Baseline data），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e50)
[^hopewell2025consortee-e51]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 26，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e51)
[^hopewell2025consortee-e52]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 26（Outcomes and estimation），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e52)
[^hopewell2025consortee-e53]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 26，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e53)
[^hopewell2025consortee-e54]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 22a（Participant flow），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e54)
[^hopewell2025consortee-e55]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 29（Interpretation），Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e55)
[^hopewell2025consortee-e56]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e56)
[^hopewell2025consortee-e57]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 2，Explanation（引用世界卫生组织 2015 年关于公开试验结果的声明）。[证据](../../../../sources/notes/hopewell2025consortee.md#e57)
[^hopewell2025consortee-e58]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e58)
[^hopewell2025consortee-e59]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20a，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e59)
[^hopewell2025consortee-e60]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 20b，Explanation。[证据](../../../../sources/notes/hopewell2025consortee.md#e60)
[^hopewell2025consort-e2]: CONSORT 2025（Hopewell 等人 2025），Introduction，PDF 第 3 页。[证据](../../../../sources/notes/hopewell2025consort.md#e2)
[^hopewell2025consort-e9]: CONSORT 2025（Hopewell 等人 2025），CONSORT 2025 statement。[证据](../../../../sources/notes/hopewell2025consort.md#e9)
[^hopewell2025consort-e10]: CONSORT 2025（Hopewell 等人 2025），Implication and limitations，PDF 第 7 页。[证据](../../../../sources/notes/hopewell2025consort.md#e10)
[^hopewell2025consort-e1]: CONSORT 2025（Hopewell 等人 2025），Abstract，Results，PDF 第 2 页。[证据](../../../../sources/notes/hopewell2025consort.md#e1)
[^hopewell2025consort-e11]: CONSORT 2025（Hopewell 等人 2025），CONSORT 2025 statement。[证据](../../../../sources/notes/hopewell2025consort.md#e11)
[^hopewell2025consort-e12]: CONSORT 2025（Hopewell 等人 2025），CONSORT 2025 statement。[证据](../../../../sources/notes/hopewell2025consort.md#e12)
[^hopewell2025consort-e13]: CONSORT 2025（Hopewell 等人 2025），CONSORT 2025 statement。[证据](../../../../sources/notes/hopewell2025consort.md#e13)
[^hopewell2025consort-e8]: CONSORT 2025（Hopewell 等人 2025），表 1 之后的说明段落，PDF 第 9 页。[证据](../../../../sources/notes/hopewell2025consort.md#e8)
[^hopewell2025consort-e7]: CONSORT 2025（Hopewell 等人 2025），Implication and limitations，PDF 第 7 页。[证据](../../../../sources/notes/hopewell2025consort.md#e7)
[^chan2025spirit-e1]: SPIRIT 2025（Chan 等人 2025），Table 1，item 20。[证据](../../../../sources/notes/chan2025spirit.md#e1)
[^chan2025spirit-e2]: SPIRIT 2025（Chan 等人 2025），Table 1，item 21b。[证据](../../../../sources/notes/chan2025spirit.md#e2)
[^chan2025spirit-e3]: SPIRIT 2025（Chan 等人 2025），Table 1，item 24c。[证据](../../../../sources/notes/chan2025spirit.md#e3)
[^chan2025spirit-e4]: SPIRIT 2025（Chan 等人 2025），Introduction。[证据](../../../../sources/notes/chan2025spirit.md#e4)
[^chan2025spirit-e5]: SPIRIT 2025（Chan 等人 2025），Updated SPIRIT 2025 statement。[证据](../../../../sources/notes/chan2025spirit.md#e5)
[^chan2025spirit-e6]: SPIRIT 2025（Chan 等人 2025），Table 1，item 32a。[证据](../../../../sources/notes/chan2025spirit.md#e6)
[^chan2025spirit-e7]: SPIRIT 2025（Chan 等人 2025），Definition of a randomised trial protocol。[证据](../../../../sources/notes/chan2025spirit.md#e7)
[^chan2025spirit-e8]: SPIRIT 2025（Chan 等人 2025），Introduction。[证据](../../../../sources/notes/chan2025spirit.md#e8)
[^chan2025spirit-e9]: SPIRIT 2025（Chan 等人 2025），Table 1，item 28a。[证据](../../../../sources/notes/chan2025spirit.md#e9)
[^chan2025spirit-e10]: SPIRIT 2025（Chan 等人 2025），Table 1，item 28b。[证据](../../../../sources/notes/chan2025spirit.md#e10)
[^chan2025spirit-e11]: SPIRIT 2025（Chan 等人 2025），Table 1，item 25b。[证据](../../../../sources/notes/chan2025spirit.md#e11)
[^chan2025spirit-e12]: SPIRIT 2025（Chan 等人 2025），Definition of a randomised trial protocol。[证据](../../../../sources/notes/chan2025spirit.md#e12)
[^whotrialregistration-e1]: WHO 国际临床试验注册平台，Trial registration 网页，How to register a trial。[证据](../../../../sources/notes/whotrialregistration.md#e1)
[^whotrialregistration-e2]: WHO 国际临床试验注册平台，Trial registration 网页，How to register a trial。[证据](../../../../sources/notes/whotrialregistration.md#e2)
[^whotrialregistration-e3]: WHO 国际临床试验注册平台，Trial registration 网页，How to register a trial，NOTE。[证据](../../../../sources/notes/whotrialregistration.md#e3)
[^icmje2026recommendations-e21]: ICMJE 建议 2026 年 1 月版，§III.L.1 Registration。[证据](../../../../sources/notes/icmje2026recommendations.md#e21)
[^icmje2026recommendations-e15]: ICMJE 建议 2026 年 1 月版，§III.L.1 Registration。[证据](../../../../sources/notes/icmje2026recommendations.md#e15)
[^wma2024helsinki-e14]: WMA 2024（《赫尔辛基宣言》），Use of Placebo。[证据](../../../../sources/notes/wma2024helsinki.md#e14)
[^wma2024helsinki-e15]: WMA 2024（《赫尔辛基宣言》），Scientific Requirements and Research Protocols。[证据](../../../../sources/notes/wma2024helsinki.md#e15)
[^wma2024helsinki-e9]: WMA 2024（《赫尔辛基宣言》），Research Registration, Publication, and Dissemination of Results。[证据](../../../../sources/notes/wma2024helsinki.md#e9)
[^wma2024helsinki-e16]: WMA 2024（《赫尔辛基宣言》），Research Ethics Committees。[证据](../../../../sources/notes/wma2024helsinki.md#e16)
[^wma2024helsinki-e17]: WMA 2024（《赫尔辛基宣言》），Risks, Burdens, and Benefits。[证据](../../../../sources/notes/wma2024helsinki.md#e17)
