# 复现研究：有计划地重做已发表的研究，检验结论是否成立

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**复现研究**（replication study）：有意、有计划地重做一项已发表的研究（称为**原研究**），看它的结果能否再次得到[^ralph2020empirical-e208]。重做时可以用原作者的**制品**（artifact：论文配套的代码、数据和脚本），也可以自己重新实现、换一批数据或换一个情境。

本文不讲怎样让**自己的**研究容易被别人复现，那部分见[工程研究](engineering_research.md)、[基准评测](benchmarking.md)中关于公开制品的步骤，以及通用篇的[整理科研材料](../../../general/2_during/03_organizing_materials.md)；ACM 制品徽章见[计算机领域概况：制品评估与徽章](../README.md#制品评估与徽章)。

**读完本文，你应该能：**

- 分清可重复、可复现、可重现，并在论文里写明自己用哪一套定义；
- 判断自己要做哪一类复现，选出值得检验的主张；
- 按步骤完成一次复现：摸清原研究、联系原作者、记录偏差、事先定好成功标准，并如实报告结果，包括没能复现的结果；
- 用文末的检查清单检查自己的复现论文。

---

## 1. 这是什么研究，什么时候用

SIGSOFT（美国计算机协会软件工程分会）的实证研究标准给复现研究定了两个条件：复现是**有意、有计划的**，不是碰巧和别人的研究重叠；原研究是**明确指出的另一篇已发表论文**[^ralph2020empirical-e209]。

它的价值在于让研究者能证实、推翻或深化先前研究的结论[^carver2010towards-e1]。ACM 的立场是：实验结果只有能被独立复现，才算真正确立[^acm2020artifact-e9]。

### 先把术语说清楚

和"复现"有关的几个英文词，不同资料的用法不一样，有时正好相反。计算机研究者都同意实证结果应当可复现，但"可复现"到底指什么，既没有明确定义，也没有共识[^gundersen2018state-e1]。下面先介绍 ACM 的三分法，它按"是不是同一团队""是不是同一实验设置"来分：

| 术语 | 谁来做 | 实验设置 | 对计算实验来说 |
|---|---|---|---|
| 可重复（repeatability） | 同一团队 | 相同 | 研究者能可靠地重复自己的计算[^acm2020artifact-e16] |
| 可复现（reproducibility） | 不同团队 | 相同 | 独立团队用原作者的制品得到相同结果[^acm2020artifact-e17] |
| 可重现（replicability） | 不同团队 | 不同 | 独立团队用自己独立开发的制品得到相同结果[^acm2020artifact-e18] |

ACM "结果已验证"徽章的两级"已复现""已重现"，就按是否用了原作者的制品来区分[^acm2020artifact-e5]，徽章的完整说明见[计算机领域概况：制品评估与徽章](../README.md#制品评估与徽章)。

读文献时注意：

- **ACM 自己对调过两个词。** ACM 采纳美国国家信息标准组织（NISO）的建议，把 reproducibility 和 replication 的含义对调，以和更广的科学界一致[^acm2020artifact-e19]。读较早的文献，要先看清它用的是哪一套 `[本项目分析]`。
- **SIGSOFT 按数据来分。** reproduce 指在原数据上重做原分析；replicate 指收集新数据，再做原分析[^ralph2020empirical-e210]。
- **机器学习常见四分法。** Pineau 等人（NeurIPS 2019 可复现性计划的组织者）把研究分为：可复现（同数据、同分析工具）、可重现（不同数据）、稳健（同数据、不同分析，例如重新实现代码）、可推广（数据和分析工具都不同，结论仍相同）[^pineau2021improving-e1]。

**怎么办**：论文里写明采用哪一套定义，并直接描述你做了什么：谁做的、用没用原代码、用没用原数据。不要只丢一个术语 `[本项目分析]`。本文用"复现研究"统称所有有计划的重做，需要细分时用上表的三个词。

### 复现研究的分类

SIGSOFT 标准要求从三个角度写明你做的是哪一类复现[^ralph2020empirical-e215]：

| 角度 | 类别 |
|---|---|
| 方法有多像 | **精确复现**：问题、方法、情境都相同；**方法复现**：问题和方法相同，情境不同；**概念复现**：问题相同，方法和情境都不同[^ralph2020empirical-e211] |
| 覆盖多少 | **部分复现**：只回答一部分原问题；**完整复现**：回答全部原问题；**扩展复现**：全部原问题之外再加新问题[^ralph2020empirical-e212] |
| 谁来做 | **内部复现**：同一团队；**外部复现**：不同团队；**混合复现**：两个团队有重叠[^ralph2020empirical-e213] |

在以代码和数据为主的方向（如人工智能、机器学习），Gundersen & Kjensmo 按复现时换掉了什么，分出三个程度[^gundersen2018state-e2]：**R1 实验复现**（同一份实现，同一份数据）、**R2 数据复现**（另写一份实现，同一份数据）、**R3 方法复现**（另写一份实现，换一份数据）。从 R1 到 R3，复现成功所说明的结果越来越具有一般性[^gundersen2018state-e3]。R1 只说明"这份代码在这份数据上确实给出这个数"，R3 才接近说明"这个方法本身有效" `[本项目分析]`。

### 和相近工作的区别 `[本项目分析]`

| | 复现研究 | 复现基线 | 制品评估 |
|---|---|---|---|
| 目的 | 检验原研究的结论是否成立 | 把别人的方法跑起来，当作比较对象（见[工程研究](engineering_research.md)、[基准评测](benchmarking.md)） | 检查论文附带的制品能否运行、是否与论文一致（见[计算机领域概况](../README.md#制品评估与徽章)） |
| 成果 | 一篇独立的论文 | 你自己论文的一部分 | 一枚徽章 |

**什么时候值得做** `[本项目分析]`：一个结论被广泛引用、很多工作建立在它之上，却还没有人独立检验过；或者你怀疑它依赖某个特定条件，例如特定的数据、评测程序或参数设置（例子见第一步）。如果只是要在别人的结果上继续做，先在自己的条件下把原结果做出来即可，不必写成复现论文，见通用篇[用清楚、令人信服的证据支撑结果](../../../general/1_before/01_what_is_good_research.md#4-用清楚令人信服的证据支撑结果)中的"先复现，再改条件"。

---

## 2. 怎么做

### 第一步：选定要检验的主张，写清动机

**怎么做：**

- **写下为什么做这次复现。** SIGSOFT 把动机列为必要项，例如验证结果，或通过更换参与者、制品来扩大结果的适用范围[^ralph2020empirical-e214]。
- **列出要检验的具体主张**，而不是笼统地"复现这篇论文"。NeurIPS 复现挑战赛的目标就是独立验证已录用论文中的实证主张[^pineau2021improving-e8]。
- **想清楚改哪些条件最能检验结论。** 安全方向的例子：Klees 等人重新评估模糊测试工具 AFLFast（模糊测试：用大量随机生成的输入测试程序、发现缺陷），发现它在原论文选的程序上表现好，换成其他论文用过的两个程序，就不比作为比较对象的 AFL 好了[^klees2018evaluating-e3]。机器学习的例子：有研究发现，把超参数（训练前人为设定的参数，如学习率）搜索做得更充分，甚至只换一组随机初始化，新提出的方法往往就不比旧方法好了[^pineau2021improving-e2]。其他学科的对应做法是换一批参与者或换一个情境，例如心理学实验换到另一个国家、另一类人群中重做，看效应是否还在 `[本项目分析]`。
- **估计成本。** 有的实验即使有数据和代码，计算量也大到多数研究者无法复现[^pineau2021improving-e5]。

**为什么**：动机决定复现的类型。只想确认结果，就尽量贴近原研究；想知道能否推广，就有意改变情境或方法 `[本项目分析]`。

**容易错在哪：**

- **照搬原研究的弱点。** 用一项同样统计功效不足的研究去复现一项功效不足的研究，或者照搬而不纠正原研究的错误（例如用了不合适的统计检验），都是 SIGSOFT 列出的反面做法[^ralph2020empirical-e227]。统计功效指研究能检测出真实效应的能力，通常随样本量增大而提高。能改进的地方就改进，例如设计、分析或统计功效[^ralph2020empirical-e221]，并记进偏差记录（见第四步）。
- **擅自改研究问题。** 研究问题由原研究确定，复现必须沿用，概念复现也一样[^ralph2020empirical-e230]。想问新问题，就做扩展复现：保留全部原问题，再加新问题[^ralph2020empirical-e212]。

### 第二步：摸清原研究

**怎么做**：动手之前，把原研究的信息整理成一份文档。SIGSOFT 要求论文写清原研究的研究问题、设计、可能影响设计或结果解读的情境变量，以及主要发现[^ralph2020empirical-e216]。整理时可以把设计拆细 `[本项目分析]`：

- 参与者（如果有）：人数和相关特征；
- 制品：问卷、说明文档、原始数据、预处理后的数据、分析脚本等；
- 情境变量：例如硬件、数据版本、参与者背景。

后面每一处"和原研究不同"，都要相对这份文档来说。同时清点原作者公开了什么：方法描述、数据、代码、实验设置；公开了多少，决定了你最多能做到 R1、R2 还是 R3 `[本项目分析]`。

**容易错在哪**：以为论文写全了。Gundersen & Kjensmo 调查人工智能会议论文后发现，没有一篇记录了复现所需的全部信息，方法、数据、实验三类信息各只记录了 20%～30%[^gundersen2018state-e9]。机器学习结果难以复现的原因包括：模型或训练过程描述不完整、没有代码或代码有错、结果用的指标没说清楚[^pineau2021improving-e10]。缺什么就列出来，准备问原作者。

### 第三步：联系原作者，并记录互动

**怎么做：**

- **缺信息、缺材料时，联系原作者。** 一项研究发现，402 篇实验论文中，不联系作者能重复出 32.3%，联系后升到 48.3%[^gundersen2018state-e4]。另一项机器学习研究发现，原作者提供帮助时 85% 的结果被成功复现，作者不回复时只有 4%；但这里可能有选择偏差：确信能复现的作者更愿意帮忙[^pineau2021improving-e3]。
- **记下互动的程度**，从"只读了论文"到"原作者充当顾问"都有可能[^carver2010towards-e2]。论文里要描述与原作者的重叠或互动[^ralph2020empirical-e217]；原作者完全没参与，也写明这一点 `[本项目分析]`。
- **条件允许时，请原作者审阅你的复现方案**，这是 SIGSOFT 的加分项[^ralph2020empirical-e225]。

> **不同的看法：原作者该参与多少？**
> - **主张独立**：Gundersen & Kjensmo 认为独立团队更客观，他们没有动机夸大别人方法的表现，也不共享原团队的先入之见和没写下来的隐性知识[^gundersen2018state-e5]。他们把"独立团队"定义为只依据原团队留下的文档做实验[^gundersen2018state-e6]。
> - **主张合作**：原作者能补上论文没写的细节；上面的数据显示，有原作者参与时，能做出原结果的比例高得多[^gundersen2018state-e4][^pineau2021improving-e3]。SIGSOFT 也把原作者审阅方案列为加分项[^ralph2020empirical-e225]。
> - Carver（软件工程复现研究报告规范的提出者）指出，这个问题上有两种对立观点，双方都有合理之处[^carver2010towards-e3]；他的报告规范只要求写清互动程度[^carver2010towards-e2]。
>
> 实际操作中可以这样做 `[本项目分析]`：向原作者索取材料、询问缺失的细节；但怎样分析、怎样判定成功，由你事先自己决定。互动内容全部记下来，在论文里如实报告，让读者判断独立性。

### 第四步：写下方案，记录每一处偏差

**怎么做：**

- **开跑之前写下方案**：沿用原研究的哪些部分，改了哪些、为什么改，以及第五步的成功标准 `[本项目分析]`。
- **决定用原代码还是重新实现。** 用原作者的制品，是 ACM 意义上的可复现；完全自己实现，是可重现[^acm2020artifact-e17][^acm2020artifact-e18]。两者检验的东西不同：拿到原代码不等于代码是对的，直接根据论文描述重新实现算法有很大价值[^pineau2021improving-e4]。一种稳妥的顺序是：先用原代码跑通，确认你的环境能得到原来的数，再改条件或重新实现 `[本项目分析]`。
- **维护一份偏差记录。** 与原研究的每一处不同（设计、参与者、制品、流程、数据收集、分析）都要写出来并说明理由[^ralph2020empirical-e218][^carver2010towards-e4]，包括不得不做的改动，例如原数据版本已经拿不到。可以用这样一张表 `[本项目分析]`：

| 项目 | 原研究 | 本次复现 | 为什么不同 | 可能的影响 |
|---|---|---|---|---|
| 例：评测程序 | 6 个 | 原来的 6 个，另加 2 个 | 检验结论能否推广 | 新程序上结果可能不同 |

- **记录自己的过程**：每一步用的程序名和版本、确切的参数和输入[^sandve2013ten-e8]。具体做法见通用篇[整理科研材料](../../../general/2_during/03_organizing_materials.md)。

**为什么**：结果和原研究不一致时，读者首先会问"是不是你改了什么"。Carver 要求讨论你的改动是否可能导致了这些差异[^carver2010towards-e6]；没有偏差记录，就回答不了。

**容易错在哪**：边做边改，事后才回忆改了什么。换库版本、改预处理这类小改动最容易漏记，却可能正是结果不同的原因 `[本项目分析]`。

### 第五步：事先定好"怎样才算复现成功"

**怎么做：**

- **不要求数字完全一致。** ACM 的标准是：结果在该类实验可接受的误差范围内一致即可[^acm2020artifact-e14]，差异不应改变论文的主要主张[^acm2020artifact-e15]。
- **按复现程度定标准。** 什么算"相同的结果"，取决于复现到哪一级[^gundersen2018state-e7]。同一实现、同一数据（R1），结果应当完全相同；换了实现（R2），结果应当相同但不一定完全一致，差异可能来自实现和硬件，例如浮点运算方式不同[^gundersen2018state-e8]；实现和数据都换了（R3），要看结果是否支持相同的假设[^gundersen2018state-e7]。
- **开跑之前定好标准。** 看了结果再决定"多接近算成功"，标准会不自觉地偏向你期望的方向 `[本项目分析]`。
- **逐条主张判断，不给一个总分。** "这篇论文能不能复现"很少有简单的答案；多数复现报告给出的是细致的说明：方法、结果、主张分别复现到什么程度，不适合用一个分数概括[^pineau2021improving-e6]。SIGSOFT 要求清楚区分哪些结果一致、哪些不一致[^ralph2020empirical-e219]，并区分大小差异，分析差异是否合理、是否在预料之中[^ralph2020empirical-e222]。
- **结果有随机性时，跑多次。** Klees 等人发现，在程序 nm 上，单次运行时 AFL 比 AFLFast 找到更多崩溃，30 次运行的中位数却正好相反[^klees2018evaluating-e11]。只跑一次，"成功"或"失败"都可能是运气。重复次数和统计检验见通用篇[认真对待随机性和统计](../../../general/2_during/02_evidence_and_validity.md#5-认真对待随机性和统计)。

### 第六步：报告结果

**怎么做**：把四类信息分开写[^ralph2020empirical-e220]：

1. **原研究**：第二步整理的信息[^ralph2020empirical-e216]。
2. **本次复现**：动机和复现类型[^ralph2020empirical-e214][^ralph2020empirical-e215]，与原作者的互动[^carver2010towards-e2]，每一处改动及理由[^carver2010towards-e4]。
3. **结果对比**：专门用一节对比复现结果和原结果[^carver2010towards-e5]，可以把两边的结果并排放进一张汇总表[^carver2010towards-e10]。列出不一致的结果，讨论你的改动是否可能导致了差异[^carver2010towards-e6]。
4. **结论**：把两项研究放在一起，给出单看任何一项都看不出的认识，指出原研究的哪些结论得到了加强[^ralph2020empirical-e223][^carver2010towards-e7]；比较两边的局限[^ralph2020empirical-e224]。

篇幅有限（例如会议论文）时，四类信息仍要都给，只是写得简略，对比可以用表格[^carver2010towards-e8]。不得不删时，最不能删的是与原研究之间的改动和差异[^carver2010towards-e9]。

如果原研究已被复现过多次（一个"复现家族"），要简要总结之前的研究，把本次结果放到整个家族中看[^ralph2020empirical-e226][^carver2010towards-e11]。要用统计方法合并多项研究的结果，见[综述研究](review_study.md)中的元分析。

**没能复现，也要报告。** 报告负面结果的一般做法见通用篇[诚实报告：负面结果、局限和推测](../../../general/2_during/02_evidence_and_validity.md#7-诚实报告负面结果局限和推测)，复现研究还要注意：

- 推翻一个已有发现，需要的证据比发表一个新发现多得多，可能要好几个团队毫无疑问地证明结果是错的，学界才会改变看法[^pineau2021improving-e7]。所以报告失败的复现时，更要把偏差记录、重复次数、与原作者的沟通写完整 `[本项目分析]`。
- 写成"在这些条件下没有得到原结果"，而不是"原作者错了"。差异可能来自你的改动、原论文没写明的条件，也可能来自原结论本身 `[本项目分析]`。
- 复现论文有专门的去处：有会议专门征集复现论文（如信息检索会议 ECIR 2020），也有专门发表复现论文的开放获取期刊 ReScience C[^pineau2021improving-e9]。

---

## 3. 检查清单

依据 SIGSOFT 复现研究标准（该标准没有"做得出色"一档）。

**必须做到**

- [ ] 说明做这次复现的动机[^ralph2020empirical-e214]
- [ ] 从方法相似度、覆盖范围、团队三个角度写明复现类型[^ralph2020empirical-e215]
- [ ] 描述原研究：研究问题、设计、情境变量、主要发现[^ralph2020empirical-e216]
- [ ] 描述与原作者的重叠或互动[^ralph2020empirical-e217]
- [ ] 写出与原研究的每一处不同，并说明理由[^ralph2020empirical-e218]
- [ ] 对比复现结果和原结果，清楚区分一致和不一致的结果[^ralph2020empirical-e219]

**做到更好**

- [ ] 原研究、本次复现、结果对比、结论四部分分开写[^ralph2020empirical-e220]
- [ ] 在设计、分析或统计功效上改进原研究[^ralph2020empirical-e221]
- [ ] 讨论不一致的结果时区分大小差异，分析是否合理、是否在预料之中[^ralph2020empirical-e222]
- [ ] 综合两项研究下结论，指出原研究哪些结论得到了加强[^ralph2020empirical-e223]
- [ ] 比较两边的局限，提出综合多项研究后才显现的新情境变量假设[^ralph2020empirical-e224]
- [ ] 复现方案经原作者审阅[^ralph2020empirical-e225]
- [ ] 属于复现家族时，总结之前的研究，把结果放到整个家族中看[^ralph2020empirical-e226]
- [ ] 开跑之前写下成功标准 `[本项目分析]`

**这些情况可以不做，不算缺陷**

- 没有公开属于原作者、且原作者未允许公开的材料[^ralph2020empirical-e229]

**审稿时常见、但不成立的批评**

- "复现只是证实了原研究，没有发现不一致"[^ralph2020empirical-e228]
- 批评研究问题本身或它的措辞：研究问题由原研究确定，复现必须沿用[^ralph2020empirical-e230]
- 因为是重复已有工作的研究而拒稿[^ralph2020empirical-e62]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 笼统地"复现一篇论文"，不列具体主张 | 复现结果很少能用"能/不能"一句话概括[^pineau2021improving-e6] |
| 照搬原研究的功效不足或统计错误 | SIGSOFT 列为反面做法[^ralph2020empirical-e227] |
| 改动不记录，或事后才回忆 | 结果不一致时，无法判断是不是改动造成的[^carver2010towards-e6] |
| 看了结果再定成功标准 | 标准会偏向你期望的方向 `[本项目分析]` |
| 有随机性的实验只跑一次 | 单次运行的结论可能和多次运行正好相反[^klees2018evaluating-e11] |
| 只用原代码跑出相同的数，就宣称结论成立 | 原代码本身可能有错[^pineau2021improving-e4]；这只是 R1，说明不了方法本身有效[^gundersen2018state-e3] |
| 复现失败就不写了 | 推翻已有发现本来就需要更多证据[^pineau2021improving-e7]，你的结果是其中一份 `[本项目分析]` |

---

## 5. 延伸阅读

- **SIGSOFT Empirical Standards 的复现研究标准**：复现论文的审稿标准，投稿前逐条对照。
- **Carver 2010，Towards Reporting Guidelines for Experimental Replications**：只有 4 页，讲复现论文每部分写什么、会议论文篇幅不够时怎么取舍。
- **ACM Artifact Review and Badging**：可重复、可复现、可重现的正式定义，以及两个词对调的说明。
- **Pineau 等人 2021，Improving Reproducibility in Machine Learning Research**：机器学习方向。讲结果难以复现的原因、NeurIPS 复现挑战赛，以及一份好的复现报告是什么样。
- **Gundersen & Kjensmo 2018，State of the Art: Reproducibility in Artificial Intelligence**：R1～R3 三个复现程度，以及复现需要原论文记录哪些信息（方法、数据、实验）。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^ralph2020empirical-e208]: SIGSOFT 复现研究标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e208)
[^ralph2020empirical-e209]: SIGSOFT 复现研究标准，Application。[证据](../../../../sources/notes/ralph2020empirical.md#e209)
[^ralph2020empirical-e210]: SIGSOFT 复现研究标准，Definitions。[证据](../../../../sources/notes/ralph2020empirical.md#e210)
[^ralph2020empirical-e211]: SIGSOFT 复现研究标准，脚注 1。[证据](../../../../sources/notes/ralph2020empirical.md#e211)
[^ralph2020empirical-e212]: SIGSOFT 复现研究标准，脚注 2。[证据](../../../../sources/notes/ralph2020empirical.md#e212)
[^ralph2020empirical-e213]: SIGSOFT 复现研究标准，脚注 3。[证据](../../../../sources/notes/ralph2020empirical.md#e213)
[^ralph2020empirical-e214]: SIGSOFT 复现研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e214)
[^ralph2020empirical-e215]: SIGSOFT 复现研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e215)
[^ralph2020empirical-e216]: SIGSOFT 复现研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e216)
[^ralph2020empirical-e217]: SIGSOFT 复现研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e217)
[^ralph2020empirical-e218]: SIGSOFT 复现研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e218)
[^ralph2020empirical-e219]: SIGSOFT 复现研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e219)
[^ralph2020empirical-e220]: SIGSOFT 复现研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e220)
[^ralph2020empirical-e221]: SIGSOFT 复现研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e221)
[^ralph2020empirical-e222]: SIGSOFT 复现研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e222)
[^ralph2020empirical-e223]: SIGSOFT 复现研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e223)
[^ralph2020empirical-e224]: SIGSOFT 复现研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e224)
[^ralph2020empirical-e225]: SIGSOFT 复现研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e225)
[^ralph2020empirical-e226]: SIGSOFT 复现研究标准，加分项（复现家族）。[证据](../../../../sources/notes/ralph2020empirical.md#e226)
[^ralph2020empirical-e227]: SIGSOFT 复现研究标准，Antipatterns。[证据](../../../../sources/notes/ralph2020empirical.md#e227)
[^ralph2020empirical-e228]: SIGSOFT 复现研究标准，Invalid Criticisms。[证据](../../../../sources/notes/ralph2020empirical.md#e228)
[^ralph2020empirical-e229]: SIGSOFT 复现研究标准，Invalid Criticisms。[证据](../../../../sources/notes/ralph2020empirical.md#e229)
[^ralph2020empirical-e230]: SIGSOFT 复现研究标准，Invalid Criticisms。[证据](../../../../sources/notes/ralph2020empirical.md#e230)
[^ralph2020empirical-e62]: SIGSOFT 通用标准，Invalid Criticisms。[证据](../../../../sources/notes/ralph2020empirical.md#e62)
[^carver2010towards-e1]: Carver 2010，§2.3。[证据](../../../../sources/notes/carver2010towards.md#e1)
[^carver2010towards-e2]: Carver 2010，§3.1.2。[证据](../../../../sources/notes/carver2010towards.md#e2)
[^carver2010towards-e3]: Carver 2010，§1。[证据](../../../../sources/notes/carver2010towards.md#e3)
[^carver2010towards-e4]: Carver 2010，§3.1.2。[证据](../../../../sources/notes/carver2010towards.md#e4)
[^carver2010towards-e5]: Carver 2010，§3.1.3。[证据](../../../../sources/notes/carver2010towards.md#e5)
[^carver2010towards-e6]: Carver 2010，§3.1.3。[证据](../../../../sources/notes/carver2010towards.md#e6)
[^carver2010towards-e7]: Carver 2010，§3.1.4。[证据](../../../../sources/notes/carver2010towards.md#e7)
[^carver2010towards-e8]: Carver 2010，§3.3。[证据](../../../../sources/notes/carver2010towards.md#e8)
[^carver2010towards-e9]: Carver 2010，§3.3。[证据](../../../../sources/notes/carver2010towards.md#e9)
[^carver2010towards-e10]: Carver 2010，§2.3。[证据](../../../../sources/notes/carver2010towards.md#e10)
[^carver2010towards-e11]: Carver 2010，§3.2。[证据](../../../../sources/notes/carver2010towards.md#e11)
[^acm2020artifact-e5]: ACM 2020，Results Validated。[证据](../../../../sources/notes/acm2020artifact.md#e5)
[^acm2020artifact-e9]: ACM 2020，开头。[证据](../../../../sources/notes/acm2020artifact.md#e9)
[^acm2020artifact-e14]: ACM 2020，Results Validated。[证据](../../../../sources/notes/acm2020artifact.md#e14)
[^acm2020artifact-e15]: ACM 2020，Results Validated。[证据](../../../../sources/notes/acm2020artifact.md#e15)
[^acm2020artifact-e16]: ACM 2020，术语：Repeatability。[证据](../../../../sources/notes/acm2020artifact.md#e16)
[^acm2020artifact-e17]: ACM 2020，术语：Reproducibility。[证据](../../../../sources/notes/acm2020artifact.md#e17)
[^acm2020artifact-e18]: ACM 2020，术语：Replicability。[证据](../../../../sources/notes/acm2020artifact.md#e18)
[^acm2020artifact-e19]: ACM 2020，术语部分的注释。[证据](../../../../sources/notes/acm2020artifact.md#e19)
[^pineau2021improving-e1]: Pineau 等人 2021，§2.1。[证据](../../../../sources/notes/pineau2021improving.md#e1)
[^pineau2021improving-e2]: Pineau 等人 2021，§2。[证据](../../../../sources/notes/pineau2021improving.md#e2)
[^pineau2021improving-e3]: Pineau 等人 2021，§2（转述 Raff 2019）。[证据](../../../../sources/notes/pineau2021improving.md#e3)
[^pineau2021improving-e4]: Pineau 等人 2021，§3。[证据](../../../../sources/notes/pineau2021improving.md#e4)
[^pineau2021improving-e5]: Pineau 等人 2021，§3。[证据](../../../../sources/notes/pineau2021improving.md#e5)
[^pineau2021improving-e6]: Pineau 等人 2021，§4。[证据](../../../../sources/notes/pineau2021improving.md#e6)
[^pineau2021improving-e7]: Pineau 等人 2021，§1。[证据](../../../../sources/notes/pineau2021improving.md#e7)
[^pineau2021improving-e8]: Pineau 等人 2021，§4。[证据](../../../../sources/notes/pineau2021improving.md#e8)
[^pineau2021improving-e9]: Pineau 等人 2021，§6。[证据](../../../../sources/notes/pineau2021improving.md#e9)
[^pineau2021improving-e10]: Pineau 等人 2021，§1。[证据](../../../../sources/notes/pineau2021improving.md#e10)
[^gundersen2018state-e1]: Gundersen & Kjensmo 2018，The Terminology of Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e1)
[^gundersen2018state-e2]: Gundersen & Kjensmo 2018，Degrees of Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e2)
[^gundersen2018state-e3]: Gundersen & Kjensmo 2018，Degrees of Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e3)
[^gundersen2018state-e4]: Gundersen & Kjensmo 2018，Introduction（转述 Collberg & Proebsting 2016）。[证据](../../../../sources/notes/gundersen2018state.md#e4)
[^gundersen2018state-e5]: Gundersen & Kjensmo 2018，Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e5)
[^gundersen2018state-e6]: Gundersen & Kjensmo 2018，Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e6)
[^gundersen2018state-e7]: Gundersen & Kjensmo 2018，Reproducibility；Degrees of Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e7)
[^gundersen2018state-e8]: Gundersen & Kjensmo 2018，Degrees of Reproducibility。[证据](../../../../sources/notes/gundersen2018state.md#e8)
[^gundersen2018state-e9]: Gundersen & Kjensmo 2018，Abstract。[证据](../../../../sources/notes/gundersen2018state.md#e9)
[^klees2018evaluating-e3]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e11]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e11)
[^sandve2013ten-e8]: Sandve 等人 2013，Rule 1。[证据](../../../../sources/notes/sandve2013ten.md#e8)
