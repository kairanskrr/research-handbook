# 电气、电子与信息工程：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲电气工程、电子工程、信息工程（以下简称"电子信息领域"）的研究实际怎样运转：要做实物、要测量，还常常要在发表、专利和标准之间做安排。这个领域和计算机领域有大片交叉，共通的做法见[计算机篇](../computer-science/README.md)；各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里的主线各章和[贯穿全程](../../08_throughout/README.md)。这里只写本领域特有的东西。

**读完本文，你应该能：**

- 说清本领域和计算机科学的关系，知道交叉部分该参考哪些文档；
- 理解流片、实验平台、仿真和测量在研究节奏里的位置；
- 以 IEEE 为例，知道出版方对署名、一稿多投、会议论文转期刊、预印本有哪些规定；
- 在发表和申请专利之间做出不吃亏的安排。

---

## 本领域研究怎样运转

### 和计算机科学是什么关系

两个学科一直走得很近。按 2005 年计算学科课程总报告的回顾，1990 年代以前，想做软件和计算理论的学生选计算机科学，想做硬件的选电气工程[^shackelford2005computing-e1]。两边都在开发新技术，常在大学的同一个学院，有时需要彼此帮忙[^shackelford2005computing-e2]。1970 年代中期微处理器出现后，计算机工程从电气工程里分了出来，成为独立学科[^shackelford2005computing-e3]。计算机工程研究硬件、软件、通信以及它们之间的相互作用[^shackelford2005computing-e4]。这份报告还提到，有的大学把电气工程和计算机科学放在同一个学院[^shackelford2005computing-e6]。同一份报告这样区分侧重点：在计算机工程里，关注的是硬件设备上的软件；在计算机科学里，软件是表达想法的媒介[^shackelford2005computing-e5]。

交叉的方向包括硬件（芯片、体系结构）、信号处理、通信与网络、控制 `[本项目分析]`。做这些方向，计算机篇的不少内容可以直接参考，下面"常见的研究类型"一节给出了对应文档 `[本项目分析]`。

### 研究要和实物打交道：流片与实验平台

有些方向的结论要靠做出实物、实际测量来证明 `[本项目分析]`。下面是两个例子。
**芯片要"流片"。** 流片（tape-out）指把设计好的芯片交给工厂制造 `[本项目分析]`。为小市场的专门用途直接找商业代工厂做一颗专用芯片（Application-Specific Integrated Circuit，ASIC），成本可能很高；**多项目晶圆**（Multi Project Wafer，MPW）是降低原型成本的一种办法[^europracticempw-e1]，做法是把多个设计放在同一片晶圆上一起制造 `[本项目分析]`。下面以欧洲的芯片原型服务机构 Europractice 为例说明流程。这只是一家机构的做法；其他地区的服务机构、代工厂和你所在单位的渠道，流程和条件可能不同，以实际使用的渠道为准 `[本项目分析]`。在 Europractice，流程是[^europracticempw-e3]：

1. 设计完成后提交；
2. 做电气规则检查和设计规则检查；
3. 交给代工厂，在某一轮多项目晶圆上制造；
4. 把原型芯片寄回，由设计者测试和验证。

Europractice 寄回的原型芯片一般没有封装，也没有测过[^europracticempw-e4]，所以拿到芯片后还有不少测试工作要自己做 `[本项目分析]`。另外，选定工艺后，要拿到代工厂的**设计套件**（包括设计规则、电气参数、标准单元库）才能设计；在 Europractice，拿到它要先签保密协议或设计套件许可协议[^europracticempw-e2]。这意味着你的完整设计可能不能像代码那样直接公开 `[本项目分析]`。

**通信和网络实验要上"实验平台"。** 实验平台（testbed）是用真实设备搭起来、专门做实验的系统 `[本项目分析]`。Lamela 等人在无线网络研究中指出：实验平台维护成本越来越高、经常用不上，但结果真实，是验证和调优协议必不可少的一步[^lamela2019repeatable-e2]。

这类工作的节奏常由外部排期决定：多项目晶圆按轮次开工，平台要预约；一次流片出错，可能要等下一轮重来 `[本项目分析]`。所以动手前要把检查做足，把时间往回排。排期的通用方法见贯穿全程的[计划与日常节奏](../../08_throughout/planning_and_routines.md)。

### 仿真和测量：两样都要，各有局限

下面三条来自无线网络和信号处理方向的文献，其他方向可以参考，但未必完全一样 `[本项目分析]`

- **仿真偏乐观。** 在无线网络研究里，仿真很灵活，但为了建模必须做很多简化，结果往往偏乐观[^lamela2019repeatable-e1]。
- **测量难重复。** 真实的无线实验受噪声、干扰、多径（信号经不同路径反射后叠加）等随机因素影响，同样的输入可能得到差别很大的结果[^lamela2019repeatable-e3]。Vandewalle 等人认为，实物实验大概是最难复现的一类工作，往往最多只能得到统计上等价的结果[^vandewalle2009reproducible-e6]。
- **怎么办。** 测量做不到完全重复，就让测量数据能被别人再用[^vandewalle2009reproducible-e6]；同时详细写明实验装置和测量设备[^vandewalle2009reproducible-e7]。Lamela 等人的办法是：在真实实验中记录实验条件，再在仿真器里回放，让实验条件可以重复[^lamela2019repeatable-e4]。仿真研究怎样做验证和确认，见[定量仿真](../../06_methods/simulation_study.md)。

### 发表：以 IEEE 为例，会议版可以发展成期刊版

IEEE（电气与电子工程师学会）自称是世界上最大的技术专业组织[^ieeeauthorreproducibility-e5]，本文的规范部分以它的规定为例。下面的规则都是 IEEE 自己的；投 IET、Elsevier 等其他出版方或国内期刊时，以对方的规定为准 `[本项目分析]`。IEEE 的出版规则写明，技术出版中常见"逐步发表"：早期想法发在研讨会或预印本上，较成熟的工作发会议，完全成熟的成果发期刊或**汇刊**（Transactions，IEEE 许多期刊的名称）[^ieee2026pspb-e4]。IEEE 支持这条路，但有两个条件[^ieee2026pspb-e5]：

- 期刊版要完整引用之前的会议版；
- 期刊版要比会议版多出**实质性**的技术内容。

投 IEEE 期刊时，要主动披露自己已发表或已投出的相似论文（例如会议论文），并写清新稿和它们有什么不同[^ieeeauthorsubmission-e1]。这和计算机领域多数方向"顶级会议论文就是正式成果"的做法不完全一样（见[计算机篇](../computer-science/README.md#会议是主要的发表渠道)），投稿前要看清目标期刊的要求 `[本项目分析]`。IEEE 还有几条容易踩的规定：

- **一稿多投**指同一篇论文同时在两个以上的出版物审稿；IEEE 各下属单位自己决定是否允许[^ieeeauthorsubmission-e2]，要看具体期刊或会议的规定。
- **会议论文要有人到会报告。** 没有报告的论文，IEEE 可以不把它收进 IEEE Xplore（IEEE 的论文数据库）[^ieee2026pspb-e13]。
- **预印本可以发。** 留在 arXiv、TechRxiv（IEEE 管理的工程技术预印本网站）[^ieee2026pspb-e15]或 IEEE 认可的其他非营利预印本网站上的预印本，IEEE 不算"已发表"[^ieeeauthorposting-e1]。录用后，要把公开版本换成带 DOI（数字对象标识符，一种永久链接）的完整引用，或换成带 DOI 的录用稿[^ieeeauthorposting-e2]；非开放获取的论文，IEEE 排版的正式版不能自己挂到网上[^ieeeauthorposting-e3]。注意：预印本一上传，在专利上就算公开了，见下文"发表还是申请专利"。

### 署名：做原型也算贡献

IEEE 的署名条件有三条，要同时满足[^ieee2026pspb-e6][^ieee2026pspb-e7]：

1. 在理论推导、系统或实验设计、**原型开发**、数据分析中至少一项有重要的智力贡献；
2. 参与起草论文，或在内容上修改论文；
3. 认可最终录用的版本。

原型开发被明确写进了第 1 条[^ieee2026pspb-e6]。也就是说，搭硬件、做测试的人，只要另外两条也满足，就应该署名 `[本项目分析]`。作者顺序 IEEE 不做规定，由作者们自己决定[^ieee2026pspb-e8]。署名的通用原则和怎样提前谈好顺序，见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#5-署名引用和利益冲突给每个贡献者应得的认可)。

---

## 和计算机领域不同的地方

下表是本项目的归纳，用来帮你快速定位差别，不是严格的学科划分 `[本项目分析]`。

| | 电子信息领域 | 计算机领域 |
|---|---|---|
| 结果从哪来 | 理论推导、仿真，再加上实物测量（芯片、电路、实验平台） | 以代码、系统和数据上的实验为主 |
| 周期受谁控制 | 还要受流片轮次、平台预约等外部排期影响 | 主要受会议截稿日控制 |
| 发表路径 | IEEE 明确支持"会议版→期刊版"，期刊版要有实质新增内容[^ieee2026pspb-e5] | 多数方向以顶级会议为主（见[计算机篇](../computer-science/README.md#会议是主要的发表渠道)） |
| 能公开多少 | 芯片设计套件通常要签保密或许可协议才能拿到（Europractice 的例子[^europracticempw-e2]）；企业合作项目可能不让公开代码[^vandewalle2009reproducible-e9] | 实验方向有公开制品（代码、数据）的传统（见[计算机篇](../computer-science/README.md#制品评估与徽章)） |
| 专利 | 发表前可能要考虑申请专利（见下文） | 计算机篇未涉及 |
| 标准 | 通信等方向的部分研究与 IEEE、3GPP 等标准组织的工作相关（见下文） | 计算机篇未涉及 |

---

## 本领域的规范和报告标准

### IEEE 伦理准则和出版规则

IEEE 的出版运行手册收有《IEEE 伦理准则》全文。其中和本领域研究关系较大的两条 `[本项目分析]`：

- **公众安全放在首位。** 发现可能危害公众或环境的因素，要及时披露[^ieee2026pspb-e1]。做电力、医疗电子、汽车电子等方向时，这一条尤其要记住 `[本项目分析]`。
- **利益冲突要披露。** 能避免就避免；避免不了，就告诉受影响的各方[^ieee2026pspb-e2]。论文里也要写明资助来源和潜在的利益冲突[^ieee2026pspb-e10]。

IEEE 出版规则中值得单独记住的几条：

- 方法和材料要写到别人能评估、能重做的程度[^ieee2026pspb-e9]。
- 在自己旧作（包括会议论文）的基础上写新稿，要引用旧作，并简要说明新贡献是什么[^ieee2026pspb-e12]。
- 涉及军事、国防等受出口管制的敏感信息，IEEE 不能发表；大学里常教的一般科学、数学、工程原理和已公开的信息不在此列[^ieeeauthorsubmission-e3]。

其余几条是各学科通用的诚信要求：根据数据如实陈述结论、恰当承认别人的贡献[^ieee2026pspb-e3]，不抄袭（IEEE 把不注明出处地使用别人的文字、想法、流程、结果或算法都算作抄袭）[^ieee2026pspb-e11]，发现错误及时更正[^ieee2026pspb-e14]。详细内容见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md#7-发现错误主动更正)。

### 可复现性：信号处理领域的讨论

2009 年，Vandewalle 等人在《IEEE 信号处理杂志》上发文，给"可复现"下的定义是：与研究有关的全部信息（文字、数据、代码等）都公开，让独立研究者能重新得到结果[^vandewalle2009reproducible-e2]。他们检查了 2004 年《IEEE 图像处理汇刊》的全部 134 篇论文，只有 9% 公开了代码，33% 公开了数据[^vandewalle2009reproducible-e3]。他们指出了几种问题：

- 算法论文常常省略确切的数据集、初始化和终止条件、精确的参数值[^vandewalle2009reproducible-e1]；
- 常用测试图像在网上有多个版本，读者不知道论文用的是哪一版[^vandewalle2009reproducible-e4]；
- 连作者自己都复现不了：硬盘上好几个版本的代码，不知道最终的图是哪一版生成的[^vandewalle2009reproducible-e5]。

他们自己的做法可以借鉴：给每张图、每个表各写一个脚本，运行就能重新生成[^vandewalle2009reproducible-e13]；即使代码理论上与平台无关，也写明测试用的平台[^vandewalle2009reproducible-e8]。第一次事后整理花了约一周，后来从一开始就考虑复现，同样的工作约一天完成[^vandewalle2009reproducible-e11]。

IEEE 现在的做法：

- 鼓励（不是强制）所有作者共享数据和代码[^ieeeauthorreproducibility-e1]，数据可以放在 figshare、Zenodo、Dryad 等公开仓库[^ieeeauthorreproducibility-e2]；
- 推荐用 Code Ocean（一个能在云端存放和运行代码的平台）[^ieeeauthorreproducibility-e3]；近五年在 IEEE 发表过论文的作者，可以把代码链接到 IEEE Xplore 上的论文页面[^ieeeauthorreproducibility-e4]；
- 《IEEE 信号处理开放期刊》（OJSP）在试点**复现性审查**[^ojspreproducibility-e2]：论文有条件录用后[^ojspreproducibility-e3]，审稿人在 Code Ocean 上实际运行作者的代码，检查计算结果[^ojspreproducibility-e1]。审查是善意验证，不是故意找让代码出错的极端条件[^ojspreproducibility-e4]。OJSP 解释为什么不只用 GitHub：只放源代码，别人往往要花很多时间配环境才能跑起来[^ojspreproducibility-e5]。这是一本期刊的试点，不是 IEEE 的统一要求 `[本项目分析]`。

**注意术语。** 讨论可复现性时，"reproduce"和"replicate"在不同群体里的用法正好对调[^barba2018terminologies-e2]。信号处理文献多沿用上面 Vandewalle 等人这类说法：reproduce 指用作者公开的数据和代码重新得到结果[^vandewalle2009reproducible-e2]；Barba 的分类表也把信号处理归入 Claerbout、Donoho、Peng 这一派[^barba2018terminologies-e3]。计算机领域（ACM）的用法和它的变化，见[复现研究：先把术语说清楚](../../06_methods/replication.md#先把术语说清楚)。读文献时，先看作者怎么定义这两个词。

### 发表还是申请专利（以美国为例）

如果研究成果有应用价值，发表前要想一想专利 `[本项目分析]`。下面的规则全部来自美国几所大学（罗格斯、伯克利、犹他）技术转移办公室（负责学校专利和成果转化的部门）的说明，按美国法律和这些学校的政策写成。**中国和其他国家的专利法、你所在单位的政策可能不同，以本单位的说明为准。**

**什么算"公开"（美国大学的说法）。** 非保密地把发明告诉公众，而且说得足够清楚，本领域普通技术人员不用过多试验就能照着做出来，就算公开[^rutgersinventionfaq-e4]。容易忽略的几种情况：

- 会议报告本身和公开的摘要都算[^utahprotecting-e3]；没发讲义，只要有听众记了笔记，也算[^rutgersinventionfaq-e5]；
- 预印本一上传就算[^utahprotecting-e2]；
- 期刊论文从正式发表才算，投稿和保密审稿期间不算[^utahprotecting-e1]；
- 在美国，学位论文答辩依法算公开，哪怕只有校内人员参加[^utahprotecting-e4]。

**公开之后会怎样。** 按伯克利的说明，公开之后，在美国只剩一年期限可以申请；在大多数美国以外的国家，直接失去申请资格[^berkeleydisclose-e4]。罗格斯的说明也是这样：先公开再报告学校，就拿不到美国以外的专利权；一年内不申请，美国的专利权也可能丢失[^rutgersinventionfaq-e1][^rutgersinventionfaq-e2]。网上常说的美国"一年宽限期"没有考虑国际专利法等因素，不能依赖[^berkeleydisclose-e3]。

**怎样两头都不耽误。** 伯克利建议最好在公开前至少 1～2 个月向学校提交发明披露[^berkeleydisclose-e2]。美国的"临时申请"可以几天内提交，甚至直接用论文稿或幻灯片，先占住优先权日期[^utahprotecting-e5]。罗格斯明确承诺，只要提前告知，就会在不推迟发表的前提下配合申请专利，也绝不阻止研究者发表[^rutgersinventionfaq-e3]。

**和企业合作。** 伯克利要求合作开始前就向学校提交发明披露[^berkeleydisclose-e1]。罗格斯提醒，大学本来就不是保密的好地方，因为研究者的主要职责之一是发表[^rutgersinventionfaq-e6]。Vandewalle 等人也提到，企业里常常先申请专利再发表，资助研究的企业也可能不愿公开代码[^vandewalle2009reproducible-e9]。这时至少在内部做到可复现，让同事能复现你的结果[^vandewalle2009reproducible-e10]。

### 标准组织

通信等方向的一部分研究会和标准打交道，例如和标准方案做比较，或向标准提交方案 `[本项目分析]`。IEEE 标准协会认为，标准有助于互操作，即让不同设备能配合工作[^ieeesadevelop-e1]。两个例子：

- **IEEE 标准协会（IEEE SA）**：标准按一个分六个阶段的固定流程制定[^ieeesadevelop-e2]，靠相关各方自愿合作[^ieeesadevelop-e3]。它设有专门的专利委员会，负责标准相关的专利政策[^ieeesadevelop-e4]。
- **3GPP（第三代合作伙伴计划）**：1998 年成立，最初为了制定 3G 移动通信标准[^3gpp2026about-e2]，现在的规范覆盖蜂窝移动通信的无线接入、核心网和业务能力[^3gpp2026about-e1]。

如果你的研究和某个标准有关，先读懂标准的相关部分，并问清导师和合作方在专利和保密上的安排 `[本项目分析]`。

---

## 常见的研究类型

**相关学科的研究类型文档**：[实验测量研究](../physical-sciences/research-types/experimental_measurement.md)。

本领域常用的方法，有不少在研究方法和计算机篇的实践里有对应文档，可以直接参考。下面只写本领域额外要注意的地方：

- [工程研究](../computer-science/practices/engineering_research.md)：提出新的电路、算法或系统并评估。评估可能要包括原型的实测结果，不能只靠仿真 `[本项目分析]`。
- [定量仿真](../../06_methods/simulation_study.md)：电路仿真、链路级或网络仿真。无线网络研究的经验是仿真结果偏乐观，最好有实验平台或实测结果对照[^lamela2019repeatable-e1][^lamela2019repeatable-e2]。
- [基准评测](../computer-science/practices/benchmarking.md)：在相同条件下比较多个方案。除了软件环境，还要写明测量装置、设备和测试平台[^vandewalle2009reproducible-e7][^vandewalle2009reproducible-e8]。
- [理论研究](../computer-science/practices/theoretical_research.md)：推导性能界限、证明算法性质。Vandewalle 等人认为信号处理介于理论和实验之间，定理常配上数值仿真，帮助理解结果[^vandewalle2009reproducible-e12]。
- [优化研究](../computer-science/practices/optimization_study.md)：把问题建模成优化问题求解，例如资源分配、电路参数选择 `[本项目分析]`。
- [复现研究](../../06_methods/replication.md)：重做已发表的研究。注意上文的术语问题。
- **测量研究**（没有单独文档）：在真实环境中系统地测量信道、器件或系统的特性 `[本项目分析]`。要点是让测量数据能被别人再用，并详细写明装置[^vandewalle2009reproducible-e6][^vandewalle2009reproducible-e7]。

---

## 给新手的建议

1. **从第一天起为每张图写生成脚本。** Vandewalle 等人从一开始就考虑复现后，整理工作从约一周缩到约一天[^vandewalle2009reproducible-e11]。整理材料的通用做法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。
2. **仿真和测量都做，并说清两者的差距。** 至少在无线网络研究里，只有仿真，结论容易偏乐观[^lamela2019repeatable-e1]。
3. **流片和平台实验，按外部排期倒推计划。** 提交前把检查做足，出了错可能要等下一轮 `[本项目分析]`。
4. **写论文前先想专利。** 投稿、报告、上传预印本之前，先问导师成果要不要申请专利；需要的话，尽早联系本单位负责专利的部门（伯克利的建议是公开前至少 1～2 个月[^berkeleydisclose-e2]）。
5. **会议论文转期刊，要真正扩展内容。** 投 IEEE 期刊时，引用会议版，写清新增了什么[^ieee2026pspb-e5][^ieeeauthorsubmission-e1]。
6. **签保密协议前，先问清能公开什么。** 设计套件、企业数据、合作代码都可能受限[^europracticempw-e2][^vandewalle2009reproducible-e9]；能公开的部分（测量数据、仿真代码）尽量公开 `[本项目分析]`。
7. **读文献时先查术语定义。** reproduce 和 replicate 在不同群体里的用法正好对调[^barba2018terminologies-e2]。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只有仿真结果，就宣称方案在真实系统中有效 | 在无线网络研究里，仿真因为简化往往偏乐观[^lamela2019repeatable-e1] |
| 只报一次实测结果，不说明装置和条件 | 无线实验受随机因素影响，同样输入结果可能差很多[^lamela2019repeatable-e3]；Vandewalle 等人也要求详细写明装置和测量设备[^vandewalle2009reproducible-e7] |
| 论文不写确切参数、数据版本和测试平台 | 别人复现不了，过一段时间自己也复现不了[^vandewalle2009reproducible-e1][^vandewalle2009reproducible-e5] |
| 把会议论文稍作修改就投 IEEE 期刊，也不引用会议版 | IEEE 要求期刊版有实质新增内容并引用前作[^ieee2026pspb-e5] |
| 以为一稿多投总是允许或总是禁止 | 在 IEEE，由各下属单位自行决定，要看具体期刊的规定[^ieeeauthorsubmission-e2] |
| IEEE 会议论文录用后没人去报告 | IEEE 可以不把它收进 IEEE Xplore[^ieee2026pspb-e13] |
| 先在会上报告或发预印本，再想起申请专利 | 按美国大学的说明，在大多数美国以外的国家已经失去申请资格[^berkeleydisclose-e4] |
| 只给做理论和写论文的人署名，忽略做原型和测试的人 | IEEE 把原型开发列为可以构成署名资格的贡献[^ieee2026pspb-e6] |
| 不写资助来源和利益冲突 | IEEE 要求在论文里写明[^ieee2026pspb-e10] |

---

## 延伸阅读

- **IEEE PSPB Operations Manual**：IEEE 出版规则的原始文件，收有《IEEE 伦理准则》全文。重点读 §8.1.7.F（会议论文转期刊）和 §8.2.1（署名与作者责任）。投 IEEE 之前读。
- **IEEE 作者中心（Author Center）的出版伦理页面**：一稿多投、预印本、版权和复现性的具体操作说明。
- **Vandewalle、Kovačević 与 Vetterli 2009，Reproducible Research in Signal Processing**：讲为什么要做可复现研究、怎么做，含作者自己的失败案例。适合刚开始做仿真和算法的人。
- **Barba 2018，Terminologies for Reproducible Research**：整理了各领域对 reproduce 和 replicate 的不同用法。读复现相关文献前读。
- **你所在单位技术转移或专利管理部门的说明**：本文引用的是美国几所大学的页面，各国法律和各单位政策不同，以本单位为准。

[^shackelford2005computing-e1]: Shackelford 等人 2005（Computing Curricula 2005 总报告），§2.2.1，第 9 页。[证据](../../../sources/notes/shackelford2005computing.md#e1)
[^shackelford2005computing-e2]: Shackelford 等人 2005，§2.2.1，第 10 页。[证据](../../../sources/notes/shackelford2005computing.md#e2)
[^shackelford2005computing-e3]: Shackelford 等人 2005，§2.2.1，第 10 页。[证据](../../../sources/notes/shackelford2005computing.md#e3)
[^shackelford2005computing-e4]: Shackelford 等人 2005，§2.3.1，第 13 页。[证据](../../../sources/notes/shackelford2005computing.md#e4)
[^shackelford2005computing-e5]: Shackelford 等人 2005，§2.2.3，第 12 页。[证据](../../../sources/notes/shackelford2005computing.md#e5)
[^shackelford2005computing-e6]: Shackelford 等人 2005，§3.4.1，第 30 页。[证据](../../../sources/notes/shackelford2005computing.md#e6)
[^europracticempw-e1]: Europractice，MPW Prototyping，页首。[证据](../../../sources/notes/europracticempw.md#e1)
[^europracticempw-e2]: Europractice，MPW Prototyping，Selecting and Accessing Technology。[证据](../../../sources/notes/europracticempw.md#e2)
[^europracticempw-e3]: Europractice，MPW Prototyping，Fabricating and Packaging Prototypes。[证据](../../../sources/notes/europracticempw.md#e3)
[^europracticempw-e4]: Europractice，MPW Prototyping，Fabricating and Packaging Prototypes。[证据](../../../sources/notes/europracticempw.md#e4)
[^lamela2019repeatable-e1]: Lamela 等人 2019，I. Introduction。[证据](../../../sources/notes/lamela2019repeatable.md#e1)
[^lamela2019repeatable-e2]: Lamela 等人 2019，I. Introduction。[证据](../../../sources/notes/lamela2019repeatable.md#e2)
[^lamela2019repeatable-e3]: Lamela 等人 2019，I. Introduction。[证据](../../../sources/notes/lamela2019repeatable.md#e3)
[^lamela2019repeatable-e4]: Lamela 等人 2019，III. Trace-based Simulation Approach。[证据](../../../sources/notes/lamela2019repeatable.md#e4)
[^vandewalle2009reproducible-e1]: Vandewalle 等人 2009，开头，第 37 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e1)
[^vandewalle2009reproducible-e2]: Vandewalle 等人 2009，When is research reproducible，第 39 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e2)
[^vandewalle2009reproducible-e3]: Vandewalle 等人 2009，Reproducible research study，第 40 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e3)
[^vandewalle2009reproducible-e4]: Vandewalle 等人 2009，Failures of reproducibility，第 41 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e4)
[^vandewalle2009reproducible-e5]: Vandewalle 等人 2009，Failures of reproducibility，第 41 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e5)
[^vandewalle2009reproducible-e6]: Vandewalle 等人 2009，Experiments，第 41–42 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e6)
[^vandewalle2009reproducible-e7]: Vandewalle 等人 2009，Experiments，第 42 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e7)
[^vandewalle2009reproducible-e8]: Vandewalle 等人 2009，Algorithms，第 41 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e8)
[^vandewalle2009reproducible-e9]: Vandewalle 等人 2009，Implementation and issues，第 43 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e9)
[^vandewalle2009reproducible-e10]: Vandewalle 等人 2009，Implementation and issues，第 43 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e10)
[^vandewalle2009reproducible-e11]: Vandewalle 等人 2009，Case study: super-resolution，第 42 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e11)
[^vandewalle2009reproducible-e12]: Vandewalle 等人 2009，Components 与 Theory，第 41 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e12)
[^vandewalle2009reproducible-e13]: Vandewalle 等人 2009，Case study: super-resolution，第 42 页。[证据](../../../sources/notes/vandewalle2009reproducible.md#e13)
[^ieee2026pspb-e1]: IEEE PSPB Operations Manual 2026，§2.7（《IEEE 伦理准则》第 1 条）。[证据](../../../sources/notes/ieee2026pspb.md#e1)
[^ieee2026pspb-e2]: IEEE PSPB Operations Manual 2026，§2.7（《IEEE 伦理准则》第 3 条）。[证据](../../../sources/notes/ieee2026pspb.md#e2)
[^ieee2026pspb-e3]: IEEE PSPB Operations Manual 2026，§2.7（《IEEE 伦理准则》第 5 条）。[证据](../../../sources/notes/ieee2026pspb.md#e3)
[^ieee2026pspb-e4]: IEEE PSPB Operations Manual 2026，§8.1.7.F。[证据](../../../sources/notes/ieee2026pspb.md#e4)
[^ieee2026pspb-e5]: IEEE PSPB Operations Manual 2026，§8.1.7.F。[证据](../../../sources/notes/ieee2026pspb.md#e5)
[^ieee2026pspb-e6]: IEEE PSPB Operations Manual 2026，§8.2.1.A.1。[证据](../../../sources/notes/ieee2026pspb.md#e6)
[^ieee2026pspb-e7]: IEEE PSPB Operations Manual 2026，§8.2.1.A.1。[证据](../../../sources/notes/ieee2026pspb.md#e7)
[^ieee2026pspb-e8]: IEEE PSPB Operations Manual 2026，§8.2.1.A.2。[证据](../../../sources/notes/ieee2026pspb.md#e8)
[^ieee2026pspb-e9]: IEEE PSPB Operations Manual 2026，§8.2.1.B.3。[证据](../../../sources/notes/ieee2026pspb.md#e9)
[^ieee2026pspb-e10]: IEEE PSPB Operations Manual 2026，§8.2.1.B.2。[证据](../../../sources/notes/ieee2026pspb.md#e10)
[^ieee2026pspb-e11]: IEEE PSPB Operations Manual 2026，§8.2.1.B.9。[证据](../../../sources/notes/ieee2026pspb.md#e11)
[^ieee2026pspb-e12]: IEEE PSPB Operations Manual 2026，§8.2.1.B.12。[证据](../../../sources/notes/ieee2026pspb.md#e12)
[^ieee2026pspb-e13]: IEEE PSPB Operations Manual 2026，§8.2.1.B.16。[证据](../../../sources/notes/ieee2026pspb.md#e13)
[^ieee2026pspb-e14]: IEEE PSPB Operations Manual 2026，§8.2.1.B.8。[证据](../../../sources/notes/ieee2026pspb.md#e14)
[^ieee2026pspb-e15]: IEEE PSPB Operations Manual 2026，§4.3.7。[证据](../../../sources/notes/ieee2026pspb.md#e15)
[^ieeeauthorsubmission-e1]: IEEE 作者中心，Submission and Peer Review Policies，Multiple Submission and Prior Publication。[证据](../../../sources/notes/ieeeauthorsubmission.md#e1)
[^ieeeauthorsubmission-e2]: IEEE 作者中心，Submission and Peer Review Policies，Multiple Submission and Prior Publication。[证据](../../../sources/notes/ieeeauthorsubmission.md#e2)
[^ieeeauthorsubmission-e3]: IEEE 作者中心，Submission and Peer Review Policies，出口管制部分。[证据](../../../sources/notes/ieeeauthorsubmission.md#e3)
[^ieeeauthorposting-e1]: IEEE 作者中心，Post-Publication Policies，Preprint。[证据](../../../sources/notes/ieeeauthorposting.md#e1)
[^ieeeauthorposting-e2]: IEEE 作者中心，Post-Publication Policies，Author-submitted article。[证据](../../../sources/notes/ieeeauthorposting.md#e2)
[^ieeeauthorposting-e3]: IEEE 作者中心，Post-Publication Policies，Published article。[证据](../../../sources/notes/ieeeauthorposting.md#e3)
[^ieeeauthorreproducibility-e1]: IEEE 作者中心，Research Reproducibility，IEEE Open Research Statement。[证据](../../../sources/notes/ieeeauthorreproducibility.md#e1)
[^ieeeauthorreproducibility-e2]: IEEE 作者中心，Research Reproducibility，Sharing Data。[证据](../../../sources/notes/ieeeauthorreproducibility.md#e2)
[^ieeeauthorreproducibility-e3]: IEEE 作者中心，Research Reproducibility，Uploading Code。[证据](../../../sources/notes/ieeeauthorreproducibility.md#e3)
[^ieeeauthorreproducibility-e4]: IEEE 作者中心，Research Reproducibility，Uploading Code。[证据](../../../sources/notes/ieeeauthorreproducibility.md#e4)
[^ieeeauthorreproducibility-e5]: IEEE 作者中心，页脚。[证据](../../../sources/notes/ieeeauthorreproducibility.md#e5)
[^ojspreproducibility-e1]: IEEE 信号处理学会，OJSP 复现性审查作者说明，正文第 1 段。[证据](../../../sources/notes/ojspreproducibility.md#e1)
[^ojspreproducibility-e2]: IEEE 信号处理学会，OJSP 复现性审查作者说明，正文第 1 段。[证据](../../../sources/notes/ojspreproducibility.md#e2)
[^ojspreproducibility-e3]: IEEE 信号处理学会，OJSP 复现性审查作者说明，提交时间说明。[证据](../../../sources/notes/ojspreproducibility.md#e3)
[^ojspreproducibility-e4]: IEEE 信号处理学会，OJSP 复现性审查作者说明，FAQ。[证据](../../../sources/notes/ojspreproducibility.md#e4)
[^ojspreproducibility-e5]: IEEE 信号处理学会，OJSP 复现性审查作者说明，FAQ。[证据](../../../sources/notes/ojspreproducibility.md#e5)
[^barba2018terminologies-e2]: Barba 2018，Introduction。[证据](../../../sources/notes/barba2018terminologies.md#e2)
[^barba2018terminologies-e3]: Barba 2018，决策树说明；Conclusions，Table 2。[证据](../../../sources/notes/barba2018terminologies.md#e3)
[^rutgersinventionfaq-e1]: Rutgers 技术转移常见问题，When should I submit an invention disclosure?。[证据](../../../sources/notes/rutgersinventionfaq.md#e1)
[^rutgersinventionfaq-e2]: Rutgers 技术转移常见问题，When should I submit an invention disclosure?。[证据](../../../sources/notes/rutgersinventionfaq.md#e2)
[^rutgersinventionfaq-e3]: Rutgers 技术转移常见问题，What if I want to publish my results?。[证据](../../../sources/notes/rutgersinventionfaq.md#e3)
[^rutgersinventionfaq-e4]: Rutgers 技术转移常见问题，What constitutes a public disclosure?。[证据](../../../sources/notes/rutgersinventionfaq.md#e4)
[^rutgersinventionfaq-e5]: Rutgers 技术转移常见问题，Oral disclosures。[证据](../../../sources/notes/rutgersinventionfaq.md#e5)
[^rutgersinventionfaq-e6]: Rutgers 技术转移常见问题，面向企业合作方的问题。[证据](../../../sources/notes/rutgersinventionfaq.md#e6)
[^berkeleydisclose-e1]: UC Berkeley IPIRA，When to Disclose an Invention to OTL。[证据](../../../sources/notes/berkeleydisclose.md#e1)
[^berkeleydisclose-e2]: UC Berkeley IPIRA，When to Disclose an Invention to OTL。[证据](../../../sources/notes/berkeleydisclose.md#e2)
[^berkeleydisclose-e3]: UC Berkeley IPIRA，FAQ（宽限期）。[证据](../../../sources/notes/berkeleydisclose.md#e3)
[^berkeleydisclose-e4]: UC Berkeley IPIRA，FAQ（提前公开的后果）。[证据](../../../sources/notes/berkeleydisclose.md#e4)
[^utahprotecting-e1]: University of Utah TLO，Protecting Your Research，Journal publications。[证据](../../../sources/notes/utahprotecting.md#e1)
[^utahprotecting-e2]: University of Utah TLO，Protecting Your Research，Online preprint servers。[证据](../../../sources/notes/utahprotecting.md#e2)
[^utahprotecting-e3]: University of Utah TLO，Protecting Your Research，Conference presentations。[证据](../../../sources/notes/utahprotecting.md#e3)
[^utahprotecting-e4]: University of Utah TLO，Protecting Your Research，Thesis and dissertation defenses。[证据](../../../sources/notes/utahprotecting.md#e4)
[^utahprotecting-e5]: University of Utah TLO，Protecting Your Research，Provisional applications。[证据](../../../sources/notes/utahprotecting.md#e5)
[^ieeesadevelop-e1]: IEEE SA，Develop Standards，页首。[证据](../../../sources/notes/ieeesadevelop.md#e1)
[^ieeesadevelop-e2]: IEEE SA，Develop Standards，页首。[证据](../../../sources/notes/ieeesadevelop.md#e2)
[^ieeesadevelop-e3]: IEEE SA，Develop Standards，Our Principles。[证据](../../../sources/notes/ieeesadevelop.md#e3)
[^ieeesadevelop-e4]: IEEE SA，Develop Standards，Standards Board Committees。[证据](../../../sources/notes/ieeesadevelop.md#e4)
[^3gpp2026about-e1]: 3GPP，About 3GPP，页首。[证据](../../../sources/notes/3gpp2026about.md#e1)
[^3gpp2026about-e2]: 3GPP，About 3GPP，历史部分。[证据](../../../sources/notes/3gpp2026about.md#e2)
