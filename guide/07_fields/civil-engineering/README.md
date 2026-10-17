# 土木工程：学科概况

本文讲土木工程（结构、岩土、交通、水资源、施工管理等方向）的研究实际怎样运转：大尺度试验和现场试验要排期、要审批、要管安全；数值模型要和试验对得上；一部分成果最终会进入设计规范和标准。各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)。本学科常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。这里只写本学科特有的东西。

本文引用的规定都来自美国的具体单位：美国土木工程师学会（American Society of Civil Engineers，ASCE）的准则、期刊政策和标准；美国国家科学基金会资助的两个试验设施各自的文件；美国国家标准与技术研究院 2008 财年的一份预算说明。它们只代表这些单位在当时的做法，不是土木工程的通用规矩。中国和其他国家的学会、期刊、规范体系和你所在单位的规定可能不同，以本地规定为准。

**读完本文，你应该能：**

- 说清大尺度试验、现场试验和数值模拟在本领域研究里各自的位置；
- 分清模型的"验证""确认"和"校准"，不把调参数当成证明模型可靠；
- 理解研究成果和设计规范、标准之间的关系；
- 以 ASCE 为例，知道伦理准则、数据可得性声明和会议论文转期刊有哪些规定；
- 在大尺度试验和现场试验中把安全放在进度前面。

---

## 本领域研究怎样运转

土木工程下面的方向，研究方式差别很大：结构方向常做构件和整体结构的加载试验；岩土方向既做试验室土工试验，也做现场试验；交通方向大量用交通数据和模型；水资源方向以水文数据和计算模型为主；施工管理方向常和企业合作做案例和调查。下面的内容不一定适用于每个方向，进组后先问导师本方向的惯例。

### 大尺度试验：排队、审批、准备都要很久

结构和岩土方向的一部分研究要做大尺度甚至足尺（和真实结构一样大）的试验，这类试验往往要用到专门的大型试验设施。下面以美国国家科学基金会资助的**自然灾害工程研究基础设施**（Natural Hazards Engineering Research Infrastructure，NHERI）的两个设施为例。这只是两家设施在各自文件里写的做法，其他试验室的流程以本单位规定为准。

**利哈伊大学的实时多向试验设施**（做大尺度结构试验；依据是它 2016 年 11 月版的用户指南）：

- 支持**混合仿真**：把大尺度实物模型和计算机数值模型结合起来做试验[^nherilehigh2016users-e1]。
- 写项目申请时就要尽早联系设施运行经理，帮助规划、排期、估算费用[^nherilehigh2016users-e9]。
- 所有试验都要事先交设施人员审查，确认不危及人员安全、不损坏设备。研究者要提交**试验矩阵**（列出每次试验怎么做的计划表），并说明每次试验预计试件会出现什么损伤；书面批准前不得开始[^nherilehigh2016users-e2]，未经批准也不得偏离[^nherilehigh2016users-e3]。
- 控制程序要先在关闭液压的仿真模式下开发和确认，正式试验前各环节都要安全地测试过[^nherilehigh2016users-e4]。试验用的软件装上控制系统前必须经过确认，所依据的算法必须证明是稳定的[^nherilehigh2016users-e5]。

**得克萨斯大学奥斯汀分校的现场试验设施**（依据是它 2020 年 8 月的安全计划，第 2.3 版）用大型移动激振车在美国各地现场做试验[^nheriutexas2020safety-e1]。这份安全计划写道：该设施的一个典型项目要经过数月、有时数年的准备，经费、组织、排期和后勤问题可能让完成项目的时间窗口非常有限[^nheriutexas2020safety-e2]。

这意味着：一次大尺度试验的机会很宝贵，试件一旦破坏就不能重来。动手前把测点布置、加载方案、预计的破坏过程和数据记录方式都想清楚，并用数值模型先做预测。排期的通用方法见第二部分的[形成研究计划](../../02_do-the-project/03_research-plan.md)。另外，利哈伊设施在网站上公布所有在研和新资助的项目，方便其他研究者寻找"搭载项目"的机会[^nherilehigh2016users-e8]。搭载项目就是在别人的试验上附加自己的研究。对经费有限的学生，这是参与大尺度试验的一种途径。

### 现场试验和现场监测：场地不是你的

在真实场地、真实结构上做试验或长期监测时，还要和场地的主人、周围的人打交道。以得克萨斯大学设施 2020 年的安全计划为例：

- 试验前，用户团队的项目负责人要踏勘场地、识别危害，并提前一个月把试验计划交给设施[^nheriutexas2020safety-e4]；
- 涉及场地和周边结构安全的责任在用户一方，项目负责人还要负责办理场地准入许可和责任保险[^nheriutexas2020safety-e5]；
- 激振点 50 英尺（约 15 米）内有对振动敏感的结构（尤其是有人住的建筑）时，必须征得业主同意，并强烈建议在试验前后给这些结构拍照留档[^nheriutexas2020safety-e6]。
- 在既有桥梁、道路、水利设施上做监测，同样要事先取得管理部门的许可，并约定数据归谁、能否发表。

### 数值模拟：先分清验证、确认和校准

有限元分析、水文模型、交通仿真等数值模型在本领域用得很多。仿真研究的完整做法见[定量仿真](../../06_methods/simulation_study.md)。下面三个词的定义来自美国桑迪亚国家实验室 Oberkampf 等人 2003 年的报告（讲计算工程和物理）和 Sargent 2010 年的仿真方法论文，不是土木工程专门的规定，但做数值模拟时要分清：

- **验证**（verification）：程序有没有正确实现你的模型、算得对不对[^oberkampf2003verification-e1]。
- **确认**（validation）：从预期用途出发，模型在多大程度上代表真实世界[^oberkampf2003verification-e1]。确认是针对特定用途的：模型在一组条件下有效，换一组条件可能无效[^sargent2010verification-e2]。
- **校准**（calibration）：调整模型参数，让模型和试验结果更吻合[^oberkampf2003verification-e5]。

容易混淆的地方：Oberkampf 等人指出，结构动力学研究者常把"用模态试验（测结构振动特性的试验）结果调整模型里的未知参数"叫作"模型确认"，他们认为更准确的叫法是"模型修正"或"模型校准"[^oberkampf2003verification-e2]。所以，用同一组试验数据既调参数又宣称"模型已确认"，并不能说明模型能预测新情况。

Oberkampf 等人认为，对大多数复杂或大型系统，做真正的确认试验不可行。他们推荐"积木式"方法：把系统分成子系统、基准情形、单元问题等由繁到简的几层，在各层分别和试验比较[^oberkampf2003verification-e3]。但物理过程复杂时（例如断裂），从一层推断另一层的可信度通常很弱[^oberkampf2003verification-e6]。确认试验要有目的地设计，目标和模型的应用目标挂钩[^oberkampf2003verification-e4]。Sargent 还提醒：模型任何改动之后，都要重新验证和确认[^sargent2010verification-e20]。和计算机领域相比：计算机领域的仿真研究多用来比较策略或系统设计；在本领域，模型结果常被用来支持设计决策，最终关系到公众安全，所以和物理试验的对照更受重视。

### 和业界、政府合作

本领域不少研究有企业、设计院或政府部门参与，常见问题是保密和数据所有权。合作开始前就要问清：数据归谁、论文发表前要不要合作方审阅、哪些内容不能公开。可以参考的相关规定：

- ASCE 伦理准则（2020 年修订版，约束 ASCE 会员）要求对委托方和雇主指明的专有信息保密[^asce2020code-e15]，并说清任何实际的、潜在的或可能被认为存在的利益冲突[^asce2020code-e14]。
- 利哈伊设施 2016 年的用户指南提到：2004—2014 年，美国 NEES（地震工程模拟网络，NHERI 的前身项目）的获资助项目在开始试验室工作前，要签"研究参与协议"，条款包括知识产权和发表权等；到 2016 年 4 月写指南时，NHERI 已不要求这类文件[^nherilehigh2016users-e10]。
- Rosenberg 等人 2020 年在 ASCE《水资源规划与管理期刊》的社论里，把"专有、敏感或含受保护知识产权的材料不能共享"列为复现研究的障碍之一[^rosenberg2020next-e2]。ASCE 期刊的数据政策页面（本文读到的是 2022 年的存档版本）鼓励作者在签数据协议时就谈好，让论文所用数据能以匿名等方式提供给读者[^ascedataavailability-e9]。

### 发表：以 ASCE 为例

据 2020 年的一篇社论，ASCE 出版 30 多种期刊[^rosenberg2020next-e1]。下面几条是 ASCE 自己的规定，出自 2011 年 ASCE《桥梁工程期刊》的一篇社论（Hendrickson 等人）。本文是通过网页存档网站 Internet Archive 2022 年的快照读到这篇社论的，ASCE 现行政策可能已经更新，投稿时以目标期刊的作者指南为准。投 Elsevier、Springer 等其他出版方或国内期刊时，以对方的规定为准。

- **不能一稿两发。** 社论说这是 ASCE 的长期政策：在 ASCE 期刊发表的内容，不能在别处发表过，也不能之后在别处发表[^hendrickson2011conference-e1]。
- **会议论文转期刊要有一半新内容。** 可以在会议报告的基础上写期刊论文，但期刊论文要和已出版的会议论文"显著不同"，一般指有 50% 的新内容[^hendrickson2011conference-e2]。社论还说，这适用于所有出版论文集的会议；放到网上的论文被视为已发表[^hendrickson2011conference-e4]。
- **交通方向的例子。** 从 2011 年 1 月的年会起，美国交通研究委员会（Transportation Research Board，TRB）把年会论文汇编放到网上，ASCE 因此把 TRB 年会论文视为已发表；作者可以选择不收入汇编，保留投 ASCE 期刊的权利[^hendrickson2011conference-e3]。
- **和 IEEE 比较。** 这和电子信息领域 IEEE（电气与电子工程师学会）"期刊版要有实质性新增内容"的规定思路相近，但 ASCE 给出了"50% 新内容"这个具体说法（见[电子信息篇](../electrical-engineering/README.md)）。
- **预印本。** 预印本是投稿前就公开在网上的论文稿。ASCE 的期刊作者指南网页（本文读到的是 Internet Archive 2025 年 5 月的快照）说：只要版权还能转让给 ASCE，放在预印本服务器上的论文不算已发表；论文被接收后，要在预印本上补上正式论文的完整引用和 DOI（数字对象标识符，论文的永久编号），并加上 ASCE 的版权声明（选开放获取的作者保留版权，改加一条说明）[^asce2025publishing-e1]。但同一页"已发表内容"一节又说，"已发表"可能包括放在机构库、预印本服务器等网站上的预印本[^asce2025publishing-e2]。本手册对照这两处，发现说法不完全一致，投稿前最好向目标期刊编辑部确认。

---

## 和其他学科不同的地方

下表是本项目的归纳，用来帮你快速定位差别，不是严格的学科划分。

| | 土木工程 | 计算机领域 |
|---|---|---|
| 结果从哪来 | 试验室试验（含大尺度试件）、现场试验和监测、数值模拟，常常几种结合 | 以代码、系统和数据上的实验为主 |
| 周期受谁控制 | 大型设施排期、场地许可、季节和天气；例如得克萨斯大学 NHERI 现场试验设施的典型项目要准备数月甚至数年[^nheriutexas2020safety-e2] | 主要受会议截稿日控制（见[计算机篇](../computer-science/README.md#截止日期决定节奏也有代价)） |
| 发表路径 | 以 ASCE 为例（2011 年社论），会议论文转期刊一般要 50% 新内容[^hendrickson2011conference-e2] | 多数方向以顶级会议为主（见[计算机篇](../computer-science/README.md#会议是主要的发表渠道)） |
| 研究的去向 | 部分成果会进入设计规范和标准（见下文） | 计算机篇未涉及 |
| 伦理重点 | 以 ASCE 伦理准则为例，公众的健康、安全和福祉放在第一位[^asce2020code-e12]；试验安全 | 见[计算机篇](../computer-science/README.md#伦理问题有本领域的特点) |
| 能公开多少 | 专有、敏感或含知识产权的材料可能无法共享[^rosenberg2020next-e2] | 实验方向有公开制品（代码、数据）的传统 |

---

## 本领域的规范和报告标准

### ASCE 伦理准则：公众安全第一

ASCE 伦理准则 1914 年首次通过，2020 年 10 月最近一次修订，是 ASCE 会员的职业行为规范[^asce2020code-e10]（本文读的是 2026 年 10 月的网页版本）。它要求会员首先保护和促进公众的健康、安全和福祉[^asce2020code-e11]；伦理责任冲突时，这一条高于其他所有责任[^asce2020code-e12]。ASCE 说明这份准则本身不构成"注意标准"（法律上判断专业人员是否尽责的标准）[^asce2020code-e9]。其他国家的学会和注册工程师制度有各自的准则，以本地为准。通用的科研诚信要求见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md)。和研究关系较大的几条：

- 只在知识充分、真心相信时发表专业意见，并如实表达[^asce2020code-e3]。写论文结论和给工程建议时都适用。
- 工作中用到现有或新兴技术时，要考虑它的能力、局限和影响[^asce2020code-e13]；及时向委托方和雇主告知工作的风险和局限[^asce2020code-e14]。
- 只把自己亲自完成的工作算作自己的功劳，注明别人的贡献[^asce2020code-e16]。

### 研究和设计规范、标准

一部分土木工程研究的最终用户是写规范的委员会和做设计的工程师。下面以美国和 ASCE 为例（依据是 2026 年 10 月读取的 ASCE 网页），其他国家的规范体系不同：

- ASCE 7 是美国全国采用的一般结构设计荷载标准[^asce2026asce7-e1]。许多 ASCE 标准被示范建筑规范引用，并被各州和地方采纳[^asce2026standards-e1]。
- ASCE 标准由各方代表均衡的志愿者委员会制定或更新，之后有公众审阅期[^asce2026standards-e2]，至少 45 天[^asce2026standards-e5]；所有标准至少每 5 年更新或重新确认一次[^asce2026standards-e3]。以 ASCE 7 为例，有投票权的委员来自生产方、使用方和监管机构等各方[^asce2026asce7-e3]。任何人都可以提议修改标准，委员会会议对任何人开放[^asce2026standards-e4]。
- 新数据会推动条文修订。例如 ASCE 7-22 版修订了地面雪荷载，以反映更新的雪荷载数据[^asce2026asce7-e2]。
- 研究进入规范并不自动发生。一个地震工程方面的例子：美国国家标准与技术研究院（NIST）在 2008 财年预算申请中，关于"国家地震减灾计划"的说明写道，基础研究成果和工程实际应用之间存在关键差距，建筑规范和标准没有反映当时的认识水平[^nist2008nehrp-e1]；它提出的计划之一就是找出研究成果和设计指南、全国示范建筑规范条文之间的落地差距[^nist2008nehrp-e2]。这反映的是 2007—2008 年前后美国地震工程的情况，现在和其他方向未必如此。Rosenberg 等人 2020 年的社论也认为，公开数据和代码让工程从业者更容易用上研究成果，有助于缩小研究和实践之间的差距[^rosenberg2020next-e6]。
- **对新手的意义**：写论文时，说清你的结果和现行规范的哪一条相关、是否支持修改；引用规范时写明版本号，因为规范会修订，例如 ASCE 标准至少每 5 年更新或重新确认一次[^asce2026standards-e3]。

### 数据可得性声明（ASCE）

2018 年，ASCE《水资源规划与管理期刊》开始要求作者说明数据、计算模型和代码能否获得[^rosenberg2018new-e1]，据 2020 年的社论，这项政策后来被 ASCE 几乎所有期刊采用[^rosenberg2020next-e1][^ascedataavailability-e1]。ASCE 网站不允许程序读取，下面几条是本文从 Internet Archive 2022 年 6 月的存档快照里读到的 ASCE 期刊政策页面。现行版本可能已经更新，投稿时以目标期刊页面为准：

- 投稿时在致谢前加一节"数据可得性声明"，从给定的几种说法中原样选择[^ascedataavailability-e2]，例如"可向通讯作者合理索取""属于专有或保密材料，只能有条件提供"[^ascedataavailability-e3]；
- 公开的数据和代码要列入参考文献；声明在审稿期间可以改，录用后不能再改[^ascedataavailability-e4]；
- 编辑和审稿人要求时，审稿期间必须提供数据和材料[^ascedataavailability-e5]；
- ASCE 的补充材料不适合大数据集和代码，也没有自己的 DOI（数字对象标识符，一种持久链接）[^ascedataavailability-e6]，最好放在能分配 DOI 的数据仓库[^ascedataavailability-e10]，ASCE 页面列出的通用仓库包括 Dryad、Figshare、DesignSafe、Zenodo、HydroShare 等[^ascedataavailability-e11]；
- 生成图表所用的数据应当包括在共享内容里[^ascedataavailability-e7]；
- ASCE 不对数据和代码做同行评审，审稿人可能看，也可能不看[^ascedataavailability-e8]，所以材料能不能用，要靠你自己检查。

### 可复现性：水文与水资源领域的一项调查

Stagge 等人 2019 年发表了一项调查：他们从六种水文与水资源期刊 2017 年发表的 1,989 篇论文里，抽了 360 篇来评估[^stagge2019assessing-e1]。在这 360 篇里，70.3% 声称有材料可得，但这些材料只有 48.6% 能在网上拿到；只有 1.1% 的论文既公开了材料、结果又被完整复现[^stagge2019assessing-e2]。他们估计，全部 1,989 篇中能复现结果的只有 0.6% 到 6.8%[^stagge2019assessing-e3]。注意范围：这项调查只看了水文与水资源方向的六种期刊、2017 年一年的论文，不能直接推到结构、岩土、交通等其他方向或整个土木工程；其他方向的情况，本文资料未涉及。这项调查发现的几个问题，新手自己就能避免：

- 在没能跑出结果的论文里，一个常见问题是文件路径写死成只在作者电脑上有效[^stagge2019assessing-e4]；
- 在被调查的六种期刊里，提供了代码、数据或软件的论文，数量都是提供了使用说明的 2 到 3 倍[^stagge2019assessing-e5]，也就是说，不少人给了材料却没写怎么用；
- 期刊政策有用，但不能只靠政策：在这六种期刊里，数据政策越强，材料可得率和可复现率往往越高，但期刊之间差异很大[^stagge2019assessing-e6]；要求写数据可得性声明的两种期刊（HESS 和 WRR，都不是 ASCE 期刊），公开材料的论文比例反而较低，更多论文让读者去找作者或第三方要材料[^stagge2019assessing-e7]。

Rosenberg 等人 2020 年社论附了一份检查清单，例如写明哪段代码生成哪张图、哪个表，去掉只在自己电脑上有效的本地路径[^rosenberg2020next-e3]；其余是整理材料的通用做法，见[整理科研材料](../../08_throughout/organizing_materials.md)。试验数据也一样：利哈伊设施 2016 年的用户指南要求研究者上传描述试验装置的元数据、未处理的原始数据和转换后的数据[^nherilehigh2016users-e6]，让有资质的研究者能重做试验并重新生成派生数据[^nherilehigh2016users-e7]。

### 大尺度试验和现场试验的安全

大尺度试验用到大吨位作动器（液压驱动的加载装置）、重型试件和吊装，现场试验用到重型车辆和设备。ASCE 伦理准则也要求在工作场所促进健康和安全[^asce2020code-e16]。两家 NHERI 设施文件里的做法可以参考（利哈伊设施 2016 年用户指南、得克萨斯大学设施 2020 年安全计划），你所在试验室以本单位的安全规定为准：

- **先培训再动手**（利哈伊）：使用任何设备前，必须完成正式的现场培训[^nherilehigh2016users-e11]。
- **事先分析危害**（得克萨斯）：安全计划里的工作危害分析，是以具体作业任务为单位、在危害发生前把它识别出来的方法[^nheriutexas2020safety-e3]。
- **每天开安全简会**（得克萨斯）：现场作业期间，每天由首席科学家或首席工程师召集全体现场人员开安全简会[^nheriutexas2020safety-e7]。
- **试验时人不进试验区**（利哈伊）[^nherilehigh2016users-e12]。
- **出事先停工**（得克萨斯）：出现失误、事故或设备故障时立即停工，确定纠正措施再调整计划；安全、稳妥的流程永远优先于进度[^nheriutexas2020safety-e8]。不要对安全想当然，别人可能没意识到出了问题[^nheriutexas2020safety-e9]。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表只列本文资料能支持的两种；比较评估、解释因果、综合等套路在土木工程里怎样用，本文资料未涉及。表的分组和"在土木工程里的样子"一栏是本项目的归纳，每条标准只代表脚注里的那家单位或那份文献。

| 套路 | 在土木工程里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md) | 提出新的结构体系、构件、材料用法或分析方法，常配有限元、水文、交通等数值模型 | 利哈伊设施要求大尺度试验事先提交试验矩阵和每次试验预计的试件损伤，书面批准后才能做[^nherilehigh2016users-e2]；数值模型要分清验证、确认和校准[^oberkampf2003verification-e1][^oberkampf2003verification-e5]，用模态试验调参数是校准，不该叫确认[^oberkampf2003verification-e2]；模型在一组条件下有效，换一组条件可能无效[^sargent2010verification-e2] | [工程研究](../computer-science/practices/engineering_research.md)（计算机篇）、[定量仿真](../../06_methods/simulation_study.md) |
| [观察描述](../../05_research-strategies/observe_describe.md) | 在试验室或真实场地测出结构、土体的实际表现，包括现场试验和长期监测 | 利哈伊设施要求上传描述试验装置的元数据、未处理的原始数据和转换后的数据[^nherilehigh2016users-e6]，让有资质的研究者能重做试验、重新生成派生数据[^nherilehigh2016users-e7]；投 ASCE 期刊要写数据可得性声明[^ascedataavailability-e2] | [实验测量研究](../../06_methods/experimental_measurement.md) |

怎么用这张表：先按核心主张定主要套路。例如提出新节点、再做加载试验看它怎样破坏，主张是"新节点更好"，就按构建改进的标准要求，试验数据按观察描述的要求写清。

## 本学科常用的研究方法

土木工程没有独有的方法文档，用的是[研究类型](../../06_methods/README.md)里的跨学科方法和计算机篇的实践：

- [实验测量研究](../../06_methods/experimental_measurement.md)：试验室加载试验、现场试验和监测。先排期、先报批，见上文[大尺度试验](#大尺度试验排队审批准备都要很久)。
- [定量仿真](../../06_methods/simulation_study.md)：先分清验证、确认和校准，见上文[数值模拟](#数值模拟先分清验证确认和校准)。
- [工程研究](../computer-science/practices/engineering_research.md)、[优化研究](../computer-science/practices/optimization_study.md)（计算机篇）：评估新结构常要有物理试验，不能只靠数值模拟；结构优化、水资源调度、交通网络设计可参考优化研究。
- [案例研究](../../06_methods/case_study.md)：施工管理、工程事故分析等方向常用。[复现研究](../../06_methods/replication.md)：见上文[可复现性](#可复现性水文与水资源领域的一项调查)。

---

## 给新手的建议

1. **大尺度试验从写申请时就排期。** 以利哈伊设施为例，写申请时就尽早联系设施[^nherilehigh2016users-e9]；试验矩阵和每次试验预计的试件损伤要事先交设施书面批准[^nherilehigh2016users-e2]。测点布置也要在这时想好，并先用模型预测一遍。
2. **别把校准当确认。** 用模态试验调参数是校准，不是确认[^oberkampf2003verification-e2][^oberkampf2003verification-e5]；留一部分独立的试验结果做检验，道理见[比较评估：留一份数据只用于最后检验](../../05_research-strategies/compare_evaluate.md#留一份数据只用于最后检验)。
3. **合作开始前问清数据和发表权。** ASCE 期刊的数据政策页面鼓励作者在签数据协议时就谈好数据怎么提供给读者[^ascedataavailability-e9]。
4. **从第一天起整理数据和代码**，别让路径写死在自己电脑上[^stagge2019assessing-e4]。
5. **引用规范写明版本。** 规范会修订，例如 ASCE 标准至少每 5 年更新或重新确认一次[^asce2026standards-e3]。
6. **投稿前查清会议论文和预印本的规定。** 以 ASCE 为例，按 2011 年的一篇社论，出版了论文集的会议论文，转投期刊一般要 50% 新内容[^hendrickson2011conference-e2]；现行规定以目标期刊作者指南为准。
7. **安全优先于进度。** 没培训不碰设备，出了状况先停工；两家 NHERI 设施的文件都这样要求[^nherilehigh2016users-e11][^nheriutexas2020safety-e8]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 用同一组试验数据调参数，又说"模型已确认" | 那是校准，不是确认[^oberkampf2003verification-e2][^oberkampf2003verification-e5] |
| 在一种工况下确认过模型，就用它预测完全不同的工况 | 模型在一组条件下有效，换一组条件可能无效[^sargent2010verification-e2] |
| 改了模型之后没有重新检查 | 模型任何改动之后都要重新验证和确认[^sargent2010verification-e20] |
| 试验开始后临时改加载方案 | 在利哈伊设施，未经批准不得偏离试验矩阵[^nherilehigh2016users-e3] |
| 现场试验没征得业主同意就在有人住的建筑旁激振 | 在得克萨斯大学设施，50 英尺内有敏感结构必须征得业主同意[^nheriutexas2020safety-e6] |
| 只声称"材料可得"，却不把材料放到读者拿得到的地方 | Stagge 等人调查的水文与水资源期刊论文里，声称有材料可得的，只有 48.6% 的材料能在网上拿到[^stagge2019assessing-e2]；ASCE 期刊政策也写明，不能因为不想共享就声称数据是专有的[^ascedataavailability-e9] |
| 公开了代码，但路径写死、没有说明 | 别人跑不出结果[^stagge2019assessing-e4][^stagge2019assessing-e5] |
| 在自己不熟悉的问题上给出确定的工程结论 | ASCE 伦理准则要求只在知识充分时发表专业意见[^asce2020code-e3] |

---

## 延伸阅读

- **ASCE Code of Ethics**：ASCE 伦理准则全文，篇幅很短。进入本领域时读一遍。
- **ASCE Library 的 Data Availability Statement 页面**：数据可得性声明的可选说法和数据仓库建议。投 ASCE 期刊前读现行版本。
- **Stagge 等人 2019，Assessing data availability and research reproducibility in hydrology and water resources**（Scientific Data，开放获取）：调查了六种水文与水资源期刊 2017 年论文的数据可得性和可复现性。
- **Rosenberg 等人 2020，The Next Frontier: Making Research More Reproducible**（ASCE《水资源规划与管理期刊》社论）：附有一份让研究更容易复现的检查清单。
- **Oberkampf、Trucano 与 Hirsch 2003，Verification, Validation, and Predictive Capability in Computational Engineering and Physics**（桑迪亚国家实验室公开报告）：系统讲计算模型的验证、确认和校准。做数值模拟前读引言和第 2 节。
- **你要用的试验设施的用户指南和安全规定**：本文引用的是 NHERI 两个设施的文件（利哈伊 2016 年用户指南、得克萨斯大学 2020 年安全计划），各试验室规定不同，以本单位为准。

[^nherilehigh2016users-e1]: NHERI Lehigh 2016 用户指南，Preface。[证据](../../../sources/notes/nherilehigh2016users.md#e1)
[^nherilehigh2016users-e2]: NHERI Lehigh 2016 用户指南，§1.6 Configuring an Experiment。[证据](../../../sources/notes/nherilehigh2016users.md#e2)
[^nherilehigh2016users-e3]: NHERI Lehigh 2016 用户指南，§1.6 Configuring an Experiment。[证据](../../../sources/notes/nherilehigh2016users.md#e3)
[^nherilehigh2016users-e4]: NHERI Lehigh 2016 用户指南，§1.6 Configuring an Experiment。[证据](../../../sources/notes/nherilehigh2016users.md#e4)
[^nherilehigh2016users-e5]: NHERI Lehigh 2016 用户指南，§2.7 Software Policies。[证据](../../../sources/notes/nherilehigh2016users.md#e5)
[^nherilehigh2016users-e6]: NHERI Lehigh 2016 用户指南，§1.9.1 Data Description。[证据](../../../sources/notes/nherilehigh2016users.md#e6)
[^nherilehigh2016users-e7]: NHERI Lehigh 2016 用户指南，§1.9.1 Data Description。[证据](../../../sources/notes/nherilehigh2016users.md#e7)
[^nherilehigh2016users-e8]: NHERI Lehigh 2016 用户指南，§1.11 Payload Project Protocol。[证据](../../../sources/notes/nherilehigh2016users.md#e8)
[^nherilehigh2016users-e9]: NHERI Lehigh 2016 用户指南，§5.1 Guidelines for Proposal Preparation。[证据](../../../sources/notes/nherilehigh2016users.md#e9)
[^nherilehigh2016users-e10]: NHERI Lehigh 2016 用户指南，§5.3 Required Documentation。[证据](../../../sources/notes/nherilehigh2016users.md#e10)
[^nherilehigh2016users-e11]: NHERI Lehigh 2016 用户指南，§5.4 Training。[证据](../../../sources/notes/nherilehigh2016users.md#e11)
[^nherilehigh2016users-e12]: NHERI Lehigh 2016 用户指南，§5.5 Experiment Execution。[证据](../../../sources/notes/nherilehigh2016users.md#e12)
[^nheriutexas2020safety-e1]: NHERI@UTexas 2020 安全计划（第 2.3 版），§1.1。[证据](../../../sources/notes/nheriutexas2020safety.md#e1)
[^nheriutexas2020safety-e2]: NHERI@UTexas 2020 安全计划（第 2.3 版），§1.1。[证据](../../../sources/notes/nheriutexas2020safety.md#e2)
[^nheriutexas2020safety-e3]: NHERI@UTexas 2020 安全计划（第 2.3 版），§1.7 Job Hazard Analysis。[证据](../../../sources/notes/nheriutexas2020safety.md#e3)
[^nheriutexas2020safety-e4]: NHERI@UTexas 2020 安全计划（第 2.3 版），§2.2.1。[证据](../../../sources/notes/nheriutexas2020safety.md#e4)
[^nheriutexas2020safety-e5]: NHERI@UTexas 2020 安全计划（第 2.3 版），§2.2.1。[证据](../../../sources/notes/nheriutexas2020safety.md#e5)
[^nheriutexas2020safety-e6]: NHERI@UTexas 2020 安全计划（第 2.3 版），§2.2.2。[证据](../../../sources/notes/nheriutexas2020safety.md#e6)
[^nheriutexas2020safety-e7]: NHERI@UTexas 2020 安全计划（第 2.3 版），§1.12。[证据](../../../sources/notes/nheriutexas2020safety.md#e7)
[^nheriutexas2020safety-e8]: NHERI@UTexas 2020 安全计划（第 2.3 版），§1.12。[证据](../../../sources/notes/nheriutexas2020safety.md#e8)
[^nheriutexas2020safety-e9]: NHERI@UTexas 2020 安全计划（第 2.3 版），§1.12。[证据](../../../sources/notes/nheriutexas2020safety.md#e9)
[^oberkampf2003verification-e1]: Oberkampf 等人 2003，§1.2。[证据](../../../sources/notes/oberkampf2003verification.md#e1)
[^oberkampf2003verification-e2]: Oberkampf 等人 2003，§1.1。[证据](../../../sources/notes/oberkampf2003verification.md#e2)
[^oberkampf2003verification-e3]: Oberkampf 等人 2003，§1.2。[证据](../../../sources/notes/oberkampf2003verification.md#e3)
[^oberkampf2003verification-e4]: Oberkampf 等人 2003，§2.4.1。[证据](../../../sources/notes/oberkampf2003verification.md#e4)
[^oberkampf2003verification-e5]: Oberkampf 等人 2003，§3.3。[证据](../../../sources/notes/oberkampf2003verification.md#e5)
[^oberkampf2003verification-e6]: Oberkampf 等人 2003，§1.2。[证据](../../../sources/notes/oberkampf2003verification.md#e6)
[^sargent2010verification-e2]: Sargent 2010，§1 Introduction。[证据](../../../sources/notes/sargent2010verification.md#e2)
[^sargent2010verification-e20]: Sargent 2010，§3 Paradigms。[证据](../../../sources/notes/sargent2010verification.md#e20)
[^asce2020code-e10]: ASCE Code of Ethics（2020 年修订），页首说明。[证据](../../../sources/notes/asce2020code.md#e10)
[^asce2020code-e11]: ASCE Code of Ethics，Preamble。[证据](../../../sources/notes/asce2020code.md#e11)
[^asce2020code-e12]: ASCE Code of Ethics，Preamble；1a。[证据](../../../sources/notes/asce2020code.md#e12)
[^asce2020code-e3]: ASCE Code of Ethics，1c。[证据](../../../sources/notes/asce2020code.md#e3)
[^asce2020code-e13]: ASCE Code of Ethics，1h。[证据](../../../sources/notes/asce2020code.md#e13)
[^asce2020code-e14]: ASCE Code of Ethics，4b、4c。[证据](../../../sources/notes/asce2020code.md#e14)
[^asce2020code-e15]: ASCE Code of Ethics，4e、4f。[证据](../../../sources/notes/asce2020code.md#e15)
[^asce2020code-e16]: ASCE Code of Ethics，5a、5b、5c。[证据](../../../sources/notes/asce2020code.md#e16)
[^asce2020code-e9]: ASCE Code of Ethics，脚注 1。[证据](../../../sources/notes/asce2020code.md#e9)
[^rosenberg2020next-e1]: Rosenberg 等人 2020，正文 Figure 1 之后。[证据](../../../sources/notes/rosenberg2020next.md#e1)
[^rosenberg2020next-e2]: Rosenberg 等人 2020，正文第 2 段。[证据](../../../sources/notes/rosenberg2020next.md#e2)
[^rosenberg2020next-e3]: Rosenberg 等人 2020，Checklist。[证据](../../../sources/notes/rosenberg2020next.md#e3)
[^rosenberg2018new-e1]: Rosenberg & Watkins 2018，正文第 1 段。[证据](../../../sources/notes/rosenberg2018new.md#e1)
[^ascedataavailability-e2]: ASCE Library，Data Availability Statement（2022 年快照）。[证据](../../../sources/notes/ascedataavailability.md#e2)
[^ascedataavailability-e3]: ASCE Library，Data Availability Statement（2022 年快照），可选说法列表。[证据](../../../sources/notes/ascedataavailability.md#e3)
[^ascedataavailability-e4]: ASCE Library，Data Availability Statement（2022 年快照）。[证据](../../../sources/notes/ascedataavailability.md#e4)
[^ascedataavailability-e5]: ASCE Library，Data Availability Statement（2022 年快照）。[证据](../../../sources/notes/ascedataavailability.md#e5)
[^ascedataavailability-e6]: ASCE Library，Data Availability Statement（2022 年快照），Where should my data go?。[证据](../../../sources/notes/ascedataavailability.md#e6)
[^ascedataavailability-e9]: ASCE Library，Data Availability Statement（2022 年快照），What if my data is proprietary?。[证据](../../../sources/notes/ascedataavailability.md#e9)
[^ascedataavailability-e10]: ASCE Library，Data Availability Statement（2022 年快照），Where should my data go?。[证据](../../../sources/notes/ascedataavailability.md#e10)
[^hendrickson2011conference-e1]: Hendrickson 等人 2011，第 1 段。[证据](../../../sources/notes/hendrickson2011conference.md#e1)
[^hendrickson2011conference-e2]: Hendrickson 等人 2011，第 2 段。[证据](../../../sources/notes/hendrickson2011conference.md#e2)
[^hendrickson2011conference-e3]: Hendrickson 等人 2011，第 3 段。[证据](../../../sources/notes/hendrickson2011conference.md#e3)
[^hendrickson2011conference-e4]: Hendrickson 等人 2011，第 4 段。[证据](../../../sources/notes/hendrickson2011conference.md#e4)
[^asce2025publishing-e1]: ASCE Library，Publishing in ASCE Journals（2025 年快照），Preprint Servers。[证据](../../../sources/notes/asce2025publishing.md#e1)
[^asce2025publishing-e2]: ASCE Library，Publishing in ASCE Journals（2025 年快照），Previously Published Content。[证据](../../../sources/notes/asce2025publishing.md#e2)
[^asce2026standards-e1]: ASCE，Codes and Standards 页面。[证据](../../../sources/notes/asce2026standards.md#e1)
[^asce2026standards-e2]: ASCE，Codes and Standards 页面，Get involved with Standards。[证据](../../../sources/notes/asce2026standards.md#e2)
[^asce2026standards-e3]: ASCE，Codes and Standards 页面，Get involved with Standards。[证据](../../../sources/notes/asce2026standards.md#e3)
[^asce2026standards-e4]: ASCE，Codes and Standards 页面。[证据](../../../sources/notes/asce2026standards.md#e4)
[^asce2026standards-e5]: ASCE，Codes and Standards 页面，Comment on a draft standard。[证据](../../../sources/notes/asce2026standards.md#e5)
[^asce2026asce7-e1]: ASCE，ASCE 7-22 页面。[证据](../../../sources/notes/asce2026asce7.md#e1)
[^asce2026asce7-e2]: ASCE，ASCE 7-22 页面，新内容列表。[证据](../../../sources/notes/asce2026asce7.md#e2)
[^nist2008nehrp-e1]: NIST，2008 财年预算说明，国家地震减灾计划，Challenge。[证据](../../../sources/notes/nist2008nehrp.md#e1)
[^nist2008nehrp-e2]: NIST，2008 财年预算说明，国家地震减灾计划，Proposed Program；Expected Impacts。[证据](../../../sources/notes/nist2008nehrp.md#e2)
[^stagge2019assessing-e1]: Stagge 等人 2019，Abstract。[证据](../../../sources/notes/stagge2019assessing.md#e1)
[^stagge2019assessing-e2]: Stagge 等人 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e2)
[^stagge2019assessing-e3]: Stagge 等人 2019，Abstract。[证据](../../../sources/notes/stagge2019assessing.md#e3)
[^stagge2019assessing-e4]: Stagge 等人 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e4)
[^stagge2019assessing-e5]: Stagge 等人 2019，Discussion。[证据](../../../sources/notes/stagge2019assessing.md#e5)
[^stagge2019assessing-e7]: Stagge 等人 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e7)
[^ascedataavailability-e7]: ASCE Library，Data Availability Statement（2022 年快照），What should we share?。[证据](../../../sources/notes/ascedataavailability.md#e7)
[^ascedataavailability-e8]: ASCE Library，Data Availability Statement（2022 年快照），Will my data or code be peer reviewed?。[证据](../../../sources/notes/ascedataavailability.md#e8)
[^ascedataavailability-e11]: ASCE Library，Data Availability Statement（2022 年快照），Where should my data go?。[证据](../../../sources/notes/ascedataavailability.md#e11)
[^stagge2019assessing-e6]: Stagge 等人 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e6)
[^asce2026asce7-e3]: ASCE，ASCE 7-22 页面，Who develops standards?。[证据](../../../sources/notes/asce2026asce7.md#e3)
[^rosenberg2020next-e6]: Rosenberg 等人 2020，正文好处列表之后。[证据](../../../sources/notes/rosenberg2020next.md#e6)
[^ascedataavailability-e1]: ASCE Library，Data Availability Statement（2022 年快照），第 1 段。[证据](../../../sources/notes/ascedataavailability.md#e1)
