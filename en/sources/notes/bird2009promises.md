# Bird et al. 2009: The Promises and Perils of Mining Git

- Source: `bird2009promises`, [Original](https://microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009ppm.pdf)
- Version: MSR 2009 conference paper; local PDF `papers/pdf/bird2009promises.pdf`

### E1

- Location: §1 Introduction
- Quote: "In the course of mining and analysis, we suffered many setbacks and came to false inital conclusions due to incomplete understandings about the data and what processes led to the data we observed."
- Key point: The authors themselves suffered many setbacks while mining and first reached false conclusions, because they did not fully understand the data and the processes that produced it.

### E2

- Location: §3 Peril 4
- Quote: "Git history is revisionist: a repository owner can rewrite it." / "Thus, the history in a git repository (especially a stable official project repository) may not reflect what actually happened to arrive at that particular state."
- Key point: Git history can be rewritten (for example by rebasing or squashing commits), so the history in a repository, especially a stable official one, may not reflect how development actually happened.

### E3

- Location: §3 Peril 5
- Quote: "You cannot always determine what branch a commit was made on."
- Key point: You cannot always tell which branch a commit was made on.

### E4

- Location: §3 Peril 6
- Quote: "It is not always possible to track the source of a merge or even determine if a merge occurred." / "In this scenario no merge commit is created."
- Key point: You cannot always trace the source of a merge, or even tell whether a merge happened; a fast-forward merge, for example, creates no merge commit.

### E5

- Location: §3 Peril 7
- Quote: "The accessible data may only contain commits that are success selected."
- Key point: The accessible data may contain only the commits that were accepted; rejected or rewritten work is invisible.

### E6

- Location: §5 Analysis
- Quote: "However, researchers should perform similar analyses when interpreting and reporting results based on sources of merges."
- Key point: The authors measured the recall of their heuristic for identifying merge sources (about 98%) and recommend that other researchers run a similar check whenever they rely on such heuristics.

### E7

- Location: §5 Analysis
- Quote: "Although statistically significant, the magnitude of the difference was uninteresting (only 2 lines less per commit)."
- Key point: The difference in commit size before and after moving to git was statistically significant but only 2 lines per commit, so of little practical interest.
