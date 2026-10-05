# Klees 等人 2018：Evaluating Fuzz Testing

- 资料：`klees2018evaluating`，[原文](https://arxiv.org/abs/1808.09700)
- 版本：arXiv:1808.09700v2（CCS 2018），本地 PDF `papers/pdf/klees2018evaluating.pdf`。
- 说明：模糊测试（fuzz testing，用大量随机生成的输入测试程序以发现缺陷）属于软件安全方向。文中关于基线、评测程序、指标、重复次数的分析，是"怎样评估一个新工具"的典型例子。

### E1

- 位置：§1 Introduction
- 原文："When a researcher develops a new fuzzer algorithm (call it A), they must empirically demonstrate that it provides an advantage over the status quo. To do this, they must choose:" / "a compelling baseline fuzzer B to compare against" / "a sample of target programs—the benchmark suite" / "a meaningful set of configuration parameters"
- 要点：评估一个新的模糊测试算法，要选定：有说服力的基线、一组评测程序（基准套件）、性能指标、有意义的配置参数（如初始输入和运行时长），并考虑随机性。

### E2

- 位置：Abstract
- 原文："We surveyed the recent research literature and assessed the experimental evaluations carried out by 32 fuzzing papers. We found problems in every evaluation we considered."
- 要点：作者检查了 32 篇模糊测试论文的实验评估，每一篇都有问题。

### E3

- 位置：§9 Conclusions and Future Work
- 原文："Our experiments showed AFLFast performs well on the targets it was originally assessed against, but performed no better than AFL on two targets used by other papers."
- 要点：一个已发表的新工具在原论文选的程序上表现好，换成别的论文用过的两个程序，就不比基线好了。

### E4

- 位置：§9 Conclusions and Future Work
- 原文："Many papers measured fuzzer performance not by counting distinct bugs, but instead by counting “unique crashes” using heuristics" / "the heuristics can dramatically over-count the number of bugs, and indeed may suppress bugs by wrongly grouping crashing inputs. This means that apparent improvements may be modest or illusory."
- 要点：很多论文用"不同崩溃数"这种启发式指标代替"真实缺陷数"，而这种指标会严重多算缺陷，表面上的提升可能很小甚至不存在。

### E5

- 位置：§9 Conclusions and Future Work
- 原文："multiple trials with statistical tests to distinguish distributions" / "a range of benchmark target programs with known bugs" / "a consideration of various (well documented) seed choices including empty seed" / "timeouts of at least 24 hours, or else justification for less, with performance plotted over time"
- 要点：作者的建议：多次运行并做统计检验；用一系列已知缺陷的评测程序；以已知缺陷数衡量性能；考虑多种有记录的初始输入；运行至少 24 小时或说明理由，并画出随时间的变化。

### E6

- 位置：§1 Introduction
- 原文："Fuzzing performance can vary over the course of a run. This means that short timeouts (of less than 5 or 6 hours, as used by 11 papers) may paint a misleading picture."
- 要点：性能会随运行时间变化，运行时间太短可能得出误导性的结论；文中有例子在 6 小时时一方领先、24 小时时反过来。

### E7

- 位置：§8 Target Programs
- 原文："If a static benchmark suite comes into common use, tools may start to employ heuristics and strategies that are not of fundamental advantage, but apply disproportionately to the benchmark programs."
- 要点：一套固定的基准用久了，工具会开始针对它做特殊优化，这些优化并没有根本性的好处。

### E8

- 位置：§5 Seed Selection
- 原文："Papers should be specific about how the seeds were collected, and better still to make available the actual seeds used."
- 要点：论文要具体说明初始输入是怎么得到的，最好把实际用的初始输入公开。

### E9

- 位置：§1 Introduction
- 原文："Fuzzing performance under the same configuration can vary substantially from run to run."
- 要点：同样的配置，每次运行的结果可能差别很大。

### E10

- 位置：§1 Introduction
- 原文："An evaluation should also account for the fundamentally random nature of fuzzing" / "an evaluation should measure sufficiently many trials to sample the overall distribution that represents the fuzzer's performance, using a statistical test to determine that A's measured improvement over B is real, rather than due to chance."
- 要点：模糊测试本质上是随机的，评估要做足够多次试验来描述性能的分布，并用统计检验确认 A 比 B 的改进是真实的，而不是偶然。

### E11

- 位置：§1 Introduction
- 原文："on nm, one AFL run found just over 1200 crashing inputs while one AFLFast run found around 800. Yet, comparing the median of 30 runs tells a different story: 400 crashes for AFL and closer to 1250 for AFLFast."
- 要点：只比较单次运行会得出相反的结论：单次运行 AFL 比 AFLFast 找到更多崩溃，30 次运行的中位数却是 AFLFast 远多于 AFL。

### E12

- 位置：§1 Introduction
- 原文："short timeouts (of less than 5 or 6 hours, as used by 11 papers) may paint a misleading picture."
- 要点：性能在一次运行过程中会变化，过短的超时（少于 5～6 小时）可能给出误导的结论；有的比较在 6 小时和 24 小时时结论相反。

### E13

- 位置：§1 Introduction
- 原文："We similarly found substantial performance variations based on the seeds used" / "most papers treated the choice of seed casually, apparently assuming that any seed would work equally well, without providing particulars."
- 要点：初始输入（种子）不同，性能差异很大；但多数论文随意选择种子，似乎认为任何种子都一样，也不给出细节。

### E14

- 位置：§4 Statistically Sound Comparisons
- 原文："Mann Whitney is non parametric in that it makes no assumption about the distribution of a randomized algorithm's performance; by contrast, the standard t-test assumes a normal distribution."
- 要点：对随机化算法，建议用 Mann-Whitney U 检验：它是非参数检验，不对性能分布做假设；常用的 t 检验则假设正态分布。

### E15

- 位置：§4 Statistically Sound Comparisons
- 原文："Just because A is likely to be better than B doesn't tell us how much better it is." / "Bootstrap methods can also be employed here."
- 要点：知道 A 可能比 B 好，不等于知道好多少，还要估计效应量；可以用 Vargha-Delaney A12 统计量或自助法（bootstrap）。

### E16

- 位置：§9 Conclusions
- 原文："multiple trials with statistical tests to distinguish distributions" / "a range of benchmark target programs with known bugs" / "measurement of performance in terms of known bugs, rather than heuristics based on AFL coverage profiles or stack hashes" / "timeouts of at least 24 hours, or else justification for less, with performance plotted over time"
- 要点：建议的评估要素：多次试验加统计检验；一组含已知缺陷的目标程序；以已知缺陷数衡量性能，而不是启发式指标；至少 24 小时的超时（或说明更短的理由），并画出性能随时间的变化；考虑多种有文档记录的种子选择，包括空种子。

### E17

- 位置：§9 Conclusions
- 原文："the heuristics can dramatically over-count the number of bugs, and indeed may suppress bugs by wrongly grouping crashing inputs."
- 要点：用"唯一崩溃数"等启发式方法去重，可能大大多算缺陷数，也可能错误地合并而漏掉缺陷，因此看到的改进可能很小甚至是假的。

### E18

- 位置：§9 Conclusions
- 原文："Our experiments showed AFLFast performs well on the targets it was originally assessed against, but performed no better than AFL on two targets used by other papers." / "which have the advantage that they are defined independently of a given algorithm"
- 要点：AFLFast 在原论文选的目标程序上表现好，在其他论文用的两个目标上并不比 AFL 好。合成的基准套件（如 CGC、LAVA-M）的好处是独立于具体算法定义，缺陷能可靠计数。

### E19

- 位置：§1 Introduction
- 原文："We found that no fuzz testing evaluation carries out all of the above steps properly (though some get close)."
- 要点：被调查的 32 篇论文中，没有一篇的评估把所有步骤都做对了。
