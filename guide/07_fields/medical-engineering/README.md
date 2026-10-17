# 医学工程：学科概况

本文讲医学工程（也叫生物医学工程）的研究实际怎样运转：做器械、做算法，从台架试验一路走到动物实验和人体研究；做出来的东西将来可能成为医疗器械，所以研究阶段就要想到设计文档、法规和伦理。人体研究和动物研究的规则分别见[临床医学篇](../clinical-medicine/README.md)和[生物科学篇](../biological-sciences/README.md)；各学科都适用的做法见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)。这里只写本学科特有的东西。常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)；具体做法见文末的[本学科常用的研究方法](#本学科常用的研究方法)。

**读完本文，你应该能：**

- 说清一个器械或算法从想法到用在病人身上，大致要经过哪些阶段；
- 知道"研究原型"和"可以上市的产品"差在哪里，以及美国"设计控制"的思路要你留下哪些记录（旧条文已被替代，见下文）；
- 知道计算模型怎样才算"可信"，用到机器学习时该找哪份报告规范；
- 分清工程期刊和医学期刊的不同规矩。

---

## 本领域研究怎样运转

### 从想法到病人：一条很长的链

一个器械或算法要用到病人身上，大致要经过这样几步 `[本项目分析]`：

1. **概念和可行性原型**：先做一个粗糙的原型，看想法行不行；
2. **台架试验**：在实验台上测性能。按美国食品药品监督管理局（Food and Drug Administration，FDA）的用法，"台架试验"是个宽泛的说法，包括体外试验、尸体试验和其他非临床试验[^fda2023cmscredibility-e11]；
3. **计算建模与仿真**：在计算机上模拟器械和人体，见下文"计算模型怎样才算可信"；
4. **动物实验**；
5. **首次人体试验和临床研究**。

这些步骤不一定按顺序走完，常常要来回 `[本项目分析]`。美国 FDA 1997 年的《设计控制指南》（已撤回，见下文"设计控制"一节）也说过：实际开发中，各阶段和前面的阶段之间都要有反馈，产品开发是迭代的[^fda1997designcontrol-e6]。一篇论文可以只覆盖其中一段 `[本项目分析]`。以《IEEE 生物医学工程汇刊》（IEEE Transactions on Biomedical Engineering，TBME）这一本期刊为例，它收的论文从方法和技术开发，到有工程贡献的实验研究和临床研究都有[^embstbmeprepare-e1]。

### 工程师和医生一起做

器械研究可能需要工程师和医生合作：医生知道临床上缺什么，工程师知道怎样做出来 `[本项目分析]`。合作中容易出现的问题是"说的不是一回事" `[本项目分析]`。上面那份已撤回的 1997 年指南给过一个建议：开发和审查的人都熟悉医学术语时，需求里可以用医学术语；但在需求阶段把概念翻译成工程语言，往往更能减少误解[^fda1997designcontrol-e4]。它还提醒：再简单的说法也可能牵出大量设计问题，所以一份概念说明可以是开发的起点，但不等于设计要求[^fda1997designcontrol-e3]。

美国生物医学工程学会（Biomedical Engineering Society，BMES）的伦理准则也要求：超出自己专长时，请合作者或顾问把关[^bmes2021ethics-e4]。

### 研究原型不等于产品

那份 1997 年指南承认，研究和开发的界线不好划。在写正式的设计要求之前，先做一个快速原型探索想法是否可行，是合理的；但不要把原型设计当成成品设计[^fda1997designcontrol-e1]。原因是：这个阶段的原型缺少成品必需的安全功能和辅助功能，也没法充分考虑批量制造带来的差异[^fda1997designcontrol-e2]。

对研究者的意思是：论文里的原型性能好，不代表离临床使用很近；写论文和对外介绍时，要说清楚它还处在哪个阶段 `[本项目分析]`。BMES 准则要求对媒体和公众讲话要严格诚实，讲清结论有多大把握，避免给人虚假的治疗希望[^bmes2021ethics-e11]。

### 发表：工程期刊和医学期刊两套习惯

本领域的论文既投工程期刊，也投医学期刊 `[本项目分析]`。两边的规矩不一样，投稿前先看清目标期刊的要求。

**工程期刊，以 TBME 为例。** 下面是 TBME 投稿说明页的规定（读取的是 2025 年 1 月的网页存档，之后可能有更新）。这些只是 TBME 一本期刊的要求，其他工程期刊以各自的作者须知为准 `[本项目分析]`：

- 摘要要结构化，不超过 250 词，写清目的、方法、结果、结论和意义五点；缺了任何一点，稿件可能不经审稿就被退回[^embstbmeprepare-e2]。
- 投稿信必须披露相关的已发表会议论文，并说明为什么它们和这次投稿是不同的工作[^embstbmeprepare-e3]。只以会议摘要形式出现过的工作可以写成全文投稿；但已经发表过内容充分的会议长文，可能就失去投稿资格[^embstbmeprepare-e4]。IEEE 的出版规则则认可"会议版可以发展成期刊版"[^ieee2026pspb-e4]，TBME 这一条比它更严，所以要先查具体期刊 `[本项目分析]`（IEEE 的一般规则见[电子信息篇](../electrical-engineering/README.md#发表以-ieee-为例会议版可以发展成期刊版)）。
- 每篇文章至少两位独立审稿人，单盲审稿（审稿人知道作者是谁，作者不知道审稿人）[^embstbmeprepare-e6]；页面当时写的投稿到决定时间约 30 天[^embstbmeprepare-e5]。
- 一稿多投被发现，IEEE 医学与生物学工程学会（Engineering in Medicine and Biology Society，EMBS，TBME 的主办学会）会处罚作者[^embstbmeprepare-e7]。

**医学期刊。** 投稿前先看目标期刊是否采用国际医学期刊编辑委员会（ICMJE）的建议。ICMJE 关于署名、利益冲突、数据共享声明、报告规范的规定，详见[临床医学篇](../clinical-medicine/README.md#本领域的规范和报告标准)。和本领域最相关的一条是：ICMJE 所说的"健康相关干预"明确包括器械[^icmje2026recommendations-e17]，而 ICMJE 建议医学期刊把"在第一位病人签署入组同意时或之前公开登记"作为考虑发表的前提[^icmje2026recommendations-e15]。所以做器械的临床试验，也要提前登记 `[本项目分析]`。

**署名。** IEEE 的署名条件把"原型开发"明确列为可以构成署名资格的智力贡献之一[^ieee2026pspb-e6]。投 ICMJE 体系的医学期刊时，按 ICMJE 的四条标准判断，见[临床医学篇](../clinical-medicine/README.md#署名icmje-的四条标准)。

---

## 和其他领域不同的地方

下表是本项目的归纳，用来帮你快速定位差别 `[本项目分析]`。

| | 医学工程 | 计算机领域 | 临床医学 |
|---|---|---|---|
| 结果从哪来 | 原型、台架试验、仿真、动物实验、人体研究，常常几样组合 | 以代码、系统和数据上的实验为主 | 以人体研究为主 |
| 文档要求 | 可能成为医疗器械的项目，要留下设计和测试记录（美国的规定见下文） | 计算机篇未涉及 | 研究方案、登记、伦理审批 |
| 发表 | 工程期刊和医学期刊都投，两边规则不同 | 多数方向以顶级会议为主（见[计算机篇](../computer-science/README.md#会议是主要的发表渠道)） | 以期刊为主 |
| 伦理 | 工程背景的研究者可能要第一次面对人体和动物研究的审批 | 有人参与的实验要过伦理审查 | 伦理审查是第一道关 |

---

## 本领域的规范和报告标准

### 当研究可能变成医疗器械：设计控制（美国的规则）

**下面讲的都是美国的规定。** 中国、欧盟等地区的医疗器械法规不同，你所在单位也可能有自己的要求，以本地法规和单位规定为准 `[本项目分析]`。BMES 准则也把"弄懂本地法规"写成研究者自己的责任[^bmes2021ethics-e2]。

**先说清楚：下文引用的旧条文和旧指南都已不再有效。**

- 美国《联邦法规汇编》第 21 编第 820 部分的现行版本（本文 2026 年 10 月读取）里，原来讲"设计控制"的第 820.30 节已经删去，只标"保留"[^cfr2026qmsr-e1]。
- 现行规定是：II 类、III 类和部分 I 类器械的制造商，设计和开发要遵守国际标准 ISO 13485 的第 7.3 条[^cfr2026qmsr-e2]。ISO 13485:2016 是医疗器械质量管理体系的国际标准，由国际标准化组织（ISO）制定，被新法规引用为法规内容[^aabb2026qmsr-e1]；要从 ISO 获取[^cfr2026qmsr-e3]。
- 解释旧条文的 FDA 1997 年《设计控制指南》也已撤回[^fda2026withdrawn-e2]。

本文仍引用旧条文和旧指南，只是因为它们可以免费读到，又把设计控制的思路讲得清楚。**它们不是现行要求**；正式做法以现行法规和 ISO 13485 为准 `[本项目分析]`。

**旧条文讲了什么（仅供理解思路）。** 旧版第 820.30 节（2023 年 4 月 1 日版）当时要求 III 类、II 类和部分 I 类器械的制造商控制器械的设计过程[^cfr2023designcontrols-e1]。它的几个环节，可以当作研究阶段"该留下什么记录"的参考清单 `[本项目分析]`：

- **设计输入**：写清设计要求，覆盖预期用途、使用者和病人的需要[^cfr2023designcontrols-e2]。
- **设计评审**：每次评审要有相关各方的代表，还要有一位不直接负责这一阶段的人[^cfr2023designcontrols-e3]。
- **设计验证**（verification）：确认设计输出满足设计输入，回答"东西是不是按要求做出来了"[^cfr2023designcontrols-e4]。旧指南说，手段是测试、检查和分析[^fda1997designcontrol-e9]。
- **设计确认**（validation）：确保器械符合用户需要和预期用途，要在实际或模拟使用条件下测试生产出来的器械[^cfr2023designcontrols-e5]，回答"做出来的东西是不是用户真正需要的"。旧指南说，确认包含验证，又比验证多走一步[^fda1997designcontrol-e7]。
- **设计变更**：改设计之前要记录、评审、批准[^cfr2023designcontrols-e6]。
- **设计历史文件**：把这些记录收在一起，证明设计是按批准的计划完成的[^cfr2023designcontrols-e7]。

**对研究生意味着什么。** 现行美国法规约束的是器械"制造商"[^cfr2026qmsr-e4]。研究阶段要不要遵守，FDA 在 1996 年发布旧法规时写过一句说明：设计控制不打算用于概念开发和可行性研究；但一旦决定要开发某个设计，就必须先定计划，确保最终投产的设计满足批准的要求[^fda1996qsr-e1]。这是对旧法规的说明；FDA 2024 年发布新法规时说，新旧法规大体相似[^fda2024qmsr-e3]。另外，器械要拿到人身上做临床研究时，美国用"研究用器械豁免"（Investigational Device Exemption，IDE，见下一节）免掉一批上市前的要求，但现行条文写明，设计和开发要求（§820.10(c)，适用时）不在免除之列[^cfr2026ide-e7]。大学实验室的项目具体从哪一步起要遵守，以导师和本单位负责法规或技术转移的部门的意见为准。即使不受约束，有两件事值得从第一天就做 `[本项目分析]`：

1. **把需求写下来**：用户是谁、要解决什么临床问题、要达到什么指标。旧指南提醒，关键需求如果到确认阶段才发现，可能要付出昂贵的重新设计和返工[^fda1997designcontrol-e5]；如果预计要做临床试验，计划里还要留出相应的法规工作[^fda1997designcontrol-e8]。
2. **把过程记下来**：BMES 准则要求在研究和设计的全过程中保持细致、完整、准确的记录[^bmes2021ethics-e3]。记录方法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。

### 进入人体之前：研究用器械（美国 21 CFR 812）

**以下也是美国的规定，而且是现行的；在中国或其他国家做器械临床研究，以当地法规为准 `[本项目分析]`。** 美国《联邦法规汇编》第 21 编第 812 部分（21 CFR 812）规定了器械临床研究的程序[^cfr2026ide-e1]：凡是为了确定器械安全性和有效性的临床研究都适用，该部分列出的几类情况除外[^cfr2026ide-e2]。几个关键概念：

- **重大风险器械**：法规列了几类，总的意思是可能对受试者健康、安全或福祉造成严重风险的研究用器械[^cfr2026ide-e3]。不是重大风险器械的研究，要求之一是向机构审查委员会（Institutional Review Board，美国的伦理审查委员会）简要说明为什么它不是重大风险器械，并取得批准[^cfr2026ide-e4]。
- **申办者兼研究者**：自己发起、自己实施研究的人，要同时承担研究者和申办者两方面的义务[^cfr2026ide-e5]。大学里自己发起器械研究的研究者，可能就处在这个位置 `[本项目分析]`。
- **只用于实验动物研究**、并按规定贴了标签的器械，除个别条款外不适用第 812 部分[^cfr2026ide-e6]；动物实验本身的伦理要求另有规定，见下文。

### 计算模型怎样才算"可信"（美国 FDA 2023 年指南）

本领域常用计算模型：例如在计算机上评估植入式支架的耐久性[^fda2023cmscredibility-e3]，或用一批模拟病人（"虚拟队列"）做"计算机上的临床试验"[^fda2023cmscredibility-e4]。美国 FDA 2023 年的一份指南讲向 FDA 提交器械申请时，怎样证明这类模型可信。先说清两点：它对 FDA 和公众都没有约束力[^fda2023cmscredibility-e1]；它只管基于物理或机理的模型，不管机器学习等数据驱动的模型[^fda2023cmscredibility-e2]。

指南里几个概念，做研究时也用得上 `[本项目分析]`：

- **可信度是针对某个用途说的。** 可信度指对模型在某个"使用情境"下预测能力的信任[^fda2023cmscredibility-e5]；使用情境要说清模型在回答问题时具体起什么作用、管多大范围[^fda2023cmscredibility-e6]。同一个模型，换个用途就要重新论证 `[本项目分析]`。
- **风险越高，要的证据越多。** 模型需要多可信，取决于用它回答问题的风险；风险看两点：模型对决策影响多大、决策错了后果多严重[^fda2023cmscredibility-e7]。如果还有台架试验或动物试验结果一起回答同一个问题，模型的影响就会不同[^fda2023cmscredibility-e8]。
- **验证和确认是两回事。** 验证看求解数学模型的程序有没有写对[^fda2023cmscredibility-e9]；确认看模型在多大程度上准确反映真实世界[^fda2023cmscredibility-e13]。
- **校准不等于确认。** 用调参数的同一批数据去比较，不算确认证据，比确认证据弱[^fda2023cmscredibility-e10]。要留出独立的数据来检验 `[本项目分析]`。

### 用到机器学习：找对报告规范

上面的 FDA 指南不管机器学习模型[^fda2023cmscredibility-e2]。做临床预测模型（不管用回归还是机器学习），可以按 TRIPOD+AI 报告[^collins2024tripodai-e2]：它有一份 27 项的清单和一份 13 项的摘要清单[^collins2024tripodai-e1]。这篇 2024 年文章的表 1 还按研究类型列了其他报告规范，例如医学影像人工智能研究、人工智能决策支持系统的早期临床评估、含人工智能成分的临床试验报告，各有对应的规范，具体名称查原文表 1[^collins2024tripodai-e3]。

两点和计算机领域的习惯不同，要特别注意：

- **术语。** 在机器学习研究里，"验证数据"可能指调参用的数据，也可能指评估模型表现的数据[^collins2024tripodai-e6]。TRIPOD+AI 的作者认为不存在"已经验证好的预测模型"，文中把"验证"改称"评估"[^collins2024tripodai-e4]。
- **数据分开。** 评估数据要和训练、调参、选模型用的数据分开，两边不能有同一个受试者[^collins2024tripodai-e5]。同一个病人的多张图像分到训练集和测试集两边，就违反了这一条 `[本项目分析]`。

### 人和动物：伦理审查（详见其他篇）

涉及人的研究见[临床医学篇](../clinical-medicine/README.md#研究对象是人伦理排在第一位)和[研究涉及人时，先保护人](../../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)；涉及动物的研究见[生物科学篇](../biological-sciences/README.md#动物研究3r-原则和-arrive-报告规范)和[临床前动物研究](../../06_methods/preclinical_animal_study.md)。和本领域相关的一点：英国国家动物研究替代、优化与减少中心（NC3Rs）把数学和计算机模型列为"完全替代"动物的方法之一[^nc3rsthe3rs-e4]，这也是做好计算模型的一个价值 `[本项目分析]`。写进论文时按目标期刊要求说明伦理审批：例如 TBME 页面引用的是 2000 年修订的《赫尔辛基宣言》[^embstbmeprepare-e9]，而 ICMJE 要求符合 2024 年修订版[^icmje2026recommendations-e11]。

### 职业伦理：BMES 准则

BMES 准则不是法律，规定的是监管要求之外，生物医学工程师还应遵守的职业伦理[^bmes2021ethics-e1]。除上面已经提到的几条，和研究最相关的还有下面几条：

- **为尽可能广泛的人群设计**：考虑不同年龄、性别、体型、能力和生理特征[^bmes2021ethics-e8]。只用健康年轻志愿者测出的性能，未必适用于病人 `[本项目分析]`。
- **公开数据和方法**：项目结束后，在人体数据隐私限制之内尽量公开[^bmes2021ethics-e5]。
- **声明利益冲突**：经济上的和学术观点上的都要声明[^bmes2021ethics-e10]。本领域的成果可能涉及专利或创业公司 `[本项目分析]`；TBME 要求披露的利益就包括作者在可能授权、申请专利或使用这项成果的公司里的经济利益[^embstbmeprepare-e8]。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，按核心主张来定，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表只列本文资料能支持的几种。表的分组和"在医学工程里的样子"一栏是本项目的归纳；标准多出自美国的法规、指南和个别期刊，只代表脚注里的出处。观察描述、综合等套路在本学科怎样用，本文资料未涉及 `[本项目分析]`。

| 套路 | 在医学工程里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md)：器械和原型 | 提出新的器械、传感器或方法。TBME 收的论文就包括有生物医学应用的方法和技术开发[^embstbmeprepare-e1]；性能可以用台架试验来测，按 FDA 的用法它包括体外、尸体等非临床试验[^fda2023cmscredibility-e11] | 分清验证（输出满足设计输入）[^cfr2023designcontrols-e4]和确认（在实际或模拟使用条件下满足用户需要）[^cfr2023designcontrols-e5]；原型缺少成品必需的安全功能，不能当成品看[^fda1997designcontrol-e2] | [工程研究](../computer-science/practices/engineering_research.md)（计算机篇，可参考） |
| [构建改进](../../05_research-strategies/build_improve.md)：计算模型 | 在计算机上评估器械，例如植入式支架的耐久性[^fda2023cmscredibility-e3] | 按美国 FDA 2023 年指南：可信度针对具体的使用情境[^fda2023cmscredibility-e5]；风险越高要的证据越多[^fda2023cmscredibility-e7]；校准数据不算确认证据[^fda2023cmscredibility-e10] | [定量仿真](../../06_methods/simulation_study.md) |
| [构建改进](../../05_research-strategies/build_improve.md)：诊断或预测算法 | 开发或评估临床预测模型，不管用回归还是机器学习[^collins2024tripodai-e2] | 按 TRIPOD+AI 报告[^collins2024tripodai-e2]；评估数据和训练数据不能有同一个受试者[^collins2024tripodai-e5]；BMES 准则要求在实际用途上验证，讲清局限和数据来源[^bmes2021ethics-e9] | [数据科学研究](../../06_methods/data_science.md) |
| [解释因果](../../05_research-strategies/explain_causality.md)：器械的临床研究 | 检验器械用在病人身上是否安全有效。在美国，为确定器械安全性和有效性的临床研究适用 21 CFR 812[^cfr2026ide-e2] | 设计、实施、分析和报告都恰当的随机试验，一般被认为是评价医疗干预的最高质量证据[^hopewell2025consort-e2]；ICMJE 所说的干预包括器械[^icmje2026recommendations-e17]，它建议期刊把"在第一位病人签署入组同意时或之前登记"作为考虑发表的前提[^icmje2026recommendations-e15] | [随机对照试验](../../06_methods/randomized_controlled_trial.md)、[临床前动物研究](../../06_methods/preclinical_animal_study.md) |

怎么用这张表 `[本项目分析]`：

- **一个项目常常跨几行。** 例如先做原型和台架试验，再用计算模型补充，最后进入动物和人体研究。按这篇论文的核心主张定主要套路，并写清项目在"原型→台架→动物→人体"这条链上走到了哪一步。
- **同一套路，投工程期刊和投医学期刊，"够不够"可能不同。** 投稿前对照目标期刊的要求，见上文[发表：工程期刊和医学期刊两套习惯](#发表工程期刊和医学期刊两套习惯)。

## 本学科常用的研究方法

本学科没有单独的学科独有方法页。跨学科的研究方法里，常用的有[定量仿真](../../06_methods/simulation_study.md)、[数据科学研究](../../06_methods/data_science.md)、[对照实验](../../06_methods/controlled_experiment.md)、[随机对照试验](../../06_methods/randomized_controlled_trial.md)、[临床前动物研究](../../06_methods/preclinical_animal_study.md)；做新器械、新算法，可以参考计算机篇的[工程研究](../computer-science/practices/engineering_research.md)。下面只写额外要注意的地方：

- **台架试验**（没有单独文档）：测试条件要尽量接近实际使用，并写清装置 `[本项目分析]`。
- **对照实验**：比较不同设计对使用者（医生、护士、病人）的影响，例如可用性测试 `[本项目分析]`。用的是研究用器械，在美国还可能适用第 812 部分[^cfr2026ide-e2]。

---

## 给新手的建议

1. **先写需求，再做原型。** 和合作医生一起把"要解决什么临床问题、达到什么指标"写成工程语言[^fda1997designcontrol-e4]。
2. **从第一天起好好记录。** 设计决策、测试结果、改动原因都记下来[^bmes2021ethics-e3]；项目将来要转化时，这些记录会用上 `[本项目分析]`。
3. **涉及人或动物，先问伦理审查。** 器械研究还要问清本地关于研究用器械的规定；在美国要看第 812 部分[^cfr2026ide-e2]。
4. **对外介绍时，说清成果处在哪个阶段。** 别让一个台架原型听起来像马上能治病的产品[^bmes2021ethics-e11]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 把研究原型当成接近成品的东西来宣传 | 原型缺少成品必需的安全功能，也没法充分考虑批量制造的差异[^fda1997designcontrol-e2] |
| 需求只停留在一份笼统的概念说明 | 再简单的说法也可能牵出大量设计问题，概念说明不等于设计要求[^fda1997designcontrol-e3]；关键需求到后期才发现，返工代价大[^fda1997designcontrol-e5] |
| 只做了验证（规格达标），就说器械"满足临床需要" | 验证和确认是两回事；按美国旧条文的说法，确认要在实际或模拟使用条件下测试[^cfr2023designcontrols-e5] |
| 把 21 CFR 820.30 或 FDA 1997 年指南当成现行要求 | 前者已从现行法规中删去，设计和开发改按 ISO 13485 第 7.3 条[^cfr2026qmsr-e1][^cfr2026qmsr-e2]；后者 FDA 已撤回[^fda2026withdrawn-e2] |
| 同一个病人的数据同时出现在训练集和测试集 | 评估数据要和训练数据分开，不能有同一个受试者[^collins2024tripodai-e5] |
| 已发表过会议长文，再几乎原样投 TBME | TBME 可能因此不考虑这篇稿件[^embstbmeprepare-e4] |
| 器械临床试验开始后才登记 | ICMJE 建议期刊把"第一位病人签署入组同意时或之前登记"作为考虑发表的前提，器械也在干预范围内[^icmje2026recommendations-e15][^icmje2026recommendations-e17] |
| 不披露自己在相关公司的股份或专利 | TBME 要求披露这类经济利益[^embstbmeprepare-e8] |
| 把美国 FDA 的规定当成各国通用的规矩 | 本文引用的都是美国规定；BMES 准则要求弄懂本地法规[^bmes2021ethics-e2] |

---

## 延伸阅读

- **BMES Code of Ethics（2021）**：读完就知道这个职业对研究、数据、受试者、动物和公众有哪些期待。入门第一份。
- **美国 FDA，Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions（2023）**：做仿真或计算模型的人读。重点读第 IV 节（定义）和第 VI 节（使用情境、模型风险、证据类别）。
- **美国 FDA，Design Control Guidance for Medical Device Manufacturers（1997，已撤回）**：只作理解设计控制概念的历史资料；正式做法以现行法规和 ISO 13485 为准。
- **Collins 等人 2024，TRIPOD+AI**：开发或评估临床预测模型的人读；表 1 可以帮你找到其他人工智能相关的报告规范。
- **目标期刊的投稿须知**：例如 TBME 的投稿说明页；投医学期刊时读 ICMJE 建议（见[临床医学篇](../clinical-medicine/README.md)）。
- **你所在国家的医疗器械法规和本单位的说明**：本文引用的都是美国的规定，各国和各单位不同，以本地为准。

[^fda2023cmscredibility-e1]: FDA 2023，计算建模与仿真可信度指南，封面后说明。[证据](../../../sources/notes/fda2023cmscredibility.md#e1)
[^fda2023cmscredibility-e2]: FDA 2023，I. Introduction。[证据](../../../sources/notes/fda2023cmscredibility.md#e2)
[^fda2023cmscredibility-e3]: FDA 2023，II. Background。[证据](../../../sources/notes/fda2023cmscredibility.md#e3)
[^fda2023cmscredibility-e4]: FDA 2023，II. Background。[证据](../../../sources/notes/fda2023cmscredibility.md#e4)
[^fda2023cmscredibility-e5]: FDA 2023，IV. Definitions。[证据](../../../sources/notes/fda2023cmscredibility.md#e5)
[^fda2023cmscredibility-e6]: FDA 2023，IV. Definitions。[证据](../../../sources/notes/fda2023cmscredibility.md#e6)
[^fda2023cmscredibility-e7]: FDA 2023，VI.A.(3) Model risk。[证据](../../../sources/notes/fda2023cmscredibility.md#e7)
[^fda2023cmscredibility-e8]: FDA 2023，VI.A.(3) Model risk。[证据](../../../sources/notes/fda2023cmscredibility.md#e8)
[^fda2023cmscredibility-e9]: FDA 2023，VI.B Credibility evidence。[证据](../../../sources/notes/fda2023cmscredibility.md#e9)
[^fda2023cmscredibility-e10]: FDA 2023，VI.B (2) Model calibration evidence。[证据](../../../sources/notes/fda2023cmscredibility.md#e10)
[^fda2023cmscredibility-e11]: FDA 2023，VI.B (3) Bench test validation results。[证据](../../../sources/notes/fda2023cmscredibility.md#e11)
[^fda2023cmscredibility-e13]: FDA 2023，IV. Definitions。[证据](../../../sources/notes/fda2023cmscredibility.md#e13)
[^fda1997designcontrol-e1]: FDA 1997，设计控制指南（已撤回），Section C，Research and Development。[证据](../../../sources/notes/fda1997designcontrol.md#e1)
[^fda1997designcontrol-e2]: FDA 1997（已撤回），Section C，Research and Development。[证据](../../../sources/notes/fda1997designcontrol.md#e2)
[^fda1997designcontrol-e3]: FDA 1997（已撤回），Section C，Concept Documents versus Design Input。[证据](../../../sources/notes/fda1997designcontrol.md#e3)
[^fda1997designcontrol-e4]: FDA 1997（已撤回），Section C，Responsibility for Design Input Development。[证据](../../../sources/notes/fda1997designcontrol.md#e4)
[^fda1997designcontrol-e5]: FDA 1997（已撤回），Section C，开头讨论部分。[证据](../../../sources/notes/fda1997designcontrol.md#e5)
[^fda1997designcontrol-e6]: FDA 1997（已撤回），Introduction。[证据](../../../sources/notes/fda1997designcontrol.md#e6)
[^fda1997designcontrol-e7]: FDA 1997（已撤回），Introduction。[证据](../../../sources/notes/fda1997designcontrol.md#e7)
[^fda1997designcontrol-e8]: FDA 1997（已撤回），Section B。[证据](../../../sources/notes/fda1997designcontrol.md#e8)
[^fda1997designcontrol-e9]: FDA 1997（已撤回），Section F。[证据](../../../sources/notes/fda1997designcontrol.md#e9)
[^fda1996qsr-e1]: FDA 1996，质量体系法规最终规则公告（61 FR 52602），第 62 条意见的答复，52616 页。[证据](../../../sources/notes/fda1996qsr.md#e1)
[^cfr2023designcontrols-e1]: 21 CFR 820.30（2023 年 4 月 1 日版，现已删除），(a)。[证据](../../../sources/notes/cfr2023designcontrols.md#e1)
[^cfr2023designcontrols-e2]: 21 CFR 820.30（2023 年版，现已删除），(c)。[证据](../../../sources/notes/cfr2023designcontrols.md#e2)
[^cfr2023designcontrols-e3]: 21 CFR 820.30（2023 年版，现已删除），(e)。[证据](../../../sources/notes/cfr2023designcontrols.md#e3)
[^cfr2023designcontrols-e4]: 21 CFR 820.30（2023 年版，现已删除），(f)。[证据](../../../sources/notes/cfr2023designcontrols.md#e4)
[^cfr2023designcontrols-e5]: 21 CFR 820.30（2023 年版，现已删除），(g)。[证据](../../../sources/notes/cfr2023designcontrols.md#e5)
[^cfr2023designcontrols-e6]: 21 CFR 820.30（2023 年版，现已删除），(i)。[证据](../../../sources/notes/cfr2023designcontrols.md#e6)
[^cfr2023designcontrols-e7]: 21 CFR 820.30（2023 年版，现已删除），(j)。[证据](../../../sources/notes/cfr2023designcontrols.md#e7)
[^cfr2026qmsr-e1]: 21 CFR Part 820（现行版，eCFR），§§820.20–820.30。[证据](../../../sources/notes/cfr2026qmsr.md#e1)
[^cfr2026qmsr-e2]: 21 CFR Part 820（现行版），§820.10(c)。[证据](../../../sources/notes/cfr2026qmsr.md#e2)
[^cfr2026qmsr-e3]: 21 CFR Part 820（现行版），§820.7。[证据](../../../sources/notes/cfr2026qmsr.md#e3)
[^cfr2026qmsr-e4]: 21 CFR Part 820（现行版），§820.1(a)。[证据](../../../sources/notes/cfr2026qmsr.md#e4)
[^aabb2026qmsr-e1]: AABB 2026 年 2 月 4 日新闻，第 2 段。[证据](../../../sources/notes/aabb2026qmsr.md#e1)
[^fda2026withdrawn-e2]: FDA 官网《Withdrawn or Expired Guidance》页（内容更新至 2026-03-06），Design Control Guidance 一行。[证据](../../../sources/notes/fda2026withdrawn.md#e2)
[^fda2024qmsr-e3]: FDA 2024，质量管理体系法规最终规则公告（89 FR 7496），第 76 条意见的答复，7517 页。[证据](../../../sources/notes/fda2024qmsr.md#e3)
[^cfr2026ide-e1]: 21 CFR Part 812（现行版，eCFR），§812.1(a)。[证据](../../../sources/notes/cfr2026ide.md#e1)
[^cfr2026ide-e2]: 21 CFR Part 812（现行版），§812.2(a)。[证据](../../../sources/notes/cfr2026ide.md#e2)
[^cfr2026ide-e3]: 21 CFR Part 812（现行版），§812.3(m)。[证据](../../../sources/notes/cfr2026ide.md#e3)
[^cfr2026ide-e4]: 21 CFR Part 812（现行版），§812.2(b)(1)(ii)。[证据](../../../sources/notes/cfr2026ide.md#e4)
[^cfr2026ide-e5]: 21 CFR Part 812（现行版），§812.3(o)。[证据](../../../sources/notes/cfr2026ide.md#e5)
[^cfr2026ide-e6]: 21 CFR Part 812（现行版），§812.2(c)(6)。[证据](../../../sources/notes/cfr2026ide.md#e6)
[^cfr2026ide-e7]: 21 CFR Part 812（现行版），§812.1(a)。[证据](../../../sources/notes/cfr2026ide.md#e7)
[^bmes2021ethics-e1]: BMES Code of Ethics 2021，序言。[证据](../../../sources/notes/bmes2021ethics.md#e1)
[^bmes2021ethics-e2]: BMES Code of Ethics 2021，1.1.1。[证据](../../../sources/notes/bmes2021ethics.md#e2)
[^bmes2021ethics-e3]: BMES Code of Ethics 2021，2.1.3。[证据](../../../sources/notes/bmes2021ethics.md#e3)
[^bmes2021ethics-e4]: BMES Code of Ethics 2021，2.1.4。[证据](../../../sources/notes/bmes2021ethics.md#e4)
[^bmes2021ethics-e5]: BMES Code of Ethics 2021，2.2.2。[证据](../../../sources/notes/bmes2021ethics.md#e5)
[^bmes2021ethics-e8]: BMES Code of Ethics 2021，3.1.2。[证据](../../../sources/notes/bmes2021ethics.md#e8)
[^bmes2021ethics-e9]: BMES Code of Ethics 2021，3.2.2。[证据](../../../sources/notes/bmes2021ethics.md#e9)
[^bmes2021ethics-e10]: BMES Code of Ethics 2021，5.1.1。[证据](../../../sources/notes/bmes2021ethics.md#e10)
[^bmes2021ethics-e11]: BMES Code of Ethics 2021，5.1.2。[证据](../../../sources/notes/bmes2021ethics.md#e11)
[^embstbmeprepare-e1]: IEEE EMBS，TBME 投稿说明页（2025 年 1 月存档），期刊简介。[证据](../../../sources/notes/embstbmeprepare.md#e1)
[^embstbmeprepare-e2]: IEEE EMBS，TBME 投稿说明页，Abstract。[证据](../../../sources/notes/embstbmeprepare.md#e2)
[^embstbmeprepare-e3]: IEEE EMBS，TBME 投稿说明页，Cover Letter。[证据](../../../sources/notes/embstbmeprepare.md#e3)
[^embstbmeprepare-e4]: IEEE EMBS，TBME 投稿说明页，Cover Letter 之后的说明。[证据](../../../sources/notes/embstbmeprepare.md#e4)
[^embstbmeprepare-e5]: IEEE EMBS，TBME 投稿说明页，Letters。[证据](../../../sources/notes/embstbmeprepare.md#e5)
[^embstbmeprepare-e6]: IEEE EMBS，TBME 投稿说明页，Peer Review。[证据](../../../sources/notes/embstbmeprepare.md#e6)
[^embstbmeprepare-e7]: IEEE EMBS，TBME 投稿说明页，Author Consent Form。[证据](../../../sources/notes/embstbmeprepare.md#e7)
[^embstbmeprepare-e8]: IEEE EMBS，TBME 投稿说明页，利益冲突披露。[证据](../../../sources/notes/embstbmeprepare.md#e8)
[^embstbmeprepare-e9]: IEEE EMBS，TBME 投稿说明页，人和动物受试者。[证据](../../../sources/notes/embstbmeprepare.md#e9)
[^collins2024tripodai-e1]: Collins 等人 2024（TRIPOD+AI），Summary points。[证据](../../../sources/notes/collins2024tripodai.md#e1)
[^collins2024tripodai-e2]: Collins 等人 2024，Abstract。[证据](../../../sources/notes/collins2024tripodai.md#e2)
[^collins2024tripodai-e3]: Collins 等人 2024，Table 1。[证据](../../../sources/notes/collins2024tripodai.md#e3)
[^collins2024tripodai-e4]: Collins 等人 2024，Development of TRIPOD+AI。[证据](../../../sources/notes/collins2024tripodai.md#e4)
[^collins2024tripodai-e5]: Collins 等人 2024，Box 1 Glossary。[证据](../../../sources/notes/collins2024tripodai.md#e5)
[^collins2024tripodai-e6]: Collins 等人 2024，Box 1 Glossary 脚注。[证据](../../../sources/notes/collins2024tripodai.md#e6)
[^icmje2026recommendations-e15]: ICMJE 2026，§III.L.1。[证据](../../../sources/notes/icmje2026recommendations.md#e15)
[^icmje2026recommendations-e17]: ICMJE 2026，§III.L.1。[证据](../../../sources/notes/icmje2026recommendations.md#e17)
[^icmje2026recommendations-e11]: ICMJE 2026，§II.E。[证据](../../../sources/notes/icmje2026recommendations.md#e11)
[^ieee2026pspb-e4]: IEEE PSPB Operations Manual 2026，§8.1.7.F。[证据](../../../sources/notes/ieee2026pspb.md#e4)
[^ieee2026pspb-e6]: IEEE PSPB Operations Manual 2026，§8.2.1.A.1。[证据](../../../sources/notes/ieee2026pspb.md#e6)
[^nc3rsthe3rs-e4]: NC3Rs，The 3Rs，Replacement。[证据](../../../sources/notes/nc3rsthe3rs.md#e4)
[^hopewell2025consort-e2]: Hopewell 等人 2025（CONSORT 2025），Introduction。[证据](../../../sources/notes/hopewell2025consort.md#e2)
