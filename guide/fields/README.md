# 领域篇

不同领域的研究运转方式不同：研究节奏、组织方式、发表文化、领域惯例都不一样。每个领域一个文件夹，里面有：

- `README.md`：领域概况——这个领域的研究实际怎样运转，有哪些惯例和常见陷阱
- `research-types/`：这个领域常见的研究类型（研究方法），每种的流程、关键决策、检查清单和常见错误

领域决定经验和惯例，研究类型决定方法规范；同一种研究方法在不同领域往往相近，研究类型文档可以跨领域引用。`[本项目分析]`

## 学科分类

领域篇按经济合作与发展组织（OECD）《Frascati Manual 2015》中的研究与开发领域分类（Fields of Research and Development，FORD）组织，共 6 个大类、42 个二级学科 `oecd2015frascati`。中文名为本项目翻译。

| 代码 | 学科 | 英文原名 | 领域篇 |
|---|---|---|---|
| **1** | **自然科学** | **Natural sciences** | |
| 1.1 | 数学 | Mathematics | 未开始 |
| 1.2 | 计算机与信息科学 | Computer and information sciences | **进行中**：[计算机领域篇](#计算机领域篇) |
| 1.3 | 物理科学 | Physical sciences | 未开始 |
| 1.4 | 化学科学 | Chemical sciences | 未开始 |
| 1.5 | 地球及相关环境科学 | Earth and related environmental sciences | 未开始 |
| 1.6 | 生物科学 | Biological sciences | 未开始 |
| 1.7 | 其他自然科学 | Other natural sciences | 未开始 |
| **2** | **工程与技术** | **Engineering and technology** | |
| 2.1 | 土木工程 | Civil engineering | 未开始 |
| 2.2 | 电气工程、电子工程、信息工程 | Electrical engineering, electronic engineering, information engineering | 未开始 |
| 2.3 | 机械工程 | Mechanical engineering | 未开始 |
| 2.4 | 化学工程 | Chemical engineering | 未开始 |
| 2.5 | 材料工程 | Materials engineering | 未开始 |
| 2.6 | 医学工程 | Medical engineering | 未开始 |
| 2.7 | 环境工程 | Environmental engineering | 未开始 |
| 2.8 | 环境生物技术 | Environmental biotechnology | 未开始 |
| 2.9 | 工业生物技术 | Industrial biotechnology | 未开始 |
| 2.10 | 纳米技术 | Nano-technology | 未开始 |
| 2.11 | 其他工程与技术 | Other engineering and technologies | 未开始 |
| **3** | **医学与健康科学** | **Medical and health sciences** | |
| 3.1 | 基础医学 | Basic medicine | 未开始 |
| 3.2 | 临床医学 | Clinical medicine | 未开始 |
| 3.3 | 健康科学 | Health sciences | 未开始 |
| 3.4 | 医学生物技术 | Medical biotechnology | 未开始 |
| 3.5 | 其他医学科学 | Other medical sciences | 未开始 |
| **4** | **农业与兽医科学** | **Agricultural and veterinary sciences** | |
| 4.1 | 农业、林业与渔业 | Agriculture, forestry, and fisheries | 未开始 |
| 4.2 | 动物与乳品科学 | Animal and dairy science | 未开始 |
| 4.3 | 兽医科学 | Veterinary science | 未开始 |
| 4.4 | 农业生物技术 | Agricultural biotechnology | 未开始 |
| 4.5 | 其他农业科学 | Other agricultural sciences | 未开始 |
| **5** | **社会科学** | **Social sciences** | |
| 5.1 | 心理学与认知科学 | Psychology and cognitive sciences | 未开始 |
| 5.2 | 经济学与商学 | Economics and business | 未开始 |
| 5.3 | 教育学 | Education | 未开始 |
| 5.4 | 社会学 | Sociology | 未开始 |
| 5.5 | 法学 | Law | 未开始 |
| 5.6 | 政治学 | Political science | 未开始 |
| 5.7 | 社会与经济地理学 | Social and economic geography | 未开始 |
| 5.8 | 媒体与传播 | Media and communications | 未开始 |
| 5.9 | 其他社会科学 | Other social sciences | 未开始 |
| **6** | **人文与艺术** | **Humanities and the arts** | |
| 6.1 | 历史与考古 | History and archaeology | 未开始 |
| 6.2 | 语言与文学 | Languages and literature | 未开始 |
| 6.3 | 哲学、伦理与宗教 | Philosophy, ethics and religion | 未开始 |
| 6.4 | 艺术 | Arts (arts, history of arts, performing arts, music) | 未开始 |
| 6.5 | 其他人文学科 | Other humanities | 未开始 |

计算机领域篇对应 1.2。计算机工程、信息工程方向的部分内容在分类上属于 2.2，两者有交叉。

## 计算机领域篇

位置：[`computer-science/`](computer-science/README.md)。领域概况（研究节奏、组织方式、发表文化、惯例）：初稿，待审阅。

### 研究类型

以研究类型为主线。类型划分依据 ACM SIGSOFT Empirical Standards（美国计算机协会软件工程分会制定的一套实证研究标准）的方法分类。这套标准面向软件工程，多数类型也适用于计算机的其他方向；它不覆盖理论研究，这一类由本项目补充。分组为本项目分析。另有一份适用于所有类型的 General Standard，会在各研究类型文档中引用。

| 分组 | 研究类型 | 对应的 SIGSOFT 标准 | 状态 |
|---|---|---|---|
| 文献类 | 综述研究：系统综述、映射研究、综述论文 | Systematic Reviews | 初稿，待审阅：[`review_study.md`](computer-science/research-types/review_study.md)。研究类型文档的样板 |
|  | 案例调查（案例元分析） | Case Survey | 初稿，待审阅：[`case_survey.md`](computer-science/research-types/case_survey.md) |
|  | 方法论研究与元科学 | Methodological Guidelines and Meta-Science | 初稿，待审阅：[`meta_science.md`](computer-science/research-types/meta_science.md) |
| 构建与评估 | 工程研究：提出并评估新的方法、工具或系统 | Engineering Research | 初稿，待审阅：[`engineering_research.md`](computer-science/research-types/engineering_research.md) |
|  | 优化研究（含基于搜索的软件工程） | Optimization Studies | 初稿，待审阅：[`optimization_study.md`](computer-science/research-types/optimization_study.md) |
| | 基准评测 | Benchmarking | 初稿，待审阅：[`benchmarking.md`](computer-science/research-types/benchmarking.md) |
|  | 定量仿真 | Simulation (Quantitative) | 初稿，待审阅：[`simulation_study.md`](computer-science/research-types/simulation_study.md) |
| 基于已有数据 | 仓库挖掘 | Repository Mining | 初稿，待审阅：[`repository_mining.md`](computer-science/research-types/repository_mining.md) |
|  | 数据科学 | Data Science | 初稿，待审阅：[`data_science.md`](computer-science/research-types/data_science.md) |
|  | 纵向研究 | Longitudinal Studies | 初稿，待审阅：[`longitudinal_study.md`](computer-science/research-types/longitudinal_study.md) |
| 涉及人的研究 | 对照实验（有人类参与者） | Experiments | 初稿，待审阅：[`controlled_experiment.md`](computer-science/research-types/controlled_experiment.md) |
|  | 问卷调查 | Questionnaire Surveys | 初稿，待审阅：[`questionnaire_survey.md`](computer-science/research-types/questionnaire_survey.md) |
|  | 访谈研究（定性访谈） | Qualitative Surveys | 初稿，待审阅：[`interview_study.md`](computer-science/research-types/interview_study.md) |
|  | 案例研究与民族志 | Case Study and Ethnography | 初稿，待审阅：[`case_study.md`](computer-science/research-types/case_study.md) |
|  | 扎根理论 | Grounded Theory | 初稿，待审阅：[`grounded_theory.md`](computer-science/research-types/grounded_theory.md) |
|  | 行动研究 | Action Research | 初稿，待审阅：[`action_research.md`](computer-science/research-types/action_research.md) |
| 跨方法 | 复现研究 | Replication | 初稿，待审阅：[`replication.md`](computer-science/research-types/replication.md) |
|  | 混合方法 | Multi-Methodology and Mixed Methods | 初稿，待审阅：[`mixed_methods.md`](computer-science/research-types/mixed_methods.md) |
| 理论 | 理论研究（证明、形式化分析） | 无，本项目补充 | 初稿，待审阅：[`theoretical_research.md`](computer-science/research-types/theoretical_research.md) |
