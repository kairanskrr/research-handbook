# Cunningham：Causal Inference: The Remix（在线第二版）

- 资料：`cunningham2026remix`，[作者免费在线版](https://mixtape.scunning.com/)；第一版为 Causal Inference: The Mixtape（Yale University Press，2021），在线版见 https://mixtape-1ed.netlify.app/
- 版本：2026 年 10 月 6 日读取的在线版。网站说明第二版在线版"仍在完善中"（work-in-progress），内容可能变动。摘录了第 6 章（断点回归）、第 7 章（工具变量）、第 9 章（双重差分基础）、第 10 章（复杂双重差分设计）、第 11 章（合成控制）；位置写章节标题。

### E1

- 位置：第 7 章 Instrumental Variables（The Problem of Weak Instruments 之后，弱工具变量的诊断一节）
- 原文："The number 10 is now widely seen as too low—especially in models with multiple endogenous regressors, heteroskedasticity, or non-normal errors."
- 要点：第一阶段 F 统计量大于 10 这条经验门槛，现在普遍被认为太低。

### E2

- 位置：第 7 章，同上
- 原文："So in summary—regarding weak instruments, your studies should report the Anderson-Rubin confidence intervals for robustness and use Olea and Pflueger (2013) effective \(F\)-statistic to assess instrument strength."
- 要点：作者的总结建议：报告 Anderson-Rubin 置信区间（不受工具强弱影响的置信区间），并用 Olea 和 Pflueger 的"有效 F 统计量"判断工具变量强弱。

### E3

- 位置：第 7 章（转引 Bound、Jaeger 和 Baker 1995，第 448 页）
- 原文："It is striking that the second-stage results reported in Table 3 look quite reasonable even with no information about educational attainment in the simulated instruments. They give no indication that the instruments were randomly generated."
- 要点：Bound 等人把真实工具变量换成随机生成的数字，第二阶段结果看起来仍然"相当合理"，完全看不出工具是随机编的。

### E4

- 位置：第 7 章（LATE 的假设一节）
- 原文："Note: unlike independence and exclusion, the first stage is testable as it is based solely on \(D\) and \(Z\), both of which you have data on."
- 要点：和独立性、排他性不同，第一阶段（工具变量是否真的改变了处理）可以用数据检验。

### E5

- 位置：第 7 章（LATE 的假设一节）
- 原文："As outlined above, with all five assumptions satisfied, IV estimates the average treatment effect for compliers, which is the parameter we've called the local average treatment effect."
- 要点：几条假设都满足时，工具变量估计的是"遵从者"（行为被工具变量改变的那部分人）的平均处理效应，即局部平均处理效应。

### E6

- 位置：第 7 章（如何向读者讲清工具变量一节）
- 原文："The problem with IV is that it has several untestable assumptions." / "Defeating the LATE merely requires creating doubt in someone's mind that exclusion holds."
- 要点：工具变量有好几条无法检验的假设；只要让人怀疑排他性约束，结论就站不住。

### E7

- 位置：第 7 章（Know Your Treatment Assignment Mechanism）
- 原文："Ask yourself why you think it's random? Why do you think it satisfies exclusion? Be your own worst critic."
- 要点：问自己：凭什么认为它是随机的？凭什么认为它满足排他性？做自己最严厉的批评者。

### E8

- 位置：第 7 章（Make Beautiful Figures of Your Instrument）
- 原文："What you want to therefore do is present to people the numerator and the denominator of that Wald estimator."
- 要点：要给读者看的是工具变量估计的"分子"和"分母"，即简约式（工具变量对结果的影响）和第一阶段（工具变量对处理的影响），而不只是最后的系数。

### E9

- 位置：第 9 章 Difference-in-Differences Fundamentals（Event Studies）
- 原文："The parallel trends assumption cannot be tested because it involves a non-existent counterfactual that cannot be observed." / "What's needed is that the post-treatment counterfactual trend in \(E[Y^0]\) for the treatment group be the same as the control group. That is not the same thing as requiring pretrends to be parallel."
- 要点：平行趋势涉及看不到的反事实，无法检验；真正需要的是处理之后的反事实趋势相同，这和"处理前趋势平行"不是一回事。

### E10

- 位置：第 9 章（The Importance of Falsifications in Diff-in-Diff）
- 原文："In diff-in-diff, falsifications are tests of alternative explanations for your results." / "There are roughly two kinds of falsification designs that people employ, which I call "same outcome, alternative groups" and "same group, alternative outcomes.""
- 要点：证伪检验是在检验其他解释。常见两类："同一结果、换一组人"和"同一组人、换一个结果"。

### E11

- 位置：第 10 章 Complex Diff-in-Diff Designs（Designing Your Diff-in-Diff by Checklist）
- 原文："Count the Units in Your Cohorts: Count the number of units that are treated in each cohort, including the cohort of never-treated and the cohort of always-treated." / "Plot Treatment Rollout: Visualize when and how treatment varies across units and time." / "Pick Your Control Group: Decide which units will serve as your counterfactual and justify that choice."
- 要点：作者的双重差分设计清单中的几步：数清每批（同一时间开始处理的）单位有多少，包括从未处理和一直处理的；画出处理随时间铺开的情况；选定对照组并说明理由。

### E12

- 位置：第 10 章（Designing Your Diff-in-Diff by Checklist）
- 原文："DDDiD, or "Don't Do Diff-in-Diff": Always fold a losing hand as soon as possible and move on to a different approach if you can—even if that means walking away from diff-in-diff."
- 要点：清单最后一步："别做双重差分"：手里的牌不行就尽早放弃，换别的方法。

### E13

- 位置：第 10 章（估计方法比较一节）
- 原文："As a general principle, if a researcher cannot select between two methods ex ante, they must use both to avoid \(p\)-hacking."
- 要点：如果事先没法在两种方法之间做选择，就两种都报告，以免挑结果。

### E14

- 位置：第 10 章（协变量选择一节）
- 原文："The key is being transparent about your choices and to make these choices well in advance of ever peeking at the results."
- 要点：关键是选择要透明，并且在看到结果之前很早就定下来。

### E15

- 位置：第 11 章 Synthetic Control（Cuba, Miami, and the Mariel Boatlift）
- 原文："But the problems with the study were that the selection of the control group was, in retrospect, ad hoc and therefore potentially subjective." / "The method is based on the observation that, when the units of analysis are a few aggregate units, a combination of comparison units (the "synthetic control") often does a better job of reproducing characteristics of a treated unit than using a single comparison unit alone."
- 要点：传统比较案例研究的问题是对照组挑得随意、可能主观。合成控制的出发点：分析单位是少数几个加总单位（如城市、州）时，多个对照单位的加权组合往往比单个对照更像处理单位。

### E16

- 位置：第 11 章（Synthetic Control from Alberto Abadie 一节）
- 原文："Unlike regression-based methods, synthetic control does not require access to post-treatment outcomes when constructing the counterfactual."
- 要点：构造合成控制时用不到处理之后的结果数据，有助于避免边看结果边调模型。

### E17

- 位置：第 11 章（推断一节）
- 原文："Recall that randomization inference involves reassigning the treatment to each untreated unit as if it had been treated, reestimating the model each time, and then collecting the resulting estimates into a distribution that forms the basis for inference."
- 要点：合成控制常用随机化推断：把每个未处理单位都假装成处理单位重做一遍，得到一组"安慰剂效应"，看真实效应在其中是否突出。

### E18

- 位置：第 11 章（推断一节）
- 原文："Abadie, Diamond, and Hainmueller (2010) recommend dropping the states whose pretreatment RMSPE is considerably different than California's"
- 要点：处理前拟合很差的安慰剂单位，Abadie 等人建议在比较时剔除（处理前拟合误差远大于处理单位的）。
