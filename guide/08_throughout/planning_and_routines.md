# 计划与日常节奏

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本页的道理适用于各学科，例子和具体做法以计算机为例。本页引用的资料，大多是计算机、机器学习研究者写的个人经验文章，只有一项是实验研究。把它们当作可以试一试的建议，不是对所有研究者都成立的规律；试过以后，按你自己的日志调整。`[本项目分析]`

## 什么时候需要这一页

你已经有了一份研究计划，可每天坐下来还是不知道先干什么，一周过去说不清项目往前走了多少；或者时间被会议和消息切得粉碎，手上压着两三个项目，计划写好一个月就没再打开过。

这一页讲怎样让计划落到每天、每周、每月的时间上。计划本身怎么做（终点、里程碑、"做完"的标准、排序、估时），见[形成研究计划](../01_from-interest-to-project/04_research-plan.md)，这里不重复。

---

## 1. 每天：开工先定今天的目标，收工前写"下一步"

**怎么做：**

- **开工时，先读日志的最后一条，再写下今天的目标。** 今天的目标是研究计划里分层目标的最下面一层（以天计，见[形成研究计划第 5 节](../01_from-interest-to-project/04_research-plan.md#5-估时间并把余量留出来)）。写的是：今天结束时，手里要多出什么。例如"把 50 个样本里的前 20 个人工核对完，记下判断不一致的原因"，而不是"做泄露检测" `[本项目分析]`。
- **边做边记研究日志。** 每天记下想法和实验[^schulman2020opinionated-e16]；顺手记下每件事预估多久、实际用了多久，每周回顾时要用（见第 4 节）。日志怎么写、和其他笔记怎么分工，见[整理科研材料第 5 节](organizing_materials.md#5-分清三种笔记)和[执行与迭代第 3 节](../03_conduct-and-analyze/01_run-and-iterate.md#3-每次运行都留下记录)。
- **新冒出的想法，记进想法清单，然后回到手上的事**[^carlini2024logfile-e2]。
- **收工前写一行"下一步"**：今天停在了哪里，明天第一件要做的事是什么。第二天开工时，这一行就是你要读的"最后一条" `[本项目分析]`。

**为什么：** `[本项目分析]` 日志是后面所有回顾的原料。没有每天的记录，每周回顾只能凭记忆，而记忆偏向最近的、最顺利的事。"下一步"这一行让你第二天不用花半小时回想昨天做到哪里。

**容易错在哪：** `[本项目分析]`

- 只记"做了什么"，不记"看到了什么、怎么理解"。几周后你只知道跑过一个实验，不知道它说明了什么。
- 每天的目标写成活动，如"看代码""调参"。做了一整天，说不清算不算完成。

**写下来：** 明天开工时，用一句话写下"今天结束时手里要多出什么"；收工前，写一行"下一步"。

## 2. 每周留出整块时间，给最难的事

**怎么做：**

1. **先看清时间去了哪里。** 有人如实记下自己每天的时间，吃惊地发现：扣除打断、邮件、上网、电话、没有结果的会议和闲聊之后，他每天平均只做了半小时研究[^nielsen2004principles-e2]。觉得时间和产出对不上时，做一次时间记录[^dredze2012successful-e1]：记下时间花在哪里，再回头想下次怎样能更快[^nanda2025mindsets-e13]。
2. **在日历上划出整块的时间。** 日历把时间变成看得见的格子，让你看清时间是有限的[^parikh2018calendar-e1]。先把一周里你最清醒的几个半天划出来，留给最需要连续思考的事：推公式、设计实验、写论文的核心部分 `[本项目分析]`。
3. **整块时间里只做一件事，并且事先拆好。** 事先把它拆成小步骤（拆多细，见[形成研究计划第 5 节](../01_from-interest-to-project/04_research-plan.md#5-估时间并把余量留出来)），整块时间一开始就知道先做哪一步，不用临场想 `[本项目分析]`。
4. **把零碎的事集中放。** 回邮件、看消息、填表、改格式，放进整块时间之外的零碎时段 `[本项目分析]`。

**为什么：** "半天"这个单位来自一篇随笔。作者 Paul Graham 是程序员出身的创业者和投资人，他说写程序、写文章的人通常喜欢以至少半天为单位安排时间，一小时只够起个头[^graham2009makers-e1]。一个会议就能毁掉整个下午：它把下午切成两段，每段都太短，做不了难的事[^graham2009makers-e2]。影响还会往前传：他知道下午会被打断，上午就不太愿意开始有挑战的事[^graham2009makers-e3]。

**适用范围：** 这是一个人的经验，不是对研究者的调查。研究工作的整块时间要多长才够，本页资料没有涉及；先试半天，再按你自己的日志调整 `[本项目分析]`。

**容易错在哪：** 一开始就把整周排满整块时间，结果被会议和课程挤掉一半，几周后干脆不排了。从每周两三个半天开始，守得住比排得多更有用 `[本项目分析]`。

**写下来：** 打开下周的日历，划出两三个半天，每个写上要做的那一件事。

## 3. 应对打断：先记下，再回来

被打断是常态：导师找你，合作者发消息，服务器出了问题，临时加了课。你能做的是减少不必要的打断，并让每次打断的代价小一点。

**怎么做：** `[本项目分析]`

| 打断的来源 | 做法 |
|---|---|
| 突然冒出的新想法 | 写进想法清单，回到手上的事[^carlini2024logfile-e2] |
| 消息和邮件 | 整块时间里关掉提醒，在固定的零碎时段集中处理 |
| 会议和讨论 | 尽量排在一天的开头或末尾，不放进整块时间的中间。Graham 把见人的时段集中在工作日末尾，这些会议就不会打断他的工作[^graham2009makers-e4] |
| 必须马上处理的急事 | 停下前花一分钟，在日志里写下做到哪里、下一步是什么；回来时从这一行接着做 |
| 几天以上的大打断（生病、出差、考试周） | 回来后先重排本周计划，不要硬按原计划赶。重新排期是计划的一部分，不是失败[^parikh2018calendar-e3] |

**为什么：** 有一项实验室研究，在模拟的办公环境里让 48 名参与者回复电子邮件，每两分钟打断一次[^mark2008cost-e2]。被打断时他们完成得反而更快，质量也没有差别；但这是靠加快速度补偿的，代价是更大的压力、挫败感、时间紧迫感和付出的努力[^mark2008cost-e1]。只这样工作了 20 分钟，这些感受就明显上升[^mark2008cost-e3]。打断的内容和手头的事是否相关，结果都一样[^mark2008cost-e4]。

要注意：这项研究的任务是回邮件，不是研究工作，时间也只有几十分钟。需要长时间连续思考的研究被打断，代价是更大还是更小，本页资料没有涉及。

**容易错在哪：** 为了不被打断，把自己完全关起来。开着门工作会被打扰，但也会不时得到"什么可能重要"的线索[^hamming1986you-e18]。要守住的是整块时间，而不是拒绝所有交流 `[本项目分析]`。为什么不要一个人闷头干，见[心态与长期积累第 5 节](mindset_and_growth.md#5-别一个人闷头干)。

**写下来：** 列出上周打断你最多的三件事，每件写一个下周要试的做法。

## 4. 每周回顾：停下来，拉远看一次

每周回顾把每天的日志和整个项目的计划连起来。排优先级和执行是两种不同的思考状态，不该同时进行[^nanda2025mindsets-e6]；每周回顾就是专门留给排优先级的时间，平时就可以放心埋头执行 `[本项目分析]`。

**怎么做：** 每周固定一个时间（例如周五下午的最后一小时），按下面五步走 `[本项目分析]`：

1. **读这周的日志，压缩成几行总结**：发现了什么，有什么新理解，完成了什么，下一步做什么。有人每一两周做一次这样的回顾，把所有日常记录读一遍，压缩成一份总结[^schulman2020opinionated-e17]。
2. **回答证据方面的问题**（对照研究计划和论文提纲）：
   - 离下一个里程碑的"做完"还差什么？
   - 哪些主张更有把握了，哪些变弱了？
   - 下一步做什么？按"单位时间能得到多少信息"从高到低排[^steinhardt2018stochastic-e4]。
3. **回答时间方面的问题**[^nanda2025mindsets-e8]：
   - 最近什么最花时间？
   - 什么卡住了我？
   - 犯了什么错，怎样系统地调整做法，避免以后再犯？
4. **排下周。** 对比本周的预估用时和实际用时，算出"实际 / 预估"的倍数[^parikh2018calendar-e2]；把下周的事拆成小块，按倍数估好时间，放进日历的空位。估时偏差怎么测、怎么用，见[形成研究计划第 5 节](../01_from-interest-to-project/04_research-plan.md#5-估时间并把余量留出来)。
5. **把总结带给导师。** 和导师见面时用这份总结开头；觉得某个里程碑赶不上了，尽早说。怎么开会、怎么报坏消息，见[导师与合作第 3 节](collaboration_and_advisors.md#3-尽早汇报进展包括坏消息)。

**为什么：** 每周回顾可以非常有用：拉远看一看整体进展和眼下的问题[^nanda2025mindsets-e7]。不回顾，你会一直在执行，却不知道执行的是不是最该做的事 `[本项目分析]`。

**容易错在哪：** `[本项目分析]`

- 只回顾"这周做了多少事、花了多少时间"。时间是辅助，重心是证据：离完成标准还差什么。
- 回顾完什么都没改。回顾的产出应该是改过的下周日程，必要时还有改过的计划。

**写下来：** 把上面五步抄成一份模板，这周用它做第一次回顾。

## 5. 每月：让计划活着

研究计划写好以后，最常见的结局不是被推翻，而是被遗忘：每天忙着跑实验，几个月没再打开它 `[本项目分析]`。

**怎么做：** 每月一次，在当周的回顾之外多花一两个小时 `[本项目分析]`：

- **重读一页简介和研究计划。** 核心主张还是那一句吗？哪个里程碑超出了余量？要改，就按[形成研究计划第 7 节](../01_from-interest-to-project/04_research-plan.md#7-计划怎样改)的顺序：先看主张，再看里程碑，最后才看时间。
- **把这个月的周总结连起来读。** 回看几个月，你可能发现自己一直在想法之间跳来跳去，留下几个半成品，哪条线都没跟到出结果[^schulman2020opinionated-e18]。
- **留一点时间想大问题。** 不只想眼前的里程碑，也想想你的领域里什么重要，见[心态与长期积累第 4 节](mindset_and_growth.md#4-留出时间想重要的问题并敢于开始)。
- **找人帮你守住节奏。** 每月把计划的变化发给导师或合作者。为什么对别人负责能帮你自律，见[导师与合作第 5 节](collaboration_and_advisors.md#5-和同伴组外的人合作)。

**为什么：** 大多数时候动起来比停着好，前提是经常留出时间反思和重新审视目标[^nielsen2004principles-e3]。计划为什么一定会变，见[形成研究计划第 7 节](../01_from-interest-to-project/04_research-plan.md#7-计划怎样改)。

**容易错在哪：** 每月只把落后的日期往后挪。只改日期、不改内容，说明你没有回答"为什么落后"，计划很快就会和实际脱节 `[本项目分析]`。

**写下来：** 在日历上每月最后一周选一天，写上"月度回顾"，并把这一节的四件事列在下面。

## 6. 同时有几个项目时

读研究生一两年后，你很可能同时有一个主项目、一个合作项目和一些零碎的任务。

**怎么做：**

- **分清主次。** 主项目拿走大部分整块时间；副项目用等待的时间：等实验跑完、等数据、等别人回复 `[本项目分析]`。
- **按天切换，不按小时切换。** 为减少来回切换，有人一般每天只做一个项目[^ruder2020tips-e2]。
- **每个项目各有一份日志和一行"下一步"**，每周回顾时逐个过一遍 `[本项目分析]`。
- **给新想法定预算。** 有人建议给偏离主线的新想法留一份固定的时间预算[^schulman2020opinionated-e21]，主线照常推进 `[本项目分析]`。

**容易错在哪：** `[本项目分析]` 项目越开越多，每个都只推进一点；或者副项目慢慢占掉了主项目的整块时间。每周回顾时看一眼：主项目这周拿到了几个半天？

> **不同的看法：同时做一个项目还是两个？**
>
> - **赞成同时做两个**：一个项目碰壁时，可以转去做另一个，让自己不至于憋坏[^ruder2020tips-e1]。两个项目还可以一个稳妥、一个风险高但影响可能更大，稳妥的那个保证你能毕业[^ruder2020tips-e9]。这是作者自己的经验。
> - **提醒切换和分心的代价**：新想法总比做了几个月的旧想法显得更诱人，人很容易仅仅因为它新就分心[^carlini2026best-e15]。总在切换、什么都没好好探索，就什么也学不到[^nanda2025mindsets-e1]。回看几个月，可能只留下几个半成品[^schulman2020opinionated-e18]。这几位没有直接反对同时做两个项目，提醒的是项目一多就容易出现的问题。
>
> 实际操作中 `[本项目分析]`：新手先保证**一个主项目**能走完；主项目常常要等（等数据、等设备、等别人）时，再加一个小的副项目。月度回顾时，如果说不清两个项目各自往前走了多少，就先停掉一个。什么时候该放弃一个方向，见[执行与迭代第 6 节](../03_conduct-and-analyze/01_run-and-iterate.md#6-坚持还是换方向)。

**写下来：** 列出你手上所有的项目和任务，标出哪个是主项目，它每周拿到几个半天。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 每天的目标写成活动 | 做了一天，说不清算不算完成 `[本项目分析]` |
| 不记日志，回顾全凭记忆 | 看不出自己是不是在想法之间跳来跳去、留下一堆半成品[^schulman2020opinionated-e18] |
| 以为自己每天都在做研究 | 有人如实记录后发现，扣掉各种打断，每天只做了半小时研究[^nielsen2004principles-e2] |
| 把会议插在整块时间中间 | 一个会议就能把下午切成两段，每段都做不了难事[^graham2009makers-e2] |
| 一有新想法就去试 | 新想法常常只因为新才显得诱人[^carlini2026best-e15]；先记进想法清单[^carlini2024logfile-e2] |
| 一边排优先级一边执行 | 这是两种不同的思考状态，不该同时进行[^nanda2025mindsets-e6] |
| 按直觉估时间，从不对照实际 | 不知道自己的偏差；测出"实际 / 预估"的倍数要容易得多[^parikh2018calendar-e2] |
| 计划落后就只挪日期 | 没回答"为什么落后"，计划很快和实际脱节，见[形成研究计划第 7 节](../01_from-interest-to-project/04_research-plan.md#7-计划怎样改) `[本项目分析]` |
| 同时开很多项目，按小时切换 | 总在切换、什么都没好好探索，就什么也学不到[^nanda2025mindsets-e1]；有人每天只做一个项目来减少切换[^ruder2020tips-e2] |

## 延伸阅读

- **Schulman, "An Opinionated Guide to ML Research"**（2020）："Keep a Notebook, and Review It" 一节讲日志和每一两周一次的回顾。写给机器学习研究者。
- **Nanda, "My Research Process: Key Mindsets"**（2025）：Prioritisation 一节有三层目标和每周回顾的问题。写给机器学习研究者。
- **Parikh, "Calendar. Not to-do lists."**（2018）：时间总是不够、计划总落空时读。
- **Graham, "Maker's Schedule, Manager's Schedule"**（2009）：一页短文，创业者的随笔，讲为什么一个会议能毁掉一个下午，以及怎样把会议集中安排。
- **Carlini, "My research idea logfile, 2016-2019"**（2024）：想法清单的具体做法，附了作者几年的真实清单。
- **Nielsen, "Principles of Effective Research"**（2004）：Self-discipline 一节讲时间记录和对别人负责。

[^carlini2024logfile-e2]: Carlini 2024，A bit more detail。[证据](../../sources/notes/carlini2024logfile.md#e2)
[^carlini2026best-e15]: Carlini 2026，While doing the best-paper-worthy research › Re-prioritize projects ruthlessly。[证据](../../sources/notes/carlini2026best.md#e15)
[^dredze2012successful-e1]: Dredze & Wallach 2012（v1.2），#16，第 4 页。[证据](../../sources/notes/dredze2012successful.md#e1)
[^graham2009makers-e1]: Graham 2009，介绍两种日程的段落。[证据](../../sources/notes/graham2009makers.md#e1)
[^graham2009makers-e2]: Graham 2009，"meetings are a disaster" 一段。[证据](../../sources/notes/graham2009makers.md#e2)
[^graham2009makers-e3]: Graham 2009，"one meeting can sometimes affect a whole day" 一段。[证据](../../sources/notes/graham2009makers.md#e3)
[^graham2009makers-e4]: Graham 2009，"office hours" 一段。[证据](../../sources/notes/graham2009makers.md#e4)
[^hamming1986you-e18]: Hamming 1986，讲"door open / door closed"的部分。[证据](../../sources/notes/hamming1986you.md#e18)
[^mark2008cost-e1]: Mark、Gudith、Klocke 2008，Abstract。[证据](../../sources/notes/mark2008cost.md#e1)
[^mark2008cost-e2]: Mark、Gudith、Klocke 2008，Experimental Design and Procedure。[证据](../../sources/notes/mark2008cost.md#e2)
[^mark2008cost-e3]: Mark、Gudith、Klocke 2008，Discussion and Conclusions。[证据](../../sources/notes/mark2008cost.md#e3)
[^mark2008cost-e4]: Mark、Gudith、Klocke 2008，Discussion and Conclusions。[证据](../../sources/notes/mark2008cost.md#e4)
[^nanda2025mindsets-e1]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e1)
[^nanda2025mindsets-e6]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e6)
[^nanda2025mindsets-e7]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e7)
[^nanda2025mindsets-e8]: Nanda 2025b，Prioritisation。[证据](../../sources/notes/nanda2025mindsets.md#e8)
[^nanda2025mindsets-e13]: Nanda 2025b，Moving Fast。[证据](../../sources/notes/nanda2025mindsets.md#e13)
[^nielsen2004principles-e2]: Nielsen 2004，Self-discipline。[证据](../../sources/notes/nielsen2004principles.md#e2)
[^nielsen2004principles-e3]: Nielsen 2004，The skills of the problem-solver。[证据](../../sources/notes/nielsen2004principles.md#e3)
[^parikh2018calendar-e1]: Parikh 2018，Philosophy。[证据](../../sources/notes/parikh2018calendar.md#e1)
[^parikh2018calendar-e2]: Parikh 2018，Principle 2。[证据](../../sources/notes/parikh2018calendar.md#e2)
[^parikh2018calendar-e3]: Parikh 2018，Principle 4。[证据](../../sources/notes/parikh2018calendar.md#e3)
[^ruder2020tips-e1]: Ruder 2020，Work on two things。[证据](../../sources/notes/ruder2020tips.md#e1)
[^ruder2020tips-e2]: Ruder 2020，Work on two things。[证据](../../sources/notes/ruder2020tips.md#e2)
[^ruder2020tips-e9]: Ruder 2020，3) Be ambitious。[证据](../../sources/notes/ruder2020tips.md#e9)
[^schulman2020opinionated-e16]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e17)
[^schulman2020opinionated-e18]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../sources/notes/schulman2020opinionated.md#e18)
[^schulman2020opinionated-e21]: Schulman 2020，When to Switch Problems。[证据](../../sources/notes/schulman2020opinionated.md#e21)
[^steinhardt2018stochastic-e4]: Steinhardt 2018，A Better Strategy: Sorting by Information Rate。[证据](../../sources/notes/steinhardt2018stochastic.md#e4)
