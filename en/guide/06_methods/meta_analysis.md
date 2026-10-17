# Systematic reviews and meta-analysis (health research)

This page covers systematic reviews in health research that ask "how well does this intervention work?", and meta-analysis: using statistics to combine the results of several studies into one overall estimate. The steps every field shares (searching, screening, data extraction, the flow diagram) are already covered in [Review studies](review_study.md#2-how-to-do-a-systematic-review), so they are not repeated here. This page covers only what is specific to health research: protocol registration, risk-of-bias assessment, effect measures and models, heterogeneity, small-study effects, rating the certainty of evidence, and reporting. For the wider context of health research, see the [health sciences field overview](../07_fields/health-sciences/README.md).

**Whose advice this page follows.** Our main source is the Cochrane Handbook, in full the Cochrane Handbook for Systematic Reviews of Interventions (we read version 6.5, 2024). It is the methods handbook Cochrane writes for authors of Cochrane reviews[^higgins2024cochrane-e70], and it is about reviews of intervention effects. Whenever this page says "should" or "do not" based on it, that is the Handbook's recommendation; items the Handbook marks as "mandatory" are requirements for Cochrane review authors. If your review is not going to Cochrane, follow your advisor or your target journal `[Our analysis]`. Other kinds of review have their own standards. Take diagnostic test accuracy reviews (which assess how accurately a test detects a disease): Cochrane has a separate Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy (in October 2026 the Cochrane website listed version 2.0, updated July 2023)[^deeks2023cochrane-e1][^deeks2023cochrane-e2], and for reporting there is PRISMA-DTA, the diagnostic test accuracy extension of PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses), published 2018[^prismadta2018-e1]. Diagnostic accuracy reviews differ from intervention reviews in a few places; see [How diagnostic test accuracy reviews differ](#how-diagnostic-test-accuracy-reviews-differ) at the end of Section 1. Our sources do not cover the specific methods for prognostic and other kinds of review. For all of these, follow your advisor or your target journal.

**Scope** `[Our analysis]`: this page was first written for [Health sciences](../07_fields/health-sciences/README.md). Its sources are mainly the Cochrane Handbook, the PRISMA 2020 reporting guideline, the rules of the PROSPERO registry, and the literature on the GRADE approach, all of which describe how reviews of intervention effects are done in health research. The [Clinical medicine](../07_fields/clinical-medicine/README.md) and [Psychology and cognitive science](../07_fields/psychology/README.md) field overviews also point here. If you do meta-analysis in another field, the statistical reasoning behind pooling effects carries over; for registries, risk-of-bias tools, and evidence grading, check your own field's standards first.

**Strategies it usually serves**: [Synthesis](../05_research-strategies/synthesize.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md).


**After reading this page, you should be able to:** decide whether your question calls for a systematic review and whether to include a meta-analysis; write and register a protocol before you start screening; assess the risk of bias of included studies with the RoB 2 and ROBINS-I tools; choose the right effect measure and model, and read I² and funnel plots correctly; rate the certainty of evidence for each outcome with the GRADE approach (introduced in Step 7); and report according to PRISMA 2020.

---

## 1. What this kind of study is, and when to use it

A **systematic review** addresses a clearly formulated question and uses systematic, explicit methods to identify, select, and critically appraise relevant research, and to collect and analyze data from it; statistical methods may or may not be used[^moher2009prisma-e1]. A **meta-analysis** is the use of statistical methods within a systematic review to integrate the results of the included studies[^moher2009prisma-e2]. So meta-analysis is an optional step inside a systematic review, not a different kind of review.

| | Systematic review without meta-analysis | Systematic review + meta-analysis |
|---|---|---|
| Output | Structured tables and a narrative synthesis `[Our analysis]` | For each meta-analysis, a summary estimate, a confidence interval, and measures of heterogeneity[^page2021prisma-e13] |
| Prerequisites | A protocol, a comprehensive search, risk-of-bias assessment `[Our analysis]` | Same as the left, plus studies similar enough that the pooled answer is clinically meaningful[^higgins2024cochrane-e15] |
| Benefits | Applies widely `[Our analysis]` | More precise estimates, answers to questions no single study asked, and a way to settle conflicting findings[^higgins2024cochrane-e13] |
| Risks | Easily slides into a study-by-study list `[Our analysis]` | Can be seriously misleading if study design, bias, variation across studies, and reporting bias are not carefully considered[^higgins2024cochrane-e13] |

**When to do a systematic review:** first state the question with the PICO framework: Population, Intervention, Comparison, Outcome[^higgins2024cochrane-e5]; then estimate the workload. These two points, and the advice to review the literature before starting a new study, are covered in the [health sciences field overview](../07_fields/health-sciences/README.md#systematic-reviews-the-cochrane-handbook). One more thing: according to PROSPERO's archived 2023 pages (PROSPERO is the registry introduced in Step 1 below), it does not register reviews done by fewer than two people[^crd2023prospero-e7], nor "mini" reviews done as training-course assignments[^crd2023prospero-e9]. A course exercise done alone probably cannot be registered; whether it can be submitted as a proper systematic review is a question for your advisor or target journal `[Our analysis]`.

**When not to do a meta-analysis:** a systematic review does not have to include a meta-analysis[^higgins2024cochrane-e16]. The Cochrane Handbook lists these situations: there are no studies or only one, so there is nothing to pool[^higgins2024cochrane-e19]; outcomes or effect estimates are incompletely reported, or the studies use different effect measures; the evidence itself is biased[^higgins2024cochrane-e17]; the populations, interventions, comparisons, or outcomes are not similar enough for a pooled answer to be clinically meaningful, for example when the studies use different kinds of control group[^higgins2024cochrane-e15]; the results vary a lot, especially when effects point in different directions, so that reporting an average could mislead[^higgins2024cochrane-e16]. But large differences and high heterogeneity are not in themselves a reason to give up. The Handbook's view is that you should still consider a meta-analysis, because done and interpreted properly it can give important information[^higgins2024cochrane-e17]. When you don't do a meta-analysis, don't fall back on vote counting (tallying how many studies were significant and how many were not); the Handbook calls this unacceptable[^higgins2024cochrane-e18].

**Which study designs to include:** in GRADE, evidence from randomized trials starts at "high" certainty and evidence from non-randomized studies starts at "low" (see Step 7)[^higgins2024cochrane-e66]; but some evidence, especially about the harms of an intervention, often has to come from non-randomized studies[^higgins2024cochrane-e8]. Confounding, measurement error, and selection bias in observational studies are covered under [three pitfalls of observational studies](../07_fields/health-sciences/README.md#three-pitfalls-of-observational-studies) in the health sciences field overview. A meta-analysis pooling observational studies at high risk of bias cannot be treated as equivalent to one pooling randomized trials at low risk of bias[^murad2016new-e5]; see [the evidence pyramid](../07_fields/clinical-medicine/README.md#the-evidence-pyramid-useful-but-do-not-apply-it-mechanically) in the clinical medicine field overview.

### How diagnostic test accuracy reviews differ

The PRISMA-DTA statement paper (McInnes et al., JAMA 2018) explains that diagnostic accuracy studies differ from randomized controlled trials in design and in the measures they report, so assessing risk of bias and summarizing results also work differently from intervention reviews[^mcinnes2018preferred-e1]. The differences we found fall into three areas. First, the research question must state the participants, the index test (the test being evaluated), and the target condition (the disease or condition the test is meant to detect); the eligibility criteria must also state the reference standard (the best available method for deciding whether someone has the condition)[^prismadta2018checklist-e1][^prismadta2018checklist-e2][^cohen2016stard-e1]. Second, the PRISMA-DTA checklist asks you to describe how you assessed each study's risk of bias and how well it matches your review question (applicability)[^prismadta2018checklist-e3]. The widely used QUADAS-2 tool (Quality Assessment of Diagnostic Accuracy Studies, version 2; Whiting et al., 2011, a revision of the 2003 QUADAS tool) assesses risk of bias in four domains (patient selection, index test, reference standard, and flow and timing) and assesses applicability in the first three (we read only the abstract of this paper)[^whiting2011quadas-e1]. Third, the checklist asks you to state the main accuracy measures; its examples are sensitivity (the proportion of people who have the condition whose test is positive) and specificity (the proportion of people without the condition whose test is negative)[^prismadta2018checklist-e4][^cohen2016stard-e2]. The statement paper says these meta-analyses usually need a multivariate model, such as a bivariate model, that analyzes the two together, because they trade off against each other as the positivity threshold changes and may also be correlated across studies; the traditional univariate approach (pooling each one separately) ignores this correlation and can give misleading results[^mcinnes2018preferred-e2]. The chapters of the Cochrane diagnostic test accuracy handbook can only be downloaded with a Cochrane account, so we did not read them; our sources do not cover that handbook's specific requirements.

---

## 2. How to do it

The eight steps below are in chronological order. After Step 1, do the searching, screening, and extraction as described in the [execution phase](review_study.md#phase-2-conducting-the-review) of [Review studies](review_study.md); in health research the search must also cover trial registries, as Step 6 explains.

### Step 1: Write a protocol and register it in PROSPERO

PROSPERO (the International Prospective Register of Systematic Reviews) was built and is run by the Centre for Reviews and Dissemination at the University of York, UK, and is funded by the UK National Institute for Health Research[^crd2023prospero-e2]. It accepts systematic reviews with a health-related outcome[^crd2023prospero-e3]. PROSPERO says registration is meant to avoid unplanned duplication and to let others compare what was planned with what was finally reported, which reduces bias[^crd2023prospero-e1].

**How:** all the rules below come from its archived pages of January 2023 and may have changed since; we could not read the current pages, so check the official site's current rules when you register `[Our analysis]`.
- Write the full protocol first, then register: you need a complete protocol before registering, and it must be submitted before you start data extraction[^crd2023prospero-e4]; ideally, register before you start screening[^crd2023prospero-e5]. But don't register too early either: registering a review and then not doing it may damage your team's reputation[^crd2023prospero-e10].
- It does not accept scoping reviews, literature reviews that merely use a systematic search, reviews with sports performance as the outcome, and some others[^crd2023prospero-e6]; nor reviews whose results will not be made public (for example a master's thesis known not to be published)[^crd2023prospero-e8]. Protocols of Cochrane reviews should not be registered separately, to avoid duplication[^crd2023prospero-e11].
- Specify in the protocol in advance the primary outcomes, effect measures, model, subgroup analyses, and sensitivity analyses `[Our analysis, based on the sources for Steps 3–5]`. When you include non-randomized studies, the Cochrane Handbook requires the protocol to list the important confounders and the co-interventions of concern (other treatments received at the same time)[^higgins2024cochrane-e28].

**Where people go wrong:** thinking that changing the protocol is a violation. Amending the protocol during a review is normal, as long as you report and explain the changes; but without a publicly accessible protocol, it is hard for others to judge whether the changes were appropriate[^moher2009prisma-e3]. PRISMA 2020 requires you to report the registration number, where the protocol can be accessed, and any amendments to the registered information, with reasons[^page2021prisma-e6][^page2021prisma-e7].

### Step 2: Assess risk of bias result by result

**How:** don't give studies an overall "quality score". Assess **risk of bias** instead: the risk that a result overestimates or underestimates the true effect of the intervention[^higgins2024cochrane-e21]. **Why:** early quality scales added several features into one score; it later turned out that switching to a different scale could noticeably change how the results of a meta-analysis were interpreted, so the approach fell into doubt[^higgins2024cochrane-e20].

**For randomized trials, use RoB 2** (version 2 of the Cochrane risk-of-bias tool for randomized trials):

- It assesses **one specific result** of a trial, not the whole trial[^higgins2024cochrane-e22]. Don't choose which results to assess based on what the assessment is likely to show[^higgins2024cochrane-e26].
- Five domains: the randomization process, deviations from intended interventions, missing outcome data, measurement of the outcome, and selection of the reported result[^higgins2024cochrane-e23]. Each domain is judged "low risk", "some concerns", or "high risk", and the overall judgment is the worst of the domain judgments[^higgins2024cochrane-e24]; write down the reason for every judgment[^higgins2024cochrane-e25].
- The two kinds of effect answer different questions: the effect of assignment to the intervention suits health-policy questions, and the effect of adhering to the intervention as specified suits decisions for individual patients[^higgins2024cochrane-e27]. Decide which one you care about before you start `[Our analysis]`.

**For non-randomized studies, use ROBINS-I** (the Risk Of Bias In Non-randomized Studies of Interventions tool): first describe a "target trial", a hypothetical randomized trial comparing the same interventions in the same population with no features putting it at risk of bias, and then compare the actual study against it[^higgins2024cochrane-e29]. Judgments have four levels: low, moderate, serious, and critical[^higgins2024cochrane-e30].

**Where people go wrong:** expecting ROBINS-I to be as quick as RoB 2. It takes more work than assessing randomized trials, and it needs both methodological and subject-matter expertise[^higgins2024cochrane-e31].

### Step 3: Choose the effect measure

**How:** the effect measure is the number you use to express "how much better the intervention is than the comparison" `[Our analysis]`.
- **Dichotomous outcomes** (such as getting a disease or not): the Handbook generally recommends pooling with the risk ratio or the odds ratio; with a risk ratio, think carefully about which category counts as the "event"[^higgins2024cochrane-e32]. Many meta-analysis methods rely on large-sample approximations and are unsuitable when events are rare[^higgins2024cochrane-e71].
- **Continuous outcomes** (such as blood pressure): use the mean difference when all studies use the same scale; when they use different scales, the standardized mean difference is generally used[^higgins2024cochrane-e36].

**Why the presentation matters:** the odds ratio is the hardest to understand, and the published literature has many examples of odds ratios from meta-analyses being misread as risk ratios[^higgins2024cochrane-e33]. The Handbook's view is that you can often pool with one measure and then convert to an easier one for presentation[^higgins2024cochrane-e34].

**Where people go wrong:** looking at the data and then picking the measure that gives "the most consistent results". This can artificially inflate the apparent precision of the pooled result[^higgins2024cochrane-e35]. So fix the measure in advance in the protocol `[Our analysis]`, and report which measure you used for each outcome[^page2021prisma-e8].

### Step 4: Choose the model: fixed effect or random effects

The pooled result of a meta-analysis is a weighted average of the study effects; in the common methods, larger studies with smaller standard errors (more precise results) get more weight[^higgins2024cochrane-e37]. A **fixed-effect model** assumes every study has the same true effect; a **random-effects model** drops this assumption and instead assumes the true effects follow some distribution (usually a normal distribution)[^higgins2024cochrane-e38]. **Why the distinction matters:** the two results mean different things. A fixed-effect confidence interval does not reflect heterogeneity; a random-effects result refers to the average of the study effects[^higgins2024cochrane-e73].

> **Where sources disagree: which model?**
> - **For random effects:** it is generally considered unlikely that the intervention effect is exactly the same in every study (unless the intervention has no effect at all), so many people argue for random effects[^higgins2024cochrane-e40].
> - **For fixed effect:** others argue that a fixed-effect result can still be interpreted when there is heterogeneity, and that it makes fewer assumptions than a random-effects model[^higgins2024cochrane-e41].
>
> The Cochrane Handbook says this question is much debated and it makes no single recommendation[^higgins2024cochrane-e39]. It warns that if the funnel plot is asymmetric (effect size is related to study size), the random-effects result is pulled toward the findings of the small studies[^higgins2024cochrane-e43]. It suggests a pragmatic approach: plan both in advance, and report the random-effects result when there is no sign of funnel plot asymmetry[^higgins2024cochrane-e44]. It also says plainly: **never choose the model based on the result of a test for heterogeneity**[^higgins2024cochrane-e42].

### Step 5: Look at heterogeneity and read I² correctly

**Heterogeneity** means the effects vary across studies by more than chance alone can explain[^higgins2024cochrane-e45]. You must take differences between studies into account[^higgins2024cochrane-e72]; otherwise the meaning of the pooled result will be misread (see Step 4)[^higgins2024cochrane-e73].

**How to look at it:**
- **Test for heterogeneity**: a significant result may indicate a problem; a non-significant result cannot be taken as evidence of no heterogeneity[^higgins2024cochrane-e46].
- **I²**: the percentage of the variability in effect estimates that is due to heterogeneity rather than sampling error[^higgins2024cochrane-e47]. The Cochrane Handbook gives a rough guide: 0–40% might not be important, 30–60% may be moderate, 50–90% may be substantial, and 75–100% is considerable; it also warns that interpreting I² by thresholds can be misleading[^higgins2024cochrane-e48]. With few studies, I² is very uncertain, so don't use simple thresholds to diagnose heterogeneity[^higgins2024cochrane-e49].
- **A random-effects confidence interval does not describe heterogeneity**; it describes uncertainty about where the average effect lies[^higgins2024cochrane-e50]. When there is a reasonable number of studies (for example, five or more) and no clear funnel plot asymmetry, the Handbook encourages reporting a **prediction interval**[^higgins2024cochrane-e51], which shows the range in which the true effect of an individual study is likely to fall `[Our analysis]`.

**Once you find heterogeneity:**
1. **Check the data first.** Unusually large heterogeneity may come from an extraction or data-entry error, such as entering a standard error as a standard deviation[^higgins2024cochrane-e52].
2. **Then look for the cause.** The usual tool is subgroup analysis: splitting the studies into groups by some characteristic and looking at each group separately `[Our analysis]`. Reliable conclusions can come only from analyses that were truly specified before anyone looked at the studies' results, and even those conclusions need cautious interpretation; analyses thought up after seeing the heterogeneity can at best generate hypotheses[^higgins2024cochrane-e53]. With very few studies, looking for causes is of doubtful value[^higgins2024cochrane-e75]; the Handbook notes that most Cochrane reviews do not have enough studies to identify causes reliably[^higgins2024cochrane-e72].
3. **Don't exclude studies that "don't fit".** Excluding studies based on their results may introduce bias; you can run a sensitivity analysis with and without them instead[^higgins2024cochrane-e54].
4. **Switching to random effects does not solve the problem**; it is no substitute for investigating the cause[^higgins2024cochrane-e55]. **Do sensitivity analyses** to check whether your conclusions still hold if you make a different choice at a decision point that could affect the results[^higgins2024cochrane-e56].

### Step 6: Assess small-study effects and publication bias

**Why:** "significant, it works" results are more likely than non-significant ones to be published, to be published quickly, and to be cited often, so they are also more likely to be found by a review[^higgins2024cochrane-e57].

**How:**
- **Guard against it at the search stage.** Besides several bibliographic databases, you may need to search trial registries and contact manufacturers, regulators, study authors, or funders[^higgins2024cochrane-e58].
- **Check study by study** whether the studies you found selectively left out or under-reported results; the Handbook considers this possibly the most valuable step[^higgins2024cochrane-e63].
- A **funnel plot** is a scatter plot of each study's effect against its size `[Our analysis]`. What it shows is "small-study effects", the tendency for small studies to give different effect estimates from large ones[^higgins2024cochrane-e59]. If you are worried about small-study effects, compare the fixed-effect and random-effects estimates; if they are similar, small-study effects have little influence on the result[^higgins2024cochrane-e62].

**Where people go wrong:**
- Treating funnel plot asymmetry as evidence of publication bias. Asymmetry cannot be used to diagnose non-reporting bias[^higgins2024cochrane-e61].
- Running a funnel plot asymmetry test with very few studies. The Handbook's rule of thumb is to test only when the meta-analysis has at least 10 studies, because otherwise the test has too little power; it cites a survey showing that in a random sample of 300 systematic reviews indexed in 2020, only 28% contained a meta-analysis with at least 10 studies[^higgins2024cochrane-e60].

### Step 7: Rate the evidence for each outcome with GRADE

GRADE (Grading of Recommendations Assessment, Development and Evaluation) is an approach to rating how much confidence you can place in a body of evidence; Chapter 14 of the Cochrane Handbook uses it to assess the certainty of evidence[^higgins2024cochrane-e64]. It does not say that a "higher" design automatically means stronger evidence; instead it looks, outcome by outcome, at how trustworthy the evidence is. This differs from the evidence-pyramid thinking described in the [clinical medicine field overview](../07_fields/clinical-medicine/README.md#the-evidence-pyramid-useful-but-do-not-apply-it-mechanically) `[Our analysis]`.

**How:**
- **Rate by outcome, not by study.** The evidence for each outcome gets one of four levels: high, moderate, low, or very low[^higgins2024cochrane-e64]. In the 2013 GRADE Handbook's terms, "high" means we are very confident that the true effect lies close to the estimate; "very low" means the true effect is likely to be substantially different from the estimate[^schunemann2013grade-e1].
- **The starting point depends on the design.** Randomized trials start at "high"; non-randomized studies start at "low"[^higgins2024cochrane-e66].
- **Five reasons to rate down**: risk of bias, inconsistency, indirectness, imprecision, and publication bias; for non-randomized studies there are three further considerations that can rate the evidence up[^higgins2024cochrane-e65]. Even when ROBINS-I is used, well-conducted non-randomized studies are generally rated as low certainty[^higgins2024cochrane-e74].
- **Give a reason for every upgrade or downgrade**[^higgins2024cochrane-e68], ideally with two people rating independently and then reaching consensus on downgrades[^higgins2024cochrane-e67]. Collect the results in a "Summary of findings" table, one row per important outcome, with at most seven outcomes[^higgins2024cochrane-e69].

**Where people go wrong:**
- Readily rating up for a large effect when the outcome is subjective and assessors knew the group allocation. The 2013 GRADE Handbook advises caution here[^schunemann2013grade-e4].
- Treating the four levels as a precise scale. The 2013 GRADE Handbook says that the grading itself inevitably has some arbitrariness[^schunemann2013grade-e3].
- Getting confused by old and new terms. The 2013 GRADE Handbook speaks of "quality of evidence"; PRISMA 2020 notes the shift to assessing "certainty of evidence"[^page2021prisma-e15].

### Step 8: Report according to PRISMA 2020

PRISMA 2020 is a reporting guideline for systematic reviews: it tells you how to report a review, not how to conduct one[^page2021prisma-e16]. The general parts are covered in the [reporting phase](review_study.md#phase-3-reporting) of [Review studies](review_study.md). The Cochrane Handbook requires Cochrane protocols and reviews to comply with PRISMA 2020 and its protocol version (PRISMA for Protocols)[^higgins2024cochrane-e70]. Items related to meta-analysis that are easy to miss:

- The effect measure for each outcome (item 12)[^page2021prisma-e8]; the model, the methods for identifying heterogeneity, and the software (item 13d)[^page2021prisma-e9]; subgroup analyses, meta-regression, and sensitivity analyses (items 13e and 13f)[^page2021prisma-e10]
- The methods for assessing reporting bias and certainty of evidence (items 14 and 15)[^page2021prisma-e11]; the risk of bias of each study (item 18)[^page2021prisma-e12]; the summary estimate, confidence interval, and measures of heterogeneity for each meta-analysis (item 20b)[^page2021prisma-e13]
- The registration number, protocol, and amendments (item 24)[^page2021prisma-e6][^page2021prisma-e7]; whether data and code are publicly available (item 27)[^page2021prisma-e14]

---

## 3. Checklist

Each item names its source: "Cochrane mandatory" is a mandatory requirement the Cochrane Handbook sets for Cochrane reviews; "PRISMA" is a PRISMA 2020 reporting item; "PROSPERO" is a rule from its archived 2023 pages. If you are not submitting to Cochrane, follow your target journal's requirements `[Our analysis]`.

**Must do**
- [ ] Write the full protocol before registering; if registering in PROSPERO, submit before you start data extraction (PROSPERO)[^crd2023prospero-e4]
- [ ] Report the registration number, where the protocol is, and any amendments with reasons (PRISMA)[^page2021prisma-e6][^page2021prisma-e7]
- [ ] Do a meta-analysis only when the studies are similar enough for pooling to be clinically meaningful (Cochrane mandatory)[^higgins2024cochrane-e15]
- [ ] With few studies, don't use simple thresholds to diagnose heterogeneity (Cochrane mandatory)[^higgins2024cochrane-e49]; when interpreting results, explain what heterogeneity means under the model you used (Cochrane mandatory)[^higgins2024cochrane-e73]
- [ ] Give and record a reason for every upgrade or downgrade of certainty (Cochrane mandatory)[^higgins2024cochrane-e68]
- [ ] Report the risk of bias of each study, and the summary estimate, confidence interval, and measures of heterogeneity for each meta-analysis (PRISMA)[^page2021prisma-e12][^page2021prisma-e13]

**Better practice**
- [ ] Ideally, register before you start screening (PROSPERO)[^crd2023prospero-e5]
- [ ] Assess risk of bias with domain-based tools such as RoB 2 and ROBINS-I, give a reason for each judgment, and don't use an overall quality score[^higgins2024cochrane-e25][^higgins2024cochrane-e20]
- [ ] Plan both fixed-effect and random-effects analyses in advance[^higgins2024cochrane-e44]; report a prediction interval when there is a reasonable number of studies[^higgins2024cochrane-e51]; test key decisions with sensitivity analyses[^higgins2024cochrane-e56]
- [ ] Have two people rate certainty of evidence independently (Cochrane lists this as mandatory, but its wording is "ideally")[^higgins2024cochrane-e67]
- [ ] Search trial registries and check study by study for selective non-reporting[^higgins2024cochrane-e58][^higgins2024cochrane-e63]
- [ ] Share the data extraction forms, the extracted data, and the analysis code (PRISMA asks you to state whether they are available)[^page2021prisma-e14]

**Fine to skip; not a flaw:** no meta-analysis when there are too few studies or they are not similar enough[^higgins2024cochrane-e16][^higgins2024cochrane-e19]; no funnel plot asymmetry test when a meta-analysis has fewer than 10 studies[^higgins2024cochrane-e60]; no forced search for the causes of heterogeneity when there are very few studies[^higgins2024cochrane-e75].

**Common reviewer criticisms that don't hold up** (whether these are "common" is our judgment `[Our analysis]`; why they don't hold up is backed by the sources)
- "I² is over 50%, so you can't pool": interpreting I² by a fixed threshold can mislead, and high heterogeneity is not in itself a reason to abandon meta-analysis[^higgins2024cochrane-e48][^higgins2024cochrane-e17]
- "The test for heterogeneity is not significant, so you should use a fixed-effect model": the model must not be chosen based on a test for heterogeneity[^higgins2024cochrane-e42]
- "The protocol was changed, so the review can't be trusted": amendments can be reported and explained and are not improper in themselves[^moher2009prisma-e3]
- "No meta-analysis, so it isn't a systematic review": a systematic review does not have to include a meta-analysis[^higgins2024cochrane-e16]

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Running the statistical pooling before the question, eligibility criteria, and risk-of-bias assessment are settled | The meta-analysis results can be highly misleading[^higgins2024cochrane-e14] |
| Treating a meta-analysis of observational studies at high risk of bias as strong evidence | It cannot be treated as equivalent to a meta-analysis of randomized trials at low risk of bias[^murad2016new-e5] |
| Picking the effect measure after seeing the data; reading odds ratios as risk ratios | The first can artificially inflate precision[^higgins2024cochrane-e35]; the second is common in the published literature[^higgins2024cochrane-e33] |
| Saying "no heterogeneity" because the test was not significant; taking the random-effects confidence interval as the size of between-study differences | Not significant does not mean none[^higgins2024cochrane-e46]; the confidence interval only describes uncertainty about where the average effect lies[^higgins2024cochrane-e50] |
| Finding subgroups after the fact and writing them into the conclusions; excluding studies whose results "don't fit" | Post hoc analyses can at best generate hypotheses[^higgins2024cochrane-e53]; exclusion may introduce bias[^higgins2024cochrane-e54] |
| Running a funnel plot test with very few studies and using it to declare that publication bias is present or absent | The test has low power, and asymmetry cannot diagnose non-reporting bias anyway[^higgins2024cochrane-e60][^higgins2024cochrane-e61] |

For giving studies an overall quality score, choosing the model from the heterogeneity test, and vote counting by significance, see Step 2, Step 4, and Section 1.

---

## 5. Further reading

- **Cochrane Handbook** (version 6.5, free online): Chapter 10 covers meta-analysis; start with its opening section, "Do not start here!". Chapters 8 and 25 cover RoB 2 and ROBINS-I; Chapter 13 covers funnel plots; Chapter 14 covers GRADE; Chapter 12 covers synthesis without meta-analysis.
- **PRISMA 2020**: the full checklist and flow diagram templates. **GRADE Handbook** (October 2013 version, free online): explains the reasons for rating up and down; it uses the term "quality of evidence". **PROSPERO website**: we only read its archived 2023 pages, so read the current guidance before you register.

Links to every source are in the [source list](../../sources/README.md).

[^moher2009prisma-e1]: Moher et al. 2009, Terminology. [Evidence](../../sources/notes/moher2009prisma.md#e1)
[^moher2009prisma-e2]: Moher et al. 2009, Terminology. [Evidence](../../sources/notes/moher2009prisma.md#e2)
[^moher2009prisma-e3]: Moher et al. 2009, Box 1. [Evidence](../../sources/notes/moher2009prisma.md#e3)
[^higgins2024cochrane-e13]: Cochrane Handbook 2024, Chapter 10 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e13)
[^higgins2024cochrane-e14]: Cochrane Handbook 2024, Chapter 10 §10.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e14)
[^higgins2024cochrane-e15]: Cochrane Handbook 2024, Chapter 10 §10.10.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e15)
[^higgins2024cochrane-e16]: Cochrane Handbook 2024, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e16)
[^higgins2024cochrane-e17]: Cochrane Handbook 2024, Chapter 12 §12.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e17)
[^higgins2024cochrane-e18]: Cochrane Handbook 2024, Chapter 12 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e18)
[^higgins2024cochrane-e19]: Cochrane Handbook 2024, Chapter 12, Table 12.1.a. [Evidence](../../sources/notes/higgins2024cochrane.md#e19)
[^higgins2024cochrane-e20]: Cochrane Handbook 2024, Chapter 7 §7.1.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e20)
[^higgins2024cochrane-e21]: Cochrane Handbook 2024, Chapter 7 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e21)
[^higgins2024cochrane-e22]: Cochrane Handbook 2024, Chapter 8 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e22)
[^higgins2024cochrane-e23]: Cochrane Handbook 2024, Chapter 8 §8.2.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e23)
[^higgins2024cochrane-e24]: Cochrane Handbook 2024, Chapter 8 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e24)
[^higgins2024cochrane-e25]: Cochrane Handbook 2024, Chapter 8 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e25)
[^higgins2024cochrane-e26]: Cochrane Handbook 2024, Chapter 8 §8.2.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e26)
[^higgins2024cochrane-e27]: Cochrane Handbook 2024, Chapter 8 §8.2.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e27)
[^higgins2024cochrane-e28]: Cochrane Handbook 2024, Chapter 25 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e28)
[^higgins2024cochrane-e29]: Cochrane Handbook 2024, Chapter 25 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e29)
[^higgins2024cochrane-e30]: Cochrane Handbook 2024, Chapter 25 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e30)
[^higgins2024cochrane-e31]: Cochrane Handbook 2024, Chapter 25 §25.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e31)
[^higgins2024cochrane-e32]: Cochrane Handbook 2024, Chapter 10 §10.4.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e32)
[^higgins2024cochrane-e33]: Cochrane Handbook 2024, Chapter 10 §10.4.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e33)
[^higgins2024cochrane-e34]: Cochrane Handbook 2024, Chapter 10 §10.4.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e34)
[^higgins2024cochrane-e35]: Cochrane Handbook 2024, Chapter 10 §10.4.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e35)
[^higgins2024cochrane-e36]: Cochrane Handbook 2024, Chapter 10 §10.5.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e36)
[^higgins2024cochrane-e37]: Cochrane Handbook 2024, Chapter 10 §10.2.1, §10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e37)
[^higgins2024cochrane-e38]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e38)
[^higgins2024cochrane-e39]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e39)
[^higgins2024cochrane-e40]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e40)
[^higgins2024cochrane-e41]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e41)
[^higgins2024cochrane-e42]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e42)
[^higgins2024cochrane-e43]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e43)
[^higgins2024cochrane-e44]: Cochrane Handbook 2024, Chapter 10 §10.10.4.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e44)
[^higgins2024cochrane-e45]: Cochrane Handbook 2024, Chapter 10 §10.10.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e45)
[^higgins2024cochrane-e46]: Cochrane Handbook 2024, Chapter 10 §10.10.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e46)
[^higgins2024cochrane-e47]: Cochrane Handbook 2024, Chapter 10 §10.10.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e47)
[^higgins2024cochrane-e48]: Cochrane Handbook 2024, Chapter 10 §10.10.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e48)
[^higgins2024cochrane-e49]: Cochrane Handbook 2024, Chapter 10 §10.10.2 (mandatory standard C63). [Evidence](../../sources/notes/higgins2024cochrane.md#e49)
[^higgins2024cochrane-e50]: Cochrane Handbook 2024, Chapter 10 §10.10.4.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e50)
[^higgins2024cochrane-e51]: Cochrane Handbook 2024, Chapter 10 §10.10.4.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e51)
[^higgins2024cochrane-e52]: Cochrane Handbook 2024, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e52)
[^higgins2024cochrane-e53]: Cochrane Handbook 2024, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e53)
[^higgins2024cochrane-e54]: Cochrane Handbook 2024, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e54)
[^higgins2024cochrane-e55]: Cochrane Handbook 2024, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e55)
[^higgins2024cochrane-e56]: Cochrane Handbook 2024, Chapter 10 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e56)
[^higgins2024cochrane-e57]: Cochrane Handbook 2024, Chapter 13 §13.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e57)
[^higgins2024cochrane-e58]: Cochrane Handbook 2024, Chapter 13 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e58)
[^higgins2024cochrane-e59]: Cochrane Handbook 2024, Chapter 13 §13.3.4.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e59)
[^higgins2024cochrane-e60]: Cochrane Handbook 2024, Chapter 13 §13.3.4.4. [Evidence](../../sources/notes/higgins2024cochrane.md#e60)
[^higgins2024cochrane-e61]: Cochrane Handbook 2024, Chapter 13 §13.3.4.4. [Evidence](../../sources/notes/higgins2024cochrane.md#e61)
[^higgins2024cochrane-e62]: Cochrane Handbook 2024, Chapter 13 §13.3.4.6. [Evidence](../../sources/notes/higgins2024cochrane.md#e62)
[^higgins2024cochrane-e63]: Cochrane Handbook 2024, Chapter 13 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e63)
[^higgins2024cochrane-e64]: Cochrane Handbook 2024, Chapter 14 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e64)
[^higgins2024cochrane-e65]: Cochrane Handbook 2024, Chapter 14 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e65)
[^higgins2024cochrane-e66]: Cochrane Handbook 2024, Chapter 14 §14.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e66)
[^higgins2024cochrane-e67]: Cochrane Handbook 2024, Chapter 14 §14.2 (mandatory standard C74). [Evidence](../../sources/notes/higgins2024cochrane.md#e67)
[^higgins2024cochrane-e68]: Cochrane Handbook 2024, Chapter 14 §14.2 (mandatory standard C75). [Evidence](../../sources/notes/higgins2024cochrane.md#e68)
[^higgins2024cochrane-e69]: Cochrane Handbook 2024, Chapter 14 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e69)
[^higgins2024cochrane-e70]: Cochrane Handbook 2024, Chapter III Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e70)
[^higgins2024cochrane-e71]: Cochrane Handbook 2024, Chapter 10 §10.4.4. [Evidence](../../sources/notes/higgins2024cochrane.md#e71)
[^higgins2024cochrane-e72]: Cochrane Handbook 2024, Chapter 10 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e72)
[^higgins2024cochrane-e73]: Cochrane Handbook 2024, Chapter 10 §10.10.3 (mandatory standard C69). [Evidence](../../sources/notes/higgins2024cochrane.md#e73)
[^higgins2024cochrane-e74]: Cochrane Handbook 2024, Chapter 14 §14.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e74)
[^higgins2024cochrane-e5]: Cochrane Handbook 2024, Chapter 1 §1.2. [Evidence](../../sources/notes/higgins2024cochrane.md#e5)
[^higgins2024cochrane-e8]: Cochrane Handbook 2024, Chapter 24 §24.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e8)
[^higgins2024cochrane-e75]: Cochrane Handbook 2024, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e75)
[^crd2023prospero-e1]: PROSPERO website, 2023 archived copy, Registering a review. [Evidence](../../sources/notes/crd2023prospero.md#e1)
[^crd2023prospero-e2]: PROSPERO website, 2023 archived copy, Registering a review. [Evidence](../../sources/notes/crd2023prospero.md#e2)
[^crd2023prospero-e3]: PROSPERO website, 2023 archived copy, Inclusion criteria. [Evidence](../../sources/notes/crd2023prospero.md#e3)
[^crd2023prospero-e4]: PROSPERO website, 2023 archived copy, Requirements for registration. [Evidence](../../sources/notes/crd2023prospero.md#e4)
[^crd2023prospero-e5]: PROSPERO website, 2023 archived copy, Integrity of data and prospective registration. [Evidence](../../sources/notes/crd2023prospero.md#e5)
[^crd2023prospero-e6]: PROSPERO website, 2023 archived copy, PROSPERO does not accept. [Evidence](../../sources/notes/crd2023prospero.md#e6)
[^crd2023prospero-e7]: PROSPERO website, 2023 archived copy, registration eligibility checklist page. [Evidence](../../sources/notes/crd2023prospero.md#e7)
[^crd2023prospero-e8]: PROSPERO website, 2023 archived copy, registration eligibility checklist page. [Evidence](../../sources/notes/crd2023prospero.md#e8)
[^crd2023prospero-e9]: PROSPERO website, 2023 archived copy, homepage notice. [Evidence](../../sources/notes/crd2023prospero.md#e9)
[^crd2023prospero-e10]: PROSPERO website, 2023 archived copy, When to register your review. [Evidence](../../sources/notes/crd2023prospero.md#e10)
[^crd2023prospero-e11]: PROSPERO website, 2023 archived copy, Other considerations. [Evidence](../../sources/notes/crd2023prospero.md#e11)
[^page2021prisma-e6]: PRISMA 2020 (Page et al. 2021), Item 24a. [Evidence](../../sources/notes/page2021prisma.md#e6)
[^page2021prisma-e7]: PRISMA 2020, Items 24b and 24c. [Evidence](../../sources/notes/page2021prisma.md#e7)
[^page2021prisma-e8]: PRISMA 2020, Item 12. [Evidence](../../sources/notes/page2021prisma.md#e8)
[^page2021prisma-e9]: PRISMA 2020, Item 13d. [Evidence](../../sources/notes/page2021prisma.md#e9)
[^page2021prisma-e10]: PRISMA 2020, Items 13e and 13f. [Evidence](../../sources/notes/page2021prisma.md#e10)
[^page2021prisma-e11]: PRISMA 2020, Items 14 and 15. [Evidence](../../sources/notes/page2021prisma.md#e11)
[^page2021prisma-e12]: PRISMA 2020, Item 18. [Evidence](../../sources/notes/page2021prisma.md#e12)
[^page2021prisma-e13]: PRISMA 2020, Item 20b. [Evidence](../../sources/notes/page2021prisma.md#e13)
[^page2021prisma-e14]: PRISMA 2020, Item 27. [Evidence](../../sources/notes/page2021prisma.md#e14)
[^page2021prisma-e15]: PRISMA 2020, Introduction. [Evidence](../../sources/notes/page2021prisma.md#e15)
[^page2021prisma-e16]: PRISMA 2020, Introduction. [Evidence](../../sources/notes/page2021prisma.md#e16)
[^murad2016new-e5]: Murad et al. 2016, Rationale for modification 2. [Evidence](../../sources/notes/murad2016new.md#e5)
[^schunemann2013grade-e1]: GRADE Handbook 2013, Table 5.1. [Evidence](../../sources/notes/schunemann2013grade.md#e1)
[^schunemann2013grade-e3]: GRADE Handbook 2013, §5. [Evidence](../../sources/notes/schunemann2013grade.md#e3)
[^schunemann2013grade-e4]: GRADE Handbook 2013, §5.3.1. [Evidence](../../sources/notes/schunemann2013grade.md#e4)
[^deeks2023cochrane-e1]: Cochrane website, Cochrane Handbook for Systematic Reviews of Diagnostic Test Accuracy introduction page, About the Handbook. [Evidence](../../sources/notes/deeks2023cochrane.md#e1)
[^deeks2023cochrane-e2]: Cochrane website, ibid., How to cite the Handbook. [Evidence](../../sources/notes/deeks2023cochrane.md#e2)
[^prismadta2018-e1]: PRISMA official website, PRISMA-Diagnostic Test Accuracy page. [Evidence](../../sources/notes/prismadta2018.md#e1)
[^mcinnes2018preferred-e1]: McInnes et al. 2018, JAMA, PRISMA-DTA statement, Introduction. [Evidence](../../sources/notes/mcinnes2018preferred.md#e1)
[^mcinnes2018preferred-e2]: McInnes et al. 2018, Ibid., Results (item D2). [Evidence](../../sources/notes/mcinnes2018preferred.md#e2)
[^prismadta2018checklist-e1]: PRISMA-DTA checklist (PDF on the PRISMA website), Item 4. [Evidence](../../sources/notes/prismadta2018checklist.md#e1)
[^prismadta2018checklist-e2]: PRISMA-DTA checklist, Item 6. [Evidence](../../sources/notes/prismadta2018checklist.md#e2)
[^prismadta2018checklist-e3]: PRISMA-DTA checklist, Item 12. [Evidence](../../sources/notes/prismadta2018checklist.md#e3)
[^prismadta2018checklist-e4]: PRISMA-DTA checklist, Item 13. [Evidence](../../sources/notes/prismadta2018checklist.md#e4)
[^cohen2016stard-e1]: Cohen et al. 2016, BMJ Open, STARD 2015 explanation and elaboration, Table 1. [Evidence](../../sources/notes/cohen2016stard.md#e1)
[^cohen2016stard-e2]: Cohen et al. 2016, ibid., Table 1. [Evidence](../../sources/notes/cohen2016stard.md#e2)
[^whiting2011quadas-e1]: Whiting et al. 2011, Annals of Internal Medicine, QUADAS-2, Abstract. [Evidence](../../sources/notes/whiting2011quadas.md#e1)
