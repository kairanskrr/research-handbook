# 比较评估

> 本页讲的道理适用于各学科，例子和具体做法以计算机为例。

你手里有几个现成的做法：几款大模型、几个静态分析工具、几种提示写法。论文里各自都说自己效果好，可放在一起，你说不清哪个更好。你想做的研究，就是把它们放在同一把尺子下比一比。

这就是**比较评估**：不造新东西，而是回答"已有的做法里，哪个更好、好多少、在什么条件下"。研究套路的总体介绍见[核心术语](../00_start-here/key-concepts.md#研究套路)。

---

## 1. 这类研究产生什么知识

**核心主张的样子是："在条件 C 下、按指标 M，做法 A 比 B 好（或差不多）。"** 用"大模型与智能合约安全"举几个假设的例子（不是真实结论）：

- "在真实部署的合约上，大模型检测工具的重入漏洞检出率与静态分析工具相当，但误报多出一倍。"
- "论文里报告的高检出率，换到另一批合约上就看不到了。"
- "三种提示写法中，给出漏洞模式说明的那种在各个模型上都最好。"

每句话都有三个部分：**比的是谁**（已有的工具或做法）、**用什么尺子**（任务集和指标）、**结论能推到多远**（条件）。少了任何一部分，读者就无从判断。

**和相邻套路的区别** `[本项目分析]`：

| | 比较评估 | [构建改进](build_improve.md) | [解释因果](explain_causality.md) | [测量](measure.md) |
|---|---|---|---|---|
| 主张 | 已有的 A 比 B 好 | 我做的新东西比已有的好 | 因素 X 导致了结果 Y | 某个东西这样测才准 |
| 有没有自己的新制品 | 没有，被比的都是别人的 | 有，比较只是证明它好的一步 | 不一定 | 新的测量工具或评测集 |
| 要回答的 | 哪个好、好多少 | 我的方法够不够好 | 为什么 | 尺子准不准 |

和构建改进的界线：软件工程的实证研究标准要求，工程类研究要把自己做出的新制品和最先进的替代方案做实证比较[^ralph2020empirical-e161]，所以在构建改进里，比较常常只是其中一步。如果你的核心主张是关于**别人的工具**，就是比较评估。

和解释因果的界线：比较回答"效果有多好"；再往下问"什么起了作用、为什么"[^lipton2019troubling-e7]，就进入了解释因果。比如发现提示写法 A 最好，是比较；只改提示里的一个成分、其他不动，检验是哪个成分带来了提升，是解释因果 `[本项目分析]`。

**为什么值得做。** 下面三个例子分别来自模糊测试、机器学习和用机器学习做的政治学预测，说明已发表的比较结论可能被高估：

- 模糊测试（用大量随机输入测程序、找缺陷）方向：工具 AFLFast 在原论文选的评测程序上表现好，换到其他论文用过的两个程序上，就不比基线工具 AFL 好了[^klees2018evaluating-e3]。
- 机器学习方向：一系列被归功于新网络结构的改进，后来发现来自更好的调参；同等条件下，老方法反而排第一[^lipton2019troubling-e5]。
- 用机器学习预测内战的研究中，改正错误后，复杂模型并不比几十年前的逻辑回归模型明显更好[^kapoor2023leakage-e8]。

独立、公平的比较，正是用来纠正这类结论的 `[本项目分析]`。

**写下来：** 用"在条件 C 下、按指标 M，A 比 B……"的句式写出你的核心主张。写不出 C 或 M，说明比较还没想清楚。

## 2. 什么样的证据才够

问自己：**一个被你比输了的工具的作者，会从哪里挑你的毛病？** 可以从下面五处逐一检查。

### 对手是否被同等对待

一种典型的不公平，是你对某个工具更上心 `[本项目分析]`。系统安全方向整理的评测缺陷清单里，就有"和对手比较，却给对手用了不是最优的配置"这一条[^vanderkouwe2019sok-e4]。软件工程的基准评测标准也要求，被测系统的不同配置要能凭各自实力竞争，不受人为限制[^ralph2020empirical-e149]。

怎么做：

- **给每个工具同样的调参预算和运行条件**。对抗样本（专门构造来骗过机器学习模型的输入）方向有类似的要求：评估一个防御时，只用默认超参数跑现成的攻击是不够的，即使那是最先进的攻击[^carlini2019evaluating-e1]。对大模型来说，提示写法、输出解析方式也是"参数"，要对每个模型同样用心 `[本项目分析]`。
- **拿不准就问原作者**。系统方向的基准评测指南建议，联系对方作者，确认你的测量对他们的系统是公平的[^heiserbenchmarking-e15]。
- **注意"最优条件"因对象而异**。催化化学有一个现成的例子：适合一种催化剂的反应条件，对另一种可能明显不是最优的[^bligaard2016benchmarking-e7]。软件工具也可能这样：统一用一套设置，未必对每个工具都公平 `[本项目分析]`。

### 任务是否有代表性

软件工程的基准评测标准把"测的是对的方面、基准真实、工作负载有代表性"列为总体质量标准[^ralph2020empirical-e155]。评估随机算法时，选哪些研究对象，往往强烈影响评估结果[^arcuri2014hitchhiker-e11]。

怎么做：

- **说清楚任务是怎么选出来的**。无偏、有代表性的对象往往拿不到，但一定要交代它们是怎么选的[^arcuri2014hitchhiker-e15]。
- **不要随意挑子集**。系统安全方向的建议是：从一大批测试里随意挑出的子集不太可能代表全体，能合理运行的都要跑，省略的要说明原因[^vanderkouwe2019sok-e17]。
- **警惕被"刷过"的评测集**。模糊测试方向的作者提醒，一套固定的基准用久了，工具会开始针对它做没有根本好处的特殊优化[^klees2018evaluating-e7]。对大模型还有一层：好的评测集发布后，题目会传播到网上各处[^wei2024evals-e9]。这些题目可能已经进了模型的训练数据，所以比较大模型工具时，最好加入它们训练截止之后才出现的合约 `[本项目分析]`。

### 指标是否测到了你关心的东西

软件工程的基准评测标准要求讨论基准的构念效度，也就是：它测的是不是它应该测的东西[^ralph2020empirical-e100]。

- **代用指标会骗人**。模糊测试论文常用"不同崩溃数"代替真实缺陷数，这种指标可能严重多算，表面上的提升可能很小甚至不存在[^klees2018evaluating-e4]。
- **判断类工具要报它准不准**。系统安全方向的缺陷清单指出，不知道系统有多准，就无法判断它的价值[^vanderkouwe2019sok-e7]。漏洞检测正是这种工具，"准不准"要看误报和漏报各有多少：只报检出率、不报误报，开发者得到的信息是不完整的 `[本项目分析]`。
- **把代价也算进去**。系统安全方向提醒，只测运行时间不够，还要看内存等其他开销[^vanderkouwe2019sok-e6]；评估随机算法的指南也说，实际选算法时，还要看成本差异，比如需要用户提供的输入和执行时间[^arcuri2014hitchhiker-e6]。对大模型工具来说，调用费用和耗时也是代价 `[本项目分析]`。

### 留一份数据只用于最后检验

下面的做法主要出自机器学习和编程语言方向的评测文献。比较时你多半也要调东西：给每个工具调参数、改提示写法、改输出解析。调的时候看过的数据，不能再拿来报告最终结果 `[本项目分析]`。

- **一开始就划出一份检验数据。** 机器学习的方法指南建议：项目一开始就分出一部分数据，只在项目最后用一次，评估最终的那一个方案[^lones2021avoid-e3]。
- **开发时参考过的例子，不能再拿来评估。** 编程语言方向的实证评估清单写道：系统想做到通用，开发时却仔细参考了某些具体例子，评估就必须用和这些例子不同的数据[^blackburn2018sigplan-e12]。
- **别拿检验数据反复试方案。** 同一份机器学习指南说，常见的做法是随手试不同的模型和参数，直到在检验数据上效果好[^lones2021avoid-e4]；检验数据用的次数越多，结果就越只对这份数据好[^lones2021avoid-e5]。

评估用的信息混进了开发过程，机器学习里叫"数据泄漏"。一项调查在 17 个领域发现了这类问题，涉及 294 篇论文，有些得出了严重过于乐观的结论[^kapoor2023leakage-e1]。

在大模型检测合约的例子里：先用一小批合约调提示写法，定稿后，在另一批从没看过的合约上只跑一次，报告这一次的结果 `[本项目分析]`。道理也不限于机器学习：根据一批样本提出的假设，要换一批样本来检验 `[本项目分析]`。

### 差异是不是真的

下面的做法主要出自模糊测试、软件工程和机器学习的评测文献，也有一条来自政治学的复现经验。

- **多次运行，看分布**。模糊测试这类带随机性的工具，要做足够多次试验来描述性能分布，并用统计检验确认差异不是偶然[^klees2018evaluating-e10]。只比单次运行可能得出相反的结论：在同一个程序上，一次运行里 AFL 找到的崩溃比 AFLFast 多，30 次运行的中位数却是 AFLFast 远多于 AFL[^klees2018evaluating-e11]。大模型的输出也带随机性，同样适用 `[本项目分析]`。
- **记下随机种子，并换几个种子重复**。随机种子是程序生成随机数的起点，固定它，"随机"的过程就能重现。软件分析方向指出，带随机性的算法不给出种子，别人就无法精确复现[^menzies2019bad-e8]；政治学期刊的复现经验也建议在代码里设定种子，保证每次都跑出论文里的结果[^eubank2016lessons-e7]。训练神经网络的经验是，排错时固定种子，让两次运行结果相同[^karpathy2019recipe-e4]。评估时则要换多个种子重复，两者并不矛盾 `[本项目分析]`。
- **报告波动，检验做多了要校正**。只评估一次不可靠，可能高估，也可能低估[^lones2021avoid-e6]。怎样报告波动、效应量和多重比较，见[分析与解读：报告差多少、有多确定，而不只是 p 值](../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。
- **报告差多少，而不只是"显著"**。效应量是衡量差异有多大的数。运行次数多到几千次时，几乎任何差异都会显著，所以必须同时分析效应量[^arcuri2014hitchhiker-e9]。
- **分对象报告**。评估随机算法的指南举过一个例子：五个对象上的效应量是 0.6、0.6、0.6、0.6、0.1，平均是 0.5，看起来"没有差别"，其实一方在四个对象上更好、在一个上差得多[^arcuri2014hitchhiker-e21]。

这些不是苛求。系统安全方向，调查的 50 篇顶会防御论文平均每篇有 5 个评测缺陷[^vanderkouwe2019sok-e26]；其中最普遍的是不给数据的波动或显著性指标，在适用的论文中占 80%[^vanderkouwe2019sok-e15]。模糊测试方向，被检查的 32 篇论文的实验评估每一篇都有问题[^klees2018evaluating-e2]。

更系统的效度讨论见[效度与局限](../02_do-the-project/04_validity-and-limits.md)。

**写下来：** 列出你要比的每个工具，在旁边写下：用什么配置、调参花了多少功夫、为什么这样对它是公平的。

## 3. 常用的研究方法

`[本项目分析]`，另有出处的已单独标出。

| 方法 | 什么时候用 | 说明 |
|---|---|---|
| [基准评测](../07_fields/computer-science/practices/benchmarking.md) | 被比较的是软件、工具或模型本身，能自动运行、重复测量 | 计算机比较评估最常用的方法 |
| [有人参与的对照实验](../06_methods/controlled_experiment.md) | 要比的是人用不同工具时的表现，例如开发者用哪个工具更快找到漏洞 | 需要招募参与者、随机分组 |
| [复现研究](../06_methods/replication.md) | 想检验某篇论文的比较结论在别的条件下是否还成立 | 常和比较评估结合 |
| [优化研究](../07_fields/computer-science/practices/optimization_study.md) | 比较搜索、优化类算法 | 搜索算法至少要和随机搜索比，确认成功不是因为问题本身太简单[^arcuri2014hitchhiker-e4] |
| [系统综述与元分析](../06_methods/meta_analysis.md) | 不自己做实验，而是合并已发表研究里的比较结果 | 健康领域常用 |

方法和套路是两层：同一种方法可以服务不同的套路，见[选定研究套路和方法](../02_do-the-project/02_choose-method.md)。

## 4. 它怎样影响整个项目

`[本项目分析]`，各条另有出处的已单独标出。

| 阶段 | 比较评估要特别注意什么 |
|---|---|
| 读文献 | 不只读结论，还要记下每篇论文**怎么比的**：用了哪些对象、几次运行、什么指标。整理成表格，就能看出谁的结论站得住。系统地检查一批论文的评测做法，本身就能写成研究，例如逐篇检查 32 篇论文的评估做法[^klees2018evaluating-e23] |
| 选题 | 值得比的地方，是大家需要做选择、而现有结论互相矛盾或没人公平比过的地方。健康领域的 Cochrane 手册把"平息相互矛盾的结论"列为元分析（合并多项研究结果的统计方法）的好处之一[^higgins2024cochrane-e13] |
| 设计 | 动手前定好对象、指标、运行次数和"多大差异才算有意义"。软件工程的实证研究标准把验证性研究里先看结果再提假设、只报告显著的检验，列为反面做法[^ralph2020empirical-e27] |
| 执行 | 保存全部原始结果，不要只存汇总值[^ralph2020empirical-e158]。记下每个工具和模型的版本，因为同一个大模型接口背后的模型可能会更新 |
| 写作 | 计算机几份评测指南的共同要求：给出每个对象上的结果，而不只是总分[^heiserbenchmarking-e18]；除了相对数，还要给绝对数[^vanderkouwe2019sok-e23]；写清平台和软件版本[^vanderkouwe2019sok-e13]；报告所有 p 值，不论是否显著[^arcuri2014hitchhiker-e17]。写作的整体做法见[讲清故事，写成论文](../03_write-and-publish/01_story-and-paper.md) |

**比输了怎么办** `[本项目分析]`：比较评估的结论没有"失败"一说。"新工具在真实合约上并不比老工具好"，本身就是有价值的主张，前提是比较足够公平。

## 5. 哪些学科常用

下面只列本文资料里有依据的；其他学科本文资料未涉及。

- **计算机**。软件工程的实证研究标准专门有一类"基准评测"，定义就是用标准工具对方法、技术或系统做竞争性的评估和比较[^ralph2020empirical-e143]。系统安全、软件测试、机器学习都有专门讨论比较怎样做才可靠的文献，见上文各节。
- **化学（催化）**。以下要求出自催化研究的基准评测文献，只代表这一方向。活性、选择性、失活情况等指标，用来比较新催化剂和标准催化剂[^bligaard2016benchmarking-e1]；报告新催化剂时，要和成熟或最先进的催化剂在相同条件下比较[^bligaard2016benchmarking-e17]；比较几种催化剂的选择性，要在相同转化率下测[^bligaard2016benchmarking-e15]。
- **计算材料与物理**。例子来自固体材料计算方向：一项社区合作比较了 15 个固体计算程序，在 71 种单质晶体上评估同一类计算的结果[^lejaeghere2016reproducibility-e3]；结论是新近的程序彼此吻合得很好，较老的方法吻合度差一些[^lejaeghere2016reproducibility-e4]。
- **健康**。Cochrane 系统综述手册写道，问干预效果时一般用 PICO 框架（人群、干预、对照、结局），其中 C 就是对照（Comparison）[^higgins2024cochrane-e5]。在健康领域，"比较两种疗法"常常同时是因果问题，要用随机试验等因果设计，比较评估和解释因果的界线不像计算机那么分明 `[本项目分析]`。

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 给自己偏爱的工具精心调参，其他用默认设置 | 比出来的是调参功夫，不是工具本身。机器学习里就有被归功于新结构的改进，后来发现来自更好的调参[^lipton2019troubling-e5] |
| 只挑对某个工具有利的任务 | 换一批任务结论可能反过来[^klees2018evaluating-e3]；系统方向的指南直言，只评估有利的场景是在欺骗读者[^heiserbenchmarking-e3] |
| 为某个工具量身定做评测集 | 软件工程的基准评测标准把它列为反面做法[^ralph2020empirical-e157] |
| 只报检出率，不报误报 | 不知道准确率，就无法判断工具的价值[^vanderkouwe2019sok-e7] |
| 调方案时反复看检验数据 | 检验数据用的次数越多，结果越只对这份数据好[^lones2021avoid-e5] |
| 每个工具只跑一次 | 单次运行可能得出相反的结论[^klees2018evaluating-e11] |
| 只说"显著"，不说差多少 | 运行次数多时几乎任何差异都显著[^arcuri2014hitchhiker-e9] |
| 只给所有任务的平均分 | 平均会掩盖一方在个别对象上大幅落后[^arcuri2014hitchhiker-e21] |
| 不写版本和平台 | 别人无法复现，也无法判断差异从哪来[^vanderkouwe2019sok-e13] |
| 把"哪个好"直接写成"为什么好" | 比较只回答效果有多好；为什么，需要另做检验 `[本项目分析]` |

## 7. 延伸阅读

- **ACM SIGSOFT Empirical Standards，Benchmarking 标准**（美国计算机协会软件工程分会制定的实证研究标准）：基准评测的必要项、加分项和反面做法。
- **Klees 等人，Evaluating Fuzz Testing**：模糊测试方向，用大量实验演示比较做得不对时结论会怎样翻转。
- **van der Kouwe 等人，SoK: Benchmarking Flaws in Systems Security**：系统安全方向，22 种评测缺陷的清单[^vanderkouwe2019sok-e26]，投稿前可以逐条对照。
- **Heiser，Systems Benchmarking Crimes**：系统方向的评测"罪行"清单。
- **Arcuri & Briand，A Hitchhiker's Guide to Statistical Tests for Assessing Randomized Algorithms**：比较带随机性的算法时，怎样定运行次数、选检验和效应量。

[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards，General Standard，Research and Reporting Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e100]: ACM SIGSOFT Empirical Standards，Benchmarking 标准，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e143]: ACM SIGSOFT Empirical Standards，Benchmarking 标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e143)
[^ralph2020empirical-e149]: ACM SIGSOFT Empirical Standards，Benchmarking 标准，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e149)
[^ralph2020empirical-e155]: ACM SIGSOFT Empirical Standards，Benchmarking 标准，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e155)
[^ralph2020empirical-e157]: ACM SIGSOFT Empirical Standards，Benchmarking 标准，Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e157)
[^ralph2020empirical-e158]: ACM SIGSOFT Empirical Standards，Benchmarking 标准，Antipatterns。[证据](../../sources/notes/ralph2020empirical.md#e158)
[^ralph2020empirical-e161]: ACM SIGSOFT Empirical Standards，Engineering Research 标准，Essential Attributes。[证据](../../sources/notes/ralph2020empirical.md#e161)
[^lipton2019troubling-e5]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../sources/notes/lipton2019troubling.md#e5)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../sources/notes/lipton2019troubling.md#e7)
[^kapoor2023leakage-e8]: Kapoor & Narayanan 2023，Summary 与内战预测案例一节。[证据](../../sources/notes/kapoor2023leakage.md#e8)
[^klees2018evaluating-e2]: Klees 等人 2018，摘要。[证据](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees 等人 2018，§9。[证据](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e4]: Klees 等人 2018，§9。[证据](../../sources/notes/klees2018evaluating.md#e4)
[^klees2018evaluating-e7]: Klees 等人 2018，§8。[证据](../../sources/notes/klees2018evaluating.md#e7)
[^klees2018evaluating-e10]: Klees 等人 2018，§1。[证据](../../sources/notes/klees2018evaluating.md#e10)
[^klees2018evaluating-e11]: Klees 等人 2018，§1。[证据](../../sources/notes/klees2018evaluating.md#e11)
[^klees2018evaluating-e23]: Klees 等人 2018，Table 1 与 §4。[证据](../../sources/notes/klees2018evaluating.md#e23)
[^vanderkouwe2019sok-e26]: van der Kouwe 等人 2019，摘要。[证据](../../sources/notes/vanderkouwe2019sok.md#e26)
[^vanderkouwe2019sok-e4]: van der Kouwe 等人 2019，§II-D。[证据](../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e6]: van der Kouwe 等人 2019，附录 E2。[证据](../../sources/notes/vanderkouwe2019sok.md#e6)
[^vanderkouwe2019sok-e7]: van der Kouwe 等人 2019，§II-E。[证据](../../sources/notes/vanderkouwe2019sok.md#e7)
[^vanderkouwe2019sok-e13]: van der Kouwe 等人 2019，§II，Table I。[证据](../../sources/notes/vanderkouwe2019sok.md#e13)
[^vanderkouwe2019sok-e15]: van der Kouwe 等人 2019，§IV。[证据](../../sources/notes/vanderkouwe2019sok.md#e15)
[^vanderkouwe2019sok-e17]: van der Kouwe 等人 2019，§VI 与 §II-A。[证据](../../sources/notes/vanderkouwe2019sok.md#e17)
[^vanderkouwe2019sok-e23]: van der Kouwe 等人 2019，§II-F。[证据](../../sources/notes/vanderkouwe2019sok.md#e23)
[^arcuri2014hitchhiker-e4]: Arcuri & Briand 2014，§3。[证据](../../sources/notes/arcuri2014hitchhiker.md#e4)
[^arcuri2014hitchhiker-e6]: Arcuri & Briand 2014，§4。[证据](../../sources/notes/arcuri2014hitchhiker.md#e6)
[^arcuri2014hitchhiker-e9]: Arcuri & Briand 2014，§8。[证据](../../sources/notes/arcuri2014hitchhiker.md#e9)
[^arcuri2014hitchhiker-e11]: Arcuri & Briand 2014，§10.1。[证据](../../sources/notes/arcuri2014hitchhiker.md#e11)
[^arcuri2014hitchhiker-e15]: Arcuri & Briand 2014，§11。[证据](../../sources/notes/arcuri2014hitchhiker.md#e15)
[^arcuri2014hitchhiker-e17]: Arcuri & Briand 2014，§11。[证据](../../sources/notes/arcuri2014hitchhiker.md#e17)
[^arcuri2014hitchhiker-e21]: Arcuri & Briand 2014，§10.2。[证据](../../sources/notes/arcuri2014hitchhiker.md#e21)
[^carlini2019evaluating-e1]: Carlini 等人 2019，§2.5。[证据](../../sources/notes/carlini2019evaluating.md#e1)
[^heiserbenchmarking-e3]: Heiser，Systems Benchmarking Crimes，Not evaluating potential performance degradation。[证据](../../sources/notes/heiserbenchmarking.md#e3)
[^heiserbenchmarking-e15]: Heiser，Systems Benchmarking Crimes，Unfair benchmarking of competitors。[证据](../../sources/notes/heiserbenchmarking.md#e15)
[^heiserbenchmarking-e18]: Heiser，Systems Benchmarking Crimes，Missing sub-benchmark results。[证据](../../sources/notes/heiserbenchmarking.md#e18)
[^wei2024evals-e9]: Jason Wei 2024，测试集污染一节。[证据](../../sources/notes/wei2024evals.md#e9)
[^bligaard2016benchmarking-e1]: Bligaard 等人 2016，摘要。[证据](../../sources/notes/bligaard2016benchmarking.md#e1)
[^bligaard2016benchmarking-e7]: Bligaard 等人 2016，§2.2，第 2595 页。[证据](../../sources/notes/bligaard2016benchmarking.md#e7)
[^bligaard2016benchmarking-e15]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../sources/notes/bligaard2016benchmarking.md#e15)
[^bligaard2016benchmarking-e17]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../sources/notes/bligaard2016benchmarking.md#e17)
[^lejaeghere2016reproducibility-e3]: Lejaeghere 等人 2016，摘要。[证据](../../sources/notes/lejaeghere2016reproducibility.md#e3)
[^lejaeghere2016reproducibility-e4]: Lejaeghere 等人 2016，摘要。[证据](../../sources/notes/lejaeghere2016reproducibility.md#e4)
[^higgins2024cochrane-e5]: Cochrane 手册 6.5 版，第 1 章，§1.2。[证据](../../sources/notes/higgins2024cochrane.md#e5)
[^higgins2024cochrane-e13]: Cochrane 手册 6.5 版，第 10 章，Key Points。[证据](../../sources/notes/higgins2024cochrane.md#e13)
[^lones2021avoid-e3]: Lones 2021，§3.1，第 8 页。[证据](../../sources/notes/lones2021avoid.md#e3)
[^lones2021avoid-e4]: Lones 2021，§4.3，第 15 页。[证据](../../sources/notes/lones2021avoid.md#e4)
[^lones2021avoid-e5]: Lones 2021，§4.3，第 15 页。[证据](../../sources/notes/lones2021avoid.md#e5)
[^lones2021avoid-e6]: Lones 2021，§4.4，第 15 页。[证据](../../sources/notes/lones2021avoid.md#e6)
[^blackburn2018sigplan-e12]: SIGPLAN 实证评估清单，Tested on training set。[证据](../../sources/notes/blackburn2018sigplan.md#e12)
[^kapoor2023leakage-e1]: Kapoor & Narayanan 2023，Summary。[证据](../../sources/notes/kapoor2023leakage.md#e1)
[^menzies2019bad-e8]: Menzies & Shepperd 2019，§4.4。[证据](../../sources/notes/menzies2019bad.md#e8)
[^eubank2016lessons-e7]: Eubank 2016，Randomizations and Simulations。[证据](../../sources/notes/eubank2016lessons.md#e7)
[^karpathy2019recipe-e4]: Karpathy 2019，第 2 步 fix random seed。[证据](../../sources/notes/karpathy2019recipe.md#e4)
