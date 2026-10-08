# 行动研究：一边改进真实组织，一边研究

本文讲**行动研究**（action research）：研究者和一个真实组织合作，亲自参与一项改变（例如和一个开发团队一起引入代码评审流程），一边推动改进，一边系统地研究这项改变带来了什么。

如果你只观察、不干预，那是[案例研究](case_study.md)；如果你的贡献是一个新工具或新技术本身，见[工程研究](../07_fields/computer-science/practices/engineering_research.md)。

**适用范围** `[本项目分析]`：本文资料来自软件工程和信息系统领域，依据是 ACM SIGSOFT 实证研究标准中的行动研究标准、Staron 的软件工程行动研究指南（其中转述了 Davison 等人的原则），以及 dos Santos 和 Travassos 的软件工程行动研究报告。其他计算机方向，只要研究的是"在某个团队或组织里推行一项改变"（例如在运维团队推行新的故障复盘制度、在实验室推行新的数据管理规范），可以直接参考。其他学科做行动研究时，先看本学科的规范，因为同一个名字的含义可能不同。例如教育学的行动研究里，教育者既是研究者又是教师[^anderson2012design-e4]，通常由教师自己完成[^anderson2012design-e5]，见[教育学学科概况](../07_fields/education/README.md#本学科常用的研究方法)；本文这种"研究者和实践者组队、在真实环境里推动改变"的做法，在教育学里更接近[基于设计的研究](../07_fields/education/practices/design_based_research.md)。

**常服务的套路**：[构建改进](../05_research-strategies/build_improve.md)（在真实组织里引入一项改进）、[观察描述](../05_research-strategies/observe_describe.md)（看真实环境里的人怎么反应）。

**读完本文，你应该能：**

- 判断自己的项目是行动研究、案例研究，还是"经验报告"；
- 和合作组织谈好协议，按"诊断—计划—行动—评估—反思"的循环推进；
- 设计能说明干预效果的数据收集，处理好研究者的双重角色；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

行动研究研究的是**一项干预（例如引入某种方法或工具）如何影响真实环境**[^ralph2020empirical-e330]。研究者和参与者以合作的方式共同解决问题[^santos2011action-e1]。它针对的难题是：**如何一边引入新做法，一边研究它**[^staron2025guidelines-e1]。

**和相近方法的区别**：

| | 行动研究 | 案例研究 | 实验 | 工程研究 |
|---|---|---|---|---|
| 研究者干预吗 | 干预，改变和观察是研究的核心[^ralph2020empirical-e331] | 不干预，是观察者或参与者[^staron2025guidelines-e2] | 干预，但要求可控，偏向孤立的小问题[^staron2025guidelines-e2] | 提出并评估一个技术制品 |
| 适合的问题 | 改变工作方式、流程、文化等社会层面的干预[^ralph2020empirical-e332] | 理解真实环境中的现象 | 检验假设 | 新工具或新技术本身，尤其缺少社会层面的[^ralph2020empirical-e332] |

如果研究既造了一个新工具、又在组织里推动了带社会层面的改变，两种标准都要参考[^ralph2020empirical-e332]。行动研究和案例研究有时不好分，尤其某些阶段观察多于行动的时候[^santos2011action-e8]。一个简单的判断：**研究者是否参与决定并推动了这项改变**。`[本项目分析]`

**行动研究不是咨询，也不是经验报告。** 它与日常改进工作的区别在于，它由理论和研究方法主动驱动[^santos2011action-e7]。研究开始前就要把标准写明，否则最后描述的可能只是"行动而不是研究"[^santos2011action-e5]。反过来，系统的观察和反思也不应被贬为咨询；咨询或经验也不应冒充行动研究[^ralph2020empirical-e342]。

**什么时候不该做**[^staron2025guidelines-e9]：

- 进不了组织，团队里也没有组织的人；
- 你不能长期投入；
- 你只想发论文，并不能为对方的实践做出贡献。

条件不具备时要准备换方法；多数情况下，先做一个案例研究熟悉组织，是更好的起点[^staron2025guidelines-e10]。

---

## 2. 怎么做

下面用一个例子贯穿：**你和一家公司的开发团队合作，引入代码评审流程，并评估效果。** `[本项目分析]`

### 第 0 步：谈好合作协议，组好团队

行动研究需要一份协议，明确双方的行动和各自能得到什么[^santos2011action-e3]。按 Davison 等人提出的原则（Staron 转述），要确认这几件事[^staron2025guidelines-e3]：

- 双方都同意行动研究适合这个情况，组织明确承诺参与；
- 双方的角色和职责；
- 项目目标和**评估指标**；
- 数据收集和分析方法。

双方还要摊开说清期望：研究者想得到什么成果、要发表什么、投入多少时间；组织能给多少资源、能否真的实施干预[^staron2025guidelines-e10]。发表前的审查和保密要求也要谈好 `[本项目分析]`。

**找谁谈**：等级制的组织先找管理层，自主型的组织先找团队[^staron2025guidelines-e11]。**团队里要有两种人**：至少有几位有研究学位的人，和至少几位来自该组织的从业者[^staron2025guidelines-e8]。

**为什么**：协议也决定了研究何时结束：双方都对结果满意时[^santos2011action-e3]。论文里要说明研究者和组织的关系，例如项目经费、潜在利益冲突、靠什么关系获得了进入机会[^ralph2020empirical-e333]。

### 循环：诊断、计划、行动、评估、反思

行动研究按循环推进。常见的描述是五阶段循环[^santos2011action-e2][^staron2025guidelines-e6]，阶段数也可以不同[^staron2025guidelines-e6]；每个循环建立在上一个循环的基础上[^ralph2020empirical-e335]。各阶段之间也可以回退，例如问题描述不清、计划做不下去时，可以回到诊断[^santos2011action-e4]。

**1. 诊断**：全面了解情况、利益相关者和他们的期望[^santos2011action-e2]，找出问题和可能的原因。研究者要**独立诊断**组织状况[^staron2025guidelines-e4]。

> 例：访谈团队成员、查看缺陷记录，发现很多缺陷是合并后才发现的，原因之一是没人看别人的代码。`[本项目分析]`

**2. 计划**：针对诊断出的原因设计干预[^staron2025guidelines-e17]，并事先写明所依据的理论，之后用它来解释结果[^staron2025guidelines-e22]。这一步要事先定好：

- **怎样算成功、怎样算失败，什么时候停**[^staron2025guidelines-e14]；
- **基线**：每次干预都要和基线比较[^staron2025guidelines-e14]。要验证引入代码评审的效果，就要在引入**之前**测量评审的速度、时长和次数[^staron2025guidelines-e15]；
- **收集哪些数据**。事先定好，意外发生时你才能专注于监控行动[^santos2011action-e10]；
- 每个循环的干预要**小而单一**。同时发生的其他变化会成为混杂因素（同时影响结果、让你误判原因的因素），让你分不清效果来自干预还是别的变化[^staron2025guidelines-e13]；
- 计划要经组织批准再实施[^staron2025guidelines-e4]。

**3. 行动**：实施干预。实施的人应是有能力在自己职责范围内做出这项改变的团队成员；在现有工作之外做个演示原型，不算行动研究[^staron2025guidelines-e13]。

- 计划外的事一定会发生。把它们记下来，以便之后说明理由[^santos2011action-e10]；
- 留意重组、新成员加入、产品变化等可能影响结果的事件[^staron2025guidelines-e16]；
- 尽量用自动化方式收集数据，例如录音，给自己腾出时间参与干预[^santos2011action-e11]。

**4. 评估**：同时看定量和定性两方面的效果[^staron2025guidelines-e12][^ralph2020empirical-e334]：

- 定量：和基线比较，例如评审耗时、合并后发现的缺陷数[^staron2025guidelines-e12]；`[本项目分析：具体指标]`
- 定性：访谈、研讨会、事后复盘[^staron2025guidelines-e12]；
- 报告参与者和利益相关者对干预的反应[^ralph2020empirical-e336]，但**不能只报告参与者怎么看**，要有系统评估，不回避问题[^ralph2020empirical-e341]；
- 干预前收集数据时，要准备应对霍桑效应：人们知道自己被观察时会改变行为[^staron2025guidelines-e15]。

**5. 反思**：和参与者一起总结学到了什么，并在组织内传播[^santos2011action-e2]。然后**明确决定**是否再走一个循环[^staron2025guidelines-e4]，必要时调整理论、范围、团队或干预本身[^staron2025guidelines-e17]。整个研究可能两三个循环就结束，也可能十个以上[^staron2025guidelines-e19]。

**干预失败了也有价值。** 报告干预的负面结果、分析某方法为什么不适用，是可以接受的[^ralph2020empirical-e340]；负面或不确定的结果对研究界也有价值[^staron2025guidelines-e18]。

---

## 3. 研究者的双重角色

做行动研究时，你往往既是研究者，又是推动改变的人，甚至就是团队成员[^santos2011action-e9]。这带来两个风险：失去距离，只看到自己想看的；以及推销自己带来的方法。ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准（下称 SIGSOFT 标准）把"失去职业距离和公正""不顾参与者的问题和价值观推销某个工具或方法"列为反面模式[^ralph2020empirical-e341]。

> **不同的看法：研究者应该嵌入组织多深？**
> - Staron 认为，在软件工程中研究必须嵌入组织内部，否则改变往往会被放弃[^staron2025guidelines-e5]。嵌入指研究者要么受雇于该组织，要么拥有和员工一样的访问权限[^staron2025guidelines-e7]。
> - SIGSOFT 标准则提醒，与研究对象过度融为一体、失去距离和公正，是反面模式[^ralph2020empirical-e341]。
>
> 两者并不矛盾：嵌入是为了让改变真正落地，距离是为了让评估可信。实际操作中，可以深度参与干预，同时用下面的办法保住评估的公正 `[本项目分析]`。

**怎样减轻偏见**：

- **事先写定理论、评估指标和成功标准**，再用它们解释结果，减少过度解读[^staron2025guidelines-e22][^staron2025guidelines-e14]。严谨的行动研究既要有一定的控制，减少研究者偏见和其他因素的影响，也要让所依据的理论始终明确[^santos2011action-e15]；
- **反思自己的偏见**，这是必须做到的[^ralph2020empirical-e336]，包括反思你对某些参与者可能造成的负面影响[^ralph2020empirical-e344]；
- **请别人来看**：参与者核验（请参与者确认你对他们说法和经历的理解）、请没参与的从业者提意见、请导师或同行审查编码[^ralph2020empirical-e337]；最好由多名研究者相互印证[^ralph2020empirical-e338]；
- **定量和定性数据相互印证**[^ralph2020empirical-e337]。

---

## 4. 结论能推广到哪里

SIGSOFT 标准认为，"只研究了一个组织，结论不能推广"是对行动研究**不成立**的批评[^ralph2020empirical-e343]。行动研究的评价标准例如反思性、可信度、共鸣、有用性和可迁移性；内部效度、构念效度、可推广性、信度这类实证主义的标准通常不适用[^ralph2020empirical-e339]。可迁移性指结果在多大程度上可能适用于其他地点、人群或情境[^ralph2020empirical-e344]。

但反过来，**你自己也不要过快推广**：在一个组织有效，不代表在另一个组织也有效[^staron2025guidelines-e22]。行动研究产出的理论往往是直接来自观察的具体关系，或者有一定抽象、但仍紧扣观察的"中层理论"[^santos2011action-e14]。所以：

- **详细描述情境**，包括采取了哪些干预[^staron2025guidelines-e20]，例如组织类型、团队规模、项目背景 `[本项目分析]`。如果只能在公开组织名称和公开组织特征之间二选一，特征对读者更有用[^staron2025guidelines-e20]；
- **讲清过程**：行动研究达不到自然科学那样的可重复性，但要讲清你得出结论所依据的过程[^santos2011action-e6]。

效度的一般讨论见[效度与局限](../02_from-project-to-study/03_validity-and-limits.md)。

---

## 5. 伦理

行动研究是在真实环境中的合作研究，伦理问题更加重要[^santos2011action-e13]：

- **自愿很难真正做到**：研究活动和本职工作重叠，参与者会觉得不得不参加。可以承诺不发表个人数据[^santos2011action-e13]。
- **敏感信息**：你会接触到私人对话、邮件、含敏感信息的提交记录。传播之前咨询组织的管理层和法务；在更大范围展示时，去掉个人和团队的身份信息[^staron2025guidelines-e21]。
- **不伤害组织**：干预如果造成伤害，要随时准备停止[^staron2025guidelines-e18]；要像员工一样遵守组织的规定[^staron2025guidelines-e11]。
- **不为了论文牺牲问题本身**：协议的目标始终是解决真实问题[^santos2011action-e12]。
- 不要强推参与者或组织不能接受的干预[^ralph2020empirical-e341]。

研究伦理的一般原则见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)。所有研究都必须承认并减轻研究可能带来的风险和伤害[^ralph2020empirical-e65]。

---

## 6. 检查清单

下面依据 SIGSOFT 的行动研究标准，它是软件工程领域的审稿标准；其他学科以本学科的规范为准 `[本项目分析]`。

**必须做到**

- [ ] 说明为什么选这个组织，并详细描述它[^ralph2020empirical-e333]
- [ ] 说明研究者和组织的关系（经费、利益冲突、如何获得进入机会）[^ralph2020empirical-e333]
- [ ] 详细描述干预，说明干预由谁决定、如何评估[^ralph2020empirical-e334]
- [ ] 说明研究持续多久，谁实施了干预、和组织的哪一部分合作[^ralph2020empirical-e335]
- [ ] 说明研究的循环或阶段，以及它们和干预的关系[^ralph2020empirical-e335]
- [ ] 给出从观察到结论的清楚证据链[^ralph2020empirical-e336]
- [ ] 报告参与者和利益相关者对干预的反应，以及组织学到了什么[^ralph2020empirical-e336]
- [ ] 反思研究者自己可能的偏见[^ralph2020empirical-e336]

**做到更好**

- [ ] 大量使用直接引语，提供访谈提纲、编码方案等补充材料[^ralph2020empirical-e337]
- [ ] 用参与者核验、同行审查编码等方式检验结果[^ralph2020empirical-e337]
- [ ] 结论可能迁移到其他情境[^ralph2020empirical-e337]
- [ ] 定量和定性数据相互印证[^ralph2020empirical-e337]

**做得出色**

- [ ] 由多名研究者组成团队，相互印证，减轻研究者偏见[^ralph2020empirical-e338]

**这些情况可以不做，不算缺陷**[^ralph2020empirical-e340]

- 为保护参与者，省略详细情况和直接引语
- 干预失败了：报告负面结果并分析原因

**审稿时常见、但不成立的批评**（SIGSOFT 标准列出的，针对软件工程的投稿）[^ralph2020empirical-e342][^ralph2020empirical-e343]：你不必为此担心

- "研究者干预了环境，所以结论无效"——引入改变并观察反应，正是行动研究的意义所在
- "这只是咨询或经验报告"（前提是你做了系统的观察和反思）
- "只研究了一个组织""样本不具代表性""不能推广"
- "没有对照组"——行动研究不是实验

---

## 7. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 把一次咨询或改进项目事后写成行动研究 | 没有事先写明的标准，就只是"行动而不是研究"[^santos2011action-e5][^ralph2020empirical-e342] |
| 没有基线就开始干预 | 无法判断是否改进了[^staron2025guidelines-e14] |
| 只报告参与者喜不喜欢新流程 | 缺少系统评估，回避了问题[^ralph2020empirical-e341] |
| 推销自己带来的工具或方法 | 不顾参与者的问题和价值观[^ralph2020empirical-e341] |
| 强推组织不接受的干预 | 违背合作原则[^ralph2020empirical-e341] |
| 干预又大又长 | 容易被打断，分不清效果来自哪里[^staron2025guidelines-e13] |
| 不记录重组、人员变动等意外事件 | 这些事件可能才是结果的原因[^staron2025guidelines-e16][^santos2011action-e10] |
| 在一个组织见效就宣称"普遍有效" | 过度推广[^staron2025guidelines-e22] |
| 用组织名称代替情境描述 | 读者无法判断结果是否适用于自己的情况[^staron2025guidelines-e20] |

---

## 8. 延伸阅读

- **审稿标准**：SIGSOFT 实证研究标准中的行动研究标准，附有推荐读物和范例论文。
- **具体操作指南**：Staron 2025 给出了 20 条指南，覆盖项目准备、组织环境、干预设计、报告和伦理，并转述了 Davison 等人 2004 的典范行动研究原则和检查项。作者也承认这些指南尚未在工业行动研究中验证[^staron2025guidelines-e23]。
- **完整的研究实例**：dos Santos & Travassos 2011 按五阶段完整报告了一项重构研究，并给出行动研究报告模板（§5.2.3）。他们对已有文献的调查发现，软件工程中行动研究的严谨性还需要提高[^santos2011action-e16]。
- **专著**：Staron 2020 *Action Research in Software Engineering: Theory and Applications*（Springer）。该书不是开放获取，本项目没有读到全文。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e330]: SIGSOFT 行动研究标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e330)
[^ralph2020empirical-e331]: SIGSOFT 行动研究标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e331)
[^ralph2020empirical-e332]: SIGSOFT 行动研究标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e332)
[^ralph2020empirical-e333]: SIGSOFT 行动研究标准，必要项及脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e333)
[^ralph2020empirical-e334]: SIGSOFT 行动研究标准，必要项及脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e334)
[^ralph2020empirical-e335]: SIGSOFT 行动研究标准，必要项及脚注 3、4。[证据](../../sources/notes/ralph2020empirical.md#e335)
[^ralph2020empirical-e336]: SIGSOFT 行动研究标准，必要项（结果与讨论）。[证据](../../sources/notes/ralph2020empirical.md#e336)
[^ralph2020empirical-e337]: SIGSOFT 行动研究标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e337)
[^ralph2020empirical-e338]: SIGSOFT 行动研究标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e338)
[^ralph2020empirical-e339]: SIGSOFT 行动研究标准，质量标准。[证据](../../sources/notes/ralph2020empirical.md#e339)
[^ralph2020empirical-e340]: SIGSOFT 行动研究标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e340)
[^ralph2020empirical-e341]: SIGSOFT 行动研究标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e341)
[^ralph2020empirical-e342]: SIGSOFT 行动研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e342)
[^ralph2020empirical-e343]: SIGSOFT 行动研究标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e343)
[^ralph2020empirical-e344]: SIGSOFT 标准术语表，Reflexivity、Transferability。[证据](../../sources/notes/ralph2020empirical.md#e344)
[^ralph2020empirical-e65]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e65)
[^staron2025guidelines-e1]: Staron 2025，§1。[证据](../../sources/notes/staron2025guidelines.md#e1)
[^staron2025guidelines-e2]: Staron 2025，§1。[证据](../../sources/notes/staron2025guidelines.md#e2)
[^staron2025guidelines-e3]: Staron 2025，§2.2，转述 Davison 等人 2004。[证据](../../sources/notes/staron2025guidelines.md#e3)
[^staron2025guidelines-e4]: Staron 2025，§2.2，转述 Davison 等人 2004。[证据](../../sources/notes/staron2025guidelines.md#e4)
[^staron2025guidelines-e5]: Staron 2025，§2.2。[证据](../../sources/notes/staron2025guidelines.md#e5)
[^staron2025guidelines-e6]: Staron 2025，§2.1 与图 2。[证据](../../sources/notes/staron2025guidelines.md#e6)
[^staron2025guidelines-e7]: Staron 2025，§3。[证据](../../sources/notes/staron2025guidelines.md#e7)
[^staron2025guidelines-e8]: Staron 2025，§3.1。[证据](../../sources/notes/staron2025guidelines.md#e8)
[^staron2025guidelines-e9]: Staron 2025，§3.2。[证据](../../sources/notes/staron2025guidelines.md#e9)
[^staron2025guidelines-e10]: Staron 2025，§4.1，指南 2、3。[证据](../../sources/notes/staron2025guidelines.md#e10)
[^staron2025guidelines-e11]: Staron 2025，§4.2，指南 5、6。[证据](../../sources/notes/staron2025guidelines.md#e11)
[^staron2025guidelines-e12]: Staron 2025，§4.3，指南 7。[证据](../../sources/notes/staron2025guidelines.md#e12)
[^staron2025guidelines-e13]: Staron 2025，§4.3，指南 8、9。[证据](../../sources/notes/staron2025guidelines.md#e13)
[^staron2025guidelines-e14]: Staron 2025，§4.4，指南 10、11。[证据](../../sources/notes/staron2025guidelines.md#e14)
[^staron2025guidelines-e15]: Staron 2025，§4.4。[证据](../../sources/notes/staron2025guidelines.md#e15)
[^staron2025guidelines-e16]: Staron 2025，§4.4，指南 12。[证据](../../sources/notes/staron2025guidelines.md#e16)
[^staron2025guidelines-e17]: Staron 2025，§4.4，指南 13。[证据](../../sources/notes/staron2025guidelines.md#e17)
[^staron2025guidelines-e18]: Staron 2025，§4.4，指南 14。[证据](../../sources/notes/staron2025guidelines.md#e18)
[^staron2025guidelines-e19]: Staron 2025，§4.4，指南 15。[证据](../../sources/notes/staron2025guidelines.md#e19)
[^staron2025guidelines-e20]: Staron 2025，§4.5，指南 18。[证据](../../sources/notes/staron2025guidelines.md#e20)
[^staron2025guidelines-e21]: Staron 2025，§4.6。[证据](../../sources/notes/staron2025guidelines.md#e21)
[^staron2025guidelines-e22]: Staron 2025，§4.6，指南 19、20。[证据](../../sources/notes/staron2025guidelines.md#e22)
[^staron2025guidelines-e23]: Staron 2025，§5。[证据](../../sources/notes/staron2025guidelines.md#e23)
[^santos2011action-e1]: dos Santos & Travassos 2011，§2.2。[证据](../../sources/notes/santos2011action.md#e1)
[^santos2011action-e2]: dos Santos & Travassos 2011，§2.2。[证据](../../sources/notes/santos2011action.md#e2)
[^santos2011action-e3]: dos Santos & Travassos 2011，§2.2。[证据](../../sources/notes/santos2011action.md#e3)
[^santos2011action-e4]: dos Santos & Travassos 2011，§2.2。[证据](../../sources/notes/santos2011action.md#e4)
[^santos2011action-e5]: dos Santos & Travassos 2011，§2.2。[证据](../../sources/notes/santos2011action.md#e5)
[^santos2011action-e6]: dos Santos & Travassos 2011，§2.2。[证据](../../sources/notes/santos2011action.md#e6)
[^santos2011action-e7]: dos Santos & Travassos 2011，§2.2.1。[证据](../../sources/notes/santos2011action.md#e7)
[^santos2011action-e8]: dos Santos & Travassos 2011，§5.1.1。[证据](../../sources/notes/santos2011action.md#e8)
[^santos2011action-e9]: dos Santos & Travassos 2011，§5.1.1。[证据](../../sources/notes/santos2011action.md#e9)
[^santos2011action-e10]: dos Santos & Travassos 2011，§5.1.1。[证据](../../sources/notes/santos2011action.md#e10)
[^santos2011action-e11]: dos Santos & Travassos 2011，§5.1.1。[证据](../../sources/notes/santos2011action.md#e11)
[^santos2011action-e12]: dos Santos & Travassos 2011，§5.1.3。[证据](../../sources/notes/santos2011action.md#e12)
[^santos2011action-e13]: dos Santos & Travassos 2011，§5.1.3。[证据](../../sources/notes/santos2011action.md#e13)
[^santos2011action-e14]: dos Santos & Travassos 2011，§5.2.1。[证据](../../sources/notes/santos2011action.md#e14)
[^santos2011action-e15]: dos Santos & Travassos 2011，§5.2.2。[证据](../../sources/notes/santos2011action.md#e15)
[^santos2011action-e16]: dos Santos & Travassos 2011，摘要。[证据](../../sources/notes/santos2011action.md#e16)
[^anderson2012design-e4]: Anderson & Shattuck 2012，collaborative partnership。[证据](../../sources/notes/anderson2012design.md#e4)
[^anderson2012design-e5]: Anderson & Shattuck 2012，Comparison to Action Research。[证据](../../sources/notes/anderson2012design.md#e5)
