# Longitudinal studies: observing the same subjects repeatedly over time

This page covers **longitudinal studies**: over a period of time, you repeatedly measure the same things on the same set of subjects to see how they change. Examples: following a set of projects for several years to see how technical debt accumulates and gets paid down, or surveying the same developers every few months to see how their productivity changes.

Much longitudinal data comes from the history of code repositories; for how to extract and clean repository data, see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md). For handling threats to validity in general, see [Validity and limitations: think them through at the design stage](../02_do-the-project/04_validity-and-limits.md). This page covers only the problems that come specifically from observing things repeatedly over time.

**Scope** `[Our analysis]`: The checklist on this page follows the longitudinal studies standard that ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) wrote for software engineering. The pitfalls of repository data come from software engineering, the planning principles for studies of people come from information systems (Kehr & Kowatsch 2015), and the examples are mostly about software projects and developers. If you are doing a longitudinal study in another field, start with your field's conventions. For example, cohort studies in health research, which follow populations over time and compare groups with different exposures, have stricter rules; see [Observational epidemiology](observational_epidemiology.md).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md) (describing how a phenomenon changes over time).

**After reading this page, you should be able to:**

- judge whether your question needs a longitudinal design, and whether two waves of measurement are enough;
- set the measurement points and intervals, choose your subjects, and plan ahead for attrition and survivorship bias;
- recognize common mistakes such as analyzing longitudinal data as if it were cross-sectional;
- check your own study against the checklist at the end of the page.

---

## 1. What this kind of study is, and when to use it

The ACM SIGSOFT Empirical Standards define it as research that studies how a phenomenon changes and evolves over time, observing the same variables (for example, productivity or technical debt) repeatedly over a period; analyzing datasets that change over time, such as code evolution, also counts[^ralph2020empirical-e257]. It has two hard requirements: **at least two waves of observation**, and **each subject (person or artifact) can be matched across waves**[^ralph2020empirical-e258].

**Questions it is good at**:

- **What the change looks like**: is it growing or declining, linear or fast at first and then slowing[^kehr2015quantitative-e7]?
- **Whether something changed, and why**[^kehr2015quantitative-e8]: for example, whether defects dropped after a new process was introduced `[Our analysis]`.
- **Clues about causation**: causes come before effects[^kehr2015quantitative-e1]. The SIGSOFT standard lists "investigates causality using the longitudinal nature of the data to establish precedence and statistically controlling for third-variable explanations" as a desirable attribute[^ralph2020empirical-e264]. The SIGSOFT standard notes that longitudinal studies use time precisely to maximize internal validity (whether a result really comes from the stated cause)[^ralph2020empirical-e269].

**How it differs from related designs** `[Our analysis, based on the sources below]`:

| | Cross-sectional study | Retrospective survey | Longitudinal study | Experiment |
|---|---|---|---|---|
| How many observations | One point in time | Once, asking people to recall the past | At least two waves, with subjects matched across them | Usually before and after a manipulation, or under different conditions |
| Does the researcher actively change a variable? | No | No | No | Yes |
| What it can show | Distributions and correlations at one moment | Relies on memory, large errors | The shape of change, temporal order | Causal effects |

For analyses that look at only one point in time, SIGSOFT points you to its Exploratory Data Science standard, and for studies that manipulate variables, its Experiments standard[^ralph2020empirical-e258] (the corresponding pages in this handbook are [Data science research](data_science.md) and [Controlled experiments](controlled_experiment.md)). A one-off survey that asks subjects to recall past changes is sometimes also called longitudinal, but Kehr & Kowatsch don't use that definition[^kehr2015quantitative-e3]. Their definition is repeated observation of **the same outcome variables** on **the same units**[^kehr2015quantitative-e2].

**Two variants**[^ralph2020empirical-e271]:

- **Experience sampling**: measuring several times a day over a short period (usually one to three weeks), with the emphasis on capturing the current state rather than after-the-fact recall.
- **Cohort study**: observing subjects over time and comparing groups with different levels of exposure. It has stricter rules than this page covers, and you should read dedicated guidelines before doing one; for how it is done in health research, see [Observational epidemiology](observational_epidemiology.md).

**Across computer science** `[Our analysis]`: In software engineering, the common case is following projects, code or developers; in systems and security, you can follow the performance or vulnerabilities of the same software across many versions; in machine learning, you can follow how a deployed model's performance changes over time. Whenever it is "the same subjects, several time points, the same measurements", the requirements on this page apply.

---

## 2. How to do it

### Step 1: Be clear which kind of "change" question you are asking

The type of question decides how many waves you need:

- **To describe the shape of change** (for example, linear growth), you need at least three waves; to identify nonlinear change, you need more[^kehr2015quantitative-e7].
- **If you only ask "did it change, and why?"**, a two-wave pretest–posttest design is common[^kehr2015quantitative-e8]. But two-wave designs have long been criticized as vulnerable to measurement error and similar problems, which make it hard to tell real change from change produced by measurement. The usual remedy is to add a randomly assigned control group with the same starting conditions: measurement error affects both groups equally, so real change shows up as the difference between the two groups' changes[^kehr2015quantitative-e9].

**Where people go wrong**: Collecting two waves of data and then trying to talk about a "trend". Two points can't make a curve.

### Step 2: Set time points and intervals by the phenomenon's own rhythm

How many waves and how far apart should follow how fast the phenomenon itself changes; the SIGSOFT standard makes this an essential attribute[^ralph2020empirical-e259]. Start from theory or prior research, work out how the outcome variable is expected to fluctuate, and then decide the number of measurements, the interval and the time scale[^kehr2015quantitative-e4].

- **The time scale doesn't have to be calendar time.** Any irreversible quantity will do, such as how long a system has been in use[^kehr2015quantitative-e5]. `[Our analysis]` When studying code, other common time scales are version numbers, number of releases or number of commits; which one to use depends on your question.
- **If there is no theory to go on**: run a small qualitative pre-study to estimate the rhythm, or set the interval by the fastest-changing variable[^kehr2015quantitative-e6].

**Where people go wrong**: An interval that doesn't match the phenomenon's cycle; SIGSOFT lists this as an antipattern[^ralph2020empirical-e270]. If you sample once a year, for example, you won't see technical debt rise and fall within each release cycle `[Our analysis]`.

### Step 3: Choose subjects, make sure they can be matched across waves, and watch for survivorship bias

- **Every subject must be identifiable across waves**[^ralph2020empirical-e259]. With people, you need a stable anonymous ID; with projects, you have to deal with renames, migrations and mergers `[Our analysis]`.
- **Explain how subjects were selected and filtered.** When your subjects are software repositories, describe the quality controls you used to keep the artifacts consistent[^ralph2020empirical-e263].
- **Watch for survivorship bias.** If you analyze the past 100 years using only stock markets that still exist today, you get a much higher average return than if you analyzed all the stock markets that existed 100 years ago[^ralph2020empirical-e266]. In repository data this problem is common: GitHub's application programming interface (API) only gives a repository's current state, and once a repository is deleted, all its events and metadata are lost[^kalliamvakou2016indepth-e3]. `[Our analysis]` So if you start from "projects still active today" and look back through their histories, you get a set of survivors, and the reasons projects fail are invisible in that sample. A safer approach is to fix your sample at the starting point and follow it forward, or to use data archived in advance.

### Step 4: Plan for attrition, and report it honestly

Attrition means subjects dropping out partway through: people stop answering the questionnaire, projects stop being maintained or are deleted. It is almost unavoidable in longitudinal research and has two consequences: the sample shrinks and statistical power (the probability of detecting an effect that really exists) drops; and the subjects who stay may differ systematically from those who leave[^kehr2015quantitative-e13]. For example, if the people with low acceptance all drop out, average acceptance is artificially inflated[^kehr2015quantitative-e14].

- **Beforehand**: recruit more subjects than you need, use incentives to raise response rates, and keep the number of waves and the intervals reasonable[^kehr2015quantitative-e15]; justify the sample size, for example with a statistical power analysis[^ralph2020empirical-e262].
- **Afterwards**: report how many subjects were lost at each wave, and explain how missing data was handled[^ralph2020empirical-e262].
- **Don't quietly delete incomplete data.** Of the 21 longitudinal information systems studies Kehr & Kowatsch reviewed, 20 did not explicitly deal with attrition and simply deleted the incomplete data[^kehr2015quantitative-e16].

### Step 5: Keep measurement consistent across waves

A longitudinal study compares the difference between waves. If the measurement itself changes, the difference may come from the measurement rather than the phenomenon.

- Discuss whether the data is consistent across waves, for example the test–retest reliability of a questionnaire (whether the same people give stable answers when they take it again after a while); check for differences in data distributions between waves[^ralph2020empirical-e265].
- **Platforms and the meaning of data change too.** For example, what "watchers" means on GitHub is different before and after August 2012[^kalliamvakou2016indepth-e6]; git history can also be rewritten[^bird2009promises-e2]. For pitfalls like these in repository data, see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md#step-4-extract-and-clean-the-data).
- `[Our analysis]` When you compute metrics with a tool (for example, estimating technical debt with a static analysis tool), fix the same tool version and the same rule set for every wave; if you have to upgrade partway through, recompute the old data with the new version.

### Step 6: Analyze with methods suited to dependent data

Longitudinal data is serially dependent: each wave's data can be partly predicted from the previous wave. That violates the "uncorrelated residuals" assumption of many common statistical methods[^kehr2015quantitative-e17], and ordinary correlation analysis can overstate the relationships between variables[^kehr2015quantitative-e18]. "Analyzing longitudinal data as if it were cross-sectional" is an antipattern listed by SIGSOFT[^ralph2020empirical-e270].

- If you only care about change at the group level, you can use repeated-measures methods such as repeated-measures analysis of variance (ANOVA) or the paired t-test; if you want to study how different subjects' trajectories of change differ, you can use multilevel models (also called hierarchical linear models)[^kehr2015quantitative-e19].
- Justify why you chose your analysis method, and explain how it handles the serial dependence in the data[^ralph2020empirical-e260].
- Longitudinal analysis usually involves many variables and multiple comparisons, which makes it easier to get "significant" results by chance. Adjust the significance threshold, or use Bayesian statistics[^ralph2020empirical-e261]. For general issues with significance and effect sizes, see [Analysis and interpretation: report how big and how certain](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 7: Beware of threats to validity that time itself introduces

Time doesn't only bring the change you want to see; it can also hide change or create it:

- **Practice effects**: if you test the same users again and again, gains in efficiency may just mean they got familiar with the system and learned to work around problems, not that the product got better[^kehr2015quantitative-e10].
- **Memory and demand effects**: participants who remember how they answered last time may answer the same way to stay consistent, masking real change; and the more often they are measured, the easier it is for them to guess the study's purpose and answer the way they think the researcher expects[^kehr2015quantitative-e11].
- **External events during the study** `[Our analysis]`: if, during the tracking period, the team changes its development process, a programming language ships a major version, or the company has layoffs, these can affect all subjects at once and be mistaken for effects of the factor you are studying. Record major events during the tracking period and take them into account in the analysis.

When you study why something changed, the strongest approach is to add a control group under similar conditions[^kehr2015quantitative-e12]. Confounders you can't control statistically should be discussed in the paper[^ralph2020empirical-e264].

### Step 8: Reporting

Beyond the general writing requirements (see [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md)), a longitudinal study needs to spell out: who the subjects are and how they were selected[^ralph2020empirical-e263]; how the time points and intervals were chosen; how many subjects were lost at each wave and how missing data was handled[^ralph2020empirical-e262]; how each metric gets from concept to measurement[^ralph2020empirical-e263]; and the cost of collecting the data and any incentives used[^ralph2020empirical-e267]. Publish the dataset, the collection scripts and the analysis scripts[^ralph2020empirical-e267]. Once you have acknowledged a limitation, your conclusions must actually respect it[^ralph2020empirical-e103][^ralph2020empirical-e126].

---

## 3. Checklist

This list mainly follows SIGSOFT's longitudinal studies standard, which was written for software engineering.

**Essential**

- [ ] At least two waves of data collection, with subjects identifiable across waves[^ralph2020empirical-e259]
- [ ] Number of waves and intervals set by the phenomenon's natural rhythm[^ralph2020empirical-e259]
- [ ] The analysis method is justified and suits the serial dependence of the data[^ralph2020empirical-e260]
- [ ] With many variables and comparisons, the significance threshold is adjusted, or Bayesian statistics are used instead[^ralph2020empirical-e261]
- [ ] Sample size is justified; attrition at each wave is described; handling of missing data is explained[^ralph2020empirical-e262]
- [ ] Subjects are described; the construct validity of the metrics is discussed[^ralph2020empirical-e263]

**Desirable**

- [ ] Provide the dataset, collection scripts or tools, analysis scripts and instructions for reproduction[^ralph2020empirical-e267]
- [ ] Use temporal order to examine causation, with statistical control for third variables; discuss confounders that can't be controlled[^ralph2020empirical-e264]
- [ ] Discuss consistency of data across waves and check for differences in distributions between waves[^ralph2020empirical-e265]
- [ ] Describe the cost of data collection and the incentives[^ralph2020empirical-e267]
- [ ] Address survivorship bias[^ralph2020empirical-e266]

**Extraordinary**

- [ ] Use a multi-stage selection process to determine subjects; follow subjects for an exceptionally long time, for example more than five years[^ralph2020empirical-e268]

**Common but invalid reviewer criticisms**: you need not worry about these

- Saying in general terms that "the measurement interval is too short" or "too long"; saying "not enough waves" without a reason; saying "the sample is too small" without a post-hoc power calculation[^ralph2020empirical-e272]
- Demanding a more conservative significance threshold or Bayesian methods when there are few comparisons; complaining about generalizability when the paper already explicitly acknowledges its limits on generalization[^ralph2020empirical-e273]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Talking about a "trend" with only two waves of data | Describing the shape of change needs at least three waves[^kehr2015quantitative-e7] |
| Setting intervals for convenience, ignoring the phenomenon's rhythm | You may miss the real shape of change entirely[^ralph2020empirical-e270][^kehr2015quantitative-e4] |
| Looking back from projects that are still active today | Survivorship bias: the subjects that failed are excluded[^ralph2020empirical-e266][^kalliamvakou2016indepth-e3] |
| Simply deleting incomplete data and not reporting attrition | Those who dropped out may differ systematically, distorting the conclusions[^kehr2015quantitative-e13][^kehr2015quantitative-e14] |
| Changing the measurement tool or definition partway through | Differences between waves may come from the measurement, not the phenomenon[^ralph2020empirical-e265][^kalliamvakou2016indepth-e6] |
| Analyzing longitudinal data as if it were cross-sectional | Violates the independence assumption and can overstate relationships[^ralph2020empirical-e270][^kehr2015quantitative-e18] |
| Attributing all change to the factor you are studying | Practice effects, demand effects and external events can all produce change[^kehr2015quantitative-e10][^kehr2015quantitative-e11] |

---

## 5. Further reading

- **SIGSOFT longitudinal studies standard**: the full checklist and antipatterns, plus a list of exemplar papers in software engineering; worth checking against before you start and before you submit.
- **Kehr & Kowatsch 2015**: on quantitative longitudinal research with human subjects in information systems. It sets out four planning principles (follow the natural rhythm, choose the right number of waves, attend to internal validity, choose the right analysis method) and compares several common statistical models. Most useful for longitudinal questionnaire or user studies.
- **Pitfalls of repository data**: Bird et al. 2009 and Kalliamvakou et al. 2016, which you should read before doing longitudinal analysis on repository histories; their main points are summarized in [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md).

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e257]: SIGSOFT Longitudinal Studies standard, Definition and Application. [Evidence](../../sources/notes/ralph2020empirical.md#e257)
[^ralph2020empirical-e258]: SIGSOFT Longitudinal Studies standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e258)
[^ralph2020empirical-e259]: SIGSOFT Longitudinal Studies standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e259)
[^ralph2020empirical-e260]: SIGSOFT Longitudinal Studies standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e260)
[^ralph2020empirical-e261]: SIGSOFT Longitudinal Studies standard, Essential Attributes, footnote 4. [Evidence](../../sources/notes/ralph2020empirical.md#e261)
[^ralph2020empirical-e262]: SIGSOFT Longitudinal Studies standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e262)
[^ralph2020empirical-e263]: SIGSOFT Longitudinal Studies standard, Essential Attributes and footnotes 6 and 7. [Evidence](../../sources/notes/ralph2020empirical.md#e263)
[^ralph2020empirical-e264]: SIGSOFT Longitudinal Studies standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e264)
[^ralph2020empirical-e265]: SIGSOFT Longitudinal Studies standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e265)
[^ralph2020empirical-e266]: SIGSOFT Longitudinal Studies standard, Desirable Attributes and footnote 8. [Evidence](../../sources/notes/ralph2020empirical.md#e266)
[^ralph2020empirical-e267]: SIGSOFT Longitudinal Studies standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e267)
[^ralph2020empirical-e268]: SIGSOFT Longitudinal Studies standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e268)
[^ralph2020empirical-e269]: SIGSOFT Longitudinal Studies standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e269)
[^ralph2020empirical-e270]: SIGSOFT Longitudinal Studies standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e270)
[^ralph2020empirical-e271]: SIGSOFT Longitudinal Studies standard, Variations. [Evidence](../../sources/notes/ralph2020empirical.md#e271)
[^ralph2020empirical-e272]: SIGSOFT Longitudinal Studies standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e272)
[^ralph2020empirical-e273]: SIGSOFT Longitudinal Studies standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e273)
[^ralph2020empirical-e103]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e103)
[^ralph2020empirical-e126]: SIGSOFT General Standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e126)
[^kehr2015quantitative-e1]: Kehr & Kowatsch 2015, §1. [Evidence](../../sources/notes/kehr2015quantitative.md#e1)
[^kehr2015quantitative-e2]: Kehr & Kowatsch 2015, §1. [Evidence](../../sources/notes/kehr2015quantitative.md#e2)
[^kehr2015quantitative-e3]: Kehr & Kowatsch 2015, §1. [Evidence](../../sources/notes/kehr2015quantitative.md#e3)
[^kehr2015quantitative-e4]: Kehr & Kowatsch 2015, §4.1. [Evidence](../../sources/notes/kehr2015quantitative.md#e4)
[^kehr2015quantitative-e5]: Kehr & Kowatsch 2015, §4.1. [Evidence](../../sources/notes/kehr2015quantitative.md#e5)
[^kehr2015quantitative-e6]: Kehr & Kowatsch 2015, §4.1. [Evidence](../../sources/notes/kehr2015quantitative.md#e6)
[^kehr2015quantitative-e7]: Kehr & Kowatsch 2015, §4.2. [Evidence](../../sources/notes/kehr2015quantitative.md#e7)
[^kehr2015quantitative-e8]: Kehr & Kowatsch 2015, §4.2. [Evidence](../../sources/notes/kehr2015quantitative.md#e8)
[^kehr2015quantitative-e9]: Kehr & Kowatsch 2015, §4.2. [Evidence](../../sources/notes/kehr2015quantitative.md#e9)
[^kehr2015quantitative-e10]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e10)
[^kehr2015quantitative-e11]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e11)
[^kehr2015quantitative-e12]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e12)
[^kehr2015quantitative-e13]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e13)
[^kehr2015quantitative-e14]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e14)
[^kehr2015quantitative-e15]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e15)
[^kehr2015quantitative-e16]: Kehr & Kowatsch 2015, §4.3. [Evidence](../../sources/notes/kehr2015quantitative.md#e16)
[^kehr2015quantitative-e17]: Kehr & Kowatsch 2015, §4.4. [Evidence](../../sources/notes/kehr2015quantitative.md#e17)
[^kehr2015quantitative-e18]: Kehr & Kowatsch 2015, §4.4. [Evidence](../../sources/notes/kehr2015quantitative.md#e18)
[^kehr2015quantitative-e19]: Kehr & Kowatsch 2015, §4.4. [Evidence](../../sources/notes/kehr2015quantitative.md#e19)
[^kalliamvakou2016indepth-e3]: Kalliamvakou et al. 2016, §4.8 Peril XII. [Evidence](../../sources/notes/kalliamvakou2016indepth.md#e3)
[^kalliamvakou2016indepth-e6]: Kalliamvakou et al. 2016, §4.8 Peril XIII. [Evidence](../../sources/notes/kalliamvakou2016indepth.md#e6)
[^bird2009promises-e2]: Bird et al. 2009, §3 Peril 4. [Evidence](../../sources/notes/bird2009promises.md#e2)
