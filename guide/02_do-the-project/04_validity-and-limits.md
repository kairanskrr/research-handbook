# 效度与局限：设计阶段就想清楚

> 本章的道理适用于各学科，例子和具体做法以计算机为例。

> **这一章必须做的事**
>
> 1. **先假设结论错了，列出至少八条可能的原因。** 列不出来，请一个同学扮演最挑剔的审稿人来列（[第 1 节](#1-先假设结论错了列出所有可能的原因)）。
> 2. **给每条原因归类，盯住你的套路最要紧的那一类。** 那一类如果列得最少，回去补（[第 2 节](#2-用四个问题给威胁归类)）。
> 3. **说清指标为什么能代表概念，结论能推到哪里。** 每个关键概念写一句定义，再写一句"为什么这个指标能代表它"；然后写"我的结论适用于____"和"它不一定适用于____"（[第 3 节](#3-构念效度你测的是你想说的东西吗)、[第 5 节](#5-外部效度结论能推广到哪里)）。
> 4. **看数据之前写好一页分析计划。** 比较什么、用什么指标、多大的差异算有意义；需要人判断的地方，写好由谁判、按什么规则判（[第 6 节](#6-结论效度与可靠性数据够不够换人做还一样吗)）。
> 5. **给每个威胁定一个处理办法。** "高"威胁要消除或减轻，做不到就把主张改小（[第 7 节](#7-给每个威胁定一个处理办法)）。
> 6. **现在就写局限草稿。** 让核心主张和局限一致，把"无论结果如何都报告"和"记录每一次偏离"写进计划（[第 8 节](#8-现在就写下局限定下诚实报告的规矩)）。
>
> **做到了就往下走：** 每个"高"威胁都有了处理办法，局限草稿写好了，导师或同学看过威胁清单，没有指出漏掉的严重威胁。下一步：[最小可跑版本](05_pilot-and-derisk.md)。

## 你现在在哪里

你已经有了证据清单（见[从研究问题到证据清单](01_question-to-evidence.md)），选好了研究套路和研究方法（见[选方法](02_choose-method.md)），也排好了计划（见[形成研究计划](03_research-plan.md)）。空的结果表行和列都想好了，就等着填数字。

接着贯穿全书的项目：主张是"现有大模型漏洞检测的评测结果被数据泄露高估了"。证据清单里的问题二，要比较几个模型在泄露样本和未泄露样本上的检出率；你预测泄露样本要高 10 个百分点以上。

看起来可以动手了。但先停一下：**如果实验做完，结果和你预想的一样，审稿人会用哪些理由说"这不能证明你的结论"？**

## 这一阶段要解决什么

在跑任何实验、发任何问卷之前，把"我的结论可能错在哪"想清楚，并且在设计里先堵上能堵的口子。具体来说，是回答下面几个问题：

1. 我测的东西，真是我想说的那个东西吗？
2. 如果看到了差异，真是我关心的那个因素造成的吗？
3. 结论能推广到多大范围？
4. 数据和分析，真的足以支撑这个结论吗？换个人来做，会得到一样的结果吗？
5. 堵不上的口子，我打算怎样诚实地写出来？

**效度**指结论可信的程度。软件工程的案例研究指南这样定义：结果在多大程度上是真的，没有被研究者自己的看法带偏[^runeson2009guidelines-e1]。本章讲的是各种研究都要想的通用框架。具体某种研究套路要做的事，比如选基线、做消融实验（把方法的组成部分逐个去掉，看效果怎么变）、留一份只在最后用的检验数据、重复运行和统计检验，放在各套路页和方法页里，本章只在需要时链接过去，不再重复。

---

## 1. 先假设结论错了，列出所有可能的原因

**做法：** 想象一年后，有人发了一篇论文，指出你的结论站不住。他会说什么？把你能想到的理由全部列出来，越多越好，先不分类、不评价。

为什么要这样做？做研究的第一原则是不要骗自己，而你自己恰恰是最容易被骗的人[^feynman1974cargo-e7]。等结果出来，你会本能地想相信它。现在结果还没出来，是你最能冷静挑毛病的时候。

为什么要**现在**做？软件工程的案例研究指南提醒：到分析阶段才考虑效度就太晚了，效度要在之前的每个阶段都考虑[^runeson2009guidelines-e2]。实验做完再发现"测错了东西"或"没控制住某个因素"，往往只能重做。

也别指望找到一个完美的设计。一本软件工程研究方法手册说得很直接：所有研究设计都有缺陷[^easterbrook2008selecting-e69]。你要做的是知道缺陷在哪，能补的补上，补不上的说清楚。

假设结果和预测一样：泄露样本的检出率高出一截。你可能会列出：

- 泄露的合约本来就更老、更短、漏洞更典型，检出率高也许不是因为模型"见过"它们；
- "泄露"按完全相同算，改了变量名的复制被算成"未泄露"，两组混在了一起；
- "检出"是怎么判定的？大模型说"可能有重入风险"算不算检出？
- 有的模型用了新版，有的用了旧版，训练语料也不一样；
- 只用了一个评测集、一种合约语言；
- 大模型每次输出不一样，只跑一次，差距可能是运气；
- 判定"检出"的是你自己，你心里希望泄露样本那组更高。

**写下来：** 给你的核心主张列出至少八条"它可能错的理由"。如果列不出来，找一个同学扮演最挑剔的审稿人，让他来列。

## 2. 用四个问题给威胁归类

列出来的理由很杂。按它们威胁结论的方式分一下类，你就知道每一类该用什么办法对付。

**效度威胁**指可能让你的结论不成立的因素。分类的框架不止一种。心理学测量文献引用的是 Shadish 等人的四类：构念效度、内部效度、外部效度、统计结论效度[^flake2020measurement-e16]。软件工程的研究方法手册用的四类里，前三类相同，第四类换成可靠性[^easterbrook2008selecting-e68]。本章把两套合在一起用，对应开头的四个问题（第 4 问包含最后两类）：

| 类型 | 用大白话问 | 例子里对应的威胁 |
|---|---|---|
| **构念效度** | 我测的东西，真是我想说的那个概念吗？[^easterbrook2008selecting-e66] | "泄露"的定义漏掉了改名的复制；"检出"的判定标准含糊 |
| **内部效度** | 看到的差异，真是我关心的那个因素造成的吗？[^easterbrook2008selecting-e65] | 泄露样本本来就更简单 |
| **外部效度** | 结论能推广到我研究的对象之外吗？[^easterbrook2008selecting-e67] | 只用了一个评测集、一种合约语言 |
| **结论效度** | 从数据和分析得出的结论本身对吗？[^flake2020measurement-e16] | 只跑一次，差距可能是随机波动 |
| **可靠性** | 换一个研究者重做，结果还一样吗？[^easterbrook2008selecting-e68] | 判定"检出"的人自己希望看到差距 |

表里的"结论效度"，在 Shadish 等人的框架里叫"统计结论效度"，问的是统计分析得出的结论是否正确[^flake2020measurement-e16]。不做统计的研究也有同样的问题：你的证据到底够不够得出那句话。

**不是每一类都同样重要。** 软件工程的实证研究标准写明：没有通用的质量标准，每项研究要按适合它的方法的标准来评价；比如对一项没有因果关系的研究，就不该要求内部效度[^ralph2020empirical-e24]。拿某类方法本身固有的局限去批评它，比如批评案例研究推广性有限，这个标准也认为不成立[^ralph2020empirical-e25]。

所以先看你走的是哪种研究套路，再决定把力气花在哪：

| 研究套路 | 最要紧的通常是 | 详见 |
|---|---|---|
| 观察描述 | 外部效度（样本能代表谁）、构念效度（分类和判定准不准） | [观察描述](../05_research-strategies/observe_describe.md) |
| 测量 | 构念效度 | [测量](../05_research-strategies/measure.md) |
| 比较评估 | 构念效度（指标）、结论效度（差异是不是真的）、比较是否公平 | [比较评估](../05_research-strategies/compare_evaluate.md) |
| 解释因果 | 内部效度 | [解释因果](../05_research-strategies/explain_causality.md) |
| 构建改进 | 结论效度、外部效度（换个数据还灵不灵） | [构建改进](../05_research-strategies/build_improve.md) |
| 综合 | 检索和筛选会不会漏、会不会偏 | [综合](../05_research-strategies/synthesize.md) |
| 证明 | 假设和定义是否贴近现实 | [证明](../05_research-strategies/prove.md) |

**定性研究怎么办？** 访谈、民族志这类研究，有一套不同的说法，见本章末"不同的看法"。

**写下来：** 把第 1 节列的每条理由，标上它属于哪一类。再看看你的套路最要紧的那一类，是不是列得最少？如果是，回去补。

## 3. 构念效度：你测的是你想说的东西吗？

你的主张里有一些抽象的概念，比如"检出率""漏洞检测能力""代码质量"。研究里要说的这种抽象概念叫**构念**。构念没法直接拿尺子量，你必须选一个具体能算出来的东西代替它。代替得不好，后面做得再仔细也没用。

**做法：**

1. **先用一两句话定义构念。** 一开始没把构念定义清楚，后面每个测量决定都会很难做，也会留下有意无意钻空子的机会[^flake2020measurement-e7]。比如"检出"：是要求模型指出具体的函数和行号，还是说出漏洞类型就算？
2. **写出你用的指标，以及它为什么能代表这个概念。** 编程语言领域的评估清单要求：间接指标只有在明确说明理由时，才能代替直接指标[^blackburn2018sigplan-e13]。机器学习的报告清单也提醒，被预测的结果通常只是一个看不见的理论概念的替代品[^kapoor2024reforms-e6]。
3. **优先用别人验证过的指标；自己编的，至少说明为什么不用已有的。** 效度证据很少时，要写进局限[^flake2020measurement-e13]。怎样把测量本身做扎实（信度、多种效度证据、量表编制），见[测量](../05_research-strategies/measure.md)。
4. **人工检查一批数据的标签。** 自动拿来的标签可能错得很多。一项研究发现，所查的缺陷报告里有 33.8% 被分错了：它们对应的不是代码修复，而是新功能、文档更新或内部重构[^herzig2013bug-e1]。作者的建议是：用缺陷数据集之前，至少人工验证足够多的样本，并把数据质量当作效度威胁来讨论[^herzig2013bug-e5]。

**计算机里常见的构念效度陷阱**：

- **用平台数据代表抽象概念。** GitHub 数据可以直接用来描述项目的属性，但用它对更抽象的概念下结论，就要谨慎[^kalliamvakou2014promises-e11]。比如用"星标数"代表"项目质量"。
- **大模型"见过"评测题。** 如果评测数据进过模型的训练数据，模型的表现会被高估[^sainz2023nlp-e2]。这时你测到的可能是记忆，不是检测能力。评测集本身被用于训练时，整个实验的结论都会作废[^sainz2023nlp-e3]。怎样选评测数据来避开它，见[比较评估](../05_research-strategies/compare_evaluate.md)。贯穿例子要证明的正是这一条：它是别人评测的构念效度威胁，在你的项目里成了要测量的对象。

**写下来：** 写出你主张里的每个关键概念，各用一两句话定义。在旁边写出你打算用的指标，再写一句"为什么它能代表这个概念"。写不出那一句的，就是你的构念效度威胁。

## 4. 内部效度：真的是你改变的因素造成的吗？

**这一节在你的主张涉及"A 导致 B"时是重点。** 贯穿例子说评测结果"被泄露高估"，暗含"泄露让检出率变高"，所以也要过这一关。只描述现象的研究，比如只数泄露样本占多少，可以跳过。

软件工程的研究方法手册这样说内部效度：它关注结果是否真的由数据得出，典型的错误是没有处理好混杂变量，或者误用统计分析[^easterbrook2008selecting-e65]。**混杂变量**是你没控制住、又会影响结果的第三个因素：研究 A 是否影响 B 时，B 可能同时受第三个因素影响[^runeson2009guidelines-e4]。

**做法：**

1. **列出"其他解释"。** 对你预期看到的结果，写出除了你的解释之外，还有什么能产生同样的结果。做实验时，要报告所有你认为可能让它不成立的东西：其他可能的原因，以及你用什么办法排除了哪些[^feynman1974cargo-e11]。
2. **对每个其他解释，在设计里想一个办法排除它**。贯穿例子里：泄露样本可能本来更简单，就按长度、漏洞类型和部署年份，给泄露样本配上相近的未泄露样本再比；所有比较用同一个模型版本、同样的参数和提示；判定"检出"时隐去样本是否泄露，再判。如果你的主张是因果的，比如"加入漏洞模式提示会提高检出率"，还要一次只改一处（提示里同时加了漏洞模式和示例代码，就分不清是哪个起作用），要分组时随机分。
3. **别以为自己足够客观。** 光有好的意愿不够，记忆会出错，人会不自觉地往想要的方向推理，这些偏差常常发生在意识之外[^nosek2018preregistration-e3]。所以要靠设计来防，而不是靠自觉。

这些办法不是计算机独有的。动物实验的设计指南里，内部效度方面最常见的建议就是随机分配、对评估结局的人设盲等[^henderson2013threats-e9]；具体要防哪些混杂，又因领域和模型而不同[^henderson2013threats-e12]。怎样系统地排除其他解释、什么时候做消融，见[解释因果](../05_research-strategies/explain_causality.md#主动排除其他解释)、[构建改进](../05_research-strategies/build_improve.md)和[对照实验](../06_methods/controlled_experiment.md)。

**写下来：** 对你预期的核心结果，写出至少三个"其他解释"，每个旁边写一句你打算怎样在设计里排除它。排除不了的，标出来，第 7 节要用。

## 5. 外部效度：结论能推广到哪里？

软件工程的研究方法手册这样说外部效度：它关注"结果具有普遍性"的说法是否站得住，这常常取决于你怎样抽样[^easterbrook2008selecting-e67]。

**做法：**

1. **先写下目标总体。** 目标总体是你希望结论能推广到的那个群体或数据分布。机器学习的报告清单指出，论文并不总是写清楚它[^kapoor2024reforms-e5]。你的结论是关于"所有 Solidity 合约"、"以太坊上已部署的合约"，还是"大模型生成的合约"？
2. **比较你的样本和目标总体差在哪。** 例子：
   - 你用的是公开漏洞数据集里的合约，它们大多比真实合约短、漏洞更典型；
   - 你只试了几个模型，每个只有一个版本；
   - 你只能在公开的训练语料里找泄露，训练数据不公开的模型查不了。
3. **对每个差别，决定是扩大样本，还是缩小主张。** 能多试几个模型、几个数据集，就多试：动物实验的研究者也常通过在多种模型系统中重现效果，来应对外部效度威胁[^henderson2013threats-e6]。做不到，就把主张写窄。推广的说法要和支持它的证据强度相称[^henrich2010weirdest-e7]。
4. **为你的样本选择给出具体的理由。** 软件工程常招学生做被试，容易招够人，但降低了外部效度，需要论证为什么学生身上的结果仍适用于业界开发者[^easterbrook2008selecting-e74]。理由要针对你这项研究的具体情况，而不是泛泛一句"学生可以代表开发者"[^falessi2018empirical-e6]。

**两件容易忽略的事：**

- **多跑几个数据集，不等于更贴近真实。** 用同一种方法换更多数据，可能提高推广性，但不能提高真实性，也不能加强对人为因素的控制[^storey2020who-e8]。如果你关心开发者真实使用时有没有用，光加数据集不够。
- **结论会过期。** 即使模型现在能推广到目标总体，表现也可能因为数据分布随时间变化而下降[^kapoor2024reforms-e23]。大模型更新很快，记下每个结果对应的模型版本和时间。

**内部效度和外部效度常常要取舍。** 软件工程的方法文献指出：做实验要在两者之间权衡，不可能同时做到最大[^falessi2018empirical-e3]；每种研究策略在推广性、真实性、控制和精度上都各有长短，每个设计决定都是取舍[^storey2020who-e3]。条件控制得越严，越像实验室，越不像真实世界。你要做的是：按你的主张决定哪个更重要，然后把另一个写进局限。

**写下来：** 写一句"我的结论适用于____"。再写一句"它不一定适用于____"。第二句至少列三项。

## 6. 结论效度与可靠性：数据够不够，换人做还一样吗？

### 结论效度

这一类威胁大多出在分析阶段，但要在设计阶段就定下规矩。

**做法：**

1. **事先定好怎么分析。** 做实验和问卷时，要事先定好用什么统计检验，提前规划，才能顺利分析和解读结果[^easterbrook2008selecting-e73]。具体要写下：比较哪几组、看什么指标、多大的差异算有意义、每组跑几次。
2. **考虑预注册。** **预注册**是在看到研究结果之前，先把研究问题和分析计划定下来[^nosek2018preregistration-e1]。它限制什么、不限制什么、计算机方向的现状，见[从研究问题到证据清单](01_question-to-evidence.md)。
3. **知道哪些做法不能碰。** 软件工程的实证研究标准把这两种列为反面做法：在声称是验证性的研究里，看到结果再提出假设；只报告结果显著的那部分检验[^ralph2020empirical-e27]。

重复几次、怎样报告波动、怎样做统计检验和效应量，属于具体套路和方法的内容，见[比较评估](../05_research-strategies/compare_evaluate.md)和[分析与解读](07_analyze-and-interpret.md)。

### 可靠性

可靠性问的是：换别的研究者重做，结果是否一样。研究者引入偏差时就会出问题，比如被评估的工具是研究者自己有利害关系的[^easterbrook2008selecting-e68]。换句话说，**评估自己提出的方法，正是这种情况**。

**做法：**

- **把判定规则写成文字，并且公开。** 类别之间的界限本身可能就不清楚，前面那项缺陷报告研究的应对是逐字公开完整的分类规则[^herzig2013bug-e4]。
- **需要人判断的，安排两个人独立判断。** 软件工程的评分者一致性标准要求：描述两个以上评分者怎样独立评分、分歧怎样解决，并报告合适的一致性统计量[^ralph2020empirical-e129]。

**写下来：** 写一份一页以内的分析计划：比较什么、用什么指标、多大的差异算有意义、需要人判断的地方由谁判、判断规则是什么。

## 7. 给每个威胁定一个处理办法

现在你手上有一份分好类的威胁清单。对每一条，决定三件事之一：

- **消除**：改设计，让它不再成立。比如所有比较都用同一个模型版本。
- **减轻**：做不到完全消除，但可以检查它有多大影响。比如人工检查 100 个样本，估计标签错了多少。
- **承认**：做不到，或者代价太大，就写进局限，并相应地缩小主张。

把它们整理成一张表：

| 威胁 | 类型 | 有多严重 | 设计上怎么处理 | 处理后还剩什么 | 写进局限吗 |
|---|---|---|---|---|---|
| 泄露样本本来就更简单 | 内部 | 高：差距可能全来自难度 | 按长度、漏洞类型、部署年份配对再比 | 配不上对的样本只能单独报告 | 是 |
| "完全相同"漏掉了改名的复制 | 构念 | 中 | 同时用"高度相似"的定义，两种结果都报告 | 相似的阈值带主观性 | 是 |
| 只能查训练语料公开的模型 | 外部 | 中 | 再加两个训练语料公开的开源模型 | 闭源模型的结论不确定 | 是 |
| 判定人知道样本是否泄露 | 可靠性 | 中 | 隐去泄露标记，两人独立判 | 很小 | 否，但在方法里写清做法 |

**怎样判断"有多严重"：** 问自己，如果这个威胁成立，你的核心主张还剩多少。会让主张整个作废的，必须消除；只影响适用范围的，可以缩小主张、写进局限。

几条要求：

- **写真正的威胁，不要凑数。** 编程语言领域的评估清单批评过：软件工程论文的效度威胁一节，常常只提无关紧要的，回避真正的威胁[^blackburn2018sigplan-e10]。
- **说明你做了什么。** 软件工程的实证研究标准把"写出为考察或减轻局限所做的合理努力"列为加分项[^ralph2020empirical-e51]；它的实验标准把"只罗列威胁、不联系到结果"列为反面做法[^ralph2020empirical-e52]。
- **严重的威胁消除不了，就改主张。** 这时回到[收敛成项目](../01_find-a-problem/05_converge.md)，而不是寄希望于审稿人看不出来。

**写下来：** 填好上面这张表。至少要有一行是"高"，而且你已经想出了处理办法。如果没有一行是"高"，多半是你还没找到真正的威胁。

## 8. 现在就写下局限，定下诚实报告的规矩

局限不是论文写完才补的一段。在设计阶段写下来，能让你从一开始就知道主张该说到多大。

**做法：**

1. **写一份局限草稿。** 把上一节表里"写进局限"的那些整理成几句话。软件工程的实证研究标准要求披露所有主要局限[^ralph2020empirical-e18]。机器学习的报告清单还建议写清结论在哪些情况下预计不成立，这能帮读者形成合理的预期，避免炒作[^kapoor2024reforms-e24]。
2. **对照局限，改写主张。** 编程语言领域的评估清单提醒：不写局限、或只写无关紧要的局限，会让读者得出过强的结论[^blackburn2018sigplan-e3]。软件工程的实证研究标准列出的一种反面做法是：承认了局限，写结论时却当它不存在[^ralph2020empirical-e66]。如果局限写着"只试了一个模型"，主张里就不能说"大模型"。
3. **现在就决定：无论结果如何都报告。** 决定检验一个想法，就要无论结果正反都发表；只发表某一类结果，会让论证显得比实际更好[^feynman1974cargo-e9]。
4. **准备好记录偏离。** 实际做的时候，你多半会改计划。要记录最初的研究方案和之后的所有偏离，让别人能理解你的设计、解读结果[^easterbrook2008selecting-e72]。偏离了怎样报告，见[从研究问题到证据清单](01_question-to-evidence.md)。

为什么这些关乎科研诚信，见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)。

**写下来：** 写一段三到五句的局限草稿，再写一句修改后的核心主张，让它和局限一致。把"无论结果如何都报告"和"记录每一次偏离"写进你的研究计划。

> **不同类型的研究，这一步有什么不同**
>
> - **实证研究**（见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)）：威胁多在数据和判定规则上，要单列一节写清。He 等 2020 在最后的"结语与未来工作"一节写了两点可以改进的地方：判定克隆的阈值可以改成自适应的，人工整理的合约模板可能覆盖不全[^he2020characterizing-e14]。我们通读全文，没有找到单独的效度威胁小节；这是我们的阅读判断，原文本身证明不了"没有"。
> - **工具或方法论文**（见[工程研究](../07_fields/computer-science/practices/engineering_research.md)）：威胁多在"比得公不公平、够不够广"。Slither 写明最主要的效度威胁：主实验只比了重入检测、合约数量有限，按交易次数挑合约也没有社区统一的标准[^feist2019slither-e14]。
> - **基准或数据集**（见[基准评测](../07_fields/computer-science/practices/benchmarking.md)）：最大的威胁常在标注本身。SmartBugs 承认人工标注可能标错，应对办法是全体作者各自标注，再讨论分歧达成一致[^durieux2020empirical-e14]。
> - **综述**（见[综述研究](../06_methods/review_study.md)）：威胁在检索和筛选会不会漏。Rameder 等 2022 写明：检索截止后发表的研究没有收进来，也没有做有结构的滚雪球检索（顺着参考文献继续找）[^rameder2022review-e14]。

---

> **不同的看法：定性研究要不要谈"效度"？**
>
> 上面的效度分类，软件工程的研究方法手册是拿来评价以检验假设为主的（实证主义）研究的[^easterbrook2008selecting-e69]。访谈、民族志这类定性研究要不要套用，有两种看法：
>
> - **不该套用。** 许多持建构主义立场的研究者（认为现实是由人建构的、因人因情境而异）认为，"效度"这个概念本身太偏向实证主义，不能准确反映定性研究的性质[^easterbrook2008selecting-e70]。软件工程的扎根理论标准也说，评价这类研究应看可信度、共鸣、有用性以及是否扩展了已有知识，内部效度、可推广性等定量标准一般不适用[^ralph2020empirical-e323]。
> - **仍要讲效度，但在研究过程中用具体策略建立它。** 同一本手册转述了这一派的主张，并列出提高这类研究效度的策略[^easterbrook2008selecting-e75]，例如用不同来源的数据互相印证、诚实交代研究者自己带入的偏见[^easterbrook2008selecting-e71]，回去请参与者确认你的解读、报告和正在形成的理论不一致的信息[^easterbrook2008selecting-e27]。
>
> 两种看法都要求你防止自己被带偏，分歧在用什么词、按什么标准评价。实际操作中：先确认你的方法属于哪个传统，按那个传统的标准来列威胁和应对。定性研究也要做第 1 节的练习，只是归类时用可信度这类说法。具体做法见[访谈研究](../06_methods/interview_study.md)、[扎根理论](../06_methods/grounded_theory.md)和[案例研究](../06_methods/case_study.md)。

## 关键判断

**这个威胁是要堵上，还是写进局限？** 可以这样判断：

| 情况 | 通常的做法 |
|---|---|
| 威胁成立时，核心主张整个作废 | 必须在设计里消除；消除不了，改主张 |
| 只影响结论适用的范围 | 缩小主张，写进局限 |
| 是你选的方法固有的局限（如案例研究推广性有限） | 写清楚即可；软件工程的实证研究标准认为拿它批评研究不成立[^ralph2020empirical-e25] |
| 消除它要花的时间比整个项目还长 | 承认它，并想一个便宜的办法估计它有多大 |
| 你说不清它有多严重 | 在[小规模试验](05_pilot-and-derisk.md)里先试一下 |

**什么时候算想够了？** 不是"再也想不出威胁"，而是：你的套路最要紧的那一类威胁都有了处理办法；剩下的威胁都写进了局限草稿；主张已经按局限改写过；导师或同学看过威胁清单，没有指出你漏掉的严重威胁。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 实验做完才想效度 | 到分析阶段才考虑效度已经太晚[^runeson2009guidelines-e2] |
| 效度威胁只列无关紧要的 | 回避真正的威胁[^blackburn2018sigplan-e10]，读者会得出过强的结论[^blackburn2018sigplan-e3] |
| 只罗列威胁，不说对结果有什么影响 | 是软件工程实验标准列出的反面做法[^ralph2020empirical-e52] |
| 用间接指标，不说明为什么能代替 | 测到的可能不是你想说的东西[^blackburn2018sigplan-e13] |
| 直接用现成的标签，不人工检查 | 标签可能大量出错[^herzig2013bug-e1] |
| 不确认评测数据是否进过模型的训练数据 | 模型表现会被高估[^sainz2023nlp-e2] |
| 用不合适的标准要求自己的研究 | 比如对没有因果关系的研究追求内部效度；软件工程的实证研究标准明确要求避免这样做[^ralph2020empirical-e24] |
| 局限里承认了，结论里却当没这回事 | 局限形同虚设[^ralph2020empirical-e66] |
| 相信自己足够客观，不做设盲和事先计划 | 偏差常常发生在意识之外[^nosek2018preregistration-e3] |

## 产出物

- 一份"结论可能错的理由"清单，每条标了类型（第 1、2 节）
- 关键概念的定义和指标，以及指标能代表概念的理由（第 3 节）
- （涉及因果时）其他解释清单和排除办法（第 4 节）
- "适用于 / 不一定适用于"两句话（第 5 节）
- 一页分析计划，含判定规则（第 6 节）
- 威胁处理表（第 7 节）
- 局限草稿和改写后的核心主张（第 8 节）

## 检查点

满足下面几条，可以进入下一步：

- [ ] 列出了至少八条"结论可能错的理由"，并按类型归了类
- [ ] 知道自己的研究套路最要紧的是哪一类效度，那一类的威胁都有了处理办法
- [ ] 每个关键概念都有定义，每个指标都能说出它为什么能代表这个概念
- [ ] 写下了目标总体，说得出样本和它差在哪
- [ ] 分析计划在看到数据之前就写好了，需要人判断的地方有书面规则
- [ ] 威胁处理表里，每个"高"威胁都已消除或减轻，或者主张已经相应改小
- [ ] 写好了局限草稿，核心主张和局限一致
- [ ] 导师或同学看过威胁清单，没有指出漏掉的严重威胁

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 有一个会让主张作废的威胁，怎么也消除不了 | [收敛成项目](../01_find-a-problem/05_converge.md)第 1 节，把主张改小或换一个 |
| 关键概念找不到能代表它的指标 | [从研究问题到证据清单](01_question-to-evidence.md)，重新想需要什么证据 |
| 发现选的方法根本排除不了主要的其他解释 | [选方法](02_choose-method.md)，换一种方法或套路 |
| 按局限改写后，主张弱到没人在乎 | [收敛成项目](../01_find-a-problem/05_converge.md)第 2 节，重新判断值不值得做 |

## 下一步

威胁清单里总有几条你拿不准有多严重，比如"评测数据到底有多少进过训练数据""两个人判定的一致性够不够"。下一步，用花钱最少的小实验先把这些最没把握的地方试出来，见[最小可跑版本](05_pilot-and-derisk.md)。

[^runeson2009guidelines-e1]: Runeson & Höst 2009，§5.2.3，第 153 页。[证据](../../sources/notes/runeson2009guidelines.md#e1)
[^runeson2009guidelines-e2]: Runeson & Höst 2009，§5.2.3，第 153 页。[证据](../../sources/notes/runeson2009guidelines.md#e2)
[^runeson2009guidelines-e4]: Runeson & Höst 2009，§5.2.3，Internal validity。[证据](../../sources/notes/runeson2009guidelines.md#e4)
[^feynman1974cargo-e7]: Feynman 1974，演讲正文，Millikan 油滴实验之后。[证据](../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e9]: Feynman 1974，演讲正文，发表结果。[证据](../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e11]: Feynman 1974，演讲正文，科学诚信一段。[证据](../../sources/notes/feynman1974cargo.md#e11)
[^easterbrook2008selecting-e65]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e65)
[^easterbrook2008selecting-e66]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e66)
[^easterbrook2008selecting-e67]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e67)
[^easterbrook2008selecting-e68]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e68)
[^easterbrook2008selecting-e69]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e69)
[^easterbrook2008selecting-e70]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e70)
[^easterbrook2008selecting-e71]: Easterbrook 等 2008，§7.0，转述 Creswell 2002 的策略。[证据](../../sources/notes/easterbrook2008selecting.md#e71)
[^easterbrook2008selecting-e27]: Easterbrook 等 2008，§7.0，转述 Creswell 2002 的策略。[证据](../../sources/notes/easterbrook2008selecting.md#e27)
[^easterbrook2008selecting-e72]: Easterbrook 等 2008，§7.0 Practical Considerations。[证据](../../sources/notes/easterbrook2008selecting.md#e72)
[^easterbrook2008selecting-e73]: Easterbrook 等 2008，§7.0 Practical Considerations。[证据](../../sources/notes/easterbrook2008selecting.md#e73)
[^easterbrook2008selecting-e74]: Easterbrook 等 2008，§5.1 Controlled Experiments。[证据](../../sources/notes/easterbrook2008selecting.md#e74)
[^easterbrook2008selecting-e75]: Easterbrook 等 2008，§7.0 Empirical Validity。[证据](../../sources/notes/easterbrook2008selecting.md#e75)
[^flake2020measurement-e16]: Flake & Fried 2020，Questionable Measurement Practices，引用 Shadish 等 2002。[证据](../../sources/notes/flake2020measurement.md#e16)
[^flake2020measurement-e7]: Flake & Fried 2020，Question 1: What is your construct?。[证据](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e13]: Flake & Fried 2020，Question 6: Do you create a measure on the fly?。[证据](../../sources/notes/flake2020measurement.md#e13)
[^ralph2020empirical-e18]: ACM SIGSOFT Empirical Standards，General Standard，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e18)
[^ralph2020empirical-e24]: ACM SIGSOFT Empirical Standards，General Standard，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e25]: ACM SIGSOFT Empirical Standards，General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e51]: ACM SIGSOFT Empirical Standards，General Standard，Desirable Attributes。[证据](../../sources/notes/ralph2020empirical.md#e51)
[^ralph2020empirical-e52]: ACM SIGSOFT Empirical Standards，Experiments，Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e52)
[^ralph2020empirical-e66]: ACM SIGSOFT Empirical Standards，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e129]: ACM SIGSOFT Empirical Standards，Inter-Rater Reliability and Agreement，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e323]: ACM SIGSOFT Empirical Standards，Grounded Theory，Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e323)
[^blackburn2018sigplan-e3]: SIGPLAN 清单 2018，Fails to acknowledge limitations。[证据](../../sources/notes/blackburn2018sigplan.md#e3)
[^blackburn2018sigplan-e10]: SIGPLAN 清单 2018，Notes。[证据](../../sources/notes/blackburn2018sigplan.md#e10)
[^blackburn2018sigplan-e13]: SIGPLAN 清单 2018，Indirect or inappropriate proxy metric。[证据](../../sources/notes/blackburn2018sigplan.md#e13)
[^kapoor2024reforms-e5]: Kapoor 等 2024（REFORMS），Module 1，1a。[证据](../../sources/notes/kapoor2024reforms.md#e5)
[^kapoor2024reforms-e6]: Kapoor 等 2024（REFORMS），Module 3，3d。[证据](../../sources/notes/kapoor2024reforms.md#e6)
[^kapoor2024reforms-e23]: Kapoor 等 2024（REFORMS），Module 8，8a。[证据](../../sources/notes/kapoor2024reforms.md#e23)
[^kapoor2024reforms-e24]: Kapoor 等 2024（REFORMS），Module 8，8b。[证据](../../sources/notes/kapoor2024reforms.md#e24)
[^herzig2013bug-e1]: Herzig、Just、Zeller 2013，摘要。[证据](../../sources/notes/herzig2013bug.md#e1)
[^herzig2013bug-e4]: Herzig、Just、Zeller 2013，§XI Threats to Validity。[证据](../../sources/notes/herzig2013bug.md#e4)
[^herzig2013bug-e5]: Herzig、Just、Zeller 2013，§XII Conclusion and Consequences。[证据](../../sources/notes/herzig2013bug.md#e5)
[^kalliamvakou2014promises-e11]: Kalliamvakou 等 2014，§6 Discussion & Conclusions。[证据](../../sources/notes/kalliamvakou2014promises.md#e11)
[^sainz2023nlp-e2]: Sainz 等 2023，摘要。[证据](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e3]: Sainz 等 2023，§3 Defining data contamination。[证据](../../sources/notes/sainz2023nlp.md#e3)
[^henderson2013threats-e6]: Henderson 等 2013，Introduction。[证据](../../sources/notes/henderson2013threats.md#e6)
[^henderson2013threats-e9]: Henderson 等 2013，Editors' Summary。[证据](../../sources/notes/henderson2013threats.md#e9)
[^henderson2013threats-e12]: Henderson 等 2013，Discussion。[证据](../../sources/notes/henderson2013threats.md#e12)
[^henrich2010weirdest-e7]: Henrich 等 2010，§6.3 Recommendations。[证据](../../sources/notes/henrich2010weirdest.md#e7)
[^falessi2018empirical-e3]: Falessi 等 2018，§4.1.2。[证据](../../sources/notes/falessi2018empirical.md#e3)
[^falessi2018empirical-e6]: Falessi 等 2018，§6.2 Added statements，ST16。[证据](../../sources/notes/falessi2018empirical.md#e6)
[^storey2020who-e3]: Storey 等 2020，§3.3。[证据](../../sources/notes/storey2020who.md#e3)
[^storey2020who-e8]: Storey 等 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e8)
[^nosek2018preregistration-e1]: Nosek 等 2018，Abstract。[证据](../../sources/notes/nosek2018preregistration.md#e1)
[^nosek2018preregistration-e3]: Nosek 等 2018，Mental Constraints on Distinguishing Predictions and Postdictions。[证据](../../sources/notes/nosek2018preregistration.md#e3)
[^he2020characterizing-e14]: He 等 2020（以太坊合约代码克隆），§7 Concluding Remarks and Future Work，第 15 页。[证据](../../sources/notes/he2020characterizing.md#e14)
[^feist2019slither-e14]: Feist 等 2019（智能合约静态分析工具 Slither），§V-D Threats to Validity，第 7 页。[证据](../../sources/notes/feist2019slither.md#e14)
[^durieux2020empirical-e14]: Durieux 等 2020（智能合约分析工具评测 SmartBugs），§4.2 Threats to Validity，第 10 页。[证据](../../sources/notes/durieux2020empirical.md#e14)
[^rameder2022review-e14]: Rameder 等 2022（以太坊智能合约漏洞分析的系统综述），§9.3 Limitations of Our Review，第 17 页。[证据](../../sources/notes/rameder2022review.md#e14)
