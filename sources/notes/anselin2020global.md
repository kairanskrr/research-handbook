# Anselin 2020：Global Spatial Autocorrelation (1)（GeoDa 教程）

- 资料：`anselin2020global`，[GeoDa 工作手册在线版](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html)
- 版本：芝加哥大学空间数据科学中心 GeoDa 软件的免费在线教程，作者 Luc Anselin（空间计量和局部空间自相关指标的提出者之一），2020 年 10 月 9 日修订版。位置写小节名。

### E1

- 位置：The Moran Scatter Plot > Moran's I
- 原文："Moran's I statistic is arguably the most commonly used indicator of global spatial autocorrelation." / "In essence, it is a cross-product statistic between a variable and its spatial lag, with the variable expressed in deviations from its mean."
- 要点：莫兰指数可以说是最常用的全局空间自相关指标；本质上是变量（减去均值后）与其空间滞后的交叉乘积。

### E2

- 位置：The Moran Scatter Plot > Permutation inference
- 原文："This calculates a reference distribution for the statistic under the null hypothesis of spatial randomness by randomly permuting the observed values over the locations."
- 要点：置换检验：把观测值随机打乱分配到各位置，反复计算统计量，得到"空间随机"时的参照分布。

### E3

- 位置：The Moran Scatter Plot > Permutation inference
- 原文："More precisely, a result that has a p-value of 0.01 with 99 permutations is not necessarily more significant than a result with a p-value of 0.001 with 999 permutations."
- 要点：伪 p 值的大小部分由置换次数决定；99 次置换得到 0.01 不一定比 999 次得到 0.001 更不显著。

### E4

- 位置：Interpretation > Moran scatter plot 的四个象限
- 原文："it is important to keep in mind that the classification as such does not imply significance."
- 要点：莫兰散点图把观测分成"高-高""低-低"等四类，但分进哪一类本身不代表显著。

### E5

- 位置：Inference 一节
- 原文："we select 999 Permutations, which is typically sufficient for reliable inference."
- 要点：999 次置换通常足以得到可靠的推断。

### E6

- 位置：Inference 一节
- 原文："In order to facilitate replication, the default setting in GeoDa is to use a specified seed for the random number generator." / "Using the same random seed ensures reproducibility on a particular machine. However, due to the way the random number generator is implemented, there may be differences depending on the hardware, specifically when a different number of CPU cores is used."
- 要点：GeoDa 默认用固定随机种子便于复现；但即使种子相同，换了硬件（例如 CPU 核数不同）结果也可能不同。

### E7

- 位置：Moran scatter plot as a standard scatter plot 一节
- 原文："The usual standard errors and t-statistics provided in the scatter plot are not appropriate in the spatial case."
- 要点：普通散点图给出的标准误和 t 统计量，在空间情形下不适用。

### E8

- 位置：Interpretation 一节
- 原文："We can see that the shape of the point cloud is influenced by the presence of several outliers on the high end"
- 要点：例子中，几个极端高值影响了莫兰散点图的形状（作者随后指出它们把斜率拉低）。
