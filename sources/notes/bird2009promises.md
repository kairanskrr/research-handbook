# Bird 等人 2009：The Promises and Perils of Mining Git

- 资料：`bird2009promises`，[原文](https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf)
- 版本：MSR 2009 会议论文；本地 PDF `papers/pdf/bird2009promises.pdf`

### E1

- 位置：§1 Introduction
- 原文："In the course of mining and analysis, we suffered many setbacks and came to false inital conclusions due to incomplete understandings about the data and what processes led to the data we observed."
- 要点：作者自己在挖掘中多次受挫，因为没有完全理解数据以及数据是怎样产生的，一开始得出了错误结论。

### E2

- 位置：§3 Peril 4
- 原文："Git history is revisionist: a repository owner can rewrite it." / "Thus, the history in a git repository (especially a stable official project repository) may not reflect what actually happened to arrive at that particular state."
- 要点：git 历史可以被改写（如变基、压缩提交），所以仓库里的历史，尤其是官方稳定仓库的历史，未必反映真实发生的开发过程。

### E3

- 位置：§3 Peril 5
- 原文："You cannot always determine what branch a commit was made on."
- 要点：并不总能确定一个提交是在哪个分支上做的。

### E4

- 位置：§3 Peril 6
- 原文："It is not always possible to track the source of a merge or even determine if a merge occurred." / "In this scenario no merge commit is created."
- 要点：不一定能追踪合并的来源，甚至不一定能判断发生过合并；例如快进合并（fast-forward）不会留下合并提交。

### E5

- 位置：§3 Peril 7
- 原文："The accessible data may only contain commits that are success selected."
- 要点：能拿到的数据可能只包含"被接受"的提交，被拒绝或被重写的工作看不到。

### E6

- 位置：§5 Analysis
- 原文："However, researchers should perform similar analyses when interpreting and reporting results based on sources of merges."
- 要点：作者测量了自己识别合并来源的启发式规则的召回率（约 98%），并建议其他研究者在依赖类似规则时也做同样的检验。

### E7

- 位置：§5 Analysis
- 原文："Although statistically significant, the magnitude of the difference was uninteresting (only 2 lines less per commit)."
- 要点：迁移到 git 前后的提交大小差异虽然统计显著，但只差每次提交 2 行，实际意义不大。
