# Fabijan 等 2019：Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners

- 资料：`fabijan2019diagnosing`，[原文（作者团队网站 PDF）](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf)
- 版本：KDD 2019（美国安克雷奇）论文的作者版 PDF，DOI 10.1145/3292500.3330722。作者来自微软、Booking.com 和 Outreach.io，基于四家公司的案例研究（访谈 14 人、分析一万多个历史实验）。位置只写章节。

### E1

- 位置：§2.3.1 Sample Ratio Mismatch
- 原文："While there are many data quality issues that could decrease the validity and significance of a controlled experiment, Sample Ratio Mismatch in most cases completely invalidates experiment results. For example, a ratio of 50.2/49.8 (821,588 versus 815,482 users) diverges enough from an expected 50/50 ratio that the probability that it happened by chance is less than 1 in 500k."
- 要点：样本比例不匹配多数时候会让实验结果完全无效；例如 50.2/49.8（821,588 对 815,482 个用户）偏离预期的 50/50，纯属偶然的概率不到五十万分之一。

### E2

- 位置：§2.3.1 Sample Ratio Mismatch
- 原文："To detect an SRM, a chi-square test [30] can be used. If the test determines an unlikely difference between the configured and observed numbers, analysts must investigate the root cause."
- 要点：用卡方检验发现样本比例不匹配；检验显示配置人数和实际人数的差异不太可能是偶然时，必须查出根本原因。

### E3

- 位置：§4.1 SRMs are a Common Data Quality Issue
- 原文："During this study, and through quantitative analysis of experiments conducted within the last year we identified that approximately 6% of experiments at Microsoft exhibit an SRM."
- 要点：微软近一年的实验中，大约 6% 出现样本比例不匹配。

### E4

- 位置：§4.2 SRMs Indicate Invalid Analysis
- 原文："In particular, SRMs cause a selection bias that invalidates any causal inference that could be drawn from the experiment."
- 要点：样本比例不匹配带来选择偏差，使实验得出的任何因果推断都无效。

### E5

- 位置：§4.3 SRMs are Challenging to Root-Cause
- 原文："The time to diagnose an SRM can span from minutes to months, and SRMs can happen due to issues with experiment design, the randomization process, variant deployment, data logging, data collection, data cooking, as well as due to data analysis conditions."
- 要点：诊断一次样本比例不匹配可能要几分钟到几个月；原因可能出在实验设计、随机化、版本部署、数据记录、收集、加工和分析条件等任何环节。

### E6

- 位置：§1 Introduction
- 原文："After resolving the issue that was causing the SRM in experiment above (see section 5.3 for details), it was found that the change was in fact positive and significantly increased the engagement with the product."
- 要点：MSN 轮播图实验最初显示用户参与度下降，解决了导致样本比例不匹配的问题后，发现改动其实是正面的，显著提高了参与度。

### E7

- 位置：§5.1 Experiment Assignment SRMs
- 原文："For every A/B test, it is a best practice to compute results for the pre-period before the test started and confirm that a random split of users into two groups does not cause a large difference in key metrics. If it does, then the same metric in the A/B test period would carry over some of that bias."
- 要点：好的做法是先用实验开始前一段时间的数据算一遍，确认随机分出的两组在关键指标上本来就没有大差异；否则实验期间的指标会带着这份偏差。
