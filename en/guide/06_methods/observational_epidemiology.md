# Observational epidemiology

This page explains how to do the three most common kinds of observational epidemiological study well: **cohort studies, case-control studies, and cross-sectional studies**. "Observational" means the researcher does not intervene; they only observe[^song2010observational-e1].

The [health sciences field overview](../07_fields/health-sciences/README.md) already covers [the three pitfalls of observational studies](../07_fields/health-sciences/README.md#three-pitfalls-of-observational-studies) (confounding, inaccurate measurement, and who ends up in the study), as well as [deciding up front whether you are asking an association question or a causal one](../07_fields/health-sciences/README.md#before-you-start-are-you-answering-a-question-about-association-or-causation) and the basic idea of a "target trial." This page assumes you have read those and covers only **how to actually do it**. For reporting requirements when you use registries, insurance claims, electronic health records, or other routinely collected data, see [this section](../07_fields/health-sciences/README.md#using-routinely-collected-data-report-the-codes-the-linkage-and-where-the-data-came-from) of the same overview; this page adds only a few points.

**Scope**: This page was written for the [Health sciences](../07_fields/health-sciences/README.md) (epidemiology and public health). Its sources are mainly STROBE (Strengthening the Reporting of Observational Studies in Epidemiology, the reporting guideline for observational epidemiology), its explanation and elaboration paper, and its extensions (STROBE-nut, STROBE-Nutritional Epidemiology, for nutrition research; RECORD, REporting of studies Conducted using Observational Routinely-collected health Data, for routinely collected data); Hernán and colleagues' causal inference textbook and their "target trial" paper; and the US National Cancer Institute's primer on dietary assessment. So the practices and vocabulary below are those of health research. The [Clinical medicine](../07_fields/clinical-medicine/README.md) and [Economics and business](../07_fields/economics/README.md) field overviews also point here; economics handles the same problems with different vocabulary and methods, see [Quasi-experiments and causal identification](quasi_experiment.md). If you work in another field and want to draw causal conclusions from observational data, check your own field's conventions first.

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md); cross-sectional studies are also used for [Description](../05_research-strategies/observe_describe.md).


**After reading this page, you should be able to:** choose the right design for your question; define the exposure, the outcome, and the start of follow-up, and choose a good comparison group; use a causal diagram to decide which confounders to adjust for, and recognize selection bias and information bias; plan sensitivity analyses, and write the paper to the reporting guideline.

---

## 1. What this kind of study is, and when to use it

The three designs differ in **where you start when you select people**:

| | Cohort study | Case-control study | Cross-sectional study |
|---|---|---|---|
| How people are selected | Select by exposure, then follow them to see who develops the outcome[^song2010observational-e2] | Find the cases first, then select controls; the controls represent the population the cases came from[^vandenbroucke2007strobe-e14] | Survey a sample at a single point in time |
| Good for | Rare exposures; one exposure with several outcomes[^song2010observational-e2]; repeated measurements during follow-up[^vandenbroucke2007strobe-e16] | Rare outcomes and outcomes with long latency[^song2010observational-e3] | Describing the current situation (e.g., prevalence); analytical cross-sectional studies can also quantify the association between an exposure and a disease[^vandenbroucke2007strobe-e15] |
| Main weaknesses | Large samples, long follow-up, high cost[^song2010observational-e2] | Cannot give incidence in the exposed and unexposed groups[^song2010observational-e3]; risk of recall bias[^vandenbroucke2007strobe-e26] | Hard to establish that the exposure came before the disease[^vandenbroucke2007strobe-e15] |

**How to choose** (our summary, based on the sources in the table above):

- The outcome is very rare (for example, an uncommon birth defect): use a case-control study. Waiting for enough cases to turn up in a cohort often takes a great many people and many years.
- The exposure is very rare (for example, a particular occupational exposure), or you want to look at several outcomes of the same exposure: use a cohort study.
- You want to know "how many people have this disease or this behavior right now": use a cross-sectional study. If you want to infer cause, first ask yourself whether the exposure must have come before the disease. For characteristics people are born with, such as genes, the order is settled.

**Two naming issues.** Don't just say "prospective" or "retrospective." The STROBE explanation and elaboration paper says these terms are poorly defined and recommends describing exactly how and when the data were collected[^vandenbroucke2007strobe-e17]. A study that follows only one group of people, with no comparison group, is a **case series**, not a cohort study[^song2010observational-e4].

**How it differs from related designs**:

- **Randomized controlled trials**: the researcher assigns the intervention; see [Randomized controlled trials](randomized_controlled_trial.md). Causal analysis of observational data can be seen as emulating a trial you cannot run (see Step 1).
- **[Data science research](data_science.md)**: there the focus is prediction, and the thing to guard against is data leakage. Most studies on this page want to answer questions about causes or effects, and the main enemies are confounding and bias. With the same electronic health records, "predicting who will be readmitted" and "does this drug reduce readmissions" are two different studies.
- **[Longitudinal studies](longitudinal_study.md)**: a cohort study also observes the same people repeatedly over a long time, so what that page says about choosing time points, attrition, and analyzing correlated data all applies. The difference is that the heart of a cohort study is **comparing outcomes between the exposed and unexposed groups**, so you need to put more effort into confounding and selection bias.

## 2. How to do it

### Step 1: Write the question as a "target trial"

First decide whether you are asking an association question or a causal one. A purely descriptive study of association does not need to adjust for confounding[^hernan2018cword-e7] (for why, see the [health sciences field overview](../07_fields/health-sciences/README.md#before-you-start-are-you-answering-a-question-about-association-or-causation)). If it is a causal question, first write the protocol of the trial you would like to run but can't, then explain how you will emulate it with observational data[^hernan2020whatif-e1][^hernan2016target-e1].

**How:** Hernán and Robins's 2016 paper lists the seven components of a target trial protocol. Write each one down[^hernan2016target-e2]:

(1) Eligibility criteria: every eligible person should, in principle, be able to receive each of the treatments being compared[^hernan2020whatif-e2]; (2) the treatment strategies being compared, including when they start and stop; (3) the assignment procedure; (4) the follow-up period; (5) the outcome of interest; (6) the causal contrast of interest (for example, "start the drug" versus "don't"); (7) the analysis plan.

**Why:** it forces you to think clearly about what you are actually comparing. For example, directly comparing the risk of death in people with a body mass index of 25 versus 30 at the start of follow-up amounts to emulating a trial that "suddenly changes people's weight by a large amount at the start of follow-up," which is not a realistic intervention. You can ask a more realistic question instead, such as "from age 40, reduce body mass index by 5% every year for as long as it stays above 25"[^hernan2020whatif-e3].

**Where people go wrong:**

- **Getting the start of follow-up ("time zero") wrong.** The eligibility criteria must be met at time zero, and outcomes are counted from that moment on[^hernan2016target-e5]. With existing data, it is best to set time zero at the moment an eligible person starts a treatment strategy[^hernan2016target-e6]. If time zero comes later than the start of treatment, outcomes that happen in between are missed[^hernan2016target-e5].
- **Selecting people on future events.** Eligibility criteria cannot be things only known after baseline, such as "people who used this drug during follow-up"[^hernan2016target-e3]. Similarly, recruiting only 50-year-olds while studying "lifetime exposure" can also produce selection bias[^hernan2020whatif-e19].
- **Choosing a comparator that invites confounding.** Comparing a treatment with "no treatment" can lead to especially severe confounding; comparing it with another active treatment is better[^hernan2016target-e9].
- You can rarely emulate the ideal trial. In the paper, give the protocol and a flow diagram, and say how the trial you emulated differs from the ideal one[^hernan2016target-e10]. Case-control studies can use the same idea: first work out which follow-up study (cohort) the cases and controls were sampled from[^hernan2016target-e11].

### Step 2: Define the exposure and the outcome

**How:** Give clear definitions of all outcomes, exposures, potential confounders, and effect modifiers (factors that change the size of the exposure's effect), with diagnostic criteria where applicable[^vandenbroucke2007strobe-e23]. In a case-control study, fix the inclusion and exclusion criteria before you select cases[^song2010observational-e7].

**Why:** In a retrospective cohort built from existing data, the researcher has almost no control over data collection; the data may be incomplete or inaccurate, or measured differently for different people[^song2010observational-e10]. The same code can also mean different things. Hernán and Robins give the example of a "breast cancer" code in a database, which might be recorded at diagnosis, or merely when a doctor suspected it and ordered a test; so ask people who know the data, and validate it[^hernan2016target-e4]. Not validating the outcome can lead to misleading estimates[^hernan2016target-e12].

**Where people go wrong:** If you group a continuous exposure into categories and pick the cut points after the fact from several options, tell the reader. Choosing cut points to get the smallest P value exaggerates the association[^vandenbroucke2007strobe-e24].

### Step 3: Choose the study population and the comparison group

**Cohort studies**: The exposed and unexposed groups should come from the same source population (the population the study participants are drawn from); exclude people who cannot develop the outcome[^song2010observational-e5]. Ideally, decide how to handle loss to follow-up when you plan the study[^vandenbroucke2007strobe-e36]; at analysis, compare those who stayed with those who were lost, as far as you can, to see whether they differ systematically[^song2010observational-e6].

**Case-control studies**: The principle is that **controls should reflect the population that gave rise to the cases**[^vandenbroucke2007strobe-e18].

- **Hospital controls** (people with other diseases): for hospital-based cases, they better represent the population the hospital serves, their recall is more comparable, and they are easy to recruit; but if the exposure you are studying affects the occurrence of the controls' diseases or whether they are hospitalized, you have a problem[^vandenbroucke2007strobe-e19]. An example from the book *What If*: studying estrogen and coronary heart disease while preferentially selecting controls from women with hip fractures; since estrogen reduces hip fractures, the results are biased[^hernan2020whatif-e14].
- **Watch where the cases come from**: cases selected in hospital tend to be more severely ill than those in the community[^song2010observational-e7]. Having cases and controls reach diagnosis through the same referral pathway can offset this kind of bias[^vandenbroucke2007strobe-e28].
- **Number of controls**: about three or four controls per case may improve precision[^song2010observational-e8].

**Be careful with matching.** Matching is intuitively appealing, but methodologists advise against routine matching in case-control studies[^vandenbroucke2007strobe-e20]. When the matching factor is related to the exposure and you match but don't use a matched or stratified analysis, the odds ratio (the usual measure of association in case-control studies) is usually biased toward 1, that is, toward "no association"[^vandenbroucke2007strobe-e22]. The most dangerous case is matching on a variable on the causal pathway, for example matching on birth weight when studying in vitro fertilization and perinatal death; this bias cannot be fixed in the analysis[^vandenbroucke2007strobe-e21].

### Step 4: Measure the exposure, especially self-reports and diet

For why inaccurate measurement causes problems, see [pitfall 2](../07_fields/health-sciences/README.md#pitfall-2-exposures-are-hard-to-measure-especially-diet) in the health sciences field overview. In practice:

- **Measure both groups the same way.** If interviewers question all the cases first and then the controls, growing practice can introduce bias; you can randomize the order of interviews[^vandenbroucke2007strobe-e25]. An example cited in the STROBE explanation and elaboration paper: samples from matched cases and controls were always assayed in the same batch, and laboratory staff could not tell which were cases[^vandenbroucke2007strobe-e45].
- **Blind where you can.** Cases may recall or report past exposures with different accuracy from controls (recall bias); interviewers who know the study hypothesis may, consciously or not, collect data selectively[^vandenbroucke2007strobe-e26]. An example from *What If*: asking mothers about their alcohol intake during pregnancy only after delivery means their recall is affected by how the pregnancy turned out[^hernan2020whatif-e17]. Use trained interviewers and standardized interviews to reduce interviewer bias[^song2010observational-e9].
- **Fix it at the source.** *What If* says the best way to deal with measurement bias is to improve the measurement procedure itself[^hernan2020whatif-e18].

**Diet** is especially hard to measure. The US National Cancer Institute's Dietary Assessment Primer says diet can rarely be observed directly and usually relies on self-report instruments such as 24-hour dietary recalls, food records, and food frequency questionnaires[^nci2025dietprimer-e1]; what studies usually care about is "usual intake" (the long-run average), not what someone ate on a particular day[^nci2025dietprimer-e2]. Food frequency questionnaires are mainly used to assess long-run average intake[^lachat2016strobenut-e2]. A few things to know:

- **Misreporting is unavoidable**, both under-reporting and over-reporting[^nci2025dietprimer-e6]. Energy under-reporting is most consistently related to body mass index[^nci2025dietprimer-e8], so when you study diet and obesity-related diseases, the misreporting itself may be related to the outcome.
- **The direction of the error is not fixed.** With a single dietary exposure and only random within-person error, the association is always attenuated[^nci2025dietprimer-e3]; when there is also systematic error, it may be attenuated or exaggerated[^nci2025dietprimer-e4]; when the model contains other dietary variables that are equally hard to measure, it may also be attenuated or exaggerated[^nci2025dietprimer-e5]. So the claim that "measurement error only makes results conservative" does not always hold.
- **What you can do**: average repeated measurements[^nci2025dietprimer-e9]; adjust for energy intake[^lachat2016strobenut-e5]; be careful about dropping misreporters, and consider a sensitivity analysis with and without them[^nci2025dietprimer-e7], comparing participant characteristics before and after exclusion[^lachat2016strobenut-e4].
- **In validation studies, check what the reference method is.** Ideal reference measures are few, only a handful such as doubly labeled water (for energy) and 24-hour urinary nitrogen (for protein); in practice, imperfect references such as 24-hour recalls or food records are common[^lachat2016strobenut-e3].

### Step 5: Handle confounding: draw a causal diagram first, then decide what to adjust for

**How:**
1. **Think about confounders at the design stage**, because this decides which data you need to collect in detail. In the design you can use restriction (for example, studying only one age group) or matching[^vandenbroucke2007strobe-e29]. If you can't get data on a confounder, do a sensitivity analysis to estimate the bias it might cause[^hernan2020whatif-e10].
2. **Draw a causal diagram** (a directed acyclic graph, DAG): draw the causal relationships you believe in as arrows. In a 2021 review of how these diagrams are used in health research, Tennant and colleagues found that, of 234 original health research articles published 1999–2017 that used one, 21% stated the quantity they were estimating, 48% reported the adjustment set implied by the diagram, and 62% published at least one diagram[^tennant2021dags-e1]. Their recommendations include:
   - Include every plausible confounder, **including unmeasured ones**[^tennant2021dags-e3];
   - Arrange the variables so that all arrows point the same way (left to right or top to bottom)[^tennant2021dags-e7];
   - Leaving out an arrow between two variables means assuming that neither has any causal effect on the other[^tennant2021dags-e4], so removing an arrow needs a reason;
   - Put the diagram in the main text or the supplementary material, or give an online link to it[^tennant2021dags-e2].
3. **Derive the variables to adjust for from the diagram** (the adjustment set) and state it in the paper; if you also use a different adjustment set, explain why and report the results separately[^tennant2021dags-e5]. State the quantity you want to estimate (the estimand) in the study aims first[^tennant2021dags-e6].
4. **Adjust in the analysis using stratification or multivariable models**[^vandenbroucke2007strobe-e30].

**Why you can't rely on statistics alone to choose variables**: associations or statistical criteria alone are not enough to decide what is a confounder[^hernan2020whatif-e6]. Causal inference from observational data needs prior causal knowledge; drawing it as a diagram makes your assumptions explicit, so others can criticize them concretely[^hernan2020whatif-e7]. See also ["don't let software choose your confounders"](../07_fields/health-sciences/README.md#before-you-start-are-you-answering-a-question-about-association-or-causation) in the health sciences field overview.

**Where people go wrong:**

- **Adjusting for variables you shouldn't.** In general, don't adjust for variables affected by the exposure or the outcome[^hernan2020whatif-e8], such as intermediate variables on the causal pathway from exposure to disease[^vandenbroucke2007strobe-e31].
- **Choosing variables by "how much the estimate changes when it is added" without stating the criterion.** If you use this approach, report how large a change was needed for inclusion[^vandenbroucke2007strobe-e32].
- **Assuming adjustment makes you safe.** If the confounders themselves are measured poorly, residual confounding remains. Socioeconomic status is the classic case: income, education, and occupation are only proxies for it[^vandenbroucke2007strobe-e47].
- **Picking just one causal structure when two are plausible.** Analyze under each, and state the assumptions each analysis needs to be valid[^hernan2020whatif-e9].
- Learn to recognize common confounding structures: for example, being healthy makes people able to become firefighters and also gives them a lower risk of death[^hernan2020whatif-e4]; subclinical disease that hasn't yet been diagnosed makes people exercise less and also raises their risk of the disease (often called "reverse causation")[^hernan2020whatif-e5].

### Step 6: Guard against selection bias and information bias

**Selection bias** is an association created by "who gets into the analysis"; it is different from confounding and can occur even in randomized trials[^hernan2020whatif-e12]. Randomization protects against confounding but not against selection bias that arises after randomization[^hernan2020whatif-e15]. Sources include analyzing only people with complete outcome data (whatever the reason for the missing data)[^hernan2020whatif-e13], as well as the poor choice of controls[^hernan2020whatif-e14] and wrong time zero[^hernan2016target-e5] discussed above. For bias from people choosing whether to take part, see [pitfall 3](../07_fields/health-sciences/README.md#pitfall-3-who-takes-part-can-itself-create-an-association) in the health sciences field overview.

**Information bias** comes from measurement. Besides the recall bias in Step 4, also guard against **detection bias**: for example, people taking a drug that causes stomach upset have more endoscopies and so are found to have more ulcers, even if the drug does not cause ulcers; you can measure how intensively each group is examined and adjust for it in the analysis[^vandenbroucke2007strobe-e27]. Ideally, outcome ascertainment should not be affected by knowing who took the drug; deaths obtained independently from a death registry are not affected[^hernan2016target-e8]. Measurement bias can occur in any design and should always be considered when interpreting results[^hernan2020whatif-e16].

### Step 7: Analysis

- **Write the main analyses into the protocol in advance**, and when reporting, say which analyses you thought of only after seeing the data[^vandenbroucke2007strobe-e33]. This is the [distinction between exploratory and confirmatory research](../02_do-the-project/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring) covered in Part 2.
- **Give both unadjusted and adjusted estimates**, so readers can see how much adjustment changed the result and in which direction[^vandenbroucke2007strobe-e34].
- **Missing data**: analyzing only people with complete data may be biased and always loses efficiency; the assumptions behind the various methods for handling missing data generally can't be verified, so they are best treated as sensitivity analyses[^vandenbroucke2007strobe-e35]. Adding a "missing" category for a confounder can increase residual confounding[^vandenbroucke2007strobe-e46].
- **In case-control studies, don't judge confounding from baseline differences between cases and controls**: controls represent the source population and naturally differ from cases in many ways[^vandenbroucke2007strobe-e40].
- **Sample size**: when you use data already collected for another purpose, what matters is whether precision is adequate, and sample size considerations can be informal; don't do post hoc power calculations[^vandenbroucke2007strobe-e44]. For general statistical practice, see the Part 2 section [Report how big the difference is and how certain you are, not just the p-value](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 8: Sensitivity analyses

**How:** Change an analysis strategy or assumption and see whether the main result changes; you can change, for example, the inclusion criteria or the definitions of exposure and outcome[^vandenbroucke2007strobe-e37]. For this kind of study specifically:

- **Unmeasured confounding**: ask "how strong would a confounder have to be to explain the result away?" The classic example is the 1959 analysis by Cornfield and colleagues: the relative risk (how many times higher the risk is in the exposed than in the unexposed) of lung cancer for smoking was 9, so any confounder that could explain it would have to be at least 9 times as prevalent in smokers as in nonsmokers[^vandenbroucke2007strobe-e38]. When the confounder is unknown, repeat the analysis under several assumptions about the size of the bias[^hernan2020whatif-e11].
- **A "reverse" comparison**: for example, also emulate a trial of "continuing the drug versus stopping it." If both "starting the drug" and "stopping the drug" appear to lower risk, at least one of the analyses did not achieve a fair comparison[^hernan2016target-e7].
- **Do them even when the result is "no association"**: confounding or bias can pull a result toward no association[^vandenbroucke2007strobe-e39].

### Step 9: Reporting

- **STROBE**: applies to all three designs (cohort, case-control, and cross-sectional)[^vonelm2007strobe-e2] and has 22 items[^vonelm2007strobe-e4]. It covers only how to report, not how to design a study, and it is not a quality assessment tool[^vonelm2007strobe-e3].
- **Routinely collected data**: in addition to STROBE, report according to its extension RECORD (13 items)[^benchimol2015record-e3]. A few points the field overview doesn't cover: when you link several databases, you can use a flow diagram to show how many people were linked at each step[^benchimol2015record-e16]; describe in detail how the study population was selected step by step[^benchimol2015record-e19]; and state how much access the researchers had to the original databases and how the data were cleaned[^benchimol2015record-e17]. The reason is that when a data analyst who doesn't know the details of cohort construction or the study's aims builds the cohort, mistakes are easy to make[^benchimol2015record-e18].
- **Diet studies**: also use STROBE-nut, the STROBE extension for nutritional epidemiology, which adds 24 recommendations to STROBE[^lachat2016strobenut-e1], for example stating the reference method, timing, and population of the validation study for your dietary assessment method[^lachat2016strobenut-e6].
- **Limitations**: don't just list biases; discuss their likely direction and size[^vandenbroucke2007strobe-e41]. The real uncertainty is larger than the confidence interval shows[^vandenbroucke2007strobe-e42]. Adjusted results may still be affected by random error, selection bias, information bias, or residual confounding[^vandenbroucke2007strobe-e34]; for the debate over "causal" language, see the [health sciences field overview](../07_fields/health-sciences/README.md#before-you-start-are-you-answering-a-question-about-association-or-causation).

## 3. Checklist

**Must do** (compiled from STROBE and its explanation and elaboration paper, RECORD, STROBE-nut, and the sources above)

- [ ] State whether you are asking an association question or a causal one[^hernan2018cword-e7]; for a causal question, write out each component of the target trial, especially time zero[^hernan2016target-e2][^hernan2016target-e5]
- [ ] Define every exposure, outcome, and confounder, with diagnostic criteria where applicable[^vandenbroucke2007strobe-e23]
- [ ] In a case-control study, explain where the controls come from and why they reflect the population that gave rise to the cases[^vandenbroucke2007strobe-e18]
- [ ] Decide which variables to adjust for using causal knowledge or explicit assumptions, not statistical criteria alone[^vandenbroucke2007strobe-e31][^hernan2020whatif-e6]
- [ ] Report both unadjusted and adjusted estimates[^vandenbroucke2007strobe-e34]
- [ ] Decide in advance how to handle loss to follow-up and missing data, and report it honestly[^vandenbroucke2007strobe-e36][^vandenbroucke2007strobe-e35]
- [ ] Discuss the direction and size of biases[^vandenbroucke2007strobe-e41]
- [ ] Report according to STROBE[^vonelm2007strobe-e2]; add RECORD when using existing data[^benchimol2015record-e3], and STROBE-nut for diet studies[^lachat2016strobenut-e1]

**Better practice**

- [ ] Draw a causal diagram, include it in the paper, and state the adjustment set[^tennant2021dags-e2][^tennant2021dags-e5]
- [ ] Do sensitivity analyses: change the exposure and outcome definitions[^vandenbroucke2007strobe-e37], assess unmeasured confounding[^hernan2020whatif-e11], and try other ways of handling missing data[^vandenbroucke2007strobe-e35]
- [ ] Use a "reverse" comparison to check confounding indirectly[^hernan2016target-e7]
- [ ] Describe the validation study for your exposure measurement, including the reference method, timing, and population[^lachat2016strobenut-e6]; for more, see [pitfall 2](../07_fields/health-sciences/README.md#pitfall-2-exposures-are-hard-to-measure-especially-diet) in the health sciences field overview
- [ ] Explain how the target trial you emulated differs from the ideal trial[^hernan2016target-e10]

**Fine to skip; not a flaw**

- Not adjusting for confounding in a purely descriptive study of association[^hernan2018cword-e7].
- Not matching in a case-control study: methodologists advise against routine matching anyway[^vandenbroucke2007strobe-e20].
- Not doing a formal sample size calculation when using data already collected for another purpose, and discussing only whether precision is adequate[^vandenbroucke2007strobe-e44].

**Common reviewer criticisms that don't hold up**

- **"Your results may be confounded."** *What If* says that a critic who makes such a generic criticism "is not making a scientific statement, but a logical one"; once a critic names a specific factor (such as smoking), the researcher's next step is to adjust for it, and if the data aren't available, to do a sensitivity analysis[^hernan2020whatif-e10].
- **"A relative risk below 2 or 3 isn't believable."** The STROBE explanation and elaboration paper notes that some have argued for ignoring relative risks below 2 or 3, but it points out that a relative risk below 3 is not necessarily spurious[^vandenbroucke2007strobe-e43].
- **"The cases and controls differ a lot at baseline, so they aren't comparable."** In a case-control study the controls represent the source population and usually differ from the cases in many ways; you can't judge confounding this way[^vandenbroucke2007strobe-e40].

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Follow-up starts later than the start of treatment | Outcomes in between are missed, producing selection bias[^hernan2016target-e5] |
| Eligibility criteria say "people who used the drug during follow-up" | Selecting people on events after baseline introduces bias[^hernan2016target-e3] |
| Controls drawn from people with a disease related to the exposure | E.g., selecting controls from hip fracture patients to study estrogen: whether controls are selected depends on a consequence of the exposure[^hernan2020whatif-e14] |
| Matching or adjusting on an intermediate variable on the causal pathway | Matching creates bias that can't be fixed in the analysis[^vandenbroucke2007strobe-e21]; adjusting also introduces bias[^vandenbroucke2007strobe-e31] |
| Matching but not using a matched analysis | When the matching factor is related to the exposure, the odds ratio is usually biased toward 1[^vandenbroucke2007strobe-e22] |
| Choosing confounders by significance tests or other statistical criteria alone | Statistical criteria are not enough to decide what is a confounder[^hernan2020whatif-e6] |
| Choosing exposure cut points to get the smallest P value | Exaggerates the association[^vandenbroucke2007strobe-e24] |
| Assuming dietary measurement error only makes results conservative | With systematic error or several poorly measured dietary variables, it can also exaggerate the association[^nci2025dietprimer-e4][^nci2025dietprimer-e5] |
| Dropping "misreporters" without comparing | May introduce selection bias[^lachat2016strobenut-e4] |
| Writing only "prospective cohort study" | The term is poorly defined; say how and when the data were collected[^vandenbroucke2007strobe-e17] |
| Calling follow-up of a single group a cohort study | Without a comparison group it is a case series[^song2010observational-e4] |

## 5. Further reading

- **The STROBE explanation and elaboration paper (Vandenbroucke et al. 2007)**: the source of most of the practices on this page. Read it item by item while you design the study, especially Box 2 (matching), Box 3 (bias), Box 5 (confounding), Box 6 (missing data), and Item 12 (statistical methods).
- **Hernán & Robins, *Causal Inference: What If***: a causal inference textbook, free to download from the authors' website. This page uses parts of Section 3.6 (target trials) and Chapters 7, 8, and 9 (confounding, selection bias, measurement bias).
- **Hernán & Robins 2016, "Using Big Data to Emulate a Target Trial"**: read it before doing causal analysis with existing data; it covers specific traps around time zero, eligibility criteria, and outcome ascertainment.
- **Tennant et al. 2021**: a review of how causal diagrams are used in health research; the recommendations in the second half are useful to check against while you draw your diagram.
- **Song & Chung 2010**: an introductory article for surgeons that uses surgical examples to explain the strengths and weaknesses of cohort and case-control studies and how to select participants.
- **The US National Cancer Institute's Dietary Assessment Primer and STROBE-nut (Lachat et al. 2016)**: read them if you study diet; the first covers measurement error, the second covers reporting.
- Our sources do not cover how to implement specific statistical methods (such as inverse probability weighting or propensity scores); follow your advisor, a statistical collaborator, or the textbooks above.

[^song2010observational-e1]: Song & Chung 2010, Introduction. [Evidence](../../sources/notes/song2010observational.md#e1)
[^song2010observational-e2]: Song & Chung 2010, Cohort Studies. [Evidence](../../sources/notes/song2010observational.md#e2)
[^song2010observational-e3]: Song & Chung 2010, Case-Control Studies and Table 4. [Evidence](../../sources/notes/song2010observational.md#e3)
[^song2010observational-e4]: Song & Chung 2010, Cohort Studies (how they differ from case series). [Evidence](../../sources/notes/song2010observational.md#e4)
[^song2010observational-e5]: Song & Chung 2010, Selection of Subjects in Cohort Studies. [Evidence](../../sources/notes/song2010observational.md#e5)
[^song2010observational-e6]: Song & Chung 2010, Attrition Bias. [Evidence](../../sources/notes/song2010observational.md#e6)
[^song2010observational-e7]: Song & Chung 2010, Selection of Cases. [Evidence](../../sources/notes/song2010observational.md#e7)
[^song2010observational-e8]: Song & Chung 2010, Selection of Controls. [Evidence](../../sources/notes/song2010observational.md#e8)
[^song2010observational-e9]: Song & Chung 2010, Bias in Case-Control Studies. [Evidence](../../sources/notes/song2010observational.md#e9)
[^song2010observational-e10]: Song & Chung 2010, Cohort Studies (retrospective cohorts). [Evidence](../../sources/notes/song2010observational.md#e10)
[^vandenbroucke2007strobe-e14]: Vandenbroucke et al. 2007, Box 1. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e14)
[^vandenbroucke2007strobe-e15]: Vandenbroucke et al. 2007, Box 1. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e15)
[^vandenbroucke2007strobe-e16]: Vandenbroucke et al. 2007, Box 1. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e16)
[^vandenbroucke2007strobe-e17]: Vandenbroucke et al. 2007, Item 4. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e17)
[^vandenbroucke2007strobe-e18]: Vandenbroucke et al. 2007, Item 6. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e18)
[^vandenbroucke2007strobe-e19]: Vandenbroucke et al. 2007, Item 6. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e19)
[^vandenbroucke2007strobe-e20]: Vandenbroucke et al. 2007, Box 2. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e20)
[^vandenbroucke2007strobe-e21]: Vandenbroucke et al. 2007, Box 2. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e21)
[^vandenbroucke2007strobe-e22]: Vandenbroucke et al. 2007, Box 2. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e22)
[^vandenbroucke2007strobe-e23]: STROBE checklist, Item 7. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e23)
[^vandenbroucke2007strobe-e24]: Vandenbroucke et al. 2007, Box 4. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e24)
[^vandenbroucke2007strobe-e25]: Vandenbroucke et al. 2007, Item 8. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e25)
[^vandenbroucke2007strobe-e26]: Vandenbroucke et al. 2007, Box 3. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e26)
[^vandenbroucke2007strobe-e27]: Vandenbroucke et al. 2007, Box 3. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e27)
[^vandenbroucke2007strobe-e28]: Vandenbroucke et al. 2007, Box 3. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e28)
[^vandenbroucke2007strobe-e29]: Vandenbroucke et al. 2007, Box 5. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e29)
[^vandenbroucke2007strobe-e30]: Vandenbroucke et al. 2007, Box 5. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e30)
[^vandenbroucke2007strobe-e31]: Vandenbroucke et al. 2007, Item 16. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e31)
[^vandenbroucke2007strobe-e32]: Vandenbroucke et al. 2007, Item 16. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e32)
[^vandenbroucke2007strobe-e33]: Vandenbroucke et al. 2007, Item 12. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e33)
[^vandenbroucke2007strobe-e34]: Vandenbroucke et al. 2007, Item 16. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e34)
[^vandenbroucke2007strobe-e35]: Vandenbroucke et al. 2007, Box 6. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e35)
[^vandenbroucke2007strobe-e36]: Vandenbroucke et al. 2007, Item 12(d). [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e36)
[^vandenbroucke2007strobe-e37]: Vandenbroucke et al. 2007, Item 12(e). [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e37)
[^vandenbroucke2007strobe-e38]: Vandenbroucke et al. 2007, Item 12(e). [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e38)
[^vandenbroucke2007strobe-e39]: Vandenbroucke et al. 2007, Item 12(e). [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e39)
[^vandenbroucke2007strobe-e40]: Vandenbroucke et al. 2007, Item 14. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e40)
[^vandenbroucke2007strobe-e41]: Vandenbroucke et al. 2007, Item 19. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e41)
[^vandenbroucke2007strobe-e42]: Vandenbroucke et al. 2007, Item 20. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e42)
[^vandenbroucke2007strobe-e43]: Vandenbroucke et al. 2007, Item 20. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e43)
[^vandenbroucke2007strobe-e44]: Vandenbroucke et al. 2007, Item 10. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e44)
[^vandenbroucke2007strobe-e45]: Vandenbroucke et al. 2007, Item 8, Example 2. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e45)
[^vandenbroucke2007strobe-e46]: Vandenbroucke et al. 2007, Box 6. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e46)
[^vandenbroucke2007strobe-e47]: Vandenbroucke et al. 2007, Item 20. [Evidence](../../sources/notes/vandenbroucke2007strobe.md#e47)
[^vonelm2007strobe-e2]: von Elm et al. 2007, Aims and Use of the STROBE Statement. [Evidence](../../sources/notes/vonelm2007strobe.md#e2)
[^vonelm2007strobe-e3]: von Elm et al. 2007, Aims and Use of the STROBE Statement. [Evidence](../../sources/notes/vonelm2007strobe.md#e3)
[^vonelm2007strobe-e4]: von Elm et al. 2007, STROBE Components. [Evidence](../../sources/notes/vonelm2007strobe.md#e4)
[^benchimol2015record-e3]: Benchimol et al. 2015, Abstract and Introduction. [Evidence](../../sources/notes/benchimol2015record.md#e3)
[^benchimol2015record-e16]: Benchimol et al. 2015, RECORD 6.3. [Evidence](../../sources/notes/benchimol2015record.md#e16)
[^benchimol2015record-e17]: Benchimol et al. 2015, RECORD 12.1, 12.2. [Evidence](../../sources/notes/benchimol2015record.md#e17)
[^benchimol2015record-e18]: Benchimol et al. 2015, explanation of RECORD 12.1, 12.2. [Evidence](../../sources/notes/benchimol2015record.md#e18)
[^benchimol2015record-e19]: Benchimol et al. 2015, RECORD 13.1. [Evidence](../../sources/notes/benchimol2015record.md#e19)
[^hernan2018cword-e7]: Hernán 2018, Better Confounding Adjustment. [Evidence](../../sources/notes/hernan2018cword.md#e7)
[^hernan2016target-e1]: Hernán & Robins 2016, Abstract. [Evidence](../../sources/notes/hernan2016target.md#e1)
[^hernan2016target-e2]: Hernán & Robins 2016, Introduction (Table 1). [Evidence](../../sources/notes/hernan2016target.md#e2)
[^hernan2016target-e3]: Hernán & Robins 2016, Eligibility criteria. [Evidence](../../sources/notes/hernan2016target.md#e3)
[^hernan2016target-e4]: Hernán & Robins 2016, Emulating the Target Trial. [Evidence](../../sources/notes/hernan2016target.md#e4)
[^hernan2016target-e5]: Hernán & Robins 2016, Defining Time Zero. [Evidence](../../sources/notes/hernan2016target.md#e5)
[^hernan2016target-e6]: Hernán & Robins 2016, Defining Time Zero. [Evidence](../../sources/notes/hernan2016target.md#e6)
[^hernan2016target-e7]: Hernán & Robins 2016, Assignment procedures. [Evidence](../../sources/notes/hernan2016target.md#e7)
[^hernan2016target-e8]: Hernán & Robins 2016, Outcome. [Evidence](../../sources/notes/hernan2016target.md#e8)
[^hernan2016target-e9]: Hernán & Robins 2016, Assignment procedures. [Evidence](../../sources/notes/hernan2016target.md#e9)
[^hernan2016target-e10]: Hernán & Robins 2016, Discussion. [Evidence](../../sources/notes/hernan2016target.md#e10)
[^hernan2016target-e11]: Hernán & Robins 2016, Discussion. [Evidence](../../sources/notes/hernan2016target.md#e11)
[^hernan2016target-e12]: Hernán & Robins 2016, Outcome. [Evidence](../../sources/notes/hernan2016target.md#e12)
[^hernan2020whatif-e1]: Hernán & Robins, What If, §3.6. [Evidence](../../sources/notes/hernan2020whatif.md#e1)
[^hernan2020whatif-e2]: Hernán & Robins, What If, §3.6. [Evidence](../../sources/notes/hernan2020whatif.md#e2)
[^hernan2020whatif-e3]: Hernán & Robins, What If, §3.6. [Evidence](../../sources/notes/hernan2020whatif.md#e3)
[^hernan2020whatif-e4]: Hernán & Robins, What If, §7.1. [Evidence](../../sources/notes/hernan2020whatif.md#e4)
[^hernan2020whatif-e5]: Hernán & Robins, What If, §7.1. [Evidence](../../sources/notes/hernan2020whatif.md#e5)
[^hernan2020whatif-e6]: Hernán & Robins, What If, §7.4. [Evidence](../../sources/notes/hernan2020whatif.md#e6)
[^hernan2020whatif-e7]: Hernán & Robins, What If, §7.4. [Evidence](../../sources/notes/hernan2020whatif.md#e7)
[^hernan2020whatif-e8]: Hernán & Robins, What If, §7.6. [Evidence](../../sources/notes/hernan2020whatif.md#e8)
[^hernan2020whatif-e9]: Hernán & Robins, What If, §7.6. [Evidence](../../sources/notes/hernan2020whatif.md#e9)
[^hernan2020whatif-e10]: Hernán & Robins, What If, §7.6. [Evidence](../../sources/notes/hernan2020whatif.md#e10)
[^hernan2020whatif-e11]: Hernán & Robins, What If, §7.3. [Evidence](../../sources/notes/hernan2020whatif.md#e11)
[^hernan2020whatif-e12]: Hernán & Robins, What If, Chapter 8, opening. [Evidence](../../sources/notes/hernan2020whatif.md#e12)
[^hernan2020whatif-e13]: Hernán & Robins, What If, §8.2. [Evidence](../../sources/notes/hernan2020whatif.md#e13)
[^hernan2020whatif-e14]: Hernán & Robins, What If, Chapter 8 Fine Point (selection bias in case-control studies). [Evidence](../../sources/notes/hernan2020whatif.md#e14)
[^hernan2020whatif-e15]: Hernán & Robins, What If, §8.3. [Evidence](../../sources/notes/hernan2020whatif.md#e15)
[^hernan2020whatif-e16]: Hernán & Robins, What If, Chapter 9, opening. [Evidence](../../sources/notes/hernan2020whatif.md#e16)
[^hernan2020whatif-e17]: Hernán & Robins, What If, §9.2. [Evidence](../../sources/notes/hernan2020whatif.md#e17)
[^hernan2020whatif-e18]: Hernán & Robins, What If, §9.2. [Evidence](../../sources/notes/hernan2020whatif.md#e18)
[^hernan2020whatif-e19]: Hernán & Robins, What If, §8.2. [Evidence](../../sources/notes/hernan2020whatif.md#e19)
[^nci2025dietprimer-e1]: U.S. National Cancer Institute, Dietary Assessment Primer, Key Concepts about Measurement Error. [Evidence](../../sources/notes/nci2025dietprimer.md#e1)
[^nci2025dietprimer-e2]: Ibid. [Evidence](../../sources/notes/nci2025dietprimer.md#e2)
[^nci2025dietprimer-e3]: U.S. National Cancer Institute, Dietary Assessment Primer, Effects of Measurement Error. [Evidence](../../sources/notes/nci2025dietprimer.md#e3)
[^nci2025dietprimer-e4]: Ibid. [Evidence](../../sources/notes/nci2025dietprimer.md#e4)
[^nci2025dietprimer-e5]: Ibid. [Evidence](../../sources/notes/nci2025dietprimer.md#e5)
[^nci2025dietprimer-e6]: U.S. National Cancer Institute, Dietary Assessment Primer, Learn More about Misreporting. [Evidence](../../sources/notes/nci2025dietprimer.md#e6)
[^nci2025dietprimer-e7]: Ibid. [Evidence](../../sources/notes/nci2025dietprimer.md#e7)
[^nci2025dietprimer-e8]: Ibid. [Evidence](../../sources/notes/nci2025dietprimer.md#e8)
[^nci2025dietprimer-e9]: U.S. National Cancer Institute, Dietary Assessment Primer, Effects of Measurement Error, Table 1. [Evidence](../../sources/notes/nci2025dietprimer.md#e9)
[^lachat2016strobenut-e1]: Lachat et al. 2016, Abstract. [Evidence](../../sources/notes/lachat2016strobenut.md#e1)
[^lachat2016strobenut-e2]: Lachat et al. 2016, Introduction. [Evidence](../../sources/notes/lachat2016strobenut.md#e2)
[^lachat2016strobenut-e3]: Lachat et al. 2016, Introduction. [Evidence](../../sources/notes/lachat2016strobenut.md#e3)
[^lachat2016strobenut-e4]: Lachat et al. 2016, nut-9. [Evidence](../../sources/notes/lachat2016strobenut.md#e4)
[^lachat2016strobenut-e5]: Lachat et al. 2016, nut-12.2. [Evidence](../../sources/notes/lachat2016strobenut.md#e5)
[^lachat2016strobenut-e6]: Lachat et al. 2016, nut-8.6. [Evidence](../../sources/notes/lachat2016strobenut.md#e6)
[^tennant2021dags-e1]: Tennant et al. 2021, Abstract. [Evidence](../../sources/notes/tennant2021dags.md#e1)
[^tennant2021dags-e2]: Tennant et al. 2021, Recommendations. [Evidence](../../sources/notes/tennant2021dags.md#e2)
[^tennant2021dags-e3]: Tennant et al. 2021, Recommendations. [Evidence](../../sources/notes/tennant2021dags.md#e3)
[^tennant2021dags-e4]: Tennant et al. 2021, Recommendations. [Evidence](../../sources/notes/tennant2021dags.md#e4)
[^tennant2021dags-e5]: Tennant et al. 2021, Recommendations. [Evidence](../../sources/notes/tennant2021dags.md#e5)
[^tennant2021dags-e6]: Tennant et al. 2021, Recommendations. [Evidence](../../sources/notes/tennant2021dags.md#e6)
[^tennant2021dags-e7]: Tennant et al. 2021, Recommendations. [Evidence](../../sources/notes/tennant2021dags.md#e7)
