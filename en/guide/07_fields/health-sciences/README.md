# Health sciences: field overview

This page explains how research actually runs in the health sciences: public health, epidemiology, health services research, nutrition, nursing, sport and exercise science, environmental and occupational health, and related areas. The health sciences share many rules with clinical medicine: the Declaration of Helsinki, the recommendations of the International Committee of Medical Journal Editors (ICMJE), trial registration, reporting guidelines such as CONSORT (Consolidated Standards of Reporting Trials) and STROBE (Strengthening the Reporting of Observational Studies in Epidemiology), and the evidence pyramid. The [Clinical medicine page](../clinical-medicine/README.md) already covers these; this page assumes you have read it and only links to it. For what applies in every field, see the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies the health sciences commonly use and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

This page covers only what stands out more in the health sciences: the subject of study is often a **population**; many questions have to be answered with observational data; many studies use data that were not collected for research in the first place; qualitative research has its own quality standards; and ethics has to consider groups and communities, not just individuals. Our sources are mostly from epidemiology and public health. Our sources do not cover the specific norms of nursing, sport and exercise science, and similar areas; follow your advisor or your target journal. `[Our analysis]`

**After reading this page, you should be able to:**

- explain why observational studies are easily misled by confounding, measurement error, and selection bias;
- say, before you start the analysis, whether you are answering a question about association or a question about causation;
- know what to report when you use existing data such as registries, insurance claims, or electronic health records;
- know that population research also has to consider groups and communities ethically;
- name the research strategies the health sciences commonly use, and what evidence and standards each one is judged by.

---

## How research works in this field

### The subject is often a population

Public health and epidemiology are often concerned with the health of a group of people: what effect a diet, a policy, or an environmental exposure has on a population `[Our analysis]`. For example, the interventions studied in Cochrane systematic reviews include clinical ones as well as public health and policy ones[^higgins2024cochrane-e11]. Ethics guidelines reflect this too. The Council for International Organizations of Medical Sciences (CIOMS) is an international organization; its 2016 international ethical guidelines widened their scope from "biomedical research" to "health-related research"[^cioms2016ethical-e1], and merged what had been separate guidelines for biomedical research and for epidemiological studies into one document[^cioms2016ethical-e3].

### Many questions have to be answered with observational data

Randomized trials cannot answer every question; the Clinical medicine page [already covers this](../clinical-medicine/README.md#research-methods-common-in-this-field). The Cochrane Handbook also says that evidence about the harms of an intervention often has to come from non-randomized studies[^higgins2024cochrane-e8].

For some questions, a trial would simply be unethical. Hernán gives this example: to learn the long-term effect of drinking a glass of wine a day on chronic disease, a trial that assigns people to drink for years would be unethical, so observational analyses are the best chance to estimate that long-term effect[^hernan2018cword-e11]. That is why, as a newcomer, you first need to learn to spot [the three pitfalls of observational studies](#three-pitfalls-of-observational-studies) `[Our analysis]`.

### Many studies use data that already exist

**Routinely collected health data** are data collected without a specific research question decided in advance, and used for research later[^benchimol2015record-e1]. Examples include disease registries, primary care databases, health administrative data (such as insurance claims), electronic health record databases, cancer registries, and public health reporting data[^benchimol2015record-e2]. Large population databases let you study rare diseases, but they also magnify the risk of misclassifying people[^benchimol2015record-e15]. For how to use these data well, see [Using routinely collected data](#using-routinely-collected-data-report-the-codes-the-linkage-and-where-the-data-came-from) below.

### Publishing, preprints, and registration

The health sciences publish mainly in journals `[Our analysis]`; for the ICMJE recommendations, authorship, conflicts of interest, and data sharing statements, see the [Clinical medicine page](../clinical-medicine/README.md#norms-and-reporting-standards-in-this-field). You can post a **preprint** on medRxiv, a free preprint server for medicine and the health sciences[^medrxivabout-e1]. Before you do, know three things:

- It does not accept case reports, narrative reviews, scoping reviews, systematic reviews without a meta-analysis, and some other article types[^medrxivabout-e3].
- Preprints have not been peer reviewed. The server itself says they should not be used to guide clinical practice or health-related behavior, and should not be reported in the media as established information[^medrxivabout-e2].
- Once posted, a preprint cannot be removed[^medrxivabout-e4]. Check your target journal's preprint policy first (see the [Clinical medicine page](../clinical-medicine/README.md#publishing-is-mostly-in-journals-and-the-rules-are-fairly-uniform)).

**Registration**: for observational studies and other non-trial designs, the ICMJE encourages registration but does not require it[^icmje2026recommendations-e21]. But a public health intervention study may count as a "clinical trial": the interventions the ICMJE has in mind include behavioral treatments, educational programs, dietary interventions, quality improvement interventions, and changes to processes of care[^icmje2026recommendations-e17]. For when and where to register a clinical trial, see the [Clinical medicine page](../clinical-medicine/README.md#register-before-you-enroll-the-first-patient).

---

## How this field differs from others

In the table below, the health sciences column rests on the attached footnotes; the clinical medicine and computer science columns are our own summary of those two pages, which have the details `[Our analysis]`:

| | Health sciences | Clinical medicine | Computer science |
|---|---|---|---|
| Typical subject of study | Populations, communities, health systems `[Our analysis]` | Patients | Systems, algorithms, data |
| Where evidence comes from | Questions such as harms of interventions often rely on non-randomized studies[^higgins2024cochrane-e8]; existing data are common[^benchimol2015record-e1] | Trials and observational studies | Experiments and benchmarking |
| Main methodological risks | Confounding, measurement error, misclassification[^vandenbroucke2007strobe-e6] | Bias, selective reporting | Unfair comparisons, data leakage |
| Ethical focus | Individuals, plus groups and communities[^cioms2016ethical-e6] | Individuals (research participants) | Reviewed only when people are involved |
| Reporting guidelines | STROBE plus RECORD (REporting of studies Conducted using Observational Routinely-collected health Data)[^benchimol2015record-e3], COREQ (COnsolidated criteria for REporting Qualitative research), and others[^equatorcoreq-e3] | CONSORT, STROBE, and others | Whatever the conference requires |

---

## Three pitfalls of observational studies

### Pitfall 1: confounding, or "associated with" is not "causes"

For definitions of confounding and bias, see the [Clinical medicine page](../clinical-medicine/README.md#research-methods-common-in-this-field). In short, **confounding** means the association is real, but a factor you did not account for affects both the exposure and the outcome, so the association cannot be read as causal[^vandenbroucke2007strobe-e5]. Hernán's example: suppose the data show that people who drink a glass of wine a day have 0.8 times the risk of heart disease of people who do not drink (a risk ratio of 0.8). That does **not** mean drinking a glass a day lowers your risk by 20%[^hernan2018cword-e3]. It may be that these people have higher incomes, can afford nutritious food, have time to exercise, and have better access to preventive care, so their risk would be lower even if they did not drink[^hernan2018cword-e4].

### Pitfall 2: exposures are hard to measure, especially diet

Exposures such as diet and physical activity are often measured by questionnaire or recall, and are hard to measure accurately `[Our analysis]`. The STROBE explanation and elaboration paper says that inaccurate measurement or misclassification of exposures or outcomes can make true causal relationships harder to detect, or can create spurious ones; and measuring confounders inaccurately leaves "residual confounding" (confounding that remains after adjustment)[^vandenbroucke2007strobe-e6]. The less precisely an exposure is measured, the more the estimated effect tends to be pulled toward "no association"[^vandenbroucke2007strobe-e7]. Diet research has a further difficulty: what people eat is bound up with many other parts of their lifestyle. The same paper's example is that a finding such as "eating 2 to 4 eggs a week is associated with a doubled risk of ovarian cancer" should not be taken at face value, because dietary habits are associated with many lifestyle factors and with socioeconomic status[^vandenbroucke2007strobe-e8].

**What to do**: when you report your measurement methods, do not just cite one validation study. Give estimates of the measurement's validity or reliability, so that others can correct for measurement error or run sensitivity analyses[^vandenbroucke2007strobe-e10].

### Pitfall 3: who takes part can itself create an association

The STROBE explanation paper gives this example: some case-control studies found an association between young maternal age and childhood leukemia, and it later turned out that young mothers of healthy children were less willing to take part[^vandenbroucke2007strobe-e11]. Low participation does not necessarily make a study invalid, but you need to report participation honestly, along with the reasons people did not take part[^vandenbroucke2007strobe-e13].

### Before you start: are you answering a question about association or causation?

In 2018 Hernán published a commentary in the *American Journal of Public Health* that represents his personal view. He argues that causal inference is a core task of science, whether or not a study is randomized[^hernan2018cword-e2]. What he proposes:

1. **Frame the causal question as a "target trial."** A causal analysis of observational data can be seen as an attempt to emulate a hypothetical trial[^hernan2018cword-e5]. Writing that trial down forces you to be clear about what the intervention of interest is and when it happens. For example, "one glass a day for 10 years, starting at age 55" and "for 20 years, starting at age 30" are two different target trials that answer different causal questions[^hernan2018cword-e6].
2. **Your goal decides whether to adjust for confounding.** If the goal is causal, you generally need to adjust for confounding; if the goal is purely to describe an association, you do not[^hernan2018cword-e7].
3. **Do not let software choose your confounders.** Automated variable selection may suit prediction but not necessarily causal inference[^hernan2018cword-e8]. The STROBE explanation paper also advises against choosing confounders on the basis of statistical significance tests alone[^vandenbroucke2007strobe-e9].
4. **Present results in the results section; do not interpret them there.** In his view, the only place in a paper where "causal effect" should not appear is the results section[^hernan2018cword-e9].

There is a related distinction. The Cochrane Handbook's example: a nutritionist cares about the health effect of the diet itself, such as eating at least five portions of fruit and vegetables a day; this is a question of **etiology**. A public health practitioner cares about the effect of interventions that get people to eat this way; this is a question of **effectiveness**[^higgins2024cochrane-e9]. When you write your research question, be clear which kind you are asking `[Our analysis]`.

> **Where sources disagree: can a paper on an observational study use the word "causal"?**
> - **The cautious camp**: Hernán notes that many journal editors ask authors to avoid causal language[^hernan2018cword-e1]. The STROBE checklist also asks for a cautious overall interpretation of results that considers limitations, the number of analyses, results from similar studies, and other evidence[^vandenbroucke2007strobe-e12].
> - **Hernán's view**: avoiding the word "causal" is harmful, because causal inference is a core task of science[^hernan2018cword-e2]. But he also admits that you can never be sure a model includes all confounders, so an estimate cannot always be interpreted as causal[^hernan2018cword-e10]. The same journal issue published several responses to his commentary[^hernan2018cword-e12]; our sources did not include those responses.
>
> In practice: follow your target journal on wording first. But whatever words you use, your methods section should say which causal question you are trying to estimate, what you adjusted for, and which confounding you cannot rule out. `[Our analysis]`

---

## Norms and reporting standards in this field

### Reporting guidelines: a few more on top of the Clinical medicine page

For what reporting guidelines are and how to find them on the EQUATOR (Enhancing the QUAlity and Transparency Of health Research) Network, see the [Clinical medicine page](../clinical-medicine/README.md#reporting-guidelines-pick-the-checklist-for-your-study-type). The health sciences also commonly use the guidelines below. Apart from RECORD, we read only the COREQ entry page on the EQUATOR website, not the original texts of these guidelines; read the originals before you use them `[Our analysis]`.

| Study design | Reporting guideline | Notes |
|---|---|---|
| Observational studies using routinely collected data | RECORD | An extension of STROBE with 13 items[^benchimol2015record-e3]; it covers only how to report, not how to conduct the study[^benchimol2015record-e14] |
| Qualitative research | COREQ, SRQR (Standards for Reporting Qualitative Research) | EQUATOR lists both as the main reporting guidelines for qualitative research[^equatorcoreq-e3]; COREQ is a 32-item checklist for interviews and focus groups[^equatorcoreq-e1], from the 2007 paper by Tong, Sainsbury, and Craig[^equatorcoreq-e2] |
| Quality improvement studies | SQUIRE (Standards for QUality Improvement Reporting Excellence) | A main reporting guideline listed by EQUATOR[^equatorcoreq-e4] |
| Economic evaluations | CHEERS (Consolidated Health Economic Evaluation Reporting Standards) | A main reporting guideline listed by EQUATOR[^equatorcoreq-e5] |

### Using routinely collected data: report the codes, the linkage, and where the data came from

The authors of RECORD point out that common reporting gaps in these studies are unclear descriptions of how exposures and outcomes were coded, and missing linkage rates between data sources[^benchimol2015record-e4]. Following RECORD, report these things:

- **Where the data came from and why they were originally collected**, so readers understand the database's content and validity[^benchimol2015record-e13].
- **All codes and algorithms**: give a complete list of those used to define exposures, outcomes, confounders, and effect modifiers[^benchimol2015record-e5]; if the codes or algorithms used to select the study population have been validated, cite the validation studies[^benchimol2015record-e6].
- **How the data were linked**: if you linked two or more databases, describe the level at which they were linked, the linkage method, and how linkage quality was assessed[^benchimol2015record-e11].
- **Whether the hypotheses were formed before or after the analysis**[^benchimol2015record-e7]. This is the distinction between exploratory and confirmatory research covered in the Part 2 chapter [From research questions to an evidence plan](../../02_do-the-project/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring) `[Our analysis]`.
- **How to access the protocol, the raw data, or the code**[^benchimol2015record-e12].
- **Limitations**: the data were not collected for your question, so discuss the effects of misclassification bias, unmeasured confounding, missing data, changing eligibility over time, and similar problems[^benchimol2015record-e8].

Two traps that are easy to miss: administrative data are prone to "upcoding"; for example, when payment depends on case complexity, hospitals may use more complex diagnosis codes more often[^benchimol2015record-e9]. And when coding practices change, the data may no longer be consistent over time[^benchimol2015record-e10]. So if the "incidence" of a disease suddenly changes in a particular year, first check whether the coding rules changed `[Our analysis]`.

### Qualitative health research: say who you are and how you analyzed

Mays and Pope wrote in the *BMJ* (*British Medical Journal*) in 2000 that qualitative methods were by then widely used in health research, but many health services researchers were unsure how to judge their quality[^mays2000assessing-e1]. Whether qualitative research should be judged by the same criteria as quantitative research has long been hotly debated[^mays2000assessing-e2]. One camp holds that qualitative research is a distinct paradigm and should not be judged by conventional criteria such as validity and reliability[^mays2000assessing-e3]. Mays and Pope argue that the concepts of validity and relevance can be used, but how you apply them must be adapted to the goals of qualitative research[^mays2000assessing-e4]. They say there is no mechanical way to guarantee that qualitative research is free of error[^mays2000assessing-e10], but you can make it more credible like this:

- **Triangulation**: compare findings from different data collection methods (such as interviews and observation) or different data sources[^mays2000assessing-e5].
- **Reflexivity**: be aware of how you as the researcher shaped the data[^mays2000assessing-e6]. The interviewer's age, gender, and professional status (doctor, nurse, and so on) all affect the data and should be discussed[^mays2000assessing-e7].
- **Attention to negative cases**: actively look for and discuss data that contradict your interpretation[^mays2000assessing-e8].
- **Give enough of the original data** for readers to judge whether your interpretation is supported by the data[^mays2000assessing-e11].
- **Respondent validation** (asking participants to check your findings): useful, but only as one way to reduce error, not as a final test[^mays2000assessing-e9].
- For designing and coding interviews, the approach is the same as in [Interview studies](../../06_methods/interview_study.md) in Research types `[Our analysis]`.

### Ethics: protect individuals, and consider groups and communities

For ethics at the individual level (ethics review, informed consent), see the [Clinical medicine page](../clinical-medicine/README.md#your-subjects-are-people-so-ethics-comes-first) and [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) in Throughout the project. The 2016 CIOMS guidelines come from an international organization; they are not national law, and what you actually do depends on the rules of your country and institution `[Our analysis]`. They cover several issues that stand out more in population research:

- **Research must have value, but value does not justify treating people badly.** The ethical justification for health-related research with humans is its scientific and social value[^cioms2016ethical-e4]; but however great that value, it cannot justify treating participants or their communities badly[^cioms2016ethical-e5].
- **Results can harm a whole group.** Results of epidemiological, genetic, or sociological research can damage the interests of communities, families, or racial or ethnic groups[^cioms2016ethical-e6], and can expose a group to stigma or discrimination[^cioms2016ethical-e7]. Keep this in mind when you publish results such as "group X has a high prevalence of disease Y" `[Our analysis]`.
- **Engage communities early and keep them engaged.** The guidelines say potential participants and communities should be involved in the design, conduct, design of the informed consent process, monitoring, and dissemination of results[^cioms2016ethical-e8]. This makes the research relevant to the community and helps the community accept it[^cioms2016ethical-e9]. For example, when all community leaders are men, you should actively seek out women's views[^cioms2016ethical-e10]. The materials you submit to the ethics committee should include a community engagement plan[^cioms2016ethical-e11].
- **Using existing data also has ethical requirements.** When you use data collected in routine clinical care, you must use an informed opt-out procedure (people are told and can say no)[^cioms2016ethical-e12]. For an ethics committee to waive individual informed consent, three conditions must all hold: the research would not be feasible without the waiver; it has important social value; and it poses no more than minimal risk[^cioms2016ethical-e13]. Data custodians may give researchers only anonymized or coded data[^cioms2016ethical-e14]. When collecting and storing data in low-resource settings, work with local health authorities[^cioms2016ethical-e15].
- **Cluster randomized trials need separate thinking about consent.** These trials randomize communities, hospitals, or hospital units[^cioms2016ethical-e16]. Before starting, judge whether requiring individual informed consent, and letting people refuse, would undermine the study's results[^cioms2016ethical-e17].
- **When unsure, ask.** CIOMS itself admits there is no clear line between the ethics of social science research, behavioral research, and public health surveillance and the ethics of other research[^cioms2016ethical-e18]. If you are not sure whether or how your project needs review, ask your institution's ethics committee `[Our analysis]`.

### Systematic reviews: the Cochrane Handbook

The Cochrane Handbook covers systematic reviews of the effects of interventions, specifically the methods Cochrane uses[^higgins2024cochrane-e12]. For the full process (protocol, risk-of-bias assessment, pooling, grading the certainty of evidence, reporting according to PRISMA, the Preferred Reporting Items for Systematic reviews and Meta-Analyses), see [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md) in Research types. Reviews in the health sciences often have to include non-randomized studies, and then results must always be interpreted with caution[^higgins2024cochrane-e7]. To judge such studies, look at their specific design features (for example, which parts were designed prospectively), not just labels such as "cohort" or "case-control"[^higgins2024cochrane-e10].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists the three strategies the health sciences (mainly epidemiology and public health) commonly use. The grouping and the "What it looks like in the health sciences" column are our own summary; each standard represents only the source cited in its footnote `[Our analysis]`.

| Strategy | What it looks like in the health sciences | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Estimate the effect of diets, policies, or environmental exposures on population health; when a long-term randomized trial would be unethical, observational analyses are the best chance[^hernan2018cword-e11]; there are also cluster randomized trials that randomize communities, hospitals, or hospital units[^cioms2016ethical-e16] | A causal analysis of observational data can be seen as emulating a "target trial"[^hernan2018cword-e5]; if the goal is causal, adjust for confounding[^hernan2018cword-e7], and do not choose confounders on significance tests alone[^vandenbroucke2007strobe-e9]; report studies using existing data according to RECORD[^benchimol2015record-e3] | [Observational epidemiology](../../06_methods/observational_epidemiology.md), [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), [Quasi-experiments and causal identification](../../06_methods/quasi_experiment.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Cross-sectional studies are often used to estimate the prevalence of exposures, risk factors, or diseases[^vandenbroucke2007strobe-e3]; qualitative studies use interviews and focus groups to understand people's experiences and views | Report participation honestly, with reasons for non-participation[^vandenbroucke2007strobe-e13]; give estimates of measurement validity or reliability[^vandenbroucke2007strobe-e10]; qualitative studies gain credibility through triangulation, reflexivity, and attention to negative cases[^mays2000assessing-e5][^mays2000assessing-e6][^mays2000assessing-e8], and report according to COREQ or SRQR[^equatorcoreq-e3] | [Observational epidemiology](../../06_methods/observational_epidemiology.md), [Interview studies](../../06_methods/interview_study.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Systematic reviews of intervention effects, covering clinical as well as public health and policy interventions[^higgins2024cochrane-e11] | When including non-randomized studies, always interpret with caution[^higgins2024cochrane-e7]; look at specific design features, not just labels such as "cohort" or "case-control"[^higgins2024cochrane-e10] | [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md) |

How to use this table `[Our analysis]`:

- **First separate etiology questions from effectiveness questions.** The health effect of eating five portions of fruit and vegetables a day is an etiology question; the effect of an intervention that gets people to eat this way is an effectiveness question[^higgins2024cochrane-e9]. Both belong to causal explanation, but the target trial and the data sources differ.
- **In the health sciences, "comparing two interventions" is usually a causal question.** It needs a randomized trial or an observational causal design, not just a descriptive comparison.

## Research methods common in this field

Cross-field research types: [Observational epidemiology](../../06_methods/observational_epidemiology.md), [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md), [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), [Quasi-experiments and causal identification](../../06_methods/quasi_experiment.md), [Interview studies](../../06_methods/interview_study.md). For the differences between cohort, case-control, and cross-sectional studies, see the [Clinical medicine page](../clinical-medicine/README.md#research-methods-common-in-this-field). The following are also common in the health sciences but do not yet have their own how-to pages:

- **Studies using routinely collected data**: they use existing data such as registries, administrative data, and electronic health records[^benchimol2015record-e2], and report according to RECORD. The thinking is similar to [mining software repositories](../computer-science/practices/repository_mining.md) on the Computer science page, but health data raise privacy issues and need ethics approval `[Our analysis]`.
- **Cluster randomized trials**: they randomize communities, hospitals, or hospital units rather than individuals[^cioms2016ethical-e16].
- **Quality improvement studies** and **economic evaluations**: report them according to SQUIRE[^equatorcoreq-e4] and CHEERS[^equatorcoreq-e5] respectively.

---

## Advice for newcomers

1. **Write one sentence saying whether you are answering a question about association or causation.** If it is causal, try writing out the corresponding "target trial"[^hernan2018cword-e6].
2. **Before you use existing data, find out why they were originally collected**[^benchimol2015record-e13] **and whether the coding rules have changed**[^benchimol2015record-e10].
3. **Keep all your codes, algorithms, and analysis code in order.** RECORD asks you to list the complete codes and say how the code can be accessed[^benchimol2015record-e5][^benchimol2015record-e12].
4. **For population research, talk to the community early.** Your community engagement plan should go into the materials you submit to the ethics committee[^cioms2016ethical-e11].
5. **For public health intervention studies, check first whether you need to register.** Educational, dietary, and behavioral interventions can all count as clinical trials[^icmje2026recommendations-e17].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Turning "drinkers have less heart disease" into "drinking prevents heart disease" | The association may come from confounders such as income and lifestyle[^hernan2018cword-e4] |
| Citing one validation study and calling the questionnaire "valid" | You should give estimates of validity or reliability[^vandenbroucke2007strobe-e10] |
| Treating diagnosis codes in insurance or administrative data as true diagnoses | Upcoding and changes in coding rules are real problems[^benchimol2015record-e9][^benchimol2015record-e10] |
| Publishing that a group has "high prevalence" without considering stigma | Research results can harm a whole group[^cioms2016ethical-e7] |
| Assuming existing clinical data are free to use | CIOMS requires a way to opt out, and waiving consent is a decision for the ethics committee under set conditions[^cioms2016ethical-e12][^cioms2016ethical-e13] |
| Mixing up etiology questions and effectiveness questions | "The effect of eating five portions of fruit and vegetables" and "the effect of getting people to eat them" are two different questions[^higgins2024cochrane-e9] |

---

## Further reading

- **STROBE explanation and elaboration (Vandenbroucke et al. 2007)**: goes item by item through how to report observational studies, with many examples, and explains bias, confounding, and measurement error along the way. Read it when you do an observational study.
- **RECORD (Benchimol et al. 2015)**: read it before doing research with registry, insurance, or electronic health record data, and use its checklist to see what you need to report.
- **Hernán 2018, The C-Word**: a short commentary on why you should state your causal question first, and on the "target trial" idea. It is one side of a debate, and several responses were published in the same issue; read them side by side.
- **CIOMS 2016 International Ethical Guidelines**: the ethics of population research, community engagement, data use, and cluster randomized trials. Start with Guidelines 1, 4, 7, 12, and 21.
- **Cochrane Handbook**: read it when you do a systematic review of intervention effects. Start with Chapter 1; read Chapter 24 when you include non-randomized studies.
- **Mays & Pope 2000, Assessing quality in qualitative research**: a three-page paper on how to judge the quality of qualitative health research.

[^vandenbroucke2007strobe-e3]: Vandenbroucke et al. 2007, Box 1. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e3)
[^cioms2016ethical-e1]: CIOMS 2016, Preface (Scope of the 2016 version). [Evidence](../../../sources/notes/cioms2016ethical.md#e1)
[^cioms2016ethical-e3]: CIOMS 2016, Preface. [Evidence](../../../sources/notes/cioms2016ethical.md#e3)
[^cioms2016ethical-e4]: CIOMS 2016, Guideline 1. [Evidence](../../../sources/notes/cioms2016ethical.md#e4)
[^cioms2016ethical-e5]: CIOMS 2016, Guideline 1. [Evidence](../../../sources/notes/cioms2016ethical.md#e5)
[^cioms2016ethical-e6]: CIOMS 2016, Guideline 4 commentary (Risks to groups). [Evidence](../../../sources/notes/cioms2016ethical.md#e6)
[^cioms2016ethical-e7]: CIOMS 2016, Guideline 4 commentary (Risks to groups). [Evidence](../../../sources/notes/cioms2016ethical.md#e7)
[^cioms2016ethical-e8]: CIOMS 2016, Guideline 7. [Evidence](../../../sources/notes/cioms2016ethical.md#e8)
[^cioms2016ethical-e9]: CIOMS 2016, Guideline 7 commentary. [Evidence](../../../sources/notes/cioms2016ethical.md#e9)
[^cioms2016ethical-e10]: CIOMS 2016, Guideline 7 commentary. [Evidence](../../../sources/notes/cioms2016ethical.md#e10)
[^cioms2016ethical-e11]: CIOMS 2016, Guideline 7 commentary. [Evidence](../../../sources/notes/cioms2016ethical.md#e11)
[^cioms2016ethical-e12]: CIOMS 2016, Guideline 12. [Evidence](../../../sources/notes/cioms2016ethical.md#e12)
[^cioms2016ethical-e13]: CIOMS 2016, Guideline 12. [Evidence](../../../sources/notes/cioms2016ethical.md#e13)
[^cioms2016ethical-e14]: CIOMS 2016, Guideline 12. [Evidence](../../../sources/notes/cioms2016ethical.md#e14)
[^cioms2016ethical-e15]: CIOMS 2016, Guideline 12. [Evidence](../../../sources/notes/cioms2016ethical.md#e15)
[^cioms2016ethical-e16]: CIOMS 2016, Guideline 21 commentary. [Evidence](../../../sources/notes/cioms2016ethical.md#e16)
[^cioms2016ethical-e17]: CIOMS 2016, Guideline 21. [Evidence](../../../sources/notes/cioms2016ethical.md#e17)
[^cioms2016ethical-e18]: CIOMS 2016, Preface (Scope of the 2016 version). [Evidence](../../../sources/notes/cioms2016ethical.md#e18)
[^higgins2024cochrane-e7]: Cochrane Handbook, Chapter 24 Key Points. [Evidence](../../../sources/notes/higgins2024cochrane.md#e7)
[^higgins2024cochrane-e8]: Cochrane Handbook, §24.1. [Evidence](../../../sources/notes/higgins2024cochrane.md#e8)
[^higgins2024cochrane-e9]: Cochrane Handbook, §24.1. [Evidence](../../../sources/notes/higgins2024cochrane.md#e9)
[^higgins2024cochrane-e10]: Cochrane Handbook, Chapter 24 Key Points. [Evidence](../../../sources/notes/higgins2024cochrane.md#e10)
[^higgins2024cochrane-e11]: Cochrane Handbook, §1.1. [Evidence](../../../sources/notes/higgins2024cochrane.md#e11)
[^higgins2024cochrane-e12]: Cochrane Handbook, §1.1. [Evidence](../../../sources/notes/higgins2024cochrane.md#e12)
[^vandenbroucke2007strobe-e5]: Vandenbroucke et al. 2007 (STROBE explanation and elaboration article), Box 3. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e5)
[^vandenbroucke2007strobe-e6]: Vandenbroucke et al. 2007, Item 8 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e6)
[^vandenbroucke2007strobe-e7]: Vandenbroucke et al. 2007, Item 19 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e7)
[^vandenbroucke2007strobe-e8]: Vandenbroucke et al. 2007, Item 20 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e8)
[^vandenbroucke2007strobe-e9]: Vandenbroucke et al. 2007, Item 16 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e9)
[^vandenbroucke2007strobe-e10]: Vandenbroucke et al. 2007, Item 8 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e10)
[^vandenbroucke2007strobe-e11]: Vandenbroucke et al. 2007, Item 13 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e11)
[^vandenbroucke2007strobe-e12]: Vandenbroucke et al. 2007, STROBE checklist Item 20. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e12)
[^vandenbroucke2007strobe-e13]: Vandenbroucke et al. 2007, Item 13 explanation. [Evidence](../../../sources/notes/vandenbroucke2007strobe.md#e13)
[^hernan2018cword-e1]: Hernán 2018, beginning of the main text. [Evidence](../../../sources/notes/hernan2018cword.md#e1)
[^hernan2018cword-e2]: Hernán 2018, beginning of the main text. [Evidence](../../../sources/notes/hernan2018cword.md#e2)
[^hernan2018cword-e3]: Hernán 2018, Of course "association is not causation". [Evidence](../../../sources/notes/hernan2018cword.md#e3)
[^hernan2018cword-e4]: Hernán 2018, Of course "association is not causation". [Evidence](../../../sources/notes/hernan2018cword.md#e4)
[^hernan2018cword-e5]: Hernán 2018, Better causal questions. [Evidence](../../../sources/notes/hernan2018cword.md#e5)
[^hernan2018cword-e6]: Hernán 2018, Better causal questions. [Evidence](../../../sources/notes/hernan2018cword.md#e6)
[^hernan2018cword-e7]: Hernán 2018, Better confounding adjustment. [Evidence](../../../sources/notes/hernan2018cword.md#e7)
[^hernan2018cword-e8]: Hernán 2018, Better confounding adjustment. [Evidence](../../../sources/notes/hernan2018cword.md#e8)
[^hernan2018cword-e9]: Hernán 2018, Conflating the means and the ends. [Evidence](../../../sources/notes/hernan2018cword.md#e9)
[^hernan2018cword-e10]: Hernán 2018, Better confounding adjustment. [Evidence](../../../sources/notes/hernan2018cword.md#e10)
[^hernan2018cword-e11]: Hernán 2018, Conflating the means and the ends. [Evidence](../../../sources/notes/hernan2018cword.md#e11)
[^hernan2018cword-e12]: Hernán 2018, footnote. [Evidence](../../../sources/notes/hernan2018cword.md#e12)
[^benchimol2015record-e1]: Benchimol et al. 2015 (RECORD), Introduction. [Evidence](../../../sources/notes/benchimol2015record.md#e1)
[^benchimol2015record-e2]: Benchimol et al. 2015, Introduction. [Evidence](../../../sources/notes/benchimol2015record.md#e2)
[^benchimol2015record-e3]: Benchimol et al. 2015, Abstract. [Evidence](../../../sources/notes/benchimol2015record.md#e3)
[^benchimol2015record-e4]: Benchimol et al. 2015, Introduction. [Evidence](../../../sources/notes/benchimol2015record.md#e4)
[^benchimol2015record-e5]: Benchimol et al. 2015, RECORD item 7.1. [Evidence](../../../sources/notes/benchimol2015record.md#e5)
[^benchimol2015record-e6]: Benchimol et al. 2015, RECORD item 6.2. [Evidence](../../../sources/notes/benchimol2015record.md#e6)
[^benchimol2015record-e7]: Benchimol et al. 2015, explanation in the Introduction section. [Evidence](../../../sources/notes/benchimol2015record.md#e7)
[^benchimol2015record-e8]: Benchimol et al. 2015, RECORD item 19.1. [Evidence](../../../sources/notes/benchimol2015record.md#e8)
[^benchimol2015record-e9]: Benchimol et al. 2015, explanation in the Discussion (Limitations) section. [Evidence](../../../sources/notes/benchimol2015record.md#e9)
[^benchimol2015record-e10]: Benchimol et al. 2015, explanation in the Discussion (Limitations) section. [Evidence](../../../sources/notes/benchimol2015record.md#e10)
[^benchimol2015record-e11]: Benchimol et al. 2015, RECORD item 12.3. [Evidence](../../../sources/notes/benchimol2015record.md#e11)
[^benchimol2015record-e12]: Benchimol et al. 2015, RECORD item 22.1. [Evidence](../../../sources/notes/benchimol2015record.md#e12)
[^benchimol2015record-e13]: Benchimol et al. 2015, explanation in the Methods (Setting) section. [Evidence](../../../sources/notes/benchimol2015record.md#e13)
[^benchimol2015record-e14]: Benchimol et al. 2015, Introduction. [Evidence](../../../sources/notes/benchimol2015record.md#e14)
[^benchimol2015record-e15]: Benchimol et al. 2015, explanation in the Methods (Participants) section. [Evidence](../../../sources/notes/benchimol2015record.md#e15)
[^mays2000assessing-e1]: Mays & Pope 2000, Summary points. [Evidence](../../../sources/notes/mays2000assessing.md#e1)
[^mays2000assessing-e2]: Mays & Pope 2000, Two opposing views. [Evidence](../../../sources/notes/mays2000assessing.md#e2)
[^mays2000assessing-e3]: Mays & Pope 2000, the antirealist position. [Evidence](../../../sources/notes/mays2000assessing.md#e3)
[^mays2000assessing-e4]: Mays & Pope 2000, Summary points. [Evidence](../../../sources/notes/mays2000assessing.md#e4)
[^mays2000assessing-e5]: Mays & Pope 2000, Triangulation. [Evidence](../../../sources/notes/mays2000assessing.md#e5)
[^mays2000assessing-e6]: Mays & Pope 2000, Reflexivity. [Evidence](../../../sources/notes/mays2000assessing.md#e6)
[^mays2000assessing-e7]: Mays & Pope 2000, Reflexivity. [Evidence](../../../sources/notes/mays2000assessing.md#e7)
[^mays2000assessing-e8]: Mays & Pope 2000, Attention to negative cases. [Evidence](../../../sources/notes/mays2000assessing.md#e8)
[^mays2000assessing-e9]: Mays & Pope 2000, Respondent validation. [Evidence](../../../sources/notes/mays2000assessing.md#e9)
[^mays2000assessing-e10]: Mays & Pope 2000, Assessing the validity of qualitative research. [Evidence](../../../sources/notes/mays2000assessing.md#e10)
[^mays2000assessing-e11]: Mays & Pope 2000, Clear exposition of methods. [Evidence](../../../sources/notes/mays2000assessing.md#e11)
[^equatorcoreq-e1]: EQUATOR Network, COREQ checklist page. [Evidence](../../../sources/notes/equatorcoreq.md#e1)
[^equatorcoreq-e2]: EQUATOR Network, COREQ checklist page. [Evidence](../../../sources/notes/equatorcoreq.md#e2)
[^equatorcoreq-e3]: EQUATOR Network, COREQ checklist page sidebar. [Evidence](../../../sources/notes/equatorcoreq.md#e3)
[^equatorcoreq-e4]: EQUATOR Network, COREQ checklist page sidebar. [Evidence](../../../sources/notes/equatorcoreq.md#e4)
[^equatorcoreq-e5]: EQUATOR Network, COREQ checklist page sidebar. [Evidence](../../../sources/notes/equatorcoreq.md#e5)
[^medrxivabout-e1]: medRxiv, About medRxiv. [Evidence](../../../sources/notes/medrxivabout.md#e1)
[^medrxivabout-e2]: medRxiv, About medRxiv. [Evidence](../../../sources/notes/medrxivabout.md#e2)
[^medrxivabout-e3]: medRxiv, About medRxiv. [Evidence](../../../sources/notes/medrxivabout.md#e3)
[^medrxivabout-e4]: medRxiv, About medRxiv. [Evidence](../../../sources/notes/medrxivabout.md#e4)
[^icmje2026recommendations-e17]: ICMJE Recommendations, §III.L.1. [Evidence](../../../sources/notes/icmje2026recommendations.md#e17)
[^icmje2026recommendations-e21]: ICMJE Recommendations, January 2026 version, §III.L.1. [Evidence](../../../sources/notes/icmje2026recommendations.md#e21)
