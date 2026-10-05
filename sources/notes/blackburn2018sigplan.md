# Berger, Blackburn, Hauswirth & Hicks 2018：SIGPLAN Empirical Evaluation Checklist

- 资料：`blackburn2018sigplan`，[原文](http://www.sigplan.org/Resources/EmpiricalEvaluation/)
- 版本：2018 年 10 月版，单页清单加注释和 FAQ。本地 PDF `papers/pdf/blackburn2018sigplan.pdf`。
- 说明：ACM SIGPLAN（美国计算机协会程序设计语言分会）为本领域实证评估制定的清单。其中的编译器、基准测试套件等例子属于计算机领域；"主张要明确""基线要合适""报告分布"等类别适用于各学科。

### E1

- 位置：Clearly Stated Claims › Claims not explicit
- 原文："Claims must be explicit in order for the reader to assess whether the empirical evaluation supports them."
- 要点：主张必须写明确，读者才能判断实验是否支持它。

### E2

- 位置：Clearly Stated Claims › Claims not appropriately scoped
- 原文："The truth of a claim should clearly follow from the evidence provided. Claims that are not fully supported mislead readers."
- 要点：主张要能从给出的证据中清楚地推出；证据支撑不足的主张会误导读者。

### E3

- 位置：Clearly Stated Claims › Fails to acknowledge limitations
- 原文："Stating no limitations at all, or only tangential ones, while omitting the more relevant ones may mislead the reader into drawing overly-strong conclusions."
- 要点：不写局限，或只写无关紧要的局限、漏掉真正相关的，会让读者得出过强的结论。

### E4

- 位置：Suitable Comparison › Fails to compare against appropriate baseline
- 原文："A ‘straw man’ baseline that is misrepresented as state-of-the-art is also problematic, as it would inﬂate apparent beneﬁt."
- 要点：把很弱的"稻草人"基线说成最先进方法，会夸大新方法的好处。

### E5

- 位置：Suitable Comparison › Comparison is unfair
- 原文："Comparisons to a competing system should not unfairly disadvantage that system."
- 要点：比较时不能让对手处于不公平的劣势。原文的例子是计算机领域的：对手用最低优化级别编译，自己用最高级别。

### E6

- 位置：Notes › Fails to Compare Against Appropriate Baseline
- 原文："The baseline could also be an unsophisticated approach to the same problem, e.g., a fancy testing tool is usefully compared against one that is purely random, in order to see whether it does better."
- 要点：基线也可以是同一问题的朴素做法，例如拿精巧的工具和纯随机的做法比，看它是否真的更好。

### E7

- 位置：Adequate Data Analysis › Insufficient number of trials
- 原文："Failure to do so risks treating noise as signal."
- 要点：重复次数不够，可能把噪声当成信号。

### E8

- 位置：Adequate Data Analysis › No data distribution reported
- 原文："Reporting just a measure of central tendency (e.g., a mean or median) can mislead the reader, especially when the distribution is bimodal or has signiﬁcant variance."
- 要点：只报平均数或中位数会误导读者，要同时报告波动程度（方差、标准差、分位数）或置信区间。

### E9

- 位置：Appropriate and Clear Experimental Design › Misleading summary of results
- 原文："it is not appropriate to summarize speedups of 4%, 6%, 7%, and 49% as ’up to 49%’. Instead, the full distribution of results must be reported."
- 要点：不能把 4%、6%、7%、49% 概括成"最高提升 49%"，要报告完整的结果分布。

### E10

- 位置：Notes › Fails to Acknowledge Limitations
- 原文："threats to validity sections in software engineering papers often mention threats of little signiﬁcance while ignoring real threats."
- 要点：有人批评"效度威胁"一节常常只列无关紧要的威胁、回避真正的威胁。清单作者认为这不能成为不写局限的理由。

### E11

- 位置：Notes › Fails to Acknowledge Limitations
- 原文："For science to progress, we need to be honest about what we have achieved."
- 要点：科学要进步，就要诚实说明自己到底做到了什么。

### E12

- 位置：Appropriate and Clear Experimental Design › Tested on training set
- 原文："When a system aims to be general but was developed with close consideration of speciﬁc examples, it is essential that the evaluation explicitly perform cross-validation, so that the system is evaluated on data distinct from the training set."
- 要点：开发时参考过的例子不能再拿来评估，必须在开发时没用过的数据上评估。

### E13

- 位置：Relevant Metrics › Indirect or inappropriate proxy metric
- 原文："Proxy metrics can substitute for direct ones only when the substitution is clearly, explicitly justiﬁed."
- 要点：用间接指标代替真正关心的指标，必须明确说明为什么可以代替。

### E14

- 位置：标题下说明
- 原文："This checklist is meant to support informed judgement, not supplant it."
- 要点：清单用于辅助判断，不能代替判断。
