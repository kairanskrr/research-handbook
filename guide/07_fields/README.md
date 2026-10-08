# 学科篇

不同学科的研究运转方式不同：研究节奏、组织方式、发表文化、伦理要求、什么证据才会被接受，都不一样 `[本项目分析]`。学科篇**只写学科特有的内容**；多个学科通用的研究方法（对照实验、问卷、访谈、案例研究、综述、复现等）放在[研究方法](../06_methods/README.md)，学科篇里链接过去，只说明本学科的差异。分层规则见[重构计划 §4](../../docs/restructure-plan.md#4-目录结构)。

每个学科一个文件夹，里面有：

- `README.md`：学科概况，讲这个学科的研究实际怎样运转，有哪些规矩和常见陷阱；
- `practices/`（部分学科有）：只有这个学科使用的研究实践，每篇讲流程、关键决策、检查清单和常见错误。

## 学科分类

学科篇按经济合作与发展组织（OECD）《Frascati Manual 2015》中的研究与开发领域分类（Fields of Research and Development，FORD）组织，共 6 个大类、42 个二级学科 `oecd2015frascati`。中文名为本项目翻译。

| 代码 | 学科 | 英文原名 | 学科篇 |
|---|---|---|---|
| **1** | **自然科学** | **Natural sciences** | |
| 1.1 | 数学 | Mathematics | 学科概况，初稿，待审阅：[`README.md`](mathematics/README.md) |
| 1.2 | 计算机与信息科学 | Computer and information sciences | 学科概况和 5 篇独有实践，初稿，待审阅：见下文[计算机](#计算机)一节 |
| 1.3 | 物理科学 | Physical sciences | 学科概况，初稿，待审阅：[`README.md`](physical-sciences/README.md) |
| 1.4 | 化学科学 | Chemical sciences | 学科概况，初稿，待审阅：[`README.md`](chemistry/README.md) |
| 1.5 | 地球及相关环境科学 | Earth and related environmental sciences | 学科概况，初稿，待审阅：[`README.md`](earth-environmental-sciences/README.md) |
| 1.6 | 生物科学 | Biological sciences | 学科概况，初稿，待审阅：[`README.md`](biological-sciences/README.md) |
| 1.7 | 其他自然科学 | Other natural sciences | 不单独写，见相近学科 |
| **2** | **工程与技术** | **Engineering and technology** | |
| 2.1 | 土木工程 | Civil engineering | 学科概况，初稿，待审阅：[`README.md`](civil-engineering/README.md) |
| 2.2 | 电气工程、电子工程、信息工程 | Electrical engineering, electronic engineering, information engineering | 学科概况，初稿，待审阅：[`README.md`](electrical-engineering/README.md) |
| 2.3 | 机械工程 | Mechanical engineering | 学科概况，初稿，待审阅：[`README.md`](mechanical-engineering/README.md) |
| 2.4 | 化学工程 | Chemical engineering | 学科概况，初稿，待审阅：[`README.md`](chemical-engineering/README.md) |
| 2.5 | 材料工程 | Materials engineering | 学科概况，初稿，待审阅：[`README.md`](materials-engineering/README.md) |
| 2.6 | 医学工程 | Medical engineering | 学科概况，初稿，待审阅：[`README.md`](medical-engineering/README.md) |
| 2.7 | 环境工程 | Environmental engineering | 学科概况，初稿，待审阅：[`README.md`](environmental-engineering/README.md) |
| 2.8 | 环境生物技术 | Environmental biotechnology | 见[生物技术](biotechnology/README.md)（初稿，待审阅） |
| 2.9 | 工业生物技术 | Industrial biotechnology | 见[生物技术](biotechnology/README.md)（初稿，待审阅） |
| 2.10 | 纳米技术 | Nano-technology | 见[材料工程与纳米技术](materials-engineering/README.md)（初稿，待审阅） |
| 2.11 | 其他工程与技术 | Other engineering and technologies | 不单独写，见相近学科 |
| **3** | **医学与健康科学** | **Medical and health sciences** | |
| 3.1 | 基础医学 | Basic medicine | 学科概况，初稿，待审阅：[`README.md`](basic-medicine/README.md) |
| 3.2 | 临床医学 | Clinical medicine | 学科概况，初稿，待审阅：[`README.md`](clinical-medicine/README.md) |
| 3.3 | 健康科学 | Health sciences | 学科概况，初稿，待审阅：[`README.md`](health-sciences/README.md) |
| 3.4 | 医学生物技术 | Medical biotechnology | 见[生物技术](biotechnology/README.md)（初稿，待审阅） |
| 3.5 | 其他医学科学 | Other medical sciences | 不单独写，见[基础医学](basic-medicine/README.md)、[临床医学](clinical-medicine/README.md)、[健康科学](health-sciences/README.md) |
| **4** | **农业与兽医科学** | **Agricultural and veterinary sciences** | |
| 4.1 | 农业、林业与渔业 | Agriculture, forestry, and fisheries | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](agriculture/README.md)；[田间试验](agriculture/practices/field_trial.md) |
| 4.2 | 动物与乳品科学 | Animal and dairy science | 学科概况，初稿，待审阅：[`README.md`](animal-veterinary-science/README.md) |
| 4.3 | 兽医科学 | Veterinary science | 见[动物科学与兽医学](animal-veterinary-science/README.md)（初稿，待审阅） |
| 4.4 | 农业生物技术 | Agricultural biotechnology | 见[生物技术](biotechnology/README.md)（初稿，待审阅） |
| 4.5 | 其他农业科学 | Other agricultural sciences | 不单独写，见[农业、林业与渔业](agriculture/README.md) |
| **5** | **社会科学** | **Social sciences** | |
| 5.1 | 心理学与认知科学 | Psychology and cognitive sciences | 学科概况，初稿，待审阅：[`README.md`](psychology/README.md) |
| 5.2 | 经济学与商学 | Economics and business | 学科概况，初稿，待审阅：[`README.md`](economics/README.md) |
| 5.3 | 教育学 | Education | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](education/README.md)；[基于设计的研究](education/practices/design_based_research.md) |
| 5.4 | 社会学 | Sociology | 学科概况，初稿，待审阅：[`README.md`](sociology/README.md) |
| 5.5 | 法学 | Law | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](law/README.md)；[规范法学研究](law/practices/doctrinal_research.md) |
| 5.6 | 政治学 | Political science | 学科概况，初稿，待审阅：[`README.md`](political-science/README.md) |
| 5.7 | 社会与经济地理学 | Social and economic geography | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](geography/README.md)；[空间分析研究](geography/practices/spatial_analysis.md) |
| 5.8 | 媒体与传播 | Media and communications | 学科概况，初稿，待审阅：[`README.md`](media-communication/README.md) |
| 5.9 | 其他社会科学 | Other social sciences | 不单独写，见[社会学](sociology/README.md)及相近学科 |
| **6** | **人文与艺术** | **Humanities and the arts** | |
| 6.1 | 历史与考古 | History and archaeology | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](history-archaeology/README.md)；[考古发掘与野外调查](history-archaeology/practices/archaeological_excavation.md) |
| 6.2 | 语言与文学 | Languages and literature | 学科概况和 2 篇独有实践，初稿，待审阅：[`README.md`](languages-literature/README.md)；[文本细读与文学论证](languages-literature/practices/close_reading.md)、[语言记录与语言学田野调查](languages-literature/practices/language_documentation.md) |
| 6.3 | 哲学、伦理与宗教 | Philosophy, ethics and religion | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](philosophy-ethics-religion/README.md)；[哲学论证研究](philosophy-ethics-religion/practices/philosophical_argument.md) |
| 6.4 | 艺术 | Arts (arts, history of arts, performing arts, music) | 学科概况和 1 篇独有实践，初稿，待审阅：[`README.md`](arts/README.md)；[基于实践的研究](arts/practices/practice_based_research.md) |
| 6.5 | 其他人文学科 | Other humanities | 不单独写，见[语言与文学](languages-literature/README.md)、[历史与考古](history-archaeology/README.md)、[哲学、伦理与宗教](philosophy-ethics-religion/README.md) |

计算机篇对应 1.2。计算机工程、信息工程方向的部分内容在分类上属于 2.2，两者有交叉。

## 计算机

- **学科概况**：[`computer-science/README.md`](computer-science/README.md)，讲以会议为中心的发表方式、预印本、制品评估，以及各方向的惯例差异。初稿，待审阅。
- **计算机特有的研究实践**：[计算机特有的研究实践](computer-science/practices/README.md)，目前有[工程研究](computer-science/practices/engineering_research.md)、[优化研究](computer-science/practices/optimization_study.md)、[基准评测](computer-science/practices/benchmarking.md)、[仓库挖掘研究](computer-science/practices/repository_mining.md)、[理论研究](computer-science/practices/theoretical_research.md)五篇。初稿，待审阅。
- **通用的研究方法**：综述、对照实验、问卷、访谈、案例研究、复现等在多个学科通用，放在[研究方法](../06_methods/README.md)。

## 学科独有的实践

只有一个学科使用、[研究方法](../06_methods/README.md)没有收录的做法，单独成篇，放在对应学科的 `practices/` 下。多个学科都用的方法（对照实验、随机对照试验、问卷、访谈、档案研究、复现等）放在研究方法，不在这里重复；各学科概况的"本学科常用的研究方法"一节链接过去，并说明本学科的差异。

| 学科 | 独有实践 | 状态 |
|---|---|---|
| 农业、林业与渔业 | [田间试验](agriculture/practices/field_trial.md) | 初稿，待审阅 |
| 社会与经济地理学 | [空间分析研究](geography/practices/spatial_analysis.md) | 初稿，待审阅 |
| 教育学 | [基于设计的研究](education/practices/design_based_research.md) | 初稿，待审阅 |
| 法学 | [规范法学研究](law/practices/doctrinal_research.md) | 初稿，待审阅 |
| 历史与考古 | [考古发掘与野外调查](history-archaeology/practices/archaeological_excavation.md) | 初稿，待审阅 |
| 语言与文学 | [文本细读与文学论证](languages-literature/practices/close_reading.md) | 初稿，待审阅 |
| 语言与文学 | [语言记录与语言学田野调查](languages-literature/practices/language_documentation.md) | 初稿，待审阅 |
| 哲学、伦理与宗教 | [哲学论证研究](philosophy-ethics-religion/practices/philosophical_argument.md) | 初稿，待审阅 |
| 艺术 | [基于实践的研究](arts/practices/practice_based_research.md) | 初稿，待审阅 |
| 计算机与信息科学 | [工程研究](computer-science/practices/engineering_research.md) | 初稿，待审阅 |
| 计算机与信息科学 | [优化研究](computer-science/practices/optimization_study.md) | 初稿，待审阅 |
| 计算机与信息科学 | [基准评测](computer-science/practices/benchmarking.md) | 初稿，待审阅 |
| 计算机与信息科学 | [仓库挖掘研究](computer-science/practices/repository_mining.md) | 初稿，待审阅 |
| 计算机与信息科学 | [理论研究](computer-science/practices/theoretical_research.md) | 初稿，待审阅 |

一项研究靠什么逻辑产生知识、该用哪些方法，先看[研究套路](../05_research-strategies/README.md)。
