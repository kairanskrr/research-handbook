# 工程研究（设计科学）：提出并评估新的方法、工具或系统

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本文讲计算机领域最常见的一类研究：**提出一个新的技术、算法、工具或系统，并证明它有效**。

本文只讲这类研究特有的做法。通用的部分用链接指过去，不在这里重复：主张与证据怎么对应、基线怎么比才公平、消融实验、随机性与统计、效度威胁，见通用篇的[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)；论文怎么写，见[写作](../../../general/3_after/01_writing.md)；代码和数据怎么整理，见[整理科研材料](../../../general/2_during/03_organizing_materials.md)。

如果你只是系统地比较一批现有工具或模型，而不提出新方法，那是[基准评测](benchmarking.md)。

**读完本文，你应该能：**

- 判断自己的研究是不是工程研究，说清"新在哪里、比谁好"；
- 把贡献写成可以检验的主张，并为每条主张选对验证方式；
- 选出站得住的基线和基准，设计一套覆盖有效性、代价、通用性和各部分必要性的评估；
- 写出真正的效度威胁，并按社区通行的标准公开研究制品；
- 用文末的检查清单检查自己的论文。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为"发明并评估技术制品的研究"[^ralph2020empirical-e79]。这里的**制品**（artifact）范围很广：算法、模型、语言、方法、系统、工具，以及其他基于计算机的技术[^ralph2020empirical-e80]。在软件工程顶会 ICSE 上，报告一种新技术的论文是最常见的一类[^shaw2003writing-e26]。系统、安全、程序语言、机器学习等方向的大多数论文也属于这一类 `[本项目分析]`。

它回答的问题通常是："怎样做到（或自动做到）X？有没有更好的做法？"或者"怎样评估 X 的质量或正确性？"[^shaw2003writing-e25]

**和相近的研究怎么区分**：

| | 工程研究 | 评估已有方法的实验 | 经验报告 |
|---|---|---|---|
| 主要产出 | 一个新的制品，以及它有效的证据 | 关于已有方法效果的结论 | 应用已有方法的经历和教训 |
| 核心问题 | 我的新方法是否比现有的更好、好在哪里 | A 和 B 哪个更好、在什么条件下 | 实际用起来怎么样 |
| SIGSOFT 对应标准 | 工程研究标准 | 实验标准 | 不属于工程研究 |

依据：SIGSOFT 工程研究标准的适用范围[^ralph2020empirical-e80]。

审稿人要能一眼看出你做的是哪一种：提出了新技术并演示，还是把以前的技术用在新例子上，还是评估一项成熟技术。看不出来，就是没写清楚[^shaw2003writing-e31]。

> **关于名称**：这类研究在信息系统领域常被称为"设计科学"（design science）。SIGSOFT 标准的作者认为这是误用：这个词原本指研究设计者及其设计过程，应当叫"工程研究"[^ralph2020empirical-e98]。两个名字你都会遇到，指的是同一类研究。

---

## 2. 怎么做

### 第 1 步：说清问题，以及"新在哪里、比谁好"

**怎么做：**

1. **先讲问题，再讲方案。** 说明要解决什么问题、为什么重要，以及**现有最好的方法为什么不够好**[^ralph2020empirical-e81][^ralph2020empirical-e82]。工程论文常用一个"问题"或"目标"来代替研究问题，这是可以的[^ralph2020empirical-e96]。
2. **说清贡献是什么类型的成果。** 是一种技术（必须是可操作的过程，而不是建议或指导原则），还是体现某种技术的工具[^shaw2003writing-e27]？
3. **具体写出你比谁好、好在哪里。** 说清你建立在哪些工作之上、替代了什么、和它们相比有什么不同[^shaw2003writing-e34]。最好的写法是逐个说出已有工作做到了什么、有什么限制，再说你在哪一点上超过了它们，例如"A 达到 60% 覆盖率；B 达到 80%，但只适用于无指针的情况；我们达到 90%，并放宽了限制"[^shaw2003writing-e3]。

**新颖性不等于复杂。** 审稿人常把复杂、困难、技术性强误当成新颖[^black2022novelty-e1]。只改了一处、但以前没人想到这样改，本身就是新颖的[^black2022novelty-e2]；新数据集、旧方法的新用法也可以是新颖的[^black2022novelty-e4]。一个简单的想法如果比当前最好的方法效果更好，多半不平凡[^black2022novelty-e7]。SIGSOFT 标准也明确说："技术上不复杂"不是成立的批评，重要的是有效，不必要的复杂反而不好[^ralph2020empirical-e96]。

**不必是第一个解法，但要在某个维度上胜出。** 新制品要在某些维度上胜过已有制品，例如可扩展性、某类问题上的性能、对真实系统的适用性、理论保证[^ralph2020empirical-e95]。

**容易错在哪：**

- **夸大新颖性**[^ralph2020empirical-e91]。新颖性怎么判断，见通用篇[审稿与发表](../../../general/3_after/02_reviewing_and_publishing.md)第 4 节。
- **只讲实现细节，漏掉关键思路**[^ralph2020empirical-e91]。描述制品时要讲清整体流程、各部分如何配合，并**把新的部分明确标出来**[^ralph2020empirical-e83]。

### 第 2 步：把贡献写成可以检验的主张

主张必须写明确，读者才能判断实验是否支持它[^blackburn2018sigplan-e1]。

**怎么做** `[本项目分析]`：把每条贡献写成一句可检验的话，并标明它属于哪个维度。工程研究的主张通常落在下面几个维度上：

| 维度 | 主张的例子 | 需要的证据 |
|---|---|---|
| 有效性 | "比 X 多发现 30% 的缺陷" | 和基线在同一组评测对象上比较 |
| 效率与代价 | "运行时开销低于 5%" | 时间、内存等各项代价的测量 |
| 通用性 | "适用于各类 Web 应用" | 多样、有代表性的评测对象 |
| 各部分的必要性 | "组件 A 是提升的关键" | 消融实验 |
| 易用性 | "开发者更快完成任务" | 有人参与的实验或案例研究 |

**再检查主张的强度。** Shaw 建议把主张拆成分句，看每个分句是全称的（"总是"）、有限定的（"提升 25%"）还是存在性的（"找到一个实例"）：全称主张通常要分析论证，有限定的主张可以靠评估，存在性主张有时一个正例就够[^shaw2003writing-e30]。

**验证要对准主张。** 声称性能提升，就要分析性能，而不是易用性或通用性[^shaw2003writing-e29]。声称达到了某个目标，就必须有实验检验它；系统安全论文中，声称了却没检验的情况并不少见[^vanderkouwe2019sok-e5]。

怎样把主张写进引言和摘要，见通用篇[写作](../../../general/3_after/01_writing.md)第 2 节。

### 第 3 步：为每条主张选对验证方式

好研究不仅要有结果，还要有清楚、令人信服的证据，证据应来自实际经验或系统分析，而不是说服性的论述或教科书式的例子[^shaw2002makes-e7]。

**有哪些验证方式**（据 Shaw 2003 的分类）：

| 方式 | 是什么 | 说服力 |
|---|---|---|
| 分析 | 严格的推导、证明，或精心设计的实验 | 强[^shaw2003writing-e32] |
| 经验 | 成果被**作者以外的人**用在真实例子上[^shaw2003writing-e33] | 强[^shaw2003writing-e32] |
| 评估 | 按事先说明的标准衡量，包括可行性研究、试点项目 | 中 `[本项目分析]` |
| 例子 | 演示它在某个例子上怎么工作 | 取自真实系统的例子较有说服力，玩具例子往往没有[^shaw2003writing-e28] |
| 说服 | "我认真想过，我相信……" | 很少足够[^shaw2003writing-e10] |
| 断言 | 不做任何验证 | 几乎不可能被接受[^shaw2003writing-e37] |

SIGSOFT 标准要求用一种实证方法评估制品，并写明用的是哪一种：研究者带着制品进入真实组织的行动研究、观察真实组织使用制品的案例研究、有人参与的对照实验、在人工环境中评估的定量仿真、基于基准的基准测试，或者另有充分理由的方法[^ralph2020empirical-e84]。此外还要**从概念上**分析制品的长处、短处和局限[^ralph2020empirical-e81]；有理论贡献时，最好给出正确性论证，如定理、复杂度分析或证明[^ralph2020empirical-e88]。

**两个例外：**

- 如果问题本身是"能不能做到"，一个能运行的系统就可能足以回答[^shaw2003writing-e10]。
- 制品越创新、概念分析越全面，对实证部分的要求越低；反过来，**创新程度越低，评估要越严格**[^ralph2020empirical-e94][^ralph2020empirical-e90]。

**容易错在哪**：评估只有用户的主观评价；只有性能数字，却不和公认基准或替代方案比较；没有对照、不重复；用玩具例子评估，还把它称作"案例研究"[^ralph2020empirical-e92][^ralph2020empirical-e93]。

### 第 4 步：选基线

SIGSOFT 标准要求：和当前最好的替代方案或公认基准做实证比较；做不到时，给出清楚、令人信服的理由[^ralph2020empirical-e85]。

**选哪几类基线**（一般三类都要有 `[本项目分析]`）：

1. **最朴素的做法**，例如拿精巧的测试工具和纯随机测试比，看它是否真的更好[^blackburn2018sigplan-e6]。
2. **更简单的方法**，用来证明新方法多出来的复杂度确有必要[^lones2021avoid-e1][^arp2022dos-e1]。
3. **当前最好的方法**[^lones2021avoid-e2][^arp2022dos-e1]。只和自己以前的工作比，不算数[^vanderkouwe2019sok-e4]。

**比较要公平：**

- 不要把很弱的"稻草人"基线说成最先进方法[^blackburn2018sigplan-e4]。
- 给对手同样好的配置。常见的不公平是：对手用非最优配置[^vanderkouwe2019sok-e4]，或对手用最低优化级别编译、自己用最高级别[^blackburn2018sigplan-e5]，或者把自己的参数针对评测集调到最好、和没调参的对手比[^zeller2021devil-e2]。机器学习中就出现过这种情况：一系列被归功于新结构的改进，实际来自更好的调参[^lipton2019troubling-e5]。
- 基线本身要设对。系统安全方向计算开销时，合适的基线通常是默认设置、不加任何防御的原始系统[^vanderkouwe2019sok-e14]。
- **安全方向**：评估防御手段时，对手是会针对你的防御调整策略的攻击者。要问"什么攻击可能攻破它"，并证明这些攻击都无效；只用默认参数跑现成攻击是不够的[^carlini2019evaluating-e1]。

**这些情况可以不比**：对方方法拿不到或跑不起来时，没和它比较不算缺陷[^ralph2020empirical-e95]。但要在论文里说明。

基线的一般原则，见通用篇[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)第 2 节。

### 第 5 步：选基准和评测对象

**基准**（benchmark）是一组公认的评测对象和测量方法，例如一组程序、数据集或工作负载。

**怎么做：**

1. **用现成基准，要说明为什么选它**（是否相关、是否过时）[^ralph2020empirical-e99]。**新建基准**，要写清测哪种质量、用什么指标、在什么工作负载下测[^ralph2020empirical-e104]。
2. **讨论基准测的是不是你想测的东西**（构念效度）[^ralph2020empirical-e100]。用间接指标时尤其要小心：模糊测试论文常用"不同崩溃数"代替"真实缺陷数"，而前者会严重多算缺陷，表面上的提升可能很小甚至不存在[^klees2018evaluating-e4]。引入新指标，要精确定义并说明它比已有指标好[^shaw2003writing-e36]。
3. **评测对象要多样、有代表性，不要只挑对自己有利的。** 一个已发表的模糊测试工具在原论文选的程序上表现好，换成别的论文用过的两个程序，就不比基线好了[^klees2018evaluating-e3]。随意挑一部分基准子项、却当作整体结果报告，是一种缺陷[^vanderkouwe2019sok-e3]。
4. **用接近实际的评测对象。** 只测某个具体操作的微基准，不能代表系统在实际中的速度[^vanderkouwe2019sok-e9]；只在实验室环境中评估、不讨论实际局限，也是常见陷阱[^arp2022dos-e2]。取自真实系统的例子比玩具例子有说服力[^shaw2003writing-e28]；能在广泛使用的开源项目或专业开发者中评估更好[^ralph2020empirical-e88]。
5. **开发时用过的对象不能再拿来评估**[^blackburn2018sigplan-e12][^vanderkouwe2019sok-e10]。

**容易错在哪：**

- **为自己的方法量身定做基准**，或用与问题无关的测试掩盖弱点[^ralph2020empirical-e101]。
- **对基准过拟合。** 一套基准用久了，工具会开始针对它做特殊优化，而这些优化没有根本性的好处[^klees2018evaluating-e7]。

### 第 6 步：设计评估，回答四个问题

**问题一：有效吗？** 在同一组评测对象上和基线比较（第 4、5 步）。如果系统要做判断（例如判断行为是否恶意），必须测误报和漏报；不知道准确率，就无法判断它的价值[^vanderkouwe2019sok-e7]。

**问题二：代价多大？** 先列出方案可能影响的所有性能维度（处理器、并发、内存、磁盘和网络读写等），每个维度至少用一个合适的测试[^vanderkouwe2019sok-e11]。凡是可以合理预期会受影响的操作都要测[^vanderkouwe2019sok-e2]。只测运行时间不够，还要测内存，以及程序体积、预处理时间等代价[^vanderkouwe2019sok-e6]。Zeller 讽刺过一种套路：给简单方法套上庞大的装置（如一个机器学习模型加一个语料库），总能提升一点，于是号称"更好"[^zeller2021devil-e6]。报告提升时，也要报告付出了什么。

**问题三：能推广吗？** 在一个数据集上表现好，不代表在别的数据集上也好[^lones2021avoid-e10]。光是"对你自己有效"不够，还要有证据表明它对别人也有用[^shaw2003writing-e35]。

**问题四：每个部分都必要吗？** 用消融实验逐个去掉组成部分。同时提出很多改动却不做消融，就看不出提升从哪里来，有时真正起作用的只有一个[^lipton2019troubling-e4]。如果比别人快只是因为实现得更好，而不是因为新设计，新颖性就值得怀疑[^vanderkouwe2019sok-e8]。不只问"效果有多好"，还要问"什么起了作用、为什么"[^lipton2019troubling-e7]。消融做不了时怎么办，见通用篇[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)第 3 节的"不同的看法"。

**别忘了随机性和运行条件。** 要有足够的重复次数和运行时长来检验结果是否稳定[^ralph2020empirical-e99]；保存全部原始结果，而不只是汇总数字[^ralph2020empirical-e101]；不要把 4%、6%、7%、49% 概括成"最高提升 49%"[^blackburn2018sigplan-e9]。重复次数、统计检验和效应量的一般做法，见通用篇第 5 节。

> **一个完整的例子：评估模糊测试工具（安全方向）**
>
> 模糊测试（fuzz testing）是用大量随机生成的输入测试程序、以发现缺陷的技术。Klees 等人指出，评估一个新的模糊测试算法，要选定有说服力的基线、一组评测程序、性能指标和有意义的配置参数（如初始输入和运行时长），并考虑随机性[^klees2018evaluating-e1]。他们检查了 32 篇论文，**每一篇的评估都有问题**[^klees2018evaluating-e2]。他们自己的实验表明：
>
> - 同样的配置，每次运行的结果差别很大[^klees2018evaluating-e9]，只比一次会得出错误结论；
> - 性能随运行时间变化，运行太短可能得出误导性的结论[^klees2018evaluating-e6]；
> - 换一组评测程序，原来的优势就消失了[^klees2018evaluating-e3]；
> - 常用指标会严重多算缺陷[^klees2018evaluating-e4]。
>
> 他们的建议是：多次运行并做统计检验；用一系列已知缺陷的评测程序；考虑多种有记录的初始输入；运行至少 24 小时或说明理由，并画出随时间的变化[^klees2018evaluating-e5]。其他方向的具体参数不同，但"基线、评测对象、指标、配置、随机性"这五项选择，是每个工程研究评估都要逐一想清楚的 `[本项目分析]`。

> **不同的看法：评估要做到多大规模？**
> - SIGSOFT 标准认为，不应要求工程论文的实证部分像纯实证论文那样宏大；评测对象少，如果该领域本来就少，或者实验只是整体验证的一部分，也不算缺陷[^ralph2020empirical-e94]。
> - 另一方面，对具体方向的调查显示评估问题非常普遍：模糊测试论文无一例外都有问题[^klees2018evaluating-e2]；系统安全顶会的防御论文平均每篇有 5 个基准测试缺陷，50 篇中只有 1 篇没有[^vanderkouwe2019sok-e1]。
>
> 两者并不矛盾。SIGSOFT 说的是"规模"可以小，调查批评的是"做法"不对：基线不公平、评测对象挑过、不重复、指标不对。实际操作中，规模可以按资源和创新程度调整（创新越少，越要严格[^ralph2020empirical-e90]），但公平比较、多次运行、说明选择理由这些做法不能省。van der Kouwe 等人也指出，很多缺陷只需很少的额外工作就能避免[^vanderkouwe2019sok-e12]。

### 第 7 步：写出真正的局限和效度威胁

**怎么做：**

- **从概念上讨论制品的长处、短处和局限**，这是必须项[^ralph2020empirical-e81]。
- **写明所有假设**，它们要合理、彼此不矛盾，也不和贡献的目标矛盾[^ralph2020empirical-e86]。
- **披露所有主要局限**[^ralph2020empirical-e103]。只写无关紧要的、漏掉真正相关的，会让读者得出过强的结论[^blackburn2018sigplan-e3]。反面做法是"成果写进标题，局限藏进脚注"[^zeller2021devil-e3]。

**工程研究常见的真实威胁** `[本项目分析]`：

- 实现有错误，测到的不是你设计的方法；
- 基线配置不当，或基线复现得不对；
- 评测对象不够有代表性，或开发时看过；
- 指标不能代表真正关心的质量；
- 测量环境有干扰（其他进程、缓存、硬件差异）。

效度威胁的一般写法，见通用篇[证据、分析与效度](../../../general/2_during/02_evidence_and_validity.md)第 6、7 节。

### 第 8 步：公开研究制品

在 ACM 的定义里，研究**制品**指作者为研究制作的、或实验产生的数字对象，例如软件系统、运行实验的脚本、输入数据、原始实验数据、分析脚本[^acm2020artifact-e1]。结构良好、有文档的制品，让别人能直接在你的工作之上继续做[^acm2020artifact-e8]。

**ACM 的制品徽章**分几个级别，可以当作目标来准备：

| 级别 | 要求 |
|---|---|
| 可获取（Available） | 放到公开的长期存档库，给出 DOI（数字对象标识符，一种永久链接）或带唯一标识的链接；个人网页不算[^acm2020artifact-e4] |
| 已评估–可运行（Functional） | 有文档、与论文一致、完整、能运行，并附有验证的证据[^acm2020artifact-e2] |
| 已评估–可复用（Reusable） | 在可运行之上，文档细致、结构良好，便于他人复用和改作他用[^acm2020artifact-e3] |
| 结果已复现 / 已重现（Reproduced / Replicated） | 他人用你的制品得到了主要结果 / 他人不用你的制品独立得到了主要结果[^acm2020artifact-e5] |

**怎么做：**

- 提供源代码（或对非软件制品的完整描述）和输入数据[^ralph2020empirical-e87]。
- 写清复现所需的信息：硬件平台、软件版本、各子项结果、绝对数字而不只是相对数字[^vanderkouwe2019sok-e13]；带随机性的方法，说明初始输入或种子怎么得到，最好一并公开[^klees2018evaluating-e8]。
- 有专有部分不能公开时，写明它是什么、怎么获取[^acm2020artifact-e6]；复现包里缺了什么，从实际或伦理角度说明原因[^ralph2020empirical-e87]。有清楚、令人信服的原因时，不提供复现包不算缺陷[^ralph2020empirical-e97]。
- 不能公开时，"已评估"徽章仍然可以申请：只需要提供给评审人[^acm2020artifact-e7]。

目录结构、版本控制和 README（项目说明文件）怎么写，见通用篇[整理科研材料](../../../general/2_during/03_organizing_materials.md)。

---

## 3. 检查清单

下面主要依据 ACM SIGSOFT 的工程研究标准，评估部分补充了基准测试标准。

**必须做到**

- [ ] 足够详细地描述制品，并说明为什么需要它[^ralph2020empirical-e81]
- [ ] 讲清整体流程，把新的部分明确标出来[^ralph2020empirical-e83]
- [ ] 从概念上讨论制品的长处、短处和局限[^ralph2020empirical-e81]
- [ ] 用某种实证方法评估，并写明用的是哪一种[^ralph2020empirical-e84]
- [ ] 讨论当前最好的替代方案；和它们或公认基准做实证比较，做不到时说明理由[^ralph2020empirical-e85]
- [ ] 写明假设，假设合理且不互相矛盾[^ralph2020empirical-e86]
- [ ] 说明为什么选这个基准；讨论它测的是不是你想测的东西[^ralph2020empirical-e99][^ralph2020empirical-e100]
- [ ] 让各方配置凭实力公平竞争；有足够的重复次数和运行时长[^ralph2020empirical-e99]
- [ ] 披露所有主要局限[^ralph2020empirical-e103]

**做到更好**

- [ ] 提供源代码和输入数据；缺什么说明原因[^ralph2020empirical-e87]
- [ ] 讨论制品的理论基础；为关键理论贡献给出正确性论证[^ralph2020empirical-e88]
- [ ] 用贯穿全文的例子讲解制品[^ralph2020empirical-e88]
- [ ] 在贴近实际的环境中评估，如广泛使用的开源项目、专业开发者[^ralph2020empirical-e88]

**做得出色**

- [ ] 加深了大家对设计原则的理解[^ralph2020empirical-e89]
- [ ] 带来有明显实际好处的突破[^ralph2020empirical-e89]

**这些情况可以不做，不算缺陷**

- 没写明研究问题：工程论文常用"问题"或"目标"代替[^ralph2020empirical-e96]
- 没和拿不到、跑不起来的方法比较[^ralph2020empirical-e95]
- 有清楚的实际或伦理原因时，不提供复现包[^ralph2020empirical-e97]

**审稿时常见、但不成立的批评**：你不必为此担心

- "实证部分不如纯实证论文宏大""评测对象太少"（该领域本来就少，或实验只是整体验证的一部分时）[^ralph2020empirical-e94]
- "这不是该问题的第一个解法"：只要在某个维度上胜过已有方法即可[^ralph2020empirical-e95]
- "技术上不够复杂"[^ralph2020empirical-e96]
- "这个基准用的人不多"：新基准可以先由一小群研究者提出[^ralph2020empirical-e102]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 夸大新颖性，或把复杂当新颖 | 新颖不等于复杂；夸大会失去审稿人的信任[^ralph2020empirical-e91][^black2022novelty-e1] |
| 只讲实现细节，不讲关键思路 | 读者看不出新在哪里[^ralph2020empirical-e91] |
| 只有性能数字，没有比较 | 数字孤立地看没有意义[^ralph2020empirical-e92] |
| 弱基线、只和自己以前的工作比 | 夸大新方法的好处[^blackburn2018sigplan-e4][^vanderkouwe2019sok-e4] |
| 自己精心调参，对手用默认配置 | 比较不公平，提升可能来自调参[^zeller2021devil-e2][^lipton2019troubling-e5] |
| 挑选对自己有利的评测对象或基准子项 | 换一组对象，优势可能消失[^klees2018evaluating-e3][^vanderkouwe2019sok-e3] |
| 用玩具例子评估，称作"案例研究" | 说服不了别人[^ralph2020empirical-e93][^shaw2003writing-e28] |
| 用间接指标却不论证 | 指标可能严重夸大效果[^klees2018evaluating-e4] |
| 只测一次 | 一次运行的结果可能完全相反[^klees2018evaluating-e9][^ralph2020empirical-e93] |
| 只报提升，不报代价 | 读者无法判断是否值得用[^vanderkouwe2019sok-e6][^zeller2021devil-e6] |
| 不做消融 | 不知道哪个部分起作用，甚至不知道新设计是否有用[^lipton2019troubling-e4][^vanderkouwe2019sok-e8] |
| 声称了却没检验 | 主张没有证据[^vanderkouwe2019sok-e5] |
| 局限藏起来 | 读者得出过强的结论[^blackburn2018sigplan-e3][^zeller2021devil-e3] |
| 不写平台、版本、种子 | 别人无法复现[^vanderkouwe2019sok-e13][^klees2018evaluating-e8] |

---

## 5. 延伸阅读

- **整体框架**：Shaw 2003《Writing Good Software Engineering Research Papers》，用研究问题、成果、验证三张表讲清"一篇工程论文该回答什么"；Shaw 2002 是它的期刊版。
- **检查清单**：ACM SIGSOFT 实证研究标准中的工程研究标准和基准测试标准；SIGPLAN（美国计算机协会编程语言分会）实证评估清单（偏程序语言和系统方向）。
- **一个方向怎样系统地反思自己的评估**：Klees 等人 2018（模糊测试）；van der Kouwe 等人 2019（系统安全，列出 22 种基准测试缺陷）；Carlini 等人 2019（对抗样本防御）；Arp 等人 2022（机器学习用于安全）。即使不做这些方向，也值得读一篇，看看评估会在哪些地方出错。
- **评估的反面教材**：Zeller 2021《The Devil's Guide to Incremental Research》，用反讽列出凑论文的套路。
- **制品公开**：ACM 制品评审与徽章政策。
- **信息系统领域的"设计科学"方法论**（如 Hevner 等人 2004、Peffers 等人 2007）本文没有引用，因为没有找到确定合法的开放获取全文 `[待确认]`。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^ralph2020empirical-e79]: SIGSOFT 工程研究标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e79)
[^ralph2020empirical-e80]: SIGSOFT 工程研究标准，适用范围。[证据](../../../../sources/notes/ralph2020empirical.md#e80)
[^ralph2020empirical-e81]: SIGSOFT 工程研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e81)
[^ralph2020empirical-e82]: SIGSOFT 工程研究标准，脚注 2。[证据](../../../../sources/notes/ralph2020empirical.md#e82)
[^ralph2020empirical-e83]: SIGSOFT 工程研究标准，脚注 1。[证据](../../../../sources/notes/ralph2020empirical.md#e83)
[^ralph2020empirical-e84]: SIGSOFT 工程研究标准，必要项（方法）。[证据](../../../../sources/notes/ralph2020empirical.md#e84)
[^ralph2020empirical-e85]: SIGSOFT 工程研究标准，必要项（方法）。[证据](../../../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e86]: SIGSOFT 工程研究标准，必要项（其他）。[证据](../../../../sources/notes/ralph2020empirical.md#e86)
[^ralph2020empirical-e87]: SIGSOFT 工程研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e87)
[^ralph2020empirical-e88]: SIGSOFT 工程研究标准，加分项。[证据](../../../../sources/notes/ralph2020empirical.md#e88)
[^ralph2020empirical-e89]: SIGSOFT 工程研究标准，优秀项。[证据](../../../../sources/notes/ralph2020empirical.md#e89)
[^ralph2020empirical-e90]: SIGSOFT 工程研究标准，总体质量标准。[证据](../../../../sources/notes/ralph2020empirical.md#e90)
[^ralph2020empirical-e91]: SIGSOFT 工程研究标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e91)
[^ralph2020empirical-e92]: SIGSOFT 工程研究标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e92)
[^ralph2020empirical-e93]: SIGSOFT 工程研究标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e93)
[^ralph2020empirical-e94]: SIGSOFT 工程研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e94)
[^ralph2020empirical-e95]: SIGSOFT 工程研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e95)
[^ralph2020empirical-e96]: SIGSOFT 工程研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e96)
[^ralph2020empirical-e97]: SIGSOFT 工程研究标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e97)
[^ralph2020empirical-e98]: SIGSOFT 工程研究标准，脚注 4。[证据](../../../../sources/notes/ralph2020empirical.md#e98)
[^ralph2020empirical-e99]: SIGSOFT 基准测试标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e99)
[^ralph2020empirical-e100]: SIGSOFT 基准测试标准，必要项（讨论）。[证据](../../../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e101]: SIGSOFT 基准测试标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e101)
[^ralph2020empirical-e102]: SIGSOFT 基准测试标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e102)
[^ralph2020empirical-e103]: SIGSOFT General Standard，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e103)
[^ralph2020empirical-e104]: SIGSOFT 基准测试标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e104)
[^shaw2003writing-e25]: Shaw 2003，§2.1，表 1。[证据](../../../../sources/notes/shaw2003writing.md#e25)
[^shaw2003writing-e26]: Shaw 2003，§3.2。[证据](../../../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e27]: Shaw 2003，§3.1，表 3。[证据](../../../../sources/notes/shaw2003writing.md#e27)
[^shaw2003writing-e28]: Shaw 2003，§4.1，表 5。[证据](../../../../sources/notes/shaw2003writing.md#e28)
[^shaw2003writing-e10]: Shaw 2003，§4.1，表 5 后。[证据](../../../../sources/notes/shaw2003writing.md#e10)
[^shaw2003writing-e29]: Shaw 2003，§4.3。[证据](../../../../sources/notes/shaw2003writing.md#e29)
[^shaw2003writing-e30]: Shaw 2003，§5。[证据](../../../../sources/notes/shaw2003writing.md#e30)
[^shaw2003writing-e3]: Shaw 2003，§3.3。[证据](../../../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e31]: Shaw 2003，§2.3。[证据](../../../../sources/notes/shaw2003writing.md#e31)
[^shaw2003writing-e32]: Shaw 2003，§4.2。[证据](../../../../sources/notes/shaw2003writing.md#e32)
[^shaw2003writing-e33]: Shaw 2003，§4.1，表 5。[证据](../../../../sources/notes/shaw2003writing.md#e33)
[^shaw2003writing-e34]: Shaw 2003，§1。[证据](../../../../sources/notes/shaw2003writing.md#e34)
[^shaw2003writing-e35]: Shaw 2003，§4.3。[证据](../../../../sources/notes/shaw2003writing.md#e35)
[^shaw2003writing-e36]: Shaw 2003，§3.3。[证据](../../../../sources/notes/shaw2003writing.md#e36)
[^shaw2003writing-e37]: Shaw 2003，§4.1，表 5。[证据](../../../../sources/notes/shaw2003writing.md#e37)
[^shaw2002makes-e7]: Shaw 2002，§2.3。[证据](../../../../sources/notes/shaw2002makes.md#e7)
[^black2022novelty-e1]: Black 2022，开头。[证据](../../../../sources/notes/black2022novelty.md#e1)
[^black2022novelty-e2]: Black 2022，Novelty as complexity。[证据](../../../../sources/notes/black2022novelty.md#e2)
[^black2022novelty-e4]: Black 2022，Novelty as technical novelty。[证据](../../../../sources/notes/black2022novelty.md#e4)
[^black2022novelty-e7]: Black 2022，Novelty as difficulty。[证据](../../../../sources/notes/black2022novelty.md#e7)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019，§3.2。[证据](../../../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e5]: Lipton & Steinhardt 2019，§3.2。[证据](../../../../sources/notes/lipton2019troubling.md#e5)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019，§5.1。[证据](../../../../sources/notes/lipton2019troubling.md#e7)
[^lones2021avoid-e1]: Lones 2021，§5.2。[证据](../../../../sources/notes/lones2021avoid.md#e1)
[^lones2021avoid-e2]: Lones 2021，§5.2。[证据](../../../../sources/notes/lones2021avoid.md#e2)
[^lones2021avoid-e10]: Lones 2021，§6.3。[证据](../../../../sources/notes/lones2021avoid.md#e10)
[^blackburn2018sigplan-e1]: SIGPLAN 实证评估清单，Clearly Stated Claims。[证据](../../../../sources/notes/blackburn2018sigplan.md#e1)
[^blackburn2018sigplan-e4]: SIGPLAN 实证评估清单，Suitable Comparison。[证据](../../../../sources/notes/blackburn2018sigplan.md#e4)
[^blackburn2018sigplan-e5]: SIGPLAN 实证评估清单，Suitable Comparison。[证据](../../../../sources/notes/blackburn2018sigplan.md#e5)
[^blackburn2018sigplan-e6]: SIGPLAN 实证评估清单，Notes。[证据](../../../../sources/notes/blackburn2018sigplan.md#e6)
[^blackburn2018sigplan-e12]: SIGPLAN 实证评估清单，Tested on training set。[证据](../../../../sources/notes/blackburn2018sigplan.md#e12)
[^blackburn2018sigplan-e9]: SIGPLAN 实证评估清单，Misleading summary of results。[证据](../../../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e3]: SIGPLAN 实证评估清单，Fails to acknowledge limitations。[证据](../../../../sources/notes/blackburn2018sigplan.md#e3)
[^zeller2021devil-e2]: Zeller 2021，THE AUTOTUNE。[证据](../../../../sources/notes/zeller2021devil.md#e2)
[^zeller2021devil-e6]: Zeller 2021，THE RUBE GOLDBERG。[证据](../../../../sources/notes/zeller2021devil.md#e6)
[^zeller2021devil-e3]: Zeller 2021，THE ACHILLES HEEL。[证据](../../../../sources/notes/zeller2021devil.md#e3)
[^klees2018evaluating-e1]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e1)
[^klees2018evaluating-e2]: Klees 等人 2018，摘要。[证据](../../../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e4]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e4)
[^klees2018evaluating-e5]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e5)
[^klees2018evaluating-e6]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e6)
[^klees2018evaluating-e7]: Klees 等人 2018，§8。[证据](../../../../sources/notes/klees2018evaluating.md#e7)
[^klees2018evaluating-e8]: Klees 等人 2018，§5。[证据](../../../../sources/notes/klees2018evaluating.md#e8)
[^klees2018evaluating-e9]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e9)
[^vanderkouwe2019sok-e1]: van der Kouwe 等人 2019，摘要。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e1)
[^vanderkouwe2019sok-e2]: van der Kouwe 等人 2019，§II-A。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e2)
[^vanderkouwe2019sok-e3]: van der Kouwe 等人 2019，§II-A。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e3)
[^vanderkouwe2019sok-e4]: van der Kouwe 等人 2019，§II-D。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e5]: van der Kouwe 等人 2019，§II-E。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e5)
[^vanderkouwe2019sok-e6]: van der Kouwe 等人 2019，附录 E2。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e6)
[^vanderkouwe2019sok-e7]: van der Kouwe 等人 2019，§II-E。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e7)
[^vanderkouwe2019sok-e8]: van der Kouwe 等人 2019，§II-E。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e8)
[^vanderkouwe2019sok-e9]: van der Kouwe 等人 2019，§II-B。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e9)
[^vanderkouwe2019sok-e10]: van der Kouwe 等人 2019，§II-C。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e10)
[^vanderkouwe2019sok-e11]: van der Kouwe 等人 2019，§VI。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e11)
[^vanderkouwe2019sok-e12]: van der Kouwe 等人 2019，§I。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e12)
[^vanderkouwe2019sok-e13]: van der Kouwe 等人 2019，表 I。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e13)
[^vanderkouwe2019sok-e14]: van der Kouwe 等人 2019，§II-D。[证据](../../../../sources/notes/vanderkouwe2019sok.md#e14)
[^acm2020artifact-e1]: ACM 制品评审与徽章政策 v1.1，开头。[证据](../../../../sources/notes/acm2020artifact.md#e1)
[^acm2020artifact-e2]: ACM 制品评审与徽章政策 v1.1，Artifacts Evaluated – Functional。[证据](../../../../sources/notes/acm2020artifact.md#e2)
[^acm2020artifact-e3]: ACM 制品评审与徽章政策 v1.1，Artifacts Evaluated – Reusable。[证据](../../../../sources/notes/acm2020artifact.md#e3)
[^acm2020artifact-e4]: ACM 制品评审与徽章政策 v1.1，Artifacts Available。[证据](../../../../sources/notes/acm2020artifact.md#e4)
[^acm2020artifact-e5]: ACM 制品评审与徽章政策 v1.1，Results Validated。[证据](../../../../sources/notes/acm2020artifact.md#e5)
[^acm2020artifact-e6]: ACM 制品评审与徽章政策 v1.1，Functional 级别注释。[证据](../../../../sources/notes/acm2020artifact.md#e6)
[^acm2020artifact-e7]: ACM 制品评审与徽章政策 v1.1，Artifacts Evaluated。[证据](../../../../sources/notes/acm2020artifact.md#e7)
[^acm2020artifact-e8]: ACM 制品评审与徽章政策 v1.1，开头。[证据](../../../../sources/notes/acm2020artifact.md#e8)
[^carlini2019evaluating-e1]: Carlini 等人 2019，§2.5。[证据](../../../../sources/notes/carlini2019evaluating.md#e1)
[^arp2022dos-e1]: Arp 等人 2022，P6。[证据](../../../../sources/notes/arp2022dos.md#e1)
[^arp2022dos-e2]: Arp 等人 2022，P9。[证据](../../../../sources/notes/arp2022dos.md#e2)
