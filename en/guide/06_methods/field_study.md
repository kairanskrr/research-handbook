# Field studies: observation and sampling

This page is about studies where you **go out to a site to observe and take samples**: you set up sampling locations in rivers, lakes, groundwater, soil, rock outcrops, the atmosphere, or the ocean, take measurements and samples, and use the data to answer a question. Ecological field surveys (quadrats, transects, species surveys) can also draw on this page `[Our analysis]`.

Not covered here: field trials where you **actively apply a treatment** in the field, see the [agriculture field overview](../07_fields/agriculture/README.md#designing-field-trials); details of quality control for lab analyses, see the [environmental engineering field overview](../07_fields/environmental-engineering/README.md#quality-control-samples-blanks-replicates-and-spikes); analyzing only data that others have already collected, see [Data science research](data_science.md) under research methods; safety, permits, ethics, and harassment in the field, see the [earth and environmental sciences field overview](../07_fields/earth-environmental-sciences/README.md#fieldwork-sort-out-safety-and-permits-first).

**First, where this page's sources come from.** Most of the practical detail comes from two US government agencies. The *National Field Manual for the Collection of Water-Quality Data* of the United States Geological Survey (USGS) is the protocol USGS sets for **its own** water-quality field staff[^usgs2018nfmprep-e2]. The planning guidance of the Environmental Protection Agency (EPA) was written by EPA for **projects it funds**; for its scope, see the [environmental engineering field overview](../07_fields/environmental-engineering/README.md#write-the-plan-down-epas-quality-assurance-project-plan). `[Our analysis]` These are not field-wide rules and do not bind you, but they are concrete and work well as checklists. What you must follow are the rules of your own country, institution, funder, and target journal.

**Scope** `[Our analysis]`: this page was written for the earth and environmental sciences section, and its examples focus on observing and sampling environmental media such as water, soil, and rock. Its sources are mainly handbooks and guidance from US government agencies (USGS, EPA), documents from societies such as the American Geophysical Union (AGU), and methods papers in ecological and environmental statistics. Besides [Earth and environmental sciences](../07_fields/earth-environmental-sciences/README.md), the field overviews for [agriculture](../07_fields/agriculture/README.md), [Environmental engineering](../07_fields/environmental-engineering/README.md), and [geography](../07_fields/geography/README.md) also link here. Other fields that do on-site observation may have different requirements for sampling and quality control; check your own field's norms before using this page.

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md#3-common-research-methods).

**After reading this page, you should be able to:**

- turn your research question into "where to sample, when, and how much";
- prepare for safety and instruments before you set out, and keep field records that others can understand;
- plan quality-control samples and manage sample IDs and data;
- recognize three common traps when analyzing field data: pseudoreplication, confounding, and autocorrelation.

---

## 1. What this kind of study is, and when to use it

| | Field observation study | Manipulative field experiment | Analyzing existing observational data |
|---|---|---|---|
| What you do | Measure and sample on site without changing what you study | Apply a treatment on site (fertilizing, burning, fencing) and compare the effects | Use ready-made data from monitoring networks, satellites, or databases |
| Where the data come from | You collect them | You collect them | Someone else collected them |
| Biggest difficulty | Sampling design, quality in the field; missed opportunities can't be made up | True replication and randomization | Working out how the data were produced and how good they are |
| Where to look | This page | [Agriculture field overview](../07_fields/agriculture/README.md#designing-field-trials) | [Data science research](data_science.md) |

`[Our analysis]` How to choose: if you want to know "what state something is in at a given place now, and how it varies over time and space", do field observation; if you want to know "whether a treatment causes a change", and you can control the treatment, do a manipulative experiment. With observational data only, your causal conclusions are weaker; see Step 11 below. Many projects mix the two: first use field observation to establish the current state, then design an experiment or a simulation.

## 2. How to do it

### Step 1: Turn your question into one that can be answered in the field

**How:** first write down four things: what the data are for (estimating a mean? comparing two areas? detecting a trend?); the target population, that is, the scope you want your conclusions to cover; the sampling unit; and how much error you can tolerate. When you study a continuous medium such as air, water, or soil, EPA guidance requires the sampling unit to be defined as a specific area, volume, or mass[^epa2006dqo-e6]. EPA uses a seven-step "data quality objectives process" for this; for the steps, see the [environmental engineering field overview](../07_fields/environmental-engineering/README.md#plan-before-you-sample-epas-data-quality-objectives-process).

**Why:** EPA guidance says that without planning before sampling, there is an unacceptably high chance that the data you collect will not meet your needs[^epa2006dqo-e1]. Once a moment in the field has passed, you cannot go back and collect the data `[Our analysis]`.

**Where people go wrong:** writing only "survey the water quality of a lake" without saying whether you want to estimate the lake-wide average or compare the inlet with the outlet. The two goals call for completely different sampling layouts `[Our analysis]`. For how to make your research question concrete, see [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md) in Part 2.

### Step 2: Design the sampling: where, when, and how much

**First decide between probability sampling and judgmental sampling.** In probability sampling, every sampling unit has a known probability of being selected; in judgmental sampling, the person in charge picks locations from experience[^epa2006dqo-e12]. According to EPA guidance, common probability designs include simple random, stratified, systematic, and grid sampling; they let you draw quantitative conclusions about the target population and state how uncertain those conclusions are[^epa2006dqo-e13]. Judgmental sampling cannot do this: statistical analysis of a judgmental sample cannot support defensible probabilistic statements about the population[^epa2006dqo-e14].

| Design | How | When to use it |
|---|---|---|
| Simple random | Place points at random across the study area | The area is fairly uniform and you have no prior information `[Our analysis]` |
| Stratified | First divide the area by known differences (such as past land use), then sample within each part | The parts differ, and each must be represented[^epa2006dqo-e15] |
| Systematic or grid | Place points at fixed spacing | You need a map of spatial distribution or even coverage `[Our analysis]` |
| Judgmental | Pick points from experience | Conclusions rest only on professional judgment; no probabilistic inference[^epa2006dqo-e14] |

**Use many points in space.** The USGS manual notes that in most flowing or still water bodies, a single sampling point is not enough to represent the physical, chemical, or biological condition of the whole water body[^usgs2018nfmprep-e3]. When choosing sites, consider together the number and location of points, the data quality objectives, access, safety, and budget[^usgs2018nfmprep-e5]. Measuring field parameters across a cross-section first gives a rough idea of whether mixing is uniform; but that does not guarantee the substance you care about is uniform too, so test this early in sampling[^usgs2018nfmprep-e6].

**Repeat in time as well.** EPA guidance says that, in general, sampling error is much larger than measurement error[^epa2006dqo-e7]; when you expect large variation in space or time, you can use a cheaper, somewhat less precise analytical method and spend the money on more locations and times[^epa2006dqo-e9]. Casler (a review of experimental design written for agronomists) likewise recommends adding more locations and years rather than more replicates within each location[^casler2015fundamentals-e27].

**How much to sample.** Casler recommends a statistical power analysis (estimating how many samples you need to have a good chance of detecting the difference you care about) before every design, even if you have to guess the parameters[^casler2015fundamentals-e21]. For how, see the [agriculture field overview](../07_fields/agriculture/README.md#sites-years-and-power-analysis).

**Where people go wrong: pseudoreplication.** Pseudoreplication is using a statistical test of a treatment effect when the treatment is not truly replicated, or the replicates are not independent[^davies2015pseudoreplication-e1]. Casler's example: with only two plots, one burned and one not, the statistics can be computed correctly, but the design cannot unambiguously explain the result[^casler2015fundamentals-e5]. He stresses that replication has to match the spatial and temporal scale at which the treatment is applied[^casler2015fundamentals-e4]. The same goes for observational studies: if you compare "one point upstream" with "one point downstream" and take 30 bottles of water at each, you still have only one point on each side `[Our analysis]`. For more examples, see the [agriculture field overview](../07_fields/agriculture/README.md#pseudoreplication-treatment-confounded-with-the-plot).

### Step 3: Get all your permits

**How:** go through access permits, sampling permits, and, where needed, permits to import or export samples, one by one; also check whether the site is protected. The checklist and the ethical issues are in the [earth and environmental sciences field overview](../07_fields/earth-environmental-sciences/README.md#fieldwork-sort-out-safety-and-permits-first) and are not repeated here. Two additions:

- USGS requires its staff to obtain permission before entering public or private land to select sites or sample; written permission is preferred, and oral permission must be documented[^usgs2018nfmprep-e2]. If you don't have written permission, at least record who agreed, when, and to what `[Our analysis]`.
- When animals are involved (for example, collecting fish), the guidelines of the American Fisheries Society and two other societies require researchers to obtain all necessary permits[^afs2014fishes-e4]; when working outside the United States, follow the host country's wildlife regulations[^afs2014fishes-e5].

**Where people go wrong:** assuming your advisor or collaborators have already taken care of it. Our sources do not cover which permits your particular country requires. Before you set out, make a list and ask about each item `[Our analysis]`: who manages the land or protected area; whether sampling or collecting plants and animals needs a permit; whether there are restrictions on moving samples between regions or out of the country. When unsure, ask your advisor and your institution's research office, and keep the approvals and permit records.

### Step 4: Safety and logistics

**How:** (from the USGS manual; these are rules for USGS staff, and you can use them as a checklist)

- Go through each specific task with a "job hazard analysis" to identify hazards before they happen[^usgs2018nfmprep-e14].
- At all times the team should include at least one experienced, trained person[^usgs2018nfmprep-e13]; check in with your office every evening, and agree that if no call comes in, someone will start a rescue[^usgs2018nfmprep-e15].
- When choosing sites, make sure you can reach them under both normal and extreme flow and weather conditions[^usgs2018nfmprep-e4]. Any stream, including seasonal ones, can quickly become too deep and fast to wade safely[^usgs2018nfmprep-e7].

**Where people go wrong:** treating safety preparation as a formality. For having your risk assessment reviewed and shared with everyone in the party, first aid, reporting channels and so on, see the [earth and environmental sciences field overview](../07_fields/earth-environmental-sciences/README.md#fieldwork-sort-out-safety-and-permits-first).

### Step 5: Instruments and field calibration

**How:** these are USGS rules for its own staff. Calibrate instruments before every field trip, and check most of them again in the field[^usgs2023nfmfield-e6]; check precision and accuracy periodically in the field[^usgs2023nfmfield-e8]. Keep a separate logbook for each instrument or replaceable sensor, recording its repair, maintenance, and calibration history, and keep the logbook with the instrument[^usgs2023nfmfield-e4]. The first time you use a type of instrument, practice with someone experienced[^usgs2023nfmfield-e7].

**Why:** what USGS calls "field measurements" are properties that must be measured on site, as close as possible in time and place to when the sample is taken[^usgs2023nfmfield-e1], such as water temperature and dissolved oxygen `[Our analysis]`. These data cannot be remeasured later; if an instrument fails, the whole trip's data may be lost `[Our analysis]`.

**Where people go wrong:** setting out with an instrument that wasn't fixed after the last trip; calibrating only once before leaving and never checking for drift in the field `[Our analysis]`.

### Step 6: Field records

**How:** (USGS rules for its own staff)

- Every uniquely numbered sampling site must have a record that permanently documents field activities, readings, instrument calibration, and similar information[^usgs2023nfmfield-e2]. Most of the record is completed in the field and independently checked by a colleague or data manager[^usgs2023nfmfield-e3].
- Paper records must not be written in pencil; to correct a mistake, draw a single line through it and initial it; don't scribble it out[^usgs2023nfmfield-e5]. When you use judgment to choose one reading among several, note in the record how you decided[^usgs2023nfmfield-e9].
- Draw a site sketch detailed enough that someone who has never been there could find the spot from it[^usgs2018nfmprep-e16].
- Archive the original records (the data, metadata and so on first written down in the field), whether on paper or electronic[^usgs2018nfmprep-e9].

**Why:** the ethics policy of the American Geophysical Union (AGU) requires careful documentation of methods, assumptions, and uncertainties[^agu2023ethics-e8], and papers written in enough detail for peers to repeat the work[^agu2023ethics-e7]. Weather, water levels, and anything unusual in the field exist only if you write them down at the time `[Our analysis]`. Our sources do not cover which metadata fields to record; follow the requirements of your target database or journal.

### Step 7: Sample IDs

**How:** give each sample a unique ID and track it throughout, to avoid mix-ups[^epa2002qapp-e6]; prepare bottle labels before you set out, with the site, sample type and so on (an item on the USGS checklist)[^usgs2018nfmprep-e18]. If you can, register an International Generalized Sample Number (IGSN, a globally unique, persistent identifier for physical samples); for how, see the [earth and environmental sciences field overview](../07_fields/earth-environmental-sciences/README.md#samples-give-every-sample-a-permanent-identifier). If you attach a QR code, the label should also show a human-readable ID[^igsnpublications-e3]. For chain of custody (recording who handled the sample at every step), see the [environmental engineering field overview](../07_fields/environmental-engineering/README.md#sample-ids-and-chain-of-custody).

**Why:** the USGS manual says the analytical results can be no better than the sample that was analyzed[^usgs2018nfmprep-e1].

### Step 8: Plan quality-control samples

**How:** state in your sampling plan which quality-control samples you will take and how often (a requirement of EPA's guidance on quality assurance project plans)[^epa2002qapp-e13]. Two kinds are collected in the field:

- **Field blanks**: clean samples containing none of the target substance, taken to the site, exposed to sampling conditions, and then sent to the lab like ordinary samples[^epa2002qapp-e14]. USGS requires blanks to be collected before regular sampling begins, and periodically after that[^usgs2018nfmprep-e10].
- **Field replicates**: two or more samples taken at the same time and place, and labeled as such[^epa2002qapp-e16]. According to the USGS manual, they are used to estimate the natural variability of the water body and the variability introduced by sampling, processing, and analysis[^usgs2018nfmprep-e11].

**Why:** EPA guidance says the purpose of quality control is not to eliminate error but to measure how large it is[^epa2002qapp-e9]. For spiked samples, detection limits, and "non-detect" data, see the [environmental engineering field overview](../07_fields/environmental-engineering/README.md#quality-control-samples-blanks-replicates-and-spikes).

**Where people go wrong:** field replicates are quality control, not replication. Two bottles of water from the same point cannot be treated as two independent sampling sites `[Our analysis]`.

### Step 9: Data management and archiving

**How:** the USGS manual requires data management to be planned before sampling begins[^usgs2018nfmprep-e8]. A USGS project work plan includes: scope, schedule, and budget; standard operating procedures; a quality assurance plan; a data management plan; and an analysis and publication plan[^usgs2018nfmprep-e17]. If you submit to AGU journals, field observation data are among the data that must be made available[^fox2021agudata-e16]; for requirements such as data being accessible at submission (with "available from the authors on request" not acceptable) and how to choose a repository, see the [earth and environmental sciences field overview](../07_fields/earth-environmental-sciences/README.md#data-available-at-submission).

### Step 10: Dealing with events that can't be repeated

Floods, storms, wildfires, and volcanic eruptions happen once. A 2015 perspective article by Davies and Gray says that pseudoreplication is very common in studies of such events[^davies2015pseudoreplication-e7]. They also concede that, strictly speaking, with only one disturbance and plots on either side of its boundary, you cannot statistically separate spatial differences from the effect of the event[^davies2015pseudoreplication-e8].

But they argue that you shouldn't label every single-event study as pseudoreplicated: confounding (see Step 11) has to be considered separately from pseudoreplication[^davies2015pseudoreplication-e9]; and before alleging pseudoreplication, one should first show that the allegation is statistically valid and ecologically meaningful[^davies2015pseudoreplication-e4]. Their approach:

- **Make the comparison as close as possible**: they placed the compared plots close together, on the same soil, at the same elevation, and with the same aspect[^davies2015pseudoreplication-e11].
- **Separate what you can infer from what you can interpret**: statistically, say only that "the two sides differ"; write the causal interpretation separately, as an ecological judgment[^davies2015pseudoreplication-e10].
- **Address it in the paper yourself**: they think reviewers can ask authors to acknowledge the problem, state their mitigation measures, interpret cautiously, and frame conclusions as new hypotheses[^davies2015pseudoreplication-e12]. It is enough for authors to do these things themselves up front `[Our analysis]`.

`[Our analysis]` After an event, get to the site as soon as possible, record in more detail than usual, keep enough sample material, and register IDs. The IGSN organization also notes that some samples can never be collected again[^igsnabout-e4].

### Step 11: Analyzing field observation data

First read [Data science research](data_science.md#step-8-interpret-the-results-correlation-is-not-causation) under research methods: in observational data, correlation is not causation. Field data bring three further problems.

**1. Confounding.** Differences between two areas may come partly from uncontrolled variables such as soil, moisture, aspect, or elevation[^davies2015pseudoreplication-e9]. In the design, make the compared points as similar as possible on these[^davies2015pseudoreplication-e11], and measure them `[Our analysis]`.

**2. Non-independent observations (autocorrelation).** Zuur and colleagues' 2010 data exploration protocol for ecologists points out that most statistical methods assume observations are independent of each other[^zuur2010protocol-e2]. Field data often are not:

- **Spatial autocorrelation**: values at nearby locations are not independent of each other[^dormann2007spatial-e1]; for example, birds at nearby sites are more alike than those far away[^zuur2010protocol-e3].
- **Serial correlation in time**: a USGS statistics textbook on water resources by Helsel and colleagues gives an example: sampling daily for 20 years gives about 7,300 values, and computing a confidence interval with n = 7,300 would greatly overstate how certain the result is[^helsel2020statistical-e9]; when sampling is so frequent that correlation is strong, 100 observations may estimate the mean only as accurately as 10 independent ones[^helsel2020statistical-e7].

The consequence: Dormann and colleagues' 2007 methods review notes that parameter estimates may be biased and "false positives" (concluding there is an effect when there is none) become more frequent[^dormann2007spatial-e3].

**How to check and what to do** (methodological advice from these authors): look at the raw data before analysis and at the residuals after, plotting them against time or spatial coordinates[^zuur2010protocol-e6]; for space, you can plot how the similarity or variance between data points changes with distance (a correlogram or semivariogram)[^dormann2007spatial-e4]. What looks like serial correlation is often actually caused by a time component such as seasonality, or by a trend[^helsel2020statistical-e10]. If you find non-independence, the model has to account for it[^zuur2010protocol-e4], for example with nested or random effects[^davies2015pseudoreplication-e3]. The specific methods are beyond this page; find a collaborator who knows statistics.

**3. A variable you didn't measure can't be added later.** Correlated residuals often come from leaving out an important variable, and this may be impossible to fix after the fact[^zuur2010protocol-e5][^dormann2007spatial-e2]. So think hard from the very start about what to measure `[Our analysis]`.

### Step 12: Reporting

`[Our analysis]` The methods section should state at least: the sampling design and why you chose your sites; when you sampled and the conditions at the time; instruments and calibration; quality-control samples and their results; sample IDs and where the samples are stored; and where the data are archived. The basis: AGU requires papers to be written in enough detail that peers can repeat the work[^agu2023ethics-e7], and AGU journals require both raw and processed data to be cited in the references[^fox2021agudata-e12]. If the design has limitations (for example, only one event site), address them up front as in Step 10.

## 3. Checklist

**Must do**

- [ ] Planned before sampling[^epa2006dqo-e1], with the purpose of the data, the target population, and the sampling unit written down[^epa2006dqo-e6]
- [ ] If you want statistical inference, you used probability sampling[^epa2006dqo-e14]
- [ ] Replicates are at the same spatial and temporal scale as what you are comparing[^casler2015fundamentals-e4]
- [ ] Access, sampling, and import/export permits all obtained, one by one[^greene2021safety-e3]
- [ ] Risk assessment reviewed by a third party, with everyone in the party informed[^greene2021safety-e5]
- [ ] Instruments calibrated before leaving and checked in the field[^usgs2023nfmfield-e6]
- [ ] Every sample has a unique ID[^epa2002qapp-e6], and original records are archived[^usgs2018nfmprep-e9]
- [ ] Types and frequency of quality-control samples written down[^epa2002qapp-e13]
- [ ] Spatial and temporal correlation checked before and after analysis[^zuur2010protocol-e6]

**Better practice**

- [ ] Power analysis done before the design[^casler2015fundamentals-e21]
- [ ] Blanks collected before regular sampling, to catch problems early[^usgs2018nfmprep-e10]
- [ ] IGSNs registered where possible[^igsnabout-e2]
- [ ] Records independently checked by a colleague[^usgs2023nfmfield-e3]

**Fine to skip; not a flaw**

- For a preliminary survey or a search for the "worst case", judgmental sampling is fine `[Our analysis]`; but conclusions then rest only on professional judgment, with no probabilistic inference[^epa2006dqo-e14].

**Common reviewer criticisms that may not hold up**

- "There is only one event site, so it's pseudoreplication and can't be published." Davies and Gray argue that the concept of pseudoreplication is applied too dogmatically and often leads to rejection in review[^davies2015pseudoreplication-e2]; they hold that before making the charge, one should show it is statistically valid and ecologically meaningful[^davies2015pseudoreplication-e4]; and reviewers can ask authors to acknowledge the problem, interpret cautiously, and frame conclusions as new hypotheses[^davies2015pseudoreplication-e12]. This is these two authors' view, not a consensus in the field `[Our analysis]`.

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Taking many bottles at one point and counting them as many samples | The American Fisheries Society and partner societies' guidelines count this as pseudoreplication[^afs2014fishes-e1]; field replicates are only for estimating variability[^usgs2018nfmprep-e11] |
| Picking points for convenience, then running statistical tests | Judgmental sampling does not support probabilistic inference[^epa2006dqo-e14] |
| Spending everything on precise analysis and having very few sites | EPA guidance holds that sampling error is generally much larger than measurement error[^epa2006dqo-e7] |
| Recording in pencil, or scribbling out mistakes | The USGS protocol does not allow it[^usgs2023nfmfield-e5] |
| Sampling daily for 20 years and computing a confidence interval with n = 7,300 | Serial correlation means the real information content is much smaller[^helsel2020statistical-e9] |
| Attributing the difference between the two sides directly to the event | Spatial differences and the event's effect can't be separated[^davies2015pseudoreplication-e8], and there may also be confounding[^davies2015pseudoreplication-e9] |

## 5. Further reading

- **USGS *National Field Manual for the Collection of Water-Quality Data*, Chapter A1 (preparations for water sampling) and Chapter A6.0 (field measurements)**: free. This is the USGS protocol for its own staff and should be used only as a checklist; it is concrete on preparation, safety, records, and calibration before you set out. If you work with media other than water, you can still borrow its record-keeping and preparation practices `[Our analysis]`.
- **EPA QA/G-4 (data quality objectives) and QA/G-5 (quality assurance project plans)**: guidance EPA wrote for the projects it funds. They cover how to turn a question into a sampling design and how to write a quality-control plan.
- **Davies & Gray 2015**: a perspective article, open access. On how to do and write up single-event studies, and how to respond to charges of pseudoreplication.
- **Zuur et al. 2010**: a data exploration protocol to follow before analyzing ecological data; the step on independence is the most relevant. **Dormann et al. 2007**: a review of methods for detecting and handling spatial autocorrelation.
- **Helsel et al. 2020**: the USGS statistics textbook for water resources, free.

[^epa2006dqo-e1]: U.S. Environmental Protection Agency (EPA) 2006, Introduction, PDF p. 11. [Evidence](../../sources/notes/epa2006dqo.md#e1)
[^epa2006dqo-e7]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 6, PDF p. 57. [Evidence](../../sources/notes/epa2006dqo.md#e7)
[^epa2006dqo-e12]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 7, PDF p. 83. [Evidence](../../sources/notes/epa2006dqo.md#e12)
[^epa2006dqo-e13]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 7, PDF p. 83. [Evidence](../../sources/notes/epa2006dqo.md#e13)
[^epa2006dqo-e14]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 7, PDF p. 83. [Evidence](../../sources/notes/epa2006dqo.md#e14)
[^epa2006dqo-e15]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 7, PDF p. 84. [Evidence](../../sources/notes/epa2006dqo.md#e15)
[^epa2006dqo-e9]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 7, PDF p. 83. [Evidence](../../sources/notes/epa2006dqo.md#e9)
[^epa2006dqo-e6]: U.S. Environmental Protection Agency (EPA) 2006, Chapter 4, PDF p. 41. [Evidence](../../sources/notes/epa2006dqo.md#e6)
[^epa2002qapp-e9]: U.S. Environmental Protection Agency (EPA) 2002, Element B5, PDF p. 39. [Evidence](../../sources/notes/epa2002qapp.md#e9)
[^epa2002qapp-e14]: U.S. Environmental Protection Agency (EPA) 2002, Appendix B, PDF p. 71. [Evidence](../../sources/notes/epa2002qapp.md#e14)
[^epa2002qapp-e16]: U.S. Environmental Protection Agency (EPA) 2002, Appendix B, PDF p. 69. [Evidence](../../sources/notes/epa2002qapp.md#e16)
[^epa2002qapp-e6]: U.S. Environmental Protection Agency (EPA) 2002, Element B3, PDF p. 36. [Evidence](../../sources/notes/epa2002qapp.md#e6)
[^epa2002qapp-e13]: U.S. Environmental Protection Agency (EPA) 2002, Element B5, PDF p. 39. [Evidence](../../sources/notes/epa2002qapp.md#e13)
[^usgs2018nfmprep-e1]: USGS 2018, §1.1, PDF p. 11. [Evidence](../../sources/notes/usgs2018nfmprep.md#e1)
[^usgs2018nfmprep-e3]: USGS 2018, §2.2, PDF p. 14. [Evidence](../../sources/notes/usgs2018nfmprep.md#e3)
[^usgs2018nfmprep-e2]: USGS 2018, §2.1, PDF p. 14. [Evidence](../../sources/notes/usgs2018nfmprep.md#e2)
[^usgs2018nfmprep-e4]: USGS 2018, §2.2, PDF p. 14. [Evidence](../../sources/notes/usgs2018nfmprep.md#e4)
[^usgs2018nfmprep-e5]: USGS 2018, §2.0, PDF p. 13. [Evidence](../../sources/notes/usgs2018nfmprep.md#e5)
[^usgs2018nfmprep-e6]: USGS 2018, §2.2.1, PDF p. 15. [Evidence](../../sources/notes/usgs2018nfmprep.md#e6)
[^usgs2018nfmprep-e7]: USGS 2018, §2.2.1, PDF p. 15. [Evidence](../../sources/notes/usgs2018nfmprep.md#e7)
[^usgs2018nfmprep-e8]: USGS 2018, §3.0, PDF p. 18. [Evidence](../../sources/notes/usgs2018nfmprep.md#e8)
[^usgs2018nfmprep-e9]: USGS 2018, §3.0, PDF p. 18. [Evidence](../../sources/notes/usgs2018nfmprep.md#e9)
[^usgs2018nfmprep-e10]: USGS 2018, §4.2, PDF p. 25. [Evidence](../../sources/notes/usgs2018nfmprep.md#e10)
[^usgs2018nfmprep-e11]: USGS 2018, §4.2, PDF p. 25. [Evidence](../../sources/notes/usgs2018nfmprep.md#e11)
[^usgs2018nfmprep-e13]: USGS 2018, Table 1-4, PDF p. 26. [Evidence](../../sources/notes/usgs2018nfmprep.md#e13)
[^usgs2018nfmprep-e14]: USGS 2018, §5.1.1, PDF p. 28. [Evidence](../../sources/notes/usgs2018nfmprep.md#e14)
[^usgs2018nfmprep-e15]: USGS 2018, Table 1-5, PDF p. 28. [Evidence](../../sources/notes/usgs2018nfmprep.md#e15)
[^usgs2018nfmprep-e16]: USGS 2018, §5.2, PDF p. 31. [Evidence](../../sources/notes/usgs2018nfmprep.md#e16)
[^usgs2018nfmprep-e17]: USGS 2018, §4.0, PDF p. 24. [Evidence](../../sources/notes/usgs2018nfmprep.md#e17)
[^usgs2018nfmprep-e18]: USGS 2018, Table 1-4, PDF p. 27. [Evidence](../../sources/notes/usgs2018nfmprep.md#e18)
[^usgs2023nfmfield-e1]: USGS 2023, §1.0, PDF p. 9. [Evidence](../../sources/notes/usgs2023nfmfield.md#e1)
[^usgs2023nfmfield-e2]: USGS 2023, §2.1, PDF p. 10. [Evidence](../../sources/notes/usgs2023nfmfield.md#e2)
[^usgs2023nfmfield-e3]: USGS 2023, §2.1, PDF p. 10. [Evidence](../../sources/notes/usgs2023nfmfield.md#e3)
[^usgs2023nfmfield-e4]: USGS 2023, §2.1, PDF p. 10. [Evidence](../../sources/notes/usgs2023nfmfield.md#e4)
[^usgs2023nfmfield-e5]: USGS 2023, §2.1, PDF p. 10. [Evidence](../../sources/notes/usgs2023nfmfield.md#e5)
[^usgs2023nfmfield-e6]: USGS 2023, PDF p. 12. [Evidence](../../sources/notes/usgs2023nfmfield.md#e6)
[^usgs2023nfmfield-e7]: USGS 2023, PDF p. 12. [Evidence](../../sources/notes/usgs2023nfmfield.md#e7)
[^usgs2023nfmfield-e8]: USGS 2023, Performance, PDF p. 12. [Evidence](../../sources/notes/usgs2023nfmfield.md#e8)
[^usgs2023nfmfield-e9]: USGS 2023, Performance, PDF p. 12. [Evidence](../../sources/notes/usgs2023nfmfield.md#e9)
[^casler2015fundamentals-e4]: Casler 2015, Replication. [Evidence](../../sources/notes/casler2015fundamentals.md#e4)
[^casler2015fundamentals-e5]: Casler 2015, Replication. [Evidence](../../sources/notes/casler2015fundamentals.md#e5)
[^casler2015fundamentals-e27]: Casler 2015, Number of replicates. [Evidence](../../sources/notes/casler2015fundamentals.md#e27)
[^casler2015fundamentals-e21]: Casler 2015, Conclusions section. [Evidence](../../sources/notes/casler2015fundamentals.md#e21)
[^davies2015pseudoreplication-e1]: Davies & Gray 2015, Abstract. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e1)
[^davies2015pseudoreplication-e7]: Davies & Gray 2015, Discussion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e7)
[^davies2015pseudoreplication-e8]: Davies & Gray 2015, Discussion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e8)
[^davies2015pseudoreplication-e9]: Davies & Gray 2015, Discussion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e9)
[^davies2015pseudoreplication-e10]: Davies & Gray 2015, Discussion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e10)
[^davies2015pseudoreplication-e11]: Davies & Gray 2015, Discussion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e11)
[^davies2015pseudoreplication-e12]: Davies & Gray 2015, Discussion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e12)
[^davies2015pseudoreplication-e3]: Davies & Gray 2015, Abstract. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e3)
[^davies2015pseudoreplication-e4]: Davies & Gray 2015, Conclusion. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e4)
[^davies2015pseudoreplication-e2]: Davies & Gray 2015, Abstract. [Evidence](../../sources/notes/davies2015pseudoreplication.md#e2)
[^afs2014fishes-e1]: American Fisheries Society et al. 2014, 2.3. [Evidence](../../sources/notes/afs2014fishes.md#e1)
[^afs2014fishes-e4]: American Fisheries Society et al. 2014, 3. [Evidence](../../sources/notes/afs2014fishes.md#e4)
[^afs2014fishes-e5]: American Fisheries Society et al. 2014, 3.1. [Evidence](../../sources/notes/afs2014fishes.md#e5)
[^greene2021safety-e3]: Greene et al. 2021, §4.2.2. [Evidence](../../sources/notes/greene2021safety.md#e3)
[^greene2021safety-e5]: Greene et al. 2021, §4.2.6. [Evidence](../../sources/notes/greene2021safety.md#e5)
[^igsnabout-e2]: IGSN e.V., About IGSNs. [Evidence](../../sources/notes/igsnabout.md#e2)
[^igsnabout-e4]: IGSN e.V., About IGSNs. [Evidence](../../sources/notes/igsnabout.md#e4)
[^igsnpublications-e3]: IGSN e.V., Using IGSN in Publications. [Evidence](../../sources/notes/igsnpublications.md#e3)
[^agu2023ethics-e7]: AGU 2023, VI.C, item 2. [Evidence](../../sources/notes/agu2023ethics.md#e7)
[^agu2023ethics-e8]: AGU 2023, VI.C, item 4. [Evidence](../../sources/notes/agu2023ethics.md#e8)
[^fox2021agudata-e16]: Fox et al. 2021, Introduction. [Evidence](../../sources/notes/fox2021agudata.md#e16)
[^fox2021agudata-e12]: Fox et al. 2021, §1, Data Citation. [Evidence](../../sources/notes/fox2021agudata.md#e12)
[^zuur2010protocol-e2]: Zuur et al. 2010, Step 8. [Evidence](../../sources/notes/zuur2010protocol.md#e2)
[^zuur2010protocol-e3]: Zuur et al. 2010, Step 8. [Evidence](../../sources/notes/zuur2010protocol.md#e3)
[^zuur2010protocol-e4]: Zuur et al. 2010, Step 8. [Evidence](../../sources/notes/zuur2010protocol.md#e4)
[^zuur2010protocol-e5]: Zuur et al. 2010, Step 8. [Evidence](../../sources/notes/zuur2010protocol.md#e5)
[^zuur2010protocol-e6]: Zuur et al. 2010, Step 8. [Evidence](../../sources/notes/zuur2010protocol.md#e6)
[^dormann2007spatial-e1]: Dormann et al. 2007, Introduction. [Evidence](../../sources/notes/dormann2007spatial.md#e1)
[^dormann2007spatial-e2]: Dormann et al. 2007, Introduction. [Evidence](../../sources/notes/dormann2007spatial.md#e2)
[^dormann2007spatial-e3]: Dormann et al. 2007, Abstract. [Evidence](../../sources/notes/dormann2007spatial.md#e3)
[^dormann2007spatial-e4]: Dormann et al. 2007, Methods section. [Evidence](../../sources/notes/dormann2007spatial.md#e4)
[^helsel2020statistical-e7]: Helsel et al. 2020, §1.1. [Evidence](../../sources/notes/helsel2020statistical.md#e7)
[^helsel2020statistical-e9]: Helsel et al. 2020, §9.4.2.4. [Evidence](../../sources/notes/helsel2020statistical.md#e9)
[^helsel2020statistical-e10]: Helsel et al. 2020, §9.4.2.4. [Evidence](../../sources/notes/helsel2020statistical.md#e10)
