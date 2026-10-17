# 测量

> 本页的道理适用于各学科，例子和具体做法以计算机为例。文中引用的心理学、计量、营养流行病学、催化化学等学科的规范，只代表各自学科的做法，标明了出处，不是所有研究的通则。

你在做"大模型与智能合约安全"，读论文时发现一件事：大家报告的检出率都很高，但你怀疑评测用的合约早就被模型"见过"。如果你最后想证明的是"这些数字不可信，应该这样测才准"，你做的就是**测量**这类研究：核心主张不是关于被测的东西，而是关于**尺子本身**。

把"测量"单独列为一种研究套路，是本手册的分组方式，资料里并没有把它作为独立的一类（见[这个分组从哪里来](README.md#这个分组从哪里来)）。它在各学科有不同的名字：计算机叫评测和基准，心理学叫量表编制，物理叫计量和不确定度。我们把它们放在一起，是因为它们回答的是同一类问题。术语见[核心术语](../00_start-here/key-concepts.md#研究套路)。

---

## 1. 这类研究产生什么知识

测量研究产生的知识是：**某个东西怎么测才准，现在的测法差在哪里，差了多少。**

它的核心主张通常是下面几种之一：

| 主张的样子 | 计算机例子 |
|---|---|
| 现有测量有缺陷 | "现有漏洞评测集中，大量合约出现在模型的训练数据里，检出率被高估了" |
| 现有指标测偏了 | "用'工具报警条数'衡量检出能力，会把同一个漏洞重复计数" |
| 新的测量更有效 | "用模型训练之后才部署的合约建的新评测集，更能反映真实检出能力" |
| 测量本身不稳定 | "两位专家给同一批合约标注漏洞，一致程度只有中等，标签本身有很大噪声" |
| 测量误差改变了结论 | "修正泄露后，大模型并不比传统静态分析工具好" |

**它和其他套路的区别：** [比较评估](compare_evaluate.md)问"A 和 B 哪个好"，[构建改进](build_improve.md)问"我的新东西是否更好"，它们都默认尺子是准的。测量研究恰恰去检查这把尺子。所以同一个评测集，在别人的论文里是工具，在你的论文里是研究对象。和[观察描述](observe_describe.md)的区别见[研究套路](README.md#怎样选出主要套路)里"怎样选出主要套路"一节。

**为什么值得做：** 测不准的问题，后面很难补救。心理学方法文献的说法是：如果测的根本不是想测的东西，再严谨的设计、再高级的统计、再大的样本，也纠正不了错误的推断[^flake2020measurement-e2]。在机器学习中，评测是研究社区的指挥棒，突破常和某个评测上的大幅提升联系在一起[^wei2024evals-e1]。尺子歪了，整个方向都可能跟着歪。

**写下来：** 用一句话写出你的测量主张，并写明它针对的是哪一把"尺子"（哪个评测集、指标、量表或仪器）。

## 2. 什么样的证据才够

一个持怀疑态度的审稿人，会对一把尺子追问五件事。你的证据要能逐一回答：

**① 你要测的东西定义清楚了吗？** 物理计量的国际指南（《测量不确定度表示指南》）写道：测量从明确"测什么、用什么方法、按什么程序"开始[^jcgm2008gum-e11]；定义要完整到所需精度下值是唯一的，比如要把一根约一米长的钢棒测到微米级，就要写明在什么温度和压力下的长度[^jcgm2008gum-e12]。心理学方法文献有类似的提醒：一开始没把构念（无法直接观察、只能间接测量的概念，如抑郁、态度）定义清楚，后面每个测量决定都难做，也给有意无意的操作留下空间[^flake2020measurement-e7]。在合约例子里，"检出漏洞"到底指报出漏洞类型、指出具体代码行，还是给出可利用的攻击，必须先说定。

**② 它测到你想测的东西了吗？** 这叫**构念效度**：实际测量的东西，是否真的代表你想研究的概念[^runeson2009guidelines-e3]。软件工程的实证研究标准要求基准评测论文必须讨论这一点[^ralph2020empirical-e100]。心理学的期刊报告标准强调，效度不是工具的固定属性，而是针对"按某种用途解释分数"说的[^appelbaum2018journal-e10]。量表编制文献里常见的效度证据有：新测量和测同一概念的其他测量高度相关（聚合效度），和本应测不同东西的测量相关不能过高（区分效度）[^boateng2018best-e20]；在已知应该有差别的两组上，确实测出差别，例如饮用水含大肠杆菌的家庭，"用水不安全"量表得分更高[^boateng2018best-e21]。

**③ 它稳定吗？** 这叫**信度**。例如同一批人隔一段时间再测，总分是否一致[^boateng2018best-e18]。如果数据靠人标注，要报告标注者之间的一致程度；质性研究的方法文献普遍认为，只算"百分之多少一致"不够，因为它没扣除碰巧一致的部分[^mcdonald2019reliability-e4]。做大模型评测集时，标准答案错误要少[^wei2024evals-e3]，评分要极其准确[^wei2024evals-e7]。

**④ 误差有多大？** 物理计量的国际指南要求：报告测量结果，必须给出它有多可信的定量说明，否则结果之间、结果和参考值之间都无法比较[^jcgm2008gum-e1]。系统误差和随机误差一样无法消除，但常常可以减小；识别出的系统效应可以修正[^jcgm2008gum-e18]。

**⑤ 换一把尺子，结论会变吗？** 不光指出问题，还要展示它造成了什么后果。我们认为这是测量研究最有说服力的部分。一个例子：有研究复查内战预测的 12 篇论文，发现有错误的 4 篇，恰好是声称复杂机器学习模型优于传统逻辑回归基线的那 4 篇；改正错误后，复杂模型并不比几十年前的逻辑回归好多少[^kapoor2023leakage-e8]。

**只检查一项不够。** 一项研究用约 14.4 万场次的实验数据，检验了社会与人格心理学常用的 15 份自评问卷（共 26 个量表）。只看内部一致性（同一量表各题的得分是否彼此一致），89% 显得效度良好；综合检验内部一致性、重测信度、因子结构，以及在年龄和性别组之间的测量不变性后，只有 4% 良好[^hussey2020hidden-e1]。这是对这一批量表的结果，不能直接推到别的工具上，但它说明单一指标可能严重误导。同一研究还指出，结果能重复，也不等于测量有效[^hussey2020hidden-e6]。

**举证责任在你。** 在机器学习用于科学研究的场景中，证明"没有泄露"的责任，在提出科学主张的研究者身上[^kapoor2023leakage-e9]。以"现有评测集被泄露高估"为例：

| 审稿人会问 | 需要的证据 |
|---|---|
| 泄露真的存在吗？ | 训练数据公开的模型：评测集有多大比例能在训练数据里找到[^sainz2023nlp-e4]；不公开的：利用模型的记忆能力，看它能否背出评测样本[^sainz2023nlp-e5] |
| 你的检测方法可靠吗？ | 在已知泄露和已知未泄露的样本上验证检测方法；人工抽查一批 |
| 泄露影响结论了吗？ | 去掉泄露样本前后，多个模型、多个工具的成绩和排名对比 |
| 新评测集更好在哪？ | 新集合的构建方法、标注一致性，以及它为什么不容易泄露 |

**写下来：** 对你的尺子，按上面五个问题各写一句"我打算用什么证据回答"。答不上的，就是项目里最需要先解决的部分。

## 3. 常用的研究方法

测量研究没有一种专属方法，下面这些常被用来拿到证据：

| 方法 | 能给你什么 | 去哪里看 |
|---|---|---|
| 基准评测 | 检查一个评测集或指标是否测到了想测的东西；数据污染的检查办法 | [基准评测](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗) |
| 量表编制 | 定义构念、编题、信度、效度、测量不变性的完整流程 | [量表编制与测量研究](../06_methods/scale_development.md) |
| 实验测量 | 定义被测量、校准、系统效应、不确定度预算 | [实验测量研究](../06_methods/experimental_measurement.md) |
| 问卷调查 | 测抽象概念时怎样选用验证过的量表 | [问卷调查](../06_methods/questionnaire_survey.md#第四步测量抽象概念时用验证过的量表) |
| 复现研究 | 换一套数据或测法重做，看原结论是否还在 | [复现研究](../06_methods/replication.md) |
| 方法论研究与元科学 | 系统调查一个领域的论文测量做得怎么样 | [方法论研究与元科学](../06_methods/meta_science.md) |

## 4. 它怎样影响整个项目

**读文献时：** 不只看结果，还要看每篇论文**怎么测的**：用了哪个评测集、指标怎么定义、有没有报告误差。很多论文对测量交代不全：一项检查发现，《人格与社会心理学杂志》论文用到的 433 个量表中，40% 没说来源[^flake2020measurement-e9]。交代不全的地方，往往就是测量研究的切入点。

**选题时：** 先在文献里找现成的、验证过的测量工具。软件工程的心理测量指南提醒，开发并验证一个新工具可能要好几年[^graziotin2021psychometrics-e4]。已有类似工具还要新编时，要说明为什么、和已有的有什么不同[^boateng2018best-e3]。如果你发现别人的评测有问题，"指出并修正它"本身就可以是一个项目，见[收敛成项目](../01_find-a-problem/05_converge.md#3-别人做过了吗)。

**设计时：**

- **先定义，再选尺子。** 名字相似的两个工具，不一定测同一个东西；名字不同的，也不一定测不同的东西[^flake2020measurement-e8]。
- **事先定好规则。** 删哪些题、怎样分组，最好动手前就定[^flake2020measurement-e10]；评估效度用哪些指标、什么阈值，也可以写进预注册[^hussey2020hidden-e9]。
- **建尺子和检验尺子用不同的数据。** 量表编制的理想做法是在样本 A 上编制，在独立的样本 B 上检验[^boateng2018best-e12]；计算机系统的性能评测里，校准和评估用的工作负载必须完全不重叠[^heiserbenchmarking-e12]。
- **防止数据泄露。** 在用机器学习做科学研究时，研究者建模时能接触全部数据，这正是泄露常发生的原因[^kapoor2023leakage-e3]。训练样本和测试样本不独立也算泄露，除非你的主张针对的本来就是有同样依赖关系的数据[^kapoor2023leakage-e6]。在合约例子里，大量复制粘贴的同源合约如果分在训练和测试两边，成绩就会虚高。

**执行时：** 计量指南提醒，不确定度评定不是例行公事，要靠对被测对象和测量过程的深入了解[^jcgm2008gum-e6]；记录或分析时的过失不在不确定度的涵盖范围内[^jcgm2008gum-e5]，所以要靠复查发现。做大模型评测集时，可以同时准备公开和私有两份测试集，监测模型在两者上的表现是否明显不同[^wei2024evals-e9]。

**写作时：** 计量指南建议，报告测量结果和不确定度时，宁可信息给多，不要给少[^jcgm2008gum-e7]。心理学的期刊报告标准要求说明工具是已验证的还是临时编的，尽可能报告本样本上的信度[^appelbaum2018journal-e4]；改动了已有工具，要说明怎么改、为什么改[^flake2020measurement-e6]；自编工具效度证据少，要作为局限讨论[^flake2020measurement-e13]。怎样写效度和局限，见[效度与局限](../02_do-the-project/04_validity-and-limits.md)。

**写下来：** 列出你项目里用到的每一把尺子（评测集、指标、标注、问卷），在旁边写"现成且验证过 / 现成但没验证 / 自己做"。后两类要单独安排检验。

## 5. 哪些学科有专门的测量规范

下面只列本手册资料中有依据的学科。其他学科没有列出，不代表它们不重视测量，只是本文资料未涉及。

| 学科 | 依据 |
|---|---|
| 计算机（软件工程） | 实证研究标准要求基准评测讨论构念效度[^ralph2020empirical-e100]；问卷调查要么用验证过的量表，要么事后分析构念效度[^ralph2020empirical-e236]；仓库挖掘要说明并论证所用的度量[^ralph2020empirical-e112] |
| 计算机（机器学习） | 数据污染会高估模型表现[^sainz2023nlp-e2]；在用机器学习做研究的 17 个科学领域中，已发现数据泄露问题，涉及 294 篇论文[^kapoor2023leakage-e1] |
| 心理学 | 伦理准则要求使用在被测人群中已确立效度和信度的工具[^apa2017ethical-e11]；有专门讨论"可疑测量做法"的文献[^flake2020measurement-e1] |
| 物理与计量 | 计量指南联合委员会发布的《测量不确定度表示指南》，要求报告物理量的测量结果时给出可信程度的定量说明[^jcgm2008gum-e1] |
| 化学（催化） | 有研究者提议多个课题组盲法轮流测量同一批样品，以确定现实的误差范围[^bligaard2016benchmarking-e8] |
| 流行病学与营养学 | 任何研究设计都会有测量误差，解释效应时总要考虑[^hernan2020whatif-e16]；单一饮食暴露只有个体内随机误差时，它与健康结局的关联估计总会被削弱[^nci2025dietprimer-e3] |

学科规矩的细节见各学科篇，例如[计算机](../07_fields/computer-science/README.md)、[心理学](../07_fields/psychology/README.md#测量用有效度证据的量表)。

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 用间接指标代替真正关心的东西，不说理由 | 程序设计语言领域的评测清单说，只有明确论证过，间接指标才能代替[^blackburn2018sigplan-e13] |
| 用启发式计数代替真实计数 | 例如模糊测试中按"不同崩溃数"计数，会严重多算缺陷，表面提升可能是假的[^klees2018evaluating-e4] |
| 只报一个一致性系数，就说测量有效 | 在上文那批心理学量表上，只看内部一致性时 89% 显得效度良好，综合检验后只有 4%[^hussey2020hidden-e1] |
| 有选择地挑指标和阈值，让工具看起来有效 | 这被称为"效度操纵"[^hussey2020hidden-e7] |
| 改动了验证过的量表，不声明 | 改动本身不一定错，不声明、不说明理由才威胁结论[^flake2020measurement-e12]；软件工程研究借用心理学量表时常改题，破坏了原有的信度和效度[^graziotin2021psychometrics-e1] |
| 标注一致性只报百分比 | 没扣除碰巧一致的部分[^mcdonald2019reliability-e4] |
| 不检查评测数据是否被模型见过 | 模型训练时见过评测集，实验完全无效[^sainz2023nlp-e3] |
| 只给数值，不给误差 | 计量指南指出，没有可信程度的说明，结果之间无法比较[^jcgm2008gum-e1] |
| 指出了测量问题，却不展示它对结论的影响 | 读者不知道这个问题有多要紧 |

## 7. 延伸阅读

- **Flake & Fried 2020**，*Measurement Schmeasurement*（心理学）：可疑测量做法，附一张透明报告测量的问题表[^flake2020measurement-e6]。
- **Kapoor & Narayanan 2023**（用机器学习做科学研究）：数据泄露的分类，和逐项检查用的"模型信息表"[^kapoor2023leakage-e10]。
- **Sainz 等人 2023**（自然语言处理）：大模型数据污染的定义和检测办法。
- **Hussey & Hughes 2020**（心理学）：15 份常用问卷的"隐藏的无效"，说明为什么只看一个指标不够。
- **JCGM 100:2008**（计量）：《测量不确定度表示指南》，常简称 GUM。
- **Boateng 等人 2018**（健康与行为科学）：量表编制和验证的步骤综述。

[^flake2020measurement-e1]: Flake & Fried 2020，Abstract。[证据](../../sources/notes/flake2020measurement.md#e1)
[^flake2020measurement-e2]: Flake & Fried 2020，Introduction。[证据](../../sources/notes/flake2020measurement.md#e2)
[^flake2020measurement-e6]: Flake & Fried 2020，Table 1。[证据](../../sources/notes/flake2020measurement.md#e6)
[^flake2020measurement-e7]: Flake & Fried 2020，Question 1。[证据](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e8]: Flake & Fried 2020，Question 2。[证据](../../sources/notes/flake2020measurement.md#e8)
[^flake2020measurement-e9]: Flake & Fried 2020，Question 3（转述 Flake 等人 2017）。[证据](../../sources/notes/flake2020measurement.md#e9)
[^flake2020measurement-e10]: Flake & Fried 2020，Question 4。[证据](../../sources/notes/flake2020measurement.md#e10)
[^flake2020measurement-e12]: Flake & Fried 2020，Question 5。[证据](../../sources/notes/flake2020measurement.md#e12)
[^flake2020measurement-e13]: Flake & Fried 2020，Question 6。[证据](../../sources/notes/flake2020measurement.md#e13)
[^wei2024evals-e1]: Wei 2024，第 1 段。[证据](../../sources/notes/wei2024evals.md#e1)
[^wei2024evals-e3]: Wei 2024，评测常见错误。[证据](../../sources/notes/wei2024evals.md#e3)
[^wei2024evals-e7]: Wei 2024，评测常见错误。[证据](../../sources/notes/wei2024evals.md#e7)
[^wei2024evals-e9]: Wei 2024，测试集污染。[证据](../../sources/notes/wei2024evals.md#e9)
[^jcgm2008gum-e1]: JCGM 100:2008，0.1。[证据](../../sources/notes/jcgm2008gum.md#e1)
[^jcgm2008gum-e5]: JCGM 100:2008，3.4.7。[证据](../../sources/notes/jcgm2008gum.md#e5)
[^jcgm2008gum-e6]: JCGM 100:2008，3.4.8。[证据](../../sources/notes/jcgm2008gum.md#e6)
[^jcgm2008gum-e7]: JCGM 100:2008，7.1.4。[证据](../../sources/notes/jcgm2008gum.md#e7)
[^jcgm2008gum-e11]: JCGM 100:2008，3.1.1。[证据](../../sources/notes/jcgm2008gum.md#e11)
[^jcgm2008gum-e12]: JCGM 100:2008，3.1.3。[证据](../../sources/notes/jcgm2008gum.md#e12)
[^jcgm2008gum-e18]: JCGM 100:2008，3.2.3。[证据](../../sources/notes/jcgm2008gum.md#e18)
[^runeson2009guidelines-e3]: Runeson & Höst 2009，§5.2.3。[证据](../../sources/notes/runeson2009guidelines.md#e3)
[^ralph2020empirical-e100]: SIGSOFT 基准评测标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e112]: SIGSOFT 仓库挖掘标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e112)
[^ralph2020empirical-e236]: SIGSOFT 问卷调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e236)
[^appelbaum2018journal-e4]: Appelbaum 等人 2018，Table 1，Psychometrics。[证据](../../sources/notes/appelbaum2018journal.md#e4)
[^appelbaum2018journal-e10]: Appelbaum 等人 2018，Changes in Table 1，Psychometrics。[证据](../../sources/notes/appelbaum2018journal.md#e10)
[^apa2017ethical-e11]: 美国心理学会伦理准则，9.02(b)。[证据](../../sources/notes/apa2017ethical.md#e11)
[^boateng2018best-e3]: Boateng 等人 2018，Step 1。[证据](../../sources/notes/boateng2018best.md#e3)
[^boateng2018best-e12]: Boateng 等人 2018，Step 4。[证据](../../sources/notes/boateng2018best.md#e12)
[^boateng2018best-e18]: Boateng 等人 2018，Step 8。[证据](../../sources/notes/boateng2018best.md#e18)
[^boateng2018best-e20]: Boateng 等人 2018，Step 9。[证据](../../sources/notes/boateng2018best.md#e20)
[^boateng2018best-e21]: Boateng 等人 2018，Step 9（已知组比较）。[证据](../../sources/notes/boateng2018best.md#e21)
[^mcdonald2019reliability-e4]: McDonald 等人 2019，§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e4)
[^kapoor2023leakage-e1]: Kapoor & Narayanan 2023，Summary。[证据](../../sources/notes/kapoor2023leakage.md#e1)
[^kapoor2023leakage-e3]: Kapoor & Narayanan 2023，Leakage in modeling competitions。[证据](../../sources/notes/kapoor2023leakage.md#e3)
[^kapoor2023leakage-e6]: Kapoor & Narayanan 2023，Taxonomy [L3.2]。[证据](../../sources/notes/kapoor2023leakage.md#e6)
[^kapoor2023leakage-e8]: Kapoor & Narayanan 2023，Summary；内战预测案例。[证据](../../sources/notes/kapoor2023leakage.md#e8)
[^kapoor2023leakage-e9]: Kapoor & Narayanan 2023，Model info sheets。[证据](../../sources/notes/kapoor2023leakage.md#e9)
[^kapoor2023leakage-e10]: Kapoor & Narayanan 2023，Summary。[证据](../../sources/notes/kapoor2023leakage.md#e10)
[^hussey2020hidden-e1]: Hussey & Hughes 2020，Abstract。[证据](../../sources/notes/hussey2020hidden.md#e1)
[^hussey2020hidden-e6]: Hussey & Hughes 2020，Discussion。[证据](../../sources/notes/hussey2020hidden.md#e6)
[^hussey2020hidden-e7]: Hussey & Hughes 2020，Discussion。[证据](../../sources/notes/hussey2020hidden.md#e7)
[^hussey2020hidden-e9]: Hussey & Hughes 2020，Discussion。[证据](../../sources/notes/hussey2020hidden.md#e9)
[^sainz2023nlp-e2]: Sainz 等人 2023，摘要。[证据](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e3]: Sainz 等人 2023，§3。[证据](../../sources/notes/sainz2023nlp.md#e3)
[^sainz2023nlp-e4]: Sainz 等人 2023，§5.1。[证据](../../sources/notes/sainz2023nlp.md#e4)
[^sainz2023nlp-e5]: Sainz 等人 2023，§5.2。[证据](../../sources/notes/sainz2023nlp.md#e5)
[^graziotin2021psychometrics-e1]: Graziotin 等人 2021，§1.1。[证据](../../sources/notes/graziotin2021psychometrics.md#e1)
[^graziotin2021psychometrics-e4]: Graziotin 等人 2021，§13。[证据](../../sources/notes/graziotin2021psychometrics.md#e4)
[^heiserbenchmarking-e12]: Heiser，Same dataset for calibration and validation。[证据](../../sources/notes/heiserbenchmarking.md#e12)
[^blackburn2018sigplan-e13]: SIGPLAN 清单 2018，Indirect or inappropriate proxy metric。[证据](../../sources/notes/blackburn2018sigplan.md#e13)
[^klees2018evaluating-e4]: Klees 等人 2018，§9。[证据](../../sources/notes/klees2018evaluating.md#e4)
[^bligaard2016benchmarking-e8]: Bligaard 等人 2016，§2.2.1。[证据](../../sources/notes/bligaard2016benchmarking.md#e8)
[^hernan2020whatif-e16]: Hernán & Robins，第 9 章开头。[证据](../../sources/notes/hernan2020whatif.md#e16)
[^nci2025dietprimer-e3]: 美国国家癌症研究所饮食评估入门，Effects of Measurement Error。[证据](../../sources/notes/nci2025dietprimer.md#e3)
