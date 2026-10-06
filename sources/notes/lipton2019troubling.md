# Lipton & Steinhardt 2019：Troubling Trends in Machine Learning Scholarship

- 资料：`lipton2019troubling`，[原文](https://arxiv.org/abs/1807.03341)
- 版本：arXiv:1807.03341v2（2018-07-26），本地 PDF `papers/pdf/lipton2019troubling.pdf`。页码为 PDF 页脚页码。
- 说明：文章讨论的是机器学习领域的论文，但"区分解释与推测""找出提升的来源"等原则适用于各学科。

### E1

- 位置：§1 Introduction，第 1 页
- 原文："(i) provide intuition to aid the reader’s understanding, but clearly distinguish it from stronger conclusions supported by evidence; (ii) describe empirical investigations that consider and rule out alternative hypotheses"
- 要点：好论文要把直觉和有证据支持的结论分开，并且在实验中考虑、排除其他可能的解释。

### E2

- 位置：§3.1 Explanation vs. Speculation，第 2 页
- 原文："papers often oﬀer speculation in the guise of explanations, which are then interpreted as authoritative due to the trappings of a scientiﬁc paper and the presumed expertise of the authors."
- 要点：论文常把推测包装成解释；读者因为它出现在论文里、出自专家之手，就当成定论。

### E3

- 位置：§3.1，第 3 页（正面例子：dropout 论文）
- 原文："a designated “Motivation” section clearly quarantines this discussion. This practice avoids confusing readers while allowing authors to express informal ideas."
- 要点：把推测性的讨论放进单独标明的一节，既能表达非正式的想法，又不会让读者混淆。

### E4

- 位置：§3.2 Failure to Identify the Sources of Empirical Gains，第 3 页
- 原文："Too frequently, authors propose many tweaks absent proper ablation studies, obscuring the source of empirical gains. Sometimes just one of the changes is actually responsible for the improved results."
- 要点：同时提出很多改动却不做消融实验，就看不出提升从哪里来；有时真正起作用的只有其中一个改动。

### E5

- 位置：§3.2，第 3 页
- 原文："a series of published improvements, originally attributed to complex innovations in network architectures, were actually due to better hyperparameter tuning. On equal footing, vanilla LSTMs, hardly modiﬁed since 1997, topped the leaderboard."
- 要点：（机器学习的例子）一系列被归功于复杂新结构的改进，实际来自更好的调参；在同等条件下，老方法反而最好。说明比较不公平会制造虚假的进步。

### E6

- 位置：§3.2，第 3 页
- 原文："ablation is neither necessary nor suﬃcient for understanding a method, and can even be impractical given computational constraints."
- 要点：消融实验不是理解一个方法的唯一途径，计算资源有限时也可能做不了；稳健性检查和错误分析同样能带来理解。

### E7

- 位置：§5.1 Suggestions for Authors，第 8 页
- 原文："We encourage authors to ask “what worked?” and “why?”, rather than just “how well?”."
- 要点：不只问"效果有多好"，更要问"什么起了作用、为什么"。

### E8

- 位置：§5.1，第 8 页
- 原文："Three practices that are common in the strongest empirical papers are error analysis, ablation studies, and robustness checks"
- 要点：最强的实证论文常见三种做法：错误分析、消融实验、稳健性检查。

### E9

- 位置：§5.2 Suggestions for Publishers and Reviewers，第 8 页
- 原文："a paper describing a simple idea that leads to improved performance, together with two negative results, should be judged more favorably than a paper that combines three ideas together (without ablation studies) yielding the same improvement."
- 要点：一个简单想法加两个负面结果的论文，应当比把三个想法捆在一起、不做消融、得到同样提升的论文评价更高。

### E10

- 位置：§6.1 Countervailing Considerations，第 9 页
- 原文："the breakthrough paper on ImageNet classiﬁcation proposes multiple techniques without ablation studies, several of which were subsequently determined to be unnecessary. However, at the time the results were so signiﬁcant and the experiments so computationally expensive to run that waiting for ablations to complete was perhaps not worth the cost to the community."
- 要点：反方考虑：有时结果足够重要、实验又很昂贵，等消融做完再发表可能得不偿失。作者承认这类考虑有道理。

### E11

- 位置：§1，四种趋势之一
- 原文："Failure to distinguish between explanation and speculation."
- 要点：常见问题之一：不区分有证据的解释和推测。

### E12

- 位置：§3.1
- 原文："We ourselves have been equally guilty of speculation disguised as explanation."
- 要点：作者承认自己也犯过"把推测伪装成解释"的错误，说明这是很容易犯的错。

### E13

> 已作废：与 [E3](#e3) 重复（原文被 E3 完整包含）。

- 位置：§3.1
- 原文："a designated “Motivation” section clearly quarantines this discussion"
- 要点：好的做法：把推测放在专门的小节里，与有证据的结论明确隔开。

### E14

> 已作废：与 [E4](#e4) 重复（原文被 E4 完整包含）。

- 位置：§3.2
- 原文："Too frequently, authors propose many tweaks absent proper ablation studies, obscuring the source of empirical gains."
- 要点：同时做了很多改动却不逐一检验，会掩盖效果真正来自哪里。

### E15

- 位置：§4.1
- 原文："Authors with strong results may feel licensed to insert arbitrary unsupported stories"
- 要点：结果好时，作者容易觉得可以随意加入没有证据支持的解释。

### E16

- 位置：§2 Disclaimers
- 原文："This paper aims to instigate discussion, answering a call for papers from the ICML Machine Learning Debates workshop. While we stand by the points represented here, we do not purport to offer a full or balanced viewpoint or to discuss the overall quality of science in ML."
- 要点：作者说明文章的定位：为 ICML 一个辩论性质的研讨会而写，目的是引发讨论；坚持文中观点，但不声称观点全面、平衡，也不评价机器学习研究的整体质量。

### E17

- 位置：§2 Disclaimers
- 原文："We note that these arguments are made by us, against us, by insiders offering a critical introspective look, not as sniping outsiders." / "Exhibiting one of these patterns doesn’t make a paper bad nor does it indict the paper’s authors"
- 要点：作者强调批评来自圈内人的自我反省，也针对自己；一篇论文出现这些问题，不代表它是坏论文，也不是在指控作者。

### E18

- 位置：§2 Disclaimers
- 原文："our guiding principles are to (i) implicate ourselves, and (ii) to preferentially select from the work of better-established researchers and institutions that we admire, to avoid singling out junior students for whom inclusion in this discussion might have consequences and who lack the opportunity to reply symmetrically."
- 要点：举例的原则：一是把自己也算进去；二是优先选自己敬重的知名研究者和机构的工作，避免点名年轻学生——他们被点名可能受影响，也没有对等的回应机会。

### E19

- 位置：§3 Troubling Trends
- 原文："In each subsection below, we (i) describe a trend; (ii) provide several examples (as well as positive examples that resist the trend); and (iii) explain the consequences. Pointing to weaknesses in individual papers can be a sensitive topic. To minimize this, we keep examples short and specific."
- 要点：每一节的写法：描述一种趋势，给几个例子（也给出没有这个问题的正面例子），再解释后果；指出具体论文的弱点是敏感的，所以例子要简短、具体。

### E20

- 位置：§3.1，正面例子
- 原文："Here, the authors carefully convey uncertainty. Instead of presenting the guidelines as authoritative, the paper states" / "they should be challenged. They constitute a good starting point"
- 要点：正面例子：一篇给出神经网络训练指南的论文，没有把指南说成权威结论，而是说明它们应当接受质疑、只是一个好的起点。

### E21

- 位置：§6.1 Countervailing Considerations
- 原文："There are a number of countervailing considerations to the suggestions set forth above." / "We recognize the validity of these considerations, and also recognize that these standards are at times exacting." / "we present these as strong heuristics rather than unbreakable rules"
- 要点：作者专门用一节讨论反对自己建议的理由，承认这些理由成立、自己的标准有时要求很高，并把建议定位为"强有力的经验法则"而不是不可违反的规则。
