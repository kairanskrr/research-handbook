# 田间试验

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲怎样从头到尾做一个田间试验：在试验地的小区上比较品种、肥料、耕作等处理，从定目标、选设计、布置小区，到整季记录、收获和检查数据、用混合模型分析、多环境试验、农场试验，最后写进论文。实验单位、伪重复、区组、裂区、功效分析、元数据标准 MIAPPE、和农民合作的基本做法，[农业领域概况](../README.md#田间试验的设计)已经讲过，本文直接用。研究设计的一般道理见通用篇[研究设计](../../../general/1_before/04_research_design.md)；以人为参与者的对照实验见计算机篇[对照实验](../../../06_methods/controlled_experiment.md)。

**读完本文，你应该能：**
- 写清目标、处理和对照，据此选设计、定小区大小和重复数；
- 在田里正确随机化，整季按日期记录操作和意外；
- 检查数据，用混合模型做基本分析，分清固定效应和随机效应；
- 按目标期刊要求写清设计和分析，避开常见错误。

---

## 1. 这是什么研究，什么时候用

田间试验是**比较试验**。Piepho 和 Edmondson 2018 年的分析教程说，它讨论的田间试验关心的只是同一个试验里各处理之间的差别[^piepho2018tutorial-e1]。它回答"在田里，处理 A 比处理 B 好多少"这类问题 `[本项目分析]`。下表是本项目的归纳 `[本项目分析]`，带脚注的格子有资料支持：

| | 试验站小区试验 | 多环境试验 | 农场试验 |
|---|---|---|---|
| 在哪里做 | 试验站，条件高度受控[^kool2020reproducibility-e13] | 多个地点，可能还跨多个年份[^smith2005analysis-e1] | 农民自己的田，研究者能控制的少得多[^kool2020reproducibility-e13] |
| 主要回答 | 受控条件下的处理效应 | 品种在不同环境下的表现[^smith2005analysis-e1] | 效应在什么条件下出现、对谁有用[^kool2020reproducibility-e12] |
| 主要难点 | 田块不均匀、意外干扰 | 品种与环境的交互作用[^smith2005analysis-e3]；不是每个品种都在每个环境里种[^smith2005analysis-e2] | 农民做法各异、难有重复 |

怎么选 `[本项目分析]`：想弄清机理、比较很多处理，先在试验站做；想推荐品种或技术，要跨地点和年份；想知道农民用了有没有效果，要到农民田里做。三者常常前后接着做。

---

## 2. 怎么做

Kramer、Paparozzi、Stroup 2016 年在《美国园艺学会会刊》上的文章说："种之前先计划"；收集数据前的统计思考，是统计在研究中最重要的用途[^kramer2016statistics-e10]。下面按时间顺序分九步写。

### 第 1 步：写清目标、处理和对照

**怎么做：**
- 用一两句话写出要回答的问题，以及要据此做什么决定 `[本项目分析]`。
- 分开写处理设计和试验设计。美国农学会、美国作物科学学会、美国土壤科学学会（下称"美国三学会"）给自家期刊和图书编的出版手册这样区分：**处理设计**是关心哪些因素、每个因素取哪些水平、因素之间什么关系（例如两个因素的所有组合都做，叫析因结构），以及选哪些区组变量和协变量；**试验设计**是怎样安排实验单位、怎样把处理分配给它们[^asa2024style-e10]。
- 设好对照。例如比较品种的增广设计里，会随机往各区组加入对照品种（check），用来估计误差和小尺度的空间差异[^casler2015fundamentals-e41]。
- 施肥量、播种密度这类定量处理，想好水平之间的间隔，后面要按水平的顺序分析（见第 6 步）`[本项目分析]`。

**为什么：** 处理设计和试验设计决定了后面用什么分析方法 `[本项目分析]`。

**容易错在哪里：** Kool 等人指出，农场试验常拿"农民常规做法"当对照，却默认这种做法到处一样、读者都知道[^kool2020reproducibility-e3]。对照到底怎么做，要写成具体操作 `[本项目分析]`。

### 第 2 步：选设计，定小区大小和重复数

**怎么做：**
- 按田块的变异方向和操作需要选设计，见[领域概况](../README.md#区组和随机化)。写设计要写全：只写"A 为主区、B 为副区的裂区设计"不完整，还要写主区因素 A 用的基本设计，例如随机完全区组[^casler2015fundamentals-e39]。
- 定小区大小。按 Smith 定律，单个小区的方差随小区面积增大而下降，并逐渐趋平[^casler2015fundamentals-e36]：小区本来就小，加大一点效果明显；已经够大，再加大几乎没用[^casler2015fundamentals-e37]。Casler 课题组定小区大小，看种子和土地够不够，以及这块地以往估出的方差与面积的关系[^casler2015fundamentals-e38]。
- 定重复数前做功效分析（概念见[领域概况](../README.md#地点年份和功效分析)）。把不同设计下的功效画成图，挑一个达到目标的，目标常定为 80%[^casler2015fundamentals-e29]。参数要用以往试验估出的**方差分量**[^casler2015fundamentals-e30]，即总变异里分别来自地点、年份、区组、小区等各层的部分，所以先找组里或试验站历年的数据 `[本项目分析]`。相对于重复数，要优先增加地点和年份[^casler2015fundamentals-e27]。

**为什么：** 小区越大，每块的误差越小，但能放的重复和处理就越少；设计错了，常要等下一季才能重来 `[本项目分析]`。

**容易错在哪里：** 在一个小区里多取样、多量几株，不能代替多做小区，见[领域概况](../README.md#先定实验单位再谈重复)。边行、保护行留多宽，收获时去掉多少边，本文资料未涉及，以导师、试验站惯例或该作物的试验规范为准。

### 第 3 步：在田里布置和随机化

**怎么做：**
- 用随机数生成器排定每个区组里处理的顺序，这才叫随机化；凭感觉"排得均匀些"叫穿插，是主观的[^casler2015fundamentals-e32]。
- 排好后看一眼田间图。随机排列偶尔会让某些处理扎堆；如果田里的空间变异恰好和这种排列相关，就可能带来偏倚[^casler2015fundamentals-e33]。空间均衡完全区组设计就是为此提出的，兼顾随机化和穿插[^casler2015fundamentals-e34]。把田间图、随机化用的程序和随机种子、小区编号一起存档；在田里插牌、拍照，核对编号 `[本项目分析]`。

**为什么：** 区组和随机化都像保险，防的是试验中途可能出现的意外[^casler2015fundamentals-e35]。

**容易错在哪里：** 嫌随机结果"不好看"就手工挪。要调整，就整体重新随机，或换用空间均衡设计 `[本项目分析]`。

### 第 4 步：整个生长季的管理和记录

**怎么做：**
- 开季前列一张田间日历：整地、播种、施肥、灌溉、施药、调查、收获各在什么时候 `[本项目分析]`。
- 每件事当天记日期。植物表型元数据标准 MIAPPE 把这些叫"事件"：既包括播种、施杀菌剂这类田间操作，也包括降雨、病原菌侵染这类意外[^papoutsoglou2020enabling-e6]。它的指导原则之一是减少研究者漏记重要信息的机会[^papoutsoglou2020enabling-e4]，可以照它的字段记 `[本项目分析]`。
- 冰雹、倒伏、动物啃食、喷错药这类意外，记清影响了哪些小区、多大面积 `[本项目分析]`。

**为什么：** 这些信息事后很难补 `[本项目分析]`。Kool 等人 2020 年分析了 1986—2015 年发表的 172 篇撒哈拉以南非洲农场试验论文[^kool2020reproducibility-e1]：只有 10% 把品种、播种日期、株行距、单作间作和轮作这四项作物信息都写全，写了播种日期的只有 41%[^kool2020reproducibility-e9]。

**容易错在哪里：** 除草、补苗、灌溉只在部分小区做，又没记下来 `[本项目分析]`。在农民田里还有一种意外：Kool 等人引用的一项研究发现，农民会照搬某些处理的管理办法，有时还和研究者管理的小区"比赛"[^kool2020reproducibility-e11]。

### 第 5 步：收获、测量和检查数据

**怎么做：**
- 每个性状写清怎样测的[^asa2024style-e1]，例如收获面积、含水量折算、取样位置和株数 `[本项目分析]`。分清实验单位和取样单位，记下每个实验单位取了多少样[^asa2024style-e2]。
- 在同一份材料上、不同时间或不同位置测的数据常常相关[^asa2024style-e4]，分析时要专门处理（见第 6 步）。
- 录入后核对：小区编号和田间图对得上吗，有没有超出合理范围的值，缺失是什么原因 `[本项目分析]`；再画图看分布和残差。要做数据变换（如取对数），记住一次变换会同时影响好几条统计假定[^piepho2018tutorial-e6]。

**为什么：** Kramer 等人检查了《美国园艺学会会刊》2014 年全部各期和 2015 年第 1 期，共 86 篇论文[^kramer2016statistics-e12]，略少于一半看起来有统计问题[^kramer2016statistics-e1]。最常见的（30 篇）是在同一观测单位上测了多个指标，却没有恰当地分析[^kramer2016statistics-e2]；还有 11 篇从图上就能看出方差随均值增大，却用了要求两者无关的方法，说明没有检查统计假定[^kramer2016statistics-e3]。

**容易错在哪里：** 发现异常值就悄悄删掉。应保留原始数据，删改的每一条都写明理由 `[本项目分析]`。

### 第 6 步：用混合模型分析

**混合模型**同时含有固定效应和随机效应。**固定效应**是你直接关心、要比较的因素；**随机效应**看成从更大总体里随机抽出来的，你关心的是它带来多少变异 `[本项目分析]`。

**怎么做：**
- **处理当固定效应。** 处理因素通常当固定效应；区组这类干扰因素可以当固定，也可以当随机[^piepho2018tutorial-e2]。区组大而完整时，当固定比较稳妥[^piepho2018tutorial-e3]；不完全区组设计里，区组当随机才能把区组之间的处理信息也用上[^piepho2018tutorial-e4]。
- **模型照着设计写。** 裂区类设计要把主区、副区的误差项都作为随机效应放进模型；每个处理因素用哪个误差项，看它被随机分配到哪一级小区[^piepho2018tutorial-e5]。
- **定量处理别逐对比较。** 几个施氮量之间逐对做多重比较、标字母，不考虑水平的顺序，完全不适合[^piepho2018tutorial-e7]；可以改用回归这类考虑顺序的方法 `[本项目分析]`。
- **重复测量要专门建模。** 同一单位上多次测量的数据在农学研究中很常见，却常被误读、分析不当[^piepho2018tutorial-e8]。
- **报告差值的标准误。** 要说明两个处理差多少，需要置信区间，至少要有差值的标准误，它和均值的标准误不能互换[^kramer2016statistics-e5]；有区组的设计，没法从后者直接推出前者[^kramer2016statistics-e6]。
- **报告方差分量。** 多地点、多年份的区组试验，混合模型能直接估出各个方差分量[^casler2015fundamentals-e31]。写进论文或附表，别人（包括明年的你）就能拿来做功效分析 `[本项目分析]`。

**为什么：** 区组、多地点、多年份这些因素，过去通常当固定效应，直到 20 世纪 90 年代初有了软件，才能正确地当随机效应[^kramer2016statistics-e8]。照搬老论文的分析容易出错 `[本项目分析]`。

**容易错在哪里：** 设计里有区组、地点、年份，分析时没放进模型，Kramer 等人检查的 86 篇里有 7 篇这样[^kramer2016statistics-e4]。软件选错也会出问题，例如用统计软件 SAS 的 PROC GLM 过程分析含随机效应的数据[^kramer2016statistics-e11]。要用不熟悉的方法时，尽早请统计学者做合作者[^kramer2016statistics-e13]。统计基础见通用篇[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)。

### 第 7 步：多环境试验

**怎么做：**
- 育种和品种评价的产量数据，一般来自在多个地点、可能还跨多个年份做的一系列田间试验，叫**多环境试验**[^smith2005analysis-e1]。
- 用线性混合模型分析：不是每个品种都在每个环境里种也能分析；试验内误差可以用更现实的模型（不完全区组、空间相关）；品种或环境效应可以当随机效应[^smith2005analysis-e2]。但不要只看平均表现：Smith 等人指出，传统方差分析看不出品种与环境交互作用的性质，可能妨碍品种选择和推荐[^smith2005analysis-e3]。
- 保存每个小区的原始数据。先逐个试验求品种均值再合并（两阶段分析），只是直接用全部小区数据（一阶段分析）的近似；过去这样做是因为小区数据常没有电子存档，现在不应再是问题[^smith2005analysis-e4][^smith2005analysis-e5]。

**为什么：** 同一品种在不同地点、年份的表现常常不一样，见[领域概况](../README.md#多地点多年份)。

**容易错在哪里：** 把某地表现好归因于"那里雨多"。雨量这类环境变量没有重复，下不了这种结论[^casler2015fundamentals-e42]。

> **不同的看法：品种效应当固定的还是随机的？**
>
> - **当随机**：Smith 等人认为品种效应应当作随机效应，这样挑选最好品种时选错的概率最小[^smith2005analysis-e7]。
> - **当固定**：Piepho 和 Edmondson 的教程写道，处理因素是直接关心的，通常当固定效应[^piepho2018tutorial-e2]。Smith 等人自己也承认，推动大家改用随机的品种效应并不容易，这在统计学家之间仍有争议[^smith2005analysis-e6]。
> - **实际建议** `[本项目分析]`：目的是比较几个指定的处理（如几种施肥方案），当固定效应；目的是从大量品系里选优、预测，可以考虑当随机效应。无论哪种，都在方法里写明并说明理由。

### 第 8 步：和农民一起做农场试验

**怎么做：** 为什么做、怎样让农民参与、母—子试验、怎样写清"农民常规做法"，见[领域概况](../README.md#和农民一起做研究)。这里只补充几点：
- **先谈清各方想要什么。** Lacoste 等人 2022 年在《自然·食品》（Nature Food）上的观点文章，把"农场实验"定义为让农业各方围绕互惠的试验聚到一起、支持农民自己管理决策的创新过程[^lacoste2022onfarm-e1]；它在农民自己的田里、以对他们有意义的尺度做，并明确承认各方的私人利益[^lacoste2022onfarm-e2]。
- **农民不愿多做重复时**，Casler 给了三种办法：多个农场当区组；把一个对照穿插在其他处理之间；或两者结合[^casler2015fundamentals-e43]。对照隔一块放一块要占一半小区，效率低，但对小型农场试验仍很可行[^casler2015fundamentals-e40]。
- **写清选了哪些地点、农户和田块，为什么选**，并说明效应在什么条件下出现、对谁有用[^kool2020reproducibility-e12]。**把结果讲回去。** 《农学杂志》2019 年农场试验专刊的导言作者 Kyveryga 认为，把结果分析好、汇总好，讲给农民和农艺师听，是农场试验的关键之一[^kyveryga2019onfarm-e5]。

**为什么：** 在农民田里，研究者能控制的少得多[^kool2020reproducibility-e13]，试验站的结论不一定能直接搬过去 `[本项目分析]`。

**容易错在哪里：** 只写"按农民常规做法管理""必要时除草"。Kool 等人指出，这类描述没交代具体怎么做，别人无法重现[^kool2020reproducibility-e10]。

> **不同的看法：农场试验要多讲究统计？**
>
> - **保住对照和重复**：Casler 给组织农场试验的研究者三种办法，都围绕区组和对照小区[^casler2015fundamentals-e43]；效率不高的对照小区设计，他认为对小型农场试验仍很可行[^casler2015fundamentals-e40]。
> - **以农民的需要为先**：Lacoste 等人指出，作物生产在空间和时间上的变异远大于试验处理的效应[^lacoste2022onfarm-e3]；统计显著性说明不了结果在当地有没有用[^lacoste2022onfarm-e4]；农民也可能不太看重统计结果和重复[^lacoste2022onfarm-e5]。
> - **实际建议** `[本项目分析]`：要写成论文的试验，保住随机化和真重复；同时把对农民有用的信息（每块田的效应、经济收益）单独整理给他们。

### 第 9 步：写进论文

**怎么做：** 先查目标期刊的作者须知 `[本项目分析]`。以美国三学会的期刊为例，它们的出版手册要求方法部分写清区组、实验单位大小、地点数和年份数、重复数、田间条件、各性状的测法等[^asa2024style-e1]，详见[领域概况](../README.md#统计分析和报告)。该手册还要求每项分析写出统计方法的简要说明和给出完整细节的文献，并说明统计假定满足到什么程度[^asa2024style-e11]。也写上所用软件，但 Kramer 等人提醒，软件只是实现分析的工具，本身不是统计方法[^kramer2016statistics-e7]，写了软件不等于写了方法 `[本项目分析]`。

**为什么：** 美国三学会的手册说，读者要看懂试验怎样设计和实施，才能判断结果是否可信，也才能据此设计以后的研究[^asa2024style-e9]。

**容易错在哪里：** 只写了"用 SAS 分析"，没写模型里有哪些固定效应和随机效应 `[本项目分析]`。写作的一般做法见通用篇[写作](../../../general/3_after/01_writing.md)。

---

## 3. 检查清单

本文资料里没有专门针对田间试验的报告规范，下面依据美国三学会出版手册和上文资料整理 `[本项目分析]`。

**必须做到**
- [ ] 写清处理设计和试验设计，裂区写出主区的基本设计[^asa2024style-e10][^casler2015fundamentals-e39]
- [ ] 用随机数生成器随机化[^casler2015fundamentals-e32]，存好田间图 `[本项目分析]`
- [ ] 写清实验单位和取样单位，以及各自的数量[^asa2024style-e2]
- [ ] 田间操作和意外都按日期记录[^papoutsoglou2020enabling-e6]
- [ ] 分析模型和设计一致：区组、地点、年份、主区误差都在模型里[^kramer2016statistics-e4][^piepho2018tutorial-e5]
- [ ] 检查统计假定，并报告满足到什么程度[^asa2024style-e11]
- [ ] 用来下结论的数据给出标准误或置信区间（美国三学会期刊的要求）[^asa2024style-e3]
- [ ] 对照（包括"农民常规做法"）写成具体操作[^kool2020reproducibility-e10]

**做到更好**
- [ ] 动手前用以往的方差分量做功效分析[^casler2015fundamentals-e29][^casler2015fundamentals-e30]
- [ ] 随机排列扎堆时，考虑空间均衡设计[^casler2015fundamentals-e34]
- [ ] 报告方差分量，方便别人规划试验 `[本项目分析]`
- [ ] 定量处理不用逐对多重比较[^piepho2018tutorial-e7]
- [ ] 多环境试验保存逐个小区的数据[^smith2005analysis-e5]
- [ ] 农场试验公开选地点、农户和田块的标准[^kool2020reproducibility-e12]

**这些情况可以不做，不算缺陷**
- 小型农场试验用对照小区穿插设计：效率虽低，仍是可行的选择[^casler2015fundamentals-e40]。

**审稿时常见、但不成立的批评**
- 不加分析就指责"伪重复"。生态学者 Davies 和 Gray 2015 年认为，指责之前要先证明它在统计上成立[^davies2015pseudoreplication-e4]；可以用嵌套、随机效应等方法，并承认统计推断的局限[^davies2015pseudoreplication-e3]。详见[领域概况](../README.md#伪重复处理和地块混在一起)。
- 质疑正确的现代方法。Kramer 等人指出，统计知识过时的审稿人可能误以为统计有错而拒稿，其实方法是对的[^kramer2016statistics-e9]。回复时给出方法的出处 `[本项目分析]`。

---

## 4. 常见错误

| 错误（例子由本项目编写 `[本项目分析]`） | 为什么是问题 |
|---|---|
| 嫌随机结果不好看，手工调整小区位置 | 主观穿插不是随机化[^casler2015fundamentals-e32] |
| 播种、施药日期没记，写论文时靠回忆 | Kool 等人分析的 172 篇撒哈拉以南非洲农场试验论文，只有 41% 写了播种日期[^kool2020reproducibility-e9] |
| 有区组、多地点，分析时只做单因素方差分析 | 分析没有考虑设计里的变异来源[^kramer2016statistics-e4] |
| 几个施氮量之间逐对比较、标字母 | 忽略了水平的顺序[^piepho2018tutorial-e7] |
| 多环境试验只留各点均值，小区数据丢了 | 只能做近似的两阶段分析[^smith2005analysis-e4] |

---

## 5. 延伸阅读

- **Casler 2015（Agronomy Journal）**：重复、随机化、区组、小区大小和功效分析。设计试验前读。
- **Piepho 和 Edmondson 2018（Journal of Agronomy and Crop Science）**：用田间实例讲析因、裂区、定量处理和重复测量的混合模型分析，附 SAS 和 R 代码。分析数据时对照着做。
- **Smith、Cullis、Thompson 2005（Journal of Agricultural Science）**：多环境试验混合模型分析的综述。做品种试验时读。
- **Kramer、Paparozzi、Stroup 2016（Journal of the American Society for Horticultural Science）**：一份园艺期刊里的统计错误清单，投稿前对照自查。
- **Lacoste 等人 2022（Nature Food）**：怎样把农民放在农场试验的中心。美国三学会出版手册、Kool 等人 2020 等见[领域概况的延伸阅读](../README.md#延伸阅读)。

[^piepho2018tutorial-e1]: Piepho 和 Edmondson 2018，1 Introduction。[证据](../../../../sources/notes/piepho2018tutorial.md#e1)
[^piepho2018tutorial-e2]: Piepho 和 Edmondson 2018，2.2.1 Block effects。[证据](../../../../sources/notes/piepho2018tutorial.md#e2)
[^piepho2018tutorial-e3]: Piepho 和 Edmondson 2018，2.2.1 Block effects。[证据](../../../../sources/notes/piepho2018tutorial.md#e3)
[^piepho2018tutorial-e4]: Piepho 和 Edmondson 2018，2.2.1 Block effects。[证据](../../../../sources/notes/piepho2018tutorial.md#e4)
[^piepho2018tutorial-e5]: Piepho 和 Edmondson 2018，裂区示例。[证据](../../../../sources/notes/piepho2018tutorial.md#e5)
[^piepho2018tutorial-e6]: Piepho 和 Edmondson 2018，10 Discussion。[证据](../../../../sources/notes/piepho2018tutorial.md#e6)
[^piepho2018tutorial-e7]: Piepho 和 Edmondson 2018，10 Discussion。[证据](../../../../sources/notes/piepho2018tutorial.md#e7)
[^piepho2018tutorial-e8]: Piepho 和 Edmondson 2018，10 Discussion。[证据](../../../../sources/notes/piepho2018tutorial.md#e8)
[^kool2020reproducibility-e1]: Kool 等人 2020，Methods。[证据](../../../../sources/notes/kool2020reproducibility.md#e1)
[^kool2020reproducibility-e9]: Kool 等人 2020，Results，Crop information。[证据](../../../../sources/notes/kool2020reproducibility.md#e9)
[^kool2020reproducibility-e10]: Kool 等人 2020，Results。[证据](../../../../sources/notes/kool2020reproducibility.md#e10)
[^kool2020reproducibility-e3]: Kool 等人 2020，Abstract。[证据](../../../../sources/notes/kool2020reproducibility.md#e3)
[^kool2020reproducibility-e11]: Kool 等人 2020，Discussion。[证据](../../../../sources/notes/kool2020reproducibility.md#e11)
[^kool2020reproducibility-e12]: Kool 等人 2020，Abstract。[证据](../../../../sources/notes/kool2020reproducibility.md#e12)
[^kool2020reproducibility-e13]: Kool 等人 2020，Introduction。[证据](../../../../sources/notes/kool2020reproducibility.md#e13)
[^smith2005analysis-e1]: Smith 等人 2005，Introduction。[证据](../../../../sources/notes/smith2005analysis.md#e1)
[^smith2005analysis-e2]: Smith 等人 2005，Introduction。[证据](../../../../sources/notes/smith2005analysis.md#e2)
[^smith2005analysis-e3]: Smith 等人 2005，Introduction。[证据](../../../../sources/notes/smith2005analysis.md#e3)
[^smith2005analysis-e4]: Smith 等人 2005，Two-stage analyses。[证据](../../../../sources/notes/smith2005analysis.md#e4)
[^smith2005analysis-e5]: Smith 等人 2005，Two-stage analyses。[证据](../../../../sources/notes/smith2005analysis.md#e5)
[^smith2005analysis-e6]: Smith 等人 2005，Conclusions。[证据](../../../../sources/notes/smith2005analysis.md#e6)
[^smith2005analysis-e7]: Smith 等人 2005，Conclusions。[证据](../../../../sources/notes/smith2005analysis.md#e7)
[^kramer2016statistics-e1]: Kramer 等人 2016，Abstract。[证据](../../../../sources/notes/kramer2016statistics.md#e1)
[^kramer2016statistics-e12]: Kramer 等人 2016，Methods。[证据](../../../../sources/notes/kramer2016statistics.md#e12)
[^kramer2016statistics-e13]: Kramer 等人 2016，Abstract。[证据](../../../../sources/notes/kramer2016statistics.md#e13)
[^kramer2016statistics-e2]: Kramer 等人 2016，Statistical problems。[证据](../../../../sources/notes/kramer2016statistics.md#e2)
[^kramer2016statistics-e3]: Kramer 等人 2016，Statistical problems。[证据](../../../../sources/notes/kramer2016statistics.md#e3)
[^kramer2016statistics-e4]: Kramer 等人 2016，Statistical problems。[证据](../../../../sources/notes/kramer2016statistics.md#e4)
[^kramer2016statistics-e5]: Kramer 等人 2016，Statistical problems。[证据](../../../../sources/notes/kramer2016statistics.md#e5)
[^kramer2016statistics-e6]: Kramer 等人 2016，Statistical problems。[证据](../../../../sources/notes/kramer2016statistics.md#e6)
[^kramer2016statistics-e7]: Kramer 等人 2016，Software packages。[证据](../../../../sources/notes/kramer2016statistics.md#e7)
[^kramer2016statistics-e8]: Kramer 等人 2016，Underlying reasons。[证据](../../../../sources/notes/kramer2016statistics.md#e8)
[^kramer2016statistics-e9]: Kramer 等人 2016，Underlying reasons。[证据](../../../../sources/notes/kramer2016statistics.md#e9)
[^kramer2016statistics-e10]: Kramer 等人 2016，Recommendations。[证据](../../../../sources/notes/kramer2016statistics.md#e10)
[^kramer2016statistics-e11]: Kramer 等人 2016，Software packages。[证据](../../../../sources/notes/kramer2016statistics.md#e11)
[^asa2024style-e10]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e10)
[^asa2024style-e1]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e1)
[^asa2024style-e2]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e2)
[^asa2024style-e11]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e11)
[^asa2024style-e3]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e3)
[^asa2024style-e4]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e4)
[^asa2024style-e9]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../../sources/notes/asa2024style.md#e9)
[^casler2015fundamentals-e29]: Casler 2015，功效分析示例。[证据](../../../../sources/notes/casler2015fundamentals.md#e29)
[^casler2015fundamentals-e30]: Casler 2015，资源分配。[证据](../../../../sources/notes/casler2015fundamentals.md#e30)
[^casler2015fundamentals-e31]: Casler 2015，Table 2。[证据](../../../../sources/notes/casler2015fundamentals.md#e31)
[^casler2015fundamentals-e32]: Casler 2015，Randomization。[证据](../../../../sources/notes/casler2015fundamentals.md#e32)
[^casler2015fundamentals-e33]: Casler 2015，Randomization。[证据](../../../../sources/notes/casler2015fundamentals.md#e33)
[^casler2015fundamentals-e34]: Casler 2015，Randomization。[证据](../../../../sources/notes/casler2015fundamentals.md#e34)
[^casler2015fundamentals-e35]: Casler 2015，Blocking。[证据](../../../../sources/notes/casler2015fundamentals.md#e35)
[^casler2015fundamentals-e36]: Casler 2015，Size of experimental units。[证据](../../../../sources/notes/casler2015fundamentals.md#e36)
[^casler2015fundamentals-e37]: Casler 2015，Size of experimental units。[证据](../../../../sources/notes/casler2015fundamentals.md#e37)
[^casler2015fundamentals-e38]: Casler 2015，Size of experimental units。[证据](../../../../sources/notes/casler2015fundamentals.md#e38)
[^casler2015fundamentals-e39]: Casler 2015，Blocking，裂区设计。[证据](../../../../sources/notes/casler2015fundamentals.md#e39)
[^casler2015fundamentals-e40]: Casler 2015，Replication，对照小区设计。[证据](../../../../sources/notes/casler2015fundamentals.md#e40)
[^casler2015fundamentals-e41]: Casler 2015，Replication，增广设计。[证据](../../../../sources/notes/casler2015fundamentals.md#e41)
[^casler2015fundamentals-e27]: Casler 2015，资源分配。[证据](../../../../sources/notes/casler2015fundamentals.md#e27)
[^casler2015fundamentals-e42]: Casler 2015，Replication。[证据](../../../../sources/notes/casler2015fundamentals.md#e42)
[^casler2015fundamentals-e43]: Casler 2015，Replication，农场试验。[证据](../../../../sources/notes/casler2015fundamentals.md#e43)
[^papoutsoglou2020enabling-e6]: Papoutsoglou 等人 2020，MIAPPE 1.1 的"事件"部分。[证据](../../../../sources/notes/papoutsoglou2020enabling.md#e6)
[^papoutsoglou2020enabling-e4]: Papoutsoglou 等人 2020，MIAPPE 的指导原则。[证据](../../../../sources/notes/papoutsoglou2020enabling.md#e4)
[^lacoste2022onfarm-e1]: Lacoste 等人 2022，OFE embeds research in farm management。[证据](../../../../sources/notes/lacoste2022onfarm.md#e1)
[^lacoste2022onfarm-e2]: Lacoste 等人 2022，OFE embeds research in farm management。[证据](../../../../sources/notes/lacoste2022onfarm.md#e2)
[^lacoste2022onfarm-e3]: Lacoste 等人 2022，Progressing experimentation。[证据](../../../../sources/notes/lacoste2022onfarm.md#e3)
[^lacoste2022onfarm-e4]: Lacoste 等人 2022，Progressing experimentation。[证据](../../../../sources/notes/lacoste2022onfarm.md#e4)
[^lacoste2022onfarm-e5]: Lacoste 等人 2022，Figure 2 图注。[证据](../../../../sources/notes/lacoste2022onfarm.md#e5)
[^kyveryga2019onfarm-e5]: Kyveryga 2019，导言。[证据](../../../../sources/notes/kyveryga2019onfarm.md#e5)
[^davies2015pseudoreplication-e4]: Davies 和 Gray 2015，Abstract。[证据](../../../../sources/notes/davies2015pseudoreplication.md#e4)
[^davies2015pseudoreplication-e3]: Davies 和 Gray 2015，Abstract。[证据](../../../../sources/notes/davies2015pseudoreplication.md#e3)
