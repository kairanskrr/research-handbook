# 野外观测研究

本文讲**到现场去观测和采样**的研究：在河流、湖泊、地下水、土壤、岩石露头、大气或海洋里布点、测量、取样，再用这些数据回答问题。生态学的野外调查（样方、样线、物种调查）也可以参考本文 `[本项目分析]`。

不在本文讲的：在野外**主动施加处理**的田间试验，见[农业学科概况](../07_fields/agriculture/README.md#田间试验的设计)；实验室测定的质量控制细节，见[环境工程学科概况](../07_fields/environmental-engineering/README.md#质量控制样品空白平行样加标)；只分析别人已经采好的数据，见研究方法里的[数据科学研究](data_science.md)；野外的安全、许可、伦理和骚扰问题，见[地球与环境科学学科概况](../07_fields/earth-environmental-sciences/README.md#野外工作先把安全和许可办好)。

**先说清本文资料的来历。** 操作细节大多来自两家美国政府机构：美国地质调查局（United States Geological Survey，USGS）的《水质数据采集国家野外手册》，是 USGS 给**本局**水质野外人员定的规程[^usgs2018nfmprep-e2]；美国环境保护署（Environmental Protection Agency，EPA）的计划指南，是 EPA 为**它资助的项目**写的，适用范围见[环境工程学科概况](../07_fields/environmental-engineering/README.md#把计划写下来epa-的质量保证项目计划)。`[本项目分析]` 它们不是全学科的统一规定，对你没有约束力，但写得具体，适合当清单参考。你要遵守的，是你所在国家、单位、资助方和目标期刊的规定。

**适用范围** `[本项目分析]`：本篇原为地球与环境科学学科篇写，例子以水、土壤、岩石等环境介质的观测和采样为主；资料主要来自美国政府机构的手册和指南（USGS、EPA）、美国地球物理联合会（AGU）等学会的文件，以及生态、环境统计的方法学文章。除[地球与环境科学](../07_fields/earth-environmental-sciences/README.md)外，[农业](../07_fields/agriculture/README.md)、[环境工程](../07_fields/environmental-engineering/README.md)、[地理学](../07_fields/geography/README.md)的学科概况也链接到本篇。其他学科到现场观测时，采样和质量控制的要求可能不同；用之前先看本学科的规范。

**常服务的套路**：[观察描述](../05_research-strategies/observe_describe.md#3-常用的研究方法)。

**读完本文，你应该能：**

- 把研究问题落实到"在哪采、什么时候采、采多少"；
- 出发前做好安全和仪器准备，在现场记好别人也看得懂的记录；
- 安排质量控制样品，管好样品编号和数据；
- 分析野外数据时，认出伪重复、混杂和自相关这三个常见陷阱。

---

## 1. 这是什么研究，什么时候用

| | 野外观测研究 | 野外操纵试验 | 分析已有观测数据 |
|---|---|---|---|
| 你做什么 | 到现场测量、采样，不改变研究对象 | 在现场施加处理（施肥、烧荒、围栏），比较效果 | 用站网、卫星、数据库里现成的数据 |
| 数据从哪来 | 自己采 | 自己采 | 别人采 |
| 最大的难点 | 采样设计、现场质量、错过了补不回来 | 真正的重复和随机化 | 弄清数据怎么来的、质量如何 |
| 对应篇目 | 本文 | [农业学科概况](../07_fields/agriculture/README.md#田间试验的设计) | [数据科学研究](data_science.md) |

`[本项目分析]` 怎么选：想知道"某地某物现在是什么状态、怎样随时间和空间变化"，做野外观测；想知道"某个处理会不会造成某个变化"，而且你能控制处理，做操纵试验。只有观测数据时，能下的因果结论更弱，见下文第十一步。很多项目是混合的：先用野外观测摸清现状，再设计试验或模拟。

## 2. 怎么做

### 第一步：把问题变成在野外能回答的问题

**怎么做**：先写清四件事：数据拿来做什么（估计平均值？比较两片区域？看趋势？）；目标总体是什么，也就是你想下结论的范围；采样单元是什么；误差能容忍多大。研究对象是空气、水、土壤这类连续介质时，EPA 指南要求把采样单元定义成一定的面积、体积或质量[^epa2006dqo-e6]。EPA 用七步的"数据质量目标流程"做这件事，各步内容见[环境工程学科概况](../07_fields/environmental-engineering/README.md#采样前先做计划epa-的数据质量目标流程)。

**为什么**：EPA 的指南说，采样前不做计划，收来的数据满足不了需要的可能性高得不可接受[^epa2006dqo-e1]。野外数据错过了时机就补不回来 `[本项目分析]`。

**容易错在哪里**：只写"调查某湖的水质"，没说是要估计全湖平均，还是比较入湖口和出湖口。两种目的的布点完全不同 `[本项目分析]`。研究问题怎么写具体，见第二部分的[从研究问题到证据清单](../02_do-the-project/01_question-to-evidence.md)。

### 第二步：设计采样：在哪、什么时候、采多少

**先决定用概率抽样还是判断抽样。** 概率抽样里，每个采样单元被抽中的概率是已知的；判断抽样由负责人凭经验挑点[^epa2006dqo-e12]。按 EPA 指南，常见的概率抽样有简单随机、分层、系统和网格抽样，它们能让你对目标总体下定量结论，并说清结论有多不确定[^epa2006dqo-e13]。判断抽样做不到这一点：在它上面做统计分析，不能对总体作出站得住的概率性陈述[^epa2006dqo-e14]。

| 方式 | 做法 | 什么时候用 |
|---|---|---|
| 简单随机 | 在研究区里随机定点 | 研究区比较均一，没有先验信息 `[本项目分析]` |
| 分层 | 先按已知差异分区（如土地过去的用途），再在各区内抽样 | 各部分性质不同，要保证每部分都有代表[^epa2006dqo-e15] |
| 系统或网格 | 按固定间距布点 | 要画空间分布图、要均匀覆盖 `[本项目分析]` |
| 判断 | 凭经验挑点 | 结论只能靠专业判断，不能做概率推断[^epa2006dqo-e14] |

**空间上要多点。** USGS 手册指出：在大多数流动或静止的水体里，一个采样点不足以代表整段水体的物理、化学或生物状况[^usgs2018nfmprep-e3]。选点要同时考虑点的数量和位置、数据质量目标、能否到达、安全和预算[^usgs2018nfmprep-e5]。先在断面上测一轮现场指标，可以粗看混合是否均匀；但这不保证你关心的物质也均匀，要在采样初期检验[^usgs2018nfmprep-e6]。

**时间上也要重复。** EPA 指南说，一般来说采样误差远大于测量误差[^epa2006dqo-e7]；预计空间或时间上的变化很大时，可以用便宜、精度稍低的分析方法，把钱花在更多地点和时间上[^epa2006dqo-e9]。Casler（一篇写给农学研究者的试验设计综述）也建议优先增加地点数和年份数，而不是每个地点内的重复数[^casler2015fundamentals-e27]。

**采多少。** Casler 建议每次设计前都做统计功效分析（估算要多少样本，才有足够把握发现你关心的差异），参数只能靠猜也要做[^casler2015fundamentals-e21]。具体做法见[农业学科概况](../07_fields/agriculture/README.md#地点年份和功效分析)。

**容易错在哪里：伪重复。** 伪重复指处理没有真正重复、或重复之间不独立，却仍用统计检验来检验处理效应[^davies2015pseudoreplication-e1]。Casler 的例子：只用两块地，一块烧荒、一块不烧，统计算得没错，但设计没法明确解释结果[^casler2015fundamentals-e5]。他强调重复要和施加处理的空间、时间尺度一致[^casler2015fundamentals-e4]。观测研究里同理：比较"上游一个点"和"下游一个点"，每个点采 30 瓶水，每边仍只有一个点 `[本项目分析]`。更多例子见[农业学科概况](../07_fields/agriculture/README.md#伪重复处理和地块混在一起)。

### 第三步：办齐许可

**怎么做**：进入许可、采样许可，需要时还有样品进出口许可，逐项办；还要查地点是否受保护。这些清单和伦理问题见[地球与环境科学学科概况](../07_fields/earth-environmental-sciences/README.md#野外工作先把安全和许可办好)，这里不重复。两点补充：

- USGS 规定其人员进入公有或私有土地选点、采样前必须取得许可，最好书面，口头许可要记录下来[^usgs2018nfmprep-e2]。没有书面许可时，至少记下谁、何时、同意了什么 `[本项目分析]`。
- 涉及动物（例如采鱼）时，美国渔业学会等三家学会的指南要求研究者取得全部所需许可[^afs2014fishes-e4]；在美国以外做研究，要遵守所在国的野生动物法规[^afs2014fishes-e5]。

**容易错在哪里**：以为导师或合作方已经办好了。你所在国家具体要办哪些许可，本文资料未涉及。出发前列一张清单逐项问清 `[本项目分析]`：土地或保护区归谁管，采样、采集动植物要不要许可，样品跨地区或出境运输有没有限制；拿不准的问导师和单位的科研管理部门，批文和许可记录要保存好。

### 第四步：安全和后勤

**怎么做**（以下来自 USGS 手册，是给本局人员的规定，可当清单参考）：

- 用"作业危害分析"把每项具体工作过一遍，在危险发生前找出它们[^usgs2018nfmprep-e14]。
- 小组里任何时候至少有一名有经验、受过训练的人[^usgs2018nfmprep-e13]；每晚向单位报平安，约好没接到电话就有人启动救援[^usgs2018nfmprep-e15]。
- 选点时确认在一般和极端的水流、天气下都能到达[^usgs2018nfmprep-e4]。任何河流，包括季节性小河，都可能迅速变得太深太急，无法安全涉水[^usgs2018nfmprep-e7]。

**容易错在哪里**：把安全准备当成走形式。风险评估要经人审核、告诉所有同行者，急救和举报渠道等，见[地球与环境科学学科概况](../07_fields/earth-environmental-sciences/README.md#野外工作先把安全和许可办好)。

### 第五步：仪器和现场校准

**怎么做**（USGS 对本局人员的规定）：每次出野外前校准仪器，多数仪器在现场还要检查[^usgs2023nfmfield-e6]；在现场定期检查精密度和准确度[^usgs2023nfmfield-e8]。每台仪器或可换的传感器单独建日志，记维修、保养和校准历史，日志跟着仪器走[^usgs2023nfmfield-e4]。第一次用某种仪器，先跟有经验的人练习[^usgs2023nfmfield-e7]。

**为什么**：USGS 所说的"现场测量"，是必须在现场、在时间和地点上尽量贴近采样时测的性质[^usgs2023nfmfield-e1]，例如水温、溶解氧 `[本项目分析]`。这类数据事后没法重测，仪器出了问题，这一趟的数据就可能作废 `[本项目分析]`。

**容易错在哪里**：带着上次没修好的仪器出发；只在出发前校准一次，现场从不检查漂移 `[本项目分析]`。

### 第六步：现场记录

**怎么做**（USGS 对本局人员的规定）：

- 每个有唯一编号的采样点都要有记录，永久记下现场活动、读数、仪器校准等信息[^usgs2023nfmfield-e2]。大部分记录在现场完成，并由同伴或数据管理员独立核对[^usgs2023nfmfield-e3]。
- 纸质记录不能用铅笔；写错了划一道线、签上姓名缩写，不要涂掉[^usgs2023nfmfield-e5]。凭经验在几个读数里挑一个时，在记录里写明怎样决定的[^usgs2023nfmfield-e9]。
- 画现场草图，详细到从没去过的人也能凭它找到这个点[^usgs2018nfmprep-e16]。
- 原始记录（野外最初记下的数据、元数据等）不论纸质还是电子，都要存档[^usgs2018nfmprep-e9]。

**为什么**：美国地球物理学会（American Geophysical Union，AGU）的伦理政策要求认真记录方法、假设和不确定性[^agu2023ethics-e8]，论文要写到同行能重复的程度[^agu2023ethics-e7]。野外的天气、水位、异常情况，只有当时记下才有 `[本项目分析]`。具体要记哪些元数据字段，本文资料未涉及，以目标数据库或期刊的要求为准。

### 第七步：样品编号

**怎么做**：给每个样品唯一编号，全程追踪，避免弄混[^epa2002qapp-e6]；出发前就准备好瓶签，写上站点、样品类型等（USGS 的清单条目）[^usgs2018nfmprep-e18]。能注册国际通用样品编号（IGSN，实物样品的全球唯一永久编号）就注册，做法见[地球与环境科学学科概况](../07_fields/earth-environmental-sciences/README.md#样品给每个样品一个永久编号)；贴二维码时，标签上还要印出人能读的编号[^igsnpublications-e3]。监管链（记录样品每一步由谁经手）见[环境工程学科概况](../07_fields/environmental-engineering/README.md#样品编号和监管链)。

**为什么**：USGS 手册说，分析结果的好坏不可能超过被分析的那个样品本身[^usgs2018nfmprep-e1]。

### 第八步：安排质量控制样品

**怎么做**：在采样计划里写明做哪些质量控制样品、多久做一次（EPA 质量保证项目计划指南的要求）[^epa2002qapp-e13]。在野外采的有两种：

- **现场空白**：不含目标物的干净样品，带到现场、暴露于采样条件，再按普通样品送检[^epa2002qapp-e14]。USGS 要求在正式采样前就采空白，之后定期采[^usgs2018nfmprep-e10]。
- **现场平行样**：同一时间、同一地点采两份以上，并标明身份[^epa2002qapp-e16]。按 USGS 手册，它用来估计水体的自然变化，以及采样、处理和分析带来的变化[^usgs2018nfmprep-e11]。

**为什么**：EPA 指南说，质量控制不是为了消除误差，而是测出误差有多大[^epa2002qapp-e9]。加标样、检出限和"测不到"的数据，见[环境工程学科概况](../07_fields/environmental-engineering/README.md#质量控制样品空白平行样加标)。

**容易错在哪里**：现场平行样是质量控制，不是重复。同一点的两瓶水不能当成两个独立的采样点 `[本项目分析]`。

### 第九步：数据管理和存档

**怎么做**：USGS 手册要求数据管理在采样之前就开始计划[^usgs2018nfmprep-e8]。USGS 的项目工作计划包括：范围、时间表和预算，标准操作程序，质量保证计划，数据管理计划，分析和发表计划[^usgs2018nfmprep-e17]。投 AGU 期刊时，野外观测数据也在必须公开之列[^fox2021agudata-e16]；投稿时就要能拿到、"可向作者索取"不合格等要求，以及存储库怎么选，见[地球与环境科学学科概况](../07_fields/earth-environmental-sciences/README.md#数据投稿时就要能拿到)。

### 第十步：对付不可重复的事件

洪水、风暴、野火、火山喷发只发生一次。Davies 和 Gray 2015 年的一篇观点文章说，研究这类事件时，伪重复问题非常常见[^davies2015pseudoreplication-e7]。他们也承认：严格说，只有一次干扰、样地分布在边界两侧时，无法在统计上把空间差异和事件影响分开[^davies2015pseudoreplication-e8]。

但他们认为，不能一见单次事件就扣上伪重复的帽子：混杂（见第十一步）要和伪重复分开看[^davies2015pseudoreplication-e9]；指责伪重复之前，要先说明这个指责在统计上成立、在生态学上有意义[^davies2015pseudoreplication-e4]。他们给出的做法：

- **把对照做得尽量像**：他们让对比的样地离得近，处在同一土壤、同一海拔、同一坡向[^davies2015pseudoreplication-e11]。
- **分清能推断什么、能解释什么**：统计上只说"两侧有差异"，因果解释作为生态学判断单独写[^davies2015pseudoreplication-e10]。
- **在论文里主动交代**：他们认为审稿人可以要求作者承认问题、写明缓解措施、谨慎解释、把结论写成新假设[^davies2015pseudoreplication-e12]。作者自己先做到这几点即可 `[本项目分析]`。

`[本项目分析]` 事件发生后尽快到现场，记录比平时更详细，样品留够、注册编号。IGSN 组织也说，有些样品再也采不到了[^igsnabout-e4]。

### 第十一步：分析野外观测数据

先读研究方法里的[数据科学研究](data_science.md#第八步解释结果相关不等于因果)：观测数据里相关不等于因果。野外数据还有三个特别的问题。

**1. 混杂。** 两片区域的差异，可能部分来自土壤、湿度、坡向、海拔等没控制的变量[^davies2015pseudoreplication-e9]。设计时让对比的点在这些方面尽量一致[^davies2015pseudoreplication-e11]，并把它们测下来 `[本项目分析]`。

**2. 观测不独立（自相关）。** Zuur 等 2010 年给生态学者写的数据探索步骤指出，大多数统计方法都假设观测之间相互独立[^zuur2010protocol-e2]。野外数据常常不是这样：

- **空间自相关**：相邻地点的值彼此不独立[^dormann2007spatial-e1]，比如相近地点的鸟比远处的更相像[^zuur2010protocol-e3]。
- **时间上的序列相关**：Helsel 等的 USGS 水资源统计教材举例，每天采一次、20 年约 7300 个数据，如果按 n = 7300 算置信区间，会严重高估结果的确定程度[^helsel2020statistical-e9]；采样太密、相关很强时，100 个观测估计均值的准确度可能只相当于 10 个独立观测[^helsel2020statistical-e7]。

后果：Dormann 等 2007 年的方法综述指出，参数估计可能有偏，"假阳性"（本来没有效应，却判断为有）会变多[^dormann2007spatial-e3]。

**怎么查、怎么办**（以下是这几位作者的方法建议）：分析前看原始数据、分析后看残差，把它们对时间或空间坐标作图[^zuur2010protocol-e6]；空间上，可以画数据点之间的相似度或方差随距离变化的图（相关图、半变异函数图）[^dormann2007spatial-e4]。看起来像序列相关的，常常其实是季节等时间成分或趋势造成的[^helsel2020statistical-e10]。发现不独立，模型就要把它考虑进去[^zuur2010protocol-e4]，例如用嵌套或随机效应[^davies2015pseudoreplication-e3]。具体方法超出本文范围，找懂统计的合作者。

**3. 漏测变量补不回来。** 残差相关常常源于漏测了一个重要变量，这时事后可能无法补救[^zuur2010protocol-e5][^dormann2007spatial-e2]。所以第一步就要想清楚该测什么 `[本项目分析]`。

### 第十二步：报告

`[本项目分析]` 方法部分至少写清：采样设计和选点理由、采样时间和当时的条件、仪器和校准、质量控制样品及其结果、样品编号和存放地点、数据的存档位置。依据：AGU 要求论文写到同行能重复[^agu2023ethics-e7]，AGU 期刊要求原始数据和处理后的数据都写进参考文献[^fox2021agudata-e12]。设计有局限（例如只有一个事件点）时，按第十步主动交代。

## 3. 检查清单

**必须做到**

- [ ] 采样前做计划[^epa2006dqo-e1]，写清数据用途、目标总体和采样单元[^epa2006dqo-e6]
- [ ] 想做统计推断的，用概率抽样[^epa2006dqo-e14]
- [ ] 重复和要比较的东西在同一空间、时间尺度上[^casler2015fundamentals-e4]
- [ ] 进入、采样、进出口许可逐项办齐[^greene2021safety-e3]
- [ ] 风险评估经第三方审核，所有同行者知情[^greene2021safety-e5]
- [ ] 仪器出发前校准，现场检查[^usgs2023nfmfield-e6]
- [ ] 每个样品唯一编号[^epa2002qapp-e6]，原始记录存档[^usgs2018nfmprep-e9]
- [ ] 写明质量控制样品的种类和频率[^epa2002qapp-e13]
- [ ] 分析前后检查空间、时间上的相关[^zuur2010protocol-e6]

**做到更好**

- [ ] 设计前做功效分析[^casler2015fundamentals-e21]
- [ ] 正式采样前先采空白，提早发现问题[^usgs2018nfmprep-e10]
- [ ] 能注册 IGSN 就注册[^igsnabout-e2]
- [ ] 记录由同伴独立核对[^usgs2023nfmfield-e3]

**这些情况可以不做，不算缺陷**

- 只做预调查或找"最坏情况"时，可以用判断抽样 `[本项目分析]`；但结论只能靠专业判断，不做概率推断[^epa2006dqo-e14]。

**审稿时常见、但可能不成立的批评**

- "只有一个事件点，就是伪重复，不能发表。"Davies 和 Gray 认为，伪重复概念被用得太教条，常导致审稿时被拒[^davies2015pseudoreplication-e2]；他们主张，指责之前要先说明它在统计上成立、在生态学上有意义[^davies2015pseudoreplication-e4]；审稿人可以要求作者交代问题、谨慎解释、把结论写成新假设[^davies2015pseudoreplication-e12]。这是这两位作者的观点，不是学界共识 `[本项目分析]`。

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 一个点采很多瓶，当成很多个样本 | 美国渔业学会等的指南把这算作伪重复[^afs2014fishes-e1]；现场平行样只用来估计变化[^usgs2018nfmprep-e11] |
| 凭方便挑点，却做统计检验 | 判断抽样不能做概率推断[^epa2006dqo-e14] |
| 把钱都花在精密分析上，点位很少 | EPA 指南认为采样误差一般远大于测量误差[^epa2006dqo-e7] |
| 用铅笔记录、写错就涂掉 | USGS 规程不允许[^usgs2023nfmfield-e5] |
| 每天采样 20 年，按 n = 7300 算置信区间 | 序列相关让真实信息量少得多[^helsel2020statistical-e9] |
| 把两侧差异直接说成事件造成的 | 空间差异和事件影响分不开[^davies2015pseudoreplication-e8]，还可能有混杂[^davies2015pseudoreplication-e9] |

## 5. 延伸阅读

- **USGS《水质数据采集国家野外手册》A1 章（准备采样）和 A6.0 章（现场测量）**：免费。这是 USGS 给本局人员的规程，只能当清单参考；出发前的准备、安全、记录、校准写得具体。做水以外的介质，也可以借鉴记录和准备的做法 `[本项目分析]`。
- **EPA QA/G-4（数据质量目标）和 QA/G-5（质量保证项目计划）**：EPA 为它资助的项目写的指南。讲怎样把问题变成采样设计、怎样写质量控制计划。
- **Davies & Gray 2015**：观点文章，开放获取。讲单次事件研究怎么做、怎么写、怎么回应伪重复的批评。
- **Zuur 等 2010**：分析生态数据前的数据探索步骤，独立性那一步最相关。**Dormann 等 2007**：空间自相关的检查和处理方法综述。
- **Helsel 等 2020**：USGS 的水资源统计教材，免费。

[^epa2006dqo-e1]: EPA 2006，Introduction，PDF 第 11 页。[证据](../../sources/notes/epa2006dqo.md#e1)
[^epa2006dqo-e7]: EPA 2006，Chapter 6，PDF 第 57 页。[证据](../../sources/notes/epa2006dqo.md#e7)
[^epa2006dqo-e12]: EPA 2006，Chapter 7，PDF 第 83 页。[证据](../../sources/notes/epa2006dqo.md#e12)
[^epa2006dqo-e13]: EPA 2006，Chapter 7，PDF 第 83 页。[证据](../../sources/notes/epa2006dqo.md#e13)
[^epa2006dqo-e14]: EPA 2006，Chapter 7，PDF 第 83 页。[证据](../../sources/notes/epa2006dqo.md#e14)
[^epa2006dqo-e15]: EPA 2006，Chapter 7，PDF 第 84 页。[证据](../../sources/notes/epa2006dqo.md#e15)
[^epa2006dqo-e9]: EPA 2006，Chapter 7，PDF 第 83 页。[证据](../../sources/notes/epa2006dqo.md#e9)
[^epa2006dqo-e6]: EPA 2006，Chapter 4，PDF 第 41 页。[证据](../../sources/notes/epa2006dqo.md#e6)
[^epa2002qapp-e9]: EPA 2002，Element B5，PDF 第 39 页。[证据](../../sources/notes/epa2002qapp.md#e9)
[^epa2002qapp-e14]: EPA 2002，Appendix B，PDF 第 71 页。[证据](../../sources/notes/epa2002qapp.md#e14)
[^epa2002qapp-e16]: EPA 2002，Appendix B，PDF 第 69 页。[证据](../../sources/notes/epa2002qapp.md#e16)
[^epa2002qapp-e6]: EPA 2002，Element B3，PDF 第 36 页。[证据](../../sources/notes/epa2002qapp.md#e6)
[^epa2002qapp-e13]: EPA 2002，Element B5，PDF 第 39 页。[证据](../../sources/notes/epa2002qapp.md#e13)
[^usgs2018nfmprep-e1]: USGS 2018，§1.1，PDF 第 11 页。[证据](../../sources/notes/usgs2018nfmprep.md#e1)
[^usgs2018nfmprep-e3]: USGS 2018，§2.2，PDF 第 14 页。[证据](../../sources/notes/usgs2018nfmprep.md#e3)
[^usgs2018nfmprep-e2]: USGS 2018，§2.1，PDF 第 14 页。[证据](../../sources/notes/usgs2018nfmprep.md#e2)
[^usgs2018nfmprep-e4]: USGS 2018，§2.2，PDF 第 14 页。[证据](../../sources/notes/usgs2018nfmprep.md#e4)
[^usgs2018nfmprep-e5]: USGS 2018，§2.0，PDF 第 13 页。[证据](../../sources/notes/usgs2018nfmprep.md#e5)
[^usgs2018nfmprep-e6]: USGS 2018，§2.2.1，PDF 第 15 页。[证据](../../sources/notes/usgs2018nfmprep.md#e6)
[^usgs2018nfmprep-e7]: USGS 2018，§2.2.1，PDF 第 15 页。[证据](../../sources/notes/usgs2018nfmprep.md#e7)
[^usgs2018nfmprep-e8]: USGS 2018，§3.0，PDF 第 18 页。[证据](../../sources/notes/usgs2018nfmprep.md#e8)
[^usgs2018nfmprep-e9]: USGS 2018，§3.0，PDF 第 18 页。[证据](../../sources/notes/usgs2018nfmprep.md#e9)
[^usgs2018nfmprep-e10]: USGS 2018，§4.2，PDF 第 25 页。[证据](../../sources/notes/usgs2018nfmprep.md#e10)
[^usgs2018nfmprep-e11]: USGS 2018，§4.2，PDF 第 25 页。[证据](../../sources/notes/usgs2018nfmprep.md#e11)
[^usgs2018nfmprep-e13]: USGS 2018，表 1-4，PDF 第 26 页。[证据](../../sources/notes/usgs2018nfmprep.md#e13)
[^usgs2018nfmprep-e14]: USGS 2018，§5.1.1，PDF 第 28 页。[证据](../../sources/notes/usgs2018nfmprep.md#e14)
[^usgs2018nfmprep-e15]: USGS 2018，表 1-5，PDF 第 28 页。[证据](../../sources/notes/usgs2018nfmprep.md#e15)
[^usgs2018nfmprep-e16]: USGS 2018，§5.2，PDF 第 31 页。[证据](../../sources/notes/usgs2018nfmprep.md#e16)
[^usgs2018nfmprep-e17]: USGS 2018，§4.0，PDF 第 24 页。[证据](../../sources/notes/usgs2018nfmprep.md#e17)
[^usgs2018nfmprep-e18]: USGS 2018，表 1-4，PDF 第 27 页。[证据](../../sources/notes/usgs2018nfmprep.md#e18)
[^usgs2023nfmfield-e1]: USGS 2023，§1.0，PDF 第 9 页。[证据](../../sources/notes/usgs2023nfmfield.md#e1)
[^usgs2023nfmfield-e2]: USGS 2023，§2.1，PDF 第 10 页。[证据](../../sources/notes/usgs2023nfmfield.md#e2)
[^usgs2023nfmfield-e3]: USGS 2023，§2.1，PDF 第 10 页。[证据](../../sources/notes/usgs2023nfmfield.md#e3)
[^usgs2023nfmfield-e4]: USGS 2023，§2.1，PDF 第 10 页。[证据](../../sources/notes/usgs2023nfmfield.md#e4)
[^usgs2023nfmfield-e5]: USGS 2023，§2.1，PDF 第 10 页。[证据](../../sources/notes/usgs2023nfmfield.md#e5)
[^usgs2023nfmfield-e6]: USGS 2023，PDF 第 12 页。[证据](../../sources/notes/usgs2023nfmfield.md#e6)
[^usgs2023nfmfield-e7]: USGS 2023，PDF 第 12 页。[证据](../../sources/notes/usgs2023nfmfield.md#e7)
[^usgs2023nfmfield-e8]: USGS 2023，Performance，PDF 第 12 页。[证据](../../sources/notes/usgs2023nfmfield.md#e8)
[^usgs2023nfmfield-e9]: USGS 2023，Performance，PDF 第 12 页。[证据](../../sources/notes/usgs2023nfmfield.md#e9)
[^casler2015fundamentals-e4]: Casler 2015，Replication。[证据](../../sources/notes/casler2015fundamentals.md#e4)
[^casler2015fundamentals-e5]: Casler 2015，Replication。[证据](../../sources/notes/casler2015fundamentals.md#e5)
[^casler2015fundamentals-e27]: Casler 2015，Number of replicates。[证据](../../sources/notes/casler2015fundamentals.md#e27)
[^casler2015fundamentals-e21]: Casler 2015，结论部分。[证据](../../sources/notes/casler2015fundamentals.md#e21)
[^davies2015pseudoreplication-e1]: Davies & Gray 2015，Abstract。[证据](../../sources/notes/davies2015pseudoreplication.md#e1)
[^davies2015pseudoreplication-e7]: Davies & Gray 2015，Discussion。[证据](../../sources/notes/davies2015pseudoreplication.md#e7)
[^davies2015pseudoreplication-e8]: Davies & Gray 2015，Discussion。[证据](../../sources/notes/davies2015pseudoreplication.md#e8)
[^davies2015pseudoreplication-e9]: Davies & Gray 2015，Discussion。[证据](../../sources/notes/davies2015pseudoreplication.md#e9)
[^davies2015pseudoreplication-e10]: Davies & Gray 2015，Discussion。[证据](../../sources/notes/davies2015pseudoreplication.md#e10)
[^davies2015pseudoreplication-e11]: Davies & Gray 2015，Discussion。[证据](../../sources/notes/davies2015pseudoreplication.md#e11)
[^davies2015pseudoreplication-e12]: Davies & Gray 2015，Discussion。[证据](../../sources/notes/davies2015pseudoreplication.md#e12)
[^davies2015pseudoreplication-e3]: Davies & Gray 2015，Abstract。[证据](../../sources/notes/davies2015pseudoreplication.md#e3)
[^davies2015pseudoreplication-e4]: Davies & Gray 2015，Conclusion。[证据](../../sources/notes/davies2015pseudoreplication.md#e4)
[^davies2015pseudoreplication-e2]: Davies & Gray 2015，Abstract。[证据](../../sources/notes/davies2015pseudoreplication.md#e2)
[^afs2014fishes-e1]: 美国渔业学会等 2014，2.3。[证据](../../sources/notes/afs2014fishes.md#e1)
[^afs2014fishes-e4]: 美国渔业学会等 2014，3。[证据](../../sources/notes/afs2014fishes.md#e4)
[^afs2014fishes-e5]: 美国渔业学会等 2014，3.1。[证据](../../sources/notes/afs2014fishes.md#e5)
[^greene2021safety-e3]: Greene 等 2021，§4.2.2。[证据](../../sources/notes/greene2021safety.md#e3)
[^greene2021safety-e5]: Greene 等 2021，§4.2.6。[证据](../../sources/notes/greene2021safety.md#e5)
[^igsnabout-e2]: IGSN e.V.，About IGSNs。[证据](../../sources/notes/igsnabout.md#e2)
[^igsnabout-e4]: IGSN e.V.，About IGSNs。[证据](../../sources/notes/igsnabout.md#e4)
[^igsnpublications-e3]: IGSN e.V.，Using IGSN in Publications。[证据](../../sources/notes/igsnpublications.md#e3)
[^agu2023ethics-e7]: AGU 2023，VI.C 第 2 条。[证据](../../sources/notes/agu2023ethics.md#e7)
[^agu2023ethics-e8]: AGU 2023，VI.C 第 4 条。[证据](../../sources/notes/agu2023ethics.md#e8)
[^fox2021agudata-e16]: Fox 等 2021，引言。[证据](../../sources/notes/fox2021agudata.md#e16)
[^fox2021agudata-e12]: Fox 等 2021，§1，Data Citation。[证据](../../sources/notes/fox2021agudata.md#e12)
[^zuur2010protocol-e2]: Zuur 等 2010，Step 8。[证据](../../sources/notes/zuur2010protocol.md#e2)
[^zuur2010protocol-e3]: Zuur 等 2010，Step 8。[证据](../../sources/notes/zuur2010protocol.md#e3)
[^zuur2010protocol-e4]: Zuur 等 2010，Step 8。[证据](../../sources/notes/zuur2010protocol.md#e4)
[^zuur2010protocol-e5]: Zuur 等 2010，Step 8。[证据](../../sources/notes/zuur2010protocol.md#e5)
[^zuur2010protocol-e6]: Zuur 等 2010，Step 8。[证据](../../sources/notes/zuur2010protocol.md#e6)
[^dormann2007spatial-e1]: Dormann 等 2007，引言。[证据](../../sources/notes/dormann2007spatial.md#e1)
[^dormann2007spatial-e2]: Dormann 等 2007，引言。[证据](../../sources/notes/dormann2007spatial.md#e2)
[^dormann2007spatial-e3]: Dormann 等 2007，摘要。[证据](../../sources/notes/dormann2007spatial.md#e3)
[^dormann2007spatial-e4]: Dormann 等 2007，方法部分。[证据](../../sources/notes/dormann2007spatial.md#e4)
[^helsel2020statistical-e7]: Helsel 等 2020，§1.1。[证据](../../sources/notes/helsel2020statistical.md#e7)
[^helsel2020statistical-e9]: Helsel 等 2020，§9.4.2.4。[证据](../../sources/notes/helsel2020statistical.md#e9)
[^helsel2020statistical-e10]: Helsel 等 2020，§9.4.2.4。[证据](../../sources/notes/helsel2020statistical.md#e10)
