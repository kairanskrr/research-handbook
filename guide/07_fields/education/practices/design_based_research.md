# 基于设计的研究

> **状态**：初稿，待审阅 · **最后更新**：2026-10-08

本文讲**基于设计的研究**（design-based research）：研究者和教师合作，在真实课堂里一轮一轮地设计、试用、改进一种教学干预，同时提炼出别人也能用的设计原则和理论。[教育学学科概况](../README.md#本学科常用的研究方法)已经简单介绍过它，本文专讲怎么做。本文主要依据四份方法文献：Easterday 等人 2014 年在国际学习科学大会上发表的一篇会议论文；Bakker 和 van Eerde 2015 年为一本数学教育研究方法书写的入门章节，面向包括硕士、博士生在内的研究者[^bakker2015introduction-e1]；Scott 等人 2020 年发表的一篇方法文章，用他们自己的一项生物学教学研究做例子；Anderson 和 Shattuck 2012 年对这一方法十年进展的回顾。下文说"某某建议"的，都是这些作者的个人建议，不是学界统一的规定。

不在本文讲的：进学校的审批和"守门人"、按校历排时间，见[学科概况](../README.md#研究多在学校里做先过守门人)；未成年人同意、研究自己的学生等伦理通则，见[学科概况的伦理一节](../README.md#伦理未成年人守门人和研究自己的学生)；教师独自改进自己课堂的行动研究，见[学科概况的研究方法一节](../README.md#本学科常用的研究方法)（注意它和研究方法里的"行动研究"含义不同）；要证明一种干预"有效"的随机对照试验，见研究方法里的[对照实验](../../../06_methods/controlled_experiment.md)和学科概况的[证据标准](../README.md#证据标准what-works-clearinghouse-怎样给研究评级)。

**适用范围** `[本项目分析]`：这是教育学的研究方法，依据的是上面列出的四份教育研究方法文献。"造出新东西、再证明它有用"的通用逻辑，见研究套路里的[构建改进](../../../05_research-strategies/build_improve.md)；选题、做计划、写作等各学科共通的步骤，见主线各章，例如[收敛成项目](../../../01_from-interest-to-project/03_converge.md)和[讲清故事，写成论文](../../../04_write-and-publish/01_story-and-paper.md)。

**常服务的套路**：[构建改进](../../../05_research-strategies/build_improve.md)（以该套路页"常用的研究方法"一节为准）。

**读完本文，你应该能：**

- 判断你的问题适不适合用基于设计的研究，和行动研究、对照实验、单纯的教学材料开发分清楚；
- 和学校、教师组成团队，从一个真实问题和一套写明的设计猜想出发；
- 规划一轮一轮的"设计—实施—分析—再设计"，知道每轮收什么数据、怎样记设计日志；
- 从数据中既得出更好的设计，也提炼出可迁移的设计原则；处理"研究者就是设计者"带来的可信度和伦理问题，知道报告里要写什么。

---

## 1. 这是什么研究，什么时候用

**它要同时交出两样东西。** Easterday 等人说，学界普遍同意：基于设计的研究既要产出有效的教育干预，也要产出有用的理论[^easterday2014design-e1]。Bakker 和 van Eerde 的说法是：一边是教学材料这类有用的产品，一边是这些产品怎样在教育中使用的科学认识[^bakker2015introduction-e2]。这里的"干预"范围很广：一种学习活动、一种评估方式、一项管理措施（例如调整假期），或一个技术工具[^anderson2012design-e12]。

**为什么需要它。** Easterday 等人认为，"基础研究→应用研究→开发→产品"这条线性路子效果不好；而没有理论指导的设计，又容易零敲碎打、碰运气[^easterday2014design-e2]。Bakker 和 van Eerde 指出了随机对照试验的一个局限：新做法要先设计出来才能检验，而很多时候，设计创新的做法本身就需要大量研究[^bakker2015introduction-e29]。

**和相近研究的区别：**

| | 基于设计的研究 | 行动研究 | 对照实验、随机对照试验 | 单纯的教学材料开发 |
|---|---|---|---|---|
| 谁来做 | 研究者和教师组队，从定问题到发表都一起[^anderson2012design-e15][^scott2020design-e5] | 通常是教师自己[^anderson2012design-e5] | 研究者决定实施和分析，教师执行处理[^scott2020design-e30] | 设计者 |
| 干预能不能中途改 | 能，实施中就地修改[^scott2020design-e10] | 能 | 不能，整个实验期间固定[^scott2020design-e9] | 能 |
| 要不要产出理论 | 要，并且更明确地追求教学理论[^bakker2015introduction-e7] | 关注行动和改变[^bakker2015introduction-e7] | 检验已有理论 | 不要；有没有理论产出正是两者的区别[^bakker2015introduction-e3] |
| 能下的因果结论 | 不如随机对照试验有说服力[^bakker2015introduction-e6] | 弱 | 强 | 不追求 |

表中没有脚注的格子是本项目的归纳 `[本项目分析]`。几条判断办法：

- **你是任课教师，又是研究者。** Scott 等人的分法是：问题是"我怎样改进自己的课堂"，更接近行动研究；问题能产出可推广、可能广泛影响教学的结果，才符合基于设计的研究[^scott2020design-e6][^scott2020design-e7]。
- **你的目标是"证明这个干预有效"。** 那更像是效力研究或有效性研究的任务 `[本项目分析]`。美国教育科学研究所（Institute of Education Sciences，IES）和美国国家科学基金会（National Science Foundation，NSF）这两家资助方，为它们资助的教育研究划分了几种类型，见学科概况的[证据链一节](../README.md#一项研究常常只做证据链上的一段)。基于设计的研究大致对应其中的"设计与开发研究" `[本项目分析]`：依据已有理论和证据，迭代地设计开发干预[^ies2013common-e4]；按这两家的要求，项目结束时要交出一套"行动理论"（说明干预为什么会起作用的一串因果设想）、一组干预组成部分，以及有希望改善结果的**初步**证据[^ies2013common-e10]。
- **和其他学科对照** `[本项目分析]`。计算机篇的[工程研究](../../computer-science/practices/engineering_research.md)也"造东西再评估"；艺术的[基于实践的研究](../../arts/practices/practice_based_research.md)以创作本身为研究。基于设计的研究的特点是在真实课堂里、和教师一起、边改边研究。

**时间要算够。** 迭代多，很难知道什么时候算做完[^anderson2012design-e3]。Anderson 和 Shattuck 提到，Herrington 等人 2007 年专门写文章，讨论怎样在四年里把它做成博士论文[^anderson2012design-e7]；他们自己提出的部分解决办法，是资深研究者设立多年期计划，让研究生承担并"拥有"其中重要的一块[^anderson2012design-e18]。硕士或短期博士项目，可以只做一到两轮，并在开题时说清楚 `[本项目分析]`。

---

## 2. 怎么做

基于设计的研究没有公认的、像实验那样具体的统一流程，不同人做出来的样子不同[^easterday2014design-e3]。下面综合三种说法：Easterday 等人的六个阶段（聚焦、理解、确定、构思、做出、检验）[^easterday2014design-e4]，Bakker 和 van Eerde 的三阶段循环（准备与设计、教学实验、回溯分析）[^bakker2015introduction-e9]，以及 Scott 等人的四阶段循环（设计、检验、评估、反思）[^scott2020design-e31]。Scott 等人也提醒，他们的四个阶段实际上常常重叠[^scott2020design-e2]。

### 第一步：找合作学校和教师，先谈好分工

**怎么做**：组一个研究者加一线教师的团队。按 Anderson 和 Shattuck 的描述，双方从确定问题、读文献、设计和制作干预、实施、评估，一直合作到形成并发表设计原则[^anderson2012design-e15]。组队时就写下：谁设计、谁上课、谁收数据、谁分析、多久碰一次头、教师能在课上自行调整到什么程度 `[本项目分析]`。

**为什么**：Anderson 和 Shattuck 说，教师通常太忙，也常缺少做严谨研究的训练；研究者则常常不了解实际运转的学校在文化、技术、目标和内部政治上的复杂之处[^anderson2012design-e14]。Scott 等人认为，教师是团队成员，就能在实施中做有依据的调整，同时不偏离研究目标[^scott2020design-e29]。

**容易错在哪里**：低估合作的难度。Scott 等人提醒，迭代要求合作维持很长时间，组队时就要正视这些困难，并明确研究者和教师各自的角色[^scott2020design-e24]。进校审批、校历和招募的一般问题见[学科概况](../README.md#时间表要按校历倒排)。

### 第二步：从一个真实问题出发，先把问题弄懂

**怎么做**（按 Easterday 等人的前三个阶段）：
1. **聚焦**：划定服务对象（学习者，以及家长、社区等受影响的人）、主题和范围[^easterday2014design-e5]。Scott 等人说，学习问题通常来自研究者自己在课堂内外的经验，或已有文献[^scott2020design-e12]。
2. **理解**：研究学习者、学科内容、具体环境和已有的解决办法[^easterday2014design-e6]。设计干预要从准确评估本地情况开始，参考相关文献和别处的实践[^anderson2012design-e11]。
3. **确定目标**：定下目标和评估方式[^easterday2014design-e7]。只有先定下目标，才谈得上设计成功还是失败[^easterday2014design-e8]。

**为什么**：Scott 等人按 Sandoval 提出的原则要求，选的问题必须能推进某种学习理论[^scott2020design-e13]。有没有理论产出，正是它和单纯开发教学材料的区别[^bakker2015introduction-e3]。

**容易错在哪里**：只写"提高学生的统计学习兴趣"，没有定下怎样算成功；或者问题只关乎本校本班，说不出能推进哪一条理论 `[本项目分析]`。怎样把题目变成能回答的问题，见主线章节[从研究问题到证据清单](../../../02_from-project-to-study/01_question-to-evidence.md#1-把主张拆成研究问题)。

### 第三步：动手前，把设计背后的猜想写出来

**怎么做**：Easterday 等人建议，先不急着做成品，用示意图把方案拆开，分析它由哪些部分组成、各部分怎样配合起作用[^easterday2014design-e9]。另外三种做法：

- **画出设计猜想**（据 Scott 等人转述 Sandoval 2014 的做法，本文未读到 Sandoval 原文）：列出设计中理论上关键的特征，画出预计它们怎样共同产生期望的结果[^scott2020design-e26]。这样在动手前就讲明：学习理论怎样体现在工具里、工具会产生哪些可分析的数据、什么结果算成功的证据[^scott2020design-e27]。
- **写假设的学习轨迹**（hypothetical learning trajectory，Bakker 和 van Eerde 在数学教育中使用）：写下学习目标、学生的起点和已有知识、要用的任务，以及对学生可能怎样学、教师可以怎样支持的设想[^bakker2015introduction-e12]。
- **先攒一批候选任务**：Bakker 和 van Eerde 建议，第一轮设计时收集和自创一批可能有用的任务，和有设计经验的同行讨论[^bakker2015introduction-e15]。

**为什么**：Scott 等人认为，理论、教学工具和评估学生的方式三者对得上，是这类研究严谨的核心[^scott2020design-e14]。事先写下的预测，也是回溯分析时拿来和实际对照的标尺[^bakker2015introduction-e18]。

**容易错在哪里**：只有一份教案，没有写下"为什么这样设计会让学生这样学"。分析时就只能说"学生学会了"，说不出是设计中的哪一点起了作用 `[本项目分析]`。

### 第四步：一轮一轮地做，先粗后精

**怎么做**：每一轮包括设计、在课堂中实施、分析、再设计[^bakker2015introduction-e9]。Easterday 等人建议：早期做粗糙原型，只收集足以快速淘汰失败方案、找出有希望方案的最少数据[^easterday2014design-e14]；找到有希望的原型后，再用定性方法弄清它通过什么机制影响学习[^easterday2014design-e20]。原型可粗可精，看项目阶段和要检验的问题[^easterday2014design-e10]。Scott 等人转述的一条原则是：要在课堂里做持续较长时间、反复迭代的教学实验[^scott2020design-e4]。实施中可以改：教师或研究者可能觉得需要调整下一节课的活动[^bakker2015introduction-e28]，设计团队也可以在使用中调整工具，以应对没预料到的情况[^scott2020design-e15]。

**为什么**：不要把整套干预做完才发现不管用；快速做原型、检验、再设计，让干预逐步演化[^easterday2014design-e12]。一轮接一轮，也让前一轮形成的猜想能在后一轮中检验[^bakker2015introduction-e21]。

**容易错在哪里**：Easterday 等人提醒两种偏差：一开始就做随机对照实验，很可能浪费资源验证一个不好的设计；反过来，一直停在建构理论和做新设计上，又拿不出有力的效果证据[^easterday2014design-e15][^easterday2014design-e16]。他们说，规划时提前想清楚检验阶段，帮他们避开了这两种偏差[^easterday2014design-e18]。

### 第五步：每一轮收什么数据，怎样记设计日志

**怎么做**：
- **学生学习的数据**。Bakker 和 van Eerde 说，教学实验通常收集：学生作品、教学前后测、现场笔记、全班讨论录音、每节课录像，以及最后对学生和教师访谈的录像[^bakker2015introduction-e16]；他们还发现，课上对学生做 20 秒到 4 分钟的"微型访谈"很有用，前提是有系统地做[^bakker2015introduction-e17]。Scott 等人还列了作业、实验报告、态度问卷、活动参与率、访谈、课堂话语、考试数据等[^scott2020design-e16]。
- **实施过程的数据**。Scott 等人强调，工具实际怎样实施、哪些地方没按计划进行、工具或实施过程怎样被修改，都要收集[^scott2020design-e8]。
- **事先挑好数据**。可收的数据太多、成本也高，所以要事先确定用哪些数据、什么分析方法，来回答理论和实践问题[^scott2020design-e25]。要揭示学习机制，就要长时间收多种数据，常常需要大量时间和经费[^scott2020design-e28]。

**设计日志**：Bakker 和 van Eerde 说，中途的每次修改本身就是数据，要好好报告，有理论依据的修改说服力更强[^bakker2015introduction-e13]。按 Anderson 和 Shattuck 的描述，研究者要记下设计和实施干预所花的时间、投入和遇到的意外，让读者判断在自己的环境里能否做到[^anderson2012design-e13]。建议每次课后当天写一条，至少包括：日期和班级；原计划；实际发生了什么（尤其是和预想不同的地方）；改了什么、为什么改、依据哪条理论或哪份数据；改动由谁决定 `[本项目分析]`。

**为什么**：一个真实例子：Scott 等人回看 2017 年春季的实施记录，发现前测是在第一天上课、学生已经接触相关内容之后才截止的，这可能是前测成绩异常高的原因之一[^scott2020design-e19]；于是他们决定下一轮在开课前就关闭前测[^scott2020design-e20]。没有这份记录，他们就解释不了这个异常 `[本项目分析]`。日志怎样和其他研究材料一起管理，见贯穿全程的[整理科研材料](../../../08_throughout/organizing_materials.md#5-分清三种笔记)。

**容易错在哪里**：只收前后测，丢掉了过程数据，最后只能说"成绩提高了"，说不出怎样提高的；或者什么都录，却没人有时间分析 `[本项目分析]`。

### 第六步：回溯分析：既改设计，也提炼设计原则

**怎么做**：
1. **把预想和实际对照。** Bakker 和 van Eerde 用一张矩阵：左边写假设的学习轨迹（每个任务预想学生怎样反应），右边填转写摘录、研究者的说明，以及预想和实际的吻合程度[^bakker2015introduction-e18]。
2. **生成并检验猜想。** 以研究问题为指引，生成关于学生学习的猜想并记下来，再拿其他片段和数据去检验，既找支持也找反例[^bakker2015introduction-e19]。
3. **回答三个问题**（Scott 等人提出）：理论推进了什么？工具是否帮助了学生学习？设计中哪些关键特征起了作用（即设计原则）[^scott2020design-e18]？
4. **把设计原则写成别人能用的样子。** Scott 等人说，设计原则描述学习环境的特征，让别人据此开发适合自己情境的工具[^scott2020design-e21]，要在具体和可调整之间取得平衡[^scott2020design-e22]。Bakker 和 van Eerde 说，也可以写成预测的形式："在条件 X 下用方法 Y，学生可能学会 Z"[^bakker2015introduction-e4]。Scott 等人第一轮得出的原则之一是：教学工具要明确讲出目标原理，并具体指导怎样在情境中应用它[^scott2020design-e23]。

**为什么**：据 Scott 等人转述，Sandoval 说设计研究不是为了找"效果"，而是为了找"作用方式"，理解效果怎样在设计好的环境中产生[^scott2020design-e11]。目标不是"完美的教学序列"（Bakker 和 van Eerde 认为不存在），而是别人能按本地情况调整的、有实证基础的结果[^bakker2015introduction-e14]。

**容易错在哪里**：把设计原则写成放之四海而皆准的口号。Anderson 和 Shattuck 说，设计原则不是脱离情境的大理论，它反映的是它起作用的条件[^anderson2012design-e16]，所以要把条件写进去 `[本项目分析]`。

### 第七步：守住可信度：你既是设计者又是研究者

Anderson 和 Shattuck 引述了一条批评：研究者全程参与一种教学方法的构想、设计、实施和研究，要保证结论可信是个挑战[^anderson2012design-e6]。他们说，好的研究要求怀疑和超然，而这类研究又要求和伙伴同心、积极支持干预[^anderson2012design-e17]。Bakker 和 van Eerde 给出的做法：
- **找反例，跨轮检验**：用其他数据去检验猜想，并专门找反例[^bakker2015introduction-e19]；拿后一轮检验前一轮的猜想[^bakker2015introduction-e21]。
- **请同事挑战你的解释**：关键片段拿去和同事讨论，看他们是否同意、能否想到别的解释[^bakker2015introduction-e20]。
- **减少对你个人的依赖**：用录音录像等客观设备收数据[^bakker2015introduction-e24]；多人编码时，除了一致百分比，还要算 Cohen's kappa 等考虑了偶然一致的指标[^bakker2015introduction-e25]。
- **说清能推广到哪里**：它产出的理论通常绑定在具体学习环境上，难以推广[^bakker2015introduction-e8]。许多（主要是定性的）研究方法追求的是推到理论、模型或概念，而不是从随机样本推到总体[^bakker2015introduction-e5]；产出的理论还要能用到别处的课堂，这叫"可迁移性"[^bakker2015introduction-e10]。推广怎样论证，见研究方法里的[案例研究](../../../06_methods/case_study.md#第八步做分析性推广而不是统计推广)。

此外，美国 IES 和 NSF 的指南要求它们资助的设计与开发项目，理论框架、数据收集、分析和报告接受一系列外部的批判性审查[^ies2013common-e14]。不受这两家资助的项目，可以借鉴这个做法，例如请课题组以外的人定期审阅 `[本项目分析]`。效度的一般讲法见主线章节[效度与局限](../../../02_from-project-to-study/03_validity-and-limits.md)。Anderson 和 Shattuck 说这类研究通常用混合方法[^anderson2012design-e10]，多种数据怎样整合见研究方法里的[混合方法研究](../../../06_methods/mixed_methods.md)。

> **不同的看法：基于设计的研究要不要做随机对照、下因果结论？**
> - **Anderson 和 Shattuck**：他们回顾的研究普遍没有对照组，这和该方法的理念一致[^anderson2012design-e8]；大多数研究不产出证明"什么有效"的效应量[^anderson2012design-e9]。
> - **Bakker 和 van Eerde**：它不能以随机对照试验那样令人信服的严谨程度声称因果[^bakker2015introduction-e6]；成果按创新性和有用性评判，不只看过程的严谨[^bakker2015introduction-e27]。
> - **Easterday 等人**：随机对照检验可以嵌套在检验阶段，作为基于设计的研究的一部分[^easterday2014design-e13]；有了站得住的理论和初步成功的实施后，就可以用随机对照实验验证效果[^easterday2014design-e15]；一直不往这一步走，就很难拿出有力的效果证据[^easterday2014design-e16]。
>
> **实际建议** `[本项目分析]`：早期几轮写"怎样起作用"，不要写"证明有效"；结论里出现"提高了""有效"时，标明这是初步证据。如果项目后期确实要回答"有没有效"，就按对照实验或随机对照试验的标准单独设计那一部分。

### 第八步：伦理：设计者和研究者是同一个人

伦理通则见[学科概况的伦理一节](../README.md#伦理未成年人守门人和研究自己的学生)，那里已介绍英国教育研究协会（British Educational Research Association，BERA）的伦理指南。下面只补这条指南里和本类型特别相关的几点；其他国家以本地规定和本单位伦理审查要求为准 `[本项目分析]`：
- **你可能就是学生的老师。** BERA 要求考虑"教师兼研究者"的双重身份带来的权力关系[^bera2024ethical-e10]，尽量让学生放心：不参加完全没问题[^bera2024ethical-e12]；办法包括把研究者身份讲清楚、请独立的第三方参与研究过程[^bera2024ethical-e11]。
- **你希望干预成功。** 你既想证明自己的设计好，又要报告真实结果。BERA 要求报告干预和评估的所有结果，包括负面结果[^bera2024ethical-e16]。不管用的设计和被推翻的猜想，正是迭代研究的数据 `[本项目分析]`。
- **合作教师的负担和署名。** BERA 要求考虑研究给参与者生活和工作量带来的负担[^bera2024ethical-e23]；学者和教师合作的研究，凡有实质贡献的人都应列为合著者[^bera2024ethical-e18]。BERA 举例说，教师群体做行动研究应告知学校管理层[^bera2024ethical-e24]；合作做设计研究同样应让学校领导知情 `[本项目分析]`。
- **伦理申请要预留变化。** 设计会一轮轮改，申请时就写明"会在既定范围内调整活动和材料"，调整超出范围时补报 `[本项目分析]`。

### 第九步：报告：要写清什么

Bakker 和 van Eerde 说，基于设计的研究报告需要"深描"，所以往往很长[^bakker2015introduction-e22]。本文资料中没有专门针对基于设计的研究的报告规范；下面综合三方面：美国教育研究协会（American Educational Research Association，AERA）为其出版物制定的报告标准（详见[学科概况](../README.md#报告标准aera-的实证研究报告标准)），美国 IES 和 NSF 对其资助的设计与开发项目的产出要求，以及方法学者的建议。论文写作的一般方法见主线章节[讲清故事，写成论文](../../../04_write-and-publish/01_story-and-paper.md)。

- **讲清完整过程**，让读者能重建研究：失败和成功、所用程序、概念框架、做选择的理由[^bakker2015introduction-e26]。Easterday 等人发现，用阶段来组织，能更简洁地说清项目做过什么[^easterday2014design-e19]。
- **主要的设计迭代、每轮的证据，以及据此对行动理论和设计做了哪些调整**（IES 和 NSF 的要求）[^ies2013common-e11]。
- **干预本身**：AERA 标准要求描述得足够详细，让别人能识别其关键特征[^aera2006standards-e6]；IES 和 NSF 还要求交出实施所需的全部材料[^ies2013common-e11]。
- **你的角色**（AERA 标准）：怎样进入现场、研究者担任什么角色、关系后来有没有变化[^aera2006standards-e5]；研究者和参与者的关系会影响收集到的数据[^aera2006standards-e16]。
- **证据和反例**（AERA 标准中针对定性研究的条目）：每个论断给出证据，报告重要的反例[^aera2006standards-e11]；超出证据的推测明确标出[^aera2006standards-e12]；想推广时写清推广范围[^aera2006standards-e13]。
- **实施情况和初步效果**（IES 和 NSF 的要求）：在真实环境中的实施数据，以及显示干预有望带来预期结果的预研究数据[^ies2013common-e12]。

---

## 3. 检查清单

**必须做到**
- [ ] 问题来自真实教育情境，能推进一条学习理论[^scott2020design-e13]；写下了目标和成功标准[^easterday2014design-e8]
- [ ] 动手前写下了设计猜想：理论怎样体现在工具里、会产生什么数据、什么结果算成功[^scott2020design-e27]
- [ ] 在真实课堂中实施[^scott2020design-e4]，并收集了实施过程的数据[^scott2020design-e8]
- [ ] 每次修改都记录了内容和理由，并在报告中交代[^bakker2015introduction-e13]
- [ ] 分析时找过反例[^bakker2015introduction-e19]，产出了写明适用条件的设计原则[^scott2020design-e21][^anderson2012design-e16]
- [ ] 报告写清研究者的角色和与参与者的关系[^aera2006standards-e5]
- [ ] 处理了"教师兼研究者"的双重身份问题[^bera2024ethical-e10]；负面结果也报告[^bera2024ethical-e16]

**做到更好**
- [ ] 用多轮实施检验前一轮的猜想[^bakker2015introduction-e21]
- [ ] 关键片段请同事做同行检视[^bakker2015introduction-e20]；多人编码时报告考虑了偶然一致的一致性指标[^bakker2015introduction-e25]
- [ ] 接受外部的批判性审查（IES 和 NSF 对其资助项目的要求）[^ies2013common-e14]
- [ ] 记录干预所需时间、投入和意外，让读者判断能否在本地做到[^anderson2012design-e13]

**这些情况可以不做，不算缺陷**
- 没有对照组、没有效应量：Anderson 和 Shattuck 回顾的研究普遍如此，他们认为这和该方法的理念一致[^anderson2012design-e8][^anderson2012design-e9]；Easterday 等人也提醒，过早做随机对照实验可能浪费资源[^easterday2014design-e15]。但此时不要声称"证明有效" `[本项目分析]`。

**审稿时可能遇到、但不成立的批评**（这些批评有多常见，本文资料没有统计 `[本项目分析]`）

- "中途改了干预，实验就不成立了。"在比较实验中这确实一般不被接受，但在基于设计的研究里，修改是数据的一部分，前提是报告清楚、最好有理论依据[^bakker2015introduction-e13]。
- "样本不是随机抽的，不能推广。"这类研究追求的是推广到理论和可迁移性，不是统计推广[^bakker2015introduction-e5][^bakker2015introduction-e10]。如果作者自己声称了统计意义上的推广，这条批评就成立 `[本项目分析]`。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只交出一套教学材料，没有理论或设计原则 | 有没有理论产出，正是它和单纯开发工作的区别[^bakker2015introduction-e3] |
| 没写下设计猜想就开始上课 | 理论、工具和评估对不上，严谨性无从谈起[^scott2020design-e14] |
| 第一轮就做大规模随机对照试验 | 很可能浪费资源验证一个不好的设计[^easterday2014design-e15] |
| 无限迭代，迟迟不收尾 | 本来就难知道何时做完[^anderson2012design-e3]；要事先定下轮数和每轮目标 `[本项目分析]` |
| 改了设计却没记录 | 修改本身是数据，必须报告[^bakker2015introduction-e13]；事后也解释不了异常结果[^scott2020design-e19] |
| 什么都录，事先不定分析计划 | 数据多、成本高，必须事先确定用哪些数据回答什么问题[^scott2020design-e25] |
| 设计原则写成脱离情境的口号 | 设计原则应反映它起作用的条件[^anderson2012design-e16] |
| 研究者只报告支持自己设计的片段 | 结论可信本就是这类研究的难点[^anderson2012design-e6]；要找反例[^bakker2015introduction-e19]、报告负面结果[^bera2024ethical-e16] |
| 把初步证据写成"证明有效" | 它不能以随机对照试验那样的严谨程度声称因果[^bakker2015introduction-e6] |
| 把合作教师当作执行者，不署名 | 按英国 BERA 指南，有实质贡献的教师应列为合著者[^bera2024ethical-e18] |

---

## 5. 延伸阅读

- **Bakker & van Eerde 2015**：数学教育研究方法书中的一章，写给包括硕士、博士生在内的研究者，讲假设的学习轨迹、数据收集、分析矩阵和效度信度，附统计教育的例子。新手可以先读这一篇。
- **Scott, Wenderoth & Doherty 2020**：发表在 CBE—Life Sciences Education 的方法文章，用作者自己的一项生物学教学研究，完整走了一轮"设计—检验—评估—反思"，并讨论合作、资源和严谨性的困难。开放获取。
- **Easterday, Rees Lewis & Gerber 2014**：国际学习科学大会的会议论文，提出六阶段流程，以及"什么阶段用什么方法"的思路，适合规划项目和写资助申请。
- **Anderson & Shattuck 2012**：发表在 Educational Researcher，讲基于设计的研究的特征、难点，并回顾了十年来的研究。
- **IES & NSF 2013《教育研究与开发通用指南》**：美国这两家资助方对其资助的"设计与开发研究"项目的计划和产出要求，可当作报告清单参考。
- 本文未读到原文的：Sandoval 2014（Scott 等人多处转述，猜想的写法即出自此文）。

[^bakker2015introduction-e1]: Bakker & van Eerde 2015，§16.1.1，第 429 页。[证据](../../../../sources/notes/bakker2015introduction.md#e1)
[^easterday2014design-e1]: Easterday 等 2014，Introduction，第 317 页。[证据](../../../../sources/notes/easterday2014design.md#e1)
[^bakker2015introduction-e2]: Bakker & van Eerde 2015，§16.1.1，第 430 页。[证据](../../../../sources/notes/bakker2015introduction.md#e2)
[^anderson2012design-e12]: Anderson & Shattuck 2012，What is DBR?。[证据](../../../../sources/notes/anderson2012design.md#e12)
[^easterday2014design-e2]: Easterday 等 2014，Introduction，第 317 页。[证据](../../../../sources/notes/easterday2014design.md#e2)
[^bakker2015introduction-e29]: Bakker & van Eerde 2015，§16.1.2.5，第 434 页。[证据](../../../../sources/notes/bakker2015introduction.md#e29)
[^anderson2012design-e15]: Anderson & Shattuck 2012，collaborative partnership。[证据](../../../../sources/notes/anderson2012design.md#e15)
[^scott2020design-e5]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e5)
[^anderson2012design-e5]: Anderson & Shattuck 2012，Comparison to Action Research。[证据](../../../../sources/notes/anderson2012design.md#e5)
[^scott2020design-e30]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e30)
[^scott2020design-e10]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e10)
[^scott2020design-e9]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e9)
[^bakker2015introduction-e7]: Bakker & van Eerde 2015，§16.1.2.6，第 435 页。[证据](../../../../sources/notes/bakker2015introduction.md#e7)
[^bakker2015introduction-e3]: Bakker & van Eerde 2015，§16.1.2.1，第 430 页。[证据](../../../../sources/notes/bakker2015introduction.md#e3)
[^bakker2015introduction-e6]: Bakker & van Eerde 2015，§16.1.2.5，第 434 页。[证据](../../../../sources/notes/bakker2015introduction.md#e6)
[^scott2020design-e6]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e6)
[^scott2020design-e7]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e7)
[^ies2013common-e4]: IES & NSF 2013，Types of Research。[证据](../../../../sources/notes/ies2013common.md#e4)
[^ies2013common-e10]: IES & NSF 2013，Introduction。[证据](../../../../sources/notes/ies2013common.md#e10)
[^anderson2012design-e3]: Anderson & Shattuck 2012，Involving multiple iterations。[证据](../../../../sources/notes/anderson2012design.md#e3)
[^anderson2012design-e7]: Anderson & Shattuck 2012，Problems with DBR。[证据](../../../../sources/notes/anderson2012design.md#e7)
[^anderson2012design-e18]: Anderson & Shattuck 2012，Problems with DBR。[证据](../../../../sources/notes/anderson2012design.md#e18)
[^easterday2014design-e3]: Easterday 等 2014，Problem 1，第 317 页。[证据](../../../../sources/notes/easterday2014design.md#e3)
[^easterday2014design-e4]: Easterday 等 2014，Design Process，第 319 页。[证据](../../../../sources/notes/easterday2014design.md#e4)
[^bakker2015introduction-e9]: Bakker & van Eerde 2015，§16.1.2.9，第 438 页。[证据](../../../../sources/notes/bakker2015introduction.md#e9)
[^scott2020design-e31]: Scott 等 2020，What Is Design-Based Research?。[证据](../../../../sources/notes/scott2020design.md#e31)
[^scott2020design-e2]: Scott 等 2020，What Is Design-Based Research?。[证据](../../../../sources/notes/scott2020design.md#e2)
[^anderson2012design-e14]: Anderson & Shattuck 2012，collaborative partnership。[证据](../../../../sources/notes/anderson2012design.md#e14)
[^scott2020design-e29]: Scott 等 2020，Design-Based Research Fosters Collaborations across Disciplines。[证据](../../../../sources/notes/scott2020design.md#e29)
[^scott2020design-e24]: Scott 等 2020，Collaborations Can Be Difficult to Maintain。[证据](../../../../sources/notes/scott2020design.md#e24)
[^easterday2014design-e5]: Easterday 等 2014，Focus，第 319 页。[证据](../../../../sources/notes/easterday2014design.md#e5)
[^scott2020design-e12]: Scott 等 2020，Identifying the Learning Problem。[证据](../../../../sources/notes/scott2020design.md#e12)
[^easterday2014design-e6]: Easterday 等 2014，Understand，第 319 页。[证据](../../../../sources/notes/easterday2014design.md#e6)
[^anderson2012design-e11]: Anderson & Shattuck 2012，What is DBR?。[证据](../../../../sources/notes/anderson2012design.md#e11)
[^easterday2014design-e7]: Easterday 等 2014，Define，第 320 页。[证据](../../../../sources/notes/easterday2014design.md#e7)
[^easterday2014design-e8]: Easterday 等 2014，Define，第 320 页。[证据](../../../../sources/notes/easterday2014design.md#e8)
[^scott2020design-e13]: Scott 等 2020，Identifying the Learning Problem。[证据](../../../../sources/notes/scott2020design.md#e13)
[^easterday2014design-e9]: Easterday 等 2014，Conceive，第 320 页。[证据](../../../../sources/notes/easterday2014design.md#e9)
[^scott2020design-e26]: Scott 等 2020，Concerns with Experimental Rigor（引 Sandoval 2014）。[证据](../../../../sources/notes/scott2020design.md#e26)
[^scott2020design-e27]: Scott 等 2020，Concerns with Experimental Rigor。[证据](../../../../sources/notes/scott2020design.md#e27)
[^bakker2015introduction-e12]: Bakker & van Eerde 2015，§16.1.3.1，第 439 页。[证据](../../../../sources/notes/bakker2015introduction.md#e12)
[^bakker2015introduction-e15]: Bakker & van Eerde 2015，§16.1.4.1，第 441 页。[证据](../../../../sources/notes/bakker2015introduction.md#e15)
[^scott2020design-e14]: Scott 等 2020，Cycle 1, Phase 1。[证据](../../../../sources/notes/scott2020design.md#e14)
[^bakker2015introduction-e18]: Bakker & van Eerde 2015，§16.1.4.3，第 442 页。[证据](../../../../sources/notes/bakker2015introduction.md#e18)
[^easterday2014design-e14]: Easterday 等 2014，Stage Dependent Search，第 322 页。[证据](../../../../sources/notes/easterday2014design.md#e14)
[^easterday2014design-e20]: Easterday 等 2014，Stage Dependent Search，第 322 页。[证据](../../../../sources/notes/easterday2014design.md#e20)
[^easterday2014design-e10]: Easterday 等 2014，Build，第 320 页。[证据](../../../../sources/notes/easterday2014design.md#e10)
[^scott2020design-e4]: Scott 等 2020，What Is Design-Based Research?。[证据](../../../../sources/notes/scott2020design.md#e4)
[^bakker2015introduction-e28]: Bakker & van Eerde 2015，§16.1.3.2，第 439 页。[证据](../../../../sources/notes/bakker2015introduction.md#e28)
[^scott2020design-e15]: Scott 等 2020，Phase 2。[证据](../../../../sources/notes/scott2020design.md#e15)
[^easterday2014design-e12]: Easterday 等 2014，Iteration，第 321 页。[证据](../../../../sources/notes/easterday2014design.md#e12)
[^bakker2015introduction-e21]: Bakker & van Eerde 2015，§16.1.5.1，第 444 页。[证据](../../../../sources/notes/bakker2015introduction.md#e21)
[^easterday2014design-e15]: Easterday 等 2014，Stage Dependent Search，第 322 页。[证据](../../../../sources/notes/easterday2014design.md#e15)
[^easterday2014design-e16]: Easterday 等 2014，Stage Dependent Search，第 322 页。[证据](../../../../sources/notes/easterday2014design.md#e16)
[^easterday2014design-e18]: Easterday 等 2014，Better Design，第 322 页。[证据](../../../../sources/notes/easterday2014design.md#e18)
[^bakker2015introduction-e16]: Bakker & van Eerde 2015，§16.1.4.2，第 442 页。[证据](../../../../sources/notes/bakker2015introduction.md#e16)
[^bakker2015introduction-e17]: Bakker & van Eerde 2015，§16.1.4.2，第 442 页。[证据](../../../../sources/notes/bakker2015introduction.md#e17)
[^scott2020design-e16]: Scott 等 2020，Phase 3。[证据](../../../../sources/notes/scott2020design.md#e16)
[^scott2020design-e8]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?。[证据](../../../../sources/notes/scott2020design.md#e8)
[^scott2020design-e25]: Scott 等 2020，Design-Based Research Experiments Are Resource Intensive。[证据](../../../../sources/notes/scott2020design.md#e25)
[^scott2020design-e28]: Scott 等 2020，Design-Based Research Experiments Are Resource Intensive。[证据](../../../../sources/notes/scott2020design.md#e28)
[^bakker2015introduction-e13]: Bakker & van Eerde 2015，§16.1.3.2，第 440 页。[证据](../../../../sources/notes/bakker2015introduction.md#e13)
[^anderson2012design-e13]: Anderson & Shattuck 2012，What is DBR?。[证据](../../../../sources/notes/anderson2012design.md#e13)
[^scott2020design-e19]: Scott 等 2020，Practical Outcome。[证据](../../../../sources/notes/scott2020design.md#e19)
[^scott2020design-e20]: Scott 等 2020，Practical Outcome。[证据](../../../../sources/notes/scott2020design.md#e20)
[^bakker2015introduction-e19]: Bakker & van Eerde 2015，§16.1.4.3，第 443 页。[证据](../../../../sources/notes/bakker2015introduction.md#e19)
[^scott2020design-e18]: Scott 等 2020，Phase 4。[证据](../../../../sources/notes/scott2020design.md#e18)
[^scott2020design-e21]: Scott 等 2020，Design Principles。[证据](../../../../sources/notes/scott2020design.md#e21)
[^scott2020design-e22]: Scott 等 2020，Design Principles。[证据](../../../../sources/notes/scott2020design.md#e22)
[^bakker2015introduction-e4]: Bakker & van Eerde 2015，§16.1.2.2，第 431 页。[证据](../../../../sources/notes/bakker2015introduction.md#e4)
[^scott2020design-e23]: Scott 等 2020，Design Principles。[证据](../../../../sources/notes/scott2020design.md#e23)
[^scott2020design-e11]: Scott 等 2020，How Is Design-Based Research Different from an Experimental Approach?（引 Sandoval 2014）。[证据](../../../../sources/notes/scott2020design.md#e11)
[^bakker2015introduction-e14]: Bakker & van Eerde 2015，§16.1.3.3，第 440 页。[证据](../../../../sources/notes/bakker2015introduction.md#e14)
[^anderson2012design-e16]: Anderson & Shattuck 2012，Evolution of design-principles。[证据](../../../../sources/notes/anderson2012design.md#e16)
[^anderson2012design-e6]: Anderson & Shattuck 2012，Problems with DBR。[证据](../../../../sources/notes/anderson2012design.md#e6)
[^anderson2012design-e17]: Anderson & Shattuck 2012，Problems with DBR。[证据](../../../../sources/notes/anderson2012design.md#e17)
[^bakker2015introduction-e20]: Bakker & van Eerde 2015，§16.1.4.3，第 443 页。[证据](../../../../sources/notes/bakker2015introduction.md#e20)
[^bakker2015introduction-e24]: Bakker & van Eerde 2015，§16.1.5.3，第 445 页。[证据](../../../../sources/notes/bakker2015introduction.md#e24)
[^bakker2015introduction-e25]: Bakker & van Eerde 2015，§16.1.5.3，第 445 页。[证据](../../../../sources/notes/bakker2015introduction.md#e25)
[^bakker2015introduction-e8]: Bakker & van Eerde 2015，§16.1.2.8，第 437 页。[证据](../../../../sources/notes/bakker2015introduction.md#e8)
[^bakker2015introduction-e5]: Bakker & van Eerde 2015，§16.1.2.5，第 434 页。[证据](../../../../sources/notes/bakker2015introduction.md#e5)
[^bakker2015introduction-e10]: Bakker & van Eerde 2015，§16.1.2.9，第 438 页。[证据](../../../../sources/notes/bakker2015introduction.md#e10)
[^ies2013common-e14]: IES & NSF 2013，附录，External Feedback Plan。[证据](../../../../sources/notes/ies2013common.md#e14)
[^anderson2012design-e10]: Anderson & Shattuck 2012，Use of mixed methods。[证据](../../../../sources/notes/anderson2012design.md#e10)
[^anderson2012design-e8]: Anderson & Shattuck 2012，Results。[证据](../../../../sources/notes/anderson2012design.md#e8)
[^anderson2012design-e9]: Anderson & Shattuck 2012，Results。[证据](../../../../sources/notes/anderson2012design.md#e9)
[^bakker2015introduction-e27]: Bakker & van Eerde 2015，§16.1.2.3，第 432 页。[证据](../../../../sources/notes/bakker2015introduction.md#e27)
[^easterday2014design-e13]: Easterday 等 2014，Recursively Nested Research Processes，第 322 页。[证据](../../../../sources/notes/easterday2014design.md#e13)
[^bera2024ethical-e10]: BERA 2024，第 19 段。[证据](../../../../sources/notes/bera2024ethical.md#e10)
[^bera2024ethical-e12]: BERA 2024，第 20 段。[证据](../../../../sources/notes/bera2024ethical.md#e12)
[^bera2024ethical-e11]: BERA 2024，第 19 段。[证据](../../../../sources/notes/bera2024ethical.md#e11)
[^bera2024ethical-e16]: BERA 2024，第 69 段。[证据](../../../../sources/notes/bera2024ethical.md#e16)
[^bera2024ethical-e23]: BERA 2024，第 37 段。[证据](../../../../sources/notes/bera2024ethical.md#e23)
[^bera2024ethical-e18]: BERA 2024，第 76 段。[证据](../../../../sources/notes/bera2024ethical.md#e18)
[^bera2024ethical-e24]: BERA 2024，第 52 段。[证据](../../../../sources/notes/bera2024ethical.md#e24)
[^bakker2015introduction-e22]: Bakker & van Eerde 2015，§16.1.5.1，第 444 页。[证据](../../../../sources/notes/bakker2015introduction.md#e22)
[^bakker2015introduction-e26]: Bakker & van Eerde 2015，§16.1.5.4，第 445 页。[证据](../../../../sources/notes/bakker2015introduction.md#e26)
[^easterday2014design-e19]: Easterday 等 2014，Communicating Research Process，第 323 页。[证据](../../../../sources/notes/easterday2014design.md#e19)
[^ies2013common-e11]: IES & NSF 2013，Table 4，Design and Development Research。[证据](../../../../sources/notes/ies2013common.md#e11)
[^aera2006standards-e6]: AERA 2006，3.1.d。[证据](../../../../sources/notes/aera2006standards.md#e6)
[^aera2006standards-e5]: AERA 2006，3.1.b。[证据](../../../../sources/notes/aera2006standards.md#e5)
[^aera2006standards-e16]: AERA 2006，3. Sources of Evidence。[证据](../../../../sources/notes/aera2006standards.md#e16)
[^aera2006standards-e11]: AERA 2006，5.12。[证据](../../../../sources/notes/aera2006standards.md#e11)
[^aera2006standards-e12]: AERA 2006，5.12。[证据](../../../../sources/notes/aera2006standards.md#e12)
[^aera2006standards-e13]: AERA 2006，6.2。[证据](../../../../sources/notes/aera2006standards.md#e13)
[^ies2013common-e12]: IES & NSF 2013，Table 4，Design and Development Research。[证据](../../../../sources/notes/ies2013common.md#e12)
