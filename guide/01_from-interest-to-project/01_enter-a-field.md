# 进入领域、探索文献

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本章的道理适用于各学科，例子和具体做法以计算机为例。

## 你现在在哪里

你手里有一个方向，比如导师说"你看看大模型和智能合约安全"，或者你自己对它感兴趣。但你对这个方向知道得不多：不清楚大家在做什么，不知道该读哪些论文，也说不出谁是这个方向的主要研究者、论文都发在哪里。

打开学术搜索，结果有几百上千篇。你随便点开一篇，读了两个小时，还是没太懂，也不知道它重不重要。

## 这一阶段要解决什么

在有限的时间里，对这个方向建立一个**够用的了解**，具体来说，是拿到下面五样东西：

1. **一张领域地图**：这个方向分成哪几块，每块在解决什么问题、用什么办法；
2. **一份核心论文清单**：哪些论文被反复引用，其中有几篇你读透了；
3. **人和发表处**：谁在做这个方向，论文主要发在哪些会议或期刊上；
4. **每篇论文的笔记**：几个月后翻开还看得懂；
5. **一份问题记录**：读的过程中发现的不对劲、不够好、没人回答的地方。它是下一章[找到候选问题](02_find-problems.md)的原料。

这里说的"问题"，是指这片领域里不对劲、不够好、或者还不知道的地方，见[核心术语](../00_start-here/key-concepts.md#问题)。

**本章不教的：** 以综述本身为成果的研究，要求把相关研究找全、过程可复现，做法见[综述研究](../06_methods/review_study.md)。怎么写论文里的"相关工作"一节，见[讲清故事，写成论文](../04_write-and-publish/01_story-and-paper.md)。

## 这一章怎么用

下面八节大致按顺序走，但读、找、记、问是交替进行的：读到一篇好论文，会顺着它的引用去找新论文；和人聊一次，可能让你换一批关键词。

**给这一阶段定个时间。** 不要在背景阅读上耗个没完，你只能在"一知半解"的状态下开始自己的工作，因为没有时间学会所有需要知道的东西[^eisnerproblems-e8]。具体多久，和导师商量；我们的建议是先以几周为一轮，到期检查一次本章末尾的检查点 `[本项目分析]`。

---

## 1. 先写下：你要从文献里找什么

**开始搜论文之前，先花半小时写清楚你想知道什么。** 不写，你很容易被搜索结果牵着走，读了一堆和你无关的论文。

把方向拆成几个具体的小问题。以"大模型与智能合约安全"为例 `[本项目分析]`：

- 大模型在这里被用来做什么？找漏洞、修漏洞、写更安全的合约，还是别的？
- 现在效果怎么样？是怎么评测的？用的什么数据？
- 和传统的漏洞检测工具（如静态分析、模糊测试）比，各有什么长短？
- 大家公认还没解决的难点是什么？

这些小问题会随着阅读改变，这是正常的。它们的作用是让你每读一篇论文，都知道自己在找什么。

**写下来：** 用三到五个问句写出"我想从这个方向的文献里弄清楚什么"，再写一句"这一轮我打算用多长时间"。

## 2. 先找别人整理好的

**不要一上来就逐篇读研究论文。** 先看看有没有人已经替你列好了书单，比如课程大纲、学位论文里的文献综述章节[^eisnerread-e12]，以及下面说的教程和综述。

两种整理性的文章，用途不同：

| 类型 | 写给谁 | 你能从中得到什么 |
|---|---|---|
| 教程 | 外行；讲基本概念，配具体例子[^acm2026csurguidelines-e2] | 入门：基本术语、基本做法 |
| 综述 | 已有一般了解的读者；重在给已有文献分类、提出对这个方向的看法、评估趋势[^acm2026csurguidelines-e1] | 地图：这个方向分几块、各块的代表作 |

如果你对智能合约本身都不熟，先找一篇讲智能合约安全的教程或入门材料；如果基本概念已经清楚，直接找综述 `[本项目分析]`。

**找不到综述，就自己找起点论文。** 用学术搜索引擎（如谷歌学术）和几个精选的关键词，找三到五篇近期论文[^keshav2007read-e9]。选关键词时站在作者的角度想：他们会用什么说法描述这个问题[^eisnerread-e10]？比如同一件事，有人写"漏洞检测"，有人写"安全审计"，有人直接写某类漏洞的名字（如"重入"）。中英文、缩写和全称都要试 `[本项目分析]`。

**注意时效。** 大模型方向变化快，几年前的综述可能已经漏掉了最新的一批工作，要用近期论文补上 `[本项目分析]`。新工作可能先以预印本的形式发在 arXiv（一个预印本网站）上 `[本项目分析]`；arXiv 只做分类和基本的学术价值审核，**不做同行评审**[^arxivabout-e2]。预印本能让你看到最新进展，但读的时候要比读正式发表的论文更谨慎。

**写下来：** 列出你找到的综述、教程、课程大纲各几份；如果没有，列出三到五篇起点论文，以及你试过的每一组关键词。

## 3. 顺着引用，找出核心论文、关键的人和发表处

有了起点，接下来像滚雪球一样扩大：

1. **读起点论文的相关工作部分。** 在它们的参考文献里，找被反复引用的论文和反复出现的作者名字，他们就是这个方向的关键论文和关键研究者[^keshav2007read-e10]。
2. **双向追引用。** 找到一篇相关论文后，向后查它的参考文献，向前查谁引用了它[^eisnerread-e11]。拿一篇关键论文做"被引检索"，看后来有哪些论文引用了它，是了解一个领域的好办法[^taocareer-e16]。
3. **找出最主要的几个会议，翻它们近期的论文集。** 如果这些新论文都引用了某篇你还没找到的关键论文，就把它找来读，必要时再迭代一轮[^keshav2007read-e11]。
4. **先广后深。** 先读大量摘要，需要时略读正文，再决定哪些最值得精读[^eisnerread-e13]。

**第 3 步翻会议，是计算机的做法。** 计算机把会议论文当作发表研究成果的主要方式；据《ACM 通讯》（ACM 即美国计算机协会）主编 Vardi 所知，这在各学科中是独一份[^vardi2009conferences-e1]。所以在计算机领域，"主要发表处"多半是几个会议。有的方向有公认的顶级会议，例如安全领域常说的"前四"会议，它们最有影响力，事实上定下了这个社区做基准测试的惯例[^vanderkouwe2019sok-e27]。其他学科主要发在哪里、看哪些期刊或会议，本文资料没有逐一核对；问导师，或者看你收集的论文主要发在哪里 `[本项目分析]`。计算机会议文化的更多细节，见[计算机学科概况](../07_fields/computer-science/README.md)。

**关键的人，除了名字还要知道什么** `[本项目分析]`：他属于哪个组，这个组主要做哪一块，最近一两年发了什么。可以看他所在研究组的主页，那里有时列着这个组的全部论文。

**跟上新论文。** 可以订阅 arXiv 上你关心的学科分类，有新论文时收到通知[^taocareer-e27]。

**什么时候停：** 反复迭代后，新找到的论文引用的关键论文你都已经见过了，就可以停下这一轮 `[本项目分析]`。

**写下来：** 建一张核心论文清单，每行一篇：标题、作者、年份、发表处、被你的其他论文引用了几次、你读到第几遍。再列出三到五位关键研究者和两三个主要发表处。

## 4. 分层读：大多数读一遍，少数读透

**不要每篇都从第一页硬读到最后一页。** 最多分三遍读，每一遍有自己的目标，后一遍建立在前一遍之上[^keshav2007read-e1]：

| | 第一遍 | 第二遍 | 第三遍 |
|---|---|---|---|
| 用时 | 5～10 分钟[^keshav2007read-e2] | 最多一小时[^keshav2007read-e6] | 新手四五个小时，熟手约一小时[^keshav2007read-e8] |
| 读什么 | 标题、摘要、引言、各级小标题、结论[^keshav2007read-e3] | 更仔细地读，但跳过证明等细节，边读边记要点[^keshav2007read-e5] | 假设自己是作者，在脑中把这项工作重做一遍，再和原文对比[^keshav2007read-e7] |
| 读完应该能 | 说出论文类型、和哪些工作相关、假设是否成立、主要贡献、写得是否清楚[^keshav2007read-e4] | 向别人概括论文的主旨和支撑证据[^keshav2007read-e6] | 凭记忆重建论文结构，指出它的优点和缺点[^keshav2007read-e8] |

第一遍费脑的部分先跳过，只求知道论文要讲什么、为什么写、哪些对你是新的[^eisnerread-e1]。第一遍的作用之一，就是决定还要不要往下读[^keshav2007read-e2]。

**进入新方向时，至少要读透几篇。** 把它们读到弄懂每一句话、每一个符号在做什么，你才能真正学会这个方向常用的技术[^eisnerread-e7]。选哪几篇读透 `[本项目分析]`：一两篇综述或被引最多的经典论文，加上一两篇和你的兴趣最接近的近期论文。

**还可以更进一步：动手复现一篇。** 复现或实现别人的工作，虽然算不上原创，但对你的学习有用，有时对领域也有用[^eisnerproblems-e1]。比如把一篇用大模型检测合约漏洞的论文的实验在小数据上跑一遍，你会对它的数据、提示和评测方式了解得比读十遍还清楚 `[本项目分析]`。

**读得慢不丢人。** 有经验的研究者读一篇自己不熟的方向的论文，也要花好几个小时[^eisnerread-e9]。判断不了一篇论文哪里重要时，可以找引用它的论文，看别人怎么评价它[^eisnerread-e14]。

**写下来：** 在核心论文清单里，标出你打算读透的两到四篇，并写下为什么选它们。

## 5. 带着问题读

只跟着作者的思路读，读完常常只记住了作者想让你记住的。要主动地读：检查文中没有明说的假设，包括问题是怎么提出来的，以及从证据推到结论的过程。这不等于挑刺，读完你可以喜欢它，也可以不喜欢，但会更清楚为什么[^bender2003critical-e1][^bender2003critical-e2]。

**对每篇值得读第二遍的论文，回答这几个问题：**

1. **它要解决什么问题？** 分两层找：现实中想要的好处是什么，为什么这个问题没有简单的解法。这些常常没有明说，要你自己找出来[^griswoldread-e1][^griswoldread-e2]。
2. **这样提问，隐含了什么假设？数据是怎么收集的，可能有什么偏差？**[^bender2003critical-e3]
3. **它用什么证明自己的想法有价值？** 是论证、实现，还是实验[^griswoldread-e3]？比较公平吗？结果真的支持论文的主张吗？能推广到实验场景之外吗[^eisnerread-e8]？
4. **它的结果属于哪一种？** 用[核心术语](../00_start-here/key-concepts.md#研究套路)里的研究套路给它归类（构建改进、比较评估、测量……）。再看它的确定程度：是确证的发现、对实际现象的观察，还是作者的经验之谈[^shaw2002makes-e5]？在还没有确证发现的方向，观察和经验之谈也有价值[^shaw2002makes-e6]，但你要知道自己读到的是哪一种。
5. **证据够不够硬？** 好研究需要清楚、令人信服的证据，证据应来自实际使用或系统分析，而不只是有说服力的论证或教科书式的示例[^shaw2002makes-e7]。

以大模型检测合约漏洞的论文为例，第 2、3 个问题可以具体成 `[本项目分析]`：评测用的合约，模型训练时是不是已经见过？和哪些传统工具比了，比较的设置一样吗？只测了一类漏洞，还是很多类？

**批判地读之外，还要创造性地读。** 拆台总比建设容易。更难的是问：这篇论文里有哪些好想法？还能用到哪里[^eisnerread-e6]？三个好用的问题：如果有一个评审小组追问你这篇论文，哪个问题你答不上来[^vinitskypaper-e6]？我会补做什么实验，让它更有说服力[^vinitskypaper-e7]？如果基于它做一个新项目，我会做什么[^vinitskypaper-e8]？

**写下来：** 对你打算读透的那几篇，逐一写出上面五个问题的答案。答不出的，就是还没读完[^griswoldread-e6]。

## 6. 记笔记：一篇一份，再加一份问题记录

边读边写能让注意力集中，逼你主动投入[^eisnerread-e2]。光在页边做批注不够，还要写整体的笔记：提炼论文、和其他论文对比、记下自己的问题和想法[^eisnerread-e4]。不写，很容易读了一两个小时，却发现什么都没学到[^vinitskypaper-e1]。

**每篇论文一份笔记。** 可以直接套用这个模板 `[本项目分析]`：

> **出处**：作者、年份、标题、发表处、链接
>
> **为什么读**：它和我要弄清楚的哪个问题有关（第 1 节）
>
> **一句话总结**：它证明了什么
>
> **归类**：属于哪种研究套路；确定程度是发现、观察还是经验之谈
>
> **证据**：用了什么数据、和谁比较、主要结果
>
> **我的看法**：好在哪里，可疑在哪里
>
> **没读懂的地方**
>
> **它让我想到的问题**

几个要点：

- **读之前就填"为什么读"。** 填不出来，也许就不该读[^vinitskypaper-e2]。
- **总结分档。** 大多数论文一句话；需要时写一段；完整的总结只留给极少数论文[^vinitskypaper-e3]。
- **用自己的话写，写给几个月后的自己。** 重读时应能很快恢复当时的理解[^eisnerread-e5]。不要改写原摘要，要从你的角度概括[^griswoldread-e7]。
- **没读懂的地方集中记在一处**，以后回头看[^vinitskypaper-e4]。

**另建一份"问题记录"，这是本章最重要的产出之一。** 读的时候，凡是觉得不对劲、没说清、对不上的地方，一出现就记下来。把疑问写下来，常能引出原本没想清楚的东西，比如论文在关键问题上含糊，或者忽略了你认为重要的问题[^griswoldread-e8]。

本章只要求你**随手记**：每条一句话，注明来自哪篇论文，不必当场判断值不值得做 `[本项目分析]`。把有意思的东西集中记在一份文档里，更容易发现它们之间的联系[^nanda2025process-e4]。读论文时具体盯哪些地方（作者的简化、背后的假设、评估方式），见下一章[第 2 节](02_find-problems.md#2-从论文的空白和局限里找)和[第 4 节](02_find-problems.md#4-质疑已有工作的假设)；怎么把这份记录整理成带来源、验证办法的想法清单，见[第 8 节](02_find-problems.md#8-记一份想法清单)。

**写下来：** 建好论文笔记的模板和问题记录。读完本章的这一轮，问题记录里至少应该有十来条 `[本项目分析]`。

## 7. 画出领域地图

读了一二十篇之后，把它们放在一起看。**地图不是论文清单，而是分类。** 一个简单的画法 `[本项目分析]`：行是这个方向的几个子问题，列是研究套路，每一格填代表性论文。

下面是一个示意（格子里应填你实际读到的论文，这里只示范格式）：

| 子问题 | 构建改进 | 比较评估 | 测量 | 观察描述 |
|---|---|---|---|---|
| 用大模型找漏洞 | 论文 A、B | 论文 C | | |
| 用大模型修漏洞 | 论文 D | | | |
| 评测数据和指标 | | | 论文 E | |
| 大模型生成的合约本身是否安全 | | | | 论文 F |

画完后看三件事 `[本项目分析]`：

- **哪些格子很挤？** 很多人在做，竞争激烈，你需要特别清楚自己的不同；
- **哪些格子是空的？** 可能是没人想到，也可能是做不了或不值得做，要问懂行的人；
- **哪些想法流行起来了，哪些被遗忘了？** 选题的眼光，就是在观察哪些想法兴盛、哪些被遗忘的过程中慢慢练出来的[^schulman2020opinionated-e3]。积累判断最容易的办法，一是靠导师，二是看论文里什么做法管用[^nanda2025taste-e5]。

也可以照着综述的做法：给已有文献分类、提出自己对这个方向的看法、看出趋势[^acm2026csurguidelines-e1]。你的地图就是一份只写给自己的小综述。

**写下来：** 画出你的领域地图，在下面用三五句话写出你看到的格局：哪里挤、哪里空、什么在变。

## 8. 找懂行的人聊

文献只是一半。**导师是你最好的引导来源之一**，不只直接帮你做研究，还会明里暗里把你引向相关的研究者、会议、论文、公开问题和圈内常识[^taocareer-e23]。

具体可以做的：

- **拿着地图和问题记录去找导师。** 一边读一边自己想，定期把想法拿给能提醒你相关工作、给你指论文的人看[^eisnerproblems-e9]。带着具体的东西去，比问"我该读什么"有用得多 `[本项目分析]`。
- **问身边的研究者怎么选题。** 他们为什么做现在的问题？怎么挑的[^olah2021taste-e6]？
- **帮师兄师姐做点事。** 第一年可以找一位课题有意思的高年级学生，主动提出帮忙[^dredze2012successful-e18]。帮别人做一个你感兴趣方向的项目，能学到很多，又不必长期绑定[^olah2021taste-e17]。
- **听报告。** 别指望每场都能听懂全部，尤其是不熟悉的方向；只要学到了点东西，就不算白费[^taocareer-e33]。

为什么不能关起门来只读、和人聊怎样帮你找到问题，见下一章[和人聊](02_find-problems.md#7-和人聊)。本章聊天的重点是**补全地图**。

聊的时候可以直接问 `[本项目分析]`：我的地图漏了哪一块？哪几篇是必须读透的？问题记录里哪几条已经有人做过、哪几条你觉得值得想？

**写下来：** 每次聊完，记下对方推荐的论文和人、指出的遗漏、对你问题记录的评价，并更新地图和论文清单。

---

## 关键判断

**读到什么程度，可以开始找问题？** 不是"读完了"，而是 `[本项目分析]`：

| 你能做到 | 说明 |
|---|---|
| 用几句话向同学讲清这个方向分哪几块 | 有了地图 |
| 说出三五篇核心论文各自证明了什么、证据是什么 | 读透了几篇 |
| 新找到的论文大多已经在你的清单里 | 核心文献找得差不多了 |
| 问题记录里有十来条具体的疑问 | 有了找问题的原料 |

做不到第一条，继续读；四条都做到了，就进入下一章，不要等到"什么都懂"。

> **不同的看法：先大量读文献，还是先自己想？**
> - **先自己想：** Varian 认为，最终当然要做彻底的文献检索，但先在自己的想法上琢磨几周、再系统地检索，效果会好得多[^varian1997build-e3]。Eisner 也说不要在背景阅读上耗个没完，要早点开始自己思考，和阅读交替进行[^eisnerproblems-e8][^eisnerproblems-e9]。
> - **先查清楚：** Noble 提醒，最可怕的陷阱是做完整个项目，才发现开工之前就有人发表了同样的工作，所以要在一开始就做文献调研[^noble2023ten-e5]。
>
> 两种说法针对的是不同时刻 `[本项目分析]`：**找想法时**，读到够用（有地图、读透几篇）就开始自己想，边想边读；**决定投入一个具体项目之前**，必须针对它做一次仔细的查重，见[收敛成项目](03_converge.md#3-别人做过了吗)。

**这种调研能用来做什么、不能做什么。** 你这样有目的地挑论文，和大多数论文写"相关工作"的方式一样。它适合用来寻找有前景的选题；但它有抽样偏差、无法复现，容易只挑对自己有利的证据，所以**不能用来支撑"X 导致 Y"这类实证结论**[^ralph2022paving-e1][^ralph2022paving-e2]。如果你的问题本身需要把相关研究找全，就要做系统综述，见[综述研究](../06_methods/review_study.md)。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 一上来就逐篇读研究论文 | 很可能已经有综述、课程大纲替你整理好了[^eisnerread-e12] |
| 只用一个关键词搜 | 作者可能用了别的说法；要换位思考用词，并顺着引用双向找[^eisnerread-e10][^eisnerread-e11] |
| 每篇都从头到尾逐字读 | 时间花在不需要深读的论文上；应分遍读，每遍后决定是否继续[^keshav2007read-e1][^keshav2007read-e2] |
| 每篇都只略读 | 学不会这个方向的核心技术[^eisnerread-e7] |
| 把预印本当成已经过同行评审的结论 | arXiv 不做同行评审[^arxivabout-e2] |
| 只在论文上做批注，不写整体笔记 | 几个月后无法恢复理解[^eisnerread-e4][^eisnerread-e5] |
| 读的时候不记疑问 | 下一章找问题时没有原料，只能从头再读 `[本项目分析]` |
| 只读不聊 | 漏掉懂行的人一句话就能告诉你的相关工作[^eisnerproblems-e9] |
| 想读完所有文献再开始 | 不可能读完，只能在一知半解中开始[^eisnerproblems-e8] |
| 用自己挑的文献证明"X 导致 Y" | 非系统的调研有抽样偏差，撑不起实证结论[^ralph2022paving-e2] |

## 产出物

- 一份"我要从文献里弄清楚什么"的问题清单（第 1 节）
- 一份核心论文清单，标出读透的几篇（第 3、4 节）
- 关键研究者和主要发表处的名单（第 3 节）
- 每篇读过的论文一份笔记（第 6 节）
- 一份问题记录（第 6 节）
- 一张领域地图，加三五句格局判断（第 7 节）
- 和导师或懂行的人聊过的记录（第 8 节）

## 检查点

满足下面几条，可以进入下一步：

- [ ] 能用几句话讲清这个方向分哪几块，每块在解决什么
- [ ] 至少读透了两三篇论文，能说出它们的问题、证据和隐含的假设
- [ ] 能说出几位关键研究者和两三个主要发表处
- [ ] 新找到的论文大多已经在清单里
- [ ] 问题记录里有十来条具体的疑问，每条注明了出处
- [ ] 导师或懂行的人看过你的地图，指出的遗漏已经补上

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 搜出来的论文太多太杂，地图画不出来 | 本章第 1 节，和导师一起把方向收窄到一两个子问题 |
| 几乎找不到相关论文 | 本章第 2 节，换关键词，问导师；也可能这个方向的工作散在相邻领域 `[本项目分析]` |
| 读了很久，问题记录还是空的 | 本章第 5、6 节，带着问题重读几篇核心论文 |
| 读完发现对这个方向毫无兴趣 | 和导师谈，考虑换方向；不要硬撑 `[本项目分析]` |
| 下一章或收敛时发现对领域了解太少，判断不了重要性和新颖性 | 回到本章，针对那个问题再读一批 |

## 下一步

有了地图、核心论文和问题记录，下一步是从中筛出几个值得做的候选问题，见[找到候选问题](02_find-problems.md)。

[^eisnerproblems-e1]: Eisner，How to Find Research Problems，small bones。[证据](../../sources/notes/eisnerproblems.md#e1)
[^eisnerproblems-e8]: Eisner，How to Find Research Problems，Finally。[证据](../../sources/notes/eisnerproblems.md#e8)
[^eisnerproblems-e9]: Eisner，How to Find Research Problems，Finally。[证据](../../sources/notes/eisnerproblems.md#e9)
[^eisnerread-e1]: Eisner 2009，Multi-pass reading。[证据](../../sources/notes/eisnerread.md#e1)
[^eisnerread-e2]: Eisner 2009，Write as you read。[证据](../../sources/notes/eisnerread.md#e2)
[^eisnerread-e4]: Eisner 2009，High-level notes。[证据](../../sources/notes/eisnerread.md#e4)
[^eisnerread-e5]: Eisner 2009，High-level notes。[证据](../../sources/notes/eisnerread.md#e5)
[^eisnerread-e6]: Eisner 2009，High-level notes（引 Mitzenmacher）。[证据](../../sources/notes/eisnerread.md#e6)
[^eisnerread-e7]: Eisner 2009，Which parts to focus on。[证据](../../sources/notes/eisnerread.md#e7)
[^eisnerread-e8]: Eisner 2009，Which parts to focus on — Experiments。[证据](../../sources/notes/eisnerread.md#e8)
[^eisnerread-e9]: Eisner 2009，Set aside time。[证据](../../sources/notes/eisnerread.md#e9)
[^eisnerread-e10]: Eisner 2009，What to read。[证据](../../sources/notes/eisnerread.md#e10)
[^eisnerread-e11]: Eisner 2009，What to read。[证据](../../sources/notes/eisnerread.md#e11)
[^eisnerread-e12]: Eisner 2009，What to read。[证据](../../sources/notes/eisnerread.md#e12)
[^eisnerread-e13]: Eisner 2009，What to read。[证据](../../sources/notes/eisnerread.md#e13)
[^eisnerread-e14]: Eisner 2009，Which parts to focus on。[证据](../../sources/notes/eisnerread.md#e14)
[^keshav2007read-e1]: Keshav 2007，§2。[证据](../../sources/notes/keshav2007read.md#e1)
[^keshav2007read-e2]: Keshav 2007，§2.1。[证据](../../sources/notes/keshav2007read.md#e2)
[^keshav2007read-e3]: Keshav 2007，§2.1。[证据](../../sources/notes/keshav2007read.md#e3)
[^keshav2007read-e4]: Keshav 2007，§2.1。[证据](../../sources/notes/keshav2007read.md#e4)
[^keshav2007read-e5]: Keshav 2007，§2.2。[证据](../../sources/notes/keshav2007read.md#e5)
[^keshav2007read-e6]: Keshav 2007，§2.2。[证据](../../sources/notes/keshav2007read.md#e6)
[^keshav2007read-e7]: Keshav 2007，§2.3。[证据](../../sources/notes/keshav2007read.md#e7)
[^keshav2007read-e8]: Keshav 2007，§2.3。[证据](../../sources/notes/keshav2007read.md#e8)
[^keshav2007read-e9]: Keshav 2007，§3。[证据](../../sources/notes/keshav2007read.md#e9)
[^keshav2007read-e10]: Keshav 2007，§3。[证据](../../sources/notes/keshav2007read.md#e10)
[^keshav2007read-e11]: Keshav 2007，§3。[证据](../../sources/notes/keshav2007read.md#e11)
[^griswoldread-e1]: Griswold，"What are the motivations for this work?"。[证据](../../sources/notes/griswoldread.md#e1)
[^griswoldread-e2]: Griswold，"What are the motivations for this work?"。[证据](../../sources/notes/griswoldread.md#e2)
[^griswoldread-e3]: Griswold，"What is the work's evaluation of the proposed solution?"。[证据](../../sources/notes/griswoldread.md#e3)
[^griswoldread-e6]: Griswold，读论文的方法。[证据](../../sources/notes/griswoldread.md#e6)
[^griswoldread-e7]: Griswold，读论文的方法。[证据](../../sources/notes/griswoldread.md#e7)
[^griswoldread-e8]: Griswold，读论文的方法。[证据](../../sources/notes/griswoldread.md#e8)
[^bender2003critical-e1]: Bender 2003，第 1 页。[证据](../../sources/notes/bender2003critical.md#e1)
[^bender2003critical-e2]: Bender 2003，第 1 页。[证据](../../sources/notes/bender2003critical.md#e2)
[^bender2003critical-e3]: Bender 2003，第 1 页，研究论文问题 1～4。[证据](../../sources/notes/bender2003critical.md#e3)
[^vinitskypaper-e1]: Vinitsky，A template。[证据](../../sources/notes/vinitskypaper.md#e1)
[^vinitskypaper-e2]: Vinitsky，Why am I reading this paper?。[证据](../../sources/notes/vinitskypaper.md#e2)
[^vinitskypaper-e3]: Vinitsky，Summary。[证据](../../sources/notes/vinitskypaper.md#e3)
[^vinitskypaper-e4]: Vinitsky，Unresolved question。[证据](../../sources/notes/vinitskypaper.md#e4)
[^vinitskypaper-e6]: Vinitsky，Paper games。[证据](../../sources/notes/vinitskypaper.md#e6)
[^vinitskypaper-e7]: Vinitsky，Paper games。[证据](../../sources/notes/vinitskypaper.md#e7)
[^vinitskypaper-e8]: Vinitsky，Paper games。[证据](../../sources/notes/vinitskypaper.md#e8)
[^acm2026csurguidelines-e1]: ACM Computing Surveys（美国计算机协会的综述期刊）作者指南，Long Survey Paper。[证据](../../sources/notes/acm2026csurguidelines.md#e1)
[^acm2026csurguidelines-e2]: ACM Computing Surveys（美国计算机协会的综述期刊）作者指南，Tutorial Paper。[证据](../../sources/notes/acm2026csurguidelines.md#e2)
[^arxivabout-e2]: arXiv，About arXiv。[证据](../../sources/notes/arxivabout.md#e2)
[^taocareer-e16]: Tao，Career advice，Learn and relearn your field。[证据](../../sources/notes/taocareer.md#e16)
[^taocareer-e23]: Tao，Career advice，Talk to your advisor。[证据](../../sources/notes/taocareer.md#e23)
[^taocareer-e27]: Tao，Career advice，Take the initiative。[证据](../../sources/notes/taocareer.md#e27)
[^taocareer-e33]: Tao，Career advice，Attend talks and conferences。[证据](../../sources/notes/taocareer.md#e33)
[^vardi2009conferences-e1]: Vardi 2009，正文第 2 段。[证据](../../sources/notes/vardi2009conferences.md#e1)
[^vanderkouwe2019sok-e27]: van der Kouwe 等人 2019，§III-B。[证据](../../sources/notes/vanderkouwe2019sok.md#e27)
[^shaw2002makes-e5]: Shaw 2002，§1.2.3。[证据](../../sources/notes/shaw2002makes.md#e5)
[^shaw2002makes-e6]: Shaw 2002，§1.2.3。[证据](../../sources/notes/shaw2002makes.md#e6)
[^shaw2002makes-e7]: Shaw 2002，§2.3。[证据](../../sources/notes/shaw2002makes.md#e7)
[^nanda2025process-e4]: Nanda 2025，Exploration (Stage 2)。[证据](../../sources/notes/nanda2025process.md#e4)
[^nanda2025taste-e5]: Nanda 2025，How to learn it?。[证据](../../sources/notes/nanda2025taste.md#e5)
[^schulman2020opinionated-e3]: Schulman 2020，Honing Your Taste。[证据](../../sources/notes/schulman2020opinionated.md#e3)
[^olah2021taste-e6]: Olah 2021，Exercise 3。[证据](../../sources/notes/olah2021taste.md#e6)
[^olah2021taste-e17]: Olah 2021，Failure mode 2。[证据](../../sources/notes/olah2021taste.md#e17)
[^dredze2012successful-e18]: Dredze 2012，#32 First Year。[证据](../../sources/notes/dredze2012successful.md#e18)
[^varian1997build-e3]: Varian 1997，§1.3。[证据](../../sources/notes/varian1997build.md#e3)
[^noble2023ten-e5]: Noble 2023，Rule 4。[证据](../../sources/notes/noble2023ten.md#e5)
[^ralph2022paving-e1]: Ralph & Baltes 2022，§2.1。[证据](../../sources/notes/ralph2022paving.md#e1)
[^ralph2022paving-e2]: Ralph & Baltes 2022，§2.1。[证据](../../sources/notes/ralph2022paving.md#e2)
