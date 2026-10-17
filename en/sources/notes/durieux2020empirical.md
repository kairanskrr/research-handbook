# Durieux et al. 2020: Empirical Review of Automated Analysis Tools on 47,587 Ethereum Smart Contracts

- Source: `durieux2020empirical`, [original (arXiv:1910.10601v2)](https://arxiv.org/abs/1910.10601)
- Version: arXiv v2 (February 9, 2020), the authors' version of the ICSE 2020 paper (published by ACM, pp. 530–541, DOI 10.1145/3377811.3380364, checked against Crossref). Locations give arXiv PDF page numbers. Note: the abstract and conclusion say "97%" of contracts in sbwild were flagged as vulnerable, but the body text in §3.2 and the answer to RQ2 say "93%" (44,589); the two figures disagree, so cite the §3.2 figure and say where it comes from.

### E1

- Location: §1 Introduction, p. 1
- Quote: "However, it is not easy to compare and reproduce that research: even though several of the tools are publicly available, the datasets used are not."
- Key point: The motivation is that existing smart contract analysis tools are hard to compare and reproduce, because many of the tools are available but the datasets they used are not.

### E2

- Location: §1 Introduction, p. 2
- Quote: "In summary, the contributions of the paper are: (1) A dataset of annotated vulnerable Solidity smart contracts; (2) A dataset that contains all the available smart contracts from the Ethereum blockchain that have Solidity source code available in Etherscan; (3) An execution framework that includes 9 pre-configured smart contract analysis tools; and (4) An analysis of the execution of 9 tools on 47,587 smart contracts."
- Key point: The paper lists four contributions: a manually annotated dataset of vulnerable contracts, a large dataset of contracts collected from Ethereum, an execution framework with 9 preconfigured tools, and an analysis of running those 9 tools.

### E3

- Location: §2.1 Research Questions, p. 2
- Quote: "RQ1. [Effectiveness] What is the effectiveness of current analysis tools in detecting vulnerabilities in Solidity smart contracts?" / "RQ2. [Production] How many vulnerabilities are present in the Ethereum blockchain?" / "RQ3. [Performance] How long do the tools require to analyze the smart contracts?"
- Key point: The three research questions ask how well the tools detect vulnerabilities, how many vulnerabilities exist in real on-chain contracts, and how long the tools take to run.

### E4

- Location: §2.2 Subject Tools, pp. 2–3
- Quote: "We ended up with the 35 tools that are listed in Table 1." / "After inspecting all 35 analysis tools presented in Table 1, we found 9 tools that meet the inclusion criteria outlined."
- Key point: The authors first found 35 tools through surveys and web searches, then narrowed them to 9 using predefined inclusion criteria (publicly available with a command-line interface, takes Solidity source code as input, needs only the source, reports vulnerabilities).

### E5

- Location: §2.3.1 sbcurated, p. 3
- Quote: "We use the taxonomy presented in the DASP to describe vulnerabilities of Ethereum smart contracts (see Categories in Table 3). Each collected contract is classified in one of the ten categories. We also manually tagged the lines that contain the vulnerability."
- Key point: The annotated dataset uses the existing ten-category DASP taxonomy of vulnerabilities; each contract is assigned to one category, and the lines containing the vulnerability are tagged by hand.

### E6

- Location: §2.3.1 sbcurated, pp. 3–4
- Quote: "This dataset has been created by collecting contracts from three different sources: 1. GitHub repositories, 2. blog posts that analyze contracts, and 3. the Ethereum network. 80% of the contracts were collected from GitHub repositories." / "We also ensure the traceability of each contract by providing the URL from which they were taken and its author, where possible."
- Key point: Contracts in the annotated dataset come from three sources (GitHub repositories, blog posts analyzing contracts, and the Ethereum network), 80% from GitHub, and each records its source URL and author for traceability.

### E7

- Location: §2.3.1 sbcurated, p. 4
- Quote: "The dataset contains 69 contracts and 115 tagged vulnerabilities, divided into ten categories of vulnerabilities."
- Key point: The annotated dataset has 69 contracts and 115 tagged vulnerabilities across ten categories.

### E8

- Location: §2.3.2 sbwild, p. 4
- Quote: "we firstly use Google BigQuery to collect the Ethereum contract addresses that have at least one transaction." / "we observe that 95% of the available Solidity contracts are duplicates. We consider that two contracts are duplicates when the MD5 checksums of the two source files are identical after removing all the spaces and tabulations."
- Key point: For the large dataset, the authors used BigQuery to get addresses of contracts with at least one transaction, then fetched source code from Etherscan; deduplicating by MD5 checksum after stripping spaces and tabs showed that 95% of the source files were duplicates.

### E9

- Location: §2.3.2 sbwild, p. 4
- Quote: "The query on Google BigQuery retrieved 2,263,096 smart contract addresses. We then requested Etherscan for the Solidity source code of those contracts, and we obtained 972,975 Solidity files." / "The filtering process of removing duplicate contracts resulted in 47,518 unique contracts (a total of 9,693,457 lines)."
- Key point: From 2,263,096 addresses they obtained 972,975 source files; after deduplication, 47,518 unique contracts remained, about 9.69 million lines of code.

### E10

- Location: §3.1 Precision of the Analysis Tools (RQ1), p. 5
- Quote: "To achieve this task, we manually annotated all the vulnerability types that have been detected into one of the ten DASP categories. For example, Oyente detects a vulnerability called Integer Overflow that we link to the category Arithmetic."
- Key point: To compare the tools' outputs, the authors manually mapped each tool's vulnerability types onto the ten DASP categories, for example mapping Oyente's "Integer Overflow" to "Arithmetic".

### E11

- Location: §3.1, p. 6
- Quote: "A vulnerability is considered as identified when a tool detects a vulnerability of a specific category at a specific line, and it matches the vulnerability that has been annotated in the dataset."
- Key point: A vulnerability counts as detected only when both the category and the line the tool reports match the annotation in the dataset.

### E12

- Location: §3.1 Answer to RQ1, p. 7
- Quote: "By combining the 9 tools together, they are only able to detect 42% of all the vulnerabilities." / "We also observe that Mythril outperforms the other tools by the number of detected vulnerabilities (31/115, 27%)"
- Key point: All 9 tools combined detected only 42% of the annotated vulnerabilities, and the best single tool, Mythril, found only 27% (31 of 115).

### E13

- Location: §3.2, p. 7
- Quote: "In total, 44,589 contracts (93%) have at least one vulnerability detected by one of the 9 tools. Such a high number of vulnerable contracts suggests the presence of a considerable number of false positives."
- Key point: On the large dataset with no ground truth, 93% of contracts were flagged by at least one tool, which the authors take as a sign of many false positives; they therefore use agreement among several tools as an approximate judgment instead.

### E14

- Location: §4.2 Threats to Validity, p. 10
- Quote: "A potential threat to the construct validity relates to the fact that we needed to manually label the vulnerable smart contracts into one of the DASP categories, and these could be mislabeled. This risk was mitigated as follows: all authors labeled the contracts, and then disagreements were discussed to reach a consensus."
- Key point: The authors acknowledge that manual labels could be wrong; to mitigate this, all authors labeled the contracts and then discussed disagreements to reach consensus.

### E15

- Location: §2.3.1 Dataset Availability and §1, pp. 2, 4
- Quote: "Moreover, the dataset contains the file vulnerabilities.json which contains the details of each vulnerable contract. It details the name, the origin URL, the path, and the lines and the category of the vulnerabilities." / "SmartBugs is available at https://smartbugs.github.io"
- Key point: The dataset is public in the SmartBugs repository, with a JSON file recording each vulnerable contract's name, source URL, path, vulnerable lines and category.
