# 地球与环境科学：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲地球与环境科学（地质、地球物理、大气与气候、海洋、水文，以及和生态相邻的环境科学）的研究里几件具体的事：野外工作、样品、数值模式、模式比较计划，以及数据、代码和不确定性怎样报告。各学科共通的做法（选题、做计划、写作、审稿、科研伦理）见[通用篇](../../general/README.md)。采样计划、质量控制样品、检出限这类测量问题，见[环境工程](../environmental-engineering/README.md)；以实验室为主的生态和生命科学研究，见[生物科学](../biological-sciences/README.md)；考古发掘的伦理，见[历史与考古](../history-archaeology/README.md)。

本文的规范类资料主要来自三家，各管各的：**美国地球物理学会**（American Geophysical Union，AGU）的伦理政策管它的会员和参加其活动的人，它的数据指南管投 AGU 期刊的稿件；期刊**《地球科学模式开发》**（Geoscientific Model Development，GMD，欧洲地球科学联合会 EGU 旗下、由出版社 Copernicus 出版）的代码政策只管投 GMD 的稿件；**政府间气候变化专门委员会**（Intergovernmental Panel on Climate Change，IPCC）的不确定性指南是写给它的评估报告作者的。它们都不是全学科的统一规定。你所在国家、单位和目标期刊的要求，以它们自己的规定为准 `[本项目分析]`。

**读完本文，你应该能：**

- 出发做野外工作之前，做好安全、许可和伦理方面的准备；
- 管理样品编号、数据和模型代码，写出合格的"数据与软件可获取性声明"；
- 看懂 IPCC 的不确定性用语，知道它是为谁定的；发预印本前知道要查什么。

---

## 本领域研究怎样运转

### 三种工作方式，常在一个项目里交织

`[本项目分析]` 本领域的研究大体有三种工作方式，一个项目常同时用到几种。野外季节怎样安排、观测网络怎样组织，本文资料未涉及，以导师和本组的惯例为准。

| 工作方式 | 做什么 | 本文对应的部分 |
|---|---|---|
| 野外观测和采样 | 去现场测量、布设仪器，采集岩石、沉积物、水、冰芯等样品 | [野外工作](#野外工作先把安全和许可办好)、[样品](#样品给每个样品一个永久编号) |
| 实验室分析 | 对样品做化学、物理测定 | [样品](#样品给每个样品一个永久编号)；测量的质量控制见[环境工程](../environmental-engineering/README.md) |
| 数值模拟 | 用数值模式（numerical model，用计算机求解描述地球系统的方程）模拟大气、海洋、地下水等 | [模式和代码](#数值模式代码没准备好论文就没准备好) |

### 模式比较计划

气候方向有一种大合作：**模式比较计划**（Model Intercomparison Project，MIP）。最有名的是**耦合模式比较计划**（Coupled Model Intercomparison Project，CMIP）。据 CMIP 第六期（CMIP6）的概述论文（Eyring 等 2016），CMIP 协调全球气候模式对过去、现在和未来气候的模拟设计和数据分发，已成为气候科学的基础之一[^eyring2016cmip6-e1]；它的目标是在多个模式的框架下更好地理解气候变化[^eyring2016cmip6-e4]。

在 CMIP6 里，一个模式要参加，必须跑一组叫 DECK 的规定试验和 CMIP 历史模拟，并采用 CMIP 的数据标准；之后参加哪些专题比较计划，由各建模组按自己的科学兴趣决定[^eyring2016cmip6-e2][^eyring2016cmip6-e3]。DECK 具体包括哪些试验，本文只读了这篇论文的摘要和引言首段，没有涉及，需要时读原文。

对新手来说 `[本项目分析]`：你可能不自己开发模式，而是用某个机构的模式，或分析 CMIP 已公开的输出，这时要把模式版本、试验名称和数据标准写进论文。另外，GMD 编辑部指出，一些地球系统模式由大机构控制，许可证受限[^gmd2019editorial-e6]。用之前先问清楚：将来论文里的代码声明怎么写 `[本项目分析]`。

### 发表：期刊、公开审稿和数据论文

- **期刊**：本文找到的规范都来自期刊和学会 `[本项目分析]`；审稿周期等数字本文资料未涉及，以目标期刊公布的为准。
- **公开审稿**：EGU 期刊公开审稿的核心想法是，投稿和审稿过程都公开、长期可查[^gmd2019editorial-e9]。GMD 要求投稿时就提供代码和数据，不接受"录用后再公开"[^gmdcodepolicy-e4]。
- **数据论文**：Copernicus 有专门发表数据论文、并对数据集做同行评审的期刊《地球系统科学数据》（Earth System Science Data，ESSD）[^gmdcodepolicy-e10]。也就是说，一套整理好的数据集本身可以投稿。
- **署名**：AGU 伦理政策要求只把有重要科学贡献的人列为合作者，按贡献排序，并特别注意学生工作的署名[^agu2023ethics-e9]。野外帮工、提供样品的人算不算作者，本文资料没有规定，开工前和导师说清楚 `[本项目分析]`。通用做法见通用篇[科研诚信与伦理](../../general/4_throughout/02_integrity_and_ethics.md#5-署名和引用给每个贡献者应得的认可)。

### 预印本：EarthArXiv

**EarthArXiv** 自 2017 年运行，收地球科学各方向和相关行星科学的稿件[^eartharxivabout-e1]。每篇都有 DOI（数字对象标识符，一种永久链接），可以被引用[^eartharxivabout-e2]。它不评估稿件的科学质量，也就是不做同行评审[^eartharxivabout-e3]。它的常见问题页还提到 AGU 的预印本平台 ESSOAr（地球与空间科学开放存档），作为另一个选择[^eartharxivfaq-e6]。

发预印本前要知道（以下都是 EarthArXiv 的规定）：

- **发出去就删不掉**，只能更新[^eartharxivfaq-e1]；期刊拒稿后，预印本仍然公开[^eartharxivfaq-e4]。
- **先查期刊政策**：把论文可能依次投的所有期刊都查一遍，确认它们接受预印本[^eartharxivfaq-e5]。
- **写明身份**：稿件上要写清"这是未经同行评审的 EarthArXiv 预印本"[^eartharxivmoderation-e2]。**收什么**：不支持假设的"零结果"可以投[^eartharxivmoderation-e1]；学位论文和课程作业不收[^eartharxivmoderation-e3]。
- **数据和代码放别处**：EarthArXiv 不存补充材料，只能链接到别处[^eartharxivfaq-e7]。预印本和正式论文各有 DOI，引用可能指向任何一个[^eartharxivfaq-e2]。

---

## 和其他学科不同的地方

| 方面 | 地球与环境科学 | 对照 |
|---|---|---|
| 研究对象 | 有些样品再也采不到[^igsnabout-e4] | 计算机研究的对象多半可以在机器上重新运行 `[本项目分析]` |
| 实物样品 | 有专用的永久编号 IGSN[^igsnabout-e2] | 生物学的抗体、细胞系另有标识规范，见[生物科学](../biological-sciences/README.md) |
| 模型代码 | GMD 要求投稿时就提供确切版本，否则拒稿[^gmdcodepolicy-e3][^gmdcodepolicy-e4] | 计算机部分方向在录用后另做制品评估，见[计算机篇](../computer-science/README.md#制品评估与徽章) |
| 不确定性表达 | IPCC 评估报告用固定的用语[^mastrandrea2010ipcc-e4][^mastrandrea2010ipcc-e6] | 本文资料只涉及 IPCC 这一套 `[本项目分析]` |

---

## 本领域的规范和报告标准

### 野外工作：先把安全和许可办好

AGU 的伦理政策管它的会员、员工、志愿者和参加 AGU 活动的人[^agu2023ethics-e1]。它把野外和课堂、实验室、会议并列，都要求良好行为[^agu2023ethics-e2]；在这份政策里，歧视、骚扰（含性骚扰）和霸凌**属于科研不端**[^agu2023ethics-e3]。

野外有哪些风险，一个参考是 Clancy 等 2014 年发表的调查。它在 2013 年做网上问卷，666 人作答，约四分之三来自美国[^clancy2014survey-e1][^clancy2014survey-e3][^clancy2014survey-e4]。受访者近一半是人类学者，地质学者只有 29 人[^clancy2014survey-e2]。所以它说的不是地球科学的情况。作者也说明，这种调查不能用来估计任何学科里这类事有多普遍[^clancy2014survey-e7]。

在这 666 名受访者中，只有 37.7% 记得在工作过的野外站点见过行为准则[^clancy2014survey-e5]；骚扰和侵害绝大多数针对学生、博士后和雇员[^clancy2014survey-e6]；很少有人知道怎样举报[^clancy2014survey-e9]。作者还指出：学生有时在不归本校管理的站点工作，如果没有明确执行的政策，行为规范就更难立起来[^clancy2014survey-e8]。

出发前可以对照一份清单：Greene 等 2021 年为**教学野外实习**写的检查清单。作者是英国高校地理、地球与环境科学方向的师生[^greene2021safety-e1]；它是未经同行评审的预印本。下面几条，科研野外也可以参考；单位有自己的野外安全制度和表格的，以单位的为准 `[本项目分析]`：

- **许可**：守法只是底线。先查要去的地点是否受保护（不只岩石，也包括生物和环境）[^greene2021safety-e2]；办好进入许可、采样许可，需要时办样品进出口许可[^greene2021safety-e3]。
- **伦理**：这是谁的土地，当地人有没有参与，他们有没有受益、至少没有受损[^greene2021safety-e4]。涉及原住民的数据，AGU 期刊数据指南要求参考 CARE 原则（原住民数据治理原则）[^fox2021agudata-e2]。
- **风险评估**：由第三方审核，出发前告诉所有参与者[^greene2021safety-e5]；看往年的事故和险情记录[^greene2021safety-e7]。
- **急救**：查清出事打给谁、最近的医院在哪[^greene2021safety-e6]。只靠急救培训不够[^greene2021safety-e10]。
- **日程和人**：除了季节天气和潮汐，也考虑宗教节日[^greene2021safety-e9]；规划时把参与者的身份和背景考虑进去[^greene2021safety-e8]。

### 样品：给每个样品一个永久编号

IGSN 组织认为，样品数据难以长期利用，主要是因为：论文里样品记录不完整，样品名称有歧义，找不到样品存在哪里[^igsnabout-e1]。**国际通用样品编号**（International Generic Sample Number，IGSN）就是为此设的：给实物样品用的全球唯一、永久的编号[^igsnabout-e2]，样品从注册到分析、发表都能被追踪[^igsnabout-e3]。它起源于地球科学，现在面向所有学科[^igsnabout-e5]。

据 IGSN 组织的说明：IGSN 的机器可读形式是完整的 https://doi.org/ 链接[^igsnpublications-e2]；给样品袋贴二维码时，标签上还要印出人能读的编号[^igsnpublications-e3]；自 2017 年 5 月起，Copernicus 的地球科学期刊都能在文章"资产"栏列出 IGSN[^igsnpublications-e1][^gmdcodepolicy-e9]。怎样注册 IGSN、国内有没有对应渠道，本文资料未涉及，问导师或单位的数据管理部门。样品唯一编号和"监管链"（记录样品每一步由谁经手）的做法，另见[环境工程篇](../environmental-engineering/README.md#样品编号和监管链)。

### 数据：投稿时就要能拿到

**AGU 期刊**的要求（据 Fox 等 2021 年写的 AGU 期刊数据与软件共享指南）：

- 投稿时，数据和软件就必须能让编辑和审稿人拿到[^fox2021agudata-e3]；
- 原则是"尽可能开放，必要时才封闭"[^fox2021agudata-e2]，敏感数据（例如化石产地位置）也要存进有访问控制的存储库[^fox2021agudata-e4]；写"数据可向作者索取"不合格，只给一个大网站首页也不合格[^fox2021agudata-e6]；
- 原始数据和处理后的数据都要写进参考文献，数据的贡献者才能得到认可[^fox2021agudata-e12]；
- 选存储库从写项目申请和数据管理计划时就开始[^fox2021agudata-e9]；超过 1 TB 的数据，有些存储库可以付费保存，要写进预算[^fox2021agudata-e10]；图书馆员可以帮忙选库[^fox2021agudata-e11]。
- AGU 伦理政策另外要求：论文要写到同行能重复这项工作的程度，数据有使用限制的要写清[^agu2023ethics-e7]。

**为什么值得认真做？** Stagge 等 2019 年的一项研究，从六种水文与水资源期刊 2017 年发表的 1989 篇论文里抽查了 360 篇[^stagge2019assessing-e1]：

- 70.3% 声称有材料可用，但其中只有 48.6% 能在网上真正拿到[^stagge2019assessing-e9]；
- 只有 1.6% 能用公开材料复现结果；推算到全部 1989 篇，可复现比例在 0.6%–6.8% 之间[^stagge2019assessing-e8]；
- 复现失败的常见问题是路径写死在作者电脑上[^stagge2019assessing-e4]；另一些论文只指向笼统的数据门户，或依赖昂贵的商业软件[^stagge2019assessing-e11]。

每种期刊里，给了代码或数据的论文数，都是给了使用说明的论文数的 2 到 3 倍[^stagge2019assessing-e12]。作者建议，投稿前用他们的问卷当清单自查[^stagge2019assessing-e13]。整理数据的通用做法见通用篇[整理科研材料](../../general/2_during/03_organizing_materials.md)。

### 数值模式：代码没准备好，论文就没准备好

这是 GMD 编辑部 2019 年社论里的看法[^gmd2019editorial-e7]。理由是：

- 几乎所有不简单的代码都有错误[^gmd2019editorial-e2]；两个实现同一算法的程序，结果也未必相同，没有源代码就查不出差异从哪来[^gmd2019editorial-e3]。光有源代码也不够，还要有全部输入数据，并知道从原始数据到图上每个点的全部步骤[^gmd2019editorial-e4]；
- 交互式手工处理和画图会切断模型和论文之间的"来源链"，唯一的补救是全部用脚本运行和处理[^gmd2019editorial-e5]；代码没管理好，事后还可能找不回论文用的确切版本[^gmd2019editorial-e8]。

**GMD 的要求**（只管投 GMD 的稿件）：

- 论文末尾设"代码与数据可获取性"一节[^gmdcodepolicy-e1]，引用全部代码和数据的**确切版本**，存在永久公开存档里[^gmdcodepolicy-e2]；
- 不能公开的，必须私下提供给编辑和审稿人，做不到就拒稿[^gmdcodepolicy-e3]；
- 要提供覆盖每一步数据处理的脚本[^gmdcodepolicy-e5]；修改稿期间代码和数据变了，新版本也要存档[^gmdcodepolicy-e7]；GitHub 等代码托管平台适合开发，不适合存档[^gmdcodepolicy-e6]（AGU 期刊指南也不认它为保存库[^fox2021agudata-e5]）；可以另外给出最新版的下载地址[^gmd2019editorial-e10]；
- 审稿时可能检查模型是否容易下载、编译、跑通测试算例[^gmdcodepolicy-e8]。

**AGU 期刊**对模式研究的要求：提供到"有足够算力的读者能重复你的模拟"的程度[^fox2021agudata-e7]；海量输出难以全存，存够画论文图表的部分一般就够了[^fox2021agudata-e8]；分析和画图的代码放在开放平台，并存档到 Zenodo 这类保存库[^fox2021agudata-e15]。

### 表达不确定性：IPCC 的用语

AGU 伦理政策要求会员报告结果时包括对不确定性的刻画[^agu2023ethics-e4]，并认真记录方法、假设和不确定性[^agu2023ethics-e8]。气候方向常见的一套用语，来自 IPCC 2010 年写给第五次评估报告主要作者的指南（Mastrandrea 等 2010）[^mastrandrea2010ipcc-e1]。它用两种度量：

- **信度**（confidence）：根据证据的类型、数量、质量、一致性和各方一致的程度来判断，用文字表达[^mastrandrea2010ipcc-e2]，分很低、低、中等、高、很高五级[^mastrandrea2010ipcc-e4]。信度不是概率，也不同于统计学的"置信度"[^mastrandrea2010ipcc-e5]。
- **可能性**（likelihood）：用概率表达的定量不确定性[^mastrandrea2010ipcc-e3]，每个词对应一个概率区间[^mastrandrea2010ipcc-e6]：

| 英文用语 | 概率 |
|---|---|
| virtually certain | 99%–100% |
| very likely | 90%–100% |
| likely | 66%–100% |
| about as likely as not | 33%–66% |
| unlikely | 0–33% |
| very unlikely | 0–10% |
| exceptionally unlikely | 0–1% |

指南还提醒报告作者：

- "about as likely as not"不能用来表示"不知道"[^mastrandrea2010ipcc-e7]；信息足够时，最好直接给概率分布或区间[^mastrandrea2010ipcc-e8]。
- 做专家判断时，给出"可追溯的说明"，交代判断依据[^mastrandrea2010ipcc-e9]；警惕团体讨论时意见趋同、过度自信[^mastrandrea2010ipcc-e10]；专家容易低估结构不确定性，也就是对系统理解不完整带来的不确定性[^mastrandrea2010ipcc-e11]。
- 同一结论换一种说法，读者的理解就不同[^mastrandrea2010ipcc-e12]；读者还会按后果轻重调整对这些用词的理解[^mastrandrea2010ipcc-e14]。指南鼓励给出关键变量分布"尾部"的信息[^mastrandrea2010ipcc-e13]。

`[本项目分析]` 这套用语是为 IPCC 评估报告定的。普通研究论文要不要用、怎么用，看目标期刊和导师的意见；用的时候注明出处，别让读者把"likely"当成日常口语。

**对公众说话**：AGU 伦理政策要求，只有证据强到足以在学术文献上发表时，才向公众宣布发现[^agu2023ethics-e10]；并认为会员有义务向公众负责、准确、清楚地说明自然资源、灾害等问题[^agu2023ethics-e6]。

---

## 常见的研究类型

| 研究类型 | 一句话说明 | 和计算机篇的关系 |
|---|---|---|
| 野外观测与采样 | 去现场测量、采样，为后续分析提供数据 `[本项目分析]` | 计算机篇没有对应类型；安全和许可见上文 |
| 样品的实验室分析 | 对岩石、水、冰芯等样品做测定 `[本项目分析]` | 计算机篇没有对应类型；样品编号见上文，测量质量控制见[环境工程](../environmental-engineering/README.md) |
| 数值模拟与模式开发 | 用数值模式模拟地球系统，或开发、评估模式 `[本项目分析]` | 相通：[定量仿真](../computer-science/research-types/simulation_study.md)。差异：GMD 要求投稿时就提供确切版本的代码和数据，否则拒稿[^gmdcodepolicy-e3]；有些地球系统模式许可受限[^gmd2019editorial-e6] |
| 多模式比较 | 按统一协调的试验设计，在多个模式的框架下研究气候[^eyring2016cmip6-e1][^eyring2016cmip6-e4] | 相通：[基准评测](../computer-science/research-types/benchmarking.md)。差异：参加 CMIP 的模式要跑规定试验、采用共同的数据标准[^eyring2016cmip6-e2] |
| 用已有观测数据做分析 | 分析卫星、站网等已有数据 `[本项目分析]` | 相通：[数据科学研究](../computer-science/research-types/data_science.md)。差异：投 AGU 期刊时，要给出数据的具体来源，不能只给门户网站[^fox2021agudata-e6] |
| 数据论文 | 整理一套数据集发表，数据集本身接受评审[^gmdcodepolicy-e10] | 计算机篇没有对应类型 |

---

## 给新手的建议

1. **第一次出野外前，做完风险评估、拿齐许可。** 进入、采样，需要时还有进出口许可[^greene2021safety-e3]；风险评估要有人审核，并告诉所有同行者[^greene2021safety-e5]。
2. **出发前问清怎样举报不当行为。** 在 Clancy 2014 那项 666 人的调查里，很少有受访者知道怎样举报[^clancy2014survey-e9]；问清站点归谁管、适用哪份行为准则 `[本项目分析]`。
3. **采样当天就给样品编号、做记录** `[本项目分析]`。记录不全、名称含糊，是样品数据难以利用的主要问题[^igsnabout-e1]；能注册 IGSN 就注册[^igsnabout-e2]。
4. **从第一天起全部用脚本处理数据和画图。** 手工处理会切断来源链[^gmd2019editorial-e5]；不要把路径写死在自己电脑上[^stagge2019assessing-e4]。
5. **代码和数据放在一起，写好使用说明。** 在 Stagge 2019 的抽查里，给了代码或数据的论文远多于给了使用说明的[^stagge2019assessing-e12]；代码和数据打包在一起的项目更容易复现[^stagge2019assessing-e14]。
6. **投稿前把代码和数据存档，拿到 DOI。** GMD 和 AGU 期刊都要求投稿时就能拿到[^gmdcodepolicy-e4][^fox2021agudata-e3]；GitHub 不算存档[^gmdcodepolicy-e6]。
7. **写"likely""high confidence"之前，先查 IPCC 的定义。** 这些词在 IPCC 用语里有固定含义[^mastrandrea2010ipcc-e5][^mastrandrea2010ipcc-e6]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只办了进入许可，没办采样或进出口许可 | 许可要逐项办齐[^greene2021safety-e3] |
| 样品名只有自己看得懂，记录不全 | 正是样品数据难以利用的主要问题[^igsnabout-e1] |
| 数据声明写"可向作者索取" | AGU 期刊不接受[^fox2021agudata-e6]；在 HESS、WRR 两种水文期刊 2017 年的抽查论文里，38.5%–40.2% 的材料只能向第一作者索取[^stagge2019assessing-e10] |
| 只放 GitHub 链接，不做存档 | GitHub 不是存档服务[^gmdcodepolicy-e6][^fox2021agudata-e5] |
| 用"about as likely as not"表示"不知道" | IPCC 指南明确不许这样用[^mastrandrea2010ipcc-e7] |
| 发预印本前没查后续可能投的期刊 | 预印本删不掉[^eartharxivfaq-e1]；EarthArXiv 要求先确认这些期刊都接受预印本[^eartharxivfaq-e5] |

---

## 延伸阅读

- **AGU Scientific Integrity and Professional Ethics（2023 更新版）**：AGU 的伦理政策。想了解它怎样看待骚扰，读第 III.D 部分。
- **Data and Software Sharing Guidance for Authors Submitting to AGU Journals（Fox 等 2021）**：投 AGU 期刊前对照写数据和软件声明。
- **GMD 代码与数据政策和 2019 年编辑部社论**：讲为什么要公开代码、怎样存档。**IPCC 不确定性指南（Mastrandrea 等 2010）**：4 页，讲信度和可能性。
- **Stagge 等 2019**：对六种水文期刊的复现抽查，能看到"材料公开了却复现不了"的具体原因。**EarthArXiv 常见问题和审核政策**：发预印本前读。
- **Greene 等 2021、Clancy 等 2014**：前者是英国作者为教学野外实习写的安全清单（未经同行评审的预印本）；后者是一项野外骚扰的网上调查，受访者以人类学者为主。

[^fox2021agudata-e2]: Fox 等 2021，引言。[证据](../../../sources/notes/fox2021agudata.md#e2)
[^fox2021agudata-e3]: Fox 等 2021，§1。[证据](../../../sources/notes/fox2021agudata.md#e3)
[^fox2021agudata-e4]: Fox 等 2021，§1。[证据](../../../sources/notes/fox2021agudata.md#e4)
[^fox2021agudata-e5]: Fox 等 2021，Software Availability Statement。[证据](../../../sources/notes/fox2021agudata.md#e5)
[^fox2021agudata-e6]: Fox 等 2021，§6。[证据](../../../sources/notes/fox2021agudata.md#e6)
[^fox2021agudata-e7]: Fox 等 2021，§2。[证据](../../../sources/notes/fox2021agudata.md#e7)
[^fox2021agudata-e8]: Fox 等 2021，§2。[证据](../../../sources/notes/fox2021agudata.md#e8)
[^fox2021agudata-e9]: Fox 等 2021，§3。[证据](../../../sources/notes/fox2021agudata.md#e9)
[^fox2021agudata-e10]: Fox 等 2021，§1，Large Data。[证据](../../../sources/notes/fox2021agudata.md#e10)
[^fox2021agudata-e11]: Fox 等 2021，§3。[证据](../../../sources/notes/fox2021agudata.md#e11)
[^fox2021agudata-e12]: Fox 等 2021，§1，Data Citation。[证据](../../../sources/notes/fox2021agudata.md#e12)
[^fox2021agudata-e15]: Fox 等 2021，§2。[证据](../../../sources/notes/fox2021agudata.md#e15)
[^eyring2016cmip6-e1]: Eyring 等 2016，摘要。[证据](../../../sources/notes/eyring2016cmip6.md#e1)
[^eyring2016cmip6-e2]: Eyring 等 2016，摘要。[证据](../../../sources/notes/eyring2016cmip6.md#e2)
[^eyring2016cmip6-e3]: Eyring 等 2016，摘要。[证据](../../../sources/notes/eyring2016cmip6.md#e3)
[^eyring2016cmip6-e4]: Eyring 等 2016，§1。[证据](../../../sources/notes/eyring2016cmip6.md#e4)
[^gmd2019editorial-e2]: GMD Executive Editors 2019，§2。[证据](../../../sources/notes/gmd2019editorial.md#e2)
[^gmd2019editorial-e3]: GMD Executive Editors 2019，§2。[证据](../../../sources/notes/gmd2019editorial.md#e3)
[^gmd2019editorial-e4]: GMD Executive Editors 2019，§3.1。[证据](../../../sources/notes/gmd2019editorial.md#e4)
[^gmd2019editorial-e5]: GMD Executive Editors 2019，§3.2。[证据](../../../sources/notes/gmd2019editorial.md#e5)
[^gmd2019editorial-e6]: GMD Executive Editors 2019，§3.3。[证据](../../../sources/notes/gmd2019editorial.md#e6)
[^gmd2019editorial-e7]: GMD Executive Editors 2019，§3.4。[证据](../../../sources/notes/gmd2019editorial.md#e7)
[^gmd2019editorial-e8]: GMD Executive Editors 2019，§4。[证据](../../../sources/notes/gmd2019editorial.md#e8)
[^gmd2019editorial-e9]: GMD Executive Editors 2019，§3.5。[证据](../../../sources/notes/gmd2019editorial.md#e9)
[^gmd2019editorial-e10]: GMD Executive Editors 2019，§3.5。[证据](../../../sources/notes/gmd2019editorial.md#e10)
[^agu2023ethics-e1]: AGU 2023，I. Executive Summary。[证据](../../../sources/notes/agu2023ethics.md#e1)
[^agu2023ethics-e2]: AGU 2023，II. Preamble。[证据](../../../sources/notes/agu2023ethics.md#e2)
[^agu2023ethics-e3]: AGU 2023，III.D。[证据](../../../sources/notes/agu2023ethics.md#e3)
[^agu2023ethics-e4]: AGU 2023，III.B 第 3 条。[证据](../../../sources/notes/agu2023ethics.md#e4)
[^agu2023ethics-e6]: AGU 2023，III.B 第 15 条。[证据](../../../sources/notes/agu2023ethics.md#e6)
[^agu2023ethics-e7]: AGU 2023，VI.C 第 2 条。[证据](../../../sources/notes/agu2023ethics.md#e7)
[^agu2023ethics-e8]: AGU 2023，VI.C 第 4 条。[证据](../../../sources/notes/agu2023ethics.md#e8)
[^agu2023ethics-e9]: AGU 2023，VI.C 第 10 条。[证据](../../../sources/notes/agu2023ethics.md#e9)
[^agu2023ethics-e10]: AGU 2023，VI.E 第 2 条。[证据](../../../sources/notes/agu2023ethics.md#e10)
[^gmdcodepolicy-e1]: GMD 代码与数据政策，Core principles。[证据](../../../sources/notes/gmdcodepolicy.md#e1)
[^gmdcodepolicy-e2]: GMD 代码与数据政策，Core principles。[证据](../../../sources/notes/gmdcodepolicy.md#e2)
[^gmdcodepolicy-e3]: GMD 代码与数据政策，Core principles。[证据](../../../sources/notes/gmdcodepolicy.md#e3)
[^gmdcodepolicy-e4]: GMD 代码与数据政策，Core principles。[证据](../../../sources/notes/gmdcodepolicy.md#e4)
[^gmdcodepolicy-e5]: GMD 代码与数据政策，Scope。[证据](../../../sources/notes/gmdcodepolicy.md#e5)
[^gmdcodepolicy-e6]: GMD 代码与数据政策，Archive standards。[证据](../../../sources/notes/gmdcodepolicy.md#e6)
[^gmdcodepolicy-e7]: GMD 代码与数据政策，Archive standards。[证据](../../../sources/notes/gmdcodepolicy.md#e7)
[^gmdcodepolicy-e8]: GMD 代码与数据政策，Scope。[证据](../../../sources/notes/gmdcodepolicy.md#e8)
[^gmdcodepolicy-e9]: GMD 代码与数据政策，Copernicus 数据政策补充。[证据](../../../sources/notes/gmdcodepolicy.md#e9)
[^gmdcodepolicy-e10]: GMD 代码与数据政策，Copernicus 数据政策补充。[证据](../../../sources/notes/gmdcodepolicy.md#e10)
[^eartharxivabout-e1]: EarthArXiv About。[证据](../../../sources/notes/eartharxivabout.md#e1)
[^eartharxivabout-e2]: EarthArXiv About。[证据](../../../sources/notes/eartharxivabout.md#e2)
[^eartharxivabout-e3]: EarthArXiv About。[证据](../../../sources/notes/eartharxivabout.md#e3)
[^eartharxivfaq-e1]: EarthArXiv FAQ，引用问题。[证据](../../../sources/notes/eartharxivfaq.md#e1)
[^eartharxivfaq-e2]: EarthArXiv FAQ，引用问题。[证据](../../../sources/notes/eartharxivfaq.md#e2)
[^eartharxivfaq-e4]: EarthArXiv FAQ，期刊政策问题。[证据](../../../sources/notes/eartharxivfaq.md#e4)
[^eartharxivfaq-e5]: EarthArXiv FAQ，期刊政策问题。[证据](../../../sources/notes/eartharxivfaq.md#e5)
[^eartharxivfaq-e6]: EarthArXiv FAQ，ESSOAr 问题。[证据](../../../sources/notes/eartharxivfaq.md#e6)
[^eartharxivfaq-e7]: EarthArXiv FAQ，补充材料问题。[证据](../../../sources/notes/eartharxivfaq.md#e7)
[^eartharxivmoderation-e1]: EarthArXiv 审核政策，What does EarthArXiv accept?。[证据](../../../sources/notes/eartharxivmoderation.md#e1)
[^eartharxivmoderation-e2]: EarthArXiv 审核政策，Basic Requirements。[证据](../../../sources/notes/eartharxivmoderation.md#e2)
[^eartharxivmoderation-e3]: EarthArXiv 审核政策，What does EarthArXiv accept?。[证据](../../../sources/notes/eartharxivmoderation.md#e3)
[^igsnabout-e1]: IGSN e.V.，About IGSNs。[证据](../../../sources/notes/igsnabout.md#e1)
[^igsnabout-e2]: IGSN e.V.，About IGSNs。[证据](../../../sources/notes/igsnabout.md#e2)
[^igsnabout-e3]: IGSN e.V.，About IGSNs。[证据](../../../sources/notes/igsnabout.md#e3)
[^igsnabout-e4]: IGSN e.V.，About IGSNs。[证据](../../../sources/notes/igsnabout.md#e4)
[^igsnabout-e5]: IGSN e.V.，About IGSNs。[证据](../../../sources/notes/igsnabout.md#e5)
[^igsnpublications-e1]: IGSN e.V.，Using IGSN in Publications。[证据](../../../sources/notes/igsnpublications.md#e1)
[^igsnpublications-e2]: IGSN e.V.，Using IGSN in Publications。[证据](../../../sources/notes/igsnpublications.md#e2)
[^igsnpublications-e3]: IGSN e.V.，Using IGSN in Publications。[证据](../../../sources/notes/igsnpublications.md#e3)
[^greene2021safety-e1]: Greene 等 2021，§1。[证据](../../../sources/notes/greene2021safety.md#e1)
[^greene2021safety-e2]: Greene 等 2021，§4.2.2。[证据](../../../sources/notes/greene2021safety.md#e2)
[^greene2021safety-e3]: Greene 等 2021，§4.2.2。[证据](../../../sources/notes/greene2021safety.md#e3)
[^greene2021safety-e4]: Greene 等 2021，§4.2.2。[证据](../../../sources/notes/greene2021safety.md#e4)
[^greene2021safety-e5]: Greene 等 2021，§4.2.6。[证据](../../../sources/notes/greene2021safety.md#e5)
[^greene2021safety-e6]: Greene 等 2021，§4.2.6。[证据](../../../sources/notes/greene2021safety.md#e6)
[^greene2021safety-e7]: Greene 等 2021，§4.2.6。[证据](../../../sources/notes/greene2021safety.md#e7)
[^greene2021safety-e8]: Greene 等 2021，摘要。[证据](../../../sources/notes/greene2021safety.md#e8)
[^greene2021safety-e9]: Greene 等 2021，§4.2.5。[证据](../../../sources/notes/greene2021safety.md#e9)
[^greene2021safety-e10]: Greene 等 2021，§4.1.1。[证据](../../../sources/notes/greene2021safety.md#e10)
[^clancy2014survey-e1]: Clancy 等 2014，摘要。[证据](../../../sources/notes/clancy2014survey.md#e1)
[^clancy2014survey-e2]: Clancy 等 2014，Results。[证据](../../../sources/notes/clancy2014survey.md#e2)
[^clancy2014survey-e3]: Clancy 等 2014，Results。[证据](../../../sources/notes/clancy2014survey.md#e3)
[^clancy2014survey-e4]: Clancy 等 2014，Methods。[证据](../../../sources/notes/clancy2014survey.md#e4)
[^clancy2014survey-e5]: Clancy 等 2014，Results。[证据](../../../sources/notes/clancy2014survey.md#e5)
[^clancy2014survey-e6]: Clancy 等 2014，Results。[证据](../../../sources/notes/clancy2014survey.md#e6)
[^clancy2014survey-e7]: Clancy 等 2014，Discussion。[证据](../../../sources/notes/clancy2014survey.md#e7)
[^clancy2014survey-e8]: Clancy 等 2014，Discussion。[证据](../../../sources/notes/clancy2014survey.md#e8)
[^clancy2014survey-e9]: Clancy 等 2014，摘要。[证据](../../../sources/notes/clancy2014survey.md#e9)
[^stagge2019assessing-e1]: Stagge 等 2019，摘要。[证据](../../../sources/notes/stagge2019assessing.md#e1)
[^stagge2019assessing-e8]: Stagge 等 2019，摘要。[证据](../../../sources/notes/stagge2019assessing.md#e8)
[^stagge2019assessing-e9]: Stagge 等 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e9)
[^stagge2019assessing-e10]: Stagge 等 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e10)
[^stagge2019assessing-e4]: Stagge 等 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e4)
[^stagge2019assessing-e11]: Stagge 等 2019，Results。[证据](../../../sources/notes/stagge2019assessing.md#e11)
[^stagge2019assessing-e12]: Stagge 等 2019，Discussion。[证据](../../../sources/notes/stagge2019assessing.md#e12)
[^stagge2019assessing-e13]: Stagge 等 2019，Discussion。[证据](../../../sources/notes/stagge2019assessing.md#e13)
[^stagge2019assessing-e14]: Stagge 等 2019，Discussion。[证据](../../../sources/notes/stagge2019assessing.md#e14)
[^mastrandrea2010ipcc-e1]: Mastrandrea 等 2010，引言。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e1)
[^mastrandrea2010ipcc-e2]: Mastrandrea 等 2010，引言。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e2)
[^mastrandrea2010ipcc-e3]: Mastrandrea 等 2010，引言。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e3)
[^mastrandrea2010ipcc-e4]: Mastrandrea 等 2010，第 9 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e4)
[^mastrandrea2010ipcc-e5]: Mastrandrea 等 2010，第 9 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e5)
[^mastrandrea2010ipcc-e6]: Mastrandrea 等 2010，第 10 段及表 1。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e6)
[^mastrandrea2010ipcc-e7]: Mastrandrea 等 2010，第 10 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e7)
[^mastrandrea2010ipcc-e8]: Mastrandrea 等 2010，第 10 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e8)
[^mastrandrea2010ipcc-e9]: Mastrandrea 等 2010，第 2 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e9)
[^mastrandrea2010ipcc-e10]: Mastrandrea 等 2010，第 3 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e10)
[^mastrandrea2010ipcc-e11]: Mastrandrea 等 2010，第 6 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e11)
[^mastrandrea2010ipcc-e12]: Mastrandrea 等 2010，第 4 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e12)
[^mastrandrea2010ipcc-e13]: Mastrandrea 等 2010，引言。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e13)
[^mastrandrea2010ipcc-e14]: Mastrandrea 等 2010，第 10 段。[证据](../../../sources/notes/mastrandrea2010ipcc.md#e14)
