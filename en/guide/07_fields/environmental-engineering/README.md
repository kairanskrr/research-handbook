# Environmental engineering: field overview

This page covers a few concrete things about research in environmental engineering (water and wastewater treatment, air quality, solid waste, contaminated site remediation, and so on): how to plan before you sample, how to run quality control on measurements, how to report low concentrations, and what to watch for when working with water utilities and communities. For content shared with the Earth and environmental sciences (field observation, environmental processes), see the [Earth and environmental sciences page](../earth-environmental-sciences/README.md); for how research on chemical processes works and more uses of life cycle assessment, see the [Chemical engineering page](../chemical-engineering/README.md); for what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). This page covers only what is specific to this field. For the research strategies the field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence); for how to do the work, see [Research methods common in this field](#research-methods-common-in-this-field).

Almost all the rules cited on this page come from the US: documents from the US Environmental Protection Agency, the US Geological Survey, and the American Society of Civil Engineers, plus one journal of the American Chemical Society. They are examples, not worldwide conventions; if you do research in China or anywhere else, follow your local authorities, your funder, and your target journal.

**After reading this page, you should be able to:**

- explain how research in this field divides the work among the lab, pilot scale, the field, and models;
- plan with "data quality objectives" before you sample, and know what goes into a quality assurance project plan;
- say what blanks, replicates, and spikes each check, know how a detection limit is determined, and know how to handle data below it;
- know which ethical and trust issues to watch for when working with water utilities and communities;
- know what life cycle assessment is and where it tends to go wrong.

---

## How research works in this field

### What the field studies: pollution control technologies and contaminated environments

In a 2002 guidance document, the US Environmental Protection Agency (EPA) defined "environmental technology" as a broad category: pollution control devices and systems, waste treatment and storage facilities, and site remediation technologies, such as wet scrubbers for air emissions, soil washing, and granular activated carbon units for treating water[^epa2002qapp-e17]. Research in this field roughly revolves around two things: developing and improving such technologies; and measuring and predicting the concentrations and fate of pollutants in water, air, and soil.

A technology project may pass through several scales. The table below is our own summary:

| Scale | What you do | What to watch for |
|---|---|---|
| Bench scale (lab) | Run tests in beakers, columns, or small reactors, with synthetic or real water samples | Conditions are easy to control, but may be far from the real environment (see the journal requirements below) |
| Pilot scale | Set up a larger unit at a water treatment plant, wastewater treatment plant, or site, and run it continuously on real influent | You have to coordinate with the operator; it takes a long time, and influent quality fluctuates |
| Field sampling | Collect samples from rivers, distribution systems, or sites and send them to the lab for analysis | You need a sampling plan and quality control in advance (see below) |
| Modeling | Use models to predict treatment performance or pollutant transport | The EPA guidance requires you to state whether you are applying an existing model (evaluate first whether it is fit for the purpose) or developing a new one because no suitable model exists[^epa2002qapp-e5] |

Some journals explicitly require research to move beyond "ideal conditions." Take *Environmental Science & Technology* (ES&T), a journal of the American Chemical Society (ACS). Its author guidelines require that:

- evaluations are done under environmentally relevant conditions and concentrations, and concentrations are reported as **measured** values, not nominal ones (the amount you meant to add when preparing the solution)[^estauthorguidelines-e6];
- new materials (such as sorbents or catalysts) have been tested under at least one environmental condition, at environmentally meaningful pollutant concentrations[^estauthorguidelines-e9];
- new measurement techniques are validated with real environmental samples wherever possible[^estauthorguidelines-e3];
- the conclusions of environmental monitoring studies apply beyond the places and times sampled[^estauthorguidelines-e7].

These are one journal's requirements, and other journals may not have them. But they are a warning: results obtained only under ideal lab conditions carry limited weight with journals of this kind.

### Publishing: ES&T as the example

Below, ES&T's author guidelines (accessed October 2026) serve as an example of the requirements you will meet when you submit. Journal policies change, and other journals may have different rules, so follow your target journal's requirements at the time you submit:

- **Novelty is the first hurdle.** ES&T states that lack of novelty is a common reason for rejection[^estauthorguidelines-e1]; manuscripts that only report routine data, or that address questions already well understood, are not considered[^estauthorguidelines-e2]; studies that only describe the results of standard lab or field tests, or the performance of commercial products, are also not suitable[^estauthorguidelines-e4].
- **The cover letter matters.** ES&T says a substantial share of submissions are not sent out for review because the editors judge them insufficient in novelty, scientific merit, or environmental significance; the cover letter is your chance to convince the editor[^estauthorguidelines-e12].
- **Manuscripts leaning toward chemical engineering, catalyst synthesis, or analytical chemistry must briefly argue that they are primarily significant to the environmental field**, and where appropriate compare against state-of-the-art methods[^estauthorguidelines-e8].
- **Length**: research articles are limited to 7,000 words[^estauthorguidelines-e10]; urgent preliminary findings can go to the sister journal ES&T Letters[^estauthorguidelines-e11].
- **Deposit your data in public repositories.** ES&T requires all published papers to deposit materials, data, and protocols in public repositories[^estauthorguidelines-e14]; when code is central to the paper, state the exact versions of the language, compiler or interpreter, and operating system[^estauthorguidelines-e15].
- **Preprints are allowed**: before acceptance you can post to platforms that assign a DOI (Digital Object Identifier, a permanent link), such as ChemRxiv, bioRxiv, or arXiv, but you must cite the preprint in the manuscript[^estauthorguidelines-e16].
- **Watch out with theses**: if the submitted content is used in your thesis or dissertation, either deposit the thesis in a public repository with a DOI, or delay or remove the online version of the thesis until the paper is formally published[^estauthorguidelines-e17].

**How long review takes (cross-field figures, for reference only).** In a study published in 2013, Björk and Solomon drew a stratified random sample of 2,700 articles from 135 journals in the Scopus citation database[^bjork2013publishing-e1]; for each journal they took the last 20 articles published in 2012, counting backward, and grouped the journals roughly into nine groups such as engineering, earth sciences, and social sciences[^bjork2013publishing-e2]. "Submission to acceptance" reflects the time spent on review and revision; "acceptance to publication" reflects the production process and the queue waiting to be published[^bjork2013publishing-e3]. For the engineering group, these two stages averaged 5.0 months and 4.3 months[^bjork2013publishing-e4]. But the differences among journals within a group were much larger than the differences between groups[^bjork2013publishing-e5]. The study did not break out environmental engineering separately, and the data are more than ten years old, so treat them only as a rough guide; for how long your target journal actually takes, go by the figures the journal publishes.

Our sources do not say whether this field publishes mainly in journals or at conferences, or what its authorship-order conventions are; follow your advisor and your target journal.

---

## How this field differs from others

The table below is our own summary, meant to help you spot the differences quickly; it is not a strict division between fields.

| | Environmental engineering | Computing |
|---|---|---|
| Where data come from | Physical samples: water, air, soil, sludge, which must be collected, preserved, transported, and analyzed | Mostly experiments on code, systems, and datasets |
| Where most of the error is | The EPA guidance holds that sampling error is generally much larger than measurement error[^epa2006dqo-e7] | Random seeds, data splits, implementation details, and so on (see the [Computer science page](../computer-science/README.md)) |
| Quality control | A full set of formal practices: quality assurance project plans, blanks, replicates, spikes (see below) | Relies mainly on releasing code and on artifact evaluation |
| What if you "can't detect it"? | There are detection limits and reporting limits, and data below them need special handling (see below) | Rarely comes up |
| Who uses the results | Regulators, water utilities, and communities may use them to make decisions; they may also be used as evidence in court[^epa2002qapp-e8] | Mainly academic peers and industry |
| Who you deal with | Possibly water treatment plants, wastewater treatment plants, site owners, and local residents | Less often; for research involving people, see the relevant research type page |

---

## Norms and reporting standards in this field

### Plan before you sample: EPA's data quality objectives process

Environmental data may be used to decide whether something "meets the standard," or to estimate "what the average pollutant concentration is." EPA recommends planning with the **Data Quality Objectives** (DQO) process in these situations[^epa2006dqo-e2], because if you do not plan before sampling, the chance that the data you collect cannot meet the project's needs is unacceptably high[^epa2006dqo-e1]. EPA's 2006 guidance divides the process into seven steps, which can be repeated[^epa2006dqo-e4]. The brief explanations in parentheses are ours:

1. State the problem.
2. Identify the goal of the study (what question the data must answer).
3. Identify information inputs.
4. Define the boundaries of the study (what is being studied, and its spatial and temporal extent).
5. Develop the analytic approach (which statistic to use and how to reach a conclusion).
6. Specify performance or acceptance criteria (how much error you can tolerate).
7. Develop the plan for obtaining data (how many samples, where, and by what method).

A few points from this guidance worth remembering:

- **First define "what one sample represents."** When the population is a continuous medium such as air, water, or soil, you must define the sampling unit as a given area, volume, or mass[^epa2006dqo-e6].
- **Put resources into sampling, not only into more precise measurement.** The guidance says that sampling error is generally much larger than measurement error and needs more resources to control[^epa2006dqo-e7]; when you expect large spatial or temporal variation, consider using a cheaper, less precise analytical method in exchange for samples from more places and times[^epa2006dqo-e9].
- **Decision errors can only be controlled, never eliminated.** When you use data for a statistical test, you can never fully rule out making the wrong decision[^epa2006dqo-e8]; that is why step 6 sets performance or acceptance criteria in advance[^epa2006dqo-e4].
- **Before using someone else's data, check its quality assurance and quality control information** to see whether it meets your needs[^epa2006dqo-e10].
- **Match the detail and rigor of the plan to how the data will be used and the resources you have**[^epa2006dqo-e11].
- **Bring in the people who will use the data.** The guidance says the planning team usually includes the project manager, technical staff, data users, and stakeholders[^epa2006dqo-e5].
- **You can adjust as you go.** The Triad approach, developed by EPA's technology innovation program, uses the results of early sampling to guide later sampling[^epa2006dqo-e3].

### Write the plan down: EPA's quality assurance project plan

A **Quality Assurance Project Plan** (QAPP) puts the results of a project's technical planning in one place: how the data work will be done, what the quality objectives are, and who the key people are[^epa2002qapp-e1]. EPA's 2002 guidance requires it to be completed and approved before the project starts[^epa2002qapp-e2].

Be clear about the scope: this is **EPA's policy for projects it funds**. Any EPA-funded work that collects, evaluates, uses, or reports environmental data (including the use of existing data and modeling), or that involves the design, construction, or operation of environmental technology, must have an approved plan[^epa2002qapp-e3]. For projects not funded by EPA, whether you need one and what form it takes depend on your funder and institution; if nobody requires it, writing a simplified version following its structure can still help you think the problem through before you start. Under EPA's "graded approach," if an element does not apply, you simply state why[^epa2002qapp-e4].

### Quality control samples: blanks, replicates, and spikes

First understand the purpose of quality control: **not to eliminate error, but to measure or estimate its effect**[^epa2002qapp-e9]. EPA's QAPP guidance requires you to state, for each measurement, which quality control checks you will run and how often[^epa2002qapp-e13]. The types the guidance mentions:

| Quality control sample | What it is | What it checks |
|---|---|---|
| Blank | A "clean" sample containing none of the target analyte | Contamination introduced at each stage of sampling and analysis[^epa2002qapp-e10] |
| Field blank | Taken to the sampling site, exposed to sampling conditions, then brought back to the lab and handled like an environmental sample[^epa2002qapp-e14] | Contamination introduced at the sampling site and during transport (our inference from the definition) |
| Replicates, split samples | Measuring the same sample more than once, or dividing one sample into several portions measured separately | Random error, that is, precision[^epa2002qapp-e12] |
| Collocated samples, also called field duplicates | Two or more samples, considered identical, collected at the same time and place[^epa2002qapp-e16] | Replicates can show the precision of the measurement or sampling stage[^epa2002qapp-e12] |
| Standards, matrix spikes | Samples of known concentration; or real samples to which a known amount of the target analyte is added[^epa2002qapp-e15] | Systematic error, that is, bias[^epa2002qapp-e11]; the effect of the matrix on recovery[^epa2002qapp-e15] |

Report these results in your paper: ES&T requires, where applicable, an assessment of uncertainty or a sensitivity analysis, and adequate quality assurance and quality control[^estauthorguidelines-e5].

### Detection limits and "non-detect" data

The **Method Detection Limit** (MDL), as US EPA defines it, is the lowest measured concentration that can be reported with 99% confidence that it is distinguishable from method blank results[^epa2016mdl-e2]. The procedure below comes from the appendix on analytical methods under the Clean Water Act in the US Code of Federal Regulations[^epa2016mdl-e1]; other countries and other kinds of testing have their own standards. Its requirements show that a laboratory must determine the detection limit by actually running its own full procedure:

- It must include **all the steps** the lab uses to process samples[^epa2016mdl-e3].
- Use at least 7 spiked samples and 7 method blanks, prepared and analyzed in at least 3 batches on 3 different days[^epa2016mdl-e4].
- In the initial determination, **do not use statistical methods to reject outliers**, because there are few data points and the procedure is meant to reflect the method's routine variability[^epa2016mdl-e5].
- Calculate one value from the spiked samples and one from the method blanks, and take the larger[^epa2016mdl-e6].
- Recalculate at least every 13 months[^epa2016mdl-e7].

Another common term is the **reporting limit**: below this concentration, the lab cannot confidently give a specific value[^helsel2020statistical-e6]. Data reported as "below the reporting limit" are, in statistical terms, **censored data**[^helsel2020statistical-e1].

On how to analyze censored data, *Statistical Methods in Water Resources* (2020 edition), the textbook Helsel and colleagues wrote for the United States Geological Survey (USGS), gives clear warnings:

- **Don't casually replace "non-detects" with half the reporting limit.** Substituting this way and then running a t-test is common in water resources, but it can miss differences that really exist and find differences that do not[^helsel2020statistical-e2].
- **A better approach**: when comparing which of two groups is higher, you can treat all data below the highest reporting limit as tied ranks and run a rank-sum test, without making up values[^helsel2020statistical-e4]; this way you do not pretend to know the exact value of each non-detect[^helsel2020statistical-e3].
- **How much it matters depends on the proportion.** In trend analysis, replacing censored values with arbitrary values biases the slope estimate; but when "less-than" values are rare (below about 5%), the effect may be small[^helsel2020statistical-e5].

So in your paper, state the detection and reporting limits and how they were determined, how many data fall below them, and how you handled them in the statistics.

### Sample IDs and chain of custody

The following practices come from EPA's QAPP guidance:

- **Give every sample a unique ID** and track it throughout, so samples do not get mixed up[^epa2002qapp-e6].
- **Chain of custody**: record who held the sample and how it was handled at every step from collection to lab analysis[^epa2002qapp-e7]. Practices may include sample labels, a record signed by everyone who handles the sample, and containers sealed with custody seals; a project may require this when the data might be used as evidence in court[^epa2002qapp-e8].

Academic research does not always need chain of custody in the legal sense; but if your data might be used by regulators, in litigation, or in public controversy, it is best to keep records to this standard from the start. For general ways to organize samples and data, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

### Working with water utilities and communities; environmental justice

Research in this field may take place in other people's facilities and homes: water treatment plants, wastewater treatment plants, site owners, residents. Professional codes of ethics can serve as a reference. Take the code of ethics the American Society of Civil Engineers (ASCE) sets for its members (most recently updated in October 2020)[^asce2020code-e10]:

- First and foremost, protect the health, safety, and welfare of the public[^asce2020code-e2]; this takes precedence over all other responsibilities[^asce2020code-e1].
- Express professional opinions truthfully, and only when founded on adequate knowledge and honest conviction[^asce2020code-e3]; work only in areas of your competence[^asce2020code-e8].
- Disclose actual, potential, or perceived conflicts of interest[^asce2020code-e6]; keep confidential any information that clients and employers identify as proprietary[^asce2020code-e7].
- Acknowledge the diverse historical, social, and cultural needs of communities, and incorporate these considerations into your work[^asce2020code-e4].

When working with a water utility, it is best to agree in writing, before you start, whether and in what form the data can be made public. When research involves residents' samples or data, ES&T requires you to name the approving ethics committee and the approval number, and to state that the samples or data were obtained with informed consent[^estauthorguidelines-e18]; for general principles, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) in Throughout the project.

**Environmental justice** is a related concept. The definition on the US EPA website in 2024 was: the just treatment and meaningful involvement of all people, regardless of income, race, color, national origin, Tribal affiliation, or disability, in agency decision-making and other federal activities that affect human health and the environment[^epa2024environmentaljustice-e1], so that people are protected from disproportionate and adverse human health and environmental effects, including cumulative impacts of multiple burdens[^epa2024environmentaljustice-e2]. Three caveats: when we accessed it in October 2026, this page had been taken down and could only be read through a May 2024 snapshot in the Internet Archive; the definition comes from US federal policy at the time, US policy in this area has since changed, and our sources do not go into it; and we use it here only to illustrate the concept, as other countries have their own terms.

One example is the lead contamination of drinking water in Flint, Michigan, in the US. What follows comes from a 2019 retrospective by Roy and Edwards, members of the Virginia Tech team that was involved. It is one participating team's account, not a neutral investigation; the people and organizations it criticizes may not agree.

- According to the authors, in 2015 a collaboration among Flint residents, the Virginia Tech team, and others was the first to expose the contamination of the water supply[^roy2019citizen-e1]. The university provided the technical approach, analysis, and funding; residents provided local knowledge and turned their own homes into sampling sites[^roy2019citizen-e2]; citywide sampling coordinated by residents eventually covered 269 homes[^roy2019citizen-e3].
- The authors argue that when scientists ignore people with local knowledge, the consequences can be disastrous[^roy2019citizen-e5].
- The authors also record problems that came later, for example people collecting unrepresentative data that caused unfounded fear among residents about bathing water[^roy2019citizen-e6]. They cite strategies proposed by Freitag and colleagues for improving credibility, including training participants, quality assurance procedures, and cross-checking data against professionals' data[^roy2019citizen-e4].

What this example shows: community collaboration can uncover problems others have overlooked; and representative sampling and quality control are just as necessary in community collaboration.

### Life cycle assessment

**Life Cycle Assessment** (LCA) is a "cradle-to-grave" assessment: from the extraction of raw materials to the point where all materials return to the earth[^epa2006lca-e1]. According to EPA's 2006 introductory report, it has four parts: goal and scope definition, inventory analysis, impact assessment, and interpretation[^epa2006lca-e2]. For how it is used for chemical processes, see the [Chemical engineering page](../chemical-engineering/README.md).

Its value is that it looks at the whole product system, avoiding the "local optimum" that comes from focusing on one stage only[^epa2006lca-e3]. For example, option 1 produces less solid waste and looks greener; a life cycle assessment may show that its total impact across air, water, and land is actually larger[^epa2006lca-e4].

The report warns about several places where it is easy to go wrong:

- **Comparing on the wrong basis.** Choose the **functional unit**, the basis for measuring and presenting the results, carefully[^epa2006lca-e7]. To compare two kinds of wall insulation, compare them on the same function (their ability to reduce heat flow)[^epa2006lca-e8].
- **Not stating assumptions.** If you do not state your assumptions, the results may be taken out of context or misinterpreted[^epa2006lca-e9].
- **Ignoring data limitations.** What data you can get greatly affects how accurate the results are[^epa2006lca-e5].
- **Treating "which is better" as an objective conclusion.** Under the international standard ISO 14042, judging which option is better involves deciding which kinds of impact matter more, and that is a subjective judgment[^epa2006lca-e10].
- **Thinking it can answer everything.** It cannot tell you which option is the most cost-effective or works best[^epa2006lca-e6].

---

## Research methods common in this field

The cross-field methods are linked below; here we note only what this field needs to watch for in addition. Lab and pilot-scale studies and life cycle assessment do not yet have pages of their own; see above.

- [Field studies: observation and sampling](../../06_methods/field_study.md), [Longitudinal studies](../../06_methods/longitudinal_study.md): field monitoring and long-term repeated monitoring of the same sites. Plan with data quality objectives and include a full set of quality control samples (see above).
- [Quantitative simulation](../../06_methods/simulation_study.md): water quality models, air dispersion models, groundwater transport models. State whether you are applying an existing model or developing a new one[^epa2002qapp-e5].
- [Data science](../../06_methods/data_science.md): analyzing existing monitoring data. First check the data's quality assurance and quality control information[^epa2006dqo-e10], and handle data below the reporting limit correctly[^helsel2020statistical-e2].
- [Review studies](../../06_methods/review_study.md), [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md): systematically pooling existing studies. For systematic reviews in the environmental field, you can follow the guidelines of the Collaboration for Environmental Evidence, which does not accept reviews without a protocol registered in advance[^cee2022guidelines-e1]; see the "Synthesis" row of the table in the next section.
- [Case studies](../../06_methods/case_study.md), [Interview studies](../../06_methods/interview_study.md), [Questionnaire surveys](../../06_methods/questionnaire_survey.md): used when studying pollution incidents, community experiences, and public perceptions. Research involving people needs ethics committee approval, and ES&T requires you to say so in the paper[^estauthorguidelines-e18].

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by the central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists the six strategies this page's sources support, what evidence each usually relies on, and what standards it is judged by.

The grouping and the "What it looks like in environmental engineering" column are our own summary; the standards come mostly from EPA guidance and from the author guidelines of one journal, ES&T, and represent only the sources in the footnotes. Two things to note: the "Causal explanation" row rests on CADDIS (the Causal Analysis/Diagnosis Decision Information System), an online system from the US EPA aimed mainly at stream ecosystems[^epa2026caddis-e1]; the "Synthesis" row rests on the 2022 guidelines of the Collaboration for Environmental Evidence and on ROSES by Haddaway and colleagues (2018), which address environmental management as a whole; neither was written specifically for environmental engineering. Our sources do not cover how other strategies, such as proof or interpretation and argument, are used in this field.

| Strategy | What it looks like in environmental engineering | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Developing and improving "environmental technologies": pollution control devices, waste treatment facilities, site remediation technologies, and so on[^epa2002qapp-e17], often moving from bench scale to pilot scale | ES&T requires evaluation under realistic conditions and concentrations, with measured concentrations reported[^estauthorguidelines-e6]; new materials tested under at least one environmental condition at meaningful concentrations[^estauthorguidelines-e9]; manuscripts leaning toward catalyst synthesis or chemical engineering compared, where appropriate, against state-of-the-art methods[^estauthorguidelines-e8]; studies that only describe standard tests or commercial product performance are not enough[^estauthorguidelines-e4] | No page of its own for this field; for ideas, see [Engineering research](../computer-science/practices/engineering_research.md) (computer science) and [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Field monitoring, for example estimating the average concentration of a pollutant[^epa2006dqo-e2] | Plan before sampling with the [data quality objectives process](#plan-before-you-sample-epas-data-quality-objectives-process)[^epa2006dqo-e1]; sampling error is generally much larger than measurement error[^epa2006dqo-e7]; ES&T requires the conclusions of monitoring studies to apply beyond the places and times sampled[^estauthorguidelines-e7] | [Field studies: observation and sampling](../../06_methods/field_study.md), [Longitudinal studies](../../06_methods/longitudinal_study.md), [Data science](../../06_methods/data_science.md) |
| [Measurement](../../05_research-strategies/measure.md) | Developing new measurement techniques; determining method detection limits | ES&T requires new measurement techniques to be validated with real environmental samples wherever possible[^estauthorguidelines-e3]; the method detection limit must include all sample-processing steps[^epa2016mdl-e3] and be determined in at least 3 batches[^epa2016mdl-e4] | [Experimental measurement](../../06_methods/experimental_measurement.md), [Detection limits](#detection-limits-and-non-detect-data) above |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Using life cycle assessment to compare the total environmental impact of several products or options[^epa2006lca-e4] | Compare on the same function[^epa2006lca-e8]; state assumptions[^epa2006lca-e9]; judging which option is better involves subjective judgment[^epa2006lca-e10] | [Life cycle assessment](#life-cycle-assessment) above |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Finding the cause of a problem at a specific site, for example whether biological impairment in a stretch of river is caused by a particular effluent discharge[^epa2026caddis-e2]. CADDIS deals specifically with such "why is this site impaired" cases[^epa2026caddis-e3] | Following CADDIS: list several candidate causes at the outset and compare them at the end[^epa2026caddis-e6]; consider all relevant evidence, such as field observations, regional monitoring, and lab experiments[^epa2026caddis-e4]; the more kinds and amounts of evidence, the less likely you are to be misled by one flawed dataset[^epa2026caddis-e9]; ruling out is more certain than confirming, so rule out as much as you can first, for example if the effect appears upstream of a source, that source is ruled out[^epa2026caddis-e5]; evidence from the site itself, more than one association, and evidence tightly linking the proximate cause to the effect score highest[^epa2026caddis-e8]; each candidate cause is finally classed as refuted, diagnosed, probable, unlikely, or uncertain, and when evidence is insufficient the cause may not be identified[^epa2026caddis-e7] | No page of its own for this field; data come from [Field studies: observation and sampling](../../06_methods/field_study.md) and [Data science](../../06_methods/data_science.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Using a **systematic review** (searching, screening, appraising, and pooling existing studies according to a protocol written in advance) to answer a question, for example a protocol published in 2026 by a South African team: pooling the effectiveness of a class of biodegradable foam materials at removing heavy metals from water[^mokoena2026adsorption-e1], including lab and pilot-scale studies[^mokoena2026adsorption-e2] | The 2022 guidelines (version 5.1) of the Collaboration for Environmental Evidence (CEE): reviews without a protocol registered in advance are not accepted, nor are protocols written after the fact[^cee2022guidelines-e1]; report methods so that others can check the results, using the recommended ROSES checklist (RepOrting standards for Systematic Evidence Syntheses)[^cee2022guidelines-e2], a set of reporting forms and a flow diagram that Haddaway and colleagues designed in 2018 specifically for systematic reviews and systematic maps (another form of evidence synthesis alongside systematic reviews) in conservation and environmental management[^haddaway2018roses-e2]; beyond a checklist, it also asks for summary information on each key step of the review[^haddaway2018roses-e4], such as the total number of search results before duplicates are removed[^haddaway2018roses-e5]; conclusions can report the quality and relevance of the included studies, effect sizes, and whether effects are consistent[^cee2022guidelines-e5], and point out where the evidence may not apply[^cee2022guidelines-e6]; do not treat "no evidence of an effect" as "evidence of no effect"[^cee2022guidelines-e3]. The protocol above uses a checklist to appraise each study's internal validity, external validity, and reporting transparency[^mokoena2026adsorption-e3], for example whether it accounted for interfering factors such as competing ions in the water and complex water matrices[^mokoena2026adsorption-e4] | [Review studies](../../06_methods/review_study.md), [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md) |

How to use this table: first find your strategy from your central claim, then read the matching strategy page and methods page. Many projects are mixed, for example developing a new sorbent (building and improving) while also building an analytical method for it (measurement); in that case choose the main strategy based on your central claim, and hold the other parts to their own standards.

---

## Advice for newcomers

1. **Write a plan before you sample.** Following the seven DQO steps, at least state the problem, the study boundaries, and the acceptance criteria[^epa2006dqo-e4]. For general planning methods, see the Part 2 chapter [Writing a research plan](../../02_do-the-project/03_research-plan.md).
2. **Treat sampling as the main source of error.** Put your effort into how many sites to sample and when, not only into measuring more precisely[^epa2006dqo-e7][^epa2006dqo-e9].
3. **Decide on quality control in advance.** For each measurement, write down which checks you will run (blanks, replicates, spikes, and so on) and how often[^epa2002qapp-e13].
4. **Find out how the detection limit you use was determined**[^epa2016mdl-e3]. In the paper, state how many data fall below the reporting limit and how you handled them; don't casually replace them with half the reporting limit[^helsel2020statistical-e2].
5. **Number every sample and record who handled it, starting with the first one.** That is the only way to trace problems when something goes wrong[^epa2002qapp-e6][^epa2002qapp-e7].
6. **Test lab results under real conditions.** For example, ES&T requires new materials to have been tested under at least one environmental condition at meaningful concentrations[^estauthorguidelines-e9].
7. **Before working with a water utility or community, agree on how the data will be used, whether they can be made public, and who hears the results first**. The ASCE code puts protecting public health first[^asce2020code-e2].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Not running blanks | You cannot know how much contamination sampling and analysis introduced[^epa2002qapp-e10] |
| Reporting only nominal concentrations | ES&T requires measured concentrations[^estauthorguidelines-e6] |
| Copying the detection limit from the instrument manual | EPA's method detection limit must include all sample-processing steps and be determined in several batches[^epa2016mdl-e3][^epa2016mdl-e4] |
| Replacing every "non-detect" with half the reporting limit and then running a t-test | It can miss real differences and find differences that do not exist[^helsel2020statistical-e2] |
| Sample labels that say only "1, 2, 3," with no custody records | Samples get mixed up easily; if the data must serve as evidence, you cannot account for who handled them[^epa2002qapp-e6][^epa2002qapp-e8] |
| Sampling in a community and publicizing conclusions from unrepresentative data | According to Roy and Edwards (2019), such data caused unfounded fear in Flint[^roy2019citizen-e6] |

---

## Further reading

- **EPA QA/G-4, Guidance on Systematic Planning Using the Data Quality Objectives Process (2006)**: the full explanation of the seven DQO steps. Read it before your first sampling project.
- **EPA QA/G-5, Guidance for Quality Assurance Project Plans (2002)**: what to write in each element of a QAPP; the appendix explains terms such as quality control samples.
- **EPA, Definition and Procedure for the Determination of the Method Detection Limit, Revision 2 (2016)**: very short, and explains clearly how a method detection limit is determined.
- **Helsel et al., Statistical Methods in Water Resources (USGS, 2020)**: a statistics textbook for water resources data published by the US Geological Survey, free to read, including how to handle censored data. Read the relevant chapters before you analyze monitoring data.
- **EPA, Life Cycle Assessment: Principles and Practice (2006)**: an introduction to life cycle assessment.
- **ES&T author guidelines**: read them before you submit to ES&T, especially the list of requirements in the Journal Scope section.
- **ASCE Code of Ethics**: three pages on the responsibilities of ASCE members to society, the environment, clients, peers, and others.
- **Roy and Edwards 2019**: a participant's retrospective on community collaboration in the Flint crisis, useful if you want to do community-engaged research; keep in mind that it is one participating team's account.

[^epa2002qapp-e1]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Chapter 1, PDF p. 9. [Evidence](../../../sources/notes/epa2002qapp.md#e1)
[^epa2002qapp-e2]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Chapter 1, PDF p. 10. [Evidence](../../../sources/notes/epa2002qapp.md#e2)
[^epa2002qapp-e3]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Chapter 1, PDF p. 10. [Evidence](../../../sources/notes/epa2002qapp.md#e3)
[^epa2002qapp-e4]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Chapter 1, PDF p. 13. [Evidence](../../../sources/notes/epa2002qapp.md#e4)
[^epa2002qapp-e5]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element A6, PDF p. 25. [Evidence](../../../sources/notes/epa2002qapp.md#e5)
[^epa2002qapp-e6]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B3, PDF p. 36. [Evidence](../../../sources/notes/epa2002qapp.md#e6)
[^epa2002qapp-e7]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B3, PDF p. 36. [Evidence](../../../sources/notes/epa2002qapp.md#e7)
[^epa2002qapp-e8]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B3, PDF p. 36. [Evidence](../../../sources/notes/epa2002qapp.md#e8)
[^epa2002qapp-e9]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B5, PDF p. 39. [Evidence](../../../sources/notes/epa2002qapp.md#e9)
[^epa2002qapp-e10]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B5, PDF p. 39. [Evidence](../../../sources/notes/epa2002qapp.md#e10)
[^epa2002qapp-e11]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B5, PDF p. 39. [Evidence](../../../sources/notes/epa2002qapp.md#e11)
[^epa2002qapp-e12]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B5, PDF p. 39. [Evidence](../../../sources/notes/epa2002qapp.md#e12)
[^epa2002qapp-e13]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Element B5, PDF p. 39. [Evidence](../../../sources/notes/epa2002qapp.md#e13)
[^epa2002qapp-e14]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Appendix B glossary, PDF p. 71. [Evidence](../../../sources/notes/epa2002qapp.md#e14)
[^epa2002qapp-e15]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Appendix B glossary, PDF p. 72. [Evidence](../../../sources/notes/epa2002qapp.md#e15)
[^epa2002qapp-e16]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Appendix B glossary, PDF p. 69. [Evidence](../../../sources/notes/epa2002qapp.md#e16)
[^epa2002qapp-e17]: U.S. Environmental Protection Agency (EPA) 2002 (QA/G-5), Appendix B glossary, PDF p. 71. [Evidence](../../../sources/notes/epa2002qapp.md#e17)
[^epa2006dqo-e1]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Introduction, PDF p. 11. [Evidence](../../../sources/notes/epa2006dqo.md#e1)
[^epa2006dqo-e2]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Introduction, PDF p. 16. [Evidence](../../../sources/notes/epa2006dqo.md#e2)
[^epa2006dqo-e3]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Introduction, PDF p. 16. [Evidence](../../../sources/notes/epa2006dqo.md#e3)
[^epa2006dqo-e4]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Introduction, Figure 2. [Evidence](../../../sources/notes/epa2006dqo.md#e4)
[^epa2006dqo-e5]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Chapter 1, PDF p. 26. [Evidence](../../../sources/notes/epa2006dqo.md#e5)
[^epa2006dqo-e6]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Chapter 4, PDF p. 41. [Evidence](../../../sources/notes/epa2006dqo.md#e6)
[^epa2006dqo-e7]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Chapter 6, PDF p. 57. [Evidence](../../../sources/notes/epa2006dqo.md#e7)
[^epa2006dqo-e8]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Chapter 6, PDF p. 60. [Evidence](../../../sources/notes/epa2006dqo.md#e8)
[^epa2006dqo-e9]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Chapter 7, PDF p. 83. [Evidence](../../../sources/notes/epa2006dqo.md#e9)
[^epa2006dqo-e10]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Chapter 3, PDF p. 38. [Evidence](../../../sources/notes/epa2006dqo.md#e10)
[^epa2006dqo-e11]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Introduction, PDF p. 12. [Evidence](../../../sources/notes/epa2006dqo.md#e11)
[^epa2016mdl-e1]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), cover note. [Evidence](../../../sources/notes/epa2016mdl.md#e1)
[^epa2016mdl-e2]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), Definition. [Evidence](../../../sources/notes/epa2016mdl.md#e2)
[^epa2016mdl-e3]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), Scope and Application. [Evidence](../../../sources/notes/epa2016mdl.md#e3)
[^epa2016mdl-e4]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), Procedure (2)(b). [Evidence](../../../sources/notes/epa2016mdl.md#e4)
[^epa2016mdl-e5]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), Procedure (2)(b). [Evidence](../../../sources/notes/epa2016mdl.md#e5)
[^epa2016mdl-e6]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), Procedure (2)(e). [Evidence](../../../sources/notes/epa2016mdl.md#e6)
[^epa2016mdl-e7]: U.S. Environmental Protection Agency (EPA) 2016 (MDL Revision 2), Procedure (4)(a). [Evidence](../../../sources/notes/epa2016mdl.md#e7)
[^helsel2020statistical-e1]: Helsel et al. 2020 (U.S. Geological Survey (USGS)), §1.1. [Evidence](../../../sources/notes/helsel2020statistical.md#e1)
[^helsel2020statistical-e2]: Helsel et al. 2020 (U.S. Geological Survey (USGS)), §5.5. [Evidence](../../../sources/notes/helsel2020statistical.md#e2)
[^helsel2020statistical-e3]: Helsel et al. 2020 (U.S. Geological Survey (USGS)), §5.5. [Evidence](../../../sources/notes/helsel2020statistical.md#e3)
[^helsel2020statistical-e4]: Helsel et al. 2020 (U.S. Geological Survey (USGS)), §5.3.5. [Evidence](../../../sources/notes/helsel2020statistical.md#e4)
[^helsel2020statistical-e5]: Helsel et al. 2020 (U.S. Geological Survey (USGS)), §12.7. [Evidence](../../../sources/notes/helsel2020statistical.md#e5)
[^helsel2020statistical-e6]: Helsel et al. 2020 (U.S. Geological Survey (USGS)), §15.3. [Evidence](../../../sources/notes/helsel2020statistical.md#e6)
[^epa2006lca-e1]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 1. [Evidence](../../../sources/notes/epa2006lca.md#e1)
[^epa2006lca-e2]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 1. [Evidence](../../../sources/notes/epa2006lca.md#e2)
[^epa2006lca-e3]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 1. [Evidence](../../../sources/notes/epa2006lca.md#e3)
[^epa2006lca-e4]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 1. [Evidence](../../../sources/notes/epa2006lca.md#e4)
[^epa2006lca-e5]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 1, Limitations. [Evidence](../../../sources/notes/epa2006lca.md#e5)
[^epa2006lca-e6]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 1, Limitations. [Evidence](../../../sources/notes/epa2006lca.md#e6)
[^epa2006lca-e7]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 2. [Evidence](../../../sources/notes/epa2006lca.md#e7)
[^epa2006lca-e8]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 2, examples of functional units. [Evidence](../../../sources/notes/epa2006lca.md#e8)
[^epa2006lca-e9]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 2. [Evidence](../../../sources/notes/epa2006lca.md#e9)
[^epa2006lca-e10]: U.S. Environmental Protection Agency (EPA) 2006 (LCA: Principles and Practice), Chapter 4. [Evidence](../../../sources/notes/epa2006lca.md#e10)
[^estauthorguidelines-e1]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e1)
[^estauthorguidelines-e2]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e2)
[^estauthorguidelines-e3]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e3)
[^estauthorguidelines-e4]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e4)
[^estauthorguidelines-e5]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e5)
[^estauthorguidelines-e6]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e6)
[^estauthorguidelines-e7]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e7)
[^estauthorguidelines-e8]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e8)
[^estauthorguidelines-e9]: ES&T Author Guidelines, Journal Scope. [Evidence](../../../sources/notes/estauthorguidelines.md#e9)
[^estauthorguidelines-e10]: ES&T Author Guidelines, Article Types. [Evidence](../../../sources/notes/estauthorguidelines.md#e10)
[^estauthorguidelines-e11]: ES&T Author Guidelines, Article Types. [Evidence](../../../sources/notes/estauthorguidelines.md#e11)
[^estauthorguidelines-e12]: ES&T Author Guidelines, Cover Letter. [Evidence](../../../sources/notes/estauthorguidelines.md#e12)
[^estauthorguidelines-e14]: ES&T Author Guidelines, Research Data Policy. [Evidence](../../../sources/notes/estauthorguidelines.md#e14)
[^estauthorguidelines-e15]: ES&T Author Guidelines, Research Data Policy, Computer Codes. [Evidence](../../../sources/notes/estauthorguidelines.md#e15)
[^estauthorguidelines-e16]: ES&T Author Guidelines, Prior Publication Policy. [Evidence](../../../sources/notes/estauthorguidelines.md#e16)
[^estauthorguidelines-e17]: ES&T Author Guidelines, Theses/Dissertations. [Evidence](../../../sources/notes/estauthorguidelines.md#e17)
[^estauthorguidelines-e18]: ES&T Author Guidelines, Ethical Use of Animals or Human Participants in Research. [Evidence](../../../sources/notes/estauthorguidelines.md#e18)
[^asce2020code-e1]: ASCE Code of Ethics, Preamble. [Evidence](../../../sources/notes/asce2020code.md#e1)
[^asce2020code-e2]: ASCE Code of Ethics, 1a. [Evidence](../../../sources/notes/asce2020code.md#e2)
[^asce2020code-e3]: ASCE Code of Ethics, 1c. [Evidence](../../../sources/notes/asce2020code.md#e3)
[^asce2020code-e4]: ASCE Code of Ethics, 1g. [Evidence](../../../sources/notes/asce2020code.md#e4)
[^asce2020code-e6]: ASCE Code of Ethics, 4b. [Evidence](../../../sources/notes/asce2020code.md#e6)
[^asce2020code-e7]: ASCE Code of Ethics, 4e. [Evidence](../../../sources/notes/asce2020code.md#e7)
[^asce2020code-e8]: ASCE Code of Ethics, 4f. [Evidence](../../../sources/notes/asce2020code.md#e8)
[^asce2020code-e10]: ASCE website, Code of Ethics overview page. [Evidence](../../../sources/notes/asce2020code.md#e10)
[^epa2024environmentaljustice-e1]: U.S. Environmental Protection Agency (EPA) environmental justice web page (2024 snapshot), definition paragraph. [Evidence](../../../sources/notes/epa2024environmentaljustice.md#e1)
[^epa2024environmentaljustice-e2]: U.S. Environmental Protection Agency (EPA) environmental justice web page (2024 snapshot), definition paragraph. [Evidence](../../../sources/notes/epa2024environmentaljustice.md#e2)
[^roy2019citizen-e1]: Roy & Edwards 2019, Introduction. [Evidence](../../../sources/notes/roy2019citizen.md#e1)
[^roy2019citizen-e2]: Roy & Edwards 2019, Uncovering the Flint Water Crisis through Citizen Science. [Evidence](../../../sources/notes/roy2019citizen.md#e2)
[^roy2019citizen-e3]: Roy & Edwards 2019, Uncovering the Flint Water Crisis through Citizen Science. [Evidence](../../../sources/notes/roy2019citizen.md#e3)
[^roy2019citizen-e4]: Roy & Edwards 2019, Characteristics of quality citizen science projects. [Evidence](../../../sources/notes/roy2019citizen.md#e4)
[^roy2019citizen-e5]: Roy & Edwards 2019, Persistent attacks on merited expertise. [Evidence](../../../sources/notes/roy2019citizen.md#e5)
[^roy2019citizen-e6]: Roy & Edwards 2019, Abstract. [Evidence](../../../sources/notes/roy2019citizen.md#e6)
[^epa2026caddis-e1]: U.S. Environmental Protection Agency (EPA) CADDIS website, Basic Information About CADDIS. [Evidence](../../../sources/notes/epa2026caddis.md#e1)
[^epa2026caddis-e2]: U.S. Environmental Protection Agency (EPA) CADDIS website, About Causal Assessment. [Evidence](../../../sources/notes/epa2026caddis.md#e2)
[^epa2026caddis-e3]: U.S. Environmental Protection Agency (EPA) CADDIS website, About Causal Assessment. [Evidence](../../../sources/notes/epa2026caddis.md#e3)
[^epa2026caddis-e4]: U.S. Environmental Protection Agency (EPA) CADDIS website, About Causal Assessment, Weighing of Evidence. [Evidence](../../../sources/notes/epa2026caddis.md#e4)
[^epa2026caddis-e5]: U.S. Environmental Protection Agency (EPA) CADDIS website, About Causal Assessment, Rejection. [Evidence](../../../sources/notes/epa2026caddis.md#e5)
[^epa2026caddis-e6]: U.S. Environmental Protection Agency (EPA) CADDIS website, Step 5. Identify Probable Causes. [Evidence](../../../sources/notes/epa2026caddis.md#e6)
[^epa2026caddis-e7]: U.S. Environmental Protection Agency (EPA) CADDIS website, Step 5. Identify Probable Causes. [Evidence](../../../sources/notes/epa2026caddis.md#e7)
[^epa2026caddis-e8]: U.S. Environmental Protection Agency (EPA) CADDIS website, About Scoring the Evidence. [Evidence](../../../sources/notes/epa2026caddis.md#e8)
[^epa2026caddis-e9]: U.S. Environmental Protection Agency (EPA) CADDIS website, Step 5. Identify Probable Causes. [Evidence](../../../sources/notes/epa2026caddis.md#e9)
[^cee2022guidelines-e1]: Collaboration for Environmental Evidence 2022 (version 5.1), §1.1. [Evidence](../../../sources/notes/cee2022guidelines.md#e1)
[^cee2022guidelines-e2]: Collaboration for Environmental Evidence 2022 (version 5.1), §9.2. [Evidence](../../../sources/notes/cee2022guidelines.md#e2)
[^haddaway2018roses-e2]: Haddaway et al. 2018, Abstract. [Evidence](../../../sources/notes/haddaway2018roses.md#e2)
[^haddaway2018roses-e4]: Haddaway et al. 2018, Key differences between ROSES and PRISMA, p. 5. [Evidence](../../../sources/notes/haddaway2018roses.md#e4)
[^haddaway2018roses-e5]: Haddaway et al. 2018, Background, p. 4. [Evidence](../../../sources/notes/haddaway2018roses.md#e5)
[^cee2022guidelines-e3]: Collaboration for Environmental Evidence 2022 (version 5.1), §9.1. [Evidence](../../../sources/notes/cee2022guidelines.md#e3)
[^cee2022guidelines-e5]: Collaboration for Environmental Evidence 2022 (version 5.1), §9.3. [Evidence](../../../sources/notes/cee2022guidelines.md#e5)
[^cee2022guidelines-e6]: Collaboration for Environmental Evidence 2022 (version 5.1), §9.3.1. [Evidence](../../../sources/notes/cee2022guidelines.md#e6)
[^mokoena2026adsorption-e1]: Mokoena et al. 2026, Methods. [Evidence](../../../sources/notes/mokoena2026adsorption.md#e1)
[^mokoena2026adsorption-e2]: Mokoena et al. 2026, Searching for articles. [Evidence](../../../sources/notes/mokoena2026adsorption.md#e2)
[^mokoena2026adsorption-e3]: Mokoena et al. 2026, Study validity assessment. [Evidence](../../../sources/notes/mokoena2026adsorption.md#e3)
[^mokoena2026adsorption-e4]: Mokoena et al. 2026, Study validity assessment. [Evidence](../../../sources/notes/mokoena2026adsorption.md#e4)
[^bjork2013publishing-e1]: Björk & Solomon 2013, Abstract. [Evidence](../../../sources/notes/bjork2013publishing.md#e1)
[^bjork2013publishing-e2]: Björk & Solomon 2013, §2 Methods. [Evidence](../../../sources/notes/bjork2013publishing.md#e2)
[^bjork2013publishing-e3]: Björk & Solomon 2013, §3 Results. [Evidence](../../../sources/notes/bjork2013publishing.md#e3)
[^bjork2013publishing-e4]: Björk & Solomon 2013, Appendix, table "Publication Time in Months by Discipline". [Evidence](../../../sources/notes/bjork2013publishing.md#e4)
[^bjork2013publishing-e5]: Björk & Solomon 2013, §4 Discussion. [Evidence](../../../sources/notes/bjork2013publishing.md#e5)
