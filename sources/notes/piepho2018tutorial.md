# Piepho、Edmondson 2018：A tutorial on the statistical analysis of factorial experiments with qualitative and quantitative treatment factor levels

- 资料：`piepho2018tutorial`，[原文](https://doi.org/10.1111/jac.12267)
- 版本：Journal of Agronomy and Crop Science 204: 429–455，2018，CC BY 开放获取。原文文本取自 Internet Archive 保存的出版社 PDF。用田间试验实例讲析因试验和混合模型分析的教程，附 SAS 和 R 代码。位置写小节。

### E1

- 位置：1 Introduction
- 原文："All the experiments considered are comparative, meaning that the focus is exclusively on comparisons between treatments in the same experiment"
- 要点：本文讨论的都是比较试验，关注的只是同一试验内处理之间的比较。

### E2

- 位置：2.2.1 Block effects
- 原文："Treatment factors are of direct interest and are usually modelled as fixed effects, but nuisance factors such as block effects can be modelled either as fixed or as random effects."
- 要点：处理因素是直接关心的，通常当固定效应；区组这类"干扰因素"可以当固定效应，也可以当随机效应。

### E3

- 位置：2.2.1 Block effects
- 原文："Fixed block effects models are robust against distributional assumptions and are useful for eliminating block differences in designs with large complete or near-complete blocks"
- 要点：区组当固定效应，对分布假定比较稳健，适合区组大而完整（或接近完整）的设计。

### E4

- 位置：2.2.1 Block effects
- 原文："In general, however, incomplete block designs will confound substantial treatment information between blocks and then an analysis with recovery of inter-block information will be necessary. Fixed blocks are not useful for recovery of inter-block treatment information, but an assumption of random blocks will allow treatment information to be recovered by combining inter- and intra-block information"
- 要点：不完全区组设计里有相当多处理信息在区组之间；区组当固定效应就回收不了这部分信息，当随机效应则可以把区组间和区组内的信息合起来用。

### E5

- 位置：裂区示例（Example 2）
- 原文："It is particularly important to explicitly fit the main-plot, sub-plot and sub-sub-plot error terms as random to properly represent the three-stage randomization layout and hence to obtain valid inferences for the fixed effects. Each treatment effect has its own specific error term, depending on the experimental units to which the levels of the relevant treatment factor were randomly allocated."
- 要点：裂区类设计要把主区、副区、再裂区的误差项明确作为随机效应放进模型；每个处理效应有自己的误差项，取决于这个因素随机分配到哪一级实验单位。

### E6

- 位置：Discussion
- 原文："It is important to keep in mind that a data transformation affects several assumptions simultaneously."
- 要点：对数据做变换，会同时影响好几条统计假定。

### E7

- 位置：10 Discussion
- 原文："Although the analysis of such designs is often based on a comparison of the treatment means using multiple comparisons tests, such comparisons take no account of the ordered structure of the observations and are totally inappropriate for structured treatment comparisons."
- 要点：处理是定量水平（如几个施氮量）时，常有人用多重比较逐对比较均值，但这不考虑水平的顺序结构，完全不适合；应当用回归模型。

### E8

- 位置：Discussion
- 原文："Repeated-measures data are common in agronomic research but are frequently misinterpreted and analysed inappropriately."
- 要点：在同一实验单位上多次测量的数据（重复测量数据）在农学研究中很常见，却经常被误读、分析不当。
