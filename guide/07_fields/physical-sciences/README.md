# 物理科学：学科概况

本文讲物理科学（这里以物理学和天文学为主）的研究实际怎样运转：理论、实验、计算的分工，几千人的大合作，arXiv 预印本，盲分析和"5σ"发现标准，以及数据和代码共享。各学科共通的做法（选题、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)，这里不重复。物理常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。

文中很多具体例子来自粒子物理和引力波天文学，因为本文找到的公开规范主要来自这两个方向。凝聚态、光学等方向的惯例可能不同，要以本组和目标期刊的要求为准。

**读完本文，你应该能：**

- 说清物理研究里理论、实验、计算几类工作的分工；
- 知道在大合作里，一个结果从分析到发表要过哪些关口，学生能做什么、不能做什么；
- 理解 arXiv 预印本和期刊在物理中各起什么作用；
- 说清盲分析和 5σ 是什么、为什么用、有什么争议；
- 按学会和期刊的要求处理署名、数据和代码。

---

## 本领域研究怎样运转

### 理论、实验、计算：先弄清自己属于哪一类

在高能物理，arXiv 的分类就是按做法分的：做实验、做理论、做唯象，还是做格点计算。

| arXiv 分类 | 做什么 |
|---|---|
| hep-ex（实验） | 粒子物理实验的结果[^arxivtaxonomy-e1] |
| hep-th（理论） | 量子场论的形式理论、弦论等[^arxivtaxonomy-e2] |
| hep-ph（唯象） | 联系理论和实验的理论工作[^arxivtaxonomy-e3] |
| hep-lat（格点） | 格点场论，包括它的算法和专用硬件[^arxivtaxonomy-e4] |

在实验粒子物理，理论和实验分工明确[^junk2021reproducibility-e21]。要检验的模型一般先在理论或唯象论文里发表，然后才做实验[^junk2021reproducibility-e23]。实验者几乎从不检验自己提出的理论，这能减少**确认偏差**（只看见支持自己想法的证据）[^junk2021reproducibility-e22]。你属于哪一类，决定了你每天做什么、和谁合作、论文长什么样。进组前先问清楚。

### 大合作：几千人做一个实验

有些方向的实验规模极大，粒子物理是典型。粒子物理实验要花好几年设计、建造和运行，需要大量经费、设备和人力[^junk2021reproducibility-e3]。大型强子对撞机（Large Hadron Collider，LHC）上的 ATLAS 和 CMS 合作组各有三千多名物理学家，中微子实验的合作组也常有几百到一千多人[^junk2021reproducibility-e2]。很多论文的作者超过三千人[^junk2021reproducibility-e1]。

在这样的合作组里，一个结果要过多道关口才能发表。下表只是两个例子，不是所有合作组的统一规定：标"LIGO"的一行来自 LIGO 科学合作组（LIGO Scientific Collaboration，LSC，做引力波探测）的政策；其余几行来自 Junk 和 Lyons 的介绍，他们以 CDF 合作组（一个典型的强子对撞机合作组）为例[^junk2021reproducibility-e33]。**你所在合作组的流程以它自己的政策为准**：

| 关口 | 发生什么 |
|---|---|
| 开始分析 | 先找合作组的统计委员会，免得做到内部审查时才发现方向错了[^junk2021reproducibility-e16] |
| 初步结果 | 在合作组外公开之前，要过一个漫长的正式批准流程[^junk2021reproducibility-e11] |
| 论文内部审查 | 由做过类似课题、但没参与这项结果的成员组成委员会审初稿[^junk2021reproducibility-e12]；名单上的所有作者都有机会审阅[^junk2021reproducibility-e30]；可能要几个月甚至几年[^junk2021reproducibility-e13] |
| 投稿或发 arXiv 之前（LIGO） | LIGO 要求先确定是否需要内部审查[^ligo2018publication-e6]；内部审稿人要核实最重要的结果，并对署名提意见[^ligo2018publication-e7] |
| 期刊审稿 | 仍然有用：合作组也会陷入"群体思维"，外部审稿能补上[^junk2021reproducibility-e15] |

LIGO 有几条和学生直接相关的规定。别的合作组不一定一样，但多半有类似条款，要自己去查：

- 合作组正式宣布之前，学位论文里不能发表声称探测到信号的分析[^ligo2018publication-e9]；
- 没经合作组审查的学位论文，要在引言里声明它不代表合作组的观点[^ligo2018publication-e10]；
- 对外做报告时，只能展示已公开或经合作组批准的结果[^ligo2018publication-e8]。

大合作里也不是每篇论文都几千人署名。以 LIGO 为例：单个或几个机构完成的技术论文，按一般的署名原则定作者[^ligo2018publication-e4]；某些论文的主要作者还可以申请只列实质贡献者的"短作者名单"[^ligo2018publication-e5]。

### 小课题组：没有人替你把关

不是所有物理研究都在大合作里做。在一个课题组里做实验，没有统计委员会和内部审查委员会，上面那些检查要靠你和导师自己做。

最需要防的是"和已知值一致就收工"。Feynman 讲过电子电荷测量的历史：后人测出的值离 Millikan 的值太远，就去找毛病；接近 Millikan 的值，就不再细查[^feynman1974cargo-e14]。他的结论是：第一原则是不要骗自己，而你是最容易被骗的人[^feynman1974cargo-e7]。粒子物理学家 Roodman 说得更直接：结果和以前的测量符不符合，不能说明测量本身做得对不对[^roodman2003blind-e4]。小实验也能做盲测量：Dunnington 测电子荷质比时，让机械师随意设定一个关键角度，直到分析完成、准备发表时才去精确测量它[^roodman2003blind-e5]。

### 发表：arXiv 预印本加期刊

**arXiv 是从物理开始的。** 它的前身是 1991 年开始运行的高能物理理论（hep-th）电子邮件预印本服务器[^ginsparg2011twenty-e1][^ginsparg2011twenty-e2]，由 Paul Ginsparg 创办[^arxivabout-e1]。在那之前，作者只能把论文复印件寄给少数人[^ginsparg2011twenty-e3]，非名校的年轻研究者常常拿不到[^ginsparg2011twenty-e4]。

**现在预印本和期刊并存，各起不同作用**[^ginsparg2011twenty-e5]。物理学家很快接受了审稿之前就公开论文的做法，其他学科不一定如此[^ginsparg2011twenty-e6]。几件要知道的事：

- **arXiv 不做同行评审。** 它只审核稿件是否属于该学科、是否有学术价值[^arxivabout-e2]，内容由提交者自己负责[^arxivabout-e3]。
- **第一次投稿要先获得"背书"（endorsement）**，第一次投某个新分类时也要[^arxivendorsement-e1]。研究生可以找导师，或本单位同领域、也在 arXiv 上发文的教授背书[^arxivendorsement-e2]。背书也不是同行评审[^arxivendorsement-e4]。
- **APS（美国物理学会）的态度**：预印本是分享新工作的好办法，很多期刊不把它算作重复发表，但作者要自己查清目标期刊的政策；论文正式发表后，要在预印本上加上正式版本的链接[^aps2024ethics-e8]。

### 署名

APS 2024 年修订的《伦理标准》（Ethics Standards）规定：

- 署名只给、也不能漏掉在构思、设计、执行、解释或写作上有重要贡献的人；每个作者都要能说清自己具体做了什么[^aps2024ethics-e4]。
- 只提供经费不够资格署名，应写进致谢[^aps2024ethics-e9]。
- 大合作可以有自己的署名约定，只要署名程序透明[^aps2024ethics-e6]。例如 LIGO 的观测论文按字母顺序列出所有有资格的成员[^ligo2018publication-e1]；取得资格，大约要用一年时间、把至少一半的研究精力投入合作组[^ligo2018publication-e2]。
- 有资格的成员可以要求不在某篇论文上署名[^ligo2018publication-e3]。合作组内部达不成共识时，持不同意见的人可以要求去掉自己的名字[^junk2021reproducibility-e14]。

按字母排序的几千人名单，看不出谁做了哪项分析。本文没有找到资料说明大合作里个人贡献一般怎样被外界看到；建议尽早问导师，本组学生通常靠什么让别人知道自己的工作。可以参考的一点是，LIGO 把"鼓励年轻科学家和工程师参与报告和发表"写进了政策目标[^ligo2018publication-e11]。通用的署名做法见贯穿全程的[合作与导师](../../08_throughout/collaboration_and_advisors.md#6-署名开工时就谈并随进展调整)。

---

## 和其他学科不同的地方

| 方面 | 粒子物理（本文证据大多来自这里，其他物理方向未必相同） | 其他学科的对照 |
|---|---|---|
| 主要发表渠道 | 期刊，加上 arXiv 预印本，两者并存[^ginsparg2011twenty-e5] | 计算机以会议为主[^vardi2009conferences-e1]；生物医学长期只认审过的期刊论文为优先权依据[^ginsparg2011twenty-e7] |
| 宣布"发现"的统计门槛 | 按惯例，p 值小于 2.87×10⁻⁷（5σ）[^junk2021reproducibility-e31] | 一些学科常用 0.05[^junk2021reproducibility-e31] |
| 发表前的审查 | 大合作有严格的多级内部审查，很多分析是盲的[^junk2021reproducibility-e32] | |

### 5σ：宣布"发现"的门槛

5σ 是粒子物理的惯例，不是全物理统一的规定[^lyons2013discovering-e1]。先解释两个词。**p 值**：假设只有本底、没有新效应，靠随机涨落看到至少这么大效应的概率[^lyons2013discovering-e1]。**σ**（标准差）：这里是换算 p 值的单位，"5σ"指标准正态分布单侧 5 个标准差以外的面积[^lyons2013discovering-e1]。

- **惯例**：在粒子物理，要宣布发现新物理，按惯例这个概率不能超过 5σ 对应的面积[^lyons2013discovering-e1]，也就是 p 值门槛取 2.87×10⁻⁷[^junk2021reproducibility-e4]。达不到，期刊很不愿意让"发现"一词出现在标题、摘要或结论里[^lyons2013discovering-e2]。
- **为什么这么严**（以下是 Junk 和 Lyons 对粒子物理给出的理由）：历史上 3σ、4σ 的效应在收集更多数据后常常消失[^junk2021reproducibility-e5]。相互竞争的合作组需要共用一个事先定好的门槛，否则发现的功劳会落到标准最低的人手里[^junk2021reproducibility-e28]。
- **5σ 挡不住什么**：**系统误差**（由仪器、标定或分析方法带来的偏差，不是随机涨落）如果没被估计进不确定度，可以造成任意高显著性的假发现[^junk2021reproducibility-e7]。所以显著性再高，也要先查系统误差。
- **别处效应**（Look Elsewhere Effect）：只算"在你看到峰的那个位置"出现涨落的概率，叫局部 p 值；允许涨落出现在任何位置，叫全局 p 值，它更大[^lyons2013discovering-e3]。用什么方法要在分析前定好，论文里要写清全局 p 值怎么定义[^lyons2013discovering-e4]。
- **适用范围**：Junk 和 Lyons 认为，5σ 放在粒子物理比放在医学试验等领域更说得通[^junk2021reproducibility-e29]。本文找到的资料只讨论了粒子物理；凝聚态、天文等方向是否有、有什么样的发现门槛，本文无法确认，请问导师或查目标期刊。

> **不同的看法：所有发现都要 5σ 吗？**
> - **支持统一门槛**：门槛本身是人为约定[^junk2021reproducibility-e6]，但竞争的合作组共用一个事先定好的标准，能防止大家比谁的标准低[^junk2021reproducibility-e28]。
> - **反对一刀切**：Lyons 指出统计学家很怀疑 5σ 是否合理[^lyons2013discovering-e5]；他认为对所有新物理搜索都用统一的 5σ 并不合理[^lyons2013discovering-e7]，主张不再要求"所有发现都要 5σ"[^lyons2013discovering-e6]。
>
> 实际做法：按你所在合作组和目标期刊的规定来；同时在论文里如实报告局部和全局 p 值，写清系统误差是怎么估计的。

### 盲分析：先定方法，再看答案

**盲分析**就是不看答案做测量[^roodman2003blind-e1]。它防的是**实验者偏差**：测量无意中被推向以前的结果或理论预期[^roodman2003blind-e2]。比如，在知道选择条件（cut，用来筛选事件的门槛）会怎样影响结果的情况下设定它，就可能产生偏差[^roodman2003blind-e3]。实验粒子物理里很多分析是盲的[^junk2021reproducibility-e32]。

常见做法：

- 先用模拟数据把分析调好，事件选择、分类和统计方法都定下来，再放入真实数据[^junk2021reproducibility-e9]；
- **隐藏信号框**：分析完成前，把信号可能出现的区域藏起来不看[^roodman2003blind-e6]；
- **隐藏答案**：精密测量参数时，常用的办法是先把答案藏起来[^roodman2003blind-e7]；
- 先在一小部分数据上把方法定死，再原样用到全部数据上[^roodman2003blind-e9]。

关键规则：**揭盲之后不能再改分析的任何步骤，否则就不算完全的盲分析**[^junk2021reproducibility-e10]。不是所有分析都容易做成盲的[^roodman2003blind-e8]。BABAR 合作组起初对盲分析有保留，后来把它变成了标准做法[^roodman2003blind-e10]。

> **不同的看法：盲分析值不值？**
> - **支持**：Roodman 认为盲分析是减少实验者偏差的最好办法[^roodman2003blind-e1]。
> - **质疑**：物理学家 Golub 在一篇未经同行评审的短评中指出，盲分析会严重妨碍寻找系统误差，也会让人没法研究落在被遮住区域里的意外事件[^golub2023blind-e1]；为一个可能并不存在的问题引入它[^golub2023blind-e2]，在他看来是过度了[^golub2023blind-e3]。
>
> 实际做法：看数据之前，和导师一起决定要不要盲、怎么盲，并写下来；揭盲后如果确实要改，就在论文里写明改了什么、为什么。通用的做法见研究套路[比较评估](../../05_research-strategies/compare_evaluate.md#2-什么样的证据才够)。

---

## 本领域的规范和报告标准

**APS《伦理标准》（2024 年修订）** 是物理学会层面的总规范：

- 物理学家必须说真话[^aps2024ethics-e1]。诚实的错误不算捏造或篡改[^aps2024ethics-e10]，但发现已发表论文有错，要及时更正或撤回[^aps2024ethics-e11]。
- 不要把一项研究拆成几篇来凑数[^aps2024ethics-e12]；同一篇论文不能同时投多个期刊[^aps2024ethics-e13]。
- 在会议上发过摘要，一般不妨碍再投完整论文，但投稿时要说明[^aps2024ethics-e15]。
- 在社交媒体等公开场合介绍工作时，超出已证实范围的影响要么不说，要么明确标为推测[^aps2024ethics-e14]。
- 所有合作都要建立保证结果准确的流程[^aps2024ethics-e7]。

**数据和代码。** APS 要求研究结果的记录方式尽可能让别人能复现[^aps2024ethics-e2]，数据和代码要保存一段合理的时间[^aps2024ethics-e3]。Physical Review 系列期刊要求：

- 每篇论文都要有"数据可获取性声明"（Data Availability Statement）[^apsdataavailability-e1]；这里的"数据和软件"指核实或复现结果所需的一切材料[^apsdataavailability-e5]，所以你自己写的分析代码通常也算；
- 强烈鼓励按 FAIR 原则（可发现、可获取、可互操作、可重用）公开数据和软件[^apsdataavailability-e2]，公开的数据和软件要写进参考文献[^apsdataavailability-e3]；
- 不能公开的，必须同意在合理请求下私下提供[^apsdataavailability-e4]。数值模拟论文的示例声明是"源代码和参数已公开"[^apsdataavailability-e6]。

**天文学的软件引用。** 美国天文学会（AAS）期刊建议引用软件时两种方式都用：引描述软件的论文，再引软件本身的 DOI（数字对象标识符，一种永久链接），后者让读者拿到你用的确切版本[^aassoftware-e2]。AAS 强烈建议用开源许可证发布代码[^aassoftware-e3]，也接受专门介绍软件的论文[^aassoftware-e4]。注意：AAS 期刊的审稿人不直接审查软件[^aassoftware-e5]，代码对不对主要靠你自己。

**大合作的数据公开（以 CERN 为例）。** LHC 实验的论文全部开放获取[^cern2020opendata-e1]，发表时同时把补充数据放到 HEPData 等平台[^cern2020opendata-e2]；重建后的数据，目标是在运行期结束后五年内开始公开[^cern2020opendata-e3]。用开放数据的外部研究者要知道：合作组多年积累的隐性知识你拿不到[^cern2020opendata-e4]，结论由你自己负责[^cern2020opendata-e5]。

**计算的可复现。** 粒子物理的经验：不只源代码，运行环境也要做版本控制[^junk2021reproducibility-e19]；在不同架构的计算机上跑同一程序、比较结果[^junk2021reproducibility-e20]。但能复现只说明计算步骤没错，不说明假设和输入数据可靠[^junk2021reproducibility-e18]。已发表结果常见的缺陷是没给出相关的不确定度，别人就没法精确复现结论[^junk2021reproducibility-e26]。整理代码和数据的通用做法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，按核心主张来定，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表的分组和"在物理里的样子"一栏是本项目的归纳；每条标准只代表脚注里那个方向或那本期刊（多为粒子物理；理论研究几行主要出自 Physical Review A），其他方向以本组和目标期刊为准。

| 套路 | 在物理里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [测量](../../05_research-strategies/measure.md) | 精密测量一个常数、一种性质或一个参数 | 测量结果必须带上可信程度的定量说明[^jcgm2008gum-e1]；系统误差没估计进不确定度，可能造成假发现[^junk2021reproducibility-e7]；精密测量常先把答案藏起来[^roodman2003blind-e7] | [实验测量研究](../../06_methods/experimental_measurement.md) |
| [观察描述](../../05_research-strategies/observe_describe.md) | 搜寻新粒子、新效应，回答"有没有" | 粒子物理宣布发现按惯例要 5σ[^junk2021reproducibility-e4]；写清全局 p 值怎么定义[^lyons2013discovering-e4]；零结果写成信号强度的上限，照样发表[^junk2021reproducibility-e25] | 上文[5σ](#5σ宣布发现的门槛)和[盲分析](#盲分析先定方法再看答案) |
| [比较评估](../../05_research-strategies/compare_evaluate.md) | 比较计算程序或方法。例如一项社区合作在 71 种单质晶体上比较了 15 个固体计算程序[^lejaeghere2016reproducibility-e3] | 看同一批体系上的逐对差异；该研究发现新近程序之间的差异和不同高精度实验之间的差异相当[^lejaeghere2016reproducibility-e4] | [定量仿真](../../06_methods/simulation_study.md) |
| [构建改进](../../05_research-strategies/build_improve.md) | 设计探测器、望远镜，开发数据分析方法和软件[^arxivtaxonomy-e6] | 天文期刊接受专门的软件论文[^aassoftware-e4]，但审稿人不直接审查软件[^aassoftware-e5]；数值模拟论文要声明代码和参数能否获取[^apsdataavailability-e6] | [工程研究](../computer-science/practices/engineering_research.md)（计算机的实践，可参考） |
| [构建改进](../../05_research-strategies/build_improve.md) | 理论方法：发展新的理论技巧、形式体系或近似方法[^aps2011uncertainty-e3] | 对近似方法来说，和实验或其他理论的比较本身就评估了方法的误差[^aps2011uncertainty-e3] | [理论研究](../computer-science/practices/theoretical_research.md)（计算机的实践，可参考） |
| [解释因果](../../05_research-strategies/explain_causality.md) | 理论解释和唯象：解释以前没解释的现象[^aps2011uncertainty-e3]；唯象指联系理论和实验的理论工作[^arxivtaxonomy-e3] | 解释现象时，和实验半定量地符合就已经有意义[^aps2011uncertainty-e3] | 暂无专门的方法篇 |
| [测量](../../05_research-strategies/measure.md) | 精密理论计算：算出要和高精度实验比较的数值，或提供作参考数据的基准结果[^aps2011uncertainty-e3] | 这两类最需要仔细评估理论不确定度[^aps2011uncertainty-e4]；只要可行，就给出不确定度估计（什么时候必须给、怎么估，见表后） | [定量仿真](../../06_methods/simulation_study.md) |

理论研究按核心主张分到表里最后三行：发展新方法归构建改进，解释现象归解释因果，给出要和实验比较的精确数值归测量。在粒子物理，要检验的模型一般先在理论或唯象论文里发表，再由实验者去测[^junk2021reproducibility-e23]。

这三行的标准出自 Physical Review A（美国物理学会的期刊之一）编辑部 2011 年的一篇社论，只代表这本期刊当时的要求。社论的出发点是：实验论文不详细讨论测量不确定度，这本期刊通常不会接收[^aps2011uncertainty-e2]；而理论论文投来时，数值结果不带不确定度估计并不少见[^aps2011uncertainty-e1]。社论对理论计算的要求：

- **什么时候必须给。** 只要可行就要给；以下三种情况尤其要给：声称精度高或比以前更准；主要目的是和高精度实验比较；主要目的是内插或外推已有的实验数据[^aps2011uncertainty-e7]。
- **不确定度从哪来。** 一是数值结果是否收敛，例如随基组大小、积分步长变化；二是计算一开始就没包含的物理效应[^aps2011uncertainty-e5]。
- **要多严格。** 要的是估计，不是误差的确切大小或严格上界[^aps2011uncertainty-e6]。
- **给不出时。** 社论承认，很多情况下确实给不出有意义的误差估计，例如复杂体系的散射过程[^aps2011uncertainty-e8]。

另外两本物理期刊在网站上写了接收标准，可以作对照。注意它们针对的是所有投稿，不是专门评判理论论文的标准：JHEP（Journal of High Energy Physics，高能物理期刊；读的是 2026 年查阅的网页，页面没有注明日期）的收稿范围包括量子场论、弦和膜理论[^jhepabout-e1]，接收看科学质量、原创性和相关性[^jhepabout-e2]。SciPost Physics（荷兰 SciPost 基金会的开放获取期刊；读的是 2025 年 12 月的网页存档）要求稿件至少做到四条"期望"之一，比如在公认的长期难题上取得突破，或打开一个能引出后续工作的新方向[^scipost2025physics-e1]；还要满足全部一般要求，其中包括把细节写够，让内行专家能自己重走一遍你的论证和推导，并在结论里如实说明结果能用到哪里、有哪些局限[^scipost2025physics-e2]。

形式理论（例如弦论[^arxivtaxonomy-e2]）按什么标准评判、其他物理期刊怎样评判理论论文，本文资料未涉及，以目标期刊为准。

---

## 本学科常用的研究方法

下面的归类是本手册的归纳。

- **实验测量**：[实验测量研究](../../06_methods/experimental_measurement.md)（跨学科方法）。物理实验特有的盲分析和 5σ 见上文。研究类型里的[对照实验](../../06_methods/controlled_experiment.md)针对人类参与者，做法不同。
- **理论研究**：可参考计算机篇的[理论研究](../computer-science/practices/theoretical_research.md)。唯象研究没有对应的方法篇。
- **数值计算与模拟**（计算物理、格点计算[^arxivtaxonomy-e5][^arxivtaxonomy-e4]）：[定量仿真](../../06_methods/simulation_study.md)。
- **用公开数据做分析**：合作组外的研究者用 LHC 等实验公开的数据发表自己的分析，结论由自己负责[^cern2020opendata-e5]，见[复现研究](../../06_methods/replication.md)。外部研究者缺少合作组的隐性知识[^cern2020opendata-e4]。

---

## 给新手的建议

1. **进组第一周，读完合作组的发表政策。** 特别是学位论文、会议报告和 arXiv 的规定，例如 LIGO 不允许学位论文抢先发表探测结果[^ligo2018publication-e9]。小组没有成文政策的，问导师。
2. **动手分析之前，先把方法和盲化方式写下来。** 在大合作里，先找统计委员会[^junk2021reproducibility-e16]；揭盲后不再改分析步骤[^junk2021reproducibility-e10]。
3. **接手别人的分析，先复现前人的结果。** 这是粒子物理新学生的第一件事[^junk2021reproducibility-e17]。
4. **结果和已知值一致时，同样认真找错。** 一致不说明测量做对了[^roodman2003blind-e4]，Millikan 之后的电子电荷测量史就是教训[^feynman1974cargo-e14]。
5. **零结果也要发表。** 决定检验一个理论，就要无论结果如何都发表[^feynman1974cargo-e18]；粒子物理把零结果写成上限照样发表[^junk2021reproducibility-e25]。
6. **从第一天起，按要公开的标准整理代码和数据。** 投稿时要写数据声明[^apsdataavailability-e1]，代码要能被引用到确切版本[^aassoftware-e2]。
7. **发 arXiv 前查清两件事**：合作组是否要求先做内部审查[^ligo2018publication-e6]，目标期刊对预印本的政策[^aps2024ethics-e8]。正式发表后回去更新链接[^aps2024ethics-e8]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 测出的值和文献一致就停止检查，不一致才找毛病 | 这种不对称会让偏差延续很久[^feynman1974cargo-e14]；一致不说明做对了[^roodman2003blind-e4] |
| 边看结果边调选择条件 | 知道选择会怎样影响结果时设定它，会产生实验者偏差[^roodman2003blind-e3] |
| 揭盲后发现结果"不理想"，又回去改分析 | 这样就不再是盲分析[^junk2021reproducibility-e10] |
| 在粒子物理，3σ 的效应就说"发现" | 3σ、4σ 的效应常在更多数据后消失[^junk2021reproducibility-e5]；期刊不愿意在没达标时用"发现"一词[^lyons2013discovering-e2] |
| 只报告局部 p 值 | 全局 p 值更大，要写清怎么定义[^lyons2013discovering-e3][^lyons2013discovering-e4] |
| 没查合作组政策，就把结果放上 arXiv 或写进学位论文 | 可能违反合作组政策，例如 LIGO 对两者都有规定[^ligo2018publication-e6][^ligo2018publication-e9] |
| 把只提供经费的人列为作者 | 不够署名资格，应写进致谢[^aps2024ethics-e9] |
| 只在致谢里写"感谢某软件"，不引用具体版本 | 读者拿不到你用的确切版本[^aassoftware-e2]；Physical Review 要求公开软件写进参考文献[^apsdataavailability-e3] |
| 论文里只给直方图，不给相关不确定度 | 别人没法精确复现结论[^junk2021reproducibility-e26] |

---

## 延伸阅读

- **Junk & Lyons 2021，Reproducibility and Replication of Experimental Particle Physics Results**：两位实验粒子物理学家介绍粒子物理怎样保证结果可靠，包括内部审查、盲分析、5σ、软件和数据保存。想了解大合作怎样运转，先读这篇。
- **APS Ethics Standards（2024）**：美国物理学会的伦理标准，署名、重复发表、预印本、数据保存都有规定。
- **LIGO Publication and Presentation Policy（2018）**：一份公开的大合作发表政策全文，可以看到署名资格、内部审查、学位论文规则的具体写法。进入任何大合作前，找本合作组的同类文件来读。
- **Roodman 2003，Blind Analysis in Particle Physics**：会议论文，讲清实验者偏差和几种盲分析方法。配合 Golub 2023 的质疑一起读。**Lyons 2013，Discovering the Significance of 5σ**：讲粒子物理为什么用 5σ，以及统一用 5σ 的问题。
- **Feynman 1974，Cargo Cult Science**：讲"不要骗自己"，含 Millikan 油滴实验之后的测量史。**Physical Review 数据可获取性声明指南、AAS 软件政策**：投稿前对照检查。

[^arxivtaxonomy-e1]: arXiv Category Taxonomy，hep-ex。[证据](../../../sources/notes/arxivtaxonomy.md#e1)
[^arxivtaxonomy-e2]: arXiv Category Taxonomy，hep-th。[证据](../../../sources/notes/arxivtaxonomy.md#e2)
[^arxivtaxonomy-e3]: arXiv Category Taxonomy，hep-ph。[证据](../../../sources/notes/arxivtaxonomy.md#e3)
[^arxivtaxonomy-e4]: arXiv Category Taxonomy，hep-lat。[证据](../../../sources/notes/arxivtaxonomy.md#e4)
[^arxivtaxonomy-e5]: arXiv Category Taxonomy，physics.comp-ph。[证据](../../../sources/notes/arxivtaxonomy.md#e5)
[^arxivtaxonomy-e6]: arXiv Category Taxonomy，astro-ph.IM。[证据](../../../sources/notes/arxivtaxonomy.md#e6)
[^aps2011uncertainty-e1]: Physical Review A 编辑部 2011，第 1–2 段。[证据](../../../sources/notes/aps2011uncertainty.md#e1)
[^aps2011uncertainty-e2]: Physical Review A 编辑部 2011，第 2 段。[证据](../../../sources/notes/aps2011uncertainty.md#e2)
[^aps2011uncertainty-e3]: Physical Review A 编辑部 2011，第 3 段。[证据](../../../sources/notes/aps2011uncertainty.md#e3)
[^aps2011uncertainty-e4]: Physical Review A 编辑部 2011，第 4 段。[证据](../../../sources/notes/aps2011uncertainty.md#e4)
[^aps2011uncertainty-e5]: Physical Review A 编辑部 2011，第 4 段。[证据](../../../sources/notes/aps2011uncertainty.md#e5)
[^aps2011uncertainty-e6]: Physical Review A 编辑部 2011，第 4 段。[证据](../../../sources/notes/aps2011uncertainty.md#e6)
[^aps2011uncertainty-e7]: Physical Review A 编辑部 2011，第 5 段。[证据](../../../sources/notes/aps2011uncertainty.md#e7)
[^aps2011uncertainty-e8]: Physical Review A 编辑部 2011，第 5 段。[证据](../../../sources/notes/aps2011uncertainty.md#e8)
[^jhepabout-e1]: JHEP，About 网页（2026 年查阅，页面未注明日期），Scope。[证据](../../../sources/notes/jhepabout.md#e1)
[^jhepabout-e2]: JHEP，About 网页，Editorial policy。[证据](../../../sources/notes/jhepabout.md#e2)
[^scipost2025physics-e1]: SciPost Physics，About 网页（2025 年 12 月存档），Acceptance Criteria。[证据](../../../sources/notes/scipost2025physics.md#e1)
[^scipost2025physics-e2]: SciPost Physics，About 网页，Acceptance Criteria。[证据](../../../sources/notes/scipost2025physics.md#e2)
[^junk2021reproducibility-e1]: Junk & Lyons 2021，摘要。[证据](../../../sources/notes/junk2021reproducibility.md#e1)
[^junk2021reproducibility-e2]: Junk & Lyons 2021，§1。[证据](../../../sources/notes/junk2021reproducibility.md#e2)
[^junk2021reproducibility-e3]: Junk & Lyons 2021，§1。[证据](../../../sources/notes/junk2021reproducibility.md#e3)
[^junk2021reproducibility-e4]: Junk & Lyons 2021，§3。[证据](../../../sources/notes/junk2021reproducibility.md#e4)
[^junk2021reproducibility-e5]: Junk & Lyons 2021，§3。[证据](../../../sources/notes/junk2021reproducibility.md#e5)
[^junk2021reproducibility-e6]: Junk & Lyons 2021，§3。[证据](../../../sources/notes/junk2021reproducibility.md#e6)
[^junk2021reproducibility-e7]: Junk & Lyons 2021，§3。[证据](../../../sources/notes/junk2021reproducibility.md#e7)
[^junk2021reproducibility-e9]: Junk & Lyons 2021，§6.6。[证据](../../../sources/notes/junk2021reproducibility.md#e9)
[^junk2021reproducibility-e10]: Junk & Lyons 2021，§6.6。[证据](../../../sources/notes/junk2021reproducibility.md#e10)
[^junk2021reproducibility-e11]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e11)
[^junk2021reproducibility-e12]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e12)
[^junk2021reproducibility-e13]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e13)
[^junk2021reproducibility-e14]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e14)
[^junk2021reproducibility-e15]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e15)
[^junk2021reproducibility-e16]: Junk & Lyons 2021，§6.9，Statistics Committees。[证据](../../../sources/notes/junk2021reproducibility.md#e16)
[^junk2021reproducibility-e17]: Junk & Lyons 2021，§4.1。[证据](../../../sources/notes/junk2021reproducibility.md#e17)
[^junk2021reproducibility-e18]: Junk & Lyons 2021，§4.1。[证据](../../../sources/notes/junk2021reproducibility.md#e18)
[^junk2021reproducibility-e19]: Junk & Lyons 2021，§6.2。[证据](../../../sources/notes/junk2021reproducibility.md#e19)
[^junk2021reproducibility-e20]: Junk & Lyons 2021，§4.1。[证据](../../../sources/notes/junk2021reproducibility.md#e20)
[^junk2021reproducibility-e21]: Junk & Lyons 2021，§7。[证据](../../../sources/notes/junk2021reproducibility.md#e21)
[^junk2021reproducibility-e22]: Junk & Lyons 2021，§7。[证据](../../../sources/notes/junk2021reproducibility.md#e22)
[^junk2021reproducibility-e23]: Junk & Lyons 2021，§7。[证据](../../../sources/notes/junk2021reproducibility.md#e23)
[^junk2021reproducibility-e25]: Junk & Lyons 2021，§7。[证据](../../../sources/notes/junk2021reproducibility.md#e25)
[^junk2021reproducibility-e26]: Junk & Lyons 2021，§4.2。[证据](../../../sources/notes/junk2021reproducibility.md#e26)
[^junk2021reproducibility-e28]: Junk & Lyons 2021，§3。[证据](../../../sources/notes/junk2021reproducibility.md#e28)
[^junk2021reproducibility-e29]: Junk & Lyons 2021，§7。[证据](../../../sources/notes/junk2021reproducibility.md#e29)
[^junk2021reproducibility-e30]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e30)
[^junk2021reproducibility-e31]: Junk & Lyons 2021，Media Summary。[证据](../../../sources/notes/junk2021reproducibility.md#e31)
[^junk2021reproducibility-e32]: Junk & Lyons 2021，§10。[证据](../../../sources/notes/junk2021reproducibility.md#e32)
[^junk2021reproducibility-e33]: Junk & Lyons 2021，§6.9。[证据](../../../sources/notes/junk2021reproducibility.md#e33)
[^ligo2018publication-e1]: LIGO LSC 2018，§2.A。[证据](../../../sources/notes/ligo2018publication.md#e1)
[^ligo2018publication-e2]: LIGO LSC 2018，§2.A。[证据](../../../sources/notes/ligo2018publication.md#e2)
[^ligo2018publication-e3]: LIGO LSC 2018，§2.A。[证据](../../../sources/notes/ligo2018publication.md#e3)
[^ligo2018publication-e4]: LIGO LSC 2018，§2.B。[证据](../../../sources/notes/ligo2018publication.md#e4)
[^ligo2018publication-e5]: LIGO LSC 2018，§2.B。[证据](../../../sources/notes/ligo2018publication.md#e5)
[^ligo2018publication-e6]: LIGO LSC 2018，§3.A。[证据](../../../sources/notes/ligo2018publication.md#e6)
[^ligo2018publication-e7]: LIGO LSC 2018，§3.B。[证据](../../../sources/notes/ligo2018publication.md#e7)
[^ligo2018publication-e8]: LIGO LSC 2018，§4.1。[证据](../../../sources/notes/ligo2018publication.md#e8)
[^ligo2018publication-e9]: LIGO LSC 2018，§5 Theses。[证据](../../../sources/notes/ligo2018publication.md#e9)
[^ligo2018publication-e10]: LIGO LSC 2018，§5 Theses。[证据](../../../sources/notes/ligo2018publication.md#e10)
[^ligo2018publication-e11]: LIGO LSC 2018，§1。[证据](../../../sources/notes/ligo2018publication.md#e11)
[^feynman1974cargo-e14]: Feynman 1974，Millikan 油滴实验之后。[证据](../../../sources/notes/feynman1974cargo.md#e14)
[^feynman1974cargo-e7]: Feynman 1974，Millikan 油滴实验之后。[证据](../../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e18]: Feynman 1974，无论结果如何都发表。[证据](../../../sources/notes/feynman1974cargo.md#e18)
[^roodman2003blind-e1]: Roodman 2003，§1。[证据](../../../sources/notes/roodman2003blind.md#e1)
[^roodman2003blind-e2]: Roodman 2003，§2。[证据](../../../sources/notes/roodman2003blind.md#e2)
[^roodman2003blind-e3]: Roodman 2003，§2。[证据](../../../sources/notes/roodman2003blind.md#e3)
[^roodman2003blind-e4]: Roodman 2003，§2。[证据](../../../sources/notes/roodman2003blind.md#e4)
[^roodman2003blind-e5]: Roodman 2003，§1。[证据](../../../sources/notes/roodman2003blind.md#e5)
[^roodman2003blind-e6]: Roodman 2003，§3.1。[证据](../../../sources/notes/roodman2003blind.md#e6)
[^roodman2003blind-e7]: Roodman 2003，§3.2。[证据](../../../sources/notes/roodman2003blind.md#e7)
[^roodman2003blind-e8]: Roodman 2003，§3.4。[证据](../../../sources/notes/roodman2003blind.md#e8)
[^roodman2003blind-e9]: Roodman 2003，§3.4。[证据](../../../sources/notes/roodman2003blind.md#e9)
[^roodman2003blind-e10]: Roodman 2003，§4。[证据](../../../sources/notes/roodman2003blind.md#e10)
[^golub2023blind-e1]: Golub 2023，§2。[证据](../../../sources/notes/golub2023blind.md#e1)
[^golub2023blind-e2]: Golub 2023，§2。[证据](../../../sources/notes/golub2023blind.md#e2)
[^golub2023blind-e3]: Golub 2023，§2。[证据](../../../sources/notes/golub2023blind.md#e3)
[^ginsparg2011twenty-e1]: Ginsparg 2011，开头。[证据](../../../sources/notes/ginsparg2011twenty.md#e1)
[^ginsparg2011twenty-e2]: Ginsparg 2011，开头。[证据](../../../sources/notes/ginsparg2011twenty.md#e2)
[^ginsparg2011twenty-e3]: Ginsparg 2011，第 2 页。[证据](../../../sources/notes/ginsparg2011twenty.md#e3)
[^ginsparg2011twenty-e4]: Ginsparg 2011，第 2 页。[证据](../../../sources/notes/ginsparg2011twenty.md#e4)
[^ginsparg2011twenty-e5]: Ginsparg 2011，第 7 页。[证据](../../../sources/notes/ginsparg2011twenty.md#e5)
[^ginsparg2011twenty-e6]: Ginsparg 2011，第 7 页。[证据](../../../sources/notes/ginsparg2011twenty.md#e6)
[^ginsparg2011twenty-e7]: Ginsparg 2011，第 7 页。[证据](../../../sources/notes/ginsparg2011twenty.md#e7)
[^arxivabout-e1]: arXiv，About arXiv。[证据](../../../sources/notes/arxivabout.md#e1)
[^arxivabout-e2]: arXiv，About arXiv。[证据](../../../sources/notes/arxivabout.md#e2)
[^arxivabout-e3]: arXiv，About arXiv。[证据](../../../sources/notes/arxivabout.md#e3)
[^arxivendorsement-e1]: arXiv，Endorsement。[证据](../../../sources/notes/arxivendorsement.md#e1)
[^arxivendorsement-e2]: arXiv，Endorsement，How can I get endorsed?。[证据](../../../sources/notes/arxivendorsement.md#e2)
[^arxivendorsement-e4]: arXiv，Endorsement。[证据](../../../sources/notes/arxivendorsement.md#e4)
[^vardi2009conferences-e1]: Vardi 2009，正文第 2 段。[证据](../../../sources/notes/vardi2009conferences.md#e1)
[^aps2024ethics-e1]: APS Ethics Standards 2024，Integrity。[证据](../../../sources/notes/aps2024ethics.md#e1)
[^aps2024ethics-e2]: APS Ethics Standards 2024，Research Results。[证据](../../../sources/notes/aps2024ethics.md#e2)
[^aps2024ethics-e3]: APS Ethics Standards 2024，Research Results。[证据](../../../sources/notes/aps2024ethics.md#e3)
[^aps2024ethics-e4]: APS Ethics Standards 2024，Authorship。[证据](../../../sources/notes/aps2024ethics.md#e4)
[^aps2024ethics-e6]: APS Ethics Standards 2024，Authorship。[证据](../../../sources/notes/aps2024ethics.md#e6)
[^aps2024ethics-e7]: APS Ethics Standards 2024，Authorship。[证据](../../../sources/notes/aps2024ethics.md#e7)
[^aps2024ethics-e8]: APS Ethics Standards 2024，Redundant Publication。[证据](../../../sources/notes/aps2024ethics.md#e8)
[^aps2024ethics-e9]: APS Ethics Standards 2024，Treatment of Supervisees。[证据](../../../sources/notes/aps2024ethics.md#e9)
[^aps2024ethics-e10]: APS Ethics Standards 2024，Research Results。[证据](../../../sources/notes/aps2024ethics.md#e10)
[^aps2024ethics-e11]: APS Ethics Standards 2024，Research Results。[证据](../../../sources/notes/aps2024ethics.md#e11)
[^aps2024ethics-e12]: APS Ethics Standards 2024，Redundant Publication。[证据](../../../sources/notes/aps2024ethics.md#e12)
[^aps2024ethics-e13]: APS Ethics Standards 2024，Redundant Publication。[证据](../../../sources/notes/aps2024ethics.md#e13)
[^aps2024ethics-e14]: APS Ethics Standards 2024，Social Media。[证据](../../../sources/notes/aps2024ethics.md#e14)
[^aps2024ethics-e15]: APS Ethics Standards 2024，Redundant Publication。[证据](../../../sources/notes/aps2024ethics.md#e15)
[^lyons2013discovering-e1]: Lyons 2013，§1。[证据](../../../sources/notes/lyons2013discovering.md#e1)
[^lyons2013discovering-e2]: Lyons 2013，§1。[证据](../../../sources/notes/lyons2013discovering.md#e2)
[^lyons2013discovering-e3]: Lyons 2013，§2，Look Elsewhere Effect。[证据](../../../sources/notes/lyons2013discovering.md#e3)
[^lyons2013discovering-e4]: Lyons 2013，§2，Look Elsewhere Effect。[证据](../../../sources/notes/lyons2013discovering.md#e4)
[^lyons2013discovering-e5]: Lyons 2013，§2。[证据](../../../sources/notes/lyons2013discovering.md#e5)
[^lyons2013discovering-e6]: Lyons 2013，§4。[证据](../../../sources/notes/lyons2013discovering.md#e6)
[^lyons2013discovering-e7]: Lyons 2013，§3。[证据](../../../sources/notes/lyons2013discovering.md#e7)
[^apsdataavailability-e1]: Physical Review 数据可获取性声明指南，Overview of Policies。[证据](../../../sources/notes/apsdataavailability.md#e1)
[^apsdataavailability-e2]: Physical Review 数据可获取性声明指南，Overview of Policies。[证据](../../../sources/notes/apsdataavailability.md#e2)
[^apsdataavailability-e3]: Physical Review 数据可获取性声明指南，Overview of Policies。[证据](../../../sources/notes/apsdataavailability.md#e3)
[^apsdataavailability-e4]: Physical Review 数据可获取性声明指南，Overview of Policies。[证据](../../../sources/notes/apsdataavailability.md#e4)
[^apsdataavailability-e5]: Physical Review 数据可获取性声明指南，What Qualifies as Research Data?。[证据](../../../sources/notes/apsdataavailability.md#e5)
[^apsdataavailability-e6]: Physical Review 数据可获取性声明指南，示例。[证据](../../../sources/notes/apsdataavailability.md#e6)
[^aassoftware-e2]: AAS Journals 软件政策，Guidelines for citation of software。[证据](../../../sources/notes/aassoftware.md#e2)
[^aassoftware-e3]: AAS Journals 软件政策，Guidelines for software articles。[证据](../../../sources/notes/aassoftware.md#e3)
[^aassoftware-e4]: AAS Journals 软件政策，Guidelines for software articles。[证据](../../../sources/notes/aassoftware.md#e4)
[^aassoftware-e5]: AAS Journals 软件政策，Review of Software。[证据](../../../sources/notes/aassoftware.md#e5)
[^cern2020opendata-e1]: CERN 2020 开放数据政策，Level 1。[证据](../../../sources/notes/cern2020opendata.md#e1)
[^cern2020opendata-e2]: CERN 2020 开放数据政策，Level 1。[证据](../../../sources/notes/cern2020opendata.md#e2)
[^cern2020opendata-e3]: CERN 2020 开放数据政策，Level 3。[证据](../../../sources/notes/cern2020opendata.md#e3)
[^cern2020opendata-e4]: CERN 2020 开放数据政策，Level 3。[证据](../../../sources/notes/cern2020opendata.md#e4)
[^cern2020opendata-e5]: CERN 2020 开放数据政策，Level 3。[证据](../../../sources/notes/cern2020opendata.md#e5)
[^jcgm2008gum-e1]: JCGM 100:2008（GUM），0.1。[证据](../../../sources/notes/jcgm2008gum.md#e1)
[^lejaeghere2016reproducibility-e3]: Lejaeghere 等人 2016，摘要。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e3)
[^lejaeghere2016reproducibility-e4]: Lejaeghere 等人 2016，摘要。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e4)
