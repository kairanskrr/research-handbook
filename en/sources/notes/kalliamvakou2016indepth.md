# Kalliamvakou et al. 2016: An in-depth study of the promises and perils of mining GitHub

- Source: `kalliamvakou2016indepth`, [original](https://kblincoe.github.io/publications/2015_EMSE_GitHubPerils.pdf)
- Version: Empirical Software Engineering 21(5), 2016 (author's self-archived version); local PDF `papers/pdf/kalliamvakou2016indepth.pdf`

### E1

- Location: §4.7 Peril X
- Quote: "In other words, 47 % of Torvalds' commits in GitHub are not associated with his user account." / "For empirical studies that need to map activity to specific users, use heuristics for email unification to improve the validity of the results."
- Key point: One person may commit under several email addresses; for example, 47% of Linus Torvalds's commits on GitHub are not linked to his account. If you need to map activity to people, use email (identity) unification heuristics.

### E2

- Location: §4.7 Peril XI
- Quote: "This peril is unavoidable when using data from public Websites—acknowledging this partial view in the discussion of results and replicating a study in other contexts can help reduce its impact."
- Key point: Public websites show only public activity, and this is unavoidable; acknowledge the partial view when discussing results, and replicate the study in other contexts.

### E3

- Location: §4.8 Peril XII
- Quote: "While the repositories hosted in GitHub are continuously evolving, GitHub reports only their current state (via its API)." / "When a repository is deleted, all of its events and metadata are lost"
- Key point: GitHub's API reports only a repository's current state, not its history; when a repository is deleted, all its events and metadata are lost.

### E4

- Location: §4.8 Peril XII
- Quote: "When commits are rebased (one or more commits changes its metadata, or are modified and/or combined into new commits) the old commits disappear from the repository and are replaced by the new commits."
- Key point: When commits are rebased, the old commits disappear from the repository and are replaced by new ones.

### E5

- Location: §4.8 Peril XII
- Quote: "Obtaining data from one of the services which archives data from the GitHub API (like GHTORRENT) can help avoid this peril. However, researchers should be aware that such services contain their own assumptions regarding the collected data."
- Key point: Services that continuously archive GitHub data (such as GHTorrent) can mitigate this, but they carry their own assumptions about the collected data.

### E6

- Location: §4.8 Peril XIII
- Quote: "First, the meaning of “watchers” is different before and after August 2012." / "Understand how both the GitHub API and the Website have evolved over time."
- Key point: The platform keeps changing; for example, the meaning of "watchers" differs before and after August 2012. Understand how the API and website have evolved over time.

### E7

- Location: §4.9 Relationship Between Perils
- Quote: "Have many committers, and" / "Had recent activity, and" / "Have a large number of commits." / "In our experience bot-users tend to commit to a single repository."
- Key point: To select active projects, look for many committers, recent activity, and many commits; bot accounts tend to commit to a single repository.

### E8

- Location: §5.2 The Papers
- Quote: "The analysis considered merged pull requests as successful, while marked-as-non-merged as unsuccessful." / "This issue could have impacted the results in the paper"
- Key point: One study used the platform's "merged" flag to separate successful from unsuccessful pull requests, yet many pull requests are merged without being flagged, which may have affected its results.

### E9

- Location: §6 Comparing Perils Between SourceForge and GitHub
- Quote: "We also concluded that the simplicity of metrics may hide dangers"
- Key point: Simple metrics can hide dangers; for example, the number of commits in a pull request does not reflect the effort needed to merge it.

### E10

- Location: §6 Comparing Perils Between SourceForge and GitHub
- Quote: "Researchers need to be conscious of the data skewness and the fact that they will need to use screening variables to get data that is relevant to and representative of the properties they want to study, but also that the use of screening variables will significantly reduce the number of repositories and projects studied."
- Key point: The data are highly skewed, so you need screening variables to get relevant data, but screening greatly reduces the number of repositories you can study.

### E11

- Location: §8 Discussion & Conclusions
- Quote: "Mined data does not always tell the whole story." / "One last conclusion point is to advocate complementing quantitative studies with qualitative data."
- Key point: Mined data does not always tell the whole story; the authors advocate complementing quantitative studies with qualitative data.

### E12

- Location: §8 Discussion & Conclusions
- Quote: "The take-away message is that perils in the data equals perils in assumptions equals perils in results."
- Key point: Perils in the data equal perils in assumptions equal perils in results.
