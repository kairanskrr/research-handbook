# 观察描述

> 本页的道理适用于各学科，例子和具体做法以计算机为例。文中引用的软件工程评审标准（ACM SIGSOFT 实证研究标准）、医学和兽医的报告规范、美国环境保护署的规划指南等，只代表各自领域的做法，都标明了出处，不是所有研究的通则。

你想弄清的是"这个现象到底是什么样的"：它存不存在、有哪些种类、有多常见、和别的东西有什么不同。你不打算做出一个新工具，也还没打算解释它为什么会这样。这时你走的就是**观察描述**这一套路。

研究套路的意思见[核心术语](../00_start-here/key-concepts.md#研究套路)，它和解释因果、测量、综合的分界见[研究套路](README.md#怎样选出主要套路)里"怎样选出主要套路"一节；怎样从几种套路里选出自己的，见[选定研究套路和方法](../02_do-the-project/02_choose-method.md)。

---

## 1. 这类研究产生什么知识

观察描述回答的是关于"世界现在是什么样"的问题。按问法，大致分五种[^easterbrook2008selecting-e44][^easterbrook2008selecting-e46][^easterbrook2008selecting-e47]：

| 问题类型 | 问法 | 例子：大模型与智能合约安全 | 主张长什么样 |
|---|---|---|---|
| 存在 | X 存在吗？ | 大模型生成的合约里，会不会出现人写的代码里很少见的漏洞写法？ | "存在一类……的漏洞写法，我们找到了 N 个真实例子" |
| 描述与分类 | X 是什么样的？可以分成哪几类？ | 生成合约里的漏洞可以分成哪几类？ | "可归为五类，其中两类此前没有被描述过" |
| 频率与分布 | X 多常见？在哪里多、哪里少？ | 生成合约里有重入漏洞的比例是多少？ | "大模型生成的合约中，四成有重入漏洞" |
| 描述比较 | X 和 Y 有什么不同？ | 生成合约和人写合约的漏洞分布有什么不同？ | "生成合约的重入漏洞比例明显高于人写合约" |
| 描述过程 | X 通常是怎样发生的？ | 开发者实际怎样用大模型写合约、怎样检查生成的代码？ | "开发者通常先……再……，很少……" |

表中的例子和主张是本项目举的例子。最后一种常用访谈、观察来回答，结果是一段过程或一组类别，不一定是数字 `[本项目分析]`。

**它为什么值得做。** 不知道某件事通常有多常见，就没法判断眼前的情况是正常还是异常[^easterbrook2008selecting-e34]。"怎样做得更好"这类设计问题，本身就预设了相关的知识问题已经回答过，我们对要解决的问题已经了解得足够多[^easterbrook2008selecting-e48]。一个领域还没有确证的结论时，如实报告实际现象的"观察"能指导实践，也为以后得出确证结论打基础[^shaw2002makes-e6]。

**它不产生什么。** 它不回答"为什么"，也不回答"哪个更好"。把相关当成因果是常见错误，而证明因果比证明两个变量相关难得多[^easterbrook2008selecting-e36]。想说"某个因素导致了漏洞"，见[解释因果](explain_causality.md)；想说"工具 A 比 B 好"，见[比较评估](compare_evaluate.md)；想说"这个评测集测得不准"，见[测量](measure.md)。

**写下来：** 用上表的五种问法，各写一个你方向里的问题。挑出你最想知道答案的一个，写出它的答案可能长什么样。

## 2. 什么样的证据才够

拿"大模型生成的合约中，四成有重入漏洞"这句主张来说，审稿人至少会追问下面这些。表里和本节引的标准，多数来自 ACM SIGSOFT 实证研究标准，也就是美国计算机协会软件工程分会制定的评审标准，适用于软件工程；其他领域的出处单独标明。

| 审稿人会问 | 你要拿出的东西 |
|---|---|
| "大模型生成的合约"指什么？ | 哪些模型、哪个版本、什么提示、什么时间生成的。研究开始时就要说清你想描述、想推广到的目标总体[^wagner2020challenges-e3][^baltes2022sampling-e11] |
| 样本怎么来的？能代表谁？ | 抽样的目的和步骤。代表性是样本和总体之间的关系，不是某种抽样技术自带的性质[^baltes2022sampling-e3]；抽样框本身有偏差时，样本再大也补不回来[^baltes2022sampling-e5] |
| "有重入漏洞"是怎么判定的？ | 判定规则、所用工具或人工标注的过程。先把术语的确切含义定义清楚，并确认能可靠地认出它[^easterbrook2008selecting-e43] |
| 判定准不准？ | 软件工程的仓库挖掘标准要求：用过已验证的度量，或者自己检验过构念效度（测的是不是你想测的东西）[^ralph2020empirical-e112]；人工标注时用多名标注者，报告人数和标注者间一致性[^ralph2020empirical-e111] |
| 四成是多确定的数？ | 美国环境保护署的数据规划指南指出：概率抽样（按已知概率随机抽取）能让你对总体下定量结论，并恰当地表达不确定性；凭判断挑出来的样本做不到这一点[^epa2006dqo-e13][^epa2006dqo-e14] |
| 所以呢？跟什么比？ | 一个参照：人写合约的比例、旧版本模型的比例。没有参照，读者不知道四成算多算少 `[本项目分析]` |

**要达到的标准**，可以归成四条 `[本项目分析]`：

1. **对象定义清楚。** 读者能照你的定义认出同一种东西。只问"多普遍"，往往已经预设了你知道研究对象是什么、能可靠地认出它[^easterbrook2008selecting-e43]。用 GitHub 星标数代表"流行度"这种未经验证的单一指标，在软件工程的仓库挖掘标准里属于反面模式[^ralph2020empirical-e119]。
2. **样本和结论的范围对得上。** 写明抽样是为了代表总体，还是为了别的目标（如找到特殊案例），并说明你的做法对这个目标是合理的[^ralph2020empirical-e36]。从一个有偏的抽样框里随机抽，然后声称样本有代表性，是反面模式[^ralph2020empirical-e37]。
3. **判断有人复核。** 判断越可能有争议，越需要多名评分者[^ralph2020empirical-e128]。"这算不算重入漏洞"常常就有争议 `[本项目分析]`。
4. **过程能被重复。** 写清在哪里、什么时候、怎样收集了什么数据[^ralph2020empirical-e125]。

**别用错标准。** 没有适用于所有研究的质量标准，每项研究都要按适合它的方法的标准来评价[^ralph2020empirical-e24]。代表性本来就不是研究目标时，抱怨它不够有代表性是不成立的批评[^ralph2020empirical-e39]。例如案例研究的目的是深入理解一个现场，不是从样本推广到总体[^baltes2022sampling-e10]。反过来，软件工程的问卷调查标准也把"结果不出所料"列为不成立的批评[^ralph2020empirical-e249]。

> **不同的看法：只有描述，够不够发表？**
>
> - **够，但要有意思。** Shaw 对软件工程研究结果的分类里，如实报告实际现象的"观察"是一类结果，评价标准是有没有意思[^shaw2002makes-e5]；她引 Brooks 的看法说，观察可以是好的初步结果[^shaw2002makes-e4]。
> - **不够，要连上理论。** 软件工程的仓库挖掘标准把"只做定量描述，不检验、不建立、不扩展理论"列为反面模式[^ralph2020empirical-e122]。Easterbrook 等人也指出，很多实证研究没有把数据和背后的理论联系起来，结果难以解读，研究之间也没法比较[^easterbrook2008selecting-e54]。
>
> 实际操作 `[本项目分析]`：投计算机的实证类会议或期刊时，除了"是什么样"，至少再写一层"这说明了什么"：它支持还是挑战了哪种已有说法，对谁的做法有什么含义。只有一堆百分比的论文，最容易被问"所以呢"。

**写下来：** 把你的描述性主张写成一句话，然后照上表逐行写出你的回答。答不上的行，就是你设计时要补的地方。

## 3. 常用的研究方法

| 方法 | 什么时候用 | 要特别注意 |
|---|---|---|
| [仓库挖掘](../07_fields/computer-science/practices/repository_mining.md) | 想知道大量代码、提交、缺陷报告里的分布。GitHub 这类平台的数据可以直接用来报告项目属性[^kalliamvakou2014promises-e11] | 用它对抽象概念下结论要格外谨慎[^kalliamvakou2014promises-e11]；分析单元要先定义好[^ralph2020empirical-e108] |
| [问卷调查](../06_methods/questionnaire_survey.md) | 想知道一个人群里某种做法、工具、看法的分布。调查研究通常用来回答基础比率问题[^easterbrook2008selecting-e49]；描述性调查关心分布是什么，不关心它为什么存在[^wagner2020challenges-e1] | 人们说自己怎么做，可能和实际做的毫无关系[^easterbrook2008selecting-e52]；可以用工作仓库等数据交叉核对[^molleri2020empirically-e7] |
| [访谈研究](../06_methods/interview_study.md)、[扎根理论](../06_methods/grounded_theory.md) | 还不知道现象有哪些种类、该问什么。研究早期适合用能提供丰富定性数据的方法，帮助建立初步理论[^easterbrook2008selecting-e45] | 结果是类别和过程，不是比例；不要用它回答"有多少人" `[本项目分析]` |
| [案例研究](../06_methods/case_study.md) | 想深入描述少数真实场景里实际发生了什么 | 用代表性换深度[^easterbrook2008selecting-e19]，不要假装一两个现场有代表性[^baltes2022sampling-e10] |
| [纵向研究](../06_methods/longitudinal_study.md) | 想描述现象随时间怎样变化[^ralph2020empirical-e257] | 只想知道"现在用得多广"，一次横断面的"快照"就够；要看变化，才需要跟踪同一批对象[^easterbrook2008selecting-e53] |
| [数据科学](../06_methods/data_science.md) | 对已有数据集做探索性分析 | 只看一个时间点的分析，SIGSOFT 标准建议参考探索性数据科学标准[^ralph2020empirical-e258] |
| [行动研究](../06_methods/action_research.md) | 想看一项改变引入真实组织后，里面的人怎么反应。行动研究的意义就在于引入改变，并观察参与者的反应[^ralph2020empirical-e342] | 研究者要在真实环境里实施干预；只观察、不干预的，按案例研究的标准做[^ralph2020empirical-e331] |
| [空间分析研究](../07_fields/geography/practices/spatial_analysis.md)（地理学的实践） | 想知道一个现象在空间上怎样分布、是否成团。空间自相关指观测值彼此有多相似，和它们位置有多近有多大关系[^rey2023geographic-e11] | 人常把随机看成规律[^rey2023geographic-e13]，"是否成团"要靠检验：p 值足够小，才能拒绝"这张地图的格局是随机的"[^rey2023geographic-e15]；区域数据的结论会随尺度和分区方式改变[^kwan2018limits-e2] |
| [综述](../06_methods/review_study.md) | 文献里可能已经有答案 | 探索性问题仍然要问，但可以用文献调研而不是新的实证研究来回答[^easterbrook2008selecting-e41]；见[综合](synthesize.md) |

表中没有脚注的做法和注意事项是本项目的归纳 `[本项目分析]`。其他学科的对应做法，见跨学科方法[野外观测研究](../06_methods/field_study.md)（原多用于地球与环境科学）、[观察性流行病学](../06_methods/observational_epidemiology.md)（原多用于健康科学）中的横断面研究，以及语言与文学的实践[语言记录](../07_fields/languages-literature/practices/language_documentation.md)。

**行动研究为什么放在这里。** 软件工程的评审标准把行动研究定义为研究一项干预（例如引入某种方法或工具）如何影响真实环境的实证研究[^ralph2020empirical-e330]。它服务两个套路：在真实组织里引入一项改进，属于[构建改进](build_improve.md)；看真实环境里的人怎么反应，属于观察描述 `[本项目分析]`。同一份标准也写明，行动研究不是实验[^ralph2020empirical-e343]，所以本手册不把它归入[解释因果](explain_causality.md) `[本项目分析]`。

**空间分析为什么放在这里** `[本项目分析]`：它的一部分工作是描述现象在空间上怎样分布、检验是否成团，属于观察描述；研究环境怎样影响个人的那部分，属于[解释因果](explain_causality.md)。

**常见的组合** `[本项目分析]`：先用访谈或人工细读少量样本，归纳出类别；再用仓库挖掘或问卷，统计每一类有多常见。例如先人工读 50 份生成合约归纳漏洞类型，再用工具在几千份合约上统计分布，最后抽样人工复核工具的判定。

## 4. 它怎样影响整个项目

观察描述不只决定你怎么设计，它从读文献到写论文都在起作用。

**读文献时** `[本项目分析]`：先查有没有人描述过同一个现象，答案可能已经在文献里[^easterbrook2008selecting-e41]。特别留意别人用的定义和分类：把关键术语定义清楚，不同研究的结果才能互相比较[^easterbrook2008selecting-e55]。能沿用别人的定义，就别自己另起一套。找文献的做法见[进入领域、探索文献](../01_find-a-problem/01_enter-a-field.md)。

**选题时** `[本项目分析]`：描述性问题在一个方向刚起步时最有价值。大模型写合约还是新现象，"它通常会出什么问题"本身就值得回答。如果你原本想做"构建改进"，却发现没人知道问题有多普遍，先做一项描述研究常常更扎实（理由见第 1 节[^easterbrook2008selecting-e48]）。收敛题目时，用"所以呢"检验一下：数字算出来以后，谁会因此改变做法？见[收敛成项目](../01_find-a-problem/05_converge.md)。

**设计时**：先写下目标总体和分析单元。分析单元决定该怎样抽样：问题是关于公司的，却按开发者抽样，同一公司的几个人会让这家公司被过度代表[^easterbrook2008selecting-e50]。换到本例，问题是关于"合约"还是"项目"，统计方式就不同 `[本项目分析]`。写清抽样目的[^baltes2022sampling-e6]，提前定好判定规则。语料可能很快过时，保持稳定和保持最新之间本来就有矛盾[^baltes2022sampling-e15]；大模型版本更新快，要记下每份数据对应的模型版本和生成时间 `[本项目分析]`。怎样判断结论能推广到哪里，见[效度与局限](../02_do-the-project/04_validity-and-limits.md)。

**执行时**：回复率低会增加偏差风险，例如可能只有对某样东西不满的人回答了问卷[^easterbrook2008selecting-e51]。抽样框可能有偏时，可以换一个抽样框把研究重复一遍，例如从 GitHub 换到 SourceForge[^baltes2022sampling-e13]。人工标注先拿一小批试标，算一致性，改规则，再铺开 `[本项目分析]`。

**分析时**：混杂指同时影响两个变量、让它们看起来有关系的第三个因素。流行病学的方法文献指出，分析只为描述关联时，不需要调整混杂；目标是因果时才需要[^hernan2018cword-e7]。但别把描述悄悄说成因果：问卷数据常被当成实验数据，看到并不存在的因果关系[^torchiano2017lessons-e2]。怎样解读结果，见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md)。

**写作时**：主张里写明范围，例如"在某三个模型、某种提示下"。很少有软件工程研究真能声称样本有代表性，夸大代表性既没必要也不科学[^baltes2022sampling-e8]。不要在局限一节承认抽样偏差，到了结论又写得像普遍成立[^baltes2022sampling-e9][^ralph2020empirical-e66]。论文怎样讲清"这说明了什么"，见[讲清故事，写成论文](../03_write-and-publish/01_story-and-paper.md)。

## 5. 哪些学科常用

只列本文资料能支持的；其他学科是否常用，本文资料未涉及。

- **计算机（尤其软件工程）**：软件工程的问卷调查标准把"详细描述一个现象或人群的性质"列为问卷的一种用途[^ralph2020empirical-e234]。仓库挖掘的发现本身也常是描述性的，例如 GitHub 上多数项目是个人的、不活跃的[^kalliamvakou2014promises-e1]，67% 的项目只有一名提交者[^kalliamvakou2014promises-e5]。见[计算机学科概况](../07_fields/computer-science/README.md)。
- **医学与公共卫生**：按医学观察性研究报告规范 STROBE 的解释文件，横断面研究在同一时间点调查一个样本，常用来看暴露、危险因素或疾病的患病率[^vandenbroucke2007strobe-e3]。见[健康科学](../07_fields/health-sciences/README.md)、[临床医学](../07_fields/clinical-medicine/README.md)。
- **兽医学**：按兽医观察性研究报告规范 STROBE-Vet，观察性研究可以用来估计某种状况的患病率或发病率，研究它在时间和空间上的分布[^sargeant2016strobevet-e2]。见[动物科学与兽医学](../07_fields/animal-veterinary-science/README.md)。
- **环境工程与地球科学**：美国环境保护署的规划指南把"估计"（例如确定某种污染物的平均浓度）列为数据的一种用途[^epa2006dqo-e2]。见[环境工程](../07_fields/environmental-engineering/README.md)、[地球与环境科学](../07_fields/earth-environmental-sciences/README.md)。
- **政治学**：政治学的案例研究方法文献指出，推断是描述性而非因果性时，案例研究通常更有用[^gerring2004case-e7]。见[政治学](../07_fields/political-science/README.md)。
- **语言学**：语言学讨论里，"描写"一种语言和"记录"语言被当作两类工作；Himmelmann 曾要求把两者分开，但也有学者认为，有些对这一要求的解读走得太远[^riesberg2018adequacy-e2]。见[语言与文学](../07_fields/languages-literature/README.md)。

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 没定义清楚就开始数 | 你数的东西别人认不出，结果也没法和别的研究比[^easterbrook2008selecting-e43][^easterbrook2008selecting-e55] |
| 用一个现成指标代替抽象概念 | 例如用星标数代表流行度，是未经验证的单一指标[^ralph2020empirical-e119] |
| 从有偏的抽样框里随机抽，就说有代表性 | 抽样框的偏差不会因为随机或样本大而消失[^ralph2020empirical-e37][^baltes2022sampling-e5] |
| 把方便样本（手边容易找到的样本）的结果当成普遍比例 | 例如一项用滚雪球抽样（让受访者再介绍受访者）调查野外科研人员经历的研究，作者自己也说无法据此判断这些经历有多普遍[^clancy2014survey-e7] |
| 问卷问"你怎么做"，就当成实际怎么做 | 说的和做的可能毫无关系[^easterbrook2008selecting-e52] |
| 争议大的判断只有一个人标 | 判断越有争议，越需要多名评分者[^ralph2020empirical-e128] |
| 只报百分比，不说明意味着什么 | 没有参照就分不清正常还是异常[^easterbrook2008selecting-e34]；软件工程的仓库挖掘标准把纯定量描述列为反面模式[^ralph2020empirical-e122] |
| 在描述数据里"看出"因果 | 相关不等于因果[^easterbrook2008selecting-e36][^torchiano2017lessons-e2] |
| 局限里承认偏差，结论里当没这回事 | 夸大结论是 SIGSOFT 列出的反面模式[^ralph2020empirical-e66] |

## 7. 延伸阅读

- **Easterbrook 等人 2008，*Selecting Empirical Methods for Software Engineering Research*。** 第 2 节把研究问题分成存在、描述分类、基础比率、关系、因果等类型，并讲每种该用什么方法。本篇的分类主要来自这里。[摘录](../../sources/notes/easterbrook2008selecting.md)
- **Baltes & Ralph 2022，*Sampling in Software Engineering Research*。** 讲清代表性、抽样框、方便抽样，最后有一组写作建议。做任何"有多普遍"的研究前都值得读。[摘录](../../sources/notes/baltes2022sampling.md)
- **ACM SIGSOFT 实证研究标准（Ralph 等人 2020）。** 仓库挖掘、问卷、纵向研究、抽样、评分者一致性各有一份清单，列出必须做到的、加分的、反面模式和不成立的批评。[摘录](../../sources/notes/ralph2020empirical.md)
- **Wagner 等人 2020，*Challenges in Survey Research*。** 描述性调查和理论、抽样的关系。[摘录](../../sources/notes/wagner2020challenges.md)
- **Kalliamvakou 等人 2014，*The Promises and Perils of Mining GitHub*。** 列出用 GitHub 数据做研究时的一组陷阱。[摘录](../../sources/notes/kalliamvakou2014promises.md)
- **STROBE 解释与说明（Vandenbroucke 等人 2007）。** 医学观察性研究的报告规范，横断面研究部分可作参照。[摘录](../../sources/notes/vandenbroucke2007strobe.md)

[^easterbrook2008selecting-e43]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e43)
[^easterbrook2008selecting-e44]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e44)
[^easterbrook2008selecting-e45]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e45)
[^easterbrook2008selecting-e41]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e41)
[^easterbrook2008selecting-e34]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e34)
[^easterbrook2008selecting-e46]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e46)
[^easterbrook2008selecting-e47]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e47)
[^easterbrook2008selecting-e36]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e48]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e48)
[^easterbrook2008selecting-e49]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e49)
[^easterbrook2008selecting-e50]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e50)
[^easterbrook2008selecting-e51]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e51)
[^easterbrook2008selecting-e52]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e52)
[^easterbrook2008selecting-e53]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e53)
[^easterbrook2008selecting-e19]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e19)
[^easterbrook2008selecting-e54]: Easterbrook 等人 2008，§4.0。[证据](../../sources/notes/easterbrook2008selecting.md#e54)
[^easterbrook2008selecting-e55]: Easterbrook 等人 2008，§4.0。[证据](../../sources/notes/easterbrook2008selecting.md#e55)
[^shaw2002makes-e4]: Shaw 2002，§2.2。[证据](../../sources/notes/shaw2002makes.md#e4)
[^shaw2002makes-e5]: Shaw 2002，§1.2.3。[证据](../../sources/notes/shaw2002makes.md#e5)
[^shaw2002makes-e6]: Shaw 2002，§1.2.3。[证据](../../sources/notes/shaw2002makes.md#e6)
[^ralph2020empirical-e24]: ACM SIGSOFT 实证研究标准，General Standard，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e36]: ACM SIGSOFT 实证研究标准，Sampling Supplement，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e36)
[^ralph2020empirical-e37]: ACM SIGSOFT 实证研究标准，Sampling Supplement，Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e37)
[^ralph2020empirical-e39]: ACM SIGSOFT 实证研究标准，Sampling Supplement，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e39)
[^ralph2020empirical-e66]: ACM SIGSOFT 实证研究标准，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e108]: ACM SIGSOFT 实证研究标准，Repository Mining 标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e108)
[^ralph2020empirical-e111]: ACM SIGSOFT 实证研究标准，Repository Mining 标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e111)
[^ralph2020empirical-e112]: ACM SIGSOFT 实证研究标准，Repository Mining 标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e112)
[^ralph2020empirical-e119]: ACM SIGSOFT 实证研究标准，Repository Mining 标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e119)
[^ralph2020empirical-e122]: ACM SIGSOFT 实证研究标准，Repository Mining 标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e122)
[^ralph2020empirical-e125]: ACM SIGSOFT 实证研究标准，General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e125)
[^ralph2020empirical-e128]: ACM SIGSOFT 实证研究标准，Inter-Rater Reliability and Agreement 补充标准。[证据](../../sources/notes/ralph2020empirical.md#e128)
[^ralph2020empirical-e234]: ACM SIGSOFT 实证研究标准，Questionnaire Surveys 标准，Variations。[证据](../../sources/notes/ralph2020empirical.md#e234)
[^ralph2020empirical-e249]: ACM SIGSOFT 实证研究标准，Questionnaire Surveys 标准，Invalid Criticism。[证据](../../sources/notes/ralph2020empirical.md#e249)
[^ralph2020empirical-e257]: ACM SIGSOFT 实证研究标准，Longitudinal 标准，定义与 Application。[证据](../../sources/notes/ralph2020empirical.md#e257)
[^ralph2020empirical-e258]: ACM SIGSOFT 实证研究标准，Longitudinal 标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e258)
[^baltes2022sampling-e3]: Baltes & Ralph 2022，§2.6。[证据](../../sources/notes/baltes2022sampling.md#e3)
[^baltes2022sampling-e5]: Baltes & Ralph 2022，§2.6。[证据](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e6]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e6)
[^baltes2022sampling-e8]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e8)
[^baltes2022sampling-e9]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e9)
[^baltes2022sampling-e10]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e10)
[^baltes2022sampling-e11]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e11)
[^baltes2022sampling-e13]: Baltes & Ralph 2022，§6.2。[证据](../../sources/notes/baltes2022sampling.md#e13)
[^baltes2022sampling-e15]: Baltes & Ralph 2022，§6.2。[证据](../../sources/notes/baltes2022sampling.md#e15)
[^wagner2020challenges-e1]: Wagner 等人 2020，§2。[证据](../../sources/notes/wagner2020challenges.md#e1)
[^wagner2020challenges-e3]: Wagner 等人 2020，§3。[证据](../../sources/notes/wagner2020challenges.md#e3)
[^kalliamvakou2014promises-e1]: Kalliamvakou 等人 2014，摘要。[证据](../../sources/notes/kalliamvakou2014promises.md#e1)
[^kalliamvakou2014promises-e5]: Kalliamvakou 等人 2014，§4.3。[证据](../../sources/notes/kalliamvakou2014promises.md#e5)
[^kalliamvakou2014promises-e11]: Kalliamvakou 等人 2014，§6。[证据](../../sources/notes/kalliamvakou2014promises.md#e11)
[^molleri2020empirically-e7]: Molléri 等人 2020，§4.2.1。[证据](../../sources/notes/molleri2020empirically.md#e7)
[^torchiano2017lessons-e2]: Torchiano 等人 2017，§III-A-1。[证据](../../sources/notes/torchiano2017lessons.md#e2)
[^hernan2018cword-e7]: Hernán 2018，Better Confounding Adjustment。[证据](../../sources/notes/hernan2018cword.md#e7)
[^epa2006dqo-e2]: 美国环境保护署 2006，Introduction。[证据](../../sources/notes/epa2006dqo.md#e2)
[^epa2006dqo-e13]: 美国环境保护署 2006，Chapter 7。[证据](../../sources/notes/epa2006dqo.md#e13)
[^epa2006dqo-e14]: 美国环境保护署 2006，Chapter 7。[证据](../../sources/notes/epa2006dqo.md#e14)
[^clancy2014survey-e7]: Clancy 等 2014，Discussion。[证据](../../sources/notes/clancy2014survey.md#e7)
[^vandenbroucke2007strobe-e3]: Vandenbroucke 等人 2007，Box 1。[证据](../../sources/notes/vandenbroucke2007strobe.md#e3)
[^sargeant2016strobevet-e2]: Sargeant 等人 2016，Introduction。[证据](../../sources/notes/sargeant2016strobevet.md#e2)
[^gerring2004case-e7]: Gerring 2004，Conclusion，第 352 页。[证据](../../sources/notes/gerring2004case.md#e7)
[^ralph2020empirical-e330]: SIGSOFT 行动研究标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e330)
[^ralph2020empirical-e331]: SIGSOFT 行动研究标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e331)
[^ralph2020empirical-e342]: SIGSOFT 行动研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e342)
[^ralph2020empirical-e343]: SIGSOFT 行动研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e343)
[^riesberg2018adequacy-e2]: Riesberg 2018，第 152 页。[证据](../../sources/notes/riesberg2018adequacy.md#e2)
[^rey2023geographic-e11]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../sources/notes/rey2023geographic.md#e11)
[^rey2023geographic-e13]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../sources/notes/rey2023geographic.md#e13)
[^rey2023geographic-e15]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../sources/notes/rey2023geographic.md#e15)
[^kwan2018limits-e2]: Kwan 2018，第 1486 页。[证据](../../sources/notes/kwan2018limits.md#e2)
