# Civil engineering: field overview

This page explains how research actually runs in civil engineering (structural, geotechnical, transportation, water resources, construction management, and related areas): large-scale and field tests have to be scheduled, approved, and run safely; numerical models have to agree with tests; and some results end up in design codes and standards `[Our analysis]`. For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies this field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). This page covers only what is specific to civil engineering.

Every rule cited on this page comes from a specific US body: the code of ethics, journal policies, and standards of the American Society of Civil Engineers (ASCE); documents from two test facilities funded by the US National Science Foundation; and a fiscal year 2008 budget document from the US National Institute of Standards and Technology. They show what those bodies did at the time, not universal conventions of civil engineering. Professional societies, journals, and code systems in China and other countries, and the rules of your own institution, may differ; follow your local rules `[Our analysis]`.

**After reading this page, you should be able to:**

- explain the role that large-scale tests, field tests, and numerical simulation each play in research in this field;
- tell model verification, validation, and calibration apart, and not mistake tuning parameters for proof that a model is reliable;
- understand how research results relate to design codes and standards;
- know, using ASCE as the example, what the rules say about the code of ethics, data availability statements, and turning conference papers into journal papers;
- put safety ahead of schedule in large-scale and field tests.

---

## How research works in this field

The subfields of civil engineering do research in very different ways. Structural engineers often load-test components and whole structures; geotechnical engineers run both laboratory soil tests and field tests; transportation research relies heavily on traffic data and models; water resources research is mostly hydrologic data and computational models; construction management often works with companies on case studies and surveys `[Our analysis]`. Not everything below applies to every subfield, so when you join a group, ask your advisor how your subfield usually works `[Our analysis]`.

### Large-scale tests: long queues, approvals, and preparation

Some structural and geotechnical research calls for large-scale or even full-scale (as big as the real structure) tests, which often need a dedicated large test facility `[Our analysis]`. The examples below are two facilities of the **Natural Hazards Engineering Research Infrastructure** (NHERI), funded by the US National Science Foundation. They describe only what these two facilities say in their own documents; for other laboratories, follow your institution's procedures `[Our analysis]`.

**The Real-Time Multi-Directional (RTMD) experimental facility at Lehigh University** (large-scale structural testing; based on its user guide of November 2016):

- It supports **hybrid simulation**, which combines large-scale physical models with computer-based numerical models in one test[^nherilehigh2016users-e1].
- When you write a proposal, contact the facility's operations manager early for help with planning, scheduling, and cost estimates[^nherilehigh2016users-e9].
- Facility staff review every proposed test beforehand to make sure it puts no one at risk and will not damage equipment. You submit a **test matrix** (a planned list of every test and how it will be run) and state the damage you expect the specimen to suffer in each test; nothing starts until the test matrix is approved in writing[^nherilehigh2016users-e2], and you may not deviate from it without approval[^nherilehigh2016users-e3].
- Control programs must first be developed and validated in simulation mode with the hydraulics off, and every part must be tested safely before the real test[^nherilehigh2016users-e4]. Software used in a test must be validated before it is installed on the control system, and the algorithms it is based on must be shown to be stable[^nherilehigh2016users-e5].

**The field testing facility at the University of Texas at Austin** (based on its safety plan, version 2.3, August 2020) uses large mobile shaker trucks to run tests at sites across the US[^nheriutexas2020safety-e1]. The safety plan says a typical project there is the result of months, sometimes years, of preparation, and funding, organization, scheduling, and logistics can leave a very narrow window for finishing the project[^nheriutexas2020safety-e2].

What this means for you: a chance to run a large-scale test is precious, and once a specimen fails you cannot run it again `[Our analysis]`. Before you start, work out the instrumentation layout, the loading protocol, the failure sequence you expect, and how data will be recorded, and run a numerical prediction first `[Our analysis]`. For general scheduling methods, see the Part 2 chapter [Writing a research plan](../../02_do-the-project/03_research-plan.md). The Lehigh facility also posts all ongoing and newly funded projects on its website so that other researchers can spot "payload project" opportunities[^nherilehigh2016users-e8]. A payload project adds your own study on top of someone else's test `[Our analysis]`. For students with little funding, this is one way to take part in large-scale testing `[Our analysis]`.

### Field tests and field monitoring: the site is not yours

When you test or monitor a real structure on a real site, you also have to deal with the owner and the people around it `[Our analysis]`. The University of Texas facility's 2020 safety plan is an example:

- Before testing, the principal investigator of the user team must survey the site to identify hazards and send the test plan to the facility one month in advance[^nheriutexas2020safety-e4];
- the user is responsible for the safety of the site and nearby structures, and the principal investigator must obtain site access permits and liability insurance[^nheriutexas2020safety-e5];
- if vibration-sensitive structures (especially inhabited buildings) are within 50 feet (about 15 meters) of the shake point, you must get the owner's permission, and you are strongly encouraged to photograph these structures before and after testing[^nheriutexas2020safety-e6].
- Monitoring existing bridges, roads, or water infrastructure likewise requires permission from the managing agency in advance, along with an agreement on who owns the data and whether you can publish them `[Our analysis]`.

### Numerical simulation: first tell verification, validation, and calibration apart

Finite element analysis, hydrologic models, traffic simulation, and other numerical models are widely used in this field `[Our analysis]`. For the full method of simulation research, see [Quantitative simulation](../../06_methods/simulation_study.md). The three definitions below come from a 2003 report by Oberkampf and colleagues at Sandia National Laboratories in the US (on computational engineering and physics) and from Sargent's 2010 paper on simulation methodology. They are not civil engineering rules, but you need to keep them apart whenever you do numerical simulation:

- **Verification**: does the program implement your model correctly, and does it compute the right answer[^oberkampf2003verification-e1]?
- **Validation**: how well the model represents the real world, from the standpoint of its intended use[^oberkampf2003verification-e1]. Validation is specific to a purpose: a model that is valid under one set of conditions may be invalid under another[^sargent2010verification-e2].
- **Calibration**: adjusting model parameters so the model agrees better with test results[^oberkampf2003verification-e5].

Where people get confused: Oberkampf and colleagues point out that structural dynamics researchers often call "using results from modal testing (tests that measure a structure's vibration properties) to tune unknown parameters in the model" "model validation"; they argue the more precise term is "model updating" or "model calibration"[^oberkampf2003verification-e2]. If you tune parameters on one set of test data and then declare the model "validated" on the same data, you have shown nothing about whether it can predict new situations `[Our analysis]`.

Oberkampf and colleagues consider true validation experiments infeasible for most complex or large systems. They recommend a building-block approach: divide the system into progressively simpler tiers (subsystem cases, benchmark cases, unit problems) and compare with experiments at each tier[^oberkampf2003verification-e3]. But when the physics is complex (fracture, for example), inferring confidence at one tier from another is usually weak[^oberkampf2003verification-e6]. Validation experiments must be designed on purpose, with goals tied to the model's intended application[^oberkampf2003verification-e4]. Sargent adds that after any change to a model, you must verify and validate it again[^sargent2010verification-e20]. Compared with computer science: there, simulation studies are mostly used to compare policies or system designs; in civil engineering, model results often support design decisions that ultimately affect public safety, so comparison with physical tests carries more weight `[Our analysis]`.

### Working with industry and government

Much research in this field involves companies, design institutes, or government agencies, and the usual problems are confidentiality and data ownership. Before the collaboration starts, settle who owns the data, whether the partner must review papers before publication, and what cannot be made public `[Our analysis]`. Relevant rules you can refer to:

- The ASCE Code of Ethics (2020 revision, binding on ASCE members) requires members to keep confidential any proprietary information that clients and employers designate as such[^asce2020code-e15], and to disclose any real, potential, or perceived conflicts of interest[^asce2020code-e14].
- The Lehigh facility's 2016 user guide notes that from 2004 to 2014, funded projects of the US Network for Earthquake Engineering Simulation (NEES, the predecessor of NHERI) had to sign a "research participation agreement", covering intellectual property, publication rights, and more, before starting laboratory work; by April 2016, when the guide was written, NHERI no longer required such documents[^nherilehigh2016users-e10].
- In a 2020 editorial in ASCE's *Journal of Water Resources Planning and Management*, Rosenberg and colleagues list "proprietary, sensitive, or protected intellectual property that cannot be shared" as one barrier to reproducible research[^rosenberg2020next-e2]. The data policy page of ASCE's journals (the version we read is a 2022 archived copy) encourages authors to negotiate, when they sign data agreements, for the data used in a paper to be made available to readers, for example in anonymized form[^ascedataavailability-e9].

### Publishing: ASCE as an example

According to a 2020 editorial, ASCE publishes more than 30 journals[^rosenberg2020next-e1]. The points below are ASCE's own rules, taken from a 2011 editorial in ASCE's *Journal of Bridge Engineering* (Hendrickson and colleagues). We read this editorial through a 2022 snapshot on the Internet Archive, so ASCE's current policy may have changed; when you submit, follow the target journal's author guidelines. For other publishers such as Elsevier or Springer, or for Chinese journals, follow their rules `[Our analysis]`.

- **No duplicate publication.** The editorial says this is long-standing ASCE policy: content published in an ASCE journal must not have been published elsewhere, nor be published elsewhere later[^hendrickson2011conference-e1].
- **Turning a conference paper into a journal paper takes 50% new content.** You may build a journal paper on a conference presentation, but it must be "significantly different" from the paper in the published proceedings, which generally means 50% new content[^hendrickson2011conference-e2]. The editorial adds that this applies to every conference that publishes proceedings, and papers posted online count as published[^hendrickson2011conference-e4].
- **An example from transportation.** Starting with its January 2011 annual meeting, the US Transportation Research Board (TRB) put its compendium of annual meeting papers online, so ASCE treats TRB annual meeting papers as published; authors can choose to leave their paper out of the compendium to keep the option of submitting to an ASCE journal[^hendrickson2011conference-e3].
- **Compared with IEEE.** This is close in spirit to the rule of IEEE (the Institute of Electrical and Electronics Engineers) in electrical engineering that the journal version must add substantial new content, but ASCE gives the concrete figure of "50% new content" (see the [Electrical engineering page](../electrical-engineering/README.md)) `[Our analysis]`.
- **Preprints.** A preprint is a manuscript posted publicly online before it is submitted to a journal. ASCE's journal author guidelines page (the version we read is an Internet Archive snapshot from May 2025) says that a paper on a preprint server does not count as published as long as copyright can still be transferred to ASCE; once the paper is accepted, you must add the full citation and DOI (Digital Object Identifier, the paper's permanent ID) of the published paper to the preprint, along with ASCE's copyright notice (authors who choose open access keep copyright and add a different statement instead)[^asce2025publishing-e1]. But the "previously published content" section of the same page says that "published" may include preprints posted on institutional repositories, preprint servers, and similar sites[^asce2025publishing-e2]. The two statements do not fully agree, so check with the target journal's editorial office before you submit `[Our analysis]`.

---

## How this field differs from others

The table below is our own summary, meant to help you locate the differences quickly; it is not a strict classification of fields `[Our analysis]`.

| | Civil engineering | Computer science |
|---|---|---|
| Where results come from | Laboratory tests (including large-scale specimens), field tests and monitoring, numerical simulation, often in combination | Mostly experiments on code, systems, and data |
| What controls the timeline | Large-facility schedules, site permits, seasons, and weather; for example, a typical project at the University of Texas NHERI field testing facility takes months or even years to prepare[^nheriutexas2020safety-e2] | Mainly conference deadlines (see the [Computer science page](../computer-science/README.md#deadlines-set-the-pace-at-a-cost)) |
| Publication path | Taking ASCE as the example (2011 editorial), a conference paper turned into a journal paper generally needs 50% new content[^hendrickson2011conference-e2] | Top conferences dominate in most subfields (see the [Computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue)) |
| Where the research ends up | Some results go into design codes and standards (see below) | Not covered on the Computer science page |
| Ethical focus | Taking the ASCE Code of Ethics as the example, the health, safety, and welfare of the public come first[^asce2020code-e12]; test safety | See the [Computer science page](../computer-science/README.md#ethics-issues-specific-to-this-field) |
| How much can be shared | Proprietary, sensitive, or intellectual-property material may not be shareable[^rosenberg2020next-e2] | Experimental subfields have a tradition of releasing artifacts (code, data) |

---

## Norms and reporting standards in this field

### ASCE Code of Ethics: public safety first

The ASCE Code of Ethics was first adopted in 1914 and last revised in October 2020; it is the standard of professional conduct for ASCE members[^asce2020code-e10] (we read the web version as of October 2026). It requires members first and foremost to protect and advance the health, safety, and welfare of the public[^asce2020code-e11]; when ethical obligations conflict, this one overrides all others[^asce2020code-e12]. ASCE states that the code itself does not establish a "standard of care" (the legal yardstick for whether a professional has done their job properly)[^asce2020code-e9]. Other countries' professional societies and engineering licensure systems have their own codes; follow your local one `[Our analysis]`. For general research integrity requirements, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md) in Throughout the project. The provisions most relevant to research `[Our analysis]`:

- Express professional opinions only when you have adequate knowledge and honest conviction, and express them truthfully[^asce2020code-e3]. This applies both to the conclusions of a paper and to engineering recommendations `[Our analysis]`.
- When your work uses existing or emerging technologies, consider their capabilities, limitations, and implications[^asce2020code-e13]; inform clients and employers promptly of the risks and limitations of the work[^asce2020code-e14].
- Take credit only for work you did yourself, and acknowledge the contributions of others[^asce2020code-e16].

### Research and design codes and standards

For some civil engineering research, the end users are the committees that write codes and the engineers who design `[Our analysis]`. The examples below are from the US and ASCE (based on ASCE web pages read in October 2026); other countries have different code systems:

- ASCE 7 is the general structural design load standard adopted across the US[^asce2026asce7-e1]. Many ASCE standards are referenced by model building codes and adopted by states and localities[^asce2026standards-e1].
- ASCE standards are developed or updated by balanced committees of volunteers, followed by a public comment period[^asce2026standards-e2] of at least 45 days[^asce2026standards-e5]; every standard is updated or reaffirmed at least every 5 years[^asce2026standards-e3]. For ASCE 7, voting members come from producers, users, regulators, and other interests[^asce2026asce7-e3]. Anyone can propose a change to a standard, and committee meetings are open to anyone[^asce2026standards-e4].
- New data drive revisions. For example, the ASCE 7-22 edition revised ground snow loads to reflect updated snow load data[^asce2026asce7-e2].
- Research does not find its way into codes automatically. An example from earthquake engineering: in its fiscal year 2008 budget request, the US National Institute of Standards and Technology (NIST) wrote, in its description of the National Earthquake Hazards Reduction Program, that there was a critical gap between basic research results and their practical engineering application, and that building codes and standards did not reflect the current state of knowledge[^nist2008nehrp-e1]; one of the programs it proposed was to identify the gaps in carrying research results into design guidelines and national model building code provisions[^nist2008nehrp-e2]. This reflects US earthquake engineering around 2007–2008; it may not hold today or in other subfields `[Our analysis]`. Rosenberg and colleagues' 2020 editorial also argues that open data and code make it easier for practicing engineers to use research results, helping to close the gap between research and practice[^rosenberg2020next-e6].
- **What this means for a newcomer**: in your paper, say which provision of the current code your results bear on and whether they support changing it `[Our analysis]`; when you cite a code, give its edition, because codes are revised; ASCE standards, for example, are updated or reaffirmed at least every 5 years[^asce2026standards-e3].

### Data availability statements (ASCE)

In 2018, ASCE's *Journal of Water Resources Planning and Management* began requiring authors to state whether their data, models, and code are available[^rosenberg2018new-e1]; according to the 2020 editorial, nearly all ASCE journals later adopted the policy[^rosenberg2020next-e1][^ascedataavailability-e1]. The ASCE website does not allow automated access, so the points below come from ASCE's journal policy page as we read it in a June 2022 snapshot on the Internet Archive. The current version may have changed; when you submit, follow the target journal's page:

- When you submit, add a "Data Availability Statement" section before the acknowledgments, choosing verbatim from a set of given statements[^ascedataavailability-e2], such as "available from the corresponding author upon reasonable request" or "proprietary or confidential in nature and may only be provided with restrictions"[^ascedataavailability-e3];
- list publicly available data and code in the references; the statement can be changed during review but not after acceptance[^ascedataavailability-e4];
- if the editor and reviewers ask, you must provide data and materials during review[^ascedataavailability-e5];
- ASCE's supplemental materials are not suited to large datasets or code and do not get their own DOI (Digital Object Identifier, a persistent link)[^ascedataavailability-e6]; it is better to use a data repository that assigns DOIs[^ascedataavailability-e10], and the general repositories listed on ASCE's page include Dryad, Figshare, DesignSafe, Zenodo, and HydroShare[^ascedataavailability-e11];
- the data used to make figures and tables should be included in what you share[^ascedataavailability-e7];
- ASCE does not peer-review data or code, and reviewers may or may not look at them[^ascedataavailability-e8], so checking that your materials actually work is up to you `[Our analysis]`.

### Reproducibility: a survey in hydrology and water resources

In 2019 Stagge and colleagues published a survey: from 1,989 papers published in 2017 in six hydrology and water resources journals, they sampled 360 to assess[^stagge2019assessing-e1]. Of those 360, 70.3% claimed that materials were available, but only 48.6% of those materials could actually be obtained online; only 1.1% of the papers both made their materials available and had their results fully reproduced[^stagge2019assessing-e2]. They estimate that only 0.6% to 6.8% of all 1,989 papers have reproducible results[^stagge2019assessing-e3]. Mind the scope: the survey looked only at six hydrology and water resources journals and one year of papers (2017), so it cannot be carried over directly to structural, geotechnical, transportation, or other subfields, or to civil engineering as a whole; our sources do not cover the situation in other subfields `[Our analysis]`. Several problems the survey found are ones a newcomer can avoid `[Our analysis]`:

- Among the papers whose results could not be reproduced, a common problem was file paths hard-coded so they only work on the author's computer[^stagge2019assessing-e4];
- in each of the six journals surveyed, papers that provided code, data, or software outnumbered papers that provided instructions for using them by 2 to 3 times[^stagge2019assessing-e5]; in other words, many people shared materials without saying how to use them `[Our analysis]`;
- journal policies help, but you cannot rely on policy alone: across the six journals, stronger data policies tended to go with higher availability and reproducibility, but the journals differed widely[^stagge2019assessing-e6]; the two journals that required data availability statements (*Hydrology and Earth System Sciences*, HESS, and *Water Resources Research*, WRR; neither is an ASCE journal) actually had a lower share of papers with public materials, and more papers that sent readers to the authors or a third party for materials[^stagge2019assessing-e7].

Rosenberg and colleagues' 2020 editorial includes a checklist, for example stating which code produces which figure or table and removing local paths that only work on your own computer[^rosenberg2020next-e3]; the rest is general practice for organizing materials, covered in [Organizing your research materials](../../08_throughout/organizing_materials.md). Test data are no different: the Lehigh facility's 2016 user guide requires researchers to upload metadata describing the test setup, unprocessed raw data, and converted data[^nherilehigh2016users-e6], so that qualified researchers can repeat the test and regenerate the derived data[^nherilehigh2016users-e7].

### Safety in large-scale and field tests

Large-scale tests involve high-capacity actuators (hydraulic loading devices), heavy specimens, and crane lifts; field tests involve heavy vehicles and equipment `[Our analysis]`. The ASCE Code of Ethics also requires members to promote health and safety in the workplace[^asce2020code-e16]. The practices in the two NHERI facilities' documents (the Lehigh facility's 2016 user guide and the University of Texas facility's 2020 safety plan) are a useful reference; in your own laboratory, follow your institution's safety rules `[Our analysis]`:

- **Get trained before you touch anything** (Lehigh): you must complete formal on-site training before using any equipment[^nherilehigh2016users-e11].
- **Analyze hazards in advance** (Texas): the safety plan's job hazard analysis is a technique that looks at specific job tasks to identify hazards before they occur[^nheriutexas2020safety-e3].
- **Hold a safety briefing every day** (Texas): during field operations, the chief scientist or chief engineer holds a daily "tailgate meeting" safety briefing with all field personnel[^nheriutexas2020safety-e7].
- **No one in the test area during a test** (Lehigh)[^nherilehigh2016users-e12].
- **When something goes wrong, stop work first** (Texas): after a mistake, accident, or equipment failure, stop work immediately, decide on corrective action, and then adjust the schedule; a safe and deliberate workflow always takes precedence over schedule[^nheriutexas2020safety-e8]. Never make assumptions about safety; other people may not realize something is wrong[^nheriutexas2020safety-e9].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists only the two strategies this page's sources support; our sources do not cover how Comparative evaluation, Causal explanation, Synthesis, and the other strategies are used in civil engineering. The grouping and the "What it looks like in civil engineering" column are our own summary, and each standard represents only the body or document cited in its footnote `[Our analysis]`.

| Strategy | What it looks like in civil engineering | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Propose a new structural system, component, use of a material, or analysis method, often paired with a finite element, hydrologic, traffic, or other numerical model | The Lehigh facility requires you to submit a test matrix and the damage expected in each test before a large-scale test, and to get written approval before running it[^nherilehigh2016users-e2]; numerical models must keep verification, validation, and calibration apart[^oberkampf2003verification-e1][^oberkampf2003verification-e5], and tuning parameters with modal test data is calibration, not validation[^oberkampf2003verification-e2]; a model valid under one set of conditions may be invalid under another[^sargent2010verification-e2] | [Engineering research](../computer-science/practices/engineering_research.md) (Computer science page), [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Measure how structures and soils actually behave in the laboratory or on real sites, including field tests and long-term monitoring | The Lehigh facility requires uploading metadata describing the test setup, unprocessed raw data, and converted data[^nherilehigh2016users-e6], so that qualified researchers can repeat the test and regenerate the derived data[^nherilehigh2016users-e7]; ASCE journals require a data availability statement[^ascedataavailability-e2] | [Experimental measurement](../../06_methods/experimental_measurement.md) |

How to use this table `[Our analysis]`: choose the main strategy from your central claim. For example, if you propose a new connection and then load-test it to see how it fails, your claim is "the new connection is better", so hold it to the standards of Building and improving, and write up the test data to the requirements of Description.

## Research methods common in this field

Civil engineering has no method pages of its own; it uses the cross-field methods in [Research types](../../06_methods/README.md) and the practices from the Computer science pages:

- [Experimental measurement](../../06_methods/experimental_measurement.md): laboratory load tests, field tests, and monitoring. Schedule and get approval first; see [Large-scale tests](#large-scale-tests-long-queues-approvals-and-preparation) above.
- [Quantitative simulation](../../06_methods/simulation_study.md): first tell verification, validation, and calibration apart; see [Numerical simulation](#numerical-simulation-first-tell-verification-validation-and-calibration-apart) above.
- [Engineering research](../computer-science/practices/engineering_research.md) and [Optimization studies](../computer-science/practices/optimization_study.md) (Computer science pages): evaluating a new structure usually needs physical tests, not numerical simulation alone; for structural optimization, water resources operation, and transportation network design, the optimization studies page is a useful reference `[Our analysis]`.
- [Case studies](../../06_methods/case_study.md): common in construction management, engineering failure analysis, and similar areas `[Our analysis]`. [Replication studies](../../06_methods/replication.md): see [Reproducibility](#reproducibility-a-survey-in-hydrology-and-water-resources) above.

---

## Advice for newcomers

1. **Schedule large-scale tests when you write the proposal.** At the Lehigh facility, for example, you contact the facility early, while writing the proposal[^nherilehigh2016users-e9]; the test matrix and the damage expected in each test need the facility's written approval in advance[^nherilehigh2016users-e2]. Plan your instrumentation at this stage too, and run a model prediction first `[Our analysis]`.
2. **Do not mistake calibration for validation.** Tuning parameters with modal test data is calibration, not validation[^oberkampf2003verification-e2][^oberkampf2003verification-e5]; hold back an independent set of test results for checking. For the reasoning, see [Comparative evaluation: keep one set of data for the final test only](../../05_research-strategies/compare_evaluate.md#keep-some-data-for-the-final-test-only) `[Our analysis]`.
3. **Settle data and publication rights before a collaboration starts.** ASCE's journal data policy page encourages authors to agree, when signing data agreements, on how the data will be made available to readers[^ascedataavailability-e9].
4. **Organize your data and code from day one**, and do not let paths get hard-coded to your own computer[^stagge2019assessing-e4].
5. **Give the edition when you cite a code.** Codes are revised; ASCE standards, for example, are updated or reaffirmed at least every 5 years[^asce2026standards-e3].
6. **Check the rules on conference papers and preprints before you submit.** Taking ASCE as the example, according to a 2011 editorial, a paper from a conference that published proceedings generally needs 50% new content to be submitted to a journal[^hendrickson2011conference-e2]; follow the target journal's current author guidelines.
7. **Safety comes before schedule.** Do not touch equipment until you are trained, and when something goes wrong, stop work first; both NHERI facilities' documents require this[^nherilehigh2016users-e11][^nheriutexas2020safety-e8].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Tuning parameters on a set of test data and then saying the model is "validated" | That is calibration, not validation[^oberkampf2003verification-e2][^oberkampf2003verification-e5] |
| Validating a model under one loading condition and then using it to predict completely different conditions | A model valid under one set of conditions may be invalid under another[^sargent2010verification-e2] |
| Not rechecking a model after changing it | Any change to a model requires verifying and validating it again[^sargent2010verification-e20] |
| Changing the loading protocol on the fly after testing has started | At the Lehigh facility, you may not deviate from the test matrix without approval[^nherilehigh2016users-e3] |
| Shaking next to an inhabited building in a field test without the owner's permission | At the University of Texas facility, you must get the owner's permission when sensitive structures are within 50 feet[^nheriutexas2020safety-e6] |
| Claiming "materials available" without putting them where readers can get them | In the hydrology and water resources papers surveyed by Stagge and colleagues, only 48.6% of the materials claimed to be available could be obtained online[^stagge2019assessing-e2]; ASCE's journal policy also states that you may not claim data are proprietary just because you do not want to share them[^ascedataavailability-e9] |
| Releasing code with hard-coded paths and no instructions | Others cannot reproduce the results[^stagge2019assessing-e4][^stagge2019assessing-e5] |
| Giving firm engineering conclusions on problems you do not know well | The ASCE Code of Ethics requires you to express professional opinions only when you have adequate knowledge[^asce2020code-e3] |

---

## Further reading

- **ASCE Code of Ethics**: the full text of the ASCE code of ethics, and it is short. Read it once when you enter the field.
- **The Data Availability Statement page in the ASCE Library**: the allowed statements for data availability and advice on data repositories. Read the current version before submitting to an ASCE journal.
- **Stagge et al. 2019, Assessing data availability and research reproducibility in hydrology and water resources** (*Scientific Data*, open access): surveys data availability and reproducibility in 2017 papers from six hydrology and water resources journals.
- **Rosenberg et al. 2020, The Next Frontier: Making Research More Reproducible** (editorial in ASCE's *Journal of Water Resources Planning and Management*): includes a checklist for making research easier to reproduce.
- **Oberkampf, Trucano & Hirsch 2003, Verification, Validation, and Predictive Capability in Computational Engineering and Physics** (public report from Sandia National Laboratories): a systematic treatment of verification, validation, and calibration of computational models. Read the introduction and Section 2 before doing numerical simulation.
- **The user guide and safety rules of the test facility you will use**: this page cites documents from two NHERI facilities (Lehigh's 2016 user guide and the University of Texas's 2020 safety plan); every laboratory's rules differ, so follow your own institution's.

[^nherilehigh2016users-e1]: NHERI Lehigh 2016 User Guide, Preface. [Evidence](../../../sources/notes/nherilehigh2016users.md#e1)
[^nherilehigh2016users-e2]: NHERI Lehigh 2016 User Guide, §1.6 Configuring an Experiment. [Evidence](../../../sources/notes/nherilehigh2016users.md#e2)
[^nherilehigh2016users-e3]: NHERI Lehigh 2016 User Guide, §1.6 Configuring an Experiment. [Evidence](../../../sources/notes/nherilehigh2016users.md#e3)
[^nherilehigh2016users-e4]: NHERI Lehigh 2016 User Guide, §1.6 Configuring an Experiment. [Evidence](../../../sources/notes/nherilehigh2016users.md#e4)
[^nherilehigh2016users-e5]: NHERI Lehigh 2016 User Guide, §2.7 Software Policies. [Evidence](../../../sources/notes/nherilehigh2016users.md#e5)
[^nherilehigh2016users-e6]: NHERI Lehigh 2016 User Guide, §1.9.1 Data Description. [Evidence](../../../sources/notes/nherilehigh2016users.md#e6)
[^nherilehigh2016users-e7]: NHERI Lehigh 2016 User Guide, §1.9.1 Data Description. [Evidence](../../../sources/notes/nherilehigh2016users.md#e7)
[^nherilehigh2016users-e8]: NHERI Lehigh 2016 User Guide, §1.11 Payload Project Protocol. [Evidence](../../../sources/notes/nherilehigh2016users.md#e8)
[^nherilehigh2016users-e9]: NHERI Lehigh 2016 User Guide, §5.1 Guidelines for Proposal Preparation. [Evidence](../../../sources/notes/nherilehigh2016users.md#e9)
[^nherilehigh2016users-e10]: NHERI Lehigh 2016 User Guide, §5.3 Required Documentation. [Evidence](../../../sources/notes/nherilehigh2016users.md#e10)
[^nherilehigh2016users-e11]: NHERI Lehigh 2016 User Guide, §5.4 Training. [Evidence](../../../sources/notes/nherilehigh2016users.md#e11)
[^nherilehigh2016users-e12]: NHERI Lehigh 2016 User Guide, §5.5 Experiment Execution. [Evidence](../../../sources/notes/nherilehigh2016users.md#e12)
[^nheriutexas2020safety-e1]: NHERI@UTexas 2020 Safety Plan (version 2.3), §1.1. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e1)
[^nheriutexas2020safety-e2]: NHERI@UTexas 2020 Safety Plan (version 2.3), §1.1. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e2)
[^nheriutexas2020safety-e3]: NHERI@UTexas 2020 Safety Plan (version 2.3), §1.7 Job Hazard Analysis. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e3)
[^nheriutexas2020safety-e4]: NHERI@UTexas 2020 Safety Plan (version 2.3), §2.2.1. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e4)
[^nheriutexas2020safety-e5]: NHERI@UTexas 2020 Safety Plan (version 2.3), §2.2.1. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e5)
[^nheriutexas2020safety-e6]: NHERI@UTexas 2020 Safety Plan (version 2.3), §2.2.2. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e6)
[^nheriutexas2020safety-e7]: NHERI@UTexas 2020 Safety Plan (version 2.3), §1.12. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e7)
[^nheriutexas2020safety-e8]: NHERI@UTexas 2020 Safety Plan (version 2.3), §1.12. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e8)
[^nheriutexas2020safety-e9]: NHERI@UTexas 2020 Safety Plan (version 2.3), §1.12. [Evidence](../../../sources/notes/nheriutexas2020safety.md#e9)
[^oberkampf2003verification-e1]: Oberkampf et al. 2003, §1.2. [Evidence](../../../sources/notes/oberkampf2003verification.md#e1)
[^oberkampf2003verification-e2]: Oberkampf et al. 2003, §1.1. [Evidence](../../../sources/notes/oberkampf2003verification.md#e2)
[^oberkampf2003verification-e3]: Oberkampf et al. 2003, §1.2. [Evidence](../../../sources/notes/oberkampf2003verification.md#e3)
[^oberkampf2003verification-e4]: Oberkampf et al. 2003, §2.4.1. [Evidence](../../../sources/notes/oberkampf2003verification.md#e4)
[^oberkampf2003verification-e5]: Oberkampf et al. 2003, §3.3. [Evidence](../../../sources/notes/oberkampf2003verification.md#e5)
[^oberkampf2003verification-e6]: Oberkampf et al. 2003, §1.2. [Evidence](../../../sources/notes/oberkampf2003verification.md#e6)
[^sargent2010verification-e2]: Sargent 2010, §1 Introduction. [Evidence](../../../sources/notes/sargent2010verification.md#e2)
[^sargent2010verification-e20]: Sargent 2010, §3 Paradigms. [Evidence](../../../sources/notes/sargent2010verification.md#e20)
[^asce2020code-e10]: ASCE Code of Ethics (2020 revision), note at the top of the page. [Evidence](../../../sources/notes/asce2020code.md#e10)
[^asce2020code-e11]: ASCE Code of Ethics, Preamble. [Evidence](../../../sources/notes/asce2020code.md#e11)
[^asce2020code-e12]: ASCE Code of Ethics, Preamble; 1a. [Evidence](../../../sources/notes/asce2020code.md#e12)
[^asce2020code-e3]: ASCE Code of Ethics, 1c. [Evidence](../../../sources/notes/asce2020code.md#e3)
[^asce2020code-e13]: ASCE Code of Ethics, 1h. [Evidence](../../../sources/notes/asce2020code.md#e13)
[^asce2020code-e14]: ASCE Code of Ethics, 4b, 4c. [Evidence](../../../sources/notes/asce2020code.md#e14)
[^asce2020code-e15]: ASCE Code of Ethics, 4e, 4f. [Evidence](../../../sources/notes/asce2020code.md#e15)
[^asce2020code-e16]: ASCE Code of Ethics, 5a, 5b, 5c. [Evidence](../../../sources/notes/asce2020code.md#e16)
[^asce2020code-e9]: ASCE Code of Ethics, footnote 1. [Evidence](../../../sources/notes/asce2020code.md#e9)
[^rosenberg2020next-e1]: Rosenberg et al. 2020, main text, after Figure 1. [Evidence](../../../sources/notes/rosenberg2020next.md#e1)
[^rosenberg2020next-e2]: Rosenberg et al. 2020, main text, para. 2. [Evidence](../../../sources/notes/rosenberg2020next.md#e2)
[^rosenberg2020next-e3]: Rosenberg et al. 2020, Checklist. [Evidence](../../../sources/notes/rosenberg2020next.md#e3)
[^rosenberg2018new-e1]: Rosenberg & Watkins 2018, main text, para. 1. [Evidence](../../../sources/notes/rosenberg2018new.md#e1)
[^ascedataavailability-e2]: ASCE Library, Data Availability Statement (2022 snapshot). [Evidence](../../../sources/notes/ascedataavailability.md#e2)
[^ascedataavailability-e3]: ASCE Library, Data Availability Statement (2022 snapshot), list of suggested wordings. [Evidence](../../../sources/notes/ascedataavailability.md#e3)
[^ascedataavailability-e4]: ASCE Library, Data Availability Statement (2022 snapshot). [Evidence](../../../sources/notes/ascedataavailability.md#e4)
[^ascedataavailability-e5]: ASCE Library, Data Availability Statement (2022 snapshot). [Evidence](../../../sources/notes/ascedataavailability.md#e5)
[^ascedataavailability-e6]: ASCE Library, Data Availability Statement (2022 snapshot), Where should my data go? [Evidence](../../../sources/notes/ascedataavailability.md#e6)
[^ascedataavailability-e9]: ASCE Library, Data Availability Statement (2022 snapshot), What if my data is proprietary? [Evidence](../../../sources/notes/ascedataavailability.md#e9)
[^ascedataavailability-e10]: ASCE Library, Data Availability Statement (2022 snapshot), Where should my data go? [Evidence](../../../sources/notes/ascedataavailability.md#e10)
[^hendrickson2011conference-e1]: Hendrickson et al. 2011, paragraph 1. [Evidence](../../../sources/notes/hendrickson2011conference.md#e1)
[^hendrickson2011conference-e2]: Hendrickson et al. 2011, paragraph 2. [Evidence](../../../sources/notes/hendrickson2011conference.md#e2)
[^hendrickson2011conference-e3]: Hendrickson et al. 2011, paragraph 3. [Evidence](../../../sources/notes/hendrickson2011conference.md#e3)
[^hendrickson2011conference-e4]: Hendrickson et al. 2011, paragraph 4. [Evidence](../../../sources/notes/hendrickson2011conference.md#e4)
[^asce2025publishing-e1]: ASCE Library, Publishing in ASCE Journals (2025 snapshot), Preprint Servers. [Evidence](../../../sources/notes/asce2025publishing.md#e1)
[^asce2025publishing-e2]: ASCE Library, Publishing in ASCE Journals (2025 snapshot), Previously Published Content. [Evidence](../../../sources/notes/asce2025publishing.md#e2)
[^asce2026standards-e1]: ASCE, Codes and Standards page. [Evidence](../../../sources/notes/asce2026standards.md#e1)
[^asce2026standards-e2]: ASCE, Codes and Standards page, Get involved with Standards. [Evidence](../../../sources/notes/asce2026standards.md#e2)
[^asce2026standards-e3]: ASCE, Codes and Standards page, Get involved with Standards. [Evidence](../../../sources/notes/asce2026standards.md#e3)
[^asce2026standards-e4]: ASCE, Codes and Standards page. [Evidence](../../../sources/notes/asce2026standards.md#e4)
[^asce2026standards-e5]: ASCE, Codes and Standards page, Comment on a draft standard. [Evidence](../../../sources/notes/asce2026standards.md#e5)
[^asce2026asce7-e1]: ASCE, ASCE 7-22 page. [Evidence](../../../sources/notes/asce2026asce7.md#e1)
[^asce2026asce7-e2]: ASCE, ASCE 7-22 page, list of new content. [Evidence](../../../sources/notes/asce2026asce7.md#e2)
[^nist2008nehrp-e1]: NIST, fiscal year 2008 budget justification, National Earthquake Hazards Reduction Program, Challenge. [Evidence](../../../sources/notes/nist2008nehrp.md#e1)
[^nist2008nehrp-e2]: NIST, fiscal year 2008 budget justification, National Earthquake Hazards Reduction Program, Proposed Program; Expected Impacts. [Evidence](../../../sources/notes/nist2008nehrp.md#e2)
[^stagge2019assessing-e1]: Stagge et al. 2019, Abstract. [Evidence](../../../sources/notes/stagge2019assessing.md#e1)
[^stagge2019assessing-e2]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e2)
[^stagge2019assessing-e3]: Stagge et al. 2019, Abstract. [Evidence](../../../sources/notes/stagge2019assessing.md#e3)
[^stagge2019assessing-e4]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e4)
[^stagge2019assessing-e5]: Stagge et al. 2019, Discussion. [Evidence](../../../sources/notes/stagge2019assessing.md#e5)
[^stagge2019assessing-e7]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e7)
[^ascedataavailability-e7]: ASCE Library, Data Availability Statement (2022 snapshot), What should we share? [Evidence](../../../sources/notes/ascedataavailability.md#e7)
[^ascedataavailability-e8]: ASCE Library, Data Availability Statement (2022 snapshot), Will my data or code be peer reviewed? [Evidence](../../../sources/notes/ascedataavailability.md#e8)
[^ascedataavailability-e11]: ASCE Library, Data Availability Statement (2022 snapshot), Where should my data go? [Evidence](../../../sources/notes/ascedataavailability.md#e11)
[^stagge2019assessing-e6]: Stagge et al. 2019, Results. [Evidence](../../../sources/notes/stagge2019assessing.md#e6)
[^asce2026asce7-e3]: ASCE, ASCE 7-22 page, Who develops standards? [Evidence](../../../sources/notes/asce2026asce7.md#e3)
[^rosenberg2020next-e6]: Rosenberg et al. 2020, main text, after the list of benefits. [Evidence](../../../sources/notes/rosenberg2020next.md#e6)
[^ascedataavailability-e1]: ASCE Library, Data Availability Statement (2022 snapshot), para. 1. [Evidence](../../../sources/notes/ascedataavailability.md#e1)
