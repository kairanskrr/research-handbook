# 系统综述与元分析（健康领域）

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲健康领域里回答"某项干预效果如何"的系统综述，以及元分析（meta-analysis，医学文献里也叫"荟萃分析"）：用统计方法把多项研究的结果合并成一个总的估计。检索、筛选、提取数据、流程图这些各学科共通的步骤，计算机篇的[综述研究](../../../06_methods/review_study.md#2-系统综述怎么做)已经讲过，本文不重复，只讲健康领域特有的部分：方案登记、偏倚风险评价、效应指标和模型、异质性、小研究效应、证据确定性评级和报告。健康科学的整体背景见[领域概况](../README.md)。

**本文主要依据谁的说法。** 本文资料以 Cochrane 手册为主。它的全称是 Cochrane Handbook for Systematic Reviews of Interventions（本文读的是 6.5 版，2024 年），是 Cochrane 组织为撰写 Cochrane 综述的作者编写的方法手册[^higgins2024cochrane-e70]，讲的是干预效果的综述。下文凡出自它的"应该""不要"，都是这本手册的建议；手册标为"强制"的条目，是对 Cochrane 综述作者的要求。不投 Cochrane 的综述，以导师或目标期刊的要求为准 `[本项目分析]`。诊断准确性、预后等其他类型综述的专门方法，本文资料未涉及，同样以导师或目标期刊要求为准。

**读完本文，你应该能：** 判断自己的问题该不该做系统综述、要不要做元分析；在开始筛选之前写好方案并登记；用 RoB 2 和 ROBINS-I 两个工具评价纳入研究的偏倚风险；选对效应指标和模型，正确解读 I² 和漏斗图；用 GRADE 方法给每个结局的证据定级，并按 PRISMA 2020 报告。

---

## 1. 这是什么研究，什么时候用

**系统综述**针对一个界定清楚的问题，用系统、明确的方法查找、筛选、评价相关研究，并收集和分析其数据；可以用、也可以不用统计方法[^moher2009prisma-e1]。**元分析**是在系统综述中用统计方法整合纳入研究的结果[^moher2009prisma-e2]。所以元分析是系统综述里的一个可选步骤，不是另一种综述。

| | 系统综述，不做元分析 | 系统综述 + 元分析 |
|---|---|---|
| 产出 | 结构化的表格和文字综合 `[本项目分析]` | 每个元分析的合并估计、置信区间和异质性指标[^page2021prisma-e13] |
| 前提 | 方案、全面检索、偏倚风险评价 `[本项目分析]` | 同左，另外要求研究足够相似、合并后的答案有临床意义[^higgins2024cochrane-e15] |
| 好处 | 适用面广 `[本项目分析]` | 提高精确度，回答单个研究没问过的问题，平息相互矛盾的结论[^higgins2024cochrane-e13] |
| 风险 | 容易退化成逐篇罗列 `[本项目分析]` | 不仔细考虑设计、偏倚、研究间差异和报告偏倚时，可能严重误导[^higgins2024cochrane-e13] |

**什么时候做系统综述：** 先用 PICO 框架把问题说清楚：人群（Population）、干预（Intervention）、对照（Comparison）、结局（Outcome）[^higgins2024cochrane-e5]；再估计工作量。这两点和"开始新研究前先做综述"的建议，[领域概况](../README.md#系统综述cochrane-手册)已讲过。还要注意：按 PROSPERO（下文第 1 步介绍的登记平台）2023 年存档页面的规定，它不登记少于两人做的综述[^crd2023prospero-e7]，也不登记培训课程作业式的"迷你"综述[^crd2023prospero-e9]。一个人做的课程练习多半登记不了；能不能当作正式系统综述投稿，先问导师或目标期刊 `[本项目分析]`。

**什么时候不做元分析：** 系统综述不一定要有元分析[^higgins2024cochrane-e16]。Cochrane 手册列出的情况有：没有研究或只有一项研究，无法合并[^higgins2024cochrane-e19]；结局或效应估计报告不全，或各研究用的效应指标不同；证据本身有偏倚[^higgins2024cochrane-e17]；人群、干预、对照、结局不够相似，合并后得不到有临床意义的答案，例如各研究的对照组形式不同[^higgins2024cochrane-e15]；结果差异很大，尤其效应方向不一致，这时报一个平均值可能误导[^higgins2024cochrane-e16]。但"差异大、异质性高"本身不一定是放弃的理由。手册认为这时仍应考虑元分析，做得恰当、解释得当，它可能给出重要信息[^higgins2024cochrane-e17]。不做元分析时，也不要按"显著的几篇、不显著的几篇"来计票，手册称这种方法不可接受[^higgins2024cochrane-e18]。

**纳入哪些设计：** 在 GRADE 评级里，随机试验的证据从"高"起评，非随机研究从"低"起评（见第 7 步）[^higgins2024cochrane-e66]；但有些证据，尤其是关于干预危害的，常常要来自非随机研究[^higgins2024cochrane-e8]。观察性研究的混杂、测量误差、选择偏倚见领域概况的[观察性研究的三个坑](../README.md#观察性研究的三个坑)。合并高偏倚风险观察性研究的元分析，不能和合并低偏倚风险随机试验的元分析等同看待[^murad2016new-e5]，详见临床医学篇的[证据金字塔](../../clinical-medicine/README.md#证据金字塔有用但别机械套用)。

---

## 2. 怎么做

下面八步按时间顺序排。第 1 步之后的检索、筛选、提取，照计算机篇[综述研究的执行阶段](../../../06_methods/review_study.md#第二阶段执行)做；健康领域的检索还要查试验登记库，见第 6 步。

### 第 1 步：写方案，在 PROSPERO 登记

PROSPERO（International prospective register of systematic reviews，国际前瞻性系统综述登记平台）由英国约克大学评价与传播中心建设和管理，英国国家卫生研究院资助[^crd2023prospero-e2]；收录有健康相关结局的系统综述[^crd2023prospero-e3]。PROSPERO 说，登记是为了避免无计划的重复，并让别人能对照"计划做的"和"最后报告的"，从而减少偏倚[^crd2023prospero-e1]。

**怎么做：** 下面的规则都来自它 2023 年 1 月的存档页面，之后可能已经改变；本文读不到改版后的现行页面，登记时以官网现行规定为准 `[本项目分析]`。
- 先写完整方案，再登记：登记前要有完整方案，必须在开始提取数据之前提交[^crd2023prospero-e4]；最好在开始筛选之前登记[^crd2023prospero-e5]。也不要登记得太早：登记了却不做，可能损害团队声誉[^crd2023prospero-e10]。
- 它不收范围综述、只是用了系统检索的文献综述、以运动成绩为结局的综述等[^crd2023prospero-e6]；结果不会公开的综述（例如已知不会公开的硕士论文）也不收[^crd2023prospero-e8]。Cochrane 综述的方案不要再单独登记，以免重复[^crd2023prospero-e11]。
- 方案里事先写好主要结局、效应指标、模型、亚组分析和敏感性分析 `[本项目分析，依据第 3–5 步的资料]`。纳入非随机研究时，Cochrane 手册要求在方案里写明重要的混杂因素和需要关注的合并干预（同时接受的其他治疗）[^higgins2024cochrane-e28]。

**容易错在哪里：** 以为改了方案就是违规。做综述过程中修改方案很正常，报告并解释即可；但没有公开的方案，别人就无法判断修改是否恰当[^moher2009prisma-e3]。PRISMA 2020 要求报告登记号、方案在哪里能看到，以及对登记内容的任何修改和理由[^page2021prisma-e6][^page2021prisma-e7]。

### 第 2 步：逐个结果评价偏倚风险

**怎么做：** 不给研究打"质量总分"，而是评**偏倚风险**：结果高估或低估真实干预效果的风险[^higgins2024cochrane-e21]。**为什么：** 早期的质量量表把多项特征加成一个分数；后来发现，换一种量表就会明显改变对元分析结果的解读，这种做法因此受到质疑[^higgins2024cochrane-e20]。

**随机试验用 RoB 2**（Cochrane 随机试验偏倚风险工具第 2 版）：

- 评的是试验里的**某一个结果**，不是整篇试验[^higgins2024cochrane-e22]。不要按"可能评出什么"来挑要评的结果[^higgins2024cochrane-e26]。
- 五个领域：随机化过程、偏离预定干预、结局数据缺失、结局测量、报告结果的选择[^higgins2024cochrane-e23]。每个领域判"低风险""有些担忧"或"高风险"，整体判断取各领域中最差的那个[^higgins2024cochrane-e24]；每个判断都写下理由[^higgins2024cochrane-e25]。
- 两种效果回答的问题不同："被分配到干预组"的效果适合回答卫生政策问题，"按方案坚持干预"的效果适合回答个体患者的决策[^higgins2024cochrane-e27]。评之前先想清楚自己关心哪一种 `[本项目分析]`。

**非随机研究用 ROBINS-I**（非随机干预研究偏倚风险工具）：先描述一个"目标试验"：在同一人群中比较同样干预、没有偏倚隐患的假想随机试验，再拿实际研究和它对照[^higgins2024cochrane-e29]。判断分四级：低、中、严重、极严重[^higgins2024cochrane-e30]。

**容易错在哪里：** 把 ROBINS-I 当成和 RoB 2 一样省事。它比评随机试验更费事，既要懂方法，也要懂专业内容[^higgins2024cochrane-e31]。

### 第 3 步：选效应指标

**怎么做：** 效应指标就是用什么数来表示"干预比对照好多少" `[本项目分析]`。
- **二分类结局**（如发病或不发病）：手册一般建议用风险比（risk ratio）或比值比（odds ratio）来合并；用风险比时要想清楚哪一类算"事件"[^higgins2024cochrane-e32]。很多元分析方法依靠大样本近似，事件罕见时不适用[^higgins2024cochrane-e71]。
- **连续结局**（如血压）：各研究用同一量表时用均数差（mean difference）；用不同量表时一般用标准化均数差（standardized mean difference）[^higgins2024cochrane-e36]。

**为什么要想清楚呈现方式：** 比值比最难理解，已发表文献里有很多把元分析的比值比误读成风险比的例子[^higgins2024cochrane-e33]。手册认为，常常可以用一种指标合并，再换算成更好懂的指标来呈现[^higgins2024cochrane-e34]。

**容易错在哪里：** 看了数据再挑"结果最一致"的指标，可能人为夸大合并结果的精确度[^higgins2024cochrane-e35]。所以指标要在方案里事先定好 `[本项目分析]`，报告时写明每个结局用了什么指标[^page2021prisma-e8]。

### 第 4 步：选模型，固定效应还是随机效应

元分析的合并结果是各研究效应的加权平均；常用方法里，标准误小（结果更精确）的大研究权重更大[^higgins2024cochrane-e37]。**固定效应模型**假定每项研究的真实效应都相同；**随机效应模型**不作这个假定，而假定各研究的真实效应服从某个分布（通常是正态分布）[^higgins2024cochrane-e38]。**为什么要分清：** 两者的结果含义不同。固定效应的置信区间没有反映异质性；随机效应的结果指的是各研究效应的平均值[^higgins2024cochrane-e73]。

> **不同的看法：用哪个模型？**
> - **主张随机效应：** 一般认为各研究的干预效应完全相同不太可能（除非干预完全无效），所以很多人主张用随机效应[^higgins2024cochrane-e40]。
> - **主张固定效应：** 也有人认为，有异质性时固定效应的结果仍可解释，而且它的假设比随机效应少[^higgins2024cochrane-e41]。
>
> Cochrane 手册说这个问题争论很多，它不给统一建议[^higgins2024cochrane-e39]。它提醒：如果漏斗图不对称（效应大小和研究规模有关），随机效应的结果会被推向小研究的结论[^higgins2024cochrane-e43]。它提出一个务实的做法：事先计划两种都做，没有漏斗图不对称的迹象时报告随机效应的结果[^higgins2024cochrane-e44]。它还明确说：**绝不要根据异质性检验的结果来选模型**[^higgins2024cochrane-e42]。

### 第 5 步：看异质性，正确解读 I²

**异质性**指各研究的效应差异，超出了单靠机遇能解释的程度[^higgins2024cochrane-e45]。必须考虑研究间的差异[^higgins2024cochrane-e72]，否则合并结果的含义会被误读（见第 4 步）[^higgins2024cochrane-e73]。

**怎么看：**
- **异质性检验**：显著可能提示有问题；不显著不能当作"没有异质性"的证据[^higgins2024cochrane-e46]。
- **I²**：效应估计的变异中，有多大比例来自异质性而不是抽样误差[^higgins2024cochrane-e47]。Cochrane 手册给了一个粗略参考：0–40% 可能不重要，30–60% 可能中等，50–90% 可能较大，75–100% 很大；同时提醒，用阈值解读 I² 可能误导[^higgins2024cochrane-e48]。研究少时 I² 很不确定，不要用简单阈值来诊断异质性[^higgins2024cochrane-e49]。
- **随机效应的置信区间不表示异质性**，它说的是平均效应位置的不确定性[^higgins2024cochrane-e50]。研究数量合理（例如五项以上）且漏斗图没有明显不对称时，手册鼓励报告**预测区间**[^higgins2024cochrane-e51]，用它表示各研究真实效应可能落在的范围 `[本项目分析]`。

**发现异质性以后：**
1. **先查数据。** 异质性异常大，可能是提取或录入错了，例如把标准误当成标准差录入[^higgins2024cochrane-e52]。
2. **再找原因。** 常用的是亚组分析，即把研究按某个特征分组分别看 `[本项目分析]`。只有看结果之前事先规定的分析才能得出比较可靠的结论；看到异质性后才想出来的分析，最多只能提出假设[^higgins2024cochrane-e53]。研究很少时，找原因的价值存疑[^higgins2024cochrane-e75]；手册指出，大多数 Cochrane 综述的研究数量都不够可靠地查明原因[^higgins2024cochrane-e72]。
3. **不要剔除"不合群"的研究。** 按结果剔除研究可能引入偏倚；可以在敏感性分析里分别做包含和不包含它的分析[^higgins2024cochrane-e54]。
4. **换成随机效应不等于解决了问题**，它不能代替调查原因[^higgins2024cochrane-e55]。**做敏感性分析**，检查换一种可能影响结果的决定，结论是否还站得住[^higgins2024cochrane-e56]。

### 第 6 步：评估小研究效应和发表偏倚

**为什么：** "显著有效"的结果比"不显著"的更容易公开、公开得更快、被更多引用，因而更容易被综述找到[^higgins2024cochrane-e57]。

**怎么做：**
- **检索时就要防。** 除了多个文献数据库，可能还要查试验登记库，并联系厂商、监管机构、研究作者或资助方[^higgins2024cochrane-e58]。
- **逐项核查**已找到的研究有没有选择性地不报告或少报告结果；手册认为这可能是最有价值的一步[^higgins2024cochrane-e63]。
- **漏斗图**是把每项研究的效应和研究规模画在一起的散点图 `[本项目分析]`。它展示的是"小研究效应"，即小研究估计的效应和大研究不同的倾向[^higgins2024cochrane-e59]。担心小研究效应时，比较固定效应和随机效应的估计；两者相近，说明小研究效应对结果影响不大[^higgins2024cochrane-e62]。

**容易错在哪里：**
- 把漏斗图不对称当成发表偏倚的证据。不对称不能用来诊断未报告偏倚[^higgins2024cochrane-e61]。
- 研究很少也做漏斗图不对称检验。手册的经验法则是元分析至少有 10 项研究才做，否则检验效能太低；它引用的一项调查显示，2020 年被收录的 300 篇系统综述的随机样本中，只有 28% 含有至少 10 项研究的元分析[^higgins2024cochrane-e60]。

### 第 7 步：用 GRADE 给每个结局的证据定级

GRADE（Grading of Recommendations Assessment, Development and Evaluation，推荐分级的评估、制订与评价）是给证据可信程度定级的方法，Cochrane 手册第 14 章用它评定证据确定性[^higgins2024cochrane-e64]。它不是设计越"高级"证据就越强，而是逐个结局看证据有多可信，这和[临床医学篇](../../clinical-medicine/README.md#证据金字塔有用但别机械套用)讲的证据金字塔思路不同 `[本项目分析]`。

**怎么做：**
- **按结局评，不按研究评。** 每个结局的证据分四级：高、中、低、极低[^higgins2024cochrane-e64]。按 2013 年版 GRADE 手册的说法，"高"指很有把握真实效应接近估计值；"极低"指真实效应很可能与估计值差别很大[^schunemann2013grade-e1]。
- **起点看设计。** 随机试验从"高"起评，非随机研究从"低"起评[^higgins2024cochrane-e66]。
- **五个降级理由**：偏倚风险、不一致性、间接性、不精确性、发表偏倚；非随机研究还可以根据另外三个方面上调[^higgins2024cochrane-e65]。即使用了 ROBINS-I，做得好的非随机研究一般也评为低确定性[^higgins2024cochrane-e74]。
- **每次升降级都写理由**[^higgins2024cochrane-e68]，最好两人独立评定，再对降级达成共识[^higgins2024cochrane-e67]。结果汇总成"结果总结表"（Summary of findings table），每个重要结局一行，最多七个结局[^higgins2024cochrane-e69]。

**容易错在哪里：**
- 结局是主观指标、评估者又知道分组时，因为效应大就轻易上调。2013 年版 GRADE 手册提醒这时要谨慎[^schunemann2013grade-e4]。
- 把四个等级当成精确刻度。2013 年版 GRADE 手册说，分级本身难免有些武断[^schunemann2013grade-e3]。
- 被新旧术语弄糊涂。2013 年版 GRADE 手册用的是"证据质量"，PRISMA 2020 指出现在已转向评"证据确定性"[^page2021prisma-e15]。

### 第 8 步：按 PRISMA 2020 报告

PRISMA 2020 是系统综述的报告规范，它规范怎么报告，不指导怎么做[^page2021prisma-e16]；通用部分见计算机篇[综述研究的报告阶段](../../../06_methods/review_study.md#第三阶段报告)。Cochrane 手册要求 Cochrane 的方案和综述符合 PRISMA 2020 和它的方案版（PRISMA for Protocols）[^higgins2024cochrane-e70]。和元分析有关、容易漏的条目：

- 每个结局的效应指标（第 12 项）[^page2021prisma-e8]；模型、判断异质性的方法、软件（第 13d 项）[^page2021prisma-e9]；亚组分析、元回归、敏感性分析（第 13e、13f 项）[^page2021prisma-e10]
- 报告偏倚和证据确定性的评估方法（第 14、15 项）[^page2021prisma-e11]；每项研究的偏倚风险（第 18 项）[^page2021prisma-e12]；每个元分析的合并估计、置信区间和异质性指标（第 20b 项）[^page2021prisma-e13]
- 登记号、方案和修改（第 24 项）[^page2021prisma-e6][^page2021prisma-e7]；数据和代码是否公开（第 27 项）[^page2021prisma-e14]

---

## 3. 检查清单

每条后面注明出处："Cochrane 强制"是 Cochrane 手册对 Cochrane 综述的强制要求；"PRISMA"是 PRISMA 2020 的报告条目；"PROSPERO"是它 2023 年存档页面的规定。不投 Cochrane 时，以目标期刊要求为准 `[本项目分析]`。

**必须做到**
- [ ] 写好完整方案再登记；在 PROSPERO 登记的，开始提取数据之前提交（PROSPERO）[^crd2023prospero-e4]
- [ ] 报告登记号、方案在哪里、对方案的修改和理由（PRISMA）[^page2021prisma-e6][^page2021prisma-e7]
- [ ] 只在研究足够相似、合并有临床意义时做元分析（Cochrane 强制）[^higgins2024cochrane-e15]
- [ ] 研究少时不用简单阈值诊断异质性（Cochrane 强制）[^higgins2024cochrane-e49]；解释结果时讲清所用模型下异质性意味着什么（Cochrane 强制）[^higgins2024cochrane-e73]
- [ ] 每次升降证据确定性都写理由并记录（Cochrane 强制）[^higgins2024cochrane-e68]
- [ ] 报告每项研究的偏倚风险、每个元分析的合并估计、置信区间和异质性指标（PRISMA）[^page2021prisma-e12][^page2021prisma-e13]

**做到更好**
- [ ] 最好在开始筛选之前就登记（PROSPERO）[^crd2023prospero-e5]
- [ ] 用 RoB 2、ROBINS-I 这类分领域的工具评偏倚风险，每个判断写理由，不打质量总分[^higgins2024cochrane-e25][^higgins2024cochrane-e20]
- [ ] 事先计划固定效应和随机效应两种分析[^higgins2024cochrane-e44]；研究数量合理时报告预测区间[^higgins2024cochrane-e51]；用敏感性分析检验关键决定[^higgins2024cochrane-e56]
- [ ] 两人独立评定证据确定性（Cochrane 列为强制，原文用"最好"）[^higgins2024cochrane-e67]
- [ ] 查试验登记库，逐项核查选择性不报告[^higgins2024cochrane-e58][^higgins2024cochrane-e63]
- [ ] 公开数据提取表、提取的数据和分析代码（PRISMA 要求说明是否公开）[^page2021prisma-e14]

**这些情况可以不做，不算缺陷：** 研究太少或不够相似时，不做元分析[^higgins2024cochrane-e16][^higgins2024cochrane-e19]；元分析少于 10 项研究时，不做漏斗图不对称检验[^higgins2024cochrane-e60]；研究很少时，不硬找异质性的原因[^higgins2024cochrane-e75]。

**审稿时常见、但不成立的批评**（这些说法是否"常见"是本项目的判断 `[本项目分析]`；为什么不成立有资料依据）
- "I² 超过 50%，不能合并"：用固定阈值解读 I² 可能误导；异质性高本身不一定是放弃元分析的理由[^higgins2024cochrane-e48][^higgins2024cochrane-e17]
- "异质性检验不显著，应该用固定效应"：模型不能根据异质性检验来选[^higgins2024cochrane-e42]
- "方案改过，所以不可信"：修改可以报告并解释，本身不算不当[^moher2009prisma-e3]
- "没做元分析，不算系统综述"：系统综述不一定要有元分析[^higgins2024cochrane-e16]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 问题、纳入标准、偏倚评价还没做好，就先做统计合并 | 元分析结果可能非常误导[^higgins2024cochrane-e14] |
| 把高偏倚风险观察性研究的元分析当成强证据 | 不能和低偏倚风险随机试验的元分析等同看待[^murad2016new-e5] |
| 看数据挑效应指标；把比值比读成风险比 | 前者可能人为夸大精确度[^higgins2024cochrane-e35]；后者在已发表文献里很多[^higgins2024cochrane-e33] |
| 检验不显著就说"没有异质性"；把随机效应的置信区间当成研究间差异的大小 | 不显著不等于没有[^higgins2024cochrane-e46]；置信区间只描述平均效应位置的不确定性[^higgins2024cochrane-e50] |
| 事后找亚组再写进结论；剔除结果"不合群"的研究 | 事后分析最多只能提出假设[^higgins2024cochrane-e53]；剔除可能引入偏倚[^higgins2024cochrane-e54] |
| 研究很少也做漏斗图检验，并据此断言有无发表偏倚 | 检验效能低，不对称也不能诊断未报告偏倚[^higgins2024cochrane-e60][^higgins2024cochrane-e61] |

给研究打质量总分、按异质性检验结果选模型、按显著与否计票，见第 2 步、第 4 步和第 1 节。

---

## 5. 延伸阅读

- **Cochrane 手册**（6.5 版，官网免费在线）：第 10 章讲元分析，先读开头"Do not start here!"一节；第 8、25 章分别讲 RoB 2、ROBINS-I；第 13 章讲漏斗图；第 14 章讲 GRADE；第 12 章讲不做元分析时怎样综合。
- **PRISMA 2020**：完整清单和流程图模板。**GRADE 手册**（2013 年 10 月版，免费在线）：升降级理由的解释，它用"证据质量"一词。**PROSPERO 官网**：本文只读到 2023 年的存档页面，登记前读现行须知。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^moher2009prisma-e1]: Moher 等人 2009，Terminology。[证据](../../../../sources/notes/moher2009prisma.md#e1)
[^moher2009prisma-e2]: Moher 等人 2009，Terminology。[证据](../../../../sources/notes/moher2009prisma.md#e2)
[^moher2009prisma-e3]: Moher 等人 2009，Box 1。[证据](../../../../sources/notes/moher2009prisma.md#e3)
[^higgins2024cochrane-e13]: Cochrane 手册 2024，第 10 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e13)
[^higgins2024cochrane-e14]: Cochrane 手册 2024，第 10 章 §10.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e14)
[^higgins2024cochrane-e15]: Cochrane 手册 2024，第 10 章 §10.10.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e15)
[^higgins2024cochrane-e16]: Cochrane 手册 2024，第 10 章 §10.10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e16)
[^higgins2024cochrane-e17]: Cochrane 手册 2024，第 12 章 §12.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e17)
[^higgins2024cochrane-e18]: Cochrane 手册 2024，第 12 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e18)
[^higgins2024cochrane-e19]: Cochrane 手册 2024，第 12 章表 12.1.a。[证据](../../../../sources/notes/higgins2024cochrane.md#e19)
[^higgins2024cochrane-e20]: Cochrane 手册 2024，第 7 章 §7.1.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e20)
[^higgins2024cochrane-e21]: Cochrane 手册 2024，第 7 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e21)
[^higgins2024cochrane-e22]: Cochrane 手册 2024，第 8 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e22)
[^higgins2024cochrane-e23]: Cochrane 手册 2024，第 8 章 §8.2.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e23)
[^higgins2024cochrane-e24]: Cochrane 手册 2024，第 8 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e24)
[^higgins2024cochrane-e25]: Cochrane 手册 2024，第 8 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e25)
[^higgins2024cochrane-e26]: Cochrane 手册 2024，第 8 章 §8.2.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e26)
[^higgins2024cochrane-e27]: Cochrane 手册 2024，第 8 章 §8.2.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e27)
[^higgins2024cochrane-e28]: Cochrane 手册 2024，第 25 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e28)
[^higgins2024cochrane-e29]: Cochrane 手册 2024，第 25 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e29)
[^higgins2024cochrane-e30]: Cochrane 手册 2024，第 25 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e30)
[^higgins2024cochrane-e31]: Cochrane 手册 2024，第 25 章 §25.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e31)
[^higgins2024cochrane-e32]: Cochrane 手册 2024，第 10 章 §10.4.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e32)
[^higgins2024cochrane-e33]: Cochrane 手册 2024，第 10 章 §10.4.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e33)
[^higgins2024cochrane-e34]: Cochrane 手册 2024，第 10 章 §10.4.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e34)
[^higgins2024cochrane-e35]: Cochrane 手册 2024，第 10 章 §10.4.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e35)
[^higgins2024cochrane-e36]: Cochrane 手册 2024，第 10 章 §10.5.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e36)
[^higgins2024cochrane-e37]: Cochrane 手册 2024，第 10 章 §10.2.1、§10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e37)
[^higgins2024cochrane-e38]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e38)
[^higgins2024cochrane-e39]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e39)
[^higgins2024cochrane-e40]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e40)
[^higgins2024cochrane-e41]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e41)
[^higgins2024cochrane-e42]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e42)
[^higgins2024cochrane-e43]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e43)
[^higgins2024cochrane-e44]: Cochrane 手册 2024，第 10 章 §10.10.4.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e44)
[^higgins2024cochrane-e45]: Cochrane 手册 2024，第 10 章 §10.10.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e45)
[^higgins2024cochrane-e46]: Cochrane 手册 2024，第 10 章 §10.10.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e46)
[^higgins2024cochrane-e47]: Cochrane 手册 2024，第 10 章 §10.10.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e47)
[^higgins2024cochrane-e48]: Cochrane 手册 2024，第 10 章 §10.10.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e48)
[^higgins2024cochrane-e49]: Cochrane 手册 2024，第 10 章 §10.10.2（强制要求 C63）。[证据](../../../../sources/notes/higgins2024cochrane.md#e49)
[^higgins2024cochrane-e50]: Cochrane 手册 2024，第 10 章 §10.10.4.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e50)
[^higgins2024cochrane-e51]: Cochrane 手册 2024，第 10 章 §10.10.4.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e51)
[^higgins2024cochrane-e52]: Cochrane 手册 2024，第 10 章 §10.10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e52)
[^higgins2024cochrane-e53]: Cochrane 手册 2024，第 10 章 §10.10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e53)
[^higgins2024cochrane-e54]: Cochrane 手册 2024，第 10 章 §10.10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e54)
[^higgins2024cochrane-e55]: Cochrane 手册 2024，第 10 章 §10.10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e55)
[^higgins2024cochrane-e56]: Cochrane 手册 2024，第 10 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e56)
[^higgins2024cochrane-e57]: Cochrane 手册 2024，第 13 章 §13.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e57)
[^higgins2024cochrane-e58]: Cochrane 手册 2024，第 13 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e58)
[^higgins2024cochrane-e59]: Cochrane 手册 2024，第 13 章 §13.3.4.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e59)
[^higgins2024cochrane-e60]: Cochrane 手册 2024，第 13 章 §13.3.4.4。[证据](../../../../sources/notes/higgins2024cochrane.md#e60)
[^higgins2024cochrane-e61]: Cochrane 手册 2024，第 13 章 §13.3.4.4。[证据](../../../../sources/notes/higgins2024cochrane.md#e61)
[^higgins2024cochrane-e62]: Cochrane 手册 2024，第 13 章 §13.3.4.6。[证据](../../../../sources/notes/higgins2024cochrane.md#e62)
[^higgins2024cochrane-e63]: Cochrane 手册 2024，第 13 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e63)
[^higgins2024cochrane-e64]: Cochrane 手册 2024，第 14 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e64)
[^higgins2024cochrane-e65]: Cochrane 手册 2024，第 14 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e65)
[^higgins2024cochrane-e66]: Cochrane 手册 2024，第 14 章 §14.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e66)
[^higgins2024cochrane-e67]: Cochrane 手册 2024，第 14 章 §14.2（强制要求 C74）。[证据](../../../../sources/notes/higgins2024cochrane.md#e67)
[^higgins2024cochrane-e68]: Cochrane 手册 2024，第 14 章 §14.2（强制要求 C75）。[证据](../../../../sources/notes/higgins2024cochrane.md#e68)
[^higgins2024cochrane-e69]: Cochrane 手册 2024，第 14 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e69)
[^higgins2024cochrane-e70]: Cochrane 手册 2024，第 III 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e70)
[^higgins2024cochrane-e71]: Cochrane 手册 2024，第 10 章 §10.4.4。[证据](../../../../sources/notes/higgins2024cochrane.md#e71)
[^higgins2024cochrane-e72]: Cochrane 手册 2024，第 10 章要点。[证据](../../../../sources/notes/higgins2024cochrane.md#e72)
[^higgins2024cochrane-e73]: Cochrane 手册 2024，第 10 章 §10.10.3（强制要求 C69）。[证据](../../../../sources/notes/higgins2024cochrane.md#e73)
[^higgins2024cochrane-e74]: Cochrane 手册 2024，第 14 章 §14.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e74)
[^higgins2024cochrane-e5]: Cochrane 手册 2024，第 1 章 §1.2。[证据](../../../../sources/notes/higgins2024cochrane.md#e5)
[^higgins2024cochrane-e8]: Cochrane 手册 2024，第 24 章 §24.1。[证据](../../../../sources/notes/higgins2024cochrane.md#e8)
[^higgins2024cochrane-e75]: Cochrane 手册 2024，第 10 章 §10.10.3。[证据](../../../../sources/notes/higgins2024cochrane.md#e75)
[^crd2023prospero-e1]: PROSPERO 网站 2023 年存档，Registering a review。[证据](../../../../sources/notes/crd2023prospero.md#e1)
[^crd2023prospero-e2]: PROSPERO 网站 2023 年存档，Registering a review。[证据](../../../../sources/notes/crd2023prospero.md#e2)
[^crd2023prospero-e3]: PROSPERO 网站 2023 年存档，Inclusion criteria。[证据](../../../../sources/notes/crd2023prospero.md#e3)
[^crd2023prospero-e4]: PROSPERO 网站 2023 年存档，Requirements for registration。[证据](../../../../sources/notes/crd2023prospero.md#e4)
[^crd2023prospero-e5]: PROSPERO 网站 2023 年存档，Integrity of data and prospective registration。[证据](../../../../sources/notes/crd2023prospero.md#e5)
[^crd2023prospero-e6]: PROSPERO 网站 2023 年存档，PROSPERO does not accept。[证据](../../../../sources/notes/crd2023prospero.md#e6)
[^crd2023prospero-e7]: PROSPERO 网站 2023 年存档，登记资格自查页。[证据](../../../../sources/notes/crd2023prospero.md#e7)
[^crd2023prospero-e8]: PROSPERO 网站 2023 年存档，登记资格自查页。[证据](../../../../sources/notes/crd2023prospero.md#e8)
[^crd2023prospero-e9]: PROSPERO 网站 2023 年存档，首页通知。[证据](../../../../sources/notes/crd2023prospero.md#e9)
[^crd2023prospero-e10]: PROSPERO 网站 2023 年存档，When to register your review。[证据](../../../../sources/notes/crd2023prospero.md#e10)
[^crd2023prospero-e11]: PROSPERO 网站 2023 年存档，Other considerations。[证据](../../../../sources/notes/crd2023prospero.md#e11)
[^page2021prisma-e6]: PRISMA 2020（Page 等人 2021），第 24a 项。[证据](../../../../sources/notes/page2021prisma.md#e6)
[^page2021prisma-e7]: PRISMA 2020，第 24b、24c 项。[证据](../../../../sources/notes/page2021prisma.md#e7)
[^page2021prisma-e8]: PRISMA 2020，第 12 项。[证据](../../../../sources/notes/page2021prisma.md#e8)
[^page2021prisma-e9]: PRISMA 2020，第 13d 项。[证据](../../../../sources/notes/page2021prisma.md#e9)
[^page2021prisma-e10]: PRISMA 2020，第 13e、13f 项。[证据](../../../../sources/notes/page2021prisma.md#e10)
[^page2021prisma-e11]: PRISMA 2020，第 14、15 项。[证据](../../../../sources/notes/page2021prisma.md#e11)
[^page2021prisma-e12]: PRISMA 2020，第 18 项。[证据](../../../../sources/notes/page2021prisma.md#e12)
[^page2021prisma-e13]: PRISMA 2020，第 20b 项。[证据](../../../../sources/notes/page2021prisma.md#e13)
[^page2021prisma-e14]: PRISMA 2020，第 27 项。[证据](../../../../sources/notes/page2021prisma.md#e14)
[^page2021prisma-e15]: PRISMA 2020，引言。[证据](../../../../sources/notes/page2021prisma.md#e15)
[^page2021prisma-e16]: PRISMA 2020，引言。[证据](../../../../sources/notes/page2021prisma.md#e16)
[^murad2016new-e5]: Murad 等人 2016，Rationale for modification 2。[证据](../../../../sources/notes/murad2016new.md#e5)
[^schunemann2013grade-e1]: GRADE 手册 2013，表 5.1。[证据](../../../../sources/notes/schunemann2013grade.md#e1)
[^schunemann2013grade-e3]: GRADE 手册 2013，§5。[证据](../../../../sources/notes/schunemann2013grade.md#e3)
[^schunemann2013grade-e4]: GRADE 手册 2013，§5.3.1。[证据](../../../../sources/notes/schunemann2013grade.md#e4)
