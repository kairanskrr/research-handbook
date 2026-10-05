# 计算机领域篇：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本文讲计算机领域的研究实际怎样运转：以会议为中心的发表方式、预印本、制品评估，以及这些带来的节奏和惯例。各学科共通的做法（选题、做计划、写作、审稿与回复审稿意见、科研伦理）见[通用篇](../../general/README.md)，这里不重复。具体某一类研究怎么做，见文末的[研究类型](#研究类型)。

**读完本文，你应该能：**

- 说清计算机领域的一篇论文从投稿到发表要经过哪些环节；
- 理解会议、预印本、制品评估在本领域的地位，以及围绕它们的争议；
- 知道自己所在方向有哪些特殊惯例，去哪里查；
- 避开新手在截稿、匿名、预印本和制品上最常犯的错误。

---

## 本领域研究怎样运转

### 会议是主要的发表渠道

在大多数学科，"发表"指在期刊上发表。计算机领域不同：会议论文集是主要的发表渠道，顶级会议的论文就是正式成果，而不是"会议摘要"。CACM（《ACM 通讯》，ACM 即美国计算机协会）主编 Vardi 说，据他所知，计算机是唯一一个以会议为主要发表方式的学科[^vardi2009conferences-e1]。美国计算研究协会（Computing Research Association，CRA）1999 年的一份备忘录明确写道，本领域更看重会议发表[^cra1999evaluating-e1]，并且顶级会议通常比顶级期刊更难中[^cra1999evaluating-e3]。

理论方向是个例外：理论界也看重会议，但有把会议论文补全、扩展后再投期刊的长期传统[^cra1999evaluating-e4]。

计算机领域还有一个底层特点：很多研究对象是人造出来的。造出一个新东西本身不算贡献，**必须证明它更好**[^cra1999evaluating-e6]。所以本领域的大部分论文都在回答"新方法比已有方法好在哪里、好多少"，评估做得好不好，直接决定论文的命运。怎样做公平的比较，见通用篇的[证据、分析与效度](../../general/2_during/02_evidence_and_validity.md)。

### 一篇会议论文的一生

各会议的流程大同小异。下面以安全方向的 USENIX Security（USENIX 协会主办的安全顶级会议）和机器学习方向的 NeurIPS 为例（具体日期和规则每年会变，**以你要投的会议当年的征稿启事为准**）：

| 环节 | 发生什么 | 例子 |
|---|---|---|
| 征稿启事（Call for Papers，CFP） | 公布截稿日期、页数、匿名规则、伦理和制品要求 | NeurIPS 正文限 9 页，含图表[^neurips2025cfp-e2] |
| 截稿 | 常常先注册标题和摘要，几天后交全文；时间多按"地球上任何地方"（Anywhere on Earth，AoE）计算 | NeurIPS 2025 摘要 5 月 11 日、全文 5 月 15 日截止[^neurips2025cfp-e1] |
| 程序委员会（Program Committee，PC）审稿 | 委员会成员审稿，大会议还有领域主席（Area Chair，AC）汇总意见并参与决定[^parikh2020rebuttals-e2] | 有的会议先发"早期拒稿"通知[^usenixsec2026cfp-e1] |
| 作者回复（rebuttal） | 作者看到初审意见后，在很短的时间内书面回复 | NeurIPS 给一周[^neurips2025cfp-e8] |
| 录用决定、定稿（camera-ready） | 录用后按意见修改，提交最终版 | |
| 制品评估（部分方向） | 录用后另交代码、数据等，由专门委员会评估并发徽章 | 见下文 |
| 会议报告 | 在会上做报告，和同行面对面交流 | |

有的会议一年有多轮投稿，例如 USENIX Security 2026 分两轮，每轮都有截稿、早期拒稿、作者回复期等固定节点[^usenixsec2026cfp-e1]。

回复审稿意见是计算机会议的一个重要环节。它的读者不只是审稿人，还有做最终决定的领域主席，后者可能只读审稿意见和你的回复[^parikh2020rebuttals-e2]；所以回复要全面、直接、容易看懂[^parikh2020rebuttals-e1]。具体写法见通用篇的[审稿、回复审稿意见与发表](../../general/3_after/02_reviewing_and_publishing.md)。

### 双盲评审与预印本

很多会议采用**双盲评审**：审稿人不知道作者是谁，作者也不知道审稿人是谁。投稿（包括补充材料和代码链接）不能暴露作者身份[^neurips2025cfp-e4]；引用自己以前的工作，要用第三人称，像引用别人的一样[^usenixsec2026cfp-e4]。隐去作者信息、让作者回复初审意见，都是会议为了让评审更公平而做的尝试[^fortnow2009time-e4]。

与此同时，本领域普遍在 arXiv（一个免费的预印本网站）上公开论文。双盲和预印本看起来矛盾，多数会议的处理办法是**允许，但不能故意暴露身份**：

- NeurIPS：在 arXiv 等处发了署名的预印本不会因此被拒，审稿人被要求不要主动去搜[^neurips2025cfp-e5]；但公开版本不要写"正在 NeurIPS 审稿中"之类的话[^neurips2025cfp-e6]。
- USENIX Security：审稿期间作者仍可做报告、发预印本、披露漏洞[^usenixsec2026cfp-e3]。
- 软件工程的 ACM SIGSOFT（美国计算机协会软件工程分会）实证标准：预印本不算"已发表"[^ralph2020empirical-e141]。

注意"已发表"的边界：NeurIPS 允许投在研讨会（workshop）上报告过的论文，前提是它没有进入正式论文集[^neurips2025cfp-e7]。同一工作同时投多个地方，属于不诚实行为[^usenixsec2026cfp-e11]。

### 制品评估与徽章

计算机实验方向有一个重要传统：尽可能把自己做出来的东西分享给其他研究者[^cra1999evaluating-e5]。这里的**制品**（artifact）指论文背后的代码、数据、系统、证明脚本等。ACM（美国计算机协会）的立场是：实验结果只有能被独立复现，才算真正确立[^acm2020artifact-e9]。

为此，ACM 定义了三类相互独立的徽章[^acm2020artifact-e11]：

| 徽章 | 含义 |
|---|---|
| 制品已评估（Artifacts Evaluated） | "可用"级：有文档、与论文一致、尽量完整、能运行[^acm2020artifact-e2]；"可复用"级：文档和结构好到别人能直接复用[^acm2020artifact-e12] |
| 制品可获取（Artifacts Available） | 放在公开的长期存档库里，个人主页不算[^acm2020artifact-e13] |
| 结果已验证（Results Validated） | 别人重做得到一致的结果；不要求数字完全一致，只要在可接受误差内、不改变主要结论[^acm2020artifact-e14] |

制品评估通常是**自愿的**[^acm2020artifact-e10]。在系统方向，评估多在论文录用之后进行[^sysartifactsguide-e1]，评估标准是制品是否符合论文本身设定的预期[^sysartifactsguide-e4]。参与已经很普遍：OSDI（操作系统设计与实现会议，系统方向的顶级会议）2023 有 64% 的录用论文参加了制品评估[^sysartifactsguide-e3]。也有会议更进一步：USENIX Security 2026 要求审稿期间就提供制品，做不到要说明原因[^usenixsec2026cfp-e12]；NeurIPS 鼓励录用论文同时提交代码和数据[^neurips2025cfp-e10]。

---

## 和其他领域不同的地方

### 会议还是期刊：一直有争议

两者的主要区别 `[本项目分析，依据下列资料]`：

| | 会议 | 期刊 |
|---|---|---|
| 审稿 | 有固定日程，一次决定；作者回复的机会通常只有一次[^neurips2025cfp-e8] | 可以多轮修改 |
| 速度 | 快（CRA 1999 年的数字是 7 个月）[^cra1999evaluating-e2] | 慢（同一来源：1～2 年） |
| 篇幅 | 页数限制严，打磨时间少[^cra1999evaluating-e7] | 较宽松 |
| 在本领域的地位 | 多数方向以顶级会议为主 | 理论方向常把会议论文扩展成期刊版[^cra1999evaluating-e4] |

> **不同的看法：以会议为主好不好？**
> - **支持**：CRA 1999 年的备忘录认为，对实验方向，会议发表更快（当时是 7 个月对 1～2 年）、能当面向同行报告、每篇得到的审稿意见更多（4～5 份对 2～3 份）[^cra1999evaluating-e2]；不足只在篇幅限制严、打磨时间少[^cra1999evaluating-e7]。
> - **反对**：Vardi 认为程序委员会在极大的时间和工作量压力下审稿，达不到仔细审阅的水平[^vardi2009conferences-e2]；人们期待会议论文之后出期刊版，实际上只有一小部分会这样做[^vardi2009conferences-e3]。快速传播也不一定要靠会议，物理学家靠 arXiv 预印本就做到了[^vardi2009conferences-e4]。Fortnow 主张用预印本网站做快速传播，用期刊来评价研究者[^fortnow2009time-e7]。
>
> 对新手来说，这场争论不改变现实：招聘时，人们首先看候选人发表在哪些会议[^fortnow2009time-e6]。实际做法是：**按你所在方向的惯例投稿**，同时清楚会议审稿的局限，不把一次录用或拒稿看得太重。

### 截止日期决定节奏，也有代价

会议有固定截稿日，整个领域的节奏围着截稿日转。这带来效率，也带来副作用。Fortnow 指出：

- 会议模式把研究推向短期、被截止日期驱动的方向[^fortnow2009time-e1]；
- 大家按截止日期而不是按研究是否成熟来投稿，不少人只发"最小可发表单元"[^fortnow2009time-e2]；
- 程序委员会靠共识做决定，容易偏向稳妥的增量工作，而不是探索新方向的论文[^fortnow2009time-e3]；
- 特别好和特别差的论文结果比较确定，中间那一大批扎实的论文结果带有很大偶然性[^fortnow2009time-e5]。近一半哥德尔奖（理论计算机最佳论文奖）获奖论文，最初被顶级理论会议拒过或根本没在那里发表[^fortnow2009time-e8]。

### 各方向的惯例不一样

计算机各方向差别很大，判断一篇论文够不够格，要了解目标会议和学术社区的标准[^hicks2014reviewing-e9]。下表只列本文资料能支持的几点，**以目标会议的征稿启事为准**：

| 方向 | 值得注意的惯例（举例） |
|---|---|
| 理论 | 结果以定理和证明为主；会议论文常扩展成期刊版[^cra1999evaluating-e4] |
| 系统 | 制品评估普遍；评估在录用后进行，时间紧[^sysartifactsguide-e2] |
| 安全 | 必须讨论研究伦理，USENIX Security 要求单列"伦理考虑"附录[^usenixsec2026cfp-e2]；涉及漏洞要负责任地披露（见下文） |
| 机器学习 | 双盲加 arXiv 预印本并存[^neurips2025cfp-e5]；投稿要填论文检查清单[^neurips2025cfp-e3]；录用论文的审稿意见和讨论会公开[^neurips2025cfp-e9] |
| 软件工程 | ACM SIGSOFT 实证标准按研究方法分别给出评审标准，没有通用的质量标准[^ralph2020empirical-e142] |

### 伦理问题有本领域的特点

通用的伦理原则见通用篇的[科研诚信与伦理](../../general/4_throughout/02_integrity_and_ethics.md)。计算机领域，尤其是安全和网络测量方向，有几点需要特别注意：

- **漏洞要先私下告知，再公开。** 在告知负责方、漏洞被修复之前就公开，会让人受到伤害[^usenixsec2026cfp-e5]；论文里要写清向谁披露了、结果如何[^usenixsec2026cfp-e6]。
- **伦理审查委员会（Institutional Review Board，IRB）批准不等于没有伦理问题。** IRB 不一定了解计算机安全研究的惯例，批准了也仍然要自己分析[^usenixsec2026cfp-e7]。
- **用《Menlo 报告》做分析框架。** USENIX Security 建议作者熟悉它[^usenixsec2026cfp-e10]。它在尊重个人、有益、公正之外，加了一条尊重法律和公共利益[^bailey2012menlo-e2]。
- **越早考虑越好**[^usenixsec2026cfp-e9]。有时最合乎伦理的选择是不做，或做完了不发表[^usenixsec2026cfp-e8]。
- **有破坏性的制品要醒目标明**，让评估者提前做好防护[^sysartifactsguide-e7]。

软件工程的实证标准也把"承认并减轻研究可能带来的风险和伤害"列为必要项[^ralph2020empirical-e65]。

---

## 给新手的建议

1. **先把目标会议的征稿启事从头读到尾。** 页数、匿名规则、预印本政策、伦理附录、制品要求，每个会议都不一样，违反格式或匿名规则可能直接被拒。也要读这类研究已有的指南；不读指南就动手，是软件工程实证标准明确列出的反面做法[^ralph2020empirical-e26]。
2. **从截稿日往回排计划。** 三个月后截稿，至少提前一个月开始写[^parikh2018calendar-e5]；至少提前一周写完，导师才有时间给出有用的反馈[^dredze2012successful-e21]。可以在正式截稿前两周设一个组内截稿，按正式审稿的方式内部评审[^karpathy2016survival-e8]。
3. **论文还在审，就开始准备制品。** 录用到提交制品之间时间很短[^sysartifactsguide-e2]。依赖复杂的，用容器或虚拟机打包[^sysartifactsguide-e6]；按自己写的步骤，在全新的环境里跑一遍[^sysartifactsguide-e5]。整理代码和数据的通用做法见通用篇的[整理科研材料](../../general/2_during/03_organizing_materials.md)。
4. **发预印本前查清政策，发了也别破坏匿名。** 不在公开版本里写"正在某会议审稿中"[^neurips2025cfp-e6]，投稿版本里用第三人称引用自己的工作[^usenixsec2026cfp-e4]。
5. **把作者回复当成正式环节来准备。** 时间只有几天到一周[^neurips2025cfp-e8]，要写给做决定的领域主席看[^parikh2020rebuttals-e2]。
6. **不要被截稿日推着发半成品。** 研究没成熟时，等下一个截稿日往往比硬投更好[^fortnow2009time-e2] `[本项目分析]`。
7. **被拒很正常，不要只凭一次结果判断工作的价值。** 中间档论文的结果偶然性很大[^fortnow2009time-e5]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 没读征稿启事就按别的会议的格式写 | 页数、匿名、伦理附录等要求各不相同，不合规可能直接被拒[^usenixsec2026cfp-e2] |
| 投稿里写"我们之前的工作[5]"，或代码链接指向自己署名的仓库 | 破坏双盲，可能被拒[^neurips2025cfp-e4][^usenixsec2026cfp-e4] |
| 预印本里写"正在 NeurIPS 审稿中" | 会议明确不允许[^neurips2025cfp-e6] |
| 把同一工作同时投两个会议 | 属于不诚实行为[^usenixsec2026cfp-e11] |
| 录用后才开始整理代码，赶不上制品评估 | 录用到提交制品之间时间很短[^sysartifactsguide-e2] |
| 把制品放在个人主页上就算"公开" | 不满足"可获取"徽章的长期存档要求[^acm2020artifact-e13] |
| 发现漏洞后先公开再通知厂商 | 修复前公开会让用户受到伤害[^usenixsec2026cfp-e5] |
| 以为 IRB 批准了就不用写伦理分析 | IRB 批准不能代替伦理分析[^usenixsec2026cfp-e7] |
| 用一个方向的标准去评判另一个方向的论文 | 没有通用的质量标准，各方向、各方法标准不同[^ralph2020empirical-e142] |

---

## 研究类型

计算机领域常见的几类研究，各有专门的文档：

- [综述研究](research-types/review_study.md)：系统综述、映射研究与综述论文
- [工程研究](research-types/engineering_research.md)：提出并评估新的方法、工具或系统
- [基准测试](research-types/benchmarking.md)：用基准比较性能
- [仓库挖掘](research-types/repository_mining.md)：分析代码仓库、缺陷记录等软件开发数据

---

## 延伸阅读

- **CRA 1999，Evaluating Computer Scientists and Engineers for Promotion and Tenure**：篇幅短，讲清为什么本领域以会议为主、为什么看重制品。适合想了解本领域发表文化由来的人。
- **Vardi 2009 和 Fortnow 2009（CACM）**：对会议文化的两篇著名批评。适合想了解会议审稿局限、截稿驱动研究的代价的人。
- **ACM Artifact Review and Badging**：徽章的正式定义，以及重复、复现、再现三个术语的区别。准备制品评估前读。
- **sysartifacts.github.io 的打包指南**：系统方向制品评估的实操指南，含格式选择、工具和小技巧。
- **你要投的会议的征稿启事**，例如 USENIX Security 的伦理指南、NeurIPS 的预印本和双盲政策。每次投稿前都要重新读。

[^cra1999evaluating-e1]: CRA 1999（Patterson、Snyder、Ullman），开头。[证据](../../../sources/notes/cra1999evaluating.md#e1)
[^cra1999evaluating-e2]: CRA 1999，Structure of The Field。[证据](../../../sources/notes/cra1999evaluating.md#e2)
[^cra1999evaluating-e3]: CRA 1999，Structure of The Field。[证据](../../../sources/notes/cra1999evaluating.md#e3)
[^cra1999evaluating-e4]: CRA 1999，Structure of The Field。[证据](../../../sources/notes/cra1999evaluating.md#e4)
[^cra1999evaluating-e5]: CRA 1999，Structure of The Field。[证据](../../../sources/notes/cra1999evaluating.md#e5)
[^cra1999evaluating-e6]: CRA 1999，Structure of The Field（引 Fred Brooks）。[证据](../../../sources/notes/cra1999evaluating.md#e6)
[^cra1999evaluating-e7]: CRA 1999，Structure of The Field。[证据](../../../sources/notes/cra1999evaluating.md#e7)
[^vardi2009conferences-e1]: Vardi 2009，正文第 2 段。[证据](../../../sources/notes/vardi2009conferences.md#e1)
[^vardi2009conferences-e2]: Vardi 2009，正文第 6 段。[证据](../../../sources/notes/vardi2009conferences.md#e2)
[^vardi2009conferences-e3]: Vardi 2009，正文第 6 段。[证据](../../../sources/notes/vardi2009conferences.md#e3)
[^vardi2009conferences-e4]: Vardi 2009，正文第 7 段。[证据](../../../sources/notes/vardi2009conferences.md#e4)
[^fortnow2009time-e1]: Fortnow 2009，摘要段。[证据](../../../sources/notes/fortnow2009time.md#e1)
[^fortnow2009time-e2]: Fortnow 2009，正文。[证据](../../../sources/notes/fortnow2009time.md#e2)
[^fortnow2009time-e3]: Fortnow 2009，正文。[证据](../../../sources/notes/fortnow2009time.md#e3)
[^fortnow2009time-e4]: Fortnow 2009，正文。[证据](../../../sources/notes/fortnow2009time.md#e4)
[^fortnow2009time-e5]: Fortnow 2009，正文。[证据](../../../sources/notes/fortnow2009time.md#e5)
[^fortnow2009time-e6]: Fortnow 2009，正文。[证据](../../../sources/notes/fortnow2009time.md#e6)
[^fortnow2009time-e7]: Fortnow 2009，摘要段。[证据](../../../sources/notes/fortnow2009time.md#e7)
[^fortnow2009time-e8]: Fortnow 2009，正文。[证据](../../../sources/notes/fortnow2009time.md#e8)
[^acm2020artifact-e9]: ACM Artifact Review and Badging v1.1，开头。[证据](../../../sources/notes/acm2020artifact.md#e9)
[^acm2020artifact-e10]: ACM Artifact Review and Badging v1.1，开头。[证据](../../../sources/notes/acm2020artifact.md#e10)
[^acm2020artifact-e11]: ACM Artifact Review and Badging v1.1，Badging。[证据](../../../sources/notes/acm2020artifact.md#e11)
[^acm2020artifact-e2]: ACM Artifact Review and Badging v1.1，Artifacts Evaluated – Functional。[证据](../../../sources/notes/acm2020artifact.md#e2)
[^acm2020artifact-e12]: ACM Artifact Review and Badging v1.1，Artifacts Evaluated – Reusable。[证据](../../../sources/notes/acm2020artifact.md#e12)
[^acm2020artifact-e13]: ACM Artifact Review and Badging v1.1，Artifacts Available。[证据](../../../sources/notes/acm2020artifact.md#e13)
[^acm2020artifact-e14]: ACM Artifact Review and Badging v1.1，Results Validated。[证据](../../../sources/notes/acm2020artifact.md#e14)
[^sysartifactsguide-e1]: sysartifacts，OSDI '24 Call for Artifacts，Benefits and Goals。[证据](../../../sources/notes/sysartifactsguide.md#e1)
[^sysartifactsguide-e2]: sysartifacts，OSDI '24 Call for Artifacts，Overview。[证据](../../../sources/notes/sysartifactsguide.md#e2)
[^sysartifactsguide-e3]: sysartifacts，OSDI '24 Call for Artifacts，Overview。[证据](../../../sources/notes/sysartifactsguide.md#e3)
[^sysartifactsguide-e4]: sysartifacts，OSDI '24 Call for Artifacts，Criteria。[证据](../../../sources/notes/sysartifactsguide.md#e4)
[^sysartifactsguide-e5]: sysartifacts，打包指南，Tools and tips。[证据](../../../sources/notes/sysartifactsguide.md#e5)
[^sysartifactsguide-e6]: sysartifacts，打包指南，Formats。[证据](../../../sources/notes/sysartifactsguide.md#e6)
[^sysartifactsguide-e7]: sysartifacts，打包指南，Formats。[证据](../../../sources/notes/sysartifactsguide.md#e7)
[^usenixsec2026cfp-e1]: USENIX Security '26 征稿启事，Important Dates。[证据](../../../sources/notes/usenixsec2026cfp.md#e1)
[^usenixsec2026cfp-e2]: USENIX Security '26 征稿启事，Executive Summary。[证据](../../../sources/notes/usenixsec2026cfp.md#e2)
[^usenixsec2026cfp-e3]: USENIX Security '26 征稿启事，Anonymous Submission。[证据](../../../sources/notes/usenixsec2026cfp.md#e3)
[^usenixsec2026cfp-e4]: USENIX Security '26 征稿启事，Anonymous Submission。[证据](../../../sources/notes/usenixsec2026cfp.md#e4)
[^usenixsec2026cfp-e5]: USENIX Security '26 伦理指南，Disclosures。[证据](../../../sources/notes/usenixsec2026cfp.md#e5)
[^usenixsec2026cfp-e6]: USENIX Security '26 伦理指南，Disclosures。[证据](../../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e7]: USENIX Security '26 伦理指南，IRB 一问。[证据](../../../sources/notes/usenixsec2026cfp.md#e7)
[^usenixsec2026cfp-e8]: USENIX Security '26 伦理指南。[证据](../../../sources/notes/usenixsec2026cfp.md#e8)
[^usenixsec2026cfp-e9]: USENIX Security '26 伦理指南，何时开始考虑伦理。[证据](../../../sources/notes/usenixsec2026cfp.md#e9)
[^usenixsec2026cfp-e10]: USENIX Security '26 伦理指南。[证据](../../../sources/notes/usenixsec2026cfp.md#e10)
[^usenixsec2026cfp-e11]: USENIX Security '26 征稿启事，Simultaneous Submission and Plagiarism。[证据](../../../sources/notes/usenixsec2026cfp.md#e11)
[^usenixsec2026cfp-e12]: USENIX Security '26 征稿启事，Executive Summary。[证据](../../../sources/notes/usenixsec2026cfp.md#e12)
[^neurips2025cfp-e1]: NeurIPS 2025 征稿启事，日期列表。[证据](../../../sources/notes/neurips2025cfp.md#e1)
[^neurips2025cfp-e2]: NeurIPS 2025 征稿启事，Paper Formatting Instructions。[证据](../../../sources/notes/neurips2025cfp.md#e2)
[^neurips2025cfp-e3]: NeurIPS 2025 征稿启事，Paper Checklist。[证据](../../../sources/notes/neurips2025cfp.md#e3)
[^neurips2025cfp-e4]: NeurIPS 2025 征稿启事，Double-blind Reviewing。[证据](../../../sources/notes/neurips2025cfp.md#e4)
[^neurips2025cfp-e5]: NeurIPS 2025 征稿启事，Preprints。[证据](../../../sources/notes/neurips2025cfp.md#e5)
[^neurips2025cfp-e6]: NeurIPS 2025 征稿启事，Preprints。[证据](../../../sources/notes/neurips2025cfp.md#e6)
[^neurips2025cfp-e7]: NeurIPS 2025 征稿启事，Dual Submissions。[证据](../../../sources/notes/neurips2025cfp.md#e7)
[^neurips2025cfp-e8]: NeurIPS 2025 征稿启事，Author Responses。[证据](../../../sources/notes/neurips2025cfp.md#e8)
[^neurips2025cfp-e9]: NeurIPS 2025 征稿启事，Publication of Accepted Submissions。[证据](../../../sources/notes/neurips2025cfp.md#e9)
[^neurips2025cfp-e10]: NeurIPS 2025 征稿启事，Publication of Accepted Submissions。[证据](../../../sources/notes/neurips2025cfp.md#e10)
[^ralph2020empirical-e141]: SIGSOFT General Standard，Initial Checks。[证据](../../../sources/notes/ralph2020empirical.md#e141)
[^ralph2020empirical-e142]: SIGSOFT General Standard，General Quality Criteria。[证据](../../../sources/notes/ralph2020empirical.md#e142)
[^ralph2020empirical-e65]: SIGSOFT General Standard，必要项。[证据](../../../sources/notes/ralph2020empirical.md#e65)
[^ralph2020empirical-e26]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e26)
[^hicks2014reviewing-e9]: Hicks 2014，Interesting or useful?。[证据](../../../sources/notes/hicks2014reviewing.md#e9)
[^parikh2020rebuttals-e1]: Parikh 等人 2020，开头。[证据](../../../sources/notes/parikh2020rebuttals.md#e1)
[^parikh2020rebuttals-e2]: Parikh 等人 2020，谁读回复。[证据](../../../sources/notes/parikh2020rebuttals.md#e2)
[^parikh2018calendar-e5]: Parikh 2018，Principle 6。[证据](../../../sources/notes/parikh2018calendar.md#e5)
[^dredze2012successful-e21]: Dredze & Wallach 2012，#46。[证据](../../../sources/notes/dredze2012successful.md#e21)
[^karpathy2016survival-e8]: Karpathy 2016，Writing papers。[证据](../../../sources/notes/karpathy2016survival.md#e8)
[^bailey2012menlo-e2]: Bailey 等人 2012，第 72 页。[证据](../../../sources/notes/bailey2012menlo.md#e2)
