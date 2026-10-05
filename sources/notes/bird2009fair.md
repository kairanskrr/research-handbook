# Bird 等人 2009：Fair and Balanced? Bias in Bug-Fix Datasets

- 资料：`bird2009fair`，[原文](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009fbb.pdf)
- 版本：ESEC/FSE 2009 会议论文，Microsoft Research 网站上的作者版本。

### E1

- 位置：摘要
- 原文："only a fraction of bug fixes are actually labelled in source code version histories, and thus become available for study in the extracted datasets." / "we investigate historical data from several software projects, and find strong evidence of systematic bias."
- 要点：只有一部分缺陷修复在版本历史中被标注出来，进入研究数据集；作者在多个项目中发现了系统性偏差。

### E2

- 位置：§1 Introduction
- 原文："However, there is no standard or enforced practice to link a particular source code change to the corresponding entry in the bug database. Linkages, sadly, are irregular and inconsistent."
- 要点：没有统一或强制的做法把代码修改链接到缺陷库中的条目，链接是不规则、不一致的。

### E3

- 位置：§1 Introduction
- 原文："Hypothesis-testing on this dataset might lead to the incorrect conclusion that more experienced developers make more mistakes"
- 要点：如果有经验的开发者更认真地标注修复，基于这类数据检验假设，可能得出"越有经验的开发者犯错越多"的错误结论。

### E4

- 位置：§4 Data Gathering，Linking the Data Sources
- 原文："Scan through the commit messages for numbers in a given format" / "Exclude all false-positive numbers (e.g., release numbers, year dates, etc.), which have a defined format." / "Check if the potential reference number exists in the bug database." / "Check if the referenced bug report has a fixing activity 7 days before or 7 days past the commit date."
- 要点：常见的提交–缺陷链接方法：在提交信息中找特定格式的编号，排除版本号、年份等误报，确认编号在缺陷库中存在，并检查缺陷是否在提交前后 7 天内有修复活动。

### E5

- 位置：§4 Data Gathering，Linking the Data Sources
- 原文："As additional verification, we manually inspected the results of our scan, looking for both false positives and false negatives."
- 要点：作者对自动链接结果做了人工抽查，既查误报（错链），也查漏报（漏链）。
