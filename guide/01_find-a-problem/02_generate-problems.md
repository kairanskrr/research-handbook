# 生成候选问题

> 本章的道理适用于各学科，例子和具体做法以计算机为例。四种生成办法各有出处：质疑假设的步骤来自管理学，按问题类型逐个问的分类来自软件工程，从话题写成问题的句式来自大学写作指导。

> **这一章必须做的事** `[本项目分析]`
>
> 1. **给生成问题划一段时间。** 写下从哪天到哪天，在这段时间里同时读、写、试；再定起点：从文献出发，还是从目标出发（[第 1 节](#1-先定时间和起点)）。
> 2. **至少用两种办法生成，其中一种不是找空白。** 找空白最容易上手，但想法容易和别人撞车；再配上质疑假设、按问题类型逐个问，或从话题写成问题（[第 2 节](#2-办法一找空白)到[第 5 节](#5-办法四从话题写成问题)）。
> 3. **带着清单找人聊。** 别只问"我该做什么"，要问"这几条里哪条有意思，哪条别人做过了"（[和人聊](#和人聊)）。
> 4. **全部记进同一份想法清单。** 每条写清：不对劲或不知道的是什么、从哪来、最快怎么验证；最想做的两三条，再用三步句式各写一句（[第 7 节](#7-记一份想法清单)）。
>
> **做到了就往下走：** 清单上有十条左右，来自至少三种办法或来源，每条都能一句话说清，至少和一位导师或懂行的人聊过。下一步：[动手探索](03_explore.md)。

## 你现在在哪里

你已经进入了一个方向，读过一批核心论文，大致知道这个领域在做什么、谁在做、用什么办法做。比如导师给你的方向是"用大模型做智能合约安全"，你读了二三十篇相关论文，手里还有一份读论文时随手记的问题记录。

但你还不知道自己要做什么。脑子里可能有一两个模模糊糊的念头，也可能一个都没有。你担心的是：好问题是不是早就被别人做完了？我怎么才能"想出"一个题目？

## 这一阶段要解决什么

从一个**方向**里，生成**一批**候选**问题**，攒成一份想法清单，带进下一步。

这里的"问题"，指这片领域里不对劲、不够好、或者还不知道的地方，见[核心术语](../00_start-here/key-concepts.md#问题)。它还不需要是一个能直接回答的研究问题，更不需要是一句写好的主张。那是[收敛成项目](05_converge.md)要做的事。

这一章要你做到两件事：

1. 用几种**能照着做的办法**生成问题，而不是干等灵感；
2. 把生成的都**记下来**，攒成一份想法清单。

怎么动手试、怎么筛，分别是[动手探索](03_explore.md)和[判断和筛选](04_judge-and-screen.md)的事。

**为什么是一批，而不是一个？** 选题时一个常见的错误，是抓住第一个想到的问题。一个项目通常要做好几年，草率的选择会带来很多挫败[^alon2009choose-e8]。手里只有一个想法，你没法比较，也就没法判断它好不好。

## 这一章怎么用

第 2–5 节是四种生成办法，第 6 节是几个补充来源。每种办法都写了怎么做、什么时候用、会产出什么，并用同一个方向从头走一遍。你会看到，四种办法从不同的路走到了同一个候选问题："现有大模型漏洞检测的评测结果，可能被数据泄露高估了。"

不必四种都用。一个参考 `[本项目分析]`：至少用两种，其中一种不是"找空白"。只用一种办法，生成的想法容易彼此相似。

---

## 1. 先定时间和起点

**给"生成问题"划出一段明确的时间。** 好问题不会在读第一篇论文时就出现。有一条建议是：新学生或博士后在头 3 个月里先别定课题，用这段时间读、讨论、计划[^alon2009choose-e9]。想法刚显得可行就急着动手，也容易出问题；多和它相处一段时间，常能想出更深的版本[^olah2021taste-e12]。

但也不能只读、只想。判断问题好坏的能力，离不开亲手做[^olah2021taste-e9]；怎样边想边动手试，见[动手探索](03_explore.md)。别在背景阅读上耗个没完、要读和想交替进行，上一章已经讲过，见[进入领域、探索文献](01_enter-a-field.md#关键判断)。

> **不同的看法：找问题该花多久？**
> - **多花时间：** 在选题上多花一周，后面可能省下几个月甚至几年[^alon2009choose-e8]。不过，提出这条建议的人也承认，不是每个人都能自由选题、有时间长时间寻找[^alon2009choose-e10]。
> - **别拖太久：** 尽早开始自己思考，和阅读交替进行[^eisnerproblems-e9]；找想法找到一定程度后，多想一小时，不如先随便动手做点什么[^carlini2026best-e13]。
>
> 实际操作中 `[本项目分析]`：给自己定一个时间段（几周到三个月，看你的阶段和导师的要求），在这段时间里**同时**读、写、试。时间到了就进入[判断和筛选](04_judge-and-screen.md)；筛不出来，就带着清单找导师一起定。

**两种起点。** 找问题大致有两种起点[^schulman2020opinionated-e6][^schulman2020opinionated-e8]：

- **从文献出发**：读到"别人怎么做 X"，想到怎么做得更好，然后去验证。它的缺点是容易撞车，因为大家读的是同样的文献，会想到相似的点子[^schulman2020opinionated-e7]。
- **从目标出发**：先定一个具体目标，比如"让开发者在部署合约前能可靠地发现重入漏洞"，再去解决通往目标路上的问题。目标会给你与众不同的视角，让你问出别人没问的问题[^schulman2020opinionated-e8]。

两种起点都能用下面的办法。区别在于，从目标出发时，你会更多地问"离目标还差什么"，而不只是"这篇论文还能怎么改" `[本项目分析]`。

**写下来：** 写下你给生成问题定的时间段（从哪天到哪天），以及你打算从文献出发、从目标出发，还是两者都试。如果从目标出发，用一句话写出这个目标。

## 2. 办法一：找空白

**它是什么。** 找出已有文献里还没做、没做好的地方，提出问题去补上。管理学研究者 Alvesson 和 Sandberg 把这叫作"找空白"：靠找出或构造已有文献里的空白来提出研究问题[^alvesson2013has-e2]。构造空白，常常是把几批不同的文献放在一起看[^alvesson2013has-e4]。

**怎么做** `[本项目分析]`：

1. **回到问题记录和核心论文。** 上一章让你建了一份问题记录，见[进入领域、探索文献](01_enter-a-field.md#6-记笔记一篇一份再加一份问题记录)。对最相关的几篇，再看一遍它们的"局限"和"未来工作"。
2. **找作者的简化和随意选择。** 作者在哪里做了可能有害的简化，或者做了随意的选择？这些地方是你可以换一种做法的机会[^eisnerproblems-e2]。例如只考虑了一种漏洞类型、只用了一个模型、只在一个数据集上测试，却没说明为什么。
3. **举一个让作者为难的例子。** 想想有什么例子能说明作者的想法，又有什么例子会让作者的说法站不住[^eisnerread-e3]。
4. **重新检查别人是怎么评估的。** 比较公平吗？结论真的被支持吗[^eisnerread-e8]？具体可以看：基线是不是太弱、指标是不是选得对自己有利 `[本项目分析]`。
5. **把每个空白写成一个问句。**

实验公不公平、结论能不能推广，以及"这篇论文的好想法还能用到哪里"，上一章的[带着问题读](01_enter-a-field.md#5-带着问题读)已经列出，这里不重复。复现时发现结果对不上、某个步骤论文没写清楚、换个设置就不行了，这些也都可能变成新问题 `[本项目分析]`。

**第 4 步为什么值得多花时间。** 一个方向通行的评估做法，本身就可能有问题，而且可能很普遍。下面的例子都来自计算机安全方向：

- 有研究者检查了 32 篇模糊测试论文（模糊测试是用大量随机输入测试程序、以发现缺陷的方法）的实验评估，每一篇都有问题[^klees2018evaluating-e2]。另一项研究分析了 30 篇使用机器学习的安全顶会论文，每篇至少有三个陷阱[^arp2022dos-e3]。
- 换一组评测对象，结论可能就变了：一个已发表的模糊测试工具，换成其他论文用过的两个程序，就不比基线好了[^klees2018evaluating-e3]。
- 评测集会被"用旧"：一套固定的评测集用多了，工具可能会针对它做没有根本好处的特殊优化[^klees2018evaluating-e7]；公开数据集被研究得越透，基于它开发的方法越会隐含地利用测试数据的信息，所以在知名数据集上的实验，应该再配上更新的数据[^arp2022dos-e5]。

别的方向是不是也这样，本文资料没有给出证据 `[本项目分析]`。做证明、做文本解读的研究可以跳过第 4 步。

**走一遍例子** `[本项目分析]`：

| 你在论文里注意到 | 空白写成问句 |
|---|---|
| 多篇论文都在同一个公开数据集上测试，数据集来自公开合约库 | 换到模型训练之后才部署的新合约上，检出率还一样高吗？ |
| 论文只报告了检出率，没报告误报 | 误报多到什么程度，开发者还愿不愿意用？ |
| 提示词是作者手写的，没说明怎么选的 | 换一种提示，结果变化大吗？ |
| 复现时某个基线跑出来比论文报告的差很多 | 原论文的设置有什么没写出来的地方？ |

第一行就是通往"评测结果被泄露高估"的入口：它还只是"没人在新合约上测过"这个空白，还没说出为什么可能不一样。

**什么时候用、会产出什么** `[本项目分析]`：读完一批论文、手里有问题记录时最好上手，几乎总能产出一批问题。产出多是"扩展""补上"式的问题：做得出来，但往往增量不大。

**它的局限。** Alvesson 和 Sandberg 不否认找空白也能有重要贡献，但认为它不刻意质疑已有文献背后的假设，所以很少产生新的重要理论[^alvesson2013has-e5]；他们在管理学里观察到，找空白式研究几乎一统天下[^alvesson2013has-e1]。这是管理学里的判断，别的领域是不是也这样，资料没有给出证据。另外，大家读同样的文献，找到的空白也相似，容易撞车[^schulman2020opinionated-e7]。所以别只用这一种办法 `[本项目分析]`。

**写下来：** 挑三篇你读过的、最相关的论文，每篇写出至少一个空白，并写成问句。

## 3. 办法二：质疑假设（问题化）

**它是什么。** 不是补上文献的空白，而是质疑文献里占主导的假设，由此提出研究问题。Alvesson 和 Sandberg 把这叫作"问题化"，作为找空白之外的另一条路[^alvesson2013has-e8]。他们的理由是：一个理论如果没有明显挑战读者原有的某些假设，即使做得极其严谨，也不太可能受到关注[^alvesson2013has-e6]。

这套办法来自管理学。他们举的例子是：绝大多数领导力研究默认员工需要或想要被领导；问题化可以把这当成一个错误的假设或一个开放问题，甚至提出有些人希望在工作中不被领导[^alvesson2020problematizing-e3]。

**怎么做。** 他们给出了六步[^alvesson2020problematizing-e5]。下面按六步写，每步配上我们例子里的做法 `[本项目分析]`：

1. **圈定一片文献。** 例如"用大模型做智能合约漏洞检测、并在公开评测集上报告结果的论文"。与其浅读一大堆，不如深读这片文献的奠基论文和适量代表性论文，这样更容易找出被当成理所当然的假设[^alvesson2020problematizing-e4]。读着读着，你可能会改这片文献的范围，这很正常[^alvesson2020problematizing-e7]。
2. **找出并写明背后的假设。** 有的写在论文里，有的连作者自己都没意识到 `[本项目分析]`。例子："评测集里的漏洞标注是对的""检出率高就是好工具""大模型没见过评测集里的合约"。
3. **评估这些假设，挑出最有问题、最有局限的。** 例子：第三条最可疑，因为公开合约很可能在大模型的训练数据里。
4. **提出一套替代假设。** 它应当有可能成为新贡献的起点。例子："模型可能见过评测合约，高分有一部分来自记忆，而不是真会找漏洞。"
5. **想想读者。** 在这个方向的读者看来，什么是新的、可信的、有趣的？例子：做检测的人会在乎，因为这关系到已发表的结果还能不能信。
6. **评估这套替代假设。** 看它能不能和同行展开一场新的、反直觉的讨论[^alvesson2020problematizing-e6]。例子：如果成立，大家要重新看已有的排名，这是一个反直觉的结论。

这样得到的候选问题是：**"现有评测结果里，有多少来自模型对评测合约的记忆？"** 它和办法一那条"新合约上检出率还一样高吗"指向同一件事，但已经说出了**为什么**可能不一样。

**第 2 步找假设，几个帮手：**

- **列出假设，试着放宽**，让方法在限制更少的条件下也能用[^huang2021ideas-e1]；**或者反过来，增加假设**，把通用方法用到具体问题上，利用领域知识改进它[^huang2021ideas-e2]。
- **问"笨问题"。** 数学里的一个办法是：拿一条公认的引理，问去掉一个前提会怎样[^taocareer-e8]。换到你的方向，就是对一个公认的结论问同样的问题 `[本项目分析]`。
- **特别留意整个方向都在沿用的做法。** 有时一篇有影响的早期论文在方法或评估上犯了关键错误，后来的人不加思考地跟着走，因为"大家都这么做"[^carlini2026best-e7]。一个信号是：你总忍不住想问"为什么大家都用明显不对的方式做"[^carlini2026best-e9]。
- **看问题是怎么被提出来的。** 问题最初怎么框定、从证据推到结论时用了什么假设，见上一章的[带着问题读](01_enter-a-field.md#5-带着问题读)。
- **从意外出发。** 他们还提到另一条路：特别留意经验材料里让你困惑的意外之处，先"制造一个谜"，再"解开它"[^alvesson2013has-e13]。翻真实数据时看到的怪现象，常是假设出问题的线索 `[本项目分析]`。

**作者自己说的局限：**

- **不是机械流程。** 问题化很依赖创造力、直觉、阅读、和人交谈；他们不相信有机械的程序，只认为一点结构有帮助[^alvesson2013has-e11]。
- **没有保证。** 按定义，大多数研究都做不到真正"有趣"，因为有趣意味着明显高于一般水平[^alvesson2013has-e12]。
- **仍要了解领域。** 走这条路，也要对自己的领域有合理的了解，并和重要的已有研究做比较[^alvesson2013has-e14]；挑战假设的研究要和已有文献联系起来，别人才会觉得有意义[^alvesson2013has-e7]。
- **难、要求高。** 他们承认，背后的假设很难发现，这种做法给研究者太多自由裁量，要求也太高[^alvesson2020problematizing-e8]。

**两种走偏：**

- **伪问题化。** 只是拿自己偏爱的现成理论去批评别人，只会重复那套理论的假设，不太可能带来新想法[^alvesson2013has-e9]。
- **为质疑而质疑。** 问题化不是否定前人的一切，同样要指出高质量的研究和想法[^alvesson2020problematizing-e10]。

**什么时候用、会产出什么** `[本项目分析]`：读过一批论文、开始觉得"大家都这么做，但好像不对"时最合适。产出比找空白少，但更可能是有分量的问题。它比找空白难，新手第一次用，最好和导师一起过一遍第 2、3 步。

**写下来：** 选你方向里最有影响的一两篇论文，按六步写：圈定的文献、三个假设、你认为最可疑的一个、替代假设、读者为什么会在乎。

## 4. 办法三：按问题类型逐个问

**它是什么。** 研究问题有几种常见类型。把你方向里的一个对象，按每种类型都问一遍，就能一次生成一串候选问题。下面的分类来自软件工程的实证研究[^easterbrook2008selecting-e38]，人文学科的解读类研究不一定适用 `[本项目分析]`。

**问题类型和问法：**

| 类型 | 问法 | 例子：对象是"大模型漏洞检测的评测结果" `[本项目分析]` |
|---|---|---|
| 存在 | X 存在吗？[^easterbrook2008selecting-e44] | 评测集里有没有在模型训练前就公开了的合约？ |
| 描述与分类 | X 是什么样？怎么分类？怎么测？[^easterbrook2008selecting-e44] | 泄露有哪几种（原样复制、改名后复制……）？怎么判断一份合约算不算泄露？ |
| 多常见 | X 多常发生？[^easterbrook2008selecting-e46] | 常用评测集里，泄露的合约占多大比例？ |
| 比较 | X 和 Y 有什么不同？[^easterbrook2008selecting-e47] | 泄露和没泄露的合约上，检出率差多少？ |
| 关系 | X 和 Y 相关吗？[^easterbrook2008selecting-e35] | 合约在网上出现得越多，模型越容易答对吗？ |
| 因果 | X 导致 Y 吗？[^easterbrook2008selecting-e37] | 是不是泄露导致了检出率偏高？ |
| 设计 | 做到 X 的有效办法是什么？[^easterbrook2008selecting-e39] | 怎样构建一个不泄露的评测集？ |
| 评估 | 怎样评估 X？怎样在 X 和 Y 之间选？[^shaw2003writing-e25] | 怎样公平地比较几种大模型的漏洞检测能力？ |

**怎么做** `[本项目分析]`：

1. **选一个对象。** 从你的方向里挑一个具体的东西：一类工具、一种现象、一套评测做法。
2. **按表逐行填。** 每种类型写一个问句。填不出来的跳过，别硬凑。
3. **对每个问句，查文献里有没有好答案。** 有些问题已发表的文献里已有好答案，这时用文献调研就能回答，不必自己做研究[^easterbrook2008selecting-e41]。
4. **留下没人答好的那几行**，写进想法清单。

**为什么要从上往下问。** 研究刚起步时，通常要先问"存在吗""是什么样"这类探索性问题[^easterbrook2008selecting-e45]。不问"多常见"，就无法判断某个情况是正常还是反常[^easterbrook2008selecting-e34]。"怎样做得更好"这类设计问题，前提是前面的知识问题已经回答过[^easterbrook2008selecting-e48]。所以，如果"泄露存在吗""多常见"都还没人认真回答，直接去做"怎样构建不泄露的评测集"就太早了 `[本项目分析]`。另外，"相关"不等于"因果"，证明因果通常难得多[^easterbrook2008selecting-e36]，表里"关系"和"因果"两行要分开写。

走完这张表，你会发现最上面几行（存在吗、多常见、差多少）都还没人答好。它们合起来，就是"评测结果被泄露高估了吗、高估了多少"，这是一个"测量"类的问题，见[核心术语](../00_start-here/key-concepts.md#研究套路) `[本项目分析]`。

**什么时候用、会产出什么** `[本项目分析]`：手里有一个具体对象，但不知道该问什么时最好用。它产出的是一串成梯子的问题，还能帮你看出先后：哪个要先回答，哪个要等前面答完。

**写下来：** 选你方向里的一个对象，按上表每种类型写一个问句，并标出哪些文献里已有答案。

## 5. 办法四：从话题写成问题

**它是什么。** 很多人卡在"只有话题，没有问题"。一份据 Booth 等人《The Craft of Research》改编的写作指南，把说清研究课题拆成三个小步骤[^booth2016craft-e1]，每步一个句式：

1. **说出话题：** "我在研究______。"[^booth2016craft-e2]
2. **加一个问句，说出你不知道什么：** "因为我想弄清谁 / 什么 / 是否 / 为什么 / 如何______。"[^booth2016craft-e3]
3. **说出意义：** "以帮助读者更好地理解______。"这一步检验你的问题是不是不只对你自己有意思[^booth2016craft-e4]。

三步分别说清：你写什么、你对它还不知道什么、读者为什么该关心[^booth2016craft-e7]。指南里的例子是：我在研究林肯的宿命论信念，因为我想弄清他对天命的信念怎样影响了他对内战起因的理解，以帮助读者理解他的宗教信念可能怎样影响了他的军事决策[^booth2016craft-e5]。

**用我们的例子填一遍** `[本项目分析]`：

- 第一稿："我在研究大模型做智能合约漏洞检测，因为我想弄清它效果怎么样，以帮助读者……"写不下去了。第二步太宽，第三步写不出来。
- 第二稿："我在研究大模型漏洞检测的评测方法，因为我想弄清现有评测集里的合约是否早就出现在模型的训练数据里、这会让检出率虚高多少，以帮助读者判断已发表的检测结果还有多可信。"

第二稿的第二步，就是前面几种办法得到的候选问题；第三步说出了谁会在乎。

**写不出第三步怎么办。** 写不出，说明你还没想清楚这个问题的意义。这很常见：说明意义是三步里最难的一步，可能要写完初稿才有确定答案[^booth2016craft-e10]。所以写不出时不必扔掉，在想法清单上标"意义未明"，接着想 `[本项目分析]`。话题也要足够具体，让你能在现有时间里找到、读完相关资料[^booth2016craft-e8]。指南还建议定期请室友、亲戚或朋友逼你把三步说完整，这样至少知道自己走到哪一步、还差什么[^booth2016craft-e6]。

**顺手再问三句。** 美国国防高级研究计划局用一份八问清单评估每一个提议的研究项目[^darpaheilmeier-e1][^darpaheilmeier-e2]。它主要用于评估，但前几问在生成时就能用：不用行话，你想做什么[^darpaheilmeier-e3]？现在是怎么做的，局限在哪里[^darpaheilmeier-e4]？谁在乎，成功了会带来什么不同[^darpaheilmeier-e5]？答不上来的，正好在想法清单上记下来。认真评估留给[收敛成项目](05_converge.md)的[值不值得做](05_converge.md#2-它值得做吗)、[别人做过没有](05_converge.md#3-别人做过了吗)、[拿什么让人信](05_converge.md#4-拿什么让人相信)和[做不做得出来](05_converge.md#5-你做得出来吗)。

**什么时候用、会产出什么** `[本项目分析]`：只有一个话题、或者想法太散时用。它不太会产出新想法，但能把模糊的想法写成一句完整的问题，并暴露出哪一步还没想清楚。前三种办法得到的每一条，都可以用它过一遍。

**写下来：** 对清单上你最想做的两三条，各用三步句式写一句。写不出第三步的，标上"意义未明"。

## 6. 其他来源

除了上面四种办法，下面几个地方也常冒出问题。它们更像"去哪里看"，可以和四种办法配合用 `[本项目分析]`。

### 实际中不好用的地方

论文里的方法在论文里好用，不等于在实际中好用。**去看现有的方法或系统在哪里做得不好**[^eisnerproblems-e5]。

- **给最好的方法做压力测试。** 把它放到更多样、限制更少的例子上，看它怎么失败。这是发现已有工作局限的好办法[^huang2021ideas-e4]。
- **离开实验室环境。** 以计算机安全方向为例：一篇总结机器学习用于安全研究时各种陷阱的论文，把"只在实验室环境中评估"列为其中一种，并建议只要可能，就在真实环境中评估[^arp2022dos-e2]。"放到真实环境中会怎样"，本身就可能是一个还没人回答的问题 `[本项目分析]`。
- **看数据。** 在很多领域，数据本身会提示问题[^eisnerproblems-e6]。动手翻一翻真实的合约、真实的漏洞报告，常常会看到论文里没提到的情况 `[本项目分析]`。
- **找卡住大家的瓶颈。** 哪些问题，不管有没有被公认，在阻碍这个领域进步？能不能解决？不能的话，能不能至少把它讲清楚[^eisnerproblems-e3]？

### 把别处的想法搬过来

- **关注新出现的工具。** 领域里出现了新工具，就试着用到自己的问题上[^huang2021ideas-e3]。"大模型与智能合约安全"这个方向本身，就是把一个新工具搬到一个老问题上 `[本项目分析]`。
- **找相似的问题。** 发现手头的问题和另一个领域的某个问题相似，就去查那个问题的文献，请教那个领域的专家[^taocareer-e21]。比如普通软件的漏洞检测已有很多年的积累，其中哪些做法还没用到智能合约上 `[本项目分析]`？
- **问另一个学科的人。** 如果你的方向是跨学科的，去问另一个学科的人觉得什么有意思[^eisnerproblems-e5]。
- **往前看一步。** 与其只盯着大家现在在做的，不如预判新技术出现后会冒出哪些大问题[^huang2023decide-e3]。

搬过来之前，先说得出两个领域在哪里不同、这个不同为什么让搬过来的事有挑战。只是"把 A 用在 B 上"，很容易被认为缺乏新意 `[本项目分析]`。

### 和人聊

有些问题不在论文里，在人的脑子里。导师会把你引向开放问题和圈内流传、没写下来的知识[^taocareer-e23]；关着门工作的人，多年后可能不知道什么问题值得做[^hamming1986you-e18]。怎么找人聊，见上一章的[找懂行的人聊](01_enter-a-field.md#8-找懂行的人聊)。

- **别怕做别人建议的题目。** 想法很多，本事在于挑哪个、做得多好[^schulman2020opinionated-e4]。
- **问用户和实际做事的人。** 在智能合约方向，就是写合约的开发者、做审计的人 `[本项目分析]`。
- **问"大家都知道挺重要，却没人认真做过"的问题。** 如果你觉得发现了一个，先问同事、查文献，确认还没人做[^eisnerproblems-e4]。
- **带上具体的东西。** 不要只问"你觉得我该做什么"，带上你的想法清单，问"这几个里你觉得哪个有意思，哪个别人做过了" `[本项目分析]`。

**写下来：** 选一个"公认效果好"的方法，写出你打算怎样看它在实际中哪里不好用；写出一个相邻领域里两个还没用到你方向上的做法；列出三个你可以去聊的人（至少一个不在你的研究组里）和要问的具体问题。

## 7. 记一份想法清单

**前面几节生成的东西，都要写进同一份清单。** 想法不记下来很快就会忘；记下来，才能比较、修改、过一段时间再看。

**为什么要攒，而不是用完就扔。** 大多数优秀的科学家心里装着 10 到 20 个重要问题，一直在找攻克的办法；看到一个新想法时，能立刻意识到它和哪个问题有关[^hamming1986you-e10]。几个月甚至几年里反复回到你脑中的想法，是你真正感兴趣的一个好信号[^alon2009choose-e13]，而这只有记下来、过段时间再看才看得出 `[本项目分析]`。错得难堪的想法也要私下存着，说不定以后能从中挽救出有用的东西[^taocareer-e19]。

**怎么记：**

- 记在一个固定的地方，每天随手记下想法[^schulman2020opinionated-e16]；
- 每一两周通读一遍，整理成小结[^schulman2020opinionated-e17]；
- 每条至少写清楚下面几项 `[本项目分析]`：

| 栏目 | 写什么 | 例子 |
|---|---|---|
| 一句话 | 不对劲或不知道的是什么 | 现有大模型漏洞检测的高准确率，可能部分来自评测集泄露 |
| 三步句式 | 我在研究……因为我想弄清……以帮助读者理解……（第 5 节） | 见第 5 节第二稿；写不出第三步就标"意义未明" |
| 来源 | 用哪种办法生成的（第 2–6 节） | 第 3 节：质疑"模型没见过评测集"这个假设；第 2、4 节也指向它 |
| 触发它的东西 | 哪篇论文、哪次对话、哪个数据 | 某篇论文的评测集来自公开合约库 |
| 最快的验证办法 | 用一两周能做的小尝试 | 抽 50 个评测样本，查它们是否公开出现过 |
| 日期和状态 | 新想到 / 在想 / 已放下（写原因） | 已放下：某组已发表，见某文 |

**清单要多长？** 本文资料没有给出统一的数字。作为一个参考 `[本项目分析]`：进入[判断和筛选](04_judge-and-screen.md)前，攒到十条左右、至少来自三种不同的办法或来源。全部来自同一种（比如都是"某论文换个数据集"），说明你找得还不够宽。一条想法被两三种办法同时生成，是个好信号，在"来源"栏都写上。

**写下来：** 建好你的想法清单，把前面各节"写下来"里冒出的想法都放进去，每条填满上表。

## 8. 接下来：动手试，再筛选

清单攒够了，先挑几条最想做的动手试一试，见[动手探索](03_explore.md)；再从清单里快速筛出两到四个，见[判断和筛选](04_judge-and-screen.md)。

---

## 关键判断

**先用哪种办法？** 可以这样选 `[本项目分析]`：

| 你现在的状态 | 先用 |
|---|---|
| 读了一批论文，问题记录里有不少疑问 | 办法一：找空白 |
| 总觉得"大家都这么做，但好像不对" | 办法二：质疑假设 |
| 有一个具体对象，但不知道该问什么 | 办法三：按问题类型逐个问 |
| 只有一个话题，或想法太散说不清 | 办法四：从话题写成问题 |
| 读不进论文，想法都很空 | 第 6 节：看数据、看实际中不好用的地方、和人聊 |

**什么时候该停止生成？** 可以这样判断 `[本项目分析]`：

| 情况 | 做法 |
|---|---|
| 清单不到五条，或都来自同一种办法 | 继续，换一种还没用过的办法 |
| 清单有十条左右，来自三种以上办法或来源 | 挑几条去[动手探索](03_explore.md)，再进入[判断和筛选](04_judge-and-screen.md) |
| 给自己定的时间到了，还是拿不准 | 带着清单找导师一起看 |

**一个想法不够"大"，要不要留？** 生成时不必太在意大小。很多小问题后面会被改写、合并或者放大；把问题稍微换个提法，常常能把不错的工作变成重大的工作[^hamming1986you-e13]。但要警惕那种"只能把某个指标提高一点点"的想法，它的上限一开始就是低的[^schulman2020opinionated-e10]。怎么筛，见[判断和筛选](04_judge-and-screen.md)。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 抓住第一个想到的问题 | 项目要做几年，草率选择会带来很多挫败[^alon2009choose-e8] |
| 一直读，迟迟不写想法、不动手 | 你注定要在不完全了解时开始；判断力离不开实践[^eisnerproblems-e8][^olah2021taste-e9] |
| 只会找空白 | 想法同质，容易撞车[^schulman2020opinionated-e7]；不质疑假设，很少产生新的重要理论（管理学里的观察）[^alvesson2013has-e5] |
| 拿自己偏爱的理论去批评别人，就当是质疑假设 | 这是伪问题化，只会重复那套理论的假设[^alvesson2013has-e9] |
| 读论文只挑刺、为质疑而质疑 | 会错过论文里能用到别处的好想法[^eisnerread-e6]；问题化同样要指出高质量的研究[^alvesson2020problematizing-e10] |
| 一上来就问"怎样做得更好" | 设计问题的前提是前面的知识问题已经回答过[^easterbrook2008selecting-e48] |
| 写不出"以帮助读者理解……"就当问题想清楚了 | 第三步检验问题是不是不只对你自己有意思[^booth2016craft-e4] |
| 想法只放在脑子里 | 记不住，也没法比较和回头看 `[本项目分析]` |
| 不和人聊 | 漏掉圈内知道、但还没写进论文的开放问题和已有工作[^taocareer-e23][^eisnerproblems-e9] |

## 产出物

- 一份想法清单，十条左右，来自至少三种办法或来源，每条填好上表各栏（第 7 节）
- 至少一种非"找空白"办法的完整记录：比如问题化六步的笔记，或一张按问题类型填好的表（第 3、4 节）
- 最想做的两三条，各有一句三步句式（第 5 节）

筛选结果不在这一章产出，见[判断和筛选](04_judge-and-screen.md)。

## 检查点

满足下面几条，可以进入下一步：

- [ ] 想法清单上有十条左右，来自至少三种不同的办法或来源
- [ ] 四种办法里至少用过两种，其中一种不是找空白
- [ ] 每条都能用一句话说出"不对劲或不知道的是什么"
- [ ] 最想做的两三条，能用三步句式说出来，或者标明了"意义未明"
- [ ] 至少和一位导师或懂行的人聊过这份清单

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 想了几周，一条想法都写不出来 | [进入领域、探索文献](01_enter-a-field.md)，再读一批，特别是最近一两年的论文和综述 |
| 每条想法都说不清"不对劲在哪"，也找不出领域里的假设 | 对领域了解还太少，回到[进入领域、探索文献](01_enter-a-field.md) |
| 清单上全是别人已经做过的 | 换办法：质疑假设（第 3 节）、实际中不好用的地方或和人聊（第 6 节） |
| 对这个方向本身已经没有兴趣 | 和导师谈，考虑换方向；逼自己做不觉得兴奋的题目，效率会低很多[^olah2021taste-e3] |

## 下一步

带着想法清单，进入[动手探索](03_explore.md)：对最想做的几条做小而快的尝试，把纸面上的想法变成"我大概知道这里是怎么回事"。之后在[判断和筛选](04_judge-and-screen.md)里筛出两到四个，带进[收敛成项目](05_converge.md)。

后面任何一步发现所有候选都站不住，就回到本章，换一种办法再生成一轮。

[^alon2009choose-e8]: Alon 2009，Take Your Time。[证据](../../sources/notes/alon2009choose.md#e8)
[^alon2009choose-e9]: Alon 2009，Take Your Time。[证据](../../sources/notes/alon2009choose.md#e9)
[^alon2009choose-e10]: Alon 2009，Take Your Time。[证据](../../sources/notes/alon2009choose.md#e10)
[^alon2009choose-e13]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../sources/notes/alon2009choose.md#e13)
[^alvesson2013has-e1]: Alvesson & Sandberg 2013，摘要，第 128 页。[证据](../../sources/notes/alvesson2013has.md#e1)
[^alvesson2013has-e2]: Alvesson & Sandberg 2013，Gap-Spotting 一节，第 131 页。[证据](../../sources/notes/alvesson2013has.md#e2)
[^alvesson2013has-e4]: Alvesson & Sandberg 2013，Gap-Spotting 一节，第 131–132 页。[证据](../../sources/notes/alvesson2013has.md#e4)
[^alvesson2013has-e5]: Alvesson & Sandberg 2013，Gap-Spotting 一节，第 132 页。[证据](../../sources/notes/alvesson2013has.md#e5)
[^alvesson2013has-e6]: Alvesson & Sandberg 2013，What Makes a Theory Interesting and Influential?，第 131 页。[证据](../../sources/notes/alvesson2013has.md#e6)
[^alvesson2013has-e7]: Alvesson & Sandberg 2013，Gap-Spotting 一节，第 131 页。[证据](../../sources/notes/alvesson2013has.md#e7)
[^alvesson2013has-e8]: Alvesson & Sandberg 2013，A Need to Consider Alternative Methodologies for Theory Development，第 144–145 页。[证据](../../sources/notes/alvesson2013has.md#e8)
[^alvesson2013has-e9]: Alvesson & Sandberg 2013，A Need to Consider Alternative Methodologies for Theory Development，第 145 页。[证据](../../sources/notes/alvesson2013has.md#e9)
[^alvesson2013has-e11]: Alvesson & Sandberg 2013，A Need to Consider Alternative Methodologies for Theory Development，第 145 页。[证据](../../sources/notes/alvesson2013has.md#e11)
[^alvesson2013has-e12]: Alvesson & Sandberg 2013，A Need to Consider Alternative Methodologies for Theory Development，第 144 页。[证据](../../sources/notes/alvesson2013has.md#e12)
[^alvesson2013has-e13]: Alvesson & Sandberg 2013，A Need to Consider Alternative Methodologies for Theory Development，第 146 页。[证据](../../sources/notes/alvesson2013has.md#e13)
[^alvesson2013has-e14]: Alvesson & Sandberg 2013，注释 3。[证据](../../sources/notes/alvesson2013has.md#e14)
[^alvesson2020problematizing-e3]: Alvesson & Sandberg 2020，The ideal of reflexivity。[证据](../../sources/notes/alvesson2020problematizing.md#e3)
[^alvesson2020problematizing-e4]: Alvesson & Sandberg 2020，Not accumulating but problematizing。[证据](../../sources/notes/alvesson2020problematizing.md#e4)
[^alvesson2020problematizing-e5]: Alvesson & Sandberg 2020，Not accumulating but problematizing。[证据](../../sources/notes/alvesson2020problematizing.md#e5)
[^alvesson2020problematizing-e6]: Alvesson & Sandberg 2020，Not accumulating but problematizing。[证据](../../sources/notes/alvesson2020problematizing.md#e6)
[^alvesson2020problematizing-e7]: Alvesson & Sandberg 2020，Not accumulating but problematizing。[证据](../../sources/notes/alvesson2020problematizing.md#e7)
[^alvesson2020problematizing-e8]: Alvesson & Sandberg 2020，Final Remarks。[证据](../../sources/notes/alvesson2020problematizing.md#e8)
[^alvesson2020problematizing-e10]: Alvesson & Sandberg 2020，Less is more。[证据](../../sources/notes/alvesson2020problematizing.md#e10)
[^arp2022dos-e2]: Arp 等人 2022，§2，P9 Lab-Only Evaluation。[证据](../../sources/notes/arp2022dos.md#e2)
[^arp2022dos-e3]: Arp 等人 2022，摘要。[证据](../../sources/notes/arp2022dos.md#e3)
[^arp2022dos-e5]: Arp 等人 2022，§2，P3 Data Snooping。[证据](../../sources/notes/arp2022dos.md#e5)
[^booth2016craft-e1]: 据 Booth 等人《The Craft of Research》改编的 Brandeis 大学写作讲义，开头段。[证据](../../sources/notes/booth2016craft.md#e1)
[^booth2016craft-e2]: 据 Booth 等人改编的 Brandeis 大学写作讲义，Step 1。[证据](../../sources/notes/booth2016craft.md#e2)
[^booth2016craft-e3]: 据 Booth 等人改编的 Brandeis 大学写作讲义，Step 2。[证据](../../sources/notes/booth2016craft.md#e3)
[^booth2016craft-e4]: 据 Booth 等人改编的 Brandeis 大学写作讲义，Step 3。[证据](../../sources/notes/booth2016craft.md#e4)
[^booth2016craft-e5]: 据 Booth 等人改编的 Brandeis 大学写作讲义，Step 3 中的例子。[证据](../../sources/notes/booth2016craft.md#e5)
[^booth2016craft-e6]: 据 Booth 等人改编的 Brandeis 大学写作讲义，Step 3 之后。[证据](../../sources/notes/booth2016craft.md#e6)
[^booth2016craft-e7]: 据 Booth 等人改编的 Brandeis 大学写作讲义，To summarize。[证据](../../sources/notes/booth2016craft.md#e7)
[^booth2016craft-e8]: 据 Booth 等人改编的宾州州立大学图书馆页面，Name Your Topic。[证据](../../sources/notes/booth2016craft.md#e8)
[^booth2016craft-e10]: 据 Booth 等人改编的宾州州立大学图书馆页面，Motivate Your Question。[证据](../../sources/notes/booth2016craft.md#e10)
[^carlini2026best-e7]: Carlini 2026，Ignore all the papers。[证据](../../sources/notes/carlini2026best.md#e7)
[^carlini2026best-e9]: Carlini 2026，Do something only you can do。[证据](../../sources/notes/carlini2026best.md#e9)
[^carlini2026best-e13]: Carlini 2026，Pick your ideas for impact。[证据](../../sources/notes/carlini2026best.md#e13)
[^darpaheilmeier-e1]: DARPA，Heilmeier Catechism，What is the Heilmeier Catechism?。[证据](../../sources/notes/darpaheilmeier.md#e1)
[^darpaheilmeier-e2]: DARPA，Heilmeier Catechism，What is the Heilmeier Catechism?。[证据](../../sources/notes/darpaheilmeier.md#e2)
[^darpaheilmeier-e3]: DARPA，Heilmeier Catechism，第 1 问。[证据](../../sources/notes/darpaheilmeier.md#e3)
[^darpaheilmeier-e4]: DARPA，Heilmeier Catechism，第 2、3 问。[证据](../../sources/notes/darpaheilmeier.md#e4)
[^darpaheilmeier-e5]: DARPA，Heilmeier Catechism，第 4 问。[证据](../../sources/notes/darpaheilmeier.md#e5)
[^easterbrook2008selecting-e34]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e34)
[^easterbrook2008selecting-e35]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e36]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e37]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e37)
[^easterbrook2008selecting-e38]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e38)
[^easterbrook2008selecting-e39]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e39)
[^easterbrook2008selecting-e41]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e41)
[^easterbrook2008selecting-e44]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e44)
[^easterbrook2008selecting-e45]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e45)
[^easterbrook2008selecting-e46]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e46)
[^easterbrook2008selecting-e47]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e47)
[^easterbrook2008selecting-e48]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e48)
[^eisnerproblems-e2]: Eisner，How to Find Research Problems，"small bones"。[证据](../../sources/notes/eisnerproblems.md#e2)
[^eisnerproblems-e3]: Eisner，How to Find Research Problems，"big bones"。[证据](../../sources/notes/eisnerproblems.md#e3)
[^eisnerproblems-e4]: Eisner，How to Find Research Problems，"ripe for the plucking"。[证据](../../sources/notes/eisnerproblems.md#e4)
[^eisnerproblems-e5]: Eisner，How to Find Research Problems，"identify new interesting problems"。[证据](../../sources/notes/eisnerproblems.md#e5)
[^eisnerproblems-e6]: Eisner，How to Find Research Problems，"identify new interesting problems"。[证据](../../sources/notes/eisnerproblems.md#e6)
[^eisnerproblems-e8]: Eisner，How to Find Research Problems，Finally。[证据](../../sources/notes/eisnerproblems.md#e8)
[^eisnerproblems-e9]: Eisner，How to Find Research Problems，Finally。[证据](../../sources/notes/eisnerproblems.md#e9)
[^eisnerread-e3]: Eisner 2009，How to Read a Technical Paper。[证据](../../sources/notes/eisnerread.md#e3)
[^eisnerread-e6]: Eisner 2009，How to Read a Technical Paper。[证据](../../sources/notes/eisnerread.md#e6)
[^eisnerread-e8]: Eisner 2009，How to Read a Technical Paper。[证据](../../sources/notes/eisnerread.md#e8)
[^hamming1986you-e10]: Hamming 1986，"Great Thoughts Time" 之后。[证据](../../sources/notes/hamming1986you.md#e10)
[^hamming1986you-e13]: Hamming 1986，把问题当作一类问题来解决的一段。[证据](../../sources/notes/hamming1986you.md#e13)
[^hamming1986you-e18]: Hamming 1986，"door open or the door closed" 一段。[证据](../../sources/notes/hamming1986you.md#e18)
[^huang2021ideas-e1]: Huang 2021，Relax assumptions。[证据](../../sources/notes/huang2021ideas.md#e1)
[^huang2021ideas-e2]: Huang 2021，Make more assumptions。[证据](../../sources/notes/huang2021ideas.md#e2)
[^huang2021ideas-e3]: Huang 2021，Grab a powerful hammer and find all the nails。[证据](../../sources/notes/huang2021ideas.md#e3)
[^huang2021ideas-e4]: Huang 2021，Stress test the state-of-the-art。[证据](../../sources/notes/huang2021ideas.md#e4)
[^huang2023decide-e3]: Huang 2023，Anticipate disruptive technologies。[证据](../../sources/notes/huang2023decide.md#e3)
[^klees2018evaluating-e2]: Klees 等人 2018，摘要。[证据](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees 等人 2018，§9。[证据](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e7]: Klees 等人 2018，§8。[证据](../../sources/notes/klees2018evaluating.md#e7)
[^olah2021taste-e3]: Olah 2021，开头。[证据](../../sources/notes/olah2021taste.md#e3)
[^olah2021taste-e9]: Olah 2021，Failure mode 2。[证据](../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e12]: Olah 2021，文末收录的 Andy Matuschak 的建议。[证据](../../sources/notes/olah2021taste.md#e12)
[^schulman2020opinionated-e4]: Schulman 2020，Honing Your Taste。[证据](../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e6]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../sources/notes/schulman2020opinionated.md#e6)
[^schulman2020opinionated-e7]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../sources/notes/schulman2020opinionated.md#e7)
[^schulman2020opinionated-e8]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../sources/notes/schulman2020opinionated.md#e8)
[^schulman2020opinionated-e10]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../sources/notes/schulman2020opinionated.md#e10)
[^schulman2020opinionated-e16]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e17)
[^shaw2003writing-e25]: Shaw 2003，§2.1，Table 1。[证据](../../sources/notes/shaw2003writing.md#e25)
[^taocareer-e8]: Tao，Career advice，Ask yourself dumb questions – and answer them!。[证据](../../sources/notes/taocareer.md#e8)
[^taocareer-e19]: Tao，Career advice，Use the wastebasket。[证据](../../sources/notes/taocareer.md#e19)
[^taocareer-e21]: Tao，Career advice，Be sceptical of your own work。[证据](../../sources/notes/taocareer.md#e21)
[^taocareer-e23]: Tao，Career advice，Talk to your advisor。[证据](../../sources/notes/taocareer.md#e23)
