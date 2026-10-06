# Rey, Arribas-Bel & Wolf 2023：Geographic Data Science with Python

- 资料：`rey2023geographic`，[免费在线版](https://geographicdata.science/book/intro.html)
- 版本：CRC Press 2023 年出版的教材，作者在网站上免费公开全文。读取的是在线版的四章：Spatial Weights（空间权重）、Choropleth Mapping（分级统计地图）、Global Spatial Autocorrelation（全局空间自相关）、Spatial Regression（空间回归）。作者是空间分析方向的学者，例子用 Python 的 PySAL 工具包。位置写章名。

### E1

- 位置：Spatial Weights 一章，开头
- 原文："By expressing the notion of geographical proximity or connectedness, spatial weights are the main mechanism through which the spatial relationships in geographical data is brought to bear in the subsequent analysis."
- 要点：空间权重表达"谁和谁相邻、相连"，是把空间关系带进后续分析的主要手段。

### E2

- 位置：Spatial Weights 一章，Contiguity weights（邻接权重）一节
- 原文："If we wanted them to be considered as neighbours, we can switch to the more inclusive notion of Queen contiguity, which requires the pair of polygons to only share one or more vertices."
- 要点：只共用一个顶点的两块区域，按"车式邻接"（Rook，要共边）不算邻居，按"后式邻接"（Queen，共一个顶点即可）算邻居；定义不同，邻居就不同。

### E3

- 位置：Spatial Weights 一章，Distance based weights（基于距离的权重）一节
- 原文："in cases where the density of the observations varies over the study region, using the same threshold anywhere will result in regions with a high density of neighbors while others with observations very sparsely connected."
- 要点：观测点疏密不均时，全区用同一个距离阈值，会让有的地方邻居很多、有的地方几乎没有邻居。

### E4

- 位置：Spatial Weights 一章，处理"孤岛"的一节
- 原文："Imagine one of our tracts was an island and did not have any neighbors in the contiguity case. This can create issues in the spatial analytics that build on spatial weights, so it is good practice to amend the matrix before using it."
- 要点：按邻接定义没有任何邻居的单元（"孤岛"）会给后续分析带来问题，使用前应修补权重矩阵。

### E5

- 位置：Choropleth Mapping 一章，Quantitative data classification 一节
- 原文："The choice of the classification scheme should take into consideration the statistical distribution of the attribute values as well as the goal of our map (e.g., highlight outliers vs. accurately depict the distribution of values)."
- 要点：选分级方法要同时考虑数据的分布和地图的目的（突出异常值，还是如实呈现分布）。

### E6

- 位置：Choropleth Mapping 一章，Equal intervals（等间距）一节
- 原文："However, this rule only considers the extreme values of the distribution and, in some cases, this can result in one or more classes being sparse."
- 要点：等间距分级只看最大最小值，数据偏态时会出现几乎没有观测的空级。

### E7

- 位置：Choropleth Mapping 一章，Quantiles（分位数）一节
- 原文："While quantile classification avoids the pitfall of sparse classes, this classification is not problem-free. The varying widths of the intervals can be markedly different which can lead to problems of interpretation."
- 要点：分位数分级避免了空级，但各级宽度可能差得很远，容易误读。

### E8

- 位置：Choropleth Mapping 一章，Color 一节之前
- 原文："This can have major impacts on our brain's pattern recognition capabilities, as we tend to be drawn to the larger polygons, even though they might not be the most relevant ones for our analysis."
- 要点：各区域大小、形状差别大时，人眼会被大块区域吸引，即使它们对分析并不最重要。

### E9

- 位置：Choropleth Mapping 一章，Color 一节
- 原文："The choice of a color scheme for a choropleth map should be based on the type of variable under consideration (Brewer et al. 1997). Generally, a distinction is drawn between three types of numerical attributes: sequential, diverging, and qualitative."
- 要点：配色要按变量类型选：顺序型、发散型、定性（类别）型三类。

### E10

- 位置：Choropleth Mapping 一章，Sequential / Diverging / Qualitative palettes 各节
- 原文："Sequential color schemes are appropriate for continuous data where the origin is in one end of the series." / "This is useful with continuous data when one wishes to place equal emphasis on mid-range critical values as well as extremes at both ends of the distribution." / "Qualitative palettes encode categorical data."
- 要点：顺序配色用于起点在一端的连续数据；发散配色用于中间有关键值、两端极值同样重要的连续数据；定性配色用于类别数据。

### E11

- 位置：Global Spatial Autocorrelation 一章，开头
- 原文："Spatial autocorrelation thus has to do with the degree to which the similarity in values between observations in a dataset is related to the similarity in locations of such observations."
- 要点：空间自相关指：观测值之间的相似程度，和它们位置上的接近程度有多大关系。

### E12

- 位置：Global Spatial Autocorrelation 一章，开头
- 原文："For example, think of the distribution of income, or poverty, over space: it is common to find similar values located nearby (wealthy areas close to other wealthy areas, poor population concentrated in space too)."
- 要点：正的空间自相关在社会现象中常见，例如富裕地区挨着富裕地区，贫困人口也在空间上集中。

### E13

- 位置：Global Spatial Autocorrelation 一章，Brexit 例子之后
- 原文："This extraordinary capability to spot trends, patterns and associations tends to also create many false positives: cases where we think there is a pattern, but in fact what we are seeing is largely random"
- 要点：人很擅长发现规律，也因此常把随机看成规律；单凭看地图判断有没有空间集聚并不可靠。

### E14

- 位置：Global Spatial Autocorrelation 一章，Moran's I 一节
- 原文："In fact, there is a close connection between the two: the value of Moran's I corresponds with the slope of the linear fit overlayed on top of the Moran Plot."
- 要点：莫兰指数（Moran's I）等于莫兰散点图（横轴是变量，纵轴是它的空间滞后，即邻居的平均值）上拟合直线的斜率。

### E15

- 位置：Global Spatial Autocorrelation 一章，Moran's I 一节
- 原文："A small enough p-value associated with the Moran's I of a map allows to reject the hypothesis that the map is random."
- 要点：莫兰指数对应的 p 值足够小，才能拒绝"这张地图的格局是随机的"这一假设。

### E16

- 位置：Spatial Regression 一章，Non-spatial regression 一节
- 原文："But, our model might display some clustering in the errors, which may be a problem as that violates the i.i.d. assumption linear models usually come built-in with."
- 要点：普通线性回归的误差如果在空间上成团，就违反了线性模型通常默认的"误差独立同分布"假设。

### E17

- 位置：Spatial Regression 一章，导言
- 原文："They might also arise because there is some other feature whose omission causes the spatial patterns in the error we see; if this additional feature were included, the structure would disappear."
- 要点：误差的空间格局可能来自遗漏了某个有空间格局的变量；把它加进模型，格局可能就消失。

### E18

- 位置：Spatial Regression 一章，Spatial heterogeneity 一节
- 原文："At its most basic, spatial heterogeneity means that parts of the model may vary systematically with geography, change in different places."
- 要点：空间异质性指模型的某些部分随地理位置系统地变化，在不同地方不一样。

### E19

- 位置：Spatial Regression 一章，Spatial error / Spatial lag 两节
- 原文："Although it appears similar, this specification violates the assumptions about the error term in a classical OLS model. Hence, alternative estimation methods are required." / "Although it might not seem very different from the previous equation, this model violates the exogeneity assumption, crucial for OLS to work."
- 要点：空间误差模型和空间滞后模型都违反普通最小二乘法（OLS）的假设，要用专门的估计方法。

### E20

- 位置：Spatial Regression 一章，Spatial lag 一节
- 原文："Similarly to the effects in the SLX regression, changes in the spatial lag regression need to be interpreted with care."
- 要点：空间滞后模型里的系数不能像普通回归那样直接读，要小心解释（作者建议用预测和情景模拟区分直接和间接效应）。

### E21

- 位置：Spatial Regression 一章，Questions（练习题）
- 原文："Fortunately for us, spatial error models recover the same estimates (asymptotically) as a typical OLS estimate, although their confidence intervals will change. Statistically, this occurs because OLS miscalculates when there is spatial correlation and/or spatial heteroskedasticity."
- 要点：存在空间相关时，普通最小二乘法会算错置信区间；空间误差模型的系数估计（大样本下）与它相同，但置信区间会变。
