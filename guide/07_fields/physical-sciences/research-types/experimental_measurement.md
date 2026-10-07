# 实验测量研究

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**以测量为中心的实验**：目标是测出一个物理量的值，并说清这个值有多可信。例如测一个常数、一种材料的某项性质、一个粒子的寿命。工程里的试验台测试（测效率、载荷、流量等）也可以按本文的步骤做 `[本项目分析]`；工程期刊对不确定度的要求见[机械工程领域概况](../../mechanical-engineering/README.md#测量结果要带上不确定度)。5σ 发现标准、盲分析的基本概念，[物理科学领域概况](../README.md)已经讲过，本文只讲具体怎么做。计算机里的性能测量也要对付噪声和测量偏差，可以对照[基准评测](../../computer-science/practices/benchmarking.md#第四步设计测量流程)读。

**读完本文，你应该能：**

- 把要测的量定义清楚，并按它设计装置和测量程序；
- 做校准，找出并处理系统效应；
- 列一张不确定度预算表，算出合成不确定度和扩展不确定度；
- 用盲分析和交叉检验防止自己"不知不觉往想要的数靠"；
- 按规范报告结果，并和理论、其他测量做比较。

---

## 1. 这是什么研究，什么时候用

实验测量研究回答的问题是：**这个量是多少？可信到什么程度？** 只给数值、不给可信程度，测量结果之间、测量结果和标准里的参考值之间，都无法比较[^jcgm2008gum-e28]。

| 研究类型 | 回答什么 | 去哪里看 |
|---|---|---|
| 实验测量（本文） | 一个量的值和它的不确定度 | 本文 |
| 搜寻与发现 | 有没有新效应，显著到什么程度 | [物理科学领域概况：5σ](../README.md#5σ宣布发现的门槛)；最后报告的测量值或上限，仍按本文处理不确定度 `[本项目分析]` |
| 性能基准评测 | 哪个计算机系统更快、更好 | 计算机篇[基准评测](../../computer-science/practices/benchmarking.md) |

## 2. 怎么做

### 第一步：定义被测量

**怎么做**：写清你要测的量（计量学叫**被测量**，measurand），连同测量方法和测量程序[^jcgm2008gum-e11]。定义要完整到这个量在实际用途上只有一个值；要测得越准，定义就要越细[^jcgm2008gum-e12]。GUM（计量指南联合委员会 JCGM 发布的国际指南《测量不确定度表示指南》）举的例子是：要把一根约一米长的钢棒测到微米级，就得写明"在什么温度、什么压力下的长度"[^jcgm2008gum-e12]。

**为什么**：定义本身不完整，就会给结果带来一个不确定度分量[^jcgm2008gum-e13]。测得再仔细，也消不掉这一项。

**容易错在哪里**：只写"测钢棒长度"，不写条件；或者选了一个系统效应很难控制的量。Junk 和 Lyons 讲粒子物理时提到：系统不确定度难以控制时，可以改测一个定义更明确的量，例如两个产生率的比值[^junk2021reproducibility-e41]。

### 第二步：设计装置和测量程序，先估灵敏度

**怎么做**：

1. 列出所有可能影响读数的量（温度、气压、电源、对准、样品状态等），想好哪些要控制、哪些要监测记录 `[本项目分析]`；
2. 让这些相关的量在实验中尽可能实际变化，这样不确定度评定能尽量建立在观测数据上[^jcgm2008gum-e14]；
3. 取数据之前，至少在分析数据之前，先估算预期能测多准。Junk 和 Lyons 说这在实验粒子物理里是常规且必要的做法[^junk2021reproducibility-e44]；
4. 第一次做不确定度分析，要先弄清需要多少资源，把数据收集和分析的计划仔细排好[^nist2012ehandbook-e5]。

**为什么**：设计良好的实验能让不确定度评定可靠得多[^jcgm2008gum-e15]。先估灵敏度还有一个好处：结果不显著、但检验的灵敏度高，这个结果也值得发表[^junk2021reproducibility-e45]。

**容易错在哪里**：一次性的、破坏性的试验，很难事后再表征测量过程[^nist2012ehandbook-e17]，所以更要事先设计好。装置本身怎么搭（屏蔽、接地、隔振、温控等），本文资料未涉及，以导师和本组的经验为准。

### 第三步：校准，并持续核查

**怎么做**：

- **校准**：把你的仪器或样品和参考标准相比较，目的是消除或减小测量系统相对于参考基准的偏差[^nist2012ehandbook-e1]。参考标准和标准物质本身的不确定度仍要计入[^jcgm2008gum-e19]。
- **设一个核查标准**（check standard）：找一个稳定的样品，隔一段时间测一次，用来暴露测量过程随时间出现的误差[^nist2012ehandbook-e2]。它的材料和形状要和你平时测的样品接近[^nist2012ehandbook-e3]。它的读数如果在几轮测量里持续停在一个新水平，就是要查原因的信号[^nist2012ehandbook-e4]。
- **先测一个已知的东西**：用同一套装置和分析测一个早有定论的信号（粒子物理叫"标准烛光"），强度和性质都符合预期，才说明整条链条在正常工作[^junk2021reproducibility-e46]。

**容易错在哪里**：校准也会被自己的期望影响。Junk 和 Lyons 指出，潜意识的偏差可能在校准环节进入分析[^junk2021reproducibility-e48]。小课题组可以先把校准方法定下来、写进记录本，再看测量结果 `[本项目分析]`。模型参数的"校准"和"确认"不是一回事，见[机械工程领域概况](../../mechanical-engineering/README.md#校准不是确认)。

### 第四步：找出并处理系统效应

**先分清两种误差。** 统计误差可以靠重复发现：重复几次，结果会变。**系统效应**会把结果从真值推开，但不一定每次都变[^junk2021reproducibility-e36]，所以重复再多次也发现不了它。

**怎么做**：

1. **把系统效应找全。** 系统效应不容易发现，评估它们一般要多花得多的功夫[^junk2021reproducibility-e34]。最麻烦的是被忽略或被错误排除的那些[^junk2021reproducibility-e40]。
2. **能修正的先修正。** 随机误差无法修正，偏差至少在理论上可以修正[^nist2012ehandbook-e6]。系统误差消除不了，但常常可以减小：对识别出的系统效应施加修正值或修正因子[^jcgm2008gum-e18]。GUM 的前提就是：结果已经对所有已识别的重要系统效应做了修正[^jcgm2008gum-e10]。
3. **修正值的不确定度要计入。** 修正之后，修正值本身的不确定度进入总不确定度[^junk2021reproducibility-e35][^nist2012ehandbook-e7]。
4. **用多种办法估计同一个效应。** 粒子物理会用几个不同的控制样本（已知没有信号的数据）去预测本底，预测之间的差异常被计入系统不确定度[^junk2021reproducibility-e47]。

**容易错在哪里**：以为做了盲分析就不用管系统误差。盲分析只解决实验者偏差这一个问题；其他偏差盲不盲都还要修正，或计入系统不确定度[^klein2005blind-e7]。

### 第五步：做不确定度预算

**不确定度预算**是一张表：列出每个不确定度分量，以及它的灵敏系数、标准差和自由度[^nist2012ehandbook-e14]。

**1. 逐项评定，都换成"标准不确定度"（一个标准差）。**

- **A 类评定**：对重复观测做统计分析；**B 类评定**：用统计分析以外的办法[^jcgm2008gum-e3]。A 类要注意漂移：重复观测之间如果随时间相关，普通的平均值和平均值标准差可能不合适[^jcgm2008gum-e21]。NIST 手册列的 B 类来源有：别的实验室校准的参考标准、计算里用的物理常数、无法抽样的环境影响、仪器的装配偏差、仪器分辨力不足[^nist2012ehandbook-e10]。
- **B 类注意换算**：别处给的不确定度，通常报的是扩展不确定度 U，要除以 k 换成标准不确定度；没写 k 时，NIST 手册认为假设 k = 2 大概是保守的[^nist2012ehandbook-e11]。只知道"不超过 ±a"时，不能把 a 直接拿来和其他分量相加，要先换成等效的标准差[^nist2012ehandbook-e12]。对区间内的情况一无所知，就只能假设均匀分布，标准差是 a/√3[^jcgm2008gum-e22]，这是最保守的估计[^nist2012ehandbook-e13]。

**2. 合成。** A 类和 B 类分量处理方式相同[^nist2012ehandbook-e9]，都代入不确定度传播公式[^jcgm2008gum-e23]。基本做法是按平方和开根号合成[^nist2012ehandbook-e8]；输入量之间有显著相关时，必须把相关性考虑进去[^jcgm2008gum-e24]。

**3. 扩展。** 扩展不确定度 U = k × 合成标准不确定度[^jcgm2008gum-e25]。美国国家标准与技术研究院（NIST）和 SEMATECH（美国半导体产业联盟）合编的统计手册建议：自由度较大时取 k = 2，近似对应 95% 的包含概率[^nist2012ehandbook-e15]。NIST 对本院测量结果也规定按惯例取 k = 2[^taylor1994nist-e1]。这是 NIST 自己的政策，其他单位以本单位或目标期刊的要求为准 `[本项目分析]`。大的分量如果只重复了几次、自由度很小，合成结果的自由度就很成问题[^nist2012ehandbook-e16]；这时不要照搬 k = 2，先估算有效自由度再定 k `[本项目分析]`。

**4. 自查。** 把实际观测到的标准差，和由各分量合成预测的标准差比一比[^jcgm2008gum-e17]。两者差得多，说明预算里漏了或高估了某些东西 `[本项目分析]`。

### 第六步：盲分析，防止自己影响结果

盲分析的定义和常见方法，见[物理科学领域概况](../README.md#盲分析先定方法再看答案)。这里讲为什么做、怎么落地。

**为什么**：**实验者偏差**和其他偏差的关键区别是，它的大小没法估计，只能靠方法去预防[^klein2005blind-e1]。Klein 和 Roodman 认为，在核物理和粒子物理里，最常见的一种大概是**停止偏差**：结果接近预想值时，就停止查错、拿去发表[^klein2005blind-e2]。例如 1930—1940 年的一系列光速测量和后来的测定相差 17 千米/秒，他们引用的一份分析推测：研究者一直找误差，直到结果接近公认值才停下[^klein2005blind-e3]。他们查看历史测量，发现测量值倾向于靠近当时已发表的平均值，而不是后来的最终值，但也说这不一定说明有偏差[^klein2005blind-e4]。

**怎么做（以精密测量为例）**：

- **藏起答案，而不是藏起数据。** 盲分析不是不让你看数据，而是不让结果反过来影响分析[^klein2005blind-e17]。精密测量单个参数、且这个参数不直接取决于事件数时，隐藏答案法最合适[^klein2005blind-e14]：在软件里给最后的结果加一个固定的隐藏偏移量，做分析的人看不到它[^junk2021reproducibility-e49]。方案要尽量简单、只遮住尽量少的东西[^klein2005blind-e6]。
- **桌面实验也能做。** Dunnington 测电子荷质比时，让机械师随意设定一个关键角度，分析完成后才去精确测量它[^roodman2003blind-e5]。一个引力实验让合作组外的人保管一个质量块的准确质量，组内只知道到 1%[^klein2005blind-e15]。
- **事先约定揭盲规则。** 揭盲后不改分析的任何步骤，否则就不算完全的盲分析[^junk2021reproducibility-e10]。可能出现的意外，最好事先想好怎么处理[^klein2005blind-e10]。合作组还可以规定，揭盲要由更大的小组批准，而不是分析者自己决定[^klein2005blind-e11]。
- **揭盲后发现真错了怎么办。** 不能因为做了盲分析，就去发表一个已知是错的结果[^klein2005blind-e9]；在论文里写明哪些改动是揭盲后做的[^klein2005blind-e8]。上面那个引力实验组后来改进了分析，但仍发表了改进前的结果[^klein2005blind-e15]。

> **不同的看法：盲分析值不值？**
> - **主张做**：Klein 和 Roodman 认为，实验者偏差的大小没法估计，唯一的办法就是用能预防它的方法[^klein2005blind-e1]；每个实验都应考虑实验者偏差的可能，但盲分析不一定处处可行或必要[^klein2005blind-e5]。
> - **担心代价**：Klein 和 Roodman 自己也承认，"意外现象只有把数据全看一遍才能发现"是个严重问题[^klein2005blind-e12]。物理学家 Golub 在一篇未经同行评审的短评中认为，盲分析会严重妨碍寻找系统误差，也让人没法研究被遮住区域里的意外事件[^golub2023blind-e1]。
>
> 实际做法：精密测量优先用"隐藏答案"，它只遮最终数值，不妨碍查数据和系统误差；做不做、怎么做，看数据前和导师定好并写下来 `[本项目分析]`。

### 第七步：交叉检验和一致性检验

**怎么做**：

- **把数据按条件拆开看。** 按日期、仪器配置、操作者、样品分组，各算一个结果，看彼此是否在不确定度范围内一致 `[本项目分析]`。
- **先看控制样本。** 在控制样本上先跑一遍分析，有时会发现没意识到的本底来源或校准错误[^junk2021reproducibility-e50]。
- **数据说模型不完整，就改模型。** 观测数据（包括对同一个量的独立测定）表明测量模型不完整时，要修改模型[^jcgm2008gum-e16]。
- **异常结果要写出来。** 美国航空航天学会（AIAA）的期刊要求：异常结果不论能否解释，都要指出来[^aiaaeditorialpolicy-e9]。

**容易错在哪里**：拿"和以前的测量或理论一致"当作测量正确的证据。Roodman 指出，结果的数值和它与以前测量是否一致，不能说明测量本身做得对不对[^roodman2003blind-e4]。另外，有些交叉检验只能在揭盲后做[^klein2005blind-e13]，最好事先列出来 `[本项目分析]`。

### 第八步：记录一切

**怎么做**：

- **当场记录。** 每条记录在做完之后立即写[^schnell2015ten-e3]；靠记忆，很可能到时想不起关键步骤[^schnell2015ten-e9]。
- **错了划掉，不要擦掉。** 纸质记录本写错了，划一条细线，在旁边写正确信息[^schnell2015ten-e4]。（Schnell 2015 是写给做计算的生物学者的，这里借用其中通用的记录原则 `[本项目分析]`。）
- **记录运行条件。** 粒子物理实验会持续记录温度、气压、湿度等环境变量[^junk2021reproducibility-e42]。发现异常，要给受影响的数据做标记，以免它们让结果产生偏差[^junk2021reproducibility-e43]。
- **记下采集顺序。** AIAA 期刊要求论文写出实验条件和数据采集的先后顺序[^aiaaeditorialpolicy-e6]，没有当时的记录就写不出来 `[本项目分析]`。
- **保存每张图的原始数据**[^schnell2015ten-e7]。整理数据和代码的通用做法见通用篇[整理科研材料](../../../general/2_during/03_organizing_materials.md)。

**为什么**：记错数、算错数这类过失，不在不确定度的涵盖范围内[^jcgm2008gum-e5]，只能靠记录和检查去发现 `[本项目分析]`。

### 第九步：报告结果

GUM 和 AIAA 对报告的要求（列出全部分量和评定方法、写明 k、写出没计入的来源等），[机械工程领域概况](../../mechanical-engineering/README.md#测量结果要带上不确定度)已经列过，"准确度"不配数字等用词问题也在那里。这里补充三点：

- **统计和系统分开写，系统部分按来源列出**[^junk2021reproducibility-e39]。这样读者能判断多取数据还有没有用，还是结果已经"受系统误差限制"[^junk2021reproducibility-e38]。
- **有效数字**：GUM 说不确定度一般最多给两位有效数字就够了[^jcgm2008gum-e26]。粒子数据组（Particle Data Group）编《粒子物理评论》时的规则更具体：误差的前三位数字在 100—354 之间留两位，在 355—949 之间留一位[^pdg2024intro-e3]；中心值保留到和误差相同的位数，例如 0.827 ± 0.119 写成 0.83 ± 0.12[^pdg2024intro-e4]。
- **读文献注意用词**：不确定度是对误差可能取值的数值估计，但粒子物理学家常把 error（误差）当 uncertainty（不确定度）用[^junk2021reproducibility-e37]。

### 第十步：和理论、其他测量比较

**怎么做**：

- **先看多个测量是否彼此一致。** 粒子数据组的做法：先取加权平均，再用卡方（χ²，按各自的不确定度衡量各测量偏离平均值有多远 `[本项目分析]`）检查各测量是否一致[^pdg2024intro-e1]。卡方偏大，很可能是至少一个实验低估了误差；不知道是哪个，就假设所有误差都被低估了同一个倍数[^pdg2024intro-e2]。
- **注意共有的误差来源。** 判断两个结果是否一致，要分清它们共有的和各自独立的误差来源[^junk2021reproducibility-e52]。
- **不确定度大不是优点。** 系统不确定度很大的结果，更容易"和别人一致"[^junk2021reproducibility-e53]；但高估系统不确定度也有坏处[^junk2021reproducibility-e51]。
- **吻合得太好也要警惕。** 全局拟合里卡方异常地低，常被当作测量可能有偏差的迹象[^klein2005blind-e18]。
- **和别人不一致，不等于你错了。** 离群的数据可能是错的，也可能反过来，主体数据是错的[^pdg2024intro-e5]。改变了某些条件的重复实验，可能比完全照搬更有信息量[^junk2021reproducibility-e54]。

## 3. 检查清单

**必须做到**

- [ ] 被测量定义完整，写明条件和测量方法[^jcgm2008gum-e11][^jcgm2008gum-e12]
- [ ] 已识别的重要系统效应都做了修正，修正值的不确定度计入[^jcgm2008gum-e10][^junk2021reproducibility-e35]
- [ ] 参考标准的不确定度计入[^jcgm2008gum-e19]
- [ ] 列出所有不确定度分量和评定方法[^jcgm2008gum-e8]
- [ ] 报告扩展不确定度时写明 k[^jcgm2008gum-e9]
- [ ] 写出已知但没计入的不确定度来源（AIAA 期刊的要求）[^aiaaeditorialpolicy-e5]
- [ ] 实验条件和采集顺序有记录、有报告（AIAA 期刊的要求）[^aiaaeditorialpolicy-e6]

**做到更好**

- [ ] 取数据前估算预期灵敏度[^junk2021reproducibility-e44]
- [ ] 用核查标准持续监控测量过程[^nist2012ehandbook-e2]
- [ ] 用已知信号（标准烛光）检验整条链条[^junk2021reproducibility-e46]
- [ ] 看结果前定好盲分析方案，事先想好揭盲后的意外怎么处理[^klein2005blind-e10]
- [ ] 统计和系统不确定度分开报告，系统部分按来源列出[^junk2021reproducibility-e38][^junk2021reproducibility-e39]
- [ ] 比较观测标准差和预算预测的标准差[^jcgm2008gum-e17]
- [ ] 不确定度一般最多两位有效数字[^jcgm2008gum-e26]；中心值与之对齐（粒子数据组的做法）[^pdg2024intro-e4]

**这些情况可以不做，不算缺陷**

- 盲分析不一定在所有测量里都可行或必要，但每个实验都应考虑实验者偏差的可能[^klein2005blind-e5]。

**审稿时常见、但不成立的批评**

- "结果和理论（或以前的测量）不一致，所以测错了"：数值是否和以前一致，不能说明测量本身对不对[^roodman2003blind-e4]；也可能是以前的主体数据错了[^pdg2024intro-e5]。更该问的是系统效应查全了没有 `[本项目分析]`。

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只报数值，不报不确定度 | 结果无法和别的测量或标准比较[^jcgm2008gum-e28] |
| 只靠重复测量估不确定度 | 系统效应不随重复而变，重复发现不了[^junk2021reproducibility-e36] |
| 把"最坏情况"的偏差直接和其他分量相加 | 要先换成等效标准差再合成[^nist2012ehandbook-e12] |
| 别处给的 U 直接当标准不确定度用 | 要先除以 k[^nist2012ehandbook-e11] |
| 输入量明明相关，还按独立合成 | 相关性必须考虑[^jcgm2008gum-e24] |
| 结果接近预期就停止查错 | 这正是停止偏差[^klein2005blind-e2] |
| 揭盲后悄悄改分析 | 不再是盲分析[^junk2021reproducibility-e10]；要在论文里写明[^klein2005blind-e8] |
| 以为盲分析能消除系统误差 | 它只防实验者偏差[^klein2005blind-e7] |
| 事后凭记忆补记录 | 关键细节会忘[^schnell2015ten-e9]；过失不在不确定度涵盖范围内[^jcgm2008gum-e5] |

## 5. 延伸阅读

- **JCGM 100:2008（GUM）**：计量指南联合委员会的国际指南，国际计量局网站免费下载。可以先读第 3 章（基本概念）和第 7 章（怎样报告）`[本项目分析]`。它也提醒，它代替不了批判性思考、诚实和专业技能[^jcgm2008gum-e27]。
- **NIST/SEMATECH e-Handbook of Statistical Methods 第 2 章**：美国政府网站上的免费在线手册，讲校准、核查标准和不确定度预算，适合动手时查。
- **Klein & Roodman 2005，Blind Analysis in Nuclear and Particle Physics**：讲实验者偏差和各种盲分析方法。可以配合 Golub 2023（未经同行评审）的质疑读。
- **Junk & Lyons 2021**：粒子物理怎样处理系统不确定度、控制样本、校准和重复实验。
- **粒子数据组《粒子物理评论》Introduction 第 5 节**：粒子数据组怎样平均多个测量、处理不一致的数据、修约。

[^jcgm2008gum-e11]: JCGM 100:2008（GUM），3.1.1。[证据](../../../../sources/notes/jcgm2008gum.md#e11)
[^jcgm2008gum-e12]: JCGM 100:2008（GUM），3.1.3。[证据](../../../../sources/notes/jcgm2008gum.md#e12)
[^jcgm2008gum-e13]: JCGM 100:2008（GUM），D.1.1。[证据](../../../../sources/notes/jcgm2008gum.md#e13)
[^jcgm2008gum-e14]: JCGM 100:2008（GUM），3.4.2。[证据](../../../../sources/notes/jcgm2008gum.md#e14)
[^jcgm2008gum-e15]: JCGM 100:2008（GUM），3.4.2。[证据](../../../../sources/notes/jcgm2008gum.md#e15)
[^jcgm2008gum-e16]: JCGM 100:2008（GUM），3.4.2。[证据](../../../../sources/notes/jcgm2008gum.md#e16)
[^jcgm2008gum-e17]: JCGM 100:2008（GUM），3.4.3。[证据](../../../../sources/notes/jcgm2008gum.md#e17)
[^jcgm2008gum-e18]: JCGM 100:2008（GUM），3.2.3。[证据](../../../../sources/notes/jcgm2008gum.md#e18)
[^jcgm2008gum-e10]: JCGM 100:2008（GUM），3.2.4。[证据](../../../../sources/notes/jcgm2008gum.md#e10)
[^jcgm2008gum-e19]: JCGM 100:2008（GUM），3.2.4 注 1。[证据](../../../../sources/notes/jcgm2008gum.md#e19)
[^jcgm2008gum-e3]: JCGM 100:2008（GUM），2.3.2、2.3.3。[证据](../../../../sources/notes/jcgm2008gum.md#e3)
[^jcgm2008gum-e21]: JCGM 100:2008（GUM），4.2.7。[证据](../../../../sources/notes/jcgm2008gum.md#e21)
[^jcgm2008gum-e22]: JCGM 100:2008（GUM），4.3.7。[证据](../../../../sources/notes/jcgm2008gum.md#e22)
[^jcgm2008gum-e23]: JCGM 100:2008（GUM），5.1.2。[证据](../../../../sources/notes/jcgm2008gum.md#e23)
[^jcgm2008gum-e24]: JCGM 100:2008（GUM），5.2.1。[证据](../../../../sources/notes/jcgm2008gum.md#e24)
[^jcgm2008gum-e25]: JCGM 100:2008（GUM），3.3.7。[证据](../../../../sources/notes/jcgm2008gum.md#e25)
[^jcgm2008gum-e9]: JCGM 100:2008（GUM），7.2.3。[证据](../../../../sources/notes/jcgm2008gum.md#e9)
[^jcgm2008gum-e8]: JCGM 100:2008（GUM），7.1.4。[证据](../../../../sources/notes/jcgm2008gum.md#e8)
[^jcgm2008gum-e26]: JCGM 100:2008（GUM），7.2.6。[证据](../../../../sources/notes/jcgm2008gum.md#e26)
[^jcgm2008gum-e5]: JCGM 100:2008（GUM），3.4.7。[证据](../../../../sources/notes/jcgm2008gum.md#e5)
[^jcgm2008gum-e27]: JCGM 100:2008（GUM），3.4.8。[证据](../../../../sources/notes/jcgm2008gum.md#e27)
[^jcgm2008gum-e28]: JCGM 100:2008（GUM），0.1。[证据](../../../../sources/notes/jcgm2008gum.md#e28)
[^nist2012ehandbook-e1]: NIST/SEMATECH e-Handbook，2.3.1。[证据](../../../../sources/notes/nist2012ehandbook.md#e1)
[^nist2012ehandbook-e2]: NIST/SEMATECH e-Handbook，2.1.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e2)
[^nist2012ehandbook-e3]: NIST/SEMATECH e-Handbook，2.1.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e3)
[^nist2012ehandbook-e4]: NIST/SEMATECH e-Handbook，2.2.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e4)
[^nist2012ehandbook-e5]: NIST/SEMATECH e-Handbook，2.5.1。[证据](../../../../sources/notes/nist2012ehandbook.md#e5)
[^nist2012ehandbook-e6]: NIST/SEMATECH e-Handbook，2.5.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e6)
[^nist2012ehandbook-e7]: NIST/SEMATECH e-Handbook，2.5.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e7)
[^nist2012ehandbook-e8]: NIST/SEMATECH e-Handbook，2.5.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e8)
[^nist2012ehandbook-e9]: NIST/SEMATECH e-Handbook，2.5.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e9)
[^nist2012ehandbook-e10]: NIST/SEMATECH e-Handbook，2.5.4。[证据](../../../../sources/notes/nist2012ehandbook.md#e10)
[^nist2012ehandbook-e11]: NIST/SEMATECH e-Handbook，2.5.4。[证据](../../../../sources/notes/nist2012ehandbook.md#e11)
[^nist2012ehandbook-e12]: NIST/SEMATECH e-Handbook，2.5.4.1。[证据](../../../../sources/notes/nist2012ehandbook.md#e12)
[^nist2012ehandbook-e13]: NIST/SEMATECH e-Handbook，2.5.4.1。[证据](../../../../sources/notes/nist2012ehandbook.md#e13)
[^nist2012ehandbook-e14]: NIST/SEMATECH e-Handbook，2.5.6。[证据](../../../../sources/notes/nist2012ehandbook.md#e14)
[^nist2012ehandbook-e15]: NIST/SEMATECH e-Handbook，2.5.2。[证据](../../../../sources/notes/nist2012ehandbook.md#e15)
[^nist2012ehandbook-e16]: NIST/SEMATECH e-Handbook，2.5.7.1。[证据](../../../../sources/notes/nist2012ehandbook.md#e16)
[^nist2012ehandbook-e17]: NIST/SEMATECH e-Handbook，2.1.1。[证据](../../../../sources/notes/nist2012ehandbook.md#e17)
[^taylor1994nist-e1]: Taylor & Kuyatt 1994（NIST TN 1297），6.5。[证据](../../../../sources/notes/taylor1994nist.md#e1)
[^junk2021reproducibility-e34]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e34)
[^junk2021reproducibility-e35]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e35)
[^junk2021reproducibility-e36]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e36)
[^junk2021reproducibility-e37]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e37)
[^junk2021reproducibility-e38]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e38)
[^junk2021reproducibility-e39]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e39)
[^junk2021reproducibility-e40]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e40)
[^junk2021reproducibility-e41]: Junk & Lyons 2021，§3.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e41)
[^junk2021reproducibility-e42]: Junk & Lyons 2021，§6.1。[证据](../../../../sources/notes/junk2021reproducibility.md#e42)
[^junk2021reproducibility-e43]: Junk & Lyons 2021，§6.1。[证据](../../../../sources/notes/junk2021reproducibility.md#e43)
[^junk2021reproducibility-e44]: Junk & Lyons 2021，§6.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e44)
[^junk2021reproducibility-e45]: Junk & Lyons 2021，§6.3。[证据](../../../../sources/notes/junk2021reproducibility.md#e45)
[^junk2021reproducibility-e46]: Junk & Lyons 2021，§6.4。[证据](../../../../sources/notes/junk2021reproducibility.md#e46)
[^junk2021reproducibility-e47]: Junk & Lyons 2021，§6.4。[证据](../../../../sources/notes/junk2021reproducibility.md#e47)
[^junk2021reproducibility-e48]: Junk & Lyons 2021，§6.5。[证据](../../../../sources/notes/junk2021reproducibility.md#e48)
[^junk2021reproducibility-e10]: Junk & Lyons 2021，§6.6。[证据](../../../../sources/notes/junk2021reproducibility.md#e10)
[^junk2021reproducibility-e49]: Junk & Lyons 2021，§6.6。[证据](../../../../sources/notes/junk2021reproducibility.md#e49)
[^junk2021reproducibility-e50]: Junk & Lyons 2021，§6.6。[证据](../../../../sources/notes/junk2021reproducibility.md#e50)
[^junk2021reproducibility-e51]: Junk & Lyons 2021，§6.9。[证据](../../../../sources/notes/junk2021reproducibility.md#e51)
[^junk2021reproducibility-e52]: Junk & Lyons 2021，§5。[证据](../../../../sources/notes/junk2021reproducibility.md#e52)
[^junk2021reproducibility-e53]: Junk & Lyons 2021，§5。[证据](../../../../sources/notes/junk2021reproducibility.md#e53)
[^junk2021reproducibility-e54]: Junk & Lyons 2021，§5。[证据](../../../../sources/notes/junk2021reproducibility.md#e54)
[^klein2005blind-e1]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e1)
[^klein2005blind-e2]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e2)
[^klein2005blind-e3]: Klein & Roodman 2005，§1。[证据](../../../../sources/notes/klein2005blind.md#e3)
[^klein2005blind-e4]: Klein & Roodman 2005，§1。[证据](../../../../sources/notes/klein2005blind.md#e4)
[^klein2005blind-e5]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e5)
[^klein2005blind-e6]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e6)
[^klein2005blind-e7]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e7)
[^klein2005blind-e8]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e8)
[^klein2005blind-e9]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e9)
[^klein2005blind-e10]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e10)
[^klein2005blind-e11]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e11)
[^klein2005blind-e12]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e12)
[^klein2005blind-e13]: Klein & Roodman 2005，§2。[证据](../../../../sources/notes/klein2005blind.md#e13)
[^klein2005blind-e14]: Klein & Roodman 2005，§3.2。[证据](../../../../sources/notes/klein2005blind.md#e14)
[^klein2005blind-e15]: Klein & Roodman 2005，§3.2.1。[证据](../../../../sources/notes/klein2005blind.md#e15)
[^klein2005blind-e17]: Klein & Roodman 2005，§3.4。[证据](../../../../sources/notes/klein2005blind.md#e17)
[^klein2005blind-e18]: Klein & Roodman 2005，§1。[证据](../../../../sources/notes/klein2005blind.md#e18)
[^roodman2003blind-e4]: Roodman 2003，§2。[证据](../../../../sources/notes/roodman2003blind.md#e4)
[^roodman2003blind-e5]: Roodman 2003，§1。[证据](../../../../sources/notes/roodman2003blind.md#e5)
[^golub2023blind-e1]: Golub 2023（未经同行评审），§2。[证据](../../../../sources/notes/golub2023blind.md#e1)
[^aiaaeditorialpolicy-e6]: AIAA Editorial Policy Statement，Statement of Experimental Design。[证据](../../../../sources/notes/aiaaeditorialpolicy.md#e6)
[^aiaaeditorialpolicy-e9]: AIAA Editorial Policy Statement，Estimation of Precision Uncertainty。[证据](../../../../sources/notes/aiaaeditorialpolicy.md#e9)
[^aiaaeditorialpolicy-e5]: AIAA Editorial Policy Statement，Statement of Total Uncertainty。[证据](../../../../sources/notes/aiaaeditorialpolicy.md#e5)
[^schnell2015ten-e3]: Schnell 2015，Rule 4。[证据](../../../../sources/notes/schnell2015ten.md#e3)
[^schnell2015ten-e4]: Schnell 2015，Rule 5。[证据](../../../../sources/notes/schnell2015ten.md#e4)
[^schnell2015ten-e9]: Schnell 2015，Rule 3。[证据](../../../../sources/notes/schnell2015ten.md#e9)
[^schnell2015ten-e7]: Schnell 2015，Rule 6。[证据](../../../../sources/notes/schnell2015ten.md#e7)
[^pdg2024intro-e1]: Particle Data Group 2024，Introduction §5.2.2。[证据](../../../../sources/notes/pdg2024intro.md#e1)
[^pdg2024intro-e2]: Particle Data Group 2024，Introduction §5.2.2。[证据](../../../../sources/notes/pdg2024intro.md#e2)
[^pdg2024intro-e3]: Particle Data Group 2024，Introduction §5.3。[证据](../../../../sources/notes/pdg2024intro.md#e3)
[^pdg2024intro-e4]: Particle Data Group 2024，Introduction §5.3。[证据](../../../../sources/notes/pdg2024intro.md#e4)
[^pdg2024intro-e5]: Particle Data Group 2024，Introduction §5.4。[证据](../../../../sources/notes/pdg2024intro.md#e5)
