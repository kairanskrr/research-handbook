# Rameder, di Angelo & Salzer 2022：Review of Automated Vulnerability Analysis of Smart Contracts on Ethereum

- 资料：`rameder2022review`，[原文（Frontiers 开放获取 PDF）](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2022.814977/pdf)
- 版本：Frontiers in Blockchain 第 5 卷，文章号 814977，2022 年 3 月 24 日出版，CC BY 许可。DOI 10.3389/fbloc.2022.814977（已在 Crossref 核对）。位置写期刊页码（与 PDF 页码一致）。

### E1

- 位置：摘要，第 1 页
- 原文："Moreover, publications keep emerging with different focus, scope, and quality, making it difficult to keep up with the field and to identify relevant trends. Thus, regular reviews are essential to keep pace with the varied developments in a structured manner."
- 要点：相关论文不断涌现，侧重点、范围和质量各不相同，很难跟上这个领域，所以需要定期做有结构的综述。

### E2

- 位置：§1 Introduction，第 2 页
- 原文："We assess the publications with respect to the following questions: [...] Which vulnerabilities are mentioned? How are vulnerabilities classified? [...] Which methods do automated tools use to detect vulnerabilities? [...] Which vulnerabilities are addressed by the tools? [...] How are the tools evaluated? [...] What are the open challenges of automated detection?"
- 要点：综述先列出要回答的问题：有哪些漏洞、怎么分类，工具用什么方法检测、覆盖哪些漏洞、怎么评估，以及还有哪些未解决的难题。

### E3

- 位置：§1 Introduction，第 2 页
- 原文："Our contributions are [...] a list of high quality publications, with the selection based on clear criteria, [...] an overview and taxonomy of vulnerabilities, methods and tools, [...] a discussion of the state of the art with respect to automated analysis, and [...] the identification of gaps and challenges."
- 要点：论文的贡献有四项：按明确标准选出的高质量文献清单、漏洞/方法/工具的分类，对现状的讨论，以及指出空白和挑战。

### E4

- 位置：§2 Systematic Review，第 2 页
- 原文："For the literature review, we apply a rigorous protocol to ensure comprehensive and reproducible results as suggested in several guidelines (Brereton et al., 2007; Kitchenham and Charters, 2007; Okoli, 2015; Snyder, 2019)."
- 要点：作者按 Kitchenham & Charters 2007 等几份指南制定了严格的综述方案，目的是让结果全面、可重复。

### E5

- 位置：§2.1.1 Initial Search，第 2–3 页
- 原文："we choose the primary search term smart contract and a disjunction of the terms security, vulnerability, bug, analysis, detection, verification and tool." / "The initial search was conducted at the end of January 2021 and yielded a total of 1326 results, with 546 contributed by Google Scholar, 229 by IEEE Xplore, 199 by ScienceDirect, 178 by TU Wien CatalogPlus, and 174 by ACM Digital Library."
- 要点：检索词是 smart contract 加上 security、vulnerability、bug 等词中任意一个；2021 年 1 月底在五个数据库检索，共得到 1326 条结果，每个库各贡献多少条都写明了。

### E6

- 位置：§2.1.2 Exclusion and Inclusion Criteria，第 3 页
- 原文："Exclusion Criteria: We exclude search results if the work is 1) not written in English, 2) a patent, blog entry or other grey literature, 3) not accessible on-line via the library network of TU Wien, 4) published before 2014, and 5) unrelated to Ethereum."
- 要点：排除标准有五条：非英文、专利或博客等灰色文献、学校图书馆网络无法获取、2014 年以前发表、与以太坊无关。

### E7

- 位置：§2.1.2–§2.1.3，第 3 页
- 原文："Inclusion Criteria: We include search results if it is clear from title and abstract that the work is related to 1) smart contract security bugs or vulnerabilities, 2) smart contract vulnerability detection, analysis or security verification tools, or 3) automated detection or verification methods." / "After removing 299 duplicates and excluding 724 articles according to the criteria above, we group the remaining 303 studies into three classes"
- 要点：只看标题和摘要判断是否纳入；去掉 299 篇重复、按标准排除 724 篇后，剩下 303 篇，再分成系统综述、普通综述和原始研究三类。

### E8

- 位置：§2.2.2 Contextual and Final Data Quality，第 4 页；§2.3 Data Extraction，第 5 页
- 原文："For the sake of readability, and ease of classification, we map CDQ and FDQ to a three point Likert scale, by calling a score low if it is below 0.5, high if it is at least 0.8, and medium otherwise. We exclude a study from the survey if its CDQ or FDQ is low." / "After quality appraisal and reclassification, we are left with 8 systematic literature reviews, 38 surveys and 149 primary studies"
- 要点：每篇文献按事先定好的问题打质量分，低于 0.5 算低分并排除；质量评估后剩下 8 篇系统综述、38 篇普通综述和 149 篇原始研究，进入数据提取。

### E9

- 位置：§4.2 Academic Classifications，第 8 页
- 原文："Atzei et al. (2017) create one of the first taxonomies for vulnerabilities." / "Although this work is referenced in several other papers, we have found some issues and inconsistencies regarding the classification of concrete vulnerabilities."
- 要点：作者认为 Atzei 等人 2017 年的分类是最早的漏洞分类之一，被很多论文引用，但其中具体漏洞的归类有一些问题和不一致。

### E10

- 位置：§4.1 Consolidated Taxonomy，第 8 页
- 原文："In total, we extracted 54 vulnerabilities from the collected papers. [...] Our consolidated classification in Table 6 consists of 10 classes of vulnerabilities."
- 要点：作者从文献中整理出 54 种漏洞，归成 10 大类。

### E11

- 位置：§6 Tools for Automated Security Analysis，第 12–13 页
- 原文："The 24 SLRs and surveys as well as the 149 primary studies we finally selected describe a total of 140 tools for analyzing the security of Ethereum smart contracts, with 83 published open source." / "The vast majority of tools (113, 80.7%) employs static methods, about a third (43, 30.7%) uses dynamic methods, and several (16, 11.4%) use both."
- 要点：入选文献共描述了 140 个以太坊智能合约安全分析工具，其中 83 个开源；约八成（113 个）用静态方法，约三成（43 个）用动态方法。

### E12

- 位置：§7 Benchmarks and Test Sets，第 13 页
- 原文："The number of contracts per test set (fourth column) varies between 6 and 47 541. More than half of the projects also include contracts that were manually verified to be true or false positives with respect to some property, in order to serve as a ground truth."
- 要点：各个测试集的合约数量从 6 个到 47541 个不等；一半以上的项目包含人工核对过的合约，作为判断对错的标准答案（ground truth）。

### E13

- 位置：§9.1 New Vulnerabilities and Tools，第 17 页
- 原文："At the same time, there is not a single tool that covers all documented vulnerabilities."
- 要点：没有任何一个工具能覆盖所有已记录的漏洞。

### E14

- 位置：§9.3 Limitations of Our Review，第 17 页
- 原文："The restricted timespan of the study excludes relevant studies recently published, which poses a threat to construct and external validity (Zhou et al., 2016)." / "Therefore we did not include a structured snowballing process, which poses threats to both the internal and conclusion validity."
- 要点：作者自己写明了效度威胁：检索时间截止后发表的研究没有收进来；因为时间有限，也没有做有结构的滚雪球检索（顺着参考文献继续找）。

### E15

- 位置：§1 Introduction，第 2 页
- 原文："The extensive Supplementary Material contains a description of all vulnerabilities, organized in a consolidated taxonomy, an overview of the 140 tools we found, and the quality appraisal or surveys and primary studies."
- 要点：补充材料公开了全部漏洞的说明、140 个工具的概览，以及普通综述和原始研究的质量评估结果（系统综述的评估在正文表 5），读者可以核对筛选过程。

