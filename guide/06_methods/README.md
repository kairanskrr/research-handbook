# 研究方法

你已经选定了研究套路，知道要拿出什么样的证据。现在你想知道：具体用什么方法拿到这些证据，怎样把这个方法做好？

这一层回答的就是这个问题。

## 方法和套路的分工

- **研究套路**讲"这个项目产生什么知识、需要什么证据"，见[研究套路](../05_research-strategies/README.md)。
- **研究方法**讲"具体怎么做好"：步骤、关键决定、检查清单和常见错误。
- **一个方法可以服务多个套路。** 例如对照实验既能用来比较两个已有工具，也能用来检验"X 导致 Y"。所以下表每一行都列出它常服务的套路。
- **哪些方法放在这里**：两个及以上学科都用的方法放在这一层；只有一个学科用的实践，放在该学科的文件夹里（见本页末尾）。

这样的分工是本手册的约定 `[本项目分析]`。

怎样根据问题选套路和方法，见[选定研究套路和方法](../02_from-project-to-study/02_choose-strategy-and-method.md)。

## 28 种方法

"常服务的套路"一列依据各套路页"常用的研究方法"一节；套路页没有列到的，写"暂未列出"。"原来为哪个学科写"一列说明这篇方法篇的资料主要来自哪里，不是说只有这个学科在用。

### 以已发表的研究为材料

| 方法 | 做什么 | 原来为哪个学科写 | 常服务的套路 |
|---|---|---|---|
| [综述研究](review_study.md) | 系统综述、映射研究和综述论文：把已发表的研究收集起来，汇总、分析 | 计算机 | [综合](../05_research-strategies/synthesize.md)、[观察描述](../05_research-strategies/observe_describe.md) |
| [案例调查](case_survey.md) | 把已发表的大量案例研究编码成数据集，再做定量分析 | 计算机 | [综合](../05_research-strategies/synthesize.md) |
| [方法论研究与元科学](meta_science.md) | 研究"怎么做研究"：方法指南、批判性综述、研究实践调查 | 计算机 | [综合](../05_research-strategies/synthesize.md)、[测量](../05_research-strategies/measure.md) |
| [系统综述与元分析（健康领域）](meta_analysis.md) | 回答"某项干预效果如何"的系统综述，用统计方法把多项研究的结果合并成一个总的估计 | 健康科学 | [比较评估](../05_research-strategies/compare_evaluate.md)、[综合](../05_research-strategies/synthesize.md) |

### 基于已有数据或模型

| 方法 | 做什么 | 原来为哪个学科写 | 常服务的套路 |
|---|---|---|---|
| [数据科学研究](data_science.md) | 对已有数据做预测建模或统计建模，用结果回答科学问题 | 计算机 | [观察描述](../05_research-strategies/observe_describe.md) |
| [纵向研究](longitudinal_study.md) | 长时间重复观察同一批对象，看它怎样变化 | 计算机 | [观察描述](../05_research-strategies/observe_describe.md) |
| [定量仿真](simulation_study.md) | 建立模仿真实系统的计算模型，在模型上做实验 | 计算机 | [构建改进](../05_research-strategies/build_improve.md) |
| [准实验与因果识别](quasi_experiment.md) | 不能随机分组时，用双重差分、断点回归、工具变量等办法，从观察性数据估计因果效应 | 经济学与商学 | [解释因果](../05_research-strategies/explain_causality.md) |
| [观察性流行病学研究](observational_epidemiology.md) | 队列研究、病例对照研究、横断面研究：研究者不施加干预，只观察 | 健康科学 | [解释因果](../05_research-strategies/explain_causality.md)、[观察描述](../05_research-strategies/observe_describe.md) |

### 涉及人的研究

| 方法 | 做什么 | 原来为哪个学科写 | 常服务的套路 |
|---|---|---|---|
| [对照实验](controlled_experiment.md) | 有人参与，随机分组，比较一个因素对人的表现有什么影响 | 计算机 | [比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md) |
| [随机对照试验](randomized_controlled_trial.md) | 把受试者随机分到不同干预组，比较他们的结局 | 临床医学 | [解释因果](../05_research-strategies/explain_causality.md) |
| [田野实验](field_experiment.md) | 和政府、企业或社区合作，在真实世界里随机决定谁接受一项干预，再比较各组的结果 | 经济学与商学 | [解释因果](../05_research-strategies/explain_causality.md) |
| [问卷调查](questionnaire_survey.md) | 用问卷向大量人收集数据，再系统分析 | 计算机 | [观察描述](../05_research-strategies/observe_describe.md)、[测量](../05_research-strategies/measure.md) |
| [量表编制与测量研究](scale_development.md) | 以测量工具本身为成果：新编、翻译改编量表，或为已有量表积累信度和效度证据 | 心理学与认知科学 | [测量](../05_research-strategies/measure.md) |
| [访谈研究](interview_study.md) | 深度访谈一批人，用定性分析归纳主题 | 计算机 | [观察描述](../05_research-strategies/observe_describe.md) |
| [口述历史](oral_history.md) | 访谈亲历者、录音存档，再把访谈当作需要核对的证据来用 | 历史与考古 | 暂未列出 |
| [案例研究与民族志](case_study.md) | 在真实环境里深入研究少数对象 | 计算机 | [观察描述](../05_research-strategies/observe_describe.md)、[解释因果](../05_research-strategies/explain_causality.md) |
| [扎根理论](grounded_theory.md) | 一边收集数据一边分析，从数据中逐步归纳出理论 | 计算机 | [观察描述](../05_research-strategies/observe_describe.md) |
| [行动研究](action_research.md) | 和真实组织合作推动一项改变，一边改进一边研究 | 计算机 | [构建改进](../05_research-strategies/build_improve.md)、[观察描述](../05_research-strategies/observe_describe.md) |

### 实验室和野外的实验与观测

| 方法 | 做什么 | 原来为哪个学科写 | 常服务的套路 |
|---|---|---|---|
| [实验台实验（湿实验）](bench_experiment.md) | 在实验台上用培养的细胞、提取的分子和试剂做处理，和对照比较，检验一个假设 | 生物科学 | 暂未列出 |
| [临床前动物研究](preclinical_animal_study.md) | 在活体动物身上做实验，为人类医学提供依据 | 基础医学 | 暂未列出 |
| [合成与表征研究](synthesis_study.md) | 设计路线、做反应、纯化和表征产物，报告产率和底物范围 | 化学科学 | [构建改进](../05_research-strategies/build_improve.md) |
| [实验测量研究](experimental_measurement.md) | 测出一个物理量的值，并说清这个值有多可信 | 物理科学 | [测量](../05_research-strategies/measure.md) |
| [野外观测研究](field_study.md) | 到河流、土壤、大气等现场布点、测量、取样，再用这些数据回答问题 | 地球与环境科学 | [观察描述](../05_research-strategies/observe_describe.md) |

### 以档案和案例为材料

| 方法 | 做什么 | 原来为哪个学科写 | 常服务的套路 |
|---|---|---|---|
| [档案研究](archival_research.md) | 查阅没有出版过的原始记录，用它们回答关于过去的问题 | 历史与考古 | [解读论证](../05_research-strategies/interpret_argue.md) |
| [过程追踪与比较案例研究](process_tracing.md) | 在一个案例内部一步步检查事情怎样发生，或有意挑选少数案例互相比较 | 政治学 | [解释因果](../05_research-strategies/explain_causality.md) |

### 跨方法

| 方法 | 做什么 | 原来为哪个学科写 | 常服务的套路 |
|---|---|---|---|
| [复现研究](replication.md) | 有计划地重做已发表的研究，检验结论是否成立 | 计算机 | [比较评估](../05_research-strategies/compare_evaluate.md)、[测量](../05_research-strategies/measure.md) |
| [混合方法](mixed_methods.md) | 用两种及以上方法研究同一个问题 | 计算机 | [解释因果](../05_research-strategies/explain_causality.md) |

分组是本手册为了方便查找做的归纳 `[本项目分析]`。

## 这些方法篇的适用范围

`[本项目分析]` 这些方法篇原来分别是为计算机或某一个学科写的，后来因为不止一个学科在用，才放到这一层：

- **原为计算机写的 14 篇**主要面向软件工程：大多数篇目的检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，例子也多来自软件工程。
- **原为其他学科写的 14 篇**，依据的是该学科的规范和资料，例如随机对照试验按医学的试验报告规范写，准实验讲的是经济学里的做法。

方法本身多个学科都在用，但具体规范各学科不同。每篇开头写明了它原来为哪个学科写、资料来自哪里。如果你不在这篇原来的学科，先看本学科的规范和本学科的实践，再把这里的方法篇当作参考。

## 学科独有的实践

只有一个学科使用的研究实践，放在该学科文件夹的 `practices/` 下。

### 其他学科

| 学科 | 实践 |
|---|---|
| 农业、林业与渔业 | [田间试验](../07_fields/agriculture/practices/field_trial.md) |
| 社会与经济地理学 | [空间分析研究](../07_fields/geography/practices/spatial_analysis.md) |
| 教育学 | [基于设计的研究](../07_fields/education/practices/design_based_research.md) |
| 法学 | [规范法学研究](../07_fields/law/practices/doctrinal_research.md) |
| 历史与考古 | [考古发掘与野外调查](../07_fields/history-archaeology/practices/archaeological_excavation.md) |
| 语言与文学 | [文本细读与文学论证](../07_fields/languages-literature/practices/close_reading.md)、[语言记录与语言学田野调查](../07_fields/languages-literature/practices/language_documentation.md) |
| 哲学、伦理与宗教 | [哲学论证研究](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md) |
| 艺术 | [基于实践的研究](../07_fields/arts/practices/practice_based_research.md) |

各学科的整体规矩见[学科篇](../07_fields/README.md)。

### 计算机

只在计算机里使用的研究实践，放在 `07_fields/computer-science/practices/`：

- [工程研究](../07_fields/computer-science/practices/engineering_research.md)：提出并评估新的方法、工具或系统
- [基准评测](../07_fields/computer-science/practices/benchmarking.md)：用自动化、可重复的流程比较系统、工具或模型
- [优化研究](../07_fields/computer-science/practices/optimization_study.md)：把问题建模成优化问题，用搜索求解
- [仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)：从代码仓库、缺陷库和问答网站中挖数据
- [理论研究](../07_fields/computer-science/practices/theoretical_research.md)：证明与形式化分析
