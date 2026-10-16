# Baltes & Ralph 2022: Sampling in Software Engineering Research: A Critical Review and Guidelines

- Source: `baltes2022sampling`, [arXiv:2002.07764](https://arxiv.org/abs/2002.07764)
- Version: Empirical Software Engineering 2022; local PDF `papers/pdf/baltes2022sampling.pdf`

### E1

- Location: §2 Sampling
- Quote: "Researchers have developed diverse approaches for selecting samples from populations. There is no single best technique or hierarchy of better and worse techniques. Diﬀerent sampling approaches are appropriate for diﬀerent purposes in diﬀerent circumstances."
- Key point: There is no single best sampling technique and no hierarchy of better and worse ones; different approaches suit different purposes and circumstances.

### E2

- Location: §2.1.1 Convenience sampling
- Quote: "In convenience sampling, items are selected based on availability or expedience. [...] Convenience sampling is controversial because it is very popular despite threatening generalizability"
- Key point: Convenience sampling selects items based on availability; it is very popular but threatens generalizability.

### E3

- Location: §2.6 Representativeness
- Quote: "Representativeness is a mutual property of a sample and a population. Representativeness is not a property of a sampling technique."
- Key point: Representativeness is a property of a sample relative to a population, not a property of a sampling technique.

### E4

- Location: §2.6 Representativeness
- Quote: "1. Representativeness is dimension-speciﬁc. A sample can be representative on one parameter but not another. 2. Probability sampling does not guarantee representativeness on the dimensions of interest."
- Key point: Representativeness is dimension-specific: a sample can be representative on one dimension but not another, and probability sampling does not guarantee representativeness on the dimensions you care about.

### E5

- Location: §2.6 Representativeness
- Quote: "Moreover, no sample size can overcome bias in the sampling frame."
- Key point: No sample size can overcome bias in the sampling frame (the list of items you can sample from).

### E6

- Location: §6 Recommendations
- Quote: "1. Clarify your philosophical position. [...] Otherwise the reader (or reviewer) may apply inappropriate criteria. 2. Explain the purpose of sampling. Clearly state whether you are aiming for a representative sample, or have a diﬀerent goal (e.g. theoretical saturation)."
- Key point: State your philosophical position in a sentence, or readers may apply inappropriate criteria; and state the purpose of sampling: a representative sample or another goal (e.g., theoretical saturation).

### E7

- Location: §6 Recommendations
- Quote: "3. Explain how your sample was selected. For qualitative studies, the reader should be able to recover your reasoning about what to study [...]. For quantitative studies, the reader should be able to replicate your sampling approach and the size of the sample should be evident."
- Key point: Explain how the sample was selected: in qualitative studies, readers should be able to follow your reasoning about what to study; in quantitative studies, they should be able to replicate your sampling.

### E8

- Location: §6 Recommendations
- Quote: "5. Avoid defensiveness. Very few software engineering studies have a strong claim to representative sampling. Overselling the representativeness of your sample is unnecessary and unscientiﬁc."
- Key point: Avoid defensiveness: overselling the representativeness of your sample is unnecessary and unscientific.

### E9

- Location: §6 Recommendations
- Quote: "Do not admit to sampling bias in your limitations section only to pretend the results are near-universal in your conclusion."
- Key point: Do not admit sampling bias in the limitations section and then present the results as near-universal in the conclusion.

### E10

- Location: §6 Recommendations
- Quote: "we should explain that the purpose of a case study is to understand one site deeply, not to generalize from a sample to a population. We should not pretend that one or a few sites are representative because they are large companies or real projects or use popular practices."
- Key point: In a case study, explain that the purpose is to understand one site deeply, not to generalize from a sample to a population; do not pretend a site is representative because it is a large company or a real project.

### E11

- Location: §6 Recommendations
- Quote: "1. Identify the population; that is, in principle, who or what you would like to generalize to"
- Key point: If you aim for representativeness, first identify the population: in principle, who or what you want to generalize to.

### E12

- Location: §2.5 Sampling Frameworks and Algorithms
- Quote: "We suggest bypassing all this confusion by thinking of most quantitative studies as having a multistage sampling algorithm." / "Authors should identify the population they want to generalize to and papers should reflect on how each step in the sampling algorithm could bias the results."
- Key point: Think of most quantitative studies as having a multistage sampling algorithm; authors should identify the population they want to generalize to and reflect on how each step could bias the results.

### E13

- Location: §6.2 Mitigating sampling bias in different kinds of studies
- Quote: "If a sampling frame is biased, consider replicating the study using different sampling frames. For example, if we find a pattern in a sample of GitHub projects, replicate the study on a sample of SourceForge projects."
- Key point: If a sampling frame is biased, consider replicating the study with a different frame, e.g., checking a pattern found on GitHub against SourceForge projects.

### E14

- Location: §6.2 Mitigating sampling bias in different kinds of studies
- Quote: "Evaluating sampling bias in software repository mining is fraught. Each repository is likely biased in unpredictable, non-obvious ways."
- Key point: Evaluating sampling bias in mining software repositories is fraught; each repository is likely biased in unpredictable, non-obvious ways.

### E15

- Location: §6.2 Mitigating sampling bias in different kinds of studies
- Quote: "Corpora can quickly go out of date and there exists an innate tension between keeping corpora stable and up-to-date."
- Key point: Corpora go out of date quickly, and there is an inherent tension between keeping them stable and keeping them up to date.

### E16

- Location: §6.3 Guidelines for reviewers
- Quote: "randomness argument to representativeness is unconvincing when the sample was randomly selected from a purposively assembled subset of the repository," [...] "and there is no evidence that the software in the repository does not differ from software in general on the dimensions of interest."
- Key point: The argument "random, therefore representative" is unconvincing when the sample was drawn at random from a purposively assembled subset of a repository and there is no evidence that this software does not differ from software in general on the dimensions of interest.

### E17

- Location: §2.6 Representativeness
- Quote: "The breadth argument supports generalization of correlations" [...] "However, the breath argument does not support point estimates."
- Key point: A large, broad sample can support generalizing correlations but not point estimates (such as a specific proportion like "1% of people do X").

### E18

- Location: §2.1.4 Respondent-driven sampling
- Quote: "Respondent-driven sampling is an advanced form of referral-chain sampling designed to mitigate sampling bias" [...] "Respondent-driven sampling has, however, been criticized for producing optimistic conﬁdence intervals"
- Key point: Respondent-driven sampling is an advanced form of referral-chain (snowball) sampling designed to mitigate sampling bias, but it has been criticized for producing optimistic confidence intervals.

### E19

- Location: §6.2 Mitigating sampling bias in different kinds of studies
- Quote: "These include starting with important questions that resonate with participants (not demographics), avoiding matrix questions, avoiding mandatory questions, and sending reminders. Oﬀering incentives (e.g. cash, prizes) is also eﬀective." [...] "Many questionnaire studies in SE use none of these techniques."
- Key point: Ways to reduce sampling and response bias in questionnaires: start with important questions that resonate (not demographics), avoid matrix and mandatory questions, send reminders, and offer incentives; many software engineering questionnaire studies use none of these.

### E20

- Location: §6.3 Guidelines for reviewers
- Quote: "The whole point of a large questionnaire survey is to sacriﬁce internal validity for external validity."
- Key point: The whole point of a large questionnaire survey is to sacrifice internal validity for external validity (generalizability).

### E21

- Location: §6.3 Guidelines for reviewers
- Quote: "This should be rejected not because it uses convenience sampling but because appropriate, practical steps for mitigating sampling bias were not taken." [...] "They should have reported response rates or bounce rates, compared early responders to late responders and so on."
- Key point: A questionnaire study recruited through mailing lists should be rejected not for using convenience sampling but for not taking practical steps to mitigate bias, such as reporting response or bounce rates and comparing early and late responders.

### E22

- Location: §7 Related Work
- Quote: "contacting developers on GitHub using email addresses users did not provide for this purpose"
- Key point: Contacting developers on GitHub through email addresses they did not provide for this purpose raises ethical problems.

### E23

- Location: §2.1.2 Purposive sampling
- Quote: "In purposive sampling, items are selected according to some logic or strategy, carefully but not randomly" / "the goal of non-probability sampling is often to ﬁnd accessible, information-rich cases, sites, organizations or contexts from which researchers can learn about their topic of study"
- Key point: Purposive sampling selects items according to some logic or strategy, carefully but not randomly; non-probability sampling often aims to find accessible, information-rich cases from which to learn about the topic.

### E24

- Location: §2.1.2 Purposive sampling
- Quote: "The main challenge with purposive sampling is that it is intrinsically subjective and opportunistic."
- Key point: The main challenge of purposive sampling is that it is intrinsically subjective and opportunistic.

### E25

- Location: §2.4 Sampling in qualitative research
- Quote: "Interviewing whoever will speak on a subject of interest is convenience sampling."
- Key point: Interviewing whoever will speak on a subject is convenience sampling.

### E26

- Location: §2.4 Sampling in qualitative research
- Quote: "In the grounded theory literature, theoretical sampling refers to selecting items to study based on an emerging theory"
- Key point: Theoretical sampling selects what to study next based on the emerging theory.
