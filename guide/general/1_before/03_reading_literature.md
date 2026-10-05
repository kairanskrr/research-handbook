# 读文献与文献调研

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲做自己的研究时怎么读论文、怎么做笔记、怎么找到一个方向的关键文献，以及怎么写"相关工作"来说明你的工作在哪里。以综述本身为成果的研究（系统综述、映射研究、综述论文）不在本章范围内，见[综述研究](../../fields/computer-science/research-types/review_study.md)（这是计算机领域的版本；跨学科通用的系统综述报告规范是 PRISMA 2020[^page2021prisma-e2]）。

**读完本章，你应该能：**

- 按自己的需要决定一篇论文读到多深，并分几遍读完；
- 带着一组固定的问题批判地读，而不是被动地跟着作者走；
- 写出几个月后还用得上的读书笔记；
- 从几篇论文出发，找到一个方向的关键论文和关键研究者；
- 写出能说清自己工作位置的相关工作，而不是一份论文清单。

---

## 1. 分几遍读，按需要决定读多深

不要从第一页硬读到最后一页。最多分三遍读，每一遍有自己的目标，后一遍建立在前一遍之上[^keshav2007read-e1]。

| | 第一遍 | 第二遍 | 第三遍 |
|---|---|---|---|
| 用时 | 5～10 分钟[^keshav2007read-e2] | 最多一小时[^keshav2007read-e6] | 新手四五个小时，熟手约一小时[^keshav2007read-e8] |
| 读什么 | 标题、摘要、引言、各级小标题、结论，扫一眼参考文献[^keshav2007read-e3] | 仔细读正文和图表，跳过证明等细节，边读边记要点[^keshav2007read-e5] | 假设自己是作者，在脑中把这项工作重做一遍，再和原文对比[^keshav2007read-e7] |
| 读完应该能 | 说出论文类型、和哪些工作相关、假设是否成立、主要贡献、写得是否清楚[^keshav2007read-e4] | 向别人概括论文的主旨和支撑证据[^keshav2007read-e6] | 凭记忆重建论文结构，指出它的优点、缺点和隐藏的假设[^keshav2007read-e7][^keshav2007read-e8] |

第一遍只求知道论文要讲什么、为什么写、哪些对你是新的，费脑的部分先跳过[^eisnerread-e1]。

**每读完一遍，都决定要不要继续。** 第一遍的作用之一，就是决定还要不要往下读[^keshav2007read-e2]。一个实用的办法是在读之前写下"我为什么要读这篇"；写不出来，也许就不该读。即使读了，做完总结后如果读它的理由不够有力，也可以停下[^vinitskypaper-e2][^vinitskypaper-e5]。

**容易错在哪：**

- **刚进入一个新方向，却每篇都只略读。** 进入新方向时，至少要把几篇论文读得极其透彻，弄懂每一句话、每一个符号在做什么，这样才能真正学会这个方向常用的技术[^eisnerread-e7]。
- **读得慢就焦虑。** 读得慢不丢人。即使是资深研究者，读一篇自己不熟悉的方向的论文，也要好几个小时[^eisnerread-e9]。
- **判断不了一篇论文哪里重要。** 可以找引用它的论文，看别人怎么评价它[^eisnerread-e14]。

## 2. 带着问题读：批判，但不是挑刺

批判性阅读（critical reading）是主动地和文本交锋：不只跟着作者的论证走，还要检查文中没有明说的假设，包括问题是怎么提出来的，以及从证据推到结论的过程[^bender2003critical-e1]。它**不等于挑刺**：读完你可以喜欢这篇论文，也可以不喜欢，但你会更清楚为什么[^bender2003critical-e2]。

**读一篇研究论文，依次回答这些问题：**

1. **它要解决什么问题？** 分两层找：现实中想要的好处是什么，为什么这个问题没有简单的解法。动机和问题最后会落到一个研究问题上，而这些要素常常没有明说，需要你自己找出来[^griswoldread-e1][^griswoldread-e2]。
2. **这样提问，隐含了什么假设？**[^bender2003critical-e3]
3. **数据是怎么收集的？收集过程中可能有什么偏差？**[^bender2003critical-e3]
4. **用什么来证明想法有价值？** 是论证、实现，还是实验[^griswoldread-e3]？如果你在意它的结论，就要仔细看实验设计和数据选择：比较公平吗？结果真的支持论文的主张吗？结论能推广到这个实验场景之外吗[^eisnerread-e8]？
5. **结论是什么？从这些证据推出这些结论，依赖了哪些假设？**[^bender2003critical-e4]
6. **你自己怎么看？** 想法好不好，有什么缺陷，最有意思和最有争议的地方在哪里[^griswoldread-e4]。

Bender 的问题清单最初是为社会语言学课程写的，她认为适用面更广；回答时还要记住作者是谁、写给谁看[^bender2003critical-e5]。

**不要只会挑刺。** 拆台总比建设容易，所以批判地读其实不难。更难的是创造性地读：这篇论文里有哪些好想法？还能推广到哪里[^eisnerread-e6]？下面几个问题能帮你从"读懂"走到"能用"：

- 如果有一个评审小组在追问你这篇论文，哪个问题你答不上来[^vinitskypaper-e6]？
- 我会补做什么实验，让这篇论文更有说服力[^vinitskypaper-e7]？
- 如果基于这篇论文做一个新项目，我会做什么[^vinitskypaper-e8]？

## 3. 边读边写笔记，写给将来的自己

边读边写能让注意力集中，迫使你主动投入[^eisnerread-e2]。笔记分两层：

**第一层：在论文上批注。** 用自己的话重述没讲清的地方；举出能说明作者观点的例子，也举出会难住作者的例子；质疑论文的主张和方法[^eisnerread-e3]。

**第二层：每篇论文一份总结笔记。** 光有批注不够[^eisnerread-e4]。下面是一个可以直接套用的模板 `[本项目分析，综合下列资料]`：

- **出处**：作者、年份、标题、链接
- **为什么读**：它和我的问题有什么关系[^vinitskypaper-e2]
- **一句话总结**；需要时再写一段话总结。完整总结只留给极少数论文[^vinitskypaper-e3]
- **核心收获**：从你自己的角度，这篇论文最主要的启示是什么[^griswoldread-e5]
- **与其他论文的对比**，以及**我的问题和后续想法**[^eisnerread-e4]
- **没读懂的地方**：集中记到一处，以后回头再看[^vinitskypaper-e4]

**为什么要写：** 不写，很容易读了一两个小时，却发现什么都没学到[^vinitskypaper-e1]。笔记是写给将来的自己的，几个月后重读时，你应该能很快恢复当时的理解[^eisnerread-e5]。写下疑问，常常还能引出原本没想清楚的东西，例如论文在关键问题上含糊，或者忽略了你认为重要的问题[^griswoldread-e8]。Griswold 的标准很直接：答不出他列的那组问题（动机、方案、评估、你的看法、核心收获），就还没读完[^griswoldread-e6]。

**容易错在哪：** 把原文摘要改写一遍当总结。可以试着写一段（英文）约 250 词的"自己的摘要"，但它不是改写原摘要，而是从你的角度概括动机、方案、评估和贡献[^griswoldread-e7]。

## 4. 找文献：从几篇论文出发，顺着引用找

**一个够用的流程**（改编自 Keshav[^keshav2007read-e9][^keshav2007read-e10][^keshav2007read-e11]）：

1. **找起点。** 用学术搜索引擎和几个精选的关键词，找三到五篇近期论文。选词时站在作者的角度想：他们会用什么说法描述这个问题[^eisnerread-e10]？
2. **先看别人是否已经列好了。** 综述文章、课程大纲、学位论文的文献综述章节，往往已经替你整理好了一份书单[^eisnerread-e12]。
3. **读起点论文的相关工作部分**，找出被反复引用的论文和反复出现的作者，他们就是这个方向的关键论文和关键研究者[^keshav2007read-e10]。
4. **看关键研究者最近在哪里发表**，翻阅这些期刊或会议的近期论文。Keshav 写的是计算机领域的"顶级会议"[^keshav2007read-e11]；在以期刊为主的学科，对应的是核心期刊 `[本项目分析]`。
5. **顺着引用双向找。** 找到一篇相关论文后，向后查它的参考文献，向前查谁引用了它[^eisnerread-e11]。
6. **先广后深。** 先读大量摘要，再决定哪些值得精读[^eisnerread-e13]。
7. **何时停：** 新找到的论文都引用了某篇你还没读的关键论文，就把它找来，必要时再迭代一轮[^keshav2007read-e11]；反复迭代都找不到新的关键论文时，就可以停下 `[本项目分析]`。

**知道这种调研的局限。** 这样找文献，是你有目的地挑选有用、相关或支持自己观点的论文，大多数论文的"相关工作"都是这样写出来的[^ralph2022paving-e1]。它适合用来发展理论、寻找有前景的选题；但它有抽样偏差、无法复现，容易只挑对自己有利的证据，所以**不能用来支撑"X 导致 Y"这类实证结论**[^ralph2022paving-e2]。如果你的问题需要"把相关研究找全"，就要做系统综述。检索和滚雪球的详细做法见[综述研究](../../fields/computer-science/research-types/review_study.md)，它是计算机领域的版本；其他学科可参考 PRISMA 2020，它规定系统综述报告里要写清哪些内容，但不指导具体怎么做[^page2021prisma-e2]。

## 5. 写相关工作：说清你的工作在哪里

相关工作不是为了证明"我读过很多论文"，而是为了说明你的工作和已有工作是什么关系：是在它们的基础上推进，还是提供了另一种做法[^shaw2003writing-e1]。

**同一段相关工作，从差到好**（据 Shaw 的示例改写[^shaw2003writing-e2][^shaw2003writing-e3]）：

| 写法 | 例子 |
|---|---|
| 很差 | "这个问题受到了广泛关注 [3,8,10,18,26,32,37]。" |
| 差 | "Smith 和 Jones 研究过这个问题。" |
| 好 | "Smith 的方法能处理 60% 的情况。Jones 能处理 80%，但只适用于某一类较简单的情况。" |
| 更好 | 在"好"的基础上再加一句："我们借用 Jones 方法的关键做法改进了 Smith 的方法，能处理 90% 的情况，并把适用范围放宽到只排除一类最难的情况。" |

Shaw 的原例来自软件工程，用的是"覆盖率""不含指针"这类说法，这里换成了通用说法。其他学科结构相同 `[本项目分析]`：说清每项工作做到了什么、限制在哪里，再说你在哪一点上往前推进。例如在历史研究中，可以写"A 用官方档案重建了这一事件，B 补充了地方报刊，但两人都没用到亲历者的日记；本文……"。

**怎么做：**

- **选适量的相关工作，做综合而不是罗列。** 不必列出每一篇相关研究[^ralph2020empirical-e19]；要说清每项工作做到了什么、局限在哪里[^shaw2003writing-e3]。
- **每一组相关工作都落到你自己的工作上**，说清你的贡献和它们是什么关系[^ralph2020empirical-e20]。
- **让文献调研反过来指导研究设计。** 写相关工作时，你会更清楚该用什么数据、和谁比较、要证明自己能做到别人做不到的什么[^eisnerfirst-e1]。
- **先写下自己的想法，再和文献对比。** Eisner 建议不要先写文献综述，先把自己的想法写出来，这样更可能找到新的角度[^eisnerfirst-e2]。

**为什么重要：** 你不讲清和已有工作的关系，审稿人就看不出你增加了什么新知识；看不出你是否了解相关工作，还会损害你的可信度[^shaw2003writing-e4]。

**容易错在哪：** 提到一项工作只是为了说它和本文无关；只罗列，不综合[^ralph2020empirical-e21]。

---

## 本章检查清单

**读论文**

- [ ] 读之前写下"为什么读这篇"[^vinitskypaper-e2]
- [ ] 第一遍结束时，能回答类型、背景、正确性、贡献、清晰度五个问题[^keshav2007read-e4]
- [ ] 对重要论文，能说出研究问题、数据来源和可能的偏差、从证据到结论依赖的假设[^bender2003critical-e3][^bender2003critical-e4]
- [ ] 在新方向上，至少有几篇论文读到能在脑中重做的程度[^eisnerread-e7][^keshav2007read-e7]

**做笔记**

- [ ] 每篇读过的论文都有一份总结笔记，包括一句话总结和自己的核心收获[^vinitskypaper-e3][^griswoldread-e5]
- [ ] 笔记用自己的话写，几个月后重读能很快恢复理解[^eisnerread-e5]
- [ ] 没读懂的地方集中记录，定期回头看[^vinitskypaper-e4]

**找文献**

- [ ] 先查有没有现成的综述、课程大纲、学位论文综述章节[^eisnerread-e12]
- [ ] 找出被反复引用的关键论文和关键研究者[^keshav2007read-e10]
- [ ] 对关键论文做了向后和向前的引用追踪[^eisnerread-e11]
- [ ] 清楚自己的调研是非系统的，没有用它支撑"X 导致 Y"这类结论[^ralph2022paving-e2]

**写相关工作**

- [ ] 每项相关工作都写了它做到了什么、局限在哪里[^shaw2003writing-e3]
- [ ] 写清了自己的贡献和相关工作的关系[^ralph2020empirical-e20]
- [ ] 没有逐篇罗列，也没有只为了说"不相关"而提及某项工作[^ralph2020empirical-e21]

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 每篇论文都从头到尾逐字读 | 时间花在不需要深读的论文上；应分遍读，每遍后决定是否继续[^keshav2007read-e1][^keshav2007read-e2] |
| 新方向的论文都只略读 | 学不会这个方向的核心技术[^eisnerread-e7] |
| 读完说不出研究问题和证据 | 只是看过，没有读懂；Griswold 认为答不出他列的问题就还没读完[^griswoldread-e6] |
| 把批判性阅读当成挑刺 | 批判性阅读是检查假设，读完可以喜欢也可以不喜欢[^bender2003critical-e2]；只挑刺还会错过论文里的好想法[^eisnerread-e6] |
| 只在论文上划线，不写总结 | 几个月后无法恢复理解[^eisnerread-e4][^eisnerread-e5] |
| 只用一个关键词检索 | 作者可能用了别的说法；应换位思考用词，并顺着引用双向找[^eisnerread-e10][^eisnerread-e11] |
| 用自己挑的文献支撑"X 导致 Y" | 非系统的调研有抽样偏差，撑不起实证结论[^ralph2022paving-e2] |
| 相关工作写成"A 做了 X，B 做了 Y" | 读者看不出你的工作和它们的关系[^shaw2003writing-e2][^ralph2020empirical-e21] |

## 延伸阅读

- **Keshav, How to Read a Paper**：两页的三遍阅读法，外加一个简单的文献调研流程。适合第一次系统地学怎么读论文。
- **Bender, Critical Reading**：一页的提问清单，分研究论文、教材和评论文章三类。适合打印出来放在手边。
- **Griswold, How to Read an Engineering Research Paper**：围绕动机、方案、评估、贡献的提问清单，附笔记表格。适合工程类论文。
- **Eisner, How to Read a Technical Paper**：怎么做批注和总结笔记、哪些部分可以先跳过、去哪里找文献。适合已经在读、但觉得效率低的人。
- **Vinitsky, Ways to Engage Deeply with a Paper**：一个读书笔记模板和几个让阅读更主动的"小游戏"。
- **Shaw 2003, Writing Good Software Engineering Research Papers**：其中"与已有工作的关系"一段给出了从差到好的相关工作写法。
- 需要把一个问题的相关研究找全时，见[综述研究](../../fields/computer-science/research-types/review_study.md)（计算机领域的版本）；跨学科的报告规范见 **Page 等人 2021, The PRISMA 2020 statement**。

各资料的链接见[原始资料列表](../../../sources/README.md)。

[^keshav2007read-e1]: Keshav 2007，§2。[证据](../../../sources/notes/keshav2007read.md#e1)
[^keshav2007read-e2]: Keshav 2007，§2.1。[证据](../../../sources/notes/keshav2007read.md#e2)
[^keshav2007read-e3]: Keshav 2007，§2.1。[证据](../../../sources/notes/keshav2007read.md#e3)
[^keshav2007read-e4]: Keshav 2007，§2.1。[证据](../../../sources/notes/keshav2007read.md#e4)
[^keshav2007read-e5]: Keshav 2007，§2.2。[证据](../../../sources/notes/keshav2007read.md#e5)
[^keshav2007read-e6]: Keshav 2007，§2.2。[证据](../../../sources/notes/keshav2007read.md#e6)
[^keshav2007read-e7]: Keshav 2007，§2.3。[证据](../../../sources/notes/keshav2007read.md#e7)
[^keshav2007read-e8]: Keshav 2007，§2.3。[证据](../../../sources/notes/keshav2007read.md#e8)
[^keshav2007read-e9]: Keshav 2007，§3。[证据](../../../sources/notes/keshav2007read.md#e9)
[^keshav2007read-e10]: Keshav 2007，§3。[证据](../../../sources/notes/keshav2007read.md#e10)
[^keshav2007read-e11]: Keshav 2007，§3。[证据](../../../sources/notes/keshav2007read.md#e11)
[^eisnerread-e1]: Eisner 2009，Multi-pass reading。[证据](../../../sources/notes/eisnerread.md#e1)
[^eisnerread-e2]: Eisner 2009，Write as you read。[证据](../../../sources/notes/eisnerread.md#e2)
[^eisnerread-e3]: Eisner 2009，Low-level notes。[证据](../../../sources/notes/eisnerread.md#e3)
[^eisnerread-e4]: Eisner 2009，High-level notes。[证据](../../../sources/notes/eisnerread.md#e4)
[^eisnerread-e5]: Eisner 2009，High-level notes。[证据](../../../sources/notes/eisnerread.md#e5)
[^eisnerread-e6]: Eisner 2009，High-level notes（引 Mitzenmacher）。[证据](../../../sources/notes/eisnerread.md#e6)
[^eisnerread-e7]: Eisner 2009，Which parts to focus on。[证据](../../../sources/notes/eisnerread.md#e7)
[^eisnerread-e8]: Eisner 2009，Which parts to focus on — Experiments。[证据](../../../sources/notes/eisnerread.md#e8)
[^eisnerread-e9]: Eisner 2009，Set aside time。[证据](../../../sources/notes/eisnerread.md#e9)
[^eisnerread-e10]: Eisner 2009，What to read。[证据](../../../sources/notes/eisnerread.md#e10)
[^eisnerread-e11]: Eisner 2009，What to read。[证据](../../../sources/notes/eisnerread.md#e11)
[^eisnerread-e12]: Eisner 2009，What to read。[证据](../../../sources/notes/eisnerread.md#e12)
[^eisnerread-e13]: Eisner 2009，What to read。[证据](../../../sources/notes/eisnerread.md#e13)
[^eisnerread-e14]: Eisner 2009，Which parts to focus on。[证据](../../../sources/notes/eisnerread.md#e14)
[^griswoldread-e1]: Griswold，"What are the motivations for this work?"。[证据](../../../sources/notes/griswoldread.md#e1)
[^griswoldread-e2]: Griswold，"What are the motivations for this work?"。[证据](../../../sources/notes/griswoldread.md#e2)
[^griswoldread-e3]: Griswold，"What is the work's evaluation of the proposed solution?"。[证据](../../../sources/notes/griswoldread.md#e3)
[^griswoldread-e4]: Griswold，"What is your analysis of the identified problem, idea and evaluation?"。[证据](../../../sources/notes/griswoldread.md#e4)
[^griswoldread-e5]: Griswold，"What is your take-away message from this paper?"。[证据](../../../sources/notes/griswoldread.md#e5)
[^griswoldread-e6]: Griswold，读论文的方法。[证据](../../../sources/notes/griswoldread.md#e6)
[^griswoldread-e7]: Griswold，读论文的方法。[证据](../../../sources/notes/griswoldread.md#e7)
[^griswoldread-e8]: Griswold，读论文的方法。[证据](../../../sources/notes/griswoldread.md#e8)
[^bender2003critical-e1]: Bender 2003，第 1 页。[证据](../../../sources/notes/bender2003critical.md#e1)
[^bender2003critical-e2]: Bender 2003，第 1 页。[证据](../../../sources/notes/bender2003critical.md#e2)
[^bender2003critical-e3]: Bender 2003，第 1 页，研究论文问题 1～4。[证据](../../../sources/notes/bender2003critical.md#e3)
[^bender2003critical-e4]: Bender 2003，第 1 页，研究论文问题 6～7。[证据](../../../sources/notes/bender2003critical.md#e4)
[^bender2003critical-e5]: Bender 2003，第 1 页。[证据](../../../sources/notes/bender2003critical.md#e5)
[^vinitskypaper-e1]: Vinitsky，A template。[证据](../../../sources/notes/vinitskypaper.md#e1)
[^vinitskypaper-e2]: Vinitsky，Why am I reading this paper?。[证据](../../../sources/notes/vinitskypaper.md#e2)
[^vinitskypaper-e3]: Vinitsky，Summary。[证据](../../../sources/notes/vinitskypaper.md#e3)
[^vinitskypaper-e4]: Vinitsky，Unresolved question。[证据](../../../sources/notes/vinitskypaper.md#e4)
[^vinitskypaper-e5]: Vinitsky，Unresolved question。[证据](../../../sources/notes/vinitskypaper.md#e5)
[^vinitskypaper-e6]: Vinitsky，Paper games。[证据](../../../sources/notes/vinitskypaper.md#e6)
[^vinitskypaper-e7]: Vinitsky，Paper games。[证据](../../../sources/notes/vinitskypaper.md#e7)
[^vinitskypaper-e8]: Vinitsky，Paper games。[证据](../../../sources/notes/vinitskypaper.md#e8)
[^ralph2022paving-e1]: Ralph & Baltes 2022，§2.1。[证据](../../../sources/notes/ralph2022paving.md#e1)
[^ralph2022paving-e2]: Ralph & Baltes 2022，§2.1。[证据](../../../sources/notes/ralph2022paving.md#e2)
[^shaw2003writing-e1]: Shaw 2003，§3.3。[证据](../../../sources/notes/shaw2003writing.md#e1)
[^shaw2003writing-e2]: Shaw 2003，§3.3 示例。[证据](../../../sources/notes/shaw2003writing.md#e2)
[^shaw2003writing-e3]: Shaw 2003，§3.3 示例。[证据](../../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e4]: Shaw 2003，§3.3。[证据](../../../sources/notes/shaw2003writing.md#e4)
[^ralph2020empirical-e19]: ACM SIGSOFT（美国计算机协会软件工程分会）实证研究标准，General Standard，加分项。[证据](../../../sources/notes/ralph2020empirical.md#e19)
[^ralph2020empirical-e20]: SIGSOFT General Standard，加分项。[证据](../../../sources/notes/ralph2020empirical.md#e20)
[^ralph2020empirical-e21]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e21)
[^eisnerfirst-e1]: Eisner 2010，What needs to be done?。[证据](../../../sources/notes/eisnerfirst.md#e1)
[^eisnerfirst-e2]: Eisner 2010，What needs to be done?。[证据](../../../sources/notes/eisnerfirst.md#e2)
[^page2021prisma-e2]: Page 等人 2021，PDF 第 2 页。[证据](../../../sources/notes/page2021prisma.md#e2)
