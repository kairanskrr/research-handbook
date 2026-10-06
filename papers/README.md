# 论文索引

- 引用信息：[`references.bib`](references.bib)，下表"key"一列对应其中的条目。
- 下载：在仓库根目录运行 `bash scripts/fetch_papers.sh`，有免费全文的 PDF 会保存为 `papers/pdf/<key>.pdf`。
- 核实日期：2026-10-02 / 2026-10-05。表中"免费全文"一列只列出已确认的合法来源（作者主页、机构库、arXiv、开放获取期刊）。

## 关于 PDF 是否提交进仓库

`papers/pdf/` 默认已加入 `.gitignore`，PDF 不会被提交。原因是各论文的版权不同：
- **可以提交**：开放许可的论文，例如 PRISMA 2009（PLoS，CC BY）、PRISMA 2020（BMJ，CC BY 4.0）、Erren et al. 2007（PLoS，CC BY）、Petersen et al. 2008（出版社版本 CC BY 4.0），以及 PLoS 的 `wilson2014best`、`wilson2017good`、`sandve2013ten`、`mensh2017ten`、`zhang2014ten`、`bourne2005published`、`bourne2006reviewers`（均为 CC BY）。如果要提交，需要用 `git add -f`。
- **不建议提交**：作者主页上的自存档版本、出版社的付费论文。这些只放链接和我们自己写的概括。

## 已收录

| key | 标题 | 出处 | 免费全文 |
|---|---|---|---|
| `ralph2020empirical` | Empirical Standards for Software Engineering Research | arXiv 2020 | [arXiv:2010.03525](https://arxiv.org/abs/2010.03525) |
| `baltes2026guidelines` | Guidelines for Empirical Studies in Software Engineering involving Large Language Models | EMSE 2026 | [arXiv:2508.15503](https://arxiv.org/abs/2508.15503) |
| `kapoor2024reforms` | REFORMS: Consensus-based Recommendations for Machine-learning-based Science | Science Advances 2024 | 出版社页面（下载脚本会尝试） |
| `moher2009prisma` | The PRISMA Statement | PLoS Medicine 2009 | [PLoS](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000097)（CC BY） |
| `page2021prisma` | The PRISMA 2020 statement | BMJ 2021 | [BMJ](https://www.bmj.com/content/372/bmj.n71)（CC BY 4.0） |
| `kitchenham2007guidelines` | Guidelines for performing Systematic Literature Reviews in Software Engineering | 技术报告 2007 | [PDF](https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf) |
| `petersen2008systematic` | Systematic Mapping Studies in Software Engineering | EASE 2008 | [作者主页](https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf)（出版社版本 CC BY 4.0） |
| `petersen2015guidelines` | Guidelines for conducting systematic mapping studies in software engineering: An update | IST 2015 | 💰 见下方"待获取" |
| `wohlin2014guidelines` | Guidelines for snowballing in systematic literature studies and a replication in software engineering | EASE 2014 | [作者主页](https://www.wohlin.eu/ease14.pdf) |
| `wohlin2022successful` | Successful Combination of Database Search and Snowballing for Identification of Primary Studies in Systematic Literature Studies | IST 2022 | [arXiv:2307.02612](https://arxiv.org/abs/2307.02612) |
| `ralph2022paving` | Paving the Way for Mature Secondary Research: The Seven Types of Literature Review | ESEC/FSE 2022 | [arXiv:2205.01163](https://arxiv.org/abs/2205.01163) |
| `shull2008role` | The role of replications in Empirical Software Engineering | EMSE 2008 | 💰 |
| `carver2010towards` | Towards Reporting Guidelines for Experimental Replications: A Proposal | RESER 2010 | [作者主页](https://carver.cs.ua.edu/Papers/Conference/2010/2010_RESER.pdf)（链接会在 http/https 间跳转，脚本失败时请用浏览器下载） |
| `gomez2014understanding` | Understanding replication of experiments in software engineering: A classification | IST 2014 | 💰 |
| `acm2020artifact` | Artifact Review and Badging（v1.1） | ACM 2020 | [网页](https://www.acm.org/publications/policies/artifact-review-and-badging-current) |
| `bird2009promises` | The promises and perils of mining git | MSR 2009 | [Microsoft Research](https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf) |
| `herzig2013bug` | It's not a bug, it's a feature: how misclassification impacts bug prediction | ICSE 2013 | [Saarland](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf)；原地址现无法访问，可用 [Internet Archive 存档](https://web.archive.org/web/2019id_/https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf) |
| `kalliamvakou2014promises` | The promises and perils of mining GitHub | MSR 2014 | [作者主页](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf) |
| `kalliamvakou2016indepth` | An in-depth study of the promises and perils of mining GitHub | EMSE 2016 | [作者主页](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf) |
| `arcuri2011practical` | A practical guide for using statistical tests to assess randomized algorithms in software engineering | ICSE 2011 | 未确认（ACM 上可能免费） |
| `arcuri2014hitchhiker` | A Hitchhiker's guide to statistical tests for assessing randomized algorithms in software engineering | STVR 2014 | [卢森堡大学机构库（作者版本）](https://orbilu.uni.lu/bitstream/10993/1071/1/paper_stvr_icse_2012.pdf) |
| `klees2018evaluating` | Evaluating Fuzz Testing | CCS 2018 | [arXiv:1808.09700](https://arxiv.org/abs/1808.09700) |
| `vanderkouwe2019sok` | SoK: Benchmarking Flaws in Systems Security | EuroS&P 2019 | [作者机构](https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf) |
| `arp2022dos` | Dos and Don'ts of Machine Learning in Computer Security | USENIX Security 2022 | [arXiv:2010.09470](https://arxiv.org/abs/2010.09470) |
| `runeson2009guidelines` | Guidelines for conducting and reporting case study research in software engineering | EMSE 2009 | [Springer](https://doi.org/10.1007/s10664-008-9102-8)（开放获取，CC BY-NC，不提交） |
| `wohlin2024experimentation` | Experimentation in Software Engineering（第 2 版） | Springer 2024 | 💰 |
| `felderer2020contemporary` | Contemporary Empirical Methods in Software Engineering | Springer 2020 | 💰（仅第 17 章开放获取） |
| `zhang2026survey` | A Survey on Large Language Models for Software Engineering | Sci China Inf Sci 2026 | [arXiv:2312.15223](https://arxiv.org/abs/2312.15223)（预印本） |
| `zhang2024unifying` | Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code | TMLR 2024 | [arXiv:2311.07989](https://arxiv.org/abs/2311.07989) |
| `hamming1986you` | You and Your Research | 1986 年演讲 | [文字稿](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html) |
| `erren2007ten` | Ten Simple Rules for Doing Your Best Research, According to Hamming | PLoS Comput Biol 2007 | [PLoS](https://doi.org/10.1371/journal.pcbi.0030213)（CC BY） |
| `schulman2020opinionated` | An Opinionated Guide to ML Research | 博客 2020 | [网页](http://joschu.net/blog/opinionated-guide-ml-research.html) |
| `perez2024tips` | Tips for Empirical Alignment Research | 博客 2024 | [网页](https://www.alignmentforum.org/posts/dZFpEdKyb9Bf4xYn7/tips-for-empirical-alignment-research) |
| `peytonjones2013write` | How to Write a Great Research Paper | 演讲 | [网页](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) |
| `keshav2007read` | How to Read a Paper | ACM SIGCOMM CCR 2007 | [SIGCOMM CCR](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf) |
| `karpathy2016survival` | A Survival Guide to a PhD | 博客 2016 | [网页](http://karpathy.github.io/2016/09/07/phd/) |
| `acm2026csurguidelines` | ACM Computing Surveys: Author Guidelines | ACM 网页 | [Internet Archive 快照](http://web.archive.org/web/20260711105913/https://dl.acm.org/journal/csur/author-guidelines) |
| `huang2021ideas` | How to come up with research ideas? | 推文串 2021 | [链接](https://twitter.com/jbhuang0604/status/1423499757591400448) |
| `huang2023decide` | How to decide what to work on? | 推文串 2023 | [链接](https://twitter.com/jbhuang0604/status/1628521223838654464) |
| `huang2023experiments` | How to do experiments? | 推文串 2023 | [链接](https://twitter.com/jbhuang0604/status/1647098218172252160) |
| `nanda2025mindsets` | My Research Process: Key Mindsets - Truth-Seeking, Prioritisation, Moving Fast | 博客 2025 | [链接](https://www.alignmentforum.org/posts/cbBwwm4jW6AZctymL) |
| `huang2023unstuck` | How to get unstuck? | 推文串 2023 | [链接](https://twitter.com/jbhuang0604/status/1717381151508054029) |
| `huang2023introduction` | How to write the Introduction? | 推文串 2023 | [链接](https://twitter.com/jbhuang0604/status/1638029709073166336) |
| `hicks2014response` | Advice on writing an author response | 博客 2014 | [链接](http://www.pl-enthusiast.net/2014/09/17/advice-writing-author-response/) |
| `huang2021rejection` | How to cope with paper rejection? | 推文串 2021 | [链接](https://twitter.com/jbhuang0604/status/1443248831102136333) |
| `huang2023advisor` | How to meet with your advisors/mentors? | 推文串 2023 | [链接](https://twitter.com/jbhuang0604/status/1653614931202195458) |
| `allea2023european` | The European Code of Conduct for Research Integrity -- Revised Edition 2023 | 准则 2023 | [链接](https://allea.org/wp-content/uploads/2023/06/European-Code-of-Conduct-Revised-Edition-2023.pdf) |
| `might2010successful` | 3 qualities of successful Ph.D. students: Perseverance, tenacity and cogency | 博客 2010 | [链接](https://matt.might.net/articles/successful-phd-students/) |
| `noble2023ten` | Ten simple rules for defining a computational biology project | PLoS Computational Biology 2023 | [链接](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010786) |
| `turingwaydesign` | The Turing Way：Guide for Project Design | 持续更新 | [链接](https://book.the-turing-way.org/project-design/project-design) |
| `noble2009quick` | A Quick Guide to Organizing Computational Biology Projects | PLoS Computational Biology 2009 | [链接](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424) |
| `turingwaycompendia` | The Turing Way：Research Compendia | 持续更新 | [链接](https://book.the-turing-way.org/reproducible-research/compendia) |
| `mineault2021good` | The Good Research Code Handbook | 2021 | [链接](https://goodresearch.dev/) |
| `osforganizing` | OSF Help：Organizing Files | 持续更新 | [链接](https://help.osf.io/article/147-organizing-files) |
| `mlflowtracking` | MLflow Tracking | MLflow 官方文档（工具文档） | [链接](https://mlflow.org/docs/latest/ml/tracking/) |
| `bird2009fair` | Fair and Balanced? Bias in Bug-Fix Datasets | ESEC/FSE 2009 | [链接](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009fbb.pdf) |
| `cra1999evaluating` | Evaluating Computer Scientists and Engineers for Promotion and Tenure | 1999 | [链接](https://cra.org/resources/best-practice-memos/evaluating-computer-scientists-and-engineers-for-promotion-and-tenure/) |
| `vardi2009conferences` | Conferences vs. Journals in Computing Research | CACM 2009 | [链接](https://cacm.acm.org/opinion/conferences-vs-journals-in-computing-research/) |
| `fortnow2009time` | Time for Computer Science to Grow Up | CACM 2009 | [链接](https://cacm.acm.org/magazines/2009/8/34492-viewpoint-time-for-computer-science-to-grow-up/fulltext) |
| `sysartifactsguide` | sysartifacts：系统会议制品评估指南 | 持续更新 | [链接](https://sysartifacts.github.io/) |
| `usenixsec2026cfp` | USENIX Security '26 Call for Papers | 2026 | [链接](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| `neurips2025cfp` | NeurIPS 2025 Call for Papers | 2025 | [链接](https://neurips.cc/Conferences/2025/CallForPapers) |
| `sainz2023nlp` | NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark | Findings of EMNLP 2023 | [链接](https://arxiv.org/abs/2310.18018) |
| `aaronson2008ten` | Ten Signs a Claimed Mathematical Breakthrough is Wrong | Shtetl-Optimized (blog) 2008 | [链接](https://scottaaronson.blog/?p=304) |
| `alexopoulos2002output` | Output Data Analysis for Simulations | Proceedings of the 2002 Winter Simulatio 2002 | [链接](https://www.informs-sim.org/wsc02papers/012.pdf) |
| `braun2006using` | Using thematic analysis in psychology | Qualitative Research in Psychology 2006 | [链接](https://doi.org/10.1191/1478088706qp063oa) |
| `defranca2015simulation` | Simulation Based Studies in Software Engineering: A Matter of Validity | CLEI Electronic Journal 2015 | [链接](https://www.clei.org/cleiej/index.php/cleiej/article/view/54) |
| `easterbrook2008selecting` | Selecting Empirical Methods for Software Engineering Research | Guide to Advanced Empirical Software Eng 2008 | [链接](https://doi.org/10.1007/978-1-84800-044-5_11) |
| `falessi2018empirical` | Empirical Software Engineering Experts on the Use of Students and Professionals in Experiments | Empirical Software Engineering 2018 | [链接](https://bura.brunel.ac.uk/handle/2438/14575) |
| `graziotin2021psychometrics` | Psychometrics in Behavioral Software Engineering: A Methodological Introduction with Guidelines | ACM Transactions on Software Engineering 2021 | [链接](https://arxiv.org/abs/2005.09959) |
| `gundersen2018state` | State of the Art: Reproducibility in Artificial Intelligence | Proceedings of the Thirty-Second AAAI Co 2018 | [链接](https://ojs.aaai.org/index.php/AAAI/article/view/11503) |
| `kallio2016systematic` | Systematic methodological review: developing a framework for a qualitative semi-structured interview guide | Journal of Advanced Nursing 2016 | [链接](https://doi.org/10.1111/jan.13031) |
| `kapoor2023leakage` | Leakage and the reproducibility crisis in machine-learning-based science | Patterns 2023 | [链接](https://doi.org/10.1016/j.patter.2023.100804) |
| `kehr2015quantitative` | Quantitative Longitudinal Research: A Review of IS Literature, and a Set of Methodological Guidelines | Proceedings of the 23rd European Confere 2015 | [链接](https://aisel.aisnet.org/ecis2015_cr/94) |
| `ko2015practical` | A Practical Guide to Controlled Experiments of Software Engineering Tools with Human Participants | Empirical Software Engineering 2015 | [链接](https://faculty.washington.edu/ajko/papers/Ko2013SEToolEvaluations.pdf) |
| `lamport1995how` | How to Write a Proof | The American Mathematical Monthly 1995 | [链接](https://lamport.azurewebsites.net/pubs/lamport-how-to-write.pdf) |
| `lamport2012how` | How to Write a 21st Century Proof | Journal of Fixed Point Theory and Applic 2012 | [链接](https://lamport.azurewebsites.net/pubs/proof.pdf) |
| `mcdonald2019reliability` | Reliability and Inter-rater Reliability in Qualitative Research: Norms and Guidelines for CSCW and HCI Practice | Proceedings of the ACM on Human-Computer 2019 | [链接](https://doi.org/10.1145/3359174) |
| `melegati2020case` | Case Survey Studies in Software Engineering Research | Proceedings of the 14th ACM / IEEE Inter 2020 | [链接](https://doi.org/10.1145/3382494.3410683) |
| `molleri2020empirically` | An Empirically Evaluated Checklist for Surveys in Software Engineering | Information and Software Technology 2020 | [链接](https://arxiv.org/abs/1901.09850) |
| `pineau2021improving` | Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program) | Journal of Machine Learning Research 2021 | [链接](https://jmlr.org/papers/v22/20-303.html) |
| `santos2011action` | Action Research Can Swing the Balance in Experimental Software Engineering | Advances in Computers 2011 | [链接](https://arxiv.org/abs/1306.2414) |
| `sargent2010verification` | Verification and Validation of Simulation Models | Proceedings of the 2010 Winter Simulatio 2010 | [链接](https://www.informs-sim.org/wsc10papers/016.pdf) |
| `sharp2016role` | The Role of Ethnographic Studies in Empirical Software Engineering | IEEE Transactions on Software Engineerin 2016 | [链接](https://doi.org/10.1109/TSE.2016.2519887) |
| `shepperd2018inferencing` | Inferencing into the Void: Problems with Implicit Populations. Comments on ``Empirical Software Engineering Experts on the Use of Students and Professionals in Experiments'' | 2018 | [链接](https://arxiv.org/abs/1810.07392) |
| `staron2025guidelines` | Guidelines for Conducting Action Research Studies in Software Engineering | e-Informatica Software Engineering Journ 2025 | [链接](https://www.e-informatyka.pl/EISEJ/papers/2025/1/5/) |
| `stol2016grounded` | Grounded Theory in Software Engineering Research: A Critical Review and Guidelines | Proceedings of the 38th International Co 2016 | [链接](https://hdl.handle.net/10344/5396) |
| `storey2020who` | The who, what, how of software engineering research: a socio-technical framework | Empirical Software Engineering 2020 | [链接](https://doi.org/10.1007/s10664-020-09858-z) |
| `taocareer` | Career Advice | What's new (blog)  | [链接](https://terrytao.wordpress.com/career-advice/) |
| `taowriting` | On Writing | What's new (blog)  | [链接](https://terrytao.wordpress.com/advice-on-writing-papers/) |
| `torchiano2017lessons` | Lessons Learnt in Conducting Survey Research | Proceedings of the 5th IEEE/ACM Internat 2017 | [链接](https://arxiv.org/abs/1702.05744) |
| `wagner2020challenges` | Challenges in Survey Research | Contemporary Empirical Methods in Softwa 2020 | [链接](https://arxiv.org/abs/1908.05899) |
| `wohlin2021case` | Case Study Research in Software Engineering---It is a Case, and it is a Study, but is it a Case Study? | Information and Software Technology 2021 | [链接](https://doi.org/10.1016/j.infsof.2021.106514) |
| `oecd2015frascati` | Frascati Manual 2015 | OECD 2015 | [OECD](https://doi.org/10.1787/9789264239012-en) |
| `nielsen2004principles` | Principles of Effective Research | 技术笔记 2004 | [Internet Archive 快照](https://web.archive.org/web/20260824165302/https://michaelnielsen.org/blog/principles-of-effective-research/)（原地址已失效） |
| `patterson2001bad` | How to Have a Bad Career in Research/Academia | 演讲 2001 | [作者主页](https://people.eecs.berkeley.edu/~pattrsn/talks/BadCareer.pdf) |
| `sutherland1996courage` | Technology and Courage | Sun Labs Perspectives 1996 | 第三方托管的 PDF（未加入下载脚本） |
| `feynman1974cargo` | Cargo Cult Science | Caltech 演讲 1974 | [Caltech](https://calteches.library.caltech.edu/51/2/CargoCult.htm) |
| `freeman2013research` | How to do research | 讲义 2013 | [作者主页](https://people.csail.mit.edu/billf/publications/How_To_Do_Research.pdf) |
| `durandgoodresearch` | Do Good Research! | 演讲（年份待确认） | [作者主页](http://people.csail.mit.edu/fredo/DoGoodResearch.pdf) |
| `ruder2020tips` | 10 Tips for Research and a PhD | 博客 2020 | [网页](https://www.ruder.io/10-tips-for-research-and-a-phd/) |
| `carlini2026best` | How to win a best paper award (or, an opinionated take on how to do important research that matters) | 博客 2026 | [网页](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html) |
| `shaw2002makes` | What Makes Good Research in Software Engineering? | STTT 2002 | [作者主页](https://www.cs.cmu.edu/~Compose/ftp/shaw-fin-etaps.pdf) |
| `zeller2012good` | What makes good research? | 博客 2012 | [网页](https://andreas-zeller.info/2012/10/16/what-makes-good-research.html) |
| `lipton2019troubling` | Troubling Trends in Machine Learning Scholarship | ACM Queue 2019 | [arXiv:1807.03341](https://arxiv.org/abs/1807.03341) |
| `ousterhout2021sayings` | Favorite Sayings | 网页 | [网页](https://web.stanford.edu/~ouster/cgi-bin/sayings.php) |
| `kidger2023know` | Just know stuff (Or, how to achieve success in a machine learning PhD) | 博客 2023 | [网页](https://kidger.site/thoughts/just-know-stuff/) |
| `alon2009choose` | How To Choose a Good Scientific Problem | Molecular Cell 2009 | 未确认（出版社页面有反爬，只找到第三方镜像） |
| `olah2021taste` | Research Taste Exercises | 博客 2021 | [网页](https://colah.github.io/notes/taste/) |
| `nanda2025taste` | My Research Process: Understanding and Cultivating Research Taste | 博客 2025 | [网页](https://www.alignmentforum.org/posts/Ldrss6o3tiKT6NdMm) |
| `eisnerproblems` | How to Find Research Problems | 网页 | [网页](https://www.cs.jhu.edu/~jason/advice/how-to-find-research-problems.html) |
| `sutton2019bitter` | The Bitter Lesson | 博客 2019 | [网页](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) |
| `yao2025second` | The Second Half | 博客 2025 | [网页](https://ysymyth.github.io/The-Second-Half/) |
| `wei2022enjoy` | Research I enjoy | 博客 2022 | [网页](https://www.jasonwei.net/blog/research-i-enjoy) |
| `dettmers2019creativity` | Creativity in Academia | 博客 2019 | [网页](https://timdettmers.com/2019/09/03/creativity-in-academia/) |
| `carlini2024logfile` | My research idea logfile, 2016-2019 | 博客 2024 | [网页](https://nicholas.carlini.com/writing/2024/my-research-logfile.html) |
| `hicks2020impact` | Increasing the Impact of PL Research | 博客 2020 | [网页](http://www.pl-enthusiast.net/2020/07/29/increasing-the-impact-of-pl-research/) |
| `steinhardt2018stochastic` | Research as a Stochastic Decision Process | 博客 2018 | [网页](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html) |
| `nanda2025process` | How I Think About My Research Process: Explore, Understand, Distill | 博客 2025 | [网页](https://www.alignmentforum.org/s/5GT3yoYM9gRmMEKqL/p/hjMy4ZxS5ogA9cTYK) |
| `wei2023practicing` | Practicing AI research | 博客 2023 | [网页](https://www.jasonwei.net/blog/practicing-ai-research) |
| `karpathy2019recipe` | A Recipe for Training Neural Networks | 博客 2019 | [网页](https://karpathy.github.io/2019/04/25/recipe/) |
| `carlini2022rapid` | Rapid Iteration in Machine Learning Research | 博客 2022 | [网页](https://nicholas.carlini.com/writing/2022/rapid-iteration-machine-learning-research.html) |
| `vinitskyrules` | Personal Rules of Productive Research | 博客 | [网页](https://www.eugenevinitsky.com/posts/personal-rules-of-productive-research) |
| `parikh2018calendar` | Calendar. Not to-do lists. | 博客 2018 | [网页](https://deviparikh.substack.com/p/calendar-in-stead-of-to-do-lists-9ada86a512dd) |
| `eisnerread` | How to Read a Technical Paper | 网页 | [网页](https://www.cs.jhu.edu/~jason/advice/how-to-read-a-paper.html) |
| `griswoldread` | How to Read an Engineering Research Paper | 网页 | [网页](https://cseweb.ucsd.edu/~wgg/CSE210/howtoread.html) |
| `bender2003critical` | Critical Reading | 讲义 | [作者主页](https://faculty.washington.edu/ebender/critical_reading.pdf) |
| `vinitskypaper` | Ways to Engage Deeply with a Paper | 博客 | [网页](https://www.eugenevinitsky.com/posts/paper-games) |
| `shaw2003writing` | Writing Good Software Engineering Research Papers | ICSE 2003 | [作者主页](https://www.cs.cmu.edu/~Compose/shaw-icse03.pdf) |
| `ernstwrite` | How to write a technical paper | 网页 | [网页](https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html) |
| `widomtips` | Tips for Writing Technical Papers | 网页 | [网页](https://cs.stanford.edu/people/widom/paper-writing.html) |
| `eisnerfirst` | Write the Paper First | 网页 2010 | [网页](https://www.cs.jhu.edu/~jason/advice/write-the-paper-first.html) |
| `whitesides2004writing` | Whitesides' Group: Writing a Paper | Advanced Materials 2004 | 未确认（只找到第三方镜像） |
| `raibert1985good` | Good Writing | 短文 1985 | [网页](http://www.cs.cmu.edu/~pausch/Randy/Randy/raibert.htm) |
| `vandeursen2013writing` | Some Research Paper Writing Recommendations | 博客 2013 | [网页](https://avandeursen.com/2013/07/10/research-paper-writing-recommendations/) |
| `levin1983sosp` | An Evaluation of the Ninth SOSP Submissions; or, How (and How Not) to Write a Good Systems Paper | ACM SIGOPS OSR 1983 | [USENIX](https://www.usenix.org/legacy/events/samples/submit/advice.html) |
| `allman2001plea` | A Referee's Plea | 短文 2001 | [作者主页](https://mallman.net/plea.txt) |
| `gutmann2008security` | HOWTO: Avoid common problems when writing a security conference paper | 邮件列表 2008 | [网页](https://www.metzdowd.com/pipermail/cryptography/2008-January/013419.html) |
| `nanda2025writing` | Highly Opinionated Advice on How to Write ML Papers | 博客 2025 | [网页](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) |
| `black2024writing` | Writing a good scientific paper | 博客 2024 | [网页](https://perceiving-systems.blog/en/news/writing-a-good-scientific-paper) |
| `parikh2019planning` | Planning paper writing | 博客 2019 | [网页](https://deviparikh.substack.com/p/planning-paper-writing-553f497e8839) |
| `olah2017debt` | Research Debt | Distill 2017 | [Distill](https://distill.pub/2017/research-debt/) |
| `durandwriting` | Notes on writing | 讲义 | [作者主页](http://people.csail.mit.edu/fredo/PUBLI/writing.pdf) |
| `mensh2017ten` | Ten simple rules for structuring papers | PLoS Comput Biol 2017 | [PLoS](https://doi.org/10.1371/journal.pcbi.1005619)（CC BY） |
| `zhang2014ten` | Ten Simple Rules for Writing Research Papers | PLoS Comput Biol 2014 | [PLoS](https://doi.org/10.1371/journal.pcbi.1003453)（CC BY） |
| `bourne2005published` | Ten Simple Rules for Getting Published | PLoS Comput Biol 2005 | [PLoS](https://doi.org/10.1371/journal.pcbi.0010057)（CC BY） |
| `ernstreview` | Reviewing a technical paper | 网页 | [网页](https://homes.cs.washington.edu/~mernst/advice/review-technical-paper.html) |
| `roscoe2007reviews` | Writing reviews for systems conferences | 短文 2007 | [作者主页](https://people.inf.ethz.ch/troscoe/pubs/review-writing.pdf) |
| `allman2008thoughts` | Thoughts on Reviewing | ACM SIGCOMM CCR 2008 | [作者主页](https://mallman.net/pubs/All08a/All08a.pdf) |
| `hicks2014reviewing` | Advice on reviewing papers | 博客 2014 | [网页](http://www.pl-enthusiast.net/2014/08/21/advice-reviewing-papers/) |
| `zeller2012rebuttals` | Patterns for writing good rebuttals | 博客 2012 | [网页](https://andreas-zeller.info/2012/10/01/patterns-for-writing-good-rebuttals.html) |
| `zeller2021fields` | How do different fields review papers? Experiences from ICSE, PLDI, and CCS | 博客 2021 | [网页](https://andreas-zeller.info/2021/07/27/Reviewing-across-fields-ICSE-PLDI-CCS.html) |
| `parikh2020rebuttals` | How we write rebuttals | 博客 2020 | [网页](https://deviparikh.substack.com/p/how-we-write-rebuttals-dc84742fece1) |
| `black2022novelty` | Novelty in Science: A guide for reviewers | 博客 2022 | [网页](https://perceiving-systems.blog/en/news/novelty-in-science) |
| `mightreview` | How to peer review scientific work | 博客 | [网页](https://matt.might.net/articles/how-to-peer-review/) |
| `bourne2006reviewers` | Ten Simple Rules for Reviewers | PLoS Comput Biol 2006 | [PLoS](https://doi.org/10.1371/journal.pcbi.0020110)（CC BY） |
| `ernsttalk` | Giving a technical presentation | 网页 | [网页](https://homes.cs.washington.edu/~mernst/advice/giving-talk.html) |
| `winston2018speak` | How to Speak | 讲座 2018 | [视频](https://www.youtube.com/watch?v=Unzc731iCUY) |
| `fatahalian2023talks` | Tips for Giving Clear Talks | 幻灯片 2023 | [作者主页](http://graphics.stanford.edu/~kayvonf/misc/cleartalktips.pdf) |
| `kim2019talk` | Assembling A Talk: Two Wrong Ways and a Right Way | 短文 2019 | [作者主页](http://www.tkim.graphics/HOWTOTALK/HowToTalk.pdf) |
| `hilltalk` | Oral Presentation Advice | 网页 | [网页](https://pages.cs.wisc.edu/~markhill/conference-talk.html) |
| `hicks2019talk` | How to Write a Conference Talk | 博客 2019 | [网页](http://www.pl-enthusiast.net/2019/01/02/how-to-write-a-conference-talk/) |
| `dahlin2006badtalk` | How to Give a Bad Talk | 幻灯片 2006 | [作者主页](https://www.cs.utexas.edu/~dahlin/professional/badTalk.pdf) |
| `dredze2012successful` | How to Be a Successful PhD Student (in Computer Science (in NLP/ML)) | 指南 2012（v1.2 2022） | [作者主页](https://www.cs.jhu.edu/~mdredze/publications/HowtoBeaSuccessfulPhDStudent.1_2.pdf) |
| `halimtips` | Prof Halim's PhD Tips | 网页 | [网页](https://www.comp.nus.edu.sg/~stevenha/myresearch/phd_tips.html) |
| `wood2020five` | Five tips for starting (and continuing) a PhD | 博客 2020 | [网页](https://blogs.ed.ac.uk/ellie-wood/2020/09/04/five-tips-for-starting-and-continuing-a-phd/) |
| `prieto2025so` | A PhD So Good It Can't Be Ignored: Passion, Practice, and Control | 博客 2025 | [网页](https://ahappyphd.org/posts/phd-so-good-1/) |
| `herremans2020successful` | How to be a successful PhD student? | 博客 2020 | [网页](https://medium.com/data-science/how-to-be-a-successful-phd-student-3f3a4eb48be8) |
| `kuroseadvice` | 10 pieces of advice I wish my PhD advisor had given me | 幻灯片 | [ACM SIGCOMM Education](https://www.sigcommedu.web.illinois.edu/advice/kurose_wish_advisor.pdf) |
| `might2010illustrated` | The illustrated guide to a Ph.D. | 博客 2010 | [网页](https://matt.might.net/articles/phd-school-in-pictures/) |
| `azuma2003survival` | A graduate school survival guide: "So long, and thanks for the Ph.D!" | 短文 1997/2003 | [网页](https://www.cs.unc.edu/~azuma/hitch4.html) |
| `vinitskyexpectation` | Expectation Setting for a PhD | 博客 | [网页](https://www.eugenevinitsky.com/posts/expectation-setting) |
| `huang2021struggle` | Behind the Scenes: The Struggle for Each Paper | 博客 2021 | [网页](https://jeffhuang.com/struggle_for_each_paper/) |
| `wei2025maxperf` | AI research is a max-performance domain | 博客 2025 | [网页](https://jasonwei.net/blog/ai-research-is-a-max-performance-domain) |
| `harcholbalter2014applying` | Applying to Ph.D. Programs in Computer Science | 指南 2014 | [作者主页](https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf) |
| `dettmers2022grad` | How to Choose Your Grad School | 博客 2022 | [网页](https://timdettmers.com/2022/03/13/how-to-choose-your-grad-school/) |
| `blackburn2018sigplan` | SIGPLAN Empirical Evaluation Guidelines | ACM SIGPLAN 2018 | [SIGPLAN](https://www.sigplan.org/Resources/EmpiricalEvaluation/) |
| `heiserbenchmarking` | Gernot's List of Systems Benchmarking Crimes | 网页 | [网页](https://gernot-heiser.org/benchmarking-crimes.html) |
| `zeller2021devil` | The Devil's Guide to Incremental Research | 博客 2021 | [网页](https://andreas-zeller.info/2021/04/15/the-devils-guide-to-incremental-research.html) |
| `menzies2019bad` | "Bad smells" in software analytics papers | IST 2019 | [arXiv:1803.05518](https://arxiv.org/abs/1803.05518) |
| `lones2021avoid` | How to avoid machine learning pitfalls: a guide for academic researchers | arXiv 2021 | [arXiv:2108.02497](https://arxiv.org/abs/2108.02497) |
| `carlini2019evaluating` | On Evaluating Adversarial Robustness | arXiv 2019 | [arXiv:1902.06705](https://arxiv.org/abs/1902.06705) |
| `wei2024evals` | Successful language model evals | 博客 2024 | [网页](https://jasonwei.net/blog/evals) |
| `mytkowicz2009producing` | Producing wrong data without doing anything obviously wrong! | ASPLOS 2009 | 未确认 |
| `georges2007statistically` | Statistically rigorous Java performance evaluation | OOPSLA 2007 | [合作者主页](https://dri.es/files/oopsla07-georges.pdf) |
| `kalibera2013rigorous` | Rigorous benchmarking in reasonable time | ISMM 2013 | [肯特大学机构库（作者接受稿）](https://kar.kent.ac.uk/33611/) |
| `blackburn2008wake` | Wake up and smell the coffee: evaluation methodology for the 21st century | CACM 2008 | 未确认 |
| `hoefler2015scientific` | Scientific benchmarking of parallel computing systems | SC 2015 | [作者主页](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf) |
| `baltes2022sampling` | Sampling in software engineering research: a critical review and guidelines | EMSE 2022 | [arXiv:2002.07764](https://arxiv.org/abs/2002.07764) |
| `siegmund2015views` | Views on Internal and External Validity in Empirical Software Engineering | ICSE 2015 | 未确认 |
| `herley2017sok` | SoK: Science, Security and the Elusive Goal of Security as a Scientific Pursuit | IEEE S&P 2017 | 未确认 |
| `bailey2012menlo` | The Menlo Report | IEEE S&P 2012 | [CAIDA](https://www.caida.org/publications/papers/2012/menlo_report/menlo_report.pdf) |
| `partridge2016ethical` | Ethical considerations in network measurement papers | CACM 2016 | 未确认 |
| `wilson2014best` | Best Practices for Scientific Computing | PLoS Biology 2014 | [PLoS](https://doi.org/10.1371/journal.pbio.1001745)（CC BY） |
| `wilson2017good` | Good enough practices in scientific computing | PLoS Comput Biol 2017 | [PLoS](https://doi.org/10.1371/journal.pcbi.1005510)（CC BY） |
| `sandve2013ten` | Ten Simple Rules for Reproducible Computational Research | PLoS Comput Biol 2013 | [PLoS](https://doi.org/10.1371/journal.pcbi.1003285)（CC BY） |
| `carlini2022checklist` | Research Paper Release Checklist | 博客 2022 | [网页](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) |
| `amsculture2004joint` | The Culture of Research and Scholarship in Mathematics: Joint Research and Its Publication | AMS statement 2004 | [链接](https://www.ams.org/profession/leaders/CultureStatement04.pdf) |
| `amsculture2006rates` | The Culture of Research and Scholarship in Mathematics: Rates of Publication | AMS statement 2006 | [链接](https://www.ams.org/profession/leaders/culture/CultureStatement06.pdf) |
| `ams2022ethical` | Policy Statement on Ethical Guidelines | AMS 政策声明 2022 | [链接](https://www.ams.org/about-us/governance/policy-statements/sec-ethics) |
| `thurston1994proof` | On Proof and Progress in Mathematics | Bulletin of the American Mathematical Society 1994 | [链接](https://arxiv.org/abs/math/9404236) |
| `stodden2013setting` | Setting the Default to Reproducible: Reproducibility in Computational and Experimental Mathematics | Institute for Computational and Experimental Research in Mathematics (ICERM) 2013 | [链接](https://icerm.brown.edu/topical_workshops/tw12-5-rcem/icerm_report.pdf) |
| `arxivendorsement` | The arXiv Endorsement System | arXiv help page | [链接](https://info.arxiv.org/help/endorsement.html) |
| `arxivmoderation` | Content Moderation | arXiv help page | [链接](https://info.arxiv.org/help/moderation/index.html) |
| `aps2024ethics` | APS Ethics Standards | 网页 2024 | [链接](https://www.aps.org/about/governance/policies-procedures/ethics-standards) |
| `apsdataavailability` | Guidelines for Data Availability Statements in Physical Review | 网页 2024 | [链接](https://journals.aps.org/authors/data-availability-statements) |
| `aassoftware` | Policy Statement on Software | 网页 | [链接](https://journals.aas.org/policy-statement-on-software/) |
| `arxivabout` | About arXiv | 网页 | [链接](https://info.arxiv.org/about/index.html) |
| `arxivtaxonomy` | Category Taxonomy | 网页 | [链接](https://arxiv.org/category_taxonomy) |
| `ginsparg2011twenty` | It was twenty years ago today ... | arXiv:1108.2700 2011 | [链接](https://arxiv.org/abs/1108.2700) |
| `junk2021reproducibility` | Reproducibility and Replication of Experimental Particle Physics Results | arXiv:2009.06864 2020 | [链接](https://arxiv.org/abs/2009.06864) |
| `lyons2013discovering` | Discovering the Significance of 5 sigma | arXiv:1310.1284 2013 | [链接](https://arxiv.org/abs/1310.1284) |
| `roodman2003blind` | Blind Analysis in Particle Physics | arXiv:physics/0312102 2003 | [链接](https://arxiv.org/abs/physics/0312102) |
| `golub2023blind` | Blind analysis in Physics experiments: Is this trip necessary? | arXiv:2311.13542 2023 | [链接](https://arxiv.org/abs/2311.13542) |
| `ligo2018publication` | LIGO Scientific Collaboration Publication and Presentation Policy | 网页 2018 | [链接](https://dcc.ligo.org/public/0026/T010168/010/T010168-10.pdf) |
| `cern2020opendata` | CERN Open Data Policy for the LHC Experiments | 网页 2020 | [链接](https://opendata.cern.ch/docs/cern-open-data-policy-for-lhc-experiments) |
| `perciedusert2020arrive` | The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research | PLoS Biology 2020 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000410) |
| `perciedusert2020reporting` | Reporting animal research: Explanation and elaboration for the ARRIVE guidelines 2.0 | PLoS Biology 2020 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000411) |
| `vaux2012replicates` | Replicates and repeats–-what is the difference and is it significant? A brief discussion of statistics and experimental design | EMBO Reports 2012 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC3321166/) |
| `schnell2015ten` | Ten Simple Rules for a Computational Biologist's Laboratory Notebook | PLoS Computational Biology 2015 | [链接](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004385) |
| `tscharntke2007author` | Author Sequence and Credit for Contributions in Multiauthored Publications | PLoS Biology 2007 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0050018) |
| `freedman2015economics` | The Economics of Reproducibility in Preclinical Research | PLoS Biology 2015 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002165) |
| `errington2021investigating` | Investigating the replicability of preclinical cancer biology | eLife 2021 | [链接](https://elifesciences.org/articles/71601) |
| `errington2021challenges` | Challenges for assessing replicability in preclinical cancer biology | eLife 2021 | [链接](https://elifesciences.org/articles/67995) |
| `nihrigorguidance` | Guidance: Rigor and Reproducibility in Grant Applications | 网页 | [链接](https://grants.nih.gov/policy/reproducibility/guidance.htm) |
| `nc3rsthe3rs` | The 3Rs | 网页 | [链接](https://nc3rs.org.uk/who-we-are/3rs) |
| `biorxivabout` | About bioRxiv | 网页 | [链接](https://www.biorxiv.org/about-biorxiv) |
| `plosdatapolicy` | Data Availability | 网页 | [链接](https://journals.plos.org/plosone/s/data-availability) |
| `ieee2026pspb` | IEEE Publication Services and Products Board Operations Manual | IEEE 2026 | [链接](https://pspb.ieee.org/images/files/files/opsmanual.pdf) |
| `ieeeauthorposting` | Post-Publication Policies | IEEE Author Center Journals 2026 | [链接](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/post-publication-policies/) |
| `ieeeauthorsubmission` | Submission and Peer Review Policies | IEEE Author Center Journals 2026 | [链接](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/) |
| `ieeeauthorreproducibility` | Research Reproducibility | IEEE Author Center Journals 2026 | [链接](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/) |
| `ojspreproducibility` | Author Instructions for OJSP Reproducibility Review | IEEE Signal Processing Society 网页 2025 | [链接](https://signalprocessingsociety.org/publications-resources/ieee-open-journal-signal-processing/author-instructions-ojsp-reproducibility) |
| `vandewalle2009reproducible` | Reproducible Research in Signal Processing | IEEE Signal Processing Magazine 2009 | [链接](https://infoscience.epfl.ch/record/136640) |
| `barba2018terminologies` | Terminologies for Reproducible Research | arXiv:1802.03311 2018 | [链接](https://arxiv.org/abs/1802.03311) |
| `lamela2019repeatable` | Repeatable and Reproducible Wireless Networking Experimentation through Trace-based Simulation | arXiv:1903.12033 2019 | [链接](https://arxiv.org/abs/1903.12033) |
| `shackelford2005computing` | Computing Curricula 2005: The Overview Report | ACM, AIS, and IEEE Computer Society 2005 | [链接](https://www.acm.org/binaries/content/assets/education/curricula-recommendations/cc2005-march06final.pdf) |
| `rutgersinventionfaq` | Inventions and Commercialization FAQs | Rutgers University 网页 2026 | [链接](https://research.rutgers.edu/faculty-staff/inventions-commercialization/faqs) |
| `berkeleydisclose` | When to Disclose an Invention to OTL | UC Berkeley IPIRA 网页 2026 | [链接](https://ipira.berkeley.edu/researchers/intellectual-property-protection/when-disclose-invention-otl) |
| `utahprotecting` | Protecting Your Research: A Guide to IP Disclosure and Grant Compliance at the University of Utah | University of Utah 网页 2026 | [链接](https://technologylicensing.utah.edu/news-events/resources-opportunities/protecting-your-research) |
| `europracticempw` | MPW Prototyping | Europractice 网页 2026 | [链接](https://europractice-ic.com/mpw-prototyping/) |
| `ieeesadevelop` | Develop Standards | IEEE SA 网页 2026 | [链接](https://standards.ieee.org/develop/) |
| `3gpp2026about` | About 3GPP | 3GPP 网页 2026 | [链接](https://www.3gpp.org/about-us) |
| `wma2024helsinki` | WMA Declaration of Helsinki – Ethical Principles for Medical Research Involving Human Participants | 网页 2024 | [链接](https://www.wma.net/policies-post/wma-declaration-of-helsinki/) |
| `icmje2026recommendations` | Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals | 网页 2026 | [链接](https://www.icmje.org/icmje-recommendations.pdf) |
| `hopewell2025consort` | CONSORT 2025 statement: Updated guideline for reporting randomised trials | PLOS Medicine 2025 | [链接](https://doi.org/10.1371/journal.pmed.1004587) |
| `vonelm2007strobe` | The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) Statement: Guidelines for Reporting Observational Studies | PLoS Medicine 2007 | [链接](https://doi.org/10.1371/journal.pmed.0040296) |
| `vandenbroucke2007strobe` | Strengthening the Reporting of Observational Studies in Epidemiology (STROBE): Explanation and Elaboration | PLoS Medicine 2007 | [链接](https://doi.org/10.1371/journal.pmed.0040297) |
| `gagnier2013care` | The CARE guidelines: consensus-based clinical case reporting guideline development | Journal of Medical Case Reports 2013 | [链接](https://doi.org/10.1186/1752-1947-7-223) |
| `murad2016new` | New evidence pyramid | Evidence-Based Medicine 2016 | [链接](https://doi.org/10.1136/ebmed-2016-110401) |
| `ioannidis2005why` | Why Most Published Research Findings Are False | PLoS Medicine 2005 | [链接](https://doi.org/10.1371/journal.pmed.0020124) |
| `equatorreporting` | About Us; What Is a Reporting Guideline? | 网页 | [链接](https://www.equator-network.org/about-us/) |
| `osc2015estimating` | Estimating the Reproducibility of Psychological Science | Science 2015 | [链接](https://discovery.dundee.ac.uk/ws/files/7385883/RPP_SCIENCE_2015.pdf) |
| `nelson2018psychology` | Psychology's Renaissance | Annual Review of Psychology 2018 | [链接](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/05/Nelson-Simmons-Simonsohn-2018.pdf) |
| `simmons2018false` | False-Positive Citations | Perspectives on Psychological Science 2018 | [链接](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/02/26-Simmons-Nelson-Simonsohn-2018.pdf) |
| `nosek2018preregistration` | The Preregistration Revolution | Proceedings of the National Academy of Sciences 2018 | [链接](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5856500/) |
| `chambers2022past` | The Past, Present and Future of Registered Reports | Nature Human Behaviour 2022 | [链接](https://orca.cardiff.ac.uk/id/eprint/145541/1/Chambers%26Tzavella2021-MS.pdf) |
| `henrich2010weirdest` | The Weirdest People in the World? | Behavioral and Brain Sciences 2010 | [链接](https://www.konsortswd.de/wp-content/uploads/RatSWD_WP_139.pdf) |
| `apa2017ethical` | Ethical Principles of Psychologists and Code of Conduct (2002, amended effective June 1, 2010, and January 1, 2017) | 网页 2017 | [链接](https://www.apa.org/ethics/code/ethics-code-2017.pdf) |
| `appelbaum2018journal` | Journal Article Reporting Standards for Quantitative Research in Psychology: The APA Publications and Communications Board Task Force Report | American Psychologist 2018 | [链接](https://www.apa.org/pubs/journals/releases/amp-amp0000191.pdf) |
| `apajars` | Journal Article Reporting Standards (JARS) | APA Style 网页 2025 | [链接](https://apastyle.apa.org/jars) |
| `apastyleabout` | About APA Style | APA Style 网页 2023 | [链接](https://apastyle.apa.org/about-apa-style) |
| `cosregisteredreports` | Registered Reports | Center for Open Science 网页 2026 | [链接](https://www.cos.io/initiatives/registered-reports) |
| `lakens2022sample` | Sample Size Justification | Collabra: Psychology 2022 | [链接](https://osf.io/preprints/psyarxiv/9d3yf/) |
| `flake2020measurement` | Measurement Schmeasurement: Questionable Measurement Practices and How to Avoid Them | Advances in Methods and Practices in Psychological Science 2020 | [链接](https://osf.io/preprints/psyarxiv/hs7wm/) |
| `angrist2010credibility` | The Credibility Revolution in Empirical Economics: How Better Research Design Is Taking the Con out of Econometrics | Journal of Economic Perspectives 2010 | [链接](https://www.nber.org/system/files/working_papers/w15794/w15794.pdf) |
| `cochrane2005writing` | Writing Tips for Ph.D. Students | 网页 2005 | [链接](https://www.johnhcochrane.com/s/phd_paper_writing.pdf) |
| `varian1997build` | How to Build an Economic Model in Your Spare Time | The American Economist 1997 | [链接](https://people.ischool.berkeley.edu/~hal/Papers/how.pdf) |
| `brodeur2016star` | Star Wars: The Empirics Strike Back | American Economic Journal: Applied Economics 2016 | [链接](https://docs.iza.org/dp7268.pdf) |
| `ellison2002slowdown` | The Slowdown of the Economics Publishing Process | Journal of Political Economy 2002 | [链接](https://www.nber.org/system/files/working_papers/w7804/w7804.pdf) |
| `card2013nine` | Nine Facts about Top Journals in Economics | Journal of Economic Literature 2013 | [链接](https://www.nber.org/system/files/working_papers/w18665/w18665.pdf) |
| `heckman2020tyranny` | Publishing and Promotion in Economics: The Tyranny of the Top Five | Journal of Economic Literature 2020 | [链接](https://docs.iza.org/dp11868.pdf) |
| `einav2006surname` | What's in a Surname? The Effects of Surname Initials on Academic Success | Journal of Economic Perspectives 2006 | [链接](https://web.stanford.edu/~leinav/pubs/JEP2006.pdf) |
| `cawley2018guide` | A Guide and Advice for Economists on the U.S. Junior Academic Job Market: 2018–2019 Edition | American Economic Association 2018 | [链接](https://www.aeaweb.org/content/file?id=869) |
| `olken2015promises` | Promises and Perils of Pre-analysis Plans | Journal of Economic Perspectives 2015 | [链接](https://www.aeaweb.org/articles?id=10.1257/jep.29.3.61) |
| `nberworkingpapers` | Working Papers | 网页 | [链接](https://www.nber.org/papers) |
| `aea2026data` | Data and Code Availability Policy | 网页 2026 | [链接](https://www.aeaweb.org/journals/data/data-code-policy) |
| `aea2026rct` | About the AEA RCT Registry; AEA RCT Registry Registration Guidelines | 网页 2026 | [链接](https://www.aeaweb.org/journals/policies/rct-registry) |
| `aea2026disclosure` | Disclosure Policy | 网页 2026 | [链接](https://www.aeaweb.org/journals/policies/disclosure-policy) |
| `aha2023standards` | Statement on Standards of Professional Conduct | American Historical Association 网页 2023 | [链接](https://web.archive.org/web/20240604095630/https://www.historians.org/jobs-and-professional-development/statements-standards-and-guidelines-of-the-discipline/statement-on-standards-of-professional-conduct) |
| `aha2013embargo` | Statement on Policies Regarding the Option to Embargo Completed History PhD Dissertations | American Historical Association 网页 2013 | [链接](https://web.archive.org/web/20240601005252/https://www.historians.org/jobs-and-professional-development/statements-standards-and-guidelines-of-the-discipline/statement-on-policies-regarding-the-option-to-embargo-completed-history-phd-dissertations) |
| `aha2021collaborators` | Guidelines for Acknowledgment of Collaborators | American Historical Association 网页 2021 | [链接](https://web.archive.org/web/20240601010410/https://www.historians.org/jobs-and-professional-development/statements-standards-and-guidelines-of-the-discipline/guidelines-for-acknowledgment-of-collaborators) |
| `hunt2002against` | Against Presentism | Perspectives on History 2002 | [链接](https://web.archive.org/web/20220918163213/https://www.historians.org/publications-and-directories/perspectives-on-history/may-2002/against-presentism) |
| `oha2018principles` | OHA Principles and Best Practices: Principles and Best Practices for Oral History | Oral History Association 网页 2018 | [链接](https://oralhistory.org/principles-and-best-practices-revised-2018/) |
| `saa2024principles` | SAA Principles of Archaeological Ethics | 网页 2024 | [链接](https://www.saa.org/common/Uploaded%20files/saadocs/CareerPractice/saa_ethics.pdf) |
| `cifa2023excavation` | Standard and Universal Guidance for Archaeological Excavation | 网页 2023 | [链接](https://www.archaeologists.net/sites/default/files/2024-11/CIfA-Standard-Archaeological-Excavation_2023.pdf) |
| `cronon2009learning` | Learning to Do Historical Research: A Primer for Environmental Historians and Others | 网页 2009 | [链接](https://www.williamcronon.net/researching/) |
| `chicago2024citation` | Chicago-Style Citation Quick Guide | The Chicago Manual of Style Online 2024 | [链接](https://www.chicagomanualofstyle.org/tools_citationguide.html) |
| `rutner2012supporting` | Supporting the Changing Research Practices of Historians | Ithaka S+R 2012 | [链接](https://sr.ithaka.org/wp-content/uploads/2015/08/supporting-the-changing-research-practices-of-historians.pdf) |

## 待获取

以下资料有价值，但目前无法读到全文。获取后请保存为 `papers/pdf/<key>.pdf`（不提交进仓库）。

| 优先级 | key | 用途 | 情况 |
|---|---|---|---|
| 高 | `petersen2015guidelines` | 映射研究的更新版指南和评估清单 | 出版社付费。BTH 机构库可能有免费 PDF：[diva2:815606](http://www.diva-portal.org/smash/record.jsf?pid=diva2:815606)，需要用浏览器确认 |
| 高 | `gomez2014understanding` | 复现研究的分类，整理"复现研究"的核心依据 | 付费，未找到自存档版本 |
| 中 | `wohlin2024experimentation` | 威胁效度的经典论述 | 付费书籍；只需要讲效度的部分（2012 年版位于 Planning 一章） |
| 中 | `arcuri2014hitchhiker` | 工具评测中的统计检验 | 付费；ICSE 2011 短版 `arcuri2011practical` 可能在 ACM 免费 |
| 中 | `shull2008role` | 复现研究的定位 | 付费 |
| 低 | `felderer2020contemporary` | 多种实证方法的较新综述 | 需要先看目录挑选章节 |
