# 工程研究：提出并评估新的方法、工具或系统

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲计算机领域最常见的一类研究：**提出一个新的技术、算法、工具或系统，并证明它有效**。

**适用范围** `[本项目分析]`：这是计算机里"构建改进"这种研究套路的具体做法，例子和标准主要来自软件工程、系统、安全和机器学习。这类研究产生什么知识、审稿人要看到哪些证据、为什么要尽早跑基线、主张和证据怎样对应，这些各学科通用的部分见[构建改进](../../../05_research-strategies/build_improve.md)，本文不重复，只写计算机特有的部分：软件工程评审标准的具体要求、基线和基准在各方向的选法、评估代价的惯例、研究制品的公开和评估。其他通用内容：效度威胁见[效度与局限](../../../02_from-project-to-study/03_validity-and-limits.md)；多次运行和随机种子见[比较评估：差异是不是真的](../../../05_research-strategies/compare_evaluate.md#差异是不是真的)，统计的一般做法见[分析与解读：报告差多少、有多确定，而不只是 p 值](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)；论文怎么写见[讲清故事，写成论文](../../../04_write-and-publish/01_story-and-paper.md)；代码和数据怎么整理见[整理科研材料](../../../08_throughout/organizing_materials.md)。如果你只是系统地比较一批现有工具或模型，而不提出新方法，那是[基准评测](benchmarking.md)。

**读完本文，你应该能：**

- 判断自己的研究是不是工程研究，说清"新在哪里、比谁好"；
- 把贡献写成可以检验的主张，并为每条主张选对验证方式；
- 选出站得住的基线和基准，设计一套覆盖有效性、代价、通用性和各部分必要性的评估；
- 写出真正的效度威胁，并按社区通行的标准公开研究制品；
- 用文末的检查清单检查自己的论文。

---

## 1. 这是什么研究，什么时候用

这类研究产生什么知识、回答什么样的问题、和比较评估或经验报告怎么分，见[构建改进](../../../05_research-strategies/build_improve.md#1-这类研究产生什么知识)。下文常引用的 ACM SIGSOFT（美国计算机协会软件工程分会）实证研究标准（软件工程界按研究方法给出的论文评审标准，下称 SIGSOFT 标准），把它叫作"工程研究"，定义是"发明并评估技术制品的研究"[^ralph2020empirical-e79]。在软件工程顶会 ICSE 上，报告一种新技术的论文是最常见的一类[^shaw2003writing-e26]。系统、安全、程序语言、机器学习等方向的大多数论文也属于这一类 `[本项目分析]`。

审稿人要能一眼看出你做的是哪一种：提出了新技术并演示，还是把以前的技术用在新例子上，还是评估一项成熟技术。看不出来，就是没写清楚[^shaw2003writing-e31]。

> **关于名称**：你还会看到"设计科学"（design science）这个叫法。SIGSOFT 标准的作者认为，信息系统领域约 2004 年借用了"设计科学"这个词，用法不当；他们主张叫"工程研究"[^ralph2020empirical-e98]。

---

## 2. 怎么做

### 第 1 步：说清问题，以及"新在哪里、比谁好"

先讲问题再讲方案、逐个说清你比最接近的工作好在哪、新颖不等于复杂，这些通用做法见[构建改进](../../../05_research-strategies/build_improve.md#2-什么样的证据才够)。工程研究里还要写清两点：

1. **贡献是什么类型的成果。** 是一种技术（必须是可操作的过程，而不是建议或指导原则），还是体现某种技术的工具[^shaw2003writing-e27]？
2. **在哪个维度上胜过已有制品。** 说清你建立在哪些工作之上、替代了什么、和它们相比有什么不同[^shaw2003writing-e34]。SIGSOFT 标准举的维度有可扩展性、某类问题上的性能、对真实系统的适用性、理论保证[^ralph2020empirical-e95]。

审稿人怎样判断新颖性，见[当审稿人](../../../08_throughout/being_a_reviewer.md#4-按它的套路评判它)。

**容易错在哪**：夸大新颖性；只讲实现细节，漏掉关键思路[^ralph2020empirical-e91]。描述制品时要讲清整体流程、各部分如何配合，并**把新的部分明确标出来**[^ralph2020empirical-e83]。

### 第 2 步：把贡献写成可以检验的主张

主张必须写明确，读者才能判断实验是否支持它[^blackburn2018sigplan-e1]。

**怎么做** `[本项目分析]`：把每条贡献写成一句可检验的话，并标明它属于哪个维度。工程研究的主张通常落在下面几个维度上：

| 维度 | 主张的例子 | 需要的证据 |
|---|---|---|
| 有效性 | "比 X 多发现 30% 的缺陷" | 和基线在同一组评测对象上比较 |
| 效率与代价 | "运行时开销低于 5%" | 时间、内存等各项代价的测量 |
| 通用性 | "适用于各类 Web 应用" | 多样、有代表性的评测对象 |
| 各部分的必要性 | "组件 A 是提升的关键" | 消融实验（逐个去掉方法的组成部分，看效果变化） |
| 易用性 | "开发者更快完成任务" | 有人参与的实验或案例研究 |

**再检查主张的强度，让验证对准主张。** 主张说得多满、证据就要多硬，声称性能提升就要分析性能，这两条规则见[构建改进](../../../05_research-strategies/build_improve.md#2-什么样的证据才够)。系统安全方向，van der Kouwe 等人把"声称达到了某个目标、却没用实验检验"列为一种基准评测缺陷[^vanderkouwe2019sok-e5]。怎样把主张写进引言和摘要，见[讲清故事，写成论文](../../../04_write-and-publish/01_story-and-paper.md#4-引言五个问题加一份贡献清单)。

### 第 3 步：为每条主张选对验证方式

Shaw 2003 把软件工程论文的验证方式分成下面几类：

| 方式 | 是什么 | 说服力 |
|---|---|---|
| 分析 | 严格的推导、证明，或精心设计的实验 | 强[^shaw2003writing-e32] |
| 经验 | 成果被**作者以外的人**用在真实例子上[^shaw2003writing-e33] | 强[^shaw2003writing-e32] |
| 评估 | 按事先说明的标准衡量，包括可行性研究、试点项目 | 中 `[本项目分析]` |
| 例子 | 演示它在某个例子上怎么工作 | 取自真实系统的例子较有说服力，玩具例子往往没有[^shaw2003writing-e28] |
| 说服 | "我认真想过，我相信……" | 很少足够[^shaw2003writing-e10] |
| 断言 | 不做任何验证 | 几乎不可能被接受[^shaw2003writing-e37] |

SIGSOFT 标准要求用一种实证方法评估制品，并写明用的是哪一种[^ralph2020empirical-e84]：

- 行动研究：研究者带着制品进入真实组织；
- 基于一个或多个基准的评估；
- 其他方法，但要给出清楚、令人信服的理由；
- 有人参与的对照实验、定量仿真等，也是常见的实证评估方式 `[本项目分析]`。

此外还要**从概念上**分析制品的长处、短处和局限[^ralph2020empirical-e81]；有理论贡献时，最好给出正确性论证，如定理、复杂度分析或证明[^ralph2020empirical-e88]。

问题本身是"能不能做到"时，或者制品很有创新时，对实证部分的要求会不同，这两个例外见[构建改进](../../../05_research-strategies/build_improve.md#2-什么样的证据才够)。

**容易错在哪**：评估只有用户的主观评价；只有性能数字，却不和替代方案比较；没有对照、不重复；用玩具例子评估，还把它称作"案例研究"[^ralph2020empirical-e92][^ralph2020empirical-e93]。

### 第 4 步：选基线

要和当前最好的替代方案比，基线至少有哪几类，见[构建改进](../../../05_research-strategies/build_improve.md#尽早把基线跑起来)；怎样给对手同样好的配置，见[比较评估](../../../05_research-strategies/compare_evaluate.md#对手是否被同等对待)。SIGSOFT 标准还说明：对方方法拿不到或跑不起来时，没和它比较不算缺陷[^ralph2020empirical-e95]，但要在论文里说明。工程研究里还要注意：

- **只和自己以前的工作比，不算数**；给对手用非最优配置，也是常见缺陷[^vanderkouwe2019sok-e4]。
- **基线本身要设对。** 系统安全方向计算开销时，合适的基线通常是默认设置、不加任何防御的原始系统[^vanderkouwe2019sok-e14]。
- **对手会主动适应。** 评估对抗样本防御（以及其他面对主动攻击者的防御）时，要问"什么攻击可能攻破它"，并证明这些攻击都无效；只用默认参数跑现成攻击是不够的[^carlini2019evaluating-e1]。

### 第 5 步：选基准和评测对象

**基准**（benchmark）是一组公认的评测对象和测量方法，例如一组程序、数据集或工作负载。怎样选基准、怎样做测量，[基准评测](benchmarking.md)一文讲得更全；这里只列提出新方法时最常出问题的几点。

1. **用现成基准，要说明为什么选它**（是否相关、是否过时）[^ralph2020empirical-e99]。**新建基准**，要写清测哪种质量、用什么指标、在什么工作负载下测[^ralph2020empirical-e104]。
2. **讨论基准测的是不是你想测的东西**（构念效度）[^ralph2020empirical-e100]。用间接指标时尤其要小心：模糊测试（用大量自动生成的输入测试程序、以发现缺陷的技术）论文常用"不同崩溃数"代替"真实缺陷数"，而前者会严重多算缺陷，表面上的提升可能很小甚至不存在[^klees2018evaluating-e4]。引入新指标，要精确定义并说明它比已有指标好[^shaw2003writing-e36]。
3. **评测对象要多样、有代表性，不要只挑对自己有利的。** 一个已发表的模糊测试工具在原论文选的程序上表现好，换成别的论文用过的两个程序，就不比基线好了[^klees2018evaluating-e3]。随意挑一部分基准子项、却当作整体结果报告，是一种缺陷[^vanderkouwe2019sok-e3]。
4. **用接近实际的评测对象。** 只测某个具体操作的微基准，不能代表系统在实际中的速度[^vanderkouwe2019sok-e9]；在机器学习用于安全的研究中，只在实验室环境中评估、不讨论实际局限，是常见陷阱[^arp2022dos-e2]。能在广泛使用的开源项目或专业开发者中评估更好[^ralph2020empirical-e88]。
5. **开发时用过的对象不能再拿来评估**[^blackburn2018sigplan-e12][^vanderkouwe2019sok-e10]。道理见[比较评估：留一份数据只用于最后检验](../../../05_research-strategies/compare_evaluate.md#留一份数据只用于最后检验)。

**容易错在哪：** 为自己的方法量身定做基准，或用与问题无关的测试掩盖弱点[^ralph2020empirical-e101]；一套基准用久了，工具会开始针对它做特殊优化，而这些优化没有根本性的好处[^klees2018evaluating-e7]。

### 第 6 步：设计评估，回答四个问题

**问题一：有效吗？** 在同一组评测对象上和基线比较（第 4、5 步）。如果系统要做判断，必须报告它的准确率；不知道准确率，就无法判断它的价值[^vanderkouwe2019sok-e7]（例如判断行为是否恶意时，要测误报和漏报 `[本项目分析]`）。

**问题二：代价多大？** 先列出方案可能影响的所有性能维度（处理器、并发、内存、磁盘和网络读写等），每个维度至少用一个合适的测试[^vanderkouwe2019sok-e11]。凡是可以合理预期会受影响的操作都要测[^vanderkouwe2019sok-e2]。只测运行时间不够，还要测内存，以及程序体积、预处理时间等代价[^vanderkouwe2019sok-e6]。Zeller 讽刺过一种套路：给简单方法套上庞大的装置（如一个机器学习模型加一个语料库），总能提升一点，于是号称"更好"[^zeller2021devil-e6]。

**问题三：能推广吗？** 在一个数据集上好、只对你自己有效都不够，见[构建改进](../../../05_research-strategies/build_improve.md#2-什么样的证据才够)。在计算机里，通常靠多个基准、多种评测对象来回答（第 5 步） `[本项目分析]`。

**问题四：每个部分都必要吗？** 用消融实验回答，见[构建改进](../../../05_research-strategies/build_improve.md#2-什么样的证据才够)。工程研究里特别要防的一种情况：如果比别人快只是因为实现得更好，而不是因为新设计，新颖性就值得怀疑[^vanderkouwe2019sok-e8]。

**别忘了重复和运行条件。** 要有足够的重复次数和运行时长来检验结果是否稳定[^ralph2020empirical-e99]；保存全部原始结果，而不只是汇总数字[^ralph2020empirical-e101]。重复次数、统计检验和效应量（差异有多大，而不只是有没有差异）的一般做法，见[分析与解读](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)；测量流程的细节见[基准评测](benchmarking.md#第四步设计测量流程)。

> **例子：评估模糊测试工具（安全方向）。** Klees 等人指出，提出一个新的模糊测试算法，必须选定有说服力的基线、一组评测程序（基准套件）和有意义的配置参数[^klees2018evaluating-e1]。他们检查了 32 篇论文，**每一篇的评估都有问题**[^klees2018evaluating-e2]。他们自己的实验表明：同样配置的多次运行结果差别很大，只跑一次可能得出错误结论[^klees2018evaluating-e9]；运行太短可能得出误导性的结论[^klees2018evaluating-e6]。换到其他方向，具体参数不同，但"基线、评测对象、指标、配置、随机性"这五项选择，是每个工程研究评估都要逐一想清楚的 `[本项目分析]`。

**评估要做到多大规模？** SIGSOFT 标准认为，不应要求工程论文的实证部分像纯实证论文那样宏大；评测对象少，如果该领域本来就少，或者实验只是整体验证的一部分，也不算缺陷[^ralph2020empirical-e94]。但对具体方向的调查显示评估问题非常普遍：系统安全顶会的防御论文平均每篇有 5 个基准评测缺陷，样本中只有 1 篇没有[^vanderkouwe2019sok-e1]。两者并不矛盾 `[本项目分析]`：规模可以按资源和创新程度调整（创新越少，越要严格[^ralph2020empirical-e90]），但公平比较、多次运行、说明选择理由这些做法不能省。很多缺陷只需很少的额外工作就能避免[^vanderkouwe2019sok-e12]。

### 第 7 步：写出真正的局限和效度威胁

- **从概念上讨论制品的长处、短处和局限**，这是必须项[^ralph2020empirical-e81]。
- **写明所有假设**，它们要合理、彼此不矛盾，也不和贡献的目标矛盾[^ralph2020empirical-e86]。
- **披露所有主要局限**[^ralph2020empirical-e103]。只写无关紧要的、漏掉真正相关的，会让读者得出过强的结论[^blackburn2018sigplan-e3]。反面做法是"成果写进标题，局限藏进脚注"[^zeller2021devil-e3]。

工程研究常见的真实威胁有：实现有错误，测到的不是你设计的方法；基线配置不当或复现得不对；评测对象没代表性或开发时看过；指标不能代表真正关心的质量；测量环境有干扰 `[本项目分析]`。效度威胁的一般写法，见[效度与局限](../../../02_from-project-to-study/03_validity-and-limits.md)。

### 第 8 步：公开研究制品

在 ACM 的定义里，研究**制品**指作者为研究制作的、或实验产生的数字对象，例如软件系统、运行实验的脚本、输入数据、原始实验数据、分析脚本[^acm2020artifact-e1]。结构良好、有文档的制品，让别人能直接在你的工作之上继续做[^acm2020artifact-e8]。ACM 的三类制品徽章（制品已评估、制品可获取、结果已验证）可以当作准备的目标，含义见[计算机学科概况](../README.md#制品评估与徽章)。

- 提供源代码（或对非软件制品的完整描述）和输入数据[^ralph2020empirical-e87]。
- 写清复现所需的信息：硬件平台、软件版本、各子项结果、绝对数字而不只是相对数字[^vanderkouwe2019sok-e13]。模糊测试等依赖初始输入的方法，要说明初始输入（seed）怎么得到，最好一并公开[^klees2018evaluating-e8]。随机数种子的记录见[分析与解读](../../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。
- 有专有部分不能公开时，写明它是什么、怎么获取[^acm2020artifact-e6]；复现包里缺了什么，从实际或伦理角度说明原因[^ralph2020empirical-e87]。有清楚、令人信服的原因时，不提供复现包不算缺陷[^ralph2020empirical-e97]。
- 不能公开时，"制品已评估"徽章仍然可以申请：只需要提供给评审人[^acm2020artifact-e7]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 的工程研究标准，评估部分补充了它的基准评测标准。

**必须做到**

- [ ] 足够详细地描述制品，并说明为什么需要它[^ralph2020empirical-e81]
- [ ] 讲清整体流程，把新的部分明确标出来[^ralph2020empirical-e83]
- [ ] 从概念上讨论制品的长处、短处和局限[^ralph2020empirical-e81]
- [ ] 用某种实证方法评估，并写明用的是哪一种[^ralph2020empirical-e84]
- [ ] 和当前最好的替代方案做实证比较，做不到时说明理由[^ralph2020empirical-e85]
- [ ] 写明假设，假设合理且不互相矛盾[^ralph2020empirical-e86]
- [ ] 说明为什么选这个基准；讨论它测的是不是你想测的东西[^ralph2020empirical-e99][^ralph2020empirical-e100]
- [ ] 让各方配置凭实力公平竞争；有足够的重复次数和运行时长[^ralph2020empirical-e99]
- [ ] 披露所有主要局限[^ralph2020empirical-e103]

**做到更好，乃至出色**

- [ ] 提供源代码和输入数据；缺什么说明原因[^ralph2020empirical-e87]
- [ ] 讨论制品的理论基础；为关键理论贡献给出正确性论证[^ralph2020empirical-e88]
- [ ] 用贯穿全文的例子讲解制品[^ralph2020empirical-e88]
- [ ] 在贴近实际的环境中评估，如广泛使用的开源项目、专业开发者[^ralph2020empirical-e88]
- [ ] 加深了大家对设计原则的理解[^ralph2020empirical-e89]
- [ ] 带来有明显实际好处的突破[^ralph2020empirical-e89]

**这些不算缺陷**（SIGSOFT 列出的不成立的批评，你不必为此担心）

- 没写明研究问题：工程论文常用"问题"或"目标"代替[^ralph2020empirical-e96]
- 没和拿不到、跑不起来的方法比较[^ralph2020empirical-e95]
- 有清楚的实际或伦理原因时，不提供复现包[^ralph2020empirical-e97]
- "实证部分不如纯实证论文宏大""评测对象太少"（该领域本来就少，或实验只是整体验证的一部分时）[^ralph2020empirical-e94]
- "技术上不够复杂"[^ralph2020empirical-e96]
- "这个基准用的人不多"：新基准可以先由一小群研究者提出[^ralph2020empirical-e102]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只和自己以前的工作比，或给对手非最优配置 | 夸大新方法的好处[^vanderkouwe2019sok-e4] |
| 只报提升，不报代价 | 读者无法判断是否值得用[^vanderkouwe2019sok-e6][^zeller2021devil-e6] |
| 只跑一次 | 同样配置的多次运行结果差别很大，只跑一次可能得出错误结论[^klees2018evaluating-e9] |
| 不写平台、版本、初始输入 | 别人无法复现[^vanderkouwe2019sok-e13][^klees2018evaluating-e8] |

---

## 5. 延伸阅读

- **整体框架**：Shaw 2003《Writing Good Software Engineering Research Papers》，用研究问题、成果、验证三张表讲清"一篇工程论文该回答什么"；Shaw 2002（STTT）从同样三个维度讨论什么是好的软件工程研究。
- **检查清单**：SIGSOFT 实证研究标准中的工程研究标准和基准评测标准；SIGPLAN（美国计算机协会编程语言分会）实证评估清单（偏程序语言和系统方向）。
- **一个方向怎样系统地反思自己的评估**：Klees 等人 2018（模糊测试）；van der Kouwe 等人 2019（系统安全，列出 22 种基准评测缺陷）；Carlini 等人 2019（对抗样本防御）；Arp 等人 2022（机器学习用于安全）。即使不做这些方向，也值得读一篇，看看评估会在哪些地方出错。
- **评估的反面教材**：Zeller 2021《The Devil's Guide to Incremental Research》，用反讽列出凑论文的套路。

各资料的链接见[原始资料列表](../../../../sources/README.md)。

[^ralph2020empirical-e79]: SIGSOFT 工程研究标准，定义。[证据](../../../../sources/notes/ralph2020empirical.md#e79)
[^ralph2020empirical-e81]: SIGSOFT 工程研究标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e81)
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
[^ralph2020empirical-e99]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e99)
[^ralph2020empirical-e100]: SIGSOFT 基准评测标准，必要项（讨论）。[证据](../../../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e101]: SIGSOFT 基准评测标准，反面模式。[证据](../../../../sources/notes/ralph2020empirical.md#e101)
[^ralph2020empirical-e102]: SIGSOFT 基准评测标准，不成立的批评。[证据](../../../../sources/notes/ralph2020empirical.md#e102)
[^ralph2020empirical-e103]: SIGSOFT General Standard，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e103)
[^ralph2020empirical-e104]: SIGSOFT 基准评测标准，必要项。[证据](../../../../sources/notes/ralph2020empirical.md#e104)
[^shaw2003writing-e26]: Shaw 2003，§3.2。[证据](../../../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e27]: Shaw 2003，§3.1，表 3。[证据](../../../../sources/notes/shaw2003writing.md#e27)
[^shaw2003writing-e28]: Shaw 2003，§4.1，表 5。[证据](../../../../sources/notes/shaw2003writing.md#e28)
[^shaw2003writing-e10]: Shaw 2003，§4.1，表 5 后。[证据](../../../../sources/notes/shaw2003writing.md#e10)
[^shaw2003writing-e31]: Shaw 2003，§2.3。[证据](../../../../sources/notes/shaw2003writing.md#e31)
[^shaw2003writing-e32]: Shaw 2003，§4.2。[证据](../../../../sources/notes/shaw2003writing.md#e32)
[^shaw2003writing-e33]: Shaw 2003，§4.1，表 5。[证据](../../../../sources/notes/shaw2003writing.md#e33)
[^shaw2003writing-e34]: Shaw 2003，§1。[证据](../../../../sources/notes/shaw2003writing.md#e34)
[^shaw2003writing-e36]: Shaw 2003，§3.3。[证据](../../../../sources/notes/shaw2003writing.md#e36)
[^shaw2003writing-e37]: Shaw 2003，§4.1，表 5。[证据](../../../../sources/notes/shaw2003writing.md#e37)
[^blackburn2018sigplan-e1]: SIGPLAN 实证评估清单，Clearly Stated Claims。[证据](../../../../sources/notes/blackburn2018sigplan.md#e1)
[^blackburn2018sigplan-e12]: SIGPLAN 实证评估清单，Tested on training set。[证据](../../../../sources/notes/blackburn2018sigplan.md#e12)
[^blackburn2018sigplan-e3]: SIGPLAN 实证评估清单，Fails to acknowledge limitations。[证据](../../../../sources/notes/blackburn2018sigplan.md#e3)
[^zeller2021devil-e6]: Zeller 2021，THE RUBE GOLDBERG。[证据](../../../../sources/notes/zeller2021devil.md#e6)
[^zeller2021devil-e3]: Zeller 2021，THE ACHILLES HEEL。[证据](../../../../sources/notes/zeller2021devil.md#e3)
[^klees2018evaluating-e1]: Klees 等人 2018，§1。[证据](../../../../sources/notes/klees2018evaluating.md#e1)
[^klees2018evaluating-e2]: Klees 等人 2018，摘要。[证据](../../../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e4]: Klees 等人 2018，§9。[证据](../../../../sources/notes/klees2018evaluating.md#e4)
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
[^acm2020artifact-e6]: ACM 制品评审与徽章政策 v1.1，Functional 级别注释。[证据](../../../../sources/notes/acm2020artifact.md#e6)
[^acm2020artifact-e7]: ACM 制品评审与徽章政策 v1.1，Artifacts Evaluated。[证据](../../../../sources/notes/acm2020artifact.md#e7)
[^acm2020artifact-e8]: ACM 制品评审与徽章政策 v1.1，开头。[证据](../../../../sources/notes/acm2020artifact.md#e8)
[^carlini2019evaluating-e1]: Carlini 等人 2019，§2.5。[证据](../../../../sources/notes/carlini2019evaluating.md#e1)
[^arp2022dos-e2]: Arp 等人 2022，P9。[证据](../../../../sources/notes/arp2022dos.md#e2)
