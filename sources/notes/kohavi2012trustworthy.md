# Kohavi 等 2012：Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained

- 资料：`kohavi2012trustworthy`，[原文（作者团队网站 PDF）](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf)
- 版本：KDD 2012（ACM SIGKDD 知识发现与数据挖掘会议，北京）论文的作者版 PDF，共 9 页。作者来自微软实验平台团队，例子主要来自必应搜索和 MSN。位置写 PDF 上印的页码。

### E1

- 位置：§1 Introduction，第 1 页
- 原文："In a controlled experiment, users are randomly split between the variants (e.g., the six designs for the Real Estate widget) in a persistent manner (a user receives the same experience in multiple visits) during the experiment period."
- 要点：在线对照实验把用户随机、而且持久地分到各版本：同一用户在实验期间多次访问，看到的都是同一个版本。

### E2

- 位置：§1 Introduction，第 2 页
- 原文："In the paper Online Experimentation at Microsoft [2], we shared the statistic that only one third of ideas tested at Microsoft improved the metric(s) they were designed to improve."
- 要点：在微软做过实验的想法里，只有三分之一改善了它本来想改善的指标。

### E3

- 位置：§2 Background and Terminology，第 3 页
- 原文："The A/A test has been our most useful tool in identifying issues in practical systems. We strongly recommend that every practical system continuously run A/A tests."
- 要点：A/A 测试是作者发现实际系统问题最有用的工具；强烈建议每个实验系统都持续跑 A/A 测试。

### E4

- 位置：§3.1.2 Puzzling Outcome，第 3 页
- 原文："When Bing had a bug in an experiment, which resulted in very poor results being shown to users, two key organizational metrics improved significantly: distinct queries per user went up over 10%, and revenue per user went up over 30%!"
- 要点：必应的一次实验因缺陷给用户显示了很差的搜索结果，两个关键业务指标反而显著上升：每用户查询数涨了 10% 以上，每用户收入涨了 30% 以上。

### E5

- 位置：§3.1.3 Explanation，第 4 页
- 原文："(If the ratio of users in the variants varies significantly from the design, it's a good indication of a bug.)"
- 要点：各组用户数的比例明显偏离设计比例，很可能说明有程序缺陷。

### E6

- 位置：§3.2.3 Explanation，第 4 页
- 原文："The "success" of getting users to click more was not real, but rather an instrumentation difference."
- 要点：一次实验里"用户点击更多"的成功并不真实，只是两组的数据埋点（记录用户行为的代码）丢数据的程度不同。

### E7

- 位置：§3.3.4 Lessons Learned，第 6 页
- 原文："Most experiments have a stable effect (constant mean), but the high variance means that we need to collect enough data to get better estimates; early results are often misleading."
- 要点：多数实验的效应其实是稳定的，但波动大，要收集足够数据；早期结果常常误导人。

### E8

- 位置：§3.3.1 Background，第 5 页
- 原文："The existence of Primacy and Novelty effects can be assessed by generating the delta graph (between Control and Treatment) over time, and evaluating trends, visually or analytically." / "But this is where our surprising result comes in: most cases of suspected Primacy and Novelty effects are not real, but just a statistical artifact."
- 要点：可以把两组差值随时间画出来，检查首因效应和新奇效应；但多数被怀疑的这类效应并不真实，只是统计上的假象。

### E9

- 位置：§3.4.2 Puzzling Outcome，第 6 页
- 原文："For some of our key metrics, including Sessions/user, the confidence interval of the percent effect does not shrink over time. Running the experiment longer does not provide additional statistical power for these metrics."
- 要点：对每用户会话数等一些关键指标，置信区间不会随实验时间变窄；对这些指标，跑得更久并不增加功效。

### E10

- 位置：§3.5.3 Explanation，第 7–8 页
- 原文："One big drawback with the "bucket system" is its vulnerability to carryover effects, where the same users who were impacted by the first experiment are being used for the follow-on experiment." / "Even after three months, the user buckets still had not fully recovered to their pre-experiment levels."
- 要点：反复使用同一批用户分桶的系统容易受遗留效应影响：上一个实验影响过的用户被用到下一个实验里；有一次三个月后这些用户还没恢复到实验前的水平。

### E11

- 位置：§4 Summary，第 8 页
- 原文："Instrumentation issues are related to the concept of measure validity, i.e., the extent to which the metric used captures the concept we intended to measure" / "Generating numbers is easy; generating numbers you should trust is hard!"
- 要点：埋点问题关系到测量效度，即指标在多大程度上测到了想测的概念；算出数字容易，算出值得信任的数字难。
