# 讲清故事，写成论文

> 本章的道理适用于各学科，例子和具体做法以计算机为例。本章的写作建议主要来自计算机研究者的经验和计算机领域的评估标准，少量来自计算生物学和统计作图的资料；它们是建议，不是各学科都必须遵守的规矩，具体以目标去处的惯例为准 `[本项目分析]`。

## 你现在在哪里

实验做完了，或者主要结果已经有了。你的文件夹里有几十张表、几百行日志、一份越来越长的笔记。研究计划里的论文提纲（见[形成研究计划](../02_do-the-project/03_research-plan.md#2-把主张拆成里程碑每个里程碑是一份证据)），有的格子填上了，有的结果和当初设想的不一样。

你可能正卡在这些地方：结果很多，不知道哪些该写、哪些该删；打开空白文档，第一句话就写不下去；引言、相关工作、局限，不知道各写到什么程度；自己读着挺清楚，不知道别人读不读得懂。

## 这一阶段要解决什么

把一堆结果写成一篇**别人读得懂、信得过、记得住**的论文。具体来说，是回答下面几个问题：

1. 这篇论文最想让读者相信的那句话是什么？
2. 全文按什么顺序讲，每一段的任务是什么？
3. 摘要、引言、相关工作、方法、结果、局限，各要讲到什么程度？
4. 图和表怎样让读者一眼看出结论？
5. 读者能不能看出你满足了这类研究的证据标准？
6. 怎样改，找谁读？

本章不讲语法和用词，也不讲各会议、期刊的格式。投到哪里、怎么投，见下一章[选择发表渠道与投稿](02_venue-and-submission.md)。

## 这一章怎么用

各节大致按写作顺序排列，但实际会来回走：写摘要时说不清核心主张，就回到第 1 节；写结果时发现某条主张没有证据，就删掉它或回去补实验（见"回退信号"） `[本项目分析]`。写作本身会暴露研究的漏洞，越早暴露越好[^eisnerfirst-e6]。

---

## 1. 找到故事：一句核心主张

**先别急着写，先回答：读者读完这篇论文，最应该相信哪一句话？**

这句话就是论文的核心主张（见[核心术语](../00_start-here/key-concepts.md#主张)；怎样用表示结果的说法写、说得多满，见[收敛成项目](../01_find-a-problem/05_converge.md#1-写出你想证明的那句话)）。一篇论文只讲一个清楚、鲜明的想法[^peytonjones2013write-e2]。手里有两个大想法，就考虑写成两篇：放在一篇里，读者只会记住一个[^black2024writing-e3]；同时主打几个贡献的论文，每个都不够有说服力[^mensh2017ten-e1]。可以是一到三条主张，但要围绕同一个主题[^nanda2025writing-e1]。

动笔时说不准没关系，写完时必须说得出来[^peytonjones2013write-e3]。还要说出让问题变得可解的那个**洞见**：它不是你的技术贡献本身，而是引出贡献的那个看法[^black2024writing-e2]。

**拿收敛阶段的一页简介对一对。** 简介里写过"希望证明的核心结论"，结果出来后它常常要改，按实际做到的东西重新表述主张是很常见的事[^shaw2003writing-e17]。怎样按证据改，见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md#7-证据和主张对不上时改主张)。例如只有两个评测集泄露严重，主张就写成"在某两个常用评测集上，泄露使准确率被明显高估"，而不是"高准确率主要来自泄露" `[本项目分析]`。

**用核心主张当筛子。** 任何不支持主线的部分，不管多正确、花了你多少力气，都删掉或改写[^ernstwrite-e9]。读者能带走的往往只有几句话，所以要主动挑出那几句[^nanda2025writing-e2]。

**两个检验：** 读者读完一年后，还能向同事说出你的主要贡献吗[^mensh2017ten-e2]？你能在几分钟内向同事讲完整篇论文的提纲吗？你讲不出，读者也不会明白[^mensh2017ten-e11]。

**写下来：** 用一句话写出核心主张，再用一句话写出背后的洞见。对照一页简介，写下主张改了什么、为什么改。

## 2. 先搭提纲，再写句子

**不要从第一句话开始写，先搭一份提纲。** 一个好用的顺序是：摘要 → 要点式提纲 → 引言 → 完整初稿，然后反复迭代[^nanda2025writing-e6]。提纲里每个计划中的段落，先用一句大白话写出它要说什么[^mensh2017ten-e21]。好的提纲紧凑精简，每一部分都在主线里有明确的作用[^nanda2025writing-e9]。

**结果部分的提纲，写成一串陈述句。** 先把"结果怎样一步步支撑主张"的逻辑理出来，写成一串陈述句，直接用作结果部分的小节标题[^mensh2017ten-e7]。

**按逻辑排，不按时间排。** 读者不关心你按什么顺序得到结果，只关心最终的主张和支撑它的逻辑[^mensh2017ten-e5]。只讲结果本身的故事，不讲你是怎么一路摸索到结果的[^widomtips-e5]。那条路"也许浸透了你的心血"，但读者不感兴趣[^peytonjones2013write-e7]。

**把力气花在读的人最多的地方。** 标题、摘要和图被看得最多，方法部分被读得最少，分配时间时要据此倾斜[^mensh2017ten-e9]。也不要按你花的时间分配篇幅：花时间最多的部分，不一定是读者最需要的[^ernstwrite-e3]。

用测量泄露的例子，一份提纲可以是这样 `[本项目分析]`：

```
核心主张：在两个常用评测集上，数据泄露使大模型漏洞检测的准确率被明显高估
1 引言：问题、为什么重要、已有评测缺什么、本文做了什么、贡献清单
2 背景与相关工作：评测集怎么建的；已有的泄露研究做到了哪里
3 怎样判断一份合约是否泄露（方法，及其准确性）
4 结果（每个小标题是一句结论）
  4.1 四个评测集中，两个有大量合约出现在模型的训练数据里
  4.2 去掉泄露样本后，这两个评测集上的准确率明显下降
  4.3 这一下降在多个模型上都出现，不是个别模型的问题
5 讨论与局限：判断泄露的方法会漏掉什么；结论适用到哪里
6 结论
```

研究计划里那份带状态的图表清单，这时正好变成结果部分的骨架。

**写下来：** 写出你的提纲：每节一行，结果部分每个小标题写成一句结论。再检查一遍：有没有哪一节说不出它在主线里的作用？

## 3. 标题和摘要：把整个故事讲完

对大多数读者来说，摘要是唯一会读的部分[^mensh2017ten-e12]，人们靠它决定读不读全文，所以摘要要把整个故事讲出来[^shaw2003writing-e23]。

**摘要按"背景—内容—结论"写**[^mensh2017ten-e15]：

| 部分 | 写什么 | 例子（示意） |
|---|---|---|
| 背景 | 从大的领域收窄到一个缺口：缺什么、为什么要紧 | 大模型漏洞检测在评测集上准确率很高，但没人确认评测合约是否已出现在训练数据里 |
| 内容 | 用了什么方法，主要结果是什么 | 我们提出一种判断泄露的方法，检查了四个常用评测集…… |
| 结论 | 回答开头的问题；对领域意味着什么 | 现有结果中有一部分被高估，评测时应先排除泄露样本 |

摘要最常见的错误，是在读者还没准备好理解时就谈结果[^mensh2017ten-e16]。另一个常见错误是只说"研究了什么"，不说"发现了什么"：要一开始就把整个故事讲出来，不要有所保留[^raibert1985good-e3]。标题则是对贡献的最终提炼，尽早想一个，写作中反复打磨[^mensh2017ten-e17]。

**写下来：** 按上面三行写一版摘要，每行一两句。读给一个不了解这个项目的同学听，问他：这篇论文发现了什么？

## 4. 引言：五个问题，加一份贡献清单

对新手来说，引言往往是最难写的部分[^huang2023introduction-e1]。审稿人读完引言时，多半已经有了初步判断[^widomtips-e1][^black2024writing-e1]。

**怎么写：** 一个好用的写法是：没有特别理由时，引言写五段，回答五个问题[^widomtips-e2][^widomtips-e8]：

1. **问题是什么？** 最好用一个具体例子引出[^peytonjones2013write-e13]。
2. **为什么有趣、重要？**
3. **为什么难？** 比如简单的做法为什么不行。
4. **为什么以前没解决？** 已有方案哪里不够好，你的有什么不同。要说清楚已有方案为什么不令人满意[^huang2023introduction-e2]。如果能放一张图，用一个具体例子展示已有工作的核心问题，效果最好[^huang2023introduction-e5]。
5. **你的方法和结果的关键是什么？** 包括具体的局限。引言最后一段简要概括结果，说明它们怎样填补了前面提出的缺口[^mensh2017ten-e18]。

**然后列出贡献清单。** 用列表写出主要贡献，注明各在哪一节[^widomtips-e3]。整篇论文就是在证实这份清单[^peytonjones2013write-e4]。贡献（这项研究给领域增加的新东西，见[核心术语](../00_start-here/key-concepts.md#贡献)）是论文之前世界不知道、因为这篇论文现在知道了的东西[^vandeursen2013writing-e1]；它是成果，不是付出的努力[^vandeursen2013writing-e2]。每条贡献要具体到可以被检验[^peytonjones2013write-e5]。下表的数字和说法都是示意 `[本项目分析]`：

| 写成努力（不好） | 写成成果（好） |
|---|---|
| "我们收集了 2 万份合约，测试了 5 个模型" | "我们发现，四个常用评测集中有两个，大量合约出现在模型的训练数据里（第 4.1 节）" |
| "我们设计了一个泄露检测流程" | "我们给出一种判断合约是否泄露的方法，在人工核对的样本上与人工判断基本一致（第 3 节）" |

**把新的和旧的分开。** 你做的东西不全是新的，很大一部分可能建立在已有方法上，所以要明确写出哪些是你的贡献[^huang2023introduction-e4]，并把背景材料和自己的贡献分开[^vandeursen2013writing-e3]。尤其在引言和相关工作里，要非常清楚哪些是新的、哪些不是[^nanda2025writing-e7]。引言里不写泛泛的文献综述，只写和动机有关的部分[^mensh2017ten-e6]。

> **学科差异**：逐条列贡献、注明节号，以及"读到第 3 页就该看到一个清楚的新贡献"[^widomtips-e6]，都来自计算机研究者的写作建议。`[本项目分析]` 它们主要是计算机和工程类会议论文的惯例。很多期刊和学科有固定结构，不一定逐条列贡献。但"读者很快能看出你新在哪里"各学科都适用。动笔前先看目标去处近期论文的写法。

**写下来：** 按五个问题各写一两句。再写出贡献清单，每条以"我们发现 / 我们证明 / 我们给出"开头，并注明在第几节。

## 5. 相关工作：说清你站在哪里

相关工作不是为了证明"我读过很多论文"，而是说明你的工作和已有工作是什么关系：是在它们的基础上推进，还是提供了另一种做法[^shaw2003writing-e1]。不讲清这一点，审稿人就看不出你增加了什么新知识；看不出你是否了解相关工作，还会损害你的可信度[^shaw2003writing-e4]。

**写成具体的对比，不写成一串引用。** 差的写法是"这个问题受到了广泛关注 [3,8,10,18,26]"或"A 和 B 研究过这个问题"[^shaw2003writing-e2]；好的写法具体说出每项工作做到了多少、限制在哪、你在哪一点上不同[^shaw2003writing-e3]。你在[收敛成项目](../01_find-a-problem/05_converge.md#3-别人做过了吗)里画过的对比表，正是这样的内容，相关工作一节就是把它写成文字 `[本项目分析]`。

- **选适量的工作，做综合而不是罗列。** 不必列出每一篇相关研究[^ralph2020empirical-e19]。把工作按思路分组，每一组都落到你自己的工作上，说清你的贡献和它们是什么关系[^ralph2020empirical-e20]。在合约例子里，可以按"怎样建漏洞评测集""已有的泄露检查做到了哪里""大模型漏洞检测的评测做法"分三组，每组最后一句都落到"本文在这一点上不同" `[本项目分析]`。
- **不要只为了说"不相关"而提一项工作，也不要只罗列不综合**[^ralph2020empirical-e21]。
- **大方地给别人功劳。** 承认别人的贡献，不会减少你的功劳[^peytonjones2013write-e11]。

> **不同的看法：相关工作放前面还是后面？**
>
> - 放后面：先讲别人的做法，会挡在读者和你的想法之间[^peytonjones2013write-e8]。
> - 看情况，两种都行：能写得短而具体、或必须一开始就和已有工作划清界限时放前面[^widomtips-e4]；能在引言里先简短概括、或要讲清比较必须先讲完技术内容时放后面[^widomtips-e9]。
>
> 两种做法都要求在引言里说清和最相关工作的区别[^nanda2025writing-e7]。`[本项目分析]` 先看目标去处的惯例，再问自己：读者需不需要先懂你的方法，才看得懂这些比较？

**写下来：** 把对比表改写成两三段相关工作，每段最后一句写"本文在这一点上不同"。

## 6. 方法与结果：写成别人能检查的样子

**方法：先给直觉，再给细节。** 传达直觉是首要的，不是次要的[^peytonjones2013write-e9]。可以先用一个具体合约走一遍你的判断流程，再给完整定义 `[本项目分析]`。细节要写到别人能重做的程度。软件工程实证研究标准对基准评测类研究的必要要求之一，是把实验设置写到足以让别人独立重做[^ralph2020empirical-e148]。一篇梳理系统安全方向评测缺陷的综述，列出的常见遗漏包括：硬件平台、软件版本、各子项的结果[^vanderkouwe2019sok-e13]。大模型方向还要写清模型版本、调用时间和提示原文 `[本项目分析]`。

**结果：每段回答一个问题。** 每段开头一两句提出这段要回答的问题，中间给数据和推理，最后一句给出答案。这样读者容易找到可疑的结论出在哪一段，并检查那一段的逻辑[^mensh2017ten-e20]。

**每条主张都指向证据。** 逐条检查引言里的主张，找到支撑它的证据，并在主张处注明证据在哪一节[^peytonjones2013write-e6]。证据要对得上主张：主张性能提升，就要分析性能，而不是易用性[^shaw2003writing-e12]。

**把分析阶段核对过的说法原样搬进论文。** 主张说得多满、需要多强的证据，见[收敛成项目](../01_find-a-problem/05_converge.md#1-写出你想证明的那句话)；结果怎样报告（差多少、多确定、不只报最好的一次），见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)；结论能说到多远、怎样把推测和证据分开，见同一章[第 6 节](../02_do-the-project/07_analyze-and-interpret.md#6-结论能说到多远)。写作时最容易犯的，是在润色时又把话说满了 `[本项目分析]`。表格里给出各子项的结果，不要只给总分[^heiserbenchmarking-e18]；给相对数时也给绝对数，读者才能判断配置是否合理[^vanderkouwe2019sok-e23]。少用"新颖""显著""最好"这类自我评价，给出事实，让读者自己判断[^ernstwrite-e7]。

**写下来：** 把引言里的每条主张抄成一列，旁边写出支撑它的图、表或小节。找不到对应证据的主张，删掉或改弱。

## 7. 图和表：标题说结论，图注说做法

很多读者看完摘要就直接看图。所以**图的标题要说出分析的结论，图注要说明是怎么做的**[^mensh2017ten-e19]。例如不写"图 3：各模型准确率"，而写"图 3：去掉泄露样本后，两个评测集上的准确率都明显下降" `[本项目分析]`。

**图注里必须交代**误差线是什么（标准差、标准误，还是置信区间）[^cumming2007error-e1]，以及样本量 n，即独立重复的次数[^cumming2007error-e2]。

**让读者看到数据本身。** 均值加误差线的柱状图，可能掩盖数据的真实分布：很多不同的分布会画出一模一样的柱状图[^weissgerber2015beyond-e1]。数据点很少时，最好把每个点都画出来[^weissgerber2015beyond-e3][^cumming2007error-e5]。画标准误而不画标准差，会在视觉上放大组间差异[^weissgerber2015beyond-e5]。只报平均数或中位数可能误导读者，要同时报告分布[^blackburn2018sigplan-e8]。配色也要让所有人都读得出：亮度相近的红绿配色，有很大一部分读者读不出来[^crameri2020misuse-e4]。

**还可以有一张"为什么"的图。** 引言里放一张图，用一个具体例子展示已有工作的核心问题[^huang2023introduction-e5]。在合约例子里，可以把一份评测合约和模型训练数据里几乎一模一样的那份并排放 `[本项目分析]`。

**从计划阶段的空表出发。** 如果你在计划阶段画过空的结果表，并写好了行列标题和说明[^eisnerfirst-e5]，现在是把它们填满、再按"标题说结论"改一遍的时候 `[本项目分析]`。

**写下来：** 给论文的每张图表写一句"标题结论"。检查每张图注：误差线是什么、n 是多少，写了没有。

## 8. 讨论与局限：诚实地说清做到了哪里

**讨论部分做三件事：** 说明结果怎样填补了引言里提出的缺口；说明解释结果时要注意什么；说明论文怎样推进了这个领域[^mensh2017ten-e8]。后面的段落，每段讲论文的一个弱点或长处，并结合相关文献评价它[^mensh2017ten-e22]。

**局限要写，而且要写真正相关的。** ACM 软件工程分会的实证研究标准把"披露所有主要局限"列为必须做到的[^ralph2020empirical-e18]，把"说明为考察或减轻局限做了哪些合理的尝试"列为加分项[^ralph2020empirical-e51]。只写无关紧要的局限为什么会误导，见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md#6-结论能说到多远)。

**怎样找到真正的局限：** 从设计阶段写下的局限清单出发（见[效度与局限：设计阶段就想清楚](../02_do-the-project/04_validity-and-limits.md#8-现在就写下局限定下诚实报告的规矩)），再问自己：假设自己错了，错在哪[^nanda2025writing-e4]？在合约例子里，可以问：判断泄露的方法会漏掉什么，改写过变量名的合约算不算泄露？训练数据不公开的模型，你是怎么判断的？只看了四个评测集、某几个模型，结论能推广到哪里 `[本项目分析]`？

**局限和结论要一致。** 不要在局限里承认抽样偏差，到结论又说结果几乎普遍适用[^baltes2022sampling-e9]。既不要夸大，也不要贬低自己的结果[^zhang2014ten-e4]。

**写下来：** 写出三条你认为最真实的局限，每条写清：它会怎样影响结论，你做了什么来减轻它。再回头读结论，看有没有一句话超出了局限允许的范围。

## 9. 让套路的证据标准看得见

不同的研究套路（这个项目主要靠什么逻辑产生新知识，见[核心术语](../00_start-here/key-concepts.md#研究套路)），读者用来判断"够不够"的标准不同。写作时要让读者**一眼看出你交的是哪一种知识，以及你满足了它的标准**。如果审稿人分不清你是提出了新的评估技术、把旧技术用在新例子上，还是在评估一项成熟技术，说明你没写清楚[^shaw2003writing-e31]。

每种套路要求什么证据，写在各套路说明的"什么样的证据才够"一节：[观察描述](../05_research-strategies/observe_describe.md#2-什么样的证据才够)、[测量](../05_research-strategies/measure.md#2-什么样的证据才够)、[比较评估](../05_research-strategies/compare_evaluate.md#2-什么样的证据才够)、[解释因果](../05_research-strategies/explain_causality.md#2-什么样的证据才够)、[构建改进](../05_research-strategies/build_improve.md#2-什么样的证据才够)、[综合](../05_research-strategies/synthesize.md#2-什么样的证据才够)、[证明](../05_research-strategies/prove.md#2-什么样的证据才够)。写完后，用你那一种逐条对照论文，让每一条要求在论文里都有一个明确的位置：哪一节、哪张图表，而不是散在各处让读者自己拼 `[本项目分析]`。我们的例子属于测量：主张是"现有评测高估了准确率"。读者最先会问的是"你判断泄露的方法可靠吗"，所以第 3 节要单独证明这一点，而不是只在附录里一笔带过 `[本项目分析]`。

**写下来：** 写出你的论文属于哪种套路。打开那一篇套路说明，列出它要求的证据，在每一条旁边写上：论文第几节、哪张图表满足了它。

## 10. 修改，并请人读

**接受初稿是坏的。** 好文字就是先写出坏东西，再把它改好[^raibert1985good-e1]；同样的字句改十几遍是常事[^raibert1985good-e2]。所有好论文都是从坏论文开始的[^black2024writing-e5]。写不出来时，先写点东西，以后再改[^ernstwrite-e8]。

**敢删。** 整段删掉重写，常常比一点点改更快[^mensh2017ten-e10]。让每个字都有用[^ernstwrite-e10]。改的时候，先完全站在审稿人的位置，仔细检查每一部分[^zhang2014ten-e5]。

**再请别人读。** 你在项目里泡了几个月，很容易以为读者也懂，这叫"透明错觉"[^nanda2025writing-e5]。只有别人的反馈能帮你发现 `[本项目分析]`。

- **珍惜读者。** 每个读者只能"第一次读"你的论文一次[^peytonjones2013write-e10]；读过一遍的人，再读时已经知道你要说什么[^raibert1985good-e6]。所以按阶段请不同的人读 `[本项目分析]`。
- **问对问题。** 请读者告诉你"读到哪里看不懂了"，这比挑错字重要得多 `[本项目分析]`。
- **相信读者的困惑。** 读者说看不懂，不要争辩，去改那一部分[^raibert1985good-e4]。反馈很笼统、读者不太兴奋，往往说明他们没抓住主线[^mensh2017ten-e14]。
- **互相帮忙。** 主动帮别人读初稿[^vandeursen2013writing-e5]。

投稿前的最后一遍检查（校对、提前回答审稿人会问的问题、留出内部截止日期），见[选择发表渠道与投稿](02_venue-and-submission.md#5-投稿前最后一遍检查)。

**为什么值得花这些力气。** 论文是一对多的：解释的成本你只付一次，看不懂的成本每个读者都要付[^olah2017debt-e1]。有计算机研究者甚至建议，对能否被接收来说，清楚的动机和表述比结果更重要[^eisnerfirst-e9]。

> **不同的看法：摘要和引言先写还是最后写？**
>
> - 有人习惯最后写，因为那时正文已经完成，照着描述就行[^ernstwrite-e11]。
> - 另一些人主张早写：摘要和引言框定了整篇论文，早写再按需修改[^ernstwrite-e6]；甚至可以在有结果之前写引言[^black2024writing-e4]。
>
> `[本项目分析]` 对新手，建议早写一个粗糙版，用来检验思路、和导师讨论；正文完成后，按实际结果再重写一遍。

**写下来：** 列出两三位可以请来读稿的人，写下每人在哪个阶段读、请他重点看什么。每轮反馈后，记下改了什么。

---

## 关键判断

**结果和原来的主张对不上，改主张还是补实验？** `[本项目分析]`

| 情况 | 通常的做法 |
|---|---|
| 结果支持一个更窄的主张 | 改主张，写你真正做到的 |
| 缺一个关键实验，主张就站不住 | 回去补；补不了就删掉依赖它的主张 |
| 结果和预期相反，但证据扎实 | 围绕新发现重写故事 |
| 两条主线都有证据，但彼此无关 | 拆成两篇，或者只写一条 |

**哪些东西放正文，哪些放附录或删掉？** 问一句：它支撑核心主张吗？支撑的放正文；读者核对证据时需要、但不影响主线的放附录；都不是的删掉 `[本项目分析]`。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 一篇塞进好几个大想法 | 每个都不够有说服力，读者只会记住一个[^mensh2017ten-e1][^black2024writing-e3] |
| 把工作量当贡献 | 贡献是成果，不是努力[^vandeursen2013writing-e2] |
| 摘要只说"研究了什么" | 摘要要讲完整个故事[^shaw2003writing-e23][^raibert1985good-e3] |
| 相关工作写成"A 做了 X，B 做了 Y" | 读者看不出你的工作和它们的关系[^ralph2020empirical-e21] |
| 润色时把主张写得比证据强 | 越强的说法需要越高的证据标准[^nanda2025writing-e3] |
| 只给总分 | 往坏处说会掩盖问题，往好处说也让读者少看到很多信息[^heiserbenchmarking-e18] |
| 图标题只写"各模型准确率" | 很多读者只看图，标题要说出结论[^mensh2017ten-e19] |
| 局限里承认，结论里忘掉 | 软件工程实证研究标准列出的反面做法[^ralph2020empirical-e66] |
| 读者说看不懂时和他争辩 | 应当相信读者的困惑，去改[^raibert1985good-e4] |

## 产出物

- 一句核心主张，以及它相对一页简介的改动说明（第 1 节）
- 论文提纲，结果部分的小标题都是陈述句（第 2 节）
- 完整初稿：摘要、引言及贡献清单、相关工作、方法、结果、讨论与局限
- 一张"主张—证据"对照表（第 6 节），以及按套路标准对照的检查结果（第 9 节）
- 至少一轮他人反馈，以及按反馈修改的记录（第 10 节）

## 检查点

满足下面几条，可以进入下一步：

- [ ] 能用一句话说出核心主张，用的是表示结果的说法
- [ ] 摘要讲完了背景、内容、结论，包括发现了什么
- [ ] 引言回答了五个问题，贡献清单每条都是成果、注明了小节
- [ ] 相关工作说清了每组工作和本文的关系，没有逐篇罗列
- [ ] 每条主张都能指到具体的图、表或小节，强度和证据相称
- [ ] 每张图的标题说出了结论，图注写明了误差线和 n
- [ ] 写了真正相关的局限，结论没有超出局限允许的范围
- [ ] 对照所属套路的证据标准检查过一遍
- [ ] 至少一位没读过这篇稿子的人读过，并按他的困惑改过

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 写作中发现缺一个关键实验，主张站不住 | [执行与迭代](../02_do-the-project/06_run-and-iterate.md)，补实验 |
| 怎么写都说不清结果意味着什么 | [分析与解读](../02_do-the-project/07_analyze-and-interpret.md)，重新解读结果 |
| 说不出和最接近工作的区别，或写作时发现别人已发表 | [收敛成项目](../01_find-a-problem/05_converge.md#3-别人做过了吗) |
| 局限一节写下来，发现证据撑不起任何有意思的主张 | [效度与局限：设计阶段就想清楚](../02_do-the-project/04_validity-and-limits.md)，先和导师一起判断还能主张什么 |

## 下一步

初稿改到检查点都满足后，下一步是决定投到哪里、按那里的要求整理稿件并提交，见[选择发表渠道与投稿](02_venue-and-submission.md)。收到审稿意见后怎样回复和修改，见[审稿意见、修改与被拒之后](03_review-and-revision.md)。

[^peytonjones2013write-e2]: Peyton Jones 2013，幻灯片 "The idea"。[证据](../../sources/notes/peytonjones2013write.md#e2)
[^peytonjones2013write-e3]: Peyton Jones 2013，幻灯片 "The idea"。[证据](../../sources/notes/peytonjones2013write.md#e3)
[^peytonjones2013write-e4]: Peyton Jones 2013，幻灯片 "State your contributions"。[证据](../../sources/notes/peytonjones2013write.md#e4)
[^peytonjones2013write-e5]: Peyton Jones 2013，幻灯片 "Contributions should be refutable"。[证据](../../sources/notes/peytonjones2013write.md#e5)
[^peytonjones2013write-e6]: Peyton Jones 2013，幻灯片 "Evidence"。[证据](../../sources/notes/peytonjones2013write.md#e6)
[^peytonjones2013write-e7]: Peyton Jones 2013，幻灯片 "Putting the reader first"。[证据](../../sources/notes/peytonjones2013write.md#e7)
[^peytonjones2013write-e8]: Peyton Jones 2013，幻灯片 "Related work"。[证据](../../sources/notes/peytonjones2013write.md#e8)
[^peytonjones2013write-e9]: Peyton Jones 2013，幻灯片 "Presenting the idea"。[证据](../../sources/notes/peytonjones2013write.md#e9)
[^peytonjones2013write-e10]: Peyton Jones 2013，幻灯片 "Getting help"。[证据](../../sources/notes/peytonjones2013write.md#e10)
[^peytonjones2013write-e11]: Peyton Jones 2013，幻灯片 "Credit"。[证据](../../sources/notes/peytonjones2013write.md#e11)
[^peytonjones2013write-e13]: Peyton Jones 2013，幻灯片 "Describe the problem"。[证据](../../sources/notes/peytonjones2013write.md#e13)
[^mensh2017ten-e1]: Mensh & Kording 2017，Rule 1。[证据](../../sources/notes/mensh2017ten.md#e1)
[^mensh2017ten-e2]: Mensh & Kording 2017，Rule 1。[证据](../../sources/notes/mensh2017ten.md#e2)
[^mensh2017ten-e5]: Mensh & Kording 2017，Rule 3。[证据](../../sources/notes/mensh2017ten.md#e5)
[^mensh2017ten-e6]: Mensh & Kording 2017，Rule 6。[证据](../../sources/notes/mensh2017ten.md#e6)
[^mensh2017ten-e7]: Mensh & Kording 2017，Rule 7。[证据](../../sources/notes/mensh2017ten.md#e7)
[^mensh2017ten-e8]: Mensh & Kording 2017，Rule 8。[证据](../../sources/notes/mensh2017ten.md#e8)
[^mensh2017ten-e9]: Mensh & Kording 2017，Rule 9。[证据](../../sources/notes/mensh2017ten.md#e9)
[^mensh2017ten-e10]: Mensh & Kording 2017，Rule 10。[证据](../../sources/notes/mensh2017ten.md#e10)
[^mensh2017ten-e11]: Mensh & Kording 2017，Rule 10。[证据](../../sources/notes/mensh2017ten.md#e11)
[^mensh2017ten-e12]: Mensh & Kording 2017，Rule 5。[证据](../../sources/notes/mensh2017ten.md#e12)
[^mensh2017ten-e14]: Mensh & Kording 2017，Rule 10。[证据](../../sources/notes/mensh2017ten.md#e14)
[^mensh2017ten-e15]: Mensh & Kording 2017，Rule 5。[证据](../../sources/notes/mensh2017ten.md#e15)
[^mensh2017ten-e16]: Mensh & Kording 2017，Rule 5。[证据](../../sources/notes/mensh2017ten.md#e16)
[^mensh2017ten-e17]: Mensh & Kording 2017，Rule 1。[证据](../../sources/notes/mensh2017ten.md#e17)
[^mensh2017ten-e18]: Mensh & Kording 2017，Rule 6。[证据](../../sources/notes/mensh2017ten.md#e18)
[^mensh2017ten-e19]: Mensh & Kording 2017，Rule 7。[证据](../../sources/notes/mensh2017ten.md#e19)
[^mensh2017ten-e20]: Mensh & Kording 2017，Rule 7。[证据](../../sources/notes/mensh2017ten.md#e20)
[^mensh2017ten-e21]: Mensh & Kording 2017，Rule 9。[证据](../../sources/notes/mensh2017ten.md#e21)
[^mensh2017ten-e22]: Mensh & Kording 2017，Rule 8。[证据](../../sources/notes/mensh2017ten.md#e22)
[^widomtips-e1]: Widom 2006，The Introduction。[证据](../../sources/notes/widomtips.md#e1)
[^widomtips-e2]: Widom 2006，The Introduction。[证据](../../sources/notes/widomtips.md#e2)
[^widomtips-e3]: Widom 2006，The Introduction。[证据](../../sources/notes/widomtips.md#e3)
[^widomtips-e4]: Widom 2006，Related Work。[证据](../../sources/notes/widomtips.md#e4)
[^widomtips-e5]: Widom 2006，The Body。[证据](../../sources/notes/widomtips.md#e5)
[^widomtips-e6]: Widom 2006，The Body。[证据](../../sources/notes/widomtips.md#e6)
[^widomtips-e8]: Widom 2006，The Introduction。[证据](../../sources/notes/widomtips.md#e8)
[^widomtips-e9]: Widom 2006，Related Work。[证据](../../sources/notes/widomtips.md#e9)
[^huang2023introduction-e1]: Huang 2023，推文串开头。[证据](../../sources/notes/huang2023introduction.md#e1)
[^huang2023introduction-e2]: Huang 2023，推文串 Q1–Q3。[证据](../../sources/notes/huang2023introduction.md#e2)
[^huang2023introduction-e4]: Huang 2023，推文串 Q5。[证据](../../sources/notes/huang2023introduction.md#e4)
[^huang2023introduction-e5]: Huang 2023，推文串 WHY 图部分。[证据](../../sources/notes/huang2023introduction.md#e5)
[^shaw2003writing-e1]: Shaw 2003，§3.3。[证据](../../sources/notes/shaw2003writing.md#e1)
[^shaw2003writing-e2]: Shaw 2003，§3.3 示例。[证据](../../sources/notes/shaw2003writing.md#e2)
[^shaw2003writing-e3]: Shaw 2003，§3.3 示例。[证据](../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e4]: Shaw 2003，§3.3。[证据](../../sources/notes/shaw2003writing.md#e4)
[^shaw2003writing-e12]: Shaw 2003，§4.3。[证据](../../sources/notes/shaw2003writing.md#e12)
[^shaw2003writing-e17]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e17)
[^shaw2003writing-e23]: Shaw 2003，§6。[证据](../../sources/notes/shaw2003writing.md#e23)
[^shaw2003writing-e31]: Shaw 2003，§2.3。[证据](../../sources/notes/shaw2003writing.md#e31)
[^nanda2025writing-e1]: Nanda 2025，TL;DR。[证据](../../sources/notes/nanda2025writing.md#e1)
[^nanda2025writing-e2]: Nanda 2025，Crafting a Narrative。[证据](../../sources/notes/nanda2025writing.md#e2)
[^nanda2025writing-e3]: Nanda 2025，Crafting a Narrative。[证据](../../sources/notes/nanda2025writing.md#e3)
[^nanda2025writing-e4]: Nanda 2025，Rigorous Supporting Evidence。[证据](../../sources/notes/nanda2025writing.md#e4)
[^nanda2025writing-e5]: Nanda 2025，The Writing Process。[证据](../../sources/notes/nanda2025writing.md#e5)
[^nanda2025writing-e6]: Nanda 2025，TL;DR。[证据](../../sources/notes/nanda2025writing.md#e6)
[^nanda2025writing-e7]: Nanda 2025，Novelty。[证据](../../sources/notes/nanda2025writing.md#e7)
[^nanda2025writing-e9]: Nanda 2025，Iteratively Expand。[证据](../../sources/notes/nanda2025writing.md#e9)
[^black2024writing-e1]: Black 2024，Introduction。[证据](../../sources/notes/black2024writing.md#e1)
[^black2024writing-e2]: Black 2024，The Nugget。[证据](../../sources/notes/black2024writing.md#e2)
[^black2024writing-e3]: Black 2024，How to tell a story: Goal, Problem, Solution。[证据](../../sources/notes/black2024writing.md#e3)
[^black2024writing-e4]: Black 2024，Number one writing tip。[证据](../../sources/notes/black2024writing.md#e4)
[^black2024writing-e5]: Black 2024，Number one writing tip。[证据](../../sources/notes/black2024writing.md#e5)
[^ernstwrite-e3]: Ernst，Which details to include。[证据](../../sources/notes/ernstwrite.md#e3)
[^ernstwrite-e6]: Ernst，Make the organization and results clear。[证据](../../sources/notes/ernstwrite.md#e6)
[^ernstwrite-e7]: Ernst，Writing style。[证据](../../sources/notes/ernstwrite.md#e7)
[^ernstwrite-e8]: Ernst，Getting started。[证据](../../sources/notes/ernstwrite.md#e8)
[^ernstwrite-e9]: Ernst，Which details to include。[证据](../../sources/notes/ernstwrite.md#e9)
[^ernstwrite-e10]: Ernst，Brevity。[证据](../../sources/notes/ernstwrite.md#e10)
[^ernstwrite-e11]: Ernst，Make the organization and results clear。[证据](../../sources/notes/ernstwrite.md#e11)
[^raibert1985good-e1]: Raibert 1985，开头。[证据](../../sources/notes/raibert1985good.md#e1)
[^raibert1985good-e2]: Raibert 1985，Good Writing is Bad Writing That Was Rewritten。[证据](../../sources/notes/raibert1985good.md#e2)
[^raibert1985good-e3]: Raibert 1985，Spill the Beans Fast。[证据](../../sources/notes/raibert1985good.md#e3)
[^raibert1985good-e4]: Raibert 1985，Trust Your Readers。[证据](../../sources/notes/raibert1985good.md#e4)
[^raibert1985good-e6]: Raibert 1985，Husband Your Readers。[证据](../../sources/notes/raibert1985good.md#e6)
[^vandeursen2013writing-e1]: van Deursen 2013，Identify the Contributions。[证据](../../sources/notes/vandeursen2013writing.md#e1)
[^vandeursen2013writing-e2]: van Deursen 2013，Identify the Contributions。[证据](../../sources/notes/vandeursen2013writing.md#e2)
[^vandeursen2013writing-e3]: van Deursen 2013，Structure the Paper。[证据](../../sources/notes/vandeursen2013writing.md#e3)
[^vandeursen2013writing-e5]: van Deursen 2013，Share Contributions Early。[证据](../../sources/notes/vandeursen2013writing.md#e5)
[^zhang2014ten-e4]: Zhang 2014，Rule 8。[证据](../../sources/notes/zhang2014ten.md#e4)
[^zhang2014ten-e5]: Zhang 2014，Rule 8。[证据](../../sources/notes/zhang2014ten.md#e5)
[^eisnerfirst-e5]: Eisner 2010，What needs to be done?。[证据](../../sources/notes/eisnerfirst.md#e5)
[^eisnerfirst-e6]: Eisner 2010，What needs to be done?。[证据](../../sources/notes/eisnerfirst.md#e6)
[^eisnerfirst-e9]: Eisner 2010，Clear writing increases your odds of acceptance。[证据](../../sources/notes/eisnerfirst.md#e9)
[^olah2017debt-e1]: Olah & Carter 2017，Interpretive Labor。[证据](../../sources/notes/olah2017debt.md#e1)
[^ralph2020empirical-e18]: ACM SIGSOFT 实证研究标准，General Standard，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e18)
[^ralph2020empirical-e19]: ACM SIGSOFT 实证研究标准，General Standard，Desirable Attributes。[证据](../../sources/notes/ralph2020empirical.md#e19)
[^ralph2020empirical-e20]: ACM SIGSOFT 实证研究标准，General Standard，Desirable Attributes。[证据](../../sources/notes/ralph2020empirical.md#e20)
[^ralph2020empirical-e21]: ACM SIGSOFT 实证研究标准，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e21)
[^ralph2020empirical-e51]: ACM SIGSOFT 实证研究标准，Desirable Attributes。[证据](../../sources/notes/ralph2020empirical.md#e51)
[^ralph2020empirical-e66]: ACM SIGSOFT 实证研究标准，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e148]: ACM SIGSOFT 实证研究标准，Benchmarking Standard，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e148)
[^baltes2022sampling-e9]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e9)
[^heiserbenchmarking-e18]: Heiser，Benchmarking Crimes，Missing sub-benchmark results。[证据](../../sources/notes/heiserbenchmarking.md#e18)
[^vanderkouwe2019sok-e13]: van der Kouwe 等人 2019，§II，表 I。[证据](../../sources/notes/vanderkouwe2019sok.md#e13)
[^vanderkouwe2019sok-e23]: van der Kouwe 等人 2019，§II-F。[证据](../../sources/notes/vanderkouwe2019sok.md#e23)
[^blackburn2018sigplan-e8]: SIGPLAN 实证评估清单，Adequate Data Analysis。[证据](../../sources/notes/blackburn2018sigplan.md#e8)
[^cumming2007error-e1]: Cumming 等人 2007，Rule 1。[证据](../../sources/notes/cumming2007error.md#e1)
[^cumming2007error-e2]: Cumming 等人 2007，Rule 2。[证据](../../sources/notes/cumming2007error.md#e2)
[^cumming2007error-e5]: Cumming 等人 2007，Rule 4。[证据](../../sources/notes/cumming2007error.md#e5)
[^weissgerber2015beyond-e1]: Weissgerber 等人 2015，Introduction。[证据](../../sources/notes/weissgerber2015beyond.md#e1)
[^weissgerber2015beyond-e3]: Weissgerber 等人 2015，Recommendations for a New Data Presentation Paradigm。[证据](../../sources/notes/weissgerber2015beyond.md#e3)
[^weissgerber2015beyond-e5]: Weissgerber 等人 2015，Are Your Figures Worth a Thousand Words?。[证据](../../sources/notes/weissgerber2015beyond.md#e5)
[^crameri2020misuse-e4]: Crameri 等人 2020，引言。[证据](../../sources/notes/crameri2020misuse.md#e4)
