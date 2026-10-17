# 化学工程：学科概况

本文讲化学工程的研究实际怎样运转：在实验室里测反应和材料，用模型算过程，还要考虑放大、安全、成本和环境影响。化学工程和化学有大片交叉，偏化学本身的内容见[化学篇](../chemistry/README.md)；本学科常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)；各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)。这里只写本学科特有的东西。

**读完本文，你应该能：**

- 说清实验室结果和工业规模之间隔着什么，为什么"放大"本身就是研究问题；
- 在动手前做危害评估，知道一次大学化学系实验室事故暴露了哪些问题；
- 参考一组催化研究者的建议报告动力学和催化数据，让别人能拿来比较；
- 以碳捕集与利用方向的一套指南为例，读懂并透明地报告技术经济分析和生命周期评估；
- 在和企业合作时，提前处理好保密、专利和发表的关系。

---

## 本领域研究怎样运转

### 研究什么：从分子尺度的反应到整个过程

化学工程的研究跨度很大。以美国化学会（American Chemical Society，ACS）的期刊《Industrial & Engineering Chemistry Research》（下称 I&EC Research）为例，它按主题把论文分成动力学、催化与反应工程，材料与界面，过程系统工程，分离，热力学、传递与流体力学等栏目[^acsiecrauthorguide-e2]，也接收过程设计与开发方面的论文，包括建模和放大方法[^acsiecrauthorguide-e1]。这只是一份期刊的分类，但能看出研究对象既有反应和材料本身，也有由许多设备组成的整个过程 `[本项目分析]`。

一个典型的课题，常常是几种工作的组合：在实验室测反应速率、选择性或物性；用这些数据建立模型；再用模型去设计、优化或评估一个过程 `[本项目分析]`。

### 实验室结果离工业还有多远：放大

**放大**（scale-up）指把实验室里几克、几毫升的过程，做到中试装置乃至工业装置的规模 `[本项目分析]`。这一步不是"多做一点"那么简单：

- **催化剂性能还会在更大的装置里测。** Bligaard 等人（2016 年的一篇观点文章，作者是美国能源部催化科学项目资助的一批研究者）提到，催化剂性能常在成排几乎相同的实验台规模反应器和中试规模反应器里测[^bligaard2016benchmarking-e3]。
- **实验室规模的数据会让估算偏差。** 一份专门针对碳捕集与利用（把二氧化碳收集起来、再做成产品的技术）的生命周期评估指南指出：技术成熟度低的工艺还没做热集成和优化，能耗、溶剂消耗偏高，又缺少反应后提纯等辅助工序，所以基于实验室规模的评估可能高估也可能低估环境影响[^muller2020lca-e7]。同系列的技术经济评估指南也要求，技术成熟度低时考虑学习曲线和改进[^zimmermann2020tea-e12]。
- **量变了，危险也会变。** 见下文[实验安全](#实验安全是研究的一部分动手前先做危害评估)里那次放大到约 10 克后发生的事故[^csb2011texastech-e2]。

所以，论文里说"有工业应用前景"时，要说清结果是在什么规模下得到的，放大后哪些结论可能变 `[本项目分析]`。

### 建模和仿真：先过物料衡算和能量衡算这一关

过程模型和仿真是本领域的常用工具 `[本项目分析]`。一个朴素但常被跳过的检查是：方案本身说得通吗？上面那份碳捕集与利用的技术经济评估指南要求，评估之前先做"合理性检查"，核对动力学、物料衡算和能量衡算，方案不能违反热力学定律[^zimmermann2020tea-e5]。这份指南只针对碳捕集与利用，但这条检查拿到一般的过程建模里也值得做 `[本项目分析]`。仿真研究怎样做验证和确认，见研究方法里的[定量仿真](../../06_methods/simulation_study.md)。

### 发表：以期刊为主，看清目标期刊的要求

本文资料没有化学工程会议和期刊比重的统计；下面只以 I&EC Research 一份期刊为例，投其他期刊时以对方的作者指南为准 `[本项目分析]`。

- **只报数据不够。** I&EC Research 写明，只报告数据或计算结果的论文会被拒[^acsiecrauthorguide-e3]；结论缺乏明显的重要性和新意、读者面太窄的稿件，最可能在编辑初审就被拒[^acsiecrauthorguide-e4]。
- **预印本可以发，但要说明。** 这份期刊接受作者把投稿原稿放到预印本服务器上，但要在投稿信里明确说明[^acsiecrauthorguide-e5]。
- **署名和审稿的一般规则**见写作和发表部分的[选择发表渠道与投稿](../../03_write-and-publish/02_venue-and-submission.md)。本文资料没有化学工程特有的署名惯例。

### 和企业合作：保密、专利、发表要提前安排

化学工程的不少课题和产业应用有关，可能涉及企业合作 `[本项目分析]`。资料里能看到几个具体的影响：

- **企业的数据常常不公开。** 碳捕集与利用的技术经济评估指南提到，据报道企业常按内部标准做这类评估，但通常不发表[^zimmermann2020tea-e2]。所以你能对比的公开数据可能有限 `[本项目分析]`。
- **专利要在发表前处理好。** I&EC Research 要求作者在首次发表前解决好专利和知识产权问题，期刊不会因此推迟发表[^acsiecrauthorguide-e10]。
- **先报告学校，再公开或合作。** 按美国伯克利的说明，和企业合作前、公开前至少 1～2 个月，都要先向学校提交发明披露[^berkeleydisclose-e1][^berkeleydisclose-e2]；一旦公开，在大多数美国以外的国家直接失去申请资格[^berkeleydisclose-e4]。**各国和各单位规定不同，以本单位为准** `[本项目分析]`。详见[电子信息篇：发表还是申请专利](../electrical-engineering/README.md#发表还是申请专利以美国为例)。

---

## 和其他学科不同的地方

下表是本项目的归纳，用来帮你快速定位差别，不是严格的学科划分 `[本项目分析]`。

| | 化学工程 | 化学 | 计算机领域 |
|---|---|---|---|
| 关心的问题 | 除了"能不能反应"，还关心放大、成本、能耗和环境影响 | 偏重分子、反应和材料本身（见[化学篇](../chemistry/README.md)） | 以算法、系统和软件为主 |
| 结果从哪来 | 实验室测量、过程模型和仿真，常常两者结合 | 以实验室合成和表征为主 | 以代码、系统和数据上的实验为主 |
| "比较"怎么做 | 要统一反应条件、转化率、系统边界等前提（见下文） | 和化学工程有交叉，例如催化 | 有公开的基准数据集和评测流程（见[基准评测](../computer-science/practices/benchmarking.md)） |
| 安全 | 实验本身可能有爆炸、毒性等危害，动手前要评估 | 同样重要 | 一般没有实验室物理危害 |
| 和产业的关系 | 合作多，数据和规程可能受保密限制 | 视方向而定 | 视方向而定 |

---

## 本领域的规范和报告标准

### 职业伦理：以美国化学工程师学会的准则为例

美国化学工程师学会（American Institute of Chemical Engineers，AIChE）的伦理准则由学会理事会通过，约束对象是它的会员[^aichecodeethics-e1]。不是会员、不在美国，也可以把它当作参考 `[本项目分析]`。和研究最相关的几条：

- 把公众的安全、健康和福祉放在首位，并保护环境[^aichecodeethics-e2]；
- 发现工作会损害同事或公众的健康安全时，正式告知雇主或客户[^aichecodeethics-e3]；
- 主动听取对自己工作的批评，发表意见、提供信息都要客观真实[^aichecodeethics-e4][^aichecodeethics-e5]；
- 避免利益冲突，绝不泄露保密信息[^aichecodeethics-e6]——和企业合作时尤其要记住。

科研诚信的一般规则见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md)。

### 实验安全是研究的一部分：动手前先做危害评估

**一次学校实验室事故。** 美国化学安全与危害调查委员会（Chemical Safety Board，CSB，美国联邦政府的事故调查机构）调查过这样一起事故：2010 年 1 月，得克萨斯理工大学化学与生物化学系一名研究生在处理的化合物发生爆炸，失去三根手指，手和脸烧伤，一只眼睛受伤[^csb2011texastech-e1]。事故发生在化学系，不是化学工程系；放在这里，是因为教训对任何做化学实验的人都适用 `[本项目分析]`。调查报告列出的问题包括：

- **放大没有经过负责人。** 学生把合成量放大到约 10 克，没有征求两位课题负责人的意见[^csb2011texastech-e2]；他们假定少量时有效的防护措施，量大时同样有效[^csb2011texastech-e3]。
- **安全限制只是口头说过。** 合成量不超过 100 毫克的限制只是口头传达的[^csb2011texastech-e4]，接受访谈的学生都没有说知道这条严格的上限[^csb2011texastech-e5]。
- **没有做正式的危害评估**[^csb2011texastech-e6]。危害评估指有组织地识别和分析一个过程或活动中的危险情形有多严重[^csb2011texastech-e7]。
- **未遂事件没有传开。** 此前，同一课题组有学生用错计量单位，做出了过量的含能材料[^csb2011texastech-e12]，但这件事没有向课题组以外的人报告[^csb2011texastech-e13]。
- **组会不谈安全，记录不完整。** 每周组会主要谈实验结果，不谈实际怎么做和安全影响[^csb2011texastech-e14]；实验记录本没有日期，也不总是记下用量[^csb2011texastech-e15]；戴不戴护目镜被当成个人选择[^csb2011texastech-e16]。

**这对你意味着什么。** 这家调查机构认为，化工过程行业的标准不能全部搬到学校实验室，但借鉴其中适用的经验是有用的[^csb2011texastech-e8]；现有的危害评估标准面向工业环境，不能完全照搬到学校研究实验室[^csb2011texastech-e9]。它总结的教训包括：需要针对具体研究的书面规程和培训[^csb2011texastech-e10]；未遂事件只有被记录、追踪、传达，才能成为改进的机会[^csb2011texastech-e11]。落到个人身上，就是：动手前做危害评估，改变用量或条件前先找负责人，把安全要求写下来，出了未遂事件要报告 `[本项目分析]`。具体用什么评估方法、要走什么审批，以你所在单位和国家的规定为准 `[本项目分析]`。

**写进论文。** 以 I&EC Research 为例，它要求作者突出写明工作中任何意外的、新的或重大的危害和风险，完整论文写在实验部分[^acsiecrauthorguide-e9]。

### 催化和动力学数据：怎样报告别人才能比较

下面的做法来自 Bligaard 等人 2016 年的观点文章。作者说明，这些建议只代表署名作者，来自美国能源部催化科学项目部分研究者的讨论，讨论不以达成共识为目标[^bligaard2016benchmarking-e2]。所以下面是一组作者的观点，不是行业或期刊标准；它讲的是催化研究，但"统一前提才能比较"的道理也适用于其他反应数据 `[本项目分析]`。

**为什么难比较。** 在催化研究里，重要的性能指标是活性、选择性和失活情况[^bligaard2016benchmarking-e1]。可是在多相催化里，对一种催化剂最优的条件，对另一种可能很差；活性位点在测试中还会变化[^bligaard2016benchmarking-e7]。在分子催化方向，重复文献里的反应，可能只得到远低于报告值的活性，甚至完全没有活性，原因可能是没写全的试剂和操作差别[^bligaard2016benchmarking-e10]。

**作者们建议报告时做到**（下面几条分别出自原文的多相、分子、计算和电催化部分，做哪个方向就读哪部分原文）：

1. **测的是本征速率。** 本征速率指不受传质传热干扰、只反映反应本身的速率 `[本项目分析]`。测量要准确、可重复，不受传质传热限制干扰，并覆盖较宽的转化率范围[^bligaard2016benchmarking-e5]；要验证不存在传质、传热和混合的影响[^bligaard2016benchmarking-e12]。转换频率（按活性位点归一化的反应速率）要基于速率测量，不能只用某一个时间点的转化率[^bligaard2016benchmarking-e6]。
2. **写清怎么算的。** 写明转换数、转换频率怎样从原始数据算出，活性位点是怎样数出来或估计出来的[^bligaard2016benchmarking-e14]。
3. **选择性配上转化率。** 报告选择性时同时给出转化率[^bligaard2016benchmarking-e11]；比较几种催化剂的选择性时，在相同转化率下测[^bligaard2016benchmarking-e15]。核对物料衡算[^bligaard2016benchmarking-e13]。
4. **有对照。** 在相同条件下和公认的或最先进的催化剂比较[^bligaard2016benchmarking-e17]；做不加催化剂的对照实验[^bligaard2016benchmarking-e18]。
5. **报告稳定性，但别用错方法。** 只在高转化率下测产率的循环实验，不能证明催化剂稳定[^bligaard2016benchmarking-e16]；加速老化试验在不清楚失活原因时有风险[^bligaard2016benchmarking-e9]。
6. **计算研究公开输入输出文件**[^bligaard2016benchmarking-e19]。电催化有自己的归一化要求，例如电流要按几种不同的参数分别归一化[^bligaard2016benchmarking-e20]，做这个方向时要读原文。

作者们还建议多个课题组合作，对同一批样品做盲法轮流测量，以确定现实的误差范围[^bligaard2016benchmarking-e8]。

### 技术经济分析和生命周期评估：前提写清楚，结论才可信

**技术经济分析**（techno-economic assessment）估算一个过程要花多少钱、能不能赚钱 `[本项目分析]`；**生命周期评估**（life cycle assessment）计算一个产品或服务在整个生命周期中的环境影响[^muller2020lca-e2]。有些化学工程论文用它们来论证新工艺值得做 `[本项目分析]`。

下面的规则来自 Global CO2 Initiative（美国密歇根大学）等机构牵头制定的一套指南，适用对象是碳捕集与利用技术。技术经济评估部分吸收了 50 多位产业界、学术界和政策界专家的意见[^zimmermann2020tea-e4]，生命周期评估部分有 40 多位专家参与[^muller2020lca-e1]。其他技术方向可以参考，但不是通用标准 `[本项目分析]`。

**问题有多大。** 指南作者指出，这一领域的技术经济评估没有公认标准，常常拿不可比的东西作比较，也不透明[^zimmermann2020tea-e1]；这一领域的生命周期评估研究常因功能单位（计算环境影响的比较基准）或系统边界（算进哪些环节）不同而无法相互比较[^muller2020lca-e4]。例如二氧化碳制甲醇，文献报告的碳足迹从每千克 −1.7 到 +9.7 千克二氧化碳当量都有[^muller2020lca-e5]；把电力和二氧化碳供应的假设统一后，差异缩小到所有结果同号，并能和化石路线甲醇清楚区分[^muller2020lca-e6]。

**指南对碳捕集与利用评估的要求（做其他技术时可以拿来对照）：**

- **先写清和什么比、在哪、多大规模、谁委托。** 评估目标要写明比较对象、地点、时间跨度、规模和合作方[^zimmermann2020tea-e6]，以及委托方和作者[^zimmermann2020tea-e7]。
- **功能单位按用途定。** 新产品和传统产品不一样时，按实际用途中的性能比较，例如洗涤剂按洗涤效果比，而不是按质量比[^muller2020lca-e9]。
- **不要把排除在外的东西当成免费。** 不算上游工序，不等于二氧化碳、氢气、电可以按零成本计[^zimmermann2020tea-e8]；也不要在基准情景里假设电价为零或为负[^zimmermann2020tea-e14]，或假设乐观的未来制氢技术、比目前可行更大的生产规模[^zimmermann2020tea-e13]。
- **统一口径。** 不同来源的数据换算到同一年份、同一热值基准[^zimmermann2020tea-e11]。分清"捕集一吨二氧化碳的成本"和"减排一吨二氧化碳的成本"[^zimmermann2020tea-e15]。
- **结论建立在不确定性和敏感性分析上**[^zimmermann2020tea-e17]。指标要和对照值比较后再解读[^zimmermann2020tea-e18]。负的生命周期评估结果只是比较的结果，不一定说明产品是碳中和或负排放的[^muller2020lca-e10]。
- **报告写全。** 写出全部假设、数据、方法、结果和局限[^zimmermann2020tea-e19][^muller2020lca-e11]；保密数据拿不到要明说[^zimmermann2020tea-e10]；列出做评估的人，说明是否经过审查[^zimmermann2020tea-e20]。
- **数据不够就收缩问题。** 数据质量提不到够用，要么调整目标和范围，要么停止研究[^zimmermann2020tea-e9]。早期阶段，生命周期评估最有用的是找出影响最大的环节，再做敏感性分析[^muller2020lca-e8]。

### 数据公开和利益冲突

美国化学会所有期刊都强烈鼓励作者发表时公开研究数据[^acsiecrauthorguide-e7]，但 I&EC Research 自己没有专门的数据要求[^acsiecrauthorguide-e8]。利益冲突的声明是各学科通用的要求，见[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#5-署名引用和利益冲突给每个贡献者应得的认可)；和企业合作的研究尤其要写清楚 `[本项目分析]`。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表只列本文资料能支持的三种，其他套路本文资料未涉及。表的分组和第二栏是本项目的归纳；催化的标准来自一篇观点文章，技术经济分析和生命周期评估的标准来自碳捕集与利用方向的指南，都不是全学科通用的规定 `[本项目分析]`。

| 套路 | 在化学工程里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md) | 提出新的工艺、催化剂或设备，或用过程模型设计一个过程 | 和最先进的催化剂在相同条件下比[^bligaard2016benchmarking-e17]，做不加催化剂的对照[^bligaard2016benchmarking-e18]；过程方案先核对物料衡算、能量衡算，不能违反热力学定律[^zimmermann2020tea-e5] | [合成与表征研究](../../06_methods/synthesis_study.md)、[定量仿真](../../06_methods/simulation_study.md)、[优化研究](../computer-science/practices/optimization_study.md)（计算机篇） |
| [比较评估](../../05_research-strategies/compare_evaluate.md) | 比较几种催化剂；用技术经济分析和生命周期评估把新工艺和现有路线比 | 催化剂的选择性在相同转化率下比[^bligaard2016benchmarking-e15]；写清比较对象、地点、规模[^zimmermann2020tea-e6]；考虑学习曲线时，对照技术也同样考虑[^zimmermann2020tea-e12]；功能单位按实际用途定[^muller2020lca-e9] | [基准评测](../computer-science/practices/benchmarking.md)（计算机篇）、上文[技术经济分析和生命周期评估](#技术经济分析和生命周期评估前提写清楚结论才可信) |
| [测量](../../05_research-strategies/measure.md) | 测反应速率、选择性等数据，让别人能拿来比 | 测本征速率，验证没有传质、传热和混合的影响[^bligaard2016benchmarking-e5][^bligaard2016benchmarking-e12]；写清转换频率怎样算出[^bligaard2016benchmarking-e14]；有作者建议多个课题组盲法轮测同一批样品，定出现实的误差范围[^bligaard2016benchmarking-e8] | [实验测量研究](../../06_methods/experimental_measurement.md)、上文[催化和动力学数据](#催化和动力学数据怎样报告别人才能比较) |

怎么用这张表 `[本项目分析]`：先按核心主张定主要套路。例如提出新催化剂、再用技术经济分析论证它值得做，按构建改进的标准要求，经济部分按比较评估的要求写清前提。

## 本学科常用的研究方法

本学科没有独有的方法文档，用的是[研究类型](../../06_methods/README.md)里的跨学科方法和计算机篇的实践 `[本项目分析]`：

- [合成与表征研究](../../06_methods/synthesis_study.md)、[实验测量研究](../../06_methods/experimental_measurement.md)：改用量、改条件前先做危害评估，见上文[实验安全](#实验安全是研究的一部分动手前先做危害评估)。
- [定量仿真](../../06_methods/simulation_study.md)：过程模拟、反应器建模，参数常来自实验数据。
- [优化研究](../computer-science/practices/optimization_study.md)、[基准评测](../computer-science/practices/benchmarking.md)、[工程研究](../computer-science/practices/engineering_research.md)（计算机篇）：过程优化的目标常常不止一个（成本、能耗、排放），约束来自物理和安全限制；催化的"基准"是标准催化剂、标准反应条件，前提统一更难[^bligaard2016benchmarking-e7]。技术经济分析和生命周期评估没有单独的方法文档，按上文一节做。

---

## 给新手的建议

1. **动手前做危害评估，改用量先找负责人。** 得克萨斯理工大学的事故里，放大没有经过负责人，也没有正式的危害评估[^csb2011texastech-e2][^csb2011texastech-e6]。具体流程以你所在单位为准。
2. **把安全要求和未遂事件写下来。** 口头传达的限制，学生都说不知道[^csb2011texastech-e5]；未遂事件没有传开，教训就丢了[^csb2011texastech-e13]。
3. **测数据前，先想好别人怎样拿它比较**，标准见上文[常用套路与证据标准](#常用套路与证据标准)。
4. **说"有工业前景"之前，写清规模和假设。** 碳捕集与利用的生命周期评估指南提醒，基于实验室规模的环境影响估算可能偏高也可能偏低[^muller2020lca-e7]。
5. **做技术经济分析和生命周期评估，把假设放到最显眼的地方。** 以二氧化碳制甲醇为例，文献报告的碳足迹从负值到正值都有[^muller2020lca-e5]，统一电力和二氧化碳供应的假设后差异才缩小[^muller2020lca-e6]。
6. **签合作协议前，问清能发表什么、要不要先申请专利。** 期刊不会因为专利问题推迟发表[^acsiecrauthorguide-e10]；按美国一所大学的说明，公开后在美国以外的大多数国家就不能再申请[^berkeleydisclose-e4]，你所在国家和单位以本地规定为准。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 自己决定把用量放大，假定小量时的防护措施照样有效 | 得克萨斯理工大学的事故正是这样发生的[^csb2011texastech-e2][^csb2011texastech-e3] |
| 安全限制只口头说，实验记录不写日期和用量 | 调查发现学生不知道限制，记录也查不清用量[^csb2011texastech-e5][^csb2011texastech-e15] |
| 用某一个时间点的转化率算转换频率 | 应基于速率测量，并改变浓度来检验[^bligaard2016benchmarking-e6] |
| 只在高转化率下做循环实验，就说催化剂稳定 | 这证明不了稳定性[^bligaard2016benchmarking-e16] |
| 技术经济分析里把没算进边界的原料、电力当成免费 | 碳捕集与利用指南指出，供应商不会免费提供[^zimmermann2020tea-e8] |
| 把负的生命周期评估结果说成"负排放" | 负值只是比较的结果[^muller2020lca-e10] |

---

## 延伸阅读

- **美国化学安全与危害调查委员会，Texas Tech University Laboratory Explosion 案例研究（2011）**：一所大学化学系实验室事故的调查报告，讲清前因后果。开始做实验之前读。
- **Bligaard 等人 2016，Toward Benchmarking in Catalysis Science**：催化数据怎样测、怎样报告才能比较，分计算、多相、分子和电催化四部分。做催化或动力学实验时读对应部分。
- **Zimmermann 等人 2020（技术经济评估）和 Müller 等人 2020（生命周期评估）**：碳捕集与利用方向的两份指南摘要，都开放获取。不做这个方向，也可以拿来当检查清单参考，但它不是通用标准 `[本项目分析]`。
- **美国化学工程师学会伦理准则**：条目不多，会员要遵守，非会员可作参考。
- **目标期刊的作者指南**：本文只以 I&EC Research 一份期刊为例，不代表其他化工期刊；投稿前读目标期刊自己的指南，特别是安全、数据和预印本部分。
- **你所在单位的实验室安全规定和技术转移部门的说明**：本文引用的是美国的资料，以本单位为准。

[^acsiecrauthorguide-e1]: 美国化学会，I&EC Research 作者指南，Scope of the Journal。[证据](../../../sources/notes/acsiecrauthorguide.md#e1)
[^acsiecrauthorguide-e2]: 美国化学会，I&EC Research 作者指南，Topical Categories。[证据](../../../sources/notes/acsiecrauthorguide.md#e2)
[^acsiecrauthorguide-e3]: 美国化学会，I&EC Research 作者指南，Scope of the Journal。[证据](../../../sources/notes/acsiecrauthorguide.md#e3)
[^acsiecrauthorguide-e4]: 美国化学会，I&EC Research 作者指南，Scope of the Journal。[证据](../../../sources/notes/acsiecrauthorguide.md#e4)
[^acsiecrauthorguide-e5]: 美国化学会，I&EC Research 作者指南，Prior Publication Policy。[证据](../../../sources/notes/acsiecrauthorguide.md#e5)
[^acsiecrauthorguide-e7]: 美国化学会，I&EC Research 作者指南，Research Data Policy。[证据](../../../sources/notes/acsiecrauthorguide.md#e7)
[^acsiecrauthorguide-e8]: 美国化学会，I&EC Research 作者指南，Data Requirements。[证据](../../../sources/notes/acsiecrauthorguide.md#e8)
[^acsiecrauthorguide-e9]: 美国化学会，I&EC Research 作者指南，Safety Considerations。[证据](../../../sources/notes/acsiecrauthorguide.md#e9)
[^acsiecrauthorguide-e10]: 美国化学会，I&EC Research 作者指南，Patent Activities and Intellectual Property。[证据](../../../sources/notes/acsiecrauthorguide.md#e10)
[^aichecodeethics-e1]: 美国化学工程师学会，Code of Ethics，导言段。[证据](../../../sources/notes/aichecodeethics.md#e1)
[^aichecodeethics-e2]: 美国化学工程师学会，Code of Ethics，第 1 条。[证据](../../../sources/notes/aichecodeethics.md#e2)
[^aichecodeethics-e3]: 美国化学工程师学会，Code of Ethics，第 2 条。[证据](../../../sources/notes/aichecodeethics.md#e3)
[^aichecodeethics-e4]: 美国化学工程师学会，Code of Ethics，第 3 条。[证据](../../../sources/notes/aichecodeethics.md#e4)
[^aichecodeethics-e5]: 美国化学工程师学会，Code of Ethics，第 4 条。[证据](../../../sources/notes/aichecodeethics.md#e5)
[^aichecodeethics-e6]: 美国化学工程师学会，Code of Ethics，第 5 条。[证据](../../../sources/notes/aichecodeethics.md#e6)
[^berkeleydisclose-e1]: 伯克利 IPIRA，When to Disclose an Invention to OTL，When to disclose。[证据](../../../sources/notes/berkeleydisclose.md#e1)
[^berkeleydisclose-e2]: 伯克利 IPIRA，When to disclose。[证据](../../../sources/notes/berkeleydisclose.md#e2)
[^berkeleydisclose-e4]: 伯克利 IPIRA，FAQ。[证据](../../../sources/notes/berkeleydisclose.md#e4)
[^bligaard2016benchmarking-e1]: Bligaard 等人 2016，摘要。[证据](../../../sources/notes/bligaard2016benchmarking.md#e1)
[^bligaard2016benchmarking-e2]: Bligaard 等人 2016，§1.5，第 2593 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e2)
[^bligaard2016benchmarking-e3]: Bligaard 等人 2016，§1.4，第 2591 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e3)
[^bligaard2016benchmarking-e5]: Bligaard 等人 2016，§2.2.1，第 2595 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e5)
[^bligaard2016benchmarking-e6]: Bligaard 等人 2016，§2.2.1，第 2595 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e6)
[^bligaard2016benchmarking-e7]: Bligaard 等人 2016，§2.2，第 2595 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e7)
[^bligaard2016benchmarking-e8]: Bligaard 等人 2016，§2.2.1，第 2595 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e8)
[^bligaard2016benchmarking-e9]: Bligaard 等人 2016，§2.2.1，第 2595–2596 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e9)
[^bligaard2016benchmarking-e10]: Bligaard 等人 2016，§2.3，第 2596 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e10)
[^bligaard2016benchmarking-e11]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e11)
[^bligaard2016benchmarking-e12]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e12)
[^bligaard2016benchmarking-e13]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e13)
[^bligaard2016benchmarking-e14]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e14)
[^bligaard2016benchmarking-e15]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e15)
[^bligaard2016benchmarking-e16]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e16)
[^bligaard2016benchmarking-e17]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e17)
[^bligaard2016benchmarking-e18]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e18)
[^bligaard2016benchmarking-e19]: Bligaard 等人 2016，§2.1.1，第 2593 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e19)
[^bligaard2016benchmarking-e20]: Bligaard 等人 2016，§2.4.1，第 2598 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e20)
[^csb2011texastech-e1]: 美国化学安全与危害调查委员会 2011（Texas Tech 案例研究），§1.0，第 1 页。[证据](../../../sources/notes/csb2011texastech.md#e1)
[^csb2011texastech-e2]: 美国化学安全与危害调查委员会 2011，§4.0，第 3 页。[证据](../../../sources/notes/csb2011texastech.md#e2)
[^csb2011texastech-e3]: 美国化学安全与危害调查委员会 2011，§4.0，第 4 页。[证据](../../../sources/notes/csb2011texastech.md#e3)
[^csb2011texastech-e4]: 美国化学安全与危害调查委员会 2011，§3.0，第 3 页。[证据](../../../sources/notes/csb2011texastech.md#e4)
[^csb2011texastech-e5]: 美国化学安全与危害调查委员会 2011，§3.0，第 3 页。[证据](../../../sources/notes/csb2011texastech.md#e5)
[^csb2011texastech-e6]: 美国化学安全与危害调查委员会 2011，§4.0，第 4 页。[证据](../../../sources/notes/csb2011texastech.md#e6)
[^csb2011texastech-e7]: 美国化学安全与危害调查委员会 2011，§4.0 脚注 13，第 4 页。[证据](../../../sources/notes/csb2011texastech.md#e7)
[^csb2011texastech-e8]: 美国化学安全与危害调查委员会 2011，§6.2，第 8 页。[证据](../../../sources/notes/csb2011texastech.md#e8)
[^csb2011texastech-e9]: 美国化学安全与危害调查委员会 2011，§9.0 第 3 条，第 17 页。[证据](../../../sources/notes/csb2011texastech.md#e9)
[^csb2011texastech-e10]: 美国化学安全与危害调查委员会 2011，§9.0 第 4 条，第 17 页。[证据](../../../sources/notes/csb2011texastech.md#e10)
[^csb2011texastech-e11]: 美国化学安全与危害调查委员会 2011，§9.0 第 6 条，第 17 页。[证据](../../../sources/notes/csb2011texastech.md#e11)
[^csb2011texastech-e12]: 美国化学安全与危害调查委员会 2011，§7.0，第 13 页。[证据](../../../sources/notes/csb2011texastech.md#e12)
[^csb2011texastech-e13]: 美国化学安全与危害调查委员会 2011，§7.0，第 13 页。[证据](../../../sources/notes/csb2011texastech.md#e13)
[^csb2011texastech-e14]: 美国化学安全与危害调查委员会 2011，§6.2.3，第 12 页。[证据](../../../sources/notes/csb2011texastech.md#e14)
[^csb2011texastech-e15]: 美国化学安全与危害调查委员会 2011，§4.0 脚注 7，第 3 页。[证据](../../../sources/notes/csb2011texastech.md#e15)
[^csb2011texastech-e16]: 美国化学安全与危害调查委员会 2011，§4.0，第 4 页。[证据](../../../sources/notes/csb2011texastech.md#e16)
[^muller2020lca-e1]: Müller 等人 2020，Abstract。[证据](../../../sources/notes/muller2020lca.md#e1)
[^muller2020lca-e2]: Müller 等人 2020，General Introduction to Life Cycle Assessment。[证据](../../../sources/notes/muller2020lca.md#e2)
[^muller2020lca-e4]: Müller 等人 2020，Introduction。[证据](../../../sources/notes/muller2020lca.md#e4)
[^muller2020lca-e5]: Müller 等人 2020，Introduction。[证据](../../../sources/notes/muller2020lca.md#e5)
[^muller2020lca-e6]: Müller 等人 2020，Introduction。[证据](../../../sources/notes/muller2020lca.md#e6)
[^muller2020lca-e7]: Müller 等人 2020，General Introduction to Life Cycle Assessment。[证据](../../../sources/notes/muller2020lca.md#e7)
[^muller2020lca-e8]: Müller 等人 2020，General Introduction to Life Cycle Assessment。[证据](../../../sources/notes/muller2020lca.md#e8)
[^muller2020lca-e9]: Müller 等人 2020，Scope Definition › Defining Functional Units。[证据](../../../sources/notes/muller2020lca.md#e9)
[^muller2020lca-e10]: Müller 等人 2020，Life Cycle Interpretation。[证据](../../../sources/notes/muller2020lca.md#e10)
[^muller2020lca-e11]: Müller 等人 2020，Reporting。[证据](../../../sources/notes/muller2020lca.md#e11)
[^zimmermann2020tea-e1]: Zimmermann 等人 2020，Abstract。[证据](../../../sources/notes/zimmermann2020tea.md#e1)
[^zimmermann2020tea-e2]: Zimmermann 等人 2020，Introduction。[证据](../../../sources/notes/zimmermann2020tea.md#e2)
[^zimmermann2020tea-e4]: Zimmermann 等人 2020，Discussion。[证据](../../../sources/notes/zimmermann2020tea.md#e4)
[^zimmermann2020tea-e5]: Zimmermann 等人 2020，Goal › Perspectives and Principles of Assessment Goals。[证据](../../../sources/notes/zimmermann2020tea.md#e5)
[^zimmermann2020tea-e6]: Zimmermann 等人 2020，Goal › Perspectives and Principles of Assessment Goals。[证据](../../../sources/notes/zimmermann2020tea.md#e6)
[^zimmermann2020tea-e7]: Zimmermann 等人 2020，Goal › Perspectives and Principles of Assessment Goals。[证据](../../../sources/notes/zimmermann2020tea.md#e7)
[^zimmermann2020tea-e8]: Zimmermann 等人 2020，Scope › Including or excluding CCU upstream processes。[证据](../../../sources/notes/zimmermann2020tea.md#e8)
[^zimmermann2020tea-e9]: Zimmermann 等人 2020，Inventory › Data Quality。[证据](../../../sources/notes/zimmermann2020tea.md#e9)
[^zimmermann2020tea-e10]: Zimmermann 等人 2020，Inventory › Data Quality。[证据](../../../sources/notes/zimmermann2020tea.md#e10)
[^zimmermann2020tea-e11]: Zimmermann 等人 2020，Inventory › Collecting Data。[证据](../../../sources/notes/zimmermann2020tea.md#e11)
[^zimmermann2020tea-e12]: Zimmermann 等人 2020，Inventory › Collecting Data。[证据](../../../sources/notes/zimmermann2020tea.md#e12)
[^zimmermann2020tea-e13]: Zimmermann 等人 2020，Inventory › Hydrogen as an input。[证据](../../../sources/notes/zimmermann2020tea.md#e13)
[^zimmermann2020tea-e14]: Zimmermann 等人 2020，Inventory › Electricity as an input。[证据](../../../sources/notes/zimmermann2020tea.md#e14)
[^zimmermann2020tea-e15]: Zimmermann 等人 2020，Inventory › Deriving a CO2 Price。[证据](../../../sources/notes/zimmermann2020tea.md#e15)
[^zimmermann2020tea-e17]: Zimmermann 等人 2020，Interpretation › Uncertainty and Sensitivity Analysis。[证据](../../../sources/notes/zimmermann2020tea.md#e17)
[^zimmermann2020tea-e18]: Zimmermann 等人 2020，Interpretation › Interpretation of Indicators。[证据](../../../sources/notes/zimmermann2020tea.md#e18)
[^zimmermann2020tea-e19]: Zimmermann 等人 2020，Reporting › Content。[证据](../../../sources/notes/zimmermann2020tea.md#e19)
[^zimmermann2020tea-e20]: Zimmermann 等人 2020，Reporting › Reporting Styles。[证据](../../../sources/notes/zimmermann2020tea.md#e20)
