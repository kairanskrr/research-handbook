# Baltes & Ralph 2022：Sampling in Software Engineering Research: A Critical Review and Guidelines

- 资料：`baltes2022sampling`，[arXiv:2002.07764](https://arxiv.org/abs/2002.07764)
- 版本：Empirical Software Engineering 2022；本地 PDF `papers/pdf/baltes2022sampling.pdf`

### E1

- 位置：§2 Sampling
- 原文："Researchers have developed diverse approaches for selecting samples from populations. There is no single best technique or hierarchy of better and worse techniques. Diﬀerent sampling approaches are appropriate for diﬀerent purposes in diﬀerent circumstances."
- 要点：没有唯一最好的抽样方法，也没有方法之间的优劣等级；不同目的和情境适合不同的抽样方法。

### E2

- 位置：§2.1.1 Convenience sampling
- 原文："In convenience sampling, items are selected based on availability or expedience. [...] Convenience sampling is controversial because it is very popular despite threatening generalizability"
- 要点：便利抽样是按"方便拿到"来选对象；它很流行，但会威胁结论的可推广性。

### E3

- 位置：§2.6 Representativeness
- 原文："Representativeness is a mutual property of a sample and a population. Representativeness is not a property of a sampling technique."
- 要点：代表性是样本和总体之间的关系，不是某种抽样技术自带的属性。

### E4

- 位置：§2.6 Representativeness
- 原文："1. Representativeness is dimension-speciﬁc. A sample can be representative on one parameter but not another. 2. Probability sampling does not guarantee representativeness on the dimensions of interest."
- 要点：代表性是分维度的，样本可能在一个维度上有代表性、在另一个维度上没有；随机抽样也不能保证在你关心的维度上有代表性。

### E5

- 位置：§2.6 Representativeness
- 原文："Moreover, no sample size can overcome bias in the sampling frame."
- 要点：抽样框（可供抽取的对象名单）本身有偏差时，样本再大也无法弥补。

### E6

- 位置：§6 Recommendations
- 原文："1. Clarify your philosophical position. [...] Otherwise the reader (or reviewer) may apply inappropriate criteria. 2. Explain the purpose of sampling. Clearly state whether you are aiming for a representative sample, or have a diﬀerent goal (e.g. theoretical saturation)."
- 要点：建议一句话说明研究立场，否则读者可能套用不合适的标准；说明抽样目的：是追求代表性，还是有别的目标（如理论饱和）。

### E7

- 位置：§6 Recommendations
- 原文："3. Explain how your sample was selected. For qualitative studies, the reader should be able to recover your reasoning about what to study [...]. For quantitative studies, the reader should be able to replicate your sampling approach and the size of the sample should be evident."
- 要点：说明样本怎么选出来的：定性研究要让读者看懂你选择研究对象的理由；定量研究要让读者能重复你的抽样过程。

### E8

- 位置：§6 Recommendations
- 原文："5. Avoid defensiveness. Very few software engineering studies have a strong claim to representative sampling. Overselling the representativeness of your sample is unnecessary and unscientiﬁc."
- 要点：不要防御性地夸大样本的代表性；这既无必要，也不科学。

### E9

- 位置：§6 Recommendations
- 原文："Do not admit to sampling bias in your limitations section only to pretend the results are near-universal in your conclusion."
- 要点：不要在局限部分承认抽样偏差，到了结论又把结果写得几乎普遍适用。

### E10

- 位置：§6 Recommendations
- 原文："we should explain that the purpose of a case study is to understand one site deeply, not to generalize from a sample to a population. We should not pretend that one or a few sites are representative because they are large companies or real projects or use popular practices."
- 要点：做案例研究时，应说明目的是深入理解一个场景，而不是从样本推广到总体；不要因为对象是大公司或真实项目就假装它有代表性。

### E11

- 位置：§6 Recommendations
- 原文："1. Identify the population; that is, in principle, who or what you would like to generalize to"
- 要点：如果追求代表性，先明确总体：原则上你想把结论推广到谁或什么上。

### E12

- 位置：§2.5 Sampling Frameworks and Algorithms
- 原文："We suggest bypassing all this confusion by thinking of most quantitative studies as having a multistage sampling algorithm." / "Authors should identify the population they want to generalize to and papers should reflect on how each step in the sampling algorithm could bias the results."
- 要点：把大多数定量研究的抽样看作多阶段的算法；作者要说明想推广到的总体，并反思每一步可能带来的偏差。

### E13

- 位置：§6.2 Mitigating sampling bias in different kinds of studies
- 原文："If a sampling frame is biased, consider replicating the study using different sampling frames. For example, if we find a pattern in a sample of GitHub projects, replicate the study on a sample of SourceForge projects."
- 要点：抽样框有偏差时，可以换一个抽样框重复研究，例如在 GitHub 上发现的规律，到 SourceForge 的项目上再验证一次。

### E14

- 位置：§6.2 Mitigating sampling bias in different kinds of studies
- 原文："Evaluating sampling bias in software repository mining is fraught. Each repository is likely biased in unpredictable, non-obvious ways."
- 要点：评估仓库挖掘中的抽样偏差很难，每个数据源都可能以难以预料、不明显的方式带有偏差。

### E15

- 位置：§6.2 Mitigating sampling bias in different kinds of studies
- 原文："Corpora can quickly go out of date and there exists an innate tension between keeping corpora stable and up-to-date."
- 要点：语料库很快会过时，保持稳定和保持更新之间存在内在矛盾。

### E16

- 位置：§6.3 Guidelines for reviewers
- 原文："randomness argument to representativeness is unconvincing when the sample was randomly selected from a purposively assembled subset of the repository," [...] "and there is no evidence that the software in the repository does not differ from software in general on the dimensions of interest."
- 要点：从仓库里按目的挑出的子集中再随机抽样，并且没有证据说明这些软件在关心的维度上与一般软件无异时，"随机所以有代表性"的论证站不住。
