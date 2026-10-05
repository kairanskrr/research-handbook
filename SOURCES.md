# 资料目录

- **核实日期**：2026-10-02，2026-10-05 补充。"✓"表示已打开原始页面，确认了标题、作者和出处；"⚠"表示部分核实，具体情况见说明。
- **适用阶段**：P1 为实证研究，P2 为方案层面的创新（工具/方法 + 评估），P3 为选题。详见项目章程。
- star 数和最后更新日期取自 GitHub 页面（2026-10-02），只作参考。**star 多不代表内容经过验证。**

## 1. 质量标准（评估时的主要依据）

| 资料 | 出处 | 阶段 | 研究类型 | 核实 | 用途 |
|---|---|---|---|---|---|
| [ACM SIGSOFT Empirical Standards](https://www2.sigsoft.org/EmpiricalStandards/)（[GitHub](https://github.com/acmsigsoft/EmpiricalStandards)） | Ralph et al., [arXiv:2010.03525](https://arxiv.org/abs/2010.03525)，2020 | P1–P3 | 全部 | ✓ | 为 19 种研究方法分别给出必要、加分、优秀三档要求，以及反面模式、可接受的偏离、不成立的批评和范例论文。与 P1 直接相关的有：`GeneralStandard`、`SystematicReviews`、`Replication`、`RepositoryMining`、`Benchmarking`、`DataScience`；P2 相关的有 `EngineeringResearch`。还有 `Sampling`、`InterRaterReliabilityAndAgreement`、`OpenScience` 等补充文档。许可为 CC0。 |
| [Guidelines for Empirical Studies in SE involving LLMs](https://arxiv.org/abs/2508.15503)（[llm-guidelines.org](https://llm-guidelines.org/)） | Baltes et al.，Empirical Software Engineering，2026（arXiv v7） | P1–P2 | 涉及 LLM 的研究 | ✓ | 8 条指南，包括声明 LLM 的使用、报告模型版本和配置、公开提示词和交互日志、用人工验证 LLM 输出、用开源模型作 baseline 等。也可以用来检查 agent 自己产出的研究。 |
| [REFORMS](https://reforms.cs.princeton.edu/) | Kapoor et al.，Science Advances 10(18)，2024，[doi:10.1126/sciadv.adk3452](https://doi.org/10.1126/sciadv.adk3452) | P1–P2 | 基于 ML 的研究 | ✓ | 分 8 个部分、共 32 项的检查清单，针对基于机器学习的科研。 |
| [Dos and Don'ts of Machine Learning in Computer Security](https://arxiv.org/abs/2010.09470) | Arp et al.，USENIX Security 2022 | P1–P2 | 安全 + ML | ✓ | 基于对 30 篇安全顶会论文的分析，总结设计、实现和评估中的常见陷阱。 |
| [Evaluating Fuzz Testing](https://doi.org/10.1145/3243734.3243804)（[免费全文](https://arxiv.org/pdf/1808.09700)） | Klees et al.，ACM CCS 2018 | P1–P2 | 工具评测（模糊测试） | ✓ | 调研 32 篇模糊测试论文的评估方法，指出常见问题并给出建议。 |
| [SoK: Benchmarking Flaws in Systems Security](https://www.vusec.net/projects/benchmarking-crimes/)（[免费全文](https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf)） | van der Kouwe et al.，IEEE EuroS&P 2019 | P1–P2 | 工具评测（系统安全） | ✓ | 已打开完整的 SoK 全文；IEEE DOI 未在登记库中核实。总结了 22 种 benchmark 误用（分为 A–F 六组），基于 50 篇论文。早期技术报告为 "Benchmarking Crimes: An Emerging Threat in Systems Security"（[arXiv:1801.02381](https://arxiv.org/abs/1801.02381)，2018）。 |

## 2. 方法论

| 资料 | 出处 | 阶段 | 研究类型 | 核实 | 用途 |
|---|---|---|---|---|---|
| [Guidelines for performing Systematic Literature Reviews in Software Engineering](https://ebse.webspace.durham.ac.uk/ebse-bibliography/guidelines-for-performing-systematic-literature-reviews-in-software-engineering/) | Kitchenham & Charters，Technical Report EBSE-2007-01，v2.3，2007 | P1 | SLR | ✓ | SE 领域 SLR 的基础指南：规划、执行、报告三个阶段，研究方案（protocol）应包含的内容，筛选、质量评估、数据提取与综合的方法。 |
| [Guidelines for conducting systematic mapping studies in software engineering: An update](https://doi.org/10.1016/j.infsof.2015.03.007) | Petersen, Vakkalanka, Kuzniarz，Information and Software Technology 64，2015 | P1 | 映射研究 | ⚠ | 出处已核实；全文在付费墙后，尚未读到，见第 7 节"待获取"。目前只引用其对映射研究和 SLR 的区分。 |
| [Systematic Mapping Studies in Software Engineering](https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf) | Petersen, Feldt, Mujtaba, Mattsson，EASE 2008，[doi:10.14236/ewic/EASE2008.8](https://doi.org/10.14236/ewic/EASE2008.8) | P1 | 映射研究 | ✓ | 映射研究的原始指南：五步流程、通过关键词标注建立分类方案、映射研究与系统性综述的区别。出版社版本以 CC BY 4.0 开放获取。 |
| [Guidelines for snowballing in systematic literature studies and a replication in software engineering](https://doi.org/10.1145/2601248.2601268)（[作者主页全文](https://www.wohlin.eu/ease14.pdf)） | Wohlin，EASE 2014 | P1 | SLR | ✓ | 滚雪球检索的原始指南：起始集的选择、向后/向前滚雪球、迭代与停止条件；并用滚雪球重做了已发表的 SLR 作对比。 |
| [Successful Combination of Database Search and Snowballing for Identification of Primary Studies in Systematic Literature Studies](https://arxiv.org/abs/2307.02612) | Wohlin, Kalinowski, Felizardo, Mendes，Information and Software Technology 147，2022 | P1 | SLR | ✓ | 数据库检索与滚雪球结合的混合检索策略，比单独检索多找到约 30% 的一手研究；还提出了"wild card"和"borderline article"的处理方式。 |
| [A practical guide for using statistical tests to assess randomized algorithms in software engineering](https://doi.org/10.1145/1985793.1985795) | Arcuri & Briand，ICSE 2011 | P1–P2 | 工具评测 | ✓ | 如何用统计检验比较带随机性的算法或工具。另有扩展的期刊版本（STVR 2014），未核实。 |
| [The PRISMA Statement](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000097) | Moher et al.，PLoS Medicine 6(7)，2009 | P1 | SLR | ✓ | 系统性综述的报告规范（2009 版），开放获取。 |
| [The PRISMA 2020 statement](https://www.bmj.com/content/372/bmj.n71) | Page et al.，BMJ 372:n71，2021 | P1 | SLR | ✓ | 更新版报告规范：7 个部分共 27 项，以及新版流程图。注意它规范的是报告，而不是执行。开放获取。 |
| [Paving the Way for Mature Secondary Research: The Seven Types of Literature Review](https://arxiv.org/abs/2205.01163) | Ralph & Baltes，ESEC/FSE 2022 IVR | P1 | SLR | ✓ | 把文献综述分为七类，并建议 SE 领域多做元分析、案例调查、元综合，少做范围综述和快速综述。 |

### 后续研究类型将用到的资料（已确认有免费全文）

| 资料 | 出处 | 研究类型 | 核实 | 用途 |
|---|---|---|---|---|
| [The promises and perils of mining GitHub](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf) | Kalliamvakou et al.，MSR 2014 | 数据挖掘研究 | ✓ | 挖掘 GitHub 数据时的常见陷阱。作者自存档版本。 |
| [An in-depth study of the promises and perils of mining GitHub](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf) | Kalliamvakou et al.，Empirical Software Engineering 21(5)，2016 | 数据挖掘研究 | ✓ | 上一篇的扩展期刊版。 |
| [The promises and perils of mining git](https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf) | Bird et al.，MSR 2009 | 数据挖掘研究 | ✓ | 挖掘 git 历史数据时的陷阱。 |
| [It's not a bug, it's a feature: how misclassification impacts bug prediction](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf) | Herzig, Just, Zeller，ICSE 2013 | 数据挖掘研究 | ✓ | issue 数据中的分类错误及其对研究结论的影响。 |
| [Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current) | ACM，v1.1，2020 | 复现研究 | ✓ | ACM 的复现材料评审与徽章政策，区分了可用、可用且已评估、结果已复现等级别。 |

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

## 7. 待获取（需要付费或无法直接访问）

以下资料有价值，但目前无法读到全文。获取到 PDF 后只用于阅读和概括，**不要把 PDF 放进本仓库**。

| 优先级 | 资料 | 用途 | 情况 |
|---|---|---|---|
| 高 | Petersen, Vakkalanka, Kuzniarz (2015)，[Guidelines for conducting systematic mapping studies in software engineering: An update](https://doi.org/10.1016/j.infsof.2015.03.007)，IST 64 | 映射研究的更新版指南和评估清单 | 出版社付费。BTH 机构库可能有免费 PDF：[diva2:815606](http://www.diva-portal.org/smash/record.jsf?pid=diva2:815606)，需要用浏览器确认 |
| 高 | Gómez, Juristo, Vegas (2014)，[Understanding replication of experiments in software engineering: A classification](https://doi.org/10.1016/j.infsof.2014.04.004)，IST 56(8) | 复现研究的分类，整理"复现研究"的核心依据 | 付费，未找到自存档版本 |
| 中 | Wohlin et al.，[Experimentation in Software Engineering](https://doi.org/10.1007/978-3-662-69306-3)（第 2 版，Springer 2024） | 威胁效度的经典论述 | 付费书籍；只需要讲效度的部分 |
| 中 | Arcuri & Briand (2014)，[A Hitchhiker's guide to statistical tests for assessing randomized algorithms in software engineering](https://doi.org/10.1002/stvr.1486)，STVR 24(3) | 工具评测中的统计检验 | 付费；ICSE 2011 短版可能在 ACM 免费，未能确认 |
| 中 | Shull, Carver, Vegas, Juristo (2008)，[The role of replications in Empirical Software Engineering](https://doi.org/10.1007/s10664-008-9060-1)，EMSE 13(2) | 复现研究的定位 | 付费 |
| 低 | Carver (2010)，[Towards Reporting Guidelines for Experimental Replications: A Proposal](https://carver.cs.ua.edu/ReplicationGuidelines.htm)，RESER 2010 | 复现研究的报告规范 | 作者主页有 PDF，但链接在 http/https 之间循环跳转，需要用浏览器下载 |
| 低 | Felderer & Travassos (eds.)，[Contemporary Empirical Methods in Software Engineering](https://doi.org/10.1007/978-3-030-32489-6)，Springer 2020 | 多种实证方法的较新综述 | 付费，仅第 17 章（Open Science）开放获取；需要先看目录挑选章节 |
| 低 | Runeson & Höst (2009)，[Guidelines for conducting and reporting case study research in software engineering](https://doi.org/10.1007/s10664-008-9102-8)，EMSE 14(2) | 案例研究指南，其中的效度讨论有参考价值 | 可能是开放获取（CC BY-NC），但 Springer 限流，未能打开确认 |

