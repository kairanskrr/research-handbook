# 原始资料

写作[整理内容](../guide/README.md)时依据的资料：论文、规范、博客、讲义、GitHub 仓库等，按 awesome 列表的形式登记，每条附一句话说明。

整理内容引用资料时，指向 [`notes/`](notes/README.md) 里的证据摘录：记录资料原文在哪里说了什么，方便核对。

| 内容 | 位置 |
|---|---|
| 资料列表 | 本页 |
| 证据摘录 | [`notes/`](notes/README.md) |
| 所有资料的引用信息（BibTeX） | [`../papers/references.bib`](../papers/references.bib) |
| 论文索引与获取情况 | [`../papers/README.md`](../papers/README.md) |
| 下载有免费全文的论文 PDF | 在仓库根目录运行 `bash scripts/fetch_papers.sh`，PDF 保存在 `papers/pdf/` |
| GitHub 仓库的上游地址与固定版本 | [`../repos/README.md`](../repos/README.md) |

**图例**：🆓 有免费全文 · 💰 需要付费 · 📦 GitHub 仓库（已作为 submodule 引入 `repos/`）· `key` 为 `references.bib` 中的条目。

## 目录

- [质量标准与报告规范](#质量标准与报告规范)
- [研究方法指南](#研究方法指南)
  - [系统性文献综述与映射研究](#系统性文献综述与映射研究)
  - [复现研究](#复现研究)
  - [数据挖掘研究](#数据挖掘研究)
  - [工具与模型评测](#工具与模型评测)
  - [实证研究通用](#实证研究通用)
  - [计算机各研究类型的方法资料](#计算机各研究类型的方法资料)
  - [其他学科领域概况的资料](#其他学科领域概况的资料)
- [数据集与工具](#数据集与工具)
- [论文列表](#论文列表)
  - [LLM 与软件工程](#llm-与软件工程)
  - [安全与模糊测试](#安全与模糊测试)
- [可复现研究](#可复现研究)
- [如何做好科研](#如何做好科研)
  - [综合与经典](#综合与经典)
  - [选题与研究品味](#选题与研究品味)
  - [研究流程与习惯](#研究流程与习惯)
  - [读论文](#读论文)
  - [写作](#写作)
  - [审稿与作者回复](#审稿与作者回复)
  - [学术报告](#学术报告)
  - [读博、导师与职业](#读博导师与职业)
  - [建议合集](#建议合集)
- [科研 skills（待评估）](#科研-skills待评估)
  - [软件工程实证研究](#软件工程实证研究)
  - [科研流程与写作](#科研流程与写作)
  - [合集与规范](#合集与规范)
- [AI Scientist 相关系统](#ai-scientist-相关系统)
- [待获取](#待获取)

## 质量标准与报告规范

各类研究公认的质量标准和报告规范。

- [ACM SIGSOFT Empirical Standards](https://www2.sigsoft.org/EmpiricalStandards/) - Ralph 等人，2020 起持续更新。为 19 种研究方法分别列出必要、加分、优秀三档要求，以及反面模式、可接受的偏离、不成立的批评和范例论文。其中 General Standard 适用于所有研究类型。采用 CC0 许可。📦 🆓 `ralph2020empirical`
- [Guidelines for Empirical Studies in Software Engineering involving Large Language Models](https://llm-guidelines.org/) - Baltes 等人，Empirical Software Engineering 2026。8 条指南：声明 LLM 的使用、报告模型版本和配置、公开提示词和交互日志、用人工验证 LLM 输出、用开源模型作 baseline 等。🆓 `baltes2026guidelines`
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
- [ACM Computing Surveys: Author Guidelines](https://dl.acm.org/journal/csur/author-guidelines) - ACM，计算机领域最主要的综述期刊对投稿的要求：综述论文应对已有文献分类、形成对领域的视角、评估趋势；并区分综述与教程。🆓 `acm2026csurguidelines`

### 复现研究

- [Understanding replication of experiments in software engineering: A classification](https://doi.org/10.1016/j.infsof.2014.04.004) - Gómez、Juristo、Vegas，IST 2014。复现研究的分类。💰 `gomez2014understanding`
- [The role of replications in Empirical Software Engineering](https://doi.org/10.1007/s10664-008-9060-1) - Shull 等人，EMSE 2008。复现研究在实证软件工程中的作用。💰 `shull2008role`
- [Towards Reporting Guidelines for Experimental Replications: A Proposal](https://carver.cs.ua.edu/ReplicationGuidelines.htm) - Carver，RESER 2010。复现研究的报告规范。🆓 `carver2010towards`
- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current) - ACM，v1.1，2020。复现材料评审与徽章政策，区分"可用""已评估""结果已复现/已重现"等级别。🆓 `acm2020artifact`

### 数据挖掘研究

- [The promises and perils of mining git](https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf) - Bird 等人，MSR 2009。挖掘 git 历史数据时的陷阱。🆓 `bird2009promises`
- [Fair and Balanced? Bias in Bug-Fix Datasets](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009fbb.pdf) - Bird 等人，ESEC/FSE 2009。缺陷数据集中"能链接到提交的缺陷修复"只是有系统性偏差的子集，这种偏差会影响假设检验和缺陷预测的结论。🆓 `bird2009fair`
- [The promises and perils of mining GitHub](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf) - Kalliamvakou 等人，MSR 2014。挖掘 GitHub 数据时的常见陷阱。🆓 `kalliamvakou2014promises`
- [An in-depth study of the promises and perils of mining GitHub](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf) - Kalliamvakou 等人，EMSE 2016。上一篇的扩展期刊版。🆓 `kalliamvakou2016indepth`
- [It's not a bug, it's a feature: how misclassification impacts bug prediction](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf) - Herzig、Just、Zeller，ICSE 2013。issue 数据中的分类错误及其对研究结论的影响。🆓 `herzig2013bug`

### 工具与模型评测

- [Evaluating Fuzz Testing](https://arxiv.org/abs/1808.09700) - Klees 等人，CCS 2018。调研 32 篇模糊测试论文的评估方法，指出常见问题并给出建议。🆓 `klees2018evaluating`
- [SoK: Benchmarking Flaws in Systems Security](https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf) - van der Kouwe 等人，EuroS&P 2019。总结系统安全论文中 22 种 benchmark 误用，基于 50 篇论文。🆓 `vanderkouwe2019sok`
- [Dos and Don'ts of Machine Learning in Computer Security](https://arxiv.org/abs/2010.09470) - Arp 等人，USENIX Security 2022。基于 30 篇安全顶会论文，总结机器学习安全研究中设计、实现和评估的常见陷阱。🆓 `arp2022dos`
- [A practical guide for using statistical tests to assess randomized algorithms in software engineering](https://doi.org/10.1145/1985793.1985795) - Arcuri & Briand，ICSE 2011。如何用统计检验比较带随机性的算法或工具。`arcuri2011practical`
- [A Hitchhiker's guide to statistical tests for assessing randomized algorithms in software engineering](https://doi.org/10.1002/stvr.1486) - Arcuri & Briand，STVR 2014。上一篇的扩展期刊版。[作者版本](https://orbilu.uni.lu/bitstream/10993/1071/1/paper_stvr_icse_2012.pdf)。🆓 `arcuri2014hitchhiker`
- [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/) - Blackburn、Berger、Hauswirth、Hicks 等，ACM SIGPLAN 2018。七类检查项：明确声明、基准选择、数据分析、工作负载、统计严谨、威胁缓解、可复现。适合当作工具评测的检查清单。🆓 `blackburn2018sigplan`
- [Gernot's List of Systems Benchmarking Crimes](https://gernot-heiser.org/benchmarking-crimes.html) - Gernot Heiser（UNSW），持续更新。系统论文中常见的基准测试"罪行"：选择性使用基准、不当比较、关键信息缺失等。🆓 `heiserbenchmarking`
- [The Devil's Guide to Incremental Research](https://andreas-zeller.info/2021/04/15/the-devils-guide-to-incremental-research.html) - Andreas Zeller，2021。以反讽方式列出 12 种"注水"研究的套路（例如挑选有利的结果），供作者和审稿人识别。🆓 `zeller2021devil`
- ["Bad smells" in software analytics papers](https://arxiv.org/abs/1803.05518) - Menzies & Shepperd，IST 2019。软件分析类论文的"坏味道"清单，供作者和审稿人自查。🆓 `menzies2019bad`
- [How to avoid machine learning pitfalls: a guide for academic researchers](https://arxiv.org/abs/2108.02497) - Michael Lones，arXiv 2021（持续更新）。从建模、评估、比较到报告，列出学术 ML 研究的常见陷阱及避免方法。🆓 `lones2021avoid`
- [On Evaluating Adversarial Robustness](https://arxiv.org/abs/1902.06705) - Carlini 等人，arXiv 2019。对抗鲁棒性防御的评估方法与检查清单。🆓 `carlini2019evaluating`
- [Successful language model evals](https://jasonwei.net/blog/evals) - Jason Wei，2024。好的 LLM 评测基准有哪些特征：样本足够多、分数含义清楚易懂、有大论文使用等。🆓 `wei2024evals`
- [NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark](https://arxiv.org/abs/2310.18018) - Sainz 等人，Findings of EMNLP 2023。大语言模型评测中的数据污染：测试数据混进了训练数据，会高估模型表现；提出按每个评测集测量污染的办法。🆓 `sainz2023nlp`
- [Producing wrong data without doing anything obviously wrong!](https://doi.org/10.1145/1508244.1508275) - Mytkowicz 等人，ASPLOS 2009。链接顺序、环境变量大小等看似无关的因素会产生测量偏差，足以推翻实验结论。`mytkowicz2009producing`
- [Statistically rigorous Java performance evaluation](https://doi.org/10.1145/1297027.1297033) - Georges 等人，OOPSLA 2007。性能测量中应使用置信区间等统计方法，而不是只报告单次或最好的结果。[合作者主页](https://dri.es/files/oopsla07-georges.pdf)。🆓 `georges2007statistically`
- [Rigorous benchmarking in reasonable time](https://doi.org/10.1145/2464157.2464160) - Kalibera & Jones，ISMM 2013。在有限时间内设计多层次的重复实验，以获得可靠的性能结果。[肯特大学机构库（作者接受稿）](https://kar.kent.ac.uk/33611/)。🆓 `kalibera2013rigorous`
- [Wake up and smell the coffee: evaluation methodology for the 21st century](https://doi.org/10.1145/1378704.1378723) - Blackburn 等人，CACM 2008。指出性能评估方法上的缺陷并给出改进建议。`blackburn2008wake`
- [Scientific benchmarking of parallel computing systems](https://doi.org/10.1145/2807591.2807644) - Hoefler & Belli，SC 2015。并行计算性能报告的 12 条规则。[作者主页](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf)。🆓 `hoefler2015scientific`


### 实证研究通用

- [Experimentation in Software Engineering](https://doi.org/10.1007/978-3-662-69306-3) - Wohlin 等人，Springer，第 2 版 2024。实验研究的标准教材，威胁效度的经典论述出自这里。💰 `wohlin2024experimentation`
- [Guidelines for conducting and reporting case study research in software engineering](https://doi.org/10.1007/s10664-008-9102-8) - Runeson & Höst，EMSE 2009。案例研究指南，其中的效度讨论有参考价值。开放获取（CC BY-NC）。🆓 `runeson2009guidelines`
- [Contemporary Empirical Methods in Software Engineering](https://doi.org/10.1007/978-3-030-32489-6) - Felderer & Travassos（编），Springer 2020。多种实证方法的较新综述，仅第 17 章（Open Science）开放获取。💰 `felderer2020contemporary`
- [Sampling in software engineering research: a critical review and guidelines](https://arxiv.org/abs/2002.07764) - Baltes & Ralph，EMSE 2022。SE 研究中抽样方法的批判性综述和指南。🆓 `baltes2022sampling`
- [Views on Internal and External Validity in Empirical Software Engineering](https://doi.org/10.1109/ICSE.2015.24) - Siegmund、Siegmund、Apel，ICSE 2015。调查 SE 社区如何看待内部效度与外部效度的取舍。`siegmund2015views`
- [SoK: Science, Security and the Elusive Goal of Security as a Scientific Pursuit](https://doi.org/10.1109/SP.2017.38) - Herley & van Oorschot，IEEE S&P 2017。借科学哲学审视安全研究的科学性，批评不可证伪的主张。`herley2017sok`
- [The Menlo Report](https://www.caida.org/publications/papers/2012/menlo_report/menlo_report.pdf) - Bailey、Dittrich、Kenneally、Maughan，IEEE Security & Privacy 2012。介绍美国国土安全部资助的 Menlo 报告：在 Belmont 报告三原则之上增加"尊重法律与公共利益"，是安全和网络研究伦理的常用依据。报告原文见 [SSRN](https://doi.org/10.2139/ssrn.2445102)。🆓 `bailey2012menlo`
- [The European Code of Conduct for Research Integrity（2023 修订版）](https://doi.org/10.26356/ECOC) - ALLEA（欧洲科学与人文学院联合会），2023。适用于所有学科的科研诚信准则：四条基本原则、良好研究规范、学术不端的定义。CC BY 4.0。🆓 `allea2023european`
- [Ethical considerations in network measurement papers](https://doi.org/10.1145/2896816) - Partridge & Allman，CACM 2016。测量类论文应如何讨论和处理伦理问题。`partridge2016ethical`


### 计算机各研究类型的方法资料

计算机领域篇各研究类型文档引用的方法论资料（2026-10 新增）。

- [Ten Signs a Claimed Mathematical Breakthrough is Wrong](https://scottaaronson.blog/?p=304) - Aaronson，Shtetl-Optimized (blog) 2008。理论计算机科学家 Scott Aaronson 的博客文章，列出判断"重大数学突破"声明多半有错的十个信号，作者强调只是启发式。🆓 `aaronson2008ten`
- [Output Data Analysis for Simulations](https://www.informs-sim.org/wsc02papers/012.pdf) - Alexopoulos 等人，Proceedings of the 2002 Winter Simulation Conference 2002。仿真输出数据统计分析的教程：终止型与稳态仿真的区别、独立重复运行、初始化偏差与预热期截断（含 Welch 作图法）、重复/删除法等。🆓 `alexopoulos2002output`
- [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) - Braun 等人，Qualitative Research in Psychology 2006。主题分析的经典指南：主题分析是什么、归纳与演绎、六个分析阶段、常见陷阱和 15 条检查清单。🆓 `braun2006using`
- [Simulation Based Studies in Software Engineering: A Matter of Validity](https://www.clei.org/cleiej/index.php/cleiej/article/view/54) - de França 等人，CLEI Electronic Journal 2015。de França & Travassos 从软件工程仿真研究中整理出 28 种效度威胁，把它们和验证/确认方法对应起来，给出 7 条规划仿真研究的建议。🆓 `defranca2015simulation`
- [Selecting Empirical Methods for Software Engineering Research](https://doi.org/10.1007/978-1-84800-044-5_11) - Easterbrook 等人，Guide to Advanced Empirical Software Engineering 2008。软件工程实证方法选择的经典导论，讲研究问题类型、哲学立场、各种方法（实验、案例研究、调查、民族志、行动研究）的适用场合，§5.6 介绍三种混合方法设计。🆓 `easterbrook2008selecting`
- [Empirical Software Engineering Experts on the Use of Students and Professionals in Experiments](https://bura.brunel.ac.uk/handle/2438/14575) - Falessi 等人，Empirical Software Engineering 2018。Falessi 等七位实证软件工程研究者基于 ISERN 2014 焦点小组和后续专家调查，讨论实验中用学生还是专业人员作参与者，提出 16 条陈述和"真实、相关、近期经验"（R3）刻画方案。🆓 `falessi2018empirical`
- [Psychometrics in Behavioral Software Engineering: A Methodological Introduction with Guidelines](https://arxiv.org/abs/2005.09959) - Graziotin 等人，ACM Transactions on Software Engineering and Methodology 2021。Graziotin、Lenberg、Feldt、Wagner 为软件工程研究者介绍心理测量学：怎样开发和评估测量心理构念的量表（题目分析、因子分析、信度、效度、公平性），附 R 示例。🆓 `graziotin2021psychometrics`
- [State of the Art: Reproducibility in Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/11503) - Gundersen 等人，Proceedings of the Thirty-Second AAAI Conference on Artifici 2018。调查 IJCAI 和 AAAI 的 400 篇论文为可复现记录了多少必要信息；提出可复现的三个程度（R1 同实现同数据、R2 换实现同数据、R3 换实现换数据）。🆓 `gundersen2018state`
- [Systematic methodological review: developing a framework for a qualitative semi-structured interview guide](https://doi.org/10.1111/jan.13031) - Kallio 等人，Journal of Advanced Nursing 2016。对半结构化访谈提纲设计方法的系统综述，归纳出五个阶段：确认前提、利用已有知识、拟定初稿、预试、呈现完整提纲；对主要话题、追问和三种预试方式讲得具体。🆓 `kallio2016systematic`
- [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) - Kapoor 等人，Patterns 2023。调查 17 个领域中由数据泄漏造成的可复现性问题（涉及 294 篇论文），提出 8 类泄漏的分类和"模型信息表"，并复现内战预测研究，发现改正泄漏后复杂模型并不优于逻辑回归。🆓 `kapoor2023leakage`
- [Quantitative Longitudinal Research: A Review of IS Literature, and a Set of Methodological Guidelines](https://aisel.aisnet.org/ecis2015_cr/94) - Kehr 等人，Proceedings of the 23rd European Conference on Information S 2015。回顾信息系统领域的定量纵向研究，提出四条规划原则：按现象的自然节律安排测量、选对测量轮数、注意内部效度威胁（含流失）、选用适合相依数据的分析方法。🆓 `kehr2015quantitative`
- [A Practical Guide to Controlled Experiments of Software Engineering Tools with Human Participants](https://faculty.washington.edu/ajko/papers/Ko2013SEToolEvaluations.pdf) - Ko 等人，Empirical Software Engineering 2015。Ko、LaToza、Burnett 在 Empirical Software Engineering 上的方法论文，结合对 2001～2011 年 345 项有人参与的工具评估的系统综述，逐项讲解招募、知情同意、分组、培训、任务设计、结果测量、结束说明和预实验的可选做法及其利弊。🆓 `ko2015practical`
- [How to Write a Proof](https://lamport.azurewebsites.net/pubs/lamport-how-to-write.pdf) - Lamport，The American Mathematical Monthly 1995。Lamport 最早提出结构化证明的文章，讲写法、展开层次和作者发现教材证明错误的经历。🆓 `lamport1995how`
- [How to Write a 21st Century Proof](https://lamport.azurewebsites.net/pubs/proof.pdf) - Lamport，Journal of Fixed Point Theory and Applications 2012。Leslie Lamport 讲结构化（分层编号）证明写法的文章，含二十年使用经验和一个用 TLAPS 机器检查的证明示例。🆓 `lamport2012how`
- [Reliability and Inter-rater Reliability in Qualitative Research: Norms and Guidelines for CSCW and HCI Practice](https://doi.org/10.1145/3359174) - McDonald 等人，Proceedings of the ACM on Human-Computer Interaction 2019。分析 2016–2018 年 CSCW 和 CHI 的定性论文怎样报告可靠性，并给出何时该、何时不该计算编码者间信度的建议。🆓 `mcdonald2019reliability`
- [Case Survey Studies in Software Engineering Research](https://doi.org/10.1145/3382494.3410683) - Melegati 等人，Proceedings of the 14th ACM / IEEE International Symposium o 2020。梳理案例调查方法的经典定义和步骤（Lucas、Yin、Larsson 等），并用映射研究分析 12 篇自称用了案例调查的软件工程论文，发现大多没有按经典定义来做。🆓 `melegati2020case`
- [An Empirically Evaluated Checklist for Surveys in Software Engineering](https://arxiv.org/abs/1901.09850) - Molléri 等人，Information and Software Technology 2020。Molléri、Petersen、Mendes 汇总 14 篇软件工程问卷方法论文献，得到一份问卷研究检查清单，并用它评估了 24 篇问卷论文、请原作者反馈。🆓 `molleri2020empirically`
- [Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)](https://jmlr.org/papers/v22/20-303.html) - Pineau 等人，Journal of Machine Learning Research 2021。NeurIPS 2019 可复现性计划的报告：代码提交政策、社区复现挑战赛、机器学习可复现性检查清单；给出机器学习中复现困难的原因和几种术语的区分。🆓 `pineau2021improving`
- [Action Research Can Swing the Balance in Experimental Software Engineering](https://arxiv.org/abs/1306.2414) - dos Santos 等人，Advances in Computers 2011。*Advances in Computers* 第 83 卷中的一章。🆓 `santos2011action`
- [Verification and Validation of Simulation Models](https://www.informs-sim.org/wsc10papers/016.pdf) - Sargent，Proceedings of the 2010 Winter Simulation Conference 2010。Sargent 关于仿真模型验证与确认的经典教程（WSC 2010 版），给出验证、确认的定义，四类检查（概念模型确认、计算机模型验证、运行确认、数据有效性），常用检验技术，以及一套推荐的最低确认步骤。🆓 `sargent2010verification`
- [The Role of Ethnographic Studies in Empirical Software Engineering](https://doi.org/10.1109/TSE.2016.2519887) - Sharp 等人，IEEE Transactions on Software Engineering 2016。面向软件工程研究者介绍民族志：四个主要特征、研究设计的五个维度、在实证软件工程中的四种作用，附八个软件工程民族志例子。🆓 `sharp2016role`
- [Inferencing into the Void: Problems with Implicit Populations. Comments on ``Empirical Software Engineering Experts on the Use of Students and Professionals in Experiments''](https://arxiv.org/abs/1810.07392) - Shepperd，2018。Shepperd 对 Falessi 等人 2018 的评论（后收入 Feldt 等人 2018 在 Empirical Software Engineering 上发表的"四篇评论"），强调要明确定义目标总体，并同时考虑参与者、任务和环境的代表性；目标是专业人员时应尽量用专业人员。🆓 `shepperd2018inferencing`
- [Guidelines for Conducting Action Research Studies in Software Engineering](https://www.e-informatyka.pl/EISEJ/papers/2025/1/5/) - Staron，e-Informatica Software Engineering Journal 2025。Staron（Springer 2020 专著 *Action Research in Software Engineering* 的作者）在 e-Informatica 期刊发表的行动研究指南，整理了 Davison、Baskerville 等已有指南，提出 20 条覆盖项目准备、干预、报告和伦理的建议。🆓 `staron2025guidelines`
- [Grounded Theory in Software Engineering Research: A Critical Review and Guidelines](https://hdl.handle.net/10344/5396) - Stol 等人，Proceedings of the 38th International Conference on Software 2016。ICSE 2016 论文。🆓 `stol2016grounded`
- [The who, what, how of software engineering research: a socio-technical framework](https://doi.org/10.1007/s10664-020-09858-z) - Storey 等人，Empirical Software Engineering 2020。提出"谁受益、贡献是什么、怎样研究"的社会—技术研究框架，用它分析 ICSE 和 EMSE 2017 年的 151 篇论文，发现大多数声称惠及人的研究并未直接研究人，以数据为主的论文很少与其他研究策略做三角验证。🆓 `storey2020who`
- [Career Advice](https://terrytao.wordpress.com/career-advice/) - Tao，Whats new (blog) 。Terence Tao（陶哲轩）博客上的职业建议系列短文。🆓 `taocareer`
- [On Writing](https://terrytao.wordpress.com/advice-on-writing-papers/) - Tao，Whats new (blog) 。Tao 博客上的写论文建议系列短文。🆓 `taowriting`
- [Lessons Learnt in Conducting Survey Research](https://arxiv.org/abs/1702.05744) - Torchiano 等人，Proceedings of the 5th IEEE/ACM International Workshop on Co 2017。Torchiano、Méndez Fernández、Travassos、de Mello 总结在业界做问卷调查的经验教训，覆盖定研究目标、定总体和分析单元、抽样框、题目措辞和选项设计、招募与提醒，附大量正反例句。🆓 `torchiano2017lessons`
- [Challenges in Survey Research](https://arxiv.org/abs/1908.05899) - Wagner 等人，Contemporary Empirical Methods in Software Engineering 2020。Wagner、Mendez、Felderer、Graziotin、Kalinowski 基于多轮跨国问卷（NaPiRE 等）的经验，讨论问卷调查与理论、抽样与样本量、邀请与跟进、定序数据的统计分析、开放题编码和心理测量量表的使用。🆓 `wagner2020challenges`
- [Case Study Research in Software Engineering---It is a Case, and it is a Study, but is it a Case Study?](https://doi.org/10.1016/j.infsof.2021.106514) - Wohlin，Information and Software Technology 2021。检查 7 个软件工程期刊上最近 100 篇自称"案例研究"的论文，发现接近一半不符合案例研究的定义，并提出一个更严格的定义。🆓 `wohlin2021case`

### 其他学科领域概况的资料

各学科领域概况（`guide/fields/<学科>/README.md`）引用的资料（2026-10 新增），按学科分组。

**数学**

- [The Culture of Research and Scholarship in Mathematics: Joint Research and Its Publication](https://www.ams.org/profession/leaders/CultureStatement04.pdf) - American Mathematical Society Committee on the Profession，AMS statement 2004。美国数学会职业委员会 2004 年声明，解释数学的合作研究文化和按字母署名的传统，含署名统计。🆓 `amsculture2004joint`
- [The Culture of Research and Scholarship in Mathematics: Rates of Publication](https://www.ams.org/profession/leaders/culture/CultureStatement06.pdf) - American Mathematical Society Committee on the Profession，AMS statement 2006。美国数学会职业委员会 2006 年声明，说明数学家发表少、以期刊为主、发表延迟常见，评价应看质量。🆓 `amsculture2006rates`
- [Policy Statement on Ethical Guidelines](https://www.ams.org/about-us/governance/policy-statements/sec-ethics) - American Mathematical Society，AMS 政策声明 2022。美国数学会伦理准则（2005 年通过，2019、2022 年修订），涵盖抄袭、署名、宣布结果、审稿保密与利益冲突、编辑责任、博士培养。🆓 `ams2022ethical`
- [On Proof and Progress in Mathematics](https://arxiv.org/abs/math/9404236) - Thurston，Bulletin of the American Mathematical Society 1994。Thurston 回应 Jaffe & Quinn 的名文，讨论数学家怎样理解、交流和检查证明，以及数学研究的社会性。arXiv 开放全文。🆓 `thurston1994proof`
- [Setting the Default to Reproducible: Reproducibility in Computational and Experimental Mathematics](https://icerm.brown.edu/topical_workshops/tw12-5-rcem/icerm_report.pdf) - Stodden 等人，Institute for Computational and Experimental Research in Mathematics (ICERM) 2013。ICERM 2012 年"计算与实验数学的可复现性"研讨会报告，给出计算数学研究公开代码数据、验证计算的建议。🆓 `stodden2013setting`
- [The arXiv Endorsement System](https://info.arxiv.org/help/endorsement.html) - arXiv，arXiv help page。arXiv 帮助页面，说明首次投稿的背书（endorsement）制度和找背书人的做法。🆓 `arxivendorsement`
- [Content Moderation](https://info.arxiv.org/help/moderation/index.html) - arXiv，arXiv help page。arXiv 帮助页面，说明审核不是同行评审、分类调整和可能拒稿的情形。🆓 `arxivmoderation`

**物理科学**

- [APS Ethics Standards](https://www.aps.org/about/governance/policies-procedures/ethics-standards) - American Physical Society，网页 2024。美国物理学会的伦理标准，2024 年 12 月修订、2025 年 1 月生效，涵盖研究结果、署名、重复发表与预印本、抄袭、同行评审等。🆓 `aps2024ethics`
- [Guidelines for Data Availability Statements in Physical Review](https://journals.aps.org/authors/data-availability-statements) - American Physical Society，网页 2024。Physical Review 系列期刊的数据可获取性声明指南：所有论文必须有声明，鼓励按 FAIR 原则公开数据和代码。🆓 `apsdataavailability`
- [Policy Statement on Software](https://journals.aas.org/policy-statement-on-software/) - AAS Journals，网页。美国天文学会期刊的软件政策：软件论文、开源与存档建议、软件引用的两种方式。🆓 `aassoftware`
- [About arXiv](https://info.arxiv.org/about/index.html) - arXiv，网页。arXiv 官方介绍：创办时间、审核方式（不做同行评审）。🆓 `arxivabout`
- [Category Taxonomy](https://arxiv.org/category_taxonomy) - arXiv，网页。arXiv 学科分类表，含高能物理实验、理论、唯象、格点，计算物理，天体物理仪器与方法等分类的官方说明。🆓 `arxivtaxonomy`
- [It was twenty years ago today ...](https://arxiv.org/abs/1108.2700) - Ginsparg，arXiv:1108.2700 2011。arXiv 创办人 Paul Ginsparg 的 20 周年回顾：arXiv 起源于高能物理理论的预印本交流，以及预印本与期刊在物理中的并存。🆓 `ginsparg2011twenty`
- [Reproducibility and Replication of Experimental Particle Physics Results](https://arxiv.org/abs/2009.06864) - Junk 等人，arXiv:2009.06864 2020。两位实验粒子物理学家全面介绍粒子物理保证结果可靠的做法：大合作的内部审查、5σ 发现标准、盲分析、软件与数据保存、零结果发表。🆓 `junk2021reproducibility`
- [Discovering the Significance of 5 sigma](https://arxiv.org/abs/1310.1284) - Lyons，arXiv:1310.1284 2013。讨论粒子物理 5σ 发现标准的理由和局限，以及别处效应（Look Elsewhere Effect）。🆓 `lyons2013discovering`
- [Blind Analysis in Particle Physics](https://arxiv.org/abs/physics/0312102) - Roodman，arXiv:physics/0312102 2003。PHYSTAT2003 会议论文，介绍实验者偏差和粒子物理中的三种盲分析方法，以及 BABAR 合作组的经验。🆓 `roodman2003blind`
- [Blind analysis in Physics experiments: Is this trip necessary?](https://arxiv.org/abs/2311.13542) - Golub，arXiv:2311.13542 2023。对 Klein & Roodman 2005 盲分析主张的质疑短评（未经同行评审），认为盲分析妨碍寻找系统误差和研究意外事件。🆓 `golub2023blind`
- [LIGO Scientific Collaboration Publication and Presentation Policy](https://dcc.ligo.org/public/0026/T010168/010/T010168-10.pdf) - LIGO Scientific Collaboration，网页 2018。LIGO 科学合作组公开的发表与报告政策：作者资格、内部审查流程、会议报告和学位论文的规定。🆓 `ligo2018publication`
- [CERN Open Data Policy for the LHC Experiments](https://opendata.cern.ch/docs/cern-open-data-policy-for-lhc-experiments) - CERN Open Data Policy Working Group，网页 2020。CERN 对 LHC 各实验数据公开的分级政策：论文开放获取、发表时附数据、重建数据定期公开、原始数据不公开的理由。🆓 `cern2020opendata`

**生物科学**

- [The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000410) - Percie du Sert 等人，PLoS Biology 2020。ARRIVE 2.0 动物实验报告指南的正式发布文章，介绍"核心 10 项"和"推荐项"两组条目。开放获取（CC0）。🆓 `perciedusert2020arrive`
- [Reporting animal research: Explanation and elaboration for the ARRIVE guidelines 2.0](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000411) - Percie du Sert 等人，PLoS Biology 2020。ARRIVE 2.0 的逐条解释与示例（Explanation and Elaboration），讲实验单位、对照、随机、盲法等。开放获取。🆓 `perciedusert2020reporting`
- [Replicates and repeats–-what is the difference and is it significant? A brief discussion of statistics and experimental design](https://pmc.ncbi.nlm.nih.gov/articles/PMC3321166/) - Vaux 等人，EMBO Reports 2012。用骨髓集落实验和 qRT-PCR 两个例子，讲清重复测量（replicates）和独立重复的区别，以及 n 怎么算。PubMed Central 开放全文。🆓 `vaux2012replicates`
- [Ten Simple Rules for a Computational Biologist's Laboratory Notebook](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004385) - Schnell，PLoS Computational Biology 2015。PLoS Computational Biology "Ten Simple Rules" 系列，讲实验记录本怎么记（面向计算生物学家，原则通用）。开放获取（CC BY）。🆓 `schnell2015ten`
- [Author Sequence and Credit for Contributions in Multiauthored Publications](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0050018) - Tscharntke 等人，PLoS Biology 2007。讨论多作者论文的署名顺序与贡献认定，包括生物医学中"最后作者"惯例。开放获取。🆓 `tscharntke2007author`
- [The Economics of Reproducibility in Preclinical Research](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002165) - Freedman 等人，PLoS Biology 2015。估算临床前研究不可复现的比例和经济代价，把原因分为研究设计、生物试剂、操作规程、数据分析与报告四类，并以细胞系鉴定为例。开放获取（CC BY）。🆓 `freedman2015economics`
- [Investigating the replicability of preclinical cancer biology](https://elifesciences.org/articles/71601) - Errington 等人，eLife 2021。癌症生物学可复现性项目（Reproducibility Project: Cancer Biology）的结果汇总：50 个实验、158 个效应的复现情况。开放获取（CC BY）。🆓 `errington2021investigating`
- [Challenges for assessing replicability in preclinical cancer biology](https://elifesciences.org/articles/67995) - Errington 等人，eLife 2021。同一项目的过程报告：方法描述不足、数据和试剂难获取、方案需反复修改、各阶段耗时。开放获取（CC BY）。🆓 `errington2021challenges`
- [Guidance: Rigor and Reproducibility in Grant Applications](https://grants.nih.gov/policy/reproducibility/guidance.htm) - National Institutes of Health，网页。美国国立卫生研究院关于资助申请中严谨性与可复现性的指南：前期研究严谨性、实验设计、生物学变量（含性别）、关键资源鉴定四个方面。🆓 `nihrigorguidance`
- [The 3Rs](https://nc3rs.org.uk/who-we-are/3rs) - National Centre for the Replacement, Refinement and Reduction of Animals in Research，网页。英国 NC3Rs 对 3R 原则（替代、减少、优化）的定义和说明。🆓 `nc3rsthe3rs`
- [About bioRxiv](https://www.biorxiv.org/about-biorxiv) - bioRxiv，网页。bioRxiv 官方说明页：预印本不经同行评审、与期刊投稿的关系、发布后不能撤下、引用方式。🆓 `biorxivabout`
- [Data Availability](https://journals.plos.org/plosone/s/data-availability) - PLOS，网页。PLOS 系列期刊的数据可用性政策：公开重复研究所需数据、按领域选仓库（如 GenBank、GEO）、不允许"数据未展示"、印迹图须提供原始图像。🆓 `plosdatapolicy`

**电气电子与信息工程**

- [IEEE Publication Services and Products Board Operations Manual](https://pspb.ieee.org/images/files/files/opsmanual.pdf) - IEEE Publication Services and Products Board，IEEE 2026。IEEE 出版服务与产品委员会运行手册（2026 年 6 月修订），IEEE 出版规则的原始文件，含署名、作者责任、会议论文转期刊、预印本政策，并全文转载《IEEE 伦理准则》。🆓 `ieee2026pspb`
- [Post-Publication Policies](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/post-publication-policies/) - IEEE，IEEE Author Center Journals 2026。IEEE 期刊作者中心关于预印本、录用稿和正式版公开范围的说明页面。🆓 `ieeeauthorposting`
- [Submission and Peer Review Policies](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/) - IEEE，IEEE Author Center Journals 2026。IEEE 期刊作者中心关于一稿多投、先前发表、抄袭、出口管制等投稿与审稿政策的页面。🆓 `ieeeauthorsubmission`
- [Research Reproducibility](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/) - IEEE，IEEE Author Center Journals 2026。IEEE 期刊作者中心的研究可复现性页面，含 IEEE 开放研究声明和 Code Ocean 代码共享说明。🆓 `ieeeauthorreproducibility`
- [Author Instructions for OJSP Reproducibility Review](https://signalprocessingsociety.org/publications-resources/ieee-open-journal-signal-processing/author-instructions-ojsp-reproducibility) - IEEE Signal Processing Society，IEEE Signal Processing Society 网页 2025。IEEE 信号处理学会《IEEE 信号处理开放期刊》（OJSP）复现性审查试点的作者说明，基于 Code Ocean。🆓 `ojspreproducibility`
- [Reproducible Research in Signal Processing](https://infoscience.epfl.ch/record/136640) - Vandewalle 等人，IEEE Signal Processing Magazine 2009。信号处理领域讨论可复现研究的代表性文章，含对 2004 年《IEEE 图像处理汇刊》134 篇论文的复现性调查和作者自己的经验。EPFL 机构知识库公开全文。🆓 `vandewalle2009reproducible`
- [Terminologies for Reproducible Research](https://arxiv.org/abs/1802.03311) - Barba，arXiv:1802.03311 2018。梳理各学科对 reproduce / replicate 用法的分歧，按学科分组。🆓 `barba2018terminologies`
- [Repeatable and Reproducible Wireless Networking Experimentation through Trace-based Simulation](https://arxiv.org/abs/1903.12033) - Lamela 等人，arXiv:1903.12033 2019。无线网络研究中仿真与实验平台各自的局限，以及用"轨迹回放仿真"让实验可重复的方法。🆓 `lamela2019repeatable`
- [Computing Curricula 2005: The Overview Report](https://www.acm.org/binaries/content/assets/education/curricula-recommendations/cc2005-march06final.pdf) - Shackelford 等人，ACM, AIS, and IEEE Computer Society 2005。ACM、AIS、IEEE 计算机学会联合发布的计算学科课程总报告，讲电气工程、计算机工程、计算机科学等学科的分化历史和区别。🆓 `shackelford2005computing`
- [Inventions and Commercialization FAQs](https://research.rutgers.edu/faculty-staff/inventions-commercialization/faqs) - Rutgers University Office for Research，Rutgers University 网页 2026。罗格斯大学技术转移常见问题，解释什么算"公开披露"、公开对专利的影响、发表与申请专利如何协调。🆓 `rutgersinventionfaq`
- [When to Disclose an Invention to OTL](https://ipira.berkeley.edu/researchers/intellectual-property-protection/when-disclose-invention-otl) - UC Berkeley Intellectual Property and Industry Research Alliances，UC Berkeley IPIRA 网页 2026。加州大学伯克利分校关于何时向技术许可办公室披露发明的说明，含宽限期的提醒。🆓 `berkeleydisclose`
- [Protecting Your Research: A Guide to IP Disclosure and Grant Compliance at the University of Utah](https://technologylicensing.utah.edu/news-events/resources-opportunities/protecting-your-research) - University of Utah Technology Licensing Office，University of Utah 网页 2026。犹他大学技术许可办公室的指南，逐项说明期刊、会议、预印本、答辩是否构成公开，以及临时申请。🆓 `utahprotecting`
- [MPW Prototyping](https://europractice-ic.com/mpw-prototyping/) - Europractice，Europractice 网页 2026。Europractice 芯片原型服务的流程说明（多项目晶圆、设计套件、制造与寄回测试）。🆓 `europracticempw`
- [Develop Standards](https://standards.ieee.org/develop/) - IEEE Standards Association，IEEE SA 网页 2026。IEEE 标准协会关于标准制定流程、原则和下属委员会（含专利委员会）的介绍页面。🆓 `ieeesadevelop`
- [About 3GPP](https://www.3gpp.org/about-us) - 3GPP，3GPP 网页 2026。3GPP 官网的介绍页面，说明其规范范围和发展历史。🆓 `3gpp2026about`

**临床医学**

- [WMA Declaration of Helsinki – Ethical Principles for Medical Research Involving Human Participants](https://www.wma.net/policies-post/wma-declaration-of-helsinki/) - World Medical Association，网页 2024。世界医学会《赫尔辛基宣言》2024 年 10 月修订版，涉及人的医学研究伦理原则，官网公开全文。🆓 `wma2024helsinki`
- [Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals](https://www.icmje.org/icmje-recommendations.pdf) - International Committee of Medical Journal Editors，网页 2026。国际医学期刊编辑委员会的《医学期刊学术工作的实施、报告、编辑和发表建议》，含署名标准、利益冲突、试验登记、数据共享、预印本政策。2026 年 1 月更新版。🆓 `icmje2026recommendations`
- [CONSORT 2025 statement: Updated guideline for reporting randomised trials](https://doi.org/10.1371/journal.pmed.1004587) - Hopewell 等人，PLOS Medicine 2025。CONSORT 2025 声明，随机试验的报告规范（30 项清单加流程图），CC BY 开放获取。🆓 `hopewell2025consort`
- [The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) Statement: Guidelines for Reporting Observational Studies](https://doi.org/10.1371/journal.pmed.0040296) - von Elm 等人，PLoS Medicine 2007。STROBE 声明，观察性研究（队列、病例对照、横断面）的报告规范，22 项清单，CC BY 开放获取。🆓 `vonelm2007strobe`
- [Strengthening the Reporting of Observational Studies in Epidemiology (STROBE): Explanation and Elaboration](https://doi.org/10.1371/journal.pmed.0040297) - Vandenbroucke 等人，PLoS Medicine 2007。STROBE 的配套解释文章（Explanation and Elaboration），解释三种观察性设计、偏倚与混杂等，CC BY 开放获取。🆓 `vandenbroucke2007strobe`
- [The CARE guidelines: consensus-based clinical case reporting guideline development](https://doi.org/10.1186/1752-1947-7-223) - Gagnier 等人，Journal of Medical Case Reports 2013。CARE 病例报告规范（13 项清单）及其制定过程，开放获取。🆓 `gagnier2013care`
- [New evidence pyramid](https://doi.org/10.1136/ebmed-2016-110401) - Murad 等人，Evidence-Based Medicine 2016。讨论传统证据金字塔的局限（结合 GRADE），建议把系统综述当作审视证据的"透镜"。CC BY-NC 4.0 开放获取。🆓 `murad2016new`
- [Why Most Published Research Findings Are False](https://doi.org/10.1371/journal.pmed.0020124) - Ioannidis，PLoS Medicine 2005。用概率模型论证研究发现可信度受样本量、效应大小、设计灵活性、利益冲突等影响的著名观点文章，CC BY 开放获取。引用时注明是模型论证。🆓 `ioannidis2005why`
- [About Us; What Is a Reporting Guideline?](https://www.equator-network.org/about-us/) - EQUATOR Network，网页。EQUATOR 网络官网的"关于我们"和"什么是报告规范"页面。🆓 `equatorreporting`

**心理学与认知科学**

- [Estimating the Reproducibility of Psychological Science](https://discovery.dundee.ac.uk/ws/files/7385883/RPP_SCIENCE_2015.pdf) - Open Science Collaboration，Science 2015。开放科学合作组织重做 100 项心理学研究的报告，可重复性危机的标志性研究。邓迪大学机构库公开的同行评审接受稿。🆓 `osc2015estimating`
- [Psychology's Renaissance](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/05/Nelson-Simmons-Simonsohn-2018.pdf) - Nelson 等人，Annual Review of Psychology 2018。《False-Positive Psychology》作者回顾 2010 年以来心理学的方法改革（p-hacking、披露、预注册、重复研究的判断方法）。作者主页公开的 PDF。🆓 `nelson2018psychology`
- [False-Positive Citations](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/02/26-Simmons-Nelson-Simonsohn-2018.pdf) - Simmons 等人，Perspectives on Psychological Science 2018。作者回顾 2011 年《False-Positive Psychology》的写作和被引用情况，修正"每组至少 20 人"的建议，并主张预注册。作者主页公开的 PDF。🆓 `simmons2018false`
- [The Preregistration Revolution](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5856500/) - Nosek 等人，Proceedings of the National Academy of Sciences 2018。讲预注册是什么、为什么需要，以及偏离计划、已有数据、探索性研究等情况下怎样做。PNAS 开放获取，PubMed Central 全文。🆓 `nosek2018preregistration`
- [The Past, Present and Future of Registered Reports](https://orca.cardiff.ac.uk/id/eprint/145541/1/Chambers%26Tzavella2021-MS.pdf) - Chambers 等人，Nature Human Behaviour 2022。注册报告的历史、效果证据、局限和给作者、审稿人、编辑的建议。卡迪夫大学机构库公开的作者接受稿。🆓 `chambers2022past`
- [The Weirdest People in the World?](https://www.konsortswd.de/wp-content/uploads/RatSWD_WP_139.pdf) - Henrich 等人，Behavioral and Brain Sciences 2010。提出 WEIRD 样本问题的经典文章：行为科学的被试大多来自西方富裕社会，而这些人群在很多心理指标上是离群的。RatSWD 工作论文版。🆓 `henrich2010weirdest`
- [Ethical Principles of Psychologists and Code of Conduct (2002, amended effective June 1, 2010, and January 1, 2017)](https://www.apa.org/ethics/code/ethics-code-2017.pdf) - American Psychological Association，网页 2017。美国心理学会伦理准则（2002 年通过，含 2010、2016 年修订）。第 8 节为研究与发表，第 9 节为测评。🆓 `apa2017ethical`
- [Journal Article Reporting Standards for Quantitative Research in Psychology: The APA Publications and Communications Board Task Force Report](https://www.apa.org/pubs/journals/releases/amp-amp0000191.pdf) - Appelbaum 等人，American Psychologist 2018。APA 定量研究报告标准（JARS–Quant）的工作组报告，含各部分应报告的条目表。APA 官网公开 PDF。🆓 `appelbaum2018journal`
- [Journal Article Reporting Standards (JARS)](https://apastyle.apa.org/jars) - American Psychological Association，APA Style 网页 2025。APA Style 网站的 JARS 总页面，说明定量、定性、混合方法和种族民族文化四套报告标准的适用范围。🆓 `apajars`
- [About APA Style](https://apastyle.apa.org/about-apa-style) - American Psychological Association，APA Style 网页 2023。APA Style 网站的"About APA Style"页面，说明 APA 格式的由来、适用领域和目的。🆓 `apastyleabout`
- [Registered Reports](https://www.cos.io/initiatives/registered-reports) - Center for Open Science，Center for Open Science 网页 2026。开放科学中心的注册报告页面：定义、采用期刊列表、最低要求和入门步骤。🆓 `cosregisteredreports`
- [Sample Size Justification](https://osf.io/preprints/psyarxiv/9d3yf/) - Lakens，Collabra: Psychology 2022。讲怎样说明样本量的六种理由，以及功效分析的常见误区。PsyArXiv 预印本，正式版在开放获取期刊 Collabra: Psychology。🆓 `lakens2022sample`
- [Measurement Schmeasurement: Questionable Measurement Practices and How to Avoid Them](https://osf.io/preprints/psyarxiv/hs7wm/) - Flake 等人，Advances in Methods and Practices in Psychological Science 2020。提出"可疑测量做法"（QMP）这一概念，附透明报告测量的问题清单。PsyArXiv 上经同行评审的预印本。🆓 `flake2020measurement`

**经济学**

- [The Credibility Revolution in Empirical Economics: How Better Research Design Is Taking the Con out of Econometrics](https://www.nber.org/system/files/working_papers/w15794/w15794.pdf) - Angrist 等人，Journal of Economic Perspectives 2010。Angrist 和 Pischke 回顾 1983 年以来实证经济学的"可信性革命"，介绍随机实验、工具变量、断点回归、双重差分，讨论宏观和产业组织，并回应对设计派的批评。🆓 `angrist2010credibility`
- [Writing Tips for Ph.D. Students](https://www.johnhcochrane.com/s/phd_paper_writing.pdf) - Cochrane，网页 2005。芝加哥大学金融经济学家 John Cochrane 给博士生的写作建议，含论文结构、实证识别清单和研讨会报告建议。作者主页公开。🆓 `cochrane2005writing`
- [How to Build an Economic Model in Your Spare Time](https://people.ischool.berkeley.edu/~hal/Papers/how.pdf) - Varian，The American Economist 1997。Hal Varian 讲自己怎样做理论研究：找想法、简化模型、推广、做报告、写论文。作者主页公开。🆓 `varian1997build`
- [Star Wars: The Empirics Strike Back](https://docs.iza.org/dp7268.pdf) - Brodeur 等人，American Economic Journal: Applied Economics 2016。统计 2005–2011 年 AER、JPE、QJE 上约五万个检验的 p 值分布，发现刚好低于显著性门槛的结果偏多，解释为研究者挑选"显著"的设定。摘录依据 2013 年 IZA 讨论稿版。🆓 `brodeur2016star`
- [The Slowdown of the Economics Publishing Process](https://www.nber.org/system/files/working_papers/w7804/w7804.pdf) - Ellison，Journal of Political Economy 2002。记录 1970–1999 年经济学顶级期刊审稿周期的大幅延长，并分析原因。摘录依据 NBER 工作论文版（2000 年）。🆓 `ellison2002slowdown`
- [Nine Facts about Top Journals in Economics](https://www.nber.org/system/files/working_papers/w18665/w18665.pdf) - Card 等人，Journal of Economic Literature 2013。用 1970–2012 年五大期刊的数据，总结投稿量、接收率、篇幅、作者数、引用等九个趋势。摘录依据 NBER 工作论文版。🆓 `card2013nine`
- [Publishing and Promotion in Economics: The Tyranny of the Top Five](https://docs.iza.org/dp11868.pdf) - Heckman 等人，Journal of Economic Literature 2020。分析五大期刊发表对终身教职的影响，并批评以五大为筛选标准的做法。摘录依据 2018 年 IZA 讨论稿版。🆓 `heckman2020tyranny`
- [What's in a Surname? The Effects of Surname Initials on Academic Success](https://web.stanford.edu/~leinav/pubs/JEP2006.pdf) - Einav 等人，Journal of Economic Perspectives 2006。研究经济学按字母顺序署名的惯例对职业成就的影响，并与按贡献署名的心理学对照。作者主页公开期刊版。🆓 `einav2006surname`
- [A Guide and Advice for Economists on the U.S. Junior Academic Job Market: 2018–2019 Edition](https://www.aeaweb.org/content/file?id=869) - Cawley，American Economic Association 2018。美国经济学博士学术求职指南（2018–19 版），讲求职论文、申请、面试、校园访问、谈判等。AEA 网站公开。🆓 `cawley2018guide`
- [Promises and Perils of Pre-analysis Plans](https://www.aeaweb.org/articles?id=10.1257/jep.29.3.61) - Olken，Journal of Economic Perspectives 2015。讨论经济学中预分析计划的内容、好处、局限和成本，主要针对随机对照试验。只引用了文章页上的公开摘要。🆓 `olken2015promises`
- [Working Papers](https://www.nber.org/papers) - National Bureau of Economic Research，网页。NBER 工作论文系列的说明页面：同行评审前发布、开放获取规则。2026 年 10 月 6 日读取。🆓 `nberworkingpapers`
- [Data and Code Availability Policy](https://www.aeaweb.org/journals/data/data-code-policy) - American Economic Association，网页 2026。美国经济学会期刊的数据与代码可得性政策（2026 年 2 月版）及实验和一手数据论文的补充政策。🆓 `aea2026data`
- [About the AEA RCT Registry; AEA RCT Registry Registration Guidelines](https://www.aeaweb.org/journals/policies/rct-registry) - American Economic Association，网页 2026。AEA 随机对照试验注册平台的说明、注册指南和常见问题，含 AEA 期刊对田野实验登记的要求。🆓 `aea2026rct`
- [Disclosure Policy](https://www.aeaweb.org/journals/policies/disclosure-policy) - American Economic Association，网页 2026。AEA 期刊的利益披露政策：资金来源、利益相关方资助、审阅权、伦理审查批准等。🆓 `aea2026disclosure`

**历史与考古**

- [Statement on Standards of Professional Conduct](https://web.archive.org/web/20240604095630/https://www.historians.org/jobs-and-professional-development/statements-standards-and-guidelines-of-the-discipline/statement-on-standards-of-professional-conduct) - American Historical Association，American Historical Association 网页 2023。美国历史学会的职业行为准则（2023 年修订版），讲一手/二手资料、注释、抄袭、保密承诺和简历诚信。🆓 `aha2023standards`
- [Statement on Policies Regarding the Option to Embargo Completed History PhD Dissertations](https://web.archive.org/web/20240601005252/https://www.historians.org/jobs-and-professional-development/statements-standards-and-guidelines-of-the-discipline/statement-on-policies-regarding-the-option-to-embargo-completed-history-phd-dissertations) - American Historical Association，American Historical Association 网页 2013。美国历史学会 2013 年声明，建议允许历史学博士论文电子版延迟公开最多六年；说明了"以书为本"、博士论文改书的周期和终身教职对专著的要求。🆓 `aha2013embargo`
- [Guidelines for Acknowledgment of Collaborators](https://web.archive.org/web/20240601010410/https://www.historians.org/jobs-and-professional-development/statements-standards-and-guidelines-of-the-discipline/guidelines-for-acknowledgment-of-collaborators) - American Historical Association，American Historical Association 网页 2021。美国历史学会 2021 年关于承认合作者的一段式指南，提到合作增加、署名顺序可按贡献或字母排。🆓 `aha2021collaborators`
- [Against Presentism](https://web.archive.org/web/20220918163213/https://www.historians.org/publications-and-directories/perspectives-on-history/may-2002/against-presentism) - Hunt，Perspectives on History 2002。Lynn Hunt 任美国历史学会会长时的专栏短文，讲"当下主义"的两种表现和应对。🆓 `hunt2002against`
- [OHA Principles and Best Practices: Principles and Best Practices for Oral History](https://oralhistory.org/principles-and-best-practices-revised-2018/) - Oral History Association，Oral History Association 网页 2018。美国口述历史协会 2018 年通过的原则与最佳实践，含伦理声明、访谈前后的操作要求、保存和使用规范。🆓 `oha2018principles`
- [SAA Principles of Archaeological Ethics](https://www.saa.org/common/Uploaded%20files/saadocs/CareerPractice/saa_ethics.pdf) - Society for American Archaeology，网页 2024。美国考古学会 2024 年修订的九条考古伦理原则（守护、责任、不商业化、公众与社区参与、保存记录、报告、培训、安全环境、多元包容）。🆓 `saa2024principles`
- [Standard and Universal Guidance for Archaeological Excavation](https://www.archaeologists.net/sites/default/files/2024-11/CIfA-Standard-Archaeological-Excavation_2023.pdf) - Chartered Institute for Archaeologists，网页 2023。英国特许考古学家协会 2023 年的考古发掘标准和通用指南，规定项目设计书、记录、发掘后评估、报告和归档的要求。🆓 `cifa2023excavation`
- [Learning to Do Historical Research: A Primer for Environmental Historians and Others](https://www.williamcronon.net/researching/) - Cronon 等人，网页 2009。William Cronon 与其 2008 年秋季研究生讨论课学生合写的历史研究入门网站，讲提问、找文献、做笔记、查手稿、论证与叙事。🆓 `cronon2009learning`
- [Chicago-Style Citation Quick Guide](https://www.chicagomanualofstyle.org/tools_citationguide.html) - The University of Chicago，The Chicago Manual of Style Online 2024。《芝加哥格式手册》官网免费公开的引用速查页（第 18 版），说明"注释—参考书目"和"作者—年份"两种体系及各自的适用领域。🆓 `chicago2024citation`
- [Supporting the Changing Research Practices of Historians](https://sr.ithaka.org/wp-content/uploads/2015/08/supporting-the-changing-research-practices-of-historians.pdf) - Rutner 等人，Ithaka S+R 2012。Ithaka S+R 2012 年基于 39 位美国历史学者和博士生访谈的报告，讲档案拍照、资料整理、数字方法和终身教职对专著的要求。🆓 `rutner2012supporting`

**化学**

- [Identifying and Evaluating Hazards in Research Laboratories](https://www.acs.org/content/dam/acsorg/about/governance/committees/chemicalsafety/publications/identifying-and-evaluating-hazards-in-research-laboratories.pdf) - American Chemical Society, Committee on Chemical Safety, Hazard Identification and Evaluation Task Force，American Chemical Society 2015。美国化学会化学安全委员会 2015 年的研究实验室危害识别与评估指南，应 CSB 对得克萨斯理工大学事故的建议编写，含五种评估工具和"变化控制"一章。🆓 `acs2015identifying`
- [Ethical Guidelines to Publication of Chemical Research](https://researcher-resources.acs.org/publish/ethical_guidelines) - American Chemical Society Publications，ACS Publications 网页 2026。美国化学会出版部的《化学研究发表伦理准则》，2026 年 6 月 15 日生效的修订版，规定编辑、作者、审稿人的义务（数据、安全、重复发表、署名等）。🆓 `acs2026ethical`
- [The Journal of Organic Chemistry: Author Guidelines](https://researcher-resources.acs.org/publish/author_guidelines?coden=joceah) - American Chemical Society，ACS Publications 网页 2026。美国化学会《有机化学杂志》（JOC）作者须知，含化合物表征、纯度、核磁原始数据、计算数据、安全声明和预印本政策的详细要求。🆓 `acsjocguidelines`
- [ACS Research Data Policy](https://researcher-resources.acs.org/publish/data_policy) - American Chemical Society Publications，ACS Publications 网页。美国化学会出版部的研究数据政策，支持 FAIR 原则，规定四级数据共享要求和数据可用性声明的写法。🆓 `acsdatapolicy`
- [Reproducibility in Chemical Research](https://doi.org/10.1002/anie.201606591) - Bergman 等人，Angewandte Chemie International Edition 2016。Bergman 和 Danheiser 在 Angewandte Chemie 的两页社论，讨论化学研究中重复不出结果的原因（含《Organic Syntheses》2010—2016 年 7.5% 拒稿率）和对课题负责人、期刊、审稿人的建议。🆓 `bergman2016reproducibility`
- [Organic Syntheses: Instructions for Authors](https://www.orgsyn.org/instructions.aspx) - Organic Syntheses, Inc.，Organic Syntheses 网页。《Organic Syntheses》作者须知，规定实验步骤的详细写法、规模、纯度（≥97%）、安全说明（Note 1），以及编委实验室独立核查的规则。🆓 `orgsyninstructions`
- [About ChemRxiv; FAQs for ChemRxiv Authors](https://chemrxiv.org/engage/assets/public/chemrxiv/term/about.htm) - ChemRxiv，ChemRxiv 网页。化学预印本平台 ChemRxiv 的简介和作者常见问题，说明筛查方式、不经同行评审、学科分类、合办学会和撤稿规则。🆓 `chemrxivabout`
- [IUPAC FAIR Chemistry Cookbook](https://iupac.github.io/WFChemCookbook/intro.html) - IUPAC WorldFAIR Chemistry D3.2 Project，网页。国际纯粹与应用化学联合会（IUPAC）WorldFAIR 化学项目维护的在线手册，用可运行的示例演示化学数据的机器可读管理和 FAIR 原则。🆓 `iupacfaircookbook`

**地球与环境科学**

- [AGU Scientific Integrity and Professional Ethics](https://www.agu.org/-/media/Files/Learn-About-AGU/AGU_Scientific_Integrity_and_Professional_Ethics_Policy_document.pdf) - American Geophysical Union，网页 2023。美国地球物理学会的科学诚信与职业伦理政策（2023 更新版），含行为准则、骚扰属于科研不端、作者和编辑义务。🆓 `agu2023ethics`
- [Data and Software Sharing Guidance for Authors Submitting to AGU Journals](https://data.agu.org/resources/agu-data-software-sharing-guidance) - Fox 等人，Zenodo 2021。AGU 期刊的数据与软件共享指南，含可获取性声明模板、模式研究的特别要求、数据库选择建议。🆓 `fox2021agudata`
- [GMD Code and Data Policy](https://www.geoscientific-model-development.net/policies/code_and_data_policy.html) - Geoscientific Model Development，Copernicus Publications。期刊 Geoscientific Model Development 的代码与数据政策：投稿时就要存档确切版本的代码和数据，不接受延期公开。🆓 `gmdcodepolicy`
- [Editorial: The publication of geoscientific model developments v1.2](https://doi.org/10.5194/gmd-12-2215-2019) - GMD Executive Editors，Geoscientific Model Development 2019。GMD 编辑部 2019 年社论，解释为什么模式论文必须公开代码、为什么不接受延期、什么样的地方才算存档。🆓 `gmd2019editorial`
- [Guidance Note for Lead Authors of the IPCC Fifth Assessment Report on Consistent Treatment of Uncertainties](https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf) - Mastrandrea 等人，Intergovernmental Panel on Climate Change (IPCC) 2010。IPCC 第五次评估报告的不确定性指南，定义"信度"和"可能性"两套校准用语。🆓 `mastrandrea2010ipcc`
- [About IGSNs](https://www.igsn.org/about-igsns) - IGSN e.V.，IGSN e.V. 网页。IGSN e.V. 对国际通用样品编号的介绍：为什么样品需要永久编号。🆓 `igsnabout`
- [Using IGSN in Publications](https://www.igsn.org/resources/using-igsn-in-publications) - IGSN e.V.，IGSN e.V. 网页。IGSN e.V. 关于在论文和样品标签上怎样显示 IGSN 的说明。🆓 `igsnpublications`
- [About EarthArXiv](https://eartharxiv.org/repository/about/) - EarthArXiv，EarthArXiv 网页。EarthArXiv 地球科学预印本平台的"关于"页面。🆓 `eartharxivabout`
- [Frequently Asked Questions](https://eartharxiv.github.io/faq.html) - EarthArXiv，EarthArXiv 网页。EarthArXiv 常见问题：预印本删不掉、与期刊政策的关系、和 AGU 的 ESSOAr 的关系。🆓 `eartharxivfaq`
- [Moderation Policy](https://eartharxiv.github.io/moderation.html) - EarthArXiv，EarthArXiv 网页。EarthArXiv 审核政策：收什么、不收什么、稿件格式要求。🆓 `eartharxivmoderation`
- [Assessing data availability and research reproducibility in hydrology and water resources](https://doi.org/10.1038/sdata.2019.30) - Stagge 等人，Scientific Data 2019。对六种水文与水资源期刊 2017 年论文的数据可获取性和可复现性抽查（360 篇）。与第 62 篇共用。🆓 `stagge2019assessing`
- [Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) experimental design and organization](https://doi.org/10.5194/gmd-9-1937-2016) - Eyring 等人，Geoscientific Model Development 2016。第六期耦合模式比较计划（CMIP6）的总体设计和组织方式。🆓 `eyring2016cmip6`
- [Survey of Academic Field Experiences (SAFE): Trainees Report Harassment and Assault](https://doi.org/10.1371/journal.pone.0102172) - Clancy 等人，PLoS ONE 2014。2013 年对 666 名野外科学工作者（以人类学和考古学者为主）的网上调查，关于野外的骚扰和侵害。🆓 `clancy2014survey`
- [Safety and Belonging in the Field: A Checklist for Educators](https://go-outdoors.caltech.edu/documents/20636/greene-et-al_2021.pdf) - Greene 等人，EarthArXiv preprint (non-peer reviewed) 2021。英国高校地理、地球与环境科学师生写的野外实习安全与包容检查清单（EarthArXiv 预印本，未经同行评审）。🆓 `greene2021safety`

**土木工程**

- [Code of Ethics](https://www.asce.org/career-growth/ethics/code-of-ethics) - American Society of Civil Engineers，ASCE 网页 2020。美国土木工程师学会（ASCE）伦理准则全文（1914 年首次通过，2020 年 10 月 26 日修订），核心是"首先保护公众的健康、安全和福祉"。🆓 `asce2020code`
- [Data Availability Statement](https://ascelibrary.org/page/dataavailability) - American Society of Civil Engineers，ASCE Library。ASCE 期刊的数据可得性声明政策页面：可选说法、数据仓库建议、专有数据的处理。🆓 `ascedataavailability`
- [New Policy to Specify Availability of Data, Models, and Code](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000998) - Rosenberg 等人，Journal of Water Resources Planning and Management 2018。《水资源规划与管理期刊》编辑按语，宣布要求作者说明数据、模型和代码的可得性；这项政策后来推广到几乎所有 ASCE 期刊。🆓 `rosenberg2018new`
- [The Next Frontier: Making Research More Reproducible](https://par.nsf.gov/servlets/purl/10188458) - Rosenberg 等人，Journal of Water Resources Planning and Management 2020。水资源领域的社论，分析复现研究的障碍，并给作者、期刊、资助方和机构列出提高可复现性的检查清单。🆓 `rosenberg2020next`
- [Conference Papers and Prior Publication](https://doi.org/10.1061/(ASCE)BE.1943-5592.0000294) - Hendrickson 等人，Journal of Bridge Engineering 2011。ASCE《桥梁工程期刊》社论：ASCE 关于一稿两发、会议论文转期刊（一般要 50% 新内容）和 TRB 年会论文的规定。🆓 `hendrickson2011conference`
- [Verification, Validation, and Predictive Capability in Computational Engineering and Physics](https://digital.library.unt.edu/ark:/67531/metadc885833/m2/1/high_res_d/918370.pdf) - Oberkampf 等人，Sandia National Laboratories 2003。美国桑迪亚国家实验室公开报告，系统讨论计算模型的验证、确认、校准和预测能力，包括"积木式"确认试验层级。🆓 `oberkampf2003verification`
- [NHERI@UTexas Safety Plan, Version 2.3](https://utexas.designsafe-ci.org/media/filer_public/02/b1/02b1b9f1-9b83-4fe7-ad82-7acc4c959a50/nheriutexas_safety_plan-20200826.pdf) - NHERI@UTexas Management Team，University of Texas at Austin 2020。美国 NHERI 在得克萨斯大学奥斯汀分校的现场试验设施（大型移动激振车）安全手册 2.3 版：工作危害分析、现场踏勘、每日安全简会、停工规则。🆓 `nheriutexas2020safety`
- [NHERI Lehigh RTMD Experimental Facility User's Guide](https://lehigh.designsafe-ci.org/media/cms_page_media/95/NHERI%20Lehigh%20RTMD%20EF%20User's%20Guide%202016-11-02_YsuNvbw.pdf) - NHERI Lehigh RTMD Experimental Facility，Lehigh University 2016。美国 NHERI 在利哈伊大学的大尺度结构试验设施用户指南：试验矩阵审批、控制软件确认、数据管理、搭载项目、培训和安全。🆓 `nherilehigh2016users`
- [Codes and Standards](https://www.asce.org/publications-and-news/codes-and-standards) - American Society of Civil Engineers，ASCE 网页。ASCE"规范与标准"页面：标准的制定流程（ANSI 认可、均衡委员会、公众意见期、5 年周期）以及参与方式。🆓 `asce2026standards`
- [ASCE/SEI 7-22: Minimum Design Loads and Associated Criteria for Buildings and Other Structures](https://www.asce.org/publications-and-news/codes-and-standards/asce-sei-7-22) - American Society of Civil Engineers，ASCE 网页。ASCE 网站上 ASCE/SEI 7-22（建筑及其他结构最小设计荷载标准）的介绍页：新版变化和委员会构成。🆓 `asce2026asce7`
- [FY 2008 Budget Request Details: National Earthquake Hazards Reduction Program](https://www.nist.gov/congressional-and-legislative-affairs/fy08-national-earthquake-hazards-reduction-program) - National Institute of Standards and Technology，NIST 网页。美国国家标准与技术研究院 2008 财年预算说明中的国家地震减灾计划一节，指出基础研究成果和建筑规范之间的落地差距。🆓 `nist2008nehrp`

**机械工程**

- [Journal of Fluids Engineering Editorial Policy Statement on the Control of Numerical Accuracy](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf) - Journal of Fluids Engineering，American Society of Mechanical Engineers。《流体工程杂志》（ASME）关于数值精度控制的编辑政策声明，十条标准加简化版，ASME 官网免费 PDF。🆓 `jfenumaccuracy`
- [Procedure for Estimation and Reporting of Uncertainty Due to Discretization in CFD Applications](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf) - Celik 等人，Journal of Fluids Engineering 2008。Celik、Ghia、Roache、Freitas 为《流体工程杂志》写的离散误差估计与报告程序（网格收敛指数方法）。🆓 `celik2008procedure`
- [Editorial Policy Statement on Numerical and Experimental Accuracy](https://aiaa.org/EditorialPolicyStatement) - American Institute of Aeronautics and Astronautics，AIAA 网页。美国航空航天学会（AIAA）期刊关于数值精度和实验精度的编辑政策声明。🆓 `aiaaeditorialpolicy`
- [Evaluation of Measurement Data – Guide to the Expression of Uncertainty in Measurement](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf) - Joint Committee for Guides in Metrology，BIPM 2008。《测量不确定度表示指南》（GUM），国际通行的测量不确定度评定与报告指南，BIPM 免费提供。🆓 `jcgm2008gum`
- [Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results](https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1297.pdf) - Taylor 等人，National Institute of Standards and Technology 1994。NIST 技术说明 1297，GUM 的精简说明和 NIST 的不确定度政策。🆓 `taylor1994nist`
- [Verification and Validation in Computational Fluid Dynamics](https://www.osti.gov/biblio/793406) - Oberkampf 等人，Sandia National Laboratories 2002。桑迪亚国家实验室报告，系统论述计算流体力学的验证与确认，含确认实验设计指南。🆓 `oberkampf2002verification`
- [Society Policy P-15.7: Ethics (Code of Ethics of Engineers)](https://www.asme.org/getmedia/1d9d64bf-f6a7-4e75-a8f5-0cabd8c04269/P-15-7-Ethics_2.pdf) - American Society of Mechanical Engineers，ASME 2024。ASME 学会政策 P-15.7《工程师伦理准则》，2024 年 10 月修订版。🆓 `asme2024ethics`
- [The ASME Criteria for Interpretation of the Canons](https://www.asme.org/wwwasmeorg/media/ResourceFiles/AboutASME/Get%20Involved/Advocacy/Policy-Publications/CRITERIA-FOR-INTERPRETATION-OF-THE-CANONSJune2012.pdf) - American Society of Mechanical Engineers，ASME 2012。ASME 对《伦理准则》基本条款的解释准则（署名、抄袭、利益冲突、知识产权约定等）。🆓 `asme2012canons`
- [Ethical Standards](https://www.asme.org/publications-submissions/proceedings/submission-review-and-acceptance/ethical-standards) - American Society of Mechanical Engineers，ASME Proceedings: Submission, Review and Acceptance 2026。ASME 出版伦理标准（作者、审稿人的伦理义务），位于会议论文集投稿栏目下。🆓 `asmeethicalstandards`
- [Papers Presented at a Conference](https://www.asme.org/publications-submissions/journals/information-for-authors/journal-guidelines/papers-presented-at-a-conference) - American Society of Mechanical Engineers，ASME Journals: Information for Authors 2026。ASME 期刊关于会议论文转投期刊的规定。🆓 `asmeconfpapers`
- [IMECE 2026: International Mechanical Engineering Congress & Exposition](https://event.asme.org/IMECE) - American Society of Mechanical Engineers，ASME event 网页 2026。ASME 国际机械工程大会与展览（IMECE）2026 年会议主页，含技术方向和投稿日程。🆓 `asme2026imece`
- [Machine Guarding – Overview](https://www.osha.gov/machine-guarding) - Occupational Safety and Health Administration，U.S. Department of Labor。美国职业安全与健康管理局（OSHA）机器防护概述页面。🆓 `oshamachineguarding`
- [Control of Hazardous Energy (Lockout/Tagout) – Overview](https://www.osha.gov/control-hazardous-energy) - Occupational Safety and Health Administration，U.S. Department of Labor。OSHA 危险能量控制（上锁挂牌）概述页面。🆓 `oshalockout`
- [Machine Shop Safety – Guideline](https://www.cmu.edu/ehs/Workplace-Construction/documents/machine-shop-safety-policy.pdf) - Carnegie Mellon University Environmental Health and Safety，Carnegie Mellon University 2025。卡内基梅隆大学环境健康与安全办公室的机加工车间安全指南（第 15 版，2025 年 11 月修订）。🆓 `cmu2025machineshop`

**化学工程**

- [Texas Tech University Laboratory Explosion: Case Study](https://www.csb.gov/assets/1/20/CSB_Study_TTU_.pdf) - U.S. Chemical Safety and Hazard Investigation Board，网页 2011。美国化学安全与危害调查委员会对 2010 年得克萨斯理工大学化学系实验室爆炸事故的案例研究，分析了放大、危害评估、书面规程、未遂事件报告和组织监管方面的问题。美国联邦政府出版物，免费下载。另一位写作者也可能用到此 key，内容相同时合并即可。🆓 `csb2011texastech`
- [Toward Benchmarking in Catalysis Science: Best Practices, Challenges, and Opportunities](https://doi.org/10.1021/acscatal.6b00183) - Bligaard 等人，ACS Catalysis 2016。十位催化研究者的观点文章，讲催化研究中怎样测量和报告活性、选择性、失活等数据，才能公平比较；分计算、多相、分子和电催化四个方向给出建议。出版方以 ACS AuthorChoice 许可开放获取。🆓 `bligaard2016benchmarking`
- [Techno-Economic Assessment Guidelines for CO2 Utilization](https://www.frontiersin.org/articles/10.3389/fenrg.2020.00005/full) - Zimmermann 等人，Frontiers in Energy Research 2020。Global CO2 Initiative 等机构《二氧化碳利用技术经济评估与生命周期评估指南》中技术经济评估部分的期刊摘要版，给出评估目标、范围、数据、计算、解读和报告各阶段的必须规则和推荐规则。CC BY 开放获取。🆓 `zimmermann2020tea`
- [A Guideline for Life Cycle Assessment of Carbon Capture and Utilization](https://www.frontiersin.org/articles/10.3389/fenrg.2020.00015/full) - Muller 等人，Frontiers in Energy Research 2020。同一套指南中生命周期评估部分的期刊摘要版，讲碳捕集与利用技术的功能单位、系统边界、低技术成熟度工艺的评估和报告要求。CC BY 开放获取。🆓 `muller2020lca`
- [Code of Ethics](https://www.aiche.org/about/governance/policies/code-ethics) - American Institute of Chemical Engineers，AIChE 网页。美国化学工程师学会的伦理准则，约束学会会员，共十余条。🆓 `aichecodeethics`
- [Industrial & Engineering Chemistry Research: Author Guidelines](https://researcher-resources.acs.org/publish/author_guidelines?coden=iecred) - American Chemical Society，ACS Researcher Resources。美国化学会期刊 Industrial & Engineering Chemistry Research 的作者指南（页面标注 2026-10-05 更新），含期刊范围、预印本、数据、安全声明、专利和利益冲突要求。🆓 `acsiecrauthorguide`

**材料工程与纳米技术**

- [Minimum information reporting in bio–nano experimental literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC6150419/) - Faria 等人，Nature Nanotechnology 2018。纳米—生物交叉研究的最低信息报告标准（MIRIBEL），分材料表征、生物学表征、实验流程三类条目，附检查清单。🆓 `faria2018minimum`
- [Approaches to Safe Nanotechnology: Managing the Health and Safety Concerns Associated with Engineered Nanomaterials](http://web.archive.org/web/20260726080036/https://www.cdc.gov/niosh/docs/2009-125/pdfs/2009-125.pdf) - National Institute for Occupational Safety and Health，U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, National Institute for Occupational Safety and Health 2009。美国国家职业安全卫生研究所关于安全操作工程纳米材料的指南，讲暴露途径、工程控制、工作习惯、个人防护和燃爆风险。🆓 `niosh2009approaches`
- [A checklist for photovoltaic research](https://www.nature.com/articles/nmat4473) - Nature Materials，网页 2015。Nature Materials 2015 年社论，宣布光伏论文须填写技术信息清单，建议同时报告平均效率和最好器件、说明是否经独立认证。🆓 `naturematerials2015checklist`
- [Solar Cells Reporting Summary](https://www.nature.com/documents/nr-photovoltaic-reporting-flat.pdf) - Nature Portfolio，Nature Portfolio 网页。Nature Portfolio 期刊的太阳能电池报告摘要表（平面参考版），列出器件面积、电流—电压测试、校准、认证、统计、稳定性等必报条目。🆓 `naturesolarcellsreporting`
- [Reporting standards and availability of data, materials, code and protocols](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards) - Nature Portfolio，Nature Portfolio editorial policies。Nature Portfolio 关于报告规范和数据、材料、代码、流程可获取性的编辑政策页面。🆓 `naturereportingstandards`
- [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618) - Wilkinson 等人，Scientific Data 2016。FAIR 数据原则（可查找、可获取、可互操作、可重用）的原始文献。🆓 `wilkinson2016fair`
- [An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles](https://www.nature.com/articles/s41560-021-00941-3) - Jacobsson 等人，Nature Energy 2022。钙钛矿太阳能电池数据库项目，从 1.5 万多篇论文中人工提取 4.2 万多个器件数据，讨论批次差异、隐藏参数和只报最好器件的问题。🆓 `jacobsson2022open`
- [NOMAD: The FAIR Concept for Big Data-Driven Materials Science](https://arxiv.org/abs/1805.05039) - Draxl 等人，arXiv:1805.05039 2018。NOMAD 计算材料数据库的设计理念和 2018 年时的数据接收规则，以及实验数据共享的难点。🆓 `draxl2018nomad`
- [Reproducibility in density functional theory calculations of solids](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919278) - Lejaeghere 等人，Science 2016。15 个固体密度泛函理论程序的社区比较，结论是新程序和新势文件之间高度一致、旧的差一些。🆓 `lejaeghere2016reproducibility`
- [Characterization of Nanoparticle Batch-To-Batch Variability](https://pmc.ncbi.nlm.nih.gov/articles/PMC5977325/) - Mulhopt 等人，Nanomaterials 2018。欧洲 14 个实验室对 46 个纳米材料批次的系统表征，评估批次间差异的来源。🆓 `mulhopt2018characterization`
- [User Program Overview](https://foundry.lbl.gov/become-a-foundry-user/) - The Molecular Foundry, Lawrence Berkeley National Laboratory，Molecular Foundry 网页。美国能源部纳米科学用户设施 Molecular Foundry 的用户项目说明：申请、费用、安全培训、致谢要求。🆓 `lblfoundryuser`

**医学工程**

- [Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions: Guidance for Industry and Food and Drug Administration Staff](https://web.archive.org/web/20260513124224/https://www.fda.gov/media/154985/download) - U.S. Food and Drug Administration，U.S. Food and Drug Administration, Center for Devices and Radiological Health 2023。美国 FDA 2023 年最终版指南，讲怎样评估和证明器械相关计算模型（基于物理或机理，不含机器学习）的可信度：使用情境、模型风险、证据类别。🆓 `fda2023cmscredibility`
- [Design Control Guidance for Medical Device Manufacturers](https://web.archive.org/web/20251214094548/https://www.fda.gov/media/116573/download) - U.S. Food and Drug Administration，U.S. Food and Drug Administration, Center for Devices and Radiological Health 1997。美国 FDA 1997 年设计控制指南，用大量例子解释旧版 21 CFR 820.30（研究与开发的界线、设计输入、验证与确认等）；2026 年随 QMSR 实施已撤回，作为历史资料引用。🆓 `fda1997designcontrol`
- [21 CFR 820.30 – Design Controls](https://www.govinfo.gov/content/pkg/CFR-2023-title21-vol8/pdf/CFR-2023-title21-vol8-sec820-30.pdf) - U.S. Government，Code of Federal Regulations, Title 21, Volume 8, revised as of April 1, 2023 (govinfo.gov) 2023。美国 21 CFR 820.30"设计控制"条文（2023 年 4 月 1 日版）。现行版本已删除此节。🆓 `cfr2023designcontrols`
- [21 CFR Part 820 – Quality Management System Regulation](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820) - U.S. Government，Electronic Code of Federal Regulations (eCFR) 2026。美国现行 21 CFR Part 820"质量管理体系法规"，把 ISO 13485:2016 引用为法规内容；§820.20–820.30 已标为保留。🆓 `cfr2026qmsr`
- [FDA Implements Quality Management System Regulation for Medical Devices](https://aabb.org/news-resources/news/article/2026/02/04/fda-implements-quality-management-system-regulation-for-medical-devices) - AABB，AABB News 2026。AABB（输血与生物治疗促进协会）2026 年 2 月 4 日新闻，报道 FDA 实施 QMSR 并撤回 1997 年设计控制指南。用来补 FDA 官网读不到的信息。🆓 `aabb2026qmsr`
- [21 CFR Part 812 – Investigational Device Exemptions](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812) - U.S. Government，Electronic Code of Federal Regulations (eCFR) 2026。美国现行 21 CFR Part 812"研究用器械豁免"，规定器械临床研究的程序、重大风险器械和申办者兼研究者的定义。🆓 `cfr2026ide`
- [BMES Code of Ethics](https://www.bmes.org/hubfs/Files/BMES_Code_of_Ethics_2021_-_Revised_October_2021.pdf) - Biomedical Engineering Society，Biomedical Engineering Society 网页 2021。美国生物医学工程学会（BMES）伦理准则 2021 年修订版，三页，涵盖法规遵守、研究记录、数据与代码、人和动物、技术应用、导师关系和利益冲突。🆓 `bmes2021ethics`
- [Prepare and Submit Manuscript – IEEE Transactions on Biomedical Engineering](https://web.archive.org/web/20250115120531/https://www.embs.org/tbme/for-authors/prepare-and-submit-manuscript/) - IEEE Engineering in Medicine and Biology Society，EMBS 网页 2025。IEEE EMBS 期刊《IEEE Transactions on Biomedical Engineering》的投稿说明页：结构化摘要、会议论文披露、一稿多投处罚、利益冲突、人和动物受试者声明。🆓 `embstbmeprepare`
- [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) - Collins 等人，BMJ 2024。TRIPOD+AI 报告规范（BMJ 2024，开放获取），用于开发或评估诊断、预后预测模型的研究，不论用回归还是机器学习；表 1 列出其他人工智能相关报告规范。🆓 `collins2024tripodai`

**环境工程**

- [Guidance on Systematic Planning Using the Data Quality Objectives Process (EPA QA/G-4)](https://www.epa.gov/sites/default/files/2015-06/documents/g4-final.pdf) - U.S. Environmental Protection Agency，U.S. Environmental Protection Agency, Office of Environmental Information 2006。美国环境保护署的数据质量目标流程指南（QA/G-4），讲采样前怎样用七步做系统规划。🆓 `epa2006dqo`
- [Guidance for Quality Assurance Project Plans (EPA QA/G-5)](https://www.epa.gov/sites/default/files/2015-06/documents/g5-final.pdf) - U.S. Environmental Protection Agency，U.S. Environmental Protection Agency, Office of Environmental Information 2002。美国环境保护署的质量保证项目计划指南（QA/G-5），讲计划每一部分写什么，含质量控制样品和监管链。🆓 `epa2002qapp`
- [Definition and Procedure for the Determination of the Method Detection Limit, Revision 2](https://www.epa.gov/sites/default/files/2016-12/documents/mdl-procedure_rev2_12-13-2016.pdf) - U.S. Environmental Protection Agency，U.S. Environmental Protection Agency, Office of Water 2016。美国环境保护署方法检出限测定程序第 2 版（40 CFR 136 附录 B 的单行本）。🆓 `epa2016mdl`
- [Statistical Methods in Water Resources](https://pubs.usgs.gov/tm/04/a03/tm4a3.pdf) - Helsel 等人，U.S. Geological Survey 2020。美国地质调查局的水资源统计方法教材（2020 年版），含删失数据（低于报告限的数据）的处理。🆓 `helsel2020statistical`
- [Life Cycle Assessment: Principles and Practice](https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P1000L86.PDF) - Scientific Applications International Corporation，U.S. Environmental Protection Agency, National Risk Management Research Laboratory 2006。美国环境保护署的生命周期评价入门报告，讲四个阶段、功能单位、局限和解释。🆓 `epa2006lca`
- [Environmental Science & Technology: Author Guidelines](https://researcher-resources.acs.org/publish/author_guidelines?coden=esthag) - American Chemical Society，ACS Researcher Resources 网页。美国化学会期刊《Environmental Science & Technology》的作者指南，含选题范围、质量控制、数据存储、预印本和学位论文政策。🆓 `estauthorguidelines`
- [Citizen Science During the Flint, Michigan Federal Water Emergency: Ethical Dilemmas and Lessons Learned](https://doi.org/10.5334/cstp.154) - Roy 等人，Citizen Science: Theory and Practice 2019。弗吉尼亚理工大学团队对弗林特饮用水危机中公民科学合作及其伦理问题的回顾（开放获取，当事一方的说法）。🆓 `roy2019citizen`
- [Environmental Justice](http://web.archive.org/web/20240531090447/https://www.epa.gov/environmentaljustice) - U.S. Environmental Protection Agency，EPA 网页 2024。美国环境保护署环境正义主页 2024 年快照，给出当时联邦政策下"环境正义"的定义（原页面已下线）。🆓 `epa2024environmentaljustice`

**生物技术**

- [Biosafety in Microbiological and Biomedical Laboratories](https://www.cdc.gov/labs/pdf/SF__19_308133-A_BMBL6_00-BOOK-WEB-final-3.pdf) - U.S. Centers for Disease Control and Prevention and National Institutes of Health，U.S. Department of Health and Human Services 2020。美国疾病控制与预防中心和国立卫生研究院合编的《微生物和生物医学实验室生物安全》第 6 版，生物安全等级和风险评估的标准参考（建议性文件，非法规）。🆓 `cdc2020bmbl`
- [NIH Guidelines for Research Involving Recombinant or Synthetic Nucleic Acid Molecules](https://osp.od.nih.gov/wp-content/uploads/NIH_Guidelines.pdf) - National Institutes of Health，National Institutes of Health, Office of Science Policy 2024。美国国立卫生研究院《涉及重组或合成核酸分子研究的准则》2024 年 4 月版，规定实验分类、机构生物安全委员会和课题组负责人的责任。🆓 `nih2024guidelines`
- [Global Guidance Framework for the Responsible Use of the Life Sciences: Mitigating Biorisks and Governing Dual-Use Research](https://iris.who.int/bitstream/handle/10665/362313/9789240056107-eng.pdf) - World Health Organization，网页 2022。世界卫生组织《负责任使用生命科学全球指导框架》，给出生物安全、生物安保、两用研究的定义和给科研人员的清单。许可 CC BY-NC-SA 3.0 IGO。🆓 `who2022responsible`
- [Cartagena Protocol on Biosafety to the Convention on Biological Diversity: Text and Annexes](https://www.cbd.int/doc/legal/cartagena-protocol-en.pdf) - Secretariat of the Convention on Biological Diversity，网页 2000。《卡塔赫纳生物安全议定书》英文文本及附件，规定改性活生物体跨境转移的国际规则。🆓 `cbd2000cartagena`
- [The MIQE Guidelines: Minimum Information for Publication of Quantitative Real-Time PCR Experiments](https://doi.org/10.1373/clinchem.2008.112797) - Bustin 等人，Clinical Chemistry 2009。MIQE 指南，定量 PCR 实验发表所需的最低信息和清单。🆓 `bustin2009miqe`
- [MIQE 2.0 and the Urgent Need to Rethink qPCR Standards](https://doi.org/10.3390/ijms26114975) - Bustin，International Journal of Molecular Sciences 2025。MIQE 第一作者 2025 年的开放获取社论，说明 MIQE 2.0 已发表，并指出遵守情况仍参差不齐。🆓 `bustin2025miqe`
- [Reproducibility of Fluorescent Expression from Engineered Biological Constructs in E. coli](https://doi.org/10.1371/journal.pone.0150182) - Beal 等人，PLoS ONE 2016。合成生物学第一项大规模跨实验室测量研究（依托 2014、2015 年 iGEM 大赛，88 个机构），说明校准和测量单位为什么重要。🆓 `beal2016reproducibility`
- [Scale-up of Industrial Microbial Processes](https://doi.org/10.1093/femsle/fny138) - Crater 等人，FEMS Microbiology Letters 2018。工业微生物工艺放大的综述式短文，两位作者来自企业，含常见错误表和尺度相关参数表。🆓 `crater2018scaleup`
- [The Synthetic Biology Open Language (SBOL) Version 3: Simplified Data Exchange for Bioengineering](https://doi.org/10.3389/fbioe.2020.01009) - McLaughlin 等人，Frontiers in Bioengineering and Biotechnology 2020。合成生物学开放语言第 3 版的介绍，用于用标准格式描述工程化生物设计。🆓 `mclaughlin2020sbol3`
- [Recent Executive Actions Related to Gain-of-Function Research and Laboratory Biosafety](https://www.everycrsreport.com/reports/IN12554.html) - Congressional Research Service，网页 2025。美国国会研究服务处 2025 年 5 月的简报，交代美国生物安全监管的格局和 2024 年两用研究政策被要求修订的过程。美国政府作品，通过 EveryCRSReport.com 公开镜像读取。🆓 `crs2025gainoffunction`
- [USG Policy for Stopping High-Risk Life Sciences Research: What Changes for Institutions](https://casrai.org/news/usg-policy-stopping-high-risk-life-sciences-research-institutions-2026) - CASRAI Editorial Board，CASRAI news 2026。研究管理组织 CASRAI 编辑部 2026 年 8 月的解读文章，介绍替代 2024 年两用研究政策的美国新政策对机构和课题组负责人的要求。不是政府原文。🆓 `casrai2026highrisk`

**基础医学**

- [A call for transparent reporting to optimize the predictive value of preclinical research](https://pmc.ncbi.nlm.nih.gov/articles/PMC3511845/) - Landis 等人，Nature 2012。美国国家神经疾病与卒中研究所 2012 年研讨会的建议，提出临床前动物研究至少要报告随机、盲法、样本量估计和数据处理。🆓 `landis2012call`
- [A proposal for validation of antibodies](https://pmc.ncbi.nlm.nih.gov/articles/PMC10335836/) - Uhlen 等人，Nature Methods 2016。国际抗体验证工作组提出的抗体验证"五种思路"，以及使用者在论文中报告抗体的建议。🆓 `uhlen2016proposal`
- [Experimental design and analysis and their reporting II: updated and simplified guidance for authors and peer reviewers](https://pmc.ncbi.nlm.nih.gov/articles/PMC5843711/) - Curtis 等人，British Journal of Pharmacology 2018。《英国药理学杂志》给作者和审稿人的实验设计与分析指南（2018 年更新版），含 n、归一化、离群值、显著性阈值等具体规定和一次合规审查。🆓 `curtis2018experimental`
- [Lost in translation: animal models and clinical trials in cancer treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC3902221/) - Mak 等人，American Journal of Translational Research 2014。癌症领域动物模型向临床试验转化失败的简短叙述性综述，附几个具体失败案例。🆓 `mak2014lost`
- [OECD Principles on Good Laboratory Practice (as revised in 1997)](https://one.oecd.org/document/env/mc/chem(98)17/en/pdf) - OECD，Organisation for Economic Co-operation and Development, Environment Directorate 1998。经济合作与发展组织《良好实验室规范原则》（1997 年修订版，1998 年发布），规定为监管申报做的非临床安全研究怎样计划、实施、记录、质量保证和归档。🆓 `oecd1998glp`
- [WMA Declaration of Taipei on Ethical Considerations regarding Health Databases and Biobanks](https://www.wma.net/policies-post/wma-declaration-of-taipei-on-ethical-considerations-regarding-health-databases-and-biobanks/) - World Medical Association，Adopted October 2002, revised by the 67th WMA General Assembly, Taipei, October 2016 2016。世界医学会《台北宣言》，关于健康数据库和生物样本库的伦理原则：知情同意、撤回、伦理委员会审批和治理安排。🆓 `wma2016taipei`

**健康科学**

- [The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement](https://doi.org/10.1371/journal.pmed.1001885) - Benchimol 等人，PLOS Medicine 2015。RECORD 声明，STROBE 的扩展，规定使用常规收集健康数据（登记、行政数据、电子病历等）的观察性研究应报告什么；13 项清单加逐条解释。CC BY。🆓 `benchimol2015record`
- [The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC5888052/) - Hernan，American Journal of Public Health 2018。Hernán 在《美国公共卫生杂志》的评论：观察性研究应明确说出因果目标，用"目标试验"界定因果问题，按因果目标选择混杂调整。🆓 `hernan2018cword`
- [International Ethical Guidelines for Health-related Research Involving Humans](https://cioms.ch/wp-content/uploads/2017/01/WEB-CIOMS-EthicalGuidelines.pdf) - Council for International Organizations of Medical Sciences，Council for International Organizations of Medical Sciences (CIOMS) 2016。国际医学科学组织理事会（CIOMS）与世界卫生组织合作编写的《涉人健康相关研究国际伦理准则》2016 版，25 条准则，覆盖流行病学研究、社区参与、数据使用、整群随机试验等。官网免费 PDF。🆓 `cioms2016ethical`
- [Cochrane Handbook for Systematic Reviews of Interventions](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) - ，Cochrane 2024。Cochrane 系统综述手册 6.5 版，官网免费在线阅读。本文引用第 1 章（Starting a review）和第 24 章（Including non-randomized studies on intervention effects）。🆓 `higgins2024cochrane`
- [Qualitative research in health care: Assessing quality in qualitative research](https://pmc.ncbi.nlm.nih.gov/articles/PMC1117321/) - Mays 等人，BMJ 2000。BMJ "健康领域的质性研究"系列中的一篇，讲怎样评价质性健康研究的质量：三角互证、反身性、反例分析、受访者核对等。PubMed Central 免费全文。🆓 `mays2000assessing`
- [Consolidated criteria for reporting qualitative research (COREQ): a 32-item checklist for interviews and focus groups (Library entry)](https://www.equator-network.org/reporting-guidelines/coreq/) - EQUATOR Network，网页 2023。EQUATOR 网络报告规范库中 COREQ 的条目页：COREQ 的出处、适用范围，以及侧栏列出的各研究类型主要报告规范（SRQR、COREQ、SQUIRE、CHEERS 等）。🆓 `equatorcoreq`
- [About medRxiv](https://www.medrxiv.org/content/about-medrxiv) - medRxiv，网页。medRxiv（医学和健康科学预印本平台）的介绍页：收稿范围、筛查、预印本不应指导临床和健康行为、发布后不能撤下。🆓 `medrxivabout`

**农业、林业与渔业**

- [Fundamentals of Experimental Design: Guidelines for Designing Successful Experiments](https://doi.org/10.2134/agronj2013.0114) - Casler，Agronomy Journal 2015。Agronomy Journal 上写给农学研究者的试验设计综述，讲重复、随机化、区组、小区大小，含农场试验和给年轻研究者的建议。🆓 `casler2015fundamentals`
- [Enabling reusability of plant phenomic datasets with MIAPPE 1.1](https://doi.org/10.1111/nph.16544) - Papoutsoglou 等人，New Phytologist 2020。植物表型试验元数据标准 MIAPPE 1.1 的介绍论文，开放获取。🆓 `papoutsoglou2020enabling`
- [CGIAR Open and FAIR Data Assets Policy](https://cgspace.cgiar.org/server/api/core/bitstreams/3c39bf16-b35d-4faa-b509-b29d045a9144/content) - CGIAR System Organization，Approved by the System Management Board, effective 16 April 2021 2021。国际农业研究磋商组织（CGIAR）2021 年起生效的开放与 FAIR 数据资产政策。🆓 `cgiar2021fair`
- [The Long Term Experiments](https://www.rothamsted.ac.uk/long-term-experiments) - Rothamsted Research，网页。英国洛桑研究所长期定位试验的介绍页（历史、样品库、电子档案、申请使用方式）。🆓 `rothamstedlte`
- [Editorial Policies](https://www.sciencesocieties.org/publications/journals/author-resources/editorial-policies) - American Society of Agronomy and Crop Science Society of America and Soil Science Society of America，Web page, last updated June 30, 2026。美国农学会、美国作物科学学会、美国土壤科学学会期刊的编辑政策页面（数据政策、预印本、作者伦理声明、科研不端处理）。🆓 `sciencesocietieseditorial`
- [Publications Handbook and Style Manual](https://www.agronomy.org/files/publications/style/style-manual.pdf) - American Society of Agronomy and Crop Science Society of America and Soil Science Society of America，ASA, CSSA, SSSA 2024。三家学会的出版手册与格式手册（2024 年 2 月更新），第 4 章规定试验设计和统计分析怎样报告。🆓 `asa2024style`
- [On-Farm Research: Experimental Approaches, Analytical Frameworks, Case Studies, and Impact](https://doi.org/10.2134/agronj2019.11.0001) - Kyveryga，Agronomy Journal 2019。Agronomy Journal 农场试验专刊的导言，概述农场试验的发展、农民动机和结果分析。🆓 `kyveryga2019onfarm`
- [Reproducibility and external validity of on-farm experimental research in Africa](https://doi.org/10.1017/S0014479720000174) - Kool 等人，Experimental Agriculture 2020。分析 172 篇撒哈拉以南非洲农场试验论文的可重现性和外部效度，开放获取。🆓 `kool2020reproducibility`
- [Don't let spurious accusations of pseudoreplication limit our ability to learn from natural experiments (and other messy kinds of ecological monitoring)](https://doi.org/10.1002/ece3.1782) - Davies 等人，Ecology and Evolution 2015。生态学观点文章，认为伪重复被审稿人用得太教条，附 103 份问卷结果，开放获取。🆓 `davies2015pseudoreplication`
- [Guidelines for the Use of Fishes in Research](https://fisheries.org/policy-media/science-guidelines/guidelines-for-the-use-of-fishes-in-research/) - Use of Fishes in Research Committee (joint committee of the American Fisheries Society, the American Institute of Fishery Research Biologists, and the American Society of Ichthyologists and Herpetologists)，American Fisheries Society 2014。美国渔业学会等三家学会联合委员会编写的鱼类研究使用指南（2014 年版），含统计设计、许可、动物福利。🆓 `afs2014fishes`

**动物科学与兽医学**

- [Guide for the Care and Use of Agricultural Animals in Research and Teaching](https://www.asas.org/docs/default-source/default-document-library/agguide_4th.pdf) - American Dairy Science Association and American Society of Animal Science and Poultry Science Association，American Dairy Science Association, American Society of Animal Science, and Poultry Science Association 2020。美国乳品科学学会、美国动物科学学会、家禽科学学会联合发布的《农业动物研究与教学照料和使用指南》第 4 版（俗称 Ag Guide），CC BY-NC-ND 4.0。key 沿用早期版本发布方"动物科学学会联合会"（FASS）的常用叫法；如需改为 `adsa2020agguide` 请在合并时统一。🆓 `fass2020agguide`
- [The REFLECT statement: Methods and processes of creating reporting guidelines for randomized controlled trials for livestock and food safety](https://www.aasv.org/shap/issues/v18n1/v18n1p18.pdf) - O'Connor 等人，Journal of Swine Health and Production 2010。REFLECT 声明（家畜和食品安全随机对照试验的报告规范）的方法与过程论文，含 22 项清单和术语定义；同时发表在五本期刊。🆓 `oconnor2010reflect`
- [Methods and Processes of Developing the Strengthening the Reporting of Observational Studies in Epidemiology – Veterinary (STROBE-Vet) Statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC5115188/) - Sargeant 等人，Journal of Veterinary Internal Medicine 2016。STROBE-Vet（兽医观察性研究报告规范）的方法与过程论文，开放获取（CC BY-NC）。🆓 `sargeant2016strobevet`
- [Conduct, Oversight, and Ethical Considerations of Clinical Trials in Companion Animals with Cancer: Report of a Workshop on Best Practice Recommendations](https://pmc.ncbi.nlm.nih.gov/articles/PMC4913608/) - Page 等人，Journal of Veterinary Internal Medicine 2016。2014 年 AVMA 总部研讨会的共识报告，伴侣动物肿瘤临床试验的实施、监督和伦理（含主人知情同意的最佳实践），开放获取（CC BY-NC）。🆓 `page2016conduct`
- [Recommendations for Ethical Review of Veterinary Clinical Trials](https://doi.org/10.3389/fvets.2021.715926) - Bertout 等人，Frontiers in Veterinary Science 2021。讨论美国客户自有动物临床研究伦理审查缺口、建议扩大"兽医临床研究委员会"作用的短综述，开放获取。作者有利益冲突声明。🆓 `bertout2021recommendations`
- [One Health](https://www.who.int/news-room/fact-sheets/detail/one-health) - World Health Organization，Fact sheet 2026。世界卫生组织关于"同一健康"（One Health）的情况说明书，页面日期 2026 年 5 月 8 日。🆓 `who2026onehealth`

**教育学**

- [Ethical Guidelines for Educational Research](https://www.bera.ac.uk/publication/ethical-guidelines-for-educational-research-fifth-edition-2024) - British Educational Research Association，网页 2024。英国教育研究协会《教育研究伦理指南》第 5 版（2024），CC BY-NC-ND 4.0 许可，免费下载。🆓 `bera2024ethical`
- [Code of Ethics](https://www.aera.net/Portals/38/docs/About_AERA/CodeOfEthics(1).pdf) - American Educational Research Association，Approved by the AERA Council, February 2011 2011。美国教育研究协会伦理准则，2011 年 2 月理事会批准。🆓 `aera2011code`
- [Standards for Reporting on Empirical Social Science Research in AERA Publications](https://www.aera.net/Portals/38/docs/12ERv35n6_Standard4Report%20.pdf) - American Educational Research Association，Educational Researcher 2006。AERA 2006 年通过的实证社会科学研究报告标准，覆盖定量和定性研究。🆓 `aera2006standards`
- [What Works Clearinghouse Procedures and Standards Handbook, Version 5.0](https://ies.ed.gov/ncee/wwc/Docs/referenceresources/Final_WWC-HandbookVer5_0-0-508.pdf) - What Works Clearinghouse，U.S. Department of Education, Institute of Education Sciences, National Center for Education Evaluation and Regional Assistance 2022。美国有效教育策略信息中心的程序与标准手册第 5.0 版，规定怎样给教育干预研究评级；公有领域。🆓 `wwc2022handbook`
- [Interpreting Effect Sizes of Education Interventions](https://edworkingpapers.com/ai19-10) - Kraft，Annenberg Institute at Brown University 2019。Kraft 关于怎样解读教育干预效应量的工作论文，提出五条准则和基于 747 项随机对照试验的新尺度。🆓 `kraft2019interpreting`
- [Facts Are More Important Than Novelty: Replication in the Education Sciences](https://www.aera.net/Newsroom/Recent-AERA-Research/Facts-Are-More-Important-Than-Novelty-Replication-in-the-Education-Sciences) - Makel 等人，Educational Researcher 2014。Makel 和 Plucker 统计前 100 种教育期刊中重复研究的比例和成功率；只读了 AERA 官网的摘要和新闻稿。🆓 `makel2014facts`
- [Guidance on Recruitment and Retention](https://educationendowmentfoundation.org.uk/public/files/Recruitment_and_retention_guidance_FINAL..pdf) - Education Endowment Foundation，网页 2022。英国教育捐赠基金会写给其资助试验团队的学校招募与保留指南（2022 年 10 月更新）。🆓 `eef2022recruitment`
- [Common Guidelines for Education Research and Development](https://ies.ed.gov/pdf/commonguidelines.pdf) - Institute of Education Sciences and National Science Foundation，U.S. Department of Education and National Science Foundation 2013。美国教育科学研究所和国家科学基金会联合发布的教育研究六种类型及证据要求。🆓 `ies2013common`
- [Design-Based Research: A Decade of Progress in Education Research?](https://auspace.athabascau.ca/handle/2149/3184) - Anderson 等人，Educational Researcher 2012。Anderson 和 Shattuck 对基于设计的研究十年发展的回顾（作者稿）。🆓 `anderson2012design`
- [Celebrating the Launch of the Registry of Efficacy and Effectiveness Studies (REES)](https://ies.ed.gov/learn/blog/celebrating-launch-registry-efficacy-and-effectiveness-studies-rees) - Institute of Education Sciences，IES blog 2018。IES 官网介绍教育因果研究登记平台 REES 上线的博客（2018）。🆓 `ies2018rees`
- [About EdWorkingPapers](https://edworkingpapers.com/about) - Annenberg Institute at Brown University，网页 2026。布朗大学安嫩伯格研究所主办的教育学工作论文系列的介绍页。🆓 `edworkingpapersabout`

**社会学**

- [Code of Ethics](https://www.asanet.org/wp-content/uploads/asa_code_of_ethics-june2018.pdf) - American Sociological Association，American Sociological Association, Washington, DC 2018。美国社会学会伦理准则（2018 年 6 月版），含保密、知情同意、数据共享、署名等条款。🆓 `asa2018code`
- [Statement of Ethical Practice](https://www.britsoc.co.uk/media/24310/bsa_statement_of_ethical_practice.pdf) - British Sociological Association，BSA Publications, Durham 2017。英国社会学会《伦理实践声明》（2017 年版），讲田野研究的同意、把关人、隐蔽研究、保密限度、数据存档。🆓 `bsa2017statement`
- [Replication in Social Science](https://osf.io/preprints/socarxiv/5bck9) - Freese 等人，Annual Review of Sociology 2017。Freese 和 Peterson 在 Annual Review of Sociology 上的综述，从社会学角度讲定量研究的四种"重复"和定性研究的透明问题；读的是作者在 SocArXiv 上的免费稿件。🆓 `freese2017replication`
- [Editorial: Ethnography in the Open Science and Digital Age: New Debates, Dilemmas, and Issues](https://pmc.ncbi.nlm.nih.gov/articles/PMC10978767/) - Jerolmack 等人，Frontiers in Sociology 2024。Frontiers in Sociology 专题社论，概括民族志在开放科学、数字田野、田野伦理上的争论（开放获取，CC BY）。🆓 `jerolmack2024ethnography`
- [About ICPSR; Deposit Data; Citing Data; Data Confidentiality](https://www.icpsr.umich.edu/web/pages/about/) - Inter-university Consortium for Political and Social Research，ICPSR, University of Michigan, web pages 2025。美国校际政治与社会研究联盟（ICPSR）关于机构概况、数据存档、数据引用和数据保密的四个官网页面。🆓 `icpsrdata`
- [Sociological Science: Editorial and Review Process; Reproducibility Policy; Journal Information](https://sociologicalscience.com/for-authors/editorial-and-review-process/) - Society for Sociological Science，Journal 网页 2026。开放获取期刊 Sociological Science 的审稿流程、复现政策（2023 年起对定量论文强制要求复现包）和期刊介绍页面。🆓 `sociologicalsciencepolicy`
- [Submission Guidelines](https://journals.sagepub.com/author-instructions/ASR) - American Sociological Review，Sage Publications 2026。《美国社会学评论》的投稿指南，含论文定位、15,000 词上限、匿名审稿、一稿一投、引用格式和数据集引用要求。🆓 `asrsubmission`
- [Expectations for Promotion to Associate Professor Conferring Tenure](https://www.wesleyan.edu/acaf/Tenure-and-Promotion-Expectations/SOC_2015.pdf) - Department of Sociology, Wesleyan University，Wesleyan University Office of Academic Affairs 2015。美国卫斯理大学社会学系的终身教职晋升要求（2015 年修订），写明主要成果可以是一本书或一系列论文；只代表这一个系。🆓 `wesleyan2015sociology`

**法学**

- [The Rules of Inference](https://gking.harvard.edu/files/gking/files/rules.pdf) - Epstein 等人，University of Chicago Law Review 2002。两位美国学者把社会科学的推断规则介绍给法学界的长文，基于对美国法律评论实证文章的系统阅读，讲选择案件、测量、不确定性和可复现。🆓 `epstein2002rules`
- [Defining and Describing What We Do: Doctrinal Legal Research](https://ojs.deakin.edu.au/index.php/dlr/article/view/70) - Hutchinson 等人，Deakin Law Review 2012。澳大利亚和英国学者讨论"规范研究"（doctrinal research）是什么方法、和其他方法有何异同、为什么要把方法写出来。🆓 `hutchinson2012defining`
- [OSCOLA: The Oxford University Standard for Citation of Legal Authorities](https://www.law.ox.ac.uk/oscola) - ，Hart Publishing 2026。牛津大学法律文献引注标准第 5 版，英国等地常用的法律引注规则，官网免费提供。🆓 `goudkamp2026oscola`
- [Submissions; Data Retention Policy for Authors](https://www.yalelawjournal.org/submissions) - The Yale Law Journal，Web page and PDF。《耶鲁法学杂志》的投稿须知和实证稿件数据保存政策。🆓 `yljsubmissions`
- [Submissions](https://lawreview.uchicago.edu/submissions) - The University of Chicago Law Review，网页。《芝加哥大学法律评论》的投稿须知（收稿平台、加速审阅、撤稿、轻度编辑）。🆓 `uclrsubmissions`
- [Publishing Tips](https://www.lwionline.org/sites/default/files/Publishing-Tips.pdf) - Legal Writing Institute，PDF。美国法律写作学会的投稿指南，讲向美国法律评论同时投稿、加速审阅、接受录用和出版流程。🆓 `lwipublishingtips`
- [Legal Scholarship Network](https://www.ssrn.com/index.cfm/en/lsn/) - SSRN，网页。SSRN 法学研究网络（Legal Scholarship Network）的介绍页。🆓 `ssrnlsn`
- [Researching Case Law: Determining Whether Cases Are Still Good Law](https://library.law.northwestern.edu/cases/updating) - Pritzker Legal Research Center, Northwestern Pritzker School of Law，Research guide。美国西北大学法学院图书馆的研究指南，讲怎样用法律引证工具核查判例是否仍然有效。🆓 `northwesterngoodlaw`
- [Help: Guide to Revised Legislation on legislation.gov.uk](https://www.legislation.gov.uk/help) - The National Archives，网页。英国官方立法网站的帮助页，说明修订版立法多久更新、怎样看有没有尚未并入的修改。🆓 `legislationgovukhelp`
- [Statement of Principles of Ethical Research Practice](https://slsa.ac.uk/images/slsadownloads/SLSA_Board_2021/SLSA_Ethics_Statement_-_September_2021.pdf) - Socio-Legal Studies Association，PDF 2021。英国社会法律研究协会的研究伦理原则（2021 年修订），讲知情同意、把门人、保密的法律边界和数据安全。🆓 `slsa2021ethics`

**政治学**

- [A Guide to Professional Ethics in Political Science](https://www.apsanet.org/Portals/54/APSA%20Files/publications/ethicsguideweb.pdf) - American Political Science Association, Committee on Professional Ethics, Rights and Freedoms，American Political Science Association 2012。美国政治学会职业伦理指南（第二版，2012 年修订），第 III.A 节第 6 条是"数据获取与研究透明"条款的出处。🆓 `apsa2012ethics`
- [Principles and Guidance for Human Subjects Research](https://www.apsanet.org/Portals/54/diversity%20and%20inclusion%20prgms/Ethics/Final_Principles%20with%20Guidance%20with%20intro.pdf) - American Political Science Association，网页 2020。美国政治学会理事会 2020 年 4 月通过的人类受试者研究 12 条原则及说明，涵盖权力、同意、欺骗、伤害、保密、对政治过程的影响。🆓 `apsa2020humansubjects`
- [Data Access and Research Transparency (DA-RT): A Joint Statement by Political Science Journal Editors (Journal Editors' Transparency Statement, JETS)](https://www.dartstatement.org/2014-journal-editors-statement-jets) - DA-RT，网页 2014。2014 年政治学期刊编辑联合发布的《期刊编辑透明声明》（JETS）全文及签署期刊名单、后续争议记录。🆓 `dart2014jets`
- [AJPS Verification Policy](https://ajps.org/ajps-verification-policy/) - American Journal of Political Science，网页 2026。美国政治学刊（AJPS）的核验政策：接收后提交复现材料，期刊核验通过才能发表。🆓 `ajps2026verification`
- [The Qualitative Transparency Deliberations: Insights and Implications](https://eprints.whiterose.ac.uk/id/eprint/158221/) - Jacobs 等人，Perspectives on Politics 2021。定性研究透明度审议（QTD）的总述文章，汇总数百位政治学者对定性研究透明、数据共享和参与者保护的讨论。🆓 `jacobs2021qualitative`
- [Pre-Analysis Plans: An Early Stocktaking](https://researchonline.lse.ac.uk/id/eprint/112747/) - Ofosu 等人，Perspectives on Politics 2023。检查 2011–2016 年在 EGAP 和 AEA 平台登记的 195 份预分析计划写得是否清楚、论文是否照做，并调查研究者的成本和看法。开放获取（CC BY 4.0）。🆓 `ofosu2023preanalysis`
- [Lessons from a Decade of Replications at the Quarterly Journal of Political Science](https://dukespace.lib.duke.edu/items/319e52d7-0932-4d21-89bb-85df233fbcbd) - Eubank，PS: Political Science & Politics 2016。《政治学季刊》（QJPS）复现助理对 2012–2015 年内部复现审查的总结，以及对复现包的具体要求。🆓 `eubank2016lessons`
- [Ethics in Field Experimentation: A Call to Establish New Standards to Protect the Public from Unwanted Manipulation and Real Harms](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720186/) - McDermott 等人，Proceedings of the National Academy of Sciences 2020。PNAS 观点文章，批评在真实选举等社会环境中未经同意的田野实验，主张增加"尊重社会"的伦理原则。🆓 `mcdermott2020ethics`
- [10 Things to Know About Pre-Analysis Plans](https://methods.egap.org/guides/planning/pap_en.html) - Chen 等人，Evidence in Governance and Politics (EGAP)。EGAP（治理与政治证据网络）方法指南，讲预分析计划写什么、为什么写、何时何处登记，附例子。🆓 `egappreanalysis`
- [10 Things to Know About Survey Experiments](https://methods.egap.org/guides/data-collection/survey-experiments_en.html) - Grady，Evidence in Governance and Politics (EGAP)。EGAP 方法指南，介绍调查实验及联合分析、启动、背书、列举、随机化回答等设计和局限。🆓 `egapsurveyexperiments`

**社会与经济地理学**

- [Statement of Professional Ethics](https://aag.org/statement-of-professional-ethics) - American Association of Geographers，网页 2024。美国地理学家协会的职业伦理声明（1998 年通过，2024 年 6 月最近一次修订），含田野、知情同意、地理空间技术与隐私、资金披露等条款。🆓 `aag2024ethics`
- [Code of Practice for the Grants Programme](https://www.rgs.org/in-the-field/grants/guidance-for-society-grant-applicants/code-of-practice-for-the-grants-programme) - Royal Geographical Society (with IBG)，网页。英国皇家地理学会（RGS-IBG）资助项目的行为守则，含东道国伦理审查、当地合作者署名、出行和碳足迹等要求。🆓 `rgsgrantscode`
- [Safe, Responsible and Ethical Research](https://www.rgs.org/exploration/grants/guidance-for-society-grant-applicants/safe-responsible-and-ethical-research/) - Royal Geographical Society (with IBG)，网页。RGS-IBG 给资助申请人的安全、负责和伦理研究说明，含风险评估和伦理评估要求。🆓 `rgssaferesearch`
- [Reproducibility and Replicability: Opportunities and Challenges for Geospatial Research](https://par.nsf.gov/servlets/purl/10292882) - Kedron 等人，International Journal of Geographical Information Science 2021。地理空间研究可复现性与可复制性的综述，讨论设定搜索、预分析计划、保密数据和"换地方能否复制"的问题。🆓 `kedron2021reproducibility`
- [The Uncertain Geographic Context Problem](http://meipokwan.org/Paper/Kwan_UGCoP_2012.pdf) - Kwan，Annals of the Association of American Geographers 2012。提出"不确定的地理背景问题"（UGCoP），并区分它和可塑性面积单元问题；注释中讨论 GPS 数据的隐私保护。🆓 `kwan2012uncertain`
- [The Limits of the Neighborhood Effect: Contextual Uncertainties in Geographic, Environmental Health, and Social Science Research](http://meipokwan.org/Paper/Kwan_2018_AAAG.pdf) - Kwan，Annals of the American Association of Geographers 2018。讨论邻里效应研究中的背景不确定性，定义可塑性面积单元问题的尺度效应和分区效应，以及可塑性时间单元问题。🆓 `kwan2018limits`
- [Ethical Guidelines for Geoprivacy: A Framework for Researchers and Ethics Committees](https://pmc.ncbi.nlm.nih.gov/articles/PMC13092162/) - Malekzadeh 等人，International Journal of Health Geographics 2026。面向研究者和伦理委员会的地理隐私伦理指南，按研究生命周期列出自查问题（开放获取）。🆓 `malekzadeh2026ethical`
- [Reproducible Research and GIScience: An Evaluation Using AGILE Conference Papers](https://pmc.ncbi.nlm.nih.gov/articles/PMC6047504/) - Nust 等人，PeerJ 2018。对 AGILE 会议 32 篇最佳论文提名论文的可复现性评估，附作者问卷和改进建议（开放获取）。🆓 `nust2018reproducible`
- [Positionality Statements in Science](https://pmc.ncbi.nlm.nih.gov/articles/PMC11200055/) - Karhulahti，Open Research Europe 2024。讨论各学科何时适合写立场声明、怎样写的短文（开放获取）。🆓 `karhulahti2024positionality`

**媒体与传播**

- [Internet Research: Ethical Guidelines 3.0](https://aoir.org/reports/ethics3.pdf) - franzke 等人，Association of Internet Researchers 2020。网络研究者协会（AoIR）第三版网络研究伦理指南（IRE 3.0），讨论知情同意、公开与私密、服务条款、去标识化等问题。🆓 `franzke2020internet`
- [Practical Resources for Assessing and Reporting Intercoder Reliability in Content Analysis Research Projects](http://matthewlombard.com/reliability/) - Lombard 等人，Online resource, last updated June 1, 2010 2010。Lombard、Snyder-Duch 和 Bracken 关于内容分析编码者间信度的公开在线指南，是其 2002 年 Human Communication Research 论文的配套资源，给出测试和报告信度的分步建议。🆓 `lombard2010practical`
- [An Agenda for Open Science in Communication](https://doi.org/10.1093/joc/jqz052) - Dienlin 等人，Journal of Communication 2021。传播学开放科学议程，汇总传播学可重复性问题的证据，提出七条建议，并讨论定性研究和常见顾虑。🆓 `dienlin2021agenda`
- [ICA Code of Ethics](https://cdn.ymaws.com/www.icahdq.org/resource/resmgr/governance_documents/ica.code.of.ethics.may2019.pdf) - International Communication Association，Adopted May 2019 2019。国际传播学会（ICA）伦理准则，2019 年 5 月通过，涵盖研究参与者权利、署名、透明与披露、合理使用等。🆓 `ica2019ethics`
- [76th Annual ICA Conference: Conference Submission Guidelines and Conference Submission Types](https://www.icahdq.org/page/conf-submission-guidelines) - International Communication Association，Web pages, accessed via Internet Archive snapshots of 2025-09-05 and 2025-10-02 2025。国际传播学会第 76 届年会（ICA26，2026 年，开普敦）的投稿指南和投稿类型页面，规定截稿、一稿一投、投稿数量限制、篇幅、预注册投稿类型等。🆓 `ica2026conference`
- [Open Scholarship](https://www.icahdq.org/page/OpenScholarship) - International Communication Association，Web page, accessed via Internet Archive snapshot of 2025-09-18 2025。ICA 官网"开放学术"页面，介绍 ICA 对开放科学的立场与争论、开放科学徽章和数据可得性声明要求。🆓 `icaopenscholarship`
- [Journals Frequently Asked Questions](https://www.icahdq.org/page/JournalsFAQ) - International Communication Association，Web page, accessed via Internet Archive snapshot of 2025-09-12 2025。ICA 期刊常见问题页，列出 ICA 的六本期刊和稿件格式（APA 第 7 版）要求。🆓 `icajournalsfaq`
- [Computational Research in the Post-API Age](https://doi.org/10.1080/10584609.2018.1477506) - Freelon，Political Communication 2018。Facebook 关闭公共主页接口后，计算传播研究者怎样权衡网页抓取与平台服务条款的短文。🆓 `freelon2018computational`
- [Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market for Digital Services and amending Directive 2000/31/EC (Digital Services Act)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065) - European Parliament and Council of the European Union，Official Journal of the European Union, L 277, 27 October 2022, p. 1 2022。欧盟《数字服务法》，第 40 条规定超大型平台向经审核的研究者提供数据的义务。🆓 `eu2022dsa`

**语言与文学**

- [LSA Ethics Statement](https://www.lsadc.org/lsa_ethics_statement) - Linguistic Society of America，网页 2019。美国语言学会 2019 年修订的伦理声明，讲对参与者、社区、学生和同行的责任。🆓 `lsa2019ethics`
- [Human Subjects in Linguistic Research](https://www.lsadc.org/human_subjects_in_linguistic_research) - Linguistic Society of America，网页 1992。美国语言学会 1992 年关于语言研究中人类受试者问题的声明，讲和发音人的长期关系、署名意愿。🆓 `lsa1992humansubjects`
- [Resolution Recognizing the Scholarly Merit of Language Documentation](https://lsa.membershipsoftware.org//Files/Advocacy/201001_Resolution_Scholarly_Merit_Lang_Documentation.pdf) - Linguistic Society of America，网页 2010。美国语言学会 2010 年决议，支持把语言记录成果（语法书、词典、语料库等）算作学术贡献。🆓 `lsa2010documentation`
- [Reproducible research in linguistics: A position statement on data citation and attribution in our field](https://doi.org/10.1515/ling-2017-0032) - Berez-Kroeker 等人，Linguistics 2018。约 41 位语言学者的立场声明，讲语言学的可复现研究、数据引用和数据工作的学术承认。🆓 `berezkroeker2018reproducible`
- [The Austin Principles of Data Citation in Linguistics](https://site.uit.no/linguisticsdatacitation/austinprinciples/) - Berez-Kroeker 等人，网页 2018。《奥斯汀语言学数据引用原则》1.0 版，把 FORCE11 数据引用原则落实到语言数据上。🆓 `berezkroeker2018austin`
- [Researcher degrees of freedom in phonetic research](https://doi.org/10.5334/labphon.147) - Roettger，Laboratory Phonology: Journal of the Association for Laboratory Phonology 2019。讨论语音学研究中"研究者自由度"造成的假阳性，以及预注册、透明报告、直接重复等对策。🆓 `roettger2019researcher`
- [Report of the MLA Task Force on Evaluating Scholarship for Tenure and Promotion](https://www.mla.org/content/download/3362/file/taskforcereport0608.pdf) - MLA Task Force on Evaluating Scholarship for Tenure and Promotion，Profession 2007。MLA 终身教职与晋升学术评价工作组报告，基于 2005 年对美国 1,339 个英语和外语系的调查，讨论专著、期刊论文、学术版本和合作研究的评价。🆓 `mla2007evaluating`
- [Guidelines for Evaluating Work in Digital Humanities and Digital Media](https://www.mla.org/About-Us/Governance/Committees/Committee-Listings/Professional-Issues/Committee-on-Information-Technology/Guidelines-for-Evaluating-Work-in-Digital-Humanities-and-Digital-Media) - Modern Language Association, Committee on Information Technology，网页 2012。MLA 关于评价数字人文和数字媒体工作的指南（2012 年修订），含人文学科与计算机领域对会议论文看法的对比。🆓 `mla2012digital`
- [MLA Style Center: In-Text Citations: An Overview; Plagiarism and Academic Dishonesty; Works Cited: A Quick Guide](https://style.mla.org/in-text-citations-overview/) - Modern Language Association，网页。MLA 格式官网的免费页面（依据《MLA 手册》第 9 版），讲文中引注、引用文献列表的"容器"概念和抄袭。🆓 `mlastylecenter`
- [Guidelines for Editors of Scholarly Editions](https://www.mla.org/Resources/Guidelines-and-Data/Reports-and-Professional-Guidelines/Guidelines-for-Editors-of-Scholarly-Editions) - Modern Language Association, Committee on Scholarly Editions，网页。MLA 学术版本委员会给学术版本编者的指南和审读问题清单。🆓 `mlacseguidelines`
- [Literature (Fiction)](https://writingcenter.unc.edu/tips-and-tools/literature/) - The Writing Center, University of North Carolina at Chapel Hill，网页。北卡罗来纳大学教堂山分校写作中心的免费讲义，用九步讲怎样写一篇有论点的文学（小说）分析。🆓 `uncwritinglit`
- [Close reading](https://www.york.ac.uk/english/about/writing-at-york/writing-resources/close-reading/) - Department of English and Related Literature, University of York，网页。英国约克大学英语与相关文学系的写作资源页面，讲细读的定义、做法和常见问题。🆓 `yorkclosereading`

**哲学、伦理与宗教**

- [Guidelines on Writing a Philosophy Paper](https://www.jimpryor.net/teaching/guidelines/writing.html) - Pryor，网页 2012。美国纽约大学哲学教师 Jim Pryor 写给本科生的哲学论文写作指南（页面标注 2012 年 9 月更新）。🆓 `pryor2012writing`
- [Guidelines on Reading Philosophy](https://www.jimpryor.net/teaching/guidelines/reading.html) - Pryor，网页 2006。Jim Pryor 写给本科生的哲学文献阅读指南（知识共享许可，页面标注 2006 年 8 月更新）。🆓 `pryor2006reading`
- [Statement on Best Practices in Journal Publishing](https://www.apaonline.org/page/journalpractices) - American Philosophical Association，网页 2022。美国哲学学会关于期刊出版的最佳实践声明（2022 年 2 月理事会批准），分期刊、作者、审稿人、版权与开放获取四部分。🆓 `apaphil2022journal`
- [Statement on Research](https://www.apaonline.org/page/research) - American Philosophical Association，Proceedings and Addresses of the American Philosophical Association 1996。美国哲学学会 1996 年的《研究声明》，说明哲学研究的形式、发表方式和评价标准。🆓 `apaphil1996research`
- [Code of Conduct](https://www.apaonline.org/page/codeofconduct) - American Philosophical Association，网页 2016。美国哲学学会 2016 年行为准则（职业伦理、反歧视、对学生的责任等）。🆓 `apaphil2016conduct`
- [Insights from the American Philosophical Association's Journal Surveys Project](https://blog.apaonline.org/2024/06/07/insights-from-the-american-philosophical-associations-journal-surveys-project/) - Andrews，网页 2024。美国哲学学会博客文章，分析"期刊调查"项目 2019–2023 年作者自报的审稿时间、意见质量等数据。🆓 `andrews2024journal`
- [Submissions Statistics](https://jhp.wisc.edu/submissions.html) - Journal of the History of Philosophy，网页 2025。《哲学史杂志》官网公布的历年投稿数、接收数、接收率和审稿时间。🆓 `jhp2025statistics`
- [Prolific philosophy authors' preferences regarding scientific collaboration, journal levels, and author role](https://hdl.handle.net/2142/117350) - Chang 等人，iConference 2023 Proceedings 2023。iConference 2023 海报，统计 2011–2020 年哲学期刊最高产 100 位作者的合著情况。🆓 `chang2023prolific`
- [Experimental Philosophy](https://plato.stanford.edu/entries/experimental-philosophy/) - Sytsma 等人，The Stanford Encyclopedia of Philosophy 2026。《斯坦福哲学百科全书》2026 年新版"实验哲学"条目，讲方法、代表性研究和元哲学争论。🆓 `sytsma2026experimental`
- [Reflective Equilibrium](https://plato.stanford.edu/entries/reflective-equilibrium/) - Knight，The Stanford Encyclopedia of Philosophy 2023。《斯坦福哲学百科全书》"反思平衡"条目。🆓 `knight2023reflective`
- [Thought Experiments](https://plato.stanford.edu/entries/thought-experiment/) - Brown 等人，The Stanford Encyclopedia of Philosophy 2023。《斯坦福哲学百科全书》"思想实验"条目。🆓 `brown2023thought`
- [Philosophy and Christian Theology](https://plato.stanford.edu/entries/christiantheology-philosophy/) - Wood，The Stanford Encyclopedia of Philosophy 2021。《斯坦福哲学百科全书》"哲学与基督教神学"条目，讲两者关系的几种历史模式。🆓 `wood2021philosophy`
- [AAR Religious Literacy Guidelines: What U.S. College Graduates Need to Understand about Religion](https://aarweb.org/resource/aar-religious-literacy-guidelines/) - American Academy of Religion，网页 2019。美国宗教学会 2019 年的宗教素养指南，区分宗教学路径和基于信仰等其他路径。🆓 `aar2019literacy`

**艺术**

- [Practice Based Research: A Guide](https://www.creativityandcognition.com/resources/PBR%20Guide-1.1-2006.pdf) - Candy，Creativity & Cognition Studios, University of Technology, Sydney 2006。悉尼科技大学创造力与认知工作室的研究生指南，讲基于实践和实践引导的研究的区别、博士论文结构和反思记录。🆓 `candy2006practice`
- [The Vienna Declaration on Artistic Research](https://aec-music.eu/media/2021/05/viennadeclarationonarfinalversion24june20_20201216163421.pdf) - AEC and CILECT/GEECT and Culture Action Europe and Cumulus and EAAE and ELIA and EPARM and EQ-Arts and MusiQuE and SAR，Policy paper 2020。欧洲十个艺术高等教育和艺术研究相关组织联合署名的政策文件，定义艺术研究并呼吁在 Frascati 手册中把它列为独立类别。🆓 `aec2020vienna`
- [Practice Research – Report 1: What is practice research? and Report 2: How can practice research be shared?](https://doi.org/10.23636/1347) - Bulley 等人，Practice Research Advisory Group UK (PRAG-UK) 2021。英国实践研究顾问组（PRAG-UK）的两份报告，基于对英格兰 62 人的访谈和调查，讲什么是实践研究、怎样分享和保存实践研究成果。CC BY-NC-ND 4.0。🆓 `bulley2021practice`
- [Guidance on submissions (REF 2019/01)](https://2021.ref.ac.uk/media/1447/ref-2019_01-guidance-on-submissions.pdf) - Research Excellence Framework，Research England, Scottish Funding Council, Higher Education Funding Council for Wales, Department for the Economy Northern Ireland 2019。英国 REF 2021 的提交指南，附录 C 给出 REF 对"研究"的定义；附录 B 规定非文字、基于实践成果的文字说明。🆓 `ref2019guidance`
- [Panel criteria and working methods (REF 2019/02)](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf) - Research Excellence Framework，Research England, Scottish Funding Council, Higher Education Funding Council for Wales, Department for the Economy Northern Ireland 2019。REF 2021 的评审组标准和工作方法；Main Panel D（艺术与人文）第 263–269 段讲实践成果怎样提交，第 32、33 评估单元覆盖艺术与设计、音乐与表演艺术。🆓 `ref2019panel`
- [Code of Best Practices in Fair Use for the Visual Arts](https://www.collegeart.org/pdf/fair-use/best-practices-fair-use-visual-arts.pdf) - College Art Association，网页 2015。美国大学艺术协会的视觉艺术合理使用准则，讲写作、教学、创作、博物馆和档案中怎样依据美国版权法的合理使用使用作品。🆓 `caa2015fairuse`
- [Standards for the Practice of Art History](https://www.collegeart.org/standards-and-guidelines/guidelines/art-history-ethics) - College Art Association，网页 2014。美国大学艺术协会的《艺术史实践标准》，讲研究与发表、资料获取、致谢、社区责任、利益冲突。🆓 `caa2014standards`
- [Position Statement on Ethical Considerations](https://www.ethnomusicology.org/page/EthicsStatement) - Society for Ethnomusicology，网页 1998。民族音乐学会 1998 年的伦理声明，讲田野研究、发表和教学中的伦理责任。🆓 `sem1998ethics`
- [Position Statement on Ethnographic Research & Institutional Review Boards](https://www.ethnomusicology.org/page/PS_IRB) - Society for Ethnomusicology，网页 2008。民族音乐学会 2008 年关于民族志研究和美国伦理审查委员会的立场声明。🆓 `sem2008irb`

**研究类型：随机对照试验**

- [CONSORT 2025 explanation and elaboration: updated guideline for reporting randomised trials](https://doi.org/10.1136/bmj-2024-081124) - Hopewell 等人，BMJ 2025。CONSORT 2025 的配套解释文章，逐条讲随机试验报告清单每一项的含义、理由、实证依据和好的写法示例；随机化、分配隐藏、盲法、样本量、意向性分析等部分是本文的主要依据。🆓 `hopewell2025consortee`
- [SPIRIT 2025 statement: updated guideline for protocols of randomised trials](https://doi.org/10.1136/bmj-2024-081477) - Chan 等人，BMJ 2025。SPIRIT 2025 声明，随机试验方案的报告规范（34 项条目加时间安排图），讲方案应包含哪些内容，包括数据监查委员会、期中分析、揭盲规则、知情同意。🆓 `chan2025spirit`
- [Trial registration – International Clinical Trials Registry Platform (ICTRP)](https://www.who.int/tools/clinical-trials-registry-platform/network/trial-registration) - World Health Organization，网页。世界卫生组织国际临床试验注册平台（ICTRP）关于试验登记的官方网页：为什么要登记、去哪里登记（WHO 一级登记库或 ICMJE 认可的登记库）、各国要求不同。🆓 `whotrialregistration`

**研究类型：观察性流行病学研究**

- [Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/) - Hernan 等人，American Journal of Epidemiology 2016。Hernán 和 Robins 讲怎样用大型观察性数据库模拟"目标试验"的方法学文章，详细讲纳入标准、零时刻、宽限期、结局判定等陷阱。🆓 `hernan2016target`
- [Causal Inference: What If](https://miguelhernan.org/whatifbook) - Hernan 等人，Chapman & Hall/CRC 2020。Hernán 和 Robins 的因果推断教材，作者网站免费提供 PDF；第 7、8、9 章分别讲混杂、选择偏倚、测量偏倚，第 3.6 节讲目标试验。🆓 `hernan2020whatif`
- [Observational Studies: Cohort and Case-Control Studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC2998589/) - Song 等人，Plastic and Reconstructive Surgery 2010。面向外科医生的入门文章，讲队列研究和病例对照研究的优缺点、怎样选病例和对照、失访与回忆偏倚。🆓 `song2010observational`
- [Strengthening the Reporting of Observational Studies in Epidemiology–-Nutritional Epidemiology (STROBE-nut): An Extension of the STROBE Statement](https://doi.org/10.1371/journal.pmed.1002036) - Lachat 等人，PLoS Medicine 2016。STROBE 针对营养流行病学的扩展（STROBE-nut），在 STROBE 上加了 24 条建议，讲饮食评估方法、误报、能量调整、验证研究怎样报告。🆓 `lachat2016strobenut`
- [Dietary Assessment Primer](https://epi.grants.cancer.gov/dietary-assessment-primer/) - National Cancer Institute，Epidemiology and Genomics Research Program, Division of Cancer Control and Population Sciences, National Cancer Institute 2025。美国国家癌症研究所的饮食评估入门资料，讲自我报告饮食工具的测量误差类型、对研究结果的影响和误报。🆓 `nci2025dietprimer`
- [Use of Directed Acyclic Graphs (DAGs) to Identify Confounders in Applied Health Research: Review and Recommendations](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128477/) - Tennant 等人，International Journal of Epidemiology 2021。综述 1999—2017 年 234 篇用有向无环图（因果图）挑选混杂因素的健康研究，并提出八条报告和使用建议。🆓 `tennant2021dags`

**研究类型：系统综述与元分析（健康领域）**

- [PROSPERO: International Prospective Register of Systematic Reviews](https://www.crd.york.ac.uk/prospero/) - Centre for Reviews and Dissemination, University of York，网页 2023。PROSPERO 国际前瞻性系统综述登记平台（英国约克大学评价与传播中心管理、英国国家卫生研究院资助）的网站说明页，包括登记目的、收录范围、登记时间要求、不收的综述类型、登记资格自查问题。🆓 `crd2023prospero`
- [GRADE Handbook for Grading Quality of Evidence and Strength of Recommendations](https://gdt.gradepro.org/app/handbook/handbook.html) - ，The GRADE Working Group 2013。GRADE 工作组的《GRADE 手册》（2013 年 10 月更新版），讲怎样用 GRADE 方法给证据质量（现多称"确定性"）分级、怎样形成推荐，包括四个等级的定义、五个降级理由和三个升级理由的解释与例子。免费在线阅读。🆓 `schunemann2013grade`

**研究类型：准实验与因果识别**

- [What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature](https://arxiv.org/abs/2201.01194) - Roth 等人，arXiv:2201.01194 2023。近年双重差分计量方法的综述，按"放松了标准设定的哪条假设"分类，附检查清单和软件包表。🆓 `roth2023trending`
- [Regression Discontinuity Designs: A Guide to Practice](https://www.nber.org/papers/w13039) - Imbens 等人，Journal of Econometrics 2008。断点回归的实操指南：画图、局部线性回归、带宽选择、各类设定检验，末尾有操作步骤总结。🆓 `imbens2008rd`
- [Regression Discontinuity Designs in Economics](https://www.nber.org/papers/w14723) - Lee 等人，Journal of Economic Literature 2010。面向实证研究者的断点回归"用户指南"：什么时候成立（"精确控制"的概念）、怎样估计和画图，第 4.6 节有实施清单。🆓 `lee2010rd`
- [A Practitioner's Guide to Cluster-Robust Inference](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf) - Cameron 等人，Journal of Human Resources 2015。聚类稳健标准误的实用指南：为什么要聚类、在哪一级聚类、聚类太少怎么办、多维聚类。🆓 `cameron2015practitioner`
- [How Much Should We Trust Differences-in-Differences Estimates?](https://www.nber.org/papers/w8841) - Bertrand 等人，Quarterly Journal of Economics 2004。用随机生成的"安慰剂法律"说明，忽视序列相关会让双重差分的标准误严重偏小，并提出几种修正办法。🆓 `bertrand2004trust`
- [Causal Inference: The Remix](https://mixtape.scunning.com/) - Cunningham，网页 2026。Scott Cunningham 的因果推断教材第二版在线版，作者免费公开；讲断点回归、工具变量、双重差分、合成控制等，附 R 和 Stata 代码。🆓 `cunningham2026remix`

**研究类型：田野实验**

- [Using Randomization in Development Economics Research: A Toolkit](https://www.nber.org/papers/t0333) - Duflo 等人，National Bureau of Economic Research 2006。Duflo、Glennerster、Kremer 写的发展经济学随机评估方法手册，覆盖合作伙伴、随机化方式、功效、整群、依从、溢出、流失、推断和外部效度。🆓 `duflo2007toolkit`
- [Power Calculations](https://www.povertyactionlab.org/resource/power-calculations) - Gupta 等人，J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2021。J-PAL 研究资源页，讲功效计算的组成、整群设计、不依从和流失对样本量的影响，以及参数从哪里找。🆓 `jpal2021power`
- [Randomization](https://www.povertyactionlab.org/resource/randomization) - Kopper 等人，J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2023。J-PAL 研究资源页，讲随机化方法、随机化单位、分层、平衡检验和可复现的随机分组代码。🆓 `jpal2023randomization`
- [Ethical Conduct of Randomized Evaluations](https://www.povertyactionlab.org/resource/ethical-conduct-randomized-evaluations) - Feeney 等人，J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2022。J-PAL 研究资源页，按尊重个人、有利、公正三原则讲随机评估的伦理实务（页面自述作者不是伦理学家）。🆓 `jpal2022ethics`
- [Implementation Monitoring](https://www.povertyactionlab.org/resource/implementation-monitoring) - Gibson，J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2021。J-PAL 研究资源页，讲怎样监测干预是否按设计执行，以及流失、依从、溢出、评估驱动效应等威胁的监测方法。🆓 `jpal2021implementation`
- [Data Security Procedures for Researchers](https://www.povertyactionlab.org/resource/data-security-procedures-researchers) - O'Toole 等人，J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2023。J-PAL 研究资源页，讲随机评估中个人数据的最小化收集、去标识、加密和与伙伴共享。🆓 `jpal2023datasecurity`
- [10 Things You Need to Know About Statistical Power](https://methods.egap.org/guides/assessing-designs/power_en.html) - Coppock，EGAP Methods Guides, Evidence in Governance and Politics。EGAP 方法指南"关于统计功效要知道的 10 件事"，含公式、模拟和整群设计的功效。🆓 `egappower`
- [10 Things to Know About Spillovers](https://methods.egap.org/guides/data-collection/spillovers_en.html) - Coppock，EGAP Methods Guides, Evidence in Governance and Politics。EGAP 方法指南"关于溢出要知道的 10 件事"，讲溢出怎样造成偏差、无干扰假设、隔离带和多层设计。🆓 `egapspillovers`
- [10 Things You Need to Know About Cluster Randomization](https://methods.egap.org/guides/data-collection/cluster-randomization_en.html) - Bowers 等人，EGAP Methods Guides, Evidence in Governance and Politics。EGAP 方法指南"关于整群随机要知道的 10 件事"，讲信息损失、有效样本量、聚类标准误和群大小不等的偏差。🆓 `egapclusterrandomization`
- [10 Things You Need to Know About the Local Average Treatment Effect](https://methods.egap.org/guides/research-questions/late_en.html) - van der Windt，EGAP Methods Guides, Evidence in Governance and Politics。EGAP 方法指南"关于局部平均处理效应要知道的 10 件事"，讲不依从、排除性约束、鼓励设计和功效。🆓 `egaplate`
- [10 Conversations that Implementers and Evaluators Need to Have](https://methods.egap.org/guides/implementation/evaluation-conversations_en.html) - Bowers 等人，EGAP Methods Guides, Evidence in Governance and Politics。EGAP 方法指南"实施方和评估者需要进行的 10 次对话"，讲合作评估前要谈清的目标、分工、沟通、结果公开和意外结果。🆓 `egapevaluationconversations`

**研究类型：量表编制与测量研究**

- [Best Practices for Developing and Validating Scales for Health, Social, and Behavioral Research: A Primer](https://pmc.ncbi.nlm.nih.gov/articles/PMC6004510/) - Boateng 等人，Frontiers in Public Health 2018。Boateng 等人写的量表编制入门，按"编题、形成量表、评价量表"三阶段九步骤讲解，每步给定义、常见陷阱和实例。🆓 `boateng2018best`
- [Hidden Invalidity Among 15 Commonly Used Measures in Social and Personality Psychology](https://osf.io/preprints/psyarxiv/7rbfp) - Hussey 等人，Advances in Methods and Practices in Psychological Science 2020。Hussey 和 Hughes 用大规模在线数据检验 15 份常用问卷的结构效度，发现只看内部一致性会掩盖大量问题，并提出"效度操纵"（v-hacking）的概念。🆓 `hussey2020hidden`
- [Measurement Invariance Conventions and Reporting: The State of the Art and Future Directions for Psychological Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/) - Putnick 等人，Developmental Review 2016。Putnick 和 Bornstein 对测量不变性的非技术介绍和文献回顾：四个检验步骤、拟合标准、部分不变性和报告惯例。🆓 `putnick2016measurement`
- [The ITC Guidelines for Translating and Adapting Tests (Second Edition)](https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf) - International Test Commission，International Test Commission, version 2.4 2017。国际测验委员会（International Test Commission）《测验翻译与改编指南》第二版（v2.4），18 条指南分六类，附解释和检查表。🆓 `itc2017guidelines`

**研究类型：实验测量研究**

- [Blind Analysis in Nuclear and Particle Physics](https://inspirehep.net/files/123bf8d8ec8f80e60be89076c65dbdbd) - Klein 等人，Annual Review of Nuclear and Particle Science 2005。两位实验物理学家对核物理和粒子物理中盲分析的综述：实验者偏差的几种形式（含"停止偏差"）、隐藏信号框、隐藏答案、隐藏偏移量、数据预留等方法，以及揭盲后怎么办。🆓 `klein2005blind`
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/mpc/mpc.htm) - NIST/SEMATECH，National Institute of Standards and Technology 2012。美国国家标准与技术研究院（NIST）和 SEMATECH 合编的在线统计方法手册，第 2 章"测量过程表征"讲核查标准、控制图、校准和不确定度分析（A 类、B 类、预算表、扩展不确定度）。🆓 `nist2012ehandbook`
- [Review of Particle Physics: Introduction](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-rpp-intro.pdf) - Navas 等人，Physical Review D 2024。粒子数据组《粒子物理评论》2024 年版的引言，第 5 节讲怎样对多个测量取加权平均、用卡方检查一致性、用标度因子放大误差，以及数值修约规则。🆓 `pdg2024intro`

**研究类型：实验台实验（湿实验）**

- [What exactly is `N' in cell culture and animal experiments?](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2005282) - Lazic 等人，PLOS Biology 2018。用生物单位、实验单位、观察单位三个概念和三条标准，讲清细胞培养和动物实验里 n 到底该怎么算。🆓 `lazic2018what`
- [Error bars in experimental biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/) - Cumming 等人，Journal of Cell Biology 2007。写给实验生物学家的八条误差线规则：图注写清 n 和误差线类型，重复测量不能算 n，代表性实验 n = 1。🆓 `cumming2007error`
- [Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128) - Weissgerber 等人，PLOS Biology 2015。系统回顾 703 篇生理学论文的作图方式，主张小样本连续数据画出全部数据点，而不是只画柱状图加误差线。🆓 `weissgerber2015beyond`
- [What's in a picture? The temptation of image manipulation](https://pmc.ncbi.nlm.nih.gov/articles/PMC2172141/) - Rossner 等人，Journal of Cell Biology 2004。《细胞生物学杂志》编辑用示例图讲解印迹、凝胶和显微图像哪些处理可以接受、哪些属于不当修改。🆓 `rossner2004what`

**研究类型：临床前动物研究**

- [Threats to Validity in the Design and Conduct of Preclinical Efficacy Studies: A Systematic Review of Guidelines for In Vivo Animal Experiments](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1001489) - Henderson 等人，PLoS Medicine 2013。对 26 份临床前动物有效性研究设计指南的系统综述，把 55 条建议按内部、构念、外部效度威胁分类。开放获取。🆓 `henderson2013threats`
- [Survey of the Quality of Experimental Design, Statistical Analysis and Reporting of Research Using Animals](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0007824) - Kilkenny 等人，PLoS ONE 2009。英国 NC3Rs 资助的调查，评估英美公共资助机构 271 篇大鼠、小鼠、非人灵长类研究论文的设计、统计和报告质量。开放获取。🆓 `kilkenny2009survey`
- [Reproducibility of preclinical animal research improves with heterogeneity of study samples](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2003693) - Voelkl 等人，PLoS Biology 2018。基于 CAMARADES 数据库中 440 项卒中、心肌梗死、乳腺癌动物研究的模拟，比较单实验室和多实验室设计估计效应量的准确度。开放获取。🆓 `voelkl2018reproducibility`
- [The Experimental Design Assistant](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2003779) - Percie du Sert 等人，PLoS Biology 2017。介绍英国 NC3Rs 的免费在线工具"实验设计助手"（Experimental Design Assistant，EDA），可做样本量计算、区组随机和盲法安排。开放获取；作者都参与了工具开发。工具网址 https://eda.nc3rs.org.uk 。🆓 `perciedusert2017experimental`
- [animalstudyregistry.org: Welcome](https://www.animalstudyregistry.org/asr_web/index.action) - German Centre for the Protection of Laboratory Animals (Bf3R), German Federal Institute for Risk Assessment，网页。德国联邦风险评估研究所（BfR）下属德国实验动物保护中心（Bf3R）运营的动物研究预注册平台首页。2026-10-06 读取。🆓 `animalstudyregistry`

**研究类型：野外观测研究**

- [Preparations for Water Sampling](https://doi.org/10.3133/tm9A1) - U.S. Geological Survey，网页 2018。美国地质调查局《水质数据采集国家野外手册》A1 章，讲采样前的准备：选点、准入许可、记录、工作计划、质量保证计划、数据管理计划、安全（作业危害分析）。是 USGS 对本局水质野外人员的规程。🆓 `usgs2018nfmprep`
- [Guidelines for Field-Measured Water-Quality Properties](https://doi.org/10.3133/tm9A6.0) - U.S. Geological Survey，网页 2023。同一手册的 A6.0 章，讲水温、溶解氧、电导率、pH 等现场指标的测量、仪器校准和记录规范（仪器日志、不用铅笔、改错划线签名等）。🆓 `usgs2023nfmfield`
- [A protocol for data exploration to avoid common statistical problems](https://doi.org/10.1111/j.2041-210X.2009.00001.x) - Zuur 等人，Methods in Ecology and Evolution 2010。写给生态学者的数据探索八步流程（离群值、方差齐性、共线性、观测独立性等）。本文只用了第 8 步"观测是否独立"。🆓 `zuur2010protocol`
- [Methods to account for spatial autocorrelation in the analysis of species distributional data: a review](https://doi.org/10.1111/j.2007.0906-7590.05171.x) - Dormann 等人，Ecography 2007。生态学里空间自相关的成因、后果、检查方法（相关图、半变异函数）和处理方法综述。🆓 `dormann2007spatial`

**研究类型：田间试验**

- [A tutorial on the statistical analysis of factorial experiments with qualitative and quantitative treatment factor levels](https://doi.org/10.1111/jac.12267) - Piepho 等人，Journal of Agronomy and Crop Science 2018。用真实田间试验讲析因、裂区、定量处理和重复测量数据的混合模型分析的教程，附 SAS 和 R 代码；CC BY 开放获取。🆓 `piepho2018tutorial`
- [The analysis of crop cultivar breeding and evaluation trials: an overview of current mixed model approaches](https://doi.org/10.1017/S0021859605005587) - Smith 等人，The Journal of Agricultural Science 2005。该刊百年综述，概述多环境品种试验的线性混合模型分析方法（随机品种效应、一阶段与两阶段分析等）。🆓 `smith2005analysis`
- [Statistics in a Horticultural Journal: Problems and Solutions](https://doi.org/10.21273/JASHS03747-16) - Kramer 等人，Journal of the American Society for Horticultural Science 2016。检查美国园艺学会会刊 2014 年至 2015 年第 1 期共 86 篇论文的统计问题，分类列出常见错误和改进建议；CC BY-NC-ND 开放获取。🆓 `kramer2016statistics`
- [On-Farm Experimentation to transform global agriculture](https://doi.org/10.1038/s43016-021-00424-4) - Lacoste 等人，Nature Food 2022。多国学者的观点文章，提出以农民为中心、在整块田尺度上做的"农场实验"（On-Farm Experimentation），并讨论小区试验和统计显著性对农民的局限。🆓 `lacoste2022onfarm`

**研究类型：合成与表征研究**

- [On the Topic of Substrate Scope](https://doi.org/10.1021/acs.orglett.2c03246) - Kozlowski，Organic Letters 2022。《Organic Letters》主编 2022 年社论，讨论方法学快报的底物范围该多大、怎样挑选，以及失败底物怎样报告。🆓 `kozlowski2022substrate`
- [Standardizing Substrate Selection: A Strategy toward Unbiased Evaluation of Reaction Generality](https://doi.org/10.1021/acscentsci.3c01638) - Rana 等人，ACS Central Science 2024。明斯特大学 Glorius 课题组的研究文章，指出底物范围表中的选择偏倚和报告偏倚，提出按化学空间标准化挑选底物的方法。🆓 `rana2024standardizing`
- [Improving reproducibility through condition-based sensitivity assessments: application, advancement and prospect](https://doi.org/10.1039/d4sc03017f) - Schafer 等人，Chemical Science 2024。Glorius 课题组的观点文章，总结"灵敏度筛查"（一次只改一个反应条件看产率变化）的用法和各子领域应考察的条件，讨论可重复性。🆓 `schafer2024sensitivity`
- [Stirring the Debate: How Mixing Influences Reproducibility and Efficiency in Synthetic Organic Chemistry](https://doi.org/10.1021/acscentsci.5c01825) - Schuurmans 等人，ACS Central Science 2026。讨论搅拌和混合怎样影响有机合成的可重复性、效率和安全的观点文章，建议论文报告搅拌条件、容器形状和加料方式。🆓 `schuurmans2026stirring`
- [A Return to the Logic-First Spirit of Corey's Retrosynthetic Analysis, Now Implemented in Modern Data-Driven CASP](https://doi.org/10.1021/acscentsci.6c00702) - Kabeshov 等人，ACS Central Science 2026。阿斯利康研究人员的评论文章，用通俗的话解释逆合成分析"先定拆分策略、再定具体试剂"的思路，以及计算机辅助合成规划和化学家判断的分工。🆓 `kabeshov2026retrosynthesis`

**研究类型：档案研究**

- [Using Archives: A Guide to Effective Research](https://www2.archivists.org/usingarchives) - Schmidt，Society of American Archivists 2016。美国档案工作者协会（SAA）官网免费指南，讲档案馆和图书馆的区别、怎样找档案馆、远程申请、计划到访、阅览室规则、版权与受限材料、未整理收藏，附带注释的检索指南样例。🆓 `schmidt2016using`
- [Guidelines for Primary Source Literacy](https://www2.archivists.org/sites/all/files/Guidelines%20for%20Primary%20Souce%20Literacy_AsApproved062018_1.pdf) - SAA-ACRL/RBMS Joint Task Force on the Development of Guidelines for Primary Source Literacy，Society of American Archivists and Association of College and Research Libraries 2018。SAA 与 ACRL/RBMS 联合工作组制定的《一手资料素养指南》，列出提问、查找、阅读、评估、使用一手资料所需的能力，附词汇表（沉默、中介、真实性等）。🆓 `saaacrl2018primary`
- [Start Here: Help with Your Research](https://www.nationalarchives.gov.uk/help-with-your-research/start-here/) - The National Archives (UK)，网页。英国国家档案馆官网的研究入门栏目，讲档案和图书馆的区别、怎样准备查档、哪些记录在网上、哪些不在。🆓 `tnastarthere`
- [Getting Started Overview](https://www.archives.gov/research/start) - National Archives and Records Administration，网页。美国国家档案与记录管理局（NARA）官网研究入门页面，给出查档四步和"联邦记录只有 1%–3% 永久保存"的说明。🆓 `naragettingstarted`

**研究类型：口述历史**

- [OHA Archives Principles and Best Practices](https://oralhistory.org/archives-principles-and-best-practices/) - Oral History Association，Oral History Association 网页 2019。美国口述历史协会 2019 年通过的存档最佳实践，是其 2018 年《原则与最佳实践》的附录，讲接收、元数据、保存、查阅、合作、所有权和权利管理。🆓 `oha2019archiving`
- [Workshop on the Web: Introduction to Oral History](https://www.baylor.edu/content/services/document.php/66420.pdf) - Baylor University Institute for Oral History，Baylor University Institute for Oral History website (series of one-page PDFs) 2012。美国贝勒大学口述历史研究所的网上入门工作坊讲义，每个主题一页：定义、规划、伦理关系、法律文件、录音设备、选题、选受访者、提纲、提问、访谈现场、保存、索引、转录、评估与引用、面向公众。🆓 `baylor2012introduction`
- [Is Your Oral History Legal and Ethical? Ethical and Legal Guidance](https://www.ohs.org.uk/advice/ethical-and-legal/) - Oral History Society，Oral History Society 网页 2019。英国口述历史学会的法律与伦理指南，按访谈流程（准备、第一次接触、访谈中、访谈后、存档）讲英国法律下的同意、版权、数据保护和存档要求。🆓 `ohs2019legal`
- [Looking After Yourself](https://ohs.org.uk/looking-after-yourself/) - Oral History Society，Oral History Society 网页 2026。英国口述历史学会关于访谈者自我照顾的网页：日程安排、人身安全、情绪支持，以及转录和编目人员的休息。🆓 `ohs2026wellbeing`
- [Major Legal Challenges Facing Oral History in the Digital Age](https://ohda.matrix.msu.edu/2012/06/major-legal-challenges/) - Neuenschwander，Oral History in the Digital Age 2014。美国法律下口述历史的主要法律问题：授权书的用途条款、波士顿学院"贝尔法斯特项目"传票案、诽谤和隐私侵权、版权与知识共享许可。🆓 `neuenschwander2014legal`
- [Making Sense of Oral History](https://historymatters.gmu.edu/mse/oral/oral.pdf) - Shopes，History Matters: The U.S. Survey Course on the Web, George Mason University 2002。美国口述历史协会前会长 Linda Shopes 为乔治·梅森大学 History Matters 网站写的指南，讲怎样把口述访谈当历史证据来读：讲述者的可靠性、和其他证据对照、记忆的偏差与意义。🆓 `shopes2002making`

**研究类型：考古发掘与野外调查**

- [Standard and Universal Guidance for Archaeological Field Evaluation](https://www.archaeologists.net/sites/default/files/2024-11/CIfA-Standard-Field-Evaluation_2023.pdf) - Chartered Institute for Archaeologists，网页 2023。英国特许考古学家协会 2023 年 12 月发布的考古野外评估标准和通用指南，讲先非侵入后侵入、项目设计书和评估报告的内容。🆓 `cifa2023evaluation`
- [Standard and Guidance for the Creation, Compilation, Transfer and Deposition of Archaeological Archives](https://www.archaeologists.net/sites/default/files/2023-11/CIfA-SandG-Archaeological-Archives-2020.pdf) - Chartered Institute for Archaeologists，网页 2020。英国特许考古学家协会的考古档案标准和指南（2014 年首发，2020 年更新），讲档案的定义、开工前的归档计划、记录和出土物处理、移交和所有权；针对英国和马恩岛。🆓 `cifa2020archives`
- [Standard and Guidance for Archaeological Geophysical Survey](https://www.archaeologists.net/sites/default/files/2023-11/CIfA-SandG-Geophysical-Survey-2020.pdf) - Chartered Institute for Archaeologists，网页 2020。英国特许考古学家协会的考古地球物理勘探标准和指南（2014 年首发，2020 年小幅更新），讲物探的定义、方法、许可和报告内容。🆓 `cifa2020geophysics`
- [Management of Research Projects in the Historic Environment: The MoRPHE Project Managers' Guide](https://historicengland.org.uk/images-books/publications/morphe-project-managers-guide/) - Lee，Historic England 2015。英格兰历史遗产局的研究项目管理指南（MoRPHE），讲项目阶段、检查点、风险日志、档案和传播；该局资助的项目必须遵循。🆓 `historicengland2015morphe`
- [Principles of Archaeological Stratigraphy](https://harrismatrix.com/download/) - Harris，Academic Press 1989。Edward Harris 的《考古地层学原理》第 2 版，哈里斯矩阵的出处，讲地层单位、叠压定律、平面图、残留物和渗入物、现场记录流程。🆓 `harris1989principles`
- [Archeology and Historic Preservation: Secretary of the Interior's Standards and Guidelines](https://www.nps.gov/subjects/historicpreservation/upload/standards-guidelines-archeology-historic-preservation.pdf) - U.S. Department of the Interior, National Park Service，Federal Register 48(190): 44716–44742 1983。美国内政部长的考古与历史保护标准和指南（1983 年《联邦公报》第 48 卷第 190 期），本文只用"考古记录"标准和指南部分：研究设计、野外记录、报告、保管。🆓 `nps1983standards`

**研究类型：规范法学研究**

- [The Doctrinal Method: Incorporating Interdisciplinary Methods in Reforming the Law](https://eprints.qut.edu.au/93564/3/93564.pdf) - Hutchinson，Erasmus Law Review 2015。澳大利亚学者 Hutchinson 考察澳大利亚法学博士论文、32 篇 2013 年刑法改革期刊文章和法律改革委员会报告，讨论改革导向的规范研究怎样吸收统计、比较法和社会科学证据。🆓 `hutchinson2015doctrinal`
- [Choosing a Successful Paper Topic](https://www.law.georgetown.edu/wp-content/uploads/2021/04/Handout_3-Kaplan_Woods_Choosing_a_Successful_Paper_Topic.pdf) - Uhlig 等人，The Writing Center at Georgetown University Law Center, handout 2020。美国乔治城大学法学院写作中心讲义，讲法学学术论文怎样选题、缩小题目、做"抢先检查"。🆓 `georgetown2020topic`
- [Developing a Thesis Statement](https://www.law.georgetown.edu/wp-content/uploads/2018/11/Updated-Developing-a-Thesis-Statement-Handout.pdf) - Lambert 等人，The Writing Center at Georgetown University Law Center, handout 2018。美国乔治城大学法学院写作中心讲义，讲法学论文的论点（thesis）是什么、几类论证角度和示例。🆓 `georgetown2018thesis`
- [You Have Your Scholarly Paper Topic, Now \ldots Get the Research Done](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2026/10/You-Have-Your-Scholarly-Paper-Topic-Now-Get-the-Research-Done_Kelsey-Handschuh-2026-Revisions_FINAL-1.pdf) - Klein 等人，The Writing Center at Georgetown Law, handout 2026。美国乔治城大学法学院写作中心讲义，讲学术论文的检索策略、检索日志、抢先检查、二手和一手资料的检索、什么时候停止检索。🆓 `georgetown2026research`
- [Using Cases in Legal Analysis: Methods and Examples](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2025/08/Using_Cases_in_Legal_Analysis_Methods_and_ExamplesFCD.pdf) - Hsieh 等人，The Writing Center at Georgetown University Law Center, handout 2025。美国乔治城大学法学院写作中心讲义，讲判例摘要（case brief）的栏目，以及用判例解释制定法、综合规则、做普通法分析和识别趋势的方法。🆓 `georgetown2025cases`
- [How to Craft an Effective Case Comparison](https://www.law.georgetown.edu/wp-content/uploads/2018/07/How-to-Craft-an-Effective-Case-Comparison.pdf) - Djandji，The Writing Center at Georgetown Law, handout 2017。美国乔治城大学法学院写作中心讲义，讲类比和区分判例、什么差别在法律上有意义、"错误否定"和反例。🆓 `georgetown2017comparison`
- [Checklist for Scholarly Writing](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2026/10/Checklist-for-Scholarly-Writing_fcd.pdf) - Kotter，The Writing Center at Georgetown Law, handout 2026。美国乔治城大学法学院写作中心的法学学术写作检查清单（论点、结构、分析、脚注、文风）。🆓 `georgetown2026checklist`
- [A Guide to Reading, Interpreting and Applying Statutes](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2026/08/A-Guide-to-Reading-Interpreting-and-Applying-Statutes.pdf) - Clark 等人，The Writing Center at Georgetown Law, handout 2026。美国乔治城大学法学院写作中心讲义，讲读美国制定法的准备步骤、解释工具和解释理论。🆓 `georgetown2026statutes`
- [Statutory Interpretation: Theories, Tools, and Trends](https://www.congress.gov/crs-product/R45153) - Brannon，Congressional Research Service 2023。美国国会研究服务部报告，系统介绍美国联邦法院解释制定法的两大理论（目的主义、文本主义）和五类工具。🆓 `brannon2023statutory`
- [Researching Case Law](https://library.law.northwestern.edu/cases/overview) - Pritzker Legal Research Center, Northwestern Pritzker School of Law，Research guide 2026。美国西北大学普利兹克法学院法律研究中心的判例检索指南：记录检索过程、"一个好判例"法、怎样判断查全。🆓 `northwesterncaselaw`
- [Wex Legal Dictionary and Encyclopedia](https://www.law.cornell.edu/wex) - Legal Information Institute, Cornell Law School，Online legal dictionary 2026。美国康奈尔大学法学院法律信息研究所的免费法律词典 Wex，用来给判决理由、附带意见、区分、先例、大陆法系等术语下简明定义。🆓 `liiwex`

**研究类型：哲学论证研究**

- [Philosophical Terms and Methods](https://www.jimpryor.net/teaching/vocab/index.html) - Pryor，网页 2025。Jim Pryor 写给入门哲学课学生的讲义《哲学术语与方法》，讲有效、可靠、隐含前提、窃取论题、举证责任、宽容原则、反例和思想实验；以知识共享许可免费发布，三页页脚日期 2025-08-24。`src/pryor2025terms.txt` 是三页正文按 arguments、method、definitions 顺序拼接。🆓 `pryor2025terms`
- [Analysis](https://plato.stanford.edu/entries/analysis/) - Beaney 等人，The Stanford Encyclopedia of Philosophy 2024。《斯坦福哲学百科全书》"分析"条目：哲学中各种"分析"方法的历史，包括概念分析和它的局限。🆓 `beaney2024analysis`
- [Informal Logic](https://plato.stanford.edu/entries/logic-informal/) - Groarke，The Stanford Encyclopedia of Philosophy 2026。《斯坦福哲学百科全书》"非形式逻辑"条目：怎样把真实论证标准化（列出前提和结论、补隐含前提、宽容原则），以及评价论证的标准。🆓 `groarke2026informal`
- [Argument and Argumentation](https://plato.stanford.edu/entries/argument/) - Dutilh Novaes，The Stanford Encyclopedia of Philosophy 2021。《斯坦福哲学百科全书》"论证与论辩"条目：论证的类型（演绎、归纳、溯因、类比），以及论辩应当对抗还是合作的讨论。🆓 `dutilhnovaes2021argument`
- [Intuition](https://plato.stanford.edu/entries/intuition/) - Pust，The Stanford Encyclopedia of Philosophy 2024。《斯坦福哲学百科全书》"直觉"条目：直觉在哲学中的证据作用（案例法）、对它的质疑和辩护，以及实验哲学的相关结果。🆓 `pust2024intuition`

**研究类型：过程追踪与比较案例研究**

- [Understanding Process Tracing](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/183A057AD6A36783E678CB37440346D1/S1049096511001429a.pdf/div-class-title-understanding-process-tracing-div.pdf) - Collier，PS: Political Science & Politics 2011。PS 期刊"教师"栏目的教学文章，用福尔摩斯故事演示过程追踪的四种检验（风中稻草、环检验、冒烟的枪、双重决定性）。🆓 `collier2011understanding`
- [Process Tracing: From Philosophical Roots to Best Practices](https://web.archive.org/web/20170816174541/http://summit.sfu.ca/system/files/iritems1/14884/SimonsWorkingPaper21.pdf) - Bennett 等人，School for International Studies, Simon Fraser University 2012。Bennett & Checkel 主编 Process Tracing in the Social Sciences（剑桥大学出版社，2015）第 1 章的工作论文版：过程追踪的定义、哲学基础、四种检验和"好的过程追踪"的十条标准。🆓 `bennett2012process`
- [Case Selection Techniques in Case Study Research: A Menu of Qualitative and Quantitative Options](https://web.archive.org/web/2016/http://blogs.bu.edu/jgerring/files/2013/06/CaseSelection.pdf) - Seawright 等人，Political Research Quarterly 2008。七种为案例研究挑选案例的方式（典型、多样、极端、偏离、有影响力、最相似、最不同），以及怎样借助大样本数据来选。🆓 `seawright2008case`
- [What Is a Case Study and What Is It Good For?](https://web.archive.org/web/2016/http://blogs.bu.edu/jgerring/files/2013/06/CasestudyAPSR.pdf) - Gerring，American Political Science Review 2004。给"案例研究"下定义，并列出案例研究相对于跨案例研究的七种长处和短处。🆓 `gerring2004case`
- [How the Cases You Choose Affect the Answers You Get: Selection Bias in Comparative Politics](https://escholarship.org/uc/item/9r45g86c) - Geddes，Institute of Governmental Studies, University of California, Berkeley 1990。用比较政治学的实例说明"按因变量选案例"（只挑结果相同的案例）会得出什么错误结论。工作论文版；正式版发表于 Political Analysis 2 (1990): 131–150。🆓 `geddes1990cases`

**研究类型：空间分析研究**

- [Geographic Data Science with Python](https://geographicdata.science/book/intro.html) - Rey 等人，CRC Press 2023。空间数据科学教材，作者免费公开在线全文。本任务用了 Spatial Weights、Choropleth Mapping、Global Spatial Autocorrelation、Spatial Regression 四章：空间权重的定义和常见问题、分级统计地图的分级和配色、莫兰指数、普通回归在空间数据上的问题和空间回归入门。🆓 `rey2023geographic`
- [Spatial Data Science: With Applications in R](https://r-spatial.org/book/) - Pebesma 等人，Chapman and Hall/CRC 2023。R 语言空间数据工具包主要开发者写的教材，作者免费公开在线全文。本任务用了第 2 章（坐标、大地基准、投影、坐标顺序）和第 5 章（属性属于点还是区域、空间聚合、广延量和强度量、面积加权插值）。🆓 `pebesma2023spatial`
- [Global Spatial Autocorrelation (1): Visualizing Spatial Autocorrelation](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html) - Anselin，GeoDa Workbook, Center for Spatial Data Science, University of Chicago 2020。GeoDa 软件官方免费教程中讲全局空间自相关的一章：莫兰指数、莫兰散点图、置换检验和伪 p 值、随机种子与复现。🆓 `anselin2020global`
- [Practical Reproducibility in Geography and Geosciences](https://doi.org/10.1080/24694452.2020.1806028) - Nust 等人，Annals of the American Association of Geographers 2021。地理学和地球科学的计算可复现性实务：脚本化流程、软件环境与版本锁定、研究材料包、在线地理服务、图形界面和闭源软件、敏感数据与模拟数据。🆓 `nust2021practical`
- [The misuse of colour in science communication](https://doi.org/10.1038/s41467-020-19160-7) - Crameri 等人，Nature Communications 2020。开放获取（CC BY 4.0）的科学配色指南：彩虹色和红绿配色的问题、色觉障碍、感知均匀配色和免费配色来源（含 ColorBrewer）。🆓 `crameri2020misuse`
- [Ensuring Confidentiality of Geocoded Health Data: Assessing Geographic Masking Strategies for Individual-Level Data](https://doi.org/10.1155/2014/567049) - Zandbergen，Advances in Medicine 2014。开放获取（CC BY）综述：地址地理编码的误差、反向地理编码导致的重新识别风险、空间汇总的代价、各种地理掩蔽方法及其对空间分析的影响。🆓 `zandbergen2014ensuring`

**研究类型：文本细读与文学论证**

- [A Brief Guide to Writing the English Paper](https://writingproject.fas.harvard.edu/files/hwp/files/bg_writing_english.pdf) - Syba，Harvard College Writing Center, Brief Guide Series 2008。哈佛学院写作中心的英文（文学）论文简明指南：细读的归纳法、常见论文类型（理论框架、历史框架、比较等）、两个从细读到论点的完整示例、写作惯例（避免复述情节、叙述者不等于作者、大段引文的用法）。🆓 `syba2008englishpaper`
- [How to Do a Close Reading](https://writingcenter.fas.harvard.edu/pages/how-do-close-reading) - Kain，Harvard College Writing Center 1998。哈佛学院写作中心的经典短文，以一段 Loren Eiseley 散文为例，演示批注、找模式、问"怎样"和"为什么"、从观察归纳出阐释。🆓 `kain1998closereading`
- [Thesis](https://writingcenter.fas.harvard.edu/thesis) - Harvard College Writing Center，Harvard College Writing Center, Strategies for Essay Writing n.d.。哈佛学院写作中心讲论点的网页：好论点要可争辩、范围合适；描述性论点、过宽论点的例子；自查论点的五个问题。🆓 `harvardwcthesis`
- [Counterargument](https://writingcenter.fas.harvard.edu/counterargument) - Harvard College Writing Center，Harvard College Writing Center, Strategies for Essay Writing n.d.。哈佛学院写作中心讲反方论证的网页：反方论证的类型、回应的方式、在文中放在哪里。🆓 `harvardwccounterargument`
- [Quotations](https://writingcenter.unc.edu/tips-and-tools/quotations/) - The Writing Center, University of North Carolina at Chapel Hill，UNC Writing Center Tips and Tools handout n.d.。北卡罗来纳大学教堂山分校写作中心讲引文的讲义：什么时候引、引文前后怎样交代语境和意义、怎样嵌入句子、引多少、大段引文的用法、避免断章取义。🆓 `uncwritingquotations`
- [Ways of Reading a Translation](https://www.york.ac.uk/english/about/writing-at-york/writing-resources/ways-of-reading-translation/) - Asciuto，Department of English and Related Literature, University of York, Writing at York resources 2018。英国约克大学英语系的写作资源页面，讲怎样细读译本：优先用原文对照版、比较不同译本、引用时写明译者、把译文用词看作译者的选择。🆓 `asciuto2018translation`

**研究类型：语言记录与语言学田野调查**

- [The Leipzig Glossing Rules: Conventions for Interlinear Morpheme-by-Morpheme Glosses](https://www.eva.mpg.de/lingua/pdf/Glossing-Rules.pdf) - Comrie 等人，Department of Linguistics, Max Planck Institute for Evolutionary Anthropology, and Department of Linguistics, University of Leipzig 2015。语言学行间注释（逐词素注释）的通行格式约定，十条规则加缩写表。🆓 `leipzig2015glossing`
- [Deposit (Depositing Material with PARADISEC; Catalog Structure & File Naming; File Formats; Metadata; Access Conditions; Do You Own Your Records?)](https://www.paradisec.org.au/deposit/) - PARADISEC，Pacific And Regional Archive for Digital Sources in Endangered Cultures 网页 2026。澳大利亚语言档案馆 PARADISEC 给存档人的指南：存档流程、文件命名、文件格式、元数据字段、访问条件、版权归属。🆓 `paradisecdeposit`
- [Seven Dimensions of Portability for Language Documentation and Description](https://arxiv.org/abs/cs/0204020) - Bird 等人，arXiv:cs/0204020 2002。讨论数字化语言记录怎样在内容、格式、发现、访问、引用、保存、权利七个方面做到长期可用，并给出最佳做法建议。🆓 `bird2002portability`
- [Research Models, Community Engagement, and Linguistic Fieldwork: Reflections on Working within Canadian Indigenous Communities](http://hdl.handle.net/10125/4423) - Czaykowska-Higgins，Language Documentation & Conservation 2009。比较语言田野工作的几种研究模式，讨论在加拿大原住民社区做合作研究时怎样建立关系、分配角色。🆓 `czaykowskahiggins2009research`
- [Public Access to Research Data in Language Documentation: Challenges and Possible Strategies](http://hdl.handle.net/10125/24901) - Seyfeddinipur 等人，Language Documentation & Conservation 2019。30 位作者合写，讨论语言记录数据的同意、版权、访问级别、封存期和档案馆的作用，并给出策略建议。🆓 `seyfeddinipur2019public`
- [Meeting the Transcription Challenge](http://hdl.handle.net/10125/24806) - Himmelmann，Reflections on Language Documentation 20 Years after Himmelmann 1998 2018。讨论语言记录中的转写：耗时、转写包含解释、母语者改稿、转写对社区语言生态的影响。🆓 `himmelmann2018transcription`
- [Reflections on the Scope of Language Documentation](http://hdl.handle.net/10125/24804) - Good，Reflections on Language Documentation 20 Years after Himmelmann 1998 2018。语言记录的定义、核心组成（录音、元数据、注释），以及"流水线式记录"的问题。🆓 `good2018scope`
- [Reflections on Linguistic Fieldwork](http://hdl.handle.net/10125/24822) - Bowern，Reflections on Language Documentation 20 Years after Himmelmann 1998 2018。二十年来田野方法的变化：半结构化诱导任务、重视自然语料、数字录音的利弊。🆓 `bowern2018fieldwork`
- [Reflections on Descriptive and Documentary Adequacy](http://hdl.handle.net/10125/24816) - Riesberg，Reflections on Language Documentation 20 Years after Himmelmann 1998 2018。反对"记录语料不应包含诱导材料"的看法，讨论原始数据怎样提供才能让结论可核查。🆓 `riesberg2018adequacy`
- [Reflections on (De)colonialism in Language Documentation](http://hdl.handle.net/10125/24808) - Leonard，Reflections on Language Documentation 20 Years after Himmelmann 1998 2018。一位美国原住民语言学者谈语言记录怎样从社区需求出发、怎样呈现语料。🆓 `leonard2018decolonialism`
- [Reflections on Documentary Corpora](http://hdl.handle.net/10125/24817) - Rice，Reflections on Language Documentation 20 Years after Himmelmann 1998 2018。从语料库语言学的角度谈记录语料怎样变成可检索、可分析的语料库。🆓 `rice2018corpora`

**研究类型：基于实践的研究**

- [Practice-Based Research in the Creative Arts: Foundations and Futures from the Front Line](https://doi.org/10.1162/LEON_a_01471) - Candy 等人，Leonardo 2018。两位作者依据 35 年以上指导艺术、设计、数字媒体跨学科博士的经验，讲基于实践的研究和实践的区别、作品在博士研究中的作用、评审怎样接触作品、书面论文的作用，并附六个博士案例（Scrivener、Tebby、Bell、Burraston、Johnston、Seevinck）。🆓 `candy2018practice`
- [Characteristics Statement: Doctoral Degree](https://www.qaa.ac.uk/docs/qaa/quality-code/doctoral-degree-characteristics-statement-2020.pdf) - Quality Assurance Agency for Higher Education，Quality Assurance Agency for Higher Education (QAA) 2020。英国高等教育质量保障署《博士学位特征说明》第三版，描述英国各类博士（含基于实践的博士）的特征和考核方式：作品、作品集、作曲通常附批判性评述，加口头答辩。帮助学校设计课程，不属于强制要求。🆓 `qaa2020doctoral`
- [Submissions: Basic Requirements and Submission Checklist](https://www.jar-online.net/en/submissions) - Journal for Artistic Research，Journal for Artistic Research 网页 2026。《艺术研究期刊》（艺术研究学会主办）的投稿要求：展陈（exposition）形式、一小时阅读量、博士论文材料的再利用、设计、媒体文件和版权要求。🆓 `jar2026submissions`
- [Peer Reviewing and Artistic Research; JAR Peer Review Form](https://www.jar-online.net/en/peer-reviewing-and-artistic-research) - Journal for Artistic Research，Journal for Artistic Research 网页 2023。JAR 的同行评议说明（单盲评审及理由、流程）和给评审人的评审表 2023 版。评审表第 3 节列出评审要看的五点（问题、创新、背景定位、新知识、方法），并要求评审判断"缺失是否要紧"；附录 B 讲建设性评审的误区。🆓 `jar2023peerreview`

**研究类型：基于设计的研究**

- [Design-Based Research Process: Problems, Phases, and Applications](https://repository.isls.org/bitstream/1/1130/1/317-324.pdf) - Easterday 等人，Learning and Becoming in Practice: The International Conference of the Learning Sciences (ICLS) 2014 2014。国际学习科学大会论文，把基于设计的研究定义为"聚焦、理解、确定、构思、做出、检验"六个迭代阶段，并提出按项目阶段选方法（早期粗原型、后期随机对照检验）。🆓 `easterday2014design`
- [An Introduction to Design-Based Research with an Example From Statistics Education](https://dspace.library.uu.nl/handle/1874/356250) - Bakker 等人，Approaches to Qualitative Research in Mathematics Education: Examples of Methodology and Methods 2015。专为硕士、博士生写的基于设计的研究入门章节：与随机对照试验和行动研究的比较、假设的学习轨迹、每轮的三个阶段、数据收集和分析矩阵、效度与信度，附统计教育的完整例子。🆓 `bakker2015introduction`
- [Design-Based Research: A Methodology to Extend and Enrich Biology Education Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC8711803/) - Scott 等人，CBE–-Life Sciences Education 2020。开放获取的方法论文章，以大学生理学课程为例完整走一轮"设计—检验—评估—反思"，转述 Sandoval 2014 的"认识论承诺"和猜想图思路，并讨论合作、资源和严谨性方面的困难。🆓 `scott2020design`

## 数据集与工具

- [dspinellis/awesome-msr](https://github.com/dspinellis/awesome-msr) - 实证软件工程研究可用的数据集和工具合集，以 MSR 会议命名。数据挖掘研究和工具评测找数据的首选入口。CC0。📦
- [fudanselab/awesome-software-engineering-research](https://github.com/fudanselab/awesome-software-engineering-research) - 带代码实现的 SE 论文、数据集和工具，可作为复现研究的候选。2022 年后未更新。CC0。📦

## 论文列表

### LLM 与软件工程

- [iSEngLab/AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) - 综述 *A Survey on Large Language Models for Software Engineering*（Science China Information Sciences 2026）配套的论文列表。这类综述本身就是一份系统性文献综述，可以作为系统综述的实例参考。📦 `zhang2026survey`
- [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) - 综述 *Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code*（TMLR 2024）配套的代码大模型论文列表，持续更新。📦 `zhang2024unifying`

### 安全与模糊测试

- [wcventure/FuzzingPaper](https://github.com/wcventure/FuzzingPaper) - 按会议整理的模糊测试论文列表，持续更新，附关键词检索脚本。MIT。📦
- [secfigo/Awesome-Fuzzing](https://github.com/secfigo/Awesome-Fuzzing) - 模糊测试的学习资源和工具合集。2023 年后未更新。CC0。📦

## 可复现研究

- [leipzig/awesome-reproducible-research](https://github.com/leipzig/awesome-reproducible-research) - 可复现研究的案例、复现尝试、理论文章、工具和最低标准合集。📦
- [Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745) - Wilson 等人，PLoS Biology 2014。科研编程的版本控制、测试、自动化等最佳实践。🆓 `wilson2014best`
- [Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510) - Wilson 等人，PLoS Computational Biology 2017。科研代码和数据管理的最低实用规范。🆓 `wilson2017good`
- [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285) - Sandve 等人，PLoS Computational Biology 2013。可复现计算研究的十条规则。🆓 `sandve2013ten`
- [sysartifacts：系统会议制品评估指南](https://sysartifacts.github.io/) - EuroSys、SOSP、OSDI、ATC 等会议的制品评估委员会，持续更新。作者怎样准备和打包制品，评审怎样评估。🆓 `sysartifactsguide`
- [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/) - MLflow 官方文档（工具文档）。实验追踪工具会记录哪些信息：代码版本、参数、指标、产出文件。这是工具厂商的文档，仅用来说明"该记录什么"。🆓 `mlflowtracking`
- [OSF Help：Organizing Files](https://help.osf.io/article/147-organizing-files) - 开放科学中心（Center for Open Science），持续更新。原始数据和处理后数据分开、原始数据只读、每个目录配说明文件。🆓 `osforganizing`
- [The Good Research Code Handbook](https://goodresearch.dev/) - Patrick Mineault，2021。面向写研究代码的人：一个项目一个文件夹、一个代码仓库，频繁提交，代码怎样组织和测试。🆓 `mineault2021good`
- [The Turing Way：Research Compendia](https://book.the-turing-way.org/reproducible-research/compendia) - The Turing Way 社区，持续更新。把数据、代码、文本和运行环境作为一个整体管理；数据、方法、产出分开存放，并写明运行环境。🆓 `turingwaycompendia`
- [A Quick Guide to Organizing Computational Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424) - Noble，PLoS Computational Biology 2009。计算类项目怎样组织目录：结果按日期存放、写详细的研究日志、每个数据目录配说明。🆓 `noble2009quick`
- [Ten simple rules for defining a computational biology project](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010786) - Noble，PLoS Computational Biology 2023。项目开始时怎样把目标、要回答的问题、交付物和完成标准写清楚，是写"项目简介"的依据。🆓 `noble2023ten`
- [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) - Nicholas Carlini，2022。每次发布论文（arXiv、代码等）前逐项检查的清单，把犯过的错误变成检查项。🆓 `carlini2022checklist`
- [paperswithcode/releasing-research-code](https://github.com/paperswithcode/releasing-research-code) - NeurIPS 2020 官方推荐的研究代码发布 README 模板和复现清单。2021 年后未更新。MIT。📦
- [sysartifacts/sysartifacts.github.io](https://github.com/sysartifacts/sysartifacts.github.io) - EuroSys、SOSP、OSDI、ATC 的 Artifact Evaluation 网站源码，含作者和评审的 AE 指南及历年结果。**未找到 LICENSE 文件。**📦


## 如何做好科研

资深研究者写的科研经验：博客、讲义、演讲和推文串，是通用篇的主要依据。评测方法类的条目放在上面的"研究方法指南"中。只确认了页面标题、未细读正文的条目已在说明中注明"待确认"。

### 综合与经典

- [Frascati Manual 2015](https://doi.org/10.1787/9789264239012-en) - OECD（经济合作与发展组织），2015。各国统计研发活动的国际标准，给出"什么算研究"的定义和五条判定标准（新颖、有创造性、结果不确定、系统、可转移或可复现），以及本项目采用的学科分类。🆓 `oecd2015frascati`
- [NeurIPS 2025 Call for Papers](https://neurips.cc/Conferences/2025/CallForPapers) - NeurIPS，2025。机器学习方向顶级会议的征稿启事：日期、页数、论文检查清单、双盲与预印本政策。作为会议流程的示例，以当年征稿启事为准。🆓 `neurips2025cfp`
- [USENIX Security '26 Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) - USENIX，2026。安全方向顶级会议的征稿启事：投稿日程、匿名与预印本政策、制品要求、伦理指南。作为会议流程的示例，以当年征稿启事为准。🆓 `usenixsec2026cfp`
- [Time for Computer Science to Grow Up](https://cacm.acm.org/magazines/2009/8/34492-viewpoint-time-for-computer-science-to-grow-up/fulltext) - Lance Fortnow，CACM 2009。批评会议模式导致截止日期驱动、偏向稳妥的增量工作，主张用预印本传播、用期刊评价。 `fortnow2009time`
- [Conferences vs. Journals in Computing Research](https://cacm.acm.org/opinion/conferences-vs-journals-in-computing-research/) - Moshe Vardi，CACM 2009。质疑计算机领域以会议为主的发表方式：审稿时间压力大、很少有后续期刊版。 `vardi2009conferences`
- [Evaluating Computer Scientists and Engineers for Promotion and Tenure](https://cra.org/resources/best-practice-memos/evaluating-computer-scientists-and-engineers-for-promotion-and-tenure/) - 美国计算研究协会（CRA），1999。说明计算机领域为何以会议发表为主、为何重视软件等制品。🆓 `cra1999evaluating`
- [You and Your Research](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html) - Richard Hamming，1986 年演讲。如何选择重要的问题，保持开放、长期积累。🆓 `hamming1986you`
- [Ten Simple Rules for Doing Your Best Research, According to Hamming](https://doi.org/10.1371/journal.pcbi.0030213) - Erren 等人，PLoS Computational Biology 2007。对上面演讲的归纳。🆓 `erren2007ten`
- [Principles of Effective Research](https://web.archive.org/web/20260824165302/https://michaelnielsen.org/blog/principles-of-effective-research/) - Michael Nielsen，技术笔记 2004。把高效研究拆成可培养的习惯：自我发展、提出问题与解决问题两种风格、建立研究愿景。原地址现已 404，链接为 Internet Archive 快照。🆓 `nielsen2004principles`
- [How to Have a Bad Career in Research/Academia](https://people.eecs.berkeley.edu/~pattrsn/talks/BadCareer.pdf) - David Patterson（图灵奖），演讲幻灯片 2001。用反讽的方式列出毁掉研究生涯的做法，从反面讲选题、合作、沟通和交付。🆓 `patterson2001bad`
- [Technology and Courage](https://people.cs.uchicago.edu/~ravenben/ucsb/courage-IS.pdf) - Ivan Sutherland（图灵奖），Sun Labs Perspectives 96-1，1996。研究需要勇气：面对不确定时如何决定做什么、如何坚持。链接为第三方托管的 PDF（该服务器证书链不完整，部分工具无法打开）。🆓 `sutherland1996courage`
- [Cargo Cult Science](https://calteches.library.caltech.edu/51/2/CargoCult.htm) - Richard Feynman，Caltech 毕业典礼演讲 1974。科学诚信的核心是不欺骗自己，报告所有可能推翻结论的信息。🆓 `feynman1974cargo`
- [How to do research](https://people.csail.mit.edu/billf/publications/How_To_Do_Research.pdf) - Bill Freeman（MIT），讲义 2013。从做题到做研究的转变，第一条是 "Slow down to speed up"。🆓 `freeman2013research`
- [Do Good Research!](http://people.csail.mit.edu/fredo/DoGoodResearch.pdf) - Frédo Durand（MIT），演讲幻灯片，年份待确认。关于如何做出好研究的讲座幻灯片。🆓 `durandgoodresearch`
- [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html) - John Schulman，2020。如何选题、如何推进 ML 研究。🆓 `schulman2020opinionated`
- [Tips for Empirical Alignment Research](https://www.alignmentforum.org/posts/dZFpEdKyb9Bf4xYn7/tips-for-empirical-alignment-research) - Ethan Perez，2024。实证研究的具体做法，例如快速迭代实验。🆓 `perez2024tips`
- [10 Tips for Research and a PhD](https://www.ruder.io/10-tips-for-research-and-a-phd/) - Sebastian Ruder，2020。十条建议：广泛阅读、同时推进两件事、有野心、多合作、写博客、着眼长期。🆓 `ruder2020tips`
- [How to win a best paper award (or, an opinionated take on how to do important research that matters)](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) - Nicholas Carlini，2026。最重要的是选题品味；执行要极度严谨、快速放弃不行的项目、论文只讲一个核心想法。🆓 `carlini2026best`
- [What Makes Good Research in Software Engineering?](https://www.cs.cmu.edu/~Compose/ftp/shaw-fin-etaps.pdf) - Mary Shaw，STTT 2002。用"研究问题—结果类型—验证方式"三个维度刻画什么是好的 SE 研究。🆓 `shaw2002makes`
- [What makes good research?](https://andreas-zeller.info/2012/10/16/what-makes-good-research.html) - Andreas Zeller，2012。Zeller 心目中好研究的标准：解决真实问题、有实际影响。🆓 `zeller2012good`
- [Troubling Trends in Machine Learning Scholarship](https://arxiv.org/abs/1807.03341) - Lipton & Steinhardt，ACM Queue 2019。ML 论文的四类问题：解释与推测不分、不说明收益来源（缺消融）、数学堆砌、误用术语。🆓 `lipton2019troubling`
- [Favorite Sayings](https://web.stanford.edu/~ouster/cgi-bin/sayings.php) - John Ousterhout（Stanford），持续更新。系统研究的格言集，例如"用直觉提问而不是回答问题""没被用过的东西就不算能用"。🆓 `ousterhout2021sayings`
- [Just know stuff (Or, how to achieve success in a machine learning PhD)](https://kidger.site/thoughts/just-know-stuff/) - Patrick Kidger，2023。ML 博士成功的关键是广而扎实的知识面：ML、科学计算、软件工程、数学和统计。🆓 `kidger2023know`
- [CS197: Computer Science Research](https://web.stanford.edu/class/cs197/) - Stanford 课程，Michael Bernstein 创设，2022 起。本科生科研方法课：bit flip 式的贡献表述、vectoring（逐步聚焦问题）、velocity（迭代速度）、评估、写作和同行评审。🆓

### 选题与研究品味

- [How To Choose a Good Scientific Problem](https://doi.org/10.1016/j.molcel.2009.09.013) - Uri Alon，Molecular Cell 2009。用"可行性 × 兴趣"二维图选题，并说明研究途中迷茫期（"云"）是正常的。`alon2009choose`
- [Research Taste Exercises](https://colah.github.io/notes/taste/) - Chris Olah，2021。研究品味就是挑好问题的能力，可以刻意练习：写下想法请导师评点、回顾自己的判断等。🆓 `olah2021taste`
- [My Research Process: Understanding and Cultivating Research Taste](https://www.alignmentforum.org/posts/Ldrss6o3tiKT6NdMm) - Neel Nanda，2025。研究品味不是天赋，可以通过反思、导师反馈和缩短反馈回路培养。🆓 `nanda2025taste`
- [How to come up with research ideas?](https://twitter.com/jbhuang0604/status/1423499757591400448) - Jia-Bin Huang，推文串 2021。七种产生想法的套路：换维度、放宽或增加假设、组合想法、借用新工具、对 SOTA 做压力测试等。🆓 `huang2021ideas`
- [How to decide what to work on?](https://twitter.com/jbhuang0604/status/1628521223838654464) - Jia-Bin Huang，推文串 2023。选题看五点：自己的独特优势、兴趣、对未来技术的判断、野心、能否快速验证。🆓 `huang2023decide`
- [How to Find Research Problems](https://www.cs.jhu.edu/~jason/advice/how-to-find-research-problems.html) - Jason Eisner（JHU），年份待确认。从阅读中的不满和已有工作的缺口里找研究问题。🆓 `eisnerproblems`
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) - Rich Sutton（图灵奖），2019。70 年 AI 史表明，能随算力扩展的通用方法最终胜过人工注入知识的方法。判断 AI 研究方向的常用参照。🆓 `sutton2019bitter`
- [The Second Half](https://ysymyth.github.io/The-Second-Half/) - 姚顺雨，2025。AI 进入"下半场"：重点从改进训练方法转向定义有意义的问题、设计贴近真实效用的评测。🆓 `yao2025second`
- [Research I enjoy](https://www.jasonwei.net/blog/research-i-enjoy) - Jason Wei，2022。偏好通用、影响面广、长期有用的研究，而不是窄任务上的改进。🆓 `wei2022enjoy`
- [Creativity in Academia](https://timdettmers.com/2019/09/03/creativity-in-academia/) - Tim Dettmers，2019。学术创造力的关键在于严格筛选想法、坚持面对失败，而不只是多出想法。🆓 `dettmers2019creativity`
- [My research idea logfile, 2016-2019](https://nicholas.carlini.com/writing/2024/my-research-logfile.html) - Nicholas Carlini，2024。公开 2016–2019 年的研究想法记录文件，可以看到想法如何产生、哪些后来做成了。需要对抗机器学习背景。🆓 `carlini2024logfile`
- [Increasing the Impact of PL Research](http://www.pl-enthusiast.net/2020/07/29/increasing-the-impact-of-pl-research/) - Michael Hicks，PL Enthusiast 2020。什么是一个研究领域（基础技术 + 围绕它的难题与应用），以及 PL 研究如何面向更大的问题扩大影响。🆓 `hicks2020impact`
- [Don't teach. Incentivize: Scale-first view of large language models](https://www.csail.mit.edu/event/ei-seminar-hyung-won-chung-openai-dont-teach-incentivize-scale-first-view-large-language) - Hyung Won Chung，MIT EI Seminar 2024。与其教模型每项技能，不如设计激励让它自己学；研究方向要顺应算力扩展。链接为活动页面，视频地址待确认。🆓

### 研究流程与习惯

- [Research as a Stochastic Decision Process](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html) - Jacob Steinhardt，2018。按"单位时间获得的信息量"排序任务，先做最可能让项目失败的环节，尽早去风险。🆓 `steinhardt2018stochastic`
- [The Turing Way：Guide for Project Design](https://book.the-turing-way.org/project-design/project-design) - The Turing Way 社区（艾伦·图灵研究所发起），持续更新。项目设计阶段要想清楚的研究问题、范围、成功标准和计划方式；也讨论了甘特图等计划工具在研究中的适用性。🆓 `turingwaydesign`
- [How I Think About My Research Process: Explore, Understand, Distill](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL/p/hjMy4ZxS5ogA9cTYK) - Neel Nanda，2025。把研究分成选题、探索、理解、提炼四个阶段，各有目标和常见陷阱。同系列的 [Key Mindsets](https://www.alignmentforum.org/posts/cbBwwm4jW6AZctymL) 讲求真、排优先级和快速推进。🆓 `nanda2025process` `nanda2025mindsets`
- [Practicing AI research](https://www.jasonwei.net/blog/practicing-ai-research) - Jason Wei，2023。研究是可以练习的技能，分为选题、做实验、写论文、扩大影响四部分。🆓 `wei2023practicing`
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) - Andrej Karpathy，2019。训练神经网络的系统流程：先吃透数据，从简单到复杂，每一步都验证假设。🆓 `karpathy2019recipe`
- [How to do experiments?](https://twitter.com/jbhuang0604/status/1647098218172252160) - Jia-Bin Huang，推文串 2023。实验是为了检验假设而不是刷分：一次只改一个变量、先写下预期、建好 baseline、系统记录。🆓 `huang2023experiments`
- [How to get unstuck?](https://twitter.com/jbhuang0604/status/1717381151508054029) - Jia-Bin Huang，推文串 2023。大多数实验会失败；卡住时找人讨论、画出流程、逐步简化问题。🆓 `huang2023unstuck`
- [Rapid Iteration in Machine Learning Research](https://nicholas.carlini.com/writing/2022/rapid-iteration-machine-learning-research.html) - Nicholas Carlini，2022。缩短实验的等待时间，例如对 Python 环境做快照、交互式修改后反复运行，以加快迭代。🆓 `carlini2022rapid`
- [Personal Rules of Productive Research](https://www.eugenevinitsky.com/posts/personal-rules-of-productive-research) - Eugene Vinitsky，年份待确认。从反复试错中总结的个人高效研究规则。🆓 `vinitskyrules`
- [google-research/tuning_playbook](https://github.com/google-research/tuning_playbook) - Google Research 的深度学习调参与实验设计手册：科学化的增量实验、超参数分类。2024 年后未更新。CC BY 4.0。📦
- [Calendar. Not to-do lists.](https://deviparikh.substack.com/p/calendar-in-stead-of-to-do-lists-9ada86a512dd) - Devi Parikh，2018。把每项任务排进日历而不是写待办清单，让"时间有限"变得看得见。🆓 `parikh2018calendar`

### 读论文

- [How to Read a Paper](https://doi.org/10.1145/1273445.1273458) - S. Keshav，ACM SIGCOMM CCR 2007。三遍阅读法。🆓 `keshav2007read`
- [How to Read a Technical Paper](https://www.cs.jhu.edu/~jason/advice/how-to-read-a-paper.html) - Jason Eisner（JHU），年份待确认。主动地、分多遍读论文，边读边批注和总结。🆓 `eisnerread`
- [How to Read an Engineering Research Paper](https://cseweb.ucsd.edu/~wgg/CSE210/howtoread.html) - William Griswold（UCSD），年份待确认。面向 SE 和工程类论文的阅读提问清单。🆓 `griswoldread`
- [Critical Reading](https://faculty.washington.edu/ebender/critical_reading.pdf) - Emily Bender（UW），讲义 2003。批判性阅读的提问清单：研究问题是什么、提问时有哪些预设、数据如何收集、可能有哪些偏差、结论依据什么证据。🆓 `bender2003critical`
- [Ways to Engage Deeply with a Paper](https://www.eugenevinitsky.com/posts/paper-games) - Eugene Vinitsky，年份待确认。用模板和"小游戏"让读论文更主动、更深入。🆓 `vinitskypaper`
- [CS230 Lecture 8: Career Advice / Reading Research Papers](https://www.youtube.com/watch?v=733m6qBH-jI) - Andrew Ng，Stanford CS230 2018。分多遍读论文（先看标题、摘要和图），入门读 15–20 篇、深入读 50–100 篇；以及 ML 职业建议。只确认了视频页面标题，内容待确认。🆓

### 写作

- [How to Write a Great Research Paper](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) - Simon Peyton Jones。论文写作，附幻灯片和视频。🆓 `peytonjones2013write`
- [Writing Good Software Engineering Research Papers](https://www.cs.cmu.edu/~Compose/shaw-icse03.pdf) - Mary Shaw，ICSE 2003。分析 ICSE 2002 投稿，归纳 SE 论文的问题类型、结果类型和验证方式，以及被录用论文怎样陈述它们。🆓 `shaw2003writing`
- [How to write a technical paper](https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html) - Michael Ernst（UW），持续更新。从动机、贡献陈述到结构和修改，系统讲技术论文写作。🆓 `ernstwrite`
- [Tips for Writing Technical Papers](https://cs.stanford.edu/people/widom/paper-writing.html) - Jennifer Widom（Stanford），年份待确认。经典的"引言五问"模板，以及标题、摘要、相关工作、实验的写法。🆓 `widomtips`
- [Write the Paper First](https://www.cs.jhu.edu/~jason/advice/write-the-paper-first.html) - Jason Eisner（JHU），2010。在做实验之前先写论文草稿，用来理清论点、决定要做哪些实验。🆓 `eisnerfirst`
- [Whitesides' Group: Writing a Paper](https://doi.org/10.1002/adma.200400767) - George Whitesides，Advanced Materials 2004。用提纲写论文，并在研究进行中就开始写提纲，让写作推动研究。`whitesides2004writing`
- [Good Writing](http://www.cs.cmu.edu/~pausch/Randy/Randy/raibert.htm) - Marc Raibert，1985。好文章靠想写好、相信能写好、先写烂稿再反复修改，附具体的修改技巧。🆓 `raibert1985good`
- [Some Research Paper Writing Recommendations](https://avandeursen.com/2013/07/10/research-paper-writing-recommendations/) - Arie van Deursen（TU Delft），2013。SE 论文写作建议，例如贡献要写成结果而不是付出的工作量。🆓 `vandeursen2013writing`
- [An Evaluation of the Ninth SOSP Submissions; or, How (and How Not) to Write a Good Systems Paper](https://www.usenix.org/legacy/events/samples/submit/advice.html) - Levin & Redell，ACM SIGOPS OSR 1983。SOSP 程序委员会主席总结的系统论文清单：原创性、真实系统、经验教训、设计选择与评估。🆓 `levin1983sosp`
- [A Referee's Plea](https://mallman.net/plea.txt) - Mark Allman（ICSI），2001。以 SIGCOMM 程序委员会的经历列出论文中容易修正的常见问题，包括实验结果的呈现。🆓 `allman2001plea`
- [HOWTO: Avoid common problems when writing a security conference paper](https://www.metzdowd.com/pipermail/cryptography/2008-January/013419.html) - Peter Gutmann，2008。安全会议程序委员会视角下投稿的常见问题清单。🆓 `gutmann2008security`
- [Highly Opinionated Advice on How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) - Neel Nanda，2025。把研究压缩成 1–3 个有严格证据支撑的核心论断，再从摘要、引言到正文逐层展开。🆓 `nanda2025writing`
- [Writing a good scientific paper](https://perceiving-systems.blog/en/news/writing-a-good-scientific-paper) - Michael J. Black（MPI-IS），2024。他多年来给学生的 CV/图形学论文写作指南。🆓 `black2024writing`
- [How to write the Introduction?](https://twitter.com/jbhuang0604/status/1638029709073166336) - Jia-Bin Huang，推文串 2023。用 WHAT/WHY/HOW 和五个问题（问题、已有工作、缺口、做了什么、贡献）组织引言。🆓 `huang2023introduction`
- [Planning paper writing](https://deviparikh.substack.com/p/planning-paper-writing-553f497e8839) - Devi Parikh，2019。提前规划论文写作的时间线和分工。另见同作者的 [Shortening papers to fit page limits](https://deviparikh.substack.com/p/shortening-papers-to-fit-page-limits-97601318681d)。🆓 `parikh2019planning`
- [Research Debt](https://distill.pub/2017/research-debt/) - Olah & Carter，Distill 2017。糟糕的解释让领域积累"研究债"；提炼和清晰解释是被低估的研究工作。🆓 `olah2017debt`
- [Notes on writing](http://people.csail.mit.edu/fredo/PUBLI/writing.pdf) - Frédo Durand（MIT），年份待确认。论文写作讲义。🆓 `durandwriting`
- [Writing Technical Articles / Common Bugs in Writing](https://www.cs.columbia.edu/~hgs/etc/writing-style.html) - Henning Schulzrinne（Columbia）。系统、网络论文的结构建议，以及[常见英文写作错误清单](https://www.cs.columbia.edu/~hgs/etc/writing-bugs.html)。🆓
- [Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619) - Mensh & Kording，PLoS Computational Biology 2017。论文结构的十条规则：每段、每节都按"背景—内容—结论"组织。🆓 `mensh2017ten`
- [Ten Simple Rules for Writing Research Papers](https://doi.org/10.1371/journal.pcbi.1003453) - Weixiong Zhang，PLoS Computational Biology 2014。研究论文写作的十条规则。🆓 `zhang2014ten`
- [Ten Simple Rules for Getting Published](https://doi.org/10.1371/journal.pcbi.0010057) - Philip Bourne，PLoS Computational Biology 2005。发表论文的十条规则。🆓 `bourne2005published`

### 审稿与作者回复

- [Reviewing a technical paper](https://homes.cs.washington.edu/~mernst/advice/review-technical-paper.html) - Michael Ernst（UW），持续更新。如何写出公正、有建设性、对作者有用的评审。🆓 `ernstreview`
- [Writing reviews for systems conferences](https://people.inf.ethz.ch/troscoe/pubs/review-writing.pdf) - Timothy Roscoe（ETH），2007。为 SOSP 影子程序委员会写的审稿指南：评审有哪些用途、怎样写好。🆓 `roscoe2007reviews`
- [Thoughts on Reviewing](https://mallman.net/pubs/All08a/All08a.pdf) - Mark Allman，ACM SIGCOMM CCR 2008。对网络领域审稿流程和评审质量的反思与建议。🆓 `allman2008thoughts`
- [Advice on reviewing papers](http://www.pl-enthusiast.net/2014/08/21/advice-reviewing-papers/) - Michael Hicks，PL Enthusiast 2014。PL 社区的审稿建议：如何评估贡献、写出有帮助的评审。同作者另有 [Advice on writing an author response](http://www.pl-enthusiast.net/2014/09/17/advice-writing-author-response/)。🆓 `hicks2014reviewing` `hicks2014response`
- [Patterns for writing good rebuttals](https://andreas-zeller.info/2012/10/01/patterns-for-writing-good-rebuttals.html) - Andreas Zeller，2012。作者回复（rebuttal）的常用写法和注意事项。🆓 `zeller2012rebuttals`
- [How do different fields review papers? Experiences from ICSE, PLDI, and CCS](https://andreas-zeller.info/2021/07/27/Reviewing-across-fields-ICSE-PLDI-CCS.html) - Andreas Zeller，2021。比较 SE、PL、安全三个社区审稿文化的差异。🆓 `zeller2021fields`
- [How we write rebuttals](https://deviparikh.substack.com/p/how-we-write-rebuttals-dc84742fece1) - Parikh、Batra、Lee，2020。rebuttal 的目的是澄清和说服，要周全、直接、好读，同时照顾审稿人和 AC 两类读者。🆓 `parikh2020rebuttals`
- [Novelty in Science: A guide for reviewers](https://perceiving-systems.blog/en/news/novelty-in-science) - Michael J. Black，2022。审稿人常把复杂和难度误当作新颖性；真正的新颖往往是简单而深刻的洞见。🆓 `black2022novelty`
- [How to peer review scientific work](https://matt.might.net/articles/how-to-peer-review/) - Matt Might，年份待确认。同行评审的方法。同作者另有 [Responding to peer review](https://matt.might.net/articles/peer-review-rebuttals/)。🆓 `mightreview`
- [Ten Simple Rules for Reviewers](https://doi.org/10.1371/journal.pcbi.0020110) - Bourne & Korngreen，PLoS Computational Biology 2006。审稿人的十条规则。🆓 `bourne2006reviewers`
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines) - ACL Rolling Review。NLP 会议的官方审稿指南，包括常见的不当审稿理由。🆓

### 学术报告

- [Giving a technical presentation](https://homes.cs.washington.edu/~mernst/advice/giving-talk.html) - Michael Ernst（UW），持续更新。学术报告的结构、幻灯片和演讲技巧。🆓 `ernsttalk`
- [How to Speak](https://www.youtube.com/watch?v=Unzc731iCUY) - Patrick Winston（MIT），讲座 2018。MIT 的经典公开讲座：开场承诺、反复强调、给听众"带得走的东西"、幻灯片与收尾技巧。🆓 `winston2018speak`
- [Tips for Giving Clear Talks](http://graphics.stanford.edu/~kayvonf/misc/cleartalktips.pdf) - Kayvon Fatahalian（Stanford），2023。每张幻灯片一个要点、标题就是结论、从听众角度组织叙事。🆓 `fatahalian2023talks`
- [Assembling A Talk: Two Wrong Ways and a Right Way](http://www.tkim.graphics/HOWTOTALK/HowToTalk.pdf) - Theodore Kim（Yale），2019。不要先开 PowerPoint 硬凑；先写提纲、讲清故事，再做幻灯片。🆓 `kim2019talk`
- [Oral Presentation Advice](https://pages.cs.wisc.edu/~markhill/conference-talk.html) - Mark Hill（UW-Madison），年份待确认。会议报告的准备和表达要点。🆓 `hilltalk`
- [How to Write a Conference Talk](http://www.pl-enthusiast.net/2019/01/02/how-to-write-a-conference-talk/) - Michael Hicks，PL Enthusiast 2019。会议报告的构思和组织方法。🆓 `hicks2019talk`
- [How to Give a Bad Talk](https://www.cs.utexas.edu/~dahlin/professional/badTalk.pdf) - Mike Dahlin（UT Austin）整理自 Ousterhout、Anderson、Patterson 等人，2006。系统领域会议报告的反面教材。同作者另有 [Giving a Conference Talk](https://www.cs.utexas.edu/~dahlin/professional/goodTalk.pdf)。🆓 `dahlin2006badtalk`

### 读博、导师与职业

- [A Survival Guide to a PhD](http://karpathy.github.io/2016/09/07/phd/) - Andrej Karpathy，2016。要不要读博、选导师、培养选题品味、论文只讲一个核心贡献、作报告和参会。🆓 `karpathy2016survival`
- [How to Be a Successful PhD Student (in Computer Science (in NLP/ML))](https://www.cs.jhu.edu/~mdredze/publications/HowtoBeaSuccessfulPhDStudent.1_2.pdf) - Mark Dredze & Hanna Wallach，2012（v1.2 更新于 2022）。面向 NLP/ML 博士生：与导师相处和开会、日常效率、读论文和选题、先做最简单的证伪实验、分析失败样本、按期投稿。🆓 `dredze2012successful`
- [Prof Halim's PhD Tips](https://www.comp.nus.edu.sg/~stevenha/myresearch/phd_tips.html) - Steven Halim（NUS），持续更新。博士生活的利弊、科技写作规范、报告技巧、审稿和回复审稿、答辩与教学。🆓 `halimtips`
- [Five tips for starting (and continuing) a PhD](https://blogs.ed.ac.uk/ellie-wood/2020/09/04/five-tips-for-starting-and-continuing-a-phd/) - Ellie Wood（爱丁堡大学博士研究者），2020。系统记阅读笔记、读几篇近期的学位论文、尽早建立论文大纲文档、多和同伴与导师交流。🆓 `wood2020five`
- [A PhD So Good It Can't Be Ignored: Passion, Practice, and Control](https://ahappyphd.org/posts/phd-so-good-1/) - Luis P. Prieto（A Happy PhD），2025。借用 Cal Newport 的观点：不要只追随热情，先靠刻意练习积累稀缺技能，再争取自主权。🆓 `prieto2025so`
- [How to be a successful PhD student?](https://medium.com/data-science/how-to-be-a-successful-phd-student-3f3a4eb48be8) - Dorien Herremans（SUTD），2020。实验室最佳实践清单：别在截稿前一天才给导师看稿、与博后结对、开源代码并发预印本、固定作息、主动掌控项目。🆓 `herremans2020successful`
- [10 pieces of advice I wish my PhD advisor had given me](https://www.sigcommedu.web.illinois.edu/advice/kurose_wish_advisor.pdf) - Jim Kurose（UMass），幻灯片，年份待确认。十条建议：广泛学习（尤其数学）、慎选问题、自上而下地写作、站在读者角度、好文章需要时间。🆓 `kuroseadvice`
- [The illustrated guide to a Ph.D.](https://matt.might.net/articles/phd-school-in-pictures/) - Matt Might，2010。用一组圆形图说明博士就是把人类知识的边界向外推出一个小凸起。另见 [3 qualities of successful Ph.D. students](https://matt.might.net/articles/successful-phd-students/)。🆓 `might2010illustrated` `might2010successful`
- [A graduate school survival guide: "So long, and thanks for the Ph.D!"](https://www.cs.unc.edu/~azuma/hitch4.html) - Ronald Azuma，1997（2003 修订）。读博所需的心理韧性和技能，以及毕业后求职。🆓 `azuma2003survival`
- [Expectation Setting for a PhD](https://www.eugenevinitsky.com/posts/expectation-setting) - Eugene Vinitsky，年份待确认。博士生和导师之间如何设定相互期望。🆓 `vinitskyexpectation`
- [How to meet with your advisor?](https://twitter.com/jbhuang0604/status/1653614931202195458) - Jia-Bin Huang，推文串 2023。会前异步分享结果、准备议程、先讲背景再讲细节、主动提出下一步、会后立刻写纪要。🆓 `huang2023advisor`
- [How to cope with paper rejection?](https://twitter.com/jbhuang0604/status/1443248831102136333) - Jia-Bin Huang，推文串 2021。被拒是常态；把审稿意见当作改进清单，也可以建一份"失败简历"。🆓 `huang2021rejection`
- [Behind the Scenes: The Struggle for Each Paper](https://jeffhuang.com/struggle_for_each_paper/) - Jeff Huang（Brown），2021。逐篇复盘自己 30 篇论文背后的被拒、时机和合作经历，说明发表从来不顺利。🆓 `huang2021struggle`
- [AI research is a max-performance domain](https://jasonwei.net/blog/ai-research-is-a-max-performance-domain) - Jason Wei，2025。AI 研究看的是最高水平：一项能力足够突出就能弥补其他短板。另见 [Dopamine cycles in AI research](https://jasonwei.net/blog/e2jwko63n64ot4kkvqdd7nlejd2m3x)。🆓 `wei2025maxperf`
- [Career Advice](https://terrytao.wordpress.com/career-advice/) - Terence Tao（UCLA），持续更新。按本科、研究生、博士后阶段整理的数学研究职业建议，例如多听报告、接受阶段性进展。🆓
- [Applying to Ph.D. Programs in Computer Science](https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf) - Mor Harchol-Balter（CMU），2014。CS 博士申请指南：录取看什么、推荐信与研究经历、如何选校和导师。🆓 `harcholbalter2014applying`
- [How to Choose Your Grad School](https://timdettmers.com/2022/03/13/how-to-choose-your-grad-school/) - Tim Dettmers，2022。从导师、同伴、地点、资金等方面选研究生院。另见 [Machine Learning PhD Applications](https://timdettmers.com/2018/11/26/phd-applications/)。🆓 `dettmers2022grad`
- [AI research: the unreasonably narrow path and how not to be miserable](https://www.youtube.com/watch?v=0blQp0_9NwY) - Rosanne Liu，演讲 2020。AI 研究职业道路之窄，以及如何不让自己痛苦。只确认了视频页面标题，讲者与日期待确认。🆓

### 建议合集

- [jbhuang0604/awesome-tips](https://github.com/jbhuang0604/awesome-tips) - Jia-Bin Huang 整理的研究、写作、审稿、报告建议。MIT。📦
- [pliang279/awesome-phd-advice](https://github.com/pliang279/awesome-phd-advice) - Paul Liang（CMU）整理的博士生建议链接合集。2023 年后未更新。MIT。📦
- [shaily99/advice](https://github.com/shaily99/advice) - Shaily Bhatt 整理的研究和申请建议链接合集。2023 年后未更新。MIT。📦
- [Michael Ernst's advice](https://homes.cs.washington.edu/~mernst/advice/) - Michael Ernst（UW）。30 多篇实用指南：写论文、作报告、找导师、申请、审稿、求职。🆓
- [Advice for Research Students (and others)](https://www.cs.jhu.edu/~jason/advice/) - Jason Eisner（JHU）。二十多篇短文：读论文、找问题、先写论文、作报告、评估导师等。🆓
- [Resources for students](https://people.csail.mit.edu/fredo/student.html) - Frédo Durand（MIT）。Durand 自己的研究、写作、报告、审稿讲义，以及大量外部经典资源。🆓
- [Advice for Researchers and Students](https://taoxie.cs.illinois.edu/advice/) - Tao Xie。SE 方向的建议合集：写作、研究规划、研究伦理、相机就绪版检查清单等。另见 [Advice on Getting a Start into Research](https://taoxie.cs.illinois.edu/adviceonresearch.html)。🆓
- [ACM SIGCOMM Education: Advice](https://www.sigcommedu.web.illinois.edu/advice.html) - ACM SIGCOMM。网络和系统社区的研究、写作、报告建议合集（部分子链接已失效）。🆓
- [Collected Advice on Research and Writing](https://www.cs.cmu.edu/afs/cs.cmu.edu/user/mleone/web/how-to.html) - Mark Leone（CMU）。较早的研究与写作建议链接合集。🆓
- [pengsida/learning_research](https://github.com/pengsida/learning_research) - 浙大彭思达整理的科研经验：选题、做研究、论文写作和投稿。约 14.5k star。**未找到 LICENSE 文件。**📦
- [hzwer/WritingAIPaper](https://github.com/hzwer/WritingAIPaper) - 面向新手的 AI 会议论文写作手册：写作、投稿、审稿流程、被拒后的处理。**未找到 LICENSE 文件。**📦

## 科研 skills（待评估）

> 这些仓库把科研流程写成一步步的具体做法（多数以 Claude Code 等 AI 工具的 skill 形式发布），是 best practice 的另一类来源：同一个流程，不同的人有不同的拆法。多数没有公开证据说明按它们做研究质量会更好，需要和经验类资料、方法规范对照评估后再采用。

- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) - 98 个 skills，以 ML 工程为主（微调、分布式训练、推理部署等）。MIT。📦
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) - 原名 claude-scientific-skills。177 个 skills，面向生物信息、化学信息、临床、材料等领域。MIT。📦
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) - Claude Code 插件，包含深度调研、论文写作、审稿和一个 10 阶段的流程，带人工检查点。**CC BY-NC 4.0，禁止商用。**📦
- [brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research](https://github.com/brycewang-stanford/Awesome-Agent-Skills-for-Empirical-Research) - 面向实证研究的 agent skills（AERS），偏经济学和统计方法。现已改名为 Auto-Empirical-Research-Skills（旧地址自动跳转）。CC BY-SA 4.0。📦
- [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) - 科研类 agent skills 的索引。MIT。📦

### 软件工程实证研究

以下来自海德堡大学 SE 组（se-uhd），star 很少但作者权威、2026-09 至 10 月仍在更新，都没有公开的效果评测。

- [se-uhd/llm-guidelines-skill](https://github.com/se-uhd/llm-guidelines-skill) - 把 `baltes2026guidelines` 的 8 条指南做成 skill：explore 模式用于讨论指南、规划研究，review 模式按指南审查论文草稿并出报告。自有内容 CC BY 4.0。📦
- [se-uhd/llm-guidelines-paper](https://github.com/se-uhd/llm-guidelines-paper) - 上述指南的 LaTeX 源，llm-guidelines.org 内容的来源。CC BY 4.0。📦
- [se-uhd/cea-skill](https://github.com/se-uhd/cea-skill) - Claim-Evidence Alignment：从论文 PDF 抽取定量论断及其证据链，与论文和 artifact 逐一对照；Claude 起草、人工核查。可用于复现和审稿。MIT。📦
- [se-uhd/hallucite](https://github.com/se-uhd/hallucite) - 检测论文 PDF 中伪造（幻觉）的参考文献，附打分脚本，结果数字待确认。MIT。📦
- [se-uhd/ai-slop-skill](https://github.com/se-uhd/ai-slop-skill) - 检测并修改文稿中的"AI 腔"，针对实证 SE 论文。自有内容 CC BY 4.0。📦
- [keemanxp/slr-prisma](https://github.com/keemanxp/slr-prisma) - 按 PRISMA 2020 的 27 项清单分六个阶段引导撰写系统综述。作者背景不明，面向通用学科而不是 SE 的 Kitchenham 范式。MIT。📦

### 科研流程与写作

- [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - ARIS，纯 Markdown 的自主 ML 科研 skills：选题、文献、实验、跨模型评审循环、写作，直到产出论文。约 17k star；README 只有一次运行的分数变化，没有对照实验。MIT。📦
- [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) - 半自动科研助手的 skills、commands 和 hooks：文献、实验分析、消融、写作、rebuttal、汇报。MIT。📦
- [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) - 约 30 个 skills：文献综述、想法生成与打分、新颖性评估、rebuttal。**未找到 LICENSE 文件。**📦
- [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) - 两阶段（先大纲、后深入）的 deep research skill，带人工控制点，支持 Claude Code、OpenCode、Codex。MIT。📦
- [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) - Emory 经济学者 Pedro Sant'Anna 的 Claude Code 学术工作流模板：多 agent 评审、0–100 分的质量门槛、对抗式 QA。MIT。📦
- [flonat/flonat-research](https://github.com/flonat/flonat-research) - 面向博士研究者的 Claude Code / Codex 科研配置：skills、agents、rules、hooks。MIT。📦
- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) - 把彭思达的科研写作笔记整理成写作 skill，按章节给指南，带论断—证据检查和投稿前自审。MIT。📦
- [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) - UCSB 系统与网络实验室的论文写作 skill：五阶段流程、各章节的写法、风格审计和独立 red-team。规则从 7,600 多次 Overleaf 修改中归纳（见其 DESIGN.md）。MIT。📦
- [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) - 科学写作 agent 和 skills：同行评审、示意图、文献检索与引用。MIT。📦
- [Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra) - 社区对 Google PaperOrchestra 论文的非官方实现：把附录中的五个 agent 的提示词做成 skills，从实验日志生成 LaTeX 论文。原论文有 PaperWritingBench 评测，本实现没有。MIT。📦

### 合集与规范

- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic 官方 skills 仓库。没有科研专用 skill，但 `skill-creator` 包含编写 skill 和做评测的方法，可作为自建科研 skill 的规范参考。多数 skill 为 Apache-2.0。📦
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) - 1000 多个 agent skills 的通用合集，科研只占一小部分。MIT。📦

## AI Scientist 相关系统

属于相关工作，不是科研方法知识。

- [ResearAI/Awesome-AI-Scientist](https://github.com/ResearAI/Awesome-AI-Scientist) - 按知识、选题、实验、写作、审稿组织的 AI 科研论文和工具列表。2025-11 后未更新；许可信息不一致（LICENSE 文件为 Apache-2.0，README 写的是 MIT）。📦
- [ai4s-research/awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) - 原 ai-boost/awesome-ai-for-science。AI for Science 的工具、论文、数据集合集。MIT。📦
- [worldbench/awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) - 按 8 个研究阶段整理的自动化科研论文列表。MIT。📦
- [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) - 基于 agentic tree search 的端到端 AI Scientist，包含选题、实验、写作、审稿的提示词模板；生成的论文通过了 ICLR workshop 评审。**AI Scientist Source Code License（基于 RAIL，有使用限制）。**📦
- [SamuelSchmidgall/AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) - 文献综述、实验、报告写作的端到端科研 agent，各阶段有角色提示词；论文（arXiv:2501.04227）含人工评测。MIT。📦
- [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) - 从想法到论文的自主科研系统，含新颖性打分；论文（arXiv:2605.20025）提出 ARC-Bench（55 个开放课题）。MIT。📦
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) - 极简的自主实验循环：人只写一个 program.md，agent 在单 GPU 上反复"改 train.py、跑 5 分钟、保留或回滚"。没有正式评测。**未找到 LICENSE 文件。**📦
- [stanford-oval/storm](https://github.com/stanford-oval/storm) - 通过多视角提问和检索生成带引用的长篇综述，可作为文献调研流程的参考；NAACL 2024 论文含自动和人工评测。MIT。📦
- [NeuroDong/Ai-Review](https://github.com/NeuroDong/Ai-Review) - 大模型辅助审稿，并能与目标会议的录用论文做相对排序；在 PeerRead ICLR 2017 的 100 组样本上 pairwise 准确率 83.8%（仓库自报）。MIT。📦

## 待获取

需要付费或无法直接访问、但有价值的资料，见 [`papers/README.md`](../papers/README.md#待获取)。
