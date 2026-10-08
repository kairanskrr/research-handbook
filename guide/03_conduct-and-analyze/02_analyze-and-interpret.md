# 分析与解读

> 本章的道理适用于各学科，例子和具体做法以计算机为例。第 3 节讲的数字和统计，主要针对定量研究；做定性研究的，可以取其道理。

## 你现在在哪里

实验跑完了，或者数据收齐了。你手里有一堆数字、表格、日志，也许还有几张初步画出的图。

你现在可能正面对这样的问题：

- 结果看上去不错，但心里没底：是真的，还是哪里弄错了？
- 原来计划的分析做完了，结果一般；换个分析方法，好像就"显著"了，能这样写吗？
- p 值小于 0.05，是不是就说明方法有效？
- 结果和预期相反，或者什么都没发现，这个项目是不是白做了？
- 论文里，结论能写到多大？

## 这一阶段要解决什么

把一堆结果，变成**有证据撑着的结论**。具体来说，是回答下面七个问题：

1. 数据和程序有没有出错？
2. 哪些分析是事先计划好的，哪些是看到数据后才想到的？
3. 差异有多大，有多确定？
4. 除了你的解释，还有什么可能产生同样的结果？
5. 负面的、出乎意料的结果，怎么对待？
6. 结论能说到多远？
7. 证据和原来的主张对不上时，怎么改？

## 这一章怎么用

第 1 节到第 6 节大致按顺序做：先确认数据没错，再做分析，再解读。第 7 节随时可能用上：任何一步发现证据撑不住原来的主张，都要回来改主张。

不同研究套路要的统计细节不一样。和基线比、做消融实验、多次运行比较工具，这些具体做法放在套路篇里：[比较评估](../05_research-strategies/compare_evaluate.md#差异是不是真的)、[构建改进](../05_research-strategies/build_improve.md)、[解释因果](../05_research-strategies/explain_causality.md#主动排除其他解释)。本章只讲各类研究都要做的那部分 `[本项目分析]`。

本章的所有做法，都是为了一件事：不要骗自己，而你自己恰恰是最容易被骗的人[^feynman1974cargo-e7]。

---

## 1. 先确认数据没出错，再看结论

**拿到结果后，先别急着解读。第一件事是亲自看原始数据和原始输出。**

很多错误不会报错。训练神经网络就是一个典型：程序语法完全正确，整个流程却没有按你以为的方式运行，而且很难看出来[^karpathy2019recipe-e3]。所以要动手翻：

- **一条一条看几十个原始样本和输出。** 离群值（和其他数据差得特别远的值）尤其值得看。一份训练神经网络的经验总结说，它们几乎总能暴露数据质量或预处理的问题[^karpathy2019recipe-e7]。软件工程的数据科学标准把"人工检查相当一部分数据"列为加分做法，也就是数据合理性检查[^ralph2020empirical-e199]。
- **别因为数据集有名就不查。** 机器学习的方法指南提醒：一个数据集被很多论文用过，不代表它质量好[^lones2021avoid-e19]。软件工程里，一项研究缺陷数据误分类问题的论文在结论中写道：自动化的定量分析，始终要加上人对输入数据和分析结果的检查；用缺陷数据集之前，至少要人工验证足够多的样本[^herzig2013bug-e5]。
- **找重复和异常，但别乱删。** 同一份机器学习指南说，常见的问题是同一条数据被无意中收录了几份；离群值只有在可能是噪声或错误时才删，不要删掉真实存在的极端情况[^lones2021avoid-e20]。删了什么、为什么删，都记下来 `[本项目分析]`。

**结果好得出乎意料时，更要查。** 有一种自我欺骗叫检查不对称：结果偏离预期时拼命找错，接近预期时就不仔细查了。电子电荷测量史上就出过这样的事，后来的测量者测出的数值比权威结果高出太多时，就去找"哪里出了错"；接近时就不再细查[^feynman1974cargo-e14]。只查一个方向，结果就会被拉向你预期的样子。对"好结果"和"坏结果"，用同样的力度去查 `[本项目分析]`。

用"大模型检测智能合约漏洞"举例，看到检出率高达 95%，先查这几件事 `[本项目分析]`：

| 要查的 | 怎么查 |
|---|---|
| 输出解析对不对 | 随机抽 30 条模型原始输出，人工判断，和程序解析的结果对一遍 |
| 标签对不对 | 抽查一批"有漏洞"的合约，确认漏洞真的存在 |
| 有没有重复 | 查评测集里有没有同一份合约换了名字出现多次 |
| 模型是不是"见过" | 查这些合约是否早在模型训练截止之前就公开了 |
| 离群的样本 | 看检出时间最长、输出最长、最短的几个例子 |

**写下来：** 列出你的结果可能"假好看"的三个原因，各用一个最便宜的办法查一遍。查完再往下走。

## 2. 先做计划好的分析，计划外的标成探索性

**先按动手前定好的计划做分析，把计划里的每一项结果都写下来，不管好坏。看到数据后才想到的分析，可以做，但要单独标成"探索性"。**

为什么要这么分？因为"事先预测"和"事后解释"给出的证据强度不同。看到结果后再提出假设，却写得像是事先就有的，叫"结果已知后再提假设"（hypothesizing after the results are known，简称 HARKing）[^nosek2018preregistration-e2]。软件工程的实证研究标准把两件事列为反面做法：在声称是验证性的研究里这样提假设，以及只报告显著的那部分统计检验[^ralph2020empirical-e27]。后一种做法叫 p 值操纵（p-hacking）。

光靠"我不会这样做"的决心是不够的：记忆会出错，人会不自觉地往想要的方向推理，这些偏差常常发生在意识之外[^nosek2018preregistration-e3]。心理学的方法学者指出，研究者通常没意识到自己在做 p 值操纵，也没意识到它的后果[^nelson2018psychology-e8]。他们描述过第一次分析不显著时研究者的典型做法：接着翻数据，看是不是离群值干扰了效应，换一部分参与者看看，或者换一种方式给结果变量编码[^nelson2018psychology-e6]。每一步单看都说得过去；在他们的模拟里，这类做法叠加起来，能把假阳性率（把没有的效应当成有）从 5% 抬到 61%[^nelson2018psychology-e7]。

**怎么做：**

- **计划里的分析全部报告。** 定了分析计划，计划中所有分析的结果都要报告，否则还是选择性报告[^nosek2018preregistration-e6]。这不是苛求：一项盘点分析了政治学和经济学两个登记平台上的 195 份预分析计划[^ofosu2023preanalysis-e1]，发现样本里的中位数论文漏报了分析计划中 25% 的假设[^ofosu2023preanalysis-e9]。
- **计划外的分析，标出来并说明为什么加。** 政治学的一份方法指南写道：探索性分析是可以做的，事先写分析计划的目的不是禁止它，而是把它的来龙去脉写清楚[^egappreanalysis-e5]。上面那项盘点的作者也主张：可以自由做计划外的探索，但论文里要明确标出哪些分析不是事先定好的，并解释为什么加[^ofosu2023preanalysis-e14]。同一项盘点里，报告了计划外假设的论文，82% 没有说明这一点[^ofosu2023preanalysis-e10]。美国心理学会的定量研究报告标准，也把假设、分析和结论分成主要、次要、探索性三类[^appelbaum2018journal-e1]。
- **偏离了计划，写明改了什么、为什么改。** 如实报告改动和理由，仍比完全没有计划可信得多[^nosek2018preregistration-e5]。但同一项盘点里，模型偏离计划的 14 处，只有 1 处说明了改动[^ofosu2023preanalysis-e7]。
- **事后分出来的子群，结论要格外小心。** 医学临床试验的报告规范写道：看过数据后才做的亚组比较，尤其难被后续研究证实；一个亚组显著、另一个不显著，也不能据此说两组之间有差异[^hopewell2025consortee-e49]。

这么做的目的，不是说事先预测比事后探索高级，而是让人分清哪个是哪个[^nosek2018preregistration-e4]。探索性的发现往往正是下一个项目的起点 `[本项目分析]`。

**如果动手前没写分析计划** `[本项目分析]`：现在补写一份，按你看结果之前"本来会怎么做"来写，越早越好；论文里诚实说明哪些分析是看到结果后才定的。下次在[从研究问题到证据清单](../02_from-project-to-study/01_question-to-evidence.md)那一步就把分析计划写好。

**写下来：** 画一张分析清单，每做一项分析就加一行。

| 分析 | 计划内 / 探索性 | 什么时候决定做的 | 为什么做 | 结果（不论好坏） |
|---|---|---|---|---|
| 新方法与基线的总检出率 | 计划内 | 开题时 | 核心主张 | |
| 按漏洞类型分开看 | 探索性 | 看到总结果后 | 怀疑提升集中在某一类 | |

## 3. 报告差多少、有多确定，而不只是 p 值

**每个关键结果，都回答两个问题：差异（或关联）有多大？这个数有多确定？** 前者是效应量，后者是不确定性，常用置信区间（真实值大概率落在的范围）或标准误表示。

不同学科的报告规范和方法文献，在这一点上意见一致：

- 教育研究的报告标准要求，关键统计结果要报告效应量，例如干预效应、回归系数[^aera2006standards-e8]，还要报告它的不确定性，例如标准误或置信区间[^aera2006standards-e9]。
- 医学临床试验的报告规范要求，所有结局都要给出效应量的置信区间，不要只报 p 值[^hopewell2025consortee-e52]。
- 计算机性能评测方向的建议是：用效应量的置信区间报告性能变化，它说明了变化有多大、误差范围多大、有多确定，比显著性检验更不容易被误读[^kalibera2013rigorous-e8]。

**为什么不能只看 p 值？**

- **显著不等于重要。** 机器学习的方法指南提醒，样本足够多时，再小的差异也能显著[^lones2021avoid-e8]。软件分析方向举过一个例子：一个"显著"的相关系数只有 0.01，实际意义可以忽略，和没有相关没有区别[^menzies2019bad-e2]。所以方法学者建议，在研究开始前就定下"多大的差异才算有实际意义"，叫最小有意义效应量[^menzies2019bad-e3]。
- **不显著也不等于没有差别。** 结果不显著时，别急着写"两者没有差异"，先看置信区间有多宽：区间很宽，只说明这次的数据还分辨不出来 `[本项目分析]`。也不要事后用这次的结果去算统计功效（研究能检测出真实差异的概率），拿它来解释不显著，这样做没有价值，还可能误导读者[^hopewell2025consortee-e18]。
- **一样大的效应，重要性未必一样。** 一篇解读教育干预效应量的文章指出，大小相同的效应，重要性很少相同[^kraft2019interpreting-e21]。它举的例子是：效果相近时，成本低的干预更值得重视[^kraft2019interpreting-e13]。计算机里也一样，例如检出率提高同样 5 个百分点，一个靠多调用十倍的大模型接口，一个几乎不增加开销，意义就很不一样 `[本项目分析]`。

**怎么做：**

- **报告波动，而不只是平均数或最好的一次。** 编程语言方向的实证评估清单提醒，重复次数不够，可能把噪声当成信号[^blackburn2018sigplan-e7]。Java 性能评测的一个例子：只按最好的结果看，会得出一个垃圾回收器明显更快的结论；看置信区间，两者重叠，差异很可能只是随机波动[^georges2007statistically-e2]。一篇反讽软件工程"凑论文"套路的文章，把"反复运行、只报跑赢的那次"列为其中一招[^zeller2021devil-e1]。
- **概括要老实。** 同一份清单写道：不要把 4%、6%、7%、49% 的提升概括成"最高提升 49%"，要报告完整的分布[^blackburn2018sigplan-e9]。数字的精度也要和误差相称：误差有正负 1% 时报告"49.9%"，就夸大了精度[^blackburn2018sigplan-e30]。
- **检验做多了，要校正。** 机器学习的方法指南举例：做 20 次 95% 置信水平的两两检验，很可能有一次给出错误结论[^lones2021avoid-e7]。校正方法有很多，什么时候该校正也有争论[^lones2021avoid-e12]。至少要报告一共做了多少次比较 `[本项目分析]`。

在例子里，一句好的结果陈述是这样的 `[本项目分析]`："在 300 份训练截止后才出现的合约上，加入漏洞模式提示后，重入漏洞检出率从 41% 提高到 52%（5 次运行，提高量的 95% 置信区间为 6 到 16 个百分点）；误报率基本不变。"对比"检出率显著提高（p < 0.05）"，前一句让读者知道了差多少、多确定、在什么条件下。

具体用哪种检验、怎么算置信区间，请教导师或本学科的统计方法资料；比较工具和方法时的统计细节，见[比较评估：差异是不是真的](../05_research-strategies/compare_evaluate.md#差异是不是真的) `[本项目分析]`。

**写下来：** 把核心结果改写成上面那样的一句话：条件、效应量、不确定性、重复次数。写不出不确定性的，回去补实验或补计算。

## 4. 逐个排除其他解释

**看到结果后，问自己：除了我的解释，还有什么可能产生同样的结果？然后逐个去查。**

做实验时，要报告所有可能让结果不成立的因素：能解释结果的其他原因，以及哪些已经被你用别的实验排除了、怎么排除的[^feynman1974cargo-e11]。机器学习方向一篇批评学术写作风气的文章，也把"考虑并排除其他假设"列为好论文该做的事[^lipton2019troubling-e1]。

几乎每项研究都要先过这几关 `[本项目分析]`：

| 其他解释 | 问自己 | 例子里怎么查 |
|---|---|---|
| 偶然 | 换几次运行、换一批样本，结果还在吗？ | 多次运行，看置信区间（第 3 节） |
| 出错 | 是不是程序、标签、解析出了问题？ | 第 1 节的检查 |
| 测歪了 | 指标真的测到了你关心的东西吗？ | 只报检出率、不报误报，"提升"可能只是模型更爱报漏洞 |
| 别的因素 | 有没有你没控制的因素在同时变化？ | 提示更长了、换了模型版本、评测合约被模型"见过" |
| 只在这里成立 | 换个数据集、换个设置还成立吗？ | 换一批合约、换一个模型再试 |

"测歪了"这一条常被忽视。用间接指标代替真正关心的指标时，必须说明为什么可以代替[^blackburn2018sigplan-e13]。

**除了"效果有多好"，还要问"什么起了作用、为什么"**[^lipton2019troubling-e7]。同一篇文章说，最强的实证论文常见三种做法：错误分析（逐个看出错的例子，找出错在哪类情况）、消融实验、稳健性检查（换数据、换设置或换分析方法，看结论是否还成立）[^lipton2019troubling-e8]。

主张是因果关系（"X 导致 Y"）时，排除其他解释要更系统，见[解释因果](../05_research-strategies/explain_causality.md#主动排除其他解释)；主张是"新方法更好"时，提升从哪里来要靠消融实验说明，见[构建改进](../05_research-strategies/build_improve.md) `[本项目分析]`。效度威胁的系统讨论见[效度与局限](../02_from-project-to-study/03_validity-and-limits.md)。

**写下来：** 对核心结果列出至少三个其他解释。每个写一句：怎样查、查了没有、结果如何。查不了的，留着写进局限。

## 5. 负面结果和意外结果

**结果不如预期，先别下"这个想法不行"的结论；结果出乎意料，先别急着高兴，也别急着丢掉。**

**负面结果。** 一次实验失败，很容易得出"我试了 X，X 不行"。但如果 X 是一个思路，更准确的说法是：我试了 X 的一种具体做法，这种做法不行[^steinhardt2018stochastic-e10]。所以失败后要追问为什么，免得再试一堆会因为同样原因失败的做法[^steinhardt2018stochastic-e9]。代码和实验都查过还是不行，就退一步，检查想法本身[^huang2023unstuck-e5]。

查清楚之后，负面结果要照实报告。决定检验一个想法，就要决定无论结果如何都发表；只发表某一类结果，会让论证显得比实际更好[^feynman1974cargo-e9]。不报告不显著或"没意思"的结果，叫报告偏差，会严重高估效应[^menzies2019bad-e1]。软件工程的实证研究标准明确写道：因为研究报告了负面结果就否定它，是不成立的审稿意见[^ralph2020empirical-e41]。

> **不同的看法：负面结果要不要单独写成论文？**
>
> - 《欧洲科研诚信行为准则》认为，负面结果在发表和传播上，可以和正面结果同样重要[^allea2023european-e12]。
> - 一位计算机研究者在谈研究方法的文章里说，他比多数人更不赞成发表负面结果，除非它附带了对失败原因的洞见[^steinhardt2018stochastic-e11]。
>
> 实际操作 `[本项目分析]`：两种看法不冲突的地方是，**论文里不能隐瞒**和主张相关的负面结果。要不要把一个负面结果单独写成论文，取决于你能不能说清它为什么失败；说得清，它就是一条有价值的主张，例如"在训练截止后的合约上，现有方法的优势消失了"。

**意外结果。** 先按第 1 节查一遍，排除出错。查过之后它还在，就认真对待。政治学过程追踪方法的标准写道：要重视"意外"的感觉，并努力解释意外的事实[^bennett2012process-e43]。意外的结果可能指向一个比原计划更有意思的问题 `[本项目分析]`。但它是看到数据之后才发现的，按第 2 节标成探索性，最好再用一批新数据验证一次 `[本项目分析]`。

**写下来：** 列出所有和预期不符的结果。每一个写：查过是不是出错了吗？可能的原因是什么？打算怎么报告？

## 6. 结论能说到多远

**结论的强度要和证据对上。** 主张要能从你给出的证据中清楚地推出，证据撑不住的主张会误导读者[^blackburn2018sigplan-e2]。

最常见的是说过头。机器学习的方法指南提醒：一个数据集上效果很好，不代表在别的数据集上也好[^lones2021avoid-e10]。软件工程的实证研究标准把"结论或推广超出证据"和"淡化局限"都列为反面做法；还有一种更隐蔽的：写了局限，结论和意义却写得好像局限不存在[^ralph2020empirical-e66]。

可以用下面的表，把结论的说法和证据对齐 `[本项目分析]`：

| 你手里的证据 | 可以说 | 不能说 |
|---|---|---|
| 一个评测集、一个模型 | "在评测集 D 上，用模型 M 时……" | "大模型能……" |
| 只有相关，没有对照实验 | "用了提示的审计，检出率更高" | "提示提高了检出率" |
| 几个成功的例子 | "能发现静态分析工具漏掉的漏洞" | "比静态分析工具更好" |
| 平均提升，但各类漏洞差别很大 | "平均提升 X，主要来自某一类漏洞" | "全面提升 X" |

主张说法的强弱和需要的证据，在[收敛成项目](../01_from-interest-to-project/03_converge.md#1-写出你想证明的那句话)第 1 节讲过；到了这一步，是拿着真实的证据回头核对。

**把结果和推测分开。** 前面那篇机器学习的批评文章指出，论文常把推测包装成解释，读者因为它出现在论文里、出自专家之手，就当成定论[^lipton2019troubling-e2]。结果越好，越容易觉得可以随意加一些没有证据的解释[^lipton2019troubling-e15]。好的做法是把推测放进单独标明的一节[^lipton2019troubling-e3]，写作时用"结果显示……"和"我们推测……"明确区分 `[本项目分析]`。

**写出不利的事实和真正的局限。** 提出一个解释时，要把与它不符的事实也一起写出来[^feynman1974cargo-e4]。不写局限，或只写无关紧要的、漏掉真正相关的，会让读者得出过强的结论[^blackburn2018sigplan-e3]。还要小心"每句都对，整体误导"：每句话都属实，传达的暗示却可能是假的[^feynman1974cargo-e6]。目标是给出让别人能判断你工作价值的全部信息，而不只是引向某个方向的信息[^feynman1974cargo-e5]。

**写下来：** 画一张两列的表：左边列出每一条结论，右边写支撑它的具体表格、图或实验。右边空着的，要么补证据，要么把结论改弱。

## 7. 证据和主张对不上时，改主张

**证据不支持原来的主张时，改的是主张，不是证据。**

常见的几种情况和改法 `[本项目分析]`：

| 情况 | 改法 |
|---|---|
| 效果只在部分条件下成立 | 收窄主张：限定数据、对象、漏洞类型 |
| 效果比预期小很多 | 如实报告大小，重新判断还值不值得写；也许它更适合作为次要主张 |
| 效果来自你没想到的原因 | 主张换成这个原因，按第 2 节标成探索性，再设计验证 |
| 原来的主张被否定了 | 负面结果本身可能就是主张；或者回到收敛阶段换一个 |

在整理和提炼结论时发现事情比想象复杂，要退回去重新理解、甚至重新探索，这很正常，并不说明你搞砸了[^nanda2025process-e6]。

**底线在哪：** 改主张、补实验、收窄范围，都是正常的研究过程。但为了保住原来的主张而悄悄删掉不利的数据或结果，就越过了红线：无正当理由地改动、删除或隐瞒数据和结果，属于篡改[^allea2023european-e3]。什么算学术不端、发现自己的错误后怎么更正，见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)。

**每次改主张，都记下来**：原来的主张、新的主张、促使你改的证据。这份记录在写论文和回复审稿意见时都用得上 `[本项目分析]`。记录的方法见[整理材料](../08_throughout/organizing_materials.md)。

**写下来：** 拿出你的一页项目简介（见[收敛成项目](../01_from-interest-to-project/03_converge.md#6-写成一页项目简介并反复修改)），对照现在的证据，把"核心结论"那一栏重写一遍。和原来一样也没关系，但要能指出支撑它的证据。

---

## 关键判断

**这个结果能信吗？** 可以这样判断 `[本项目分析]`：

| 遇到的情况 | 通常的做法 |
|---|---|
| 结果好得出乎意料 | 先按第 1 节查错，再查"模型见过"、数据重复这类问题 |
| 计划内的分析不显著，换个分析就显著了 | 两个都报告，后一个标成探索性；不要只报后一个 |
| 显著，但差异很小 | 对照事先定的"多大才算有意义"，如实说明实际意义有限 |
| 不显著，置信区间很宽 | 说"这次的数据分辨不出来"，不要说"没有差异" |
| 一个其他解释查不了 | 写进局限，并相应收窄结论 |
| 核心主张被证据否定 | 先查是不是出错；确认无误后，改主张，见第 7 节 |

**什么时候算分析完了？** 不是"再也想不出新的分析"，而是：计划内的分析都做完并记下结果；每条结论都能指出证据；主要的其他解释都查过或写进了局限；主张已经按证据改过 `[本项目分析]`。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 不看原始数据，直接看汇总数字 | 很多错误是静默的，结果看上去照样能用[^karpathy2019recipe-e3] |
| 结果好时不查，结果差时才查 | 只往一个方向找错，结果会被拉向预期 `[本项目分析]` |
| 一个个试分析方法，只报显著的那个 | 心理学的模拟里，假阳性率从 5% 升到 61%[^nelson2018psychology-e7] |
| 看到结果后提假设，写得像事先就有 | 公认的反面做法[^ralph2020empirical-e27] |
| 计划外的分析不加说明 | 读者分不清哪些是预测、哪些是事后解释[^nosek2018preregistration-e4] |
| 只报 p 值 | 样本大时微不足道的差异也会显著[^lones2021avoid-e8] |
| 只报最好的一次运行 | 差异可能只是随机波动[^georges2007statistically-e2] |
| 把"不显著"写成"没有差异" | 可能只是数据不够，分辨不出来 `[本项目分析]` |
| 只报告"有意思"的结果 | 报告偏差会严重高估效应[^menzies2019bad-e1] |
| 一次失败就说"这个思路不行" | 只说明这一种做法不行[^steinhardt2018stochastic-e10] |
| 把推测写成解释 | 读者会当成定论[^lipton2019troubling-e2] |
| 承认了局限，结论却照旧 | 局限形同虚设[^ralph2020empirical-e66] |
| 为保住主张悄悄删掉不利的结果 | 属于篡改[^allea2023european-e3] |

## 产出物

- 数据检查记录：查了什么、发现了什么、删了什么、为什么删（第 1 节）
- 分析清单：每项分析是计划内还是探索性，结果如何（第 2 节）
- 核心结果的陈述：条件、效应量、不确定性、重复次数（第 3 节）
- 其他解释清单，以及每个的排查结果（第 4 节）
- 结论与证据对照表（第 6 节）
- 更新后的一页项目简介，以及主张的修改记录（第 7 节）

## 检查点

满足下面几条，可以进入写作：

- [ ] 亲自看过原始数据和输出，查过离群值、重复和解析错误
- [ ] 结果好的部分和不好的部分，用同样的力度查过
- [ ] 计划内的分析全部报告了结果；计划外的都标成了探索性，并写了为什么加
- [ ] 每个关键结果都有效应量和不确定性，而不只是 p 值
- [ ] 报告了全部运行，说明了一共做了多少次比较
- [ ] 列出并检查了主要的其他解释；查不了的写进了局限
- [ ] 负面结果和意外结果都查过原因，并打算如实报告
- [ ] 每条结论都能指出证据，说法的强弱和证据对得上
- [ ] 一页项目简介里的核心结论已按证据更新

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 数据检查发现大问题，结果要重跑 | [执行与迭代](01_run-and-iterate.md) |
| 现有的数据根本回答不了研究问题 | [从研究问题到证据清单](../02_from-project-to-study/01_question-to-evidence.md)，重新想需要什么证据 |
| 有一个致命的其他解释，现有设计排除不了 | [效度与局限](../02_from-project-to-study/03_validity-and-limits.md)，补设计 |
| 核心主张被否定，改小之后也没什么意思了 | [收敛成项目](../01_from-interest-to-project/03_converge.md)，换一个候选结论 |
| 探索中发现了一个更有意思的问题 | [收敛成项目](../01_from-interest-to-project/03_converge.md)，把它当成新的候选，和导师商量 |

## 下一步

结论和证据对齐之后，下一步是把它们讲成一个故事，写成论文：先讲什么、证据怎么排、局限放在哪里。见[讲清故事，写成论文](../04_write-and-publish/01_story-and-paper.md)。

[^allea2023european-e3]: ALLEA 2023，§3.1 Research Misconduct。[证据](../../sources/notes/allea2023european.md#e3)
[^allea2023european-e12]: ALLEA 2023，§2.7。[证据](../../sources/notes/allea2023european.md#e12)
[^aera2006standards-e8]: 美国教育研究协会 2006，5.10。[证据](../../sources/notes/aera2006standards.md#e8)
[^aera2006standards-e9]: 美国教育研究协会 2006，5.10。[证据](../../sources/notes/aera2006standards.md#e9)
[^appelbaum2018journal-e1]: Appelbaum 等人 2018，摘要，第 3 页。[证据](../../sources/notes/appelbaum2018journal.md#e1)
[^bennett2012process-e43]: Bennett & Checkel 2012，标准 8，第 34 页。[证据](../../sources/notes/bennett2012process.md#e43)
[^blackburn2018sigplan-e2]: SIGPLAN 清单 2018，Clearly Stated Claims。[证据](../../sources/notes/blackburn2018sigplan.md#e2)
[^blackburn2018sigplan-e3]: SIGPLAN 清单 2018，Fails to acknowledge limitations。[证据](../../sources/notes/blackburn2018sigplan.md#e3)
[^blackburn2018sigplan-e7]: SIGPLAN 清单 2018，Insufficient number of trials。[证据](../../sources/notes/blackburn2018sigplan.md#e7)
[^blackburn2018sigplan-e9]: SIGPLAN 清单 2018，Misleading summary of results。[证据](../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e13]: SIGPLAN 清单 2018，Indirect or inappropriate proxy metric。[证据](../../sources/notes/blackburn2018sigplan.md#e13)
[^blackburn2018sigplan-e30]: SIGPLAN 清单 2018，Inappropriate level of precision。[证据](../../sources/notes/blackburn2018sigplan.md#e30)
[^egappreanalysis-e5]: EGAP 方法指南，§9 Why make a PAP?。[证据](../../sources/notes/egappreanalysis.md#e5)
[^feynman1974cargo-e4]: Feynman 1974，演讲正文，科学诚信一段。[证据](../../sources/notes/feynman1974cargo.md#e4)
[^feynman1974cargo-e5]: Feynman 1974，演讲正文。[证据](../../sources/notes/feynman1974cargo.md#e5)
[^feynman1974cargo-e6]: Feynman 1974，Wesson Oil 的例子。[证据](../../sources/notes/feynman1974cargo.md#e6)
[^feynman1974cargo-e7]: Feynman 1974，演讲正文。[证据](../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e9]: Feynman 1974，演讲正文。[证据](../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e11]: Feynman 1974，演讲正文，科学诚信一段。[证据](../../sources/notes/feynman1974cargo.md#e11)
[^feynman1974cargo-e14]: Feynman 1974，演讲正文，Millikan 的例子。[证据](../../sources/notes/feynman1974cargo.md#e14)
[^georges2007statistically-e2]: Georges 等人 2007，§1，Figure 1 讨论。[证据](../../sources/notes/georges2007statistically.md#e2)
[^herzig2013bug-e5]: Herzig 等人 2013，§XII。[证据](../../sources/notes/herzig2013bug.md#e5)
[^hopewell2025consortee-e18]: CONSORT 2025 解释文章，Item 16a。[证据](../../sources/notes/hopewell2025consortee.md#e18)
[^hopewell2025consortee-e49]: CONSORT 2025 解释文章，Item 21d。[证据](../../sources/notes/hopewell2025consortee.md#e49)
[^hopewell2025consortee-e52]: CONSORT 2025 解释文章，Item 26。[证据](../../sources/notes/hopewell2025consortee.md#e52)
[^huang2023unstuck-e5]: Jia-Bin Huang 2023，推文串，Debug the idea。[证据](../../sources/notes/huang2023unstuck.md#e5)
[^kalibera2013rigorous-e8]: Kalibera & Jones 2013，§4。[证据](../../sources/notes/kalibera2013rigorous.md#e8)
[^karpathy2019recipe-e3]: Karpathy 2019，"Neural net training fails silently"。[证据](../../sources/notes/karpathy2019recipe.md#e3)
[^karpathy2019recipe-e7]: Karpathy 2019，第 1 步 Become one with the data。[证据](../../sources/notes/karpathy2019recipe.md#e7)
[^kraft2019interpreting-e13]: Kraft 2019，第 17 页（准则 4）。[证据](../../sources/notes/kraft2019interpreting.md#e13)
[^kraft2019interpreting-e21]: Kraft 2019，第 26 页（结论）。[证据](../../sources/notes/kraft2019interpreting.md#e21)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019，§1，第 1 页。[证据](../../sources/notes/lipton2019troubling.md#e1)
[^lipton2019troubling-e2]: Lipton & Steinhardt 2019，§3.1，第 2 页。[证据](../../sources/notes/lipton2019troubling.md#e2)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019，§3.1，第 3 页。[证据](../../sources/notes/lipton2019troubling.md#e3)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../sources/notes/lipton2019troubling.md#e7)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../sources/notes/lipton2019troubling.md#e8)
[^lipton2019troubling-e15]: Lipton & Steinhardt 2019，§4.1。[证据](../../sources/notes/lipton2019troubling.md#e15)
[^lones2021avoid-e7]: Lones 2021，§5.4，第 22 页。[证据](../../sources/notes/lones2021avoid.md#e7)
[^lones2021avoid-e8]: Lones 2021，§6.4，第 25 页。[证据](../../sources/notes/lones2021avoid.md#e8)
[^lones2021avoid-e10]: Lones 2021，§6.3，第 24 页。[证据](../../sources/notes/lones2021avoid.md#e10)
[^lones2021avoid-e12]: Lones 2021，§5.4，第 22 页。[证据](../../sources/notes/lones2021avoid.md#e12)
[^lones2021avoid-e19]: Lones 2021，§2.2。[证据](../../sources/notes/lones2021avoid.md#e19)
[^lones2021avoid-e20]: Lones 2021，§2.4。[证据](../../sources/notes/lones2021avoid.md#e20)
[^menzies2019bad-e1]: Menzies & Shepperd 2019，§4.4。[证据](../../sources/notes/menzies2019bad.md#e1)
[^menzies2019bad-e2]: Menzies & Shepperd 2019，§4.6。[证据](../../sources/notes/menzies2019bad.md#e2)
[^menzies2019bad-e3]: Menzies & Shepperd 2019，§4.6。[证据](../../sources/notes/menzies2019bad.md#e3)
[^nanda2025process-e6]: Nanda 2025，Distillation (Stage 4): Compress, Refine, Communicate。[证据](../../sources/notes/nanda2025process.md#e6)
[^nelson2018psychology-e6]: Nelson 等人 2018，P-Hacking Explains an Old Paradox，第 514 页。[证据](../../sources/notes/nelson2018psychology.md#e6)
[^nelson2018psychology-e7]: Nelson 等人 2018，P-Hacking Explains an Old Paradox，第 516 页。[证据](../../sources/notes/nelson2018psychology.md#e7)
[^nelson2018psychology-e8]: Nelson 等人 2018，False Positives Are Bad，第 518 页。[证据](../../sources/notes/nelson2018psychology.md#e8)
[^nosek2018preregistration-e2]: Nosek 等人 2018，Mental Constraints on Distinguishing Predictions and Postdictions。[证据](../../sources/notes/nosek2018preregistration.md#e2)
[^nosek2018preregistration-e3]: Nosek 等人 2018，Mental Constraints on Distinguishing Predictions and Postdictions。[证据](../../sources/notes/nosek2018preregistration.md#e3)
[^nosek2018preregistration-e4]: Nosek 等人 2018，Preregistration Distinguishes Prediction and Postdiction。[证据](../../sources/notes/nosek2018preregistration.md#e4)
[^nosek2018preregistration-e5]: Nosek 等人 2018，Challenge 1。[证据](../../sources/notes/nosek2018preregistration.md#e5)
[^nosek2018preregistration-e6]: Nosek 等人 2018，Challenge 6。[证据](../../sources/notes/nosek2018preregistration.md#e6)
[^ofosu2023preanalysis-e1]: Ofosu & Posner 2023，摘要。[证据](../../sources/notes/ofosu2023preanalysis.md#e1)
[^ofosu2023preanalysis-e7]: Ofosu & Posner 2023，Do PAPs Reduce the Scope for Fishing?。[证据](../../sources/notes/ofosu2023preanalysis.md#e7)
[^ofosu2023preanalysis-e9]: Ofosu & Posner 2023，Do PAPs Reduce the Scope for Post-Hoc Hypothesis Adjustment?。[证据](../../sources/notes/ofosu2023preanalysis.md#e9)
[^ofosu2023preanalysis-e10]: Ofosu & Posner 2023，Do PAPs Reduce the Scope for Post-Hoc Hypothesis Adjustment?。[证据](../../sources/notes/ofosu2023preanalysis.md#e10)
[^ofosu2023preanalysis-e14]: Ofosu & Posner 2023，Objections to PAPs: Limit Flexibility and Scope for New Discoveries。[证据](../../sources/notes/ofosu2023preanalysis.md#e14)
[^ralph2020empirical-e27]: ACM SIGSOFT 实证研究标准，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e41]: ACM SIGSOFT 实证研究标准，General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e66]: ACM SIGSOFT 实证研究标准，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e199]: ACM SIGSOFT 实证研究标准，Data Science 标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e199)
[^steinhardt2018stochastic-e9]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e9)
[^steinhardt2018stochastic-e10]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e11]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e11)
[^zeller2021devil-e1]: Zeller 2021，THE CHERRY SHUFFLE。[证据](../../sources/notes/zeller2021devil.md#e1)
