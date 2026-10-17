# 机器学习

> 本页只写这个方向特有的做法；通用做法见第一部分、第二部分各章和研究套路，计算机共通的规矩见[计算机学科概况](../README.md)。

## 这个方向研究什么

机器学习研究让计算机从数据中学到规律，再用学到的模型去预测或生成。常见的问题有两类（这个划分是本项目的归纳）`[本项目分析]`：

- **提出更好的方法**：一种新的模型结构、训练方法或优化技巧，在公认的基准上是否比已有方法更好，好在哪里、为什么。
- **用机器学习回答别的学科的问题**：REFORMS 清单（一份给这类研究的报告清单）把它叫作"基于机器学习的科学"，即把模型的预测表现当作科学主张的证据[^kapoor2024reforms-e1]。

先分清两件事。多数机器学习研究关注在训练时没见过的新样本上预测得准；传统统计更关注估计能代表真实生成过程的参数[^kapoor2024reforms-e3]。你的论文属于哪一种，决定了要拿什么证据。

本页也覆盖自然语言处理（让计算机处理人类语言的方向）里以模型为主的研究。原因是两边的审稿清单同源：ACL 滚动评审（ACL Rolling Review，ARR，计算语言学学会 ACL 的统一审稿服务；ACL 即 Association for Computational Linguistics）的清单，大体以 NeurIPS（Conference on Neural Information Processing Systems，神经信息处理系统大会）2021 年的论文检查清单为基础[^arr2024responsible-e13]。

## 主要发表处和节奏

下面以两个会议为例：

- **NeurIPS**：机器学习方向的大型会议，用 2025 年的规定；
- **ARR**：自然语言处理方向的统一审稿服务，用它按 2024 年 10 月一轮更新的清单。

它们只是例子，不代表这个方向所有会议的做法。规定每年会变，**以你要投的会议当年的说明为准**。NeurIPS 2025 的截稿日期、页数、双盲和预印本规定，已写在[学科概况：一篇会议论文的一生](../README.md#一篇会议论文的一生)和[双盲评审与预印本](../README.md#双盲评审与预印本)，这里只补充别处没写的：

| 环节 | 规定（会议和年份） |
|---|---|
| 检查清单 | NeurIPS 2025：不附清单直接拒稿[^neurips2025checklist-e1]；清单随最终版公开[^neurips2025checklist-e14]。ARR：在投稿表单里填[^arr2024responsible-e3] |
| 作者回复 | NeurIPS 2025：回复期不能交修改稿，只能在审稿平台上发讨论[^neurips2025cfp-e11]；之后还能回答追问[^neurips2025cfp-e12] |
| 公开审稿 | NeurIPS 2025：录用论文的审稿意见和作者回复都公开；被拒论文可自愿公开[^neurips2025cfp-e13] |
| 代码 | NeurIPS 2025：不强制公开代码，但要给出某种合理的复现途径[^neurips2025checklist-e8]；不能只因没附代码而拒稿，除非代码就是贡献，例如新的开源基准[^neurips2025checklist-e9] |

复现在这个方向有专门的渠道。NeurIPS 2019 办过复现挑战赛，目标是独立验证已录用论文的实证主张，并公开留档[^pineau2021improving-e8]。也有会议专门征集复现论文；还有一份开放获取的同行评审期刊 ReScience C，专门发表复现研究[^pineau2021improving-e9]。怎样做复现研究，见[复现研究](../../../06_methods/replication.md)。

## 常用套路与证据标准

下表是本项目按机器学习的资料归纳的；每条标准只代表脚注里那份资料的要求 `[本项目分析]`。通用的公平比较要求（同等调参、多次运行、留一份数据最后检验）见[比较评估](../../../05_research-strategies/compare_evaluate.md#2-什么样的证据才够)，这里只写这个方向的特点。

| 套路 | 在这个方向的样子 | 这个方向特别看重的证据 | 具体做法 |
|---|---|---|---|
| [构建改进](../../../05_research-strategies/build_improve.md) | 新模型、新训练方法 | 既和简单基线比，说明新增的复杂度有必要[^lones2021avoid-e1]，也和当前最好的方法比[^lones2021avoid-e2]；做消融实验（逐个去掉组成部分，看效果怎么变），说明提升从哪来[^lipton2019troubling-e4] | [工程研究](../practices/engineering_research.md)、[优化研究](../practices/optimization_study.md) |
| [比较评估](../../../05_research-strategies/compare_evaluate.md) | 在公共基准上比较已有模型 | 用多个数据集评估[^lones2021avoid-e17]；整个社区反复在同一测试集上比，排第一的模型可能只是碰巧过拟合了它[^lones2021avoid-e15] | [基准评测](../practices/benchmarking.md) |
| [测量](../../../05_research-strategies/measure.md) | 建新数据集或基准，检查评测靠不靠得住 | 查数据污染（见下文），它会高估模型的表现[^sainz2023nlp-e2]；同一指标的不同实现结果不同，要写明实现和版本[^arr2024responsible-e10] | [基准评测：基准本身有效吗](../practices/benchmarking.md#3-基准本身有效吗) |
| [解释因果](../../../05_research-strategies/explain_causality.md) | 解释方法为什么有效 | 最强的实证论文常做错误分析、消融实验和稳健性检查[^lipton2019troubling-e8]；推测放进单独标明的一节，和有证据的结论分开[^lipton2019troubling-e3] | [数据科学：解释结果](../../../06_methods/data_science.md#第八步解释结果相关不等于因果) |
| [证明](../../../05_research-strategies/prove.md) | 学习理论、收敛性、泛化界 | NeurIPS 2025 清单：写全所有假设，给出完整证明[^neurips2025checklist-e16] | [理论研究](../practices/theoretical_research.md) |

用机器学习回答别的学科的问题时，套路按你的核心主张来定。写清目标总体、被预测的变量代表什么、怎样论证没有泄漏，都见[数据科学](../../../06_methods/data_science.md#第一步写清主张目标总体和结果变量)。

## 这个方向特有的规矩

### 审稿看检查清单

NeurIPS 2025 和 ARR 都要求填检查清单。ARR 说，清单相当于给审稿人的常见问题解答，提前回答本来会在作者回复期被问到的问题[^arr2024responsible-e4]。NeurIPS 2025 要求审稿人把清单当作评价因素之一[^neurips2025checklist-e2]。

两份清单里和证据直接相关的几项（各以该会议当年的说明为准）：

- **主张不超出结果**：主张要和结果能推广的程度相符（NeurIPS 2025）[^neurips2025checklist-e12]。
- **写出局限**：审稿人被明确要求不要因为作者诚实写局限而扣分（NeurIPS 2025）[^neurips2025checklist-e4]。
- **误差线说清楚**：写明它反映哪种波动，例如数据划分、初始化[^neurips2025checklist-e5]，是标准差还是标准误[^neurips2025checklist-e6]；每个结果是单次运行、多个随机种子里的最大值还是平均值（ARR）[^arr2024responsible-e9]。
- **超参数**：写清怎么选的（NeurIPS 2025）[^neurips2025checklist-e15]；除特殊情况外，不在评测用的留出数据上调（ARR）[^arr2024responsible-e8]。
- **算力**：说明整个项目是否用了比论文实验更多的算力，包括没写进论文的失败实验（NeurIPS 2025）[^neurips2025checklist-e7]；ARR 也要求包括所有实验，而不只是最终那几次[^arr2024responsible-e7]。

答"否"或"不适用"一般不是拒稿理由，只要给出理由[^neurips2025checklist-e3][^arr2024responsible-e2]。但 ARR 对系统性地既不指出对应章节、也不给理由的投稿直接拒稿[^arr2024responsible-e1]。ARR 建议早点读清单，它会影响你怎样做研究[^arr2024responsible-e5]。

### 小心数据泄漏和数据污染

"测试数据只在最后用一次"、怎样防止数据泄漏，见[比较评估：留一份数据只用于最后检验](../../../05_research-strategies/compare_evaluate.md#留一份数据只用于最后检验)和[数据科学：先划分数据，再做任何处理](../../../06_methods/data_science.md#第三步先划分数据再做任何处理)。

大语言模型带来了一个新问题：**数据污染**，即模型在某个基准的测试集上训练过，又在同一基准上评测[^sainz2023nlp-e1]。模型见过评测集，实验就完全无效[^sainz2023nlp-e3]。用别人训练的大模型做评测时，要先查它的训练数据是否可能含有你的测试集 `[本项目分析]`。

### 数据、代码和资产

- **写清用了谁的、哪个版本**：用别人的代码、数据、模型，写明版本和许可证名称（NeurIPS 2025）[^neurips2025checklist-e13]；语言数据要写明是什么语言，常用基准也一样（ARR）[^arr2024responsible-e6]。
- **公开代码有用，但不够**：拿到原代码不等于代码是对的，照论文描述重新实现也很有价值[^pineau2021improving-e4]；有的实验算力大到多数研究者无法复现[^pineau2021improving-e5]。
- **复现很少是"能或不能"**：NeurIPS 2019 复现挑战赛的多数报告，给出的是方法、结果、主张分别复现到什么程度[^pineau2021improving-e6]。

### 伦理和社会影响

- **看得到滥用的路径就要写**：NeurIPS 2025 清单承认很多论文是基础研究，不和具体应用挂钩[^neurips2025checklist-e18]；但看到通向有害应用的直接路径时，要指出来[^neurips2025checklist-e11]。ARR 列出的风险还包括训练超大模型的环境影响[^arr2024responsible-e16]。
- **标注者和参与者**：按 NeurIPS 伦理准则，参与数据收集、整理的人员报酬至少达到所在国最低工资[^neurips2025checklist-e10]；ARR 要求写明每项任务付多少钱、怎样估计耗时[^arr2024responsible-e11]。
- **伦理审查批准不等于不用讨论社会影响**（ARR）[^arr2024responsible-e12]。
- **用了大模型**：各会议规定不同，通用做法和 NeurIPS 2025 的例子见[科研诚信与伦理：用大模型等工具时，责任仍然在你](../../../08_throughout/integrity_and_ethics.md#6-用大模型等工具时责任仍然在你)。

## 常见错误

通用的比较错误（基线不调参、只跑一次、在测试集上反复试）见[比较评估：常见错误](../../../05_research-strategies/compare_evaluate.md#6-常见错误)。这个方向特别常见的：

| 错误 | 为什么是问题 |
|---|---|
| 一次加很多改动，不做消融实验 | 看不出提升从哪来；有时真正起作用的只有一个改动[^lipton2019troubling-e4] |
| 只和当前最好的方法比，不和简单基线比 | 说明不了新增的复杂度有必要[^lones2021avoid-e1] |
| 只在一个数据集上评估 | 多个数据集才能评得更严谨[^lones2021avoid-e17] |
| 评测大模型时不查基准是否被污染 | 污染会高估模型表现[^sainz2023nlp-e2] |
| 把推测写成解释 | 读者会当成定论[^lipton2019troubling-e2] |
| 怕被拒而不写局限 | 审稿人自己发现没写的局限，后果可能更糟[^neurips2025checklist-e17] |
| 清单上答"否"却不给理由 | ARR 对系统性不给理由的投稿直接拒稿[^arr2024responsible-e1] |

## 延伸阅读

- **Lipton & Steinhardt 2019，Troubling Trends in Machine Learning Scholarship**：机器学习论文的四种常见毛病，每种都配了正反例子。写第一篇论文前读。
- **Lones 2021，How to avoid machine learning pitfalls**：按数据、建模、评估、比较、报告的顺序列出常见陷阱。
- **Kapoor & Narayanan 2023 和 Kapoor 等人 2024（REFORMS 清单）**：数据泄漏的分类和"基于机器学习的科学"的报告清单。用机器学习回答别的学科的问题时读。
- **Pineau 等人 2021，Improving Reproducibility in Machine Learning Research**：NeurIPS 检查清单和复现挑战赛的来由。
- **你要投的会议当年的检查清单**，例如 NeurIPS 的论文检查清单指南、ARR 的负责任自然语言处理研究清单（Responsible NLP Research Checklist）：每一项都附了怎样回答的说明。投稿前对照着检查。
- 同一学科的其他方向：[人机交互](hci.md)、[系统](systems.md)、[安全](security.md)、[软件工程](software_engineering.md)、[理论](theory.md)、[程序设计语言](programming_languages.md)。

[^kapoor2024reforms-e1]: Kapoor 等人 2024，The scope of our claims。[证据](../../../../sources/notes/kapoor2024reforms.md#e1)
[^kapoor2024reforms-e3]: Kapoor 等人 2024，Module 1，1c。[证据](../../../../sources/notes/kapoor2024reforms.md#e3)
[^arr2024responsible-e13]: ACL 滚动评审负责任 NLP 研究清单，开头。[证据](../../../../sources/notes/arr2024responsible.md#e13)
[^neurips2025checklist-e1]: NeurIPS 论文检查清单指南，开头段。[证据](../../../../sources/notes/neurips2025checklist.md#e1)
[^neurips2025checklist-e14]: NeurIPS 论文检查清单指南，答题说明。[证据](../../../../sources/notes/neurips2025checklist.md#e14)
[^arr2024responsible-e3]: ACL 滚动评审负责任 NLP 研究清单，开头。[证据](../../../../sources/notes/arr2024responsible.md#e3)
[^neurips2025cfp-e11]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../../../sources/notes/neurips2025cfp.md#e11)
[^neurips2025cfp-e12]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../../../sources/notes/neurips2025cfp.md#e12)
[^neurips2025cfp-e13]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../../../sources/notes/neurips2025cfp.md#e13)
[^neurips2025checklist-e8]: NeurIPS 论文检查清单指南，第 4 项。[证据](../../../../sources/notes/neurips2025checklist.md#e8)
[^neurips2025checklist-e9]: NeurIPS 论文检查清单指南，第 5 项。[证据](../../../../sources/notes/neurips2025checklist.md#e9)
[^pineau2021improving-e8]: Pineau 等人 2021，§4。[证据](../../../../sources/notes/pineau2021improving.md#e8)
[^pineau2021improving-e9]: Pineau 等人 2021，§6。[证据](../../../../sources/notes/pineau2021improving.md#e9)
[^lones2021avoid-e1]: Lones 2021，§5.2。[证据](../../../../sources/notes/lones2021avoid.md#e1)
[^lones2021avoid-e2]: Lones 2021，§5.2。[证据](../../../../sources/notes/lones2021avoid.md#e2)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019，§3.2。[证据](../../../../sources/notes/lipton2019troubling.md#e4)
[^lones2021avoid-e17]: Lones 2021，§6.2。[证据](../../../../sources/notes/lones2021avoid.md#e17)
[^lones2021avoid-e15]: Lones 2021，§5.5。[证据](../../../../sources/notes/lones2021avoid.md#e15)
[^sainz2023nlp-e2]: Sainz 等人 2023，摘要。[证据](../../../../sources/notes/sainz2023nlp.md#e2)
[^arr2024responsible-e10]: ACL 滚动评审负责任 NLP 研究清单，C4。[证据](../../../../sources/notes/arr2024responsible.md#e10)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019，§5.1。[证据](../../../../sources/notes/lipton2019troubling.md#e8)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019，§3.1。[证据](../../../../sources/notes/lipton2019troubling.md#e3)
[^neurips2025checklist-e16]: NeurIPS 论文检查清单指南，第 3 项。[证据](../../../../sources/notes/neurips2025checklist.md#e16)
[^arr2024responsible-e4]: ACL 滚动评审负责任 NLP 研究清单，开头。[证据](../../../../sources/notes/arr2024responsible.md#e4)
[^neurips2025checklist-e2]: NeurIPS 论文检查清单指南，答题说明。[证据](../../../../sources/notes/neurips2025checklist.md#e2)
[^neurips2025checklist-e12]: NeurIPS 论文检查清单指南，第 1 项 Claims。[证据](../../../../sources/notes/neurips2025checklist.md#e12)
[^neurips2025checklist-e4]: NeurIPS 论文检查清单指南，第 2 项 Limitations。[证据](../../../../sources/notes/neurips2025checklist.md#e4)
[^neurips2025checklist-e5]: NeurIPS 论文检查清单指南，第 7 项。[证据](../../../../sources/notes/neurips2025checklist.md#e5)
[^neurips2025checklist-e6]: NeurIPS 论文检查清单指南，第 7 项。[证据](../../../../sources/notes/neurips2025checklist.md#e6)
[^arr2024responsible-e9]: ACL 滚动评审负责任 NLP 研究清单，C3。[证据](../../../../sources/notes/arr2024responsible.md#e9)
[^neurips2025checklist-e15]: NeurIPS 论文检查清单指南，第 6 项。[证据](../../../../sources/notes/neurips2025checklist.md#e15)
[^arr2024responsible-e8]: ACL 滚动评审负责任 NLP 研究清单，C2。[证据](../../../../sources/notes/arr2024responsible.md#e8)
[^neurips2025checklist-e7]: NeurIPS 论文检查清单指南，第 8 项。[证据](../../../../sources/notes/neurips2025checklist.md#e7)
[^arr2024responsible-e7]: ACL 滚动评审负责任 NLP 研究清单，C1。[证据](../../../../sources/notes/arr2024responsible.md#e7)
[^neurips2025checklist-e3]: NeurIPS 论文检查清单指南，答题说明。[证据](../../../../sources/notes/neurips2025checklist.md#e3)
[^arr2024responsible-e2]: ACL 滚动评审负责任 NLP 研究清单，Guidelines for Answering Checklist Questions。[证据](../../../../sources/notes/arr2024responsible.md#e2)
[^arr2024responsible-e1]: ACL 滚动评审负责任 NLP 研究清单，Guidelines for Answering Checklist Questions。[证据](../../../../sources/notes/arr2024responsible.md#e1)
[^arr2024responsible-e5]: ACL 滚动评审负责任 NLP 研究清单，Guidelines for Answering Checklist Questions。[证据](../../../../sources/notes/arr2024responsible.md#e5)
[^sainz2023nlp-e1]: Sainz 等人 2023，摘要。[证据](../../../../sources/notes/sainz2023nlp.md#e1)
[^sainz2023nlp-e3]: Sainz 等人 2023，§3。[证据](../../../../sources/notes/sainz2023nlp.md#e3)
[^neurips2025checklist-e13]: NeurIPS 论文检查清单指南，第 12 项 Licenses。[证据](../../../../sources/notes/neurips2025checklist.md#e13)
[^arr2024responsible-e6]: ACL 滚动评审负责任 NLP 研究清单，B5。[证据](../../../../sources/notes/arr2024responsible.md#e6)
[^pineau2021improving-e4]: Pineau 等人 2021，§3。[证据](../../../../sources/notes/pineau2021improving.md#e4)
[^pineau2021improving-e5]: Pineau 等人 2021，§3。[证据](../../../../sources/notes/pineau2021improving.md#e5)
[^pineau2021improving-e6]: Pineau 等人 2021，§4。[证据](../../../../sources/notes/pineau2021improving.md#e6)
[^neurips2025checklist-e18]: NeurIPS 论文检查清单指南，第 10 项 Broader Impacts。[证据](../../../../sources/notes/neurips2025checklist.md#e18)
[^neurips2025checklist-e11]: NeurIPS 论文检查清单指南，第 10 项。[证据](../../../../sources/notes/neurips2025checklist.md#e11)
[^arr2024responsible-e16]: ACL 滚动评审负责任 NLP 研究清单，A2。[证据](../../../../sources/notes/arr2024responsible.md#e16)
[^neurips2025checklist-e10]: NeurIPS 论文检查清单指南，第 14 项。[证据](../../../../sources/notes/neurips2025checklist.md#e10)
[^arr2024responsible-e11]: ACL 滚动评审负责任 NLP 研究清单，D2。[证据](../../../../sources/notes/arr2024responsible.md#e11)
[^arr2024responsible-e12]: ACL 滚动评审负责任 NLP 研究清单，D4。[证据](../../../../sources/notes/arr2024responsible.md#e12)
[^lipton2019troubling-e2]: Lipton & Steinhardt 2019，§3.1。[证据](../../../../sources/notes/lipton2019troubling.md#e2)
[^neurips2025checklist-e17]: NeurIPS 论文检查清单指南，第 2 项 Limitations。[证据](../../../../sources/notes/neurips2025checklist.md#e17)
