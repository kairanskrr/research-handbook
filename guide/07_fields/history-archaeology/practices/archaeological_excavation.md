# 考古发掘与野外调查

> **状态**：初稿，待审阅 · **最后更新**：2026-10-08

本文讲**考古田野工作**怎么做：从写研究设计、先做不挖土的调查，到按地层发掘、逐单位记录，再到发掘后的评估、归档和写报告。考古学的伦理原则（守护遗址、尊重后裔群体、不做买卖）和英国 CIfA 发掘标准的基本要求，已在[历史与考古学科概况](../README.md#考古学守护遗址和社区合作)讲过，这里不重复。野外的安全、后勤和仪器校准等通用做法，见地球与环境科学《野外观测研究》的[安全和后勤](../../../06_methods/field_study.md#第四步安全和后勤)和[仪器校准](../../../06_methods/field_study.md#第五步仪器和现场校准)两步。

**适用范围。** 这是考古学特有的研究实践，只适用于考古田野工作。在本手册的套路划分里，它主要服务[观察描述](../../../05_research-strategies/observe_describe.md)：记录遗存是什么样的，再加以解释（见[学科概况的常用套路与证据标准](../README.md#常用套路与证据标准)）。研究设计、效度和计划等各学科共通的部分，见主线[从研究问题到证据清单](../../../02_from-project-to-study/01_question-to-evidence.md)和[形成研究计划](../../../01_from-interest-to-project/04_research-plan.md) `[本项目分析]`。**常服务的套路**：套路页暂未列出。

**先说清本文资料的来历。** 它们来自几个国家和一位学者，各有各的适用范围，都不是全学科的统一规定 `[本项目分析]`。在其他国家做发掘，许可、出土物归属和归档都按当地法规办；CIfA 的指南自己也要求遵守工作所在地的法律和本地指南[^cifa2023excavation-e12]。

- **英国 CIfA**：英国特许考古学家协会（Chartered Institute for Archaeologists，英国考古从业者的职业组织）的四份标准和指南，分别管野外评估、发掘、地球物理勘探和档案。它们是对**本会会员**的要求 `[本项目分析，依据各文件的版本说明]`，针对在英国和马恩岛的工作[^cifa2020archives-e12]。
- **英格兰 Historic England**：英格兰历史遗产局（英格兰的政府遗产机构）的项目管理指南。由它**资助**的研究项目必须遵守，其他人可以参考[^historicengland2015morphe-e1]。
- **美国 SAA**：美国考古学会（Society for American Archaeology）2024 年的伦理原则，是这个学会对考古学家的要求。
- **美国内政部 1983 年标准**：美国内政部 1983 年在《联邦公报》上发布的考古记录标准和指南，用于美国联邦层面的历史保护工作 `[本项目分析，依据其版本说明]`。它已有四十多年，部分做法可能已更新。
- **Harris 的地层学**：Edward Harris 的《考古地层学原理》（1989 年第 2 版），"哈里斯矩阵"就出自这本书。这是**一位学者提出的方法体系**，不是哪个机构的规定 `[本项目分析]`。

**读完本文，你应该能：**

- 说清案头研究、非侵入调查、野外评估、发掘各回答什么问题，为什么先做不挖土的那几种；
- 写出一份能被检查的项目设计书；
- 按地层发掘，给每个地层单位编号、填表、画图、记录地层关系；
- 分清"地层的先后"和"地层的年代"，正确使用出土物定年；
- 知道发掘结束后还要做评估、归档和报告，项目才算完成。

---

## 1. 这是什么研究，什么时候用

考古田野工作是到现场去，找出、记录并解释埋在地下或留在地表的人类活动遗存。它和别的研究最大的不同是：**发掘会毁掉证据本身**。Harris 说，考古地层的形成不可逆，一个地层单位一旦形成，只会被改变或消失，不能再造[^harris1989principles-e1]。挖掉的土放不回去，所以记录就是挖完之后唯一剩下的证据 `[本项目分析]`。

| 工作类型 | 回答什么问题 | 会破坏遗址吗 | 依据 |
|---|---|---|---|
| 案头研究 | 这里以前发现过什么、有什么历史记载 | 不会 | `[本项目分析]`，本文资料未详细涉及 |
| 非侵入调查（地球物理勘探等） | 地下可能有什么 | 不会 | 英国 CIfA 物探标准[^cifa2020geophysics-e1] |
| 野外评估（可含试掘） | 这片区域有没有遗存 | 可能会 | 英国 CIfA 评估标准[^cifa2023evaluation-e1] |
| 发掘 | 带着明确研究目标，检查、记录、解释遗存 | 会 | 见[学科概况](../README.md#证据在这里指什么)对 CIfA 定义的介绍 |
| 藏品研究 | 用已有的出土物和记录回答问题 | 不会 | 美国 SAA[^saa2024principles-e11] |

**怎么判断该做哪一种。** 几份资料方向一致：**能不挖就先不挖**。美国 SAA 说，研究设计要优先分析已有藏品，新的田野工作要说明理由（详见[学科概况](../README.md#考古学守护遗址和社区合作)）[^saa2024principles-e11]。英国 CIfA 的评估指南说，只要可能，先考虑非侵入方法，确有必要才用侵入性手段[^cifa2023evaluation-e2]。美国内政部 1983 年的指南说，能用非破坏方法时，就不要用破坏性方法[^nps1983standards-e7]。所以，先问"已有的藏品和记录能不能回答我的问题"，再问"不挖土的调查能不能回答"，最后才是发掘 `[本项目分析]`。

---

## 2. 怎么做

### 第 1 步：写研究设计和项目设计书

**怎么做。** 动手之前，把目标、方法、记录方式、采样和测年策略、归档计划写成一份文件，英国 CIfA 的文件里叫项目设计书（project design）。美国内政部 1983 年的指南说，只有先定出明确的目标和达到目标的方法，才能开展考古记录工作[^nps1983standards-e2]。CIfA 的发掘指南列出了设计书应包含的内容，下面三项和研究质量关系最直接 `[本项目分析：条目为本项目挑选]`：调查方法，包括环境采样和科学测年的策略[^cifa2023excavation-e10]；记录方法，包括空间数据的采集标准[^cifa2023excavation-e4]；归档策略，包括数据管理计划、哪些材料保留、当地收藏机构的要求[^cifa2023excavation-e8]。英格兰历史遗产局的项目管理指南（适用于它资助的项目）把"启动"阶段定为设计阶段，并要求把不确定性、潜在问题和机会记进**风险日志**[^historicengland2015morphe-e2]。

**为什么。** 设计书是之后检查工作的基准：做完了，拿它对照，看做到没有（CIfA）[^cifa2023excavation-e9]。

**容易错在哪里。** 套模板。CIfA 两份指南都提醒，设计书要针对本项目，所选方法要符合可能发现的遗存的性质、范围、保存状况和重要性，模板要慎用[^cifa2023excavation-e9][^cifa2023evaluation-e3]。

### 第 2 步：先做不挖土的调查

**怎么做。** 地球物理勘探（geophysical survey，简称物探，例如测磁、测电阻、探地雷达 `[本项目分析：举例]`）用非侵入、非破坏的技术，判断地下有没有可能由遗存引起的"异常"[^cifa2020geophysics-e1]。物探结果可以用来决定试掘或发掘放在哪里 `[本项目分析]`。

**为什么。** 不破坏遗址，符合上一节"能不挖就不挖"的原则[^cifa2023evaluation-e2]。美国内政部 1983 年的考古记录标准也要求：适当时就用非破坏性技术，所选方法要让结果在必要时可以核实[^nps1983standards-e1]。

**容易错在哪里。**

- **把异常当成遗迹。** CIfA 的物探指南说，单凭物探数据往往无法确定异常的成因，报告要写清推断的不确定程度[^cifa2020geophysics-e2]。
- **忘了物探也要许可。** 这份英国指南提到，在列级古迹（scheduled monuments，英国受法律保护的古迹）等受保护地点做物探，需要"第 42 条许可"（Section 42 Licence）[^cifa2020geophysics-e3]。

### 第 3 步：办许可，和土地所有者、社区协商

**怎么做。**

- **守法。** 美国 SAA 要求考古学家遵守所有法律法规，并尽可能和受影响的群体合作，达成双方都认可、都受益的结果[^saa2024principles-e3]。具体要申请哪些许可证、找哪个部门，各国法律不同，**本文资料未涉及**，以当地主管部门、收藏机构和导师的要求为准。
- **弄清出土物归谁。** 以英国为例：在英格兰、威尔士、北爱尔兰和马恩岛，除非另有法律规定，出土物归土地所有者[^cifa2020archives-e11]。CIfA 要求在项目计划阶段就联系将来接收档案的博物馆，并在设计书里写清入藏安排[^cifa2020archives-e10]。
- **和后裔群体、当地群体协商。** 美国 SAA 说，许多后裔群体和原住民社区把考古记录视为自己的遗产，应当让他们参与有关记录和研究的决定[^saa2024principles-e13]。美国内政部 1983 年的指南说，调查阶段对当地群体（如美洲原住民群体）关切的回应，到发掘阶段也要保持，因为发掘通常会扰动遗址[^nps1983standards-e4]。

### 第 4 步：定发掘策略和采样方案

**怎么做。**

- **承认挖不全。** 美国内政部 1983 年的指南说，考古调查很少能收集和记录所有可能的数据[^nps1983standards-e3]。所以要事先想好挖哪里、挖多少 `[本项目分析]`；CIfA 要求把调查方法和环境采样策略写进设计书[^cifa2023excavation-e10]。
- **采样前后一致。** 同一遗址分几期工作时，最好保持抽样设计一致（美国内政部）[^nps1983standards-e6]，否则几期数据很难放在一起比 `[本项目分析]`。
- **环境样品在现场就处理一部分。** CIfA 建议适当时在野外阶段就处理环境样品，帮助判断遗址的重要性和保存状况[^cifa2023excavation-e13]。
- **规模和重要性相称。** 发掘后的分析、发表和档案的规模，要和遗存的重要性、研究潜力相称（CIfA）[^cifa2023excavation-e21]。

**允许中途调整，但要留下记录。** 美国内政部 1983 年的指南说，野外执行研究设计要有弹性，能应对意外发现和现场条件的变化[^nps1983standards-e5]。英格兰历史遗产局的指南把项目分成若干执行阶段，每段结束时对照目标检查，必要时更新设计书[^historicengland2015morphe-e3]，认为这种灵活做法适合难以预料的历史环境研究[^historicengland2015morphe-e4]。CIfA 则要求任何改动都在团队内传达，并由各相关方书面同意[^cifa2023excavation-e11]。

### 第 5 步：按地层发掘，逐个单位记录

这是发掘的核心 `[本项目分析]`。下面的做法来自 Harris 的书，是他个人提出的一套方法；你所在单位的记录系统可能有自己的规定 `[本项目分析]`。

**先认识两个概念。** 一是**叠压定律**：在保持原状的地层中，上面的单位较晚，下面的较早[^harris1989principles-e2]。二是**地层单位**：Harris 把它分成两类，一类是堆积层，一类是"界面"[^harris1989principles-e1]。界面例如挖坑留下的坑壁和坑底；英国的记录系统常把每个单位叫一个 context（"堆积单位"）`[本项目分析]`。

**怎么做。**

1. **按地层挖，不按固定深度挖。** Harris 说，有明显地层时必须按地层挖[^harris1989principles-e3]；在地层清楚的遗址上按人为深度一层层挖，等于毁掉自己要找的原始数据[^harris1989principles-e4]。
2. **每个单位都编号，只用一套号。** 从最晚的单位往下挖，每个单位都编号；记录里只用一套编号就够了[^harris1989principles-e5]。
3. **每个单位填一张表。** 地层关系最好记在预先印好的表格上，要找三种关系：哪些单位在它上面，哪些在它下面，哪些和它可以对应为同一单位[^harris1989principles-e6]。
4. **挖之前先画平面图。** 动手挖一个单位之前，先画它表面的平面图；堆积复杂、相互重叠的遗址，每个单位都单独画一张（单层平面图）[^harris1989principles-e7]。
5. **边挖边搭地层序列图。** 发掘过程中就可以一边挖一边在纸上搭建地层序列[^harris1989principles-e9]。这种图就是"哈里斯矩阵"，用方框和连线表示各单位的先后；边挖边搭，有矛盾能当场回去核对 `[本项目分析]`。

**为什么。** 每个单位单独画图，挖完后才能用这些图把遗址"重建"出来，再合成综合平面图[^harris1989principles-e8]。

**容易错在哪里。** 不是所有遗址都要每层单独画图：Harris 说，地层很简单的遗址，综合平面图就够了[^harris1989principles-e8]。表格格式和填写规则，各单位常有自己的记录手册 `[本项目分析]`；本文没有找到这类手册（如伦敦博物馆《考古现场手册》）可公开的原文，以你所在单位的手册为准。

### 第 6 步：记录照片、图纸、出土物和样品

**怎么做。** 英国 CIfA 的档案标准要求：所有图纸和照片都标上项目编号，适用时标明对象、比例尺、位置和方向[^cifa2020archives-e6]；纸质和数字记录都用一致、有说明的术语[^cifa2020archives-e5]；出土物按公认标准收集、分类、清洗、标记、登记和包装[^cifa2020archives-e8]；所有数字材料都做备份[^cifa2020archives-e7]。美国内政部 1983 年的指南提出两条总要求：野外记录要尽量让别人能独立解读；记录的格式和详细程度要统一[^nps1983standards-e9]。

**容易错在哪里。** 只记"有用的"出土物。Harris 说，不管出土物是原生的、后来渗入的还是更早残留的，野外都要用同样的方式记录，之后才能区分[^harris1989principles-e11]。另外，CIfA 的档案标准明确写着：健康和安全优先于考古要求[^cifa2020archives-e13]。

### 第 7 步：年代证据：先排先后，再定年代

**怎么做。**

1. **先用地层排出先后。** Harris 说，一个单位的绝对年代，永远改变不了它在地层序列中的位置[^harris1989principles-e13]。如果年代和序列对不上，要回头查是年代有问题还是记录有问题 `[本项目分析]`。
2. **用出土物定年时，看最晚的那件。** Harris 说，地层中最晚的器物最接近地层的年代。它给出一条"不早于"的界限（拉丁文 terminus post quem，意思是"在此之后"）：地层一定晚于这件器物的制造时间。但前提是地层没有被后来的东西侵入[^harris1989principles-e12]。
3. **警惕残留物和渗入物。** 残留物比所在地层早得多；渗入物比所在地层晚，是后来混进去的[^harris1989principles-e10]。
4. **科学测年要事先计划。** CIfA 要求把科学测年策略写进设计书[^cifa2023excavation-e10]。放射性碳测年怎样选样、怎样建模，本文资料未涉及，见下文"延伸阅读"中英格兰历史遗产局的测年指南。

### 第 8 步：发掘后评估，再决定怎么分析

**怎么做。** 英国 CIfA 把发掘之后分成两步：先**评估**，再**分析**。

- 野外工作之后（合适时在进行中），对照设计书评估发现：研究目标达成了多少、还能达成多少，有没有新问题要写进更新后的设计书[^cifa2023excavation-e14]。
- 评估报告要说明：现场档案里有多少数据、质量怎样，这些数据回答研究目标的潜力有多大，以及对后续分析和数据保存的建议[^cifa2023excavation-e15]。
- 评估时发现值得深入研究的材料，就更新设计书，即使研究目标没变[^cifa2023excavation-e16]。
- 正式成果要把各类专家分析的结果和遗址的地层序列整合起来，免得漏掉重要数据[^cifa2023excavation-e17]。

**为什么。** 先看清"手里有什么、值得做什么"，再投入分析的时间和经费 `[本项目分析]`。美国内政部 1983 年的指南还提醒：没有分析的数据也要记录、保存好，方便将来使用[^nps1983standards-e8]。

### 第 9 步：整理档案，交给收藏机构

**怎么做。** 先弄清档案包括什么：英国 CIfA 的定义是考古记录的全部，即出土物、样品、数字记录，以及文字、图纸和照片记录[^cifa2020archives-e1]。开工前就在设计书里写清筛选策略、数据管理计划和最终存放的收藏机构（CIfA）[^cifa2020archives-e4]；美国内政部 1983 年的指南也要求在规划阶段就安排好保管[^nps1983standards-e11]。英格兰历史遗产局的指南说，档案要在整个项目过程中边产生边整理、边编索引[^historicengland2015morphe-e5]，最终应当能让独立的第三方查询核对[^historicengland2015morphe-e6]。

**为什么。** 项目档案是理解已发表解释的钥匙[^cifa2020archives-e2]。CIfA 说，档案成功移交并能完全查阅之前，项目不算完成[^cifa2020archives-e3]。美国 SAA 也要求按现行专业标准，确保记录得到归档、保管和发表[^saa2024principles-e8]。

### 第 10 步：写报告，及时公开

**怎么做。** 发掘报告不一定正式出版；CIfA 的档案指南把这类报告也算作"灰色文献"（grey literature，没有经过正式出版渠道的报告）[^cifa2020archives-e9]。它同样要写好：

- **写明档案在哪。** CIfA 要求项目报告（包括灰色文献和在线登记）写明档案存放机构和入藏编号[^cifa2020archives-e9]。
- **写明偏离和可信度。** CIfA 的评估指南要求报告写明所用方法，包括偏离设计书的地方[^cifa2023evaluation-e4]；结论要给出所用技术的可信度评级，以及能提高可信度的后续工作建议[^cifa2023evaluation-e5]。
- **让别人能找回位置、能质疑解释。** 图上要有准确的空间信息，让以后的人能找回调查区域[^cifa2023evaluation-e6]；报告要有足够的数据和档案出处，让别人能质疑其中的解释[^cifa2023excavation-e17]。
- **交出去、放上网。** CIfA 要求在合理的保密约定之外，按设计书的时间把报告交给国家或地方的记录机构[^cifa2023excavation-e18]，电子版放到网上[^cifa2023excavation-e19]。美国 SAA 要求及时分享和发表，并尽可能开放获取[^saa2024principles-e9]。

**容易错在哪里。** 公开得太细。美国 SAA 要求发表时考虑保护敏感信息[^saa2024principles-e10]；美国内政部 1983 年的指南说，具体位置等信息公开后可能招来人为破坏[^nps1983standards-e10]。一种做法是公开版本只写到大致位置，精确坐标留在档案里，按收藏机构的规定查阅 `[本项目分析]`。

---

## 3. 检查清单

下面各项依据英国 CIfA 的标准和指南（对其会员）、美国 SAA 的伦理原则、美国内政部 1983 年的指南和 Harris 的方法整理。其他国家以本地规定为准 `[本项目分析]`。

**必须做到**

- [ ] 开工前有针对本项目的设计书，写清目标、方法、记录、采样和测年、归档策略（CIfA）[^cifa2023excavation-e10][^cifa2023excavation-e4][^cifa2023excavation-e8]
- [ ] 遵守当地法律，办齐许可（SAA、CIfA）[^saa2024principles-e3][^cifa2023excavation-e12]
- [ ] 有明显地层时按地层挖，每个单位编号、记录上下关系（Harris）[^harris1989principles-e3][^harris1989principles-e6]
- [ ] 图纸和照片标明项目编号、比例尺、位置和方向（CIfA）[^cifa2020archives-e6]
- [ ] 设计书的改动经各方书面同意（CIfA）[^cifa2023excavation-e11]
- [ ] 产出报告和一套稳定、有序、可查阅的档案（CIfA）[^cifa2023excavation-e1]；报告写明档案存放机构和编号[^cifa2020archives-e9]

**做到更好**

- [ ] 先分析已有藏品、先考虑非侵入方法，再决定是否发掘（SAA、CIfA）[^saa2024principles-e11][^cifa2023evaluation-e2]
- [ ] 让后裔群体和原住民社区参与有关的决定（SAA）[^saa2024principles-e13]
- [ ] 发掘过程中就搭建地层序列图（Harris）[^harris1989principles-e9]
- [ ] 在野外阶段就处理一部分环境样品（CIfA）[^cifa2023excavation-e13]
- [ ] 电子版报告放到网上，尽可能开放获取（CIfA、SAA）[^cifa2023excavation-e19][^saa2024principles-e9]

**这些情况可以不做，不算缺陷**

- 地层简单的遗址，不必每个单位单独画平面图，用综合平面图即可（Harris）[^harris1989principles-e8]。
- 不是每次发掘都要出一本专著：分析和发表的规模与遗存的重要性相称即可（CIfA）[^cifa2023excavation-e21]。
- 可以偏离通用指南，但要有清楚的理由并正式记录（CIfA）[^cifa2023excavation-e20]。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 照搬别的项目的设计书模板 | 设计书是检查工作的基准，要针对本项目（CIfA）[^cifa2023excavation-e9][^cifa2023evaluation-e3] |
| 能用藏品或物探回答的问题，直接去挖 | 地层不可再造（Harris）[^harris1989principles-e1]；SAA 要求新田野工作说明理由[^saa2024principles-e11] |
| 把物探异常直接当成遗迹 | 单凭物探往往无法确定异常成因（CIfA）[^cifa2020geophysics-e2] |
| 地层清楚却按固定深度挖 | 会毁掉要找的原始数据（Harris）[^harris1989principles-e4] |
| 只记"重要"的出土物 | 所有出土物要用同样方式记录，之后才能区分（Harris）[^harris1989principles-e11] |
| 拿一件器物的年代直接当地层的年代 | 地层只能晚于最晚器物的年代，前提是没有后来的东西侵入；还要排除残留物（Harris）[^harris1989principles-e12][^harris1989principles-e10] |
| 现场随意改方案、不留记录 | 改动要各方书面同意（CIfA）[^cifa2023excavation-e11] |
| 发掘结束才想档案交给谁 | 入藏安排要在计划阶段谈好（CIfA）[^cifa2020archives-e10]；档案移交前项目不算完成[^cifa2020archives-e3] |
| 报告只写解释，不给数据和档案出处 | 别人无法质疑和核对（CIfA）[^cifa2023excavation-e17] |
| 报告公开精确的遗址位置 | 可能招来人为破坏（美国内政部 1983）[^nps1983standards-e10]；SAA 要求保护敏感信息[^saa2024principles-e10] |

---

## 5. 延伸阅读

- **Harris，Principles of Archaeological Stratigraphy（第 2 版，1989）**：作者网站 harrismatrix.com 免费下载。讲地层单位、叠压关系、平面图和哈里斯矩阵；第 12 章是发掘现场地层记录的提纲，新手可以先读这一章。
- **CIfA，野外评估、发掘、地球物理勘探、考古档案四份标准和指南**：archaeologists.net 免费下载。针对英国的职业要求，设计书和报告的内容清单可以拿来当检查表 `[本项目分析]`。
- **Historic England，MoRPHE Project Managers' Guide（2015）**：讲研究项目怎样分阶段、设检查点、记风险日志。
- **美国内政部，Secretary of the Interior's Standards and Guidelines for Archeology and Historic Preservation（1983）**：美国国家公园管理局网站免费下载，"考古记录"部分讲研究设计、野外记录、报告和保管。
- **Historic England，Radiocarbon Dating and Chronological Modelling**：英格兰历史遗产局的放射性碳测年和年代建模指南，计划测年时查阅（本文未摘录其内容）。
- **考古数据服务中心（Archaeology Data Service）的 Guides to Good Practice**：英国的考古数字档案机构发布，讲数字数据怎样创建、整理和存档（本文未摘录其内容）。
- 研究设计的通用原则见主线章节[从研究问题到证据清单](../../../02_from-project-to-study/01_question-to-evidence.md)；从单个遗址怎样推广结论，可参考[案例研究](../../../06_methods/case_study.md)。

[^cifa2023excavation-e1]: CIfA 2023，发掘标准，开头。[证据](../../../../sources/notes/cifa2023excavation.md#e1)
[^cifa2023excavation-e9]: CIfA 2023，发掘通用指南 2.2。[证据](../../../../sources/notes/cifa2023excavation.md#e9)
[^cifa2023excavation-e10]: CIfA 2023，发掘通用指南 2.12 (h)。[证据](../../../../sources/notes/cifa2023excavation.md#e10)
[^cifa2023excavation-e4]: CIfA 2023，发掘通用指南 2.12 (i)。[证据](../../../../sources/notes/cifa2023excavation.md#e4)
[^cifa2023excavation-e8]: CIfA 2023，发掘通用指南 2.12 (l)。[证据](../../../../sources/notes/cifa2023excavation.md#e8)
[^cifa2023excavation-e11]: CIfA 2023，发掘通用指南 2.9。[证据](../../../../sources/notes/cifa2023excavation.md#e11)
[^cifa2023excavation-e12]: CIfA 2023，发掘通用指南 1.4。[证据](../../../../sources/notes/cifa2023excavation.md#e12)
[^cifa2023excavation-e13]: CIfA 2023，发掘通用指南 3.3。[证据](../../../../sources/notes/cifa2023excavation.md#e13)
[^cifa2023excavation-e14]: CIfA 2023，发掘通用指南 3.4。[证据](../../../../sources/notes/cifa2023excavation.md#e14)
[^cifa2023excavation-e15]: CIfA 2023，发掘通用指南 4.5。[证据](../../../../sources/notes/cifa2023excavation.md#e15)
[^cifa2023excavation-e16]: CIfA 2023，发掘通用指南 4.3。[证据](../../../../sources/notes/cifa2023excavation.md#e16)
[^cifa2023excavation-e17]: CIfA 2023，发掘通用指南 5.3。[证据](../../../../sources/notes/cifa2023excavation.md#e17)
[^cifa2023excavation-e18]: CIfA 2023，发掘通用指南 5.4。[证据](../../../../sources/notes/cifa2023excavation.md#e18)
[^cifa2023excavation-e19]: CIfA 2023，发掘通用指南 5.5。[证据](../../../../sources/notes/cifa2023excavation.md#e19)
[^cifa2023excavation-e20]: CIfA 2023，发掘通用指南 1.5。[证据](../../../../sources/notes/cifa2023excavation.md#e20)
[^cifa2023excavation-e21]: CIfA 2023，发掘通用指南 3.2。[证据](../../../../sources/notes/cifa2023excavation.md#e21)
[^cifa2023evaluation-e1]: CIfA 2023，野外评估标准，定义。[证据](../../../../sources/notes/cifa2023evaluation.md#e1)
[^cifa2023evaluation-e2]: CIfA 2023，野外评估通用指南 2.8。[证据](../../../../sources/notes/cifa2023evaluation.md#e2)
[^cifa2023evaluation-e3]: CIfA 2023，野外评估通用指南 2.2。[证据](../../../../sources/notes/cifa2023evaluation.md#e3)
[^cifa2023evaluation-e4]: CIfA 2023，野外评估通用指南 3.9 (c)。[证据](../../../../sources/notes/cifa2023evaluation.md#e4)
[^cifa2023evaluation-e5]: CIfA 2023，野外评估通用指南 3.9 (f)。[证据](../../../../sources/notes/cifa2023evaluation.md#e5)
[^cifa2023evaluation-e6]: CIfA 2023，野外评估通用指南 3.9 (e)。[证据](../../../../sources/notes/cifa2023evaluation.md#e6)
[^cifa2020archives-e1]: CIfA 2020，考古档案标准，定义。[证据](../../../../sources/notes/cifa2020archives.md#e1)
[^cifa2020archives-e2]: CIfA 2020，考古档案标准，目的。[证据](../../../../sources/notes/cifa2020archives.md#e2)
[^cifa2020archives-e3]: CIfA 2020，考古档案指南 3.1.1。[证据](../../../../sources/notes/cifa2020archives.md#e3)
[^cifa2020archives-e4]: CIfA 2020，考古档案指南 3.3.1、3.3.2。[证据](../../../../sources/notes/cifa2020archives.md#e4)
[^cifa2020archives-e5]: CIfA 2020，考古档案指南 3.4.3。[证据](../../../../sources/notes/cifa2020archives.md#e5)
[^cifa2020archives-e6]: CIfA 2020，考古档案指南 3.4.4。[证据](../../../../sources/notes/cifa2020archives.md#e6)
[^cifa2020archives-e7]: CIfA 2020，考古档案指南 3.4.7。[证据](../../../../sources/notes/cifa2020archives.md#e7)
[^cifa2020archives-e8]: CIfA 2020，考古档案指南 3.4.8。[证据](../../../../sources/notes/cifa2020archives.md#e8)
[^cifa2020archives-e9]: CIfA 2020，考古档案指南 3.4.15。[证据](../../../../sources/notes/cifa2020archives.md#e9)
[^cifa2020archives-e10]: CIfA 2020，考古档案指南 3.8.1。[证据](../../../../sources/notes/cifa2020archives.md#e10)
[^cifa2020archives-e11]: CIfA 2020，考古档案指南 3.8.2。[证据](../../../../sources/notes/cifa2020archives.md#e11)
[^cifa2020archives-e12]: CIfA 2020，考古档案指南 1 Introduction。[证据](../../../../sources/notes/cifa2020archives.md#e12)
[^cifa2020archives-e13]: CIfA 2020，考古档案指南 3.4.14。[证据](../../../../sources/notes/cifa2020archives.md#e13)
[^cifa2020geophysics-e1]: CIfA 2020，地球物理勘探标准，定义。[证据](../../../../sources/notes/cifa2020geophysics.md#e1)
[^cifa2020geophysics-e2]: CIfA 2020，地球物理勘探指南，附录 2。[证据](../../../../sources/notes/cifa2020geophysics.md#e2)
[^cifa2020geophysics-e3]: CIfA 2020，地球物理勘探指南，附录 1。[证据](../../../../sources/notes/cifa2020geophysics.md#e3)
[^historicengland2015morphe-e1]: Historic England 2015，MoRPHE，Summary。[证据](../../../../sources/notes/historicengland2015morphe.md#e1)
[^historicengland2015morphe-e2]: Historic England 2015，MoRPHE，1.1。[证据](../../../../sources/notes/historicengland2015morphe.md#e2)
[^historicengland2015morphe-e3]: Historic England 2015，MoRPHE，1.1。[证据](../../../../sources/notes/historicengland2015morphe.md#e3)
[^historicengland2015morphe-e4]: Historic England 2015，MoRPHE，2.5。[证据](../../../../sources/notes/historicengland2015morphe.md#e4)
[^historicengland2015morphe-e5]: Historic England 2015，MoRPHE，2.5.3。[证据](../../../../sources/notes/historicengland2015morphe.md#e5)
[^historicengland2015morphe-e6]: Historic England 2015，MoRPHE，2.5.3。[证据](../../../../sources/notes/historicengland2015morphe.md#e6)
[^harris1989principles-e1]: Harris 1989，第 6 章。[证据](../../../../sources/notes/harris1989principles.md#e1)
[^harris1989principles-e2]: Harris 1989，第 5 章，叠压定律。[证据](../../../../sources/notes/harris1989principles.md#e2)
[^harris1989principles-e3]: Harris 1989，第 12 章。[证据](../../../../sources/notes/harris1989principles.md#e3)
[^harris1989principles-e4]: Harris 1989，第 3 章。[证据](../../../../sources/notes/harris1989principles.md#e4)
[^harris1989principles-e5]: Harris 1989，第 12 章。[证据](../../../../sources/notes/harris1989principles.md#e5)
[^harris1989principles-e6]: Harris 1989，第 12 章。[证据](../../../../sources/notes/harris1989principles.md#e6)
[^harris1989principles-e7]: Harris 1989，第 12 章。[证据](../../../../sources/notes/harris1989principles.md#e7)
[^harris1989principles-e8]: Harris 1989，第 9 章。[证据](../../../../sources/notes/harris1989principles.md#e8)
[^harris1989principles-e9]: Harris 1989，第 5 章。[证据](../../../../sources/notes/harris1989principles.md#e9)
[^harris1989principles-e10]: Harris 1989，第 11 章。[证据](../../../../sources/notes/harris1989principles.md#e10)
[^harris1989principles-e11]: Harris 1989，第 11 章。[证据](../../../../sources/notes/harris1989principles.md#e11)
[^harris1989principles-e12]: Harris 1989，第 11 章。[证据](../../../../sources/notes/harris1989principles.md#e12)
[^harris1989principles-e13]: Harris 1989，第 6 章。[证据](../../../../sources/notes/harris1989principles.md#e13)
[^nps1983standards-e1]: 美国内政部 1983，考古记录标准 II。[证据](../../../../sources/notes/nps1983standards.md#e1)
[^nps1983standards-e2]: 美国内政部 1983，考古记录指南，研究设计。[证据](../../../../sources/notes/nps1983standards.md#e2)
[^nps1983standards-e3]: 美国内政部 1983，考古记录指南，记录计划。[证据](../../../../sources/notes/nps1983standards.md#e3)
[^nps1983standards-e4]: 美国内政部 1983，考古记录指南，记录计划。[证据](../../../../sources/notes/nps1983standards.md#e4)
[^nps1983standards-e5]: 美国内政部 1983，考古记录指南，野外工作。[证据](../../../../sources/notes/nps1983standards.md#e5)
[^nps1983standards-e6]: 美国内政部 1983，考古记录指南，野外工作。[证据](../../../../sources/notes/nps1983standards.md#e6)
[^nps1983standards-e7]: 美国内政部 1983，考古记录指南，野外工作。[证据](../../../../sources/notes/nps1983standards.md#e7)
[^nps1983standards-e8]: 美国内政部 1983，考古记录指南，野外工作。[证据](../../../../sources/notes/nps1983standards.md#e8)
[^nps1983standards-e9]: 美国内政部 1983，考古记录指南，野外工作。[证据](../../../../sources/notes/nps1983standards.md#e9)
[^nps1983standards-e10]: 美国内政部 1983，考古记录指南，报告。[证据](../../../../sources/notes/nps1983standards.md#e10)
[^nps1983standards-e11]: 美国内政部 1983，考古记录指南，保管。[证据](../../../../sources/notes/nps1983standards.md#e11)
[^saa2024principles-e3]: SAA 2024，Principle No. 2。[证据](../../../../sources/notes/saa2024principles.md#e3)
[^saa2024principles-e13]: SAA 2024，Principle No. 5。[证据](../../../../sources/notes/saa2024principles.md#e13)
[^saa2024principles-e11]: SAA 2024，Principle No. 7。[证据](../../../../sources/notes/saa2024principles.md#e11)
[^saa2024principles-e9]: SAA 2024，Principle No. 6。[证据](../../../../sources/notes/saa2024principles.md#e9)
[^saa2024principles-e10]: SAA 2024，Principle No. 6。[证据](../../../../sources/notes/saa2024principles.md#e10)
[^saa2024principles-e8]: SAA 2024，Principle No. 5。[证据](../../../../sources/notes/saa2024principles.md#e8)
