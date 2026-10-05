# Wilson 等人 2017：Good enough practices in scientific computing

- 资料：`wilson2017good`，本地 PDF `papers/pdf/wilson2017good.pdf`
- 版本：PLoS Computational Biology 13(6): e1005510, 2017，开放获取

### E1

- 位置：引言
- 原文："a minimum set of tools and techniques that we believe every researcher can and should consider adopting"
- 要点：这篇文章给的是每个研究者都能、也应该考虑采用的最低限度做法。

### E2

- 位置：引言
- 原文："the collaborator every researcher cares about most: their future self" / "yourself from 3 months ago doesn’t answer email"
- 要点：这些做法最大的受益者是未来的自己：三个月前的你不会回邮件。

### E3

- 位置：Box 1，数据管理
- 原文："Save the raw data." / "Ensure that raw data are backed up in more than one location." / "Record all the steps used to process data."
- 要点：保存原始数据；原始数据至少备份在两个地方；记录处理数据的每一步。

### E4

- 位置：Box 1，数据管理与协作
- 原文："Submit data to a reputable DOI-issuing repository so that others can access and cite it." / "Make the license explicit."
- 要点：把数据提交到能分配 DOI（数字对象标识符）的可靠仓库，让别人能获取和引用；明确许可协议。

### E5

- 位置：Introduction
- 原文："Many of our recommendations are for the benefit of the collaborator every researcher cares about most: their future self (as the joke goes, yourself from 3 months ago doesn’t answer email"
- 要点：这些做法最大的受益者是未来的自己：三个月前的你不会回邮件。

### E6

- 位置：Project organization，4a
- 原文："Put each project in its own directory, which is named after the project (4a). [...] As a rule of thumb, divide work into projects based on the overlap in data and code files."
- 要点：每个项目放在以项目命名的独立目录里；按数据和代码的重叠程度划分项目。

### E7

- 位置：Project organization，4b–4d
- 原文："Put text documents associated with the project in the doc directory (4b). This includes files for manuscripts, documentation for source code, and/or an electronic lab notebook recording your experiments."
- 要点：与项目相关的文字材料（稿件、代码文档、记录实验的电子实验记录本）放在 doc 目录。

### E8

- 位置：Project organization，4c
- 原文："Put raw data and metadata in a data directory and files generated during cleanup and analysis in a results directory (4c)"
- 要点：原始数据和元数据放 data 目录；清洗和分析中生成的文件放 results 目录。

### E9

- 位置：Data management，1a
- 原文："Save the raw data (1a). [...] Consider changing file permissions to read-only or using spreadsheet protection features so that it is harder to damage raw data by accident or to hand edit it in a moment of weakness."
- 要点：保存原始数据；可以把原始数据设为只读，防止误损或一时冲动手工修改。

### E10

- 位置：Data management，1b
- 原文："Ensure that raw data are backed up in more than one location (1b)."
- 要点：原始数据至少备份在两个地方。

### E11

- 位置：Collaboration，3a
- 原文："Create an overview of your project (3a). Have a short file in the project’s home directory that explains the purpose of the project."
- 要点：在项目根目录放一个简短的概述文件（通常叫 README），说明项目的目的。

### E12

- 位置：Collaboration，3b
- 原文："Create a shared "to-do" list (3b). This can be a plain text file called something like notes.txt or todo.txt"
- 要点：建一份待办清单，纯文本文件就可以。

### E13

- 位置：Project organization，4f
- 原文："Name all files to reflect their content or function (4f). [...] Do not use sequential numbers (e.g., result1.csv, result2.csv) or a location in a final manuscript (e.g., fig_3_a.png), since those numbers will almost certainly change as the project evolves."
- 要点：文件名要反映内容或功能；不要用流水号或在稿件中的位置命名，这些编号几乎一定会变。

### E14

- 位置：Keeping track of changes，5b
- 原文："Keep changes small (5b). [...] As a rule of thumb, a good size for a single change is a group of edits that you could imagine wanting to undo in one step at some point in the future."
- 要点：每次改动要小；合适的大小是"将来可能想一步撤销的一组修改"。

### E15

- 位置：Keeping track of changes，5f
- 原文："Add a file called CHANGELOG.txt to the project’s docs subfolder (5f), and make dated notes about changes to the project in this file in reverse chronological order (i.e., most recent first). This file is the equivalent of a lab notebook"
- 要点：用一个按日期倒序记录的变更日志文件，相当于实验记录本。

### E16

- 位置：Keeping track of changes，版本控制的好处
- 原文："Instead of relying on users to choose sensible names for backup copies, the version control system timestamps all saved changes automatically."
- 要点：版本控制自动给每次保存打时间戳，不再依赖人给备份副本起合理的名字。

### E17

- 位置：Keeping track of changes，What not to put under version control
- 原文："Keeping intermediate data files and other results under version control is also not necessary if you can regenerate them from raw data and software."
- 要点：中间数据和结果如果能从原始数据和程序重新生成，就不必放进版本控制。

### E18

- 位置：Project organization，Box 3 之后的说明
- 原文："The doc directory contains 2 text files written in Markdown, 1 containing a running lab notebook describing various ideas for the project and how these were implemented, and the other containing a running draft of a manuscript describing the project findings."
- 要点：示例项目的 doc 目录里有两份持续更新的文件：一份实验记录本，一份论文草稿。

### E19

- 位置：Project organization，4c
- 原文："Intermediate files such as cleaned data, statistical tables, and final publication-ready figures or tables should be separated clearly by file-naming conventions or placed into different subdirectories; those belonging to different papers or other publications should be grouped together."
- 要点：results 下按类型分开中间文件和可发表的图表，属于不同论文的结果分组存放。
