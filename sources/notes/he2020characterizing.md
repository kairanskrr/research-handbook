# He 等 2020：Characterizing Code Clones in the Ethereum Smart Contract Ecosystem

- 资料：`he2020characterizing`，[原文（FC 2020 会前论文集 PDF）](https://fc20.ifca.ai/preproceedings/106.pdf)
- 版本：Financial Cryptography and Data Security 2020 会前论文集版（正式版收入 LNCS，第 654–675 页，DOI 10.1007/978-3-030-51280-4_35）；另有 arXiv 版 [1905.00272](https://arxiv.org/abs/1905.00272)。位置写会前论文集 PDF 上印的页码。

### E1

- 位置：§1 Introduction，第 2 页
- 原文："However, the open-source nature of smart contracts has provided convenience for plagiarists to create contract clones, i.e., copying code from other available contracts." / "as many smart contracts are suffering from serious vulnerabilities, the copy-paste vulnerabilities would be inherited by the plagiarized contracts."
- 要点：智能合约大多公开源码，方便别人照抄；被抄的合约如果有漏洞，抄来的合约也会带上同样的漏洞。

### E2

- 位置：§1 Introduction，第 2 页
- 原文："LastWinner, one of the most successful followers of Fomo3D, was attacked and lost more than 5,000 ETHs within 4 days." / "Interestingly, the vulnerable part was kept wholly intact by the plagiarist"
- 要点：论文用一个真实事件引出问题：模仿 Fomo3D 的游戏原样保留了有漏洞的代码，4 天内被攻击损失 5000 多个以太币。

### E3

- 位置：§1 Introduction，第 2–3 页
- 原文："We present a large scale systematic study to characterize the code clone behaviors of Ethereum smart contracts in a comprehensive manner." / "Then, we further seek to understand the reasons leading to contract clones and characterize their security impacts."
- 要点：研究目标是大规模、系统地刻画以太坊合约的代码克隆现象，并弄清克隆的原因和它对安全的影响。

### E4

- 位置：§5 Qualitative Analysis，第 10 页
- 原文："We first seek to cluster the distinct contracts into groups based on their similarity scores, for which we try to understand the reasons leading to contract clones and study the diversity of the ecosystem (e.g., what are these contracts?). Then we propose to explore the correlation between code clones and vulnerabilities, i.e., whether code clones lead to the spread of vulnerabilities. At last, we try to identify the DApp Clones in the wild and measure their impact."
- 要点：（本项目通读全文后的判断，不是原文的话：论文没有编号的研究问题。）作者用文字给出了三个具体问题：克隆从哪来、克隆会不会传播漏洞、有没有抄袭的去中心化应用以及影响多大。

### E5

- 位置：§1 Introduction，第 3 页
- 原文："To the best of our knowledge, this is the first systematic study of code clones in the Ethereum smart contract ecosystem at scale." / "Our results motivated the need for research efforts to identify security issues introduced by copy-paste behaviors."
- 要点：作者声称的贡献是第一次大规模、系统地研究以太坊合约克隆，并指出需要研究复制粘贴带来的安全问题。

### E6

- 位置：§4.1 Dataset、§4.2 Pre-processing，第 8 页
- 原文："covering almost 10 million smart contracts deployed on the Ehtereum mainnet from July 30th, 2015 to December 31st, 2018." / "the proportion of contracts to be analyzed has been shrunk dramatically to 0.798%(78,611/9,850,757) of the original dataset we collected."
- 要点：数据是 2015 年 7 月到 2018 年底部署在以太坊主网上的近 1000 万个合约；去掉完全重复的之后，只剩 78,611 个不同的合约，不到原来的 0.8%。

### E7

- 位置：§3 Methodology，第 5 页
- 原文："We first seek to remove duplicate smart contracts to reduce the computational workload in two steps" / "we take advantage of a customized fuzzy hashing approach to generate the fingerprints. Lastly, we enforce a pair-wise comparison strategy with pruning to achieve scalability."
- 要点：方法分三步：先去重，再给每个合约的字节码生成"模糊指纹"，最后两两比较指纹，并提前跳过明显不像的合约对来节省计算。

### E8

- 位置：§3 Methodology，第 5 页
- 原文："In this paper, we did not rely on heavy-weight methods such as comparing the control-flow graph (CFG) and program dependency graph (PDG), mainly due to two reasons. First, our approach should be scalable. Second, the simplicity of smart contracts and EVM bytecode [...] makes it unnecessary to adopt those heavy approaches."
- 要点：作者明确说明了为什么选轻量方法：要能处理千万级数据，而且合约逻辑简单，用不着更重的程序分析。

### E9

- 位置：§4.3 Similarity Comparison，第 9–10 页
- 原文："we randomly samples 100 pairs each range (1,100 pairs in total)" / "The first two authors performed manually comparison of the source code to label the ground truth." / "we empirically found that 70 is a good indicator to achieve the balance, with 97.5% of precision and 88% of recall at this threshold."
- 要点：为了检验克隆检测是否可靠，两位作者人工比对了随机抽取的 1,100 对合约的源码作为标准答案；相似度阈值取 70 时，精确率 97.5%，召回率 88%。

### E10

- 位置：Abstract，第 1 页；§5 Qualitative Analysis，第 10 页
- 原文："Our analysis revealed that over 96% of the contracts had duplicates, while a large number of them were similar, which suggests that the ecosystem is highly homogeneous." / "For the distinct contracts, the top 20% of the clusters account for 60% of the contracts."
- 要点：主要发现之一：超过 96% 的合约有完全相同的副本，不同合约也集中在少数几类里，说明整个生态高度同质化。

### E11

- 位置：§5.2 Vulnerability Provenance，第 12 页
- 原文："To identify security vulnerabilities, we take advantage of a state-of-the-art tool developed by PeckShield." / "As it is not the emphasis of this paper, we will use the results directly without giving technical details of the tool."
- 要点：漏洞检测用的是 PeckShield 公司的工具（作者之一来自该公司），论文直接使用结果，没有给出工具的技术细节。

### E12

- 位置：Abstract，第 1 页；§5.2 Vulnerability Provenance，第 13 页
- 原文："Our results also suggested that roughly 9.7% of the similar contract pairs have exactly the same vulnerabilities, which we assume were introduced by code clones." / "Over 46K contract pairs share the same vulnerabilities, and over 90% of them were created by different authors."
- 要点：约 9.7% 的相似合约对带有完全相同的漏洞，其中九成以上出自不同作者，作者推断这些漏洞是抄代码时一起抄过去的。

### E13

- 位置：§5.3 Clone Detection of DApps，第 14 页
- 原文："We have made our best efforts to collect 2,533 DApps from well-known DApp browsers" / "The overall volume of the 41 original DApps is 304,797.344 ETH, while the volume of the 73 DApp clones reaches 89,565.321 ETH"
- 要点：作者从知名的去中心化应用目录网站收集了 2,533 个应用，找出 41 组克隆；73 个抄袭应用的交易额约 8.96 万个以太币，约为 41 个原版应用交易额的三成。

### E14

- 位置：§7 Concluding Remarks and Future Work，第 15 页
- 原文："First, the threshold used to identify contract clones can be improved by adopting adaptive approaches. Second, we may have coverage issues on manually labelling the contract templates, which can be alleviated by exploring some advanced techniques."
- 要点：作者承认的局限：判定克隆的阈值是固定的，人工整理的合约模板清单可能不全。（本项目通读全文后的判断，不是原文的话：论文没有单独的"效度威胁"小节。）

