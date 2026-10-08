# 研究方法

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

你已经选定了研究套路，知道要拿出什么样的证据。现在你想知道：具体用什么方法拿到这些证据，怎样把这个方法做好？

这一层回答的就是这个问题。

## 方法和套路的分工

- **研究套路**讲"这个项目产生什么知识、需要什么证据"，见[研究套路](../05_research-strategies/README.md)。
- **研究方法**讲"具体怎么做好"：步骤、关键决定、检查清单和常见错误。
- **一个方法可以服务多个套路。** 例如对照实验既能用来比较两个已有工具，也能用来检验"X 导致 Y"。所以下表每一行都列出它常服务的套路。
- **哪些方法放在这里**：两个及以上学科都用的方法放在这一层；只有一个学科用的实践，放在该学科的文件夹里（见本页末尾）。

这样的分工是本手册的约定 `[本项目分析]`。

怎样根据问题选套路和方法，见[选定研究套路和方法](../02_from-project-to-study/02_choose-strategy-and-method.md)。

## 14 种方法

"常服务的套路"一列依据各套路页"常用的研究方法"一节；套路页没有列到的，写"暂未列出"。

### 以已发表的研究为材料

| 方法 | 做什么 | 常服务的套路 |
|---|---|---|
| [综述研究](review_study.md) | 系统综述、映射研究和综述论文：把已发表的研究收集起来，汇总、分析 | [综合](../05_research-strategies/synthesize.md)、[观察描述](../05_research-strategies/observe_describe.md) |
| [案例调查](case_survey.md) | 把已发表的大量案例研究编码成数据集，再做定量分析 | [综合](../05_research-strategies/synthesize.md) |
| [方法论研究与元科学](meta_science.md) | 研究"怎么做研究"：方法指南、批判性综述、研究实践调查 | [综合](../05_research-strategies/synthesize.md)、[测量](../05_research-strategies/measure.md) |

### 基于已有数据或模型

| 方法 | 做什么 | 常服务的套路 |
|---|---|---|
| [数据科学研究](data_science.md) | 对已有数据做预测建模或统计建模，用结果回答科学问题 | [观察描述](../05_research-strategies/observe_describe.md) |
| [纵向研究](longitudinal_study.md) | 长时间重复观察同一批对象，看它怎样变化 | [观察描述](../05_research-strategies/observe_describe.md) |
| [定量仿真](simulation_study.md) | 建立模仿真实系统的计算模型，在模型上做实验 | [构建改进](../05_research-strategies/build_improve.md) |

### 涉及人的研究

| 方法 | 做什么 | 常服务的套路 |
|---|---|---|
| [对照实验](controlled_experiment.md) | 有人参与，随机分组，比较一个因素对人的表现有什么影响 | [比较评估](../05_research-strategies/compare_evaluate.md)、[解释因果](../05_research-strategies/explain_causality.md)、[构建改进](../05_research-strategies/build_improve.md) |
| [问卷调查](questionnaire_survey.md) | 用问卷向大量人收集数据，再系统分析 | [观察描述](../05_research-strategies/observe_describe.md)、[测量](../05_research-strategies/measure.md) |
| [访谈研究](interview_study.md) | 深度访谈一批人，用定性分析归纳主题 | [观察描述](../05_research-strategies/observe_describe.md) |
| [案例研究与民族志](case_study.md) | 在真实环境里深入研究少数对象 | [观察描述](../05_research-strategies/observe_describe.md)、[解释因果](../05_research-strategies/explain_causality.md) |
| [扎根理论](grounded_theory.md) | 一边收集数据一边分析，从数据中逐步归纳出理论 | [观察描述](../05_research-strategies/observe_describe.md) |
| [行动研究](action_research.md) | 和真实组织合作推动一项改变，一边改进一边研究 | 暂未列出 |

### 跨方法

| 方法 | 做什么 | 常服务的套路 |
|---|---|---|
| [复现研究](replication.md) | 有计划地重做已发表的研究，检验结论是否成立 | [比较评估](../05_research-strategies/compare_evaluate.md)、[测量](../05_research-strategies/measure.md) |
| [混合方法](mixed_methods.md) | 用两种及以上方法研究同一个问题 | [解释因果](../05_research-strategies/explain_causality.md) |

分组是本手册为了方便查找做的归纳 `[本项目分析]`。

## 这些方法篇的适用范围

`[本项目分析]` 这 14 篇原来是为计算机写的，主要面向软件工程：大多数篇目的检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，例子也多来自软件工程。方法本身多个学科都在用，但具体规范各学科不同。每篇开头的"适用范围"一段写明了它的资料来自哪里。

如果你不在计算机领域，先看本学科的规范和下面的学科方法篇，再把这里的方法篇当作参考。

### 其他学科专门的方法篇

| 学科 | 方法篇 |
|---|---|
| 临床医学 | [随机对照试验](randomized_controlled_trial.md) |
| 健康科学 | [系统综述与元分析（健康领域）](meta_analysis.md)、[观察性流行病学研究](observational_epidemiology.md) |
| 基础医学 | [临床前动物研究](preclinical_animal_study.md) |
| 生物科学 | [实验台实验（湿实验）](bench_experiment.md) |
| 化学科学 | [合成与表征研究](synthesis_study.md) |
| 物理科学 | [实验测量研究](experimental_measurement.md) |
| 地球与环境科学 | [野外观测研究](field_study.md) |
| 农业、林业与渔业 | [田间试验](../07_fields/agriculture/practices/field_trial.md) |
| 经济学与商学 | [田野实验](field_experiment.md)、[准实验与因果识别](quasi_experiment.md) |
| 心理学与认知科学 | [量表编制与测量研究](scale_development.md) |
| 政治学 | [过程追踪与比较案例研究](process_tracing.md) |
| 社会与经济地理学 | [空间分析研究](../07_fields/geography/practices/spatial_analysis.md) |
| 教育学 | [基于设计的研究](../07_fields/education/practices/design_based_research.md) |
| 法学 | [规范法学研究](../07_fields/law/practices/doctrinal_research.md) |
| 历史与考古 | [考古发掘与野外调查](../07_fields/history-archaeology/practices/archaeological_excavation.md)、[档案研究](archival_research.md)、[口述历史](oral_history.md) |
| 语言与文学 | [文本细读与文学论证](../07_fields/languages-literature/practices/close_reading.md)、[语言记录与语言学田野调查](../07_fields/languages-literature/practices/language_documentation.md) |
| 哲学、伦理与宗教 | [哲学论证研究](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md) |
| 艺术 | [基于实践的研究](../07_fields/arts/practices/practice_based_research.md) |

共 23 篇，列表和学科分类见[学科篇：其他学科的研究类型](../07_fields/README.md#其他学科的研究类型)。

### 计算机特有的实践

只在计算机里使用的研究实践，放在 `07_fields/computer-science/practices/`：

- [工程研究](../07_fields/computer-science/practices/engineering_research.md)：提出并评估新的方法、工具或系统
- [基准评测](../07_fields/computer-science/practices/benchmarking.md)：用自动化、可重复的流程比较系统、工具或模型
- [优化研究](../07_fields/computer-science/practices/optimization_study.md)：把问题建模成优化问题，用搜索求解
- [仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)：从代码仓库、缺陷库和问答网站中挖数据
- [理论研究](../07_fields/computer-science/practices/theoretical_research.md)：证明与形式化分析
