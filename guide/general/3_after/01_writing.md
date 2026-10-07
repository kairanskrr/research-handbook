# 写作

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲怎么把研究写成一篇别人读得懂、信得过、记得住的论文：先想清楚要说什么，再搭结构、写引言、摆证据，最后反复修改。

本章不讲语法、用词等句子层面的细节，也不讲各学科特有的论文格式。投稿之后怎么面对审稿意见、怎么改稿重投，见[审稿、回复审稿意见与发表](02_reviewing_and_publishing.md)。

**读完本章，你应该能：**

- 用一两句话说出自己论文的核心信息，并据此决定写什么、删什么；
- 把贡献写成具体、可检验的成果，而不是工作量；
- 按"背景—内容—结论"组织全文和每个段落，写出一个回答清楚五个问题的引言；
- 检查每条主张有没有与之相称的证据；
- 从研究一开始就动笔，并通过多轮修改和他人反馈把初稿改好。

---

## 1. 先想清楚一个核心信息

**怎么做：**

- 尽早用一两句话写下这篇论文最想让读者记住的东西。Peyton Jones 把它叫作论文的 "ping"：一个清楚、鲜明的想法[^peytonjones2013write-e2]。动笔时说不准没关系，写完时必须说得出来[^peytonjones2013write-e3]。
- 说清背后的关键洞见。Black 强调，要讲的不只是技术贡献本身，还有让问题变得可解、从而带来贡献的那个新看法[^black2024writing-e2]。
- 一篇论文只讲一个故事。手里有两个大想法，就考虑写成两篇[^peytonjones2013write-e2][^black2024writing-e3]。
- 用这个核心信息当筛子：任何不支持它的部分，不管多正确、花了你多少力气，都删掉或改写[^ernstwrite-e9]。
- 检验办法：读者读完一年后，还能向同事说出你的主要贡献吗[^mensh2017ten-e2]？你自己能在几分钟内向同事讲完整篇论文的提纲吗？讲不出，说明故事还要再提炼[^mensh2017ten-e11]。

**为什么：**

- 读者能带走的内容很少，往往只有几句话，所以要主动挑出最重要的那几句[^nanda2025writing-e2]。
- 同时主打多个贡献的论文，每个贡献都不够有说服力，也更难被记住[^mensh2017ten-e1]。Zhang 的说法是"少即是多"：以对领域的影响来衡量，少而重要的论文胜过多而零碎的论文[^zhang2014ten-e3]。
- 动笔前先想清楚读者是谁。读者不同，论文的组织方式和需要交代的背景深度都不同[^zhang2014ten-e7]。

**容易错在哪：** 想把做过的所有事都塞进一篇论文。Nanda 建议把研究压缩成一到三个围绕同一主题的主张[^nanda2025writing-e1]，其余的细节要么舍弃，要么放进附录[^nanda2025writing-e2]。

## 2. 把贡献写成成果，而且要可检验

**怎么做：**

- 先写贡献清单。整篇论文都围绕证实这份清单来写[^peytonjones2013write-e4]。
- 每条贡献写成一个**成果**，而不是一段**过程**。van Deursen 的定义是：贡献是"在这篇论文之前世界不知道、因为这篇论文现在知道了"的东西[^vandeursen2013writing-e1]。贡献是结果，不是付出的努力[^vandeursen2013writing-e2]。
- 每条贡献要**具体、可检验**，最好注明在第几节给出证据[^peytonjones2013write-e5][^widomtips-e3]。
- 把背景材料和自己的贡献明确分开，让读者一眼看出哪些是新的[^vandeursen2013writing-e3][^huang2023introduction-e4]。

| 不好的写法 | 好的写法 |
|---|---|
| "我们花了六个月人工分析了 50 万条记录" | "我们发现，在 X 条件下，A 现象的出现比例约为 B（第 4 节）" |
| "我们访谈了 30 位教师，研究了他们的看法" | "我们发现，教师应对 X 的做法可以归为三类，其中一类此前未被描述（第 3 节）" |

`[本项目分析]` 表中例子是示意。依据是：贡献是成果，不是付出的努力[^vandeursen2013writing-e2]；Peyton Jones 举的例子来自编程语言研究，把"研究了某系统的性质"写成"我们证明该类型系统是可靠的（第 4 节）"[^peytonjones2013write-e5]。

**为什么：** van Deursen 指出，贡献不仅要强，还要讲得清楚[^vandeursen2013writing-e4]。他的理由是审稿讨论常以贡献为单位进行（在计算机等以会议为主的领域尤其如此），所以要让不是本方向专家的人也能看懂。

**容易错在哪：** 按花费的时间分配篇幅。你花了最多时间的部分，不一定是读者最需要的部分[^ernstwrite-e3]。

## 3. 按"背景—内容—结论"组织，先亮出结论

**怎么做：**

- 全文按"背景（context）—内容（content）—结论（conclusion）"组织：引言给背景，结果部分给内容，讨论部分给结论[^mensh2017ten-e4]。
- 每个段落也一样：第一句点出话题，中间给内容，最后一句给出要读者记住的结论[^mensh2017ten-e4]。每段只讲一个主要意思[^raibert1985good-e7]。
- **先说结论，再给支撑。** 论文不是推理小说，一开始就把故事和发现讲出来[^raibert1985good-e3][^ernstwrite-e4]；章节和段落也是先说观点，再给证据[^ernstwrite-e5]。
- **按逻辑写，不按时间写。** 读者不关心你是按什么顺序得到结果的，只关心最终的主张和支撑它的逻辑[^mensh2017ten-e5][^widomtips-e5]。走过的弯路"也许浸透了你的心血"，但读者不感兴趣[^peytonjones2013write-e7]。
- 结果部分：把"结果如何一步步支撑主张"写成一串陈述句，直接用作小节标题[^mensh2017ten-e7]。
- 讨论部分：说明缺口如何被填补、解释有哪些局限、对领域有什么推进[^mensh2017ten-e8]。
- 先给直觉，再给细节；可以用一个具体例子引出问题和想法[^peytonjones2013write-e9][^peytonjones2013write-e13]。
- 讲故事可以用"目标—障碍—解决"的节奏：先让读者想要这个目标，再说明是什么挡住了它，最后给出你的办法[^black2024writing-e7]。
- 为不了解你工作的读者写：术语要清楚定义，少用缩写[^mensh2017ten-e13]。

**为什么：** 缺了背景，读者会问"为什么要告诉我这个"；缺了结论，读者会问"所以呢"[^mensh2017ten-e3]。

**摘要和标题要格外用心。** 对大多数读者来说，摘要是唯一会读的部分[^mensh2017ten-e12]，人们靠摘要决定要不要读全文[^shaw2003writing-e23]。摘要写清问题、方法和主要贡献[^widomtips-e7]；标题、摘要和图被看得最多，花时间时要向它们倾斜[^mensh2017ten-e9]。

## 4. 把引言写好：回答五个问题

对新手来说，引言往往是最难写的部分[^huang2023introduction-e1]。

**怎么做：** 引言按顺序回答下面五个问题，大致每个问题一段。这五个问题综合了 Widom 和 Huang 的写法[^widomtips-e2][^huang2023introduction-e2]：

1. **问题是什么？** 最好用一个具体例子引出，而不是空喊"这个问题很重要"[^peytonjones2013write-e13]。
2. **为什么重要？** 说明读者为什么该关心。
3. **别人做了什么，为什么还不够？** 指出已有方法的缺口，以及为什么这个问题难[^widomtips-e2][^ernstwrite-e2]。能用一个具体例子展示已有方法的问题最好[^huang2023introduction-e5]。
4. **你做了什么？** 用"本文……"开头，和已有工作清楚分开，讲清任务、核心思路、怎么评估[^huang2023introduction-e3]，以及主要结果和局限[^widomtips-e2]。
5. **你的贡献是什么？** 用列表写出，注明各在哪一节[^widomtips-e3][^huang2023introduction-e4]。

Widom 原本的五个问题是：问题是什么；为什么有趣、重要；为什么难；为什么以前没解决（已有方法哪里不行）；你的方法和结果的关键部分是什么（包括局限）。他另外建议引言最后用列表写出贡献[^widomtips-e2][^widomtips-e3]。Mensh & Kording 也强调，引言围绕论文的动机展开，不在此之外写泛泛的文献综述[^mensh2017ten-e6]。

> `[本项目分析]` **学科差异**：逐条列贡献并注明节号、"读到第 3 页就要看到贡献"、相关工作放前还是放后，主要是计算机和工程类会议论文的惯例。很多期刊和学科有自己的固定结构（例如医学、心理学常用"引言—方法—结果—讨论"，人文学科多是论证式写法），不一定逐条列贡献。但"读者很快能看出你新在哪里"这一点各学科通用。动笔前先看目标期刊或会议近期论文的写法。

**为什么：** 审稿人读完引言时，多半已经对论文有了初步判断，后面是在找证据支持这个判断[^widomtips-e1][^black2024writing-e1]。Widom 的标准是（以计算机会议论文的篇幅为准）：读者读到第 3 页时，就应该已经清楚看到你的贡献[^widomtips-e6]。

**容易错在哪：**

- 在引言里写一大段泛泛的文献综述[^mensh2017ten-e6]。
- 只说"我们研究了 X 和 Y 的关系"，不说发现了什么[^raibert1985good-e3][^ernstwrite-e4]。
- 不说清哪些是新的、哪些建立在已有工作上[^nanda2025writing-e7]。

> **不同的看法：相关工作放在前面还是后面？**
> - Peyton Jones 主张放在后面：读者还不了解问题时看不懂那些比较，而且讲别人的方法会挡在读者和你的想法之间[^peytonjones2013write-e8]。
> - Widom 认为两种都可以：能写得短而具体、或者必须一开始就和已有工作划清界限时，放在前面；需要先讲完技术内容才能比较时，放在后面[^widomtips-e4]。
>
> 两种做法都要求在引言里说清本文和最相关工作的区别[^nanda2025writing-e7]。`[本项目分析]` 实际操作时先看所投期刊或会议的惯例，再按上面的标准判断：读者需不需要先理解你的方法，才能看懂比较。

## 5. 每个主张都要有相称的证据

**怎么做：**

- 列出引言里的每条主张，在正文中找到支撑它的证据，并从主张处注明证据在哪一节。证据可以是分析比较、定理、测量、案例研究等[^peytonjones2013write-e6]。
- **证据要对得上主张。** 主张"更快"，就要测速度，而不是去论证"更易用"[^shaw2003writing-e12]。
- **主张的强度要和证据相称。** 把核心主张拆成几个分句，看每个分句说的是"总是成立"、"在某条件下提升多少"，还是"至少存在一个例子"。说法越强，需要的证据越强[^shaw2003writing-e16][^nanda2025writing-e3]。检查之后常常需要把主张改得更准确，让它只说你真正做到的[^shaw2003writing-e17]。
- 证据要说明成果对别人也有用，而不只是"在我这里管用"[^shaw2003writing-e11]。
- 主动找自己的漏洞：假设自己错了，错在哪[^nanda2025writing-e4]？承认方法的弱点，给别人应得的功劳。这些都不会减少你的功劳[^peytonjones2013write-e11]。
- 少用"新颖""显著""最好"之类的自我评价，给出事实，让读者自己判断[^ernstwrite-e7]。

**为什么：** 论文要讲清你做成了什么、怎么做到的，以及读者为什么该关心[^shaw2003writing-e19]；而要让读者相信，就要靠证据。摘要和引言里的承诺，正文必须兑现[^shaw2003writing-e23]。

**容易错在哪：** 夸大或贬低自己的结果[^zhang2014ten-e4]。

## 6. 尽早动笔，把写作当作研究的一部分

**怎么做：**

- 不要等有了"了不起的想法"或研究做完再写。写论文本身就是发展想法的过程[^peytonjones2013write-e12]，是做研究的主要手段，而不只是汇报[^peytonjones2013write-e1]；写作和研究不能分开[^zhang2014ten-e8]。
- 在做实验之前，就可以写出动机、问题、方法和实验设计[^eisnerfirst-e10]。怎样从项目开始就用论文提纲安排研究、把计划中的图表当作待办清单，见[做计划：从终点倒推](../1_before/05_planning.md#1-从终点倒推先想清楚最后要说什么)和[把论文提纲当作项目看板](../1_before/05_planning.md#5-把论文提纲当作项目看板)。
- 把前两三页给别人看。如果基本想法会让人怀疑或觉得无聊，越早知道越好[^eisnerfirst-e3]。
- 先写自己的想法，再拿去和文献比较，这样更容易找到新角度[^eisnerfirst-e2]。
- 写不出来时，先写点东西，以后再改：可以先讲给别人听再记下来，可以先写提纲，也可以先写零散的笔记[^ernstwrite-e8]。也可以先准备一个报告，用讲解的顺序来组织论文[^black2024writing-e6]。

**为什么：**

- 写作迫使你理清思路，常会暴露漏洞或带来新想法[^nanda2025writing-e8][^ernstwrite-e1]；诚实地写下来，还常会发现要证明你的观点需要比预想更多的工作，所以越早写越好[^eisnerfirst-e6]。
- 讲不清一个想法，往往说明你还没真正理解它[^olah2017debt-e2]。写不下去时，多半是还没想清楚要说什么[^raibert1985good-e5]。

> **不同的看法：摘要和引言先写还是最后写？**
> - 有人习惯最后写，因为那时正文已经完成，照着概括就行[^ernstwrite-e6]。
> - Ernst、Nanda、Black 都主张早写：摘要和引言框定了整篇论文，早写再按需修改[^ernstwrite-e6]；Nanda 的顺序是摘要 → 要点提纲 → 引言 → 完整初稿，然后反复迭代[^nanda2025writing-e6]；Black 认为甚至可以在有结果之前写引言[^black2024writing-e4]。
>
> `[本项目分析]` 对新手，建议早写一个粗糙版本，用来检验思路、和导师讨论；正文完成后，再按实际结果重写一遍。这样两边的好处都能得到。

## 7. 反复修改，并善用读者

**怎么做：**

- **接受初稿是坏的。** 好文字的公式就是先写出坏东西，再把它改好[^raibert1985good-e1]，通常要改十几遍[^raibert1985good-e2][^black2024writing-e5]。
- **敢删。** 整段删掉重写，常常比一点点改更快[^mensh2017ten-e10]。逐节、逐段、逐句检查，凡是不服务于主线的都删掉[^ernstwrite-e10][^nanda2025writing-e9]。
- **当自己的审稿人。** 把稿子放一两天，再当作别人写的东西来读，站在审稿人的角度检查意义、逻辑、结论和呈现[^zhang2014ten-e5]。
- **珍惜读者。** 每个读者只能"第一次读"一次[^peytonjones2013write-e10][^raibert1985good-e6]。请他们告诉你"读到哪里看不懂了"，这比挑拼写错误重要得多[^peytonjones2013write-e10]。
- **相信读者的困惑。** 读者说看不懂，不要争辩你写得很清楚，去改那一部分[^raibert1985good-e4]。读者给的反馈很笼统，往往说明他们没抓住主线；反馈很具体，通常是某一段的逻辑不够[^mensh2017ten-e14]。
- **投稿前先在身边试水。** 在组会或报告中讲，请同事和合作者挑毛病，提前解决审稿人可能提的问题[^zhang2014ten-e6]。
- **互相帮忙。** 主动帮别人读初稿，别人也会帮你读[^vandeursen2013writing-e5]。

**为什么：**

- 你对自己的项目太熟悉，容易以为读者也懂，这叫"透明错觉"，只有别人的反馈能帮你发现[^nanda2025writing-e5]。
- 论文是一对多的：你多花力气把它讲清楚，每个读者都能少花力气去理解[^olah2017debt-e1]。好的解释也不只是表面润色，往往需要重新组织想法本身[^olah2017debt-e3]。
- 写作不清楚的代价很高。Eisner 认为，对能否被接收来说，清楚的动机和表述比结果更重要[^eisnerfirst-e9]；他还提到，有资深学者审稿时读到看不懂为止，按读到多远打分[^eisnerfirst-e14]。Eisner 并不赞成这种审稿方式，但它说明了写不清楚的代价。

## 本章检查清单

- [ ] 能用一两句话说出论文的核心信息[^peytonjones2013write-e3][^mensh2017ten-e11]
- [ ] 不支持核心信息的内容已经删掉或移到附录[^ernstwrite-e9][^nanda2025writing-e2]
- [ ] 贡献以列表形式写出，每条都是具体、可检验的成果，并注明在哪一节[^peytonjones2013write-e5][^vandeursen2013writing-e2][^widomtips-e3]
- [ ] 背景材料和自己的贡献清楚分开[^vandeursen2013writing-e3]
- [ ] 引言回答了五个问题（综合 Widom 和 Huang）：问题、为什么重要、已有工作的缺口和难点、本文做了什么（含结果和局限）、贡献[^widomtips-e2][^huang2023introduction-e2]
- [ ] 摘要讲完了整个故事，包括发现了什么[^mensh2017ten-e12][^raibert1985good-e3]
- [ ] 全文和每段都是先给背景和观点，再给内容，最后给结论[^mensh2017ten-e4][^ernstwrite-e5]
- [ ] 没有按时间顺序讲自己的探索过程[^mensh2017ten-e5][^peytonjones2013write-e7]
- [ ] 每条主张都能在正文中找到对应的证据，证据类型对得上主张，强度配得上说法[^peytonjones2013write-e6][^shaw2003writing-e12][^shaw2003writing-e16]
- [ ] 讨论部分写了局限[^mensh2017ten-e8]
- [ ] 至少请一位没读过这篇稿子的人读过，并按他们的困惑改过[^peytonjones2013write-e10][^raibert1985good-e4]

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 一篇论文塞进好几个大想法 | 每个都不够有说服力，读者只会记住一个[^mensh2017ten-e1][^black2024writing-e3] |
| 把工作量当贡献（"我们花了六个月……"） | 贡献是成果，不是付出的努力[^vandeursen2013writing-e2] |
| 按时间顺序讲自己的探索过程 | 读者只关心最终主张和支撑它的逻辑[^mensh2017ten-e5][^peytonjones2013write-e7] |
| 按花费的时间分配篇幅 | 花时间最多的部分，不一定是读者最需要的[^ernstwrite-e3] |
| 把结论藏到最后 | 读者和审稿人在引言阶段就形成了判断[^widomtips-e1][^ernstwrite-e4] |
| 在引言里写泛泛的文献综述 | 引言应聚焦于缺口和本文的贡献[^mensh2017ten-e6] |
| 主张比证据强 | 全称的说法需要比"存在一个例子"强得多的证据[^shaw2003writing-e16][^nanda2025writing-e3] |
| 证据和主张对不上 | 主张性能提升却去论证易用性，说服不了读者[^shaw2003writing-e12] |
| 满篇"新颖""显著""最好" | 自我评价代替不了事实，应给出事实让读者判断[^ernstwrite-e7] |
| 等研究全部做完、临近截止才动笔 | 来不及发现漏洞、补实验、找人反馈[^eisnerfirst-e6][^eisnerfirst-e3] |
| 舍不得删、只做小修小补 | 整段重写往往更快更好[^mensh2017ten-e10] |
| 读者说看不懂时和他争辩 | 应当相信读者的反馈，去改写那一部分[^raibert1985good-e4] |

## 延伸阅读

- **Mensh & Kording 2017**，Ten simple rules for structuring papers：讲论文结构最系统的一篇，从全文到段落都有，适合在搭提纲时对照。开放获取，篇幅短。
- **Peyton Jones**，How to write a great research paper（幻灯片和讲座视频）：七条建议，讲"一个核心想法""可检验的贡献""主张要有证据"，适合动笔前看一遍。
- **Widom**，Tips for Writing Technical Papers：本章引言"五个问题"的主要来源之一（本章综合了 Widom 和 Huang），也讲了各部分怎么写，适合写引言时对照。例子偏计算机会议论文。
- **Eisner**，Write the Paper First：说明为什么要在做实验之前写论文，适合总想"做完再写"的人。
- **Ernst**，How to write a technical paper：内容全面，从组织结构到克服拖延都有，适合修改阶段逐条检查。
- **Shaw 2003**：例子来自软件工程，但"主张—证据"的对应关系和摘要结构的分析适用于各学科，适合检查证据够不够。
- **Raibert 1985**，Good Writing：很短，讲"好文字都是改出来的"，适合写不下去的时候读。
- **Olah & Carter 2017**，Research Debt：从整个学术共同体的角度说明，为什么把想法解释清楚本身就是有价值的工作。

[^peytonjones2013write-e1]: Peyton Jones 2013，幻灯片 "Writing papers: model 2"。[证据](../../../sources/notes/peytonjones2013write.md#e1)
[^peytonjones2013write-e2]: Peyton Jones 2013，幻灯片 "The idea"。[证据](../../../sources/notes/peytonjones2013write.md#e2)
[^peytonjones2013write-e3]: Peyton Jones 2013，幻灯片 "The idea"。[证据](../../../sources/notes/peytonjones2013write.md#e3)
[^peytonjones2013write-e4]: Peyton Jones 2013，幻灯片 "State your contributions"。[证据](../../../sources/notes/peytonjones2013write.md#e4)
[^peytonjones2013write-e5]: Peyton Jones 2013，幻灯片 "Contributions should be refutable"。[证据](../../../sources/notes/peytonjones2013write.md#e5)
[^peytonjones2013write-e6]: Peyton Jones 2013，幻灯片 "Evidence"。[证据](../../../sources/notes/peytonjones2013write.md#e6)
[^peytonjones2013write-e7]: Peyton Jones 2013，幻灯片 "Putting the reader first"。[证据](../../../sources/notes/peytonjones2013write.md#e7)
[^peytonjones2013write-e8]: Peyton Jones 2013，幻灯片 "Related work"。[证据](../../../sources/notes/peytonjones2013write.md#e8)
[^peytonjones2013write-e9]: Peyton Jones 2013，幻灯片 "Presenting the idea"。[证据](../../../sources/notes/peytonjones2013write.md#e9)
[^peytonjones2013write-e10]: Peyton Jones 2013，幻灯片 "Getting help"。[证据](../../../sources/notes/peytonjones2013write.md#e10)
[^peytonjones2013write-e11]: Peyton Jones 2013，幻灯片 "Credit"。[证据](../../../sources/notes/peytonjones2013write.md#e11)
[^peytonjones2013write-e12]: Peyton Jones 2013，幻灯片 "Do not be intimidated"。[证据](../../../sources/notes/peytonjones2013write.md#e12)
[^peytonjones2013write-e13]: Peyton Jones 2013，幻灯片 "Describe the problem"。[证据](../../../sources/notes/peytonjones2013write.md#e13)
[^mensh2017ten-e1]: Mensh & Kording 2017，Rule 1。[证据](../../../sources/notes/mensh2017ten.md#e1)
[^mensh2017ten-e2]: Mensh & Kording 2017，Rule 1。[证据](../../../sources/notes/mensh2017ten.md#e2)
[^mensh2017ten-e3]: Mensh & Kording 2017，Rule 3。[证据](../../../sources/notes/mensh2017ten.md#e3)
[^mensh2017ten-e4]: Mensh & Kording 2017，Rule 3。[证据](../../../sources/notes/mensh2017ten.md#e4)
[^mensh2017ten-e5]: Mensh & Kording 2017，Rule 3。[证据](../../../sources/notes/mensh2017ten.md#e5)
[^mensh2017ten-e6]: Mensh & Kording 2017，Rule 6。[证据](../../../sources/notes/mensh2017ten.md#e6)
[^mensh2017ten-e7]: Mensh & Kording 2017，Rule 7。[证据](../../../sources/notes/mensh2017ten.md#e7)
[^mensh2017ten-e8]: Mensh & Kording 2017，Rule 8。[证据](../../../sources/notes/mensh2017ten.md#e8)
[^mensh2017ten-e9]: Mensh & Kording 2017，Rule 9。[证据](../../../sources/notes/mensh2017ten.md#e9)
[^mensh2017ten-e10]: Mensh & Kording 2017，Rule 10。[证据](../../../sources/notes/mensh2017ten.md#e10)
[^mensh2017ten-e11]: Mensh & Kording 2017，Rule 10。[证据](../../../sources/notes/mensh2017ten.md#e11)
[^mensh2017ten-e12]: Mensh & Kording 2017，Rule 5。[证据](../../../sources/notes/mensh2017ten.md#e12)
[^mensh2017ten-e13]: Mensh & Kording 2017，Rule 2。[证据](../../../sources/notes/mensh2017ten.md#e13)
[^mensh2017ten-e14]: Mensh & Kording 2017，Rule 10。[证据](../../../sources/notes/mensh2017ten.md#e14)
[^zhang2014ten-e8]: Zhang 2014，Rule 1。[证据](../../../sources/notes/zhang2014ten.md#e8)
[^zhang2014ten-e3]: Zhang 2014，Rule 2。[证据](../../../sources/notes/zhang2014ten.md#e3)
[^zhang2014ten-e4]: Zhang 2014，Rule 8。[证据](../../../sources/notes/zhang2014ten.md#e4)
[^zhang2014ten-e5]: Zhang 2014，Rule 8。[证据](../../../sources/notes/zhang2014ten.md#e5)
[^zhang2014ten-e6]: Zhang 2014，Rule 9。[证据](../../../sources/notes/zhang2014ten.md#e6)
[^zhang2014ten-e7]: Zhang 2014，Rule 3。[证据](../../../sources/notes/zhang2014ten.md#e7)
[^shaw2003writing-e19]: Shaw 2003，§1。[证据](../../../sources/notes/shaw2003writing.md#e19)
[^shaw2003writing-e12]: Shaw 2003，§4。[证据](../../../sources/notes/shaw2003writing.md#e12)
[^shaw2003writing-e16]: Shaw 2003，§5。[证据](../../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e17]: Shaw 2003，§5。[证据](../../../sources/notes/shaw2003writing.md#e17)
[^shaw2003writing-e23]: Shaw 2003，§6。[证据](../../../sources/notes/shaw2003writing.md#e23)
[^shaw2003writing-e11]: Shaw 2003，§4。[证据](../../../sources/notes/shaw2003writing.md#e11)
[^widomtips-e1]: Widom 2006，The Introduction。[证据](../../../sources/notes/widomtips.md#e1)
[^widomtips-e2]: Widom 2006，The Introduction。[证据](../../../sources/notes/widomtips.md#e2)
[^widomtips-e3]: Widom 2006，The Introduction。[证据](../../../sources/notes/widomtips.md#e3)
[^widomtips-e4]: Widom 2006，Related Work。[证据](../../../sources/notes/widomtips.md#e4)
[^widomtips-e5]: Widom 2006，The Body。[证据](../../../sources/notes/widomtips.md#e5)
[^widomtips-e6]: Widom 2006，The Body。[证据](../../../sources/notes/widomtips.md#e6)
[^widomtips-e7]: Widom 2006，The Abstract。[证据](../../../sources/notes/widomtips.md#e7)
[^eisnerfirst-e9]: Eisner 2010，Clear writing increases your odds of acceptance。[证据](../../../sources/notes/eisnerfirst.md#e9)
[^eisnerfirst-e10]: Eisner 2010，The document is a focus for discussion with others。[证据](../../../sources/notes/eisnerfirst.md#e10)
[^eisnerfirst-e3]: Eisner 2010，Is it a good topic?。[证据](../../../sources/notes/eisnerfirst.md#e3)
[^eisnerfirst-e6]: Eisner 2010，What needs to be done?。[证据](../../../sources/notes/eisnerfirst.md#e6)
[^eisnerfirst-e2]: Eisner 2010，What needs to be done?。[证据](../../../sources/notes/eisnerfirst.md#e2)
[^eisnerfirst-e14]: Eisner 2010，Clear writing increases your odds of acceptance。[证据](../../../sources/notes/eisnerfirst.md#e14)
[^nanda2025writing-e1]: Nanda 2025，TL;DR。[证据](../../../sources/notes/nanda2025writing.md#e1)
[^nanda2025writing-e2]: Nanda 2025，Crafting a Narrative。[证据](../../../sources/notes/nanda2025writing.md#e2)
[^nanda2025writing-e3]: Nanda 2025，Crafting a Narrative。[证据](../../../sources/notes/nanda2025writing.md#e3)
[^nanda2025writing-e4]: Nanda 2025，Rigorous Supporting Evidence。[证据](../../../sources/notes/nanda2025writing.md#e4)
[^nanda2025writing-e5]: Nanda 2025，The Writing Process。[证据](../../../sources/notes/nanda2025writing.md#e5)
[^nanda2025writing-e6]: Nanda 2025，TL;DR。[证据](../../../sources/notes/nanda2025writing.md#e6)
[^nanda2025writing-e7]: Nanda 2025，Novelty。[证据](../../../sources/notes/nanda2025writing.md#e7)
[^nanda2025writing-e8]: Nanda 2025，Introduction。[证据](../../../sources/notes/nanda2025writing.md#e8)
[^nanda2025writing-e9]: Nanda 2025，Iteratively Expand。[证据](../../../sources/notes/nanda2025writing.md#e9)
[^black2024writing-e1]: Black 2024，Introduction。[证据](../../../sources/notes/black2024writing.md#e1)
[^black2024writing-e2]: Black 2024，The Nugget。[证据](../../../sources/notes/black2024writing.md#e2)
[^black2024writing-e3]: Black 2024，How to tell a story: Goal, Problem, Solution。[证据](../../../sources/notes/black2024writing.md#e3)
[^black2024writing-e4]: Black 2024，Number one writing tip。[证据](../../../sources/notes/black2024writing.md#e4)
[^black2024writing-e5]: Black 2024，Number one writing tip。[证据](../../../sources/notes/black2024writing.md#e5)
[^black2024writing-e6]: Black 2024，Introduction。[证据](../../../sources/notes/black2024writing.md#e6)
[^black2024writing-e7]: Black 2024，How to tell a story: Goal, Problem, Solution。[证据](../../../sources/notes/black2024writing.md#e7)
[^ernstwrite-e1]: Ernst，开头。[证据](../../../sources/notes/ernstwrite.md#e1)
[^ernstwrite-e2]: Ernst，Know your message, and stay on message。[证据](../../../sources/notes/ernstwrite.md#e2)
[^ernstwrite-e3]: Ernst，Which details to include。[证据](../../../sources/notes/ernstwrite.md#e3)
[^ernstwrite-e4]: Ernst，Make the organization and results clear。[证据](../../../sources/notes/ernstwrite.md#e4)
[^ernstwrite-e5]: Ernst，Make the organization and results clear。[证据](../../../sources/notes/ernstwrite.md#e5)
[^ernstwrite-e6]: Ernst，Make the organization and results clear。[证据](../../../sources/notes/ernstwrite.md#e6)
[^ernstwrite-e7]: Ernst，Writing style。[证据](../../../sources/notes/ernstwrite.md#e7)
[^ernstwrite-e8]: Ernst，Getting started。[证据](../../../sources/notes/ernstwrite.md#e8)
[^ernstwrite-e9]: Ernst，Which details to include。[证据](../../../sources/notes/ernstwrite.md#e9)
[^ernstwrite-e10]: Ernst，Brevity。[证据](../../../sources/notes/ernstwrite.md#e10)
[^raibert1985good-e1]: Raibert 1985，开头。[证据](../../../sources/notes/raibert1985good.md#e1)
[^raibert1985good-e2]: Raibert 1985，Good Writing is Bad Writing That Was Rewritten。[证据](../../../sources/notes/raibert1985good.md#e2)
[^raibert1985good-e3]: Raibert 1985，Spill the Beans Fast。[证据](../../../sources/notes/raibert1985good.md#e3)
[^raibert1985good-e4]: Raibert 1985，Trust Your Readers。[证据](../../../sources/notes/raibert1985good.md#e4)
[^raibert1985good-e5]: Raibert 1985，How to Get Unstuck。[证据](../../../sources/notes/raibert1985good.md#e5)
[^raibert1985good-e6]: Raibert 1985，Husband Your Readers。[证据](../../../sources/notes/raibert1985good.md#e6)
[^raibert1985good-e7]: Raibert 1985，Good Writing is Bad Writing That Was Rewritten。[证据](../../../sources/notes/raibert1985good.md#e7)
[^vandeursen2013writing-e1]: van Deursen 2013，Identify the Contributions。[证据](../../../sources/notes/vandeursen2013writing.md#e1)
[^vandeursen2013writing-e2]: van Deursen 2013，Identify the Contributions。[证据](../../../sources/notes/vandeursen2013writing.md#e2)
[^vandeursen2013writing-e3]: van Deursen 2013，Structure the Paper。[证据](../../../sources/notes/vandeursen2013writing.md#e3)
[^vandeursen2013writing-e4]: van Deursen 2013，Communicate the Contributions。[证据](../../../sources/notes/vandeursen2013writing.md#e4)
[^vandeursen2013writing-e5]: van Deursen 2013，Share Contributions Early。[证据](../../../sources/notes/vandeursen2013writing.md#e5)
[^olah2017debt-e1]: Olah & Carter 2017，Interpretive Labor。[证据](../../../sources/notes/olah2017debt.md#e1)
[^olah2017debt-e2]: Olah & Carter 2017，Clear Thinking。[证据](../../../sources/notes/olah2017debt.md#e2)
[^olah2017debt-e3]: Olah & Carter 2017，Research Distillation。[证据](../../../sources/notes/olah2017debt.md#e3)
[^huang2023introduction-e1]: Huang 2023，推文串开头，[原推文](https://twitter.com/jbhuang0604/status/1638029709073166336)。[证据](../../../sources/notes/huang2023introduction.md#e1)
[^huang2023introduction-e2]: Huang 2023，推文串 Q1–Q3，[原推文](https://twitter.com/jbhuang0604/status/1638029709073166336)。[证据](../../../sources/notes/huang2023introduction.md#e2)
[^huang2023introduction-e3]: Huang 2023，推文串 Q4，[原推文](https://twitter.com/jbhuang0604/status/1638029709073166336)。[证据](../../../sources/notes/huang2023introduction.md#e3)
[^huang2023introduction-e4]: Huang 2023，推文串 Q5，[原推文](https://twitter.com/jbhuang0604/status/1638029709073166336)。[证据](../../../sources/notes/huang2023introduction.md#e4)
[^huang2023introduction-e5]: Huang 2023，推文串 WHY 图部分，[原推文](https://twitter.com/jbhuang0604/status/1638029709073166336)。[证据](../../../sources/notes/huang2023introduction.md#e5)
