# 社会与经济地理学：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲人文地理学（社会、经济、城市、文化、政治、发展地理等）和社会科学中的空间分析、地理信息系统（GIS）研究实际怎样运转：在"地方"里做田野，用带坐标的数据做分析，以及这两样带来的特有问题——研究者立场、田野伦理和安全、空间单元怎么划会改变结论、参与者的位置隐私、地理研究的可复现性。自然地理（地貌、气候、水文等）见[地球与环境科学领域篇](../earth-environmental-sciences/README.md)。和社会学重叠的部分（访谈、民族志伦理、数据存档）见[社会学领域篇](../sociology/README.md)，这里只讲地理学多出来的东西。各学科共通的做法见[通用篇](../../README.md)。

**读完本文，你应该能：**

- 说清人文地理学几种主要做法各自的长处，以及它们怎样组合；
- 知道两份有代表性的地理学伦理规定讲了什么：美国地理学家协会（AAG）给会员的职业伦理声明，和英国皇家地理学会（RGS-IBG）给它资助的项目定的守则；
- 用大白话解释可塑性面积单元问题、生态谬误和"不确定的地理背景问题"，并知道怎样在论文里交代；
- 在收集、分析、发表带位置的数据时保护参与者隐私；
- 让自己的空间分析能被别人复现。

---

## 本领域研究怎样运转

### 一个学科，几种做法

美国地理学家协会（American Association of Geographers，AAG）的伦理声明开篇就说：地理学横跨自然科学、社会科学和人文艺术[^aag2024ethics-e1]。具体到人文地理，研究大致有三种做法（这个分法是本项目的归纳 `[本项目分析]`）：

- **定性田野研究**：到一个地方去，做访谈、参与观察、民族志、参与式制图（请当地人一起画地图），理解人和地方的关系 `[本项目分析]`。AAG 把"和参与者一起做研究，而不是对参与者做研究"、避免索取式研究，视为尊重的重要标志[^aag2024ethics-e4]。
- **定量空间分析和 GIS**：用带位置的数据（人口普查、调查、GPS 轨迹、遥感影像、社交媒体签到等）做空间统计、空间回归、制图 `[本项目分析]`。这类分析要事先定下许多参数，例如分析的尺度、怎样表示"相邻"[^kedron2021reproducibility-e2]，后文会讲为什么这一点很关键。
- **混合方法**：把两者结合。例如地理学者关美宝（Mei-Po Kwan）在 2018 年的文章中认为，测量一个人受什么环境影响时，加入他怎样感知、理解自己环境的定性信息，似乎有助于减轻下文讲的"不确定的地理背景问题"[^kwan2018limits-e4]。

同一个系里，这几种做法的研究者对"什么是好研究"的看法可能差别很大 `[本项目分析]`。新手先弄清导师和目标期刊属于哪一种传统，再决定怎样写方法部分 `[本项目分析]`。

### 发表与署名

- **会议论文（GIScience 方向）。** 地理信息科学（GIScience，研究地理信息怎样获取、表示和分析的方向）有专门的学术会议。例如欧洲地理信息实验室协会（AGILE）自 1998 年起每年开会[^nust2018reproducible-e1]；2007 年起分长论文和短论文两个通道，短论文在 AGILE 网站免费发布[^nust2018reproducible-e2]。人文地理各方向期刊和专著的地位、审稿周期、署名顺序惯例，本文资料未涉及，以导师或目标期刊要求为准。
- **有的期刊要求公开数据。** 据 Kedron 等人 2020 年的介绍，国际地理信息科学期刊（IJGIS）要求作者免费公开数据和研究材料，并符合 FAIR 原则（可查找、可访问、可互操作、可重用）[^kedron2021reproducibility-e10]。
- **美国 AAG 的规定：披露资金来源。** 在 AAG 的期刊发表、在 AAG 年会或地区分会报告，都必须披露资金来源[^aag2024ethics-e16]。
- **署名一开始就谈。** AAG 的伦理声明要求，合作范围、各方权责、合著署名和致谢，在一开始就公开、公平地商定[^aag2024ethics-e8]。英国皇家地理学会（RGS-IBG）的资助项目守则要求：当地合作者应在数据所有权和论文署名上得到承认[^rgsgrantscode-e5]。署名的通用原则见通用篇[署名和引用](../../08_throughout/integrity_and_ethics.md#5-署名引用和利益冲突给每个贡献者应得的认可)。

---

## 和其他学科不同的地方

| | 社会与经济地理学 | 对照 |
|---|---|---|
| 研究对象 | 人和地方 `[本项目分析]`；AAG 认为地理知识都是"有处境的"，和产生它的人与场合有关[^aag2024ethics-e3] | 社会学关注社会关系和社会结构，见[社会学领域篇](../sociology/README.md) `[本项目分析]` |
| 数据的特殊风险 | 坐标本身就能认人：即使匿名化了，轨迹数据也常能被重新识别[^malekzadeh2026ethical-e1] | 一般数据的处理做法见[数据科学](../../06_methods/data_science.md)；带位置的数据要多一层防范 `[本项目分析]` |
| 分析结果的稳定性 | 换一种空间单元划法，结论可能就变了[^kwan2018limits-e2] | 不按地区汇总的数据，没有"单元怎么划"这个问题 `[本项目分析]` |
| 结果能否在别处重现 | 能否期待"换个地方也成立"，本身就有争议[^kedron2021reproducibility-e6] | 许多实验学科把"别的实验室能重复出来"当作检验结果的标准 `[本项目分析]` |
| 野外工作 | 野外工作是地理研究的组成部分，常要出行[^rgsgrantscode-e6]；英国 RGS-IBG 要求它资助的项目同时通过东道国的伦理审查[^rgsgrantscode-e3] | 自然地理的野外安全和许可，见[地球与环境科学领域篇](../earth-environmental-sciences/README.md#野外工作先把安全和许可办好) |

---

## 本领域的规范和报告标准

下面以两份规定为例。它们各有约束对象，不是全世界地理学的统一规矩：

- **美国地理学家协会（AAG）的职业伦理声明**（2024 年修订[^aag2024ethics-e18]）。AAG 会员必须遵守协会的职业行为政策；许多地理学者还要遵守所在机构和资助方的受试者伦理要求[^aag2024ethics-e2]。
- **英国皇家地理学会（RGS-IBG）的资助项目守则**和给资助申请人的安全伦理说明。守则的伦理条款适用于学会支持的研究：它资助的、在它的会议上报告的、在它的期刊发表的[^rgsgrantscode-e1]。

不在这两家管辖范围内的研究，以本国、本单位和资助方的规定为准 `[本项目分析]`。

### 田野伦理：先保护人和地方

- **不伤害优先于求知。** AAG 的声明说，不造成伤害的义务高于获取或传播新知识的目标[^aag2024ethics-e6]。
- **意识到自己的权力。** AAG 提醒：研究者相对参与者常处于强势地位，很容易意识不到这种不平等的影响[^aag2024ethics-e7]。
- **同意是持续的对话。** AAG 要求把知情同意写进项目设计，并在实施中持续协商[^aag2024ethics-e9]。看重的是同意的质量，不是形式；拒绝的权利也属于整个社区，不只属于个人[^aag2024ethics-e11]。
- **有审查就过审查，没有就找社区。** AAG 要求：所在国家有机构审查委员会（Institutional Review Board，IRB，即伦理审查委员会）或类似程序的，必须获得批准；没有的，应取得相关社区的许可[^aag2024ethics-e10]。英国 RGS-IBG 还要求它资助的项目在东道国有伦理委员会时也经其批准，即使本单位已经批过[^rgsgrantscode-e3]。
- **征求同意时就讲清钱从哪来。** AAG 要求在征求同意时，用易懂的方式披露全部资金来源和合作方[^aag2024ethics-e15]。
- **让当地人参与，并把结果带回去。** RGS-IBG 的守则要求当地合作者、社区和参与者参与从计划到研究后反馈的全过程[^rgsgrantscode-e4]；AAG 要求在合适时，以对方看得懂的形式，把结果分享给参与者和受影响的社区[^aag2024ethics-e12]。
- **出行要有理由。** RGS-IBG 守则在"可持续研究"部分要求：出行和目的地的选择要有清楚的理由[^rgsgrantscode-e6]。

人类受试者伦理的通用做法见通用篇[研究涉及人时，先保护人](../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)；长期田野中的化名、把关人、保密限度等，见[社会学领域篇](../sociology/README.md#民族志特有的难题化名改细节以及怎样让人核查)。

### 田野安全：风险评估要针对这一次

- 英国 RGS-IBG 要求它资助的人先取得本单位的健康安全审批和伦理审批，才拨款[^rgssaferesearch-e1]；风险评估不能套模板，要针对项目地点和研究性质写[^rgssaferesearch-e2]。
- RGS-IBG 还请申请人想清楚：研究会不会冒犯当地人的文化禁忌？是否取得了参与者或其他受影响者的恰当同意[^rgssaferesearch-e3]？
- AAG 提醒，权衡伦理义务时也要考虑研究者自身的安全，尤其是研究者属于边缘群体，或参与者、资助方对研究者有权力时[^aag2024ethics-e17]。
- RGS-IBG 守则说，审查力度应和风险相称，研究弱势或高风险人群要更加小心[^rgsgrantscode-e7]。

### 立场与反思：把"研究工具"本身交代清楚

这一节的写法建议主要来自芬兰学者 Karhulahti 2024 年的一篇短文。它讨论的是各学科的立场声明，不是专门针对地理学；用在地理田野上是本项目的对应 `[本项目分析]`。

**立场**（positionality）指研究者自己和所做研究之间的关系和位置；**立场声明**就是把它写出来[^karhulahti2024positionality-e1]。**反思**（reflexivity）指在研究全程想一想自己的身份、预设和权力怎样影响了资料和解释 `[本项目分析]`。

为什么要在意：研究者本人就是产生一手数据的"工具"时（例如写民族志田野笔记），这个工具的情况应当交代[^karhulahti2024positionality-e2]；田野中只有一小部分互动能被记下来，所以是谁在场、谁挑选了写进笔记的内容很重要[^karhulahti2024positionality-e3]。地理学这边，AAG 的声明也要求地理学者反思自己怎样呈现自己、参与者和地方[^aag2024ethics-e5]。

怎样写：

- 只写和这项研究的方法、题目有关的方面，不要像"购物清单"一样罗列身份[^karhulahti2024positionality-e4]。例如研究外来移民社区时，你是不是本地人、会不会当地语言，可能比其他身份更相关 `[本项目分析]`。
- 进入田野前就写下自己的预设。Karhulahti 认为这和预注册类似，便于及早调整分析[^karhulahti2024positionality-e5]。
- Karhulahti 认为期刊不应强制要求立场声明，而应在适合研究方法时使用[^karhulahti2024positionality-e6]。你的目标期刊要不要，以期刊要求为准 `[本项目分析]`。

### 位置隐私：坐标就是身份信息

- **哪些研究要格外小心。** AAG 的声明在隐私保密一条里列出：自动追踪个人或车辆的位置和移动；用分辨率足以认出个人或车辆的卫星、无人机等影像；用高分辨率位置去关联数据、泄露个人信息；以及任何损害隐私的大数据使用，即使数据被认为是"公开"的[^aag2024ethics-e14]。
- **只收集需要的精度。** Malekzadeh 等人 2026 年的地理隐私伦理指南（作者来自芬兰、加拿大等国，指南属建议性质）建议：只在研究问题确实需要时才收集地理数据；邻里层面的分析未必需要精确的住址坐标[^malekzadeh2026ethical-e2]。
- **同意书要讲清能推断出什么。** 即使不问住址，也常能从反复出现的 GPS 轨迹推出住址和工作地点；要用大白话告诉参与者[^malekzadeh2026ethical-e3]。
- **去掉姓名不等于匿名。** 每天通勤这种独特的移动模式，删掉直接标识后仍能认出人[^malekzadeh2026ethical-e4]。关美宝也提醒，GPS 数据处理不当时，可以通过反向地理编码（由坐标查出地址）认出一个人[^kwan2012uncertain-e9]。
- **地图本身会泄密。** 即使原始数据已匿名，地图仍可能暴露个人或社区；可以汇总到更粗的层级[^malekzadeh2026ethical-e5]，涉及弱势或易被污名化的人群时避免做小区域地图[^malekzadeh2026ethical-e6]。关美宝 2012 年的文章提到的一项健康研究中，参与者的住处、去过的地点和日常路径一律不得印成地图或公开展示[^kwan2012uncertain-e10]。
- **汇总单元也可能敏感。** 邮编区、行政区在人口很少、或关联到特定健康暴露时，可能变得高度敏感[^malekzadeh2026ethical-e7]。
- **共享时分层。** 可以公开汇总或降低分辨率的版本，把精细版本放在受限条件下提供[^malekzadeh2026ethical-e11]。AAG 也提到需要时对数据做概括化处理或用化名[^aag2024ethics-e13]。
- **"网上公开"不等于同意了研究。** 关美宝提醒，社交网站签到这类数据，发布者并不知道、也没同意会被用于研究，可能根本没有知情同意程序[^kwan2012uncertain-e11]。

Malekzadeh 等人的指南按研究阶段列出一系列问题，可以在提交伦理审查前自查[^malekzadeh2026ethical-e9]。据这些作者观察，不少项目因为没想清楚地理数据的伦理问题，在审查中被拖延、要求修改甚至被拒[^malekzadeh2026ethical-e10]。

### 空间分析的陷阱：单元怎么划，结论就可能怎么变

- **可塑性面积单元问题**（modifiable areal unit problem，MAUP）：用按区域汇总的数据分析变量之间的关系时，结果会受区域的大小（尺度效应）和边界怎么划（分区效应）影响[^kwan2018limits-e2]。比如同一城市的数据按街道汇总和按区汇总，收入和健康的相关可能强弱不同 `[本项目分析]`。时间上也有类似问题：按天还是按月汇总，结论也可能不同[^kwan2018limits-e3]。
- **生态谬误**（ecological fallacy）：把区域层面的关系，直接当成个人层面的关系。例如只看到"失业率高的区，犯罪率也高"，不能据此推出"失业的人更容易犯罪"；区里犯罪的人未必是失业的人 `[本项目分析]`。Malekzadeh 等人的指南也提醒，用汇总数据时要处理好生态谬误[^malekzadeh2026ethical-e8]。
- **不确定的地理背景问题**（uncertain geographic context problem，UGCoP）：这是关美宝 2012 年在同名文章中提出的概念 `[本项目分析]`。研究"环境怎样影响个人"时，不知道到底哪片区域在影响这个人，也不知道他在什么时候、多长时间受到影响[^kwan2012uncertain-e3]，所以结论可能随"邻里"怎么划定而变[^kwan2012uncertain-e2]。例如不同研究把邻里定义成住处周围 1 公里或 3 公里的圆、1 公里路网范围等[^kwan2012uncertain-e5]。关美宝认为，在环境影响健康的研究里，这可能是同类研究结论常常不一致的一个主要原因[^kwan2012uncertain-e4]。
- **模型拟合好，不能证明单元选得对。** 关美宝指出，拟合最好的模型不一定用的是真实的地理背景[^kwan2012uncertain-e7]。

怎样应对：明确写出用了什么空间单元、它们离真实的地理背景有多近、考虑了哪些时间因素[^kwan2012uncertain-e6]；用几种尺度或划法做敏感性分析，并全部报告 `[本项目分析]`。条件允许时，可以考虑用个人的**活动空间**（一个人因日常活动和出行到过的所有地点构成的区域[^kwan2012uncertain-e8]）来界定地理背景，而不只用行政区 `[本项目分析]`。

### 可复现与可复制

**可复现**（reproducibility）指用同样的数据和步骤得到一致的结果；**可复制**（replicability）指回答同一问题、各自收集数据的研究得到一致的发现[^kedron2021reproducibility-e1]。

- **空间分析容易"挑设定"。** Kedron 等人（美国的地理信息科学学者）指出：尺度、"相邻"的定义等参数要事先定下，研究者却往往不知道它们的真实取值，可选的"合理设定"就更多[^kedron2021reproducibility-e2]。Kedron 等人举例：一项城市化与空气质量的空间回归研究要选空间权重矩阵（规定哪些城市算相邻）；如果试过很多种只报一种，其余检验就从文献里消失了[^kedron2021reproducibility-e3]。他们建议，地理研究的预分析计划写明分析尺度和要检验的空间权重矩阵[^kedron2021reproducibility-e4]，但也承认地理学界对预注册还探索得很少[^kedron2021reproducibility-e5]。
- **交代怎样把概念变成空间数据。** 要复现地理研究，需要知道空间过程怎样被概念化、怎样测量、怎样在分析中操作化[^kedron2021reproducibility-e13]。
- **换个地方不成立，不一定是失败。** 换了地点、时间或背景后，差异大到什么程度就不该再指望结果重现，还没有定论[^kedron2021reproducibility-e6]；Kedron 等人建议把可复制性看作一个连续谱[^kedron2021reproducibility-e7]。
- **一项小规模评估的结果不乐观。** Nüst 等人 2018 年只评估了一个欧洲地理信息科学会议（AGILE）上的 32 篇论文，都是 2010 年及 2012–2017 年获最佳论文提名的[^nust2018reproducible-e3]。结果没有一篇在任何一项上达到最高可复现等级；32 篇中有 19 篇的数据既拿不到，也无法根据论文重新生成[^nust2018reproducible-e4]。这 32 篇论文的 82 位作者中有 22 位回答了问卷，最常提到的原因是法律限制和没有时间[^nust2018reproducible-e6][^nust2018reproducible-e7]。Nüst 等人还认为，专有（商业闭源）软件最终会成为可复现的致命障碍[^nust2018reproducible-e9]。这个样本很小，只代表这个会议的获提名论文，不能当作整个地理学的情况 `[本项目分析]`。
- **数据不能公开时。** 涉及人的地理数据常常不能共享[^kedron2021reproducibility-e8]。可以公开代码，再发布一份保留原数据空间结构的模拟数据[^kedron2021reproducibility-e9]；Kedron 等人也认为，这类研究不应因此被挡在发表之外[^kedron2021reproducibility-e11]。
- **定性研究也可以留下记录。** 访谈信息、编码和提炼主题的过程，也可以像计算步骤一样记录[^kedron2021reproducibility-e12]；民族志透明到什么程度还有争论，有人主张部分披露人或地点、共享编码方案等折中做法[^jerolmack2024ethnography-e5]，详见[社会学领域篇](../sociology/README.md#定性研究的透明争论还在继续)。

整理数据和代码的通用做法见通用篇[整理科研材料](../../08_throughout/organizing_materials.md)。

---

## 常见的研究类型

**本领域的研究类型文档**：[空间分析研究](research-types/spatial_analysis.md)。

**相关学科的研究类型文档**：[野外观测研究](../earth-environmental-sciences/research-types/field_study.md)。

下面的对应关系和差异说明是本项目的归纳 `[本项目分析]`，具体要求见所附脚注。

- **深度访谈**：见[访谈研究](../../06_methods/interview_study.md)。差异：研究者本人也参与产生数据，要交代自己的立场，见上文"立场与反思" `[本项目分析]`；引用时注意地点细节会不会让人认出受访者[^aag2024ethics-e13]。
- **民族志与地方案例研究**：见[案例研究与民族志](../../06_methods/case_study.md)。差异：案例往往就是一个"地方"，可能涉及跨国田野 `[本项目分析]`，英国 RGS-IBG 资助的项目还要过东道国审查[^rgsgrantscode-e3]；长期田野的伦理细节见[社会学领域篇](../sociology/README.md#民族志特有的难题化名改细节以及怎样让人核查)。
- **定量空间分析与 GIS**：数据处理的通用做法见[数据科学](../../06_methods/data_science.md)。差异：要说明空间单元和"相邻"的定义，并检查结论对它们是否敏感[^kwan2018limits-e2][^kedron2021reproducibility-e4]。
- **GPS 与移动轨迹研究**：用定位设备记录人每天去了哪里，例如用来划出个人的活动空间 `[本项目分析]`。计算机领域篇没有对应类型。差异：隐私风险最高，见上文"位置隐私"[^malekzadeh2026ethical-e4]。
- **混合方法**：见[混合方法](../../06_methods/mixed_methods.md)。一种可能的组合是用空间数据找规律，再用访谈或参与式制图理解原因 `[本项目分析]`。
- **问卷调查**：见[问卷调查](../../06_methods/questionnaire_survey.md)。差异：问卷里的地址、常去地点本身就是敏感信息，只收需要的精度[^malekzadeh2026ethical-e2]。
- **复现研究**：见[复现研究](../../06_methods/replication.md)。差异：先想清楚该期待"复现"还是"在别处复制"[^kedron2021reproducibility-e6]。

---

## 给新手的建议

1. **先定数据的空间精度，再写同意书。** 问自己：回答研究问题到底需要多精确的位置？够用就好[^malekzadeh2026ethical-e2]；同意书里写明从这些数据能推断出什么[^malekzadeh2026ethical-e3]。
2. **在方法部分写清空间单元。** 用什么单元、为什么、离真实的地理背景有多近[^kwan2012uncertain-e6]；再用另一种尺度或划法试一次，结果一并报告 `[本项目分析]`。
3. **试过的设定都记下来。** 每换一次空间权重矩阵或尺度，就是又做了一次检验[^kedron2021reproducibility-e3]；用脚本和版本控制留下记录，见通用篇[整理科研材料](../../08_throughout/organizing_materials.md#3-每个结果都要能追溯到它是怎么来的)。
4. **尽量用开源工具，把分析写成脚本** `[本项目分析]`。Nüst 等人认为专有软件是可复现的致命障碍[^nust2018reproducible-e9]；在他们的评估里，"数据可应要求提供"也算作拿不到[^nust2018reproducible-e5]。
5. **进入田野前写一段立场反思。** 只写和这项研究有关的身份和预设[^karhulahti2024positionality-e4]，田野中随时补充 `[本项目分析]`。
6. **出国做田野，提前查东道国的伦理审查和安全要求。** 可以参考英国 RGS-IBG 对它资助项目的要求：风险评估要针对具体地点写[^rgssaferesearch-e2]，东道国有伦理委员会的也要申请[^rgsgrantscode-e3]；具体以本单位和资助方规定为准 `[本项目分析]`。
7. **发表前把每张地图当作数据来检查。** 问：这张图能让人找到某个参与者的家吗[^malekzadeh2026ethical-e5]？
8. **把结果带回给当地人。** 用他们看得懂的形式[^aag2024ethics-e12]，并在一开始就和当地合作者商定署名[^aag2024ethics-e8][^rgsgrantscode-e5]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只用一种空间单元（如行政区）分析，不说明理由 | 结果会随尺度和分区方式改变[^kwan2018limits-e2]；同类研究结论不一致，可能就出在单元不同[^kwan2012uncertain-e4] |
| 用区域汇总数据，得出关于个人的结论 | 这是生态谬误，区域层面的关系不能直接套到个人身上 `[本项目分析]`[^malekzadeh2026ethical-e8] |
| 拿模型拟合最好来证明"邻里"划得对 | 拟合最好的模型不一定用的是真实的地理背景[^kwan2012uncertain-e7] |
| 试了多种空间权重矩阵，只报告结果最好的那个 | 其余检验从文献中消失，别人无法复现或评估[^kedron2021reproducibility-e3] |
| 删掉姓名就以为 GPS 轨迹已经匿名 | 独特的移动模式本身就能认出人[^malekzadeh2026ethical-e4][^malekzadeh2026ethical-e1] |
| 论文里放参与者住处或日常路径的点位图 | 地图本身会暴露个人[^malekzadeh2026ethical-e5]；有的研究明确禁止这类地图[^kwan2012uncertain-e10] |
| 认为社交媒体上的签到数据"公开"，可以随便用 | AAG 提醒即使数据被认为是公开的，也可能损害隐私[^aag2024ethics-e14]；发布者并未同意被研究[^kwan2012uncertain-e11] |
| 本单位批了伦理审查，就不管东道国的审查 | 英国 RGS-IBG 要求它资助的项目在东道国有伦理委员会时也经其批准[^rgsgrantscode-e3] |
| 套用模板写田野风险评估 | RGS-IBG 要求申请人针对具体地点和研究性质写[^rgssaferesearch-e2] |
| 立场声明写成一串身份标签 | 应只写和这项研究有关的方面[^karhulahti2024positionality-e4] |
| 田野结束就走，不回馈当地 | AAG 要求在合适时以对方看得懂的形式分享结果[^aag2024ethics-e12]；RGS-IBG 守则要求当地人参与到研究后的反馈[^rgsgrantscode-e4] |

---

## 延伸阅读

- **AAG Statement of Professional Ethics（2024 年修订）**：美国地理学家协会给会员的伦理声明，田野、同意、地理空间技术和隐私、资金披露都有专门条款。开始涉及人或地方的研究前读。
- **RGS-IBG 资助项目守则和安全伦理说明**：英国皇家地理学会给它资助的项目定的规则，篇幅短，讲东道国审查、当地合作者、出行理由和风险评估。准备出国田野时读。
- **Kwan 2012，The Uncertain Geographic Context Problem**，以及 **Kwan 2018，The Limits of the Neighborhood Effect**：讲清空间单元和地理背景怎样左右结论（作者主页有全文）。做邻里效应、环境暴露类研究前读。
- **Kedron 等 2021，Reproducibility and replicability: opportunities and challenges for geospatial research**：地理研究为什么容易挑设定、预分析计划该写什么、数据不能公开时怎么办。
- **Nüst 等 2018，Reproducible research and GIScience**：对 AGILE 会议 32 篇论文的可复现性评估，附给作者的具体建议（开放获取）。
- **Malekzadeh 等 2026，Ethical guidelines for geoprivacy**：按研究阶段列出的地理隐私自查问题（开放获取）。写伦理申请前逐条对照。
- **Karhulahti 2024，Positionality statements in science**：一篇跨学科的短文，讲立场声明有什么用、怎样写才不流于形式（开放获取）。

[^aag2024ethics-e1]: AAG Statement of Professional Ethics（2024），I. Preamble。[证据](../../../sources/notes/aag2024ethics.md#e1)
[^aag2024ethics-e2]: AAG Statement of Professional Ethics，I. Preamble。[证据](../../../sources/notes/aag2024ethics.md#e2)
[^aag2024ethics-e3]: AAG Statement of Professional Ethics，II. Do Good。[证据](../../../sources/notes/aag2024ethics.md#e3)
[^aag2024ethics-e4]: AAG Statement of Professional Ethics，II. Respect Research Participants。[证据](../../../sources/notes/aag2024ethics.md#e4)
[^aag2024ethics-e5]: AAG Statement of Professional Ethics，II. Respect Research Participants。[证据](../../../sources/notes/aag2024ethics.md#e5)
[^aag2024ethics-e6]: AAG Statement of Professional Ethics，III. Do No Harm。[证据](../../../sources/notes/aag2024ethics.md#e6)
[^aag2024ethics-e7]: AAG Statement of Professional Ethics，III. Recognize Power Hierarchies。[证据](../../../sources/notes/aag2024ethics.md#e7)
[^aag2024ethics-e8]: AAG Statement of Professional Ethics，IV. Collaborate with Care。[证据](../../../sources/notes/aag2024ethics.md#e8)
[^aag2024ethics-e9]: AAG Statement of Professional Ethics，VI. Obtain Informed Consent。[证据](../../../sources/notes/aag2024ethics.md#e9)
[^aag2024ethics-e10]: AAG Statement of Professional Ethics，VI. Obtain Institutional Approval。[证据](../../../sources/notes/aag2024ethics.md#e10)
[^aag2024ethics-e11]: AAG Statement of Professional Ethics，VI. Take Informed Consent Seriously。[证据](../../../sources/notes/aag2024ethics.md#e11)
[^aag2024ethics-e12]: AAG Statement of Professional Ethics，VI. Share Findings。[证据](../../../sources/notes/aag2024ethics.md#e12)
[^aag2024ethics-e13]: AAG Statement of Professional Ethics，VI. Make Data Available。[证据](../../../sources/notes/aag2024ethics.md#e13)
[^aag2024ethics-e14]: AAG Statement of Professional Ethics，VI. Protect Privacy and Confidentiality。[证据](../../../sources/notes/aag2024ethics.md#e14)
[^aag2024ethics-e15]: AAG Statement of Professional Ethics，VII. Disclose Funding Sources。[证据](../../../sources/notes/aag2024ethics.md#e15)
[^aag2024ethics-e16]: AAG Statement of Professional Ethics，VII. Be Transparent。[证据](../../../sources/notes/aag2024ethics.md#e16)
[^aag2024ethics-e17]: AAG Statement of Professional Ethics，VIII. Weigh Competing Ethical Obligations。[证据](../../../sources/notes/aag2024ethics.md#e17)
[^aag2024ethics-e18]: AAG Statement of Professional Ethics，页首修订记录。[证据](../../../sources/notes/aag2024ethics.md#e18)
[^rgsgrantscode-e1]: RGS-IBG Code of Practice for the Grants Programme，伦理条款段首。[证据](../../../sources/notes/rgsgrantscode.md#e1)
[^rgsgrantscode-e3]: RGS-IBG Code of Practice for the Grants Programme，伦理条款。[证据](../../../sources/notes/rgsgrantscode.md#e3)
[^rgsgrantscode-e4]: RGS-IBG Code of Practice for the Grants Programme，伦理条款。[证据](../../../sources/notes/rgsgrantscode.md#e4)
[^rgsgrantscode-e5]: RGS-IBG Code of Practice for the Grants Programme，伦理条款。[证据](../../../sources/notes/rgsgrantscode.md#e5)
[^rgsgrantscode-e6]: RGS-IBG Code of Practice for the Grants Programme，可持续研究条款。[证据](../../../sources/notes/rgsgrantscode.md#e6)
[^rgsgrantscode-e7]: RGS-IBG Code of Practice for the Grants Programme，伦理条款。[证据](../../../sources/notes/rgsgrantscode.md#e7)
[^rgssaferesearch-e1]: RGS-IBG，Safe, responsible and ethical research，开头。[证据](../../../sources/notes/rgssaferesearch.md#e1)
[^rgssaferesearch-e2]: RGS-IBG，Safe, responsible and ethical research，风险评估段。[证据](../../../sources/notes/rgssaferesearch.md#e2)
[^rgssaferesearch-e3]: RGS-IBG，Safe, responsible and ethical research，伦理评估段。[证据](../../../sources/notes/rgssaferesearch.md#e3)
[^karhulahti2024positionality-e1]: Karhulahti 2024，Introduction。[证据](../../../sources/notes/karhulahti2024positionality.md#e1)
[^karhulahti2024positionality-e2]: Karhulahti 2024，What positionality does。[证据](../../../sources/notes/karhulahti2024positionality.md#e2)
[^karhulahti2024positionality-e3]: Karhulahti 2024，What positionality does。[证据](../../../sources/notes/karhulahti2024positionality.md#e3)
[^karhulahti2024positionality-e4]: Karhulahti 2024，Two common misunderstandings。[证据](../../../sources/notes/karhulahti2024positionality.md#e4)
[^karhulahti2024positionality-e5]: Karhulahti 2024，What positionality does。[证据](../../../sources/notes/karhulahti2024positionality.md#e5)
[^karhulahti2024positionality-e6]: Karhulahti 2024，Two common misunderstandings。[证据](../../../sources/notes/karhulahti2024positionality.md#e6)
[^malekzadeh2026ethical-e1]: Malekzadeh 等 2026，Introduction。[证据](../../../sources/notes/malekzadeh2026ethical.md#e1)
[^malekzadeh2026ethical-e2]: Malekzadeh 等 2026，Data collection，Q2。[证据](../../../sources/notes/malekzadeh2026ethical.md#e2)
[^malekzadeh2026ethical-e3]: Malekzadeh 等 2026，Data collection，Q4。[证据](../../../sources/notes/malekzadeh2026ethical.md#e3)
[^malekzadeh2026ethical-e4]: Malekzadeh 等 2026，Q24。[证据](../../../sources/notes/malekzadeh2026ethical.md#e4)
[^malekzadeh2026ethical-e5]: Malekzadeh 等 2026，Results dissemination，Q59。[证据](../../../sources/notes/malekzadeh2026ethical.md#e5)
[^malekzadeh2026ethical-e6]: Malekzadeh 等 2026，Results dissemination，Q59。[证据](../../../sources/notes/malekzadeh2026ethical.md#e6)
[^malekzadeh2026ethical-e7]: Malekzadeh 等 2026，Ethical questions 一节导言。[证据](../../../sources/notes/malekzadeh2026ethical.md#e7)
[^malekzadeh2026ethical-e8]: Malekzadeh 等 2026，Data analysis，Q53。[证据](../../../sources/notes/malekzadeh2026ethical.md#e8)
[^malekzadeh2026ethical-e9]: Malekzadeh 等 2026，Ethical questions for geographic data privacy in research。[证据](../../../sources/notes/malekzadeh2026ethical.md#e9)
[^malekzadeh2026ethical-e10]: Malekzadeh 等 2026，Introduction。[证据](../../../sources/notes/malekzadeh2026ethical.md#e10)
[^malekzadeh2026ethical-e11]: Malekzadeh 等 2026，Data sharing，Q34。[证据](../../../sources/notes/malekzadeh2026ethical.md#e11)
[^kwan2012uncertain-e2]: Kwan 2012，第 959 页。[证据](../../../sources/notes/kwan2012uncertain.md#e2)
[^kwan2012uncertain-e3]: Kwan 2012，第 959 页。[证据](../../../sources/notes/kwan2012uncertain.md#e3)
[^kwan2012uncertain-e4]: Kwan 2012，第 959 页。[证据](../../../sources/notes/kwan2012uncertain.md#e4)
[^kwan2012uncertain-e5]: Kwan 2012，第 960 页。[证据](../../../sources/notes/kwan2012uncertain.md#e5)
[^kwan2012uncertain-e6]: Kwan 2012，第 963 页。[证据](../../../sources/notes/kwan2012uncertain.md#e6)
[^kwan2012uncertain-e7]: Kwan 2012，第 963–964 页。[证据](../../../sources/notes/kwan2012uncertain.md#e7)
[^kwan2012uncertain-e8]: Kwan 2012，第 964 页。[证据](../../../sources/notes/kwan2012uncertain.md#e8)
[^kwan2012uncertain-e9]: Kwan 2012，第 966 页注 2。[证据](../../../sources/notes/kwan2012uncertain.md#e9)
[^kwan2012uncertain-e10]: Kwan 2012，第 966 页注 2。[证据](../../../sources/notes/kwan2012uncertain.md#e10)
[^kwan2012uncertain-e11]: Kwan 2012，第 966 页注 2。[证据](../../../sources/notes/kwan2012uncertain.md#e11)
[^kwan2018limits-e2]: Kwan 2018，第 1486 页。[证据](../../../sources/notes/kwan2018limits.md#e2)
[^kwan2018limits-e3]: Kwan 2018，第 1486 页。[证据](../../../sources/notes/kwan2018limits.md#e3)
[^kwan2018limits-e4]: Kwan 2018，第 1488 页。[证据](../../../sources/notes/kwan2018limits.md#e4)
[^kedron2021reproducibility-e1]: Kedron 等 2021，§1 Introduction。[证据](../../../sources/notes/kedron2021reproducibility.md#e1)
[^kedron2021reproducibility-e2]: Kedron 等 2021，§2。[证据](../../../sources/notes/kedron2021reproducibility.md#e2)
[^kedron2021reproducibility-e3]: Kedron 等 2021，§2。[证据](../../../sources/notes/kedron2021reproducibility.md#e3)
[^kedron2021reproducibility-e4]: Kedron 等 2021，§3.1。[证据](../../../sources/notes/kedron2021reproducibility.md#e4)
[^kedron2021reproducibility-e5]: Kedron 等 2021，§3.1。[证据](../../../sources/notes/kedron2021reproducibility.md#e5)
[^kedron2021reproducibility-e6]: Kedron 等 2021，§4.1。[证据](../../../sources/notes/kedron2021reproducibility.md#e6)
[^kedron2021reproducibility-e7]: Kedron 等 2021，§4.1。[证据](../../../sources/notes/kedron2021reproducibility.md#e7)
[^kedron2021reproducibility-e8]: Kedron 等 2021，§3.2。[证据](../../../sources/notes/kedron2021reproducibility.md#e8)
[^kedron2021reproducibility-e9]: Kedron 等 2021，§3.2。[证据](../../../sources/notes/kedron2021reproducibility.md#e9)
[^kedron2021reproducibility-e10]: Kedron 等 2021，§3.2。[证据](../../../sources/notes/kedron2021reproducibility.md#e10)
[^kedron2021reproducibility-e11]: Kedron 等 2021，§3.2。[证据](../../../sources/notes/kedron2021reproducibility.md#e11)
[^kedron2021reproducibility-e12]: Kedron 等 2021，§3.1。[证据](../../../sources/notes/kedron2021reproducibility.md#e12)
[^kedron2021reproducibility-e13]: Kedron 等 2021，§4.2。[证据](../../../sources/notes/kedron2021reproducibility.md#e13)
[^nust2018reproducible-e1]: Nüst 等 2018，Introduction。[证据](../../../sources/notes/nust2018reproducible.md#e1)
[^nust2018reproducible-e2]: Nüst 等 2018，Materials & Methods。[证据](../../../sources/notes/nust2018reproducible.md#e2)
[^nust2018reproducible-e3]: Nüst 等 2018，Materials & Methods。[证据](../../../sources/notes/nust2018reproducible.md#e3)
[^nust2018reproducible-e4]: Nüst 等 2018，Results。[证据](../../../sources/notes/nust2018reproducible.md#e4)
[^nust2018reproducible-e5]: Nüst 等 2018，Materials & Methods，Definition and criteria。[证据](../../../sources/notes/nust2018reproducible.md#e5)
[^nust2018reproducible-e6]: Nüst 等 2018，Results，Author feedback。[证据](../../../sources/notes/nust2018reproducible.md#e6)
[^nust2018reproducible-e7]: Nüst 等 2018，Results，Author feedback。[证据](../../../sources/notes/nust2018reproducible.md#e7)
[^nust2018reproducible-e9]: Nüst 等 2018，Discussion，Suggestions to authors。[证据](../../../sources/notes/nust2018reproducible.md#e9)
[^jerolmack2024ethnography-e5]: Jerolmack, Murphy & Reyes 2024，第 2 段。[证据](../../../sources/notes/jerolmack2024ethnography.md#e5)
