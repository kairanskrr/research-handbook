# Quasi-experiments and causal identification

This page is about how economists **estimate causal effects from observational data when they cannot randomize**. Observational data means data that already exists, where the researcher did not assign who gets treated. The page goes in this order: first write down your identification strategy; then choose difference-in-differences, regression discontinuity, instrumental variables, or synthetic control; then run placebo tests, get the standard errors right, and report the results clearly. For the background of the "credibility revolution" and a one-line summary of the assumption each method rests on, see the [Economics and business field overview](../07_fields/economics/README.md#the-credibility-revolution-first-answer-whats-your-identification-strategy); we don't repeat it here. Public health and medicine also estimate causal effects from observational data, but with different vocabulary; see [Observational epidemiology](observational_epidemiology.md). A table mapping the two vocabularies is at the end of Section 1. For general concepts such as threats to validity and exploratory versus confirmatory analysis, see the Part 2 chapters [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md) and [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring).

**Scope** `[Our analysis]`: this page was written for [Economics and business](../07_fields/economics/README.md), and its sources are mostly causal inference textbooks and methods papers from economics (Cunningham's online textbook, Angrist and Pischke's article on the "credibility revolution", and reviews of difference-in-differences, regression discontinuity, clustered standard errors, and so on). So the vocabulary below, and what we say is "most important to check", follow economics conventions. The field overviews for [Health sciences](../07_fields/health-sciences/README.md) and [Political science](../07_fields/political-science/README.md) also point here. If you use these methods in another field, check that field's conventions first; for the corresponding practice in health research, see [Observational epidemiology](observational_epidemiology.md).

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md).


**After reading this page, you should be able to:**

- write your identification strategy in one paragraph: what you are estimating, who you compare with whom, and which assumptions you rely on;
- carry out difference-in-differences, regression discontinuity, and instrumental variables analyses step by step, and know what matters most to check for each;
- judge when synthetic control is worth considering;
- run placebo and robustness checks, and cluster standard errors at the right level;
- avoid common traps such as "the pre-trends aren't significant, so we're fine" and "the first-stage F is above 10, so we're fine".

---

## 1. What this kind of research is and when to use it

Quasi-experimental research answers "how large is the causal effect of X on Y", for example whether a minimum wage policy reduced employment. When a randomized experiment isn't possible, it builds its comparison on variation created by institutional rules or natural events (see the field overview linked above).

**Look at how the treatment was assigned first, then choose the method.** The table below starts from the situation you are in `[Our analysis, based on the footnotes in each row]`:

| Your situation | Consider | Key assumptions | What matters most to check |
|---|---|---|---|
| A policy affected some units at some point in time while others were unaffected, and you have data before and after | Difference-in-differences | Without the policy, the two groups' average outcomes would have moved in parallel; the policy had no effect before it took effect[^roth2023trending-e1] | Pre-treatment trends; how sensitive the conclusion is to departures from parallel trends[^roth2023trending-e6] |
| Whether someone is treated depends on whether a score, age, distance, or similar crosses a cutoff | Regression discontinuity | People cannot **precisely** place themselves on one side of the cutoff[^lee2010rd-e1] | Whether people bunch near the cutoff; whether characteristics fixed beforehand are balanced on both sides[^lee2010rd-e2] |
| Some variable pushes people into treatment and has no other connection to the outcome | Instrumental variables | It really does change the treatment; it affects the outcome only through that channel; its value is as good as random[^angrist2010credibility-e5] | How strong the first stage is; whether the exclusion restriction is convincing |
| Only one or a few large units, such as a city or a state, are treated, and you have a long pre-treatment time series | Synthetic control | A weighted combination of comparison units closely tracks the treated unit before treatment[^cunningham2026remix-e15] | How well it fits before treatment; placebo tests[^cunningham2026remix-e17] |

None of the four methods relies on "controlling for every variable you can think of". They rely on what you know about **how the treatment was assigned** `[Our analysis]`. Before using an instrument, Cunningham suggests asking yourself: why should I believe it is as good as random? Why should I believe it satisfies the exclusion restriction? Be your own harshest critic[^cunningham2026remix-e7]. The same question applies to the other three methods `[Our analysis]`.

> **Economics and epidemiology vocabulary** `[Our analysis]`: the table below is our own rough mapping. The terms on the two sides are not equivalent; the table only helps you find the nearest concept when you read the other field's literature.
>
> | Economists say | Nearest term in epidemiology |
> |---|---|
> | Identification strategy (the argument for why a causal interpretation is justified) | No one-to-one equivalent. The closest practice is treating an observational analysis as an emulation of a hypothetical "target trial"[^hernan2018cword-e5] |
> | Omitted variable bias (leaving out a factor that affects both treatment and outcome) | Confounding; Hernán argues that when the goal is causal, you generally need to adjust for confounding[^hernan2018cword-e13] |
> | Control variables | Adjustment variables, covariates |
>
> The arguments also start from different places. A quasi-experimental paper in economics focuses on arguing "where the variation in treatment comes from and why it is as good as random"; the approach in [Observational epidemiology](observational_epidemiology.md) starts more from "which trial are we emulating, and which confounders do we adjust for". This is only our rough comparison of the sources read for the two pages.

---

## 2. How to do it

### Step 1: Write your identification strategy before you touch the data

**How:** Before you run any regression, write one paragraph that answers three questions:

1. **What you are estimating**: whose effect, over what period. In a difference-in-differences design, is it the average treatment effect on the treated units, or the effect after a particular point in time?
2. **Who you compare with whom**: who the comparison group is, and why you chose it.
3. **Which assumptions you rely on**: and why they are plausible in your setting.

Reviewing recent difference-in-differences methods, Roth et al. boil the main points down to three: be clear about the comparison group used for identification; match the estimation and inference methods to the identifying assumptions; and check how robust the conclusion is to violations of those assumptions. They also stress that choosing the right assumptions often depends on knowing the specific setting well[^roth2023trending-e11].

**Why:** For why economists put so much weight on the identification strategy, see the [Economics and business field overview](../07_fields/economics/README.md#the-credibility-revolution-first-answer-whats-your-identification-strategy).

**Where people go wrong:**

- **Changing the specification as the results come in.** Decide control variables, sample, and comparison group before you see the results, and say so openly[^cunningham2026remix-e14]. If you can't choose between two approaches in advance, report both[^cunningham2026remix-e13].
- **Mistaking a specification search for robustness.** Brodeur et al. tallied about 50,000 tests published in three economics journals (the American Economic Review, the Journal of Political Economy, and the Quarterly Journal of Economics) from 2005 to 2011 (2013 discussion-paper version) and found too many p-values just below 0.05. Their explanation: when a result is just short of significance, researchers may go looking for a "significant" specification[^brodeur2016star-e2][^brodeur2016star-e3]. In their data, papers using data from randomized controlled trials or lab experiments show less of this[^brodeur2016star-e5].
- **Not letting go when the design doesn't hold.** The last item on Cunningham's difference-in-differences checklist is "don't do difference-in-differences": if the hand you've been dealt is bad, switch methods early[^cunningham2026remix-e12].

### Step 2: Difference-in-differences

**The assumptions.** Standard difference-in-differences rests on two assumptions: without the policy, the treated and comparison groups' average outcomes would have moved in parallel (parallel trends); and the policy had no effect before it took effect (no anticipation)[^roth2023trending-e1]. Parallel trends allows the two groups to start at different levels, but the gap between them must be the same before and after the policy[^roth2023trending-e2].

**How:**

1. **Count first, then plot.** Count how many units are in each cohort (units first treated at the same time), including never-treated and always-treated units; plot how treatment rolls out over time; choose the comparison group and write down why[^cunningham2026remix-e11].
2. **Draw an event-study plot** and check whether the differences between the groups in the pre-treatment periods are close to zero[^roth2023trending-e6]. But remember: parallel trends can't itself be tested. What you actually need is for the counterfactual trends **after** treatment to be the same, and that is not the same thing as "parallel trends before treatment"[^cunningham2026remix-e9].
3. **Don't treat "insignificant pre-trends" as evidence.** These tests often have low power, and choosing your analysis based on a pre-test introduces bias of its own[^roth2023trending-e5]. Roth et al. argue that sensitivity analysis should be standard practice[^roth2023trending-e6], for example reporting how many times larger than the largest pre-treatment deviation the post-treatment deviation from parallel trends would have to be to overturn the conclusion[^roth2023trending-e7].
4. **With staggered adoption, don't just run the usual regression.** When units start treatment at different times, the usual two-way fixed effects regression (a regression that controls for both unit and time) uses already-treated units as controls. Roth et al. call these "forbidden comparisons": when treatment effects vary across units, the coefficient can even have the opposite sign from every individual effect[^roth2023trending-e3]. Use one of the newer estimators built for this case. In Roth et al.'s experience these usually (but not always) give similar results; what matters first is being clear about what you are estimating and who you compare with whom[^roth2023trending-e4]. Table 2 of their paper lists the R and Stata packages[^roth2023trending-e13]. With staggered adoption, don't draw the event-study plot from the usual dynamic regression either[^roth2023trending-e12].

### Step 3: Regression discontinuity

**How:**

1. **First make sure nothing else happens at the cutoff.** If some other institutional change kicks in at the same line, the effect will be miscalculated. Imbens and Lemieux's example: many cultural venues give discounts from age 65, but other institutional changes also happen at 65, so a jump seen at 65 more likely comes from those other changes[^imbens2008rd-e2].
2. **Check whether people "squeeze" precisely across the cutoff.** People always have some influence over their score, and that's fine; what matters is whether they can place themselves **precisely** on one side[^lee2010rd-e1]. Plot a histogram of the running variable (the score that determines treatment)[^lee2010rd-e3], and you can also run the McCrary density test. A jump in the density at the cutoff doesn't necessarily prove the design fails, but it helps you spot problems[^imbens2008rd-e4]. The test can also miss manipulation: if some people push their score up and others push it down, the effects can cancel out and the density still looks continuous[^lee2010rd-e4].
3. **Check balance on both sides.** Run the same regression discontinuity with characteristics fixed beforehand (baseline covariates) as the "outcome"[^lee2010rd-e7]. A jump in treatment at the cutoff generally shouldn't make these characteristics jump too[^imbens2008rd-e3]. This is the same logic as checking covariate balance in a randomized experiment[^lee2010rd-e2].
4. **Draw the main graph.** Divide the running variable into small bins and plot the average outcome in each bin[^imbens2008rd-e1]. Don't just draw a smooth curve that breaks at the cutoff; that can look like a jump even when there isn't one[^lee2010rd-e5]. Graphs leave room for "manufacturing" an effect, so pair them with formal estimates[^lee2010rd-e10].
5. **Estimate, and vary the bandwidth and specification.** Imbens and Lemieux's practical summary recommends running separate linear regressions within a window (the bandwidth) on each side of the cutoff[^imbens2008rd-e7]. They also say that however you choose the bandwidth, report results with the bandwidth doubled and halved; a result that holds only at one bandwidth is far less credible[^imbens2008rd-e6]. Lee and Lemieux recommend estimating over a range of bandwidths and polynomial orders and reporting a "typical" estimate along with the range of estimates[^lee2010rd-e6]. Both of these are from 2008–2010. For more recent practice, see the introductory book by Cattaneo, Idrobo, and Titiunik (Cambridge University Press, Cambridge Elements series, 2020; we read the authors' 2019 arXiv version):
   - **Use only data near the cutoff.** They advise against fitting high-order polynomials (fourth or fifth order) to all the data for formal analysis, because the conclusions can be badly misleading. Use "local polynomials" instead: take only the data near the cutoff and fit a curve on each side[^cattaneo2020practical-e1]. The "linear regression within the bandwidth" from Imbens and Lemieux above is one of these `[Our analysis]`.
   - **Let the data choose the bandwidth.** Observations within the bandwidth are usually weighted by their distance from the cutoff, with the weights set by a "kernel function". They recommend the triangular kernel, which gives more weight to observations closer to the cutoff, combined with an "MSE-optimal" bandwidth (optimal for mean squared error), which can be computed from the data[^cattaneo2020practical-e2]. Mean squared error measures how far the estimate is from the true value on average, counting both bias and variability `[Our analysis]`.
   - **Bias-correct the confidence interval.** This bandwidth is chosen for the point estimate. It isn't narrow enough for the bias to be negligible, so the authors consider conventional confidence intervals computed with it invalid[^cattaneo2020practical-e3]. They recommend using this bandwidth for the point estimate and reporting a "robust bias-corrected" confidence interval[^cattaneo2020practical-e4]: subtract the estimated bias from the estimate, then also account for the extra uncertainty that comes from estimating the bias, so at the same bandwidth it is wider than the conventional interval[^cattaneo2020practical-e6]. The book demonstrates this with the rdrobust package; the row labeled Robust in its output is this interval[^cattaneo2020practical-e5].
   - **Vary the bandwidth to check stability.** The book also treats this as a check, with the same purpose as "doubling and halving the bandwidth" above. But the authors think it only makes sense to vary the bandwidth within a small range around the optimal one: much larger and the estimate's bias is too big; much smaller and its variability is too big; either way the estimates and test conclusions are unreliable[^cattaneo2020practical-e7].

   These are the book's authors' recommendations; if your target journal requires something different, follow the journal `[Our analysis]`.
6. **Test at fake cutoffs**, to see whether there is a "jump" where there shouldn't be one[^imbens2008rd-e5].

If crossing the cutoff only raises the **probability** of treatment (a "fuzzy" regression discontinuity), the cutoff works like an instrumental variable. It corresponds to a randomized experiment where eligibility is randomized but compliance isn't enforced[^lee2010rd-e11], and the points in Step 4 apply too.

### Step 4: Instrumental variables

**Make three separate arguments.**

- **First stage**: the instrument really does change the treatment. You can test this with data[^cunningham2026remix-e4].
- **Exclusion and as-good-as-random assignment**: the instrument affects the outcome only through the channel you care about, and its value is as good as random. You can't just label these as true; you have to argue them in full[^angrist2010credibility-e5], and specifically check whether the instrument might affect the outcome through some other channel[^angrist2010credibility-e9].
- Instrumental variables rest on several untestable assumptions, and as soon as there is doubt about the exclusion restriction, the conclusion falls apart[^cunningham2026remix-e6]. So the argument has to be written in the paper, not kept in your head `[Our analysis]`.

**Weak instruments.** When the instrument is only weakly related to the treatment, the second-stage results can look fine but be untrustworthy. Cunningham cites a simulation by Bound, Jaeger, and Baker (1995): they replaced the real instrument with randomly generated numbers, and the second-stage results still looked "quite reasonable", with no sign that the instrument was made up[^cunningham2026remix-e3]. "First-stage F statistic above 10" is an old rule of thumb. Cunningham writes in his textbook that this number is "now widely seen as too low", especially with multiple endogenous variables, heteroskedasticity, or non-normal errors[^cunningham2026remix-e1]. This is Cunningham's summary of current views; we have not read the original literature he draws on. His advice: judge instrument strength with the "effective F statistic" of Montiel Olea and Pflueger, and report Anderson-Rubin confidence intervals[^cunningham2026remix-e2]. The latter are confidence intervals that remain valid when the instrument is weak `[Our analysis]`.

**Interpreting the result.** When all the assumptions hold, instrumental variables estimate the average effect for "compliers"[^cunningham2026remix-e5], the people whose behavior the instrument changes. When you write the conclusion, say clearly whose effect this is; don't present it as the effect for everyone `[Our analysis]`.

**Presentation.** Show readers the "numerator" and "denominator" of the estimate[^cunningham2026remix-e8]: the numerator is the reduced form (the instrument's effect on the outcome), and the denominator is the first stage (the instrument's effect on the treatment). Ideally plot both.

### Step 5: Synthetic control (briefly)

Cunningham points out that traditional comparative case studies often choose comparison units arbitrarily and possibly subjectively. The idea of synthetic control is that when you only have a few units of analysis, such as cities or states, a weighted combination of several comparison units often resembles the treated unit better than any single one does[^cunningham2026remix-e15].

- Building the synthetic control doesn't use post-treatment outcomes[^cunningham2026remix-e16], which helps you avoid tuning the model while looking at results `[Our analysis]`.
- For inference, pretend each untreated unit was treated and redo the analysis, giving a set of "placebo effects"; use their distribution to judge whether the real effect stands out[^cunningham2026remix-e17]. According to Cunningham, Abadie, Diamond, and Hainmueller (2010) recommend dropping units whose pre-treatment fit is much worse than the treated unit's[^cunningham2026remix-e18].
- **First decide whether it fits your case.** Abadie's 2021 review in the Journal of Economic Literature lists several preconditions:
  - A long enough pre-intervention period. How credible a synthetic control is depends largely on whether it can closely track the treated unit's trajectory before the intervention, so collect enough pre-intervention data when you design the study[^abadie2021using-e4].
  - A suitable pool of comparison units. Units that adopted similar interventions must be left out, and the pool should be limited to units with characteristics similar to the treated unit[^abadie2021using-e2]. If no combination of comparison units can credibly approximate the treated unit, you shouldn't use standard synthetic control[^abadie2021using-e3].
  - A large enough effect. An effect about as large as the outcome's normal volatility is hard to detect; when the outcome is very volatile, even a large effect may not show up[^abadie2021using-e1].
- On estimation and inference details for synthetic control, our sources only cover Cunningham's Chapter 11 and the sections of Abadie 2021 above; start with those two.

### Step 6: Placebo tests and robustness checks

**Placebo tests**: look for an effect where there shouldn't be one. If you find one, your design may have a problem `[Our analysis]`.

- Difference-in-differences: run "falsification tests" that test alternative explanations. Two common kinds: the same outcome for a different group that shouldn't be affected; or the same group with a different outcome that shouldn't be affected[^cunningham2026remix-e10].
- Regression discontinuity: baseline covariate tests[^lee2010rd-e7]; tests at fake cutoffs[^imbens2008rd-e5].
- Difference-in-differences with state-level policies: Bertrand et al. propose randomly generating nonexistent "placebo laws" and using their estimated effects as the distribution for the test[^bertrand2004trust-e2].

**Robustness checks**: Lee and Lemieux's main advice for regression discontinuity is not to rely on a single method or specification[^lee2010rd-e9], and this applies to the other methods as well `[Our analysis]`. But Angrist and Pischke warn that casting a wide net and running a huge number of regressions does little to support a causal interpretation[^angrist2010credibility-e13]. Which specifications you will vary should also be decided in advance[^cunningham2026remix-e14].

### Step 7: Standard errors and clustering

**Why cluster.** Observations from the same state or the same village often have correlated errors. In that case default standard errors can greatly overstate precision[^cameron2015practitioner-e1]. It is not unusual for standard errors that account for within-group correlation to be several times larger than the default ones[^cameron2015practitioner-e2]. The classic case is estimating the effect of a variable that takes the same value for everyone in a group, such as a policy variable[^cameron2015practitioner-e3].

Bertrand, Duflo, and Mullainathan randomly generated fake laws in US state-level data on women's wages and estimated them with standard difference-in-differences (2002 working-paper version). With about 20 years of data, up to 45% of the fake laws came out "significant"[^bertrand2004trust-e1]. As Cameron and Miller describe it, the paper showed that many difference-in-differences studies did not account for within-group correlation, and those that did often clustered at the wrong level[^cameron2015practitioner-e5].

**What level to cluster at.** Roth et al.'s rule of thumb: cluster at the level at which treatment is independently assigned. If policy is set by state, cluster by state[^roth2023trending-e8].

**What if there are too few clusters?** Cameron and Miller say there is no clear line for "too few"; when clusters are of similar size, it ranges from fewer than 20 to fewer than 50 depending on the situation. With too few clusters and no correction, tests reject the null hypothesis too often and confidence intervals are too narrow[^cameron2015practitioner-e4]. In difference-in-differences, if only a few clusters are treated, standard methods can perform poorly, and you should consider other inference methods[^roth2023trending-e9][^roth2023trending-e8]. On which method to choose, our sources only give an overview; see Cameron and Miller Section VI and Roth et al. Section 5.1.

### Step 8: Reporting

Organizing the results in this order makes it easiest for readers to judge whether your design is credible `[Our analysis, based on the footnotes in each item]`:

1. **The identification strategy paragraph**: what you estimate, who you compare with whom, which assumptions you rely on, and why they are plausible (Step 1).
2. **Graphs of the raw data**: for difference-in-differences, the treatment rollout plot and the event-study plot[^cunningham2026remix-e11][^roth2023trending-e6]; for regression discontinuity, the histogram of the running variable and the binned means plot[^lee2010rd-e3][^lee2010rd-e5]; for instrumental variables, the first stage and the reduced form[^cunningham2026remix-e8].
3. **Main results**: a typical estimate plus the range across specifications[^lee2010rd-e6]; for instrumental variables, also report the effective F statistic and Anderson-Rubin confidence intervals[^cunningham2026remix-e2].
4. **Tests and sensitivity analyses**: placebo tests, balance tests, sensitivity analysis for parallel trends[^roth2023trending-e6]. Whatever doesn't fit in the main text goes in an online appendix[^lee2010rd-e8].
5. **Who the conclusion applies to**: whose effect it is, for example people near the cutoff, or compliers[^cunningham2026remix-e5].

For data and code sharing requirements, see [Data and code must be reproducible](../07_fields/economics/README.md#data-and-code-must-reproduce-the-results) in the Economics and business field overview.

---

## 3. Checklist

**Must do**

- [ ] Write down the identification strategy: what you estimate, who the comparison group is, which assumptions you rely on, and why they are plausible[^roth2023trending-e11]
- [ ] Fix the main specification (control variables, sample, comparison group) before looking at the results[^cunningham2026remix-e14]
- [ ] Difference-in-differences: draw an event-study plot[^roth2023trending-e6]; with staggered adoption, don't use the usual two-way fixed effects regression as the main estimate[^roth2023trending-e3]
- [ ] Regression discontinuity: show the distribution of the running variable[^lee2010rd-e3], baseline covariate tests[^lee2010rd-e7], and bandwidth sensitivity[^imbens2008rd-e6]
- [ ] Instrumental variables: report the first stage, write out the exclusion argument[^angrist2010credibility-e5], and following Cunningham, judge instrument strength with the effective F statistic[^cunningham2026remix-e2]
- [ ] Cluster standard errors at the level at which treatment is independently assigned[^roth2023trending-e8]

**Better practice**

- [ ] Difference-in-differences: report a formal sensitivity analysis for parallel trends, such as "how large a deviation would overturn the conclusion"[^roth2023trending-e7]
- [ ] Instrumental variables: report Anderson-Rubin confidence intervals[^cunningham2026remix-e2], and plot the first stage and reduced form[^cunningham2026remix-e8]
- [ ] At least one placebo or falsification test[^cunningham2026remix-e10]
- [ ] Regression discontinuity: test at fake cutoffs[^imbens2008rd-e5]
- [ ] With very few clusters, switch to an inference method suited to few clusters[^cameron2015practitioner-e4]

**Fine to skip; not a flaw**

- You don't need to put every combination of bandwidth, polynomial order, and covariates in the main text; they can go in an online appendix[^lee2010rd-e8].

**Common reviewer criticisms that don't hold up**

- "Scores are influenced by individual effort, so the regression discontinuity is invalid." Some influence over the score is fine; what matters is whether people can control it **precisely**[^lee2010rd-e1]. Respond with the histogram and the covariate balance tests `[Our analysis]`.
- "Your sample is all 50 states, there is no larger population, so standard errors are meaningless." Roth et al. think this need not worry you: if you view the uncertainty as coming from the randomness of treatment assignment, the analysis usually still makes sense[^roth2023trending-e10].

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Claiming parallel trends hold because pre-trends are "not significant" | These tests often have low power[^roth2023trending-e5]; parallel trends before treatment don't mean the counterfactual trends after treatment are parallel[^cunningham2026remix-e9] |
| Using the usual two-way fixed effects regression with staggered adoption | It uses already-treated units as controls, and the coefficient can have the opposite sign from the true effect[^roth2023trending-e3] |
| In regression discontinuity, drawing only a smooth curve that breaks at the cutoff | It can look like a jump even when there isn't one[^lee2010rd-e5] |
| In regression discontinuity, reporting results for only one bandwidth | A result that holds only at one bandwidth is far less credible[^imbens2008rd-e6] |
| Calling an instrument "exogenous" without arguing the exclusion restriction | It has to be argued in full[^angrist2010credibility-e5]; as soon as there is doubt about exclusion, the conclusion falls apart[^cunningham2026remix-e6] |
| Treating a first-stage F above 10 as proof the instrument is strong enough | According to Cunningham's summary, this threshold is now widely considered too low[^cunningham2026remix-e1]; second-stage results with a weak instrument can still look "reasonable"[^cunningham2026remix-e3] |
| Presenting the instrumental variables estimate as the effect for everyone | It estimates the effect for compliers[^cunningham2026remix-e5] |
| Using default standard errors, or clustering at a finer level than treatment assignment | Default standard errors can greatly overstate precision[^cameron2015practitioner-e1]; with standard difference-in-differences on state-level data, up to 45% of fake laws come out "significant" (simulation in the 2002 working-paper version)[^bertrand2004trust-e1] |
| Trying every specification and reporting only the significant one | The excess of p-values just below 0.05 may come from exactly this kind of selection[^brodeur2016star-e3]; running regressions with a wide net can't support a causal interpretation[^angrist2010credibility-e13] |
| Pushing ahead when the design clearly doesn't hold | If the hand you've been dealt is bad, switch methods early[^cunningham2026remix-e12] |

---

## 5. Further reading

- **Cunningham, Causal Inference: The Remix (free online)**: Chapters 6, 7, 9, 10, and 11 cover regression discontinuity, instrumental variables, difference-in-differences (basic and complex designs), and synthetic control. Chapter 10 has a checklist for difference-in-differences designs. Note that this web edition is still being revised and its content may change; this page cites the version read on October 6, 2026. The first edition (The Mixtape, 2021) is also free online. Good for getting started `[Our analysis]`.
- **Roth et al. 2023, What's Trending in Difference-in-Differences? (free on arXiv)**: a review of recent difference-in-differences methods. Table 1 is a checklist and Table 2 lists software packages. Worth reading before you do difference-in-differences `[Our analysis]`.
- **Lee & Lemieux 2010, Regression Discontinuity Designs in Economics (free as a National Bureau of Economic Research (NBER) working paper)**: when regression discontinuity works; Section 4.6 has an implementation checklist.
- **Imbens & Lemieux 2008, Regression Discontinuity Designs: A Guide to Practice (free as an NBER working paper)**: Section 7 covers the various tests; Section 8 summarizes the steps.
- **Cattaneo, Idrobo & Titiunik 2020, A Practical Introduction to Regression Discontinuity Designs: Foundations (Cambridge University Press; free version on arXiv)**: local polynomial estimation, bandwidth selection, and robust bias-corrected confidence intervals for regression discontinuity, with demonstrations using the rdrobust package.
- **Abadie 2021, Using Synthetic Controls (Journal of Economic Literature; free from the Massachusetts Institute of Technology's open access repository)**: Sections 5 and 6 cover when synthetic control is appropriate and what data it needs.
- **Cameron & Miller 2015, A Practitioner's Guide to Cluster-Robust Inference (free on the authors' websites)**: how to compute clustered standard errors and what to do with too few clusters.
- **Bertrand, Duflo & Mullainathan 2004 (free as an NBER working paper)**: uses "fake laws" to show why difference-in-differences standard errors come out too small.
- **Angrist & Pischke 2010**: why identification matters; see the [Economics and business field overview](../07_fields/economics/README.md#further-reading).

[^roth2023trending-e1]: Roth et al. 2023, §1 Introduction. [Evidence](../../sources/notes/roth2023trending.md#e1)
[^roth2023trending-e2]: Roth et al. 2023, §2.3. [Evidence](../../sources/notes/roth2023trending.md#e2)
[^roth2023trending-e3]: Roth et al. 2023, §1 Introduction. [Evidence](../../sources/notes/roth2023trending.md#e3)
[^roth2023trending-e4]: Roth et al. 2023, §3.5 Recommendations. [Evidence](../../sources/notes/roth2023trending.md#e4)
[^roth2023trending-e5]: Roth et al. 2023, §1 Introduction. [Evidence](../../sources/notes/roth2023trending.md#e5)
[^roth2023trending-e6]: Roth et al. 2023, §4.6 Recommendations. [Evidence](../../sources/notes/roth2023trending.md#e6)
[^roth2023trending-e7]: Roth et al. 2023, §4.6 Recommendations. [Evidence](../../sources/notes/roth2023trending.md#e7)
[^roth2023trending-e8]: Roth et al. 2023, Table 1. [Evidence](../../sources/notes/roth2023trending.md#e8)
[^roth2023trending-e9]: Roth et al. 2023, §1 Introduction. [Evidence](../../sources/notes/roth2023trending.md#e9)
[^roth2023trending-e10]: Roth et al. 2023, §5.2 Recommendations. [Evidence](../../sources/notes/roth2023trending.md#e10)
[^roth2023trending-e11]: Roth et al. 2023, §7 Conclusion. [Evidence](../../sources/notes/roth2023trending.md#e11)
[^roth2023trending-e12]: Roth et al. 2023, §4.3. [Evidence](../../sources/notes/roth2023trending.md#e12)
[^roth2023trending-e13]: Roth et al. 2023, §1 Introduction. [Evidence](../../sources/notes/roth2023trending.md#e13)
[^lee2010rd-e1]: Lee & Lemieux 2010, §3.1. [Evidence](../../sources/notes/lee2010rd.md#e1)
[^lee2010rd-e2]: Lee & Lemieux 2010, §2.3. [Evidence](../../sources/notes/lee2010rd.md#e2)
[^lee2010rd-e3]: Lee & Lemieux 2010, §4.6. [Evidence](../../sources/notes/lee2010rd.md#e3)
[^lee2010rd-e4]: Lee & Lemieux 2010, §4.4.1. [Evidence](../../sources/notes/lee2010rd.md#e4)
[^lee2010rd-e5]: Lee & Lemieux 2010, §4.6. [Evidence](../../sources/notes/lee2010rd.md#e5)
[^lee2010rd-e6]: Lee & Lemieux 2010, §4.6. [Evidence](../../sources/notes/lee2010rd.md#e6)
[^lee2010rd-e7]: Lee & Lemieux 2010, §4.6. [Evidence](../../sources/notes/lee2010rd.md#e7)
[^lee2010rd-e8]: Lee & Lemieux 2010, §4.6. [Evidence](../../sources/notes/lee2010rd.md#e8)
[^lee2010rd-e9]: Lee & Lemieux 2010, §1 Introduction. [Evidence](../../sources/notes/lee2010rd.md#e9)
[^lee2010rd-e10]: Lee & Lemieux 2010, §1 Introduction. [Evidence](../../sources/notes/lee2010rd.md#e10)
[^lee2010rd-e11]: Lee & Lemieux 2010, §3.4.1. [Evidence](../../sources/notes/lee2010rd.md#e11)
[^imbens2008rd-e1]: Imbens & Lemieux 2008, §8. [Evidence](../../sources/notes/imbens2008rd.md#e1)
[^imbens2008rd-e2]: Imbens & Lemieux 2008, §7. [Evidence](../../sources/notes/imbens2008rd.md#e2)
[^imbens2008rd-e3]: Imbens & Lemieux 2008, §7.1. [Evidence](../../sources/notes/imbens2008rd.md#e3)
[^imbens2008rd-e4]: Imbens & Lemieux 2008, §7.2. [Evidence](../../sources/notes/imbens2008rd.md#e4)
[^imbens2008rd-e5]: Imbens & Lemieux 2008, §7.3. [Evidence](../../sources/notes/imbens2008rd.md#e5)
[^imbens2008rd-e6]: Imbens & Lemieux 2008, §7.5. [Evidence](../../sources/notes/imbens2008rd.md#e6)
[^imbens2008rd-e7]: Imbens & Lemieux 2008, §8. [Evidence](../../sources/notes/imbens2008rd.md#e7)
[^cattaneo2020practical-e1]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §4.2. [Evidence](../../sources/notes/cattaneo2020practical.md#e1)
[^cattaneo2020practical-e2]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §4.2.1–4.2.2. [Evidence](../../sources/notes/cattaneo2020practical.md#e2)
[^cattaneo2020practical-e3]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §4.3. [Evidence](../../sources/notes/cattaneo2020practical.md#e3)
[^cattaneo2020practical-e4]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §4.3, §4.3.2. [Evidence](../../sources/notes/cattaneo2020practical.md#e4)
[^cattaneo2020practical-e5]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §4.3.3. [Evidence](../../sources/notes/cattaneo2020practical.md#e5)
[^cattaneo2020practical-e6]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §4.3. [Evidence](../../sources/notes/cattaneo2020practical.md#e6)
[^cattaneo2020practical-e7]: Cattaneo, Idrobo & Titiunik 2020 (2019 arXiv version), §5.5. [Evidence](../../sources/notes/cattaneo2020practical.md#e7)
[^abadie2021using-e1]: Abadie 2021, §5 Size of the Effect and Volatility of the Outcome. [Evidence](../../sources/notes/abadie2021using.md#e1)
[^abadie2021using-e2]: Abadie 2021, §5 Availability of a Comparison Group. [Evidence](../../sources/notes/abadie2021using.md#e2)
[^abadie2021using-e3]: Abadie 2021, §5 Convex Hull Condition. [Evidence](../../sources/notes/abadie2021using.md#e3)
[^abadie2021using-e4]: Abadie 2021, §6 Sufficient Pre-intervention Information. [Evidence](../../sources/notes/abadie2021using.md#e4)
[^angrist2010credibility-e5]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../sources/notes/angrist2010credibility.md#e5)
[^angrist2010credibility-e9]: Angrist & Pischke 2010, Whither Sensitivity Analysis? [Evidence](../../sources/notes/angrist2010credibility.md#e9)
[^angrist2010credibility-e13]: Angrist & Pischke 2010, Whither Sensitivity Analysis? [Evidence](../../sources/notes/angrist2010credibility.md#e13)
[^cunningham2026remix-e1]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e1)
[^cunningham2026remix-e2]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e2)
[^cunningham2026remix-e3]: Cunningham, The Remix (online second edition, still being revised), Chapter 7 (cited from Bound, Jaeger & Baker 1995). [Evidence](../../sources/notes/cunningham2026remix.md#e3)
[^cunningham2026remix-e4]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e4)
[^cunningham2026remix-e5]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e5)
[^cunningham2026remix-e6]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e6)
[^cunningham2026remix-e7]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e7)
[^cunningham2026remix-e8]: Cunningham, The Remix (online second edition, still being revised), Chapter 7. [Evidence](../../sources/notes/cunningham2026remix.md#e8)
[^cunningham2026remix-e9]: Cunningham, The Remix (online second edition, still being revised), Chapter 9. [Evidence](../../sources/notes/cunningham2026remix.md#e9)
[^cunningham2026remix-e10]: Cunningham, The Remix (online second edition, still being revised), Chapter 9. [Evidence](../../sources/notes/cunningham2026remix.md#e10)
[^cunningham2026remix-e11]: Cunningham, The Remix (online second edition, still being revised), Chapter 10. [Evidence](../../sources/notes/cunningham2026remix.md#e11)
[^cunningham2026remix-e12]: Cunningham, The Remix (online second edition, still being revised), Chapter 10. [Evidence](../../sources/notes/cunningham2026remix.md#e12)
[^cunningham2026remix-e13]: Cunningham, The Remix (online second edition, still being revised), Chapter 10. [Evidence](../../sources/notes/cunningham2026remix.md#e13)
[^cunningham2026remix-e14]: Cunningham, The Remix (online second edition, still being revised), Chapter 10. [Evidence](../../sources/notes/cunningham2026remix.md#e14)
[^cunningham2026remix-e15]: Cunningham, The Remix (online second edition, still being revised), Chapter 11. [Evidence](../../sources/notes/cunningham2026remix.md#e15)
[^cunningham2026remix-e16]: Cunningham, The Remix (online second edition, still being revised), Chapter 11. [Evidence](../../sources/notes/cunningham2026remix.md#e16)
[^cunningham2026remix-e17]: Cunningham, The Remix (online second edition, still being revised), Chapter 11. [Evidence](../../sources/notes/cunningham2026remix.md#e17)
[^cunningham2026remix-e18]: Cunningham, The Remix (online second edition, still being revised), Chapter 11. [Evidence](../../sources/notes/cunningham2026remix.md#e18)
[^hernan2018cword-e5]: Hernán 2018, main text. [Evidence](../../sources/notes/hernan2018cword.md#e5)
[^hernan2018cword-e13]: Hernán 2018, main text. [Evidence](../../sources/notes/hernan2018cword.md#e13)
[^brodeur2016star-e2]: Brodeur et al. 2016 (2013 discussion paper version), Abstract. [Evidence](../../sources/notes/brodeur2016star.md#e2)
[^brodeur2016star-e3]: Brodeur et al. 2016 (2013 discussion paper version), Abstract. [Evidence](../../sources/notes/brodeur2016star.md#e3)
[^brodeur2016star-e5]: Brodeur et al. 2016 (2013 discussion paper version), §1. [Evidence](../../sources/notes/brodeur2016star.md#e5)
[^cameron2015practitioner-e1]: Cameron & Miller 2015, Abstract. [Evidence](../../sources/notes/cameron2015practitioner.md#e1)
[^cameron2015practitioner-e2]: Cameron & Miller 2015, §I. [Evidence](../../sources/notes/cameron2015practitioner.md#e2)
[^cameron2015practitioner-e3]: Cameron & Miller 2015, §I. [Evidence](../../sources/notes/cameron2015practitioner.md#e3)
[^cameron2015practitioner-e4]: Cameron & Miller 2015, §I. [Evidence](../../sources/notes/cameron2015practitioner.md#e4)
[^cameron2015practitioner-e5]: Cameron & Miller 2015, §I. [Evidence](../../sources/notes/cameron2015practitioner.md#e5)
[^bertrand2004trust-e1]: Bertrand, Duflo & Mullainathan 2004 (2002 working paper version), Abstract. [Evidence](../../sources/notes/bertrand2004trust.md#e1)
[^bertrand2004trust-e2]: Bertrand, Duflo & Mullainathan 2004 (2002 working paper version), Abstract. [Evidence](../../sources/notes/bertrand2004trust.md#e2)
