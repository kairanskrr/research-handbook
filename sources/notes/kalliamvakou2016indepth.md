# Kalliamvakou 等人 2016：An in-depth study of the promises and perils of mining GitHub

- 资料：`kalliamvakou2016indepth`，[原文](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf)
- 版本：Empirical Software Engineering 21(5), 2016（作者自存版）；本地 PDF `papers/pdf/kalliamvakou2016indepth.pdf`

### E1

- 位置：§4.7 Peril X
- 原文："In other words, 47 % of Torvalds' commits in GitHub are not associated with his user account." / "For empirical studies that need to map activity to specific users, use heuristics for email unification to improve the validity of the results."
- 要点：同一个人可能用多个邮箱提交，例如 Linus Torvalds 在 GitHub 上 47% 的提交没有关联到他的账号；需要把活动对应到人时，要做邮箱合并（身份合并）。

### E2

- 位置：§4.7 Peril XI
- 原文："This peril is unavoidable when using data from public Websites—acknowledging this partial view in the discussion of results and replicating a study in other contexts can help reduce its impact."
- 要点：公开网站只能看到公开活动，这个问题无法避免；应在讨论中承认只看到了局部，并在其他情境中重复研究。

### E3

- 位置：§4.8 Peril XII
- 原文："While the repositories hosted in GitHub are continuously evolving, GitHub reports only their current state (via its API)." / "When a repository is deleted, all of its events and metadata are lost"
- 要点：GitHub 的接口只报告仓库的当前状态，不报告历史事件；仓库被删除后，它的事件和元数据全部丢失。

### E4

- 位置：§4.8 Peril XII
- 原文："When commits are rebased (one or more commits changes its metadata, or are modified and/or combined into new commits) the old commits disappear from the repository and are replaced by the new commits."
- 要点：提交被变基（rebase）后，旧提交从仓库中消失，被新提交取代。

### E5

- 位置：§4.8 Peril XII
- 原文："Obtaining data from one of the services which archives data from the GitHub API (like GHTORRENT) can help avoid this peril. However, researchers should be aware that such services contain their own assumptions regarding the collected data."
- 要点：使用持续存档 GitHub 数据的服务（如 GHTorrent）可以缓解这个问题，但要清楚这些服务自身也带有采集假设。

### E6

- 位置：§4.8 Peril XIII
- 原文："First, the meaning of “watchers” is different before and after August 2012." / "Understand how both the GitHub API and the Website have evolved over time."
- 要点：平台在不断变化，例如"关注者（watchers）"的含义在 2012 年 8 月前后不同；要了解接口和网站随时间的变化。

### E7

- 位置：§4.9 Relationship Between Perils
- 原文："Have many committers, and" / "Had recent activity, and" / "Have a large number of commits." / "In our experience bot-users tend to commit to a single repository."
- 要点：选择活跃项目的建议：提交者多、近期有活动、提交数多；机器人账号往往只向单个仓库提交。

### E8

- 位置：§5.2 The Papers
- 原文："The analysis considered merged pull requests as successful, while marked-as-non-merged as unsuccessful." / "This issue could have impacted the results in the paper"
- 要点：有研究直接用平台的"已合并"标记区分拉取请求成败，而许多拉取请求实际已合并却未被标记，这可能影响了其结论。

### E9

- 位置：§6 Comparing Perils Between SourceForge and GitHub
- 原文："We also concluded that the simplicity of metrics may hide dangers"
- 要点：容易计算的指标可能隐藏风险，例如拉取请求中的提交数并不能代表合并所花的工夫。

### E10

- 位置：§6 Comparing Perils Between SourceForge and GitHub
- 原文："Researchers need to be conscious of the data skewness and the fact that they will need to use screening variables to get data that is relevant to and representative of the properties they want to study, but also that the use of screening variables will significantly reduce the number of repositories and projects studied."
- 要点：数据高度偏斜，需要用筛选变量挑出相关的数据，但筛选会大幅减少可研究的仓库数量。

### E11

- 位置：§8 Discussion & Conclusions
- 原文："Mined data does not always tell the whole story." / "One last conclusion point is to advocate complementing quantitative studies with qualitative data."
- 要点：挖掘出的数据并不总能讲出全部故事；建议用定性数据补充定量研究。

### E12

- 位置：§8 Discussion & Conclusions
- 原文："The take-away message is that perils in the data equals perils in assumptions equals perils in results."
- 要点：数据里的陷阱就是假设里的陷阱，也就是结果里的陷阱。
