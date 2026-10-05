# Merevo Resources：科研方法资料库

为 Auto Research 项目收集的科研方法资料，按 awesome 列表的形式整理：各类研究应该怎么做、什么是好的研究、常见陷阱有哪些，以及相关的数据集、工具和论文列表。

> **现阶段的用途是评估，而不是 agent 能力**。这些资料用来定义"什么是好的研究"，作为评估 agent 产出质量的参照（服务于 S1）。是否把其中的知识做成 agent 的 skills，要等 S2 的实验证据出来后再决定。另外，同一套知识不宜既当 agent 的操作指南、又当评估标准，否则 agent 可能学会"对着评分表打勾"。

## 怎么用

| 内容 | 位置 |
|---|---|
| 所有论文的引用信息（BibTeX） | [`papers/references.bib`](papers/references.bib) |
| 论文索引与获取情况 | [`papers/README.md`](papers/README.md) |
| 下载有免费全文的论文 PDF | 在仓库根目录运行 `bash scripts/fetch_papers.sh`，PDF 保存在 `papers/pdf/` |
| GitHub 仓库的上游地址与固定版本 | [`repos/README.md`](repos/README.md) |
| 按研究类型整理的笔记 | [`research-types/`](research-types/) |
| 团队内部材料 | [`internal/`](internal/) |

**图例**：🆓 有免费全文 · 💰 需要付费 · 📦 GitHub 仓库 · `key` 为 `references.bib` 中的条目。P1 为实证研究，P2 为方案层面的创新，P3 为选题（见项目章程）。

## 目录

- [质量标准与报告规范](#质量标准与报告规范)
- [研究方法指南](#研究方法指南)
  - [系统性文献综述与映射研究](#系统性文献综述与映射研究)
  - [复现研究](#复现研究)
  - [数据挖掘研究](#数据挖掘研究)
  - [工具与模型评测](#工具与模型评测)
  - [实证研究通用](#实证研究通用)
- [数据集与工具](#数据集与工具)
- [论文列表](#论文列表)
- [可复现研究](#可复现研究)
- [如何做好科研](#如何做好科研)
- [Agent 科研 skills（仅供参考）](#agent-科研-skills仅供参考)
- [AI Scientist 相关系统](#ai-scientist-相关系统)
- [本仓库的整理笔记](#本仓库的整理笔记)
- [待获取](#待获取)

## 质量标准与报告规范

评估研究质量时的主要依据。

- [ACM SIGSOFT Empirical Standards](https://www2.sigsoft.org/EmpiricalStandards/) - Ralph 等人，2020 起持续更新。为 19 种研究方法分别列出必要、加分、优秀三档要求，以及反面模式、可接受的偏离、不成立的批评和范例论文。与 P1 直接相关的有 General、Systematic Reviews、Replication、Repository Mining、Benchmarking、Data Science；P2 相关的有 Engineering Research。采用 CC0 许可。📦 🆓 `ralph2020empirical`
- [Guidelines for Empirical Studies in Software Engineering involving Large Language Models](https://llm-guidelines.org/) - Baltes 等人，Empirical Software Engineering 2026。8 条指南：声明 LLM 的使用、报告模型版本和配置、公开提示词和交互日志、用人工验证 LLM 输出、用开源模型作 baseline 等。也可以用来检查 agent 自己产出的研究。🆓 `baltes2026guidelines`
- [REFORMS](https://reforms.cs.princeton.edu/) - Kapoor 等人，Science Advances 2024。针对基于机器学习的科研，分 8 个部分共 32 项的检查清单。`kapoor2024reforms`
- [PRISMA 2020](https://www.bmj.com/content/372/bmj.n71) - Page 等人，BMJ 2021。系统性综述的报告规范：7 个部分共 27 项，以及流程图模板。注意它规范的是报告，而不是执行。🆓 `page2021prisma`
- [PRISMA 2009](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000097) - Moher 等人，PLoS Medicine 2009。上一版报告规范，很多 SE 综述仍在引用。🆓 `moher2009prisma`

## 研究方法指南

### 系统性文献综述与映射研究

- [Guidelines for performing Systematic Literature Reviews in Software Engineering](https://ebse.webspace.durham.ac.uk/ebse-bibliography/guidelines-for-performing-systematic-literature-reviews-in-software-engineering/) - Kitchenham & Charters，技术报告 EBSE-2007-01，2007。SE 领域 SLR 的基础指南：规划、执行、报告三个阶段，研究方案的内容，筛选、质量评估、数据提取与综合；附定量和定性研究的质量评估清单。🆓 `kitchenham2007guidelines`
- [Systematic Mapping Studies in Software Engineering](https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf) - Petersen 等人，EASE 2008。映射研究的原始指南：五步流程、通过关键词标注建立分类方案、映射研究与系统性综述的区别。🆓 `petersen2008systematic`
- [Guidelines for conducting systematic mapping studies in software engineering: An update](https://doi.org/10.1016/j.infsof.2015.03.007) - Petersen 等人，IST 2015。映射研究指南的更新版。💰 `petersen2015guidelines`
- [Guidelines for snowballing in systematic literature studies and a replication in software engineering](https://www.wohlin.eu/ease14.pdf) - Wohlin，EASE 2014。滚雪球检索的原始指南：起始集的选择、向前/向后滚雪球、停止条件；并用滚雪球重做了已发表的 SLR 作对比。🆓 `wohlin2014guidelines`
- [Successful Combination of Database Search and Snowballing for Identification of Primary Studies in Systematic Literature Studies](https://arxiv.org/abs/2307.02612) - Wohlin 等人，IST 2022。数据库检索与滚雪球结合的混合策略，比单独数据库检索多找到约 30% 的一手研究。🆓 `wohlin2022successful`
- [Paving the Way for Mature Secondary Research: The Seven Types of Literature Review](https://arxiv.org/abs/2205.01163) - Ralph & Baltes，ESEC/FSE 2022。把文献综述分为七类，并建议 SE 领域多做元分析、案例调查、元综合，少做范围综述和快速综述。🆓 `ralph2022paving`

### 复现研究

- [Understanding replication of experiments in software engineering: A classification](https://doi.org/10.1016/j.infsof.2014.04.004) - Gómez、Juristo、Vegas，IST 2014。复现研究的分类。💰 `gomez2014understanding`
- [The role of replications in Empirical Software Engineering](https://doi.org/10.1007/s10664-008-9060-1) - Shull 等人，EMSE 2008。复现研究在实证软件工程中的作用。💰 `shull2008role`
- [Towards Reporting Guidelines for Experimental Replications: A Proposal](https://carver.cs.ua.edu/ReplicationGuidelines.htm) - Carver，RESER 2010。复现研究的报告规范。🆓 `carver2010towards`
- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current) - ACM，v1.1，2020。复现材料评审与徽章政策，区分"可用""已评估""结果已复现/已重现"等级别。也可用来筛选适合作为复现任务的论文。🆓 `acm2020artifact`

### 数据挖掘研究

- [The promises and perils of mining git](https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf) - Bird 等人，MSR 2009。挖掘 git 历史数据时的陷阱。🆓 `bird2009promises`
- [The promises and perils of mining GitHub](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf) - Kalliamvakou 等人，MSR 2014。挖掘 GitHub 数据时的常见陷阱。🆓 `kalliamvakou2014promises`
- [An in-depth study of the promises and perils of mining GitHub](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf) - Kalliamvakou 等人，EMSE 2016。上一篇的扩展期刊版。🆓 `kalliamvakou2016indepth`
- [It's not a bug, it's a feature: how misclassification impacts bug prediction](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf) - Herzig、Just、Zeller，ICSE 2013。issue 数据中的分类错误及其对研究结论的影响。🆓 `herzig2013bug`

### 工具与模型评测

- [Evaluating Fuzz Testing](https://arxiv.org/abs/1808.09700) - Klees 等人，CCS 2018。调研 32 篇模糊测试论文的评估方法，指出常见问题并给出建议。🆓 `klees2018evaluating`
- [SoK: Benchmarking Flaws in Systems Security](https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf) - van der Kouwe 等人，EuroS&P 2019。总结系统安全论文中 22 种 benchmark 误用，基于 50 篇论文。🆓 `vanderkouwe2019sok`
- [Dos and Don'ts of Machine Learning in Computer Security](https://arxiv.org/abs/2010.09470) - Arp 等人，USENIX Security 2022。基于 30 篇安全顶会论文，总结机器学习安全研究中设计、实现和评估的常见陷阱。🆓 `arp2022dos`
- [A practical guide for using statistical tests to assess randomized algorithms in software engineering](https://doi.org/10.1145/1985793.1985795) - Arcuri & Briand，ICSE 2011。如何用统计检验比较带随机性的算法或工具。`arcuri2011practical`
- [A Hitchhiker's guide to statistical tests for assessing randomized algorithms in software engineering](https://doi.org/10.1002/stvr.1486) - Arcuri & Briand，STVR 2014。上一篇的扩展期刊版。💰 `arcuri2014hitchhiker`

### 实证研究通用

- [Experimentation in Software Engineering](https://doi.org/10.1007/978-3-662-69306-3) - Wohlin 等人，Springer，第 2 版 2024。实验研究的标准教材，威胁效度的经典论述出自这里。💰 `wohlin2024experimentation`
- [Guidelines for conducting and reporting case study research in software engineering](https://doi.org/10.1007/s10664-008-9102-8) - Runeson & Höst，EMSE 2009。案例研究指南，其中的效度讨论有参考价值。`runeson2009guidelines`
- [Contemporary Empirical Methods in Software Engineering](https://doi.org/10.1007/978-3-030-32489-6) - Felderer & Travassos（编），Springer 2020。多种实证方法的较新综述，仅第 17 章（Open Science）开放获取。💰 `felderer2020contemporary`

## 数据集与工具

- [dspinellis/awesome-msr](https://github.com/dspinellis/awesome-msr) - 实证软件工程研究可用的数据集和工具合集，以 MSR 会议命名。数据挖掘研究和工具评测找数据的首选入口。CC0。📦
- [fudanselab/awesome-software-engineering-research](https://github.com/fudanselab/awesome-software-engineering-research) - 带代码实现的 SE 论文、数据集和工具，可作为复现研究的候选。2022 年后未更新。CC0。📦

## 论文列表

### LLM 与软件工程

- [iSEngLab/AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) - 综述 *A Survey on Large Language Models for Software Engineering*（Science China Information Sciences 2026）配套的论文列表。这类综述本身就是一份 SLR，它的论文列表可以作为 SLR 复现任务的参照答案。📦 `zhang2026survey`
- [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) - 综述 *Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code*（TMLR 2024）配套的代码大模型论文列表，持续更新。📦 `zhang2024unifying`

### 安全与模糊测试

- [wcventure/FuzzingPaper](https://github.com/wcventure/FuzzingPaper) - 按会议整理的模糊测试论文列表，持续更新，附关键词检索脚本。MIT。📦
- [secfigo/Awesome-Fuzzing](https://github.com/secfigo/Awesome-Fuzzing) - 模糊测试的学习资源和工具合集。2023 年后未更新。CC0。📦

## 可复现研究

- [leipzig/awesome-reproducible-research](https://github.com/leipzig/awesome-reproducible-research) - 可复现研究的案例、复现尝试、理论文章、工具和最低标准合集。📦

## 如何做好科研

### 经典文章

- [You and Your Research](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html) - Richard Hamming，1986 年演讲。如何选择重要的问题。P3。🆓 `hamming1986you`
- [Ten Simple Rules for Doing Your Best Research, According to Hamming](https://doi.org/10.1371/journal.pcbi.0030213) - Erren 等人，PLoS Computational Biology 2007。对上面演讲的归纳。🆓 `erren2007ten`
- [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html) - John Schulman，2020。如何选题、如何推进 ML 研究。P2–P3。🆓 `schulman2020opinionated`
- [Tips for Empirical Alignment Research](https://www.alignmentforum.org/posts/dZFpEdKyb9Bf4xYn7/tips-for-empirical-alignment-research) - Ethan Perez，2024。实证研究的具体做法，例如快速迭代实验。P1–P2。🆓 `perez2024tips`
- [How to Write a Great Research Paper](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) - Simon Peyton Jones。论文写作，附幻灯片和视频。🆓 `peytonjones2013write`
- [How to Read a Paper](https://doi.org/10.1145/1273445.1273458) - S. Keshav，ACM SIGCOMM CCR 2007。三遍阅读法。`keshav2007read`
- [A Survival Guide to a PhD](http://karpathy.github.io/2016/09/07/phd/) - Andrej Karpathy，2016。选题、研究习惯等。🆓 `karpathy2016survival`

### 资源合集

- [jbhuang0604/awesome-tips](https://github.com/jbhuang0604/awesome-tips) - Jia-Bin Huang 整理的研究、写作、审稿、报告建议。MIT。📦
- [pliang279/awesome-phd-advice](https://github.com/pliang279/awesome-phd-advice) - Paul Liang（CMU）整理的博士生建议链接合集。2023 年后未更新。MIT。📦
- [shaily99/advice](https://github.com/shaily99/advice) - Shaily Bhatt 整理的研究和申请建议链接合集。2023 年后未更新。MIT。📦

## Agent 科研 skills（仅供参考）

> 这些仓库大多没有公开的评估证据，无法说明加入后研究质量是否提高，领域也大多与 P1 不匹配。**不要在没有证据的情况下直接搬进系统**。合理的用法是参考它们组织知识的方式，或在 S2 中作为外部 baseline 的一部分。

- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) - 98 个 skills，以 ML 工程为主（微调、分布式训练、推理部署等），大部分对应 P4。MIT。📦
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) - 原名 claude-scientific-skills。177 个 skills，面向生物信息、化学信息、临床、材料等领域。MIT。📦
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) - Claude Code 插件，包含深度调研、论文写作、审稿和一个 10 阶段的流程，带人工检查点。**CC BY-NC 4.0，禁止商用。**📦
- [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) - 面向实证研究的 agent skills（AERS），偏经济学和统计方法。CC BY-SA 4.0。📦
- [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) - 科研类 agent skills 的索引。MIT。📦

## AI Scientist 相关系统

属于相关工作，不是科研方法知识。

- [ResearAI/Awesome-AI-Scientist](https://github.com/ResearAI/Awesome-AI-Scientist) - 按知识、选题、实验、写作、审稿组织的 AI 科研论文和工具列表。2025-11 后未更新；许可信息不一致（LICENSE 文件为 Apache-2.0，README 写的是 MIT）。📦
- [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) - 原 ai-boost/awesome-ai-for-science。AI for Science 的工具、论文、数据集合集。MIT。📦
- [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) - 按 8 个研究阶段整理的自动化科研论文列表。MIT。📦

## 本仓库的整理笔记

按统一模板（[`templates/research-type.md`](templates/research-type.md)）整理各类研究的阶段、决策点、质量标准和反面模式。

| 研究类型 | 状态 |
|---|---|
| [系统性文献综述与映射研究](research-types/slr.md) | 初版，待审阅 |
| 复现研究 | 未开始（核心文献待获取） |
| 数据挖掘研究 | 未开始 |
| 工具与模型评测 | 未开始 |

## 待获取

需要付费或无法直接访问、但有价值的资料，见 [`papers/README.md`](papers/README.md#待获取)。

## 贡献

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。
