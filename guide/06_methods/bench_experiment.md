# 实验台实验（湿实验）

本文讲细胞生物学、分子生物学里常见的一类研究：在实验台上用培养的细胞、提取的分子和试剂做处理，和对照比较，检验一个假设。重点是一个实验从设计到写进论文，每一步具体怎么做。

实验单位、两种重复、对照、随机、盲法、试剂验证、记录本的规矩，以及动物实验的 3R 原则和 ARRIVE 报告规范，见[生物科学学科概况](../07_fields/biological-sciences/README.md)。临床前研究（进入人体试验之前的细胞和动物研究）的报告要求、《英国药理学杂志》的规定、抗体验证，见[基础医学学科概况](../07_fields/basic-medicine/README.md)。统计的一般做法见主线章节[报告差多少、有多确定，而不只是 p 值](../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。本文只讲实验台上具体怎么做。

**适用范围** `[本项目分析]`：本篇原为生物科学学科篇写，例子是细胞生物学、分子生物学的细胞和分子实验；依据主要来自生物医学期刊的方法学文章，以及动物研究的报告指南（ARRIVE 2.0 解释文件、Landis 等人 2012）。除[生物科学](../07_fields/biological-sciences/README.md)外，[基础医学](../07_fields/basic-medicine/README.md)、[生物技术](../07_fields/biotechnology/README.md)的学科概况也把它列为常用方法。其他学科（例如化学、材料、心理学）也做实验室里的对照实验，但对照、重复和报告的规矩不尽相同；用之前先看本学科的规范和目标期刊的作者须知。

**常服务的套路**：套路页暂未列出。各种套路见[研究套路](../05_research-strategies/README.md)。

**读完本文，你应该能：**

- 动手前写清假设，分清这是探索性实验还是验证性实验；
- 画出实验的层级，找到实验单位，算对 n；
- 在实验台上安排对照、随机和盲法，事先定好 n、排除标准和分析方法；
- 诚实地处理离群值和失败的实验，画出不误导人的图，不越过图像处理的红线；
- 把方法写到别人能照着重复。

---

## 1. 这是什么研究，什么时候用

实验台实验回答"改变这个因素，结果会不会变"这类问题 `[本项目分析]`。例如敲低某个基因后，细胞增殖会不会变慢。基本做法是一次只改变一个因素，其他因素保持不变[^vaux2012replicates-e6]。

它和研究方法里的[对照实验](controlled_experiment.md)逻辑相同：操纵一个变量，随机分组，控制其他条件。不同在于，人类参与者天然是独立的个体；在实验台上，"独立的个体"（实验单位）要靠你自己设计出来，这里最容易出错 `[本项目分析]`。和动物实验相比，细胞实验不涉及动物福利审批，但伪重复、试剂出错、批次效应、图像处理越界这些风险是一样的 `[本项目分析]`。

**先分清探索性实验和验证性实验。** 探索性实验测多个指标、在数据里找规律、提出假设；预实验也属于这一类[^perciedusert2020reporting-e12]。验证性实验检验一个具体的假设：事先估算样本量，事先定好主要结局指标，用推断统计分析[^perciedusert2020reporting-e13]。探索性实验的结果只能当作"提出的假设"，要靠后续的验证性实验来确认，详见[基础医学学科概况](../07_fields/basic-medicine/README.md#分清探索性实验和验证性实验)[^landis2012call-e12][^landis2012call-e17]。新手常把探索时看到的现象直接写成结论 `[本项目分析]`。

---

## 2. 怎么做

**依据从哪里来。** 本文资料里没有专门针对细胞实验的报告规范。下面不少依据借用自动物研究：ARRIVE 2.0 的解释文件（ARRIVE 是动物研究的报告指南），以及 Landis 等人 2012 年为动物研究提出的报告建议。把其中的实验设计原则用到细胞实验上，是本项目的借用，不是这些文件本身的说法；涉及动物福利的部分本文没有采用 `[本项目分析]`。

### 第 1 步：写出假设，定下主要结局指标

**怎么做**：用一句话写出要检验的假设：比较哪几组、测哪个指标、多大的差异才算有生物学意义 `[本项目分析]`。验证性实验要有一个事先定好的主要结局指标[^perciedusert2020reporting-e13]。

**为什么**：没有事先定好主要结局，或收完数据再换，容易只挑显著的结果来报告。事先登记研究方案，可以免于"选择性报告结局"（也叫 p 值操纵，p-hacking）的嫌疑[^perciedusert2020reporting-e25]。

**容易错在哪**：统计显著不等于生物学上重要[^cumming2007error-e7]。只看到部分效应，就不要说某个基因"必需"（见[生物科学学科概况](../07_fields/biological-sciences/README.md#对照随机分组和盲法)）。

### 第 2 步：画出层级，找到实验单位

**怎么做**：把实验画成一棵树：细胞系 → 实验日 → 培养板 → 孔 → 细胞 → 每个细胞上的测量 `[本项目分析]`。然后分清三种"单位"[^lazic2018what-e3]：

- **实验单位**：被随机、独立地分到不同处理组的那个对象。**n 等于实验单位的个数。**
- **观察单位**：你实际测量的对象，比如显微镜下的一个个细胞。观察单位再多，n 也不会增加。
- **生物单位**：你想对它下结论的对象。假设是"乳腺癌细胞系比肺癌细胞系增殖快"，就要用多株乳腺癌和多株肺癌细胞系，因为假设讲的是组织来源[^lazic2018what-e7]。

一个对象要算真正的重复，要同时满足三条：被独立地分组；处理被独立地施加到它身上；它和别的实验单位互不影响[^lazic2018what-e4]。好记的一句话："在哪一层随机分组，样本量就按哪一层算"[^lazic2018what-e10]。

**细胞实验怎么算**：同一孔里的细胞彼此影响，不能当实验单位；孔或培养皿才是[^lazic2018what-e5]。体外实验通常还要在不同的日子把整个实验重复几次，同一天内的孔只算子样本[^lazic2018what-e6]。例如：每次做三个平行培养，独立重复四次，n = 4，不是 3，也不是 12[^cumming2007error-e3]。从同一份细胞储备液分出的平行培养，抽样的总体只是这一份储备液[^cumming2007error-e8]。

**为什么**：重复做在了错误的层次上，实验做完以后再巧妙的统计方法也补救不了[^lazic2018what-e1]。这个错误不少见：Lazic 等人检索了 2011 年 1 月到 2016 年 9 月发表的一批动物研究论文，只有 22% 做了真正的重复，46% 有伪重复[^lazic2018what-e9]。这是动物研究的数据，细胞实验的比例本文资料未涉及 `[本项目分析]`。

> **不同的看法：要不要用"生物学重复 / 技术重复"这对说法？** 生物科学学科概况沿用了这对说法（[见此](../07_fields/biological-sciences/README.md#先弄清实验单位再算-n)）。Lazic 等人认为它定义不一致，也说不清该重复什么，主张改用上面三种单位来想[^lazic2018what-e2]。他们也承认，把哪一层当作 n 是一个科学判断，看法可能不同，但标准越严，结果越可信[^lazic2018what-e6]。实际建议 `[本项目分析]`：组里可以继续用"生物学重复"这个词，但设计时用上面三条标准逐一检查；拿不准就选更严的那一层，并在论文里写清 n 指的是什么。

### 第 3 步：设计对照

**怎么做**：阴性对照、阳性对照的作用见[生物科学学科概况](../07_fields/biological-sciences/README.md#对照随机分组和盲法)。落到实验台上，例如：敲低实验配一个无关序列的对照，药物实验配一个溶剂对照，再配一个已知有效的处理作阳性对照 `[本项目分析]`。

**容易错在哪**：对照组和处理组不在同一天做、不用同一批试剂。样品分批处理时不注意安排，就可能把批次效应误当成处理效应[^landis2012call-e7]。

### 第 4 步：动手前定好 n、排除标准和分析方法

**怎么做**：在记录本里写下这几件事，日期要早于第一个数据 `[本项目分析]`：

- **n 是多少、怎么定的。** 任何实验都要说明样本量怎么定[^perciedusert2020reporting-e14]。样本量计算要用到效应量、变异程度、显著性水平和统计功效；设计复杂或不常见时，先咨询统计人员[^perciedusert2020reporting-e15]。
- **什么时候停。** 样本量和停止收集数据的规则要事先定好[^landis2012call-e9]。
- **排除标准。** 在实验开始前定好[^perciedusert2020reporting-e17]，至少写进记录本，并在论文里说明是事先定的[^perciedusert2020reporting-e18]。典型的排除理由是没达到质控标准，比如样品量不够、污染超标[^perciedusert2020reporting-e17]。
- **统计方法。** 在收集数据之前定好[^perciedusert2020reporting-e26]。

**为什么**：统计功效低时，真实的效应更容易漏掉；即使测到了，效应量也常被高估[^perciedusert2020reporting-e14]。"显著了就停，不显著就再加几次"正是事先定停止规则要防的做法[^landis2012call-e9]，它会增加假阳性的机会 `[本项目分析]`。

**容易错在哪**：有的期刊对 n 和显著性阈值有硬性规定。例如《英国药理学杂志》（British Journal of Pharmacology）2018 年的指南规定，做统计分析的数据每组 n 至少为 5[^curtis2018experimental-e14]，显著性阈值写在方法部分、结果部分不能再换[^curtis2018experimental-e5]。这只是这一家期刊的规定，其他期刊以各自的作者须知为准；该刊的其他规定见[基础医学学科概况](../07_fields/basic-medicine/README.md#一家药理学期刊的具体规定英国药理学杂志) `[本项目分析]`。

### 第 5 步：在实验台上做随机和盲法

**怎么做**：
- **随机分配**：用随机数决定哪个孔、哪块板接受哪种处理，不要固定"左边对照、右边处理" `[本项目分析]`。
- **用区组控制批次**：把实验拆成几个小的子实验（叫"区组"），比如按实验日分，在每个区组内随机分配处理[^perciedusert2020reporting-e21]。试剂批次、操作者这类可能影响结果的因素，分析时也作为区组因素处理[^perciedusert2020reporting-e31]。
- **随机化操作顺序**：取样和测量的顺序也随机，或者用区组、平衡安排[^perciedusert2020reporting-e22]。
- **设盲**：至少在评估结果时设盲，尤其是带主观判断的评估，比如看切片；这可能需要请别人帮忙[^perciedusert2020reporting-e23]。做分组的人也不该知道下一个对象会分到哪组，这叫分组隐藏；原文以动物为例，用到细胞实验是本项目的借用[^landis2012call-e6] `[本项目分析]`。

**为什么**：ARRIVE 解释文件引用的系统综述数据显示，缺少随机和盲法这类减少偏倚的措施，可能让效应量虚高多达 30%～45%[^perciedusert2020reporting-e24]。

### 第 6 步：先做预实验

**怎么做**：正式实验前，先用少量样品把方法跑通，比如抗体浓度、细胞密度、处理时间、检测的线性范围 `[本项目分析]`。预实验的目的是为后续实验的设计和可行性提供信息[^perciedusert2020reporting-e12]；只为改进操作的预实验，样本一般很少，不适合做功效计算[^perciedusert2020reporting-e16]。

**容易错在哪**：把预实验的数据并进正式实验 `[本项目分析]`。《英国药理学杂志》的规定是：预实验数据可以写进论文，但放在方法部分单列的"预实验"小节，不给 P 值[^curtis2018experimental-e11]。另一个错误是只靠预实验估算正式实验的样本量：单靠预实验，不太可能为功效计算提供足够的变异数据[^perciedusert2020reporting-e16]。

### 第 7 步：确认试剂和细胞系

为什么要验证，见[生物科学学科概况](../07_fields/biological-sciences/README.md#试剂抗体和细胞系要验证)。具体到实验台上：

- **细胞系**：新到的细胞系先做身份鉴定 `[本项目分析]`。短串联重复序列分析是公认的鉴定标准[^freedman2015economics-e3]。花费不大：Freedman 等人估算，对一项美国国立卫生研究院（NIH）资助、平均 45 万美元的四年期课题，从可靠来源买细胞系并每年鉴定一次，约 1000 美元，占经费的 0.2%[^freedman2015economics-e10]。
- **抗体**：在自己的用途和样品中至少做一种验证[^uhlen2016proposal-e6]；验证的思路见[基础医学学科概况](../07_fields/basic-medicine/README.md#抗体要按用途验证试剂要写到能被找到)。
- **记下来**：每种试剂的来源、货号、批号写进记录本 `[本项目分析]`；论文里抗体至少写货号和批号[^uhlen2016proposal-e6]。

### 第 8 步：边做边记

记录本的通行规矩见[生物科学学科概况](../07_fields/biological-sciences/README.md#实验记录本是第一手记录)：按时间顺序记、每条写日期和主题[^schnell2015ten-e10]，做完立即写[^schnell2015ten-e3]。实验台上要额外注意：

- **失败的实验也记。** 错误本身是科研过程的一部分，不要擦掉或销毁记录[^schnell2015ten-e11]。写下失败的原因（污染、仪器故障、试剂过期），这是之后判断能否排除这次数据的依据 `[本项目分析]`。
- **原始图像原样保存，并记下仪器设置**，比如曝光时间、增益[^rossner2004what-e8]。

### 第 9 步：诚实处理离群值和失败的实验

**怎么做**：
- **按事先定的标准排除，不按结果好坏排除。** 明显的录入错误、超出合理范围的读数可以剔除，但要写明理由，读者才能区分负责任的数据清理和数据操纵[^perciedusert2020reporting-e19]。用了统计软件自带的离群值检验，要明确写出来[^perciedusert2020reporting-e20]。
- **分清层次**：同一样品重复测量里的离群值，有令人信服的解释时可以去掉，但重做更稳妥；独立样本的结果，只有在特殊情况下才能去掉[^vaux2012replicates-e8]。
- **报告全部重复**：整轮实验重复过几次，就报告几次的结果，不要只挑"代表性实验"[^perciedusert2020reporting-e27]。写明实验一共做了几次，可以抵消"只发表最好那次"的倾向[^landis2012call-e15]。

**容易错在哪**：看到某次结果不支持假设，才回头找它"失败"的理由 `[本项目分析]`。所以失败原因要在看结果之前记下来。

### 第 10 步：分析和画图

**怎么做**：
- **每个实验单位先汇总成一个值**（比如同一天各孔的平均值），再做统计。这是避免伪重复最简单的办法[^lazic2018what-e8]。
- **图注写清 n 和误差线是什么。** 写明 n，也就是独立进行的实验次数[^cumming2007error-e2]；写明误差线是标准差、标准误还是置信区间[^cumming2007error-e1]。只展示一次"代表性实验"时 n = 1，不应画误差线、给 P 值[^cumming2007error-e4]。
- **n 很小时把每个点画出来。** n = 3 这样的小样本，与其画误差线，不如直接画出每个数据点[^cumming2007error-e5]。很多不同的数据分布会画出一模一样的柱状图[^weissgerber2015beyond-e1]；配对数据画成柱状图，看不出每对的变化方向是否一致[^weissgerber2015beyond-e2]。这类图很常见：Weissgerber 等人回顾了 2014 年 1–3 月生理学排名前 25% 期刊的 703 篇原创研究论文，85.6% 至少有一张柱状图，只有 13.4% 用过单变量散点图[^weissgerber2015beyond-e4]。
- **不要用标准误"放大"差异。** 画标准误而不画标准差，会在视觉上放大组间差异[^weissgerber2015beyond-e5]。

**容易错在哪**：P 大于 0.05 就下结论说"没有效应"，是常见而严重的错误[^cumming2007error-e6]。可能效应真的存在，只是 n 不够 `[本项目分析]`。

### 第 11 步：处理图像，守住红线

印迹、凝胶和显微照片是湿实验常见的证据，也容易越界 `[本项目分析]`。下面的规则来自《细胞生物学杂志》（Journal of Cell Biology）2004 年的一篇编辑文章，代表该刊当时的规定和编辑的建议；你投的期刊以其作者须知为准 `[本项目分析]`。

- **不能做**：增强、遮盖、移动、删除或添加图像中的任何特定部分[^rossner2004what-e2]。删掉一条你认为无关的背景带，也是歪曲数据[^rossner2004what-e4]。不要用"仿制图章"一类工具清理背景[^rossner2004what-e5]。不要把不同胶的片段拼在一起比较蛋白或核酸水平，应把所有样品在同一块胶上重跑[^rossner2004what-e6]。
- **可以做，但要整张图一起做**：亮度、对比度、色彩平衡的调整，作用于整张图、不消除原图信息，就可以；非线性调整（如改伽马值）要在图注里说明[^rossner2004what-e3]。实验组和对照组的照片不要调得不一样[^rossner2004what-e7]。
- **可以做，但要标出来**：去掉整条泳道再拼接，要在拼接处留一条细线[^rossner2004what-e6]；不同视野、不同曝光的图拼在一起，要用分隔线并在图注说明[^rossner2004what-e2]。
- **在实验时解决，不在电脑上解决**：多拍几个曝光，而不是事后过度调对比度[^rossner2004what-e9]。不要靠调仪器设置有选择地采集数据，也不要把极不寻常的结果当作"代表性"结果[^rossner2004what-e10]。

拿不准时问自己：调整后的图像还准确代表原始数据吗[^rossner2004what-e11]？不当的修改可能被认定为科研不端[^rossner2004what-e1]。

### 第 12 步：把方法写到别人能重复

**怎么做**：写清每组（包括对照）做了什么、怎么做的、用了什么，写到别人能重复；说明用了哪些质控措施；有研究资源标识符（Research Resource Identifier，RRID，给试剂和工具的唯一编号）的就引用它[^perciedusert2020reporting-e28]。至少交代 n 怎么定、是否随机、是否设盲、数据怎么处理；这是 Landis 等人那次研讨会对动物研究提出的最低报告要求[^landis2012call-e1]，细胞实验借来参照 `[本项目分析]`。

**为什么**：癌症生物学可复现性项目计划复现的 193 个实验，没有一个能不问原作者就设计出复现方案[^errington2021challenges-e7]。有一次询问实验细节，得到的回答只是"用的是标准方法"[^errington2021challenges-e8]。

---

## 3. 检查清单

本文资料里没有专门针对细胞实验的报告清单。下面借用 ARRIVE 解释文件，并结合 Cumming 等人的误差线规则和《细胞生物学杂志》的图像规则整理，分档为本项目分析 `[本项目分析]`。

**必须做到**

- [ ] 写清实验单位，n 按实验单位算，不按孔、细胞或测量次数算[^lazic2018what-e3][^cumming2007error-e3]
- [ ] 说明样本量怎么定的[^perciedusert2020reporting-e14]
- [ ] 排除标准事先定好、写进记录本，论文里报告[^perciedusert2020reporting-e18]
- [ ] 报告所有重复的结果，不只挑代表性实验[^perciedusert2020reporting-e27]
- [ ] 图注写明 n 和误差线类型[^cumming2007error-e1][^cumming2007error-e2]
- [ ] 图像只做整图调整，拼接处标出，原始图像原样保存[^rossner2004what-e2][^rossner2004what-e8]
- [ ] 方法写到别人能重复；抗体写清货号、批号[^perciedusert2020reporting-e28][^uhlen2016proposal-e6]

**做到更好**

- [ ] 用区组和随机安排处理位置和操作顺序[^perciedusert2020reporting-e21][^perciedusert2020reporting-e22]
- [ ] 评估结果时设盲[^perciedusert2020reporting-e23]
- [ ] n 小时把每个数据点画出来[^cumming2007error-e5][^weissgerber2015beyond-e3]
- [ ] 事先登记研究方案[^perciedusert2020reporting-e25]

**这些情况可以不做，不算缺陷**

- 只为跑通操作的预实验：可以不做功效计算[^perciedusert2020reporting-e16]，可能不需要对照组[^perciedusert2020reporting-e29]。
- 探索性实验：不必确定单一的主要结局指标[^perciedusert2020reporting-e30]，但结论只能当作待验证的假设[^landis2012call-e12]。

---

## 4. 常见错误

和生物科学学科概况[常见错误](../07_fields/biological-sciences/README.md#常见错误)重复的（伪重复、不鉴定细胞系、方法写得太简略）不再列。

| 错误 | 为什么是问题 |
|---|---|
| 同一天、同一份细胞铺了很多孔，按孔数算 n | 抽样的总体只是这一份储备液[^cumming2007error-e8]；同一天内的孔只算子样本[^lazic2018what-e6] |
| 展示一次"代表性实验"，还画误差线、标 P 值 | 这时 n = 1[^cumming2007error-e4] |
| 结果不显著就再加几次实验，显著了就停 | 停止规则要事先定好[^landis2012call-e9]；否则假阳性机会变大 `[本项目分析]` |
| 看了结果再决定哪次实验"失败了"、要排除 | 排除标准要在收数据前定好[^perciedusert2020reporting-e17] |
| 对照组和处理组分不同的天、用不同批试剂做 | 批次效应会被误当成处理效应[^landis2012call-e7] |
| 用柱状图加标准误展示 n = 3 的数据 | 不同的数据分布能画出同样的柱状图，标准误还会放大差异[^weissgerber2015beyond-e1][^weissgerber2015beyond-e5] |
| 擦掉印迹上"多余"的带，或单独调某一张图的对比度 | 歪曲数据，可能被认定为科研不端[^rossner2004what-e4][^rossner2004what-e7][^rossner2004what-e1] |

---

## 5. 延伸阅读

- **Lazic 等人 2018，What exactly is 'N' in cell culture and animal experiments?（PLOS Biology）**：用实验单位判断 n，有细胞培养的例子。设计第一个实验前读。
- **Cumming、Fidler 和 Vaux 2007，Error bars in experimental biology（Journal of Cell Biology）**：误差线规则，讲清 n 和代表性实验。画第一张图前读。
- **Rossner 和 Yamada 2004，What's in a picture?（Journal of Cell Biology）**：用示例图讲哪些图像处理可以、哪些不行。处理第一张印迹图前读。
- **Weissgerber 等人 2015，Beyond bar and line graphs（PLOS Biology）**：为什么小样本不该只画柱状图。
- Vaux 等人 2012 和 ARRIVE 2.0 解释文件见[生物科学学科概况](../07_fields/biological-sciences/README.md#延伸阅读)；Landis 等人 2012 和 Curtis 等人 2018 见[基础医学学科概况](../07_fields/basic-medicine/README.md#延伸阅读)。

[^vaux2012replicates-e6]: Vaux 等人 2012，Sidebar A。[证据](../../sources/notes/vaux2012replicates.md#e6)
[^vaux2012replicates-e8]: Vaux 等人 2012，Sidebar A。[证据](../../sources/notes/vaux2012replicates.md#e8)
[^lazic2018what-e1]: Lazic 等人 2018，Introduction。[证据](../../sources/notes/lazic2018what.md#e1)
[^lazic2018what-e2]: Lazic 等人 2018，Introduction。[证据](../../sources/notes/lazic2018what.md#e2)
[^lazic2018what-e3]: Lazic 等人 2018，Box 2。[证据](../../sources/notes/lazic2018what.md#e3)
[^lazic2018what-e4]: Lazic 等人 2018，Requirements for genuine replication。[证据](../../sources/notes/lazic2018what.md#e4)
[^lazic2018what-e5]: Lazic 等人 2018，Cell culture experiments。[证据](../../sources/notes/lazic2018what.md#e5)
[^lazic2018what-e6]: Lazic 等人 2018，Cell culture experiments。[证据](../../sources/notes/lazic2018what.md#e6)
[^lazic2018what-e7]: Lazic 等人 2018，Requirements for genuine replication。[证据](../../sources/notes/lazic2018what.md#e7)
[^lazic2018what-e8]: Lazic 等人 2018，Analysis of hierarchical data。[证据](../../sources/notes/lazic2018what.md#e8)
[^lazic2018what-e9]: Lazic 等人 2018，What is the extent of the problem? 和 Box 1。[证据](../../sources/notes/lazic2018what.md#e9)
[^lazic2018what-e10]: Lazic 等人 2018，Requirements for genuine replication。[证据](../../sources/notes/lazic2018what.md#e10)
[^cumming2007error-e1]: Cumming 等人 2007，Rule 1。[证据](../../sources/notes/cumming2007error.md#e1)
[^cumming2007error-e2]: Cumming 等人 2007，Rule 2。[证据](../../sources/notes/cumming2007error.md#e2)
[^cumming2007error-e3]: Cumming 等人 2007，Replicates or independent samples—what is n?。[证据](../../sources/notes/cumming2007error.md#e3)
[^cumming2007error-e4]: Cumming 等人 2007，Rule 3。[证据](../../sources/notes/cumming2007error.md#e4)
[^cumming2007error-e5]: Cumming 等人 2007，Rule 4。[证据](../../sources/notes/cumming2007error.md#e5)
[^cumming2007error-e6]: Cumming 等人 2007，Statistical significance tests and P values。[证据](../../sources/notes/cumming2007error.md#e6)
[^cumming2007error-e7]: Cumming 等人 2007，Statistical significance tests and P values。[证据](../../sources/notes/cumming2007error.md#e7)
[^cumming2007error-e8]: Cumming 等人 2007，Replicates or independent samples—what is n?。[证据](../../sources/notes/cumming2007error.md#e8)
[^perciedusert2020reporting-e12]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 13。[证据](../../sources/notes/perciedusert2020reporting.md#e12)
[^perciedusert2020reporting-e13]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 13。[证据](../../sources/notes/perciedusert2020reporting.md#e13)
[^perciedusert2020reporting-e14]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 2b。[证据](../../sources/notes/perciedusert2020reporting.md#e14)
[^perciedusert2020reporting-e15]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 2b 和 Box 3。[证据](../../sources/notes/perciedusert2020reporting.md#e15)
[^perciedusert2020reporting-e16]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 2b。[证据](../../sources/notes/perciedusert2020reporting.md#e16)
[^perciedusert2020reporting-e17]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 3a。[证据](../../sources/notes/perciedusert2020reporting.md#e17)
[^perciedusert2020reporting-e18]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 3a。[证据](../../sources/notes/perciedusert2020reporting.md#e18)
[^perciedusert2020reporting-e19]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 3b。[证据](../../sources/notes/perciedusert2020reporting.md#e19)
[^perciedusert2020reporting-e20]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 3b。[证据](../../sources/notes/perciedusert2020reporting.md#e20)
[^perciedusert2020reporting-e21]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 4，Box 4。[证据](../../sources/notes/perciedusert2020reporting.md#e21)
[^perciedusert2020reporting-e22]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 4b。[证据](../../sources/notes/perciedusert2020reporting.md#e22)
[^perciedusert2020reporting-e23]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 5。[证据](../../sources/notes/perciedusert2020reporting.md#e23)
[^perciedusert2020reporting-e24]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 5。[证据](../../sources/notes/perciedusert2020reporting.md#e24)
[^perciedusert2020reporting-e25]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 6b。[证据](../../sources/notes/perciedusert2020reporting.md#e25)
[^perciedusert2020reporting-e26]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 7a。[证据](../../sources/notes/perciedusert2020reporting.md#e26)
[^perciedusert2020reporting-e27]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 10a。[证据](../../sources/notes/perciedusert2020reporting.md#e27)
[^perciedusert2020reporting-e28]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 9a。[证据](../../sources/notes/perciedusert2020reporting.md#e28)
[^perciedusert2020reporting-e29]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1a。[证据](../../sources/notes/perciedusert2020reporting.md#e29)
[^perciedusert2020reporting-e30]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 6b。[证据](../../sources/notes/perciedusert2020reporting.md#e30)
[^perciedusert2020reporting-e31]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 7a。[证据](../../sources/notes/perciedusert2020reporting.md#e31)
[^landis2012call-e9]: Landis 等人 2012，Interim data analysis。[证据](../../sources/notes/landis2012call.md#e9)
[^landis2012call-e7]: Landis 等人 2012，Randomization and blinding。[证据](../../sources/notes/landis2012call.md#e7)
[^landis2012call-e12]: Landis 等人 2012，An important note about exploratory experiments。[证据](../../sources/notes/landis2012call.md#e12)
[^landis2012call-e17]: Landis 等人 2012，An important note about exploratory experiments。[证据](../../sources/notes/landis2012call.md#e17)
[^landis2012call-e15]: Landis 等人 2012，Small effect sizes。[证据](../../sources/notes/landis2012call.md#e15)
[^landis2012call-e6]: Landis 等人 2012，Box 1。[证据](../../sources/notes/landis2012call.md#e6)
[^landis2012call-e1]: Landis 等人 2012，Abstract。[证据](../../sources/notes/landis2012call.md#e1)
[^curtis2018experimental-e14]: Curtis 等人 2018，Key points of the updated guidance。[证据](../../sources/notes/curtis2018experimental.md#e14)
[^curtis2018experimental-e5]: Curtis 等人 2018，Key points of the updated guidance。[证据](../../sources/notes/curtis2018experimental.md#e5)
[^curtis2018experimental-e11]: Curtis 等人 2018，Flexibility and pilot data。[证据](../../sources/notes/curtis2018experimental.md#e11)
[^uhlen2016proposal-e6]: Uhlen 等人 2016，Suggestions for providers and users。[证据](../../sources/notes/uhlen2016proposal.md#e6)
[^freedman2015economics-e3]: Freedman 等人 2015，正文，细胞系的例子。[证据](../../sources/notes/freedman2015economics.md#e3)
[^freedman2015economics-e10]: Freedman 等人 2015，正文，细胞系的例子。[证据](../../sources/notes/freedman2015economics.md#e10)
[^schnell2015ten-e10]: Schnell 2015，Rule 5。[证据](../../sources/notes/schnell2015ten.md#e10)
[^schnell2015ten-e11]: Schnell 2015，Rule 5。[证据](../../sources/notes/schnell2015ten.md#e11)
[^schnell2015ten-e3]: Schnell 2015，Rule 4。[证据](../../sources/notes/schnell2015ten.md#e3)
[^rossner2004what-e1]: Rossner 和 Yamada 2004，引言。[证据](../../sources/notes/rossner2004what.md#e1)
[^rossner2004what-e2]: Rossner 和 Yamada 2004，Journal guidelines。[证据](../../sources/notes/rossner2004what.md#e2)
[^rossner2004what-e3]: Rossner 和 Yamada 2004，Journal guidelines。[证据](../../sources/notes/rossner2004what.md#e3)
[^rossner2004what-e4]: Rossner 和 Yamada 2004，Gross misrepresentation。[证据](../../sources/notes/rossner2004what.md#e4)
[^rossner2004what-e5]: Rossner 和 Yamada 2004，Cleaning up background。[证据](../../sources/notes/rossner2004what.md#e5)
[^rossner2004what-e6]: Rossner 和 Yamada 2004，Splicing lanes together。[证据](../../sources/notes/rossner2004what.md#e6)
[^rossner2004what-e7]: Rossner 和 Yamada 2004，Linear vs. nonlinear adjustments。[证据](../../sources/notes/rossner2004what.md#e7)
[^rossner2004what-e8]: Rossner 和 Yamada 2004，Other data-management issues。[证据](../../sources/notes/rossner2004what.md#e8)
[^rossner2004what-e9]: Rossner 和 Yamada 2004，Brightness/contrast adjustments。[证据](../../sources/notes/rossner2004what.md#e9)
[^rossner2004what-e10]: Rossner 和 Yamada 2004，Other data-management issues。[证据](../../sources/notes/rossner2004what.md#e10)
[^rossner2004what-e11]: Rossner 和 Yamada 2004，Conclusion。[证据](../../sources/notes/rossner2004what.md#e11)
[^weissgerber2015beyond-e1]: Weissgerber 等人 2015，Introduction。[证据](../../sources/notes/weissgerber2015beyond.md#e1)
[^weissgerber2015beyond-e2]: Weissgerber 等人 2015，Introduction。[证据](../../sources/notes/weissgerber2015beyond.md#e2)
[^weissgerber2015beyond-e3]: Weissgerber 等人 2015，Recommendations for a New Data Presentation Paradigm。[证据](../../sources/notes/weissgerber2015beyond.md#e3)
[^weissgerber2015beyond-e4]: Weissgerber 等人 2015，Introduction 和 Are Your Figures Worth a Thousand Words?。[证据](../../sources/notes/weissgerber2015beyond.md#e4)
[^weissgerber2015beyond-e5]: Weissgerber 等人 2015，Are Your Figures Worth a Thousand Words?。[证据](../../sources/notes/weissgerber2015beyond.md#e5)
[^errington2021challenges-e7]: Errington 等人 2021（eLife e67995），Abstract。[证据](../../sources/notes/errington2021challenges.md#e7)
[^errington2021challenges-e8]: Errington 等人 2021（eLife e67995），Requesting assistance from original authors。[证据](../../sources/notes/errington2021challenges.md#e8)
