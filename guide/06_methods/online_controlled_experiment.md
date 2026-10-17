# 在线对照实验（A/B 测试）：在真实产品里随机分组，比较指标

本文讲**在线对照实验**（online controlled experiment），业界常叫 **A/B 测试**：把一个正在运行的网站、应用或服务的真实用户随机分成两组，一组用现有版本（对照组），一组用新版本（处理组），再比较两组的指标[^kohavi2009controlled-e1]。

它和几个相邻页面的关系 `[本项目分析]`：

- [对照实验](controlled_experiment.md)讲的是研究者招募参与者、在受控条件下比较人的表现。在线对照实验的逻辑相同，但参与者是产品的真实用户，通常不知道自己在实验里，测的是他们在日常使用中留下的行为数据。
- [田野实验](field_experiment.md)讲的是和政府、企业或社区合作，在真实世界里随机分配干预。在线对照实验可以看成在软件产品里做的田野实验，只是由产品方自己实施，样本动辄几十万人，一次实验只跑几周。田野实验页里关于随机化单位、溢出和伦理的讨论，这里也用得上。
- 被比较的如果是系统或模型本身，不需要真实用户，看[基准评测](../07_fields/computer-science/practices/benchmarking.md)。统计检验的一般讲法见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md)，本文不重复。

**适用范围** `[本项目分析]`：本文的资料几乎都来自软件行业的实验团队（微软的必应和 MSN、Booking.com，以及商业 A/B 测试平台 Optimizely），发表在数据挖掘会议 KDD 和期刊《数据挖掘与知识发现》上；伦理部分用的是 Facebook 情绪传染实验引起的争议。所以这里讲的是"有一个大流量产品"时的做法。学术研究者在人机交互、信息系统、计算社会科学里做这类实验，通常要和平台合作，或在自己运营的网站、课程平台上做，流量小得多，伦理审查也按本单位的规定。市场营销、经济学里在网上做的随机实验，先看本学科的规范和[田野实验](field_experiment.md)。

**常服务的套路**：[比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md)。

**读完本文，你应该能：**

- 判断自己的问题适不适合、有没有条件用在线对照实验回答；
- 事先定好总体评价指标、护栏指标和随机化单位，算出要跑多久；
- 用 A/A 测试和样本比例检查，确认实验本身可信；
- 避开中途偷看、新奇效应、组间干扰等常见陷阱，处理好知情同意。

---

## 1. 这是什么研究，什么时候用

核心是"随机"：用户不能随便分，任何因素都不能影响谁进哪一组。设计和执行都正确时，两组之间唯一系统性的不同就是这次改动，指标的差异因此可以归因于它[^kohavi2009controlled-e2]。这一点让它和事后分析、中断时间序列这类准实验不同：它检验的是因果关系[^kohavi2009controlled-e25]。

**为什么要做实验，而不是凭判断。** 想法的成功率比人们以为的低得多：在微软做过实验的想法里，只有三分之一改善了它本来想改善的指标[^kohavi2012trustworthy-e2]。

**它擅长回答的问题** `[本项目分析]`：

- "把功能 X 上线给真实用户，某个行为指标变了多少？"例如改一个按钮、换一种推荐排序。不只界面改动，后台算法的改动（如搜索算法）也可以这样评估，这一点常被忽视[^kohavi2009controlled-e26]。
- "离线评测里更好的模型，到了真实使用中还更好吗？"这正是离线评测和真实效果之间的那道缝。

**它不擅长回答的问题：**

- **为什么**。它能告诉你哪个版本更好、好多少，但说不出原因；可用性实验室里的用户研究能收集用户的评论，可以补上这一块[^kohavi2009controlled-e12]。这类研究见[对照实验](controlled_experiment.md)和[访谈研究](interview_study.md)。
- **长期效果**。它测的是实验期间（通常几周）的效果[^kohavi2009controlled-e13]。
- **还没做出来的东西**。功能必须已经实现，而且质量足以给真实用户用[^kohavi2009controlled-e15]。早期想法先用原型和用户研究打磨 `[本项目分析]`。

**和相近方法的区别** `[本项目分析]`：

| | 在线对照实验 | [对照实验](controlled_experiment.md) | [田野实验](field_experiment.md) | [基准评测](../07_fields/computer-science/practices/benchmarking.md) | [准实验](quasi_experiment.md) |
|---|---|---|---|---|---|
| 谁参与 | 产品的真实用户，通常不知情 | 招募来的参与者，签知情同意书 | 真实世界的个人、村、学校 | 没有人，只有系统或模型 | 已经发生的事里的人 |
| 谁实施 | 产品方（或和产品方合作的研究者） | 研究者 | 合作的政府、组织、企业 | 研究者 | 没人为研究实施 |
| 规模和时长 | 成千上万人，几天到几周 | 几十人，一两个小时 | 几百到几千个单位，几个月到几年 | 一套评测集 | 看现成数据 |
| 主要难点 | 指标选择、数据质量、中途偷看、组间干扰 | 情境人为，人少 | 执行走样、流失、溢出 | 评测集是否有效 | 论证"近似随机" |

**你有没有条件做** `[本项目分析]`：在线对照实验需要一个有真实用户、能按用户分流、能记录行为数据的产品。学生和学术研究者往往没有。常见的出路是：和公司或开源平台合作；在自己运营的工具、插件、课程平台上做；或者退一步，招募参与者做[对照实验](controlled_experiment.md)。

**例子：贯穿全书的项目会不会用到它？** `[本项目分析]` 项目"现有大模型漏洞检测的评测结果被数据泄露高估了"本身是离线评测，主要方法是[基准评测](../07_fields/computer-science/practices/benchmarking.md)，用不到在线对照实验。但设想它的后续：你和一个智能合约审计平台合作，平台想知道，在去除泄露的新评测上更好的那个模型，换到线上以后是否真的帮审计员多确认了真实漏洞。这时就可以做在线对照实验：把审计任务随机分给"旧模型提示"和"新模型提示"两组，总体评价指标是每个任务中被确认的真实漏洞数，护栏指标是审计员处理误报花的时间。下面各步会接着用这个设想。

---

## 2. 怎么做

一个典型的在线实验，从开始到结束是：定指标 → 选随机化单位 → 算样本量 → 先跑 A/A、再小流量上线 → 按计划跑满时间 → 先查数据质量、再看结论 `[本项目分析]`。

### 第一步：定好总体评价指标，以及护栏指标和数据质量指标

**怎么做：**

- **总体评价指标**（Overall Evaluation Criterion，简称 OEC）是实验目标的量化度量，决定上不上线就看它。好的总体评价指标不应只看短期（如点击），而应包含能预测长期目标的因素，如用户的长期价值和回访[^kohavi2009controlled-e3]。最好只选一个指标，可以是几个目标的加权组合；这样权衡只做一次，所有实验共用一个清楚的目标[^kohavi2009controlled-e4]。
- **护栏指标**不直接说明改动是否成功，但上线时不能让它明显变差，例如页面加载时间[^dmitriev2017dirty-e2]。
- **数据质量指标**回答第一个问题：实验有没有被正确配置和运行，结果能不能信[^dmitriev2017dirty-e3]。下面第六步讲的样本比例就是其中最重要的一个。
- **比率指标要拆开**：对点击率这类指标，同时定义并报告分子和分母的计数[^dmitriev2017dirty-e4]。
- **在实验开始前定好**，并和相关各方商定怎样评价[^kohavi2009controlled-e21]。

**为什么：** 短期指标可能和真正的目标背道而驰。必应的一次实验因为程序缺陷给用户显示了很差的搜索结果，每用户查询数反而涨了 10% 以上，每用户收入涨了 30% 以上[^kohavi2012trustworthy-e4]。结果越差，用户搜得越多。事后再挑指标，又更容易碰巧找到看似显著的结果[^kohavi2009controlled-e7]。

**容易错在哪：** 指标测到的不是你想测的东西。微软的一次实验里，"用户点击更多"其实只是两组埋点（记录用户行为的代码）丢数据的程度不同[^kohavi2012trustworthy-e6]。作者把这类问题归为测量效度问题：指标在多大程度上测到了想测的概念[^kohavi2012trustworthy-e11]。效度的一般讲法见[效度与局限](../02_do-the-project/04_validity-and-limits.md)。

例子续 `[本项目分析]`：审计平台的实验里，"模型标出的漏洞数"是个坏的总体评价指标，模型多报误报它也会涨；"审计员确认的真实漏洞数"更接近目标。审计员处理每个任务的时间作为护栏指标。

### 第二步：选随机化单位

**怎么做：**

- 网上最常见的单位是用户；也有按用户日、会话或页面浏览计算指标的，但无论哪种都优先按用户随机。同一用户在整个实验中应看到一致的版本，通常靠存在 cookie 里的用户编号实现[^kohavi2009controlled-e5][^kohavi2012trustworthy-e1]。
- 分组程序要满足三条：每个用户看到各版本的机会相等；同一用户每次访问都分到同一版本；同时运行的多个实验之间分组互不相关[^kohavi2009controlled-e16]。

**为什么：** 统计分析假定各单位相互独立[^kohavi2009controlled-e5]。一个用户在不同访问中看到不同版本，或一个单位的结果受别的单位的分组影响，这个假定就不成立了 `[本项目分析]`。

**容易错在哪：组间干扰。** 有些场景里，处理组会影响对照组。例如在拍卖网站上给一部分用户"首个出价优惠"，处理会影响所有拍品，按用户随机测不准真实效果；这时改为随机分配拍品，而不是用户[^kohavi2009controlled-e23]。社交网络、双边市场里也常有这个问题；怎样避开和测量这种"溢出"，见田野实验的[想清溢出](field_experiment.md#第-9-步想清溢出)一步 `[本项目分析]`。

**容易错在哪：上一个实验留下的影响。** 有的平台反复使用同一批用户"分桶"，上一个实验影响过的用户会被用到下一个实验里；有一次三个月后这些用户还没恢复到实验前的水平[^kohavi2012trustworthy-e10]。

例子续 `[本项目分析]`：同一位审计员如果有时用旧模型、有时用新模型，会把一边学到的经验带到另一边；按审计员随机更稳妥。同一团队的审计员互相交流发现时，就要按团队随机。

### 第三步：算样本量和实验时长

**怎么做：** 先定功效（真实存在差异时能检测到它的概率）、想检测到多大的效应，用 A/A 测试（见第四步）估计指标的波动，再算出最小样本量和要跑多久[^kohavi2009controlled-e18]。

- **样本量可能比你想的大得多。** 文中的电商例子：想以 80% 的功效检测到收入 5% 的变化，需要 40.9 万以上用户[^kohavi2009controlled-e9]。
- **降低波动。** 把根本没接触到改动的用户排除出分析；例如改了结账页，就只分析到达结账页的用户[^kohavi2009controlled-e8]。
- **两组各一半。** 为了功效最大、时间最短，建议各 50%；按 99%/1% 分流，要跑大约 25 倍长的时间[^kohavi2009controlled-e19]。
- **按整周跑。** 即使流量很大，也至少跑一到两周，并按整周延长，以便分析星期几的影响[^kohavi2009controlled-e20]。
- **至少对总体评价指标和护栏指标事先做功效分析**[^dmitriev2017dirty-e6]。

**为什么：** 常见错误是功效不足[^kohavi2009controlled-e18]。功效不足时，结果不显著不等于没有影响[^dmitriev2017dirty-e6]；碰巧显著了，观察到的变化又更可能夸大了真实效应[^dmitriev2017dirty-e7]。

**容易错在哪：** 以为"跑得越久越准"。对每用户会话数等一些指标，置信区间不会随时间变窄，跑得更久并不增加功效[^kohavi2012trustworthy-e9]。功效的一般讲法见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

### 第四步：先跑 A/A 测试，再小流量上线

**怎么做：**

- **A/A 测试**：照常把用户分成两组，但两组看到完全相同的版本。它有两个用途：估计数据波动、供功效计算；检验实验系统本身，在 95% 置信水平下，应该只有约 5% 的时候显示"显著"[^kohavi2009controlled-e6]。要检查三件事：用户是否按计划比例分组，收集的数据是否和业务系统的记录一致，是否 95% 的时候结果不显著；并且和其他实验并行、持续地跑[^kohavi2009controlled-e17]。
- **回看实验前的数据**：用实验开始前一段时间的数据把两组算一遍，确认随机分出的两组在关键指标上本来就没有大差异[^fabijan2019diagnosing-e7]。
- **逐步放量**：先给很小比例的用户上线处理版本，每一步检查有没有严重问题，再让更多用户看到[^kohavi2009controlled-e11]。

**为什么：** A/A 测试是微软实验团队发现实际系统问题最有用的工具[^kohavi2012trustworthy-e3]。例如机器人流量会严重扭曲估计，作者见过机器人让 A/A 测试的假阳性远超 5%[^kohavi2009controlled-e10]。

**容易错在哪：** 把 A/A 测试当成一次性的上线检查。实验系统、埋点和流量都在变，所以要持续地跑[^kohavi2009controlled-e17]。

### 第五步：按计划跑满，盯住护栏，不要盯着结论

**怎么做：** 在事先定好的时间点做上线决定。如果确实需要边跑边看结论，就用为此设计的方法：把多看的次数计入 p 值，或改用允许持续监控的贝叶斯框架[^dmitriev2017dirty-e10]，或用"始终有效"的 p 值和置信区间，它们不管你什么时候停，都能控制假阳性率[^johari2015always-e3]。

**为什么：** 不断查看结果、一显著就停，会提高假阳性的概率；提前停止和临时延长实验都是很常见的错误[^dmitriev2017dirty-e9]。如果实验者一边盯着结果、一边决定什么时候停，常规的 p 值和置信区间就完全不可靠[^johari2015always-e1]。业界通常不做校正；即使只有一万个样本，假阳性率也很容易涨到五倍[^johari2015always-e2]。

**容易错在哪：** 把"监控"和"偷看结论"混为一谈。实验必须持续监控，用户体验明显变差时才能尽快关掉，这正是这个问题棘手的地方[^dmitriev2017dirty-e11]。`[本项目分析]` 可以把两件事分开：护栏指标和数据质量指标随时看，用来叫停；总体评价指标只在计划的时间点用来做决定。

**也不要被早期"趋势"骗了。** 多数实验的效应其实是稳定的，但前几天数据少、波动大，早期结果常常误导人[^kohavi2012trustworthy-e7]。

### 第六步：分析前，先查样本比例

**怎么做：** 看结论之前，先用卡方检验比较两组的实际人数和配置的比例[^fabijan2019diagnosing-e2]。两组人数偏离预期比例，叫**样本比例不匹配**（Sample Ratio Mismatch），说明抽样过程出了问题，很可能是程序有缺陷[^dmitriev2017dirty-e1][^kohavi2012trustworthy-e5]。检验显示差异不太可能是偶然时，必须查出根本原因[^fabijan2019diagnosing-e2]。

**为什么：**

- **它会让结果作废。** 样本比例不匹配带来选择偏差，使实验得出的任何因果推断都无效[^fabijan2019diagnosing-e4]。
- **偏差小也要当回事。** 50.2/49.8（821,588 对 815,482 个用户）看起来很接近 50/50，但纯属偶然的概率不到五十万分之一[^fabijan2019diagnosing-e1]。
- **它不罕见。** 微软近一年的实验中，大约 6% 出现样本比例不匹配[^fabijan2019diagnosing-e3]。
- **它可能让结论颠倒。** MSN 的一次轮播图实验，最初显示用户参与度下降；解决了导致样本比例不匹配的问题后，发现改动其实显著提高了参与度[^fabijan2019diagnosing-e6]。

**容易错在哪：** 只查整体、不查每个指标。原因可能出在实验设计、随机化、版本部署、数据记录、收集、加工和分析的任何环节[^fabijan2019diagnosing-e5]。比如两组遥测数据（产品自动回传的使用记录）的丢失率不同，就是让结果产生偏差的常见原因[^dmitriev2017dirty-e5]；过滤异常值时，也要确保各组受过滤规则的影响相同[^dmitriev2017dirty-e16]。

**一条通用的提醒：** 任何意外的指标变化，无论正负，通常说明有问题（特怀曼定律）[^dmitriev2017dirty-e14]。结果"好得不像真的"时，先查数据，再庆祝 `[本项目分析]`。

### 第七步：解读结果：效应大小、新奇效应和分群

**怎么做：**

- **报告置信区间。** 除了检验结果，还要给出两组之差的置信区间，它说明效应大概有多大[^kohavi2009controlled-e27]。
- **检查效应是否随时间变化。** 两种方向相反的效应要注意：老用户要适应新导航，开始时效率低，这叫首因效应；用户对新设计好奇、到处点，这叫新奇效应。一种办法是只看新用户，他们不受这两种效应影响[^kohavi2009controlled-e14]。也可以按实验的不同天、用户的不同次访问分别看效应[^dmitriev2017dirty-e13]。
- **分群分析要小心。** 分群条件本身不能受处理影响；一直细分用户直到找到显著结果，是多重检验问题，会提高假阳性率[^dmitriev2017dirty-e12]。但也要看重要的用户群：一个总体有利的改动，可能严重伤害某一群用户[^dmitriev2017dirty-e15]。
- **p 值在边界附近时重跑。** 微软的一个 p 值为 0.029 的正面结果，用双倍流量重跑后不再显著；作者建议重视强显著的指标，总体评价指标的 p 值在边界附近时用更大流量重跑[^dmitriev2017dirty-e8]。

**为什么：** 多数被怀疑的新奇效应和首因效应并不真实，只是统计上的假象[^kohavi2012trustworthy-e8]。先把效应随时间的变化画出来，再下结论 `[本项目分析]`。

**容易错在哪：** 结果不显著就上线，理由是"反正没坏处"。不显著可能真的没差别，也可能只是功效不够，改动其实有害[^kohavi2009controlled-e22]。

### 第八步：处理好伦理和知情同意

**一个反面例子。** 2014 年，Facebook 的研究者在 PNAS（《美国国家科学院院刊》）上发表了一项在 689,003 人身上做的实验[^kramer2014experimental-e1]，处理是减少用户动态消息里带情绪的内容[^kramer2014experimental-e2]。作者认为，用户注册时同意的数据使用政策就构成了知情同意[^kramer2014experimental-e3]。论文发表后，这项研究在知情同意和让参与者选择退出这两条原则上受到质疑[^verma2014editorial-e1]。康奈尔大学的伦理审查委员会认定，因为实验是 Facebook 为内部目的做的，不归学校管[^verma2014editorial-e2]；Facebook 作为私营公司，也没有义务遵守美国保护人类受试者的"共同规则"[^verma2014editorial-e3]。期刊仍然发表了编辑关注声明，关切数据收集可能不完全符合知情同意和允许退出的原则[^verma2014editorial-e4]。

**由此得到的做法** `[本项目分析]`：

- **公司内部常规做 A/B 测试，不等于你的研究可以不过伦理审查。** 你作为学术研究者参与、并打算发表时，按本单位的规定申请审查，说明用户会被怎样影响、被告知什么、能否退出。一般要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)，在真实环境里做随机实验的伦理考虑见田野实验的[处理好真实社区里的伦理](field_experiment.md#第-10-步处理好真实社区里的伦理)一步。
- **想清楚处理会不会伤人。** 改按钮颜色和操纵用户看到的情绪内容、价格、健康信息，风险完全不同。有些处理即使合法，按用户随机也不合适：例如测价格时，顾客发现别人拿到不同的价格，会伤害客户关系，可以改为随机分配商品[^kohavi2009controlled-e24]。
- **保护数据。** 实验日志是用户行为数据，按隐私规定处理，公开前去除身份信息。

---

## 3. 检查清单

下面主要依据微软等公司实验团队的经验论文整理，它们是业界做法，不是某个学会的审稿标准；在学术论文里，还要满足本学科对实验报告的要求 `[本项目分析]`。

**必须做到**

- [ ] 实验开始前定好总体评价指标，并和相关各方商定怎样评价[^kohavi2009controlled-e7][^kohavi2009controlled-e21]
- [ ] 按用户（或能包住干扰的单位）随机，同一用户始终看到同一版本[^kohavi2009controlled-e5][^kohavi2009controlled-e16]
- [ ] 至少对总体评价指标和护栏指标事先做功效分析，定好样本量和时长[^dmitriev2017dirty-e6]
- [ ] 分析前做样本比例检查；不匹配时查出原因，不能直接用结果[^fabijan2019diagnosing-e2][^fabijan2019diagnosing-e4]
- [ ] 不在偷看到显著时提前停止；需要边跑边看时，用为持续监控设计的方法[^dmitriev2017dirty-e9][^dmitriev2017dirty-e10]
- [ ] 报告效应的置信区间，而不只是"显著/不显著"[^kohavi2009controlled-e27]
- [ ] 作为学术研究发表时，通过本单位的伦理审查，说明知情同意和退出安排 `[本项目分析]`

**做到更好**

- [ ] 持续跑 A/A 测试，检查分组比例、数据和业务记录是否一致、假阳性率是否约 5%[^kohavi2009controlled-e17]
- [ ] 设护栏指标和数据质量指标；比率指标同时报告分子和分母[^dmitriev2017dirty-e2][^dmitriev2017dirty-e4]
- [ ] 小流量起步、逐步放量[^kohavi2009controlled-e11]
- [ ] 按整周跑，至少一到两周[^kohavi2009controlled-e20]
- [ ] 按天、按访问次数看效应，检查新奇效应和首因效应[^dmitriev2017dirty-e13]
- [ ] 回看实验前的数据，确认两组本来没有差异[^fabijan2019diagnosing-e7]

**做得出色**

- [ ] 总体评价指标的 p 值在边界附近时，用更大流量独立重跑一次[^dmitriev2017dirty-e8]
- [ ] 用访谈或可用性研究补上"为什么"[^kohavi2009controlled-e12]

**这些情况可以不做，不算缺陷** `[本项目分析]`

- 只看总体效应、不做分群分析：分群是探索性的，做了反而要处理多重检验；做了就要标成探索性，见[先做计划好的分析，计划外的标成探索性](../02_do-the-project/07_analyze-and-interpret.md#2-先做计划好的分析计划外的标成探索性)
- 流量小、无法按 50/50 分流或跑满多周时，按实际情况做，但要在论文里写明功效的限制

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 用短期点击、查询数当总体评价指标 | 可能和长期目标背道而驰，产品变差指标反而上涨[^kohavi2012trustworthy-e4] |
| 看了结果再挑指标 | 更容易碰巧找到显著结果[^kohavi2009controlled-e7] |
| 一显著就停，不显著就延长 | 假阳性率上升[^dmitriev2017dirty-e9] |
| 不查样本比例就看结论 | 选择偏差使因果推断无效，结论甚至可能颠倒[^fabijan2019diagnosing-e4][^fabijan2019diagnosing-e6] |
| 功效不足，又把"不显著"当成"没影响" | 改动可能有害，只是没测出来[^kohavi2009controlled-e22][^dmitriev2017dirty-e6] |
| 把前几天的趋势外推 | 早期数据波动大，常常误导人[^kohavi2012trustworthy-e7] |
| 一直细分用户直到找到显著的一群 | 多重检验，假阳性率上升[^dmitriev2017dirty-e12] |
| 处理组会影响对照组时仍按用户随机 | 测不准真实效果[^kohavi2009controlled-e23] |
| 结果好得出奇就直接上线 | 意外的指标变化通常说明有问题[^dmitriev2017dirty-e14] |
| 以为公司的数据政策就等于知情同意 | 期刊和学界仍会质疑[^verma2014editorial-e4] |

---

## 5. 延伸阅读

- **入门和全貌**：Kohavi 等人 2009，《数据挖掘与知识发现》上的综述和实践指南，讲总体评价指标、功效和样本量、随机化算法、局限，以及一批实践教训。本文的多数操作建议来自这里。
- **结果为什么不可信**：Kohavi 等人 2012，用五个令人困惑的真实结果，讲指标选择、埋点、早期趋势、功效和遗留效应。
- **怎样解读指标**：Dmitriev 等人 2017，十二个常见的指标解读陷阱，每个都配真实例子。
- **样本比例不匹配**：Fabijan 等人 2019，分类讲各种原因和诊断方法。
- **中途偷看的统计学**：Johari 等人的"始终有效的推断"，适合想在实验中持续监控的读者，需要一定统计基础。
- **伦理争议**：Kramer 等人 2014 和 PNAS 的编辑关注声明，两篇一起读。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^kohavi2009controlled-e1]: Kohavi 等人 2009，§1，第 142 页。[证据](../../sources/notes/kohavi2009controlled.md#e1)
[^kohavi2009controlled-e2]: Kohavi 等人 2009，§3，第 149 页。[证据](../../sources/notes/kohavi2009controlled.md#e2)
[^kohavi2009controlled-e3]: Kohavi 等人 2009，§3.1，第 150 页。[证据](../../sources/notes/kohavi2009controlled.md#e3)
[^kohavi2009controlled-e4]: Kohavi 等人 2009，§3.1，第 150 页。[证据](../../sources/notes/kohavi2009controlled.md#e4)
[^kohavi2009controlled-e5]: Kohavi 等人 2009，§3.1，第 150 页。[证据](../../sources/notes/kohavi2009controlled.md#e5)
[^kohavi2009controlled-e6]: Kohavi 等人 2009，§3.1，第 151 页。[证据](../../sources/notes/kohavi2009controlled.md#e6)
[^kohavi2009controlled-e7]: Kohavi 等人 2009，§3.2.4，第 154 页。[证据](../../sources/notes/kohavi2009controlled.md#e7)
[^kohavi2009controlled-e8]: Kohavi 等人 2009，§3.2，第 151 页。[证据](../../sources/notes/kohavi2009controlled.md#e8)
[^kohavi2009controlled-e9]: Kohavi 等人 2009，§3.2.1，第 153 页。[证据](../../sources/notes/kohavi2009controlled.md#e9)
[^kohavi2009controlled-e10]: Kohavi 等人 2009，§3.4，第 155 页。[证据](../../sources/notes/kohavi2009controlled.md#e10)
[^kohavi2009controlled-e11]: Kohavi 等人 2009，§3.5.1，第 156 页。[证据](../../sources/notes/kohavi2009controlled.md#e11)
[^kohavi2009controlled-e12]: Kohavi 等人 2009，§3.6，第 157 页。[证据](../../sources/notes/kohavi2009controlled.md#e12)
[^kohavi2009controlled-e13]: Kohavi 等人 2009，§3.6，第 157 页。[证据](../../sources/notes/kohavi2009controlled.md#e13)
[^kohavi2009controlled-e14]: Kohavi 等人 2009，§3.6，第 158 页。[证据](../../sources/notes/kohavi2009controlled.md#e14)
[^kohavi2009controlled-e15]: Kohavi 等人 2009，§3.6，第 158 页。[证据](../../sources/notes/kohavi2009controlled.md#e15)
[^kohavi2009controlled-e16]: Kohavi 等人 2009，§5.1，第 163–164 页。[证据](../../sources/notes/kohavi2009controlled.md#e16)
[^kohavi2009controlled-e17]: Kohavi 等人 2009，§6.2.1，第 174 页。[证据](../../sources/notes/kohavi2009controlled.md#e17)
[^kohavi2009controlled-e18]: Kohavi 等人 2009，§6.2.3，第 175 页。[证据](../../sources/notes/kohavi2009controlled.md#e18)
[^kohavi2009controlled-e19]: Kohavi 等人 2009，§6.2.4，第 175 页。[证据](../../sources/notes/kohavi2009controlled.md#e19)
[^kohavi2009controlled-e20]: Kohavi 等人 2009，§6.2.5，第 175 页。[证据](../../sources/notes/kohavi2009controlled.md#e20)
[^kohavi2009controlled-e21]: Kohavi 等人 2009，§6.3.1，第 176 页。[证据](../../sources/notes/kohavi2009controlled.md#e21)
[^kohavi2009controlled-e22]: Kohavi 等人 2009，§6.3.2，第 176 页。[证据](../../sources/notes/kohavi2009controlled.md#e22)
[^kohavi2009controlled-e23]: Kohavi 等人 2009，附录 A，第 178 页。[证据](../../sources/notes/kohavi2009controlled.md#e23)
[^kohavi2009controlled-e24]: Kohavi 等人 2009，附录 A，第 179 页。[证据](../../sources/notes/kohavi2009controlled.md#e24)
[^kohavi2009controlled-e25]: Kohavi 等人 2009，§1，第 142 页。[证据](../../sources/notes/kohavi2009controlled.md#e25)
[^kohavi2009controlled-e26]: Kohavi 等人 2009，§2.4，第 146 页。[证据](../../sources/notes/kohavi2009controlled.md#e26)
[^kohavi2009controlled-e27]: Kohavi 等人 2009，§3.3，第 154 页。[证据](../../sources/notes/kohavi2009controlled.md#e27)
[^kohavi2012trustworthy-e1]: Kohavi 等人 2012，§1，第 1 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e1)
[^kohavi2012trustworthy-e2]: Kohavi 等人 2012，§1，第 2 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e2)
[^kohavi2012trustworthy-e3]: Kohavi 等人 2012，§2，第 3 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e3)
[^kohavi2012trustworthy-e4]: Kohavi 等人 2012，§3.1.2，第 3 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e4)
[^kohavi2012trustworthy-e5]: Kohavi 等人 2012，§3.1.3，第 4 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e5)
[^kohavi2012trustworthy-e6]: Kohavi 等人 2012，§3.2.3，第 4 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e6)
[^kohavi2012trustworthy-e7]: Kohavi 等人 2012，§3.3.4，第 6 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e7)
[^kohavi2012trustworthy-e8]: Kohavi 等人 2012，§3.3.1，第 5 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e8)
[^kohavi2012trustworthy-e9]: Kohavi 等人 2012，§3.4.2，第 6 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e9)
[^kohavi2012trustworthy-e10]: Kohavi 等人 2012，§3.5.3，第 7–8 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e10)
[^kohavi2012trustworthy-e11]: Kohavi 等人 2012，§4，第 8 页。[证据](../../sources/notes/kohavi2012trustworthy.md#e11)
[^dmitriev2017dirty-e1]: Dmitriev 等人 2017，§4。[证据](../../sources/notes/dmitriev2017dirty.md#e1)
[^dmitriev2017dirty-e2]: Dmitriev 等人 2017，§4。[证据](../../sources/notes/dmitriev2017dirty.md#e2)
[^dmitriev2017dirty-e3]: Dmitriev 等人 2017，§4。[证据](../../sources/notes/dmitriev2017dirty.md#e3)
[^dmitriev2017dirty-e4]: Dmitriev 等人 2017，§5.2。[证据](../../sources/notes/dmitriev2017dirty.md#e4)
[^dmitriev2017dirty-e5]: Dmitriev 等人 2017，§5.3。[证据](../../sources/notes/dmitriev2017dirty.md#e5)
[^dmitriev2017dirty-e6]: Dmitriev 等人 2017，§5.4。[证据](../../sources/notes/dmitriev2017dirty.md#e6)
[^dmitriev2017dirty-e7]: Dmitriev 等人 2017，§5.4。[证据](../../sources/notes/dmitriev2017dirty.md#e7)
[^dmitriev2017dirty-e8]: Dmitriev 等人 2017，§5.5。[证据](../../sources/notes/dmitriev2017dirty.md#e8)
[^dmitriev2017dirty-e9]: Dmitriev 等人 2017，§5.6。[证据](../../sources/notes/dmitriev2017dirty.md#e9)
[^dmitriev2017dirty-e10]: Dmitriev 等人 2017，§5.6。[证据](../../sources/notes/dmitriev2017dirty.md#e10)
[^dmitriev2017dirty-e11]: Dmitriev 等人 2017，§5.6。[证据](../../sources/notes/dmitriev2017dirty.md#e11)
[^dmitriev2017dirty-e12]: Dmitriev 等人 2017，§5.8。[证据](../../sources/notes/dmitriev2017dirty.md#e12)
[^dmitriev2017dirty-e13]: Dmitriev 等人 2017，§5.10。[证据](../../sources/notes/dmitriev2017dirty.md#e13)
[^dmitriev2017dirty-e14]: Dmitriev 等人 2017，§5.12。[证据](../../sources/notes/dmitriev2017dirty.md#e14)
[^dmitriev2017dirty-e15]: Dmitriev 等人 2017，§5.7。[证据](../../sources/notes/dmitriev2017dirty.md#e15)
[^dmitriev2017dirty-e16]: Dmitriev 等人 2017，§5.9。[证据](../../sources/notes/dmitriev2017dirty.md#e16)
[^fabijan2019diagnosing-e1]: Fabijan 等人 2019，§2.3.1。[证据](../../sources/notes/fabijan2019diagnosing.md#e1)
[^fabijan2019diagnosing-e2]: Fabijan 等人 2019，§2.3.1。[证据](../../sources/notes/fabijan2019diagnosing.md#e2)
[^fabijan2019diagnosing-e3]: Fabijan 等人 2019，§4.1。[证据](../../sources/notes/fabijan2019diagnosing.md#e3)
[^fabijan2019diagnosing-e4]: Fabijan 等人 2019，§4.2。[证据](../../sources/notes/fabijan2019diagnosing.md#e4)
[^fabijan2019diagnosing-e5]: Fabijan 等人 2019，§4.3。[证据](../../sources/notes/fabijan2019diagnosing.md#e5)
[^fabijan2019diagnosing-e6]: Fabijan 等人 2019，§1。[证据](../../sources/notes/fabijan2019diagnosing.md#e6)
[^fabijan2019diagnosing-e7]: Fabijan 等人 2019，§5.1。[证据](../../sources/notes/fabijan2019diagnosing.md#e7)
[^johari2015always-e1]: Johari 等人，arXiv 1512.04922，摘要。[证据](../../sources/notes/johari2015always.md#e1)
[^johari2015always-e2]: Johari 等人，arXiv 1512.04922，§1。[证据](../../sources/notes/johari2015always.md#e2)
[^johari2015always-e3]: Johari 等人，arXiv 1512.04922，§1。[证据](../../sources/notes/johari2015always.md#e3)
[^kramer2014experimental-e1]: Kramer 等人 2014，Significance。[证据](../../sources/notes/kramer2014experimental.md#e1)
[^kramer2014experimental-e2]: Kramer 等人 2014，摘要。[证据](../../sources/notes/kramer2014experimental.md#e2)
[^kramer2014experimental-e3]: Kramer 等人 2014，Materials and Methods。[证据](../../sources/notes/kramer2014experimental.md#e3)
[^verma2014editorial-e1]: Verma 2014，PNAS 编辑关注声明。[证据](../../sources/notes/verma2014editorial.md#e1)
[^verma2014editorial-e2]: Verma 2014，PNAS 编辑关注声明。[证据](../../sources/notes/verma2014editorial.md#e2)
[^verma2014editorial-e3]: Verma 2014，PNAS 编辑关注声明。[证据](../../sources/notes/verma2014editorial.md#e3)
[^verma2014editorial-e4]: Verma 2014，PNAS 编辑关注声明。[证据](../../sources/notes/verma2014editorial.md#e4)
