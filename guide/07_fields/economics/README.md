# 经济学与商学：学科概况

本文讲经济学的研究实际怎样运转：理论和实证的分工，围绕"因果识别"的实证方法，工作论文先行、期刊审稿很慢的发表方式，以及研讨会、求职论文、按字母署名等惯例。本文以经济学为主；商学院里的金融、管理、市场营销等方向各有惯例，这里没有展开 `[本项目分析]`。各学科共通的做法（选题、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里列出的各章和[贯穿全程](../../08_throughout/README.md)，这里不重复；常用哪些研究套路、各看什么证据，见[常用套路与证据标准](#常用套路与证据标准)。

**读完本文，你应该能：**

- 用大白话说清什么是"识别策略"，以及几种常见因果识别方法各靠什么假设；
- 理解工作论文、"五大期刊"、研讨会和求职论文在经济学里的位置；
- 知道美国经济学会（American Economic Association，AEA）期刊对数据、代码、实验登记和利益披露的要求；
- 知道经济学实证研究主要走哪种研究套路、按什么标准评判；
- 避开设定搜索、只看显著性等新手常犯的错误。

---

## 本领域研究怎样运转

### 理论和实证：一个模型，一套数据

经济学研究大致分两类：建理论模型，和用数据做实证 `[本项目分析]`。一篇论文里可以两者都有（见本节末尾）。

**理论模型**的骨架，Varian 说"看起来都差不多"：有一些行为人，各自为目标做选择；选择受约束；有某种东西会调整，让大家的选择相互一致[^varian1997build-e4]。Varian 建议先算最简单的例子，再写最简单的模型，能再简化就再简化[^varian1997build-e5]；之后再推广，看结论有多一般[^varian1997build-e6]。

**实证研究**又分几种路子（下面的分法是本项目的归纳 `[本项目分析]`）：

- **应用微观**：用个人、家庭、企业层面的数据研究劳动、教育、健康、发展、公共财政等问题 `[本项目分析]`。据 Angrist 和 Pischke 2010 年的判断，以研究设计为核心的做法（下一节讲）主要见于发展、教育、环境、劳动、健康、公共财政这些微观领域，在产业组织和宏观经济学中仍然少见[^angrist2010credibility-e2]。
- **宏观**：据 Angrist 和 Pischke 2010 年的描述，很多宏观经济学家转向"计算实验"：先建一个理论上的模型经济，再"校准"参数，让模型在关键统计特征上像真实经济，然后改变税率、货币规则等参数看结果[^angrist2010credibility-e14]。Angrist 和 Pischke 认为，这能讲清模型的含义，但不直接提供因果效应的证据[^angrist2010credibility-e14]。
- **结构估计与简约式估计**：结构估计是把完整的经济模型（偏好、技术、市场行为）拿去拟合数据，再用估出的参数模拟没发生过的情形 `[本项目分析]`。Angrist 和 Pischke 描述的产业组织兼并分析是一个例子：先估计需求，再假设企业之间怎样竞争，最后模拟有无兼并时的行业表现[^angrist2010credibility-e21]。相对的"简约式"（reduced-form）或"设计派"做法，不写出完整模型，只靠研究设计直接估计某个因果效应 `[本项目分析]`。两派的争论见下文。

在 Cochrane 看来，多数论文的主要结果是实证的；文中的理论或模型是用来帮助理解实证结果的[^cochrane2005writing-e11]。

### 可信性革命：先回答"你的识别策略是什么"

**识别**（identification）说的是：你凭什么认为数据里看到的关系是因果关系，而不是巧合、反向因果或遗漏了别的因素。**识别策略**就是你给出的这条理由 `[本项目分析]`。

Angrist 和 Pischke 把实证经济学的这场变化称为"可信性革命"，认为它来自以研究设计为本的做法：重视因果效应的识别，借助真实实验或自然实验，并花大力气论证结果为什么能作因果解释[^angrist2010credibility-e1]。"你的识别策略是什么？"已经是实证研讨会上的常规提问[^angrist2010credibility-e10]。Cochrane 说得更直接：实证研究最重要的三件事是识别、识别、识别[^cochrane2005writing-e4]。

最直接的办法是做随机实验。但实验耗时、昂贵，有时根本做不了（比如研究移民对本国经济的影响）；这时可以利用制度或自然事件造成的变化，这叫"自然实验"或"准实验"[^angrist2010credibility-e3]。准实验研究最常用三种方法：工具变量、断点回归、双重差分[^angrist2010credibility-e4]。用大白话说：

| 方法 | 怎么做 | 靠什么假设 | 要重点检查什么 |
|---|---|---|---|
| 随机实验 | 随机决定谁接受处理（如发现金、给补贴），比较两组 `[本项目分析]` | 分组是随机的，所以两组在处理前平均来说相似 `[本项目分析]` | 随机分组是否真的照做了；两组在处理前是否相似 `[本项目分析]` |
| 工具变量（instrumental variables） | 找一个会影响"原因"的变量，只用它带来的那部分变化来估计效应 `[本项目分析]` | 它只通过你关心的那条渠道影响结果，而且它的取值近似随机分配；这两点都要专门论证[^angrist2010credibility-e5] | 它会不会经由别的渠道影响结果[^angrist2010credibility-e9] |
| 双重差分（difference-in-differences） | 比较受政策影响较大和较小的两组，在政策前后结果的变化有何不同[^angrist2010credibility-e8] | 如果没有这项政策，两组的结果会按相同的趋势变化 `[本项目分析]` | 两组是否各有不同的趋势；有的话，比较就失效了[^angrist2010credibility-e9] |
| 断点回归（regression discontinuity） | 按分数线分组时，比较刚好在线上和刚好在线下的人[^angrist2010credibility-e6] | 分界线两侧的人，除了是否受到处理，其他方面相似[^angrist2010credibility-e7] | 有没有人扎堆在分界线附近；扎堆可能说明分界线本身改变了人们的行为[^angrist2010credibility-e9] |

好的设计还有一个好处：方法容易讲清楚，结果可以直接呈现[^angrist2010credibility-e11]。随机实验也不是万能的：Angrist 和 Pischke 承认，做得好的观察性研究，可能比执行糟糕的随机试验更可信[^angrist2010credibility-e18]。

Cochrane 给实证新手的几条自问，可以直接用作检查清单：是什么经济机制让你的解释变量发生了变化？真正的自然实验并不常有[^cochrane2005writing-e5]。哪些控制变量该放、哪些不该放？他认为多数论文放的解释变量太多了[^cochrane2005writing-e6]。结果在经济上有多大意义？样本很大时，再小的效应也会"统计显著"[^cochrane2005writing-e7]。

> **不同的看法：设计派还是结构派？**
>
> 注意：下面三条都来自 Angrist 和 Pischke 这一篇文章，他们本人是设计派，批评者的观点是他们转述的。结构派几位作者自己的说法见下文[常用套路与证据标准](#常用套路与证据标准)。
>
> - **设计派**（Angrist 和 Pischke）：好的结构模型能同时告诉我们机制和因果效应，但它的估计应该和假设更弱的方法对得上[^angrist2010credibility-e15]。他们更信服好的研究设计得出的结果，而不是好理论推出的结论[^angrist2010credibility-e19]。
> - **批评者**（据 Angrist 和 Pischke 转述，包括 Heckman、Rosenzweig 和 Wolpin、Deaton 等人）：为了追求内部效度，设计派的研究变得狭窄、特殊[^angrist2010credibility-e20]。具体有两条：一个实验得出的结论，换个环境可能不成立（外部效度问题）；研究者在做小问题，大问题没人回答[^angrist2010credibility-e16]。
> - **设计派的回应**：单个研究有局限，就去找更多证据，让更一般的图景逐渐显现[^angrist2010credibility-e17]。
>
> 对新手的实际建议：不管走哪条路，都要能回答"这个数字靠什么假设才成立"。结构模型要说清假设从哪来；设计派研究要说清结论能推广到哪里 `[本项目分析]`。

### 先发工作论文，期刊发表很慢

在经济学里，论文可以在投期刊之前，先以**工作论文**（working paper）的形式公开。例如 NBER（美国国家经济研究局）工作论文：它是成员的新研究，在同行评审之前发布，供讨论和评论[^nberworkingpapers-e1]。IZA 等机构也有自己的讨论稿（discussion paper）系列。IZA 自己说明，这些讨论稿往往是初步成果，引用时要考虑它是暂定版本[^brodeur2016star-e6]。本文引用的几篇研究（Brodeur 等、Heckman 和 Moktan、Ellison、Card 和 DellaVigna）读的也是工作论文或讨论稿版，正式发表版的数字可能略有不同。

据 Heckman 和 Moktan（2018 年讨论稿版）观察，美国排名靠前的经济系里已有名气的学者，越来越多地不在五大或领域期刊发表，而是把论文放在有影响力的工作论文系列里，这些论文引用很高[^heckman2020tyranny-e4]。

期刊审稿很慢。Ellison（2000 年工作论文版，数据到 1999 年）发现：三四十年前，顶级期刊的论文通常投稿后六到九个月被接收；到他写作时，期刊更常要求大幅修改，审稿和修改平均要花大约两年[^ellison2002slowdown-e1]。Econometrica 和 Review of Economic Studies 的审稿周期，从 1970 年代初的 6–12 个月延长到 1990 年代末的 24–30 个月[^ellison2002slowdown-e2]。Heckman 和 Moktan（2018 年讨论稿版）也提到，五大期刊的投稿量和论文篇幅都在增加，拒稿率随之上升，审稿也在拖延[^heckman2020tyranny-e3]。

### "五大期刊"

"五大期刊"（top five）指 American Economic Review、Econometrica、Journal of Political Economy、Quarterly Journal of Economics 和 Review of Economic Studies[^card2013nine-e2]。Card 和 DellaVigna 认为，在这些期刊发表，深刻影响经济学的研究方向、年轻学者的职业道路和学术经济学家的收入[^card2013nine-e1]。据他们统计（2013 年工作论文版），五大的总体接收率从 1980 年的约 15% 降到 2012 年前后的约 6%[^card2013nine-e3]。Heckman 和 Moktan 分析了美国前 35 名经济系预聘教师的履历，发现五大发表对能否拿到终身教职影响很大[^heckman2020tyranny-e1]；但他们也认为这道筛子远不可靠，相当一部分有影响的论文发表在五大之外，靠它选人会鼓励功利而不是创造[^heckman2020tyranny-e2]。

### 研讨会报告

在经济学里，研讨会（seminar）报告是打磨论文的主要场合 `[本项目分析]`。Varian 认为，越多地讲自己的工作，最终的论文越好，因为报告逼你直奔重点[^varian1997build-e7]。听众会当场插话提问[^varian1997build-e10][^cochrane2005writing-e12]；Cochrane 给某个冬季学季的金融研讨会计过时，没有一篇论文在一小时内讲到主要结果[^cochrane2005writing-e12]。他建议不要文献综述和铺垫，直接讲重点[^cochrane2005writing-e8]。报告后要马上记下听众在哪里没听懂、问了什么、推荐了什么文献[^varian1997build-e8]。当听众不再提问时，说明论文快可以投了[^varian1997build-e9]。

### 求职论文

下面依据 Cawley 为 2018–19 求职季写的指南，只讲美国学术就业市场；具体日程每年会变。博士生申请美国学术职位时，必须提交求职信、简历和**求职论文**（job market paper）[^cawley2018guide-e7]。求职成败最重要的因素，是这篇论文的质量和你讲它讲得好不好[^cawley2018guide-e1]。求职时要做的报告（job talk）是基于这篇论文的 90 分钟研讨会报告[^cawley2018guide-e2]。实证论文的作者在面试时会被仔细追问识别策略和方法[^cawley2018guide-e5]；面试官还想确认，论文的想法和关键决定确实出自你本人[^cawley2018guide-e6]。所以求职论文最好是你自己主导的独立工作 `[本项目分析]`。

### 署名按字母顺序

经济学的惯例是合著论文按作者姓氏的字母顺序署名，而不是按贡献排序[^einav2006surname-e1]。1980–2002 年五大期刊上约一半论文是合著，其中 88% 按字母顺序署名[^einav2006surname-e4]。心理学则按贡献排序[^einav2006surname-e3]。这意味着在经济学里，作者顺序一般看不出谁贡献大，贡献要另外说明 `[本项目分析]`。Einav 和 Yariv 还发现，在前十名经济系，姓氏首字母靠前的教师更可能拿到终身教职[^einav2006surname-e2]；心理学中没有这种关系[^einav2006surname-e3]。

---

## 和其他领域不同的地方

| | 经济学 | 对照 |
|---|---|---|
| 主要发表渠道 | 期刊；在顶级期刊发表对职业影响很大[^card2013nine-e1] | 计算机多数方向以会议为主，见[计算机篇](../computer-science/README.md#会议是主要的发表渠道) |
| 成果先怎样公开 | 工作论文，同行评审前发布[^nberworkingpapers-e1] | 计算机常用 arXiv 预印本，见[计算机篇](../computer-science/README.md#双盲评审与预印本) |
| 审稿周期 | 顶级期刊审稿加修改平均约两年（2000 年前后的统计）[^ellison2002slowdown-e1] | 计算机会议有固定日程，一次决定，见[计算机篇](../computer-science/README.md#会议还是期刊一直有争议) |
| 署名顺序 | 惯例是按姓氏字母顺序[^einav2006surname-e1] | 心理学按贡献排序[^einav2006surname-e3] |
| 复现材料 | AEA 期刊在接收前必须提交数据和代码，由数据编辑检查[^aea2026data-e1][^aea2026data-e3] | 计算机的制品评估通常是自愿的，见[计算机篇](../computer-science/README.md#制品评估与徽章) |
| 实证论文的核心追问 | 识别策略[^angrist2010credibility-e10] | 计算机多问"比已有方法好在哪、好多少"，见[计算机篇](../computer-science/README.md#会议是主要的发表渠道) |

---

## 本领域的规范和报告标准

下面以 AEA 旗下期刊的政策为例。其他期刊的要求可能不同，**以目标期刊的最新政策为准**。

### 数据和代码要能复现

- **接收前交复现包。** 含实证、模拟或实验的论文，在接收前必须提供足以复现结果的数据、代码和计算细节，存放在公开可访问的可信数据仓库中[^aea2026data-e1]。AEA 数据编辑会做可复现性检查[^aea2026data-e3]。
- **数据不能公开也有要求。** 要保存数据和代码至少五年、协助别人复现、公开代码、公开说明数据来源[^aea2026data-e2]。如果别人要数据还得经你本人批准，"可应要求提供"一般不被接受[^aea2026data-e4]。
- **清洗数据的程序也要交。** 即使原始数据不能提供，从原始数据生成分析数据的全部程序也必须提供[^aea2026data-e5]。
- **写好 README，最好有总脚本。** 复现包顶层放 PDF 格式的 README，写明复现全部结果的所有步骤[^aea2026data-e7]；强烈建议提供一个一键运行全部分析的总脚本[^aea2026data-e6]。
- **实验和问卷要交原始材料。** 投稿时就要附上完整的实验说明或问卷原文[^aea2026data-e10]。

这些要求最好从项目第一天就照着做，而不是投稿时再补 `[本项目分析]`。整理数据和代码的通用做法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。

### 田野实验要登记；预分析计划

- **田野实验必须登记。** AEA 期刊要求所有田野实验在投稿前，到 AEA 的随机对照试验（randomized controlled trial，RCT）注册平台登记；实验室实验目前不要求[^aea2026rct-e1][^aea2026data-e9]。
- **越早越好。** 试验的任何阶段都可以登记，但鼓励尽早[^aea2026rct-e1]；在干预开始前登记的，会被标为"预注册"[^aea2026rct-e5]。
- **登记内容。** 必填项包括结果变量、实验设计和计划样本量等[^aea2026rct-e4]。登记免费，之后可以修改，修改历史会被保留[^aea2026rct-e2]。正在调查时，部分字段可以先隐藏，以免影响受访者[^aea2026rct-e3]。
- **登记审核不等于质量或伦理审查。** 平台的审核不评判研究质量和伦理[^aea2026rct-e6]。

**预分析计划**（pre-analysis plan）是在看数据之前，精确写下要做哪些分析：用哪些变量、怎样清洗数据、跑哪些回归[^olken2015promises-e1]。它比上面的登记写得更细 `[本项目分析]`。下面几句只依据 Olken 2015 文章页上公开的摘要，本文没有读到全文：如果事先写定回归、并报告所有写定的结果，"数据挖掘"（反复试分析、只挑好看的结果）问题会大大减少[^olken2015promises-e2]；但这种计划也有局限和成本，Olken 认为在很多情形下它的好处可能没有最初设想的那么大[^olken2015promises-e3]；他的讨论主要针对随机对照试验[^olken2015promises-e4]。探索性分析和验证性分析的区别见第二部分的[从研究问题到证据清单](../../02_do-the-project/01_question-to-evidence.md#5-分清你是在检验还是在探索)。

### 利益披露

- 每篇投稿都要说明资金来源，没有也要写明[^aea2026disclosure-e1]。
- 每位作者要披露过去三年从利益相关方获得的累计至少一万美元的资助，包括提供数据访问这类非现金支持[^aea2026disclosure-e2]。
- 有其他方有权在论文发布前审阅论文的，要披露[^aea2026disclosure-e3]。这一点和用企业、政府数据的研究尤其相关 `[本项目分析]`。
- 每位作者单独提交一份"披露声明"[^aea2026disclosure-e4]；收集人类受试者数据的，要说明是否获得伦理审查委员会批准，没有的要说明原因[^aea2026disclosure-e5]。投稿时没披露，可能导致撤销录用[^aea2026disclosure-e6]。

---

## 常用套路与证据标准

**研究套路**指一个项目主要靠什么逻辑产生新知识，见[核心术语](../../00_start-here/key-concepts.md#研究套路)和[研究套路](../../05_research-strategies/README.md)。经济学实证研究的主流是解释因果，下表前两行是拿到因果证据的两种途径；第三行是理论建模；最后两行是结构估计和校准，它们靠经济模型做定量推断。表的分组和"在经济学里的样子"一栏是本项目的归纳；"证据和评判标准"一栏的每条只代表脚注里那份资料（多为 AEA 期刊 2026 年版的政策和几位经济学者的文章），不是整个学科的规定 `[本项目分析]`。

| 套路 | 在经济学里的样子 | 常用证据和评判标准 | 具体做法 |
|---|---|---|---|
| [解释因果](../../05_research-strategies/explain_causality.md)（随机实验） | 随机决定谁接受干预，如发现金、给补贴 `[本项目分析]`；耗时、昂贵，有时做不了[^angrist2010credibility-e3] | AEA 期刊：田野实验投稿前登记[^aea2026rct-e1]，干预开始前登记才算"预注册"[^aea2026rct-e5]；实验说明随稿提交[^aea2026data-e10] | [田野实验](../../06_methods/field_experiment.md) |
| [解释因果](../../05_research-strategies/explain_causality.md)（准实验） | 借制度或自然事件造成的变化；最常用工具变量、断点回归、双重差分[^angrist2010credibility-e4] | 先说清识别策略[^angrist2010credibility-e10]，按方法逐项查漏洞，见上文[可信性革命](#可信性革命先回答你的识别策略是什么)；AEA 期刊要求接收前交复现包[^aea2026data-e1] | [准实验与因果识别](../../06_methods/quasi_experiment.md) |
| [证明](../../05_research-strategies/prove.md)（理论建模） | 写出行为人、目标、约束和均衡[^varian1997build-e4]，从模型推出结论 `[本项目分析]` | Varian 建议先写最简单、仍有意思的模型[^varian1997build-e5]，再推广，看结论有多一般[^varian1997build-e6]。罗切斯特大学的 Thomson 1999 年在《经济文献杂志》（Journal of Economic Literature）上写给博士生的理论论文写作指南，建议讲清结果有意思、前人没做过[^thomson1999young-e1]，并逐个检查定理里的假设能不能去掉[^thomson1999young-e2]。计量经济学会（Econometric Society）的理论期刊 Theoretical Economics 的审稿人指南（2026 年 10 月查阅的网页版本，网页未注日期）：篇幅本身是评判标准之一[^te2026guidelines-e1]，审稿人要说明哪些结果该删、结果不那么一般时证明能否更短[^te2026guidelines-e2]，只要求必不可少的扩展[^te2026guidelines-e3]。贡献要多大才够发表，本文资料未涉及 | 计算机篇的[理论研究](../computer-science/practices/theoretical_research.md)可参考 |
| [解释因果](../../05_research-strategies/explain_causality.md)（结构估计） | 估计一个经济模型的参数，再用它分析没实施过的政策（见表后）；例如兼并分析[^angrist2010credibility-e21] | Low 和 Meghir 2017：写清推断依赖哪些假设，这是结构模型的价值所在[^low2017use-e3]；估计后报告标准误，说明每个参数由数据的哪个统计特征确定[^low2017use-e4]，再拿其他数据特征或简约式结果检验模型，最好是估计时没用到的[^low2017use-e5]。AEA 期刊：估计和模拟的程序都放进复现包[^aea2026data-e11] | 目前没有对应文档 |
| [解释因果](../../05_research-strategies/explain_causality.md)（校准与计算实验） | 建一个模型经济，调参数让它在几个关键统计特征上像真实经济，再改政策参数看结果[^angrist2010credibility-e14] | 报告参数有多不确定、结果对模型设定有多敏感（见表后）；模拟程序放进复现包[^aea2026data-e11] | [定量仿真](../../06_methods/simulation_study.md)（以计算机为例） |

"结构估计"和"校准"两行的说明。下面和后面"两派的分歧"里引的 Nevo 和 Whinston、Low 和 Meghir、Keane、Kydland 和 Prescott、Hansen 和 Heckman 五篇文章，都发表在《经济学展望杂志》（Journal of Economic Perspectives）。Low 和 Meghir 一篇读了全文（伦敦大学学院机构库保存的期刊版本）；其余四篇只读了美国经济学会网站上的摘要，所以只转述摘要里作者的说法：

- **结构估计**：按 Nevo 和 Whinston 的说法，结构建模用数据去识别一个经济模型的参数，这个模型建立在个人选择之上[^nevo2010taking-e1]。Low 和 Meghir 认为，结构模型能找出决定结果的机制，并用来分析没有实施过的政策[^low2017use-e2]。
- **校准与计算实验**：据 Angrist 和 Pischke 2010 年的描述，很多宏观经济学家用这种做法[^angrist2010credibility-e14]。Kydland 和 Prescott 认为，在整个国家的层面拿真人做实验不可行，但可以建一个模型经济，算出模型里的人会怎样行动[^kydland1996computational-e1]，用来回答一个提得清楚的定量问题[^kydland1996computational-e2]。Hansen 和 Heckman 质疑校准所需的微观估计并不是现成的[^hansen1996empirical-e1]，主张常规报告参数有多不确定、结果对模型设定有多敏感[^hansen1996empirical-e2]。

**两派的分歧会影响你怎样设计研究**，所以这里把两边并列：

- **设计派**：Angrist 和 Pischke 更信服好的研究设计得出的结果，而不是好理论推出的结论[^angrist2010credibility-e19]；结构估计应该和假设更弱的方法得到的结果对得上[^angrist2010credibility-e15]；校准能说明模型的含义，但不直接提供因果效应的证据[^angrist2010credibility-e14]。
- **结构派**：Low 和 Meghir 认为，结构模型的主要好处，是能超出只给出简约式因果关系的常规研究[^low2017use-e1]。Nevo 和 Whinston 认为，可信的分析可以是结构的，也可以是非结构的，对某些问题结构分析有重要优势[^nevo2010taking-e2]。Keane 认为，统计工作摆脱不了假设，结论总是有条件的[^keane2010structural-e1]；能做对照实验，也不等于不需要理论[^keane2010structural-e3]。

怎么用这张表 `[本项目分析]`：

- **前两行共同的追问是识别**：这个数字靠什么假设才成立。效应在经济上有多大，也要单独讲清，不能只报显著性[^cochrane2005writing-e7]。
- **结构估计和校准放在解释因果下，是本项目的归类。** 它们的核心主张常是"某项政策会带来多大影响"，但这类结论主要靠模型假设，不像前两行那样靠研究设计。
- **用了模型，就把模型当成证据的一部分交出来。** 说清模型假设了什么、参数从哪来、结论对假设有多敏感，求解和模拟的代码一起交[^aea2026data-e11]。

## 本学科常用的研究方法

跨学科的研究类型和经济学的对应如下；对应关系和差异说明是本项目的归纳 `[本项目分析]`：

- **田野实验**见[田野实验](../../06_methods/field_experiment.md)，**实验室实验**的通用流程见[对照实验](../../06_methods/controlled_experiment.md)。
- **用观察数据做因果推断**见[准实验与因果识别](../../06_methods/quasi_experiment.md)，数据处理见[数据科学](../../06_methods/data_science.md)。经济学这里的核心追问是识别策略[^angrist2010credibility-e10]。
- **理论建模**和**结构估计**目前没有对应的方法文档，评判标准见上文[常用套路与证据标准](#常用套路与证据标准)；理论建模可参考计算机篇的[理论研究](../computer-science/practices/theoretical_research.md)。**校准与计算实验**可参考[定量仿真](../../06_methods/simulation_study.md)，那篇的例子以计算机为主。
- **问卷调查**见[问卷调查](../../06_methods/questionnaire_survey.md)，AEA 期刊要求随稿提交问卷原文[^aea2026data-e10]。**复现研究**见[复现研究](../../06_methods/replication.md)。**元研究**（例如统计顶级期刊上 p 值的分布[^brodeur2016star-e2]）见[方法论研究与元科学](../../06_methods/meta_science.md)。

---

## 给新手的建议

1. **动手之前，先写下识别策略。** 用一两句话回答：是什么经济机制让我的解释变量发生了变化[^cochrane2005writing-e5]？凭什么认为这种变化和其他影响结果的因素无关？答不上来，先别急着跑回归 `[本项目分析]`。
2. **按方法逐项检查漏洞。** 双重差分看两组是否各有不同的趋势，断点回归看分界线附近有没有扎堆，工具变量看有没有别的渠道[^angrist2010credibility-e9]。
3. **先发工作论文，同时做好"慢"的准备。** 据 2000 年前后的统计，顶级期刊审稿和修改平均要两年左右[^ellison2002slowdown-e1]。做时间计划时把这一点算进去 `[本项目分析]`。
4. **多讲，讲完就记。** 报告逼你直奔重点[^varian1997build-e7]；每次讲完马上记下听众的问题和建议[^varian1997build-e8]。
5. **把求职论文当作博士阶段最重要的一件事。** 争取在求职那年的夏末前完成[^cawley2018guide-e3]，和同届同学组织讨论会反复练讲[^cawley2018guide-e4]。
6. **从第一天起按复现包的标准整理。** 清洗和分析都写成程序，最后能一键重跑[^aea2026data-e5][^aea2026data-e6]；原始数据只读，见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md#2-原始数据只读其余都能重新生成)。目标是同学只凭论文和附录就能复现每个数字[^cochrane2005writing-e3]。
7. **做田野实验，干预开始前就登记。** 在干预开始前登记才算"预注册"[^aea2026rct-e5]；想清楚要不要写更详细的预分析计划[^olken2015promises-e3]。
8. **合著时把贡献说清楚。** 署名按字母顺序，看不出谁做了什么[^einav2006surname-e1]；分工和功劳的处理见贯穿全程的[合作与导师](../../08_throughout/collaboration_and_advisors.md#6-署名开工时就谈并随进展调整) `[本项目分析]`。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 试遍各种回归设定，只报告显著的那个（叫"设定搜索"或 p-hacking。p 值是：假如其实没有效应，仅凭偶然得到至少这么极端结果的概率；0.05 常被当作"显著"的门槛 `[本项目分析]`） | Brodeur 等人统计了 2005–2011 年 AER、JPE、QJE 三本期刊上的约五万个检验（2013 年讨论稿版），发现刚好低于 0.05 的 p 值偏多；作者的解释是，结果差一点显著时，研究者可能会去挑一个"显著"的设定[^brodeur2016star-e2][^brodeur2016star-e3]。撒大网式地跑大量回归，不能为因果解释提供多少依据[^angrist2010credibility-e13] |
| 只报告统计显著性，不讲效应有多大 | 样本很大时，再小的效应也会显著[^cochrane2005writing-e7] |
| 把所有能想到的变量都放进回归当控制 | Cochrane 认为多数论文放的解释变量太多了[^cochrane2005writing-e6]；有些变量本身就是结果的一部分，控制它会把要估的效应也控制掉 `[本项目分析]` |
| 只声称工具变量"与其他影响因素无关"，不论证它为什么成立 | 工具变量的假设必须充分论证[^angrist2010credibility-e5] |
| 报告前二十分钟都在铺垫和讲文献 | 研讨会上直接讲重点[^cochrane2005writing-e8]；听众插话会把时间耗光[^cochrane2005writing-e12] |
| 写"数据可应要求提供"就算公开 | 如果索取要经作者本人批准，一般不被接受[^aea2026data-e4] |
| 田野实验做完才想起登记 | AEA 期刊要求投稿前登记，并鼓励尽早[^aea2026rct-e1]；干预开始后才登记，就不算预注册[^aea2026rct-e5] |
| 漏报资助或数据提供方的审阅权 | 投稿时未披露，可能导致撤销录用[^aea2026disclosure-e6] |
| 只盯五大期刊，用发表在哪里评判研究的价值 | Heckman 和 Moktan 发现，相当一部分有影响的论文发表在五大之外[^heckman2020tyranny-e2] |

---

## 延伸阅读

- **Angrist & Pischke 2010，The Credibility Revolution in Empirical Economics**：讲清以研究设计为本的实证方法从何而来、几种方法各检查什么，以及对它的批评和回应。想了解"识别"为什么这么重要时读。
- **Cochrane 2005，Writing Tips for Ph.D. Students**：篇幅短，涵盖论文结构、实证识别的自问清单和研讨会报告。写第一篇论文前读。
- **Varian 1997，How to Build an Economic Model in Your Spare Time**：从找想法、简化模型到做报告，讲一位理论经济学家怎样工作。做理论或者想学建模时读。
- **AEA Data and Code Availability Policy**：复现包的具体要求和 README 应包含的内容。开始整理数据和代码前读。
- **AEA RCT Registry 的说明和注册指南**：要做田野实验时读。
- **Cawley，A Guide and Advice for Economists on the U.S. Junior Academic Job Market**：美国经济学学术求职的流程和建议。本文用的是 2018–19 版；准备求职前一年，找最新的版本读。
- **Card & DellaVigna 2013、Heckman & Moktan 2020**：五大期刊的数据和争论（本文读的是工作论文或讨论稿版）。想了解发表压力从何而来时读。

[^varian1997build-e4]: Varian 1997，§1.4 Building your model。[证据](../../../sources/notes/varian1997build.md#e4)
[^varian1997build-e5]: Varian 1997，§1.4 Building your model。[证据](../../../sources/notes/varian1997build.md#e5)
[^varian1997build-e6]: Varian 1997，§1.6 Making mistakes。[证据](../../../sources/notes/varian1997build.md#e6)
[^varian1997build-e7]: Varian 1997，§1.8 Giving a seminar。[证据](../../../sources/notes/varian1997build.md#e7)
[^varian1997build-e8]: Varian 1997，§1.8 Giving a seminar。[证据](../../../sources/notes/varian1997build.md#e8)
[^varian1997build-e9]: Varian 1997，§1.11 When to stop。[证据](../../../sources/notes/varian1997build.md#e9)
[^varian1997build-e10]: Varian 1997，§1.8 Giving a seminar。[证据](../../../sources/notes/varian1997build.md#e10)
[^thomson1999young-e1]: Thomson 1999，§2 General Principles，第 159 页。[证据](../../../sources/notes/thomson1999young.md#e1)
[^thomson1999young-e2]: Thomson 1999，§5 Writing Proofs，第 177 页。[证据](../../../sources/notes/thomson1999young.md#e2)
[^te2026guidelines-e1]: Theoretical Economics 审稿人指南（2026 年 10 月查看），The opinion。[证据](../../../sources/notes/te2026guidelines.md#e1)
[^te2026guidelines-e2]: Theoretical Economics 审稿人指南（2026 年 10 月查看），Substantive comments。[证据](../../../sources/notes/te2026guidelines.md#e2)
[^te2026guidelines-e3]: Theoretical Economics 审稿人指南（2026 年 10 月查看），Substantive comments。[证据](../../../sources/notes/te2026guidelines.md#e3)
[^angrist2010credibility-e1]: Angrist & Pischke 2010，摘要。[证据](../../../sources/notes/angrist2010credibility.md#e1)
[^angrist2010credibility-e2]: Angrist & Pischke 2010，摘要。[证据](../../../sources/notes/angrist2010credibility.md#e2)
[^angrist2010credibility-e3]: Angrist & Pischke 2010，引言。[证据](../../../sources/notes/angrist2010credibility.md#e3)
[^angrist2010credibility-e4]: Angrist & Pischke 2010，Better Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e4)
[^angrist2010credibility-e5]: Angrist & Pischke 2010，Better Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e5)
[^angrist2010credibility-e6]: Angrist & Pischke 2010，Better Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e6)
[^angrist2010credibility-e7]: Angrist & Pischke 2010，Better Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e7)
[^angrist2010credibility-e8]: Angrist & Pischke 2010，Better Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e8)
[^angrist2010credibility-e9]: Angrist & Pischke 2010，Whither Sensitivity Analysis?。[证据](../../../sources/notes/angrist2010credibility.md#e9)
[^angrist2010credibility-e10]: Angrist & Pischke 2010，More Transparent Discussion of Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e10)
[^angrist2010credibility-e11]: Angrist & Pischke 2010，More Transparent Discussion of Research Design。[证据](../../../sources/notes/angrist2010credibility.md#e11)
[^angrist2010credibility-e13]: Angrist & Pischke 2010，Whither Sensitivity Analysis?。[证据](../../../sources/notes/angrist2010credibility.md#e13)
[^angrist2010credibility-e14]: Angrist & Pischke 2010，Mad About Macro。[证据](../../../sources/notes/angrist2010credibility.md#e14)
[^angrist2010credibility-e15]: Angrist & Pischke 2010，Industrial Disorganization。[证据](../../../sources/notes/angrist2010credibility.md#e15)
[^angrist2010credibility-e16]: Angrist & Pischke 2010，Has the Research Design Pendulum Swung Too Far?。[证据](../../../sources/notes/angrist2010credibility.md#e16)
[^angrist2010credibility-e17]: Angrist & Pischke 2010，External Validity。[证据](../../../sources/notes/angrist2010credibility.md#e17)
[^angrist2010credibility-e19]: Angrist & Pischke 2010，Industrial Disorganization。[证据](../../../sources/notes/angrist2010credibility.md#e19)
[^angrist2010credibility-e20]: Angrist & Pischke 2010，External Validity。[证据](../../../sources/notes/angrist2010credibility.md#e20)
[^angrist2010credibility-e21]: Angrist & Pischke 2010，Industrial Disorganization。[证据](../../../sources/notes/angrist2010credibility.md#e21)
[^angrist2010credibility-e18]: Angrist & Pischke 2010，Other Empirical Work in the Age of Heavy Metal。[证据](../../../sources/notes/angrist2010credibility.md#e18)
[^cochrane2005writing-e3]: Cochrane 2005，§2 Writing。[证据](../../../sources/notes/cochrane2005writing.md#e3)
[^cochrane2005writing-e4]: Cochrane 2005，§3 Tips for empirical work。[证据](../../../sources/notes/cochrane2005writing.md#e4)
[^cochrane2005writing-e5]: Cochrane 2005，§3 Tips for empirical work。[证据](../../../sources/notes/cochrane2005writing.md#e5)
[^cochrane2005writing-e6]: Cochrane 2005，§3 Tips for empirical work。[证据](../../../sources/notes/cochrane2005writing.md#e6)
[^cochrane2005writing-e7]: Cochrane 2005，§3 Tips for empirical work。[证据](../../../sources/notes/cochrane2005writing.md#e7)
[^cochrane2005writing-e8]: Cochrane 2005，§4 Seminar presentations。[证据](../../../sources/notes/cochrane2005writing.md#e8)
[^cochrane2005writing-e11]: Cochrane 2005，§1 Organization / Theory。[证据](../../../sources/notes/cochrane2005writing.md#e11)
[^cochrane2005writing-e12]: Cochrane 2005，§4 Seminar presentations。[证据](../../../sources/notes/cochrane2005writing.md#e12)
[^nberworkingpapers-e1]: NBER Working Papers 页面。[证据](../../../sources/notes/nberworkingpapers.md#e1)
[^brodeur2016star-e2]: Brodeur 等 2016，摘要（IZA 讨论稿版）。[证据](../../../sources/notes/brodeur2016star.md#e2)
[^brodeur2016star-e3]: Brodeur 等 2016，摘要（IZA 讨论稿版）。[证据](../../../sources/notes/brodeur2016star.md#e3)
[^brodeur2016star-e6]: IZA 讨论稿封二说明（见 Brodeur 等 2016 讨论稿版）。[证据](../../../sources/notes/brodeur2016star.md#e6)
[^heckman2020tyranny-e1]: Heckman & Moktan 2020，摘要（IZA 讨论稿版）。[证据](../../../sources/notes/heckman2020tyranny.md#e1)
[^heckman2020tyranny-e2]: Heckman & Moktan 2020，摘要（IZA 讨论稿版）。[证据](../../../sources/notes/heckman2020tyranny.md#e2)
[^heckman2020tyranny-e3]: Heckman & Moktan 2020，§1 Introduction（IZA 讨论稿版）。[证据](../../../sources/notes/heckman2020tyranny.md#e3)
[^heckman2020tyranny-e4]: Heckman & Moktan 2020，§1 Introduction（IZA 讨论稿版）。[证据](../../../sources/notes/heckman2020tyranny.md#e4)
[^ellison2002slowdown-e1]: Ellison 2002，§1 Introduction（NBER 工作论文版）。[证据](../../../sources/notes/ellison2002slowdown.md#e1)
[^ellison2002slowdown-e2]: Ellison 2002，§2（NBER 工作论文版）。[证据](../../../sources/notes/ellison2002slowdown.md#e2)
[^card2013nine-e1]: Card & DellaVigna 2013，§1 Introduction（NBER 工作论文版）。[证据](../../../sources/notes/card2013nine.md#e1)
[^card2013nine-e2]: Card & DellaVigna 2013，§1 Introduction（NBER 工作论文版）。[证据](../../../sources/notes/card2013nine.md#e2)
[^card2013nine-e3]: Card & DellaVigna 2013，§1 Introduction（NBER 工作论文版）。[证据](../../../sources/notes/card2013nine.md#e3)
[^cawley2018guide-e1]: Cawley 2018，Introduction。[证据](../../../sources/notes/cawley2018guide.md#e1)
[^cawley2018guide-e2]: Cawley 2018，Introduction。[证据](../../../sources/notes/cawley2018guide.md#e2)
[^cawley2018guide-e3]: Cawley 2018，Preparing to Go on the Job Market。[证据](../../../sources/notes/cawley2018guide.md#e3)
[^cawley2018guide-e4]: Cawley 2018，Preparing to Go on the Job Market。[证据](../../../sources/notes/cawley2018guide.md#e4)
[^cawley2018guide-e5]: Cawley 2018，Interviewing at the ASSA Meetings。[证据](../../../sources/notes/cawley2018guide.md#e5)
[^cawley2018guide-e6]: Cawley 2018，Interviewing at the ASSA Meetings。[证据](../../../sources/notes/cawley2018guide.md#e6)
[^cawley2018guide-e7]: Cawley 2018，Applying for Academic Jobs。[证据](../../../sources/notes/cawley2018guide.md#e7)
[^einav2006surname-e1]: Einav & Yariv 2006，第 175 页。[证据](../../../sources/notes/einav2006surname.md#e1)
[^einav2006surname-e2]: Einav & Yariv 2006，第 175 页。[证据](../../../sources/notes/einav2006surname.md#e2)
[^einav2006surname-e3]: Einav & Yariv 2006，第 182 页脚注 8；第 175 页。[证据](../../../sources/notes/einav2006surname.md#e3)
[^einav2006surname-e4]: Einav & Yariv 2006，第 184 页。[证据](../../../sources/notes/einav2006surname.md#e4)
[^aea2026data-e1]: AEA Data and Code Availability Policy（2026 年 2 月版），开头。[证据](../../../sources/notes/aea2026data.md#e1)
[^aea2026data-e2]: AEA Data and Code Availability Policy，开头。[证据](../../../sources/notes/aea2026data.md#e2)
[^aea2026data-e3]: AEA Data and Code Availability Policy，开头。[证据](../../../sources/notes/aea2026data.md#e3)
[^aea2026data-e4]: AEA Data and Code Availability Policy，Non-Public Data。[证据](../../../sources/notes/aea2026data.md#e4)
[^aea2026data-e5]: AEA Data and Code Availability Policy，数据与代码可得性标准（Data and Code Availability Standard，DCAS）第 7 条。[证据](../../../sources/notes/aea2026data.md#e5)
[^aea2026data-e6]: AEA Data and Code Availability Policy，Computer Code。[证据](../../../sources/notes/aea2026data.md#e6)
[^aea2026data-e7]: AEA Data and Code Availability Policy，数据与代码可得性标准（DCAS）第 13 条。[证据](../../../sources/notes/aea2026data.md#e7)
[^aea2026data-e9]: AEA Data and Code Availability Policy，数据与代码可得性标准（DCAS）第 12 条。[证据](../../../sources/notes/aea2026data.md#e9)
[^aea2026data-e10]: AEA Policy for Papers Conducting Experiments and Collecting Primary Data，Original Instructions。[证据](../../../sources/notes/aea2026data.md#e10)
[^aea2026rct-e1]: About the AEA RCT Registry。[证据](../../../sources/notes/aea2026rct.md#e1)
[^aea2026rct-e2]: About the AEA RCT Registry。[证据](../../../sources/notes/aea2026rct.md#e2)
[^aea2026rct-e3]: About the AEA RCT Registry。[证据](../../../sources/notes/aea2026rct.md#e3)
[^aea2026rct-e4]: AEA RCT Registry 注册指南，Required Information。[证据](../../../sources/notes/aea2026rct.md#e4)
[^aea2026rct-e5]: AEA RCT Registry 注册指南。[证据](../../../sources/notes/aea2026rct.md#e5)
[^aea2026rct-e6]: AEA RCT Registry 注册指南，Registration Review Criteria。[证据](../../../sources/notes/aea2026rct.md#e6)
[^olken2015promises-e1]: Olken 2015，摘要。[证据](../../../sources/notes/olken2015promises.md#e1)
[^olken2015promises-e2]: Olken 2015，摘要。[证据](../../../sources/notes/olken2015promises.md#e2)
[^olken2015promises-e3]: Olken 2015，摘要。[证据](../../../sources/notes/olken2015promises.md#e3)
[^olken2015promises-e4]: Olken 2015，摘要。[证据](../../../sources/notes/olken2015promises.md#e4)
[^aea2026disclosure-e1]: AEA Disclosure Policy，Disclosure Principles。[证据](../../../sources/notes/aea2026disclosure.md#e1)
[^aea2026disclosure-e2]: AEA Disclosure Policy，Disclosure Principles。[证据](../../../sources/notes/aea2026disclosure.md#e2)
[^aea2026disclosure-e3]: AEA Disclosure Policy，Disclosure Principles。[证据](../../../sources/notes/aea2026disclosure.md#e3)
[^aea2026disclosure-e4]: AEA Disclosure Policy，Instructions。[证据](../../../sources/notes/aea2026disclosure.md#e4)
[^aea2026disclosure-e5]: AEA Disclosure Policy，IRB Approval。[证据](../../../sources/notes/aea2026disclosure.md#e5)
[^aea2026disclosure-e6]: AEA Disclosure Policy，Instructions。[证据](../../../sources/notes/aea2026disclosure.md#e6)
[^aea2026data-e11]: AEA Data and Code Availability Policy，Code for Analysis（数据与代码可得性标准第 8 条）。[证据](../../../sources/notes/aea2026data.md#e11)
[^nevo2010taking-e1]: Nevo & Whinston 2010，摘要（只读了摘要）。[证据](../../../sources/notes/nevo2010taking.md#e1)
[^nevo2010taking-e2]: Nevo & Whinston 2010，摘要（只读了摘要）。[证据](../../../sources/notes/nevo2010taking.md#e2)
[^low2017use-e1]: Low & Meghir 2017，摘要。[证据](../../../sources/notes/low2017use.md#e1)
[^low2017use-e2]: Low & Meghir 2017，摘要。[证据](../../../sources/notes/low2017use.md#e2)
[^low2017use-e3]: Low & Meghir 2017，引言，第 33 页。[证据](../../../sources/notes/low2017use.md#e3)
[^low2017use-e4]: Low & Meghir 2017，Standard Errors and Post-Estimation Checks，第 53 页。[证据](../../../sources/notes/low2017use.md#e4)
[^low2017use-e5]: Low & Meghir 2017，Standard Errors and Post-Estimation Checks，第 53 页。[证据](../../../sources/notes/low2017use.md#e5)
[^keane2010structural-e1]: Keane 2010，摘要（只读了摘要）。[证据](../../../sources/notes/keane2010structural.md#e1)
[^keane2010structural-e3]: Keane 2010，摘要（只读了摘要）。[证据](../../../sources/notes/keane2010structural.md#e3)
[^kydland1996computational-e1]: Kydland & Prescott 1996，摘要（只读了摘要）。[证据](../../../sources/notes/kydland1996computational.md#e1)
[^kydland1996computational-e2]: Kydland & Prescott 1996，摘要（只读了摘要）。[证据](../../../sources/notes/kydland1996computational.md#e2)
[^hansen1996empirical-e1]: Hansen & Heckman 1996，摘要（只读了摘要）。[证据](../../../sources/notes/hansen1996empirical.md#e1)
[^hansen1996empirical-e2]: Hansen & Heckman 1996，摘要（只读了摘要）。[证据](../../../sources/notes/hansen1996empirical.md#e2)
