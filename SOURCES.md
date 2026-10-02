# 资料目录

- **核实日期**：2026-10-02。"✓"表示已打开原始页面，确认了标题、作者和出处；"⚠"表示部分核实，具体情况见说明。
- **适用阶段**：P1 为实证研究，P2 为方案层面的创新（工具/方法 + 评估），P3 为选题。详见项目章程。
- star 数和最后更新日期取自 GitHub 页面（2026-10-02），只作参考。**star 多不代表内容经过验证。**

## 1. 质量标准（评估时的主要依据）

| 资料 | 出处 | 阶段 | 研究类型 | 核实 | 用途 |
|---|---|---|---|---|---|
| [ACM SIGSOFT Empirical Standards](https://www2.sigsoft.org/EmpiricalStandards/)（[GitHub](https://github.com/acmsigsoft/EmpiricalStandards)） | Ralph et al., [arXiv:2010.03525](https://arxiv.org/abs/2010.03525)，2020 | P1–P3 | 全部 | ✓ | 为 19 种研究方法分别给出必要、加分、优秀三档要求，以及反面模式、可接受的偏离、不成立的批评和范例论文。与 P1 直接相关的有：`GeneralStandard`、`SystematicReviews`、`Replication`、`RepositoryMining`、`Benchmarking`、`DataScience`；P2 相关的有 `EngineeringResearch`。还有 `Sampling`、`InterRaterReliabilityAndAgreement`、`OpenScience` 等补充文档。许可为 CC0。 |
| [Guidelines for Empirical Studies in SE involving LLMs](https://arxiv.org/abs/2508.15503)（[llm-guidelines.org](https://llm-guidelines.org/)） | Baltes et al.，Empirical Software Engineering，2026（arXiv v7） | P1–P2 | 涉及 LLM 的研究 | ✓ | 8 条指南，包括声明 LLM 的使用、报告模型版本和配置、公开提示词和交互日志、用人工验证 LLM 输出、用开源模型作 baseline 等。也可以用来检查 agent 自己产出的研究。 |
| [REFORMS](https://reforms.cs.princeton.edu/) | Kapoor et al.，Science Advances 10(18)，2024，[doi:10.1126/sciadv.adk3452](https://doi.org/10.1126/sciadv.adk3452) | P1–P2 | 基于 ML 的研究 | ✓ | 分 8 个部分、共 32 项的检查清单，针对基于机器学习的科研。 |
| [Dos and Don'ts of Machine Learning in Computer Security](https://arxiv.org/abs/2010.09470) | Arp et al.，USENIX Security 2022 | P1–P2 | 安全 + ML | ✓ | 基于对 30 篇安全顶会论文的分析，总结设计、实现和评估中的常见陷阱。 |
| [Evaluating Fuzz Testing](https://doi.org/10.1145/3243734.3243804) | Klees et al.，ACM CCS 2018 | P1–P2 | 工具评测（模糊测试） | ✓ | 调研 32 篇模糊测试论文的评估方法，指出常见问题并给出建议。 |
| [SoK: Benchmarking Flaws in Systems Security](https://www.vusec.net/projects/benchmarking-crimes/) | van der Kouwe et al.，IEEE EuroS&P 2019 | P1–P2 | 工具评测（系统安全） | ⚠ | 标题、作者、会议已核实，IEEE DOI 未找到。总结了 22 种 benchmark 误用，基于 50 篇论文。早期技术报告为 "Benchmarking Crimes: An Emerging Threat in Systems Security"（[arXiv:1801.02381](https://arxiv.org/abs/1801.02381)，2018）。 |

## 2. 方法论

| 资料 | 出处 | 阶段 | 研究类型 | 核实 | 用途 |
|---|---|---|---|---|---|
| [Guidelines for performing Systematic Literature Reviews in Software Engineering](https://ebse.webspace.durham.ac.uk/ebse-bibliography/guidelines-for-performing-systematic-literature-reviews-in-software-engineering/) | Kitchenham & Charters，Technical Report EBSE-2007-01，v2.3，2007 | P1 | SLR | ✓ | SE 领域 SLR 的基础指南：规划、执行、报告三个阶段，研究方案（protocol）应包含的内容，筛选、质量评估、数据提取与综合的方法。 |
| [Guidelines for conducting systematic mapping studies in software engineering: An update](https://doi.org/10.1016/j.infsof.2015.03.007) | Petersen, Vakkalanka, Kuzniarz，Information and Software Technology 64，2015 | P1 | 映射研究 | ⚠ | 出处已核实；全文在付费墙后，尚未读到。目前只引用其对映射研究和 SLR 的区分。 |
| [Guidelines for snowballing in systematic literature studies and a replication in software engineering](https://doi.org/10.1145/2601248.2601268) | Wohlin，EASE 2014 | P1 | SLR | ⚠ | 出处已核实；全文未读到。滚雪球检索的具体步骤目前引用自下一条 Wohlin 等人 2022 年论文中的描述。 |
| [Successful Combination of Database Search and Snowballing for Identification of Primary Studies in Systematic Literature Studies](https://arxiv.org/abs/2307.02612) | Wohlin, Kalinowski, Felizardo, Mendes，Information and Software Technology 147，2022 | P1 | SLR | ✓ | 数据库检索与滚雪球结合的混合检索策略，比单独检索多找到约 30% 的一手研究；还提出了"wild card"和"borderline article"的处理方式。 |
| [A practical guide for using statistical tests to assess randomized algorithms in software engineering](https://doi.org/10.1145/1985793.1985795) | Arcuri & Briand，ICSE 2011 | P1–P2 | 工具评测 | ✓ | 如何用统计检验比较带随机性的算法或工具。另有扩展的期刊版本（STVR 2014），未核实。 |
| PRISMA Statement | Moher et al.，PLoS Medicine，2009 | P1 | SLR | — | 由 SIGSOFT Systematic Reviews 标准引用，本仓库未单独核实。 |
| The Seven Types of Literature Review | Ralph & Baltes，ESEC/FSE 2022 IVR | P1 | SLR | — | 由 SIGSOFT Systematic Reviews 标准引用，本仓库未单独核实。 |

## 3. "如何做好科研"的经典文章

| 资料 | 出处 | 阶段 | 核实 | 用途 |
|---|---|---|---|---|
| [You and Your Research](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html) | Richard Hamming，1986 年演讲文字稿 | P3 | ✓ | 如何选择重要的问题、如何做出有影响力的研究。 |
| [Ten Simple Rules for Doing Your Best Research, According to Hamming](https://doi.org/10.1371/journal.pcbi.0030213) | Erren et al.，PLoS Computational Biology，2007 | P3 | ✓ | 对上面演讲的归纳。 |
| [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html) | John Schulman，2020 | P2–P3 | ✓ | 如何选题、如何推进 ML 研究。 |
| [Tips for Empirical Alignment Research](https://www.alignmentforum.org/posts/dZFpEdKyb9Bf4xYn7/tips-for-empirical-alignment-research) | Ethan Perez，2024 | P1–P2 | ✓ | 实证研究的具体做法，比如快速迭代实验、避免在错误方向上浪费时间。 |
| [How to Write a Great Research Paper](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) | Simon Peyton Jones | 全部 | ✓ | 论文写作。 |
| [How to Read a Paper](https://doi.org/10.1145/1273445.1273458) | S. Keshav，ACM SIGCOMM CCR 37(3)，2007 | 全部 | ✓ | 三遍阅读法。 |
| [A Survival Guide to a PhD](http://karpathy.github.io/2016/09/07/phd/) | Andrej Karpathy，2016 | P3 | ✓ | 选题、研究习惯等。 |

## 4. 面向研究者的资源合集

| 资料 | 核实 | 说明 |
|---|---|---|
| [jbhuang0604/awesome-tips](https://github.com/jbhuang0604/awesome-tips) | ✓ | Jia-Bin Huang 整理的研究、写作、审稿、职业建议，约 4.7k star，最后更新 2025-12。 |
| [pliang279/awesome-phd-advice](https://github.com/pliang279/awesome-phd-advice) | ✓ | Paul Liang（CMU）整理的博士生建议链接合集，约 2.2k star，最后更新 2023-06。 |
| [shaily99/advice](https://github.com/shaily99/advice) | ✓ | Shaily Bhatt 整理的研究和申请建议链接合集，约 2.6k star，最后更新 2023-10。 |

## 5. Agent 科研 skills 参考

> **注意**：这些仓库大多没有公开的评估证据，无法说明加入后研究质量是否提高；领域也大多与 P1 不匹配。按 ROADMAP 的原则，**不应在没有证据的情况下直接搬进系统**。合理的用法有两种：参考它们组织知识的方式；或者在 S2 中作为外部 baseline 的一部分（例如"通用 agent + 某套 skills"）。

| 资料 | 核实 | 说明 |
|---|---|---|
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | ✓ | 约 11.4k star，98 个 skills，以 ML 工程为主（微调、分布式训练、推理部署等），大部分对应 P4。MIT。 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | ✓ | 原名 claude-scientific-skills。约 47.3k star，177 个 skills，面向生物信息、化学信息、临床、材料等领域，与本项目领域不重合。MIT。 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | ✓ | Claude Code 插件，包含深度调研、论文写作、审稿和一个 10 阶段的流程，带人工检查点。页面显示约 48.2k star。**许可为 CC BY-NC 4.0（禁止商用）。** |
| [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | ✓ | 科研类 agent skills 的索引，约 554 star。MIT。 |

## 6. AI Scientist 相关系统合集（相关工作，不是科研知识）

| 资料 | 核实 | 说明 |
|---|---|---|
| [ResearAI/Awesome-AI-Scientist](https://github.com/ResearAI/Awesome-AI-Scientist) | ✓ | 按知识、选题、实验、写作、审稿组织的论文和工具列表，约 304 star，最后更新 2025-11。许可信息不一致（LICENSE 文件为 Apache-2.0，README 写的是 MIT）。 |
| [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | ✓ | 原 ai-boost/awesome-ai-for-science，已迁移。AI for Science 的工具、论文、数据集合集，约 2k star。 |
| [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) | ✓ | 按 8 个研究阶段整理的自动化科研论文列表，约 536 star。配套综述 arXiv 2605.18661，未核实。 |
