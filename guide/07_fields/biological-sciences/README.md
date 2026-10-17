# 生物科学：学科概况

本文讲生物科学（以实验室里的生命科学为主）的研究实际怎样运转：实验室怎样组织、实验为什么慢、记录本怎么记、重复和对照怎么做、动物研究有哪些规矩、论文怎样发表和署名、数据交到哪里。野外生态学、进化生物学等方向有自己的做法，本文只在个别地方提到。各学科共通的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)，这里不重复。生物科学常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。

**读完本文，你应该能：**

- 说清一个生命科学实验室怎样分工，一篇论文怎样从实验台走到期刊；
- 分清"独立重复"和"重复测量"，知道你的 n 到底是几；
- 知道试剂、抗体、细胞系为什么要验证，动物实验要遵守哪些原则和报告规范；
- 避开新手在记录、重复、对照、数据提交上最常犯的错误。

---

## 本领域研究怎样运转

### 实验室围着课题组负责人转

实验室方向的研究以课题组为单位：课题组负责人（Principal Investigator，PI）定方向、找经费，学生和博士后在实验台上做实验。这种分工也体现在署名上：在生物医学领域，按非正式惯例，最后一位作者被看作研究在思路和经费上的推动者[^tscharntke2007author-e2]。

对新手来说，这意味着：你用的试剂、细胞、动物、仪器多半是组里共用的，记录和交接要按组里的规矩来；你的课题常常是 PI 大方向下的一块。机构没有记录本政策时，课题组也应该有自己的规定[^schnell2015ten-e2]。怎样和导师对齐期望、汇报进展，见贯穿全程的[合作与导师](../../08_throughout/collaboration_and_advisors.md)。

### 湿实验慢，而且常出意外

**湿实验**指在实验台上用细胞、组织、动物和试剂做的实验；只用计算机做的研究叫**干实验**。湿实验的节奏和计算研究很不一样：

- **周期长。** 举一个极端的例子：癌症生物学可复现性项目（一个专门重做已发表癌症生物学实验的大项目）报告，从开始做实验到交付最终数据，间隔是 90 周[^errington2021challenges-e4]。这是一个大型复现项目的数字，不代表一般课题的速度，但能说明湿实验可能非常耗时。
- **方案常常要改。** 同一个项目里，67% 已经通过同行评审的实验方案，开工后还需要修改才能做完；而这些修改里只有 41% 真正做得成[^errington2021challenges-e2]。有时只是小改，比如在蛋白质印迹（Western blot，一种检测特定蛋白的方法）里调整抗体浓度或封闭试剂[^errington2021challenges-e3]。
- **论文里的方法可能不够用。** 这个项目计划复现的 193 个实验，没有一个能只靠原论文就设计出复现方案，都要去问原作者[^errington2021challenges-e1]。

所以，做湿实验的计划要留出余量，先用小规模的预实验把方法跑通。怎样做计划、怎样先做最可能失败的部分，见第二部分的[形成研究计划](../../02_do-the-project/03_research-plan.md)和[执行与迭代](../../02_do-the-project/06_run-and-iterate.md)。

### 实验记录本是第一手记录

实验记录本（lab notebook）是科研活动的主要记录，也是想法和结果归谁所有的法律凭证[^schnell2015ten-e1]。下面几条来自一篇写给计算生物学家的文章[^schnell2015ten-e8]，但它讲的是记录本的通行规矩，我们认为湿实验同样适用。研究日志的一般写法见第二部分的[执行与迭代](../../02_do-the-project/06_run-and-iterate.md#3-每次运行都留下记录)和[整理科研材料](../../08_throughout/organizing_materials.md#5-分清三种笔记)。

- **当场记。** 每条记录在做完后立即写[^schnell2015ten-e3]。靠记忆，很可能到时候就想不起来了[^schnell2015ten-e9]。
- **写错了划掉，不要擦。** 纸质记录本写错了，用一条细线划掉，在旁边写正确内容；永远不要擦掉或销毁记录[^schnell2015ten-e4]。
- **写清谁做了什么，当作证据来记。** 每条记录都写明谁做了哪部分工作、讨论时谁在场[^schnell2015ten-e5]。发生科研不端调查时，机构或政府资助机构可以调取记录本作为证据[^schnell2015ten-e6]。
- **保存每张图的原始数据**[^schnell2015ten-e7]。

### 发表：期刊和预印本

在生命科学，正式发表指在期刊上发表。这和计算机领域以会议为主不同，见[计算机篇](../computer-science/README.md#会议是主要的发表渠道)。**预印本**是没经过同行评审、先公开的论文稿。生命科学有专门的预印本平台 bioRxiv，它免费存档和发布尚未正式发表的论文[^biorxivabout-e1]。几点要知道：

- 文章上线前**不经过同行评审**[^biorxivabout-e2]，读别人的预印本时要自己判断质量。
- 可以在投期刊之前或同时发；已被期刊接收的文章不应再发[^biorxivabout-e3]。**发了就撤不下来**，因为它已经可以被引用[^biorxivabout-e4]。
- bioRxiv 说大多数期刊允许发表前先发预印本，但发之前要查清目标期刊的政策[^biorxivabout-e5]。好处是成果马上能被同行看到，投稿前还能收到反馈[^biorxivabout-e6]。

### 署名：第一作者和最后作者最受关注

- **第一作者**：传统上贡献最大，得到的认可也最多[^tscharntke2007author-e1]。
- **最后作者**：在生物医学，按非正式惯例，常和第一作者得到同样多的认可[^tscharntke2007author-e2]。评审委员会和资助机构常把它看作领导课题组的标志，但这只是非正式惯例，并不总被遵守[^tscharntke2007author-e3]。
- **中间作者**：怎样排序，各国、各领域传统差别很大[^tscharntke2007author-e4]。有作者建议在致谢里写明本文用的是哪种排序方式[^tscharntke2007author-e5]。
- **通讯作者**：按 ICMJE 的定义，是投稿、审稿、发表过程中主要负责和期刊沟通的那个人[^icmje2026recommendations-e28]。

谁能署名，没有一套全生命科学统一的规定，以目标期刊的作者须知为准。常被提到的国际医学期刊编辑委员会（ICMJE）署名规范是为医学期刊定的，它的署名条件和"开工时就谈"的做法，见贯穿全程的[合作与导师：署名](../../08_throughout/collaboration_and_advisors.md#6-署名开工时就谈并随进展调整)。

---

## 和其他领域不同的地方

下表和计算机领域对照。计算机一栏的依据见[计算机篇](../computer-science/README.md)；生物一栏按本文资料整理。

| | 生物科学（实验室方向） | 计算机 |
|---|---|---|
| 正式发表 | 期刊；bioRxiv 预印本在投稿前或投稿时发[^biorxivabout-e3] | 多数方向以会议为主 |
| 实验周期 | 可能很长：一个大型复现项目从开始实验到交付数据用了 90 周[^errington2021challenges-e4] | 很多实验可以在计算机上很快重跑 |
| n 怎么算 | 按独立的实验单位（动物、一笼、一窝等）算，不按测了多少次算[^perciedusert2020reporting-e4][^perciedusert2020reporting-e6] | 常按随机种子、数据集等算 |
| 材料 | 试剂、抗体、细胞系本身可能有问题，要验证[^nihrigorguidance-e4] | 代码和数据可以完整复制 |
| 伦理审批 | 动物实验一般要经过"伤害—收益"审批[^perciedusert2020arrive-e6] | 涉及人或安全问题时才审批 |
| 数据 | 期刊可能要求把序列等数据交到专门的公共数据库，PLOS 就是这样[^plosdatapolicy-e2] | 常靠制品评估和代码仓库 |

---

## 本领域的规范和报告标准

### 先弄清实验单位，再算 n

n 算错了，后面的统计就靠不住，还可能得出假阳性[^perciedusert2020reporting-e5]。**实验单位**是独立接受处理的那个对象：任意两个实验单位都可以被分到不同的处理组[^perciedusert2020reporting-e3]。它常常是一只动物，但也可能是一笼、一窝动物，或动物身体的一部分[^perciedusert2020reporting-e6]。区分两种"重复"（下面的叫法是实验室常用说法）：

- **生物学重复（独立重复）**：用不同的动物、不同的独立培养物，各做一遍。它才能检验你的假设。要把结论推广到一类小鼠，必须用多只小鼠做多次独立比较[^vaux2012replicates-e2]。
- **技术重复（重复测量）**：同一份样品测几次，或从同一份细胞悬液里分出几个平板。它不是对假设的独立检验，不能拿来算置信区间或 P 值[^vaux2012replicates-e1]，只能对那一份样品下结论[^vaux2012replicates-e5]。一句话：结论只能推广到你抽取独立样本的那个总体[^vaux2012replicates-e3]。

技术重复也有用：它检查实验本身做得好不好。比如某个平板的结果明显异常，你会去查是不是贴错了标签、是不是长了污染的酵母[^vaux2012replicates-e4]。但不能拿它算 n：实验单位是小鼠时，从一只小鼠测 50 个细胞，n 还是 1[^perciedusert2020reporting-e4]。把它报告成 n = 50 叫**伪重复**，会低估真实变异，导致假阳性[^perciedusert2020reporting-e5]。

实验里的因素常常是一层套一层的：细胞在动物里，动物在笼子里[^perciedusert2020reporting-e10]。设计实验前，先画出这几层，标出哪一层是实验单位。统计的一般做法见第二部分的[报告差多少、有多确定，而不只是 p 值](../../02_do-the-project/07_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

### 对照、随机分组和盲法

- **设对照组，没设要说明理由**[^perciedusert2020reporting-e1]。**阴性对照**用来判断差异是不是处理造成的，例如野生型对基因改造动物、假手术对真手术；**阳性对照**用来确认实验能测出预期的效应，帮你解释阴性结果[^perciedusert2020reporting-e2]。
- **一次只改一个因素。** 两组之间只有你关心的那个因素不同，才能把差异归到它身上[^vaux2012replicates-e6]。
- **真正随机分组。** 从笼子里"随手"抓一只不算随机，因为里面有人的判断[^perciedusert2020reporting-e7]。
- **能盲就盲。** 研究者常常预期某个结果，可能无意中影响实验或解读数据。**盲法**就是让分组、做实验、评估结果、分析数据的人尽量不知道每个对象属于哪一组，以减少这种偏倚；论文里要写清各个阶段谁知道分组[^perciedusert2020reporting-e8]。
- **不挑着报告。** 因为数据和论文的说法冲突就去掉某些组，是误导[^perciedusert2020reporting-e9]。独立样本的结果，只有在特殊情况下才能剔除[^vaux2012replicates-e8]。
- **结论别说过头。** 只看到部分效应，就不要说某个基因"必需"[^vaux2012replicates-e7]。

### 试剂、抗体和细胞系要验证

在计算研究里，代码复制一份就一模一样。湿实验不行：试剂本身可能出问题。

- 试剂和生物材料不稳定、验证不足，是研究难以复现的原因之一[^perciedusert2020arrive-e4]。Freedman 等人认为，临床前研究（进入人体试验之前的研究，如细胞和动物实验）不可复现的主要原因可以分成四类，其中一类就是生物试剂和参考材料[^freedman2015economics-e1]。
- **细胞系可能根本不是你以为的那个。** Freedman 等人 2015 年的文章提到，生物医学研究里细胞系鉴定错误和交叉污染的情况，估计在 15% 到 36% 之间[^freedman2015economics-e2]。这是一个估计范围，不是精确测量。文章还说，短串联重复序列（STR）分析是公认的细胞系身份鉴定方法，每次约 200 美元；但通常只有三分之一的实验室会检测细胞系的身份[^freedman2015economics-e3]。
- **有的资助机构也在要求。** 例如美国国立卫生研究院（National Institutes of Health，NIH）的资助申请和评审，把"关键生物和化学资源的鉴定"列为四个重点之一[^nihrigorguidance-e2]；这些资源包括细胞系、抗体等，它们的质量直接决定结果能否复现[^nihrigorguidance-e4]。
- **别人的材料不一定拿得到。** 前面那个复现项目计划的 193 个实验里，有 136 个（70%）要向原作者索要关键试剂，比如细胞系、质粒、模式生物、抗体；这些试剂既买不到，也不在公共资源库里[^errington2021challenges-e5]。
- **把验证当成规范做法。** Freedman 等人建议，课题组负责人把使用经过验证的试剂当作有记录的规范做法[^freedman2015economics-e5]。实际做法：在记录本里写下每种试剂的来源、货号和批号；新到的细胞系先鉴定；新抗体先用阳性、阴性对照确认它认的是对的蛋白。

### 动物研究：3R 原则和 ARRIVE 报告规范

**3R 原则**提出于 50 多年前，是让动物研究更人道的框架，已经写进很多国家和国际的法规[^nc3rsthe3rs-e1]：

| 原则 | 意思 |
|---|---|
| 替代（Replacement） | 能不用动物就不用[^nc3rsthe3rs-e2]。例如用人体组织和细胞、计算机模型、细胞系[^nc3rsthe3rs-e4] |
| 减少（Reduction） | 在满足科学目的的前提下少用动物[^nc3rsthe3rs-e2]；实验设计和分析得当，结果可靠[^nc3rsthe3rs-e3] |
| 优化（Refinement） | 尽量减轻动物的疼痛、痛苦和持久伤害[^nc3rsthe3rs-e2] |

动物实验的审批一般基于"伤害—收益分析"：动物受到的伤害，要和研究对社会的收益相权衡[^perciedusert2020arrive-e6]。研究即使做得严谨，报告不清楚，收益也可能落空[^perciedusert2020arrive-e6]。所以报告要写全：**ARRIVE**（Animal Research: Reporting of In Vivo Experiments，动物研究：活体实验报告指南）是一份清单，列出动物实验论文应写的信息，让别人能审查、评估和重复你的工作[^perciedusert2020arrive-e1]。它适用于所有用活体动物的研究[^perciedusert2020arrive-e8]。2.0 版分两组[^perciedusert2020arrive-e2]：

- **核心 10 项**（最低要求）：研究设计、样本量、减少主观偏倚的措施、结局指标、统计方法、动物信息、实验步骤和结果[^perciedusert2020arrive-e3]。
- **推荐项**：伦理声明、利益声明、研究方案注册、数据获取方式，以及饲养和照料等细节[^perciedusert2020arrive-e9]。

报告不全有数据为证：ARRIVE 作者引用的既往研究显示，动物研究论文中只有 30%～40% 报告了随机分组，约 20% 报告了盲法，不到 10% 说明了样本量的依据[^perciedusert2020arrive-e5]。ARRIVE 也可以在**设计实验时**就拿来用[^perciedusert2020arrive-e7]。

另一个容易忽略的点：性别、年龄、体重、基础健康状况等生物学变量，常常影响健康和疾病[^nihrigorguidance-e5]。以 NIH 为例，它要求所资助的脊椎动物和人体研究，在设计、分析和报告中考虑性别这个变量[^nihrigorguidance-e3]。其他资助机构的要求，以它们自己的规定为准。

### 数据交到公共数据库

有些类型的数据有本领域专门的公共数据库。下面以 PLOS 系列期刊的数据政策为例，这是一家出版商的规定：

- 发表时，要公开重复研究结果所需的全部数据[^plosdatapolicy-e1]。
- 有本领域的数据提交标准，就必须遵守；例如基因序列交 GenBank、EMBL 或 DDBJ，基因芯片数据交 ArrayExpress 或 GEO[^plosdatapolicy-e2]。
- 论文的数据可用性声明里要写数据库名称和**登录号**（accession number，数据库给每条数据的唯一编号）[^plosdatapolicy-e3]。
- 不允许写"数据未展示"[^plosdatapolicy-e4]。
- 蛋白质印迹和凝胶结果，要提供未裁剪的原始图像[^plosdatapolicy-e5]；图背后的数值也要交[^plosdatapolicy-e6]。
- 不同期刊要求不同，以目标期刊的政策为准。原始数据怎样保存，见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md#2-原始数据只读其余都能重新生成)。

### 可复现性：领域正在面对的问题

- 癌症生物学可复现性项目最终重做了 23 篇论文中的 50 个实验，共涉及 158 个效应[^errington2021investigating-e1]。只看原论文报告的阳性效应，复现实验的效应量中位数，比原实验的效应量中位数小 85%[^errington2021investigating-e2]。
- 复现失败不等于原结果错了，只说明还需要更多研究来确认；同样，复现成功也不能确证原结果[^errington2021investigating-e3]。
- 原论文的数据也难拿到：计划复现的 193 个实验里，只有 4 个公开了计算效应量和做统计功效分析所需的数据；联系原作者后，仍有 68% 的实验拿不到这些数据[^errington2021challenges-e6]。
- Freedman 等人综合既往研究，估计不可复现的临床前研究累计超过 50%。但这个数是推算出来的，区间很宽：假设各类问题大量重叠时低到 18%，假设几乎不重叠时高到 88.5%[^freedman2015economics-e4]。所以它只能当作粗略估计，不能说成"一半以上的研究是错的"。
- 有的资助机构把严谨性写进了申请和评审标准。例如 NIH 把科学严谨性定义为在实验设计、方法、分析、解释和报告各个环节严格运用科学方法，做到稳健、无偏[^nihrigorguidance-e1]。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，按核心主张来定，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表只列本文资料能支持的；分组和"在生物科学里的样子"一栏是本手册的归纳。

| 套路 | 在生物科学里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [解释因果](../../05_research-strategies/explain_causality.md) | 细胞和分子实验：改变一个因素（例如敲低一个基因），看结果会不会变 | 一次只改一个因素[^vaux2012replicates-e6]；设对照组，不设要说明理由[^perciedusert2020reporting-e1]；n 按独立的实验单位算，不按测量次数算[^perciedusert2020reporting-e4]；技术重复不能拿来算 P 值[^vaux2012replicates-e1] | [实验台实验](../../06_methods/bench_experiment.md) |
| [解释因果](../../05_research-strategies/explain_causality.md) | 动物实验：在活体动物上做处理和测量 | 一般要经过"伤害—收益"审批[^perciedusert2020arrive-e6]，按 3R 原则设计[^nc3rsthe3rs-e2]；真正随机分组[^perciedusert2020reporting-e7]，写清各阶段谁知道分组[^perciedusert2020reporting-e8]；按 ARRIVE 核心 10 项报告[^perciedusert2020arrive-e3] | [临床前动物研究](../../06_methods/preclinical_animal_study.md) |
| [观察描述](../../05_research-strategies/observe_describe.md) | 组学的描述性研究：用基因芯片或高通量测序产生大批数据，描述样品处在什么状态 | 交出足够的信息，让别人能无歧义地解读结果、有可能重复实验[^fgedmiame-e1][^fgedminseqe-e1]：原始数据、处理后的数据、实验和数据处理流程[^fgedmiame-e2][^fgedminseqe-e2]（两份最低信息标准见表后） | [数据科学研究](../../06_methods/data_science.md) |
| [综合](../../05_research-strategies/synthesize.md) | 系统综述和元分析：把已发表的研究汇总起来，回答一个问题 | 用结构化、透明、可重复的方法收集和汇总证据[^odea2021preferred-e1]；报告做了什么、为什么这样做、发现了什么，读者才能判断结论能不能信[^odea2021preferred-e2]（生态学的报告清单和动物实验的偏倚评价工具见表后） | [综述研究](../../06_methods/review_study.md)、[元分析](../../06_methods/meta_analysis.md) |

怎么用这张表：

- **复现已发表的实验，也按这些标准做。** 大型复现项目发现了什么，见上文[可复现性](#可复现性领域正在面对的问题)；做法见[复现研究](../../06_methods/replication.md)。
- **开发新实验技术或分析软件，先读目标期刊的要求。** 本文只读了两本期刊的说明，各自只代表本刊。《自然—方法》（Nature Methods）的办刊宗旨要求：方法要有充分的验证，要用在一个重要的生物学问题上，还要拿结果和现有方法比性能[^naturemethodsaims-e1]；选稿看读者面、对方法性能的评估是否全面、技术描述是否完整到别人能马上用上[^naturemethodsaims-e2]。《PLOS 计算生物学》（PLOS Computational Biology）接收的软件文章，介绍的是广泛有用、在提供新的生物学认识上有重大进步的开源（公开源代码、允许别人使用和修改）工具[^ploscompbiolsubmission-e1]；软件要已被广泛采用或有望被广泛采用，源代码要能匿名下载、用开源许可证，还要附上安装和使用文档，包括怎样用附带的测试数据检验软件[^ploscompbiolsubmission-e2]。
- **其他套路本文资料未涉及。**

组学和系统综述两行引用的是具体组织在具体年份发布的标准，不是生物科学的统一规定；现在具体交什么、按什么报告，以目标期刊和数据仓库的要求为准。

- **组学数据：MIAME 和 MINSEQE。** MIAME（Minimum Information About a Microarray Experiment，基因芯片实验最低信息标准）2001 年提出[^fgedmiame-e1]；MINSEQE（Minimum Information about a high-throughput nucleotide SEQuencing Experiment，高通量测序实验最低信息标准）1.0 版发布于 2012 年[^fgedminseqe-e3]。两者都由功能基因组数据学会（Functional Genomics Data Society，FGED）维护，这个学会已经停止运作[^fgedmiame-e3]。MIAME 特别要求写清哪个数据文件对应哪个样品，哪些是技术重复、哪些是生物学重复[^fgedmiame-e2]。数据交到哪个数据库，见上文[数据交到公共数据库](#数据交到公共数据库)。
- **生态学和进化生物学的综述：PRISMA-EcoEvo。** 它是系统综述报告规范 PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses，系统综述和元分析优先报告条目）面向这两个学科的扩展版，2021 年发布，有 27 个主要条目[^odea2021preferred-e5]。其中一条：把综述的目标和方法登记在公开、带时间戳的存档里，最好在检索文献之前[^odea2021preferred-e6]。它的作者评估了 2010–2019 年发表的 102 篇系统综述和元分析，发现报告质量远不理想[^odea2021preferred-e3]；引用了报告指南的少数论文（约 16%），报告质量明显高于平均[^odea2021preferred-e4]。分子和细胞方向（例如汇总体外实验）专门的系统综述报告清单，本文没有找到。通用的 PRISMA 2020 主要为评价健康干预效果的系统综述设计，但它的作者说明，很多条目也适用于目标不是评价干预的系统综述[^page2021prisma-e17]；可以先按它报告，用法见[元分析](../../06_methods/meta_analysis.md#第-8-步按-prisma-2020-报告)。汇总的是动物实验时，再用下一条的 SYRCLE 工具评价偏倚。
- **汇总动物实验：SYRCLE 偏倚风险工具。** SYRCLE 是实验动物系统综述中心（SYstematic Review Centre for Laboratory animal Experimentation）[^hooijmans2014syrcle-e4]。它 2014 年发表的工具有 10 个条目，用来逐篇评价纳入的动物研究有没有偏倚[^hooijmans2014syrcle-e1]；工具改编自 Cochrane 协作网评价随机对照试验的偏倚风险工具[^hooijmans2014syrcle-e2][^hooijmans2014syrcle-e3]。

---

## 本学科常用的研究方法

下面的归类是本手册做的。细胞和分子实验见[实验台实验（湿实验）](../../06_methods/bench_experiment.md)；它和[对照实验](../../06_methods/controlled_experiment.md)逻辑相通，但那篇讲的是人类参与者。动物实验见[临床前动物研究](../../06_methods/preclinical_animal_study.md)。组学和生物信息学分析接近[数据科学](../../06_methods/data_science.md)，数据背后的样品和实验条件要交代清楚；程序、版本、参数怎样记录，见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。计算建模见[定量仿真](../../06_methods/simulation_study.md)，复现见[复现研究](../../06_methods/replication.md)（湿实验复现的难处是方法细节和材料难以获得[^errington2021challenges-e1][^errington2021challenges-e5]），系统综述和元分析见[综述研究](../../06_methods/review_study.md)。

---

## 给新手的建议

1. **动手前先问清组里的规矩。** 记录本怎么记、怎么保管，课题组应有规定[^schnell2015ten-e2]；试剂怎么领、动物和仪器怎么预约，也先问清楚。
2. **设计实验时先定实验单位，再算 n。** 技术重复不能当独立重复用[^perciedusert2020reporting-e4]。拿不准就在动手前问导师或统计人员。
3. **设对照组（不设要说明理由），能随机就随机，能盲就盲**[^perciedusert2020reporting-e1][^perciedusert2020reporting-e7][^perciedusert2020reporting-e8]。
4. **当天记录，写错不擦**[^schnell2015ten-e3][^schnell2015ten-e4]。试剂的来源和批号也记进去。
5. **新的细胞系和抗体先验证再用**[^nihrigorguidance-e4]。
6. **做动物实验前读一遍 ARRIVE**，按它设计，而不是写论文时才补[^perciedusert2020arrive-e7]。
7. **发预印本前查期刊政策**，记住发了就撤不下来[^biorxivabout-e4][^biorxivabout-e5]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 一只小鼠测 50 个细胞，报告 n = 50 | 实验单位是小鼠时 n = 1；这是伪重复，会导致假阳性[^perciedusert2020reporting-e4][^perciedusert2020reporting-e5] |
| 同一份样品测三次，就算"三次重复"并算 P 值 | 技术重复不是对假设的独立检验[^vaux2012replicates-e1] |
| 结果不合预期就去掉某些组或某些样本 | 是误导；独立样本只有特殊情况才能剔除[^perciedusert2020reporting-e9][^vaux2012replicates-e8] |
| 细胞系从别的实验室拿来就用，从不鉴定 | 细胞系鉴定错误和交叉污染并不少见，有估计在 15%～36% 之间[^freedman2015economics-e2] |
| 论文里写"数据未展示"，或只放裁剪过的印迹图 | 有的期刊不允许，例如 PLOS[^plosdatapolicy-e4][^plosdatapolicy-e5] |
| 方法部分写得很简略 | 别人没法重复；复现项目里没有一个实验能只靠原论文设计出复现方案[^errington2021challenges-e1] |

---

## 延伸阅读

- **ARRIVE 2.0 及其解释文件（Percie du Sert 等人 2020，PLoS Biology）**：动物实验的报告清单，解释文件逐条讲了实验单位、对照、随机、盲法。做动物实验前读；做细胞实验的人也能从中学到实验设计。
- **Vaux 等人 2012，Replicates and repeats（EMBO Reports）**：用两个具体例子讲清重复测量和独立重复的区别。第一次算 n 之前读。
- **Schnell 2015，Ten Simple Rules for a Computational Biologist's Laboratory Notebook**：十条记录本规则，篇幅短。
- **NC3Rs（英国国家动物研究 3R 中心）的 3Rs 页面**：3R 原则的定义和例子。
- **Errington 等人 2021 两篇（eLife）**：癌症生物学可复现性项目的结果和遇到的障碍。想了解为什么方法要写详细、材料要共享的人读。
- **ICMJE 关于作者和贡献者的规范**：署名四条件的原文。它面向医学期刊；投生物学期刊时，先读目标期刊自己的作者须知和数据政策。

[^tscharntke2007author-e1]: Tscharntke 等人 2007，第 1 段。[证据](../../../sources/notes/tscharntke2007author.md#e1)
[^tscharntke2007author-e2]: Tscharntke 等人 2007，第 2 段。[证据](../../../sources/notes/tscharntke2007author.md#e2)
[^tscharntke2007author-e3]: Tscharntke 等人 2007，第 2 段。[证据](../../../sources/notes/tscharntke2007author.md#e3)
[^tscharntke2007author-e4]: Tscharntke 等人 2007，第 3 段。[证据](../../../sources/notes/tscharntke2007author.md#e4)
[^schnell2015ten-e1]: Schnell 2015，引言。[证据](../../../sources/notes/schnell2015ten.md#e1)
[^schnell2015ten-e2]: Schnell 2015，Rule 1。[证据](../../../sources/notes/schnell2015ten.md#e2)
[^schnell2015ten-e3]: Schnell 2015，Rule 4。[证据](../../../sources/notes/schnell2015ten.md#e3)
[^schnell2015ten-e4]: Schnell 2015，Rule 5。[证据](../../../sources/notes/schnell2015ten.md#e4)
[^schnell2015ten-e5]: Schnell 2015，Rule 8。[证据](../../../sources/notes/schnell2015ten.md#e5)
[^schnell2015ten-e6]: Schnell 2015，Rule 8。[证据](../../../sources/notes/schnell2015ten.md#e6)
[^schnell2015ten-e7]: Schnell 2015，Rule 6。[证据](../../../sources/notes/schnell2015ten.md#e7)
[^schnell2015ten-e8]: Schnell 2015，引言。[证据](../../../sources/notes/schnell2015ten.md#e8)
[^schnell2015ten-e9]: Schnell 2015，Rule 3。[证据](../../../sources/notes/schnell2015ten.md#e9)
[^errington2021challenges-e1]: Errington 等人 2021（eLife e67995），Abstract。[证据](../../../sources/notes/errington2021challenges.md#e1)
[^errington2021challenges-e2]: Errington 等人 2021（eLife e67995），Abstract。[证据](../../../sources/notes/errington2021challenges.md#e2)
[^errington2021challenges-e3]: Errington 等人 2021（eLife e67995），Challenges during experiments and peer review。[证据](../../../sources/notes/errington2021challenges.md#e3)
[^errington2021challenges-e4]: Errington 等人 2021（eLife e67995），The duration of the different phases in the project。[证据](../../../sources/notes/errington2021challenges.md#e4)
[^errington2021challenges-e5]: Errington 等人 2021（eLife e67995），Independent development of replication protocols。[证据](../../../sources/notes/errington2021challenges.md#e5)
[^errington2021challenges-e6]: Errington 等人 2021（eLife e67995），Abstract。[证据](../../../sources/notes/errington2021challenges.md#e6)
[^errington2021investigating-e1]: Errington 等人 2021（eLife e71601），Abstract。[证据](../../../sources/notes/errington2021investigating.md#e1)
[^errington2021investigating-e2]: Errington 等人 2021（eLife e71601），Abstract。[证据](../../../sources/notes/errington2021investigating.md#e2)
[^errington2021investigating-e3]: Errington 等人 2021（eLife e71601），Abstract。[证据](../../../sources/notes/errington2021investigating.md#e3)
[^biorxivabout-e1]: bioRxiv，About bioRxiv。[证据](../../../sources/notes/biorxivabout.md#e1)
[^biorxivabout-e2]: bioRxiv，About bioRxiv。[证据](../../../sources/notes/biorxivabout.md#e2)
[^biorxivabout-e3]: bioRxiv，About bioRxiv。[证据](../../../sources/notes/biorxivabout.md#e3)
[^biorxivabout-e4]: bioRxiv，About bioRxiv。[证据](../../../sources/notes/biorxivabout.md#e4)
[^biorxivabout-e5]: bioRxiv，Journal Preprint Policies。[证据](../../../sources/notes/biorxivabout.md#e5)
[^biorxivabout-e6]: bioRxiv，About bioRxiv。[证据](../../../sources/notes/biorxivabout.md#e6)
[^icmje2026recommendations-e28]: ICMJE 2026，II.A.2 Who Is an Author?。[证据](../../../sources/notes/icmje2026recommendations.md#e28)
[^perciedusert2020arrive-e1]: Percie du Sert 等人 2020（ARRIVE 2.0），Abstract。[证据](../../../sources/notes/perciedusert2020arrive.md#e1)
[^perciedusert2020arrive-e2]: Percie du Sert 等人 2020（ARRIVE 2.0），Abstract。[证据](../../../sources/notes/perciedusert2020arrive.md#e2)
[^perciedusert2020arrive-e3]: Percie du Sert 等人 2020（ARRIVE 2.0），Introducing ARRIVE 2.0。[证据](../../../sources/notes/perciedusert2020arrive.md#e3)
[^perciedusert2020arrive-e4]: Percie du Sert 等人 2020（ARRIVE 2.0），Why good reporting is important。[证据](../../../sources/notes/perciedusert2020arrive.md#e4)
[^perciedusert2020arrive-e5]: Percie du Sert 等人 2020（ARRIVE 2.0），Why good reporting is important。[证据](../../../sources/notes/perciedusert2020arrive.md#e5)
[^perciedusert2020arrive-e6]: Percie du Sert 等人 2020（ARRIVE 2.0），Why good reporting is important。[证据](../../../sources/notes/perciedusert2020arrive.md#e6)
[^perciedusert2020arrive-e7]: Percie du Sert 等人 2020（ARRIVE 2.0），Introducing ARRIVE 2.0。[证据](../../../sources/notes/perciedusert2020arrive.md#e7)
[^perciedusert2020arrive-e8]: Percie du Sert 等人 2020（ARRIVE 2.0），Why good reporting is important。[证据](../../../sources/notes/perciedusert2020arrive.md#e8)
[^perciedusert2020arrive-e9]: Percie du Sert 等人 2020（ARRIVE 2.0），Introducing ARRIVE 2.0。[证据](../../../sources/notes/perciedusert2020arrive.md#e9)
[^perciedusert2020reporting-e1]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1a。[证据](../../../sources/notes/perciedusert2020reporting.md#e1)
[^perciedusert2020reporting-e2]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1a。[证据](../../../sources/notes/perciedusert2020reporting.md#e2)
[^perciedusert2020reporting-e3]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Glossary。[证据](../../../sources/notes/perciedusert2020reporting.md#e3)
[^perciedusert2020reporting-e4]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1b。[证据](../../../sources/notes/perciedusert2020reporting.md#e4)
[^perciedusert2020reporting-e5]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1b。[证据](../../../sources/notes/perciedusert2020reporting.md#e5)
[^perciedusert2020reporting-e6]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1b。[证据](../../../sources/notes/perciedusert2020reporting.md#e6)
[^perciedusert2020reporting-e7]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 4。[证据](../../../sources/notes/perciedusert2020reporting.md#e7)
[^perciedusert2020reporting-e8]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 5。[证据](../../../sources/notes/perciedusert2020reporting.md#e8)
[^perciedusert2020reporting-e9]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1a。[证据](../../../sources/notes/perciedusert2020reporting.md#e9)
[^perciedusert2020reporting-e10]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 1b。[证据](../../../sources/notes/perciedusert2020reporting.md#e10)
[^vaux2012replicates-e1]: Vaux 等人 2012，引言。[证据](../../../sources/notes/vaux2012replicates.md#e1)
[^vaux2012replicates-e2]: Vaux 等人 2012，骨髓集落实验的例子。[证据](../../../sources/notes/vaux2012replicates.md#e2)
[^vaux2012replicates-e4]: Vaux 等人 2012，Why bother with replicates at all?。[证据](../../../sources/notes/vaux2012replicates.md#e4)
[^vaux2012replicates-e5]: Vaux 等人 2012，qRT-PCR 的例子。[证据](../../../sources/notes/vaux2012replicates.md#e5)
[^vaux2012replicates-e6]: Vaux 等人 2012，Sidebar A。[证据](../../../sources/notes/vaux2012replicates.md#e6)
[^vaux2012replicates-e7]: Vaux 等人 2012，So, what is wrong?。[证据](../../../sources/notes/vaux2012replicates.md#e7)
[^vaux2012replicates-e8]: Vaux 等人 2012，Sidebar A。[证据](../../../sources/notes/vaux2012replicates.md#e8)
[^freedman2015economics-e1]: Freedman 等人 2015，正文。[证据](../../../sources/notes/freedman2015economics.md#e1)
[^freedman2015economics-e2]: Freedman 等人 2015，正文，细胞系的例子。[证据](../../../sources/notes/freedman2015economics.md#e2)
[^freedman2015economics-e3]: Freedman 等人 2015，正文，细胞系的例子。[证据](../../../sources/notes/freedman2015economics.md#e3)
[^freedman2015economics-e4]: Freedman 等人 2015，Abstract 和正文。[证据](../../../sources/notes/freedman2015economics.md#e4)
[^nihrigorguidance-e2]: NIH，Rigor and Reproducibility 申请指南。[证据](../../../sources/notes/nihrigorguidance.md#e2)
[^nihrigorguidance-e3]: NIH，Consideration of relevant biological variables。[证据](../../../sources/notes/nihrigorguidance.md#e3)
[^nihrigorguidance-e4]: NIH，Authentication of key biological and/or chemical resources。[证据](../../../sources/notes/nihrigorguidance.md#e4)
[^nc3rsthe3rs-e1]: NC3Rs，What are the 3Rs?。[证据](../../../sources/notes/nc3rsthe3rs.md#e1)
[^nc3rsthe3rs-e2]: NC3Rs，Definitions of the 3Rs。[证据](../../../sources/notes/nc3rsthe3rs.md#e2)
[^nc3rsthe3rs-e3]: NC3Rs，Definitions of the 3Rs。[证据](../../../sources/notes/nc3rsthe3rs.md#e3)
[^nc3rsthe3rs-e4]: NC3Rs，Replacement。[证据](../../../sources/notes/nc3rsthe3rs.md#e4)
[^plosdatapolicy-e1]: PLOS 数据政策，Introduction。[证据](../../../sources/notes/plosdatapolicy.md#e1)
[^plosdatapolicy-e2]: PLOS 数据政策，数据仓库。[证据](../../../sources/notes/plosdatapolicy.md#e2)
[^plosdatapolicy-e3]: PLOS 数据政策，数据仓库。[证据](../../../sources/notes/plosdatapolicy.md#e3)
[^plosdatapolicy-e4]: PLOS 数据政策，Minimal data set。[证据](../../../sources/notes/plosdatapolicy.md#e4)
[^plosdatapolicy-e5]: PLOS 数据政策，Minimal data set。[证据](../../../sources/notes/plosdatapolicy.md#e5)
[^plosdatapolicy-e6]: PLOS 数据政策，Minimal data set。[证据](../../../sources/notes/plosdatapolicy.md#e6)
[^tscharntke2007author-e5]: Tscharntke 等人 2007，第 3 段。[证据](../../../sources/notes/tscharntke2007author.md#e5)
[^vaux2012replicates-e3]: Vaux 等人 2012，Sidebar A。[证据](../../../sources/notes/vaux2012replicates.md#e3)
[^freedman2015economics-e5]: Freedman 等人 2015，解决方案部分。[证据](../../../sources/notes/freedman2015economics.md#e5)
[^nihrigorguidance-e1]: NIH，Rigorous experimental design for robust and unbiased results。[证据](../../../sources/notes/nihrigorguidance.md#e1)
[^nihrigorguidance-e5]: NIH，Consideration of relevant biological variables。[证据](../../../sources/notes/nihrigorguidance.md#e5)
[^fgedmiame-e1]: FGED，MIAME 页面，页首。[证据](../../../sources/notes/fgedmiame.md#e1)
[^fgedmiame-e2]: FGED，MIAME 页面，六个关键要素。[证据](../../../sources/notes/fgedmiame.md#e2)
[^fgedmiame-e3]: FGED，MIAME 页面，页首。[证据](../../../sources/notes/fgedmiame.md#e3)
[^fgedminseqe-e1]: FGED，MINSEQE 页面，页首。[证据](../../../sources/notes/fgedminseqe.md#e1)
[^fgedminseqe-e2]: FGED，MINSEQE 页面，五个要素。[证据](../../../sources/notes/fgedminseqe.md#e2)
[^fgedminseqe-e3]: FGED，MINSEQE 页面，MINSEQE specification。[证据](../../../sources/notes/fgedminseqe.md#e3)
[^odea2021preferred-e1]: O'Dea 等人 2021（PRISMA-EcoEvo），Abstract。[证据](../../../sources/notes/odea2021preferred.md#e1)
[^odea2021preferred-e2]: O'Dea 等人 2021（PRISMA-EcoEvo），Abstract。[证据](../../../sources/notes/odea2021preferred.md#e2)
[^odea2021preferred-e3]: O'Dea 等人 2021（PRISMA-EcoEvo），Abstract。[证据](../../../sources/notes/odea2021preferred.md#e3)
[^odea2021preferred-e4]: O'Dea 等人 2021（PRISMA-EcoEvo），Abstract。[证据](../../../sources/notes/odea2021preferred.md#e4)
[^odea2021preferred-e5]: O'Dea 等人 2021（PRISMA-EcoEvo），Abstract。[证据](../../../sources/notes/odea2021preferred.md#e5)
[^page2021prisma-e17]: Page 等人 2021（PRISMA 2020），Scope of the guideline。[证据](../../../sources/notes/page2021prisma.md#e17)
[^odea2021preferred-e6]: O'Dea 等人 2021（PRISMA-EcoEvo），Table 1，条目 3.1。[证据](../../../sources/notes/odea2021preferred.md#e6)
[^hooijmans2014syrcle-e1]: Hooijmans 等人 2014，Abstract。[证据](../../../sources/notes/hooijmans2014syrcle.md#e1)
[^naturemethodsaims-e1]: Nature Methods，Aims & Scope。[证据](../../../sources/notes/naturemethodsaims.md#e1)
[^naturemethodsaims-e2]: Nature Methods，Aims & Scope。[证据](../../../sources/notes/naturemethodsaims.md#e2)
[^ploscompbiolsubmission-e1]: PLOS Computational Biology 投稿指南，Software Submissions。[证据](../../../sources/notes/ploscompbiolsubmission.md#e1)
[^ploscompbiolsubmission-e2]: PLOS Computational Biology 投稿指南，Software Submissions。[证据](../../../sources/notes/ploscompbiolsubmission.md#e2)
[^hooijmans2014syrcle-e2]: Hooijmans 等人 2014，Abstract。[证据](../../../sources/notes/hooijmans2014syrcle.md#e2)
[^hooijmans2014syrcle-e3]: Hooijmans 等人 2014，Abstract。[证据](../../../sources/notes/hooijmans2014syrcle.md#e3)
[^hooijmans2014syrcle-e4]: Hooijmans 等人 2014，Background。[证据](../../../sources/notes/hooijmans2014syrcle.md#e4)
