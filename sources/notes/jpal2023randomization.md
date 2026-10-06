# J-PAL 研究资源：Randomization

- 资料：`jpal2023randomization`，[原文网页](https://www.povertyactionlab.org/resource/randomization)
- 版本：J-PAL 研究资源页，作者 Sarah Kopper、Anja Sautmann，2023 年 9 月更新；2026 年 10 月访问。位置写小标题。

### E1

- 位置：Choosing the unit of randomization
- 原文："At a minimum, the unit of randomization should be the unit at which the treatment will be delivered, and ideally at a unit that minimizes spillovers (see below) as well as evaluation-driven effects"
- 要点：随机化单位至少要是干预实际发放的单位，最好还能把溢出和"因被评估而改变行为"的影响降到最低。

### E2

- 位置：Choosing the unit of randomization
- 原文："In general, moving up in level of randomization decreases the study’s effective sample size, meaning that more observational units are required to achieve a given level of power."
- 要点：随机化层级越高，有效样本量越小，要达到同样功效需要更多观测单位。

### E3

- 位置：Randomization designs to estimate spillover effects
- 原文："This is done by randomizing at the cluster level and varying the “intensity” of treatment for the cluster, that is, the share of observational units in the cluster that receive the treatment, and then measuring treatment effects on both treated and untreated units within the cluster."
- 要点：测溢出的一种设计：按群随机，并随机改变每个群里接受干预的比例，再分别测群内接受者和未接受者的效应。

### E4

- 位置：Stratified randomization
- 原文："Stratification variables should thus be ones you expect to be correlated with the outcome of interest, or those for which you are interested in differential or heterogeneous treatment effects."
- 要点：分层变量应选和结果相关的变量，或你想比较不同群体效应的变量。

### E5

- 位置：Randomization methods; Solutions/programming
- 原文："Typically, this would be done in statistical software such as Stata or R to ensure the randomization is replicable." / "Set the seed for the random number generator"
- 要点：随机分组通常用统计软件做，以保证可以复现；要设定随机数种子。

### E6

- 位置：Balance tests
- 原文："If you are testing for balance at the 5% level, you would expect to see statistically significant differences between the treatment and control groups in roughly 5% of your covariates simply by chance. Note, there is no clear rule for how many imbalanced variables is too many."
- 要点：在 5% 水平上检验平衡，纯属偶然也会有约 5% 的变量显著不同；多少个不平衡算太多，没有明确规则。

### E7

- 位置：Balance tests
- 原文："Balance tests may be most useful when there are reasons to doubt that the randomization was done correctly"
- 要点：有理由怀疑随机化没有做对时，平衡检验最有用。

### E8

- 位置：Solutions to imbalance
- 原文："An alternative approach is to consider before implementing randomization whether there are covariates on which imbalance would not be acceptable and stratifying on them, so that balance on key covariates is achieved by construction (Athey & Imbens 2017)."
- 要点：与其抽到不平衡再重抽，不如事先想好哪些变量绝不能不平衡，直接按它们分层。

### E9

- 位置：Balance tests
- 原文："Balance test regressions should use the same specification as your final regression when possible."
- 要点：平衡检验的回归设定，尽量和最终分析的回归一致（如分层随机就加入分层固定效应）。
