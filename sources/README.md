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
| 团队内部材料 | [`../internal/`](../internal/README.md) |

**图例**：🆓 有免费全文 · 💰 需要付费 · 📦 GitHub 仓库（已作为 submodule 引入 `repos/`）· `key` 为 `references.bib` 中的条目。

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

### 复现研究

- [Understanding replication of experiments in software engineering: A classification](https://doi.org/10.1016/j.infsof.2014.04.004) - Gómez、Juristo、Vegas，IST 2014。复现研究的分类。💰 `gomez2014understanding`
- [The role of replications in Empirical Software Engineering](https://doi.org/10.1007/s10664-008-9060-1) - Shull 等人，EMSE 2008。复现研究在实证软件工程中的作用。💰 `shull2008role`
- [Towards Reporting Guidelines for Experimental Replications: A Proposal](https://carver.cs.ua.edu/ReplicationGuidelines.htm) - Carver，RESER 2010。复现研究的报告规范。🆓 `carver2010towards`
- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current) - ACM，v1.1，2020。复现材料评审与徽章政策，区分"可用""已评估""结果已复现/已重现"等级别。🆓 `acm2020artifact`

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
- [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/) - Blackburn、Berger、Hauswirth、Hicks 等，ACM SIGPLAN 2018。七类检查项：明确声明、基准选择、数据分析、工作负载、统计严谨、威胁缓解、可复现。适合当作工具评测的检查清单。🆓 `blackburn2018sigplan`
- [Gernot's List of Systems Benchmarking Crimes](https://gernot-heiser.org/benchmarking-crimes.html) - Gernot Heiser（UNSW），持续更新。系统论文中常见的基准测试"罪行"：选择性使用基准、不当比较、关键信息缺失等。🆓 `heiserbenchmarking`
- [The Devil's Guide to Incremental Research](https://andreas-zeller.info/2021/04/15/the-devils-guide-to-incremental-research.html) - Andreas Zeller，2021。以反讽方式列出 12 种"注水"研究的套路（例如挑选有利的结果），供作者和审稿人识别。🆓 `zeller2021devil`
- ["Bad smells" in software analytics papers](https://arxiv.org/abs/1803.05518) - Menzies & Shepperd，IST 2019。软件分析类论文的"坏味道"清单，供作者和审稿人自查。🆓 `menzies2019bad`
- [How to avoid machine learning pitfalls: a guide for academic researchers](https://arxiv.org/abs/2108.02497) - Michael Lones，arXiv 2021（持续更新）。从建模、评估、比较到报告，列出学术 ML 研究的常见陷阱及避免方法。🆓 `lones2021avoid`
- [On Evaluating Adversarial Robustness](https://arxiv.org/abs/1902.06705) - Carlini 等人，arXiv 2019。对抗鲁棒性防御的评估方法与检查清单。🆓 `carlini2019evaluating`
- [Successful language model evals](https://jasonwei.net/blog/evals) - Jason Wei，2024。好的 LLM 评测基准有哪些特征：样本足够多、分数含义清楚易懂、有大论文使用等。🆓 `wei2024evals`
- [Producing wrong data without doing anything obviously wrong!](https://doi.org/10.1145/1508244.1508275) - Mytkowicz 等人，ASPLOS 2009。链接顺序、环境变量大小等看似无关的因素会产生测量偏差，足以推翻实验结论。`mytkowicz2009producing`
- [Statistically rigorous Java performance evaluation](https://doi.org/10.1145/1297027.1297033) - Georges 等人，OOPSLA 2007。性能测量中应使用置信区间等统计方法，而不是只报告单次或最好的结果。`georges2007statistically`
- [Rigorous benchmarking in reasonable time](https://doi.org/10.1145/2464157.2464160) - Kalibera & Jones，ISMM 2013。在有限时间内设计多层次的重复实验，以获得可靠的性能结果。`kalibera2013rigorous`
- [Wake up and smell the coffee: evaluation methodology for the 21st century](https://doi.org/10.1145/1378704.1378723) - Blackburn 等人，CACM 2008。指出性能评估方法上的缺陷并给出改进建议。`blackburn2008wake`
- [Scientific benchmarking of parallel computing systems](https://doi.org/10.1145/2807591.2807644) - Hoefler & Belli，SC 2015。并行计算性能报告的 12 条规则。`hoefler2015scientific`


### 实证研究通用

- [Experimentation in Software Engineering](https://doi.org/10.1007/978-3-662-69306-3) - Wohlin 等人，Springer，第 2 版 2024。实验研究的标准教材，威胁效度的经典论述出自这里。💰 `wohlin2024experimentation`
- [Guidelines for conducting and reporting case study research in software engineering](https://doi.org/10.1007/s10664-008-9102-8) - Runeson & Höst，EMSE 2009。案例研究指南，其中的效度讨论有参考价值。开放获取（CC BY-NC）。🆓 `runeson2009guidelines`
- [Contemporary Empirical Methods in Software Engineering](https://doi.org/10.1007/978-3-030-32489-6) - Felderer & Travassos（编），Springer 2020。多种实证方法的较新综述，仅第 17 章（Open Science）开放获取。💰 `felderer2020contemporary`
- [Sampling in software engineering research: a critical review and guidelines](https://arxiv.org/abs/2002.07764) - Baltes & Ralph，EMSE 2022。SE 研究中抽样方法的批判性综述和指南。🆓 `baltes2022sampling`
- [Views on Internal and External Validity in Empirical Software Engineering](https://doi.org/10.1109/ICSE.2015.24) - Siegmund、Siegmund、Apel，ICSE 2015。调查 SE 社区如何看待内部效度与外部效度的取舍。`siegmund2015views`
- [SoK: Science, Security and the Elusive Goal of Security as a Scientific Pursuit](https://doi.org/10.1109/SP.2017.38) - Herley & van Oorschot，IEEE S&P 2017。借科学哲学审视安全研究的科学性，批评不可证伪的主张。`herley2017sok`
- [The Menlo Report](https://www.caida.org/publications/papers/2012/menlo_report/menlo_report.pdf) - Bailey、Dittrich、Kenneally、Maughan，IEEE Security & Privacy 2012。介绍美国国土安全部资助的 Menlo 报告：在 Belmont 报告三原则之上增加"尊重法律与公共利益"，是安全和网络研究伦理的常用依据。报告原文见 [SSRN](https://doi.org/10.2139/ssrn.2445102)。🆓 `bailey2012menlo`
- [Ethical considerations in network measurement papers](https://doi.org/10.1145/2896816) - Partridge & Allman，CACM 2016。测量类论文应如何讨论和处理伦理问题。`partridge2016ethical`


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
- [Research Paper Release Checklist](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) - Nicholas Carlini，2022。每次发布论文（arXiv、代码等）前逐项检查的清单，把犯过的错误变成检查项。🆓 `carlini2022checklist`
- [paperswithcode/releasing-research-code](https://github.com/paperswithcode/releasing-research-code) - NeurIPS 2020 官方推荐的研究代码发布 README 模板和复现清单。2021 年后未更新。MIT。📦
- [sysartifacts/sysartifacts.github.io](https://github.com/sysartifacts/sysartifacts.github.io) - EuroSys、SOSP、OSDI、ATC 的 Artifact Evaluation 网站源码，含作者和评审的 AE 指南及历年结果。**未找到 LICENSE 文件。**📦


## 如何做好科研

资深研究者写的科研经验：博客、讲义、演讲和推文串，是通用篇的主要依据。评测方法类的条目放在上面的"研究方法指南"中。只确认了页面标题、未细读正文的条目已在说明中注明"待确认"。

### 综合与经典

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
- [How to come up with research ideas?](https://twitter.com/jbhuang0604/status/1423499757591400448) - Jia-Bin Huang，推文串 2021。七种产生想法的套路：换维度、放宽或增加假设、组合想法、借用新工具、对 SOTA 做压力测试等。🆓
- [How to decide what to work on?](https://twitter.com/jbhuang0604/status/1628521223838654464) - Jia-Bin Huang，推文串 2023。选题看五点：自己的独特优势、兴趣、对未来技术的判断、野心、能否快速验证。🆓
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
- [How I Think About My Research Process: Explore, Understand, Distill](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL/p/hjMy4ZxS5ogA9cTYK) - Neel Nanda，2025。把研究分成选题、探索、理解、提炼四个阶段，各有目标和常见陷阱。同系列的 [Key Mindsets](https://www.alignmentforum.org/posts/cbBwwm4jW6AZctymL) 讲求真、排优先级和快速推进。🆓 `nanda2025process`
- [Practicing AI research](https://www.jasonwei.net/blog/practicing-ai-research) - Jason Wei，2023。研究是可以练习的技能，分为选题、做实验、写论文、扩大影响四部分。🆓 `wei2023practicing`
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) - Andrej Karpathy，2019。训练神经网络的系统流程：先吃透数据，从简单到复杂，每一步都验证假设。🆓 `karpathy2019recipe`
- [How to do experiments?](https://twitter.com/jbhuang0604/status/1647098218172252160) - Jia-Bin Huang，推文串 2023。实验是为了检验假设而不是刷分：一次只改一个变量、先写下预期、建好 baseline、系统记录。🆓
- [How to get unstuck?](https://twitter.com/jbhuang0604/status/1717381151508054029) - Jia-Bin Huang，推文串 2023。大多数实验会失败；卡住时找人讨论、画出流程、逐步简化问题。🆓
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
- [How to write the Introduction?](https://twitter.com/jbhuang0604/status/1638029709073166336) - Jia-Bin Huang，推文串 2023。用 WHAT/WHY/HOW 和五个问题（问题、已有工作、缺口、做了什么、贡献）组织引言。🆓
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
- [Advice on reviewing papers](http://www.pl-enthusiast.net/2014/08/21/advice-reviewing-papers/) - Michael Hicks，PL Enthusiast 2014。PL 社区的审稿建议：如何评估贡献、写出有帮助的评审。同作者另有 [Advice on writing an author response](http://www.pl-enthusiast.net/2014/09/17/advice-writing-author-response/)。🆓 `hicks2014reviewing`
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
- [The illustrated guide to a Ph.D.](https://matt.might.net/articles/phd-school-in-pictures/) - Matt Might，2010。用一组圆形图说明博士就是把人类知识的边界向外推出一个小凸起。另见 [3 qualities of successful Ph.D. students](https://matt.might.net/articles/successful-phd-students/)。🆓 `might2010illustrated`
- [A graduate school survival guide: "So long, and thanks for the Ph.D!"](https://www.cs.unc.edu/~azuma/hitch4.html) - Ronald Azuma，1997（2003 修订）。读博所需的心理韧性和技能，以及毕业后求职。🆓 `azuma2003survival`
- [Expectation Setting for a PhD](https://www.eugenevinitsky.com/posts/expectation-setting) - Eugene Vinitsky，年份待确认。博士生和导师之间如何设定相互期望。🆓 `vinitskyexpectation`
- [How to meet with your advisor?](https://twitter.com/jbhuang0604/status/1653614931202195458) - Jia-Bin Huang，推文串 2023。会前异步分享结果、准备议程、先讲背景再讲细节、主动提出下一步、会后立刻写纪要。🆓
- [How to cope with paper rejection?](https://twitter.com/jbhuang0604/status/1443248831102136333) - Jia-Bin Huang，推文串 2021。被拒是常态；把审稿意见当作改进清单，也可以建一份"失败简历"。🆓
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
