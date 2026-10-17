# 内容分析：按编码手册把大量文本系统地编成类别

本文讲**内容分析**（content analysis）：拿一批已经记录下来的文本、图片、视频或帖子，按事先写好的规则，一段一段地编进类别，再统计或解读这些类别。新闻报道、广告、社交媒体帖子、政策文件、病历、开放式问卷回答、GitHub 上的问题报告，都可以是它的材料。

它有定量和定性两个变体。定量的内容分析把文本变成数字，回答"某类内容有多常见"；定性的内容分析也用类别，但更看重类别本身和它们的含义。研究涉及人的数据时，一般伦理要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md#4-研究涉及人或可能伤害别人时先保护人)，本文只讲内容分析本身。

**适用范围**：内容分析起源于传播学，社会学、心理学、护理学和健康研究、教育研究都常用；计算机里，人工给问题报告、代码审查评论、论坛帖子、论文归类，用的也是同一套逻辑。本文的编码者间信度部分依据传播学的资料（Lombard 等人的公开指南，Krippendorff 2004）；定性内容分析的步骤依据 Mayring（德国的心理学与社会科学传统）；显性和隐性内容的区分依据药学教育期刊上的一篇入门文章（Kleinheksel 等人）；一般步骤参考哥伦比亚大学公共卫生学院的方法页；抽样和计算机领域的例子来自软件工程。新闻传播学怎样看待这类研究，另见[媒体与传播学科概况](../07_fields/media-communication/README.md#内容分析测好报好编码者间信度)。

**常服务的套路**：[观察描述](../05_research-strategies/observe_describe.md)；材料是已发表的研究时，也服务[综合](../05_research-strategies/synthesize.md)。

**读完本文，你应该能：**

- 判断你的问题适不适合用内容分析，选定量还是定性、显性还是隐性；
- 定好分析单元，从一大堆文本里抽出样本；
- 写出一份别人拿去也能照着编的编码手册；
- 培训编码者，按传播学的做法测好、报好编码者间信度；
- 分清内容分析、访谈研究里的主题分析和扎根理论。

---

## 1. 这是什么研究，什么时候用

内容分析是从记录下来的交流中识别和解读意义的方法：把代表关键概念的小段数据分离出来，再套用或建立一个框架把它们组织起来，用来描述或解释一个现象[^kleinheksel2020demystifying-e1]。它的对象可以是任何被记录下来的交流：访谈转录稿、话语、观察记录、录像、文件等[^mayring2000qualitative-e2]。研究者可以据此推断文本中的信息、作者、受众，乃至文本所处的文化和时代[^columbia2023contentanalysis-e2]。

内容分析最初是严格的定量方法，统计事先确定的目标出现的频次[^kleinheksel2020demystifying-e2]。后来发展出定性的变体：Mayring 的定性内容分析，出发点就是保留传播学里定量内容分析的长处，再把它们用到定性、诠释性的分析步骤上[^mayring2000qualitative-e1]。

**它擅长回答的问题**：

- **"某类内容有多常见、怎样分布"**：新闻报道里某类框架占多大比例，健康类应用的说明里有多少条有依据，一批问题报告里各类缺陷各占多少；
- **"不同来源、不同时期有什么差别"**：两类媒体的报道有什么不同，某个话题的讨论十年间怎样变化；
- **"一批文本里有哪些类别"**：开放式问卷回答、用户反馈、论坛帖子可以归成哪几类。

它回答不了"为什么会这样"和"A 是否导致 B"。文本只是交流留下的痕迹，内容分析常常忽视文本产生的背景[^columbia2023contentanalysis-e12]；要知道作者为什么这样写，要配合[访谈研究](interview_study.md)；要检验因果，要用实验或[准实验](quasi_experiment.md)。

**和相近方法的区别**：

| | 内容分析 | [访谈研究](interview_study.md)里的主题分析 | [扎根理论](grounded_theory.md) | [仓库挖掘](../07_fields/computer-science/practices/repository_mining.md) |
|---|---|---|---|---|
| 材料 | 已有的任何文本、媒体，也可以是转录稿 | 自己做的访谈转录稿 | 访谈等数据，收集和分析交替进行 | 大量代码仓库、缺陷库的记录 |
| 类别从哪来 | 事先定好（演绎），或按规则从材料中归纳，最后写成编码手册 | 从数据中归纳出主题 | 从数据中生成，不套用事先定好的编码方案 | 多由程序抽取，部分人工标注 |
| 主要产出 | 类别和它们的频次、分布；或一套类别体系 | 几个主题 | 一个由概念和关系构成的理论 | 统计规律 |
| 数一数次数 | 定量变体的核心 | 次数多不等于更重要 | 只数不解读是反面模式 | 核心 |
| 编码者间信度 | 定量变体的关键部分 | 有争议，看研究立场 | 一般不要求 | 人工标注部分要求 |

依据：内容分析一列，类别处在分析的中心，事先定好的类别要有明确定义、例子和编码规则[^mayring2000qualitative-e4][^mayring2000qualitative-e9]，定量的目的是得到数值、说明普遍程度[^kleinheksel2020demystifying-e4]，编码者间信度是关键部分[^lombard2010practical-e3]；主题分析一列，主题不是数出来的[^braun2006using-e4]，信度有争议[^mcdonald2019reliability-e1]；扎根理论一列，不把数据归入事先定好的编码方案[^stol2016grounded-e11]，只数词、数编码而不解读是反面模式[^ralph2020empirical-e325]。仓库挖掘一列和整张表的归纳是本手册做的。

**一句话分清**：内容分析的核心产物是**一份别人拿去也能照着编的编码手册**，以及按它编出来的数据；主题分析的核心产物是研究者对数据的一种解读；扎根理论的核心产物是一个新理论。同样是给转录稿贴标签，你要是先写好类别定义、让两个人各自去编、再算一致性，那做的就是内容分析。

**还有两个邻居。** 把已发表的案例研究编码成变量再做统计，是[案例调查](case_survey.md)，它是内容分析用在一类特定材料上；系统综述里从每篇论文提取数据，也要一份编码方案，见[综述研究](review_study.md)。

**什么时候不合适。** Mayring 认为，研究问题高度开放、探索性强、会不断变化，用类别会成为束缚，或者打算做整体性而非分步的分析时，定性内容分析就不太合适[^mayring2000qualitative-e12]。这时考虑[访谈研究](interview_study.md)的主题分析或[扎根理论](grounded_theory.md)。

---

## 2. 怎么做

下面八步以定量内容分析为主线，定性变体不同的地方随处标出。

### 第一步：写清研究问题，决定定量还是定性、显性还是隐性

**怎么做：**

- **先写研究问题。** 选方法时，研究问题和材料的特点应当优先[^mayring2000qualitative-e13]。问题要写到能看出你要从文本推断什么：推断文本本身的特点，还是推断作者、受众、时代[^columbia2023contentanalysis-e2]。
- **决定定量还是定性。** 两者的实际区别在意图：定量的要得到数值，用来说明普遍程度或做统计；定性的要在文本中识别一个概念并用原文词句佐证，或给文本更有条理的结构[^kleinheksel2020demystifying-e4]。
- **决定意义在表面还是深处。** Kleinheksel 等人说，选哪种内容分析要做两个决定：分析的目标是什么，你认为意义在哪里[^kleinheksel2020demystifying-e11]。**显性内容**（manifest content）是字面上存在的东西，稍加训练就能识别和计数[^kleinheksel2020demystifying-e3]，例如"帖子里有没有附代码"；**隐性内容**（latent content）要解读言外之意[^kleinheksel2020demystifying-e5]，例如"这条评论是不是在讽刺"。
- **决定只看概念，还是也看概念之间的关系。** 概念分析确定概念是否出现、出现多少次；关系分析进一步考察概念之间的关系[^columbia2023contentanalysis-e4]。

**为什么：** 这几个决定会改变后面每一步。显性内容容易测出高信度，隐性内容难得多；定性变体对信度的要求也不同（见第六步）。

**容易错在哪：** 问题写成"看看这些帖子里有什么"，然后边读边想类别，最后数一数。这样得出的数字没法解释，因为类别是看了数据才定的。探索阶段可以这样读，但正式编码前要把类别和规则定下来。

### 第二步：定好分析单元

**怎么做：**

- **分清两种单元**：**抽样单元**是你抽出来的一份材料，例如一篇报道、一个问题报告、一篇论文；**编码单元**是你给它贴一个类别的那一段，例如一个句子、一条评论、一个段落。两者可以相同，也可以不同。
- **定编码单元的层次。** 哥伦比亚大学的方法页把第一步写成：决定分析层次，是词、词义、短语、句子还是主题[^columbia2023contentanalysis-e5]。意义单元怎么切没有唯一的办法，取决于分析类型；书面文本要决定按短语、句子还是段落切分[^kleinheksel2020demystifying-e7]。Mayring 也要求把材料切分成分析单元，一步步按规则处理[^mayring2000qualitative-e4]。
- **决定数"有没有"还是"有几次"。** 编码的是概念"是否出现"还是"出现几次"，会改变编码过程[^columbia2023contentanalysis-e7]。

**为什么：** 单元不定，两位编码者看同一份材料时，可能一个按整篇编、一个按句子编，信度从一开始就测不准。

**容易错在哪：** 一个问题报告里讨论了三个缺陷，你按"报告"抽样、按"报告"编码，就只能给它贴一个类别。先想清楚你最后要报告的是"多少份报告"还是"多少个缺陷"，再定单元。

### 第三步：抽样文本

**怎么做：**

- **写清总体。** 先说清你想把结论推广到哪一批文本，再说明你从哪里抽、怎么抽。Baltes 和 Ralph 建议把多数定量研究看作多阶段的抽样过程，作者要说清想推广到的总体，并反思每一步可能怎样带来偏差[^baltes2022sampling-e12]。以代表性为目标时，SIGSOFT（美国计算机协会软件工程分会）的抽样标准要求给出可重复的、算法式的抽样步骤说明，并说明每一步可能带来的偏差[^ralph2020empirical-e127]。
- **想清来源本身的偏差。** 再大的样本也消除不了抽样框的偏差[^baltes2022sampling-e5]。在软件仓库里，每个仓库都可能有难以预料的偏差[^baltes2022sampling-e14]。如果抽样框有偏差，可以换一个抽样框重做研究，例如在 GitHub 项目上发现的规律，再到 SourceForge 的项目上检验[^baltes2022sampling-e13]。
- **样本量要做得完。** 选文本时要平衡：信息要足够做彻底的分析，又不能多到编码不堪重负[^columbia2023contentanalysis-e10]。人工编码很慢，先估算每个单元要编几分钟，再决定抽多少。

**常见的计算机例子**：想知道"开源项目的安全相关问题报告里，各类问题各占多少"，抽样单元是问题报告。你要写清：从哪些项目抽（按什么标准选项目），时间范围，用什么关键词或标签筛出"安全相关"，筛完之后怎么随机抽。关键词筛选本身就会漏掉没写"security"的报告，这一点要写进局限。抽样怎样做、怎样论证，详见[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md#第三步筛选和抽样项目)。

**定性变体：** 定性内容分析常按目的选材料，不追求统计意义上的代表性；做法和理由见[访谈研究](interview_study.md#第一步选受访者)的抽样部分。

### 第四步：建编码手册

编码手册（codebook，Mayring 叫 coding agenda）是内容分析的核心。它告诉每个编码者：有哪些类别，每个类别是什么意思，什么情况下用，什么情况下不用。

**类别从哪里来：演绎还是归纳。**

Mayring 把定性内容分析的两个核心做法概括为：归纳地发展类别，演绎地应用类别[^mayring2000qualitative-e6]。

- **演绎**：现象已经有现成框架描述过，就事先根据理论或文献中的概念建编码[^kleinheksel2020demystifying-e6]。Hsieh 和 Shannon 把这种做法叫"定向式"内容分析：用已有理论的概念做演绎编码，进一步描述或验证理论[^kleinheksel2020demystifying-e12]。
- **归纳**：没有现成框架时，编码在分析中产生[^kleinheksel2020demystifying-e6]，Hsieh 和 Shannon 叫它"常规式"[^kleinheksel2020demystifying-e12]。经典的定量内容分析很少回答"类别从哪里来"[^mayring2000qualitative-e7]；Mayring 的做法是：先依据理论背景和研究问题定一个选取标准，决定看材料的哪些方面；按这个标准逐段处理材料，暂定类别；在反馈循环中修订、归并成主类别，并检查信度[^mayring2000qualitative-e8]。
- **混合**：先演绎，同时允许在编码中增加类别；或者坚持事先定好的类别。这要事先决定[^columbia2023contentanalysis-e6]。

和[扎根理论](grounded_theory.md)不同的是：内容分析即使用归纳的办法得出类别，最后也要把它们**固定成一份有定义、有规则的手册**，再拿去系统地编全部材料。

**每个类别写什么。**

Mayring 要求给每个类别写明确定义、例子和编码规则，准确规定什么情况下一段文本可以编入这个类别[^mayring2000qualitative-e9]。Kleinheksel 等人的手册至少有三栏：编码名称、编码说明、例子[^kleinheksel2020demystifying-e8]。在此基础上，建议每个类别写五样东西：

| 栏目 | 例子（给安全相关问题报告编"问题类型"） |
|---|---|
| 名称 | 访问控制 |
| 定义 | 报告的问题是：未经授权的人能做本不该允许他做的事 |
| 什么时候用 | 报告描述了绕过权限检查、越权调用、缺少身份验证 |
| 什么时候不用（和相邻类别怎么分） | 只是泄露了信息、没有越权操作的，编"信息泄露" |
| 例子 | 一两段真实材料中的原文 |

**还要事先定下的规则：**

- 允许多大程度的隐含：只算明说的，还是暗示的也算[^columbia2023contentanalysis-e8]；
- 和研究问题无关的内容怎么处理[^columbia2023contentanalysis-e9]；
- 一个单元能不能同时属于多个类别；拿不准时编哪一类（例如设一个"无法判断"类）。

类别定义、典型例句和区分相邻类别的规则，依据理论和材料写成，逐步补全，并随分析修订[^mayring2000qualitative-e10]。但我们建议，定量变体在正式编码开始后就要冻结手册，否则前后编的数据不可比。

**容易错在哪：** 定义只有一个词（"性能问题"），没写边界，两个编码者对"慢"算不算性能问题各有理解。好的检验办法是：把手册交给一个没参与讨论的人，看他能不能照着编。

### 第五步：培训编码者，预测试

**怎么做：**

1. **讲解手册，一起试编。** 大家读完编码手册、听完讲解后，各自独立给同一份材料编码[^kleinheksel2020demystifying-e9]。
2. **非正式地测信度，改手册。** 用少量最好不在正式样本里的单元非正式地测信度，反复修改编码表和说明，直到一致程度足够[^lombard2010practical-e16]。
3. **正式预测试。** 预测试样本的经验值是 30 个单元[^lombard2010practical-e8]。
4. **多轮迭代。** SIGSOFT 标准的优秀做法是：先标一部分数据，解决分歧，更新标注方案或判定规则，直到一致性达到最低阈值[^ralph2020empirical-e131]。

**为什么：** Krippendorff 指出，信度测试的很多问题来自三处：编码者并不真正独立，拿到的编码说明没法照着做，或者编码的材料他们看不懂[^krippendorff2004reliability-e2]。培训和预测试就是在正式编码前把后两个问题暴露出来。

**容易错在哪：** 用预测试时讨论过、改过的那批单元来算正式信度。那批单元大家已经对过答案，一致性会虚高。正式测信度要用新的单元。

### 第六步：正式编码，测编码者间信度

**编码者间信度**（intercoder reliability）指几位编码者各自独立判断一条信息的某个特征时，得出相同结论的程度[^lombard2010practical-e2]。有信度不保证结论有效，但信度没确立好，数据和解读就不能算有效[^lombard2010practical-e3]。Krippendorff 的说法是：一致性是测出来的东西，信度是想从中推断的东西；在内容分析里，信度最重要的含义是可复现[^krippendorff2004reliability-e1]。

**怎么做：**

1. **收数据前先选好指标。** 用哪个信度指标，必须在收集数据、评估信度之前选定[^lombard2010practical-e5]。
2. **抽信度样本。** 正式信度样本不少于 50 个单元或全样本的 10%，很少需要超过 300 个[^lombard2010practical-e9]。这个样本要代表待检验信度的那批数据[^krippendorff2004reliability-e5]。
3. **独立编码。** 信度测试的编码必须各自独立完成，不能商量或被指导；可能的话研究者本人不要当编码者[^lombard2010practical-e7]。
4. **算考虑了碰巧一致的指标。** 不要只用百分比一致率[^lombard2010practical-e11]；Krippendorff 主张明确不用它，尤其不要拿它当退路[^krippendorff2004reliability-e3]。举个极端的例子：所有编码者都只用同一个类别时，百分比一致率是 100%，但数据没有变化，也就没有任何信度证据[^krippendorff2004reliability-e4]。也不要用 Cronbach's alpha、Pearson 相关系数这类只衡量两人打分是否一起高低变化的指标[^lombard2010practical-e13]。哪一个指标"最好"没有共识[^lombard2010practical-e14]；Krippendorff's alpha 评价好、适用面广：可用于多名编码者，能处理不同样本量和缺失数据，也能用于有序和数值型变量[^lombard2010practical-e15]。选哪个取决于编码者人数、样本量和数据类型[^kleinheksel2020demystifying-e10]。
5. **逐个变量报告，取最低的。** 不要用所有变量合在一起的总体信度[^lombard2010practical-e12]。几个变量一起支撑结论时，逐个测，取最低的作为整体信度；把容易编的变量和难编的平均在一起会误导人[^krippendorff2004reliability-e8]。
6. **看置信区间，不做显著性检验。** 要参考置信区间；检验"一致性显著高于碰巧"对信度没有意义[^krippendorff2004reliability-e10]。
7. **不达标怎么办。** 可以去掉不可靠的区分、重新编码或合并类别、删掉不达标的变量[^krippendorff2004reliability-e9]，再重新测。
8. **其余材料怎么编。** Krippendorff 认为编码者要可以互换，可以各编不同的子样本，只要有足够的重复或重叠[^krippendorff2004reliability-e5]。编得久了，同一编码者的判断会随时间变；过一段时间重新编码一遍，能提高一致性和稳定性[^kleinheksel2020demystifying-e15]。

> **不同的看法：合格线定在哪？**
>
> - **Lombard 等人的指南**：系数 0.90 以上几乎总能接受，0.80 以上多数情况下可接受，某些探索性研究中对某些指标 0.70 也可能合适[^lombard2010practical-e6]。
> - **Krippendorff**：合格线要按"得出错误结论的代价"来定；他建议一般要求 α ≥ 0.800，只作初步结论时 α ≥ 0.667，但除了完全一致，没有神奇的数字[^krippendorff2004reliability-e7]。
> - **Mayring 的定性内容分析**：只用受过训练的课题组成员估计信度，并降低标准，Cohen's Kappa 0.7 以上即可[^mayring2000qualitative-e5]。
>
> 实际操作中：在论文里写明你用的指标和合格线、出处是谁，在收数据前就定下来，不要看了结果再选。

> **定性变体要不要算信度？**
>
> 看你的研究立场。Kleinheksel 等人指出，定性研究一般不用"信度""效度"，而用"可信赖性"[^kleinheksel2020demystifying-e17]。在显性内容分析里，编码几乎不需判断，一致性不高数据就无效；在隐性内容分析里，信度和效度此消彼长：规则写得越细，一致性越高，但编码结果可能离读者的理解越远[^kleinheksel2020demystifying-e13][^kleinheksel2020demystifying-e14]。SIGSOFT 的一致性补充标准认为，诠释主义的定性分析不适用编码者一致性的要求[^ralph2020empirical-e365]。两方理由和折中做法见[访谈研究](interview_study.md#第六步让分析可信)。

**容易错在哪：** 三个人投票解决分歧，就当信度问题解决了。用多数票解决分歧会让人安心，但不改变测得的信度[^krippendorff2004reliability-e9]。分歧怎样解决要写，但信度要用讨论**之前**各自独立编的结果来算。

### 第七步：分析

**怎么做**：

- **定量变体**：报告每个类别的频次和比例；比较不同来源、不同时期的分布；需要时做卡方检验等统计（一般讲法见[分析与解读](../02_do-the-project/07_analyze-and-interpret.md)）。比例最好附上置信区间，样本小时尤其要注意。
- **定性变体**：描述每个类别的含义，用原文例子支撑，说明类别之间的关系；Mayring 认为，研究问题需要时也可以分析编码类别的频次[^mayring2000qualitative-e8]。

**用软件和自动方法要小心。** 计算机程序是用来支持、而不是取代文本解读步骤的[^mayring2000qualitative-e11]。软件能准确数出一个词出现了多少次，却分不清每次用法的含义[^columbia2023contentanalysis-e11]。如果你用关键词规则、机器学习分类器或大模型来自动编码，就要把它当作又一个"编码者"：先在人工编好的样本上检验它和人的一致性，再用到全部数据上，并在论文里报告这个检验。

**容易错在哪：** 内容分析常见的缺点是缺乏理论基础、推断过度，常常只是数词频，忽视文本产生的背景[^columbia2023contentanalysis-e12]。"新闻里提到某词的次数增加了"，不等于"公众更关心它了"；从文本推断作者意图或社会态度，要说明推断的依据。

### 第八步：写报告

**怎么做：**

- **报告信度的最少信息。** 信度样本的大小、抽取方法和理由；每个变量、每个指标的信度值；分歧怎样解决等[^lombard2010practical-e10]。SIGSOFT 的一致性补充标准同样要求描述两名以上评分者如何独立评分、分歧如何解决，并报告合适的一致性统计量[^ralph2020empirical-e129]。
- **留下审计记录。** 编码怎样建立和定义、培训编码者用了什么材料、为保证编码者间信度做了哪些步骤[^kleinheksel2020demystifying-e16]。
- **公开编码手册。** 最好把完整的编码手册、编码示例和判定规则作为补充材料公开，让别人能复现。
- **写清抽样**：总体、来源、筛选和抽样的每一步，以及可能的偏差（见第三步）。

**写下来：** 在动手编码前，用一页纸写好：研究问题、定量还是定性、分析单元、抽样步骤、编码手册初稿、信度指标和合格线。这一页就是你的分析计划，以后的改动都对照它记录。

### 例子：用在贯穿全书的项目上

贯穿全书的项目主张"现有大模型漏洞检测的评测结果被数据泄露高估了"，主体是[基准评测](../07_fields/computer-science/practices/benchmarking.md)，但其中一个子问题很适合用内容分析回答：**已发表的大模型智能合约漏洞检测论文，有多少检查过数据泄露？**

- **研究问题和类型**：定量、显性内容分析，材料是已发表论文，所以也服务[综合](../05_research-strategies/synthesize.md)。
- **单元**：抽样单元是一篇论文；编码单元是论文里的"一项评测"（一篇论文可能在几个数据集上评测）。
- **抽样**：写清检索了哪些会议和预印本库、时间范围、检索词、纳入标准（例如"用大模型检测智能合约漏洞并报告了量化结果"）。做法可以借用[综述研究](review_study.md)的检索和筛选步骤。
- **编码手册（演绎）**：变量例如"是否报告了所用模型的训练数据截止日期""测试合约的公开时间是否早于这个截止日期""是否做了去重或泄露检查""测试集是否公开"。每个变量写定义、什么时候编"是"、什么时候编"无法判断"，各附一篇论文里的原文例子。
- **信度**：两人各自独立编 50 篇左右的信度样本，逐个变量算 Krippendorff's alpha，达不到合格线的变量修改定义后重测。
- **产出**：一张表，"在 N 项评测中，X% 没有报告任何泄露检查"。它本身不证明结果被高估了，证明这一点要靠基准评测部分的实验；它说明的是这个问题在文献里有多普遍。

同一领域的真实例子：Durieux 等人比较智能合约分析工具时，把各工具报告的漏洞类型人工对应到 DASP 的十类漏洞上，例如把"整数溢出"归到"算术"类[^durieux2020empirical-e10]。这是演绎地应用一套现成类别。他们承认人工标注可能标错，应对办法是全体作者各自标注，再讨论分歧达成一致[^durieux2020empirical-e14]。如果要报告编码者间信度，就要在讨论之前用各自独立的结果来算（见第六步）。

---

## 3. 检查清单

下面以传播学的信度指南（Lombard 等人，Krippendorff）和软件工程的 SIGSOFT 标准为主要依据；其他学科以本学科的规范为准。

**必须做到**

- [ ] 写清研究问题，说明做的是定量还是定性内容分析
- [ ] 定义分析单元，说明数的是"有没有"还是"有几次"[^columbia2023contentanalysis-e7]
- [ ] 写清抽样步骤和可能的偏差[^ralph2020empirical-e127][^baltes2022sampling-e12]
- [ ] 编码手册里每个类别有定义、例子和编码规则[^mayring2000qualitative-e9]
- [ ] 多人编码时，事先选好信度指标[^lombard2010practical-e5]，各自独立编码[^lombard2010practical-e7]
- [ ] 用考虑了碰巧一致的指标，不只报百分比一致率[^lombard2010practical-e11]
- [ ] 报告信度样本的大小和抽法、每个变量的信度值、分歧怎样解决[^lombard2010practical-e10]

**做到更好**

- [ ] 用不在正式样本里的单元培训和预测试，反复修改手册[^lombard2010practical-e16]
- [ ] 多轮"试编—解决分歧—改规则"，直到一致性达标[^ralph2020empirical-e131]
- [ ] 逐个变量报告信度，并以最低的一个作为整体信度[^krippendorff2004reliability-e8]
- [ ] 留下审计记录：手册怎样形成、培训材料、信度步骤[^kleinheksel2020demystifying-e16]
- [ ] 隔一段时间重新编一部分，检查稳定性[^kleinheksel2020demystifying-e15]
- [ ] 公开编码手册和编码示例

**做得出色**：信度报告置信区间[^krippendorff2004reliability-e10]；按得出错误结论的代价论证合格线[^krippendorff2004reliability-e7]；换一个抽样框重做，检验结论是否依赖来源[^baltes2022sampling-e13]

**这些情况可以不做，不算缺陷**：诠释取向的定性内容分析不计算编码者间信度[^ralph2020empirical-e365]；多人编码不现实或与研究立场不符时只有一个编码者[^ralph2020empirical-e367]。但这时要按定性研究的质量标准说明分析为什么可信，见[访谈研究](interview_study.md#第六步让分析可信)。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只报百分比一致率 | 没考虑碰巧一致；所有人都用同一个类别时它也是 100%[^lombard2010practical-e11][^krippendorff2004reliability-e4] |
| 用 Cronbach's alpha 或相关系数当信度 | 它们只衡量打分是否一起高低变化，不衡量编码是否相同[^lombard2010practical-e13] |
| 把所有变量的信度平均成一个数 | 容易编的变量会掩盖难编的变量[^krippendorff2004reliability-e8][^lombard2010practical-e12] |
| 算了几种指标，只报最好看的 | SIGSOFT 列出的反面模式[^ralph2020empirical-e132] |
| 信度低于合格线，仍说成"良好" | SIGSOFT 列出的反面模式[^ralph2020empirical-e132] |
| 编码者商量着编信度样本 | 信度测试必须各自独立[^lombard2010practical-e7] |
| 讨论解决分歧后才算信度 | 多数票或讨论不改变测得的信度[^krippendorff2004reliability-e9] |
| 类别定义只有一个词，没写边界和例子 | 别人没法照着编[^mayring2000qualitative-e9] |
| 只数词频，不看语境 | 软件分不清同一个词的不同含义[^columbia2023contentanalysis-e11]；数词频而忽视背景是常见缺点[^columbia2023contentanalysis-e12] |
| 不加检验地用关键词规则或模型自动编码 | 自动方法也是一个编码者，要先和人工编码比对 |
| 用大样本掩盖抽样框的偏差 | 再大的样本也消除不了抽样框的偏差[^baltes2022sampling-e5] |
| 把内容分析的计数说成"扎根理论" | 扎根理论不套用预设编码方案，只数不解读是它的反面模式[^stol2016grounded-e11][^ralph2020empirical-e325] |

---

## 5. 延伸阅读

- **定性内容分析入门**：Mayring 2000，开放获取，讲归纳发展类别和演绎应用类别的步骤，附一份编码手册示例。出自德国的心理学与社会科学传统。
- **显性和隐性内容怎么选**：Kleinheksel 等人 2020，开放获取，用教学数据的例子讲显性、隐性内容分析，并对照了 Hsieh 和 Shannon 的三种分法。出自药学教育。
- **编码者间信度怎么测、怎么报**：Lombard、Snyder-Duch 和 Bracken 的公开在线指南（2010 年更新），给出分步建议；Krippendorff 2004 对这份指南的回应，讲为什么不用百分比一致率、合格线怎样定。两者出自传播学，在合格线和指标选择上有分歧，可以对照着读。
- **一般步骤速览**：哥伦比亚大学公共卫生学院的内容分析方法页，讲概念分析和关系分析的步骤和优缺点。
- **没有开放全文、但常被引用的经典**：Hsieh 和 Shannon 2005 年在 Qualitative Health Research 上的"三种定性内容分析"，Elo 和 Kyngäs 2008 年的定性内容分析流程，以及 Krippendorff、Neuendorf 的内容分析教科书。本文没有直接引用它们，Hsieh 和 Shannon 的分法转引自 Kleinheksel 等人。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^kleinheksel2020demystifying-e1]: Kleinheksel 等人 2020，Introduction。[证据](../../sources/notes/kleinheksel2020demystifying.md#e1)
[^kleinheksel2020demystifying-e2]: Kleinheksel 等人 2020，Introduction。[证据](../../sources/notes/kleinheksel2020demystifying.md#e2)
[^kleinheksel2020demystifying-e3]: Kleinheksel 等人 2020，Qualitative Content Analysis。[证据](../../sources/notes/kleinheksel2020demystifying.md#e3)
[^kleinheksel2020demystifying-e4]: Kleinheksel 等人 2020，Qualitative Content Analysis。[证据](../../sources/notes/kleinheksel2020demystifying.md#e4)
[^kleinheksel2020demystifying-e5]: Kleinheksel 等人 2020，Qualitative Content Analysis。[证据](../../sources/notes/kleinheksel2020demystifying.md#e5)
[^kleinheksel2020demystifying-e6]: Kleinheksel 等人 2020，Creating and Using Codes。[证据](../../sources/notes/kleinheksel2020demystifying.md#e6)
[^kleinheksel2020demystifying-e7]: Kleinheksel 等人 2020，Creating and Using Codes。[证据](../../sources/notes/kleinheksel2020demystifying.md#e7)
[^kleinheksel2020demystifying-e8]: Kleinheksel 等人 2020，Manifest Content Analysis。[证据](../../sources/notes/kleinheksel2020demystifying.md#e8)
[^kleinheksel2020demystifying-e9]: Kleinheksel 等人 2020，Manifest Content Analysis。[证据](../../sources/notes/kleinheksel2020demystifying.md#e9)
[^kleinheksel2020demystifying-e10]: Kleinheksel 等人 2020，Manifest Content Analysis。[证据](../../sources/notes/kleinheksel2020demystifying.md#e10)
[^kleinheksel2020demystifying-e11]: Kleinheksel 等人 2020，How to Choose a Methodological Approach。[证据](../../sources/notes/kleinheksel2020demystifying.md#e11)
[^kleinheksel2020demystifying-e12]: Kleinheksel 等人 2020，Navigating Terminology。[证据](../../sources/notes/kleinheksel2020demystifying.md#e12)
[^kleinheksel2020demystifying-e13]: Kleinheksel 等人 2020，Ensuring Quality。[证据](../../sources/notes/kleinheksel2020demystifying.md#e13)
[^kleinheksel2020demystifying-e14]: Kleinheksel 等人 2020，Ensuring Quality。[证据](../../sources/notes/kleinheksel2020demystifying.md#e14)
[^kleinheksel2020demystifying-e15]: Kleinheksel 等人 2020，Ensuring Quality。[证据](../../sources/notes/kleinheksel2020demystifying.md#e15)
[^kleinheksel2020demystifying-e16]: Kleinheksel 等人 2020，Ensuring Quality。[证据](../../sources/notes/kleinheksel2020demystifying.md#e16)
[^kleinheksel2020demystifying-e17]: Kleinheksel 等人 2020，Ensuring Quality。[证据](../../sources/notes/kleinheksel2020demystifying.md#e17)
[^mayring2000qualitative-e1]: Mayring 2000，第 [2] 段。[证据](../../sources/notes/mayring2000qualitative.md#e1)
[^mayring2000qualitative-e2]: Mayring 2000，第 [4] 段。[证据](../../sources/notes/mayring2000qualitative.md#e2)
[^mayring2000qualitative-e4]: Mayring 2000，第 [7] 段。[证据](../../sources/notes/mayring2000qualitative.md#e4)
[^mayring2000qualitative-e5]: Mayring 2000，第 [7] 段。[证据](../../sources/notes/mayring2000qualitative.md#e5)
[^mayring2000qualitative-e6]: Mayring 2000，第 [8] 段。[证据](../../sources/notes/mayring2000qualitative.md#e6)
[^mayring2000qualitative-e7]: Mayring 2000，第 [9] 段。[证据](../../sources/notes/mayring2000qualitative.md#e7)
[^mayring2000qualitative-e8]: Mayring 2000，第 [12] 段。[证据](../../sources/notes/mayring2000qualitative.md#e8)
[^mayring2000qualitative-e9]: Mayring 2000，第 [15] 段。[证据](../../sources/notes/mayring2000qualitative.md#e9)
[^mayring2000qualitative-e10]: Mayring 2000，第 [17] 段。[证据](../../sources/notes/mayring2000qualitative.md#e10)
[^mayring2000qualitative-e11]: Mayring 2000，第 [18] 段。[证据](../../sources/notes/mayring2000qualitative.md#e11)
[^mayring2000qualitative-e12]: Mayring 2000，第 [27] 段。[证据](../../sources/notes/mayring2000qualitative.md#e12)
[^mayring2000qualitative-e13]: Mayring 2000，第 [28] 段。[证据](../../sources/notes/mayring2000qualitative.md#e13)
[^krippendorff2004reliability-e1]: Krippendorff 2004，Relation Between Agreement and Reliability，作者稿第 3 页。[证据](../../sources/notes/krippendorff2004reliability.md#e1)
[^krippendorff2004reliability-e2]: Krippendorff 2004，作者稿第 3 页。[证据](../../sources/notes/krippendorff2004reliability.md#e2)
[^krippendorff2004reliability-e3]: Krippendorff 2004，作者稿第 10 页。[证据](../../sources/notes/krippendorff2004reliability.md#e3)
[^krippendorff2004reliability-e4]: Krippendorff 2004，作者稿第 10 页。[证据](../../sources/notes/krippendorff2004reliability.md#e4)
[^krippendorff2004reliability-e5]: Krippendorff 2004，Recommendations (i)。[证据](../../sources/notes/krippendorff2004reliability.md#e5)
[^krippendorff2004reliability-e7]: Krippendorff 2004，Recommendations (iii)。[证据](../../sources/notes/krippendorff2004reliability.md#e7)
[^krippendorff2004reliability-e8]: Krippendorff 2004，Recommendations (iv)。[证据](../../sources/notes/krippendorff2004reliability.md#e8)
[^krippendorff2004reliability-e9]: Krippendorff 2004，Recommendations (iv)。[证据](../../sources/notes/krippendorff2004reliability.md#e9)
[^krippendorff2004reliability-e10]: Krippendorff 2004，Recommendations (iii)。[证据](../../sources/notes/krippendorff2004reliability.md#e10)
[^columbia2023contentanalysis-e2]: 哥伦比亚大学公共卫生学院方法页，Overview。[证据](../../sources/notes/columbia2023contentanalysis.md#e2)
[^columbia2023contentanalysis-e4]: 哥伦比亚大学公共卫生学院方法页，Types of Content Analysis。[证据](../../sources/notes/columbia2023contentanalysis.md#e4)
[^columbia2023contentanalysis-e5]: 哥伦比亚大学公共卫生学院方法页，Conceptual Analysis 第 1 步。[证据](../../sources/notes/columbia2023contentanalysis.md#e5)
[^columbia2023contentanalysis-e6]: 哥伦比亚大学公共卫生学院方法页，Conceptual Analysis 第 2 步。[证据](../../sources/notes/columbia2023contentanalysis.md#e6)
[^columbia2023contentanalysis-e7]: 哥伦比亚大学公共卫生学院方法页，Conceptual Analysis 第 3 步。[证据](../../sources/notes/columbia2023contentanalysis.md#e7)
[^columbia2023contentanalysis-e8]: 哥伦比亚大学公共卫生学院方法页，Conceptual Analysis 第 4–5 步。[证据](../../sources/notes/columbia2023contentanalysis.md#e8)
[^columbia2023contentanalysis-e9]: 哥伦比亚大学公共卫生学院方法页，Conceptual Analysis 第 6 步。[证据](../../sources/notes/columbia2023contentanalysis.md#e9)
[^columbia2023contentanalysis-e10]: 哥伦比亚大学公共卫生学院方法页，Relational Analysis。[证据](../../sources/notes/columbia2023contentanalysis.md#e10)
[^columbia2023contentanalysis-e11]: 哥伦比亚大学公共卫生学院方法页，Reliability and Validity。[证据](../../sources/notes/columbia2023contentanalysis.md#e11)
[^columbia2023contentanalysis-e12]: 哥伦比亚大学公共卫生学院方法页，Disadvantages of Content Analysis。[证据](../../sources/notes/columbia2023contentanalysis.md#e12)
[^lombard2010practical-e2]: Lombard 等人 2010，第 2 节。[证据](../../sources/notes/lombard2010practical.md#e2)
[^lombard2010practical-e3]: Lombard 等人 2010，第 3 节。[证据](../../sources/notes/lombard2010practical.md#e3)
[^lombard2010practical-e5]: Lombard 等人 2010，第 4 节第 1 步。[证据](../../sources/notes/lombard2010practical.md#e5)
[^lombard2010practical-e6]: Lombard 等人 2010，第 4 节第 3 步。[证据](../../sources/notes/lombard2010practical.md#e6)
[^lombard2010practical-e7]: Lombard 等人 2010，第 4 节第 5 步。[证据](../../sources/notes/lombard2010practical.md#e7)
[^lombard2010practical-e8]: Lombard 等人 2010，第 4 节第 5 步。[证据](../../sources/notes/lombard2010practical.md#e8)
[^lombard2010practical-e9]: Lombard 等人 2010，第 4 节第 6 步。[证据](../../sources/notes/lombard2010practical.md#e9)
[^lombard2010practical-e10]: Lombard 等人 2010，第 4 节第 8 步。[证据](../../sources/notes/lombard2010practical.md#e10)
[^lombard2010practical-e11]: Lombard 等人 2010，第 4 节。[证据](../../sources/notes/lombard2010practical.md#e11)
[^lombard2010practical-e12]: Lombard 等人 2010，第 4 节。[证据](../../sources/notes/lombard2010practical.md#e12)
[^lombard2010practical-e13]: Lombard 等人 2010，第 4 节。[证据](../../sources/notes/lombard2010practical.md#e13)
[^lombard2010practical-e14]: Lombard 等人 2010，第 5 节。[证据](../../sources/notes/lombard2010practical.md#e14)
[^lombard2010practical-e15]: Lombard 等人 2010，第 5 节。[证据](../../sources/notes/lombard2010practical.md#e15)
[^lombard2010practical-e16]: Lombard 等人 2010，第 4 节第 4 步。[证据](../../sources/notes/lombard2010practical.md#e16)
[^baltes2022sampling-e5]: Baltes & Ralph 2022，§2.6。[证据](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e12]: Baltes & Ralph 2022，§2.5。[证据](../../sources/notes/baltes2022sampling.md#e12)
[^baltes2022sampling-e13]: Baltes & Ralph 2022，§6.2。[证据](../../sources/notes/baltes2022sampling.md#e13)
[^baltes2022sampling-e14]: Baltes & Ralph 2022，§6.2。[证据](../../sources/notes/baltes2022sampling.md#e14)
[^ralph2020empirical-e127]: SIGSOFT 抽样补充标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e127)
[^ralph2020empirical-e129]: SIGSOFT 编码者一致性补充标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e131]: SIGSOFT 编码者一致性补充标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e131)
[^ralph2020empirical-e132]: SIGSOFT 编码者一致性补充标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e132)
[^ralph2020empirical-e325]: SIGSOFT 扎根理论标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e325)
[^ralph2020empirical-e365]: SIGSOFT 编码者一致性补充标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e365)
[^ralph2020empirical-e367]: SIGSOFT 编码者一致性补充标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e367)
[^braun2006using-e4]: Braun & Clarke 2006，What counts as a theme?。[证据](../../sources/notes/braun2006using.md#e4)
[^mcdonald2019reliability-e1]: McDonald 等人 2019，§1、§2.2。[证据](../../sources/notes/mcdonald2019reliability.md#e1)
[^stol2016grounded-e11]: Stol 等人 2016，§2.1。[证据](../../sources/notes/stol2016grounded.md#e11)
[^durieux2020empirical-e10]: Durieux 等人 2020，§3.1。[证据](../../sources/notes/durieux2020empirical.md#e10)
[^durieux2020empirical-e14]: Durieux 等人 2020，§4.2。[证据](../../sources/notes/durieux2020empirical.md#e14)
