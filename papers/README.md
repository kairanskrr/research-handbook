# 论文索引

- 引用信息：[`references.bib`](references.bib)，下表"key"一列对应其中的条目。
- 下载：在仓库根目录运行 `bash scripts/fetch_papers.sh`，有免费全文的 PDF 会保存为 `papers/pdf/<key>.pdf`。
- 核实日期：2026-10-02 / 2026-10-05。表中"免费全文"一列只列出已确认的合法来源（作者主页、机构库、arXiv、开放获取期刊）。

## 关于 PDF 是否提交进仓库

`papers/pdf/` 默认已加入 `.gitignore`，PDF 不会被提交。原因是各论文的版权不同：
- **可以提交**：开放许可的论文，例如 PRISMA 2009（PLoS，CC BY）、PRISMA 2020（BMJ，CC BY 4.0）、Erren et al. 2007（PLoS，CC BY）、Petersen et al. 2008（出版社版本 CC BY 4.0）。如果要提交，需要用 `git add -f`。
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
| `runeson2009guidelines` | Guidelines for conducting and reporting case study research in software engineering | EMSE 2009 | 可能开放获取（Springer，未能确认） |
| `wohlin2024experimentation` | Experimentation in Software Engineering（第 2 版） | Springer 2024 | 💰 |
| `felderer2020contemporary` | Contemporary Empirical Methods in Software Engineering | Springer 2020 | 💰（仅第 17 章开放获取） |
| `zhang2026survey` | A Survey on Large Language Models for Software Engineering | Sci China Inf Sci 2026 | [arXiv:2312.15223](https://arxiv.org/abs/2312.15223)（预印本） |
| `zhang2024unifying` | Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code | TMLR 2024 | [arXiv:2311.07989](https://arxiv.org/abs/2311.07989) |
| `hamming1986you` | You and Your Research | 1986 年演讲 | [文字稿](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html) |
| `erren2007ten` | Ten Simple Rules for Doing Your Best Research, According to Hamming | PLoS Comput Biol 2007 | [PLoS](https://doi.org/10.1371/journal.pcbi.0030213)（CC BY） |
| `schulman2020opinionated` | An Opinionated Guide to ML Research | 博客 2020 | [网页](http://joschu.net/blog/opinionated-guide-ml-research.html) |
| `perez2024tips` | Tips for Empirical Alignment Research | 博客 2024 | [网页](https://www.alignmentforum.org/posts/dZFpEdKyb9Bf4xYn7/tips-for-empirical-alignment-research) |
| `peytonjones2013write` | How to Write a Great Research Paper | 演讲 | [网页](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/) |
| `keshav2007read` | How to Read a Paper | ACM SIGCOMM CCR 2007 | 未确认 |
| `karpathy2016survival` | A Survival Guide to a PhD | 博客 2016 | [网页](http://karpathy.github.io/2016/09/07/phd/) |

## 待获取

以下资料有价值，但目前无法读到全文。获取后请保存为 `papers/pdf/<key>.pdf`（不提交进仓库）。

| 优先级 | key | 用途 | 情况 |
|---|---|---|---|
| 高 | `petersen2015guidelines` | 映射研究的更新版指南和评估清单 | 出版社付费。BTH 机构库可能有免费 PDF：[diva2:815606](http://www.diva-portal.org/smash/record.jsf?pid=diva2:815606)，需要用浏览器确认 |
| 高 | `gomez2014understanding` | 复现研究的分类，整理"复现研究"的核心依据 | 付费，未找到自存档版本 |
| 中 | `wohlin2024experimentation` | 威胁效度的经典论述 | 付费书籍；只需要讲效度的部分（2012 年版位于 Planning 一章） |
| 中 | `arcuri2014hitchhiker` | 工具评测中的统计检验 | 付费；ICSE 2011 短版 `arcuri2011practical` 可能在 ACM 免费 |
| 中 | `shull2008role` | 复现研究的定位 | 付费 |
| 低 | `carver2010towards` | 复现研究的报告规范 | 作者主页有 PDF，但需要用浏览器下载 |
| 低 | `felderer2020contemporary` | 多种实证方法的较新综述 | 需要先看目录挑选章节 |
| 低 | `runeson2009guidelines` | 案例研究指南中的效度讨论 | 可能开放获取，未能确认 |
