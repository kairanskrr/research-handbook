# Online controlled experiments (A/B tests): randomize real users of a live product and compare metrics

This page is about **online controlled experiments**, which industry usually calls **A/B tests**. You take the real users of a running website, app, or service and randomly split them into two groups: one gets the existing version (the control), the other gets the new version (the treatment). Then you compare the two groups' metrics[^kohavi2009controlled-e1].

How it relates to nearby pages `[Our analysis]`:

- [Controlled experiments](controlled_experiment.md) covers studies where the researcher recruits participants and compares how people perform under controlled conditions. An online controlled experiment follows the same logic, but the participants are the product's real users, who usually don't know they are in an experiment, and what you measure is the behavioral data they leave while using the product as they normally would.
- [Field experiments](field_experiment.md) covers working with a government, firm, or community to randomize an intervention in the real world. You can think of an online controlled experiment as a field experiment inside a software product, except that the product team runs it themselves, samples often run to hundreds of thousands of people, and a single experiment lasts only a few weeks. The field experiments page's discussion of the unit of randomization, spillovers, and ethics applies here too.
- If what you are comparing is the system or model itself, and no real users are needed, see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md). Statistical testing in general is covered in [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md) and not repeated here.

**Scope** `[Our analysis]`: almost all the sources for this page come from experimentation teams in the software industry (Microsoft's Bing and MSN, Booking.com, and the commercial A/B testing platform Optimizely), published at the data mining conference KDD (the ACM SIGKDD Conference on Knowledge Discovery and Data Mining) and in the journal *Data Mining and Knowledge Discovery*. The ethics section draws on the controversy over Facebook's emotional contagion experiment. So what this page describes is how to work when you have a high-traffic product. Academic researchers who run this kind of experiment in human-computer interaction, information systems, or computational social science usually have to partner with a platform, or run it on a website or course platform they operate themselves; traffic is much lower, and ethics review follows their own institution's rules. For online randomized experiments in marketing or economics, check your field's norms and [Field experiments](field_experiment.md) first.

**Strategies it usually serves**: [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Causal explanation](../05_research-strategies/explain_causality.md), [Building and improving](../05_research-strategies/build_improve.md).

**After reading this page, you should be able to:**

- judge whether your question suits an online controlled experiment, and whether you have what it takes to run one;
- fix the overall evaluation criterion, the guardrail metrics, and the unit of randomization in advance, and work out how long to run;
- use A/A tests and a sample ratio check to confirm the experiment itself can be trusted;
- avoid the common traps of peeking, novelty effects, and interference between groups, and handle informed consent properly.

---

## 1. What this kind of study is, and when to use it

The key word is "random": you can't split users any old way, and nothing may influence who ends up in which group. If the experiment is designed and run correctly, the only systematic difference between the two groups is the change itself, so any difference in the metrics can be attributed to it[^kohavi2009controlled-e2]. That is what separates it from post-hoc analysis or quasi-experiments such as interrupted time series: it tests for causal relationships[^kohavi2009controlled-e25].

**Why run an experiment instead of trusting judgment.** Ideas succeed far less often than people expect: of the ideas tested in experiments at Microsoft, only a third improved the metric they were designed to improve[^kohavi2012trustworthy-e2].

**Questions it answers well** `[Our analysis]`:

- "If we ship feature X to real users, how much does some behavioral metric change?" For example, changing a button or switching to a different recommendation ranking. It isn't limited to interface changes: backend algorithm changes (such as to a search algorithm) can be evaluated the same way, and this is often overlooked[^kohavi2009controlled-e26].
- "Is the model that looks better in offline evaluation still better in real use?" This is exactly the gap between offline evaluation and real-world effect.

**Questions it answers poorly:**

- **Why.** It tells you which version is better and by how much, but not the reason. User studies in a usability lab capture users' comments and can fill that gap[^kohavi2009controlled-e12]. For that kind of study, see [Controlled experiments](controlled_experiment.md) and [Interview studies](interview_study.md).
- **Long-term effects.** It measures the effect during the experiment period, typically a few weeks[^kohavi2009controlled-e13].
- **Things that don't exist yet.** The feature has to be built, and be of good enough quality to put in front of real users[^kohavi2009controlled-e15]. Refine early ideas with prototypes and user studies first `[Our analysis]`.

**How it differs from related methods** `[Our analysis]`:

| | Online controlled experiment | [Controlled experiments](controlled_experiment.md) | [Field experiments](field_experiment.md) | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | [Quasi-experiment](quasi_experiment.md) |
|---|---|---|---|---|---|
| Who takes part | The product's real users, usually unaware | Recruited participants who sign a consent form | Real-world individuals, villages, schools | No people, only systems or models | People involved in something that already happened |
| Who runs it | The product team (or researchers working with them) | The researcher | A partner government, organization, or firm | The researcher | No one runs it for the study |
| Scale and duration | Thousands of people or more, days to weeks | Dozens of people, an hour or two | Hundreds to thousands of units, months to years | One benchmark | Whatever existing data there is |
| Main difficulties | Choosing metrics, data quality, peeking, interference between groups | Artificial setting, few participants | Implementation drift, attrition, spillovers | Whether the benchmark is valid | Arguing assignment was "as good as random" |

**Do you have what it takes** `[Our analysis]`: an online controlled experiment needs a product with real users, a way to split traffic by user, and logging of user behavior. Students and academic researchers often have none of these. The usual ways out: partner with a company or an open-source platform; run it on a tool, plugin, or course platform you operate yourself; or step back and recruit participants for a [Controlled experiments](controlled_experiment.md).

**Example: would the running example use it?** `[Our analysis]` The project "published evaluations of large language model vulnerability detectors are inflated by data leakage" is itself an offline evaluation. Its main method is [Benchmarking](../07_fields/computer-science/practices/benchmarking.md), and it doesn't need an online controlled experiment. But imagine a follow-up: you partner with a smart contract auditing platform, and the platform wants to know whether the model that does better on the new leakage-free benchmark actually helps auditors confirm more real vulnerabilities once it is deployed. Now you can run an online controlled experiment: randomly assign audit tasks to an "old model's hints" group and a "new model's hints" group. The overall evaluation criterion is the number of real vulnerabilities confirmed per task; the guardrail metric is the time auditors spend dealing with false positives. The steps below keep using this scenario.

---

## 2. How to do it

A typical online experiment runs like this from start to finish: define the metrics → choose the unit of randomization → compute the sample size → run an A/A test first, then ramp up from a small share of traffic → run for the full planned time → check data quality first, then look at the results `[Our analysis]`.

### Step 1: Define the overall evaluation criterion, plus guardrail and data quality metrics

**How:**

- The **overall evaluation criterion** (OEC) is a quantitative measure of the experiment's objective, and the ship decision rests on it. A good OEC shouldn't focus on the short term (such as clicks); it should include factors that predict long-term goals, such as users' predicted lifetime value and repeat visits[^kohavi2009controlled-e3]. Ideally choose a single metric, which can be a weighted combination of several objectives. That way the tradeoffs are made once, and every experiment shares one clear objective[^kohavi2009controlled-e4].
- **Guardrail metrics** don't tell you directly whether the change succeeded, but you can't ship if they get significantly worse. Page load time is a typical example[^dmitriev2017dirty-e2].
- **Data quality metrics** answer the first question: was the experiment configured and run correctly, and can the results be trusted[^dmitriev2017dirty-e3]? The sample ratio described in Step 6 below is the most important of these.
- **Break ratio metrics apart**: for metrics like click-through rate, also define and report the counts for the numerator and the denominator[^dmitriev2017dirty-e4].
- **Fix them before the experiment starts**, and agree with everyone involved on how the experiment will be evaluated[^kohavi2009controlled-e21].

**Why:** short-term metrics can point the opposite way from your real goal. In one Bing experiment, a bug showed users very poor search results, and queries per user went up by more than 10% while revenue per user went up by more than 30%[^kohavi2012trustworthy-e4]. The worse the results, the more users searched. And picking metrics after the fact makes it easier to find results that look significant by chance[^kohavi2009controlled-e7].

**Where people go wrong:** the metric doesn't measure what you meant it to. In one Microsoft experiment, "users clicked more" turned out to be nothing more than the two groups' instrumentation (the code that logs user behavior) losing data at different rates[^kohavi2012trustworthy-e6]. The authors file this kind of problem under measure validity: the extent to which a metric captures the concept you intended to measure[^kohavi2012trustworthy-e11]. For validity in general, see [Validity and limitations](../02_do-the-project/04_validity-and-limits.md).

Example, continued `[Our analysis]`: in the auditing platform's experiment, "number of vulnerabilities flagged by the model" is a bad OEC, because it also rises when the model reports more false positives. "Number of real vulnerabilities confirmed by auditors" is closer to the goal. The time auditors spend on each task serves as a guardrail metric.

### Step 2: Choose the unit of randomization

**How:**

- On the web the most common unit is the user. Some metrics are computed per user-day, per session, or per page view, but in every case randomizing by user is preferred. Each user should see the same version throughout the experiment, which is usually done with a user ID stored in a cookie[^kohavi2009controlled-e5][^kohavi2012trustworthy-e1].
- The assignment code has to meet three conditions: every user is equally likely to see each version; the same user gets the same version on every visit; and when several experiments run at once, their assignments are uncorrelated[^kohavi2009controlled-e16].

**Why:** the statistical analysis assumes the units are independent[^kohavi2009controlled-e5]. If a user sees different versions on different visits, or one unit's outcome is affected by how other units were assigned, that assumption breaks `[Our analysis]`.

**Where people go wrong: interference between groups.** In some settings the treatment group affects the control group. Say an auction site gives some users a "first bid" incentive: the treatment affects every item up for auction, so randomizing by user can't measure the true effect. Here you randomize items instead of users[^kohavi2009controlled-e23]. Social networks and two-sided marketplaces often have the same problem; for how to avoid and measure these spillovers, see the [Think through spillovers](field_experiment.md#step-9-think-through-spillovers) step on the field experiments page `[Our analysis]`.

**Where people go wrong: carryover from the previous experiment.** Some platforms reuse the same "buckets" of users, so users affected by one experiment end up in the next. In one case, three months later those users still hadn't returned to their pre-experiment levels[^kohavi2012trustworthy-e10].

Example, continued `[Our analysis]`: if the same auditor sometimes works with the old model and sometimes with the new one, lessons learned on one side carry over to the other; randomizing by auditor is safer. If auditors on the same team share their findings with each other, randomize by team.

### Step 3: Compute the sample size and the duration

**How:** decide on the statistical power (the probability of detecting a difference that really exists) and the size of effect you want to detect, estimate the metric's variability with an A/A test (see Step 4), and from these compute the minimum sample size and how long you need to run[^kohavi2009controlled-e18].

- **The sample may need to be much larger than you think.** In the paper's e-commerce example, detecting a 5% change in revenue with 80% power takes more than 409,000 users[^kohavi2009controlled-e9].
- **Reduce variability.** Leave out of the analysis the users who never encountered the change. If you changed the checkout page, for instance, analyze only users who reached the checkout page[^kohavi2009controlled-e8].
- **Split 50/50.** To maximize power and minimize running time, the recommendation is 50% per group; at a 99%/1% split, you have to run about 25 times longer[^kohavi2009controlled-e19].
- **Run in whole weeks.** Even with heavy traffic, run for at least a week or two, and extend in multiples of a week so you can analyze day-of-week effects[^kohavi2009controlled-e20].
- **Do an a priori power analysis, at least for the OEC and the guardrail metrics**[^dmitriev2017dirty-e6].

**Why:** a common mistake is running underpowered experiments[^kohavi2009controlled-e18]. When an experiment is underpowered, a nonsignificant result doesn't mean there was no effect[^dmitriev2017dirty-e6]; and if the result happens to be significant, the observed change is more likely to exaggerate the true effect[^dmitriev2017dirty-e7].

**Where people go wrong:** assuming "the longer you run, the more precise it gets." For some metrics, such as sessions per user, the confidence interval doesn't shrink over time, and running longer adds no power[^kohavi2012trustworthy-e9]. For statistical power in general, see [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 4: Run an A/A test first, then ramp up from a small share of traffic

**How:**

- **A/A test**: split users into two groups as usual, but show both groups exactly the same version. It has two uses: estimating the data's variability for the power calculation, and testing the experimentation system itself. At a 95% confidence level, it should come out "significant" only about 5% of the time[^kohavi2009controlled-e6]. Check three things: are users split in the planned proportions, does the collected data match the system of record, and are the results nonsignificant 95% of the time? And run A/A tests continuously, in parallel with your other experiments[^kohavi2009controlled-e17].
- **Look back at the pre-experiment period**: compute the two groups' metrics on data from a stretch of time before the experiment started, and confirm that the randomly split groups didn't already differ much on key metrics[^fabijan2019diagnosing-e7].
- **Ramp up gradually**: start by exposing a very small share of users to the treatment, check at each step for serious problems, and only then show it to more users[^kohavi2009controlled-e11].

**Why:** the A/A test has been the Microsoft experimentation team's most useful tool for finding problems in real systems[^kohavi2012trustworthy-e3]. Robot traffic, for example, can badly skew estimates: the authors have seen robots push an A/A test's false positive rate far above 5%[^kohavi2009controlled-e10].

**Where people go wrong:** treating the A/A test as a one-time check before launch. The experimentation system, the instrumentation, and the traffic all keep changing, so run it continuously[^kohavi2009controlled-e17].

### Step 5: Run for the full planned time; watch the guardrails, not the result

**How:** make the ship decision at the time point you fixed in advance. If you really do need to look at the result as you go, use a method designed for it: adjust the p-values to account for the extra looks, switch to a Bayesian framework that allows continuous monitoring[^dmitriev2017dirty-e10], or use "always valid" p-values and confidence intervals, which control the false positive rate no matter when you stop[^johari2015always-e3].

**Why:** checking the results over and over and stopping as soon as they turn significant raises the chance of a false positive; stopping early and extending the experiment are both very common mistakes[^dmitriev2017dirty-e9]. If the experimenter watches the results while deciding when to stop, ordinary p-values and confidence intervals are wholly unreliable[^johari2015always-e1]. Industry usually makes no correction for this, and even with just 10,000 samples the false positive rate can easily go up fivefold[^johari2015always-e2].

**Where people go wrong:** confusing monitoring with peeking at the result. You must monitor an experiment continuously so you can shut it down quickly if the user experience gets clearly worse, and that is exactly what makes this problem hard[^dmitriev2017dirty-e11]. `[Our analysis]` You can keep the two apart: watch the guardrail and data quality metrics at any time and use them to stop the experiment; use the OEC only at the planned time point, to make the decision.

**Don't be fooled by early "trends" either.** Most experiments actually have a stable effect, but in the first few days there is little data and a lot of noise, so early results are often misleading[^kohavi2012trustworthy-e7].

### Step 6: Before analyzing, check the sample ratio

**How:** before looking at the result, use a chi-square test to compare the actual number of users in each group with the configured split[^fabijan2019diagnosing-e2]. When the group sizes depart from the expected ratio, that is a **sample ratio mismatch** (SRM). It means something went wrong with the sampling process, very likely a bug[^dmitriev2017dirty-e1][^kohavi2012trustworthy-e5]. When the test says the difference is unlikely to be chance, you must find the root cause[^fabijan2019diagnosing-e2].

**Why:**

- **It invalidates the results.** An SRM introduces selection bias, which invalidates any causal inference drawn from the experiment[^fabijan2019diagnosing-e4].
- **Take small deviations seriously too.** A 50.2/49.8 split (821,588 versus 815,482 users) looks very close to 50/50, but the probability that it happened by chance is less than 1 in 500,000[^fabijan2019diagnosing-e1].
- **It isn't rare.** About 6% of the experiments Microsoft ran over roughly a year showed an SRM[^fabijan2019diagnosing-e3].
- **It can flip the conclusion.** An MSN experiment on a carousel first showed engagement going down; once the issue causing the SRM was fixed, the change turned out to have significantly increased engagement[^fabijan2019diagnosing-e6].

**Where people go wrong:** checking only the overall split and not each metric. The cause can sit anywhere in experiment design, randomization, variant deployment, data logging, collection, processing ("cooking"), or analysis[^fabijan2019diagnosing-e5]. For example, different rates of telemetry loss (telemetry being the usage records a product sends back automatically) between the groups is a common way results get biased[^dmitriev2017dirty-e5]; and when you filter outliers, make sure the filtering rule affects every group the same way[^dmitriev2017dirty-e16].

**A general reminder:** any unexpected metric movement, positive or negative, usually means something is wrong (Twyman's law)[^dmitriev2017dirty-e14]. When a result looks too good to be true, check the data before you celebrate `[Our analysis]`.

### Step 7: Interpret the results: effect size, novelty effects, and segments

**How:**

- **Report confidence intervals.** Besides the test result, give a confidence interval for the difference between the two groups; it shows roughly how big the effect is[^kohavi2009controlled-e27].
- **Check whether the effect changes over time.** Watch for two effects that pull in opposite directions. Experienced users have to get used to a new navigation and are less efficient at first: this is the primacy effect. Users who are curious about a new design click around everywhere: this is the novelty effect. One remedy is to look only at new users, who are affected by neither[^kohavi2009controlled-e14]. You can also break the effect down by day of the experiment or by user visit[^dmitriev2017dirty-e13].
- **Be careful with segment analysis.** The condition that defines a segment must not itself be affected by the treatment; and slicing users into ever-finer segments until one turns up significant is a multiple testing problem that raises the false positive rate[^dmitriev2017dirty-e12]. But do look at important user groups: a change that helps overall can badly hurt one group of users[^dmitriev2017dirty-e15].
- **Rerun when the p-value is borderline.** One positive result at Microsoft with a p-value of 0.029 was no longer significant when rerun with double the traffic. The authors recommend putting weight on strongly significant metrics, and rerunning with more traffic when the OEC's p-value is borderline[^dmitriev2017dirty-e8].

**Why:** most suspected novelty and primacy effects aren't real, just statistical artifacts[^kohavi2012trustworthy-e8]. Plot how the effect changes over time before drawing a conclusion `[Our analysis]`.

**Where people go wrong:** shipping a nonsignificant change on the grounds that "it doesn't hurt anyway." Nonsignificant can mean there really is no difference, or that the experiment was underpowered and the change is in fact harmful[^kohavi2009controlled-e22].

### Step 8: Handle ethics and informed consent properly

**A cautionary example.** In 2014, Facebook researchers published an experiment on 689,003 people in PNAS (*Proceedings of the National Academy of Sciences*)[^kramer2014experimental-e1]. The treatment reduced the emotional content in users' News Feeds[^kramer2014experimental-e2]. The authors held that the data use policy users agreed to when they signed up constituted informed consent[^kramer2014experimental-e3]. After publication, the study was questioned on two principles: informed consent and allowing participants to opt out[^verma2014editorial-e1]. Cornell University's institutional review board concluded that because Facebook ran the experiment for internal purposes, it fell outside the university's jurisdiction[^verma2014editorial-e2]; and Facebook, as a private company, was not obliged to follow the Common Rule, the US rules for protecting human subjects[^verma2014editorial-e3]. The journal still published an Editorial Expression of Concern, saying it was concerned that the data collection may not have been fully consistent with the principles of informed consent and allowing participants to opt out[^verma2014editorial-e4].

**What to do as a result** `[Our analysis]`:

- **That companies routinely run A/B tests internally doesn't mean your study can skip ethics review.** If you take part as an academic researcher and plan to publish, apply for review under your institution's rules, explaining how users will be affected, what they will be told, and whether they can opt out. For the general requirements, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); for the ethics of randomized experiments in real settings, see the [Handle the ethics of working in real communities](field_experiment.md#step-10-handle-the-ethics-of-working-in-real-communities) step on the field experiments page.
- **Think through whether the treatment could hurt people.** Changing a button color carries completely different risks from manipulating the emotional content, prices, or health information users see. Some treatments are inappropriate to randomize by user even when they are legal. When testing prices, for example, customers who find out others got a different price can sour customer relations; you can randomize products instead[^kohavi2009controlled-e24].
- **Protect the data.** Experiment logs are user behavior data. Handle them under privacy rules, and remove identifying information before releasing anything.

---

## 3. Checklist

This list is drawn mainly from experience papers by the experimentation teams at Microsoft and other companies. It reflects industry practice, not any professional society's review standard; in an academic paper, you also have to meet your field's requirements for reporting experiments `[Our analysis]`.

**Must do**

- [ ] Fix the OEC before the experiment starts, and agree with everyone involved on how it will be evaluated[^kohavi2009controlled-e7][^kohavi2009controlled-e21]
- [ ] Randomize by user (or by a unit large enough to contain interference), and show each user the same version throughout[^kohavi2009controlled-e5][^kohavi2009controlled-e16]
- [ ] Do an a priori power analysis, at least for the OEC and the guardrail metrics, and fix the sample size and duration[^dmitriev2017dirty-e6]
- [ ] Check the sample ratio before analyzing; if there is a mismatch, find the cause rather than using the results as they are[^fabijan2019diagnosing-e2][^fabijan2019diagnosing-e4]
- [ ] Don't stop early because a peek shows significance; if you need to look as you go, use methods designed for continuous monitoring[^dmitriev2017dirty-e9][^dmitriev2017dirty-e10]
- [ ] Report the effect's confidence interval, not just "significant / not significant"[^kohavi2009controlled-e27]
- [ ] When publishing as academic research, pass your institution's ethics review and describe the informed consent and opt-out arrangements `[Our analysis]`

**Better practice**

- [ ] Run A/A tests continuously, checking the split proportions, agreement between your data and the system of record, and a false positive rate of about 5%[^kohavi2009controlled-e17]
- [ ] Set guardrail and data quality metrics; report the numerator and denominator alongside ratio metrics[^dmitriev2017dirty-e2][^dmitriev2017dirty-e4]
- [ ] Start with a small share of traffic and ramp up gradually[^kohavi2009controlled-e11]
- [ ] Run in whole weeks, for at least a week or two[^kohavi2009controlled-e20]
- [ ] Look at the effect by day and by visit, to check for novelty and primacy effects[^dmitriev2017dirty-e13]
- [ ] Look back at the pre-experiment period to confirm the groups didn't already differ[^fabijan2019diagnosing-e7]

**Outstanding**

- [ ] When the OEC's p-value is borderline, run an independent rerun with more traffic[^dmitriev2017dirty-e8]
- [ ] Use interviews or usability studies to fill in the "why"[^kohavi2009controlled-e12]

**Fine to skip; not a flaw** `[Our analysis]`

- Looking only at the overall effect, with no segment analysis: segment analysis is exploratory, and doing it means you then have to deal with multiple testing; if you do it, label it exploratory, see [Do the planned analyses first; label unplanned ones as exploratory](../02_do-the-project/07_analyze-and-interpret.md#2-run-the-planned-analyses-first-label-unplanned-ones-as-exploratory)
- When traffic is too low to split 50/50 or to run for several full weeks, do what you can, but state the limits on power in the paper

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Using short-term clicks or query counts as the OEC | They can point the opposite way from long-term goals: the product gets worse and the metric goes up[^kohavi2012trustworthy-e4] |
| Choosing metrics after seeing the results | It's easier to find significant results by chance[^kohavi2009controlled-e7] |
| Stopping as soon as it's significant, extending when it isn't | The false positive rate goes up[^dmitriev2017dirty-e9] |
| Reading the result without checking the sample ratio | Selection bias invalidates causal inference, and the conclusion may even be reversed[^fabijan2019diagnosing-e4][^fabijan2019diagnosing-e6] |
| Running underpowered, then treating "not significant" as "no effect" | The change may be harmful and you just didn't detect it[^kohavi2009controlled-e22][^dmitriev2017dirty-e6] |
| Extrapolating from the first few days' trend | Early data is noisy and often misleading[^kohavi2012trustworthy-e7] |
| Slicing users into segments until one turns up significant | Multiple testing raises the false positive rate[^dmitriev2017dirty-e12] |
| Randomizing by user when the treatment group affects the control group | You can't measure the true effect[^kohavi2009controlled-e23] |
| Shipping straight away when the result is surprisingly good | An unexpected metric movement usually means something is wrong[^dmitriev2017dirty-e14] |
| Assuming the company's data policy amounts to informed consent | Journals and the research community will still question it[^verma2014editorial-e4] |

---

## 5. Further reading

- **Introduction and overview**: Kohavi et al. 2009, a survey and practical guide in *Data Mining and Knowledge Discovery*, covering the OEC, power and sample size, randomization algorithms, limitations, and a batch of lessons from practice. Most of the practical advice on this page comes from it.
- **Why results can't be trusted**: Kohavi et al. 2012, which uses five puzzling real results to discuss metric choice, instrumentation, early trends, power, and carryover effects.
- **How to interpret metrics**: Dmitriev et al. 2017, twelve common pitfalls in interpreting metrics, each with a real example.
- **Sample ratio mismatch**: Fabijan et al. 2019, a taxonomy of its causes and how to diagnose them.
- **The statistics of peeking**: Johari et al.'s "always valid inference," for readers who want to monitor experiments continuously; it needs some statistical background.
- **The ethics controversy**: Kramer et al. 2014 and the PNAS Editorial Expression of Concern; read the two together.

For links to every source, see the [source list](../../sources/README.md).

[^kohavi2009controlled-e1]: Kohavi et al. 2009, §1, p. 142. [Evidence](../../sources/notes/kohavi2009controlled.md#e1)
[^kohavi2009controlled-e2]: Kohavi et al. 2009, §3, p. 149. [Evidence](../../sources/notes/kohavi2009controlled.md#e2)
[^kohavi2009controlled-e3]: Kohavi et al. 2009, §3.1, p. 150. [Evidence](../../sources/notes/kohavi2009controlled.md#e3)
[^kohavi2009controlled-e4]: Kohavi et al. 2009, §3.1, p. 150. [Evidence](../../sources/notes/kohavi2009controlled.md#e4)
[^kohavi2009controlled-e5]: Kohavi et al. 2009, §3.1, p. 150. [Evidence](../../sources/notes/kohavi2009controlled.md#e5)
[^kohavi2009controlled-e6]: Kohavi et al. 2009, §3.1, p. 151. [Evidence](../../sources/notes/kohavi2009controlled.md#e6)
[^kohavi2009controlled-e7]: Kohavi et al. 2009, §3.2.4, p. 154. [Evidence](../../sources/notes/kohavi2009controlled.md#e7)
[^kohavi2009controlled-e8]: Kohavi et al. 2009, §3.2, p. 151. [Evidence](../../sources/notes/kohavi2009controlled.md#e8)
[^kohavi2009controlled-e9]: Kohavi et al. 2009, §3.2.1, p. 153. [Evidence](../../sources/notes/kohavi2009controlled.md#e9)
[^kohavi2009controlled-e10]: Kohavi et al. 2009, §3.4, p. 155. [Evidence](../../sources/notes/kohavi2009controlled.md#e10)
[^kohavi2009controlled-e11]: Kohavi et al. 2009, §3.5.1, p. 156. [Evidence](../../sources/notes/kohavi2009controlled.md#e11)
[^kohavi2009controlled-e12]: Kohavi et al. 2009, §3.6, p. 157. [Evidence](../../sources/notes/kohavi2009controlled.md#e12)
[^kohavi2009controlled-e13]: Kohavi et al. 2009, §3.6, p. 157. [Evidence](../../sources/notes/kohavi2009controlled.md#e13)
[^kohavi2009controlled-e14]: Kohavi et al. 2009, §3.6, p. 158. [Evidence](../../sources/notes/kohavi2009controlled.md#e14)
[^kohavi2009controlled-e15]: Kohavi et al. 2009, §3.6, p. 158. [Evidence](../../sources/notes/kohavi2009controlled.md#e15)
[^kohavi2009controlled-e16]: Kohavi et al. 2009, §5.1, pp. 163–164. [Evidence](../../sources/notes/kohavi2009controlled.md#e16)
[^kohavi2009controlled-e17]: Kohavi et al. 2009, §6.2.1, p. 174. [Evidence](../../sources/notes/kohavi2009controlled.md#e17)
[^kohavi2009controlled-e18]: Kohavi et al. 2009, §6.2.3, p. 175. [Evidence](../../sources/notes/kohavi2009controlled.md#e18)
[^kohavi2009controlled-e19]: Kohavi et al. 2009, §6.2.4, p. 175. [Evidence](../../sources/notes/kohavi2009controlled.md#e19)
[^kohavi2009controlled-e20]: Kohavi et al. 2009, §6.2.5, p. 175. [Evidence](../../sources/notes/kohavi2009controlled.md#e20)
[^kohavi2009controlled-e21]: Kohavi et al. 2009, §6.3.1, p. 176. [Evidence](../../sources/notes/kohavi2009controlled.md#e21)
[^kohavi2009controlled-e22]: Kohavi et al. 2009, §6.3.2, p. 176. [Evidence](../../sources/notes/kohavi2009controlled.md#e22)
[^kohavi2009controlled-e23]: Kohavi et al. 2009, Appendix A, p. 178. [Evidence](../../sources/notes/kohavi2009controlled.md#e23)
[^kohavi2009controlled-e24]: Kohavi et al. 2009, Appendix A, p. 179. [Evidence](../../sources/notes/kohavi2009controlled.md#e24)
[^kohavi2009controlled-e25]: Kohavi et al. 2009, §1, p. 142. [Evidence](../../sources/notes/kohavi2009controlled.md#e25)
[^kohavi2009controlled-e26]: Kohavi et al. 2009, §2.4, p. 146. [Evidence](../../sources/notes/kohavi2009controlled.md#e26)
[^kohavi2009controlled-e27]: Kohavi et al. 2009, §3.3, p. 154. [Evidence](../../sources/notes/kohavi2009controlled.md#e27)
[^kohavi2012trustworthy-e1]: Kohavi et al. 2012, §1, p. 1. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e1)
[^kohavi2012trustworthy-e2]: Kohavi et al. 2012, §1, p. 2. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e2)
[^kohavi2012trustworthy-e3]: Kohavi et al. 2012, §2, p. 3. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e3)
[^kohavi2012trustworthy-e4]: Kohavi et al. 2012, §3.1.2, p. 3. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e4)
[^kohavi2012trustworthy-e5]: Kohavi et al. 2012, §3.1.3, p. 4. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e5)
[^kohavi2012trustworthy-e6]: Kohavi et al. 2012, §3.2.3, p. 4. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e6)
[^kohavi2012trustworthy-e7]: Kohavi et al. 2012, §3.3.4, p. 6. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e7)
[^kohavi2012trustworthy-e8]: Kohavi et al. 2012, §3.3.1, p. 5. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e8)
[^kohavi2012trustworthy-e9]: Kohavi et al. 2012, §3.4.2, p. 6. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e9)
[^kohavi2012trustworthy-e10]: Kohavi et al. 2012, §3.5.3, pp. 7–8. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e10)
[^kohavi2012trustworthy-e11]: Kohavi et al. 2012, §4, p. 8. [Evidence](../../sources/notes/kohavi2012trustworthy.md#e11)
[^dmitriev2017dirty-e1]: Dmitriev et al. 2017, §4. [Evidence](../../sources/notes/dmitriev2017dirty.md#e1)
[^dmitriev2017dirty-e2]: Dmitriev et al. 2017, §4. [Evidence](../../sources/notes/dmitriev2017dirty.md#e2)
[^dmitriev2017dirty-e3]: Dmitriev et al. 2017, §4. [Evidence](../../sources/notes/dmitriev2017dirty.md#e3)
[^dmitriev2017dirty-e4]: Dmitriev et al. 2017, §5.2. [Evidence](../../sources/notes/dmitriev2017dirty.md#e4)
[^dmitriev2017dirty-e5]: Dmitriev et al. 2017, §5.3. [Evidence](../../sources/notes/dmitriev2017dirty.md#e5)
[^dmitriev2017dirty-e6]: Dmitriev et al. 2017, §5.4. [Evidence](../../sources/notes/dmitriev2017dirty.md#e6)
[^dmitriev2017dirty-e7]: Dmitriev et al. 2017, §5.4. [Evidence](../../sources/notes/dmitriev2017dirty.md#e7)
[^dmitriev2017dirty-e8]: Dmitriev et al. 2017, §5.5. [Evidence](../../sources/notes/dmitriev2017dirty.md#e8)
[^dmitriev2017dirty-e9]: Dmitriev et al. 2017, §5.6. [Evidence](../../sources/notes/dmitriev2017dirty.md#e9)
[^dmitriev2017dirty-e10]: Dmitriev et al. 2017, §5.6. [Evidence](../../sources/notes/dmitriev2017dirty.md#e10)
[^dmitriev2017dirty-e11]: Dmitriev et al. 2017, §5.6. [Evidence](../../sources/notes/dmitriev2017dirty.md#e11)
[^dmitriev2017dirty-e12]: Dmitriev et al. 2017, §5.8. [Evidence](../../sources/notes/dmitriev2017dirty.md#e12)
[^dmitriev2017dirty-e13]: Dmitriev et al. 2017, §5.10. [Evidence](../../sources/notes/dmitriev2017dirty.md#e13)
[^dmitriev2017dirty-e14]: Dmitriev et al. 2017, §5.12. [Evidence](../../sources/notes/dmitriev2017dirty.md#e14)
[^dmitriev2017dirty-e15]: Dmitriev et al. 2017, §5.7. [Evidence](../../sources/notes/dmitriev2017dirty.md#e15)
[^dmitriev2017dirty-e16]: Dmitriev et al. 2017, §5.9. [Evidence](../../sources/notes/dmitriev2017dirty.md#e16)
[^fabijan2019diagnosing-e1]: Fabijan et al. 2019, §2.3.1. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e1)
[^fabijan2019diagnosing-e2]: Fabijan et al. 2019, §2.3.1. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e2)
[^fabijan2019diagnosing-e3]: Fabijan et al. 2019, §4.1. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e3)
[^fabijan2019diagnosing-e4]: Fabijan et al. 2019, §4.2. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e4)
[^fabijan2019diagnosing-e5]: Fabijan et al. 2019, §4.3. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e5)
[^fabijan2019diagnosing-e6]: Fabijan et al. 2019, §1. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e6)
[^fabijan2019diagnosing-e7]: Fabijan et al. 2019, §5.1. [Evidence](../../sources/notes/fabijan2019diagnosing.md#e7)
[^johari2015always-e1]: Johari et al., arXiv 1512.04922, Abstract. [Evidence](../../sources/notes/johari2015always.md#e1)
[^johari2015always-e2]: Johari et al., arXiv 1512.04922, §1. [Evidence](../../sources/notes/johari2015always.md#e2)
[^johari2015always-e3]: Johari et al., arXiv 1512.04922, §1. [Evidence](../../sources/notes/johari2015always.md#e3)
[^kramer2014experimental-e1]: Kramer et al. 2014, Significance. [Evidence](../../sources/notes/kramer2014experimental.md#e1)
[^kramer2014experimental-e2]: Kramer et al. 2014, Abstract. [Evidence](../../sources/notes/kramer2014experimental.md#e2)
[^kramer2014experimental-e3]: Kramer et al. 2014, Materials and Methods. [Evidence](../../sources/notes/kramer2014experimental.md#e3)
[^verma2014editorial-e1]: Verma 2014, PNAS Editorial Expression of Concern. [Evidence](../../sources/notes/verma2014editorial.md#e1)
[^verma2014editorial-e2]: Verma 2014, PNAS Editorial Expression of Concern. [Evidence](../../sources/notes/verma2014editorial.md#e2)
[^verma2014editorial-e3]: Verma 2014, PNAS Editorial Expression of Concern. [Evidence](../../sources/notes/verma2014editorial.md#e3)
[^verma2014editorial-e4]: Verma 2014, PNAS Editorial Expression of Concern. [Evidence](../../sources/notes/verma2014editorial.md#e4)
