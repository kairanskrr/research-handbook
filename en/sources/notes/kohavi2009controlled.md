# Kohavi et al. 2009: Controlled experiments on the web: survey and practical guide

- Source: `kohavi2009controlled`, [PDF (author's homepage)](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf)
- Version: Data Mining and Knowledge Discovery 18(1), pp. 140–181, DOI 10.1007/s10618-008-0114-1 (journal-version PDF on the author's homepage). The authors were members of Microsoft's experimentation platform team. Locations give journal page numbers.

### E1

- Location: §1 Introduction, p. 142
- Quote: "In the simplest manifestation of such experiments, live users are randomly assigned to one of two variants: (i) the Control, which is commonly the "existing" version, and (ii) the Treatment, which is usually a new version being evaluated."
- Key point: The simplest online controlled experiment randomly assigns live users to one of two variants: the Control (usually the existing version) and the Treatment (the new version being evaluated).

### E2

- Location: §3 Controlled experiments, p. 149
- Quote: "The key here is "random." Users cannot be distributed "any old which way" (Weiss 1997); no factor can influence the decision." / "If the experiment was designed and executed properly, the only thing consistently different between the two variants is the change between the Control and Treatment, so any differences in the OEC are inevitably the result of this assignment, establishing causality"
- Key point: The key is randomization, with no factor influencing assignment; when the experiment is designed and run properly, the only systematic difference between the groups is the change itself, so differences in the metric can be attributed to it.

### E3

- Location: §3.1 Terminology, p. 150
- Quote: "Overall Evaluation Criterion (OEC) (Roy 2001). A quantitative measure of the experiment's objective." / "A good OEC should not be short-term focused (e.g., clicks); to the contrary, it should include factors that predict long-term goals, such as predicted lifetime value and repeat visits."
- Key point: The Overall Evaluation Criterion (OEC) is a quantitative measure of the experiment's objective; a good OEC is not short-term focused (such as clicks) but includes factors that predict long-term goals, such as lifetime value and repeat visits.

### E4

- Location: §3.1 Terminology, p. 150
- Quote: "selecting a single metric, possibly as a weighted combination of such objectives is highly desired and recommended (Roy 2001, p. 50). A single metric forces tradeoffs to be made once for multiple experiments and aligns the organization behind a clear objective."
- Key point: Choosing a single metric, possibly a weighted combination of objectives, is strongly recommended; the tradeoffs are then made once and every experiment serves one clear objective.

### E5

- Location: §3.1 Terminology, p. 150
- Quote: "The units are assumed to be independent. On the web, the user is a common experimental unit, although some metrics may have user-day, user-session or page views as the experimental units. For any of these randomization by user is preferred. It is important that the user receive a consistent experience throughout the experiment, and this is commonly achieved through randomization based on user IDs stored in cookies."
- Key point: Experimental units are assumed independent; on the web the user is the usual unit, though some metrics use user-days, sessions, or page views; in every case randomizing by user is preferred so each user gets a consistent experience, usually via a user ID stored in a cookie.

### E6

- Location: §3.1 Terminology, p. 151
- Quote: "Instead of an A/B test, you exercise the experimentation system, assigning users to one of two groups, but expose them to exactly the same experience. An A/A test can be used to (i) collect data and assess its variability for power calculations, and (ii) test the experimentation system (the Null hypothesis should be rejected about 5% of the time when a 95% confidence level is used)."
- Key point: An A/A test splits users into two groups as usual but shows both exactly the same experience; it is used to estimate variability for power calculations and to test the experimentation system itself (at a 95% confidence level, the null hypothesis should be rejected only about 5% of the time).

### E7

- Location: §3.2.4 The choice of OEC must be made in advance, p. 154
- Quote: "When running experiments, it is important to decide in advance on the OEC (a planned comparison); otherwise, there is an increased risk of finding what appear to be significant results by chance (familywise type I error)"
- Key point: The OEC must be chosen in advance; otherwise you are more likely to find results that look significant by chance.

### E8

- Location: §3.2 Hypothesis testing and sample size, p. 151
- Quote: "Lower the variability of the OEC by filtering out users who were not exposed to the variants, yet were still included in the OEC. For example, if you make a change to the checkout page, analyze only users who got to the page, as everyone else adds noise, increasing the variability."
- Key point: Filtering out users who were never exposed to the change lowers the metric's variability; for example, if you change the checkout page, analyze only users who reached it.

### E9

- Location: §3.2.1 Example: impact of lower-variability OEC on the sample size, p. 153
- Quote: "If you are running an A/B test and want to detect a 5% change to revenue, you will need over 409,000 users to achieve the desired 80% power"
- Key point: In the paper's e-commerce example, detecting a 5% change in revenue with 80% power requires over 409,000 users.

### E10

- Location: §3.4 Effect of robots on experimental results, p. 155
- Quote: "Robots can introduce significant skew into estimates, enough to render assumptions invalid. We have seen cases where robots caused many metrics to be significant when they should not have been (e.g., much more than 5% false positives for an A/A test)."
- Key point: Robot traffic can badly skew estimates; the authors have seen robots push A/A test false positives far above 5%.

### E11

- Location: §3.5.1 Treatment ramp-up, p. 156
- Quote: "An experiment can be initiated with a small percentage of users assigned to the Treatment(s), and then that percentage can be gradually increased." / "At each step, which could run for, say, a couple of hours, you can analyze the data to make sure there are no egregious problems with the Treatment before exposing it to more users."
- Key point: An experiment can start by exposing a small percentage of users to the Treatment and ramp up gradually, checking at each step for serious problems before exposing more users.

### E12

- Location: §3.6 Limitations, item 1, p. 157
- Quote: "It is possible to know which variant is better, and by how much, but not "why." In user studies, for example, behavior is often augmented with users' comments, and hence usability labs can be used to augment and complement controlled experiments (Nielsen 2005)."
- Key point: Online experiments tell you which variant is better and by how much, but not why; user studies in usability labs, which capture users' comments, can complement them.

### E13

- Location: §3.6 Limitations, item 2, p. 157
- Quote: "Controlled experiments measure the effect on the OEC during the experimentation period, typically a few weeks."
- Key point: Online experiments measure the effect during the experiment period, typically a few weeks.

### E14

- Location: §3.6 Limitations, item 3, p. 158
- Quote: "If you change the navigation on a web site, experienced users may be less efficient until they get used to the new navigation, thus giving an inherent advantage to the Control. Conversely, when a new design or feature is introduced, some users will investigate it, click everywhere, and thus introduce a "newness" bias." / "One analysis that can be done is to compute the OEC only for new users on the different variants, since they are not affected by either factor."
- Key point: Primacy effects (experienced users are slower until they adapt to new navigation, favoring the Control) and novelty effects (users click around a new design, biasing results) pull in opposite directions; one remedy is to analyze only new users, who are affected by neither.

### E15

- Location: §3.6 Limitations, item 4, p. 158
- Quote: "Nonetheless, the feature must be implemented and be of sufficient quality to expose users to it."
- Key point: Online experiments require that the feature already be implemented and of good enough quality to show to real users.

### E16

- Location: §5.1 Randomization algorithm, pp. 163–164
- Quote: "End users must be equally likely to see each variant of an experiment (assuming a 50–50 split). There should be no bias toward any particular variant." / "Repeat assignments of a single end user must be consistent; the end user should be assigned to the same variant on each successive visit to the site." / "When multiple experiments are run, there must be no correlation between experiments."
- Key point: A randomization algorithm must meet three requirements: each user is equally likely to see each variant, a user gets the same variant on every visit, and concurrent experiments have uncorrelated assignments.

### E17

- Location: §6.2.1 Run continuous A/A tests, p. 174
- Quote: "Run A/A tests (see Sect. 3.1) and validate the following. 1. Are users split according to the planned percentages? 2. Is the data collected matching the system of record? 3. Are the results showing non-significant results 95% of the time? Continuously run A/A tests in parallel with other experiments."
- Key point: A/A tests should check three things: whether users are split in the planned proportions, whether collected data match the system of record, and whether results are non-significant 95% of the time; they should run continuously alongside other experiments.

### E18

- Location: §6.2.3 Determine the minimum sample size, p. 175
- Quote: "Decide on the statistical power, the effect you would like to detect, and estimate the variability of the OEC through an A/A test. Based on this data you can compute the minimum sample size needed for the experiment and hence the running time for your web site. A common mistake is to run experiments that are underpowered."
- Key point: Decide the power and the effect size you want to detect, estimate the metric's variability with an A/A test, then compute the minimum sample size and running time; a common mistake is running underpowered experiments.

### E19

- Location: §6.2.4 Assign 50% of users to treatment, p. 175
- Quote: "In order to maximize the power of an experiment and minimize the running time, we recommend that 50% of users see each of the variants in an A/B test." / "For example, if an experiment is run at 99%/1%, then it will have to run about 25 times longer than if it ran at 50%/50%."
- Key point: To maximize power and minimize running time, split users 50/50; a 99%/1% split must run about 25 times longer.

### E20

- Location: §6.2.5 Beware of day of week effects, p. 175
- Quote: "we strongly recommend running experiments for at least a week or two, then continuing by multiples of a week so that day-of-week effects can be analyzed."
- Key point: Even with heavy traffic, run experiments for at least a week or two and extend them in whole weeks so day-of-week effects can be analyzed.

### E21

- Location: §6.3.1 Agree on the OEC upfront, p. 176
- Quote: "it best serves this purpose when the interested parties have agreed on how an experiment is to be evaluated before the experiment is run."
- Key point: An experiment best serves as an objective measure of value when the interested parties agree on how it will be evaluated before it runs.

### E22

- Location: §6.3.2 Beware of launching features that "do not hurt" users, p. 176
- Quote: "When an experiment yields no statistically significant difference between variants, this may mean that there truly is no difference between the variants or that the experiment did not have sufficient power to detect the change." / "It is possible that the experiment is negative but underpowered."
- Key point: A non-significant result may mean there is truly no difference or that the experiment lacked power; launching because it "does no harm" may ship a change that is actually harmful but went undetected.

### E23

- Location: Appendix A, item 1 (eBay auction example), p. 178
- Quote: "If some users have this incentive and others do not, the presence of the Treatment will affect all items so we cannot get a true measure of the effectiveness of making this change. In this case you can randomly assign one group of items in the auction to be in the Control and the rest to be in the Treatment and compare the OEC for these two groups. i.e. randomly assign the items in the auction, not the users."
- Key point: When some users in an auction get an incentive and others do not, the Treatment affects all items, so randomizing by user cannot measure the true effect; randomize the items instead of the users.

### E24

- Location: Appendix A, item 2 (price elasticity study), p. 179
- Quote: "The usual randomization based on user is not desirable because bad customer relations could result if it's exposed that some customers are getting a different price than other customers (everything else being equal) as Amazon.com discovered when it ran such a study (Weiss 2000)."
- Key point: Randomizing by user is a bad idea for price tests: if customers discover they are paying different prices, customer relations suffer, as Amazon found; randomize products instead.

### E25

- Location: §1 Introduction, p. 142
- Quote: "Unlike other methodologies, such as post-hoc analysis or interrupted time series (quasi experimentation) (Charles and Melvin 2004), this experimental design methodology tests for causal relationships"
- Key point: Unlike post-hoc analysis or quasi-experimental methods such as interrupted time series, controlled experiments test causal relationships.

### E26

- Location: §2.4 Behavior-Based Search at Amazon, p. 146
- Quote: "The examples above changed User-Interface (UI) elements. This example deals with a backend algorithmic change, which is often overlooked as an area to apply controlled experiments."
- Key point: Online experiments are not only for user-interface changes; they can also evaluate backend algorithm changes, such as search algorithms, an often overlooked use.

### E27

- Location: §3.3 Confidence intervals for absolute and percent effect, p. 154
- Quote: "It is useful to give a confidence interval for the difference in the means of the Treatment and Control in addition to the results of the hypothesis test. The confidence interval gives a range of plausible values for the size of the effect of the Treatment whereas the hypothesis test only determines if there is a statistically significant difference in the mean."
- Key point: Besides the hypothesis test result, report a confidence interval for the difference in means; the interval gives a range of plausible effect sizes, while the test only says whether the difference is significant.
