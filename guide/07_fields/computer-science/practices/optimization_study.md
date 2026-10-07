# 优化研究：把问题建模成优化问题，用搜索求解

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲**优化研究**：把一个计算机问题表述成"在很多候选解中找最好的那个"，再用搜索算法、进化算法等优化技术求解，并用实验说明求解效果。软件工程里的**基于搜索的软件工程**（Search-Based Software Engineering，常缩写为 SBSE），例如自动生成测试用例，就是典型例子。

**适用范围** `[本项目分析]`：这是计算机的做法，例子和标准主要来自软件工程里基于搜索的软件工程。提出新的搜索方法时，它属于[构建改进](../../../05_research-strategies/build_improve.md)这种研究套路；拿几种算法比高低时，属于[比较评估](../../../05_research-strategies/compare_evaluate.md)。这些套路各学科通用的部分（要什么证据、怎样公平比较）见套路页，本文只讲优化研究特有的部分。

优化研究常常也是一项[工程研究](engineering_research.md)（你提出了新方法），评估时也像一次[基准评测](benchmarking.md)。"怎样公平配置对手、怎样控制测量环境"见基准评测；显著性检验、效应量的基本概念见[分析与解读](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

**读完本文，你应该能：**

- 把问题写成清楚的优化问题：解怎么表示、怎么打分、有哪些约束；
- 选出合适的基线，至少包括随机搜索；
- 处理算法的随机性：重复运行，用 Mann-Whitney U 检验和 Â12 效应量比较；
- 公平地设置参数和搜索预算，并报告清楚；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准这样界定：优化研究把问题表述为搜索问题，并用优化技术求解[^ralph2020empirical-e374]。它有两个要素：

- **适应度函数**（fitness function，也叫目标函数）：给每个候选解打分的数值函数，分数表示解的好坏[^ralph2020empirical-e375]。例如生成测试用例时，分数可以是覆盖了多少代码分支。
- **求解方法**：让这个分数尽量高（或尽量低）的算法，如元启发式算法（遗传算法、模拟退火等）、数值优化器、约束求解器。其中一部分带随机性[^ralph2020empirical-e376]。

标准是为软件工程写的，但同样的思路在计算机各方向都很常见，例如编译器参数的自动调优、集群任务调度、机器学习的超参数搜索 `[本项目分析]`。

**和相近类型的区别** `[本项目分析]`：

| | 优化研究 | 基准评测 | 定量仿真 |
|---|---|---|---|
| 核心问题 | 能不能找到更好的解？哪种搜索方法更有效？ | 现有系统在给定负载下表现如何？ | 如果系统这样运行，会发生什么？ |
| 主要产出 | 问题的表述方式、求解方法，以及它们的效果 | 系统间的比较结果 | 关于系统行为的推断 |
| 典型例子 | 用遗传算法生成测试用例，提高分支覆盖率 | 比较几个数据库的吞吐量 | 仿真不同调度策略下的集群吞吐量 |

**什么时候用**：问题的候选解太多，人工做太慢，或者组合起来无法穷举时，才值得用优化。标准把"说明为什么不能在合理时间内靠人工或穷举解决"列为必须做到的第一项[^ralph2020empirical-e377]。

---

## 2. 怎么做

### 第一步：把问题表述清楚

**怎么做**：写下四样东西[^ralph2020empirical-e378][^ralph2020empirical-e381]：

1. **解是什么**：一个解代表什么，例如一个测试套件。
2. **解怎么表示、怎么修改**：用什么数据结构表示（如向量、树），算法怎样改动它（如交叉、变异）。
3. **适应度函数**：优化什么目标，计算公式是什么。
4. **搜索空间和约束**：变量有哪些、各自能取什么值、有哪些约束。

**为什么**：表述决定了算法能找到什么。读者看不到你的表述，就无法判断结果来自好的算法，还是来自对问题的巧妙（或过度）简化 `[本项目分析]`。

**容易错在哪**：

- **简化过头。** 简化和约束要符合实际、有节制；如果简化到所有解都能穷举，就不需要优化了[^ralph2020empirical-e378]。
- **选项空间不真实。** 属性的取值应是现实中可能出现的，而不是从随意的分布中生成的[^ralph2020empirical-e386]。
- **多个目标硬凑成一个分数。** 有多个互相冲突的目标时（如覆盖率和测试时长），把它们简单加权成一个分数，会掩盖目标之间的取舍 `[本项目分析]`。SIGSOFT 标准指出，评价多目标方法，更重要的是看帕累托前沿（Pareto front：一组解，其中任何一个都无法在不牺牲某个目标的情况下改进另一个目标）和相应的质量指标[^ralph2020empirical-e395]。

### 第二步：选算法，选基线

**怎么做：**

1. **说明为什么选这个算法。** 对新问题，很少有人知道哪种算法最好；但至少要参考类似问题上用过的算法，做有依据的判断[^ralph2020empirical-e379]。
2. **一定要和随机搜索比。** 随机搜索就是不断随机生成解、保留最好的那个 `[本项目分析]`。新问题至少要和随机搜索比；已有人做过的问题，要和现有最先进的方法比[^ralph2020empirical-e380]。
3. **再和更简单的方法比。** 看似复杂的方法，应当和更简单的替代方案比较[^menzies2019bad-e7]。

**为什么要和随机搜索比**：只有这样才能确认成功不是因为问题（或所选的实例）本身太简单[^arcuri2014hitchhiker-e4]。Arcuri & Briand 举过一个例子：ICSE 2009 的一篇获奖论文用遗传编程（一种进化算法）自动生成修复缺陷的补丁，每次运行总共只做 400 次适应度评估（种群 40 个、进化 10 代）；在一半的研究对象上，平均而言，合适的补丁在随机生成第一代种群时就已找到，进化搜索还没真正开始[^arcuri2014hitchhiker-e3]。

### 第三步：公平地设置参数和预算

**怎么做：**

1. **写清每个方法的全部参数及取值**，例如种群大小、交叉率、变异率[^ralph2020empirical-e382]，并说明为什么这样设[^ralph2020empirical-e387]。
2. **同等调参。** 把自己的方法精心调好、对手用默认参数，是特别糟糕的做法：这种比较只能说明"用好新方法，能胜过用坏另一个方法"[^menzies2019bad-e5][^menzies2019bad-e6]。怎样做到同等调优，见基准评测的[第三步](benchmarking.md#第三步选被比较的系统公平地配置每一个)。
3. **给每个方法相同的搜索预算**，例如相同的适应度评估次数或相同的运行时间，并在论文中写明 `[本项目分析]`。上面 400 次评估的例子说明，读者需要知道预算有多大，才能判断搜索到底起了多大作用[^arcuri2014hitchhiker-e3]。
4. **报告成本。** 实际选算法时，除了效果和 p 值，还要看成本差异，例如执行时间、需要用户提供多少输入[^arcuri2014hitchhiker-e6]。
5. **调参用的问题实例，最好不要同时用来做最终评估。** 否则参数可能只是恰好适合这几个实例 `[本项目分析]`；道理同[构建改进](../../../05_research-strategies/build_improve.md#对后面各阶段的影响)里"开发时参考过的例子不能再用来评估"一条。

更进一步，可以系统地分析不同参数选择的影响，并说明最终参数是怎么选出来的，标准把这列为"做得出色"[^ralph2020empirical-e390]。

### 第四步：重复运行，处理随机性

带随机性的算法，同一个问题实例跑两次，结果可能不同[^arcuri2014hitchhiker-e1]。Arcuri & Briand 对 2009—2010 年论文的系统综述发现，软件工程中涉及随机化算法的实证分析，总体上往往没有恰当处理这一点[^arcuri2014hitchhiker-e2]。

**怎么做：**

1. **找出所有随机性来源**：算法本身的随机性；测量环境随机量的适应度函数（例如以执行时间打分，每次测都不一样）；数据抽样或交叉验证[^ralph2020empirical-e384]。
2. **每个方法独立运行多次**，得到结果的分布，而不是一个数[^arcuri2014hitchhiker-e5][^ralph2020empirical-e384]。
3. **记录随机种子。** 不提供种子，别人就无法精确复现[^menzies2019bad-e8]。固定种子和换种子重复的关系，见[比较评估：差异是不是真的](../../../05_research-strategies/compare_evaluate.md#差异是不是真的)。
4. **写清运行了多少次、用了什么统计检验**[^arcuri2014hitchhiker-e12]。

> **不同的看法：要跑多少次？**
> - Arcuri & Briand 建议每个算法在每个问题实例上至少跑 1000 次；做不到就说明原因，并报告整个实验花了多少时间。他们的理由是多数软件工程问题跑几千次是可行的[^arcuri2014hitchhiker-e13][^arcuri2014hitchhiker-e9]。他们也承认会有例外，偏离时说明理由即可[^arcuri2014hitchhiker-e20]。
> - SIGSOFT 标准不规定次数：实验很耗时或有人参与时，可以只做有限几次，但要披露这一局限并讨论随机性的影响[^ralph2020empirical-e391]。
>
> 实际操作中：先估一下单次运行要多久。跑得起就多跑；跑不起就如实报告次数、总耗时和理由 `[本项目分析]`。如果问题实例很多而时间有限，Arcuri & Briand 建议宁可每个实例少跑几次（至少 10 次）、多用一些实例[^arcuri2014hitchhiker-e14]。

### 第五步：用合适的统计方法比较

**怎么做**：每对方法、每个问题实例，同时报告两样东西[^arcuri2014hitchhiker-e16][^arcuri2014hitchhiker-e18]：

**1. Mann-Whitney U 检验：差异是不是偶然的？**

Arcuri & Briand 建议，数值型结果（如覆盖率）用双侧的 Mann-Whitney U 检验；"找到/没找到"这类二元结果用 Fisher 精确检验（比较两组成功次数的检验）[^arcuri2014hitchhiker-e16]。

大白话 `[本项目分析]`：把 A、B 两组运行结果混在一起从小到大排序，看其中一组是不是系统性地排在前面。它只看排名，不要求结果服从正态分布。这一点很重要，因为搜索算法的结果分布常常高度偏斜[^arcuri2014hitchhiker-e7]。

报告所有 p 值，不论是否小于显著性水平，而不只说"显著"[^arcuri2014hitchhiker-e17]。

**2. Vargha-Delaney Â12 效应量：A 比 B 好多少？**

Â12 是"随机跑一次 A，结果比随机跑一次 B 更高"的概率。两者相当时 Â12 = 0.5；Â12 = 0.7 表示 70% 的情况下 A 的结果更高[^arcuri2014hitchhiker-e8]。

举例 `[本项目分析]`：假设 A 跑三次得 {42, 11, 7}，B 跑三次得 {1, 20, 5}。把 A 的每个结果和 B 的每个结果配对比较，共 3 × 3 = 9 对；A 更高的有 7 对（42 胜 3 对，11 和 7 各胜 2 对，都输给 20），没有平局，所以 Â12 = 7/9 ≈ 0.78（有平局时，每个平局算半对）。注意方向：指标越低越好（如运行时间）时，Â12 小于 0.5 才说明 A 更好 `[本项目分析]`。

**为什么两样都要**：显著性检验回答"能不能区分开"，效应量回答"差异是否大到值得关注"[^ralph2020empirical-e396]。跑几千次时，几乎任何差异都会显著[^arcuri2014hitchhiker-e9]，所以只报检验、不报效应量，是标准列出的反面模式[^ralph2020empirical-e392]。效应量要和检验配套：用基于排名的检验，就配基于排名的效应量（如 Â12），而不是"均值差除以标准差"[^arcuri2014hitchhiker-e10][^arcuri2014hitchhiker-e7]。

**还要注意：**

- **报告整个分布，而不只是平均数或中位数**，例如画箱线图[^ralph2020empirical-e388][^ralph2020empirical-e392]。
- **给效应量加置信区间**，例如用自助法（bootstrap，从已有结果中反复有放回地抽样来估计不确定性）[^arcuri2014hitchhiker-e18]。
- **比较两个以上的方法时，两两比较**，每对都做检验、都给效应量[^arcuri2014hitchhiker-e19]；比较次数多了要不要做多重比较校正，见[分析与解读](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

### 第六步：选问题实例，看能推广多远

**怎么做：**

1. **说清实例是怎么选的。** 选哪些程序、哪些数据集，对结果影响很大[^arcuri2014hitchhiker-e11]。很难拿到大量无偏、有代表性的实例，但一定要说明是怎么选出来的[^arcuri2014hitchhiker-e15][^ralph2020empirical-e385]。
2. **描述实例的特征和"难度"**，讨论各实例难在哪里[^ralph2020empirical-e385]。
3. **用合成数据要说明理由**：为什么不能用真实数据，结论在多大程度上适用于现实[^ralph2020empirical-e386]。
4. **逐个实例报告，不要只给总平均。** Arcuri & Briand 的例子：五个实例上的 Â12 是 0.6、0.6、0.6、0.6、0.1，平均下来是 0.5，看起来"没有差别"；实际上一个方法在四个实例上更好，在一个实例上差得多。应当分别报告，并尝试解释差异[^arcuri2014hitchhiker-e21]。

### 第七步：报告和公开

- 公开数据，或说明为什么不能公开（如保密协议）[^ralph2020empirical-e383]。
- 提供复现包：方法、解的表示和适应度计算的源代码，实验输入数据，输出日志和生成的解[^ralph2020empirical-e389]。
- 结果部分只写有证据的结果，解读和推测放到讨论部分[^ralph2020empirical-e388]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 优化研究标准。

**必须做到**

- [ ] 说明为什么问题无法在合理时间内靠人工或穷举解决[^ralph2020empirical-e377]
- [ ] 描述搜索空间；简化和约束符合实际，没有把问题简化到可以穷举[^ralph2020empirical-e378]
- [ ] 明确定义解的含义、表示和修改方式，以及所有适应度函数[^ralph2020empirical-e381]
- [ ] 说明为什么选这个算法[^ralph2020empirical-e379]
- [ ] 和合理的基线比较：新问题至少比随机搜索，否则比最先进的方法[^ralph2020empirical-e380]
- [ ] 写清每个方法的技术、启发式、参数及取值[^ralph2020empirical-e382]
- [ ] 说明数据集怎么收集和准备；公开数据或说明理由[^ralph2020empirical-e383]
- [ ] 找出所有随机性来源；带随机性的方法运行多次，或说明为什么做不到[^ralph2020empirical-e384]

**做到更好**

- [ ] 说明实例怎么选，描述实例特征和难度[^ralph2020empirical-e385]
- [ ] 解释参数取值的理由[^ralph2020empirical-e387]
- [ ] 用合适的统计方法比较分布，而不只是平均数[^ralph2020empirical-e388]
- [ ] 区分有证据的结果和推测[^ralph2020empirical-e388]
- [ ] 提供复现包[^ralph2020empirical-e389]

**做得出色**

- [ ] 分析不同参数选择的影响，说明最终参数怎么选出[^ralph2020empirical-e390]
- [ ] 分析适应度函数的"地形"（fitness landscape：好解和差解在解空间里怎样分布）[^ralph2020empirical-e390]

**这些情况可以不做，不算缺陷**

- 实验很耗时或有人参与时，只做有限几次试验；前提是披露局限、讨论随机性的影响[^ralph2020empirical-e391]

**审稿时常见、但不成立的批评**：你不必为此担心

- "只用了老算法"：老算法可以作为众多对比方法之一、作为性能的"底线"，或作为只改一处、其余不变的实验平台[^ralph2020empirical-e393]
- "没和某个方法比"，而那个方法不合适或拿不到可用的实现[^ralph2020empirical-e394]
- "多目标方法没和逐个目标单独优化的方法比"[^ralph2020empirical-e394]
- "研究对象太少"，而论文给了合理理由[^ralph2020empirical-e394]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不和随机搜索比较 | 无法排除"问题本身太简单"[^arcuri2014hitchhiker-e4] |
| 不报告搜索预算 | 读者无法判断搜索到底起了多大作用[^arcuri2014hitchhiker-e3] |
| 自己的方法调过参，对手用默认参数 | 只说明"用好 A 胜过用坏 B"[^menzies2019bad-e6] |
| 带随机性的方法只跑一次 | 结果可能只是运气[^arcuri2014hitchhiker-e1][^ralph2020empirical-e384] |
| 只报显著性检验，不报效应量 | 次数多时几乎什么都显著，看不出差异有多大[^ralph2020empirical-e392][^arcuri2014hitchhiker-e9] |
| 只报平均数或中位数，不给波动 | 隐藏了试验之间的差异[^ralph2020empirical-e392] |
| 对偏斜的结果用"均值差除以标准差"当效应量 | 分布偏斜时这种效应量失效[^arcuri2014hitchhiker-e7] |
| 只报所有实例的平均效应量 | 可能掩盖在个别实例上差得多的情况[^arcuri2014hitchhiker-e21] |
| 不说明实例怎么选 | 读者无法判断结果能推广到哪里[^arcuri2014hitchhiker-e15] |

---

## 5. 延伸阅读

- **ACM SIGSOFT Empirical Standards，Optimization Studies**：优化研究的检查清单，含审稿时不成立的批评。原文在 submodule `repos/acmsigsoft__EmpiricalStandards/docs/standards/OptimizationStudies.md`。
- **Arcuri & Briand 2014，A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms in Software Engineering**：怎样比较随机化算法的详细指南：运行次数、检验方法、效应量、多个研究对象的分析。第 11 节是可直接照做的实用建议。卢森堡大学机构库有作者存档版。它是 ICSE 2011 论文 `arcuri2011practical` 的扩展版。
- **Menzies & Shepperd 2019，"Bad smells" in software analytics papers**：数据驱动研究中的常见问题，包括不调参、不和简单方法比较。
- 计算机篇的相关实践：[基准评测](benchmarking.md)（公平配置、测量流程）、[工程研究](engineering_research.md)（提出并评估新方法）。

[^ralph2020empirical-e374]: SIGSOFT 优化研究标准，定义与适用范围。[证据](../../../../sources/notes/ralph2020empirical.md#e374)
[^ralph2020empirical-e375]: SIGSOFT 优化研究标准，脚注 3。[证据](../../../../sources/notes/ralph2020empirical.md#e375)
[^ralph2020empirical-e376]: SIGSOFT 优化研究标准，脚注 1。[证据](../../../../sources/notes/ralph2020empirical.md#e376)
[^ralph2020empirical-e377]: SIGSOFT 优化研究标准，必要项及脚注 4。[证据](../../../../sources/notes/ralph2020empirical.md#e377)
[^ralph2020empirical-e378]: SIGSOFT 优化研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e378)
[^ralph2020empirical-e379]: SIGSOFT 优化研究标准，必要项及脚注 6。[证据](../../../../sources/notes/ralph2020empirical.md#e379)
[^ralph2020empirical-e380]: SIGSOFT 优化研究标准，必要项及脚注 7。[证据](../../../../sources/notes/ralph2020empirical.md#e380)
[^ralph2020empirical-e381]: SIGSOFT 优化研究标准，必要项及脚注 8、9。[证据](../../../../sources/notes/ralph2020empirical.md#e381)
[^ralph2020empirical-e382]: SIGSOFT 优化研究标准，必要项及脚注 10。[证据](../../../../sources/notes/ralph2020empirical.md#e382)
[^ralph2020empirical-e383]: SIGSOFT 优化研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e383)
[^ralph2020empirical-e384]: SIGSOFT 优化研究标准，必要项及脚注 12、13。[证据](../../../../sources/notes/ralph2020empirical.md#e384)
[^ralph2020empirical-e385]: SIGSOFT 优化研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e385)
[^ralph2020empirical-e386]: SIGSOFT 优化研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e386)
[^ralph2020empirical-e387]: SIGSOFT 优化研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e387)
[^ralph2020empirical-e388]: SIGSOFT 优化研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e388)
[^ralph2020empirical-e389]: SIGSOFT 优化研究标准，加分项及脚注 14。[证据](../../../../sources/notes/ralph2020empirical.md#e389)
[^ralph2020empirical-e390]: SIGSOFT 优化研究标准，优秀项。[证据](../../../../sources/notes/ralph2020empirical.md#e390)
[^ralph2020empirical-e391]: SIGSOFT 优化研究标准，可接受的偏离。[证据](../../../../sources/notes/ralph2020empirical.md#e391)
[^ralph2020empirical-e392]: SIGSOFT 优化研究标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e392)
[^ralph2020empirical-e393]: SIGSOFT 优化研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e393)
[^ralph2020empirical-e394]: SIGSOFT 优化研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e394)
[^ralph2020empirical-e395]: SIGSOFT 优化研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e395)
[^ralph2020empirical-e396]: SIGSOFT 优化研究标准，Notes。[证据](../../../../sources/notes/ralph2020empirical.md#e396)
[^arcuri2014hitchhiker-e1]: Arcuri & Briand 2014，§1。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e1)
[^arcuri2014hitchhiker-e2]: Arcuri & Briand 2014，摘要。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e2)
[^arcuri2014hitchhiker-e3]: Arcuri & Briand 2014，§3。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e3)
[^arcuri2014hitchhiker-e4]: Arcuri & Briand 2014，§3。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e4)
[^arcuri2014hitchhiker-e5]: Arcuri & Briand 2014，§4。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e5)
[^arcuri2014hitchhiker-e6]: Arcuri & Briand 2014，§4。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e6)
[^arcuri2014hitchhiker-e7]: Arcuri & Briand 2014，§7。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e7)
[^arcuri2014hitchhiker-e8]: Arcuri & Briand 2014，§7。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e8)
[^arcuri2014hitchhiker-e9]: Arcuri & Briand 2014，§8。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e9)
[^arcuri2014hitchhiker-e10]: Arcuri & Briand 2014，§8。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e10)
[^arcuri2014hitchhiker-e11]: Arcuri & Briand 2014，§10.1。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e11)
[^arcuri2014hitchhiker-e12]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e12)
[^arcuri2014hitchhiker-e13]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e13)
[^arcuri2014hitchhiker-e14]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e14)
[^arcuri2014hitchhiker-e15]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e15)
[^arcuri2014hitchhiker-e16]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e16)
[^arcuri2014hitchhiker-e17]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e17)
[^arcuri2014hitchhiker-e18]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e18)
[^arcuri2014hitchhiker-e19]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e19)
[^arcuri2014hitchhiker-e20]: Arcuri & Briand 2014，§11。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e20)
[^arcuri2014hitchhiker-e21]: Arcuri & Briand 2014，§10.2。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e21)
[^menzies2019bad-e5]: Menzies & Shepperd 2019，§4.10。[证据](../../../../sources/notes/menzies2019bad.md#e5)
[^menzies2019bad-e6]: Menzies & Shepperd 2019，§4.10。[证据](../../../../sources/notes/menzies2019bad.md#e6)
[^menzies2019bad-e7]: Menzies & Shepperd 2019，§4.11。[证据](../../../../sources/notes/menzies2019bad.md#e7)
[^menzies2019bad-e8]: Menzies & Shepperd 2019，§4.4。[证据](../../../../sources/notes/menzies2019bad.md#e8)
