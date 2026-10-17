# He et al. 2020: Characterizing Code Clones in the Ethereum Smart Contract Ecosystem

- Source: `he2020characterizing`, [original (FC 2020 pre-proceedings PDF)](https://fc20.ifca.ai/preproceedings/106.pdf)
- Version: Financial Cryptography and Data Security 2020 pre-proceedings version (the final version is in LNCS, pp. 654–675, DOI 10.1007/978-3-030-51280-4_35); an arXiv version also exists, [1905.00272](https://arxiv.org/abs/1905.00272). Locations give the page numbers printed on the pre-proceedings PDF.

### E1

- Location: §1 Introduction, p. 2
- Quote: "However, the open-source nature of smart contracts has provided convenience for plagiarists to create contract clones, i.e., copying code from other available contracts." / "as many smart contracts are suffering from serious vulnerabilities, the copy-paste vulnerabilities would be inherited by the plagiarized contracts."
- Key point: Most smart contracts publish their source code, which makes copying easy; if the copied contract has vulnerabilities, the copies inherit them.

### E2

- Location: §1 Introduction, p. 2
- Quote: "LastWinner, one of the most successful followers of Fomo3D, was attacked and lost more than 5,000 ETHs within 4 days." / "Interestingly, the vulnerable part was kept wholly intact by the plagiarist"
- Key point: The paper opens with a real incident: a game imitating Fomo3D kept the vulnerable code wholly intact and was attacked, losing more than 5,000 ETH within 4 days.

### E3

- Location: §1 Introduction, pp. 2–3
- Quote: "We present a large scale systematic study to characterize the code clone behaviors of Ethereum smart contracts in a comprehensive manner." / "Then, we further seek to understand the reasons leading to contract clones and characterize their security impacts."
- Key point: The goal is a large-scale, systematic characterization of code cloning in Ethereum contracts, including why cloning happens and how it affects security.

### E4

- Location: §5 Qualitative Analysis, p. 10
- Quote: "We first seek to cluster the distinct contracts into groups based on their similarity scores, for which we try to understand the reasons leading to contract clones and study the diversity of the ecosystem (e.g., what are these contracts?). Then we propose to explore the correlation between code clones and vulnerabilities, i.e., whether code clones lead to the spread of vulnerabilities. At last, we try to identify the DApp Clones in the wild and measure their impact."
- Key point: (This project's judgment after reading the full text, not the authors' words: the paper has no numbered research questions.) The authors state three concrete questions in prose: where clones come from, whether clones spread vulnerabilities, and whether plagiarized decentralized applications exist and how much impact they have.

### E5

- Location: §1 Introduction, p. 3
- Quote: "To the best of our knowledge, this is the first systematic study of code clones in the Ethereum smart contract ecosystem at scale." / "Our results motivated the need for research efforts to identify security issues introduced by copy-paste behaviors."
- Key point: The claimed contribution is the first large-scale, systematic study of contract clones on Ethereum, along with the point that security problems introduced by copy-paste need research.

### E6

- Location: §4.1 Dataset, §4.2 Pre-processing, p. 8
- Quote: "covering almost 10 million smart contracts deployed on the Ehtereum mainnet from July 30th, 2015 to December 31st, 2018." / "the proportion of contracts to be analyzed has been shrunk dramatically to 0.798%(78,611/9,850,757) of the original dataset we collected."
- Key point: The data are nearly 10 million contracts deployed on the Ethereum mainnet from July 2015 to the end of 2018; after removing exact duplicates, only 78,611 distinct contracts remained, under 0.8% of the original.

### E7

- Location: §3 Methodology, p. 5
- Quote: "We first seek to remove duplicate smart contracts to reduce the computational workload in two steps" / "we take advantage of a customized fuzzy hashing approach to generate the fingerprints. Lastly, we enforce a pair-wise comparison strategy with pruning to achieve scalability."
- Key point: The method has three steps: remove duplicates, generate a fuzzy-hash fingerprint of each contract's bytecode, then compare fingerprints pairwise, pruning obviously dissimilar pairs early to save computation.

### E8

- Location: §3 Methodology, p. 5
- Quote: "In this paper, we did not rely on heavy-weight methods such as comparing the control-flow graph (CFG) and program dependency graph (PDG), mainly due to two reasons. First, our approach should be scalable. Second, the simplicity of smart contracts and EVM bytecode [...] makes it unnecessary to adopt those heavy approaches."
- Key point: The authors explicitly justify choosing a lightweight method: it has to scale to tens of millions of contracts, and contract logic is simple enough that heavier program analysis is unnecessary.

### E9

- Location: §4.3 Similarity Comparison, pp. 9–10
- Quote: "we randomly samples 100 pairs each range (1,100 pairs in total)" / "The first two authors performed manually comparison of the source code to label the ground truth." / "we empirically found that 70 is a good indicator to achieve the balance, with 97.5% of precision and 88% of recall at this threshold."
- Key point: To check that clone detection is reliable, two authors manually compared the source code of 1,100 randomly sampled contract pairs as ground truth; at a similarity threshold of 70, precision was 97.5% and recall 88%.

### E10

- Location: Abstract, p. 1; §5 Qualitative Analysis, p. 10
- Quote: "Our analysis revealed that over 96% of the contracts had duplicates, while a large number of them were similar, which suggests that the ecosystem is highly homogeneous." / "For the distinct contracts, the top 20% of the clusters account for 60% of the contracts."
- Key point: One main finding: over 96% of contracts have exact duplicates, and distinct contracts cluster into a few groups, so the ecosystem is highly homogeneous.

### E11

- Location: §5.2 Vulnerability Provenance, p. 12
- Quote: "To identify security vulnerabilities, we take advantage of a state-of-the-art tool developed by PeckShield." / "As it is not the emphasis of this paper, we will use the results directly without giving technical details of the tool."
- Key point: Vulnerability detection used a tool from the company PeckShield (one of the authors works there); the paper uses its results directly without giving technical details of the tool.

### E12

- Location: Abstract, p. 1; §5.2 Vulnerability Provenance, p. 13
- Quote: "Our results also suggested that roughly 9.7% of the similar contract pairs have exactly the same vulnerabilities, which we assume were introduced by code clones." / "Over 46K contract pairs share the same vulnerabilities, and over 90% of them were created by different authors."
- Key point: About 9.7% of similar contract pairs share exactly the same vulnerabilities, over 90% of them created by different authors, and the authors infer that the vulnerabilities were copied along with the code.

### E13

- Location: §5.3 Clone Detection of DApps, p. 14
- Quote: "We have made our best efforts to collect 2,533 DApps from well-known DApp browsers" / "The overall volume of the 41 original DApps is 304,797.344 ETH, while the volume of the 73 DApp clones reaches 89,565.321 ETH"
- Key point: The authors collected 2,533 decentralized applications from well-known directory sites and found 41 clone groups; the 73 clones handled about 89,600 ETH in volume, roughly 30% of the volume of the 41 originals.

### E14

- Location: §7 Concluding Remarks and Future Work, p. 15
- Quote: "First, the threshold used to identify contract clones can be improved by adopting adaptive approaches. Second, we may have coverage issues on manually labelling the contract templates, which can be alleviated by exploring some advanced techniques."
- Key point: Limitations the authors acknowledge: the threshold for identifying clones is fixed, and the manually compiled list of contract templates may be incomplete. (This project's judgment after reading the full text, not the authors' words: the paper has no separate threats-to-validity section.)
