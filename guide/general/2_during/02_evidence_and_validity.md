# 证据、分析与效度

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲怎样让结论站得住：主张怎么提，证据怎么收集、比较和分析，怎样诚实地报告结果和局限。第 1、6、7 节适用于各类研究；第 2 到 5 节主要针对**定量的、做比较的研究**（实验、计算、问卷统计等），定性研究可取其道理，标"（适用时）"的做法按自己的方法取舍 `[本项目分析]`。具体学科的统计方法、实验设计细节不在这里展开，请查本学科的方法教材；为什么这些做法关乎诚信，见[科研诚信与伦理](../4_throughout/02_integrity_and_ethics.md)；怎么把结果写成论文，见[写作](../3_after/01_writing.md)。

**读完本章，你应该能：**

- 把每个结论和支撑它的证据一一对上；
- 设计公平的比较，选对基线；
- 一次只改一个因素，弄清效果到底从哪来；
- 正确对待随机性：重复实验、报告波动、警惕"多试几次总有一次显著"；
- 用大白话说清自己研究的效度威胁，诚实报告负面结果和局限。

---

## 1. 先写清主张，再检查证据够不够

Feynman 说，科研的第一原则是不要欺骗自己，而你自己恰恰是最容易被骗的人[^feynman1974cargo-e7]。本章所有做法，都是在防止自己被自己骗。

一种常见的自我欺骗是**不对称的检查**：结果不合预期时拼命找毛病，合预期时就不再细查。Millikan 用油滴实验测出了电子电荷，但他的数值有偏差。后来者测得的数值偏离 Millikan 太多时，就去找"哪里出了错"；接近时就不再仔细查[^feynman1974cargo-e14]。这样，偏差会被一直保留下来 `[本项目分析]`。

**怎么防**：对"好结果"和"坏结果"用同样严格的检查。结果好得出乎意料时，尤其要先怀疑自己哪里做错了 `[本项目分析]`。

**怎么做：**

1. **动手前写下研究问题和预期结果。** 实验的目的是检验研究问题[^huang2023experiments-e1]，而不只是得到一个更好看的结果 `[本项目分析]`。先预测"如果加上 X、去掉 Y，应该看到什么"，这样才能解读结果，也更容易发现错误[^huang2023experiments-e3][^huang2023experiments-e4]。
2. **把主张写成明确的句子。** 主张不明确，读者就无法判断实验是否支持它[^blackburn2018sigplan-e1]。
3. **逐条对证据。** 每个结论都要对应研究问题，并有明确的数据、观察或论证支持[^ralph2020empirical-e18]。
4. **检查主张的范围。** 结论要能从证据中清楚地推出，证据支撑不足的主张会误导读者[^blackburn2018sigplan-e2]。

一个简单的自查方法 `[本项目分析]`：画一张两列的表，左边列结论，右边列支撑它的具体实验、表格或图。右边空着的，要么补证据，要么把结论改弱。

**容易错在哪：**

- **范围写大了。** 只在一个数据集、一个样本上表现好，不代表在别处也好[^lones2021avoid-e10]。
- **测的不是你想说的。** 用间接指标代替真正关心的指标，必须说明为什么可以代替[^blackburn2018sigplan-e13]。例如用"完成任务的时间"去说明"任务的难度"，就需要论证 `[本项目分析]`。

---

## 2. 和强基线做公平的比较

想说"我的方法更好"，就要回答"比什么好"。用来对比的方法叫**基线**（baseline）。没有可靠的基线，后面看到的"变化"就无从解读[^huang2023experiments-e5]。

**选哪些基线：**

- **最朴素的做法（适用时）。** 例如拿精巧的方法和纯随机的做法比，看它是否真的更好[^blackburn2018sigplan-e6]。
- **更简单的替代方案。** 基线常常比新方法简单，用来证明新方法多出来的复杂度确有必要[^lones2021avoid-e1][^menzies2019bad-e7]。
- **当前最好的方法（适用时）。** 只和弱对手比，说服力不够[^lones2021avoid-e2]。定性研究中对应的做法是认真对照已有理论和解释，说明你的解释比它们多说明了什么 `[本项目分析]`。
- **"本不该有效"的对照。** 在机器学习中，可以训练一个完全不看输入的模型：如果它和真实模型差不多好，说明模型并没有从数据中学到东西[^karpathy2019recipe-e5]。其他学科的对应做法是设置空白对照或安慰剂组 `[本项目分析]`。

**比较要公平：**

- **不要立稻草人。** 把弱基线说成"最先进方法"，会夸大新方法的好处[^blackburn2018sigplan-e4]。
- **给对手同样的待遇。** 不能让对手处于不公平的劣势[^blackburn2018sigplan-e5]。最常见的不公平是：自己的方法精心调过参数，对手用默认设置。这样只能说明"好好用新方法能胜过随便用旧方法"[^menzies2019bad-e5][^menzies2019bad-e6]。在机器学习中，曾有一系列被归功于新模型结构的"改进"，后来发现其实来自更好的调参；同等条件下，老方法反而最好[^lipton2019troubling-e5]。
- **数字更高不等于更好。** 数字更高并不说明方法更好，原因有很多[^lones2021avoid-e11]；例如两篇论文用的数据、设置不同，直接比数字就没有意义 `[本项目分析]`。
- **先重复别人的结果，再改条件。** Feynman 讲过一个例子：想知道条件 Y 下老鼠是否仍有行为 A，应先在自己实验室按原条件 X 重做一遍，确认能得到 A，再只把 X 换成 Y。这样才知道差异真的来自你控制的那个因素[^feynman1974cargo-e10]。

---

## 3. 一次只改一个因素，弄清效果从哪来

**怎么做：**

- **一次只改一处。** 同时改好几处，等于在检验一个牵涉多个因素的复杂假设，结果说明不了什么[^huang2023experiments-e2]。要加入几样新东西时，一样一样加，每次确认得到了预期的效果[^karpathy2019recipe-e6]。
- **从简单开始，每步验证。** 从最简单的版本做起，每一步先预测结果再验证，不符合就查到找出原因为止；避免一次引入大量未经验证的复杂度[^karpathy2019recipe-e1][^karpathy2019recipe-e2]。
- **"没报错"不等于"做对了"。** 很多错误是静默的，结果看上去照样能用[^karpathy2019recipe-e3]。动手前先亲自看看原始数据，离群值往往能暴露数据或处理流程的问题[^karpathy2019recipe-e7]。
- **最后做消融实验（适用时）。** 消融实验（ablation study）就是把方法中的组成部分逐个去掉，看效果怎么变。同时提出很多改动却不做消融，就看不出提升从哪里来，有时真正起作用的只有其中一个[^lipton2019troubling-e4]。
- **两种设计都合理时，都做。** 不必纠结选 A 还是 B，让结果说话[^huang2023experiments-e7]。

Feynman 讲过一个"一流实验"的例子：Young 想训练老鼠走进特定的门，却发现老鼠总能认出上次放食物的门。他依次排除了门的外观、气味、灯光，最后发现老鼠靠的是跑过地板时的声音，把走廊铺上沙子才解决。这个实验的价值在于找出了老鼠**真正**依靠的线索，而不是研究者以为的那个[^feynman1974cargo-e15]。

所以，不要只问"效果有多好"，还要问"什么起了作用、为什么"[^lipton2019troubling-e7]。强的实证论文常见三种做法：错误分析（逐个查看出错的例子，找出错在哪类情况）、消融实验、稳健性检查（换数据、换设置或换分析方法后，看结论是否还成立）[^lipton2019troubling-e8]。

> **不同的看法：消融实验是不是必须做？**
> - Lipton & Steinhardt 认为，不做消融会误导读者，让人以为每个改动都必要[^lipton2019troubling-e4]。审稿人应当更看重"一个简单想法加两个负面结果"，而不是"三个想法捆在一起、不做消融、得到同样提升"[^lipton2019troubling-e9]。
> - 他们也承认：消融不是理解方法的唯一途径，计算资源有限时可能做不了[^lipton2019troubling-e6]；有的突破性工作结果足够重要、实验又很昂贵，等消融做完再发表可能得不偿失[^lipton2019troubling-e10]。
>
> 实际操作中：能做就做，至少对你主张"关键"的那个部分做；做不了的，在论文里说明原因，并用错误分析或稳健性检查补充 `[本项目分析]`。

---

## 4. 留一份数据只用于最后检验

开发方法时看过、用过的数据，不能再拿来证明方法有效。下面的做法主要针对要开发和评估方法的研究（适用时）。

**怎么做：**

- 项目一开始就划出一份独立的检验数据，只在最后用一次，评估最终的那个方案[^lones2021avoid-e3]。
- 开发时参考过的例子不能再用来评估，必须在开发时没用过的数据上评估[^blackburn2018sigplan-e12]。

**容易错在哪**：反复用同一份检验数据试不同方案，直到结果好看。这个过程往往没有记录[^lones2021avoid-e4]，但检验数据用得越多次，结论就越偏向这份数据，越不可信[^lones2021avoid-e5]。

这条原则在机器学习中常称为"测试集只用一次"，与"数据泄漏"（评估用的信息混进了开发过程）相关，但道理通用 `[本项目分析]`：问卷题目根据预调查结果反复修改后，就不能再用同一批预调查数据证明问卷有效；根据一批样本提出的假设，要用另一批样本来检验。

---

## 5. 认真对待随机性和统计

**怎么做：**

1. **重复多次。** 只测一次不可靠，可能高估也可能低估[^lones2021avoid-e6]。重复次数不够，可能把噪声当成信号[^blackburn2018sigplan-e7]。
2. **报告波动，而不只是平均数。** 只报平均数或中位数会误导读者，要同时给出方差、标准差（衡量结果分散程度）、分位数（如中间一半结果落在哪个范围）或置信区间（真实值大概率落在的范围）[^blackburn2018sigplan-e8]。不要把 4%、6%、7%、49% 概括成"最高提升 49%"，要报告完整的分布[^blackburn2018sigplan-e9]。要检查效应是真实存在，还是只是噪声[^menzies2019bad-e4]。
3. **报告全部运行结果。** 一遍遍重跑、只报告最好的那一次，是典型的"凑结果"套路[^zeller2021devil-e1]。
4. **记录随机种子和全部设置（适用时）。** 随机种子是程序生成随机数的起点，固定它就能让"随机"过程重现。带随机性的方法不提供随机种子，别人就无法精确复现[^menzies2019bad-e8]。在计算机领域，排错阶段可以固定随机种子，让两次运行结果相同[^karpathy2019recipe-e4]；但评估阶段要换多个种子重复，两者不矛盾 `[本项目分析]`。怎样记录和保存这些信息，见[整理材料](03_organizing_materials.md)。
5. **比较次数多了，要校正。** 做 20 次 95% 置信水平的检验，很可能有一次是假阳性（其实没有差异，却判断为有）[^lones2021avoid-e7]，所以要做多重比较校正，即按比较次数把"显著"的门槛调严。Zeller 反讽地"建议"：随便拿两个量找相关，总能找到一个"新发现"[^zeller2021devil-e4]。只报告显著的那部分检验（p-hacking），或在声称是验证性的研究中看到结果后再提出假设（HARKing），都是公认的反面做法[^ralph2020empirical-e27]。
6. **显著不等于重要。** 样本足够多时，再小的差异也能"显著"[^lones2021avoid-e8]。例如相关系数仅约 0.01 时，实际意义可以忽略，和没有相关没有区别[^menzies2019bad-e2]。研究开始前就定下"多大的差异才算有实际意义"（最小有意义效应量）[^menzies2019bad-e3]，报告时同时给出效应量（差异或关联有多大，而不只是有没有）。

> **不同的看法：要不要依赖显著性检验？**
> - Lones 建议比较方法时使用统计检验，比较多个方法时做多重比较校正[^lones2021avoid-e7]；但他也指出，校正方法很多，什么时候该校正本身有争论[^lones2021avoid-e12]。
> - Menzies & Shepperd 认为，过度依赖 "p < 0.05" 本身就是问题，更应关注效应量，并事先定好有实际意义的效应大小[^menzies2019bad-e2][^menzies2019bad-e3]。
>
> 实际操作中：显著性检验可以用，但不要只报"显著/不显著"。同时报告效应量和置信区间，并说明做了多少次比较。具体用哪种检验，请教导师或本学科的统计方法资料 `[本项目分析]`。

---

## 6. 说清效度威胁

**效度**（validity）指结果的可信程度：结果在多大程度上是真的，没有被研究者的主观看法带偏[^runeson2009guidelines-e1]。常见的三类，用大白话说：

| 类型 | 问的是什么 | 例子 `[本项目分析]` |
|---|---|---|
| **构念效度**（construct validity） | 你实际测的东西，真的代表你想研究的概念吗？[^runeson2009guidelines-e3] | 用"论文引用数"代表"研究质量" |
| **内部效度**（internal validity） | 你看到的"A 影响 B"，会不会其实是第三个因素 C 造成的？[^runeson2009guidelines-e4] | 新教学法班级成绩更好，但这个班的学生本来就更强 |
| **外部效度**（external validity） | 结论能推广到你研究的对象之外吗？[^runeson2009guidelines-e5] | 只在大学生中做的实验，结论能否用于职场人士 |

**怎么做：**

- **从设计阶段就考虑。** 到分析阶段才想效度就太晚了[^runeson2009guidelines-e2]。
- **写出真正的威胁，而不是凑数。** Feynman 要求报告所有可能使实验不成立的因素：其他可能的解释，以及你用什么实验排除了哪些[^feynman1974cargo-e11]。SIGPLAN 清单的作者指出，软件工程论文的效度威胁一节常常只列无关紧要的，回避真正的[^blackburn2018sigplan-e10]。
- **说明每个威胁对结果有什么影响。** 只罗列威胁、不联系结果，是反面做法[^ralph2020empirical-e52]。能做的话，说明你为考察或减轻它做了什么[^ralph2020empirical-e51]。
- **只用适合你研究的标准。** 没有通用的质量标准，每项研究要按适合其方法的标准来评价[^ralph2020empirical-e24]；例如不做因果推断的研究，内部效度就不是重点 `[本项目分析]`。某类方法固有的局限（如案例研究推广性有限）不算缺陷[^ralph2020empirical-e25]。

---

## 7. 诚实报告：负面结果、局限和推测

这里讲具体做法；为什么这关乎科研诚信，见[科研诚信与伦理：报告全部结果，包括负面结果](../4_throughout/02_integrity_and_ethics.md#2-报告全部结果包括负面结果)。

**怎么做：**

- **无论结果如何都报告。** 决定检验一个想法，就要无论正反都发表；只发表某一类结果，会让论证显得比实际更好[^feynman1974cargo-e9]。只报告显著或"有意思"的结果（报告偏差，reporting bias），会严重高估效应[^menzies2019bad-e1]。要完整报告工作，包括有效的和无效的[^lones2021avoid-e9]。负面结果本身不是拒稿的理由[^ralph2020empirical-e41]。
- **写出不利的事实。** 提出一个解释时，要同时写出支持它的和与它不符的事实[^feynman1974cargo-e4]。目标是给出让别人能判断你工作价值的全部信息，而不只是引向某个方向的信息[^feynman1974cargo-e5]。
- **如实写局限，并让结论与局限一致。** 要披露所有主要局限[^ralph2020empirical-e18]。不写局限或只写无关紧要的，会让读者得出过强的结论[^blackburn2018sigplan-e3]。常见的反面做法是：承认了局限，写结论时却当它不存在[^ralph2020empirical-e66]；或者"成果写进标题，局限藏进脚注"[^zeller2021devil-e3]。
- **把结果和推测分开。** 论文常把推测包装成解释，读者因为它出现在论文里就当成定论[^lipton2019troubling-e2]。好的做法是把直觉和有证据的结论分开[^lipton2019troubling-e1]，例如把推测放进单独标明的一节[^lipton2019troubling-e3]。写作时可以用"结果显示……"和"我们推测……"明确区分 `[本项目分析]`。
- **记录一切。** 实验设置、决策、失败的尝试都要记下来，别靠脑子记[^huang2023experiments-e6]。不记日志、不留历史、不验证结果、不共享，正是 Zeller 反讽的"高效凑论文"做法[^zeller2021devil-e8]。

诚实说明自己做到了什么、没做到什么，科学才能一步步扎实地前进[^blackburn2018sigplan-e11]。

---

## 本章检查清单

清单用来辅助判断，不能代替判断[^blackburn2018sigplan-e14]。

- [ ] 每个结论都写成了明确的句子，并能指出支撑它的具体证据
- [ ] 结论的范围没有超出数据和样本
- [ ] 测量的指标确实代表想研究的概念；用了间接指标的，说明了理由
- [ ] （适用时）有朴素基线、更简单的替代方案，以及当前最好的方法；定性研究对照了已有的解释
- [ ] 所有对比方法得到了同等的调整和条件
- [ ] 每次只改一个因素；（适用时）对主张关键的部分做了消融或其他检查
- [ ] （适用时）有一份只在最后使用一次的检验数据；用来提出假设的材料没有再用来检验它
- [ ] 重复了多次，报告了波动（标准差、置信区间等），而不只是平均数
- [ ] 报告了全部运行，而不是最好的一次；（适用时）记录了随机种子和全部设置
- [ ] 比较次数多时做了校正；同时报告了效应量
- [ ] 写出了真正的效度威胁，并说明它们对结果的影响
- [ ] 报告了负面结果和与结论不符的事实
- [ ] 结果和推测分开写

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只和弱基线或没调参的对手比 | 只说明"好好用新方法胜过随便用旧方法"，夸大了好处[^menzies2019bad-e6][^blackburn2018sigplan-e4] |
| 一次改好几处，不做消融 | 看不出提升从哪来，可能只有一处在起作用[^lipton2019troubling-e4] |
| 反复用同一份检验数据调方案 | 结论偏向这份数据，越用越不可信[^lones2021avoid-e5] |
| 只跑一次，或只报最好的一次 | 可能把噪声当信号[^blackburn2018sigplan-e7][^zeller2021devil-e1] |
| 只报平均数或"最高提升 X%" | 掩盖了结果的真实分布[^blackburn2018sigplan-e9] |
| 只看 p 值是否小于 0.05 | 样本大时微不足道的差异也会显著[^menzies2019bad-e2] |
| 效度威胁只列无关紧要的 | 回避真正的威胁，让读者得出过强结论[^blackburn2018sigplan-e10] |
| 承认局限，结论却照旧 | 局限形同虚设[^ralph2020empirical-e66] |
| 只报告"有意思"的结果 | 报告偏差会严重高估效应[^menzies2019bad-e1] |
| 把推测写成解释 | 读者会因为它出现在论文里就当成定论[^lipton2019troubling-e2] |

## 延伸阅读

- **Feynman，Cargo Cult Science**：一篇短演讲，讲清科研诚信为什么要"向后弯腰"，适合每个新手读一遍。
- **Lipton & Steinhardt，Troubling Trends in Machine Learning Scholarship**：机器学习领域的例子，但"区分解释与推测""找出提升的来源"适用于各学科。
- **SIGPLAN Empirical Evaluation Checklist**（美国计算机协会编程语言分会制定）：一页纸的实证评估清单，适合投稿前逐项自查。
- **ACM SIGSOFT Empirical Standards（General Standard）**（美国计算机协会软件工程分会制定的实证研究标准）：各类实证研究都适用的基本要求和反面模式。
- **Menzies & Shepperd，"Bad smells" in software analytics papers**：数据分析类研究的常见问题，统计部分尤其值得读。
- **Lones，How to avoid machine learning pitfalls**：做机器学习研究的新手必读；其他学科可读第 5、6 节（比较和报告）。
- **Zeller，The Devil's Guide to Incremental Research**：反讽写法，反着读就是一份"别这样做"的清单。

[^feynman1974cargo-e7]: Feynman 1974，演讲正文。[证据](../../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e11]: Feynman 1974，演讲正文，科学诚信一段。[证据](../../../sources/notes/feynman1974cargo.md#e11)
[^feynman1974cargo-e4]: Feynman 1974，演讲正文，科学诚信一段。[证据](../../../sources/notes/feynman1974cargo.md#e4)
[^feynman1974cargo-e9]: Feynman 1974，演讲正文。[证据](../../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e10]: Feynman 1974，演讲正文，老鼠实验的例子。[证据](../../../sources/notes/feynman1974cargo.md#e10)
[^feynman1974cargo-e14]: Feynman 1974，演讲正文，Millikan 的例子。[证据](../../../sources/notes/feynman1974cargo.md#e14)
[^feynman1974cargo-e15]: Feynman 1974，演讲正文，Young 的例子。[证据](../../../sources/notes/feynman1974cargo.md#e15)
[^feynman1974cargo-e5]: Feynman 1974，演讲正文。[证据](../../../sources/notes/feynman1974cargo.md#e5)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019，§1，第 1 页。[证据](../../../sources/notes/lipton2019troubling.md#e1)
[^lipton2019troubling-e2]: Lipton & Steinhardt 2019，§3.1，第 2 页。[证据](../../../sources/notes/lipton2019troubling.md#e2)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019，§3.1，第 3 页。[证据](../../../sources/notes/lipton2019troubling.md#e3)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e5]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../../sources/notes/lipton2019troubling.md#e5)
[^lipton2019troubling-e6]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../../sources/notes/lipton2019troubling.md#e6)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../../sources/notes/lipton2019troubling.md#e7)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../../sources/notes/lipton2019troubling.md#e8)
[^lipton2019troubling-e9]: Lipton & Steinhardt 2019，§5.2，第 8 页。[证据](../../../sources/notes/lipton2019troubling.md#e9)
[^lipton2019troubling-e10]: Lipton & Steinhardt 2019，§6.1，第 9 页。[证据](../../../sources/notes/lipton2019troubling.md#e10)
[^lones2021avoid-e1]: Lones 2021，§5.2，第 21 页。[证据](../../../sources/notes/lones2021avoid.md#e1)
[^lones2021avoid-e2]: Lones 2021，§5.2，第 21 页。[证据](../../../sources/notes/lones2021avoid.md#e2)
[^lones2021avoid-e3]: Lones 2021，§3.1，第 8 页。[证据](../../../sources/notes/lones2021avoid.md#e3)
[^lones2021avoid-e4]: Lones 2021，§4.3，第 15 页。[证据](../../../sources/notes/lones2021avoid.md#e4)
[^lones2021avoid-e5]: Lones 2021，§4.3，第 15 页。[证据](../../../sources/notes/lones2021avoid.md#e5)
[^lones2021avoid-e6]: Lones 2021，§4.4，第 15 页。[证据](../../../sources/notes/lones2021avoid.md#e6)
[^lones2021avoid-e7]: Lones 2021，§5.4，第 22 页。[证据](../../../sources/notes/lones2021avoid.md#e7)
[^lones2021avoid-e8]: Lones 2021，§6.4，第 25 页。[证据](../../../sources/notes/lones2021avoid.md#e8)
[^lones2021avoid-e9]: Lones 2021，§6，第 23 页。[证据](../../../sources/notes/lones2021avoid.md#e9)
[^lones2021avoid-e10]: Lones 2021，§6.3，第 24 页。[证据](../../../sources/notes/lones2021avoid.md#e10)
[^lones2021avoid-e11]: Lones 2021，§5.1，第 19 页。[证据](../../../sources/notes/lones2021avoid.md#e11)
[^lones2021avoid-e12]: Lones 2021，§5.4，第 22 页。[证据](../../../sources/notes/lones2021avoid.md#e12)
[^blackburn2018sigplan-e1]: SIGPLAN 清单 2018，Clearly Stated Claims。[证据](../../../sources/notes/blackburn2018sigplan.md#e1)
[^blackburn2018sigplan-e2]: SIGPLAN 清单 2018，Clearly Stated Claims。[证据](../../../sources/notes/blackburn2018sigplan.md#e2)
[^blackburn2018sigplan-e3]: SIGPLAN 清单 2018，Fails to acknowledge limitations。[证据](../../../sources/notes/blackburn2018sigplan.md#e3)
[^blackburn2018sigplan-e4]: SIGPLAN 清单 2018，Suitable Comparison。[证据](../../../sources/notes/blackburn2018sigplan.md#e4)
[^blackburn2018sigplan-e5]: SIGPLAN 清单 2018，Comparison is unfair。[证据](../../../sources/notes/blackburn2018sigplan.md#e5)
[^blackburn2018sigplan-e6]: SIGPLAN 清单 2018，Notes。[证据](../../../sources/notes/blackburn2018sigplan.md#e6)
[^blackburn2018sigplan-e7]: SIGPLAN 清单 2018，Insufficient number of trials。[证据](../../../sources/notes/blackburn2018sigplan.md#e7)
[^blackburn2018sigplan-e8]: SIGPLAN 清单 2018，No data distribution reported。[证据](../../../sources/notes/blackburn2018sigplan.md#e8)
[^blackburn2018sigplan-e9]: SIGPLAN 清单 2018，Misleading summary of results。[证据](../../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e10]: SIGPLAN 清单 2018，Notes。[证据](../../../sources/notes/blackburn2018sigplan.md#e10)
[^blackburn2018sigplan-e11]: SIGPLAN 清单 2018，Notes。[证据](../../../sources/notes/blackburn2018sigplan.md#e11)
[^blackburn2018sigplan-e12]: SIGPLAN 清单 2018，Tested on training set。[证据](../../../sources/notes/blackburn2018sigplan.md#e12)
[^blackburn2018sigplan-e13]: SIGPLAN 清单 2018，Indirect or inappropriate proxy metric。[证据](../../../sources/notes/blackburn2018sigplan.md#e13)
[^blackburn2018sigplan-e14]: SIGPLAN 清单 2018，标题下说明。[证据](../../../sources/notes/blackburn2018sigplan.md#e14)
[^menzies2019bad-e1]: Menzies & Shepperd 2019，§4.4。[证据](../../../sources/notes/menzies2019bad.md#e1)
[^menzies2019bad-e2]: Menzies & Shepperd 2019，§4.6。[证据](../../../sources/notes/menzies2019bad.md#e2)
[^menzies2019bad-e3]: Menzies & Shepperd 2019，§4.6。[证据](../../../sources/notes/menzies2019bad.md#e3)
[^menzies2019bad-e4]: Menzies & Shepperd 2019，§4.9。[证据](../../../sources/notes/menzies2019bad.md#e4)
[^menzies2019bad-e5]: Menzies & Shepperd 2019，§4.10。[证据](../../../sources/notes/menzies2019bad.md#e5)
[^menzies2019bad-e6]: Menzies & Shepperd 2019，§4.10。[证据](../../../sources/notes/menzies2019bad.md#e6)
[^menzies2019bad-e7]: Menzies & Shepperd 2019，§4.11。[证据](../../../sources/notes/menzies2019bad.md#e7)
[^menzies2019bad-e8]: Menzies & Shepperd 2019，§4.4。[证据](../../../sources/notes/menzies2019bad.md#e8)
[^zeller2021devil-e1]: Zeller 2021，THE CHERRY SHUFFLE。[证据](../../../sources/notes/zeller2021devil.md#e1)
[^zeller2021devil-e3]: Zeller 2021，THE ACHILLES HEEL。[证据](../../../sources/notes/zeller2021devil.md#e3)
[^zeller2021devil-e4]: Zeller 2021，THE FISHING EXPEDITION。[证据](../../../sources/notes/zeller2021devil.md#e4)
[^zeller2021devil-e8]: Zeller 2021，倒数第三段。[证据](../../../sources/notes/zeller2021devil.md#e8)
[^ralph2020empirical-e18]: ACM SIGSOFT Empirical Standards，General Standard，Essential Attributes。[证据](../../../sources/notes/ralph2020empirical.md#e18)
[^ralph2020empirical-e66]: ACM SIGSOFT Empirical Standards，General Standard，Research and Reporting Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards，General Standard，Research and Reporting Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e24]: ACM SIGSOFT Empirical Standards，General Standard，General Quality Criteria。[证据](../../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e41]: ACM SIGSOFT Empirical Standards，General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e25]: ACM SIGSOFT Empirical Standards，General Standard，Invalid Criticisms。[证据](../../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e51]: ACM SIGSOFT Empirical Standards，General Standard，Desirable Attributes。[证据](../../../sources/notes/ralph2020empirical.md#e51)
[^ralph2020empirical-e52]: ACM SIGSOFT Empirical Standards，Experiments，Antipatterns。[证据](../../../sources/notes/ralph2020empirical.md#e52)
[^runeson2009guidelines-e1]: Runeson & Höst 2009，§5.2.3，第 153 页。[证据](../../../sources/notes/runeson2009guidelines.md#e1)
[^runeson2009guidelines-e2]: Runeson & Höst 2009，§5.2.3，第 153 页。[证据](../../../sources/notes/runeson2009guidelines.md#e2)
[^runeson2009guidelines-e3]: Runeson & Höst 2009，§5.2.3。[证据](../../../sources/notes/runeson2009guidelines.md#e3)
[^runeson2009guidelines-e4]: Runeson & Höst 2009，§5.2.3。[证据](../../../sources/notes/runeson2009guidelines.md#e4)
[^runeson2009guidelines-e5]: Runeson & Höst 2009，§5.2.3。[证据](../../../sources/notes/runeson2009guidelines.md#e5)
[^huang2023experiments-e1]: Jia-Bin Huang 2023，推文串 *Why?*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e1)
[^huang2023experiments-e2]: Jia-Bin Huang 2023，推文串 *One thing at a time*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e2)
[^huang2023experiments-e3]: Jia-Bin Huang 2023，推文串 *Anticipate the results*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e3)
[^huang2023experiments-e4]: Jia-Bin Huang 2023，推文串 *Anticipate the results*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e4)
[^huang2023experiments-e5]: Jia-Bin Huang 2023，推文串 *Start with a baseline*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e5)
[^huang2023experiments-e6]: Jia-Bin Huang 2023，推文串 *Document everything*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e6)
[^huang2023experiments-e7]: Jia-Bin Huang 2023，推文串 *Two valid design choices? Do both!*，[原推文](https://twitter.com/jbhuang0604/status/1647098218172252160)。[证据](../../../sources/notes/huang2023experiments.md#e7)
[^karpathy2019recipe-e1]: Karpathy 2019，The recipe。[证据](../../../sources/notes/karpathy2019recipe.md#e1)
[^karpathy2019recipe-e2]: Karpathy 2019，The recipe。[证据](../../../sources/notes/karpathy2019recipe.md#e2)
[^karpathy2019recipe-e3]: Karpathy 2019，"Neural net training fails silently"。[证据](../../../sources/notes/karpathy2019recipe.md#e3)
[^karpathy2019recipe-e4]: Karpathy 2019，第 2 步 fix random seed。[证据](../../../sources/notes/karpathy2019recipe.md#e4)
[^karpathy2019recipe-e5]: Karpathy 2019，第 2 步 input-independent baseline。[证据](../../../sources/notes/karpathy2019recipe.md#e5)
[^karpathy2019recipe-e6]: Karpathy 2019，第 3 步 complexify only one at a time。[证据](../../../sources/notes/karpathy2019recipe.md#e6)
[^karpathy2019recipe-e7]: Karpathy 2019，第 1 步 Become one with the data。[证据](../../../sources/notes/karpathy2019recipe.md#e7)
