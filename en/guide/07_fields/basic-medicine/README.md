# Basic medical sciences: field overview

This page explains how research in the basic medical sciences actually works. The basic medical sciences include anatomy, physiology, pathology, pharmacology, toxicology, immunology, medical microbiology, and similar disciplines. Much of their day-to-day practice is the same as in lab-based life sciences: how a lab divides the work, how to keep a lab notebook, how to tell biological replicates from technical replicates, the 3Rs of animal research (Replacement, Reduction, Refinement), and the ARRIVE guidelines (Animal Research: Reporting of In Vivo Experiments) for reporting animal research. These are covered in the [biological sciences field overview](../biological-sciences/README.md). Clinical trials involving patients, trial registration, the authorship criteria of the International Committee of Medical Journal Editors (ICMJE), and clinical reporting guidelines are in the [clinical medicine field overview](../clinical-medicine/README.md). Practices shared by all fields are in the main Parts listed in [The research journey at a glance](../../00_start-here/research-journey.md) and in [Throughout the project](../../08_throughout/README.md). This page covers only what is specific to the basic medical sciences: why so many preclinical findings fail in humans, and the rules you follow because of that. For which research strategies are common and what evidence each relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence); for how to actually do the work, see [Research methods common in this field](#research-methods-common-in-this-field).

**After reading this page, you should be able to:**

- explain what "bench to bedside" means, and why preclinical findings so often fail to translate;
- design and report experiments to the core standards for preclinical research: randomization, blinding, sample size, and data handling;
- tell exploratory experiments from confirmatory ones, and know which results can be analyzed statistically and which are only leads;
- know why antibodies must be validated for each application, and how to report reagents in a paper;
- know which ethical requirements apply when you use human tissue and biobank samples;
- know who sets Good Laboratory Practice and which studies it governs.

---

## How research works in this field

### Your research sits upstream on the path "from bench to bedside"

Medical research is often described as a chain: discoveries start with basic research at the bench, move through preclinical animal studies, and end with clinical trials that show efficacy in humans[^mak2014lost-e9]. Many projects in the basic medical sciences sit upstream on this chain `[Our analysis]`. So your results may be used by others as the basis for the next step `[Our analysis]`. For example, the US Food and Drug Administration and Health Canada both require animal testing before a new molecular entity is used in humans[^mak2014lost-e10]. Freedman et al. 2015 report that academic research with clinical promise is usually repeated inside a drug company before clinical studies begin, and each attempt takes 3 to 24 months and costs US$500,000 to US$2,000,000[^freedman2015economics-e6]. Flawed preclinical research gives false hope to patients waiting for treatment[^freedman2015economics-e8].

### Many preclinical findings do not hold up in humans

This is the most important background for a newcomer to this field `[Our analysis]`. The figures and examples below come from a short 2014 review by Mak et al. It is a narrative review, not a systematic review; its figures are cited from other studies, and it covers only cancer and new drugs, so you cannot apply it directly to every area `[Our analysis]`.

- **Translation success rates are low.** The review states that the average rate of successful translation from animal models to clinical cancer trials is less than 8%[^mak2014lost-e1]. It also cites that 85% of new drugs that succeeded in preclinical testing fail in early clinical trials, and of those that reach Phase III, only half are approved[^mak2014lost-e2].
- **Some failures are dramatic.** TGN1412 caused catastrophic systemic organ failure in its first-in-human trial, at a dose 500 times lower than the dose found safe in animal studies[^mak2014lost-e7]. IPI-926 extended survival fivefold in mice with advanced brain tumors, yet in human trials it was no different from placebo[^mak2014lost-e8].

The review attributes the failures partly to two things[^mak2014lost-e5]:

1. **The models themselves are not like humans.** Animal models struggle to reproduce the complex process by which human cancer arises and progresses[^mak2014lost-e3]. Stroke researchers analyzing a series of failed clinical trials also acknowledged that no animal model fully reproduces human stroke[^landis2012call-e3].
2. **Preclinical studies are poorly done and poorly reported.** This is the part you can control `[Our analysis]`. In animal studies of the stroke drug NXY-059, papers that reported randomization, allocation concealment, or blinded outcome assessment found clearly smaller effect sizes than papers that did not report them[^landis2012call-e4]. A series of poorly designed, poorly reported studies can together become the basis for a large, expensive clinical trial that ultimately fails, exposing patients to risk for nothing[^landis2012call-e5].

The improvements Mak et al. summarize include: using higher animals, not only rodents; randomization and blinding of outcome assessors; including animals of both sexes and different ages; and publishing both positive and negative data[^mak2014lost-e6]. They also write that because negative results often go unpublished, animal studies appear to overestimate the likelihood that a treatment works by about 30%[^mak2014lost-e4]. For how to report negative results, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#2-be-honest-with-the-evidence-dont-fool-yourself-report-all-results). So in the basic medical sciences, "do it rigorously and write it up clearly" is not about making the paper look good; it matters because people downstream, and patients, will rely on your results `[Our analysis]`.

### How work is organized, published, and credited

Lab roles, notebooks, and the management of reagents and animals are the same as in lab-based life sciences; see the [biological sciences field overview](../biological-sciences/README.md). Publication is mainly in journals; for preprints, see [Publishing: journals and preprints](../biological-sciences/README.md#publishing-journals-and-preprints) on that page `[Our analysis]`. For authorship criteria, see [Authorship: the four ICMJE criteria](../clinical-medicine/README.md#authorship-the-icmjes-four-criteria) in the clinical medicine field overview; whether your target journal follows them is stated in its instructions for authors `[Our analysis]`.

---

## How this field differs from others

The table below compares this field with the [computer science field overview](../computer-science/README.md). The basic medical sciences column follows the attached footnotes; the computer science column is our own summary, and the computer science field overview has the details `[Our analysis]`.

| | Basic medical sciences | Computer science |
|---|---|---|
| Who uses the results | They may become the basis for clinical trials[^landis2012call-e5]; academic research with clinical promise is usually repeated by a drug company before clinical studies[^freedman2015economics-e6] | Mostly peers and engineering practice, directly |
| Biggest risk | Models that are not like humans, plus poorly done preclinical research[^mak2014lost-e5] | Unfair baselines, benchmark leakage, and the like |
| Experimental materials | Reagents such as antibodies may themselves be unreliable and must be validated for each application[^uhlen2016proposal-e1][^uhlen2016proposal-e2] | Code and data can be copied exactly |
| Where samples come from | Animals and cells, but also human tissue and biobanks, which need ethics approval and informed consent[^wma2024helsinki-e11][^wma2024helsinki-e12] | Ethics review only when human data is involved |
| External rules | Safety studies done for regulatory submission must follow the Organisation for Economic Co-operation and Development's Good Laboratory Practice (see below)[^oecd1998glp-e2] | Usually no comparable mandatory quality system |

How it relates to neighboring fields: the basic medical sciences share their lab conventions with the [Biological sciences](../biological-sciences/README.md), and their ethics and publication rules with [Clinical medicine](../clinical-medicine/README.md). The question they especially have to answer is "does this result still hold in humans?" `[Our analysis]`

---

## Norms and reporting standards in this field

### Report at least four things in preclinical research: recommendations from a US workshop

In June 2012, the US National Institute of Neurological Disorders and Stroke convened a meeting of stakeholders to discuss how to improve the reporting of animal study methods in grant applications and papers[^landis2012call-e16]. Its main recommendation: studies should report **at a minimum** how the sample size was estimated, whether and how animals were randomized, whether the investigators were blinded, and how the data were handled[^landis2012call-e1]. These are recommendations from one meeting, not regulations; your institution, funder, and journals may have their own requirements `[Our analysis]`. Why stress them? The meeting paper cites a review of 100 papers published in *Cancer Research* in 2010: 28% reported randomization, 2% reported blinding of observers, and none explained how the number of animals per group was decided[^landis2012call-e2].

- **Randomize, and conceal allocation.** The investigator should not know which group the next animal taken from the cage will be assigned to[^landis2012call-e6]. When samples are processed in batches, plan the batches carefully, or you may mistake a batch effect for a treatment effect[^landis2012call-e7].
- **Calculate the sample size in advance.** An experiment with so few animals that it can hardly detect a meaningful difference is also unethical[^landis2012call-e8].
- **Decide in advance when to stop.** Don't "stop if it's significant, add more data if it isn't"; fix the sample size and the rule for stopping data collection in advance, and report them in the paper[^landis2012call-e9]. Otherwise the chance of a false positive goes up `[Our analysis]`.
- **Account for animals that drop out.** If a treatment kills the weakest animals and this is not reported, the treatment can look effective[^landis2012call-e10].
- **Prespecify the primary endpoint**, the time of assessment, and the analysis method; don't pick them after the fact[^landis2012call-e11].
- **Report how many times the experiment was done.** This counteracts the tendency to publish only the best run[^landis2012call-e15].

These points match the core items of the ARRIVE guidelines for reporting animal research; ARRIVE itself is described in the [biological sciences field overview](../biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines) `[Our analysis]`. The meeting paper also observed that few animal studies report randomization, blinding, or the basis for the sample size, yet most state that they complied with animal regulations, because journals require it[^landis2012call-e14].

### Tell exploratory experiments from confirmatory ones

Early exploratory experiments often have small samples, no primary outcome, and no blinding. That is fine, but they can only be interpreted as hypothesis-generating[^landis2012call-e12]. Findings from the exploratory stage need to be confirmed by follow-up experiments designed and reported to the core standards above[^landis2012call-e17].

### One pharmacology journal's specific rules: the *British Journal of Pharmacology*

In 2018 the *British Journal of Pharmacology* published guidance on design and analysis for authors and reviewers, updating its 2015 version; it is also the standard the journal uses in peer review[^curtis2018experimental-e1]. What follows is only this one journal's 2018 rules, not a field-wide requirement; for other journals, their instructions for authors apply `[Our analysis]`. The authors of the guidance say themselves that some of the rules are arbitrary and some will change[^curtis2018experimental-e12]; check the journal's latest version before you submit `[Our analysis]`.

- **Statistics only when each group has n of at least 5.** Groups with n below 5 may not be subjected to statistical tests, and their results must be labeled "exploratory" or "preliminary"[^curtis2018experimental-e2].
- **n is the number of independent samples.** Measuring three samples five times each and analyzing them as n = 15 is a common mistake; n should be 3[^curtis2018experimental-e3]. Five cells from the same mouse are technical replicates, so n = 1[^curtis2018experimental-e10]. For how to define the experimental unit, see the [biological sciences field overview](../biological-sciences/README.md#identify-the-experimental-unit-before-you-count-n).
- **Add 50% to the sample size from a power analysis.** A power analysis gives the minimum sample size; the journal encourages (but does not require) adding 50% to reduce the risk of missing a real difference[^curtis2018experimental-e9].
- **After normalization, change your statistical test.** When each value is divided by its paired control, the control group's mean is always 1 and has no standard error. Parametric tests such as analysis of variance (ANOVA) can then no longer be used; only nonparametric tests can. This situation is common in Western blot analysis[^curtis2018experimental-e4].
- **State the significance threshold in the Methods and don't change it in the Results**[^curtis2018experimental-e5].
- **Keep outliers by default**, unless you have prespecified, justifiable exclusion criteria[^curtis2018experimental-e6].
- **The Methods must include a "Data and statistical analysis" subsection**[^curtis2018experimental-e13].
- **Pilot data can be included, but without P values.** Pilot data that are not suitable for statistical analysis go in a "Pilot studies" subsection of the Methods[^curtis2018experimental-e11].

These rules are not well followed. The journal checked three issues published at least six months after the 2015 guidance came out and found that many papers did not fully comply[^curtis2018experimental-e7]. So the journal now rejects at initial screening any paper that combines all of these: no randomization or blinding, unequal n across groups, and statistics on groups with n below 5[^curtis2018experimental-e8].

### Validate antibodies for each application, and report reagents so they can be found

Antibodies are among the most common tools in the basic medical sciences `[Our analysis]`. But although antibodies are used very widely, there is no framework for validating them across applications, and the quality of data obtained with antibodies varies greatly[^uhlen2016proposal-e1]. Freedman et al. also list biological reagents and reference materials as one of the four main categories of causes of irreproducible preclinical research[^freedman2015economics-e7]; they estimate that this category, together with study design, accounts for most of the spending on irreproducible research, so these should be improved first[^freedman2015economics-e9].

In 2016, Uhlen et al., on behalf of an international working group on antibody validation, put forward recommendations[^uhlen2016proposal-e3]:

- **Validate for the application and the sample.** An antibody that performs well in a Western blot will not necessarily perform well in an enzyme-linked immunosorbent assay (ELISA)[^uhlen2016proposal-e2]. Users should do at least one validation in their own application and samples[^uhlen2016proposal-e6].
- **Five validation strategies; use at least one**: genetic strategies, orthogonal strategies, independent antibodies against the same target, expression of a tagged target protein, and immunocapture followed by mass spectrometry[^uhlen2016proposal-e3]. Put simply, a genetic strategy removes or reduces the target protein and checks whether the signal changes accordingly; an orthogonal strategy compares against a method that does not rely on antibodies `[Our analysis]`.
- **Human samples pose special difficulties.** Genetic strategies cannot be used on human tissue samples or on body fluids such as plasma and serum[^uhlen2016proposal-e4]; only the other strategies are possible `[Our analysis]`.
- **Binding the target is not the same as being specific.** Some supplementary methods can show that an antibody binds its target, but cannot rule out that it also binds structurally similar proteins (cross-reactivity)[^uhlen2016proposal-e9].
- **Show the whole gel.** When validating by Western blot, show the whole gel, not just the region around the target size[^uhlen2016proposal-e5].
- **Report reagents in the paper.** At a minimum give the catalog number and lot number, and ideally the Research Resource Identifier (RRID, a free reagent identifier used across journals)[^uhlen2016proposal-e6][^uhlen2016proposal-e7]. Manufacturers should repeat validation for every new lot[^uhlen2016proposal-e8], so watch whether your results change when the lot number changes `[Our analysis]`.

When reading these recommendations, be aware of the industry ties: editorial assistance for the article was provided by Phase Five Communications and paid for by the reagent company Thermo Fisher Scientific; the first author, Uhlen, is a cofounder of Atlas Antibodies and other antibody-related companies[^uhlen2016proposal-e10]. For other reagent issues, such as cell line authentication, see the [biological sciences field overview](../biological-sciences/README.md#validate-reagents-antibodies-and-cell-lines).

### Using human tissue and biobanks: check consent and ethics approval first

The basic medical sciences often use surgically removed tissue, blood, pathology slides, or samples from biobanks `[Our analysis]`. A **biobank** is a collection of biological material and the data associated with it[^wma2016taipei-e2]. Using these samples falls under ethical rules even if you never meet the patients themselves: the World Medical Association's *Declaration of Helsinki* (2024 revision) explicitly covers research using identifiable human material or data[^wma2024helsinki-e1].

Two World Medical Association documents, the *Declaration of Helsinki* and the *Declaration of Taipei* (2016 revision), which deals specifically with health databases and biobanks, set out the following principles:

- **Collection and storage both need informed consent.** Collecting, processing, and storing biological material and identifiable data, as well as foreseeable secondary uses, require free and informed consent[^wma2024helsinki-e11].
- **The biobank itself must be approved by an ethics committee.** Establishing a database or biobank requires approval from a research ethics committee, which also oversees its later use[^wma2024helsinki-e12].
- **If a new project uses old samples, check whether the original consent covers it.** The ethics committee must check whether the consent given at collection covers your planned use[^wma2016taipei-e6]. Where consent is impossible or impracticable to obtain, secondary research on stored samples must first be approved by a research ethics committee[^wma2024helsinki-e13].
- **Consent to "store for future research" is valid only if it is explained clearly.** When samples are stored in a biobank for multiple, indefinite uses, consent is valid only if the person has been adequately informed (paragraph 12 of the *Declaration of Taipei* lists what they must be told)[^wma2016taipei-e3]. One item: once a sample is de-identified, the person may not be able to know how it is used, and can no longer withdraw consent[^wma2016taipei-e4].
- **Donors can withdraw.** Individuals can change their consent at any time, or ask for their identifiable data and samples to be withdrawn[^wma2016taipei-e5].
- **When you request samples from, or provide them to, another institution, sign the proper agreements.** A biobank's governance rules must regulate access and sharing, using material transfer agreements where necessary[^wma2016taipei-e8].

The *Declaration of Taipei* is addressed mainly to physicians, but encourages everyone who uses health databases and biobanks to follow it[^wma2016taipei-e9]; it also requires that national ethical, legal, and regulatory requirements be taken into account[^wma2016taipei-e7]. For how to actually apply, follow your country's regulations and your institution's ethics committee `[Our analysis]`.

### Toxicology and safety studies: Good Laboratory Practice

**Who set it, and what does it cover?** This page relies on the *OECD Principles of Good Laboratory Practice* (GLP) of the Organisation for Economic Co-operation and Development (OECD). It is a quality system for studies done for regulatory purposes, governing how nonclinical health and environmental safety studies are planned, performed, monitored, recorded, archived, and reported[^oecd1998glp-e1]. It was adopted by the OECD Council in 1981 as an annex to the *Council Decision on the Mutual Acceptance of Data in the Assessment of Chemicals*[^oecd1998glp-e3], and revised in 1997[^oecd1998glp-e14]; it is based on the US Food and Drug Administration's 1976 regulations for nonclinical laboratory studies[^oecd1998glp-e4]. One aim is to let countries accept each other's test data and avoid duplicate testing[^oecd1998glp-e5].

**Which studies does it govern?** Nonclinical safety studies required by regulations for registering or licensing pharmaceuticals, pesticides, food and feed additives, cosmetics, veterinary drugs, and similar products (except where national legislation grants exemptions)[^oecd1998glp-e2]. Test facilities that submit results to national authorities for assessment must comply[^oecd1998glp-e12]. Exploratory studies in university labs that are not intended for regulators are generally outside its scope; but if your toxicology or pharmacology project is meant to support a drug submission, find out first whether it must be done in a GLP-compliant facility. The specific requirements depend on your country's regulations `[Our analysis]`.

Even if GLP does not apply to you, several of its practices are worth adopting `[Our analysis]`:

- **One person in overall charge.** Each study has a study director responsible for its overall conduct and the final report[^oecd1998glp-e6].
- **A written plan before you start**[^oecd1998glp-e8]; record deviations from the plan promptly, with the reason and the date[^oecd1998glp-e9].
- **Record data at the time, sign and date it**[^oecd1998glp-e10]; changes to raw data must not obscure the original entry and must give a reason[^oecd1998glp-e11].
- **Independent quality checks.** The person doing quality assurance is not involved in the study they inspect[^oecd1998glp-e7].
- **Archive everything.** The study plan, raw data, samples of test items, specimens, and the final report are all retained[^oecd1998glp-e13].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by its central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table lists only the three strategies our sources support. The grouping and the "What it looks like in the basic medical sciences" column are our own summary; each standard speaks only for the source in its footnote (mostly preclinical animal research in cancer and stroke), and our sources do not cover other areas `[Our analysis]`. Our sources do not cover the standards for other strategies, such as Building and improving (for example, establishing a new disease model).

| Strategy | What it looks like in the basic medical sciences | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Testing mechanisms and drug effects in cells or animal disease models; results may become the basis for clinical trials[^landis2012call-e5] | Report at least how the sample size was estimated, how randomization was done, whether there was blinding, and how data were handled[^landis2012call-e1]; studies that did not report randomization, allocation concealment, or blinding show clearly larger effect sizes[^landis2012call-e4]; exploratory experiments only generate hypotheses and need confirming in follow-up experiments[^landis2012call-e17]; to generalize to humans, preclinical guidelines most often recommend reproducing the effect in more than one animal model and replicating it independently[^henderson2013threats-e8] | [Preclinical animal studies](../../06_methods/preclinical_animal_study.md), [Bench experiment](../../06_methods/bench_experiment.md) |
| [Measurement](../../05_research-strategies/measure.md) | Checking whether measurement tools such as antibodies are themselves reliable. The quality of data obtained with antibodies varies greatly[^uhlen2016proposal-e1] | Validate for the application and the sample; good performance in blots does not mean good performance in other applications[^uhlen2016proposal-e2]; users do at least one validation in their own application and report the catalog and lot numbers in the paper[^uhlen2016proposal-e6] | [Bench experiment: authenticate reagents and cell lines](../../06_methods/bench_experiment.md#step-7-authenticate-your-reagents-and-cell-lines) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Pooling published preclinical studies, for example comparing several stroke animal studies of the same drug[^landis2012call-e4] | Check whether included studies reported randomization and blinding, because this affects effect sizes[^landis2012call-e4]; negative results often go unpublished, so animal studies may overestimate efficacy by about 30%[^mak2014lost-e4] | [Review studies](../../06_methods/review_study.md), [Meta-analysis](../../06_methods/meta_analysis.md) |

How to use this table `[Our analysis]`: first find your strategy from your central claim, then read the matching strategy page and methods page. A project often mixes several strategies, for example validating an antibody first (measurement) and then using it to test a mechanism (causal explanation); hold each part to its own standards.

---

## Research methods common in this field

**Cross-field research types**: [Preclinical animal studies](../../06_methods/preclinical_animal_study.md), [Bench experiments (wet lab)](../../06_methods/bench_experiment.md), [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), [Quantitative simulation](../../06_methods/simulation_study.md), [Replication studies](../../06_methods/replication.md), [Review studies](../../06_methods/review_study.md). The basic medical sciences do not yet have a methods page of their own.

What this field particularly demands `[Our analysis]`: in cell and molecular experiments, pay special attention to antibody validation; do animal model studies to the four core standards above, and state the gap between the model and humans in your conclusions; do pharmacology experiments to your target journal's design and analysis rules; safety and toxicology studies for regulatory submission must follow Good Laboratory Practice[^oecd1998glp-e2]; for research on human samples, confirm that the original consent covers your use[^wma2016taipei-e6]. Non-animal alternatives include in vitro studies, computer modeling, epidemiological studies, and others[^mak2014lost-e11].

---

## Advice for newcomers

1. **First decide how far your results need to travel.** If they are meant to support later animal or human studies, design the experiment to confirmatory standards from the start `[Our analysis]`; if you are only looking for leads, label the work honestly as exploratory[^landis2012call-e12].
2. **Before you start, settle four things:** how the sample size is calculated, how animals are randomized, who is blinded, and how data are handled (including the stopping rule, exclusion criteria, and primary endpoint)[^landis2012call-e1][^landis2012call-e9][^landis2012call-e11]. Write them down, ideally with your advisor's review `[Our analysis]`.
3. **Count your n correctly.** Use the number of independent samples for statistics, not the number of measurements[^curtis2018experimental-e3][^curtis2018experimental-e10].
4. **Validate a new antibody in your own samples and application before using it**, and record the catalog number, lot number, and RRID[^uhlen2016proposal-e6].
5. **Before using human samples, check what uses the ethics approval and the original consent forms cover**[^wma2016taipei-e6]; if you are unsure, ask your institution's ethics committee `[Our analysis]`.
6. **Read your target journal's design and statistics rules before you submit**, rather than waiting for reviewers to point them out; some journals will reject your paper outright for this[^curtis2018experimental-e8].
7. **Don't let your conclusions go beyond the model.** Working in mice only shows it works in mice; in the discussion, state the gap between the model and humans[^mak2014lost-e3] `[Our analysis]`.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| No randomization, no blinding, just "complied with animal regulations" in the paper | Studies that do not report randomization and blinding may show inflated effect sizes[^landis2012call-e4]; the *British Journal of Pharmacology* will reject outright[^curtis2018experimental-e8] |
| Running a few animals first, stopping if it's significant and adding more if it isn't | The stopping rule must be fixed in advance[^landis2012call-e9]; otherwise the chance of a false positive goes up `[Our analysis]` |
| Measuring three samples five times each and computing P values as n = 15 | n should be 3; the *British Journal of Pharmacology* does not accept this[^curtis2018experimental-e3] |
| Only 3 animals per group, but running statistical tests and drawing conclusions anyway | Experiments with too few animals can hardly detect meaningful differences[^landis2012call-e8]; the *British Journal of Pharmacology* does not allow statistics with n below 5[^curtis2018experimental-e2] |
| Using an antibody for immunohistochemistry just because it worked in a blot | Antibody performance depends on the application and sample, so validate for each application[^uhlen2016proposal-e2] |
| Showing only the strip of blot around the target size | Validation should show the whole gel[^uhlen2016proposal-e5]; with only a strip, no one can see whether there are extra bands elsewhere `[Our analysis]` |
| Using old samples from the pathology department directly for a new project | An ethics committee must confirm that the original consent covers the new use[^wma2016taipei-e6][^wma2024helsinki-e13] |
| Several animals died, and the paper doesn't mention it | If a treatment kills the weakest animals and this is not reported, it can look effective[^landis2012call-e10] |
| Writing up a mouse result as "promising for curing disease X" | Animal models struggle to reproduce human disease[^mak2014lost-e3]; in cancer, many findings in animal models have failed to be reproduced in clinical trials[^mak2014lost-e1] |

---

## Further reading

- **Landis et al. 2012, A call for transparent reporting to optimize the predictive value of preclinical research (Nature; author manuscript in PubMed Central)**: explains clearly why preclinical research needs randomization, blinding, sample size calculations, and prespecified data handling rules. Read it before you design your first animal experiment.
- **Curtis et al. 2018, Experimental design and analysis and their reporting II (British Journal of Pharmacology)**: one pharmacology journal's specific rules on n, normalization, outliers, and significance thresholds. For anyone in pharmacology or who runs a lot of Western blots; check the journal's latest version before submitting.
- **Uhlen et al. 2016, A proposal for validation of antibodies (Nature Methods)**: the five antibody validation strategies. Read it before you choose an antibody yourself for the first time; note the industry ties mentioned above.
- **Mak, Evaniew, and Ghert 2014, Lost in translation (American Journal of Translational Research)**: a short review of translational failure in cancer, with several concrete examples; most figures are cited from other studies. For anyone who wants to understand how "works in animals, fails in humans" happens.
- **OECD Principles of Good Laboratory Practice (the 1997 revision, published in 1998)**: for anyone doing toxicology or supporting a drug submission; others can just read the definitions in Section I and Section II, part 8, "Performance of the study".
- **World Medical Association, Declaration of Taipei (2016) and Declaration of Helsinki (2024)**: read them before using human samples or biobanks, then check against your country's regulations and your institution's ethics committee.

[^mak2014lost-e1]: Mak, Evaniew & Ghert 2014, Abstract. [Evidence](../../../sources/notes/mak2014lost.md#e1)
[^mak2014lost-e2]: Mak, Evaniew & Ghert 2014, Introduction. [Evidence](../../../sources/notes/mak2014lost.md#e2)
[^mak2014lost-e3]: Mak, Evaniew & Ghert 2014, Abstract. [Evidence](../../../sources/notes/mak2014lost.md#e3)
[^mak2014lost-e4]: Mak, Evaniew & Ghert 2014, Limitations of animal models in cancer research. [Evidence](../../../sources/notes/mak2014lost.md#e4)
[^mak2014lost-e5]: Mak, Evaniew & Ghert 2014, Limitations of animal models in cancer research. [Evidence](../../../sources/notes/mak2014lost.md#e5)
[^mak2014lost-e6]: Mak, Evaniew & Ghert 2014, Limitations of animal models in cancer research. [Evidence](../../../sources/notes/mak2014lost.md#e6)
[^mak2014lost-e7]: Mak, Evaniew & Ghert 2014, Notable examples of failed clinical cancer trials. [Evidence](../../../sources/notes/mak2014lost.md#e7)
[^mak2014lost-e8]: Mak, Evaniew & Ghert 2014, Notable examples of failed clinical cancer trials. [Evidence](../../../sources/notes/mak2014lost.md#e8)
[^mak2014lost-e9]: Mak, Evaniew & Ghert 2014, Introduction. [Evidence](../../../sources/notes/mak2014lost.md#e9)
[^mak2014lost-e10]: Mak, Evaniew & Ghert 2014, Introduction. [Evidence](../../../sources/notes/mak2014lost.md#e10)
[^mak2014lost-e11]: Mak, Evaniew & Ghert 2014, Critical re-evaluation of animal models and alternative strategies. [Evidence](../../../sources/notes/mak2014lost.md#e11)
[^freedman2015economics-e6]: Freedman et al. 2015, main text, after the direct economic costs. [Evidence](../../../sources/notes/freedman2015economics.md#e6)
[^freedman2015economics-e7]: Freedman et al. 2015, main text, causes of irreproducibility. [Evidence](../../../sources/notes/freedman2015economics.md#e7)
[^freedman2015economics-e8]: Freedman et al. 2015, main text, Introduction. [Evidence](../../../sources/notes/freedman2015economics.md#e8)
[^freedman2015economics-e9]: Freedman et al. 2015, main text, solutions section. [Evidence](../../../sources/notes/freedman2015economics.md#e9)
[^landis2012call-e1]: Landis et al. 2012, Abstract. [Evidence](../../../sources/notes/landis2012call.md#e1)
[^landis2012call-e2]: Landis et al. 2012, Widespread deficiencies in methods reporting. [Evidence](../../../sources/notes/landis2012call.md#e2)
[^landis2012call-e3]: Landis et al. 2012, Widespread deficiencies in methods reporting. [Evidence](../../../sources/notes/landis2012call.md#e3)
[^landis2012call-e4]: Landis et al. 2012, Widespread deficiencies in methods reporting. [Evidence](../../../sources/notes/landis2012call.md#e4)
[^landis2012call-e5]: Landis et al. 2012, Widespread deficiencies in methods reporting. [Evidence](../../../sources/notes/landis2012call.md#e5)
[^landis2012call-e6]: Landis et al. 2012, Box 1. [Evidence](../../../sources/notes/landis2012call.md#e6)
[^landis2012call-e7]: Landis et al. 2012, Randomization and blinding. [Evidence](../../../sources/notes/landis2012call.md#e7)
[^landis2012call-e8]: Landis et al. 2012, Sample-size estimation. [Evidence](../../../sources/notes/landis2012call.md#e8)
[^landis2012call-e9]: Landis et al. 2012, Interim data analysis. [Evidence](../../../sources/notes/landis2012call.md#e9)
[^landis2012call-e10]: Landis et al. 2012, Ad hoc exclusion of data. [Evidence](../../../sources/notes/landis2012call.md#e10)
[^landis2012call-e11]: Landis et al. 2012, Retrospective primary end-point selection. [Evidence](../../../sources/notes/landis2012call.md#e11)
[^landis2012call-e12]: Landis et al. 2012, An important note about exploratory experiments. [Evidence](../../../sources/notes/landis2012call.md#e12)
[^landis2012call-e14]: Landis et al. 2012, The path to implementation. [Evidence](../../../sources/notes/landis2012call.md#e14)
[^landis2012call-e15]: Landis et al. 2012, Small effect sizes. [Evidence](../../../sources/notes/landis2012call.md#e15)
[^landis2012call-e16]: Landis et al. 2012, Abstract. [Evidence](../../../sources/notes/landis2012call.md#e16)
[^landis2012call-e17]: Landis et al. 2012, An important note about exploratory experiments. [Evidence](../../../sources/notes/landis2012call.md#e17)
[^curtis2018experimental-e1]: Curtis et al. 2018, Abstract. [Evidence](../../../sources/notes/curtis2018experimental.md#e1)
[^curtis2018experimental-e2]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../../sources/notes/curtis2018experimental.md#e2)
[^curtis2018experimental-e3]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../../sources/notes/curtis2018experimental.md#e3)
[^curtis2018experimental-e4]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../../sources/notes/curtis2018experimental.md#e4)
[^curtis2018experimental-e5]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../../sources/notes/curtis2018experimental.md#e5)
[^curtis2018experimental-e6]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../../sources/notes/curtis2018experimental.md#e6)
[^curtis2018experimental-e7]: Curtis et al. 2018, Table 1 and notes. [Evidence](../../../sources/notes/curtis2018experimental.md#e7)
[^curtis2018experimental-e8]: Curtis et al. 2018, Areas of particular concern that require renewed vigilance. [Evidence](../../../sources/notes/curtis2018experimental.md#e8)
[^curtis2018experimental-e9]: Curtis et al. 2018, What is a group and what is a group size? [Evidence](../../../sources/notes/curtis2018experimental.md#e9)
[^curtis2018experimental-e10]: Curtis et al. 2018, What is a group and what is a group size? [Evidence](../../../sources/notes/curtis2018experimental.md#e10)
[^curtis2018experimental-e11]: Curtis et al. 2018, Flexibility and pilot data. [Evidence](../../../sources/notes/curtis2018experimental.md#e11)
[^curtis2018experimental-e12]: Curtis et al. 2018, Conclusions. [Evidence](../../../sources/notes/curtis2018experimental.md#e12)
[^curtis2018experimental-e13]: Curtis et al. 2018, Introduction. [Evidence](../../../sources/notes/curtis2018experimental.md#e13)
[^henderson2013threats-e8]: Henderson et al. 2013, Results, Threats to Internal Validity, Construct Validity, and External Validity. [Evidence](../../../sources/notes/henderson2013threats.md#e8)
[^uhlen2016proposal-e1]: Uhlen et al. 2016, Introduction. [Evidence](../../../sources/notes/uhlen2016proposal.md#e1)
[^uhlen2016proposal-e2]: Uhlen et al. 2016, Introduction. [Evidence](../../../sources/notes/uhlen2016proposal.md#e2)
[^uhlen2016proposal-e3]: Uhlen et al. 2016, Introduction. [Evidence](../../../sources/notes/uhlen2016proposal.md#e3)
[^uhlen2016proposal-e4]: Uhlen et al. 2016, Genetic strategies. [Evidence](../../../sources/notes/uhlen2016proposal.md#e4)
[^uhlen2016proposal-e5]: Uhlen et al. 2016, Independent antibody strategies. [Evidence](../../../sources/notes/uhlen2016proposal.md#e5)
[^uhlen2016proposal-e6]: Uhlen et al. 2016, Suggestions for providers and users. [Evidence](../../../sources/notes/uhlen2016proposal.md#e6)
[^uhlen2016proposal-e7]: Uhlen et al. 2016, Antibody reproducibility. [Evidence](../../../sources/notes/uhlen2016proposal.md#e7)
[^uhlen2016proposal-e8]: Uhlen et al. 2016, Suggestions for providers and users. [Evidence](../../../sources/notes/uhlen2016proposal.md#e8)
[^uhlen2016proposal-e9]: Uhlen et al. 2016, Additional methods for antibody characterization. [Evidence](../../../sources/notes/uhlen2016proposal.md#e9)
[^uhlen2016proposal-e10]: Uhlen et al. 2016, Acknowledgments; Competing financial interests. [Evidence](../../../sources/notes/uhlen2016proposal.md#e10)
[^wma2024helsinki-e1]: WMA 2024, Preamble. [Evidence](../../../sources/notes/wma2024helsinki.md#e1)
[^wma2024helsinki-e11]: WMA 2024, Free and Informed Consent. [Evidence](../../../sources/notes/wma2024helsinki.md#e11)
[^wma2024helsinki-e12]: WMA 2024, Free and Informed Consent. [Evidence](../../../sources/notes/wma2024helsinki.md#e12)
[^wma2024helsinki-e13]: WMA 2024, Free and Informed Consent. [Evidence](../../../sources/notes/wma2024helsinki.md#e13)
[^wma2016taipei-e2]: WMA 2016 (Declaration of Taipei), para. 4. [Evidence](../../../sources/notes/wma2016taipei.md#e2)
[^wma2016taipei-e3]: WMA 2016 (Declaration of Taipei), para. 12. [Evidence](../../../sources/notes/wma2016taipei.md#e3)
[^wma2016taipei-e4]: WMA 2016 (Declaration of Taipei), para. 12. [Evidence](../../../sources/notes/wma2016taipei.md#e4)
[^wma2016taipei-e5]: WMA 2016 (Declaration of Taipei), para. 15. [Evidence](../../../sources/notes/wma2016taipei.md#e5)
[^wma2016taipei-e6]: WMA 2016 (Declaration of Taipei), para. 19. [Evidence](../../../sources/notes/wma2016taipei.md#e6)
[^wma2016taipei-e7]: WMA 2016 (Declaration of Taipei), para. 6. [Evidence](../../../sources/notes/wma2016taipei.md#e7)
[^wma2016taipei-e8]: WMA 2016 (Declaration of Taipei), para. 21. [Evidence](../../../sources/notes/wma2016taipei.md#e8)
[^wma2016taipei-e9]: WMA 2016 (Declaration of Taipei), para. 7. [Evidence](../../../sources/notes/wma2016taipei.md#e9)
[^oecd1998glp-e1]: OECD 1998, Section I, 2.1. [Evidence](../../../sources/notes/oecd1998glp.md#e1)
[^oecd1998glp-e2]: OECD 1998, Section I, 1. Scope. [Evidence](../../../sources/notes/oecd1998glp.md#e2)
[^oecd1998glp-e3]: OECD 1998, Preface. [Evidence](../../../sources/notes/oecd1998glp.md#e3)
[^oecd1998glp-e4]: OECD 1998, Foreword. [Evidence](../../../sources/notes/oecd1998glp.md#e4)
[^oecd1998glp-e5]: OECD 1998, Preface. [Evidence](../../../sources/notes/oecd1998glp.md#e5)
[^oecd1998glp-e6]: OECD 1998, Section II, 1.2. [Evidence](../../../sources/notes/oecd1998glp.md#e6)
[^oecd1998glp-e7]: OECD 1998, Section II, 2.1. [Evidence](../../../sources/notes/oecd1998glp.md#e7)
[^oecd1998glp-e8]: OECD 1998, Section II, 8.1. [Evidence](../../../sources/notes/oecd1998glp.md#e8)
[^oecd1998glp-e9]: OECD 1998, Section II, 8.1. [Evidence](../../../sources/notes/oecd1998glp.md#e9)
[^oecd1998glp-e10]: OECD 1998, Section II, 8.3. [Evidence](../../../sources/notes/oecd1998glp.md#e10)
[^oecd1998glp-e11]: OECD 1998, Section II, 8.3. [Evidence](../../../sources/notes/oecd1998glp.md#e11)
[^oecd1998glp-e12]: OECD 1998, Foreword. [Evidence](../../../sources/notes/oecd1998glp.md#e12)
[^oecd1998glp-e13]: OECD 1998, Section II, 10.1. [Evidence](../../../sources/notes/oecd1998glp.md#e13)
[^oecd1998glp-e14]: OECD 1998, Foreword. [Evidence](../../../sources/notes/oecd1998glp.md#e14)
