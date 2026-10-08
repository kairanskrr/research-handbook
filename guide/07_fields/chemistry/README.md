# 化学科学：学科概况

本文讲化学研究实际怎样运转：课题组和实验台、把安全当成研究的一部分、记录本、新化合物要交哪些表征数据、合成步骤为什么常常重复不出来、谱图和原始数据怎样报告、ChemRxiv 预印本和署名。各学科共通的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里的主线各章和[贯穿全程](../../08_throughout/README.md)，这里不重复。化学常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。

本文的具体规定多来自美国化学会（American Chemical Society，ACS）和它旗下的期刊，以及美国的安全调查报告，因为这些资料公开、写得具体。**它们是美国机构和具体期刊的规定，不是全世界化学界统一的规矩**；你所在国家、单位和目标期刊有自己的规定时，以本地和目标期刊为准 `[本项目分析]`。例子也偏重有机合成，因为本文找到的具体报告规范多出自这个方向；物理化学、分析化学等方向的惯例可能不同 `[本项目分析]`。

**读完本文，你应该能：**

- 说清自己做的是化学的哪一类工作、属于哪种研究套路，这对论文要交的证据有什么影响；
- 把危害评估当成实验设计的一步，知道什么时候必须重新评估；
- 知道一个新化合物要交哪些证据，才能证明"它是什么"和"它有多纯"；
- 理解合成结果为什么常常重复不出来，自己怎样把步骤写到别人能重复；
- 避开新手在安全、记录、谱图处理和预印本上最常犯的错误。

---

## 本领域研究怎样运转

### 先分清自己做的是哪一类化学

化学的方向很多。化学预印本平台 ChemRxiv 投稿时要从一组分类里选，包括分析化学、有机化学、物理化学、理论与计算化学等[^chemrxivabout-e3]。按日常工作的样子，可以粗分成几类 `[本项目分析]`：

| 类别 | 每天大致在做什么 | 论文的核心证据 |
|---|---|---|
| 合成（有机、无机、高分子等） | 设计并做反应，分离纯化，鉴定产物 | 实验步骤、产率、表征数据和谱图 |
| 物理化学与机理研究 | 测量反应速率、能量、光谱等，解释反应为什么这样发生 | 测量数据及其误差、模型 |
| 分析化学 | 发展和验证测定方法 | 方法的准确度、灵敏度、重复性 |
| 理论与计算化学 | 用量子化学、分子模拟等计算分子性质和反应 | 计算方法、参数、坐标和能量 |

你属于哪一类，决定了要交什么数据。比如美国化学会旗下的《有机化学杂志》（The Journal of Organic Chemistry，JOC），对新化合物要求证明结构和纯度[^acsjocguidelines-e1]，对计算部分要求写明理论方法、基组、程序，并给出分子坐标和能量[^acsjocguidelines-e13]。进组前先弄清楚自己属于哪一类 `[本项目分析]`。

### 课题组和实验台：很多规矩靠口头传

实验化学的日常工作一般在课题组里进行 `[本项目分析]`。按美国一份事故调查报告（见下文）的说法，在大学里，课题负责人（Principal Investigator，PI）一般是负责这项研究、以及实验室里学生、博士后和技术员的教授[^csb2011texastech-e24]。这一点和实验室方向的生物科学相近，见[生物科学篇](../biological-sciences/README.md#实验室围着课题组负责人转)。

新手要特别注意：组里很多关键规矩可能只是口头传下来的。下文讲的 2010 年得克萨斯理工大学事故里，"每次最多合成 100 毫克"这条限制只是课题负责人口头告诉了部分学生[^csb2011texastech-e17]；事后被调查访谈的学生，包括当事人，没有一个说自己知道有严格的 100 毫克上限[^csb2011texastech-e5]。所以，进组后要主动问清楚、并争取写下来：哪些操作有上限、改哪些条件要先问导师 `[本项目分析]`。

Bergman 和 Danheiser（加州大学伯克利分校和麻省理工学院的两位化学教授，Danheiser 当时任《Organic Syntheses》主编）在 2016 年一篇讨论化学结果可重复性的社论里建议，课题负责人应定期和组员当面讨论，查看原始数据和实验记录本[^bergman2016reproducibility-e7]。如果你的组没有这个习惯，你可以主动把记录本和原始谱图带去组会 `[本项目分析]`。

### 实验安全是研究的一部分，不是额外的手续

**案例：得克萨斯理工大学 2010 年实验室爆炸。** 美国化学安全与危害调查委员会（Chemical Safety Board，CSB，调查化学事故的美国联邦机构）专门写了案例研究：

- 2010 年 1 月 7 日，该校化学与生物化学系一名研究生手上的化合物爆炸，他失去三根手指，手和脸烧伤，一只眼睛受伤[^csb2011texastech-e1]。
- 学生决定把这种化合物的合成放大到约 10 克，放大前没有征求课题负责人的意见[^csb2011texastech-e2]；针对当天的合成量，也没有做正式的危害评估[^csb2011texastech-e6]。
- 在这几个做含能材料的实验室里，学生改实验条件（包括自己认为"少量"地增加合成量、改温度）前，不需要征得课题负责人同意[^csb2011texastech-e23]。

报告列出的其他问题（此前的未遂事件没有传开、组会不谈安全、戴不戴护目镜被当成个人选择等），见[化学工程篇](../chemical-engineering/README.md#实验安全是研究的一部分动手前先做危害评估)的逐条介绍。CSB 还指出，本科生多做风险已知、照着做的实验，做研究的学生需要的安全训练和他们很不一样[^csb2011texastech-e22]。管理研究风险，需要针对具体研究的书面规程和培训[^csb2011texastech-e10]。

美国化学会应 CSB 的建议，编写了《研究实验室危害识别与评估》指南[^acs2015identifying-e1]。它写给从本科生到系主任的所有研究者[^acs2015identifying-e4]。下面三条是本文从中挑出的要点 `[本项目分析]`：

1. **动手前先评估。** 研究人员有权利也有责任在开始实验前提问，弄清所有危害和防护措施[^acs2015identifying-e9]。指南介绍的工具包括"如果……会怎样"分析（列一串问题找出可能出错的地方）和检查清单[^acs2015identifying-e3]。
2. **条件一变就重新评估。** 很多事故都能追溯到没被注意到的变化；工作一变，就要对照原来的危害分析，看它是否仍然够用[^acs2015identifying-e5]。需要重新评估的变化包括：放大规模、换了多一个官能团的反应物、组里来了新人或有经验的人离开等[^acs2015identifying-e6]。危害评估是持续的过程[^acs2015identifying-e2]。
3. **多人一起审查，组会上谈安全，讨论未遂事件**[^acs2015identifying-e7][^acs2015identifying-e8]。

安全也写进了发表要求。美国化学会的出版伦理准则（适用于 ACS 旗下期刊）要求，研究中化学品、设备或步骤有任何不寻常的危险，都必须在稿件中明确指出[^acs2026ethical-e3]；2021 年，ACS 出版部给旗下每本期刊的作者须知都加了"安全考虑"要求[^acsjocguidelines-e17]。

### 实验记录本：写给事后核查的人看

在得克萨斯理工大学的事故里，CSB 只能主要靠访谈还原经过，因为实验记录本没有写日期，也不总是记下用了多少反应物[^csb2011texastech-e18]；记录本也没有被课题负责人定期查看，学生之间记法差别很大[^csb2011texastech-e19]。记录本的通行规矩（当场记、写错划掉不擦、保存原始数据）见[生物科学篇](../biological-sciences/README.md#实验记录本是第一手记录)和主线章节[执行与迭代](../../03_conduct-and-analyze/01_run-and-iterate.md#3-每次运行都留下记录)。化学实验额外要记清每次的用量（质量、体积、物质的量）、日期、试剂来源和批次，以及反应中看到的现象 `[本项目分析]`。

### 发表：期刊为主，ChemRxiv 是化学的预印本平台

化学的正式成果一般发表在期刊上 `[本项目分析]`，这和计算机领域以会议为主不同，见[计算机篇](../computer-science/README.md#会议是主要的发表渠道)；审稿要多久，本文资料未涉及，以目标期刊的说明为准。几点要知道：

- **短篇快报和完整论文。** 有的期刊发表短篇的快报（communication 或 letter）。美国化学会的出版伦理准则说，在已发表的快报基础上扩展成完整论文一般可以，但要引用早先的快报，投稿时告诉编辑[^acs2026ethical-e6]。同一准则还要求：一项研究应避免拆成多篇发表[^acs2026ethical-e5]；一稿同时只能投一家期刊[^acs2026ethical-e6]。
- **ChemRxiv。** 它是化学及相关领域未发表预印本的免费平台[^chemrxivabout-e1]，由美国化学会等几家化学学会共同拥有和管理[^chemrxivabout-e4]。上线前只做基本筛查，**不经过同行评审**[^chemrxivabout-e2]；筛查人员不评价内容是否正确、完整、重要[^chemrxivabout-e5]。**发了就基本删不掉**：ChemRxiv 说，发上去的内容可以被引用、算作学术记录的一部分，除极少数情况外不能删除[^chemrxivabout-e6]。
- **先查目标期刊的预印本政策。** ChemRxiv 说大多数期刊接受投稿前发过预印本的稿件，但有的期刊有限制，建议上传前先查[^chemrxivabout-e7]。以 JOC 为例：允许投稿前发预印本，但要在投稿信里说明并给链接[^acsjocguidelines-e14]；投稿之后不先问主编就发预印本，它不鼓励[^acsjocguidelines-e15]。

### 署名：所有作者都要对结果负责

美国化学会的出版伦理准则对署名的要求是：合作者应是对工作有重要科学贡献、并愿意为结果的诚信和准确共同负责的人[^acs2026ethical-e7]；投稿作者负责把稿件发给每位在世的合作者，并取得他们同意[^acs2026ethical-e8]；有贡献但不够署名的人（如技术人员）可以写进致谢[^acs2026ethical-e9]。Bergman 和 Danheiser 强调两点：筹集经费很重要，但署名还应要求直接参与研究并有重要的智力贡献[^bergman2016reproducibility-e9]；发表的结果由所有合作者共同负责，包括课题负责人[^bergman2016reproducibility-e10]。署名的一般原则见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#5-署名引用和利益冲突给每个贡献者应得的认可)。

---

## 和其他领域不同的地方

下表和计算机领域对照。计算机一栏的依据见[计算机篇](../computer-science/README.md)；化学一栏按本文资料整理 `[本项目分析]`。

| | 化学（以实验合成为主） | 计算机 |
|---|---|---|
| 正式发表 | 期刊；ChemRxiv 预印本，政策看目标期刊[^chemrxivabout-e7] | 多数方向以会议为主 |
| 研究对象 | 真实的物质，需要证明"它是什么、有多纯"[^acsjocguidelines-e1] | 代码和数据，可以完整复制 `[本项目分析]` |
| 安全 | 每个反应前都应做危害分析（《Organic Syntheses》的规定措辞）[^orgsyninstructions-e13]；稿件要写明不寻常的危险[^acs2026ethical-e3] | 一般不涉及人身安全，涉及人或漏洞时才有伦理审查 `[本项目分析]` |
| 别人怎样核查你的结果 | 看谱图、色谱图、元素分析等表征数据[^acsjocguidelines-e2]；《Organic Syntheses》还由编委实验室重做[^orgsyninstructions-e2] | 制品评估、重跑代码 |
| 重复不出来时 | 多数涉及原作者确实得到过的真实结果，问题常在没写清的细节（前半句是 Bergman 和 Danheiser 的判断[^bergman2016reproducibility-e6]，后半句为本项目分析） | 常见于环境、随机性、实现细节 `[本项目分析]` |

---

## 本领域的规范和报告标准

### 新化合物：证明"是什么"和"有多纯"

以美国化学会旗下 JOC 的作者须知为例（**只代表这一本期刊；投别的期刊先读它自己的须知**）。做纳米材料、器件这类材料研究的，表征报告的要点见[材料工程篇](../materials-engineering/README.md)。

- **两件事都要证明。** 新化合物必须提供足以确定结构和纯度的证据[^acsjocguidelines-e1]，而且要逐个化合物记录纯度[^acsjocguidelines-e2]。
- **确定结构。** 要有氢谱和碳谱核磁共振（Nuclear Magnetic Resonance，NMR）数据，再加高分辨质谱（High-Resolution Mass Spectrometry，HRMS）或元素分析之一[^acsjocguidelines-e3]。元素分析的碳、氢、氮实测值应与理论值相差在 0.4% 以内[^acsjocguidelines-e6]。
- **证明纯度。** 以合成为主的工作，JOC 不设最低纯度，但要如实记录；化合物要拿去做物理测量或生物测试时，要证明纯度至少 95%[^acsjocguidelines-e4]。熔程窄本身不够；高分辨质谱只能支持分子式，不能证明纯度[^acsjocguidelines-e5]。
- **产率要称出来。** 报告的产率应是分离纯化后称重得到的，同时给出质量和百分比[^acsjocguidelines-e9]。JOC 编辑提醒：产率超过 95%、异构体比例超过 200:1、对映体过量超过 99%，没有进一步解释的话通常不现实[^acsjocguidelines-e10]。
- **缺数据要说明。** 比如太难溶测不了碳谱，要在实验部分写明原因[^acsjocguidelines-e18]。

### 谱图：不能修

JOC 明确说，修改数据或谱图（如校正基线、去掉溶剂峰或杂质峰）是不道德的[^acsjocguidelines-e7]，也不能用修峰软件压低或遮盖杂质峰[^acsjocguidelines-e8]。这不是假想的问题：据 Bergman 和 Danheiser 2016 年的社论，《Organic Letters》编辑部发现，投给该刊的稿件中有 2%～3% 有手工去掉核磁谱峰的迹象[^bergman2016reproducibility-e3]。他们还列出了相关的不当做法：丢掉不符合预期的数据点、只报告最好的一次产率或选择性[^bergman2016reproducibility-e4]。怎样完整报告结果，见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#2-对证据诚实不骗自己报告全部结果)。

### 合成步骤：写到别人能重复

**合成结果常常难以精确重复。** Bergman 和 Danheiser 认为，化学里完全重复不出已发表结果的情况很少，但很难精确重复出论文报告的产率、选择性等数据并不少见[^bergman2016reproducibility-e1]，合成化学尤其如此[^bergman2016reproducibility-e2]。他们认为，多数问题涉及的是原作者确实得到过的真实结果[^bergman2016reproducibility-e6]，也就是说，问题常常出在没写清楚的细节上 `[本项目分析]`。

**最严格的例子：《Organic Syntheses》的独立核查。** 《Organic Syntheses》是一本有机合成期刊，它要求实验步骤写得比一般期刊和支持信息详细得多，而且每个步骤都要在一位编委的实验室里重做核查[^orgsyninstructions-e2]：

- 核查时每一步至少成功做两次，其中至少一次与投稿人规模完全相同[^orgsyninstructions-e3]；核查者的产率和选择性一般不能比原报告低约 5% 以上[^orgsyninstructions-e4]。核查的编委和合作者现在作为"核查作者"署名[^orgsyninstructions-e5]。
- 即便这样，据 Bergman 和 Danheiser 2016 年的社论，2010—2016 年投给这本期刊的稿件中，仍有 7.5%（约每 13 篇有 1 篇）因为编委实验室在合理范围内重复不出原作者的产率或选择性而被拒[^bergman2016reproducibility-e5]。

普通期刊不会替你重做。下面这些是《Organic Syntheses》对投稿的要求和建议，别的期刊不一定要求，但拿来当自查清单很好用 `[本项目分析]`：

- [ ] 所有原料和试剂写明来源，商品试剂写纯度[^orgsyninstructions-e8]
- [ ] 室温写具体摄氏度，不只写"rt"；真空度写具体数值[^orgsyninstructions-e9][^orgsyninstructions-e10]
- [ ] 描述反应中看到的变化：颜色、放气、析出固体、放热[^orgsyninstructions-e11]
- [ ] 上一步粗品直接用于下一步时，说明纯化方法，给出纯品和粗品的数据[^orgsyninstructions-e14]
- [ ] 按所写规模至少做两次；多次产率相差超过 10%，可能还有没找到的影响因素[^orgsyninstructions-e6][^orgsyninstructions-e7]
- [ ] 投稿前请一位没参与的同事只看你写的步骤重复一次（"内部核查"）[^orgsyninstructions-e6][^bergman2016reproducibility-e8]

### 数据：支持信息、原始数据与 FAIR

**支持信息**（Supporting Information，SI）是随论文一起发布的补充文件。JOC 允许把实验内容放在正文、支持信息或两者里，只要准确完整，详细到别人能重复[^acsjocguidelines-e11]。

- **原始数据要保存。** 美国化学会的出版伦理准则要求数据在发表后至少保存并可提供五年，鼓励存入公开数据库[^acs2026ethical-e2]。JOC 要求作者提供核磁原始数据文件（FID 文件，即仪器直接采集、尚未处理的信号，以及采集和处理参数）[^acsjocguidelines-e12]。所以测完谱，要保存原始文件，不要只留导出的图片 `[本项目分析]`。
- **数据政策分级，看目标期刊。** ACS 的研究数据政策分四级，从"鼓励公开"到"必须公开、数据随稿件一起审"[^acsdatapolicy-e3]，每本期刊自己决定执行哪一级[^acsdatapolicy-e2]。数据可用性声明要说明数据在哪、怎么获取，最好用 DOI 等永久链接[^acsdatapolicy-e4]。
- **FAIR 原则。** FAIR 指数据可查找、可获取、可互操作、可重用，原则本身的介绍见[材料工程篇](../materials-engineering/README.md#材料数据共享与-fair-原则)。ACS 强烈支持这套原则[^acsdatapolicy-e1]；数据放在支持信息里可以接受，但它鼓励提供机器可读的数据[^acsdatapolicy-e5]。想学具体怎么做，可以看国际纯粹与应用化学联合会（IUPAC）维护的《FAIR 化学手册》，它用可交互的示例演示怎样以机器可读的方式管理化学数据[^iupacfaircookbook-e1][^iupacfaircookbook-e2]。数据整理的一般做法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，按核心主张来定，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。下表的分组和"在化学里的样子"一栏是本项目的归纳；每条标准只代表脚注里那本期刊或那个方向（合成多出自 JOC，比较和测量出自催化方向） `[本项目分析]`。

| 套路 | 在化学里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [构建改进](../../05_research-strategies/build_improve.md) | 合成方法学和全合成：发展新反应、新试剂，或做出一个特定分子 | JOC 期待概念上的新意，不只是把已有反应换一类底物、试剂或催化剂再做一遍[^acsjocguidelines-e30]；新化合物要证明结构和纯度[^acsjocguidelines-e1]；产率报分离纯化、称重后的结果[^acsjocguidelines-e9] | [合成与表征研究](../../06_methods/synthesis_study.md) |
| [比较评估](../../05_research-strategies/compare_evaluate.md) | 催化：用活性、选择性、失活情况比较新催化剂和标准催化剂[^bligaard2016benchmarking-e1] | 在相同条件下和成熟或最先进的催化剂比较[^bligaard2016benchmarking-e17]；比较选择性要在相同转化率下测[^bligaard2016benchmarking-e15] | 暂无专门的方法篇 |
| [测量](../../05_research-strategies/measure.md) | 催化：弄清一项测量的现实误差有多大 | 有研究者提议多个课题组盲法轮流测量同一批样品，以确定现实的误差范围[^bligaard2016benchmarking-e8] | [实验测量研究](../../06_methods/experimental_measurement.md) |

机理研究、分析方法开发、计算化学各属于哪种套路、按什么标准评判，本文资料未涉及。

---

## 本学科常用的研究方法

下面的归类是本项目分析 `[本项目分析]`。合成方法学、全合成和目标分子合成，见[合成与表征研究](../../06_methods/synthesis_study.md)。机理和物理化学测量，见[实验测量研究](../../06_methods/experimental_measurement.md)；它和[对照实验](../../06_methods/controlled_experiment.md)一样讲究一次只改一个因素，但对象是化学体系而不是人。计算化学见[定量仿真](../../06_methods/simulation_study.md)，要交代理论方法、基组、程序和坐标[^acsjocguidelines-e13]；比较不同计算方法时，可参考计算机的[基准评测](../computer-science/practices/benchmarking.md)。复现和独立核查见[复现研究](../../06_methods/replication.md)，合成化学里"重复出产率和选择性"本身就是一项要求很高的工作[^orgsyninstructions-e4]。综述见[综述研究](../../06_methods/review_study.md)。分析方法开发暂无对应的方法篇。

---

## 给新手的建议

1. **进组第一周，问清并写下组里的安全规矩。** 哪些物质有用量上限、改哪些条件要先问导师。口头规矩容易传丢[^csb2011texastech-e5]。
2. **每个新反应、每次改条件，都先做危害评估。** 尤其是放大规模、换反应物时[^acs2015identifying-e6]。拿不准就问，提问是研究者的权利和责任[^acs2015identifying-e9]。
3. **护目镜等防护按规定戴，不要当成"看情况"的个人选择** `[本项目分析]`；得克萨斯理工大学的实验室里就有人这样看待护目镜[^csb2011texastech-e16]。遇到未遂事件，即使没人受伤也要报告[^csb2011texastech-e25]；未遂事件只有被记录、跟踪、传达出去，才能起到教育和改进的作用[^csb2011texastech-e11]。
4. **记录本当天记，写日期，写清用量和现象。** 原始谱图文件（FID 等）单独保存[^csb2011texastech-e18][^acsjocguidelines-e12]。
5. **对自己想要的结果多一分怀疑。** 好的课题负责人会训练组员怀疑那些自己希望是对的结果[^bergman2016reproducibility-e11]。不修谱图、不挑最好的一次产率[^acsjocguidelines-e7][^bergman2016reproducibility-e4]。
6. **写实验步骤时，假设读者是一个没来过你们实验室的人。** 按上面的自查清单写，投稿前请同事做一次内部核查[^orgsyninstructions-e6]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 觉得"只是放大一点"，不重新评估就做 | 放大是需要重新评估的典型变化[^acs2015identifying-e6]；得克萨斯理工大学事故就发生在一次未经评估的放大之后[^csb2011texastech-e2][^csb2011texastech-e6] |
| 记录本不写日期、不写用量 | 出了问题无法还原经过[^csb2011texastech-e18]，结果也无法重复 `[本项目分析]` |
| 用软件去掉谱图里的溶剂峰或杂质峰 | JOC 明确认定为不道德[^acsjocguidelines-e7] |
| 只用高分辨质谱或熔点"证明"纯度 | JOC 说两者都不足以证明新化合物的纯度[^acsjocguidelines-e5] |
| 报告最好的一次产率，或用粗品的核磁算产率 | JOC 要求产率是分离纯化、称重后的结果[^acsjocguidelines-e9]；Bergman 和 Danheiser 把只报最好的一次列为不当行为[^bergman2016reproducibility-e4] |
| 实验步骤写"室温搅拌过夜""减压浓缩" | 温度、压力、时间不明确，别人难以重复[^orgsyninstructions-e9][^orgsyninstructions-e10] |
| 只保存谱图的截图或 PDF | 期刊可能要求原始数据文件[^acsjocguidelines-e12] |
| 投稿后没问主编就发 ChemRxiv 预印本 | 有的期刊（如 JOC）不鼓励[^acsjocguidelines-e15]；而且发了基本删不掉[^chemrxivabout-e6] |
| 把只出了经费、没参与研究的人列为作者 | 署名应要求直接参与和重要的智力贡献[^bergman2016reproducibility-e9][^acs2026ethical-e7] |

---

## 延伸阅读

- **CSB，Texas Tech University Laboratory Explosion（2011）**：美国化学安全与危害调查委员会的事故案例研究，讲清一次放大实验怎样变成事故。进实验室之前值得读一遍。**ACS，Identifying and Evaluating Hazards in Research Laboratories（2015）**：美国化学会的危害评估指南，介绍检查清单等工具；第 6 章讲"条件一变就重新评估"。
- **Bergman & Danheiser 2016，Reproducibility in Chemical Research（Angewandte Chemie 社论）**：两页，讲化学里重复不出结果的几种原因，以及对课题负责人和作者的建议。
- **《Organic Syntheses》作者须知**：比一般期刊详细得多的合成步骤写作要求，适合当自查清单。
- **目标期刊的作者须知**，例如 JOC 的表征和纯度要求、ACS 的研究数据政策。每次投稿前都要重新读。**ACS，Ethical Guidelines to Publication of Chemical Research**：美国化学会旗下期刊的出版伦理准则，包括数据保存、署名和重复发表。
- **IUPAC FAIR Chemistry Cookbook**：想把数据整理成机器可读、可重用格式时读。

[^chemrxivabout-e1]: ChemRxiv，About ChemRxiv。[证据](../../../sources/notes/chemrxivabout.md#e1)
[^chemrxivabout-e2]: ChemRxiv，About ChemRxiv。[证据](../../../sources/notes/chemrxivabout.md#e2)
[^chemrxivabout-e3]: ChemRxiv，About ChemRxiv，Scope。[证据](../../../sources/notes/chemrxivabout.md#e3)
[^chemrxivabout-e4]: ChemRxiv，About ChemRxiv，The ChemRxiv partnership。[证据](../../../sources/notes/chemrxivabout.md#e4)
[^chemrxivabout-e5]: ChemRxiv，作者常见问题，How is the content screened?。[证据](../../../sources/notes/chemrxivabout.md#e5)
[^chemrxivabout-e6]: ChemRxiv，作者常见问题，Can I retract my content?。[证据](../../../sources/notes/chemrxivabout.md#e6)
[^chemrxivabout-e7]: ChemRxiv，作者常见问题，期刊政策。[证据](../../../sources/notes/chemrxivabout.md#e7)
[^acsjocguidelines-e1]: JOC 作者须知，Compound Characterization Data。[证据](../../../sources/notes/acsjocguidelines.md#e1)
[^acsjocguidelines-e2]: JOC 作者须知，Compound Characterization Data。[证据](../../../sources/notes/acsjocguidelines.md#e2)
[^acsjocguidelines-e3]: JOC 作者须知，NMR。[证据](../../../sources/notes/acsjocguidelines.md#e3)
[^acsjocguidelines-e4]: JOC 作者须知，Purity。[证据](../../../sources/notes/acsjocguidelines.md#e4)
[^acsjocguidelines-e5]: JOC 作者须知，Purity。[证据](../../../sources/notes/acsjocguidelines.md#e5)
[^acsjocguidelines-e6]: JOC 作者须知，Elemental Analysis and Accurate Mass Measurement。[证据](../../../sources/notes/acsjocguidelines.md#e6)
[^acsjocguidelines-e7]: JOC 作者须知，Experimental Section。[证据](../../../sources/notes/acsjocguidelines.md#e7)
[^acsjocguidelines-e8]: JOC 作者须知，Purity / NMR 谱图。[证据](../../../sources/notes/acsjocguidelines.md#e8)
[^acsjocguidelines-e9]: JOC 作者须知，Synthesis Experiments。[证据](../../../sources/notes/acsjocguidelines.md#e9)
[^acsjocguidelines-e10]: JOC 作者须知，Synthesis Experiments。[证据](../../../sources/notes/acsjocguidelines.md#e10)
[^acsjocguidelines-e11]: JOC 作者须知，Experimental Section/Computational Methods。[证据](../../../sources/notes/acsjocguidelines.md#e11)
[^acsjocguidelines-e12]: JOC 作者须知，NMR 原始数据。[证据](../../../sources/notes/acsjocguidelines.md#e12)
[^acsjocguidelines-e13]: JOC 作者须知，Computational Data。[证据](../../../sources/notes/acsjocguidelines.md#e13)
[^acsjocguidelines-e14]: JOC 作者须知，Editorial Policies（预印本）。[证据](../../../sources/notes/acsjocguidelines.md#e14)
[^acsjocguidelines-e15]: JOC 作者须知，Editorial Policies（预印本）。[证据](../../../sources/notes/acsjocguidelines.md#e15)
[^acsjocguidelines-e17]: JOC 作者须知，Emphasis on Chemical Safety。[证据](../../../sources/notes/acsjocguidelines.md#e17)
[^acsjocguidelines-e18]: JOC 作者须知，Compound Characterization Data。[证据](../../../sources/notes/acsjocguidelines.md#e18)
[^csb2011texastech-e1]: CSB 2011，1.0 Introduction。[证据](../../../sources/notes/csb2011texastech.md#e1)
[^csb2011texastech-e17]: CSB 2011，3.0 Pre-incident Events。[证据](../../../sources/notes/csb2011texastech.md#e17)
[^csb2011texastech-e5]: CSB 2011，3.0 Pre-incident Events。[证据](../../../sources/notes/csb2011texastech.md#e5)
[^csb2011texastech-e2]: CSB 2011，4.0 Incident Description。[证据](../../../sources/notes/csb2011texastech.md#e2)
[^csb2011texastech-e6]: CSB 2011，4.0 Incident Description。[证据](../../../sources/notes/csb2011texastech.md#e6)
[^csb2011texastech-e18]: CSB 2011，第 3 页脚注 7。[证据](../../../sources/notes/csb2011texastech.md#e18)
[^csb2011texastech-e19]: CSB 2011，6.2.3。[证据](../../../sources/notes/csb2011texastech.md#e19)
[^csb2011texastech-e11]: CSB 2011，9.0 Key Lessons。[证据](../../../sources/notes/csb2011texastech.md#e11)
[^csb2011texastech-e22]: CSB 2011，6.2.2。[证据](../../../sources/notes/csb2011texastech.md#e22)
[^csb2011texastech-e16]: CSB 2011，4.0 Incident Description。[证据](../../../sources/notes/csb2011texastech.md#e16)
[^csb2011texastech-e10]: CSB 2011，9.0 Key Lessons。[证据](../../../sources/notes/csb2011texastech.md#e10)
[^csb2011texastech-e23]: CSB 2011，6.2.3。[证据](../../../sources/notes/csb2011texastech.md#e23)
[^csb2011texastech-e24]: CSB 2011，第 3 页脚注 6。[证据](../../../sources/notes/csb2011texastech.md#e24)
[^csb2011texastech-e25]: CSB 2011，7.0。[证据](../../../sources/notes/csb2011texastech.md#e25)
[^acs2015identifying-e1]: ACS 2015，Executive Summary。[证据](../../../sources/notes/acs2015identifying.md#e1)
[^acs2015identifying-e2]: ACS 2015，Executive Summary。[证据](../../../sources/notes/acs2015identifying.md#e2)
[^acs2015identifying-e3]: ACS 2015，Executive Summary。[证据](../../../sources/notes/acs2015identifying.md#e3)
[^acs2015identifying-e4]: ACS 2015，1.2 Application。[证据](../../../sources/notes/acs2015identifying.md#e4)
[^acs2015identifying-e5]: ACS 2015，6. Change Control。[证据](../../../sources/notes/acs2015identifying.md#e5)
[^acs2015identifying-e6]: ACS 2015，6.1 Recognizing Change。[证据](../../../sources/notes/acs2015identifying.md#e6)
[^acs2015identifying-e7]: ACS 2015，5.3。[证据](../../../sources/notes/acs2015identifying.md#e7)
[^acs2015identifying-e8]: ACS 2015，5.3。[证据](../../../sources/notes/acs2015identifying.md#e8)
[^acs2015identifying-e9]: ACS 2015，4.3 Researcher and Laboratory Worker。[证据](../../../sources/notes/acs2015identifying.md#e9)
[^acs2026ethical-e2]: ACS 出版伦理准则（2026 年修订），B 第 3 条。[证据](../../../sources/notes/acs2026ethical.md#e2)
[^acs2026ethical-e3]: ACS 出版伦理准则（2026 年修订），B 第 5 条。[证据](../../../sources/notes/acs2026ethical.md#e3)
[^acs2026ethical-e5]: ACS 出版伦理准则（2026 年修订），B 第 7 条。[证据](../../../sources/notes/acs2026ethical.md#e5)
[^acs2026ethical-e6]: ACS 出版伦理准则（2026 年修订），B 第 9 条。[证据](../../../sources/notes/acs2026ethical.md#e6)
[^acs2026ethical-e7]: ACS 出版伦理准则（2026 年修订），B 第 13 条。[证据](../../../sources/notes/acs2026ethical.md#e7)
[^acs2026ethical-e8]: ACS 出版伦理准则（2026 年修订），B 第 13 条。[证据](../../../sources/notes/acs2026ethical.md#e8)
[^acs2026ethical-e9]: ACS 出版伦理准则（2026 年修订），B 第 13 条。[证据](../../../sources/notes/acs2026ethical.md#e9)
[^bergman2016reproducibility-e1]: Bergman & Danheiser 2016，Sources of Irreproducibility。[证据](../../../sources/notes/bergman2016reproducibility.md#e1)
[^bergman2016reproducibility-e2]: Bergman & Danheiser 2016，Sources of Irreproducibility。[证据](../../../sources/notes/bergman2016reproducibility.md#e2)
[^bergman2016reproducibility-e3]: Bergman & Danheiser 2016，Sources of Irreproducibility。[证据](../../../sources/notes/bergman2016reproducibility.md#e3)
[^bergman2016reproducibility-e4]: Bergman & Danheiser 2016，Sources of Irreproducibility。[证据](../../../sources/notes/bergman2016reproducibility.md#e4)
[^bergman2016reproducibility-e5]: Bergman & Danheiser 2016，Replicating Valid Results。[证据](../../../sources/notes/bergman2016reproducibility.md#e5)
[^bergman2016reproducibility-e6]: Bergman & Danheiser 2016，Replicating Valid Results。[证据](../../../sources/notes/bergman2016reproducibility.md#e6)
[^bergman2016reproducibility-e7]: Bergman & Danheiser 2016，Recommendations。[证据](../../../sources/notes/bergman2016reproducibility.md#e7)
[^bergman2016reproducibility-e8]: Bergman & Danheiser 2016，Recommendations。[证据](../../../sources/notes/bergman2016reproducibility.md#e8)
[^bergman2016reproducibility-e9]: Bergman & Danheiser 2016，Recommendations。[证据](../../../sources/notes/bergman2016reproducibility.md#e9)
[^bergman2016reproducibility-e10]: Bergman & Danheiser 2016，Recommendations。[证据](../../../sources/notes/bergman2016reproducibility.md#e10)
[^bergman2016reproducibility-e11]: Bergman & Danheiser 2016，Recommendations。[证据](../../../sources/notes/bergman2016reproducibility.md#e11)
[^orgsyninstructions-e2]: Organic Syntheses 作者须知，开头。[证据](../../../sources/notes/orgsyninstructions.md#e2)
[^orgsyninstructions-e3]: Organic Syntheses 作者须知，Checking of procedures。[证据](../../../sources/notes/orgsyninstructions.md#e3)
[^orgsyninstructions-e4]: Organic Syntheses 作者须知，Checking of procedures。[证据](../../../sources/notes/orgsyninstructions.md#e4)
[^orgsyninstructions-e5]: Organic Syntheses 作者须知，Checking of procedures。[证据](../../../sources/notes/orgsyninstructions.md#e5)
[^orgsyninstructions-e6]: Organic Syntheses 作者须知，Scale / reproducibility。[证据](../../../sources/notes/orgsyninstructions.md#e6)
[^orgsyninstructions-e7]: Organic Syntheses 作者须知，Scale / reproducibility。[证据](../../../sources/notes/orgsyninstructions.md#e7)
[^orgsyninstructions-e8]: Organic Syntheses 作者须知，Common Omissions。[证据](../../../sources/notes/orgsyninstructions.md#e8)
[^orgsyninstructions-e9]: Organic Syntheses 作者须知，Common Omissions。[证据](../../../sources/notes/orgsyninstructions.md#e9)
[^orgsyninstructions-e10]: Organic Syntheses 作者须知，Reaction procedure。[证据](../../../sources/notes/orgsyninstructions.md#e10)
[^orgsyninstructions-e11]: Organic Syntheses 作者须知，Reaction procedure。[证据](../../../sources/notes/orgsyninstructions.md#e11)
[^orgsyninstructions-e13]: Organic Syntheses 作者须知，Safety（Note 1）。[证据](../../../sources/notes/orgsyninstructions.md#e13)
[^orgsyninstructions-e14]: Organic Syntheses 作者须知，Common Omissions。[证据](../../../sources/notes/orgsyninstructions.md#e14)
[^acsdatapolicy-e1]: ACS 研究数据政策，开头。[证据](../../../sources/notes/acsdatapolicy.md#e1)
[^acsdatapolicy-e2]: ACS 研究数据政策，ACS Research Data Policy。[证据](../../../sources/notes/acsdatapolicy.md#e2)
[^acsdatapolicy-e3]: ACS 研究数据政策，Research Data Policy Levels。[证据](../../../sources/notes/acsdatapolicy.md#e3)
[^acsdatapolicy-e4]: ACS 研究数据政策，Data Availability Statements。[证据](../../../sources/notes/acsdatapolicy.md#e4)
[^acsdatapolicy-e5]: ACS 研究数据政策，Data Availability Statements。[证据](../../../sources/notes/acsdatapolicy.md#e5)
[^iupacfaircookbook-e1]: IUPAC FAIR Chemistry Cookbook，首页。[证据](../../../sources/notes/iupacfaircookbook.md#e1)
[^iupacfaircookbook-e2]: IUPAC FAIR Chemistry Cookbook，首页。[证据](../../../sources/notes/iupacfaircookbook.md#e2)
[^acsjocguidelines-e30]: JOC 作者须知，Scope of the Journal (a)。[证据](../../../sources/notes/acsjocguidelines.md#e30)
[^bligaard2016benchmarking-e1]: Bligaard 等人 2016，摘要。[证据](../../../sources/notes/bligaard2016benchmarking.md#e1)
[^bligaard2016benchmarking-e8]: Bligaard 等人 2016，§2.2.1，第 2595 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e8)
[^bligaard2016benchmarking-e15]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e15)
[^bligaard2016benchmarking-e17]: Bligaard 等人 2016，§2.3.1，第 2597 页。[证据](../../../sources/notes/bligaard2016benchmarking.md#e17)
