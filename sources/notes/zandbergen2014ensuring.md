# Zandbergen 2014：Ensuring Confidentiality of Geocoded Health Data: Assessing Geographic Masking Strategies for Individual-Level Data

- 资料：`zandbergen2014ensuring`，[PubMed Central 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4590956/)，doi:10.1155/2014/567049
- 版本：Advances in Medicine 2014:567049，CC BY 许可的综述。作者是美国新墨西哥大学的地理学者，以公共卫生数据为背景讨论地址地理编码、反向地理编码和地理掩蔽。位置写小节名。

### E1

- 位置：第 2 节 Individual-Level Data and Geocoding
- 原文："This confirms that geocoding has become firmly established as an analytical tool in public health research"
- 要点：作者认为地理编码（把地址变成地图上的点）已成为公共卫生研究中确立的分析工具。

### E2

- 位置：第 2 节 Individual-Level Data and Geocoding
- 原文："Geocoding is not error-free. Typically, a certain number of records do not geocode due to incomplete or incorrect information. Geocoded locations may also not be accurate due to incorrect reference information or errors in the geocoding process"
- 要点：地理编码有误差：一部分地址因信息不全或错误而匹配不上；匹配上的位置也可能因参考数据错误或编码过程出错而不准。

### E3

- 位置：第 3 节 Reverse Geocoding
- 原文："Publishing a location as coordinates (e.g., latitude/longitude) means that these can be plotted on a map and then associated with an address. Publishing a map in paper or digital form also means that the locations can be associated with an address."
- 要点：公布坐标或公布点位地图，别人都能把点对回到地址上。

### E4

- 位置：第 3 节 Reverse Geocoding
- 原文："created a hypothetical map of geocoded patient addresses and were able to correctly identify 79% of the addresses using manual reverse geocoding techniques in GIS."
- 要点：作者引用的一项研究：用一张假想的病人地址点位图，靠在地理信息系统中手工反向地理编码，正确找出了 79% 的地址。

### E5

- 位置：第 5 节 Confidentiality Protection Strategies
- 原文："Many spatial analytical techniques, such as general point-pattern analysis and cluster detection, are much less powerful or simply not possible using aggregated data."
- 要点：汇总成区域数据后，点格局分析、聚集探测等很多方法效力大减，甚至无法做。

### E6

- 位置：第 6 节 Ensuring Confidentiality Using Geographic Masking
- 原文："Geographic masking is the process of altering the coordinates of point location data to limit the risk of reidentification upon release of the data."
- 要点：地理掩蔽是在发布前改动点的坐标，以降低被重新识别的风险。

### E7

- 位置：第 7 节 Different Approaches to Geographic Masking
- 原文："Determining the amount of displacement necessary to achieve confidentiality has been addressed by several of the studies on geographic masking [56], but no universal guidelines have emerged. However, it is widely agreed upon that the amount of displacement should be inversely proportional to the local population density"
- 要点：位移多大才够，没有通用标准；但普遍认为位移应与当地人口密度成反比（人越稀，移得越远）。

### E8

- 位置：第 10 节 Effects of Masking on Spatial-Analytic Methods
- 原文："Findings indicated a consistent tradeoff between the amount of perturbation and the accuracy of the analytical results"
- 要点：作者引用的一项研究发现：扰动越大，分析结果越不准，两者一直此消彼长。

### E9

- 位置：第 7 节 Different Approaches to Geographic Masking
- 原文："The earlier review of applications of geographic masking to real-world datasets has indicated that some studies do not mention the specific technique by name."
- 要点：作者回顾实际应用时发现，有些研究没写明用的是哪种掩蔽方法。
