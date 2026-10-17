# 数据科学研究：用预测或统计建模从已有数据中得出新结论

本文讲**数据科学研究**：对已有数据做预测建模或统计建模，用建模结果回答一个科学问题。例如"能不能根据代码变更的特征，预测哪次提交会引入缺陷"；也包括在其他学科里用机器学习做科研，例如用模型预测内战或疾病。

相近的几篇：数据怎样从代码仓库、缺陷库里挖出来，见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)；比较现有工具或模型谁更好，见[基准评测](../07_fields/computer-science/practices/benchmarking.md)；提出新的学习方法或工具，见[工程研究](../07_fields/computer-science/practices/engineering_research.md)。基线怎么选，见[构建改进：尽早把基线跑起来](../05_research-strategies/build_improve.md#尽早把基线跑起来)；测试数据为什么只用一次、怎样对待随机性，见[比较评估：留一份数据只用于最后检验](../05_research-strategies/compare_evaluate.md#留一份数据只用于最后检验)和[比较评估：差异是不是真的](../05_research-strategies/compare_evaluate.md#差异是不是真的)；统计的一般做法见[分析与解读：报告差多少、有多确定，而不只是 p 值](../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。这些是各类研究共通的内容，本文只讲数据科学特有的部分。

**适用范围**：本文的检查清单主要依据 ACM SIGSOFT（美国计算机协会软件工程分会）为软件工程写的数据科学标准，很多例子来自软件工程、系统安全和机器学习。防数据泄漏的部分依据跨学科的资料：REFORMS 清单由计算机、社会科学、生物医学等领域的研究者共同制定，数据泄漏的调查覆盖 17 个领域（见第 2 节）。其他学科用预测或统计建模做研究时，这部分可以直接参考；统计建模和报告的其他要求，先看本学科的规范，例如健康领域用观察数据研究病因时，见[观察性流行病学研究](observational_epidemiology.md)。

**常服务的套路**：[观察描述](../05_research-strategies/observe_describe.md)（对已有数据集做探索性分析）。

**读完本文，你应该能：**

- 分清自己要"预测"还是要"解释"，写清主张针对的总体；
- 认出并防住最常见的数据泄漏，包括时间泄漏和重复样本；
- 用"笨"基线、公平调参和与决策对应的指标评估模型；
- 不把相关说成因果，不把推测说成结论；
- 用 SIGSOFT 标准和 REFORMS 清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为：用机器学习等以数据为中心的方法分析软件工程现象或制品的研究，适用于主要用预测性建模分析已有现象的研究[^ralph2020empirical-e188][^ralph2020empirical-e189]。跨学科的 REFORMS 清单（Recommendations for Machine-learning-based Science，基于机器学习的科学研究建议）说得更直接：这类研究**把模型的表现当作科学主张的证据**[^kapoor2024reforms-e1]。

关键在于：**成果是关于世界的结论，而不是模型本身。** 如果重点是工具本身，而不是工具得出的新结论，SIGSOFT 建议改用别的标准[^ralph2020empirical-e189]。商业中的预测分析也不同：它的目标总体可以不明确，找到的关系只要在本公司内成立即可[^kapoor2024reforms-e27]；科研则要说清结论推广到哪个总体（见第一步）。

**和相近类型的区别**（本手册根据各篇的定义整理）：

| | 数据科学研究 | 仓库挖掘 | 基准评测 | 工程研究 |
|---|---|---|---|---|
| 主要贡献 | 从数据和模型中得出的新结论 | 数据集，以及描述性、关系性的统计 | 对现有系统或模型的比较 | 新方法、新工具 |
| 典型问题 | "X 能预测到什么程度？" | "多普遍？和什么相关？" | "A 和 B 谁更好？" | "我的新工具解决问题了吗？" |

一项研究常常跨两类：先挖数据再建模。数据收集部分照[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)做，建模和评估部分照本文做。

### 先分清：你要预测，还是要解释

REFORMS 借用 Breiman 的"两种文化"[^kapoor2024reforms-e3]：

- **解释**（数据建模文化，传统统计）：估计能代表真实生成过程的参数，回答"X 和 Y 是什么关系、有多大"。
- **预测**（算法建模文化，多数机器学习研究）：在训练时没见过的新样本上准确预测，参数不必有解释意义。

两者的证据不同：解释看参数估计，预测看模型在新数据上的表现。REFORMS 的大部分条目针对预测，不适用于解释性建模[^kapoor2024reforms-e4]。例如"代码评审人数和缺陷率是什么关系"是解释问题；"给定一次提交的特征，能多准地预测它是否引入缺陷"是预测问题。**预测得准，不等于弄清了原因**，见第八步。

---

## 2. 怎么做

问题非常普遍：一项跨学科调查在 17 个领域发现了数据泄漏，涉及 294 篇论文，有的结论严重过于乐观[^kapoor2023leakage-e1]。作者强调这只是问题的下限，而且代码里的错误光读论文是看不出来的[^kapoor2023leakage-e2]。对 30 篇安全顶会机器学习论文的分析发现，每篇至少有三个陷阱[^arp2022dos-e3]。

### 第一步：写清主张、目标总体和结果变量

**怎么做：**

- **写下目标总体**：结论想推广到哪个群体或哪种数据，例如"开源 Java 项目的提交"还是"某一家公司的提交"。论文常常不写这一条[^kapoor2024reforms-e5]。
- **说清结果变量代表什么。** 被预测的变量通常只是某个看不见的理论概念的替代指标[^kapoor2024reforms-e6]。例如用"后来被修复的变更"代表"缺陷"，二者并不等同。
- **说明为什么现在适合用这个方法研究这个问题**[^ralph2020empirical-e207]。

### 第二步：弄清数据的来源和质量

**怎么做：**

- 说明数据怎样选、为什么选，怎样预处理、过滤[^ralph2020empirical-e190]。具体说明这份数据为什么适合你的问题，"这是能找到的最好数据集"不算理由[^kapoor2024reforms-e7]。
- **不要因为一个数据集被很多论文用过，就认为它质量好**[^lones2021avoid-e19]。重度依赖数据的研究要时刻警惕数据质量[^menzies2019bad-e11]。
- 逐项检查：数据是否代表真实分布（抽样偏差）[^arp2022dos-e11]；标签是否有噪声[^arp2022dos-e10]；有没有重复样本；离群值是错误还是真实的极端值[^lones2021avoid-e20]。
- **亲自看数据。** 人工抽查相当一部分数据，是 SIGSOFT 标准的加分项[^ralph2020empirical-e199]。
- 排除了哪些样本，要写明理由：选哪个子集会大大影响模型表现[^kapoor2024reforms-e10]。同一个体占多行时，分别报告个体数和行数[^kapoor2024reforms-e9]。

**容易错在哪**：以为数据量大就没问题。抽样框（实际能抽到的那份名单）没有代表性时，样本越大只会让置信区间越窄，偏差并不减少[^kapoor2024reforms-e8]。

### 第三步：先划分数据，再做任何处理

**数据泄漏**（data leakage）是指在数据收集、抽样、预处理或建模过程中人为造成的、特征和结果之间的虚假关系，例如测试数据的信息混进了训练[^kapoor2024reforms-e15]。它常发生，是因为研究者建模时能接触到全部数据[^kapoor2023leakage-e3]。最常见的几类：

| 类型 | 例子 | 怎么防 |
|---|---|---|
| 预处理用了全部数据 | 在全部数据上做归一化[^kapoor2024reforms-e15]、缩放或填补缺失值[^lones2021avoid-e18]、特征选择[^kapoor2023leakage-e4] | 先划分；所有统计量只用训练数据算；交叉验证时每一折分别处理[^kapoor2024reforms-e11] |
| 测试集被"改造"了 | 为平衡类别对测试数据也做了下采样或过采样 | 重采样只用于训练数据，测试数据保持真实的样子[^ralph2020empirical-e204] |
| 时间泄漏 | 要预测未来，测试集里却有比训练集更早的数据[^kapoor2023leakage-e5]；对时间序列直接用标准交叉验证[^lones2021avoid-e22] | 按时间划分：早的训练，晚的测试 |
| 重复和依赖 | 重复样本被随机分到两边[^kapoor2024reforms-e18]；同一病人的多条记录分在训练集和测试集[^lones2021avoid-e21] | 先去重；按个体（病人、用户、项目）分组划分[^kapoor2024reforms-e17] |
| 不合法的特征 | 败血症模型用"是否开了抗生素"作特征，而抗生素通常确诊后才开[^kapoor2024reforms-e16] | 对每个特征问：真正预测时能拿到它吗？特征越多越要逐个查[^kapoor2024reforms-e19] |
| 用测试集做决定 | 在测试数据上调参数或定阈值[^arp2022dos-e7]；用全部数据的统计量去除离群值[^arp2022dos-e4] | 见第五步 |
| 测试集不代表目标总体 | 只用一个地区的数据测试，却声称在其他地区也适用[^kapoor2023leakage-e7] | 写清测试集来自哪里，结论只说到那里 |

在软件工程里，时间泄漏的典型情形是用较新版本的数据训练、去"预测"较旧版本的缺陷；依赖的典型情形是同一项目的数据同时出现在训练集和测试集，而主张却是"能推广到新项目"。

**为什么值得这样较真：** 一项内战预测的复现研究中，12 篇论文里有错误的 4 篇，恰好是声称复杂模型胜过逻辑回归基线的 4 篇；改正泄漏后，复杂模型并不比几十年前的逻辑回归好多少[^kapoor2023leakage-e8]。

**怎么做：** 项目一开始就划出测试集，只在最后用一次，理由见上表"用测试集做决定"一行和第五步。论文里要论证没有泄漏，这个举证责任在你[^kapoor2023leakage-e9]；可以用 Kapoor & Narayanan 提出的"模型信息表"逐类自查[^kapoor2023leakage-e10]。用知名公开数据集时还要注意：它的特点已被研究透，方法会不知不觉地利用测试数据的知识，最好再在更新的数据上做实验[^arp2022dos-e5]。大语言模型训练时可能见过公开基准的测试集（数据污染），怎样检查见[基准评测：基准本身有效吗](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗)。

### 第四步：从"笨"基线开始比

怎样公平比较的一般原则，见[比较评估：什么样的证据才够](../05_research-strategies/compare_evaluate.md#2-什么样的证据才够)。数据科学研究里特别要做的：

- **先算"笨"基线**（不学习任何东西的朴素模型）。永远预测多数类的模型，准确率可以是 50% 也可以是 90%，全看类别比例[^lones2021avoid-e23]；回归中总是预测"不变"的模型也可能得高分[^lones2021avoid-e24]。不先算出这些数字，就不知道自己的模型好在哪。
- **再比简单模型**，例如逻辑回归。先跑很简单的算法，能很快了解问题的大致结构[^menzies2019bad-e16]。在软件工程中，很多数据集结构简单，简单方法和深度学习效果一样甚至更好[^menzies2019bad-e15]；上面内战预测的例子也是教训。
- **最后比当前最好的方法**，或说明为什么没有、为什么无法直接比较，这是 SIGSOFT 的必要项[^ralph2020empirical-e191]。用多种不同类型的学习器处理数据，是加分项[^ralph2020empirical-e196]。

### 第五步：调参要公平，选模型不碰测试集

**怎么做：**

- **给每个被比较的方法同样的调参投入**，原因见[比较评估：什么样的证据才够](../05_research-strategies/compare_evaluate.md#2-什么样的证据才够)中"对手是否被同等对待"。机器学习里要特别注意：很多算法的默认设置本身就不好[^menzies2019bad-e13]，所以"对手用默认设置"往往就是弱基线；基线没有用和新方法同样的方法挑选和调参，也会成为"弱基线"[^kapoor2024reforms-e14]。
- **报告调参细节**[^kapoor2024reforms-e28]，例如搜索了哪些超参数、用什么方法、花了多少资源。投入多少会明显影响结果，换一组超参数，两个方法的优劣可能反过来[^kapoor2024reforms-e13]。
- **调参和挑模型只用训练数据和验证数据。** 在留出集上试多个模型、挑最好的，会高估表现。要另留一份测试集；数据少时用嵌套交叉验证（外层估计表现，内层调参挑模型）[^kapoor2024reforms-e12]。

> **不同的看法：用不用网格搜索？**
> - SIGSOFT 标准把"认真选择超参数"列为加分项，举的例子包括参考相关工作的设置，或用网格搜索等自动优化方法[^ralph2020empirical-e198]。
> - Menzies & Shepperd 强烈反对网格搜索：慢，而且可能漏掉重要的优化；他们建议用差分进化等很简单的优化器[^menzies2019bad-e14]。
>
> 实际操作中：用哪种调参方法是次要的，关键是每个被比较的方法得到同样的调参预算，并在论文里写清楚。

### 第六步：选和实际决策对应的指标

**怎么做：**

1. **先写下模型的结果会被拿去做什么决定**，再选指标，并在论文里说明理由[^ralph2020empirical-e192]。
2. **类别不平衡时不要只看准确率**[^kapoor2024reforms-e20]。只看 ROC 曲线（以假阳性率为横轴、真阳性率为纵轴的曲线）可能显得很好，精确率却很低[^arp2022dos-e9]。
3. **对照基础比率解读结果。** 真阳性率 99%、假阳性率 1% 看似很好，但正负样本比为 1:100 时，每 99 个真阳性就伴随 100 个假阳性[^arp2022dos-e8]。
4. **考虑不同错误的代价。** 有的领域里某些错误比其他错误代价高[^kapoor2024reforms-e20]。例如缺陷预测的结果用来分配测试人力时，误报太多会浪费人力，漏报太多则失去意义。

### 第七步：报告波动和不确定性

一般原则（重复多次、报告分布、效应量）见[分析与解读：报告差多少、有多确定](../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。数据科学研究的具体要求：

- 不能只给平均数或中位数，要有波动、置信度等分布信息[^ralph2020empirical-e192]。
- 用不同的随机训练/测试划分多次运行（例如交叉验证），再用显著性检验和效应量检验比较[^ralph2020empirical-e197]。反面模式是：不检查前提就用统计检验；只报显著性不报效应量；报效应量不给置信区间[^ralph2020empirical-e205]。
- 没有现成方法时，可以在测试集内做自助法（bootstrap，有放回地重复抽样）得到置信区间[^kapoor2024reforms-e21]。REFORMS 认为，报告不确定性比只做统计检验更好[^kapoor2024reforms-e22]。

这一步常被省略：上述内战预测研究中，12 篇论文有 9 篇比较模型时既没做检验，也没量化不确定性[^kapoor2023leakage-e11]。

### 第八步：解释结果——相关不等于因果

**怎么做：**

- **不轻易声称因果。** SIGSOFT 把下面这种情况列为反面模式：只确立了共变和先后顺序，没有排除第三变量的解释、也没有提出产生机制的假设，就声称因果[^ralph2020empirical-e203]。例如从大量项目中看到某种编码风格更容易出缺陷，只是相关；要相信因果，还需要主动改变编码风格的后续实验[^menzies2019bad-e10]。做不了因果推断时不做因果主张，不算缺陷[^ralph2020empirical-e206]。
- **查一查模型学到的是不是你以为的东西。** 模型可能抓住和任务相关、但与任务本身无关的痕迹（虚假相关）[^arp2022dos-e6]。一个恶意软件检测实验中，"play.google.com"这个网址成了判定正常应用最重要的特征之一，分类器学会的是区分应用来源，而不是区分恶意与正常[^arp2022dos-e12]。模型越复杂，越容易过拟合虚假相关[^lones2021avoid-e25]。研究的目的不是准确率比别人高一点，而是产生理解，所以要看看模型到底学到了什么[^lones2021avoid-e26]，例如查看最重要的特征、逐个分析出错的样本。
- **把结果和推测分开**（一般做法见[分析与解读：负面结果和意外结果](../02_do-the-project/07_analyze-and-interpret.md#5-负面结果和意外结果)）。结果好时尤其容易随意加入没有证据的说法[^lipton2019troubling-e15]。SIGSOFT 认为，通常把结果和讨论分成两节、结果一节不写推测就够了[^ralph2020empirical-e200]。
- **写清结论在哪里不成立。** 这能设定清楚的预期，避免炒作[^kapoor2024reforms-e24]。即使模型现在表现好，数据分布随时间变化后也可能变差[^kapoor2024reforms-e23]。

### 第九步：让别人能复现

**怎么做：**

- 描述特征工程、建模方法（通常用伪代码）和硬件软件环境，这是 SIGSOFT 的必要项[^ralph2020empirical-e193]。
- 提供数据、代码、环境、说明文档和一键生成结果的复现脚本[^kapoor2024reforms-e26]；数据不能公开时，提供合成数据演示算法用法[^ralph2020empirical-e195]。记录随机种子等细节，见[整理科研材料：每个结果都要能追溯到它是怎么来的](../08_throughout/organizing_materials.md#3-每个结果都要能追溯到它是怎么来的)。
- **投稿前用 REFORMS 自查。** 它有 32 个问题，由计算机、社会科学、生物医学等领域的 19 位研究者共同制定[^kapoor2024reforms-e2]；不要求逐项照做，由你判断哪些和本研究相关[^kapoor2024reforms-e25]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 数据科学标准；"防泄漏"三项依据 REFORMS。SIGSOFT 标准面向软件工程，其他方向可以按需选用。

**必须做到**

- [ ] 说明为什么现在适合用这个方法研究这个问题[^ralph2020empirical-e207]
- [ ] 说明数据怎样选、为什么选，怎样预处理、过滤和分类[^ralph2020empirical-e190]
- [ ] 描述特征工程、建模方法和软硬件环境[^ralph2020empirical-e193]
- [ ] 讨论当前最好的基线，或说明为什么没有、为什么无法直接比较[^ralph2020empirical-e191]
- [ ] 论证所用的统计量和启发式规则；讨论数据科学特有的假设和效度威胁[^ralph2020empirical-e194]
- [ ] 说明并论证评估指标；结果给出波动或置信度，不只给平均数[^ralph2020empirical-e192]
- [ ] 论证预处理和建模只用了训练数据；说明怎样处理训练集和测试集之间的依赖和重复；论证每个特征都合法（REFORMS）[^kapoor2024reforms-e29]

**做到更好**

- [ ] 提供复现包；数据不能公开时提供合成数据[^ralph2020empirical-e195]
- [ ] 用多种不同类型的学习器[^ralph2020empirical-e196]
- [ ] 多次随机划分训练/测试数据，用显著性检验和效应量检验比较[^ralph2020empirical-e197]
- [ ] 认真选择超参数[^ralph2020empirical-e198]
- [ ] 人工抽查相当一部分数据[^ralph2020empirical-e199]
- [ ] 清楚区分有证据的结果和解读、推测[^ralph2020empirical-e200]

**做得出色**[^ralph2020empirical-e201]

- [ ] 用纵向分析利用时间数据
- [ ] 对部分样本做定性分析，或用问卷、访谈等其他数据相互印证
- [ ] 把发现告诉被研究制品的创建者，征求反馈

**这些情况可以不做，不算缺陷**[^ralph2020empirical-e202]

- 数据规模太大时，用关键词匹配、随机抽样等较粗的处理
- 数据太大或太敏感时不公开
- 纯描述性的研究不做统计检验和假设

**审稿时常见、但不成立的批评**[^ralph2020empirical-e206]

- "你应该分析另一份数据"：该问的是主张是否被所分析的数据支持
- "没有复现包"：目前是加分项，不是必要项
- "没有做因果主张"：做不了，就不该做

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不写目标总体和结果变量的含义 | 读者无法判断结论能推广到哪里[^kapoor2024reforms-e5][^kapoor2024reforms-e6] |
| 在全部数据上做归一化、填补缺失值或特征选择，之后才划分 | 测试数据的信息漏进了训练，结果虚高[^kapoor2024reforms-e15][^kapoor2023leakage-e4] |
| 对时间数据随机划分 | 模型用到了"来自未来"的信息[^kapoor2023leakage-e5] |
| 同一个人、同一项目的数据分在训练集和测试集两边 | 训练和测试不独立，构成泄漏[^kapoor2023leakage-e6] |
| 用了实际预测时拿不到的特征 | 特征其实是结果的替代品[^kapoor2024reforms-e16] |
| 不和"笨"基线、简单模型比 | 看不出模型是否真的学到了东西[^lones2021avoid-e23][^kapoor2023leakage-e8] |
| 在测试集上调参、挑模型 | 高估表现[^arp2022dos-e7][^kapoor2024reforms-e12] |
| 类别不平衡时只报准确率或 ROC 曲线 | 掩盖大量误报[^arp2022dos-e8][^arp2022dos-e9] |
| 只报一个平均数 | 看不出差异是不是噪声[^ralph2020empirical-e192][^ralph2020empirical-e205] |
| 从相关直接跳到因果 | 没有排除第三变量和其他解释[^ralph2020empirical-e203] |
| 不看模型学到了什么 | 可能学到的是虚假相关[^arp2022dos-e12] |

---

## 5. 延伸阅读

- **REFORMS**（Kapoor 等人 2024）：跨学科的 32 项清单，每项配有说明和文献，适合投稿前逐项自查。
- **数据泄漏**：Kapoor & Narayanan 2023，8 类泄漏的分类、模型信息表和内战预测的完整复现案例。
- **机器学习陷阱入门**：Lones 的指南按"建模前、建模、评估、比较、报告"组织，适合新手通读；Arp 等人 2022 针对安全领域，附有数据窥探类型表。
- **软件工程中的数据分析**：Menzies & Shepperd 2019 列出软件分析论文的"坏味道"，适合审稿和自查。
- **SIGSOFT 数据科学标准**：本文检查清单的来源，原文还列出了推荐阅读和范例论文。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e188]: SIGSOFT 数据科学标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e188)
[^ralph2020empirical-e189]: SIGSOFT 数据科学标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e189)
[^ralph2020empirical-e190]: SIGSOFT 数据科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e190)
[^ralph2020empirical-e191]: SIGSOFT 数据科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e191)
[^ralph2020empirical-e192]: SIGSOFT 数据科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e192)
[^ralph2020empirical-e193]: SIGSOFT 数据科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e193)
[^ralph2020empirical-e194]: SIGSOFT 数据科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e194)
[^ralph2020empirical-e195]: SIGSOFT 数据科学标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e195)
[^ralph2020empirical-e196]: SIGSOFT 数据科学标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e196)
[^ralph2020empirical-e197]: SIGSOFT 数据科学标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e197)
[^ralph2020empirical-e198]: SIGSOFT 数据科学标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e198)
[^ralph2020empirical-e199]: SIGSOFT 数据科学标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e199)
[^ralph2020empirical-e200]: SIGSOFT 数据科学标准，加分项及脚注 8。[证据](../../sources/notes/ralph2020empirical.md#e200)
[^ralph2020empirical-e201]: SIGSOFT 数据科学标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e201)
[^ralph2020empirical-e202]: SIGSOFT 数据科学标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e202)
[^ralph2020empirical-e203]: SIGSOFT 数据科学标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e203)
[^ralph2020empirical-e204]: SIGSOFT 数据科学标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e204)
[^ralph2020empirical-e205]: SIGSOFT 数据科学标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e205)
[^ralph2020empirical-e206]: SIGSOFT 数据科学标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e206)
[^ralph2020empirical-e207]: SIGSOFT 数据科学标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e207)
[^kapoor2024reforms-e1]: Kapoor 等人 2024，The scope of our claims。[证据](../../sources/notes/kapoor2024reforms.md#e1)
[^kapoor2024reforms-e2]: Kapoor 等人 2024，摘要。[证据](../../sources/notes/kapoor2024reforms.md#e2)
[^kapoor2024reforms-e3]: Kapoor 等人 2024，Module 1，1c。[证据](../../sources/notes/kapoor2024reforms.md#e3)
[^kapoor2024reforms-e4]: Kapoor 等人 2024，The scope of our claims，Explanatory modeling。[证据](../../sources/notes/kapoor2024reforms.md#e4)
[^kapoor2024reforms-e5]: Kapoor 等人 2024，Module 1，1a。[证据](../../sources/notes/kapoor2024reforms.md#e5)
[^kapoor2024reforms-e6]: Kapoor 等人 2024，Module 3，3d。[证据](../../sources/notes/kapoor2024reforms.md#e6)
[^kapoor2024reforms-e7]: Kapoor 等人 2024，Module 3，3c。[证据](../../sources/notes/kapoor2024reforms.md#e7)
[^kapoor2024reforms-e8]: Kapoor 等人 2024，Module 3，3e。[证据](../../sources/notes/kapoor2024reforms.md#e8)
[^kapoor2024reforms-e9]: Kapoor 等人 2024，Module 3，3e。[证据](../../sources/notes/kapoor2024reforms.md#e9)
[^kapoor2024reforms-e10]: Kapoor 等人 2024，Module 4，4a。[证据](../../sources/notes/kapoor2024reforms.md#e10)
[^kapoor2024reforms-e11]: Kapoor 等人 2024，Module 4，4c。[证据](../../sources/notes/kapoor2024reforms.md#e11)
[^kapoor2024reforms-e12]: Kapoor 等人 2024，Module 5，5d。[证据](../../sources/notes/kapoor2024reforms.md#e12)
[^kapoor2024reforms-e13]: Kapoor 等人 2024，Module 5，5e。[证据](../../sources/notes/kapoor2024reforms.md#e13)
[^kapoor2024reforms-e14]: Kapoor 等人 2024，Module 5，5f。[证据](../../sources/notes/kapoor2024reforms.md#e14)
[^kapoor2024reforms-e15]: Kapoor 等人 2024，Module 6。[证据](../../sources/notes/kapoor2024reforms.md#e15)
[^kapoor2024reforms-e16]: Kapoor 等人 2024，Module 6。[证据](../../sources/notes/kapoor2024reforms.md#e16)
[^kapoor2024reforms-e17]: Kapoor 等人 2024，Module 6，6b。[证据](../../sources/notes/kapoor2024reforms.md#e17)
[^kapoor2024reforms-e18]: Kapoor 等人 2024，Module 6，6b。[证据](../../sources/notes/kapoor2024reforms.md#e18)
[^kapoor2024reforms-e19]: Kapoor 等人 2024，Module 6，6c。[证据](../../sources/notes/kapoor2024reforms.md#e19)
[^kapoor2024reforms-e20]: Kapoor 等人 2024，Module 7，7a。[证据](../../sources/notes/kapoor2024reforms.md#e20)
[^kapoor2024reforms-e21]: Kapoor 等人 2024，Module 7，7b。[证据](../../sources/notes/kapoor2024reforms.md#e21)
[^kapoor2024reforms-e22]: Kapoor 等人 2024，Module 7，7c。[证据](../../sources/notes/kapoor2024reforms.md#e22)
[^kapoor2024reforms-e23]: Kapoor 等人 2024，Module 8，8a。[证据](../../sources/notes/kapoor2024reforms.md#e23)
[^kapoor2024reforms-e24]: Kapoor 等人 2024，Module 8，8b。[证据](../../sources/notes/kapoor2024reforms.md#e24)
[^kapoor2024reforms-e25]: Kapoor 等人 2024，Table 1 说明。[证据](../../sources/notes/kapoor2024reforms.md#e25)
[^kapoor2024reforms-e26]: Kapoor 等人 2024，Module 2。[证据](../../sources/notes/kapoor2024reforms.md#e26)
[^kapoor2024reforms-e27]: Kapoor 等人 2024，The scope of our claims，Predictive analytics。[证据](../../sources/notes/kapoor2024reforms.md#e27)
[^kapoor2024reforms-e28]: Kapoor 等人 2024，Table 1，5e、5f。[证据](../../sources/notes/kapoor2024reforms.md#e28)
[^kapoor2024reforms-e29]: Kapoor 等人 2024，Table 1，6a–6c。[证据](../../sources/notes/kapoor2024reforms.md#e29)
[^kapoor2023leakage-e1]: Kapoor & Narayanan 2023，Summary。[证据](../../sources/notes/kapoor2023leakage.md#e1)
[^kapoor2023leakage-e2]: Kapoor & Narayanan 2023，Results。[证据](../../sources/notes/kapoor2023leakage.md#e2)
[^kapoor2023leakage-e3]: Kapoor & Narayanan 2023，Leakage in modeling competitions。[证据](../../sources/notes/kapoor2023leakage.md#e3)
[^kapoor2023leakage-e4]: Kapoor & Narayanan 2023，泄漏分类 L1.3。[证据](../../sources/notes/kapoor2023leakage.md#e4)
[^kapoor2023leakage-e5]: Kapoor & Narayanan 2023，泄漏分类 L3.1。[证据](../../sources/notes/kapoor2023leakage.md#e5)
[^kapoor2023leakage-e6]: Kapoor & Narayanan 2023，泄漏分类 L3.2。[证据](../../sources/notes/kapoor2023leakage.md#e6)
[^kapoor2023leakage-e7]: Kapoor & Narayanan 2023，泄漏分类 L3.3。[证据](../../sources/notes/kapoor2023leakage.md#e7)
[^kapoor2023leakage-e8]: Kapoor & Narayanan 2023，Summary 与内战预测案例。[证据](../../sources/notes/kapoor2023leakage.md#e8)
[^kapoor2023leakage-e9]: Kapoor & Narayanan 2023，Model info sheets。[证据](../../sources/notes/kapoor2023leakage.md#e9)
[^kapoor2023leakage-e10]: Kapoor & Narayanan 2023，Summary。[证据](../../sources/notes/kapoor2023leakage.md#e10)
[^kapoor2023leakage-e11]: Kapoor & Narayanan 2023，内战预测案例。[证据](../../sources/notes/kapoor2023leakage.md#e11)
[^arp2022dos-e3]: Arp 等人 2022，摘要。[证据](../../sources/notes/arp2022dos.md#e3)
[^arp2022dos-e4]: Arp 等人 2022，§2，P3。[证据](../../sources/notes/arp2022dos.md#e4)
[^arp2022dos-e5]: Arp 等人 2022，§2，P3。[证据](../../sources/notes/arp2022dos.md#e5)
[^arp2022dos-e6]: Arp 等人 2022，§2，P4。[证据](../../sources/notes/arp2022dos.md#e6)
[^arp2022dos-e7]: Arp 等人 2022，§2，P5。[证据](../../sources/notes/arp2022dos.md#e7)
[^arp2022dos-e8]: Arp 等人 2022，§2，P8。[证据](../../sources/notes/arp2022dos.md#e8)
[^arp2022dos-e9]: Arp 等人 2022，§2，P7。[证据](../../sources/notes/arp2022dos.md#e9)
[^arp2022dos-e10]: Arp 等人 2022，§2，P2。[证据](../../sources/notes/arp2022dos.md#e10)
[^arp2022dos-e11]: Arp 等人 2022，§2，P1。[证据](../../sources/notes/arp2022dos.md#e11)
[^arp2022dos-e12]: Arp 等人 2022，§4.1。[证据](../../sources/notes/arp2022dos.md#e12)
[^lones2021avoid-e18]: Lones 2021，§3.1。[证据](../../sources/notes/lones2021avoid.md#e18)
[^lones2021avoid-e19]: Lones 2021，§2.2。[证据](../../sources/notes/lones2021avoid.md#e19)
[^lones2021avoid-e20]: Lones 2021，§2.4。[证据](../../sources/notes/lones2021avoid.md#e20)
[^lones2021avoid-e21]: Lones 2021，§4.4。[证据](../../sources/notes/lones2021avoid.md#e21)
[^lones2021avoid-e22]: Lones 2021，§4.8。[证据](../../sources/notes/lones2021avoid.md#e22)
[^lones2021avoid-e23]: Lones 2021，§4.6，图 6。[证据](../../sources/notes/lones2021avoid.md#e23)
[^lones2021avoid-e24]: Lones 2021，§4.6。[证据](../../sources/notes/lones2021avoid.md#e24)
[^lones2021avoid-e25]: Lones 2021，§3.8。[证据](../../sources/notes/lones2021avoid.md#e25)
[^lones2021avoid-e26]: Lones 2021，§6.5。[证据](../../sources/notes/lones2021avoid.md#e26)
[^menzies2019bad-e10]: Menzies & Shepperd 2019，§1。[证据](../../sources/notes/menzies2019bad.md#e10)
[^menzies2019bad-e11]: Menzies & Shepperd 2019，§4.3。[证据](../../sources/notes/menzies2019bad.md#e11)
[^menzies2019bad-e13]: Menzies & Shepperd 2019，§4.10。[证据](../../sources/notes/menzies2019bad.md#e13)
[^menzies2019bad-e14]: Menzies & Shepperd 2019，§4.10。[证据](../../sources/notes/menzies2019bad.md#e14)
[^menzies2019bad-e15]: Menzies & Shepperd 2019，§4.11。[证据](../../sources/notes/menzies2019bad.md#e15)
[^menzies2019bad-e16]: Menzies & Shepperd 2019，§4.11。[证据](../../sources/notes/menzies2019bad.md#e16)
[^lipton2019troubling-e15]: Lipton & Steinhardt 2019，§4.1。[证据](../../sources/notes/lipton2019troubling.md#e15)
