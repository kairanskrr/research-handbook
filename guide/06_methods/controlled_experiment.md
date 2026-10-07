# 对照实验：有人参与，比较工具或方法对人的影响

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**有人类参与者的对照实验**：研究者主动改变一个因素（例如开发者用哪个调试工具），把参与者随机分组，在其他条件尽量相同的情况下，比较这个因素对人的表现有什么影响。

如果被比较的是软件系统、工具或模型本身，可以自动运行、重复测量，不需要人参与，见[基准评测](../07_fields/computer-science/practices/benchmarking.md)；如果你提出了一个新工具，想知道整篇论文该怎样评估它，先看[工程研究](../07_fields/computer-science/practices/engineering_research.md)，有人参与的实验只是其中一种评估方式。统计检验的细节见通用篇的[证据、分析与效度](../general/2_during/02_evidence_and_validity.md)，本文不重复。

**读完本文，你应该能：**

- 判断自己的问题是否适合用对照实验回答；
- 写出假设，定义变量，选对被试间或被试内设计；
- 想清楚招谁、招多少、做什么任务、测什么，并用预实验检验设计；
- 用文末的检查清单检查自己的实验。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把实验定义为：在受控条件下有意引入一种干预，观察它对现实某些方面的影响[^ralph2020empirical-e162]。它的人类参与者实验标准适用于同时满足四个条件的研究：操纵一个或多个**自变量**（研究者主动改变的因素），控制许多**无关变量**（可能影响结果、但不是研究对象的因素），每种处理分别施加到多个参与者身上，并且有人参与[^ralph2020empirical-e163]。

**它擅长回答因果问题。** 例如"用新调试工具，开发者定位缺陷会更快吗"。对照实验通过控制把变量隔离出来，比其他方法更能证明差异来自这个工具，而不是来自开发者的经验等其他因素；代价是情境比较人为[^ko2015practical-e2]。

**它不擅长回答"怎么样、为什么"的问题。** 开发者怎么用这个工具、要懂哪些概念、要学多久，这类问题实验很难回答，因为实验本质上是做比较；更适合用非实验的定量或定性方法。而且这类问题的答案往往要先有，你才知道实验该比较什么、用什么任务、测什么[^ko2015practical-e1]。

**和相近类型的区别** `[本项目分析]`：

| | 对照实验 | [基准评测](../07_fields/computer-science/practices/benchmarking.md) | [问卷调查](questionnaire_survey.md) | 实地部署 / [案例研究](case_study.md) |
|---|---|---|---|---|
| 研究对象 | 人在某种处理下的表现 | 系统或模型本身 | 人的看法、经历 | 真实环境中的人和工具 |
| 研究者做什么 | 主动操纵变量，随机分组 | 自动运行、测量 | 提问 | 观察，较少控制 |
| 典型问题 | "用工具 A 的人更快吗？" | "系统 A 比 B 快吗？" | "开发者怎么看工具 A？" | "团队用了工具 A 之后发生了什么？" |

**真实验与准实验。** 随机把参与者分到各组的是真实验；没有随机分组的是准实验[^ralph2020empirical-e164]。准实验只在两种情况下合适：做预研究，或者分组不由你决定（例如学生已经分在一门课的两个班）。只说一句"本研究是探索性的"，不足以作为不随机分组的理由[^ralph2020empirical-e182]。

**不只是软件工程。** SIGSOFT 标准面向软件工程，但同样的方法也用在人机交互的用户研究、安全领域的可用性研究（例如比较两种安全警告界面）；计算机以外，教育学比较两种教学方法对学生成绩的影响、心理学比较两种界面或说明方式对人判断的影响，也是同样的逻辑。各方向的惯例和术语略有不同，下面的步骤大体通用。`[本项目分析]`

---

## 2. 怎么做

一个典型的设计是：一组用基线工具，一组用你的工具；**除了用哪个工具，所有参与者拿到的材料、说明、任务和环境完全一样**。这样两组结果有差异时，才能有力地说是工具造成的[^ko2015practical-e3]。下面每一步都在为这一点服务。

一个实用的起点：先起草伦理审查申请表和论文的方法部分，把它当作设计草稿，能帮你发现还没想清楚的细节[^ko2015practical-e4]。

### 第 1 步：写出假设，定义变量

**怎么做：**

- **写出正式的假设**，例如"使用工具 A 与使用工具 B 的开发者，修复同一批缺陷的用时不同"。默认用**双侧假设**（只说"不同"，不预设方向）；要用单侧假设（"A 更快"），需要依据已有研究说明理由[^ralph2020empirical-e165]。
- **说清三类变量**[^ralph2020empirical-e166]：
  - 自变量：你操纵什么，怎么操纵（例如工具 A / 工具 B）；
  - 因变量：你测什么，单位和测量工具是什么，为什么这样测（例如用时，以分钟计）；
  - 无关变量：还有什么会影响结果（例如编程经验），用实验设计控制、用统计方法控制，还是没有控制。
- **能预注册就预注册**：在实验开始前把假设和设计公开存档[^ralph2020empirical-e176]。

**为什么**：验证性的实验，假设要在看到数据之前定下来。看到结果再提假设（HARKing）、只报告显著的检验（p-hacking），SIGSOFT 都列为反面做法[^ralph2020empirical-e27]。探索性研究和验证性研究的区别，见通用篇[分清探索性研究和验证性研究](../general/1_before/04_research_design.md#4-分清探索性研究和验证性研究)。

**容易错在哪**：用不好的替代指标当因变量，例如用完成时间代表任务有多复杂[^ralph2020empirical-e180]。

### 第 2 步：选设计：被试间还是被试内

| | 被试间设计（between-subjects） | 被试内设计（within-subjects） |
|---|---|---|
| 怎么做 | 每人只用一种工具，随机分组 | 每人在不同任务上依次用所有工具[^ko2015practical-e17] |
| 好处 | 没有学习效应，每人耗时短 `[本项目分析]` | 同样人数得到更多数据，个人差异互相抵消 `[本项目分析]` |
| 风险 | 个人差异大，需要更多人 | 学习效应、疲劳和厌倦[^ko2015practical-e18][^ko2015practical-e19] |

**被试间设计：随机分组。** 随机分组把参与者技能和习惯上的差异均匀分到各组，降低"组间差异其实来自人、不是来自工具"的可能[^ko2015practical-e16]。论文里要说明随机是怎么做的，例如随机数怎么生成；不随机，就要给出有力的理由，并说明怎样减轻"各组本来就不同"的威胁，例如做前测和后测，或按能力配对[^ralph2020empirical-e169]。

**被试内设计：一定要做平衡（counterbalancing）。** 参与者在第一个任务里学到的东西会帮到第二个任务，这叫学习效应。所以要随机安排任务的先后顺序，以及在哪个任务上用你的工具；比较三个及以上工具时，可以用拉丁方（一种让每种处理在每个顺序位置上出现次数相同的排列表）[^ko2015practical-e18]。

**其他设计**：例如中断时间序列设计，在引入工具前、引入后、撤掉后各测一次，只需要一组人，更贴近公司里的试用 `[本项目分析]`；但它对因果的把握更弱，因为很难排除引入和撤掉工具期间同时发生的其他变化[^ko2015practical-e20]。

**容易错在哪**：分析方法和设计不匹配，例如被试内设计得到的是配对数据，却用了独立样本 t 检验[^ralph2020empirical-e181]。设计时就要想好用什么检验 `[本项目分析]`。

### 第 3 步：确定参与者：招谁，招多少

**先写纳入标准。** 纳入标准应当反映你认为会从工具中受益的那类人，以及工具会派上用场的工作情境[^ko2015practical-e6]，例如"至少一年 Java 经验、没用过此类工具"。招募材料和筛选问题要问得中立，不让应征者看出"正确答案"是什么[^ko2015practical-e13]。先想清楚你想把结论推广到哪些人身上[^baltes2022sampling-e11]。

**不要自己当参与者。** Ko 等人在文献综述中发现，62% 的工具评估其实是工具发明者自己用、自己报告体验；这能说明工具能用在哪里，却说明不了别人用了会不会受益[^ko2015practical-e7]。

**学生还是专业人员？** 没有哪一类绝对更好[^falessi2018empirical-e1]。几个要点：

- **按经验刻画参与者，而不是贴标签。** "学生/专业人员"二分法不合适：很多学生有实习或工作经验[^falessi2018empirical-e2]。Falessi 等人建议从真实经验、相关经验、近期经验三个维度描述参与者[^falessi2018empirical-e8]。
- **专业人员也是便利样本**（便利样本：按"方便拿到"选出的样本，它会削弱结论的可推广性[^baltes2022sampling-e2]）。在公司里招到的人，既不是从全体开发者中随机抽的，往往也不是这家公司开发者的随机样本[^falessi2018empirical-e4]。
- **学生有特有的风险。** 例如被试期望效应：参与者猜到研究者希望看到什么，就照着去做[^ko2015practical-e8]。把实验介绍得看不出你在乎哪种结果，可以减轻它[^ko2015practical-e9]。
- **在设计阶段就想清楚，并写进论文。** 计划用便利样本时，就要想好它代表什么总体[^falessi2018empirical-e5]；论文要具体说明在本实验的情境下用学生为什么合适[^falessi2018empirical-e6]。

> **不同的看法：能招专业人员时，要不要尽量招？**
> - Falessi 等人认为，用学生是实验室实验中合理、必要的简化[^falessi2018empirical-e1]；专业人员难招，有一次只有 33% 承诺参加的人真正到场[^falessi2018empirical-e7]。
> - Shepperd 在评论中认为，用学生做初步实验很有价值；但目标总体是某类专业人员时，只要可行就应该用专业人员，"更费事"不是理由。他和合作者做过 400 多名专业人员参加的实验[^shepperd2018inferencing-e4][^shepperd2018inferencing-e1]。他还提醒，要推广的不只是参与者，还有任务和环境[^shepperd2018inferencing-e2][^shepperd2018inferencing-e3]。
>
> - 分歧没有看上去那么大：Falessi 等人的结论是，学生既不是总能、也不是总不能代替专业开发者，要看情境和总体[^falessi2018empirical-e9]；Shepperd 也肯定学生在初步实验中的价值[^shepperd2018inferencing-e4]。
>
> 实际操作中：先问自己"结论要推广到谁"。目标是新手或学生时，用学生很自然；目标是有经验的专业人员时，可以先用学生做预实验、打磨设计，正式实验尽量请到符合条件的专业人员。不管用谁，都按经验描述参与者，并说明理由。`[本项目分析]`

**招多少人。** SIGSOFT 标准要求说明样本量的依据，例如做**功效分析**（power analysis）[^ralph2020empirical-e167]：事先估算要多少人，才能在差异真实存在时有足够大的把握检测到它。它需要三个输入：预期的效应量、结果的预期波动、可以接受的第一类错误率（即假阳性率）[^ko2015practical-e11]，前两项可以用以往实验或预实验的数据来估计[^ko2015practical-e12]。作为参考，Ko 等人回顾的实验，每组参与者的中位数是 18 人；他们认为每组约 20 人可以作为起点，但不保证够[^ko2015practical-e10]。在课堂上做实验、人数固定时，可以不做事先的功效分析[^ralph2020empirical-e179]。

### 第 4 步：设计任务、材料和培训

**真实和可控之间要取舍。** 越接近真实工作，结论越能推广，但控制越少，越难确定差异来自哪里[^ko2015practical-e23]。内部效度和外部效度不可能同时达到最大[^falessi2018empirical-e3]。

- **任务从哪来**：自己从头设计，能针对工具的功能，但可能不像实际工作中的任务，还可能不公平地偏向你的工具[^ko2015practical-e24]；从真实项目（例如开源项目的缺陷报告）中选，更贴近实际 `[本项目分析]`。
- **难度要合适**：太简单，人人都完成，出现**天花板效应**；太难，谁都完不成，出现**地板效应**；两种情况都看不出工具之间的差异[^ko2015practical-e25]。
- **实验对象**（参与者要处理的程序或数据）：说明是真实系统还是玩具系统、规模多大、为什么选它。不要让对照组和实验组用不同的程序，否则程序的差异和工具的差异混在一起，分不开[^ralph2020empirical-e170]。
- **培训**：培训里教了什么，就成了"工具在什么条件下使用"的前提，论文结论也只在这个前提下成立[^ko2015practical-e21]。注意，短时间的实验天生偏向能快速学会的工具，不利于需要长期练习的工具[^ko2015practical-e22]。

**容易错在哪**：面向团队协作的工具，很难用个人对照实验评估；Ko 等人回顾的论文中，没有一篇在团队情境下做实验[^ko2015practical-e34]。这时可以考虑实地部署或案例研究。`[本项目分析]`

### 第 5 步：定好怎么测

Ko 等人指出，**结果测量的波动是实验得出负面结果的主要原因**：波动越大，越难看出真实的差异。其中一部分波动是自然的，应当保留；要消除的是无关波动[^ko2015practical-e5]。测量定义得越清楚、执行得越一致，无关波动越少 `[本项目分析]`。

- **任务是否成功**：事先定好三件事：达到什么状态算成功，怎么判断已经达到，怎么把目标讲给参与者、让所有人理解一致[^ko2015practical-e26]。
- **用时**：用时和成功率此消彼长，人可以做得快而粗、或慢而细，所以两个都测[^ko2015practical-e27]。
- **主观评价**：不要只问一句"这个工具有用吗"。有研究发现，参与者偏爱他们以为是访谈者设计的技术的可能性高出 2.5 倍，即使那项技术更差[^ko2015practical-e28]；可以改用经过验证的量表，例如技术接受模型问卷[^ko2015practical-e29]。
- **背景信息可以放在任务之后收集**：任务前询问经验，可能让经验少的人信心下降，影响表现[^ko2015practical-e15]。
- **加分项**：分析因变量是否真的测到了你想测的东西；做**操纵检查**，确认处理确实起了设想的作用（例如实验组真的用了工具）[^ralph2020empirical-e176]。

### 第 6 步：先做预实验

**怎么做**：正式实验前，先找几个人试做，目的是找出无关波动的来源[^ko2015practical-e31]，例如材料看不懂、工具有缺陷、任务有歧义 `[本项目分析]`。可以先由研究者自己当参与者预演一遍[^ko2015practical-e33]；但最重要的一轮，要尽量用与正式实验相同类型的参与者、场地、材料、流程和实验人员[^ko2015practical-e32]。发现问题就改，改完再试。

**为什么**：Ko 等人回顾的 345 项研究中，只有 11 项提到做过预实验[^ko2015practical-e31]。预实验的数据还能用来估计功效分析需要的数值[^ko2015practical-e12]。预研究的一般建议见通用篇[先用预研究或简化版本检验设计](../general/1_before/04_research_design.md#6-先用预研究或简化版本检验设计)。

**容易错在哪**：把预实验的数据并入正式结果。预实验的数据应该丢弃，因为当时的设置还在变[^ko2015practical-e32]。

### 第 7 步：处理好伦理和知情同意

有人参与的研究，风险评估、知情同意、隐私保护、伦理审查的一般要求，见通用篇的[科研诚信与伦理](../general/4_throughout/02_integrity_and_ethics.md)。对照实验要额外注意：

- **难任务也可能伤人。** 特别难的任务，尤其对经验不足的人，可能带来压力和挫败感[^ko2015practical-e14]。实验结束后要做一次说明（debriefing），不要让人带着"我失败了"的感觉离开；同时请他们不要外传答案，以免后来的参与者事先知道[^ko2015practical-e30]。
- **注意权力关系。** 通过经理或任课教师招募时，要说明怎样保证参与者是自由同意的[^ralph2020empirical-e186]。`[本项目分析]` 在自己任课的班上招募时尤其要注意，例如由别人代收同意书，并保证参加与否不影响成绩。
- **说明激励。** 论文要写明有没有给报酬、给了什么[^ralph2020empirical-e171]，以及怎样避免强迫[^ralph2020empirical-e185]。
- **用到欺骗时**，事后要向参与者说明原因，并给他们撤回数据的机会[^ralph2020empirical-e187]。

### 第 8 步：分析和报告

**分析**：报告适合数据分布的描述统计和推断统计，说明为什么选这些检验；报告效应量和置信区间，而不只是"显著/不显著"[^ralph2020empirical-e172]。把数据分布画出来[^ralph2020empirical-e177]。统计方面的一般做法见[证据、分析与效度](../general/2_during/02_evidence_and_validity.md)。

**报告要写清**：

- 参与者是谁：年龄、性别、教育、相关经验等[^ralph2020empirical-e172]；
- 完整的设计和流程：各组的处理、材料、任务、设计类型、分组方式、实施安排[^ralph2020empirical-e168]；
- 执行和设计之间的偏离及其影响，例如有人中途退出，破坏了两组的平衡[^ralph2020empirical-e175]；
- 效度：讨论构念效度、结论效度、内部效度和外部效度，以及对结果的其他解释[^ralph2020empirical-e173]；**每条威胁都要说明它对结果有什么影响**，只罗列是反面做法[^ralph2020empirical-e52]；
- 公开任务材料、去除身份信息的原始数据和分析脚本[^ralph2020empirical-e174]。

**容易错在哪**：夸大样本的代表性[^baltes2022sampling-e8]；或者在局限部分承认样本有偏差，到了结论又把结果写得几乎普遍适用[^baltes2022sampling-e9]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 的人类参与者实验标准。

**必须做到**

- [ ] 写出正式假设；用双侧假设，或说明用单侧假设的理由[^ralph2020empirical-e165]
- [ ] 说明自变量、因变量和无关变量，以及各自怎样操纵、测量或控制[^ralph2020empirical-e166]
- [ ] 说明样本量的依据[^ralph2020empirical-e167]
- [ ] 描述设计和流程，包括任务、材料、分组和实施安排[^ralph2020empirical-e168]
- [ ] 随机分组并说明怎么做的，或者给出不随机的有力理由和补救措施[^ralph2020empirical-e169]
- [ ] 描述并说明实验对象的选择，承认对象和处理之间的混杂[^ralph2020empirical-e170]
- [ ] 说明有没有给参与激励[^ralph2020empirical-e171]
- [ ] 描述参与者；报告合适的统计量、效应量和置信区间[^ralph2020empirical-e172]
- [ ] 讨论四类效度和对结果的其他解释[^ralph2020empirical-e173]
- [ ] 说明风险、招募方式、报酬和知情同意（伦理补充标准）[^ralph2020empirical-e68][^ralph2020empirical-e185]

**做到更好**

- [ ] 公开完整流程、任务材料、去除身份信息的数据和分析脚本[^ralph2020empirical-e174]
- [ ] 说明执行与设计的偏离及其影响[^ralph2020empirical-e175]
- [ ] 分析因变量的构念效度；报告操纵检查；预注册假设和设计[^ralph2020empirical-e176]
- [ ] 讨论没有采用的其他设计；把数据分布画出来[^ralph2020empirical-e177]

**做得出色**

- [ ] 在不同文化或地区做多次实验或重复研究；用多种方法收集数据、相互印证[^ralph2020empirical-e178]

**这些情况可以不做，不算缺陷**

- 在课堂上做实验、人数固定时，不做事先的功效分析[^ralph2020empirical-e179]

**审稿时常见、但不成立的批评**：你不必为此担心，但要在论文里说明自己的选择

- "参与者是学生"：是否合适要结合情境、需要的控制程度和被评估的技术来判断，论文必须说明理由[^ralph2020empirical-e183]
- "外部效度低""这只是重复研究""应该用别的方法""人数太少（没有功效分析支持）""没有用激励方案"[^ralph2020empirical-e184]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 工具作者自己当参与者 | 说明不了别人用了会不会受益[^ko2015practical-e7] |
| 只因为"方便"用学生，事后才想代表性 | 要在设计时就想清楚总体和效度[^falessi2018empirical-e5] |
| 两组用不同的程序或任务 | 对象和处理混在一起，分不清差异来自哪里[^ralph2020empirical-e170] |
| 被试内设计不做平衡 | 学习效应会被当成工具的效果[^ko2015practical-e18] |
| 任务太简单或太难 | 天花板或地板效应，看不出差异[^ko2015practical-e25] |
| 只问"工具有用吗" | 参与者倾向于讨好研究者[^ko2015practical-e28] |
| 不做预实验 | 材料、任务、工具的问题在正式实验里才暴露，产生大量无关波动[^ko2015practical-e31] |
| 对配对数据用独立样本检验 | 分析和设计不匹配[^ralph2020empirical-e181] |
| 只罗列效度威胁 | 读者不知道它们对结果有什么影响[^ralph2020empirical-e52] |

---

## 5. 延伸阅读

- **怎样实际设计和执行一个工具实验**：Ko、LaToza & Burnett 2015，从招募、知情同意、培训、任务设计到测量和预实验，逐项给出可选做法及其利弊。本文的大部分操作建议来自这里。
- **评审时用什么标准**：SIGSOFT 实证研究标准中的人类参与者实验标准和伦理补充标准；标准末尾还列了实验设计、交叉设计、统计方法、参与激励等方面的推荐读物。
- **学生还是专业人员**：Falessi 等人 2018 及 Shepperd 2018 的评论，两边的理由都值得读。
- **抽样与代表性**：Baltes & Ralph 2022。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e162]: SIGSOFT 人类参与者实验标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e162)
[^ralph2020empirical-e163]: SIGSOFT 人类参与者实验标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e163)
[^ralph2020empirical-e164]: SIGSOFT 人类参与者实验标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e164)
[^ralph2020empirical-e165]: SIGSOFT 人类参与者实验标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e165)
[^ralph2020empirical-e166]: SIGSOFT 人类参与者实验标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e166)
[^ralph2020empirical-e167]: SIGSOFT 人类参与者实验标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e167)
[^ralph2020empirical-e168]: SIGSOFT 人类参与者实验标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e168)
[^ralph2020empirical-e169]: SIGSOFT 人类参与者实验标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e169)
[^ralph2020empirical-e170]: SIGSOFT 人类参与者实验标准，必要项及脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e170)
[^ralph2020empirical-e171]: SIGSOFT 人类参与者实验标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e171)
[^ralph2020empirical-e172]: SIGSOFT 人类参与者实验标准，必要项（结果）。[证据](../../sources/notes/ralph2020empirical.md#e172)
[^ralph2020empirical-e173]: SIGSOFT 人类参与者实验标准，必要项（讨论）。[证据](../../sources/notes/ralph2020empirical.md#e173)
[^ralph2020empirical-e174]: SIGSOFT 人类参与者实验标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e174)
[^ralph2020empirical-e175]: SIGSOFT 人类参与者实验标准，加分项及脚注 3。[证据](../../sources/notes/ralph2020empirical.md#e175)
[^ralph2020empirical-e176]: SIGSOFT 人类参与者实验标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e176)
[^ralph2020empirical-e177]: SIGSOFT 人类参与者实验标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e177)
[^ralph2020empirical-e178]: SIGSOFT 人类参与者实验标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e178)
[^ralph2020empirical-e179]: SIGSOFT 人类参与者实验标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e179)
[^ralph2020empirical-e180]: SIGSOFT 人类参与者实验标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e180)
[^ralph2020empirical-e181]: SIGSOFT 人类参与者实验标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e181)
[^ralph2020empirical-e52]: SIGSOFT 人类参与者实验标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e52)
[^ralph2020empirical-e182]: SIGSOFT 人类参与者实验标准，脚注 5。[证据](../../sources/notes/ralph2020empirical.md#e182)
[^ralph2020empirical-e183]: SIGSOFT 人类参与者实验标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e183)
[^ralph2020empirical-e184]: SIGSOFT 人类参与者实验标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e184)
[^ralph2020empirical-e68]: SIGSOFT 伦理补充标准（人类参与者），必要项。[证据](../../sources/notes/ralph2020empirical.md#e68)
[^ralph2020empirical-e185]: SIGSOFT 伦理补充标准（人类参与者），必要项。[证据](../../sources/notes/ralph2020empirical.md#e185)
[^ralph2020empirical-e186]: SIGSOFT 伦理补充标准（人类参与者），脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e186)
[^ralph2020empirical-e187]: SIGSOFT 伦理补充标准（人类参与者），脚注 7。[证据](../../sources/notes/ralph2020empirical.md#e187)
[^ralph2020empirical-e27]: SIGSOFT General Standard，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e27)
[^ko2015practical-e1]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e1)
[^ko2015practical-e2]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e2)
[^ko2015practical-e3]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e3)
[^ko2015practical-e4]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e4)
[^ko2015practical-e5]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e5)
[^ko2015practical-e6]: Ko 等人 2015，§3.1。[证据](../../sources/notes/ko2015practical.md#e6)
[^ko2015practical-e7]: Ko 等人 2015，§3.1。[证据](../../sources/notes/ko2015practical.md#e7)
[^ko2015practical-e8]: Ko 等人 2015，§3.1。[证据](../../sources/notes/ko2015practical.md#e8)
[^ko2015practical-e9]: Ko 等人 2015，§3.1。[证据](../../sources/notes/ko2015practical.md#e9)
[^ko2015practical-e10]: Ko 等人 2015，§3.2。[证据](../../sources/notes/ko2015practical.md#e10)
[^ko2015practical-e11]: Ko 等人 2015，§3.2。[证据](../../sources/notes/ko2015practical.md#e11)
[^ko2015practical-e12]: Ko 等人 2015，§3.2。[证据](../../sources/notes/ko2015practical.md#e12)
[^ko2015practical-e13]: Ko 等人 2015，§3.3。[证据](../../sources/notes/ko2015practical.md#e13)
[^ko2015practical-e14]: Ko 等人 2015，§4.1。[证据](../../sources/notes/ko2015practical.md#e14)
[^ko2015practical-e15]: Ko 等人 2015，§4.2。[证据](../../sources/notes/ko2015practical.md#e15)
[^ko2015practical-e16]: Ko 等人 2015，§4.3。[证据](../../sources/notes/ko2015practical.md#e16)
[^ko2015practical-e17]: Ko 等人 2015，§4.3。[证据](../../sources/notes/ko2015practical.md#e17)
[^ko2015practical-e18]: Ko 等人 2015，§4.3。[证据](../../sources/notes/ko2015practical.md#e18)
[^ko2015practical-e19]: Ko 等人 2015，§4.3。[证据](../../sources/notes/ko2015practical.md#e19)
[^ko2015practical-e20]: Ko 等人 2015，§4.3。[证据](../../sources/notes/ko2015practical.md#e20)
[^ko2015practical-e21]: Ko 等人 2015，§4.4。[证据](../../sources/notes/ko2015practical.md#e21)
[^ko2015practical-e22]: Ko 等人 2015，§4.4。[证据](../../sources/notes/ko2015practical.md#e22)
[^ko2015practical-e23]: Ko 等人 2015，§5。[证据](../../sources/notes/ko2015practical.md#e23)
[^ko2015practical-e24]: Ko 等人 2015，§5.3。[证据](../../sources/notes/ko2015practical.md#e24)
[^ko2015practical-e25]: Ko 等人 2015，§5.5。[证据](../../sources/notes/ko2015practical.md#e25)
[^ko2015practical-e26]: Ko 等人 2015，§6.1。[证据](../../sources/notes/ko2015practical.md#e26)
[^ko2015practical-e27]: Ko 等人 2015，§6.2。[证据](../../sources/notes/ko2015practical.md#e27)
[^ko2015practical-e28]: Ko 等人 2015，§6.3。[证据](../../sources/notes/ko2015practical.md#e28)
[^ko2015practical-e29]: Ko 等人 2015，§6.3。[证据](../../sources/notes/ko2015practical.md#e29)
[^ko2015practical-e30]: Ko 等人 2015，§7。[证据](../../sources/notes/ko2015practical.md#e30)
[^ko2015practical-e31]: Ko 等人 2015，§8。[证据](../../sources/notes/ko2015practical.md#e31)
[^ko2015practical-e32]: Ko 等人 2015，§8。[证据](../../sources/notes/ko2015practical.md#e32)
[^ko2015practical-e33]: Ko 等人 2015，§8。[证据](../../sources/notes/ko2015practical.md#e33)
[^ko2015practical-e34]: Ko 等人 2015，§3.1。[证据](../../sources/notes/ko2015practical.md#e34)
[^falessi2018empirical-e1]: Falessi 等人 2018，摘要。[证据](../../sources/notes/falessi2018empirical.md#e1)
[^falessi2018empirical-e2]: Falessi 等人 2018，§4.1.1。[证据](../../sources/notes/falessi2018empirical.md#e2)
[^falessi2018empirical-e3]: Falessi 等人 2018，§4.1.2。[证据](../../sources/notes/falessi2018empirical.md#e3)
[^falessi2018empirical-e4]: Falessi 等人 2018，§4.1.3。[证据](../../sources/notes/falessi2018empirical.md#e4)
[^falessi2018empirical-e5]: Falessi 等人 2018，§6.2。[证据](../../sources/notes/falessi2018empirical.md#e5)
[^falessi2018empirical-e6]: Falessi 等人 2018，§6.2。[证据](../../sources/notes/falessi2018empirical.md#e6)
[^falessi2018empirical-e7]: Falessi 等人 2018，§4.2.1。[证据](../../sources/notes/falessi2018empirical.md#e7)
[^falessi2018empirical-e8]: Falessi 等人 2018，§7。[证据](../../sources/notes/falessi2018empirical.md#e8)
[^falessi2018empirical-e9]: Falessi 等人 2018，§9。[证据](../../sources/notes/falessi2018empirical.md#e9)
[^shepperd2018inferencing-e1]: Shepperd 2018，§2。[证据](../../sources/notes/shepperd2018inferencing.md#e1)
[^shepperd2018inferencing-e2]: Shepperd 2018，§3。[证据](../../sources/notes/shepperd2018inferencing.md#e2)
[^shepperd2018inferencing-e3]: Shepperd 2018，§4。[证据](../../sources/notes/shepperd2018inferencing.md#e3)
[^shepperd2018inferencing-e4]: Shepperd 2018，§5。[证据](../../sources/notes/shepperd2018inferencing.md#e4)
[^baltes2022sampling-e2]: Baltes & Ralph 2022，§2.1.1。[证据](../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e11]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e11)
[^baltes2022sampling-e8]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e8)
[^baltes2022sampling-e9]: Baltes & Ralph 2022，§6。[证据](../../sources/notes/baltes2022sampling.md#e9)
