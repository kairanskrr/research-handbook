# Biological sciences: field overview

This page explains how research in the biological sciences actually works, focusing on laboratory life science: how labs are organized, why experiments are slow, how to keep a lab notebook, how to handle replicates and controls, the rules for animal research, how papers get published and authored, and where your data goes. Field ecology, evolutionary biology, and similar areas have their own practices and come up only in passing. Practices shared by every field (choosing a topic, planning, writing, peer review, research ethics) are covered in the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and in [Throughout the project](../../08_throughout/README.md), and are not repeated here. For the research strategies the biological sciences commonly use and the evidence each one needs, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

**After reading this page, you should be able to:**

- explain how work is divided in a life-science lab, and how a paper gets from the bench to a journal;
- tell independent replicates from repeated measurements, and know what your n really is;
- know why reagents, antibodies, and cell lines must be validated, and which principles and reporting guidelines apply to animal experiments;
- avoid the mistakes newcomers make most often with record-keeping, replicates, controls, and data deposition.

---

## How research works in this field

### The lab revolves around the PI

Lab-based research is organized by research group: the principal investigator (PI) sets the direction and finds the funding, and students and postdocs do the experiments at the bench. This division of labor shows up in authorship too: in biomedicine, by informal convention, the last author is seen as the person who drove the work intellectually and financially[^tscharntke2007author-e2].

For a newcomer this means the reagents, cells, animals, and instruments you use are mostly shared with the group, so record-keeping and handovers follow the group's rules; and your project is often one piece of the PI's larger program. If your institution has no notebook policy, the group should have its own[^schnell2015ten-e2]. For agreeing on expectations with your advisor and reporting progress, see [Collaboration and advisors](../../08_throughout/collaboration_and_advisors.md) in Throughout the project.

### Wet-lab work is slow and full of surprises

**Wet-lab** experiments are done at the bench with cells, tissues, animals, and reagents; research done only on a computer is **dry-lab** work. Wet-lab work runs at a very different pace from computational research:

- **Long timelines.** An extreme example: the Reproducibility Project: Cancer Biology (a large project that set out to repeat published cancer biology experiments) reported 90 weeks between starting experiments and delivering final data[^errington2021challenges-e4]. This figure comes from a large replication project and does not represent the pace of a typical project, but it shows how time-consuming wet-lab work can be.
- **Protocols often have to change.** In the same project, 67% of experimental protocols that had already passed peer review needed modifying once work began, and only 41% of those modifications could actually be carried out[^errington2021challenges-e2]. Sometimes the change was small, such as adjusting antibody concentration or blocking reagent in a Western blot (a method for detecting a specific protein)[^errington2021challenges-e3].
- **Published methods may not be enough.** None of the 193 experiments the project planned to repeat could be designed from the original paper alone; every one required asking the original authors[^errington2021challenges-e1].

So build slack into a wet-lab plan, and get the method working first in a small pilot study. For planning and for doing the riskiest part first, see the Part 2 chapters [Writing a research plan](../../02_do-the-project/03_research-plan.md) and [Running and iterating](../../02_do-the-project/06_run-and-iterate.md).

### The lab notebook is the primary record

The lab notebook is the main record of research activity and the legal document that establishes who owns ideas and results[^schnell2015ten-e1]. The rules below come from an article written for computational biologists[^schnell2015ten-e8], but they are general notebook rules and, we think, apply equally to wet-lab work. For how to keep a research log in general, see the Part 2 chapter [Running and iterating](../../02_do-the-project/06_run-and-iterate.md#3-leave-a-record-of-every-run) and [Organizing your research materials](../../08_throughout/organizing_materials.md#5-keep-three-kinds-of-notes-apart).

- **Write it down as you go.** Record each entry right after you do the work[^schnell2015ten-e3]. If you rely on memory, you will very likely not remember when it counts[^schnell2015ten-e9].
- **Cross out mistakes; never erase.** In a paper notebook, strike through an error with a single thin line and write the correction next to it; never erase or destroy a record[^schnell2015ten-e4].
- **Record who did what, as if it were evidence.** Each entry should say who did which part of the work and who was present at discussions[^schnell2015ten-e5]. In a research misconduct investigation, the institution or a government funding agency can take the notebook as evidence[^schnell2015ten-e6].
- **Keep the raw data behind every figure**[^schnell2015ten-e7].

### Publishing: journals and preprints

In the life sciences, formal publication means publishing in a journal. This differs from computer science, where conferences dominate; see the [computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue). A **preprint** is a manuscript made public before peer review. The life sciences have a dedicated preprint server, bioRxiv, which archives and distributes unpublished papers for free[^biorxivabout-e1]. A few things to know:

- Articles are **not peer-reviewed** before they go online[^biorxivabout-e2], so when you read someone else's preprint, you have to judge its quality yourself.
- You can post before or at the same time as submitting to a journal; papers already accepted by a journal should not be posted[^biorxivabout-e3]. **Once posted, a preprint cannot be removed**, because it can already be cited[^biorxivabout-e4].
- bioRxiv says most journals allow preprints before publication, but check your target journal's policy before posting[^biorxivabout-e5]. The benefit is that peers can see your results immediately, and you can get feedback before you submit[^biorxivabout-e6].

### Authorship: first and last authors get the most attention

- **First author**: traditionally the person who contributed most, and who receives the most credit[^tscharntke2007author-e1].
- **Last author**: in biomedicine, by informal convention, often receives as much credit as the first author[^tscharntke2007author-e2]. Evaluation committees and funding agencies often treat it as a sign of leading the group, but this is only an informal convention and is not always followed[^tscharntke2007author-e3].
- **Middle authors**: how they are ordered varies a lot between countries and fields[^tscharntke2007author-e4]. Some authors suggest stating in the acknowledgments which ordering approach the paper uses[^tscharntke2007author-e5].
- **Corresponding author**: as the International Committee of Medical Journal Editors (ICMJE) defines it, the person who takes primary responsibility for communicating with the journal during submission, peer review, and publication[^icmje2026recommendations-e28].

There is no single rule across the life sciences for who qualifies as an author; follow your target journal's instructions for authors. The often-cited ICMJE authorship criteria were written for medical journals. For those criteria and the practice of discussing authorship at the start, see [Collaboration and advisors: authorship](../../08_throughout/collaboration_and_advisors.md#6-authorship-discuss-it-at-the-start-and-adjust-as-you-go) in Throughout the project.

---

## How this field differs from others

The table compares the biological sciences with computer science. The computer science column is based on the [computer science page](../computer-science/README.md); the biology column summarizes this page's sources.

| | Biological sciences (lab-based) | Computer science |
|---|---|---|
| Formal publication | Journals; bioRxiv preprints posted before or at submission[^biorxivabout-e3] | Conferences dominate in most subfields |
| Experiment timeline | Can be very long: one large replication project took 90 weeks from starting experiments to delivering data[^errington2021challenges-e4] | Many experiments can be rerun quickly on a computer |
| How n is counted | By independent experimental units (animal, cage, litter, etc.), not by number of measurements[^perciedusert2020reporting-e4][^perciedusert2020reporting-e6] | Often by random seeds, datasets, and so on |
| Materials | Reagents, antibodies, and cell lines can themselves be faulty and need validating[^nihrigorguidance-e4] | Code and data can be copied exactly |
| Ethics approval | Animal experiments generally need harm-benefit approval[^perciedusert2020arrive-e6] | Only when people or security issues are involved |
| Data | Journals may require sequences and similar data to be deposited in dedicated public databases, as PLOS does[^plosdatapolicy-e2] | Usually relies on artifact evaluation and code repositories |

---

## Norms and reporting standards in this field

### Identify the experimental unit before you count n

If n is wrong, the statistics that follow cannot be trusted and may produce false positives[^perciedusert2020reporting-e5]. The **experimental unit** is the entity that independently receives a treatment: any two experimental units could be assigned to different treatment groups[^perciedusert2020reporting-e3]. It is often a single animal, but it can also be a cage or litter of animals, or part of an animal's body[^perciedusert2020reporting-e6]. Distinguish two kinds of "replicate" (the names below are common lab usage):

- **Biological replicates (independent replicates)**: each run uses a different animal or a different independent culture. Only these test your hypothesis. To generalize a conclusion to a kind of mouse, you need several independent comparisons using several mice[^vaux2012replicates-e2].
- **Technical replicates (repeated measurements)**: measuring the same sample several times, or splitting one cell suspension across several plates. They are not independent tests of the hypothesis and cannot be used to calculate confidence intervals or P values[^vaux2012replicates-e1]; they support conclusions only about that one sample[^vaux2012replicates-e5]. In short, you can generalize only to the population from which you drew independent samples[^vaux2012replicates-e3].

Technical replicates do have a use: they check whether the experiment itself was done well. If one plate gives a clearly odd result, for example, you would check whether it was mislabeled or contaminated with yeast[^vaux2012replicates-e4]. But they don't count toward n: when the experimental unit is the mouse, measuring 50 cells from one mouse still gives n = 1[^perciedusert2020reporting-e4]. Reporting it as n = 50 is **pseudoreplication**; it underestimates the true variation and leads to false positives[^perciedusert2020reporting-e5].

Factors in an experiment are often nested: cells within animals, animals within cages[^perciedusert2020reporting-e10]. Before designing an experiment, sketch these levels and mark which one is the experimental unit. For the general approach to statistics, see the Part 2 chapter section [Report how big the difference is and how sure you are, not just the p-value](../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Controls, randomization, and blinding

- **Include control groups, and justify it if you don't**[^perciedusert2020reporting-e1]. **Negative controls** tell you whether a difference was caused by the treatment, for example wild-type versus genetically modified animals, or sham surgery versus real surgery; **positive controls** confirm that the experiment can detect the expected effect and help you interpret negative results[^perciedusert2020reporting-e2].
- **Change one factor at a time.** Only when the two groups differ in just the factor you care about can you attribute the difference to it[^vaux2012replicates-e6].
- **Randomize properly.** Picking whichever animal comes to hand from the cage is not random, because human judgment is involved[^perciedusert2020reporting-e7].
- **Blind wherever you can.** Researchers often expect a particular result and may unconsciously influence the experiment or how they read the data. **Blinding** means keeping the people who allocate groups, run the experiment, assess outcomes, and analyze data from knowing, as far as possible, which group each subject is in, to reduce this bias; the paper should state who knew the group allocation at each stage[^perciedusert2020reporting-e8].
- **Don't report selectively.** Dropping groups because their data conflict with the paper's story is misleading[^perciedusert2020reporting-e9]. Results from independent samples can be excluded only in special circumstances[^vaux2012replicates-e8].
- **Don't overstate your conclusions.** If you saw only a partial effect, don't say a gene is "essential"[^vaux2012replicates-e7].

### Validate reagents, antibodies, and cell lines

In computational research, a copy of the code is identical to the original. Wet-lab work is different: the reagents themselves can be the problem.

- Unstable or poorly validated reagents and biological materials are one reason research is hard to reproduce[^perciedusert2020arrive-e4]. Freedman and colleagues sort the main causes of irreproducible preclinical research (research before human trials, such as cell and animal experiments) into four categories, one of which is biological reagents and reference materials[^freedman2015economics-e1].
- **Your cell line may not be what you think it is.** Freedman and colleagues' 2015 article puts the rate of cell line misidentification and cross-contamination in biomedical research at an estimated 15% to 36%[^freedman2015economics-e2]. This is an estimated range, not a precise measurement. The article also says that short tandem repeat (STR) profiling is the accepted method for authenticating cell line identity, at about $200 per test, yet typically only a third of labs test their cell lines' identity[^freedman2015economics-e3].
- **Some funders require it too.** For example, the US National Institutes of Health (NIH) lists "authentication of key biological and/or chemical resources" as one of four areas of focus in grant applications and review[^nihrigorguidance-e2]; these resources include cell lines, antibodies, and the like, and their quality directly determines whether results can be reproduced[^nihrigorguidance-e4].
- **Other people's materials may not be available.** In the replication project above, 136 of the 193 planned experiments (70%) required asking the original authors for key reagents such as cell lines, plasmids, model organisms, and antibodies; these reagents could neither be bought nor found in public repositories[^errington2021challenges-e5].
- **Make validation standard practice.** Freedman and colleagues recommend that PIs make the use of validated reagents a documented standard practice[^freedman2015economics-e5]. In practice: record each reagent's source, catalog number, and lot number in your notebook; authenticate new cell lines before use; and check new antibodies with positive and negative controls to confirm they recognize the right protein.

### Animal research: the 3Rs and the ARRIVE guidelines

The **3Rs**, proposed more than 50 years ago, are a framework for more humane animal research and are written into many national and international regulations[^nc3rsthe3rs-e1]:

| Principle | Meaning |
|---|---|
| Replacement | Avoid using animals where possible[^nc3rsthe3rs-e2], for example by using human tissues and cells, computer models, or cell lines[^nc3rsthe3rs-e4] |
| Reduction | Use fewer animals while still meeting the scientific aims[^nc3rsthe3rs-e2]; good experimental design and analysis make the results robust[^nc3rsthe3rs-e3] |
| Refinement | Minimize the animals' pain, suffering, distress, and lasting harm[^nc3rsthe3rs-e2] |

Approval for animal experiments is generally based on a harm-benefit analysis: the harm to the animals is weighed against the benefit of the research to society[^perciedusert2020arrive-e6]. Even rigorous research can fail to deliver that benefit if it is reported unclearly[^perciedusert2020arrive-e6]. So report fully: **ARRIVE** (Animal Research: Reporting of In Vivo Experiments) is a checklist of the information a paper on animal experiments should include, so that others can scrutinize, evaluate, and repeat the work[^perciedusert2020arrive-e1]. It applies to all research using live animals[^perciedusert2020arrive-e8]. Version 2.0 has two sets[^perciedusert2020arrive-e2]:

- **The ARRIVE Essential 10** (the minimum): study design, sample size, measures to reduce subjective bias, outcome measures, statistical methods, experimental animals, experimental procedures, and results[^perciedusert2020arrive-e3].
- **The Recommended Set**: ethics statement, declaration of interests, protocol registration, data access, and details such as housing and husbandry[^perciedusert2020arrive-e9].

The evidence on incomplete reporting: earlier studies cited by the ARRIVE authors found that only 30–40% of animal research papers reported randomization, about 20% reported blinding, and fewer than 10% justified their sample size[^perciedusert2020arrive-e5]. ARRIVE can also be used **while you design the experiment**[^perciedusert2020arrive-e7].

Another point that is easy to miss: biological variables such as sex, age, weight, and underlying health often affect health and disease[^nihrigorguidance-e5]. NIH, for example, requires the vertebrate animal and human studies it funds to account for sex as a variable in design, analysis, and reporting[^nihrigorguidance-e3]. Other funders have their own rules, which take precedence.

### Deposit data in public databases

Some kinds of data have dedicated public databases in the field. The example below is the data policy of the PLOS journals, which is one publisher's rule:

- At publication, all data needed to replicate the findings must be made available[^plosdatapolicy-e1].
- Where the field has a data deposition standard, you must follow it; for example, gene sequences go to GenBank, the European Molecular Biology Laboratory (EMBL) database, or the DNA Data Bank of Japan (DDBJ), and microarray data to ArrayExpress or the Gene Expression Omnibus (GEO)[^plosdatapolicy-e2].
- The paper's data availability statement must give the database name and the **accession number** (the unique identifier the database assigns to each record)[^plosdatapolicy-e3].
- "Data not shown" is not allowed[^plosdatapolicy-e4].
- For Western blots and gels, provide the original, uncropped images[^plosdatapolicy-e5]; the values behind the figures must also be supplied[^plosdatapolicy-e6].
- Journals differ, so follow your target journal's policy. For how to keep raw data, see [Organizing your research materials](../../08_throughout/organizing_materials.md#2-raw-data-is-read-only-everything-else-can-be-regenerated) in Throughout the project.

### Reproducibility: a problem the field is facing

- The Reproducibility Project: Cancer Biology ended up repeating 50 experiments from 23 papers, covering 158 effects[^errington2021investigating-e1]. Looking only at the positive effects reported in the original papers, the median effect size in the replications was 85% smaller than the median effect size in the original experiments[^errington2021investigating-e2].
- A failed replication does not mean the original result was wrong, only that more research is needed to confirm it; likewise, a successful replication does not prove the original result[^errington2021investigating-e3].
- The original papers' data were also hard to get: of the 193 planned experiments, only 4 had published the data needed to calculate effect sizes and do power analyses; even after contacting the original authors, the data could not be obtained for 68% of the experiments[^errington2021challenges-e6].
- Pooling earlier studies, Freedman and colleagues estimated that the cumulative rate of irreproducible preclinical research exceeds 50%. But this number is extrapolated and its range is wide: as low as 18% if the different problems overlap heavily, and as high as 88.5% if they barely overlap[^freedman2015economics-e4]. So treat it only as a rough estimate; it does not mean "more than half of all studies are wrong".
- Some funders have built rigor into their application and review criteria. NIH, for example, defines scientific rigor as the strict application of the scientific method throughout experimental design, methodology, analysis, interpretation, and reporting, to ensure robust and unbiased results[^nihrigorguidance-e1].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by its central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table lists only what this page's sources support; the grouping and the "What it looks like in the biological sciences" column are our own synthesis.

| Strategy | What it looks like in the biological sciences | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Cell and molecular experiments: change one factor (for example, knock down a gene) and see whether the outcome changes | Change one factor at a time[^vaux2012replicates-e6]; include control groups, or justify not doing so[^perciedusert2020reporting-e1]; count n by independent experimental units, not by number of measurements[^perciedusert2020reporting-e4]; technical replicates cannot be used to calculate P values[^vaux2012replicates-e1] | [Bench experiment](../../06_methods/bench_experiment.md) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Animal experiments: treating and measuring live animals | Generally needs harm-benefit approval[^perciedusert2020arrive-e6] and a design following the 3Rs[^nc3rsthe3rs-e2]; randomize properly[^perciedusert2020reporting-e7] and state who knew the group allocation at each stage[^perciedusert2020reporting-e8]; report against the ARRIVE Essential 10[^perciedusert2020arrive-e3] | [Preclinical animal studies](../../06_methods/preclinical_animal_study.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Descriptive omics studies: generating large datasets with microarrays or high-throughput sequencing to describe the state of the samples | Provide enough information for others to interpret the results unambiguously and potentially reproduce the experiment[^fgedmiame-e1][^fgedminseqe-e1]: raw data, processed data, and the experimental and data-processing protocols[^fgedmiame-e2][^fgedminseqe-e2] (the two minimum information standards are described after the table) | [Data science research](../../06_methods/data_science.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Systematic reviews and meta-analyses: pooling published studies to answer a question | Collect and synthesize evidence with structured, transparent, and reproducible methods[^odea2021preferred-e1]; report what was done, why, and what was found, so readers can judge whether to trust the conclusions[^odea2021preferred-e2] (the ecology reporting checklist and the risk-of-bias tool for animal studies are described after the table) | [Review studies](../../06_methods/review_study.md), [Meta-analysis](../../06_methods/meta_analysis.md) |

How to use this table:

- **Replicating published experiments follows the same standards.** For what the large replication project found, see [Reproducibility](#reproducibility-a-problem-the-field-is-facing) above; for how to do it, see [Replication studies](../../06_methods/replication.md).
- **If you are developing a new experimental technique or analysis software, read your target journal's requirements first.** This page looked at only two journals' guidance, and each speaks only for itself. *Nature Methods*' aims and scope require that a method be thoroughly validated, applied to an important biological question, and benchmarked against existing methods[^naturemethodsaims-e1]; papers are selected on breadth of interest, how thoroughly the method's performance is evaluated, and whether the technical description is complete enough for others to use it right away[^naturemethodsaims-e2]. *PLOS Computational Biology* accepts software articles describing open-source tools (source code public, with others allowed to use and modify it) that are broadly useful and represent a significant advance in delivering new biological insight[^ploscompbiolsubmission-e1]; the software must be widely adopted or likely to be, the source code must be anonymously downloadable under an open-source license, and it must come with installation and usage documentation, including how to check the software with the supplied test data[^ploscompbiolsubmission-e2].
- **Our sources do not cover other strategies.**

The omics and systematic review rows cite standards issued by specific organizations in specific years, not uniform rules for the biological sciences; what you must submit and how you must report it today is set by your target journal and data repository.

- **Omics data: MIAME and MINSEQE.** MIAME (Minimum Information About a Microarray Experiment) was proposed in 2001[^fgedmiame-e1]; version 1.0 of MINSEQE (Minimum Information about a high-throughput nucleotide SEQuencing Experiment) was released in 2012[^fgedminseqe-e3]. Both were maintained by the Functional Genomics Data Society (FGED), which has since ceased operating[^fgedmiame-e3]. MIAME specifically requires stating which data file corresponds to which sample, and which samples are technical and which are biological replicates[^fgedmiame-e2]. For which database to deposit in, see [Deposit data in public databases](#deposit-data-in-public-databases) above.
- **Reviews in ecology and evolutionary biology: PRISMA-EcoEvo.** This is the extension for these two fields of PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses), the reporting guideline for systematic reviews. It was published in 2021 and has 27 main items[^odea2021preferred-e5]. One of them: register the review's aims and methods in a public, time-stamped archive, ideally before searching the literature[^odea2021preferred-e6]. Its authors assessed 102 systematic reviews and meta-analyses published in 2010–2019 and found reporting quality far from ideal[^odea2021preferred-e3]; the few papers (about 16%) that cited a reporting guideline had clearly better reporting than average[^odea2021preferred-e4]. We did not find a dedicated systematic review reporting checklist for molecular and cell biology (for example, for pooling in vitro experiments). The general PRISMA 2020 was designed mainly for systematic reviews evaluating health interventions, but its authors note that many items also apply to systematic reviews with other aims[^page2021prisma-e17]; you can report against it to start with, as described in [Meta-analysis](../../06_methods/meta_analysis.md#step-8-report-according-to-prisma-2020). If you are pooling animal studies, also assess bias with the SYRCLE tool in the next item.
- **Pooling animal studies: the SYRCLE risk of bias tool.** SYRCLE is the SYstematic Review Centre for Laboratory animal Experimentation[^hooijmans2014syrcle-e4]. Its tool, published in 2014, has 10 items for assessing each included animal study for bias[^hooijmans2014syrcle-e1]; it was adapted from the Cochrane Collaboration's risk of bias tool for randomized controlled trials[^hooijmans2014syrcle-e2][^hooijmans2014syrcle-e3].

---

## Research methods common in this field

The grouping below is our own. For cell and molecular experiments, see [Bench experiments (wet lab)](../../06_methods/bench_experiment.md); it shares its logic with [Controlled experiments](../../06_methods/controlled_experiment.md), but that page is about human participants. For animal experiments, see [Preclinical animal studies](../../06_methods/preclinical_animal_study.md). Omics and bioinformatics analyses are close to [Data science](../../06_methods/data_science.md), with the added need to document the samples and experimental conditions behind the data; for recording software, versions, and parameters, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project. For computational modeling, see [Quantitative simulation](../../06_methods/simulation_study.md); for replication, see [Replication studies](../../06_methods/replication.md) (the difficulty in wet-lab replication is that method details and materials are hard to obtain[^errington2021challenges-e1][^errington2021challenges-e5]); for systematic reviews and meta-analyses, see [Review studies](../../06_methods/review_study.md).

---

## Advice for newcomers

1. **Learn the group's rules before you start.** The group should have rules on how to keep and store notebooks[^schnell2015ten-e2]; also find out how to get reagents and how to book animals and instruments.
2. **When designing an experiment, fix the experimental unit before you count n.** Technical replicates cannot stand in for independent replicates[^perciedusert2020reporting-e4]. If you are unsure, ask your advisor or a statistician before you start.
3. **Include control groups (or justify not doing so), randomize wherever you can, and blind wherever you can**[^perciedusert2020reporting-e1][^perciedusert2020reporting-e7][^perciedusert2020reporting-e8].
4. **Record on the same day, and never erase mistakes**[^schnell2015ten-e3][^schnell2015ten-e4]. Record reagent sources and lot numbers too.
5. **Validate new cell lines and antibodies before using them**[^nihrigorguidance-e4].
6. **Read ARRIVE before you do animal experiments**, and design to it rather than filling it in when you write the paper[^perciedusert2020arrive-e7].
7. **Check the journal's policy before posting a preprint**, and remember that once posted, it cannot be withdrawn[^biorxivabout-e4][^biorxivabout-e5].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Measuring 50 cells from one mouse and reporting n = 50 | When the experimental unit is the mouse, n = 1; this is pseudoreplication and leads to false positives[^perciedusert2020reporting-e4][^perciedusert2020reporting-e5] |
| Measuring the same sample three times, calling it "three replicates," and calculating a P value | Technical replicates are not independent tests of the hypothesis[^vaux2012replicates-e1] |
| Dropping groups or samples because the results were not what you expected | It is misleading; independent samples can be excluded only in special circumstances[^perciedusert2020reporting-e9][^vaux2012replicates-e8] |
| Using a cell line from another lab without ever authenticating it | Cell line misidentification and cross-contamination are not rare; one estimate puts them at 15–36%[^freedman2015economics-e2] |
| Writing "data not shown," or including only cropped blots | Some journals do not allow it, PLOS among them[^plosdatapolicy-e4][^plosdatapolicy-e5] |
| Writing a very brief methods section | Others cannot repeat the work; in the replication project, not one experiment could be designed from the original paper alone[^errington2021challenges-e1] |

---

## Further reading

- **ARRIVE 2.0 and its Explanation and Elaboration document (Percie du Sert et al. 2020, PLoS Biology)**: the reporting checklist for animal experiments; the explanation document covers experimental units, controls, randomization, and blinding item by item. Read it before doing animal experiments; people doing cell experiments can learn experimental design from it too.
- **Vaux et al. 2012, Replicates and repeats (EMBO Reports)**: uses two concrete examples to make clear the difference between repeated measurements and independent replicates. Read it before you count n for the first time.
- **Schnell 2015, Ten Simple Rules for a Computational Biologist's Laboratory Notebook**: ten notebook rules; short.
- **The 3Rs pages of the NC3Rs (the UK's National Centre for the Replacement, Refinement and Reduction of Animals in Research)**: definitions and examples of the 3Rs.
- **The two Errington et al. 2021 papers (eLife)**: the results of the Reproducibility Project: Cancer Biology and the obstacles it ran into. For anyone who wants to understand why methods must be detailed and materials shared.
- **ICMJE's guidance on authors and contributors**: the original text of the four authorship criteria. It is aimed at medical journals; when submitting to a biology journal, read that journal's own instructions for authors and data policy first.

[^tscharntke2007author-e1]: Tscharntke et al. 2007, para. 1. [Evidence](../../../sources/notes/tscharntke2007author.md#e1)
[^tscharntke2007author-e2]: Tscharntke et al. 2007, para. 2. [Evidence](../../../sources/notes/tscharntke2007author.md#e2)
[^tscharntke2007author-e3]: Tscharntke et al. 2007, para. 2. [Evidence](../../../sources/notes/tscharntke2007author.md#e3)
[^tscharntke2007author-e4]: Tscharntke et al. 2007, para. 3. [Evidence](../../../sources/notes/tscharntke2007author.md#e4)
[^schnell2015ten-e1]: Schnell 2015, Introduction. [Evidence](../../../sources/notes/schnell2015ten.md#e1)
[^schnell2015ten-e2]: Schnell 2015, Rule 1. [Evidence](../../../sources/notes/schnell2015ten.md#e2)
[^schnell2015ten-e3]: Schnell 2015, Rule 4. [Evidence](../../../sources/notes/schnell2015ten.md#e3)
[^schnell2015ten-e4]: Schnell 2015, Rule 5. [Evidence](../../../sources/notes/schnell2015ten.md#e4)
[^schnell2015ten-e5]: Schnell 2015, Rule 8. [Evidence](../../../sources/notes/schnell2015ten.md#e5)
[^schnell2015ten-e6]: Schnell 2015, Rule 8. [Evidence](../../../sources/notes/schnell2015ten.md#e6)
[^schnell2015ten-e7]: Schnell 2015, Rule 6. [Evidence](../../../sources/notes/schnell2015ten.md#e7)
[^schnell2015ten-e8]: Schnell 2015, Introduction. [Evidence](../../../sources/notes/schnell2015ten.md#e8)
[^schnell2015ten-e9]: Schnell 2015, Rule 3. [Evidence](../../../sources/notes/schnell2015ten.md#e9)
[^errington2021challenges-e1]: Errington et al. 2021 (eLife e67995), Abstract. [Evidence](../../../sources/notes/errington2021challenges.md#e1)
[^errington2021challenges-e2]: Errington et al. 2021 (eLife e67995), Abstract. [Evidence](../../../sources/notes/errington2021challenges.md#e2)
[^errington2021challenges-e3]: Errington et al. 2021 (eLife e67995), Challenges during experiments and peer review. [Evidence](../../../sources/notes/errington2021challenges.md#e3)
[^errington2021challenges-e4]: Errington et al. 2021 (eLife e67995), The duration of the different phases in the project. [Evidence](../../../sources/notes/errington2021challenges.md#e4)
[^errington2021challenges-e5]: Errington et al. 2021 (eLife e67995), Independent development of replication protocols. [Evidence](../../../sources/notes/errington2021challenges.md#e5)
[^errington2021challenges-e6]: Errington et al. 2021 (eLife e67995), Abstract. [Evidence](../../../sources/notes/errington2021challenges.md#e6)
[^errington2021investigating-e1]: Errington et al. 2021 (eLife e71601), Abstract. [Evidence](../../../sources/notes/errington2021investigating.md#e1)
[^errington2021investigating-e2]: Errington et al. 2021 (eLife e71601), Abstract. [Evidence](../../../sources/notes/errington2021investigating.md#e2)
[^errington2021investigating-e3]: Errington et al. 2021 (eLife e71601), Abstract. [Evidence](../../../sources/notes/errington2021investigating.md#e3)
[^biorxivabout-e1]: bioRxiv, About bioRxiv. [Evidence](../../../sources/notes/biorxivabout.md#e1)
[^biorxivabout-e2]: bioRxiv, About bioRxiv. [Evidence](../../../sources/notes/biorxivabout.md#e2)
[^biorxivabout-e3]: bioRxiv, About bioRxiv. [Evidence](../../../sources/notes/biorxivabout.md#e3)
[^biorxivabout-e4]: bioRxiv, About bioRxiv. [Evidence](../../../sources/notes/biorxivabout.md#e4)
[^biorxivabout-e5]: bioRxiv, Journal Preprint Policies. [Evidence](../../../sources/notes/biorxivabout.md#e5)
[^biorxivabout-e6]: bioRxiv, About bioRxiv. [Evidence](../../../sources/notes/biorxivabout.md#e6)
[^icmje2026recommendations-e28]: ICMJE 2026, II.A.2 Who Is an Author? [Evidence](../../../sources/notes/icmje2026recommendations.md#e28)
[^perciedusert2020arrive-e1]: Percie du Sert et al. 2020 (ARRIVE 2.0), Abstract. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e1)
[^perciedusert2020arrive-e2]: Percie du Sert et al. 2020 (ARRIVE 2.0), Abstract. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e2)
[^perciedusert2020arrive-e3]: Percie du Sert et al. 2020 (ARRIVE 2.0), Introducing ARRIVE 2.0. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e3)
[^perciedusert2020arrive-e4]: Percie du Sert et al. 2020 (ARRIVE 2.0), Why good reporting is important. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e4)
[^perciedusert2020arrive-e5]: Percie du Sert et al. 2020 (ARRIVE 2.0), Why good reporting is important. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e5)
[^perciedusert2020arrive-e6]: Percie du Sert et al. 2020 (ARRIVE 2.0), Why good reporting is important. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e6)
[^perciedusert2020arrive-e7]: Percie du Sert et al. 2020 (ARRIVE 2.0), Introducing ARRIVE 2.0. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e7)
[^perciedusert2020arrive-e8]: Percie du Sert et al. 2020 (ARRIVE 2.0), Why good reporting is important. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e8)
[^perciedusert2020arrive-e9]: Percie du Sert et al. 2020 (ARRIVE 2.0), Introducing ARRIVE 2.0. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e9)
[^perciedusert2020reporting-e1]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1a. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e1)
[^perciedusert2020reporting-e2]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1a. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e2)
[^perciedusert2020reporting-e3]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Glossary. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e3)
[^perciedusert2020reporting-e4]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1b. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e4)
[^perciedusert2020reporting-e5]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1b. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e5)
[^perciedusert2020reporting-e6]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1b. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e6)
[^perciedusert2020reporting-e7]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 4. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e7)
[^perciedusert2020reporting-e8]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 5. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e8)
[^perciedusert2020reporting-e9]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1a. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e9)
[^perciedusert2020reporting-e10]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1b. [Evidence](../../../sources/notes/perciedusert2020reporting.md#e10)
[^vaux2012replicates-e1]: Vaux et al. 2012, Introduction. [Evidence](../../../sources/notes/vaux2012replicates.md#e1)
[^vaux2012replicates-e2]: Vaux et al. 2012, the bone marrow colony assay example. [Evidence](../../../sources/notes/vaux2012replicates.md#e2)
[^vaux2012replicates-e4]: Vaux et al. 2012, Why bother with replicates at all? [Evidence](../../../sources/notes/vaux2012replicates.md#e4)
[^vaux2012replicates-e5]: Vaux et al. 2012, the qRT-PCR example. [Evidence](../../../sources/notes/vaux2012replicates.md#e5)
[^vaux2012replicates-e6]: Vaux et al. 2012, Sidebar A. [Evidence](../../../sources/notes/vaux2012replicates.md#e6)
[^vaux2012replicates-e7]: Vaux et al. 2012, So, what is wrong? [Evidence](../../../sources/notes/vaux2012replicates.md#e7)
[^vaux2012replicates-e8]: Vaux et al. 2012, Sidebar A. [Evidence](../../../sources/notes/vaux2012replicates.md#e8)
[^freedman2015economics-e1]: Freedman et al. 2015, main text. [Evidence](../../../sources/notes/freedman2015economics.md#e1)
[^freedman2015economics-e2]: Freedman et al. 2015, main text, cell line example. [Evidence](../../../sources/notes/freedman2015economics.md#e2)
[^freedman2015economics-e3]: Freedman et al. 2015, main text, cell line example. [Evidence](../../../sources/notes/freedman2015economics.md#e3)
[^freedman2015economics-e4]: Freedman et al. 2015, Abstract and main text. [Evidence](../../../sources/notes/freedman2015economics.md#e4)
[^nihrigorguidance-e2]: NIH, Rigor and Reproducibility application guidance. [Evidence](../../../sources/notes/nihrigorguidance.md#e2)
[^nihrigorguidance-e3]: NIH, Consideration of relevant biological variables. [Evidence](../../../sources/notes/nihrigorguidance.md#e3)
[^nihrigorguidance-e4]: NIH, Authentication of key biological and/or chemical resources. [Evidence](../../../sources/notes/nihrigorguidance.md#e4)
[^nc3rsthe3rs-e1]: NC3Rs, What are the 3Rs? [Evidence](../../../sources/notes/nc3rsthe3rs.md#e1)
[^nc3rsthe3rs-e2]: NC3Rs, Definitions of the 3Rs. [Evidence](../../../sources/notes/nc3rsthe3rs.md#e2)
[^nc3rsthe3rs-e3]: NC3Rs, Definitions of the 3Rs. [Evidence](../../../sources/notes/nc3rsthe3rs.md#e3)
[^nc3rsthe3rs-e4]: NC3Rs, Replacement. [Evidence](../../../sources/notes/nc3rsthe3rs.md#e4)
[^plosdatapolicy-e1]: PLOS data policy, Introduction. [Evidence](../../../sources/notes/plosdatapolicy.md#e1)
[^plosdatapolicy-e2]: PLOS data policy, data repositories. [Evidence](../../../sources/notes/plosdatapolicy.md#e2)
[^plosdatapolicy-e3]: PLOS data policy, data repositories. [Evidence](../../../sources/notes/plosdatapolicy.md#e3)
[^plosdatapolicy-e4]: PLOS data policy, Minimal data set. [Evidence](../../../sources/notes/plosdatapolicy.md#e4)
[^plosdatapolicy-e5]: PLOS data policy, Minimal data set. [Evidence](../../../sources/notes/plosdatapolicy.md#e5)
[^plosdatapolicy-e6]: PLOS data policy, Minimal data set. [Evidence](../../../sources/notes/plosdatapolicy.md#e6)
[^tscharntke2007author-e5]: Tscharntke et al. 2007, para. 3. [Evidence](../../../sources/notes/tscharntke2007author.md#e5)
[^vaux2012replicates-e3]: Vaux et al. 2012, Sidebar A. [Evidence](../../../sources/notes/vaux2012replicates.md#e3)
[^freedman2015economics-e5]: Freedman et al. 2015, solutions section. [Evidence](../../../sources/notes/freedman2015economics.md#e5)
[^nihrigorguidance-e1]: NIH, Rigorous experimental design for robust and unbiased results. [Evidence](../../../sources/notes/nihrigorguidance.md#e1)
[^nihrigorguidance-e5]: NIH, Consideration of relevant biological variables. [Evidence](../../../sources/notes/nihrigorguidance.md#e5)
[^fgedmiame-e1]: FGED, MIAME page, top of page. [Evidence](../../../sources/notes/fgedmiame.md#e1)
[^fgedmiame-e2]: FGED, MIAME page, six key elements. [Evidence](../../../sources/notes/fgedmiame.md#e2)
[^fgedmiame-e3]: FGED, MIAME page, top of page. [Evidence](../../../sources/notes/fgedmiame.md#e3)
[^fgedminseqe-e1]: FGED, MINSEQE page, top of page. [Evidence](../../../sources/notes/fgedminseqe.md#e1)
[^fgedminseqe-e2]: FGED, MINSEQE page, five elements. [Evidence](../../../sources/notes/fgedminseqe.md#e2)
[^fgedminseqe-e3]: FGED, MINSEQE page, MINSEQE specification. [Evidence](../../../sources/notes/fgedminseqe.md#e3)
[^odea2021preferred-e1]: O'Dea et al. 2021 (PRISMA-EcoEvo), Abstract. [Evidence](../../../sources/notes/odea2021preferred.md#e1)
[^odea2021preferred-e2]: O'Dea et al. 2021 (PRISMA-EcoEvo), Abstract. [Evidence](../../../sources/notes/odea2021preferred.md#e2)
[^odea2021preferred-e3]: O'Dea et al. 2021 (PRISMA-EcoEvo), Abstract. [Evidence](../../../sources/notes/odea2021preferred.md#e3)
[^odea2021preferred-e4]: O'Dea et al. 2021 (PRISMA-EcoEvo), Abstract. [Evidence](../../../sources/notes/odea2021preferred.md#e4)
[^odea2021preferred-e5]: O'Dea et al. 2021 (PRISMA-EcoEvo), Abstract. [Evidence](../../../sources/notes/odea2021preferred.md#e5)
[^page2021prisma-e17]: Page et al. 2021 (PRISMA 2020), Scope of the guideline. [Evidence](../../../sources/notes/page2021prisma.md#e17)
[^odea2021preferred-e6]: O'Dea et al. 2021 (PRISMA-EcoEvo), Table 1, Item 3.1. [Evidence](../../../sources/notes/odea2021preferred.md#e6)
[^hooijmans2014syrcle-e1]: Hooijmans et al. 2014, Abstract. [Evidence](../../../sources/notes/hooijmans2014syrcle.md#e1)
[^naturemethodsaims-e1]: Nature Methods, Aims & Scope. [Evidence](../../../sources/notes/naturemethodsaims.md#e1)
[^naturemethodsaims-e2]: Nature Methods, Aims & Scope. [Evidence](../../../sources/notes/naturemethodsaims.md#e2)
[^ploscompbiolsubmission-e1]: PLOS Computational Biology submission guidelines, Software Submissions. [Evidence](../../../sources/notes/ploscompbiolsubmission.md#e1)
[^ploscompbiolsubmission-e2]: PLOS Computational Biology submission guidelines, Software Submissions. [Evidence](../../../sources/notes/ploscompbiolsubmission.md#e2)
[^hooijmans2014syrcle-e2]: Hooijmans et al. 2014, Abstract. [Evidence](../../../sources/notes/hooijmans2014syrcle.md#e2)
[^hooijmans2014syrcle-e3]: Hooijmans et al. 2014, Abstract. [Evidence](../../../sources/notes/hooijmans2014syrcle.md#e3)
[^hooijmans2014syrcle-e4]: Hooijmans et al. 2014, Background. [Evidence](../../../sources/notes/hooijmans2014syrcle.md#e4)
