# 准实验与因果识别

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲经济学里**不能随机分组时，怎样用观察性数据估计因果效应**。观察性数据指现成的、不是研究者安排分组得来的数据。全文按这个顺序讲：先写出识别策略，再选双重差分、断点回归、工具变量或合成控制，然后做安慰剂检验、算对标准误、把结果报告清楚。"可信性革命"的来龙去脉，以及几种方法各靠什么假设的一句话介绍，见[经济学领域概况](../README.md#可信性革命先回答你的识别策略是什么)，这里不重复。公共卫生和医学也用观察性数据估计因果效应，但用的词不一样，见健康科学篇的[观察性流行病学](../../health-sciences/research-types/observational_epidemiology.md)。两边的用词对照见第 1 节末尾。效度威胁、探索性和验证性分析等通用概念，见通用篇的[证据与效度](../../../general/2_during/02_evidence_and_validity.md#6-说清效度威胁)和[研究设计](../../../general/1_before/04_research_design.md#4-分清探索性研究和验证性研究)。

**读完本文，你应该能：**

- 用一段话写出自己的识别策略：要估计什么、拿谁和谁比、靠什么假设；
- 按步骤做双重差分、断点回归和工具变量分析，知道每种方法最该检查什么；
- 判断什么时候可以考虑合成控制；
- 做安慰剂检验和稳健性检验，在合适的层级上聚类标准误；
- 避开"处理前趋势不显著就够了""第一阶段 F 大于 10 就够了"这类常见误区。

---

## 1. 这是什么研究，什么时候用

准实验研究回答"X 对 Y 有多大的因果效应"，例如一项最低工资政策是否减少了就业。随机实验做不了时，它借助制度规则或自然事件造成的变化来做比较（见上面链接的领域概况）。

**先看处理是怎样分配的，再选方法。** 下表按"你手里是什么情形"来选 `[本项目分析，依据各行脚注]`：

| 你手里的情形 | 可以考虑 | 关键假设 | 最该检查什么 |
|---|---|---|---|
| 一项政策在某个时间影响了一部分单位，另一部分没受影响，前后都有数据 | 双重差分（difference-in-differences） | 没有政策的话，两组的平均结果会平行变化；政策实施前没有提前出现的效应[^roth2023trending-e1] | 处理前的趋势；结论对趋势偏离有多敏感[^roth2023trending-e6] |
| 是否接受处理，取决于某个分数、年龄、距离等是否越过一条分界线 | 断点回归（regression discontinuity） | 人们不能**精确地**把自己放到分界线的某一侧[^lee2010rd-e1] | 分界线附近有没有人扎堆；事先定下的特征在两侧是否平衡[^lee2010rd-e2] |
| 有一个变量会推动人们接受处理，而它和结果之间没有别的联系 | 工具变量（instrumental variables） | 它确实改变了处理；它只通过这条渠道影响结果；它的取值近似随机[^angrist2010credibility-e5] | 第一阶段有多强；排他性有没有说服力 |
| 只有一个或少数几个城市、州这样的大单位受到处理，处理前有较长的时间序列 | 合成控制（synthetic control） | 一组对照单位的加权组合，在处理前能很好地模仿处理单位[^cunningham2026remix-e15] | 处理前拟合得好不好；安慰剂检验[^cunningham2026remix-e17] |

四种方法都不靠"把能想到的变量都控制住"，靠的是你对**处理怎样分配**的了解 `[本项目分析]`。Cunningham 建议，用工具变量前先问自己：凭什么认为它是随机的？凭什么认为它满足排他性？做自己最严厉的批评者[^cunningham2026remix-e7]。这个问题对其他三种方法同样适用 `[本项目分析]`。

> **和流行病学的用词对照** `[本项目分析]`：下表是本项目归纳的粗略对应，两边的词并不等价，只帮你在读另一边的文献时找到相近的概念。
>
> | 经济学常说 | 流行病学里相近的说法 |
> |---|---|
> | 识别策略（说清凭什么能作因果解释） | 没有一一对应的词。相近的做法是把观察性分析看作在模拟一项假想的"目标试验"（target trial）[^hernan2018cword-e5] |
> | 遗漏变量偏差（漏掉了同时影响处理和结果的因素） | 混杂（confounding）；Hernán 认为，目标是因果时一般需要调整混杂[^hernan2018cword-e13] |
> | 控制变量 | 调整的变量、协变量 |
>
> 说理的出发点也不太一样：经济学的准实验论文重在论证"处理的变化从哪来、为什么近似随机"；流行病学篇的做法更多从"要模拟哪项试验、要调整哪些混杂因素"出发。这只是本项目对两篇读到的资料的粗略比较。

---

## 2. 怎么做

### 第 1 步：动手之前，写出识别策略

**怎么做。** 跑回归之前，先写一段话，回答三个问题：

1. **要估计什么**：谁的效应、哪段时间的效应。双重差分里，是"已处理单位的平均效应"，还是某个时间点之后的效应？
2. **拿谁和谁比**：对照组是谁，为什么选它们。
3. **靠什么假设**：这些假设在你的情境下为什么说得通。

Roth 等人总结近年双重差分方法时，把要点归为三条：讲清用于识别的对照组；估计和推断方法要和识别假设匹配；检查结论对假设被违反有多稳健。他们还强调，选对假设往往要靠对具体情境的了解[^roth2023trending-e11]。

**为什么。** 经济学界为什么这样看重识别策略，见[领域概况](../README.md#可信性革命先回答你的识别策略是什么)。

**容易错在哪里。**

- **边看结果边改设定。** 控制变量、样本范围、对照组，要在看到结果之前就定下来，并且公开说明[^cunningham2026remix-e14]。如果事先没法在两种方法之间做选择，就两种都报告[^cunningham2026remix-e13]。
- **把设定搜索当成稳健性。** Brodeur 等人统计了 2005–2011 年 AER、JPE、QJE 三本经济学期刊上发表的约五万个检验（2013 年讨论稿版），发现刚好低于 0.05 的 p 值偏多。他们的解释是：结果差一点显著时，研究者可能会去挑一个"显著"的设定[^brodeur2016star-e2][^brodeur2016star-e3]。在他们的数据里，用随机对照试验或实验室实验数据的论文，这种现象较轻[^brodeur2016star-e5]。
- **设计不成立时舍不得放弃。** Cunningham 的双重差分清单最后一步叫"别做双重差分"：手里的牌不行，就尽早换方法[^cunningham2026remix-e12]。

### 第 2 步：双重差分

**假设是什么。** 标准的双重差分靠两条假设：没有政策的话，处理组和对照组的平均结果会平行变化（平行趋势）；政策实施之前没有提前出现的效应（无预期效应）[^roth2023trending-e1]。平行趋势允许两组原本水平不同，但两组之间的这种差别，在政策前后必须一样大[^roth2023trending-e2]。

**怎么做。**

1. **先数清楚，再画出来。** 数清每一批（同一时间开始受处理的）单位有多少，包括从未受处理的和一直受处理的；画出处理随时间铺开的情况；选定对照组并写明理由[^cunningham2026remix-e11]。
2. **画事件研究图**，看处理前各期两组的差别是否接近零[^roth2023trending-e6]。但要记住：平行趋势本身无法检验，真正需要的是处理**之后**的反事实趋势相同，这和"处理前趋势平行"不是一回事[^cunningham2026remix-e9]。
3. **别把"前趋势不显著"当成证据。** 这类检验的检验力往往很低；按预检验结果决定怎么分析，本身还会带来偏差[^roth2023trending-e5]。Roth 等人主张把敏感性分析作为标准做法[^roth2023trending-e6]，例如报告：处理后的趋势偏离要达到处理前最大偏离的多少倍，结论才会被推翻[^roth2023trending-e7]。
4. **政策分批实施时，别直接用常规回归。** 各单位在不同时间开始受处理时，常规的双向固定效应回归（同时控制单位和时间的回归）会拿"已经受处理的"单位当对照。Roth 等人称之为"禁止的比较"：处理效应因单位而异时，系数甚至可能和所有个体效应的符号相反[^roth2023trending-e3]。改用专门处理这种情况的新估计方法。据 Roth 等人的经验，这些方法的结果通常（但不总是）相近，首要的是讲清要估什么、拿谁和谁比[^roth2023trending-e4]。他们的论文表 2 列出了相应的 R 和 Stata 软件包[^roth2023trending-e13]。分批实施时，事件研究图也不要用常规的动态回归来画[^roth2023trending-e12]。

### 第 3 步：断点回归

**怎么做。**

1. **先确认分界线上没有别的事。** 同一条线上如果还有别的制度变化，效应会被算错。Imbens 和 Lemieux 举的例子是：很多文化场所从 65 岁开始给优惠，但 65 岁时还有别的制度变化；在 65 岁看到的跳变，更可能来自这些别的变化[^imbens2008rd-e2]。
2. **检查有没有人精确地"挤"过分界线。** 人们对分数总有一定影响力，这不要紧；要紧的是能不能**精确地**把自己放到某一侧[^lee2010rd-e1]。画出驱动变量（决定是否受处理的那个分数）的直方图[^lee2010rd-e3]，可以再做 McCrary 密度检验。分布在分界线处跳变，不一定能证明设计失效，但能帮你发现异常[^imbens2008rd-e4]。这个检验也会漏判：有人往上挤、有人往下挤，相互抵消后，分布看起来仍然连续[^lee2010rd-e4]。
3. **检查两侧是否平衡。** 用事先就定下来的特征（基线协变量）当"结果"，做一遍同样的断点回归[^lee2010rd-e7]。处理在分界线上跳变，一般不会让这些特征跟着跳变[^imbens2008rd-e3]。这和检验随机实验分组是否平衡是一个道理[^lee2010rd-e2]。
4. **画主图。** 把驱动变量分成若干小区间，画出每个区间里结果的平均值[^imbens2008rd-e1]。不要只画一条在分界线处断开的平滑曲线，那样即使没有跳变，也容易看起来像有[^lee2010rd-e5]。图有被"做"出效果的空间，所以图要配上正式估计[^lee2010rd-e10]。
5. **估计，并换带宽、换设定。** Imbens 和 Lemieux 的操作总结建议，在分界线两侧一定范围（带宽）内分别做线性回归[^imbens2008rd-e7]。他们还说，不管带宽怎么选，都要报告带宽加倍、减半时的结果；结果只在某个带宽下成立，就远没有那么可信[^imbens2008rd-e6]。Lee 和 Lemieux 建议在一系列带宽和多项式阶数下估计，报告一个"典型"估计值和估计值的范围[^lee2010rd-e6]。这两篇都是 2008–2010 年的文章；带宽具体怎么选、置信区间怎么算，更新的做法本文资料未涉及，以导师或目标期刊的要求为准。
6. **在假的分界线上做检验**，看本不该有跳变的地方是否也"跳"了[^imbens2008rd-e5]。

如果越过分界线只是提高了受处理的**概率**（"模糊"断点），它就相当于一个工具变量，对应随机实验里"只随机分配了资格、没人强制遵从"的情形[^lee2010rd-e11]，第 4 步的要点也适用。

### 第 4 步：工具变量

**三件事要分开讲清。**

- **第一阶段**：工具变量确实改变了处理。这一条可以用数据检验[^cunningham2026remix-e4]。
- **排他性和近似随机**：工具变量只通过你关心的渠道影响结果，取值近似随机。这两条不能只贴标签，必须充分论证[^angrist2010credibility-e5]，并专门检查它会不会经由别的渠道影响结果[^angrist2010credibility-e9]。
- 工具变量有好几条无法检验的假设，只要让人怀疑排他性，结论就站不住[^cunningham2026remix-e6]。所以论证要写在论文里，不能只放在脑子里 `[本项目分析]`。

**弱工具变量。** 工具变量和处理的关系太弱时，第二阶段的结果可能看起来没问题，其实不可信。Cunningham 转引的 Bound、Jaeger 和 Baker（1995）做过一个模拟：把真实工具变量换成随机生成的数字，第二阶段结果看起来仍"相当合理"，完全看不出工具是随机编的[^cunningham2026remix-e3]。"第一阶段 F 统计量大于 10"是一条老的经验门槛。Cunningham 在教材里写道，这个数字"现在普遍被认为太低"，在有多个内生变量、异方差或误差不服从正态分布时尤其如此[^cunningham2026remix-e1]。这是 Cunningham 对当前看法的概括，本文没有读到他所依据的原始文献。他的建议是：用 Olea 和 Pflueger 的"有效 F 统计量"判断强弱，并报告 Anderson-Rubin 置信区间[^cunningham2026remix-e2]。后者是一种工具较弱时仍可用的置信区间 `[本项目分析]`。

**解释结果。** 几条假设都满足时，工具变量估计的是"遵从者"的平均效应[^cunningham2026remix-e5]。遵从者就是行为被工具变量改变了的那部分人。写结论时要说清这是谁的效应，不要说成所有人的效应 `[本项目分析]`。

**展示。** 给读者看估计的"分子"和"分母"[^cunningham2026remix-e8]：分子是简约式（工具变量对结果的影响），分母是第一阶段（工具变量对处理的影响）。最好都配上图。

### 第 5 步：合成控制（简要）

Cunningham 指出，传统的比较案例研究挑对照组时往往随意、可能主观。合成控制的思路是：分析单位只有少数几个城市或州时，多个对照单位的加权组合，往往比单个对照更像处理单位[^cunningham2026remix-e15]。

- 构造合成控制用不到处理之后的结果[^cunningham2026remix-e16]，这有助于避免边看结果边调模型 `[本项目分析]`。
- 推断时把每个未处理单位都假装成处理单位重做一遍，得到一组"安慰剂效应"，用它们的分布来判断真实效应是否突出[^cunningham2026remix-e17]。据 Cunningham 转述，Abadie、Diamond 和 Hainmueller（2010）建议剔除处理前拟合误差和处理单位相差很大的单位[^cunningham2026remix-e18]。
- 合成控制的更多细节，本文资料只读到 Cunningham 第 11 章，以它为起点；更新的综述（如 Abadie 2021）本文未读，资料未涉及。

### 第 6 步：安慰剂检验和稳健性检验

**安慰剂检验**：在本不该有效应的地方找效应。找到了，就说明你的设计可能有问题 `[本项目分析]`。

- 双重差分：做"证伪检验"，检验其他解释。常见两类：同一个结果、换一组不该受影响的人；同一组人、换一个不该受影响的结果[^cunningham2026remix-e10]。
- 断点回归：基线协变量检验[^lee2010rd-e7]；假分界线检验[^imbens2008rd-e5]。
- 州级政策的双重差分：Bertrand 等人提出，随机生成不存在的"安慰剂法律"，用它们的估计效应构成检验所用的分布[^bertrand2004trust-e2]。

**稳健性检验**：Lee 和 Lemieux 对断点回归的主要建议是不要只依赖一种方法或设定[^lee2010rd-e9]，这对其他方法也适用 `[本项目分析]`。但 Angrist 和 Pischke 提醒，撒大网式地跑大量回归，不能为因果解释提供多少依据[^angrist2010credibility-e13]。要换哪些设定，同样应事先定好[^cunningham2026remix-e14]。

### 第 7 步：标准误与聚类

**为什么要聚类。** 同一个州、同一个村的观测，误差往往相关。这时默认标准误会严重高估精度[^cameron2015practitioner-e1]。考虑组内相关后的标准误比默认标准误大好几倍，并不少见[^cameron2015practitioner-e2]。最典型的情形，就是要估计政策变量这种在同一组内取值都一样的变量的效应[^cameron2015practitioner-e3]。

Bertrand、Duflo 和 Mullainathan 在美国州级女性工资数据中随机生成假法律，用常规双重差分估计（2002 年工作论文版）。在约 20 年的数据下，最多有 45% 的假法律"显著"[^bertrand2004trust-e1]。据 Cameron 和 Miller 转述，这篇论文指出，许多双重差分研究没有处理组内相关，处理了的也常在错误的层级上聚类[^cameron2015practitioner-e5]。

**在哪一级聚类。** Roth 等人的经验法则是：在处理被独立分配的那一级聚类。政策按州定，就按州聚类[^roth2023trending-e8]。

**聚类太少怎么办。** Cameron 和 Miller 说，"太少"没有明确界线；在各聚类大小相近时，视情况从少于 20 个到少于 50 个不等。聚类太少又不加修正，检验会过多拒绝原假设，置信区间也会过窄[^cameron2015practitioner-e4]。双重差分里，如果受处理的聚类很少，常规方法可能表现很差，要考虑其他推断方法[^roth2023trending-e9][^roth2023trending-e8]。具体选哪种方法，本文资料只读到概述，见 Cameron 和 Miller 第 VI 节、Roth 等人第 5.1 节。

### 第 8 步：报告

按下面的顺序组织结果，读者最容易判断你的设计是否可信 `[本项目分析，依据各条脚注]`：

1. **识别策略段落**：要估什么、拿谁和谁比、靠什么假设、为什么说得通（第 1 步）。
2. **原始数据的图**：双重差分画处理铺开图和事件研究图[^cunningham2026remix-e11][^roth2023trending-e6]；断点回归画驱动变量直方图和分区间均值图[^lee2010rd-e3][^lee2010rd-e5]；工具变量画第一阶段和简约式[^cunningham2026remix-e8]。
3. **主结果**：一个典型估计值，加上不同设定下的范围[^lee2010rd-e6]；工具变量另报有效 F 统计量和 Anderson-Rubin 置信区间[^cunningham2026remix-e2]。
4. **检验和敏感性分析**：安慰剂检验、平衡检验、平行趋势敏感性分析[^roth2023trending-e6]。正文放不下的，放进网上附录[^lee2010rd-e8]。
5. **结论的适用范围**：效应是谁的效应，比如分界线附近的人、遵从者[^cunningham2026remix-e5]。

数据和代码的公开要求见领域概况的[数据和代码要能复现](../README.md#数据和代码要能复现)。

---

## 3. 检查清单

**必须做到**

- [ ] 写出识别策略：要估计什么、对照组是谁、靠什么假设、为什么说得通[^roth2023trending-e11]
- [ ] 主要设定（控制变量、样本、对照组）在看结果之前定下来[^cunningham2026remix-e14]
- [ ] 双重差分：画事件研究图[^roth2023trending-e6]；政策分批实施时，不用常规双向固定效应回归作主要估计[^roth2023trending-e3]
- [ ] 断点回归：展示驱动变量分布[^lee2010rd-e3]、基线协变量检验[^lee2010rd-e7]、带宽敏感性[^imbens2008rd-e6]
- [ ] 工具变量：报告第一阶段，写出排他性论证[^angrist2010credibility-e5]，按 Cunningham 的建议用有效 F 统计量判断工具强弱[^cunningham2026remix-e2]
- [ ] 标准误在处理被独立分配的层级上聚类[^roth2023trending-e8]

**做到更好**

- [ ] 双重差分报告平行趋势的正式敏感性分析，例如"偏离要多大才推翻结论"[^roth2023trending-e7]
- [ ] 工具变量报告 Anderson-Rubin 置信区间[^cunningham2026remix-e2]，并给出第一阶段和简约式的图[^cunningham2026remix-e8]
- [ ] 至少一项安慰剂或证伪检验[^cunningham2026remix-e10]
- [ ] 断点回归在假分界线上做检验[^imbens2008rd-e5]
- [ ] 聚类很少时，换用适合少数聚类的推断方法[^cameron2015practitioner-e4]

**这些情况可以不做，不算缺陷**

- 不必把每种带宽、阶数、协变量组合都放进正文，可以放进网上附录[^lee2010rd-e8]。

**审稿时常见、但不成立的批评**

- "分数受个人努力影响，所以断点回归无效。"人们对分数有一定影响力不要紧，要紧的是能不能**精确**控制[^lee2010rd-e1]。回应时拿出直方图和协变量平衡检验 `[本项目分析]`。
- "你的样本就是全部 50 个州，没有更大的总体，所以标准误没有意义。"Roth 等人认为不必担心：把不确定性看作来自处理分配的随机性，分析通常仍然说得通[^roth2023trending-e10]。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 处理前趋势"不显著"，就宣称平行趋势成立 | 这类检验的检验力往往很低[^roth2023trending-e5]；处理前平行，也不等于处理后的反事实平行[^cunningham2026remix-e9] |
| 政策分批实施，仍用常规双向固定效应回归 | 会拿已处理单位当对照，系数可能和真实效应符号相反[^roth2023trending-e3] |
| 断点回归只画一条在分界线处断开的平滑曲线 | 即使没有跳变，也容易看起来像有[^lee2010rd-e5] |
| 断点回归只报告一个带宽的结果 | 结果只在某个带宽下成立，就远没有那么可信[^imbens2008rd-e6] |
| 工具变量只说"外生"，不论证排他性 | 必须充分论证[^angrist2010credibility-e5]；只要让人怀疑排他性，结论就站不住[^cunningham2026remix-e6] |
| 第一阶段 F 大于 10 就认为工具够强 | 据 Cunningham 的概括，这个门槛现在普遍被认为太低[^cunningham2026remix-e1]；弱工具的第二阶段结果看起来也可能很"合理"[^cunningham2026remix-e3] |
| 把工具变量的估计说成所有人的效应 | 它估计的是遵从者的效应[^cunningham2026remix-e5] |
| 用默认标准误，或在比处理分配更细的层级上聚类 | 默认标准误会严重高估精度[^cameron2015practitioner-e1]；在州级数据上用常规双重差分，最多 45% 的假法律会"显著"（2002 年工作论文版的模拟）[^bertrand2004trust-e1] |
| 试遍设定，只报告显著的那个 | 刚好低于 0.05 的 p 值偏多，可能就来自这种挑选[^brodeur2016star-e3]；撒大网式的回归不能支撑因果解释[^angrist2010credibility-e13] |
| 设计明显不成立，还硬着头皮做下去 | 手里的牌不行，就尽早换方法[^cunningham2026remix-e12] |

---

## 5. 延伸阅读

- **Cunningham，Causal Inference: The Remix（免费在线）**：第 6、7、9、10、11 章分别讲断点回归、工具变量、双重差分（基础和复杂设计）、合成控制。第 10 章有一份双重差分设计清单。注意这是仍在修订的网络版，内容可能变动，本文引用的是 2026 年 10 月 6 日读到的版本；第一版（The Mixtape，2021）也可免费在线读。适合入门 `[本项目分析]`。
- **Roth 等人 2023，What's Trending in Difference-in-Differences?（arXiv 免费）**：近年双重差分方法的综述。表 1 是检查清单，表 2 是软件包列表。做双重差分前值得先读 `[本项目分析]`。
- **Lee & Lemieux 2010，Regression Discontinuity Designs in Economics（NBER 工作论文免费）**：讲断点回归什么时候成立，第 4.6 节有一份实施清单。
- **Imbens & Lemieux 2008，Regression Discontinuity Designs: A Guide to Practice（NBER 工作论文免费）**：第 7 节讲各种检验，第 8 节是操作步骤总结。
- **Cameron & Miller 2015，A Practitioner's Guide to Cluster-Robust Inference（作者主页免费）**：聚类标准误怎么算、聚类太少怎么办。
- **Bertrand, Duflo & Mullainathan 2004（NBER 工作论文免费）**：用"假法律"说明双重差分标准误为什么会偏小。
- **Angrist & Pischke 2010**：识别为什么重要，见[领域概况](../README.md#延伸阅读)。

[^roth2023trending-e1]: Roth 等 2023，§1 Introduction。[证据](../../../../sources/notes/roth2023trending.md#e1)
[^roth2023trending-e2]: Roth 等 2023，§2.3。[证据](../../../../sources/notes/roth2023trending.md#e2)
[^roth2023trending-e3]: Roth 等 2023，§1 Introduction。[证据](../../../../sources/notes/roth2023trending.md#e3)
[^roth2023trending-e4]: Roth 等 2023，§3.5 Recommendations。[证据](../../../../sources/notes/roth2023trending.md#e4)
[^roth2023trending-e5]: Roth 等 2023，§1 Introduction。[证据](../../../../sources/notes/roth2023trending.md#e5)
[^roth2023trending-e6]: Roth 等 2023，§4.6 Recommendations。[证据](../../../../sources/notes/roth2023trending.md#e6)
[^roth2023trending-e7]: Roth 等 2023，§4.6 Recommendations。[证据](../../../../sources/notes/roth2023trending.md#e7)
[^roth2023trending-e8]: Roth 等 2023，Table 1。[证据](../../../../sources/notes/roth2023trending.md#e8)
[^roth2023trending-e9]: Roth 等 2023，§1 Introduction。[证据](../../../../sources/notes/roth2023trending.md#e9)
[^roth2023trending-e10]: Roth 等 2023，§5.2 Recommendations。[证据](../../../../sources/notes/roth2023trending.md#e10)
[^roth2023trending-e11]: Roth 等 2023，§7 Conclusion。[证据](../../../../sources/notes/roth2023trending.md#e11)
[^roth2023trending-e12]: Roth 等 2023，§4.3。[证据](../../../../sources/notes/roth2023trending.md#e12)
[^roth2023trending-e13]: Roth 等 2023，§1 Introduction。[证据](../../../../sources/notes/roth2023trending.md#e13)
[^lee2010rd-e1]: Lee & Lemieux 2010，§3.1。[证据](../../../../sources/notes/lee2010rd.md#e1)
[^lee2010rd-e2]: Lee & Lemieux 2010，§2.3。[证据](../../../../sources/notes/lee2010rd.md#e2)
[^lee2010rd-e3]: Lee & Lemieux 2010，§4.6。[证据](../../../../sources/notes/lee2010rd.md#e3)
[^lee2010rd-e4]: Lee & Lemieux 2010，§4.4.1。[证据](../../../../sources/notes/lee2010rd.md#e4)
[^lee2010rd-e5]: Lee & Lemieux 2010，§4.6。[证据](../../../../sources/notes/lee2010rd.md#e5)
[^lee2010rd-e6]: Lee & Lemieux 2010，§4.6。[证据](../../../../sources/notes/lee2010rd.md#e6)
[^lee2010rd-e7]: Lee & Lemieux 2010，§4.6。[证据](../../../../sources/notes/lee2010rd.md#e7)
[^lee2010rd-e8]: Lee & Lemieux 2010，§4.6。[证据](../../../../sources/notes/lee2010rd.md#e8)
[^lee2010rd-e9]: Lee & Lemieux 2010，§1 Introduction。[证据](../../../../sources/notes/lee2010rd.md#e9)
[^lee2010rd-e10]: Lee & Lemieux 2010，§1 Introduction。[证据](../../../../sources/notes/lee2010rd.md#e10)
[^lee2010rd-e11]: Lee & Lemieux 2010，§3.4.1。[证据](../../../../sources/notes/lee2010rd.md#e11)
[^imbens2008rd-e1]: Imbens & Lemieux 2008，§8。[证据](../../../../sources/notes/imbens2008rd.md#e1)
[^imbens2008rd-e2]: Imbens & Lemieux 2008，§7。[证据](../../../../sources/notes/imbens2008rd.md#e2)
[^imbens2008rd-e3]: Imbens & Lemieux 2008，§7.1。[证据](../../../../sources/notes/imbens2008rd.md#e3)
[^imbens2008rd-e4]: Imbens & Lemieux 2008，§7.2。[证据](../../../../sources/notes/imbens2008rd.md#e4)
[^imbens2008rd-e5]: Imbens & Lemieux 2008，§7.3。[证据](../../../../sources/notes/imbens2008rd.md#e5)
[^imbens2008rd-e6]: Imbens & Lemieux 2008，§7.5。[证据](../../../../sources/notes/imbens2008rd.md#e6)
[^imbens2008rd-e7]: Imbens & Lemieux 2008，§8。[证据](../../../../sources/notes/imbens2008rd.md#e7)
[^angrist2010credibility-e5]: Angrist & Pischke 2010，Better Research Design。[证据](../../../../sources/notes/angrist2010credibility.md#e5)
[^angrist2010credibility-e9]: Angrist & Pischke 2010，Whither Sensitivity Analysis?。[证据](../../../../sources/notes/angrist2010credibility.md#e9)
[^angrist2010credibility-e13]: Angrist & Pischke 2010，Whither Sensitivity Analysis?。[证据](../../../../sources/notes/angrist2010credibility.md#e13)
[^cunningham2026remix-e1]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e1)
[^cunningham2026remix-e2]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e2)
[^cunningham2026remix-e3]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章（转引 Bound、Jaeger 和 Baker 1995）。[证据](../../../../sources/notes/cunningham2026remix.md#e3)
[^cunningham2026remix-e4]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e4)
[^cunningham2026remix-e5]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e5)
[^cunningham2026remix-e6]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e6)
[^cunningham2026remix-e7]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e7)
[^cunningham2026remix-e8]: Cunningham，The Remix（在线第二版，仍在修订）第 7 章。[证据](../../../../sources/notes/cunningham2026remix.md#e8)
[^cunningham2026remix-e9]: Cunningham，The Remix（在线第二版，仍在修订）第 9 章。[证据](../../../../sources/notes/cunningham2026remix.md#e9)
[^cunningham2026remix-e10]: Cunningham，The Remix（在线第二版，仍在修订）第 9 章。[证据](../../../../sources/notes/cunningham2026remix.md#e10)
[^cunningham2026remix-e11]: Cunningham，The Remix（在线第二版，仍在修订）第 10 章。[证据](../../../../sources/notes/cunningham2026remix.md#e11)
[^cunningham2026remix-e12]: Cunningham，The Remix（在线第二版，仍在修订）第 10 章。[证据](../../../../sources/notes/cunningham2026remix.md#e12)
[^cunningham2026remix-e13]: Cunningham，The Remix（在线第二版，仍在修订）第 10 章。[证据](../../../../sources/notes/cunningham2026remix.md#e13)
[^cunningham2026remix-e14]: Cunningham，The Remix（在线第二版，仍在修订）第 10 章。[证据](../../../../sources/notes/cunningham2026remix.md#e14)
[^cunningham2026remix-e15]: Cunningham，The Remix（在线第二版，仍在修订）第 11 章。[证据](../../../../sources/notes/cunningham2026remix.md#e15)
[^cunningham2026remix-e16]: Cunningham，The Remix（在线第二版，仍在修订）第 11 章。[证据](../../../../sources/notes/cunningham2026remix.md#e16)
[^cunningham2026remix-e17]: Cunningham，The Remix（在线第二版，仍在修订）第 11 章。[证据](../../../../sources/notes/cunningham2026remix.md#e17)
[^cunningham2026remix-e18]: Cunningham，The Remix（在线第二版，仍在修订）第 11 章。[证据](../../../../sources/notes/cunningham2026remix.md#e18)
[^hernan2018cword-e5]: Hernán 2018，正文。[证据](../../../../sources/notes/hernan2018cword.md#e5)
[^hernan2018cword-e13]: Hernán 2018，正文。[证据](../../../../sources/notes/hernan2018cword.md#e13)
[^brodeur2016star-e2]: Brodeur 等 2016（2013 年讨论稿版），摘要。[证据](../../../../sources/notes/brodeur2016star.md#e2)
[^brodeur2016star-e3]: Brodeur 等 2016（2013 年讨论稿版），摘要。[证据](../../../../sources/notes/brodeur2016star.md#e3)
[^brodeur2016star-e5]: Brodeur 等 2016（2013 年讨论稿版），§1。[证据](../../../../sources/notes/brodeur2016star.md#e5)
[^cameron2015practitioner-e1]: Cameron & Miller 2015，摘要。[证据](../../../../sources/notes/cameron2015practitioner.md#e1)
[^cameron2015practitioner-e2]: Cameron & Miller 2015，§I。[证据](../../../../sources/notes/cameron2015practitioner.md#e2)
[^cameron2015practitioner-e3]: Cameron & Miller 2015，§I。[证据](../../../../sources/notes/cameron2015practitioner.md#e3)
[^cameron2015practitioner-e4]: Cameron & Miller 2015，§I。[证据](../../../../sources/notes/cameron2015practitioner.md#e4)
[^cameron2015practitioner-e5]: Cameron & Miller 2015，§I。[证据](../../../../sources/notes/cameron2015practitioner.md#e5)
[^bertrand2004trust-e1]: Bertrand, Duflo & Mullainathan 2004（2002 年工作论文版），摘要。[证据](../../../../sources/notes/bertrand2004trust.md#e1)
[^bertrand2004trust-e2]: Bertrand, Duflo & Mullainathan 2004（2002 年工作论文版），摘要。[证据](../../../../sources/notes/bertrand2004trust.md#e2)
