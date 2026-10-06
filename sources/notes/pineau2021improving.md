# Pineau 等人 2021：Improving Reproducibility in Machine Learning Research

- 资料：`pineau2021improving`，[原文](https://jmlr.org/papers/v22/20-303.html)
- 版本：Journal of Machine Learning Research 22(164):1–20, 2021，开放获取（CC-BY 4.0）。报告 NeurIPS 2019 可复现性计划：代码提交政策、社区复现挑战赛、机器学习可复现性检查清单。

### E1

- 位置：§2.1 Defining Reproducibility
- 原文："Reproducible work consists of re-doing an experiment using the same data and same analytical tools, whereas Replicable work considers different data (presumably sampled from similar distribution or method), Robust work assumes the same data but different analysis (such as reimplementation of the code, perhaps different computer architecture), and Generalisable work leads to the same conclusions despite considering different data and different analytical tools."
- 要点：本文的用法：可复现（同数据、同分析工具）、可重现（不同数据）、稳健（同数据、不同分析，如重新实现代码）、可推广（数据和分析工具都不同，结论仍相同）。

### E2

- 位置：§2 Background
- 原文："This limitation has been highlighted in a few studies reporting that new proposed methods are often not better than previous implementations when a more thorough search of hyper-parameters is performed (Lucic et al., 2018; Melis et al., 2017), or even when using different random parameter initializations"
- 要点：在机器学习中，有研究发现：把超参数搜索做得更充分，或只是换一组随机初始化，新方法往往就不比旧方法好了。

### E3

- 位置：§2 Background
- 原文："Strikingly, this study found that when the original authors provided assistance to the reproducers, 85% of results were successfully reproduced, compared to 4% when the authors didn't respond." / "Although a selection bias could be at play (authors who knew their results would reproduce might have been more likely to provide assistance for the reproduction)"
- 要点：转述 Raff 2019：原作者提供帮助时 85% 的结果被成功复现，作者不回复时只有 4%；但可能有选择偏差（确信能复现的作者更愿意帮忙）。

### E4

- 位置：§3，对代码提交政策的反对意见之"Replication of mistakes"
- 原文："Having a copy of the code used to produce the experimental results is not a guarantee that this code is correct, and there is significant value in reimplementing an algorithm directly from its description in a paper."
- 要点：拿到原代码不等于代码是对的；直接根据论文描述重新实现算法有很大价值。

### E5

- 位置：§3，对代码提交政策的反对意见之"Computation infrastructure"
- 原文："Even if data and code are provided, the experiments may require so much computation (time & number of machines) that it is impractical for any reviewer, or in fact most researchers, to attempt reproducing the work."
- 要点：即使有数据和代码，有的实验需要的计算量也大到大多数研究者无法复现。

### E6

- 位置：§4 The NeurIPS 2019 Reproducibility Challenge
- 原文："There is rarely such a concise outcome to a reproducibility study. Most reports produced during the challenge offer a much more detailed & nuanced account of their efforts, and the level of fidelity to which they could reproduce the methods, results & claims of each paper." / "we have not found that the findings of most reproducibility studies lend themselves to such a coarse summary."
- 要点："这篇论文能不能复现"很少有简单的答案；多数复现报告给出的是细致的说明：方法、结果、主张分别复现到了什么程度。也不适合用一个"可复现分数"概括。

### E7

- 位置：§1 Introduction
- 原文："Indeed, the evidence threshold for publishing a new positive" [...] "finding is much lower than that for invalidating a previous finding. In the latter case, it may require several teams showing beyond the shadow of a doubt that a result is false for the research community to revise its opinion."
- 要点：发表一个新的正面发现所需的证据门槛，远低于推翻一个已有发现；后者可能需要好几个团队毫无疑问地证明结果是错的，学界才会改变看法。

### E8

- 位置：§4 The NeurIPS 2019 Reproducibility Challenge
- 原文："The main goal of this challenge is to provide independent verification of the empirical claims in accepted NeurIPS papers, and to leave a public trace of the findings from this secondary analysis."
- 要点：复现挑战赛的目标：独立验证已录用论文中的实证主张，并把验证结果公开留档。

### E9

- 位置：§6 Discussion
- 原文："Specific calls for reproducibility papers have been issued (ECIR, 2020). An open-access peer-reviewed journal is dedicated to such papers (ReScience C, 2021)"
- 要点：已有会议专门征集复现论文（如信息检索会议 ECIR 2020），也有专门发表复现论文的开放获取同行评审期刊 ReScience C。

### E10

- 位置：§1 Introduction
- 原文："Misspecification or under-specification of the model or training procedure;" / "Lack of availability of the code necessary to run the experiments, or errors in the code;" / "Under-specification of the metrics used to report results;"
- 要点：机器学习结果难以复现的部分原因：模型或训练过程描述错误或不完整；没有代码或代码有错；结果所用指标没说清楚。
