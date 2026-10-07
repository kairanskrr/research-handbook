# 找到候选问题

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本章的道理适用于各学科，例子和具体做法以计算机为例。

## 你现在在哪里

你已经进入了一个方向，读过一批核心论文，大致知道这个领域在做什么、谁在做、用什么办法做。比如导师给你的方向是"用大模型做智能合约安全"，你读了二三十篇相关论文。

但你还不知道自己要做什么。脑子里可能有一两个模模糊糊的念头，也可能一个都没有。你担心的是：好问题是不是早就被别人做完了？我怎么才能"想出"一个题目？

## 这一阶段要解决什么

从一个**方向**里，找出**一批**候选**问题**，并做一次快速初筛，挑出两到四个值得认真想的，带进下一章。

这里的"问题"，指这片领域里不对劲、不够好、或者还不知道的地方，见[核心术语](../00_start-here/key-concepts.md#问题)。它还不需要是一个能直接回答的研究问题，更不需要是一句写好的主张。那是[收敛成项目](03_converge.md)要做的事。

这一章要你做到三件事：

1. 用几种具体的办法**找**问题，而不是干等灵感；
2. 把找到的都**记下来**，攒成一份想法清单；
3. 对清单做一次**粗筛**，留下几个进入下一步。

**为什么是一批，而不是一个？** 选题时一个常见的错误，是抓住第一个想到的问题。一个项目通常要做好几年，草率的选择会带来很多挫败[^alon2009choose-e8]。手里只有一个想法，你没法比较，也就没法判断它好不好。

---

## 1. 给找问题留一段时间，边读、边想、边试

**先说做法：** 给"找问题"划出一段明确的时间，在这段时间里同时做三件事：读文献、写下想法、动手做小尝试。时间到了，就进入初筛。

**为什么要专门留时间。** 好问题不会在读第一篇论文时就出现。有一条建议是：新学生或博士后在头 3 个月里先别定课题，用这段时间读、讨论、计划[^alon2009choose-e9]。想法刚显得可行就急着动手，也容易出问题；多和它相处一段时间，常能想出更深的版本[^olah2021taste-e12]。

**为什么又不能只读。** 还没动手就想挑出完美的问题，是一个陷阱：判断问题好坏的能力，离不开亲手做[^olah2021taste-e9]。别在背景阅读上耗个没完、要读和想交替进行，上一章已经讲过，见[进入领域](01_enter-a-field.md#关键判断)。

> **不同的看法：找问题该花多久？**
> - **多花时间：** 在选题上多花一周，后面可能省下几个月甚至几年[^alon2009choose-e8]。不过，提出这条建议的人也承认，不是每个人都能自由选题、有时间长时间寻找[^alon2009choose-e10]。
> - **别拖太久：** 尽早开始自己思考，和阅读交替进行[^eisnerproblems-e9]；找想法找到一定程度后，多想一小时，不如先随便动手做点什么[^carlini2026best-e13]。
>
> 实际操作中 `[本项目分析]`：给自己定一个时间段（几周到三个月，看你的阶段和导师的要求），在这段时间里**同时**读、写、试。时间到了就进入第 9 节的初筛；筛不出来，就带着清单找导师一起定。

**两种起点。** 找问题大致有两种起点[^schulman2020opinionated-e6][^schulman2020opinionated-e8]：

- **从文献出发**：读到"别人怎么做 X"，想到怎么做得更好，然后去验证。它的缺点是容易撞车，因为大家读的是同样的文献，会想到相似的点子[^schulman2020opinionated-e7]。
- **从目标出发**：先定一个具体目标，比如"让开发者在部署合约前能可靠地发现重入漏洞"，再去解决通往目标路上的问题。目标会给你与众不同的视角，让你问出别人没问的问题[^schulman2020opinionated-e8]。

两种起点都能用下面几节的办法找问题。区别在于，从目标出发时，你会更多地问"离目标还差什么"，而不只是"这篇论文还能怎么改" `[本项目分析]`。

**写下来：** 写下你给找问题定的时间段（从哪天到哪天），以及你打算从文献出发、从目标出发，还是两者都试。如果从目标出发，用一句话写出这个目标。

## 2. 从论文的空白和局限里找

你已经在读论文了，上一章也让你建了一份"问题记录"，见[进入领域](01_enter-a-field.md#6-记笔记一篇一份再加一份问题记录)。这一节是回到那份记录和那些论文，专门从里面挖候选问题。

**回头看论文时，多问两件事：**

- **作者在哪里做了简化，或者做了随意的选择？** 这些地方是你可以换一种做法的机会[^eisnerproblems-e2]。例如一篇论文只考虑了一种漏洞类型、只用了一个模型、只在一个数据集上测试，却没说明为什么。
- **能不能举出一个让作者为难的例子？** 想想有什么例子能说明作者的想法，又有什么例子会让作者的说法站不住[^eisnerread-e3]。

实验公不公平、结论能不能推广，以及"这篇论文的好想法还能用到哪里"，上一章的[带着问题读](01_enter-a-field.md#5-带着问题读)已经列出，这里不重复。

**复现时冒出来的问题也算。** 复现时发现结果对不上、某个步骤论文没写清楚、换个设置就不行了，这些都可能变成新问题 `[本项目分析]`。

用"大模型与智能合约安全"举例 `[本项目分析]`：

| 你在论文里注意到 | 可能的候选问题 |
|---|---|
| 多篇论文只在同一个公开数据集上测试 | 换到别的合约上，结论还成立吗？ |
| 论文只报告了检出率，没报告误报 | 误报多到什么程度，开发者还愿不愿意用？ |
| 提示词是作者手写的，没说明怎么选的 | 换一种提示，结果变化大吗？ |
| 复现时某个基线跑出来比论文报告的差很多 | 原论文的设置有什么没写出来的地方？ |

**写下来：** 挑三篇你读过的、最相关的论文，每篇写出至少一个"作者简化了什么"或"结论能不能推广"的疑问。

## 3. 从"实际中不好用"的地方找

论文里的方法在论文里好用，不等于在实际中好用。**去看现有的方法或系统在哪里做得不好**[^eisnerproblems-e5]。

**几种具体做法：**

- **给最好的方法做压力测试。** 别只在固定的评测集上跑，把它放到更多样、限制更少的例子上，看它怎么失败。这是发现已有工作局限的好办法，你的工作可以从这里填补空白[^huang2021ideas-e4]。
- **离开实验室环境。** 以计算机安全方向为例：一篇总结机器学习用于安全研究时各种陷阱的论文，把"只在实验室环境中评估、不讨论实际中的局限"列为其中一种，并建议只要可能，就在真实环境中评估[^arp2022dos-e2]。反过来说，"放到真实环境中会怎样"，本身就可能是一个还没人回答的问题 `[本项目分析]`。
- **看数据。** 在很多领域，数据本身会提示问题[^eisnerproblems-e6]。动手翻一翻真实的合约、真实的漏洞报告，常常会看到论文里没提到的情况 `[本项目分析]`。
- **找卡住大家的瓶颈。** 问自己：哪些问题，不管有没有被公认，在阻碍这个领域进步？能不能解决？不能的话，能不能至少把它讲清楚[^eisnerproblems-e3]？

在智能合约安全方向，你可以试试 `[本项目分析]`：

- 把一个公认效果好的检测方法，用到最近新部署的合约上，看它漏掉了什么；
- 找几位写合约的开发者，问他们为什么不用现有的检测工具；
- 读一批真实的漏洞事故报告，看其中有多少类漏洞是现有工具根本没考虑的。

**写下来：** 选一个你所在方向里"公认效果好"的方法或工具，写出你打算用什么办法看它在实际中哪里不好用（换数据、换场景、问用户），以及你预计它会在哪里失败。

## 4. 质疑已有工作的假设

每项研究都建立在一些假设之上。有的写在论文里，有的连作者自己都没意识到。**把这些假设找出来，问"如果不成立会怎样"**，就能得到候选问题 `[本项目分析]`。

**怎么做：**

- **列出假设，试着放宽。** 找出已有工作背后的假设，试着放宽，让方法在限制更少的条件下也能用[^huang2021ideas-e1]。
- **或者反过来，增加假设。** 把一个通用方法用到你的具体问题上，利用领域知识改进它[^huang2021ideas-e2]。比如通用的代码漏洞检测方法，用在智能合约上，可以利用合约特有的结构 `[本项目分析]`。
- **问"笨问题"。** 数学里的一个办法是：拿一条公认的引理，问去掉一个前提会怎样，结论能不能说得更强[^taocareer-e8]。换到你的方向，就是对一个公认的结论问同样的问题 `[本项目分析]`。
- **看问题是怎么被提出来的。** 问题最初怎么框定、从证据推到结论时用了什么假设，这些没明说的东西怎么找，见上一章的[带着问题读](01_enter-a-field.md#5-带着问题读)。

**特别留意整个方向都在沿用的做法。** 读完之后，要能把已有工作放到一边：已经做过的，就是已经做过了[^carlini2026best-e6]。有时一篇有影响的早期论文在方法、做法或评估上犯了关键错误，后来的人不加思考地跟着走，因为"大家都这么做"[^carlini2026best-e7]。一个信号是：读某个方向的论文时，你总忍不住想问"为什么大家都用明显不对的方式做"[^carlini2026best-e9]。

在智能合约方向，可以问的假设 `[本项目分析]`：

- "评测集里的漏洞标注是对的"：标注是谁做的、怎么核对的？
- "检出率高就是好工具"：开发者真正在乎的是不是这个？
- "大模型没见过评测集里的合约"：公开合约很可能在它的训练数据里。

**写下来：** 选你方向里最有影响的一两篇论文，列出它们依赖的三个假设。对每个假设，写一句"如果它不成立，会发生什么"。

## 5. 重新检查别人是怎么评估的

> 本节适用于靠实验、测量来支撑结论的研究。做证明、做文本解读的读者可以跳过。

**一个方向通行的评估做法，本身就可能有问题，而且可能很普遍。** 下面两个例子都来自计算机安全方向：

- 有研究者检查了 32 篇模糊测试论文（模糊测试是用大量随机输入测试程序、以发现缺陷的方法）的实验评估，每一篇都有问题[^klees2018evaluating-e2]。
- 另一项研究分析了过去十年 30 篇使用机器学习的安全顶会论文，每篇至少有三个陷阱，有几个陷阱影响了大多数论文[^arp2022dos-e3]。

别的方向是不是也这样，本文资料没有给出证据。但这两个例子说明：**重新检查一个方向的评估做法，有可能找到实实在在的问题**，值得花点时间查一查 `[本项目分析]`。

**可以检查的地方（例子仍来自安全方向）：**

- **换一组评测对象，结论还成立吗？** 一个已发表的模糊测试工具，在原论文选的程序上表现好，换成其他论文用过的两个程序，就不比基线好了[^klees2018evaluating-e3]。
- **评测集是不是被"用旧了"？** 一套固定的评测集用多了，工具可能会针对它做特殊优化，而这些优化没有根本性的好处[^klees2018evaluating-e7]。机器学习用于安全的研究里也有类似提醒：公开数据集的特点被研究得越来越透，基于它开发的方法会隐含地利用测试数据的信息，所以在知名数据集上的实验，应该再配上更新的数据[^arp2022dos-e5]。
- **比较公平吗？结论真的被支持吗[^eisnerread-e8]？** 具体可以看：基线是不是太弱、指标是不是选得对自己有利 `[本项目分析]`。

如果你发现了这类问题，"指出并修正它"本身就可以是一项研究，属于"测量"这种研究套路，见[核心术语](../00_start-here/key-concepts.md#研究套路)。怎么判断这个发现够不够做成项目，是下一章的事。

**写下来：** 列出你方向里最常用的两三个评测集或评估做法。对每一个，写下你怀疑它可能有什么问题，以及你可以用什么最简单的办法验证这个怀疑。

## 6. 把别处的想法搬过来

**一个领域里已经解决的事，在另一个领域可能还没人试过。** 留意相邻领域，是找问题的另一条路 `[本项目分析]`。

**怎么做：**

- **关注新出现的工具。** 领域里出现了新工具，就试着用到自己的问题上[^huang2021ideas-e3]。"大模型与智能合约安全"这个方向本身，就是把一个新工具搬到一个老问题上 `[本项目分析]`。
- **找相似的问题。** 发现手头的问题和另一个领域的某个问题相似（或至少可以类比），就去查那个问题的文献，请教那个领域的专家，了解他们最新的看法[^taocareer-e21]。比如普通软件的漏洞检测已有很多年的积累，其中哪些做法还没用到智能合约上 `[本项目分析]`？
- **问另一个学科的人。** 如果你的方向是跨学科的，去问另一个学科的人觉得什么有意思[^eisnerproblems-e5]。
- **往前看一步。** 与其只盯着大家现在在做的，不如预判新技术出现后会冒出哪些大问题[^huang2023decide-e3]。

**搬过来之前，先想清楚为什么这里会不一样。** 只是"把 A 用在 B 上"，很容易被认为缺乏新意。要说得出两个领域在哪里不同，这个不同为什么让搬过来的事有挑战、值得做 `[本项目分析]`。

**写下来：** 写出一个和你方向相邻的领域，列出那里两个已经比较成熟、但在你的方向上还没人试过（或你没见过）的做法。

## 7. 和人聊

**有些问题不在论文里，在人的脑子里。** 导师会把你引向开放问题和圈内流传、没写下来的知识[^taocareer-e23]；关着门工作的人，多年后可能不知道什么问题值得做[^hamming1986you-e18]。为什么要聊、怎么找人聊，上一章的[找懂行的人聊](01_enter-a-field.md#8-找懂行的人聊)已经讲过。这一节只说找问题时的几个重点。

- **别怕做别人建议的题目。** 做有经验的人建议的想法并不丢人：想法很多，本事在于挑哪个、做得多好[^schulman2020opinionated-e4]。
- **问用户和实际做事的人。** 在智能合约方向，就是写合约的开发者、做审计的人。他们知道实际中什么不好用 `[本项目分析]`。
- **问"大家都知道挺重要，却没人认真做过"的问题。** 每个领域都有这样的问题；如果你觉得发现了一个，先问同事、查文献，确认还没人做[^eisnerproblems-e4]。

**聊的时候带上具体的东西。** 不要只问"你觉得我该做什么"，带上你的想法清单（下一节），问"这几个里你觉得哪个有意思，哪个别人做过了" `[本项目分析]`。

**写下来：** 列出三个你可以去聊的人（至少一个不在你的研究组里），以及你打算问每个人的一个具体问题。

## 8. 记一份想法清单

**前面几节找到的东西，都要写进同一份清单。** 想法不记下来很快就会忘；记下来，才能比较、修改、过一段时间再看。

**为什么要攒，而不是用完就扔。** 大多数优秀的科学家心里装着 10 到 20 个重要问题，一直在找攻克的办法；看到一个新想法时，能立刻意识到它和哪个问题有关[^hamming1986you-e10]。几个月甚至几年里反复回到你脑中的想法，是你真正感兴趣的一个好信号[^alon2009choose-e13]，而这只有记下来、过段时间再看才看得出 `[本项目分析]`。错得难堪的想法也要私下存着，说不定以后能从中挽救出有用的东西[^taocareer-e19]。

**怎么记：**

- 记在一个固定的地方，每天随手记下想法[^schulman2020opinionated-e16]；
- 每一两周通读一遍，整理成小结[^schulman2020opinionated-e17]；
- 每条至少写清楚下面几项 `[本项目分析]`：

| 栏目 | 写什么 | 例子 |
|---|---|---|
| 一句话 | 不对劲或不知道的是什么 | 现有大模型漏洞检测的高准确率，可能部分来自评测集泄露 |
| 来源 | 从哪里冒出来的（第 2–7 节哪一种） | 第 4 节：质疑"模型没见过评测集"这个假设 |
| 触发它的东西 | 哪篇论文、哪次对话、哪个数据 | 某篇论文的评测集来自公开合约库 |
| 最快的验证办法 | 用一两周能做的小尝试 | 抽 50 个评测样本，查它们是否公开出现过 |
| 日期和状态 | 新想到 / 在想 / 已放下（写原因） | 已放下：某组已发表，见某文 |

**清单要多长？** 本文资料没有给出统一的数字。作为一个参考 `[本项目分析]`：进入初筛前，攒到十条左右、至少来自三种不同的来源，比较容易筛出真正好的。全部来自同一种来源（比如都是"某论文换个数据集"），说明你找得还不够宽。

**写下来：** 建好你的想法清单，把前面各节的"写下来"里冒出的想法都放进去，每条填满上表的五栏。

## 9. 快速初筛：留下两到四个

清单攒够了，做一次**粗筛**。这一步只花一两个小时，目的不是选出最终题目，而是把明显不值得深想的划掉，留下两到四个，带进下一章仔细收敛 `[本项目分析]`。

**对每条想法，快速问四件事** `[本项目分析]`：

1. **能用一句话说清"不对劲的是什么"吗？** 说不清的，先留在清单里继续想，不进入这一轮。
2. **能看到一个下手的办法吗？** 问题重要，不只看结果有多大，还要看你有没有合理的攻克途径[^hamming1986you-e2]。连第一步怎么做都想不出的，先放下。
3. **它是不是被另一条全面压过？** 如果 A 在可行性和价值两方面都比 B 好，就可以划掉 B[^alon2009choose-e6]。粗看就行，不需要打分。
4. **你还想着它吗？** 问自己：如果世界上只有我一个人，我会做这些里的哪一个[^alon2009choose-e12]？同时留意，你是真觉得有意思，还是因为大家都在做。不要扎堆追最热的问题[^huang2023decide-e1]，那里撞车的风险更大 `[本项目分析]`。

**这一步不做的事。** 不在这里查清"别人做过没有"、不在这里想清"要什么证据"、不在这里评估数据和算力。那些是[收敛成项目](03_converge.md)的六个问题，需要对两到四个候选认真做。初筛时对每条只花几分钟 `[本项目分析]`。

**拿不准，就请导师帮你筛。** 把清单给导师，请他对每条打 1–10 分，对你们分歧大的几条深入讨论[^olah2021taste-e4]。这既是筛选，也是在练你判断问题好坏的能力。这种能力（常被叫作"研究品味"）怎么长期培养，见[有意识地培养研究品味](../general/1_before/02_choosing_a_problem.md#4-有意识地培养研究品味)。

**写下来：** 在想法清单上标出这一轮留下的两到四条，并对每条被划掉的写一句原因（"没有下手办法""被第 X 条压过"等）。

---

## 关键判断

**什么时候该停止找、开始筛？** 可以这样判断 `[本项目分析]`：

| 情况 | 做法 |
|---|---|
| 清单不到五条，或都来自同一种来源 | 继续找，换第 2–7 节里你还没用过的办法 |
| 清单够长，但划掉一轮后一条不剩 | 多半是找得太窄或太大，回到第 3、4 节从实际和假设里找 |
| 清单够长，初筛后留下两到四条 | 进入下一章 |
| 给自己定的时间到了，还是拿不准 | 带着清单找导师，一起定两到四条 |

**一个想法不够"大"，要不要留？** 初筛时不必太在意大小。很多小问题在收敛时会被改写、合并或者放大；把问题稍微换个提法，常常能把不错的工作变成重大的工作[^hamming1986you-e13]。但要警惕那种"只能把某个指标提高一点点"的想法，它的上限一开始就是低的[^schulman2020opinionated-e10]。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 抓住第一个想到的问题 | 项目要做几年，草率选择会带来很多挫败[^alon2009choose-e8] |
| 一直读，迟迟不写想法、不动手 | 你注定要在不完全了解时开始；判断力离不开实践[^eisnerproblems-e8][^olah2021taste-e9] |
| 只从"某论文换个数据集"一种来源找 | 想法同质，容易和读同样文献的人撞车[^schulman2020opinionated-e7] |
| 读论文只挑刺 | 会错过论文里能用到别处的好想法[^eisnerread-e6] |
| 想法只放在脑子里 | 记不住，也没法比较和回头看 `[本项目分析]` |
| 不和人聊 | 漏掉圈内知道、但还没写进论文的开放问题和已有工作[^taocareer-e23][^eisnerproblems-e9] |
| 初筛时就把每条都想得很深 | 时间花在了终会被划掉的想法上；深入的判断留给下一章 `[本项目分析]` |
| 追最热的方向 | 不要扎堆追最热的问题[^huang2023decide-e1]；不在最热的方向，反而更容易脱颖而出[^carlini2026best-e12] |

## 产出物

- 一份想法清单，十条左右，来自至少三种来源，每条填好五栏（第 8 节）
- 初筛结果：留下的两到四条，以及每条被划掉的原因（第 9 节）
- 每个留下的候选，各有一个"最快的验证办法"

## 检查点

满足下面几条，可以进入下一步：

- [ ] 想法清单上有十条左右，来自至少三种不同的来源
- [ ] 每条都能用一句话说出"不对劲或不知道的是什么"
- [ ] 至少和一位导师或懂行的人聊过这份清单
- [ ] 初筛后留下两到四条，并说得出为什么留它们、为什么划掉其他的
- [ ] 每个留下的候选，都想到了一个一两周内能做的小尝试

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 想了几周，一条想法都写不出来 | [进入领域](01_enter-a-field.md)，再读一批，特别是最近一两年的论文和综述 |
| 每条想法都说不清"不对劲在哪" | 对领域了解还太少，回到[进入领域](01_enter-a-field.md) |
| 清单上全是别人已经做过的 | 换来源：从实际中不好用的地方（第 3 节）或评估问题（第 5 节）找，或者和人聊（第 7 节） |
| 对这个方向本身已经没有兴趣 | 和导师谈，考虑换方向；逼自己做不觉得兴奋的题目，效率会低很多[^olah2021taste-e3] |

## 下一步

带着初筛留下的两到四个候选，进入[收敛成项目](03_converge.md)：把每个候选写成一句想证明的结论，判断值不值得做、别人做过没有、需要什么证据、你做不做得出来，最后收敛成一页项目简介。

收敛时，有的候选会被否定。这很正常。被否定的放回想法清单，写上原因；如果所有候选都站不住，就回到本章，再找一轮。

[^alon2009choose-e6]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../sources/notes/alon2009choose.md#e6)
[^alon2009choose-e8]: Alon 2009，Take Your Time。[证据](../../sources/notes/alon2009choose.md#e8)
[^alon2009choose-e9]: Alon 2009，Take Your Time。[证据](../../sources/notes/alon2009choose.md#e9)
[^alon2009choose-e10]: Alon 2009，Take Your Time。[证据](../../sources/notes/alon2009choose.md#e10)
[^alon2009choose-e12]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../sources/notes/alon2009choose.md#e12)
[^alon2009choose-e13]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../sources/notes/alon2009choose.md#e13)
[^arp2022dos-e2]: Arp 等人 2022，§2，P9 Lab-Only Evaluation。[证据](../../sources/notes/arp2022dos.md#e2)
[^arp2022dos-e3]: Arp 等人 2022，摘要。[证据](../../sources/notes/arp2022dos.md#e3)
[^arp2022dos-e5]: Arp 等人 2022，§2，P3 Data Snooping。[证据](../../sources/notes/arp2022dos.md#e5)
[^carlini2026best-e6]: Carlini 2026，Ignore all the papers。[证据](../../sources/notes/carlini2026best.md#e6)
[^carlini2026best-e7]: Carlini 2026，Ignore all the papers。[证据](../../sources/notes/carlini2026best.md#e7)
[^carlini2026best-e9]: Carlini 2026，Do something only you can do。[证据](../../sources/notes/carlini2026best.md#e9)
[^carlini2026best-e12]: Carlini 2026，Get lucky: you're well suited to solve important problems。[证据](../../sources/notes/carlini2026best.md#e12)
[^carlini2026best-e13]: Carlini 2026，Pick your ideas for impact。[证据](../../sources/notes/carlini2026best.md#e13)
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
[^hamming1986you-e2]: Hamming 1986，"important problems" 一段。[证据](../../sources/notes/hamming1986you.md#e2)
[^hamming1986you-e10]: Hamming 1986，"Great Thoughts Time" 之后。[证据](../../sources/notes/hamming1986you.md#e10)
[^hamming1986you-e13]: Hamming 1986，把问题当作一类问题来解决的一段。[证据](../../sources/notes/hamming1986you.md#e13)
[^hamming1986you-e18]: Hamming 1986，"door open or the door closed" 一段。[证据](../../sources/notes/hamming1986you.md#e18)
[^huang2021ideas-e1]: Huang 2021，Relax assumptions。[证据](../../sources/notes/huang2021ideas.md#e1)
[^huang2021ideas-e2]: Huang 2021，Make more assumptions。[证据](../../sources/notes/huang2021ideas.md#e2)
[^huang2021ideas-e3]: Huang 2021，Grab a powerful hammer and find all the nails。[证据](../../sources/notes/huang2021ideas.md#e3)
[^huang2021ideas-e4]: Huang 2021，Stress test the state-of-the-art。[证据](../../sources/notes/huang2021ideas.md#e4)
[^huang2023decide-e1]: Huang 2023，Find your position。[证据](../../sources/notes/huang2023decide.md#e1)
[^huang2023decide-e3]: Huang 2023，Anticipate disruptive technologies。[证据](../../sources/notes/huang2023decide.md#e3)
[^klees2018evaluating-e2]: Klees 等人 2018，摘要。[证据](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees 等人 2018，§9。[证据](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e7]: Klees 等人 2018，§8。[证据](../../sources/notes/klees2018evaluating.md#e7)
[^olah2021taste-e3]: Olah 2021，开头。[证据](../../sources/notes/olah2021taste.md#e3)
[^olah2021taste-e4]: Olah 2021，Exercise 1。[证据](../../sources/notes/olah2021taste.md#e4)
[^olah2021taste-e9]: Olah 2021，Failure mode 2。[证据](../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e12]: Olah 2021，文末收录的 Andy Matuschak 的建议。[证据](../../sources/notes/olah2021taste.md#e12)
[^schulman2020opinionated-e4]: Schulman 2020，Honing Your Taste。[证据](../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e6]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../sources/notes/schulman2020opinionated.md#e6)
[^schulman2020opinionated-e7]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../sources/notes/schulman2020opinionated.md#e7)
[^schulman2020opinionated-e8]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../sources/notes/schulman2020opinionated.md#e8)
[^schulman2020opinionated-e10]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../sources/notes/schulman2020opinionated.md#e10)
[^schulman2020opinionated-e16]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e17)
[^taocareer-e8]: Tao，Career advice，Ask yourself dumb questions – and answer them!。[证据](../../sources/notes/taocareer.md#e8)
[^taocareer-e19]: Tao，Career advice，Use the wastebasket。[证据](../../sources/notes/taocareer.md#e19)
[^taocareer-e21]: Tao，Career advice，Be sceptical of your own work。[证据](../../sources/notes/taocareer.md#e21)
[^taocareer-e23]: Tao，Career advice，Talk to your advisor。[证据](../../sources/notes/taocareer.md#e23)
