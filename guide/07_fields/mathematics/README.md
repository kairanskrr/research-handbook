# 数学：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲数学研究实际怎样运转：成果是证明，合作规模小、按字母署名，以期刊为主、发表慢，arXiv 预印本，以及导师、选题、讨论班在其中的作用。各学科共通的做法（选题、做计划、写作、审稿、科研伦理）见[通用篇](../../README.md)，这里不重复。**怎样写证明、怎样检查自己的证明**，计算机篇的[理论研究](../computer-science/practices/theoretical_research.md)已经讲过（标〔数学通用〕的部分都适用于数学），本文也不重复。

**读完本文，你应该能：**

- 说清数学论文从想法到发表要经过哪些环节，为什么慢；
- 理解按字母署名、arXiv 预印本、匿名审稿在数学里的含义；
- 知道怎样和导师相处、怎样选第一个问题、怎样用讨论班和文献学习；
- 避开新手在署名、宣布结果、投稿上最常犯的错误。

---

## 本领域研究怎样运转

### 成果是证明，目的是理解

数学论文的核心是定理和证明 `[本项目分析]`。但在 Thurston（William Thurston，数学家）看来，证明不是全部目的。他认为，数学家在做的事，根本上是找到让人理解和思考数学的方法[^thurston1994proof-e1]。计算机证明四色定理引起争议，反映的就是：人们除了想知道定理成立，还想理解证明[^thurston1994proof-e2]。

证明靠什么保证正确？Thurston 的看法是：人不太擅长逐条检查形式正确性，但很擅长发现证明的薄弱处[^thurston1994proof-e9]；数学结果的可靠性主要来自数学家仔细、批判地思考其中的想法[^thurston1994proof-e11]。所以他主张把证明写得清楚、尽量简单，让薄弱处容易被发现[^thurston1994proof-e10]。具体写法见[理论研究](../computer-science/practices/theoretical_research.md#第-3-步把证明写得可以检查-数学通用)。

### 一个人或几个人做，按字母署名

美国数学会（American Mathematical Society，AMS）2004 年专门发过一份声明，解释数学的合作文化：

- 在数学的大多数领域，合作是想法和技能的共享，无法拆开归到个人；角色也很少像实验科学那样分工[^amsculture2004joint-e1]。想法是在所有合作者的讨论中长出来的，区分"谁贡献了哪个想法"往往没有意义[^amsculture2004joint-e7]。
- 合作几乎总是少数几个人，平等地贡献[^amsculture2004joint-e2]。
- 因此，数学家传统上**按姓氏字母顺序**排作者[^amsculture2004joint-e3]。声明引用的统计：在至少有一位美国作者的期刊论文里，近一半是合著，其中超过 75% 按字母排序；纯数学合著论文超过 90% 按字母排序[^amsculture2004joint-e4]。
- 其他学科的人常误解这一点，有时对年轻数学家不利，尤其是姓氏字母靠后的人[^amsculture2004joint-e6]。

按字母排序不等于"挂名无所谓"。AMS 伦理准则要求：每个署名作者都要对内容有实质贡献，每个有实质贡献的人都应有机会署名[^ams2022ethical-e5]。

"一个人做"也不等于闭门造车。Thurston 强调，数学研究的社会环境极其重要[^thurston1994proof-e12]；证明定理的人是在数学共同体里做到的，不是独自完成的[^thurston1994proof-e14]。

### 期刊为主，发表慢，发得少

AMS 2006 年的另一份声明说明了数学的发表习惯：

- 和一些其他科学相比，数学家发表得不多；大部分研究发表在有审稿的期刊上，而不是会议论文集或书[^amsculture2006rates-e1]。2001–2005 年《数学评论》（Mathematical Reviews，一种数学文献索引）收录的条目里，80% 来自有审稿的期刊[^amsculture2006rates-e5]。
- 一篇论文通常是对一个问题的成熟论述，数学研究也不被认为有时效性，所以**发表延迟很常见**[^amsculture2006rates-e2]。陶哲轩（Terence Tao，数学家）说，从发预印本到正式发表，间隔以"年"计[^taocareer-e28]。
- 发得少不代表差。2005–2006 年获斯隆研究奖的 40 位数学家中，70% 在获奖前五年平均每年发表不超过两篇[^amsculture2006rates-e3]。评价大多数数学家的工作，关键看论文质量而不是速度[^amsculture2006rates-e4]。

一家期刊从投稿到接收要多久，本文没有可靠的统一数字。投稿前查目标期刊公布的数据，或问导师 `[本项目分析]`。AMS 伦理准则提出，发表的文章应注明最初投稿日期和修改日期[^ams2022ethical-e11]，翻一翻目标期刊近期的文章，就能大致看出它从投稿到接收要多久 `[本项目分析]`。

### 一篇论文的一生

下表是一般流程 `[本项目分析]`，各环节的依据见右栏：

| 环节 | 发生什么 | 注意 |
|---|---|---|
| 想法与部分结果 | 一个问题常常要几个月才有像样的进展[^taocareer-e34] | 部分进展本身有价值[^taocareer-e6] |
| 讨论与报告 | 在讨论班上讲、和同行当面讨论 | 当面交流能传达的，远多于正式的数学语言[^thurston1994proof-e5] |
| 写成完整论文 | 写出所有细节 | 写法见[理论研究](../computer-science/practices/theoretical_research.md) |
| 发预印本 | 放到 arXiv 上公开 | 达不到发表质量前，先别宣布[^taocareer-e30] |
| 投期刊 | 选合适的期刊 | 勉强够格就投顶刊，可能流程漫长、最后被拒[^taowriting-e17] |
| 审稿与修改 | 匿名审稿人审读，编辑决定 | 编辑只在合理确信正确时才接收[^ams2022ethical-e9] |
| 正式发表 | 常在预印本公开之后很久 | 间隔以年计[^taocareer-e28] |

### arXiv 预印本

**预印本**是正式发表前公开的论文版本。arXiv 是一个预印本网站，稿件按研究方向分类[^arxivmoderation-e2]。

- **为什么要发**：正式发表要等好几年，预印本让别人现在就能读到[^taocareer-e28]；arXiv 有可靠的时间戳，能确立优先权，也就是证明这个结果是你先做出来的[^taocareer-e29]。
- **什么时候公开**：手里只有达不到发表质量的草稿时，最好先别宣布结果[^taocareer-e30]。
- **第一次投稿要"背书"**（endorsement，即请别人为你担保）[^arxivendorsement-e1]。研究生找导师，或本单位同方向、在 arXiv 上活跃的老师最合适[^arxivendorsement-e2]。不要群发邮件找人，也不要反复催[^arxivendorsement-e3]。
- **arXiv 的审核不是同行评审**，审核员不会给你修改意见[^arxivmoderation-e1]，但会把稿件调整到最相关的分类[^arxivmoderation-e2]。课程作业、研究计划这类没有原创研究的稿件可能被拒[^arxivmoderation-e3]。所以"上了 arXiv"不等于"被认可" `[本项目分析]`。
- **要不要把预印本发给专家**：陶哲轩只在预印本确实和对方直接相关时才这样做，例如解决了对方提出的猜想[^taocareer-e31]。

### 审稿：匿名、保密、看正确性

数学期刊的审稿人（referee）要做的事，AMS 伦理准则有明确要求：

- 审稿人是匿名的，除非事先另有说明[^ams2022ethical-e8]。
- 编辑和审稿人对稿件保密，**不能把稿件里的想法据为己有**[^ams2022ethical-e10]。
- 有利益冲突（例如稿件涉及你自己、同事或学生的研究）时，应退出[^ams2022ethical-e7]。
- 编辑按投稿时的知识状态评判，只在合理确信论文正确时才接收[^ams2022ethical-e9]。

作为作者，要让审稿人容易检查。陶哲轩建议，判断论文该投什么级别的期刊时，先问自己：论文是否写得让人容易检查论证正确[^taowriting-e19]。投稿前也查一下期刊编委会里有没有懂你方向的人[^taowriting-e18]。一般审稿流程和怎样当审稿人，见通用篇的[审稿、回复审稿意见与发表](../../04_write-and-publish/02_venue-and-submission.md)。

### 导师和选题

- **导师是最好的指导来源之一**。导师不只帮你做课题，还会把你引向相关的人、会议、文献、开放问题，以及圈内流传但没写下来的知识[^taocareer-e23]。
- **别躲着导师**。主动躲着导师（或反过来）是很坏的信号[^taocareer-e24]。导师没空，就定期找至少一位别的数学家讨论，最好是有经验的[^taocareer-e25]。
- **也别完全依赖导师**。毕业后主要靠自己做数学[^taocareer-e26]；AMS 伦理准则也写明，数学博士学位证明的既是数学知识，也是在数学上的独立成就[^ams2022ethical-e12]。陶哲轩的说法是：追随数学本身，比追随某位数学家更好[^taocareer-e37]。
- **第一个问题选可行的**。著名难题几乎从不是凭空解决的[^taocareer-e13]；大部分时间花在更可行的问题上，积累经验、能力和信誉，等准备好了再去碰更大的项目[^taocareer-e14]。
- **问清出路**。AMS 伦理准则提出，指导博士生的人应向学生介绍学术界内外的就业机会[^ams2022ethical-e13]，你可以主动问 `[本项目分析]`。

一般的选题方法和导师相处，见通用篇的[选题](../../01_from-interest-to-project/02_find-problems.md)和[合作与导师](../../08_throughout/collaboration_and_advisors.md)。

### 读文献和讨论班

数学里很多东西是"听"会的，不只是"读"会的 `[本项目分析]`：

- Thurston 读研时并不明白"证明"是什么，是靠参加**讨论班**（seminar，小范围、定期的学术报告和讨论）、读论文、和其他研究生交流，慢慢明白的[^thurston1994proof-e6]。
- 同一个子领域里，一个重要证明的思路常常几分钟就能当面讲清[^thurston1994proof-e4]。当面交流能用的沟通方式，远超正式的数学语言[^thurston1994proof-e5]。
- 想知道一个领域默认哪些事实成立，Thurston 的办法是：看领域里其他论文不加证明直接引用了哪些事实、参考文献里列了什么[^thurston1994proof-e7]。
- 也去听和自己方向不直接相关的报告：知道别人在做什么、觉得什么有意思，常常给自己的工作带来新视角[^taocareer-e32]。听不懂全部很正常，学到一点就不算白听[^taocareer-e33]。Thurston 也坦言，一般的学术报告会（colloquium，面向较广听众的报告），大部分听众收获不多[^thurston1994proof-e3]。
- 跟进新文献：订阅自己方向的 arXiv 新论文通知[^taocareer-e27]；从一篇相关论文出发，往前查参考文献、往后用 MathSciNet（一个数学文献数据库）查谁引用了它[^taocareer-e36]。

一般的读文献方法见通用篇的[读文献与文献调研](../../01_from-interest-to-project/01_enter-a-field.md)。

---

## 和其他领域不同的地方

### 和计算机对照

计算机一栏的依据见[计算机领域篇](../computer-science/README.md)。

| | 数学 | 计算机（多数方向） |
|---|---|---|
| 主要发表渠道 | 有审稿的期刊[^amsculture2006rates-e1] | 会议 |
| 节奏 | 不被认为有时效性，发表延迟常见[^amsculture2006rates-e2] | 跟着会议截稿日走 |
| 合作规模 | 几乎总是少数几人[^amsculture2004joint-e2] | 从个人到大团队都有 `[本项目分析]` |
| 署名 | 传统上按字母排序[^amsculture2004joint-e3] | 本文没有找到署名顺序的资料；不要默认按字母，进组时问清 `[本项目分析]` |
| 发表数量 | 发得少，看质量[^amsculture2006rates-e4] | 见计算机领域篇 |
| 主要证据 | 证明 `[本项目分析]` | 实验和测量（理论方向除外）`[本项目分析]` |
| 预印本 | 正式发表要等几年，所以应把预印本放到网上[^taocareer-e28] | 普遍发 arXiv，但要遵守会议的匿名规则 |

### 纯数学和应用数学

两者的差别是程度上的，没有截然的界线 `[本项目分析]`。资料能支持的几点：

- **署名**：纯数学合著论文超过 90% 按字母排序[^amsculture2004joint-e4]；和其他学科联系更紧的数学方向，署名文化可能和那些学科混合[^amsculture2004joint-e5]。进组时问清本组的署名习惯 `[本项目分析]`。
- **计算**：用计算做研究的数学（数值计算、实验数学、计算机辅助证明），还要考虑计算能不能被别人重复。2012 年 ICERM（一个计算与实验数学研究所）研讨会的报告提出，要公开别人重复计算所需的全部细节，即数据和代码[^stodden2013setting-e1]。报告指出，计算工作常常没有记录实际用的代码和流程[^stodden2013setting-e2]；参会的有计算科学家和数学家，其中也有做实验数学、计算机辅助证明的纯数学家[^stodden2013setting-e3]。
- **应用数学常要和其他学科打交道**，论文的读者、期刊、评价标准可能更接近合作学科 `[本项目分析]`。

---

## 本领域的规范

本文收集的资料里，没有找到数学通用的报告规范（规定论文必须写明哪些内容的清单）或预注册要求 `[本项目分析]`。本节主要依据美国数学会公开发布的 **AMS 伦理准则**。准则自己说明，这是指导原则，不是死板的规则[^ams2022ethical-e14]。和研究直接相关的几条：

- **抄袭包括口头的**：明知是别人的发现却当作自己的，就是抄袭；书面还是口头、发表还是没发表都算[^ams2022ethical-e1]。
- **没发表的也要引用**：别人没发表的材料、网站上的材料、只宣布过的结果，都要恰当引用[^ams2022ethical-e2]。
- **不能拿"我不知道"当独立发现的理由**：已经广泛传播的结果，不能因为没读过就声称独立发现[^ams2022ethical-e6]。
- **宣布了就要及时发细节**：没有合理把握前抢先宣布，会阻碍做同一问题的人[^ams2022ethical-e3]。
- **错了就更正或撤回**[^ams2022ethical-e4]。
- **署名和审稿**：见上文"按字母署名"和"审稿"两节。

用到计算的研究，可参考 ICERM 报告的建议：对重要论断（例如计算机辅助证明一个长期未解的结果），要做严格验证，并完整公开计算细节[^stodden2013setting-e4]；符号计算的结果，最好用两个不同的软件互相核对，因为再好的软件也有缺陷[^stodden2013setting-e5]。

通用的科研诚信要求见通用篇的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md)。

---

## 常见的研究类型

| 类型 | 一句话说明 | 去哪里看 |
|---|---|---|
| 定理证明 | 证明新定理、给出反例、改进已知结果 | [理论研究](../computer-science/practices/theoretical_research.md)。标〔数学通用〕的部分都适用；"投稿：会议与期刊"一步是计算机的做法，数学以期刊为主[^amsculture2006rates-e1] |
| 计算机辅助证明、实验数学 | 用计算探索猜想，或让计算成为证明的一部分 | [理论研究](../computer-science/practices/theoretical_research.md#第-4-步检查自己的证明-数学通用机器检查部分为计算机)的机器检查部分；计算细节的公开和核对见上文"本领域的规范" |
| 数值计算与建模（应用数学） | 用数学模型和计算研究一个系统 | [定量仿真](../../06_methods/simulation_study.md)。差别：数学论文可能还要证明方法本身的性质，例如收敛性（网格或步长越细，算出的结果是否越接近真解） `[本项目分析]` |
| 综述与讲义（expository） | 把一个方向的思路讲清楚 | Thurston 认为数学家应更重视交流思考方式，不只交流定义、定理和证明[^thurston1994proof-e15]。和计算机的[综述研究](../../06_methods/review_study.md)不同：数学的综述和讲义多是作者对一个方向的梳理，不一定做系统检索 `[本项目分析]` |

---

## 给新手的建议

1. **把部分结果当成果。** 部分进展是完全解决问题的关键垫脚石[^taocareer-e6]；几个月没有明显进展并不少见[^taocareer-e35]。
2. **定期和导师说话，也找第二个人讨论。** 主动躲着导师是坏信号[^taocareer-e24]；导师没空就找另一位有经验的数学家[^taocareer-e25]。
3. **常去讨论班，也去听别的方向。** Thurston 就是靠讨论班、读论文和同学交流，才弄懂"证明"是什么的[^thurston1994proof-e6]；听不懂全部也值得[^taocareer-e33]。
4. **结果成熟了再宣布，宣布了就尽快发全文。** 先别宣布还只是草稿的结果[^taocareer-e30]；宣布后要及时发表完整细节[^ams2022ethical-e3]。
5. **投稿前找好 arXiv 背书人。** 第一次投稿需要背书[^arxivendorsement-e1]，导师是合适的人选[^arxivendorsement-e2]。
6. **按论文的实际水平选期刊。** 勉强够格就投顶刊，可能耗时很久最后被拒[^taowriting-e17]；交终稿，不交初稿，否则反而更慢[^taowriting-e21]。
7. **别用发文数量和别的学科比。** 数学评价看质量不看速度[^amsculture2006rates-e4]。申请跨学科的职位或基金时，可以附上 AMS 关于按字母署名的声明，向评审解释 `[本项目分析]`。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 和其他学科的人合作时，默认按字母署名，没事先商量 | 按字母署名是数学的传统，其他学科的人常误解[^amsculture2004joint-e6]；不同学科惯例不同，应事先说清 `[本项目分析]` |
| 给只参与过讨论、没有实质贡献的人署名，或漏掉有实质贡献的人 | 每个作者都要有实质贡献，每个有实质贡献的人都应有机会署名[^ams2022ethical-e5] |
| 在报告里讲了别人没发表的想法，却不注明来源 | 口头的、没发表的也算抄袭[^ams2022ethical-e1][^ams2022ethical-e2] |
| 证明还没写完就在报告或网上宣布"我证明了" | 没有合理把握就抢先宣布，会阻碍同行[^ams2022ethical-e3] |
| 发现自己已发表的论文有错，不吭声 | 应及时更正或撤回[^ams2022ethical-e4] |
| 以为发表了、上了 arXiv 就一定对 | arXiv 审核不是同行评审[^arxivmoderation-e1]；Thurston 也提到，有些已发表的定理圈内都知道是错的或证明不完整[^thurston1994proof-e8] |
| 一上来就死磕著名难题 | 难题几乎从不是凭空解决的[^taocareer-e13]，先做可行的问题[^taocareer-e14] |
| 审稿时用稿件里的想法做自己的研究 | 审稿人不能把稿件里的想法据为己有[^ams2022ethical-e10] |
| 计算机辅助的结果只给结论，不给代码和计算细节 | 重要论断要完整公开计算细节[^stodden2013setting-e4] |

---

## 延伸阅读

- **AMS 2004，Joint Research and Its Publication**：一页纸，讲清数学为什么按字母署名。和其他学科合作、或向外行评审解释署名时用。
- **AMS 2006，Rates of Publication**：一页纸，讲清数学为什么发得少、发得慢。
- **AMS Ethical Guidelines**：美国数学会的职业准则，重点读 I（研究与发表）和 IV（出版）两节。
- **Thurston 1994，On proof and progress in mathematics**：讲数学家实际怎样理解、交流和检查证明。适合刚开始读研、想知道"数学研究到底是什么"的人。
- **陶哲轩的 Career advice 系列**：每页一条建议。新手先读 "Talk to your advisor""Take the initiative""Attend talks and conferences""Make your work available""Be patient"。
- **ICERM 2013 报告，Setting the Default to Reproducible**：做数值计算、实验数学、计算机辅助证明的人读。
- **[理论研究](../computer-science/practices/theoretical_research.md)**：怎样推进证明、写证明、查自己的错。

[^thurston1994proof-e1]: Thurston 1994，§1。[证据](../../../sources/notes/thurston1994proof.md#e1)
[^thurston1994proof-e2]: Thurston 1994，§1。[证据](../../../sources/notes/thurston1994proof.md#e2)
[^thurston1994proof-e3]: Thurston 1994，§3。[证据](../../../sources/notes/thurston1994proof.md#e3)
[^thurston1994proof-e4]: Thurston 1994，§3。[证据](../../../sources/notes/thurston1994proof.md#e4)
[^thurston1994proof-e5]: Thurston 1994，§3。[证据](../../../sources/notes/thurston1994proof.md#e5)
[^thurston1994proof-e6]: Thurston 1994，§4。[证据](../../../sources/notes/thurston1994proof.md#e6)
[^thurston1994proof-e7]: Thurston 1994，§4。[证据](../../../sources/notes/thurston1994proof.md#e7)
[^thurston1994proof-e8]: Thurston 1994，§4。[证据](../../../sources/notes/thurston1994proof.md#e8)
[^thurston1994proof-e9]: Thurston 1994，§4。[证据](../../../sources/notes/thurston1994proof.md#e9)
[^thurston1994proof-e10]: Thurston 1994，§4。[证据](../../../sources/notes/thurston1994proof.md#e10)
[^thurston1994proof-e11]: Thurston 1994，§4。[证据](../../../sources/notes/thurston1994proof.md#e11)
[^thurston1994proof-e12]: Thurston 1994，§5。[证据](../../../sources/notes/thurston1994proof.md#e12)
[^thurston1994proof-e14]: Thurston 1994，§5。[证据](../../../sources/notes/thurston1994proof.md#e14)
[^thurston1994proof-e15]: Thurston 1994，§3。[证据](../../../sources/notes/thurston1994proof.md#e15)
[^amsculture2004joint-e1]: AMS 2004，第 2 段。[证据](../../../sources/notes/amsculture2004joint.md#e1)
[^amsculture2004joint-e2]: AMS 2004，第 2 段。[证据](../../../sources/notes/amsculture2004joint.md#e2)
[^amsculture2004joint-e3]: AMS 2004，第 3 段。[证据](../../../sources/notes/amsculture2004joint.md#e3)
[^amsculture2004joint-e4]: AMS 2004，第 3 段。[证据](../../../sources/notes/amsculture2004joint.md#e4)
[^amsculture2004joint-e5]: AMS 2004，第 4 段。[证据](../../../sources/notes/amsculture2004joint.md#e5)
[^amsculture2004joint-e6]: AMS 2004，第 5 段。[证据](../../../sources/notes/amsculture2004joint.md#e6)
[^amsculture2004joint-e7]: AMS 2004，第 2 段。[证据](../../../sources/notes/amsculture2004joint.md#e7)
[^amsculture2006rates-e1]: AMS 2006，第 2 段。[证据](../../../sources/notes/amsculture2006rates.md#e1)
[^amsculture2006rates-e2]: AMS 2006，第 2 段。[证据](../../../sources/notes/amsculture2006rates.md#e2)
[^amsculture2006rates-e3]: AMS 2006，第 3 段。[证据](../../../sources/notes/amsculture2006rates.md#e3)
[^amsculture2006rates-e4]: AMS 2006，第 5 段。[证据](../../../sources/notes/amsculture2006rates.md#e4)
[^amsculture2006rates-e5]: AMS 2006，第 4 段。[证据](../../../sources/notes/amsculture2006rates.md#e5)
[^ams2022ethical-e1]: AMS 伦理准则，I. Mathematical Research and its Presentation。[证据](../../../sources/notes/ams2022ethical.md#e1)
[^ams2022ethical-e2]: AMS 伦理准则，I。[证据](../../../sources/notes/ams2022ethical.md#e2)
[^ams2022ethical-e3]: AMS 伦理准则，I。[证据](../../../sources/notes/ams2022ethical.md#e3)
[^ams2022ethical-e4]: AMS 伦理准则，I。[证据](../../../sources/notes/ams2022ethical.md#e4)
[^ams2022ethical-e5]: AMS 伦理准则，I。[证据](../../../sources/notes/ams2022ethical.md#e5)
[^ams2022ethical-e6]: AMS 伦理准则，I。[证据](../../../sources/notes/ams2022ethical.md#e6)
[^ams2022ethical-e7]: AMS 伦理准则，II. Social Responsibility of Mathematicians。[证据](../../../sources/notes/ams2022ethical.md#e7)
[^ams2022ethical-e8]: AMS 伦理准则，II。[证据](../../../sources/notes/ams2022ethical.md#e8)
[^ams2022ethical-e9]: AMS 伦理准则，IV. Publications。[证据](../../../sources/notes/ams2022ethical.md#e9)
[^ams2022ethical-e10]: AMS 伦理准则，IV。[证据](../../../sources/notes/ams2022ethical.md#e10)
[^ams2022ethical-e11]: AMS 伦理准则，IV。[证据](../../../sources/notes/ams2022ethical.md#e11)
[^ams2022ethical-e12]: AMS 伦理准则，III. Education and Granting of Degrees。[证据](../../../sources/notes/ams2022ethical.md#e12)
[^ams2022ethical-e13]: AMS 伦理准则，III。[证据](../../../sources/notes/ams2022ethical.md#e13)
[^ams2022ethical-e14]: AMS 伦理准则，开头。[证据](../../../sources/notes/ams2022ethical.md#e14)
[^taocareer-e13]: Tao，Don't base career decisions on glamour or fame。[证据](../../../sources/notes/taocareer.md#e13)
[^taocareer-e14]: Tao，Don't prematurely obsess on a single "big problem" or "big theory"。[证据](../../../sources/notes/taocareer.md#e14)
[^taocareer-e6]: Tao，On the importance of partial progress。[证据](../../../sources/notes/taocareer.md#e6)
[^taocareer-e23]: Tao，Talk to your advisor。[证据](../../../sources/notes/taocareer.md#e23)
[^taocareer-e24]: Tao，Talk to your advisor。[证据](../../../sources/notes/taocareer.md#e24)
[^taocareer-e25]: Tao，Talk to your advisor。[证据](../../../sources/notes/taocareer.md#e25)
[^taocareer-e26]: Tao，Take the initiative。[证据](../../../sources/notes/taocareer.md#e26)
[^taocareer-e27]: Tao，Take the initiative。[证据](../../../sources/notes/taocareer.md#e27)
[^taocareer-e28]: Tao，Make your work available。[证据](../../../sources/notes/taocareer.md#e28)
[^taocareer-e29]: Tao，Make your work available。[证据](../../../sources/notes/taocareer.md#e29)
[^taocareer-e30]: Tao，Make your work available。[证据](../../../sources/notes/taocareer.md#e30)
[^taocareer-e31]: Tao，Make your work available。[证据](../../../sources/notes/taocareer.md#e31)
[^taocareer-e32]: Tao，Attend talks and conferences, even those not directly related to your work。[证据](../../../sources/notes/taocareer.md#e32)
[^taocareer-e33]: Tao，Attend talks and conferences, even those not directly related to your work。[证据](../../../sources/notes/taocareer.md#e33)
[^taocareer-e34]: Tao，Be patient。[证据](../../../sources/notes/taocareer.md#e34)
[^taocareer-e35]: Tao，Be patient。[证据](../../../sources/notes/taocareer.md#e35)
[^taocareer-e36]: Tao，Don't be afraid to learn things outside your field。[证据](../../../sources/notes/taocareer.md#e36)
[^taocareer-e37]: Tao，Take the initiative。[证据](../../../sources/notes/taocareer.md#e37)
[^taowriting-e17]: Tao，Submit to an appropriate journal。[证据](../../../sources/notes/taowriting.md#e17)
[^taowriting-e18]: Tao，Submit to an appropriate journal。[证据](../../../sources/notes/taowriting.md#e18)
[^taowriting-e19]: Tao，Submit to an appropriate journal。[证据](../../../sources/notes/taowriting.md#e19)
[^taowriting-e21]: Tao，Submit a final draft, not a first draft。[证据](../../../sources/notes/taowriting.md#e21)
[^arxivendorsement-e1]: arXiv，The arXiv endorsement system，开头。[证据](../../../sources/notes/arxivendorsement.md#e1)
[^arxivendorsement-e2]: arXiv，The arXiv endorsement system。[证据](../../../sources/notes/arxivendorsement.md#e2)
[^arxivendorsement-e3]: arXiv，The arXiv endorsement system。[证据](../../../sources/notes/arxivendorsement.md#e3)
[^arxivmoderation-e1]: arXiv，Content Moderation，开头。[证据](../../../sources/notes/arxivmoderation.md#e1)
[^arxivmoderation-e2]: arXiv，Content Moderation，开头。[证据](../../../sources/notes/arxivmoderation.md#e2)
[^arxivmoderation-e3]: arXiv，Content Moderation。[证据](../../../sources/notes/arxivmoderation.md#e3)
[^stodden2013setting-e1]: Stodden 等 2013（ICERM 报告），Abstract。[证据](../../../sources/notes/stodden2013setting.md#e1)
[^stodden2013setting-e2]: Stodden 等 2013，Introduction。[证据](../../../sources/notes/stodden2013setting.md#e2)
[^stodden2013setting-e3]: Stodden 等 2013，Introduction。[证据](../../../sources/notes/stodden2013setting.md#e3)
[^stodden2013setting-e4]: Stodden 等 2013，Journals 一节。[证据](../../../sources/notes/stodden2013setting.md#e4)
[^stodden2013setting-e5]: Stodden 等 2013，Appendix C。[证据](../../../sources/notes/stodden2013setting.md#e5)
