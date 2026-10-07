# 科研诚信与伦理

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本页的道理适用于各学科，例子和具体做法以计算机为例。下面引用的规范各有出处和适用范围（欧洲的准则、某个学科的标准、某个会议某一年的规定），引用时都写明了；你自己的研究，以所在机构、学科和投稿处的规定为准。

## 什么时候需要这一页

- 你想知道哪些事绝对不能做，哪些事"不违规"却会让结果不可信；
- 你的研究会接触人、收集人的数据，或者可能伤害到别人，比如在真实部署的智能合约上发现漏洞；
- 你要用大模型帮忙写论文或做实验，或者发现自己已发表的论文有错。

---

## 1. 先认清红线：伪造、篡改、剽窃

**怎么做：** 《欧洲科研诚信行为准则》（欧洲科学与人文学院联合会制定，下面简称"欧洲准则"）沿用了学术不端的三种传统类型[^allea2023european-e3]。把它们当作任何情况下都不能碰的底线：

| 类型 | 含义 | 计算机里的样子 |
|---|---|---|
| 伪造 | 编造数据或结果，当作真的记录下来 | 没跑过的实验填上数字 |
| 篡改 | 操纵材料、设备、图像或流程；或无正当理由地改动、删除、隐瞒数据或结果 | 删掉对自己方法不利的那几次运行 |
| 剽窃 | 使用别人的成果或想法，却不恰当注明出处 | 把别人的代码或段落直接放进自己的论文 |

"计算机里的样子"一栏是本项目举的例子 `[本项目分析]`。

欧洲准则还列出了这三种之外同样不可接受的做法，例如：滥用统计，制造"显著"的假象；无正当理由扣留数据或结果；选择性或不准确地引用[^allea2023european-e4]；为了多发论文，把一项研究拆成几篇，俗称"切香肠"；重复发表自己以前论文的实质内容（包括翻译成另一种语言再发）却不注明[^allea2023european-e5]；操纵署名，贬低别人的贡献[^allea2023european-e9]；起草论文时隐瞒用了人工智能或自动化工具[^allea2023european-e19]。软件工程的实证研究标准也把"切香肠"列为反面做法[^ralph2020empirical-e67]。

**为什么：** 按欧洲准则的说法，这些行为破坏研究过程和研究者之间的关系，削弱人们对研究的信任，浪费资源，还可能让参与者、社会或环境受到不必要的伤害[^allea2023european-e6]。这份准则虽然是欧洲的，但写明适用于所有学科领域[^allea2023european-e18]，拿来认红线很合适 `[本项目分析]`。

**容易错在哪：** 以为只有"编数据"才算不端。"悄悄丢掉不利的结果"听起来像是整理数据，其实可能已经属于篡改[^allea2023european-e3]。

**写下来：** 对照上表，想一想你现在的项目里，哪一步最可能被诱惑"稍微处理一下"（比如挑运行结果、删异常样本）。写下你打算怎么记录这一步，让别人能看到你做了什么。

## 2. 对证据诚实：不骗自己，报告全部结果

**怎么做：**

- 和你的结论不一致的事实，跟一致的事实一起写出来[^feynman1974cargo-e4]。
- 决定检验一个想法时，就决定无论结果如何都报告。只发表某一类结果，论证就会显得比实际更好[^feynman1974cargo-e9]。
- 检查要对称：结果"不好"时你会到处找错，结果"好"时也要用同样的力度去查。物理学史上就有这样的教训：后来的人测出的数值偏离权威结果时拼命找原因，接近时就不怎么查了[^feynman1974cargo-e14]。
- 方法里有随机性时，报告所有运行的结果，不要一遍遍重跑、只报最好的那次[^zeller2021devil-e1]；和别人的方法比较时，给对方同样的调参机会[^zeller2021devil-e2]。（这两条是计算机实验的例子。）
- 推测可以写，但要和有证据的结论分开，单独标明[^lipton2019troubling-e1][^lipton2019troubling-e3]。

**为什么：** 科学诚信的第一条，是不要骗自己，而你自己恰恰是最容易被骗的人[^feynman1974cargo-e7]。欧洲准则也指出，负面结果和正面结果一样，可能值得发表和传播[^allea2023european-e12]；软件工程的实证研究标准把"因为结果是负面的就拒稿"列为不成立的审稿意见[^ralph2020empirical-e41]。

**容易错在哪：**

- 只报告"显著"的统计检验（俗称"p 值操纵"）；或者在声称是事先提出假设、再收集数据检验的研究里，看完结果再把假设写成像是事先就有的。软件工程的实证研究标准把这两种都列为反面做法[^ralph2020empirical-e27]。
- 写了局限，结论却当局限不存在[^ralph2020empirical-e66]。
- 把"不违规"当成"没问题"。不预注册（事先公开登记研究计划）、不记实验日志、不留版本历史、不测试代码、不验证结果、什么都不共享，这些都不算学术不端[^zeller2021devil-e8]，但会让你的结果没法让人相信 `[本项目分析]`。

这种错误谁都会犯，批评这种做法的作者也承认自己写过"伪装成解释的推测"[^lipton2019troubling-e12]。

具体怎么做分析、怎么区分探索性和验证性的结论、怎么写局限，见[分析与解读](../03_conduct-and-analyze/02_analyze-and-interpret.md)。

**写下来：** 列出你目前所有的实验运行，包括失败的、不好看的。在旁边写一句：如果审稿人看到这张完整清单，你的结论还站得住吗？

## 3. 让别人能核查你的工作

**怎么做：**

- 报告方法时，在适用的情况下写到别人能核查或重复的程度[^allea2023european-e14]。
- 在合理且写明的期限内，妥善保存数据、代码、实验方案等研究材料[^allea2023european-e15]。
- 发表时公开数据和代码：存到能分配 DOI（数字对象标识符，一种不会随网址变化而失效的永久编号）的可靠仓库，并写明许可协议[^wilson2017good-e4][^sandve2013ten-e6]。
- 不能公开的，说明原因。欧洲准则的原则是"尽可能开放，必要时封闭"[^allea2023european-e15]；软件工程的开放科学标准写明，有伦理、法律等方面的障碍时可以不公开[^ralph2020empirical-e76]，说明原因即可[^ralph2020empirical-e77]。

**为什么：** 可复现不只是对学术界的责任，做不到可复现也会拖累你自己[^sandve2013ten-e1]：如果回不到产生某个结果的那版代码，你就没法判断这个结果是不是程序错误造成的[^sandve2013ten-e4]。让同行真的能复现，本身就是质量和可信的有力信号[^sandve2013ten-e6]。

**容易错在哪：** 以为放在 GitHub 或网盘上就算公开了。软件工程的开放科学标准指出，个人网站、GitHub、网盘都不算妥善的长期存档[^ralph2020empirical-e78]。可以考虑 Zenodo（一个免费的科研成果存档平台）、OSF（开放科学框架）或所在机构的仓库 `[本项目分析]`。

日常怎么记录每个结果的来历、怎么保存和备份原始数据（包括实验记录本、问卷、访谈录音这类非计算材料），见[整理科研材料](organizing_materials.md)。

**写下来：** 列出论文要用到的数据、代码和其他材料，逐项写下：打算公开到哪里、用什么许可协议；不能公开的，写一句原因。

## 4. 研究涉及人或可能伤害别人时，先保护人

《Menlo 报告》指出，信息与通信技术的发展拉开了"研究者能做什么"和"应该做什么"之间的距离[^bailey2012menlo-e1]。所以不只是医学和心理学，任何会接触人、收集人的数据、或者可能影响别人的研究，都要先想伦理 `[本项目分析]`。

**怎么做：**

1. **越早考虑越好**，在设计阶段就想，不要等论文写完再补一段伦理说明。安全会议 USENIX Security '26 的伦理指南就建议"在研究过程中尽早"考虑[^usenixsec2026cfp-e9]。
2. **先查所在学科和机构的规定，看要不要过伦理审查。** 以心理学为例，美国心理学会的伦理准则要求：需要机构审批时，研究开始前如实提交方案、获得批准，并按批准的方案执行[^apa2017ethical-e2]。软件工程的伦理补充标准把"论文写明是哪个伦理审查委员会批准的，并附批准编号"列为加分项[^ralph2020empirical-e73]。不同国家、学科、机构的规定差别很大，具体要求见各学科的领域概况，例如[计算机](../07_fields/computer-science/README.md#伦理问题有本领域的特点)、[心理学](../07_fields/psychology/README.md#伦理美国心理学会伦理准则与机构审批)、[临床医学](../07_fields/clinical-medicine/README.md#研究对象是人伦理排在第一位)、[教育学](../07_fields/education/README.md#伦理未成年人守门人和研究自己的学生)、[社会学](../07_fields/sociology/README.md#伦理美国社会学会准则与英国社会学会声明)、[媒体与传播](../07_fields/media-communication/README.md#网络和社交媒体研究的伦理)。
3. **用一个框架逐条检查。** 计算机安全方向可以用《Menlo 报告》，这是美国一份面向信息与通信技术研究的伦理原则报告；USENIX Security '26 强烈建议作者熟悉它[^usenixsec2026cfp-e10]。它沿用了《贝尔蒙报告》（保护人体研究对象的伦理原则和指南[^bailey2012menlo-e7]）的三条原则，又加了一条[^bailey2012menlo-e2]：

| 原则 | 具体要求 |
|---|---|
| 尊重个人 | 参与是自愿的，以知情同意为前提；不是研究对象、但会受研究影响的人，也要保护[^bailey2012menlo-e3] |
| 有益 | 避免伤害；尽量增大收益、减小伤害；系统地评估风险和收益[^bailey2012menlo-e4] |
| 公正 | 公平选择研究对象，负担在受影响的人之间公平分配[^bailey2012menlo-e5] |
| 尊重法律和公共利益 | 做法律上的尽职调查；方法和结果透明；对自己的行为负责[^bailey2012menlo-e6] |

4. **论文里写清楚。** 软件工程的伦理补充标准要求，有人参与的研究写出：参与者可能面临哪些风险，采取了哪些措施减轻，研究收益为什么值得这些风险[^ralph2020empirical-e68]；怎样招募、给了什么报酬、怎样避免强迫、怎样取得自由的知情同意[^ralph2020empirical-e69]；怎样保护隐私，包括别人把多个数据来源拼起来、重新认出参与者的可能[^ralph2020empirical-e70]。欧洲准则还要求事先告诉参与者，他们的数据将怎样使用、存储和删除[^allea2023european-e17]。

用"大模型与智能合约安全"举例 `[本项目分析]`：

- 请开发者试用你的工具、做访谈：这是有人参与的研究，要先查清要不要过伦理审查，并取得知情同意。
- 在真实部署的合约上发现了漏洞：要先私下告知负责方，再公开。USENIX Security '26 的伦理指南指出，在私下告知、漏洞得到缓解之前就公开，会让人受到伤害[^usenixsec2026cfp-e5]；它要求论文写清向谁披露了、结果如何[^usenixsec2026cfp-e6]。

**为什么：** 风险不只落在参与者身上，也可能落在研究的应用、社会和环境上，同样要识别、权衡、减轻[^allea2023european-e16][^ralph2020empirical-e65]。USENIX Security '26 的伦理指南甚至说，有时最合乎伦理的选择是不做这项研究，或做完了不发表[^usenixsec2026cfp-e8]。

**容易错在哪：**

- 用"研究总体上是有益的"为风险辩护，而不是论证"这项研究"的具体收益；招募时淡化风险。软件工程的伦理补充标准把这些列为反面做法[^ralph2020empirical-e71]。
- 以为伦理审查批准了就万事大吉。USENIX Security '26 的伦理指南提醒，审查委员会不一定了解计算机安全研究的惯例，批准了也仍然要自己分析伦理问题[^usenixsec2026cfp-e7]。
- 研究必须用到欺骗（如不告诉参与者真实目的）时，就不写知情同意。软件工程的伦理补充标准允许这时调整知情同意的写法，但欺骗本身必须在论文里完整说明[^ralph2020empirical-e72]。

> **不同的看法：守法和伦理冲突时怎么办？**
>
> - **以守法为原则**：美国的《Menlo 报告》要求研究者做法律上的尽职调查[^bailey2012menlo-e6]；欧洲准则要求遵守相关的准则、指南和法规[^allea2023european-e16]。
> - **伦理和合法性一起权衡**：软件工程的伦理补充标准认为，极少数情况下，合乎伦理的研究可能需要违法的行为；像 Menlo 这样的框架把守法纳入考虑，正是为了把伦理性和合法性放在一起权衡[^ralph2020empirical-e75]。
>
> 实际操作：新手默认守法，并走完所在机构的伦理审查。遇到灰色地带，先找导师和伦理委员会商量，不要自己判断 `[本项目分析]`。

**写下来：** 列出你的研究会接触到的所有人，包括不是研究对象、但可能受影响的人（比如合约的部署者和用户）。对每一类人，写一句：他们可能受到什么伤害，你打算怎么减轻。

## 5. 署名、引用和利益冲突：给每个贡献者应得的认可

**怎么做：**

- **署名**：谁该署名、谁进致谢、顺序怎么定、什么时候谈，见[合作与导师](collaboration_and_advisors.md#6-署名开工时就谈并随进展调整)。这里只记住一条红线：欧洲准则把操纵署名、贬低别人的贡献列为不可接受的做法[^allea2023european-e9]。
- **用了别人的想法、数据、代码或文字，都注明出处**，否则就是剽窃[^allea2023european-e3]。引用要准确，不要只引对自己有利的文献[^allea2023european-e4]。
- **披露利益冲突和资助来源**，包括经济的和非经济的[^allea2023european-e10]。

**容易错在哪：** 匿名投稿时注释掉了致谢和作者信息，公开发布时忘了恢复。发布前核对作者是否列全、姓名和单位是否正确、致谢是否恢复[^carlini2022checklist-e2]。每犯一次这类错误，就把它加进自己的发布清单[^carlini2022checklist-e1]。

**写下来：** 列出论文里用到的别人的代码、数据、想法和图，逐项核对是否注明了出处；再列出项目的资助来源和你可能有的利益冲突。

## 6. 用大模型等工具时，责任仍然在你

各家对大模型的规定不同、也在变。下面用两份规定举例：NeurIPS 2025（机器学习方向的一个顶级会议）的大模型使用政策，和国际医学期刊编辑委员会为医学期刊制定的规范。

**怎么做：**

- **大模型不能当作者。** NeurIPS 2025 规定只有人能当作者，不管用了什么工具，作者都要对论文的全部内容负责，包括文字、图和方法[^neurips2025llm-e6]。医学期刊的规范给出的理由是：工具不能对工作的准确、诚信和原创负责，而这些是署名的前提[^icmje2026recommendations-e29]。
- **逐条核对它生成的东西。** 大模型的输出听起来很权威，却可能错误、不完整或有偏差[^icmje2026recommendations-e31]。尤其是参考文献：用大模型生成的文献却不核实是否存在、是否正确、是否切题，在 NeurIPS 2025 被列为违规的例子，可能被撤销发表资格[^neurips2025llm-e7]。
- **大模型是方法的一部分时，写进方法。** NeurIPS 2025 要求，大模型是方法中重要、原创或非标准的部分时，在实验设置里写清楚[^neurips2025llm-e5]；医学期刊的规范要求写到别人能重复的程度，包括工具、版本，适用时还有提示词[^icmje2026recommendations-e32]。"大模型与智能合约安全"这类研究，大模型本身就是研究对象，这一条尤其要做到 `[本项目分析]`。
- **不要把别人的数据喂给工具。** 有些工具会保留输入的数据用于训练，NeurIPS 2025 提醒作者注意个人隐私[^neurips2025llm-e9]。将来当审稿人时，稿件同样不能交给大模型，见[当审稿人](being_a_reviewer.md)。

> **不同的看法：只用大模型润色文字，要不要声明？**
>
> - **不用声明**：NeurIPS 2025 的政策是，只用于写作、编辑或排版，不影响方法、严谨性和原创性的，不需要在论文里声明[^neurips2025llm-e8]。
> - **要声明**：医学期刊的规范要求，用人工智能辅助写作，要在致谢里说明[^icmje2026recommendations-e30]；不披露可能需要更正，某些情况下可能被认定为不端[^icmje2026recommendations-e33]。欧洲准则把起草论文时隐瞒使用人工智能列为不可接受的做法[^allea2023european-e19]。
>
> 实际操作：投稿前读目标会议或期刊自己的政策，按它的要求做；拿不准时，写明用了什么、用来做什么 `[本项目分析]`。

**写下来：** 列出你在这个项目里用到大模型的每个环节（找文献、写代码、做实验、改文字）。对每一项，写下你怎么核对了它的输出，以及目标会议或期刊是否要求声明。

## 7. 发现错误，主动更正

**怎么做：** 发现自己发表的论文有错，及时发更正，必要时撤稿[^allea2023european-e11]。对外介绍研究时，说清证据有多可靠、还有哪些不确定之处[^allea2023european-e13]。

**为什么：** 欧洲准则对不端的定义是伪造、篡改和剽窃[^allea2023european-e3]；照这个定义，诚实的错误本身不算不端，主动更正也不丢人 `[本项目分析]`。准则还要求，作者在发表后主动发更正，应当得到认可[^allea2023european-e20]。

**容易错在哪：** 怕丢面子，想等"下一篇论文里顺便改掉"。别人在这期间可能已经在你的错误结果上继续工作了 `[本项目分析]`。

**写下来：** 假设明天发现论文里一个关键数字算错了。写下你会先告诉谁（导师、合作者、编辑或会议主席），以及怎么判断是发更正还是撤稿 `[本项目分析]`。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 以为只有编数据才算不端 | 无正当理由删除或隐瞒结果属于篡改[^allea2023european-e3] |
| 多次运行只报告最好的一次 | 挑出来的结果不代表方法的真实表现[^zeller2021devil-e1] |
| 结果不好时拼命找错，结果好时不查 | 不对称的检查会让错误结论留下来[^feynman1974cargo-e14] |
| 写了局限，结论照旧夸大 | 局限形同虚设[^ralph2020empirical-e66] |
| 数据和代码只放在 GitHub 或网盘上 | 不算妥善的长期存档[^ralph2020empirical-e78] |
| 用"研究总体有益"为参与者的风险辩护 | 要论证的是这项研究的具体收益[^ralph2020empirical-e71] |
| 伦理审查批准了就不再想伦理 | 批准不等于没有伦理问题[^usenixsec2026cfp-e7] |
| 发现漏洞后直接写进论文公开 | 修复之前公开会让人受到伤害[^usenixsec2026cfp-e5] |
| 给没有实质贡献的人署名，或漏掉有贡献的人 | 操纵署名属于不可接受的做法[^allea2023european-e9] |
| 把一项研究拆成几篇发表 | "切香肠"，属于不可接受的做法[^allea2023european-e5] |
| 直接用大模型给的参考文献 | 可能根本不存在；在 NeurIPS 2025 属于违规[^neurips2025llm-e7] |
| 把大模型列为作者 | 工具不能对工作负责，不能署名[^icmje2026recommendations-e29] |

"为什么是问题"一栏是本项目的概括，脚注指向相关的规定或例子，出处和适用范围见正文 `[本项目分析]`。

## 延伸阅读

- **Feynman，"Cargo Cult Science"**：一篇短演讲，讲清"不要骗自己"和"无论结果如何都发表"，适合入门时读。
- **欧洲科学与人文学院联合会，《欧洲科研诚信行为准则》2023 修订版**：写明适用于所有学科，要查"什么算不端"时看它。
- **Sandve 等人 2013；Wilson 等人 2017**：可复现和数据管理的具体做法，都很短，可以直接照着做。
- **Bailey 等人 2012（Menlo 报告介绍）与软件工程实证标准的伦理补充标准**：设计有人参与的研究、写伦理部分时用。
- **Zeller，"The Devil's Guide to Incremental Research"**：用反讽列出常见的可疑做法，适合拿来对照检查自己。
- **目标会议或期刊的大模型使用政策**，例如 NeurIPS 2025 的政策：投稿前必读，各家要求不一样。

[^allea2023european-e3]: ALLEA 2023，§3.1。[证据](../../sources/notes/allea2023european.md#e3)
[^allea2023european-e4]: ALLEA 2023，§3.1。[证据](../../sources/notes/allea2023european.md#e4)
[^allea2023european-e5]: ALLEA 2023，§3.1。[证据](../../sources/notes/allea2023european.md#e5)
[^allea2023european-e6]: ALLEA 2023，§3。[证据](../../sources/notes/allea2023european.md#e6)
[^allea2023european-e9]: ALLEA 2023，§3.1。[证据](../../sources/notes/allea2023european.md#e9)
[^allea2023european-e10]: ALLEA 2023，§2.7。[证据](../../sources/notes/allea2023european.md#e10)
[^allea2023european-e11]: ALLEA 2023，§2.7。[证据](../../sources/notes/allea2023european.md#e11)
[^allea2023european-e12]: ALLEA 2023，§2.7。[证据](../../sources/notes/allea2023european.md#e12)
[^allea2023european-e13]: ALLEA 2023，§2.7。[证据](../../sources/notes/allea2023european.md#e13)
[^allea2023european-e14]: ALLEA 2023，§2.3。[证据](../../sources/notes/allea2023european.md#e14)
[^allea2023european-e15]: ALLEA 2023，§2.5。[证据](../../sources/notes/allea2023european.md#e15)
[^allea2023european-e16]: ALLEA 2023，§2.4。[证据](../../sources/notes/allea2023european.md#e16)
[^allea2023european-e17]: ALLEA 2023，§2.5。[证据](../../sources/notes/allea2023european.md#e17)
[^allea2023european-e18]: ALLEA 2023，Preamble。[证据](../../sources/notes/allea2023european.md#e18)
[^allea2023european-e19]: ALLEA 2023，§3.1。[证据](../../sources/notes/allea2023european.md#e19)
[^allea2023european-e20]: ALLEA 2023，§2.7。[证据](../../sources/notes/allea2023european.md#e20)
[^feynman1974cargo-e4]: Feynman 1974，"Details that could throw doubt" 段。[证据](../../sources/notes/feynman1974cargo.md#e4)
[^feynman1974cargo-e7]: Feynman 1974，"The first principle" 段。[证据](../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e9]: Feynman 1974，"One example of the principle" 段。[证据](../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e14]: Feynman 1974，Millikan 油滴实验的例子。[证据](../../sources/notes/feynman1974cargo.md#e14)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019，§1。[证据](../../sources/notes/lipton2019troubling.md#e1)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019，§3.1。[证据](../../sources/notes/lipton2019troubling.md#e3)
[^lipton2019troubling-e12]: Lipton & Steinhardt 2019，§3.1。[证据](../../sources/notes/lipton2019troubling.md#e12)
[^zeller2021devil-e1]: Zeller 2021，THE CHERRY SHUFFLE。[证据](../../sources/notes/zeller2021devil.md#e1)
[^zeller2021devil-e2]: Zeller 2021，THE AUTOTUNE。[证据](../../sources/notes/zeller2021devil.md#e2)
[^zeller2021devil-e8]: Zeller 2021，倒数第三段。[证据](../../sources/notes/zeller2021devil.md#e8)
[^ralph2020empirical-e27]: SIGSOFT General Standard，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e41]: SIGSOFT General Standard，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e65]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e65)
[^ralph2020empirical-e66]: SIGSOFT General Standard，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e67]: SIGSOFT General Standard，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e67)
[^ralph2020empirical-e68]: SIGSOFT 伦理补充标准（有人参与的研究），必要项。[证据](../../sources/notes/ralph2020empirical.md#e68)
[^ralph2020empirical-e69]: SIGSOFT 伦理补充标准（有人参与的研究），必要项。[证据](../../sources/notes/ralph2020empirical.md#e69)
[^ralph2020empirical-e70]: SIGSOFT 伦理补充标准（有人参与的研究），必要项脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e70)
[^ralph2020empirical-e71]: SIGSOFT 伦理补充标准（有人参与的研究），反面模式。[证据](../../sources/notes/ralph2020empirical.md#e71)
[^ralph2020empirical-e72]: SIGSOFT 伦理补充标准（有人参与的研究），可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e72)
[^ralph2020empirical-e73]: SIGSOFT 伦理补充标准（有人参与的研究），加分项。[证据](../../sources/notes/ralph2020empirical.md#e73)
[^ralph2020empirical-e75]: SIGSOFT 伦理补充标准（有人参与的研究），Note。[证据](../../sources/notes/ralph2020empirical.md#e75)
[^ralph2020empirical-e76]: SIGSOFT 开放科学补充标准，Principle。[证据](../../sources/notes/ralph2020empirical.md#e76)
[^ralph2020empirical-e77]: SIGSOFT 开放科学补充标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e77)
[^ralph2020empirical-e78]: SIGSOFT 开放科学补充标准，Notes。[证据](../../sources/notes/ralph2020empirical.md#e78)
[^sandve2013ten-e1]: Sandve 等人 2013，引言。[证据](../../sources/notes/sandve2013ten.md#e1)
[^sandve2013ten-e4]: Sandve 等人 2013，Rule 4。[证据](../../sources/notes/sandve2013ten.md#e4)
[^sandve2013ten-e6]: Sandve 等人 2013，Rule 10。[证据](../../sources/notes/sandve2013ten.md#e6)
[^wilson2017good-e4]: Wilson 等人 2017，Box 1。[证据](../../sources/notes/wilson2017good.md#e4)
[^bailey2012menlo-e1]: Bailey 等人 2012，第 71 页。[证据](../../sources/notes/bailey2012menlo.md#e1)
[^bailey2012menlo-e2]: Bailey 等人 2012，第 72 页。[证据](../../sources/notes/bailey2012menlo.md#e2)
[^bailey2012menlo-e3]: Bailey 等人 2012，第 72–73 页。[证据](../../sources/notes/bailey2012menlo.md#e3)
[^bailey2012menlo-e4]: Bailey 等人 2012，第 72 页。[证据](../../sources/notes/bailey2012menlo.md#e4)
[^bailey2012menlo-e5]: Bailey 等人 2012，第 73 页。[证据](../../sources/notes/bailey2012menlo.md#e5)
[^bailey2012menlo-e6]: Bailey 等人 2012，第 73 页。[证据](../../sources/notes/bailey2012menlo.md#e6)
[^bailey2012menlo-e7]: Bailey 等人 2012，第 74 页参考文献 3。[证据](../../sources/notes/bailey2012menlo.md#e7)
[^apa2017ethical-e2]: 美国心理学会伦理准则，8.01。[证据](../../sources/notes/apa2017ethical.md#e2)
[^usenixsec2026cfp-e5]: USENIX Security '26 伦理指南，Disclosures。[证据](../../sources/notes/usenixsec2026cfp.md#e5)
[^usenixsec2026cfp-e6]: USENIX Security '26 伦理指南，Disclosures。[证据](../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e7]: USENIX Security '26 伦理指南，IRB 一问。[证据](../../sources/notes/usenixsec2026cfp.md#e7)
[^usenixsec2026cfp-e8]: USENIX Security '26 伦理指南。[证据](../../sources/notes/usenixsec2026cfp.md#e8)
[^usenixsec2026cfp-e9]: USENIX Security '26 伦理指南，何时开始考虑伦理。[证据](../../sources/notes/usenixsec2026cfp.md#e9)
[^usenixsec2026cfp-e10]: USENIX Security '26 伦理指南。[证据](../../sources/notes/usenixsec2026cfp.md#e10)
[^carlini2022checklist-e1]: Carlini 2022，开头。[证据](../../sources/notes/carlini2022checklist.md#e1)
[^carlini2022checklist-e2]: Carlini 2022，Secondary checklist for public releases。[证据](../../sources/notes/carlini2022checklist.md#e2)
[^neurips2025llm-e5]: NeurIPS 2025 大模型使用政策，作者部分。[证据](../../sources/notes/neurips2025llm.md#e5)
[^neurips2025llm-e6]: NeurIPS 2025 大模型使用政策，作者部分 FAQ 2。[证据](../../sources/notes/neurips2025llm.md#e6)
[^neurips2025llm-e7]: NeurIPS 2025 大模型使用政策，作者部分。[证据](../../sources/notes/neurips2025llm.md#e7)
[^neurips2025llm-e8]: NeurIPS 2025 大模型使用政策，作者部分 FAQ 3。[证据](../../sources/notes/neurips2025llm.md#e8)
[^neurips2025llm-e9]: NeurIPS 2025 大模型使用政策，作者部分。[证据](../../sources/notes/neurips2025llm.md#e9)
[^icmje2026recommendations-e29]: ICMJE 2026，II.A.4。[证据](../../sources/notes/icmje2026recommendations.md#e29)
[^icmje2026recommendations-e30]: ICMJE 2026，II.A.4。[证据](../../sources/notes/icmje2026recommendations.md#e30)
[^icmje2026recommendations-e31]: ICMJE 2026，II.A.4。[证据](../../sources/notes/icmje2026recommendations.md#e31)
[^icmje2026recommendations-e32]: ICMJE 2026，IV.A.3.d。[证据](../../sources/notes/icmje2026recommendations.md#e32)
[^icmje2026recommendations-e33]: ICMJE 2026，V.A。[证据](../../sources/notes/icmje2026recommendations.md#e33)
