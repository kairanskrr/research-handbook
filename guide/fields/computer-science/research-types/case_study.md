# 案例研究与民族志：在真实环境里深入研究少数对象

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**案例研究**（case study）和**民族志**（ethnography）：走进一家公司、一个团队或一个开源社区，用访谈、观察、文档等多种证据，深入弄清某件事在那里是怎样发生的、为什么会这样。例如在一家公司里跟踪一个团队几周，看他们怎样做代码评审。

如果你要从大量代码仓库里批量抽数据做统计，见[仓库挖掘研究](repository_mining.md)；如果你提出了一个新工具，想"拿一个例子演示一下"，那属于[工程研究](engineering_research.md)的评估环节，不是本文说的案例研究。

**读完本文，你应该能：**

- 分清什么是案例研究、什么只是借用了这个名字；
- 按步骤设计并完成一项案例研究：定案例和分析单元、进入组织、写方案、收数据、分析、报告；
- 说清民族志和一般案例研究的不同；
- 应对"只有一个案例，没法推广"这类质疑。

---

## 1. 这是什么研究，什么时候用

**定义。** 案例研究是在真实环境中深入考察一个当下现象（"案例"）的实证研究，尤其适用于现象和环境的边界不清楚的情况[^ralph2020empirical-e414]。研究的"现场"可以是社区、组织、团队、个人、流程或互联网平台[^ralph2020empirical-e415]。它的结论不靠统计显著性，而是把数字、访谈中的陈述、文档等多种证据连起来支撑[^runeson2009guidelines-e23]。本文的依据大多来自软件工程。在计算机的其他方向，人机交互（HCI）和计算机支持的协同工作（CSCW）社区也用民族志研究工作场所、指导应用设计[^sharp2016role-e1]。

**它不是什么。** "案例研究"这个词被用得很滥。下面几种都不算：

- **演示用的例子。** 软件工程文献里，"案例研究"常被用来指一个演示用的例子，这和作为实证方法的案例研究完全是两回事[^easterbrook2008selecting-e10]。在玩具程序上做的研究没有真实环境，不算案例研究[^runeson2009guidelines-e28]；ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准要求现场必须真实存在，不能是玩具例子或虚构情境[^ralph2020empirical-e419]。
- **经验报告。** 写"我们团队用了某方法，体会如下"是经验报告；在许多现场各做一点浅层调查也不是案例研究[^ralph2020empirical-e416]。
- **只访谈了几个人。** 访谈了不止一个人，并不因此就成了案例研究[^wohlin2021case-e6]。

这种误用很普遍。Wohlin 检查了一批自称"案例研究"的软件工程期刊论文，接近一半按定义不算[^wohlin2021case-e1]。典型情况是小规模的评估或演示（例如在实验室里），以及对开源仓库、缺陷库等已有信息的分析[^wohlin2021case-e3]。所以**论文里要注明你采用的是哪个定义**[^wohlin2021case-e7]。

**和相近类型的区别** `[本项目分析，依据下列资料]`：

| | 案例研究 | 实验 | 调查 | 行动研究 |
|---|---|---|---|---|
| 研究者的角色 | 只观察，不主动改变现场[^runeson2009guidelines-e20] | 操纵变量 | 收集标准化信息 | 参与并推动变化[^runeson2009guidelines-e20] |
| 怎么选对象 | 有目的地挑选[^runeson2009guidelines-e29] | 随机分配 | 从总体中抽样 | 有改进需求的组织 |
| 典型问题 | "这里是怎样、为什么会这样？"[^easterbrook2008selecting-e12] | "A 是否导致 B？" | "有多普遍？" | "这样改有没有用？" |
| 长处和代价 | 真实性高，控制程度低[^runeson2009guidelines-e22] | 控制程度高，真实性低 | 代表性好，深度有限 | 能带来改变，难保持客观 |

**什么时候用：**

- 问题是"如何"或"为什么"[^easterbrook2008selecting-e12]，而且环境本身会影响现象（例如真实项目的压力会改变开发者的行为），或者影响要很久才显现[^easterbrook2008selecting-e16]。
- 想知道实际发生了什么，而不是人们说自己做了什么。怀疑"官方说法"和实际情况有出入时，特别适合用观察[^runeson2009guidelines-e48]。
- 愿意用"代表性"去换"深度"[^easterbrook2008selecting-e19]。要回答"多普遍"，用调查或仓库挖掘；要回答"是否导致"，用实验。`[本项目分析]`

> **不同的看法：只分析历史数据，算不算案例研究？**
>
> - **算，叫历史型案例研究**：SIGSOFT 标准列出的案例研究类型里，有一种"历史型"，它使用档案数据，例如软件仓库[^ralph2020empirical-e431]。
> - **不算**：Wohlin 认为只研究历史信息（已有的数据或软件）不符合案例研究的定义[^wohlin2021case-e2]，这类研究应叫"档案分析"[^wohlin2021case-e3]。他还认为研究者参与到案例中时应叫行动研究（见[行动研究](action_research.md)）[^wohlin2021case-e4]。
>
> 实际操作：只分析几个项目的仓库数据时，不要只写"案例研究"四个字，要写清用的是哪个定义、数据从哪来[^wohlin2021case-e7]。如果能补上访谈或观察，同时也更符合多来源三角验证的要求。`[本项目分析]`

---

## 2. 怎么做

案例研究的设计是灵活的：可以边收数据边调整。但**目标要从一开始定下**；目标变了，就是一项新的研究[^runeson2009guidelines-e25]。灵活不等于不用计划。

### 第一步：写清目标和研究问题

先写一个"如何/为什么"的研究问题，再由它推出研究命题（你希望这项研究说明什么），用命题来指导选案例、收数据[^easterbrook2008selecting-e12]。计划至少要包括：目标、案例、理论（参照框架）、研究问题、数据收集方法、选择策略[^runeson2009guidelines-e27]。**容易错在哪**：只有一个模糊的兴趣（"想看看这家公司怎么做测试"），没有问题。结果什么都记，什么都说明不了。`[本项目分析]`

### 第二步：定义案例和分析单元

**案例**是研究对象，例如一个项目；它包含一个或多个**分析单元**，例如子项目[^runeson2009guidelines-e26]。分析单元可以是公司、项目、团队、单个开发者、某次事件、某个工作产物[^easterbrook2008selecting-e15]。把案例当作一个整体来研究，叫整体式；在一个案例中研究多个分析单元，叫嵌入式[^runeson2009guidelines-e28]。**为什么重要**：分析单元决定研究聚焦在什么现象上[^easterbrook2008selecting-e15]。以"开发者"为单元，看到的是个人习惯；以"团队"为单元，看到的是团队共享的做法。

### 第三步：有目的地选案例，并说清为什么

案例要有意识地挑选，而不是像调查和实验那样从总体中抽样[^runeson2009guidelines-e29]。常见的选法有[^runeson2009guidelines-e30][^easterbrook2008selecting-e13]：**典型案例**，了解常见情况；**关键案例**，检验一个成熟的理论，理论在这里成立，很可能在许多别处也成立；**独特案例**，在某方面与众不同；**揭示性案例**，研究以前未知或没人研究过的现象[^ralph2020empirical-e431]。一个案例有时就够了，但多案例设计通常效度更高。几个案例应当看作**重复验证**，而不是样本中的成员[^easterbrook2008selecting-e14]。

**容易错在哪**：实际上很多案例是因为"正好联系得上"才选的[^runeson2009guidelines-e30]。这不可耻，但要如实写出，并论证这个案例为什么仍然适合回答你的问题。论证选择理由是 SIGSOFT 标准的必要项[^ralph2020empirical-e419]。

### 第四步：进入组织，事先谈好保密和发表

和企业合作的案例研究，难点可能不在方法，而在**能不能进去、能不能发表**。

- **留出时间建立关系。** 对方可能要和你建立关系一段时间后，才肯提供具体的项目数据[^easterbrook2008selecting-e25]。换取进入的机会，研究者通常要放弃一部分控制[^easterbrook2008selecting-e26]。
- **一开始就写进合同**：哪些信息保密、谁来批准发表什么[^runeson2009guidelines-e34][^runeson2009guidelines-e36]。企业可能不了解学术发表的惯例，要明确告诉它们[^runeson2009guidelines-e37]。不说清楚，发表可能被推迟[^easterbrook2008selecting-e26]。谈判可以有中间方案：Runeson & Höst 的例子中，企业不允许公布缺陷的原始数量，但允许公布各阶段的百分比，这对研究目的已经够用[^runeson2009guidelines-e42]。
- **事先讨论"坏结果"。** 结果可能暴露企业实践中的缺陷，这种可能要事先说清楚[^runeson2009guidelines-e39]。
- **保护员工，不只是保护公司。** 员工的意见如果被转给其上级，也可能伤害他们[^runeson2009guidelines-e36]。由管理层安排员工参与时，管理层就是"把关人"：他们控制你能接触谁，还可能决定谁的声音被听到[^ralph2020empirical-e438]。怎样减轻这种权力关系，见[访谈研究](interview_study.md#第三步做访谈)中"留意权力关系"。

知情同意、伦理审查、隐私保护的一般要求见通用篇[科研诚信与伦理](../../../general/4_throughout/02_integrity_and_ethics.md#4-研究涉及人时先保护人)；SIGSOFT 的伦理补充标准明确适用于案例研究[^ralph2020empirical-e439]。用间接方式收数据（例如自动记录工具的使用情况）时，同样不能跳过征得同意[^runeson2009guidelines-e35]。

### 第五步：写案例研究方案

**案例研究方案**（case study protocol）记录设计决策和现场操作程序，是一份随计划变化不断更新的文档[^runeson2009guidelines-e31]。**为什么要写**：它指导数据收集，防止漏收计划中的数据；可以请同行审阅、提意见；它还是研究日志，记录每次调整及其理由，最后写报告时用得上。方案要做版本管理[^runeson2009guidelines-e32]。方案含保密信息，一般不能全文公开，但访谈提纲等部分可以公开[^runeson2009guidelines-e33]。事先公开发布方案，是 SIGSOFT 标准的优秀项[^ralph2020empirical-e428]。

### 第六步：从多个来源收集数据，相互印证

**最重要的一条：不要只靠一种数据。** 只做访谈、不做印证，是 SIGSOFT 标准列出的反面模式[^ralph2020empirical-e432]。原因是受访者倾向于说访谈者想听的话，给出合理化的说法，记忆也有选择性[^sharp2016role-e2]。多个来源得出同一结论，结论才更强，这叫**三角验证**（triangulation）[^runeson2009guidelines-e43]。可以在几个层面做[^runeson2009guidelines-e44]：**数据来源**（访谈之外，再看会议、文档、缺陷记录、代码评审记录）、**观察者**（两个以上研究者）、**理论**（用不同的理论视角解读）。

常用的数据来源：

- **访谈**：案例研究中常用半结构化访谈[^runeson2009guidelines-e46]。怎样选人、设计提纲、判断饱和，见[访谈研究](interview_study.md)。
- **观察**：直接观察是只看不参与，参与式观察是加入参与者正在做的事[^ralph2020empirical-e424]。用观察或档案记录核对受访者的说法，是 SIGSOFT 标准的加分项[^ralph2020empirical-e423]。
- **已有的工作产物**：文档、缺陷报告、工时记录等。它们原本是为别的目的记录的，质量和完整性未必满足研究需要[^runeson2009guidelines-e45]。

### 第七步：分析时保持证据链

**证据链**（chain of evidence）指读者能从你收集的数据一路追到结论[^runeson2009guidelines-e50]。这是 SIGSOFT 标准的必要项[^ralph2020empirical-e421]。怎么做：

- **边收边分析。** 分析中会有新发现，需要补收数据、更新访谈提纲[^runeson2009guidelines-e15]。
- **编码**：给文本片段打上代表某个主题或概念的标签[^runeson2009guidelines-e52]。全凭直觉、没有结构的分析，很难给出清楚的证据链[^runeson2009guidelines-e55]。编码的具体做法（归纳还是演绎、编码手册、要不要算一致性）见[访谈研究](interview_study.md#第五步编码和主题分析)。
- **留下痕迹**：记录分析中的每个决定，保留访谈提纲等工具的每个版本，记下数据、编码和备忘之间的联系[^runeson2009guidelines-e54]。一个可借鉴的做法：给转录稿中的每条陈述编号，由两名研究者分类[^runeson2009guidelines-e53]。
- **主动找反例。** 反例分析是主动寻找能推翻你假设的其他解释[^runeson2009guidelines-e51]。多人分析能减少个人偏差[^runeson2009guidelines-e16]。
- **不要把乱的讲成整齐的。** 把复杂、混乱的现象讲得过于简单、过于合理，是反面模式[^ralph2020empirical-e432]。

### 第八步：做分析性推广，而不是统计推广

"只有一个案例，怎么推广？"这个质疑不成立：案例研究本来就不追求统计推广，它追求**分析性推广**：把结果推广到具有共同特征的其他案例，也就是形成理论[^runeson2009guidelines-e56]。SIGSOFT 标准明确把"样本只有一个，结论无法推广"列为不成立的批评：案例研究的目的是深入研究一个对象，它应当带来原则上可迁移的概念[^ralph2020empirical-e433]。Sharp 等人引用过一个比喻：一只燕子不成夏天，但一只燕子足以证明燕子存在；仔细解剖一只燕子，也能得到大量可靠的燕子解剖知识[^sharp2016role-e13]。

**怎么做到**：详细描述现场[^ralph2020empirical-e419]，让读者能判断结论能否迁移到自己的情况（可迁移性[^ralph2020empirical-e436]）；把结论和已有理论联系起来 `[本项目分析]`。在验证型案例研究中，证据靠后续案例不断积累[^easterbrook2008selecting-e18]。

### 第九步：报告

- **详细描述现场**，同时防止身份暴露。"瑞典一家大型电信公司"几乎等于点名爱立信[^runeson2009guidelines-e60]。只去掉公司名和人名不一定够，对象来自很小的群体时可能凭特征被认出来[^runeson2009guidelines-e38]。内部特征（单元规模、人员平均年龄等）可能比行业、营业额这类外部特征更有用[^runeson2009guidelines-e61]。
- **写出研究过程的历史**：谁在什么时候做了什么，而不只是一句"我们用半结构化访谈做了案例研究"[^runeson2009guidelines-e63]。研究问题中途有较大改变，也要说明[^runeson2009guidelines-e62]。
- **给出数据片段**，如引语、匿名化的叙述，让读者能核对结论[^runeson2009guidelines-e64]。但引语只用来说明结论，不能代替结论；每条结论要脱离引语独立写清楚[^ralph2020empirical-e426]。

---

## 3. 民族志有什么不同

民族志的目标是理解一个群体的成员怎样看待自己的社会互动[^easterbrook2008selecting-e20]。它有四个主要特征[^sharp2016role-e3]：

1. **从成员的视角看问题**：对他们来说什么重要、什么让他们头疼，而不是研究者觉得什么重要[^sharp2016role-e4]。
2. **关注日常细节**。数据收集计划要灵活，但灵活不等于不严谨。研究者带着开放的心态进入现场，而不是脑袋空空[^sharp2016role-e8]。
3. **分析的立场**。民族志研究者不是只报道所见所闻的记者[^sharp2016role-e9]，要解释"为什么"：什么让人沮丧、什么阻碍进展、什么让团队运转良好[^sharp2016role-e11]。
4. **厚描述**：给出丰富、详细的描述，让结论经得起学术检验[^sharp2016role-e3]。它的结果适合分析性推广，不适合统计推广[^sharp2016role-e12]。

**参与式观察在软件开发中的样子。** 企业往往不愿让外人访问代码仓库，所以参与式观察通常指在团队中承担一个有意义的角色，例如承担文档工作或帮项目做行政支持[^sharp2016role-e15][^sharp2016role-e16]。观察几乎总要辅以访谈、文档分析[^sharp2016role-e14]。研究开源或跨地域团队时，线上环境也是研究现场[^sharp2016role-e18]。

**现场笔记。** 观察要留下记录。例如 Sharp & Robinson 和一个极限编程团队待了一周，数据包括现场笔记、会议录音、照片和工作产物副本[^runeson2009guidelines-e49]；也可以用访谈补充观察笔记[^easterbrook2008selecting-e21]。实用建议 `[本项目分析]`：当天就整理笔记；把"看到了什么"和"我怎么理解"分开写，后者作为备忘单独标出，这样证据链才分得清哪是数据、哪是解读。

**自己是"内行"的利与弊。** 研究者懂软件开发，更能理解从业者的讨论和想法[^sharp2016role-e25]。但也容易想当然、评判别人；从业者还会期待你给出指导[^sharp2016role-e24][^sharp2016role-e19]。所以要公开自己的研究兴趣和意图，并考虑研究会怎样影响被观察的团队[^sharp2016role-e20]。

**适合和不适合的问题。** 民族志适合关注合作、社会和人的因素的问题[^sharp2016role-e21]，例如"团队实际怎样用极限编程开发"，而不是"结对编程是否更高效"[^sharp2016role-e22]。它依赖现有实践，帮不了彻底改变实践的工具或方法[^sharp2016role-e23]。

> **不同的看法：民族志要做多久？它算不算案例研究？**
>
> - **几周就可以，属于案例研究的一种**：Sharp 等人认为，一般几周就能出好结果，"一定要做很久"是常见误解[^sharp2016role-e5]；他们的例子是三周，其中一周全天观察[^sharp2016role-e6]。SIGSOFT 标准把民族志归入案例研究[^ralph2020empirical-e417]；Runeson & Höst 也把它看作案例研究的一种特殊类型[^runeson2009guidelines-e21]。
> - **可能需要更久，而且是另一种方法**：Easterbrook 等人认为，参与式观察要求研究者被群体当成自己人，可能需要比"几周"长得多的时间[^easterbrook2008selecting-e22]；民族志不去证明假设，而是建立局部理论，这一立场把它和案例研究区分开[^easterbrook2008selecting-e23]。
>
> 实际操作：时长按研究问题和团队的工作节奏来定。Sharp 等人的例子按团队三周一个迭代来安排[^sharp2016role-e6]。不必全职驻场，少去几天、中间开始分析也可以[^sharp2016role-e17]。论文里说清你观察了多久、以什么身份参与。`[本项目分析]`

---

## 4. 效度：用什么标准评价

效度的一般概念见通用篇[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md#6-说清效度威胁)，定性研究的质量标准（可信度、可迁移性等）见[访谈研究](interview_study.md#先记住定性研究的质量标准和定量研究不同)。案例研究要注意两点。**第一，从设计阶段就考虑**，到分析时才想就太晚了[^runeson2009guidelines-e2]。案例研究的主要弱点是更容易受研究者偏差影响[^easterbrook2008selecting-e17]。几种常用做法[^runeson2009guidelines-e59][^easterbrook2008selecting-e27]：三角验证；维护详细的方案；请同行评审设计；请研究对象审阅数据和结论（参与者核查）；在现场待足够长的时间；报告和主流结论不一致的信息。**第二，用对标准**，见下面的分歧。

> **不同的看法：用定量研究的效度术语，还是定性研究的？**
>
> - **沿用四类效度**：Runeson & Höst 知道有人主张为灵活设计的研究另用一套标准（可信度、可迁移性等），但他们选择沿用原有术语，按灵活设计的研究重新解释[^runeson2009guidelines-e65]：构念效度、内部效度、外部效度、可靠性[^runeson2009guidelines-e3][^runeson2009guidelines-e57][^runeson2009guidelines-e5][^runeson2009guidelines-e58]。
> - **改用定性标准**：SIGSOFT 标准认为，案例研究应该用可信度、多声音性、反思性、严谨性、可迁移性等定性标准评价；可复制性、可推广性、客观性一般不适用[^ralph2020empirical-e429]。
>
> 两者其实有交集：都要求说清偏差从哪来、结论能用到哪里。实际操作：按投稿社区的惯例选术语，并在论文里说明你用的是哪一套。`[本项目分析]` 两边都同意的一点是：**内部效度只在研究因果关系时才需要讨论**[^runeson2009guidelines-e57][^ralph2020empirical-e434]。

---

## 5. 检查清单

下面主要依据 SIGSOFT 实证研究标准中的案例研究与民族志标准。

**必须做到**

- [ ] 论证为什么选这个（些）案例或现场[^ralph2020empirical-e419]
- [ ] 详细描述现场；现场真实存在，不是玩具例子或虚构情境[^ralph2020empirical-e419]
- [ ] 说明是哪种案例研究（探索型、解释型、描述型等）[^ralph2020empirical-e420]
- [ ] 描述数据来源，如参与者的背景和工作角色；定义分析单元[^ralph2020empirical-e420]
- [ ] 从观察到结论有清楚的证据链[^ralph2020empirical-e421]

**做到更好**

- [ ] 在数据来源、信息提供者或研究者之间做三角验证；用观察或档案记录核对受访者的说法[^ralph2020empirical-e423]；使用观察，并把观察结果整合进结论[^ralph2020empirical-e424]
- [ ] 描述可能影响案例的外部事件；说明自己原有的理解怎样影响了研究；反思自己的偏见[^ralph2020empirical-e425][^ralph2020empirical-e427]
- [ ] 用引语说明结论，但结论能脱离引语独立成立[^ralph2020empirical-e426]
- [ ] 提供访谈提纲、编码方案、编码示例等补充材料[^ralph2020empirical-e422]

**做得出色**

- [ ] 多个深入的案例，并做跨案例三角验证[^ralph2020empirical-e428]
- [ ] 团队分析，如多人编码并分析一致性[^ralph2020empirical-e428]
- [ ] 事先公开发布案例研究方案[^ralph2020empirical-e428]

**审稿时常见、但不成立的批评**：你不必为此担心

- "没有定量数据"[^ralph2020empirical-e434]
- "样本只有一个，结论无法推广"[^ralph2020empirical-e433]
- "缺乏内部效度"（除非你要确立因果关系）[^ralph2020empirical-e434]
- "不可复现，数据没公开"（定性数据常常是保密的）[^ralph2020empirical-e435]
- "访谈数量或时长不够"：没有神奇的数字，关键是数据足以让结论可信[^ralph2020empirical-e435]

---

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 把演示用的例子叫"案例研究" | 没有真实环境，不符合定义[^easterbrook2008selecting-e10][^runeson2009guidelines-e28] |
| 只做访谈，不用其他来源印证 | 受访者会合理化、选择性记忆[^sharp2016role-e2][^ralph2020empirical-e432] |
| 案例是"正好联系上的"，却不说明 | 读者无法判断案例是否适合回答问题[^runeson2009guidelines-e30][^ralph2020empirical-e419] |
| 进场前没谈好保密和发表 | 后期发表受阻或被推迟[^runeson2009guidelines-e34][^easterbrook2008selecting-e26] |
| 以为去掉公司名就匿名了 | 可能凭特征被认出来[^runeson2009guidelines-e38][^runeson2009guidelines-e60] |
| 只写结论，不写从数据到结论的过程 | 没有证据链，读者无法核对[^ralph2020empirical-e421][^runeson2009guidelines-e50] |
| 用"样本小"自我否定，或硬做统计推广 | 案例研究追求分析性推广[^runeson2009guidelines-e56][^ralph2020empirical-e433] |
| 民族志只描述所见，不做分析 | 民族志不只是描述，还要解释"为什么"[^sharp2016role-e10] |

---

## 7. 延伸阅读

- **案例研究的完整指南**：Runeson & Höst 2009，按设计、数据收集、分析、报告各阶段给出做法和检查清单，并附三个真实案例。
- **方法怎么选**：Easterbrook 等人 2008，比较实验、案例研究、调查、民族志、行动研究各适合回答什么问题。
- **民族志入门**：Sharp, Dittrich & de Souza 2016，讲民族志的四个特征和研究设计的五个维度，附八个软件工程中的民族志例子。
- **什么才算案例研究**：Wohlin 2021，篇幅很短，适合动笔前对照检查。
- **标准原文**：SIGSOFT 实证研究标准的 Case Study and Ethnography 部分，推荐读物中首推 Yin 的案例研究方法专著[^ralph2020empirical-e440]。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^ralph2020empirical-e414]: SIGSOFT 案例研究与民族志标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e414)
[^ralph2020empirical-e415]: SIGSOFT 案例研究与民族志标准，Application。[证据](../../../../sources/notes/ralph2020empirical.md#e415)
[^ralph2020empirical-e416]: SIGSOFT 案例研究与民族志标准，Application。[证据](../../../../sources/notes/ralph2020empirical.md#e416)
[^ralph2020empirical-e417]: SIGSOFT 案例研究与民族志标准，Application。[证据](../../../../sources/notes/ralph2020empirical.md#e417)
[^ralph2020empirical-e419]: SIGSOFT 案例研究与民族志标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e419)
[^ralph2020empirical-e420]: SIGSOFT 案例研究与民族志标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e420)
[^ralph2020empirical-e421]: SIGSOFT 案例研究与民族志标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e421)
[^ralph2020empirical-e422]: SIGSOFT 案例研究与民族志标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e422)
[^ralph2020empirical-e423]: SIGSOFT 案例研究与民族志标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e423)
[^ralph2020empirical-e424]: SIGSOFT 案例研究与民族志标准，加分项及脚注 2。[证据](../../../../sources/notes/ralph2020empirical.md#e424)
[^ralph2020empirical-e425]: SIGSOFT 案例研究与民族志标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e425)
[^ralph2020empirical-e426]: SIGSOFT 案例研究与民族志标准，加分项及脚注 4。[证据](../../../../sources/notes/ralph2020empirical.md#e426)
[^ralph2020empirical-e427]: SIGSOFT 案例研究与民族志标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e427)
[^ralph2020empirical-e428]: SIGSOFT 案例研究与民族志标准，优秀项。[证据](../../../../sources/notes/ralph2020empirical.md#e428)
[^ralph2020empirical-e429]: SIGSOFT 案例研究与民族志标准，General Quality Criteria。[证据](../../../../sources/notes/ralph2020empirical.md#e429)
[^ralph2020empirical-e431]: SIGSOFT 案例研究与民族志标准，Types of Case Studies。[证据](../../../../sources/notes/ralph2020empirical.md#e431)
[^ralph2020empirical-e432]: SIGSOFT 案例研究与民族志标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e432)
[^ralph2020empirical-e433]: SIGSOFT 案例研究与民族志标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e433)
[^ralph2020empirical-e434]: SIGSOFT 案例研究与民族志标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e434)
[^ralph2020empirical-e435]: SIGSOFT 案例研究与民族志标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e435)
[^ralph2020empirical-e436]: SIGSOFT 标准术语表，Credibility / Transferability / Reflexivity。[证据](../../../../sources/notes/ralph2020empirical.md#e436)
[^ralph2020empirical-e438]: SIGSOFT 标准术语表，Gatekeeper。[证据](../../../../sources/notes/ralph2020empirical.md#e438)
[^ralph2020empirical-e439]: SIGSOFT 伦理补充标准（有人参与的研究），Application。[证据](../../../../sources/notes/ralph2020empirical.md#e439)
[^ralph2020empirical-e440]: SIGSOFT 案例研究与民族志标准，Suggested Readings。[证据](../../../../sources/notes/ralph2020empirical.md#e440)
[^runeson2009guidelines-e2]: Runeson & Höst 2009，§5.2.3，第 153 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e2)
[^runeson2009guidelines-e3]: Runeson & Höst 2009，§5.2.3，构念效度。[证据](../../../../sources/notes/runeson2009guidelines.md#e3)
[^runeson2009guidelines-e5]: Runeson & Höst 2009，§5.2.3，外部效度。[证据](../../../../sources/notes/runeson2009guidelines.md#e5)
[^runeson2009guidelines-e20]: Runeson & Höst 2009，§2.1，第 134 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e20)
[^runeson2009guidelines-e21]: Runeson & Höst 2009，§2.1，第 134 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e21)
[^runeson2009guidelines-e22]: Runeson & Höst 2009，§2.2，第 136 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e22)
[^runeson2009guidelines-e23]: Runeson & Höst 2009，§2.2，第 137 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e23)
[^runeson2009guidelines-e25]: Runeson & Höst 2009，§2.4，第 138 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e25)
[^runeson2009guidelines-e26]: Runeson & Höst 2009，§2.5，第 138 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e26)
[^runeson2009guidelines-e27]: Runeson & Höst 2009，§3.1，第 139 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e27)
[^runeson2009guidelines-e28]: Runeson & Höst 2009，§3.1，第 139 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e28)
[^runeson2009guidelines-e29]: Runeson & Höst 2009，§3.1，第 140 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e29)
[^runeson2009guidelines-e30]: Runeson & Höst 2009，§3.1，第 140 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e30)
[^runeson2009guidelines-e31]: Runeson & Höst 2009，§3.2，第 141 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e31)
[^runeson2009guidelines-e32]: Runeson & Höst 2009，§3.2，第 141 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e32)
[^runeson2009guidelines-e33]: Runeson & Höst 2009，§3.2，第 141 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e33)
[^runeson2009guidelines-e34]: Runeson & Höst 2009，§3.3，第 142 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e34)
[^runeson2009guidelines-e35]: Runeson & Höst 2009，§3.3，第 142 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e35)
[^runeson2009guidelines-e36]: Runeson & Höst 2009，§3.3，第 143 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e36)
[^runeson2009guidelines-e37]: Runeson & Höst 2009，§3.3，第 143 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e37)
[^runeson2009guidelines-e38]: Runeson & Höst 2009，§3.3，第 143 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e38)
[^runeson2009guidelines-e39]: Runeson & Höst 2009，§3.3，第 143 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e39)
[^runeson2009guidelines-e42]: Runeson & Höst 2009，§3.3，第 143–144 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e42)
[^runeson2009guidelines-e43]: Runeson & Höst 2009，§4.1，第 144 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e43)
[^runeson2009guidelines-e44]: Runeson & Höst 2009，§2.2，第 136 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e44)
[^runeson2009guidelines-e45]: Runeson & Höst 2009，§4.1，第 145 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e45)
[^runeson2009guidelines-e46]: Runeson & Höst 2009，§4.2，第 146–147 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e46)
[^runeson2009guidelines-e48]: Runeson & Höst 2009，§4.3，第 148 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e48)
[^runeson2009guidelines-e49]: Runeson & Höst 2009，§4.3，第 148 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e49)
[^runeson2009guidelines-e50]: Runeson & Höst 2009，§5.1，第 150–151 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e50)
[^runeson2009guidelines-e15]: Runeson & Höst 2009，§5.1，第 151 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e15)
[^runeson2009guidelines-e16]: Runeson & Höst 2009，§5.1，第 151 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e16)
[^runeson2009guidelines-e51]: Runeson & Höst 2009，§5.2，第 151 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e51)
[^runeson2009guidelines-e52]: Runeson & Höst 2009，§5.2，第 151 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e52)
[^runeson2009guidelines-e53]: Runeson & Höst 2009，§5.2，第 152 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e53)
[^runeson2009guidelines-e54]: Runeson & Höst 2009，§5.2，第 153 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e54)
[^runeson2009guidelines-e55]: Runeson & Höst 2009，§5.2，第 153 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e55)
[^runeson2009guidelines-e56]: Runeson & Höst 2009，§5.2.3，第 154 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e56)
[^runeson2009guidelines-e57]: Runeson & Höst 2009，§5.2.3，第 154 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e57)
[^runeson2009guidelines-e58]: Runeson & Höst 2009，§5.2.3，第 154 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e58)
[^runeson2009guidelines-e59]: Runeson & Höst 2009，§5.2.3，第 154 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e59)
[^runeson2009guidelines-e60]: Runeson & Höst 2009，§6.1，第 155 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e60)
[^runeson2009guidelines-e61]: Runeson & Höst 2009，§6.1，第 155 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e61)
[^runeson2009guidelines-e62]: Runeson & Höst 2009，§6.1，第 155 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e62)
[^runeson2009guidelines-e63]: Runeson & Höst 2009，§6.1，第 156 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e63)
[^runeson2009guidelines-e64]: Runeson & Höst 2009，§6.1，第 156 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e64)
[^runeson2009guidelines-e65]: Runeson & Höst 2009，§5.2.3，第 153 页。[证据](../../../../sources/notes/runeson2009guidelines.md#e65)
[^easterbrook2008selecting-e10]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e10)
[^easterbrook2008selecting-e12]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e12)
[^easterbrook2008selecting-e13]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e13)
[^easterbrook2008selecting-e14]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e14)
[^easterbrook2008selecting-e15]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e15)
[^easterbrook2008selecting-e16]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e16)
[^easterbrook2008selecting-e17]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e17)
[^easterbrook2008selecting-e18]: Easterbrook 等人 2008，§5.2。[证据](../../../../sources/notes/easterbrook2008selecting.md#e18)
[^easterbrook2008selecting-e19]: Easterbrook 等人 2008，§5.3。[证据](../../../../sources/notes/easterbrook2008selecting.md#e19)
[^easterbrook2008selecting-e20]: Easterbrook 等人 2008，§5.4。[证据](../../../../sources/notes/easterbrook2008selecting.md#e20)
[^easterbrook2008selecting-e21]: Easterbrook 等人 2008，§5.4。[证据](../../../../sources/notes/easterbrook2008selecting.md#e21)
[^easterbrook2008selecting-e22]: Easterbrook 等人 2008，§5.4。[证据](../../../../sources/notes/easterbrook2008selecting.md#e22)
[^easterbrook2008selecting-e23]: Easterbrook 等人 2008，§5.4。[证据](../../../../sources/notes/easterbrook2008selecting.md#e23)
[^easterbrook2008selecting-e25]: Easterbrook 等人 2008，Practical Considerations。[证据](../../../../sources/notes/easterbrook2008selecting.md#e25)
[^easterbrook2008selecting-e26]: Easterbrook 等人 2008，Practical Considerations。[证据](../../../../sources/notes/easterbrook2008selecting.md#e26)
[^easterbrook2008selecting-e27]: Easterbrook 等人 2008，§7.0（转述 Creswell 2002）。[证据](../../../../sources/notes/easterbrook2008selecting.md#e27)
[^sharp2016role-e1]: Sharp 等人 2016，§1。[证据](../../../../sources/notes/sharp2016role.md#e1)
[^sharp2016role-e2]: Sharp 等人 2016，§2.1 脚注 1。[证据](../../../../sources/notes/sharp2016role.md#e2)
[^sharp2016role-e3]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e3)
[^sharp2016role-e4]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e4)
[^sharp2016role-e5]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e5)
[^sharp2016role-e6]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e6)
[^sharp2016role-e8]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e8)
[^sharp2016role-e9]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e9)
[^sharp2016role-e10]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e10)
[^sharp2016role-e11]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e11)
[^sharp2016role-e12]: Sharp 等人 2016，§2.3。[证据](../../../../sources/notes/sharp2016role.md#e12)
[^sharp2016role-e13]: Sharp 等人 2016，§2.3（引 Anzai & Simon 1979）。[证据](../../../../sources/notes/sharp2016role.md#e13)
[^sharp2016role-e14]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e14)
[^sharp2016role-e15]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e15)
[^sharp2016role-e16]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e16)
[^sharp2016role-e17]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e17)
[^sharp2016role-e18]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e18)
[^sharp2016role-e19]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e19)
[^sharp2016role-e20]: Sharp 等人 2016，§2.4。[证据](../../../../sources/notes/sharp2016role.md#e20)
[^sharp2016role-e21]: Sharp 等人 2016，§4.2。[证据](../../../../sources/notes/sharp2016role.md#e21)
[^sharp2016role-e22]: Sharp 等人 2016，§4.2。[证据](../../../../sources/notes/sharp2016role.md#e22)
[^sharp2016role-e23]: Sharp 等人 2016，§4.2。[证据](../../../../sources/notes/sharp2016role.md#e23)
[^sharp2016role-e24]: Sharp 等人 2016，§4.3。[证据](../../../../sources/notes/sharp2016role.md#e24)
[^sharp2016role-e25]: Sharp 等人 2016，§4.3。[证据](../../../../sources/notes/sharp2016role.md#e25)
[^wohlin2021case-e1]: Wohlin 2021，摘要。[证据](../../../../sources/notes/wohlin2021case.md#e1)
[^wohlin2021case-e2]: Wohlin 2021，§1。[证据](../../../../sources/notes/wohlin2021case.md#e2)
[^wohlin2021case-e3]: Wohlin 2021，§4。[证据](../../../../sources/notes/wohlin2021case.md#e3)
[^wohlin2021case-e4]: Wohlin 2021，§4。[证据](../../../../sources/notes/wohlin2021case.md#e4)
[^wohlin2021case-e6]: Wohlin 2021，§6。[证据](../../../../sources/notes/wohlin2021case.md#e6)
[^wohlin2021case-e7]: Wohlin 2021，§6。[证据](../../../../sources/notes/wohlin2021case.md#e7)
