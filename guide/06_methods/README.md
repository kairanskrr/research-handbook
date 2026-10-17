# 研究类型：具体怎么做

这一页是目录：按研究者平时的叫法（用户研究、工具论文、基准评测、综述、对照实验、案例研究、复现……），帮你找到讲具体做法的那一页。

怎么用：

1. 先走完第一部分的出口[收敛成项目](../01_find-a-problem/05_converge.md)：写出你想证明的那句话，想清楚拿什么证据让人相信，判断这是哪类研究。
2. 在下面的对照表里，找你或你的领域对这类研究的叫法，点进对应页面。一个项目常常要用到两三页。
3. 拿不准自己的研究产生哪种知识，先看表里最后一列链接的[研究套路](../05_research-strategies/README.md)页。

例如贯穿全书的项目"现有大模型漏洞检测的评测结果被数据泄露高估了"，研究者多半会叫它实证研究或评测研究。它主要用到[基准评测](../07_fields/computer-science/practices/benchmarking.md)这一页，尤其是其中[基准本身有效吗](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗)一节；产生的知识属于[测量](../05_research-strategies/measure.md)套路。

## 按你的叫法找

下面各表是本手册为方便查找做的归纳："你可能这样叫"一列收的是常见的中英文叫法，不是严格定义；"常服务的套路"一列依据各套路页"常用的研究方法"一节和各页开头的说明，没有列到的写"暂未列出"。"来源"一列写"方法篇"的，是多个学科都用的方法，括号里是它原来为哪个学科写；写"某学科的实践"的，是只在这个学科用的做法，放在该学科的文件夹里。

### 以已发表的研究为材料

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 文献综述、系统综述、映射研究、综述论文；literature review、systematic review、mapping study、survey paper | [综述研究](review_study.md) | 把已发表的研究收集起来，汇总、分析 | [综合](../05_research-strategies/synthesize.md)、[观察描述](../05_research-strategies/observe_describe.md) | 方法篇（计算机） |
| 案例调查；case survey | [案例调查](case_survey.md) | 把已发表的大量案例研究编码成数据集，再做定量分析 | [综合](../05_research-strategies/synthesize.md) | 方法篇（计算机） |
| 方法论研究、元科学、研究实践调查、批判性综述；meta-science、meta-research、critical review | [方法论研究与元科学](meta_science.md) | 研究"怎么做研究"：方法指南、批判性综述、研究实践调查 | [综合](../05_research-strategies/synthesize.md)、[测量](../05_research-strategies/measure.md) | 方法篇（计算机） |
| 元分析、荟萃分析、干预效果的系统综述；meta-analysis | [系统综述与元分析（健康领域）](meta_analysis.md) | 回答"某项干预效果如何"，用统计方法把多项研究的结果合并成一个总的估计 | [比较评估](../05_research-strategies/compare_evaluate.md)、[综合](../05_research-strategies/synthesize.md) | 方法篇（健康科学） |

### 用已有的数据或模型

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 数据驱动研究、预测建模、统计建模；data-driven study、predictive modeling | [数据科学研究](data_science.md) | 对已有数据做预测建模或统计建模，用结果回答科学问题 | [观察描述](../05_research-strategies/observe_describe.md) | 方法篇（计算机） |
| 仓库挖掘、软件仓库的实证研究；mining software repositories、empirical study（软件工程里常指这类） | [仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md) | 从代码仓库、缺陷库和问答网站中挖数据 | [观察描述](../05_research-strategies/observe_describe.md)、[解释因果](../05_research-strategies/explain_causality.md) | 计算机的实践 |
| 纵向研究、追踪研究；longitudinal study | [纵向研究](longitudinal_study.md) | 长时间重复观察同一批对象，看它怎样变化 | [观察描述](../05_research-strategies/observe_describe.md) | 方法篇（计算机） |
| 仿真研究、模拟实验；simulation study | [定量仿真](simulation_study.md) | 建立模仿真实系统的计算模型，在模型上做实验 | [构建改进](../05_research-strategies/build_improve.md) | 方法篇（计算机） |
| 准实验、自然实验、因果推断、双重差分、断点回归、工具变量；quasi-experiment、natural experiment、causal inference、difference-in-differences | [准实验与因果识别](quasi_experiment.md) | 不能随机分组时，从观察性数据估计因果效应 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（经济学与商学） |
| 队列研究、病例对照研究、横断面研究、观察性研究；cohort study、case-control study、cross-sectional study | [观察性流行病学研究](observational_epidemiology.md) | 研究者不施加干预，只观察人群中的暴露和结局 | [解释因果](../05_research-strategies/explain_causality.md)、[观察描述](../05_research-strategies/observe_describe.md) | 方法篇（健康科学） |
| 空间分析、空间回归、热点分析；spatial analysis | [空间分析研究](../07_fields/geography/practices/spatial_analysis.md) | 用带位置的数据，研究现象在空间上怎样分布、环境或邻近地区怎样影响结果 | [观察描述](../05_research-strategies/observe_describe.md)、[解释因果](../05_research-strategies/explain_causality.md) | 社会与经济地理学的实践 |

### 涉及人的研究

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 对照实验、用户研究、可用性实验、被试实验；controlled experiment、user study、usability study | [对照实验](controlled_experiment.md) | 有人参与，随机分组，比较一个因素对人的表现有什么影响 | [比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md) | 方法篇（计算机） |
| 在线对照实验、A/B 测试、分流实验、线上实验；online controlled experiment、A/B test、split test | [在线对照实验（A/B 测试）](online_controlled_experiment.md) | 把正在运行的网站或应用的真实用户随机分到现有版本和新版本，比较两组的指标 | [比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md)（套路页暂未列出） | 方法篇（计算机） |
| 随机对照试验、临床试验；randomized controlled trial、clinical trial | [随机对照试验](randomized_controlled_trial.md) | 把受试者随机分到不同干预组，比较他们的结局 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（临床医学） |
| 田野实验、实地实验、随机评估；field experiment、randomized evaluation | [田野实验](field_experiment.md) | 和政府、企业或社区合作，在真实世界里随机决定谁接受一项干预，再比较各组的结果 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（经济学与商学） |
| 问卷调查、调研；questionnaire survey、survey（指问卷时） | [问卷调查](questionnaire_survey.md) | 用问卷向大量人收集数据，再系统分析 | [观察描述](../05_research-strategies/observe_describe.md)、[测量](../05_research-strategies/measure.md) | 方法篇（计算机） |
| 量表编制、量表修订、量表的信度和效度检验；scale development、psychometric validation | [量表编制与测量研究](scale_development.md) | 以测量工具本身为成果：新编、翻译改编量表，或为已有量表积累信度和效度证据 | [测量](../05_research-strategies/measure.md) | 方法篇（心理学与认知科学） |
| 访谈研究、定性访谈、半结构化访谈；interview study、qualitative study | [访谈研究](interview_study.md) | 深度访谈一批人，用定性分析归纳主题 | [观察描述](../05_research-strategies/observe_describe.md) | 方法篇（计算机） |
| 焦点小组、小组讨论、焦点访谈；focus group、focus group discussion | [焦点小组](focus_group.md) | 召集一小群人由主持人引导讨论，从讨论和互动中收集看法 | [观察描述](../05_research-strategies/observe_describe.md) | 方法篇（健康科学） |
| 口述历史；oral history | [口述历史](oral_history.md) | 访谈亲历者、录音存档，再把访谈当作需要核对的证据来用 | [解读论证](../05_research-strategies/interpret_argue.md) | 方法篇（历史与考古） |
| 案例研究、个案研究、民族志；case study、ethnography | [案例研究与民族志](case_study.md) | 在真实环境里深入研究少数对象 | [观察描述](../05_research-strategies/observe_describe.md)、[解释因果](../05_research-strategies/explain_causality.md) | 方法篇（计算机） |
| 扎根理论；grounded theory | [扎根理论](grounded_theory.md) | 一边收集数据一边分析，从数据中逐步归纳出理论 | [观察描述](../05_research-strategies/observe_describe.md) | 方法篇（计算机） |
| 行动研究；action research | [行动研究](action_research.md) | 和真实组织合作推动一项改变，一边改进一边研究 | [构建改进](../05_research-strategies/build_improve.md)、[观察描述](../05_research-strategies/observe_describe.md) | 方法篇（计算机） |

### 实验室和野外

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 湿实验、实验台实验、体外实验；wet-lab experiment、bench experiment | [实验台实验（湿实验）](bench_experiment.md) | 在实验台上用培养的细胞、提取的分子和试剂做处理，和对照比较，检验一个假设 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（生物科学） |
| 动物实验、临床前研究；animal study、preclinical study | [临床前动物研究](preclinical_animal_study.md) | 在活体动物身上做实验，为人类医学提供依据 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（基础医学） |
| 合成研究、合成方法学、表征；synthesis、characterization | [合成与表征研究](synthesis_study.md) | 设计路线、做反应、纯化和表征产物，报告产率和底物范围 | [构建改进](../05_research-strategies/build_improve.md) | 方法篇（化学科学） |
| 实验测量、精密测量、不确定度分析；measurement、uncertainty analysis | [实验测量研究](experimental_measurement.md) | 测出一个物理量的值，并说清这个值有多可信 | [测量](../05_research-strategies/measure.md) | 方法篇（物理科学） |
| 野外观测、野外采样、现场监测；field study、field campaign | [野外观测研究](field_study.md) | 到河流、土壤、大气等现场布点、测量、取样，再用这些数据回答问题 | [观察描述](../05_research-strategies/observe_describe.md) | 方法篇（地球与环境科学） |
| 田间试验、小区试验、多点试验；field trial、multi-environment trial | [田间试验](../07_fields/agriculture/practices/field_trial.md) | 在试验地的小区上比较品种、肥料、耕作等处理 | [解释因果](../05_research-strategies/explain_causality.md)、[比较评估](../05_research-strategies/compare_evaluate.md)（套路页暂未列出） | 农业、林业与渔业的实践 |
| 考古发掘、田野考古、考古调查；excavation、archaeological survey | [考古发掘与野外调查](../07_fields/history-archaeology/practices/archaeological_excavation.md) | 从写研究设计、做不挖土的调查，到按地层发掘、逐单位记录、归档和写报告 | [观察描述](../05_research-strategies/observe_describe.md)（据该页开头；套路页暂未列出） | 历史与考古的实践 |
| 语言记录、语言学田野调查；language documentation、linguistic fieldwork | [语言记录与语言学田野调查](../07_fields/languages-literature/practices/language_documentation.md) | 和说这种语言的社区一起，把它录下来、转写、翻译、注释，存进档案馆，再做分析 | [观察描述](../05_research-strategies/observe_describe.md) | 语言与文学的实践 |

### 档案、文本与论证

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 档案研究、史料研究；archival research | [档案研究](archival_research.md) | 查阅没有出版过的原始记录，用它们回答关于过去的问题 | [解读论证](../05_research-strategies/interpret_argue.md) | 方法篇（历史与考古） |
| 过程追踪、比较案例研究、小样本比较；process tracing、comparative case study | [过程追踪与比较案例研究](process_tracing.md) | 在一个案例内部一步步检查事情怎样发生，或有意挑选少数案例互相比较 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（政治学） |
| 文本细读、文学批评、作品解读；close reading、literary analysis | [文本细读与文学论证](../07_fields/languages-literature/practices/close_reading.md) | 围绕一个或几个文本提出一种阐释 | [解读论证](../05_research-strategies/interpret_argue.md) | 语言与文学的实践 |
| 规范法学、法教义学、判例研究；doctrinal legal research | [规范法学研究](../07_fields/law/practices/doctrinal_research.md) | 确定法律是什么，评价现行法，提出改革建议 | [解读论证](../05_research-strategies/interpret_argue.md) | 法学的实践 |
| 哲学论证、概念分析；philosophical argument、conceptual analysis | [哲学论证研究](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md) | 为一个论题辩护、澄清概念、检验原则 | [解读论证](../05_research-strategies/interpret_argue.md) | 哲学、伦理与宗教的实践 |
| 理论研究、证明、形式化分析、机器检查的证明；theory paper、proof、formal analysis | [理论研究](../07_fields/computer-science/practices/theoretical_research.md) | 以定理和证明为主要成果：算法复杂度的上下界、协议的安全性、用形式化方法证明系统满足某个性质 | [证明](../05_research-strategies/prove.md) | 计算机的实践 |
| 内容分析、定量内容分析、定性内容分析、编码分析、文本编码；content analysis、qualitative content analysis、coding scheme / codebook | [内容分析](content_analysis.md) | 按编码手册把大量文本、媒体、帖子或文件系统地编进类别，再统计或解读；多人编码时测编码者间信度 | [观察描述](../05_research-strategies/observe_describe.md)（套路页暂未列出）、[综合](../05_research-strategies/synthesize.md)（材料是已发表研究时；套路页暂未列出） | 方法篇（传播学） |
| 立场论文、观点论文、展望论文、反思论文；position paper、perspective、vision paper、essay | [立场论文](position_paper.md) | 为"这个领域应该做什么、相信什么"提出论证，正视最强的反对立场 | [解读论证](../05_research-strategies/interpret_argue.md) | 方法篇（计算机） |

### 提出新东西并评估

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 工程研究、工具论文、新方法论文、系统论文；tool paper、technique paper、system paper、design science | [工程研究](../07_fields/computer-science/practices/engineering_research.md) | 提出并评估新的方法、工具或系统：选基线、选基准、设计评估、公开研究制品 | [构建改进](../05_research-strategies/build_improve.md) | 计算机的实践 |
| 基准评测、评测研究、工具对比；benchmarking、benchmark study、empirical evaluation | [基准评测](../07_fields/computer-science/practices/benchmarking.md) | 用一套标准的评测对象和自动化、可重复的流程，比较系统、工具或模型；也讲怎样检查评测集本身是否有效 | [比较评估](../05_research-strategies/compare_evaluate.md)、[构建改进](../05_research-strategies/build_improve.md)、[测量](../05_research-strategies/measure.md) | 计算机的实践 |
| 数据集论文、基准论文、资源论文、数据描述；dataset paper、benchmark paper、resource paper、data descriptor | [建一个数据集或基准](dataset_paper.md) | 以新建的数据集或基准本身为成果：说清为什么需要它，收集、标注、划分，写数据表，处理许可和伦理，发布并维护 | [测量](../05_research-strategies/measure.md)、[比较评估](../05_research-strategies/compare_evaluate.md) | 方法篇（计算机） |
| 大模型实证研究、大模型评测、用大模型做标注或模拟被试、LLM 实证研究；LLM-based empirical study、LLM evaluation、LLM-as-annotator、LLM-as-judge | [大模型实证研究](llm_study.md) | 评测大模型，或把大模型当标注员、评审员、模拟被试来用：记录版本和提示词、检查污染和波动、拿人工判断验证 | [测量](../05_research-strategies/measure.md)、[比较评估](../05_research-strategies/compare_evaluate.md)、[构建改进](../05_research-strategies/build_improve.md) | 方法篇（计算机） |
| 优化研究、基于搜索的研究；optimization study、search-based software engineering | [优化研究](../07_fields/computer-science/practices/optimization_study.md) | 把问题建模成"在很多候选解中找最好的"，用搜索算法求解 | [构建改进](../05_research-strategies/build_improve.md)、[比较评估](../05_research-strategies/compare_evaluate.md) | 计算机的实践 |
| 基于设计的研究、设计实验；design-based research | [基于设计的研究](../07_fields/education/practices/design_based_research.md) | 在真实课堂里一轮轮设计、试用、改进教学干预，同时提炼设计原则 | [构建改进](../05_research-strategies/build_improve.md) | 教育学的实践 |
| 基于实践的研究、以创作为方法的研究、艺术研究；practice-based research、practice-led research、artistic research | [基于实践的研究](../07_fields/arts/practices/practice_based_research.md) | 以创作出的作品作为知识贡献的基础，再配上过程记录和文字说明 | [构建改进](../05_research-strategies/build_improve.md) | 艺术的实践 |

[合成与表征研究](synthesis_study.md)和[定量仿真](simulation_study.md)也常服务构建改进，分别放在"实验室和野外"和"用已有的数据或模型"两组。

### 跨方法

| 你可能这样叫 | 去看 | 它做什么 | 常服务的套路 | 来源 |
|---|---|---|---|---|
| 复现研究、重复研究、可复现性研究；replication study、reproduction | [复现研究](replication.md) | 有计划地重做已发表的研究，检验结论是否成立 | [比较评估](../05_research-strategies/compare_evaluate.md)、[测量](../05_research-strategies/measure.md) | 方法篇（计算机） |
| 混合方法、多方法研究；mixed methods、multi-method research | [混合方法](mixed_methods.md) | 用两种及以上方法研究同一个问题 | [解释因果](../05_research-strategies/explain_causality.md) | 方法篇（计算机） |

### 同一个叫法，可能指不同的东西

有几个叫法很常见，但在不同学科、不同语境里指的东西不一样，先弄清你说的是哪一种：

- **survey**：指综述论文时，看[综述研究](review_study.md)；指发问卷时，看[问卷调查](questionnaire_survey.md)；考古里的 survey 指野外调查，看[考古发掘与野外调查](../07_fields/history-archaeology/practices/archaeological_excavation.md)。
- **empirical study（实证研究）**：泛指一切靠观察和数据得出结论的研究，不是一种具体做法。先回到[研究套路](../05_research-strategies/README.md)判断你要的是描述、比较、测量还是因果，再按上面的表找页面。
- **case study（案例研究）**：社会科学和软件工程里指深入研究少数真实对象，看[案例研究与民族志](case_study.md)或[过程追踪与比较案例研究](process_tracing.md)；工具论文里"在几个真实系统上演示"的那种案例，属于评估的一部分，看[工程研究](../07_fields/computer-science/practices/engineering_research.md)。
- **田野调查 / fieldwork**：社会科学里多指民族志式的长期观察，看[案例研究与民族志](case_study.md)；语言学、考古、地球科学各有自己的做法，分别看上面"实验室和野外"一组。
- **实验 / experiment**：有人参与的看[对照实验](controlled_experiment.md)或[随机对照试验](randomized_controlled_trial.md)；在正在运行的产品里给真实用户分流的看[在线对照实验（A/B 测试）](online_controlled_experiment.md)；拿大模型做实验的看[大模型实证研究](llm_study.md)；在软件系统或模型上跑的看[基准评测](../07_fields/computer-science/practices/benchmarking.md)；在实验台上做的看[实验台实验（湿实验）](bench_experiment.md)。

## 方法和套路的分工

- **研究套路**讲"这个项目产生什么知识、需要什么证据"，见[研究套路](../05_research-strategies/README.md)。
- **这一栏的各页**讲"具体怎么做好"：步骤、关键决定、检查清单和常见错误。
- **一种做法可以服务多个套路。** 例如对照实验既能用来比较两个已有工具，也能用来检验"X 导致 Y"。所以上表每一行都列出它常服务的套路。
- **哪些放在 `06_methods/`，哪些放在学科文件夹**：两个及以上学科都用的方法放在 `06_methods/`；只有一个学科用的实践，放在该学科文件夹的 `practices/` 下，例如[计算机特有的研究实践](../07_fields/computer-science/practices/README.md)。网站导航里两处合在一起，就是这个"研究类型"栏目。

这样的分工是本手册的约定。

怎样根据问题选套路和方法，见[选方法](../02_do-the-project/02_choose-method.md)。

## 这些方法篇的适用范围

`06_methods/` 里有 34 篇方法篇。其中 28 篇原来分别是为计算机或某一个学科写的，后来因为不止一个学科在用，才放到这一层：

- **原为计算机写的 14 篇**主要面向软件工程：大多数篇目的检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，例子也多来自软件工程。
- **原为其他学科写的 14 篇**，依据的是该学科的规范和资料，例如随机对照试验按医学的试验报告规范写，准实验讲的是经济学里的做法。

另外 6 篇是后来补的：[在线对照实验](online_controlled_experiment.md)、[焦点小组](focus_group.md)、[内容分析](content_analysis.md)、[立场论文](position_paper.md)、[建一个数据集或基准](dataset_paper.md)、[大模型实证研究](llm_study.md)。它们一开始就按跨学科的页面写，资料来自哪个领域，各页开头的适用范围里写明了。

方法本身多个学科都在用，但具体规范各学科不同。每篇开头写明了它原来为哪个学科写、资料来自哪里。如果你不在这篇原来的学科，先看本学科的规范和本学科的实践，再把这里的方法篇当作参考。

学科独有的 14 篇实践（计算机 5 篇，其他学科 9 篇）只代表该学科的做法。各学科的整体规矩见[学科篇](../07_fields/README.md)。
