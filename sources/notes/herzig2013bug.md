# Herzig、Just、Zeller 2013：It's Not a Bug, It's a Feature: How Misclassification Impacts Bug Prediction

- 资料：`herzig2013bug`，[原文](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf)
- 版本：ICSE 2013 会议论文，作者所在的萨尔大学软件工程组主页发布的版本；原站当前无法访问，读取的是 Internet Archive 存档 `https://web.archive.org/web/2019id_/https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf`。

### E1

- 位置：摘要
- 原文："we found 33.8% of all bug reports to be misclassified—that is, rather than referring to a code fix, they resulted in a new feature, an update to documentation, or an internal refactoring." / "On average, 39% of files marked as defective actually never had a bug."
- 要点：人工检查五个开源项目 7000 多份问题报告，33.8% 标为"缺陷"的报告其实是新功能、文档更新或重构；平均 39% 被标为有缺陷的文件其实从未有过缺陷。

### E2

- 位置：§I Introduction
- 原文："However, all this assumes that the category of the issue report is accurate."
- 要点：用数据库查询筛出"缺陷"报告看似简单，但前提是报告的分类是准确的。

### E3

- 位置：Fig. 1；§XI Threats to Validity
- 原文："Second author classifies all reports marked as misclassified by first author (without knowing the new category)." / "we chose a setup that ensures that every misclassified bug report is cross-validated and that classification conflicts have to pass a third inspection."
- 要点：人工分类流程：第一作者分类，第二作者在不知道第一作者结论的情况下复核，有冲突的再做第三次检查。

### E4

- 位置：§XI Threats to Validity
- 原文："There exists no clear definition-separating feature and improvement requests." / "We counter this threat by listing the complete rules verbatim."
- 要点：类别之间的界限本身不清楚，换一套分类规则会改变结果；作者的应对是逐字公开完整的分类规则。

### E5

- 位置：§XII Conclusion and Consequences
- 原文："automated quantitative analysis should always include human qualitative analysis of the input data—and of the findings. Approaches relying on bug datasets should be preceded by a careful manual validation of data quality; at least of a significant sample. Data quality should be discussed as a threat to validity."
- 要点：自动化的定量分析应始终包括人对输入数据和结论的定性检查；使用缺陷数据集之前，至少要人工验证足够多的样本，并把数据质量作为效度威胁来讨论。
