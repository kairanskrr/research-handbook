# Kalliamvakou 等人 2014：The Promises and Perils of Mining GitHub

- 资料：`kalliamvakou2014promises`，[原文](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf)
- 版本：MSR 2014 会议论文；本地 PDF `papers/pdf/kalliamvakou2014promises.pdf`

### E1

- 位置：摘要
- 原文："We show, for example, that the majority of the projects are personal and inactive; that GitHub is also being used for free storage and as a Web hosting service; and that almost 40% of all pull requests do not appear as merged, even though they were."
- 要点：GitHub 上大多数项目是个人的、不活跃的；有些仓库只是用来存文件或托管网站；近 40% 的拉取请求实际已合并，却显示为未合并。

### E2

- 位置：§4 Peril I
- 原文："To analyze a project hosted on GitHub, one must consider the activity in both the base repository and all associated forked repositories."
- 要点：一个仓库不等于一个项目；分析一个项目要同时考虑主仓库及其所有复刻（fork）仓库的活动。

### E3

- 位置：§4.1 Peril II，图 1 说明
- 原文："The median number of commits per project is 6, and 90% of projects have less than 50 commits."
- 要点：项目提交数的中位数只有 6，90% 的项目提交数少于 50。

### E4

- 位置：§4.2 Peril IV
- 原文："The purpose of a repository cannot be reliably and automatically identifed from the project metadata." / "Researchers should review the description and README file to ensure the project fits their research needs."
- 要点：仓库的用途无法从元数据可靠地自动判断；研究者要看描述和 README，确认项目符合研究需要。

### E5

- 位置：§4.3 Peril V
- 原文："67% of projects have only one committer" / "To avoid personal projects, the number of committers should be considered."
- 要点：67% 的项目只有一个提交者；要排除个人项目，应考虑提交者人数。

### E6

- 位置：§4.4.1 Peril VII
- 原文："It is common in projects to require a commit squash (merging all different commits into a single one) before the set of commits is merged with the main repository." / "This means that at the time of analysis, the researcher can only observe the latest commit, which is the outcome of the review process."
- 要点：许多项目要求合并前把多个提交压缩成一个，研究者只能看到评审之后的结果，看不到评审过程中的原始提交。

### E7

- 位置：§4.4.1 Peril VIII
- 原文："Do not rely on GitHub's merge status, rather consider using heuristics like the ones described above to improve merge detection when analyzing merged pull requests."
- 要点：不要依赖 GitHub 显示的"已合并"状态，应使用启发式规则来识别实际被合并的拉取请求。

### E8

- 位置：§4.5 Peril IX
- 原文："Avoid projects that have a high number of committers who are not registered GitHub users and projects which explicitly state that they are mirrors in their description."
- 要点：很多活跃项目不在 GitHub 上完成全部开发；要避开大量提交者不是 GitHub 注册用户的项目，以及描述中写明是镜像的项目。

### E9

- 位置：§4.4.2
- 原文："Many interesting repositories, especially those that migrated to GitHub, have an external issue database."
- 要点：许多仓库，特别是迁移到 GitHub 的仓库，使用外部的问题跟踪系统。

### E10

- 位置：§6 Discussion & Conclusions
- 原文："the best way to identify active software development projects is to consider projects that, during a recent time period, had a good balance of number of commits and pull requests, and have a number of committers and authors larger than 2." / "Outliers, especially those with a very large number of commits per committer, point towards automatic bots."
- 要点：经验法则：选近期提交和拉取请求都较多、提交者和作者超过 2 人的项目；人均提交数极高的离群值往往是自动化机器人。

### E11

- 位置：§6 Discussion & Conclusions
- 原文："The data can be readily used to report on several project properties." / "Using GitHub to synthesize information to draw conclusions about more abstract constructs though needs some consideration."
- 要点：GitHub 数据可以直接用来描述项目属性；但要用它对更抽象的概念下结论，就需要谨慎。

### E12

- 位置：§2.1 Background
- 原文："Researchers often rely on links between bugs and commits made in commit logs, but linked bugs represent only a fraction of the entire population of fixed bugs."
- 要点：研究者常依赖提交日志里缺陷和提交之间的链接，但能链接上的缺陷只是全部已修复缺陷的一部分。

### E13

- 位置：§3 Study Design；§5 Threats to Validity
- 原文："We used the ghtorrent dataset made available in Jan 2014" / "To ameliorate these threats, we provide a replication package for our study."
- 要点：作者写明了所用数据集快照的发布时间，并提供了复现包。
