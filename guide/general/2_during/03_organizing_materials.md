# 整理科研材料：数据、代码、结果和笔记

> **状态**：初稿，待审阅 · **最后更新**：2026-10-05

本章讲一个项目的材料怎样存放和记录：目录怎么分，原始数据怎么保护，每个结果怎样能追溯到来源，笔记分几种。目标是几个月后你自己（或导师、合作者）打开文件夹，能看懂你做了什么、为什么做。研究日志的写法和回顾见[推进研究](01_making_progress.md)第 4 节；结论可信、可复现的要求见[证据、分析与效度](02_evidence_and_validity.md)；为什么要记录、保存和共享（诚信角度），见[科研诚信与伦理](../4_throughout/02_integrity_and_ethics.md#3-让结果能被复现记录保存共享)，本章只讲具体怎么做；项目计划见[做计划](../1_before/05_planning.md)。

本章的例子多来自用计算机分析数据的研究。目录、只读、备份、README（放在目录里、说明里面有什么的说明文件）这些原则对所有学科都适用；涉及代码和版本控制的部分，注明了"计算研究"。

**读完本章，你应该能：**

- 给一个新项目建好目录，分开原始数据、处理代码、结果和文档；
- 保护原始数据，并让派生数据可以重新生成；
- 为每个重要结果记下它是怎么得到的；
- 分清三种笔记：现状、按日期的研究日志、稳定的结论；
- 写出让几个月后的自己看得懂的 README。

---

## 1. 一个项目一个目录

**怎么做：**

- 一个项目的所有文件放在同一个以项目命名的根目录下[^wilson2017good-e6][^noble2009quick-e3]。
- 怎么划分项目：按数据和代码的重叠程度[^wilson2017good-e6]。在学术研究中，一个项目通常对应一篇论文，"一个项目 = 一篇论文 = 一个文件夹 = 一个 git 仓库"是个好的默认选择[^mineault2021good-e1]（git 是最常用的版本控制工具，见第 4 节）。
- 几个项目共用的代码或工具，单独建一个项目[^noble2009quick-e3][^mineault2021good-e2]。

**为什么：** 整理的核心原则是：**一个不熟悉你项目的人，看你的文件就能详细了解你做了什么、为什么做**。这个人最常见的就是几个月后的你自己[^noble2009quick-e1]。而且你做的每件事，大概都得重做一遍：发现数据有问题、拿到新数据、要换参数[^noble2009quick-e2]。组织清楚，重做就容易得多。

## 2. 原始数据只读，其余都能重新生成

**怎么做：**

- **原始数据单独放，不做任何修改。** 原始数据放 `data/`，清洗和分析中生成的文件放 `results/`[^wilson2017good-e8]。数据目录下再分原始数据、派生数据和汇总[^osforganizing-e2]。
- **设为只读。** 把原始数据文件设为只读，防止误改或一时冲动手工修改[^wilson2017good-e9][^osforganizing-e3]。不要在原始数据文件里做计算、求和或画图；要算，先复制一份[^osforganizing-e3]。
- **至少备份在两个地方**[^wilson2017good-e10]。
- **派生数据要能从原始数据重新生成。** 这样中间结果丢了也不怕，也不必全部放进版本控制[^wilson2017good-e17]。
- **记下数据从哪里来。** 在数据目录的 README 里写明谁在哪天从哪里获得了这些数据[^noble2009quick-e10]。
- 实在避免不了手工处理时，至少记下改动或移动了哪些文件、为什么[^sandve2013ten-e10]。

这对非计算研究同样适用：问卷原件、访谈录音、实验仪器导出的文件、野外记录的扫描件，都是原始数据。`[本项目分析]`

## 3. 每个结果都要能追溯到它是怎么来的

**怎么做：**

- 只要一个结果可能有用，就记下它是怎么得到的[^sandve2013ten-e7]。最低要求：一年后的你自己能大致重现它[^sandve2013ten-e2]。
- 对每次实验或分析，记下 `[本项目分析，依据下列资料]`：
  - **想检验什么**（假设或问题）；
  - **用了哪版代码**（计算研究中是版本控制的提交编号）和**哪版数据**；
  - **参数和配置**，程序的名称和版本[^sandve2013ten-e8]；有随机性时记下随机种子[^sandve2013ten-e11]；
  - **输出放在哪里**，以及你的观察和结论。
- 原则是记录你做的每一步操作，并让它尽可能透明、可重复[^noble2009quick-e8]。Noble 的做法是两者并行：记录本用文字描述实验，驱动脚本保存全部细节[^noble2009quick-e9]。
- 论文里写下的每条结论，都要能找回它所依据的确切结果[^sandve2013ten-e12]。

**用什么工具记** `[本项目分析]`：每周只跑几次实验时，一张表格或一个文本文件就够了，每行一次实验。实验科学和田野研究中，纸质或电子实验记录本（electronic lab notebook，按日期记录实验的软件）、一张记录样本和处理步骤的表格，起的是同样的作用。实验多到表格管不过来时（例如每天几十次计算实验），再考虑专门的实验追踪工具，例如 MLflow 或 Weights & Biases。这类工具记录的也正是参数、代码版本、指标和输出文件[^mlflowtracking-e1]，工具只是让记录自动化，记什么的原则不变。

## 4. 用版本控制，不要用文件名管版本

**怎么做：**

- **不要用 `final`、`final2`、`final_真的最终版` 来管理版本。** 文件名应该反映内容或用途；不要用流水号或在稿件中的位置（如 `fig_3_a.png`）命名，这些编号几乎一定会变[^wilson2017good-e13]。
- **计算研究：项目一开始就用版本控制**（如 git），不要等做了几周才发现早期版本没有任何记录[^noble2023ten-e12]。所有自己写的脚本都要纳入版本控制[^sandve2013ten-e11]。
- **小步、经常提交。** 一次提交对应一组相关的工作；节奏大约每天几次到每周几次[^mineault2021good-e3]。合适的大小是"将来可能想一步撤销的一组修改"[^wilson2017good-e14]。

**为什么：** 版本控制自动给每次保存打上时间戳，不再依赖人给备份副本起合理的名字[^wilson2017good-e16]。`final2` 说不清它和 `final` 差在哪，提交记录可以。

**不写代码的研究**：没有版本控制工具时，用"日期 + 内容"命名副本（如 `2026-10-05_问卷_第二轮修改.docx`），并在变更日志里记一笔改了什么（见第 5 节）。`[本项目分析]`

## 5. 分清三种笔记

**怎么做** `[本项目分析，依据下列资料]`：一个项目至少维护三种文字记录，各管一件事。

| 笔记 | 回答什么 | 怎么写 |
|---|---|---|
| **现状文档** | 项目现在到哪了？下一步是什么？ | 一份，始终保持最新，覆盖旧内容。可以就是项目 README 的一节，加上待办清单[^wilson2017good-e12] |
| **研究日志** | 哪天做了什么、看到了什么、怎么理解、决定了什么？ | 按日期记，写得详细[^noble2009quick-e6]；旧条目不删改 `[本项目分析]` |
| **稳定结论** | 我们确定知道了什么？做过哪些重要决定，为什么？有哪些已知局限？ | 只收经过检验的发现和决定，随项目更新；它是论文的原材料 |

- **研究日志**是主体。Noble 建议按日期记，写得详细些，附上结果图表；除了做了什么，还要记观察、结论和后续想法[^noble2009quick-e6]。实验失败时，先写下你凭什么判断它失败了，再开始下一个实验[^noble2009quick-e7]。Wilson 等人示例项目的文档目录里，就放着一份持续更新的记录本和一份持续更新的论文草稿[^wilson2017good-e18]。
- **变更日志**是研究日志的一个简化版，专记项目文件改了什么。Wilson 等人建议在文档目录放一个 `CHANGELOG.txt`，按日期倒序（最新在前）记下项目的改动，作用相当于实验记录本[^wilson2017good-e15]。不用版本控制的项目（见第 4 节）尤其需要它。
- **现状文档和稳定结论**是从日志里提炼出来的。日志按时间排，回答"那天发生了什么"；但想知道"现在怎样"或"我们确定知道什么"时，翻日志太慢。[做计划](../1_before/05_planning.md#6-每周按主张回顾持续更新计划)里的每周回顾，正好用来把日志压缩进这两份文档；日志本身怎么记、怎么回顾，见[推进研究](01_making_progress.md#4-记研究日志并定期回顾)。

**为什么：** 三者互补，不是三选一。只有日志，结论埋在几百条记录里；只有现状文档，几个月后说不清某个决定是怎么来的。`[本项目分析]`

> **不同的看法：结果目录按时间分，还是按内容分？**
> - Noble 主张数据和结果目录按日期组织（如 `2008-12-19`），因为最终的实验结构往往和最初设想的大不相同，按内容起的目录名半年后可能连自己都看不懂[^noble2009quick-e4][^noble2009quick-e5]。
> - Wilson 等人主张按文件类型组织，结果目录下用命名规则或子目录分开中间文件和可发表的图表，属于不同论文的结果分组存放[^wilson2017good-e19]。
>
> 实际操作中 `[本项目分析]`：探索阶段的实验结果按日期放（`results/2026-10-05_主题/`），配合按日期的研究日志，很好对上号；进入写论文阶段，把要进论文的图表和生成它们的脚本整理到按内容命名的位置（如 `results/paper/`）。

## 6. 给未来的自己写 README

**怎么做：**

- 项目根目录放一个 README，说明项目的目的[^wilson2017good-e11][^turingwaycompendia-e4]：是什么、怎么运行或复现、各个目录放什么。
- 每个主要目录也放一个 README，说明里面的文件是什么、目录之间什么关系；文件增减时同步更新[^osforganizing-e4]。
- 计算研究中，写明运行所需的计算环境（软件和版本）[^turingwaycompendia-e3]。

**为什么：**

- 这些做法最大的受益者是未来的你：三个月前的你不会回邮件[^wilson2017good-e5]。Karpathy 说，几个月后你一定会回到自己的代码，例如为论文终稿补几个实验，然后完全看不懂；所以他在每个仓库都写详细的 readme，作为给未来自己的说明[^karpathy2016survival-e10]。Mineault 的手册引用了一句话：文档是写给未来自己的情书[^mineault2021good-e4]。
- 文件名和位置本身就是文档，组织得越清楚，研究越容易复现[^osforganizing-e1]。

## 7. 一个可参考的目录结构

下面是综合上述资料的**建议**，不是标准 `[本项目分析，依据 Wilson 等人、Noble、The Turing Way、Mineault、OSF]`。按你的学科和项目删改；不写代码的项目可以没有 `src/`。

```
项目名/
├── README.md          项目是什么、现状、怎么复现、各目录说明
├── data/
│   ├── raw/           原始数据，只读；附 README 写明来源和获取日期
│   └── processed/     由脚本从 raw 生成，可以删掉重建
├── src/               自己写的代码和分析脚本（计算研究）
├── results/
│   ├── 2026-10-05_主题/  探索阶段按日期存放的实验输出
│   └── paper/         要进论文的图表，以及生成它们的脚本说明
├── notes/
│   ├── status.md      现状文档：始终最新
│   ├── log.md         研究日志：按日期追加
│   └── findings.md    稳定结论：发现、决定、局限
├── doc/               论文草稿、方案、报告
└── environment 文件   计算环境说明（如 requirements.txt）
```

这和 Wilson 等人把文字材料放 `doc/`、原始数据放 `data/`、生成的文件放 `results/`[^wilson2017good-e7][^wilson2017good-e8]，以及 The Turing Way 的"数据、方法、产出分开"[^turingwaycompendia-e3] 是一致的。研究汇编（research compendium，即一个项目全部数字材料的集合：数据、代码、文本[^turingwaycompendia-e1]）的重点是把各部分放在一起，一个基本的文件夹结构就可以够用[^turingwaycompendia-e2]。

## 本章检查清单

- [ ] 项目所有文件在一个以项目命名的目录下；共用工具单独成项目。
- [ ] 原始数据单独存放、设为只读、至少备份在两个地方。
- [ ] 派生数据能从原始数据重新生成，生成步骤有记录。
- [ ] 每个重要结果，我能说出它用的代码版本、数据版本、参数和输出位置（不写代码的研究：用的是哪版数据和哪些处理步骤）。
- [ ] 没有 `final2` 这样的文件；计算研究的代码在版本控制里，提交小而频繁。
- [ ] 我有现状文档、按日期的研究日志、稳定结论三种记录。
- [ ] 根目录和主要子目录都有 README，内容是最新的。
- [ ] 几个月不碰这个项目后，我能靠 README 和日志重新跑出主要结果。

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 直接在原始数据上清洗、修改 | 出错后回不去，也无法从头重跑分析[^wilson2017good-e9] |
| 用 `final`、`final2`、`result1` 命名 | 说不清版本间的区别，编号也会变[^wilson2017good-e13][^wilson2017good-e16] |
| 做了几周才开始用版本控制 | 早期版本没有记录[^noble2023ten-e12] |
| 一次提交几百行改动 | 无法单独追查或撤销某个改动[^wilson2017good-e14] |
| 结果文件没有记录怎么来的 | 一年后自己都重现不了[^sandve2013ten-e2] |
| 实验失败只留一张图就换下一个 | 别人（和未来的你）看不出它为什么算失败[^noble2009quick-e7] |
| 只有日志，没有现状和结论 | 想知道"现在怎样"要翻几百条记录 `[本项目分析]` |
| 不写 README | 几个月后自己也看不懂[^karpathy2016survival-e10] |

## 延伸阅读

- **Noble, "A Quick Guide to Organizing Computational Biology Projects"**（2009）：建目录、写实验记录本时读。几页长，例子来自计算生物学，原则通用。
- **Wilson 等人, "Good enough practices in scientific computing"**（2017）：一份"每个研究者都该做到"的最低清单，涵盖数据、代码、协作、目录和版本管理。
- **Sandve 等人, "Ten Simple Rules for Reproducible Computational Research"**（2013）：想让结果可追溯、可复现时读。
- **The Turing Way, Research Compendia**：想把项目整理成可分享、可复现的整体时读。
- **Mineault, The Good Research Code Handbook**：写研究代码的人读，讲项目结构、git、文档。
- **OSF（Open Science Framework，开放科学框架）, "Organizing files"**：简短的官方清单，讲原始数据和派生数据分开、只读、README。

[^wilson2017good-e5]: Wilson 等人 2017，Introduction。[证据](../../../sources/notes/wilson2017good.md#e5)
[^wilson2017good-e6]: Wilson 等人 2017，Project organization，4a。[证据](../../../sources/notes/wilson2017good.md#e6)
[^wilson2017good-e7]: Wilson 等人 2017，Project organization，4b。[证据](../../../sources/notes/wilson2017good.md#e7)
[^wilson2017good-e8]: Wilson 等人 2017，Project organization，4c。[证据](../../../sources/notes/wilson2017good.md#e8)
[^wilson2017good-e9]: Wilson 等人 2017，Data management，1a。[证据](../../../sources/notes/wilson2017good.md#e9)
[^wilson2017good-e10]: Wilson 等人 2017，Data management，1b。[证据](../../../sources/notes/wilson2017good.md#e10)
[^wilson2017good-e11]: Wilson 等人 2017，Collaboration，3a。[证据](../../../sources/notes/wilson2017good.md#e11)
[^wilson2017good-e12]: Wilson 等人 2017，Collaboration，3b。[证据](../../../sources/notes/wilson2017good.md#e12)
[^wilson2017good-e13]: Wilson 等人 2017，Project organization，4f。[证据](../../../sources/notes/wilson2017good.md#e13)
[^wilson2017good-e14]: Wilson 等人 2017，Keeping track of changes，5b。[证据](../../../sources/notes/wilson2017good.md#e14)
[^wilson2017good-e15]: Wilson 等人 2017，Keeping track of changes，5f。[证据](../../../sources/notes/wilson2017good.md#e15)
[^wilson2017good-e16]: Wilson 等人 2017，Keeping track of changes。[证据](../../../sources/notes/wilson2017good.md#e16)
[^wilson2017good-e17]: Wilson 等人 2017，Keeping track of changes。[证据](../../../sources/notes/wilson2017good.md#e17)
[^wilson2017good-e18]: Wilson 等人 2017，Project organization，Box 3 说明。[证据](../../../sources/notes/wilson2017good.md#e18)
[^wilson2017good-e19]: Wilson 等人 2017，Project organization，4c。[证据](../../../sources/notes/wilson2017good.md#e19)
[^noble2009quick-e1]: Noble 2009，Principles。[证据](../../../sources/notes/noble2009quick.md#e1)
[^noble2009quick-e2]: Noble 2009，Principles。[证据](../../../sources/notes/noble2009quick.md#e2)
[^noble2009quick-e3]: Noble 2009，File and Directory Organization。[证据](../../../sources/notes/noble2009quick.md#e3)
[^noble2009quick-e4]: Noble 2009，File and Directory Organization。[证据](../../../sources/notes/noble2009quick.md#e4)
[^noble2009quick-e5]: Noble 2009，File and Directory Organization。[证据](../../../sources/notes/noble2009quick.md#e5)
[^noble2009quick-e6]: Noble 2009，The Lab Notebook。[证据](../../../sources/notes/noble2009quick.md#e6)
[^noble2009quick-e7]: Noble 2009，The Lab Notebook。[证据](../../../sources/notes/noble2009quick.md#e7)
[^noble2009quick-e8]: Noble 2009，Carrying Out a Single Experiment。[证据](../../../sources/notes/noble2009quick.md#e8)
[^noble2009quick-e9]: Noble 2009，Carrying Out a Single Experiment。[证据](../../../sources/notes/noble2009quick.md#e9)
[^noble2009quick-e10]: Noble 2009，Figure 1 说明。[证据](../../../sources/notes/noble2009quick.md#e10)
[^sandve2013ten-e7]: Sandve 等人 2013，Rule 1。[证据](../../../sources/notes/sandve2013ten.md#e7)
[^sandve2013ten-e8]: Sandve 等人 2013，Rule 1。[证据](../../../sources/notes/sandve2013ten.md#e8)
[^sandve2013ten-e2]: Sandve 等人 2013，Rule 1。[证据](../../../sources/notes/sandve2013ten.md#e2)
[^sandve2013ten-e10]: Sandve 等人 2013，Rule 2。[证据](../../../sources/notes/sandve2013ten.md#e10)
[^sandve2013ten-e11]: Sandve 等人 2013，Rule 4、Rule 6。[证据](../../../sources/notes/sandve2013ten.md#e11)
[^sandve2013ten-e12]: Sandve 等人 2013，Rule 9。[证据](../../../sources/notes/sandve2013ten.md#e12)
[^turingwaycompendia-e1]: The Turing Way，Research Compendia，Summary。[证据](../../../sources/notes/turingwaycompendia.md#e1)
[^turingwaycompendia-e2]: The Turing Way，Research Compendia，Summary。[证据](../../../sources/notes/turingwaycompendia.md#e2)
[^turingwaycompendia-e3]: The Turing Way，Research Compendia，Structure of a Research Compendium。[证据](../../../sources/notes/turingwaycompendia.md#e3)
[^turingwaycompendia-e4]: The Turing Way，Research Compendia，Basic Compendium。[证据](../../../sources/notes/turingwaycompendia.md#e4)
[^mineault2021good-e1]: Mineault 2021，Setting up your project。[证据](../../../sources/notes/mineault2021good.md#e1)
[^mineault2021good-e2]: Mineault 2021，Setting up your project。[证据](../../../sources/notes/mineault2021good.md#e2)
[^mineault2021good-e3]: Mineault 2021，Setting up your project，git 一节。[证据](../../../sources/notes/mineault2021good.md#e3)
[^mineault2021good-e4]: Mineault 2021，Document your code（引 Damian Conway）。[证据](../../../sources/notes/mineault2021good.md#e4)
[^osforganizing-e1]: OSF Support，Organizing files。[证据](../../../sources/notes/osforganizing.md#e1)
[^osforganizing-e2]: OSF Support，Separate raw data from derived data。[证据](../../../sources/notes/osforganizing.md#e2)
[^osforganizing-e3]: OSF Support，Make raw data read-only。[证据](../../../sources/notes/osforganizing.md#e3)
[^osforganizing-e4]: OSF Support，Make README files。[证据](../../../sources/notes/osforganizing.md#e4)
[^mlflowtracking-e1]: MLflow 文档，MLflow Tracking（工具官方文档）。[证据](../../../sources/notes/mlflowtracking.md#e1)
[^karpathy2016survival-e10]: Karpathy 2016，Writing code，"Think of the future you"。[证据](../../../sources/notes/karpathy2016survival.md#e10)
[^noble2023ten-e12]: Noble 2023，Rule 9。[证据](../../../sources/notes/noble2023ten.md#e12)
