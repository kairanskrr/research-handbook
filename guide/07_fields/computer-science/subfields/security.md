# 安全

> 本页只写这个方向特有的做法；通用做法见第一部分、第二部分各章和研究套路，计算机共通的规矩（会议流程、双盲与预印本、制品评估、伦理要点）见[计算机学科概况](../README.md)。

## 这个方向研究什么

安全方向研究系统、软件、网络和数据怎样被攻击，又怎样保护。以 IEEE S&P 2026（IEEE Symposium on Security and Privacy，IEEE 安全与隐私研讨会；IEEE 即电气电子工程师学会）的征稿为例：论文可以是安全系统的理论、设计、实现、分析、验证，也可以是实证评估和测量；主题从网络安全与测量到面向安全和隐私的用户研究，范围很广[^ieeesp2026cfp-e13]。

几个典型问题 `[本项目分析]`：

- **防御**：一种新防御能挡住哪些攻击，要付出多少性能代价？
- **工具**：一个新的模糊测试工具（用大量自动生成的输入去"轰炸"程序，找出缺陷）是否真比已有工具强[^klees2018evaluating-e1]？
- **攻击和测量**：某种新攻击能不能成功；某个安全问题在真实世界里有多普遍。

**先想清楚对手能做什么。** 安全研究要面对会针对你的方案想办法的对手 `[本项目分析]`。以对抗样本（专门构造来骗过机器学习模型的输入）的防御为例，Carlini 等人要求：先问"什么攻击可能攻破这个防御"，再证明这些攻击都无效；只用默认参数跑现成的攻击，哪怕是最先进的攻击，也不够[^carlini2019evaluating-e1]。把这条思路用到其他防御上，是本项目的推断 `[本项目分析]`。

## 主要发表处和节奏

安全方向的主要成果发表在会议上 `[本项目分析]`。van der Kouwe 等人研究评测缺陷时，只选了"四大"安全会议的论文，理由是它们影响最大，事实上决定了领域的评测惯例[^vanderkouwe2019sok-e27]。

下表是本页资料里四个会议**各自某一年**的规则，不是整个方向的惯例。**规则每年都会变，投稿前以当年的征稿启事为准。** 表中 NDSS 即 Network and Distributed System Security Symposium，CCS 即 ACM Conference on Computer and Communications Security（ACM 即美国计算机协会）。

| 会议（年份） | 全称 | 投稿节奏 | 正文篇幅 | 修改机会 |
|---|---|---|---|---|
| USENIX Security 2026 | USENIX 协会主办的安全研讨会 | 分轮投稿，每轮有早期拒稿和作者回复期[^usenixsec2026cfp-e1] | 见当年启事 | 不再有"大修"，最多两周的指导修改[^usenixsec2026cfp-e14] |
| IEEE S&P 2026 | 见上 | 两个截稿日[^ieeesp2026cfp-e11] | 13 页[^ieeesp2026cfp-e8] | 没有"有条件录用"，按截稿时的稿子原样审[^ieeesp2026cfp-e12] |
| NDSS 2026 | 网络与分布式系统安全研讨会 | 夏、秋两轮[^ndss2026cfp-e8] | 13 页[^ndss2026cfp-e6] | 有"大修"，六周内重投[^ndss2026cfp-e1] |
| ACM CCS 2025 | 计算机与通信安全会议 | 两轮[^ccs2025cfp-e1] | 12 页[^ccs2025cfp-e4] | 有"小修"[^ccs2025cfp-e1] |

表里放不下的几条，同样只属于标出的那一年：

- **IEEE S&P 2026**：录用论文附一份公开的综合审稿意见，写明录用理由和委员会仍有的顾虑[^ieeesp2026cfp-e7]；被拒后要从原投稿日起等满一年才能再投[^ieeesp2026cfp-e9]。
- **NDSS 2026**：大修指的是补新的实现、实验或证明[^ndss2026cfp-e1]。
- **页数怎么算**：IEEE S&P 2026 另给参考文献和附录 5 页[^ieeesp2026cfp-e8]；NDSS 2026 的伦理小节、参考文献、附录不计入[^ndss2026cfp-e6]；CCS 2025 参考文献、附录和补充材料不计入[^ccs2025cfp-e4]。

从表里能看出两点 `[本项目分析]`：

- **同一年几个会议的规则就各不相同**，不能照搬上一次投稿的做法。
- **审稿人不一定读附录。** IEEE S&P 2026 和 CCS 2025 都写明审稿人不必读附录[^ieeesp2026cfp-e8][^ccs2025cfp-e4]，关键的实验和论证要放在正文里。

**知识系统化论文**（Systematization of Knowledge，简称 SoK）是安全会议上的一类专门论文。IEEE S&P 2026 征集这类论文：它要评估、梳理已有知识，并把它放进脉络里；没有这类见解的普通综述可能不经完整审稿就被拒；它按对已有工作的处理和对社区的价值录用，不看有没有新的研究结果[^ieeesp2026cfp-e1]。NDSS 2026 也收这类论文，要求不只是总结，还要深入分析已有方法、找出空白和局限[^ndss2026cfp-e5]。

**理论论文**（如密码学证明）在 IEEE S&P 2026 和 CCS 2025 都有一条额外要求：必须令人信服地说明结果和实践的关系[^ieeesp2026cfp-e2][^ccs2025cfp-e2]。理论方向自己的惯例见[理论](theory.md)。

## 常用套路与证据标准

下表的分组和概括是本项目的归纳，每条标准只代表脚注里那篇文献或那个会议 `[本项目分析]`。

| 套路 | 在这个方向的样子 | 证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../../05_research-strategies/build_improve.md) | 新防御、新检测系统 | 和当前最好的方案比，对手配置要公平[^vanderkouwe2019sok-e4]；除了运行时间，还测内存、读写、程序体积[^vanderkouwe2019sok-e6]；要做判断的系统必须测准确率[^vanderkouwe2019sok-e7] | [工程研究](../practices/engineering_research.md)、[系统](systems.md) |
| [比较评估](../../../05_research-strategies/compare_evaluate.md) | 工具之间的对比，例如模糊测试 | 多次运行加统计检验[^klees2018evaluating-e10]；数真实缺陷，不数"不同崩溃数"[^klees2018evaluating-e4] | [基准评测](../practices/benchmarking.md) |
| 构建改进（用机器学习做安全） | 恶意软件检测、入侵检测 | 不偷看测试集、不忽略时间顺序[^arp2022dos-e4]；查虚假相关[^arp2022dos-e12]；样本极不平衡时注意基础比率[^arp2022dos-e8] | [机器学习](machine_learning.md) |
| [观察描述](../../../05_research-strategies/observe_describe.md) | 网络安全测量、用户研究[^ieeesp2026cfp-e13] | 用了来自人的数据（即使已匿名），IEEE S&P 2026 要求说明伦理审查情况[^ieeesp2026cfp-e6] | [问卷调查](../../../06_methods/questionnaire_survey.md)、[对照实验](../../../06_methods/controlled_experiment.md) |
| [综合](../../../05_research-strategies/synthesize.md) | SoK 论文 | 要有见解，不能只是罗列[^ieeesp2026cfp-e1][^ndss2026cfp-e5] | [综述研究](../../../06_methods/review_study.md) |
| [证明](../../../05_research-strategies/prove.md) | 密码学和协议的安全证明 | 说明和实践的关系[^ieeesp2026cfp-e2] | [理论研究](../practices/theoretical_research.md)、[理论](theory.md) |

表里几条的展开 `[本项目分析]`：

- **机器学习用在安全上**，Arp 等人举过一个例子：恶意软件检测实验里，"play.google.com"这个网址成了判定正常应用最重要的特征之一，说明分类器学会的是区分应用来自哪里，而不是区分恶意和正常[^arp2022dos-e12]。又如真阳性率 99%、假阳性率 1% 看似很好，但正负样本比为 1:100 时，每 99 个真阳性就伴随 100 个假阳性[^arp2022dos-e8]。
- **SoK 论文的分类要可靠。** 例如 van der Kouwe 等人让两人独立给每篇论文判定，有分歧的再讨论[^vanderkouwe2019sok-e28]。
- **很多安全论文是混合的**，例如先展示一种新攻击，再提出防御。先按核心主张定主要套路，其他部分按各自套路的标准要求。

## 这个方向特有的规矩

**伦理讨论几乎是必答题，但各会议写法不同。** 通用做法（越早考虑越好、《Menlo 报告》的四条原则、伦理审查批准不等于没问题）见[科研诚信与伦理](../../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)和[计算机学科概况](../README.md#伦理问题有本领域的特点)。下面只列各会议某一年的具体规定：

| 会议（年份） | 伦理怎么写 | 不过关会怎样 |
|---|---|---|
| USENIX Security 2026 | 所有论文都要讨论研究伦理[^usenixsec2026cfp-e2] | 见当年启事 |
| IEEE S&P 2026 | 文末单设"伦理考量"小节，没有伦理问题也要写"无"[^ieeesp2026cfp-e3] | 研究伦理委员会可以建议以伦理理由拒稿[^ieeesp2026cfp-e4] |
| NDSS 2026 | "伦理考量"小节可选[^ndss2026cfp-e4]；要预见做研究和发表研究两方面的后果[^ndss2026cfp-e2] | 伦理处理不当，不论科学价值多高都可能被拒[^ndss2026cfp-e2] |
| CCS 2025 | 要让审稿人相信走了适当程序（如伦理审查、负责任披露），并尽力减少伤害[^ccs2025cfp-e3] | 见当年启事 |

另外，NDSS 2026 写明，伦理审查委员会的豁免不一定足以说明伦理问题已处理好[^ndss2026cfp-e3]。

投 CCS 这类 ACM 会议，还要守 ACM 出版委员会 2021 年批准的《涉及人类参与者和受试者的研究政策》[^acm2021humanparticipants-e1]，它适用于所有 ACM 出版物，包括 ACM 主办或合办的会议[^acm2021humanparticipants-e3]。被认定违反的论文，视情节轻重可能被加"关注说明"（Note of Concern）或撤稿[^acm2021humanparticipants-e6]。具体要求（如伦理审查和书面证明）见[人机交互：涉及人的研究和伦理](hci.md#涉及人的研究和伦理)。

**漏洞披露有具体时限和写法。** "先私下告知负责方、修好再公开"的通用原则见[科研诚信与伦理](../../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)。各会议的要求：

- **USENIX Security 2026**：论文写清向谁披露了、结果如何[^usenixsec2026cfp-e6]；投稿要匿名，但审稿期间仍可向厂商或公众披露漏洞[^usenixsec2026cfp-e3]。
- **IEEE S&P 2026**：投稿版要详细讨论已经或打算怎样处理漏洞，最晚在作者回复截止前完成披露[^ieeesp2026cfp-e5]；投稿版不写完整的 CVE 编号（Common Vulnerabilities and Exposures，公开漏洞的统一编号），以免暴露作者[^ieeesp2026cfp-e14]。
- **NDSS 2026**：报告高影响漏洞的论文，要报告或至少讨论披露计划[^ndss2026cfp-e3]。

**制品要早准备，并注意匿名。**

- 有的会议审稿时就要制品，做不到要说明理由：USENIX Security 2026[^usenixsec2026cfp-e12]、CCS 2025[^ccs2025cfp-e5]。NDSS 2026 则是强烈鼓励录用论文参加制品评估[^ndss2026cfp-e7]。
- IEEE S&P 2026 要求投稿时的制品仓库匿名，仓库和制品内容里都不能留作者信息[^ieeesp2026cfp-e15]；理论论文强烈建议投稿时就把证明作为制品提交[^ieeesp2026cfp-e10]。
- 带恶意或破坏性操作的制品（例如恶意软件样本、攻击脚本），要醒目标明，见[计算机学科概况](../README.md#伦理问题有本领域的特点)。

**性能数字按系统方向的规矩报。** 防御和安全工具常要报性能开销。van der Kouwe 等人调查了 50 篇顶会防御论文，平均每篇有 5 个评测缺陷，只有 1 篇没有[^vanderkouwe2019sok-e26]。怎样避免，见[系统](systems.md#这个方向特有的规矩)和[基准评测](../practices/benchmarking.md#2-怎么做)。

**写给一般的安全研究者看。** CCS 2025 鼓励把摘要和引言写得让一般的安全研究者也读得懂[^ccs2025cfp-e2]；评审看重对实际安全和隐私问题的重要性、新颖性、执行质量和表达[^ccs2025cfp-e3]。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只用默认参数跑几个现成攻击，就说防御有效 | 对抗样本方向要求证明针对这个防御的攻击也无效[^carlini2019evaluating-e1] |
| 防御只和自己以前的版本比 | 要和当前最好的方案比[^vanderkouwe2019sok-e4] |
| 只报运行时间开销 | 内存、读写、程序体积也要测[^vanderkouwe2019sok-e6] |
| 模糊测试只跑一次、数"崩溃数" | 结论可能反过来[^klees2018evaluating-e11]，指标会多算缺陷[^klees2018evaluating-e4] |
| 在测试集上调参数或定阈值 | 会得到过于乐观的结果[^arp2022dos-e7] |
| 把普通综述当 SoK 投 | IEEE S&P 2026 写明，没有见解的综述可能直接被拒[^ieeesp2026cfp-e1] |
| 关键实验放在附录里 | IEEE S&P 2026、CCS 2025 的审稿人不必读附录[^ieeesp2026cfp-e8][^ccs2025cfp-e4] |
| 投稿版写了完整的 CVE 编号 | IEEE S&P 2026 认为这会暴露作者[^ieeesp2026cfp-e14] |
| 照搬去年或别的会议的规则 | 大修、伦理小节、制品要求，每个会议每年都可能不同，见上文的表 `[本项目分析]` |

## 延伸阅读

- **你要投的会议当年的征稿启事和伦理指南**，例如 USENIX Security、IEEE S&P、NDSS、CCS。每次投稿前都要重新读。
- **van der Kouwe 等人 2019，SoK: Benchmarking Flaws in Systems Security**：列出 22 种评测缺陷，做防御和系统安全的人投稿前拿来逐条自查。
- **Klees 等人 2018，Evaluating Fuzz Testing**：做模糊测试或任何带随机性的工具评估时读。
- **Arp 等人 2022，Dos and Don'ts of Machine Learning in Computer Security**：用机器学习做安全时的常见陷阱。
- **Carlini 等人 2019，On Evaluating Adversarial Robustness**：评估对抗样本防御的指南。
- 相关方向：[系统](systems.md)（性能评测的规矩）、[机器学习](machine_learning.md)、[理论](theory.md)。

[^ieeesp2026cfp-e13]: IEEE S&P 2026 征稿启事，开头与 Topics of interest。[证据](../../../../sources/notes/ieeesp2026cfp.md#e13)
[^klees2018evaluating-e1]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e1)
[^carlini2019evaluating-e1]: Carlini 等人 2019，§2.5。[证据](../../../../sources/notes/carlini2019evaluating.md#e1)
[^vanderkouwe2019sok-e27]: van der Kouwe 等人 2019，§I、§III-B。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e27)
[^usenixsec2026cfp-e1]: USENIX Security '26 征稿启事，Important Dates。[证据](../../../../sources/notes/usenixsec2026cfp.md#e1)
[^usenixsec2026cfp-e14]: USENIX Security '26 征稿启事，Summary of main changes。[证据](../../../../sources/notes/usenixsec2026cfp.md#e14)
[^ieeesp2026cfp-e11]: IEEE S&P 2026 征稿启事，Important Dates。[证据](../../../../sources/notes/ieeesp2026cfp.md#e11)
[^ieeesp2026cfp-e8]: IEEE S&P 2026 征稿启事，Page Limit and Formatting。[证据](../../../../sources/notes/ieeesp2026cfp.md#e8)
[^ieeesp2026cfp-e12]: IEEE S&P 2026 征稿启事，Public Meta-Reviews。[证据](../../../../sources/notes/ieeesp2026cfp.md#e12)
[^ndss2026cfp-e8]: NDSS 2026 征稿启事，Paper Submission Information。[证据](../../../../sources/notes/ndss2026cfp.md#e8)
[^ndss2026cfp-e6]: NDSS 2026 征稿启事，Paper Formatting。[证据](../../../../sources/notes/ndss2026cfp.md#e6)
[^ndss2026cfp-e1]: NDSS 2026 征稿启事，Paper Submission Information。[证据](../../../../sources/notes/ndss2026cfp.md#e1)
[^ccs2025cfp-e1]: ACM CCS 2025 征稿启事，开头。[证据](../../../../sources/notes/ccs2025cfp.md#e1)
[^ccs2025cfp-e4]: ACM CCS 2025 征稿启事，格式要求。[证据](../../../../sources/notes/ccs2025cfp.md#e4)
[^ieeesp2026cfp-e7]: IEEE S&P 2026 征稿启事，Public Meta-Reviews。[证据](../../../../sources/notes/ieeesp2026cfp.md#e7)
[^ieeesp2026cfp-e9]: IEEE S&P 2026 征稿启事，Submission Deadlines & Decisions。[证据](../../../../sources/notes/ieeesp2026cfp.md#e9)
[^ieeesp2026cfp-e1]: IEEE S&P 2026 征稿启事，Systematization of Knowledge Papers。[证据](../../../../sources/notes/ieeesp2026cfp.md#e1)
[^ndss2026cfp-e5]: NDSS 2026 征稿启事，Areas/Topics of Interest。[证据](../../../../sources/notes/ndss2026cfp.md#e5)
[^ieeesp2026cfp-e2]: IEEE S&P 2026 征稿启事，开头。[证据](../../../../sources/notes/ieeesp2026cfp.md#e2)
[^ccs2025cfp-e2]: ACM CCS 2025 征稿启事，开头。[证据](../../../../sources/notes/ccs2025cfp.md#e2)
[^vanderkouwe2019sok-e4]: van der Kouwe 等人 2019，§II-D。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e6]: van der Kouwe 等人 2019，附录 E2。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e6)
[^vanderkouwe2019sok-e7]: van der Kouwe 等人 2019，§II-E。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e7)
[^klees2018evaluating-e10]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e10)
[^klees2018evaluating-e4]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e4)
[^arp2022dos-e4]: Arp 等人 2022，§2，P3。[证据](../../../../sources/notes/arp2022dos.md#e4)
[^arp2022dos-e12]: Arp 等人 2022，§4.1。[证据](../../../../sources/notes/arp2022dos.md#e12)
[^arp2022dos-e8]: Arp 等人 2022，§2，P8。[证据](../../../../sources/notes/arp2022dos.md#e8)
[^ieeesp2026cfp-e6]: IEEE S&P 2026 征稿启事，Ethical Considerations for Human Subjects Research。[证据](../../../../sources/notes/ieeesp2026cfp.md#e6)
[^vanderkouwe2019sok-e28]: van der Kouwe 等人 2019，§III-A。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e28)
[^usenixsec2026cfp-e2]: USENIX Security '26 征稿启事，Executive Summary。[证据](../../../../sources/notes/usenixsec2026cfp.md#e2)
[^ieeesp2026cfp-e3]: IEEE S&P 2026 征稿启事，Ethics Considerations。[证据](../../../../sources/notes/ieeesp2026cfp.md#e3)
[^ieeesp2026cfp-e4]: IEEE S&P 2026 征稿启事，Research Ethics Committee。[证据](../../../../sources/notes/ieeesp2026cfp.md#e4)
[^ndss2026cfp-e4]: NDSS 2026 征稿启事，Ethical Considerations。[证据](../../../../sources/notes/ndss2026cfp.md#e4)
[^ndss2026cfp-e2]: NDSS 2026 征稿启事，Ethical Considerations。[证据](../../../../sources/notes/ndss2026cfp.md#e2)
[^ccs2025cfp-e3]: ACM CCS 2025 征稿启事，评审标准。[证据](../../../../sources/notes/ccs2025cfp.md#e3)
[^ndss2026cfp-e3]: NDSS 2026 征稿启事，Ethical Considerations。[证据](../../../../sources/notes/ndss2026cfp.md#e3)
[^acm2021humanparticipants-e1]: ACM 2021 涉及人的研究政策，标题下。[证据](../../../../sources/notes/acm2021humanparticipants.md#e1)
[^acm2021humanparticipants-e3]: ACM 2021 涉及人的研究政策，Scope of Policy。[证据](../../../../sources/notes/acm2021humanparticipants.md#e3)
[^acm2021humanparticipants-e6]: ACM 2021 涉及人的研究政策，Violations and Penalties。[证据](../../../../sources/notes/acm2021humanparticipants.md#e6)
[^usenixsec2026cfp-e6]: USENIX Security '26 伦理指南，Disclosures。[证据](../../../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e3]: USENIX Security '26 征稿启事，Anonymous Submission。[证据](../../../../sources/notes/usenixsec2026cfp.md#e3)
[^ieeesp2026cfp-e5]: IEEE S&P 2026 征稿启事，Ethical Considerations for Vulnerability Disclosure。[证据](../../../../sources/notes/ieeesp2026cfp.md#e5)
[^ieeesp2026cfp-e14]: IEEE S&P 2026 征稿启事，Ethical Considerations for Vulnerability Disclosure。[证据](../../../../sources/notes/ieeesp2026cfp.md#e14)
[^usenixsec2026cfp-e12]: USENIX Security '26 征稿启事，Executive Summary。[证据](../../../../sources/notes/usenixsec2026cfp.md#e12)
[^ccs2025cfp-e5]: ACM CCS 2025 征稿启事，Providing Artifacts at Submission Time。[证据](../../../../sources/notes/ccs2025cfp.md#e5)
[^ndss2026cfp-e7]: NDSS 2026 征稿启事，Artifact Evaluation。[证据](../../../../sources/notes/ndss2026cfp.md#e7)
[^ieeesp2026cfp-e15]: IEEE S&P 2026 征稿启事，Anonymous Submission。[证据](../../../../sources/notes/ieeesp2026cfp.md#e15)
[^ieeesp2026cfp-e10]: IEEE S&P 2026 征稿启事，Artifacts。[证据](../../../../sources/notes/ieeesp2026cfp.md#e10)
[^vanderkouwe2019sok-e26]: van der Kouwe 等人 2019，摘要。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e26)
[^klees2018evaluating-e11]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e11)
[^arp2022dos-e7]: Arp 等人 2022，§2，P5。[证据](../../../../sources/notes/arp2022dos.md#e7)
