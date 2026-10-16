# Kalliamvakou et al. 2014: The Promises and Perils of Mining GitHub

- Source: `kalliamvakou2014promises`, [original](https://kblincoe.github.io/publications/2014_MSR_Promises_Perils.pdf)
- Version: Paper at the Mining Software Repositories (MSR) 2014 conference; local PDF `papers/pdf/kalliamvakou2014promises.pdf`

### E1

- Location: Abstract
- Quote: "We show, for example, that the majority of the projects are personal and inactive; that GitHub is also being used for free storage and as a Web hosting service; and that almost 40% of all pull requests do not appear as merged, even though they were."
- Key point: Most GitHub projects are personal and inactive; some repositories are used only for free storage or web hosting; and almost 40% of pull requests do not appear as merged even though they were.

### E2

- Location: §4 Peril I
- Quote: "To analyze a project hosted on GitHub, one must consider the activity in both the base repository and all associated forked repositories."
- Key point: A repository is not a project; to analyze a project, you must consider activity in both the base repository and all its forks.

### E3

- Location: §4.1 Peril II, caption of Figure 1
- Quote: "The median number of commits per project is 6, and 90% of projects have less than 50 commits."
- Key point: The median number of commits per project is only 6, and 90% of projects have fewer than 50 commits.

### E4

- Location: §4.2 Peril IV
- Quote: "The purpose of a repository cannot be reliably and automatically identifed from the project metadata." / "Researchers should review the description and README file to ensure the project fits their research needs."
- Key point: A repository's purpose cannot be reliably identified automatically from its metadata; researchers should read the description and README to make sure the project fits their research needs.

### E5

- Location: §4.3 Peril V
- Quote: "67% of projects have only one committer" / "To avoid personal projects, the number of committers should be considered."
- Key point: 67% of projects have only one committer; to exclude personal projects, consider the number of committers.

### E6

- Location: §4.4.1 Peril VII
- Quote: "It is common in projects to require a commit squash (merging all different commits into a single one) before the set of commits is merged with the main repository." / "This means that at the time of analysis, the researcher can only observe the latest commit, which is the outcome of the review process."
- Key point: Many projects require squashing commits into one before merging, so researchers see only the post-review result, not the original commits made during review.

### E7

- Location: §4.4.1 Peril VIII
- Quote: "Do not rely on GitHub's merge status, rather consider using heuristics like the ones described above to improve merge detection when analyzing merged pull requests."
- Key point: Do not rely on GitHub's merge status; use heuristics to detect which pull requests were actually merged.

### E8

- Location: §4.5 Peril IX
- Quote: "Avoid projects that have a high number of committers who are not registered GitHub users and projects which explicitly state that they are mirrors in their description."
- Key point: Many active projects do not do all their development on GitHub; avoid projects with many committers who are not registered GitHub users, and projects whose description says they are mirrors.

### E9

- Location: §4.4.2
- Quote: "Many interesting repositories, especially those that migrated to GitHub, have an external issue database."
- Key point: Many repositories, especially those that migrated to GitHub, use an external issue tracker.

### E10

- Location: §6 Discussion & Conclusions
- Quote: "the best way to identify active software development projects is to consider projects that, during a recent time period, had a good balance of number of commits and pull requests, and have a number of committers and authors larger than 2." / "Outliers, especially those with a very large number of commits per committer, point towards automatic bots."
- Key point: Rule of thumb: pick projects with a good balance of recent commits and pull requests and more than two committers and authors; outliers with extremely high commits per person are often automated bots.

### E11

- Location: §6 Discussion & Conclusions
- Quote: "The data can be readily used to report on several project properties." / "Using GitHub to synthesize information to draw conclusions about more abstract constructs though needs some consideration."
- Key point: GitHub data can readily be used to report project properties, but drawing conclusions about more abstract constructs from it needs care.

### E12

- Location: §2.1 Background
- Quote: "Researchers often rely on links between bugs and commits made in commit logs, but linked bugs represent only a fraction of the entire population of fixed bugs."
- Key point: Researchers often rely on links between bugs and commits in commit logs, but linked bugs are only a fraction of all fixed bugs.

### E13

- Location: §3 Study Design; §5 Threats to Validity
- Quote: "We used the ghtorrent dataset made available in Jan 2014" / "To ameliorate these threats, we provide a replication package for our study."
- Key point: The authors state the release date of the dataset snapshot they used and provide a replication package.
