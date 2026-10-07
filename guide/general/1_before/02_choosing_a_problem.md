# 选题

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲怎么找到研究问题、怎么判断它值不值得做、怎么培养这种判断力（研究品味），以及选题时的常见陷阱。"什么样的研究算好研究"见[什么是研究，什么是好的研究](01_what_is_good_research.md)；题目选定后怎么推进、什么时候该放弃，见[推进研究](../2_during/01_making_progress.md)。

**读完本章，你应该能：**

- 用几种具体办法列出一份候选问题清单；
- 从重要性、可行性、你的优势和兴趣几方面比较候选问题，做出取舍；
- 用几个练习有意识地培养研究品味；
- 识别太增量、太空泛、追热点、被新想法带跑等陷阱。

---

## 1. 给选题留出时间，但边读边动手

**先说做法：** 专门留出一段时间选题，不要抓住第一个想到的问题；但这段时间不只是读文献，还要边读边思考、边做小尝试。

**为什么要留时间。** 选题最常见的错误，是抓住第一个想到的问题。一个项目通常要做好几年，草率的选择会带来很多挫败[^alon2009choose-e8]。Alon 的实验室有条规矩：新学生或博士后入组后 3 个月内不确定课题，先读、讨论、计划[^alon2009choose-e9]。一个想法刚显得可行时就急着动手，也是常见的失败；多和它相处一段时间，常能想出更深的版本[^olah2021taste-e12]。

**为什么又不能只读。** 你注定要在不完全了解的状态下开始工作，不要无休止地读背景文献[^eisnerproblems-e8]。还没动手就想挑出完美的问题，是另一种陷阱：品味离不开亲手实践[^olah2021taste-e9]。可以在感兴趣的方向上帮别人做项目，既能动手学习，又不必长期绑定[^olah2021taste-e17]。

> **不同的看法：选题该花多久？**
> - Alon 主张慢：每在选题上多花一周，后面能省下几个月甚至几年；他也承认，不是每个人都能自由选题或有时间长时间寻找[^alon2009choose-e8][^alon2009choose-e10]。
> - Eisner 和 Carlini 提醒别拖：尽早开始自己思考，与阅读交替进行，定期把想法给懂行的人看，让他提醒你有哪些相关工作[^eisnerproblems-e9]；找想法花到一定程度后，多想一小时不如先动手做点什么[^carlini2026best-e13]。
>
> 实际操作中 `[本项目分析]`：给选题一个明确的时间段（例如几周到三个月，视你的阶段和导师要求而定），在这段时间里**同时**读文献、写想法、做小实验。时间到了就选，选不出来就找导师一起定。

## 2. 列一份候选问题清单

不要只盯着一个想法。先用下面的办法列出一批候选，再去比较。

**从文献里找：**

- **找"不对劲"的地方。** 读论文时留意作者做了哪些有害的简化或随意的选择，那是你可以换种做法的机会[^eisnerproblems-e2]。如果读某个方向时总想问"为什么大家都用明显错误的方式做"，那可能就是你的题目[^carlini2026best-e9]。
- **读完再跳出来。** 先广泛阅读，然后有意识地跳出已有工作的框架，否则想不出新东西[^carlini2026best-e6]。每个领域都可能有沿袭下来的坏做法：一篇有影响的早期论文犯了关键错误，后来者跟着走[^carlini2026best-e7]。
- **改变已有工作的假设。** 找出已有工作背后的假设，尝试放宽，让方法在限制更少的条件下也能用[^huang2021ideas-e1]；或者反过来，把通用方法用到具体问题上，利用领域知识改进它[^huang2021ideas-e2]。
- **借用新工具。** 关注领域里新出现的工具，用到自己的问题上[^huang2021ideas-e3]。
- **从复现开始。** 复现别人的工作不算原创，但对自己的学习和领域都可能有用[^eisnerproblems-e1]；复现中发现的不一致，也常常是新问题的起点 `[本项目分析]`。

**从现实和数据里找：**

- **看现有的方法或系统在哪里做得不好**[^eisnerproblems-e5]；把最好的方法放到更多样的条件下，看它怎么失败[^huang2021ideas-e4]。
- **看数据。** 在很多领域，数据本身会提示问题[^eisnerproblems-e6]。
- **问别的学科的人**觉得什么有意思[^eisnerproblems-e5]。
- **找瓶颈。** 哪些问题（公认的或没被意识到的）在阻碍领域进步？解决不了的话，能否至少把它讲清楚、形式化[^eisnerproblems-e3][^olah2021taste-e14]？还有一类是"大家都知道挺重要，却没人认真做过"的问题，发现后先查文献、问同事，确认还没人做[^eisnerproblems-e4]。
- **去混乱的地方。** 一个混乱的领域其实是机会，那里可能有待发现的统一、简化的概念[^olah2021taste-e13]。
- **往前看。** 与其盯着大家现在在做的，不如预判新技术出现后会冒出哪些大问题[^huang2023decide-e3]。

**长期积累：**

- **心里装着一份重要问题清单。** 优秀的科学家心里有 10 到 20 个重要问题，一直在找攻克途径；看到新想法时，能立刻意识到它和哪个问题有关[^hamming1986you-e10]。
- **定期想大问题。** Hamming 每周五午饭后只讨论"大想法"[^hamming1986you-e9]。
- **保持开放。** 开着门工作会被打扰，但也会不时得到"什么可能重要"的线索[^hamming1986you-e18]。

**两种路线。** 想法驱动：读到"怎么做 X"，想到怎么做得更好，然后去验证[^schulman2020opinionated-e6]。它的缺点是容易撞车，因为大家读的是同样的文献[^schulman2020opinionated-e7]。目标驱动：先定一个具体目标，再解决通往目标的问题；目标会给你与众不同的视角，让你问出别人没问的问题[^schulman2020opinionated-e8]。Schulman 向大多数人推荐后者[^schulman2020opinionated-e14]。

## 3. 用"重要性 × 可行性 × 你的优势"比较候选问题

为什么要认真比较：一般的科学家几乎把所有时间花在自己都不认为重要的问题上[^hamming1986you-e8]，而不做重要的问题，就不太可能做出重要的工作[^hamming1986you-e1]。

对清单上每个问题，逐项问自己：

| 维度 | 问自己 |
|---|---|
| 重要性 | 做成了，最好情况下会改变多少人的认识或做法 `[本项目分析]`？用 Schulman 在机器学习里的说法：是把指标提升 10% 还是 10 倍[^schulman2020opinionated-e10]？有人关心吗[^patterson2001bad-e3]？它在 6、12、48 个月后看来还值得吗[^eisnerproblems-e7]？如果另一个组发表了这篇论文，你会兴奋地去读吗[^olah2021taste-e11]？ |
| 可行性 | 有没有合理的攻克途径[^hamming1986you-e2]？按你的技能和条件，预计要多久[^alon2009choose-e2]？能否设计小实验快速验证核心假设[^huang2023decide-e5]？ |
| 你的优势 | 你相对别人有什么独特优势[^huang2023decide-e1]？你在哪个角落可能是最强的[^carlini2026best-e10]？如果你不做，别人要晚多久才会做出来[^carlini2026best-e8]？ |
| 兴趣 | 这是不是你真正在乎的问题[^huang2023decide-e2]？如果世界上只有你一个人，你会做哪个[^alon2009choose-e12]？哪个想法几个月来反复回到你脑中[^alon2009choose-e13]？你的兴奋程度够不够支撑做 3–5 年[^patterson2001bad-e4]？ |

**怎么取舍：**

- **先划掉被完全压倒的。** Alon 用"可行性"和"兴趣"两条轴比较问题：如果 A 在两方面都比 B 好，就划掉 B[^alon2009choose-e6]。同样的办法可以用在上表的几个维度上 `[本项目分析]`。
- **可行性要打折扣。** 纸面上容易的问题，实际往往很难；纸面上难的，实际几乎做不成[^alon2009choose-e3]。
- **按阶段调整权重。** 刚入门时选容易些的问题，尽快得到正反馈、建立信心[^alon2009choose-e7]；之后再往更有意思的方向走 `[本项目分析]`。
- **重要性和优势要一起看。** 影响力大约是"你在某方面的能力 × 这个方向的重要性"；在一个没那么"重要"、但你很擅长的问题上，贡献可能比做一个你不擅长的问题更大[^carlini2026best-e11]。
- **分清两种"兴趣"。** 一种是 Alon 二维图上的"兴趣"轴，指项目预期能增加多少知识[^alon2009choose-e1]，其实更接近上表的"重要性"；Alon 提醒，判断它时要分清周围人（会议、系里）的大声音和自己心里"这个我觉得有意思"的小声音[^alon2009choose-e11]，并认为你越能让自己感兴趣，就越可能让读者感兴趣[^alon2009choose-e14]。另一种是你个人对题目兴不兴奋：Olah 不建议逼自己做不觉得兴奋的题目，哪怕理智上觉得它更重要，那样效率会低很多[^olah2021taste-e3]。
- **先敢想，再尽早检验。** 构思时像外行一样敢想，先别被技术困难吓住[^huang2023decide-e4]；动手后先做最可能失败的那部分，尽早知道想法行不行[^carlini2026best-e14]。

## 4. 有意识地培养研究品味

**品味是什么。** 研究品味大致就是挑选好问题的能力[^olah2021taste-e1]；更宽地说，也包括研究过程中各种没有标准答案的判断，比如哪些异常值得追、哪个实验更有说服力[^nanda2025taste-e2]。选对问题的能力比纯技术能力更重要[^schulman2020opinionated-e3][^carlini2026best-e3]。缺了它，就会写出技术上正确却没人读的论文，因为从没问过这个问题值不值得回答[^carlini2026best-e4]。

**它可以练，但练得慢。** 品味不全是天生的，很大程度靠学习[^nanda2025taste-e1]。刚入门觉得自己没品味完全正常[^nanda2025taste-e3]。它难练，是因为验证一个想法好不好常要几个月，一年只能得到几次反馈[^olah2021taste-e2][^nanda2025taste-e4]。所以练习的思路是：**用更便宜的方式获得更多反馈**。

**练习清单：**

1. 写下一批研究想法，请你尊敬的导师逐个打 1–10 分，对分歧大的深入讨论[^olah2021taste-e4]。
2. 问导师之前，先预测他会怎么回答，再对比[^nanda2025taste-e5]。
3. 开始一个想法前，写下你的预测和"为什么觉得它好"，做完后回顾[^nanda2025taste-e7]。
4. 别人做了你想过的点子时，对比结果和你的预期[^olah2021taste-e5]。
5. 访谈身边的研究者：为什么做这些问题、怎么选题[^olah2021taste-e6]。
6. 反思：为什么有些想法被广泛采用，有些被遗忘[^schulman2020opinionated-e5]？
7. 批判地审视自己所在圈子的品味，你的品味很大程度上受合作者和导师影响[^olah2021taste-e7]。
8. 早期优先做能较快得到中间结果的项目[^nanda2025taste-e8]，并且**把项目做完**：完成项目、获得反馈是获得品味的途径[^patterson2001bad-e11][^patterson2001bad-e7][^carlini2026best-e5]。

**提醒：** 自信不等于正确。人们往往先有了信念，很久之后才有准确的直觉[^nanda2025taste-e6]。

> **不同的看法：听导师的，还是坚持自己的判断？**
> - 一些研究者认为不该太听导师的。Szegedy 回顾说，他研究中的多数错误发生在听从导师批评时，最酷的工作起初都被认为没用[^olah2021taste-e15]。Olah 也指出，兴趣与导师不合时硬把想法扭成导师能接受的样子，结果是为妥协而优化[^olah2021taste-e10]。
> - 另一些人认为新手应多依靠导师。Olah 提醒上面的说法有幸存者偏差，不同人在不同阶段成熟度不同[^olah2021taste-e16]；Nanda 认为职业早期高度依赖导师或成熟研究方向是正常的[^nanda2025taste-e9]；Schulman 说做别人提出的想法不丢人，本事在于挑哪个、做得多好[^schulman2020opinionated-e4]。
>
> 实际操作中 `[本项目分析]`：入门阶段可以先接受导师或成熟方向，在其中练判断；同时把你不同意导师的地方和理由记下来，事后对照结果。这本身就是练习 2 和 3。

## 5. 避开常见陷阱

**太增量。** 重大贡献很少来自"再多算一位小数"[^hamming1986you-e12]。很多项目是"容易但不太有意思"的低垂果实[^alon2009choose-e5]。小幅改进在服务于更大目标时最有价值[^schulman2020opinionated-e11]；Schulman 从机器学习的角度说，新方法如果只比基线（用来对比的现有标准方法）好一点，就必须非常简单，否则没人会用[^schulman2020opinionated-e12]。换到其他学科也类似 `[本项目分析]`：改进很小、却要别人花很大代价才能采用的做法，很难被接受。

**太空泛、无从下手。** 意义再大，没有攻克途径就不算重要问题[^hamming1986you-e2]。也不要以为"难就是好"：很多项目又难又没意思[^alon2009choose-e5]。"永远不定义什么算成功"被 Patterson 列为毁掉研究生涯的做法之一[^patterson2001bad-e5]。补救办法：把问题稍微换个提法，有时就能找到好的解法，还可能做得更好[^hamming1986you-e13][^eisnerproblems-e10]。

**追热点。** 不要扎堆追最热的问题[^huang2023decide-e1]。Schulman 指出，想法驱动的研究容易撞车，因为大家读同样的文献，会想到相似的点子[^schulman2020opinionated-e7]；扎堆在热门方向，这种风险只会更大 `[本项目分析]`。选一个和大家不同的问题，会引你走向不同的想法[^schulman2020opinionated-e9]；不在最热门的方向，反而更容易脱颖而出[^carlini2026best-e12]。

**被新想法带跑，或者困在旧方向里。** 这是两种方向相反的错误：

- 新想法总比做了几个月的旧想法显得更诱人[^carlini2026best-e15]。Schulman 的经验是，换题太频繁比不肯换题更常见[^schulman2020opinionated-e13]。
- 反过来，也可能过度依恋一个方向、陷入沉没成本。Olah 的建议是：留出一两周退一步，列出其他最有希望的方向，问自己"如果从零开始，会做什么"[^olah2021taste-e8]。

---

## 本章检查清单

- [ ] 我列出了不止一个候选问题，而不是抓住第一个想法[^alon2009choose-e8]
- [ ] 我查过文献、问过懂行的人，确认还没人做过[^eisnerproblems-e4][^eisnerproblems-e9]
- [ ] 我能说出这个问题做成后最好情况的收益有多大[^schulman2020opinionated-e10]
- [ ] 我有一个合理的攻克途径，而不只是"意义重大"[^hamming1986you-e2]
- [ ] 我能说出自己做这个问题的独特优势[^huang2023decide-e1]
- [ ] 我对它的兴趣足以支撑做几年[^patterson2001bad-e4]
- [ ] 我设计了一个小实验，能尽早检验核心假设[^huang2023decide-e5][^carlini2026best-e14]
- [ ] 我把选题理由和预测写了下来，以后可以回顾[^nanda2025taste-e7]
- [ ] 我请导师或同行评点过这个想法[^olah2021taste-e4]

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 抓住第一个想到的问题 | 项目要做几年，草率选择带来挫败[^alon2009choose-e8] |
| 没完没了地读文献，迟迟不动手 | 品味离不开实践；你注定要在不完全了解时开始[^eisnerproblems-e8][^olah2021taste-e9] |
| 只问"能不能发论文"，不问值不值得回答 | 会写出技术正确却没人读的论文[^carlini2026best-e4] |
| 做上限只有小幅提升的题目 | 收益有限；除非方法极简或服务于更大目标[^schulman2020opinionated-e10][^schulman2020opinionated-e12] |
| 以为越难越好 | 很多项目又难又没意思[^alon2009choose-e5] |
| 追最热的方向 | 容易撞车 `[本项目分析]`；不在热门方向反而更容易脱颖而出[^carlini2026best-e12] |
| 逼自己做不感兴趣的题目 | 效率会低很多[^olah2021taste-e3] |
| 把想法扭成导师能接受的样子 | 为妥协而优化，而不是为质量[^olah2021taste-e10] |
| 一有新想法就换题 | 换题太频繁比不肯换题更常见[^schulman2020opinionated-e13] |

## 延伸阅读

- **Alon《How To Choose a Good Scientific Problem》**：三页短文，"可行性 × 兴趣"二维图和"3 个月规则"的出处，最适合第一次选题时读。
- **Hamming《You and Your Research》**："做重要的问题""重要问题要有攻克途径"的出处。
- **Olah《Research Taste Exercises》**：培养品味的具体练习和失败模式，文末收录了很多人的补充建议。
- **Nanda《Understanding and Cultivating Research Taste》**：把品味拆成直觉、知识框架、全局判断和信念几部分，讲怎样缩短反馈回路。
- **Eisner《How to Find Research Problems》**：从小到大列出各种贡献，以及具体从哪里找问题。
- **Carlini《How to win a best paper award》**：讲选题品味、"只有你能做的事"和比较优势，例子来自计算机安全和机器学习。
- **Schulman《An Opinionated Guide to ML Research》**：想法驱动与目标驱动的对比，以及"10% 还是 10 倍"的问题，例子来自机器学习。

[^alon2009choose-e2]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../../sources/notes/alon2009choose.md#e2)
[^alon2009choose-e3]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../../sources/notes/alon2009choose.md#e3)
[^alon2009choose-e1]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../../sources/notes/alon2009choose.md#e1)
[^alon2009choose-e5]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../../sources/notes/alon2009choose.md#e5)
[^alon2009choose-e6]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../../sources/notes/alon2009choose.md#e6)
[^alon2009choose-e7]: Alon 2009，The Two Dimensions of Problem Choice。[证据](../../../sources/notes/alon2009choose.md#e7)
[^alon2009choose-e8]: Alon 2009，Take Your Time。[证据](../../../sources/notes/alon2009choose.md#e8)
[^alon2009choose-e9]: Alon 2009，Take Your Time。[证据](../../../sources/notes/alon2009choose.md#e9)
[^alon2009choose-e10]: Alon 2009，Take Your Time。[证据](../../../sources/notes/alon2009choose.md#e10)
[^alon2009choose-e11]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../../sources/notes/alon2009choose.md#e11)
[^alon2009choose-e12]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../../sources/notes/alon2009choose.md#e12)
[^alon2009choose-e13]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../../sources/notes/alon2009choose.md#e13)
[^alon2009choose-e14]: Alon 2009，The Subjectivity of the Interest Axis。[证据](../../../sources/notes/alon2009choose.md#e14)
[^hamming1986you-e1]: Hamming 1986，"important problems" 一段。[证据](../../../sources/notes/hamming1986you.md#e1)
[^hamming1986you-e2]: Hamming 1986，"important problems" 一段。[证据](../../../sources/notes/hamming1986you.md#e2)
[^hamming1986you-e8]: Hamming 1986，"important problems" 一段。[证据](../../../sources/notes/hamming1986you.md#e8)
[^hamming1986you-e9]: Hamming 1986，"Great Thoughts Time" 一段。[证据](../../../sources/notes/hamming1986you.md#e9)
[^hamming1986you-e10]: Hamming 1986，"Great Thoughts Time" 之后。[证据](../../../sources/notes/hamming1986you.md#e10)
[^hamming1986you-e18]: Hamming 1986，"door open or the door closed" 一段。[证据](../../../sources/notes/hamming1986you.md#e18)
[^hamming1986you-e12]: Hamming 1986，"ambiguity" 一段之后。[证据](../../../sources/notes/hamming1986you.md#e12)
[^hamming1986you-e13]: Hamming 1986，把问题当作一类问题来解决的一段。[证据](../../../sources/notes/hamming1986you.md#e13)
[^schulman2020opinionated-e3]: Schulman 2020，Honing Your Taste。[证据](../../../sources/notes/schulman2020opinionated.md#e3)
[^schulman2020opinionated-e4]: Schulman 2020，Honing Your Taste。[证据](../../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e5]: Schulman 2020，Honing Your Taste。[证据](../../../sources/notes/schulman2020opinionated.md#e5)
[^schulman2020opinionated-e6]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../../sources/notes/schulman2020opinionated.md#e6)
[^schulman2020opinionated-e7]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../../sources/notes/schulman2020opinionated.md#e7)
[^schulman2020opinionated-e8]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../../sources/notes/schulman2020opinionated.md#e8)
[^schulman2020opinionated-e9]: Schulman 2020，Case Study of Goal-Driven Research。[证据](../../../sources/notes/schulman2020opinionated.md#e9)
[^schulman2020opinionated-e10]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../../sources/notes/schulman2020opinionated.md#e10)
[^schulman2020opinionated-e11]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../../sources/notes/schulman2020opinionated.md#e11)
[^schulman2020opinionated-e12]: Schulman 2020，Aim High, and Climb Incrementally Towards High Goals。[证据](../../../sources/notes/schulman2020opinionated.md#e12)
[^schulman2020opinionated-e13]: Schulman 2020，When to Switch Problems。[证据](../../../sources/notes/schulman2020opinionated.md#e13)
[^schulman2020opinionated-e14]: Schulman 2020，Idea-Driven vs Goal-Driven Research。[证据](../../../sources/notes/schulman2020opinionated.md#e14)
[^carlini2026best-e3]: Carlini 2026，Have good taste for problems。[证据](../../../sources/notes/carlini2026best.md#e3)
[^carlini2026best-e4]: Carlini 2026，Have good taste for problems。[证据](../../../sources/notes/carlini2026best.md#e4)
[^carlini2026best-e5]: Carlini 2026，Have good taste for problems。[证据](../../../sources/notes/carlini2026best.md#e5)
[^carlini2026best-e6]: Carlini 2026，Ignore all the papers。[证据](../../../sources/notes/carlini2026best.md#e6)
[^carlini2026best-e7]: Carlini 2026，Ignore all the papers。[证据](../../../sources/notes/carlini2026best.md#e7)
[^carlini2026best-e8]: Carlini 2026，Do something only you can do。[证据](../../../sources/notes/carlini2026best.md#e8)
[^carlini2026best-e9]: Carlini 2026，Do something only you can do。[证据](../../../sources/notes/carlini2026best.md#e9)
[^carlini2026best-e10]: Carlini 2026，Find your comparative advantage。[证据](../../../sources/notes/carlini2026best.md#e10)
[^carlini2026best-e11]: Carlini 2026，Get lucky: you're well suited to solve important problems。[证据](../../../sources/notes/carlini2026best.md#e11)
[^carlini2026best-e12]: Carlini 2026，Get lucky: you're well suited to solve important problems。[证据](../../../sources/notes/carlini2026best.md#e12)
[^carlini2026best-e13]: Carlini 2026，Pick your ideas for impact。[证据](../../../sources/notes/carlini2026best.md#e13)
[^carlini2026best-e14]: Carlini 2026，Kill papers that are not working。[证据](../../../sources/notes/carlini2026best.md#e14)
[^carlini2026best-e15]: Carlini 2026，Re-prioritize projects ruthlessly。[证据](../../../sources/notes/carlini2026best.md#e15)
[^olah2021taste-e1]: Olah 2021，开头。[证据](../../../sources/notes/olah2021taste.md#e1)
[^olah2021taste-e2]: Olah 2021，开头。[证据](../../../sources/notes/olah2021taste.md#e2)
[^olah2021taste-e3]: Olah 2021，开头。[证据](../../../sources/notes/olah2021taste.md#e3)
[^olah2021taste-e4]: Olah 2021，Exercise 1。[证据](../../../sources/notes/olah2021taste.md#e4)
[^olah2021taste-e5]: Olah 2021，Exercise 2。[证据](../../../sources/notes/olah2021taste.md#e5)
[^olah2021taste-e6]: Olah 2021，Exercise 3。[证据](../../../sources/notes/olah2021taste.md#e6)
[^olah2021taste-e7]: Olah 2021，Exercise 5。[证据](../../../sources/notes/olah2021taste.md#e7)
[^olah2021taste-e8]: Olah 2021，Failure Mode 1。[证据](../../../sources/notes/olah2021taste.md#e8)
[^olah2021taste-e9]: Olah 2021，Failure mode 2。[证据](../../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e10]: Olah 2021，Failure mode 3。[证据](../../../sources/notes/olah2021taste.md#e10)
[^olah2021taste-e11]: Olah 2021，文末收录的 Rachel Prudden 的建议。[证据](../../../sources/notes/olah2021taste.md#e11)
[^olah2021taste-e12]: Olah 2021，文末收录的 Andy Matuschak 的建议。[证据](../../../sources/notes/olah2021taste.md#e12)
[^olah2021taste-e13]: Olah 2021，文末引用的 Michael Nielsen。[证据](../../../sources/notes/olah2021taste.md#e13)
[^olah2021taste-e14]: Olah 2021，文末收录的 Arthur Allshire 的建议。[证据](../../../sources/notes/olah2021taste.md#e14)
[^olah2021taste-e15]: Olah 2021，文末收录的 Christian Szegedy 的看法。[证据](../../../sources/notes/olah2021taste.md#e15)
[^olah2021taste-e16]: Olah 2021，Olah 对 Szegedy 的评论。[证据](../../../sources/notes/olah2021taste.md#e16)
[^olah2021taste-e17]: Olah 2021，Failure mode 2 的对策。[证据](../../../sources/notes/olah2021taste.md#e17)
[^nanda2025taste-e1]: Nanda 2025，Introduction。[证据](../../../sources/notes/nanda2025taste.md#e1)
[^nanda2025taste-e2]: Nanda 2025，What is research taste?。[证据](../../../sources/notes/nanda2025taste.md#e2)
[^nanda2025taste-e3]: Nanda 2025，Where does taste come from?。[证据](../../../sources/notes/nanda2025taste.md#e3)
[^nanda2025taste-e4]: Nanda 2025，How to learn it?。[证据](../../../sources/notes/nanda2025taste.md#e4)
[^nanda2025taste-e5]: Nanda 2025，How to learn it?。[证据](../../../sources/notes/nanda2025taste.md#e5)
[^nanda2025taste-e6]: Nanda 2025，Conviction & Confidence。[证据](../../../sources/notes/nanda2025taste.md#e6)
[^nanda2025taste-e7]: Nanda 2025，Conviction & Confidence。[证据](../../../sources/notes/nanda2025taste.md#e7)
[^nanda2025taste-e8]: Nanda 2025，Cultivating Research Taste。[证据](../../../sources/notes/nanda2025taste.md#e8)
[^nanda2025taste-e9]: Nanda 2025，Conclusion。[证据](../../../sources/notes/nanda2025taste.md#e9)
[^eisnerproblems-e1]: Eisner，"small bones"。[证据](../../../sources/notes/eisnerproblems.md#e1)
[^eisnerproblems-e2]: Eisner，"small bones"。[证据](../../../sources/notes/eisnerproblems.md#e2)
[^eisnerproblems-e3]: Eisner，"big bones"。[证据](../../../sources/notes/eisnerproblems.md#e3)
[^eisnerproblems-e4]: Eisner，"ripe for the plucking"。[证据](../../../sources/notes/eisnerproblems.md#e4)
[^eisnerproblems-e5]: Eisner，"identify new interesting problems"。[证据](../../../sources/notes/eisnerproblems.md#e5)
[^eisnerproblems-e6]: Eisner，"identify new interesting problems"。[证据](../../../sources/notes/eisnerproblems.md#e6)
[^eisnerproblems-e7]: Eisner，Keep in mind。[证据](../../../sources/notes/eisnerproblems.md#e7)
[^eisnerproblems-e8]: Eisner，Finally。[证据](../../../sources/notes/eisnerproblems.md#e8)
[^eisnerproblems-e9]: Eisner，Finally。[证据](../../../sources/notes/eisnerproblems.md#e9)
[^eisnerproblems-e10]: Eisner，"big bones"。[证据](../../../sources/notes/eisnerproblems.md#e10)
[^huang2021ideas-e1]: Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1423499757591400448) Relax assumptions。[证据](../../../sources/notes/huang2021ideas.md#e1)
[^huang2021ideas-e2]: Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1423499757591400448) Make more assumptions。[证据](../../../sources/notes/huang2021ideas.md#e2)
[^huang2021ideas-e3]: Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1423499757591400448) Grab a powerful hammer。[证据](../../../sources/notes/huang2021ideas.md#e3)
[^huang2021ideas-e4]: Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1423499757591400448) Stress test the state-of-the-art。[证据](../../../sources/notes/huang2021ideas.md#e4)
[^huang2023decide-e1]: Huang 2023，[推文串](https://twitter.com/jbhuang0604/status/1628521223838654464) Find your position。[证据](../../../sources/notes/huang2023decide.md#e1)
[^huang2023decide-e2]: Huang 2023，[推文串](https://twitter.com/jbhuang0604/status/1628521223838654464) Identify intrinsic motivation。[证据](../../../sources/notes/huang2023decide.md#e2)
[^huang2023decide-e3]: Huang 2023，[推文串](https://twitter.com/jbhuang0604/status/1628521223838654464) Anticipate disruptive technologies。[证据](../../../sources/notes/huang2023decide.md#e3)
[^huang2023decide-e4]: Huang 2023，[推文串](https://twitter.com/jbhuang0604/status/1628521223838654464) Imagine success。[证据](../../../sources/notes/huang2023decide.md#e4)
[^huang2023decide-e5]: Huang 2023，[推文串](https://twitter.com/jbhuang0604/status/1628521223838654464) Validate the idea fast。[证据](../../../sources/notes/huang2023decide.md#e5)
[^patterson2001bad-e3]: Patterson 2001，第 30 页。[证据](../../../sources/notes/patterson2001bad.md#e3)
[^patterson2001bad-e4]: Patterson 2001，第 30 页。[证据](../../../sources/notes/patterson2001bad.md#e4)
[^patterson2001bad-e5]: Patterson 2001，第 11 页。[证据](../../../sources/notes/patterson2001bad.md#e5)
[^patterson2001bad-e11]: Patterson 2001，第 35 页。[证据](../../../sources/notes/patterson2001bad.md#e11)
[^patterson2001bad-e7]: Patterson 2001，第 42 页。[证据](../../../sources/notes/patterson2001bad.md#e7)
