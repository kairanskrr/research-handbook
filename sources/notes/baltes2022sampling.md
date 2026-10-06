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

### E17

- 位置：§2.6 Representativeness
- 原文："The breadth argument supports generalization of correlations" [...] "However, the breath argument does not support point estimates."
- 要点：样本又大又广，可以支持"相关关系能推广"的论证，但不能支持点估计（例如"有 1% 的人如何"这种具体比例）。

### E18

- 位置：§2.1.4 Respondent-driven sampling
- 原文："Respondent-driven sampling is an advanced form of referral-chain sampling designed to mitigate sampling bias" [...] "Respondent-driven sampling has, however, been criticized for producing optimistic conﬁdence intervals"
- 要点：应答者驱动抽样是为减轻抽样偏差而设计的进阶版滚雪球抽样，但也被批评给出的置信区间过于乐观。

### E19

- 位置：§6.2 Mitigating sampling bias in different kinds of studies
- 原文："These include starting with important questions that resonate with participants (not demographics), avoiding matrix questions, avoiding mandatory questions, and sending reminders. Oﬀering incentives (e.g. cash, prizes) is also eﬀective." [...] "Many questionnaire studies in SE use none of these techniques."
- 要点：减轻问卷抽样偏差和回应偏差的做法：开头放能引起共鸣的重要问题（不是人口学问题），避免矩阵题和必答题，发提醒，提供激励；很多软件工程问卷研究一项都没用。

### E20

- 位置：§6.3 Guidelines for reviewers
- 原文："The whole point of a large questionnaire survey is to sacriﬁce internal validity for external validity."
- 要点：大规模问卷调查的意义，就在于牺牲内部效度换取外部效度（可推广性）。

### E21

- 位置：§6.3 Guidelines for reviewers
- 原文："This should be rejected not because it uses convenience sampling but because appropriate, practical steps for mitigating sampling bias were not taken." [...] "They should have reported response rates or bounce rates, compared early responders to late responders and so on."
- 要点：通过邮件列表招募的问卷研究，该被拒的理由不是用了便利抽样，而是没有采取可行的减偏措施；例如应报告回应率或退信率，比较早回答者和晚回答者。

### E22

- 位置：§7 Related Work
- 原文："contacting developers on GitHub using email addresses users did not provide for this purpose"
- 要点：用开发者并非为此目的提供的邮箱在 GitHub 上联系他们，存在伦理问题。

### E23

- 位置：§2.1.2 Purposive sampling
- 原文："In purposive sampling, items are selected according to some logic or strategy, carefully but not randomly" / "the goal of non-probability sampling is often to ﬁnd accessible, information-rich cases, sites, organizations or contexts from which researchers can learn about their topic of study"
- 要点：目的抽样是按某种逻辑或策略、仔细但非随机地选择对象；非概率抽样的目标常常是找到能接触到、信息丰富的个案，从中了解研究主题。

### E24

- 位置：§2.1.2 Purposive sampling
- 原文："The main challenge with purposive sampling is that it is intrinsically subjective and opportunistic."
- 要点：目的抽样的主要问题是它本质上主观、带有机会主义色彩。

### E25

- 位置：§2.4 Sampling in qualitative research
- 原文："Interviewing whoever will speak on a subject of interest is convenience sampling."
- 要点：谁愿意谈就访谈谁，属于便利抽样。

### E26

- 位置：§2.4 Sampling in qualitative research
- 原文："In the grounded theory literature, theoretical sampling refers to selecting items to study based on an emerging theory"
- 要点：理论抽样是根据正在形成的理论来决定接下来研究什么对象。
