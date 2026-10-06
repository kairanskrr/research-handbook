# Zuur 等 2010：A protocol for data exploration to avoid common statistical problems

- 资料：`zuur2010protocol`，[原文](https://doi.org/10.1111/j.2041-210X.2009.00001.x)
- 版本：Methods in Ecology and Evolution 1(1): 3–14，2010。出版社网站免费阅读（Unpaywall 标注为 bronze 开放获取）。出版社网站对脚本访问被拦截，原文文本取自 Internet Archive 2025-02-02 的全文网页快照。作者是给生态学者讲统计课的统计学者。位置写小标题。

### E1

- 位置：Summary 第 1 条
- 原文："If a random sample of their work (including scientific papers) produced before doing these courses were selected, half would probably contain violations of the underlying assumptions of the statistical techniques employed."
- 要点：作者凭讲课经验估计：学员上课前做的工作（包括论文），随机抽一批，大约一半会违反所用统计方法的前提假设。这是作者的经验判断，不是正式调查。

### E2

- 位置：Step 8: Are observations of the response variable independent?
- 原文："A crucial assumption of most statistical techniques is that observations are independent of one another"
- 要点：大多数统计方法的一个关键前提是：观测之间相互独立。

### E3

- 位置：Step 8
- 原文："If birds at locations close to each other have characteristics that are more similar to each other than to birds from locations separated by larger distances, then we would violate the independence assumption."
- 要点：例子：如果相近地点的鸟比远处地点的鸟更相像，独立性假设就被违反了。

### E4

- 位置：Step 8
- 原文："When such dependence arises, the statistical model used to analyse the data needs to account for it."
- 要点：观测之间不独立时，统计模型必须把这种相关考虑进去（例如对空间、时间关系建模，或用嵌套的层次结构）。

### E5

- 位置：Step 8
- 原文："Quite often a residual correlation structure is caused by an important covariate that was not measured. If this is the case, it may not be possible to resolve the problem."
- 要点：残差里的相关常常是因为漏测了一个重要变量；如果是这样，事后可能无法补救。

### E6

- 位置：Step 8
- 原文："Hence, it is important to check whether there is dependence in the raw data before doing the analysis, and also the residuals afterwards. These checks can be made by plotting the response variable vs. time or spatial coordinates."
- 要点：分析前检查原始数据、分析后检查残差有没有相关；办法是把响应变量对时间或空间坐标画图。
