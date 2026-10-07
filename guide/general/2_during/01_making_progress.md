# 推进研究：迭代、去风险、卡住了怎么办

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲题目选定之后，怎样把一个项目一天天、一周周地往前推：先做什么，怎样尽快知道行不行，卡住了怎么办，什么时候该换方向，几个月的项目怎么规划。怎么选题见[选题](../1_before/02_choosing_a_problem.md)；实验怎么设计、结论怎样才可信见[研究设计与方法选择](../1_before/04_research_design.md)和[证据、分析与效度](02_evidence_and_validity.md)；什么时候开始写、怎么写见[写作](../3_after/01_writing.md)；怎样和导师一起推进见[合作与导师](../4_throughout/01_collaboration_and_advisors.md)。

**读完本章，你应该能：**

- 判断项目现在处于"探索"还是"聚焦"阶段，并按阶段安排工作；
- 把项目里风险最大的部分找出来，先用便宜的办法验证；
- 缩短"有想法 → 看到结果"的周期；
- 坚持记研究日志，并定期回顾；
- 卡住时有一套固定的办法可用，并能有根据地决定坚持还是放弃；
- 把几个月的项目拆成能排进日程的任务。

---

## 1. 先弄清项目处在哪个阶段

**怎么做：**

- **探索阶段**：你还提不出具体假设，甚至不知道该问什么问题。这时的目标只是**获取信息**：多做小实验，多看数据，跟着好奇心走，求快[^nanda2025process-e1]。
- **聚焦阶段**：当你能**写下具体假设**，并且知道用什么证据判断它真假，就进入了检验假设的阶段[^nanda2025process-e5]。这时要围绕假设设计实验，不再到处试。
- 在探索阶段，经常问自己：**"单位时间内我得到的信息够不够？"** 最近没学到新东西，就换个做法[^nanda2025process-e3]。

**为什么：** 新手在项目早期卡住，常常是因为以为自己已经到了该有明确假设的阶段，其实还在探索阶段[^nanda2025process-e2]。认清这一点，就不必因为暂时没有清晰目标而焦虑。`[本项目分析]`

**容易错在哪：**

- 一有个看似合理的假设，就急着进入聚焦阶段。还没解释的异常现象，往往就是线索。`[本项目分析]`
- 以为只能往前走。做到后面发现事情比想象复杂，退回到检验假设甚至探索阶段，是正常的，不代表你搞砸了[^nanda2025process-e6]。

## 2. 先做最可能失败的部分

一个项目通常由几个部分组成，每一部分都要成功，项目才成功。比如一个证明依赖几个中间引理，一套实验需要数据、方法、测量都靠得住。

**怎么做：**

1. 列出项目的各个部分，给每部分粗估两个数：**成功的把握有多大**、**要花多长时间**。
2. **优先做"更可能失败、又花时间少"的部分**[^steinhardt2018stochastic-e3]。一句话：先做信息量最大的，而不是最容易的[^steinhardt2018stochastic-e12]。
3. 对每个部分，先找一个**便宜的办法**判断它行不行，这叫去风险（de-risking）。先对所有部分去风险，再正式执行[^steinhardt2018stochastic-e5]。

**便宜的验证办法举例：**

- 要用一批数据：先取一小部分，手工看几条、算些统计量，确认数据合用，再花大力气整理全部数据[^steinhardt2018stochastic-e6]。
- 要证明一个结论：先跑模拟看它是否真的成立[^steinhardt2018stochastic-e18]；先想想问题的简化版本[^steinhardt2018stochastic-e8]。
- 对每个关键假设问一句：**"如果这个方向注定不行，怎样最快发现？"** 然后设计最快、最粗糙的实验去检验它[^nanda2025mindsets-e12]。

**为什么：** 人的本能是从易到难。常见的结局是：容易的部分都做完了，才在难的部分撞上根本障碍，整个计划推倒重来，前面的工作白做[^steinhardt2018stochastic-e2]。

## 3. 缩短反馈周期

反馈周期（feedback loop）指从"有了一个实验想法"到"看到结果"的过程。这段时间短，就叫反馈周期"紧"[^nanda2025mindsets-e10]；周期越紧，同样的时间里能试的想法越多。`[本项目分析]`

**怎么做：**

- **先做快而粗糙的实验。** 先花一两天看到初步迹象，远好于花几周做一个昂贵但结论明确的实验[^nanda2025mindsets-e11]。项目初期，尽量选一天之内能出结果的实验[^perez2024tips-e3]。
- **用玩具例子和代理任务**缩短周转时间[^huang2023unstuck-e6]。玩具例子（toy example）指刻意简化、只保留核心机制的小例子；代理任务（proxy task）指能替代真实任务、但更小更快的任务。找能抓住核心思想的**最简单玩具模型**，用它建立直觉[^freeman2013research-e4]。
- **舍得花时间改进工具。** 如果每次都要等很久才能看到结果，花几天把流程提速往往很划算[^carlini2022rapid-e2][^carlini2022rapid-e3]。
- **每次只改一个地方。** 这样才知道结果的变化是哪个改动造成的[^freeman2013research-e2]。

**适用范围：** 上面"一天出结果""花几天提速"的建议来自计算机和机器学习。在一次实验要几个月的学科（如临床研究、野外调查、长期培养实验、大规模访谈），一天出结果不现实；可以用预实验、小样本试做、模拟，或先用已有文献和公开数据检验想法，来缩短每一轮的反馈。`[本项目分析]`

> **不同的看法：快一点，还是慢一点？**
> - Nanda、Carlini 等人强调求快：能快速迭代才能做出好研究，反馈周期要尽可能短[^carlini2022rapid-e1][^nanda2025mindsets-e11]。
> - Freeman 的第一条建议却是"慢下来才能快"：要放慢，核实自己的假设，每次实验只改一个地方[^freeman2013research-e1][^freeman2013research-e2]。
> - 两者并不完全矛盾。Nanda 也承认，以速度为名变得马虎、引入错误，长期反而更费时间[^nanda2025mindsets-e14]。
>
> 实际操作中可以这样理解 `[本项目分析]`：**缩短的是每一轮的周期，而不是降低每一轮的严谨程度。** 用小规模、简化的问题让每一轮变快；每一轮之内仍然一次只改一处、核实假设。

## 4. 记研究日志，并定期回顾

**怎么做：**

- **每天记。** 记下做了什么、想了什么[^schulman2020opinionated-e16][^dredze2012successful-e2]。边做实验边记，结果一出来就记下图表、统计量和自己的观察结论[^perez2024tips-e4]。
- **让日志可以搜索**，例如用纯文本或笔记软件[^dredze2012successful-e2]。
- **每一两周回顾一次。** 通读这段时间的记录，压缩成一份总结：实验发现、新的见解、完成了什么、下一步做什么[^schulman2020opinionated-e17]。
- **另开两份文件：**
  - "亮点文档"：只收特别有意思的结果，方便发现它们之间的联系[^nanda2025process-e4]；
  - "想法清单"：做项目时冒出的新想法先记在这里，然后回到手头的事[^carlini2024logfile-e1][^carlini2024logfile-e2]。

**这些记录和别处的回顾、笔记是什么关系** `[本项目分析]`：不要另起炉灶。这里的研究日志，就是[整理科研材料](03_organizing_materials.md#5-分清三种笔记)里三种笔记中的"研究日志"；亮点文档里的结果经过检验后，整理进那里的"稳定结论"。每一两周的日志回顾，就作为[做计划](../1_before/05_planning.md#6-每周按主张回顾持续更新计划)里每周按主张回顾的输入，不必再单独做一次回顾。

**为什么：**

- 结论很容易忘，比如哪个设置真正起了作用；定期把日志压缩成总结，结论就不会埋在几百条记录里。`[本项目分析]`
- 回顾时能看出自己是不是在想法之间跳来跳去，留下一堆半途而废的项目[^schulman2020opinionated-e18]。
- 想法清单让你不怕忘记新想法，因而不容易被它带跑；隔一段时间再读，一个想法要两次都觉得好才值得做，判断更客观[^carlini2024logfile-e2][^carlini2024logfile-e3]。

## 5. 卡住时，按固定步骤排查

大多数时候实验都不成功，这是常态[^huang2023unstuck-e1]，每个人都会卡住和灰心[^dredze2012successful-e4]。关键是有一套办法。

**依次试这些：**

1. **把失败说具体。** 不要只说"不行"。写下：输入是什么，预期结果是什么，实际结果是什么[^huang2023unstuck-e2]；问题已经缩小到哪一步，排除了哪些原因[^freeman2013research-e3]。
2. **简化问题，直到它必然成功。** 多个变单个，一般变具体，大变小，复杂变简单；先让最简单的情形成功，再一步步加回难度[^huang2023unstuck-e3][^freeman2013research-e6]。
3. **假设已知一部分。** 要同时求 A 和 B，先假设 B 已知，只求 A[^huang2023unstuck-e4]。
4. **追问失败的原因。** 目的是避免反复尝试因同一原因失败的做法[^steinhardt2018stochastic-e9][^steinhardt2018stochastic-e21]；思路同[第 2 节](#2-先做最可能失败的部分)：先弄清信息量最大的问题。
5. **检查想法本身。** 代码和实验都查过仍然不行，就退一步检查想法[^huang2023unstuck-e5]。
6. **换一种问题表述。** 死守问题的某一种表述是常见错误；找到相关问题，或换个说法让自己能往前走，也是进展[^nielsen2004principles-e4]。
7. **还是没头绪：** 定 5 分钟计时，列出所有能做的事[^nanda2025mindsets-e5]；然后找人讨论（见[合作与导师](../4_throughout/01_collaboration_and_advisors.md)）。

**记住：** 进展不只是"做成了"。说明了为什么不行、把任务简化到能跑通、为弄懂问题花时间读书，都算进展[^freeman2013research-e7]。只要在了解问题，实验"没成功"也是收获[^perez2024tips-e1]。

## 6. 有根据地决定坚持还是放弃

难点在于：有的想法只是一个细节错了才没效果，有的则怎么做都注定失败，两者很难分辨[^schulman2020opinionated-e19]。

**判断时注意：**

- **一次失败不等于想法失败，否定要有高标准。** 你试的只是这个思路的一种实现[^steinhardt2018stochastic-e10]；"看起来不行""没动力了"都不算排除了它，要能说出它为什么注定不行[^steinhardt2018stochastic-e22]。（怎样用便宜的验证尽早得到这种判断，见[第 2 节](#2-先做最可能失败的部分)。）
- **换得太勤比换得太少更常见。** 做到艰难处，新想法总显得更诱人；但新想法的初步结果多半同样令人失望[^schulman2020opinionated-e13][^schulman2020opinionated-e20]。频繁切换、什么都没好好探索，就什么也学不到[^nanda2025mindsets-e1]。
- **该停的信号：** 你在反复降低目标和期望[^dredze2012successful-e5]；或项目收益明显递减[^perez2024tips-e2]。这时果断放弃不丢人[^nanda2025mindsets-e1]。
- **先认清自己的毛病。** 有人钻牛角尖不肯放手，有人想太多迟迟不动手；对照自己偏向哪一种，取相应的建议[^nanda2025mindsets-e9]。

**一个折中：** 给偏离主线的新想法留一份固定的时间预算，主线照常推进[^schulman2020opinionated-e21]。

> **不同的看法：同时做一个项目还是两个？**
> - Schulman 提醒：回顾几个月时，可能发现自己在想法间跳来跳去，留下一堆半成品[^schulman2020opinionated-e18]。
> - Ruder 建议同时做两个项目：一个碰壁时转去做另一个，换换脑子；为减少切换，每天只做其中一个[^ruder2020tips-e1][^ruder2020tips-e2]。
>
> 实际操作中 `[本项目分析]`：新手先保证**一个主项目**能走完；如果主项目常常要等（等数据、等设备、等别人），再加一个小的副项目，并按天而不是按小时切换。从长期积累的角度看这个问题，见[心态与长期积累](../4_throughout/03_mindset_and_growth.md)。

## 7. 规划长线项目和每周的时间

**怎么做：**

1. **定三层目标并写下来：** 项目总目标（以月计）、当前子目标（以周计）、眼下的具体目标（以天计）[^nanda2025mindsets-e3]。定期检查是否在朝它推进[^nanda2025mindsets-e2]。
2. **写计划，估用时。** 至少为当前阶段写一份计划，估计每步要多久；计划不必死守，偏离很正常[^nanda2025mindsets-e4]。
3. **从截止日期倒推。** 例如会议投稿截止前三个月：至少提前一个月动笔写完整初稿，往前推就是拿到主要结果的时间[^parikh2018calendar-e5]。这是动笔写完整初稿的最晚时间；提纲和草稿从项目开始就写（见[写作](../3_after/01_writing.md#6-尽早动笔把写作当作研究的一部分)和[做计划](../1_before/05_planning.md#1-从终点倒推先想清楚最后要说什么)）。倒推出来的都是"最晚"时间，要留余量[^parikh2018calendar-e6]。期刊没有固定截止日期，可以用答辩、基金结题或自己定的投稿日期来倒推。`[本项目分析]`
4. **把任务拆小，排进日历。** 大项目拆成 20 分钟到 2 小时的小块[^steinhardt2018stochastic-e16]，放进日历的具体时段；日历让你看清时间是有限的[^parikh2018calendar-e1]。规划本身也是一项要排进日历的任务[^parikh2018calendar-e4]。
5. **测出自己的估时偏差。** 每个任务先估时间，再记下实际用时[^steinhardt2018stochastic-e16]。算出"实际 / 预估"的比值，以后排期乘上它[^parikh2018calendar-e2]。
6. **计划被打乱就重排。** 重新排期是计划的一部分，不是失败[^parikh2018calendar-e3]。
7. **每周回顾一次。** 统一按[做计划](../1_before/05_planning.md#6-每周按主张回顾持续更新计划)里的"每周按主张回顾"来做，它包括回顾证据和回顾时间两部分；输入就是第 4 节的日志回顾。

**为什么：**

- 除了埋头苦干，还要定期"掌舵"，确认自己在做对的事[^freeman2013research-e5]。排优先级和执行是两种状态，最好分开：留出反思的时间，其余时间专心执行[^nanda2025mindsets-e6]。
- 拖延和漫无目的，多半是因为没想清楚"要做成什么、为什么、怎么做"[^nielsen2004principles-e1]。把项目和一个你真正在乎的目标连起来，更容易在起起落落中坚持下去[^schulman2020opinionated-e15]。
- 大多数时候动起来比停着好，前提是经常留出时间反思目标[^nielsen2004principles-e3]。
- 你以为的研究时间可能远多于实际。有人用秒表记录，发现扣除各种打断后每天平均只做了半小时研究[^nielsen2004principles-e2]。记录时间花在哪里，再复盘[^nanda2025mindsets-e13][^dredze2012successful-e1]。

**可持续地工作：** 很多研究者因工作方式不可持续而倦怠[^perez2024tips-e5]。休息通常让有效工作时间净增加[^nanda2025process-e7]；照顾好身体和情绪，否则效率也会下降[^dredze2012successful-e3]。（更多见[心态与长期积累](../4_throughout/03_mindset_and_growth.md#5-保持能长期维持的节奏)。）

## 本章检查清单

- [ ] 我能说出项目现在处于探索阶段还是聚焦阶段；如果是聚焦阶段，我能写下要检验的假设。
- [ ] 我列出了项目的各个部分，并已用便宜的办法验证了风险最大的那几个。
- [ ] 我知道一轮"想法 → 结果"要多久，并想过怎样缩短。
- [ ] 我每天记研究日志，最近两周内做过一次回顾总结。
- [ ] 新想法记在想法清单里，没有打断主线。
- [ ] 最近一次失败，我能说清楚卡在哪一步、排除了哪些原因。
- [ ] 想放弃某个方向时，我能给出它注定不行的理由，而不只是"感觉不行"。
- [ ] 我有写下来的三层目标，以及从截止日期倒推出的时间表（留了余量）。
- [ ] 我知道自己的估时偏差大概是多少。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 从最容易的部分做起 | 做完容易的部分才发现难的部分做不了，前面的工作白做[^steinhardt2018stochastic-e2] |
| 一上来就做又大又慢的完整实验 | 几周后才得到第一个信号；快而粗糙的实验能更早告诉你方向对不对[^nanda2025mindsets-e11] |
| 一次改好几个地方 | 结果变了也不知道是哪个改动造成的[^freeman2013research-e2] |
| 向导师汇报"不行" | 别人无从帮你；要说清预期、实际结果和已排除的原因[^freeman2013research-e3][^huang2023unstuck-e2] |
| 一次实验失败就放弃整个思路 | 失败的只是一种实现，不是整个思路[^steinhardt2018stochastic-e10] |
| 一碰到困难就换新想法 | 留下一堆半成品；新想法多半同样艰难[^schulman2020opinionated-e18][^schulman2020opinionated-e20] |
| 不记日志 | 回头看不出自己是不是在想法之间跳来跳去、留下一堆半成品[^schulman2020opinionated-e18] |
| 按直觉估时间、按截止日期排期 | 大多数人低估耗时，倒推出的最晚时间没有余量[^parikh2018calendar-e2][^parikh2018calendar-e6] |

## 延伸阅读

- **Steinhardt, "Research as a Stochastic Decision Process"**：想弄清"先做哪一步"时读。用简单的计算说明为什么要先做信息量最大的部分，并给出去风险的具体办法。
- **Nanda, "How I Think About My Research Process" 与 "Key Mindsets"**：想知道项目各阶段该干什么、怎样排优先级时读。两篇文章面向机器学习研究者，但阶段划分和每周回顾的问题适用于各学科。
- **Schulman, "An Opinionated Guide to ML Research"**：想建立研究日志习惯、纠结要不要换题时读。
- **Jia-Bin Huang, "How to get unstuck?"**（推文串）：卡住时的速查清单。
- **Parikh, "Calendar. Not to-do lists."**：时间总是不够用、计划总是落空时读。
- **Freeman, "How to do research"**：三页讲义，适合刚从做习题转到做研究的人。

[^nanda2025process-e1]: Nanda 2025a，Exploration (Stage 2)。[证据](../../../sources/notes/nanda2025process.md#e1)
[^nanda2025process-e2]: Nanda 2025a，Exploration (Stage 2)。[证据](../../../sources/notes/nanda2025process.md#e2)
[^nanda2025process-e3]: Nanda 2025a，Exploration (Stage 2)。[证据](../../../sources/notes/nanda2025process.md#e3)
[^nanda2025process-e4]: Nanda 2025a，Exploration (Stage 2)。[证据](../../../sources/notes/nanda2025process.md#e4)
[^nanda2025process-e5]: Nanda 2025a，Understanding (Stage 3)。[证据](../../../sources/notes/nanda2025process.md#e5)
[^nanda2025process-e6]: Nanda 2025a，Distillation (Stage 4)。[证据](../../../sources/notes/nanda2025process.md#e6)
[^nanda2025process-e7]: Nanda 2025a，Introduction。[证据](../../../sources/notes/nanda2025process.md#e7)
[^nanda2025mindsets-e1]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e1)
[^nanda2025mindsets-e2]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e2)
[^nanda2025mindsets-e3]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e3)
[^nanda2025mindsets-e4]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e4)
[^nanda2025mindsets-e5]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e5)
[^nanda2025mindsets-e6]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e6)
[^nanda2025mindsets-e9]: Nanda 2025b，Prioritisation。[证据](../../../sources/notes/nanda2025mindsets.md#e9)
[^nanda2025mindsets-e10]: Nanda 2025b，Moving Fast。[证据](../../../sources/notes/nanda2025mindsets.md#e10)
[^nanda2025mindsets-e11]: Nanda 2025b，Moving Fast。[证据](../../../sources/notes/nanda2025mindsets.md#e11)
[^nanda2025mindsets-e12]: Nanda 2025b，Moving Fast。[证据](../../../sources/notes/nanda2025mindsets.md#e12)
[^nanda2025mindsets-e13]: Nanda 2025b，Moving Fast。[证据](../../../sources/notes/nanda2025mindsets.md#e13)
[^nanda2025mindsets-e14]: Nanda 2025b，Moving Fast。[证据](../../../sources/notes/nanda2025mindsets.md#e14)
[^steinhardt2018stochastic-e2]: Steinhardt 2018，Warm-Up。[证据](../../../sources/notes/steinhardt2018stochastic.md#e2)
[^steinhardt2018stochastic-e3]: Steinhardt 2018，Warm-Up。[证据](../../../sources/notes/steinhardt2018stochastic.md#e3)
[^steinhardt2018stochastic-e5]: Steinhardt 2018，A further improvement。[证据](../../../sources/notes/steinhardt2018stochastic.md#e5)
[^steinhardt2018stochastic-e6]: Steinhardt 2018，A further improvement。[证据](../../../sources/notes/steinhardt2018stochastic.md#e6)
[^steinhardt2018stochastic-e16]: Steinhardt 2018，Caveats。[证据](../../../sources/notes/steinhardt2018stochastic.md#e16)
[^steinhardt2018stochastic-e8]: Steinhardt 2018，Some further practical ideas。[证据](../../../sources/notes/steinhardt2018stochastic.md#e8)
[^steinhardt2018stochastic-e18]: Steinhardt 2018，Some further practical ideas。[证据](../../../sources/notes/steinhardt2018stochastic.md#e18)
[^steinhardt2018stochastic-e9]: Steinhardt 2018，Exponentially branching search trees。[证据](../../../sources/notes/steinhardt2018stochastic.md#e9)
[^steinhardt2018stochastic-e10]: Steinhardt 2018，Exponentially branching search trees。[证据](../../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e21]: Steinhardt 2018，Exponentially branching search trees。[证据](../../../sources/notes/steinhardt2018stochastic.md#e21)
[^steinhardt2018stochastic-e22]: Steinhardt 2018，Additional Discussion。[证据](../../../sources/notes/steinhardt2018stochastic.md#e22)
[^steinhardt2018stochastic-e12]: Steinhardt 2018，Summary。[证据](../../../sources/notes/steinhardt2018stochastic.md#e12)
[^perez2024tips-e1]: Perez 2024，General Mindset Tips。[证据](../../../sources/notes/perez2024tips.md#e1)
[^perez2024tips-e2]: Perez 2024，General Mindset Tips。[证据](../../../sources/notes/perez2024tips.md#e2)
[^perez2024tips-e3]: Perez 2024，Three modes of research。[证据](../../../sources/notes/perez2024tips.md#e3)
[^perez2024tips-e4]: Perez 2024，Three modes of research。[证据](../../../sources/notes/perez2024tips.md#e4)
[^perez2024tips-e5]: Perez 2024，Work Habits。[证据](../../../sources/notes/perez2024tips.md#e5)
[^huang2023unstuck-e1]: Jia-Bin Huang 2023，推文串 [How to get unstuck?](https://twitter.com/jbhuang0604/status/1717381151508054029)，第 1 条。[证据](../../../sources/notes/huang2023unstuck.md#e1)
[^huang2023unstuck-e2]: Jia-Bin Huang 2023，推文串，Show HOW it failed。[证据](../../../sources/notes/huang2023unstuck.md#e2)
[^huang2023unstuck-e3]: Jia-Bin Huang 2023，推文串，Simplify the tasks until it works。[证据](../../../sources/notes/huang2023unstuck.md#e3)
[^huang2023unstuck-e4]: Jia-Bin Huang 2023，推文串，Introduce privileged information。[证据](../../../sources/notes/huang2023unstuck.md#e4)
[^huang2023unstuck-e5]: Jia-Bin Huang 2023，推文串，Debug the idea。[证据](../../../sources/notes/huang2023unstuck.md#e5)
[^huang2023unstuck-e6]: Jia-Bin Huang 2023，推文串，Iterate fast。[证据](../../../sources/notes/huang2023unstuck.md#e6)
[^freeman2013research-e1]: Freeman 2013，第 1 页。[证据](../../../sources/notes/freeman2013research.md#e1)
[^freeman2013research-e2]: Freeman 2013，第 1 页。[证据](../../../sources/notes/freeman2013research.md#e2)
[^freeman2013research-e3]: Freeman 2013，第 1 页。[证据](../../../sources/notes/freeman2013research.md#e3)
[^freeman2013research-e4]: Freeman 2013，第 1 页。[证据](../../../sources/notes/freeman2013research.md#e4)
[^freeman2013research-e5]: Freeman 2013，第 1 页。[证据](../../../sources/notes/freeman2013research.md#e5)
[^freeman2013research-e6]: Freeman 2013，第 3 页。[证据](../../../sources/notes/freeman2013research.md#e6)
[^freeman2013research-e7]: Freeman 2013，第 3 页。[证据](../../../sources/notes/freeman2013research.md#e7)
[^carlini2022rapid-e1]: Carlini 2022，开头段。[证据](../../../sources/notes/carlini2022rapid.md#e1)
[^carlini2022rapid-e2]: Carlini 2022，"(Machine learning) research does not support rapid iteration" 一节。[证据](../../../sources/notes/carlini2022rapid.md#e2)
[^carlini2022rapid-e3]: Carlini 2022，同上。[证据](../../../sources/notes/carlini2022rapid.md#e3)
[^carlini2024logfile-e1]: Carlini 2024，开头段。[证据](../../../sources/notes/carlini2024logfile.md#e1)
[^carlini2024logfile-e2]: Carlini 2024，A bit more detail。[证据](../../../sources/notes/carlini2024logfile.md#e2)
[^carlini2024logfile-e3]: Carlini 2024，A bit more detail。[证据](../../../sources/notes/carlini2024logfile.md#e3)
[^schulman2020opinionated-e15]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../../sources/notes/schulman2020opinionated.md#e15)
[^schulman2020opinionated-e16]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../../sources/notes/schulman2020opinionated.md#e17)
[^schulman2020opinionated-e18]: Schulman 2020，Keep a Notebook, and Review It。[证据](../../../sources/notes/schulman2020opinionated.md#e18)
[^schulman2020opinionated-e19]: Schulman 2020，When to Switch Problems。[证据](../../../sources/notes/schulman2020opinionated.md#e19)
[^schulman2020opinionated-e13]: Schulman 2020，When to Switch Problems。[证据](../../../sources/notes/schulman2020opinionated.md#e13)
[^schulman2020opinionated-e20]: Schulman 2020，When to Switch Problems。[证据](../../../sources/notes/schulman2020opinionated.md#e20)
[^schulman2020opinionated-e21]: Schulman 2020，When to Switch Problems。[证据](../../../sources/notes/schulman2020opinionated.md#e21)
[^dredze2012successful-e1]: Dredze & Wallach 2012（v1.2），#16，第 4 页。[证据](../../../sources/notes/dredze2012successful.md#e1)
[^dredze2012successful-e2]: Dredze & Wallach 2012（v1.2），#18，第 4 页。[证据](../../../sources/notes/dredze2012successful.md#e2)
[^dredze2012successful-e3]: Dredze & Wallach 2012（v1.2），#20，第 4 页。[证据](../../../sources/notes/dredze2012successful.md#e3)
[^dredze2012successful-e4]: Dredze & Wallach 2012（v1.2），#21，第 4 页。[证据](../../../sources/notes/dredze2012successful.md#e4)
[^dredze2012successful-e5]: Dredze & Wallach 2012（v1.2），#34，第 6 页。[证据](../../../sources/notes/dredze2012successful.md#e5)
[^nielsen2004principles-e1]: Nielsen 2004，Self-discipline。[证据](../../../sources/notes/nielsen2004principles.md#e1)
[^nielsen2004principles-e2]: Nielsen 2004，Self-discipline。[证据](../../../sources/notes/nielsen2004principles.md#e2)
[^nielsen2004principles-e3]: Nielsen 2004，The skills of the problem-solver。[证据](../../../sources/notes/nielsen2004principles.md#e3)
[^nielsen2004principles-e4]: Nielsen 2004，The skills of the problem-solver。[证据](../../../sources/notes/nielsen2004principles.md#e4)
[^parikh2018calendar-e1]: Parikh 2018，Philosophy。[证据](../../../sources/notes/parikh2018calendar.md#e1)
[^parikh2018calendar-e2]: Parikh 2018，Principle 2。[证据](../../../sources/notes/parikh2018calendar.md#e2)
[^parikh2018calendar-e3]: Parikh 2018，Principle 4。[证据](../../../sources/notes/parikh2018calendar.md#e3)
[^parikh2018calendar-e4]: Parikh 2018，Principle 5。[证据](../../../sources/notes/parikh2018calendar.md#e4)
[^parikh2018calendar-e5]: Parikh 2018，Principle 6。[证据](../../../sources/notes/parikh2018calendar.md#e5)
[^parikh2018calendar-e6]: Parikh 2018，Principle 6。[证据](../../../sources/notes/parikh2018calendar.md#e6)
[^ruder2020tips-e1]: Ruder 2020，Work on two things。[证据](../../../sources/notes/ruder2020tips.md#e1)
[^ruder2020tips-e2]: Ruder 2020，Work on two things。[证据](../../../sources/notes/ruder2020tips.md#e2)
