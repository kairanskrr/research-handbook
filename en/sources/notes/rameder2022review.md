# Rameder, di Angelo & Salzer 2022: Review of Automated Vulnerability Analysis of Smart Contracts on Ethereum

- Source: `rameder2022review`, [PDF (Frontiers open access)](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2022.814977/pdf)
- Version: Frontiers in Blockchain vol. 5, article 814977, published March 24, 2022, CC BY license. DOI 10.3389/fbloc.2022.814977 (checked against Crossref). Locations give journal page numbers (the same as the PDF page numbers).

### E1

- Location: Abstract, p. 1
- Quote: "Moreover, publications keep emerging with different focus, scope, and quality, making it difficult to keep up with the field and to identify relevant trends. Thus, regular reviews are essential to keep pace with the varied developments in a structured manner."
- Key point: Publications keep appearing with different focus, scope, and quality, making the field hard to keep up with, so regular structured reviews are needed.

### E2

- Location: §1 Introduction, p. 2
- Quote: "We assess the publications with respect to the following questions: [...] Which vulnerabilities are mentioned? How are vulnerabilities classified? [...] Which methods do automated tools use to detect vulnerabilities? [...] Which vulnerabilities are addressed by the tools? [...] How are the tools evaluated? [...] What are the open challenges of automated detection?"
- Key point: The review first lists the questions it will answer: which vulnerabilities exist and how they are classified, what methods tools use to detect them, which vulnerabilities the tools cover, how the tools are evaluated, and what challenges remain open.

### E3

- Location: §1 Introduction, p. 2
- Quote: "Our contributions are [...] a list of high quality publications, with the selection based on clear criteria, [...] an overview and taxonomy of vulnerabilities, methods and tools, [...] a discussion of the state of the art with respect to automated analysis, and [...] the identification of gaps and challenges."
- Key point: The paper claims four contributions: a list of high-quality publications selected by clear criteria, a taxonomy of vulnerabilities, methods, and tools, a discussion of the state of the art, and the identification of gaps and challenges.

### E4

- Location: §2 Systematic Review, p. 2
- Quote: "For the literature review, we apply a rigorous protocol to ensure comprehensive and reproducible results as suggested in several guidelines (Brereton et al., 2007; Kitchenham and Charters, 2007; Okoli, 2015; Snyder, 2019)."
- Key point: Following several guidelines, including Kitchenham & Charters 2007, the authors applied a rigorous review protocol so that results would be comprehensive and reproducible.

### E5

- Location: §2.1.1 Initial Search, pp. 2–3
- Quote: "we choose the primary search term smart contract and a disjunction of the terms security, vulnerability, bug, analysis, detection, verification and tool." / "The initial search was conducted at the end of January 2021 and yielded a total of 1326 results, with 546 contributed by Google Scholar, 229 by IEEE Xplore, 199 by ScienceDirect, 178 by TU Wien CatalogPlus, and 174 by ACM Digital Library."
- Key point: The search string was "smart contract" combined with any of security, vulnerability, bug, and similar terms; run at the end of January 2021 across five databases, it returned 1326 results, with the count from each database reported.

### E6

- Location: §2.1.2 Exclusion and Inclusion Criteria, p. 3
- Quote: "Exclusion Criteria: We exclude search results if the work is 1) not written in English, 2) a patent, blog entry or other grey literature, 3) not accessible on-line via the library network of TU Wien, 4) published before 2014, and 5) unrelated to Ethereum."
- Key point: There were five exclusion criteria: not in English, patents, blogs, or other grey literature, not accessible through the university library network, published before 2014, and unrelated to Ethereum.

### E7

- Location: §2.1.2–§2.1.3, p. 3
- Quote: "Inclusion Criteria: We include search results if it is clear from title and abstract that the work is related to 1) smart contract security bugs or vulnerabilities, 2) smart contract vulnerability detection, analysis or security verification tools, or 3) automated detection or verification methods." / "After removing 299 duplicates and excluding 724 articles according to the criteria above, we group the remaining 303 studies into three classes"
- Key point: Inclusion was judged from title and abstract alone; after removing 299 duplicates and excluding 724 articles by the criteria, 303 studies remained, grouped into systematic literature reviews, surveys, and primary studies.

### E8

- Location: §2.2.2 Contextual and Final Data Quality, p. 4; §2.3 Data Extraction, p. 5
- Quote: "For the sake of readability, and ease of classification, we map CDQ and FDQ to a three point Likert scale, by calling a score low if it is below 0.5, high if it is at least 0.8, and medium otherwise. We exclude a study from the survey if its CDQ or FDQ is low." / "After quality appraisal and reclassification, we are left with 8 systematic literature reviews, 38 surveys and 149 primary studies"
- Key point: Each study received a quality score from predefined questions, and those scoring below 0.5 were rated low and excluded; after quality appraisal, 8 systematic literature reviews, 38 surveys, and 149 primary studies went on to data extraction.

### E9

- Location: §4.2 Academic Classifications, p. 8
- Quote: "Atzei et al. (2017) create one of the first taxonomies for vulnerabilities." / "Although this work is referenced in several other papers, we have found some issues and inconsistencies regarding the classification of concrete vulnerabilities."
- Key point: The authors note that Atzei et al. (2017) created one of the first vulnerability taxonomies, widely cited, but found issues and inconsistencies in how it classifies specific vulnerabilities.

### E10

- Location: §4.1 Consolidated Taxonomy, p. 8
- Quote: "In total, we extracted 54 vulnerabilities from the collected papers. [...] Our consolidated classification in Table 6 consists of 10 classes of vulnerabilities."
- Key point: The authors extracted 54 vulnerabilities from the literature and grouped them into 10 classes.

### E11

- Location: §6 Tools for Automated Security Analysis, pp. 12–13
- Quote: "The 24 SLRs and surveys as well as the 149 primary studies we finally selected describe a total of 140 tools for analyzing the security of Ethereum smart contracts, with 83 published open source." / "The vast majority of tools (113, 80.7%) employs static methods, about a third (43, 30.7%) uses dynamic methods, and several (16, 11.4%) use both."
- Key point: The selected publications describe 140 tools for analyzing Ethereum smart contract security, 83 of them open source; about 80% (113) use static methods and about 30% (43) dynamic methods.

### E12

- Location: §7 Benchmarks and Test Sets, p. 13
- Quote: "The number of contracts per test set (fourth column) varies between 6 and 47 541. More than half of the projects also include contracts that were manually verified to be true or false positives with respect to some property, in order to serve as a ground truth."
- Key point: Test sets range from 6 to 47,541 contracts; more than half of the projects include manually verified contracts that serve as ground truth.

### E13

- Location: §9.1 New Vulnerabilities and Tools, p. 17
- Quote: "At the same time, there is not a single tool that covers all documented vulnerabilities."
- Key point: No single tool covers all documented vulnerabilities.

### E14

- Location: §9.3 Limitations of Our Review, p. 17
- Quote: "The restricted timespan of the study excludes relevant studies recently published, which poses a threat to construct and external validity (Zhou et al., 2016)." / "Therefore we did not include a structured snowballing process, which poses threats to both the internal and conclusion validity."
- Key point: The authors state their own threats to validity: studies published after the search cutoff were not included, and for lack of time they did no structured snowballing (following reference lists to find more studies).

### E15

- Location: §1 Introduction, p. 2
- Quote: "The extensive Supplementary Material contains a description of all vulnerabilities, organized in a consolidated taxonomy, an overview of the 140 tools we found, and the quality appraisal or surveys and primary studies."
- Key point: The supplementary material publishes descriptions of all vulnerabilities, an overview of the 140 tools, and the quality appraisal of surveys and primary studies (the appraisal of systematic reviews is in Table 5 of the main text), so readers can check the selection.
