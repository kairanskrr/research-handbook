# 选方法

> 本章的道理适用于各学科，例子和具体做法以计算机为例。本章引用的资料几乎都来自软件工程的研究方法文献：一份方法选择指南（Easterbrook 等人 2008）、一个研究策略框架（Storey 等人 2020）、ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，以及一篇讲软件工程论文写作的教程（Shaw 2003）。它们说的是软件工程社区的看法和规定，其他学科以本学科的规矩为准。

> **这一章必须做的事**
>
> 1. **先写出主要套路，拿套路说明核对证据清单。** 把套路说明里"什么样的证据才够"一节和你的清单逐条对照，补上漏掉的证据（[第 1 节](#1-先确认主要套路)）。
> 2. **给每条证据挑一种方法。** 把清单抄成三列：证据、它在问什么、候选方法；每个方法都问一句：它的前提条件我满足了吗（[第 2 节](#2-按每条证据挑方法)）。
> 3. **说清主方法强在哪、弱在哪，为什么弱点可以接受。** 写不出"可以接受"的理由，就考虑补一种方法（[第 3 节](#3-看清每种方法得到了什么放弃了什么)、[第 4 节](#4-需要时组合几种方法)）。
> 4. **逐行检查方法真能拿到证据。** 每行写一句：产出能填进结果表哪一格，要的东西拿不拿得到；有一行不过关，先处理这一行（[第 5 节](#5-检查这个方法真能拿到你要的证据吗)）。
> 5. **动手前读方法说明。** 每种方法找一份方法说明或指南、两三篇对照论文，弄清它在你的目标社区按什么标准评价（[第 6 节](#6-动手前读方法说明了解学科规矩)）。
>
> **做到了就往下走：** 证据—方法表每一行都有方法、都过了检查，导师看过，没有根本性的反对。下一步：[形成研究计划](03_research-plan.md)。

## 你现在在哪里

你已经把核心主张拆成了几个研究问题，写好了一份证据清单（见[从研究问题到证据清单](01_question-to-evidence.md)）：每行一个研究问题，写着关键词怎么定义、什么结果算支持、什么算否定。在第一部分的出口，你也大致判断过自己要做哪一类研究（见[判断你要做哪一类研究](../01_find-a-problem/05_converge.md#判断你要做哪一类研究)）。

但这张表还没告诉你：每条证据**具体用什么办法拿**。你可能正在想：

- 导师说"做个实验吧"，可我的问题适合做实验吗？
- 问卷、访谈、挖代码仓库、跑评测，好像都能沾上边，该选哪个？
- 一种方法够不够？要不要几种一起用？
- 选好了方法，怎么知道它真能给出我要的证据？

## 这一阶段要解决什么

为每条证据选定一种（或几种）**研究方法**，并且说得出为什么。研究方法是具体怎么收集和分析证据的做法，它和研究套路的区别见[核心术语](../00_start-here/key-concepts.md#研究方法)。具体来说，是回答下面六个问题：

1. 我的主要套路是什么？它要求哪些证据？
2. 每条证据，用什么方法拿？
3. 这个方法得到了什么，又放弃了什么？
4. 一种方法够不够？要组合的话，怎么组合？
5. 这个方法真的能产出我要的那条证据吗？
6. 动手前，要读哪份方法说明、了解哪些学科规矩？

## 这一章怎么用

按证据清单**一行一行**地走第 2 到第 5 节，最后把结果填进一张"证据—方法表"（见"产出物"）。

这几步也会互相牵连：

- 第 5 节发现某条证据用哪种方法都拿不到 → 回到[从研究问题到证据清单](01_question-to-evidence.md)，换一条能拿到的证据，或者把主张改小；
- 第 3 节发现主方法放弃的正是你的主张最需要的东西 → 回到第 2 节换方法，或在第 4 节补一种方法。

---

## 1. 先确认主要套路

**方法跟着套路走，套路跟着核心主张走。** 你在 1.5 的出口已经初步定过主要套路。怎样按核心主张选出主要套路、几对容易混的套路怎么分，[研究套路](../05_research-strategies/README.md#怎样选出主要套路)里"怎样选出主要套路"一节已经讲清楚了，这里不重复。

这一节只做一件事：**拿套路说明去核对你的证据清单。** 每篇套路说明都有"什么样的证据才够"一节，列出了这种套路通常要交出的证据。逐条对照，看看清单里有没有漏的。

例如，主要套路是[构建改进](../05_research-strategies/build_improve.md)，清单里却没有"和已有方法比较"；主要套路是[解释因果](../05_research-strategies/explain_causality.md)，清单里却没有"排除其他解释"。这些漏项要先补上，否则方法选得再好，也拼不出完整的论证。

八篇套路说明是：[观察描述](../05_research-strategies/observe_describe.md)、[测量](../05_research-strategies/measure.md)、[比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md)、[综合](../05_research-strategies/synthesize.md)、[证明](../05_research-strategies/prove.md)、[解读论证](../05_research-strategies/interpret_argue.md)。每篇的第 3 节还列了这种套路常用的方法，可以作为下一节的起点。

**写下来：** 写出核心主张和主要套路。打开对应的套路说明，把"什么样的证据才够"一节和你的证据清单逐条对照，补上漏掉的证据。

## 2. 按每条证据挑方法

**一条一条地看证据，问：这条证据回答的是哪一类问题？** 方法要和问题吻合。软件工程的方法选择指南这样总结：任何问题都可以用好几种方法研究，选哪种取决于你的立场（你认为什么样的证据才可信）、能拿到的资源，以及方法和问题有多吻合[^easterbrook2008selecting-e76]。

下表按"证据在问什么"列出可以考虑的方法。最后一列是做这种研究的前提条件，**前提不满足，这个方法就先别选**。带脚注的前提条件出自上面那份指南；分类、方法的归属和没有脚注的前提条件，是本手册的归纳：

| 这条证据在问…… | 可以考虑的方法（目前的位置） | 前提条件 |
|---|---|---|
| 一群人里，某种做法、看法有多常见 | [问卷调查](../06_methods/questionnaire_survey.md) | 问题针对一个明确的目标人群；能从定义清楚的总体里抽出有代表性的样本[^easterbrook2008selecting-e81] |
| 大量代码、提交、合约里的分布或关联 | [仓库挖掘](../07_fields/computer-science/practices/repository_mining.md)、[数据科学](../06_methods/data_science.md) | 数据拿得到，分析单元定义清楚 |
| 真实环境里，事情是怎样、为什么发生的 | [案例研究](../06_methods/case_study.md)、[访谈研究](../06_methods/interview_study.md)、[扎根理论](../06_methods/grounded_theory.md) | 有一个关于"怎样""为什么"的清楚研究问题[^easterbrook2008selecting-e12]；能进入现场 |
| 一个群体的工作文化，成员怎样理解自己做的事 | 民族志，见[案例研究](../06_methods/case_study.md#3-民族志有什么不同)第 3 节 | 问题关注这个群体的文化实践，并且能接触到群体成员[^easterbrook2008selecting-e83] |
| 是不是 X 导致了 Y；人用 A 是否比用 B 好 | [对照实验](../06_methods/controlled_experiment.md) | 有一个清楚的假设[^easterbrook2008selecting-e78] |
| 几个软件、工具、模型，谁在什么条件下更好 | [基准评测](../07_fields/computer-science/practices/benchmarking.md) | 有可论证的评测对象和指标 |
| 你新做的东西是否更好 | [工程研究](../07_fields/computer-science/practices/engineering_research.md)、[优化研究](../07_fields/computer-science/practices/optimization_study.md)、[定量仿真](../06_methods/simulation_study.md) | 有能比较的基线 |
| 在一个真实组织里，一边解决问题一边研究 | [行动研究](../06_methods/action_research.md) | 有一个问题的主人，愿意和你一起界定问题、投入解决[^easterbrook2008selecting-e84] |
| 现象怎样随时间变化 | [纵向研究](../06_methods/longitudinal_study.md) | 能在多个时间点跟踪同一批对象 |
| 别人的结论换个条件还成立吗 | [复现研究](../06_methods/replication.md) | 原研究的材料足够详细 |
| 已有研究合起来说明了什么 | [综述研究](../06_methods/review_study.md)、[案例调查](../06_methods/case_survey.md) | 已有研究足够多，值得合起来看 |
| 在给定条件下必然成立 | [理论研究](../07_fields/computer-science/practices/theoretical_research.md) | 能把对象写成精确的定义 |

其他学科常用的方法（田野实验、随机对照试验、档案研究等）也收在[研究类型](../06_methods/README.md)；只有某一个学科使用的做法（如文本细读），见[学科篇](../07_fields/README.md#学科独有的实践)里"学科独有的实践"一节。

挑方法之前，也先查一下文献：有些问题已经有不错的答案，读文献就能回答，不必自己再做一项实证研究[^easterbrook2008selecting-e41]。

**用例子走一遍。** 接着贯穿全书的项目：核心主张是"现有大模型漏洞检测的评测结果被数据泄露高估了"，主要套路是测量。拿上一章的证据清单，逐行配上候选方法：

| 证据 | 它在问 | 候选方法 |
|---|---|---|
| 评测集里有多少合约，模型训练时可能见过 | 多常见 | 数据分析：把评测集和模型可能见过的代码比对 |
| 去掉泄露样本前后，准确率怎么变 | 两种条件下结果差多少 | 基准评测：同一批工具，分别在两版评测集上跑 |
| 是不是只有个别工具受影响 | 能不能推广 | 基准评测，换多个模型和工具 |
| 判断"是否泄露"的办法本身准不准 | 测法可靠吗 | 人工抽查一批样本，和自动判断对照 |

**三个容易犯的错：**

- **从"我会什么"或"别人怎么做"出发选方法。** 盲目照搬别人为完全不同的问题用过的研究范式，会导致严重的错配[^shaw2003writing-e15]。
- **追求"最好的"方法。** 软件工程的实证研究标准只要求方法适合研究目的，不要求是最优的[^ralph2020empirical-e23]。上面那份指南也说，选方法没有固定配方，要看你的资源、能不能接触到研究对象、能不能控制想研究的变量，以及你自己的技能[^easterbrook2008selecting-e42]。
- **前提没满足就开工。** 例如还写不出清楚的假设，就急着做实验。这时更该先做探索性的工作，把假设想清楚。

**写下来：** 把证据清单抄成三列：证据、它在问什么、候选方法。每个候选方法后面写一句：它的前提条件我满足了吗？

## 3. 看清每种方法得到了什么、放弃了什么

**没有十全十美的方法。** 软件工程里有一个常被引用的研究策略框架：每种研究策略在几个质量标准上各有长短，每个设计决定都是在这些标准之间做取舍[^storey2020who-e3]。这几个标准是：

- **推广性**：结论能不能推到更多的人或系统上；
- **真实性**：证据是在多接近真实使用的环境里拿到的；
- **控制**：能不能控制住会干扰证据、又和研究无关的人的行为因素；
- **精度**：收集到的系统数据有多精确。

下表是这个框架里几类做法在这些标准上的典型位置[^storey2020who-e12][^storey2020who-e13][^storey2020who-e14][^storey2020who-e15]，表中的例子是本手册所举：

| 做法 | 计算机里的例子 | 强在 | 弱在 |
|---|---|---|---|
| 实验室实验 | 请研究生在实验室里用两种调试工具完成任务 | 控制 | 真实性（环境是人为布置的），也更难推广 |
| 现场研究 | 不加干预，观察一家公司怎样使用某个工具 | 真实性 | 控制和推广性（通常只涉及少数公司） |
| 现场实验 | 在开发者真实的工作环境里比较两个测试工具 | 比现场研究的控制可能更强 | 比现场研究更有侵入性，真实性降低 |
| 问卷、访谈 | 问很多开发者怎样看代码质量 | 样本广而大时，推广性可能更高 | 真实性：影响每个人回答的因素看不到，也预料不到 |
| 用已有数据 | 挖代码仓库，或在历史数据上评测工具 | 系统数据的精度；数据来自真实现场、来自很多项目时，真实性和推广性也可能较高 | 对人的行为控制低 |

**两组最常遇到的取舍**：

**控制和真实性。** 实验越"干净"，越可能离真实情况远。把关键变量忽略或控制住了，结果就可能推广不到真实环境[^easterbrook2008selecting-e79]。实验证实的也只是你**定义的那个指标**：指南里假设的一位研究者，即使用实验证明了鱼眼视图按她定义的效率更高，也不等于证明了鱼眼视图更适合导航[^easterbrook2008selecting-e80]。放到例子里：在一个整理好的公开评测集上测出泄露带来的差距，不等于别的评测集、真实部署的合约上也有同样大的差距。结论能推广多远、怎样提前防住，见[效度与局限](04_validity-and-limits.md#5-外部效度结论能推广到哪里)。

**深度和广度。** 问卷关心的是一群人总体上怎样；想深入了解人们实际怎样用、为什么不用，案例研究可能更合适[^easterbrook2008selecting-e82]。选案例研究，就是用代表性换少数案例上更深的理解[^easterbrook2008selecting-e19]。环境本身会影响现象，或者影响要很久才显现时，对照实验那种"拆小、隔离变量"的做法就不合适，更适合用案例研究[^easterbrook2008selecting-e16]。

**怎么决定牺牲哪一个？看你的主张最需要哪一个**。贯穿例子是测量类主张，用的是已有的评测数据，最要紧的是精度：泄露判断和检出判定要准；它不涉及人怎样使用工具，真实性可以让一步。如果你的主张是因果的，比如"提供漏洞模式提示**导致**检出率提高"，控制最要紧，真实性可以让一步；主张是"开发者在实际工作中**会用**这个工具"，真实性最要紧，控制可以让一步。也不是每个项目都要把人请进来：例如评估缩短构建时间的新技术，人的反馈帮助不大[^storey2020who-e6]；但一个推荐可能缺陷的工具，可能就要放到真人使用中评估，看它怎样改变使用环境[^storey2020who-e5]。

> **不同的看法：只有实验室实验才可信吗？**
>
> 软件工程的方法选择指南用一个假设的场景描述过这场争论：
>
> - **一方**：导师坚持，只有在受控的实验室条件下做的实验才是可信的证据[^easterbrook2008selecting-e85]。理由是，受控实验能精确地确定变量之间的关系，尤其是有没有因果关系[^easterbrook2008selecting-e78]。
> - **另一方**：场景里的另一位研究者认为，实验室实验没用，因为它忽略了真实软件项目的复杂情况[^easterbrook2008selecting-e85]。研究策略框架也指出，实验室里的控制是以真实性为代价的，结果也更难推广[^storey2020who-e13]。
>
> 指南的解释是：分歧来自立场不同。你采取的立场，影响你认为哪些方法能产生可接受的证据；把立场说明白，也有助于讨论和写作[^easterbrook2008selecting-e86]。
>
> 这个分歧会影响你的操作：先按上面的办法，判断你的主张最需要控制还是真实性；然后在论文里写明你的选择和放弃了什么。软件工程的实证研究标准就把"讨论其他可选的实验设计，以及为什么没用（如效度上的取舍）"列为加分项[^ralph2020empirical-e177]；它还认为，单凭"参与者是学生"去批评一项实验不成立，参与者合不合适要结合情境、需要的控制程度和内外部效度的取舍来判断，但论文必须解释为什么这样选[^ralph2020empirical-e183]。

**写下来：** 对你的主方法，写两句话：它在哪个标准上强、在哪个标准上弱；为什么这个弱点对你的主张来说可以接受。如果写不出"可以接受"的理由，到第 4 节考虑补一种方法。

## 4. 需要时，组合几种方法

**为什么要组合：** 每种方法都有已知的缺陷，但各方法的缺陷不同，所以可以挑几种互相弥补[^easterbrook2008selecting-e1]。结果是否可靠，取决于研究设计把所选方法的短处弥补得怎么样[^easterbrook2008selecting-e77]。

**三种常见的组合方式**（软件工程的方法选择指南介绍的三种混合方法设计）：

| 组合方式 | 怎么做 | 什么时候用 |
|---|---|---|
| 先定量，后定性 | 先收集分析定量数据，再用定性结果解释定量发现 | 定量阶段出现意外结果时特别有用[^easterbrook2008selecting-e4] |
| 先定性，后定量 | 先收集分析定性数据，再用定量结果帮助解读 | 也适合检验定性研究中形成的初步理论[^easterbrook2008selecting-e5] |
| 同时进行，互相印证 | 同时用不同方法，互相确认、交叉验证 | 动机是"人们说的"常常和"人们做的"不一样[^easterbrook2008selecting-e6] |

同时进行的难点是：两种分析的结果可能难以比较，出现矛盾时也难以化解；这时可能需要再找一个证据来源，或者做一项后续研究[^easterbrook2008selecting-e7]。

**组合不一定要换方法。** 即使只用一种方法，也可以用多种数据收集手段互相印证；不同种类的数据支持同一个结论，研究就更有说服力[^easterbrook2008selecting-e9]。前者叫方法三角验证（用不同的策略或方法），后者叫数据三角验证（用同一种方法、不同的数据来源）[^storey2020who-e7]。数据三角验证可能提高推广性，但不能提高真实性[^storey2020who-e8]，详见[效度与局限](04_validity-and-limits.md#5-外部效度结论能推广到哪里)。

放到例子里：用自动比对判断"哪些样本泄露了"，再人工抽查一批样本核对，这是同一项研究里的数据三角验证；想说明"开发者实际上会被高估的结果误导"，就要换一种方法，比如访谈或对照实验。

**组合也有代价。** 数据收集量大，分析多种来源的数据很费时间，还要求研究者同时熟悉定量和定性研究[^easterbrook2008selecting-e3]。所以我们建议：

- **新手可以先把一种方法做扎实。** 在软件工程实证研究标准的通用部分里，"对同一研究问题使用两种及以上的数据收集或分析策略"属于"优秀"项，不是必要项[^ralph2020empirical-e290]。三角验证的责任也不一定落在单篇论文上[^storey2020who-e10]。
- **要组合，就写清为什么、在哪个阶段、起什么作用。** 同一份标准把这几项列为多方法研究的必要项[^ralph2020empirical-e276]。
- **不要为了好看加一个方法。** 其中一种方法只起点缀作用，却把研究包装成混合方法；或者为了迎合审稿人，加一个对发现没有实质贡献的方法：同一份标准把这些列为反面做法[^ralph2020empirical-e282]。

怎样设计和整合，见[混合方法](../06_methods/mixed_methods.md)。

**写下来：** 在证据—方法表里，标出哪条证据只靠一种方法、它最大的弱点是什么。只对弱点正好打中主张的那一两条，写下补充的方法和它起的作用。

## 5. 检查：这个方法真能拿到你要的证据吗

方法选得"对路"还不够。动手前，对每一行证据做下面的检查：

**① 方法的产出，能填进你的结果表吗？** 拿出 1.5 画的[空结果表](../01_find-a-problem/05_converge.md#4-拿什么让人相信)，想象方法做完后得到的东西，看它能不能填进那一格。验证要和主张对应：主张性能提升，就要分析性能，而不是易用性或通用性[^shaw2003writing-e12]。验证方式也要和结果类型、获得结果的方法相匹配，形式化模型要靠严格推导和证明，而不是一两个简单例子[^shaw2003writing-e9]。

**② 方法测到的，是你要的那个东西吗？** 问卷只能告诉你人们**说**自己怎么做，这可能和他们实际怎么做毫无关系[^easterbrook2008selecting-e52]。只分析开发活动留下的痕迹数据（比如提交记录），看到的也只是人的行为、意图和社会互动的一部分[^storey2020who-e1]。你的证据如果是关于"实际怎么做"，就要换方法，或者补一个来源。

**③ 你拿得到需要的东西吗？** 例子里，"评测集有多少样本模型见过"这条证据，最直接的做法是和模型的训练数据比对。如果模型的训练数据不公开，这个方法就做不了，得换一条证据或换一种办法，比如只用训练数据公开的模型，或只用模型发布后才出现的合约。在企业里做研究，还要考虑：进入现场可能要花很长时间和对方建立关系，对方才会提供具体的项目数据[^easterbrook2008selecting-e25]；为了换取进入的机会，你通常要放弃一部分控制，获得发表许可也可能很难[^easterbrook2008selecting-e26]。

**④ 时间和技能够吗？** 以定量为主的方法，比如对照实验和问卷调查，比纯定性的方法需要更多规划时间，统计检验也要事先定好[^easterbrook2008selecting-e88]。如果这是你第一次用某种方法，算上学习的时间，见第 6 节。

**⑤ 先小规模试一下。** 新手通常应当先试用数据收集工具，而且不只试收集，也试分析步骤[^easterbrook2008selecting-e89]。怎样安排这种小规模试做，见[最小可跑版本](05_pilot-and-derisk.md)。

现实条件常常会迫使你改变原来的设计，包括方法、数据收集和分析步骤。改的时候，记下原计划和之后的每一处改动[^easterbrook2008selecting-e87]。

**写下来：** 在证据—方法表里加一列"检查结果"。每行写一句：方法的产出能填进哪一格、需要的东西能不能拿到。有一行不过关，先处理这一行，再往下走。

## 6. 动手前，读方法说明，了解学科规矩

**先读这类研究的已有指南。** 动手做一项研究，却没有读过、没有理解、没有用上这类研究已发表的指南，被软件工程的实证研究标准列为反面做法[^ralph2020empirical-e26]。用了某种分析技术，就要遵守那种技术的规则[^shaw2003writing-e13]。新手要熟悉自己选的技术，知道可能遇到的陷阱[^easterbrook2008selecting-e89]；真正用上之前，可能还需要进一步学习，甚至专门训练[^easterbrook2008selecting-e90]。

**按什么顺序找**：

1. 本手册里对应的方法文件（第 2 节表格里的链接），先了解步骤和常见错误；
2. 文件"延伸阅读"里列出的方法指南或标准，正式设计时对照着用；
3. 你想投的会议或期刊最近两三年里、主张和你相近的三五篇论文，看它们用了什么方法、报告了什么。只拿来对照，不要照搬（见第 2 节）。

**找不到专门的指南怎么办？** 软件工程实证研究标准的规定是：有合适的专门标准才套用它；没有，就按已发表的指南；连合适的指南也没有，审稿人就用通用标准，并为这种新方法临时建一套评价办法[^ralph2020empirical-e441]。对你来说，就是在论文里写清楚：你按什么标准判断自己的研究做得好不好。

**为什么非读不可：** 同一份标准明确说，没有通用的质量标准，每项研究都按适合它的方法的标准来评价[^ralph2020empirical-e24]（套路层面的说明见[核心术语](../00_start-here/key-concepts.md#研究套路)）。你不知道自己的方法用什么标准评价，就既不知道该做到什么程度，也没法回应用错标准的审稿意见。这份标准还把下面这些审稿意见列为不成立的批评：用另一种研究范式的规范来批评，批评某类研究固有的局限（例如说案例研究推广性低），只因为审稿人自己会用别的方法就否定研究[^ralph2020empirical-e25]。

**再看学科规矩。** 方法说明讲"怎么做好"，学科规矩讲"这个社区接受什么"。要了解的至少有：

| 要了解的 | 去哪里看 |
|---|---|
| 你所在的方向惯用什么方法、什么样的评估 | [计算机学科概况](../07_fields/computer-science/README.md#各方向的惯例不一样) |
| 是否要求提交可复现的代码和数据 | [制品评估与徽章](../07_fields/computer-science/README.md#制品评估与徽章) |
| 研究涉及人，或者会发现真实系统的漏洞时，有哪些伦理要求 | [伦理问题有本领域的特点](../07_fields/computer-science/README.md#伦理问题有本领域的特点)；通用原则见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人) |
| 其他学科的规矩 | [学科篇](../07_fields/README.md)里各学科的概况 |

**写下来：** 对每种选定的方法，写下你要读的一份方法说明或指南，以及打算对照的两三篇论文。再写一句：这个方法在你的目标社区里，通常按什么标准评价。

> **不同类型的研究，这一步有什么不同**
>
> - **实证研究**（见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)）：方法要撑得住数据规模，并说明为什么这样选。He 等 2020 要处理近 1000 万个合约[^he2020characterizing-e6]，选了轻量的指纹比对，理由是要能扩展到这个规模，而且合约逻辑简单，用不着更重的程序分析[^he2020characterizing-e8]。
> - **工具或方法论文**（见[工程研究](../07_fields/computer-science/practices/engineering_research.md)）：方法的核心是"和谁比、比什么"。Slither 与三个开源工具对比，写明每个工具的版本，并且只比各工具都有的重入漏洞检测[^feist2019slither-e6]。
> - **基准或数据集**（见[基准评测](../07_fields/computer-science/practices/benchmarking.md)）：要先定下评测哪些对象。SmartBugs 先找到 35 个工具，再按写明的纳入标准筛出 9 个[^durieux2020empirical-e4]。
> - **综述**（见[综述研究](../06_methods/review_study.md)）：方法就是一份事先写好的综述方案。Rameder 等 2022 按 Kitchenham 和 Charters 2007 等几份指南制定方案，为的是结果全面、可重复[^rameder2022review-e4]。

---

## 关键判断

**选不定方法时，怎么办？** 可以这样判断：

| 遇到的情况 | 通常的做法 |
|---|---|
| 两种方法都能拿到这条证据 | 选前提更容易满足、你更熟悉的那个；论文里写明为什么没选另一个 |
| 最合适的方法做不了（数据拿不到、找不到人、没有现场） | 先找能支撑同类结论的其他证据；找不到，就把主张改小 |
| 主方法的弱点正好打中核心主张 | 补一种能弥补这个弱点的方法，或者把主张限定在主方法能支撑的范围 |
| 导师要的方法和你判断的不一样 | 拿出你的证据—方法表，讨论每条证据靠什么拿；分歧常常来自对主张的理解不同 |
| 写不出清楚的假设，却打算做实验 | 先做探索性的工作，比如访谈、人工读一批样本，把假设想清楚 |
| 想加一种方法，只是为了让审稿人满意 | 不加；先问它为哪条证据服务 |

**什么时候算选好了？** 不是"找到了最好的方法"，而是证据清单的每一行都有方法，前提满足，产出能填进结果表，弱点你说得出来，也说得出为什么可以接受。

## 常见错误

没有脚注的理由是本手册的归纳。

| 错误 | 为什么是问题 |
|---|---|
| 先定方法，再找能说明什么 | 选方法要看它和问题有多吻合[^easterbrook2008selecting-e76]；先定方法，容易做完才发现撑不起主张 |
| 照搬上一篇论文的方法 | 问题不同，方法可能严重错配[^shaw2003writing-e15] |
| 用一两个例子"验证"形式化的结论 | 形式化模型要靠严格推导和证明[^shaw2003writing-e9] |
| 证据和主张对不上 | 主张性能提升，却只展示了易用性[^shaw2003writing-e12] |
| 用问卷回答"人们实际怎么做" | 人们说的可能和做的毫无关系[^easterbrook2008selecting-e52] |
| 把实验室里的结果直接说成真实环境里的结论 | 被控制住的变量在真实环境里可能很重要[^easterbrook2008selecting-e79] |
| 为了显得严谨，硬凑混合方法 | 点缀性的方法对发现没有实质贡献，软件工程的实证研究标准把它列为反面做法[^ralph2020empirical-e282] |
| 没读方法指南就动手 | 软件工程的实证研究标准把它列为反面做法[^ralph2020empirical-e26]；你也不知道该按什么标准做到位 |
| 改了方法却不留记录 | 原计划和之后的每一处改动都应当记下来[^easterbrook2008selecting-e87]；不记，事后说不清结果是在什么设计下得到的 |

## 产出物

- 一张**证据—方法表**：每行一条证据，列出它在问什么、选定的方法、前提是否满足、方法的强项和弱点、检查结果（第 2、3、5 节）
- 需要组合方法时，一段说明：组合了哪几种、各在哪个阶段、起什么作用（第 4 节）
- 一份阅读清单：每种方法要读的指南和要对照的论文（第 6 节）

## 检查点

满足下面几条，可以进入下一步：

- [ ] 写出了主要套路，并按套路说明核对过证据清单，没有漏项
- [ ] 证据清单的每一行都有选定的方法，前提条件都满足
- [ ] 能说出主方法在控制、真实性、推广性、精度上的强弱，以及为什么弱点可以接受
- [ ] 组合方法的，每种方法都说得出为哪条证据服务
- [ ] 每种方法的产出都能填进空结果表里的某一格
- [ ] 需要的数据、对象、现场都确认拿得到
- [ ] 每种方法都找到了要读的方法说明或指南，知道它按什么标准评价
- [ ] 导师看过证据—方法表，没有根本性的反对

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 某条证据用哪种方法都拿不到 | [从研究问题到证据清单](01_question-to-evidence.md)，换一条能拿到的证据 |
| 能拿到的证据只撑得起一个弱得多的主张 | [收敛成项目](../01_find-a-problem/05_converge.md)第 1 节，改写主张 |
| 核对套路说明时发现，主张其实属于另一种套路 | [研究套路](../05_research-strategies/README.md#怎样选出主要套路)里"怎样选出主要套路"一节，重新定主要套路，再回到本章第 1 节 |
| 所选方法要学的东西太多，估计时间排不开 | 下一章[形成研究计划](03_research-plan.md#5-估时间并把余量留出来)排时间时算上学习时间；还是排不开，回到本章换一种更熟悉的方法 |

## 下一步

证据和方法都定了，下一步是排时间：把证据清单变成里程碑，定下先做什么、每步要多久、什么时候交。见[形成研究计划](03_research-plan.md)。

[^easterbrook2008selecting-e1]: Easterbrook 等人 2008，§1.0。[证据](../../sources/notes/easterbrook2008selecting.md#e1)
[^easterbrook2008selecting-e3]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e3)
[^easterbrook2008selecting-e4]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e4)
[^easterbrook2008selecting-e5]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e5)
[^easterbrook2008selecting-e6]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e6)
[^easterbrook2008selecting-e7]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e7)
[^easterbrook2008selecting-e9]: Easterbrook 等人 2008，§6.0。[证据](../../sources/notes/easterbrook2008selecting.md#e9)
[^easterbrook2008selecting-e12]: Easterbrook 等人 2008，§5.2。[证据](../../sources/notes/easterbrook2008selecting.md#e12)
[^easterbrook2008selecting-e16]: Easterbrook 等人 2008，§5.2。[证据](../../sources/notes/easterbrook2008selecting.md#e16)
[^easterbrook2008selecting-e19]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e19)
[^easterbrook2008selecting-e25]: Easterbrook 等人 2008，Practical Considerations。[证据](../../sources/notes/easterbrook2008selecting.md#e25)
[^easterbrook2008selecting-e26]: Easterbrook 等人 2008，Practical Considerations。[证据](../../sources/notes/easterbrook2008selecting.md#e26)
[^easterbrook2008selecting-e41]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e41)
[^easterbrook2008selecting-e42]: Easterbrook 等人 2008，§1.0。[证据](../../sources/notes/easterbrook2008selecting.md#e42)
[^easterbrook2008selecting-e76]: Easterbrook 等人 2008，§5.0。[证据](../../sources/notes/easterbrook2008selecting.md#e76)
[^easterbrook2008selecting-e77]: Easterbrook 等人 2008，§5.0。[证据](../../sources/notes/easterbrook2008selecting.md#e77)
[^easterbrook2008selecting-e78]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e78)
[^easterbrook2008selecting-e79]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e79)
[^easterbrook2008selecting-e80]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e80)
[^easterbrook2008selecting-e81]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e81)
[^easterbrook2008selecting-e52]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e52)
[^easterbrook2008selecting-e82]: Easterbrook 等人 2008，§5.3。[证据](../../sources/notes/easterbrook2008selecting.md#e82)
[^easterbrook2008selecting-e83]: Easterbrook 等人 2008，§5.4。[证据](../../sources/notes/easterbrook2008selecting.md#e83)
[^easterbrook2008selecting-e84]: Easterbrook 等人 2008，§5.5。[证据](../../sources/notes/easterbrook2008selecting.md#e84)
[^easterbrook2008selecting-e85]: Easterbrook 等人 2008，§3.0。[证据](../../sources/notes/easterbrook2008selecting.md#e85)
[^easterbrook2008selecting-e86]: Easterbrook 等人 2008，§3.0。[证据](../../sources/notes/easterbrook2008selecting.md#e86)
[^easterbrook2008selecting-e87]: Easterbrook 等人 2008，Practical Considerations。[证据](../../sources/notes/easterbrook2008selecting.md#e87)
[^easterbrook2008selecting-e88]: Easterbrook 等人 2008，Practical Considerations。[证据](../../sources/notes/easterbrook2008selecting.md#e88)
[^easterbrook2008selecting-e89]: Easterbrook 等人 2008，§6.0。[证据](../../sources/notes/easterbrook2008selecting.md#e89)
[^easterbrook2008selecting-e90]: Easterbrook 等人 2008，Conclusions。[证据](../../sources/notes/easterbrook2008selecting.md#e90)
[^storey2020who-e1]: Storey 等人 2020，§2。[证据](../../sources/notes/storey2020who.md#e1)
[^storey2020who-e3]: Storey 等人 2020，§3.3。[证据](../../sources/notes/storey2020who.md#e3)
[^storey2020who-e5]: Storey 等人 2020，§6.2。[证据](../../sources/notes/storey2020who.md#e5)
[^storey2020who-e6]: Storey 等人 2020，§6.2。[证据](../../sources/notes/storey2020who.md#e6)
[^storey2020who-e7]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e7)
[^storey2020who-e8]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e8)
[^storey2020who-e10]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e10)
[^storey2020who-e12]: Storey 等人 2020，§3.3.1。[证据](../../sources/notes/storey2020who.md#e12)
[^storey2020who-e13]: Storey 等人 2020，§3.3.2。[证据](../../sources/notes/storey2020who.md#e13)
[^storey2020who-e14]: Storey 等人 2020，§3.3.3。[证据](../../sources/notes/storey2020who.md#e14)
[^storey2020who-e15]: Storey 等人 2020，§3.3.4。[证据](../../sources/notes/storey2020who.md#e15)
[^ralph2020empirical-e23]: ACM SIGSOFT 实证研究标准，General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e23)
[^ralph2020empirical-e24]: ACM SIGSOFT 实证研究标准，General Standard，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e25]: ACM SIGSOFT 实证研究标准，General Standard，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e26]: ACM SIGSOFT 实证研究标准，General Standard，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e26)
[^ralph2020empirical-e177]: ACM SIGSOFT 实证研究标准，Experiments 标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e177)
[^ralph2020empirical-e183]: ACM SIGSOFT 实证研究标准，Experiments 标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e183)
[^ralph2020empirical-e276]: ACM SIGSOFT 实证研究标准，Multi-Methodology and Mixed Methods 标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e276)
[^ralph2020empirical-e282]: ACM SIGSOFT 实证研究标准，Multi-Methodology and Mixed Methods 标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e282)
[^ralph2020empirical-e290]: ACM SIGSOFT 实证研究标准，General Standard，Extraordinary Attributes。[证据](../../sources/notes/ralph2020empirical.md#e290)
[^ralph2020empirical-e441]: ACM SIGSOFT 实证研究标准，General Standard，Examples of Acceptable Deviations。[证据](../../sources/notes/ralph2020empirical.md#e441)
[^shaw2003writing-e9]: Shaw 2003，§4.1。[证据](../../sources/notes/shaw2003writing.md#e9)
[^shaw2003writing-e12]: Shaw 2003，§4.3。[证据](../../sources/notes/shaw2003writing.md#e12)
[^shaw2003writing-e13]: Shaw 2003，§4.3。[证据](../../sources/notes/shaw2003writing.md#e13)
[^shaw2003writing-e15]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e15)
[^he2020characterizing-e6]: He 等 2020（以太坊合约代码克隆），§4.1 Dataset、§4.2 Pre-processing，第 8 页。[证据](../../sources/notes/he2020characterizing.md#e6)
[^he2020characterizing-e8]: He 等 2020（以太坊合约代码克隆），§3 Methodology，第 5 页。[证据](../../sources/notes/he2020characterizing.md#e8)
[^feist2019slither-e6]: Feist 等 2019（智能合约静态分析工具 Slither），§V-A Vulnerability Detection Evaluation，第 5 页。[证据](../../sources/notes/feist2019slither.md#e6)
[^durieux2020empirical-e4]: Durieux 等 2020（智能合约分析工具评测 SmartBugs），§2.2 Subject Tools，第 2–3 页。[证据](../../sources/notes/durieux2020empirical.md#e4)
[^rameder2022review-e4]: Rameder 等 2022（以太坊智能合约漏洞分析的系统综述），§2 Systematic Review，第 2 页。[证据](../../sources/notes/rameder2022review.md#e4)
