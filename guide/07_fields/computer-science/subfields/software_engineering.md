# 软件工程

> 本页只写这个方向特有的做法；通用做法见第一部分、第二部分各章和研究套路，计算机共通的规矩见[计算机学科概况](../README.md)。

## 这个方向研究什么

软件工程研究软件怎样被开发、分析和维护，也研究做软件的人和团队。Shaw 把这个方向要回答的问题分成几类：开发或分析软件的方法；某个具体系统的设计或评估；对一整类系统或技术的概括；某件事是否存在、能否做到[^shaw2003writing-e38]。

范围有多宽，可以看一个会议的征稿启事。ICSE（International Conference on Software Engineering，国际软件工程大会）2026 年把投稿分成九个研究领域，定量、定性和混合方法的研究都收[^icse2026cfp-e1]。领域从"用人工智能辅助软件工程"、挖掘版本库和缺陷跟踪系统里的数据，到人和社会层面，形式化方法和模型检查也在范围内[^icse2026cfp-e2]。

所以这个方向的论文大致有两类：

- **造新技术**，例如"一个新的测试生成工具能不能比已有工具发现更多缺陷"；
- **描述现状**，例如"开源项目的开发者为什么离开"。

两类在不同发表处的比例不一样。Storey 等人统计了 2017 年的论文：ICSE 上多数论文提出（多为技术性的）解决方案；EMSE（Empirical Software Engineering，《实证软件工程》期刊）上多数论文是描述性的[^storey2020who-e17]。

## 主要发表处和节奏

**会议和期刊。** 下面只列本文资料提到的几处：

| 发表处 | 类型 | 资料里的说法 |
|---|---|---|
| ICSE | 会议 | 自称是本领域发表最新重要技术成果的首要场所[^icse2026cfp-e14] |
| ESEM（Empirical Software Engineering and Measurement，实证软件工程与度量会议） | 会议 | 以实证方法为重点，也收研究社会层面的论文[^storey2020who-e18] |
| EMSE | 期刊 | 同上[^storey2020who-e18] |
| TSE（IEEE Transactions on Software Engineering，《IEEE 软件工程汇刊》） | 期刊 | 和 ICSE 2026 一起参加一项计划，减少审稿会议论文期刊扩展版的重复工作[^icse2026cfp-e11] |
| TOSEM（ACM Transactions on Software Engineering and Methodology，《ACM 软件工程与方法汇刊》） | 期刊 | 同上[^icse2026cfp-e11] |

ICSE 上什么样的论文最常见？Shaw 2003 年的分析是：报告一种新的开发或分析技术[^shaw2003writing-e26]。

**以 ICSE 2026 为例看一篇论文怎么走。** 下表只是 ICSE 2026 研究论文征稿启事里的规定，不是整个方向的惯例；别的年份、别的会议都会不同，**投稿前读目标会议当年的征稿启事**。

| 环节 | ICSE 2026 的规定 |
|---|---|
| 投稿轮次 | 一年两轮，2024 年起这样做[^icse2026cfp-e3] |
| 作者回复 | 每轮 3 天[^icse2026cfp-e3] |
| 篇幅 | 正文最多 10 页（含图表和附录），另加最多 2 页参考文献[^icse2026cfp-e7] |
| 匿名 | 双向匿名评审，引用自己的工作用第三人称；可以发 arXiv 预印本，但不能写明投给了 ICSE 2026[^icse2026cfp-e8] |
| 评审标准 | 新颖性、严谨性、相关性、可验证与透明、表达五条；附带的制品由一位审稿人检查[^icse2026cfp-e4] |
| 结果 | 录用、修改、拒稿三种；"修改"约有 4 周，由原审稿人再审，改不好仍会被拒[^icse2026cfp-e5] |
| 被拒之后 | 第一轮被拒的，强烈不建议在第二轮重投[^icse2026cfp-e6] |
| 制品 | 不强制，但默认要分享，不分享要说明理由[^icse2026cfp-e12] |
| 同时投稿 | 审稿期间不能同时投别处[^icse2026cfp-e9] |

新手可以留意一件事：ICSE 2026 第二轮设了"影子程序委员会"，让博士生、博士后等在指导下练习审稿[^icse2026cfp-e13]。

## 常用套路与证据标准

**ACM SIGSOFT 实证标准**（ACM SIGSOFT Empirical Standards，美国计算机协会软件工程分会制定的论文评审标准，下称"实证标准"）是软件工程自己的评审标准。它的出发点是：没有通用的质量标准，每项研究要按适合它的方法的标准来评[^ralph2020empirical-e142]。所以它按研究方法分开写，例如系统综述就有专门的一份[^ralph2020empirical-e1]。

计算机常用的七种套路、各自的证据标准，见[计算机学科概况：常用套路与证据标准](../README.md#常用套路与证据标准)；那张表里的标准大多就引自实证标准，这里不重复。下表只补软件工程里特别要注意的一点。表的内容是本项目的归纳，每格的事实见脚注。

| 套路 | 在软件工程里的样子 | 特别要注意 | 具体做法 |
|---|---|---|---|
| [构建改进](../../../05_research-strategies/build_improve.md) | 新的测试、分析、修复技术或工具 | 光"对你自己有效"不够，要有证据表明对别人也有用[^shaw2003writing-e11] | [工程研究](../practices/engineering_research.md) |
| [比较评估](../../../05_research-strategies/compare_evaluate.md) | 在标准基准上比较工具 | 搜索算法至少要和随机搜索比[^arcuri2014hitchhiker-e4] | [基准评测](../practices/benchmarking.md)、[优化研究](../practices/optimization_study.md) |
| [观察描述](../../../05_research-strategies/observe_describe.md) | 挖代码仓库和缺陷记录，或用问卷、访谈描述开发实践 | 只看开发留下的痕迹数据，看不全人的行为和意图[^storey2020who-e1] | [仓库挖掘](../practices/repository_mining.md)、[问卷调查](../../../06_methods/questionnaire_survey.md)、[访谈研究](../../../06_methods/interview_study.md) |
| [解释因果](../../../05_research-strategies/explain_causality.md) | 某个工具或技术是否带来改进 | 请人试用工具时，直接问"有没有用"很可能得不到有意义的数据[^ko2015practical-e28] | [对照实验](../../../06_methods/controlled_experiment.md) |
| [综合](../../../05_research-strategies/synthesize.md) | 系统综述、映射研究 | 一步步、可复现地写清检索过程和筛选标准[^ralph2020empirical-e4] | [综述研究](../../../06_methods/review_study.md) |
| [证明](../../../05_research-strategies/prove.md) | 形式化方法和模型检查 | 形式化模型要靠严格的推导和证明，不能靠一两个例子[^shaw2003writing-e9] | [理论研究](../practices/theoretical_research.md) |

## 这个方向特有的规矩

**1. 先找到你这类研究的标准，再动手。** 实证标准按方法分开写，动手前先读你那一类。没有读、没有用这类研究已发表的指南就开始做，是实证标准明确列出的反面做法[^ralph2020empirical-e26]。

**2. 知道哪些批评不成立。** 实证标准还专门列了"不成立的批评"，例如拿别的研究范式的规范来批评，或批评某类研究固有的局限（如说案例研究推广性低）[^ralph2020empirical-e25]。

**3. "案例研究"一词要用对。** 软件工程文献里，"案例研究"常被用来指一个演示用的例子，这和作为实证方法的案例研究完全是两回事[^easterbrook2008selecting-e10]。用玩具例子评估工具、还把它叫"案例研究"，是实证标准列出的反面做法[^ralph2020empirical-e93]。真正的案例研究见[案例研究与民族志](../../../06_methods/case_study.md)。

**4. 别只靠自己评估自己的工具。** Ko 等人的综述发现，62% 的工具评估其实是发明者自己用、自己报告体验，这说明不了别人用了会不会受益[^ko2015practical-e7]。怎样请真人来试用，见[对照实验](../../../06_methods/controlled_experiment.md)。

**5. 研究说要帮人，就考虑让人参与。** ICSE 和 EMSE 2017 年的论文里，多数声称研究最终会让人受益，但大部分没有直接让人参与[^storey2020who-e16]；以数据为主的论文，绝大多数没有用别的策略（如问卷、访谈）印证结论[^storey2020who-e9]。怎样把两种方法结合起来，见[混合方法](../../../06_methods/mixed_methods.md)。

**6. 制品要能拿到，也要存对地方。** 实证标准建议把补充材料存到有长期保存保障的存储库；个人或机构网站、GitHub、网盘都不算妥善存档[^ralph2020empirical-e139]。反过来，有正当理由不能公开的材料，不应成为批评的理由[^ralph2020empirical-e140]。ICSE 2026 也写明，定性研究不以可重复为目标[^icse2026cfp-e12]。制品评估和徽章的一般说明见[计算机学科概况](../README.md#制品评估与徽章)。

**7. 伦理。** 通用原则见[科研诚信与伦理](../../../08_throughout/integrity_and_ethics.md)。涉及人类参与者时，ICSE 2026 要求遵守 ACM 关于涉及人类参与者研究的出版政策[^icse2026cfp-e10]。挖仓库、问答网站等二手数据时，要说明数据凭什么"合法可用"，只因技术上能下载就拿来用是反面做法[^ralph2020empirical-e135]；具体做法见[仓库挖掘：处理伦理和许可问题](../practices/repository_mining.md#第八步处理伦理和许可问题)。

**8. 可以先发表计划。** 实证标准把"分两阶段发表：先发表研究计划，再发表执行结果"列为加分项[^ralph2020empirical-e28]。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 提出新工具，只和很弱的方法比，或根本不比 | 实证标准要求和当前最好的替代方案比，做不到要说明理由[^ralph2020empirical-e85] |
| 拿自己编的小例子演示，称之为"案例研究" | 实证标准列为反面做法[^ralph2020empirical-e93] |
| 只问用户"这个工具好不好用"就当作评估 | 评估只有用户意见，是实证标准列出的反面做法[^ralph2020empirical-e92] |
| 只招本校学生做实验，不讨论推广性 | 要论证结果为什么适用于业界开发者[^easterbrook2008selecting-e74] |
| 搜索算法只跑几次就下结论 | 一项对 2009–2010 年论文的综述发现，这类研究常常没有恰当处理算法的随机性[^arcuri2014hitchhiker-e2]；做法见[优化研究](../practices/optimization_study.md) |
| 代码只放在 GitHub 上就算"已存档" | 实证标准认为 GitHub 不算妥善存档[^ralph2020empirical-e139] |
| 爬了公开数据就直接用，不谈伦理 | 技术上能拿到不等于合法可用[^ralph2020empirical-e135] |
| 写了效度威胁，结论却照样写得很满 | 实证标准列为反面做法[^ralph2020empirical-e126] |
| 用实验研究的标准去评一篇定性研究 | 不同方法有不同的评审标准[^ralph2020empirical-e142] |

## 延伸阅读

- **ACM SIGSOFT Empirical Standards**（Ralph 等人）：按研究方法分开写的评审标准。动手前先读你那一类。
- **Shaw 2003，Writing Good Software Engineering Research Papers**：讲 ICSE 审稿人想看到什么问题、什么结果、什么验证。适合写第一篇论文前读。
- **Easterbrook 等人 2008，Selecting Empirical Methods for Software Engineering Research**：讲软件工程里各种实证方法各适合回答什么问题。
- **Ko 等人 2015，A practical guide to controlled experiments of software engineering tools with human participants**：想让真人试用你的工具时读。
- **Storey 等人 2020，The Who, What, How of Software Engineering Research**：看本领域论文在"研究谁、产出什么、怎么做"上的分布和缺口。
- **你要投的会议当年的征稿启事**，例如 ICSE 的研究论文征稿启事和开放科学政策。

[^shaw2003writing-e38]: Shaw 2003，§2.1。[证据](../../../../sources/notes/shaw2003writing.md#e38)
[^shaw2003writing-e26]: Shaw 2003，§3.2。[证据](../../../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e11]: Shaw 2003，§4.3。[证据](../../../../sources/notes/shaw2003writing.md#e11)
[^shaw2003writing-e9]: Shaw 2003，§4.1。[证据](../../../../sources/notes/shaw2003writing.md#e9)
[^icse2026cfp-e1]: ICSE 2026 研究论文征稿启事，Research Areas。[证据](../../../../sources/notes/icse2026cfp.md#e1)
[^icse2026cfp-e2]: ICSE 2026 研究论文征稿启事，Research Areas 领域列表。[证据](../../../../sources/notes/icse2026cfp.md#e2)
[^icse2026cfp-e3]: ICSE 2026 研究论文征稿启事，Dual Submission Cycles。[证据](../../../../sources/notes/icse2026cfp.md#e3)
[^icse2026cfp-e4]: ICSE 2026 研究论文征稿启事，Review Criteria。[证据](../../../../sources/notes/icse2026cfp.md#e4)
[^icse2026cfp-e5]: ICSE 2026 研究论文征稿启事，Review Criteria 与 Revisions。[证据](../../../../sources/notes/icse2026cfp.md#e5)
[^icse2026cfp-e6]: ICSE 2026 研究论文征稿启事，Re-submissions of Rejected Papers。[证据](../../../../sources/notes/icse2026cfp.md#e6)
[^icse2026cfp-e7]: ICSE 2026 研究论文征稿启事，Submission Process。[证据](../../../../sources/notes/icse2026cfp.md#e7)
[^icse2026cfp-e8]: ICSE 2026 研究论文征稿启事，Submission Process（双向匿名）。[证据](../../../../sources/notes/icse2026cfp.md#e8)
[^icse2026cfp-e9]: ICSE 2026 研究论文征稿启事，Submission Process（同时投稿）。[证据](../../../../sources/notes/icse2026cfp.md#e9)
[^icse2026cfp-e10]: ICSE 2026 研究论文征稿启事，Submission Process（涉及人的研究）。[证据](../../../../sources/notes/icse2026cfp.md#e10)
[^icse2026cfp-e11]: ICSE 2026 研究论文征稿启事，Submission Process（期刊扩展）。[证据](../../../../sources/notes/icse2026cfp.md#e11)
[^icse2026cfp-e12]: ICSE 2026 研究论文征稿启事，Open Science Policy。[证据](../../../../sources/notes/icse2026cfp.md#e12)
[^icse2026cfp-e13]: ICSE 2026 研究论文征稿启事，开头更新说明。[证据](../../../../sources/notes/icse2026cfp.md#e13)
[^icse2026cfp-e14]: ICSE 2026 研究论文征稿启事，开头。[证据](../../../../sources/notes/icse2026cfp.md#e14)
[^storey2020who-e1]: Storey 等人 2020，§2。[证据](../../../../sources/notes/storey2020who.md#e1)
[^storey2020who-e9]: Storey 等人 2020，§6.4。[证据](../../../../sources/notes/storey2020who.md#e9)
[^storey2020who-e16]: Storey 等人 2020，摘要。[证据](../../../../sources/notes/storey2020who.md#e16)
[^storey2020who-e17]: Storey 等人 2020，摘要。[证据](../../../../sources/notes/storey2020who.md#e17)
[^storey2020who-e18]: Storey 等人 2020，§1。[证据](../../../../sources/notes/storey2020who.md#e18)
[^ralph2020empirical-e142]: SIGSOFT General Standard，General Quality Criteria。[证据](../../../../sources/notes/ralph2020empirical.md#e142)
[^ralph2020empirical-e85]: SIGSOFT 工程研究标准，必要项（方法）。[证据](../../../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e92]: SIGSOFT 工程研究标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e92)
[^ralph2020empirical-e93]: SIGSOFT 工程研究标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e93)
[^ralph2020empirical-e1]: SIGSOFT 系统综述标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e1)
[^ralph2020empirical-e4]: SIGSOFT 系统综述标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e4)
[^ralph2020empirical-e26]: SIGSOFT General Standard，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e26)
[^ralph2020empirical-e25]: SIGSOFT General Standard，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e139]: SIGSOFT 开放科学补充标准，加分项与说明。[证据](../../../../sources/notes/ralph2020empirical.md#e139)
[^ralph2020empirical-e140]: SIGSOFT 开放科学补充标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e140)
[^ralph2020empirical-e135]: SIGSOFT 伦理补充标准（二手人类数据），反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e135)
[^ralph2020empirical-e28]: SIGSOFT General Standard，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e28)
[^ralph2020empirical-e126]: SIGSOFT General Standard，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e126)
[^easterbrook2008selecting-e74]: Easterbrook 等人 2008，§5.1。[证据](../../../../sources/notes/easterbrook2008selecting.md#e74)
[^easterbrook2008selecting-e10]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e10)
[^ko2015practical-e7]: Ko 等人 2015，§3.1。[证据](../../../../sources/notes/ko2015practical.md#e7)
[^ko2015practical-e28]: Ko 等人 2015，§6.3。[证据](../../../../sources/notes/ko2015practical.md#e28)
[^arcuri2014hitchhiker-e2]: Arcuri & Briand 2014，摘要。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e2)
[^arcuri2014hitchhiker-e4]: Arcuri & Briand 2014，§3。[证据](../../../../sources/notes/arcuri2014hitchhiker.md#e4)
