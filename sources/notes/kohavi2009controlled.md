# Kohavi 等 2009：Controlled experiments on the web: survey and practical guide

- 资料：`kohavi2009controlled`，[原文（作者主页 PDF）](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf)
- 版本：Data Mining and Knowledge Discovery 第 18 卷第 1 期，第 140–181 页，DOI 10.1007/s10618-008-0114-1（作者主页上的期刊版 PDF）。作者是微软实验平台团队成员。位置写期刊页码。

### E1

- 位置：§1 Introduction，第 142 页
- 原文："In the simplest manifestation of such experiments, live users are randomly assigned to one of two variants: (i) the Control, which is commonly the "existing" version, and (ii) the Treatment, which is usually a new version being evaluated."
- 要点：最简单的在线对照实验，是把真实用户随机分到两个版本：对照组（通常是现有版本）和处理组（要评估的新版本）。

### E2

- 位置：§3 Controlled experiments，第 149 页
- 原文："The key here is "random." Users cannot be distributed "any old which way" (Weiss 1997); no factor can influence the decision." / "If the experiment was designed and executed properly, the only thing consistently different between the two variants is the change between the Control and Treatment, so any differences in the OEC are inevitably the result of this assignment, establishing causality"
- 要点：关键在"随机"，任何因素都不能影响分组；设计和执行正确时，两组唯一系统性的不同就是这次改动，指标差异因此可以归因于改动。

### E3

- 位置：§3.1 Terminology，第 150 页
- 原文："Overall Evaluation Criterion (OEC) (Roy 2001). A quantitative measure of the experiment's objective." / "A good OEC should not be short-term focused (e.g., clicks); to the contrary, it should include factors that predict long-term goals, such as predicted lifetime value and repeat visits."
- 要点：总体评价指标是实验目标的量化度量；好的总体评价指标不应只看短期（如点击），而应包含能预测长期目标的因素，如用户的长期价值和回访。

### E4

- 位置：§3.1 Terminology，第 150 页
- 原文："selecting a single metric, possibly as a weighted combination of such objectives is highly desired and recommended (Roy 2001, p. 50). A single metric forces tradeoffs to be made once for multiple experiments and aligns the organization behind a clear objective."
- 要点：强烈建议选一个单一指标（可以是多个目标的加权组合）；这样权衡只需做一次，所有实验共用一个清楚的目标。

### E5

- 位置：§3.1 Terminology，第 150 页
- 原文："The units are assumed to be independent. On the web, the user is a common experimental unit, although some metrics may have user-day, user-session or page views as the experimental units. For any of these randomization by user is preferred. It is important that the user receive a consistent experience throughout the experiment, and this is commonly achieved through randomization based on user IDs stored in cookies."
- 要点：实验单位被假定相互独立；网上常以用户为单位，也有按用户日、会话、页面浏览的；无论哪种都优先按用户随机，让同一用户在整个实验中看到一致的版本，通常靠存在 cookie 里的用户编号实现。

### E6

- 位置：§3.1 Terminology，第 151 页
- 原文："Instead of an A/B test, you exercise the experimentation system, assigning users to one of two groups, but expose them to exactly the same experience. An A/A test can be used to (i) collect data and assess its variability for power calculations, and (ii) test the experimentation system (the Null hypothesis should be rejected about 5% of the time when a 95% confidence level is used)."
- 要点：A/A 测试照常把用户分成两组，但两组看到完全相同的版本；用途一是估计数据波动、供功效计算，二是检验实验系统本身（在 95% 置信水平下，应只有约 5% 的时候拒绝零假设）。

### E7

- 位置：§3.2.4 The choice of OEC must be made in advance，第 154 页
- 原文："When running experiments, it is important to decide in advance on the OEC (a planned comparison); otherwise, there is an increased risk of finding what appear to be significant results by chance (familywise type I error)"
- 要点：总体评价指标必须事先定好；否则更容易碰巧找到看似显著的结果。

### E8

- 位置：§3.2 Hypothesis testing and sample size，第 151 页
- 原文："Lower the variability of the OEC by filtering out users who were not exposed to the variants, yet were still included in the OEC. For example, if you make a change to the checkout page, analyze only users who got to the page, as everyone else adds noise, increasing the variability."
- 要点：把根本没接触到改动的用户排除出分析，可以降低指标波动；例如改了结账页，就只分析到达结账页的用户。

### E9

- 位置：§3.2.1 Example: impact of lower-variability OEC on the sample size，第 153 页
- 原文："If you are running an A/B test and want to detect a 5% change to revenue, you will need over 409,000 users to achieve the desired 80% power"
- 要点：文中的电商例子：想以 80% 的功效检测到收入 5% 的变化，需要 40.9 万以上用户。

### E10

- 位置：§3.4 Effect of robots on experimental results，第 155 页
- 原文："Robots can introduce significant skew into estimates, enough to render assumptions invalid. We have seen cases where robots caused many metrics to be significant when they should not have been (e.g., much more than 5% false positives for an A/A test)."
- 要点：机器人流量会严重扭曲估计；作者见过机器人让 A/A 测试的假阳性远超 5% 的情况。

### E11

- 位置：§3.5.1 Treatment ramp-up，第 156 页
- 原文："An experiment can be initiated with a small percentage of users assigned to the Treatment(s), and then that percentage can be gradually increased." / "At each step, which could run for, say, a couple of hours, you can analyze the data to make sure there are no egregious problems with the Treatment before exposing it to more users."
- 要点：实验可以先给很小比例的用户上线处理版本，逐步放大；每一步先检查有没有严重问题，再让更多用户看到。

### E12

- 位置：§3.6 Limitations，第 1 条，第 157 页
- 原文："It is possible to know which variant is better, and by how much, but not "why." In user studies, for example, behavior is often augmented with users' comments, and hence usability labs can be used to augment and complement controlled experiments (Nielsen 2005)."
- 要点：在线实验能告诉你哪个版本更好、好多少，但说不出"为什么"；可用性实验室里的用户研究能收集用户的评论，可以补充在线实验。

### E13

- 位置：§3.6 Limitations，第 2 条，第 157 页
- 原文："Controlled experiments measure the effect on the OEC during the experimentation period, typically a few weeks."
- 要点：在线实验测的是实验期间（通常几周）的效果。

### E14

- 位置：§3.6 Limitations，第 3 条，第 158 页
- 原文："If you change the navigation on a web site, experienced users may be less efficient until they get used to the new navigation, thus giving an inherent advantage to the Control. Conversely, when a new design or feature is introduced, some users will investigate it, click everywhere, and thus introduce a "newness" bias." / "One analysis that can be done is to compute the OEC only for new users on the different variants, since they are not affected by either factor."
- 要点：首因效应（老用户要适应新导航，开始时效率低，对照组占便宜）和新奇效应（用户对新设计到处点，结果偏好）方向相反；一种分析办法是只看新用户，因为他们不受这两种效应影响。

### E15

- 位置：§3.6 Limitations，第 4 条，第 158 页
- 原文："Nonetheless, the feature must be implemented and be of sufficient quality to expose users to it."
- 要点：在线实验要求功能已经实现，并且质量足以给真实用户使用。

### E16

- 位置：§5.1 Randomization algorithm，第 163–164 页
- 原文："End users must be equally likely to see each variant of an experiment (assuming a 50–50 split). There should be no bias toward any particular variant." / "Repeat assignments of a single end user must be consistent; the end user should be assigned to the same variant on each successive visit to the site." / "When multiple experiments are run, there must be no correlation between experiments."
- 要点：随机化算法必须满足三条：每个用户看到各版本的机会相等；同一用户每次访问都分到同一版本；同时运行的多个实验之间分组互不相关。

### E17

- 位置：§6.2.1 Run continuous A/A tests，第 174 页
- 原文："Run A/A tests (see Sect. 3.1) and validate the following. 1. Are users split according to the planned percentages? 2. Is the data collected matching the system of record? 3. Are the results showing non-significant results 95% of the time? Continuously run A/A tests in parallel with other experiments."
- 要点：A/A 测试要检查三件事：用户是否按计划比例分组；收集的数据是否和业务系统的记录一致；是否 95% 的时候结果不显著。并且要和其他实验并行、持续地跑。

### E18

- 位置：§6.2.3 Determine the minimum sample size，第 175 页
- 原文："Decide on the statistical power, the effect you would like to detect, and estimate the variability of the OEC through an A/A test. Based on this data you can compute the minimum sample size needed for the experiment and hence the running time for your web site. A common mistake is to run experiments that are underpowered."
- 要点：先定功效、想检测的效应大小，用 A/A 测试估计指标波动，再算出最小样本量和需要跑多久；常见错误是功效不足。

### E19

- 位置：§6.2.4 Assign 50% of users to treatment，第 175 页
- 原文："In order to maximize the power of an experiment and minimize the running time, we recommend that 50% of users see each of the variants in an A/B test." / "For example, if an experiment is run at 99%/1%, then it will have to run about 25 times longer than if it ran at 50%/50%."
- 要点：为了让功效最大、时间最短，建议两组各 50%；按 99%/1% 分流，要跑大约 25 倍长的时间。

### E20

- 位置：§6.2.5 Beware of day of week effects，第 175 页
- 原文："we strongly recommend running experiments for at least a week or two, then continuing by multiples of a week so that day-of-week effects can be analyzed."
- 要点：即使流量很大，也建议至少跑一到两周，并按整周延长，以便分析星期几的影响。

### E21

- 位置：§6.3.1 Agree on the OEC upfront，第 176 页
- 原文："it best serves this purpose when the interested parties have agreed on how an experiment is to be evaluated before the experiment is run."
- 要点：相关各方在实验开始前就商定怎样评价实验，实验才最能客观地衡量价值。

### E22

- 位置：§6.3.2 Beware of launching features that "do not hurt" users，第 176 页
- 原文："When an experiment yields no statistically significant difference between variants, this may mean that there truly is no difference between the variants or that the experiment did not have sufficient power to detect the change." / "It is possible that the experiment is negative but underpowered."
- 要点：结果不显著，可能真的没差别，也可能只是功效不够；"反正没坏处"就上线，可能上线了一个其实有害、只是没测出来的改动。

### E23

- 位置：Appendix A，第 1 条（eBay 拍卖的例子），第 178 页
- 原文："If some users have this incentive and others do not, the presence of the Treatment will affect all items so we cannot get a true measure of the effectiveness of making this change. In this case you can randomly assign one group of items in the auction to be in the Control and the rest to be in the Treatment and compare the OEC for these two groups. i.e. randomly assign the items in the auction, not the users."
- 要点：拍卖里一部分用户有激励、一部分没有时，处理会影响所有拍品，按用户随机测不准真实效果；这时改为随机分配拍品，而不是随机分配用户。

### E24

- 位置：Appendix A，第 2 条（价格弹性研究），第 179 页
- 原文："The usual randomization based on user is not desirable because bad customer relations could result if it's exposed that some customers are getting a different price than other customers (everything else being equal) as Amazon.com discovered when it ran such a study (Weiss 2000)."
- 要点：测价格时不宜按用户随机：一旦被发现不同顾客拿到不同价格，会伤害客户关系，亚马逊就遇到过；可以改为随机分配商品。

### E25

- 位置：§1 Introduction，第 142 页
- 原文："Unlike other methodologies, such as post-hoc analysis or interrupted time series (quasi experimentation) (Charles and Melvin 2004), this experimental design methodology tests for causal relationships"
- 要点：和事后分析、中断时间序列等准实验方法不同，对照实验检验的是因果关系。

### E26

- 位置：§2.4 Behavior-Based Search at Amazon，第 146 页
- 原文："The examples above changed User-Interface (UI) elements. This example deals with a backend algorithmic change, which is often overlooked as an area to apply controlled experiments."
- 要点：在线实验不只用于界面改动，也可以评估后台算法的改动（如搜索算法），这一点常被忽视。

### E27

- 位置：§3.3 Confidence intervals for absolute and percent effect，第 154 页
- 原文："It is useful to give a confidence interval for the difference in the means of the Treatment and Control in addition to the results of the hypothesis test. The confidence interval gives a range of plausible values for the size of the effect of the Treatment whereas the hypothesis test only determines if there is a statistically significant difference in the mean."
- 要点：除了假设检验结果，还应给出两组均值之差的置信区间；置信区间给出效应大小的合理范围，检验只说明差异是否显著。
