# 研究套路

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本篇的分类按各学科都能用的方式设计，例子和具体做法以计算机为例。"解读论证"一类多见于人文社科，目前只留占位。

你已经有了一个方向，也许还写出了几句候选结论。现在你想知道：我要做的到底是哪一种研究？要拿出什么样的证据？

这一页帮你定位：先看八种套路各回答什么问题，再按核心主张选出你的主要套路，最后看套路怎样帮你读文献、选问题、设计研究和写论文。

**研究套路**是这个项目主要靠什么逻辑产生新知识；它和主张、方法的区别，以及为什么要分清套路，见[核心术语](../00_start-here/key-concepts.md#研究套路)，这里不重复。

---

## 八种套路一览

每种套路有一篇单独的说明，讲它产生什么知识、需要什么证据、常用哪些方法。

| 套路 | 它回答的问题 | 典型主张（计算机例子） |
|---|---|---|
| [观察描述](observe_describe.md) | X 是什么样的？有多常见？ | "大模型生成的合约中，四成有重入漏洞" |
| [测量](measure.md) | X 该怎么测才准？现有测法可靠吗？ | "现有评测集存在数据泄露，新评测集更可靠" |
| [比较评估](compare_evaluate.md) | 已有的 A 和 B，哪个更好？ | "在真实合约上，工具 A 的检出率高于 B" |
| [解释因果](explain_causality.md) | 为什么会这样？是不是 X 导致了 Y？ | "提供漏洞模式提示会提高检出率" |
| [构建改进](build_improve.md) | 怎样把 X 做得更好？ | "新方法多发现三成漏洞" |
| [综合](synthesize.md) | 已有研究合起来说明了什么？ | "该方向的研究可归为四类，存在三个空白" |
| [证明](prove.md) | 在什么条件下，X 必然成立？ | "在条件 C 下，该算法一定终止" |
| [解读论证](interpret_argue.md) | 这段文本、这项制度、这个思想该怎样理解？ | 人文社科为主，目前只留占位 |

**这不是一套公认的标准分类。** 它是本手册为了帮新手定位而归纳的，在写主线和计算机篇时还会继续检验和调整。你读到的论文不会自称"我是比较评估"；别的书也可能把这些类别拆得更细或并得更粗。它和已有分类哪里对得上、哪里是本手册自己加的，见[这个分组从哪里来](#这个分组从哪里来)。把它当成一张帮你想清楚的地图，而不是必须遵守的规定 `[本项目分析]`。

## 怎样选出主要套路

**按核心主张来定，不按话题、也不按你会用的方法来定。** 具体分三步。

**第一步，写出核心主张。** 也就是论文最重要的那句结论。还写不出来，先回到[收敛成项目](../01_from-interest-to-project/03_converge.md#1-写出你想证明的那句话)第 1 节。

**第二步，看这句话属于哪一种。** 用下面的问法对照：

| 你的主张在说…… | 主要套路 |
|---|---|
| 某个现象存在、长什么样、有多常见、怎样分布 | 观察描述 |
| 某个东西过去测错了，或者新的测法更准 | 测量 |
| 几个**已有**的做法里，哪个在什么条件下更好 | 比较评估 |
| 某个因素**导致**了某个结果 | 解释因果 |
| 你**新做出来**的东西比已有的好 | 构建改进 |
| 一批已有研究合起来说明了什么 | 综合 |
| 某个结论在给定条件下必然成立 | 证明 |
| 对一段文本、一项制度或一种思想的新解释 | 解读论证 |

**第三步，有几类贡献时，分清主次。** 比如你提出了新的检测方法，又为了评测它整理了一个新数据集。问自己：如果只能让读者记住一句话，是哪一句？是"新方法多发现三成漏洞"，主要套路就是构建改进，数据集是次要贡献；是"现有评测集严重高估了结果"，主要套路就是测量，新方法只是顺带的例子。

**几对容易混的套路：**

- **比较评估和构建改进**：都会做对比实验。区别在于被比较的东西是不是你自己新做的。只比较已有工具，是比较评估；拿新方法和已有工具比，是构建改进。
- **比较评估和解释因果**："A 比 B 好"不等于"是 A 的某个特点导致了它更好"。要说"导致"，就要排除其他解释。
- **观察描述和解释因果**："X 和 Y 一起出现"是描述，"X 导致 Y"是因果。把相关当成因果是常见错误，证明因果通常比证明相关难得多[^easterbrook2008selecting-e36]。
- **观察描述和测量**：观察描述**用**测量得到关于现象的结论；测量套路的贡献是**测量办法本身**。"四成合约有漏洞"是观察描述；"过去的统计办法把漏洞数算多了"是测量。
- **观察描述和综合**：观察的对象是现象本身（合约、代码、开发者），综合的对象是已有的研究。

以上三步和判断表都是本手册的归纳 `[本项目分析]`。

**写下来：** 写出你的核心主张，用上表判断主要套路。如果有两类贡献，写出"只能留一句时留哪句"，据此分出主次。

## 这个分组从哪里来

八种套路是本手册归纳的。和它最接近的已有分类，是两份讲"研究问题有哪些类型"的资料，**都来自软件工程**：

- **Easterbrook 等人 2008**：讲怎样为软件工程的**实证研究**选方法，分析每种方法最适合回答哪类问题[^easterbrook2008selecting-e30]，并把弄清研究问题当作选方法的第一步之一[^easterbrook2008selecting-e31]。它只覆盖实证研究：它说实证研究回答的是关于"世界是什么样"的知识问题，而软件工程里大多数非实证研究关注的是另一类问题，即怎样设计出更好的做法[^easterbrook2008selecting-e38]，它把后者称为设计问题[^easterbrook2008selecting-e39]。
- **Shaw 2003**：把软件工程研究回答的问题分为四类：开发或分析的方法、具体实例的设计或评估、对一整类系统或技术的概括、存在性或可行性的探索[^shaw2003writing-e38]。

下表把八种套路和这两份资料对照。"没有对应"是指那份资料里找不到相应的问题类型 `[本项目分析]`：

| 本手册的套路 | Easterbrook 等人 2008 | Shaw 2003 |
|---|---|---|
| 观察描述 | 存在问题、描述与分类问题（"X 存在吗""X 是什么样""怎么分类"）[^easterbrook2008selecting-e32]；基础比率问题（现象通常多常见）[^easterbrook2008selecting-e34]；关系问题（"X 和 Y 相关吗"）[^easterbrook2008selecting-e35] | 可行性或探索（"X 存在吗，是什么样"）[^shaw2003writing-e8]；具体实例（"X 的现状如何"）[^shaw2003writing-e39]；概括（"X 有哪些种类"）[^shaw2003writing-e40] |
| 测量 | 只部分对应：描述与分类问题里的"怎么测量"[^easterbrook2008selecting-e32] | 只部分对应：分析方法（"怎样评估 X 的质量或正确性"）[^shaw2003writing-e25] |
| 比较评估 | 描述性比较问题（"X 和 Y 有什么不同"）[^easterbrook2008selecting-e33]；因果比较问题（"X 是否比 Z 导致更多的 Y"）[^easterbrook2008selecting-e37] | 具体实例（"Y 有多好""X 和 Y 比较如何"）[^shaw2003writing-e39]；"怎样在 X 和 Y 之间选"[^shaw2003writing-e25] |
| 解释因果 | 因果问题（"X 是否导致 Y"）[^easterbrook2008selecting-e37] | **没有对应** |
| 构建改进 | 设计问题（"做到 X 的有效办法是什么"）[^easterbrook2008selecting-e39] | 开发方法（"怎样做到 X，有没有更好的做法"）[^shaw2003writing-e25]；具体实例的更好设计[^shaw2003writing-e39] |
| 综合 | **没有对应**；只提到探索性问题可能已在文献里有答案，可用文献调研回答[^easterbrook2008selecting-e41] | **没有对应** |
| 证明 | **没有对应**（不在实证研究范围内） | 概括（"给定 X，Y 必然是什么"）[^shaw2003writing-e40]；形式模型要靠严格推导和证明来验证[^shaw2003writing-e9] |
| 解读论证 | **没有对应** | **没有对应** |

可以看到：综合和解读论证在两份资料里都没有对应；解释因果在 Shaw 里没有，证明在 Easterbrook 里没有；测量在两份里都只是某一类问题的一部分。这几类是本手册为了覆盖更多学科、让新手更好定位而单列或拆出的。两份资料都来自软件工程，所以这张对照对计算机最贴切；其他学科的研究问题分类，本文资料未涉及 `[本项目分析]`。

**你可能见过的另外两种分类。** 它们分的是别的维度，和套路不冲突，任何一种套路都可以放进去 `[本项目分析]`：

- **按目标分（OECD）**：基础研究为了弄懂现象背后的道理，不以特定应用为目标；应用研究指向一个具体的实际目标[^oecd2015frascati-e8]；试验发展利用已有知识，做出新产品、新流程或改进已有的[^oecd2015frascati-e9]。
- **按结论的性质分（Brooks，经 Shaw 转述）**：确证的发现（看是否真实、严谨）、观察（看是否有意思）、经验法则（看是否有用）[^shaw2002makes-e5]。

## 套路和方法有什么不同

**先定主张和套路，再挑方法。** 一种方法可以服务几种套路，一个项目也常常组合几种方法。下表是计算机里的例子 `[本项目分析]`：

| 方法（目前的位置） | 可以服务的套路 |
|---|---|
| [对照实验](../06_methods/controlled_experiment.md) | 解释因果、比较评估、构建改进 |
| [基准评测](../07_fields/computer-science/practices/benchmarking.md) | 比较评估、构建改进、测量 |
| [仓库挖掘](../07_fields/computer-science/practices/repository_mining.md) | 观察描述、解释因果 |
| [问卷调查](../06_methods/questionnaire_survey.md)、[访谈研究](../06_methods/interview_study.md) | 观察描述、解释因果（作为辅助证据） |
| [综述研究](../06_methods/review_study.md) | 综合 |
| [理论研究](../07_fields/computer-science/practices/theoretical_research.md) | 证明 |

为什么要组合：每种方法都有已知的缺陷，只能提供有限的证据；但各方法的缺陷不同，所以可以挑几种互相弥补[^easterbrook2008selecting-e1]。选哪几种没有固定配方，要看你有多少资源、能不能接触到研究对象、能不能控制想研究的变量，以及你自己会什么[^easterbrook2008selecting-e42]。

为什么不能反过来，从"我会做实验"或"别人都这么做"出发：照搬别人为完全不同的问题用过的研究范式，会导致严重的错配[^shaw2003writing-e41]。怎样从套路走到具体方法，见[选择套路与方法](../02_from-project-to-study/02_choose-strategy-and-method.md)。

## 为什么从头到尾都要想着套路

套路不只是设计实验时才用得上，它在每个阶段都帮你问对问题。下面的分阶段建议是本手册的归纳；引用的资料多来自软件工程，其他学科以本学科的规矩为准 `[本项目分析]`。

**读文献时。** 先问一篇论文的核心主张属于哪种套路，再按那种套路的标准评价它。不要套用不适用的质量标准，例如对没有因果关系的研究要求内部效度（因果结论是否真的成立）[^ralph2020empirical-e24]。

**选问题时。** 有些套路常常要先做。研究刚起步时，通常要先问探索性问题，把现象弄清楚[^easterbrook2008selecting-e32]；设计问题的前提是相关的知识问题已经回答过，对要解决的问题有足够了解[^easterbrook2008selecting-e40]。放到例子里：如果大家连"现有评测结果可不可信"都不清楚，先做一个测量项目，可能比急着做新检测方法更有价值。反过来，探索性问题也可能已经在文献里有答案，这时读文献就能回答，不必自己再做一遍[^easterbrook2008selecting-e41]。

**设计研究时。** 问题、结果和验证方式不能随意搭配。用实地研究去验证一个形式模型是否正确，是错配[^shaw2003writing-e14]；形式模型要靠严格推导和证明，而不是一两个简单例子[^shaw2003writing-e9]。对认真思考的研究者来说，为问题选对结果类型通常不难；难的是选好验证方式，它常常是论文做不成的原因[^shaw2003writing-e41][^shaw2003writing-e42]。每篇套路说明都列出了该套路需要的证据，可以对照着检查。

**写论文时。** 读者要能一眼看出你交出的是哪一种知识。如果审稿人看不出你是提出了新的评估技术、把旧技术用到了新例子上，还是在评估一项成熟技术，说明你没写清楚[^shaw2003writing-e31]。验证也要和主张对应：声称性能提升，就要分析性能，而不是易用性或通用性[^shaw2003writing-e12]。

**写下来：** 找一篇你最近读的论文，写出它的核心主张和主要套路，再写一句：按这个套路，它最需要的证据是什么，它给了没有。

## 下一步

- 想知道某种套路具体要做什么：点上面表格里的链接。
- 已经定了套路，要选具体方法：见[选择套路与方法](../02_from-project-to-study/02_choose-strategy-and-method.md)。
- 还没写出核心主张：回到[收敛成项目](../01_from-interest-to-project/03_converge.md)。

[^shaw2002makes-e5]: Shaw 2002，§1.2.3。[证据](../../sources/notes/shaw2002makes.md#e5)
[^ralph2020empirical-e24]: ACM SIGSOFT 实证研究标准，General Standard，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e24)
[^oecd2015frascati-e8]: OECD 2015，第 2.9 段。[证据](../../sources/notes/oecd2015frascati.md#e8)
[^oecd2015frascati-e9]: OECD 2015，第 2.9 段。[证据](../../sources/notes/oecd2015frascati.md#e9)
[^easterbrook2008selecting-e1]: Easterbrook 等人 2008，§1.0。[证据](../../sources/notes/easterbrook2008selecting.md#e1)
[^easterbrook2008selecting-e30]: Easterbrook 等人 2008，摘要。[证据](../../sources/notes/easterbrook2008selecting.md#e30)
[^easterbrook2008selecting-e31]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e31)
[^easterbrook2008selecting-e32]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e32)
[^easterbrook2008selecting-e33]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e33)
[^easterbrook2008selecting-e34]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e34)
[^easterbrook2008selecting-e35]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e36]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e37]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e37)
[^easterbrook2008selecting-e38]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e38)
[^easterbrook2008selecting-e39]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e39)
[^easterbrook2008selecting-e40]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e40)
[^easterbrook2008selecting-e41]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e41)
[^easterbrook2008selecting-e42]: Easterbrook 等人 2008，§1.0。[证据](../../sources/notes/easterbrook2008selecting.md#e42)
[^shaw2003writing-e38]: Shaw 2003，§2.1。[证据](../../sources/notes/shaw2003writing.md#e38)
[^shaw2003writing-e25]: Shaw 2003，§2.1，表 1。[证据](../../sources/notes/shaw2003writing.md#e25)
[^shaw2003writing-e39]: Shaw 2003，§2.1，表 1。[证据](../../sources/notes/shaw2003writing.md#e39)
[^shaw2003writing-e40]: Shaw 2003，§2.1，表 1。[证据](../../sources/notes/shaw2003writing.md#e40)
[^shaw2003writing-e8]: Shaw 2003，§2.1，表 1。[证据](../../sources/notes/shaw2003writing.md#e8)
[^shaw2003writing-e9]: Shaw 2003，§4.1。[证据](../../sources/notes/shaw2003writing.md#e9)
[^shaw2003writing-e14]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e14)
[^shaw2003writing-e41]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e41)
[^shaw2003writing-e42]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e42)
[^shaw2003writing-e31]: Shaw 2003，§2.3。[证据](../../sources/notes/shaw2003writing.md#e31)
[^shaw2003writing-e12]: Shaw 2003，§4.3。[证据](../../sources/notes/shaw2003writing.md#e12)
