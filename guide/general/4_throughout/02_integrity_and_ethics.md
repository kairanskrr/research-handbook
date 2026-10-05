# 科研诚信与伦理

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲做研究时的几条底线：对证据诚实，完整报告结果，让别人能核查你的工作，保护研究涉及的人，以及署名和引用的基本规矩。统计分析和效度的具体方法见[证据、分析与效度](../2_during/02_evidence_and_validity.md)；和合作者怎么分工、怎么谈署名，见[合作与导师](../4_throughout/01_collaboration_and_advisors.md)。

**读完本章，你应该能：**

- 说清什么是学术不端（伪造、篡改、剽窃），什么是同样要避开的"可疑做法"；
- 完整报告结果，包括负面结果和局限，不挑拣；
- 把数据、代码和分析过程保存好，让别人和一年后的你都能复现；
- 在涉及人的研究中处理好知情同意、风险和隐私；
- 按通行标准决定谁署名、谁写进致谢。

---

## 1. 先做到不骗自己

**为什么这是诚信问题：** Feynman 把科学诚信的第一条原则概括为：不要骗自己，而你自己恰恰是最容易被骗的人[^feynman1974cargo-e7]。《欧洲科研诚信行为准则》（欧洲科学与人文学院联合会 ALLEA 制定，适用于所有学科[^allea2023european-e18]）把"诚实"列为四条基本原则之一，要求研究从开展到报告、交流，都做到透明、公平、完整、无偏[^allea2023european-e1]。

**底线在哪：**

- 和你的观点不一致的事实，跟一致的事实一起写出来[^feynman1974cargo-e4]。
- 检查要对称：结果"不好"时你会到处找错，结果"好"时也要用同样的力度去查。Feynman 举过物理学史上的例子：后来的人测出的数值偏离权威结果时拼命找错，接近时就不怎么查[^feynman1974cargo-e14]。
- 推测可以写，但要标明是推测，不能写得像有证据的结论[^lipton2019troubling-e11][^lipton2019troubling-e3]。

这种错误谁都会犯。Lipton 和 Steinhardt 在批评这类问题时，承认自己也写过"伪装成解释的推测"[^lipton2019troubling-e12]。

具体怎么做（列出可能推翻结论的因素、分开结果和推测），见[什么是研究，什么是好的研究：只提出证据支持的主张](../1_before/01_what_is_good_research.md#5-只提出证据支持的主张不要骗自己)和[证据、分析与效度：诚实报告](../2_during/02_evidence_and_validity.md#7-诚实报告负面结果局限和推测)。

## 2. 报告全部结果，包括负面结果

**底线在哪：**

- 决定检验一个想法时，就要决定无论结果如何都报告。只发表某一类结果，论证就会显得比实际更有力[^feynman1974cargo-e9]。
- 不要只报告"显著"的那部分统计检验，也就是"p 值操纵"（p-hacking）[^ralph2020empirical-e27]。统计检验用来判断一个结果有多大可能只是偶然出现；"显著"指检验认为它不太像是偶然。
- 在声称是验证性的研究里（事先提出假设，再收集数据检验），不要先看结果，再把假设写成像是事先就有的，也就是"结果已知后再提假设"（HARKing，Hypothesizing After Results are Known）[^ralph2020empirical-e27]。探索性分析中产生的假设本身没问题，但要标明是探索性的。`[本项目分析]`（两者的区别见[研究设计与方法选择：分清探索性研究和验证性研究](../1_before/04_research_design.md#4-分清探索性研究和验证性研究)。）
- 计算类研究中，方法里有随机性时，报告所有运行的结果，不要反复运行、只挑最好的一次[^zeller2021devil-e1]；和别人的方法比较时，给对方同样的调参机会[^zeller2021devil-e2]。
- 局限写进正文，结论要和局限对得上[^ralph2020empirical-e66]。

**为什么：** 负面结果可能和正面结果同样有价值，同样值得发表和传播[^allea2023european-e12]；在 ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准里，"因为结果是负面的就拒稿"被列为不成立的审稿意见[^ralph2020empirical-e41]。

具体怎么做，见[证据、分析与效度：诚实报告](../2_during/02_evidence_and_validity.md#7-诚实报告负面结果局限和推测)。

> **"魔鬼的建议"：哪些"不算不端"，哪些已经越线**
>
> Zeller 用反讽的口吻列出了一批"论文数量上去了、研究价值下来了"的套路[^zeller2021devil-e7]，例如反复运行直到赢一次，悄悄丢掉之前的结果[^zeller2021devil-e1]；只给自己的方法调参[^zeller2021devil-e2]；"成果写进标题，局限塞进脚注"[^zeller2021devil-e3]。他还列了一串：不预注册、不记实验日志、不留版本历史、不测试代码、不验证结果、什么都不共享，并反讽说"这些都不算学术不端！"[^zeller2021devil-e8] Patterson 列的"坏论文戒律"里也有一条：不要提你方法的缺点[^patterson2001bad-e8]。
>
> 要分清：Zeller 说"不算不端"的，是后面那一串（不记日志、不共享等）。它们不违规，却会让结果不可信。而"悄悄丢掉不利的运行结果"可能已经越过红线：无正当理由地删除或隐瞒数据和结果，属于篡改[^allea2023european-e3]（见本章[守住红线](#6-守住红线发现错误主动更正)）。`[本项目分析]`

## 3. 让结果能被复现：记录、保存、共享

**为什么：**

- 可复现是让别人能核查你的结论的前提。报告方法时，要做到便于别人核查或重复[^allea2023european-e14]；要报告足够的细节，让别人能复现结果[^patterson2001bad-e9]。
- 它也保护你自己。如果回不到产生某个结果的那版代码，就没法判断这个结果是不是程序错误造成的[^sandve2013ten-e1][^sandve2013ten-e4]。这些做法最大的受益者是未来的自己：三个月前的你不会回邮件[^wilson2017good-e2]。
- 让同行真能复现，本身就是质量和可信度的有力信号[^sandve2013ten-e6]。

怎样记录每个结果的来历、保护原始数据、做版本控制，见[整理科研材料](../2_during/03_organizing_materials.md)。这里只讲发表时的数据共享和存档：

- **在合理且写明的期限内保存数据、代码等研究材料**[^allea2023european-e15]。
- **发表时公开数据和代码**：存到能分配 DOI（Digital Object Identifier，数字对象标识符，一种不会随网址变化而失效的永久编号）的可靠仓库，写明许可协议[^wilson2017good-e4]。个人网站、GitHub、网盘都不算妥善的长期存档[^ralph2020empirical-e78]；可以考虑 Zenodo（一个免费的科研成果存档平台）、OSF（Open Science Framework，开放科学框架）或所在机构的仓库。`[本项目分析]`
- **不能公开时说明原因。** 原则是"尽可能开放，必要时封闭"：有伦理、法律等障碍时可以不公开[^ralph2020empirical-e76][^allea2023european-e15]。例如访谈记录很难可靠地匿名化，就可能属于这种情况。`[本项目分析]`

这些规则多出自计算类研究，但"记录过程、保存原始数据、公开材料"对所有学科都成立；实验记录本、问卷原始数据、访谈录音，同样要这样对待。`[本项目分析]`

## 4. 研究涉及人时，先保护人

技术的进步拉开了"研究者能做什么"和"应该做什么"之间的距离[^bailey2012menlo-e1]。不只是医学和心理学，任何会接触人、收集人的数据、或者可能影响别人的研究，都要考虑伦理。`[本项目分析]`

**先看所在学科和机构的规定。** 医学、心理学、社会科学等学科都有自己的伦理规范；做涉及人的研究，首先要遵守所在机构伦理审查委员会（国外常叫 IRB，Institutional Review Board）的规定。下面的 Menlo 报告和 SIGSOFT 标准出自计算领域，只是一个例子，用来说明通常要考虑哪些方面。`[本项目分析]`

**四条原则（以 Menlo 报告为例）。** 《Menlo 报告》是面向信息与通信技术研究的一份伦理原则报告，它沿用了《贝尔蒙报告》（Belmont Report，全称为保护人体研究对象的伦理原则和指南[^bailey2012menlo-e7]）的三条原则，又加了一条[^bailey2012menlo-e2]：

| 原则 | 具体要求 |
|---|---|
| 尊重个人 | 参与是自愿的，以知情同意为前提；不是研究对象、但会受研究影响的人，也要保护[^bailey2012menlo-e3] |
| 有益 | 避免伤害；尽量增大收益、减小伤害；系统评估风险和收益[^bailey2012menlo-e4] |
| 公正 | 公平选择研究对象，负担在受影响的人之间公平分配[^bailey2012menlo-e5] |
| 尊重法律和公共利益 | 做好法律上的尽职调查（事先查清研究涉及哪些法律要求，并照做）；方法和结果透明；对自己的行为负责[^bailey2012menlo-e6] |

**有人参与的研究，论文里要写清**（依据 SIGSOFT 伦理补充标准[^ralph2020empirical-e68][^ralph2020empirical-e69][^ralph2020empirical-e70]和 ALLEA 准则）：

- [ ] 参与者可能面临哪些风险或伤害，采取了哪些措施减轻，研究收益为什么值得这些风险
- [ ] 怎样招募参与者，给了什么报酬，怎样避免强迫
- [ ] 怎样取得自由、个人、知情的同意
- [ ] 怎样保护隐私：匿名化时，要考虑别人把多个数据来源拼起来、重新认出参与者的可能
- [ ] 按所在机构的要求申请伦理审查，并在论文里注明批准编号。这首先是机构的要求；SIGSOFT 标准只把注明批准编号列为加分项[^ralph2020empirical-e73]
- [ ] 事先告诉参与者，他们的数据将怎样使用、存储和删除[^allea2023european-e17]

**容易错在哪：**

- 用"研究总体上是有益的"来为风险辩护，而不是论证"这项研究"的具体收益；招募时淡化风险[^ralph2020empirical-e71]。
- 只想到参与者。风险也可能落在研究的应用、社会和环境上，同样要识别、权衡、减轻[^allea2023european-e16][^ralph2020empirical-e65]。
- 研究必须用到欺骗（如不告诉参与者真实目的）时，知情同意的要求可以调整，但必须在论文里完整说明[^ralph2020empirical-e72]。

> **不同的看法：守法和伦理冲突时怎么办？**
>
> - **以守法为原则**：Menlo 报告把"尊重法律和公共利益"列为四条原则之一，要求做法律上的尽职调查[^bailey2012menlo-e6]；ALLEA 准则要求遵守相关规范和法规[^allea2023european-e16]。
> - **伦理和合法性一起权衡**：SIGSOFT 伦理补充标准认为，极少数情况下，合乎伦理的研究可能需要违法的行为，应当把伦理性和合法性放在一起权衡[^ralph2020empirical-e75]；它还认为"没有经过伦理审查"本身不构成拒稿理由，除非存在审查本应阻止的实质问题[^ralph2020empirical-e74]。
>
> 实际操作：新手默认守法，并走完所在机构的伦理审查。遇到灰色地带，先找导师和伦理委员会商量，不要自己判断。`[本项目分析]`

## 5. 署名和引用：给每个贡献者应得的认可

**谁该署名。** ALLEA 准则给出四个条件[^allea2023european-e7]：

1. 对研究设计、数据收集、分析或解释有实质贡献；
2. 起草论文，或对论文做过批判性修改；
3. 同意最终版本；
4. 同意对论文内容负责。

有贡献但不满足这些条件的人，例如合作者、助手、资助方，写进致谢[^allea2023european-e8]。署名顺序要由作者们正式商定[^allea2023european-e8]，最好在项目开始时就谈。`[本项目分析]`

**怎么做：**

- 用了别人的想法、数据、代码或文字，都要注明出处。不注明就是剽窃[^allea2023european-e3]。
- 重复使用自己已发表的内容，包括翻译成另一种语言再发，也要注明，否则是"自我剽窃"[^allea2023european-e5]。
- 引用要准确，不要只引对自己有利的文献[^allea2023european-e4]。
- 披露所有经济和非经济的利益冲突，以及资助来源[^allea2023european-e10]。
- 公开发布前核对：作者是否列全，姓名和单位是否正确，匿名投稿时注释掉的致谢是否恢复[^carlini2022checklist-e2]。每犯一次这类错误，就把它加进自己的发布清单[^carlini2022checklist-e1]。

## 6. 守住红线；发现错误，主动更正

**学术不端的传统定义是"FFP"**[^allea2023european-e3]：

| 类型 | 含义 |
|---|---|
| 伪造（Fabrication） | 编造数据或结果，当作真的记录下来 |
| 篡改（Falsification） | 操纵材料、设备、图像或流程；或无正当理由地改动、删除、隐瞒数据或结果 |
| 剽窃（Plagiarism） | 使用他人的成果或想法，却不恰当注明出处 |

**FFP 之外，下面这些同样不可接受**：滥用统计来制造"显著"；无正当理由扣留数据或结果；选择性或不准确地引用[^allea2023european-e4]；为了增加论文数量把一项研究拆成几篇，即"切香肠"[^allea2023european-e5][^ralph2020empirical-e67]；操纵署名，贬低他人的贡献[^allea2023european-e9]。

**后果不只是个人的。** 违背良好研究规范会损害研究过程和研究者之间的关系，削弱人们对研究的信任和研究的可信度，浪费资源，还可能让参与者、社会或环境受到不必要的伤害[^allea2023european-e6]。

**发现自己发表的论文有错**：及时发更正，必要时撤稿[^allea2023european-e11]。对外介绍研究时，也要说清证据有多可靠，以及还有哪些不确定之处[^allea2023european-e13]。

---

## 本章检查清单

- [ ] 论文写出了可能推翻结论的因素，以及不支持结论的结果[^feynman1974cargo-e3][^feynman1974cargo-e4]
- [ ] 推测和有证据的结论分开写，推测有明确标记[^lipton2019troubling-e3]
- [ ] 报告了全部相关结果，包括负面结果和不显著的检验[^feynman1974cargo-e9][^ralph2020empirical-e27]
- [ ] 结论没有超出证据，与写出的局限一致[^ralph2020empirical-e66]
- [ ] 每个结果都能追溯到代码版本、参数、随机种子和原始数据[^sandve2013ten-e2][^sandve2013ten-e4][^sandve2013ten-e11]
- [ ] 原始数据有两处以上备份[^wilson2017good-e3]
- [ ] 数据和代码已存入长期仓库，有 DOI 和许可协议；不能公开的说明了原因[^wilson2017good-e4][^ralph2020empirical-e77]
- [ ] 有人参与的研究：写清风险、招募、报酬、知情同意和隐私保护[^ralph2020empirical-e68][^ralph2020empirical-e69]，并按机构要求通过了伦理审查
- [ ] 每位作者都满足署名条件，其他贡献者写进了致谢[^allea2023european-e7][^allea2023european-e8]
- [ ] 所有借用的想法、数据、代码和文字都注明了出处，包括自己以前的论文[^allea2023european-e3][^allea2023european-e5]
- [ ] 披露了利益冲突和资助来源[^allea2023european-e10]

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 结果不好时拼命找错，结果好时不查 | 不对称的检查会让错误结论留下来[^feynman1974cargo-e14] |
| 只报告显著的检验，或看完结果再编假设 | 论证显得比实际更有力[^ralph2020empirical-e27][^feynman1974cargo-e9] |
| 计算类研究中，多次运行只报告最好的一次 | 挑出来的结果不代表方法的真实表现[^zeller2021devil-e1] |
| 把推测写得像结论 | 读者分不清什么有证据[^lipton2019troubling-e11] |
| 局限写在一边，结论照旧夸大 | 局限形同虚设[^ralph2020empirical-e66] |
| 代码不做版本控制，原始数据只有一份 | 结果无法追溯，出错时无法判断原因[^sandve2013ten-e4][^wilson2017good-e3] |
| 数据只放在个人网站或网盘上 | 不算妥善的长期存档[^ralph2020empirical-e78] |
| 用"研究总体有益"为参与者的风险辩护 | 要论证的是这项研究的具体收益[^ralph2020empirical-e71] |
| 给没有实质贡献的人署名，或漏掉有贡献的人 | 操纵署名属于不可接受的做法[^allea2023european-e9] |
| 把一项研究拆成几篇发表 | "切香肠"，属于不可接受的做法[^allea2023european-e5] |

## 延伸阅读

- **Feynman，"Cargo Cult Science"**：一篇短演讲，讲清"不要骗自己"和"无论结果如何都发表"，适合入门时读。
- **ALLEA，《欧洲科研诚信行为准则》2023 修订版**：适用于所有学科的权威规范，要查"什么算不端""谁该署名"时看它。
- **Sandve 等人 2013；Wilson 等人 2017**：可复现和数据管理的具体做法，都很短，可以直接照着做。
- **Bailey 等人 2012（Menlo 报告介绍）与 ACM SIGSOFT 伦理补充标准**：设计有人参与的研究、写伦理部分时用。
- **Zeller，"The Devil's Guide to Incremental Research"**：用反讽列出常见的可疑做法，适合拿来对照检查自己。

[^feynman1974cargo-e7]: Feynman 1974，"The first principle" 段。[证据](../../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e3]: Feynman 1974，"leaning over backwards" 段。[证据](../../../sources/notes/feynman1974cargo.md#e3)
[^feynman1974cargo-e4]: Feynman 1974，"Details that could throw doubt" 段。[证据](../../../sources/notes/feynman1974cargo.md#e4)
[^feynman1974cargo-e9]: Feynman 1974，"One example of the principle" 段。[证据](../../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e14]: Feynman 1974，Millikan 油滴实验的例子。[证据](../../../sources/notes/feynman1974cargo.md#e14)
[^lipton2019troubling-e11]: Lipton & Steinhardt 2019，§1。[证据](../../../sources/notes/lipton2019troubling.md#e11)
[^lipton2019troubling-e12]: Lipton & Steinhardt 2019，§3.1。[证据](../../../sources/notes/lipton2019troubling.md#e12)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019，§3.1。[证据](../../../sources/notes/lipton2019troubling.md#e3)
[^allea2023european-e1]: ALLEA 2023，§1。[证据](../../../sources/notes/allea2023european.md#e1)
[^allea2023european-e3]: ALLEA 2023，§3.1。[证据](../../../sources/notes/allea2023european.md#e3)
[^allea2023european-e4]: ALLEA 2023，§3.1。[证据](../../../sources/notes/allea2023european.md#e4)
[^allea2023european-e5]: ALLEA 2023，§3.1。[证据](../../../sources/notes/allea2023european.md#e5)
[^allea2023european-e6]: ALLEA 2023，§3。[证据](../../../sources/notes/allea2023european.md#e6)
[^allea2023european-e7]: ALLEA 2023，§2.7。[证据](../../../sources/notes/allea2023european.md#e7)
[^allea2023european-e8]: ALLEA 2023，§2.7。[证据](../../../sources/notes/allea2023european.md#e8)
[^allea2023european-e9]: ALLEA 2023，§3.1。[证据](../../../sources/notes/allea2023european.md#e9)
[^allea2023european-e10]: ALLEA 2023，§2.7。[证据](../../../sources/notes/allea2023european.md#e10)
[^allea2023european-e11]: ALLEA 2023，§2.7。[证据](../../../sources/notes/allea2023european.md#e11)
[^allea2023european-e12]: ALLEA 2023，§2.7。[证据](../../../sources/notes/allea2023european.md#e12)
[^allea2023european-e13]: ALLEA 2023，§2.7。[证据](../../../sources/notes/allea2023european.md#e13)
[^allea2023european-e14]: ALLEA 2023，§2.3。[证据](../../../sources/notes/allea2023european.md#e14)
[^allea2023european-e15]: ALLEA 2023，§2.5。[证据](../../../sources/notes/allea2023european.md#e15)
[^allea2023european-e16]: ALLEA 2023，§2.4。[证据](../../../sources/notes/allea2023european.md#e16)
[^allea2023european-e17]: ALLEA 2023，§2.5。[证据](../../../sources/notes/allea2023european.md#e17)
[^allea2023european-e18]: ALLEA 2023，Preamble。[证据](../../../sources/notes/allea2023european.md#e18)
[^ralph2020empirical-e65]: SIGSOFT General Standard，必要项。[证据](../../../sources/notes/ralph2020empirical.md#e65)
[^ralph2020empirical-e27]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e66]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e41]: SIGSOFT General Standard，不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e67]: SIGSOFT General Standard，反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e67)
[^ralph2020empirical-e68]: SIGSOFT 伦理补充标准（有人参与的研究），必要项。[证据](../../../sources/notes/ralph2020empirical.md#e68)
[^ralph2020empirical-e69]: SIGSOFT 伦理补充标准（有人参与的研究），必要项。[证据](../../../sources/notes/ralph2020empirical.md#e69)
[^ralph2020empirical-e70]: SIGSOFT 伦理补充标准（有人参与的研究），必要项脚注 2。[证据](../../../sources/notes/ralph2020empirical.md#e70)
[^ralph2020empirical-e71]: SIGSOFT 伦理补充标准（有人参与的研究），反面模式。[证据](../../../sources/notes/ralph2020empirical.md#e71)
[^ralph2020empirical-e72]: SIGSOFT 伦理补充标准（有人参与的研究），可接受的偏离。[证据](../../../sources/notes/ralph2020empirical.md#e72)
[^ralph2020empirical-e73]: SIGSOFT 伦理补充标准（有人参与的研究），加分项。[证据](../../../sources/notes/ralph2020empirical.md#e73)
[^ralph2020empirical-e74]: SIGSOFT 伦理补充标准（有人参与的研究），不成立的批评。[证据](../../../sources/notes/ralph2020empirical.md#e74)
[^ralph2020empirical-e75]: SIGSOFT 伦理补充标准（有人参与的研究），Note。[证据](../../../sources/notes/ralph2020empirical.md#e75)
[^ralph2020empirical-e76]: SIGSOFT 开放科学补充标准，Principle。[证据](../../../sources/notes/ralph2020empirical.md#e76)
[^ralph2020empirical-e77]: SIGSOFT 开放科学补充标准，加分项。[证据](../../../sources/notes/ralph2020empirical.md#e77)
[^ralph2020empirical-e78]: SIGSOFT 开放科学补充标准，Notes。[证据](../../../sources/notes/ralph2020empirical.md#e78)
[^zeller2021devil-e7]: Zeller 2021，开头。[证据](../../../sources/notes/zeller2021devil.md#e7)
[^zeller2021devil-e1]: Zeller 2021，THE CHERRY SHUFFLE。[证据](../../../sources/notes/zeller2021devil.md#e1)
[^zeller2021devil-e2]: Zeller 2021，THE AUTOTUNE。[证据](../../../sources/notes/zeller2021devil.md#e2)
[^zeller2021devil-e3]: Zeller 2021，THE ACHILLES HEEL。[证据](../../../sources/notes/zeller2021devil.md#e3)
[^zeller2021devil-e8]: Zeller 2021，倒数第三段。[证据](../../../sources/notes/zeller2021devil.md#e8)
[^patterson2001bad-e8]: Patterson 2001，"5 Writing Commandments for a Bad Career"。[证据](../../../sources/notes/patterson2001bad.md#e8)
[^patterson2001bad-e9]: Patterson 2001，"5) Evaluating Quantitatively"。[证据](../../../sources/notes/patterson2001bad.md#e9)
[^sandve2013ten-e1]: Sandve 等人 2013，引言。[证据](../../../sources/notes/sandve2013ten.md#e1)
[^sandve2013ten-e2]: Sandve 等人 2013，Rule 1。[证据](../../../sources/notes/sandve2013ten.md#e2)
[^sandve2013ten-e4]: Sandve 等人 2013，Rule 4。[证据](../../../sources/notes/sandve2013ten.md#e4)
[^sandve2013ten-e11]: Sandve 等人 2013，Rule 6。[证据](../../../sources/notes/sandve2013ten.md#e11)
[^sandve2013ten-e6]: Sandve 等人 2013，Rule 10。[证据](../../../sources/notes/sandve2013ten.md#e6)
[^wilson2017good-e2]: Wilson 等人 2017，引言。[证据](../../../sources/notes/wilson2017good.md#e2)
[^wilson2017good-e3]: Wilson 等人 2017，Box 1。[证据](../../../sources/notes/wilson2017good.md#e3)
[^wilson2017good-e4]: Wilson 等人 2017，Box 1。[证据](../../../sources/notes/wilson2017good.md#e4)
[^bailey2012menlo-e1]: Bailey 等人 2012，第 71 页。[证据](../../../sources/notes/bailey2012menlo.md#e1)
[^bailey2012menlo-e2]: Bailey 等人 2012，第 72 页。[证据](../../../sources/notes/bailey2012menlo.md#e2)
[^bailey2012menlo-e3]: Bailey 等人 2012，第 72–73 页。[证据](../../../sources/notes/bailey2012menlo.md#e3)
[^bailey2012menlo-e4]: Bailey 等人 2012，第 72 页。[证据](../../../sources/notes/bailey2012menlo.md#e4)
[^bailey2012menlo-e5]: Bailey 等人 2012，第 73 页。[证据](../../../sources/notes/bailey2012menlo.md#e5)
[^bailey2012menlo-e6]: Bailey 等人 2012，第 73 页。[证据](../../../sources/notes/bailey2012menlo.md#e6)
[^bailey2012menlo-e7]: Bailey 等人 2012，第 74 页参考文献 3。[证据](../../../sources/notes/bailey2012menlo.md#e7)
[^carlini2022checklist-e1]: Carlini 2022，开头。[证据](../../../sources/notes/carlini2022checklist.md#e1)
[^carlini2022checklist-e2]: Carlini 2022，Secondary checklist for public releases。[证据](../../../sources/notes/carlini2022checklist.md#e2)
