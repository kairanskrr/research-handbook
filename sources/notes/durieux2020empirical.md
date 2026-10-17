# Durieux 等 2020：Empirical Review of Automated Analysis Tools on 47,587 Ethereum Smart Contracts

- 资料：`durieux2020empirical`，[原文（arXiv:1910.10601v2）](https://arxiv.org/abs/1910.10601)
- 版本：arXiv v2（2020 年 2 月 9 日），是 ICSE 2020 论文（ACM 出版，第 530–541 页，DOI 10.1145/3377811.3380364，已通过 Crossref 核对）的作者版。位置写 arXiv PDF 页码。注意：摘要和结论说 sbwild 中"97%"的合约被标为有漏洞，但 §3.2 正文和 RQ2 的回答写的是"93%"（44,589 个），两处数字不一致，引用时用 §3.2 的数字并说明出处。

### E1

- 位置：§1 Introduction，第 1 页
- 原文："However, it is not easy to compare and reproduce that research: even though several of the tools are publicly available, the datasets used are not."
- 要点：研究动机是已有的智能合约分析工具很难相互比较和复现，因为很多工具能拿到，但它们用的数据集拿不到。

### E2

- 位置：§1 Introduction，第 2 页
- 原文："In summary, the contributions of the paper are: (1) A dataset of annotated vulnerable Solidity smart contracts; (2) A dataset that contains all the available smart contracts from the Ethereum blockchain that have Solidity source code available in Etherscan; (3) An execution framework that includes 9 pre-configured smart contract analysis tools; and (4) An analysis of the execution of 9 tools on 47,587 smart contracts."
- 要点：论文列出四项贡献：一个人工标注的漏洞合约数据集、一个从以太坊抓取的大规模合约数据集、一个预装 9 个工具的运行框架，以及用它评测 9 个工具的结果分析。

### E3

- 位置：§2.1 Research Questions，第 2 页
- 原文："RQ1. [Effectiveness] What is the effectiveness of current analysis tools in detecting vulnerabilities in Solidity smart contracts?" / "RQ2. [Production] How many vulnerabilities are present in the Ethereum blockchain?" / "RQ3. [Performance] How long do the tools require to analyze the smart contracts?"
- 要点：三个研究问题分别问工具查漏洞查得准不准、真实链上合约里有多少漏洞、工具跑一次要多久。

### E4

- 位置：§2.2 Subject Tools，第 2–3 页
- 原文："We ended up with the 35 tools that are listed in Table 1." / "After inspecting all 35 analysis tools presented in Table 1, we found 9 tools that meet the inclusion criteria outlined."
- 要点：作者先从综述和网络检索中找到 35 个工具，再按事先定好的纳入标准（公开可用且有命令行、输入是 Solidity 源码、只需源码、能报告漏洞）筛出 9 个。

### E5

- 位置：§2.3.1 sbcurated，第 3 页
- 原文："We use the taxonomy presented in the DASP to describe vulnerabilities of Ethereum smart contracts (see Categories in Table 3). Each collected contract is classified in one of the ten categories. We also manually tagged the lines that contain the vulnerability."
- 要点：标注数据集用现成的 DASP 十类漏洞分类，每个合约归入一类，并人工标出漏洞所在的代码行。

### E6

- 位置：§2.3.1 sbcurated，第 3–4 页
- 原文："This dataset has been created by collecting contracts from three different sources: 1. GitHub repositories, 2. blog posts that analyze contracts, and 3. the Ethereum network. 80% of the contracts were collected from GitHub repositories." / "We also ensure the traceability of each contract by providing the URL from which they were taken and its author, where possible."
- 要点：标注数据集的合约来自 GitHub 仓库、分析合约的博客和以太坊链上三个来源，八成来自 GitHub，并为每个合约记录来源网址和作者以便追溯。

### E7

- 位置：§2.3.1 sbcurated，第 4 页
- 原文："The dataset contains 69 contracts and 115 tagged vulnerabilities, divided into ten categories of vulnerabilities."
- 要点：标注数据集共 69 个合约、115 个标注漏洞，分属十个类别。

### E8

- 位置：§2.3.2 sbwild，第 4 页
- 原文："we firstly use Google BigQuery to collect the Ethereum contract addresses that have at least one transaction." / "we observe that 95% of the available Solidity contracts are duplicates. We consider that two contracts are duplicates when the MD5 checksums of the two source files are identical after removing all the spaces and tabulations."
- 要点：大规模数据集先用 BigQuery 取出至少有一笔交易的合约地址，再去 Etherscan 拉源码；去掉空格和制表符后按 MD5 判重，发现 95% 的源码是重复的。

### E9

- 位置：§2.3.2 sbwild，第 4 页
- 原文："The query on Google BigQuery retrieved 2,263,096 smart contract addresses. We then requested Etherscan for the Solidity source code of those contracts, and we obtained 972,975 Solidity files." / "The filtering process of removing duplicate contracts resulted in 47,518 unique contracts (a total of 9,693,457 lines)."
- 要点：从 2,263,096 个地址中拿到 972,975 份源码，去重后剩 47,518 个不同的合约，共约 969 万行代码。

### E10

- 位置：§3.1 Precision of the Analysis Tools (RQ1)，第 5 页
- 原文："To achieve this task, we manually annotated all the vulnerability types that have been detected into one of the ten DASP categories. For example, Oyente detects a vulnerability called Integer Overflow that we link to the category Arithmetic."
- 要点：为了比较不同工具的输出，作者把各工具报告的漏洞类型人工对应到 DASP 十类上，例如把 Oyente 的"整数溢出"归到"算术"类。

### E11

- 位置：§3.1，第 6 页
- 原文："A vulnerability is considered as identified when a tool detects a vulnerability of a specific category at a specific line, and it matches the vulnerability that has been annotated in the dataset."
- 要点：判定标准是工具报出的漏洞类别和行号都要与数据集里的标注一致，才算查出。

### E12

- 位置：§3.1 Answer to RQ1，第 7 页
- 原文："By combining the 9 tools together, they are only able to detect 42% of all the vulnerabilities." / "We also observe that Mythril outperforms the other tools by the number of detected vulnerabilities (31/115, 27%)"
- 要点：9 个工具合起来只查出 42% 的标注漏洞，单个工具最好的 Mythril 也只查出 27%（115 个中的 31 个）。

### E13

- 位置：§3.2，第 7 页
- 原文："In total, 44,589 contracts (93%) have at least one vulnerability detected by one of the 9 tools. Such a high number of vulnerable contracts suggests the presence of a considerable number of false positives."
- 要点：在没有标准答案的大数据集上，93% 的合约至少被一个工具报了漏洞，作者认为这说明误报很多，于是改用"多个工具一致"作为近似判断。

### E14

- 位置：§4.2 Threats to Validity，第 10 页
- 原文："A potential threat to the construct validity relates to the fact that we needed to manually label the vulnerable smart contracts into one of the DASP categories, and these could be mislabeled. This risk was mitigated as follows: all authors labeled the contracts, and then disagreements were discussed to reach a consensus."
- 要点：作者承认人工标注可能标错，应对办法是全体作者各自标注，再讨论分歧达成一致。

### E15

- 位置：§2.3.1 Dataset Availability 与 §1，第 2、4 页
- 原文："Moreover, the dataset contains the file vulnerabilities.json which contains the details of each vulnerable contract. It details the name, the origin URL, the path, and the lines and the category of the vulnerabilities." / "SmartBugs is available at https://smartbugs.github.io"
- 要点：数据集公开在 SmartBugs 仓库，附一个 JSON 文件记录每个漏洞合约的名称、来源网址、路径、漏洞行号和类别。

