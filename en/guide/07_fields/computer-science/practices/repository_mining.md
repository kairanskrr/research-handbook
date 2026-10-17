# Mining software repositories: getting data from code repositories, bug trackers, and Q&A sites

This page covers **mining software repositories**: you write programs to extract data at scale from code repositories, bug trackers, mailing lists, Q&A sites, and similar sources, then analyze it quantitatively to learn how software actually gets built.

**Scope**: this is how it is done in computer science; the examples and standards come mainly from empirical software engineering. Repository mining most often serves the [Description](../../../05_research-strategies/observe_describe.md) research strategy: finding out what actually happens in software development. When you use it to test whether "X causes Y", it must also meet the requirements of [Causal explanation](../../../05_research-strategies/explain_causality.md). The parts of these two strategies that hold in every field are on the strategy pages; this page covers only what is specific to mining software data.

If you just want to collect data from GitHub to train or evaluate a model, Section 2 of this page still applies to the data collection; how to evaluate the model itself is in [Benchmarking](benchmarking.md); general principles of validity are in [Validity and limitations](../../../02_do-the-project/04_validity-and-limits.md).

**After reading this page, you should be able to:**

- judge whether your question suits repository mining, and how far mining can answer it;
- carry out a mining study step by step: choose data sources, filter projects, extract and clean, link data, label manually, and analyze;
- recognize the most common perils in git and GitHub data;
- check your own study against the checklist at the end.

---

## 1. What this kind of research is, and when to use it

The ACM SIGSOFT Empirical Standards (from the Association for Computing Machinery's Special Interest Group on Software Engineering) define it as research that quantitatively analyzes datasets extracted from platforms hosting structured or semi-structured text, such as source code repositories[^ralph2020empirical-e105]. Common data sources include code repositories, mailing list archives, bug tracking systems, Q&A forums, and chat platforms[^ralph2020empirical-e106].

**Questions it answers well**:

- **Descriptive questions**: how widely a language, tool, or practice is used, and how large commits and contributions are. Data from platforms like GitHub can be used directly to describe project properties[^kalliamvakou2014promises-e11].
- **Relationship questions**: which factors are **correlated** with outcomes such as bugs, merge speed, or contributor turnover.
- **Leads for later research**: first find patterns across many projects, then explain them with experiments or interviews.

**Know its limits**:

- **It usually gives you correlation, not causation.** Seeing that "code written in a certain style has more bugs" only shows the two are correlated; to believe there is a causal link, you need follow-up experiments that actively change the coding style[^menzies2019bad-e10]. The SIGSOFT standards list "establishing causality (for example, with longitudinal analysis)" as Extraordinary, not Essential[^ralph2020empirical-e117]; from this we infer that an ordinary mining study is by default expected to give only correlations. A common **confounder** (a third factor that affects two variables and makes them look related) is project size: large projects have more commits, more contributors, and more bug reports, so many metrics that seem related are really just reflecting size.
- **The data doesn't tell the whole story.** Mined data is only the trace that development activity leaves behind[^kalliamvakou2016indepth-e11]; be especially careful when you draw conclusions about abstract concepts such as "collaboration", "quality", or "popularity" from it[^kalliamvakou2014promises-e11].

**How it differs from similar kinds of study:**

| | Repository mining | Case study | Data science / predictive modeling | Qualitative content analysis |
|---|---|---|---|---|
| What is studied | Many repositories, extracted in bulk by programs | A few projects with rich context | Models trained on data | A small amount of text, read closely by hand |
| Main analysis | Quantitative statistics | Several kinds of evidence to understand one setting in depth | Predictive performance | Coding and identifying themes |
| Typical question | "How common is it? What is it related to?" | "Why does this happen here?" | "Can we predict it?" | "What are people saying, and how?" |

Basis: the scope section of the SIGSOFT repository mining standard (the data science and case study columns)[^ralph2020empirical-e107]; the rest of the comparison is our own.

**How to choose**: when your question needs "patterns across many projects", use repository mining; when you need to understand "why", combine it with interviews, questionnaires, or case studies. If you study only two or three projects, follow the requirements for case studies, and don't state conclusions as if you had a large sample.

Similar research exists in other areas of computing, for example mining commit histories for vulnerability fixes in security, or building datasets from GitHub code and issue reports in machine learning. The perils below apply to them as well.

---

## 2. How to do it

### Step 1: State the research question and the unit of analysis

First explain why this question suits repository mining, then define the **unit of analysis**: what exactly counts as "one" when you count. Is it a repository, a project, a commit, a pull request, or a developer[^ralph2020empirical-e108]?

**Where people go wrong:** treating a "repository" as a "project". On GitHub a project often consists of a main repository plus many forks, and if you analyze projects you need to consider them together[^kalliamvakou2014promises-e2]. Likewise, "one developer" is not the same as "one account" or "one email address" (see Step 4).

### Step 2: Choose your data source, and justify it

Say which platform you use and why it fits your question[^ralph2020empirical-e109]. Check one thing in particular: **does the activity you care about really all happen on this platform?**

- Some repositories are just mirrors of repositories hosted elsewhere[^kalliamvakou2014promises-e8]; some projects, especially those that migrated to GitHub, use an external issue tracker[^kalliamvakou2014promises-e9].
- When you need **all** of a project's commits, looking only at its GitHub repository is an antipattern, because it may not contain all of them[^ralph2020empirical-e121].
- Public platforms show only public activity; work in private repositories is invisible. You can't avoid this; acknowledge it in your discussion, and where possible replicate the study in other settings[^kalliamvakou2016indepth-e2].

**Use an existing dataset or crawl your own?** The GitHub API reports only the **current state**, not historical events; once a repository is deleted, its events and metadata are gone[^kalliamvakou2016indepth-e3]. Data services that archive continuously (such as GHTorrent) fill this gap, but they carry their own collection assumptions, so read their documentation before you use them[^kalliamvakou2016indepth-e5].

### Step 3: Filter and sample projects

This is the step where mining studies most often go wrong.

**First state your sampling goal and population.** Which projects do you want your conclusions to cover? "All open-source projects", or "active Java libraries on GitHub"? Write the sampling procedure as a multi-stage algorithm: which list you start from, which criteria remove which items at each stage, and what bias each stage might introduce[^baltes2022sampling-e12][^ralph2020empirical-e127].

**You must filter.** Most projects on GitHub are personal and inactive, and some repositories are used only to store files or host websites[^kalliamvakou2014promises-e1]; the median number of commits per project is just 6[^kalliamvakou2014promises-e3]. Using open-source repositories without any selection criteria is convenience sampling[^ralph2020empirical-e120], that is, choosing subjects because they are easy to get, which threatens how far your conclusions generalize[^baltes2022sampling-e2]. Common filters:

- **Personal projects**: look at the number of committers; 67% of projects have only one committer[^kalliamvakou2014promises-e5].
- **Inactive projects**: check for recent commits, pull requests, or issue reports[^kalliamvakou2016indepth-e7].
- **Repositories that aren't software development**: a repository's purpose can't be reliably determined from metadata automatically; read the description and the README (the repository's documentation file)[^kalliamvakou2014promises-e4].
- **Mirrors and forks**: avoid projects whose description says they are mirrors, and projects where many committers are not registered users of the platform[^kalliamvakou2014promises-e8]; either exclude forks or merge them into the project they belong to[^kalliamvakou2014promises-e2].
- **Rule of thumb**: choose projects with a good number of recent commits and pull requests, and more than 2 committers and authors[^kalliamvakou2014promises-e10].

**Validate your filters.** Manually check a sample of what the automatic filters produced: is what remained what you wanted, and was what you removed supposed to go[^ralph2020empirical-e109]?

**Where people go wrong:**

- **Assuming a large sample is representative.** If the **sampling frame** (the list you actually sample from) is biased, no sample size can make up for it[^baltes2022sampling-e5]. Randomly sampling from a "purposively selected subset" doesn't show that it represents software in general either[^baltes2022sampling-e16][^ralph2020empirical-e37].
- **Assuming stricter filtering is always better.** Filtering sharply reduces the number of projects you can study[^kalliamvakou2016indepth-e10], and it also makes your conclusions apply only to the kind of project that remains.

**Remedies**: any data source can be biased in non-obvious ways[^baltes2022sampling-e14]. Where possible, use **probability sampling** (every item in the population has a known, nonzero chance of being selected, as in random sampling)[^ralph2020empirical-e114]; if you worry that a platform is biased, replicate the study on another platform, for example checking a pattern found on GitHub again on SourceForge[^baltes2022sampling-e13].

### Step 4: Extract and clean the data

Record every preprocessing step[^ralph2020empirical-e110]. Ideally, write an extraction process (scripts or a pipeline) that can be rerun from scratch, with the raw data kept read-only and everything else regenerable; see [Organizing research materials](../../../08_throughout/organizing_materials.md#2-raw-data-is-read-only-everything-else-can-be-regenerated).

Research that depends heavily on data must stay alert to data quality at all times[^menzies2019bad-e11]. When cleaning, go through these known perils one by one and decide whether each could affect your question:

**Perils in git history**

- **History can be rewritten.** Through operations such as rebasing and squashing commits, the history in a repository may not reflect how development really happened, especially in official stable repositories[^bird2009promises-e2]. Old commits that were rebased disappear from the repository[^kalliamvakou2016indepth-e4].
- **You only see "successful" commits.** Rejected or rewritten work is often missing from the history[^bird2009promises-e5]. Many projects require commits to be squashed before merging, so you only see the result after review[^kalliamvakou2014promises-e6].
- **Branch and merge information is incomplete.** You can't always tell which branch a commit was made on[^bird2009promises-e3]; a **fast-forward merge** (git simply moves the branch pointer to the new commit without creating a merge commit) leaves no merge commit, and sometimes you can't even tell that a merge happened[^bird2009promises-e4].

**Perils in GitHub data**

- **The "merged" flag can't be trusted.** Nearly 40% of all pull requests were in fact merged but appear as unmerged[^kalliamvakou2014promises-e1]; our guess is that one reason is that many projects merge outside the platform. Don't rely on this flag; use heuristics to identify actual merges[^kalliamvakou2014promises-e7]. Some studies have used this flag directly to separate successful from unsuccessful pull requests, and their conclusions may be affected as a result[^kalliamvakou2016indepth-e8].
- **One person, several identities.** The same person may commit under several email addresses; for example, 47% of Linus Torvalds's commits on GitHub are not linked to his account. When you need to attribute activity to people, you have to merge identities[^kalliamvakou2016indepth-e1].
- **Bot accounts.** Outliers with extremely high commit counts per person are often automated bots[^kalliamvakou2014promises-e10], and they often commit to only a single repository[^kalliamvakou2016indepth-e7]. When you study what *people* do, identify and exclude them.
- **The platform itself changes.** For example, "watchers" meant something different before and after August 2012; learn how the API and the website have changed over time[^kalliamvakou2016indepth-e6]. A trend that spans such a date may just be an artifact of the platform redesign.

**Why be so fussy?** Bird et al. admit that they themselves reached wrong conclusions at first because they didn't fully understand how their data was produced[^bird2009promises-e1]. Perils in the data are perils in your assumptions, and so perils in your results[^kalliamvakou2016indepth-e12].

**Test your tools, too.** Your extraction scripts can have bugs; the SIGSOFT standards list testing your own tools and analyzing the cases where tools fail as Desirable[^ralph2020empirical-e115].

### Step 5: Link data from different sources

Many questions require you to connect commits with issue reports, pull requests, and review comments, for example "which commits fixed bugs?"

**The usual approach**: search commit messages for bug IDs in a particular format, exclude false matches such as version numbers and years, confirm the ID exists in the bug tracker, then check whether the bug had fix activity within a few days of the commit[^bird2009fair-e4].

**Where people go wrong:**

- **The links themselves are incomplete, and biased.** There is no uniform or enforced practice for linking code changes to the bug tracker[^bird2009fair-e2]; the bugs that can be linked are only a fraction of all fixed bugs[^kalliamvakou2014promises-e12], and that fraction is systematically biased[^bird2009fair-e1]. For example, if experienced developers are more careful about marking their fixes, data like this could lead to the false conclusion that "more experienced developers make more mistakes"[^bird2009fair-e3].
- **Category labels are unreliable.** Herzig et al. manually inspected issue reports and found that 33.8% of reports labeled "bug" were really feature requests, documentation updates, or refactoring; on average, 39% of files marked as defective never actually had a bug[^herzig2013bug-e1]. Filtering "bugs" with a database query looks easy, but it assumes the classification is accurate[^herzig2013bug-e2].

**How:** manually check a sample of the automatically linked and classified results, looking for both false positives and false negatives[^bird2009fair-e5]. When you use heuristics to identify where merges came from, check their recall (how many of the real merges they catch)[^bird2009promises-e6]; the same goes for other heuristics, such as those for merging identities. Report data quality as a threat to validity in your paper[^herzig2013bug-e5].

### Step 6: Label data manually, and check agreement

Many mining studies need human judgment: is this report a bug? Which category does this comment belong to? The more contestable the judgment, the more you need multiple raters[^ralph2020empirical-e128].

**How:**[^ralph2020empirical-e111][^ralph2020empirical-e129]

1. Write a coding scheme and decision rules, and publish them with your paper. The boundaries between categories are often unclear in themselves, and a different set of rules gives different results; Herzig et al. dealt with this by publishing their complete classification rules verbatim[^herzig2013bug-e4].
2. Have two or more raters label **independently**. Herzig et al. had a second person review reclassified reports without knowing the first person's verdict, and ran a third check on any conflicts[^herzig2013bug-e3].
3. Report how many raters there were, the labeling procedure, and how disagreements were resolved.
4. Report agreement with an appropriate statistic, such as Cohen's kappa (a statistic for how well two raters agree) or Krippendorff's alpha (a similar statistic that works for more than two raters)[^ralph2020empirical-e130].
5. Even better, iterate: label a portion, resolve disagreements, revise the rules, and repeat until agreement reaches a threshold, then label the rest[^ralph2020empirical-e131].

**Where people go wrong:** calling agreement "good" when it is below accepted thresholds; computing several agreement statistics and reporting only the best-looking one[^ralph2020empirical-e132].

### Step 7: Analyze, and state the threats to validity

General statistical and validity issues are covered in [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md) and [Validity and limitations](../../../02_do-the-project/04_validity-and-limits.md). Mining studies need extra care on these points:

- **Validate your metrics.** Explain and justify every metric you use, and preferably use metrics others have validated[^ralph2020empirical-e112]. Using an unvalidated, one-dimensional metric for a multidimensional concept, such as GitHub stars as "popularity", is an antipattern[^ralph2020empirical-e119]. Metrics that are easy to compute often hide risks[^kalliamvakou2016indepth-e9].
- **With large samples, significant does not mean important.** The reasoning and examples are in [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value). An example from mining: Bird et al. found that the change in commit size before and after moving to git was statistically significant, but amounted to just 2 lines per commit[^bird2009promises-e7]. Report effect sizes, not just p-values.
- **Keep your conclusions within the repositories you chose.** Generalizing beyond the selected repositories is an antipattern[^ralph2020empirical-e122]. Discuss the threats to external validity (whether conclusions extend beyond what you studied; see [Validity and limitations](../../../02_do-the-project/04_validity-and-limits.md#5-external-validity-how-far-do-your-conclusions-reach)) that come from your data sources, repositories, and selection criteria[^ralph2020empirical-e113]; once you've acknowledged a limitation, don't write your conclusions as if it weren't there[^ralph2020empirical-e66].
- **Don't stop at description.** Purely quantitative description without testing or building theory is an antipattern[^ralph2020empirical-e122].
- **Supplement with qualitative data.** Use interviews, questionnaires, or manual inspection to check your assumptions about the data[^kalliamvakou2016indepth-e11]; SIGSOFT also lists **triangulation** across data sources or researchers (using several sources or several researchers to cross-check the same conclusion) as Desirable[^ralph2020empirical-e115].

### Step 8: Handle ethics and licensing

Most mined data was left by people: committers' names and email addresses, comments, Q&A posts. Being publicly visible doesn't mean it's free to use however you like. General principles for research involving people are in [Research integrity and ethics](../../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); the points below are specific to mining.

- **"Technically available" is not "legitimately available".** Using data merely because you can access and download it is an antipattern[^ralph2020empirical-e135]. State the grounds on which the data was legitimately available to you for research[^ralph2020empirical-e133], for example a site's terms of use that explicitly allow scraping such information for research purposes[^ralph2020empirical-e134].
- **Assess risk and privacy.** Describe possible risks or harms to data custodians and data subjects[^ralph2020empirical-e133]; when you combine several datasets, explain how you mitigate the additional privacy risks[^ralph2020empirical-e136].
- **Watch out for re-identification.** If you quote an "anonymous" comment verbatim in your paper, anyone with a search engine may be able to find its author[^ralph2020empirical-e137]. When you need to quote, consider paraphrasing or removing searchable details.
- **When you republish data, respect the original terms.** When you release your dataset, explain how you respect the data subjects' expectations and consent[^ralph2020empirical-e138]. If the dataset includes code, also check whether the original code's open-source license allows redistribution; if unsure, release only identifiers (repository names and commit hashes) plus scripts, and let others download the data themselves `[To be confirmed]`.
- Withholding some details of a dataset for ethical reasons is acceptable[^ralph2020empirical-e118].

### Step 9: Make the study reproducible

Mining data changes: repositories get deleted, histories get rewritten, and platform APIs change too[^kalliamvakou2016indepth-e3][^kalliamvakou2016indepth-e4][^kalliamvakou2016indepth-e6]. A year later, the same scripts may not give you the same data. General practice for archiving and data sharing is in [Research integrity and ethics](../../../08_throughout/integrity_and_ethics.md#3-make-your-work-checkable-by-others); mining studies in particular need to:

- **State when the data was collected.** Describe in detail what data was collected, where, when, and how[^ralph2020empirical-e125]. For example, Kalliamvakou et al. state the release date of the dataset snapshot they used[^kalliamvakou2014promises-e13].
- **Release the dataset snapshot and all scripts**, including the tools for downloading, filtering, preprocessing, and postprocessing[^ralph2020empirical-e114]. If the description is too coarse and the data and code aren't released, nobody can reproduce the work[^menzies2019bad-e12]. Putting it only on GitHub doesn't count as proper archiving[^ralph2020empirical-e78]; when data can't be released for ethical or licensing reasons, just explain why[^ralph2020empirical-e76].
- **Freeze a snapshot instead of chasing the latest data.** Datasets go out of date quickly, and there is an inherent tension between keeping them stable and keeping them current[^baltes2022sampling-e15]; your paper's conclusions should correspond to a snapshot from a fixed date, and later updates should be released as new versions.
- **Give a repeatable sampling procedure**, so others can get the same sample[^ralph2020empirical-e127].

---

## 3. Checklist

This checklist follows mainly the repository mining standard in the SIGSOFT Empirical Standards.

**Essential**

- [ ] Explain why the question suits repository mining; define the unit of analysis[^ralph2020empirical-e108]
- [ ] Describe and justify the data source and how repositories were selected from it; explain how the inclusion and exclusion criteria were validated[^ralph2020empirical-e109]
- [ ] Describe the data acquisition process, the dataset's characteristics, and the preprocessing steps[^ralph2020empirical-e110]
- [ ] State when the data was collected[^ralph2020empirical-e125]
- [ ] If there is manual labeling: use multiple raters, report how many, describe the labeling procedure in detail, and assess agreement[^ralph2020empirical-e111]
- [ ] Explain and justify the metrics used; use validated metrics or assess construct validity[^ralph2020empirical-e112]
- [ ] Discuss threats to external validity from the data sources, repositories, and selection criteria[^ralph2020empirical-e113]
- [ ] If the data involves people: state the grounds on which it was legitimately available, the risks, and how privacy is protected[^ralph2020empirical-e133][^ralph2020empirical-e136][^ralph2020empirical-e138]

**Desirable**

- [ ] Release the complete dataset and all tools; use probability sampling where possible[^ralph2020empirical-e114]
- [ ] Triangulate across data sources or researchers; analyze cases where tools fail; test your own tools[^ralph2020empirical-e115]
- [ ] Raters reflect on their own biases; build or test theory; discuss ethical issues[^ralph2020empirical-e116]

**Extraordinary**

- [ ] Establish causality, for example with longitudinal analysis[^ralph2020empirical-e117]

**Acceptable deviations (not flaws)**[^ralph2020empirical-e118]

- Selecting only repositories from one ecosystem (such as Apache) when you are specifically studying that ecosystem
- Withholding some details of the dataset for ethical reasons

**Common but invalid reviewer criticisms**[^ralph2020empirical-e123][^ralph2020empirical-e124]: you don't need to worry about these

- Demanding "more data, more data sources, more repositories" without a good reason
- "No qualitative analysis was done"
- Demanding "a different data source" when the data source has already been justified
- Complaining about repository details deliberately withheld to protect participants' identities
- Demanding that manual studies report how much time they took

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Grabbing a batch of repositories with no filtering | Most repositories are personal and inactive; this is convenience sampling[^kalliamvakou2014promises-e1][^ralph2020empirical-e120] |
| Treating one repository as one project | You miss activity in forks, or count it twice[^kalliamvakou2014promises-e2] |
| Assuming a large sample is representative | No sample size can make up for a biased sampling frame[^baltes2022sampling-e5] |
| Treating GitHub alone as all of a project's activity | Mirrors and external issue trackers are missed[^kalliamvakou2014promises-e8][^ralph2020empirical-e121] |
| Trusting platform fields such as "merged" at face value | Many actual merges show up as unmerged[^kalliamvakou2014promises-e1][^kalliamvakou2014promises-e7] |
| Trusting the "bug" label on issue reports at face value | A third of "bugs" are not actually bugs[^herzig2013bug-e1] |
| Using only the bug fixes that can be linked | The links are systematically biased and can lead to wrong conclusions[^bird2009fair-e3] |
| Treating git history as what really happened | History may be rewritten or squashed, and failed work is invisible[^bird2009promises-e2][^bird2009promises-e5] |
| Not excluding bots or merging identities | Statistics about what *people* do get distorted[^kalliamvakou2014promises-e10][^kalliamvakou2016indepth-e1] |
| Reporting only p-values | With large samples, even trivial differences become significant[^menzies2019bad-e2][^bird2009promises-e7] |

---

## 5. Further reading

- **The repository mining standard itself**: the Repository Mining standard in the SIGSOFT Empirical Standards, plus the supplementary standards on Sampling, Inter-Rater Reliability, Ethics (Secondary Data), and Open Science. You can use them directly as a self-check before submission.
- **Perils of git data**: Bird et al. 2009, *The Promises and Perils of Mining Git*.
- **Perils of GitHub data**: Kalliamvakou et al. 2014 list nine perils and how to avoid them; the 2016 extended journal version raises this to thirteen and analyzes how these perils affected published studies.
- **Bias in bug data**: Bird et al. 2009, *Fair and Balanced? Bias in Bug-Fix Datasets* (linking bias); Herzig et al. 2013, *It's Not a Bug, It's a Feature* (misclassification).
- **Sampling**: Baltes & Ralph 2022, a systematic explanation of the sampling methods used in software engineering research and of representativeness.
- **Warning signs in data analysis**: Menzies & Shepperd 2019, listing 12 "bad smells" in software analytics papers.
- **Finding datasets and tools**: the dspinellis/awesome-msr list collects commonly used datasets (such as GHTorrent, the Software Heritage Graph Dataset, and the Stack Exchange data dump) and mining tools (such as PyDriller, Perceval, and Boa).

Links to every source are in the [source list](../../../../sources/README.md).

[^ralph2020empirical-e105]: SIGSOFT Repository Mining standard, Definition. [Evidence](../../../../sources/notes/ralph2020empirical.md#e105)
[^ralph2020empirical-e106]: SIGSOFT Repository Mining standard, Application. [Evidence](../../../../sources/notes/ralph2020empirical.md#e106)
[^ralph2020empirical-e107]: SIGSOFT Repository Mining standard, Application. [Evidence](../../../../sources/notes/ralph2020empirical.md#e107)
[^ralph2020empirical-e108]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e108)
[^ralph2020empirical-e109]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e109)
[^ralph2020empirical-e110]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e110)
[^ralph2020empirical-e111]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e111)
[^ralph2020empirical-e112]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e112)
[^ralph2020empirical-e113]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e113)
[^ralph2020empirical-e114]: SIGSOFT Repository Mining standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e114)
[^ralph2020empirical-e115]: SIGSOFT Repository Mining standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e115)
[^ralph2020empirical-e116]: SIGSOFT Repository Mining standard, Desirable Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e116)
[^ralph2020empirical-e117]: SIGSOFT Repository Mining standard, Extraordinary Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e117)
[^ralph2020empirical-e118]: SIGSOFT Repository Mining standard, Acceptable Deviations. [Evidence](../../../../sources/notes/ralph2020empirical.md#e118)
[^ralph2020empirical-e119]: SIGSOFT Repository Mining standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e119)
[^ralph2020empirical-e120]: SIGSOFT Repository Mining standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e120)
[^ralph2020empirical-e121]: SIGSOFT Repository Mining standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e121)
[^ralph2020empirical-e122]: SIGSOFT Repository Mining standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e122)
[^ralph2020empirical-e123]: SIGSOFT Repository Mining standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e123)
[^ralph2020empirical-e124]: SIGSOFT Repository Mining standard, Invalid Criticisms. [Evidence](../../../../sources/notes/ralph2020empirical.md#e124)
[^ralph2020empirical-e125]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e125)
[^ralph2020empirical-e127]: SIGSOFT Sampling Supplement, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e127)
[^ralph2020empirical-e37]: SIGSOFT Sampling Supplement, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e37)
[^ralph2020empirical-e128]: SIGSOFT Inter-Rater Reliability and Agreement Supplement. [Evidence](../../../../sources/notes/ralph2020empirical.md#e128)
[^ralph2020empirical-e129]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e130]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Notes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e130)
[^ralph2020empirical-e131]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Extraordinary Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e131)
[^ralph2020empirical-e132]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e132)
[^ralph2020empirical-e133]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e133)
[^ralph2020empirical-e134]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, footnote 1. [Evidence](../../../../sources/notes/ralph2020empirical.md#e134)
[^ralph2020empirical-e135]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e135)
[^ralph2020empirical-e136]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e136)
[^ralph2020empirical-e137]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, footnote 6. [Evidence](../../../../sources/notes/ralph2020empirical.md#e137)
[^ralph2020empirical-e138]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Essential Attributes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e138)
[^bird2009promises-e1]: Bird et al. 2009 (Git), §1. [Evidence](../../../../sources/notes/bird2009promises.md#e1)
[^bird2009promises-e2]: Bird et al. 2009 (Git), Peril 4. [Evidence](../../../../sources/notes/bird2009promises.md#e2)
[^bird2009promises-e3]: Bird et al. 2009 (Git), Peril 5. [Evidence](../../../../sources/notes/bird2009promises.md#e3)
[^bird2009promises-e4]: Bird et al. 2009 (Git), Peril 6. [Evidence](../../../../sources/notes/bird2009promises.md#e4)
[^bird2009promises-e5]: Bird et al. 2009 (Git), Peril 7. [Evidence](../../../../sources/notes/bird2009promises.md#e5)
[^bird2009promises-e6]: Bird et al. 2009 (Git), §5. [Evidence](../../../../sources/notes/bird2009promises.md#e6)
[^bird2009promises-e7]: Bird et al. 2009 (Git), §5. [Evidence](../../../../sources/notes/bird2009promises.md#e7)
[^bird2009fair-e1]: Bird et al. 2009 (bias in defect data sets), Abstract. [Evidence](../../../../sources/notes/bird2009fair.md#e1)
[^bird2009fair-e2]: Bird et al. 2009 (bias in defect data sets), §1. [Evidence](../../../../sources/notes/bird2009fair.md#e2)
[^bird2009fair-e3]: Bird et al. 2009 (bias in defect data sets), §1. [Evidence](../../../../sources/notes/bird2009fair.md#e3)
[^bird2009fair-e4]: Bird et al. 2009 (bias in defect data sets), §4. [Evidence](../../../../sources/notes/bird2009fair.md#e4)
[^bird2009fair-e5]: Bird et al. 2009 (bias in defect data sets), §4. [Evidence](../../../../sources/notes/bird2009fair.md#e5)
[^kalliamvakou2014promises-e1]: Kalliamvakou et al. 2014, Abstract. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e1)
[^kalliamvakou2014promises-e2]: Kalliamvakou et al. 2014, Peril I. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e2)
[^kalliamvakou2014promises-e3]: Kalliamvakou et al. 2014, Peril II. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e3)
[^kalliamvakou2014promises-e4]: Kalliamvakou et al. 2014, Peril IV. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e4)
[^kalliamvakou2014promises-e5]: Kalliamvakou et al. 2014, Peril V. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e5)
[^kalliamvakou2014promises-e6]: Kalliamvakou et al. 2014, Peril VII. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e6)
[^kalliamvakou2014promises-e7]: Kalliamvakou et al. 2014, Peril VIII. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e7)
[^kalliamvakou2014promises-e8]: Kalliamvakou et al. 2014, Peril IX. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e8)
[^kalliamvakou2014promises-e9]: Kalliamvakou et al. 2014, §4.4.2. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e9)
[^kalliamvakou2014promises-e10]: Kalliamvakou et al. 2014, §6. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e10)
[^kalliamvakou2014promises-e11]: Kalliamvakou et al. 2014, §6. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e11)
[^kalliamvakou2014promises-e12]: Kalliamvakou et al. 2014, §2.1. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e12)
[^kalliamvakou2014promises-e13]: Kalliamvakou et al. 2014, §3, §5. [Evidence](../../../../sources/notes/kalliamvakou2014promises.md#e13)
[^kalliamvakou2016indepth-e1]: Kalliamvakou et al. 2016, Peril X. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e1)
[^kalliamvakou2016indepth-e2]: Kalliamvakou et al. 2016, Peril XI. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e2)
[^kalliamvakou2016indepth-e3]: Kalliamvakou et al. 2016, Peril XII. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e3)
[^kalliamvakou2016indepth-e4]: Kalliamvakou et al. 2016, Peril XII. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e4)
[^kalliamvakou2016indepth-e5]: Kalliamvakou et al. 2016, Peril XII. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e5)
[^kalliamvakou2016indepth-e6]: Kalliamvakou et al. 2016, Peril XIII. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e6)
[^kalliamvakou2016indepth-e7]: Kalliamvakou et al. 2016, §4.9. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e7)
[^kalliamvakou2016indepth-e8]: Kalliamvakou et al. 2016, §5.2. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e8)
[^kalliamvakou2016indepth-e9]: Kalliamvakou et al. 2016, §6. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e9)
[^kalliamvakou2016indepth-e10]: Kalliamvakou et al. 2016, §6. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e10)
[^kalliamvakou2016indepth-e11]: Kalliamvakou et al. 2016, §8. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e11)
[^kalliamvakou2016indepth-e12]: Kalliamvakou et al. 2016, §8. [Evidence](../../../../sources/notes/kalliamvakou2016indepth.md#e12)
[^herzig2013bug-e1]: Herzig et al. 2013, Abstract. [Evidence](../../../../sources/notes/herzig2013bug.md#e1)
[^herzig2013bug-e2]: Herzig et al. 2013, §I. [Evidence](../../../../sources/notes/herzig2013bug.md#e2)
[^herzig2013bug-e3]: Herzig et al. 2013, Fig. 1 and §XI. [Evidence](../../../../sources/notes/herzig2013bug.md#e3)
[^herzig2013bug-e4]: Herzig et al. 2013, §XI. [Evidence](../../../../sources/notes/herzig2013bug.md#e4)
[^herzig2013bug-e5]: Herzig et al. 2013, §XII. [Evidence](../../../../sources/notes/herzig2013bug.md#e5)
[^baltes2022sampling-e2]: Baltes & Ralph 2022, §2.1.1. [Evidence](../../../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e5]: Baltes & Ralph 2022, §2.6. [Evidence](../../../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e12]: Baltes & Ralph 2022, §2.5. [Evidence](../../../../sources/notes/baltes2022sampling.md#e12)
[^baltes2022sampling-e13]: Baltes & Ralph 2022, §6.2. [Evidence](../../../../sources/notes/baltes2022sampling.md#e13)
[^baltes2022sampling-e14]: Baltes & Ralph 2022, §6.2. [Evidence](../../../../sources/notes/baltes2022sampling.md#e14)
[^baltes2022sampling-e15]: Baltes & Ralph 2022, §6.2. [Evidence](../../../../sources/notes/baltes2022sampling.md#e15)
[^baltes2022sampling-e16]: Baltes & Ralph 2022, §6.3. [Evidence](../../../../sources/notes/baltes2022sampling.md#e16)
[^menzies2019bad-e10]: Menzies & Shepperd 2019, §1. [Evidence](../../../../sources/notes/menzies2019bad.md#e10)
[^menzies2019bad-e2]: Menzies & Shepperd 2019, §4.6. [Evidence](../../../../sources/notes/menzies2019bad.md#e2)
[^menzies2019bad-e11]: Menzies & Shepperd 2019, §4.3. [Evidence](../../../../sources/notes/menzies2019bad.md#e11)
[^menzies2019bad-e12]: Menzies & Shepperd 2019, §4.4. [Evidence](../../../../sources/notes/menzies2019bad.md#e12)
[^ralph2020empirical-e66]: SIGSOFT General Standard, Antipatterns. [Evidence](../../../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e76]: SIGSOFT Open Science Supplement, Principle. [Evidence](../../../../sources/notes/ralph2020empirical.md#e76)
[^ralph2020empirical-e78]: SIGSOFT Open Science Supplement, Notes. [Evidence](../../../../sources/notes/ralph2020empirical.md#e78)
