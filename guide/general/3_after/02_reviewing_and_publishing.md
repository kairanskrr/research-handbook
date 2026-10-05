# 审稿、回复审稿意见与发表

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲论文写完之后的事：同行评审怎么运作、投稿前该检查什么、自己当审稿人时怎么写审稿意见、怎么回复审稿意见，以及被拒稿后怎么办。怎么把论文写好，见[写作](../3_after/01_writing.md)。

本章的资料多来自计算机领域的会议和生物信息学期刊。不同学科、不同期刊的流程细节（是否有作者回复环节、字数限制、是否允许补实验）差别很大，**动手前先读清楚你所投期刊或会议的投稿和审稿说明**。

**读完本章，你应该能：**

- 说清审稿人在判断什么、最后由谁做决定；
- 投稿前替审稿人先挑一遍毛病；
- 写出一份公正、具体、有建设性的审稿意见；
- 正确判断"新颖性"，避开常见的不成立的批评；
- 写出一份让做决定的人容易看懂的回复；
- 把拒稿变成下一轮修改的清单。

---

## 1. 先弄清审稿人在判断什么、谁做决定

**审稿有两个作用**：一是判断研究做得好不好，二是给作者反馈，帮助改进[^hicks2014reviewing-e1]。无论论文最后录用与否，第二个作用都成立[^roscoe2007reviews-e1]：审稿人是来帮助作者的，即使结论是拒稿[^bourne2006reviewers-e4]。

**审稿人主要判断四件事**[^hicks2014reviewing-e2]：

1. 这个想法或研究有没有意思、有没有用？
2. 它是新的吗，还是和已有工作大量重叠？
3. 论文得出的结论对不对？
4. 写得够不够清楚，别人能不能看懂？

这几件事里，**可信排在重要前面**：可信但不那么重要的论文可以录用；不可信的论文，看起来再重要也不能录用[^ralph2020empirical-e53]。

**谁做决定。** 期刊通常由编辑根据审稿意见做决定。计算机领域的会议通常由程序委员会（Program Committee，PC）开会讨论，有的会议还设领域主席（Area Chair，AC），他们可能只读审稿意见和作者回复，不再细读论文[^parikh2020rebuttals-e2]。程序委员会的目的是选出最好的一组论文，而不是给每篇论文下判决[^roscoe2007reviews-e14]。

在计算机等以会议为主的领域，讨论时一篇论文往往需要至少一位审稿人愿意站出来为它争取。如果没有这样的"支持者"（champion），被录用的机会很小[^zeller2012rebuttals-e1][^hicks2014response-e2]。

**对结果要有平常心。** 真实的评审更像一个拥挤的集市：每个人时间有限、注意力有限、信息不全[^parikh2020rebuttals-e16]。最终结果是全体审稿人的集体判断，"更像艺术而不是科学"[^hicks2014reviewing-e10]。

---

## 2. 投稿前先替审稿人挑一遍毛病

审稿人是在很多篇论文之间分配有限的精力。一个审稿人的原话是：**粗糙的论文让人觉得研究也粗糙**[^allman2001plea-e1]。投稿前至少做到：

- [ ] 校对全文[^allman2001plea-e2]
- [ ] 遵守页数限制和格式要求[^allman2001plea-e4]，读过并照做投稿指南，编辑和审稿人都会照它来看[^bourne2005published-e8]
- [ ] 提前回答审稿人一眼就会问的简单问题，例如"这个参数为什么取 17"[^allman2001plea-e3]
- [ ] 请与这项工作没有利害关系的同事读一遍，最好包括不做这个方向的人[^bourne2005published-e7]

**为什么要在投稿前下功夫**：Bourne 建议把精力放在投稿前提高稿件质量上[^bourne2005published-e6]。稿件有根本缺陷时，审稿意见多半停留在指出缺陷，很难给出进一步的改进建议 `[本项目分析]`。

**选投稿去处**：

- **尽早决定投哪里**，因为它决定了论文的形式、细节程度和对新颖性的要求[^bourne2005published-e5]。有的期刊提供投稿前咨询，可以利用[^bourne2005published-e10]。
- 了解目标期刊或会议的标准：判断一篇论文是否够格，审稿人参照的是这个期刊或会议、这个社区的标准[^hicks2014reviewing-e9]。在计算机领域，至少在理论上，会议论文报告完整、成熟的工作，研讨会（workshop）论文可以是早期工作或观点[^roscoe2007reviews-e12]。
- Bourne 主张**重质不重量**：宁可在高质量期刊发一篇，也不要在较差的期刊发多篇[^bourne2005published-e9]。

---

## 3. 当审稿人：写一份公正、具体、有用的审稿意见

新手可以先跟着导师练：请导师把正在审的论文交给你，由你写审稿意见的初稿[^bourne2005published-e4]；之后可以请导师讲讲他会怎么改 `[本项目分析]`。审别人的论文会帮你写好自己的论文[^bourne2005published-e4]。

**接之前先问自己**：

- 能按时完成吗？不能就推掉[^bourne2006reviewers-e1]。
- 有没有利益冲突？只要有一点可能就不要接[^bourne2006reviewers-e2]；拿不准时告诉编辑或主席，让他们决定[^mightreview-e2]。如果稿件做的正是你也在做的问题，告知编辑或主席，并回避讨论[^mightreview-e10]。

**审稿意见的结构**：

1. **摘要**：用自己的话中立地概述论文讲什么、为什么重要、做了什么，不带评判[^hicks2014reviewing-e3][^roscoe2007reviews-e3]。作者和其他审稿人能从中看出你有没有读懂。
2. **贡献**：写出你认为论文的贡献是什么[^roscoe2007reviews-e4]。
3. **具体意见**：逐条列出，便于阅读和回复，并注明每条对是否录用有多关键[^bourne2006reviewers-e5]；把"必须改"和"建议改"分开[^ralph2020empirical-e54]。论文的亮点也要写[^roscoe2007reviews-e6]。
4. **结论**：给出明确的推荐意见和理由[^roscoe2007reviews-e7]，不要骑墙[^bourne2006reviewers-e6]。

动笔写的过程本身就在检验你的判断：写过审稿意见的人，通常比只读过论文的人更有资格评价它[^roscoe2007reviews-e2]。已经花了几个小时读论文，再多花半小时到一小时写改进建议，很值得[^hicks2014reviewing-e12]。

**文字要和分数一致。** 文字是主体，分数只是文字的概括；作者读完文字，应该能猜出你打了几分[^hicks2014reviewing-e4]。最关键的论点放最前面，细节放后面[^hicks2014reviewing-e5]。

**怎么写批评**：

- **每条批评都要具体、可操作。** 批评和表扬都要给出具体理由[^bourne2006reviewers-e3]；含糊、无法据此修改的批评是反面做法[^ralph2020empirical-e56]。
- **指出问题的同时给出修改建议**[^mightreview-e5]。把"系统没有处理 X"改写成"如果讨论系统如何处理 X，论文会更有说服力"[^roscoe2007reviews-e9]。建议拒稿时，说明具体什么能改变你的判断[^mightreview-e6]。
- **怀疑有错误时，用提问代替断言**[^roscoe2007reviews-e5]。你总有可能误解了论文[^roscoe2007reviews-e10]。
- **批评论文，不批评人**，不夸张[^hicks2014reviewing-e6]，不嘲讽论文[^roscoe2007reviews-e11]，也不借审稿意见卖弄机智[^mightreview-e7]。匿名让审稿人有很大的权力而很少被问责[^roscoe2007reviews-e8]，匿名是盾牌，不是武器[^mightreview-e9]。

**怎么保持公正**：

- 研究生写的审稿意见往往最负面[^mightreview-e3]。先列出论文的优点，再批评。
- 记下自己的第一印象和原因，避免只找支持第一印象的证据[^mightreview-e4]。
- 不要让作者的名气或单位影响判断[^mightreview-e8][^ralph2020empirical-e59]。
- 不要借审稿推销自己的观点、方法或论文[^bourne2006reviewers-e7][^ralph2020empirical-e57]。
- 说明自己的局限：哪些部分你判断不了、没有审[^ralph2020empirical-e55]；拿不准时，在"审稿人信心"一栏如实打低分[^roscoe2007reviews-e13]，或在只给编辑看的意见里说明自己的不足和偏向[^bourne2006reviewers-e12]。
- 只给编辑看的意见也必须有审稿正文支撑，不能正文平和、私下却说"绝不该发表"[^bourne2006reviewers-e9]。
- **稿件保密**：不透露、不转给别人[^hicks2014reviewing-e7]；未经编辑同意，不要给同事看[^bourne2006reviewers-e11]。

> **不同的看法：每篇论文都要从头到尾细读吗？**
> - Hicks 认为，有用性和新颖性是"命门"，可以先仔细读引言、结论和相关工作，中间部分略读；这两项不过关，就不必深挖细节[^hicks2014reviewing-e11]。
> - ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把"略读稿件，而不是逐字阅读、检查每张图表"列为审稿的反面做法[^ralph2020empirical-e58]。
>
> 实际操作中 `[本项目分析]`：决定**是否值得深入**时，可以先抓引言和结论；但只要你要对结论的对错下判断，就必须细读相关部分。如果你只读了一部分，在审稿意见里说清楚[^ralph2020empirical-e55]。

---

## 4. 正确判断新颖性，不提不成立的批评

Black 观察到，审稿人常把复杂、困难、技术性强误当成新颖[^black2022novelty-e1]。

**常见的误判**：

- **把复杂当新颖。** 只改了一处，但以前没人想到这样改，这本身就是新颖的[^black2022novelty-e2]。简单的想法可能重要，也可能平凡；"平凡"指不重要，而不是简单[^black2022novelty-e6]。
- **事后诸葛亮。** 新颖性要站在想法出现之前评判；一个想法讲完之后显得理所当然，不减损它的新颖性[^black2022novelty-e3]。
- **只看技术细节。** 新数据集、旧方法的新用法，都可以是新颖的[^black2022novelty-e4]。支持已有假设、对已有发现给出新解释的论文也有价值[^bourne2006reviewers-e8]。
- **轻易断定"没用"。** 新想法的用处很难提前判断，审稿人的想象力也有限[^black2022novelty-e5]。

和已有工作有重叠，不等于没有新意；如果提供了新想法和有用的数据，仍然有一定新颖性[^hicks2014reviewing-e8]。**要说"不新"，就必须给出贡献几乎完全相同的已发表文献**[^ralph2020empirical-e60]。更好的写法是：指出相似的工作，请作者说明比它多做了什么[^roscoe2007reviews-e15]。补充作者漏掉的文献（不是你自己的）是简单有效的帮助[^bourne2006reviewers-e10]。

**这些批评不成立**（依据 SIGSOFT 实证研究标准，原文针对软件工程的实证研究；`[本项目分析]` 其中大多跨学科适用）：

- 说"缺细节""漏了重要文献""质量低"，却不具体指出是哪些[^ralph2020empirical-e61]
- 因为是重复研究而拒稿[^ralph2020empirical-e62]
- 因为审稿人自己会用别的方法或设计而拒稿[^ralph2020empirical-e25]
- 因为结果是负面的而拒稿[^ralph2020empirical-e41]
- 拿该类研究固有的局限来批评，例如批评案例研究普适性低[^ralph2020empirical-e25]
- 要求做与研究目的无关的额外分析[^ralph2020empirical-e64]

---

## 5. 回复审稿意见：写给做决定的人看

有的会议在决定前允许作者回复（author response，也叫 rebuttal），期刊则通常在修改稿中附回复信（response letter，逐条说明你怎样回应每条审稿意见、改了哪里）。作者回复最初是为了让作者指出审稿意见中的事实错误[^hicks2014response-e1]。

**先摆正预期。** 回复救不了一篇差论文；只有论文处在录用边缘，或审稿人犯了明显错误时，它才起作用[^zeller2012rebuttals-e8]。在计算机等以会议为主的领域，目标不是说服每个人，而是让至少一位审稿人愿意为你争取[^hicks2014response-e2]。

**核心原则**：回复要全面、直接、让审稿人和领域主席容易看懂[^parikh2020rebuttals-e1]。

**想清楚谁在读。** 除了审稿人，还有做决定的领域主席或编辑，他们可能只读审稿意见和你的回复；新手往往只顾前者[^parikh2020rebuttals-e2][^parikh2020rebuttals-e3]。审稿人读回复时，可能已是写完意见一个月后，细节早忘了[^hicks2014response-e7]。**检验标准**：一个中立的第三方只读你的回复，能不能判断问题是否已解决[^parikh2020rebuttals-e4]？

**步骤**：

1. **把所有意见逐条列进表格**，标出各审稿人的共同问题，避免遗漏[^parikh2020rebuttals-e5]。
2. **初稿先覆盖每一点，再按重要性删减**到字数限制内[^parikh2020rebuttals-e6]。
3. **开头**：先简要总结审稿人肯定的地方[^parikh2020rebuttals-e13]；最想让大家知道的一件事放在最前面，因为很多人只读开头[^zeller2012rebuttals-e3]。
4. **按重要性排序**：多数审稿人共同的主要问题最先、明确地回答[^hicks2014response-e5]；先答你有把握的大问题，再到小问题[^parikh2020rebuttals-e7]。
5. **每条都"先引用、再直接回答"**：用接近审稿人原话的方式点出问题[^hicks2014response-e6]，第一句就给答案，再展开[^parikh2020rebuttals-e8]。给审稿人和问题编号（R1Q1、R1Q2……）[^zeller2012rebuttals-e10]。

**写法要点**：

- 答案论文里已经有，就指出在哪一节、哪张表，并在回复里复述[^hicks2014response-e8][^parikh2020rebuttals-e12]。
- 有分歧时拿数据说话，而不是争论[^parikh2020rebuttals-e9]。
- 做不到的就如实说（例如不允许补实验、资源不够）[^parikh2020rebuttals-e11]。
- 错别字、语言问题不必在回复里争取，篇幅留给重大问题[^zeller2012rebuttals-e5]。
- 礼貌、感谢：审稿人是义务付出时间[^hicks2014response-e3]；审稿是辛苦活，再不起眼的意见里也有对你有用的东西[^zeller2012rebuttals-e7]。争辩可能让审稿人更坚定地反对，寻找共识更有效[^parikh2020rebuttals-e14]。
- 遇到明显不负责任或没有依据的意见，可以客观指出，让其他人适当降低它的分量[^parikh2020rebuttals-e15]。但如果**所有**审稿人都误解了论文，问题不在审稿人[^zeller2012rebuttals-e6]。

> **不同的看法：要不要回应每一条意见？**
> - Hicks：不必。篇幅有限，面面俱到会冲淡重点；声明已考虑全部意见、未逐条回应的会在修改中处理即可[^hicks2014response-e4]。
> - Zeller：对反对者提出的问题要逐条反驳，给支持者讨论时提供论据[^zeller2012rebuttals-e2]。Parikh 等人也主张初稿覆盖每一点，再删减[^parikh2020rebuttals-e6]。
> - 期刊的修改稿：Bourne 建议在回复信和正文修改中回应**每一条**意见[^bourne2005published-e2]。
>
> 实际操作中 `[本项目分析]`：有严格字数限制的会议回复，优先保证主要问题和反对者的关键问题，其余一句话带过；没有严格限制的期刊修改稿，逐条回应。

> **不同的看法：只承诺修改，还是直接写出来？**
> - Zeller：不必给出完整修改，但要具体勾勒你会怎么改，而不是只说"谢谢，我们会加上"[^zeller2012rebuttals-e4]。
> - Parikh 等人：不要只承诺，直接在回复里把要补的讨论写出来，这样别人更相信你会改[^parikh2020rebuttals-e10]。
>
> 两者的共同点是**要具体**。篇幅允许时，直接写出来更有说服力。

---

## 6. 面对拒稿：把意见变成修改清单

**被拒是常态。** 科研生涯充满拒稿，最好的科学家也一样[^bourne2005published-e3]。难过是正常的；怎样调整情绪、保持动力，见[心态与长期积累](../4_throughout/03_mindset_and_growth.md#1-把失败和被拒当作常态)。情绪平复后，按下面几步做：

1. **客观对待审稿意见**，不要当成针对你个人[^bourne2005published-e1][^huang2021rejection-e2]。
2. **判断问题有多严重。** 如果审稿人一致认为论文质量差，接受它，继续前进；要求大修（major revision，即需要较大修改后重新送审）时，就认真改，在回复信和正文中逐条回应[^bourne2005published-e2]。
3. **把审稿意见整理成待办清单**，在修改中逐一解决[^huang2021rejection-e2]。再不起眼的审稿意见里也有对你有用的东西[^zeller2012rebuttals-e7]。
4. **改好再投。** 大多数论文长远看并不重要，职业生涯由少数好论文决定[^huang2021rejection-e3]；与其仓促改投，不如借这次机会把论文改扎实 `[本项目分析]`。这次不中，总还有下一个截稿日[^zeller2012rebuttals-e9]。

---

## 本章检查清单

**投稿前**
- [ ] 校对过全文，符合页数和格式要求[^allman2001plea-e2][^allman2001plea-e4]
- [ ] 请无利害关系的同事读过[^bourne2005published-e7]
- [ ] 清楚目标期刊或会议的标准[^hicks2014reviewing-e9]

**写审稿意见时**
- [ ] 开头有中立的摘要和对贡献的概括[^roscoe2007reviews-e3][^roscoe2007reviews-e4]
- [ ] 每条批评都具体、附修改建议，并标明是否必须改[^mightreview-e5][^ralph2020empirical-e54]
- [ ] 说"不新"时给出了具体文献[^ralph2020empirical-e60]
- [ ] 文字和分数一致，有明确推荐[^hicks2014reviewing-e4][^bourne2006reviewers-e6]
- [ ] 重读一遍：如果收到这份意见的是自己，能接受吗[^mightreview-e1]

**写回复时**
- [ ] 意见逐条列表，没有遗漏主要问题[^parikh2020rebuttals-e5]
- [ ] 最重要的问题放在最前面[^hicks2014response-e5]
- [ ] 每条先引用问题、再直接回答[^parikh2020rebuttals-e8]
- [ ] 只读回复的人也能看懂[^parikh2020rebuttals-e4]

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 带着错别字和格式问题投稿 | 粗糙的论文让人觉得研究也粗糙[^allman2001plea-e1] |
| 审稿意见只有一句"不新"或"缺细节" | 不给出处和具体内容的批评不成立[^ralph2020empirical-e60][^ralph2020empirical-e61] |
| 把"简单"当成"不新" | 简单不等于平凡，事后显而易见不减损新颖性[^black2022novelty-e2][^black2022novelty-e3] |
| 打高分却通篇批评，或反过来 | 作者和其他审稿人无法据此理解你的判断[^hicks2014reviewing-e4] |
| 借审稿要求作者引用自己的论文 | 是推销自己，属于反面做法[^ralph2020empirical-e57] |
| 审稿意见里嘲讽论文、卖弄机智 | 审稿意见不是做这些的地方[^roscoe2007reviews-e11][^mightreview-e7] |
| 回复只写给审稿人看 | 做决定的人可能只读回复[^parikh2020rebuttals-e3] |
| 回复里发泄情绪、和审稿人争吵 | 可能让审稿人更坚定地反对，寻找共识更有效[^parikh2020rebuttals-e14] |
| 被拒后原样改投别处 | 浪费了审稿意见这份免费的改进清单[^huang2021rejection-e2] |

## 延伸阅读

- **当审稿人**：Roscoe 2007 讲审稿意见的结构和语气，例子生动；Bourne & Korngreen 2006 是期刊视角的十条规则；Might 的文章适合研究生第一次审稿前读。
- **判断新颖性**：Black 2022，短小，专门讲审稿人对新颖性的常见误解。
- **写回复**：Parikh、Batra & Lee 2020 最具体，有大量示例；Hicks 2014 附了一份完整的真实回复；Zeller 2012 讲会议讨论时回复如何起作用。
- **投稿与拒稿**：Bourne 2005 的十条规则；Jia-Bin Huang 关于拒稿的推文串，适合被拒那天读。

各资料的链接见[原始资料列表](../../../sources/README.md)。

[^hicks2014reviewing-e1]: Hicks 2014（审稿），开头。[证据](../../../sources/notes/hicks2014reviewing.md#e1)
[^hicks2014reviewing-e2]: Hicks 2014（审稿），Judging the work。[证据](../../../sources/notes/hicks2014reviewing.md#e2)
[^hicks2014reviewing-e3]: Hicks 2014（审稿），Start with a summary。[证据](../../../sources/notes/hicks2014reviewing.md#e3)
[^hicks2014reviewing-e4]: Hicks 2014（审稿），Scores abstract text。[证据](../../../sources/notes/hicks2014reviewing.md#e4)
[^hicks2014reviewing-e5]: Hicks 2014（审稿），Put the most important parts first。[证据](../../../sources/notes/hicks2014reviewing.md#e5)
[^hicks2014reviewing-e6]: Hicks 2014（审稿），Be respectful。[证据](../../../sources/notes/hicks2014reviewing.md#e6)
[^hicks2014reviewing-e7]: Hicks 2014（审稿），Confidentiality。[证据](../../../sources/notes/hicks2014reviewing.md#e7)
[^hicks2014reviewing-e8]: Hicks 2014（审稿），Judging the work。[证据](../../../sources/notes/hicks2014reviewing.md#e8)
[^hicks2014reviewing-e9]: Hicks 2014（审稿），Interesting or useful?。[证据](../../../sources/notes/hicks2014reviewing.md#e9)
[^hicks2014reviewing-e10]: Hicks 2014（审稿），Interesting or useful?。[证据](../../../sources/notes/hicks2014reviewing.md#e10)
[^hicks2014reviewing-e11]: Hicks 2014（审稿），Reading the paper。[证据](../../../sources/notes/hicks2014reviewing.md#e11)
[^hicks2014reviewing-e12]: Hicks 2014（审稿），Suggestions for improvement。[证据](../../../sources/notes/hicks2014reviewing.md#e12)
[^hicks2014response-e1]: Hicks 2014（作者回复），What is author response?。[证据](../../../sources/notes/hicks2014response.md#e1)
[^hicks2014response-e2]: Hicks 2014（作者回复），The goal of your response。[证据](../../../sources/notes/hicks2014response.md#e2)
[^hicks2014response-e3]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../../sources/notes/hicks2014response.md#e3)
[^hicks2014response-e4]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../../sources/notes/hicks2014response.md#e4)
[^hicks2014response-e5]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../../sources/notes/hicks2014response.md#e5)
[^hicks2014response-e6]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../../sources/notes/hicks2014response.md#e6)
[^hicks2014response-e7]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../../sources/notes/hicks2014response.md#e7)
[^hicks2014response-e8]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../../sources/notes/hicks2014response.md#e8)
[^zeller2012rebuttals-e1]: Zeller 2012，Identify the champion.。[证据](../../../sources/notes/zeller2012rebuttals.md#e1)
[^zeller2012rebuttals-e2]: Zeller 2012，Arm the champion.。[证据](../../../sources/notes/zeller2012rebuttals.md#e2)
[^zeller2012rebuttals-e3]: Zeller 2012，Write for the committee.。[证据](../../../sources/notes/zeller2012rebuttals.md#e3)
[^zeller2012rebuttals-e4]: Zeller 2012，Convince.。[证据](../../../sources/notes/zeller2012rebuttals.md#e4)
[^zeller2012rebuttals-e5]: Zeller 2012，Choose comments wisely.。[证据](../../../sources/notes/zeller2012rebuttals.md#e5)
[^zeller2012rebuttals-e6]: Zeller 2012，Write for the PC chair.。[证据](../../../sources/notes/zeller2012rebuttals.md#e6)
[^zeller2012rebuttals-e7]: Zeller 2012，Thank the reviewers.。[证据](../../../sources/notes/zeller2012rebuttals.md#e7)
[^zeller2012rebuttals-e8]: Zeller 2012，Don’t expect too much.。[证据](../../../sources/notes/zeller2012rebuttals.md#e8)
[^zeller2012rebuttals-e9]: Zeller 2012，Don’t expect too much.。[证据](../../../sources/notes/zeller2012rebuttals.md#e9)
[^zeller2012rebuttals-e10]: Zeller 2012，Organize your rebuttal.。[证据](../../../sources/notes/zeller2012rebuttals.md#e10)
[^parikh2020rebuttals-e1]: Parikh、Batra & Lee 2020，开头。[证据](../../../sources/notes/parikh2020rebuttals.md#e1)
[^parikh2020rebuttals-e2]: Parikh、Batra & Lee 2020，谁读回复。[证据](../../../sources/notes/parikh2020rebuttals.md#e2)
[^parikh2020rebuttals-e3]: Parikh、Batra & Lee 2020，谁读回复。[证据](../../../sources/notes/parikh2020rebuttals.md#e3)
[^parikh2020rebuttals-e4]: Parikh、Batra & Lee 2020，谁读回复。[证据](../../../sources/notes/parikh2020rebuttals.md#e4)
[^parikh2020rebuttals-e5]: Parikh、Batra & Lee 2020，写作流程。[证据](../../../sources/notes/parikh2020rebuttals.md#e5)
[^parikh2020rebuttals-e6]: Parikh、Batra & Lee 2020，写作流程。[证据](../../../sources/notes/parikh2020rebuttals.md#e6)
[^parikh2020rebuttals-e7]: Parikh、Batra & Lee 2020，Tip 2。[证据](../../../sources/notes/parikh2020rebuttals.md#e7)
[^parikh2020rebuttals-e8]: Parikh、Batra & Lee 2020，Tip 3。[证据](../../../sources/notes/parikh2020rebuttals.md#e8)
[^parikh2020rebuttals-e9]: Parikh、Batra & Lee 2020，Tip 12。[证据](../../../sources/notes/parikh2020rebuttals.md#e9)
[^parikh2020rebuttals-e10]: Parikh、Batra & Lee 2020，Tip 13。[证据](../../../sources/notes/parikh2020rebuttals.md#e10)
[^parikh2020rebuttals-e11]: Parikh、Batra & Lee 2020，Tip 15。[证据](../../../sources/notes/parikh2020rebuttals.md#e11)
[^parikh2020rebuttals-e12]: Parikh、Batra & Lee 2020，Tip 9。[证据](../../../sources/notes/parikh2020rebuttals.md#e12)
[^parikh2020rebuttals-e13]: Parikh、Batra & Lee 2020，Tip 1。[证据](../../../sources/notes/parikh2020rebuttals.md#e13)
[^parikh2020rebuttals-e14]: Parikh、Batra & Lee 2020，Tip 18。[证据](../../../sources/notes/parikh2020rebuttals.md#e14)
[^parikh2020rebuttals-e15]: Parikh、Batra & Lee 2020，Tip 16。[证据](../../../sources/notes/parikh2020rebuttals.md#e15)
[^parikh2020rebuttals-e16]: Parikh、Batra & Lee 2020，开头（引 Bill Freeman 的比喻）。[证据](../../../sources/notes/parikh2020rebuttals.md#e16)
[^roscoe2007reviews-e1]: Roscoe 2007，§2，第 1 页。[证据](../../../sources/notes/roscoe2007reviews.md#e1)
[^roscoe2007reviews-e2]: Roscoe 2007，§2，第 2 页。[证据](../../../sources/notes/roscoe2007reviews.md#e2)
[^roscoe2007reviews-e3]: Roscoe 2007，§4，第 3 页。[证据](../../../sources/notes/roscoe2007reviews.md#e3)
[^roscoe2007reviews-e4]: Roscoe 2007，§4，第 3 页。[证据](../../../sources/notes/roscoe2007reviews.md#e4)
[^roscoe2007reviews-e5]: Roscoe 2007，§4，第 4 页。[证据](../../../sources/notes/roscoe2007reviews.md#e5)
[^roscoe2007reviews-e6]: Roscoe 2007，§4，第 4 页。[证据](../../../sources/notes/roscoe2007reviews.md#e6)
[^roscoe2007reviews-e7]: Roscoe 2007，§4，第 4 页。[证据](../../../sources/notes/roscoe2007reviews.md#e7)
[^roscoe2007reviews-e8]: Roscoe 2007，§5，第 4 页。[证据](../../../sources/notes/roscoe2007reviews.md#e8)
[^roscoe2007reviews-e9]: Roscoe 2007，§5，第 5 页。[证据](../../../sources/notes/roscoe2007reviews.md#e9)
[^roscoe2007reviews-e10]: Roscoe 2007，§5，第 5 页。[证据](../../../sources/notes/roscoe2007reviews.md#e10)
[^roscoe2007reviews-e11]: Roscoe 2007，§5，第 5 页。[证据](../../../sources/notes/roscoe2007reviews.md#e11)
[^roscoe2007reviews-e12]: Roscoe 2007，§4，第 4 页。[证据](../../../sources/notes/roscoe2007reviews.md#e12)
[^roscoe2007reviews-e13]: Roscoe 2007，§5，第 4 页。[证据](../../../sources/notes/roscoe2007reviews.md#e13)
[^roscoe2007reviews-e14]: Roscoe 2007，§6，第 5 页。[证据](../../../sources/notes/roscoe2007reviews.md#e14)
[^roscoe2007reviews-e15]: Roscoe 2007，§5，第 5 页。[证据](../../../sources/notes/roscoe2007reviews.md#e15)
[^bourne2006reviewers-e1]: Bourne & Korngreen 2006，Rule 1。[证据](../../../sources/notes/bourne2006reviewers.md#e1)
[^bourne2006reviewers-e2]: Bourne & Korngreen 2006，Rule 2。[证据](../../../sources/notes/bourne2006reviewers.md#e2)
[^bourne2006reviewers-e3]: Bourne & Korngreen 2006，Rule 3。[证据](../../../sources/notes/bourne2006reviewers.md#e3)
[^bourne2006reviewers-e4]: Bourne & Korngreen 2006，Rule 4。[证据](../../../sources/notes/bourne2006reviewers.md#e4)
[^bourne2006reviewers-e5]: Bourne & Korngreen 2006，Rule 9。[证据](../../../sources/notes/bourne2006reviewers.md#e5)
[^bourne2006reviewers-e6]: Bourne & Korngreen 2006，Rule 9。[证据](../../../sources/notes/bourne2006reviewers.md#e6)
[^bourne2006reviewers-e7]: Bourne & Korngreen 2006，Rule 9。[证据](../../../sources/notes/bourne2006reviewers.md#e7)
[^bourne2006reviewers-e8]: Bourne & Korngreen 2006，引言。[证据](../../../sources/notes/bourne2006reviewers.md#e8)
[^bourne2006reviewers-e9]: Bourne & Korngreen 2006，Rule 10。[证据](../../../sources/notes/bourne2006reviewers.md#e9)
[^bourne2006reviewers-e10]: Bourne & Korngreen 2006，Rule 6。[证据](../../../sources/notes/bourne2006reviewers.md#e10)
[^bourne2006reviewers-e11]: Bourne & Korngreen 2006，Rule 8。[证据](../../../sources/notes/bourne2006reviewers.md#e11)
[^bourne2006reviewers-e12]: Bourne & Korngreen 2006，Rule 10。[证据](../../../sources/notes/bourne2006reviewers.md#e12)
[^bourne2005published-e1]: Bourne 2005，Rule 5。[证据](../../../sources/notes/bourne2005published.md#e1)
[^bourne2005published-e2]: Bourne 2005，Rule 5。[证据](../../../sources/notes/bourne2005published.md#e2)
[^bourne2005published-e3]: Bourne 2005，Rule 5。[证据](../../../sources/notes/bourne2005published.md#e3)
[^bourne2005published-e4]: Bourne 2005，Rule 8。[证据](../../../sources/notes/bourne2005published.md#e4)
[^bourne2005published-e5]: Bourne 2005，Rule 9。[证据](../../../sources/notes/bourne2005published.md#e5)
[^bourne2005published-e6]: Bourne 2005，Rule 3。[证据](../../../sources/notes/bourne2005published.md#e6)
[^bourne2005published-e7]: Bourne 2005，Rule 6。[证据](../../../sources/notes/bourne2005published.md#e7)
[^bourne2005published-e8]: Bourne 2005，Rule 7。[证据](../../../sources/notes/bourne2005published.md#e8)
[^bourne2005published-e9]: Bourne 2005，Rule 10。[证据](../../../sources/notes/bourne2005published.md#e9)
[^bourne2005published-e10]: Bourne 2005，Rule 9。[证据](../../../sources/notes/bourne2005published.md#e10)
[^black2022novelty-e1]: Black 2022，开头。[证据](../../../sources/notes/black2022novelty.md#e1)
[^black2022novelty-e2]: Black 2022，Novelty as complexity。[证据](../../../sources/notes/black2022novelty.md#e2)
[^black2022novelty-e3]: Black 2022，Novelty as surprise。[证据](../../../sources/notes/black2022novelty.md#e3)
[^black2022novelty-e4]: Black 2022，Novelty as technical novelty。[证据](../../../sources/notes/black2022novelty.md#e4)
[^black2022novelty-e5]: Black 2022，Novelty as usefulness or value。[证据](../../../sources/notes/black2022novelty.md#e5)
[^black2022novelty-e6]: Black 2022，Novelty as difficulty。[证据](../../../sources/notes/black2022novelty.md#e6)
[^mightreview-e1]: Might，开头。[证据](../../../sources/notes/mightreview.md#e1)
[^mightreview-e2]: Might，Recognize conflicts。[证据](../../../sources/notes/mightreview.md#e2)
[^mightreview-e3]: Might，Don't review like a grad student。[证据](../../../sources/notes/mightreview.md#e3)
[^mightreview-e4]: Might，Acknowledge visceral reactions。[证据](../../../sources/notes/mightreview.md#e4)
[^mightreview-e5]: Might，Offer constructive criticism。[证据](../../../sources/notes/mightreview.md#e5)
[^mightreview-e6]: Might，Offer constructive criticism。[证据](../../../sources/notes/mightreview.md#e6)
[^mightreview-e7]: Might，Hold the snark。[证据](../../../sources/notes/mightreview.md#e7)
[^mightreview-e8]: Might，Keep it impersonal。[证据](../../../sources/notes/mightreview.md#e8)
[^mightreview-e9]: Might，Anonymize but don't hide。[证据](../../../sources/notes/mightreview.md#e9)
[^mightreview-e10]: Might，Scholarly conflict。[证据](../../../sources/notes/mightreview.md#e10)
[^allman2001plea-e1]: Allman 2001，2. Sloppy Papers Are Long Shots.。[证据](../../../sources/notes/allman2001plea.md#e1)
[^allman2001plea-e2]: Allman 2001，2. Sloppy Papers Are Long Shots.。[证据](../../../sources/notes/allman2001plea.md#e2)
[^allman2001plea-e3]: Allman 2001，7. Answer All The Easy Questions.。[证据](../../../sources/notes/allman2001plea.md#e3)
[^allman2001plea-e4]: Allman 2001，6. Don't Waste My Time III.。[证据](../../../sources/notes/allman2001plea.md#e4)
[^ralph2020empirical-e53]: SIGSOFT General Standard，Good Review Practices。[证据](../../../sources/notes/ralph2020empirical.md#e53)
[^ralph2020empirical-e54]: SIGSOFT General Standard，Good Review Practices。[证据](../../../sources/notes/ralph2020empirical.md#e54)
[^ralph2020empirical-e55]: SIGSOFT General Standard，Good Review Practices。[证据](../../../sources/notes/ralph2020empirical.md#e55)
[^ralph2020empirical-e56]: SIGSOFT General Standard，Reviewing Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e56)
[^ralph2020empirical-e57]: SIGSOFT General Standard，Reviewing Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e57)
[^ralph2020empirical-e58]: SIGSOFT General Standard，Reviewing Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e58)
[^ralph2020empirical-e59]: SIGSOFT General Standard，Reviewing Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e59)
[^ralph2020empirical-e60]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e60)
[^ralph2020empirical-e61]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e61)
[^ralph2020empirical-e62]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e62)
[^ralph2020empirical-e25]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e41]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e64]: SIGSOFT General Standard，Reviewing Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e64)
[^huang2021rejection-e2]: Jia-Bin Huang 2021，第 4 条（It’s not personal），[原推文](https://twitter.com/jbhuang0604/status/1443248831102136333)。[证据](../../../sources/notes/huang2021rejection.md#e2)
[^huang2021rejection-e3]: Jia-Bin Huang 2021，第 5 条（It doesn't matter much），[原推文](https://twitter.com/jbhuang0604/status/1443248831102136333)。[证据](../../../sources/notes/huang2021rejection.md#e3)
