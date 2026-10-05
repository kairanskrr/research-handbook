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

### E15

- 位置：Suitable Comparison › Comparison is unfair
- 原文："Comparisons to a competing system should not unfairly disadvantage that system." / "it would be unfair to compile the state-of-the-art baseline at -O0 optimization level, while using -O3 for the proposed system."
- 要点：比较时不能让对手处于不公平的劣势，例如对手用最低优化级别编译，自己用最高级别。

### E16

- 位置：Principled Benchmark Choice › Inappropriate suite
- 原文："Evaluations should be conducted using appropriate established benchmarks where they exist so that claimed results are more likely to generalize." / "it would be wrong to use a singlethreaded suite for studying parallel performance."
- 要点：有公认的基准套件时应当使用，结果更可能推广；但要用在合适的场合，例如不能用单线程套件研究并行性能。

### E17

- 位置：Principled Benchmark Choice › Unjustiﬁed use of non-standard suite(s)
- 原文："sometimes a non-standard suite, such as one that is subsetted or homegrown, is the better choice. In that case, a rationale, and possible limitations, must be provided to demonstrate why using a standard suite would have been worse."
- 要点：使用裁剪过的或自建的非标准套件时，必须给出理由和可能的局限，说明为什么用标准套件会更差。

### E18

- 位置：Notes › Unjustiﬁed Use of Non-Standard Suite(s)
- 原文："A concern we heard was that use of standard suites may lead to work that overﬁts to that benchmark." / "Papers we looked at often subset a benchmark, or cherry-picked particular programs."
- 要点：有人担心标准套件会导致研究过拟合基准；清单作者认为编程语言领域更常见的是相反问题：裁剪基准、挑选特定程序。

### E19

- 位置：Notes › Unjustiﬁed Use of Non-Standard Suite(s)
- 原文："Note that ‘benchmark’ in this category includes what is measured and the parameters of that measurement. One example of an oft-unappreciated benchmark parameter is timeout choice."
- 要点：基准不只是测什么，还包括测量的参数；超时设置就是常被忽视的基准参数。

### E20

- 位置：Principled Benchmark Choice › Kernels instead of full applications
- 原文："a claim that a system beneﬁts applications should be tested on such applications directly, and not only on micro-kernels, which may lack important characteristics of full applications."
- 要点：主张对应用有好处，就要直接在应用上测，不能只用小的核心代码片段，它们可能缺少完整应用的重要特征。

### E21

- 位置：Appropriate and Clear Experimental Design › Fails to measure all important Effects
- 原文："All important effects should be measured to show the true cost of a system."
- 要点：要测量所有重要的影响，展示系统真实的代价。原文例子：编译优化让程序变快，但可能大幅增加编译时间，编译时间也要测。

### E22

- 位置：Appropriate and Clear Experimental Design › Insufﬁcient information to repeat
- 原文："All parameters (including default values) should be included, as well as all version numbers of software, and full details of hardware platforms."
- 要点：要写出全部参数（包括默认值）、所有软件版本号和硬件平台的完整细节。

### E23

- 位置：Appropriate and Clear Experimental Design › Unreasonable platform
- 原文："a claim that relates to performance on mobile platforms should not have an evaluation performed exclusively on servers."
- 要点：评测平台要和主张相符，例如关于移动平台性能的主张不能只在服务器上评测。

### E24

- 位置：Appropriate and Clear Experimental Design › Ignores key design parameters
- 原文："Key parameters should be explored over a range to evaluate sensitivity to their settings." / "All expected system conﬁgurations (e.g., from warmup to steady state) should be considered."
- 要点：关键参数要在一个范围内变化，看结果对它多敏感；要考虑所有预期的系统状态，例如从预热到稳态。

### E25

- 位置：Appropriate and Clear Experimental Design › Gated workload generator
- 原文："Load generators for typical transaction-oriented systems should be ’open loop’, to generate work independent of the performance of the system under test."
- 要点：面向事务的系统，负载生成器应当是"开环"的：产生请求的速度不受被测系统快慢的影响。

### E26

- 位置：Appropriate and Clear Experimental Design › Tested on training set
- 原文："a static analysis should not be exclusively evaluated on programs used to inform its development."
- 要点：开发时参考过的程序不能作为唯一的评估对象，要在开发时没用过的数据上评估。

### E27

- 位置：Adequate Data Analysis › Insufﬁcient number of trials
- 原文："Failure to do so risks treating noise as signal. Similarly, more trials may be needed to get the system into an intended state (e.g., into a steady state that avoids warm-up effects)."
- 要点：性能不确定的现代系统需要多次试验，否则可能把噪声当成信号；还可能需要更多轮次让系统进入预定状态，例如避开预热效应的稳态。

### E28

- 位置：Notes › Inappropriate Summary Statistics
- 原文："The geometric mean should only be used when comparing values with different ranges, and the harmonic mean when comparing rates. When distributions have outliers, a median should be presented."
- 要点：几何平均只用于比较量程不同的数值；比较速率用调和平均；分布有离群值时应给出中位数。

### E29

- 位置：Appropriate Presentation of Results › Inappropriately truncated axes / Ratios plotted incorrectly
- 原文："A truncated graph (with an axis not including zero) will exaggerate the importance of a difference." / "This misleading effect can be avoided either by using a log scale or by normalizing to the lowest (highest) value."
- 要点：坐标轴不从零开始会夸大差异；比值画在线性坐标上会扭曲观感（2.0 和 0.5 互为倒数，但离 1.0 的距离不同），应使用对数坐标或以最低（最高）值归一化。

### E30

- 位置：Appropriate Presentation of Results › Inappropriate level of precision
- 原文："reporting ’49.9%’ when the experimental error is +/- 1% overstates the level of precision of the result."
- 要点：实验误差为正负 1% 时报告"49.9%"，夸大了结果的精度。

### E31

- 位置：FAQ › How does the checklist relate to the artifact evaluation process?
- 原文："Artifact evaluation typically occurs after reviewing a paper, to check that the claims and evidence given in the paper match reality, in the artifact."
- 要点：制品评审（artifact evaluation）通常在论文审稿之后进行，检查论文中的主张和证据与提交的制品是否一致。
