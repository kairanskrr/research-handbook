# 人机交互

> 本页只写这个方向特有的做法；通用做法见主线和研究套路，计算机共通的规矩见[计算机学科概况](../README.md)。

## 这个方向研究什么

人机交互（Human-Computer Interaction，HCI）研究人怎样使用计算技术，并设计、评估新的交互方式。它的贡献类型很多。这个方向的旗舰会议 CHI（ACM Conference on Human Factors in Computing Systems，ACM 人机交互大会；ACM 即美国计算机协会）2026 年的说明，按贡献类型列出了审稿人可用的评判标准[^chi2026papers-e32]。这些类型包括：界面制品或交互技术的开发与改进、理解用户、系统与工具、方法学、理论、创新与愿景、论证、验证与复现[^chi2026papers-e40]。

两个典型问题：

- **一种新技术是否更好用**：例如一种能减少选错的新菜单，通常要做仔细的实验，和其他菜单比较出错率[^chi2026papers-e37]。
- **人在某种情境下是怎样工作的**：例如 Mark 等人 2008 年在 CHI 发表的实验，48 名参与者在实验室模拟的办公环境里处理邮件，每两分钟被打断一次[^mark2008cost-e2]。结果发现，被打断时完成得反而更快，但代价是更大的压力和挫败感[^mark2008cost-e1]。

所以同一个方向里，既有做工程的，也有做实验的，还有做访谈和民族志的。判断一篇论文够不够格，先要看它是哪一类贡献 `[本项目分析]`。

## 主要发表处和节奏

下面以 CHI 2026 为例。它只是一个会议、一年的规定，不代表这个方向的所有会议；每年会变，**以你要投的会议当年的说明为准**。

| 环节 | CHI 2026 的做法 |
|---|---|
| 规模 | 截至 2025 年，预计收到 5,000 多篇投稿[^chi2026papers-e33]；投稿指南说，通常约 75% 被拒[^chi2026papers-e2] |
| 截稿 | 2025 年 9 月 4 日交摘要和元数据，9 月 11 日交全文，2026 年 1 月 15 日通知结果[^chi2026papers-e35] |
| 作者名单 | 摘要截止后不能再改[^chi2026papers-e36] |
| 篇幅 | 按词数算：短论文 5,000 词以内，标准论文 5,000–12,000 词[^chi2026papers-e5] |
| 超长 | 超过 12,000 词又没有正当理由的，直接拒稿[^chi2026papers-e5] |
| 附录 | 审稿人和领域主席不必读附录和补充材料[^chi2026papers-e6] |
| 子委员会 | 最多选两个主题子委员会[^chi2026papers-e10] |
| 审稿方式 | "修改后重投"（Revise and Resubmit），取代了以往的作者回复[^chi2026papers-e3] |
| 第二轮 | 第一轮过门槛的有 5 周修改，但第二轮仍可能有多达一半被拒[^chi2026papers-e4] |
| 会议报告 | 录用论文的作者必须到会报告[^chi2026papers-e34] |

CHI 论文基本按投稿时的样子评审，需要大改的会被拒[^chi2026papers-e21]。双盲和预印本的一般规矩见[学科概况：双盲评审与预印本](../README.md#双盲评审与预印本)。CHI 2026 特别提醒：用户研究地点、在哪里通过伦理审查写得太细，或图里有作者的脸，都会暴露身份[^chi2026papers-e29]。CHI 不反对在审稿前或审稿期间以非存档形式公开论文，但承认这会让完全匿名更难[^chi2026papers-e28]。研讨会报告、海报等非存档形式不算已发表[^chi2026papers-e26]。

## 常用套路与证据标准

下表是本项目按 CHI 2026 的说明和人机交互相关资料归纳的；每条标准只代表脚注里那份资料 `[本项目分析]`。

| 套路 | 在这个方向的样子 | 这个方向特别看重的证据 | 具体做法 |
|---|---|---|---|
| [构建改进](../../../05_research-strategies/build_improve.md) | 新的交互技术、界面、系统或工具 | 有说服力的验证，证明提升有实际意义[^chi2026papers-e23]；描述详细到别人能重做[^chi2026papers-e38]；系统论文不一定要用户研究，但要有合适的验证[^chi2026papers-e22] | [工程研究](../practices/engineering_research.md) |
| [解释因果](../../../05_research-strategies/explain_causality.md) | 有人参与的对照实验，比较不同界面对人的影响 | 注意对照实验天生偏向能快速学会的工具[^ko2015practical-e22] | [对照实验](../../../06_methods/controlled_experiment.md) |
| [观察描述](../../../05_research-strategies/observe_describe.md) | 理解用户：访谈、现场研究、民族志 | 说明研究的是哪些人、多不多样[^chi2026papers-e24]；交代研究者的立场[^chi2026papers-e16]；写清主题怎样从数据中得出[^chi2026papers-e17] | [访谈研究](../../../06_methods/interview_study.md)、[案例研究与民族志](../../../06_methods/case_study.md)、[扎根理论](../../../06_methods/grounded_theory.md) |
| [测量](../../../05_research-strategies/measure.md) | 用问卷和量表测用户的看法 | 不直接问"有用吗"，用验证过的量表[^ko2015practical-e29] | [问卷调查](../../../06_methods/questionnaire_survey.md)、[量表开发](../../../06_methods/scale_development.md) |
| [解读论证](../../../05_research-strategies/interpret_argue.md) | 论证类论文、理论贡献 | 论据扎实、有事实支撑，平衡地考虑其他观点[^chi2026papers-e39] | |

访谈在这个方向很常见：McDonald 等人分析的 251 篇定性论文中，71.3% 用了访谈[^mcdonald2019reliability-e3]。复现也被认可：CHI 的审稿指南说，建设性的复现本身可以是重要贡献[^chi2026papers-e25]，做法见[复现研究](../../../06_methods/replication.md)。

## 这个方向特有的规矩

### 审稿先看贡献

CHI 2026 的审稿表要评重要性、原创性、研究质量、表达清晰度和相关工作[^chi2026papers-e11][^chi2026papers-e41]。研究质量按该子领域对"严谨"的定义来评[^chi2026papers-e11]，例如设计类论文按设计社区的标准，而不按计算交互社区的标准[^chi2026papers-e7]。各项中，贡献及其重要性最重要[^chi2026papers-e12]。

审稿人常提的意见有两类：研究缺少理论依据[^chi2026papers-e14]；设计选择没有说明理由[^chi2026papers-e43]。所以不只写做了什么，还要写为什么这样做[^chi2026papers-e14]。审稿人常以质量问题为由拒稿[^chi2026papers-e42]，所以怎样证明质量，要在计划阶段就想好，不要拖到最后[^chi2026papers-e13]。

CHI 2026 还新增了"协助直拒"：超出范围、或离录用标准太远的论文，可以不送外审直接拒稿[^chi2026papers-e44]，理由包括数据远不足以支撑主张、相对篇幅贡献过小[^chi2026papers-e30]。

### 评估方式要和问题相称

> **不同的看法：每个设计都要做可用性评估吗？**
> - **要评估**：CHI 2026 对界面制品和技术的要求是，有严格、有说服力的验证，例如实证研究、可用性研究或现场研究[^chi2026papers-e23]。Zhai 的看法是，评估方法虽有种种问题，总比什么都不做好[^greenberg2008usability-e7]。连批评者 Greenberg 和 Buxton 也承认，可用性评估在很多情况下有价值，社区应当在多数（但不是全部）情况下继续做[^greenberg2008usability-e6]。
> - **不一定**：Greenberg 和 Buxton 2008 年认为，用什么评估方法、甚至要不要评估，必须从具体的研究问题出发[^greenberg2008usability-e1]。在设计早期做可用性评估，可能压制不符合现有惯例的创意[^greenberg2008usability-e2]。找一个场景证明新技术更好，只是在找确认性证据，验证很弱[^greenberg2008usability-e3]。据他们描述，UIST（ACM User Interface Software and Technology Symposium，用户界面软件与技术研讨会）当时希望有评估，但设计有启发性、论证充分时不强求[^greenberg2008usability-e8]。
>
> CHI 2026 自己也说，证明质量的方式随贡献类型而变：改进已知技术，通常做仔细的实验；支持新协作方式的系统，可能在真实条件下评估[^chi2026papers-e37]。Greenberg 和 Buxton 的建议是：真正新颖的创新，"存在性证明"可能就够了；主流系统或对成熟想法的小改动，应当做可能推翻它的检验[^greenberg2008usability-e4]。
>
> 实际做法是：先想清楚你的贡献属于哪一类，再选和它相称的验证方式，并在论文里说明为什么这样选 `[本项目分析]`。

### 透明和材料分享

以下是 CHI 2026 投稿指南的要求：

- 技术类贡献和定量研究，要求可验证、可复现[^chi2026papers-e15]。
- 定性研究要交代各项决定和研究者的立场[^chi2026papers-e16]，并写清主题怎样从数据中得出、结论来自个别突出例子还是普遍趋势[^chi2026papers-e17]。
- 向参与者提问的研究，要让读者知道问了什么、原话怎么问的[^chi2026papers-e20]。
- 代码、数据、访谈提纲等，最好放到带永久标识符的公开存储库[^chi2026papers-e18]；不能全部分享时，尽量多分享，并写明其余部分为什么不能分享[^chi2026papers-e19]。

### 定性研究不一定算编码者间信度

编码者间信度是衡量多名编码者判断有多一致的统计量。McDonald 等人抽样分析了 2016–2018 年 CSCW（Computer-Supported Cooperative Work，计算机支持的协同工作）和人机交互的发表物，其中的定性论文只有约九分之一算了它[^mcdonald2019reliability-e17]。他们认为，怎样建立可靠性，应当与研究者依据的认识论传统一致[^mcdonald2019reliability-e9]。要不要算、怎样报告，见[访谈研究：让分析可信](../../../06_methods/interview_study.md#第六步让分析可信)。

### 涉及人的研究和伦理

- **伦理审查**：CHI 2026 要求，涉及人类参与者的研究必须通过作者所在研究环境要求的伦理审查；各地要求不同，所以要给审稿人附一段简短说明[^chi2026papers-e8]。会议之上还有 ACM 的总规定：ACM 出版委员会 2021 年批准的《涉及人类参与者和受试者的研究政策》[^acm2021humanparticipants-e1]，适用于所有 ACM 出版物，包括 ACM 主办或合办的会议[^acm2021humanparticipants-e3]。它要求研究的计划、实施和报告既符合当地法律法规，也符合这项政策列出的一般原则，例如知情同意[^acm2021humanparticipants-e2]；当地要求伦理审查的，作者要让研究通过审查，并准备好随时向 ACM 出示书面证明[^acm2021humanparticipants-e4]。具体的 ACM 期刊或会议可以另定更严的要求[^acm2021humanparticipants-e5]。被认定违反这项政策的论文，视情节轻重可能被加"关注说明"（Note of Concern）或撤稿[^acm2021humanparticipants-e6]。通用做法见[科研诚信与伦理](../../../08_throughout/integrity_and_ethics.md)。
- **纳入了谁**：留意研究纳入了谁、没纳入谁，主张的范围要和这一点相符[^chi2026papers-e31]。
- **参与者会讨好研究者**：不要只问"我的工具好用吗"，原因和替代做法见[对照实验：定好怎么测](../../../06_methods/controlled_experiment.md#第-5-步定好怎么测)。
- **大语言模型**：CHI 2026 要求，大语言模型生成的文字，凡用途超出修改作者自己的文字，都要标明[^chi2026papers-e9]。通用做法见[科研诚信与伦理：用大模型等工具时，责任仍然在你](../../../08_throughout/integrity_and_ethics.md#6-用大模型等工具时责任仍然在你)。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只找一个对自己有利的场景证明新技术更好 | 只是确认性证据，验证很弱[^greenberg2008usability-e3] |
| 对早期草图做正式的可用性测试 | 可能压制不合常规的创意[^greenberg2008usability-e2] |
| 把评估拖到投稿前才想 | 审稿人常以质量问题拒稿[^chi2026papers-e42] |
| 只写做了什么，不写为什么这样设计 | 审稿人常批评设计选择没有理由[^chi2026papers-e43] |
| 关键细节只放在附录里 | CHI 2026 审稿人不必读附录[^chi2026papers-e6] |
| 定性研究只报告百分比一致率 | 它没考虑碰巧一致，普遍认为不可接受[^mcdonald2019reliability-e4] |
| 方法部分写明在哪所大学通过伦理审查 | 会暴露身份[^chi2026papers-e29] |
| 只研究了一小群人，却说适用于所有用户 | 主张的范围要和研究纳入了谁相符[^chi2026papers-e31] |
| 摘要截止后才想起加作者 | CHI 2026 截止后名单不能再改[^chi2026papers-e36] |

## 延伸阅读

- **你要投的那一届 CHI 的 Guide to a Successful Submission 和 Contributions to CHI**：前者讲审稿人怎么看论文、怎样写才透明，后者按贡献类型列出评审要问的问题。动笔前读。
- **Greenberg & Buxton 2008，Usability Evaluation Considered Harmful (Some of the Time)**：讲什么时候不该用可用性评估。CHI 2026 的审稿指南把它列为"什么是好的 CHI 论文"这场争论的参考读物[^chi2026papers-e45]。
- **McDonald、Schoenebeck & Forte 2019，Reliability and Inter-rater Reliability in Qualitative Research**：什么时候该算、什么时候不该算编码者间信度。做定性研究前读。
- **Ko、LaToza & Burnett 2015**：有人参与的工具评估实验怎样设计，从招募到预实验。
- 同一学科的其他方向：[机器学习](machine_learning.md)、[软件工程](software_engineering.md)、[安全](security.md)、[系统](systems.md)、[理论](theory.md)、[程序设计语言](programming_languages.md)。

[^chi2026papers-e32]: CHI 2026，Contributions to CHI。[证据](../../../../sources/notes/chi2026papers.md#e32)
[^chi2026papers-e40]: CHI 2026，Contributions to CHI，各贡献类型小标题。[证据](../../../../sources/notes/chi2026papers.md#e40)
[^chi2026papers-e37]: CHI 2026，Guide to a Successful Submission，Ensuring High-Quality Research。[证据](../../../../sources/notes/chi2026papers.md#e37)
[^mark2008cost-e2]: Mark 等人 2008，Experimental Design and Procedure。[证据](../../../../sources/notes/mark2008cost.md#e2)
[^mark2008cost-e1]: Mark 等人 2008，Abstract。[证据](../../../../sources/notes/mark2008cost.md#e1)
[^chi2026papers-e33]: CHI 2026 征稿页，Select a Subcommittee。[证据](../../../../sources/notes/chi2026papers.md#e33)
[^chi2026papers-e2]: CHI 2026，Guide to a Successful Submission，开头。[证据](../../../../sources/notes/chi2026papers.md#e2)
[^chi2026papers-e35]: CHI 2026 征稿页，Important Dates。[证据](../../../../sources/notes/chi2026papers.md#e35)
[^chi2026papers-e36]: CHI 2026 征稿页，Complete Submission。[证据](../../../../sources/notes/chi2026papers.md#e36)
[^chi2026papers-e5]: CHI 2026 征稿页，Important Facts。[证据](../../../../sources/notes/chi2026papers.md#e5)
[^chi2026papers-e6]: CHI 2026 征稿页，Important Facts。[证据](../../../../sources/notes/chi2026papers.md#e6)
[^chi2026papers-e10]: CHI 2026 征稿页，Select a Subcommittee。[证据](../../../../sources/notes/chi2026papers.md#e10)
[^chi2026papers-e3]: CHI 2026，Guide to a Successful Submission，The Review Process。[证据](../../../../sources/notes/chi2026papers.md#e3)
[^chi2026papers-e4]: CHI 2026，Papers Review Process，Round 1。[证据](../../../../sources/notes/chi2026papers.md#e4)
[^chi2026papers-e34]: CHI 2026 征稿页，Your Paper at the Conference。[证据](../../../../sources/notes/chi2026papers.md#e34)
[^chi2026papers-e21]: CHI 2026，Guide to a Successful Submission，Describing the Work Clearly and Concisely。[证据](../../../../sources/notes/chi2026papers.md#e21)
[^chi2026papers-e29]: CHI 2026，Anonymization Policy。[证据](../../../../sources/notes/chi2026papers.md#e29)
[^chi2026papers-e28]: CHI 2026，Anonymization Policy。[证据](../../../../sources/notes/chi2026papers.md#e28)
[^chi2026papers-e26]: CHI 2026，Guide to Reviewing Papers，Prior Publication。[证据](../../../../sources/notes/chi2026papers.md#e26)
[^chi2026papers-e23]: CHI 2026，Contributions to CHI，Interface Artifacts or Techniques。[证据](../../../../sources/notes/chi2026papers.md#e23)
[^chi2026papers-e38]: CHI 2026，Contributions to CHI，Interface Artifacts or Techniques。[证据](../../../../sources/notes/chi2026papers.md#e38)
[^chi2026papers-e22]: CHI 2026，Contributions to CHI，Systems, Tools, Architectures, and Infrastructure。[证据](../../../../sources/notes/chi2026papers.md#e22)
[^ko2015practical-e22]: Ko 等人 2015，§4.4。[证据](../../../../sources/notes/ko2015practical.md#e22)
[^chi2026papers-e24]: CHI 2026，Contributions to CHI，Understanding Users。[证据](../../../../sources/notes/chi2026papers.md#e24)
[^chi2026papers-e16]: CHI 2026，Guide to a Successful Submission，Transparency。[证据](../../../../sources/notes/chi2026papers.md#e16)
[^chi2026papers-e17]: CHI 2026，Guide to a Successful Submission，Transparency。[证据](../../../../sources/notes/chi2026papers.md#e17)
[^ko2015practical-e29]: Ko 等人 2015，§6.3。[证据](../../../../sources/notes/ko2015practical.md#e29)
[^chi2026papers-e39]: CHI 2026，Contributions to CHI，Argument。[证据](../../../../sources/notes/chi2026papers.md#e39)
[^mcdonald2019reliability-e3]: McDonald 等人 2019，§4.3。[证据](../../../../sources/notes/mcdonald2019reliability.md#e3)
[^chi2026papers-e25]: CHI 2026，Guide to Reviewing Papers，Replicating Work。[证据](../../../../sources/notes/chi2026papers.md#e25)
[^chi2026papers-e11]: CHI 2026，Guide to a Successful Submission，The Review Form。[证据](../../../../sources/notes/chi2026papers.md#e11)
[^chi2026papers-e41]: CHI 2026，Guide to a Successful Submission，The Review Form。[证据](../../../../sources/notes/chi2026papers.md#e41)
[^chi2026papers-e7]: CHI 2026 征稿页，Research Quality。[证据](../../../../sources/notes/chi2026papers.md#e7)
[^chi2026papers-e12]: CHI 2026，Guide to a Successful Submission，Making a Significant Contribution。[证据](../../../../sources/notes/chi2026papers.md#e12)
[^chi2026papers-e14]: CHI 2026，Guide to a Successful Submission，Ensuring High-Quality Research。[证据](../../../../sources/notes/chi2026papers.md#e14)
[^chi2026papers-e43]: CHI 2026，Guide to a Successful Submission，Ensuring High-Quality Research。[证据](../../../../sources/notes/chi2026papers.md#e43)
[^chi2026papers-e42]: CHI 2026，Guide to a Successful Submission，Ensuring High-Quality Research。[证据](../../../../sources/notes/chi2026papers.md#e42)
[^chi2026papers-e13]: CHI 2026，Guide to a Successful Submission，Ensuring High-Quality Research。[证据](../../../../sources/notes/chi2026papers.md#e13)
[^chi2026papers-e44]: CHI 2026，Papers Review Process，Assisted Desk Reject。[证据](../../../../sources/notes/chi2026papers.md#e44)
[^chi2026papers-e30]: CHI 2026，Papers Review Process，Assisted Desk Reject。[证据](../../../../sources/notes/chi2026papers.md#e30)
[^greenberg2008usability-e7]: Greenberg & Buxton 2008，Related Work（转述 Zhai）。[证据](../../../../sources/notes/greenberg2008usability.md#e7)
[^greenberg2008usability-e6]: Greenberg & Buxton 2008，Introduction。[证据](../../../../sources/notes/greenberg2008usability.md#e6)
[^greenberg2008usability-e1]: Greenberg & Buxton 2008，Abstract。[证据](../../../../sources/notes/greenberg2008usability.md#e1)
[^greenberg2008usability-e2]: Greenberg & Buxton 2008，Abstract。[证据](../../../../sources/notes/greenberg2008usability.md#e2)
[^greenberg2008usability-e3]: Greenberg & Buxton 2008，Usability Evaluation as Weak Science。[证据](../../../../sources/notes/greenberg2008usability.md#e3)
[^greenberg2008usability-e8]: Greenberg & Buxton 2008，What To Do。[证据](../../../../sources/notes/greenberg2008usability.md#e8)
[^greenberg2008usability-e4]: Greenberg & Buxton 2008，What To Do。[证据](../../../../sources/notes/greenberg2008usability.md#e4)
[^chi2026papers-e15]: CHI 2026，Guide to a Successful Submission，Transparency。[证据](../../../../sources/notes/chi2026papers.md#e15)
[^chi2026papers-e20]: CHI 2026，Guide to a Successful Submission，Sharing research material。[证据](../../../../sources/notes/chi2026papers.md#e20)
[^chi2026papers-e18]: CHI 2026，Guide to a Successful Submission，Sharing research material。[证据](../../../../sources/notes/chi2026papers.md#e18)
[^chi2026papers-e19]: CHI 2026，Guide to a Successful Submission，Sharing research material。[证据](../../../../sources/notes/chi2026papers.md#e19)
[^mcdonald2019reliability-e17]: McDonald 等人 2019，摘要。[证据](../../../../sources/notes/mcdonald2019reliability.md#e17)
[^mcdonald2019reliability-e9]: McDonald 等人 2019，§2.3。[证据](../../../../sources/notes/mcdonald2019reliability.md#e9)
[^chi2026papers-e8]: CHI 2026 征稿页，Policy on Research Involving Human Participants and Subjects。[证据](../../../../sources/notes/chi2026papers.md#e8)
[^acm2021humanparticipants-e1]: ACM 2021 涉及人的研究政策，标题下。[证据](../../../../sources/notes/acm2021humanparticipants.md#e1)
[^acm2021humanparticipants-e2]: ACM 2021 涉及人的研究政策，Policy Statement。[证据](../../../../sources/notes/acm2021humanparticipants.md#e2)
[^acm2021humanparticipants-e3]: ACM 2021 涉及人的研究政策，Scope of Policy。[证据](../../../../sources/notes/acm2021humanparticipants.md#e3)
[^acm2021humanparticipants-e4]: ACM 2021 涉及人的研究政策，Roles and Responsibilities（Authors）。[证据](../../../../sources/notes/acm2021humanparticipants.md#e4)
[^acm2021humanparticipants-e5]: ACM 2021 涉及人的研究政策，Policy Statement。[证据](../../../../sources/notes/acm2021humanparticipants.md#e5)
[^acm2021humanparticipants-e6]: ACM 2021 涉及人的研究政策，Violations and Penalties。[证据](../../../../sources/notes/acm2021humanparticipants.md#e6)
[^chi2026papers-e31]: CHI 2026，Guide to a Successful Submission，Maximizing Impact。[证据](../../../../sources/notes/chi2026papers.md#e31)
[^chi2026papers-e9]: CHI 2026 征稿页，Policy on Use of Large Language Models。[证据](../../../../sources/notes/chi2026papers.md#e9)
[^mcdonald2019reliability-e4]: McDonald 等人 2019，§2.2。[证据](../../../../sources/notes/mcdonald2019reliability.md#e4)
[^chi2026papers-e45]: CHI 2026，Guide to Reviewing Papers，References。[证据](../../../../sources/notes/chi2026papers.md#e45)
