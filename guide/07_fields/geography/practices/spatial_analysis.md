# 空间分析研究

本文讲**用带位置的数据回答问题的定量研究**：把数据放到地图上，检查它们在空间上是否成团，用考虑了空间关系的统计模型做分析，再把结果画成诚实的地图发表出来。它是社会与经济地理学的常用方法，但不限于地理学：Zandbergen 认为，在公共卫生研究中，地址地理编码（把地址变成地图上的点）已是确立的分析工具[^zandbergen2014ensuring-e1]；Nüst 和 Pebesma 收集的可复现案例也来自生态学的空间数据收集和分析、空间统计等方向[^nust2021practical-e4]。自然地理和环境数据的背景见[地球与环境科学篇](../../earth-environmental-sciences/README.md)，健康数据的背景见[健康科学篇](../../health-sciences/README.md)。

可塑性面积单元问题、生态谬误、不确定的地理背景问题、位置隐私、可复现与可复制，地理学学科概况已经讲过（见[空间分析的陷阱](../README.md#空间分析的陷阱单元怎么划结论就可能怎么变)、[位置隐私](../README.md#位置隐私坐标就是身份信息)、[可复现与可复制](../README.md#可复现与可复制)），本文不再重复，只讲具体怎么做。不涉及位置的一般数据分析见研究类型里的[数据科学研究](../../../06_methods/data_science.md)。

本文的操作建议很多来自两本免费在线教材（Rey 等人的 *Geographic Data Science with Python*，Pebesma 和 Bivand 的 *Spatial Data Science*）和一份软件手册（Anselin 写的 GeoDa 工作手册）。它们是作者的建议，不是学界统一的规定。

**适用范围**：这是社会与经济地理学常用的研究方法，上面提到的公共卫生、生态学等方向也会用到。描述空间分布、检验"环境怎样影响个人"的通用逻辑，见研究套路里的[观察描述](../../../05_research-strategies/observe_describe.md)和[解释因果](../../../05_research-strategies/explain_causality.md)；选题、做计划、写作等各学科共通的步骤，见第一部分、第二部分、写作和发表各章，例如[从研究问题到证据清单](../../../02_do-the-project/01_question-to-evidence.md)和[分析与解读](../../../02_do-the-project/07_analyze-and-interpret.md)。

**常服务的套路**：[观察描述](../../../05_research-strategies/observe_describe.md)（描述现象在空间上怎样分布、检验是否成团）、[解释因果](../../../05_research-strategies/explain_causality.md)（研究环境或邻近地区怎样影响结果）。依据：用莫兰指数（检验空间上是否成团的统计量，见第 6 步）检验时，p 值足够小，才能拒绝"这张地图的格局是随机的"[^rey2023geographic-e15]，这是在检验分布；研究社会和物理环境对健康的影响，是关心环境的作用[^kwan2012uncertain-e4]。

**读完本文，你应该能：**

- 把一个研究问题写成"在什么单元、什么尺度上，什么空间过程"的形式，并事先计划敏感性分析；
- 检查坐标参考系、地理编码误差，正确地做空间连接和汇总；
- 画出分级和配色都诚实的地图；
- 用莫兰指数检验空间自相关，知道普通回归在什么时候会出错；
- 发表地图和数据前保护参与者的位置隐私，让整个分析能被别人重跑。

---

## 1. 这是什么研究，什么时候用

当你的问题里"在哪里"本身很重要——某个现象在空间上是否集中、邻近的地方是否互相影响、环境暴露是否和健康结果有关——就需要空间分析。即使你没打算研究空间，只要数据带位置，普通回归的误差也可能在空间上成团，违反回归默认的假设[^rey2023geographic-e16]，所以值得先检查一下。

| | 空间分析研究 | 一般数据科学研究 | 定性田野、参与式制图 |
|---|---|---|---|
| 核心问题 | 位置和邻近关系怎样影响结果 | 变量之间的预测或解释关系 | 人怎样理解和使用一个地方 |
| 特有的风险 | 结论随单元和尺度改变[^kwan2018limits-e2]；误差在空间上成团[^rey2023geographic-e16]；坐标会暴露个人[^zandbergen2014ensuring-e3] | 数据泄漏、过拟合，见[数据科学研究](../../../06_methods/data_science.md) | 研究者立场，见[地理学学科概况](../README.md#立场与反思把研究工具本身交代清楚) |
| 主要依据 | 本文 | 研究类型里的[数据科学研究](../../../06_methods/data_science.md) | [访谈研究](../../../06_methods/interview_study.md)、[案例研究与民族志](../../../06_methods/case_study.md) |

空间分析和定性田野可以组合：用空间分析找规律，再用访谈理解原因，见[混合方法](../../../06_methods/mixed_methods.md)。

---

## 2. 怎么做

### 第 1 步：把空间问题问清楚

**怎么做：** 写下三件事：你设想的空间过程是什么（例如"相邻地区互相模仿""离污染源越近越不健康"）；用什么数据测量它；分析时怎样把它变成具体的单元、距离和"相邻"定义。Kedron 等人指出，别人要复现一项地理研究，需要的正是这三样信息[^kedron2021reproducibility-e13]。再问一句：结论是关于**地区**还是关于**个人**？用地区数据回答个人问题，就可能落入生态谬误（见[学科概况](../README.md#空间分析的陷阱单元怎么划结论就可能怎么变)）。

**为什么：** 这些选择决定了后面每一步，写不清楚，别人就无法判断结论从哪来。

**容易错在哪：** 先拿到一份按行政区汇总的现成数据，再倒推问题，结果单元和问题对不上。

### 第 2 步：选空间单元和尺度，事先计划敏感性分析

**怎么做：**

- 列出候选单元。关美宝 2018 年的文章列举：地理、环境健康和社会科学研究常用的空间单元是普查区、普查街区组和邮编区，时间单元是日、月、年；换了单元，结果可能就不同[^kwan2018limits-e1]。
- 选定主分析用的单元，在方法部分写明用了什么单元、它离真实的地理背景有多近、考虑了哪些时间因素[^kwan2012uncertain-e6]。"邻里"有哪些划法，见[学科概况](../README.md#空间分析的陷阱单元怎么划结论就可能怎么变)。
- 分析开始前，写下还要试哪些尺度、划法和"相邻"定义。Kedron 等人认为，地理研究的预分析计划可能需要写明分析尺度；用空间统计方法的，还要列出并说明要检验哪些空间权重矩阵（见第 6 步）[^kedron2021reproducibility-e4]。
- 全部结果都报告。结论在不同设定下稳不稳定，本身就是发现。

**为什么：** 区域数据的分析结果会随尺度和分区方式改变[^kwan2018limits-e2]。可选的设定又很多，只报一种就等于挑设定，见[学科概况·可复现与可复制](../README.md#可复现与可复制)。

**容易错在哪：** 用"模型拟合最好"来证明单元选对了。关美宝指出，拟合最好的模型不一定用的是真实的地理背景[^kwan2012uncertain-e7]。

### 第 3 步：弄清数据来源和位置精度

**怎么做：**

- **记下每份数据的坐标参考系**（说明坐标数字对应地球上哪个位置的一套规则）。Pebesma 和 Bivand 的教材指出：经纬度只有在给出所用的大地基准（描述地球形状的参照模型）时才有明确含义[^pebesma2023spatial-e1]；不同基准之间换算坐标是近似的，本身带误差[^pebesma2023spatial-e3]；也不能再默认经纬度一定是"经度在前"[^pebesma2023spatial-e4]。画出来位置明显不对时，先查坐标顺序。
- **按用途选投影**（把球面坐标画到平面上的方法）。投影后，形状、方向、面积中至少有一样会变形[^pebesma2023spatial-e2]。要算面积或距离时，选一个在研究区域保持该量的投影，并在论文里写明。
- **报告地理编码质量。** 地理编码有误差：一部分地址因信息不全或错误匹配不上，匹配上的也可能不准[^zandbergen2014ensuring-e2]。记录匹配率，检查没匹配上的地址是否集中在某类地区，因为那会让样本有偏。
- **保存在线数据的原样。** Nüst 和 Pebesma 提醒，在线地理服务可能变化或消失，访问它的代码、发出的请求和返回的结果都要保存[^nust2021practical-e7]。

数据质量的一般检查（缺失、来源、测量误差）见[数据科学研究·第二步](../../../06_methods/data_science.md#第二步弄清数据的来源和质量)。

### 第 4 步：清理和连接空间数据

**怎么做：**

- 做任何叠加、连接之前，把所有图层转换到同一个坐标参考系。
- **分清每个属性值属于点还是整块区域。** 有的值对区域内每一点都成立，有的是整块区域的汇总[^pebesma2023spatial-e5]。比如把县换成中心点时，县的人口数并不属于那个点[^pebesma2023spatial-e6]。Pebesma 和 Bivand 认为，改变几何形状时想清楚信息是否也变了，可以避免一大类常见错误[^pebesma2023spatial-e7]。
- **汇总时检查重复计数。** 按"相交"等空间关系把数据汇总到另一套边界，同一条记录可能被算进多个区域[^pebesma2023spatial-e8]；恰好落在边界上的点会同时分给两个区[^pebesma2023spatial-e9]。汇总后核对总数是否和原始数据一致。
- **分清总量和比率。** 人口数这种总量，区域切分时要跟着分；人口密度这种比率，切分后不能相加[^pebesma2023spatial-e10]。按面积比例把数据分到新边界，只有在"总量在原区域内均匀分布、比率处处相同"时才合理[^pebesma2023spatial-e11]，论文里要说明这个假设。

**容易错在哪：** 直接把两份数据按地名或编码合并，没发现行政区划在两个年份之间调整过。

### 第 5 步：探索性分析和诚实的地图

**怎么做：**

- **先选分级方法，再看地图。** 分级统计地图（按区域填色的地图）怎么分级，Rey 等人的教材建议同时考虑数据分布和地图目的（突出异常值，还是如实呈现分布）[^rey2023geographic-e5]。等间距分级只看最大最小值，有时会出现几乎没有观测的级[^rey2023geographic-e6]；分位数分级避免了这个问题，但各级宽度可能差很多，容易误读[^rey2023geographic-e7]。图例写明分级方法和断点。
- **按变量类型选配色。** 同一本教材建议：起点在一端的连续数据用顺序配色；中间有关键值、两端同样重要的用发散配色；类别数据用定性配色[^rey2023geographic-e9][^rey2023geographic-e10]。ColorBrewer 是面向制图的配色工具，三类配色都有[^crameri2020misuse-e6]。
- **少用彩虹色和亮度相近的红绿配色。** 这是 Crameri 等人（地球科学学者）在一篇谈科学配色误用的文章里的观点：彩虹色中最亮的黄色会不公平地突出一段数值[^crameri2020misuse-e3]，而感知均匀的配色让同样大的差异看起来一样大[^crameri2020misuse-e7]；亮度相近的红绿配色，很大一部分读者读不出来[^crameri2020misuse-e4]；用错颜色等于突出了一部分数据，黑白打印时还会丢失含义[^crameri2020misuse-e2]。
- **提醒自己：大块区域更抢眼。** 人眼会被面积大的区域吸引，即使它们对分析并不最重要[^rey2023geographic-e8]。

**为什么：** 人很擅长发现规律，也常把随机看成规律[^rey2023geographic-e13]。Crameri 等人还认为，配色常常是被动选的，不像其他方法那样受审视[^crameri2020misuse-e5]。所以地图只用来提出假设，"是否成团"要靠下一步的统计检验。

### 第 6 步：检验空间自相关

**空间自相关**指观测值彼此有多相似，和它们位置有多近有多大关系[^rey2023geographic-e11]。例如收入或贫困的分布里，相近的值常常挨在一起，富裕地区挨着富裕地区[^rey2023geographic-e12]。这时普通回归的误差可能在空间上成团，违反"误差独立同分布"的假设[^rey2023geographic-e16]。

**怎么做：**

1. **定义"相邻"（空间权重矩阵）。** 它规定谁和谁算邻居，是把空间关系带进分析的主要手段[^rey2023geographic-e1]。可以要求共边才算相邻，也可以共一个顶点就算[^rey2023geographic-e2]，还可以按距离来定。观测疏密不均时，全区用同一个距离阈值，会让有的地方邻居很多、有的地方几乎没有[^rey2023geographic-e3]。没有任何邻居的"孤岛"单元，Rey 等人的教材建议用之前先处理[^rey2023geographic-e4]。
2. **算莫兰指数（Moran's I）。** 它可以说是最常用的全局空间自相关指标[^anselin2020global-e1]。它的值等于莫兰散点图（横轴是变量，纵轴是邻居的平均值）上拟合直线的斜率[^rey2023geographic-e14]。先看散点图：GeoDa 手册的例子里，几个极端高值就改变了散点图的形状[^anselin2020global-e8]。
3. **用置换检验判断显著性。** 置换检验是把观测值随机打乱到各位置、反复计算，得到"空间随机"时的参照分布[^anselin2020global-e2]。GeoDa 手册认为 999 次置换通常足够[^anselin2020global-e5]。p 值足够小，才能拒绝"这张地图的格局是随机的"[^rey2023geographic-e15]。这样得到的 p 值叫伪 p 值，和置换次数有关：99 次得到 0.01，不一定比 999 次得到 0.001 更显著[^anselin2020global-e3]。散点图上分出的"高-高""低-低"类别本身不代表显著[^anselin2020global-e4]；普通散点图给出的标准误和 t 值，在空间情形下也不适用[^anselin2020global-e7]。
4. **固定随机种子并报告。** GeoDa 默认用固定种子，便于复现；但手册也提醒，即使种子相同，换了硬件（如 CPU 核数不同）结果也可能不同[^anselin2020global-e6]。Nüst 和 Pebesma 复现别人的研究时，也把设定随机种子列为值得肯定的做法[^nust2021practical-e5]。
5. **换几种权重矩阵重算**，按第 2 步的计划全部报告[^kedron2021reproducibility-e4]。

### 第 7 步：空间回归入门

**怎么做：**

1. 先跑普通回归，把残差画到地图上，再对残差算莫兰指数。残差成团，可能是漏了一个有空间格局的变量，把它加进去格局就可能消失[^rey2023geographic-e17]。
2. 判断空间效应的类型。**空间异质性**：模型的某些部分随地点系统地变化[^rey2023geographic-e18]，可以考虑按地区设固定效应或分区估计。**空间依赖**：邻居的情况影响本地结果，可以考虑空间滞后模型（把邻居的因变量放进模型）或空间误差模型（让误差项在邻居之间相关）。
3. 这两类模型都违反普通最小二乘法（普通线性回归的标准估计方法）的假设，要用专门的估计方法[^rey2023geographic-e19]。Rey 等人的教材指出，存在空间相关时，普通最小二乘法会算错置信区间[^rey2023geographic-e21]；空间滞后模型的系数也要小心解释[^rey2023geographic-e20]。

**容易错在哪：** 照着软件菜单挑一个模型，说不出它对应什么空间过程。空间计量模型种类很多，本文只讲入门判断；正式使用前读第 5 节的教材，或请教熟悉空间统计的人。

### 第 8 步：发表地图和数据前保护位置

为什么坐标就是身份信息、汇总和分层共享怎么做，见[学科概况·位置隐私](../README.md#位置隐私坐标就是身份信息)。下面补充地理编码数据的具体做法，主要依据 Zandbergen 2014 年以公共卫生数据为背景写的一篇综述：

- **假设每个点都能被对回地址。** 公布坐标或点位地图，别人都能把点对回到地址上（反向地理编码）[^zandbergen2014ensuring-e3]。Zandbergen 引用的一项研究中，仅靠在地理信息系统里手工比对，就从一张假想的病人地址图上正确找出了 79% 的地址[^zandbergen2014ensuring-e4]。
- **在汇总和掩蔽之间权衡。** 汇总到更粗的单元最简单，但汇总后点格局分析、聚集探测等方法效力大减甚至无法做[^zandbergen2014ensuring-e5]。另一种做法是**地理掩蔽**：发布前改动点的坐标[^zandbergen2014ensuring-e6]。据这篇综述，移多远没有通用标准，但普遍认为人越稀的地方要移得越远[^zandbergen2014ensuring-e7]；它引用的一项研究发现，扰动越大，分析结果越不准[^zandbergen2014ensuring-e8]。
- **说明选择理由，写明参数。** Malekzadeh 等人 2026 年的地理隐私伦理指南（建议性质）指出，地理数据没有通用的隐私保护方法，研究者要说明为什么选这一种[^malekzadeh2026ethical-e12]；这些处理也可能扭曲空间格局，或把弱势群体排除在分析之外[^malekzadeh2026ethical-e13]。论文里写明用了哪种掩蔽方法和参数——Zandbergen 发现，有些研究连方法名称都没写[^zandbergen2014ensuring-e9]。
- **注意在线底图。** 用第三方底图插件的平台常把位置信息发到外部服务器[^malekzadeh2026ethical-e14]；处理敏感坐标时，用本地底图或机构内的环境。

### 第 9 步：让整个分析能被重跑

为什么要可复现、一项对会议论文的评估发现了什么，见[学科概况·可复现与可复制](../README.md#可复现与可复制)。下面是 Nüst 和 Pebesma 2021 年给地理学和地球科学的具体建议：

- **用脚本，不用点击。** 基于脚本的流程，指从原始数据到发表用的图，全程无需手工操作就能跑完[^nust2021practical-e1]。他们指出，主流地理信息系统软件靠点击操作、闭源，或两者兼有；要么用能记录操作步骤的工具，要么换用开放工具[^nust2021practical-e8]。
- **地图也用代码画。** 手工调整地图外观，不应以牺牲可复现性为代价[^nust2021practical-e6]。
- **记录所有参数。** 坐标参考系、单元、权重矩阵、分级断点、置换次数和随机种子，写进脚本和方法部分；在配置文件里锁定软件包版本[^nust2021practical-e2]。
- **用开放格式，加许可证**[^nust2021practical-e3]。
- **数据不能公开时**，公开代码，再发布一份保留原数据空间结构（如空间自相关）的模拟数据[^kedron2021reproducibility-e9]；编造的数据能防止认出个人，又能演示方法[^nust2021practical-e10]。
- **和参与者一起制图的研究也一样。** 地图常用于在收集数据时和参与者互动、传达结果，所以数据收集和制图也应当可复现[^nust2021practical-e9]。

整理数据和代码的通用做法见贯穿全程的[整理科研材料](../../../08_throughout/organizing_materials.md#3-每个结果都要能追溯到它是怎么来的)。

### 第 10 步：报告

方法部分至少写清：数据来源和年份、坐标参考系和投影、地理编码匹配率、空间单元和尺度及其理由[^kwan2012uncertain-e6]、空间权重矩阵和试过的其他设定[^kedron2021reproducibility-e4]、空间自相关检验的方法和置换次数、所用模型、隐私保护处理和参数、代码和数据的获取方式。地图要有图例、分级方法、比例尺和数据来源。

空间分析有没有类似临床试验那样公认的报告规范，本文资料未涉及，以目标期刊要求为准；用登记、病历等常规收集数据做的健康空间研究，可以参考[健康科学篇](../../health-sciences/README.md#报告规范在临床医学篇的基础上再加几份)列出的报告规范。

---

## 3. 检查清单

**必须做到**

- [ ] 写明空间单元、尺度及其与真实地理背景的关系[^kwan2012uncertain-e6]
- [ ] 所有图层的坐标参考系已知且一致[^pebesma2023spatial-e1]
- [ ] 汇总、连接后核对总数，没有重复计数，也没有把比率当总量相加[^pebesma2023spatial-e8][^pebesma2023spatial-e10]
- [ ] 回归前检查残差的空间自相关；存在时不直接用普通最小二乘法的置信区间[^rey2023geographic-e16][^rey2023geographic-e21]
- [ ] 显著性用置换检验，报告置换次数和随机种子[^anselin2020global-e3][^anselin2020global-e6]
- [ ] 发表的点位地图和坐标不能让人对回参与者的住址[^zandbergen2014ensuring-e3]

**做到更好**

- [ ] 预分析计划写明尺度和要检验的空间权重矩阵[^kedron2021reproducibility-e4]
- [ ] 报告多种单元、尺度、权重矩阵下的结果
- [ ] 配色感知均匀、避开亮度相近的红绿[^crameri2020misuse-e7][^crameri2020misuse-e4]
- [ ] 全流程脚本化，锁定软件版本[^nust2021practical-e1][^nust2021practical-e2]
- [ ] 数据不能公开时，发布保留空间结构的模拟数据[^kedron2021reproducibility-e9]

**审稿时常见、但不成立的批评**

- "数据不公开，所以不能发表。" Kedron 等人认为，因伦理原因或合作企业限制而不能共享数据的地理研究，不应因此被挡在发表之外[^kedron2021reproducibility-e11]；可以用模拟数据和公开代码来弥补[^kedron2021reproducibility-e9]。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不管坐标参考系，直接叠加或算距离 | 经纬度没有基准就没有明确含义[^pebesma2023spatial-e1]；投影会让面积或距离变形[^pebesma2023spatial-e2] |
| 用"相交"把点或区域汇总到新边界，不核对总数 | 同一条记录可能被算进多个区域[^pebesma2023spatial-e8] |
| 把人口密度这类比率按面积加总 | 比率切分后不能相加[^pebesma2023spatial-e10] |
| 只看地图就说"明显成团" | 人常把随机看成规律[^rey2023geographic-e13]，要做统计检验 |
| 用软件默认的彩虹色或红绿配色 | 彩虹色会不公平地突出一段数值[^crameri2020misuse-e3]；亮度相近的红绿，很多读者读不出[^crameri2020misuse-e4] |
| 偏态数据用等间距分级，不说明 | 可能出现几乎没有观测的级[^rey2023geographic-e6] |
| 空间自相关明显，仍用普通回归的显著性 | 普通最小二乘法会算错置信区间[^rey2023geographic-e21] |
| 拿 999 次置换的 p = 0.001 和 99 次的 p = 0.01 比显著性 | 伪 p 值和置换次数有关，不能直接比[^anselin2020global-e3] |
| 试了多种权重矩阵，只报最好的 | 其余检验从文献里消失[^kedron2021reproducibility-e3] |
| 发表参与者住处的点位图，以为没写地址就安全 | 点可以被反向地理编码对回地址[^zandbergen2014ensuring-e4][^kwan2012uncertain-e9] |
| 做了地理掩蔽，但不写方法和参数 | 读者无法判断隐私保护和分析精度的取舍[^zandbergen2014ensuring-e9][^malekzadeh2026ethical-e12] |
| 在图形界面里点完分析，再手工修图 | 别人和未来的自己都无法重跑[^nust2021practical-e1][^nust2021practical-e6] |

---

## 5. 延伸阅读

- **Rey、Arribas-Bel、Wolf，Geographic Data Science with Python**（免费在线教材，例子用 Python）：空间权重、分级统计地图、全局空间自相关、空间回归各有一章。做第 5–7 步时读。
- **Pebesma、Bivand，Spatial Data Science: With Applications in R**（免费在线教材，例子用 R）：第 2 章讲坐标和坐标参考系，第 5 章讲"属性属于点还是区域"和空间汇总。做第 3、4 步前读。
- **Anselin，GeoDa 工作手册中的 Global Spatial Autocorrelation 一章**（免费在线软件教程）：用图形界面软件 GeoDa 演示莫兰散点图和置换检验，适合第一次接触空间自相关。
- **Crameri 等 2020，The misuse of colour in science communication**（Nature Communications，开放获取）：作者对科学图件配色误用的看法，以及有哪些科学配色可用。画第一张图前读。
- **Zandbergen 2014，Ensuring Confidentiality of Geocoded Health Data**（开放获取）：以公共卫生数据为背景，讲反向地理编码的风险和各种地理掩蔽方法。发表点位数据前读。
- **Nüst、Pebesma 2021，Practical Reproducibility in Geography and Geosciences**（EarthArXiv 上的作者接受稿，免费）：脚本化流程、软件环境、在线服务和敏感数据的可复现做法。
- **Kedron 等 2021** 和 **关美宝 2012、2018**：为什么空间设定要事先计划、怎样交代空间单元。详见[地理学学科概况](../README.md#延伸阅读)。

[^zandbergen2014ensuring-e1]: Zandbergen 2014，第 2 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e1)
[^zandbergen2014ensuring-e2]: Zandbergen 2014，第 2 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e2)
[^zandbergen2014ensuring-e3]: Zandbergen 2014，第 3 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e3)
[^zandbergen2014ensuring-e4]: Zandbergen 2014，第 3 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e4)
[^zandbergen2014ensuring-e5]: Zandbergen 2014，第 5 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e5)
[^zandbergen2014ensuring-e6]: Zandbergen 2014，第 6 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e6)
[^zandbergen2014ensuring-e7]: Zandbergen 2014，第 7 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e7)
[^zandbergen2014ensuring-e8]: Zandbergen 2014，第 10 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e8)
[^zandbergen2014ensuring-e9]: Zandbergen 2014，第 7 节。[证据](../../../../sources/notes/zandbergen2014ensuring.md#e9)
[^nust2021practical-e1]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Creating reproducible workflows。[证据](../../../../sources/notes/nust2021practical.md#e1)
[^nust2021practical-e2]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Creating reproducible workflows。[证据](../../../../sources/notes/nust2021practical.md#e2)
[^nust2021practical-e3]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Creating reproducible workflows。[证据](../../../../sources/notes/nust2021practical.md#e3)
[^nust2021practical-e4]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Examples。[证据](../../../../sources/notes/nust2021practical.md#e4)
[^nust2021practical-e5]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Examples。[证据](../../../../sources/notes/nust2021practical.md#e5)
[^nust2021practical-e6]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Challenges。[证据](../../../../sources/notes/nust2021practical.md#e6)
[^nust2021practical-e7]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Challenges。[证据](../../../../sources/notes/nust2021practical.md#e7)
[^nust2021practical-e8]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Challenges。[证据](../../../../sources/notes/nust2021practical.md#e8)
[^nust2021practical-e9]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Challenges。[证据](../../../../sources/notes/nust2021practical.md#e9)
[^nust2021practical-e10]: Nüst & Pebesma 2021（EarthArXiv 作者接受稿），Challenges。[证据](../../../../sources/notes/nust2021practical.md#e10)
[^kwan2018limits-e1]: Kwan 2018，第 1486 页。[证据](../../../../sources/notes/kwan2018limits.md#e1)
[^kwan2018limits-e2]: Kwan 2018，第 1486 页。[证据](../../../../sources/notes/kwan2018limits.md#e2)
[^kwan2012uncertain-e4]: Kwan 2012，第 959 页。[证据](../../../../sources/notes/kwan2012uncertain.md#e4)
[^kwan2012uncertain-e6]: Kwan 2012，第 963 页。[证据](../../../../sources/notes/kwan2012uncertain.md#e6)
[^kwan2012uncertain-e7]: Kwan 2012，第 963–964 页。[证据](../../../../sources/notes/kwan2012uncertain.md#e7)
[^kwan2012uncertain-e9]: Kwan 2012，第 966 页注 2。[证据](../../../../sources/notes/kwan2012uncertain.md#e9)
[^kedron2021reproducibility-e4]: Kedron 等 2021，§3.1。[证据](../../../../sources/notes/kedron2021reproducibility.md#e4)
[^kedron2021reproducibility-e3]: Kedron 等 2021，§2。[证据](../../../../sources/notes/kedron2021reproducibility.md#e3)
[^kedron2021reproducibility-e13]: Kedron 等 2021，§4.2。[证据](../../../../sources/notes/kedron2021reproducibility.md#e13)
[^kedron2021reproducibility-e9]: Kedron 等 2021，§3.2。[证据](../../../../sources/notes/kedron2021reproducibility.md#e9)
[^kedron2021reproducibility-e11]: Kedron 等 2021，§3.2。[证据](../../../../sources/notes/kedron2021reproducibility.md#e11)
[^rey2023geographic-e1]: Rey 等 2023（在线教材），Spatial Weights。[证据](../../../../sources/notes/rey2023geographic.md#e1)
[^rey2023geographic-e2]: Rey 等 2023（在线教材），Spatial Weights。[证据](../../../../sources/notes/rey2023geographic.md#e2)
[^rey2023geographic-e3]: Rey 等 2023（在线教材），Spatial Weights。[证据](../../../../sources/notes/rey2023geographic.md#e3)
[^rey2023geographic-e4]: Rey 等 2023（在线教材），Spatial Weights。[证据](../../../../sources/notes/rey2023geographic.md#e4)
[^rey2023geographic-e5]: Rey 等 2023（在线教材），Choropleth Mapping。[证据](../../../../sources/notes/rey2023geographic.md#e5)
[^rey2023geographic-e6]: Rey 等 2023（在线教材），Choropleth Mapping。[证据](../../../../sources/notes/rey2023geographic.md#e6)
[^rey2023geographic-e7]: Rey 等 2023（在线教材），Choropleth Mapping。[证据](../../../../sources/notes/rey2023geographic.md#e7)
[^rey2023geographic-e8]: Rey 等 2023（在线教材），Choropleth Mapping。[证据](../../../../sources/notes/rey2023geographic.md#e8)
[^rey2023geographic-e9]: Rey 等 2023（在线教材），Choropleth Mapping。[证据](../../../../sources/notes/rey2023geographic.md#e9)
[^rey2023geographic-e10]: Rey 等 2023（在线教材），Choropleth Mapping。[证据](../../../../sources/notes/rey2023geographic.md#e10)
[^rey2023geographic-e11]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../../../sources/notes/rey2023geographic.md#e11)
[^rey2023geographic-e12]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../../../sources/notes/rey2023geographic.md#e12)
[^rey2023geographic-e13]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../../../sources/notes/rey2023geographic.md#e13)
[^rey2023geographic-e14]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../../../sources/notes/rey2023geographic.md#e14)
[^rey2023geographic-e15]: Rey 等 2023（在线教材），Global Spatial Autocorrelation。[证据](../../../../sources/notes/rey2023geographic.md#e15)
[^rey2023geographic-e16]: Rey 等 2023（在线教材），Spatial Regression。[证据](../../../../sources/notes/rey2023geographic.md#e16)
[^rey2023geographic-e17]: Rey 等 2023（在线教材），Spatial Regression。[证据](../../../../sources/notes/rey2023geographic.md#e17)
[^rey2023geographic-e18]: Rey 等 2023（在线教材），Spatial Regression。[证据](../../../../sources/notes/rey2023geographic.md#e18)
[^rey2023geographic-e19]: Rey 等 2023（在线教材），Spatial Regression。[证据](../../../../sources/notes/rey2023geographic.md#e19)
[^rey2023geographic-e20]: Rey 等 2023（在线教材），Spatial Regression。[证据](../../../../sources/notes/rey2023geographic.md#e20)
[^rey2023geographic-e21]: Rey 等 2023（在线教材），Spatial Regression，练习题。[证据](../../../../sources/notes/rey2023geographic.md#e21)
[^pebesma2023spatial-e1]: Pebesma & Bivand 2023（在线教材），第 2 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e1)
[^pebesma2023spatial-e2]: Pebesma & Bivand 2023（在线教材），第 2 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e2)
[^pebesma2023spatial-e3]: Pebesma & Bivand 2023（在线教材），第 2 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e3)
[^pebesma2023spatial-e4]: Pebesma & Bivand 2023（在线教材），第 2 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e4)
[^pebesma2023spatial-e5]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e5)
[^pebesma2023spatial-e6]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e6)
[^pebesma2023spatial-e7]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e7)
[^pebesma2023spatial-e8]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e8)
[^pebesma2023spatial-e9]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e9)
[^pebesma2023spatial-e10]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e10)
[^pebesma2023spatial-e11]: Pebesma & Bivand 2023（在线教材），第 5 章。[证据](../../../../sources/notes/pebesma2023spatial.md#e11)
[^crameri2020misuse-e2]: Crameri 等 2020，引言。[证据](../../../../sources/notes/crameri2020misuse.md#e2)
[^crameri2020misuse-e3]: Crameri 等 2020，引言。[证据](../../../../sources/notes/crameri2020misuse.md#e3)
[^crameri2020misuse-e4]: Crameri 等 2020，引言。[证据](../../../../sources/notes/crameri2020misuse.md#e4)
[^crameri2020misuse-e5]: Crameri 等 2020，引言。[证据](../../../../sources/notes/crameri2020misuse.md#e5)
[^crameri2020misuse-e6]: Crameri 等 2020，Box 2。[证据](../../../../sources/notes/crameri2020misuse.md#e6)
[^crameri2020misuse-e7]: Crameri 等 2020，正文。[证据](../../../../sources/notes/crameri2020misuse.md#e7)
[^anselin2020global-e1]: Anselin 2020（GeoDa 工作手册），Moran's I。[证据](../../../../sources/notes/anselin2020global.md#e1)
[^anselin2020global-e2]: Anselin 2020（GeoDa 工作手册），Permutation inference。[证据](../../../../sources/notes/anselin2020global.md#e2)
[^anselin2020global-e3]: Anselin 2020（GeoDa 工作手册），Permutation inference。[证据](../../../../sources/notes/anselin2020global.md#e3)
[^anselin2020global-e4]: Anselin 2020（GeoDa 工作手册），Interpretation。[证据](../../../../sources/notes/anselin2020global.md#e4)
[^anselin2020global-e5]: Anselin 2020（GeoDa 工作手册），Inference。[证据](../../../../sources/notes/anselin2020global.md#e5)
[^anselin2020global-e6]: Anselin 2020（GeoDa 工作手册），Inference。[证据](../../../../sources/notes/anselin2020global.md#e6)
[^anselin2020global-e7]: Anselin 2020（GeoDa 工作手册），Moran scatter plot as a standard scatter plot。[证据](../../../../sources/notes/anselin2020global.md#e7)
[^anselin2020global-e8]: Anselin 2020（GeoDa 工作手册），Interpretation。[证据](../../../../sources/notes/anselin2020global.md#e8)
[^malekzadeh2026ethical-e12]: Malekzadeh 等 2026，Q27。[证据](../../../../sources/notes/malekzadeh2026ethical.md#e12)
[^malekzadeh2026ethical-e13]: Malekzadeh 等 2026，Q26。[证据](../../../../sources/notes/malekzadeh2026ethical.md#e13)
[^malekzadeh2026ethical-e14]: Malekzadeh 等 2026，Q11。[证据](../../../../sources/notes/malekzadeh2026ethical.md#e14)
