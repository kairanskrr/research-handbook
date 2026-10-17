# 大模型实证研究：评测大模型，或把大模型当研究工具

本文讲**用到大语言模型（下文简称大模型）的实证研究**。大模型在研究里有两种身份：一是**被研究的对象**，例如在同一项任务上评测几个大模型，或者评估一个以大模型为核心的新工具；二是**研究工具**，例如让大模型代替人给数据打标签、给别的输出打分，或者模拟问卷和实验里的参与者。两种身份可以出现在同一项研究里[^baltes2026guidelines-e1]。

评测的一般流程（选基准、公平配置、测量、分析）见[基准评测](../07_fields/computer-science/practices/benchmarking.md)；研究人怎样使用大模型工具，见[对照实验](controlled_experiment.md)；提出了一个基于大模型的新工具，整篇论文怎样评估，见[工程研究](../07_fields/computer-science/practices/engineering_research.md)。统计检验见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md)，效度见[效度与局限](../02_do-the-project/04_validity-and-limits.md)。本文只讲大模型带来的额外问题。

**适用范围** `[本项目分析]`：本文主要依据软件工程的资料：22 位研究者共同制定的软件工程大模型实证研究准则（Baltes 等，下文简称"大模型准则"），以及 Sallou 等人关于大模型效度威胁的论文。讲评测的部分还用了自然语言处理方向评测框架 lm-eval 开发者的经验总结（Biderman 等）和关于数据污染的立场论文（Sainz 等）；讲标注的部分用了社会科学的最佳实践（Törnberg）。大模型准则明确说它面向软件工程；医疗、人机交互、基于机器学习的科学，各有自己的大模型报告规范[^baltes2026guidelines-e35]。在这些领域做研究，先看本领域的规范。

**常服务的套路**：[测量](../05_research-strategies/measure.md)、[比较评估](../05_research-strategies/compare_evaluate.md)、[构建改进](../05_research-strategies/build_improve.md)。

**读完本文，你应该能：**

- 分清大模型在你的研究里是被评测的对象还是研究工具，并据此决定要报告什么；
- 记录模型版本、参数、日期和提示词，让别人有可能复现你的结果；
- 检查数据污染、提示词敏感性和多次运行之间的波动，不把偶然的数字当成结论；
- 用人工判断验证大模型给出的标签或评分；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

大模型准则按**大模型在研究里扮演的角色**给研究分类，而不是按研究方法分；一项研究可以同时属于几类[^baltes2026guidelines-e1]。归纳起来是两大类 `[本项目分析]`：

| 大模型的身份 | 具体角色 | 例子 |
|---|---|---|
| 研究工具 | 标注员、评审员、综合者、模拟被试 | 给访谈记录做定性编码；评价软件制品的质量；汇总论文；模拟人的行为[^baltes2026guidelines-e2] |
| 被研究的对象 | 被观察的工具、新工具的部件、被评测的模型 | 研究工程师怎样用大模型；做集成大模型的新工具；在标准任务上评测大模型[^baltes2026guidelines-e3] |

**为什么要单独讲。** 大模型给实证研究多出三个麻烦：输出不确定，每次运行结果不同；商业模型在版本号不变的情况下也在变；连号称"开放"的模型也常不公开训练数据[^baltes2026guidelines-e5]。结果是很多研究复现不出来。一项调查看了 2024 年两个软件工程顶级会议上以大模型为中心的 85 篇论文：其中 18 篇用了 OpenAI 的模型、又提供了研究材料，只有 5 篇能跑起来，没有一篇完全复现出原来的结果[^baltes2026guidelines-e4]。

**它擅长回答的问题** `[本项目分析]`：

- 某个大模型在某项任务上表现如何，比传统方法好多少，值不值那份成本；
- 已发表的大模型评测结果可不可信，例如有没有被数据污染抬高；
- 大模型能不能可靠地替人完成某项研究任务，例如标注、打分。

**它不擅长回答的问题。** 人在真实工作里怎样用大模型、大模型对人有什么影响，要靠有人参与的研究，例如[对照实验](controlled_experiment.md)、[问卷调查](questionnaire_survey.md)、[访谈研究](interview_study.md) `[本项目分析]`。目前也没有令人信服的证据表明大模型能准确模拟人类参与者[^baltes2026guidelines-e27]。所以让大模型当被试得出的结果，不能直接当作关于人的结论。

**和相近方法的区别** `[本项目分析]`：

| | 大模型实证研究（本文） | [基准评测](../07_fields/computer-science/practices/benchmarking.md) | [对照实验](controlled_experiment.md) | [工程研究](../07_fields/computer-science/practices/engineering_research.md) |
|---|---|---|---|---|
| 关注什么 | 大模型特有的问题：版本、提示词、污染、波动、拿人工判断验证 | 评测的一般流程：选基准、公平配置、测量、统计 | 人在某种处理下的表现 | 一个新方法或新工具整体怎样评估 |
| 典型问题 | "这个评测结果有没有被污染抬高？""大模型标注能代替人吗？" | "工具 A 比 B 好吗？" | "用大模型助手的人修缺陷更快吗？" | "我的新工具比现有工具好吗？" |

实际项目里常常几页一起用：评测大模型时，按基准评测那一页走一般流程，再按本文补上大模型特有的几步。

**例子** `[本项目分析]`：贯穿全书的项目"现有大模型漏洞检测的评测结果被数据泄露高估了"，就是一项大模型实证研究。几个大模型是被评测的对象，研究要测的是：它们在公开评测合约上的成绩，有多少来自训练时"见过"这些合约。如果你还让另一个大模型从各模型的回答里抽出"报告了哪类漏洞、在哪一行"，这个大模型就成了研究工具，要另外声明、另外验证（见第七步）。

---

## 2. 怎么做

下面的步骤补在[基准评测](../07_fields/computer-science/practices/benchmarking.md#2-怎么做)的一般流程之上。大模型准则把要求分成两级："必须"是硬要求；"应当"能加强研究的严谨和透明，但特定情况下可以有正当理由不做[^baltes2026guidelines-e6]。下文照这个区分来写。

### 第一步：说清大模型在研究里的角色

**怎么做：**

- 写明用了哪个大模型、怎么用、用在研究的哪个环节[^baltes2026guidelines-e7]。
- 大模型担任几种角色，就分别声明。例如一个模型生成评测数据，另一个模型给输出打分[^baltes2026guidelines-e7]。

**为什么**：角色不同，要担心的事不同 `[本项目分析]`。被评测的模型，要担心污染和波动（第四步、第六步）；当工具用的模型，要拿人工判断验证（第七步）。先把角色分清，后面每一步才知道该对谁做。

**容易错在哪**：只写一句"我们用大模型辅助了数据处理"，不说哪个模型、处理了什么。读者没法判断它会怎样影响结果 `[本项目分析]`。

**写下来：** 列一张表，每个用到大模型的环节占一行：哪个模型、什么角色、输入是什么、输出用在哪里。

### 第二步：选模型，记下确切的版本、参数和日期

**怎么做：**

- **选模型要说出理由**[^tornberg2024best-e3]。能自己选的时候，除了商业模型，再加一个开放权重的模型作基线，最好是开源模型[^baltes2026guidelines-e23]。开放权重的模型公开了训练好的参数，别人可以自己部署；开源模型更好，因为还可以查它的训练数据里有没有你的评测集[^baltes2026guidelines-e24]。
- **整个项目固定用一个版本**，记下版本，并确保这个模型以后还能用[^tornberg2024best-e3]。
- **论文里至少写明三样**：确切的模型或工具名称和版本、影响输出的所有参数、做实验的日期。默认值也可能变，所以用了默认参数也要写出来[^baltes2026guidelines-e8][^tornberg2024best-e14]。大模型准则给的一段示例大意是："通过 Azure OpenAI 服务调用 gpt-4 的 0125-Preview 版本，温度 0.7，top_p 0.8，最大输出长度 512，随机种子 23487；实验在 2025 年 1 月 10 日运行；系统指纹为 fp_6b68a8204b"[^baltes2026guidelines-e36]。
- **不要用网页聊天界面做实验**：网页界面不能设参数，不能控制版本，隐私和版权也没有保障[^tornberg2024best-e4]。
- **商业模型拿不到全部信息时**，报告能拿到的部分，并公开承认妨碍复现的局限[^baltes2026guidelines-e9]。

**为什么**：商业模型会悄悄变。ChatGPT 的模型会在不通知的情况下变化，同样的指令给出不同的结果；接口提供的固定版本，过不久就会下线[^tornberg2024best-e2]。Sallou 等人引用的一项研究发现，2023 年 3 月到 6 月之间，GPT-4 生成代码的答案有一半变了，能直接运行的输出从 22% 降到 2%[^sallou2024breaking-e6]。在前人工作上做改进时，你很难分清提升是来自自己的新方法，还是模型本身变了[^sallou2024breaking-e2]。商业模型还可能下线或悄悄更新，开放模型以后还能用[^baltes2026guidelines-e23]。

**容易错在哪**：以为把温度设为 0 就能复现。温度（控制输出随机程度的参数）设为 0，也很少能保证输出完全确定。它只是措施之一，还要固定随机种子、记录系统指纹、存档原始输出[^baltes2026guidelines-e10]。

**写下来：** 建一份实验元数据文件，每次运行自动记下：模型名称和版本、接入渠道、全部参数（包括默认值）、随机种子、系统指纹、运行日期。

### 第三步：设计提示词，检查结果对提示词有多敏感

**怎么做：**

- **写明提示方式**：零样本（不给示例直接做题）、单样本还是少样本（给几个示例），示例是怎么挑的。试过几版提示词，就说明怎样比较、怎样选定最终版本[^baltes2026guidelines-e12]。
- **说清提示词和模型的对应关系**。提示词是针对开发时用的那个模型调出来的，换一个模型，即使规模相近，结果也可能不同[^tornberg2024best-e8]。所以要写明哪条提示词用在哪个模型、哪个版本、什么配置上[^baltes2026guidelines-e11]。
- **做提示词稳定性分析**：写几种意思相同的提示词，在一部分数据上分别运行，比较结果[^tornberg2024best-e15]。
- **规定输出格式，并检查失败是不是格式造成的。** 评测分数常把你要测的能力，和"能不能按要求的格式输出、能不能听懂指令"混在一起[^baltes2026guidelines-e37]。lm-eval 的开发者遇到过：一个模型在某种提示格式下表现接近随机猜，查看输出才发现它是没按这种格式作答，换一种格式就能得高分[^biderman2024lessons-e11]。

**为什么**：提示词的确切写法，连空格都会显著影响表现。换一种常见的提示方式，有时差 20% 以上，而且哪种方式最好因模型而异，所以提示词会改变模型的排名和研究结论[^biderman2024lessons-e4]。大模型准则引用的研究显示，光是提示词的格式，就能让准确率相差多达 76 个百分点[^baltes2026guidelines-e5]。不同提示词格式的表现，在不同模型之间只有弱相关；所以只用一个随意选定的固定格式比较模型，方法上站不住[^baltes2026guidelines-e13]。

**容易错在哪**：给自己的方法精心调提示词，给对比的模型用随手写的提示词。评测者本来就面临挑好看的提示方式的压力[^biderman2024lessons-e2]；这样比出来的差距，有一部分来自提示词，而不是来自方法 `[本项目分析]`。

**写下来：** 一份提示词变更记录：每一版提示词的全文、改了什么、为什么改、在哪些模型上试过、效果如何。

### 第四步：检查数据污染

**数据污染**指评测用的数据混进了模型的训练数据。最严重的情况是：模型在某个基准的测试集上训练过，又在同一个基准上评测[^sainz2023nlp-e1]。污染会高估模型的表现[^sainz2023nlp-e2]。污染的一般讲法见基准评测页的[基准本身有效吗](../07_fields/computer-science/practices/benchmarking.md#3-基准本身有效吗)一节，这里补充大模型研究里的具体做法。

污染的影响可能很大。Sallou 等人发现，ChatGPT 对缺陷数据集 Defects4J 里的缺陷了如指掌，所以在这个数据集上修复、定位缺陷、生成测试，表现比在没见过的代码上好[^sallou2024breaking-e1]。他们还引用了一个例子：同样是生成单元测试，大模型在放在 GitHub 上的数据集 HumanEval 上分支覆盖率超过 69%，在放在 SourceForge 上的数据集 SF110 上只有 2%[^sallou2024breaking-e3]。

**怎么做：**

- **查训练数据。** 训练数据公开的模型，查评测集有多大比例出现在训练数据里[^sainz2023nlp-e4]；不公开的，看模型能不能逐字背出评测集里的样本[^sainz2023nlp-e5]。
- **用"蜕变"改写造新样本。** 对评测样本做改写，让它的语义和行为不变、结构不同，用新样本补充评测；用哪种改写要看任务[^sallou2024breaking-e9]。Sallou 等人只是删掉文档注释、给被测方法和参数换了名字，ChatGPT 在原程序上稳定达到 71% 的覆盖率，在改写后的程序上却几乎生成不出有意义的测试[^sallou2024breaking-e10]。
- **用模型训练截止之后的数据。** 只收集某个截止日期之后的数据来建评测集，并写明数据来源和收集日期。但新模型迟早会学到这些数据，所以要不断更新[^baltes2026guidelines-e21]。
- **从多个来源收集数据**；用代码克隆检测，看模型生成的代码是否和网上已有的代码相似[^sallou2024breaking-e11]。
- **自己微调模型时**，按项目分开训练集和测试集还不够：不同项目共用的依赖和接口也会造成泄露[^sallou2024breaking-e4]。
- **自己建评测集时**，留一部分不公开的题目，专门用于持续评测；嵌入"金丝雀字符串"，也就是独特的标记，日后能据此查出评测集有没有进入训练数据[^baltes2026guidelines-e20]。

**为什么**：大模型的训练数据不透明，所以必须讨论可能的数据泄露和它对结果的影响[^baltes2026guidelines-e31]。这一步常被跳过：一项对 572 个代码评测集的调查发现，82.5% 没有处理数据污染[^baltes2026guidelines-e22]。

**容易错在哪**：以为污染只发生在评测之前。评测样本还可能被无意中用于模型的再训练，跨越较长时间的研究尤其要注意[^baltes2026guidelines-e31]。

> **不同的看法：用大模型做标注时，污染一定是问题吗？**
>
> - 软件工程的大模型准则要求：用现成评测集的研究，要把污染写进局限[^baltes2026guidelines-e20]。
> - 社会科学的 Törnberg 认为，做文本标注时，验证数据出现在训练数据里不一定是问题，只要正式标注的数据也同样出现在里面；但不要拿公开的、已经标好的数据库当验证集，因为模型可能已经见过这些标签[^tornberg2024best-e16]。
>
> 实际操作中 `[本项目分析]`：先看你要测的是什么。你在测**模型的能力**时，污染直接抬高分数，必须处理；你只是**用模型完成标注**时，关心的是它在正式数据上标得准不准，要求验证数据和正式数据在"模型见没见过"这一点上相同。

**例子** `[本项目分析]`：合约项目的核心就在这一步。把评测合约分成两组："可能见过"的公开合约，和"不可能见过"的合约。后者有两个来源：模型训练截止之后才部署的合约，以及对公开合约做的蜕变改写，例如给函数和变量换名、删注释、调整无关语句的顺序。同一个模型在两组上的检出率之差，就是结果表里"去掉泄露前后"那一列的来源。注意，改写不能改变漏洞本身，要人工抽查一部分改写后的合约。

**写下来：** 一张污染检查表：每个评测集、每个模型，用了哪种检查办法，结果如何，没法检查的写明原因。

### 第五步：选基线和指标

**怎么做：**

- **加传统方法作基线。** 检查有没有更省资源的传统方法（例如静态分析）可以当基线。即使大模型更好，也要讨论它消耗的资源值不值那点（往往不大的）提升[^baltes2026guidelines-e15]。
- **加开放模型作基线**，见第二步[^baltes2026guidelines-e23]。
- **每个指标都说明为什么合适**，不能只说"前人用过"[^baltes2026guidelines-e18]。做分类和标注时，只看准确率往往不够，类别不平衡时尤其容易误导[^tornberg2024best-e12]。
- **跑完做错误分析**：把失败的情况分类，报告每类占多少[^baltes2026guidelines-e19]；弄清模型为什么得分高或低[^biderman2024lessons-e12]。

**为什么**：人们关心的几乎从来不是某个评测集上的分数本身。评测集只是某种难以精确测量的能力的替代指标[^biderman2024lessons-e9]。有了传统基线和错误分析，读者才知道这个分数说明了什么能力 `[本项目分析]`。

**容易错在哪**：只和别的大模型比。大模型之间分出高下，说明不了大模型比传统方法强多少、值不值得用 `[本项目分析]`。

**例子** `[本项目分析]`：合约项目里，传统基线可以是现有的静态分析工具。它们不靠训练数据，不受污染影响，正好当参照：如果大模型在"可能见过"的合约上远胜静态工具，在"不可能见过"的合约上却和它们差不多，这本身就是高估的证据。

**写下来：** 列出每个基线、每个指标和选它的理由，各一句话。

### 第六步：重复运行，报告波动

**怎么做：**

- **重复实验。** 同一条提示词跑几次，结果不一定一样[^sallou2024breaking-e5]。所以要重复实验，报告均值、中位数、置信区间、标准差[^baltes2026guidelines-e16]。
- **说明重复几次的理由**：做功效分析，或者一边增加运行次数一边看统计量是否稳定下来；预实验可以帮你估计波动有多大[^baltes2026guidelines-e17]。预实验的一般做法见[最小可跑版本](../02_do-the-project/05_pilot-and-derisk.md)。
- **比较模型时用推断统计和效应量**，不要只比平均数[^baltes2026guidelines-e16]。一般做法见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。
- **分清两种波动**：同一批题目反复运行，结果怎么变；把评测题目看成从一大类题目里抽出的样本，换一批题，结果怎么变。两种都值得报告[^biderman2024lessons-e13]。

**为什么**：只报一次运行的分数，和报 10 次运行的 95% 置信区间，对模型高下会得出很不一样的结论；在小评测集上宣称的小幅提升，可能同样设置下再采样一次就没了[^biderman2024lessons-e10]。Sallou 等人的示范里，同一组提示词跑十次，平均分支覆盖率 70%，四分位距（中间一半结果的分布范围）高达 27.5%[^sallou2024breaking-e7]。可这一步常被跳过：前面那项调查发现，64.0% 的代码评测集只跑一次、不控制随机性[^baltes2026guidelines-e22]。

**容易错在哪**：多跑几次，只报最好的那次。评测者面临的压力之一，就是只报一次运行的数字，掩盖不确定性[^biderman2024lessons-e2]。

**写下来：** 在结果表里给每个数字加上运行次数和波动范围，例如"10 次运行，均值 0.62，95% 置信区间 0.58–0.66"。

### 第七步：大模型当研究工具时，拿人工判断验证它

用大模型代替人做标注、编码、打分或当被试时，必须说明这种代替是否合理[^baltes2026guidelines-e25]。大模型的表现高度依赖数据和任务，必须逐个任务验证；验证是所有用大模型做标注的论文的基本要求[^tornberg2024best-e9]。

**怎么做**（以标注为例，按 Törnberg 的流程）：

1. **先定义概念。** 把要标注的概念明确写下来，避免被大模型的理解牵着走[^tornberg2024best-e5]。
2. **在小样本上人机一起标注，反复修改。** 让人和大模型标注同一批样本，讨论分歧，修改编码手册（写明每个类别怎么判断的说明）和提示词，直到大模型和人足够一致。理想情况下，大模型应接近人与人之间的一致程度[^tornberg2024best-e6]。
3. **提示词定稿后，再在另一份验证集上测。** 不能用验证数据改提示词，否则会虚报精度[^tornberg2024best-e10]。验证集里每个类别至少要有 20–30 个样本，越多越好[^tornberg2024best-e11]。
4. **分组验证，检查失败。** 模型能力可能不同的子集（例如不同语言）要分别验证；检查失败的样本，说明模型的弱点为什么不影响后续结论[^tornberg2024best-e13]。

一致性常用 Krippendorff 的 α 系数衡量（1 表示完全一致）。按 Krippendorff 的标准，α 低于 0.667 的数据应当丢弃；0.667 到 0.8 之间只够得出初步结论；0.8 以上才算可靠[^baltes2026guidelines-e26]。

**大模型当评审员**（给输出打分）时：主观的判断，应当让大模型和一组人类专家各自独立评判同一批对象，再拿大模型的判断和汇总后的人类判断比较。人和大模型当评审都有系统偏差，例如偏爱带假引用或排版花哨的回答[^baltes2026guidelines-e38]。

**为什么**：几个模型彼此一致，可能只是有共同的偏差，所以要抽一部分和人类专家对照[^baltes2026guidelines-e25]。信度不等于效度：一个大模型可能每次都稳定地给出同样的错误答案[^baltes2026guidelines-e28]。

**容易错在哪**：把人工标注当成绝对正确。人工标注也不是标准答案，有时大模型的理解反而更好[^tornberg2024best-e7]。人和模型有分歧时，回到概念定义去判断，而不是默认人对 `[本项目分析]`。

> **不同的看法：大模型能做定性分析吗？**
>
> - 大模型准则提到，419 位有经验的定性研究者在一封公开信中认为：反思性主题分析等方法，需要有立场、能反思的研究者本人，用生成式人工智能做这类分析在方法上不相容[^baltes2026guidelines-e29]。准则自己的看法是，大模型可能更适合辅助研究者，而不是取代[^baltes2026guidelines-e27]。
> - Törnberg 认为不应全盘拒绝，而应把大模型纳入严格的标注流程来管住它的弱点；批评者说大模型主观、有缺陷、像黑箱、可能有偏差，这些往往同样适用于人类编码者[^tornberg2024best-e18]。
>
> 实际操作中 `[本项目分析]`：两种看法针对的任务不同。按明确的类别打标签（例如"这条评论是不是在报告缺陷"），可以按上面的流程验证后交给大模型；需要研究者本人解读的定性分析（见[访谈研究](interview_study.md)、[扎根理论](grounded_theory.md)），大模型最多当助手，结论由人负责，并在论文里写明它做了什么。

**例子** `[本项目分析]`：合约项目里，各模型的回答是一段文字。如果用另一个大模型从回答里抽出"报告了哪类漏洞、在哪一行"，就先由两个人各自标注一批回答，比较人与人、人与模型的一致性，修改抽取提示词；定稿后在另一批回答上验证，每类漏洞至少几十条，达到要求再用到全部回答上。

**写下来：** 一份编码手册：概念定义、每个类别的判断规则和例子、给大模型的提示词和参数；再加一张表，记录每轮的一致性系数。

### 第八步：算清成本

**怎么做：**

- 记录用了多少词元（token，模型处理文本的基本单位）、花了多少服务费，或者用了什么硬件[^baltes2026guidelines-e32]。
- 和传统方法比，说明大模型消耗的资源值得[^baltes2026guidelines-e32]。

**为什么**：成本既是大模型的优势，也是限制。大模型做标注、评判比人快、便宜：一个例子是用 GPT-4 标注花了两天、122.08 美元，同类的众包流程要几周、4508 美元[^baltes2026guidelines-e34]。另一方面，通过商业接口跑全套评测很贵，成本主要落在独立研究者身上[^biderman2024lessons-e3]。

**容易错在哪**：预算只按一次运行估。模型数 × 提示词版本数 × 重复次数 × 样本数，很快就会翻几十倍；先在预实验里量出一次完整运行的花费，再定重复次数和模型数 `[本项目分析]`。

**写下来：** 一张预算表：每个模型每次完整运行的词元数和费用，乘上计划的运行次数。

### 第九步：公开材料，写清局限

**怎么做：**

- **公开全部提示词**[^baltes2026guidelines-e11]。公开完整的提示词是完全复现的必要条件，但不够[^biderman2024lessons-e6]：尽量公开确切的评测代码，写清做了多少提示词调整、在哪些模型和评测集上调的、生成参数，以及从回答里提取答案的规则[^biderman2024lessons-e7]。
- **公开交互记录**，也就是发出的提示词和收到的回答[^baltes2026guidelines-e14]。把每个样本的得分和模型输出存下来，事后复核不必再花算力重跑[^biderman2024lessons-e8]。同时公开查询日期，用来应对输出随时间的漂移[^sallou2024breaking-e8]。
- **写局限。** 必须讨论为提高信度和可复现性做了什么[^baltes2026guidelines-e33]，必须讨论可能的数据泄露[^baltes2026guidelines-e31]。减轻外部效度威胁的办法包括：在多个模型、独立数据集、互补指标之间相互印证；改变配置、提示词、数据集做敏感性分析；隔一段时间重跑[^baltes2026guidelines-e30]。
- **保护敏感数据。** 把数据发给平台上的大模型之前，先把个人信息匿名化；没有仔细考虑伦理和法律问题，不要把专有或保密的数据发给接口或网页[^tornberg2024best-e17]。伦理的一般要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)。

**为什么**：和人的访谈记录不同，大模型的交互记录可以公开，便于别人复现、追踪模型随时间的变化、做二次研究[^baltes2026guidelines-e14]。结果不能逐字复现，本身不构成否定研究的理由[^baltes2026guidelines-e33]；但前提是你把能公开的都公开了，让别人能检查你做了什么 `[本项目分析]`。

**容易错在哪**：局限里只写"大模型的输出有随机性"一句，不说你做了什么、对结论有什么影响 `[本项目分析]`。效度威胁要逐条说明影响，见[效度与局限](../02_do-the-project/04_validity-and-limits.md)。

**写下来：** 一份研究材料清单：提示词全文和变更记录、实验元数据、评测代码、交互记录和原始输出、人工标注数据和编码手册，各放在哪里、以什么许可公开。

---

## 3. 检查清单

下面的"必须做到"和"做到更好"，分别对应大模型准则里的"必须"和"应当"[^baltes2026guidelines-e6]。"做得出色"一级，以及从其他资料补充的条目，是本手册的归纳；大模型准则面向软件工程，其他学科以本学科的规范为准 `[本项目分析]`。

**必须做到**

- [ ] 声明用了哪个大模型、怎么用、用在哪个环节；几种角色分别声明[^baltes2026guidelines-e7]
- [ ] 写明确切的模型或工具名称和版本、影响输出的所有参数、实验日期[^baltes2026guidelines-e8]
- [ ] 公开全部提示词，说清哪条用在哪个模型、哪个版本、什么配置上[^baltes2026guidelines-e11]
- [ ] 说明零样本还是少样本，以及示例怎么挑的[^baltes2026guidelines-e12]
- [ ] 说明每个指标为什么合适，不只说"前人用过"[^baltes2026guidelines-e18]
- [ ] 讨论可能的数据泄露及其对结果的影响[^baltes2026guidelines-e31]
- [ ] 用大模型代替人做标注、打分或当被试时，说明这种代替是否合理[^baltes2026guidelines-e25]
- [ ] 讨论为提高信度和可复现性做了什么[^baltes2026guidelines-e33]

**做到更好**

- [ ] 用了默认参数也写出来[^baltes2026guidelines-e8]
- [ ] 商业模型拿不到的信息，承认它是妨碍复现的局限[^baltes2026guidelines-e9]
- [ ] 重复实验，报告均值、置信区间等；比较时用推断统计和效应量[^baltes2026guidelines-e16]
- [ ] 说明重复次数的理由[^baltes2026guidelines-e17]
- [ ] 加一个开放模型作基线[^baltes2026guidelines-e23]
- [ ] 和更省资源的传统方法比较，讨论资源消耗值不值[^baltes2026guidelines-e15]
- [ ] 做错误分析，报告各类失败的比例[^baltes2026guidelines-e19]
- [ ] 公开交互记录[^baltes2026guidelines-e14]
- [ ] 大模型当标注员或评审员时，抽样和人类专家的判断对照[^baltes2026guidelines-e25]
- [ ] 报告词元数量、费用或硬件[^baltes2026guidelines-e32]
- [ ] 做提示词稳定性分析（社会科学标注的建议）[^tornberg2024best-e15]

**做得出色**

- [ ] 在多个模型、独立数据集、互补指标之间相互印证；做敏感性分析；隔一段时间重跑[^baltes2026guidelines-e30]
- [ ] 用蜕变改写的数据补充评测[^sallou2024breaking-e9]
- [ ] 新建评测集时，留不公开的题目、嵌入金丝雀字符串[^baltes2026guidelines-e20]
- [ ] 公开确切的评测代码[^biderman2024lessons-e7]

**这些情况可以不做，不算缺陷**

- 研究有人参与、没法让人用两个模型做任务，或者大模型只是研究中的次要环节时，不加开放模型基线[^baltes2026guidelines-e24]
- 用经过充分验证、广泛使用的评测集时，人工验证的必要性较小；但新建或改编评测集时仍应做[^baltes2026guidelines-e39]
- 结果不能逐字复现：讨论了为提高可复现性做了什么，这本身就不是否定研究的理由[^baltes2026guidelines-e33]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只跑一次就报数字 | 小幅提升可能再采样一次就没了[^biderman2024lessons-e10] |
| 用网页聊天界面做实验 | 不能设参数，不能控制版本[^tornberg2024best-e4] |
| 只写"用了 GPT-4" | 商业模型在版本号不变时也在变，读者不知道你用的是哪个[^baltes2026guidelines-e5] |
| 以为温度设为 0 就能复现 | 温度为 0 也很少能保证输出完全确定[^baltes2026guidelines-e10] |
| 用一个随手写的提示词比较所有模型 | 提示词会改变排名和结论[^biderman2024lessons-e4][^baltes2026guidelines-e13] |
| 在公开数据集上评测，不检查污染 | 模型可能见过答案，表现被高估[^sallou2024breaking-e1][^sainz2023nlp-e2] |
| 把格式错误当成能力不足 | 分数里混进了"能不能按格式作答"[^baltes2026guidelines-e37][^biderman2024lessons-e11] |
| 不和传统方法比 | 说明不了大模型值不值那份资源[^baltes2026guidelines-e15] |
| 用验证数据调提示词 | 会虚报精度[^tornberg2024best-e10] |
| 几个模型彼此一致，就当标注可信 | 可能只是共同的偏差[^baltes2026guidelines-e25] |

---

## 5. 延伸阅读

- **整体要求和审稿标准**：Baltes 等 2026 的软件工程大模型实证研究准则，在线版 llm-guidelines.org 持续更新。八条准则各有理由、建议、例子和给审稿人的提示，文末有按论文章节排列的报告清单。
- **大模型带来的效度威胁**：Sallou 等 2024，篇幅短，讲闭源模型、隐性泄露、可复现性三类威胁，并用 ChatGPT 生成测试做了示范。
- **评测的细节为什么重要**：Biderman 等 2024，评测框架 lm-eval 开发者的经验，讲提示词、实现细节和波动怎样改变结论。
- **数据污染**：Sainz 等 2023。
- **用大模型做文本标注**：Törnberg 2024，面向社会科学，从选模型、编码流程到验证和伦理。
- 本手册的相关页面：[基准评测](../07_fields/computer-science/practices/benchmarking.md)、[对照实验](controlled_experiment.md)、[工程研究](../07_fields/computer-science/practices/engineering_research.md)、[复现研究](replication.md)。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^baltes2026guidelines-e1]: Baltes 等 2026，§4。[证据](../../sources/notes/baltes2026guidelines.md#e1)
[^baltes2026guidelines-e2]: Baltes 等 2026，§4.1。[证据](../../sources/notes/baltes2026guidelines.md#e2)
[^baltes2026guidelines-e3]: Baltes 等 2026，§4.2、§4.2.3。[证据](../../sources/notes/baltes2026guidelines.md#e3)
[^baltes2026guidelines-e4]: Baltes 等 2026，§1。[证据](../../sources/notes/baltes2026guidelines.md#e4)
[^baltes2026guidelines-e5]: Baltes 等 2026，§1。[证据](../../sources/notes/baltes2026guidelines.md#e5)
[^baltes2026guidelines-e6]: Baltes 等 2026，§5。[证据](../../sources/notes/baltes2026guidelines.md#e6)
[^baltes2026guidelines-e7]: Baltes 等 2026，§5.1。[证据](../../sources/notes/baltes2026guidelines.md#e7)
[^baltes2026guidelines-e8]: Baltes 等 2026，§5.2.2。[证据](../../sources/notes/baltes2026guidelines.md#e8)
[^baltes2026guidelines-e9]: Baltes 等 2026，§5.2.2。[证据](../../sources/notes/baltes2026guidelines.md#e9)
[^baltes2026guidelines-e10]: Baltes 等 2026，§5.2.5。[证据](../../sources/notes/baltes2026guidelines.md#e10)
[^baltes2026guidelines-e11]: Baltes 等 2026，§5.3.2。[证据](../../sources/notes/baltes2026guidelines.md#e11)
[^baltes2026guidelines-e12]: Baltes 等 2026，§5.3.2。[证据](../../sources/notes/baltes2026guidelines.md#e12)
[^baltes2026guidelines-e13]: Baltes 等 2026，§5.3.1。[证据](../../sources/notes/baltes2026guidelines.md#e13)
[^baltes2026guidelines-e14]: Baltes 等 2026，§5.4.1、§5.4.4。[证据](../../sources/notes/baltes2026guidelines.md#e14)
[^baltes2026guidelines-e15]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e15)
[^baltes2026guidelines-e16]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e16)
[^baltes2026guidelines-e17]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e17)
[^baltes2026guidelines-e18]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e18)
[^baltes2026guidelines-e19]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e19)
[^baltes2026guidelines-e20]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e20)
[^baltes2026guidelines-e21]: Baltes 等 2026，§5.5.5。[证据](../../sources/notes/baltes2026guidelines.md#e21)
[^baltes2026guidelines-e22]: Baltes 等 2026，§5.5.5。[证据](../../sources/notes/baltes2026guidelines.md#e22)
[^baltes2026guidelines-e23]: Baltes 等 2026，§5.6、§5.6.4。[证据](../../sources/notes/baltes2026guidelines.md#e23)
[^baltes2026guidelines-e24]: Baltes 等 2026，§5.6.2。[证据](../../sources/notes/baltes2026guidelines.md#e24)
[^baltes2026guidelines-e25]: Baltes 等 2026，§5.7.2。[证据](../../sources/notes/baltes2026guidelines.md#e25)
[^baltes2026guidelines-e26]: Baltes 等 2026，§5.7.2。[证据](../../sources/notes/baltes2026guidelines.md#e26)
[^baltes2026guidelines-e27]: Baltes 等 2026，§4.3。[证据](../../sources/notes/baltes2026guidelines.md#e27)
[^baltes2026guidelines-e28]: Baltes 等 2026，§4.3。[证据](../../sources/notes/baltes2026guidelines.md#e28)
[^baltes2026guidelines-e29]: Baltes 等 2026，§4.3。[证据](../../sources/notes/baltes2026guidelines.md#e29)
[^baltes2026guidelines-e30]: Baltes 等 2026，§5.8.2。[证据](../../sources/notes/baltes2026guidelines.md#e30)
[^baltes2026guidelines-e31]: Baltes 等 2026，§5.8.2。[证据](../../sources/notes/baltes2026guidelines.md#e31)
[^baltes2026guidelines-e32]: Baltes 等 2026，§5.8.2。[证据](../../sources/notes/baltes2026guidelines.md#e32)
[^baltes2026guidelines-e33]: Baltes 等 2026，§5.8.2。[证据](../../sources/notes/baltes2026guidelines.md#e33)
[^baltes2026guidelines-e34]: Baltes 等 2026，§4.3。[证据](../../sources/notes/baltes2026guidelines.md#e34)
[^baltes2026guidelines-e35]: Baltes 等 2026，§2。[证据](../../sources/notes/baltes2026guidelines.md#e35)
[^baltes2026guidelines-e36]: Baltes 等 2026，§5.2.3。[证据](../../sources/notes/baltes2026guidelines.md#e36)
[^baltes2026guidelines-e37]: Baltes 等 2026，§5.5.2。[证据](../../sources/notes/baltes2026guidelines.md#e37)
[^baltes2026guidelines-e38]: Baltes 等 2026，§5.7.2、§4.3。[证据](../../sources/notes/baltes2026guidelines.md#e38)
[^baltes2026guidelines-e39]: Baltes 等 2026，§5.7.6。[证据](../../sources/notes/baltes2026guidelines.md#e39)
[^sallou2024breaking-e1]: Sallou 等 2024，§1。[证据](../../sources/notes/sallou2024breaking.md#e1)
[^sallou2024breaking-e2]: Sallou 等 2024，§2.1。[证据](../../sources/notes/sallou2024breaking.md#e2)
[^sallou2024breaking-e3]: Sallou 等 2024，§2.2。[证据](../../sources/notes/sallou2024breaking.md#e3)
[^sallou2024breaking-e4]: Sallou 等 2024，§2.2。[证据](../../sources/notes/sallou2024breaking.md#e4)
[^sallou2024breaking-e5]: Sallou 等 2024，§2.3。[证据](../../sources/notes/sallou2024breaking.md#e5)
[^sallou2024breaking-e6]: Sallou 等 2024，§2.3。[证据](../../sources/notes/sallou2024breaking.md#e6)
[^sallou2024breaking-e7]: Sallou 等 2024，§3.2.1。[证据](../../sources/notes/sallou2024breaking.md#e7)
[^sallou2024breaking-e8]: Sallou 等 2024，§3.2.1。[证据](../../sources/notes/sallou2024breaking.md#e8)
[^sallou2024breaking-e9]: Sallou 等 2024，§3.2.2。[证据](../../sources/notes/sallou2024breaking.md#e9)
[^sallou2024breaking-e10]: Sallou 等 2024，§3.2.2。[证据](../../sources/notes/sallou2024breaking.md#e10)
[^sallou2024breaking-e11]: Sallou 等 2024，§3.2.2。[证据](../../sources/notes/sallou2024breaking.md#e11)
[^biderman2024lessons-e2]: Biderman 等 2024，§2.2。[证据](../../sources/notes/biderman2024lessons.md#e2)
[^biderman2024lessons-e3]: Biderman 等 2024，§2.2。[证据](../../sources/notes/biderman2024lessons.md#e3)
[^biderman2024lessons-e4]: Biderman 等 2024，§3.1。[证据](../../sources/notes/biderman2024lessons.md#e4)
[^biderman2024lessons-e6]: Biderman 等 2024，§3.1。[证据](../../sources/notes/biderman2024lessons.md#e6)
[^biderman2024lessons-e7]: Biderman 等 2024，§3.2。[证据](../../sources/notes/biderman2024lessons.md#e7)
[^biderman2024lessons-e8]: Biderman 等 2024，§3.3。[证据](../../sources/notes/biderman2024lessons.md#e8)
[^biderman2024lessons-e9]: Biderman 等 2024，§4.1。[证据](../../sources/notes/biderman2024lessons.md#e9)
[^biderman2024lessons-e10]: Biderman 等 2024，§4.1。[证据](../../sources/notes/biderman2024lessons.md#e10)
[^biderman2024lessons-e11]: Biderman 等 2024，§4.1。[证据](../../sources/notes/biderman2024lessons.md#e11)
[^biderman2024lessons-e12]: Biderman 等 2024，§4.2。[证据](../../sources/notes/biderman2024lessons.md#e12)
[^biderman2024lessons-e13]: Biderman 等 2024，§4.3。[证据](../../sources/notes/biderman2024lessons.md#e13)
[^sainz2023nlp-e1]: Sainz 等 2023，摘要。[证据](../../sources/notes/sainz2023nlp.md#e1)
[^sainz2023nlp-e2]: Sainz 等 2023，摘要。[证据](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e4]: Sainz 等 2023，§5.1。[证据](../../sources/notes/sainz2023nlp.md#e4)
[^sainz2023nlp-e5]: Sainz 等 2023，§5.2。[证据](../../sources/notes/sainz2023nlp.md#e5)
[^tornberg2024best-e2]: Törnberg 2024，第 1 条。[证据](../../sources/notes/tornberg2024best.md#e2)
[^tornberg2024best-e3]: Törnberg 2024，第 1 条。[证据](../../sources/notes/tornberg2024best.md#e3)
[^tornberg2024best-e4]: Törnberg 2024，第 1 条。[证据](../../sources/notes/tornberg2024best.md#e4)
[^tornberg2024best-e5]: Törnberg 2024，第 2 条。[证据](../../sources/notes/tornberg2024best.md#e5)
[^tornberg2024best-e6]: Törnberg 2024，第 2 条。[证据](../../sources/notes/tornberg2024best.md#e6)
[^tornberg2024best-e7]: Törnberg 2024，第 2 条。[证据](../../sources/notes/tornberg2024best.md#e7)
[^tornberg2024best-e8]: Törnberg 2024，第 3 条。[证据](../../sources/notes/tornberg2024best.md#e8)
[^tornberg2024best-e9]: Törnberg 2024，第 4 条。[证据](../../sources/notes/tornberg2024best.md#e9)
[^tornberg2024best-e10]: Törnberg 2024，第 4 条。[证据](../../sources/notes/tornberg2024best.md#e10)
[^tornberg2024best-e11]: Törnberg 2024，第 4 条。[证据](../../sources/notes/tornberg2024best.md#e11)
[^tornberg2024best-e12]: Törnberg 2024，第 4 条。[证据](../../sources/notes/tornberg2024best.md#e12)
[^tornberg2024best-e13]: Törnberg 2024，第 4 条。[证据](../../sources/notes/tornberg2024best.md#e13)
[^tornberg2024best-e14]: Törnberg 2024，第 6 条。[证据](../../sources/notes/tornberg2024best.md#e14)
[^tornberg2024best-e15]: Törnberg 2024，第 8 条。[证据](../../sources/notes/tornberg2024best.md#e15)
[^tornberg2024best-e16]: Törnberg 2024，第 9 条。[证据](../../sources/notes/tornberg2024best.md#e16)
[^tornberg2024best-e17]: Törnberg 2024，第 7 条。[证据](../../sources/notes/tornberg2024best.md#e17)
[^tornberg2024best-e18]: Törnberg 2024，引言、结论。[证据](../../sources/notes/tornberg2024best.md#e18)
