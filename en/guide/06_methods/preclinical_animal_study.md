# Preclinical animal studies

This page covers **preclinical animal studies**: experiments on living animals whose results are meant to inform human medicine, for example to pave the way for a drug or therapy to enter human trials. It walks you step by step through designing, running, and reporting such an experiment well. Why so many preclinical findings fail to hold up in humans, and the four core reporting requirements proposed at a US workshop, are covered in the [Basic medicine field overview](../07_fields/basic-medicine/README.md). The basics of the 3Rs (Replacement, Reduction, Refinement) and of the ARRIVE (Animal Research: Reporting of In Vivo Experiments) reporting guidelines are covered in the [Biological sciences field overview](../07_fields/biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines). This page does not repeat them. For experiments on cells, tissues, or molecules, see [Bench experiments](bench_experiment.md); for controlled experiments with human participants, see [Controlled experiments](controlled_experiment.md) under research methods.

**Scope**: This page was first written for the Basic medicine field. It draws mainly on the reporting guidelines for animal research (ARRIVE 2.0 and its explanation document), material from the UK's National Centre for the Replacement, Refinement and Reduction of Animals in Research (NC3Rs, the body that promotes the 3Rs) and the US National Institutes of Health (NIH), and methods papers in biomedical journals. Besides [Basic medical sciences](../07_fields/basic-medicine/README.md), the field overviews for [Biological sciences](../07_fields/biological-sciences/README.md), [Animal and veterinary science](../07_fields/animal-veterinary-science/README.md), and [Medical engineering](../07_fields/medical-engineering/README.md) also list it as a common method. Animal ethics approval and reporting requirements differ across fields and countries; before you use this page, check your field's standards, the rules of your institution's animal ethics committee, and the author guidelines of your target journal.

**Strategies it usually serves:** [Causal explanation](../05_research-strategies/explain_causality.md) (showing that a treatment causes an effect in animals). The basis for this is the first aim of such studies: to show a causal relationship between treatment and effect in an animal model[^henderson2013threats-e13]; see Section 1 below.

**After reading this page, you should be able to:**

- explain why your animal model can stand in for the human disease, and what it cannot represent;
- fix the primary outcome, sample size, inclusion and exclusion criteria, humane endpoints, and stopping rules before you start, and write them into your protocol;
- randomize properly, conceal allocation, and plan blinding at each stage;
- know which housing and handling details affect results, and when a multi-laboratory study is worth doing;
- write your paper following ARRIVE 2.0.

---

## 1. What this kind of study is, and when to use it

A preclinical animal study has to do two things at once. First, it must show reliably in animals that "this treatment causes this effect"; second, the conclusion must carry over to patients[^henderson2013threats-e13]. In 2013, Henderson et al. reviewed 26 guidelines for preclinical study design, most of them aimed at drug development for neurological and cerebrovascular disease[^henderson2013threats-e1]. They sorted the risks into three kinds[^henderson2013threats-e2]:

| Risk | What it means | Example |
|---|---|---|
| Threats to internal validity | Factors that undermine the treatment-effect inference | The researcher's expectations bias how outcomes are assessed[^henderson2013threats-e13] |
| Threats to construct validity | Getting the relationship between the model and the human disease wrong | Using only an animal's rotational behavior to represent Parkinson's disease, when human Parkinson's also involves tremor and cognitive symptoms[^henderson2013threats-e3] |
| Threats to external validity | A relationship that holds in animals does not hold in patients | The response of an inbred mouse strain may be peculiar to that strain[^henderson2013threats-e6] |

Compared with cell experiments, it adds animal ethics approval (Step 7) and the ARRIVE reporting guidelines (Step 12); compared with clinical trials, its subjects are animals, so the conclusion still needs one more step to reach humans. **First decide which kind of experiment you are doing.** Exploratory experiments look for leads and generate hypotheses; confirmatory experiments test a hypothesis fixed in advance. You can only interpret the results correctly once this is clear[^perciedusert2020reporting-e56], and it also shapes many of the steps that follow. For the general version, see the Part 2 chapter on [telling exploratory and confirmatory research apart](../02_do-the-project/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring); for how basic medicine puts it, see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#tell-exploratory-experiments-from-confirmatory-ones). If others will use your results to justify human trials, run the study as a confirmatory experiment.

---

## 2. How to do it

The 12 steps below are roughly in chronological order; Steps 4 to 7 must all be finished before the first animal enters the experiment.

### Step 1: Make sure you really need animals

- **How:** Search the literature, ideally for systematic reviews of animal studies, to confirm the question has not already been answered; then write down why living animals are necessary[^perciedusert2020reporting-e33]. If you can avoid using animals, do; this is the "Replacement" in the 3Rs[^nc3rsthe3rs-e2]. For what you can use instead, see the [Biological sciences field overview](../07_fields/biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines).
- **Why:** Approval of animal experiments is generally based on a harm-benefit analysis: the harm to the animals is weighed against the benefit of the research to society[^perciedusert2020arrive-e6]. And if weak animal evidence is used to launch human trials, it adds to research waste and upsets the balance of risk and benefit for the participants[^perciedusert2020reporting-e70].
- **Where people go wrong:** Treating "nobody has done this in this model before" as an evidence gap. A systematic review can tell you whether the question has in fact already been answered.

### Step 2: Choose the model and write down why it represents humans

- **How:** State why you chose this species and model, how the measures relate to the human disease, and how the model has been validated. Writing only "this model is commonly used in the field" is not enough[^perciedusert2020reporting-e32]. Check against these questions (our own list, drawn from the sources below):
  - Is the model acute or chronic? Using an acute disease model to represent a chronic human disease is a mismatch[^henderson2013threats-e4].
  - Do the timing and route of administration match what is planned clinically? Of the recommendations on construct validity in the guidelines Henderson et al. pooled, 25 in total[^henderson2013threats-e9], 9 were about aligning preclinical procedures (such as dosing time) with the planned clinical study[^henderson2013threats-e7].
  - Was the procedure actually done right? For example, an intended tail-vein injection that ended up subcutaneous[^henderson2013threats-e5].
  - Did you characterize the model's disease phenotype before the experiment? This is one of the most common recommendations in these guidelines[^henderson2013threats-e1].
- **Why:** Getting the relationship between the model and the human disease wrong is a threat to construct validity[^henderson2013threats-e2]; however rigorous the experiment is internally, the conclusion then will not carry over to humans. Systematic reviews of the animal literature list the models others have used and their strengths and weaknesses, which can help you choose[^perciedusert2020reporting-e33].
- **Where people go wrong:** Concluding "effective in humans" from a single model and a single strain. Among the guidelines Henderson et al. pooled, the most common recommendation on external validity was to reproduce the effect in more than one model, followed by independent replication[^henderson2013threats-e8].

### Step 3: Build sex, age, and source into the design

- **How:**
  - **Sex**: Include both sexes by default and account for sex in design and analysis; if you use only one sex, have a sound reason (our recommendation, based on the sources below). Take the US National Institutes of Health as an example: for projects it funds, NIH requires vertebrate animal studies to consider sex as a biological variable in design, analysis, and reporting[^nihrigorguidance-e3], and applications proposing to study only one sex must provide strong justification[^nihrigorguidance-e6]. This is a requirement of the US NIH for its own grants; in other countries and for other funders, their own rules apply.
  - **Age**: Give the age in weeks, not "adult". "Adult mice" can be anywhere from 6 to 20 weeks old[^perciedusert2020reporting-e59].
  - **Source**: Record the supplier and batch. Animals of the same strain from different sources, or from the same source bought at different times, may differ genetically[^perciedusert2020reporting-e60].
- **Why:** Species, strain, substrain, sex, weight, and age affect most experimental results[^perciedusert2020reporting-e59]. NIH points out that sex is often overlooked in animal research, which leaves an incomplete picture of sex differences in response to treatment[^nihrigorguidance-e6]. A short review in the cancer field (Mak et al. 2014) also cites, among proposed improvements, including both sexes and a range of ages[^mak2014lost-e6]; see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#many-preclinical-findings-do-not-hold-up-in-humans) for details.
- **Where people go wrong:** Assuming that using only males ("less variable, fewer animals") needs no explanation. Where sex may be impossible to determine, as in embryos or juveniles, you need not report it; where it should have been reportable for that species and experiment but was not, give the reason[^perciedusert2020reporting-e71].

### Step 4: Decide exploratory or confirmatory, and fix the primary outcome and analysis plan

- **How:** State whether the experiment is exploratory, confirmatory, or both[^perciedusert2020reporting-e57]. A confirmatory experiment has just **one primary outcome measure**: it answers the main question and is the basis for the sample size calculation[^perciedusert2020reporting-e54]. Also fix when it will be assessed and how it will be analyzed[^landis2012call-e11]. Settle the statistical methods before collecting data[^perciedusert2020reporting-e26].
- **Why:** Exploratory studies look at many effects, some of which will come out significant by chance, so they produce more false positives[^perciedusert2020reporting-e56]. Findings from the exploratory phase need to be confirmed by confirmatory experiments designed and reported to the core requirements[^landis2012call-e17].
- **Where people go wrong:** Picking a significant measure as the primary outcome after the fact. The conclusions of a confirmatory experiment should be limited to the primary outcome; results on other measures may be underpowered and must not be presented as definitive[^perciedusert2020reporting-e58]. Hypotheses that came to you only after seeing the data must be clearly labeled as such[^perciedusert2020reporting-e57].

### Step 5: Calculate the sample size

- **How:** For a confirmatory experiment, do a power analysis. It needs these inputs[^perciedusert2020reporting-e34][^perciedusert2020reporting-e35]:
  1. **The difference in the primary outcome that would be meaningful**: set on biological grounds, and for preclinical research also with clinical relevance in mind;
  2. **Variability**: ideally from systematic reviews and previous studies; a pilot study alone usually does not give a good enough estimate[^perciedusert2020reporting-e36];
  3. **Target power**: 80% to 95% is generally considered acceptable;
  4. **Expected attrition**: build in the animals you expect to exclude or lose to death[^perciedusert2020reporting-e39].
- **Get the experimental unit right first.** Sample size counts experimental units, not measurements; when a whole cage is fed the same diet, the experimental unit is the cage[^perciedusert2020reporting-e6]. See the [Biological sciences field overview](../07_fields/biological-sciences/README.md#identify-the-experimental-unit-before-you-count-n) for details.
- **Why:** An experiment with so few animals that it has almost no chance of detecting a meaningful difference is unethical[^landis2012call-e8]. With low power, real effects are easily missed, the effects you do detect are often overestimated, and together with publication bias this adds false positives to the literature[^perciedusert2020reporting-e38]. Button, Ioannidis, and colleagues estimated the average power of animal studies in neuroscience at only about 20%[^perciedusert2017experimental-e4]. Conversely, using too many animals is also an ethical problem, and can produce results that are statistically significant but have no biological meaning[^perciedusert2020reporting-e37].
- **Where people go wrong:** Setting the number per group by "convention" without a calculation, and not mentioning this in the paper. If you did not do a power analysis, say so, and explain how you arrived at the sample size per group[^perciedusert2020reporting-e39].
- **Tool:** The Experimental Design Assistant (EDA) from the UK's NC3Rs is free. It can help you calculate sample size, generate randomization sequences that account for blocking, and plan blinding[^perciedusert2017experimental-e1][^perciedusert2017experimental-e2]. It does not replace a statistician, but it helps you ask a statistician for help more effectively[^perciedusert2017experimental-e5]. Note: all the authors of the paper introducing it were involved in building the tool (our note, from checking the author list).

### Step 6: Fix inclusion and exclusion criteria, humane endpoints, and stopping rules in advance

- **How:** Set the **inclusion and exclusion criteria** before the experiment starts and before any data are collected[^perciedusert2020reporting-e51], at the very least record them in your lab notebook, and state in the paper that they were set in advance[^perciedusert2020reporting-e52]. **Humane endpoints** are predefined physical, physiological, or behavioral signs that, once they appear, mean the animal is removed from the experiment[^perciedusert2020reporting-e65]. **Stopping rules** cover the sample size and when to stop collecting data; these too must be set in advance and reported in the paper[^landis2012call-e9].
- **Why:** Deciding afterward whom to exclude and when to stop leaves you room to pick data by the results. Animals that die or are excluded along the way are also information: if a treatment kills the sickest animals and this goes unreported, the treatment can look effective[^landis2012call-e10]; animals excluded because of adverse effects may also give safety information for human trials[^perciedusert2020reporting-e53].
- **Where people go wrong:** Adding a few more animals when the result is "almost significant". This is exactly why stopping rules have to be set in advance[^landis2012call-e9].

### Step 7: Write a protocol, get ethics approval, and consider preregistration

- **How:**
  1. **Write a protocol.** It covers the research question and hypotheses, the primary outcome, the statistical analysis plan, and the detailed procedures[^perciedusert2020reporting-e67].
  2. **Get ethics approval.** Before the experiment starts, you need approval from the relevant ethics committee and/or regulatory body[^perciedusert2020reporting-e64]. The approval process follows your country's laws and your institution's animal ethics committee.
  3. **Consider preregistration**, that is, registering the protocol on a public platform before the experiment starts. Options include:
     - animalstudyregistry.org, a registry dedicated to animal studies, run by the German Federal Institute for Risk Assessment (through its German Centre for the Protection of Laboratory Animals) and open to animal studies from anywhere in the world[^animalstudyregistry-e1]. A news item on its home page dated 2026-03-30 says that on March 25 it and preclinicaltrials.eu met to outline practical ways to expand preregistration[^animalstudyregistry-e3]; we could not read the about page of preclinicaltrials.eu, so check for yourself what studies it accepts.
     - The Open Science Framework, where you can set an embargo period so that the registration stays private until the paper is published[^perciedusert2020reporting-e68].
- **Why:** Preregistration shows that your hypotheses, methods, and analyses were planned in advance rather than tuned after seeing the data, and protects you against accusations of selective reporting[^perciedusert2020reporting-e66]. Reviewers can compare the registration with the paper[^animalstudyregistry-e2].
- **Where people go wrong:** Thinking that once you have registered, you cannot change anything. You can, but the paper must say what you deviated from and why[^perciedusert2020reporting-e69].

### Step 8: Randomize, and conceal allocation

- **How:**
  - **Generate the random sequence with a tool**: a random number generator, the Rand() function in a spreadsheet[^perciedusert2020reporting-e42], or coin tossing or a random number table[^kilkenny2009survey-e3].
  - **Prefer block randomization**: simple randomization does not guarantee that groups are balanced on other variables, and is rarely appropriate[^perciedusert2020reporting-e43]. You can form blocks by litter, cage, experiment day, or operator[^perciedusert2020reporting-e45], and randomize within each block. Include the blocks in the statistical model too[^perciedusert2020reporting-e44].
  - **Conceal allocation**: until the moment of assignment, the person doing the allocation does not know which group the next animal will go to[^perciedusert2020reporting-e48][^landis2012call-e6]. A colleague who is not involved in the experiment can hold the randomization list.
- **Why:** Picking an animal "at random" from the cage by hand is not random, because human judgment is involved; without random allocation, inferential statistics are not valid[^perciedusert2020reporting-e41].
- **Where people go wrong:** Putting the animals caught first (often the more active or easier to catch) into the treatment group and the ones caught later into the control group. Also, writing "randomized" without saying how leaves readers unable to judge. In 2009, Kilkenny et al. surveyed 271 animal research papers funded by public agencies in the UK and US: 12% reported random allocation, and of those only 9% (3 out of 33) described the method[^kilkenny2009survey-e1][^kilkenny2009survey-e4].

### Step 9: Plan blinding at each stage; at the very least, blind outcome assessment

- **How:** Blind every stage you can, from allocation, dosing, and care through to outcome assessment and data analysis. Even if you cannot blind the whole process, you can always blind some stages. This takes help from others; for example, a technician codes each animal's syringe, and a colleague codes the group labels for analysis[^perciedusert2020reporting-e47]. Priorities (our ordering, based on the sources below):
  1. **Outcome assessment**: especially important when there is a subjective element, such as scoring behavior or reading histology slides[^perciedusert2020reporting-e49].
  2. **Data analysis**: code the data before analysis and reveal the groups only after. The analyst makes semi-subjective decisions about data transformations, missing values, and outliers; this stage is often overlooked[^perciedusert2020reporting-e50].
  3. **When the assessor truly cannot be blinded** (for example, when the groups' phenotypes are obviously different): having a third party who does not know the expected result analyze the data reduces some of the bias[^perciedusert2020reporting-e49].
- **Why:** Systematic reviews show that unblinded outcome assessment overestimates treatment effects; lack of randomization and blinding can inflate effect sizes by as much as 30% to 45%[^perciedusert2020reporting-e24]. For the example of the stroke drug NXY-059, see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#many-preclinical-findings-do-not-hold-up-in-humans).
- **Where people go wrong:** One person doing allocation, dosing, scoring, and analysis alone.

### Step 10: Control the variables in housing and handling

- **How:** Standardize what you can, for example have the same person do all surgeries; what you cannot standardize, balance across groups, for example by randomizing the order of measurements or rotating each group's cage positions on the rack[^perciedusert2020reporting-e46]. Keep records too: the light cycle, the times of dosing and measurement, and the handling method (tail lifting versus cupping in the hands) all affect results[^perciedusert2020reporting-e63], so write them down. Single housing, food or water restriction, and not providing environmental enrichment all need a scientific justification[^perciedusert2020reporting-e62].
- **Why:** Every aspect of the housing environment can affect the animals' behavior and physiology, and so the results[^perciedusert2020reporting-e61]. For example, animals on the top shelf of a rack get more light, which may affect stress[^perciedusert2020reporting-e46]. Some confounders depend on the field: anesthetics affect cardiovascular function but rarely interfere with tumor growth, so they are a bigger threat in cardiovascular research[^henderson2013threats-e12].
- **Where people go wrong:** Putting all the treatment cages on the same shelf, or measuring the control group in the morning and the treatment group in the afternoon.

### Step 11: If you want the conclusions to generalize, consider a multi-laboratory or heterogenized design

- **How:** In a **multi-laboratory study**, several labs run the same protocol at the same time, and "laboratory" is included as a factor in the analysis. **Heterogenization within a single lab**: if a multi-laboratory study is not possible, you can deliberately vary the experimental conditions within one lab, for example by running the study in several batches[^voelkl2018reproducibility-e6][^voelkl2018reproducibility-e7].
- **Why:** Standardization makes animals more uniform, but it also makes the results more specific to that one set of conditions[^voelkl2018reproducibility-e2]. Labs differ in noise, odors, microbiota, staff, and so on, and the variation between labs is generally much larger than the variation within a lab[^voelkl2018reproducibility-e3]. In 2018, Voelkl et al. ran simulations using data from 440 preclinical studies in animal models of stroke, myocardial infarction, and breast cancer (simulations, not actual multi-laboratory experiments). They found that single-lab studies generally estimate effect sizes poorly; with just 2 to 4 labs taking part and no increase in sample size, the probability that the confidence interval covers the true effect rose by up to 42 percentage points[^voelkl2018reproducibility-e1]. The biggest improvement came from going from 1 lab to 2[^voelkl2018reproducibility-e4].
- **Where people go wrong:** Running a multi-laboratory study with too small a sample. The authors' rule of thumb: multi-laboratory designs improve estimates when the sample size is large enough to give a single-lab design a power of at least 0.8[^voelkl2018reproducibility-e5]. Also, multi-laboratory studies take a lot of effort to organize and may not suit more basic or exploratory research[^voelkl2018reproducibility-e6]; and simple heterogenization such as running in batches may not be enough to capture the variation between labs[^voelkl2018reproducibility-e7].

### Step 12: Report following ARRIVE 2.0

- **How:** ARRIVE 2.0 has 21 items, and reporting all of them is best practice; as a first step, at least report the "Essential 10"[^perciedusert2020arrive-e10]: study design, sample size, measures to reduce subjective bias, outcome measures, statistical methods, the experimental animals, experimental procedures, and results[^perciedusert2020arrive-e3]. Ideally, check against the checklist at the **design stage**, not after the paper is written[^perciedusert2020arrive-e7].
- Pay particular attention to these when writing (we picked these from the sources below):
  - **Report every measure you took.** If you report only the significant ones, the literature becomes biased toward positive results[^perciedusert2020reporting-e55].
  - **Say exactly how you randomized and which stages were blinded.** This is part of "measures to reduce subjective bias" in the Essential 10[^perciedusert2020arrive-e3] (for the problem of writing "randomized" without the method, see Step 8).
  - **Statistically significant does not mean biologically or clinically meaningful**: discuss the size of the effect[^perciedusert2020reporting-e72].
  - **Discuss the limitations of the model**, and do not let your conclusions go beyond what the model can support (see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#advice-for-newcomers)).
- **Why:** Submitting a completed checklist is not the same as reporting everything. A randomized controlled trial at PLOS ONE found that requiring authors to submit an ARRIVE checklist at submission, with no further checking by the editorial office, did not make the papers' reporting more complete[^perciedusert2020arrive-e11]. So check each item against the text, rather than just ticking the boxes.

---

## 3. Checklist

**Must do**

- [ ] State why you chose the model and how the measures relate to the human disease[^perciedusert2020reporting-e32]
- [ ] Get ethics approval before you start[^perciedusert2020reporting-e64]
- [ ] State whether the study is exploratory or confirmatory; for confirmatory experiments, fix one primary outcome in advance[^perciedusert2020reporting-e57][^perciedusert2020reporting-e54]
- [ ] Explain how the sample size was decided; if you did no power analysis, say so and give your reasons[^perciedusert2020reporting-e39]
- [ ] Fix inclusion and exclusion criteria, stopping rules, and statistical methods in advance[^perciedusert2020reporting-e51][^landis2012call-e9][^perciedusert2020reporting-e26]
- [ ] Randomize with a proper method[^perciedusert2020reporting-e41] and describe the method[^perciedusert2020arrive-e3]
- [ ] Blind at least some stages[^perciedusert2020reporting-e47] and state which stages were blinded[^perciedusert2020arrive-e3]
- [ ] Account for every animal that was excluded or died[^landis2012call-e10]
- [ ] Report at least the ARRIVE Essential 10[^perciedusert2020arrive-e10]

**Better practice**

- [ ] Use systematic reviews of the animal literature to establish the evidence gap and help choose the model[^perciedusert2020reporting-e33]
- [ ] Include both sexes (the US NIH requires this for projects it funds)[^mak2014lost-e6][^nihrigorguidance-e3]
- [ ] Use block randomization and include the blocks in the analysis[^perciedusert2020reporting-e43][^perciedusert2020reporting-e44]
- [ ] Conceal allocation; blind both outcome assessment and data analysis[^perciedusert2020reporting-e48][^perciedusert2020reporting-e50]
- [ ] Preregister the protocol before the experiment[^perciedusert2020reporting-e66]
- [ ] Report housing conditions and the times of dosing and measurement[^perciedusert2020reporting-e61][^perciedusert2020reporting-e63]
- [ ] Reproduce the result in a second model, or replicate independently[^henderson2013threats-e8]
- [ ] If you want the conclusions to generalize, run a multi-laboratory study or deliberately heterogenize within the lab[^voelkl2018reproducibility-e1][^voelkl2018reproducibility-e6]
- [ ] Report all 21 ARRIVE items[^perciedusert2020arrive-e10]

**Fine to skip; not a flaw**

- Animals used to produce antibodies or tissue, and pilot studies mainly for working out procedures or testing equipment, need no power analysis; base the numbers on how much you need or on practical capacity[^perciedusert2020reporting-e40].
- Exploratory experiments need no primary outcome, but their conclusions can only serve as leads[^landis2012call-e12].
- When phenotypic differences are so obvious that the assessor cannot be blinded, have a third party do the analysis instead, and say so in the paper[^perciedusert2020reporting-e49].
- When sex cannot be determined, as in embryos or juveniles, do not report it, but state why[^perciedusert2020reporting-e71].
- More basic or exploratory research need not be run as a multi-laboratory study; Voelkl et al. consider that it may not suit this kind of research[^voelkl2018reproducibility-e6].

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Writing only "we used the commonly used model X" | That is not a reason; you need to explain how the model relates to the human disease[^perciedusert2020reporting-e32] |
| Studying a chronic human disease with an acute disease model, without discussing the gap | The model does not match the clinical situation; this is a threat to construct validity[^henderson2013threats-e4] |
| Using only males, with no reason given | Sex affects results[^perciedusert2020reporting-e59]; the US NIH requires applications it funds to justify using only one sex[^nihrigorguidance-e6] |
| Grabbing animals from the cage by hand to form groups | That is not random in the statistical sense, so inferential statistics are not valid[^perciedusert2020reporting-e41] |
| The same person allocates, doses, and scores | Unblinded outcome assessment overestimates effects[^perciedusert2020reporting-e24] |
| Estimating variability from 3 animals in a pilot study and calculating the sample size from that | Pilot studies usually do not give a good enough estimate of variability[^perciedusert2020reporting-e36] |
| Adding a few more animals when the result is almost significant | Stopping rules must be set in advance[^landis2012call-e9] |
| Reporting only the significant measures | The literature becomes biased toward positive results[^perciedusert2020reporting-e55] |
| Presenting a significant result on a secondary measure as a conclusion | It may be underpowered and must not be presented as definitive[^perciedusert2020reporting-e58] |
| Treatment and control cages on different shelves of the rack | Light and other conditions differ, which may affect stress[^perciedusert2020reporting-e46] |
| Getting a result in one lab and one strain, then claiming it is "promising for clinical use" | The result may hold only under that one set of conditions[^voelkl2018reproducibility-e2]; it should be reproduced in more than one model[^henderson2013threats-e8] |
| Ticking the ARRIVE checklist at submission and leaving it at that | Submitting the checklist without any checking did not make reporting more complete[^perciedusert2020arrive-e11] |

---

## 5. Further reading

- **Percie du Sert et al. 2020, Reporting animal research: Explanation and elaboration for the ARRIVE guidelines 2.0 (PLOS Biology, open access)**: explanations and examples for every ARRIVE item; Box 3 (power analysis), Box 4 (randomization), and Box 5 (blinding at each stage) together make a design tutorial. Read it before you design your first animal experiment.
- **Henderson et al. 2013, Threats to validity in the design and conduct of preclinical efficacy studies (PLOS Medicine, open access)**: pools 26 guidelines for preclinical design and classifies their recommendations by internal, construct, and external validity. Read it when choosing a model and arguing how it relates to humans. Note that most of these guidelines target neurological and cerebrovascular disease[^henderson2013threats-e1], most came out of workshop discussions, and only 3 described how they were developed[^henderson2013threats-e11].
- **Percie du Sert et al. 2017, The Experimental Design Assistant (PLOS Biology, open access)**: introduces the free online design tool. Read it when you need to calculate sample size or generate a block randomization sequence, then use the tool directly. Note that all the authors were involved in developing the tool, so they have a stake in it (our own observation, from checking the author list).
- **Voelkl et al. 2018, Reproducibility of preclinical animal research improves with heterogeneity of study samples (PLOS Biology, open access)**: why "the more standardized the better" is not necessarily true, and the benefits of multi-laboratory designs. Read it when you plan for your conclusions to move toward the clinic. It is a simulation study based on published data.
- **Landis et al. 2012, A call for transparent reporting to optimize the predictive value of preclinical research (Nature; an author manuscript is available in PubMed Central)**: the source of the four core reporting requirements; for the key points, see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#report-at-least-four-things-in-preclinical-research-recommendations-from-a-us-workshop).

[^henderson2013threats-e1]: Henderson et al. 2013, Abstract. [Evidence](../../sources/notes/henderson2013threats.md#e1)
[^henderson2013threats-e2]: Henderson et al. 2013, Editors' Summary. [Evidence](../../sources/notes/henderson2013threats.md#e2)
[^henderson2013threats-e13]: Henderson et al. 2013, Introduction. [Evidence](../../sources/notes/henderson2013threats.md#e13)
[^henderson2013threats-e3]: Henderson et al. 2013, Introduction. [Evidence](../../sources/notes/henderson2013threats.md#e3)
[^henderson2013threats-e4]: Henderson et al. 2013, Box 1. [Evidence](../../sources/notes/henderson2013threats.md#e4)
[^henderson2013threats-e5]: Henderson et al. 2013, Box 1. [Evidence](../../sources/notes/henderson2013threats.md#e5)
[^henderson2013threats-e6]: Henderson et al. 2013, Introduction. [Evidence](../../sources/notes/henderson2013threats.md#e6)
[^henderson2013threats-e7]: Henderson et al. 2013, Results. [Evidence](../../sources/notes/henderson2013threats.md#e7)
[^henderson2013threats-e8]: Henderson et al. 2013, Results. [Evidence](../../sources/notes/henderson2013threats.md#e8)
[^henderson2013threats-e9]: Henderson et al. 2013, Editors' Summary. [Evidence](../../sources/notes/henderson2013threats.md#e9)
[^henderson2013threats-e11]: Henderson et al. 2013, Results, Guideline Characteristics. [Evidence](../../sources/notes/henderson2013threats.md#e11)
[^henderson2013threats-e12]: Henderson et al. 2013, Discussion. [Evidence](../../sources/notes/henderson2013threats.md#e12)
[^perciedusert2020reporting-e6]: Percie du Sert et al. 2020b, Item 1b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e6)
[^perciedusert2020reporting-e32]: Percie du Sert et al. 2020b, Item 12b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e32)
[^perciedusert2020reporting-e33]: Percie du Sert et al. 2020b, Item 12a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e33)
[^perciedusert2020reporting-e34]: Percie du Sert et al. 2020b, Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e34)
[^perciedusert2020reporting-e35]: Percie du Sert et al. 2020b, Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e35)
[^perciedusert2020reporting-e36]: Percie du Sert et al. 2020b, Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e36)
[^perciedusert2020reporting-e37]: Percie du Sert et al. 2020b, Item 2b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e37)
[^perciedusert2020reporting-e38]: Percie du Sert et al. 2020b, Item 2b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e38)
[^perciedusert2020reporting-e39]: Percie du Sert et al. 2020b, Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e39)
[^perciedusert2020reporting-e40]: Percie du Sert et al. 2020b, Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e40)
[^perciedusert2020reporting-e41]: Percie du Sert et al. 2020b, Item 4. [Evidence](../../sources/notes/perciedusert2020reporting.md#e41)
[^perciedusert2020reporting-e42]: Percie du Sert et al. 2020b, Item 4. [Evidence](../../sources/notes/perciedusert2020reporting.md#e42)
[^perciedusert2020reporting-e43]: Percie du Sert et al. 2020b, Box 4. [Evidence](../../sources/notes/perciedusert2020reporting.md#e43)
[^perciedusert2020reporting-e44]: Percie du Sert et al. 2020b, Box 4. [Evidence](../../sources/notes/perciedusert2020reporting.md#e44)
[^perciedusert2020reporting-e45]: Percie du Sert et al. 2020b, Box 4. [Evidence](../../sources/notes/perciedusert2020reporting.md#e45)
[^perciedusert2020reporting-e46]: Percie du Sert et al. 2020b, Item 4b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e46)
[^perciedusert2020reporting-e24]: Percie du Sert et al. 2020b, Item 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e24)
[^perciedusert2020reporting-e47]: Percie du Sert et al. 2020b, Item 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e47)
[^perciedusert2020reporting-e48]: Percie du Sert et al. 2020b, Box 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e48)
[^perciedusert2020reporting-e49]: Percie du Sert et al. 2020b, Box 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e49)
[^perciedusert2020reporting-e50]: Percie du Sert et al. 2020b, Box 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e50)
[^perciedusert2020reporting-e51]: Percie du Sert et al. 2020b, Item 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e51)
[^perciedusert2020reporting-e52]: Percie du Sert et al. 2020b, Item 3a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e52)
[^perciedusert2020reporting-e53]: Percie du Sert et al. 2020b, Item 3b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e53)
[^perciedusert2020reporting-e54]: Percie du Sert et al. 2020b, Item 6b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e54)
[^perciedusert2020reporting-e55]: Percie du Sert et al. 2020b, Item 6a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e55)
[^perciedusert2020reporting-e56]: Percie du Sert et al. 2020b, Item 13. [Evidence](../../sources/notes/perciedusert2020reporting.md#e56)
[^perciedusert2020reporting-e57]: Percie du Sert et al. 2020b, Item 13. [Evidence](../../sources/notes/perciedusert2020reporting.md#e57)
[^perciedusert2020reporting-e58]: Percie du Sert et al. 2020b, Item 17a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e58)
[^perciedusert2020reporting-e26]: Percie du Sert et al. 2020b, Item 7a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e26)
[^perciedusert2020reporting-e59]: Percie du Sert et al. 2020b, Item 8a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e59)
[^perciedusert2020reporting-e60]: Percie du Sert et al. 2020b, Item 8b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e60)
[^perciedusert2020reporting-e61]: Percie du Sert et al. 2020b, Item 15. [Evidence](../../sources/notes/perciedusert2020reporting.md#e61)
[^perciedusert2020reporting-e62]: Percie du Sert et al. 2020b, Item 15. [Evidence](../../sources/notes/perciedusert2020reporting.md#e62)
[^perciedusert2020reporting-e63]: Percie du Sert et al. 2020b, Item 9a, 9b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e63)
[^perciedusert2020reporting-e64]: Percie du Sert et al. 2020b, Item 14. [Evidence](../../sources/notes/perciedusert2020reporting.md#e64)
[^perciedusert2020reporting-e65]: Percie du Sert et al. 2020b, Item 16c. [Evidence](../../sources/notes/perciedusert2020reporting.md#e65)
[^perciedusert2020reporting-e66]: Percie du Sert et al. 2020b, Item 19. [Evidence](../../sources/notes/perciedusert2020reporting.md#e66)
[^perciedusert2020reporting-e67]: Percie du Sert et al. 2020b, Item 19. [Evidence](../../sources/notes/perciedusert2020reporting.md#e67)
[^perciedusert2020reporting-e68]: Percie du Sert et al. 2020b, Item 19. [Evidence](../../sources/notes/perciedusert2020reporting.md#e68)
[^perciedusert2020reporting-e69]: Percie du Sert et al. 2020b, Item 19. [Evidence](../../sources/notes/perciedusert2020reporting.md#e69)
[^perciedusert2020reporting-e70]: Percie du Sert et al. 2020b, Item 18. [Evidence](../../sources/notes/perciedusert2020reporting.md#e70)
[^perciedusert2020reporting-e71]: Percie du Sert et al. 2020b, Item 8a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e71)
[^perciedusert2020reporting-e72]: Percie du Sert et al. 2020b, Item 10b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e72)
[^perciedusert2020arrive-e6]: Percie du Sert et al. 2020a, Why good reporting is important. [Evidence](../../sources/notes/perciedusert2020arrive.md#e6)
[^perciedusert2020arrive-e3]: Percie du Sert et al. 2020a, Introducing ARRIVE 2.0. [Evidence](../../sources/notes/perciedusert2020arrive.md#e3)
[^perciedusert2020arrive-e7]: Percie du Sert et al. 2020a, Introducing ARRIVE 2.0. [Evidence](../../sources/notes/perciedusert2020arrive.md#e7)
[^perciedusert2020arrive-e10]: Percie du Sert et al. 2020a, Introducing ARRIVE 2.0. [Evidence](../../sources/notes/perciedusert2020arrive.md#e10)
[^perciedusert2020arrive-e11]: Percie du Sert et al. 2020a, Why good reporting is important. [Evidence](../../sources/notes/perciedusert2020arrive.md#e11)
[^perciedusert2017experimental-e1]: Percie du Sert et al. 2017, Introduction. [Evidence](../../sources/notes/perciedusert2017experimental.md#e1)
[^perciedusert2017experimental-e2]: Percie du Sert et al. 2017, The EDA improves the reliability of experimental results and analysis. [Evidence](../../sources/notes/perciedusert2017experimental.md#e2)
[^perciedusert2017experimental-e4]: Percie du Sert et al. 2017, same section (citing estimates by Button, Ioannidis, and colleagues). [Evidence](../../sources/notes/perciedusert2017experimental.md#e4)
[^perciedusert2017experimental-e5]: Percie du Sert et al. 2017, The EDA enables an effective assessment of the experimental plans. [Evidence](../../sources/notes/perciedusert2017experimental.md#e5)
[^landis2012call-e6]: Landis et al. 2012, Box 1, Blinding. [Evidence](../../sources/notes/landis2012call.md#e6)
[^landis2012call-e9]: Landis et al. 2012, Interim data analysis. [Evidence](../../sources/notes/landis2012call.md#e9)
[^landis2012call-e10]: Landis et al. 2012, Ad hoc exclusion of data. [Evidence](../../sources/notes/landis2012call.md#e10)
[^landis2012call-e11]: Landis et al. 2012, Retrospective primary end-point selection. [Evidence](../../sources/notes/landis2012call.md#e11)
[^landis2012call-e12]: Landis et al. 2012, An important note about exploratory experiments. [Evidence](../../sources/notes/landis2012call.md#e12)
[^landis2012call-e17]: Landis et al. 2012, An important note about exploratory experiments. [Evidence](../../sources/notes/landis2012call.md#e17)
[^landis2012call-e8]: Landis et al. 2012, Sample-size estimation. [Evidence](../../sources/notes/landis2012call.md#e8)
[^nc3rsthe3rs-e2]: NC3Rs, Definitions of the 3Rs. [Evidence](../../sources/notes/nc3rsthe3rs.md#e2)
[^nihrigorguidance-e3]: NIH, Consideration of relevant biological variables. [Evidence](../../sources/notes/nihrigorguidance.md#e3)
[^nihrigorguidance-e6]: NIH, Consideration of relevant biological variables. [Evidence](../../sources/notes/nihrigorguidance.md#e6)
[^mak2014lost-e6]: Mak et al. 2014, Limitations of animal models in cancer research. [Evidence](../../sources/notes/mak2014lost.md#e6)
[^animalstudyregistry-e1]: animalstudyregistry.org homepage. [Evidence](../../sources/notes/animalstudyregistry.md#e1)
[^animalstudyregistry-e2]: animalstudyregistry.org homepage. [Evidence](../../sources/notes/animalstudyregistry.md#e2)
[^animalstudyregistry-e3]: animalstudyregistry.org homepage, Latest News. [Evidence](../../sources/notes/animalstudyregistry.md#e3)
[^kilkenny2009survey-e1]: Kilkenny et al. 2009, Abstract. [Evidence](../../sources/notes/kilkenny2009survey.md#e1)
[^kilkenny2009survey-e3]: Kilkenny et al. 2009, Results. [Evidence](../../sources/notes/kilkenny2009survey.md#e3)
[^kilkenny2009survey-e4]: Kilkenny et al. 2009, Results. [Evidence](../../sources/notes/kilkenny2009survey.md#e4)
[^voelkl2018reproducibility-e1]: Voelkl et al. 2018, Abstract. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e1)
[^voelkl2018reproducibility-e2]: Voelkl et al. 2018, Introduction. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e2)
[^voelkl2018reproducibility-e3]: Voelkl et al. 2018, Introduction. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e3)
[^voelkl2018reproducibility-e4]: Voelkl et al. 2018, Discussion. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e4)
[^voelkl2018reproducibility-e5]: Voelkl et al. 2018, Discussion. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e5)
[^voelkl2018reproducibility-e6]: Voelkl et al. 2018, Discussion. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e6)
[^voelkl2018reproducibility-e7]: Voelkl et al. 2018, Discussion. [Evidence](../../sources/notes/voelkl2018reproducibility.md#e7)
