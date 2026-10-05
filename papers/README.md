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
| `herzig2013bug` | It's not a bug, it's a feature: how misclassification impacts bug prediction | ICSE 2013 | [Saarland](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf) |
| `kalliamvakou2014promises` | The promises and perils of mining GitHub | MSR 2014 | [作者主页](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf) |
| `kalliamvakou2016indepth` | An in-depth study of the promises and perils of mining GitHub | EMSE 2016 | [作者主页](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf) |
| `arcuri2011practical` | A practical guide for using statistical tests to assess randomized algorithms in software engineering | ICSE 2011 | 未确认（ACM 上可能免费） |
| `arcuri2014hitchhiker` | A Hitchhiker's guide to statistical tests for assessing randomized algorithms in software engineering | STVR 2014 | 💰 |
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
| `georges2007statistically` | Statistically rigorous Java performance evaluation | OOPSLA 2007 | 未确认 |
| `kalibera2013rigorous` | Rigorous benchmarking in reasonable time | ISMM 2013 | 未确认 |
| `blackburn2008wake` | Wake up and smell the coffee: evaluation methodology for the 21st century | CACM 2008 | 未确认 |
| `hoefler2015scientific` | Scientific benchmarking of parallel computing systems | SC 2015 | 未确认 |
| `baltes2022sampling` | Sampling in software engineering research: a critical review and guidelines | EMSE 2022 | [arXiv:2002.07764](https://arxiv.org/abs/2002.07764) |
| `siegmund2015views` | Views on Internal and External Validity in Empirical Software Engineering | ICSE 2015 | 未确认 |
| `herley2017sok` | SoK: Science, Security and the Elusive Goal of Security as a Scientific Pursuit | IEEE S&P 2017 | 未确认 |
| `bailey2012menlo` | The Menlo Report | IEEE S&P 2012 | [CAIDA](https://www.caida.org/publications/papers/2012/menlo_report/menlo_report.pdf) |
| `partridge2016ethical` | Ethical considerations in network measurement papers | CACM 2016 | 未确认 |
| `wilson2014best` | Best Practices for Scientific Computing | PLoS Biology 2014 | [PLoS](https://doi.org/10.1371/journal.pbio.1001745)（CC BY） |
| `wilson2017good` | Good enough practices in scientific computing | PLoS Comput Biol 2017 | [PLoS](https://doi.org/10.1371/journal.pcbi.1005510)（CC BY） |
| `sandve2013ten` | Ten Simple Rules for Reproducible Computational Research | PLoS Comput Biol 2013 | [PLoS](https://doi.org/10.1371/journal.pcbi.1003285)（CC BY） |
| `carlini2022checklist` | Research Paper Release Checklist | 博客 2022 | [网页](https://nicholas.carlini.com/writing/2022/paper-release-checklist.html) |

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
