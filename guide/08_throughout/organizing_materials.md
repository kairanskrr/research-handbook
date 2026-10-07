# 整理科研材料：数据、代码、结果和笔记

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07
>
> 本页的道理适用于各学科，例子和具体做法以计算机为例。

## 什么时候需要这一页

- **项目开工的第一天**：先建好目录、定好规矩，比事后返工省事得多。
- **结果开始变多的时候**：你已经说不清 `result_v3_new.csv` 是哪次实验跑出来的。
- **隔了几周回到项目、写论文要找回某个数字、导师问"这个结果怎么来的"时**：如果答不上来，就该照这一页补一补。

整理的目标只有一个：**一个不熟悉这个项目的人，看你的文件就能详细了解你做了什么、为什么做。** 这个人最常见的，就是你自己[^noble2009quick-e1]。有句玩笑说：三个月前的你不回邮件[^wilson2017good-e5]。

为什么值得花这个功夫：你做的每件事，大概都得重做一遍[^noble2009quick-e2]。发现数据有问题、拿到新数据、审稿人要求补实验，都会让你重跑。材料整理得清楚，重做就是几条命令；整理得乱，重做就是考古。`[本项目分析]`

先说明适用范围：本页引用的资料大多写给做计算的研究者。Wilson 等人讲的是科学计算中"够用"的做法[^wilson2017good-e1]，Schnell 的记录本规则写给只做计算的生物学者[^schnell2015ten-e8]，Noble 的例子来自计算生物学。原始数据只读、结果可追溯、按日期记日志这些原则，换到问卷、访谈、实验室研究里同样能用；目录名、git 这些具体做法，按你的学科调整。`[本项目分析]`

本页只讲具体怎么做。为什么要记录、保存、共享（诚信的角度），见[科研诚信与伦理](integrity_and_ethics.md)；结论怎样才可信，见[效度与局限](../02_from-project-to-study/03_validity-and-limits.md)。

---

## 1. 一个项目一个目录，开工就建好

**怎么做：**

- 一个项目的所有文件放在同一个以项目命名的根目录下[^wilson2017good-e6][^noble2009quick-e3]。
- 怎么划分项目：看数据和代码重叠多少[^wilson2017good-e6]。在学术界，一个项目往往自然对应一篇论文，所以"一个项目 = 一篇论文 = 一个文件夹 = 一个 git 仓库"是个好的默认选择[^mineault2021good-e1]（版本控制工具会记下文件的每一次改动，git 是其中一种，见第 4 节）。
- 几篇论文共用的代码或工具，单独建一个项目[^noble2009quick-e3][^mineault2021good-e2]。
- 文字材料（论文草稿、代码说明、电子实验记录本）放 `doc/`，原始数据放 `data/`，清洗和分析中生成的文件放 `results/`[^wilson2017good-e7][^wilson2017good-e8]。数据、方法、产出三者要清楚地分开[^turingwaycompendia-e3]。

下面是一个可以直接套用的起点 `[本项目分析，综合本节和第 2、5、6 节的资料]`。它不是标准，按你的项目删改；不写代码的项目可以没有 `src/`。

```
llm-contract-vuln/
├── README.md          项目是什么、现在到哪了、怎么复现、各目录放什么
├── data/
│   ├── raw/           原始数据，只读；附 README 写明来源和获取日期
│   └── processed/     由脚本从 raw 生成，可以删掉重建
├── src/               自己写的代码和分析脚本
├── results/
│   ├── 2026-10-05_重入漏洞提示对比/   探索阶段按日期存放的实验输出
│   └── paper/         要进论文的图表，以及生成它们的脚本
├── notes/
│   ├── status.md      现状：始终最新
│   ├── log.md         研究日志：按日期追加
│   └── findings.md    稳定结论：发现、决定、局限
├── doc/               论文草稿、项目简介、报告
└── requirements.txt   计算环境：用到的软件和版本
```

一个项目的全部数字材料（数据、代码、文本）放在一起，有个名字叫研究汇编[^turingwaycompendia-e1]。它的主要目的是让项目的各部分能一起发布，所以一个把各部分放在一起的基本文件夹结构就可以够用[^turingwaycompendia-e2]。

**容易错在哪：** 等"项目稳定了再整理"。项目从来不会稳定，越晚整理，要补的越多。`[本项目分析]`

**写下来：** 给你现在的项目建好这个目录，把散落在下载文件夹、桌面、聊天记录里的材料搬进去。

## 2. 原始数据只读，其余都能重新生成

**怎么做：**

- **原始数据单独放，不做任何修改。** 数据目录下再分原始数据、派生数据和汇总三个子目录[^osforganizing-e2]。
- **设为只读。** 这样就很难误改，也不会一时冲动手工去改它[^wilson2017good-e9][^osforganizing-e3]。不要在原始数据文件里做计算、求和或画图[^osforganizing-e3]。
- **至少备份在两个地方**[^wilson2017good-e10]。
- **派生数据要能用原始数据和代码重新生成。** 做得到这一点，中间文件就不必放进版本控制[^wilson2017good-e17]。
- **记下数据从哪里来。** 在数据目录的 README 里写明谁在哪天从哪里获得了这些数据[^noble2009quick-e10]。数据来自太大、没法在本地存一份的公共数据库时，要记下获取的确切步骤，以及正式版本号或下载日期[^wilson2017good-e21]。
- **实在避免不了手工处理**，至少记下改动或移动了哪些文件、为什么[^sandve2013ten-e10]。

**为什么：** 用清理过的版本覆盖原始数据很诱人，但只有原样保留原始数据，你才能从头重跑分析、从失误中恢复，并且放心地去尝试[^wilson2017good-e20]。

**在智能合约的例子里** `[本项目分析]`：从区块链浏览器抓下来的合约源码、下载的公开漏洞数据集，是原始数据，放 `data/raw/`；去重、过滤掉无法编译的合约之后的版本，是派生数据，由 `src/` 里的脚本生成。你手工标注的"是否存在重入漏洞"，是你自己产生的原始数据，标完一轮也要存一份只读的。

其他学科也一样：问卷原件、访谈录音、仪器导出的文件、田野记录的扫描件，都是原始数据。`[本项目分析]`

**容易错在哪：** 在原始文件上"顺手"删几行明显有问题的数据。几个月后你说不清删了哪些、为什么删，也没法从头重跑。`[本项目分析]`

**写下来：** 在 `data/raw/README.md` 里，给每份原始数据写一行：是什么、从哪里来、哪天拿到的、谁拿的。

## 3. 每个结果都要能追溯到它是怎么来的

**怎么做：** 只要一个结果可能有用，就记下它是怎么得到的[^sandve2013ten-e7]。最低要求：一年后的你自己能大致重现它[^sandve2013ten-e2]。

每一步里可能影响结果的细节都要记下；由程序完成的步骤，关键是程序的名称和版本，以及确切的参数和输入[^sandve2013ten-e8]。有随机性的分析，记下随机种子[^sandve2013ten-e11]。

**每次运行，至少记下这些** `[本项目分析]`：

| 记什么 | 智能合约的例子 |
|---|---|
| 想检验什么 | "提示里加漏洞模式，重入漏洞检出率会不会提高" |
| 用了哪版代码、哪版数据 | 代码的版本控制提交编号；评测集是去掉泄露前还是去掉后 |
| 参数和程序版本 | 大模型的名称和版本、温度、提示原文 |
| 随机种子 | 抽样和模型调用用到的随机种子 |
| 输出放在哪里 | `results/2026-10-07_提示对比/` |
| 看到了什么、怎么理解 | 比如"检出率上去了，但误报也多了，要看是哪类合约" |

**两份记录并行。** 原则是记录你做的每一步操作，并让它尽可能透明、可重复[^noble2009quick-e8]。一个好用的做法：记录本里用文字描述这次实验，运行实验的脚本里保存全部细节[^noble2009quick-e9]。脚本保证"能重跑"，记录本保证"看得懂为什么跑"。

**论文里的每条结论，都要能找回它所依据的确切结果**[^sandve2013ten-e12]。比如论文里写"提示使检出率提高了 12 个百分点"，这个数字要能一路找回到某个结果目录、某次提交、某版数据。

**用什么工具记** `[本项目分析]`：实验不多时，一张表格或一个文本文件就够了，每行一次实验。实验多到表格管不过来时，可以考虑专门的实验追踪工具，这类工具在机器学习里用得多。举个例子，MLflow 提供记录参数、代码版本、指标和输出文件的接口和界面[^mlflowtracking-e1]。工具只是让记录自动化，记什么的原则不变；不跑大量计算实验的研究用不着它。

**容易错在哪：** 只记"效果好的"那几次。失败和不确定的结果，往往是后面解释"为什么这样设计"的依据。`[本项目分析]`

**写下来：** 照上面的表做一个运行记录模板（每行一次运行），把你最近一次实验补记进去。补不全的栏目，就是你的记录里缺的东西。

## 4. 用版本控制，不要用文件名管版本

**怎么做：**

- **不要用 `final`、`final2`、`final_真的最终版` 管理版本** `[本项目分析]`。文件名应该反映内容或用途；也不要用流水号（`result1.csv`）或在稿件中的位置（`fig_3_a.png`）命名，这些编号几乎一定会变[^wilson2017good-e13]。
- **项目一开始就用版本控制。** 不要等做了几周，才发现最初几版代码没有任何记录[^noble2023ten-e12]。所有自己写的脚本都要纳入版本控制[^sandve2013ten-e11]。
- **小步、经常提交。** 一次提交对应一组相关的工作，节奏大约每天几次到每周几次[^mineault2021good-e3]。一次改动多大合适：将来你可能想一步撤销的那一组修改[^wilson2017good-e14]。

**为什么：** 版本控制自动给每次保存打上时间戳，不再依赖人给备份副本起合理的名字[^wilson2017good-e16]。`final2` 说不清它和 `final` 差在哪，提交记录可以。更要紧的是：回不到产生某个结果时的代码，你就没法判断那个结果是不是程序错误造成的[^sandve2013ten-e4]。

**不写代码的材料** `[本项目分析]`：问卷、访谈提纲、论文草稿如果不进版本控制，就用"日期 + 内容"命名副本（如 `2026-10-05_标注指南_第二轮.docx`），并在变更日志里记一笔改了什么（见第 5 节）。

**写下来：** 在项目根目录初始化一个 git 仓库，把现有脚本提交进去；把文件夹里所有叫 `final`、`new`、`v2` 的文件，改成说明内容的名字。

## 5. 分清三种笔记

一个项目至少维护三种文字记录，各管一件事 `[本项目分析，依据下列资料]`：

| 笔记 | 回答什么 | 怎么写 |
|---|---|---|
| **现状** | 项目现在到哪了？下一步是什么？ | 只有一份，始终最新，直接覆盖旧内容。可以是 README 里的一节，加一份待办清单[^wilson2017good-e12] |
| **研究日志** | 哪天做了什么、看到了什么、怎么理解、决定了什么？ | 按日期追加，写得详细些[^noble2009quick-e6]；旧条目不删 |
| **稳定结论** | 我们确定知道了什么？做过哪些重要决定，为什么？有哪些已知局限？ | 只收经过检验的发现和决定，随项目更新；它是论文的原材料 |

**研究日志是主体。** 执行阶段怎么每天记、每一两周怎么回顾，见[执行与迭代](../03_conduct-and-analyze/01_run-and-iterate.md)。这里只讲怎么记才经得起日后翻查。下面几条大多来自写给计算生物学者的记录本规则[^schnell2015ten-e8]，换到其他研究同样适用 `[本项目分析]`：

- **按日期记，一条一条往下写**，每条写明日期和主题[^schnell2015ten-e10]。
- **做完马上记**[^schnell2015ten-e3]。靠记忆的话，会上的一个建议、分析中一个关键步骤，到时候很可能就想不起来了[^schnell2015ten-e9]。
- **不光记做了什么**，还要记观察、结论和后续想法，附上结果图表[^noble2009quick-e6]。
- **写错了不要删**，用一条细线划掉，在旁边写更正。错误本身也是研究过程的重要部分[^schnell2015ten-e4]。

**变更日志**是研究日志的简化版，专记项目文件改了什么：在文档目录放一个 `CHANGELOG.txt`，按日期倒序（最新在前）记下改动，它的作用相当于实验记录本[^wilson2017good-e15]。不进版本控制的材料尤其需要它 `[本项目分析]`。

**读文献的笔记**另外存，每篇一份，见[进入领域](../01_from-interest-to-project/01_enter-a-field.md#6-记笔记一篇一份再加一份问题记录)。可以放在 `notes/papers/` 下，和项目放在一起。`[本项目分析]`

**为什么要三种：** 日志按时间排，回答"那天发生了什么"；想知道"现在怎样""我们确定知道什么"时，翻几百条日志太慢。反过来，只有现状文档，几个月后说不清某个决定是怎么来的。三者互补，不是三选一。每周回顾时，把这一周的日志压缩进现状和稳定结论，见[计划与日常节奏](planning_and_routines.md)。`[本项目分析]`

**写下来：** 建好 `status.md`、`log.md`、`findings.md` 三个文件。今天就在日志里写第一条：日期、做了什么、看到了什么、下一步。

> **不同的看法：结果目录按时间分，还是按内容分？**
>
> - **按时间分**：Noble 的做法是数据和结果目录按日期组织，因为给目录起"有逻辑"的名字，半年后可能连自己都看不懂[^noble2009quick-e4][^noble2009quick-e5]。
> - **按内容分**：Wilson 等人主张用命名规则或子目录，把清洗后的数据、统计表、可发表的图表这类中间文件清楚地分开，属于不同论文的放在一起[^wilson2017good-e19]。
>
> 两种可以结合 `[本项目分析]`：探索阶段按日期放（`results/2026-10-05_主题/`），正好和按日期的研究日志对上号；开始写论文时，把要进论文的图表和生成它们的脚本整理到按内容命名的位置（如 `results/paper/`）。

## 6. 给未来的自己写 README

**怎么做：**

- **项目根目录放一个 README**，说明项目的目的[^wilson2017good-e11]。它是整个项目的入口页[^turingwaycompendia-e4]。写清楚：这是什么项目、现在到哪了、怎么运行或复现、各个目录放什么 `[本项目分析]`。
- **每个主要目录也放一个 README**，说明里面的文件是什么、用途是什么；文件增减时同步更新[^osforganizing-e4]。
- **写明计算环境**[^turingwaycompendia-e3]，例如用到的软件和版本。

**为什么：** 几个月后你一定会回到自己的代码，例如为论文终稿补几个实验，然后发现自己完全摸不着头脑。一个办法是在每个仓库都写详细的 README，作为给未来自己的说明：代码怎么工作、怎么运行[^karpathy2016survival-e10]。有句话说得好：文档是写给未来自己的情书[^mineault2021good-e4]。另外，文件名和位置本身就是文档，组织得越清楚，研究越容易复现[^osforganizing-e1]。

**容易错在哪：** README 写了一次就不再更新，和实际目录对不上。过时的 README 比没有更误导人。`[本项目分析]`

**写下来：** 用十分钟写根目录的 README。写完请一个同学只看 README，说出怎么跑出你的主要结果；他卡住的地方，就是要补的地方。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 直接在原始数据上清洗、修改 | 出错后回不去，也没法从头重跑分析[^wilson2017good-e20] |
| 用 `final`、`final2`、`result1` 命名 | 说不清版本间的区别，编号也会变[^wilson2017good-e13][^wilson2017good-e16] |
| 做了几周才开始用版本控制 | 最初的版本没有记录[^noble2023ten-e12] |
| 一次提交一大堆不相关的改动 | 将来想单独撤销其中一处时做不到[^wilson2017good-e14] |
| 结果文件没记怎么来的 | 一年后自己都重现不了[^sandve2013ten-e2] |
| 实验失败只留一张图就换下一个 | 别人和未来的你看不出它为什么算失败[^noble2009quick-e7] |
| 过几天再补日志 | 关键的想法和步骤已经忘了[^schnell2015ten-e9] |
| 只有日志，没有现状和结论 | 想知道"现在怎样"要翻几百条记录 `[本项目分析]` |
| 不写 README，或写了不更新 | 几个月后自己也看不懂[^karpathy2016survival-e10] |

## 延伸阅读

- **Noble, "A Quick Guide to Organizing Computational Biology Projects"**（2009）：建目录、写记录本时读。篇幅短，写给计算生物学者，原则可以借鉴到其他研究。
- **Wilson 等人, "Good enough practices in scientific computing"**（2017）：面向科学计算，作者认为每个研究者都能、也应该考虑采用的最低限度做法[^wilson2017good-e1]，涵盖数据、代码、协作、目录和版本管理。
- **Sandve 等人, "Ten Simple Rules for Reproducible Computational Research"**（2013）：面向计算研究，想让每个结果都可追溯、可复现时读。
- **Schnell, "Ten Simple Rules for a Computational Biologist's Laboratory Notebook"**（2015）：想把研究日志记好时读。写给只做计算的生物学者。
- **The Turing Way, Research Compendia**：想把整个项目整理成可分享、可复现的一包时读。
- **Mineault, The Good Research Code Handbook**：写研究代码的人读，讲项目结构、git、文档。
- **OSF（Open Science Framework，开放科学框架）, "Organizing files"**：这个开放科学平台的帮助文档，是一份简短的清单，讲原始数据和派生数据分开、只读、README。

[^wilson2017good-e1]: Wilson 等人 2017，引言。[证据](../../sources/notes/wilson2017good.md#e1)
[^wilson2017good-e5]: Wilson 等人 2017，Introduction。[证据](../../sources/notes/wilson2017good.md#e5)
[^wilson2017good-e6]: Wilson 等人 2017，Project organization，4a。[证据](../../sources/notes/wilson2017good.md#e6)
[^wilson2017good-e7]: Wilson 等人 2017，Project organization，4b。[证据](../../sources/notes/wilson2017good.md#e7)
[^wilson2017good-e8]: Wilson 等人 2017，Project organization，4c。[证据](../../sources/notes/wilson2017good.md#e8)
[^wilson2017good-e9]: Wilson 等人 2017，Data management，1a。[证据](../../sources/notes/wilson2017good.md#e9)
[^wilson2017good-e10]: Wilson 等人 2017，Data management，1b。[证据](../../sources/notes/wilson2017good.md#e10)
[^wilson2017good-e11]: Wilson 等人 2017，Collaboration，3a。[证据](../../sources/notes/wilson2017good.md#e11)
[^wilson2017good-e12]: Wilson 等人 2017，Collaboration，3b。[证据](../../sources/notes/wilson2017good.md#e12)
[^wilson2017good-e13]: Wilson 等人 2017，Project organization，4f。[证据](../../sources/notes/wilson2017good.md#e13)
[^wilson2017good-e14]: Wilson 等人 2017，Keeping track of changes，5b。[证据](../../sources/notes/wilson2017good.md#e14)
[^wilson2017good-e15]: Wilson 等人 2017，Keeping track of changes，5f。[证据](../../sources/notes/wilson2017good.md#e15)
[^wilson2017good-e16]: Wilson 等人 2017，Keeping track of changes。[证据](../../sources/notes/wilson2017good.md#e16)
[^wilson2017good-e17]: Wilson 等人 2017，Keeping track of changes。[证据](../../sources/notes/wilson2017good.md#e17)
[^wilson2017good-e19]: Wilson 等人 2017，Project organization，4c。[证据](../../sources/notes/wilson2017good.md#e19)
[^wilson2017good-e20]: Wilson 等人 2017，Data management，1a。[证据](../../sources/notes/wilson2017good.md#e20)
[^wilson2017good-e21]: Wilson 等人 2017，Data management，1a。[证据](../../sources/notes/wilson2017good.md#e21)
[^noble2009quick-e1]: Noble 2009，Principles。[证据](../../sources/notes/noble2009quick.md#e1)
[^noble2009quick-e2]: Noble 2009，Principles。[证据](../../sources/notes/noble2009quick.md#e2)
[^noble2009quick-e3]: Noble 2009，File and Directory Organization。[证据](../../sources/notes/noble2009quick.md#e3)
[^noble2009quick-e4]: Noble 2009，File and Directory Organization。[证据](../../sources/notes/noble2009quick.md#e4)
[^noble2009quick-e5]: Noble 2009，File and Directory Organization。[证据](../../sources/notes/noble2009quick.md#e5)
[^noble2009quick-e6]: Noble 2009，The Lab Notebook。[证据](../../sources/notes/noble2009quick.md#e6)
[^noble2009quick-e7]: Noble 2009，The Lab Notebook。[证据](../../sources/notes/noble2009quick.md#e7)
[^noble2009quick-e8]: Noble 2009，Carrying Out a Single Experiment。[证据](../../sources/notes/noble2009quick.md#e8)
[^noble2009quick-e9]: Noble 2009，Carrying Out a Single Experiment。[证据](../../sources/notes/noble2009quick.md#e9)
[^noble2009quick-e10]: Noble 2009，Figure 1 说明。[证据](../../sources/notes/noble2009quick.md#e10)
[^sandve2013ten-e2]: Sandve 等人 2013，Rule 1。[证据](../../sources/notes/sandve2013ten.md#e2)
[^sandve2013ten-e4]: Sandve 等人 2013，Rule 4。[证据](../../sources/notes/sandve2013ten.md#e4)
[^sandve2013ten-e7]: Sandve 等人 2013，Rule 1。[证据](../../sources/notes/sandve2013ten.md#e7)
[^sandve2013ten-e8]: Sandve 等人 2013，Rule 1。[证据](../../sources/notes/sandve2013ten.md#e8)
[^sandve2013ten-e10]: Sandve 等人 2013，Rule 2。[证据](../../sources/notes/sandve2013ten.md#e10)
[^sandve2013ten-e11]: Sandve 等人 2013，Rule 4、Rule 6。[证据](../../sources/notes/sandve2013ten.md#e11)
[^sandve2013ten-e12]: Sandve 等人 2013，Rule 9。[证据](../../sources/notes/sandve2013ten.md#e12)
[^schnell2015ten-e3]: Schnell 2015，Rule 4。[证据](../../sources/notes/schnell2015ten.md#e3)
[^schnell2015ten-e9]: Schnell 2015，Rule 3。[证据](../../sources/notes/schnell2015ten.md#e9)
[^schnell2015ten-e10]: Schnell 2015，Rule 5。[证据](../../sources/notes/schnell2015ten.md#e10)
[^schnell2015ten-e4]: Schnell 2015，Rule 5。[证据](../../sources/notes/schnell2015ten.md#e4)
[^schnell2015ten-e8]: Schnell 2015，引言。[证据](../../sources/notes/schnell2015ten.md#e8)
[^turingwaycompendia-e1]: The Turing Way，Research Compendia，Summary。[证据](../../sources/notes/turingwaycompendia.md#e1)
[^turingwaycompendia-e2]: The Turing Way，Research Compendia，Summary。[证据](../../sources/notes/turingwaycompendia.md#e2)
[^turingwaycompendia-e3]: The Turing Way，Research Compendia，Structure of a Research Compendium。[证据](../../sources/notes/turingwaycompendia.md#e3)
[^turingwaycompendia-e4]: The Turing Way，Research Compendia，Basic Compendium。[证据](../../sources/notes/turingwaycompendia.md#e4)
[^mineault2021good-e1]: Mineault 2021，Setting up your project。[证据](../../sources/notes/mineault2021good.md#e1)
[^mineault2021good-e2]: Mineault 2021，Setting up your project。[证据](../../sources/notes/mineault2021good.md#e2)
[^mineault2021good-e3]: Mineault 2021，Setting up your project，git 一节。[证据](../../sources/notes/mineault2021good.md#e3)
[^mineault2021good-e4]: Mineault 2021，Document your code（引 Damian Conway）。[证据](../../sources/notes/mineault2021good.md#e4)
[^osforganizing-e1]: OSF Support，Organizing files。[证据](../../sources/notes/osforganizing.md#e1)
[^osforganizing-e2]: OSF Support，Separate raw data from derived data。[证据](../../sources/notes/osforganizing.md#e2)
[^osforganizing-e3]: OSF Support，Make raw data read-only。[证据](../../sources/notes/osforganizing.md#e3)
[^osforganizing-e4]: OSF Support，Make README files。[证据](../../sources/notes/osforganizing.md#e4)
[^mlflowtracking-e1]: MLflow 文档，MLflow Tracking（工具官方文档）。[证据](../../sources/notes/mlflowtracking.md#e1)
[^karpathy2016survival-e10]: Karpathy 2016，Writing code，"Think of the future you"。[证据](../../sources/notes/karpathy2016survival.md#e10)
[^noble2023ten-e12]: Noble 2023，Rule 9。[证据](../../sources/notes/noble2023ten.md#e12)
