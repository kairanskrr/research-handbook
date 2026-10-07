# 材料工程与纳米技术：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲材料工程的研究实际怎样运转，也包括纳米技术。在本项目采用的学科分类里，材料工程是 2.5，纳米技术是 2.10（见[领域篇总览](../README.md)），本文把两者放在一起讲。这个领域和化学、物理、生物、电子工程都有大片交叉：合成和化学实验的通用规范见[化学领域篇](../chemistry/README.md)，凝聚态物理和预印本文化见[物理科学篇](../physical-sciences/README.md)，纳米材料进入细胞和动物实验的部分见[生物科学篇](../biological-sciences/README.md)。各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[通用篇](../../README.md)。这里只写本领域特有的东西。

**读完本文，你应该能：**

- 说清"制备—表征—性能测试"这个循环，以及共享表征平台和计算在其中的位置；
- 知道写材料和器件论文时要报告哪些信息，以纳米材料的最低信息报告和太阳能电池报告表为例；
- 认识批次差异和只报"冠军器件"这两个常见的可重复性问题；
- 知道材料数据怎样按 FAIR 原则共享，以及在实验室里怎样安全地操作纳米材料。

---

## 本领域研究怎样运转

### 一个循环：制备、表征、测性能

本领域的很多实验研究围绕一个循环展开 `[本项目分析]`：

1. **制备**（合成或加工）：做出材料、薄膜或器件；
2. **表征**：用显微镜、衍射、光谱等手段弄清做出来的是什么（成分、结构、尺寸、表面）；
3. **性能测试**：测它在目标用途上表现如何（强度、导电性、光电转换效率、催化活性等）；
4. 根据结果调整制备条件，再来一轮。

要特别留意第一步：怎么做出来的，会影响做出来的是什么 `[本项目分析]`。合成路线会影响纳米材料的性质，包括毒性；二氧化硅、氧化铈、银等多种材料都有报道[^mulhopt2018characterization-e5]。所以 Faria 等人建议，新发表的纳米材料要给出高质量、别人能照着做的合成步骤；纯化方法也要写，因为前驱体（合成用的原料）残留可能改变生物学实验的结果[^faria2018minimum-e3]。

**什么算"纳米"。** 一种界定是：至少有一个维度在 1–100 纳米之间。美国国家职业安全卫生研究所（NIOSH）2009 年的文件对工程纳米颗粒就是这样定义的[^niosh2009approaches-e1]；Faria 等人也把"至少一个功能尺寸在 1–100 纳米"列为可选的界定办法之一[^faria2018minimum-e15]。读文献时注意作者用的是哪种定义 `[本项目分析]`。

### 表征常常要借用共享平台

电子显微镜等高端表征设备一般不在每个课题组里，很多时候要用学校的公共测试平台或国家级的用户设施 `[本项目分析]`。下面举一个具体例子：美国能源部的一个纳米科学用户设施 Molecular Foundry（设在劳伦斯伯克利国家实验室）。它只是一家设施的规则；其他国家、其他平台的规则不同，以你实际使用的平台为准 `[本项目分析]`。

- **要申请。** 任何有兴趣的研究者都可以申请，申请要经过竞争性的同行评审[^lblfoundryuser-e1]，一般在每年两次的征集中提交[^lblfoundryuser-e4]。
- **不保密的研究免费，保密的付费。** 非专有（不保密）的研究免费使用[^lblfoundryuser-e2]；专有（保密）项目在进行期间按全成本付费[^lblfoundryuser-e3]。
- **先培训再上手。** 到了设施，开始工作前还要上额外的安全培训课[^lblfoundryuser-e5]。
- **发表时要致谢。** 用到该设施的成果，要在致谢中按规定措辞写上它[^lblfoundryuser-e6]。

这对研究节奏的影响是：机时要提前申请和预约，样品要提前准备好，测试方案要在上机前想清楚 `[本项目分析]`。排期的通用方法见通用篇[推进研究](../../08_throughout/planning_and_routines.md)。

### 计算：密度泛函理论和高通量筛选

很多课题会配合计算，常用的一种是**密度泛函理论**（density functional theory，DFT），一种从量子力学出发计算原子尺度结构和性质的方法 `[本项目分析]`。按 Lejaeghere 等人 2016 年文中的说法，每年发表的密度泛函理论论文超过 1.5 万篇，它也越来越多地被自动化使用，用来建大型数据库[^lejaeghere2016reproducibility-e1]。**高通量筛选**是一次计算成千上万个结构的性质[^draxl2018nomad-e3]，用来寻找有希望的材料 `[本项目分析]`。

计算也有可复现问题。计算程序很多，实现细节差别很大[^lejaeghere2016reproducibility-e2]。Lejaeghere 等人组织了一次社区合作，比较了 15 个程序、40 种势或基组在 71 种单质晶体上的结果[^lejaeghere2016reproducibility-e3]。（势和基组是计算里描述原子和电子的近似设置，通常以文件形式随程序提供 `[本项目分析]`。）结论是：较新的程序和赝势（一类常用的势）之间非常一致，差别和不同高精度实验之间的差别相当；较老的方法一致性差一些[^lejaeghere2016reproducibility-e4]。因此他们主张只用某个程序最新版的势文件[^lejaeghere2016reproducibility-e5]。他们也承认，要完整说明一次计算，连程序默认值和写死在代码里的参数都得写上[^lejaeghere2016reproducibility-e6]。对新手来说，这意味着论文里至少要写明程序名和版本、势文件或基组、主要数值设置 `[本项目分析]`。仿真研究的一般做法见计算机篇[定量仿真](../../06_methods/simulation_study.md)。

### 发表

本文资料没有找到关于本领域署名惯例、审稿周期、期刊和会议地位的可靠公开说明，这些以导师和目标期刊的要求为准。能确定的几点：

- **有预印本渠道。** 预印本是正式发表前先公开的论文稿 `[本项目分析]`。预印本网站 arXiv 设有材料科学分类 cond-mat.mtrl-sci，覆盖合成、表征、结构、力学性质、缺陷、界面等[^arxivtaxonomy-e7]；纳米结构的物理研究（量子点、纳米管、石墨烯等）在介观与纳米物理分类 cond-mat.mes-hall[^arxivtaxonomy-e8]。偏化学的工作，发表规范可参考[化学领域篇](../chemistry/README.md) `[本项目分析]`。
- **期刊可能要求公开材料和数据。** 以 Nature Portfolio 期刊为例，发表的条件之一是及时向读者提供材料、数据、代码和流程[^naturereportingstandards-e1]；获取上有任何限制，投稿时就要告诉编辑[^naturereportingstandards-e3]。其他出版方的规定可能不同，投稿前查目标期刊 `[本项目分析]`。

---

## 和其他学科不同的地方

下表是本项目的归纳，用来帮你快速定位差别，不是严格的学科划分 `[本项目分析]`。

| | 材料工程与纳米技术 | 化学 | 计算机 |
|---|---|---|---|
| 研究对象 | 材料和器件的结构与性能 | 分子和反应 | 算法、系统、数据 |
| 典型证据 | 制备方法 + 多种表征 + 性能数据 | 合成路线 + 结构鉴定（见[化学领域篇](../chemistry/README.md)） | 代码和数据上的实验（见[计算机领域篇](../computer-science/README.md)） |
| 常见的变异来源 | 批次之间、器件之间、实验室之间的差异（纳米颗粒和钙钛矿电池研究里都有报道[^mulhopt2018characterization-e3][^jacobsson2022open-e4][^jacobsson2022open-e5]） | 本文不讨论，见化学篇 | 随机种子、软硬件环境 |
| 报告规范 | 按材料类型和用途分散制定，例如纳米—生物研究的最低信息标准、太阳能电池报告表（见下文） | 见化学篇 | 制品评估等（见计算机篇） |
| 安全 | 做纳米材料时，除化学品安全外，还要考虑纳米颗粒吸入和燃爆（见下文） | 化学品安全 | 一般不涉及实验室安全 |

---

## 本领域的规范和报告标准

### 最低信息报告：以纳米—生物研究为例

不同论文做了哪些表征、写了哪些实验细节差别很大，这是纳米—生物交叉研究进展的一大障碍[^faria2018minimum-e1]。2018 年，Faria 等人一批研究者在 Nature Nanotechnology 上提出了**最低信息报告标准** MIRIBEL（Minimum Information Reporting in Bio–Nano Experimental Literature，生物—纳米实验文献最低信息报告），分三类条目：材料表征、生物学表征、实验流程细节[^faria2018minimum-e2]，并配了一份写稿时逐项核对用的清单[^faria2018minimum-e14]。注意：MIRIBEL 是一批研究者提出的建议，不是期刊的硬性要求 `[本项目分析]`；作者自己也说，标准只有被广泛采用才有用[^faria2018minimum-e13]。投稿时以目标期刊的要求为准 `[本项目分析]`。

它的材料表征部分对做纳米材料的人都有参考价值 `[本项目分析]`：

- **写清每个参数怎么测的**：什么技术、什么仪器、什么流程[^faria2018minimum-e6]。测粒径时，还要写明测的是哪一种尺寸，例如几何尺寸还是在液体中的水合尺寸[^faria2018minimum-e5]。
- **报分布，不只报平均值。** 10–990 纳米均匀分布的颗粒和 495–505 纳米的颗粒，平均粒径都是 500 纳米，但只看平均值，没法判断它们的生物学效应[^faria2018minimum-e4]。几乎所有表征参数都是一个分布，给出分布比只给一个平均值信息更多[^faria2018minimum-e10]。
- **用两种以上独立方法**表征同一性质，价值大得多[^faria2018minimum-e7]。
- **说明波动来自哪里**：是同一批材料测了多次，还是做了多个批次[^faria2018minimum-e8]。
- **尽量在接近后续实验所用液体的介质中表征**，例如做细胞实验就在相近的液体里测[^faria2018minimum-e9]。
- **写清统计信息**：独立实验次数，以及用标准差、标准误还是置信区间表示不确定性[^faria2018minimum-e11]；尽可能提供原始数据[^faria2018minimum-e12]。

动物实验部分，MIRIBEL 写明要遵循动物研究报告指南 ARRIVE[^faria2018minimum-e16]，见[生物科学篇](../biological-sciences/README.md)。统计的通用做法见通用篇[证据与效度](../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

### 器件性能报告：以太阳能电池为例

器件性能（如太阳能电池把光变成电的效率）受测量条件影响，有的期刊为此专门制定了报告表 `[本项目分析]`。下面的例子都来自 Nature 系列期刊（出版方名为 Nature Portfolio）。2015 年，Nature Materials 宣布要求光伏（太阳能发电）论文的作者填写一份关键技术信息清单[^naturematerials2015checklist-e1]，内容由太阳能电池专家和 Nature 系列期刊编辑讨论确定[^naturematerials2015checklist-e2]。现在 Nature Portfolio 对物理科学中的太阳能电池和激光两个方向要求提交报告摘要表[^naturereportingstandards-e2]，太阳能电池的表格随录用论文一起发表[^naturesolarcellsreporting-e1]。这两份文件要求的信息包括：

- 正向和反向两个扫描方向的电流密度—电压曲线（即 J-V 曲线，电池输出电流随电压变化的曲线）[^naturesolarcellsreporting-e2]，以及扫描条件、电池面积[^naturematerials2015checklist-e3]；
- 测试了多少块电池，以及器件性能的统计分析[^naturesolarcellsreporting-e4][^naturesolarcellsreporting-e5]；
- 是否经过独立认证实验室确认，是哪一家[^naturesolarcellsreporting-e3][^naturematerials2015checklist-e4]。

2015 年那篇社论还提出：报告最好器件的同时报告平均效率[^naturematerials2015checklist-e5]；作者要格外仔细地描述所用的表征流程，并给出性能可重复的统计证据[^naturematerials2015checklist-e6]。为某种光伏技术优化的测量流程，不一定能直接用到别的体系[^naturematerials2015checklist-e7]。报告表还提到，ASTM-E44、IEC-TC 82 等国际委员会制定的光伏表征行业标准可供学术研究参考[^naturesolarcellsreporting-e6]。

以上是 Nature 系列期刊的规定，不是整个领域的统一要求；投其他期刊，以对方要求为准。即使对方不要求，这份表格也可以拿来自查 `[本项目分析]`。

### 可重复性：批次差异和"冠军器件"

**批次差异。** 同一种材料，每批做出来可能不一样。Mülhopt 等人 2018 年在论文引言中指出，目前工业和实验室的纳米材料合成工艺，批次之间差异相当显著[^mulhopt2018characterization-e3]。他们的项目由欧洲 14 个实验室历时三年多完成[^mulhopt2018characterization-e1]，完整表征了 46 个批次[^mulhopt2018characterization-e2]。结果是：ζ 电位（反映颗粒表面带电情况的指标 `[本项目分析]`）、粒径等参数批次间比较稳定，杂质等参数控制得不够好[^mulhopt2018characterization-e7]。他们还提出，单个批次能在多大程度上代表多个批次，本身就是个问题[^mulhopt2018characterization-e4]；纳米颗粒常团聚，粒径分布应当用几种方法测[^mulhopt2018characterization-e6]。

钙钛矿太阳能电池（一类新型太阳能电池）研究里也有类似问题。Jacobsson 等人 2022 年在这类电池的数据库论文中指出，电池之间、批次之间的差异可能很大，会掩盖本来统计上显著的差别；他们也说这不是钙钛矿领域独有的问题[^jacobsson2022open-e4]。还有实验室之间的差异，通常被归因于论文里没写出来的"隐藏参数"[^jacobsson2022open-e5]。他们猜测的例子有手套箱体积、制备时的气氛成分、前驱体配比的细微变化、化学杂质，并说明这些只是假设[^jacobsson2022open-e6]。所以这些看似琐碎的条件，也值得记在实验记录里 `[本项目分析]`。

**只报"冠军器件"。** Jacobsson 等人人工查阅了截至 2020 年 2 月的 1.5 万多篇钙钛矿太阳能电池论文，提取了 4.24 万多个器件的数据[^jacobsson2022open-e3]。他们发现，一个典型项目写论文前可能做了成百上千个器件，但在含原始器件数据的论文中，平均每篇能提取到数据的器件不到 6 个[^jacobsson2022open-e7]；常见的情况是一个参数改几档，每档只给出最好那个器件的数据[^jacobsson2022open-e8]。这组数字只来自钙钛矿太阳能电池论文，不能直接推广到整个材料领域；但只看最好的器件，读者无法判断结果有多容易重复，这一点对其他器件研究同样值得注意 `[本项目分析]`。可以参考上文 Nature 系列期刊的做法：说明测了多少个器件[^naturesolarcellsreporting-e4]，报告最好器件的同时报告平均值[^naturematerials2015checklist-e5]。报告全部结果的通用原则见通用篇[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#2-对证据诚实不骗自己报告全部结果)。

### 材料数据共享与 FAIR 原则

**FAIR 原则**是学术界、产业界、资助机构和出版方的代表共同设计并认可的一套数据管理原则，2016 年正式发表[^wilkinson2016fair-e6]；四个字母分别代表可查找、可获取、可互操作、可重用[^wilkinson2016fair-e2]。它特别强调让计算机能自动找到和使用数据[^wilkinson2016fair-e1]。具体要求包括：数据有长期有效的唯一标识符[^wilkinson2016fair-e3]；附明确的使用许可和详细的来源信息[^wilkinson2016fair-e4]。FAIR 不等于全部公开：数据本身不能公开时，公开详细的描述信息和获取规则，也能达到较高的 FAIR 程度[^wilkinson2016fair-e5]。

实验数据做到 FAIR 并不容易。钙钛矿数据库的作者 Jacobsson 等人认为，多数实验室做不到 FAIR，应用科学领域尤其如此[^jacobsson2022open-e1]；他们认为最大的障碍是数据多样又复杂，例如样品性质常受它的制备和处理历史影响[^jacobsson2022open-e2]。Draxl 和 Scheffler 也指出，实验样品的质量常常没有充分表征，而且很大程度上取决于样品的历史[^draxl2018nomad-e7]；要让实验数据能被再利用，必须定义好关于实验、样品和数据的描述信息[^draxl2018nomad-e8]。

计算数据有专门的数据库可存，NOMAD 是一个例子。它的建设者 Draxl 和 Scheffler 指出，高通量计算产生的信息只有极小一部分被用上[^draxl2018nomad-e1]，论文之外的大量信息通常被丢弃甚至删掉[^draxl2018nomad-e2]。按他们 2018 年的介绍，NOMAD 数据库接收计算程序直接输出的原始文件，条件是写明作者、能查到程序和版本、输入输出文件完整[^draxl2018nomad-e5]；数据可以先不公开，但最长三年后全部公开[^draxl2018nomad-e6]；免费保存至少 10 年，也方便课题组回忆几年前到底做了什么[^draxl2018nomad-e4]。现行规则以 NOMAD 官网为准 `[本项目分析]`。

Jacobsson 等人认为，共享数据对自己也有好处：能让数据被再利用、给原论文带来更多关注，也能回应纳税人、资助机构和出版方对开放的要求[^jacobsson2022open-e9]。整理数据的通用方法见通用篇[整理科研材料](../../08_throughout/organizing_materials.md#2-原始数据只读其余都能重新生成)。

### 纳米材料的实验室安全（以美国 NIOSH 指南为例）

下面的建议来自美国国家职业安全卫生研究所（NIOSH）2009 年的指南 Approaches to Safe Nanotechnology。它是美国机构 2009 年的文件，不是各国通行的规定；中国和其他国家的规定、你所在单位的安全制度可能不同，以本单位的要求为准 `[本项目分析]`。

- **风险未知，先预防。** 在研究弄清哪些纳米颗粒特性可能危害健康之前，有必要采取预防措施[^niosh2009approaches-e2]。
- **最怕吸入。** 纳米材料一旦飘在空气中，最可能经呼吸道进入人体[^niosh2009approaches-e3]。NIOSH 建议避免在敞开环境中以自由颗粒的状态操作[^niosh2009approaches-e10]，易分散的材料尽量密封存放[^niosh2009approaches-e7]。
- **用排风和过滤。** 设计良好、带高效空气过滤器（HEPA）的排风系统应能有效去除纳米材料[^niosh2009approaches-e4]。
- **清洁和个人习惯。** 用带 HEPA 过滤器的吸尘器和湿擦清洁，操作区禁止饮食，提供洗手设施[^niosh2009approaches-e5]；不要干扫或用气枪吹[^niosh2009approaches-e8]。
- **不要照搬普通粉尘的限值。** 针对非纳米颗粒的接触限值，对纳米颗粒未必能保护健康[^niosh2009approaches-e6]。
- **注意燃爆。** 可燃材料粒径变小，燃烧可能性和速率会增加，相对惰性的材料到纳米尺度可能变得高度活泼[^niosh2009approaches-e9]。

---

## 常见的研究类型

**相关学科的研究类型文档**：[合成与表征研究](../chemistry/research-types/synthesis_study.md)、[实验测量研究](../physical-sciences/research-types/experimental_measurement.md)。

本领域常用的方法，有不少和计算机领域相通，可以直接参考对应文档。下面只写本领域额外要注意的地方：

- **合成与表征研究**（计算机篇没有对应文档）：做出新材料并弄清它的结构和性质。要点是可重复的合成步骤、多种独立的表征方法、说明批次情况[^faria2018minimum-e3][^faria2018minimum-e7][^faria2018minimum-e8]。
- [工程研究](../computer-science/practices/engineering_research.md)：设计并做出新器件、新工艺，再评估性能。器件结果要说明做了多少个，最好值和平均值一起报[^naturesolarcellsreporting-e4][^naturematerials2015checklist-e5]。
- [定量仿真](../../06_methods/simulation_study.md)：密度泛函理论计算、分子动力学等。要写明程序、版本和势文件，优先用最新的势文件[^lejaeghere2016reproducibility-e5]。
- [基准评测](../computer-science/practices/benchmarking.md)：在相同条件下比较多种方法。Lejaeghere 等人比较多个计算程序的工作就是一例[^lejaeghere2016reproducibility-e3]。
- [数据科学](../../06_methods/data_science.md)：在材料数据库上做挖掘和机器学习。要注意实验数据受样品历史影响，样品质量也常常没有充分表征[^jacobsson2022open-e2][^draxl2018nomad-e7]。
- [复现研究](../../06_methods/replication.md)：重做已发表的合成或器件。复现不出来时，可以先排查批次差异和论文没写的"隐藏参数" `[本项目分析]`，后者常被认为是实验室之间结果不一致的原因[^jacobsson2022open-e5]。
- **纳米材料的生物效应和安全性研究**：要同时遵守材料表征和生物实验两套规范，见上文最低信息报告和[生物科学篇](../biological-sciences/README.md)。

---

## 给新手的建议

1. **从第一批样品起就记"琐碎"条件。** Jacobsson 等人在钙钛矿电池研究中猜测，手套箱体积、制备气氛、前驱体配比、杂质都可能是"隐藏参数"[^jacobsson2022open-e6]，记下来，日后排查才有依据 `[本项目分析]`。实验记录的通用做法见通用篇[推进研究](../../03_conduct-and-analyze/01_run-and-iterate.md#3-每次运行都留下记录)。
2. **每个关键性质至少用两种方法表征**，并写清每种方法的仪器和流程[^faria2018minimum-e6][^faria2018minimum-e7]。
3. **做多个批次、多个器件，报告分布。** 说明测了多少个、波动来自同一批还是多个批次，再给平均值和最好值[^naturesolarcellsreporting-e4][^naturematerials2015checklist-e5][^faria2018minimum-e8]。
4. **写论文前，对照目标期刊的报告表自查。** 没有专门报告表的方向，可以借用相近方向的清单，例如 MIRIBEL[^faria2018minimum-e14]或太阳能电池报告表 `[本项目分析]`。
5. **共享平台的机时提前申请**，上机前把样品和测试方案准备好；发表时别忘了致谢平台[^lblfoundryuser-e6] `[本项目分析]`。
6. **计算工作保留完整的输入输出文件**，写明程序版本和势文件[^lejaeghere2016reproducibility-e5]；可以考虑存到公开的材料数据库[^draxl2018nomad-e5]。
7. **第一次操作纳米粉末前，先完成本单位的安全培训**，问清通风、存放和清洁要求[^niosh2009approaches-e3][^niosh2009approaches-e4] `[本项目分析]`。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只报平均粒径 | 平均值相同的两批颗粒，粒径范围可能差很远，只看平均值没法判断生物学效应[^faria2018minimum-e4] |
| 只写"用某仪器测得"，不写方法和测的是哪种尺寸 | 测量流程和尺寸类型都要写清[^faria2018minimum-e5][^faria2018minimum-e6] |
| 只做一个批次，就当作这种材料的性质 | 纳米材料合成的批次差异可能相当显著[^mulhopt2018characterization-e3]，单个批次未必有代表性[^mulhopt2018characterization-e4] |
| 只报"冠军器件"，不说测了多少个 | 读者无法判断结果有多容易重复；Nature Materials 社论建议同时报告平均效率[^naturematerials2015checklist-e5] |
| 太阳能电池只给一个扫描方向的曲线 | Nature 系列期刊的报告表要求正反两个方向[^naturesolarcellsreporting-e2] |
| 计算用旧版势文件，也不写程序版本 | 较老的方法和势文件结果一致性差[^lejaeghere2016reproducibility-e4][^lejaeghere2016reproducibility-e5] |
| 数据只留下写进论文的几张图 | 论文之外的大量信息常被丢弃甚至删掉[^draxl2018nomad-e2]，别人和自己以后都用不上 `[本项目分析]` |
| 在敞开的台面上称量、转移纳米粉末，用干扫清理 | NIOSH 建议避免敞开操作，不要干扫或用气枪吹[^niosh2009approaches-e10][^niosh2009approaches-e8] |

---

## 延伸阅读

- **Faria 等人 2018，Minimum information reporting in bio–nano experimental literature**：纳米—生物研究的最低信息报告建议（MIRIBEL），附写稿用的清单。做纯材料的人可以重点读材料表征部分 `[本项目分析]`。
- **Nature 系列期刊的太阳能电池报告摘要表（Solar Cells Reporting Summary），以及 Nature Materials 2015 年社论 A checklist for photovoltaic research**：做光伏的人投稿前可以用来自查 `[本项目分析]`。
- **Jacobsson 等人 2022，An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles**：看钙钛矿太阳能电池方向的上万篇论文汇总起来是什么样子，以及只报最好器件、批次差异带来的问题。
- **Wilkinson 等人 2016，The FAIR Guiding Principles**：FAIR 原则的原始文献。
- **Lejaeghere 等人 2016，Reproducibility in density functional theory calculations of solids**：做计算的人了解不同程序之间差多少、怎样选择势文件。
- **NIOSH 2009，Approaches to Safe Nanotechnology**：美国机构关于纳米材料职业安全的指南。它是 2009 年的文件，实际操作以本单位的安全制度为准。

[^mulhopt2018characterization-e1]: Mülhopt 等人 2018，摘要。[证据](../../../sources/notes/mulhopt2018characterization.md#e1)
[^mulhopt2018characterization-e2]: Mülhopt 等人 2018，摘要。[证据](../../../sources/notes/mulhopt2018characterization.md#e2)
[^mulhopt2018characterization-e3]: Mülhopt 等人 2018，§1 Introduction。[证据](../../../sources/notes/mulhopt2018characterization.md#e3)
[^mulhopt2018characterization-e4]: Mülhopt 等人 2018，§1 Introduction。[证据](../../../sources/notes/mulhopt2018characterization.md#e4)
[^mulhopt2018characterization-e5]: Mülhopt 等人 2018，§1 Introduction。[证据](../../../sources/notes/mulhopt2018characterization.md#e5)
[^mulhopt2018characterization-e6]: Mülhopt 等人 2018，§4 Discussion。[证据](../../../sources/notes/mulhopt2018characterization.md#e6)
[^mulhopt2018characterization-e7]: Mülhopt 等人 2018，§4 Discussion。[证据](../../../sources/notes/mulhopt2018characterization.md#e7)
[^faria2018minimum-e1]: Faria 等人 2018，摘要。[证据](../../../sources/notes/faria2018minimum.md#e1)
[^faria2018minimum-e2]: Faria 等人 2018，摘要。[证据](../../../sources/notes/faria2018minimum.md#e2)
[^faria2018minimum-e3]: Faria 等人 2018，Material Characterisation：Synthesis and composition。[证据](../../../sources/notes/faria2018minimum.md#e3)
[^faria2018minimum-e4]: Faria 等人 2018，Material Characterisation：Size dispersity and aggregation。[证据](../../../sources/notes/faria2018minimum.md#e4)
[^faria2018minimum-e5]: Faria 等人 2018，Material Characterisation：Size, shape, and dimensions。[证据](../../../sources/notes/faria2018minimum.md#e5)
[^faria2018minimum-e6]: Faria 等人 2018，Material Characterisation：General guidelines。[证据](../../../sources/notes/faria2018minimum.md#e6)
[^faria2018minimum-e7]: Faria 等人 2018，Material Characterisation：General guidelines。[证据](../../../sources/notes/faria2018minimum.md#e7)
[^faria2018minimum-e8]: Faria 等人 2018，Material Characterisation：General guidelines。[证据](../../../sources/notes/faria2018minimum.md#e8)
[^faria2018minimum-e9]: Faria 等人 2018，Material Characterisation：General guidelines。[证据](../../../sources/notes/faria2018minimum.md#e9)
[^faria2018minimum-e10]: Faria 等人 2018，Material Characterisation：General guidelines。[证据](../../../sources/notes/faria2018minimum.md#e10)
[^faria2018minimum-e11]: Faria 等人 2018，Experimental Protocol Details：Details of data analysis。[证据](../../../sources/notes/faria2018minimum.md#e11)
[^faria2018minimum-e12]: Faria 等人 2018，Experimental Protocol Details：General guidelines。[证据](../../../sources/notes/faria2018minimum.md#e12)
[^faria2018minimum-e13]: Faria 等人 2018，Summary and Outlook。[证据](../../../sources/notes/faria2018minimum.md#e13)
[^faria2018minimum-e14]: Faria 等人 2018，引言。[证据](../../../sources/notes/faria2018minimum.md#e14)
[^faria2018minimum-e15]: Faria 等人 2018，Defining the Scope of a Minimum Information Standard。[证据](../../../sources/notes/faria2018minimum.md#e15)
[^faria2018minimum-e16]: Faria 等人 2018，Biological Characterisation：ARRIVE guidelines。[证据](../../../sources/notes/faria2018minimum.md#e16)
[^niosh2009approaches-e1]: NIOSH 2009，Executive Summary。[证据](../../../sources/notes/niosh2009approaches.md#e1)
[^niosh2009approaches-e2]: NIOSH 2009，Executive Summary。[证据](../../../sources/notes/niosh2009approaches.md#e2)
[^niosh2009approaches-e3]: NIOSH 2009，Executive Summary。[证据](../../../sources/notes/niosh2009approaches.md#e3)
[^niosh2009approaches-e4]: NIOSH 2009，Executive Summary。[证据](../../../sources/notes/niosh2009approaches.md#e4)
[^niosh2009approaches-e5]: NIOSH 2009，Executive Summary。[证据](../../../sources/notes/niosh2009approaches.md#e5)
[^niosh2009approaches-e6]: NIOSH 2009，Executive Summary。[证据](../../../sources/notes/niosh2009approaches.md#e6)
[^niosh2009approaches-e7]: NIOSH 2009，§8.3.3 Work practices。[证据](../../../sources/notes/niosh2009approaches.md#e7)
[^niosh2009approaches-e8]: NIOSH 2009，§8.3.3 Work practices。[证据](../../../sources/notes/niosh2009approaches.md#e8)
[^niosh2009approaches-e9]: NIOSH 2009，§6.1 Fire and Explosion Risk。[证据](../../../sources/notes/niosh2009approaches.md#e9)
[^niosh2009approaches-e10]: NIOSH 2009，§8.3.3 Work practices。[证据](../../../sources/notes/niosh2009approaches.md#e10)
[^lblfoundryuser-e1]: Molecular Foundry，User Program Overview。[证据](../../../sources/notes/lblfoundryuser.md#e1)
[^lblfoundryuser-e2]: Molecular Foundry，User Program Overview。[证据](../../../sources/notes/lblfoundryuser.md#e2)
[^lblfoundryuser-e3]: Molecular Foundry，User Program Overview。[证据](../../../sources/notes/lblfoundryuser.md#e3)
[^lblfoundryuser-e4]: Molecular Foundry，User Program Overview：Apply for Access。[证据](../../../sources/notes/lblfoundryuser.md#e4)
[^lblfoundryuser-e5]: Molecular Foundry，User Program Overview：Prepare to Start Work。[证据](../../../sources/notes/lblfoundryuser.md#e5)
[^lblfoundryuser-e6]: Molecular Foundry，User Program Overview：Project End and Reporting。[证据](../../../sources/notes/lblfoundryuser.md#e6)
[^lejaeghere2016reproducibility-e1]: Lejaeghere 等人 2016，Research Article Summary：Rationale。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e1)
[^lejaeghere2016reproducibility-e2]: Lejaeghere 等人 2016，Research Article Summary：Rationale。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e2)
[^lejaeghere2016reproducibility-e3]: Lejaeghere 等人 2016，摘要。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e3)
[^lejaeghere2016reproducibility-e4]: Lejaeghere 等人 2016，摘要。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e4)
[^lejaeghere2016reproducibility-e5]: Lejaeghere 等人 2016，正文。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e5)
[^lejaeghere2016reproducibility-e6]: Lejaeghere 等人 2016，正文。[证据](../../../sources/notes/lejaeghere2016reproducibility.md#e6)
[^draxl2018nomad-e1]: Draxl & Scheffler 2018，引言。[证据](../../../sources/notes/draxl2018nomad.md#e1)
[^draxl2018nomad-e2]: Draxl & Scheffler 2018，引言。[证据](../../../sources/notes/draxl2018nomad.md#e2)
[^draxl2018nomad-e3]: Draxl & Scheffler 2018，引言。[证据](../../../sources/notes/draxl2018nomad.md#e3)
[^draxl2018nomad-e4]: Draxl & Scheffler 2018，The NOMAD Repository。[证据](../../../sources/notes/draxl2018nomad.md#e4)
[^draxl2018nomad-e5]: Draxl & Scheffler 2018，The NOMAD Repository。[证据](../../../sources/notes/draxl2018nomad.md#e5)
[^draxl2018nomad-e6]: Draxl & Scheffler 2018，The NOMAD Repository。[证据](../../../sources/notes/draxl2018nomad.md#e6)
[^draxl2018nomad-e7]: Draxl & Scheffler 2018，Summary and outlook。[证据](../../../sources/notes/draxl2018nomad.md#e7)
[^draxl2018nomad-e8]: Draxl & Scheffler 2018，Summary and outlook。[证据](../../../sources/notes/draxl2018nomad.md#e8)
[^arxivtaxonomy-e7]: arXiv Category Taxonomy，cond-mat.mtrl-sci。[证据](../../../sources/notes/arxivtaxonomy.md#e7)
[^arxivtaxonomy-e8]: arXiv Category Taxonomy，cond-mat.mes-hall。[证据](../../../sources/notes/arxivtaxonomy.md#e8)
[^naturereportingstandards-e1]: Nature Portfolio，Reporting standards and availability of data, materials, code and protocols，页首。[证据](../../../sources/notes/naturereportingstandards.md#e1)
[^naturereportingstandards-e2]: Nature Portfolio，Reporting standards，Reporting requirements for physical sciences research。[证据](../../../sources/notes/naturereportingstandards.md#e2)
[^naturereportingstandards-e3]: Nature Portfolio，Reporting standards，页首。[证据](../../../sources/notes/naturereportingstandards.md#e3)
[^jacobsson2022open-e1]: Jacobsson 等人 2022，Main。[证据](../../../sources/notes/jacobsson2022open.md#e1)
[^jacobsson2022open-e2]: Jacobsson 等人 2022，Main。[证据](../../../sources/notes/jacobsson2022open.md#e2)
[^jacobsson2022open-e3]: Jacobsson 等人 2022，Details of the database。[证据](../../../sources/notes/jacobsson2022open.md#e3)
[^jacobsson2022open-e4]: Jacobsson 等人 2022，Example uses of the Perovskite Database。[证据](../../../sources/notes/jacobsson2022open.md#e4)
[^jacobsson2022open-e5]: Jacobsson 等人 2022，Example uses of the Perovskite Database。[证据](../../../sources/notes/jacobsson2022open.md#e5)
[^jacobsson2022open-e6]: Jacobsson 等人 2022，Example uses of the Perovskite Database。[证据](../../../sources/notes/jacobsson2022open.md#e6)
[^jacobsson2022open-e7]: Jacobsson 等人 2022，Future expansion of the database。[证据](../../../sources/notes/jacobsson2022open.md#e7)
[^jacobsson2022open-e8]: Jacobsson 等人 2022，Future expansion of the database。[证据](../../../sources/notes/jacobsson2022open.md#e8)
[^jacobsson2022open-e9]: Jacobsson 等人 2022，Future expansion of the database。[证据](../../../sources/notes/jacobsson2022open.md#e9)
[^naturematerials2015checklist-e1]: Nature Materials 2015 社论，导语。[证据](../../../sources/notes/naturematerials2015checklist.md#e1)
[^naturematerials2015checklist-e2]: Nature Materials 2015 社论，第 1 段。[证据](../../../sources/notes/naturematerials2015checklist.md#e2)
[^naturematerials2015checklist-e3]: Nature Materials 2015 社论，第 2 段。[证据](../../../sources/notes/naturematerials2015checklist.md#e3)
[^naturematerials2015checklist-e4]: Nature Materials 2015 社论，第 3 段。[证据](../../../sources/notes/naturematerials2015checklist.md#e4)
[^naturematerials2015checklist-e5]: Nature Materials 2015 社论，第 3 段。[证据](../../../sources/notes/naturematerials2015checklist.md#e5)
[^naturematerials2015checklist-e6]: Nature Materials 2015 社论，第 3 段。[证据](../../../sources/notes/naturematerials2015checklist.md#e6)
[^naturematerials2015checklist-e7]: Nature Materials 2015 社论，第 4 段。[证据](../../../sources/notes/naturematerials2015checklist.md#e7)
[^naturesolarcellsreporting-e1]: Nature Portfolio，Solar Cells Reporting Summary，表头说明。[证据](../../../sources/notes/naturesolarcellsreporting.md#e1)
[^naturesolarcellsreporting-e2]: Nature Portfolio，Solar Cells Reporting Summary，第 2 项。[证据](../../../sources/notes/naturesolarcellsreporting.md#e2)
[^naturesolarcellsreporting-e3]: Nature Portfolio，Solar Cells Reporting Summary，第 7 项。[证据](../../../sources/notes/naturesolarcellsreporting.md#e3)
[^naturesolarcellsreporting-e4]: Nature Portfolio，Solar Cells Reporting Summary，第 8 项。[证据](../../../sources/notes/naturesolarcellsreporting.md#e4)
[^naturesolarcellsreporting-e5]: Nature Portfolio，Solar Cells Reporting Summary，第 8 项。[证据](../../../sources/notes/naturesolarcellsreporting.md#e5)
[^naturesolarcellsreporting-e6]: Nature Portfolio，Solar Cells Reporting Summary，表尾说明。[证据](../../../sources/notes/naturesolarcellsreporting.md#e6)
[^wilkinson2016fair-e1]: Wilkinson 等人 2016，摘要。[证据](../../../sources/notes/wilkinson2016fair.md#e1)
[^wilkinson2016fair-e2]: Wilkinson 等人 2016，引言。[证据](../../../sources/notes/wilkinson2016fair.md#e2)
[^wilkinson2016fair-e3]: Wilkinson 等人 2016，Box 2。[证据](../../../sources/notes/wilkinson2016fair.md#e3)
[^wilkinson2016fair-e4]: Wilkinson 等人 2016，Box 2。[证据](../../../sources/notes/wilkinson2016fair.md#e4)
[^wilkinson2016fair-e5]: Wilkinson 等人 2016，The FAIR Guiding Principles in detail。[证据](../../../sources/notes/wilkinson2016fair.md#e5)
[^wilkinson2016fair-e6]: Wilkinson 等人 2016，摘要。[证据](../../../sources/notes/wilkinson2016fair.md#e6)
