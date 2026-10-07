# 观察性流行病学研究

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲怎样做好三种最常见的观察性流行病学研究：**队列研究、病例对照研究、横断面研究**。观察性研究的意思是：研究者不施加干预，只是"观察"[^song2010observational-e1]。

[健康科学领域概况](../README.md)已经讲过[观察性研究的三个坑](../README.md#观察性研究的三个坑)（混杂、测量不准、谁参加了研究），也讲过[先说清关联还是因果](../README.md#动手前先说清你要回答关联问题还是因果问题)和"目标试验"的基本想法；三种设计的一句话定义见[临床医学篇](../../clinical-medicine/README.md#常见的研究类型)。本文默认你读过这些，只讲**具体怎么做**。用登记、医保、电子病历等现成数据时的报告要求，见领域概况的[这一节](../README.md#用常规收集的数据写清编码链接和数据的来历)，本文只补充几条。

**读完本文，你应该能：** 按问题选对设计；写清暴露、结局和随访起点，选好对照；用因果图挑选要调整的混杂因素，认出选择偏倚和信息偏倚；设计敏感性分析，并按报告规范写论文。

---

## 1. 这是什么研究，什么时候用

三种设计的区别，在于**从哪里开始选人**：

| | 队列研究 | 病例对照研究 | 横断面研究 |
|---|---|---|---|
| 怎么选人 | 按暴露选人，跟踪看谁发生结局[^song2010observational-e2] | 先找到病例，再选对照；对照代表产生病例的那个人群[^vandenbroucke2007strobe-e14] | 在同一时间点调查一个样本 `[本项目分析]` |
| 擅长 | 罕见暴露；一个暴露、多个结局[^song2010observational-e2]；在随访中多次测量[^vandenbroucke2007strobe-e16] | 罕见结局、潜伏期长的结局[^song2010observational-e3] | 了解现状（如患病率）`[本项目分析]`；分析性的横断面研究也可以量化暴露和疾病的关联[^vandenbroucke2007strobe-e15] |
| 主要弱点 | 样本大、随访长、成本高[^song2010observational-e2] | 算不出暴露组和非暴露组的发病率[^song2010observational-e3]；有回忆偏倚的风险[^vandenbroucke2007strobe-e26] | 难以确定暴露发生在疾病之前[^vandenbroucke2007strobe-e15] |

**怎么选** `[本项目分析，依据上表资料]`：

- 结局很罕见（例如一种少见的先天畸形）：病例对照研究。等着队列里出现足够的病例，往往要很多人、很多年。
- 暴露很罕见（例如某种职业接触），或想看同一个暴露的多个结局：队列研究。
- 想知道"现在有多少人患病、有某种行为"：横断面研究。想推断因果时，先问自己：暴露一定发生在疾病之前吗？像基因这类与生俱来的特征，先后是确定的。

**两个命名问题。** 不要只说"前瞻性""回顾性"。STROBE（观察性流行病学研究的报告规范）的解释文章说这两个词定义不清，建议写清数据具体是怎样、在什么时候收集的[^vandenbroucke2007strobe-e17]。只跟踪一组人、没有对照组的研究，是**病例系列**，不是队列研究[^song2010observational-e4]。

**和相近类型的区别** `[本项目分析]`：

- **随机对照试验**：研究者分配干预，见[临床医学篇](../../clinical-medicine/README.md#常见的研究类型)。观察性研究的因果分析，可以看作在模拟一个做不了的试验（见第一步）。
- **计算机篇的[数据科学研究](../../../06_methods/data_science.md)**：那里重点是预测，防的是数据泄漏；本文的研究多数想回答病因或效果问题，主要对手是混杂和偏倚。用同一份电子病历，"预测谁会再入院"和"某种药是否减少再入院"是两种研究。
- **计算机篇的[纵向研究](../../../06_methods/longitudinal_study.md)**：队列研究也是长期重复观察同一批人，那篇讲的时点选择、流失、相依数据分析都适用。不同的是，队列研究的核心是**比较暴露组和非暴露组的结局**，所以要多花力气在混杂和选择偏倚上。

## 2. 怎么做

### 第一步：把问题写成一个"目标试验"

先分清关联问题还是因果问题：纯粹描述关联，不需要调整混杂[^hernan2018cword-e7]（理由见[领域概况](../README.md#动手前先说清你要回答关联问题还是因果问题)）。如果是因果问题，先写出你想做但做不了的那个试验的方案，再说明怎样用观察性数据去模拟它[^hernan2020whatif-e1][^hernan2016target-e1]。

**怎么做**：Hernán 和 Robins 2016 年的文章列出目标试验方案的 7 个部分，逐项写下来[^hernan2016target-e2]：

(1) 纳入标准：要让每个人原则上都能接受所比较的每一种处理[^hernan2020whatif-e2]；(2) 要比较的处理策略，包括什么时候开始、什么时候结束；(3) 分配方式；(4) 随访期；(5) 关心的结局；(6) 关心的因果对比（例如"开始用药"对"不用药"）；(7) 分析计划。

**为什么**：逼你想清楚到底在比较什么 `[本项目分析]`。例如直接比较随访开始时体重指数为 25 和 30 的人的死亡风险，相当于模拟一个"让人在随访开始时一下子大幅改变体重"的试验，这种干预并不现实。可以改问一个更现实的问题，例如"从 40 岁起，只要体重指数高于 25，每年减 5%"[^hernan2020whatif-e3]。

**容易错在哪里**：

- **随访起点（"零时刻"）定错。** 纳入标准要在零时刻满足，结局从这一刻之后开始计[^hernan2016target-e5]。用现成数据时，最好把"符合条件的人开始某种处理的时刻"定为零时刻[^hernan2016target-e6]。零时刻晚于开始处理的时刻，中间发生的结局就漏掉了[^hernan2016target-e5]。
- **按未来的事件选人。** 纳入标准不能写成"随访期间用过这种药的人"这类基线之后才知道的事[^hernan2016target-e3]。类似地，只招募 50 岁的人、却研究"一生的暴露"，也可能产生选择偏倚[^hernan2020whatif-e19]。
- **比较对象选得太容易混杂。** 拿一种治疗和"不治疗"比，混杂可能特别严重；和另一种积极治疗比会好一些[^hernan2016target-e9]。
- 很少能模拟出最理想的试验。论文里写出方案和流程图，并说明你模拟的试验和理想试验差在哪里[^hernan2016target-e10]。病例对照研究也能用这个思路：先想清楚病例和对照是从哪个随访研究（队列）里抽出来的[^hernan2016target-e11]。

### 第二步：定义暴露和结局

**怎么做**：写清所有结局、暴露、潜在混杂因素和效应修饰因素（会改变暴露效应大小的因素）的定义，适用时给出诊断标准[^vandenbroucke2007strobe-e23]。病例对照研究要在选病例之前就定好纳入和排除标准[^song2010observational-e7]。

**为什么**：用现成数据做回顾性队列时，研究者对数据收集几乎没有控制，数据可能不完整、不准确，或各人测量方式不一致[^song2010observational-e10]。同一个编码也可能指不同的东西：Hernán 和 Robins 举例，数据库里的"乳腺癌"编码，可能是确诊时记的，也可能只是医生怀疑、开了检查时记的；所以要请教熟悉数据的人，并做数据验证[^hernan2016target-e4]。不验证结局，可能得出误导性的估计[^hernan2016target-e12]。

**容易错在哪里**：把连续的暴露分组时，事后从几种切点中挑一种，要告诉读者；为了让 P 值最小而挑切点，会夸大关联[^vandenbroucke2007strobe-e24]。

### 第三步：选研究人群和对照

**队列研究**：暴露组和非暴露组要来自同一个源人群（研究对象所来自的那个总体）；不可能发生该结局的人要排除[^song2010observational-e5]。失访怎么处理，最好在规划时就定下来[^vandenbroucke2007strobe-e36]；分析时尽量比较留下的人和失访的人有没有系统差异[^song2010observational-e6]。

**病例对照研究**：原则是**对照要反映产生病例的那个人群**[^vandenbroucke2007strobe-e18]。

- **医院对照**（患别的病的人）：对来自医院的病例，它更能代表医院的服务人群，回忆的可比性更好，也容易招募；但如果你研究的暴露会影响对照所患疾病的发病或住院，就会出问题[^vandenbroucke2007strobe-e19]。What If 一书的例子：研究雌激素与冠心病，却优先从髋部骨折的女性里选对照，而雌激素能减少髋部骨折，结果就偏了[^hernan2020whatif-e14]。
- **注意病例从哪来**：从医院选的病例，病情往往比社区里的更重[^song2010observational-e7]。让病例和对照经同样的转诊途径进入诊断，可以抵消这类偏倚[^vandenbroucke2007strobe-e28]。
- **对照的数量**：每个病例配到大约三四个对照，精度可能提高[^song2010observational-e8]。

**匹配要慎用。** 匹配直觉上很吸引人，但方法学者不建议在病例对照研究中例行匹配[^vandenbroucke2007strobe-e20]。匹配因素和暴露有关时，用了匹配却不做匹配或分层分析，比值比（病例对照研究常用的关联指标）通常会偏向 1，也就是偏向"无关联"[^vandenbroucke2007strobe-e22]。最危险的是按因果通路上的变量匹配，例如研究试管婴儿与围产期死亡时按出生体重匹配，这种偏倚分析时补救不了[^vandenbroucke2007strobe-e21]。

### 第四步：测量暴露，尤其是自我报告和饮食

为什么测不准会出问题，见领域概况的[坑二](../README.md#坑二暴露测不准尤其是饮食)。具体做法：

- **两组用同样的方法测。** 访谈者先问完所有病例再问对照，会因为越问越熟练带来偏倚，可以随机安排访谈顺序[^vandenbroucke2007strobe-e25]。STROBE 解释文章引用的一个例子：匹配的病例和对照的样本总在同一批次检测，实验室人员分不出谁是病例[^vandenbroucke2007strobe-e45]。
- **能设盲就设盲。** 病例回忆或报告过去暴露的准确程度可能和对照不同（回忆偏倚）；访谈者知道研究假设，可能有意无意地选择性收集数据[^vandenbroucke2007strobe-e26]。What If 一书的例子：分娩后才让母亲回忆孕期饮酒量，回忆会受妊娠结局的影响[^hernan2020whatif-e17]。用训练有素的访谈者、标准化的访谈来减少访谈者偏倚[^song2010observational-e9]。
- **从根上改进测量。** What If 一书说，对付测量偏倚最好的办法，就是改进测量程序本身[^hernan2020whatif-e18]。

**饮食**格外难测。美国国家癌症研究所（National Cancer Institute）的饮食评估入门资料说，饮食很少能直接观察，通常靠 24 小时膳食回顾、膳食记录、食物频率问卷等自我报告工具[^nci2025dietprimer-e1]；研究关心的常常是"平常吃多少"（长期平均），不是某一天吃了什么[^nci2025dietprimer-e2]。食物频率问卷主要用来评估长期平均摄入[^lachat2016strobenut-e2]。几件要知道的事：

- **误报不可避免**，有少报也有多报[^nci2025dietprimer-e6]。能量少报与体重指数的关系最一致[^nci2025dietprimer-e8]，所以研究饮食与肥胖相关疾病时，误报本身就可能和结局有关 `[本项目分析]`。
- **误差的方向不一定。** 只有一个饮食暴露、且只有个体内随机误差时，关联总会被削弱[^nci2025dietprimer-e3]；同时有系统误差时，可能被削弱，也可能被夸大[^nci2025dietprimer-e4]；模型里还有别的、同样测不准的饮食变量时，也可能被削弱或夸大[^nci2025dietprimer-e5]。所以"测量误差只会让结果偏保守"这种说法不总成立 `[本项目分析]`。
- **可以做的**：多次测量取平均[^nci2025dietprimer-e9]；做能量调整[^lachat2016strobenut-e5]；删掉误报者要谨慎，可以做"排除与不排除"的敏感性分析[^nci2025dietprimer-e7]，并比较排除前后参与者的特征[^lachat2016strobenut-e4]。
- **验证研究要看清参照是什么。** 理想的参照很少，只有双标水（测能量）、24 小时尿氮（测蛋白质）等几种；实际中常用 24 小时回顾或膳食记录这类不理想的参照[^lachat2016strobenut-e3]。

### 第五步：处理混杂——先画因果图，再定调整什么

**怎么做**：
1. **设计阶段就想好混杂因素**，这决定了要详细收集哪些数据；设计上可以用限制（例如只研究某个年龄段）或匹配[^vandenbroucke2007strobe-e29]。拿不到某个混杂因素的数据，就做敏感性分析，估计它可能带来的偏倚[^hernan2020whatif-e10]。
2. **画一张因果图**（有向无环图，directed acyclic graph）：把你认为的因果关系画成箭头。Tennant 等人 2021 年综述了健康研究中这种图的用法：1999—2017 年发表的 234 篇用了这种图的原创健康研究中，21% 写明了要估计的量，48% 报告了由图推出的调整集，62% 公开了至少一张图[^tennant2021dags-e1]。他们的建议包括：
   - 画进所有说得通的混杂因素，**包括没有测量的**[^tennant2021dags-e3]；
   - 排列变量时，让箭头都朝同一个方向（从左到右或从上到下）[^tennant2021dags-e7]；
   - 两个变量之间不画箭头，等于假设两者完全没有因果作用[^tennant2021dags-e4]，所以去掉箭头要有理由 `[本项目分析]`；
   - 把图放进正文或补充材料，或给出在线链接[^tennant2021dags-e2]。
3. **由图推出要调整的变量**（调整集），在论文里写明；如果另用了别的调整集，说明理由，结果分开报告[^tennant2021dags-e5]。研究目的里先写清要估计的量[^tennant2021dags-e6]。
4. **分析时用分层或多变量模型调整**[^vandenbroucke2007strobe-e30]。

**为什么不能只靠统计挑变量**：只凭关联或统计标准，不足以判断什么是混杂[^hernan2020whatif-e6]。从观察性数据做因果推断，需要事先的因果知识；把它画成图，你的假设就变得明确，别人也能具体地批评[^hernan2020whatif-e7]。另见领域概况的["不要让软件替你挑混杂因素"](../README.md#动手前先说清你要回答关联问题还是因果问题)。

**容易错在哪里**：

- **调整了不该调整的变量。** 一般不要调整受暴露或结局影响的变量[^hernan2020whatif-e8]，例如暴露到疾病因果通路上的中间变量[^vandenbroucke2007strobe-e31]。
- **按"加入后估计值变了多少"挑变量，却不说标准。** 用这种方法，要报告多大的变化才纳入[^vandenbroucke2007strobe-e32]。
- **以为调整了就安全。** 混杂因素本身测不准，就会留下残余混杂。社会经济地位就是典型：收入、教育、职业都只是替代指标[^vandenbroucke2007strobe-e47]。
- **两种因果结构都说得通时只选一种。** 应分别分析，并写明每种分析成立需要什么假设[^hernan2020whatif-e9]。
- 常见的混杂结构要认得：例如"身体好"让人能当消防员、也让人死亡风险低[^hernan2020whatif-e4]；尚未发病的亚临床疾病让人少运动、又增加发病风险（常叫"反向因果"）[^hernan2020whatif-e5]。

### 第六步：防选择偏倚和信息偏倚

**选择偏倚**是由"哪些人进入分析"制造出来的关联；它和混杂不同，随机试验里也会有[^hernan2020whatif-e12]。随机化能防混杂，但防不了随机化之后的选择偏倚[^hernan2020whatif-e15]。来源包括：只分析结局数据完整的人（不管数据为什么缺）[^hernan2020whatif-e13]，以及前面讲的对照选择不当[^hernan2020whatif-e14]、零时刻定错[^hernan2016target-e5]。参与者自己选择参加与否带来的偏倚，见领域概况的[坑三](../README.md#坑三谁参加了研究本身就可能制造关联)。

**信息偏倚**来自测量。除了第四步的回忆偏倚，还要防**检出偏倚**：例如吃某种会引起胃部不适的药的人，做胃镜更多，于是查出更多溃疡，即使药并不导致溃疡；可以测量各组接受医疗检查的强度，并在分析中调整[^vandenbroucke2007strobe-e27]。理想情况下，结局判定不应受"知道谁用了药"的影响；从死亡登记独立获取的死亡就不受影响[^hernan2016target-e8]。测量偏倚在任何设计中都可能出现，解释结果时总要考虑[^hernan2020whatif-e16]。

### 第七步：分析

- **主要分析事先写进方案**，报告时说明哪些分析是看了数据才想到的[^vandenbroucke2007strobe-e33]。这就是通用篇讲的[探索性和验证性之分](../../../general/1_before/04_research_design.md#4-分清探索性研究和验证性研究)。
- **同时给出未调整和调整后的估计**，读者能看出调整让结果变了多少、往哪个方向变[^vandenbroucke2007strobe-e34]。
- **缺失数据**：只分析数据完整的人，可能有偏，而且总会损失效率；各种缺失数据处理方法的假设一般无法验证，最好当作敏感性分析来看[^vandenbroucke2007strobe-e35]。给混杂因素加一个"缺失"类别，可能增加残余混杂[^vandenbroucke2007strobe-e46]。
- **病例对照研究不要拿病例和对照的基线差异判断混杂**：对照代表源人群，本来就和病例在很多方面不同[^vandenbroucke2007strobe-e40]。
- **样本量**：用为别的目的已收集好的数据时，关键看精度够不够，样本量的考虑可以是非正式的；不要做事后功效计算[^vandenbroucke2007strobe-e44]。统计的一般做法见通用篇的[认真对待随机性和统计](../../../general/2_during/02_evidence_and_validity.md#5-认真对待随机性和统计)。

### 第八步：敏感性分析

**怎么做**：换一种分析策略或假设，看主要结果变不变；可以换的包括纳入标准、暴露和结局的定义等[^vandenbroucke2007strobe-e37]。具体到本研究：

- **未测量的混杂**：问一问"要多强的混杂才能把结果解释掉"。经典例子是 1959 年 Cornfield 等人的分析：吸烟与肺癌的相对危险度（暴露组发病风险是非暴露组的几倍）是 9，能解释它的混杂因素在吸烟者中的流行程度至少要是非吸烟者的 9 倍[^vandenbroucke2007strobe-e38]。混杂因素未知时，就在关于偏倚大小的几种假设下重复分析[^hernan2020whatif-e11]。
- **"反过来"的对照分析**：例如再模拟一个"继续用药对停药"的试验。如果"开始用药"和"停药"都显示风险降低，至少有一个分析没有做到公平比较[^hernan2016target-e7]。
- **结果是"无关联"时也要做**：混杂或偏倚可能把结果拉向无关联[^vandenbroucke2007strobe-e39]。

### 第九步：报告

- **STROBE**：适用于队列、病例对照、横断面三种设计[^vonelm2007strobe-e2]，共 22 项[^vonelm2007strobe-e4]。它只管怎样报告，不规定怎样设计，也不是质量评价工具[^vonelm2007strobe-e3]。
- **用常规收集的数据**：在 STROBE 之外按它的扩展 RECORD（13 项）报告[^benchimol2015record-e3]。领域概况没讲的几条：链接了多个数据库时，可以用流程图展示每一步链接上的人数[^benchimol2015record-e16]；详细写出研究人群怎样一步步筛出来[^benchimol2015record-e19]；说明研究者能多大程度接触原始数据库，以及数据怎样清洗[^benchimol2015record-e17]。原因是，不熟悉建队列细节或研究目的的数据分析员来建队列，容易出错[^benchimol2015record-e18]。
- **饮食研究**：再加 STROBE 的营养流行病学扩展 STROBE-nut，它在 STROBE 上增加了 24 条建议[^lachat2016strobenut-e1]，例如写清饮食评估方法验证研究的参照方法、时间和人群[^lachat2016strobenut-e6]。
- **局限**：不只列出偏倚，还要讨论它们可能的方向和大小[^vandenbroucke2007strobe-e41]。真实的不确定性比置信区间反映的更大[^vandenbroucke2007strobe-e42]。调整后的结果仍可能有随机误差、选择偏倚、信息偏倚或残余混杂[^vandenbroucke2007strobe-e34]；"因果"措辞的争论见[领域概况](../README.md#动手前先说清你要回答关联问题还是因果问题)。

## 3. 检查清单

**必须做到**（本节依据 STROBE 及其解释文章、RECORD、STROBE-nut 和上文资料整理 `[本项目分析]`）

- [ ] 写清是关联问题还是因果问题[^hernan2018cword-e7]；因果问题写出目标试验的各部分，尤其是零时刻[^hernan2016target-e2][^hernan2016target-e5]
- [ ] 定义所有暴露、结局、混杂因素，适用时给出诊断标准[^vandenbroucke2007strobe-e23]
- [ ] 病例对照研究说明对照从哪来、为什么能反映产生病例的人群[^vandenbroucke2007strobe-e18]
- [ ] 按因果知识或明确的假设决定调整哪些变量，不只凭统计标准[^vandenbroucke2007strobe-e31][^hernan2020whatif-e6]
- [ ] 同时报告未调整和调整后的估计[^vandenbroucke2007strobe-e34]
- [ ] 事先定好怎样处理失访和缺失数据，并如实报告[^vandenbroucke2007strobe-e36][^vandenbroucke2007strobe-e35]
- [ ] 讨论偏倚的方向和大小[^vandenbroucke2007strobe-e41]
- [ ] 按 STROBE 报告[^vonelm2007strobe-e2]；用现成数据加 RECORD[^benchimol2015record-e3]，饮食研究加 STROBE-nut[^lachat2016strobenut-e1]

**做到更好**

- [ ] 画出因果图并放进论文，写明调整集[^tennant2021dags-e2][^tennant2021dags-e5]
- [ ] 做敏感性分析：换暴露和结局定义[^vandenbroucke2007strobe-e37]、评估未测量混杂[^hernan2020whatif-e11]、换缺失数据处理方法[^vandenbroucke2007strobe-e35]
- [ ] 用"反过来"的分析间接检查混杂[^hernan2016target-e7]
- [ ] 写清暴露测量方法的验证研究，包括参照方法、时间和人群[^lachat2016strobenut-e6]；更多见领域概况的[坑二](../README.md#坑二暴露测不准尤其是饮食)
- [ ] 说明你模拟的目标试验和理想试验的差别[^hernan2016target-e10]

**这些情况可以不做，不算缺陷**

- 纯粹描述关联的研究，不调整混杂[^hernan2018cword-e7]。
- 病例对照研究不做匹配：方法学者本来就不建议例行匹配[^vandenbroucke2007strobe-e20]。
- 用为别的目的已收集好的数据时，不做正式的样本量计算，只讨论精度够不够[^vandenbroucke2007strobe-e44]。

**审稿时常见、但不成立的批评**

- **"你的结果可能有混杂。"** What If 一书说，这样泛泛的批评"不是科学陈述，而是逻辑陈述"；批评者指出了具体因素（如吸烟），研究者的下一步才是调整它，拿不到数据就做敏感性分析[^hernan2020whatif-e10]。
- **"相对危险度不到 2 或 3，不值得相信。"** STROBE 解释文章提到，有人主张忽略相对危险度低于 2 或 3 的结果；但它指出，低于 3 不一定就是假的[^vandenbroucke2007strobe-e43]。
- **"病例和对照基线差别很大，可比性差。"** 病例对照研究里，对照代表源人群，通常在很多方面都和病例不同，不能这样判断混杂[^vandenbroucke2007strobe-e40]。

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 随访起点晚于开始用药的时刻 | 中间发生的结局被漏掉，产生选择偏倚[^hernan2016target-e5] |
| 纳入标准写"随访期间用过药的人" | 按基线之后的事件选人，会带来偏倚[^hernan2016target-e3] |
| 对照选自与暴露有关的疾病人群 | 例如从髋部骨折者中选对照研究雌激素，对照入选取决于暴露的后果[^hernan2020whatif-e14] |
| 按因果通路上的中间变量匹配或调整 | 匹配会造成分析时补救不了的偏倚[^vandenbroucke2007strobe-e21]；调整也会引入偏倚[^vandenbroucke2007strobe-e31] |
| 匹配了却不做匹配分析 | 匹配因素和暴露有关时，比值比通常偏向 1[^vandenbroucke2007strobe-e22] |
| 只凭显著性检验等统计标准挑混杂因素 | 统计标准不足以判断混杂[^hernan2020whatif-e6] |
| 为让 P 值最小挑暴露的分组切点 | 夸大关联[^vandenbroucke2007strobe-e24] |
| 认为饮食测量误差只会让结果偏保守 | 有系统误差或多个测不准的饮食变量时，也可能夸大关联[^nci2025dietprimer-e4][^nci2025dietprimer-e5] |
| 直接删掉"误报者"不做比较 | 可能带来选择偏倚[^lachat2016strobenut-e4] |
| 只写"前瞻性队列研究" | 这个词定义不清，要写清数据怎样、何时收集[^vandenbroucke2007strobe-e17] |
| 把只有一组人的随访叫队列研究 | 没有对照组的是病例系列[^song2010observational-e4] |

## 5. 延伸阅读

- **STROBE 解释文章（Vandenbroucke 等人 2007）**：本文大部分做法的出处。设计时就逐条读，尤其是 Box 2（匹配）、Box 3（偏倚）、Box 5（混杂）、Box 6（缺失数据）和第 12 项（统计方法）。
- **Hernán & Robins，Causal Inference: What If**：作者网站上可免费下载的因果推断教材。本文用到的是第 3.6 节（目标试验）和第 7、8、9 章（混杂、选择偏倚、测量偏倚）的部分内容。
- **Hernán & Robins 2016，Using Big Data to Emulate a Target Trial**：用现成数据做因果分析前读，讲零时刻、纳入标准、结局判定的具体陷阱。
- **Tennant 等人 2021**：对健康研究中因果图用法的综述，后半部分的建议（Recommendations）适合在画图时对照。
- **Song & Chung 2010**：面向外科医生的入门文章，用外科的例子讲队列和病例对照研究的优缺点和选人方法。
- **美国国家癌症研究所的饮食评估入门资料（Dietary Assessment Primer）和 STROBE-nut（Lachat 等人 2016）**：做饮食研究时读，前者讲测量误差，后者讲怎样报告。
- 本文资料没有讲具体的统计方法（如逆概率加权、倾向评分）怎样实施，以导师、统计学合作者或上述教材为准。

[^song2010observational-e1]: Song & Chung 2010，引言。[证据](../../../../sources/notes/song2010observational.md#e1)
[^song2010observational-e2]: Song & Chung 2010，Cohort Studies。[证据](../../../../sources/notes/song2010observational.md#e2)
[^song2010observational-e3]: Song & Chung 2010，Case-Control Studies 与 Table 4。[证据](../../../../sources/notes/song2010observational.md#e3)
[^song2010observational-e4]: Song & Chung 2010，Cohort Studies（与病例系列的区别）。[证据](../../../../sources/notes/song2010observational.md#e4)
[^song2010observational-e5]: Song & Chung 2010，Selection of Subjects in Cohort Studies。[证据](../../../../sources/notes/song2010observational.md#e5)
[^song2010observational-e6]: Song & Chung 2010，Attrition Bias。[证据](../../../../sources/notes/song2010observational.md#e6)
[^song2010observational-e7]: Song & Chung 2010，Selection of Cases。[证据](../../../../sources/notes/song2010observational.md#e7)
[^song2010observational-e8]: Song & Chung 2010，Selection of Controls。[证据](../../../../sources/notes/song2010observational.md#e8)
[^song2010observational-e9]: Song & Chung 2010，Bias in Case-Control Studies。[证据](../../../../sources/notes/song2010observational.md#e9)
[^song2010observational-e10]: Song & Chung 2010，Cohort Studies（回顾性队列）。[证据](../../../../sources/notes/song2010observational.md#e10)
[^vandenbroucke2007strobe-e14]: Vandenbroucke 等人 2007，Box 1。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e14)
[^vandenbroucke2007strobe-e15]: Vandenbroucke 等人 2007，Box 1。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e15)
[^vandenbroucke2007strobe-e16]: Vandenbroucke 等人 2007，Box 1。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e16)
[^vandenbroucke2007strobe-e17]: Vandenbroucke 等人 2007，Item 4。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e17)
[^vandenbroucke2007strobe-e18]: Vandenbroucke 等人 2007，Item 6。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e18)
[^vandenbroucke2007strobe-e19]: Vandenbroucke 等人 2007，Item 6。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e19)
[^vandenbroucke2007strobe-e20]: Vandenbroucke 等人 2007，Box 2。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e20)
[^vandenbroucke2007strobe-e21]: Vandenbroucke 等人 2007，Box 2。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e21)
[^vandenbroucke2007strobe-e22]: Vandenbroucke 等人 2007，Box 2。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e22)
[^vandenbroucke2007strobe-e23]: STROBE 清单，Item 7。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e23)
[^vandenbroucke2007strobe-e24]: Vandenbroucke 等人 2007，Box 4。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e24)
[^vandenbroucke2007strobe-e25]: Vandenbroucke 等人 2007，Item 8。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e25)
[^vandenbroucke2007strobe-e26]: Vandenbroucke 等人 2007，Box 3。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e26)
[^vandenbroucke2007strobe-e27]: Vandenbroucke 等人 2007，Box 3。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e27)
[^vandenbroucke2007strobe-e28]: Vandenbroucke 等人 2007，Box 3。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e28)
[^vandenbroucke2007strobe-e29]: Vandenbroucke 等人 2007，Box 5。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e29)
[^vandenbroucke2007strobe-e30]: Vandenbroucke 等人 2007，Box 5。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e30)
[^vandenbroucke2007strobe-e31]: Vandenbroucke 等人 2007，Item 16。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e31)
[^vandenbroucke2007strobe-e32]: Vandenbroucke 等人 2007，Item 16。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e32)
[^vandenbroucke2007strobe-e33]: Vandenbroucke 等人 2007，Item 12。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e33)
[^vandenbroucke2007strobe-e34]: Vandenbroucke 等人 2007，Item 16。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e34)
[^vandenbroucke2007strobe-e35]: Vandenbroucke 等人 2007，Box 6。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e35)
[^vandenbroucke2007strobe-e36]: Vandenbroucke 等人 2007，Item 12(d)。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e36)
[^vandenbroucke2007strobe-e37]: Vandenbroucke 等人 2007，Item 12(e)。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e37)
[^vandenbroucke2007strobe-e38]: Vandenbroucke 等人 2007，Item 12(e)。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e38)
[^vandenbroucke2007strobe-e39]: Vandenbroucke 等人 2007，Item 12(e)。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e39)
[^vandenbroucke2007strobe-e40]: Vandenbroucke 等人 2007，Item 14。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e40)
[^vandenbroucke2007strobe-e41]: Vandenbroucke 等人 2007，Item 19。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e41)
[^vandenbroucke2007strobe-e42]: Vandenbroucke 等人 2007，Item 20。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e42)
[^vandenbroucke2007strobe-e43]: Vandenbroucke 等人 2007，Item 20。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e43)
[^vandenbroucke2007strobe-e44]: Vandenbroucke 等人 2007，Item 10。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e44)
[^vandenbroucke2007strobe-e45]: Vandenbroucke 等人 2007，Item 8，Example 2。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e45)
[^vandenbroucke2007strobe-e46]: Vandenbroucke 等人 2007，Box 6。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e46)
[^vandenbroucke2007strobe-e47]: Vandenbroucke 等人 2007，Item 20。[证据](../../../../sources/notes/vandenbroucke2007strobe.md#e47)
[^vonelm2007strobe-e2]: von Elm 等人 2007，Aims and Use of the STROBE Statement。[证据](../../../../sources/notes/vonelm2007strobe.md#e2)
[^vonelm2007strobe-e3]: von Elm 等人 2007，Aims and Use of the STROBE Statement。[证据](../../../../sources/notes/vonelm2007strobe.md#e3)
[^vonelm2007strobe-e4]: von Elm 等人 2007，STROBE Components。[证据](../../../../sources/notes/vonelm2007strobe.md#e4)
[^benchimol2015record-e3]: Benchimol 等人 2015，摘要与引言。[证据](../../../../sources/notes/benchimol2015record.md#e3)
[^benchimol2015record-e16]: Benchimol 等人 2015，RECORD 6.3。[证据](../../../../sources/notes/benchimol2015record.md#e16)
[^benchimol2015record-e17]: Benchimol 等人 2015，RECORD 12.1、12.2。[证据](../../../../sources/notes/benchimol2015record.md#e17)
[^benchimol2015record-e18]: Benchimol 等人 2015，RECORD 12.1、12.2 解释。[证据](../../../../sources/notes/benchimol2015record.md#e18)
[^benchimol2015record-e19]: Benchimol 等人 2015，RECORD 13.1。[证据](../../../../sources/notes/benchimol2015record.md#e19)
[^hernan2018cword-e7]: Hernán 2018，Better Confounding Adjustment。[证据](../../../../sources/notes/hernan2018cword.md#e7)
[^hernan2016target-e1]: Hernán & Robins 2016，摘要。[证据](../../../../sources/notes/hernan2016target.md#e1)
[^hernan2016target-e2]: Hernán & Robins 2016，引言（Table 1）。[证据](../../../../sources/notes/hernan2016target.md#e2)
[^hernan2016target-e3]: Hernán & Robins 2016，Eligibility criteria。[证据](../../../../sources/notes/hernan2016target.md#e3)
[^hernan2016target-e4]: Hernán & Robins 2016，Emulating the Target Trial。[证据](../../../../sources/notes/hernan2016target.md#e4)
[^hernan2016target-e5]: Hernán & Robins 2016，Defining Time Zero。[证据](../../../../sources/notes/hernan2016target.md#e5)
[^hernan2016target-e6]: Hernán & Robins 2016，Defining Time Zero。[证据](../../../../sources/notes/hernan2016target.md#e6)
[^hernan2016target-e7]: Hernán & Robins 2016，Assignment procedures。[证据](../../../../sources/notes/hernan2016target.md#e7)
[^hernan2016target-e8]: Hernán & Robins 2016，Outcome。[证据](../../../../sources/notes/hernan2016target.md#e8)
[^hernan2016target-e9]: Hernán & Robins 2016，Assignment procedures。[证据](../../../../sources/notes/hernan2016target.md#e9)
[^hernan2016target-e10]: Hernán & Robins 2016，Discussion。[证据](../../../../sources/notes/hernan2016target.md#e10)
[^hernan2016target-e11]: Hernán & Robins 2016，Discussion。[证据](../../../../sources/notes/hernan2016target.md#e11)
[^hernan2016target-e12]: Hernán & Robins 2016，Outcome。[证据](../../../../sources/notes/hernan2016target.md#e12)
[^hernan2020whatif-e1]: Hernán & Robins，What If，第 3.6 节。[证据](../../../../sources/notes/hernan2020whatif.md#e1)
[^hernan2020whatif-e2]: Hernán & Robins，What If，第 3.6 节。[证据](../../../../sources/notes/hernan2020whatif.md#e2)
[^hernan2020whatif-e3]: Hernán & Robins，What If，第 3.6 节。[证据](../../../../sources/notes/hernan2020whatif.md#e3)
[^hernan2020whatif-e4]: Hernán & Robins，What If，第 7.1 节。[证据](../../../../sources/notes/hernan2020whatif.md#e4)
[^hernan2020whatif-e5]: Hernán & Robins，What If，第 7.1 节。[证据](../../../../sources/notes/hernan2020whatif.md#e5)
[^hernan2020whatif-e6]: Hernán & Robins，What If，第 7.4 节。[证据](../../../../sources/notes/hernan2020whatif.md#e6)
[^hernan2020whatif-e7]: Hernán & Robins，What If，第 7.4 节。[证据](../../../../sources/notes/hernan2020whatif.md#e7)
[^hernan2020whatif-e8]: Hernán & Robins，What If，第 7.6 节。[证据](../../../../sources/notes/hernan2020whatif.md#e8)
[^hernan2020whatif-e9]: Hernán & Robins，What If，第 7.6 节。[证据](../../../../sources/notes/hernan2020whatif.md#e9)
[^hernan2020whatif-e10]: Hernán & Robins，What If，第 7.6 节。[证据](../../../../sources/notes/hernan2020whatif.md#e10)
[^hernan2020whatif-e11]: Hernán & Robins，What If，第 7.3 节。[证据](../../../../sources/notes/hernan2020whatif.md#e11)
[^hernan2020whatif-e12]: Hernán & Robins，What If，第 8 章开头。[证据](../../../../sources/notes/hernan2020whatif.md#e12)
[^hernan2020whatif-e13]: Hernán & Robins，What If，第 8.2 节。[证据](../../../../sources/notes/hernan2020whatif.md#e13)
[^hernan2020whatif-e14]: Hernán & Robins，What If，第 8 章 Fine Point（病例对照研究中的选择偏倚）。[证据](../../../../sources/notes/hernan2020whatif.md#e14)
[^hernan2020whatif-e15]: Hernán & Robins，What If，第 8.3 节。[证据](../../../../sources/notes/hernan2020whatif.md#e15)
[^hernan2020whatif-e16]: Hernán & Robins，What If，第 9 章开头。[证据](../../../../sources/notes/hernan2020whatif.md#e16)
[^hernan2020whatif-e17]: Hernán & Robins，What If，第 9.2 节。[证据](../../../../sources/notes/hernan2020whatif.md#e17)
[^hernan2020whatif-e18]: Hernán & Robins，What If，第 9.2 节。[证据](../../../../sources/notes/hernan2020whatif.md#e18)
[^hernan2020whatif-e19]: Hernán & Robins，What If，第 8.2 节。[证据](../../../../sources/notes/hernan2020whatif.md#e19)
[^nci2025dietprimer-e1]: 美国国家癌症研究所，Dietary Assessment Primer，Key Concepts about Measurement Error。[证据](../../../../sources/notes/nci2025dietprimer.md#e1)
[^nci2025dietprimer-e2]: 同上。[证据](../../../../sources/notes/nci2025dietprimer.md#e2)
[^nci2025dietprimer-e3]: 美国国家癌症研究所，Dietary Assessment Primer，Effects of Measurement Error。[证据](../../../../sources/notes/nci2025dietprimer.md#e3)
[^nci2025dietprimer-e4]: 同上。[证据](../../../../sources/notes/nci2025dietprimer.md#e4)
[^nci2025dietprimer-e5]: 同上。[证据](../../../../sources/notes/nci2025dietprimer.md#e5)
[^nci2025dietprimer-e6]: 美国国家癌症研究所，Dietary Assessment Primer，Learn More about Misreporting。[证据](../../../../sources/notes/nci2025dietprimer.md#e6)
[^nci2025dietprimer-e7]: 同上。[证据](../../../../sources/notes/nci2025dietprimer.md#e7)
[^nci2025dietprimer-e8]: 同上。[证据](../../../../sources/notes/nci2025dietprimer.md#e8)
[^nci2025dietprimer-e9]: 美国国家癌症研究所，Dietary Assessment Primer，Effects of Measurement Error，Table 1。[证据](../../../../sources/notes/nci2025dietprimer.md#e9)
[^lachat2016strobenut-e1]: Lachat 等人 2016，摘要。[证据](../../../../sources/notes/lachat2016strobenut.md#e1)
[^lachat2016strobenut-e2]: Lachat 等人 2016，引言。[证据](../../../../sources/notes/lachat2016strobenut.md#e2)
[^lachat2016strobenut-e3]: Lachat 等人 2016，引言。[证据](../../../../sources/notes/lachat2016strobenut.md#e3)
[^lachat2016strobenut-e4]: Lachat 等人 2016，nut-9。[证据](../../../../sources/notes/lachat2016strobenut.md#e4)
[^lachat2016strobenut-e5]: Lachat 等人 2016，nut-12.2。[证据](../../../../sources/notes/lachat2016strobenut.md#e5)
[^lachat2016strobenut-e6]: Lachat 等人 2016，nut-8.6。[证据](../../../../sources/notes/lachat2016strobenut.md#e6)
[^tennant2021dags-e1]: Tennant 等人 2021，摘要。[证据](../../../../sources/notes/tennant2021dags.md#e1)
[^tennant2021dags-e2]: Tennant 等人 2021，Recommendations。[证据](../../../../sources/notes/tennant2021dags.md#e2)
[^tennant2021dags-e3]: Tennant 等人 2021，Recommendations。[证据](../../../../sources/notes/tennant2021dags.md#e3)
[^tennant2021dags-e4]: Tennant 等人 2021，Recommendations。[证据](../../../../sources/notes/tennant2021dags.md#e4)
[^tennant2021dags-e5]: Tennant 等人 2021，Recommendations。[证据](../../../../sources/notes/tennant2021dags.md#e5)
[^tennant2021dags-e6]: Tennant 等人 2021，Recommendations。[证据](../../../../sources/notes/tennant2021dags.md#e6)
[^tennant2021dags-e7]: Tennant 等人 2021，Recommendations。[证据](../../../../sources/notes/tennant2021dags.md#e7)
