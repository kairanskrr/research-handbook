# 构建改进

> 本页讲的道理适用于各学科，例子和具体做法以计算机为例。

你想做出一个比现有的更好的东西：一个新方法、新工具、新系统，或者一种新的教学设计、新的合成路线。这一页帮你想清楚三件事：这类研究最后要交出什么，审稿人要看到什么才会信，以及它会怎样决定你项目里每一步怎么走。

术语（主张、贡献、证据、研究套路、研究方法）的意思，见[核心术语](../00_start-here/key-concepts.md)。

---

## 1. 这类研究产生什么知识

**核心主张是"我做出了一个更好的东西，而且它更好是有证据的"。** 用贯穿全书的例子：

> "我们的新方法在真实智能合约上，比现有工具多发现三成漏洞，误报不增加。"

这句话包含两样东西：一个新的**制品**（这里是一种漏洞检测方法），以及它比现有做法更好的**证据**。只交出东西、没有证据，是产品开发；只有比较、没有新东西，是[比较评估](compare_evaluate.md) `[本项目分析]`。

**它回答的是"设计问题"。** 知识问题问"世界是什么样的"；设计问题问"怎样更好地做一件事"，形式是"实现 X 的有效办法是什么？""什么策略有助于实现 X？"在软件工程里，大多数非实证研究关心的就是设计问题[^easterbrook2008selecting-e28]。软件工程的研究问题分类里，对应的写法是"怎样做到（或自动做到）X？做 X 有没有更好的办法？"[^shaw2003writing-e25]。软件工程的评审标准（ACM SIGSOFT，即美国计算机协会软件工程分会制定的实证研究标准）把这类研究叫"工程研究"，即"发明并评估技术制品的研究"[^ralph2020empirical-e79]；制品可以是算法、模型、语言、方法、系统、工具等[^ralph2020empirical-e80]。

**和相近的套路怎么分** `[本项目分析]`：

| 你的核心主张 | 套路 |
|---|---|
| "新方法比现有工具多发现三成漏洞" | 构建改进 |
| "在真实合约上，工具 A 的检出率高于 B"（A、B 都是别人的） | [比较评估](compare_evaluate.md) |
| "提供漏洞模式提示会提高检出率" | [解释因果](explain_causality.md) |
| "我们把现有工具用在某公司的合约上，经验如下" | 经验报告，不属于构建改进 |

分界的关键是：被比较的东西里有没有你**自己新做的**。只比较别人的工具，是比较评估，两者的区别详见[比较评估](compare_evaluate.md#1-这类研究产生什么知识)。软件工程的评审标准也明确，只评估已有方法的研究、只报告应用已有方法经验的研究，都不按工程研究的标准评[^ralph2020empirical-e80]。一个项目常常既有新方法、又有新数据集，按核心主张定主要套路，其他作为次要贡献，见[核心术语](../00_start-here/key-concepts.md#研究套路)。

**它以"对问题足够了解"为前提。** 设计问题假定相关的知识问题已经回答过，你对要解决的问题已经有足够了解[^easterbrook2008selecting-e29]。如果你还说不清现有工具**为什么**漏报、误报，可能要先做一轮[观察描述](observe_describe.md)，再来构建 `[本项目分析]`。在软件工程里，长期的研究计划通常是设计问题和知识问题交替出现[^easterbrook2008selecting-e29]。

**东西之外，最好还交出"为什么有效"的认识。** 教育学里的基于设计的研究（在真实课堂里一轮轮设计、试用、改进教学干预的研究），学界普遍认为它既要产出有效的教学干预，也要产出有用的理论[^easterday2014design-e1]；只靠反复试用、改进原型来做教学材料，没有理论产出，就不算这类研究[^bakker2015introduction-e3]。机器学习方向也有类似的建议：不只问"效果多好"，还要问"什么起了作用、为什么"[^lipton2019troubling-e7]。

## 2. 什么样的证据才够

审稿人读一篇构建改进的论文，心里大致在问下面六个问题 `[本项目分析]`。表里的出处多来自软件工程和机器学习，在其他学科可作参考：

| 审稿人会问 | 你要拿出的证据 | 在智能合约例子里 |
|---|---|---|
| 这个问题值得解决吗？现有最好的为什么不够？ | 说清问题、为什么重要、当前最好的方法缺在哪[^ralph2020empirical-e81][^ralph2020empirical-e82] | 现有工具漏报多少、误报多少，开发者为什么不用 |
| 新在哪里？和最接近的工作差在哪？ | 逐个说出已有工作做到了什么、有什么限制，你超过了哪一点[^shaw2003writing-e3] | 一张对比表：工具 A、B、C 各自的检出率和适用范围 |
| 真的更好吗？ | 和当前最好的替代方案做实证比较，做不到要给出理由[^ralph2020empirical-e85] | 在同一批合约上，和最好的静态分析工具、直接用大模型的做法比 |
| 好处从哪来？ | 消融实验：逐个去掉方法的组成部分，看效果怎么变[^lipton2019troubling-e4] | 去掉漏洞模式提示、去掉静态分析结果，各掉多少 |
| 换个场景还好吗？ | 多个数据集、多种对象上的结果[^lones2021avoid-e10] | 不同漏洞类型、不同来源的合约 |
| 有什么代价和局限？ | 从概念上讨论长处、短处和局限[^ralph2020empirical-e81] | 调用大模型的费用、运行时间、哪些漏洞类型仍然查不出 |

几条判断"够不够"的规则。它们出自软件工程的论文写作指南和评审标准，道理在其他学科也大致适用 `[本项目分析]`：

- **证据要对准主张。** 主张性能提升，就要分析性能，而不是易用性或通用性[^shaw2003writing-e29]。
- **主张说得多满，证据就要多硬。** "总是有效"常常要靠分析论证；"提升 25%"这类有限定的主张可以靠评估；"存在一个例子"有时一个正例就够[^shaw2003writing-e16]。
- **"对我有效"不够。** 还要有证据表明它对别人也有用[^shaw2003writing-e35]。证据应来自实际经验或系统分析，而不只是说服性的论述或教科书式的例子[^shaw2002makes-e7]。
- **只有用户的主观评价、或者只有不和任何基准或替代方案比较的性能数字，都不够。** 软件工程的评审标准把这两种评估列为反面做法[^ralph2020empirical-e92]。
- **两个例外。** 如果问题本身是"能不能做到"，一个能运行的系统就可能足以回答[^shaw2003writing-e10]。制品越创新、概念分析越全面，对实证部分的要求越低；反过来，创新越少，评估越要严格[^ralph2020empirical-e94][^ralph2020empirical-e90]。
- **新颖不等于复杂。** "技术上不复杂"不是成立的批评，重要的是它有效；不必要的复杂反而不受欢迎[^ralph2020empirical-e96]。

这六个问题对各学科的构建改进都适用，但"和什么比""怎么测"是学科化的 `[本项目分析]`：计算机比的是基线工具和基准，化学看产率和底物范围，教育在真实课堂里一轮轮试用。具体做法见下一节列出的各方法页。

**写下来：** 把你的核心主张写成一句话，然后填上面那张表的第二、三列。填不出的格子，就是你还缺的证据。

## 3. 常用的研究方法

套路说"要产生什么知识"，方法说"用什么手段拿到证据"。构建改进常用下面这些方法 `[本项目分析]`：

| 方法 | 在构建改进里的作用 |
|---|---|
| [工程研究](../07_fields/computer-science/practices/engineering_research.md)（计算机的实践） | 计算机里这类研究的完整做法：选基线、选基准、设计评估、公开研究制品 |
| [基准评测](../07_fields/computer-science/practices/benchmarking.md)（计算机的实践） | 用一套标准的评测对象和自动化流程，和基线比较效果与代价 |
| [优化研究](../07_fields/computer-science/practices/optimization_study.md)（计算机的实践） | 把问题写成"在很多候选解中找最好的"，用搜索算法求解 |
| [定量仿真](../06_methods/simulation_study.md)（跨学科方法） | 真实系统不便直接实验时，在模型上评估新设计 |
| [对照实验](../06_methods/controlled_experiment.md)（跨学科方法） | 主张涉及人时（如"开发者用新工具更快找到漏洞"），请人参与比较 |
| [行动研究](../06_methods/action_research.md)（跨学科方法） | 和真实组织合作，在组织里引入一项改进，一边推动改变，一边研究它带来了什么 |
| [基于设计的研究](../07_fields/education/practices/design_based_research.md)（教育学的实践） | 在真实课堂里一轮轮设计、试用、改进教学干预，同时提炼设计原则 |
| [合成与表征研究](../06_methods/synthesis_study.md)（跨学科方法，原多用于化学） | 新反应、新路线的方法学研究，用底物范围和产率说明能做什么、不能做什么 |
| [基于实践的研究](../07_fields/arts/practices/practice_based_research.md)（艺术的实践） | 以创作出的作品作为知识贡献的基础 |

**行动研究为什么放在这里。** 软件工程的评审标准把行动研究定义为研究一项干预（例如引入某种方法或工具）如何影响真实环境的实证研究[^ralph2020empirical-e330]；行动研究的意义就在于引入改变，并观察参与者的反应[^ralph2020empirical-e342]。所以它服务两个套路：在真实组织里引入一项改进，属于构建改进；看真实环境里的人怎么反应，属于[观察描述](observe_describe.md) `[本项目分析]`。同一份标准也写明，行动研究不是实验[^ralph2020empirical-e343]，所以本手册不把它归入[解释因果](explain_causality.md) `[本项目分析]`。

一个项目常常组合几种方法：例如用基准评测证明效果，再用一个小规模的对照实验说明开发者确实用得上 `[本项目分析]`。

## 4. 它怎样影响整个项目

选了构建改进，项目里有几件事要比其他套路更早、更认真地做。下面的做法以计算机为例，道理大体可以借到其他学科 `[本项目分析]`；计算机特有的细节（模糊测试的评估、系统安全的开销测量、研究制品徽章等）见计算机篇的[工程研究](../07_fields/computer-science/practices/engineering_research.md)。

### 按"问题 → 技术 → 评估"组织整个项目

下面的三段式来自软件工程的工程研究评审标准，其他学科的组织方式可能不同。

**先讲问题，再讲方案。** 说清要解决什么问题、为什么重要、现有最好的方法为什么不够[^ralph2020empirical-e81][^ralph2020empirical-e82]。在软件工程里，这类论文常常用一个"问题"或"目标"来代替研究问题，审稿人不应因此批评[^ralph2020empirical-e96]。

**再讲技术。** 讲清整体流程、各部分如何配合，并把新的部分明确标出来[^ralph2020empirical-e83]。

**最后讲评估**，回答上一节的六个问题。

这个顺序不只是论文的写法，也是你做项目的顺序 `[本项目分析]`：问题没说清就动手做方案，做出来的东西常常解决的不是大家真正卡住的地方。在[收敛成项目](../01_from-interest-to-project/03_converge.md#2-它值得做吗)里有一个例子：如果开发者不用现有工具是因为误报太多，那多发现漏洞就不是关键，降低误报才是。

### 尽早把基线跑起来

**在设计自己的方法之前，先让基线能跑。** 没有一个可靠的基线，后面会遇到麻烦[^huang2023experiments-e5]。基线是简单或现成的方法，给出可达到效果的下限；它也是合理性检查：在机器学习里，复杂的方法常常还不如简单基线[^steinhardt2018stochastic-e7]。

基线至少要有两类：比新方法更简单的替代方案，用来证明新方法多出的复杂度确有必要[^lones2021avoid-e1]；以及当前最好的方法[^lones2021avoid-e2]。这两条来自机器学习的建议；对手的方法拿不到或跑不起来时怎么办，见计算机篇[工程研究](../07_fields/computer-science/practices/engineering_research.md#第-4-步选基线)。

早跑基线还有一个好处 `[本项目分析]`：你会很快发现基线跑不起来、评测数据有问题这类卡点。这正是[先做小规模试验，排除最大风险](../02_from-project-to-study/04_pilot-and-derisk.md)要提前暴露的风险。

### 动手前估一估改进空间

**先测下限和上限。** 这是一条来自机器学习的建议：做实证工作时，测出"上限"（效果最高可能有多好）常常很有用；一个办法是把最难实现的部分先换成"作弊"版本，例如偷看测试集，或用部署时拿不到的信息[^steinhardt2018stochastic-e24]。上限和基线一起划出效果可能落在的范围，帮你解读核心结果[^steinhardt2018stochastic-e24]。

在智能合约的例子里 `[本项目分析]`：先让大模型直接看到"这份合约有重入漏洞，在第几行"，看它能不能写出正确的分析。如果连这样都做不好，那么靠更好的提示去提升检出率，空间就很有限。

**再问提升值不值得。** 重大贡献很少来自"再多算一位小数"[^hamming1986you-e12]。小幅改进在服务于一个更大目标时最有用[^schulman2020opinionated-e11]；新方法如果只比基线好一点，就必须非常简单，否则没人会用[^schulman2020opinionated-e12]。

**写下来：** 写出你的基线能达到多少、上限大概多少、你希望做到多少。三个数字之间的距离，就是你的改进空间。

### 对后面各阶段的影响

下表是本项目的归纳 `[本项目分析]`：

| 阶段 | 构建改进要特别注意的 |
|---|---|
| [收敛成项目](../01_from-interest-to-project/03_converge.md) | 主张写成"在某条件下比谁好多少"，对比表要具体到每项最接近的工作 |
| [从研究问题到证据清单](../02_from-project-to-study/01_question-to-evidence.md) | 先画出空的结果表：行是你的方法和各基线，列是效果、代价、不同数据集 |
| [效度与局限](../02_from-project-to-study/03_validity-and-limits.md) | 开发时参考过的例子不能再用来评估，要在没见过的数据上检验（编程语言领域的评估清单把这列为要求[^blackburn2018sigplan-e12]） |
| [执行与迭代](../03_conduct-and-analyze/01_run-and-iterate.md) | 一样一样加改动，留着能做消融的版本 |
| [讲清故事，写成论文](../04_write-and-publish/01_story-and-paper.md) | 按"问题 → 技术 → 评估"写，把新的部分标出来，诚实写局限 |

## 5. 哪些学科常用

只列本文资料能确认的：

- **计算机。** 据 2003 年发表的一项对软件工程顶级会议 ICSE（国际软件工程大会）论文的分析，报告一种新的开发或分析技术的论文是其中最常见的一类[^shaw2003writing-e26]。
- **教育学。** 基于设计的研究以产出有效的教学干预为目标之一[^easterday2014design-e1]，属于这一类 `[本项目分析]`。
- **化学。** 合成方法学属于这一类 `[本项目分析]`。以美国化学会《有机化学杂志》为例，它期待合成方法论文在策略、转化或路线上有概念上的新意，而不只是把已有反应换一类底物、试剂或催化剂再做一遍[^acsjocguidelines-e30]。
- **艺术。** 如果创作出的作品是知识贡献的基础，就是基于实践的研究[^candy2006practice-e1]。它也是"做出新东西"，但一般不和基线比较，评价标准和上面几类很不同 `[本项目分析]`，具体见该方法页。

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 还没弄清现有方法为什么不行，就开始设计方案 | 设计问题以对问题的了解为前提[^easterbrook2008selecting-e29] |
| 只和自己以前的工作比，不和当前最好的方法比 | 系统安全领域把它列为一种比较缺陷[^vanderkouwe2019sok-e4] |
| 把弱基线说成"最先进方法" | 会夸大表面上的好处[^blackburn2018sigplan-e4] |
| 自己精心调参，对手用默认设置或非最优配置 | 比出来的是调参功夫，不是新设计 `[本项目分析]`；怎样公平对待对手，见[比较评估](compare_evaluate.md#对手是否被同等对待) |
| 一次捆绑好几个改动，不做消融 | 看不出提升从哪来，有时真正起作用的只有一个[^lipton2019troubling-e4] |
| 比别人好只是因为实现得更好 | 不是新设计带来的提升，新颖性值得怀疑[^vanderkouwe2019sok-e8] |
| 给简单方法套上庞大装置，号称"更好" | 加上大装置几乎总能让结果好一点，这正是被讽刺的论文套路[^zeller2021devil-e6] |
| 在一个数据集上好，就说普遍有效 | 在一个数据集上表现好，不代表在别的数据集上也好[^lones2021avoid-e10] |

## 7. 延伸阅读

- **整体框架**：Shaw 2003《Writing Good Software Engineering Research Papers》，用研究问题、成果、验证三张表讲清一篇工程论文该回答什么；Shaw 2002 从同样三个维度讨论什么是好的软件工程研究。
- **评审标准**：ACM SIGSOFT（美国计算机协会软件工程分会）实证研究标准中的工程研究标准，列出必须做到的、做到更好的，以及不成立的批评。
- **设计问题和知识问题**：Easterbrook 等人 2008，§2。
- **评估会在哪里出错**：Lipton & Steinhardt 2019《Troubling Trends in Machine Learning Scholarship》。
- **计算机的具体做法**：计算机篇的[工程研究](../07_fields/computer-science/practices/engineering_research.md)，含检查清单。
- **非计算机的例子**：[基于设计的研究](../07_fields/education/practices/design_based_research.md)。

[^easterbrook2008selecting-e28]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e28)
[^easterbrook2008selecting-e29]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e29)
[^steinhardt2018stochastic-e7]: Steinhardt 2018，Some further practical ideas。[证据](../../sources/notes/steinhardt2018stochastic.md#e7)
[^steinhardt2018stochastic-e24]: Steinhardt 2018，Some further practical ideas。[证据](../../sources/notes/steinhardt2018stochastic.md#e24)
[^shaw2003writing-e3]: Shaw 2003，§3.3。[证据](../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e10]: Shaw 2003，§4.1，表 5 后。[证据](../../sources/notes/shaw2003writing.md#e10)
[^shaw2003writing-e16]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e25]: Shaw 2003，§2.1，表 1。[证据](../../sources/notes/shaw2003writing.md#e25)
[^shaw2003writing-e26]: Shaw 2003，§3.2。[证据](../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e29]: Shaw 2003，§4.3。[证据](../../sources/notes/shaw2003writing.md#e29)
[^shaw2003writing-e35]: Shaw 2003，§4.3。[证据](../../sources/notes/shaw2003writing.md#e35)
[^shaw2002makes-e7]: Shaw 2002，§2.3。[证据](../../sources/notes/shaw2002makes.md#e7)
[^ralph2020empirical-e79]: SIGSOFT 工程研究标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e79)
[^ralph2020empirical-e80]: SIGSOFT 工程研究标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e80)
[^ralph2020empirical-e81]: SIGSOFT 工程研究标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e81)
[^ralph2020empirical-e82]: SIGSOFT 工程研究标准，脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e82)
[^ralph2020empirical-e83]: SIGSOFT 工程研究标准，脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e83)
[^ralph2020empirical-e85]: SIGSOFT 工程研究标准，必要项（方法）。[证据](../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e90]: SIGSOFT 工程研究标准，总体质量标准。[证据](../../sources/notes/ralph2020empirical.md#e90)
[^ralph2020empirical-e92]: SIGSOFT 工程研究标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e92)
[^ralph2020empirical-e94]: SIGSOFT 工程研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e94)
[^ralph2020empirical-e96]: SIGSOFT 工程研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e96)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../sources/notes/lipton2019troubling.md#e7)
[^lones2021avoid-e1]: Lones 2021，§5.2，第 21 页。[证据](../../sources/notes/lones2021avoid.md#e1)
[^lones2021avoid-e2]: Lones 2021，§5.2，第 21 页。[证据](../../sources/notes/lones2021avoid.md#e2)
[^lones2021avoid-e10]: Lones 2021，§6.3，第 24 页。[证据](../../sources/notes/lones2021avoid.md#e10)
[^blackburn2018sigplan-e4]: SIGPLAN 实证评估清单，Suitable Comparison。[证据](../../sources/notes/blackburn2018sigplan.md#e4)
[^blackburn2018sigplan-e12]: SIGPLAN 实证评估清单，Tested on training set。[证据](../../sources/notes/blackburn2018sigplan.md#e12)
[^vanderkouwe2019sok-e4]: van der Kouwe 等人 2019，§II-D。[证据](../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e8]: van der Kouwe 等人 2019，§II-E。[证据](../../sources/notes/vanderkouwe2019sok.md#e8)
[^zeller2021devil-e6]: Zeller 2021，THE RUBE GOLDBERG。[证据](../../sources/notes/zeller2021devil.md#e6)
[^huang2023experiments-e5]: Jia-Bin Huang 2023，推文串 *Start with a baseline*。[证据](../../sources/notes/huang2023experiments.md#e5)
[^hamming1986you-e12]: Hamming 1986，"ambiguity" 一段之后。[证据](../../sources/notes/hamming1986you.md#e12)
[^schulman2020opinionated-e11]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../sources/notes/schulman2020opinionated.md#e11)
[^schulman2020opinionated-e12]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../sources/notes/schulman2020opinionated.md#e12)
[^easterday2014design-e1]: Easterday 等人 2014，Introduction，第 317 页。[证据](../../sources/notes/easterday2014design.md#e1)
[^bakker2015introduction-e3]: Bakker & van Eerde 2015，§16.1.2.1，第 430 页。[证据](../../sources/notes/bakker2015introduction.md#e3)
[^acsjocguidelines-e30]: JOC 作者须知，Scope of the Journal (a)。[证据](../../sources/notes/acsjocguidelines.md#e30)
[^ralph2020empirical-e330]: SIGSOFT 行动研究标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e330)
[^ralph2020empirical-e342]: SIGSOFT 行动研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e342)
[^ralph2020empirical-e343]: SIGSOFT 行动研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e343)
[^candy2006practice-e1]: Candy 2006，Summary，第 1 页。[证据](../../sources/notes/candy2006practice.md#e1)
