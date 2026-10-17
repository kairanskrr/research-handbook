# 生物技术：学科概况

本文讲生物技术研究实际怎样运转。按本项目采用的经济合作与发展组织（OECD）学科分类，本文合并覆盖四个二级学科：2.8 环境生物技术、2.9 工业生物技术、3.4 医学生物技术、4.4 农业生物技术。它们的共同点是：改造生物（菌株、细胞、植物、动物）或利用生物过程，做出有用的东西。

生物技术的实验室日常和生物科学很像。实验记录本、生物学重复和技术重复、试剂和细胞系验证、动物实验规范，见[生物科学篇](../biological-sciences/README.md)，这里不重复。本文只写生物技术多出来的部分：生物安全等级和审批、重组和合成 DNA 的规定、两用研究、转基因生物的国际规则、工程式的研发和放大、测量与描述的标准。人体试验见[临床医学篇](../clinical-medicine/README.md)，专利见[电气、电子与信息工程篇](../electrical-engineering/README.md#发表还是申请专利以美国为例)，各学科共通的做法见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)。生物技术常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。

**读完本文，你应该能：**

- 说清动手做重组 DNA 或病原相关实验之前，要过哪些安全审查（以美国为例），以及去哪里问本单位的规定；
- 分清生物安全等级和病原的风险组，知道"两用研究"是什么意思；
- 知道转基因生物出实验室、出国境时，有国际条约约束加入它的国家；
- 理解为什么实验室里的好结果不等于能放大生产，以及怎样把测量写得让别人能复现。

---

## 本领域研究怎样运转

### 改造生物，拿来用

生物技术里"改造"的核心手段，可以借一份国际条约的定义来理解。《卡塔赫纳生物安全议定书》把"现代生物技术"定义为：体外核酸技术（包括重组 DNA、把核酸直接注入细胞），或者超出"科"这一分类层级的细胞融合；它们突破了自然的繁殖或重组屏障，不是传统育种用的技术[^cbd2000cartagena-e4]。四个分支大致如下（这是本手册的归纳）：

| 分支 | 典型研究对象 | 额外要注意的 |
|---|---|---|
| 环境生物技术 | 用微生物处理污染、回收资源 | 生物体可能被放到野外环境里 |
| 工业生物技术 | 用工程菌、酵母或细胞生产化学品、酶、材料 | 从实验室放大到生产规模 |
| 医学生物技术 | 基因治疗、细胞治疗、生物药、诊断方法 | 进入人体前有专门审批，见[临床医学篇](../clinical-medicine/README.md) |
| 农业生物技术 | 转基因或基因编辑的作物和动物 | 田间试验和跨境运输的规定 |

### 动手之前，先过生物安全审查

和普通生物实验相比，生物技术研究多了一道门槛：很多实验在开始之前就要报批或登记。以美国为例，凡是在接受美国国立卫生研究院（NIH）重组或合成核酸研究资助的机构里做的这类研究[^nih2024guidelines-e2]，不论经费来自哪里，都要遵守 NIH 的准则[^nih2024guidelines-e3]；需要事先批准的实验，在机构生物安全委员会批准之前不得开始，也不得修改[^nih2024guidelines-e7]。细节见下文"本领域的规范和报告标准"。对新手的意思是：新课题的第一周，先问清楚你的实验属于哪一类、要不要报批、谁来签字。审批要花时间，计划里要留出来。

### 设计、构建、测试，反复多轮

很多生物技术项目是工程式的：设计一个基因线路或代谢通路，构建出菌株或细胞系，测它的表现，再根据结果改设计。难点在于生物系统不像电路那样听话。一项合成生物学跨实验室研究的作者指出，从原理走向应用的一大障碍，是生物系统常常对细胞或环境条件的微小变化很敏感[^beal2016reproducibility-e6]。所以每一轮都要把构建体、宿主、培养条件和测量方法记全，否则下一轮没法和这一轮比。记录本怎么记见[生物科学篇](../biological-sciences/README.md#实验记录本是第一手记录)。

### 从摇瓶到发酵罐：放大

工业生物技术的成果最终要放大生产。下面的数字和建议都来自 Crater 和 Lievense 2018 年的一篇文章。两位作者来自美国一家生物技术公司，文中原则是他们根据自己的工业项目经验总结的[^crater2018scaleup-e10]，讲的是工业微生物工艺：

- **规模差得很远。** 实验室工艺（例如 0.5～10 升发酵罐）要转到生产规模（例如 2 万～200 万升），放大倍数从几千到几百万[^crater2018scaleup-e1]。按作者的说法，从实验室到生产通常要 3～10 年[^crater2018scaleup-e2]。
- **不能照搬实验室条件。** 不能简单地把设备放大、照搬实验室条件[^crater2018scaleup-e3]；影响发酵表现的参数很多，多数在放大中会变[^crater2018scaleup-e7]。
- **选菌株时就要想到放大。** 作者说，一个常见的根本错误，是选择和改造宿主菌株时不考虑它适不适合大规模生产[^crater2018scaleup-e5]。实验室阶段的工艺开发，要尽量模拟大规模生产的条件[^crater2018scaleup-e6]。
- **中间要有中试。** 中试通常在生产规模的 1%～10% 进行[^crater2018scaleup-e9]；工业级原料要在采购前先在实验室或中试里验证[^crater2018scaleup-e8]。

作者甚至主张在做第一个实验之前，就做出设想中的生产工艺的概念设计[^crater2018scaleup-e4]。这是一家企业的视角；学位课题未必走到放大这一步。论文里说"有工业应用前景"时要写清规模和条件，这一点和放大的一般问题见[化学工程篇](../chemical-engineering/README.md#实验室结果离工业还有多远放大)。放大还会碰到安全规定：按美国 NIH 准则，超过 10 升培养物的实验，防护条件由机构生物安全委员会决定[^nih2024guidelines-e13]。

### 发表、专利和产业

本文资料没有生物技术特有的发表统计和署名惯例，一般情况见[生物科学篇](../biological-sciences/README.md#发表期刊和预印本)，以目标期刊要求为准。生物技术的成果（菌株、序列、工艺）可能有专利价值，也常和企业合作；投稿、作报告、发预印本之前，先问导师要不要申请专利。美国大学技术转移办公室的说明见[电气、电子与信息工程篇](../electrical-engineering/README.md#发表还是申请专利以美国为例)，和企业合作时的保密与发表安排见[化学工程篇](../chemical-engineering/README.md#和企业合作保密专利发表要提前安排)。

---

## 和其他领域不同的地方

| | 生物技术 | 生物科学（实验室方向） | 计算机 |
|---|---|---|---|
| 目标 | 做出有用的生物体、产品或工艺 | 弄清生命现象的机制 | 做出算法、系统，或研究计算问题 |
| 开工前的审查 | 重组 DNA、病原相关实验可能要先经生物安全委员会批准（美国规定见下文） | 做重组 DNA、病原实验时同样要过生物安全审查；动物实验要伦理审批 | 涉及人时要伦理审查 |
| 成果离开实验室 | 转基因生物有意释放到环境、跨境运输，受国际条约和各国法规管 | 一般不涉及 | 一般没有这类管制 |
| 规模 | 可能要从几升放大到几万升 | 一般停留在实验室规模 | 不涉及 |
| 被滥用的风险 | 部分研究属于"两用研究"，要单独评估 | 部分病原研究也涉及 | 安全研究有类似问题 |

---

## 本领域的规范和报告标准

**下面讲的安全规定大多是美国的。** 别的地方有自己的法规，先看欧盟和中国这两份，思路和美国相近：先评估风险，再按风险分级管理。

- **欧盟**：2009 年的指令 2009/41/EC 管基因修饰微生物的"封闭使用"，就是在有专门防护措施、限制它们接触公众和环境的条件下改造、培养或保存它们[^eu2009contained-e2]。使用者要先评估风险，把活动分成四类，从风险可忽略、用最低的 1 级防护，到高风险、用最高的 4 级防护[^eu2009contained-e3][^eu2009contained-e4]；拿不准时按更严的做[^eu2009contained-e5]；第 3 类及以上要先得到主管机构同意[^eu2009contained-e6]。
- **中国**：《生物安全法》2020 年通过、2021 年施行[^npc2020biosecurity-e1]。它把生物技术研究开发活动按风险分为高、中、低三类[^npc2020biosecurity-e2]；中、高风险的要经批准或备案，并做风险评估[^npc2020biosecurity-e3]；病原微生物实验要在防护等级相应的实验室里做[^npc2020biosecurity-e4]。本文读的是 2020 年英文本；这部法律 2024 年已修改[^npc2024legislature-e1][^npc2024legislature-e2]，以现行中文原文为准。

其他国家和地区的法规，本文资料未涉及。你所在单位一般会有生物安全委员会或类似的部门，以本地法规和单位规定为准。WHO 给科研人员的清单也要求自问：工作是否遵守本机构规定和国家或地区的法律法规[^who2022responsible-e10]。

### 生物安全等级：按风险评估选防护（美国 BMBL）

美国疾病控制与预防中心（CDC）和 NIH 编写的《微生物和生物医学实验室生物安全》（Biosafety in Microbiological and Biomedical Laboratories，BMBL）第 6 版，是建议性文件，不打算作为法规[^cdc2020bmbl-e1]。它的核心原则是按具体实验方案做风险评估[^cdc2020bmbl-e2]。风险评估要弄清四件事：病原或材料有什么危害、哪些操作会让人接触到它、接触后感染的可能性多大、感染的后果是什么[^cdc2020bmbl-e3]。这是实验室负责人和课题组负责人的责任，机构生物安全委员会等也分担[^cdc2020bmbl-e4]。

**生物安全等级**（Biosafety Level，BSL）有四级，每一级都是设施、安全设备、操作规程和个人防护的组合[^cdc2020bmbl-e5]：

| 等级 | BMBL 的描述（概括） |
|---|---|
| 一级 | 教学实验室，以及使用已明确鉴定、已知不会稳定地让健康成人致病的菌株[^cdc2020bmbl-e6] |
| 二级 | 使用能让人患上轻重不等疾病的病原和毒素[^cdc2020bmbl-e7]。不知道人、动物、植物样品（包括原代细胞系）里有没有病原时，往往可以在二级条件下安全操作[^cdc2020bmbl-e8] |
| 三级 | 可能经呼吸道传播、可能造成严重甚至致命感染的病原[^cdc2020bmbl-e9] |
| 四级 | 危及生命、可经气溶胶传播、没有疫苗或疗法的危险外来病原[^cdc2020bmbl-e10] |

两个容易混的地方：

- **安全等级不等于风险组。** 病原按致病能力分"风险组"；属于风险组 3，不等于操作一定要在三级实验室做[^cdc2020bmbl-e11]。NIH 准则也说，防护等级可能等于风险组，也可能根据具体情况升高或降低[^nih2024guidelines-e17]。
- **量大了，要求可能变。** 处理大体积或高浓度的病原，可能需要额外措施[^cdc2020bmbl-e12]。这和上面的放大直接相关。

BMBL 提醒，只读其中几节，连有经验的人也不足以做好安全处理感染性病原的准备[^cdc2020bmbl-e13]。新手的实际做法：先完成单位的生物安全培训，再请导师或生物安全官确认你的实验在哪一级做。

### 重组和合成核酸：美国 NIH 准则和机构生物安全委员会

NIH 的《涉及重组或合成核酸分子研究的准则》（下称"NIH 准则"）规定了美国 NIH 资助机构里这类研究的做法，适用范围见下。本文读的是 2024 年 4 月版；页眉写着 NIH 正在加强和更新生物安全监管[^nih2024guidelines-e14]，使用前请查最新版本。

- **管什么。** 重组核酸指拼接而成、能在活细胞里复制的核酸分子；合成核酸指化学合成或扩增、能和天然核酸配对的分子；也包括它们复制产生的分子[^nih2024guidelines-e1]。
- **管谁。** 接受 NIH 这类资助的机构里的研究[^nih2024guidelines-e2]，而且机构要保证本机构所有这类研究都遵守，不论经费来自哪里[^nih2024guidelines-e3]。违反的后果可能是暂停或终止全机构同类研究的 NIH 经费[^nih2024guidelines-e4]。NIH 资助的境外研究，所在国有规定的要遵守所在国规定[^nih2024guidelines-e16]。
- **机构生物安全委员会**（Institutional Biosafety Committee）至少 5 人，其中至少 2 人不隶属于本机构，代表周边社区在健康和环境方面的利益[^nih2024guidelines-e5]。
- **实验分几类。** 有的要事先批准；有的低风险实验可以在一级防护下做，但开始时要把签名、注明日期的登记文件交给委员会，例如所有组分都来自非致病原核生物和非致病低等真核生物的实验[^nih2024guidelines-e10][^nih2024guidelines-e11]；还有一些豁免的实验不用登记，但其他生物安全标准仍可能适用[^nih2024guidelines-e12]。自己判断属于哪一类容易出错，交给委员会确认。
- **课题组负责人的责任。** 负责人代表机构对遵守准则负全责[^nih2024guidelines-e6]。改实验也要报：换了 DNA 来源或宿主—载体系统，都要提交委员会审查[^nih2024guidelines-e9]；重大问题、违规和事故，要在 30 天内报告[^nih2024guidelines-e8]。学生不是负责人，但改实验前先告诉负责人，出了事故马上报告。
- **医学生物技术：人体基因转移。** 把重组或合成核酸转入人体的实验，要在临床试验所在地的机构生物安全委员会批准、并取得所有监管批准之后才能开始[^nih2024guidelines-e15]。

### 两用研究：想一想成果会不会被滥用

世界卫生组织（WHO）2022 年的《负责任使用生命科学全球指导框架》给了几个基本概念：

- **生物安全**（biosafety）：防止人无意中接触病原、防止病原意外泄漏[^who2022responsible-e3]。**生物安保**（biosecurity）：防止病原等生物材料被未经授权取得、丢失、被盗、滥用或释放[^who2022responsible-e4]。两者加上两用研究的监管，是生物风险管理的三根支柱[^who2022responsible-e5]。
- **两用研究**：出于有益目的，但成果也可能被故意滥用、危害人、动物、植物和环境的研究[^who2022responsible-e2]。其中不加修改或稍加修改就容易被滥用来造成伤害的，叫**值得关注的两用研究**（dual-use research of concern）[^who2022responsible-e1]。

WHO 给科研人员的清单，开工前就要问[^who2022responsible-e6]：成果会不会被滥用、准备了什么应对措施[^who2022responsible-e7]；能不能换一种方法、设计或生物体，让实验更安全[^who2022responsible-e8]；是否属于出口管制范围[^who2022responsible-e9]。它也承认，除非不做，风险不可能降到零[^who2022responsible-e11]，而且风险管理是各方共同的责任[^who2022responsible-e12]。

**美国的两用研究政策在 2025–2026 年有变化，本项目没有读到现行的官方文件。** 下面只转述两份二手资料，都不能当作现行要求。一是美国国会研究服务处（Congressional Research Service，为国会提供分析的机构）2025 年 5 月的简报：美国没有一部统一、带法律处罚的联邦法律来监管实验室生物安全和安保，靠的是联邦法律、联邦指南和自我管理的混合[^crs2025gainoffunction-e1][^crs2025gainoffunction-e3]；2024 年出台的政策把两用研究和"增强大流行潜力病原研究"（也叫功能增益研究）放在一起监管，原定 2025 年 5 月 6 日生效[^crs2025gainoffunction-e4]，但 2025 年 5 月 5 日的行政令要求修订或替换它[^crs2025gainoffunction-e5]，NIH 也撤销了落实它的通知[^crs2025gainoffunction-e6]。二是研究管理组织 CASRAI 2026 年 8 月的解读文章（第三方解读，不是政府原文）：它说 2026 年 7 月发布了替代 2024 年政策的新政策[^casrai2026highrisk-e1][^casrai2026highrisk-e2]；按它的转述，课题组负责人要在提交申请前书面说明研究属于哪一类[^casrai2026highrisk-e3]，可能属于"危险功能增益研究"的进行中工作要立即停止、24 小时内通知资助机构[^casrai2026highrisk-e4]，常规、低风险的功能增益工作不是针对对象[^casrai2026highrisk-e5]。这些转述是否准确、之后是否再变，本项目无法确认；在美国做这类研究，以 NIH 的官方通知和本单位生物安全部门的说明为准。

### 转基因生物：国际条约《卡塔赫纳生物安全议定书》

这是《生物多样性公约》下的一份国际条约，2000 年通过。它的目标是：对可能危害生物多样性的"改性活生物体"，在安全转移、处理和使用上确保足够保护，同时考虑人体健康风险，重点是跨境转移[^cbd2000cartagena-e1]。**改性活生物体**指通过现代生物技术获得新的遗传物质组合的活生物体[^cbd2000cartagena-e3]；按这个定义，转基因菌株、作物、动物都算。

条约约束的是加入它的国家（缔约方），由各国用法律和行政措施落实[^cbd2000cartagena-e2]；你的国家是否加入、怎样落实，以本国法规为准。对研究者最有用的是区分两种情况：

- **封闭使用**：在设施里用具体措施限制生物体接触和影响外部环境[^cbd2000cartagena-e5]。运往对方按其标准封闭使用的，不走"事先知情同意"程序[^cbd2000cartagena-e6]，但随附文件要标明是改性活生物体，写明安全处理要求和收货人信息[^cbd2000cartagena-e8]。和国外实验室交换活的转基因菌株、细胞或种子时，先问本单位怎样办手续。
- **有意释放到环境**：首次跨境转移、目的是释放到进口方环境里的，事先要走"事先知情同意"程序[^cbd2000cartagena-e7]。这意味着，环境生物技术的野外应用、农业生物技术的田间试验，都可能落到这一类。

### 测量和描述：写到别人能复现

生物技术的结果常常是一个数（表达量、产量、荧光强度），数是怎么测出来的决定了它有没有意义。**定量 PCR 按 MIQE 报告。** 实时荧光定量 PCR（qPCR；PCR 即聚合酶链式反应，用来扩增 DNA）是测核酸量的常用方法。Bustin 等人 2009 年的 MIQE（定量 PCR 实验发表最低信息）指出，很多论文实验细节不够，读者没法评价，也没法重复[^bustin2009miqe-e1]。它给了一份投稿时随附的清单[^bustin2009miqe-e2]，标为"必需"的条目是审稿人评价、别人重复工作所必需的[^bustin2009miqe-e8]。其中几条要点：

- **只用一个内参基因归一化**（内参基因是用来校正样品之间差别的参照基因），除非有证据证明它在你的实验条件下表达不变，否则不可接受；用几个、用哪个，要实验确定[^bustin2009miqe-e5]。
- **每块板都设无模板对照**（不加样品核酸的空白反应），事先定好剔除数据的条件[^bustin2009miqe-e6]。
- **低于检出限的结果不报**，报"0"没有意义[^bustin2009miqe-e7]。多数 RNA 定量是相对的，不是绝对的[^bustin2009miqe-e9]。
- **公开全部试剂、序列和分析方法**[^bustin2009miqe-e3]；不建议报告未经验证的商品化检测的结果[^bustin2009miqe-e10]。

据 MIQE 第一作者 Bustin 2025 年的一篇社论性文章，修订版 MIQE 2.0 已经发表，报告要求有简化和更新[^bustin2025miqe-e1][^bustin2025miqe-e2]。本项目没有读到 MIQE 2.0 原文，上面的清单条目来自 2009 年版，投稿时以最新版为准。这篇文章还说，遵守情况仍然参差不齐，作者举的问题包括扩增效率靠假设、内参基因没验证[^bustin2025miqe-e3][^bustin2025miqe-e4]。

**荧光等读数要校准。** Beal 等人 2016 年报告了合成生物学第一项大规模跨实验室研究：借 2014、2015 年国际基因工程机器大赛（iGEM），全球 88 个机构测了大肠杆菌里三个构建体（人工拼装的 DNA 片段）的荧光[^beal2016reproducibility-e1]。很少有人能测绝对荧光值，只能比比值[^beal2016reproducibility-e2]；宿主菌株不影响比值，但用哪台仪器有影响[^beal2016reproducibility-e3]。作者说，校准做得极不一致，不比直接用任意单位好[^beal2016reproducibility-e4]，并呼吁用校准过的测量得到标准单位，减少操作中"没写下来"的差别[^beal2016reproducibility-e5]。

**设计也可以用标准格式描述。** 合成生物学开放语言（Synthetic Biology Open Language，SBOL）是社区开发的数据标准，用计算机能处理的方式记录生物设计[^mclaughlin2020sbol3-e1]。据其开发者 2020 年的文章，它是期刊 ACS Synthetic Biology 推荐的工程化核酸构建体描述格式[^mclaughlin2020sbol3-e2]。投其他期刊时，看对方是否有要求。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，按核心主张来定，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。本文资料能支持的，是生物技术里的三种套路；综合等其他套路在本学科怎样用，本文资料未涉及。表的分组和"在生物技术里的样子"一栏是本项目的归纳；每条标准只代表脚注里那份资料所在的方向。

| 套路 | 在生物技术里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md) | 设计并构建工程菌、细胞系或植株，或开发生物过程并逐级放大，按"设计—构建—测试"多轮迭代 | 生物系统常对细胞或环境条件的微小变化很敏感（合成生物学）[^beal2016reproducibility-e6]，所以每轮的构建体、宿主、条件都要记全；说"能工业化"之前要知道，放大时多数参数会变，不能照搬实验室条件（工业微生物工艺，企业作者的经验）[^crater2018scaleup-e3][^crater2018scaleup-e7] | [实验台实验](../../06_methods/bench_experiment.md)；建模用[定量仿真](../../06_methods/simulation_study.md)；放大见上文[从摇瓶到发酵罐：放大](#从摇瓶到发酵罐放大) |
| [解释因果](../../05_research-strategies/explain_causality.md) | 弄清机制：敲除、过表达或突变某个基因，或加入抑制剂，看表型、产量或通路是否跟着变，以此说明"是这个因素造成的" | 下面几条来自 MDAR（Materials Design Analysis Reporting，材料、设计、分析、报告框架）。它是多家出版机构的编辑和美国开放科学中心 2021 年发表的生命科学报告框架[^macleod2021mdar-e2]，面向探索性实验室研究，不取代已有的专门标准（如上文的 MIQE）[^macleod2021mdar-e1]。写明实验独立做了几次[^macleod2021mdar-e3]，重复是生物学重复（不同实验单位）还是技术重复（同一单位测多次）[^macleod2021mdar-e4]；只有技术重复时要说明，误差反映的是操作的波动，不是生物学的波动[^macleod2021mdar-e7]；对照组定义清楚，没设对照要说明理由[^macleod2021mdar-e6]；离群值怎么处理，做实验前定好[^macleod2021mdar-e9]；细胞系对照国际细胞系鉴定委员会（International Cell Line Authentication Committee，ICLAC）的错认细胞系名单，名单上的不用，其他的定期鉴定[^macleod2021mdar-e10]。实验单位怎么定、怎么随机，探索性结果为什么要靠验证性实验确认，见实验台实验页 | [实验台实验](../../06_methods/bench_experiment.md)（[探索性和验证性](../../06_methods/bench_experiment.md#1-这是什么研究什么时候用)、[找实验单位](../../06_methods/bench_experiment.md#第-2-步画出层级找到实验单位)）；进入动物的部分见[临床前动物研究](../../06_methods/preclinical_animal_study.md) |
| [测量](../../05_research-strategies/measure.md) | 测表达量、产量、荧光强度，开发新的检测方法，或多个实验室测同一批样品做比对 | qPCR 按 MIQE 清单报告，"必需"条目是审稿人评价、别人重复工作所必需的[^bustin2009miqe-e8]；只用一个未经验证的内参基因不可接受[^bustin2009miqe-e5]；荧光读数受仪器影响[^beal2016reproducibility-e3]，要用校准过的测量得到标准单位[^beal2016reproducibility-e5] | [实验测量研究](../../06_methods/experimental_measurement.md)、[复现研究](../../06_methods/replication.md)；上文[测量和描述：写到别人能复现](#测量和描述写到别人能复现) |

**怎么用这张表**：很多项目几种套路都有，例如构建一株新菌（构建改进），它的产量数据要按测量的标准来报，再敲掉一个基因说明产量为什么提高（解释因果）。按核心主张定主要套路，其余部分按各自的标准要求；进入动物或人体的部分，按下一节所列方法和[临床医学篇](../clinical-medicine/README.md)的规矩。

---

## 本学科常用的研究方法

生物技术没有独有的研究方法页，常用的都是跨学科方法，见[研究类型总览](../../06_methods/README.md)。下面的对应关系是本项目的归纳。

- **菌株和细胞系构建、生物过程开发**：见[实验台实验（湿实验）](../../06_methods/bench_experiment.md)。思路接近计算机的[工程研究](../computer-science/practices/engineering_research.md)，条件优化可参考[优化研究](../computer-science/practices/optimization_study.md)，不同在于开工前可能要报批。
- **机制研究**（敲除、过表达、抑制剂实验）：也用[实验台实验](../../06_methods/bench_experiment.md)，报告要求见上一节表中"解释因果"一行。
- **检测和测量方法开发、跨实验室比对**：见[实验测量研究](../../06_methods/experimental_measurement.md)、[复现研究](../../06_methods/replication.md)，跨实验室的例子如 iGEM 的研究[^beal2016reproducibility-e1]。建模（代谢模型、发酵过程模型）见[定量仿真](../../06_methods/simulation_study.md)。
- **动物实验、人体试验**：见[临床前动物研究](../../06_methods/preclinical_animal_study.md)、[随机对照试验](../../06_methods/randomized_controlled_trial.md)。组学分析见[生物科学篇](../biological-sciences/README.md)。

---

## 给新手的建议

1. **第一周先问清安全手续。** 你的实验在几级防护下做、要不要报批或登记、要哪些培训；以美国为例，需要事先批准的实验，批准前不得开始[^nih2024guidelines-e7]。
2. **改实验前先报。** 换载体、换宿主、换 DNA 来源，在美国都要提交委员会审查[^nih2024guidelines-e9]；在别处也先问负责人。
3. **开题时想一想两用风险。** 用 WHO 清单问自己：成果会不会被滥用，有没有更安全的做法[^who2022responsible-e7][^who2022responsible-e8]。
4. **活的转基因材料寄出去、带出去之前，先问单位。** 《卡塔赫纳生物安全议定书》的重点是跨境转移[^cbd2000cartagena-e1]，由加入它的国家用本国法规落实[^cbd2000cartagena-e2]；具体手续以本国法规为准。
5. **做 qPCR 前读一遍 MIQE 清单**，按它设计对照和内参，而不是投稿时才补[^bustin2009miqe-e5][^bustin2009miqe-e6]。
6. **读数要校准、单位要写清。** 同一个构建体换台仪器，结果就可能不同[^beal2016reproducibility-e3]。
7. **做工业方向的课题，早点想规模。** 选菌株时就考虑它能不能放大[^crater2018scaleup-e5]；论文里写清结果是在什么规模下得到的。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 觉得"只是克隆个基因"，没报批就开工 | 在美国，需要事先批准的实验，批准前不得开始[^nih2024guidelines-e7]；违规可能影响全机构的经费[^nih2024guidelines-e4] |
| 中途换了宿主或载体，没告诉生物安全委员会 | 方案的改动也要提交审查[^nih2024guidelines-e9] |
| 以为病原属于风险组 2 就一律在二级实验室做 | 安全等级不等于风险组，要按具体操作做风险评估[^cdc2020bmbl-e11][^cdc2020bmbl-e2] |
| 小量能做，就默认放大后用同样的防护 | 大体积、高浓度可能需要额外措施[^cdc2020bmbl-e12]；在美国超过 10 升由委员会决定防护[^nih2024guidelines-e13] |
| 把美国 BMBL 当成各国通用的法规 | BMBL 是美国的建议性文件，不是法规[^cdc2020bmbl-e1]；各国以本地法规为准 |
| qPCR 只用一个内参基因，也没验证它稳定 | MIQE 认为这不可接受[^bustin2009miqe-e5] |
| 报告"表达量为 0" | 低于检出限的结果不应报告，"0"没有意义[^bustin2009miqe-e7] |
| 荧光只报任意单位，不写仪器和校准方法 | 仪器会影响结果[^beal2016reproducibility-e3]；不一致的校准不比任意单位好[^beal2016reproducibility-e4] |
| 摇瓶里产量高，就宣称"可以工业化" | 放大时多数参数会变，不能照搬实验室条件[^crater2018scaleup-e3][^crater2018scaleup-e7] |

---

## 延伸阅读

- **美国 CDC 和 NIH，BMBL 第 6 版（2020）**：讲生物安全等级和风险评估，第 II、III 节是入门；它是美国的建议性文件，不是法规。
- **美国 NIH 准则（2024 年 4 月版）**：在美国做重组或合成核酸研究要读；重点是第 III 节（实验分类）和第 IV-B-7 节（课题组负责人的责任）。NIH 说正在更新生物安全监管，注意查最新版本。
- **WHO，Global guidance framework for the responsible use of the life sciences（2022）**：两用研究和生物风险管理的概念；第 5 节 Box 6 是给科研人员的清单。
- **《卡塔赫纳生物安全议定书》文本**：转基因生物跨境转移的国际规则，只约束缔约方；本文用到第 1～3、6、7、18 条。
- **Bustin 等人 2009，MIQE（Clinical Chemistry）**：做 qPCR 时要对照的报告清单，表 1 是清单；本项目未读到 MIQE 2.0 原文，投稿时查最新版。
- **Crater 和 Lievense 2018（FEMS Microbiology Letters）**：两位企业作者根据自身经验讲工业微生物工艺的放大。
- **Beal 等人 2016（PLoS ONE）**：一个跨实验室研究的实例，说明为什么要校准、要写清测量方法。
- **你所在单位的生物安全委员会说明和所在国的法规**：本文引用的多是美国规定，以本地为准。

[^cbd2000cartagena-e1]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 1。[证据](../../../sources/notes/cbd2000cartagena.md#e1)
[^cbd2000cartagena-e2]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 2.1。[证据](../../../sources/notes/cbd2000cartagena.md#e2)
[^cbd2000cartagena-e3]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 3(g)。[证据](../../../sources/notes/cbd2000cartagena.md#e3)
[^cbd2000cartagena-e4]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 3(i)。[证据](../../../sources/notes/cbd2000cartagena.md#e4)
[^cbd2000cartagena-e5]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 3(b)。[证据](../../../sources/notes/cbd2000cartagena.md#e5)
[^cbd2000cartagena-e6]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 6.2。[证据](../../../sources/notes/cbd2000cartagena.md#e6)
[^cbd2000cartagena-e7]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 7.1。[证据](../../../sources/notes/cbd2000cartagena.md#e7)
[^cbd2000cartagena-e8]: 《生物多样性公约》秘书处 2000（卡塔赫纳议定书），Article 18.2(b)。[证据](../../../sources/notes/cbd2000cartagena.md#e8)
[^nih2024guidelines-e1]: 美国 NIH 2024（NIH 准则），Section I-B。[证据](../../../sources/notes/nih2024guidelines.md#e1)
[^nih2024guidelines-e2]: 美国 NIH 2024（NIH 准则），Section I-C-1-a-(1)。[证据](../../../sources/notes/nih2024guidelines.md#e2)
[^nih2024guidelines-e3]: 美国 NIH 2024（NIH 准则），Section I-D。[证据](../../../sources/notes/nih2024guidelines.md#e3)
[^nih2024guidelines-e4]: 美国 NIH 2024（NIH 准则），Section I-D-1。[证据](../../../sources/notes/nih2024guidelines.md#e4)
[^nih2024guidelines-e5]: 美国 NIH 2024（NIH 准则），Section IV-B-2-a-(1)。[证据](../../../sources/notes/nih2024guidelines.md#e5)
[^nih2024guidelines-e6]: 美国 NIH 2024（NIH 准则），Section IV-B-7。[证据](../../../sources/notes/nih2024guidelines.md#e6)
[^nih2024guidelines-e7]: 美国 NIH 2024（NIH 准则），Section IV-B-7-a-(1)。[证据](../../../sources/notes/nih2024guidelines.md#e7)
[^nih2024guidelines-e8]: 美国 NIH 2024（NIH 准则），Section IV-B-7-a-(3)。[证据](../../../sources/notes/nih2024guidelines.md#e8)
[^nih2024guidelines-e9]: 美国 NIH 2024（NIH 准则），Section IV-B-7-c-(3)。[证据](../../../sources/notes/nih2024guidelines.md#e9)
[^nih2024guidelines-e10]: 美国 NIH 2024（NIH 准则），Section III-E。[证据](../../../sources/notes/nih2024guidelines.md#e10)
[^nih2024guidelines-e11]: 美国 NIH 2024（NIH 准则），Section III-E。[证据](../../../sources/notes/nih2024guidelines.md#e11)
[^nih2024guidelines-e12]: 美国 NIH 2024（NIH 准则），Section III-F。[证据](../../../sources/notes/nih2024guidelines.md#e12)
[^nih2024guidelines-e13]: 美国 NIH 2024（NIH 准则），Section III-D-6。[证据](../../../sources/notes/nih2024guidelines.md#e13)
[^nih2024guidelines-e14]: 美国 NIH 2024（NIH 准则），页眉。[证据](../../../sources/notes/nih2024guidelines.md#e14)
[^nih2024guidelines-e15]: 美国 NIH 2024（NIH 准则），Section I-A-1-a。[证据](../../../sources/notes/nih2024guidelines.md#e15)
[^nih2024guidelines-e16]: 美国 NIH 2024（NIH 准则），Section I-C-1-b-(3)。[证据](../../../sources/notes/nih2024guidelines.md#e16)
[^nih2024guidelines-e17]: 美国 NIH 2024（NIH 准则），Section II-A-3。[证据](../../../sources/notes/nih2024guidelines.md#e17)
[^cdc2020bmbl-e1]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Foreword。[证据](../../../sources/notes/cdc2020bmbl.md#e1)
[^cdc2020bmbl-e2]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Foreword。[证据](../../../sources/notes/cdc2020bmbl.md#e2)
[^cdc2020bmbl-e3]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section II。[证据](../../../sources/notes/cdc2020bmbl.md#e3)
[^cdc2020bmbl-e4]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section II。[证据](../../../sources/notes/cdc2020bmbl.md#e4)
[^cdc2020bmbl-e5]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Levels。[证据](../../../sources/notes/cdc2020bmbl.md#e5)
[^cdc2020bmbl-e6]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Level 1。[证据](../../../sources/notes/cdc2020bmbl.md#e6)
[^cdc2020bmbl-e7]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Level 2。[证据](../../../sources/notes/cdc2020bmbl.md#e7)
[^cdc2020bmbl-e8]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Level 2。[证据](../../../sources/notes/cdc2020bmbl.md#e8)
[^cdc2020bmbl-e9]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Level 3。[证据](../../../sources/notes/cdc2020bmbl.md#e9)
[^cdc2020bmbl-e10]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Level 4。[证据](../../../sources/notes/cdc2020bmbl.md#e10)
[^cdc2020bmbl-e11]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Levels。[证据](../../../sources/notes/cdc2020bmbl.md#e11)
[^cdc2020bmbl-e12]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section III, Biosafety Levels。[证据](../../../sources/notes/cdc2020bmbl.md#e12)
[^cdc2020bmbl-e13]: 美国 CDC 和 NIH 2020（BMBL 第 6 版），Section I。[证据](../../../sources/notes/cdc2020bmbl.md#e13)
[^who2022responsible-e1]: WHO 2022，Glossary。[证据](../../../sources/notes/who2022responsible.md#e1)
[^who2022responsible-e2]: WHO 2022，Glossary。[证据](../../../sources/notes/who2022responsible.md#e2)
[^who2022responsible-e3]: WHO 2022，Glossary。[证据](../../../sources/notes/who2022responsible.md#e3)
[^who2022responsible-e4]: WHO 2022，Glossary。[证据](../../../sources/notes/who2022responsible.md#e4)
[^who2022responsible-e5]: WHO 2022，Executive summary。[证据](../../../sources/notes/who2022responsible.md#e5)
[^who2022responsible-e6]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e6)
[^who2022responsible-e7]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e7)
[^who2022responsible-e8]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e8)
[^who2022responsible-e9]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e9)
[^who2022responsible-e10]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e10)
[^who2022responsible-e11]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e11)
[^who2022responsible-e12]: WHO 2022，Section 5.3, Box 6。[证据](../../../sources/notes/who2022responsible.md#e12)
[^crs2025gainoffunction-e1]: 美国国会研究服务处 2025（IN12554），第 1 段。[证据](../../../sources/notes/crs2025gainoffunction.md#e1)
[^crs2025gainoffunction-e3]: 美国国会研究服务处 2025（IN12554），第 1 段。[证据](../../../sources/notes/crs2025gainoffunction.md#e3)
[^crs2025gainoffunction-e4]: 美国国会研究服务处 2025（IN12554），第 2 段。[证据](../../../sources/notes/crs2025gainoffunction.md#e4)
[^crs2025gainoffunction-e5]: 美国国会研究服务处 2025（IN12554），第 3 段。[证据](../../../sources/notes/crs2025gainoffunction.md#e5)
[^crs2025gainoffunction-e6]: 美国国会研究服务处 2025（IN12554），倒数第 4 段。[证据](../../../sources/notes/crs2025gainoffunction.md#e6)
[^casrai2026highrisk-e1]: CASRAI 编辑部 2026，TL;DR。[证据](../../../sources/notes/casrai2026highrisk.md#e1)
[^casrai2026highrisk-e2]: CASRAI 编辑部 2026，TL;DR。[证据](../../../sources/notes/casrai2026highrisk.md#e2)
[^casrai2026highrisk-e3]: CASRAI 编辑部 2026，New Institutional Obligations。[证据](../../../sources/notes/casrai2026highrisk.md#e3)
[^casrai2026highrisk-e4]: CASRAI 编辑部 2026，New Institutional Obligations。[证据](../../../sources/notes/casrai2026highrisk.md#e4)
[^casrai2026highrisk-e5]: CASRAI 编辑部 2026，Two Categories of Covered Research。[证据](../../../sources/notes/casrai2026highrisk.md#e5)
[^bustin2009miqe-e1]: Bustin 等人 2009（MIQE），Abstract。[证据](../../../sources/notes/bustin2009miqe.md#e1)
[^bustin2009miqe-e2]: Bustin 等人 2009（MIQE），Abstract。[证据](../../../sources/notes/bustin2009miqe.md#e2)
[^bustin2009miqe-e3]: Bustin 等人 2009（MIQE），Abstract。[证据](../../../sources/notes/bustin2009miqe.md#e3)
[^bustin2009miqe-e5]: Bustin 等人 2009（MIQE），8.1 Normalization。[证据](../../../sources/notes/bustin2009miqe.md#e5)
[^bustin2009miqe-e6]: Bustin 等人 2009（MIQE），7.3 Controls and quantification calibrators。[证据](../../../sources/notes/bustin2009miqe.md#e6)
[^bustin2009miqe-e7]: Bustin 等人 2009（MIQE），2.1 Analytical sensitivity。[证据](../../../sources/notes/bustin2009miqe.md#e7)
[^bustin2009miqe-e8]: Bustin 等人 2009（MIQE），Conclusions。[证据](../../../sources/notes/bustin2009miqe.md#e8)
[^bustin2009miqe-e9]: Bustin 等人 2009（MIQE），2. Conceptual Considerations。[证据](../../../sources/notes/bustin2009miqe.md#e9)
[^bustin2009miqe-e10]: Bustin 等人 2009（MIQE），2. Conceptual Considerations。[证据](../../../sources/notes/bustin2009miqe.md#e10)
[^bustin2025miqe-e1]: Bustin 2025（IJMS），第 1 段。[证据](../../../sources/notes/bustin2025miqe.md#e1)
[^bustin2025miqe-e2]: Bustin 2025（IJMS），第 2 段。[证据](../../../sources/notes/bustin2025miqe.md#e2)
[^bustin2025miqe-e3]: Bustin 2025（IJMS），第 3 段。[证据](../../../sources/notes/bustin2025miqe.md#e3)
[^bustin2025miqe-e4]: Bustin 2025（IJMS），第 5 段。[证据](../../../sources/notes/bustin2025miqe.md#e4)
[^beal2016reproducibility-e1]: Beal 等人 2016，Abstract。[证据](../../../sources/notes/beal2016reproducibility.md#e1)
[^beal2016reproducibility-e2]: Beal 等人 2016，Abstract。[证据](../../../sources/notes/beal2016reproducibility.md#e2)
[^beal2016reproducibility-e3]: Beal 等人 2016，Abstract。[证据](../../../sources/notes/beal2016reproducibility.md#e3)
[^beal2016reproducibility-e4]: Beal 等人 2016，Results, Absolute vs. Relative Units。[证据](../../../sources/notes/beal2016reproducibility.md#e4)
[^beal2016reproducibility-e5]: Beal 等人 2016，Introduction。[证据](../../../sources/notes/beal2016reproducibility.md#e5)
[^beal2016reproducibility-e6]: Beal 等人 2016，Introduction。[证据](../../../sources/notes/beal2016reproducibility.md#e6)
[^crater2018scaleup-e1]: Crater 和 Lievense 2018，What is scale-up and why does it matter?。[证据](../../../sources/notes/crater2018scaleup.md#e1)
[^crater2018scaleup-e2]: Crater 和 Lievense 2018，What is scale-up and why does it matter?。[证据](../../../sources/notes/crater2018scaleup.md#e2)
[^crater2018scaleup-e3]: Crater 和 Lievense 2018，Begin with the end in mind。[证据](../../../sources/notes/crater2018scaleup.md#e3)
[^crater2018scaleup-e4]: Crater 和 Lievense 2018，Begin with the end in mind。[证据](../../../sources/notes/crater2018scaleup.md#e4)
[^crater2018scaleup-e5]: Crater 和 Lievense 2018，Key challenges and improvement opportunities。[证据](../../../sources/notes/crater2018scaleup.md#e5)
[^crater2018scaleup-e6]: Crater 和 Lievense 2018，A road map for successful scale-up。[证据](../../../sources/notes/crater2018scaleup.md#e6)
[^crater2018scaleup-e7]: Crater 和 Lievense 2018，Key considerations for fermentation scale-up。[证据](../../../sources/notes/crater2018scaleup.md#e7)
[^crater2018scaleup-e8]: Crater 和 Lievense 2018，Table 1。[证据](../../../sources/notes/crater2018scaleup.md#e8)
[^crater2018scaleup-e9]: Crater 和 Lievense 2018，A road map for successful scale-up。[证据](../../../sources/notes/crater2018scaleup.md#e9)
[^crater2018scaleup-e10]: Crater 和 Lievense 2018，Guiding principles for process scale-up。[证据](../../../sources/notes/crater2018scaleup.md#e10)
[^mclaughlin2020sbol3-e1]: McLaughlin 等人 2020，Abstract。[证据](../../../sources/notes/mclaughlin2020sbol3.md#e1)
[^mclaughlin2020sbol3-e2]: McLaughlin 等人 2020，Introduction。[证据](../../../sources/notes/mclaughlin2020sbol3.md#e2)
[^macleod2021mdar-e1]: Macleod 等人 2021（MDAR，PNAS），正文。[证据](../../../sources/notes/macleod2021mdar.md#e1)
[^macleod2021mdar-e2]: Macleod 等人 2021（MDAR，PNAS），正文和利益声明。[证据](../../../sources/notes/macleod2021mdar.md#e2)
[^macleod2021mdar-e3]: Macleod 等人 2021（MDAR），Elaboration §2.4。[证据](../../../sources/notes/macleod2021mdar.md#e3)
[^macleod2021mdar-e4]: Macleod 等人 2021（MDAR），Elaboration §2.4。[证据](../../../sources/notes/macleod2021mdar.md#e4)
[^macleod2021mdar-e6]: Macleod 等人 2021（MDAR），Elaboration §2.4。[证据](../../../sources/notes/macleod2021mdar.md#e6)
[^macleod2021mdar-e7]: Macleod 等人 2021（MDAR），Elaboration §3.2。[证据](../../../sources/notes/macleod2021mdar.md#e7)
[^macleod2021mdar-e9]: Macleod 等人 2021（MDAR），Elaboration §2.3。[证据](../../../sources/notes/macleod2021mdar.md#e9)
[^macleod2021mdar-e10]: Macleod 等人 2021（MDAR），Elaboration §1.4。[证据](../../../sources/notes/macleod2021mdar.md#e10)
[^eu2009contained-e2]: 欧盟指令 2009/41/EC（2009），Article 2(c)。[证据](../../../sources/notes/eu2009contained.md#e2)
[^eu2009contained-e3]: 欧盟指令 2009/41/EC（2009），Article 4(2)–(3)。[证据](../../../sources/notes/eu2009contained.md#e3)
[^eu2009contained-e4]: 欧盟指令 2009/41/EC（2009），Article 4(3)。[证据](../../../sources/notes/eu2009contained.md#e4)
[^eu2009contained-e5]: 欧盟指令 2009/41/EC（2009），Article 4(4)。[证据](../../../sources/notes/eu2009contained.md#e5)
[^eu2009contained-e6]: 欧盟指令 2009/41/EC（2009），Article 9(2)。[证据](../../../sources/notes/eu2009contained.md#e6)
[^npc2020biosecurity-e1]: 《中华人民共和国生物安全法》2020（全国人大英文本），主席令第 58 号。[证据](../../../sources/notes/npc2020biosecurity.md#e1)
[^npc2020biosecurity-e2]: 《生物安全法》2020（英文本），Article 36。[证据](../../../sources/notes/npc2020biosecurity.md#e2)
[^npc2020biosecurity-e3]: 《生物安全法》2020（英文本），Article 38。[证据](../../../sources/notes/npc2020biosecurity.md#e3)
[^npc2020biosecurity-e4]: 《生物安全法》2020（英文本），Article 45。[证据](../../../sources/notes/npc2020biosecurity.md#e4)
[^npc2024legislature-e1]: 全国人大英文网站 2024 年 4 月 28 日新闻（新华社），第 1–2 段。[证据](../../../sources/notes/npc2024legislature.md#e1)
[^npc2024legislature-e2]: 全国人大英文网站 2024 年 4 月 28 日新闻（新华社），图片说明。[证据](../../../sources/notes/npc2024legislature.md#e2)
