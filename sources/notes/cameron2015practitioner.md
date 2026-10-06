# Cameron & Miller 2015：A Practitioner's Guide to Cluster-Robust Inference

- 资料：`cameron2015practitioner`，[作者主页 PDF](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf)；正式版发表于 Journal of Human Resources 50(2)，2015
- 版本：作者主页上的定稿前版本（2015 年 2 月）。位置写小节。

### E1

- 位置：摘要
- 原文："In such settings default standard errors can greatly overstate estimator precision. Instead, if the number of clusters is large, statistical inference after OLS should be based on cluster-robust standard errors."
- 要点：误差在组内相关时，默认标准误会严重高估估计的精度；聚类数量多时，应使用聚类稳健标准误。

### E2

- 位置：§I Introduction
- 原文："It is not unusual to have applications where standard errors that control for within-cluster correlation are several times larger than default standard errors that ignore such correlation."
- 要点：考虑组内相关后的标准误，比默认标准误大好几倍，并不少见。

### E3

- 位置：§I Introduction
- 原文："A leading example, highlighted by Moulton (1986, 1990), is when interest lies in measuring the effect of a policy variable, or other aggregated regressor, that takes the same value for all observations within a cluster."
- 要点：典型情形：要估计的是政策变量这类在同一组内取值都一样的变量的效应。

### E4

- 位置：§I Introduction
- 原文："There is no clear-cut definition of "few"; depending on the situation "few" may range from less than 20 to less than 50 clusters in the balanced case." / "without adjustment, test statistics based on the cluster-robust standard errors over-reject and confidence intervals are too narrow."
- 要点：聚类"太少"没有明确界线，视情况在少于 20 到少于 50 个（各组大小相近时）之间；聚类太少又不加修正，检验会过多拒绝原假设，置信区间过窄。

### E5

- 位置：§I Introduction
- 原文："who pointed out that many differences-in-differences studies failed to control for clustered errors, and those that did often clustered at the wrong level."
- 要点：（转述 Bertrand、Duflo 和 Mullainathan 2004）许多双重差分研究没有处理组内相关的误差，处理了的也常在错误的层级上聚类。
