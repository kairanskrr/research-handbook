# 心理学与认知科学：学科概况

本文讲心理学与认知科学的研究实际怎样运转：一场"可重复性危机"之后，这个领域在样本量、预注册、数据公开、测量和报告上形成了哪些新规矩。各学科共通的做法（选题、研究设计、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)，这里不重复；常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。本文的资料主要来自实验心理学和社会心理学，临床、发展、神经科学等方向有各自的规范，以目标期刊和所在机构的要求为准。文中的伦理准则和报告标准多出自美国心理学会，其他国家和机构有自己的规定。`[本项目分析]`

**读完本文，你应该能：**

- 说清心理学的"可重复性危机"是怎么回事，之后领域改了什么；
- 认出常见的可疑研究做法，知道预注册、注册报告、功效分析各自防的是什么；
- 知道做涉及人的心理学研究，伦理、测量、被试和报告上要守哪些规范；
- 知道心理学常用哪几种研究套路，每种靠什么证据、按什么标准评判；
- 避开新手最常犯的错误。

---

## 本领域研究怎样运转

### 一场可重复性危机改变了这个领域

**可重复性**指别人按同样的方法重做一项研究，能不能得到同样的结果。2015 年，开放科学合作组织（Open Science Collaboration）重做了 3 本心理学期刊上的 100 项实验和相关研究。重做时样本足够大，并尽量用原研究的材料。结果：重做得到的效应平均只有原研究的一半[^osc2015estimating-e1]；原研究 97% 结果显著，重做后只有 36% 显著[^osc2015estimating-e2]。

在这之前，2010–2012 年的几件事已经让实验心理学家意识到：他们收集、分析、报告数据的方式，让**假阳性**（其实没有效应，却得出"有效应"的结论）太容易发表[^nelson2018psychology-e1]。例如，社会心理学最有声望的期刊发表了 Bem 的 9 个实验，支持"人会受到无法预见的未来事件影响"这一明显荒谬的结论[^nelson2018psychology-e3]。

> **不同的看法：重做失败说明了什么？**
> - **说明很多结论靠不住**：重做后显著的比例从 97% 降到 36%，效应量减半[^osc2015estimating-e1][^osc2015estimating-e2]。
> - **不能简单算成"64% 失败"**：Nelson 等人用能区分"无定论"的方法重新判断，36% 明确成功，其余 64% 里只有 25% 明确失败，49% 无定论；无定论多，是因为很多重做本身样本也不够大[^nelson2018psychology-e13]。原项目也指出，重做没得到原结果，可能因为两次条件不同、原结果是假阳性，也可能是重做出了假阴性[^osc2015estimating-e3]。
>
> 原项目的分析还发现，能否重做成功，更多取决于原研究证据本身有多强[^osc2015estimating-e5]。对新手来说，两种看法指向同一个做法：**不要因为"发表过"就默认一个效应存在**，引用前看看它有没有被独立重复过、原研究的证据有多强。`[本项目分析]`

### 问题出在哪：p-hacking 和看到结果再提假设

**p-hacking** 指对同一份数据做多种分析，只报告结果"统计显著"的那一个，例如测了多个指标只报一个。"统计显著"大致是说，这个结果不太像是偶然出现的；心理学最常用的标准是 p 值小于 0.05 `[本项目分析]`。Nelson、Simmons 和 Simonsohn 在 2018 年的回顾里说，他们 2011 年的文章已经表明：这样做会大大提高发表假阳性的可能[^nelson2018psychology-e4]；在那篇文章的模拟中，即使只是当时被认为"可以接受"的 p-hacking，也能把假阳性率从 5% 提高到 61%[^nelson2018psychology-e7]。

具体是什么样子？作者描述：第一次分析不显著时，研究者会继续"看看"，例如去掉"异常值"再试、只看一部分参与者或试次、换一种方式计算结果指标[^nelson2018psychology-e6]。

这类做法很普遍。Nelson 等人引用的一项调查里，约 65% 的受访者承认报告研究时略去过某个结果指标[^nelson2018psychology-e5]。p-hacking 普遍，正是因为研究者通常意识不到自己在这样做，或者不觉得有什么后果[^nelson2018psychology-e8]。另一种问题是**看到结果再提假设**（hypothesizing after the results are known，HARKing），把事后解释写成事先预测[^nosek2018preregistration-e2]。为什么光靠诚实防不住，见第二部分的[分清：你是在检验，还是在探索](../../02_do-the-project/01_question-to-evidence.md#5-分清你是在检验还是在探索)和贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#2-对证据诚实不骗自己报告全部结果)。

这类做法常被统称为**可疑研究做法**（questionable research practices，QRP）`[本项目分析]`。Flake 和 Fried 指出，测量上也有类似问题，他们称为**可疑测量做法**（questionable measurement practices，QMP）：研究者在测量上做的、让人怀疑测量和结论是否成立的决定[^flake2020measurement-e1]。见下文[测量](#测量用有效度证据的量表)一节。

### 之后改了什么

Nelson 等人列出了这几年的变化：作者主动公开数据；顶级期刊经常发表重复研究，成功和失败的都发；数百位研究者做预注册；样本量大幅增加；部分顶级期刊要求完整披露测量、实验条件、剔除的数据和样本量的确定规则[^nelson2018psychology-e2]。下表是几项主要做法 `[本项目分析，依据下列资料]`：

| 做法 | 是什么 | 主要防什么 |
|---|---|---|
| 完整披露 | 报告全部测量指标、全部实验操纵、所有剔除的数据，以及样本量怎么定的[^nelson2018psychology-e10]；可以在论文里直接写一句标准声明[^nelson2018psychology-e11] | 选择性报告 |
| 预注册 | 在看到研究结果之前定好研究问题和分析计划[^nosek2018preregistration-e1]，是在分析任何数据之前写好、带时间戳的计划[^nelson2018psychology-e12] | 看到结果再定分析、再提假设 |
| 注册报告（Registered Reports） | 研究开始前，方案先经同行评审并被预先接收[^chambers2022past-e1] | 发表偏差：期刊和审稿人偏爱"阳性"结果 |
| 更大的样本与功效分析 | 事先算出需要多少人（见[下文](#统计功效和样本量)） | 统计功效不足[^nelson2018psychology-e9] |
| 公开数据和材料 | 例如开放科学框架（Open Science Framework，OSF），一个让研究者记录、共享、报告研究的在线平台[^nelson2018psychology-e15] | 别人无法核查和重做 |

**预注册要点。** 预注册是什么、不限制探索、偏离计划怎么办，第二部分的[要不要事先公开你的计划](../../02_do-the-project/01_question-to-evidence.md#6-要不要事先公开你的计划)已经讲过（资料多出自心理学），这里不重复。

**注册报告要点。** 分两个阶段审稿。第一阶段，作者在看到结果之前，把研究问题和方法交给期刊审[^nosek2018preregistration-e7]；通过后获得"原则性接收"：只要按批准的方案做、按证据解读结果，不管假设是否得到支持，期刊都会发表[^chambers2022past-e2]。第二阶段只看研究执行得好不好、是否按计划做，不评判结果是否"重要"[^nosek2018preregistration-e7]。开放科学中心（Center for Open Science，COS）的页面显示，目前有 300 多本期刊采用这种形式，有的作为常规投稿类型，有的只在某期专刊中使用[^cosregisteredreports-e1]。它的代价是：第一阶段审稿通常让研究推迟几个月才能开始[^chambers2022past-e6]；它特别适合检验假设的研究，不是为纯探索性研究设计的[^chambers2022past-e5]。

> **不同的看法：这些改革有多大效果？**
> - **有效的迹象**：Chambers 等人引用的一项心理学研究发现，普通论文只有 4% 没有证实第一个假设，注册报告是 56%[^chambers2022past-e3]。注册报告里，不支持假设的结果多得多。
> - **还不能下定论**：这个差异也可能因为作者用注册报告去检验更冒险的假设[^chambers2022past-e4]；预注册能提高可重复性，目前还缺少足够的实验证据[^nosek2018preregistration-e9]。预注册也不能杜绝糟糕的统计做法，只是让它们能被发现[^nosek2018preregistration-e8]。
>
> 实际操作：把预注册和完整披露当作基本功，但不要以为预注册了结论就一定可靠。`[本项目分析]`

### 发表文化：期刊、多研究论文与 APA 格式

心理学以期刊论文为主要发表形式，和计算机领域以会议为主不同 `[本项目分析]`。心理学写论文常用美国心理学会（American Psychological Association，APA）制定的"APA 格式"。它面向心理学、护理、商学等领域，专门针对投给期刊的稿件和学生课程论文[^apastyleabout-e2]，始于 1929 年[^apastyleabout-e1]。APA 格式不只管引用和排版：它要求作者报告研究方案的关键细节，让读者能评估结果、让别人能重做[^apastyleabout-e3]。

心理学论文常常一篇包含多个研究[^nelson2018psychology-e14]。开放科学合作组织选中的论文，平均每篇约有 3 项研究[^osc2015estimating-e6]。但多个研究不等于结论更可靠：只要愿意把少数不理想的研究放进抽屉不发表，一篇四个实验都"成功"的假阳性论文并不难做出来[^nelson2018psychology-e14]。

心理学也有大型合作项目。开放科学合作组织的 100 项重做由 270 位作者合作完成[^osc2015estimating-e4]；Nosek 从 2011 年起还组织过多个独立实验室合作重复已发表研究的项目[^nelson2018psychology-e15]。

**署名。** 美国心理学会的伦理准则要求署名反映各人的实际贡献，与职位高低无关；只担任系主任之类的职位不构成署名理由[^apa2017ethical-e8]。主要基于学生博士论文的多作者论文，除特殊情况外学生应为第一作者，导师要尽早和学生讨论署名[^apa2017ethical-e9]。通用做法见贯穿全程的[合作与导师](../../08_throughout/collaboration_and_advisors.md#6-署名开工时就谈并随进展调整)。

---

## 和计算机领域不同的地方

`[本项目分析，依据下列资料]`

| | 心理学与认知科学 | 计算机（见[计算机篇](../computer-science/README.md)） |
|---|---|---|
| 主要发表渠道 | 期刊，常用 APA 格式[^apastyleabout-e2] | 会议论文集 |
| 一篇论文 | 常包含多个研究[^nelson2018psychology-e14] | 常围绕一个新方法或系统的评估 |
| 研究对象 | 人的心理过程，抑郁、人格、态度这类概念往往无法直接观察[^flake2020measurement-e2] | 多为人造系统，可以直接运行和测量 |
| 报告标准 | 美国心理学会的期刊论文报告标准（JARS，见[下文](#报告标准美国心理学会的-jars)）[^apajars-e1] | 各会议的征稿启事、制品评估；软件工程有 SIGSOFT 实证标准 |
| 可重复性的重点 | 预注册、注册报告、样本量、完整披露[^nelson2018psychology-e2] | 代码、数据等制品能否运行和复现 |

---

## 本领域的规范和报告标准

### 伦理：美国心理学会伦理准则与机构审批

各学科共通的伦理原则见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)。美国心理学会（APA）的伦理准则约束其会员和学生会员[^apa2017ethical-e1]；不在美国、不是会员，也常被当作参考，但实际要以本国和本单位的规定为准 `[本项目分析]`。准则里和做研究关系最大、又是心理学特有的几条（知情同意、发表后共享数据、更正错误等通用要求见上面的链接）：

- **先审批，再开始。** 需要机构审批时，要如实提交方案、获批后才开始，并按批准的方案执行[^apa2017ethical-e2]。这里的机构审批，一般指所在单位伦理审查委员会的审批。美国叫"机构审查委员会"（Institutional Review Board，IRB），各国名称和要求不同 `[本项目分析]`。
- **学生被试要有替代选项。** 参加研究是课程要求或能换加分时，必须提供同等的替代活动[^apa2017ethical-e4]。
- **欺骗要有充分理由。** 欺骗指研究中不告诉参与者真实情况，例如隐瞒研究的真实目的 `[本项目分析]`。只有研究价值足够大、又没有可行的不欺骗方案时才可以这样做[^apa2017ethical-e5]；之后要尽早说明（最迟在数据收集结束时），并允许参与者撤回数据[^apa2017ethical-e6]。
- **事后说明（debriefing）。** 研究结束后及时告诉参与者研究的性质、结果和结论，纠正他们可能产生的误解[^apa2017ethical-e7]。

### 报告标准：美国心理学会的 JARS

美国心理学会的期刊论文报告标准（Journal Article Reporting Standards，JARS）规定论文里要写清哪些内容，是给作者、审稿人和编辑用的，目的是提高论文的严谨性[^apajars-e1]。按数据类型分三套：数值数据和统计分析用 JARS–Quant，文字、语言形式的数据用 JARS–Qual，两者结合用 JARS–Mixed[^apajars-e2]。另有一套 JARS–REC，适用于所有研究[^apajars-e3]，讲怎样讨论种族、民族和文化 `[本项目分析]`。

定量研究标准里，和上文改革直接相关的几条：

- 报告计划样本量、实际样本量，以及样本量怎么定的（功效分析等）、中途分析和停止规则[^appelbaum2018journal-e2]；
- 定义所有测量指标，**包括收集了但没在本文报告的**[^appelbaum2018journal-e3]；
- 报告收集数据后剔除参与者的标准[^appelbaum2018journal-e5]；
- 把假设、分析和结论分成主要的、次要的、探索性的[^appelbaum2018journal-e1]，并对所有假设逐一说明是否得到支持[^appelbaum2018journal-e6]；
- 做过注册的，给出注册信息[^appelbaum2018journal-e7]。

标准没有规定这些表格怎么用，可以做正式清单，也可以只当参考[^appelbaum2018journal-e8]，**以目标期刊的作者须知为准**。

### 统计功效和样本量

**统计功效**是"效应真的存在时，研究能检测出来"的概率。Nelson 等人指出一个老矛盾：绝大多数已发表研究功效不足，理论上不太可能得到显著结果[^nelson2018psychology-e9]；可开放科学合作组织抽查的 100 项原研究里，97% 结果显著[^osc2015estimating-e2]。他们认为 p-hacking 解释了这个矛盾[^nelson2018psychology-e9]。

- **事先算样本量。** 事先功效分析（a-priori power analysis）：给定想检测的效应量、显著性水平和想要的功效，算出需要多少观测[^lakens2022sample-e2]。关键是说清为什么选这个效应量[^lakens2022sample-e3]。
- **别用小预实验或已发表的效应量直接算。** 小样本预实验估出的效应量很不精确[^lakens2022sample-e4]；已发表的效应量又会因发表偏差被高估[^lakens2022sample-e5]。
- **样本量的理由不止功效分析一种。** Lakens 列了六种：收集（几乎）整个总体、按资源限制、功效分析、按估计精度、按经验规则、明确承认没有理由[^lakens2022sample-e1]。资源总是有限的，要认真评估[^lakens2022sample-e7]。"功效 80%"只是惯例，本身没有坚实的理由[^lakens2022sample-e6]。
- **别信"每组 20 个就够"。** Simmons 等人 2011 年的文章曾建议每个实验条件至少 20 个观测。同一批作者在 2018 年的回顾里说，这个门槛低得可笑：在有代表性的样本里，每组 20 个连"男性比女性重"都检测不出来[^simmons2018false-e1]。
- **投注册报告要准备更大的样本。** 很多期刊对注册报告有最低功效要求，所需样本往往很大[^chambers2022past-e7]，例如 90% 的功效[^chambers2022past-e8]。

### 测量：用有效度证据的量表

心理学测的多是抑郁、人格特质、态度这类概念（称为**构念**，construct），它们往往无法直接观察。测量本身测不准，再严谨的设计、再高级的统计、再大的样本也救不回来[^flake2020measurement-e2]。

- **信度**指测量稳不稳定，**效度**指测到的是不是你想测的东西。美国心理学会伦理准则要求使用在被测人群中已经确立了效度和信度的工具[^apa2017ethical-e11]；JARS 要求说明量表是已验证的还是为本研究临时编的，并尽可能报告本研究样本上的信度[^appelbaum2018journal-e4]。
- **照原样用已有量表，注明出处**，能减少可操作的灵活空间[^flake2020measurement-e4]。改动量表，要说明怎么改、为什么改[^flake2020measurement-e6]。
- **警惕"临时编量表"。** Flake 和 Fried 引用的一项检查发现：被检查的 43 个量表中，34 个（79%）像是临时编的，原研究里没有其他效度证据[^flake2020measurement-e5]。一份 10 道题的问卷，光挑哪些题加总就有 1023 种算法[^flake2020measurement-e3]，这给挑选想要的结果留下了很大空间 `[本项目分析]`。

### 被试：学生样本和 WEIRD 样本

Henrich 等人指出，行为科学家常常只用来自"西方、受过教育、工业化、富裕、民主"（Western, Educated, Industrialized, Rich, Democratic，缩写 WEIRD）社会的样本，就在顶级期刊上对人类心理下宽泛的结论[^henrich2010weirdest-e1]。他们引用 Arnett 2008 年的分析：心理学样本中 96% 来自西方工业化国家，而这些国家只占世界人口的 12%[^henrich2010weirdest-e3]；其中 67% 的美国样本完全由上心理学课的本科生组成[^henrich2010weirdest-e4]。问题在于，WEIRD 被试和全人类相比恰恰很特殊，常常是离群的一端[^henrich2010weirdest-e2]。连视知觉都会因人群而异：一种经典视错觉，美国本科生处在分布的极端，卡拉哈里的桑人采集者则完全不受影响[^henrich2010weirdest-e6]。

做法：详细报告被试来源和构成[^henrich2010weirdest-e8]；结论能推广到多大范围，要和证据强度相称[^henrich2010weirdest-e7]。抽样的一般原则见第二部分的[说清为什么选这些样本](../../02_do-the-project/01_question-to-evidence.md#3-定下研究对象分析单元和总体)。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表列出心理学（以实验和社会心理学为主）常用的三种。表的分组和"在心理学里的样子"一栏是本项目的归纳；每条标准只代表脚注里那份资料 `[本项目分析]`。

| 套路 | 在心理学里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [解释因果](../../05_research-strategies/explain_causality.md) | 用实验检验关于心理过程的假设 | 在看到结果之前定好研究问题和分析计划[^nosek2018preregistration-e1]；事先功效分析要能说清为什么选这个效应量[^lakens2022sample-e3]；完整披露测量、实验操纵、剔除的数据和样本量规则[^nelson2018psychology-e10]；按 JARS 报告样本量怎么定、剔除标准[^appelbaum2018journal-e2][^appelbaum2018journal-e5] | [对照实验](../../06_methods/controlled_experiment.md) |
| [测量](../../05_research-strategies/measure.md) | 给抑郁、人格、态度这类无法直接观察的构念找到可靠的测法[^flake2020measurement-e2] | 用在被测人群中已确立效度和信度的工具[^apa2017ethical-e11]；照原样用已有量表并注明出处[^flake2020measurement-e4]；报告量表是否验证过、本样本上的信度[^appelbaum2018journal-e4] | [量表编制与测量研究](../../06_methods/scale_development.md) |
| [综合](../../05_research-strategies/synthesize.md) | 用元分析合并已发表研究的效应 | 已发表的效应量会因发表偏差被高估[^lakens2022sample-e5]，合并前要考虑这一点 `[本项目分析]` | [系统综述与元分析](../../06_methods/meta_analysis.md)、[综述研究](../../06_methods/review_study.md) |

怎么用这张表 `[本项目分析]`：不管走哪种套路，心理学审稿人都会看样本量的理由和是否完整披露；测量是实验的前提，实验结论再漂亮，测不准也救不回来[^flake2020measurement-e2]。

## 本学科常用的研究方法

心理学用的方法多和研究类型里涉及人的那几种相通，先读对应文档，再注意下表的差异 `[本项目分析]`：

| 研究做法 | 研究类型 | 心理学里要多注意什么 |
|---|---|---|
| 实验（含被试间、被试内设计） | [对照实验](../../06_methods/controlled_experiment.md) | 那篇讲的是比较工具或方法对人的影响；心理学实验研究的是心理过程本身。用欺骗要有充分理由，并按准则做事后说明[^apa2017ethical-e5][^apa2017ethical-e7] |
| 问卷与量表研究 | [问卷调查](../../06_methods/questionnaire_survey.md)、[量表编制与测量研究](../../06_methods/scale_development.md) | 测心理构念时，见上文[测量](#测量用有效度证据的量表) |
| 访谈与其他定性研究 | [访谈研究](../../06_methods/interview_study.md) | 报告时对照 JARS–Qual[^apajars-e2] |
| 重复研究、纵向研究 | [复现研究](../../06_methods/replication.md)、[纵向研究](../../06_methods/longitudinal_study.md) | 顶级期刊已在经常发表重复研究[^nelson2018psychology-e2]；JARS–Quant 有重复研究和纵向研究的专门模块[^appelbaum2018journal-e9] |

---

## 给新手的建议

1. **默认做预注册。** 在看到结果之前写下研究问题和分析计划[^nosek2018preregistration-e1]；偏离了就如实报告[^nosek2018preregistration-e5]。
2. **样本量要有理由。** 动手前做功效分析或说明其他理由，不要凭"别人也用这么多人"[^lakens2022sample-e1]。
3. **在论文里写上完整披露声明**：样本量怎么定的、剔除了哪些数据、所有实验操纵和所有测量[^nelson2018psychology-e11]。
4. **用已有的、有效度证据的量表，照原样用、注明出处**[^flake2020measurement-e4]。
5. **引用一个效应之前，查查它有没有被重复过。** 发表过不等于可靠[^osc2015estimating-e1] `[本项目分析]`。
6. **主要靠学生被试时，别把结论说成"人类如何"**[^henrich2010weirdest-e7]。
7. **有一个想检验的明确假设，又不急于马上收数据，可以考虑注册报告。** 第一阶段审稿会让研究推迟几个月[^chambers2022past-e6]。先读目标期刊的作者指南，再填方案模板[^cosregisteredreports-e2]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 结果不显著就换指标、去掉"异常值"、只看部分被试，直到显著 | 这就是 p-hacking，会大大提高假阳性率[^nelson2018psychology-e6][^nelson2018psychology-e7] |
| 看到结果后把假设改成"预测到了" | 把事后解释当成事先预测（HARKing）[^nosek2018preregistration-e2] |
| 只报告结果好的指标，没提收集了但没用的指标 | JARS 要求报告所有测量，包括没用上的[^appelbaum2018journal-e3] |
| 预注册了，但没报告计划内的全部分析 | 仍然是选择性报告[^nosek2018preregistration-e6] |
| 用小预实验估的效应量算样本量 | 估计很不精确[^lakens2022sample-e4] |
| 自己临时编几道题当量表，不报告信度效度 | 无法判断测到的是什么[^flake2020measurement-e5][^appelbaum2018journal-e4] |
| 用本科生样本，结论写成"人们……" | WEIRD 被试常常是离群的一端[^henrich2010weirdest-e2]；连 Nature、Science 这样的顶级期刊上也常见这种推广[^henrich2010weirdest-e5] |
| 学生被试只能靠参加实验拿课程分 | 必须提供同等的替代活动[^apa2017ethical-e4] |
| 论文里统计结果抄错、算错 | Nelson 等人引用的一项检查发现，54% 的论文至少有一处错误，12% 至少有一处错误改变了结果是否显著[^nelson2018psychology-e16] |
| 把导师或系主任放在第一作者，而不是实际做事的学生 | 署名要反映实际贡献，与职位无关[^apa2017ethical-e8] |

---

## 延伸阅读

推荐理由为本项目分析。

- **Nelson, Simmons & Simonsohn 2018，Psychology's Renaissance**：可重复性危机的来龙去脉和改革措施。想弄清 p-hacking 和预注册的，先读这篇。
- **Open Science Collaboration 2015**：100 项重做的原始报告，看大型重复项目是怎么设计和执行的。
- **Nosek et al. 2018，The preregistration revolution**：预注册是什么，偏离计划等实际难题怎么处理。
- **Chambers & Tzavella 2022**：注册报告的历史、证据和局限，附给作者的建议。
- **Lakens 2022，Sample Size Justification**：说明样本量的六种理由，以及功效分析怎么做。
- **Flake & Fried 2020**：可疑测量做法，附一份透明报告测量的问题清单。
- **Henrich, Heine & Norenzayan 2010**：WEIRD 样本问题的经典文章。
- **美国心理学会伦理准则第 8 节和 JARS**：做研究和写论文前对照着读。

[^osc2015estimating-e1]: Open Science Collaboration 2015，摘要。[证据](../../../sources/notes/osc2015estimating.md#e1)
[^osc2015estimating-e2]: Open Science Collaboration 2015，摘要。[证据](../../../sources/notes/osc2015estimating.md#e2)
[^osc2015estimating-e3]: Open Science Collaboration 2015，引言。[证据](../../../sources/notes/osc2015estimating.md#e3)
[^osc2015estimating-e4]: Open Science Collaboration 2015，Method。[证据](../../../sources/notes/osc2015estimating.md#e4)
[^osc2015estimating-e5]: Open Science Collaboration 2015，摘要。[证据](../../../sources/notes/osc2015estimating.md#e5)
[^osc2015estimating-e6]: Open Science Collaboration 2015，Sampling frame and study selection。[证据](../../../sources/notes/osc2015estimating.md#e6)
[^nelson2018psychology-e1]: Nelson、Simmons、Simonsohn 2018，摘要。[证据](../../../sources/notes/nelson2018psychology.md#e1)
[^nelson2018psychology-e2]: Nelson 等人 2018，Introduction。[证据](../../../sources/notes/nelson2018psychology.md#e2)
[^nelson2018psychology-e3]: Nelson 等人 2018，The Renaissance Begins。[证据](../../../sources/notes/nelson2018psychology.md#e3)
[^nelson2018psychology-e4]: Nelson 等人 2018，The Renaissance Begins。[证据](../../../sources/notes/nelson2018psychology.md#e4)
[^nelson2018psychology-e5]: Nelson 等人 2018，The Renaissance Begins。[证据](../../../sources/notes/nelson2018psychology.md#e5)
[^nelson2018psychology-e6]: Nelson 等人 2018，P-Hacking Explains an Old Paradox。[证据](../../../sources/notes/nelson2018psychology.md#e6)
[^nelson2018psychology-e7]: Nelson 等人 2018，P-Hacking Explains an Old Paradox。[证据](../../../sources/notes/nelson2018psychology.md#e7)
[^nelson2018psychology-e8]: Nelson 等人 2018，False Positives Are Bad。[证据](../../../sources/notes/nelson2018psychology.md#e8)
[^nelson2018psychology-e9]: Nelson 等人 2018，P-Hacking Explains an Old Paradox。[证据](../../../sources/notes/nelson2018psychology.md#e9)
[^nelson2018psychology-e10]: Nelson 等人 2018，Disclosure。[证据](../../../sources/notes/nelson2018psychology.md#e10)
[^nelson2018psychology-e11]: Nelson 等人 2018，脚注 11。[证据](../../../sources/notes/nelson2018psychology.md#e11)
[^nelson2018psychology-e12]: Nelson 等人 2018，Preregistration。[证据](../../../sources/notes/nelson2018psychology.md#e12)
[^nelson2018psychology-e13]: Nelson 等人 2018，Replications。[证据](../../../sources/notes/nelson2018psychology.md#e13)
[^nelson2018psychology-e14]: Nelson 等人 2018，P-Hacking Explains an Old Paradox。[证据](../../../sources/notes/nelson2018psychology.md#e14)
[^nelson2018psychology-e15]: Nelson 等人 2018，The Renaissance Begins。[证据](../../../sources/notes/nelson2018psychology.md#e15)
[^nelson2018psychology-e16]: Nelson 等人 2018，Unintentional Errors。[证据](../../../sources/notes/nelson2018psychology.md#e16)
[^simmons2018false-e1]: Simmons、Nelson、Simonsohn 2018，第 256 页。[证据](../../../sources/notes/simmons2018false.md#e1)
[^nosek2018preregistration-e1]: Nosek 等人 2018，Abstract。[证据](../../../sources/notes/nosek2018preregistration.md#e1)
[^nosek2018preregistration-e2]: Nosek 等人 2018，Mental Constraints on Distinguishing Predictions and Postdictions。[证据](../../../sources/notes/nosek2018preregistration.md#e2)
[^nosek2018preregistration-e5]: Nosek 等人 2018，Challenge 1。[证据](../../../sources/notes/nosek2018preregistration.md#e5)
[^nosek2018preregistration-e6]: Nosek 等人 2018，Challenge 6。[证据](../../../sources/notes/nosek2018preregistration.md#e6)
[^nosek2018preregistration-e7]: Nosek 等人 2018，Advancing the Motive for Preregistration。[证据](../../../sources/notes/nosek2018preregistration.md#e7)
[^nosek2018preregistration-e8]: Nosek 等人 2018，Challenge 2。[证据](../../../sources/notes/nosek2018preregistration.md#e8)
[^nosek2018preregistration-e9]: Nosek 等人 2018，Preregistration Distinguishes Prediction and Postdiction。[证据](../../../sources/notes/nosek2018preregistration.md#e9)
[^chambers2022past-e1]: Chambers & Tzavella 2022，摘要。[证据](../../../sources/notes/chambers2022past.md#e1)
[^chambers2022past-e2]: Chambers & Tzavella 2022，引言，作者接受稿约第 3 页。[证据](../../../sources/notes/chambers2022past.md#e2)
[^chambers2022past-e3]: Chambers & Tzavella 2022，Bias control，作者接受稿约第 7 页。[证据](../../../sources/notes/chambers2022past.md#e3)
[^chambers2022past-e4]: Chambers & Tzavella 2022，Bias control，作者接受稿约第 7 页。[证据](../../../sources/notes/chambers2022past.md#e4)
[^chambers2022past-e5]: Chambers & Tzavella 2022，Limitations and drawbacks，作者接受稿约第 12 页。[证据](../../../sources/notes/chambers2022past.md#e5)
[^chambers2022past-e6]: Chambers & Tzavella 2022，Stage 1 delay，作者接受稿约第 13 页。[证据](../../../sources/notes/chambers2022past.md#e6)
[^chambers2022past-e7]: Chambers & Tzavella 2022，Present，作者接受稿约第 6 页。[证据](../../../sources/notes/chambers2022past.md#e7)
[^chambers2022past-e8]: Chambers & Tzavella 2022，Box 1，作者接受稿约第 13 页。[证据](../../../sources/notes/chambers2022past.md#e8)
[^cosregisteredreports-e1]: 开放科学中心，Registered Reports 页面，Participating Journals。[证据](../../../sources/notes/cosregisteredreports.md#e1)
[^cosregisteredreports-e2]: 开放科学中心，Registered Reports 页面，Participating Journals。[证据](../../../sources/notes/cosregisteredreports.md#e2)
[^henrich2010weirdest-e1]: Henrich、Heine、Norenzayan 2010，Long Abstract。[证据](../../../sources/notes/henrich2010weirdest.md#e1)
[^henrich2010weirdest-e2]: Henrich 等人 2010，Long Abstract。[证据](../../../sources/notes/henrich2010weirdest.md#e2)
[^henrich2010weirdest-e3]: Henrich 等人 2010，§1.1（引 Arnett 2008）。[证据](../../../sources/notes/henrich2010weirdest.md#e3)
[^henrich2010weirdest-e4]: Henrich 等人 2010，§1.1（引 Arnett 2008）。[证据](../../../sources/notes/henrich2010weirdest.md#e4)
[^henrich2010weirdest-e5]: Henrich 等人 2010，§1.2。[证据](../../../sources/notes/henrich2010weirdest.md#e5)
[^henrich2010weirdest-e6]: Henrich 等人 2010，§2.1。[证据](../../../sources/notes/henrich2010weirdest.md#e6)
[^henrich2010weirdest-e7]: Henrich 等人 2010，§6.3。[证据](../../../sources/notes/henrich2010weirdest.md#e7)
[^henrich2010weirdest-e8]: Henrich 等人 2010，§6.3。[证据](../../../sources/notes/henrich2010weirdest.md#e8)
[^apa2017ethical-e1]: 美国心理学会伦理准则，Introduction and Applicability。[证据](../../../sources/notes/apa2017ethical.md#e1)
[^apa2017ethical-e2]: 美国心理学会伦理准则，8.01。[证据](../../../sources/notes/apa2017ethical.md#e2)
[^apa2017ethical-e4]: 美国心理学会伦理准则，8.04(b)。[证据](../../../sources/notes/apa2017ethical.md#e4)
[^apa2017ethical-e5]: 美国心理学会伦理准则，8.07(a)。[证据](../../../sources/notes/apa2017ethical.md#e5)
[^apa2017ethical-e6]: 美国心理学会伦理准则，8.07(c)。[证据](../../../sources/notes/apa2017ethical.md#e6)
[^apa2017ethical-e7]: 美国心理学会伦理准则，8.08(a)。[证据](../../../sources/notes/apa2017ethical.md#e7)
[^apa2017ethical-e8]: 美国心理学会伦理准则，8.12(b)。[证据](../../../sources/notes/apa2017ethical.md#e8)
[^apa2017ethical-e9]: 美国心理学会伦理准则，8.12(c)。[证据](../../../sources/notes/apa2017ethical.md#e9)
[^apa2017ethical-e11]: 美国心理学会伦理准则，9.02(b)。[证据](../../../sources/notes/apa2017ethical.md#e11)
[^apajars-e1]: 美国心理学会 APA Style 网站 JARS 页面，What are APA Style JARS?。[证据](../../../sources/notes/apajars.md#e1)
[^apajars-e2]: 美国心理学会 APA Style 网站 JARS 页面，Guidelines。[证据](../../../sources/notes/apajars.md#e2)
[^apajars-e3]: 美国心理学会 APA Style 网站 JARS 页面，What are APA Style JARS?。[证据](../../../sources/notes/apajars.md#e3)
[^apastyleabout-e1]: 美国心理学会 APA Style 网站，About APA Style。[证据](../../../sources/notes/apastyleabout.md#e1)
[^apastyleabout-e2]: 美国心理学会 APA Style 网站，About APA Style。[证据](../../../sources/notes/apastyleabout.md#e2)
[^apastyleabout-e3]: 美国心理学会 APA Style 网站，About APA Style。[证据](../../../sources/notes/apastyleabout.md#e3)
[^appelbaum2018journal-e1]: Appelbaum 等人 2018（JARS–Quant），摘要。[证据](../../../sources/notes/appelbaum2018journal.md#e1)
[^appelbaum2018journal-e2]: Appelbaum 等人 2018，Table 1，Method。[证据](../../../sources/notes/appelbaum2018journal.md#e2)
[^appelbaum2018journal-e3]: Appelbaum 等人 2018，Table 1，Method。[证据](../../../sources/notes/appelbaum2018journal.md#e3)
[^appelbaum2018journal-e4]: Appelbaum 等人 2018，Table 1，Psychometrics。[证据](../../../sources/notes/appelbaum2018journal.md#e4)
[^appelbaum2018journal-e5]: Appelbaum 等人 2018，Table 1，Data diagnostics。[证据](../../../sources/notes/appelbaum2018journal.md#e5)
[^appelbaum2018journal-e6]: Appelbaum 等人 2018，Table 1，Discussion。[证据](../../../sources/notes/appelbaum2018journal.md#e6)
[^appelbaum2018journal-e7]: Appelbaum 等人 2018，Table 1，Title page and author note。[证据](../../../sources/notes/appelbaum2018journal.md#e7)
[^appelbaum2018journal-e8]: Appelbaum 等人 2018，结语。[证据](../../../sources/notes/appelbaum2018journal.md#e8)
[^appelbaum2018journal-e9]: Appelbaum 等人 2018，摘要。[证据](../../../sources/notes/appelbaum2018journal.md#e9)
[^lakens2022sample-e1]: Lakens 2022，摘要。[证据](../../../sources/notes/lakens2022sample.md#e1)
[^lakens2022sample-e2]: Lakens 2022，A-priori Power Analysis。[证据](../../../sources/notes/lakens2022sample.md#e2)
[^lakens2022sample-e3]: Lakens 2022，A-priori Power Analysis。[证据](../../../sources/notes/lakens2022sample.md#e3)
[^lakens2022sample-e4]: Lakens 2022，What is the Expected Effect Size?（引 Leon 等人 2011）。[证据](../../../sources/notes/lakens2022sample.md#e4)
[^lakens2022sample-e5]: Lakens 2022，What is the Expected Effect Size?。[证据](../../../sources/notes/lakens2022sample.md#e5)
[^lakens2022sample-e6]: Lakens 2022，A-priori Power Analysis。[证据](../../../sources/notes/lakens2022sample.md#e6)
[^lakens2022sample-e7]: Lakens 2022，Resource Constraints。[证据](../../../sources/notes/lakens2022sample.md#e7)
[^flake2020measurement-e1]: Flake & Fried 2020，摘要。[证据](../../../sources/notes/flake2020measurement.md#e1)
[^flake2020measurement-e2]: Flake & Fried 2020，引言。[证据](../../../sources/notes/flake2020measurement.md#e2)
[^flake2020measurement-e3]: Flake & Fried 2020，Questioning the Validity of Psychological Science。[证据](../../../sources/notes/flake2020measurement.md#e3)
[^flake2020measurement-e4]: Flake & Fried 2020，问题 6。[证据](../../../sources/notes/flake2020measurement.md#e4)
[^flake2020measurement-e5]: Flake & Fried 2020，问题 6（引 Shaw 等人）。[证据](../../../sources/notes/flake2020measurement.md#e5)
[^flake2020measurement-e6]: Flake & Fried 2020，Table 1。[证据](../../../sources/notes/flake2020measurement.md#e6)
