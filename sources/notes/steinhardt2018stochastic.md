# Steinhardt 2018：Research as a Stochastic Decision Process

- 资料：`steinhardt2018stochastic`，[原文](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html)
- 版本：个人网页，2018

### E1

- 位置：开篇
- 原文："Throughout, I draw my examples primarily from problems in machine learning and mathematics, but I believe that the principles generalize to other situations as well."
- 要点：例子主要来自机器学习和数学，作者认为原则适用于其他情境。

### E2

- 位置：Warm-Up
- 原文："I would do all the easy parts, then get to the hard part and encounter a fundamental obstacle that required scrapping the entire plan and coming up with a new one."
- 要点：从易到难的做法常常导致：做完所有简单部分，才在难的部分遇到根本障碍，整个计划推倒重来。

### E3

- 位置：Warm-Up
- 原文："Rather, we should prioritize tasks that are more likely to fail (so that we remove the risk of them failing) but also tasks that take less time (so that we've wasted less time if one of the tasks does fail, and also so that we get information about tasks more quickly)."
- 要点：应优先做更可能失败的任务，同时优先做耗时短的任务，这样失败时浪费更少，也能更快得到信息。

### E4

- 位置：A Better Strategy: Sorting by Information Rate
- 原文："Do the components in order from most informative per unit time to least informative per unit time."
- 要点：按"单位时间获得的信息量"从高到低排列各部分工作。

### E5

- 位置：A further improvement: opening up the "task" black box
- 原文："Specifically, for each task we want a cheap way to obtain high confidence about whether that task will be feasible. This is called "de-risking". The following pattern is indispensable: (Basic Pattern) De-risk all components (to the extent feasible), then execute."
- 要点：对每个任务，先找便宜的方法判断它是否可行，这叫"去风险"；基本模式是先给所有部分去风险，再执行。

### E6

- 位置：A further improvement
- 原文："To avoid this issue, we could first download a few thousand examples. We can then examine several examples by hand, as well as compute some aggregate statistics, to assess whether the dataset has the properties we want."
- 要点：例子：在花大力气准备整个数据集之前，先取几千条，手工看一些、算一些统计量，判断数据是否符合需要。

### E7

- 位置：Some further practical ideas
- 原文："The counterpart to ceilings are baselines--simple or off-the-shelf methods that give a quick lower bound on achievable accuracy. Baselines provide an important sanity check, as complicated methods often underperform simple baselines."
- 要点：基线（简单或现成的方法）给出可达到效果的下限，是重要的合理性检查，复杂方法常常不如简单基线。

### E8

- 位置：Some further practical ideas
- 原文："More generally, thinking about simplified instances of a problem is often useful. This is because it provides intuition that often suggests/rules out approaches for the original problem."
- 要点：先思考问题的简化版本，往往能提示或排除原问题的解决思路。

### E9

- 位置：Exponentially branching search trees
- 原文："Whenever something doesn't work, I ask why it didn't work. My goal is to avoid trying similar things that will fail for the same reason"
- 要点：每次失败都追问原因，以免反复尝试会因同样原因失败的做法。

### E10

- 位置：Exponentially branching search trees
- 原文："When an experiment fails, it is tempting to conclude "I tried X and it didn't work". However, if X is a high-level conceptual approach, then a more correct conclusion is "I tried an implementation comprising 0.1% of the possible implementations of X, and observed that that particular implementation did not work"."
- 要点：一次实验失败，只说明 X 的某一种具体实现不行，不说明 X 这个思路不行。

### E11

- 位置：Exponentially branching search trees
- 原文："For this reason, I am far less in favor than most people of publishing negative results, unless the negative result comes with insight into what caused the failure."
- 要点：因此作者比多数人更不赞成发表负面结果，除非它附带了对失败原因的洞见。

### E12

- 位置：Summary
- 原文："We often try easier tasks first, when instead we should try the most informative tasks first. [...] We are often too slow to try to disprove our own ideas."
- 要点：常见的错误直觉：先做容易的任务，而不是信息量最大的任务；太迟才去尝试否定自己的想法。

### E13

- 位置：Additional Discussion
- 原文："I am also not advocating for the failure mode of only trying low-variance ideas, or of avoiding projects that lack an obviously promising approach."
- 要点：去风险不等于只做稳妥的想法；能系统地排除想法，恰恰让人可以去尝试成功概率低的想法。

### E14

> 已作废：与 [E5](#e5) 重复（原文被 E5 完整包含）。

- 位置：A further improvement: opening up the "task" black box
- 原文："Specifically, for each task we want a cheap way to obtain high confidence about whether that task will be feasible. This is called "de-risking"."
- 要点：去风险（de-risking）的定义：为每个任务找一个便宜的办法，尽快高把握地判断它是否可行。

### E15

> 已作废：与 [E5](#e5) 重复（原文被 E5 完整包含）。

- 位置：A further improvement: opening up the "task" black box
- 原文："De-risk all components (to the extent feasible), then execute."
- 要点：基本模式：先对所有部分去风险，再正式执行。

### E16

- 位置：Caveats
- 原文："You can get better at this within a few weeks by estimating completion times for each task and then recording the actual completion times in a daily log. You should also practice decomposing tasks into small actionable chunks, each taking roughly 20 minutes to 2 hours."
- 要点：估时可以练：每个任务先估时间，再在每日日志里记下实际用时；并练习把任务拆成 20 分钟到 2 小时的小块。

### E17

> 已作废：与 [E8](#e8) 重复（原文被 E8 完整包含）。

- 位置：Some further practical ideas
- 原文："More generally, thinking about simplified instances of a problem is often useful."
- 要点：思考问题的简化版本通常很有用，能帮助提出或排除方法。

### E18

- 位置：Some further practical ideas
- 原文："Running simulations. If we wish to prove X, first run simulations to check if X is actually true."
- 要点：理论工作也能去风险：想证明 X 之前，先跑模拟看 X 是否真的成立。

### E19

> 已作废：与 [E9](#e9) 重复（原文被 E9 完整包含）。

- 位置：Exponentially branching search trees
- 原文："Whenever something doesn't work, I ask why it didn't work."
- 要点：每次失败都追问原因，以免反复尝试因同一原因失败的做法。

### E20

> 已作废：与 [E10](#e10) 重复（原文被 E10 完整包含）。

- 位置：Exponentially branching search trees
- 原文："However, if X is a high-level conceptual approach, then a more correct conclusion is "I tried an implementation comprising 0.1% of the possible implementations of X, and observed that that particular implementation did not work"."
- 要点：一次实验失败只说明"这一种实现"不行，不能等同于"这个思路"不行。

### E21

- 位置：Exponentially branching search trees
- 原文："In the past, I have spent months trying different approaches to a problem before finally stepping back and realizing that they were all failing for the same reason."
- 要点：作者曾花几个月尝试不同方法，最后才退后一步发现它们失败的原因相同。

### E22

- 位置：Additional Discussion
- 原文："When ruling out ideas, it is important to hold oneself to a high standard. "This doesn't seem like it will work" or "I feel less motivated after trying a few things along this line that didn't work" are not ruling out an idea."
- 要点：否定一个想法要有高标准；"看起来不行""试了几次没动力了"都不算真正排除了它。

### E23

> 已作废：与 [E12](#e12) 重复（原文被 E12 完整包含）。

- 位置：Summary
- 原文："We often try easier tasks first, when instead we should try the most informative tasks first."
- 要点：人们常先做容易的任务，其实应当先做信息量最大的任务。
