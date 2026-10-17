# 仓库挖掘研究：从代码仓库、缺陷库和问答网站中挖数据

本文讲**仓库挖掘研究**（mining software repositories）：用程序从代码仓库、缺陷库、邮件列表、问答网站等地方大规模抽取数据，再做定量分析，以此研究软件是怎样开发出来的。

**适用范围**：这是计算机的做法，例子和标准主要来自软件工程的实证研究。它最常服务[观察描述](../../../05_research-strategies/observe_describe.md)这种研究套路，弄清软件开发里实际发生了什么；用来检验"X 是否导致 Y"时，还要满足[解释因果](../../../05_research-strategies/explain_causality.md)的要求。这两种套路各学科通用的部分见套路页，本文只讲挖掘软件数据特有的做法。

如果你只是要从 GitHub 上收集一批数据来训练或评测模型，数据收集那部分同样适用本文的第 2 节；模型本身怎么评测，见[基准评测](benchmarking.md)；效度的一般原则见[效度与局限](../../../02_do-the-project/04_validity-and-limits.md)。

**读完本文，你应该能：**

- 判断自己的问题适不适合用仓库挖掘来回答，以及它能回答到什么程度；
- 按步骤完成一项挖掘研究：选数据源、筛项目、抽取清洗、关联数据、人工标注、分析；
- 认出 git 和 GitHub 数据里最常见的陷阱；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为：对从托管结构化或半结构化文本的平台（例如源代码仓库）中抽取的数据集做定量分析的研究[^ralph2020empirical-e105]。常见的数据来源有代码仓库、邮件列表存档、缺陷跟踪系统、问答论坛和聊天平台[^ralph2020empirical-e106]。

**它擅长回答的问题**：

- **描述性问题**：某种语言、工具、做法用得有多普遍，提交和贡献的规模如何。GitHub 这类数据可以直接用来描述项目属性[^kalliamvakou2014promises-e11]。
- **关系性问题**：哪些因素和缺陷、合并速度、贡献者流失等结果**相关**。
- **为后续研究找线索**：先在大量项目中发现规律，再用实验或访谈去解释。

**它的局限要心里有数**：

- **一般只能得到相关，得不到因果。** 看到"某种编码风格的代码缺陷更多"，只说明两者相关；要相信存在因果关系，还需要主动改变编码风格的后续实验[^menzies2019bad-e10]。SIGSOFT 标准把"确立因果关系（例如用纵向分析）"列为优秀项，而不是必要项[^ralph2020empirical-e117]；由此推断，普通的挖掘研究默认只能给出相关。一个常见的**混杂因素**（同时影响两个变量、让它们看起来相关的第三个因素）是项目规模：大项目提交多、贡献者多、缺陷报告也多，很多看似有关的指标其实都只是在反映规模。
- **数据讲不出全部故事。** 挖出来的数据只是开发活动留下的痕迹[^kalliamvakou2016indepth-e11]；用它对"协作""质量""流行度"这类抽象概念下结论，需要格外谨慎[^kalliamvakou2014promises-e11]。

**和相近类型的区别：**

| | 仓库挖掘 | 案例研究 | 数据科学 / 预测建模 | 定性内容分析 |
|---|---|---|---|---|
| 研究对象 | 大量仓库，用程序批量抽取 | 少数几个背景丰富的项目 | 从数据中训练模型 | 少量文本，人工细读 |
| 主要分析 | 定量统计 | 多种证据深入理解一个场景 | 预测效果 | 编码、归纳主题 |
| 典型问题 | "多普遍？和什么相关？" | "这里为什么会这样？" | "能不能预测？" | "人们在说什么、怎么说？" |

依据：SIGSOFT 仓库挖掘标准的适用范围（数据科学、案例研究两列）[^ralph2020empirical-e107]；其余对比由本项目整理。

**怎么选**：问题需要"很多项目的规律"时，用仓库挖掘；需要理解"为什么"时，配合访谈、问卷或案例研究。只研究两三个项目，按案例研究的要求来做，不要用大样本的口吻下结论。

在计算机的其他方向也有类似研究，例如安全方向从提交历史中挖漏洞修复，机器学习方向从 GitHub 收集代码和问题报告构建数据集。下面的陷阱对它们同样适用。

---

## 2. 怎么做

### 第一步：写清研究问题和分析单元

先写清为什么这个问题适合用仓库挖掘来回答，再定义**分析单元**：你统计的"一个"到底是什么——一个仓库、一个项目、一次提交、一个拉取请求（pull request），还是一个开发者[^ralph2020empirical-e108]。

**容易错在哪**：把"仓库"当成"项目"。在 GitHub 上，一个项目往往由主仓库和许多复刻（fork）仓库组成，分析项目要把它们放在一起考虑[^kalliamvakou2014promises-e2]。同样，"一个开发者"也不等于"一个账号"或"一个邮箱"（见第四步）。

### 第二步：选数据源，并论证为什么选它

说明用哪个平台、为什么它适合你的问题[^ralph2020empirical-e109]。要特别检查：**你关心的活动，是否真的都发生在这个平台上？**

- 有的仓库只是外部仓库的镜像[^kalliamvakou2014promises-e8]；有的项目，特别是迁移到 GitHub 的项目，用的是外部的问题跟踪系统[^kalliamvakou2014promises-e9]。
- 需要一个项目的**全部**提交时，只看 GitHub 仓库是反面模式，因为它不一定包含全部提交[^ralph2020empirical-e121]。
- 公开平台只能看到公开活动，私有仓库里的工作看不到。这无法避免，只能在讨论中承认，并尽量在其他情境中重复研究[^kalliamvakou2016indepth-e2]。

**用现成数据集还是自己抓？** GitHub 的接口只报告**当前状态**，不报告历史事件；仓库一旦删除，它的事件和元数据就全部丢失[^kalliamvakou2016indepth-e3]。持续存档的数据服务（如 GHTorrent）可以弥补这一点，但这些服务自身也带有采集假设，用之前要读它的说明[^kalliamvakou2016indepth-e5]。

### 第三步：筛选和抽样项目

这是挖掘研究最容易出问题的一步。

**先说清抽样目标和总体。** 你想把结论推广到哪些项目上？是"所有开源项目"，还是"GitHub 上活跃的 Java 库"？把抽样过程写成一个多阶段的算法：从哪个名单出发，每一步按什么条件筛掉哪些，并反思每一步可能带来什么偏差[^baltes2022sampling-e12][^ralph2020empirical-e127]。

**一定要过滤。** GitHub 上的大多数项目是个人的、不活跃的，有些仓库只用来存文件或托管网站[^kalliamvakou2014promises-e1]；项目提交数的中位数只有 6[^kalliamvakou2014promises-e3]。不加任何筛选标准地使用开源仓库，就是便利抽样[^ralph2020empirical-e120]，也就是按"方便拿到"来选对象，会威胁结论的可推广性[^baltes2022sampling-e2]。常用的过滤条件：

- **个人项目**：看提交者人数，67% 的项目只有一个提交者[^kalliamvakou2014promises-e5]。
- **不活跃项目**：看近期是否有提交、拉取请求或问题报告[^kalliamvakou2016indepth-e7]。
- **不是软件开发的仓库**：仓库用途无法从元数据可靠地自动判断，要看描述和 README（仓库里的说明文件）[^kalliamvakou2014promises-e4]。
- **镜像仓库、复刻仓库**：避开描述中写明是镜像的项目，以及大量提交者不是平台注册用户的项目[^kalliamvakou2014promises-e8]；复刻要么排除，要么并入所属项目[^kalliamvakou2014promises-e2]。
- **经验法则**：选近期提交和拉取请求都较多、提交者和作者超过 2 人的项目[^kalliamvakou2014promises-e10]。

**验证你的过滤条件。** 自动筛选的结果要人工抽查一批，看看留下的是不是你想要的、筛掉的是不是该筛的[^ralph2020empirical-e109]。

**容易错在哪**：

- **以为样本大就有代表性。** **抽样框**（实际用来抽样的那份名单）本身有偏差时，样本再大也无法弥补[^baltes2022sampling-e5]。从"按目的挑出的子集"里再随机抽样，也不能说明它代表一般软件[^baltes2022sampling-e16][^ralph2020empirical-e37]。
- **以为过滤越严越好。** 筛选会大幅减少可研究的项目数量[^kalliamvakou2016indepth-e10]，也会让结论只适用于留下的那类项目。

**补救办法**：每个数据源都可能以不明显的方式带有偏差[^baltes2022sampling-e14]。如果条件允许，用**概率抽样**（总体中每个对象被抽中的概率已知且不为零，例如随机抽样）[^ralph2020empirical-e114]；担心某个平台有偏差，就换一个平台重复研究，例如在 GitHub 上发现的规律，到 SourceForge 上再验证一次[^baltes2022sampling-e13]。

### 第四步：抽取和清洗数据

把每一步预处理都记录下来[^ralph2020empirical-e110]。最好写一个可以从头重新运行的抽取流程（脚本或流水线），原始数据只读、其他都能重新生成，见[整理科研材料](../../../08_throughout/organizing_materials.md#2-原始数据只读其余都能重新生成)。

重度依赖数据的研究必须时刻警惕数据质量[^menzies2019bad-e11]。清洗时，逐条检查下面这些已知陷阱，判断它们会不会影响你的问题：

**git 历史的陷阱**

- **历史可以被改写。** 通过变基（rebase）、压缩提交（squash）等操作，仓库里的历史未必反映真实发生的开发过程，官方稳定仓库尤其如此[^bird2009promises-e2]。被变基的旧提交会从仓库中消失[^kalliamvakou2016indepth-e4]。
- **只看得到"成功"的提交。** 被拒绝或被重写的工作往往不在历史里[^bird2009promises-e5]。很多项目要求合并前压缩提交，你只能看到评审之后的结果[^kalliamvakou2014promises-e6]。
- **分支和合并信息不完整。** 并不总能确定一个提交是在哪个分支上做的[^bird2009promises-e3]；**快进合并**（fast-forward，git 直接把分支指针移到新提交上、不生成合并提交的合并方式）不留下合并提交，有时连"发生过合并"都无法判断[^bird2009promises-e4]。

**GitHub 平台的陷阱**

- **"已合并"标记不可信。** 所有拉取请求中，近 40% 实际已合并，却显示为未合并[^kalliamvakou2014promises-e1]；我们推测，原因之一可能是不少项目在平台之外完成合并。不要依赖这个标记，应使用启发式规则识别实际合并[^kalliamvakou2014promises-e7]。有研究直接用这个标记区分拉取请求的成败，结论可能因此受影响[^kalliamvakou2016indepth-e8]。
- **一人多号。** 同一个人可能用多个邮箱提交，例如 Linus Torvalds 在 GitHub 上 47% 的提交没有关联到他的账号；需要把活动对应到人时，要做身份合并[^kalliamvakou2016indepth-e1]。
- **机器人账号。** 人均提交数极高的离群值往往是自动化机器人[^kalliamvakou2014promises-e10]，它们往往只向单个仓库提交[^kalliamvakou2016indepth-e7]。研究"人"的行为时要识别并排除。
- **平台本身在变。** 例如"关注者（watchers）"的含义在 2012 年 8 月前后不同；要了解接口和网站随时间的变化[^kalliamvakou2016indepth-e6]。跨越这些时间点的趋势，可能只是平台改版造成的。

**为什么要这么较真？** Bird 等人坦言，他们自己就因为没有完全理解数据是怎样产生的，一开始得出了错误结论[^bird2009promises-e1]。数据里的陷阱就是假设里的陷阱，也就是结果里的陷阱[^kalliamvakou2016indepth-e12]。

**你的工具也要测试。** 抽取脚本本身可能有缺陷，SIGSOFT 标准把测试自己的工具、分析工具失效的情形列为加分项[^ralph2020empirical-e115]。

### 第五步：关联不同来源的数据

很多问题需要把提交和问题报告、拉取请求、评审意见连起来，例如"哪些提交修复了缺陷"。

**常见做法**：在提交信息里找特定格式的缺陷编号，排除版本号、年份等误报，确认编号在缺陷库中存在，再检查缺陷是否在提交前后几天内有修复活动[^bird2009fair-e4]。

**容易错在哪**：

- **链接本身不完整，而且有偏差。** 把代码修改链接到缺陷库，没有统一或强制的做法[^bird2009fair-e2]；能链接上的只是全部已修复缺陷的一部分[^kalliamvakou2014promises-e12]，而且有系统性偏差[^bird2009fair-e1]。例如，如果有经验的开发者更认真地标注修复，基于这类数据可能得出"越有经验的开发者犯错越多"的错误结论[^bird2009fair-e3]。
- **类别标签不可靠。** Herzig 等人人工检查问题报告后发现，33.8% 标为"缺陷"的报告其实是新功能、文档更新或重构；平均 39% 被标为有缺陷的文件其实从未有过缺陷[^herzig2013bug-e1]。用数据库查询筛出"缺陷"看似简单，但前提是分类准确[^herzig2013bug-e2]。

**怎么做**：对自动链接和自动分类的结果，人工抽查一批，既查误报，也查漏报[^bird2009fair-e5]。用启发式规则识别合并来源时，要检验它的召回率（真实的合并中有多少被识别出来）[^bird2009promises-e6]；识别身份等其他规则同理。把数据质量作为效度威胁写进论文[^herzig2013bug-e5]。

### 第六步：人工标注，并检验一致性

很多挖掘研究需要人来判断：这份报告是不是缺陷？这条评论属于哪一类？判断越可能有争议，越需要多名标注者[^ralph2020empirical-e128]。

**怎么做**[^ralph2020empirical-e111][^ralph2020empirical-e129]：

1. 写好标注方案和判定规则，并在论文中公开。类别之间的界限常常本身就不清楚，换一套规则结果就会变；Herzig 等人的应对是逐字公开完整的分类规则[^herzig2013bug-e4]。
2. 两名以上标注者**独立**标注。Herzig 等人让第二人在不知道第一人结论的情况下复核被改判的报告，有冲突的再做第三次检查[^herzig2013bug-e3]。
3. 报告标注者人数和流程，以及分歧怎么解决。
4. 用合适的统计量报告一致性，例如 Cohen's Kappa（一种衡量两人判断有多一致的统计量）或 Krippendorff's α（同类统计量，可用于多人）[^ralph2020empirical-e130]。
5. 更好的做法是多轮迭代：先标一部分，解决分歧，修改规则，直到一致性达到阈值，再标其余数据[^ralph2020empirical-e131]。

**容易错在哪**：一致性低于公认阈值却说成"良好"；算了好几种一致性指标，只报告最好看的那个[^ralph2020empirical-e132]。

### 第七步：分析，并说清效度威胁

通用的统计和效度问题见[分析与解读](../../../02_do-the-project/07_analyze-and-interpret.md)和[效度与局限](../../../02_do-the-project/04_validity-and-limits.md)。挖掘研究要特别注意以下几点：

- **度量要经过验证。** 说明并论证你用的每个指标，最好使用别人验证过的度量[^ralph2020empirical-e112]。用一个未经验证的单一指标度量多维概念，例如用 GitHub 星标数代表"流行度"，是反面模式[^ralph2020empirical-e119]。容易计算的指标往往隐藏风险[^kalliamvakou2016indepth-e9]。
- **大样本下，显著不等于重要。** 道理和例子见[分析与解读](../../../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。挖掘研究中的例子：Bird 等人发现迁移到 git 前后提交大小的差异统计显著，但只差每次提交 2 行[^bird2009promises-e7]。报告效应大小，而不只是 p 值。
- **结论限定在你选的仓库范围内。** 把结论推广到所选仓库之外是反面模式[^ralph2020empirical-e122]。要讨论数据源、仓库、筛选条件带来的外部效度威胁（结论能否推广到研究对象之外，见[效度与局限](../../../02_do-the-project/04_validity-and-limits.md#5-外部效度结论能推广到哪里)）[^ralph2020empirical-e113]；承认了局限，写结论时就不要当它不存在[^ralph2020empirical-e66]。
- **不要只停留在描述。** 只做定量描述、不检验或建立理论，是反面模式[^ralph2020empirical-e122]。
- **用定性数据补充。** 用访谈、问卷或人工检查来核对你对数据的假设[^kalliamvakou2016indepth-e11]；SIGSOFT 也把跨数据源、跨研究者的**三角验证**（用多种来源或多名研究者互相印证同一结论）列为加分项[^ralph2020empirical-e115]。

### 第八步：处理伦理和许可问题

挖掘的数据大多是人留下的：提交者的姓名和邮箱、评论、问答帖子。公开可见不等于可以随便用。涉及人的研究的一般原则，见[科研诚信与伦理](../../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)；下面是挖掘研究特有的几点。

- **"技术上拿得到"不等于"合法可用"。** 仅以"能访问、能下载"为理由使用数据是反面模式[^ralph2020empirical-e135]。要说明数据基于什么依据可以合法地用于研究[^ralph2020empirical-e133]，例如网站的使用条款明确允许为研究目的抓取这类信息[^ralph2020empirical-e134]。
- **评估风险和隐私。** 描述对数据保管方和数据主体可能的风险或伤害[^ralph2020empirical-e133]；合并多个数据集时，说明如何缓解额外的隐私风险[^ralph2020empirical-e136]。
- **小心重新识别。** 在论文中引用"匿名"的评论原文，别人用搜索引擎就可能找到作者[^ralph2020empirical-e137]。需要引用时，考虑改写或隐去可搜索的细节。
- **再次发布数据时，尊重原来的条件。** 公开你的数据集时，要说明如何尊重数据主体的预期和同意[^ralph2020empirical-e138]。如果数据集包含代码，还要注意原代码的开源许可证是否允许再分发；拿不准时只发布标识符（仓库名和提交哈希）和脚本，让别人自己下载 `[待确认]`。
- 出于伦理考虑隐去数据集的部分细节，是可以接受的[^ralph2020empirical-e118]。

### 第九步：让研究能被复现

挖掘研究的数据会变：仓库被删除、历史被改写，平台接口也在变[^kalliamvakou2016indepth-e3][^kalliamvakou2016indepth-e4][^kalliamvakou2016indepth-e6]。过了一年，你用同样的脚本也未必能得到同样的数据。存档和数据共享的一般做法见[科研诚信与伦理](../../../08_throughout/integrity_and_ethics.md#3-让别人能核查你的工作)；挖掘研究要特别做到：

- **写清数据是什么时候采集的。** 详细说明收集了什么数据、在哪里、什么时候、怎样收集[^ralph2020empirical-e125]。例如 Kalliamvakou 等人写明了所用数据集快照的发布时间[^kalliamvakou2014promises-e13]。
- **公开数据集快照和全部脚本**，包括下载、筛选、预处理和后处理用的工具[^ralph2020empirical-e114]。描述太粗、数据和代码不公开，别人就无法复现[^menzies2019bad-e12]。只放在 GitHub 上不算妥善存档[^ralph2020empirical-e78]；数据因伦理或许可原因不能公开时，说明理由即可[^ralph2020empirical-e76]。
- **固定快照，而不是追着最新数据。** 数据集很快会过时，保持稳定和保持更新之间存在内在矛盾[^baltes2022sampling-e15]；论文结论应对应一个固定日期的快照，后续更新另行发布新版本。
- **给出可重复的抽样步骤**，让别人能得到同样的样本[^ralph2020empirical-e127]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 实证研究标准中的仓库挖掘标准。

**必须做到**

- [ ] 说明为什么这个问题适合用仓库挖掘来研究；定义分析单元[^ralph2020empirical-e108]
- [ ] 说明并论证数据源，以及从中选仓库的方式；说明怎样验证了纳入和排除标准[^ralph2020empirical-e109]
- [ ] 描述数据获取流程、数据集特征和预处理步骤[^ralph2020empirical-e110]
- [ ] 写清数据采集的时间[^ralph2020empirical-e125]
- [ ] 有人工标注时：多名标注者，报告标注者人数，详细描述标注流程，评估一致性[^ralph2020empirical-e111]
- [ ] 说明并论证所用度量，使用经过验证的度量或评估构念效度[^ralph2020empirical-e112]
- [ ] 讨论数据源、仓库、筛选条件带来的外部效度威胁[^ralph2020empirical-e113]
- [ ] 使用涉及人的数据时：说明合法使用依据、风险和隐私保护[^ralph2020empirical-e133][^ralph2020empirical-e136][^ralph2020empirical-e138]

**做到更好**

- [ ] 公开完整数据集和全部工具；条件允许时使用概率抽样[^ralph2020empirical-e114]
- [ ] 跨数据源或研究者做三角验证；分析工具失效的情形；测试自己的工具[^ralph2020empirical-e115]
- [ ] 标注者反思自身偏见；建立或检验理论；讨论伦理问题[^ralph2020empirical-e116]

**做得出色**

- [ ] 确立因果关系，例如用纵向分析[^ralph2020empirical-e117]

**这些情况可以不做，不算缺陷**[^ralph2020empirical-e118]

- 专门研究某个生态（如 Apache）时，只选该生态的仓库
- 出于伦理考虑，隐去数据集的部分细节

**审稿时常见、但不成立的批评**[^ralph2020empirical-e123][^ralph2020empirical-e124]：你不必为此担心

- 没有充分理由地要求"更多数据、更多数据源、更多仓库"
- "没有做定性分析"
- 数据源已经论证过，还要求"换一个数据源"
- 抱怨为保护参与者身份而有意隐去的仓库细节
- 人工研究要求报告花了多少时间

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不加筛选地抓一批仓库 | 大多数仓库是个人的、不活跃的，这是便利抽样[^kalliamvakou2014promises-e1][^ralph2020empirical-e120] |
| 把一个仓库当成一个项目 | 漏掉复刻中的活动，或重复计算[^kalliamvakou2014promises-e2] |
| 以为样本大就有代表性 | 抽样框的偏差，样本再大也无法弥补[^baltes2022sampling-e5] |
| 只看 GitHub 就当作项目的全部活动 | 镜像、外部问题跟踪系统都会漏掉[^kalliamvakou2014promises-e8][^ralph2020empirical-e121] |
| 直接相信"已合并"等平台字段 | 大量实际合并显示为未合并[^kalliamvakou2014promises-e1][^kalliamvakou2014promises-e7] |
| 直接相信问题报告的"缺陷"标签 | 三分之一的"缺陷"其实不是缺陷[^herzig2013bug-e1] |
| 只用能链接上的缺陷修复 | 链接有系统性偏差，可能得出错误的结论[^bird2009fair-e3] |
| 把 git 历史当作真实过程 | 历史可能被改写、压缩，失败的工作看不到[^bird2009promises-e2][^bird2009promises-e5] |
| 不排除机器人、不合并身份 | 统计"人"的行为时失真[^kalliamvakou2014promises-e10][^kalliamvakou2016indepth-e1] |
| 只报告 p 值 | 大样本下微不足道的差异也会显著[^menzies2019bad-e2][^bird2009promises-e7] |

---

## 5. 延伸阅读

- **仓库挖掘标准原文**：SIGSOFT 实证研究标准的 Repository Mining 标准，以及 Sampling、Inter-Rater Reliability、Ethics (Secondary Data)、Open Science 几个补充标准。可以直接当作投稿前的自查表。
- **git 数据的陷阱**：Bird 等人 2009，*The Promises and Perils of Mining Git*。
- **GitHub 数据的陷阱**：Kalliamvakou 等人 2014 列出九个陷阱和规避方法；2016 年的期刊扩展版增加到十三个，并分析了这些陷阱如何影响了已发表的研究。
- **缺陷数据的偏差**：Bird 等人 2009，*Fair and Balanced? Bias in Bug-Fix Datasets*（链接偏差）；Herzig 等人 2013，*It's Not a Bug, It's a Feature*（分类错误）。
- **抽样**：Baltes & Ralph 2022，系统讲解软件工程研究中的各种抽样方法和代表性问题。
- **数据分析中的警示信号**：Menzies & Shepperd 2019，列出软件分析论文的 12 种"坏味道"。
- **找数据集和工具**：dspinellis/awesome-msr 列表收录了常用的数据集（如 GHTorrent、Software Heritage Graph Dataset、Stack Exchange 数据转储）和挖掘工具（如 PyDriller、Perceval、Boa）。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^ralph2020empirical-e105]: SIGSOFT 仓库挖掘标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e105)
[^ralph2020empirical-e106]: SIGSOFT 仓库挖掘标准，适用范围。[证据](../../../../sources/notes/ralph2020empirical.md#e106)
[^ralph2020empirical-e107]: SIGSOFT 仓库挖掘标准，适用范围。[证据](../../../../sources/notes/ralph2020empirical.md#e107)
[^ralph2020empirical-e108]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e108)
[^ralph2020empirical-e109]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e109)
[^ralph2020empirical-e110]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e110)
[^ralph2020empirical-e111]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e111)
[^ralph2020empirical-e112]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e112)
[^ralph2020empirical-e113]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e113)
[^ralph2020empirical-e114]: SIGSOFT 仓库挖掘标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e114)
[^ralph2020empirical-e115]: SIGSOFT 仓库挖掘标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e115)
[^ralph2020empirical-e116]: SIGSOFT 仓库挖掘标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e116)
[^ralph2020empirical-e117]: SIGSOFT 仓库挖掘标准，优秀项。[证据](../../../../sources/notes/ralph2020empirical.md#e117)
[^ralph2020empirical-e118]: SIGSOFT 仓库挖掘标准，可接受的偏离。[证据](../../../../sources/notes/ralph2020empirical.md#e118)
[^ralph2020empirical-e119]: SIGSOFT 仓库挖掘标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e119)
[^ralph2020empirical-e120]: SIGSOFT 仓库挖掘标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e120)
[^ralph2020empirical-e121]: SIGSOFT 仓库挖掘标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e121)
[^ralph2020empirical-e122]: SIGSOFT 仓库挖掘标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e122)
[^ralph2020empirical-e123]: SIGSOFT 仓库挖掘标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e123)
[^ralph2020empirical-e124]: SIGSOFT 仓库挖掘标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e124)
[^ralph2020empirical-e125]: SIGSOFT General Standard，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e125)
[^ralph2020empirical-e127]: SIGSOFT Sampling 补充标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e127)
[^ralph2020empirical-e37]: SIGSOFT Sampling 补充标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e37)
[^ralph2020empirical-e128]: SIGSOFT 评分者间一致性补充标准。[证据](../../../../sources/notes/ralph2020empirical.md#e128)
[^ralph2020empirical-e129]: SIGSOFT 评分者间一致性补充标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e130]: SIGSOFT 评分者间一致性补充标准，Notes。[证据](../../../../sources/notes/ralph2020empirical.md#e130)
[^ralph2020empirical-e131]: SIGSOFT 评分者间一致性补充标准，优秀项。[证据](../../../../sources/notes/ralph2020empirical.md#e131)
[^ralph2020empirical-e132]: SIGSOFT 评分者间一致性补充标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e132)
[^ralph2020empirical-e133]: SIGSOFT 二手数据伦理补充标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e133)
[^ralph2020empirical-e134]: SIGSOFT 二手数据伦理补充标准，脚注 1。[证据](../../../../sources/notes/ralph2020empirical.md#e134)
[^ralph2020empirical-e135]: SIGSOFT 二手数据伦理补充标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e135)
[^ralph2020empirical-e136]: SIGSOFT 二手数据伦理补充标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e136)
[^ralph2020empirical-e137]: SIGSOFT 二手数据伦理补充标准，脚注 6。[证据](../../../../sources/notes/ralph2020empirical.md#e137)
[^ralph2020empirical-e138]: SIGSOFT 二手数据伦理补充标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e138)
[^bird2009promises-e1]: Bird 等人 2009（git），§1。[证据](../../../../sources/notes/bird2009promises.md#e1)
[^bird2009promises-e2]: Bird 等人 2009（git），Peril 4。[证据](../../../../sources/notes/bird2009promises.md#e2)
[^bird2009promises-e3]: Bird 等人 2009（git），Peril 5。[证据](../../../../sources/notes/bird2009promises.md#e3)
[^bird2009promises-e4]: Bird 等人 2009（git），Peril 6。[证据](../../../../sources/notes/bird2009promises.md#e4)
[^bird2009promises-e5]: Bird 等人 2009（git），Peril 7。[证据](../../../../sources/notes/bird2009promises.md#e5)
[^bird2009promises-e6]: Bird 等人 2009（git），§5。[证据](../../../../sources/notes/bird2009promises.md#e6)
[^bird2009promises-e7]: Bird 等人 2009（git），§5。[证据](../../../../sources/notes/bird2009promises.md#e7)
[^bird2009fair-e1]: Bird 等人 2009（缺陷数据偏差），摘要。[证据](../../../../sources/notes/bird2009fair.md#e1)
[^bird2009fair-e2]: Bird 等人 2009（缺陷数据偏差），§1。[证据](../../../../sources/notes/bird2009fair.md#e2)
[^bird2009fair-e3]: Bird 等人 2009（缺陷数据偏差），§1。[证据](../../../../sources/notes/bird2009fair.md#e3)
[^bird2009fair-e4]: Bird 等人 2009（缺陷数据偏差），§4。[证据](../../../../sources/notes/bird2009fair.md#e4)
[^bird2009fair-e5]: Bird 等人 2009（缺陷数据偏差），§4。[证据](../../../../sources/notes/bird2009fair.md#e5)
[^kalliamvakou2014promises-e1]: Kalliamvakou 等人 2014，摘要。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e1)
[^kalliamvakou2014promises-e2]: Kalliamvakou 等人 2014，Peril I。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e2)
[^kalliamvakou2014promises-e3]: Kalliamvakou 等人 2014，Peril II。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e3)
[^kalliamvakou2014promises-e4]: Kalliamvakou 等人 2014，Peril IV。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e4)
[^kalliamvakou2014promises-e5]: Kalliamvakou 等人 2014，Peril V。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e5)
[^kalliamvakou2014promises-e6]: Kalliamvakou 等人 2014，Peril VII。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e6)
[^kalliamvakou2014promises-e7]: Kalliamvakou 等人 2014，Peril VIII。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e7)
[^kalliamvakou2014promises-e8]: Kalliamvakou 等人 2014，Peril IX。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e8)
[^kalliamvakou2014promises-e9]: Kalliamvakou 等人 2014，§4.4.2。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e9)
[^kalliamvakou2014promises-e10]: Kalliamvakou 等人 2014，§6。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e10)
[^kalliamvakou2014promises-e11]: Kalliamvakou 等人 2014，§6。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e11)
[^kalliamvakou2014promises-e12]: Kalliamvakou 等人 2014，§2.1。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e12)
[^kalliamvakou2014promises-e13]: Kalliamvakou 等人 2014，§3、§5。[证据](../../../../sources/notes/kalliamvakou2014promises.md#e13)
[^kalliamvakou2016indepth-e1]: Kalliamvakou 等人 2016，Peril X。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e1)
[^kalliamvakou2016indepth-e2]: Kalliamvakou 等人 2016，Peril XI。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e2)
[^kalliamvakou2016indepth-e3]: Kalliamvakou 等人 2016，Peril XII。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e3)
[^kalliamvakou2016indepth-e4]: Kalliamvakou 等人 2016，Peril XII。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e4)
[^kalliamvakou2016indepth-e5]: Kalliamvakou 等人 2016，Peril XII。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e5)
[^kalliamvakou2016indepth-e6]: Kalliamvakou 等人 2016，Peril XIII。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e6)
[^kalliamvakou2016indepth-e7]: Kalliamvakou 等人 2016，§4.9。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e7)
[^kalliamvakou2016indepth-e8]: Kalliamvakou 等人 2016，§5.2。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e8)
[^kalliamvakou2016indepth-e9]: Kalliamvakou 等人 2016，§6。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e9)
[^kalliamvakou2016indepth-e10]: Kalliamvakou 等人 2016，§6。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e10)
[^kalliamvakou2016indepth-e11]: Kalliamvakou 等人 2016，§8。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e11)
[^kalliamvakou2016indepth-e12]: Kalliamvakou 等人 2016，§8。[证据](../../../../sources/notes/kalliamvakou2016indepth.md#e12)
[^herzig2013bug-e1]: Herzig 等人 2013，摘要。[证据](../../../../sources/notes/herzig2013bug.md#e1)
[^herzig2013bug-e2]: Herzig 等人 2013，§I。[证据](../../../../sources/notes/herzig2013bug.md#e2)
[^herzig2013bug-e3]: Herzig 等人 2013，图 1 与 §XI。[证据](../../../../sources/notes/herzig2013bug.md#e3)
[^herzig2013bug-e4]: Herzig 等人 2013，§XI。[证据](../../../../sources/notes/herzig2013bug.md#e4)
[^herzig2013bug-e5]: Herzig 等人 2013，§XII。[证据](../../../../sources/notes/herzig2013bug.md#e5)
[^baltes2022sampling-e2]: Baltes & Ralph 2022，§2.1.1。[证据](../../../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e5]: Baltes & Ralph 2022，§2.6。[证据](../../../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e12]: Baltes & Ralph 2022，§2.5。[证据](../../../../sources/notes/baltes2022sampling.md#e12)
[^baltes2022sampling-e13]: Baltes & Ralph 2022，§6.2。[证据](../../../../sources/notes/baltes2022sampling.md#e13)
[^baltes2022sampling-e14]: Baltes & Ralph 2022，§6.2。[证据](../../../../sources/notes/baltes2022sampling.md#e14)
[^baltes2022sampling-e15]: Baltes & Ralph 2022，§6.2。[证据](../../../../sources/notes/baltes2022sampling.md#e15)
[^baltes2022sampling-e16]: Baltes & Ralph 2022，§6.3。[证据](../../../../sources/notes/baltes2022sampling.md#e16)
[^menzies2019bad-e10]: Menzies & Shepperd 2019，§1。[证据](../../../../sources/notes/menzies2019bad.md#e10)
[^menzies2019bad-e2]: Menzies & Shepperd 2019，§4.6。[证据](../../../../sources/notes/menzies2019bad.md#e2)
[^menzies2019bad-e11]: Menzies & Shepperd 2019，§4.3。[证据](../../../../sources/notes/menzies2019bad.md#e11)
[^menzies2019bad-e12]: Menzies & Shepperd 2019，§4.4。[证据](../../../../sources/notes/menzies2019bad.md#e12)
[^ralph2020empirical-e66]: SIGSOFT General Standard，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e76]: SIGSOFT 开放科学补充标准，Principle。[证据](../../../../sources/notes/ralph2020empirical.md#e76)
[^ralph2020empirical-e78]: SIGSOFT 开放科学补充标准，Notes。[证据](../../../../sources/notes/ralph2020empirical.md#e78)
