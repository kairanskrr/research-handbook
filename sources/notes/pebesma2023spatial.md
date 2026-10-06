# Pebesma & Bivand 2023：Spatial Data Science: With Applications in R

- 资料：`pebesma2023spatial`，[免费在线版](https://r-spatial.org/book/)
- 版本：CRC Press 2023 年出版的教材，作者在网站上免费公开全文。作者是 R 语言空间数据工具包（sf、stars、spdep 等）的主要开发者。读取的是在线版第 2 章 Coordinates（坐标）和第 5 章 Attributes and Support（属性与支撑）。位置写章节。

### E1

- 位置：第 2 章 Coordinates，2.3 节
- 原文："The definitions above imply that coordinates in degrees longitude and latitude only have a meaning and can only be interpreted unambiguously as Earth coordinates, when the datum they are associated with is given."
- 要点：经纬度坐标只有在给出它所用的大地基准（datum）时，才有明确含义。

### E2

- 位置：第 2 章 Coordinates，投影坐标一节
- 原文："Projecting ellipsoidal coordinates means that shapes, directions, areas, or even all three, are distorted"
- 要点：把地球上的坐标投影到平面上，形状、方向、面积中至少有一样会变形。

### E3

- 位置：第 2 章 Coordinates，2.3 节
- 原文："Recomputing coordinates in a new datum is called coordinate transformation, and is approximate: because datums are a result of model fitting, transformations between datums are models too that have been fit"
- 要点：在不同大地基准之间换算坐标（坐标转换）是近似的，本身带误差。

### E4

- 位置：第 2 章 Coordinates，PROJ 一节
- 原文："Where we could safely assume for many decades that spatial data with ellipsoidal coordinates would have axis order (longitude, latitude), this is no longer the case."
- 要点：不能再默认经纬度数据的顺序一定是"经度在前、纬度在后"。

### E5

- 位置：第 5 章 Attributes and Support，导言
- 原文："for non-point geometries (lines, polygons), feature attribute values either have point support, meaning that the value applies to every point, or they have block support, meaning that the value summarises all points in the geometry."
- 要点：线、面上的属性值要么对其中每一点都成立（点支撑），要么是整块区域的汇总值（块支撑）。

### E6

- 位置：第 5 章 Attributes and Support，导言
- 原文："The reason for this is that the dataset contains variables with values that are associated with entire polygons – in this case population counts – meaning they are not associated with a POINT geometry replacing the polygon."
- 要点：例子：把县的多边形换成它的中心点时，人口数这类属于整个多边形的值，并不属于那个点，软件会给出警告。

### E7

- 位置：第 5 章 Attributes and Support，5.2 节
- 原文："Properly specifying attribute-geometry relationships, and warning against their absence or cases when change in geometry (change of support) implies a change of information can help to avoid a large class of common spatial data analysis mistakes"
- 要点：说清属性和几何的关系，并在改变几何（改变支撑）时提醒信息也变了，可以避免一大类常见的空间分析错误。

### E8

- 位置：第 5 章 Attributes and Support，空间聚合一节
- 原文："When we need an aggregate for a new area that is not a union of the geometries for a group of records, and we use a spatial predicate, then single records may be matched to multiple groups."
- 要点：按空间关系（如"相交"）把数据汇总到另一套边界时，同一条记录可能被算进多个区域，造成重复计数。

### E9

- 位置：第 5 章 Attributes and Support，空间聚合一节
- 原文："If points fall on a shared boundary than they are assigned to both polygons"
- 要点：恰好落在两区共用边界上的点，会被同时分给两个区。

### E10

- 位置：第 5 章 Attributes and Support，面积加权插值一节
- 原文："Extensive variables correspond to amounts, associated with a physical size (length, area, volume, counts of items). An example of a extensive variable is population count." / "An example of a related variable that is intensive is population density."
- 要点：广延量是总量（如人口数），区域切分时要跟着分；强度量是比率（如人口密度），切分后不能相加。

### E11

- 位置：第 5 章 Attributes and Support，5.4 节（升尺度和降尺度）
- 原文："Of course this makes only sense to the extent that the assumptions hold: over the source regions extensive variables need to be uniformly distributed and intensive variables need to have a constant value."
- 要点：面积加权插值只有在假设成立时才有意义：总量在原区域内均匀分布，比率在原区域内处处相同。
