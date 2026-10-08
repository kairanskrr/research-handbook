# 机械工程：学科概况

本文讲机械工程（流体、热工、固体力学、动力学与控制、制造、机器人硬件等方向）的研究怎样运转。这里的结论常来自两处：试验台上的测量，和计算机上的数值仿真。两样都要交代清楚"有多准" `[本项目分析]`。各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里的主线各章和[贯穿全程](../../08_throughout/README.md)；本学科常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。和实物、测量、专利打交道的共性问题，可对照[电子信息篇](../electrical-engineering/README.md)。这里只写本学科特有的东西。

**读完本文，你应该能：**

- 说清试验、数值仿真和"设计—制造—测试"各起什么作用，各按什么标准评判；
- 知道为什么测量结果要带不确定度，以及部分期刊对它的要求；
- 知道部分期刊对数值精度（网格收敛、迭代收敛）有哪些硬性要求；
- 分清校准和确认；
- 以美国机械工程师学会（ASME）为例，了解会议论文转期刊、署名和利益冲突的规定；
- 进车间、上试验台之前，知道最基本的安全规矩。

---

## 本领域研究怎样运转

### 结果从哪里来：试验台、数值仿真、做出样机

机械工程的研究常见三种做法，一个项目里往往组合使用 `[本项目分析]`：

- **试验**：在试验台、风洞、水槽、材料试验机上测量。结论靠不靠得住，很大程度看测量有多准（见下文"测量结果要带上不确定度"）。
- **数值仿真**：例如计算流体力学（Computational Fluid Dynamics，CFD，用计算机解流动方程）、有限元分析（Finite Element Analysis，FEA，常用于结构和传热）。结论靠不靠得住，要看数值误差控制住没有、模型用实验检验过没有（见下文"数值结果要证明网格够细"）。
- **设计—制造—测试**：提出新的机构、结构或控制方法，做出样机，在试验台上测性能。思路和计算机篇的[工程研究](../computer-science/practices/engineering_research.md)一致：先写清主张，再为每条主张选验证方式。

这类工作常受硬件拖累：加工零件、搭试验台、预约风洞都要时间，装错一次可能要返工 `[本项目分析]`。排期方法见贯穿全程的[计划与日常节奏](../../08_throughout/planning_and_routines.md)。

### 发表：以 ASME 为例

ASME 既办期刊，也办会议。它的综合性年会叫"国际机械工程大会与展览"（IMECE）。2026 年这届设有近 20 个技术方向[^asme2026imece-e1]，包括流体工程、传热与热工程，以及固体、结构与流体力学等[^asme2026imece-e2]。日程是：3 月 10 日交摘要[^asme2026imece-e3]，5 月 5 日起交全文送审[^asme2026imece-e4]，6 月 9 日审完[^asme2026imece-e8]，8 月 11 日交定稿[^asme2026imece-e6]，11 月开会[^asme2026imece-e7]。从交摘要到开会约八个月 `[本项目分析]`。也可以只交摘要，只做报告或贴海报[^asme2026imece-e5]。其他会议以会议网站为准 `[本项目分析]`。

**会议论文转期刊（ASME 期刊的规定）。** ASME 期刊接受在会议上发表过的论文，但要写明是哪个会议、会后改了什么[^asmeconfpapers-e1]；送不送审、发不发表由期刊主编决定[^asmeconfpapers-e2]。如果是 ASME 自己的会议，要等收到会议录用通知后才能投 ASME 期刊，以免重复投稿[^asmeconfpapers-e3]。期刊会重新独立审稿[^asmeconfpapers-e4]，期刊版要在脚注和参考文献里引用会议版[^asmeconfpapers-e5]。投其他出版方（如 Elsevier、Springer、国内期刊）时，以对方的规定为准 `[本项目分析]`。

**期刊还是会议为主。** 本文资料没有直接统计机械工程论文发在期刊还是会议，只有一项间接数据：Lisée 等人 2008 年统计了 1980–2005 年 Thomson 引文索引（今 Web of Science 的前身）所收期刊论文的参考文献[^lisee2008conference-e1]。这 26 年里，机械工程论文引用的文献约 8% 是会议论文，计算机是 19.6%，都属于会议论文占比最高的一批子领域[^lisee2008conference-e2]；而 2005 年全部自然科学和工程论文的参考文献里，会议论文只占约 1.7%[^lisee2008conference-e3]。可见机械工程期刊论文引用的大多不是会议论文，但会议论文的分量比多数学科重；注意它统计的是"引用了什么"，不是"发在哪里"。各方向（例如机器人）可能不同，以导师和目标期刊、会议的要求为准 `[本项目分析]`。

**审稿要多久（跨学科统计，只作参考）。** Björk 和 Solomon 2013 年发表的研究，从 Scopus 引文数据库分层随机抽了 135 本期刊的 2700 篇论文[^bjork2013publishing-e1]；每本期刊取 2012 年最后刊出的 20 篇往前数，期刊被粗分成工程、地球科学、社会科学等九组[^bjork2013publishing-e2]。"投稿到录用"这段反映审稿和修改花的时间，"录用到刊出"反映出版流程和排队等待刊出的时间[^bjork2013publishing-e3]。工程组期刊这两段平均是 5.0 个月和 4.3 个月[^bjork2013publishing-e4]。但同一组里各期刊之间的差别，比组与组之间的差别大得多[^bjork2013publishing-e5]。这项研究没有单列机械工程，数据也是十多年前的，只能当大致参考；目标期刊实际要多久，以期刊公布的数据为准 `[本项目分析]`。

### 署名：做试验、搭平台的人也要考虑

ASME 对其《伦理准则》的解释准则（2012 年版）写明：多人参与的研究（包括学生和导师、企业的主管或研究人员）写成论文、学位论文或报告时，要承认所有重要贡献者；合著者应在投稿前彼此同意署名安排[^asme2012canons-e1]。ASME 网站上的出版伦理标准则要求：只有对研究和论文撰写都有重要贡献的人才列为合著者[^asmeethicalstandards-e6]。所以，搭试验台、做加工的人是署名还是写进致谢，最好在项目开始时就和导师谈清楚 `[本项目分析]`。通用原则见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#5-署名引用和利益冲突给每个贡献者应得的认可)。

---

## 和其他学科不同的地方

下表是本项目的归纳，只为帮你快速定位差别 `[本项目分析]`。

| | 机械工程 | 计算机领域 |
|---|---|---|
| 结果从哪来 | 试验台测量、数值仿真（流体、结构、传热）、样机测试 | 以代码、系统和数据上的实验为主 |
| "有多准"怎么说 | 测量结果要带不确定度[^jcgm2008gum-e1]；部分期刊要求数值结果证明网格收敛[^jfenumaccuracy-e2] | 多用重复运行和统计检验（见主线章节[报告差多少、有多确定，而不只是 p 值](../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)） |
| 周期受谁控制 | 还受加工、搭台、设备预约影响 | 主要受会议截稿日控制 |
| 安全 | 车间和试验台有人身伤害风险（见下文） | 计算机篇未涉及 |

---

## 本领域的规范和报告标准

### 测量结果要带上不确定度

国际通行的依据是计量指南联合委员会（JCGM）的《测量不确定度表示指南》（简称 GUM），国际计量局（BIPM）网站可免费下载。GUM 开篇就讲了原因：报告物理量的测量结果，必须定量说明结果的质量，让用的人能判断它有多可靠；没有这个说明，测量结果彼此之间、和标准里的参考值之间都无法比较[^jcgm2008gum-e1]。

怎样定义被测量、做校准、列不确定度预算、算扩展不确定度，见跨学科方法[实验测量研究](../../06_methods/experimental_measurement.md#第五步做不确定度预算)。本学科还要注意两点：

**"准确度"不配数字。** NIST 技术说明 1297 指出，准确度是定性概念，数字应该配给不确定度[^taylor1994nist-e2]；它也提到，"精密度"常被简单当作"重复性"用[^taylor1994nist-e3]。读文献时先看作者怎么用这些词 `[本项目分析]`。

**期刊的要求（以美国航空航天学会 AIAA 为例）。** AIAA 期刊写明：没有充分给出数据精度的实验论文不接收[^aiaaeditorialpolicy-e1]，具体由各刊主编和负责的副主编执行[^aiaaeditorialpolicy-e2]。它要求作者：估计系统性偏差的不确定度并说明方法[^aiaaeditorialpolicy-e3]，量化结果的重复性[^aiaaeditorialpolicy-e4]，指出没计入总不确定度的已知来源[^aiaaeditorialpolicy-e5]，写出实验条件和数据采集顺序[^aiaaeditorialpolicy-e6]，写明包含因子[^aiaaeditorialpolicy-e8]。投其他期刊时，先查目标期刊的作者须知 `[本项目分析]`。

### 数值结果要证明网格够细

数值仿真的结果会随网格疏密、时间步长、迭代停得早晚而变 `[本项目分析]`。有些期刊为此定了硬性要求。

**《流体工程杂志》（ASME 出版）的编辑政策。** 这本期刊不考虑没有系统检验截断误差、没有估计精度的数值论文[^jfenumaccuracy-e1]。其中几条：

- 数值方法要写具体，只写"守恒的有限体积格式"再引一本通用教科书不够[^jfenumaccuracy-e4]；
- 要给出在几套疏密明显不同的网格上的解，证明结果与网格无关或随网格收敛[^jfenumaccuracy-e2]；
- 迭代计算的停止准则要写清，并估计收敛误差[^jfenumaccuracy-e6]；
- 可以和实验比较，但实验不确定度要先确定；只用一套网格算、和实验"大致吻合"不够，有可调参数时更不够[^jfenumaccuracy-e3]。

编辑也承认，很多实际工程计算还会只用一套网格，但这样的分析不适合在这本期刊发表[^jfenumaccuracy-e5]。

**Celik 等人 2008 年的具体做法**（和这份政策放在同一个 PDF 里）：

1. 先证明迭代已收敛：每个方程的归一化残差至少下降三个（最好四个）数量级[^celik2008procedure-e1]；
2. 在三套明显不同的网格上算关键量，网格加密比最好大于 1.3（作者说明这是经验值）[^celik2008procedure-e2]；
3. 用文中的网格收敛指数（Grid Convergence Index，GCI）方法估计离散误差；用这个方法，审稿时不会质疑方法本身[^celik2008procedure-e4]；
4. 画剖面曲线时，像实验数据一样用误差棒标出数值不确定度[^celik2008procedure-e6]；
5. 研究并报告解对入口条件小扰动有多敏感[^celik2008procedure-e3]。

Celik 等人在算例里特别注明：这样算出的数值不确定度不包括建模误差[^celik2008procedure-e5]。也就是说，网格收敛只说明方程解得准，不说明方程选得对 `[本项目分析]`。

AIAA 对数值论文也有要求，例如用到商业软件时要引用公开的代码测试资料[^aiaaeditorialpolicy-e7]。

### 校准不是确认

验证（verification，查方程解得对不对）和确认（validation，查模型对真实世界够不够准）的一般方法，见研究方法里的[定量仿真](../../06_methods/simulation_study.md#第三步验证与确认)。美国桑迪亚国家实验室的 Oberkampf 和 Trucano（2002 年）的说法是：验证主要是数学问题，确认主要是物理问题[^oberkampf2002verification-e2]。

本领域要特别提防的是第三件事：**校准**（calibration）。校准是调整参数，让计算结果和实验数据吻合[^oberkampf2002verification-e5]。按实验调好参数，再宣称模型"确认通过"，这是混淆。他们指出，计算流体力学代码按实验测量值校准太常见，很多人分不清自己是在校准还是在确认[^oberkampf2002verification-e7]。

他们把专门检验计算模型的实验叫"确认实验"，建议由做实验的、建模的、写代码的和用代码的人从头到尾一起设计[^oberkampf2002verification-e6]，可能的话在不同设施里做同一个确认实验[^oberkampf2002verification-e10]。另一种做法：实验数据整理好后，先不给计算方看结果，只给算题需要的全部条件[^oberkampf2002verification-e8]；计算方先量化自己解的误差和不确定度，再拿来和实验比[^oberkampf2002verification-e9]。这和物理学的[盲分析](../physical-sciences/README.md#盲分析先定方法再看答案)思路相近 `[本项目分析]`。不过作者也说，这种严格的独立性是针对工程分析用的代码，大学研究者开发的代码不一定要做到这个程度[^oberkampf2002verification-e11]。

### ASME 的伦理准则

ASME 要求会员遵守它的《工程师伦理准则》[^asme2024ethics-e1]。下面几条和研究关系较大 `[本项目分析]`，都是 ASME 的规定；其他国家的学会（例如中国机械工程学会）有自己的准则，本文资料未涉及，以所在单位和目标期刊的规定为准。

- **公众安全放在首位**[^asme2024ethics-e2]。发现与工作直接相关、可能危及公众安全或健康的情况，要报告上级和有关部门[^asme2012canons-e6]。
- **避免利益冲突**，也避免看起来有利益冲突[^asme2024ethics-e4]。投稿时要向编辑披露，例如你在可能受论文结果影响的公司有咨询关系或经济利益[^asmeethicalstandards-e4]。
- **尊重别人的专有信息和知识产权**[^asme2024ethics-e5]；未经同意，不泄露雇主或客户的技术工艺等保密信息[^asme2012canons-e4]。

写够细节让同行能重做、不一稿多投、不抄袭等通用要求，ASME 也有[^asmeethicalstandards-e1][^asmeethicalstandards-e3][^asme2012canons-e2]，详见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md)。

### 企业资助的研究：先谈好知识产权和发表

和企业合作时，以下是 ASME 的两条规定：

- 替别人做可能产生发明、设计（可能申请专利或专有权）的工作之前，先和各方明确约定权利归属[^asme2012canons-e3]。
- 作者要确保没有合同关系或专有权方面的考虑妨碍论文发表[^asmeethicalstandards-e5]。所以签合同时就要问清：结果能不能发表、发表前要不要给企业审查 `[本项目分析]`。

合作前要不要先向学校报告发明、什么算"公开"、公开后专利会怎样，见电子信息篇的[发表还是申请专利](../electrical-engineering/README.md#发表还是申请专利以美国为例)（那里引的是美国几所大学的说明）。

### 车间和试验台安全

下面是美国的例子；各国法规和各单位规定不同，进实验室前以本单位的安全培训和规章为准 `[本项目分析]`。

**美国职业安全与健康管理局（OSHA）的说明。** 机器的运动部件可能压碎手指、造成截肢、烧伤或失明[^oshamachineguarding-e1]。OSHA 要求：任何可能伤人的机器部件、功能或工序都必须加防护[^oshamachineguarding-e2]。维修设备时，机器意外启动或储存的能量意外释放，可能致人重伤或死亡[^oshalockout-e1]；办法是"上锁挂牌"（lockout/tagout）[^oshalockout-e2]，即断开能源后上锁、挂警示牌，防止别人误开 `[本项目分析]`。

**美国卡内基梅隆大学的车间安全指南**（只代表这一所学校的规定）：

- 用机器前必须接受培训并证明能胜任[^cmu2025machineshop-e1]，包括通用车间安全课和每种机器的专门培训[^cmu2025machineshop-e2]；
- 不能单独操作，车间里至少要有两个人[^cmu2025machineshop-e3]；
- 开工前确认运动部件上的防护罩已装好[^cmu2025machineshop-e5]；用钻床、锯这类带旋转部件的工具时不戴手套，以免手被卷进去[^cmu2025machineshop-e4]；
- 机器运转时不离人[^cmu2025machineshop-e8]；确认已断电、已上锁挂牌、安全装置到位[^cmu2025machineshop-e7]；
- 赶时间就做不安全；不能安全完成的就不要开始[^cmu2025machineshop-e6]。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表只列本文资料能支持的两种，其他套路本文资料未涉及。表的分组和第二栏是本项目的归纳，每条标准只代表脚注里的那份指南或那本期刊 `[本项目分析]`。

| 套路 | 在机械工程里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md) | 设计—制造—测试：提出新的机构、结构或控制方法，做出样机上试验台测；或在数值仿真上评估设计 | 测量结果要带不确定度，否则无法和别人的比较[^jcgm2008gum-e1]；《流体工程杂志》要求在几套疏密明显不同的网格上证明结果收敛[^jfenumaccuracy-e2]，只用一套网格、和实验大致吻合不够[^jfenumaccuracy-e3]；按实验调参数是校准[^oberkampf2002verification-e5]，别当成确认[^oberkampf2002verification-e7] | [工程研究](../computer-science/practices/engineering_research.md)（计算机篇）、[定量仿真](../../06_methods/simulation_study.md) |
| [测量](../../05_research-strategies/measure.md) | 在试验台、风洞、水槽上把一个量测准，并说清有多准；也包括专门检验计算模型的确认实验 | 列出全部不确定度分量并写清怎样评定[^jcgm2008gum-e8]，报扩展不确定度时写明包含因子[^jcgm2008gum-e9]；AIAA 期刊不接收没有充分给出数据精度的实验论文[^aiaaeditorialpolicy-e1]；确认实验由做实验、建模、写代码和用代码的人一起设计[^oberkampf2002verification-e6] | [实验测量研究](../../06_methods/experimental_measurement.md) |

怎么用这张表 `[本项目分析]`：先按核心主张定主要套路。例如做出新样机、同时测它的效率，主张是"新设计更好"，按构建改进的标准要求；测量部分仍要满足测量的要求。

## 本学科常用的研究方法

本学科没有独有的方法文档，用的是[研究方法](../../06_methods/README.md)里的跨学科方法和计算机篇的实践：

- [实验测量研究](../../06_methods/experimental_measurement.md)：试验台、风洞等设施上的测量，期刊要求见上文[测量结果要带上不确定度](#测量结果要带上不确定度)。
- [定量仿真](../../06_methods/simulation_study.md)：那篇举的是离散事件、系统动力学、基于智能体的仿真；本学科的仿真多是解偏微分方程，还要报告网格收敛、迭代收敛等数值误差，见上文[数值结果要证明网格够细](#数值结果要证明网格够细) `[本项目分析]`。
- [工程研究](../computer-science/practices/engineering_research.md)、[优化研究](../computer-science/practices/optimization_study.md)（计算机篇）：结构优化、形状优化如果每次评估都要跑一次仿真，结果的可信度还取决于每次仿真的数值精度 `[本项目分析]`。

---

## 给新手的建议

1. **每个测量结果都写上不确定度，并说明怎么评定的。** 没有它，结果没法和别人的比[^jcgm2008gum-e1][^jcgm2008gum-e8]。
2. **做数值仿真，从一开始就规划三套网格。** 别等审稿人要求了再补[^celik2008procedure-e2]。
3. **调过参数，就叫"校准"，不要叫"确认"。**[^oberkampf2002verification-e5][^oberkampf2002verification-e7]
4. **做计算的人，早点和做实验的人坐下来谈。** 一起定测什么、怎么测[^oberkampf2002verification-e6]。
5. **签企业合作合同前，问清发表和知识产权。**[^asme2012canons-e3][^asmeethicalstandards-e5]
6. **没培训过的机器不碰，不单独进车间，不赶工。**[^cmu2025machineshop-e1][^cmu2025machineshop-e3][^cmu2025machineshop-e6]

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 实验数据只给平均值，不给不确定度 | 别人无法判断可靠性，也没法比较[^jcgm2008gum-e1] |
| 只报告重复测量的统计不确定度，漏掉仪器、校准等来源 | GUM 列出的来源远不止重复测量的差异[^jcgm2008gum-e2] |
| 把"准确度 ±2%"当成定量指标写 | NIST 技术说明 1297 指出准确度是定性概念，数字应配给不确定度[^taylor1994nist-e2] |
| 只用一套网格算，和实验大致吻合就下结论 | 《流体工程杂志》明确说这不够，有可调参数时更不够[^jfenumaccuracy-e3] |
| 以为网格收敛了，结果就"对了" | 数值不确定度不包括建模误差[^celik2008procedure-e5] |
| ASME 会议论文还没收到录用通知，就投 ASME 期刊 | ASME 规定要等录用通知后才能投[^asmeconfpapers-e3] |

---

## 延伸阅读

- **JCGM 100:2008（GUM）**：测量不确定度的国际通行指南，BIPM 网站免费下载。第一次写实验论文前读。
- **NIST Technical Note 1297（Taylor 与 Kuyatt 1994）**：NIST 评定和表示本院测量不确定度的指南，附录有术语说明。想先读篇幅短些的材料时读它 `[本项目分析]`。
- **《流体工程杂志》数值精度政策和 Celik 等人 2008 的程序**：ASME 网站上的同一个 PDF，有完整的网格收敛指数算例。做计算流体力学前读。
- **AIAA Editorial Policy Statement on Numerical and Experimental Accuracy**：列出数值和实验两方面的报告要求，可当投稿前的检查清单。
- **Oberkampf 与 Trucano 2002，Verification and Validation in Computational Fluid Dynamics**：验证与确认的系统论述，第 4.3 节"确认实验指南"对做实验和做计算的人都有用。
- **你所在单位的实验室安全培训和技术转移部门的说明**：本文引用的是美国机构的规定，以本单位为准。

[^oberkampf2002verification-e2]: Oberkampf 与 Trucano 2002，§1.1。[证据](../../../sources/notes/oberkampf2002verification.md#e2)
[^oberkampf2002verification-e5]: Oberkampf 与 Trucano 2002，§4.1。[证据](../../../sources/notes/oberkampf2002verification.md#e5)
[^oberkampf2002verification-e6]: Oberkampf 与 Trucano 2002，§4.3，Guideline 1。[证据](../../../sources/notes/oberkampf2002verification.md#e6)
[^oberkampf2002verification-e7]: Oberkampf 与 Trucano 2002，§4.3，Guideline 4。[证据](../../../sources/notes/oberkampf2002verification.md#e7)
[^oberkampf2002verification-e8]: Oberkampf 与 Trucano 2002，§4.3，Guideline 4。[证据](../../../sources/notes/oberkampf2002verification.md#e8)
[^oberkampf2002verification-e9]: Oberkampf 与 Trucano 2002，§4.3，Guideline 4。[证据](../../../sources/notes/oberkampf2002verification.md#e9)
[^oberkampf2002verification-e10]: Oberkampf 与 Trucano 2002，§4.3。[证据](../../../sources/notes/oberkampf2002verification.md#e10)
[^oberkampf2002verification-e11]: Oberkampf 与 Trucano 2002，§4.3，Guideline 4。[证据](../../../sources/notes/oberkampf2002verification.md#e11)
[^asme2026imece-e1]: ASME，IMECE 2026 会议主页，会议介绍。[证据](../../../sources/notes/asme2026imece.md#e1)
[^asme2026imece-e2]: ASME，IMECE 2026 会议主页，Program – Tracks & Special Symposia。[证据](../../../sources/notes/asme2026imece.md#e2)
[^asme2026imece-e3]: ASME，IMECE 2026 会议主页，Important Dates。[证据](../../../sources/notes/asme2026imece.md#e3)
[^asme2026imece-e4]: ASME，IMECE 2026 会议主页，Important Dates。[证据](../../../sources/notes/asme2026imece.md#e4)
[^asme2026imece-e5]: ASME，IMECE 2026 会议主页，Important Dates。[证据](../../../sources/notes/asme2026imece.md#e5)
[^asme2026imece-e6]: ASME，IMECE 2026 会议主页，Important Dates。[证据](../../../sources/notes/asme2026imece.md#e6)
[^asme2026imece-e7]: ASME，IMECE 2026 会议主页，页面标题区。[证据](../../../sources/notes/asme2026imece.md#e7)
[^asme2026imece-e8]: ASME，IMECE 2026 会议主页，Important Dates。[证据](../../../sources/notes/asme2026imece.md#e8)
[^asmeconfpapers-e1]: ASME 期刊作者指南，Papers Presented at a Conference，Conferences。[证据](../../../sources/notes/asmeconfpapers.md#e1)
[^asmeconfpapers-e2]: ASME 期刊作者指南，Papers Presented at a Conference，Conferences。[证据](../../../sources/notes/asmeconfpapers.md#e2)
[^asmeconfpapers-e3]: ASME 期刊作者指南，Papers Presented at a Conference，ASME Conferences。[证据](../../../sources/notes/asmeconfpapers.md#e3)
[^asmeconfpapers-e4]: ASME 期刊作者指南，Papers Presented at a Conference，ASME Conferences。[证据](../../../sources/notes/asmeconfpapers.md#e4)
[^asmeconfpapers-e5]: ASME 期刊作者指南，Papers Presented at a Conference，ASME Conferences。[证据](../../../sources/notes/asmeconfpapers.md#e5)
[^asme2012canons-e1]: ASME 伦理准则解释准则 2012，2.f.(1)。[证据](../../../sources/notes/asme2012canons.md#e1)
[^asme2012canons-e2]: ASME 伦理准则解释准则 2012，2.g。[证据](../../../sources/notes/asme2012canons.md#e2)
[^asme2012canons-e3]: ASME 伦理准则解释准则 2012，4.l。[证据](../../../sources/notes/asme2012canons.md#e3)
[^asme2012canons-e4]: ASME 伦理准则解释准则 2012，4.j.(1)。[证据](../../../sources/notes/asme2012canons.md#e4)
[^asme2012canons-e6]: ASME 伦理准则解释准则 2012，1.c.(3)。[证据](../../../sources/notes/asme2012canons.md#e6)
[^asmeethicalstandards-e1]: ASME，Ethical Standards，Ethical Obligations of Authors。[证据](../../../sources/notes/asmeethicalstandards.md#e1)
[^asmeethicalstandards-e3]: ASME，Ethical Standards，Ethical Obligations of Authors。[证据](../../../sources/notes/asmeethicalstandards.md#e3)
[^asmeethicalstandards-e4]: ASME，Ethical Standards，Ethical Obligations of Authors。[证据](../../../sources/notes/asmeethicalstandards.md#e4)
[^asmeethicalstandards-e5]: ASME，Ethical Standards，Ethical Obligations of Authors。[证据](../../../sources/notes/asmeethicalstandards.md#e5)
[^asmeethicalstandards-e6]: ASME，Ethical Standards，Ethical Obligations of Authors。[证据](../../../sources/notes/asmeethicalstandards.md#e6)
[^asme2024ethics-e1]: ASME 学会政策 P-15.7（2024），开头。[证据](../../../sources/notes/asme2024ethics.md#e1)
[^asme2024ethics-e2]: ASME 学会政策 P-15.7（2024），Fundamental Canons 第 1 条。[证据](../../../sources/notes/asme2024ethics.md#e2)
[^asme2024ethics-e4]: ASME 学会政策 P-15.7（2024），Fundamental Canons 第 4 条。[证据](../../../sources/notes/asme2024ethics.md#e4)
[^asme2024ethics-e5]: ASME 学会政策 P-15.7（2024），Fundamental Canons 第 5 条。[证据](../../../sources/notes/asme2024ethics.md#e5)
[^jcgm2008gum-e1]: JCGM 100:2008（GUM），0.1。[证据](../../../sources/notes/jcgm2008gum.md#e1)
[^jcgm2008gum-e2]: JCGM 100:2008（GUM），3.3.2。[证据](../../../sources/notes/jcgm2008gum.md#e2)
[^jcgm2008gum-e8]: JCGM 100:2008（GUM），7.1.4。[证据](../../../sources/notes/jcgm2008gum.md#e8)
[^jcgm2008gum-e9]: JCGM 100:2008（GUM），7.2.3。[证据](../../../sources/notes/jcgm2008gum.md#e9)
[^taylor1994nist-e2]: Taylor 与 Kuyatt 1994（NIST TN 1297），D.1.1.1。[证据](../../../sources/notes/taylor1994nist.md#e2)
[^taylor1994nist-e3]: Taylor 与 Kuyatt 1994（NIST TN 1297），D.1.2。[证据](../../../sources/notes/taylor1994nist.md#e3)
[^aiaaeditorialpolicy-e1]: AIAA，Editorial Policy Statement on Numerical and Experimental Accuracy，开头。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e1)
[^aiaaeditorialpolicy-e2]: AIAA，Editorial Policy Statement，开头。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e2)
[^aiaaeditorialpolicy-e3]: AIAA，Editorial Policy Statement，Estimation of Bias Uncertainty。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e3)
[^aiaaeditorialpolicy-e4]: AIAA，Editorial Policy Statement，Estimation of Precision Uncertainty。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e4)
[^aiaaeditorialpolicy-e5]: AIAA，Editorial Policy Statement，Statement of Total Uncertainty。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e5)
[^aiaaeditorialpolicy-e6]: AIAA，Editorial Policy Statement，Statement of Experimental Design。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e6)
[^aiaaeditorialpolicy-e7]: AIAA，Editorial Policy Statement，Statement of Code Verification Activities。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e7)
[^aiaaeditorialpolicy-e8]: AIAA，Editorial Policy Statement，Coverage Factor。[证据](../../../sources/notes/aiaaeditorialpolicy.md#e8)
[^jfenumaccuracy-e1]: 《流体工程杂志》数值精度编辑政策，简化声明。[证据](../../../sources/notes/jfenumaccuracy.md#e1)
[^jfenumaccuracy-e2]: 《流体工程杂志》数值精度编辑政策，第 4 条。[证据](../../../sources/notes/jfenumaccuracy.md#e2)
[^jfenumaccuracy-e3]: 《流体工程杂志》数值精度编辑政策，第 10 条。[证据](../../../sources/notes/jfenumaccuracy.md#e3)
[^jfenumaccuracy-e4]: 《流体工程杂志》数值精度编辑政策，第 1 条。[证据](../../../sources/notes/jfenumaccuracy.md#e4)
[^jfenumaccuracy-e5]: 《流体工程杂志》数值精度编辑政策，十条之后的说明。[证据](../../../sources/notes/jfenumaccuracy.md#e5)
[^jfenumaccuracy-e6]: 《流体工程杂志》数值精度编辑政策，第 5 条。[证据](../../../sources/notes/jfenumaccuracy.md#e6)
[^celik2008procedure-e1]: Celik 等人 2008，Preliminaries。[证据](../../../sources/notes/celik2008procedure.md#e1)
[^celik2008procedure-e2]: Celik 等人 2008，Step 2。[证据](../../../sources/notes/celik2008procedure.md#e2)
[^celik2008procedure-e3]: Celik 等人 2008，Preliminaries。[证据](../../../sources/notes/celik2008procedure.md#e3)
[^celik2008procedure-e4]: Celik 等人 2008，Preliminaries。[证据](../../../sources/notes/celik2008procedure.md#e4)
[^celik2008procedure-e5]: Celik 等人 2008，Step 5 之后的示例说明。[证据](../../../sources/notes/celik2008procedure.md#e5)
[^celik2008procedure-e6]: Celik 等人 2008，Discretization Error Bars。[证据](../../../sources/notes/celik2008procedure.md#e6)
[^oshamachineguarding-e1]: OSHA，Machine Guarding Overview。[证据](../../../sources/notes/oshamachineguarding.md#e1)
[^oshamachineguarding-e2]: OSHA，Machine Guarding Overview。[证据](../../../sources/notes/oshamachineguarding.md#e2)
[^oshalockout-e1]: OSHA，Control of Hazardous Energy (Lockout/Tagout)，What is hazardous energy?。[证据](../../../sources/notes/oshalockout.md#e1)
[^oshalockout-e2]: OSHA，Control of Hazardous Energy (Lockout/Tagout)，What can be done to control hazardous energy?。[证据](../../../sources/notes/oshalockout.md#e2)
[^cmu2025machineshop-e1]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），4.j。[证据](../../../sources/notes/cmu2025machineshop.md#e1)
[^cmu2025machineshop-e2]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），5.a。[证据](../../../sources/notes/cmu2025machineshop.md#e2)
[^cmu2025machineshop-e3]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），7.a。[证据](../../../sources/notes/cmu2025machineshop.md#e3)
[^cmu2025machineshop-e4]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），7.b.iii。[证据](../../../sources/notes/cmu2025machineshop.md#e4)
[^cmu2025machineshop-e5]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），7.c。[证据](../../../sources/notes/cmu2025machineshop.md#e5)
[^cmu2025machineshop-e6]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），7.o。[证据](../../../sources/notes/cmu2025machineshop.md#e6)
[^cmu2025machineshop-e7]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），7.t。[证据](../../../sources/notes/cmu2025machineshop.md#e7)
[^cmu2025machineshop-e8]: Carnegie Mellon University EHS，Machine Shop Safety Guideline（2025），7.m。[证据](../../../sources/notes/cmu2025machineshop.md#e8)
[^lisee2008conference-e1]: Lisée、Larivière 与 Archambault 2008，Methods。[证据](../../../sources/notes/lisee2008conference.md#e1)
[^lisee2008conference-e2]: Lisée、Larivière 与 Archambault 2008，Results（Figure 6 及其说明）。[证据](../../../sources/notes/lisee2008conference.md#e2)
[^lisee2008conference-e3]: Lisée、Larivière 与 Archambault 2008，Results。[证据](../../../sources/notes/lisee2008conference.md#e3)
[^bjork2013publishing-e1]: Björk 与 Solomon 2013，摘要。[证据](../../../sources/notes/bjork2013publishing.md#e1)
[^bjork2013publishing-e2]: Björk 与 Solomon 2013，§2 Methods。[证据](../../../sources/notes/bjork2013publishing.md#e2)
[^bjork2013publishing-e3]: Björk 与 Solomon 2013，§3 Results。[证据](../../../sources/notes/bjork2013publishing.md#e3)
[^bjork2013publishing-e4]: Björk 与 Solomon 2013，附录 Publication Time in Months by Discipline 表。[证据](../../../sources/notes/bjork2013publishing.md#e4)
[^bjork2013publishing-e5]: Björk 与 Solomon 2013，§4 Discussion。[证据](../../../sources/notes/bjork2013publishing.md#e5)
