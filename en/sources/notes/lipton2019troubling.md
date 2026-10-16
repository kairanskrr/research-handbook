# Lipton & Steinhardt 2019: Troubling Trends in Machine Learning Scholarship

- Source: `lipton2019troubling`, [full text](https://arxiv.org/abs/1807.03341)
- Version: arXiv:1807.03341v2 (2018-07-26), local PDF `papers/pdf/lipton2019troubling.pdf`. Page numbers are those printed in the PDF footer.
- Note: The paper is about machine learning papers, but principles such as "distinguish explanation from speculation" and "identify the source of gains" apply in every field.

### E1

- Location: §1 Introduction, p. 1
- Quote: "(i) provide intuition to aid the reader’s understanding, but clearly distinguish it from stronger conclusions supported by evidence; (ii) describe empirical investigations that consider and rule out alternative hypotheses"
- Key point: Good papers separate intuition from conclusions supported by evidence, and their experiments consider and rule out alternative explanations.

### E2

- Location: §3.1 Explanation vs. Speculation, p. 2
- Quote: "papers often oﬀer speculation in the guise of explanations, which are then interpreted as authoritative due to the trappings of a scientiﬁc paper and the presumed expertise of the authors."
- Key point: Papers often offer speculation in the guise of explanations, which readers then treat as authoritative because it appears in a scientific paper written by experts.

### E3

- Location: §3.1, p. 3 (positive example: the dropout paper)
- Quote: "a designated “Motivation” section clearly quarantines this discussion. This practice avoids confusing readers while allowing authors to express informal ideas."
- Key point: Putting speculative discussion in a clearly labeled separate section lets authors express informal ideas without confusing readers.

### E4

- Location: §3.2 Failure to Identify the Sources of Empirical Gains, p. 3
- Quote: "Too frequently, authors propose many tweaks absent proper ablation studies, obscuring the source of empirical gains. Sometimes just one of the changes is actually responsible for the improved results."
- Key point: Proposing many tweaks without proper ablation studies obscures the source of empirical gains; sometimes only one of the changes actually matters.

### E5

- Location: §3.2, p. 3
- Quote: "a series of published improvements, originally attributed to complex innovations in network architectures, were actually due to better hyperparameter tuning. On equal footing, vanilla LSTMs, hardly modiﬁed since 1997, topped the leaderboard."
- Key point: (A machine learning example) A series of improvements attributed to complex new architectures were actually due to better hyperparameter tuning; under equal conditions the older method did best. Unfair comparisons create illusory progress.

### E6

- Location: §3.2, p. 3
- Quote: "ablation is neither necessary nor suﬃcient for understanding a method, and can even be impractical given computational constraints."
- Key point: Ablation is not the only way to understand a method, and it may be impractical under computational constraints; robustness checks and error analysis can also provide understanding.

### E7

- Location: §5.1 Suggestions for Authors, p. 8
- Quote: "We encourage authors to ask “what worked?” and “why?”, rather than just “how well?”."
- Key point: Ask "what worked?" and "why?", not just "how well?"

### E8

- Location: §5.1, p. 8
- Quote: "Three practices that are common in the strongest empirical papers are error analysis, ablation studies, and robustness checks"
- Key point: Three practices common in the strongest empirical papers: error analysis, ablation studies, and robustness checks.

### E9

- Location: §5.2 Suggestions for Publishers and Reviewers, p. 8
- Quote: "a paper describing a simple idea that leads to improved performance, together with two negative results, should be judged more favorably than a paper that combines three ideas together (without ablation studies) yielding the same improvement."
- Key point: A paper with a simple idea plus two negative results should be judged more favorably than one that bundles three ideas without ablation to get the same improvement.

### E10

- Location: §6.1 Countervailing Considerations, p. 9
- Quote: "the breakthrough paper on ImageNet classiﬁcation proposes multiple techniques without ablation studies, several of which were subsequently determined to be unnecessary. However, at the time the results were so signiﬁcant and the experiments so computationally expensive to run that waiting for ablations to complete was perhaps not worth the cost to the community."
- Key point: Counterpoint: sometimes a result is important enough and the experiments expensive enough that delaying publication for ablations is not worth it. The authors acknowledge such considerations are valid.

### E11

- Location: §1, one of the four trends
- Quote: "Failure to distinguish between explanation and speculation."
- Key point: A common problem: failure to distinguish between explanation and speculation.

### E12

- Location: §3.1
- Quote: "We ourselves have been equally guilty of speculation disguised as explanation."
- Key point: The authors admit they have themselves been guilty of speculation disguised as explanation, which shows how easy this mistake is.

### E13

> Withdrawn: duplicates [E3](#e3) (the quote is fully contained in E3).

- Location: §3.1
- Quote: "a designated “Motivation” section clearly quarantines this discussion"
- Key point: Good practice: put speculation in a dedicated section, clearly separated from conclusions backed by evidence.

### E14

> Withdrawn: duplicates [E4](#e4) (the quote is fully contained in E4).

- Location: §3.2
- Quote: "Too frequently, authors propose many tweaks absent proper ablation studies, obscuring the source of empirical gains."
- Key point: Making many changes without testing each one obscures where the gains actually come from.

### E15

- Location: §4.1
- Quote: "Authors with strong results may feel licensed to insert arbitrary unsupported stories"
- Key point: When results are strong, authors may feel licensed to add explanations that have no supporting evidence.

### E16

- Location: §2 Disclaimers
- Quote: "This paper aims to instigate discussion, answering a call for papers from the ICML Machine Learning Debates workshop. While we stand by the points represented here, we do not purport to offer a full or balanced viewpoint or to discuss the overall quality of science in ML."
- Key point: The authors explain the paper's purpose: written for an ICML debate-style workshop to instigate discussion; they stand by their points but do not claim to be comprehensive or balanced, nor to judge the overall quality of machine learning research.

### E17

- Location: §2 Disclaimers
- Quote: "We note that these arguments are made by us, against us, by insiders offering a critical introspective look, not as sniping outsiders." / "Exhibiting one of these patterns doesn’t make a paper bad nor does it indict the paper’s authors"
- Key point: The authors stress that the critique is insiders' self-reflection, aimed at themselves as well; a paper showing these problems is not necessarily a bad paper, and they are not accusing its authors.

### E18

- Location: §2 Disclaimers
- Quote: "our guiding principles are to (i) implicate ourselves, and (ii) to preferentially select from the work of better-established researchers and institutions that we admire, to avoid singling out junior students for whom inclusion in this discussion might have consequences and who lack the opportunity to reply symmetrically."
- Key point: Their principles for choosing examples: implicate themselves, and preferentially select work by well-established researchers and institutions they respect, avoiding junior students, who could be harmed by being named and have no equal chance to respond.

### E19

- Location: §3 Troubling Trends
- Quote: "In each subsection below, we (i) describe a trend; (ii) provide several examples (as well as positive examples that resist the trend); and (iii) explain the consequences. Pointing to weaknesses in individual papers can be a sensitive topic. To minimize this, we keep examples short and specific."
- Key point: Each section describes a trend, gives several examples (plus positive examples that resist the trend), and explains the consequences; pointing out weaknesses of specific papers is sensitive, so the examples are kept short and specific.

### E20

- Location: §3.1, positive example
- Quote: "Here, the authors carefully convey uncertainty. Instead of presenting the guidelines as authoritative, the paper states" / "they should be challenged. They constitute a good starting point"
- Key point: Positive example: a paper offering guidelines for training neural networks carefully conveys uncertainty, presenting the guidelines not as authoritative but as a good starting point that should be challenged.

### E21

- Location: §6.1 Countervailing Considerations
- Quote: "There are a number of countervailing considerations to the suggestions set forth above." / "We recognize the validity of these considerations, and also recognize that these standards are at times exacting." / "we present these as strong heuristics rather than unbreakable rules"
- Key point: The authors devote a section to considerations against their own suggestions, acknowledge their validity and that their standards can be demanding, and present their advice as strong rules of thumb rather than inviolable rules.
