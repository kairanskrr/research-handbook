# 建一个数据集或基准：把数据集本身作为研究成果

本文讲**数据集论文**和**基准论文**（dataset paper、benchmark paper，有时也叫资源论文 resource paper）：论文的主要贡献不是一个新方法，而是你新建的一个数据集或基准，别人可以拿去训练模型、评测工具或做研究。

本文只讲**怎样建、怎样发布**。拿一个基准去比较系统、工具或模型，怎样公平地比、怎样报告结果，见[基准评测](../07_fields/computer-science/practices/benchmarking.md)；检查一个已有基准是否测到了想测的东西、有没有数据污染，见其中[基准本身有效吗](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗)一节。本文用到这些内容时链接过去，不再重复。

**适用范围**：本文的做法主要来自机器学习（数据表、NeurIPS 数据集与基准分会的征稿要求、Raji 等人对"通用基准"的批评、BetterBench 的基准质量标准）和软件工程（ACM SIGSOFT 的基准评测标准，智能合约基准 SmartBugs 作范例）。跨学科的数据发表规范来自 FAIR 数据原则和 Scientific Data 期刊的投稿指南，后者覆盖自然科学、医学等多个学科。其他学科建数据集时，先看本学科的数据期刊、数据仓库和伦理规范。心理学以测量工具本身为成果的研究，见[量表编制与测量研究](scale_development.md)。

**常服务的套路**：[测量](../05_research-strategies/measure.md)、[比较评估](../05_research-strategies/compare_evaluate.md)。

**读完本文，你应该能：**

- 判断你的贡献是否适合写成数据集或基准论文，并说清为什么需要它；
- 设计收集和抽样方案，组织标注，并检验标注的一致性；
- 划分数据，堵住训练集和测试集之间的泄漏，减少数据污染；
- 写出数据表，处理好许可、同意和伦理问题；
- 把数据集发布到能长期获取的地方，并规划维护、版本和退役；
- 知道审稿人会查什么。

---

## 1. 这是什么研究，什么时候用

机器学习方向常把**基准**定义为：一个或几个数据集（至少有测试数据）加一个指标，被视为代表某些具体任务或能力，并被研究社区当作比较方法的共同框架[^raji2021everything-e1]。软件工程的 SIGSOFT 标准要求，提出新基准的论文写清四件事：要测的质量、量化它的指标、测量方法、被测系统要处理的工作负载或任务样本[^ralph2020empirical-e147]。**数据集**的范围更宽：不一定配指标，可以用来训练、分析或做别的研究。

这类论文在不少地方有专门的发表渠道。机器学习顶会 NeurIPS 设有数据集与基准分会；它的说法是，主要贡献是新数据集或基准时，最好按这类成果的标准来审，主会的审稿重点是算法、分析和应用[^neurips2024datasets-e13]。Scientific Data 期刊专门发表"数据描述"（Data Descriptor），描述存放在数据仓库中的数据集，同样经过同行评审[^scientificdata2026guidelines-e10]。

**它擅长回答的问题**：

- **某类工具没法在同一标准下比较。** SmartBugs 的出发点是：很多智能合约分析工具能拿到，但各自用的数据集拿不到，研究难以比较和复现[^durieux2020empirical-e1]。它的贡献里有两个数据集：一个人工标注的漏洞合约集，一个从以太坊上收集的大规模合约集[^durieux2020empirical-e2]。
- **现有数据检验不了你想检验的主张**：例如现有评测集太小、标注错得多、已经被模型做满，或者很可能被模型训练时见过。
- **一个领域缺少共同的"尺子"**：大家各用各的数据，结论之间无法对照。

如果你只是为了评估自己的新方法顺手收了一批数据，主要贡献仍是方法，见[工程研究](../07_fields/computer-science/practices/engineering_research.md)；数据集的构建过程照本文写清楚即可。

**和相近方法的区别**：

| | 数据集或基准论文 | 基准评测 | 仓库挖掘研究 | 量表编制 |
|---|---|---|---|---|
| 主要成果 | 数据集或基准本身 | 关于系统、工具或模型谁更好的结论 | 关于软件开发现象的结论 | 测量工具本身 |
| 数据从哪来 | 自己收集、整理、标注 | 用现有基准（或自建） | 从代码仓库、缺陷库等挖出来 | 编题、施测 |
| 读者拿它做什么 | 下载、复用、在上面比较 | 读结论 | 读结论 | 拿量表去测人 |
| 去哪里看 | 本文 | [基准评测](../07_fields/computer-science/practices/benchmarking.md) | [仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md) | [量表编制与测量研究](scale_development.md) |

> **不同的看法：数据集论文要不要报告分析结果？**
>
> - **Scientific Data 的数据描述：不要。** 这种论文不写结果、讨论和分析，因为它的根本目的是不带偏见地描述数据集的技术内容，鼓励别人使用[^scientificdata2026guidelines-e6]。但要有"技术验证"一节，写支持数据质量的实验、分析或检查[^scientificdata2026guidelines-e7]。
> - **机器学习的基准论文：通常要跑出参照结果。** NeurIPS 要求基准论文的补充材料保证所有结果都容易复现[^neurips2024datasets-e6]；BetterBench 建议给出指标的下限、上限、人类水平和随机水平，帮读者理解一个分数意味着什么[^reuel2024betterbench-e6]，并提供复现论文结果的脚本[^reuel2024betterbench-e8]。
>
> 实际操作中：先看你投的地方属于哪种传统。投数据期刊，就把精力放在方法、数据记录和技术验证上；投机器学习会议的基准分会，就要跑几个有代表性的基线，让读者知道这个基准有多难、能不能分出高下。

---

## 2. 怎么做

BetterBench 给 24 个常用人工智能基准打分后认为，基准做得不好，多半不是故意的，而是因为不知道好基准应该是什么样[^reuel2024betterbench-e15]。它把一个基准的一生分成设计、实现、文档、维护、退役五个阶段[^reuel2024betterbench-e3]；数据表把数据集的生命周期分成动机、组成、收集过程、预处理/清洗/标注、用途、分发、维护七组问题[^gebru2021datasheets-e5]。下面的步骤按这个顺序排。

### 第一步：说清为什么需要这个数据集

**怎么做：**

1. **回答数据表的第一组问题**：为什么建这个数据集？针对什么任务？填补了什么空白[^gebru2021datasheets-e7]？
2. **把"要测什么"落到任务上。** 定义被测的能力，说明它怎样转化成基准里的任务，以及在现实中有什么用[^reuel2024betterbench-e4]。设计时考虑谁会用、怎么用，请领域专家参与，结合领域文献[^reuel2024betterbench-e5]。
3. **讲清和已有数据集、基准的区别**，让使用者能判断它适不适合自己的用途[^reuel2024betterbench-e4]。
4. **范围要具体。** Raji 等人主张，基准应当按它本来的用途开发、介绍和理解：评估具体的、范围清楚、有语境的任务[^raji2021everything-e8]。

**为什么：** 基准任务未必对应任何人真正关心的问题。Raji 等人引用 Wagstaff 的话：大批机器学习研究者追逐最好的鸢尾花、蘑菇分类器，但这对植物学和真菌学似乎没有任何影响[^raji2021everything-e4]。

**容易错在哪：**

- **宣称测的是"通用能力"。** 没有中立的数据集，基准能说明的东西有限；宣称"通用"常常成了不报告局限的挡箭牌[^raji2021everything-e5]。
- **把夸奖写进论文。** Scientific Data 要求背景部分说明为什么建这个数据集、别人可能怎样重用，但不要写关于新颖性、影响或用处的主观宣称[^scientificdata2026guidelines-e2]。

**例子**：贯穿全书的项目怀疑"现有大模型漏洞检测的评测结果被数据泄露高估了"。要检验它，需要一批模型训练时**不可能见过**的合约。于是动机可以写成："现有公开的智能合约漏洞评测集很可能出现在模型的训练数据里，无法区分'模型会检测'和'模型背过答案'；我们收集在被测模型训练截止日期之后才部署的合约，人工标注漏洞，作为对照评测集。"这样，数据集就是项目里[证据清单](../02_do-the-project/01_question-to-evidence.md)的一行，而不是一个独立的副产品。

**写下来：** 用三句话写：这个数据集要支持什么任务或主张；现有数据为什么不够；和最接近的两个已有数据集差在哪里。

### 第二步：决定收什么、怎样抽样

**怎么做：**

1. **收集前先读数据表"组成"和"收集过程"两组问题**，收集完再回答[^gebru2021datasheets-e8]。提前读，你才知道收集时要记录什么。
2. **说清样本和总体。** 数据集是全部实例，还是从更大集合里抽的样本？是样本的话，那个更大的集合是什么，样本有没有代表性[^gebru2021datasheets-e9]？
3. **记下时间。** 数据是什么时间段收集的，和数据本身产生的时间是否一致（例如最近才抓取的旧新闻）[^gebru2021datasheets-e20]。对防污染的评测集来说，这一条是核心证据。
4. **每条数据都能追溯来源。** SmartBugs 的标注集来自 GitHub 仓库、分析合约的博客和以太坊链上三个来源，并为每个合约记录来源网址和作者[^durieux2020empirical-e6]。用了持续更新的数据源时，给出版本号或检索词，详细到别人能找到同样的输入、重做一遍[^scientificdata2026guidelines-e4]。
5. **说清数据集是否依赖外部资源**（网站、推文、其他数据集），这些资源以后还在不在[^gebru2021datasheets-e11]。
6. **规模要够分出高下。** BetterBench 建议，基准应能可靠地检测出 1% 的提升[^reuel2024betterbench-e12]；Jason Wei 建议大模型评测集最好至少有 1000 个样本，选择题形式的更多[^wei2024evals-e2]。规模和标注质量之间要取舍：ImageNet 的作者也说，规模已经限制了能拿到多少人工标注[^raji2021everything-e9]。

**为什么：** 数据来源的偏向会直接进入基准。ImageNet 2011 年版中，45% 的图片来自美国，六成以上来自北美和欧洲的少数西方国家[^raji2021everything-e6]。

**容易错在哪：** 手头有什么就收什么。Raji 等人批评一些"通用"基准的任务更像方便样本：建基准的团队容易拿到什么就用什么，即使理论上站不住[^raji2021everything-e3]。

### 第三步：标注，并检验一致性

标注的一般流程（写标注规则、多人独立标注、解决分歧、报告一致性）已在[仓库挖掘研究：人工标注，并检验一致性](../07_fields/computer-science/practices/repository_mining.md#第六步人工标注并检验一致性)里写过，这里只列建数据集时最要紧的几点。

**怎么做：**

1. **用多名标注者，报告人数，详细描述标注流程，评估标注者之间的一致性**[^ralph2020empirical-e111]。说明分歧怎么解决，用合适的统计量报告一致性[^ralph2020empirical-e129]。只算"百分之多少一致"不够，因为它没扣除碰巧一致的部分[^mcdonald2019reliability-e4]。
2. **标注类别尽量用公认的分类。** SmartBugs 用现成的 DASP 十类漏洞分类，每个合约归入一类，并人工标出漏洞所在的代码行[^durieux2020empirical-e5]。作者承认人工标注可能标错，应对办法是全体作者各自标注，再讨论分歧达成一致[^durieux2020empirical-e14]。
3. **不要用被评测的方法来做标准答案。** BetterBench 转述生物信息学的基准文献：被评估的方法不应被用来制作标准答案数据集[^reuel2024betterbench-e19]。比如你要评测大模型和 Slither 查漏洞的能力，就不能让大模型或 Slither 直接生成"正确答案"；如果用工具做初筛，必须每条都由人复核，并在论文里写明。
4. **写明谁标的、拿了多少报酬**（例如众包工人的报酬）[^gebru2021datasheets-e13]。
5. **保存原始数据，公开标注用的软件。** 数据表会问：处理后的数据之外，是否保存了原始数据？预处理、清洗、标注用的软件是否公开[^gebru2021datasheets-e15]？

**为什么：** 评测集里错误多了，就没人信它[^wei2024evals-e3]。

**容易错在哪：** 一致性低于公认阈值却说成"良好"；算了好几种一致性指标，只报最好看的那个[^ralph2020empirical-e132]。

### 第四步：划分数据，堵住泄漏和污染

**怎么做：**

1. **给出推荐的训练、验证、测试划分，并说明理由**[^gebru2021datasheets-e10]。为什么测试数据只能在最后用一次，见[比较评估：留一份数据只用于最后检验](../05_research-strategies/compare_evaluate.md#留一份数据只用于最后检验)；先划分、再做任何处理的道理，见[数据科学研究](data_science.md#第三步先划分数据再做任何处理)。
2. **先去重，再划分。** 公开数据里的重复可能非常多：SmartBugs 的大规模数据集去掉空格和制表符后按哈希判重，发现 95% 的源码是重复的[^durieux2020empirical-e8]。训练样本和测试样本不独立就构成泄漏[^kapoor2023leakage-e6]，所以近似重复的样本要放在同一侧。
3. **按时间切。** 要预测未来时，测试集里不能有早于训练集的数据[^kapoor2023leakage-e5]。
4. **为评测集加防污染措施。** 给评测样本加全局唯一标识或加密，能降低污染和被"刷分"的风险；附一个检测任务，可以判断模型训练数据是否含有基准样本[^reuel2024betterbench-e7]。也可以同时准备公开和私有两份测试集，监测模型在两者上的表现是否明显不同[^wei2024evals-e9]。

**为什么：** 好的评测发布后，题目会扩散到网上各处[^wei2024evals-e9]。建基准的人无法强迫模型开发者遵守"金丝雀字符串"（嵌在数据里、提醒不要拿去训练的标记）；防止污染是建基准者和模型开发者的共同责任[^reuel2024betterbench-e16]。怎样事后检查一个模型有没有见过评测集，见[基准评测：基准本身有效吗](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗)。

**例子**：在本项目的对照评测集里，同一份合约常被大量复制部署。可以先把代码相同或几乎相同的合约归成一组，整组只出现在一侧；再按部署日期，把被测模型训练截止日期之后的合约划为测试集。论文里写清两种划分规则和各自去掉了多少样本。

> **不同的看法：静态基准还是动态基准？**
>
> - 动态基准（持续加入新题目）更能应对很快被做满和数据污染的问题，但不同时间的结果更难互相比较[^reuel2024betterbench-e13]。
> - 静态基准便于比较，但有些基准发布几个月就被做满了[^reuel2024betterbench-e17]。
>
> 实际操作中：多数研究者先发布一个固定版本，让论文里的数字可比；同时把收集和标注流程写成脚本，以后能按同样规则出新版本。

### 第五步：写文档（数据表）

**怎么做：**

1. **为数据集写一份数据表**：记录它的动机、组成、收集过程、推荐用途等[^gebru2021datasheets-e1]。NeurIPS 数据集与基准分会要求新数据集提交文档和预期用途，推荐的框架包括数据表、数据营养标签、自然语言处理的数据声明、数据卡等[^neurips2024datasets-e3]。
2. **边做边写，不要事后补。** 数据表的目的是让建数据集的人认真反思创建、分发、维护的过程和风险，也让使用者有足够信息决定用不用[^gebru2021datasheets-e2]，所以不应该自动生成[^gebru2021datasheets-e4]。不适用的问题可以跳过[^gebru2021datasheets-e5]，但答不全也要尽量多答，而不是干脆不写[^gebru2021datasheets-e6]。
3. **写明不该用来做什么**[^gebru2021datasheets-e16]，写明背后的规范性假设和局限[^reuel2024betterbench-e9]。
4. **把文件讲清楚。** 托管在哪个仓库、有哪些文件和格式、目录结构，并解释用户看不懂的列名和变量名[^scientificdata2026guidelines-e5]。
5. **提供机器可读的元数据。** NeurIPS 2025 要求用 Croissant 格式（一种机器可读的数据集描述格式）记录数据集，随论文提交[^neurips2025datasets-e3]。

**为什么：** 数据表还有助于复现：拿不到原数据的人，可以照数据表的信息建一个特征相似的替代数据集[^gebru2021datasheets-e3]。

**论文怎么组织**：可以参考 Scientific Data 的数据描述结构：背景与概述、方法、数据记录、数据概览（可选）、技术验证、使用说明（可选）、数据可获取性、代码可获取性[^scientificdata2026guidelines-e1]。方法部分要完整说明实验设计、数据采集和所有计算处理[^scientificdata2026guidelines-e3]。机器学习会议的基准论文结构更自由，但这几块内容审稿人同样会找。

### 第六步：处理许可、同意和伦理

研究涉及人时的一般要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)；从公开平台挖数据的伦理和许可问题见[仓库挖掘研究：处理伦理和许可问题](../07_fields/computer-science/practices/repository_mining.md#第八步处理伦理和许可问题)。建数据集还要注意下面几点。

**怎么做：**

1. **从宽判断"涉及人"。** 数据表建议：只要数据集含有人写的文字，就算涉及人[^gebru2021datasheets-e12]。按这个标准，代码注释、提交说明、问答帖子都算。
2. **"能下载"不等于"能用"。** 仅以"技术上能访问、能下载"为理由使用数据，是 SIGSOFT 列出的反面模式[^ralph2020empirical-e135]。再次发布数据时，要说明怎样尊重数据主体的预期和同意[^ralph2020empirical-e138]。
3. **查清上游的限制。** 第三方是否对你收进来的数据施加了知识产权或其他限制[^gebru2021datasheets-e17]？把公开数据集收进自己的基准，也要检查它们的伦理问题；这些数据的伦理后果仍由你负责[^neurips2024datasets-e11]。还要了解并遵守所在地区对数据的法律要求[^neurips2024datasets-e15]。
4. **选定许可证。** NeurIPS 要求作者必须选一个许可证，数据集最好用知识共享（CC）许可，代码用开源许可[^neurips2024datasets-e4]。许可和使用条款应考虑预期用途和局限，防止滥用[^neurips2024datasets-e9]。
5. **涉及真实的人时，取得同意。** 数据集应尽量少暴露能识别个人的信息；用真实的人的真实数据，要征得明确同意，或说明为什么做不到[^neurips2024datasets-e10]。数据表还会问怎样征得同意[^gebru2021datasheets-e14]、是否经过伦理审查[^gebru2021datasheets-e13]。

**敏感数据不一定要全部公开。** FAIR 原则指出，高度敏感或能识别个人的数据，即使本身不公开，只要公开详细的元数据和获取规则，也能达到较高的 FAIR 程度[^wilkinson2016fair-e5]。NeurIPS 允许出于公共利益确有必要时（如伦理敏感的医疗数据）要求用户先取得资格再访问，但这只是例外，不能借此限制获取[^neurips2024datasets-e12]。

**容易错在哪**：从 GitHub 收代码时只看"公开"，不看各仓库的开源许可证是否允许再分发。拿不准时，只发布仓库地址、提交哈希和下载脚本，让使用者自己下载。

### 第七步：发布，并保证能长期拿到

**怎么做：**

1. **审稿时就要能拿到。** NeurIPS 2025 要求投稿时数据和代码就能被审稿人获取，不用私下找负责人要；代码要有文档、能运行；做不到可以直接拒稿[^neurips2025datasets-e1]。Scientific Data 第一轮审稿要求数据能被匿名下载，从第二轮起必须公开存放在正式的数据仓库[^scientificdata2026guidelines-e8]。
2. **放到专门的数据平台或数据仓库。** NeurIPS 2025 要求新数据集托管在 Dataverse、Kaggle、Hugging Face、OpenML 等专门的机器学习数据平台，确有需要时才用专门的网站[^neurips2025datasets-e2]。要说明数据集能长期获取：上传到数据仓库，或说明你自己怎样保证[^neurips2024datasets-e4]。
3. **申请永久标识符。** 强烈建议给数据集一个可解析的永久标识符，例如数据仓库分配的 DOI[^neurips2024datasets-e5]。FAIR 原则的第一条就是数据和元数据要有全球唯一、长期有效的标识符[^wilkinson2016fair-e3]；发布时还要附明确的使用许可和详细的来源信息[^wilkinson2016fair-e4]。
4. **基准要连评测代码一起发。** 提供能运行的评测代码、评测数据或提示词，以及复现论文结果的脚本[^reuel2024betterbench-e8]；以可直接使用的形式提供基准，方便别人独立复现[^ralph2020empirical-e151]。代码、数据和结果怎样组织，见[整理科研材料](../08_throughout/organizing_materials.md)。

**为什么：** 这些要求常被忽视。BetterBench 评估的 24 个基准中，17 个没有提供容易运行的复现脚本；14 个没有对同一模型多次评测，也没报告显著性或不确定性[^reuel2024betterbench-e14]。

### 第八步：维护、版本和退役

**怎么做：**

1. **事先写好维护计划**：会不会更新（修正标注错误、增删实例），多久一次，由谁负责，怎样通知用户；旧版本是否继续保留[^gebru2021datasheets-e18]。NeurIPS 要求新数据集提交托管、许可和维护计划[^neurips2024datasets-e3]。
2. **留反馈渠道和联系人，定期检查代码还能不能用**[^reuel2024betterbench-e10]。
3. **改了就升版本。** 小的更新（如删掉有错的题）用版本号标明；大的更新要发布新版本[^reuel2024betterbench-e11]。每个新版本都附上更新后的数据表[^gebru2021datasheets-e19]。
4. **该退役时说清楚。** 基准被做满、任务不再重要或出现更好的替代时，就会被淘汰[^reuel2024betterbench-e3]；不再维护时，要在官方发布物里声明已退役[^reuel2024betterbench-e10]。

**例子**：本项目的对照评测集发布为 v1.0。之后有人通过反馈渠道报告三个合约的漏洞行号标错了，修正后发 v1.1，在更新日志里列出改了哪几条；以后的论文写明用的是哪个版本。等新一代模型的训练截止日期晚于这批合约的部署时间，这个版本就失去了"没见过"的意义，应该声明它不再适合做防污染评测，并按同样规则收集新一批合约。

---

## 3. 检查清单

下面主要依据 NeurIPS 数据集与基准分会的要求、数据表和 BetterBench 的标准，用 SIGSOFT 基准评测标准补充。这些都是机器学习和软件工程的要求；投其他学科的数据期刊时，以该期刊的规定为准。

**必须做到**

- [ ] 说明为什么建这个数据集、填补什么空白[^gebru2021datasheets-e7]，和已有基准有什么区别[^reuel2024betterbench-e4]
- [ ] 新基准写清要测的质量、指标、测量方法和工作负载[^ralph2020empirical-e147]
- [ ] 足够详细地说明数据怎样收集和组织、包含什么信息、将怎样提供和维护[^neurips2024datasets-e8]
- [ ] 提交数据集文档和预期用途，以及托管、许可和维护计划[^neurips2024datasets-e3]
- [ ] 选定明确的许可证，并说明长期保存方案[^neurips2024datasets-e4]
- [ ] 审稿时数据和代码就能获取，不用私下申请[^neurips2025datasets-e1]
- [ ] 涉及真实的人：尽量少暴露个人信息，取得明确同意或说明为什么做不到[^neurips2024datasets-e10]
- [ ] 有人工标注：多名标注者、写清流程、评估一致性[^ralph2020empirical-e111]
- [ ] 讨论构念效度：基准是否测到了要测的东西[^ralph2020empirical-e100]
- [ ] 基准的结果容易复现[^neurips2024datasets-e6]

**做到更好**

- [ ] 申请永久标识符（如 DOI）[^neurips2024datasets-e5]
- [ ] 提供机器可读的元数据（如 Croissant）[^neurips2025datasets-e3]
- [ ] 提供评测代码和复现论文结果的脚本[^reuel2024betterbench-e8]
- [ ] 给出指标的下限、上限、人类水平和随机水平[^reuel2024betterbench-e6]
- [ ] 给出推荐的数据划分并说明理由[^gebru2021datasheets-e10]
- [ ] 保存原始数据，公开处理和标注用的软件[^gebru2021datasheets-e15]
- [ ] 采取防污染措施，例如给评测样本加唯一标识或加密[^reuel2024betterbench-e7]
- [ ] 留反馈渠道和联系人[^reuel2024betterbench-e10]；更新时标明版本[^reuel2024betterbench-e11]

**做得出色**

- [ ] 用实证证据说明基准的相关性（例如系统综述）和好用（例如行动研究、案例研究）[^ralph2020empirical-e154]
- [ ] 报告结果被独立复现过、基准有较大的使用者社区、有独立组织维护[^ralph2020empirical-e153]

**这些情况可以不做，不算缺陷**

- 数据表里不适用于你的数据集的问题，可以跳过[^gebru2021datasheets-e5]
- 新基准还没多少人用、没有独立复现、没有独立组织维护：SIGSOFT 认为这些是不成立的批评，一小组研究者先做出的"原型基准"本身就可以推动讨论[^ralph2020empirical-e159]
- 敏感数据不公开数据本身，只公开详细的元数据和获取规则[^wilkinson2016fair-e5]

上面的清单只是最低要求。BetterBench 的作者也说明，他们的标准是最低质量保证；基准是否真的测到了要测的概念，需要领域专家深入分析[^reuel2024betterbench-e18]。这一点见[基准评测：基准本身有效吗](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗)。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 宣称基准测的是"通用能力" | 没有中立的数据集，"通用"常成了不报告局限的挡箭牌[^raji2021everything-e5] |
| 手头有什么数据就收什么 | 得到的是方便样本，理论上站不住[^raji2021everything-e3] |
| 只报一个总分 | 可能掩盖模型在少数子群体上的糟糕表现[^raji2021everything-e7] |
| 用被评测的工具或模型生成标准答案 | 被评估的方法不应被用来制作标准答案[^reuel2024betterbench-e19] |
| 没去重就划分训练集和测试集 | 重复样本落在两侧，训练和测试不独立，构成泄漏[^kapoor2023leakage-e6] |
| 只有一人标注，或只报百分比一致率 | 没扣除碰巧一致的部分[^mcdonald2019reliability-e4]；标准要求多名标注者并评估一致性[^ralph2020empirical-e111] |
| "公开能下载，所以能用" | 技术上能拿到不等于可以合法使用[^ralph2020empirical-e135] |
| 不写许可证，或放在个人网盘 | 许可证和长期保存都是必须说明的[^neurips2024datasets-e4] |
| 数据表最后才补，或自动生成 | 应在收集前就读问题[^gebru2021datasheets-e8]，写数据表本身不该自动化[^gebru2021datasheets-e4] |
| 悄悄修改数据集，不升版本 | 别人的结果无法对照；小改要标版本，大改要发新版[^reuel2024betterbench-e11] |

---

## 5. 延伸阅读

- **数据表**：Gebru 等人 2021，Datasheets for Datasets。按动机、组成、收集、处理、用途、分发、维护七组列出要回答的问题，附一份示范数据表。出自机器学习，但问题大多通用。
- **机器学习会议怎样审数据集**：NeurIPS 数据集与基准分会的征稿启事。2024 年版列出了审稿时考虑的因素，2025 年版加了提交时必须公开数据和代码、用 Croissant 记录元数据等要求。每年会变，以当年页面为准。
- **基准质量清单**：Reuel 等人 2024，BetterBench。46 条标准按基准生命周期分阶段，附录里有一份给建基准者的清单；网站上持续更新对各基准的评分。
- **基准能说明什么、不能说明什么**：Raji 等人 2021，以 ImageNet 和 GLUE 为例，批评把一个基准当成"通用能力"的度量。
- **跨学科的数据发表**：Wilkinson 等人 2016 的 FAIR 数据原则，以及 Scientific Data 期刊的投稿指南（数据描述论文的结构和要求）。
- **一个智能合约领域的范例**：Durieux 等人 2020（SmartBugs），来源、标注方法和去重步骤都写得很清楚。
- **用基准做评测**：本手册的[基准评测](../07_fields/computer-science/practices/benchmarking.md)。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^raji2021everything-e1]: Raji 等人 2021，§2.2。[证据](../../sources/notes/raji2021everything.md#e1)
[^raji2021everything-e3]: Raji 等人 2021，§4.1。[证据](../../sources/notes/raji2021everything.md#e3)
[^raji2021everything-e4]: Raji 等人 2021，§4.1.1。[证据](../../sources/notes/raji2021everything.md#e4)
[^raji2021everything-e5]: Raji 等人 2021，§4.2。[证据](../../sources/notes/raji2021everything.md#e5)
[^raji2021everything-e6]: Raji 等人 2021，§4.2.2。[证据](../../sources/notes/raji2021everything.md#e6)
[^raji2021everything-e7]: Raji 等人 2021，§4.3.3。[证据](../../sources/notes/raji2021everything.md#e7)
[^raji2021everything-e8]: Raji 等人 2021，§5。[证据](../../sources/notes/raji2021everything.md#e8)
[^raji2021everything-e9]: Raji 等人 2021，§4.2.1。[证据](../../sources/notes/raji2021everything.md#e9)
[^ralph2020empirical-e100]: SIGSOFT 基准评测标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e111]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e111)
[^ralph2020empirical-e129]: SIGSOFT 评分者一致性补充标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e132]: SIGSOFT 评分者一致性补充标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e132)
[^ralph2020empirical-e135]: SIGSOFT 二手人类数据伦理补充标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e135)
[^ralph2020empirical-e138]: SIGSOFT 二手人类数据伦理补充标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e138)
[^ralph2020empirical-e147]: SIGSOFT 基准评测标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e147)
[^ralph2020empirical-e151]: SIGSOFT 基准评测标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e151)
[^ralph2020empirical-e153]: SIGSOFT 基准评测标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e153)
[^ralph2020empirical-e154]: SIGSOFT 基准评测标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e154)
[^ralph2020empirical-e159]: SIGSOFT 基准评测标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e159)
[^neurips2024datasets-e3]: NeurIPS 2024 数据集与基准分会征稿启事，Submission Instructions。[证据](../../sources/notes/neurips2024datasets.md#e3)
[^neurips2024datasets-e4]: NeurIPS 2024 数据集与基准分会征稿启事，Submission Instructions。[证据](../../sources/notes/neurips2024datasets.md#e4)
[^neurips2024datasets-e5]: NeurIPS 2024 数据集与基准分会征稿启事，Submission Instructions。[证据](../../sources/notes/neurips2024datasets.md#e5)
[^neurips2024datasets-e6]: NeurIPS 2024 数据集与基准分会征稿启事，Submission Instructions。[证据](../../sources/notes/neurips2024datasets.md#e6)
[^neurips2024datasets-e8]: NeurIPS 2024 数据集与基准分会征稿启事，审稿因素。[证据](../../sources/notes/neurips2024datasets.md#e8)
[^neurips2024datasets-e9]: NeurIPS 2024 数据集与基准分会征稿启事，审稿因素。[证据](../../sources/notes/neurips2024datasets.md#e9)
[^neurips2024datasets-e10]: NeurIPS 2024 数据集与基准分会征稿启事，审稿因素。[证据](../../sources/notes/neurips2024datasets.md#e10)
[^neurips2024datasets-e11]: NeurIPS 2024 数据集与基准分会征稿启事，审稿因素。[证据](../../sources/notes/neurips2024datasets.md#e11)
[^neurips2024datasets-e12]: NeurIPS 2024 数据集与基准分会征稿启事，常见问题。[证据](../../sources/notes/neurips2024datasets.md#e12)
[^neurips2024datasets-e13]: NeurIPS 2024 数据集与基准分会征稿启事，常见问题。[证据](../../sources/notes/neurips2024datasets.md#e13)
[^neurips2024datasets-e15]: NeurIPS 2024 数据集与基准分会征稿启事，审稿因素。[证据](../../sources/notes/neurips2024datasets.md#e15)
[^neurips2025datasets-e1]: NeurIPS 2025 数据集与基准分会征稿启事，Access。[证据](../../sources/notes/neurips2025datasets.md#e1)
[^neurips2025datasets-e2]: NeurIPS 2025 数据集与基准分会征稿启事，Hosting。[证据](../../sources/notes/neurips2025datasets.md#e2)
[^neurips2025datasets-e3]: NeurIPS 2025 数据集与基准分会征稿启事，Metadata。[证据](../../sources/notes/neurips2025datasets.md#e3)
[^scientificdata2026guidelines-e1]: Scientific Data 投稿指南，Format outline。[证据](../../sources/notes/scientificdata2026guidelines.md#e1)
[^scientificdata2026guidelines-e2]: Scientific Data 投稿指南，Background & Summary。[证据](../../sources/notes/scientificdata2026guidelines.md#e2)
[^scientificdata2026guidelines-e3]: Scientific Data 投稿指南，Methods。[证据](../../sources/notes/scientificdata2026guidelines.md#e3)
[^scientificdata2026guidelines-e4]: Scientific Data 投稿指南，Methods。[证据](../../sources/notes/scientificdata2026guidelines.md#e4)
[^scientificdata2026guidelines-e5]: Scientific Data 投稿指南，Data Record。[证据](../../sources/notes/scientificdata2026guidelines.md#e5)
[^scientificdata2026guidelines-e6]: Scientific Data 投稿指南，Data Overview。[证据](../../sources/notes/scientificdata2026guidelines.md#e6)
[^scientificdata2026guidelines-e7]: Scientific Data 投稿指南，Technical Validation。[证据](../../sources/notes/scientificdata2026guidelines.md#e7)
[^scientificdata2026guidelines-e8]: Scientific Data 投稿指南，Deposit the dataset。[证据](../../sources/notes/scientificdata2026guidelines.md#e8)
[^scientificdata2026guidelines-e10]: Scientific Data 投稿指南，Scope。[证据](../../sources/notes/scientificdata2026guidelines.md#e10)
[^durieux2020empirical-e1]: Durieux 等人 2020，§1，第 1 页。[证据](../../sources/notes/durieux2020empirical.md#e1)
[^durieux2020empirical-e2]: Durieux 等人 2020，§1，第 2 页。[证据](../../sources/notes/durieux2020empirical.md#e2)
[^durieux2020empirical-e5]: Durieux 等人 2020，§2.3.1，第 3 页。[证据](../../sources/notes/durieux2020empirical.md#e5)
[^durieux2020empirical-e6]: Durieux 等人 2020，§2.3.1，第 3–4 页。[证据](../../sources/notes/durieux2020empirical.md#e6)
[^durieux2020empirical-e8]: Durieux 等人 2020，§2.3.2，第 4 页。[证据](../../sources/notes/durieux2020empirical.md#e8)
[^durieux2020empirical-e14]: Durieux 等人 2020，§4.2，第 10 页。[证据](../../sources/notes/durieux2020empirical.md#e14)
[^reuel2024betterbench-e3]: Reuel 等人 2024，图 1、附录 B。[证据](../../sources/notes/reuel2024betterbench.md#e3)
[^reuel2024betterbench-e4]: Reuel 等人 2024，§4.1。[证据](../../sources/notes/reuel2024betterbench.md#e4)
[^reuel2024betterbench-e5]: Reuel 等人 2024，§4.1。[证据](../../sources/notes/reuel2024betterbench.md#e5)
[^reuel2024betterbench-e6]: Reuel 等人 2024，§4.1。[证据](../../sources/notes/reuel2024betterbench.md#e6)
[^reuel2024betterbench-e7]: Reuel 等人 2024，§4.2。[证据](../../sources/notes/reuel2024betterbench.md#e7)
[^reuel2024betterbench-e8]: Reuel 等人 2024，§4.2。[证据](../../sources/notes/reuel2024betterbench.md#e8)
[^reuel2024betterbench-e9]: Reuel 等人 2024，§4.3。[证据](../../sources/notes/reuel2024betterbench.md#e9)
[^reuel2024betterbench-e10]: Reuel 等人 2024，§4.4。[证据](../../sources/notes/reuel2024betterbench.md#e10)
[^reuel2024betterbench-e11]: Reuel 等人 2024，§5，Versioning。[证据](../../sources/notes/reuel2024betterbench.md#e11)
[^reuel2024betterbench-e12]: Reuel 等人 2024，§5，Detecting small improvements。[证据](../../sources/notes/reuel2024betterbench.md#e12)
[^reuel2024betterbench-e13]: Reuel 等人 2024，§5，Dynamic vs. static benchmarks。[证据](../../sources/notes/reuel2024betterbench.md#e13)
[^reuel2024betterbench-e14]: Reuel 等人 2024，§7。[证据](../../sources/notes/reuel2024betterbench.md#e14)
[^reuel2024betterbench-e15]: Reuel 等人 2024，§7。[证据](../../sources/notes/reuel2024betterbench.md#e15)
[^reuel2024betterbench-e16]: Reuel 等人 2024，§8，Contamination。[证据](../../sources/notes/reuel2024betterbench.md#e16)
[^reuel2024betterbench-e17]: Reuel 等人 2024，§8，Quick saturation。[证据](../../sources/notes/reuel2024betterbench.md#e17)
[^reuel2024betterbench-e18]: Reuel 等人 2024，§9。[证据](../../sources/notes/reuel2024betterbench.md#e18)
[^reuel2024betterbench-e19]: Reuel 等人 2024，§2.2。[证据](../../sources/notes/reuel2024betterbench.md#e19)
[^gebru2021datasheets-e1]: Gebru 等人 2021，§1。[证据](../../sources/notes/gebru2021datasheets.md#e1)
[^gebru2021datasheets-e2]: Gebru 等人 2021，§1.1。[证据](../../sources/notes/gebru2021datasheets.md#e2)
[^gebru2021datasheets-e3]: Gebru 等人 2021，§1.1。[证据](../../sources/notes/gebru2021datasheets.md#e3)
[^gebru2021datasheets-e4]: Gebru 等人 2021，§1.1。[证据](../../sources/notes/gebru2021datasheets.md#e4)
[^gebru2021datasheets-e5]: Gebru 等人 2021，§3。[证据](../../sources/notes/gebru2021datasheets.md#e5)
[^gebru2021datasheets-e6]: Gebru 等人 2021，§3。[证据](../../sources/notes/gebru2021datasheets.md#e6)
[^gebru2021datasheets-e7]: Gebru 等人 2021，§3.1。[证据](../../sources/notes/gebru2021datasheets.md#e7)
[^gebru2021datasheets-e8]: Gebru 等人 2021，§3.2。[证据](../../sources/notes/gebru2021datasheets.md#e8)
[^gebru2021datasheets-e9]: Gebru 等人 2021，§3.2。[证据](../../sources/notes/gebru2021datasheets.md#e9)
[^gebru2021datasheets-e10]: Gebru 等人 2021，§3.2。[证据](../../sources/notes/gebru2021datasheets.md#e10)
[^gebru2021datasheets-e11]: Gebru 等人 2021，§3.2。[证据](../../sources/notes/gebru2021datasheets.md#e11)
[^gebru2021datasheets-e12]: Gebru 等人 2021，§3.2。[证据](../../sources/notes/gebru2021datasheets.md#e12)
[^gebru2021datasheets-e13]: Gebru 等人 2021，§3.3。[证据](../../sources/notes/gebru2021datasheets.md#e13)
[^gebru2021datasheets-e14]: Gebru 等人 2021，§3.3。[证据](../../sources/notes/gebru2021datasheets.md#e14)
[^gebru2021datasheets-e15]: Gebru 等人 2021，§3.4。[证据](../../sources/notes/gebru2021datasheets.md#e15)
[^gebru2021datasheets-e16]: Gebru 等人 2021，§3.5。[证据](../../sources/notes/gebru2021datasheets.md#e16)
[^gebru2021datasheets-e17]: Gebru 等人 2021，§3.6。[证据](../../sources/notes/gebru2021datasheets.md#e17)
[^gebru2021datasheets-e18]: Gebru 等人 2021，§3.7。[证据](../../sources/notes/gebru2021datasheets.md#e18)
[^gebru2021datasheets-e19]: Gebru 等人 2021，§4。[证据](../../sources/notes/gebru2021datasheets.md#e19)
[^gebru2021datasheets-e20]: Gebru 等人 2021，§3.3。[证据](../../sources/notes/gebru2021datasheets.md#e20)
[^wei2024evals-e2]: Jason Wei 2024，评测常见错误。[证据](../../sources/notes/wei2024evals.md#e2)
[^wei2024evals-e3]: Jason Wei 2024，评测常见错误。[证据](../../sources/notes/wei2024evals.md#e3)
[^wei2024evals-e9]: Jason Wei 2024，测试集污染。[证据](../../sources/notes/wei2024evals.md#e9)
[^mcdonald2019reliability-e4]: McDonald 等人 2019，§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e4)
[^kapoor2023leakage-e5]: Kapoor & Narayanan 2023，Taxonomy，[L3.1]。[证据](../../sources/notes/kapoor2023leakage.md#e5)
[^kapoor2023leakage-e6]: Kapoor & Narayanan 2023，Taxonomy，[L3.2]。[证据](../../sources/notes/kapoor2023leakage.md#e6)
[^wilkinson2016fair-e3]: Wilkinson 等人 2016，Box 2。[证据](../../sources/notes/wilkinson2016fair.md#e3)
[^wilkinson2016fair-e4]: Wilkinson 等人 2016，Box 2。[证据](../../sources/notes/wilkinson2016fair.md#e4)
[^wilkinson2016fair-e5]: Wilkinson 等人 2016，The FAIR Guiding Principles in detail。[证据](../../sources/notes/wilkinson2016fair.md#e5)
