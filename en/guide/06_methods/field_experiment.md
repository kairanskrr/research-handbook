# Field experiments

This page is about **field experiments**: working in the real world with a government, a nongovernmental organization (NGO), a firm, or a community, you randomly decide who receives an intervention (a cash transfer, a training program, a get-out-the-vote letter, and so on), then compare outcomes across the groups. Economics (especially development economics) and political science both use the method.

This page covers only what is specific to field experiments. The following are covered elsewhere and not repeated here: identification strategies in economics and the registration requirements of the American Economic Association (AEA), in the [economics and business field overview](../07_fields/economics/README.md); pre-analysis plans in political science and the debate over the ethics of election experiments, in the [political science field overview](../07_fields/political-science/README.md); how randomized trials are run in clinical medicine (random sequence, intention-to-treat analysis, reporting guidelines), in [Randomized controlled trials](randomized_controlled_trial.md); controlled experiments in the lab, in [Controlled experiments](controlled_experiment.md).

**Scope**: this page was written for [Economics and business](../07_fields/economics/README.md) (especially development economics) and [Political science](../07_fields/political-science/README.md). Its sources are mainly the methods review by Duflo and colleagues, the research resources of J-PAL (the Abdul Latif Jameel Poverty Action Lab at the Massachusetts Institute of Technology), the methods guides of EGAP (Evidence in Governance and Politics, an experimental research network in political science), and the rules of the American Economic Association and the American Political Science Association. So the requirements on registration, ethics, and pre-analysis plans are the conventions of these two fields. The [Education](../07_fields/education/README.md) field overview also points here. If you run a field experiment in another field, check your own field's norms first; for randomized trials of medical interventions, see [Randomized controlled trials](randomized_controlled_trial.md).

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md).


**After reading this page, you should be able to:**

- judge whether your question can be answered with a field experiment, and choose the right way to introduce randomization;
- agree on roles with the implementing partner, choose the unit of randomization, do the power calculations, and randomize;
- handle attrition, noncompliance, and spillovers, and tell the "intention-to-treat effect" apart from "the effect on those who actually took up the program".

---

## 1. What this kind of research is and when to use it

At its core, a field experiment is still about random assignment: if assignment is random, the groups are on average similar before the intervention, so differences in outcomes can be attributed to the intervention. What sets it apart most from other randomized experiments is that **the program is real, and someone else runs it**. This page draws heavily on the 2007 methods review by Duflo, Glennerster, and Kremer (a National Bureau of Economic Research working paper on using randomization in development economics). They note that such randomized studies usually work with an implementing partner (a government, NGO, or firm) that is running a real program and wants to know whether it works and how to improve it[^duflo2007toolkit-e1]; introducing randomization into a real program almost always means working with whoever actually implements it[^duflo2007toolkit-e2].

| | Field experiment | Clinical randomized controlled trial | Lab controlled experiment | Quasi-experiment (natural experiment) |
|---|---|---|---|---|
| Who delivers the intervention | A partner government, organization, or firm | The research team, giving drugs or treatment per protocol | The researcher | No one does it for the study; it comes from a policy or an event |
| Unit of randomization | Often groups: villages, schools, stores | Mostly individual patients | Mostly individual participants | Not randomized |
| Main difficulties | Implementation drift, attrition, spillovers, partner cooperation | Blinding, safety monitoring, reporting guidelines | Artificial setting; whether findings carry over to the real world | Arguing that assignment is "as good as random" |

(The table is our own summary. For what to do when you cannot randomize, see [Quasi-experiments and causal identification](quasi_experiment.md).)

**When you can do one.** You need some opening that lets you influence "who gets the program first". Duflo and colleagues summarize several entry points:

- **Lotteries when places are limited**: if resources are limited and applicants outnumber places, a lottery among eligible applicants is both natural and fair[^duflo2007toolkit-e4].
- **Randomizing the order of a phase-in**: suitable where "no one can be left without help for good"[^duflo2007toolkit-e5]. The gap between phases has to be longer than the time the effect needs to show up; if the comparison group changes its behavior because it expects its turn to come, the design has a problem[^duflo2007toolkit-e6].
- **Randomizing within units** (for example, randomly choosing which grade in a school gets the program): the drawback is that the comparison group is more likely to be contaminated[^duflo2007toolkit-e7].
- **Encouragement designs**: instead of randomizing the program itself, you randomize encouragement to take part[^duflo2007toolkit-e8].

**When not to do one.** J-PAL's ethics guidance says: do not deny participants an intervention or service they are otherwise entitled to[^jpal2022ethics-e5]. In that case consider a phase-in or an encouragement design.

---

## 2. How to do it

### Step 1: Find an implementing partner and agree on goals and roles first

**How:**

- **Choose a partner.** In Duflo and colleagues' comparison, working with a government gives wider coverage and makes it easier for results to feed into policy; NGOs and firms are more flexible, and it is easier for researchers to monitor whether the design is followed[^duflo2007toolkit-e3].
- **Ask what the partner wants to learn.** EGAP has a guide written for implementers, which warns that if the implementer does not spell out what it needs to know, the evaluator may not be able to design the most suitable approach[^egapevaluationconversations-e1].
- **Agree in advance on what happens if the results are bad.** The guide suggests a "pre-mortem": both sides start by imagining that the evaluation has come back null or negative[^egapevaluationconversations-e4]. Also agree on how and where results will be made public; the two sides' timelines are likely to differ[^egapevaluationconversations-e3].
- **Put the agreement in writing**: who does the randomization, who has the authority to change it, who owns the data, and whether the paper can be published freely.

**Why:** the partner runs the program, not you. Even when an evaluation is meant for learning, some people in the organization will worry that the results could affect their careers[^egapevaluationconversations-e2].

**Where people go wrong:** talking only to the partner's senior staff and not to the people on the front line. J-PAL warns that a feature important to the design (such as randomly drawing payment amounts) may look unfair to field staff[^jpal2022ethics-e2].

### Step 2: Choose the unit of randomization: individuals or groups

**How:** J-PAL advises that the unit of randomization should at minimum be the unit at which the treatment is delivered, and ideally one that also minimizes spillovers and evaluation-driven effects (people changing their behavior because they are being evaluated)[^jpal2023randomization-e1]. Duflo and colleagues list several trade-offs: the larger the groups, the larger the total sample you need; but when the treatment group can affect the comparison group, randomization has to happen at a level that contains that effect[^duflo2007toolkit-e15]; and when you randomize by village, monitoring "which villages complied" is much easier than monitoring every individual[^duflo2007toolkit-e16].

**Why:** the higher the level of randomization, the smaller the effective sample size, and the more observations you need for the same power[^jpal2023randomization-e2].

**Where people go wrong:** assigning the intervention by group and measuring outcomes for individuals (this is cluster randomization[^egapclusterrandomization-e1]), but then computing standard errors in the analysis as if individuals had been randomized (see Step 8).

### Step 3: Do the power calculations

**Statistical power** is the probability that your experiment yields a significant result if the intervention really has an effect of a given size. The **minimum detectable effect** is the size below which an effect, even if it exists, may not be distinguishable[^jpal2021power-e1]. For the steps of a sample size calculation you can also refer to [calculating the sample size](randomized_controlled_trial.md#step-3-calculate-the-sample-size) on the [Randomized controlled trials](randomized_controlled_trial.md) page; below we cover only what needs extra attention in field experiments.

**How:**

1. **Start with a rough feasibility check**, then refine with new data once it passes (J-PAL's advice)[^jpal2021power-e7].
2. **Decide what effect size you need to detect.** For policy evaluation, Duflo and colleagues suggest setting it at the smallest effect that would still make the program cost-effective at scale[^duflo2007toolkit-e11]. J-PAL warns that effects reported in published studies of similar programs are usually optimistic[^jpal2021power-e5]; and the common "small, medium, large effect" rules of thumb come from social psychology lab experiments with undergraduates and have since been argued to be unrealistic in real-world settings for some sectors and regions[^jpal2021power-e6].
3. **Find the parameters.** For the variance of the outcome, the intra-cluster correlation and so on, use existing data where possible, ideally from the same country or region[^duflo2007toolkit-e10].
4. **Account for clustering, noncompliance, and attrition.** Attrition shrinks the actual sample and lowers power[^jpal2021power-e3].
   - **Clustering**: the **intra-cluster correlation coefficient** measures how similar people in the same cluster are. In J-PAL's example, an intra-cluster correlation of only 0.07 doubles the standard error, so you need four times the sample[^jpal2021power-e4]. Adding more clusters improves precision more than adding people to existing clusters[^duflo2007toolkit-e9], but usually costs more[^jpal2021power-e8].
   - **Noncompliance** (people assigned to treatment who don't take it up, or the reverse): in J-PAL's example, when only half the treatment group takes up the program and no one in the comparison group does, you need four times the sample you would need with full compliance[^jpal2021power-e2].
5. **Set a target power.** EGAP's guide says many disciplines aim for 0.80; this is only a benchmark, and you should think about whether an expected 80% chance of success is acceptable to you[^egappower-e3].
6. **Vary the assumptions and see how the result changes**, so you know how much your conclusions depend on them[^egappower-e2]. For complex designs you can simulate: have the computer run the experiment thousands of times and count how often the result is significant[^egappower-e4].

**Why:** with an underpowered study, a null result cannot tell you whether there is truly no effect or you just couldn't detect it; and a positive result is likely to overstate the effect[^egappower-e1]. J-PAL's ethics guidance also points out that a study so poorly designed that its results cannot be trusted puts the burden of participation on people without producing any knowledge in return[^jpal2022ethics-e4].

> **Where sources disagree: is an underpowered study still worth doing?** Some argue that a study that cannot reach a conclusion is not worth doing; Duflo and colleagues point out that the first few studies bring the largest gains in precision, and several low-powered studies can be combined in a meta-analysis[^duflo2007toolkit-e12]. In practice: first compute the minimum detectable effect honestly, then judge with your advisor and partner whether an effect of that size matters for policy; if you go ahead, report the power in the paper.

### Step 4: Baseline survey, stratification, and random assignment

**Whether to run a baseline survey.** By Duflo and colleagues' analysis, randomization in principle makes a baseline survey unnecessary; when the intervention is expensive and the survey cheap, a baseline saves money, but when the intervention is cheap and the survey expensive, a larger sample with no baseline may be better value[^duflo2007toolkit-e17]. A baseline also lets you check that randomization was done correctly, and lets you pilot your data collection[^duflo2007toolkit-e18]. Don't wait until after the intervention to ask people to recall "how things were before": the program may affect what they remember[^duflo2007toolkit-e19].

**Stratified randomization.** Randomization guarantees that the groups are similar "on average"; **stratified randomization** (first dividing the sample into strata by important characteristics, then randomizing within each stratum) guarantees that the particular groups you draw this time really are similar on those characteristics[^duflo2007toolkit-e14]. J-PAL suggests stratifying on variables that are related to the outcome, or by which you want to compare effects across subgroups[^jpal2023randomization-e4]; decide beforehand which variables must never be imbalanced, and stratify on them directly[^jpal2023randomization-e8].

**Make the randomization reproducible.** Do it in statistical software with a random seed set[^jpal2023randomization-e5], and save the code and the assignment. Don't over-read balance tests: testing at the 5% level, about 5% of variables will differ significantly by pure chance; there is no clear rule for how many is too many[^jpal2023randomization-e6]. Specify the balance tests as closely as possible to the final analysis[^jpal2023randomization-e9].

### Step 5: Register and write a pre-analysis plan

For registration requirements and how to write a pre-analysis plan (an analysis plan written before you see the data), see the [economics and business field overview](../07_fields/economics/README.md#field-experiments-must-be-registered-pre-analysis-plans) and the [political science field overview](../07_fields/political-science/README.md#pre-analysis-plans). The key points: AEA journals require field experiments to be registered in the American Economic Association's registry for randomized controlled trials (the AEA RCT Registry) before submission, and encourage early registration[^aea2026rct-e1]; only trials registered before the intervention begins are marked as "pre-registered"[^aea2026rct-e5]. For other journals and funders, follow their own requirements. A field experiment's plan should spell out a few more things:

- **Which variables you will control for** should be fixed in advance[^duflo2007toolkit-e13], and **which subgroups you will analyze separately** should also be stated in advance[^duflo2007toolkit-e34].
- **How you will handle attrition and noncompliance.** These two are the most often left out: Ofosu and Posner examined 195 plans registered on the EGAP and AEA registries between 2011 and 2016[^ofosu2023preanalysis-e1], and only 25% said how they would handle missing values or attrition, and 13% how they would handle noncompliance[^ofosu2023preanalysis-e8].
- **Analyses not in the plan are allowed, but label them** as "not pre-specified" and explain why you added them (Ofosu and Posner's position)[^ofosu2023preanalysis-e14].

### Step 6: Monitor implementation closely

**How** (the following are recommendations from J-PAL's implementation monitoring guide):

- **Pick a few key indicators**, focused on the parts of the program the partner controls[^jpal2021implementation-e2].
- **Check the lists**: compare the list of people who actually received the intervention against the list randomly assigned to treatment, to monitor compliance[^jpal2021implementation-e3].
- **Watch for evaluation-driven effects**: respondents may change their behavior because of the evaluation rather than the intervention[^jpal2021implementation-e4]; unannounced field visits are the most useful, but can also trigger such effects (Hawthorne effects)[^jpal2021implementation-e7].
- **Record every deviation** for later analysis and reporting[^jpal2021implementation-e5]; also collect data on the cost of the intervention and on context, to help judge whether it can be scaled up[^jpal2021implementation-e6].

**Why:** if the program was not implemented as designed, you may wrongly conclude that it has no effect[^jpal2021implementation-e1].

**Where people go wrong:** collecting outcomes differently for the two groups, for example administrative records for one and a survey for the other; any difference may be due only to the different measurement methods[^duflo2007toolkit-e20].

### Step 7: Keep attrition under control

Random attrition only lowers power; attrition related to the treatment biases the estimate[^duflo2007toolkit-e28]. Even if the two groups have similar attrition rates, different kinds of people may be dropping out[^duflo2007toolkit-e29]. Attrition is hard to fix afterwards, so control it while collecting data: at baseline, collect information that will help you find people later, such as the names of neighbors and relatives[^duflo2007toolkit-e30]. As the first step of the analysis, report the attrition rate in each group, and use baseline data to compare those who dropped out with those who stayed[^duflo2007toolkit-e31].

### Step 8: Analysis: compare by assigned group, and get the standard errors right

**Intention-to-treat effect**: compare the two groups in full, according to the original random assignment, regardless of whether people actually received the intervention; you must not drop or split the sample by any behavior that assignment might have affected[^duflo2007toolkit-e21]. Duflo and colleagues point out that in many cases this is itself the quantity you want[^duflo2007toolkit-e22].

**The effect on those who actually took it up.** If you want to know how much the intervention affected "those who actually received it", you can use random assignment as an instrumental variable (using only the variation that random assignment creates to estimate the effect): under certain assumptions, this gives the **local average treatment effect**, the effect for "those whose take-up was changed by their assignment" (the compliers)[^duflo2007toolkit-e23][^egaplate-e1]. If no one in the comparison group takes it up, this equals the effect on those in the treatment group who actually took it up[^duflo2007toolkit-e24]. Note:

- It represents only the compliers, not the whole sample[^egaplate-e3];
- It requires that outcomes respond only to the intervention actually received, not to "which group you were assigned to"[^egaplate-e2]. When people in the treatment group who did not directly receive the intervention also benefit (for example, the weakest students in a class are pulled out for remedial lessons, so the remaining students get a smaller class), this calculation is not appropriate[^duflo2007toolkit-e25];
- If the intention-to-treat effect is zero, it is zero too[^egaplate-e4], so report the intention-to-treat effect first.

**Standard errors with clusters.** Ignoring cluster assignment makes standard errors too small[^egapclusterrandomization-e3]: in EGAP's example, with 200 observations from 10 clusters and an intra-cluster correlation of 0.5, the effective sample size is only about 19[^egapclusterrandomization-e2]. Simulations cited by Duflo and colleagues show that with fewer than 50 clusters, the usual cluster-robust standard errors tend to wrongly reject the null of no effect; in that case you can use randomization inference[^duflo2007toolkit-e32].

**Multiple outcomes.** Duflo and colleagues argue that all the outcome variables you collected should be reported, significant or not[^duflo2007toolkit-e33]. For general problems with statistical tests, see [Report how big and how certain, not just the p-value](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value) in Part 2.

### Step 9: Think through spillovers

A **spillover** is when a unit is affected by whether others received the intervention[^egapspillovers-e1]. For example, if you monitor elections at some polling stations, fraud may move to nearby stations; lowering one firm's costs may change the prices other firms face[^egapspillovers-e2]. EGAP's spillover guide notes that most experimental analyses assume there are no spillovers[^egapspillovers-e5]; positive spillovers raise the comparison group's mean and bias the estimate downward, and negative spillovers do the opposite[^egapspillovers-e3]. If you want to know what would happen if the program were rolled out to everyone, ignoring spillovers can greatly overstate or understate the total effect[^egapspillovers-e4].

**How:**

- **Avoid them**: leave buffer zones between units[^egapspillovers-e6], or randomize at a level that contains the spillovers. If spillovers do not cross clusters, randomizing by cluster lets you estimate the total effect, but not separate the direct effect from the spillover effect[^duflo2007toolkit-e26].
- **Measure them**: randomly vary the share of each cluster that receives the intervention, then measure recipients and non-recipients within each cluster separately[^jpal2023randomization-e3][^duflo2007toolkit-e27].
- **Fix your assumption about how far spillovers reach in advance**, so you don't keep adjusting it after the fact until something comes out significant[^egapspillovers-e7]; but acknowledge that the assumption itself may be wrong[^egapspillovers-e8].

### Step 10: Handle the ethics of working in real communities

For general informed consent and risk assessment, see [When research involves people, protect them first](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) under Throughout the project; for the debate over the ethics of election experiments, see the [political science field overview](../07_fields/political-science/README.md#ethics-doing-research-in-real-political-settings). Field experiments call for thinking about a few more things:

- **Approval is not the end of it.** J-PAL's ethics guidance says that review by an ethics committee cannot replace researchers' own responsibility: ask yourself, and ask the people in the community, whether they accept the design[^jpal2022ethics-e1]; seek input from local partners, communities, and governments during design and implementation[^jpal2022ethics-e3].
- **Partner approval does not take away your responsibility.** The 2020 principles on human subjects research of the American Political Science Association (APSA) say that working with a third party does not transfer all ethical responsibility to that party[^apsa2020humansubjects-e14]; approval from authorities such as election bodies does not relieve researchers of all ethical considerations either[^apsa2020humansubjects-e15].
- **Think about people beyond the participants.** McDermott and Hatemi propose adding a principle of "respect for societies", considering the intervention's effects on society as a whole[^mcdermott2020ethics-e4].
- **Justice.** J-PAL points out that a phase-in means no one is permanently excluded[^jpal2022ethics-e6]; compensation for participants should be neither so low that it is exploitative nor so high that it affects their judgment of the risks[^jpal2022ethics-e8].
- **Protect the data.** J-PAL calls data breaches the most common risk in social science research[^jpal2022ethics-e7]. It advises collecting only the sensitive data the research strictly needs[^jpal2023datasecurity-e2] and separating personally identifying information from the rest of the data as soon as possible[^jpal2023datasecurity-e3]; data that look anonymous can still be re-identified[^jpal2023datasecurity-e1]. Partners and enumerators also need to understand these procedures[^jpal2023datasecurity-e4].
- **Report in the paper** the possible effects on participants and on broader political processes, and whether, and from whom, consent was sought (an American Political Science Association requirement)[^apsa2020humansubjects-e16].

---

## 3. Checklist

**Must do**

- [ ] The unit of randomization is at least the unit at which the intervention is delivered[^jpal2023randomization-e1]; with cluster randomization, both the power calculation and the standard errors account for clustering[^jpal2021power-e4][^egapclusterrandomization-e3]
- [ ] Field experiments submitted to AEA journals are registered on the American Economic Association's registry[^aea2026rct-e1]
- [ ] The main analysis compares groups as originally randomized, without dropping anyone based on behavior affected by assignment[^duflo2007toolkit-e21]
- [ ] Attrition rates for each group are reported, and those who dropped out are compared with those who stayed[^duflo2007toolkit-e31]
- [ ] Outcomes are measured the same way in both groups[^duflo2007toolkit-e20]
- [ ] Analyses not in the plan are clearly labeled, with an explanation of why they were added[^ofosu2023preanalysis-e14]

**Better practice**

- [ ] Registered before the intervention began[^aea2026rct-e5]; the plan covers control variables[^duflo2007toolkit-e13] and how attrition and noncompliance will be handled[^ofosu2023preanalysis-e8]
- [ ] Power calculations use existing data from the same region and try different assumptions[^duflo2007toolkit-e10][^egappower-e2]
- [ ] Randomization stratified on important variables, with reproducible code and seed[^jpal2023randomization-e8][^jpal2023randomization-e5]
- [ ] Implementation monitoring records, plus cost and context data[^jpal2021implementation-e5][^jpal2021implementation-e6]
- [ ] Where spillovers may matter, the design measures them explicitly[^jpal2023randomization-e3]

**Fine to skip; not a flaw**

- No baseline survey: randomization in principle makes a baseline unnecessary, and when the intervention is cheap and surveys are expensive, skipping it may be better value[^duflo2007toolkit-e17].
- Not reporting "the effect on those who actually took it up": in many cases the intention-to-treat effect is itself the quantity you want[^duflo2007toolkit-e22].
- One variable in the balance table differs significantly: about 5% of variables will differ significantly by pure chance[^jpal2023randomization-e6]; balance tests are most useful only when there is reason to suspect the randomization was not done correctly[^jpal2023randomization-e7].

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Randomizing individuals when the intervention spreads among neighbors or classmates | The treatment group affects the comparison group and the estimate is biased; randomize at a level that contains the spillovers[^duflo2007toolkit-e15] |
| Taking effect sizes straight from published studies for the power calculation | Published effects are usually optimistic[^jpal2021power-e5], so the experiment may be underpowered |
| Comparing only "those who actually received the intervention" with the comparison group | Take-up is affected by assignment, so you can't split the sample on it[^duflo2007toolkit-e21] |
| Dividing the intention-to-treat effect by the take-up rate while ignoring that non-recipients were also affected | This violates the assumption that outcomes respond only to the intervention actually received, so the calculation is not appropriate[^duflo2007toolkit-e25][^egaplate-e2] |
| Randomizing clusters but computing standard errors as if for individuals | Standard errors are too small, overstating how much information the experiment provides[^egapclusterrandomization-e3] |
| Controlling for variables affected by the intervention | This absorbs part of the effect and biases the estimate[^duflo2007toolkit-e13] |
| Asking people after the intervention to recall "how things were before" instead of running a baseline | The program may affect their recall[^duflo2007toolkit-e19] |
| Not monitoring implementation, then calling the program "ineffective" when the result is zero | The program may simply not have been implemented as designed[^jpal2021implementation-e1] |

## 5. Further reading

- **Duflo, Glennerster, and Kremer 2007, Using Randomization in Development Economics Research: A Toolkit** (a National Bureau of Economic Research technical working paper, free to download from its website; later included in Volume 4 of the *Handbook of Development Economics*): covers everything from partners and ways to randomize to power, attrition, spillovers, and inference. Read it in full before you start designing.
- **J-PAL research resources** (power calculations, randomization, implementation monitoring, ethics, data security): free web pages from the J-PAL research network; look up each one when you reach that step.
- **EGAP methods guides** (power, cluster randomization, spillovers, local average treatment effect, and "10 Conversations that Implementers and Evaluators Need to Have"): free web pages from the EGAP research network, good for looking things up by question; "10 Conversations" is written mainly for implementers and is worth reading before your first meeting with a partner.
- **The American Political Science Association's 2020 principles on human subjects research** and **McDermott and Hatemi 2020**: read these before running experiments that involve elections or political processes.

[^duflo2007toolkit-e1]: Duflo, Glennerster & Kremer 2007, §3. [Evidence](../../sources/notes/duflo2007toolkit.md#e1)
[^duflo2007toolkit-e2]: Duflo, Glennerster & Kremer 2007, §3.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e2)
[^duflo2007toolkit-e3]: Duflo, Glennerster & Kremer 2007, §3.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e3)
[^duflo2007toolkit-e4]: Duflo, Glennerster & Kremer 2007, §3.3.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e4)
[^duflo2007toolkit-e5]: Duflo, Glennerster & Kremer 2007, §3.3.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e5)
[^duflo2007toolkit-e6]: Duflo, Glennerster & Kremer 2007, §3.3.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e6)
[^duflo2007toolkit-e7]: Duflo, Glennerster & Kremer 2007, §3.3.3. [Evidence](../../sources/notes/duflo2007toolkit.md#e7)
[^duflo2007toolkit-e8]: Duflo, Glennerster & Kremer 2007, §3.3.4. [Evidence](../../sources/notes/duflo2007toolkit.md#e8)
[^duflo2007toolkit-e9]: Duflo, Glennerster & Kremer 2007, §4.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e9)
[^duflo2007toolkit-e10]: Duflo, Glennerster & Kremer 2007, §4.6. [Evidence](../../sources/notes/duflo2007toolkit.md#e10)
[^duflo2007toolkit-e11]: Duflo, Glennerster & Kremer 2007, §4.6. [Evidence](../../sources/notes/duflo2007toolkit.md#e11)
[^duflo2007toolkit-e12]: Duflo, Glennerster & Kremer 2007, §4.6. [Evidence](../../sources/notes/duflo2007toolkit.md#e12)
[^duflo2007toolkit-e13]: Duflo, Glennerster & Kremer 2007, §4.4. [Evidence](../../sources/notes/duflo2007toolkit.md#e13)
[^duflo2007toolkit-e14]: Duflo, Glennerster & Kremer 2007, §4.5. [Evidence](../../sources/notes/duflo2007toolkit.md#e14)
[^duflo2007toolkit-e15]: Duflo, Glennerster & Kremer 2007, §5.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e15)
[^duflo2007toolkit-e16]: Duflo, Glennerster & Kremer 2007, §5.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e16)
[^duflo2007toolkit-e17]: Duflo, Glennerster & Kremer 2007, §5.3.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e17)
[^duflo2007toolkit-e18]: Duflo, Glennerster & Kremer 2007, §5.3.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e18)
[^duflo2007toolkit-e19]: Duflo, Glennerster & Kremer 2007, §5.3.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e19)
[^duflo2007toolkit-e20]: Duflo, Glennerster & Kremer 2007, §5.3.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e20)
[^duflo2007toolkit-e21]: Duflo, Glennerster & Kremer 2007, §6.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e21)
[^duflo2007toolkit-e22]: Duflo, Glennerster & Kremer 2007, §6.2.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e22)
[^duflo2007toolkit-e23]: Duflo, Glennerster & Kremer 2007, §6.2.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e23)
[^duflo2007toolkit-e24]: Duflo, Glennerster & Kremer 2007, §6.2.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e24)
[^duflo2007toolkit-e25]: Duflo, Glennerster & Kremer 2007, §6.2.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e25)
[^duflo2007toolkit-e26]: Duflo, Glennerster & Kremer 2007, §6.3. [Evidence](../../sources/notes/duflo2007toolkit.md#e26)
[^duflo2007toolkit-e27]: Duflo, Glennerster & Kremer 2007, §6.3. [Evidence](../../sources/notes/duflo2007toolkit.md#e27)
[^duflo2007toolkit-e28]: Duflo, Glennerster & Kremer 2007, §6.4. [Evidence](../../sources/notes/duflo2007toolkit.md#e28)
[^duflo2007toolkit-e29]: Duflo, Glennerster & Kremer 2007, §6.4. [Evidence](../../sources/notes/duflo2007toolkit.md#e29)
[^duflo2007toolkit-e30]: Duflo, Glennerster & Kremer 2007, §6.4. [Evidence](../../sources/notes/duflo2007toolkit.md#e30)
[^duflo2007toolkit-e31]: Duflo, Glennerster & Kremer 2007, §6.4. [Evidence](../../sources/notes/duflo2007toolkit.md#e31)
[^duflo2007toolkit-e32]: Duflo, Glennerster & Kremer 2007, §7.1. [Evidence](../../sources/notes/duflo2007toolkit.md#e32)
[^duflo2007toolkit-e33]: Duflo, Glennerster & Kremer 2007, §7.2. [Evidence](../../sources/notes/duflo2007toolkit.md#e33)
[^duflo2007toolkit-e34]: Duflo, Glennerster & Kremer 2007, §7.3. [Evidence](../../sources/notes/duflo2007toolkit.md#e34)
[^jpal2021power-e1]: J-PAL, Power calculations, Essentials. [Evidence](../../sources/notes/jpal2021power.md#e1)
[^jpal2021power-e2]: J-PAL, Power calculations, Introduction. [Evidence](../../sources/notes/jpal2021power.md#e2)
[^jpal2021power-e3]: J-PAL, Power calculations, Introduction. [Evidence](../../sources/notes/jpal2021power.md#e3)
[^jpal2021power-e4]: J-PAL, Power calculations, Clustered designs. [Evidence](../../sources/notes/jpal2021power.md#e4)
[^jpal2021power-e5]: J-PAL, Power calculations, Practical tips. [Evidence](../../sources/notes/jpal2021power.md#e5)
[^jpal2021power-e6]: J-PAL, Power calculations, Practical tips. [Evidence](../../sources/notes/jpal2021power.md#e6)
[^jpal2021power-e7]: J-PAL, Power calculations, Practical tips. [Evidence](../../sources/notes/jpal2021power.md#e7)
[^jpal2021power-e8]: J-PAL, Power calculations, Practical tips. [Evidence](../../sources/notes/jpal2021power.md#e8)
[^jpal2023randomization-e1]: J-PAL, Randomization, Choosing the unit of randomization. [Evidence](../../sources/notes/jpal2023randomization.md#e1)
[^jpal2023randomization-e2]: J-PAL, Randomization, Choosing the unit of randomization. [Evidence](../../sources/notes/jpal2023randomization.md#e2)
[^jpal2023randomization-e3]: J-PAL, Randomization, Randomization designs to estimate spillover effects. [Evidence](../../sources/notes/jpal2023randomization.md#e3)
[^jpal2023randomization-e4]: J-PAL, Randomization, Stratified randomization. [Evidence](../../sources/notes/jpal2023randomization.md#e4)
[^jpal2023randomization-e5]: J-PAL, Randomization, Randomization methods. [Evidence](../../sources/notes/jpal2023randomization.md#e5)
[^jpal2023randomization-e6]: J-PAL, Randomization, Balance tests. [Evidence](../../sources/notes/jpal2023randomization.md#e6)
[^jpal2023randomization-e7]: J-PAL, Randomization, Balance tests. [Evidence](../../sources/notes/jpal2023randomization.md#e7)
[^jpal2023randomization-e8]: J-PAL, Randomization, Solutions to imbalance. [Evidence](../../sources/notes/jpal2023randomization.md#e8)
[^jpal2023randomization-e9]: J-PAL, Randomization, Balance tests. [Evidence](../../sources/notes/jpal2023randomization.md#e9)
[^jpal2022ethics-e1]: J-PAL, Ethical conduct of randomized evaluations, Introduction. [Evidence](../../sources/notes/jpal2022ethics.md#e1)
[^jpal2022ethics-e2]: J-PAL, Ethical conduct of randomized evaluations, Introduction. [Evidence](../../sources/notes/jpal2022ethics.md#e2)
[^jpal2022ethics-e3]: J-PAL, Ethical conduct of randomized evaluations, How research ethics contribute to research quality. [Evidence](../../sources/notes/jpal2022ethics.md#e3)
[^jpal2022ethics-e4]: J-PAL, Ethical conduct of randomized evaluations, Beneficence principle. [Evidence](../../sources/notes/jpal2022ethics.md#e4)
[^jpal2022ethics-e5]: J-PAL, Ethical conduct of randomized evaluations, Implementing the "do not harm" principle. [Evidence](../../sources/notes/jpal2022ethics.md#e5)
[^jpal2022ethics-e6]: J-PAL, Ethical conduct of randomized evaluations, Implementing the justice principle. [Evidence](../../sources/notes/jpal2022ethics.md#e6)
[^jpal2022ethics-e7]: J-PAL, Ethical conduct of randomized evaluations, Implementing the "minimal risk" principle. [Evidence](../../sources/notes/jpal2022ethics.md#e7)
[^jpal2022ethics-e8]: J-PAL, Ethical conduct of randomized evaluations, Implementing respect for persons. [Evidence](../../sources/notes/jpal2022ethics.md#e8)
[^jpal2021implementation-e1]: J-PAL, Implementation monitoring, Introduction. [Evidence](../../sources/notes/jpal2021implementation.md#e1)
[^jpal2021implementation-e2]: J-PAL, Implementation monitoring, Selecting indicators. [Evidence](../../sources/notes/jpal2021implementation.md#e2)
[^jpal2021implementation-e3]: J-PAL, Implementation monitoring, Indicators to monitor. [Evidence](../../sources/notes/jpal2021implementation.md#e3)
[^jpal2021implementation-e4]: J-PAL, Implementation monitoring, Indicators to monitor. [Evidence](../../sources/notes/jpal2021implementation.md#e4)
[^jpal2021implementation-e5]: J-PAL, Implementation monitoring, Indicators to monitor. [Evidence](../../sources/notes/jpal2021implementation.md#e5)
[^jpal2021implementation-e6]: J-PAL, Implementation monitoring, Indicators to monitor. [Evidence](../../sources/notes/jpal2021implementation.md#e6)
[^jpal2021implementation-e7]: J-PAL, Implementation monitoring, Monitoring methods. [Evidence](../../sources/notes/jpal2021implementation.md#e7)
[^jpal2023datasecurity-e1]: J-PAL, Data security procedures for researchers, Data security overview. [Evidence](../../sources/notes/jpal2023datasecurity.md#e1)
[^jpal2023datasecurity-e2]: J-PAL, Data security procedures for researchers, Minimizing data security threats. [Evidence](../../sources/notes/jpal2023datasecurity.md#e2)
[^jpal2023datasecurity-e3]: J-PAL, Data security procedures for researchers, De-identifying data. [Evidence](../../sources/notes/jpal2023datasecurity.md#e3)
[^jpal2023datasecurity-e4]: J-PAL, Data security procedures for researchers, Data security overview. [Evidence](../../sources/notes/jpal2023datasecurity.md#e4)
[^egappower-e1]: Evidence in Governance and Politics (EGAP) methods guide, Statistical Power, §2. [Evidence](../../sources/notes/egappower.md#e1)
[^egappower-e2]: Evidence in Governance and Politics (EGAP) methods guide, Statistical Power, §5. [Evidence](../../sources/notes/egappower.md#e2)
[^egappower-e3]: Evidence in Governance and Politics (EGAP) methods guide, Statistical Power, §2. [Evidence](../../sources/notes/egappower.md#e3)
[^egappower-e4]: Evidence in Governance and Politics (EGAP) methods guide, Statistical Power, §6. [Evidence](../../sources/notes/egappower.md#e4)
[^egapspillovers-e1]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §1. [Evidence](../../sources/notes/egapspillovers.md#e1)
[^egapspillovers-e2]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §1. [Evidence](../../sources/notes/egapspillovers.md#e2)
[^egapspillovers-e3]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §2. [Evidence](../../sources/notes/egapspillovers.md#e3)
[^egapspillovers-e4]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §2. [Evidence](../../sources/notes/egapspillovers.md#e4)
[^egapspillovers-e5]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §3. [Evidence](../../sources/notes/egapspillovers.md#e5)
[^egapspillovers-e6]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §8. [Evidence](../../sources/notes/egapspillovers.md#e6)
[^egapspillovers-e7]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §9. [Evidence](../../sources/notes/egapspillovers.md#e7)
[^egapspillovers-e8]: Evidence in Governance and Politics (EGAP) methods guide, Spillovers, §9. [Evidence](../../sources/notes/egapspillovers.md#e8)
[^egapclusterrandomization-e1]: Evidence in Governance and Politics (EGAP) methods guide, Cluster Randomization, §1. [Evidence](../../sources/notes/egapclusterrandomization.md#e1)
[^egapclusterrandomization-e2]: Evidence in Governance and Politics (EGAP) methods guide, Cluster Randomization, §2. [Evidence](../../sources/notes/egapclusterrandomization.md#e2)
[^egapclusterrandomization-e3]: Evidence in Governance and Politics (EGAP) methods guide, Cluster Randomization, §3. [Evidence](../../sources/notes/egapclusterrandomization.md#e3)
[^egaplate-e1]: Evidence in Governance and Politics (EGAP) methods guide, Local Average Treatment Effect, §1. [Evidence](../../sources/notes/egaplate.md#e1)
[^egaplate-e2]: Evidence in Governance and Politics (EGAP) methods guide, Local Average Treatment Effect, §2. [Evidence](../../sources/notes/egaplate.md#e2)
[^egaplate-e3]: Evidence in Governance and Politics (EGAP) methods guide, Local Average Treatment Effect, §6. [Evidence](../../sources/notes/egaplate.md#e3)
[^egaplate-e4]: Evidence in Governance and Politics (EGAP) methods guide, Local Average Treatment Effect, §5. [Evidence](../../sources/notes/egaplate.md#e4)
[^egapevaluationconversations-e1]: Evidence in Governance and Politics (EGAP) methods guide, 10 Conversations, §1. [Evidence](../../sources/notes/egapevaluationconversations.md#e1)
[^egapevaluationconversations-e2]: Evidence in Governance and Politics (EGAP) methods guide, 10 Conversations, §4. [Evidence](../../sources/notes/egapevaluationconversations.md#e2)
[^egapevaluationconversations-e3]: Evidence in Governance and Politics (EGAP) methods guide, 10 Conversations, §8. [Evidence](../../sources/notes/egapevaluationconversations.md#e3)
[^egapevaluationconversations-e4]: Evidence in Governance and Politics (EGAP) methods guide, 10 Conversations, §9. [Evidence](../../sources/notes/egapevaluationconversations.md#e4)
[^aea2026rct-e1]: About the AEA RCT Registry. [Evidence](../../sources/notes/aea2026rct.md#e1)
[^aea2026rct-e5]: AEA RCT Registry registration guidelines. [Evidence](../../sources/notes/aea2026rct.md#e5)
[^ofosu2023preanalysis-e1]: Ofosu & Posner 2023, Abstract. [Evidence](../../sources/notes/ofosu2023preanalysis.md#e1)
[^ofosu2023preanalysis-e8]: Ofosu & Posner 2023, Do PAPs Reduce the Scope for Fishing? [Evidence](../../sources/notes/ofosu2023preanalysis.md#e8)
[^ofosu2023preanalysis-e14]: Ofosu & Posner 2023, Objections to PAPs: Limit Flexibility and Scope for New Discoveries. [Evidence](../../sources/notes/ofosu2023preanalysis.md#e14)
[^apsa2020humansubjects-e14]: American Political Science Association 2020, Guidance (Impact). [Evidence](../../sources/notes/apsa2020humansubjects.md#e14)
[^apsa2020humansubjects-e15]: American Political Science Association 2020, Guidance (Impact). [Evidence](../../sources/notes/apsa2020humansubjects.md#e15)
[^apsa2020humansubjects-e16]: American Political Science Association 2020, Impact, 10d. [Evidence](../../sources/notes/apsa2020humansubjects.md#e16)
[^mcdermott2020ethics-e4]: McDermott & Hatemi 2020, Respect for Societies. [Evidence](../../sources/notes/mcdermott2020ethics.md#e4)
