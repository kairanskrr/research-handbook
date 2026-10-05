# 怎么做好科研：整理内容

这里是我们从[原始资料](../sources/README.md)中整理出来的内容，用中文写给科研新手。目标是：读完能明白怎么做好科研，并能照着完成实际的研究工作。

## 怎么读

- **刚开始做科研**：先读通用篇，它讲所有学科共通的研究流程和经验。
- **要做某个领域的研究**：再读对应的领域篇，了解这个领域的研究如何运转。
- **要用某种具体方法**：读对应的研究类型文档，里面有流程、关键决策、质量标准和常见错误。

每条结论都用脚注标出依据。点开脚注可以看到出自哪份资料、原文在哪里、原文怎么说。没有文献依据、属于我们自己的分析，标注 `[本项目分析]`；不确定的内容标注 `[待确认]`。不同资料说法不一致时，会并列写出各自的做法和理由。

## 三个层次

| 层次 | 回答的问题 | 位置 |
|---|---|---|
| 通用篇 | 所有学科共通的研究流程；什么是好的研究；选题、读文献、写作、审稿、合作等经验 | `general/`（未开始） |
| 领域篇 | 这个领域的研究实际怎样运转：研究节奏、组织方式、发表文化、领域惯例和常见陷阱 | `fields/<领域>/README.md` |
| 研究类型 | 领域内常见的研究方法：每种方法的流程、关键决策、质量标准和反面模式 | `fields/<领域>/research-types/` |

大致的分工是：**原则写进通用篇，具体做法写进研究类型，惯例写进领域篇。** 各阶段的名称在不同研究中基本相同（选题、了解已有工作、设计、产生证据、分析、写作、发表），共用的原则也很多，例如结论不超出证据、诚实披露局限；但同一个阶段的具体做法随研究方法而变，例如"文献调研"在一般研究中是背景工作，在系统综述中则是研究方法本身。ACM SIGSOFT Empirical Standards 也认为不存在通用的质量标准，每项研究应按其方法的标准评判。`[本项目分析]`

## 通用篇

| # | 章节 | 状态 |
|---|---|---|
| 1 | 什么是研究，什么是好的研究 | 未开始 |
| 2 | 选题 | 未开始 |
| 3 | 读文献与文献调研 | 未开始 |
| 4 | 研究设计与方法选择 | 未开始 |
| 5 | 证据、分析与效度 | 未开始 |
| 6 | 推进研究项目：迭代、去风险、长线管理 | 未开始 |
| 7 | 写作 | 未开始 |
| 8 | 审稿、回复审稿意见与发表 | 未开始 |
| 9 | 合作与导师 | 未开始 |
| 10 | 科研诚信与伦理 | 未开始 |
| 11 | 心态与长期积累 | 未开始 |

## 学科分类

领域篇按 OECD《Frascati Manual 2015》中的研究与开发领域分类（Fields of Research and Development，FORD）组织，共 6 个大类、42 个二级学科 `oecd2015frascati`。中文名为本项目翻译。

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

位置：[`fields/computer-science/`](fields/computer-science/README.md)。领域概况（研究节奏、组织方式、发表文化、惯例）：未开始。

### 研究类型

以研究类型为主线。类型划分依据 ACM SIGSOFT Empirical Standards 的方法分类。这套标准面向软件工程，多数类型也适用于计算机的其他方向；它不覆盖理论研究，这一类由本项目补充。分组为本项目分析。另有一份适用于所有类型的 General Standard，会在各研究类型文档中引用。

| 分组 | 研究类型 | 对应的 SIGSOFT 标准 | 状态 |
|---|---|---|---|
| 文献类 | 系统性文献综述与映射研究 | Systematic Reviews | 初版，待审阅：[`slr.md`](fields/computer-science/research-types/slr.md)，第一批（定稿） |
| | 案例调查（案例元分析） | Case Survey | 未开始 |
| | 方法论研究与元科学 | Methodological Guidelines and Meta-Science | 未开始 |
| 构建与评估 | 工程研究（设计科学）：提出并评估新的方法、工具或系统 | Engineering Research | 未开始，第一批 |
| | 优化研究（含基于搜索的软件工程） | Optimization Studies | 未开始 |
| | 基准评测 | Benchmarking | 未开始，第一批 |
| | 定量仿真 | Simulation (Quantitative) | 未开始 |
| 基于已有数据 | 仓库挖掘 | Repository Mining | 未开始，第一批 |
| | 数据科学 | Data Science | 未开始 |
| | 纵向研究 | Longitudinal Studies | 未开始 |
| 涉及人的研究 | 对照实验（有人类参与者） | Experiments | 未开始 |
| | 问卷调查 | Questionnaire Surveys | 未开始 |
| | 定性访谈 | Qualitative Surveys | 未开始 |
| | 案例研究与民族志 | Case Study and Ethnography | 未开始 |
| | 扎根理论 | Grounded Theory | 未开始 |
| | 行动研究 | Action Research | 未开始 |
| 跨方法 | 复现研究 | Replication | 未开始 |
| | 混合方法 | Multi-Methodology and Mixed Methods | 未开始 |
| 理论 | 理论研究（证明、形式化分析） | 无，本项目补充 | 未开始 |

