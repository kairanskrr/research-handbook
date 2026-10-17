# 执行与迭代

> 本章的道理适用于各学科，例子和具体做法以计算机为例。

> **这一章必须做的事**
>
> 1. **确认你在检验一个具体的假设。** 写下假设，以及什么结果会说明它不对；写不出来，先回到[动手探索](../01_find-a-problem/03_explore.md)（[第 1 节](#1-先认清自己在哪个阶段)）。
> 2. **每次运行都留下记录。** 一个结果只要可能有用，就记下哪版代码、哪版数据、什么参数、输出在哪（[第 3 节](#3-每次运行都留下记录)）。
> 3. **改了做法，记下来、说出来。** 每次改动写进改动记录，补上为什么改；大的改动告诉导师（[第 4 节](#4-改了做法要记下来说出来)）。
> 4. **卡住时按固定步骤排查，换方向前写出理由。** 先写"输入 / 预期 / 实际"三行；要放弃一个方向，先写出它注定不行的理由（[第 5 节](#5-卡住时按固定步骤排查)、[第 6 节](#6-坚持还是换方向)）。
> 5. **每周写周报，定期回顾。** 周报里"改动"和"卡在"两栏不要空着；每周定一个固定时间抬头看路（[第 7 节](#7-向导师汇报进展)、[第 8 节](#8-定期抬头看路)）。
>
> **做到了就往下走：** 计划里每个里程碑要的证据都拿到了，或者已经和导师商定改了主张；每个要进论文的结果都说得出怎么来的；你能用一句话说出结果支持什么、不支持什么。下一步：[分析与解读](07_analyze-and-interpret.md)。

## 你现在在哪里

你有一份证据清单和一份研究计划（见[从研究问题到证据清单](01_question-to-evidence.md)和[形成研究计划](03_research-plan.md)），效度威胁也想过了，最小版本已经从头到尾跑通（见[最小可跑版本](05_pilot-and-derisk.md)）。现在要真正做起来，而且要做上几周、几个月。

这时你可能遇到的是：

- 每天都在跑实验，可一周下来说不清自己往前走了多少；
- 结果文件越来越多，已经分不清哪个是用哪版代码、哪组参数跑出来的；
- 某个地方卡了两周，不知道是该再试试，还是该换个做法；
- 每周和导师见面，不知道该汇报什么，"还没做出来"说不出口。

## 这一阶段要解决什么

把计划一轮一轮地变成证据，并且在这个过程中不迷路。具体来说，是回答下面六个问题：

1. 我现在是在摸索，还是在检验一个具体的想法？
2. 怎样让每一轮"想法 → 结果"更快？
3. 每次运行，留下了什么记录？几个月后还找得回来吗？
4. 中途改了做法，记下来、说出来了吗？
5. 卡住了，怎么排查？什么时候该换方向？
6. 怎样向导师汇报，让导师帮得上忙？

这些问题每周都会重复出现，不是做一遍就完的。本章给的是**每天、每周都能用的做法**。

---

## 1. 先认清自己在哪个阶段

执行时，如果你写不出一个具体的假设，也说不出什么证据能判断它对不对，说明你还在探索阶段。怎样分辨探索和检验、探索时该做什么，见[动手探索](../01_find-a-problem/03_explore.md)。退回探索阶段是正常的，不代表你搞砸了[^nanda2025process-e6]。

**写下来：** 写下你正在检验的假设，以及什么结果会说明它不对。写不出来，就先回到[动手探索](../01_find-a-problem/03_explore.md)。

## 2. 让每一轮"想法 → 结果"更快

从"有了一个实验想法"到"看到结果"的过程，叫一轮反馈；这段时间短，就说反馈"紧"[^nanda2025mindsets-e10]。反馈越紧，同样的时间里能试的想法越多。

**怎么做：**

- **先做快而粗糙的实验。** 先花一点时间看到初步迹象，远好于花几周做一个结论明确但又贵又慢的实验[^nanda2025mindsets-e11]。项目早期，尽量选一天之内能出结果的实验[^perez2024tips-e3]。
- **用小例子和替代任务。** 找能缩短等待时间的小例子和替代任务[^huang2023unstuck-e6]：小例子是刻意简化、只保留核心机制的例子，替代任务是比真实任务更小更快、但能说明同一件事的任务。最好的小例子，是能抓住核心想法的最简单的那个[^freeman2013research-e4]。
- **每次只改一个地方。** 这样才知道结果变了是哪个改动造成的[^freeman2013research-e2]。
- **舍得花时间改进工具。** 一位机器学习研究者发现，脚本超过大约一秒才开始给出有用的输出，自己的效率就开始下降[^carlini2022rapid-e2]，于是从研究里抽出几天写工具，让流程快了很多[^carlini2022rapid-e3]。"一秒"是他个人在机器学习里的体会，不是通用标准。

**贯穿例子**：正式执行时，你要在两千个合约上找泄露、让几个模型去检测、再比较检出率。

| 慢的做法 | 快的做法 |
|---|---|
| 每改一次泄露判定规则，就在全部两千个合约上重新比对 | 先在固定的 20 个合约上试，规则稳定了再扩大 |
| 每次都重新调用大模型接口 | 把已经得到的回答存下来，只重跑改动过的部分 |
| 一次换了泄露定义、模型和评分规则 | 一次只换一样，其余保持不变 |
| 人工翻输出找错误 | 写个小脚本，自动列出判断错的合约 |

> **不同的看法：快一点，还是慢一点？**
>
> - 一种看法强调求快：有研究者说，自己只有在能快速迭代想法时才做得出好研究[^carlini2022rapid-e1]；宁可先做快而粗糙的实验[^nanda2025mindsets-e11]。
> - 另一种看法的第一条建议是"慢下来才能快"[^freeman2013research-e1]：放慢，核实自己的假设，每次只改一处[^freeman2013research-e2]。
> - 两者并不完全矛盾。主张求快的人也承认，以速度为名变得马虎、引入一堆错误，长期反而更费时间[^nanda2025mindsets-e14]。
>
> 实际操作中：**缩短的是每一轮的周期，不是降低每一轮的严谨程度。** 用更小、更简单的问题让每一轮变快；每一轮之内，仍然一次只改一处、核实假设。

**适用范围**："一天出结果"来自计算机和机器学习。在一次实验要几个月的学科（临床研究、野外调查、长期培养、大规模访谈），可以用小样本试做、模拟，或先用公开数据检验想法，来缩短每一轮。

先做哪一部分，见[形成研究计划](03_research-plan.md#4-排顺序最可能失败的先做)和[最小可跑版本](05_pilot-and-derisk.md)。

**写下来：** 估一下你现在一轮"想法 → 结果"要多久。写出一个能把它缩短一半的办法。

## 3. 每次运行都留下记录

跑得快以后，最常见的问题是：结果一多，就分不清哪个是怎么来的。**一个结果只要可能有用，就记下它是怎么得到的**[^sandve2013ten-e7]：哪版代码、哪版数据、什么参数、输出在哪；每天的想法和实验记进可以搜索的研究日志[^schulman2020opinionated-e16][^dredze2012successful-e2]。具体记哪些栏目、日志怎么写、目录怎么分，见[整理科研材料](../08_throughout/organizing_materials.md#3-每个结果都要能追溯到它是怎么来的)第 3 节和[第 5 节](../08_throughout/organizing_materials.md#5-分清三种笔记)。

执行阶段还要**另开两份小文件：**

- **亮点记录**：只收特别有意思的结果，方便发现它们之间的联系[^nanda2025process-e4]。
- **想法清单**：做项目时冒出新想法，先记在这里，然后回到手头的事[^carlini2024logfile-e2]。隔一段时间再读，两次都觉得好的想法才值得做[^carlini2024logfile-e3]。

**每一两周回顾一次日志**，压缩成一份总结[^schulman2020opinionated-e17]，看看自己是不是在几个想法之间跳来跳去（见第 6 节）。

**写下来：** 建好亮点记录和想法清单两份文件。把这一周最有意思的一个结果记进亮点记录，把手头冒出、但还不该做的想法记进想法清单。运行记录的模板见[整理科研材料](../08_throughout/organizing_materials.md#3-每个结果都要能追溯到它是怎么来的)第 3 节。

## 4. 改了做法，要记下来、说出来

做着做着，你一定会改：换一种泄露定义、去掉一批数据、换一种评分方法。**改动本身没有问题，问题是悄悄地改。**

**为什么悄悄改是问题：**

- **反复看同一份测试数据，结论会变得不可信。** 这在机器学习研究里很常见：在同一份测试数据上试不同的模型和参数，直到结果好看[^lones2021avoid-e4]。测试数据用得越多次，对它的过拟合就越严重[^lones2021avoid-e5]，也就是结果只在这份数据上好看。
- **记忆靠不住。** 人会记错，会不自觉地往自己想要的方向推理，而且这些偏差常常发生在意识之外，光有好的意愿不够[^nosek2018preregistration-e3]。心理学的教训是：研究者反复换分析、直到结果"显著"，往往自己都没意识到，也不觉得这有什么后果[^nelson2018psychology-e8]。
- **偏离计划很常见，说明了的却很少。** 一项研究抽查了政治学和经济学两个登记平台上 2011–2016 年登记的 195 份预分析计划（看结果之前写下的分析计划）[^ofosu2023preanalysis-e1]：在这个样本里出现了 14 处偏离计划的情形，只有 1 处注明了改动[^ofosu2023preanalysis-e7]。这是两个学科早期的情况，不代表所有学科。

**怎么做：**

1. **评估用的数据一开始就划出来，留到最后**（机器学习的做法）。项目一开始就划出一份独立的测试数据，只在项目最后用一次，评估最终的那一个模型[^lones2021avoid-e3]。平时调判定规则、调解析脚本，用另一份开发数据。
2. **每次改动，在计划的改动记录里写一行：** 改了什么、为什么改、改之前已经看到了哪些结果。改动记录的写法见[形成研究计划](03_research-plan.md#7-计划怎样改)第 7 节。
3. **分清哪些分析是事先定好的，哪些是看了结果之后才想到的。** 事后的探索不比事先的预测低一等，要做的是让人分得清哪个是哪个[^nosek2018preregistration-e4]。
4. **改了，就如实报告改了什么、为什么改。** 即使中途偏离了事先登记的计划，登记了计划再如实说明偏差，仍然比完全不登记可信得多[^nosek2018preregistration-e5]。
5. **大的改动先告诉导师，**比如换评测集、换核心指标、去掉一批数据。

**适用范围**：第 1 步是机器学习等用数据集评估方法的研究里的做法；第 2–5 步各学科都适用。"事先登记分析计划"在政治学、经济学已有专门的登记平台[^ofosu2023preanalysis-e1]，更多见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)。结论能说到哪里，见[效度与局限](04_validity-and-limits.md)。

**写下来：** 翻一下最近两周的日志，列出你做过的所有改动。每条补上"为什么改"和"改之前看到了什么结果"。有没有哪条是你没打算告诉导师的？

## 5. 卡住时，按固定步骤排查

在大多数研究项目里，绝大部分时候实验都是不成功的[^huang2023unstuck-e1]。每个人都会卡住、灰心[^dredze2012successful-e4]。要紧的是手里有一套办法。

**依次试这些：**

1. **把失败说具体。** 不要只说"不行"。写下输入是什么、预期结果是什么、实际结果是什么[^huang2023unstuck-e2]；问题已经缩小到哪一步[^freeman2013research-e3]。
2. **把问题简化，直到它一定能成功。** 一步步把任务变简单，简单到它必然"成功"[^huang2023unstuck-e3]；问一句"有没有更简单的情形能做通"[^freeman2013research-e6]。做通之后，再一样一样加回难度。
3. **先假装知道一部分。** 给自己额外的信息，是推进的一个有力办法[^huang2023unstuck-e4]。例如泄露比对一直匹配不上，先拿几份你确定是照抄来的合约去比：能匹配上，问题在别的合约身上；匹配不上，问题在比对方法本身。
4. **追问为什么失败。** 每次不成功都问为什么，避免再试那些会因同样原因失败的做法[^steinhardt2018stochastic-e9]。有人花了几个月试各种办法，最后才发现它们都因同一个原因失败[^steinhardt2018stochastic-e21]。
5. **检查想法本身。** 代码和实验都查过还是不行，就退一步检查想法[^huang2023unstuck-e5]。
6. **换一种问题的说法。** 死守问题的某一种说法是常见错误；找到一个相关的问题，或换个说法让自己能往前走，也是进展[^nielsen2004principles-e4]。
7. **还是没头绪，就定 5 分钟计时，列出所有能做的事**[^nanda2025mindsets-e5]；然后找人讨论。问其他研究者，尤其是导师，能给你新的角度[^nanda2025mindsets-e16]。发现自己进展慢，就及时、坦然地求助[^perez2024tips-e7]。

**进展不只是"做成了"。** 说明了为什么不行、为了弄懂问题花时间读书，都算进展[^freeman2013research-e7]。只要你在了解这个问题，实验没"成功"也是收获[^perez2024tips-e1]。

**写下来：** 对你现在卡住的地方，写出"输入 / 预期 / 实际"三行，再写出你已经排除了哪些原因。写完后，选上面的一步去试。

## 6. 坚持，还是换方向

难点在于：有的想法只是一个细节错了才看不到效果，有的则怎么做都注定失败[^schulman2020opinionated-e19]，而两者很难分辨。

**判断时注意：**

- **一次失败不等于想法失败。** 你试的只是这个思路的一种实现，而不是整个思路[^steinhardt2018stochastic-e10]。"看起来不行""试了几次没劲了"都不算排除了它[^steinhardt2018stochastic-e22]，要能说出它为什么注定不行。
- **换得太勤比换得太少更常见**[^schulman2020opinionated-e13]。新想法的初步结果多半同样令人失望，也要持续努力才能出结果[^schulman2020opinionated-e20]。总在切换、什么都没好好探索，就什么也学不到[^nanda2025mindsets-e1]。
- **该停的信号：** 你在反复降低目标和期望[^dredze2012successful-e5]；或者项目的收益明显递减，这时换项目完全没问题[^perez2024tips-e2]。不太有希望的方向，必要时要果断放下[^nanda2025mindsets-e1]。
- **认清自己的毛病。** 有人钻进牛角尖出不来，有人想得太多、迟迟不动手，等一个不存在的完美时机[^nanda2025mindsets-e9]。看自己偏哪一种，就多用针对它的那条建议。
- **给新想法留一份固定的时间。** 拿出一份固定的时间预算，试那些偏离主线的新想法[^schulman2020opinionated-e21]，主线照常推进。

"换方向"有大有小。先从最小的改起：

| 改什么 | 什么时候 | 例子 |
|---|---|---|
| 换一种实现 | 想法本身还没被否定，只是这种做法不行 | 泄露比对从"完全相同"换成"高度相似" |
| 改主张 | 证据只撑得住一个更小或不同的结论 | "评测结果被泄露高估"改成"在重入漏洞上，评测结果被泄露高估" |
| 换问题 | 能说出这个想法为什么注定不行 | 回到[收敛成项目](../01_find-a-problem/05_converge.md)，换一个候选结论 |

改主张或换问题，都要同时改计划，并告诉导师（见第 4 节、第 7 节）。

要不要同时做两个项目、一个碰壁时转去另一个，见[计划与日常节奏](../08_throughout/planning_and_routines.md#6-同时有几个项目时)。

**写下来：** 对你最犹豫的那个方向，写出"它注定不行的理由"。写不出具体理由，就先别放弃，写出下一个最便宜的试法；写得出，就按上表决定改哪一层。

## 7. 向导师汇报进展

**导师想听进展，而且"进展"的含义可以很宽**：有导师明确说，自己喜欢在见面时听到进展，对进展的理解也很宽[^freeman2013research-e9]。说明了为什么不行，也是进展（第 5 节）。

**怎么做：**

- **平时就经常把结果发给导师**，不要攒到见面时一次拿出来[^huang2023advisor-e2]。导师在会上才第一次看到结果，就没有时间理解和思考它们[^huang2023advisor-e1]。
- **定期见面，**比如每周一次，尤其是你不想见的时候[^dredze2012successful-e11]。每次尽量带上结果，比如图和表[^dredze2012successful-e13]。
- **先给总结。** 导师手上有很多项目，不像你一整周只做这一个，需要时间切换过来[^dredze2012successful-e14]。开场先说上次约定做什么、结论是什么，细节放后面[^huang2023advisor-e4]。
- **把结果放进上下文里讲**[^huang2023advisor-e5]：做了什么、为什么做、发现了什么、和预期是否一致。
- **给出你建议的下一步。** 展示结果后，紧接着提出下一步的几种可能和你排的优先级[^perez2024tips-e6]，并说明理由[^huang2023advisor-e6]。
- **让人看得到，不只是说。** 只用嘴描述你做了什么，别人很难完全理解[^huang2023unstuck-e8]。导师有经验也愿意帮你，但你要帮导师帮到你[^huang2023unstuck-e7]。
- **把问题说出来。** 遇到的问题要坦白说[^perez2024tips-e8]；卡住了不要躲着导师，主动找导师谈[^freeman2013research-e10]；觉得赶不上截止日期，一定要说，导师宁可早点知道[^dredze2012successful-e20]。
- **导师建议的做法不行时，**先按导师说的做，发现不行，就在原方案附近找找什么做法行得通，再把它汇报回去[^freeman2013research-e8]。你对这个具体问题了解得比导师多，有时足以做出更好的判断[^nanda2025mindsets-e15]。

**一份周报的样子**：

> **上周约定：** 在开发集上比较三个模型在泄露样本和未泄露样本上的检出率。
>
> **结论：** 按"高度相似"的定义，200 个开发集合约里找到 38 个泄露样本；三个模型在泄露样本上的检出率都更高，差 9 到 15 个百分点（附表）。
>
> **改动：** 去掉了 12 个无法编译的合约（原因见日志）。
>
> **卡在：** 泄露样本平均只有未泄露样本一半长，差距可能有一部分来自难度。已排除：解析脚本出错。
>
> **建议下一步：** ① 按长度和漏洞类型配对，再比一次（最优先，因为它决定结论能不能成立）；② 再加一个评测集。
>
> **需要您决定：** 配不上对的样本是去掉，还是单独报告？

会后，把商定的下一步写下来发给导师[^huang2023advisor-e7]。和导师日常的配合，见[合作与导师](../08_throughout/collaboration_and_advisors.md)。

**写下来：** 按上面的格式，写出你这周的周报。"改动"和"卡在"两栏不要空着不写；真的没有，就写"无"。

## 8. 定期抬头看路

除了埋头做，还要定期退一步，确认自己在做对的事[^freeman2013research-e5]。排优先级和执行是两种不同的状态，不要同时做[^nanda2025mindsets-e6]。

**每周留出一段时间回顾**[^nanda2025mindsets-e7]，问自己几个问题：最近什么最花时间？什么挡住了我？犯了什么错，怎样改变做法才能不再犯[^nanda2025mindsets-e8]？我们再加一个：**这一周拿到的东西，离计划里下一个里程碑的"做完"还差什么？** 差得越来越多，就要考虑第 6 节说的改主张。

大多数时候，动起来比停着好，前提是经常留出时间反思目标[^nielsen2004principles-e3]。每周回顾的完整做法和日常时间安排，见[计划与日常节奏](../08_throughout/planning_and_routines.md)。

**可持续地做下去。** 很多研究者因为工作方式不可持续而倦怠[^perez2024tips-e5]。休息通常会让有效工作时间净增加[^nanda2025process-e7]。更多见[心态与长期积累](../08_throughout/mindset_and_growth.md)。

**写下来：** 在日历上定一个每周固定的回顾时间。第一次回顾时，回答上面四个问题，各写一两句。

## 9. 不同套路，执行时的重点不同

上面的做法对各种研究都适用。不同的[研究套路](../00_start-here/key-concepts.md#研究套路)执行时还各有重点，比如构建改进要一样一样加改动、留着每一步的版本，综合要记下每篇论文为什么收、为什么不收。每种套路的重点见对应套路篇第 4 节"它怎样影响整个项目"：[观察描述](../05_research-strategies/observe_describe.md)、[测量](../05_research-strategies/measure.md)、[比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md)、[综合](../05_research-strategies/synthesize.md)、[证明](../05_research-strategies/prove.md)。

**写下来：** 打开你的主要套路那一篇，找到第 4 节里讲执行的那一行或那一段，把它改写成一条每次运行都要核对的检查项，加进你的运行记录模板。

---

## 关键判断

**这个改动，要不要记、要不要说？**

| 改动 | 记进日志 | 记进计划的改动记录 | 先告诉导师 |
|---|---|---|---|
| 修了一个程序错误 | 要 | 如果它影响了已有结果，要 | 影响已有结论时要 |
| 调了解析脚本、调了参数 | 要 | 不必 | 周报里说 |
| 去掉或加入一批数据 | 要 | 要 | 要 |
| 换评测集、换核心指标 | 要 | 要 | 要，而且先说再改 |
| 改主张、换问题 | 要 | 要 | 要，而且一起商量 |

**再试一次，还是换？** 能说出"为什么注定不行"之前，换实现，不换想法；能说出来，按第 6 节的表，从最小的一层改起。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 一上来就做又大又慢的完整实验 | 几周后才看到第一个信号；快而粗糙的实验能更早告诉你方向对不对[^nanda2025mindsets-e11] |
| 一次改好几个地方 | 结果变了，不知道是哪个改动造成的[^freeman2013research-e2] |
| 结果文件不记来源 | 一年后自己都重现不了[^sandve2013ten-e2] |
| 在测试数据上反复调，直到结果好看 | 用得越多次，过拟合越严重[^lones2021avoid-e5] |
| 悄悄去掉数据、换指标 | 在一个政治学和经济学的样本里，14 处偏离计划只有 1 处注明了[^ofosu2023preanalysis-e7]（见第 4 节）；这意味着，读者无从判断结论还剩多少可信 |
| 向导师汇报"不行" | 导师无从帮你；要说清预期、实际结果和问题缩小到了哪一步[^freeman2013research-e3][^huang2023unstuck-e2] |
| 一次失败就放弃整个思路 | 失败的只是一种实现[^steinhardt2018stochastic-e10] |
| 一碰到困难就换新想法 | 留下一堆半成品，新想法多半同样艰难[^schulman2020opinionated-e18][^schulman2020opinionated-e20] |
| 卡住了躲着导师 | 问题越拖越大；导师宁可早点知道[^freeman2013research-e10][^dredze2012successful-e20] |

## 产出物

- 研究日志，以及每一两周一次的回顾总结（第 3 节）
- 运行记录：每个结果都能追到代码、数据、参数和输出位置（第 3 节）
- 计划的改动记录，写明每个改动的原因（第 4 节）
- 每周的周报和会后纪要（第 7 节）
- 想法清单和亮点记录（第 3 节）

## 检查点

满足下面几条，可以进入分析阶段：

- [ ] 计划里每个里程碑要的证据都已经拿到，或者已经和导师商定改了主张
- [ ] 每个要进论文的结果，都能说出它用的代码版本、数据版本、参数和输出位置
- [ ] 最终评估用的测试数据，只在最后用过一次，或者用了几次你都记下了
- [ ] 所有偏离计划的改动都在改动记录里，导师知道其中的大改动
- [ ] 能用一句话说出现在的结果支持什么、不支持什么
- [ ] 导师看过主要结果，同意可以开始系统分析

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 不知道该坚持、调整还是退回 | [决策点：继续、调整，还是退回](08_decision-points.md#2-一张总表什么时候看到什么怎么选)，查"正式执行中，卡住了"和"做了很久，没有进展"两行 |
| 一直写不出具体的假设，探索了很久没有收获 | [动手探索](../01_find-a-problem/03_explore.md)或[收敛成项目](../01_find-a-problem/05_converge.md)，重新想要证明哪句话 |
| 卡住的原因是设计本身：拿到的数据回答不了研究问题 | [从研究问题到证据清单](01_question-to-evidence.md) |
| 某个关键部分被证明做不成，而它当初没有试过 | [最小可跑版本](05_pilot-and-derisk.md)，把剩下的风险都先试一遍 |
| 改动多到原来的计划已经对不上 | [形成研究计划](03_research-plan.md#7-计划怎样改)第 7 节，从主张开始重改计划 |
| 想换的不是做法，而是问题本身 | [收敛成项目](../01_find-a-problem/05_converge.md)，和导师一起重写一页简介 |

## 下一步

证据拿到以后，下一步是系统地分析它们：结果说明了什么、不说明什么、怎样排除别的解释。见[分析与解读](07_analyze-and-interpret.md)。

[^carlini2022rapid-e1]: Carlini 2022，开头段。[证据](../../sources/notes/carlini2022rapid.md#e1)
[^carlini2022rapid-e2]: Carlini 2022，"(Machine learning) research does not support rapid iteration" 一节。[证据](../../sources/notes/carlini2022rapid.md#e2)
[^carlini2022rapid-e3]: Carlini 2022，同上。[证据](../../sources/notes/carlini2022rapid.md#e3)
[^carlini2024logfile-e2]: Carlini 2024，A bit more detail。[证据](../../sources/notes/carlini2024logfile.md#e2)
[^carlini2024logfile-e3]: Carlini 2024，A bit more detail。[证据](../../sources/notes/carlini2024logfile.md#e3)
[^dredze2012successful-e2]: Dredze & Wallach 2012（v1.2），#18，第 4 页。[证据](../../sources/notes/dredze2012successful.md#e2)
[^dredze2012successful-e4]: Dredze & Wallach 2012（v1.2），#21，第 4 页。[证据](../../sources/notes/dredze2012successful.md#e4)
[^dredze2012successful-e5]: Dredze & Wallach 2012（v1.2），#34，第 6 页。[证据](../../sources/notes/dredze2012successful.md#e5)
[^dredze2012successful-e11]: Dredze & Wallach 2012（v1.2），#8，第 3 页。[证据](../../sources/notes/dredze2012successful.md#e11)
[^dredze2012successful-e13]: Dredze & Wallach 2012（v1.2），#10，第 3 页。[证据](../../sources/notes/dredze2012successful.md#e13)
[^dredze2012successful-e14]: Dredze & Wallach 2012（v1.2），#11，第 3 页。[证据](../../sources/notes/dredze2012successful.md#e14)
[^dredze2012successful-e20]: Dredze & Wallach 2012（v1.2），#45，第 8 页。[证据](../../sources/notes/dredze2012successful.md#e20)
[^freeman2013research-e1]: Freeman 2013，第 1 页。[证据](../../sources/notes/freeman2013research.md#e1)
[^freeman2013research-e2]: Freeman 2013，第 1 页。[证据](../../sources/notes/freeman2013research.md#e2)
[^freeman2013research-e3]: Freeman 2013，第 1 页。[证据](../../sources/notes/freeman2013research.md#e3)
[^freeman2013research-e4]: Freeman 2013，第 1 页。[证据](../../sources/notes/freeman2013research.md#e4)
[^freeman2013research-e5]: Freeman 2013，第 1 页。[证据](../../sources/notes/freeman2013research.md#e5)
[^freeman2013research-e6]: Freeman 2013，第 3 页。[证据](../../sources/notes/freeman2013research.md#e6)
[^freeman2013research-e7]: Freeman 2013，第 3 页。[证据](../../sources/notes/freeman2013research.md#e7)
[^freeman2013research-e8]: Freeman 2013，第 2 页。[证据](../../sources/notes/freeman2013research.md#e8)
[^freeman2013research-e9]: Freeman 2013，第 3 页。[证据](../../sources/notes/freeman2013research.md#e9)
[^freeman2013research-e10]: Freeman 2013，第 3 页。[证据](../../sources/notes/freeman2013research.md#e10)
[^huang2023advisor-e1]: Jia-Bin Huang 2023，推文串 [How to meet with your advisors/mentors?](https://twitter.com/jbhuang0604/status/1653614931202195458)，Present results。[证据](../../sources/notes/huang2023advisor.md#e1)
[^huang2023advisor-e2]: Jia-Bin Huang 2023，推文串，Present results。[证据](../../sources/notes/huang2023advisor.md#e2)
[^huang2023advisor-e4]: Jia-Bin Huang 2023，推文串，Start with a summary。[证据](../../sources/notes/huang2023advisor.md#e4)
[^huang2023advisor-e5]: Jia-Bin Huang 2023，推文串，Interpret your results。[证据](../../sources/notes/huang2023advisor.md#e5)
[^huang2023advisor-e6]: Jia-Bin Huang 2023，推文串，Propose next steps。[证据](../../sources/notes/huang2023advisor.md#e6)
[^huang2023advisor-e7]: Jia-Bin Huang 2023，推文串，Summarize your meeting。[证据](../../sources/notes/huang2023advisor.md#e7)
[^huang2023unstuck-e1]: Jia-Bin Huang 2023，推文串 [How to get unstuck?](https://twitter.com/jbhuang0604/status/1717381151508054029)，第 1 条。[证据](../../sources/notes/huang2023unstuck.md#e1)
[^huang2023unstuck-e2]: Jia-Bin Huang 2023，推文串，Show HOW it failed。[证据](../../sources/notes/huang2023unstuck.md#e2)
[^huang2023unstuck-e3]: Jia-Bin Huang 2023，推文串，Simplify the tasks until it works。[证据](../../sources/notes/huang2023unstuck.md#e3)
[^huang2023unstuck-e4]: Jia-Bin Huang 2023，推文串，Introduce privileged information。[证据](../../sources/notes/huang2023unstuck.md#e4)
[^huang2023unstuck-e5]: Jia-Bin Huang 2023，推文串，Debug the idea。[证据](../../sources/notes/huang2023unstuck.md#e5)
[^huang2023unstuck-e6]: Jia-Bin Huang 2023，推文串，Iterate fast。[证据](../../sources/notes/huang2023unstuck.md#e6)
[^huang2023unstuck-e7]: Jia-Bin Huang 2023，推文串，Help your mentors help you。[证据](../../sources/notes/huang2023unstuck.md#e7)
[^huang2023unstuck-e8]: Jia-Bin Huang 2023，推文串，Make your experiments easy to understand。[证据](../../sources/notes/huang2023unstuck.md#e8)
[^lones2021avoid-e3]: Lones 2021，§3.1，第 8 页。[证据](../../sources/notes/lones2021avoid.md#e3)
[^lones2021avoid-e4]: Lones 2021，§4.3，第 15 页。[证据](../../sources/notes/lones2021avoid.md#e4)
[^lones2021avoid-e5]: Lones 2021，§4.3，第 15 页。[证据](../../sources/notes/lones2021avoid.md#e5)
[^nanda2025mindsets-e1]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e1)
[^nanda2025mindsets-e5]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e5)
[^nanda2025mindsets-e6]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e6)
[^nanda2025mindsets-e7]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e7)
[^nanda2025mindsets-e8]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e8)
[^nanda2025mindsets-e9]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e9)
[^nanda2025mindsets-e10]: Nanda 2025b，Moving Fast。[证据](../../sources/notes/nanda2025mindsets.md#e10)
[^nanda2025mindsets-e11]: Nanda 2025b，Moving Fast。[证据](../../sources/notes/nanda2025mindsets.md#e11)
[^nanda2025mindsets-e14]: Nanda 2025b，Moving Fast。[证据](../../sources/notes/nanda2025mindsets.md#e14)
[^nanda2025mindsets-e15]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e15)
[^nanda2025mindsets-e16]: Nanda 2025b，Truth Seeking。[证据](../../sources/notes/nanda2025mindsets.md#e16)
[^nanda2025process-e4]: Nanda 2025a，Exploration (Stage 2)。[证据](../../sources/notes/nanda2025process.md#e4)
[^nanda2025process-e6]: Nanda 2025a，Distillation (Stage 4)。[证据](../../sources/notes/nanda2025process.md#e6)
[^nanda2025process-e7]: Nanda 2025a，Introduction。[证据](../../sources/notes/nanda2025process.md#e7)
[^nelson2018psychology-e8]: Nelson 等人 2018，False Positives Are Bad，第 518 页。[证据](../../sources/notes/nelson2018psychology.md#e8)
[^nielsen2004principles-e3]: Nielsen 2004，The skills of the problem-solver。[证据](../../sources/notes/nielsen2004principles.md#e3)
[^nielsen2004principles-e4]: Nielsen 2004，The skills of the problem-solver。[证据](../../sources/notes/nielsen2004principles.md#e4)
[^nosek2018preregistration-e3]: Nosek 等人 2018，Mental Constraints on Distinguishing Predictions and Postdictions。[证据](../../sources/notes/nosek2018preregistration.md#e3)
[^nosek2018preregistration-e4]: Nosek 等人 2018，Preregistration Distinguishes Prediction and Postdiction。[证据](../../sources/notes/nosek2018preregistration.md#e4)
[^nosek2018preregistration-e5]: Nosek 等人 2018，Challenge 1: Changes to Procedure During Study Administration。[证据](../../sources/notes/nosek2018preregistration.md#e5)
[^ofosu2023preanalysis-e1]: Ofosu & Posner 2023，摘要。[证据](../../sources/notes/ofosu2023preanalysis.md#e1)
[^ofosu2023preanalysis-e7]: Ofosu & Posner 2023，Do PAPs Reduce the Scope for Fishing?。[证据](../../sources/notes/ofosu2023preanalysis.md#e7)
[^perez2024tips-e1]: Perez 2024，General Mindset Tips。[证据](../../sources/notes/perez2024tips.md#e1)
[^perez2024tips-e2]: Perez 2024，General Mindset Tips。[证据](../../sources/notes/perez2024tips.md#e2)
[^perez2024tips-e3]: Perez 2024，Three modes of research。[证据](../../sources/notes/perez2024tips.md#e3)
[^perez2024tips-e5]: Perez 2024，Work Habits。[证据](../../sources/notes/perez2024tips.md#e5)
[^perez2024tips-e6]: Perez 2024，Tactical Research Tips & Approach。[证据](../../sources/notes/perez2024tips.md#e6)
[^perez2024tips-e7]: Perez 2024，What success generally looks like。[证据](../../sources/notes/perez2024tips.md#e7)
[^perez2024tips-e8]: Perez 2024，What success generally looks like。[证据](../../sources/notes/perez2024tips.md#e8)
[^sandve2013ten-e2]: Sandve 等人 2013，Rule 1。[证据](../../sources/notes/sandve2013ten.md#e2)
[^sandve2013ten-e7]: Sandve 等人 2013，Rule 1。[证据](../../sources/notes/sandve2013ten.md#e7)
[^schulman2020opinionated-e13]: Schulman 2020，When to Switch Problems。[证据](../../sources/notes/schulman2020opinionated.md#e13)
[^schulman2020opinionated-e16]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e17)
[^schulman2020opinionated-e18]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e18)
[^schulman2020opinionated-e19]: Schulman 2020，When to Switch Problems。[证据](../../sources/notes/schulman2020opinionated.md#e19)
[^schulman2020opinionated-e20]: Schulman 2020，When to Switch Problems。[证据](../../sources/notes/schulman2020opinionated.md#e20)
[^schulman2020opinionated-e21]: Schulman 2020，When to Switch Problems。[证据](../../sources/notes/schulman2020opinionated.md#e21)
[^steinhardt2018stochastic-e9]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e9)
[^steinhardt2018stochastic-e10]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e21]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e21)
[^steinhardt2018stochastic-e22]: Steinhardt 2018，Additional Discussion。[证据](../../sources/notes/steinhardt2018stochastic.md#e22)
