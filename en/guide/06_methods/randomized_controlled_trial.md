# Randomized controlled trials

This page covers how to design and run a **randomized controlled trial**: you randomly assign participants to different interventions and compare their outcomes. The rules on ethics approval, trial registration, authorship, conflicts of interest, and data sharing are already covered in the [clinical medicine field overview](../07_fields/clinical-medicine/README.md); here we only show where each of them comes into the trial. Observational studies (cohort, case-control, cross-sectional) are outside the scope of this page.

**Scope** `[Our analysis]`: This page was written for [Clinical medicine](../07_fields/clinical-medicine/README.md). Its sources are mainly the two reporting guidelines for clinical trials, CONSORT 2025 (Consolidated Standards of Reporting Trials) and SPIRIT 2025 (Standard Protocol Items: Recommendations for Interventional Trials), and their explanatory papers, the World Medical Association's Declaration of Helsinki, the recommendations of the International Committee of Medical Journal Editors (ICMJE), and the World Health Organization's guidance on registration. So every "must" and "should" below is what clinical medicine requires of a trial. The field overviews for [Health sciences](../07_fields/health-sciences/README.md), [Basic medical sciences](../07_fields/basic-medicine/README.md), [Animal and veterinary science](../07_fields/animal-veterinary-science/README.md), and [Medical engineering](../07_fields/medical-engineering/README.md) also point here. If you randomize in another field, check your own field's conventions first. If you randomize inside a real program run with a government or company, see [Field experiments](field_experiment.md); if you randomize people who come to a lab, see [Controlled experiments](controlled_experiment.md).

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md).


**After reading this page, you should be able to:**
- use PICO (population, intervention, comparator, outcome) to turn a clinical question into one a trial can answer, and choose the primary outcome;
- say which assumptions a sample size calculation has to state;
- tell apart the random sequence, allocation concealment, and blinding, and say which bias each one protects against;
- know that the protocol, ethics approval, and registration must all be done before the first participant is enrolled;
- analyze the data on the intention-to-treat principle and write the paper following CONSORT 2025.

---

## 1. What kind of study this is, and when to use it

A randomized controlled trial answers a **causal question**: "For this kind of patient, does intervention A improve outcome O more than comparator C?" When randomization is done properly, it removes selection bias at the point of allocation and balances both known and unknown prognostic factors across the groups[^hopewell2025consortee-e1]. That is why a randomized trial that is properly designed, conducted, analyzed, and reported is generally considered the highest quality evidence for evaluating healthcare interventions[^hopewell2025consort-e2]. The key word is "properly"; every step below is there to protect it `[Our analysis]`.

**How it differs from a cohort study** (for how to do observational studies, see [Observational epidemiology](observational_epidemiology.md)):

| | Randomized controlled trial | Cohort study |
|---|---|---|
| Who decides which intervention a participant gets | The investigator, by random allocation | Not assigned by the investigator[^icmje2026recommendations-e21] |
| Registration in advance | Required before the first participant is recruited (see Step 7) | Encouraged but not required by the International Committee of Medical Journal Editors (ICMJE)[^icmje2026recommendations-e21] |
| Reporting guideline | CONSORT 2025 (see Step 10) | STROBE (Strengthening the Reporting of Observational Studies in Epidemiology); see the [clinical medicine field overview](../07_fields/clinical-medicine/README.md#reporting-guidelines-pick-the-checklist-for-your-study-type) |

**Compared with a controlled experiment.** The logic is the same: you actively change one factor, randomize, and compare outcomes. Within-subjects designs, task design, and pilot studies, covered in [Controlled experiments](controlled_experiment.md), are not repeated here. What a clinical trial adds is what follows below: allocation concealment, blinding of several groups of people, registration before enrollment, independent data monitoring, and intention-to-treat analysis `[Our analysis]`.

**Types of design.** CONSORT 2025 applies to all randomized trials but focuses on the most common one, the two-group parallel design[^hopewell2025consort-e9]. The other main designs are multi-arm parallel-group, crossover, cluster, and factorial designs, and each has its own CONSORT extension[^hopewell2025consortee-e2]. This page uses the two-group parallel design as its example; if you use another design, find the matching extension first.

## 2. How to do it

Steps 1 to 6 are design decisions, and all of them go into the trial protocol in Step 7. Below we draw heavily on **CONSORT 2025** (the reporting guideline for randomized trial papers), **SPIRIT 2025** (the reporting guideline for trial protocols), and their explanatory papers. They do not themselves tell you how to design and run a trial, but the key issues they flag are very helpful for design[^hopewell2025consort-e10]. They are reporting guidelines, not regulations; the binding requirements on ethics and registration come from the Declaration of Helsinki, medical journals' requirements, and national rules `[Our analysis]`.

### Step 1: Pin down the question with PICO

**How:**
- Write out the four **PICO** elements: the patient population (Population), the experimental intervention (Intervention), the comparator (Comparator), and the outcome (Outcome)[^hopewell2025consortee-e3]. For example: "In patients over 65 admitted to hospital with community-acquired pneumonia (P), does a 5-day course (I) differ from a 10-day course (C) in clinical cure rate within 30 days (O)?" (our own example).
- **State the objective in neutral terms**, for example "to compare the effect of A and B on outcome X in patients with Y", without presuming which is better[^hopewell2025consortee-e4].
- **Say what you are trying to show**: that the experimental intervention is better (superiority), no worse than the comparator (non-inferiority), or about the same (equivalence)[^hopewell2025consortee-e5]. This choice affects the sample size and the analysis later on `[Our analysis]`.
- **Decide under what conditions you will test it**: there is a continuum from ideal conditions (explanatory trials) to routine clinical conditions (pragmatic trials)[^hopewell2025consortee-e6].
- **Take ethics into account when choosing the comparator**: the World Medical Association's Declaration of Helsinki requires that a new intervention, as a rule, be compared with the best proven intervention; a placebo or no intervention is acceptable as the comparator when no proven intervention exists (this is one of the exceptions)[^wma2024helsinki-e14].

**Where people go wrong**: P is too broad or too narrow, and I and C are not described in enough detail for someone to carry them out `[Our analysis]`. For the general approach, see the Part 2 chapter [Break the claim into research questions](../02_do-the-project/01_question-to-evidence.md#1-break-the-claim-into-research-questions).

### Step 2: Choose the outcomes and fix one primary outcome

**How:**
- **Fix one primary outcome**: the prespecified outcome that matters most to patients, clinicians, decision makers, and funders, and the one the sample size is calculated on[^hopewell2025consortee-e7]. Most trials have a single primary outcome; having several creates problems of interpretation from multiple comparisons[^hopewell2025consortee-e8].
- **For each outcome, specify four things**: the variable measured, the form of each participant's data (for example change from baseline), how it is summarized within each group (for example mean or proportion), and the time point used for analysis[^hopewell2025consortee-e9].
- **Check first whether a core outcome set exists**: an agreed set of outcomes that all clinical trials in a given area should at least measure and report[^hopewell2025consortee-e10]. Using it makes your results easier to compare with other trials `[Our analysis]`.
- **Plan how you will measure harms (adverse effects)**. A trial designed mainly to assess benefit may not have enough power to detect harms, but the paper should still say whether harm outcomes were considered at the planning stage[^hopewell2025consortee-e11].

**Why**: fixing the outcomes in advance is what stops you from picking outcomes after seeing the data. Outcomes in the registration or protocol often do not match those in the paper, and the changes often favor statistically significant results[^hopewell2025consortee-e12]. A study cited in the CONSORT explanatory paper compared the protocols and papers of 102 randomized trials: in 62% of the papers, at least one primary outcome had been changed, added, or dropped[^hopewell2025consortee-e13].

### Step 3: Calculate the sample size

**How:**
- Base the calculation on the primary outcome. The trial should be big enough that, if there really is a difference of a prespecified, clinically meaningful size, it has a high probability of detecting it; this probability is called **power** (the same "power" discussed in [Controlled experiments](controlled_experiment.md))[^hopewell2025consortee-e14].
- State every assumption: which primary outcome and time point it is based on, the statistical test, the alpha level (the type I error, i.e. the probability of a false positive) and whether it is two-sided, the power, and the target number per group[^hopewell2025consortee-e15].
- If you inflated the sample size to allow for loss to follow-up or nonadherence, give the details[^hopewell2025consortee-e16]. The protocol should also say how you will recruit enough participants[^chan2025spirit-e1].

**Why**: the smaller the difference you want to detect, the larger the sample you need, and the relationship is not linear: very small differences need very large samples[^hopewell2025consortee-e17]. So if you set an overly optimistic target difference, your sample will be too small `[Our analysis]`.

**Where people go wrong**: when the result is not significant, computing power from the trial's own results to explain it. This post hoc power calculation is of no value and may mislead readers[^hopewell2025consortee-e18].

### Step 4: Generate an unpredictable random sequence

**How:**
- Generate the allocation sequence with a table of random numbers or a computer random number generator, and describe the method in the paper[^hopewell2025consortee-e19].
- **Alternation, or allocation by hospital number or date of birth, is not random.** Do not call it "random", or even "quasi-random"[^hopewell2025consortee-e20].
- **Choose the type of randomization**: in trials of several hundred participants or more, simple randomization usually gives groups of similar size; in small trials of under about 200, some form of restricted randomization can help balance the groups[^hopewell2025consortee-e21]. Common restrictions are:
  - **Block randomization** (participants are taken in blocks of a fixed size, with equal numbers in each group within each block `[Our analysis]`): someone who knows the block size can guess some of the upcoming allocations; blinding the intervention, using larger blocks, and varying the block size at random all help[^hopewell2025consortee-e22]. SPIRIT 2025 recommends putting details such as block size in a separate document that is not available to the people who enroll participants or assign interventions[^chan2025spirit-e2].
  - **Stratified randomization**: multicenter trials often stratify by center; stratification only works if it is combined with a restriction such as blocking within strata[^hopewell2025consortee-e23].
- **Minimization**: the CONSORT explanatory paper calls it the only acceptable alternative to randomization[^hopewell2025consortee-e24]. It can give very good balance across groups on several prognostic factors (baseline characteristics that affect the outcome, such as sex and age), even in small samples; which group the next person goes to depends on how the people already enrolled are distributed on those factors[^altman2005treatment-e1]. Altman and Bland demonstrate it in a 2005 BMJ statistics note: the first person is allocated at random; for each new person after that, for each group you add up how many people already in that group share the new person's characteristic on each factor, and allocate the new person to the group with the smaller total, at random if the totals are equal[^altman2005treatment-e2][^altman2005treatment-e3]. Continuous variables (such as age) have to be grouped into categories first[^altman2005treatment-e2]. You can also add a random element: allocate to the group that reduces imbalance with a high probability (for example 80%), which gives slightly worse balance but makes allocation harder to predict[^altman2005treatment-e4]. Which factors to use and how much randomness to add are questions for a trial statistician `[Our analysis]`.

**Why**: successful randomization depends on two things: the sequence is unpredictable, and it is concealed from the investigators who enroll participants[^hopewell2025consortee-e25]. The second is the next step.

### Step 5: Conceal the allocation

**Allocation concealment** means that whoever enrolls participants does not know the next assignment while they are deciding whether to include someone and obtaining that person's informed consent[^hopewell2025consortee-e26].

**How:**
- **Prefer central or third-party allocation**, commonly through a pharmacy, a central computer, or a telephone randomization service[^hopewell2025consortee-e27].
- **If you use envelopes, be especially careful**: sequentially numbered, opaque, and sealed; they cannot be read when held up to the light, are opened in sequence, and have the participant's name and other details written on them before they are opened[^hopewell2025consortee-e28].
- **Separate the people**: those who generate the sequence and conceal it are completely separate from those who carry out the assignments[^hopewell2025consortee-e29].

**Why**: trials with inadequate or unclear allocation concealment produce larger estimates of treatment effect than trials with adequate concealment[^hopewell2025consortee-e30].

**Where people go wrong**: confusing allocation concealment with blinding. Allocation concealment prevents selection bias and protects the sequence before allocation; it can always be done. Blinding prevents ascertainment bias and protects information after allocation; it cannot always be done[^hopewell2025consortee-e31].

### Step 6: Blind where you can, and say who was blinded

**Blinding** (also called masking) means keeping the people in a trial who could be influenced from knowing which intervention each participant received[^hopewell2025consortee-e32].

**How:**
- **Go through each role in turn**: participants, care providers, data collectors, outcome assessors, and data analysts. Unblinded assessors may assess subjective outcomes differently between groups; unblinded analysts may introduce bias by choosing time points or outcomes, or by excluding patients[^hopewell2025consortee-e33].
- **When participants and care providers cannot be blinded, at least blind the assessors.** In surgical and similar trials the former is often impossible, but blinding data collectors and outcome assessors is often possible and is recommended[^hopewell2025consortee-e34].
- **State who was blinded and how**, for example with an identical-looking placebo, a sham intervention, or sham surgery[^hopewell2025consortee-e35]. Whether or not blinding was possible, state who was blinded[^hopewell2025consortee-e56].
- **Write the unblinding rules in advance**: under what circumstances unblinding is allowed, and how a given participant's allocation will be revealed[^chan2025spirit-e3]. Fixed codes (such as A = group 1) raise the risk of breaking the blind: unblinding one person may unblind several, or everyone[^hopewell2025consortee-e36].

**Where people go wrong**: writing only "double-blind". A survey of the authors of 200 randomized trials reported as "double-blind" found 18 different combinations of which groups were actually blinded; so state for each group of people whether they were blinded[^hopewell2025consortee-e37].

### Step 7: Before the first participant is enrolled: write the protocol, get ethics approval, register

**Write the protocol**: the protocol is the most important record of the planned methods and conduct of the trial[^chan2025spirit-e4]. Write it following SPIRIT 2025, which has 34 minimum items and a schedule diagram of enrollment, interventions, and assessments[^chan2025spirit-e5]. All the decisions from Steps 1 to 6 go into it, along with who will obtain informed consent and how[^chan2025spirit-e6]; under the Declaration of Helsinki, a clinical trial protocol must also describe the arrangements for after the trial ends[^wma2024helsinki-e15]. Finalize the protocol before any participant is allocated, and the full statistical analysis plan before the database is locked and analysis begins[^hopewell2025consortee-e38].

**Get ethics approval**: the full protocol must be submitted to a research ethics committee for approval before enrollment[^chan2025spirit-e7]. For the requirements on informed consent, see the [clinical medicine field overview](../07_fields/clinical-medicine/README.md#your-subjects-are-people-so-ethics-comes-first).

**Register**: the Declaration of Helsinki requires registration in a public database before the first participant is recruited[^wma2024helsinki-e9]; ICMJE recommends that medical journals require registration at or before the time the first patient consents to enrollment as a condition for considering publication[^icmje2026recommendations-e15]. On why ethics approval is not registration, why registering after the fact does not count, and why you include a data sharing plan when you register, see the clinical medicine field overview sections [Register before recruiting the first patient](../07_fields/clinical-medicine/README.md#register-before-you-enroll-the-first-patient) and [Data sharing statements](../07_fields/clinical-medicine/README.md#data-sharing-statements).

**Where to register**: according to the World Health Organization (WHO) International Clinical Trials Registry Platform, WHO itself is not a registry; you submit to any of the primary registries in the WHO registry network[^whotrialregistration-e1], and registering once in one primary registry or one ICMJE-approved registry is enough[^whotrialregistration-e2]. Countries differ in their regulatory, legal, and ethical requirements for clinical trials[^whotrialregistration-e3], so follow your own country's rules.

**Where people go wrong**: writing a sketchy protocol. Many protocols do not adequately describe the primary outcome, the allocation method, blinding, the sample size calculation, the analysis methods, and so on, and gaps in the protocol lead to avoidable amendments[^chan2025spirit-e8].

### Step 8: While the trial runs: monitor the data and manage changes

**How:**
- **Decide whether to set up an independent data monitoring committee.** If an intervention turns out to work especially well, ethics may require stopping early; so results should be assessed as the data accumulate, ideally by an independent committee[^hopewell2025consortee-e39]. The protocol states its composition, its role, and whether it is independent of the sponsor and funder; if you do not set one up, explain why it is not needed[^chan2025spirit-e9].
- **Set the rules for interim analyses in advance**: interim analyses can look at benefit, futility, and safety[^hopewell2025consortee-e40]. Write the method for adjusting for repeated looks at the data into the protocol in advance[^hopewell2025consortee-e41], and state who can see interim results and who makes the final decision to stop[^chan2025spirit-e10].
- **Report safety problems promptly**: the Declaration of Helsinki requires that, where monitoring is needed, researchers report to the ethics committee and/or the data and safety monitoring body, especially serious adverse events[^wma2024helsinki-e16]; when risks and burdens outweigh the potential benefits, you must assess whether to continue, modify, or stop immediately[^wma2024helsinki-e17].
- **Keep participants in the trial**: plan in advance how you will complete follow-up, including which outcomes you will still collect from people who stop or deviate from the intervention[^chan2025spirit-e11].
- **Keep a record of changes**: each protocol version records the date and content of changes, and important amendments are reported promptly to the ethics committee and the registry[^chan2025spirit-e12]; protocol amendments need ethics committee approval[^wma2024helsinki-e16]. In the paper, report what was changed and when, because changes made before and after unblinding carry different risks of bias[^hopewell2025consortee-e42].

**Why**: looking at the data repeatedly without adjusting leads to wrong conclusions. The CONSORT explanatory paper gives an example: with five interim analyses, each using P = 0.05 as the threshold, the overall false positive rate rises to nearly 19%, not the intended 5%[^hopewell2025consortee-e43].

### Step 9: Analyze on the intention-to-treat principle

**How:**
- **Intention-to-treat analysis**: every randomized participant is included in the analysis and stays in the group they were originally assigned to, whatever intervention they actually received. This is what preserves the benefits of randomization, and it is widely recommended as the preferred approach[^hopewell2025consortee-e44].
- **For each analysis, state who was included and in which group they were counted**, rather than just using labels like "modified intention-to-treat" or "per-protocol"; excluding participants can undermine randomization and bias the effect estimate[^hopewell2025consortee-e45].
- **Handle missing data carefully.** Many trials are missing outcomes for more than 10% of randomized patients[^hopewell2025consortee-e46]; imputing data to get an intention-to-treat analysis may involve inappropriate methods such as "last observation carried forward"[^hopewell2025consortee-e47]. Write the approach into the statistical analysis plan in advance, and do sensitivity analyses `[Our analysis]`.
- **Adjust for covariates as planned**: adjusting for stratification variables is often advisable; whether to adjust for a covariate should not depend on whether it differs significantly between groups[^hopewell2025consortee-e48].
- **Be restrained with subgroup analyses**: a significant effect in one subgroup and not in another does not show that the subgroups differ; subgroup comparisons made after looking at the data are especially unlikely to be confirmed by later studies[^hopewell2025consortee-e49].

**Where people go wrong**: running significance tests on baseline characteristics to "prove that randomization worked". As long as randomization was not subverted, any baseline differences are due to chance; such tests are not recommended and should not be reported[^hopewell2025consortee-e50]. For general statistical principles, see the Part 2 section [Report how big the difference is and how sure you are, not just the p-value](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 10: Report following CONSORT 2025

CONSORT 2025 has 30 essential items and a participant flow diagram[^hopewell2025consort-e1], and replaces the 2010 version[^hopewell2025consort-e11]. Use it together with its explanatory paper[^hopewell2025consort-e12]; when you submit, attach the completed checklist showing where in the manuscript each item is addressed[^hopewell2025consort-e13].

- **Report all the results**: every planned primary and secondary outcome, at every time point, not just the significant or "interesting" ones[^hopewell2025consortee-e51]. For why, see the Throughout the project section [Report all results, including negative ones](../08_throughout/integrity_and_ethics.md#2-be-honest-with-the-evidence-dont-fool-yourself-report-all-results).
- **Report effect sizes with confidence intervals**, not just P values[^hopewell2025consortee-e52]; for a binary primary outcome, report both relative and absolute effects[^hopewell2025consortee-e53].
- **Use the flow diagram to account for every participant**: excluding participants from the analysis can lead to wrong conclusions, and unequal exclusions between the groups are a particular sign of bias[^hopewell2025consortee-e54].
- **Match the protocol, the statistical analysis plan, and the registration record**: if anything was not done or was changed, say so[^hopewell2025consort-e8].
- **Do not "spin" the results in the discussion**: some discussions are overly optimistic about the results, which is called interpretation bias[^hopewell2025consortee-e55].

## 3. Checklist

Compiled from CONSORT 2025, SPIRIT 2025, and their explanatory papers. CONSORT is not a quality assessment tool[^hopewell2025consort-e7]: it lists "what to report clearly". Below we have reorganized it as "what to do", and the tiers are our own judgment `[Our analysis]`.

**Must do**
- [ ] State the research question using PICO, and say whether it is superiority, non-inferiority, or equivalence[^hopewell2025consortee-e3][^hopewell2025consortee-e5]
- [ ] Prespecify one primary outcome, with its variable, data form, summary measure, and time point[^hopewell2025consortee-e7][^hopewell2025consortee-e9]
- [ ] State every assumption of the sample size calculation[^hopewell2025consortee-e15]
- [ ] The random sequence is unpredictable, and the method for generating it is described[^hopewell2025consortee-e19][^hopewell2025consortee-e25]
- [ ] The people who generate and conceal the sequence are separate from those who carry out the assignments[^hopewell2025consortee-e29]
- [ ] State who was blinded and how[^hopewell2025consortee-e56][^hopewell2025consortee-e35]
- [ ] Before enrollment: the protocol has ethics approval[^chan2025spirit-e7] and the trial is publicly registered[^wma2024helsinki-e9]
- [ ] For each analysis, state who was included and in which group they were counted[^hopewell2025consortee-e45]
- [ ] Report every planned outcome[^hopewell2025consortee-e51], with confidence intervals for the effect sizes[^hopewell2025consortee-e52]

**Better practice**
- [ ] Use the core outcome set for the disease area you are studying[^hopewell2025consortee-e10]
- [ ] Use central or third-party allocation[^hopewell2025consortee-e27]
- [ ] Finalize the statistical analysis plan before the database is locked[^hopewell2025consortee-e38]
- [ ] Post the main results to a primary registry within 12 months of study completion (a 2015 World Health Organization statement, as cited in the CONSORT explanatory paper)[^hopewell2025consortee-e57]

**Fine to skip; not a flaw**
- Participants and care providers cannot be blinded (for example in surgical or pragmatic trials)[^hopewell2025consortee-e34][^hopewell2025consortee-e58]: just state who was blinded[^hopewell2025consortee-e56].
- When the outcome is an objective measure such as all-cause mortality, whether data collectors and assessors are blinded is unlikely to matter[^hopewell2025consortee-e59].
- No data monitoring committee, as long as the protocol explains why one is not needed[^chan2025spirit-e9].
- No "test of blinding" (asking participants at the end of the trial which group they think they were in): its usefulness is itself questioned[^hopewell2025consortee-e60].

**Common reviewer criticisms that do not hold** (our sources do not measure how common these criticisms are; the items below are requests the sources explicitly reject `[Our analysis]`)
- "The groups differ significantly at baseline, so randomization failed": as long as randomization was not subverted, baseline differences are due to chance, and such tests are not recommended in the first place[^hopewell2025consortee-e50].
- "This baseline variable differs significantly between groups; please adjust for it": whether to adjust should not depend on whether the groups differ significantly[^hopewell2025consortee-e48].
- "The result is not significant; please add a post hoc power analysis": computing power from the trial's results after the fact to explain a nonsignificant result is of no value and may mislead readers[^hopewell2025consortee-e18].

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Allocating by hospital number, date of birth, or alternation and calling it "random" | These are not random methods, and cannot even be called "quasi-random"[^hopewell2025consortee-e20] |
| The enrolling doctor can see the random sequence, or the envelopes are see-through | Trials with inadequate allocation concealment overestimate effects[^hopewell2025consortee-e30] |
| Writing only "double-blind" without saying who was blinded | A survey of 200 trials found "double-blind" covered 18 different combinations of people[^hopewell2025consortee-e37] |
| Several primary outcomes, or switching the primary outcome afterward | Multiple comparisons are hard to interpret[^hopewell2025consortee-e8]; outcome changes often favor significant results[^hopewell2025consortee-e12] |
| Looking at the data repeatedly during the trial without adjusting | Five interim analyses each at P = 0.05 give a false positive rate of nearly 19%[^hopewell2025consortee-e43] |
| Analyzing only the people who "completed per protocol" | Excluding participants can undermine randomization[^hopewell2025consortee-e45] |
| Concluding "the effect differs by population" because one subgroup is significant and another is not | You cannot infer a subgroup difference this way[^hopewell2025consortee-e49] |

## 5. Further reading

- **The CONSORT 2025 statement and its explanatory paper** (Hopewell et al. 2025; the explanatory paper is published in the BMJ, with free full text on PubMed Central): the statement is the 30-item checklist and flow diagram, for checking against as you write the paper. The explanatory paper is the main source for this page; it goes item by item through what each one means, why it matters, and the empirical evidence behind it. Its sections on randomization, allocation concealment, blinding, and intention-to-treat analysis are worth reading at the design stage.
- **The SPIRIT 2025 statement** (Chan et al. 2025): 34 protocol items; check against it item by item as you write the protocol.
- **The Declaration of Helsinki (World Medical Association, 2024 version), the ICMJE recommendations (for medical journals), and the WHO International Clinical Trials Registry Platform web pages**: the foundational documents on ethics, registration, and data sharing; see the [clinical medicine field overview](../07_fields/clinical-medicine/README.md). Before registering, look up the primary registries on the WHO pages.
- Our sources do not cover specific sample size formulas and software, the details of imputing missing data, or the details of cluster, crossover, and other designs. See the relevant CONSORT extension, or ask a trial statistician.

[^hopewell2025consortee-e1]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17a, Box 5 (Treatment allocation in trials). [Evidence](../../sources/notes/hopewell2025consortee.md#e1)
[^hopewell2025consortee-e2]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 9 (Trial design), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e2)
[^hopewell2025consortee-e3]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 7 (Specific objectives), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e3)
[^hopewell2025consortee-e4]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 7, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e4)
[^hopewell2025consortee-e5]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 7, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e5)
[^hopewell2025consortee-e6]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 7, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e6)
[^hopewell2025consortee-e7]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 14 (Outcomes), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e7)
[^hopewell2025consortee-e8]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 14, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e8)
[^hopewell2025consortee-e9]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 14, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e9)
[^hopewell2025consortee-e10]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 14, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e10)
[^hopewell2025consortee-e11]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 7 (Specific objectives), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e11)
[^hopewell2025consortee-e12]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 14, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e12)
[^hopewell2025consortee-e13]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 10 (Changes to trial), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e13)
[^hopewell2025consortee-e14]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16a (Sample size), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e14)
[^hopewell2025consortee-e15]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e15)
[^hopewell2025consortee-e16]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e16)
[^hopewell2025consortee-e17]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e17)
[^hopewell2025consortee-e18]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e18)
[^hopewell2025consortee-e19]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e19)
[^hopewell2025consortee-e20]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e20)
[^hopewell2025consortee-e21]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17b (Type of randomisation), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e21)
[^hopewell2025consortee-e22]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17b, Box 6 (Randomisation and minimisation). [Evidence](../../sources/notes/hopewell2025consortee.md#e22)
[^hopewell2025consortee-e23]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17b, Box 6. [Evidence](../../sources/notes/hopewell2025consortee.md#e23)
[^hopewell2025consortee-e24]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17b, Box 6. [Evidence](../../sources/notes/hopewell2025consortee.md#e24)
[^altman2005treatment-e1]: Altman & Bland 2005 (BMJ statistics note), main text, para. 1. [Evidence](../../sources/notes/altman2005treatment.md#e1)
[^altman2005treatment-e2]: Altman & Bland 2005 (BMJ statistics note), main text, paras. 3–4. [Evidence](../../sources/notes/altman2005treatment.md#e2)
[^altman2005treatment-e3]: Altman & Bland 2005 (BMJ statistics note), main text, paras. 5–6. [Evidence](../../sources/notes/altman2005treatment.md#e3)
[^altman2005treatment-e4]: Altman & Bland 2005 (BMJ statistics note), main text, para. 7. [Evidence](../../sources/notes/altman2005treatment.md#e4)
[^hopewell2025consortee-e25]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e25)
[^hopewell2025consortee-e26]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 18 (Allocation concealment), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e26)
[^hopewell2025consortee-e27]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 18, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e27)
[^hopewell2025consortee-e28]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 18, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e28)
[^hopewell2025consortee-e29]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 19 (Implementation), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e29)
[^hopewell2025consortee-e30]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 18, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e30)
[^hopewell2025consortee-e31]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 18, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e31)
[^hopewell2025consortee-e32]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a (Blinding), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e32)
[^hopewell2025consortee-e33]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e33)
[^hopewell2025consortee-e34]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e34)
[^hopewell2025consortee-e35]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e35)
[^hopewell2025consortee-e36]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e36)
[^hopewell2025consortee-e37]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a, Box 7 (Blinding terminology). [Evidence](../../sources/notes/hopewell2025consortee.md#e37)
[^hopewell2025consortee-e38]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 3 (Protocol and statistical analysis plan), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e38)
[^hopewell2025consortee-e39]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16b (Interim analyses and stopping), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e39)
[^hopewell2025consortee-e40]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e40)
[^hopewell2025consortee-e41]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e41)
[^hopewell2025consortee-e42]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 10, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e42)
[^hopewell2025consortee-e43]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 16b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e43)
[^hopewell2025consortee-e44]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 21b (Analysis population), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e44)
[^hopewell2025consortee-e45]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 21b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e45)
[^hopewell2025consortee-e46]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 21c (Missing data), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e46)
[^hopewell2025consortee-e47]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 21b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e47)
[^hopewell2025consortee-e48]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 21a (Statistical methods), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e48)
[^hopewell2025consortee-e49]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 21d (Additional analyses), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e49)
[^hopewell2025consortee-e50]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 25 (Baseline data), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e50)
[^hopewell2025consortee-e51]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 26, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e51)
[^hopewell2025consortee-e52]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 26 (Outcomes and estimation), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e52)
[^hopewell2025consortee-e53]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 26, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e53)
[^hopewell2025consortee-e54]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 22a (Participant flow), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e54)
[^hopewell2025consortee-e55]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 29 (Interpretation), Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e55)
[^hopewell2025consortee-e56]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e56)
[^hopewell2025consortee-e57]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 2, Explanation (citing the 2015 World Health Organization statement on public disclosure of trial results). [Evidence](../../sources/notes/hopewell2025consortee.md#e57)
[^hopewell2025consortee-e58]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e58)
[^hopewell2025consortee-e59]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20a, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e59)
[^hopewell2025consortee-e60]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 20b, Explanation. [Evidence](../../sources/notes/hopewell2025consortee.md#e60)
[^hopewell2025consort-e2]: CONSORT 2025 (Hopewell et al. 2025), Introduction, PDF p. 3. [Evidence](../../sources/notes/hopewell2025consort.md#e2)
[^hopewell2025consort-e9]: CONSORT 2025 (Hopewell et al. 2025), CONSORT 2025 statement. [Evidence](../../sources/notes/hopewell2025consort.md#e9)
[^hopewell2025consort-e10]: CONSORT 2025 (Hopewell et al. 2025), Implication and limitations, PDF p. 7. [Evidence](../../sources/notes/hopewell2025consort.md#e10)
[^hopewell2025consort-e1]: CONSORT 2025 (Hopewell et al. 2025), Abstract, Results, PDF p. 2. [Evidence](../../sources/notes/hopewell2025consort.md#e1)
[^hopewell2025consort-e11]: CONSORT 2025 (Hopewell et al. 2025), CONSORT 2025 statement. [Evidence](../../sources/notes/hopewell2025consort.md#e11)
[^hopewell2025consort-e12]: CONSORT 2025 (Hopewell et al. 2025), CONSORT 2025 statement. [Evidence](../../sources/notes/hopewell2025consort.md#e12)
[^hopewell2025consort-e13]: CONSORT 2025 (Hopewell et al. 2025), CONSORT 2025 statement. [Evidence](../../sources/notes/hopewell2025consort.md#e13)
[^hopewell2025consort-e8]: CONSORT 2025 (Hopewell et al. 2025), explanatory paragraph after Table 1, PDF p. 9. [Evidence](../../sources/notes/hopewell2025consort.md#e8)
[^hopewell2025consort-e7]: CONSORT 2025 (Hopewell et al. 2025), Implication and limitations, PDF p. 7. [Evidence](../../sources/notes/hopewell2025consort.md#e7)
[^chan2025spirit-e1]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 20. [Evidence](../../sources/notes/chan2025spirit.md#e1)
[^chan2025spirit-e2]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 21b. [Evidence](../../sources/notes/chan2025spirit.md#e2)
[^chan2025spirit-e3]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 24c. [Evidence](../../sources/notes/chan2025spirit.md#e3)
[^chan2025spirit-e4]: SPIRIT 2025 (Chan et al. 2025), Introduction. [Evidence](../../sources/notes/chan2025spirit.md#e4)
[^chan2025spirit-e5]: SPIRIT 2025 (Chan et al. 2025), Updated SPIRIT 2025 statement. [Evidence](../../sources/notes/chan2025spirit.md#e5)
[^chan2025spirit-e6]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 32a. [Evidence](../../sources/notes/chan2025spirit.md#e6)
[^chan2025spirit-e7]: SPIRIT 2025 (Chan et al. 2025), Definition of a randomised trial protocol. [Evidence](../../sources/notes/chan2025spirit.md#e7)
[^chan2025spirit-e8]: SPIRIT 2025 (Chan et al. 2025), Introduction. [Evidence](../../sources/notes/chan2025spirit.md#e8)
[^chan2025spirit-e9]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 28a. [Evidence](../../sources/notes/chan2025spirit.md#e9)
[^chan2025spirit-e10]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 28b. [Evidence](../../sources/notes/chan2025spirit.md#e10)
[^chan2025spirit-e11]: SPIRIT 2025 (Chan et al. 2025), Table 1, item 25b. [Evidence](../../sources/notes/chan2025spirit.md#e11)
[^chan2025spirit-e12]: SPIRIT 2025 (Chan et al. 2025), Definition of a randomised trial protocol. [Evidence](../../sources/notes/chan2025spirit.md#e12)
[^whotrialregistration-e1]: WHO International Clinical Trials Registry Platform, Trial registration page, How to register a trial. [Evidence](../../sources/notes/whotrialregistration.md#e1)
[^whotrialregistration-e2]: WHO International Clinical Trials Registry Platform, Trial registration page, How to register a trial. [Evidence](../../sources/notes/whotrialregistration.md#e2)
[^whotrialregistration-e3]: WHO International Clinical Trials Registry Platform, Trial registration page, How to register a trial, NOTE. [Evidence](../../sources/notes/whotrialregistration.md#e3)
[^icmje2026recommendations-e21]: ICMJE Recommendations, January 2026 version, §III.L.1 Registration. [Evidence](../../sources/notes/icmje2026recommendations.md#e21)
[^icmje2026recommendations-e15]: ICMJE Recommendations, January 2026 version, §III.L.1 Registration. [Evidence](../../sources/notes/icmje2026recommendations.md#e15)
[^wma2024helsinki-e14]: WMA 2024 (Declaration of Helsinki), Use of Placebo. [Evidence](../../sources/notes/wma2024helsinki.md#e14)
[^wma2024helsinki-e15]: WMA 2024 (Declaration of Helsinki), Scientific Requirements and Research Protocols. [Evidence](../../sources/notes/wma2024helsinki.md#e15)
[^wma2024helsinki-e9]: WMA 2024 (Declaration of Helsinki), Research Registration, Publication, and Dissemination of Results. [Evidence](../../sources/notes/wma2024helsinki.md#e9)
[^wma2024helsinki-e16]: WMA 2024 (Declaration of Helsinki), Research Ethics Committees. [Evidence](../../sources/notes/wma2024helsinki.md#e16)
[^wma2024helsinki-e17]: WMA 2024 (Declaration of Helsinki), Risks, Burdens, and Benefits. [Evidence](../../sources/notes/wma2024helsinki.md#e17)
