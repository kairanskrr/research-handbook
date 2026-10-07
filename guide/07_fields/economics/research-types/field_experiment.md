# 田野实验

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**田野实验**（field experiment）：在真实世界里，和政府、非政府组织、企业或社区合作，随机决定谁接受一项干预（发现金、开培训、送信动员投票等），再比较各组的结果。经济学（尤其是发展经济学）和政治学都用这种方法 `[本项目分析]`。

本文只讲田野实验特有的做法。下面这些内容别处已经讲过，本文不重复：经济学的识别策略和美国经济学会（American Economic Association，AEA）的登记要求，见[经济学领域概况](../README.md)；政治学的预分析计划和选举实验伦理争论，见[政治学领域概况](../../political-science/README.md)；随机试验的通用做法（随机序列、意向性分析、报告规范），见临床医学篇的[随机对照试验](../../clinical-medicine/research-types/randomized_controlled_trial.md)；实验室里的对照实验，见计算机篇的[对照实验](../../../06_methods/controlled_experiment.md)。

**读完本文，你应该能：**

- 判断自己的问题能不能做成田野实验，选对引入随机化的方式；
- 和实施伙伴谈清分工，选好随机化的单位，做功效计算和随机分组；
- 处理样本流失、不依从和溢出，分清"意向处理效应"和"实际接受者的效应"。

---

## 1. 这是什么研究，什么时候用

田野实验的核心仍是随机分组：分组随机，两组在干预前平均来说相似，结果差异就可以归于干预 `[本项目分析]`。它和其他随机实验最大的不同是：**项目是真实运行的，实施的是别人**。本文多处引用 Duflo、Glennerster 和 Kremer 2007 年的方法综述（美国国家经济研究局的工作论文，讲发展经济学里怎样用随机化）。他们指出，这类随机研究一般与实施伙伴（政府、非政府组织、企业）合作，伙伴在做真实的项目，想知道它有没有用、怎样改进[^duflo2007toolkit-e1]；在真实项目里引入随机化，几乎总要和真正负责实施的一方合作[^duflo2007toolkit-e2]。

| | 田野实验 | 临床随机对照试验 | 实验室对照实验 | 准实验（自然实验） |
|---|---|---|---|---|
| 谁实施干预 | 合作的政府、组织、企业 | 研究团队按方案给药或治疗 | 研究者本人 | 没人为研究实施，靠制度或事件 |
| 随机化单位 | 常是村、学校、门店等群体 | 多为病人个体 | 多为参与者个体 | 不随机 |
| 主要难点 | 执行走样、样本流失、溢出、伙伴配合 | 盲法、安全监测、报告规范 | 情境人为，结论能否推到真实世界 | 论证"近似随机" |

（表格为本项目归纳 `[本项目分析]`。不能随机分组时怎么做，见[准实验与因果识别](quasi_experiment.md)。）

**什么时候能做。** 你需要一个能影响"谁先得到项目"的机会。Duflo 等人总结了几种入口：

- **名额不够时抽签**：资源有限、申请人多于名额，在合格者中抽签既自然又公平[^duflo2007toolkit-e4]。
- **分批推行时随机定先后**：适合"不能让任何人一直得不到帮助"的场合[^duflo2007toolkit-e5]。两批之间的间隔要长于效果显现所需时间；如果对照组因为预期以后会轮到自己而改变行为，设计就有问题[^duflo2007toolkit-e6]。
- **单位内部随机**（如同一学校里随机定哪个年级用）：缺点是对照组更容易被"污染"[^duflo2007toolkit-e7]。
- **鼓励设计**：不随机分配项目本身，而是随机分配"鼓励参加"[^duflo2007toolkit-e8]。

**什么时候不该做。** 研究网络 J-PAL（阿卜杜勒·拉蒂夫·贾米尔贫困行动实验室，Abdul Latif Jameel Poverty Action Lab）的伦理指南要求：不要剥夺参与者本来有权得到的干预或服务[^jpal2022ethics-e5]。这时可以考虑分批推行或鼓励设计 `[本项目分析]`。

---

## 2. 怎么做

### 第 1 步：找实施伙伴，先把目标和分工谈清楚

**怎么做：**

- **选伙伴。** 按 Duflo 等人的比较：和政府合作覆盖面更广，结果更容易进入政策；非政府组织和企业更灵活，研究者更容易监督设计是否照做[^duflo2007toolkit-e3]。
- **问清对方想学什么。** 研究网络"治理与政治证据网络"（Evidence in Governance and Politics，EGAP）有一份写给实施方的指南，它提醒：实施方不讲清自己需要了解什么，评估者可能设计不出最合适的方法[^egapevaluationconversations-e1]。
- **事先谈好坏结果怎么办。** 这份指南建议做"事前验尸"：双方先设想评估结果为零或为负[^egapevaluationconversations-e4]。也要谈好怎样、在哪里公开结果，双方的时间表很可能不同[^egapevaluationconversations-e3]。
- **把约定写下来**：随机分组谁来做、谁有权改动、数据归谁、论文能否自由发表 `[本项目分析]`。

**为什么**：执行项目的是伙伴，不是你。即使评估是为了学习，组织里也会有人担心结果影响自己的前途[^egapevaluationconversations-e2]。

**容易错在哪**：只和伙伴的高层谈，没有和一线人员沟通 `[本项目分析]`。J-PAL 提醒，对设计很重要的做法（如随机决定发多少钱），在一线人员看来可能不公平[^jpal2022ethics-e2]。

### 第 2 步：选随机化的单位：个人还是群体

**怎么做**：J-PAL 建议，随机化单位至少要是干预实际发放的单位，最好还能把溢出和"因被评估而改变行为"的影响降到最低[^jpal2023randomization-e1]。Duflo 等人列了几方面的权衡：群越大，需要的总样本越多；但处理组会影响对照组时，随机化要放到能包住这种影响的层级[^duflo2007toolkit-e15]；按村随机时，监督"哪些村照做了"比监督每个人容易得多[^duflo2007toolkit-e16]。

**为什么**：随机化的层级越高，有效样本量越小，要达到同样功效需要更多观测[^jpal2023randomization-e2]。

**容易错在哪**：按群分配干预、按个人测结果（这叫整群随机[^egapclusterrandomization-e1]），分析时却当成个人随机来算标准误（见第 8 步）。

### 第 3 步：做功效计算

**功效**（statistical power）是：如果干预真有某个大小的效应，你的实验能得到显著结果的概率 `[本项目分析]`。**最小可检测效应**（minimum detectable effect）是：比它小的效应，即使存在也可能分辨不出来[^jpal2021power-e1]。样本量计算的一般步骤见临床医学篇的[算样本量](../../clinical-medicine/research-types/randomized_controlled_trial.md#第-3-步算样本量)，下面只讲田野实验要多注意的地方。

**怎么做：**

1. **先粗算可不可行**，通过后再用新数据细化（J-PAL 的建议）[^jpal2021power-e7]。
2. **定要检测多大的效应。** 评估政策时，Duflo 等人建议设为"推广后仍然划算"的最小效应[^duflo2007toolkit-e11]。J-PAL 提醒：已发表的同类研究给出的效应通常偏乐观[^jpal2021power-e5]；常用的"小、中、大效应"经验值来自大学生的社会心理学实验，在一些领域和地区的真实环境中被认为不现实[^jpal2021power-e6]。
3. **找参数。** 结果的方差、群内相关程度等，最好用已有数据，最好来自同一国家或地区[^duflo2007toolkit-e10]。
4. **把整群、不依从和流失算进去。** 流失使实际样本变小，功效也降低[^jpal2021power-e3]。
   - **整群**：**组内相关系数**（intra-cluster correlation coefficient）衡量同一群里的人有多相似。J-PAL 举的例子里，组内相关系数只有 0.07，标准误就翻倍，所需样本变成 4 倍[^jpal2021power-e4]。增加群的个数，比在已有群里加人更能提高精度[^duflo2007toolkit-e9]，但成本通常更高[^jpal2021power-e8]。
   - **不依从**（分到处理组的人没接受干预，或反过来）：J-PAL 的例子是，处理组只有一半人接受、对照组无人接受时，所需样本是完全依从时的 4 倍[^jpal2021power-e2]。
5. **定目标功效。** EGAP 的指南说，许多学科以 0.80 为目标；这只是参照，要想清楚能否接受 80% 的预期成功率[^egappower-e3]。
6. **改变假设看结果怎样变**，就知道结论有多依赖假设[^egappower-e2]。设计复杂时，可以用模拟：让计算机把实验跑几千遍，数有几次显著[^egappower-e4]。

**为什么**：功效不足的研究，阴性结果说不清是真没效应还是测不出来；阳性结果也很可能高估了效应[^egappower-e1]。J-PAL 的伦理指南还指出，设计差到结果不可信的研究，让人承担参与的负担却没有知识收益[^jpal2022ethics-e4]。

> **不同的看法：功效不足的研究还值得做吗？** 有人认为，得不出结论的研究不值得做；Duflo 等人则指出，最初几项研究带来的精度增益最大，几项低功效研究也可以合并做元分析[^duflo2007toolkit-e12]。实际操作中：先如实算出最小可检测效应，和导师、伙伴一起判断这个效应在政策上有没有意义；决定做，就在论文里写明功效 `[本项目分析]`。

### 第 4 步：基线调查、分层和随机分组

**基线调查做不做。** 按 Duflo 等人的分析，原则上随机化使基线调查不是必需的；干预贵、调查便宜时做基线省钱，干预便宜、调查贵时，扩大样本、不做基线可能更划算[^duflo2007toolkit-e17]。基线还能检查随机化是否做对，并试用数据收集流程[^duflo2007toolkit-e18]。不要等到干预后再让人回忆"以前怎样"：项目可能影响人们的回忆[^duflo2007toolkit-e19]。

**分层随机。** 随机化保证两组"平均来说"相似；**分层随机**（先按重要特征把样本分成若干层，在每层内随机）保证这一次抽到的两组在这些特征上也确实相似[^duflo2007toolkit-e14]。J-PAL 建议选和结果相关、或你想比较不同群体效应的变量来分层[^jpal2023randomization-e4]；事先想好哪些变量绝不能不平衡，直接按它们分层[^jpal2023randomization-e8]。

**随机分组要能复现。** 用统计软件做，设定随机数种子[^jpal2023randomization-e5]，保存代码和分组结果 `[本项目分析]`。平衡检验别过度解读：在 5% 水平上检验，纯属偶然也会有约 5% 的变量显著不同；多少个算太多，没有明确规则[^jpal2023randomization-e6]。平衡检验的设定尽量和最终分析一致[^jpal2023randomization-e9]。

### 第 5 步：登记，写预分析计划

登记要求和预分析计划（pre-analysis plan，看数据前写好的分析计划）的写法，见[经济学领域概况](../README.md#田野实验要登记预分析计划)和[政治学领域概况](../../political-science/README.md#预分析计划)。要点：AEA 的期刊要求田野实验在投稿前到美国经济学会的随机对照试验登记平台登记，并鼓励尽早[^aea2026rct-e1]；在干预开始前登记的，才标为"预注册"[^aea2026rct-e5]。其他期刊和资助方以各自要求为准 `[本项目分析]`。田野实验的计划要多写几件事：

- **控制哪些变量**要事先写定[^duflo2007toolkit-e13]，**要单独分析哪些子群体**也要事先写明[^duflo2007toolkit-e34]。
- **流失和不依从怎样处理。** 这两项最常被漏掉：Ofosu 和 Posner 抽查了 EGAP 和 AEA 两个登记平台上 2011–2016 年登记的 195 份计划[^ofosu2023preanalysis-e1]，只有 25% 写了怎样处理缺失值或流失，13% 写了怎样处理不依从[^ofosu2023preanalysis-e8]。
- **计划外的分析可以做，但要标明**"未事先写定"，并说明为什么加（Ofosu 和 Posner 的主张）[^ofosu2023preanalysis-e14]。

### 第 6 步：盯住实施

**怎么做**（以下是 J-PAL 实施监测指南的建议）：

- **选少数几个关键指标**，聚焦伙伴能控制的环节[^jpal2021implementation-e2]。
- **核对名单**：把实际接受干预的名单和随机分到处理组的名单对照，监测依从[^jpal2021implementation-e3]。
- **留意"被评估"本身的影响**：受访者可能因为被评估而不是因为干预改变行为[^jpal2021implementation-e4]；不打招呼的实地走访最有用，但也可能引发这种影响[^jpal2021implementation-e7]。
- **记录一切偏差**，供事后分析和报告[^jpal2021implementation-e5]；同时收集干预成本和背景信息，帮助判断能否推广[^jpal2021implementation-e6]。

**为什么**：项目没按设计执行，你可能误以为项目没有效果[^jpal2021implementation-e1]。

**容易错在哪**：两组用不同方法收结果，例如一组用行政记录、另一组做调查；差异可能只是测量方法不同造成的[^duflo2007toolkit-e20]。

### 第 7 步：管住样本流失

随机的流失只降低功效；和干预相关的流失会使估计有偏[^duflo2007toolkit-e28]。即使两组流失率相近，流失的也可能是不同类型的人[^duflo2007toolkit-e29]。流失事后很难补救，要在收数据时管住：基线时就收集日后找到人的信息，例如邻居和亲属的名字[^duflo2007toolkit-e30]。分析的第一步，报告两组各自的流失率，并用基线数据比较流失者和留下的人[^duflo2007toolkit-e31]。

### 第 8 步：分析：按分组比较，算对标准误

**意向处理效应**（intention-to-treat effect）：按最初的随机分组比较两组全体，不管实际是否接受了干预；不能按可能受分组影响的行为剔除或切分样本[^duflo2007toolkit-e21]。Duflo 等人指出，很多时候它本身就是想要的量[^duflo2007toolkit-e22]。

**实际接受者的效应。** 想知道"真正接受干预的人"受了多大影响，可以把随机分组当作工具变量（只借用随机分组带来的那部分变化来估计效应）：在一定假设下，得到的是**局部平均处理效应**（local average treatment effect），即"因分组而改变是否接受干预的人"（依从者）的效应[^duflo2007toolkit-e23][^egaplate-e1]。对照组无人接受时，它就是处理组中实际接受者的效应[^duflo2007toolkit-e24]。注意：

- 它只代表依从者，不代表全体样本[^egaplate-e3]；
- 它要求结果只对实际接受的干预有反应，而不对"被分到哪一组"有反应[^egaplate-e2]。处理组里没直接接受干预的人也受益时（例如班里最弱的学生被抽去补课，其他学生的班级变小了），这样推算就不恰当[^duflo2007toolkit-e25]；
- 意向处理效应为零，它也为零[^egaplate-e4]，所以先报告意向处理效应 `[本项目分析]`。

**整群的标准误。** 忽略整群分配，标准误会偏小[^egapclusterrandomization-e3]：EGAP 的例子里，200 个观测来自 10 个群、组内相关系数为 0.5 时，有效样本只有约 19[^egapclusterrandomization-e2]。Duflo 等人引用的模拟显示，群少于 50 个时常用的聚类稳健标准误容易错误地拒绝"没有效应"，这时可以用随机化推断[^duflo2007toolkit-e32]。

**多个结果。** Duflo 等人主张，收集的结果变量无论显著与否都应报告[^duflo2007toolkit-e33]。统计检验的一般问题见通用篇的[证据、分析与效度](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

### 第 9 步：想清溢出

**溢出**（spillover）指一个对象受到"别人是否接受了干预"的影响[^egapspillovers-e1]。例如在部分投票站监督选举，舞弊可能转移到邻近投票站；降低一家企业的成本，可能改变其他企业面对的价格[^egapspillovers-e2]。EGAP 的溢出指南指出，多数实验分析默认没有溢出[^egapspillovers-e5]；而正向溢出会抬高对照组均值，使估计偏小，负向溢出反之[^egapspillovers-e3]。想知道项目推广到所有人会怎样时，忽视溢出可能大大高估或低估总效应[^egapspillovers-e4]。

**怎么做：**

- **避开**：在单位之间留隔离带[^egapspillovers-e6]，或按能包住溢出的层级随机。溢出不跨群时，按群随机能估计总效应，但分不开直接效应和溢出效应[^duflo2007toolkit-e26]。
- **测量**：随机改变每个群里接受干预的比例，再分别测群内接受者和未接受者[^jpal2023randomization-e3][^duflo2007toolkit-e27]。
- **事先写定溢出范围的假设**，避免事后反复调整直到出现显著结果[^egapspillovers-e7]；但要承认这个假设本身可能错[^egapspillovers-e8]。

### 第 10 步：处理好真实社区里的伦理

通用的知情同意、风险评估见通用篇的[研究涉及人时，先保护人](../../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)；选举实验的伦理争论见[政治学领域概况](../../political-science/README.md#伦理在真实政治环境里做研究)。田野实验要多想几件事：

- **审批不是终点。** J-PAL 的伦理指南说，伦理审查委员会的审查不能代替研究者自己的责任，要问自己，也要问所在社区的人是否认可方案[^jpal2022ethics-e1]；在设计和实施中征询当地伙伴、社区和政府的意见[^jpal2022ethics-e3]。
- **伙伴批准不等于你没责任。** 美国政治学会（American Political Science Association，APSA）2020 年的人类受试者原则说：和第三方合作不会把伦理责任全部转给对方[^apsa2020humansubjects-e14]；选举机构等当局批准也不能免除研究者的全部伦理考量[^apsa2020humansubjects-e15]。
- **想到参与者以外的人。** McDermott 和 Hatemi 提议增加"尊重社会"原则，考虑干预对整个社会的影响[^mcdermott2020ethics-e4]。
- **公正。** J-PAL 指出，分批推行让任何人都不会被永久排除在外[^jpal2022ethics-e6]；给参与者的补偿不能低到剥削，也不能高到影响他们判断风险[^jpal2022ethics-e8]。
- **保护数据。** J-PAL 称数据泄露是社会科学研究最常见的风险[^jpal2022ethics-e7]。它建议只收集研究严格需要的敏感数据[^jpal2023datasecurity-e2]，尽快把能识别身份的信息和其他数据分开[^jpal2023datasecurity-e3]；看似匿名的数据也可能被重新识别[^jpal2023datasecurity-e1]。伙伴和调查员也要懂这些规程[^jpal2023datasecurity-e4]。
- **在论文里报告**对参与者的可能影响、对更广泛政治过程的影响，以及是否、向谁征求了同意（美国政治学会的要求）[^apsa2020humansubjects-e16]。

---

## 3. 检查清单

**必须做到**

- [ ] 随机化单位至少是干预发放的单位[^jpal2023randomization-e1]；整群随机时，功效计算和标准误都考虑了整群[^jpal2021power-e4][^egapclusterrandomization-e3]
- [ ] 投稿 AEA 期刊的田野实验，已在美国经济学会的平台登记[^aea2026rct-e1]
- [ ] 主分析按最初的随机分组比较，没有按受分组影响的行为剔除样本[^duflo2007toolkit-e21]
- [ ] 报告了两组各自的流失率，并比较了流失者和留下的人[^duflo2007toolkit-e31]
- [ ] 两组的结果用同样的方法测量[^duflo2007toolkit-e20]
- [ ] 计划外的分析明确标出，并说明为什么加[^ofosu2023preanalysis-e14]

**做到更好**

- [ ] 干预开始前登记[^aea2026rct-e5]；计划写了控制变量[^duflo2007toolkit-e13]和流失、不依从的处理[^ofosu2023preanalysis-e8]
- [ ] 功效计算用了同一地区的已有数据，并试了不同假设[^duflo2007toolkit-e10][^egappower-e2]
- [ ] 按重要变量分层随机，随机分组代码和种子可复现[^jpal2023randomization-e8][^jpal2023randomization-e5]
- [ ] 有实施监测记录、成本和背景数据[^jpal2021implementation-e5][^jpal2021implementation-e6]
- [ ] 溢出可能重要时，设计里专门测了溢出[^jpal2023randomization-e3]

**这些情况可以不做，不算缺陷**

- 没做基线调查：原则上随机化使基线不是必需的，干预便宜、调查贵时不做基线可能更划算[^duflo2007toolkit-e17]。
- 没有报告"实际接受者的效应"：很多时候意向处理效应本身就是想要的量[^duflo2007toolkit-e22]。
- 平衡表里有一个变量显著不同：纯属偶然也会有约 5% 的变量显著不同[^jpal2023randomization-e6]；只有在有理由怀疑随机化没做对时，平衡检验才最有用[^jpal2023randomization-e7]。

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 按个人随机，干预却会在邻里、同学间传开 | 处理组影响对照组，估计有偏；应放到能包住溢出的层级[^duflo2007toolkit-e15] |
| 照搬已发表研究的效应大小做功效计算 | 已发表的效应通常偏乐观[^jpal2021power-e5]，实验可能功效不足 `[本项目分析]` |
| 只比较"实际接受了干预的人"和对照组 | 接受与否受分组影响，不能按它切分样本[^duflo2007toolkit-e21] |
| 用接受率去除意向处理效应，却不管未接受者也受了影响 | 违反"结果只对实际接受的干预有反应"的假设，这样推算不恰当[^duflo2007toolkit-e25][^egaplate-e2] |
| 整群随机却按个人算标准误 | 标准误偏小，高估了实验提供的信息[^egapclusterrandomization-e3] |
| 控制了受干预影响的变量 | 吃掉了部分效应，估计有偏[^duflo2007toolkit-e13] |
| 干预后让人回忆"以前怎样"代替基线 | 项目可能影响回忆[^duflo2007toolkit-e19] |
| 没有监测执行，结果为零就说"项目无效" | 也可能是项目根本没按设计执行[^jpal2021implementation-e1] |

## 5. 延伸阅读

- **Duflo、Glennerster 和 Kremer 2007，Using Randomization in Development Economics Research: A Toolkit**（美国国家经济研究局技术工作论文，官网免费下载；后收入《发展经济学手册》第 4 卷）：从伙伴、随机化方式到功效、流失、溢出、推断都讲到了。动手设计前通读。
- **J-PAL 研究资源**（功效计算、随机分组、实施监测、伦理、数据安全）：J-PAL 研究网络的免费网页，做到哪一步查哪一篇。
- **EGAP 方法指南**（功效、整群随机、溢出、局部平均处理效应，以及《实施方和评估者需要进行的十次对话》）：EGAP 研究网络的免费网页，适合按问题查阅；"十次对话"主要写给实施方，适合和伙伴第一次见面前读。
- **美国政治学会 2020 年人类受试者原则**、**McDermott 和 Hatemi 2020**：做涉及选举、政治过程的实验前读。

[^duflo2007toolkit-e1]: Duflo, Glennerster & Kremer 2007，§3。[证据](../../../../sources/notes/duflo2007toolkit.md#e1)
[^duflo2007toolkit-e2]: Duflo, Glennerster & Kremer 2007，§3.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e2)
[^duflo2007toolkit-e3]: Duflo, Glennerster & Kremer 2007，§3.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e3)
[^duflo2007toolkit-e4]: Duflo, Glennerster & Kremer 2007，§3.3.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e4)
[^duflo2007toolkit-e5]: Duflo, Glennerster & Kremer 2007，§3.3.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e5)
[^duflo2007toolkit-e6]: Duflo, Glennerster & Kremer 2007，§3.3.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e6)
[^duflo2007toolkit-e7]: Duflo, Glennerster & Kremer 2007，§3.3.3。[证据](../../../../sources/notes/duflo2007toolkit.md#e7)
[^duflo2007toolkit-e8]: Duflo, Glennerster & Kremer 2007，§3.3.4。[证据](../../../../sources/notes/duflo2007toolkit.md#e8)
[^duflo2007toolkit-e9]: Duflo, Glennerster & Kremer 2007，§4.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e9)
[^duflo2007toolkit-e10]: Duflo, Glennerster & Kremer 2007，§4.6。[证据](../../../../sources/notes/duflo2007toolkit.md#e10)
[^duflo2007toolkit-e11]: Duflo, Glennerster & Kremer 2007，§4.6。[证据](../../../../sources/notes/duflo2007toolkit.md#e11)
[^duflo2007toolkit-e12]: Duflo, Glennerster & Kremer 2007，§4.6。[证据](../../../../sources/notes/duflo2007toolkit.md#e12)
[^duflo2007toolkit-e13]: Duflo, Glennerster & Kremer 2007，§4.4。[证据](../../../../sources/notes/duflo2007toolkit.md#e13)
[^duflo2007toolkit-e14]: Duflo, Glennerster & Kremer 2007，§4.5。[证据](../../../../sources/notes/duflo2007toolkit.md#e14)
[^duflo2007toolkit-e15]: Duflo, Glennerster & Kremer 2007，§5.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e15)
[^duflo2007toolkit-e16]: Duflo, Glennerster & Kremer 2007，§5.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e16)
[^duflo2007toolkit-e17]: Duflo, Glennerster & Kremer 2007，§5.3.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e17)
[^duflo2007toolkit-e18]: Duflo, Glennerster & Kremer 2007，§5.3.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e18)
[^duflo2007toolkit-e19]: Duflo, Glennerster & Kremer 2007，§5.3.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e19)
[^duflo2007toolkit-e20]: Duflo, Glennerster & Kremer 2007，§5.3.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e20)
[^duflo2007toolkit-e21]: Duflo, Glennerster & Kremer 2007，§6.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e21)
[^duflo2007toolkit-e22]: Duflo, Glennerster & Kremer 2007，§6.2.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e22)
[^duflo2007toolkit-e23]: Duflo, Glennerster & Kremer 2007，§6.2.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e23)
[^duflo2007toolkit-e24]: Duflo, Glennerster & Kremer 2007，§6.2.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e24)
[^duflo2007toolkit-e25]: Duflo, Glennerster & Kremer 2007，§6.2.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e25)
[^duflo2007toolkit-e26]: Duflo, Glennerster & Kremer 2007，§6.3。[证据](../../../../sources/notes/duflo2007toolkit.md#e26)
[^duflo2007toolkit-e27]: Duflo, Glennerster & Kremer 2007，§6.3。[证据](../../../../sources/notes/duflo2007toolkit.md#e27)
[^duflo2007toolkit-e28]: Duflo, Glennerster & Kremer 2007，§6.4。[证据](../../../../sources/notes/duflo2007toolkit.md#e28)
[^duflo2007toolkit-e29]: Duflo, Glennerster & Kremer 2007，§6.4。[证据](../../../../sources/notes/duflo2007toolkit.md#e29)
[^duflo2007toolkit-e30]: Duflo, Glennerster & Kremer 2007，§6.4。[证据](../../../../sources/notes/duflo2007toolkit.md#e30)
[^duflo2007toolkit-e31]: Duflo, Glennerster & Kremer 2007，§6.4。[证据](../../../../sources/notes/duflo2007toolkit.md#e31)
[^duflo2007toolkit-e32]: Duflo, Glennerster & Kremer 2007，§7.1。[证据](../../../../sources/notes/duflo2007toolkit.md#e32)
[^duflo2007toolkit-e33]: Duflo, Glennerster & Kremer 2007，§7.2。[证据](../../../../sources/notes/duflo2007toolkit.md#e33)
[^duflo2007toolkit-e34]: Duflo, Glennerster & Kremer 2007，§7.3。[证据](../../../../sources/notes/duflo2007toolkit.md#e34)
[^jpal2021power-e1]: J-PAL，Power calculations，Essentials。[证据](../../../../sources/notes/jpal2021power.md#e1)
[^jpal2021power-e2]: J-PAL，Power calculations，Introduction。[证据](../../../../sources/notes/jpal2021power.md#e2)
[^jpal2021power-e3]: J-PAL，Power calculations，Introduction。[证据](../../../../sources/notes/jpal2021power.md#e3)
[^jpal2021power-e4]: J-PAL，Power calculations，Clustered designs。[证据](../../../../sources/notes/jpal2021power.md#e4)
[^jpal2021power-e5]: J-PAL，Power calculations，Practical tips。[证据](../../../../sources/notes/jpal2021power.md#e5)
[^jpal2021power-e6]: J-PAL，Power calculations，Practical tips。[证据](../../../../sources/notes/jpal2021power.md#e6)
[^jpal2021power-e7]: J-PAL，Power calculations，Practical tips。[证据](../../../../sources/notes/jpal2021power.md#e7)
[^jpal2021power-e8]: J-PAL，Power calculations，Practical tips。[证据](../../../../sources/notes/jpal2021power.md#e8)
[^jpal2023randomization-e1]: J-PAL，Randomization，Choosing the unit of randomization。[证据](../../../../sources/notes/jpal2023randomization.md#e1)
[^jpal2023randomization-e2]: J-PAL，Randomization，Choosing the unit of randomization。[证据](../../../../sources/notes/jpal2023randomization.md#e2)
[^jpal2023randomization-e3]: J-PAL，Randomization，Randomization designs to estimate spillover effects。[证据](../../../../sources/notes/jpal2023randomization.md#e3)
[^jpal2023randomization-e4]: J-PAL，Randomization，Stratified randomization。[证据](../../../../sources/notes/jpal2023randomization.md#e4)
[^jpal2023randomization-e5]: J-PAL，Randomization，Randomization methods。[证据](../../../../sources/notes/jpal2023randomization.md#e5)
[^jpal2023randomization-e6]: J-PAL，Randomization，Balance tests。[证据](../../../../sources/notes/jpal2023randomization.md#e6)
[^jpal2023randomization-e7]: J-PAL，Randomization，Balance tests。[证据](../../../../sources/notes/jpal2023randomization.md#e7)
[^jpal2023randomization-e8]: J-PAL，Randomization，Solutions to imbalance。[证据](../../../../sources/notes/jpal2023randomization.md#e8)
[^jpal2023randomization-e9]: J-PAL，Randomization，Balance tests。[证据](../../../../sources/notes/jpal2023randomization.md#e9)
[^jpal2022ethics-e1]: J-PAL，Ethical conduct of randomized evaluations，Introduction。[证据](../../../../sources/notes/jpal2022ethics.md#e1)
[^jpal2022ethics-e2]: J-PAL，Ethical conduct of randomized evaluations，Introduction。[证据](../../../../sources/notes/jpal2022ethics.md#e2)
[^jpal2022ethics-e3]: J-PAL，Ethical conduct of randomized evaluations，How research ethics contribute to research quality。[证据](../../../../sources/notes/jpal2022ethics.md#e3)
[^jpal2022ethics-e4]: J-PAL，Ethical conduct of randomized evaluations，Beneficence principle。[证据](../../../../sources/notes/jpal2022ethics.md#e4)
[^jpal2022ethics-e5]: J-PAL，Ethical conduct of randomized evaluations，Implementing the "do not harm" principle。[证据](../../../../sources/notes/jpal2022ethics.md#e5)
[^jpal2022ethics-e6]: J-PAL，Ethical conduct of randomized evaluations，Implementing the justice principle。[证据](../../../../sources/notes/jpal2022ethics.md#e6)
[^jpal2022ethics-e7]: J-PAL，Ethical conduct of randomized evaluations，Implementing the "minimal risk" principle。[证据](../../../../sources/notes/jpal2022ethics.md#e7)
[^jpal2022ethics-e8]: J-PAL，Ethical conduct of randomized evaluations，Implementing respect for persons。[证据](../../../../sources/notes/jpal2022ethics.md#e8)
[^jpal2021implementation-e1]: J-PAL，Implementation monitoring，Introduction。[证据](../../../../sources/notes/jpal2021implementation.md#e1)
[^jpal2021implementation-e2]: J-PAL，Implementation monitoring，Selecting indicators。[证据](../../../../sources/notes/jpal2021implementation.md#e2)
[^jpal2021implementation-e3]: J-PAL，Implementation monitoring，Indicators to monitor。[证据](../../../../sources/notes/jpal2021implementation.md#e3)
[^jpal2021implementation-e4]: J-PAL，Implementation monitoring，Indicators to monitor。[证据](../../../../sources/notes/jpal2021implementation.md#e4)
[^jpal2021implementation-e5]: J-PAL，Implementation monitoring，Indicators to monitor。[证据](../../../../sources/notes/jpal2021implementation.md#e5)
[^jpal2021implementation-e6]: J-PAL，Implementation monitoring，Indicators to monitor。[证据](../../../../sources/notes/jpal2021implementation.md#e6)
[^jpal2021implementation-e7]: J-PAL，Implementation monitoring，Monitoring methods。[证据](../../../../sources/notes/jpal2021implementation.md#e7)
[^jpal2023datasecurity-e1]: J-PAL，Data security procedures for researchers，Data security overview。[证据](../../../../sources/notes/jpal2023datasecurity.md#e1)
[^jpal2023datasecurity-e2]: J-PAL，Data security procedures for researchers，Minimizing data security threats。[证据](../../../../sources/notes/jpal2023datasecurity.md#e2)
[^jpal2023datasecurity-e3]: J-PAL，Data security procedures for researchers，De-identifying data。[证据](../../../../sources/notes/jpal2023datasecurity.md#e3)
[^jpal2023datasecurity-e4]: J-PAL，Data security procedures for researchers，Data security overview。[证据](../../../../sources/notes/jpal2023datasecurity.md#e4)
[^egappower-e1]: EGAP 方法指南，Statistical Power，§2。[证据](../../../../sources/notes/egappower.md#e1)
[^egappower-e2]: EGAP 方法指南，Statistical Power，§5。[证据](../../../../sources/notes/egappower.md#e2)
[^egappower-e3]: EGAP 方法指南，Statistical Power，§2。[证据](../../../../sources/notes/egappower.md#e3)
[^egappower-e4]: EGAP 方法指南，Statistical Power，§6。[证据](../../../../sources/notes/egappower.md#e4)
[^egapspillovers-e1]: EGAP 方法指南，Spillovers，§1。[证据](../../../../sources/notes/egapspillovers.md#e1)
[^egapspillovers-e2]: EGAP 方法指南，Spillovers，§1。[证据](../../../../sources/notes/egapspillovers.md#e2)
[^egapspillovers-e3]: EGAP 方法指南，Spillovers，§2。[证据](../../../../sources/notes/egapspillovers.md#e3)
[^egapspillovers-e4]: EGAP 方法指南，Spillovers，§2。[证据](../../../../sources/notes/egapspillovers.md#e4)
[^egapspillovers-e5]: EGAP 方法指南，Spillovers，§3。[证据](../../../../sources/notes/egapspillovers.md#e5)
[^egapspillovers-e6]: EGAP 方法指南，Spillovers，§8。[证据](../../../../sources/notes/egapspillovers.md#e6)
[^egapspillovers-e7]: EGAP 方法指南，Spillovers，§9。[证据](../../../../sources/notes/egapspillovers.md#e7)
[^egapspillovers-e8]: EGAP 方法指南，Spillovers，§9。[证据](../../../../sources/notes/egapspillovers.md#e8)
[^egapclusterrandomization-e1]: EGAP 方法指南，Cluster Randomization，§1。[证据](../../../../sources/notes/egapclusterrandomization.md#e1)
[^egapclusterrandomization-e2]: EGAP 方法指南，Cluster Randomization，§2。[证据](../../../../sources/notes/egapclusterrandomization.md#e2)
[^egapclusterrandomization-e3]: EGAP 方法指南，Cluster Randomization，§3。[证据](../../../../sources/notes/egapclusterrandomization.md#e3)
[^egaplate-e1]: EGAP 方法指南，Local Average Treatment Effect，§1。[证据](../../../../sources/notes/egaplate.md#e1)
[^egaplate-e2]: EGAP 方法指南，Local Average Treatment Effect，§2。[证据](../../../../sources/notes/egaplate.md#e2)
[^egaplate-e3]: EGAP 方法指南，Local Average Treatment Effect，§6。[证据](../../../../sources/notes/egaplate.md#e3)
[^egaplate-e4]: EGAP 方法指南，Local Average Treatment Effect，§5。[证据](../../../../sources/notes/egaplate.md#e4)
[^egapevaluationconversations-e1]: EGAP 方法指南，10 Conversations，§1。[证据](../../../../sources/notes/egapevaluationconversations.md#e1)
[^egapevaluationconversations-e2]: EGAP 方法指南，10 Conversations，§4。[证据](../../../../sources/notes/egapevaluationconversations.md#e2)
[^egapevaluationconversations-e3]: EGAP 方法指南，10 Conversations，§8。[证据](../../../../sources/notes/egapevaluationconversations.md#e3)
[^egapevaluationconversations-e4]: EGAP 方法指南，10 Conversations，§9。[证据](../../../../sources/notes/egapevaluationconversations.md#e4)
[^aea2026rct-e1]: About the AEA RCT Registry。[证据](../../../../sources/notes/aea2026rct.md#e1)
[^aea2026rct-e5]: AEA RCT Registry 注册指南。[证据](../../../../sources/notes/aea2026rct.md#e5)
[^ofosu2023preanalysis-e1]: Ofosu & Posner 2023，摘要。[证据](../../../../sources/notes/ofosu2023preanalysis.md#e1)
[^ofosu2023preanalysis-e8]: Ofosu & Posner 2023，Do PAPs Reduce the Scope for Fishing?。[证据](../../../../sources/notes/ofosu2023preanalysis.md#e8)
[^ofosu2023preanalysis-e14]: Ofosu & Posner 2023，Objections to PAPs: Limit Flexibility and Scope for New Discoveries。[证据](../../../../sources/notes/ofosu2023preanalysis.md#e14)
[^apsa2020humansubjects-e14]: 美国政治学会 2020，Guidance (Impact)。[证据](../../../../sources/notes/apsa2020humansubjects.md#e14)
[^apsa2020humansubjects-e15]: 美国政治学会 2020，Guidance (Impact)。[证据](../../../../sources/notes/apsa2020humansubjects.md#e15)
[^apsa2020humansubjects-e16]: 美国政治学会 2020，Impact, 10d。[证据](../../../../sources/notes/apsa2020humansubjects.md#e16)
[^mcdermott2020ethics-e4]: McDermott & Hatemi 2020，Respect for Societies。[证据](../../../../sources/notes/mcdermott2020ethics.md#e4)
