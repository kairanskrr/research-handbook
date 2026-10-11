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
| `acs2015identifying` | Identifying and Evaluating Hazards in Research Laboratories | American Chemical Society 2015 | [链接](https://www.acs.org/content/dam/acsorg/about/governance/committees/chemicalsafety/publications/identifying-and-evaluating-hazards-in-research-laboratories.pdf) |
| `acs2026ethical` | Ethical Guidelines to Publication of Chemical Research | ACS Publications 网页 2026 | [链接](https://researcher-resources.acs.org/publish/ethical_guidelines) |
| `acsjocguidelines` | The Journal of Organic Chemistry: Author Guidelines | ACS Publications 网页 2026 | [链接](https://researcher-resources.acs.org/publish/author_guidelines?coden=joceah) |
| `acsdatapolicy` | ACS Research Data Policy | ACS Publications 网页 | [链接](https://researcher-resources.acs.org/publish/data_policy) |
| `bergman2016reproducibility` | Reproducibility in Chemical Research | Angewandte Chemie International Edition 2016 | [链接](https://doi.org/10.1002/anie.201606591) |
| `orgsyninstructions` | Organic Syntheses: Instructions for Authors | Organic Syntheses 网页 | [链接](https://www.orgsyn.org/instructions.aspx) |
| `chemrxivabout` | About ChemRxiv; FAQs for ChemRxiv Authors | ChemRxiv 网页 | [链接](https://chemrxiv.org/engage/assets/public/chemrxiv/term/about.htm) |
| `iupacfaircookbook` | IUPAC FAIR Chemistry Cookbook | 网页 | [链接](https://iupac.github.io/WFChemCookbook/intro.html) |
| `agu2023ethics` | AGU Scientific Integrity and Professional Ethics | 网页 2023 | [链接](https://www.agu.org/-/media/Files/Learn-About-AGU/AGU_Scientific_Integrity_and_Professional_Ethics_Policy_document.pdf) |
| `fox2021agudata` | Data and Software Sharing Guidance for Authors Submitting to AGU Journals | Zenodo 2021 | [链接](https://data.agu.org/resources/agu-data-software-sharing-guidance) |
| `gmdcodepolicy` | GMD Code and Data Policy | Copernicus Publications | [链接](https://www.geoscientific-model-development.net/policies/code_and_data_policy.html) |
| `gmd2019editorial` | Editorial: The publication of geoscientific model developments v1.2 | Geoscientific Model Development 2019 | [链接](https://doi.org/10.5194/gmd-12-2215-2019) |
| `mastrandrea2010ipcc` | Guidance Note for Lead Authors of the IPCC Fifth Assessment Report on Consistent Treatment of Uncertainties | Intergovernmental Panel on Climate Change (IPCC) 2010 | [链接](https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf) |
| `igsnabout` | About IGSNs | IGSN e.V. 网页 | [链接](https://www.igsn.org/about-igsns) |
| `igsnpublications` | Using IGSN in Publications | IGSN e.V. 网页 | [链接](https://www.igsn.org/resources/using-igsn-in-publications) |
| `eartharxivabout` | About EarthArXiv | EarthArXiv 网页 | [链接](https://eartharxiv.org/repository/about/) |
| `eartharxivfaq` | Frequently Asked Questions | EarthArXiv 网页 | [链接](https://eartharxiv.github.io/faq.html) |
| `eartharxivmoderation` | Moderation Policy | EarthArXiv 网页 | [链接](https://eartharxiv.github.io/moderation.html) |
| `stagge2019assessing` | Assessing data availability and research reproducibility in hydrology and water resources | Scientific Data 2019 | [链接](https://doi.org/10.1038/sdata.2019.30) |
| `eyring2016cmip6` | Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) experimental design and organization | Geoscientific Model Development 2016 | [链接](https://doi.org/10.5194/gmd-9-1937-2016) |
| `clancy2014survey` | Survey of Academic Field Experiences (SAFE): Trainees Report Harassment and Assault | PLoS ONE 2014 | [链接](https://doi.org/10.1371/journal.pone.0102172) |
| `greene2021safety` | Safety and Belonging in the Field: A Checklist for Educators | EarthArXiv preprint (non-peer reviewed) 2021 | [链接](https://go-outdoors.caltech.edu/documents/20636/greene-et-al_2021.pdf) |
| `asce2020code` | Code of Ethics | ASCE 网页 2020 | [链接](https://www.asce.org/career-growth/ethics/code-of-ethics) |
| `ascedataavailability` | Data Availability Statement | ASCE Library | [链接](https://ascelibrary.org/page/dataavailability) |
| `rosenberg2018new` | New Policy to Specify Availability of Data, Models, and Code | Journal of Water Resources Planning and Management 2018 | [链接](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000998) |
| `rosenberg2020next` | The Next Frontier: Making Research More Reproducible | Journal of Water Resources Planning and Management 2020 | [链接](https://par.nsf.gov/servlets/purl/10188458) |
| `hendrickson2011conference` | Conference Papers and Prior Publication | Journal of Bridge Engineering 2011 | [链接](https://doi.org/10.1061/(ASCE)BE.1943-5592.0000294) |
| `oberkampf2003verification` | Verification, Validation, and Predictive Capability in Computational Engineering and Physics | Sandia National Laboratories 2003 | [链接](https://digital.library.unt.edu/ark:/67531/metadc885833/m2/1/high_res_d/918370.pdf) |
| `nheriutexas2020safety` | NHERI@UTexas Safety Plan, Version 2.3 | University of Texas at Austin 2020 | [链接](https://utexas.designsafe-ci.org/media/filer_public/02/b1/02b1b9f1-9b83-4fe7-ad82-7acc4c959a50/nheriutexas_safety_plan-20200826.pdf) |
| `nherilehigh2016users` | NHERI Lehigh RTMD Experimental Facility User's Guide | Lehigh University 2016 | [链接](https://lehigh.designsafe-ci.org/media/cms_page_media/95/NHERI%20Lehigh%20RTMD%20EF%20User's%20Guide%202016-11-02_YsuNvbw.pdf) |
| `asce2026standards` | Codes and Standards | ASCE 网页 | [链接](https://www.asce.org/publications-and-news/codes-and-standards) |
| `asce2026asce7` | ASCE/SEI 7-22: Minimum Design Loads and Associated Criteria for Buildings and Other Structures | ASCE 网页 | [链接](https://www.asce.org/publications-and-news/codes-and-standards/asce-sei-7-22) |
| `nist2008nehrp` | FY 2008 Budget Request Details: National Earthquake Hazards Reduction Program | NIST 网页 | [链接](https://www.nist.gov/congressional-and-legislative-affairs/fy08-national-earthquake-hazards-reduction-program) |
| `jfenumaccuracy` | Journal of Fluids Engineering Editorial Policy Statement on the Control of Numerical Accuracy | American Society of Mechanical Engineers | [链接](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf) |
| `celik2008procedure` | Procedure for Estimation and Reporting of Uncertainty Due to Discretization in CFD Applications | Journal of Fluids Engineering 2008 | [链接](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf) |
| `aiaaeditorialpolicy` | Editorial Policy Statement on Numerical and Experimental Accuracy | AIAA 网页 | [链接](https://aiaa.org/EditorialPolicyStatement) |
| `jcgm2008gum` | Evaluation of Measurement Data – Guide to the Expression of Uncertainty in Measurement | BIPM 2008 | [链接](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf) |
| `taylor1994nist` | Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results | National Institute of Standards and Technology 1994 | [链接](https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1297.pdf) |
| `oberkampf2002verification` | Verification and Validation in Computational Fluid Dynamics | Sandia National Laboratories 2002 | [链接](https://www.osti.gov/biblio/793406) |
| `asme2024ethics` | Society Policy P-15.7: Ethics (Code of Ethics of Engineers) | ASME 2024 | [链接](https://www.asme.org/getmedia/1d9d64bf-f6a7-4e75-a8f5-0cabd8c04269/P-15-7-Ethics_2.pdf) |
| `asme2012canons` | The ASME Criteria for Interpretation of the Canons | ASME 2012 | [链接](https://www.asme.org/wwwasmeorg/media/ResourceFiles/AboutASME/Get%20Involved/Advocacy/Policy-Publications/CRITERIA-FOR-INTERPRETATION-OF-THE-CANONSJune2012.pdf) |
| `asmeethicalstandards` | Ethical Standards | ASME Proceedings: Submission, Review and Acceptance 2026 | [链接](https://www.asme.org/publications-submissions/proceedings/submission-review-and-acceptance/ethical-standards) |
| `asmeconfpapers` | Papers Presented at a Conference | ASME Journals: Information for Authors 2026 | [链接](https://www.asme.org/publications-submissions/journals/information-for-authors/journal-guidelines/papers-presented-at-a-conference) |
| `asme2026imece` | IMECE 2026: International Mechanical Engineering Congress & Exposition | ASME event 网页 2026 | [链接](https://event.asme.org/IMECE) |
| `oshamachineguarding` | Machine Guarding – Overview | U.S. Department of Labor | [链接](https://www.osha.gov/machine-guarding) |
| `oshalockout` | Control of Hazardous Energy (Lockout/Tagout) – Overview | U.S. Department of Labor | [链接](https://www.osha.gov/control-hazardous-energy) |
| `cmu2025machineshop` | Machine Shop Safety – Guideline | Carnegie Mellon University 2025 | [链接](https://www.cmu.edu/ehs/Workplace-Construction/documents/machine-shop-safety-policy.pdf) |
| `csb2011texastech` | Texas Tech University Laboratory Explosion: Case Study | 网页 2011 | [链接](https://www.csb.gov/assets/1/20/CSB_Study_TTU_.pdf) |
| `bligaard2016benchmarking` | Toward Benchmarking in Catalysis Science: Best Practices, Challenges, and Opportunities | ACS Catalysis 2016 | [链接](https://doi.org/10.1021/acscatal.6b00183) |
| `zimmermann2020tea` | Techno-Economic Assessment Guidelines for CO2 Utilization | Frontiers in Energy Research 2020 | [链接](https://www.frontiersin.org/articles/10.3389/fenrg.2020.00005/full) |
| `muller2020lca` | A Guideline for Life Cycle Assessment of Carbon Capture and Utilization | Frontiers in Energy Research 2020 | [链接](https://www.frontiersin.org/articles/10.3389/fenrg.2020.00015/full) |
| `aichecodeethics` | Code of Ethics | AIChE 网页 | [链接](https://www.aiche.org/about/governance/policies/code-ethics) |
| `acsiecrauthorguide` | Industrial & Engineering Chemistry Research: Author Guidelines | ACS Researcher Resources | [链接](https://researcher-resources.acs.org/publish/author_guidelines?coden=iecred) |
| `faria2018minimum` | Minimum information reporting in bio–nano experimental literature | Nature Nanotechnology 2018 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC6150419/) |
| `niosh2009approaches` | Approaches to Safe Nanotechnology: Managing the Health and Safety Concerns Associated with Engineered Nanomaterials | U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, National Institute for Occupational Safety and Health 2009 | [链接](http://web.archive.org/web/20260726080036/https://www.cdc.gov/niosh/docs/2009-125/pdfs/2009-125.pdf) |
| `naturematerials2015checklist` | A checklist for photovoltaic research | 网页 2015 | [链接](https://www.nature.com/articles/nmat4473) |
| `naturesolarcellsreporting` | Solar Cells Reporting Summary | Nature Portfolio 网页 | [链接](https://www.nature.com/documents/nr-photovoltaic-reporting-flat.pdf) |
| `naturereportingstandards` | Reporting standards and availability of data, materials, code and protocols | Nature Portfolio editorial policies | [链接](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards) |
| `wilkinson2016fair` | The FAIR Guiding Principles for scientific data management and stewardship | Scientific Data 2016 | [链接](https://www.nature.com/articles/sdata201618) |
| `jacobsson2022open` | An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles | Nature Energy 2022 | [链接](https://www.nature.com/articles/s41560-021-00941-3) |
| `draxl2018nomad` | NOMAD: The FAIR Concept for Big Data-Driven Materials Science | arXiv:1805.05039 2018 | [链接](https://arxiv.org/abs/1805.05039) |
| `lejaeghere2016reproducibility` | Reproducibility in density functional theory calculations of solids | Science 2016 | [链接](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919278) |
| `mulhopt2018characterization` | Characterization of Nanoparticle Batch-To-Batch Variability | Nanomaterials 2018 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC5977325/) |
| `lblfoundryuser` | User Program Overview | Molecular Foundry 网页 | [链接](https://foundry.lbl.gov/become-a-foundry-user/) |
| `fda2023cmscredibility` | Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions: Guidance for Industry and Food and Drug Administration Staff | U.S. Food and Drug Administration, Center for Devices and Radiological Health 2023 | [链接](https://web.archive.org/web/20260513124224/https://www.fda.gov/media/154985/download) |
| `fda1997designcontrol` | Design Control Guidance for Medical Device Manufacturers | U.S. Food and Drug Administration, Center for Devices and Radiological Health 1997 | [链接](https://web.archive.org/web/20251214094548/https://www.fda.gov/media/116573/download) |
| `cfr2023designcontrols` | 21 CFR 820.30 – Design Controls | Code of Federal Regulations, Title 21, Volume 8, revised as of April 1, 2023 (govinfo.gov) 2023 | [链接](https://www.govinfo.gov/content/pkg/CFR-2023-title21-vol8/pdf/CFR-2023-title21-vol8-sec820-30.pdf) |
| `cfr2026qmsr` | 21 CFR Part 820 – Quality Management System Regulation | Electronic Code of Federal Regulations (eCFR) 2026 | [链接](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820) |
| `aabb2026qmsr` | FDA Implements Quality Management System Regulation for Medical Devices | AABB News 2026 | [链接](https://aabb.org/news-resources/news/article/2026/02/04/fda-implements-quality-management-system-regulation-for-medical-devices) |
| `cfr2026ide` | 21 CFR Part 812 – Investigational Device Exemptions | Electronic Code of Federal Regulations (eCFR) 2026 | [链接](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812) |
| `bmes2021ethics` | BMES Code of Ethics | Biomedical Engineering Society 网页 2021 | [链接](https://www.bmes.org/hubfs/Files/BMES_Code_of_Ethics_2021_-_Revised_October_2021.pdf) |
| `embstbmeprepare` | Prepare and Submit Manuscript – IEEE Transactions on Biomedical Engineering | EMBS 网页 2025 | [链接](https://web.archive.org/web/20250115120531/https://www.embs.org/tbme/for-authors/prepare-and-submit-manuscript/) |
| `collins2024tripodai` | TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods | BMJ 2024 | [链接](https://doi.org/10.1136/bmj-2023-078378) |
| `epa2006dqo` | Guidance on Systematic Planning Using the Data Quality Objectives Process (EPA QA/G-4) | U.S. Environmental Protection Agency, Office of Environmental Information 2006 | [链接](https://www.epa.gov/sites/default/files/2015-06/documents/g4-final.pdf) |
| `epa2002qapp` | Guidance for Quality Assurance Project Plans (EPA QA/G-5) | U.S. Environmental Protection Agency, Office of Environmental Information 2002 | [链接](https://www.epa.gov/sites/default/files/2015-06/documents/g5-final.pdf) |
| `epa2016mdl` | Definition and Procedure for the Determination of the Method Detection Limit, Revision 2 | U.S. Environmental Protection Agency, Office of Water 2016 | [链接](https://www.epa.gov/sites/default/files/2016-12/documents/mdl-procedure_rev2_12-13-2016.pdf) |
| `helsel2020statistical` | Statistical Methods in Water Resources | U.S. Geological Survey 2020 | [链接](https://pubs.usgs.gov/tm/04/a03/tm4a3.pdf) |
| `epa2006lca` | Life Cycle Assessment: Principles and Practice | U.S. Environmental Protection Agency, National Risk Management Research Laboratory 2006 | [链接](https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P1000L86.PDF) |
| `estauthorguidelines` | Environmental Science & Technology: Author Guidelines | ACS Researcher Resources 网页 | [链接](https://researcher-resources.acs.org/publish/author_guidelines?coden=esthag) |
| `roy2019citizen` | Citizen Science During the Flint, Michigan Federal Water Emergency: Ethical Dilemmas and Lessons Learned | Citizen Science: Theory and Practice 2019 | [链接](https://doi.org/10.5334/cstp.154) |
| `epa2024environmentaljustice` | Environmental Justice | EPA 网页 2024 | [链接](http://web.archive.org/web/20240531090447/https://www.epa.gov/environmentaljustice) |
| `cdc2020bmbl` | Biosafety in Microbiological and Biomedical Laboratories | U.S. Department of Health and Human Services 2020 | [链接](https://www.cdc.gov/labs/pdf/SF__19_308133-A_BMBL6_00-BOOK-WEB-final-3.pdf) |
| `nih2024guidelines` | NIH Guidelines for Research Involving Recombinant or Synthetic Nucleic Acid Molecules | National Institutes of Health, Office of Science Policy 2024 | [链接](https://osp.od.nih.gov/wp-content/uploads/NIH_Guidelines.pdf) |
| `who2022responsible` | Global Guidance Framework for the Responsible Use of the Life Sciences: Mitigating Biorisks and Governing Dual-Use Research | 网页 2022 | [链接](https://iris.who.int/bitstream/handle/10665/362313/9789240056107-eng.pdf) |
| `cbd2000cartagena` | Cartagena Protocol on Biosafety to the Convention on Biological Diversity: Text and Annexes | 网页 2000 | [链接](https://www.cbd.int/doc/legal/cartagena-protocol-en.pdf) |
| `bustin2009miqe` | The MIQE Guidelines: Minimum Information for Publication of Quantitative Real-Time PCR Experiments | Clinical Chemistry 2009 | [链接](https://doi.org/10.1373/clinchem.2008.112797) |
| `bustin2025miqe` | MIQE 2.0 and the Urgent Need to Rethink qPCR Standards | International Journal of Molecular Sciences 2025 | [链接](https://doi.org/10.3390/ijms26114975) |
| `beal2016reproducibility` | Reproducibility of Fluorescent Expression from Engineered Biological Constructs in E. coli | PLoS ONE 2016 | [链接](https://doi.org/10.1371/journal.pone.0150182) |
| `crater2018scaleup` | Scale-up of Industrial Microbial Processes | FEMS Microbiology Letters 2018 | [链接](https://doi.org/10.1093/femsle/fny138) |
| `mclaughlin2020sbol3` | The Synthetic Biology Open Language (SBOL) Version 3: Simplified Data Exchange for Bioengineering | Frontiers in Bioengineering and Biotechnology 2020 | [链接](https://doi.org/10.3389/fbioe.2020.01009) |
| `crs2025gainoffunction` | Recent Executive Actions Related to Gain-of-Function Research and Laboratory Biosafety | 网页 2025 | [链接](https://www.everycrsreport.com/reports/IN12554.html) |
| `casrai2026highrisk` | USG Policy for Stopping High-Risk Life Sciences Research: What Changes for Institutions | CASRAI news 2026 | [链接](https://casrai.org/news/usg-policy-stopping-high-risk-life-sciences-research-institutions-2026) |
| `landis2012call` | A call for transparent reporting to optimize the predictive value of preclinical research | Nature 2012 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC3511845/) |
| `uhlen2016proposal` | A proposal for validation of antibodies | Nature Methods 2016 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC10335836/) |
| `curtis2018experimental` | Experimental design and analysis and their reporting II: updated and simplified guidance for authors and peer reviewers | British Journal of Pharmacology 2018 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC5843711/) |
| `mak2014lost` | Lost in translation: animal models and clinical trials in cancer treatment | American Journal of Translational Research 2014 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC3902221/) |
| `oecd1998glp` | OECD Principles on Good Laboratory Practice (as revised in 1997) | Organisation for Economic Co-operation and Development, Environment Directorate 1998 | [链接](https://one.oecd.org/document/env/mc/chem(98)17/en/pdf) |
| `wma2016taipei` | WMA Declaration of Taipei on Ethical Considerations regarding Health Databases and Biobanks | Adopted October 2002, revised by the 67th WMA General Assembly, Taipei, October 2016 2016 | [链接](https://www.wma.net/policies-post/wma-declaration-of-taipei-on-ethical-considerations-regarding-health-databases-and-biobanks/) |
| `benchimol2015record` | The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement | PLOS Medicine 2015 | [链接](https://doi.org/10.1371/journal.pmed.1001885) |
| `hernan2018cword` | The C-Word: Scientific Euphemisms Do Not Improve Causal Inference From Observational Data | American Journal of Public Health 2018 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC5888052/) |
| `cioms2016ethical` | International Ethical Guidelines for Health-related Research Involving Humans | Council for International Organizations of Medical Sciences (CIOMS) 2016 | [链接](https://cioms.ch/wp-content/uploads/2017/01/WEB-CIOMS-EthicalGuidelines.pdf) |
| `higgins2024cochrane` | Cochrane Handbook for Systematic Reviews of Interventions | Cochrane 2024 | [链接](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) |
| `mays2000assessing` | Qualitative research in health care: Assessing quality in qualitative research | BMJ 2000 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC1117321/) |
| `equatorcoreq` | Consolidated criteria for reporting qualitative research (COREQ): a 32-item checklist for interviews and focus groups (Library entry) | 网页 2023 | [链接](https://www.equator-network.org/reporting-guidelines/coreq/) |
| `medrxivabout` | About medRxiv | 网页 | [链接](https://www.medrxiv.org/content/about-medrxiv) |
| `casler2015fundamentals` | Fundamentals of Experimental Design: Guidelines for Designing Successful Experiments | Agronomy Journal 2015 | [链接](https://doi.org/10.2134/agronj2013.0114) |
| `papoutsoglou2020enabling` | Enabling reusability of plant phenomic datasets with MIAPPE 1.1 | New Phytologist 2020 | [链接](https://doi.org/10.1111/nph.16544) |
| `cgiar2021fair` | CGIAR Open and FAIR Data Assets Policy | Approved by the System Management Board, effective 16 April 2021 2021 | [链接](https://cgspace.cgiar.org/server/api/core/bitstreams/3c39bf16-b35d-4faa-b509-b29d045a9144/content) |
| `rothamstedlte` | The Long Term Experiments | 网页 | [链接](https://www.rothamsted.ac.uk/long-term-experiments) |
| `sciencesocietieseditorial` | Editorial Policies | Web page, last updated June 30, 2026 | [链接](https://www.sciencesocieties.org/publications/journals/author-resources/editorial-policies) |
| `asa2024style` | Publications Handbook and Style Manual | ASA, CSSA, SSSA 2024 | [链接](https://www.agronomy.org/files/publications/style/style-manual.pdf) |
| `kyveryga2019onfarm` | On-Farm Research: Experimental Approaches, Analytical Frameworks, Case Studies, and Impact | Agronomy Journal 2019 | [链接](https://doi.org/10.2134/agronj2019.11.0001) |
| `kool2020reproducibility` | Reproducibility and external validity of on-farm experimental research in Africa | Experimental Agriculture 2020 | [链接](https://doi.org/10.1017/S0014479720000174) |
| `davies2015pseudoreplication` | Don't let spurious accusations of pseudoreplication limit our ability to learn from natural experiments (and other messy kinds of ecological monitoring) | Ecology and Evolution 2015 | [链接](https://doi.org/10.1002/ece3.1782) |
| `afs2014fishes` | Guidelines for the Use of Fishes in Research | American Fisheries Society 2014 | [链接](https://fisheries.org/policy-media/science-guidelines/guidelines-for-the-use-of-fishes-in-research/) |
| `fass2020agguide` | Guide for the Care and Use of Agricultural Animals in Research and Teaching | American Dairy Science Association, American Society of Animal Science, and Poultry Science Association 2020 | [链接](https://www.asas.org/docs/default-source/default-document-library/agguide_4th.pdf) |
| `oconnor2010reflect` | The REFLECT statement: Methods and processes of creating reporting guidelines for randomized controlled trials for livestock and food safety | Journal of Swine Health and Production 2010 | [链接](https://www.aasv.org/shap/issues/v18n1/v18n1p18.pdf) |
| `sargeant2016strobevet` | Methods and Processes of Developing the Strengthening the Reporting of Observational Studies in Epidemiology – Veterinary (STROBE-Vet) Statement | Journal of Veterinary Internal Medicine 2016 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC5115188/) |
| `page2016conduct` | Conduct, Oversight, and Ethical Considerations of Clinical Trials in Companion Animals with Cancer: Report of a Workshop on Best Practice Recommendations | Journal of Veterinary Internal Medicine 2016 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC4913608/) |
| `bertout2021recommendations` | Recommendations for Ethical Review of Veterinary Clinical Trials | Frontiers in Veterinary Science 2021 | [链接](https://doi.org/10.3389/fvets.2021.715926) |
| `who2026onehealth` | One Health | Fact sheet 2026 | [链接](https://www.who.int/news-room/fact-sheets/detail/one-health) |
| `bera2024ethical` | Ethical Guidelines for Educational Research | 网页 2024 | [链接](https://www.bera.ac.uk/publication/ethical-guidelines-for-educational-research-fifth-edition-2024) |
| `aera2011code` | Code of Ethics | Approved by the AERA Council, February 2011 2011 | [链接](https://www.aera.net/Portals/38/docs/About_AERA/CodeOfEthics(1).pdf) |
| `aera2006standards` | Standards for Reporting on Empirical Social Science Research in AERA Publications | Educational Researcher 2006 | [链接](https://www.aera.net/Portals/38/docs/12ERv35n6_Standard4Report%20.pdf) |
| `wwc2022handbook` | What Works Clearinghouse Procedures and Standards Handbook, Version 5.0 | U.S. Department of Education, Institute of Education Sciences, National Center for Education Evaluation and Regional Assistance 2022 | [链接](https://ies.ed.gov/ncee/wwc/Docs/referenceresources/Final_WWC-HandbookVer5_0-0-508.pdf) |
| `kraft2019interpreting` | Interpreting Effect Sizes of Education Interventions | Annenberg Institute at Brown University 2019 | [链接](https://edworkingpapers.com/ai19-10) |
| `makel2014facts` | Facts Are More Important Than Novelty: Replication in the Education Sciences | Educational Researcher 2014 | [链接](https://www.aera.net/Newsroom/Recent-AERA-Research/Facts-Are-More-Important-Than-Novelty-Replication-in-the-Education-Sciences) |
| `eef2022recruitment` | Guidance on Recruitment and Retention | 网页 2022 | [链接](https://educationendowmentfoundation.org.uk/public/files/Recruitment_and_retention_guidance_FINAL..pdf) |
| `ies2013common` | Common Guidelines for Education Research and Development | U.S. Department of Education and National Science Foundation 2013 | [链接](https://ies.ed.gov/pdf/commonguidelines.pdf) |
| `anderson2012design` | Design-Based Research: A Decade of Progress in Education Research? | Educational Researcher 2012 | [链接](https://auspace.athabascau.ca/handle/2149/3184) |
| `ies2018rees` | Celebrating the Launch of the Registry of Efficacy and Effectiveness Studies (REES) | IES blog 2018 | [链接](https://ies.ed.gov/learn/blog/celebrating-launch-registry-efficacy-and-effectiveness-studies-rees) |
| `edworkingpapersabout` | About EdWorkingPapers | 网页 2026 | [链接](https://edworkingpapers.com/about) |
| `asa2018code` | Code of Ethics | American Sociological Association, Washington, DC 2018 | [链接](https://www.asanet.org/wp-content/uploads/asa_code_of_ethics-june2018.pdf) |
| `bsa2017statement` | Statement of Ethical Practice | BSA Publications, Durham 2017 | [链接](https://www.britsoc.co.uk/media/24310/bsa_statement_of_ethical_practice.pdf) |
| `freese2017replication` | Replication in Social Science | Annual Review of Sociology 2017 | [链接](https://osf.io/preprints/socarxiv/5bck9) |
| `jerolmack2024ethnography` | Editorial: Ethnography in the Open Science and Digital Age: New Debates, Dilemmas, and Issues | Frontiers in Sociology 2024 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC10978767/) |
| `icpsrdata` | About ICPSR; Deposit Data; Citing Data; Data Confidentiality | ICPSR, University of Michigan, web pages 2025 | [链接](https://www.icpsr.umich.edu/web/pages/about/) |
| `sociologicalsciencepolicy` | Sociological Science: Editorial and Review Process; Reproducibility Policy; Journal Information | Journal 网页 2026 | [链接](https://sociologicalscience.com/for-authors/editorial-and-review-process/) |
| `asrsubmission` | Submission Guidelines | Sage Publications 2026 | [链接](https://journals.sagepub.com/author-instructions/ASR) |
| `wesleyan2015sociology` | Expectations for Promotion to Associate Professor Conferring Tenure | Wesleyan University Office of Academic Affairs 2015 | [链接](https://www.wesleyan.edu/acaf/Tenure-and-Promotion-Expectations/SOC_2015.pdf) |
| `epstein2002rules` | The Rules of Inference | University of Chicago Law Review 2002 | [链接](https://gking.harvard.edu/files/gking/files/rules.pdf) |
| `hutchinson2012defining` | Defining and Describing What We Do: Doctrinal Legal Research | Deakin Law Review 2012 | [链接](https://ojs.deakin.edu.au/index.php/dlr/article/view/70) |
| `goudkamp2026oscola` | OSCOLA: The Oxford University Standard for Citation of Legal Authorities | Hart Publishing 2026 | [链接](https://www.law.ox.ac.uk/oscola) |
| `yljsubmissions` | Submissions; Data Retention Policy for Authors | Web page and PDF | [链接](https://www.yalelawjournal.org/submissions) |
| `uclrsubmissions` | Submissions | 网页 | [链接](https://lawreview.uchicago.edu/submissions) |
| `lwipublishingtips` | Publishing Tips | PDF | [链接](https://www.lwionline.org/sites/default/files/Publishing-Tips.pdf) |
| `ssrnlsn` | Legal Scholarship Network | 网页 | [链接](https://www.ssrn.com/index.cfm/en/lsn/) |
| `northwesterngoodlaw` | Researching Case Law: Determining Whether Cases Are Still Good Law | Research guide | [链接](https://library.law.northwestern.edu/cases/updating) |
| `legislationgovukhelp` | Help: Guide to Revised Legislation on legislation.gov.uk | 网页 | [链接](https://www.legislation.gov.uk/help) |
| `slsa2021ethics` | Statement of Principles of Ethical Research Practice | PDF 2021 | [链接](https://slsa.ac.uk/images/slsadownloads/SLSA_Board_2021/SLSA_Ethics_Statement_-_September_2021.pdf) |
| `apsa2012ethics` | A Guide to Professional Ethics in Political Science | American Political Science Association 2012 | [链接](https://www.apsanet.org/Portals/54/APSA%20Files/publications/ethicsguideweb.pdf) |
| `apsa2020humansubjects` | Principles and Guidance for Human Subjects Research | 网页 2020 | [链接](https://www.apsanet.org/Portals/54/diversity%20and%20inclusion%20prgms/Ethics/Final_Principles%20with%20Guidance%20with%20intro.pdf) |
| `dart2014jets` | Data Access and Research Transparency (DA-RT): A Joint Statement by Political Science Journal Editors (Journal Editors' Transparency Statement, JETS) | 网页 2014 | [链接](https://www.dartstatement.org/2014-journal-editors-statement-jets) |
| `ajps2026verification` | AJPS Verification Policy | 网页 2026 | [链接](https://ajps.org/ajps-verification-policy/) |
| `jacobs2021qualitative` | The Qualitative Transparency Deliberations: Insights and Implications | Perspectives on Politics 2021 | [链接](https://eprints.whiterose.ac.uk/id/eprint/158221/) |
| `ofosu2023preanalysis` | Pre-Analysis Plans: An Early Stocktaking | Perspectives on Politics 2023 | [链接](https://researchonline.lse.ac.uk/id/eprint/112747/) |
| `eubank2016lessons` | Lessons from a Decade of Replications at the Quarterly Journal of Political Science | PS: Political Science & Politics 2016 | [链接](https://dukespace.lib.duke.edu/items/319e52d7-0932-4d21-89bb-85df233fbcbd) |
| `mcdermott2020ethics` | Ethics in Field Experimentation: A Call to Establish New Standards to Protect the Public from Unwanted Manipulation and Real Harms | Proceedings of the National Academy of Sciences 2020 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720186/) |
| `egappreanalysis` | 10 Things to Know About Pre-Analysis Plans | Evidence in Governance and Politics (EGAP) | [链接](https://methods.egap.org/guides/planning/pap_en.html) |
| `egapsurveyexperiments` | 10 Things to Know About Survey Experiments | Evidence in Governance and Politics (EGAP) | [链接](https://methods.egap.org/guides/data-collection/survey-experiments_en.html) |
| `aag2024ethics` | Statement of Professional Ethics | 网页 2024 | [链接](https://aag.org/statement-of-professional-ethics) |
| `rgsgrantscode` | Code of Practice for the Grants Programme | 网页 | [链接](https://www.rgs.org/in-the-field/grants/guidance-for-society-grant-applicants/code-of-practice-for-the-grants-programme) |
| `rgssaferesearch` | Safe, Responsible and Ethical Research | 网页 | [链接](https://www.rgs.org/exploration/grants/guidance-for-society-grant-applicants/safe-responsible-and-ethical-research/) |
| `kedron2021reproducibility` | Reproducibility and Replicability: Opportunities and Challenges for Geospatial Research | International Journal of Geographical Information Science 2021 | [链接](https://par.nsf.gov/servlets/purl/10292882) |
| `kwan2012uncertain` | The Uncertain Geographic Context Problem | Annals of the Association of American Geographers 2012 | [链接](http://meipokwan.org/Paper/Kwan_UGCoP_2012.pdf) |
| `kwan2018limits` | The Limits of the Neighborhood Effect: Contextual Uncertainties in Geographic, Environmental Health, and Social Science Research | Annals of the American Association of Geographers 2018 | [链接](http://meipokwan.org/Paper/Kwan_2018_AAAG.pdf) |
| `malekzadeh2026ethical` | Ethical Guidelines for Geoprivacy: A Framework for Researchers and Ethics Committees | International Journal of Health Geographics 2026 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC13092162/) |
| `nust2018reproducible` | Reproducible Research and GIScience: An Evaluation Using AGILE Conference Papers | PeerJ 2018 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC6047504/) |
| `karhulahti2024positionality` | Positionality Statements in Science | Open Research Europe 2024 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC11200055/) |
| `franzke2020internet` | Internet Research: Ethical Guidelines 3.0 | Association of Internet Researchers 2020 | [链接](https://aoir.org/reports/ethics3.pdf) |
| `lombard2010practical` | Practical Resources for Assessing and Reporting Intercoder Reliability in Content Analysis Research Projects | Online resource, last updated June 1, 2010 2010 | [链接](http://matthewlombard.com/reliability/) |
| `dienlin2021agenda` | An Agenda for Open Science in Communication | Journal of Communication 2021 | [链接](https://doi.org/10.1093/joc/jqz052) |
| `ica2019ethics` | ICA Code of Ethics | Adopted May 2019 2019 | [链接](https://cdn.ymaws.com/www.icahdq.org/resource/resmgr/governance_documents/ica.code.of.ethics.may2019.pdf) |
| `ica2026conference` | 76th Annual ICA Conference: Conference Submission Guidelines and Conference Submission Types | Web pages, accessed via Internet Archive snapshots of 2025-09-05 and 2025-10-02 2025 | [链接](https://www.icahdq.org/page/conf-submission-guidelines) |
| `icaopenscholarship` | Open Scholarship | Web page, accessed via Internet Archive snapshot of 2025-09-18 2025 | [链接](https://www.icahdq.org/page/OpenScholarship) |
| `icajournalsfaq` | Journals Frequently Asked Questions | Web page, accessed via Internet Archive snapshot of 2025-09-12 2025 | [链接](https://www.icahdq.org/page/JournalsFAQ) |
| `freelon2018computational` | Computational Research in the Post-API Age | Political Communication 2018 | [链接](https://doi.org/10.1080/10584609.2018.1477506) |
| `eu2022dsa` | Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market for Digital Services and amending Directive 2000/31/EC (Digital Services Act) | Official Journal of the European Union, L 277, 27 October 2022, p. 1 2022 | [链接](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065) |
| `lsa2019ethics` | LSA Ethics Statement | 网页 2019 | [链接](https://www.lsadc.org/lsa_ethics_statement) |
| `lsa1992humansubjects` | Human Subjects in Linguistic Research | 网页 1992 | [链接](https://www.lsadc.org/human_subjects_in_linguistic_research) |
| `lsa2010documentation` | Resolution Recognizing the Scholarly Merit of Language Documentation | 网页 2010 | [链接](https://lsa.membershipsoftware.org//Files/Advocacy/201001_Resolution_Scholarly_Merit_Lang_Documentation.pdf) |
| `berezkroeker2018reproducible` | Reproducible research in linguistics: A position statement on data citation and attribution in our field | Linguistics 2018 | [链接](https://doi.org/10.1515/ling-2017-0032) |
| `berezkroeker2018austin` | The Austin Principles of Data Citation in Linguistics | 网页 2018 | [链接](https://site.uit.no/linguisticsdatacitation/austinprinciples/) |
| `roettger2019researcher` | Researcher degrees of freedom in phonetic research | Laboratory Phonology: Journal of the Association for Laboratory Phonology 2019 | [链接](https://doi.org/10.5334/labphon.147) |
| `mla2007evaluating` | Report of the MLA Task Force on Evaluating Scholarship for Tenure and Promotion | Profession 2007 | [链接](https://www.mla.org/content/download/3362/file/taskforcereport0608.pdf) |
| `mla2012digital` | Guidelines for Evaluating Work in Digital Humanities and Digital Media | 网页 2012 | [链接](https://www.mla.org/About-Us/Governance/Committees/Committee-Listings/Professional-Issues/Committee-on-Information-Technology/Guidelines-for-Evaluating-Work-in-Digital-Humanities-and-Digital-Media) |
| `mlastylecenter` | MLA Style Center: In-Text Citations: An Overview; Plagiarism and Academic Dishonesty; Works Cited: A Quick Guide | 网页 | [链接](https://style.mla.org/in-text-citations-overview/) |
| `mlacseguidelines` | Guidelines for Editors of Scholarly Editions | 网页 | [链接](https://www.mla.org/Resources/Guidelines-and-Data/Reports-and-Professional-Guidelines/Guidelines-for-Editors-of-Scholarly-Editions) |
| `uncwritinglit` | Literature (Fiction) | 网页 | [链接](https://writingcenter.unc.edu/tips-and-tools/literature/) |
| `yorkclosereading` | Close reading | 网页 | [链接](https://www.york.ac.uk/english/about/writing-at-york/writing-resources/close-reading/) |
| `pryor2012writing` | Guidelines on Writing a Philosophy Paper | 网页 2012 | [链接](https://www.jimpryor.net/teaching/guidelines/writing.html) |
| `pryor2006reading` | Guidelines on Reading Philosophy | 网页 2006 | [链接](https://www.jimpryor.net/teaching/guidelines/reading.html) |
| `apaphil2022journal` | Statement on Best Practices in Journal Publishing | 网页 2022 | [链接](https://www.apaonline.org/page/journalpractices) |
| `apaphil1996research` | Statement on Research | Proceedings and Addresses of the American Philosophical Association 1996 | [链接](https://www.apaonline.org/page/research) |
| `apaphil2016conduct` | Code of Conduct | 网页 2016 | [链接](https://www.apaonline.org/page/codeofconduct) |
| `andrews2024journal` | Insights from the American Philosophical Association's Journal Surveys Project | 网页 2024 | [链接](https://blog.apaonline.org/2024/06/07/insights-from-the-american-philosophical-associations-journal-surveys-project/) |
| `jhp2025statistics` | Submissions Statistics | 网页 2025 | [链接](https://jhp.wisc.edu/submissions.html) |
| `chang2023prolific` | Prolific philosophy authors' preferences regarding scientific collaboration, journal levels, and author role | iConference 2023 Proceedings 2023 | [链接](https://hdl.handle.net/2142/117350) |
| `sytsma2026experimental` | Experimental Philosophy | The Stanford Encyclopedia of Philosophy 2026 | [链接](https://plato.stanford.edu/entries/experimental-philosophy/) |
| `knight2023reflective` | Reflective Equilibrium | The Stanford Encyclopedia of Philosophy 2023 | [链接](https://plato.stanford.edu/entries/reflective-equilibrium/) |
| `brown2023thought` | Thought Experiments | The Stanford Encyclopedia of Philosophy 2023 | [链接](https://plato.stanford.edu/entries/thought-experiment/) |
| `wood2021philosophy` | Philosophy and Christian Theology | The Stanford Encyclopedia of Philosophy 2021 | [链接](https://plato.stanford.edu/entries/christiantheology-philosophy/) |
| `aar2019literacy` | AAR Religious Literacy Guidelines: What U.S. College Graduates Need to Understand about Religion | 网页 2019 | [链接](https://aarweb.org/resource/aar-religious-literacy-guidelines/) |
| `candy2006practice` | Practice Based Research: A Guide | Creativity & Cognition Studios, University of Technology, Sydney 2006 | [链接](https://www.creativityandcognition.com/resources/PBR%20Guide-1.1-2006.pdf) |
| `aec2020vienna` | The Vienna Declaration on Artistic Research | Policy paper 2020 | [链接](https://aec-music.eu/media/2021/05/viennadeclarationonarfinalversion24june20_20201216163421.pdf) |
| `bulley2021practice` | Practice Research – Report 1: What is practice research? and Report 2: How can practice research be shared? | Practice Research Advisory Group UK (PRAG-UK) 2021 | [链接](https://doi.org/10.23636/1347) |
| `ref2019guidance` | Guidance on submissions (REF 2019/01) | Research England, Scottish Funding Council, Higher Education Funding Council for Wales, Department for the Economy Northern Ireland 2019 | [链接](https://2021.ref.ac.uk/media/1447/ref-2019_01-guidance-on-submissions.pdf) |
| `ref2019panel` | Panel criteria and working methods (REF 2019/02) | Research England, Scottish Funding Council, Higher Education Funding Council for Wales, Department for the Economy Northern Ireland 2019 | [链接](https://2021.ref.ac.uk/media/1450/ref-2019_02-panel-criteria-and-working-methods.pdf) |
| `caa2015fairuse` | Code of Best Practices in Fair Use for the Visual Arts | 网页 2015 | [链接](https://www.collegeart.org/pdf/fair-use/best-practices-fair-use-visual-arts.pdf) |
| `caa2014standards` | Standards for the Practice of Art History | 网页 2014 | [链接](https://www.collegeart.org/standards-and-guidelines/guidelines/art-history-ethics) |
| `sem1998ethics` | Position Statement on Ethical Considerations | 网页 1998 | [链接](https://www.ethnomusicology.org/page/EthicsStatement) |
| `sem2008irb` | Position Statement on Ethnographic Research & Institutional Review Boards | 网页 2008 | [链接](https://www.ethnomusicology.org/page/PS_IRB) |
| `piepho2018tutorial` | A tutorial on the statistical analysis of factorial experiments with qualitative and quantitative treatment factor levels | Journal of Agronomy and Crop Science 2018 | [链接](https://doi.org/10.1111/jac.12267) |
| `smith2005analysis` | The analysis of crop cultivar breeding and evaluation trials: an overview of current mixed model approaches | The Journal of Agricultural Science 2005 | [链接](https://doi.org/10.1017/S0021859605005587) |
| `kramer2016statistics` | Statistics in a Horticultural Journal: Problems and Solutions | Journal of the American Society for Horticultural Science 2016 | [链接](https://doi.org/10.21273/JASHS03747-16) |
| `lacoste2022onfarm` | On-Farm Experimentation to transform global agriculture | Nature Food 2022 | [链接](https://doi.org/10.1038/s43016-021-00424-4) |
| `kozlowski2022substrate` | On the Topic of Substrate Scope | Organic Letters 2022 | [链接](https://doi.org/10.1021/acs.orglett.2c03246) |
| `rana2024standardizing` | Standardizing Substrate Selection: A Strategy toward Unbiased Evaluation of Reaction Generality | ACS Central Science 2024 | [链接](https://doi.org/10.1021/acscentsci.3c01638) |
| `schafer2024sensitivity` | Improving reproducibility through condition-based sensitivity assessments: application, advancement and prospect | Chemical Science 2024 | [链接](https://doi.org/10.1039/d4sc03017f) |
| `schuurmans2026stirring` | Stirring the Debate: How Mixing Influences Reproducibility and Efficiency in Synthetic Organic Chemistry | ACS Central Science 2026 | [链接](https://doi.org/10.1021/acscentsci.5c01825) |
| `kabeshov2026retrosynthesis` | A Return to the Logic-First Spirit of Corey's Retrosynthetic Analysis, Now Implemented in Modern Data-Driven CASP | ACS Central Science 2026 | [链接](https://doi.org/10.1021/acscentsci.6c00702) |
| `schmidt2016using` | Using Archives: A Guide to Effective Research | Society of American Archivists 2016 | [链接](https://www2.archivists.org/usingarchives) |
| `saaacrl2018primary` | Guidelines for Primary Source Literacy | Society of American Archivists and Association of College and Research Libraries 2018 | [链接](https://www2.archivists.org/sites/all/files/Guidelines%20for%20Primary%20Souce%20Literacy_AsApproved062018_1.pdf) |
| `tnastarthere` | Start Here: Help with Your Research | 网页 | [链接](https://www.nationalarchives.gov.uk/help-with-your-research/start-here/) |
| `naragettingstarted` | Getting Started Overview | 网页 | [链接](https://www.archives.gov/research/start) |
| `oha2019archiving` | OHA Archives Principles and Best Practices | Oral History Association 网页 2019 | [链接](https://oralhistory.org/archives-principles-and-best-practices/) |
| `baylor2012introduction` | Workshop on the Web: Introduction to Oral History | Baylor University Institute for Oral History website (series of one-page PDFs) 2012 | [链接](https://www.baylor.edu/content/services/document.php/66420.pdf) |
| `ohs2019legal` | Is Your Oral History Legal and Ethical? Ethical and Legal Guidance | Oral History Society 网页 2019 | [链接](https://www.ohs.org.uk/advice/ethical-and-legal/) |
| `ohs2026wellbeing` | Looking After Yourself | Oral History Society 网页 2026 | [链接](https://ohs.org.uk/looking-after-yourself/) |
| `neuenschwander2014legal` | Major Legal Challenges Facing Oral History in the Digital Age | Oral History in the Digital Age 2014 | [链接](https://ohda.matrix.msu.edu/2012/06/major-legal-challenges/) |
| `shopes2002making` | Making Sense of Oral History | History Matters: The U.S. Survey Course on the Web, George Mason University 2002 | [链接](https://historymatters.gmu.edu/mse/oral/oral.pdf) |
| `cifa2023evaluation` | Standard and Universal Guidance for Archaeological Field Evaluation | 网页 2023 | [链接](https://www.archaeologists.net/sites/default/files/2024-11/CIfA-Standard-Field-Evaluation_2023.pdf) |
| `cifa2020archives` | Standard and Guidance for the Creation, Compilation, Transfer and Deposition of Archaeological Archives | 网页 2020 | [链接](https://www.archaeologists.net/sites/default/files/2023-11/CIfA-SandG-Archaeological-Archives-2020.pdf) |
| `cifa2020geophysics` | Standard and Guidance for Archaeological Geophysical Survey | 网页 2020 | [链接](https://www.archaeologists.net/sites/default/files/2023-11/CIfA-SandG-Geophysical-Survey-2020.pdf) |
| `historicengland2015morphe` | Management of Research Projects in the Historic Environment: The MoRPHE Project Managers' Guide | Historic England 2015 | [链接](https://historicengland.org.uk/images-books/publications/morphe-project-managers-guide/) |
| `harris1989principles` | Principles of Archaeological Stratigraphy | Academic Press 1989 | [链接](https://harrismatrix.com/download/) |
| `nps1983standards` | Archeology and Historic Preservation: Secretary of the Interior's Standards and Guidelines | Federal Register 48(190): 44716–44742 1983 | [链接](https://www.nps.gov/subjects/historicpreservation/upload/standards-guidelines-archeology-historic-preservation.pdf) |
| `hutchinson2015doctrinal` | The Doctrinal Method: Incorporating Interdisciplinary Methods in Reforming the Law | Erasmus Law Review 2015 | [链接](https://eprints.qut.edu.au/93564/3/93564.pdf) |
| `georgetown2020topic` | Choosing a Successful Paper Topic | The Writing Center at Georgetown University Law Center, handout 2020 | [链接](https://www.law.georgetown.edu/wp-content/uploads/2021/04/Handout_3-Kaplan_Woods_Choosing_a_Successful_Paper_Topic.pdf) |
| `georgetown2018thesis` | Developing a Thesis Statement | The Writing Center at Georgetown University Law Center, handout 2018 | [链接](https://www.law.georgetown.edu/wp-content/uploads/2018/11/Updated-Developing-a-Thesis-Statement-Handout.pdf) |
| `georgetown2026research` | You Have Your Scholarly Paper Topic, Now \ldots Get the Research Done | The Writing Center at Georgetown Law, handout 2026 | [链接](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2026/10/You-Have-Your-Scholarly-Paper-Topic-Now-Get-the-Research-Done_Kelsey-Handschuh-2026-Revisions_FINAL-1.pdf) |
| `georgetown2025cases` | Using Cases in Legal Analysis: Methods and Examples | The Writing Center at Georgetown University Law Center, handout 2025 | [链接](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2025/08/Using_Cases_in_Legal_Analysis_Methods_and_ExamplesFCD.pdf) |
| `georgetown2017comparison` | How to Craft an Effective Case Comparison | The Writing Center at Georgetown Law, handout 2017 | [链接](https://www.law.georgetown.edu/wp-content/uploads/2018/07/How-to-Craft-an-Effective-Case-Comparison.pdf) |
| `georgetown2026checklist` | Checklist for Scholarly Writing | The Writing Center at Georgetown Law, handout 2026 | [链接](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2026/10/Checklist-for-Scholarly-Writing_fcd.pdf) |
| `georgetown2026statutes` | A Guide to Reading, Interpreting and Applying Statutes | The Writing Center at Georgetown Law, handout 2026 | [链接](https://www.law.georgetown.edu/academics/wp-content/uploads/sites/58/2026/08/A-Guide-to-Reading-Interpreting-and-Applying-Statutes.pdf) |
| `brannon2023statutory` | Statutory Interpretation: Theories, Tools, and Trends | Congressional Research Service 2023 | [链接](https://www.congress.gov/crs-product/R45153) |
| `northwesterncaselaw` | Researching Case Law | Research guide 2026 | [链接](https://library.law.northwestern.edu/cases/overview) |
| `liiwex` | Wex Legal Dictionary and Encyclopedia | Online legal dictionary 2026 | [链接](https://www.law.cornell.edu/wex) |
| `pryor2025terms` | Philosophical Terms and Methods | 网页 2025 | [链接](https://www.jimpryor.net/teaching/vocab/index.html) |
| `beaney2024analysis` | Analysis | The Stanford Encyclopedia of Philosophy 2024 | [链接](https://plato.stanford.edu/entries/analysis/) |
| `groarke2026informal` | Informal Logic | The Stanford Encyclopedia of Philosophy 2026 | [链接](https://plato.stanford.edu/entries/logic-informal/) |
| `dutilhnovaes2021argument` | Argument and Argumentation | The Stanford Encyclopedia of Philosophy 2021 | [链接](https://plato.stanford.edu/entries/argument/) |
| `pust2024intuition` | Intuition | The Stanford Encyclopedia of Philosophy 2024 | [链接](https://plato.stanford.edu/entries/intuition/) |
| `collier2011understanding` | Understanding Process Tracing | PS: Political Science & Politics 2011 | [链接](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/183A057AD6A36783E678CB37440346D1/S1049096511001429a.pdf/div-class-title-understanding-process-tracing-div.pdf) |
| `bennett2012process` | Process Tracing: From Philosophical Roots to Best Practices | School for International Studies, Simon Fraser University 2012 | [链接](https://web.archive.org/web/20170816174541/http://summit.sfu.ca/system/files/iritems1/14884/SimonsWorkingPaper21.pdf) |
| `seawright2008case` | Case Selection Techniques in Case Study Research: A Menu of Qualitative and Quantitative Options | Political Research Quarterly 2008 | [链接](https://web.archive.org/web/2016/http://blogs.bu.edu/jgerring/files/2013/06/CaseSelection.pdf) |
| `gerring2004case` | What Is a Case Study and What Is It Good For? | American Political Science Review 2004 | [链接](https://web.archive.org/web/2016/http://blogs.bu.edu/jgerring/files/2013/06/CasestudyAPSR.pdf) |
| `geddes1990cases` | How the Cases You Choose Affect the Answers You Get: Selection Bias in Comparative Politics | Institute of Governmental Studies, University of California, Berkeley 1990 | [链接](https://escholarship.org/uc/item/9r45g86c) |
| `rey2023geographic` | Geographic Data Science with Python | CRC Press 2023 | [链接](https://geographicdata.science/book/intro.html) |
| `pebesma2023spatial` | Spatial Data Science: With Applications in R | Chapman and Hall/CRC 2023 | [链接](https://r-spatial.org/book/) |
| `anselin2020global` | Global Spatial Autocorrelation (1): Visualizing Spatial Autocorrelation | GeoDa Workbook, Center for Spatial Data Science, University of Chicago 2020 | [链接](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html) |
| `nust2021practical` | Practical Reproducibility in Geography and Geosciences | Annals of the American Association of Geographers 2021 | [链接](https://doi.org/10.1080/24694452.2020.1806028) |
| `crameri2020misuse` | The misuse of colour in science communication | Nature Communications 2020 | [链接](https://doi.org/10.1038/s41467-020-19160-7) |
| `zandbergen2014ensuring` | Ensuring Confidentiality of Geocoded Health Data: Assessing Geographic Masking Strategies for Individual-Level Data | Advances in Medicine 2014 | [链接](https://doi.org/10.1155/2014/567049) |
| `syba2008englishpaper` | A Brief Guide to Writing the English Paper | Harvard College Writing Center, Brief Guide Series 2008 | [链接](https://writingproject.fas.harvard.edu/files/hwp/files/bg_writing_english.pdf) |
| `kain1998closereading` | How to Do a Close Reading | Harvard College Writing Center 1998 | [链接](https://writingcenter.fas.harvard.edu/pages/how-do-close-reading) |
| `harvardwcthesis` | Thesis | Harvard College Writing Center, Strategies for Essay Writing n.d. | [链接](https://writingcenter.fas.harvard.edu/thesis) |
| `harvardwccounterargument` | Counterargument | Harvard College Writing Center, Strategies for Essay Writing n.d. | [链接](https://writingcenter.fas.harvard.edu/counterargument) |
| `uncwritingquotations` | Quotations | UNC Writing Center Tips and Tools handout n.d. | [链接](https://writingcenter.unc.edu/tips-and-tools/quotations/) |
| `asciuto2018translation` | Ways of Reading a Translation | Department of English and Related Literature, University of York, Writing at York resources 2018 | [链接](https://www.york.ac.uk/english/about/writing-at-york/writing-resources/ways-of-reading-translation/) |
| `leipzig2015glossing` | The Leipzig Glossing Rules: Conventions for Interlinear Morpheme-by-Morpheme Glosses | Department of Linguistics, Max Planck Institute for Evolutionary Anthropology, and Department of Linguistics, University of Leipzig 2015 | [链接](https://www.eva.mpg.de/lingua/pdf/Glossing-Rules.pdf) |
| `paradisecdeposit` | Deposit (Depositing Material with PARADISEC; Catalog Structure & File Naming; File Formats; Metadata; Access Conditions; Do You Own Your Records?) | Pacific And Regional Archive for Digital Sources in Endangered Cultures 网页 2026 | [链接](https://www.paradisec.org.au/deposit/) |
| `bird2002portability` | Seven Dimensions of Portability for Language Documentation and Description | arXiv:cs/0204020 2002 | [链接](https://arxiv.org/abs/cs/0204020) |
| `czaykowskahiggins2009research` | Research Models, Community Engagement, and Linguistic Fieldwork: Reflections on Working within Canadian Indigenous Communities | Language Documentation & Conservation 2009 | [链接](http://hdl.handle.net/10125/4423) |
| `seyfeddinipur2019public` | Public Access to Research Data in Language Documentation: Challenges and Possible Strategies | Language Documentation & Conservation 2019 | [链接](http://hdl.handle.net/10125/24901) |
| `himmelmann2018transcription` | Meeting the Transcription Challenge | Reflections on Language Documentation 20 Years after Himmelmann 1998 2018 | [链接](http://hdl.handle.net/10125/24806) |
| `good2018scope` | Reflections on the Scope of Language Documentation | Reflections on Language Documentation 20 Years after Himmelmann 1998 2018 | [链接](http://hdl.handle.net/10125/24804) |
| `bowern2018fieldwork` | Reflections on Linguistic Fieldwork | Reflections on Language Documentation 20 Years after Himmelmann 1998 2018 | [链接](http://hdl.handle.net/10125/24822) |
| `riesberg2018adequacy` | Reflections on Descriptive and Documentary Adequacy | Reflections on Language Documentation 20 Years after Himmelmann 1998 2018 | [链接](http://hdl.handle.net/10125/24816) |
| `leonard2018decolonialism` | Reflections on (De)colonialism in Language Documentation | Reflections on Language Documentation 20 Years after Himmelmann 1998 2018 | [链接](http://hdl.handle.net/10125/24808) |
| `rice2018corpora` | Reflections on Documentary Corpora | Reflections on Language Documentation 20 Years after Himmelmann 1998 2018 | [链接](http://hdl.handle.net/10125/24817) |
| `candy2018practice` | Practice-Based Research in the Creative Arts: Foundations and Futures from the Front Line | Leonardo 2018 | [链接](https://doi.org/10.1162/LEON_a_01471) |
| `qaa2020doctoral` | Characteristics Statement: Doctoral Degree | Quality Assurance Agency for Higher Education (QAA) 2020 | [链接](https://www.qaa.ac.uk/docs/qaa/quality-code/doctoral-degree-characteristics-statement-2020.pdf) |
| `jar2026submissions` | Submissions: Basic Requirements and Submission Checklist | Journal for Artistic Research 网页 2026 | [链接](https://www.jar-online.net/en/submissions) |
| `jar2023peerreview` | Peer Reviewing and Artistic Research; JAR Peer Review Form | Journal for Artistic Research 网页 2023 | [链接](https://www.jar-online.net/en/peer-reviewing-and-artistic-research) |
| `easterday2014design` | Design-Based Research Process: Problems, Phases, and Applications | Learning and Becoming in Practice: The International Conference of the Learning Sciences (ICLS) 2014 2014 | [链接](https://repository.isls.org/bitstream/1/1130/1/317-324.pdf) |
| `bakker2015introduction` | An Introduction to Design-Based Research with an Example From Statistics Education | Approaches to Qualitative Research in Mathematics Education: Examples of Methodology and Methods 2015 | [链接](https://dspace.library.uu.nl/handle/1874/356250) |
| `scott2020design` | Design-Based Research: A Methodology to Extend and Enrich Biology Education Research | CBE–-Life Sciences Education 2020 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC8711803/) |
| `hopewell2025consortee` | CONSORT 2025 explanation and elaboration: updated guideline for reporting randomised trials | BMJ 2025 | [链接](https://doi.org/10.1136/bmj-2024-081124) |
| `chan2025spirit` | SPIRIT 2025 statement: updated guideline for protocols of randomised trials | BMJ 2025 | [链接](https://doi.org/10.1136/bmj-2024-081477) |
| `whotrialregistration` | Trial registration – International Clinical Trials Registry Platform (ICTRP) | 网页 | [链接](https://www.who.int/tools/clinical-trials-registry-platform/network/trial-registration) |
| `hernan2016target` | Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available | American Journal of Epidemiology 2016 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/) |
| `hernan2020whatif` | Causal Inference: What If | Chapman & Hall/CRC 2020 | [链接](https://miguelhernan.org/whatifbook) |
| `song2010observational` | Observational Studies: Cohort and Case-Control Studies | Plastic and Reconstructive Surgery 2010 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC2998589/) |
| `lachat2016strobenut` | Strengthening the Reporting of Observational Studies in Epidemiology–-Nutritional Epidemiology (STROBE-nut): An Extension of the STROBE Statement | PLoS Medicine 2016 | [链接](https://doi.org/10.1371/journal.pmed.1002036) |
| `nci2025dietprimer` | Dietary Assessment Primer | Epidemiology and Genomics Research Program, Division of Cancer Control and Population Sciences, National Cancer Institute 2025 | [链接](https://epi.grants.cancer.gov/dietary-assessment-primer/) |
| `tennant2021dags` | Use of Directed Acyclic Graphs (DAGs) to Identify Confounders in Applied Health Research: Review and Recommendations | International Journal of Epidemiology 2021 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128477/) |
| `crd2023prospero` | PROSPERO: International Prospective Register of Systematic Reviews | 网页 2023 | [链接](https://www.crd.york.ac.uk/prospero/) |
| `schunemann2013grade` | GRADE Handbook for Grading Quality of Evidence and Strength of Recommendations | The GRADE Working Group 2013 | [链接](https://gdt.gradepro.org/app/handbook/handbook.html) |
| `roth2023trending` | What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature | arXiv:2201.01194 2023 | [链接](https://arxiv.org/abs/2201.01194) |
| `imbens2008rd` | Regression Discontinuity Designs: A Guide to Practice | Journal of Econometrics 2008 | [链接](https://www.nber.org/papers/w13039) |
| `lee2010rd` | Regression Discontinuity Designs in Economics | Journal of Economic Literature 2010 | [链接](https://www.nber.org/papers/w14723) |
| `cameron2015practitioner` | A Practitioner's Guide to Cluster-Robust Inference | Journal of Human Resources 2015 | [链接](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf) |
| `bertrand2004trust` | How Much Should We Trust Differences-in-Differences Estimates? | Quarterly Journal of Economics 2004 | [链接](https://www.nber.org/papers/w8841) |
| `cunningham2026remix` | Causal Inference: The Remix | 网页 2026 | [链接](https://mixtape.scunning.com/) |
| `duflo2007toolkit` | Using Randomization in Development Economics Research: A Toolkit | National Bureau of Economic Research 2006 | [链接](https://www.nber.org/papers/t0333) |
| `jpal2021power` | Power Calculations | J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2021 | [链接](https://www.povertyactionlab.org/resource/power-calculations) |
| `jpal2023randomization` | Randomization | J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2023 | [链接](https://www.povertyactionlab.org/resource/randomization) |
| `jpal2022ethics` | Ethical Conduct of Randomized Evaluations | J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2022 | [链接](https://www.povertyactionlab.org/resource/ethical-conduct-randomized-evaluations) |
| `jpal2021implementation` | Implementation Monitoring | J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2021 | [链接](https://www.povertyactionlab.org/resource/implementation-monitoring) |
| `jpal2023datasecurity` | Data Security Procedures for Researchers | J-PAL Research Resources, Abdul Latif Jameel Poverty Action Lab 2023 | [链接](https://www.povertyactionlab.org/resource/data-security-procedures-researchers) |
| `egappower` | 10 Things You Need to Know About Statistical Power | EGAP Methods Guides, Evidence in Governance and Politics | [链接](https://methods.egap.org/guides/assessing-designs/power_en.html) |
| `egapspillovers` | 10 Things to Know About Spillovers | EGAP Methods Guides, Evidence in Governance and Politics | [链接](https://methods.egap.org/guides/data-collection/spillovers_en.html) |
| `egapclusterrandomization` | 10 Things You Need to Know About Cluster Randomization | EGAP Methods Guides, Evidence in Governance and Politics | [链接](https://methods.egap.org/guides/data-collection/cluster-randomization_en.html) |
| `egaplate` | 10 Things You Need to Know About the Local Average Treatment Effect | EGAP Methods Guides, Evidence in Governance and Politics | [链接](https://methods.egap.org/guides/research-questions/late_en.html) |
| `egapevaluationconversations` | 10 Conversations that Implementers and Evaluators Need to Have | EGAP Methods Guides, Evidence in Governance and Politics | [链接](https://methods.egap.org/guides/implementation/evaluation-conversations_en.html) |
| `boateng2018best` | Best Practices for Developing and Validating Scales for Health, Social, and Behavioral Research: A Primer | Frontiers in Public Health 2018 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC6004510/) |
| `hussey2020hidden` | Hidden Invalidity Among 15 Commonly Used Measures in Social and Personality Psychology | Advances in Methods and Practices in Psychological Science 2020 | [链接](https://osf.io/preprints/psyarxiv/7rbfp) |
| `putnick2016measurement` | Measurement Invariance Conventions and Reporting: The State of the Art and Future Directions for Psychological Research | Developmental Review 2016 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/) |
| `itc2017guidelines` | The ITC Guidelines for Translating and Adapting Tests (Second Edition) | International Test Commission, version 2.4 2017 | [链接](https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf) |
| `klein2005blind` | Blind Analysis in Nuclear and Particle Physics | Annual Review of Nuclear and Particle Science 2005 | [链接](https://inspirehep.net/files/123bf8d8ec8f80e60be89076c65dbdbd) |
| `nist2012ehandbook` | NIST/SEMATECH e-Handbook of Statistical Methods | National Institute of Standards and Technology 2012 | [链接](https://www.itl.nist.gov/div898/handbook/mpc/mpc.htm) |
| `pdg2024intro` | Review of Particle Physics: Introduction | Physical Review D 2024 | [链接](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-rpp-intro.pdf) |
| `lazic2018what` | What exactly is `N' in cell culture and animal experiments? | PLOS Biology 2018 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2005282) |
| `cumming2007error` | Error bars in experimental biology | Journal of Cell Biology 2007 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/) |
| `weissgerber2015beyond` | Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm | PLOS Biology 2015 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128) |
| `rossner2004what` | What's in a picture? The temptation of image manipulation | Journal of Cell Biology 2004 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC2172141/) |
| `henderson2013threats` | Threats to Validity in the Design and Conduct of Preclinical Efficacy Studies: A Systematic Review of Guidelines for In Vivo Animal Experiments | PLoS Medicine 2013 | [链接](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1001489) |
| `kilkenny2009survey` | Survey of the Quality of Experimental Design, Statistical Analysis and Reporting of Research Using Animals | PLoS ONE 2009 | [链接](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0007824) |
| `voelkl2018reproducibility` | Reproducibility of preclinical animal research improves with heterogeneity of study samples | PLoS Biology 2018 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2003693) |
| `perciedusert2017experimental` | The Experimental Design Assistant | PLoS Biology 2017 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2003779) |
| `animalstudyregistry` | animalstudyregistry.org: Welcome | 网页 | [链接](https://www.animalstudyregistry.org/asr_web/index.action) |
| `usgs2018nfmprep` | Preparations for Water Sampling | 网页 2018 | [链接](https://doi.org/10.3133/tm9A1) |
| `usgs2023nfmfield` | Guidelines for Field-Measured Water-Quality Properties | 网页 2023 | [链接](https://doi.org/10.3133/tm9A6.0) |
| `zuur2010protocol` | A protocol for data exploration to avoid common statistical problems | Methods in Ecology and Evolution 2010 | [链接](https://doi.org/10.1111/j.2041-210X.2009.00001.x) |
| `dormann2007spatial` | Methods to account for spatial autocorrelation in the analysis of species distributional data: a review | Ecography 2007 | [链接](https://doi.org/10.1111/j.2007.0906-7590.05171.x) |
| `klein2009sel4` | seL4: Formal Verification of an OS Kernel | Proceedings of the 22nd ACM Symposium on Operating Systems Principles (SOSP) 2009 | [链接](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf) |
| `thabane2010tutorial` | A tutorial on pilot studies: the what, why and how | BMC Medical Research Methodology 2010 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC2824145/) |
| `graham2009makers` | Maker's Schedule, Manager's Schedule | 网页 2009 | [链接](http://www.paulgraham.com/makersschedule.html) |
| `mark2008cost` | The Cost of Interrupted Work: More Speed and Stress | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '08) 2008 | [链接](https://www.ics.uci.edu/~gmark/chi08-mark.pdf) |
| `neurips2025llm` | NeurIPS 2025 Policy on the Use of Large Language Models | Conference on Neural Information Processing Systems 2025 | [链接](https://neurips.cc/Conferences/2025/LLM) |
| `icse2026cfp` | ICSE 2026 Research Track: Call for Papers | 网页 2025 | [链接](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) |
| `neurips2025checklist` | NeurIPS Paper Checklist Guidelines | 网页 | [链接](https://neurips.cc/public/guides/PaperChecklist) |
| `arr2024responsible` | Responsible NLP Research Checklist | 网页 2024 | [链接](https://aclrollingreview.org/responsibleNLPresearch/) |
| `ieeesp2026cfp` | 47th IEEE Symposium on Security and Privacy: Call for Papers | 网页 2025 | [链接](https://sp2026.ieee-security.org/cfpapers.html) |
| `ndss2026cfp` | NDSS Symposium 2026 Call for Papers | 网页 2025 | [链接](https://www.ndss-symposium.org/ndss2026/submissions/call-for-papers/) |
| `ccs2025cfp` | ACM Conference on Computer and Communications Security (CCS) 2025: Call for Papers | 网页 2025 | [链接](https://www.sigsac.org/ccs/CCS2025/call-for-papers/) |
| `osdi2026cfp` | OSDI '26 Call for Papers: 20th USENIX Symposium on Operating Systems Design and Implementation | 网页 2025 | [链接](https://www.usenix.org/conference/osdi26/call-for-papers) |
| `sosp2025cfp` | SOSP 2025 Call for Papers: The 31st ACM Symposium on Operating Systems Principles | 网页 2025 | [链接](https://sigops.org/s/conferences/sosp/2025/cfp.html) |
| `stoc2026cfp` | STOC 2026 Call for Papers: 58th ACM Symposium on Theory of Computing | 网页 2025 | [链接](https://acm-stoc.org/stoc2026/stoc2026-cfp.html) |
| `pldi2026cfp` | PACMPL Issue PLDI 2026: Call for Papers | 网页 2025 | [链接](https://pldi26.sigplan.org/track/pldi-2026-papers) |
| `popl2026cfp` | PACMPL Issue POPL 2026: Call for Papers | 网页 2025 | [链接](https://popl26.sigplan.org/track/POPL-2026-popl-research-papers) |
| `chi2026papers` | CHI 2026 Papers: Call for Papers, Guide to a Successful Submission, Papers Review Process, Guide to Reviewing Papers, Contributions to CHI, and Anonymization Policy | 网页 2025 | [链接](https://chi2026.acm.org/authors/papers/) |
| `greenberg2008usability` | Usability Evaluation Considered Harmful (Some of the Time) | Proceedings of the SIGCHI Conference on Human Factors in Computing Systems 2008 | [链接](https://www.billbuxton.com/usabilityHarmful.pdf) |
| `thompson2002harmonized` | Harmonized guidelines for single-laboratory validation of methods of analysis (IUPAC Technical Report) | Pure and Applied Chemistry 2002 | [链接](https://publications.iupac.org/pac/2002/pdf/7405x0835.pdf) |
| `aps2011uncertainty` | Editorial: Uncertainty Estimates | Physical Review A 2011 | [链接](https://doi.org/10.1103/PhysRevA.83.040001) |
| `siamsinumabout` | SIAM Journal on Numerical Analysis (SINUM) | Journal web page 2024 | [链接](https://www.siam.org/publications/journals/siam-journal-on-numerical-analysis-sinum) |
| `siamsiscabout` | SIAM Journal on Scientific Computing (SISC) | Journal web page 2024 | [链接](https://www.siam.org/publications/journals/siam-journal-on-scientific-computing-sisc) |
| `amsbullabout` | About Bulletin of the American Mathematical Society | Journal web page 2024 | [链接](https://www.ams.org/publications/journals/journalsframework/aboutbull) |
| `amssteeleexposition` | Leroy P. Steele Prize for Mathematical Exposition | Prize web page 2024 | [链接](https://www.ams.org/prizes-awards/paview.cgi?parent_id=26) |
| `fgedmiame` | MIAME: Minimum Information About a Microarray Experiment | Project web page | [链接](https://www.fged.org/projects/miame/) |
| `fgedminseqe` | MINSEQE: Minimum Information about a high-throughput SEQuencing Experiment | Project web page 2012 | [链接](https://www.fged.org/projects/minseqe/) |
| `odea2021preferred` | Preferred reporting items for systematic reviews and meta-analyses in ecology and evolutionary biology: a PRISMA extension | Biological Reviews 2021 | [链接](https://doi.org/10.1111/brv.12721) |
| `hooijmans2014syrcle` | SYRCLE's risk of bias tool for animal studies | BMC Medical Research Methodology 2014 | [链接](https://doi.org/10.1186/1471-2288-14-43) |
| `runge2019inferring` | Inferring causation from time series in Earth system sciences | Nature Communications 2019 | [链接](https://doi.org/10.1038/s41467-019-10105-3) |
| `nevo2010taking` | Taking the Dogma out of Econometrics: Structural Modeling and Credible Inference | Journal of Economic Perspectives 2010 | [链接](https://www.aeaweb.org/articles?id=10.1257/jep.24.2.69) |
| `low2017use` | The Use of Structural Models in Econometrics | Journal of Economic Perspectives 2017 | [链接](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33) |
| `keane2010structural` | A Structural Perspective on the Experimentalist School | Journal of Economic Perspectives 2010 | [链接](https://www.aeaweb.org/articles?id=10.1257/jep.24.2.47) |
| `kydland1996computational` | The Computational Experiment: An Econometric Tool | Journal of Economic Perspectives 1996 | [链接](https://www.aeaweb.org/articles?id=10.1257/jep.10.1.69) |
| `hansen1996empirical` | The Empirical Foundations of Calibration | Journal of Economic Perspectives 1996 | [链接](https://www.aeaweb.org/articles?id=10.1257/jep.10.1.87) |
| `skocpol1980uses` | The Uses of Comparative History in Macrosocial Inquiry | Comparative Studies in Society and History 1980 | [链接](https://doi.org/10.1017/S0010417500009282) |
| `mahoney2005clarifying` | Clarifying Comparative-Historical Methodology | Qualitative Methods: Newsletter of the American Political Science Association Organized Section on Qualitative Methods 2005 | [链接](https://doi.org/10.5281/zenodo.998194) |
| `vanhoecke2015methodology` | Methodology of Comparative Legal Research | Law and Method 2015 | [链接](https://doi.org/10.5553/REM/.000010) |
| `duve2014european` | European Legal History – Concepts, Methods, Challenges | Entanglements in Legal History: Conceptual Approaches 2014 | [链接](https://www.lhlt.mpg.de/1009830/gplh_1_duve.pdf) |
| `atiq2025nature` | The Nature of Law | The Stanford Encyclopedia of Philosophy 2025 | [链接](https://plato.stanford.edu/entries/lawphil-nature/) |
| `weisberg2021formal` | Formal Epistemology | The Stanford Encyclopedia of Philosophy 2021 | [链接](https://plato.stanford.edu/entries/formal-epistemology/) |
| `lsalanguage2026transparency` | Language: Research Transparency; Preparing Your Materials | Journal website, Cambridge University Press 2026 | [链接](https://www.cambridge.org/core/journals/language/information/journal-policies/research-transparency) |
| `vasishth2016statistical` | Statistical Methods for Linguistic Research: Foundational Ideas – Part I | Language and Linguistics Compass 2016 | [链接](https://arxiv.org/abs/1601.01126) |
| `wieling2018reproducibility` | Reproducibility in Computational Linguistics: Are We Willing to Share? | Computational Linguistics 2018 | [链接](https://aclanthology.org/J18-4003/) |
| `wallach2023proposal` | Proposal and extensive test of a calibration protocol for crop phenology models | Agronomy for Sustainable Development 2023 | [链接](https://doi.org/10.1007/s13593-023-00900-0) |
| `boote2013protocols` | Protocols for AgMIP Crop Model Improvement Teams | Agricultural Model Intercomparison and Improvement Project (AgMIP) 2013 | [链接](https://agmip.org/wp-content/uploads/2019/03/Protocols-for-AgMIP-Crop-Model-Improvement-Teams.pdf) |
| `carletto2013guesstimates` | From Guesstimates to GPStimates: Land Area Measurement and Implications for Agricultural Analysis | World Bank 2013 | [链接](https://hdl.handle.net/10986/15910) |
| `krupnik2019does` | Does Size Matter? A Critical Review of Meta-analysis in Agronomy | Experimental Agriculture 2019 | [链接](https://doi.org/10.1017/S0014479719000012) |
| `sargeant2020scoping` | Scoping Reviews, Systematic Reviews, and Meta-Analysis: Applications in Veterinary Medicine | Frontiers in Veterinary Science 2020 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC6997489/) |
| `macleod2021mdar` | The MDAR (Materials Design Analysis Reporting) Framework for transparent reporting in the life sciences | Proceedings of the National Academy of Sciences 2021 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC8092464/) |
| `jacoby2020crosscultural` | Cross-Cultural Work in Music Cognition: Challenges, Insights, and Recommendations | Music Perception 2020 | [链接](https://doi.org/10.1525/mp.2020.37.3.185) |
| `epa2026caddis` | Causal Analysis/Diagnosis Decision Information System (CADDIS) | 网页 2026 | [链接](https://www.epa.gov/caddis) |
| `cee2022guidelines` | Guidelines and Standards for Evidence Synthesis in Environmental Management. Version 5.1 | 网页 2022 | [链接](https://environmentalevidence.org/information-for-authors/) |
| `mokoena2026adsorption` | What is the adsorption efficiency and capacity of biodegradable polymer blend foams filled with carbonaceous materials in the removal of heavy metals from water? A systematic review protocol | Environmental Evidence 2026 | [链接](https://europepmc.org/article/PMC/PMC13151128) |
| `plosbiology2018importance` | The importance of being second | PLOS Biology 2018 | [链接](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2005203) |
| `oriwhistleblowers` | Whistleblowers (Handling Misconduct – Complainant) | 网页 | [链接](https://ori.hhs.gov/whistleblowers) |
| `haddaway2018roses` | ROSES RepOrting standards for Systematic Evidence Syntheses: pro forma, flow-diagram and descriptive summary of the plan and conduct of environmental systematic reviews and systematic maps | Environmental Evidence 2018 | [链接](https://doi.org/10.1186/s13750-018-0121-7) |
| `albert2003authorship` | How to Handle Authorship Disputes: A Guide for New Researchers | The COPE Report 2003 | [链接](https://web.archive.org/web/20241128073038/https://publicationethics.org/files/2003pdf12_0.pdf) |
| `cope2019authorship` | COPE Discussion Document: Authorship | Committee on Publication Ethics 2019 | [链接](https://doi.org/10.24318/cope.2019.3.3) |
| `thomson1999young` | The Young Person's Guide to Writing Economic Theory | Journal of Economic Literature 1999 | [链接](https://doi.org/10.1257/jel.37.1.157) |
| `te2026guidelines` | Guidelines for Referees | 网页 2026 | [链接](https://www.econometricsociety.org/publications/theoretical-economics/policies/guidelines-for-referees) |
| `asljslabout` | The Journal of Symbolic Logic | 网页 | [链接](https://aslonline.org/journals/the-journal-of-symbolic-logic/) |
| `aslbslabout` | The Bulletin of Symbolic Logic | 网页 | [链接](https://aslonline.org/journals/the-bulletin-of-symbolic-logic/) |
| `studialogicaaims` | Studia Logica: Aims and Scope | 网页 | [链接](https://link.springer.com/journal/11225/aims-and-scope) |
| `fernandes2020alphabetic` | Alphabetic order of authors in scholarly publications: a bibliometric study for 27 scientific fields | Scientometrics 2020 | [链接](https://doi.org/10.1007/s11192-020-03686-0) |
| `iupacgoldbookmechanism` | mechanism (of a reaction) | IUPAC Compendium of Chemical Terminology (the Gold Book), 5th ed., online version 5.0.0 2025 | [链接](https://doi.org/10.1351/goldbook.M03804) |
| `mata2017benchmarking` | Benchmarking Quantum Chemical Methods: Are We Heading in the Right Direction? | Angewandte Chemie International Edition 2017 | [链接](https://doi.org/10.1002/anie.201611308) |
| `scipost2025physics` | SciPost Physics: About (Acceptance Criteria) | 网页 | [链接](https://scipost.org/SciPostPhys/about) |
| `jhepabout` | JHEP about | 网页 | [链接](https://jhep.sissa.it/jhep/help/JHEP/JHEP_about.jsp) |
| `naturemethodsaims` | Aims & Scope | Journal 网页 | [链接](https://www.nature.com/nmeth/aims) |
| `ploscompbiolsubmission` | Submission Guidelines | Journal 网页 | [链接](https://journals.plos.org/ploscompbiol/s/submission-guidelines) |
| `hegerl2010good` | Good Practice Guidance Paper on Detection and Attribution Related to Anthropogenic Climate Change | Meeting Report of the Intergovernmental Panel on Climate Change Expert Meeting on Detection and Attribution of Anthropogenic Climate Change 2010 | [链接](https://archive.ipcc.ch/pdf/supporting-material/expert-meeting-detection-anthropogenic-2009-09.pdf) |
| `cabiagbioevidencesynthesis` | Evidence Synthesis: Preparing your manuscript | Journal 网页 | [链接](https://cabiagbio.biomedcentral.com/submission-guidelines/preparing-your-manuscript/evidence-synthesis) |
| `rosenzweig2013agricultural` | The Agricultural Model Intercomparison and Improvement Project (AgMIP): Protocols and pilot studies | Agricultural and Forest Meteorology 2013 | [链接](https://doi.org/10.1016/j.agrformet.2012.09.011) |
| `fancourt2019evidence` | What is the evidence on the role of the arts in improving health and well-being? A scoping review | WHO Regional Office for Europe 2019 | [链接](https://iris.who.int/handle/10665/329834) |
| `apa2024aesthetics` | Psychology of Aesthetics, Creativity, and the Arts: Journal Scope Statement and Submission Guidelines | Journal web page 2024 | [链接](https://www.apa.org/pubs/journals/aca) |
| `sage2024musicscience` | Music & Science: Submission Guidelines | Journal web page 2024 | [链接](https://journals.sagepub.com/author-instructions/MNS) |
| `focs2025cfp` | FOCS 2025: Call for Papers | 66th Annual IEEE Symposium on Foundations of Computer Science 2025 | [链接](https://focs.computer.org/2025/call-for-papers/) |
| `soda2025cfp` | SODA25 Submissions | ACM-SIAM Symposium on Discrete Algorithms (SODA25) 2024 | [链接](https://www.siam.org/conferences-events/siam-conferences/soda25/submissions/) |
| `waltman2012empirical` | An empirical analysis of the use of alphabetical authorship in scientific publishing | arXiv:1206.4863 2012 | [链接](https://arxiv.org/abs/1206.4863) |
| `acm2021humanparticipants` | ACM Publications Policy on Research Involving Human Participants and Subjects | Association for Computing Machinery 2021 | [链接](https://www.acm.org/publications/policies/research-involving-human-participants-and-subjects) |
| `bjork2013publishing` | The publishing delay in scholarly peer-reviewed journals | Journal of Informetrics 2013 | [链接](https://web.archive.org/web/20131008075840/http://openaccesspublishing.org/oa11/article.pdf) |
| `lisee2008conference` | Conference proceedings as a source of scientific information: A bibliometric analysis | Journal of the American Society for Information Science and Technology 2008 | [链接](https://crctcs.openum.ca/files/sites/60/2015/10/Proceedings.pdf) |
| `aerapublicationsfaq` | Publications FAQs | 网页 | [链接](https://www.aera.net/Publications/Publications-FAQs) |
| `tcnj2023polisci` | Disciplinary Standards for Reappointment, Tenure, and Promotion in Political Science | 网页 2023 | [链接](https://academicaffairs.tcnj.edu/wp-content/uploads/sites/171/2023/05/Political-Science-Disciplinary-Standards.pdf) |
| `apsr2024editorial` | American Political Science Review Editorial Report: Executive Summary (Fall 2023) | Political Science Today 2024 | [链接](https://www.cambridge.org/core/product/CFCD95D2AF8F273A6CA9D1ABAD66BD47/core-reader) |
| `ernst2023registered` | Registered reports in software engineering | Empirical Software Engineering 2023 | [链接](https://arxiv.org/abs/2302.03649) |
| `tcps2022ethical` | Tri-Council Policy Statement: Ethical Conduct for Research Involving Humans – TCPS 2 (2022) | Government of Canada, Panel on Research Ethics 2022 | [链接](https://ethics.gc.ca/eng/tcps2-eptc2_2022_chapter2-chapitre2.html) |
| `thinkchecksubmit2023checklist` | Journals: Think. Check. Submit. Checklist | 网页 2023 | [链接](https://thinkchecksubmit.org/journals/) |
| `acm2025authorship` | ACM Policy on Authorship | 网页 2025 | [链接](https://www.acm.org/publications/policies/new-acm-policy-on-authorship) |
| `cattaneo2020practical` | A Practical Introduction to Regression Discontinuity Designs: Foundations | Cambridge University Press 2020 | [链接](https://arxiv.org/abs/1911.09511) |
| `abadie2021using` | Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects | Journal of Economic Literature 2021 | [链接](https://hdl.handle.net/1721.1/144417) |
| `altman2005treatment` | Treatment allocation by minimisation | BMJ 2005 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC556084/) |
| `prismadta2018` | PRISMA-Diagnostic Test Accuracy | 网页 2024 | [链接](https://www.prisma-statement.org/dta) |
| `deeks2023cochrane` | Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy | Cochrane 2023 | [链接](https://www.cochrane.org/authors/handbooks-and-manuals/handbook-systematic-reviews-diagnostic-test-accuracy) |
| `cdu2025distress` | Distress Protocol (template) | Charles Darwin University Research Integrity and Ethics 2025 | [链接](https://www.cdu.edu.au/files/2025-09/Distress%20Protocol%20Template.docx) |
| `asce2025publishing` | Publishing in ASCE Journals | ASCE Library | [链接](https://ascelibrary.org/author-center/journal) |
| `mendez2020enlisting` | Enlisting the Gatekeeper: Chain-Referral and Elite Access in Foreign Policy Analysis | SAGE Research Methods Cases 2020 | [链接](https://researchonline.lse.ac.uk/id/eprint/103025/4/Mendez_2020_Foreign_Policy_Analysis_Case_Study.pdf) |
| `clifford2020tipsheet` | Tipsheet – Interviewing Elites | Duke Initiative on Survey Methodology 2020 | [链接](https://dism.duke.edu/files/2020/05/Tipsheet-Elite_Interviews.pdf) |
| `bayliss2022radiocarbon` | Radiocarbon Dating and Chronological Modelling: Guidelines and Best Practice | Historic England 2022 | [链接](https://historicengland.org.uk/images-books/publications/radiocarbon-dating-chronological-modelling/heag312-radiocarbon-dating/) |
| `saa2023styleguide` | Editorial Policy, Information for Authors, and Style Guide for American Antiquity, Latin American Antiquity, and Advances in Archaeological Practice | 网页 2023 | [链接](https://www.saa.org/common/Uploaded%20files/saadocs/Publications/Style%20Guide/saa-style-guide_english_updated_2021_final08023c15928949dabd02faafb269fb1c.pdf) |
| `amantiquity2026instructions` | American Antiquity: Preparing your materials (author instructions) | 网页 2026 | [链接](https://www.cambridge.org/core/journals/american-antiquity/information/author-instructions/preparing-your-materials) |
| `thieberger2019recording` | Recording Audio and Keeping Track of Recordings | 网页 2019 | [链接](https://www.paradisec.org.au/blog/wp-content/uploads/2019/08/Honiara-Audio.pdf) |
| `roseslabrada2022audiovisual` | Audiovisual Recording Advice | 网页 2022 | [链接](https://depts.washington.edu/jacobsf/Documents/Audiovisual_recording_advice.pdf) |
| `fda1996qsr` | Medical Devices; Current Good Manufacturing Practice (CGMP) Final Rule; Quality System Regulation | Federal Register, Vol. 61, No. 195, pp. 52602–52662 1996 | [链接](https://www.govinfo.gov/content/pkg/FR-1996-10-07/html/96-25720.htm) |
| `eu2009contained` | Directive 2009/41/EC of the European Parliament and of the Council of 6 May 2009 on the contained use of genetically modified micro-organisms (Recast) | Official Journal of the European Union, L 125, pp. 75–97 2009 | [链接](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009L0041) |
| `npc2020biosecurity` | Biosecurity Law of the People's Republic of China | 网页 2020 | [链接](https://subsites.chinadaily.com.cn/npc/2020-10/17/c_703568.htm) |
| `igsnglossary` | Glossary | IGSN e.V. 网页 | [链接](https://ev.igsn.org/glossary) |
| `igsnagents` | IGSN Agents and Registration | IGSN e.V. 网页 | [链接](https://ev.igsn.org/resources/igsn-agents-and-registration) |
| `ukrio2023procedure` | Procedure for the Investigation of Misconduct in Research | UK Research Integrity Office 2023 | [链接](https://ukrio.org/wp-content/uploads/Procedure-for-the-Investigation-of-Misconduct-in-Research_Accessible.pdf) |
| `npc2024cultural` | Law of the People's Republic of China on Cultural Relics Protection | 网页 2024 | [链接](https://subsites.chinadaily.com.cn/npc/2024-11/08/c_1115996.htm) |
| `npc2024legislature` | Top Legislature Concludes Standing Committee Session | 网页 2024 | [链接](https://subsites.chinadaily.com.cn/npc/2024-04/28/c_983112.htm) |
| `tetley1999mixed` | Mixed jurisdictions: common law vs civil law (codified and uncodified) (Part I) | Uniform Law Review - Revue de droit uniforme 1999 | [链接](https://unidroit.org/english/publications/review/articles/1999-3-tetley1-e.pdf) |
| `wipo2025international` | An International Guide to Patent Case Management for Judges | 网页 2025 | [链接](https://www.wipo.int/patent-judicial-guide/en/full-guide/china/4.1.4) |
| `npc2020copyright` | Copyright Law of the People's Republic of China (Amended in 2020) | 网页 2020 | [链接](https://subsites.chinadaily.com.cn/npc/2020-11/11/c_674691.htm) |
| `surrey2010excavation` | Excavation Recording Manual | Surrey Archaeological Society, Research Committee 2010 | [链接](https://d10.surreyarchaeology.org.uk/sites/surreyarchaeology.org.uk/files/Excavation%20Recording%20Manual.pdf) |
| `fda2024qmsr` | Medical Devices; Quality System Regulation Amendments | Federal Register, Vol. 89, No. 23, pp. 7496–7525 (Final rule, FR Doc. 2024-01709) 2024 | [链接](https://www.govinfo.gov/content/pkg/FR-2024-02-02/html/2024-01709.htm) |
| `fda2026withdrawn` | Withdrawn or Expired Guidance | FDA website, Center for Devices and Radiological Health 2026 | [链接](https://www.fda.gov/medical-devices/guidance-documents-medical-devices-and-radiation-emitting-products/withdrawn-or-expired-guidance) |
| `mcinnes2018preferred` | Preferred Reporting Items for a Systematic Review and Meta-analysis of Diagnostic Test Accuracy Studies: The PRISMA-DTA Statement | JAMA 2018 | [链接](https://jamanetwork.com/journals/jama/fullarticle/2670259) |
| `prismadta2018checklist` | PRISMA-DTA Checklist | 网页 | [链接](https://www.prisma-statement.org/s/PRISMA-DTA-Checklist-xh5j.pdf) |
| `cohen2016stard` | STARD 2015 guidelines for reporting diagnostic accuracy studies: explanation and elaboration | BMJ Open 2016 | [链接](https://pmc.ncbi.nlm.nih.gov/articles/PMC5128957/) |
| `whiting2011quadas` | QUADAS-2: A Revised Tool for the Quality Assessment of Diagnostic Accuracy Studies | Annals of Internal Medicine 2011 | [链接](https://pubmed.ncbi.nlm.nih.gov/22007046/) |
| `eu2025dsadata` | Commission Delegated Regulation (EU) 2025/2050 of 1 July 2025 supplementing Regulation (EU) 2022/2065 of the European Parliament and of the Council by laying down the technical conditions and procedures under which providers of very large online platforms and of very large online search engines are to share data with vetted researchers | Official Journal of the European Union, L series, 2025/2050, 9 October 2025 2025 | [链接](https://eur-lex.europa.eu/eli/reg_del/2025/2050/oj) |

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
