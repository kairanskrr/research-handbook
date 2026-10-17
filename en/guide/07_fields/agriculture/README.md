# Agriculture, forestry, and fisheries: field overview

This page explains how research actually runs in agronomy, crop science, soil science, horticulture, forestry, fisheries, and aquaculture: why field trials follow the seasons, why they are repeated across sites and years, how to run on-farm trials with farmers, how field trials are designed, analyzed, and reported, and how data are organized and shared. Field 4.5, "Other agricultural sciences", in the Organisation for Economic Co-operation and Development (OECD) classification is covered here too. Animal and dairy science, veterinary science, and agricultural biotechnology are not covered. For cell and molecular work in the lab, see the [Biological sciences page](../biological-sciences/README.md); for field observation and environmental processes, see the [Earth and environmental sciences page](../earth-environmental-sciences/README.md); for what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). This page covers only what is specific to this field; for the research strategies the field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). Every rule and practice cited here names its source: the publications handbook and journal policies of the American Society of Agronomy (ASA), the Crop Science Society of America (CSSA), and the Soil Science Society of America (SSSA) (together called "the Tri-Societies" below), fish research guidelines written by the American Fisheries Society and others, the long-term experiments at Rothamsted Research in the UK, and the data policy of CGIAR (formerly the Consultative Group on International Agricultural Research). These are the rules of particular countries and institutions, not worldwide conventions. If you do research in China or anywhere else, follow your local authorities, your funder, and your target journal.

**After reading this page, you should be able to:**

- explain why field trials are slow, why they span sites and years, and how on-farm trials differ from research-station trials;
- identify the experimental unit, tell true replication from pseudoreplication, and know what blocking and randomization each do;
- describe your experimental design and statistical methods the way your target journal requires, and organize field records according to a metadata standard;
- name the research strategies field research commonly uses, and what evidence and standards each one is judged by;
- avoid the mistakes newcomers commonly make in designing field trials, working with farmers, and writing papers.

---

## How research works in this field

### Field trials follow the seasons

Many field trials follow the crop's growing season: you plant an annual crop and have no yield data until harvest, so you often get only one round a year. This sets the pace of the field:

- **Data take years to accumulate.** A 2020 review by Kool and colleagues analyzed 172 papers on on-farm trials in sub-Saharan Africa published between 1986 and 2015[^kool2020reproducibility-e1]. These trials often ran over several seasons, generally 2 to 3[^kool2020reproducibility-e6]. A paper can also be sent back because it is "one year of data short": the Tri-Societies' publications handbook gives the example that such a manuscript can be resubmitted once the missing data are collected and added[^asa2024style-e5].
- **A design mistake costs you a whole year.** This page cites Casler's 2015 review of experimental design in *Agronomy Journal* in many places. He points out that when the P value is high (the result is not significant), you often cannot tell what went wrong, the results often cannot be published, and the time and money are wasted[^casler2015fundamentals-e23]. So put extra care into the design before you start.
- **A lot can go wrong in the field.** Casler lists disturbances his colleagues' trials have survived, rescued by a randomized complete block design: military maneuvers, a house mover, wayward herbicide sprayers, a motorcycle gang, a vengeful former employee, and partying students[^casler2015fundamentals-e15].

### Multiple sites, multiple years

It is very common to repeat the same trial across several sites and years to see how treatments perform in different environments[^casler2015fundamentals-e9]. The reason is that a treatment often works differently in different environments (statistically, a treatment-by-environment interaction). Casler worked this out with variance components: relative to the number of replicates at each site, you should give priority to adding sites and years. Adding replicates first only pays off when there is no treatment-by-environment interaction at all, which is rare[^casler2015fundamentals-e8].

### Long-term experiments

Some questions (soil fertility, carbon stocks, climate effects) take decades to answer, and for these you need long-term experiments. One example is Rothamsted Research in the UK. Here is how it describes itself on its website:

- It runs the oldest agricultural field experiments in the world that are still going, and 7 of its long-term experiments continue today[^rothamstedlte-e1]. They were set up between 1843 and 1856; some failed and were stopped because of poor soil structure or crop disease[^rothamstedlte-e2]. Nor are they frozen in time: the institute carefully changes management every 5 to 10 years to keep the experiments relevant[^rothamstedlte-e3].
- It has kept more than 300,000 samples, and analyzing old samples with new methods shows changes over 180 years[^rothamstedlte-e4]. Many records that existed only on paper have been turned into a usable database[^rothamstedlte-e6].
- If you are an outside researcher and want to use these experiments or samples, you first discuss it with a Rothamsted collaborator and then submit a sampling request form[^rothamstedlte-e5].
- Long-term data have another use for a newcomer. Casler points out that researchers who have accumulated many years of results at the same site have plenty of data to plan new trials with[^casler2015fundamentals-e22]. When you join a group, ask your advisor whether the group or the research station keeps records of past trials.

### How forestry and fisheries differ

- **Forestry**: trees live a long time, so one experiment can run for many years, and you often take over an experiment someone else started. According to Casler, incomplete block designs (each block holds only some of the treatments) are common in tree breeding programs, because these programs are mostly in mountainous areas with almost no flat land[^casler2015fundamentals-e25]. Version 1.1 of the plant phenotyping metadata standard MIAPPE (Minimum Information About a Plant Phenotyping Experiment; see "Data standards and sharing" below) extended its scope to perennial and woody plants[^papoutsoglou2020enabling-e5].
- **Fisheries and aquaculture**: fish are vertebrates. The following points come from fish research guidelines written jointly in 2014 by the American Fisheries Society and two other US scientific societies. In the US, institutions that do research with vertebrates must have an Institutional Animal Care and Use Committee (IACUC), which reviews and oversees the institution's use of animals[^afs2014fishes-e3]. Researchers must know the relevant regulations and biosecurity issues and obtain all required permits[^afs2014fishes-e4]. Research outside the US must follow the host country's wildlife regulations[^afs2014fishes-e5]. A study should use the smallest number of animals that can reliably answer the question[^afs2014fishes-e2]. Fish collected from the wild and brought into the lab should never be released back into the wild; this is the general consensus of the agencies that issue scientific collecting permits[^afs2014fishes-e6]. For the 3Rs of animal research and the reporting guidelines, see the [Biological sciences page](../biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines).

### Publishing: the Tri-Societies' journals as an example

Below are the policies of the Tri-Societies' journals; for other journals, follow their own instructions for authors. Our sources do not cover authorship-order conventions or review turnaround times; for general principles of authorship, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md):

- **Review**: most of the journals use single-blind review (authors do not know who the reviewers are); a few use double-blind review (neither side knows who the other is)[^asa2024style-e6].
- **Preprints**: you may post to a nonprofit preprint server, but you must cite the preprint when you submit[^sciencesocietieseditorial-e3].
- **Data**: you must preserve and provide the data needed to understand and evaluate the paper's results, in a recognized, community-accessible repository for your field[^sciencesocietieseditorial-e1]; data not deposited in a repository should be available from the authors on request[^sciencesocietieseditorial-e2].
- **Ethics**: authors must properly acknowledge other people's work and ideas[^sciencesocietieseditorial-e4], and consider whom their research benefits and whom it neglects[^sciencesocietieseditorial-e5].

---

## How this field differs from others

The table below compares this field with computer science and lab biology. The computer science column draws on the [Computer science page](../computer-science/README.md) and the biology column on the [Biological sciences page](../biological-sciences/README.md). The table as a whole is our own summary; cells with footnotes are supported by this page's sources.

| | Agriculture, forestry, and fisheries | Lab biology | Computer science |
|---|---|---|---|
| How long one round takes | Often tied to the growing season; the African on-farm trials in Kool and colleagues' 2020 review generally spanned 2 to 3 seasons[^kool2020reproducibility-e6] | Can be long; see the Biological sciences page | Many experiments can be rerun quickly |
| Experimental unit | Often a plot, a tank, or a farm | Often an animal or an independent culture | Often counted by random seed or dataset |
| Environment | Weather and soil differ every year and at every site, so trials often span sites and years[^casler2015fundamentals-e9] | Lab conditions can be controlled | The computing environment can be fixed |
| Who you work with | On-farm trials involve farmers and extension staff[^casler2015fundamentals-e11] | Mostly within the lab group | Mostly within the research group |
| Publishing | Our sources cover only journals; the Tri-Societies' journals accept manuscripts that were posted as preprints[^sciencesocietieseditorial-e3] | Journals; the bioRxiv preprint server | Conferences dominate in most subfields |

---

## Designing field trials

Casler reduces experimental design to four pillars: replication, randomization, blocking, and the size of the experimental unit. Each one has to be a deliberate decision[^casler2015fundamentals-e1].

### Fix the experimental unit before you think about replication

The [Biological sciences page](../biological-sciences/README.md#identify-the-experimental-unit-before-you-count-n) already covers experimental units, the two kinds of "replicates", and how to count n; the same logic applies here. For field trials, start with two points:

- The **experimental unit** is the smallest unit to which a treatment is applied[^casler2015fundamentals-e2]. If fertilizer is applied to a plot, the plot is the experimental unit; the several soil cores or plants you sample within that plot are only observational units.
- **Replication** must happen at the same spatial and temporal scale at which the treatment is applied[^casler2015fundamentals-e4].

The difference from the lab is that in the field the experimental unit is often a piece of land, a farm, or even a year: large, expensive, and hard to multiply.

### Pseudoreplication: treatment confounded with the plot

**Pseudoreplication** means using statistical tests of a treatment effect when the treatments are not truly replicated, or when the replicates are not statistically independent[^davies2015pseudoreplication-e1]. Casler gives a field example: take only two 1-hectare grassland plots, burn one, and leave the other unburned as a control. The statistical analysis itself is not wrong, but the science is flawed, and the design cannot give an unambiguous interpretation of the result[^casler2015fundamentals-e5]. According to Casler, the term "pseudoreplication" was coined by Hurlbert in 1984 to describe exactly this situation, where treatment and experimental unit are completely confounded[^casler2015fundamentals-e6]. The same holds in fisheries research: the guidelines from the American Fisheries Society and others state that treating multiple samples from one experimental unit as multiple experimental units is pseudoreplication[^afs2014fishes-e1].

Casler offers two remedies[^casler2015fundamentals-e7]: **replicate in space**, burning and not burning on several pieces of land, with each prairie treated as a block; or **replicate in time**, running the experiment across years, but re-randomizing the treatments every year, which means starting over on new land each year.

> **Where sources disagree: how strictly should pseudoreplication be policed?**
>
> - **Strict view**: Casler and the American Fisheries Society guidelines both treat pseudoreplication as an error to avoid at the design stage[^casler2015fundamentals-e6][^afs2014fishes-e1].
> - **Lenient view**: in a 2015 paper, the ecologists Davies and Gray argue that the concept is applied too dogmatically and often gets papers rejected in review[^davies2015pseudoreplication-e2]. Their own online survey received 103 responses; 58% of respondents had faced research questions where they felt pseudoreplication was unavoidable[^davies2015pseudoreplication-e5]. They point out that expensive, large-scale (landscape-scale) manipulations and natural experiments in which a chance event happens at only one site are inherently hard to replicate[^davies2015pseudoreplication-e6]. They recommend defining the hypothesis and the population of interest clearly, acknowledging the limits of statistical inference, and using statistical approaches such as nesting and random effects[^davies2015pseudoreplication-e3]. Before a reviewer alleges pseudoreplication, the reviewer should also show that the allegation holds[^davies2015pseudoreplication-e4].
> - **Our suggestion**: if you can design in true replication, do it. If you really cannot (for example, there is only one watershed), say clearly in the paper what the experimental unit is and how far the conclusion can be generalized, and do not present the number of samples as the number of replicates.

### Blocking and randomization

- **Blocking** has two uses (the points in this subsection all come from Casler 2015): grouping experimental units with similar conditions to improve precision, and practical convenience, so that one factor can be applied to larger plots[^casler2015fundamentals-e14].
- **A field that looks uniform is usually not**, and it takes years of experience to predict its pattern of spatial variation[^casler2015fundamentals-e19]. So you can block in two directions, in case you guessed the blocking direction wrong[^casler2015fundamentals-e17]. With more than 20 treatments, more and smaller blocks are almost always more efficient than complete blocks[^casler2015fundamentals-e18].
- **Randomization is insurance**: it ensures that unknown or unexpected sources of variation do not introduce bias or confounding[^casler2015fundamentals-e13].
- **Split-plot designs** are often chosen for convenience: factors such as tillage, irrigation, or planting date need larger plots, so they go on the main plots[^casler2015fundamentals-e16]. Main plots and subplots in a split-plot design have different precision, and the analysis must use different error terms for them.

### Sites, years, and power analysis

- Add sites and years first; the number of replicates comes second[^casler2015fundamentals-e8]. Casler also recommends designing so that blocking factors (years, for example) can be treated as **random effects**, meaning each block is regarded as a random draw from a larger population[^casler2015fundamentals-e24]. Only then can the conclusions possibly extend to sites and years you did not test.
- As long as you do not attribute an interaction to an environmental variable that was not replicated, you are unlikely to be criticized[^casler2015fundamentals-e9]. For example, if a variety does well at site A and poorly at site B, you cannot conclude "because site A gets more rain" unless rainfall itself was replicated.

**Do a power analysis before you start.** **Statistical power** is the probability that your trial will detect a treatment difference when one really exists. From his teaching and consulting experience, Casler believes that few agronomic researchers have seriously used power analysis to design better experiments[^casler2015fundamentals-e10]. He recommends doing one every time you design an experiment, even if you have to guess the parameters[^casler2015fundamentals-e21]. For how to design a study, see the Part 2 chapter [From research questions to an evidence plan](../../02_do-the-project/01_question-to-evidence.md).

---

## Statistical analysis and reporting

The Tri-Societies' publications handbook requires that readers be able to understand how an experiment was designed and conducted, so they can judge whether the results are credible[^asa2024style-e9]. According to the handbook:

- The methods section must describe blocking, different experimental unit sizes (as in split plots and strip plots), the number of sites and years, the number of replicates, field or greenhouse conditions, and how each trait was measured[^asa2024style-e1].
- **When the experimental unit and the sampling unit differ, describe both**, so readers can see how many experimental units were used and how many samples were taken from each[^asa2024style-e2].
- Report **standard errors or confidence intervals** for all data used to draw conclusions[^asa2024style-e3].
- Measurements taken on the same experimental material at different positions or times are **often correlated** (not independent)[^asa2024style-e4], so use statistical methods that can handle that correlation.
- Give details for unusual designs or statistical methods[^asa2024style-e8]; table titles generally state the crop or soil, the main variable, the site, and the year[^asa2024style-e7].

**On-farm trials have especially many reporting problems.** The review of 172 African on-farm trial papers by Kool and colleagues mentioned above found that it is often difficult or impossible to reconstruct the experimental design from the paper. Nutrient management, weed management, and crop information were described best; land preparation, field history, and pest and water management were rarely described[^kool2020reproducibility-e2]. Quite a few studies described their field practices in unclear, vague terms[^kool2020reproducibility-e8]. For general statistical practice, see the Part 2 chapter section [Report how big the difference is and how sure you are, not just the p-value](../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

---

## Data standards and sharing

Field data are hard to use once separated from the context of the trial. Papoutsoglou and colleagues noted in 2020 that plant phenotyping data are especially hard to reuse and combine, because experimental sites, plants, data types, and experimental designs all vary[^papoutsoglou2020enabling-e1]. They give an example: the raw data were not organized to any standard, so whoever reused them had to piece together the metadata by hand from scattered text descriptions[^papoutsoglou2020enabling-e2].

**Metadata** are data about the data: where, when, with what material, and how it was measured. A **metadata standard** lists the fields needed to interpret data from a given kind of experiment[^papoutsoglou2020enabling-e7]. The standard for plant phenotyping is **MIAPPE** (Minimum Information About a Plant Phenotyping Experiment). According to the paper, it was the first and at the time the only community metadata standard in the field[^papoutsoglou2020enabling-e3]. One of its guiding principles is to reduce the chance that researchers leave important information out when recording an experiment[^papoutsoglou2020enabling-e4]. Its "event" item is especially useful: record anything that affected the experiment at a point in time, both field operations such as sowing or fungicide application and unplanned events such as rainfall or pathogen infection[^papoutsoglou2020enabling-e6]. Even if your target journal does not require it, you can use its fields to structure your field records. For general advice on organizing data, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

**Open sharing: CGIAR as an example.** CGIAR treats its research outputs as international public goods that should benefit the poor, especially smallholder farmers in developing countries[^cgiar2021fair-e1]. It commits to making its outputs as open as possible and findable, accessible, interoperable, and reusable (together, the FAIR principles)[^cgiar2021fair-e2]. Its 2021 data policy has some concrete requirements:

- Write a data management plan when the project starts[^cgiar2021fair-e4].
- Deposit datasets in a suitable repository and make them public no later than 12 months after data collection ends or 6 months after publication of the results that use the data, whichever comes first[^cgiar2021fair-e3].
- Data may be kept closed only when there is a contractual obligation such as a confidentiality agreement[^cgiar2021fair-e6]; data management must take privacy and ethics into account[^cgiar2021fair-e5]. This is one institution's rule; your funder and journal may require something different, and their rules take precedence.

---

## Doing research with farmers

**On-farm research** is experimentation in farmers' own fields. Kool and colleagues point out that a **research station** is a highly controlled environment where you can study treatments while holding other conditions constant. In farmers' fields, researchers have much less control, and the experiment sits within a much wider and more variable biophysical and socioeconomic environment[^kool2020reproducibility-e5]. So whether research-station conclusions carry over to farmers' fields has to be tested specifically. In 2019 *Agronomy Journal* published a special issue on on-farm research, introduced by Kyveryga of the Iowa Soybean Association in the US. He writes that on-farm research has expanded rapidly over the past two decades, especially in developed countries, because precision agriculture technology has become more widely used[^kyveryga2019onfarm-e1]: equipment such as yield monitors and satellite navigation lets farmers and researchers run trials at whole-field scale, at many sites, and at much lower cost[^kyveryga2019onfarm-e2].

- **Find out why farmers take part.** According to the introduction, one study in the special issue conducted in-depth interviews with 40 participants in the Nebraska On-Farm Research Network in the US. Farmers ran on-farm trials mainly to increase profit, out of curiosity, and because they wanted unbiased results[^kyveryga2019onfarm-e3]; they also wanted to be more involved in every stage of the trials[^kyveryga2019onfarm-e4].
- **If farmers don't want replication, change the design.** Casler points out that farmers and extension staff are willing to try new treatments on a large scale but see little value in replication. You can use multiple farms as blocks, or intersperse control plots among the other treatments, ideally in an every-other-plot pattern[^casler2015fundamentals-e11]. Another option is **mother and daughter trials**: the research station runs a "mother" trial with proper replication and randomization, and many farmers each run a "daughter" trial[^casler2015fundamentals-e12].
- **Spell out what the "farmer practice" actually is.** Kool and colleagues found that on-farm trials often use "farmer practice" as the control but assume it is the same everywhere and known to the reader[^kool2020reproducibility-e3].
- **State who your conclusions apply to.** The same review found that most of the studies analyzed did not make clear which farmers and which environments their conclusions apply to[^kool2020reproducibility-e4]. The authors recommend at least answering under what conditions the effect occurs and for whom it is relevant, and making public the criteria used to select sites, farmers, and fields[^kool2020reproducibility-e7].
- **Take the results back to farmers.** Kyveryga considers it one of the keys of on-farm research to analyze and summarize the results well and present them to farmers and agronomists[^kyveryga2019onfarm-e5].

Interviews, questionnaires, and other research involving people generally also need ethics review; follow your institution's rules. See [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md) and [Collaboration and advisors](../../08_throughout/collaboration_and_advisors.md) in Throughout the project.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists only the five strategies this page's sources support. The grouping and the "What it looks like in this field" column are our own summary. Each standard represents only the source cited in its footnote: the last three rows each rest on one or two sources and describe the practice or recommendation of a particular project or paper, not rules accepted across the field.

| Strategy | What it looks like in this field | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Apply treatments such as fertilizer or tillage to plots and estimate the treatment effect | Replication, randomization, blocking, and experimental unit size are all deliberate decisions[^casler2015fundamentals-e1]; replication is at the same scale as treatment application[^casler2015fundamentals-e4]; randomization keeps unknown sources of variation from causing bias and confounding[^casler2015fundamentals-e13]; standard errors or confidence intervals are reported for data used to draw conclusions (Tri-Societies' journals)[^asa2024style-e3] | [Field trials](practices/field_trial.md) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Repeat the same trial across sites and years to compare varieties, technologies, or other treatments across environments[^casler2015fundamentals-e9]; compare a new practice with the "farmer practice" in farmers' fields[^kool2020reproducibility-e3] | Add sites and years before adding replicates[^casler2015fundamentals-e8]; do not attribute interactions to unreplicated environmental variables[^casler2015fundamentals-e9]; in on-farm trials, do not assume the "farmer practice" is common knowledge[^kool2020reproducibility-e3], and state under what conditions the effect occurs and for whom it is relevant[^kool2020reproducibility-e7] | [Field trials: multi-environment trials](practices/field_trial.md#step-7-multi-environment-trials), [Field trials: on-farm trials](practices/field_trial.md#step-8-run-on-farm-trials-with-farmers) |
| [Building and improving](../../05_research-strategies/build_improve.md) | Develop, calibrate, and improve crop models and use them to predict crop performance at new sites and in new years. Taking phenology models (which predict crop development stages) as an example, there are two routes to improvement: change the model structure, or change the calibration[^wallach2023proposal-e7] | Crop models almost always need calibration (adjusting parameters with observed data), because a model is only an approximation[^wallach2023proposal-e2]. There is no consensus on how to calibrate phenology models, and teams given the same data calibrate very differently[^wallach2023proposal-e1][^wallach2023proposal-e5]. The evaluation approach in a 2023 wheat phenology study from the Agricultural Model Intercomparison and Improvement Project (AgMIP): the evaluation data share no sites or years with the calibration data and are withheld from the modelers[^wallach2023proposal-e3]; errors are compared with a simple benchmark model[^wallach2023proposal-e6]; a documentation table is filled in for every calibration step[^wallach2023proposal-e4]. The 2013 paper by Rosenzweig and colleagues introducing AgMIP's overall plan set these practices for crop modeling teams: evaluate models by comparing their output with observed growth and yield data[^rosenzweig2013agricultural-e1]; run multiple models for the same crop and use the spread of their results to estimate crop model uncertainty[^rosenzweig2013agricultural-e2]; document both parameter calibration and code improvements[^rosenzweig2013agricultural-e3]. In that paper's wheat pilot near Obregón, Mexico, 5 crop models and 5 global climate models simulated mid-century yields: under the A2 emissions scenario, 88% of the variance in simulated yield came from differences among crop models and only 10% from differences among climate models[^rosenzweig2013agricultural-e4]. AgMIP's 2013 protocols recommend that experiments for model improvement collect weather, soil, and crop data together[^boote2013protocols-e1] and archive them for future researchers[^boote2013protocols-e2] | [Quantitative simulation: calibrate and hold out evaluation data](../../06_methods/simulation_study.md#step-4-calibrate-with-real-data-and-hold-some-data-back-for-testing) |
| [Description](../../05_research-strategies/observe_describe.md) | Use farm household surveys to collect plot area, inputs, and outputs, describe agricultural production, and analyze relationships in it, for example between farm size and yield per unit area[^carletto2013guesstimates-e8] | A 2013 working paper by World Bank researchers used Living Standards Measurement Study–Integrated Surveys on Agriculture (LSMS-ISA) data from four countries: Malawi, Uganda, Tanzania, and Niger[^carletto2013guesstimates-e7]. Findings: farmers' self-reported plot areas contain errors, and those errors may be correlated with agricultural outcomes[^carletto2013guesstimates-e1]; small plots are over-reported and large plots under-reported[^carletto2013guesstimates-e2]; adding control variables does not fix this[^carletto2013guesstimates-e3]. Measuring the plot by walking it with tape and compass is the gold standard, but national surveys cannot afford it[^carletto2013guesstimates-e5]; GPS is not perfect on small plots either, but its errors may be less related to agricultural outcomes[^carletto2013guesstimates-e6], and the authors argue for making GPS area measurement a routine part of surveys[^carletto2013guesstimates-e4] | [Questionnaire surveys](../../06_methods/questionnaire_survey.md), [Interview studies](../../06_methods/interview_study.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Pool published field trials in a meta-analysis (combining data from multiple studies statistically) to address highly contested questions such as organic agriculture and conservation agriculture[^krupnik2019does-e6] | In 2019, researchers from the International Maize and Wheat Improvement Center (known by its Spanish acronym, CIMMYT) and other institutions proposed three recommendations for judging meta-analyses: look at how the papers and data were collected; look at the rationale for the research question, how the farming systems are defined, and the scale to which conclusions are extrapolated[^krupnik2019does-e1]; and interpret more conservatively when the topic is highly politicized[^krupnik2019does-e2]. They point out that reducing farmers' diverse management practices to categories that can be analyzed statistically is a central difficulty of agronomic meta-analysis[^krupnik2019does-e5]; plot and research-station trials may not represent whole fields or whole farms[^krupnik2019does-e3]; and "global average" results detached from specific farming systems are hard to use for guiding policy and farmers' practice[^krupnik2019does-e4] | [Review studies](../../06_methods/review_study.md), [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md) (health research as the example) |

How to use this table: a single field trial often combines the first two strategies, for example comparing several varieties while also estimating the effect of nitrogen rate. Choose the main strategy based on the claim you most want to support; whichever you choose, the requirements for experimental units, replication, and randomization are the same. If your crop model or meta-analysis uses field trial data, the requirements in the first two rows also decide whether those data can be trusted.

Two things the table does not include:

- **Measurement: this page found only requirements on how to describe methods.** The Tri-Societies' publications handbook requires that materials and methods be described in enough detail for a competent scientist to repeat the work[^asa2024style-e12]; that preparation methods, equipment, and measurements be described, using units accepted by the International System of Units (SI)[^asa2024style-e13]; that when a product must be identified by trade name, the manufacturer or main distributor be given in parentheses at first mention[^asa2024style-e14]; and that how each trait was measured be stated[^asa2024style-e1]. Our sources do not cover how a measurement method itself must be validated to count as reliable, or the standards of evidence for the other strategies.
- **Reporting standards for systematic reviews: this page found none specific to agriculture; the closest is ROSES, from environmental research.** ROSES (RepOrting standards for Systematic Evidence Syntheses) is a set of reporting forms and a flow diagram designed by Haddaway and colleagues in 2018 for systematic reviews and systematic maps (another form of evidence synthesis alongside systematic reviews) in conservation and environmental management[^haddaway2018roses-e2]. They proposed it because PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) was developed for healthcare reviews and has limitations in this field, for example an overemphasis on meta-analysis[^haddaway2018roses-e1]. ROSES has two forms, one for the protocol and one for the final report, plus a flow diagram template[^haddaway2018roses-e3]. Unlike PRISMA, beyond a checklist it also asks for summary information on each key step of the review[^haddaway2018roses-e4], such as the total number of search results before duplicates are removed[^haddaway2018roses-e5]. It focuses on searching, screening, data extraction, and critical appraisal, and says less about the final synthesis[^haddaway2018roses-e6]. Its forms are much longer than PRISMA's and take more time to fill in, so the authors recommend starting early[^haddaway2018roses-e7]. At least one agricultural journal explicitly requires it: the 2025 submission guidelines of *CABI Agriculture and Bioscience*, published by CABI, state that the journal accepts systematic reviews and systematic maps conducted according to a predefined protocol[^cabiagbioevidencesynthesis-e1], and that all such submissions must include ROSES forms[^cabiagbioevidencesynthesis-e2]. It also recommends making the protocol public before starting the review, for example on the agricultural preprint server agriRxiv[^cabiagbioevidencesynthesis-e3]. For other agricultural journals, follow whatever reporting standard the target journal requires.

## Research methods common in this field

Specific to this field: [Field trials](practices/field_trial.md). Of the cross-field research types, the following are commonly used; the judgments about which methods are "related" are our own summary. Long-term experiments are related to [Longitudinal studies](../../06_methods/longitudinal_study.md), but their subjects are soils and crops. On-farm trials and participatory research are related to [Action research](../../06_methods/action_research.md), but usually still have controls and replication. For field surveys, see [Field studies: observation and sampling](../../06_methods/field_study.md); for crop models, see [Quantitative simulation](../../06_methods/simulation_study.md); for analyzing phenotyping and remote sensing data, see [Data science](../../06_methods/data_science.md), and take particular care to document field metadata; for farm household surveys and interviews, see [Questionnaire surveys](../../06_methods/questionnaire_survey.md) and [Interview studies](../../06_methods/interview_study.md); for pooling published trials, see [Review studies](../../06_methods/review_study.md) and [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md).

---

## Advice for newcomers

1. **Before you start, learn experimental design and analysis properly, or find a collaborator who knows them.** This is the first piece of advice Casler gives young researchers[^casler2015fundamentals-e20].
2. **Draw the levels of your experiment and mark the experimental unit.** Show which level each of site, year, block, plot, and sample sits at; replication must happen at the level where the treatment is applied[^casler2015fundamentals-e4]. Then do a power analysis, even if you can only guess the parameters[^casler2015fundamentals-e21].
3. **Start small.** At first, design small experiments with experimental units as large as your labor and machinery can handle[^casler2015fundamentals-e26].
4. **Sites and years take priority over the number of replicates**[^casler2015fundamentals-e8]; budget two or three seasons in your plan.
5. **Record field operations and unplanned events on the day they happen, following a metadata standard**: put a date on sowing, spraying, rainfall, and disease[^papoutsoglou2020enabling-e6].
6. **When working with farmers, first find out why they are taking part, and involve them at every stage.** In the Nebraska interview study of 40 participants mentioned above, farmers themselves asked for this[^kyveryga2019onfarm-e3][^kyveryga2019onfarm-e4].

---

## Common mistakes

| Mistake (examples written by us) | Why it is a problem |
|---|---|
| One fertilized plot and one unfertilized plot, 20 soil samples from each, reported as n = 20 | Treatment and plot are completely confounded: this is pseudoreplication[^casler2015fundamentals-e6]; multiple samples from one experimental unit are not multiple experimental units[^afs2014fishes-e1] |
| Running the trial across years, but putting the same treatment in the same spot every year | Replication in time requires re-randomizing every year[^casler2015fundamentals-e7] |
| Drawing general conclusions from one year at one research station | Treatments often interact with the environment; give priority to adding sites and years[^casler2015fundamentals-e8] |
| The methods say only "weeded as necessary" or "managed according to farmer practice" | Nobody else can reproduce the trial[^kool2020reproducibility-e2][^kool2020reproducibility-e3] |
| Reporting only means, with no standard errors or confidence intervals | The Tri-Societies' journals require you to report precision[^asa2024style-e3] |
| Field records exist only in your own notebook, in no particular format | Others (including your future self) will struggle to reuse them[^papoutsoglou2020enabling-e2] |

---

## Further reading

- **Casler 2015, Fundamentals of Experimental Design (*Agronomy Journal*)**: uses field examples to explain replication, randomization, blocking, and plot size, and ends with advice for young researchers. Read it before you design your first field trial.
- **Tri-Societies' publications handbook, Chapter 4 (Statistical Design and Analysis)**: spells out what a paper must say about experimental design and statistics.
- **Kool et al. 2020 (*Experimental Agriculture*)**: analyzes reporting problems in papers on African on-farm trials. Read it before running an on-farm trial; it helps you think through your controls and the scope of your conclusions.
- **Davies & Gray 2015 (*Ecology and Evolution*)**: the other side of pseudoreplication, worth reading when true replication really is impossible.
- **Papoutsoglou et al. 2020, MIAPPE 1.1 (*New Phytologist*)**: the plant phenotyping metadata standard, a reference for organizing field data.
- **American Fisheries Society et al. 2014, Guidelines for the Use of Fishes in Research**: design, permits, and animal welfare in fish research; a reference if you do fish research in the US.

[^casler2015fundamentals-e1]: Casler 2015, Abstract. [Evidence](../../../sources/notes/casler2015fundamentals.md#e1)
[^casler2015fundamentals-e2]: Casler 2015, Table 1. [Evidence](../../../sources/notes/casler2015fundamentals.md#e2)
[^casler2015fundamentals-e4]: Casler 2015, Replication. [Evidence](../../../sources/notes/casler2015fundamentals.md#e4)
[^casler2015fundamentals-e5]: Casler 2015, Replication, the prescribed-burn example. [Evidence](../../../sources/notes/casler2015fundamentals.md#e5)
[^casler2015fundamentals-e6]: Casler 2015, Replication, the prescribed-burn example. [Evidence](../../../sources/notes/casler2015fundamentals.md#e6)
[^casler2015fundamentals-e7]: Casler 2015, Replication, the prescribed-burn example. [Evidence](../../../sources/notes/casler2015fundamentals.md#e7)
[^casler2015fundamentals-e8]: Casler 2015, Number of replicates. [Evidence](../../../sources/notes/casler2015fundamentals.md#e8)
[^casler2015fundamentals-e9]: Casler 2015, Replication. [Evidence](../../../sources/notes/casler2015fundamentals.md#e9)
[^casler2015fundamentals-e10]: Casler 2015, Number of replicates. [Evidence](../../../sources/notes/casler2015fundamentals.md#e10)
[^casler2015fundamentals-e11]: Casler 2015, Replication, special cases. [Evidence](../../../sources/notes/casler2015fundamentals.md#e11)
[^casler2015fundamentals-e12]: Casler 2015, Replication, participatory research. [Evidence](../../../sources/notes/casler2015fundamentals.md#e12)
[^casler2015fundamentals-e13]: Casler 2015, Randomization. [Evidence](../../../sources/notes/casler2015fundamentals.md#e13)
[^casler2015fundamentals-e14]: Casler 2015, Blocking. [Evidence](../../../sources/notes/casler2015fundamentals.md#e14)
[^casler2015fundamentals-e15]: Casler 2015, Blocking. [Evidence](../../../sources/notes/casler2015fundamentals.md#e15)
[^casler2015fundamentals-e16]: Casler 2015, Blocking, split-plot designs. [Evidence](../../../sources/notes/casler2015fundamentals.md#e16)
[^casler2015fundamentals-e17]: Casler 2015, Blocking. [Evidence](../../../sources/notes/casler2015fundamentals.md#e17)
[^casler2015fundamentals-e18]: Casler 2015, Blocking. [Evidence](../../../sources/notes/casler2015fundamentals.md#e18)
[^casler2015fundamentals-e19]: Casler 2015, Conclusions section. [Evidence](../../../sources/notes/casler2015fundamentals.md#e19)
[^casler2015fundamentals-e20]: Casler 2015, Conclusions section. [Evidence](../../../sources/notes/casler2015fundamentals.md#e20)
[^casler2015fundamentals-e21]: Casler 2015, Conclusions section. [Evidence](../../../sources/notes/casler2015fundamentals.md#e21)
[^casler2015fundamentals-e22]: Casler 2015, Conclusions section. [Evidence](../../../sources/notes/casler2015fundamentals.md#e22)
[^casler2015fundamentals-e23]: Casler 2015, Conclusions section. [Evidence](../../../sources/notes/casler2015fundamentals.md#e23)
[^casler2015fundamentals-e24]: Casler 2015, Replication. [Evidence](../../../sources/notes/casler2015fundamentals.md#e24)
[^casler2015fundamentals-e25]: Casler 2015, Blocking, incomplete block designs. [Evidence](../../../sources/notes/casler2015fundamentals.md#e25)
[^casler2015fundamentals-e26]: Casler 2015, Conclusions section. [Evidence](../../../sources/notes/casler2015fundamentals.md#e26)
[^asa2024style-e1]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../sources/notes/asa2024style.md#e1)
[^asa2024style-e2]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../sources/notes/asa2024style.md#e2)
[^asa2024style-e3]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../sources/notes/asa2024style.md#e3)
[^asa2024style-e4]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../sources/notes/asa2024style.md#e4)
[^asa2024style-e5]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 1, Manuscript Handling. [Evidence](../../../sources/notes/asa2024style.md#e5)
[^asa2024style-e6]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 1, Anonymous Review. [Evidence](../../../sources/notes/asa2024style.md#e6)
[^asa2024style-e7]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 5. [Evidence](../../../sources/notes/asa2024style.md#e7)
[^asa2024style-e8]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 1. [Evidence](../../../sources/notes/asa2024style.md#e8)
[^asa2024style-e9]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../sources/notes/asa2024style.md#e9)
[^asa2024style-e12]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 1, Research Papers. [Evidence](../../../sources/notes/asa2024style.md#e12)
[^asa2024style-e13]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 1, Research Papers. [Evidence](../../../sources/notes/asa2024style.md#e13)
[^asa2024style-e14]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 1, Research Papers. [Evidence](../../../sources/notes/asa2024style.md#e14)
[^sciencesocietieseditorial-e1]: American Society of Agronomy et al., Editorial Policies, Data Policy. [Evidence](../../../sources/notes/sciencesocietieseditorial.md#e1)
[^sciencesocietieseditorial-e2]: American Society of Agronomy et al., Editorial Policies, Data Policy. [Evidence](../../../sources/notes/sciencesocietieseditorial.md#e2)
[^sciencesocietieseditorial-e3]: American Society of Agronomy et al., Editorial Policies, Prior Publication. [Evidence](../../../sources/notes/sciencesocietieseditorial.md#e3)
[^sciencesocietieseditorial-e4]: American Society of Agronomy et al., Editorial Policies, Statement of Ethics for Authors. [Evidence](../../../sources/notes/sciencesocietieseditorial.md#e4)
[^sciencesocietieseditorial-e5]: American Society of Agronomy et al., Editorial Policies, Statement of Ethics for Authors. [Evidence](../../../sources/notes/sciencesocietieseditorial.md#e5)
[^kool2020reproducibility-e1]: Kool et al. 2020, Material and Methods. [Evidence](../../../sources/notes/kool2020reproducibility.md#e1)
[^kool2020reproducibility-e2]: Kool et al. 2020, Abstract. [Evidence](../../../sources/notes/kool2020reproducibility.md#e2)
[^kool2020reproducibility-e3]: Kool et al. 2020, Abstract. [Evidence](../../../sources/notes/kool2020reproducibility.md#e3)
[^kool2020reproducibility-e4]: Kool et al. 2020, Abstract. [Evidence](../../../sources/notes/kool2020reproducibility.md#e4)
[^kool2020reproducibility-e5]: Kool et al. 2020, Introduction. [Evidence](../../../sources/notes/kool2020reproducibility.md#e5)
[^kool2020reproducibility-e6]: Kool et al. 2020, Material and Methods. [Evidence](../../../sources/notes/kool2020reproducibility.md#e6)
[^kool2020reproducibility-e7]: Kool et al. 2020, Conclusion. [Evidence](../../../sources/notes/kool2020reproducibility.md#e7)
[^kool2020reproducibility-e8]: Kool et al. 2020, Results. [Evidence](../../../sources/notes/kool2020reproducibility.md#e8)
[^kyveryga2019onfarm-e1]: Kyveryga 2019, Precision Agriculture Technology Tools. [Evidence](../../../sources/notes/kyveryga2019onfarm.md#e1)
[^kyveryga2019onfarm-e2]: Kyveryga 2019, Precision Agriculture Technology Tools. [Evidence](../../../sources/notes/kyveryga2019onfarm.md#e2)
[^kyveryga2019onfarm-e3]: Kyveryga 2019, Precision Agriculture Technology Tools. [Evidence](../../../sources/notes/kyveryga2019onfarm.md#e3)
[^kyveryga2019onfarm-e4]: Kyveryga 2019, Precision Agriculture Technology Tools. [Evidence](../../../sources/notes/kyveryga2019onfarm.md#e4)
[^kyveryga2019onfarm-e5]: Kyveryga 2019, Analytical Approaches for On-Farm Trials. [Evidence](../../../sources/notes/kyveryga2019onfarm.md#e5)
[^rothamstedlte-e1]: Rothamsted Research, The Long Term Experiments. [Evidence](../../../sources/notes/rothamstedlte.md#e1)
[^rothamstedlte-e2]: Rothamsted Research, The Classical Experiments. [Evidence](../../../sources/notes/rothamstedlte.md#e2)
[^rothamstedlte-e3]: Rothamsted Research, The Classical Experiments. [Evidence](../../../sources/notes/rothamstedlte.md#e3)
[^rothamstedlte-e4]: Rothamsted Research, Sample Archive. [Evidence](../../../sources/notes/rothamstedlte.md#e4)
[^rothamstedlte-e5]: Rothamsted Research, National Bioscience Research Infrastructure. [Evidence](../../../sources/notes/rothamstedlte.md#e5)
[^rothamstedlte-e6]: Rothamsted Research, The Electronic Rothamsted Archive. [Evidence](../../../sources/notes/rothamstedlte.md#e6)
[^papoutsoglou2020enabling-e1]: Papoutsoglou et al. 2020, Introduction. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e1)
[^papoutsoglou2020enabling-e2]: Papoutsoglou et al. 2020, Introduction. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e2)
[^papoutsoglou2020enabling-e3]: Papoutsoglou et al. 2020, Introduction. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e3)
[^papoutsoglou2020enabling-e4]: Papoutsoglou et al. 2020, Introduction. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e4)
[^papoutsoglou2020enabling-e5]: Papoutsoglou et al. 2020, Introduction. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e5)
[^papoutsoglou2020enabling-e6]: Papoutsoglou et al. 2020, Results, Event. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e6)
[^papoutsoglou2020enabling-e7]: Papoutsoglou et al. 2020, Introduction. [Evidence](../../../sources/notes/papoutsoglou2020enabling.md#e7)
[^cgiar2021fair-e1]: CGIAR (Consultative Group on International Agricultural Research) 2021, 1.1. [Evidence](../../../sources/notes/cgiar2021fair.md#e1)
[^cgiar2021fair-e2]: CGIAR (Consultative Group on International Agricultural Research) 2021, 1.1. [Evidence](../../../sources/notes/cgiar2021fair.md#e2)
[^cgiar2021fair-e3]: CGIAR (Consultative Group on International Agricultural Research) 2021, Annex 2. [Evidence](../../../sources/notes/cgiar2021fair.md#e3)
[^cgiar2021fair-e4]: CGIAR (Consultative Group on International Agricultural Research) 2021, 4.1 c). [Evidence](../../../sources/notes/cgiar2021fair.md#e4)
[^cgiar2021fair-e5]: CGIAR (Consultative Group on International Agricultural Research) 2021, 4.2. [Evidence](../../../sources/notes/cgiar2021fair.md#e5)
[^cgiar2021fair-e6]: CGIAR (Consultative Group on International Agricultural Research) 2021, 4.1 b). [Evidence](../../../sources/notes/cgiar2021fair.md#e6)
[^davies2015pseudoreplication-e1]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e1)
[^davies2015pseudoreplication-e2]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e2)
[^davies2015pseudoreplication-e3]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e3)
[^davies2015pseudoreplication-e4]: Davies & Gray 2015, Conclusion. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e4)
[^davies2015pseudoreplication-e5]: Davies & Gray 2015, survey results. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e5)
[^davies2015pseudoreplication-e6]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e6)
[^afs2014fishes-e1]: American Fisheries Society et al. 2014, 2.3 Statistical Design. [Evidence](../../../sources/notes/afs2014fishes.md#e1)
[^afs2014fishes-e2]: American Fisheries Society et al. 2014, 2.3 Statistical Design. [Evidence](../../../sources/notes/afs2014fishes.md#e2)
[^afs2014fishes-e3]: American Fisheries Society et al. 2014, 1. Introduction. [Evidence](../../../sources/notes/afs2014fishes.md#e3)
[^afs2014fishes-e4]: American Fisheries Society et al. 2014, 3. Statutory Requirements. [Evidence](../../../sources/notes/afs2014fishes.md#e4)
[^afs2014fishes-e5]: American Fisheries Society et al. 2014, 3.1 International Regulations. [Evidence](../../../sources/notes/afs2014fishes.md#e5)
[^afs2014fishes-e6]: American Fisheries Society et al. 2014, Final Disposition of Experimental Animals. [Evidence](../../../sources/notes/afs2014fishes.md#e6)
[^wallach2023proposal-e1]: Wallach et al. 2023, Abstract. [Evidence](../../../sources/notes/wallach2023proposal.md#e1)
[^wallach2023proposal-e2]: Wallach et al. 2023, §1 Introduction. [Evidence](../../../sources/notes/wallach2023proposal.md#e2)
[^wallach2023proposal-e3]: Wallach et al. 2023, §2.1, §2.3. [Evidence](../../../sources/notes/wallach2023proposal.md#e3)
[^wallach2023proposal-e4]: Wallach et al. 2023, §1 Introduction. [Evidence](../../../sources/notes/wallach2023proposal.md#e4)
[^wallach2023proposal-e5]: Wallach et al. 2023, §1 Introduction. [Evidence](../../../sources/notes/wallach2023proposal.md#e5)
[^wallach2023proposal-e6]: Wallach et al. 2023, §3.3. [Evidence](../../../sources/notes/wallach2023proposal.md#e6)
[^wallach2023proposal-e7]: Wallach et al. 2023, §1 Introduction. [Evidence](../../../sources/notes/wallach2023proposal.md#e7)
[^boote2013protocols-e1]: Boote & Jones 2013, AgMIP crop model improvement team protocol, Framework for Proposed Crop Model Improvement Activities. [Evidence](../../../sources/notes/boote2013protocols.md#e1)
[^boote2013protocols-e2]: Boote & Jones 2013, AgMIP crop model improvement team protocol, Framework for Proposed Crop Model Improvement Activities. [Evidence](../../../sources/notes/boote2013protocols.md#e2)
[^rosenzweig2013agricultural-e1]: Rosenzweig et al. 2013, §3.2 Crop Modeling Team Protocols. [Evidence](../../../sources/notes/rosenzweig2013agricultural.md#e1)
[^rosenzweig2013agricultural-e2]: Rosenzweig et al. 2013, §3.2 Crop Modeling Team Protocols. [Evidence](../../../sources/notes/rosenzweig2013agricultural.md#e2)
[^rosenzweig2013agricultural-e3]: Rosenzweig et al. 2013, §3.2 Crop Modeling Team Protocols. [Evidence](../../../sources/notes/rosenzweig2013agricultural.md#e3)
[^rosenzweig2013agricultural-e4]: Rosenzweig et al. 2013, §5.1 wheat pilot. [Evidence](../../../sources/notes/rosenzweig2013agricultural.md#e4)
[^carletto2013guesstimates-e1]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, Abstract. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e1)
[^carletto2013guesstimates-e2]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, §4 Conclusions. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e2)
[^carletto2013guesstimates-e3]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, §4 Conclusions. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e3)
[^carletto2013guesstimates-e4]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, §4 Conclusions. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e4)
[^carletto2013guesstimates-e5]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, §1, footnote 3. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e5)
[^carletto2013guesstimates-e6]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, Abstract. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e6)
[^carletto2013guesstimates-e7]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, §1. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e7)
[^carletto2013guesstimates-e8]: Carletto et al. 2013, World Bank Policy Research Working Paper 6550, §1. [Evidence](../../../sources/notes/carletto2013guesstimates.md#e8)
[^krupnik2019does-e1]: Krupnik et al. 2019, Summary. [Evidence](../../../sources/notes/krupnik2019does.md#e1)
[^krupnik2019does-e2]: Krupnik et al. 2019, Summary. [Evidence](../../../sources/notes/krupnik2019does.md#e2)
[^krupnik2019does-e3]: Krupnik et al. 2019, Conclusions. [Evidence](../../../sources/notes/krupnik2019does.md#e3)
[^krupnik2019does-e4]: Krupnik et al. 2019, Conclusions. [Evidence](../../../sources/notes/krupnik2019does.md#e4)
[^krupnik2019does-e5]: Krupnik et al. 2019, Conclusions. [Evidence](../../../sources/notes/krupnik2019does.md#e5)
[^krupnik2019does-e6]: Krupnik et al. 2019, Summary. [Evidence](../../../sources/notes/krupnik2019does.md#e6)
[^haddaway2018roses-e1]: Haddaway et al. 2018, Abstract. [Evidence](../../../sources/notes/haddaway2018roses.md#e1)
[^haddaway2018roses-e2]: Haddaway et al. 2018, Abstract. [Evidence](../../../sources/notes/haddaway2018roses.md#e2)
[^haddaway2018roses-e3]: Haddaway et al. 2018, Key differences between ROSES and PRISMA, p. 4. [Evidence](../../../sources/notes/haddaway2018roses.md#e3)
[^haddaway2018roses-e4]: Haddaway et al. 2018, Key differences between ROSES and PRISMA, p. 5. [Evidence](../../../sources/notes/haddaway2018roses.md#e4)
[^haddaway2018roses-e5]: Haddaway et al. 2018, Background, p. 4. [Evidence](../../../sources/notes/haddaway2018roses.md#e5)
[^haddaway2018roses-e6]: Haddaway et al. 2018, Benefits of ROSES, p. 6. [Evidence](../../../sources/notes/haddaway2018roses.md#e6)
[^haddaway2018roses-e7]: Haddaway et al. 2018, Benefits of ROSES, p. 6. [Evidence](../../../sources/notes/haddaway2018roses.md#e7)
[^cabiagbioevidencesynthesis-e1]: CABI Agriculture and Bioscience submission guidelines, Evidence Synthesis (archived May 2025). [Evidence](../../../sources/notes/cabiagbioevidencesynthesis.md#e1)
[^cabiagbioevidencesynthesis-e2]: CABI Agriculture and Bioscience submission guidelines, Evidence Synthesis (archived May 2025). [Evidence](../../../sources/notes/cabiagbioevidencesynthesis.md#e2)
[^cabiagbioevidencesynthesis-e3]: CABI Agriculture and Bioscience submission guidelines, Evidence Synthesis (archived May 2025). [Evidence](../../../sources/notes/cabiagbioevidencesynthesis.md#e3)
