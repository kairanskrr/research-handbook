# 审稿意见、修改与被拒之后

> 本章的道理适用于各学科，例子和具体做法以计算机为例。各期刊、会议的流程差别很大（有没有作者回复环节、字数限制、能不能补实验），**动手前先读清楚你投的那一处的审稿说明**。

## 你现在在哪里

论文投出去了，审稿意见也回来了。你可能正处在下面某一种情况：

- 会议给了一段**作者回复**期（也叫 rebuttal，在结果出来之前，书面回应审稿意见），你要写一份回复；
- 期刊要求**修改**，你要改稿，再附一封逐条说明的**回复信**；
- 论文**被拒**了，你在想：改了投哪里？还是这个项目本身有问题？

不管哪一种，第一次读审稿意见时，你可能会觉得有的审稿人没认真读、有的意见不公平，心里很不舒服。

## 这一阶段要解决什么

把审稿意见变成下一步的行动。具体来说，是回答下面五个问题：

1. 审稿人到底在说什么？哪些是要害，哪些是小事？
2. 哪些要改，哪些要解释，哪些可以有理有据地不同意？
3. 怎样写一份让做决定的人看得懂的回复？
4. 被拒之后，问题出在论文、项目，还是投错了地方？
5. 下一步投哪里，或者回到哪一章重新做？

自己当审稿人、给别人写审稿意见，是另一件事，见[当审稿人](../08_throughout/being_a_reviewer.md)。

---

## 1. 先冷静读完，弄清你面对的是什么

**第一天只读，不回，不改。** 难过很正常，休息一天再回来[^huang2021rejection-e6]。怎样调整情绪、把被拒当作常态，见[心态与长期积累](../08_throughout/mindset_and_growth.md#2-把失败和被拒当作常态)。

**情绪平复后，客观地读。** 被拒或要求大修时，要认真听审稿人的意见，客观而不是凭情绪回应[^bourne2005published-e1]。然后弄清三件事 `[本项目分析]`：

| 要弄清的 | 去哪里看 |
|---|---|
| 这是哪种决定：等你回复、要求修改，还是拒稿？ | 决定信、审稿系统里的状态 |
| 你有多少时间、多少篇幅？能不能交修改稿、补实验？ | 会议或期刊的审稿说明 |
| 最后由谁拍板？ | 会议通常是程序委员会（会议的审稿委员会）或其中的领域主席（负责汇总审稿意见、提出录用建议的人），期刊通常是编辑 |

规矩各处不同，每年也可能变，别凭印象。下面只是两个计算机会议某一年的规定，用来说明差别有多大：

- 机器学习会议 NeurIPS 2025：作者有一周时间回复初审意见[^neurips2025cfp-e8]，回复期内不能提交修改后的论文或补充材料[^neurips2025cfp-e11]；
- 安全会议 USENIX Security '26（2026 年这一届）：不再有"大修"这种结果，论文最多经过两周的指导修改[^usenixsec2026cfp-e14]。

你投的那一处怎么规定，以它当年的征稿说明为准。

**还要知道谁会读你的回复。** 几位计算机研究者分享过经验，可以参考：审稿人读回复时，可能已是写完意见一个月以后，细节记不清了[^hicks2014response-e7]；做决定的领域主席对你的论文更不熟，最好假定他们只读审稿意见和你的回复[^parikh2020rebuttals-e2]。有的会议还会公开回复：NeurIPS 2025 在结果公布后，会把录用论文和自愿公开的被拒论文，连同审稿意见和作者回复一起公开[^neurips2025cfp-e13]。所以回复要写成任何人读了都没问题的样子 `[本项目分析]`。

**写下来：** 用三行写下：这次是哪种决定、截止时间和字数限制、最后谁拍板。再写一句话：如果只能用一句话概括审稿人的总体看法，是什么？

## 2. 把意见逐条拆开、分类

**先把所有意见拆成一条一条，放进一张表。** 下面几条来自计算机研究者写回复的经验，当作建议用：把每位审稿人的每条意见、问题、疑虑逐条列出来，放在一起看，容易发现几位审稿人的共同问题，也不会漏掉哪一条[^parikh2020rebuttals-e5][^parikh2020rebuttals-e17]。给审稿人和问题编号，比如 R1、R2 表示第一、第二位审稿人，R1Q1、R1Q2 表示第一位审稿人的第一、第二个问题，方便各自找到自己的问题和你的回答[^zeller2012rebuttals-e10]。**收到意见就马上做这一步**，这样才能尽早发现需要补的实验或分析[^parikh2020rebuttals-e17]。

**再给每条意见归类。** 下面的分类是我们给的一种做法 `[本项目分析]`：

| 类型 | 怎么认出来 | 通常怎么处理 |
|---|---|---|
| 误解 | 审稿人说"没有 X"，但论文里写了；或把你的方法理解错了 | 指出在哪一节，并在回复里复述；同时想想为什么会被误解，改写那一段 |
| 事实错误 | 审稿人对已有工作或数据的说法不对 | 拿事实和数据纠正，语气平和 |
| 合理要求，做得到 | 要补一个基线、一组实验、一段讨论 | 做，在回复里给出结果或写好的内容 |
| 合理要求，做不到 | 要补的实验需要拿不到的数据或算力，或会议不允许补实验 | 如实说明，讲清对结论的影响 |
| 动摇主张的问题 | 质疑证据能否支撑你的核心结论 | 最高优先级；可能要改结论的说法，见第 3 节 |
| 偏好不同 | 审稿人想要另一种方法或设计 | 解释你为什么这样选；有余力就试一下他的建议 |
| 小问题 | 错别字、图表格式、措辞 | 直接改，回复里一句话带过 |

用"大模型与智能合约安全"的例子试一下（虚构的示例 `[本项目分析]`）。假设你的论文主张"新方法在真实合约上比现有工具多发现三成漏洞"，三位审稿人提了这些意见：

| 编号 | 意见 | 归类 |
|---|---|---|
| R1Q1 | "测试用的合约可能出现在模型的训练数据里" | 动摇主张 |
| R2Q1 | "为什么没有和工具 X 比较？" | 合理要求，可能做得到 |
| R2Q2 | "论文没说清什么算发现了一个漏洞" | 误解，或者确实没写清 |
| R3Q1 | "应该用形式化验证而不是大模型" | 偏好不同 |
| R3Q2 | 第 4 页有错别字 | 小问题 |

**最后排优先级。** 建议这样排：几位审稿人共同的主要问题最先处理[^hicks2014response-e5]；其次是审稿人认为你可能没法改好的问题[^zeller2012rebuttals-e14]；错别字、语言问题这种校对就能解决的，不用在回复里争取[^zeller2012rebuttals-e5]。

动摇结论可信度的问题，要排在最前面 `[本项目分析]`。理由可以参考软件工程领域实证研究的审稿标准：它要求审稿首先看结果是否可信，其次才看是否重要；可信但不那么重要的论文可以录用，不可信的论文看起来再重要也不能录用[^ralph2020empirical-e53]。

**写下来：** 把你收到的意见做成上面那样的表：编号、原话摘要、归类、优先级。标出至少两位审稿人都提到的问题。

## 3. 决定改什么、争什么

表做好后，对每一条做一个决定：**改、解释，还是有理有据地不同意。** 下面的判断规则是我们综合几位计算机研究者的经验整理的 `[本项目分析]`：

- **默认先改。** 与其争论审稿人的建议为什么行不通，不如试一下，也许真的有用[^parikh2020rebuttals-e20]。再不起眼的审稿意见里，也有对你有用的东西[^zeller2012rebuttals-e7]。
- **被误解时，先怪自己的写法。** 一位审稿人误解，可以指出论文里写了什么；如果所有审稿人都误解了，问题不在审稿人[^zeller2012rebuttals-e6]，要回去改写，见[讲清故事，写成论文](01_story-and-paper.md)。
- **不同意时，拿数据说话。** 与其和审稿人争论，不如给出数据支持你的说法[^parikh2020rebuttals-e9]。
- **回应意见背后的担心。** 别只答字面上的问题，也要回应这条意见背后的意图[^parikh2020rebuttals-e18]。比如"为什么没在数据集 Y 上测？"背后，可能是对整体实验是否充分的怀疑；先回答，再提醒大家你已经在哪些数据集上测过。

**哪些批评可以有理有据地不同意？** 有的批评本身就站不住。软件工程领域实证研究的审稿标准列出了一批，例如：

- 说"不新"，却没给出贡献几乎完全相同的已发表文献[^ralph2020empirical-e60]；
- 说"缺细节"，却不指出缺了哪些[^ralph2020empirical-e61]；
- 因为结果是负面的而拒稿[^ralph2020empirical-e41]，或因为是重复研究而拒稿[^ralph2020empirical-e62]；
- 因为审稿人自己会用别的方法或设计而拒稿，或拿该类研究固有的局限来批评[^ralph2020empirical-e25]；
- 要求做与研究目的无关的额外分析（这一条在标准里列为审稿的反面做法）[^ralph2020empirical-e64]。

遇到这类意见，可以礼貌地请审稿人具体指出，或说明它为什么不适用，不要反唇相讥。其他领域没有这样成文的清单时，这些道理也可以借用，但措辞要更谨慎 `[本项目分析]`。

**动摇主张的问题，要认真想：是证据不够，还是话说得太满？** 把主张拆开看：像"总是""完全"这样的全称说法，往往需要分析论证；加了限定的说法（"提升 25%""对某类结构"），常常可以用评估来支撑[^shaw2003writing-e16]。以上面的 R1Q1 为例，你有两条路 `[本项目分析]`：

- **补证据**：查出测试合约里有多少可能出现在训练数据中，去掉这些合约后重新比较；
- **改主张**：把"在真实合约上多发现三成漏洞"改成"在模型训练截止日期之后部署的合约上……"。

改主张不丢人。指导研究生时，讨论过主张和证据之后，学生常会把主张改写得更准确，让它反映研究实际做到的[^shaw2003writing-e17]。但如果改完之后，剩下的结论已经不值得发表，那就不是修改的问题了，见第 6 节 `[本项目分析]`。

**写下来：** 在表里加一列"决定"：改 / 解释 / 不同意（附理由）/ 做不到（附说明）。对每条"不同意"，写出你能拿出的数据或事实。

## 4. 写会议的作者回复

作者回复最初是为了让作者指出审稿意见里的事实错误[^hicks2014response-e1]。不是所有会议都有这一环，有的话规则也各不相同，以目标会议当年的征稿说明为准。

这一节的写法，主要来自几位计算机研究者在博客上分享的个人经验（出处见脚注）。把它们当作建议，不是规定。

**先摆正预期。** 回复救不了一篇差论文；只有论文处在录用边缘，或审稿人犯了明显错误时，它才起作用[^zeller2012rebuttals-e8]。如果大多数审稿人倾向拒稿，回复能起的作用很小[^hicks2014response-e10]。目标不是说服每个人，而是让至少一位审稿人愿意为你争取录用[^hicks2014response-e2]。没有这样一位潜在的支持者，录用的机会很小[^zeller2012rebuttals-e1]。

**想清楚说给谁听。**

- **还没拿定主意的审稿人**，是最值得争取的对象[^zeller2012rebuttals-e11]；
- **支持者**需要你提供论据，好在讨论时反驳反对者[^zeller2012rebuttals-e2]；
- **强烈反对的审稿人**，与其劝他改主意，不如给支持者论据[^zeller2012rebuttals-e12]；
- **做决定的人**：检验标准是，一个中立的第三方只读你的回复、不重读论文和审稿意见，能不能判断问题解决了没有[^parikh2020rebuttals-e4]。

**怎么写：**

1. **初稿先覆盖每一点，再删。** 先不管字数，每一条都写到，再按重要性删减到限制以内[^parikh2020rebuttals-e6]。
2. **开头**：先简要总结审稿人肯定的地方[^parikh2020rebuttals-e13]；最想让大家知道的一件事放在最前面，因为多数人只读开头[^zeller2012rebuttals-e3]。
3. **排顺序**：先答你有把握的大问题，再到没那么明确的问题和小问题[^parikh2020rebuttals-e7]。几位审稿人的相关问题合并回答，节省篇幅[^parikh2020rebuttals-e19]。
4. **每条先引用、再直接回答**：简要引用审稿人的问题，第一句就给答案，再展开[^parikh2020rebuttals-e8]。
5. **论文里已经有的，指出在哪里**[^hicks2014response-e8][^parikh2020rebuttals-e12]。
6. **别只承诺，直接写出来。** 与其说"我们会在论文中讨论某工作"，不如在回复里把讨论写出来[^parikh2020rebuttals-e10]；至少要具体勾勒你会怎么改[^zeller2012rebuttals-e4]。
7. **做不到的如实说**，比如会议不允许补实验[^parikh2020rebuttals-e21]。

还是那个例子，对 R2Q1 的一种写法 `[本项目分析]`：

> **R2Q1：为什么没有和工具 X 比较？**
> 我们补做了比较：在同样的 500 个合约上，工具 X 发现 41 个漏洞，我们的方法发现 58 个（详细结果见下表）。论文初稿没有比较，是因为工具 X 当时只支持旧版编译器；我们已改用它的新版本，修改稿会加入这组结果。

（数字仅为示意。）

**语气。** 要礼貌、表示感谢：审稿人是志愿花时间给你反馈的[^hicks2014response-e3]；特别用心、给了建设性意见的审稿人，要专门谢谢[^parikh2020rebuttals-e22]。争辩可能让审稿人更坚定地反对，找到你们意见一致的地方更有效[^parikh2020rebuttals-e14]。遇到明显不负责任的意见，可以指出来[^parikh2020rebuttals-e15]；但只摆程序委员会主席一分钟内就能核实的事实[^zeller2012rebuttals-e13]。

> **不同的看法：要不要回应每一条意见？**
> - 不必：回复的目标是争取一位支持者，所以不必觉得每条都要回应[^hicks2014response-e4]。
> - 要：反对者提出的每一条都要反驳，给支持者讨论时提供论据[^zeller2012rebuttals-e2]。
>
> 实际操作中 `[本项目分析]`：字数限制严格时，优先保证主要问题和反对者的关键问题，其余一句话带过，并说明会在修改中处理；限制宽松时，逐条回应。

**写下来：** 写一份回复初稿：开头一段总结优点和你最想让大家知道的一件事，然后按第 2 节排好的顺序逐条回答。写完请一位没读过审稿意见的同学只读回复，问他：哪些问题解决了？

## 5. 写期刊的修改稿和回复信

期刊要求修改时，你要交两样东西：改过的论文，和一封逐条说明的回复信。

**要求大修，就认真改，在回复信和正文里回应每一条意见**[^bourne2005published-e2]。和会议回复不同，这里通常没有严格的字数限制，可以逐条写全 `[本项目分析]`。

**回复信的写法** `[本项目分析]`：沿用第 4 节的原则（先引用、再直接回答、拿数据说话），每条意见下按五栏写：

| 每条意见下写 | 例子 |
|---|---|
| 审稿人原话（可以摘要） | R1Q1：测试合约可能出现在训练数据里 |
| 你的回答，第一句给结论 | 我们同意这是一个重要问题，已补做检查 |
| 你做了什么 | 按部署日期筛出模型训练截止后的 300 个合约，重新比较 |
| 结果 | 结论不变，提升幅度从三成降到两成多 |
| 论文改在哪里 | 第 5.2 节第 3 段、表 4，修改处已标色 |

（例子里的数字仅为示意。）

**改正文时，别只改到能应付回复信。** 回复信写"已修改"，正文里要能一眼找到改动 `[本项目分析]`。审稿人提出的问题，你在正文里的回答，也是将来读者会有的疑问。

**一条改动可能牵动全文。** 如果因为 R1Q1 把主张改小了，摘要、引言、结论里的说法都要跟着改，别让新旧说法同时出现 `[本项目分析]`。

**写下来：** 用上面的五栏格式，写出你最重要的三条意见的回复。对每条，标出正文里具体改了哪几处。

## 6. 被拒之后：先重新评估，再决定去哪

**别原样改投别处。** 把被拒的论文一字不改地反复重投，最终会反过来害你[^karpathy2016survival-e11]。把审稿意见整理成待办清单，在修改中逐一解决[^huang2021rejection-e2]。

**先判断问题出在哪一层** `[本项目分析]`：

| 审稿意见的主要问题 | 问题在哪一层 | 怎么办 |
|---|---|---|
| 看不懂、读错了你的贡献 | 写作 | 改写，见[讲清故事，写成论文](01_story-and-paper.md) |
| 和这个会议或期刊关注的方向不合 | 投稿去处 | 改完后换一处更合适的，见[选择发表渠道与投稿](02_venue-and-submission.md) |
| 缺基线、缺实验、分析有漏洞 | 证据 | 补做，见[执行与迭代](../03_conduct-and-analyze/01_run-and-iterate.md) |
| 证据撑不住结论 | 主张 | 把结论改小，或换一种证据，见[从研究问题到证据清单](../02_from-project-to-study/01_question-to-evidence.md) |
| 早有人做过、贡献不够 | 项目本身 | 回到[收敛成项目](../01_from-interest-to-project/03_converge.md#3-别人做过了吗)第 3 节重新定位 |

**如果审稿人一致认为论文质量差，别再争，往前走**：几乎所有这种情况下，审稿人都是对的[^bourne2005published-e2]。这时要认真考虑上表的后两行 `[本项目分析]`。

**改好再投，别急。** 长远看大多数论文并不重要，职业生涯由少数好论文决定[^huang2021rejection-e3]。所以借这次拒稿把论文改扎实，比赶着投下一处更值得 `[本项目分析]`。这次不中，总还有下一个截稿日[^zeller2012rebuttals-e9]。

**改投前，确认上一处已经结束。** 一稿多投的一般规矩见[选择发表渠道与投稿](02_venue-and-submission.md)。被拒前后最容易踩的是这一条：以 USENIX Security '26 的征稿说明为例，即使上一处的初审意见显示很可能被拒，只要论文在那里还算在审，再投过来也算一稿多投[^usenixsec2026cfp-e13]。别处怎么规定，以目标会议或期刊当年的征稿说明为准；拿不准时，先正式撤稿，或等到结果出来 `[本项目分析]`。

**新投稿时，审稿人是新的，但问题可能是旧的。** 上一轮审稿人指出的问题，新的审稿人很可能也会看到。所以不要只挑容易改的改 `[本项目分析]`。

**写下来：** 对这次被拒，用一句话写出"问题主要在哪一层"。列出改投前必须完成的修改，并写下下一个目标去处和它的截止日期。

---

## 关键判断

**改投、大改，还是放下？** 被拒后可以这样判断 `[本项目分析]`：

| 情况 | 通常的做法 |
|---|---|
| 分数接近录用线，意见集中在写作和少量实验 | 改完投下一个合适的截稿日 |
| 审稿人认可问题，但不认可证据 | 补证据或把结论改小，再投 |
| 审稿人一致认为贡献不够或早有人做过 | 回到收敛阶段，重新判断这个项目是否值得继续 |
| 改投了两三次，每次的主要问题都一样 | 问题没有真正解决；和导师一起重新评估主张 |
| 每次的意见都不一样，分数在线附近 | 可能只是运气；继续改、继续投 |

**回复里的"不同意"什么时候值得说？** 当你能拿出数据或事实，并且这条意见会影响录用时。仅仅因为不服气，不值得占篇幅 `[本项目分析]`。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 收到意见当天就写回复 | 情绪还在，容易写成争辩；先休息一天[^huang2021rejection-e6] |
| 没把意见逐条列表 | 容易漏掉问题，也看不出共同问题[^parikh2020rebuttals-e17] |
| 回复只写给审稿人看 | 做决定的人可能只读审稿意见和回复[^parikh2020rebuttals-e2] |
| 只说"谢谢，我们会加上" | 不如直接在回复里写出来[^parikh2020rebuttals-e10] |
| 和审稿人争吵 | 可能让审稿人更坚定地反对[^parikh2020rebuttals-e14] |
| 所有审稿人都误解了，却怪审稿人 | 问题在论文的写法[^zeller2012rebuttals-e6] |
| 被拒后原样改投 | 最终会反过来害你[^karpathy2016survival-e11] |
| 上一处还在审，就投了下一处 | 至少在 USENIX Security '26 算一稿多投[^usenixsec2026cfp-e13] |
| 只改容易的，回避动摇主张的问题 | 下一轮审稿人很可能提同样的问题 `[本项目分析]` |

## 产出物

- 审稿意见表：编号、摘要、归类、优先级、决定（第 2、3 节）
- 作者回复，或期刊回复信和修改稿（第 4、5 节）
- 被拒时：一句话的诊断、改投前的修改清单、下一个目标去处（第 6 节）

## 检查点

满足下面几条，这一轮就算完成：

- [ ] 每条意见都在表里，有归类和决定
- [ ] 几位审稿人的共同问题，放在了回复最前面
- [ ] 每条回答都先引用问题、再直接回答
- [ ] 只读回复的人，也能判断问题是否已解决
- [ ] 动摇主张的问题，要么补了证据，要么改了主张，全文说法一致
- [ ] 改投前确认上一处已经结束，修改清单上的事都做完了

## 回退信号

| 出现这种情况 | 回到哪里 |
|---|---|
| 所有审稿人都没看懂你的贡献 | [讲清故事，写成论文](01_story-and-paper.md) |
| 审稿人认可问题，但认为证据撑不住结论 | [效度与局限：设计阶段就想清楚](../02_from-project-to-study/03_validity-and-limits.md)，或[从研究问题到证据清单](../02_from-project-to-study/01_question-to-evidence.md) |
| 需要补的实验，暴露了分析里的错误 | [分析与解读](../03_conduct-and-analyze/02_analyze-and-interpret.md) |
| 审稿人一致认为早有人做过，或贡献不够 | [收敛成项目](../01_from-interest-to-project/03_converge.md#3-别人做过了吗)第 3 节 |
| 改投几次，每次都卡在同一个问题上 | [收敛成项目](../01_from-interest-to-project/03_converge.md#1-写出你想证明的那句话)第 1 节，重新想要证明的那句话 |

## 下一步

论文录用了，或者你决定放下这一篇，主线就走到了终点。

被拒、改、再投，在研究里很常见。怎样长期保持动力、积累经验，见[心态与长期积累](../08_throughout/mindset_and_growth.md)。

做下一个项目时，从[找到候选问题](../01_from-interest-to-project/02_find-problems.md)重新出发。这一轮审稿人问得最多的问题，往往能告诉你下一个项目该在哪里多下功夫。 `[本项目分析]`

[^bourne2005published-e1]: Bourne 2005，Rule 5。[证据](../../sources/notes/bourne2005published.md#e1)
[^bourne2005published-e2]: Bourne 2005，Rule 5。[证据](../../sources/notes/bourne2005published.md#e2)
[^huang2021rejection-e2]: Jia-Bin Huang 2021，第 4 条（It's not personal）。[证据](../../sources/notes/huang2021rejection.md#e2)
[^huang2021rejection-e3]: Jia-Bin Huang 2021，第 5 条（It doesn't matter much）。[证据](../../sources/notes/huang2021rejection.md#e3)
[^huang2021rejection-e6]: Jia-Bin Huang 2021，第 2 条（It's okay to be upset）。[证据](../../sources/notes/huang2021rejection.md#e6)
[^ralph2020empirical-e53]: SIGSOFT General Standard，Good Review Practices。[证据](../../sources/notes/ralph2020empirical.md#e53)
[^ralph2020empirical-e25]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e41]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e60]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e60)
[^ralph2020empirical-e61]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e61)
[^shaw2003writing-e16]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e17]: Shaw 2003，§5。[证据](../../sources/notes/shaw2003writing.md#e17)
[^hicks2014response-e1]: Hicks 2014（作者回复），What is author response?。[证据](../../sources/notes/hicks2014response.md#e1)
[^hicks2014response-e10]: Hicks 2014（作者回复），The goal of your response。[证据](../../sources/notes/hicks2014response.md#e10)
[^hicks2014response-e2]: Hicks 2014（作者回复），The goal of your response。[证据](../../sources/notes/hicks2014response.md#e2)
[^hicks2014response-e3]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../sources/notes/hicks2014response.md#e3)
[^hicks2014response-e4]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../sources/notes/hicks2014response.md#e4)
[^hicks2014response-e5]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../sources/notes/hicks2014response.md#e5)
[^hicks2014response-e7]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../sources/notes/hicks2014response.md#e7)
[^hicks2014response-e8]: Hicks 2014（作者回复），General themes for writing the response。[证据](../../sources/notes/hicks2014response.md#e8)
[^karpathy2016survival-e11]: Karpathy 2016，Closing thoughts。[证据](../../sources/notes/karpathy2016survival.md#e11)
[^neurips2025cfp-e8]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../sources/notes/neurips2025cfp.md#e8)
[^neurips2025cfp-e11]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../sources/notes/neurips2025cfp.md#e11)
[^neurips2025cfp-e13]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../sources/notes/neurips2025cfp.md#e13)
[^parikh2020rebuttals-e2]: Parikh、Batra & Lee 2020，谁读回复。[证据](../../sources/notes/parikh2020rebuttals.md#e2)
[^parikh2020rebuttals-e4]: Parikh、Batra & Lee 2020，谁读回复。[证据](../../sources/notes/parikh2020rebuttals.md#e4)
[^parikh2020rebuttals-e5]: Parikh、Batra & Lee 2020，写作流程。[证据](../../sources/notes/parikh2020rebuttals.md#e5)
[^parikh2020rebuttals-e17]: Parikh、Batra & Lee 2020，写作流程。[证据](../../sources/notes/parikh2020rebuttals.md#e17)
[^parikh2020rebuttals-e6]: Parikh、Batra & Lee 2020，写作流程。[证据](../../sources/notes/parikh2020rebuttals.md#e6)
[^parikh2020rebuttals-e13]: Parikh、Batra & Lee 2020，Tip 1。[证据](../../sources/notes/parikh2020rebuttals.md#e13)
[^parikh2020rebuttals-e7]: Parikh、Batra & Lee 2020，Tip 2。[证据](../../sources/notes/parikh2020rebuttals.md#e7)
[^parikh2020rebuttals-e8]: Parikh、Batra & Lee 2020，Tip 3。[证据](../../sources/notes/parikh2020rebuttals.md#e8)
[^parikh2020rebuttals-e18]: Parikh、Batra & Lee 2020，Tip 5。[证据](../../sources/notes/parikh2020rebuttals.md#e18)
[^parikh2020rebuttals-e12]: Parikh、Batra & Lee 2020，Tip 9。[证据](../../sources/notes/parikh2020rebuttals.md#e12)
[^parikh2020rebuttals-e19]: Parikh、Batra & Lee 2020，Tip 10。[证据](../../sources/notes/parikh2020rebuttals.md#e19)
[^parikh2020rebuttals-e9]: Parikh、Batra & Lee 2020，Tip 12。[证据](../../sources/notes/parikh2020rebuttals.md#e9)
[^parikh2020rebuttals-e10]: Parikh、Batra & Lee 2020，Tip 13。[证据](../../sources/notes/parikh2020rebuttals.md#e10)
[^parikh2020rebuttals-e20]: Parikh、Batra & Lee 2020，Tip 14。[证据](../../sources/notes/parikh2020rebuttals.md#e20)
[^parikh2020rebuttals-e21]: Parikh、Batra & Lee 2020，Tip 15。[证据](../../sources/notes/parikh2020rebuttals.md#e21)
[^parikh2020rebuttals-e15]: Parikh、Batra & Lee 2020，Tip 16。[证据](../../sources/notes/parikh2020rebuttals.md#e15)
[^parikh2020rebuttals-e22]: Parikh、Batra & Lee 2020，Tip 17。[证据](../../sources/notes/parikh2020rebuttals.md#e22)
[^parikh2020rebuttals-e14]: Parikh、Batra & Lee 2020，Tip 18。[证据](../../sources/notes/parikh2020rebuttals.md#e14)
[^usenixsec2026cfp-e13]: USENIX Security '26 征稿启事，Simultaneous Submission and Plagiarism。[证据](../../sources/notes/usenixsec2026cfp.md#e13)
[^usenixsec2026cfp-e14]: USENIX Security '26 征稿启事，Summary of main changes from previous editions。[证据](../../sources/notes/usenixsec2026cfp.md#e14)
[^zeller2012rebuttals-e1]: Zeller 2012，Identify the champion.。[证据](../../sources/notes/zeller2012rebuttals.md#e1)
[^zeller2012rebuttals-e11]: Zeller 2012，Identify the undecided.。[证据](../../sources/notes/zeller2012rebuttals.md#e11)
[^zeller2012rebuttals-e12]: Zeller 2012，Identify the detractors.。[证据](../../sources/notes/zeller2012rebuttals.md#e12)
[^zeller2012rebuttals-e2]: Zeller 2012，Arm the champion.。[证据](../../sources/notes/zeller2012rebuttals.md#e2)
[^zeller2012rebuttals-e13]: Zeller 2012，Write for the PC chair.。[证据](../../sources/notes/zeller2012rebuttals.md#e13)
[^zeller2012rebuttals-e6]: Zeller 2012，Write for the PC chair.。[证据](../../sources/notes/zeller2012rebuttals.md#e6)
[^zeller2012rebuttals-e3]: Zeller 2012，Write for the committee.。[证据](../../sources/notes/zeller2012rebuttals.md#e3)
[^zeller2012rebuttals-e4]: Zeller 2012，Convince.。[证据](../../sources/notes/zeller2012rebuttals.md#e4)
[^zeller2012rebuttals-e14]: Zeller 2012，Choose comments wisely.。[证据](../../sources/notes/zeller2012rebuttals.md#e14)
[^zeller2012rebuttals-e5]: Zeller 2012，Choose comments wisely.。[证据](../../sources/notes/zeller2012rebuttals.md#e5)
[^zeller2012rebuttals-e7]: Zeller 2012，Thank the reviewers.。[证据](../../sources/notes/zeller2012rebuttals.md#e7)
[^zeller2012rebuttals-e8]: Zeller 2012，Don't expect too much.。[证据](../../sources/notes/zeller2012rebuttals.md#e8)
[^zeller2012rebuttals-e9]: Zeller 2012，Don't expect too much.。[证据](../../sources/notes/zeller2012rebuttals.md#e9)
[^zeller2012rebuttals-e10]: Zeller 2012，Organize your rebuttal.。[证据](../../sources/notes/zeller2012rebuttals.md#e10)
[^ralph2020empirical-e62]: SIGSOFT General Standard，Invalid Criticisms。[证据](../../sources/notes/ralph2020empirical.md#e62)
[^ralph2020empirical-e64]: SIGSOFT General Standard，Reviewing Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e64)
