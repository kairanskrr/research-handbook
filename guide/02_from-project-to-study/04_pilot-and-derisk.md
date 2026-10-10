# 先做小规模试验，排除最大风险

> 本章的道理适用于各学科，例子和具体做法以计算机为例。

## 你现在在哪里

你的研究设计基本定了：知道要证明哪条主张、需要什么证据（见[从研究问题到证据清单](01_question-to-evidence.md)），选好了研究套路和研究方法（见[选定研究套路和方法](02_choose-strategy-and-method.md)），也想过结论可能在哪里站不住（见[效度与局限](03_validity-and-limits.md)）。

在[收敛成项目](../01_from-interest-to-project/03_converge.md#5-你做得出来吗)时，你已经用一个小实验试过项目里最没把握的部分，那次试验回答的是"这个项目值不值得做、做不做得出来"。在[研究计划](../01_from-interest-to-project/04_research-plan.md#4-排顺序最可能失败的先做)里，你也把最可能失败的里程碑排在了最前面。

现在的问题更具体：**这份设计一旦铺开，要花几周甚至几个月。在投入之前，怎样确认它真的能按设计跑下来？**

## 这一阶段要解决什么

在正式执行之前，用小规模的试验回答下面五个问题：

1. 这份设计依赖哪些假设？哪几个一旦不成立，整个研究就白做？
2. 对每个危险的假设，有没有一个便宜的办法先查清？
3. 从输入数据到填好结果表，整条流程能不能从头到尾跑通？
4. 研究要用到参与者、标注员、问卷或评分规则的，它们在实际条件下能不能用？
5. 试完以后，按什么标准决定：照原计划继续、修改后继续，还是停下来？

本章说的"小规模试验"，包括两类做法：一类是给设计里的各个部分**去风险**，即为每个部分找一个便宜的办法，有把握地判断它行不行[^steinhardt2018stochastic-e5]；另一类是**预实验**（pilot，也叫预研究），即正式研究之前的一次小规模试运行，用来找出会干扰结果的额外因素[^ko2015practical-e31]，以及实验里需要修正的问题[^ko2015practical-e32]。两者的目标相同：先评估可行性，避免贸然开始一项大研究而带来灾难性的后果[^thabane2010tutorial-e1]。

本章关于预实验的很多做法来自临床研究的预实验教程，也参考了软件工程、机器学习研究者的经验。道理可以通用，具体的数字和程序要按你所在学科的规矩来 `[本项目分析]`。

---

## 1. 列出设计依赖的假设，找出最危险的几个

**先把设计里"默认成立"的东西都写出来。** 写设计时，你脑子里有很多没说出口的前提：数据是干净的、工具跑得起来、标注规则大家理解一致、效果大到能被测出来、预算够用。这些前提任何一个不成立，后面的工作都可能白做。

可以按四类去找。临床研究的预实验教程把做预实验的理由归为流程、资源、管理和科学四类：流程看正式研究的各个步骤能不能走通，资源看时间和经费会不会出问题[^thabane2010tutorial-e2]。这个分法放到别的学科也好用。下表"要问的"一列和例子是换成计算机项目的说法 `[本项目分析]`：

| 类别 | 要问的 | 例子："评测被数据泄露高估"这个项目 |
|---|---|---|
| 流程 | 每一步能不能按设计走通 | 能不能拿到各个模型的训练数据线索？合约能不能批量编译、批量送进模型？ |
| 资源 | 时间和经费够不够 | 跑完全部合约要调用多少次接口、花多少钱、等多久？ |
| 管理 | 人和数据会不会出问题 | 两个人分头标注，结果怎么合并？中间数据存在哪里，版本怎么管？ |
| 科学 | 设计的核心判断站不站得住 | 判断"是否泄露"的方法准不准？去掉泄露前后的差别，大到能看出来吗？ |

**然后给每个假设打三个分** `[本项目分析]`：

- **如果它不成立，有多糟？** 是改一个参数就行，还是整个研究不成立？
- **你有多大把握它成立？** 有现成证据，还是只是"应该没问题"？
- **查清它要花多少力气？** 一个下午，还是两周？

排在最前面的，是"不成立就全盘皆输、把握最小、查起来又不贵"的那几个，道理和[研究计划里给里程碑排序](../01_from-interest-to-project/04_research-plan.md#4-排顺序最可能失败的先做)一样。

对每个关键假设，问自己一句：**"如果这个方向注定不行，怎样最快发现？"**[^nanda2025mindsets-e12]

**写下来：** 列出你的设计依赖的所有假设，至少十条，按流程、资源、管理、科学分组。给每条打上"不成立有多糟 / 把握多大 / 查清多贵"三个分，圈出最危险的三个。

## 2. 给每个危险的假设，找一个便宜的检验

圈出最危险的假设后，**不要直接开始正式执行，先给它们逐个去风险。** 基本做法是：能去风险的部分都先去风险，然后再执行[^steinhardt2018stochastic-e5]。

**便宜的检验长什么样？** 下面几种形式来自一位机器学习研究者的经验，换到别的方向也能借鉴：

| 担心的是 | 便宜的检验 |
|---|---|
| 数据不合用 | 先取一小部分，手工看一些、算一些统计量，看它有没有你需要的性质，再花大力气准备全部数据[^steinhardt2018stochastic-e6] |
| 想证明的结论其实不成立 | 动手证明之前，先跑模拟，看它是不是真的成立[^steinhardt2018stochastic-e18] |
| 方法好坏的空间有多大 | 测一个"上限"：把难做的部分先换成"作弊"版本，比如偷看测试集；再测一个简单基线作为下限。两者划出结果可能落在的范围，帮助解读核心结果[^steinhardt2018stochastic-e24][^steinhardt2018stochastic-e7] |
| 复杂方法不如简单方法 | 先跑简单或现成的方法；复杂方法常常还不如简单基线[^steinhardt2018stochastic-e7] |

在[收敛成项目](../01_from-interest-to-project/03_converge.md#5-你做得出来吗)时手工核对 50 个样本看泄露判断准不准，就是这样一个便宜的检验。现在把同样的做法用到设计里其他危险的假设上。以"评测被数据泄露高估"为例 `[本项目分析]`：

- **差别大不大**：先测"上限"——如果把明确泄露的样本全部去掉，准确率最多能掉多少？掉得很少，这个主张就不值得花几个月去证明。
- **费用够不够**：先跑 20 个合约，记下调用次数、花费和时间，再乘上全部合约数。

**检验之前，先写下你预期看到什么。** 训练神经网络的一份经验总结建议：每一步都先对结果做具体的预测，再用实验验证；不符合预测，就一直查到找出问题为止[^karpathy2019recipe-e1]。这个习惯在别的研究里同样有用：不写预测，你很容易把任何结果都解释成"差不多符合预期" `[本项目分析]`。

**去风险不等于只做稳妥的东西，** 也不等于回避那些还没有明显可行路线的项目[^steinhardt2018stochastic-e13]。尽早排除不行的路，正是为了腾出时间去试成功率不高、但做成了很有价值的想法 `[本项目分析]`。

**写下来：** 为圈出的三个危险假设，各写一个检验：做什么、用多少数据、花多少时间、你预期看到什么结果。每个检验最好在一周内能做完。

## 3. 先搭一个从头到尾能跑通的最小版本

单个部分都查过了，还不够。很多问题只在各部分**接起来**的时候才出现：上一步的输出格式和下一步对不上，某一步悄悄丢了一半数据，评测脚本算的不是你以为的那个指标。

**做法：在铺开之前，先用最小的规模，把整条流程从头到尾跑一遍。** 训练神经网络的经验总结里有一条建议：在用复杂模型之前，先搭起从训练到评测的完整骨架，通过一系列实验确认它是对的；这时选一个简单到不可能出错的模型[^karpathy2019recipe-e8]。

以计算机项目为例，"最小版本"可以是这样的 `[本项目分析]`：

1. **数据只取一小份。** 比如 20 个合约，挑几个你手工知道答案的。
2. **方法用最简单的版本。** 比如只用一种提示词、一个模型。
3. **每一步都接上。** 读数据 → 送进模型 → 解析输出 → 判断对错 → 算指标 → 填进结果表。
4. **把结果表真的填出来。** 拿出[收敛成项目](../01_from-interest-to-project/03_converge.md#4-拿什么让人相信)时画的空结果表，用这 20 个合约的结果填一遍。数字本身不重要，重要的是每一格都知道从哪里来。

**跑通的标准是什么？** 可以借用神经网络训练里的标准：整条流程能工作；对任何一个方法，都能可重复地算出一个你信得过的指标；手里还有几个简单基线的成绩，作为新方法必须超过的底线[^karpathy2019recipe-e9]。

**几个让最小版本真正起作用的检查**（同样来自神经网络训练的经验，例子换成了计算机项目）：

- **程序不报错，不等于做对了。** 训练神经网络时，很多错误是静默的：语法都对，整体却没有按正确的方式组织起来，而且很难看出来[^karpathy2019recipe-e3]。手工抽查几条中间结果 `[本项目分析]`。
- **做一个"不该有效"的基线。** 比如把输入全部置零，它的成绩应当比用真实输入差[^karpathy2019recipe-e5]。如果差不多，说明你的方法并没有从数据里学到东西。换到漏洞检测里，可以把合约代码打乱或换成无关代码，看模型的"检出率"会不会照样很高 `[本项目分析]`。
- **一次只加一样东西。** 尽力避免一次引入大量没验证过的复杂度[^karpathy2019recipe-e2]；要加入多个新东西时，一个一个加，每次确认得到了预期的提升[^karpathy2019recipe-e6]。

**这个道理不限于写代码。** 教育领域的设计研究也主张：不要把整套方案做完，才在最后发现它不管用；应当快速做粗糙的原型、检验、再修改[^easterday2014design-e12]。项目早期，只收集足以快速淘汰失败方案、找出有希望方案的最少数据[^easterday2014design-e14]。

**写下来：** 画出你的研究从原始数据到结果表的每一步，标出每一步的输入和输出。用最小规模跑通一遍，把空结果表填上一行，并记下跑的过程中发现的每一个问题。

## 4. 涉及人、数据和工具时：做预实验

> **适用范围：** 本节主要针对需要参与者、人工标注、问卷、访谈或筛选规则的研究。纯计算的项目，第 3 节的最小版本往往就是你的预实验 `[本项目分析]`。

研究里一旦有人参与，问题就多了：参与者看不懂任务说明，问卷题目有歧义，一次实验的时长远超预期，两个标注员对同一个合约的判断不一样。这些问题，光靠读设计是看不出来的。

**预实验是准备实验的关键一步**：正式实验之前的试运行，目的是找出会干扰结果的额外因素[^ko2015practical-e31]。在软件工程研究里，预实验可能还不是标准做法[^ko2015practical-e31]。所以别人的论文里没写，不代表你可以不做 `[本项目分析]`。

**由近到远，分几轮试。** 访谈提纲的预试有团队内部试、请专家评、实地试三种做法[^kallio2016systematic-e5]，内部试能帮你去掉含糊和诱导性的问题[^kallio2016systematic-e6]。在这之前，研究者还可以自己当参与者预演一遍[^ko2015practical-e33]。其他涉及人的研究，可以照下表安排 `[本项目分析]`：

| 轮次 | 谁来试 | 能发现什么 |
|---|---|---|
| 自己试 | 研究者自己当参与者，走一遍完整流程 | 明显的流程漏洞、时长、材料缺失 |
| 团队内部试 | 课题组里的其他人 | 含糊的问题、带诱导性的问题 |
| 请专家看 | 懂这个领域或这种方法的外部专家 | 问题有没有问到点上、遗漏了什么 |
| 实地试 | 和正式参与者同类的少数人 | 真实条件下的理解、时长、配合程度 |

最重要的一轮，是**尽量按正式研究的样子来试**：尽量用同类的参与者、同样的场地、同样的材料、说明、问卷、流程和实验人员[^ko2015practical-e32]。临床研究还要求预实验的参与者能代表目标人群，用和正式研究相同的纳入和排除标准[^thabane2010tutorial-e9]；别的学科照这个思路做也不会错 `[本项目分析]`。

**不同的研究方法，试的重点不同：**

- **问卷**：设计好后要检验它能不能测到想测的东西，资料里最常提到的办法是预调查、重测、焦点小组、专家或非专家评审[^molleri2020empirically-e2]。预调查之后和参与者聊一聊，确认题目被轻松、正确地理解了[^wagner2020challenges-e24]。具体做法见[问卷调查](../06_methods/questionnaire_survey.md)。
- **访谈**：先在团队内部试访谈提纲，去掉含糊和带诱导性的问题[^kallio2016systematic-e6]。见[访谈研究](../06_methods/interview_study.md)。
- **对照实验**：先自己当参与者走一遍，再找少数同类参与者按正式流程试[^ko2015practical-e33][^ko2015practical-e32]。见[对照实验](../06_methods/controlled_experiment.md)。
- **文献综述**：筛选标准定好后，先在一小批论文上试用[^kitchenham2007guidelines-e8]。见[综述研究](../06_methods/review_study.md)。
- **人工标注**：两个人各自标同一小批样本，对比分歧，把分歧大的地方写进标注规则，再试一轮 `[本项目分析]`。

**预实验也要对参与者说清楚。** 临床研究的做法是专门写一段说明：告诉参与者这是预研究、这次要评估哪些可行性、什么结果算可行[^thabane2010tutorial-e12]。**预实验也可能要过伦理审查。** 只举加拿大一国的例子：加拿大三大联邦研究资助机构联合发布的《三理事会政策声明》（TCPS 2，2022 年版）把预研究界定为正式研究的缩小版（参与者更少、时间更短），规定它和正式研究一样，必须在招募参与者、收集数据之前交研究伦理委员会审查[^tcps2022ethical-e1][^tcps2022ethical-e3]；只为建立合作关系或设计方案做的初步探索不用审查[^tcps2022ethical-e3]。审查松紧按参与者面临的风险来定，风险越低，审查越简化[^tcps2022ethical-e4][^tcps2022ethical-e5]。按这个界定，上表里最接近预研究的是"实地试"那一轮；前几轮内部试算不算，这份政策没有逐一说明 `[本项目分析]`。其他国家和机构怎么规定，本文资料未涉及；动手前先问导师或所在机构的伦理委员会。

**写下来：** 写出你的预实验计划：分几轮、每轮找谁、几个人、用哪些材料、重点看什么问题。最后一轮要写清楚它和正式研究在哪些地方一样、哪些地方不一样。

## 5. 事先写好：什么结果算继续、调整、停

**在试之前，就写下判断标准。** 预实验一定要写明成功标准，而且要根据主要的可行性目标来定[^thabane2010tutorial-e3]。试完再定标准，你会不自觉地把标准挪到结果附近 `[本项目分析]`。

临床研究的教程把预实验的结果分成四种[^thabane2010tutorial-e3]：

1. **停止**：正式研究不可行；
2. **修改方案后继续**：改了之后可行；
3. **不改方案，但密切监控着继续**；
4. **照原方案继续**。

**标准要写成具体的数字或可检查的条件。** 医学里的例子：一项多中心临床试验的预实验，事先规定至少招到 70% 的合格患者、至少 95% 的受试者完成随访[^thabane2010tutorial-e4]。以计算机项目为例，可以这样写 `[本项目分析]`：

| 要试的 | 继续 | 修改后继续 | 停 |
|---|---|---|---|
| 泄露判断方法 | 50 个手工核对的样本中，判断一致的不少于 45 个 | 一致率不够，但分歧集中在某一类合约，可以改规则 | 分歧没有规律，想不出改进办法 |
| 泄露的影响有多大 | 上限测试中，准确率下降明显 | 只在部分模型上明显，主张需要收窄 | 去掉所有泄露样本后几乎没有变化 |
| 费用和时间 | 估算的总花费在预算内 | 超出预算，但减少模型数量后能承受 | 怎么削减都远超预算 |
| 标注一致性 | 两人分歧很少 | 分歧集中在规则没写清的地方 | 改了两轮规则，分歧仍然很大 |

上面的阈值只是示例，要按你的项目和导师商量着定。

**"停"不是失败。** 预实验显示正式研究不太可行，恰恰是它成功了：它让你没有把有限的资源浪费在注定失败的研究上[^thabane2010tutorial-e8]。

**但也不要轻易判"停"。** 一次试验失败，说明的只是这个思路的一种具体实现不行，不是整个思路不行[^steinhardt2018stochastic-e10]。"看起来不行""试了几次没劲头了"都不算真正排除了它[^steinhardt2018stochastic-e22]。判断前先分清 `[本项目分析]`：

- **是设计的某个细节出了问题**（题目有歧义、提示词写得不好、脚本有错）→ 修改后再试；
- **是设计依赖的核心假设不成立**（泄露对结果几乎没有影响、需要的数据根本拿不到）→ 回到主张，考虑收窄或换角度。

**写下来：** 为第 1 节圈出的每个危险假设，写一行"继续 / 修改后继续 / 停"的标准，每一格都要能用试验结果直接检查。试之前把这张表发给导师。

## 6. 别从试验数据里读出太多

试验结果出来了，看起来很有希望。这时最容易犯的错，是**把预实验当成小号的正式研究**。

**预实验回答的是"能不能做"，不是"效果有多大"。** 常见的错误是把重点放在统计显著性上，而不是可行性上[^thabane2010tutorial-e6]。具体来说：

- **不要用预实验估计效果大小。** 这一点临床、心理学和动物实验的资料都提到过。样本少，估出的效果可能不现实、有偏[^thabane2010tutorial-e5]。小样本预实验的效应量很不精确，不能拿来给正式研究算样本量[^lakens2022sample-e4]。只靠预实验，也很难得到够用的波动数据；以往研究和系统综述是更合适的来源[^perciedusert2020reporting-e36]。效应量、样本量的含义，见[分析与解读](../03_conduct-and-analyze/02_analyze-and-interpret.md)。
- **没有显著结果，不等于没有效果。** 样本不足的研究没有显著结果，只能说"没有定论"，不能说"没有效果"[^thabane2010tutorial-e7]。
- **结果很好，也不要急着写进论文的主要结论。** 预实验的设计往往还在改，规模也小，它支撑不了核心主张 `[本项目分析]`。确实要报告的，可以参考一家药理学期刊的作者指南：放在方法部分单独的"预实验"小节里，不给 P 值[^curtis2018experimental-e11]。

**预实验的数据，正式研究能不能用？** 这里资料有不同的看法，会影响你怎么做。

> **不同的看法：预实验数据丢掉，还是并入正式研究？**
> - **丢掉。** 软件工程里针对有人参与的工具实验的指南说：预实验收集的数据都应丢弃，因为预实验的目的是找出实验里要修正的问题，不是收集数据[^ko2015practical-e32]。
> - **可以合并，但要事先计划。** 临床预实验的教程没有一概排除合并，而是要求：如果考虑合并预实验和正式研究的数据，必须事先计划好，在研究方案里写清楚，并讨论清楚统计上的后果和方法[^thabane2010tutorial-e10]。
>
> 实际操作中可以这样处理 `[本项目分析]`：**默认丢掉。** 只有在试之前就写明"这批数据会并入正式研究"、并且试完之后没有改过设计时，才考虑合并。看过预实验结果再改设计，改过之后的正式研究就要用新数据。

**写下来：** 试完后写一段总结，只回答三件事：每个可行性标准达到了没有、设计要改哪些地方、下一步是继续、修改还是停。不写"效果提升了多少"。

---

## 关键判断

**试到什么程度就够了？** 不是"再也找不到问题"，而是第 1 节圈出的危险假设都有了答案，整条流程跑通过一遍，涉及人的部分在接近正式条件下试过 `[本项目分析]`。临床预实验教程给的经验法则是：预实验的规模，要大到能为你要评估的那几项可行性提供有用信息[^thabane2010tutorial-e9]。

**试出问题后怎么办？** 可以这样判断 `[本项目分析]`：

| 试出的情况 | 通常的做法 |
|---|---|
| 细节问题：材料有歧义、脚本有错、流程漏了一步 | 修改后，把改过的部分再试一小轮 |
| 资源问题：时间或费用超出很多 | 缩小规模，或者和导师商量换一种更便宜的证据 |
| 测量问题：判断方法或标注规则不可靠 | 先修好测量，再做别的；测量不可靠，后面的结果都没有意义 |
| 核心假设不成立 | 停下，回到主张，考虑收窄或换角度 |
| 都没问题 | 进入正式执行，把这次试验的记录留好 |

**被安排"先做个预实验"时**，先和导师讨论清楚：这次试验的结果将怎样影响正式研究的计划[^thabane2010tutorial-e11]。说不清这一点的，与其叫预实验，不如当成一项独立的小研究来设计 `[本项目分析]`。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 跳过试验，直接铺开全部规模 | 问题在几周后才暴露，前面的工作可能白做 `[本项目分析]` |
| 先试最容易的部分 | 人们常常太迟才去否定自己的想法[^steinhardt2018stochastic-e12]；最危险的假设留到最后，才发现根本行不通 |
| 每个部分单独试过，从没整条跑通 | 各部分接起来时的问题，单独试发现不了 `[本项目分析]` |
| 只看程序没报错 | 很多错误是静默的，结果看上去照样"能用"[^karpathy2019recipe-e3] |
| 预实验找了和正式参与者完全不同的人 | 发现不了正式条件下的问题[^ko2015practical-e32][^thabane2010tutorial-e9] |
| 试完再定"什么算成功" | 标准会被结果带着走 `[本项目分析]`；临床预实验教程专门指出过这个毛病：没有明确的可行性目标和成功标准[^thabane2010tutorial-e6] |
| 用预实验的效应量算正式研究的样本量 | 小样本估出的效应量很不精确[^lakens2022sample-e4] |
| 预实验没有显著结果，就认定没效果 | 样本不足时只能说"没有定论"[^thabane2010tutorial-e7] |
| 一次试验不顺就放弃整个思路 | 失败的只是一种实现[^steinhardt2018stochastic-e10] |

## 产出物

- 一张假设清单：按流程、资源、管理、科学分组，标出最危险的三个（第 1 节）
- 每个危险假设的检验记录：预期、实际结果、结论（第 2 节）
- 一个能从头到尾跑通的最小版本，和填了一行的结果表（第 3 节）
- 预实验计划和每轮的问题记录（第 4 节，涉及人、问卷、标注时）
- 一张事先写好的"继续 / 修改后继续 / 停"标准表，以及对照它写的试验总结（第 5、6 节）
- 根据试验结果修改过的研究设计

## 检查点

满足下面几条，可以进入正式执行：

- [ ] 列出了设计依赖的假设，最危险的几个都已经检验过
- [ ] 每个检验之前都写了预期，之后都写了结论
- [ ] 整条流程用最小规模从头到尾跑通过，结果表的每一格都知道从哪里来
- [ ] 有"不该有效"的基线和简单基线的成绩
- [ ] 涉及人、问卷、标注的部分，在接近正式条件下试过，发现的问题已经改掉
- [ ] 试之前写好了"继续 / 修改后继续 / 停"的标准，试验结果对照它做了判断
- [ ] 没有把预实验的效果当成研究结论
- [ ] 导师看过试验总结和修改后的设计

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 核心假设不成立，比如要测的差别几乎不存在 | [收敛成项目](../01_from-interest-to-project/03_converge.md#1-写出你想证明的那句话)，收窄或换一个主张 |
| 需要的数据、工具或参与者拿不到 | [选定研究套路和方法](02_choose-strategy-and-method.md)，换一种能拿到的证据 |
| 测量方法或标注规则怎么改都不可靠 | [从研究问题到证据清单](01_question-to-evidence.md)，重新想用什么来衡量 |
| 试验暴露出原先没想到的效度威胁 | [效度与局限](03_validity-and-limits.md)，补上应对办法 |
| 时间和费用远超计划 | [形成研究计划](../01_from-interest-to-project/04_research-plan.md#关键判断)，重新决定砍什么 |

## 下一步

危险假设都查过了，流程跑通了，设计也按试验结果改好了。下一步是正式执行：按计划推进，在执行中不断调整，卡住时有办法往下走。见[执行与迭代](../03_conduct-and-analyze/01_run-and-iterate.md)。

[^steinhardt2018stochastic-e5]: Steinhardt 2018，A further improvement: opening up the "task" black box。[证据](../../sources/notes/steinhardt2018stochastic.md#e5)
[^steinhardt2018stochastic-e6]: Steinhardt 2018，A further improvement。[证据](../../sources/notes/steinhardt2018stochastic.md#e6)
[^steinhardt2018stochastic-e7]: Steinhardt 2018，Some further practical ideas。[证据](../../sources/notes/steinhardt2018stochastic.md#e7)
[^steinhardt2018stochastic-e10]: Steinhardt 2018，Exponentially branching search trees。[证据](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e12]: Steinhardt 2018，Summary。[证据](../../sources/notes/steinhardt2018stochastic.md#e12)
[^steinhardt2018stochastic-e13]: Steinhardt 2018，Additional Discussion。[证据](../../sources/notes/steinhardt2018stochastic.md#e13)
[^steinhardt2018stochastic-e18]: Steinhardt 2018，Some further practical ideas。[证据](../../sources/notes/steinhardt2018stochastic.md#e18)
[^steinhardt2018stochastic-e22]: Steinhardt 2018，Additional Discussion。[证据](../../sources/notes/steinhardt2018stochastic.md#e22)
[^steinhardt2018stochastic-e24]: Steinhardt 2018，Some further practical ideas。[证据](../../sources/notes/steinhardt2018stochastic.md#e24)
[^nanda2025mindsets-e12]: Nanda 2025b，Moving Fast。[证据](../../sources/notes/nanda2025mindsets.md#e12)
[^karpathy2019recipe-e1]: Karpathy 2019，The recipe。[证据](../../sources/notes/karpathy2019recipe.md#e1)
[^karpathy2019recipe-e2]: Karpathy 2019，The recipe。[证据](../../sources/notes/karpathy2019recipe.md#e2)
[^karpathy2019recipe-e3]: Karpathy 2019，2) Neural net training fails silently。[证据](../../sources/notes/karpathy2019recipe.md#e3)
[^karpathy2019recipe-e5]: Karpathy 2019，2. Set up the end-to-end training/evaluation skeleton，input-independent baseline。[证据](../../sources/notes/karpathy2019recipe.md#e5)
[^karpathy2019recipe-e6]: Karpathy 2019，3. Overfit，complexify only one at a time。[证据](../../sources/notes/karpathy2019recipe.md#e6)
[^karpathy2019recipe-e8]: Karpathy 2019，2. Set up the end-to-end training/evaluation skeleton。[证据](../../sources/notes/karpathy2019recipe.md#e8)
[^karpathy2019recipe-e9]: Karpathy 2019，2. Set up the end-to-end training/evaluation skeleton，结尾段。[证据](../../sources/notes/karpathy2019recipe.md#e9)
[^easterday2014design-e12]: Easterday 等人 2014，Iteration，第 321 页。[证据](../../sources/notes/easterday2014design.md#e12)
[^easterday2014design-e14]: Easterday 等人 2014，Stage Dependent Search，第 322 页。[证据](../../sources/notes/easterday2014design.md#e14)
[^ko2015practical-e31]: Ko 等人 2015，§8 Piloting。[证据](../../sources/notes/ko2015practical.md#e31)
[^ko2015practical-e32]: Ko 等人 2015，§8 Piloting。[证据](../../sources/notes/ko2015practical.md#e32)
[^ko2015practical-e33]: Ko 等人 2015，§8 Piloting。[证据](../../sources/notes/ko2015practical.md#e33)
[^kallio2016systematic-e5]: Kallio 等人 2016，Results，Pilot testing of the interview guide。[证据](../../sources/notes/kallio2016systematic.md#e5)
[^kallio2016systematic-e6]: Kallio 等人 2016，Results，Pilot testing of the interview guide。[证据](../../sources/notes/kallio2016systematic.md#e6)
[^molleri2020empirically-e2]: Molléri 等人 2020，§2，Instrument validation。[证据](../../sources/notes/molleri2020empirically.md#e2)
[^wagner2020challenges-e24]: Wagner 等人 2020，§6，Take Aways。[证据](../../sources/notes/wagner2020challenges.md#e24)
[^kitchenham2007guidelines-e8]: Kitchenham & Charters 2007，§5.4。[证据](../../sources/notes/kitchenham2007guidelines.md#e8)
[^thabane2010tutorial-e1]: Thabane 等人 2010，§1 Introduction。[证据](../../sources/notes/thabane2010tutorial.md#e1)
[^thabane2010tutorial-e2]: Thabane 等人 2010，§3 Reasons for Conducting Pilot Studies。[证据](../../sources/notes/thabane2010tutorial.md#e2)
[^thabane2010tutorial-e3]: Thabane 等人 2010，§6 Criteria for Success。[证据](../../sources/notes/thabane2010tutorial.md#e3)
[^thabane2010tutorial-e4]: Thabane 等人 2010，§6，POET 预研究的例子。[证据](../../sources/notes/thabane2010tutorial.md#e4)
[^thabane2010tutorial-e5]: Thabane 等人 2010，§5 Challenges and Misconceptions。[证据](../../sources/notes/thabane2010tutorial.md#e5)
[^thabane2010tutorial-e6]: Thabane 等人 2010，§5 Challenges and Misconceptions。[证据](../../sources/notes/thabane2010tutorial.md#e6)
[^thabane2010tutorial-e7]: Thabane 等人 2010，§7 Frequently asked questions。[证据](../../sources/notes/thabane2010tutorial.md#e7)
[^thabane2010tutorial-e8]: Thabane 等人 2010，§7 Frequently asked questions。[证据](../../sources/notes/thabane2010tutorial.md#e8)
[^thabane2010tutorial-e9]: Thabane 等人 2010，§5，样本量。[证据](../../sources/notes/thabane2010tutorial.md#e9)
[^thabane2010tutorial-e10]: Thabane 等人 2010，§5，样本量与合并数据。[证据](../../sources/notes/thabane2010tutorial.md#e10)
[^thabane2010tutorial-e11]: Thabane 等人 2010，§5 Challenges and Misconceptions。[证据](../../sources/notes/thabane2010tutorial.md#e11)
[^thabane2010tutorial-e12]: Thabane 等人 2010，§8 Ethical Aspects of Pilot Studies。[证据](../../sources/notes/thabane2010tutorial.md#e12)
[^tcps2022ethical-e1]: 加拿大《三理事会政策声明》2022 年版，第 2 章 Article 2.1。[证据](../../sources/notes/tcps2022ethical.md#e1)
[^tcps2022ethical-e3]: 加拿大《三理事会政策声明》2022 年版，第 6 章 Article 6.11。[证据](../../sources/notes/tcps2022ethical.md#e3)
[^tcps2022ethical-e4]: 加拿大《三理事会政策声明》2022 年版，第 6 章 Article 6.11 Pilot Studies。[证据](../../sources/notes/tcps2022ethical.md#e4)
[^tcps2022ethical-e5]: 加拿大《三理事会政策声明》2022 年版，第 6 章 Article 6.12。[证据](../../sources/notes/tcps2022ethical.md#e5)
[^lakens2022sample-e4]: Lakens 2022，What is the Expected Effect Size?。[证据](../../sources/notes/lakens2022sample.md#e4)
[^perciedusert2020reporting-e36]: Percie du Sert 等人 2020，Box 3。[证据](../../sources/notes/perciedusert2020reporting.md#e36)
[^curtis2018experimental-e11]: Curtis 等人 2018，Flexibility and pilot data。[证据](../../sources/notes/curtis2018experimental.md#e11)
