# Kedron 等 2021：Reproducibility and replicability: opportunities and challenges for geospatial research

- 资料：`kedron2021reproducibility`，[原文 PDF（美国国家科学基金会公共访问库）](https://par.nsf.gov/servlets/purl/10292882)，doi:10.1080/13658816.2020.1802032
- 版本：International Journal of Geographical Information Science（国际地理信息科学期刊，IJGIS）综述文章，2020 年 8 月在线发表，2021 年刊出（35 卷 3 期）。作者为美国亚利桑那州立大学和加州大学圣巴巴拉分校的地理信息科学学者。读取的是美国国家科学基金会（NSF）公共访问库提供的出版社版本 PDF。位置写章节。

### E1

- 位置：§1 Introduction
- 原文："Reproducibility – obtaining results consistent with a prior study using the same materials, procedures, and conditions of analysis – and Replicability – obtaining consistent findings across studies that aim to answer the same question but with each study collecting and using its own data"
- 要点：可复现性（reproducibility）指用同样的材料、步骤和分析条件得到与原研究一致的结果；可复制性（replicability）指回答同一问题、但各自收集数据的不同研究得到一致的发现。

### E2

- 位置：§2
- 原文："Geospatial research is susceptible to specification search because spatial analyses require a well-documented set of apriori decisions that set the parameters of analysis (e.g. the scale of analysis, representation of spatial relationships). [...] This lack of knowledge widens the range of reasonable specifications a researcher might explore."
- 要点：空间分析需要事先定下一系列参数（如分析尺度、怎样表示空间关系），而研究者往往不知道这些参数的真实取值，可选的"合理设定"就更多，因此地理空间研究容易出现设定搜索（反复试设定、只报告其中一个）。

### E3

- 位置：§2
- 原文："they also needed to choose a weight matrix that defines the spatial relationships that exist among neighboring cities [...] If only one of these many spatial regression specifications is reported, these many other tests are not included in the literature and cannot be replicated or reproduced."
- 要点：以一项中国 289 个城市的城市化与空气质量研究为例：做空间回归还要选空间权重矩阵（规定哪些城市算"相邻"）；如果试过很多种设定只报告一种，其余检验就从文献中消失，别人无法复现或复制。

### E4

- 位置：§3.1
- 原文："a geographic pre-analysis plan would likely need to include an explicit statement of the scale(s) used in the analysis [...] research using spatial statistical methods to explore or adjust for the impacts of spatial autocorrelation would need to outline and justify the range of spatial weights matrices examined."
- 要点：地理研究的预分析计划可能需要明确写出分析所用的尺度；用空间统计方法的研究，要列出并说明会检验哪些空间权重矩阵。

### E5

- 位置：§3.1
- 原文："To our knowledge, the geospatial community has yet to deeply explore the possibilities of pre-analysis plans and pre-registration or the practicalities of their implementation."
- 要点：据作者所知，地理空间研究界还没有深入探索预分析计划和预注册的可能性及实际做法。

### E6

- 位置：§4.1
- 原文："While it may be reasonable to expect geospatial analysis to be reproducible, it is less clear whether or not geospatial research should be replicable. When does a change in the location, time, or context of a second study represent enough of a difference that we should no longer expect a result to replicate?"
- 要点：期待地理空间分析可复现是合理的，但是否应期待它可复制并不清楚：换了地点、时间或背景，差异大到什么程度就不该再指望结果重现？

### E7

- 位置：§4.1
- 原文："It may also be useful for GIScience to develop an assessment framework for individual studies that recognize replicability not as a binary success-failure measure, but as existing along a spectrum."
- 要点：作者建议把可复制性看作一个连续谱，而不是"成功/失败"的二分。

### E8

- 位置：§3.2
- 原文："Geospatial analyses involving human subjects often requires that collected data not only be anonymized but that data also not be shared to preserve confidentiality."
- 要点：涉及人的地理空间分析，常常不仅要求数据匿名化，还要求为保密而不共享数据。

### E9

- 位置：§3.2
- 原文："Shepherd et al. (2017) propose that researchers release the code used in an analysis, but rather than releasing the original data, create and release a simulated dataset with characteristics that match the original data [...] In geospatial research, such simulated data could be created to match the spatial structures (e.g. autocorrelation) and attribute relationships in the original data."
- 要点：数据不能公开时，一种做法是公开代码，再发布一份与原数据特征相符的模拟数据；在地理研究中，模拟数据可以保留原数据的空间结构（如空间自相关）和属性关系。

### E10

- 位置：§3.2
- 原文："this journal has a data-sharing policy that requires authors to make data and research artifacts freely available and aligned with FAIR standards."
- 要点：IJGIS 有数据共享政策，要求作者免费公开数据和研究材料，并符合 FAIR 原则（可查找、可访问、可互操作、可重用）。

### E11

- 位置：§3.2
- 原文："If a geospatial researcher cannot share data for ethical reasons or because an industry partner is restricting the release of data, that research should not be kept from the published record."
- 要点：因伦理原因或企业合作方限制而不能共享数据的研究，不应因此被挡在发表之外。

### E12

- 位置：§3.1
- 原文："Interview information could be similarly recorded, as could information about the process of coding and theme extraction common in many qualitative studies."
- 要点：访谈信息、定性研究中编码和提炼主题的过程，也可以像计算步骤一样记录下来。

### E13

- 位置：§4.2
- 原文："In geospatial research, the details necessary for reproduction include information about how spatial processes were conceptualized, measured through spatial data, and then operationalized during analysis."
- 要点：地理空间研究要被复现，需要交代空间过程是怎样被概念化、怎样用空间数据测量、又怎样在分析中操作化的。
