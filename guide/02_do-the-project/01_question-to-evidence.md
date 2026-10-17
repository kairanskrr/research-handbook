# 从研究问题到证据清单

> 本章的道理适用于各学科，例子和具体做法以计算机为例。第 3、5、6 节主要针对实证研究（靠收集数据得出结论的研究），适用范围在节首注明。

> **这一章必须做的事**
>
> 1. **把核心主张拆成两到四个研究问题，标上类型。** 主张说"导致"，问题却只能回答"相关"，就改其中一个（[第 1 节](#1-把主张拆成研究问题)）。
> 2. **给主张里每个关键词写一句操作定义。** 写成"具体看什么、怎么数"；最有争议的那个，再备一个定义（[第 2 节](#2-给每个关键词一个可以操作的定义)）。
> 3. **写清你统计的"一个"是什么，结论想推到谁身上。** 分析单元、总体、抽样框、样本各写一句，再写一句抽样框和总体差在哪（[第 3 节](#3-定下研究对象分析单元和总体)）。
> 4. **看数据之前，写下什么结果算支持、什么算否定。** 标准写"差多大"，不只写"显著"；再写出至少一个竞争解释，以及怎样排除它（[第 4 节](#4-事先写下什么结果算支持什么结果算否定)）。
> 5. **标上验证或探索，合成一份带日期的证据清单。** 验证性的假设要写在看数据之前；空结果表的每一格，都要在清单里找得到怎么算出来（[第 5 节](#5-分清你是在检验还是在探索)、[第 7 节](#7-汇成一份证据清单)）。
>
> **做到了就往下走：** 每个研究问题都有类型、操作定义和事先写好的支持、否定标准，证据清单带日期存进了项目仓库。下一步：[选方法](02_choose-method.md)。

## 你现在在哪里

你刚走完第一部分的出口（见[收敛成项目](../01_find-a-problem/05_converge.md#7-出口可以进入第二部分了吗)）。手里有四样东西：一句写得下来的核心主张，一页项目简介，一张空的结果表，一份过了关的出口检查。你也大致判断了自己要做哪一类研究。

贯穿全书的例子走到这里，主张是"现有大模型漏洞检测的评测结果被数据泄露高估了"，主要套路是测量；空的结果表是"每个模型、每个工具，去掉泄露合约前后的准确率"。

可是一坐下来准备动手，问题又冒出来了：

- 主张里的"高估""检出""泄露"，到底按什么算？
- 统计的"一个"是一份合约、一个函数，还是一个漏洞？
- 结果出来以后，差多少才算"高估"，差多少只能说"差不多"？
- 你还没想好要不要先定假设，还是先跑起来看看。

这些不想清楚，数据收回来以后，你会发现怎么解释都说得通。怎么解释都通，恰恰说明它什么也证明不了。

## 这一阶段要解决什么

把核心主张变成一份**证据清单**：每一条都写清楚问什么、测什么、在谁身上测、什么结果算支持、什么结果算否定。具体是回答下面六个问题：

1. 我的核心主张，拆成哪几个能回答的研究问题？
2. 主张里的每个关键词，按什么规则去测、去数？
3. 我研究的对象是什么，结论想推到多大范围？
4. 什么结果算支持，什么结果算否定？这些要在看数据之前写下来。
5. 每个研究问题，是在检验一个事先定好的说法，还是在探索？
6. 要不要把计划事先公开存档？

这一章不选方法。用对照实验、问卷还是仓库挖掘，是下一章的事。这里只把"要回答什么、怎样算回答了"定死，方法就有了选择的依据。

---

## 1. 把主张拆成研究问题

**先把核心主张拆开，每一部分写成一个问句。** 选研究方法时，最先要做的事之一就是把研究问题弄清楚[^easterbrook2008selecting-e31]。规范的研究也要求写明研究问题，并说明它为什么重要[^ralph2020empirical-e22]。

1.5 列出的[审稿人会追问的那几个问题](../01_find-a-problem/05_converge.md#4-拿什么让人相信)，往往就是研究问题的雏形。以"现有大模型漏洞检测的评测结果被数据泄露高估了"为例：

| 研究问题 | 问题的类型 |
|---|---|
| 问题一：常用评测集里，有多少合约出现在模型的训练数据中？ | 基础比率（有多常见） |
| 问题二：模型在泄露样本和未泄露样本上的检出率差多少？ | 关系（两者有没有关联） |
| 问题三：去掉泄露样本后，工具之间的排名会不会变？ | 描述（比较去掉前后的排名） |

**认清每个问题属于哪一类，因为类型决定了要什么证据。** 下面的分类出自软件工程的研究方法指南[^easterbrook2008selecting-e32][^easterbrook2008selecting-e34][^easterbrook2008selecting-e35][^easterbrook2008selecting-e37][^easterbrook2008selecting-e39]；我们认为，问法本身不限于软件工程，其他做实证研究的学科也可以借用：

| 类型 | 问句的样子 | 合约例子 |
|---|---|---|
| 存在与描述 | X 存在吗？X 是什么样的？怎么测量它？ | 评测集里有泄露吗？ |
| 基础比率 | X 通常多常见、怎样分布？ | 泄露样本占多大比例？ |
| 关系 | X 和 Y 相关吗？ | 泄露的合约，检出率是否更高？ |
| 因果 | X 会导致 Y 吗？ | 泄露是不是检出率高的原因？ |
| 设计 | 做到 X 的有效办法是什么？ | 怎样建一个不容易泄露的评测集？ |

用这张表时注意两点：

- **基础比率常被跳过。** 不知道某个现象通常多常见，就没法判断眼前的情况是正常还是反常[^easterbrook2008selecting-e34]。在合约例子里，先回答"泄露比例有多大"，后面的"影响有多大"才有意义。
- **相关不等于因果。** 把相关当成因果是常见错误，证明因果通常比证明相关难得多[^easterbrook2008selecting-e36]。问题二是关系问题。如果你的主张写的是"泄露**导致**了高估"，就得按因果问题准备证据，见[解释因果](../05_research-strategies/explain_causality.md)。

**设计问题要建在知识问题之上。** 设计问题的前提，是相关的知识问题已经有了答案，对要解决的问题了解得足够多[^easterbrook2008selecting-e40]。如果你想建一个新评测集，最好先弄清旧评测集到底错在哪。

**写下来：** 把核心主张拆成两到四个研究问题，每个注明类型。如果某个问题的类型和你主张里的措辞对不上，比如主张说"导致"，问题却只能回答"相关"，改其中一个。

## 2. 给每个关键词一个可以操作的定义

**主张里的每个关键词，都要写成"具体看什么、怎么数"。** 这叫**操作定义**：把一个概念变成一套可以照着执行的测量规则。

为什么要这样做：你实际测量的东西，必须真的代表你想研究的概念[^runeson2009guidelines-e3]。心理学的测量研究也提醒：一开始没把概念定义清楚，后面每个测量决定都难做，也会留下有意无意钻空子的余地[^flake2020measurement-e7]。

拿合约例子，逐个词问下去：

| 关键词 | 要定下来的 | 一种可能的定义 |
|---|---|---|
| 泄露 | 一样才算，还是相似就算？在哪里找？ | 去掉注释和空白后，评测合约和训练语料中的某份合约完全相同 |
| 检出 | 报出漏洞类型就算，还是要指出代码位置？ | 报对漏洞类型，并指出漏洞所在的函数 |
| 高估 | 和什么比？差多少才算？ | 同一工具在未泄露样本上的检出率，比全体样本低 5 个百分点以上 |
| 大模型 | 哪几个模型、哪个版本、什么时候调用的？ | 列出模型名称、版本号和调用日期 |

**一个词，常常有几种合理的定义。** 这很正常。要做的是：选一种，写下理由；对结果影响大的，再试一两种别的定义，看结论变不变。比如"泄露"按完全相同算和按高度相似算，泄露比例可能差很多，两种都报告，读者才知道你的结论有多稳。

**别用一个顺手的数字代表一个复杂的概念。** 软件工程的实证研究标准把"用未经验证的单一指标度量多维的概念"列为反面做法，例子是用 GitHub 星标数代表项目流行度[^ralph2020empirical-e119]。同理，用"工具报警条数"代表"检出能力"也不行。

**名字一样，不等于测的是同一个东西。** 两个测量名字相似，不代表测的是同一个概念；名字不同，也不代表测的是不同概念[^flake2020measurement-e8]。别的论文也叫"检出率"，先看它的定义和你的是否一致，再拿来比。

怎样检验一把尺子准不准、稳不稳，是[测量](../05_research-strategies/measure.md)那一篇的内容。这里只要求你把定义写下来，并且在看到数据之前写。

**写下来：** 列出主张里的每个关键词，各写一句操作定义。对最可能有争议的那一个，再写一个备选定义。

## 3. 定下研究对象：分析单元和总体

> 本节适用于从一批对象中收集数据的研究。做证明或理论推导的研究可以跳过；做文献综合的研究，对象是文献，道理相同。

**先回答：你统计的"一个"是什么？** 这叫**分析单元**。在软件工程研究里，分析单元可以是一家公司、一个项目、一个团队、一位开发者、一次事件或一个工作产物；选对了分析单元，研究才能聚焦在你想研究的现象上[^easterbrook2008selecting-e15]。软件工程问卷调查的经验是：分析单元选错，收来的数据可能对你的研究问题毫无用处[^torchiano2017lessons-e5]。

合约例子里，至少有三种选法，算出来的"检出率"会不一样：

| 分析单元 | "检出率"的意思 | 会出什么问题 |
|---|---|---|
| 一份合约 | 有多少份合约被正确判断有无漏洞 | 一份合约里有五个漏洞，只发现一个，也可能算"检出" |
| 一个漏洞 | 所有已知漏洞里，有多少被找到 | 漏洞多的合约，权重自然更大 |
| 一个函数 | 有多少个函数被正确判断 | 跨函数的漏洞不好算 |

选哪个，看你的研究问题在问什么。问"开发者拿到一份合约，工具能不能帮上忙"，用合约；问"工具能找到多少漏洞"，用漏洞。

**再回答：结论想推到谁身上？** 先分清三个词：**总体**是你感兴趣的全部对象，**抽样框**是你实际能从中抽取的名单，**样本**是你最终研究的那一部分；抽样框通常并不完美[^ralph2020empirical-e42]。

- 合约例子中，总体可能是"以太坊上部署的所有合约"；抽样框可能是"公开了源码的合约"，它只包含愿意公开源码的那部分；样本是你最后用的几千份合约。
- 如果追求代表性，先写明你原则上想把结论推广到谁[^baltes2022sampling-e11]。代表性是样本和总体之间的关系，不是某种抽样技术自带的属性[^baltes2022sampling-e3]；抽样框本身有偏差，样本再大也弥补不了[^baltes2022sampling-e5]。
- 不追求代表性也完全可以，比如你要找的是特殊案例。这时要写明抽样的目标，并说明你的抽样办法对这个目标为什么合理，不必最优[^ralph2020empirical-e36]。研究本来就不以代表性为目标，却批评它缺乏代表性，这种批评不成立[^ralph2020empirical-e39]。

**样本要多大，要有依据。** 定量研究的样本量要足以检测出预期大小的效应，定性研究的数据要多到能达到饱和（新数据不再带来新发现）[^ralph2020empirical-e38]。具体怎么估算，要看你用的方法。

**不要夸大样本的代表性。** 尤其不要在局限部分承认抽样偏差，到了结论又把结果写得几乎普遍适用[^baltes2022sampling-e9]。

抽样的具体做法随方法而不同，见[问卷调查](../06_methods/questionnaire_survey.md#第一步从研究问题出发定义总体分析单元和抽样框)、[仓库挖掘](../07_fields/computer-science/practices/repository_mining.md#第三步筛选和抽样项目)等方法文档。

**写下来：** 写出你的分析单元、总体、抽样框和样本，各一句话。再写一句：抽样框和总体差在哪里，这个差别可能让结论偏向哪个方向。

## 4. 事先写下：什么结果算支持，什么结果算否定

**在跑实验、收数据之前，先预测结果。** 这能帮你解读结果、发现错误[^huang2023experiments-e3][^huang2023experiments-e4]。我们认为更重要的是，它逼你回答：**有没有什么结果，会让你承认主张错了？** 如果怎样的结果你都能解释成"支持"，这项研究就证明不了什么。

**怎么做：** 对每个研究问题，填一张表。后面写研究计划时，每个里程碑的["做完"标准](03_research-plan.md#3-给每个里程碑写下怎样算做完)就从这张表里来：

| 研究问题 | 我预测的结果 | 算支持的结果 | 算否定的结果 | 介于两者之间时，我会怎么写 |
|---|---|---|---|---|
| 问题一：泄露比例 | 两到三成 | 一成以上 | 几乎没有泄露 | 报告比例，主张改为"存在少量泄露" |
| 问题二：检出率差距 | 泄露样本高 10 个百分点以上 | 差 5 个百分点以上，且多个工具方向一致 | 差距小于 2 个百分点，或方向不一致 | 只能说"可能有影响"，不写"高估" |

表里的数字只是示意。关键是这些数字在看到数据之前就定下来，并且写下为什么定这个数。

**分清两种证据：有的只能否定，有的足以支持。** 政治学里的过程追踪方法（顺着事件经过一步步检验某个解释）区分了两种检验[^bennett2012process-e10][^bennett2012process-e12]：

- **过关检验**：例子是"案发当天，嫌疑人在不在本州？"不在，这个解释就被排除；在，也不大增加你对它的信心。
- **确凿证据检验**：像找到"冒烟的枪"。通过了，足以有力地支持这个解释；但它不是建立信心的必经之路，没找到这种证据，也不能说明解释错了。

它们原是政治学的方法，这里借来当作一种通用的判断思路，放到合约例子里：

- "评测集里确实有泄露样本"是过关检验。没有泄露，主张就站不住；有泄露，也不等于结果被高估了。
- "模型能逐字背出评测合约，而且在这些合约上的检出率明显高于其他合约"更接近确凿证据。

所以，光凭"找到了泄露"写不出"结果被高估"，还需要更强的证据。

**"统计上显著"不等于"差得有意义"。** 软件工程里比较随机算法（每次运行结果可能不同的算法）时，重点应是新方法有没有实际意义上的优势，用效应量（差别有多大的量化指标）及其置信区间衡量[^arcuri2014hitchhiker-e6]。重复运行几千次时，几乎任何差异都会显著，所以必须同时看效应量[^arcuri2014hitchhiker-e9]。在你的表里，"算支持"的标准应该写成差多大，而不只是"显著"。

**事先列出其他可能的解释。** 好的实证研究要考虑并排除其他可能的解释[^lipton2019troubling-e1]。合约例子里，一个明显的竞争解释是：泄露的合约可能本来就更老、更简单、漏洞更典型，检出率高也许不是因为模型"见过"它们。这条解释要在证据清单里占一行：拿什么证据排除它，比如比较难度相近的泄露样本和未泄露样本。

**证据要对准主张。** 你主张性能提升，就要分析性能，而不是易用性或通用性[^shaw2003writing-e12]。填完上面的表，回头逐行检查：每一行的证据，回答的是不是这一行的问题。

**写下来：** 为每个研究问题填好上面那张表，再为核心主张写出至少一个竞争解释，以及你打算怎样排除它。

## 5. 分清：你是在检验，还是在探索

> 本节适用于收集数据的研究。

验证性研究事先有明确的假设，用数据去检验它[^ralph2020empirical-e30]；探索性研究是为了摸清现象、产生假设。两者怎么分、探索时做什么，在[动手探索](../01_find-a-problem/03_explore.md#1-先认清你在探索还不是在检验)里讲过。到了这一步，大部分研究问题应当已经能写成验证性的，少数可以留作探索。

**真正的问题是混在一起，还不说明。** 在名为验证性的研究里，看到结果再提假设，或者只报告显著的那部分统计检验，都是反面做法[^ralph2020empirical-e27]。这不一定是故意的：记忆会出错，人会不自觉地往自己想要的方向推理，光有好的意愿不够[^nosek2018preregistration-e3]。所以要在证据清单里写明。

**怎么做**：

1. 在证据清单里，给每个研究问题标上"验证"或"探索"。
2. 标"验证"的，必须在看数据之前写好假设和第 4 节那张表。
3. 标"探索"的，也写下你打算看什么、怎么看，但不用写预测。
4. 做的过程中冒出新想法、追加了分析，单独记一笔，报告时标为探索性的。

在计算机方向，你可以先在一小批数据上反复试，摸清现象，再在另一批没看过的数据上检验。这就是先探索、后验证，只要两批数据分开，并如实写明哪一步是哪一种，就没有问题。贯穿例子里，问题一、问题二标"验证"；"按漏洞类型看，高估集中在哪一类"可以标"探索"。

**写下来：** 给每个研究问题标上"验证"或"探索"。对标"验证"的，确认你的假设已经写下、日期早于你看到相关数据的时间。

## 6. 要不要事先公开你的计划

> 本节适用于收集数据的研究，对验证性研究最重要。下面的资料主要出自心理学（Nosek 等、Simmons 等）和软件工程（ACM SIGSOFT 实证研究标准）。

**预注册**，就是在看到研究结果之前，先定好研究问题和分析计划[^nosek2018preregistration-e1]。软件工程实证研究标准说得更具体：预注册是把计划公开存档，目的是防止看到结果再提假设、减少数据分析中无意识的偏差，并对抗发表偏差[^ralph2020empirical-e29]。

**它不是要限制你。** 预注册不是说事先预测比事后探索更高级，而是让人分清哪个是哪个[^nosek2018preregistration-e4]。它不限制你做探索性分析；你也可以只提研究问题、写清打算怎么回答，结果和预测不符，同样可以发表[^simmons2018false-e2]。

**计划写到多细？** 软件工程实证研究标准对注册报告的要求是：详细到别人能照着完全重复你的数据收集和分析过程，而且你提出的假设能用你计划收集的数据来检验[^ralph2020empirical-e32]。你在第 1 到第 5 节写下的东西，基本就是这份计划的骨架。

**做的时候偏离了计划怎么办？** 研究不可能完全按计划进行。只要有理由，而且不是在知道修改会怎样影响结果之后才改，偏离就可以接受[^ralph2020empirical-e34]。如实报告改了什么、为什么改，有预注册加上偏离说明，仍比完全不预注册可信得多[^nosek2018preregistration-e5]。计划里的所有分析结果都要报告，否则仍然是选择性报告[^nosek2018preregistration-e6]。

**更进一步：注册报告。** 作者在看到结果之前，把研究问题和方法交给期刊审稿；第二阶段审稿不评判结果是否"重要"，只看研究做得好不好、是否按计划执行[^nosek2018preregistration-e7]。

**计算机方向的现状。** 软件工程的实验标准把"在会议或期刊允许时预注册假设和设计"列为加分项，而不是必要项[^ralph2020empirical-e176]。软件工程里已经有一些去处接受注册报告。据 Ernst 和 Baldassarre 2023 年的介绍，最早引入的是 2020 年的挖掘软件仓库国际会议（MSR，Mining Software Repositories）[^ernst2023registered-e1]；Empirical Software Engineering 期刊从 2020 年起支持这种形式，美国计算机协会（ACM）的 TOSEM 期刊（Transactions on Software Engineering and Methodology）从 2022 年起有类似的"Registered Paper"项目[^ernst2023registered-e2]。Empirical Software Engineering 的做法是把第一阶段（审研究计划）放到会议的专门轨道上办，当时可选 MSR、ICSME（软件维护与演化国际会议）和 ESEM（实证软件工程与度量会议）[^ernst2023registered-e3]。计算机其他方向的会议和期刊是否接受，本文资料未涉及；这些去处每年的规定也会变，请查你目标去处当年的投稿说明。即使不正式公开，在仓库里带日期地存一份计划，也能起到"让自己分清事先和事后"的作用。

**也别把它想得太神奇。** 预注册不能杜绝糟糕的统计做法，但能让这些做法被发现[^nosek2018preregistration-e8]；它能不能提高结果的可重复性，目前还没有足够的实验证据[^nosek2018preregistration-e9]。

> **不同的看法：探索性研究要不要预注册？**
>
> - 软件工程实证研究标准中的注册报告部分写明，它适用于检验假设的验证性研究；对诠释主义（关注人们怎样理解和赋予意义）、定性或探索性研究做预注册，仍有争议[^ralph2020empirical-e30]。
> - 同一份标准又把"以探索性或定性研究为由拒绝预注册"列为不成立的批评，认为各类研究都可以预注册[^ralph2020empirical-e31]。
>
> 实际操作中：验证性研究应当事先写好计划，有条件就预注册。探索性研究不一定要预注册，但最好也在开始前写下打算看什么、怎么看；报告时如实标明哪些分析是事先计划的，哪些是看到数据后追加的。

**写下来：** 决定你的项目要不要预注册，写一句理由。不管要不要，都把第 1 到第 5 节的结果合成一份带日期的计划，存进项目仓库。

## 7. 汇成一份证据清单

把前面几节的结果合成一张表，每个研究问题一行。这就是你这一章的主要产出：

| 研究问题 | 类型 | 关键词的操作定义 | 分析单元 / 总体 | 算支持 | 算否定 | 要排除的其他解释 | 验证 / 探索 |
|---|---|---|---|---|---|---|---|
| 问题一 | | | | | | | |
| 问题二 | | | | | | | |
| 问题三 | | | | | | | |

**拿空的结果表对一遍。** 1.5 画的[空结果表](../01_find-a-problem/05_converge.md#4-拿什么让人相信)，每一格都应该能从清单里找到"这个数怎么算出来"。找不到的格子，就是还没想清楚的地方。

**后面几章都从这份清单出发。** 选方法时，按清单一行一行挑；写研究计划时，每个里程碑就是清单里的一行或几行证据（见[形成研究计划](03_research-plan.md#2-把主张拆成里程碑每个里程碑是一份证据)）。

**写下来：** 填好这张证据清单，拿给导师或同学看，请他们挑一行问"这个结果出来了，你会怎么写"。答不上来的行，回到对应的小节重写。

> **不同类型的研究，这一步有什么不同**
>
> - **实证研究**（见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)）：清单围绕"要弄清什么现象"。He 等 2020 研究以太坊合约的代码克隆，用文字写出三个问题：克隆为什么出现、会不会传播漏洞、有没有被抄袭的应用以及影响多大[^he2020characterizing-e4]。
> - **工具或方法论文**（见[工程研究](../07_fields/computer-science/practices/engineering_research.md)）：清单的每一行是"好在哪"。Slither 论文先列出好工具应有的性质：处理真实代码不崩溃、快、找得全又误报少[^feist2019slither-e3]，评估就按这几条比[^feist2019slither-e9]。
> - **基准或数据集**（见[基准评测](../07_fields/computer-science/practices/benchmarking.md)）：清单要写清"标准答案"按什么算。SmartBugs 人工标出了每个漏洞所在的代码行[^durieux2020empirical-e5]，工具报出的类别和行号都对上，才算查出[^durieux2020empirical-e11]。
> - **综述**（见[综述研究](../06_methods/review_study.md)）：研究对象是文献，清单从"要回答哪些问题"开始。Rameder 等 2022 先列出：有哪些漏洞、工具用什么方法检测、工具怎么评估、还有哪些难题[^rameder2022review-e2]。

---

## 关键判断

**定义定严还是定宽？** 操作定义常常要在"准"和"做得到"之间取舍。可以这样判断：

| 情况 | 通常的做法 |
|---|---|
| 严格的定义需要的数据拿不到 | 用宽一点的定义，并在主张里写明限制，例如"按完全相同计算的泄露" |
| 两种定义都合理，结果可能差很多 | 两种都做，都报告 |
| 定义宽到几乎什么都算 | 收窄；否则"支持"的结果没有意义 |
| 怎么定义都测不了这个概念 | 回到[收敛成项目](../01_find-a-problem/05_converge.md#1-写出你想证明的那句话)，改主张 |

**支持与否定的门槛定在哪里？** 门槛最好来自你的主张"有没有意义"，而不是来自你猜结果会是多少。问自己：差多少，读者才会改变做法？例如工具的检出率差 1 个百分点，开发者大概不会因此换工具。

**问题太多怎么办？** 建议一个项目先控制在两到四个研究问题；如果清单超过十行，多半是核心主张还不够集中，回去收窄。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 关键词没有操作定义就开始收数据 | 后面每个测量决定都难做，也给钻空子留了余地[^flake2020measurement-e7] |
| 用一个现成数字代表复杂概念 | 未经验证的单一指标测不了多维的概念[^ralph2020empirical-e119] |
| 没想清楚分析单元 | 数据可能对研究问题毫无用处[^torchiano2017lessons-e5] |
| 只写了"支持"的标准，没写"否定"的 | 什么结果都能解释成支持，研究就证明不了什么 |
| 把"找到了泄露"当成"证明了高估" | 这只是过关检验：没通过能排除解释，通过了也不大增加信心[^bennett2012process-e10] |
| 只看是否显著，不看差别多大 | 运行次数多时，几乎任何差异都会显著[^arcuri2014hitchhiker-e9] |
| 主张写"导致"，证据只能说明"相关" | 证明因果比证明相关难得多[^easterbrook2008selecting-e36] |
| 看完结果再提假设，当成事先的预测报告 | 在名为验证性的研究里，这是反面做法[^ralph2020empirical-e27] |
| 局限里承认样本偏差，结论里写成普遍规律 | 结论超出了证据[^baltes2022sampling-e9] |

## 产出物

- 一份证据清单（第 7 节）：每个研究问题的类型、操作定义、分析单元和总体、支持与否定的标准、要排除的其他解释、验证还是探索
- 每个研究问题的预测表（第 4 节）
- 一份带日期的计划；如果决定预注册，还有公开存档的版本（第 6 节）

## 检查点

满足下面几条，可以进入下一步：

- [ ] 核心主张拆成了两到四个研究问题，每个标明了类型
- [ ] 主张里的每个关键词都有操作定义；有争议的，准备了备选定义
- [ ] 写明了分析单元、总体、抽样框，知道它们之间差在哪里
- [ ] 每个研究问题都写了"算支持"和"算否定"的标准，标准写的是差多大，不只是"显著"
- [ ] 至少写出了一个竞争解释，以及排除它的证据
- [ ] 每个研究问题都标了验证或探索；验证性的假设写在看数据之前
- [ ] 决定了要不要预注册，计划已带日期存档
- [ ] 空结果表的每一格，都能在证据清单里找到它怎么算出来

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 某个关键词怎么定义都测不了 | [收敛成项目](../01_find-a-problem/05_converge.md)第 1 节，改写主张 |
| 写"否定"标准时发现，怎样的结果你都能解释成支持 | [收敛成项目](../01_find-a-problem/05_converge.md)第 1 节，主张可能太含糊或太满 |
| 要的样本或数据拿不到，换了抽样框，结论就没意思了 | [收敛成项目](../01_find-a-problem/05_converge.md)第 5 节，重新评估可行性 |
| 空结果表里有好几格，清单里找不到怎么算 | [收敛成项目](../01_find-a-problem/05_converge.md#4-拿什么让人相信)第 4 节，重新想需要什么证据 |
| 研究问题超过十个，收不拢 | [收敛成项目](../01_find-a-problem/05_converge.md#1-写出你想证明的那句话)第 1 节，主张不够集中，先收窄 |

## 下一步

证据清单写好了，你已经知道每个问题要什么证据、怎样算回答了。下一步是决定**用什么办法拿到这些证据**：选研究套路、选研究方法。见[选方法](02_choose-method.md)。

[^easterbrook2008selecting-e15]: Easterbrook 等 2008（软件工程研究方法），§5.2。[证据](../../sources/notes/easterbrook2008selecting.md#e15)
[^easterbrook2008selecting-e31]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e31)
[^easterbrook2008selecting-e32]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e32)
[^easterbrook2008selecting-e34]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e34)
[^easterbrook2008selecting-e35]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e36]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e37]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e37)
[^easterbrook2008selecting-e39]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e39)
[^easterbrook2008selecting-e40]: Easterbrook 等 2008（软件工程研究方法），§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e40)
[^ralph2020empirical-e22]: ACM SIGSOFT（美国计算机协会软件工程分会）实证研究标准，General Standard，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e22)
[^ralph2020empirical-e27]: ACM SIGSOFT 实证研究标准，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e29]: ACM SIGSOFT 实证研究标准，Registered Reports 补充文件，Definition。[证据](../../sources/notes/ralph2020empirical.md#e29)
[^ralph2020empirical-e30]: ACM SIGSOFT 实证研究标准，Registered Reports 补充文件，Application。[证据](../../sources/notes/ralph2020empirical.md#e30)
[^ralph2020empirical-e31]: ACM SIGSOFT 实证研究标准，Registered Reports 补充文件，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e31)
[^ralph2020empirical-e32]: ACM SIGSOFT 实证研究标准，Registered Reports 补充文件，RR1 Specific Attributes。[证据](../../sources/notes/ralph2020empirical.md#e32)
[^ralph2020empirical-e34]: ACM SIGSOFT 实证研究标准，Registered Reports 补充文件，Justifying Deviations。[证据](../../sources/notes/ralph2020empirical.md#e34)
[^ralph2020empirical-e36]: ACM SIGSOFT 实证研究标准，Sampling 补充文件，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e36)
[^ralph2020empirical-e38]: ACM SIGSOFT 实证研究标准，Sampling 补充文件，Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e38)
[^ralph2020empirical-e39]: ACM SIGSOFT 实证研究标准，Sampling 补充文件，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e39)
[^ralph2020empirical-e42]: ACM SIGSOFT 实证研究标准，Sampling 补充文件，Application。[证据](../../sources/notes/ralph2020empirical.md#e42)
[^ralph2020empirical-e119]: ACM SIGSOFT 实证研究标准，Repository Mining 标准，Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e119)
[^ralph2020empirical-e176]: ACM SIGSOFT 实证研究标准，Experiments 标准，Desirable Attributes。[证据](../../sources/notes/ralph2020empirical.md#e176)
[^ernst2023registered-e1]: Ernst & Baldassarre 2023，摘要。[证据](../../sources/notes/ernst2023registered.md#e1)
[^ernst2023registered-e2]: Ernst & Baldassarre 2023，§2.1。[证据](../../sources/notes/ernst2023registered.md#e2)
[^ernst2023registered-e3]: Ernst & Baldassarre 2023，§3。[证据](../../sources/notes/ernst2023registered.md#e3)
[^runeson2009guidelines-e3]: Runeson & Höst 2009（软件工程案例研究），§5.2.3。[证据](../../sources/notes/runeson2009guidelines.md#e3)
[^flake2020measurement-e7]: Flake & Fried 2020（心理学，量表测量），Question 1。[证据](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e8]: Flake & Fried 2020（心理学，量表测量），Question 2。[证据](../../sources/notes/flake2020measurement.md#e8)
[^torchiano2017lessons-e5]: Torchiano 等 2017（软件工程问卷调查），§III-B-1。[证据](../../sources/notes/torchiano2017lessons.md#e5)
[^baltes2022sampling-e3]: Baltes & Ralph 2022（软件工程），§2.6。[证据](../../sources/notes/baltes2022sampling.md#e3)
[^baltes2022sampling-e5]: Baltes & Ralph 2022（软件工程），§2.6。[证据](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e9]: Baltes & Ralph 2022（软件工程），§6。[证据](../../sources/notes/baltes2022sampling.md#e9)
[^baltes2022sampling-e11]: Baltes & Ralph 2022（软件工程），§6。[证据](../../sources/notes/baltes2022sampling.md#e11)
[^huang2023experiments-e3]: Jia-Bin Huang 2023（计算机视觉研究者的经验），Anticipate the results。[证据](../../sources/notes/huang2023experiments.md#e3)
[^huang2023experiments-e4]: Jia-Bin Huang 2023（计算机视觉研究者的经验），Anticipate the results。[证据](../../sources/notes/huang2023experiments.md#e4)
[^bennett2012process-e10]: Bennett & Checkel 2012（政治学，过程追踪方法），第 19 页。[证据](../../sources/notes/bennett2012process.md#e10)
[^bennett2012process-e12]: Bennett & Checkel 2012（政治学，过程追踪方法），第 20 页。[证据](../../sources/notes/bennett2012process.md#e12)
[^arcuri2014hitchhiker-e6]: Arcuri & Briand 2014（软件工程，随机算法评估），§4。[证据](../../sources/notes/arcuri2014hitchhiker.md#e6)
[^arcuri2014hitchhiker-e9]: Arcuri & Briand 2014（软件工程，随机算法评估），§8。[证据](../../sources/notes/arcuri2014hitchhiker.md#e9)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019（机器学习），§1。[证据](../../sources/notes/lipton2019troubling.md#e1)
[^shaw2003writing-e12]: Shaw 2003（软件工程），§4.3。[证据](../../sources/notes/shaw2003writing.md#e12)
[^nosek2018preregistration-e1]: Nosek 等 2018（心理学等领域的开放科学讨论），Abstract。[证据](../../sources/notes/nosek2018preregistration.md#e1)
[^nosek2018preregistration-e3]: Nosek 等 2018（心理学等领域的开放科学讨论），Mental Constraints on Distinguishing Predictions and Postdictions。[证据](../../sources/notes/nosek2018preregistration.md#e3)
[^nosek2018preregistration-e4]: Nosek 等 2018（心理学等领域的开放科学讨论），Preregistration Distinguishes Prediction and Postdiction。[证据](../../sources/notes/nosek2018preregistration.md#e4)
[^nosek2018preregistration-e5]: Nosek 等 2018（心理学等领域的开放科学讨论），Challenge 1。[证据](../../sources/notes/nosek2018preregistration.md#e5)
[^nosek2018preregistration-e6]: Nosek 等 2018（心理学等领域的开放科学讨论），Challenge 6。[证据](../../sources/notes/nosek2018preregistration.md#e6)
[^nosek2018preregistration-e7]: Nosek 等 2018（心理学等领域的开放科学讨论），Making Preregistration the Norm。[证据](../../sources/notes/nosek2018preregistration.md#e7)
[^nosek2018preregistration-e8]: Nosek 等 2018（心理学等领域的开放科学讨论），Challenge 2。[证据](../../sources/notes/nosek2018preregistration.md#e8)
[^nosek2018preregistration-e9]: Nosek 等 2018（心理学等领域的开放科学讨论），Preregistration Distinguishes Prediction and Postdiction。[证据](../../sources/notes/nosek2018preregistration.md#e9)
[^simmons2018false-e2]: Simmons、Nelson & Simonsohn 2018（心理学），第 258 页。[证据](../../sources/notes/simmons2018false.md#e2)
[^he2020characterizing-e4]: He 等 2020（以太坊合约代码克隆），§5 Qualitative Analysis，第 10 页。[证据](../../sources/notes/he2020characterizing.md#e4)
[^feist2019slither-e3]: Feist 等 2019（智能合约静态分析工具 Slither），§I Introduction，第 1 页。[证据](../../sources/notes/feist2019slither.md#e3)
[^feist2019slither-e9]: Feist 等 2019（智能合约静态分析工具 Slither），§V-A2 Metrics，第 6 页。[证据](../../sources/notes/feist2019slither.md#e9)
[^durieux2020empirical-e5]: Durieux 等 2020（智能合约分析工具评测 SmartBugs），§2.3.1，第 3 页。[证据](../../sources/notes/durieux2020empirical.md#e5)
[^durieux2020empirical-e11]: Durieux 等 2020（智能合约分析工具评测 SmartBugs），§3.1，第 6 页。[证据](../../sources/notes/durieux2020empirical.md#e11)
[^rameder2022review-e2]: Rameder 等 2022（以太坊智能合约漏洞分析的系统综述），§1 Introduction，第 2 页。[证据](../../sources/notes/rameder2022review.md#e2)
