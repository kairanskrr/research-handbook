# Earth and environmental sciences: field overview

This page covers a few concrete things about research in the Earth and environmental sciences (geology, geophysics, atmospheric and climate science, oceanography, hydrology, and the environmental science that borders on ecology): fieldwork, samples, numerical models, model intercomparison projects, and how to report data, code, and uncertainty. For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies this field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). For measurement questions such as sampling plans, quality-control samples, and detection limits, see [Environmental engineering](../environmental-engineering/README.md); for lab-based ecology and life science, see [Biological sciences](../biological-sciences/README.md); for the ethics of archaeological excavation, see [History and archaeology](../history-archaeology/README.md).

The rules and guidelines on this page come mainly from three bodies, and each covers its own ground. The ethics policy of the **American Geophysical Union** (AGU) applies to its members and to people taking part in its activities, and its data guidance applies to manuscripts submitted to AGU journals. The code policy of the journal ***Geoscientific Model Development*** (GMD, a journal of the European Geosciences Union, EGU, published by Copernicus) applies only to manuscripts submitted to GMD. The uncertainty guidance of the **Intergovernmental Panel on Climate Change** (IPCC), and the good practice guidance on detection and attribution from its 2009 expert meeting, are both written for the authors of its assessment reports. None of them is a rule for the whole field. Where your country, your institution, or your target journal has its own requirements, theirs apply `[Our analysis]`.

**After reading this page, you should be able to:**

- prepare for safety, permits, and ethics before you go into the field;
- manage sample identifiers, data, and model code, and write a proper "data and software availability statement";
- read the IPCC's uncertainty language and know who it was written for; know what to check before you post a preprint.

---

## How research works in this field

### Three ways of working, often mixed in one project

`[Our analysis]` Research in this field broadly works in three ways: going out to measure and collect samples (see [Fieldwork](#fieldwork-sort-out-safety-and-permits-first) and [Samples](#samples-give-every-sample-a-permanent-identifier)); chemical and physical analysis of samples in the lab; and **numerical models** (computer programs that solve the equations describing the Earth system) that simulate the atmosphere, the ocean, groundwater, and so on (see [Numerical models](#numerical-models-if-the-code-isnt-ready-the-paper-isnt-ready)). A single project often uses more than one. Our sources do not cover how field seasons are scheduled or how observation networks are organized; follow your advisor and your group's usual practice.

### Model intercomparison projects

Climate science has a form of large-scale collaboration called a **Model Intercomparison Project** (MIP). The best known is the **Coupled Model Intercomparison Project** (CMIP). According to the overview paper for its sixth phase, CMIP6 (Eyring et al. 2016), CMIP coordinates the design and distribution of global climate model simulations of the past, present, and future climate, and has become one of the foundations of climate science[^eyring2016cmip6-e1]; its aim is to better understand climate change in a multi-model context[^eyring2016cmip6-e4].

In CMIP6, a model that wants to take part must run a set of prescribed experiments called the DECK (Diagnostic, Evaluation and Characterization of Klima) and the CMIP historical simulation, and must use CMIP's data standards; which of the topic-specific MIPs to join after that is up to each modeling group's own scientific interests[^eyring2016cmip6-e2][^eyring2016cmip6-e3]. Our sources do not cover which experiments the DECK includes: for this page we read only the abstract and the first paragraph of the introduction of that paper, so read the original if you need the details.

For a newcomer `[Our analysis]`: you may not develop a model yourself, but instead use one from an institution or analyze CMIP output that is already public. Either way, put the model version, the experiment names, and the data standard in your paper. Also, the GMD editors point out that some Earth system models are controlled by large institutions and have restrictive licenses[^gmd2019editorial-e6]. Before you use one, find out how you will be able to write the code statement in your paper `[Our analysis]`.

### Publishing: journals, open review, and data papers

- **Journals**: all the rules and guidelines we found come from journals and societies `[Our analysis]`.
- **Open review**: the core idea of open review in EGU journals is that the submission and the review process are both public and permanently accessible[^gmd2019editorial-e9]. GMD requires code and data to be available at submission, and does not accept "will be made public on acceptance"[^gmdcodepolicy-e4].
- **Data papers**: Copernicus has a dedicated journal, *Earth System Science Data* (ESSD), that publishes data papers and peer-reviews the datasets[^gmdcodepolicy-e10]. In other words, a well-curated dataset can itself be submitted.
- **Authorship**: the AGU ethics policy requires that only people who made significant scientific contributions be listed as coauthors, in order of contribution, with particular attention to authorship of students' work[^agu2023ethics-e9]. Our sources set no rule on whether field assistants or people who provide samples count as authors; settle this with your advisor before the work starts `[Our analysis]`. For general practice, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#5-authorship-citation-and-conflicts-of-interest-give-every-contributor-due-credit) in Throughout the project.

### Preprints: EarthArXiv

**EarthArXiv** has run since 2017 and accepts manuscripts from every area of the Earth sciences and related planetary science[^eartharxivabout-e1]. Each one gets a DOI (digital object identifier, a permanent link) and can be cited[^eartharxivabout-e2]. It does not assess the scientific quality of manuscripts, that is, it does no peer review[^eartharxivabout-e3]. Its FAQ also mentions AGU's preprint server ESSOAr (Earth and Space Science Open Archive) as an alternative[^eartharxivfaq-e6].

What to know before you post (all of these are EarthArXiv's rules):

- **Once posted, it cannot be deleted**, only updated[^eartharxivfaq-e1]; if a journal rejects the paper, the preprint stays public[^eartharxivfaq-e4].
- **Check journal policies first**: check every journal you might submit the paper to, in turn, and confirm that each accepts preprints[^eartharxivfaq-e5].
- **Say what it is**: the manuscript must state clearly that it is a non-peer-reviewed EarthArXiv preprint[^eartharxivmoderation-e2]. **What it accepts**: "null results" (results that do not support a hypothesis) are accepted[^eartharxivmoderation-e1]; theses, dissertations, and coursework are not accepted[^eartharxivmoderation-e3].
- **Put data and code elsewhere**: EarthArXiv does not host supplementary material; you can only link to it elsewhere[^eartharxivfaq-e7]. The preprint and the published paper each have their own DOI, and citations may point to either one[^eartharxivfaq-e2].

---

## How this field differs from others

| Aspect | Earth and environmental sciences | For comparison |
|---|---|---|
| What you study | Some samples can never be collected again[^igsnabout-e4] | In computer science, most objects of study can be rerun on a machine `[Our analysis]` |
| Physical samples | There is a dedicated permanent identifier, the IGSN[^igsnabout-e2] | In biology, antibodies and cell lines have their own identification standards; see [Biological sciences](../biological-sciences/README.md) |
| Model code | GMD requires the exact version at submission, or the paper is rejected[^gmdcodepolicy-e3][^gmdcodepolicy-e4] | Some areas of computer science run a separate artifact evaluation after acceptance; see the [Computer science page](../computer-science/README.md#artifact-evaluation-and-badges) |
| Expressing uncertainty | IPCC assessment reports use a fixed vocabulary[^mastrandrea2010ipcc-e4][^mastrandrea2010ipcc-e6] | Our sources cover only the IPCC's scheme `[Our analysis]` |

---

## Norms and reporting standards in this field

### Fieldwork: sort out safety and permits first

The AGU ethics policy applies to its members, staff, volunteers, and people taking part in AGU activities[^agu2023ethics-e1]. It lists the field alongside the classroom, the lab, and meetings as places where good conduct is expected[^agu2023ethics-e2]; in this policy, discrimination, harassment (including sexual harassment), and bullying **count as research misconduct**[^agu2023ethics-e3].

For a sense of the risks in the field, one reference is a survey published by Clancy and colleagues in 2014. It ran as an online questionnaire in 2013 and got 666 responses, about three-quarters of them from the US[^clancy2014survey-e1][^clancy2014survey-e3][^clancy2014survey-e4]. Nearly half the respondents were anthropologists; only 29 were geologists[^clancy2014survey-e2]. So it does not describe the situation in the Earth sciences specifically. The authors also state that a survey like this cannot be used to estimate how common these experiences are in any discipline[^clancy2014survey-e7].

Of the 666 respondents, only 37.7% remembered seeing a code of conduct at the field sites where they had worked[^clancy2014survey-e5]; harassment and assault were overwhelmingly aimed at students, postdocs, and employees[^clancy2014survey-e6]; and few knew how to report it[^clancy2014survey-e9]. The authors also point out that students sometimes work at sites not managed by their own institution, and without clearly enforced policies, standards of conduct are harder to establish there[^clancy2014survey-e8].

Before you set out, you can work through a checklist: the one Greene and colleagues wrote in 2021 for **teaching field trips**. The authors are staff and students in geography, Earth, and environmental science at UK universities[^greene2021safety-e1]; it is a preprint that has not been peer-reviewed. The points below also apply to research fieldwork; if your institution has its own field safety rules and forms, follow those `[Our analysis]`:

- **Permits**: obeying the law is only the minimum. First check whether the place you are going is protected (not just the rocks, but also the wildlife and the environment)[^greene2021safety-e2]; get access permits and sampling permits, and import/export permits for samples where needed[^greene2021safety-e3].
- **Ethics**: whose land is this; were local people involved; do they benefit, or at least not lose out[^greene2021safety-e4]. For data involving Indigenous peoples, the AGU journal data guidance asks you to consult the CARE Principles for Indigenous Data Governance[^fox2021agudata-e2].
- **Risk assessment**: have it reviewed by a third party and share it with every participant before you leave[^greene2021safety-e5]; look at records of past accidents and near misses[^greene2021safety-e7].
- **First aid**: find out whom to call in an emergency and where the nearest hospital is[^greene2021safety-e6]. First-aid training on its own is not enough[^greene2021safety-e10].
- **Schedule and people**: besides season, weather, and tides, take religious holidays into account[^greene2021safety-e9]; consider participants' identities and backgrounds when planning[^greene2021safety-e8].

### Samples: give every sample a permanent identifier

The IGSN organization sees three main reasons why sample data are hard to use over the long term: sample records in papers are incomplete, sample names are ambiguous, and nobody can find where the samples are stored[^igsnabout-e1]. The **International Generic Sample Number** (IGSN) exists to fix this: a globally unique, permanent identifier for physical samples[^igsnabout-e2], so that a sample can be tracked from registration through analysis to publication[^igsnabout-e3]. It started in the Earth sciences and is now open to all disciplines[^igsnabout-e5].

How to register: registration goes through an "allocating agent" (an organization that registers identifiers)[^igsnglossary-e1]; the IGSN organization's website lists agents that offer registration to outside users[^igsnagents-e2]. First ask your institution's data management office or sample repository whether it has its own service; if not, use an agent open to outside users `[Our analysis]`. If you cannot register yet, still give the sample name, collection site, and storage location in your paper and data, so you avoid the problems listed above `[Our analysis]`. For unique sample IDs and "chain of custody" (a record of who handled the sample at every step), see also the [Environmental engineering page](../environmental-engineering/README.md#sample-ids-and-chain-of-custody).

### Data: available at submission

What **AGU journals** require (according to the AGU journals' data and software sharing guidance written by Fox and colleagues in 2021):

- Data and software must be available to editors and reviewers at submission[^fox2021agudata-e3];
- The principle is "as open as possible, as closed as necessary"[^fox2021agudata-e2]. Sensitive data (such as fossil locality information) should still go into a repository with access controls[^fox2021agudata-e4]. "Data available from the authors on request" is not acceptable, and neither is a link to the home page of a large website[^fox2021agudata-e6];
- Both raw and processed data should be cited in the reference list, so that the people who contributed the data get credit[^fox2021agudata-e12];
- Start choosing a repository when you write the grant proposal and data management plan[^fox2021agudata-e9]; for data over 1 TB, some repositories will preserve it for a fee, which should go in the budget[^fox2021agudata-e10]; librarians can help you choose a repository[^fox2021agudata-e11].
- The AGU ethics policy adds that a paper should be written in enough detail for peers to repeat the work, and should state any restrictions on data use[^agu2023ethics-e7].

**Why is this worth doing carefully?** A 2019 study by Stagge and colleagues sampled 360 of the 1,989 papers published in 2017 in six hydrology and water resources journals[^stagge2019assessing-e1]:

- 70.3% claimed some materials were available, but only 48.6% of those could actually be obtained online[^stagge2019assessing-e9];
- only 1.6% could be reproduced from the available materials; extrapolated to all 1,989 papers, the reproducible share is between 0.6% and 6.8%[^stagge2019assessing-e8];
- a common reason reproduction failed was file paths hard-coded to the author's computer[^stagge2019assessing-e4]; other papers pointed only to a general data portal, or depended on expensive commercial software[^stagge2019assessing-e11].

In every journal, papers that provided code or data outnumbered papers that provided instructions for using them by a factor of 2 to 3[^stagge2019assessing-e12]. The authors suggest using their survey as a checklist to check your own paper before you submit[^stagge2019assessing-e13]. For general practice in organizing data, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

### Numerical models: if the code isn't ready, the paper isn't ready

This is the view of the GMD editors in a 2019 editorial[^gmd2019editorial-e7]. Their reasons:

- Almost all nontrivial code contains bugs[^gmd2019editorial-e2]; two programs implementing the same algorithm do not necessarily give the same result, and without the source code you cannot find where the difference comes from[^gmd2019editorial-e3]. Source code alone is not enough either: you also need all the input data and every step from the raw data to each point on a figure[^gmd2019editorial-e4];
- Interactive manual processing and plotting breaks the "chain of provenance" between the model and the paper, and the only remedy is to run and process everything with scripts[^gmd2019editorial-e5]; if code is not managed well, you may later be unable to recover the exact version used in the paper[^gmd2019editorial-e8].

**What GMD requires** (applies only to manuscripts submitted to GMD):

- A "Code and data availability" section at the end of the paper[^gmdcodepolicy-e1] that cites the **exact version** of all code and data, deposited in a permanent public archive[^gmdcodepolicy-e2];
- Anything that cannot be made public must be provided privately to the editor and reviewers; if that is not possible, the paper is rejected[^gmdcodepolicy-e3];
- Provide scripts covering every step of data processing[^gmdcodepolicy-e5]; if the code or data change during revision, archive the new version too[^gmdcodepolicy-e7]. Code hosting platforms such as GitHub are good for development but not for archiving[^gmdcodepolicy-e6] (the AGU journal guidance does not accept them as repositories either[^fox2021agudata-e5]); you may additionally give a download link to the latest version[^gmd2019editorial-e10];
- Reviewers may check whether the model is easy to download, compile, and run on the test cases[^gmdcodepolicy-e8].

What **AGU journals** require for modeling studies: provide enough that "a reader with sufficient computing resources could repeat your simulations"[^fox2021agudata-e7]; huge model outputs are hard to store in full, and storing enough to produce the paper's figures and tables is generally sufficient[^fox2021agudata-e8]; put the analysis and plotting code on an open platform and archive it in a repository such as Zenodo[^fox2021agudata-e15].

### Expressing uncertainty: the IPCC's language

The AGU ethics policy requires members to include a characterization of uncertainty when they report results[^agu2023ethics-e4], and to carefully document methods, assumptions, and uncertainties[^agu2023ethics-e8]. A vocabulary you will often meet in climate science comes from the IPCC's 2010 guidance note for lead authors of the Fifth Assessment Report (Mastrandrea et al. 2010)[^mastrandrea2010ipcc-e1]. It uses two metrics:

- **Confidence**: judged from the type, amount, quality, and consistency of the evidence and the degree of agreement, and expressed in words[^mastrandrea2010ipcc-e2], on five levels: very low, low, medium, high, and very high[^mastrandrea2010ipcc-e4]. Confidence is not a probability, and it is not the same as statistical confidence[^mastrandrea2010ipcc-e5].
- **Likelihood**: quantified uncertainty expressed as a probability[^mastrandrea2010ipcc-e3], with each term mapped to a probability range[^mastrandrea2010ipcc-e6]:

| Term | Probability |
|---|---|
| virtually certain | 99%–100% |
| very likely | 90%–100% |
| likely | 66%–100% |
| about as likely as not | 33%–66% |
| unlikely | 0–33% |
| very unlikely | 0–10% |
| exceptionally unlikely | 0–1% |

The guidance also reminds report authors:

- "About as likely as not" must not be used to mean "we don't know"[^mastrandrea2010ipcc-e7]; when there is enough information, it is better to give a probability distribution or range directly[^mastrandrea2010ipcc-e8].
- When making expert judgments, give a "traceable account" of what the judgment is based on[^mastrandrea2010ipcc-e9]; watch out for groupthink and overconfidence in group discussions[^mastrandrea2010ipcc-e10]; experts tend to underestimate structural uncertainty, the uncertainty that comes from incomplete understanding of the system[^mastrandrea2010ipcc-e11].
- Readers understand the same finding differently depending on how it is framed[^mastrandrea2010ipcc-e12], and they also adjust how they read these terms according to how severe the consequences are[^mastrandrea2010ipcc-e14]. The guidance encourages giving information about the "tails" of the distributions of key variables[^mastrandrea2010ipcc-e13].

`[Our analysis]` This vocabulary was set for IPCC assessment reports. Whether and how to use it in an ordinary research paper depends on your target journal and your advisor. If you use it, cite where it comes from, so readers do not take "likely" in its everyday sense.

**Speaking to the public**: the AGU ethics policy requires that findings be announced to the public only when the evidence is strong enough to be published in the scholarly literature[^agu2023ethics-e10], and holds that members have a duty to explain issues such as natural resources and hazards to the public responsibly, accurately, and clearly[^agu2023ethics-e6].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by its central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The grouping and the "What it looks like in this field" column of the table below are our own summary; each standard represents only the institution, journal, or paper cited in its footnote `[Our analysis]`.

| Strategy | What it looks like in this field | Common evidence and standards | How to do it |
|---|---|---|---|
| [Description](../../05_research-strategies/observe_describe.md) | Field observation and sampling, or analysis of station network and satellite data, to establish the current state of a place or system | The US Environmental Protection Agency's (EPA) planning guidance lists "estimation" (for example, of the mean concentration of a pollutant) as one use of data[^epa2006dqo-e2]; sample records must be complete and sample names unambiguous[^igsnabout-e1]; for AGU journals, data must be available to editors and reviewers at submission[^fox2021agudata-e3] | [Field studies: observation and sampling](../../06_methods/field_study.md), [Data science research](../../06_methods/data_science.md) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Field manipulation experiments: applying or comparing treatments in the field, for example comparing grazed and ungrazed plots[^davies2015pseudoreplication-e11] | Check first for **pseudoreplication**: using statistical tests of a treatment effect when the treatments are not truly replicated, or the replicates are not independent[^davies2015pseudoreplication-e1]. In expensive landscape-scale manipulations, this is a real but contested problem[^davies2015pseudoreplication-e6]; for how to design and write up such a study, see below the table | [Field observation studies](../../06_methods/field_study.md#step-2-design-the-sampling-where-when-and-how-much), [Field trials](../agriculture/practices/field_trial.md) (an agricultural practice, useful as a reference) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Inferring causation from observational or model data: the Earth system is so large that replicated interventional experiments are infeasible or ethically problematic[^runge2019inferring-e1], so most branches currently use computer simulation experiments instead[^runge2019inferring-e2] | Correlation and regression are still the most common tools; if you use causal inference methods, check the assumptions they rely on first[^runge2019inferring-e3] (the common ones are listed below the table) | [Data science research](../../06_methods/data_science.md), [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Building and improving](../../05_research-strategies/build_improve.md) | Developing or improving numerical models | GMD requires the exact version of code and data at submission, or the paper is rejected[^gmdcodepolicy-e3]; reviewers may check whether the model can be downloaded, compiled, and run on the test cases[^gmdcodepolicy-e8]; AGU journals require enough that "a reader with sufficient computing resources could repeat the simulations"[^fox2021agudata-e7] | [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Model intercomparison projects: coordinating the design and distribution of global climate model simulations[^eyring2016cmip6-e1] to understand climate change in a multi-model context[^eyring2016cmip6-e4] | Models taking part in CMIP6 must run a set of prescribed experiments and use common data standards[^eyring2016cmip6-e2] | [Quantitative simulation](../../06_methods/simulation_study.md), [Model intercomparison projects](#model-intercomparison-projects) above |
| [Synthesis](../../05_research-strategies/synthesize.md) | IPCC assessment reports, with uncertainty guidance written specifically for their authors[^mastrandrea2010ipcc-e1] | Confidence is judged from the type, amount, quality, and consistency of the evidence and the degree of agreement[^mastrandrea2010ipcc-e2]; likelihood terms map to fixed probability ranges[^mastrandrea2010ipcc-e6] | [The IPCC's language](#expressing-uncertainty-the-ipccs-language) above, [Review studies](../../06_methods/review_study.md) |

How to use this table `[Our analysis]`: a project often has field, lab, and modeling parts at once (see above). Choose the main strategy from your central claim, and do each of the other parts to its own standards. Our sources do not say whether societies or journals in this field have their own criteria for judging causal studies; the closest is the IPCC expert meeting's guidance document described below, which covers only climate change "detection and attribution".

The standards in the two "Causal explanation" rows come from two perspective papers; they are the authors' recommendations, not rules set by a society or journal `[Our analysis]`:

- **Field manipulation experiments: Davies and Gray 2015 (ecology).** They recommend defining the hypothesis and the population of interest carefully, acknowledging the limits of statistical inference, and using statistical approaches such as nesting and random effects[^davies2015pseudoreplication-e3]. For how to choose control plots and how to report them in the paper, see [Field observation studies: dealing with events that cannot be replicated](../../06_methods/field_study.md#step-10-dealing-with-events-that-cant-be-repeated).
- **Inferring causation from data: Runge and colleagues 2019 (Earth system science).** Many causal inference methods for time series assume that causes precede their effects and that all direct common drivers have been observed[^runge2019inferring-e4]. Before you use one, think through whether these assumptions might fail: relevant drivers often go unmeasured, and unmeasured drivers can produce spurious links[^runge2019inferring-e5]; if the time resolution is too coarse, causal links can look contemporaneous or even form cycles[^runge2019inferring-e7]. By contrast, conclusions of the form "there is no causal link" need weaker assumptions and are more robust[^runge2019inferring-e6]. For the general logic of causal inference, see [Causal explanation](../../05_research-strategies/explain_causality.md).

**Climate change "detection and attribution": the IPCC expert meeting's guidance document (Hegerl et al. 2010).** In 2009, IPCC Working Groups I and II held an expert meeting. The resulting *Good Practice Guidance Paper on Detection and Attribution* is written for authors of future IPCC reports and gives criteria for judging the quality of studies and recommendations on good practice[^hegerl2010good-e2]. It is not a submission requirement of any society or journal; the report also notes that it does not imply endorsement by the IPCC working groups or the Panel, and was not formally reviewed by the IPCC[^hegerl2010good-e1]. If you do detection and attribution studies of climate change and its impacts, you can use the points below to check your own work `[Our analysis]`:

- **Keep detection and attribution apart.** Detection means showing that the climate, or a system affected by climate, has changed in a statistically defined sense, without giving a reason; attribution means evaluating how much each of several causes contributed, with a statement of statistical confidence, and it requires that the change be detected first[^hegerl2010good-e3].
- **State which cause you attribute the change to, and rule out other explanations.** Conclusions are more credible when quantitative results are robust and the processes in the causal chain are well understood[^hegerl2010good-e6]. A **confounding factor** is something that affects the system you study but is not accounted for in the study design, and it can lead you to a wrong causal conclusion[^hegerl2010good-e4]. How thoroughly you consider other possible causes, confounding factors, and the limitations of observational data affects how much confidence the attribution deserves; if you attribute with models, assess whether the models represent this causal link correctly[^hegerl2010good-e7].
- **If attribution goes in several steps, say so, and give a [confidence](#expressing-uncertainty-the-ipccs-language) level for each step.** For example, first attribute a decline in calcification in marine organisms to a change in ocean chemistry, then attribute the change in ocean chemistry to rising atmospheric carbon dioxide; the overall conclusion is generally no stronger than its weakest step[^hegerl2010good-e5].
- **Document every step**, so others can check and repeat it[^hegerl2010good-e8].

---

## Research methods common in this field

The grouping below is our own analysis `[Our analysis]`. For field observation and sampling, see [Field studies: observation and sampling](../../06_methods/field_study.md) (a cross-field method). For numerical simulation, model development, and multi-model comparison, see [Quantitative simulation](../../06_methods/simulation_study.md); for the comparison logic, [Benchmarking](../computer-science/practices/benchmarking.md) in computer science is a useful reference; note that some Earth system models have restrictive licenses[^gmd2019editorial-e6]. For analyzing existing observational data, see [Data science research](../../06_methods/data_science.md), and for spatial data, [Spatial analysis](../geography/practices/spatial_analysis.md) in geography; when submitting to AGU journals, you must give the specific source of the data, not just a portal website[^fox2021agudata-e6]. Lab analysis of samples and data papers (publishing a curated dataset, with the dataset itself peer-reviewed[^gmdcodepolicy-e10]) do not yet have a methods page of their own; for measurement quality control, see [Environmental engineering](../environmental-engineering/README.md).

---

## Advice for newcomers

1. **Before your first field trip, finish the risk assessment and get every permit.** That means access and sampling permits, plus import/export permits where needed[^greene2021safety-e3]; have the risk assessment reviewed, and share it with everyone going[^greene2021safety-e5].
2. **Before you leave, find out how to report misconduct.** In Clancy's 2014 survey of 666 people, few respondents knew how to report[^clancy2014survey-e9]; find out who manages the site and which code of conduct applies `[Our analysis]`.
3. **Label and record samples on the day you collect them** `[Our analysis]`. Incomplete records and ambiguous names are the main reasons sample data are hard to use[^igsnabout-e1]; register IGSNs if you can[^igsnabout-e2].
4. **From day one, do all data processing and plotting with scripts.** Manual processing breaks the chain of provenance[^gmd2019editorial-e5]; do not hard-code paths to your own computer[^stagge2019assessing-e4].
5. **Keep code and data together, with instructions for using them.** In Stagge's 2019 sample, far more papers provided code or data than provided instructions[^stagge2019assessing-e12]; projects that package code and data together are easier to reproduce[^stagge2019assessing-e14].
6. **Archive your code and data and get a DOI before you submit.** Both GMD and AGU journals require them to be available at submission[^gmdcodepolicy-e4][^fox2021agudata-e3]; GitHub does not count as an archive[^gmdcodepolicy-e6].
7. **Before you write "likely" or "high confidence", check the IPCC definitions.** These words have fixed meanings in the IPCC vocabulary[^mastrandrea2010ipcc-e5][^mastrandrea2010ipcc-e6].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Getting an access permit but no sampling or import/export permit | Every permit has to be obtained, one by one[^greene2021safety-e3] |
| Sample names only you can understand, incomplete records | These are exactly the main reasons sample data are hard to use[^igsnabout-e1] |
| A data statement that says "available from the authors on request" | AGU journals do not accept it[^fox2021agudata-e6]; among the sampled 2017 papers in two hydrology journals, *Hydrology and Earth System Sciences* (HESS) and *Water Resources Research* (WRR), 38.5%–40.2% of materials were available only by request to the first author[^stagge2019assessing-e10] |
| Giving only a GitHub link, with no archive | GitHub is not an archiving service[^gmdcodepolicy-e6][^fox2021agudata-e5] |
| Using "about as likely as not" to mean "we don't know" | The IPCC guidance explicitly rules this out[^mastrandrea2010ipcc-e7] |
| Posting a preprint without checking the journals you might submit to later | A preprint cannot be deleted[^eartharxivfaq-e1]; EarthArXiv asks you to confirm first that all those journals accept preprints[^eartharxivfaq-e5] |

---

## Further reading

- **AGU Scientific Integrity and Professional Ethics (2023 update)**: AGU's ethics policy. For how it treats harassment, read Section III.D.
- **Data and Software Sharing Guidance for Authors Submitting to AGU Journals (Fox et al. 2021)**: use it to write your data and software statements before submitting to an AGU journal.
- **GMD's code and data policy and its 2019 editorial**: why code should be public and how to archive it. **The IPCC uncertainty guidance note (Mastrandrea et al. 2010)**: 4 pages on confidence and likelihood.
- **Stagge et al. 2019**: a reproducibility check of six hydrology journals that shows the concrete reasons why "the materials are public but the results still can't be reproduced". **EarthArXiv FAQ and moderation policy**: read before you post a preprint.
- **Greene et al. 2021, Clancy et al. 2014**: the first is a safety checklist for teaching field trips by UK authors (a preprint that has not been peer-reviewed); the second is an online survey of harassment in the field whose respondents were mostly anthropologists.

[^fox2021agudata-e2]: Fox et al. 2021, Introduction. [Evidence](../../../sources/notes/fox2021agudata.md#e2)
[^fox2021agudata-e3]: Fox et al. 2021, §1. [Evidence](../../../sources/notes/fox2021agudata.md#e3)
[^fox2021agudata-e4]: Fox et al. 2021, §1. [Evidence](../../../sources/notes/fox2021agudata.md#e4)
[^fox2021agudata-e5]: Fox et al. 2021, Software Availability Statement. [Evidence](../../../sources/notes/fox2021agudata.md#e5)
[^fox2021agudata-e6]: Fox et al. 2021, §6. [Evidence](../../../sources/notes/fox2021agudata.md#e6)
[^fox2021agudata-e7]: Fox et al. 2021, §2. [Evidence](../../../sources/notes/fox2021agudata.md#e7)
[^fox2021agudata-e8]: Fox et al. 2021, §2. [Evidence](../../../sources/notes/fox2021agudata.md#e8)
[^fox2021agudata-e9]: Fox et al. 2021, §3. [Evidence](../../../sources/notes/fox2021agudata.md#e9)
[^fox2021agudata-e10]: Fox et al. 2021, §1, Large Data. [Evidence](../../../sources/notes/fox2021agudata.md#e10)
[^fox2021agudata-e11]: Fox et al. 2021, §3. [Evidence](../../../sources/notes/fox2021agudata.md#e11)
[^fox2021agudata-e12]: Fox et al. 2021, §1, Data Citation. [Evidence](../../../sources/notes/fox2021agudata.md#e12)
[^fox2021agudata-e15]: Fox et al. 2021, §2. [Evidence](../../../sources/notes/fox2021agudata.md#e15)
[^eyring2016cmip6-e1]: Eyring et al. 2016, Abstract. [Evidence](../../../sources/notes/eyring2016cmip6.md#e1)
[^eyring2016cmip6-e2]: Eyring et al. 2016, Abstract. [Evidence](../../../sources/notes/eyring2016cmip6.md#e2)
[^eyring2016cmip6-e3]: Eyring et al. 2016, Abstract. [Evidence](../../../sources/notes/eyring2016cmip6.md#e3)
[^eyring2016cmip6-e4]: Eyring et al. 2016, §1. [Evidence](../../../sources/notes/eyring2016cmip6.md#e4)
[^gmd2019editorial-e2]: GMD Executive Editors 2019, §2. [Evidence](../../../sources/notes/gmd2019editorial.md#e2)
[^gmd2019editorial-e3]: GMD Executive Editors 2019, §2. [Evidence](../../../sources/notes/gmd2019editorial.md#e3)
[^gmd2019editorial-e4]: GMD Executive Editors 2019, §3.1. [Evidence](../../../sources/notes/gmd2019editorial.md#e4)
[^gmd2019editorial-e5]: GMD Executive Editors 2019, §3.2. [Evidence](../../../sources/notes/gmd2019editorial.md#e5)
[^gmd2019editorial-e6]: GMD Executive Editors 2019, §3.3. [Evidence](../../../sources/notes/gmd2019editorial.md#e6)
[^gmd2019editorial-e7]: GMD Executive Editors 2019, §3.4. [Evidence](../../../sources/notes/gmd2019editorial.md#e7)
[^gmd2019editorial-e8]: GMD Executive Editors 2019, §4. [Evidence](../../../sources/notes/gmd2019editorial.md#e8)
[^gmd2019editorial-e9]: GMD Executive Editors 2019, §3.5. [Evidence](../../../sources/notes/gmd2019editorial.md#e9)
[^gmd2019editorial-e10]: GMD Executive Editors 2019, §3.5. [Evidence](../../../sources/notes/gmd2019editorial.md#e10)
[^agu2023ethics-e1]: AGU 2023, I. Executive Summary. [Evidence](../../../sources/notes/agu2023ethics.md#e1)
[^agu2023ethics-e2]: AGU 2023, II. Preamble. [Evidence](../../../sources/notes/agu2023ethics.md#e2)
[^agu2023ethics-e3]: AGU 2023, III.D. [Evidence](../../../sources/notes/agu2023ethics.md#e3)
[^agu2023ethics-e4]: AGU 2023, III.B, item 3. [Evidence](../../../sources/notes/agu2023ethics.md#e4)
[^agu2023ethics-e6]: AGU 2023, III.B, item 15. [Evidence](../../../sources/notes/agu2023ethics.md#e6)
[^agu2023ethics-e7]: AGU 2023, VI.C, item 2. [Evidence](../../../sources/notes/agu2023ethics.md#e7)
[^agu2023ethics-e8]: AGU 2023, VI.C, item 4. [Evidence](../../../sources/notes/agu2023ethics.md#e8)
[^agu2023ethics-e9]: AGU 2023, VI.C, item 10. [Evidence](../../../sources/notes/agu2023ethics.md#e9)
[^agu2023ethics-e10]: AGU 2023, VI.E, item 2. [Evidence](../../../sources/notes/agu2023ethics.md#e10)
[^gmdcodepolicy-e1]: Geoscientific Model Development (GMD) code and data policy, Core principles. [Evidence](../../../sources/notes/gmdcodepolicy.md#e1)
[^gmdcodepolicy-e2]: Geoscientific Model Development (GMD) code and data policy, Core principles. [Evidence](../../../sources/notes/gmdcodepolicy.md#e2)
[^gmdcodepolicy-e3]: Geoscientific Model Development (GMD) code and data policy, Core principles. [Evidence](../../../sources/notes/gmdcodepolicy.md#e3)
[^gmdcodepolicy-e4]: Geoscientific Model Development (GMD) code and data policy, Core principles. [Evidence](../../../sources/notes/gmdcodepolicy.md#e4)
[^gmdcodepolicy-e5]: Geoscientific Model Development (GMD) code and data policy, Scope. [Evidence](../../../sources/notes/gmdcodepolicy.md#e5)
[^gmdcodepolicy-e6]: Geoscientific Model Development (GMD) code and data policy, Archive standards. [Evidence](../../../sources/notes/gmdcodepolicy.md#e6)
[^gmdcodepolicy-e7]: Geoscientific Model Development (GMD) code and data policy, Archive standards. [Evidence](../../../sources/notes/gmdcodepolicy.md#e7)
[^gmdcodepolicy-e8]: Geoscientific Model Development (GMD) code and data policy, Scope. [Evidence](../../../sources/notes/gmdcodepolicy.md#e8)
[^gmdcodepolicy-e10]: Geoscientific Model Development (GMD) code and data policy, Copernicus data policy supplement. [Evidence](../../../sources/notes/gmdcodepolicy.md#e10)
[^eartharxivabout-e1]: EarthArXiv About. [Evidence](../../../sources/notes/eartharxivabout.md#e1)
[^eartharxivabout-e2]: EarthArXiv About. [Evidence](../../../sources/notes/eartharxivabout.md#e2)
[^eartharxivabout-e3]: EarthArXiv About. [Evidence](../../../sources/notes/eartharxivabout.md#e3)
[^eartharxivfaq-e1]: EarthArXiv FAQ, citation question. [Evidence](../../../sources/notes/eartharxivfaq.md#e1)
[^eartharxivfaq-e2]: EarthArXiv FAQ, citation question. [Evidence](../../../sources/notes/eartharxivfaq.md#e2)
[^eartharxivfaq-e4]: EarthArXiv FAQ, journal policy question. [Evidence](../../../sources/notes/eartharxivfaq.md#e4)
[^eartharxivfaq-e5]: EarthArXiv FAQ, journal policy question. [Evidence](../../../sources/notes/eartharxivfaq.md#e5)
[^eartharxivfaq-e6]: EarthArXiv FAQ, ESSOAr question. [Evidence](../../../sources/notes/eartharxivfaq.md#e6)
[^eartharxivfaq-e7]: EarthArXiv FAQ, supplementary material question. [Evidence](../../../sources/notes/eartharxivfaq.md#e7)
[^eartharxivmoderation-e1]: EarthArXiv moderation policy, What does EarthArXiv accept? [Evidence](../../../sources/notes/eartharxivmoderation.md#e1)
[^eartharxivmoderation-e2]: EarthArXiv moderation policy, Basic Requirements. [Evidence](../../../sources/notes/eartharxivmoderation.md#e2)
[^eartharxivmoderation-e3]: EarthArXiv moderation policy, What does EarthArXiv accept? [Evidence](../../../sources/notes/eartharxivmoderation.md#e3)
[^igsnabout-e1]: IGSN e.V., About IGSNs. [Evidence](../../../sources/notes/igsnabout.md#e1)
[^igsnabout-e2]: IGSN e.V., About IGSNs. [Evidence](../../../sources/notes/igsnabout.md#e2)
[^igsnabout-e3]: IGSN e.V., About IGSNs. [Evidence](../../../sources/notes/igsnabout.md#e3)
[^igsnabout-e4]: IGSN e.V., About IGSNs. [Evidence](../../../sources/notes/igsnabout.md#e4)
[^igsnabout-e5]: IGSN e.V., About IGSNs. [Evidence](../../../sources/notes/igsnabout.md#e5)
[^igsnglossary-e1]: IGSN e.V., Glossary, Allocating Agent. [Evidence](../../../sources/notes/igsnglossary.md#e1)
[^igsnagents-e2]: IGSN e.V., IGSN Agents and Registration, GFZ Data Services and Lithodat. [Evidence](../../../sources/notes/igsnagents.md#e2)
[^greene2021safety-e1]: Greene et al. 2021, §1. [Evidence](../../../sources/notes/greene2021safety.md#e1)
[^greene2021safety-e2]: Greene et al. 2021, §4.2.2. [Evidence](../../../sources/notes/greene2021safety.md#e2)
[^greene2021safety-e3]: Greene et al. 2021, §4.2.2. [Evidence](../../../sources/notes/greene2021safety.md#e3)
[^greene2021safety-e4]: Greene et al. 2021, §4.2.2. [Evidence](../../../sources/notes/greene2021safety.md#e4)
[^greene2021safety-e5]: Greene et al. 2021, §4.2.6. [Evidence](../../../sources/notes/greene2021safety.md#e5)
[^greene2021safety-e6]: Greene et al. 2021, §4.2.6. [Evidence](../../../sources/notes/greene2021safety.md#e6)
[^greene2021safety-e7]: Greene et al. 2021, §4.2.6. [Evidence](../../../sources/notes/greene2021safety.md#e7)
[^greene2021safety-e8]: Greene et al. 2021, Abstract. [Evidence](../../../sources/notes/greene2021safety.md#e8)
[^greene2021safety-e9]: Greene et al. 2021, §4.2.5. [Evidence](../../../sources/notes/greene2021safety.md#e9)
[^greene2021safety-e10]: Greene et al. 2021, §4.1.1. [Evidence](../../../sources/notes/greene2021safety.md#e10)
[^clancy2014survey-e1]: Clancy et al. 2014, Abstract. [Evidence](../../../sources/notes/clancy2014survey.md#e1)
[^clancy2014survey-e2]: Clancy et al. 2014, Results. [Evidence](../../../sources/notes/clancy2014survey.md#e2)
[^clancy2014survey-e3]: Clancy et al. 2014, Results. [Evidence](../../../sources/notes/clancy2014survey.md#e3)
[^clancy2014survey-e4]: Clancy et al. 2014, Methods. [Evidence](../../../sources/notes/clancy2014survey.md#e4)
[^clancy2014survey-e5]: Clancy et al. 2014, Results. [Evidence](../../../sources/notes/clancy2014survey.md#e5)
[^clancy2014survey-e6]: Clancy et al. 2014, Results. [Evidence](../../../sources/notes/clancy2014survey.md#e6)
[^clancy2014survey-e7]: Clancy et al. 2014, Discussion. [Evidence](../../../sources/notes/clancy2014survey.md#e7)
[^clancy2014survey-e8]: Clancy et al. 2014, Discussion. [Evidence](../../../sources/notes/clancy2014survey.md#e8)
[^clancy2014survey-e9]: Clancy et al. 2014, Abstract. [Evidence](../../../sources/notes/clancy2014survey.md#e9)
[^stagge2019assessing-e1]: Stagge et al. 2019, Abstract. [Evidence](../../../sources/notes/stagge2019assessing.md#e1)
[^stagge2019assessing-e8]: Stagge et al. 2019, Abstract. [Evidence](../../../sources/notes/stagge2019assessing.md#e8)
[^stagge2019assessing-e9]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e9)
[^stagge2019assessing-e10]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e10)
[^stagge2019assessing-e4]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e4)
[^stagge2019assessing-e11]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e11)
[^stagge2019assessing-e12]: Stagge et al. 2019, Discussion. [Evidence](../../../sources/notes/stagge2019assessing.md#e12)
[^stagge2019assessing-e13]: Stagge et al. 2019, Discussion. [Evidence](../../../sources/notes/stagge2019assessing.md#e13)
[^stagge2019assessing-e14]: Stagge et al. 2019, Discussion. [Evidence](../../../sources/notes/stagge2019assessing.md#e14)
[^mastrandrea2010ipcc-e1]: Mastrandrea et al. 2010, Introduction. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e1)
[^mastrandrea2010ipcc-e2]: Mastrandrea et al. 2010, Introduction. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e2)
[^mastrandrea2010ipcc-e3]: Mastrandrea et al. 2010, Introduction. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e3)
[^mastrandrea2010ipcc-e4]: Mastrandrea et al. 2010, paragraph 9. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e4)
[^mastrandrea2010ipcc-e5]: Mastrandrea et al. 2010, paragraph 9. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e5)
[^mastrandrea2010ipcc-e6]: Mastrandrea et al. 2010, paragraph 10 and Table 1. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e6)
[^mastrandrea2010ipcc-e7]: Mastrandrea et al. 2010, paragraph 10. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e7)
[^mastrandrea2010ipcc-e8]: Mastrandrea et al. 2010, paragraph 10. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e8)
[^mastrandrea2010ipcc-e9]: Mastrandrea et al. 2010, paragraph 2. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e9)
[^mastrandrea2010ipcc-e10]: Mastrandrea et al. 2010, paragraph 3. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e10)
[^mastrandrea2010ipcc-e11]: Mastrandrea et al. 2010, paragraph 6. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e11)
[^mastrandrea2010ipcc-e12]: Mastrandrea et al. 2010, paragraph 4. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e12)
[^mastrandrea2010ipcc-e13]: Mastrandrea et al. 2010, Introduction. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e13)
[^mastrandrea2010ipcc-e14]: Mastrandrea et al. 2010, paragraph 10. [Evidence](../../../sources/notes/mastrandrea2010ipcc.md#e14)
[^epa2006dqo-e2]: U.S. Environmental Protection Agency (EPA) 2006 (QA/G-4), Introduction, PDF p. 16. [Evidence](../../../sources/notes/epa2006dqo.md#e2)
[^davies2015pseudoreplication-e1]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e1)
[^davies2015pseudoreplication-e3]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e3)
[^davies2015pseudoreplication-e6]: Davies & Gray 2015, Abstract. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e6)
[^davies2015pseudoreplication-e11]: Davies & Gray 2015, Discussion, Question 1. [Evidence](../../../sources/notes/davies2015pseudoreplication.md#e11)
[^runge2019inferring-e1]: Runge et al. 2019, Introduction. [Evidence](../../../sources/notes/runge2019inferring.md#e1)
[^runge2019inferring-e2]: Runge et al. 2019, Introduction. [Evidence](../../../sources/notes/runge2019inferring.md#e2)
[^runge2019inferring-e3]: Runge et al. 2019, Introduction. [Evidence](../../../sources/notes/runge2019inferring.md#e3)
[^runge2019inferring-e4]: Runge et al. 2019, Causal inference methods. [Evidence](../../../sources/notes/runge2019inferring.md#e4)
[^runge2019inferring-e5]: Runge et al. 2019, Challenges. [Evidence](../../../sources/notes/runge2019inferring.md#e5)
[^runge2019inferring-e6]: Runge et al. 2019, Challenges. [Evidence](../../../sources/notes/runge2019inferring.md#e6)
[^runge2019inferring-e7]: Runge et al. 2019, Challenges. [Evidence](../../../sources/notes/runge2019inferring.md#e7)
[^hegerl2010good-e1]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), report cover. [Evidence](../../../sources/notes/hegerl2010good.md#e1)
[^hegerl2010good-e2]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), Executive Summary, p. 1. [Evidence](../../../sources/notes/hegerl2010good.md#e2)
[^hegerl2010good-e3]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), §1, p. 2. [Evidence](../../../sources/notes/hegerl2010good.md#e3)
[^hegerl2010good-e4]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), §1, p. 2. [Evidence](../../../sources/notes/hegerl2010good.md#e4)
[^hegerl2010good-e5]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), §2 II, p. 3. [Evidence](../../../sources/notes/hegerl2010good.md#e5)
[^hegerl2010good-e6]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), §2, p. 4. [Evidence](../../../sources/notes/hegerl2010good.md#e6)
[^hegerl2010good-e7]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), §2, p. 5. [Evidence](../../../sources/notes/hegerl2010good.md#e7)
[^hegerl2010good-e8]: Hegerl et al. 2010 (Intergovernmental Panel on Climate Change (IPCC) expert meeting report on detection and attribution), §2, p. 5. [Evidence](../../../sources/notes/hegerl2010good.md#e8)
