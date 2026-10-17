# Animal and veterinary science: field overview

This page covers two fields from the classification of fields of science used by the Organisation for Economic Co-operation and Development (OECD): **4.2 Animal and dairy science** and **4.3 Veterinary science** (for the classification, see the [Fields overview](../README.md)). Roughly, the first studies the nutrition, genetics and breeding, reproduction, welfare, and production of livestock and poultry; the second studies the diagnosis, treatment, and prevention of animal disease. The two share many conventions: the subjects are animals, the animals' owners are often a party to the study, and the animals are often kept in groups `[Our analysis]`. This page is about those shared features and about what is special to each.

For animal experiments with laboratory mice and rats, see the [Biological sciences page](../biological-sciences/README.md); for clinical research on humans, see the [Clinical medicine page](../clinical-medicine/README.md); for practices common to every field, see the Parts listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). This page only covers what is specific to this field. For which research strategies the field uses and what evidence each one needs, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

**After reading this page, you should be able to:**

- explain where farm-animal research and veterinary clinical research are done, and which approvals each needs;
- explain why you need the owner's informed consent when you study someone else's animals, and what the consent form must cover;
- tell whether "one animal" or "one pen of animals" is your experimental unit, and what goes wrong if you get it wrong;
- pick the reporting guideline (the checklist of items you must report when you write the paper) that fits your study design: REFLECT (Reporting Guidelines for Randomized Controlled Trials for livestock and food safety) for livestock trials, STROBE-Vet (the veterinary extension of STROBE, Strengthening the Reporting of Observational Studies in Epidemiology) for veterinary observational studies, and ARRIVE (Animal Research: Reporting of In Vivo Experiments) for experiments on live animals.

---

## How research works in this field

### Three common research settings

Research in this field happens in roughly three kinds of places `[Our analysis]`:

1. **Research farms and animal facilities**: cattle, pigs, sheep, chickens, and other animals kept by a university or research institute for studies of nutrition, genetics, reproduction, welfare, and disease `[Our analysis]`. The authors of REFLECT say that livestock trials with production, health, and food-safety outcomes are often run in research settings where the researcher controls a deliberate infection of the animals with a pathogen; this is called a **challenge trial**[^oconnor2010reflect-e8]. The US Ag Guide (the guide for agricultural animals, see below) requires that research involving pathogens with high morbidity and mortality (such as tuberculosis or foot-and-mouth disease) be done in biocontainment facilities[^fass2020agguide-e12].
2. **Commercial farms**: field trials or observational studies on working farms `[Our analysis]`. Here the farm owner or manager has to agree to take part; they are a party to the study[^oconnor2010reflect-e3].
3. **Veterinary practices and animal hospitals**: clinical studies that enroll pets (dogs, cats, horses, and so on) brought in by their owners for care, much like human clinical trials. These are not the same as research animals owned by an institution[^bertout2021recommendations-e2].

### Studying animals also serves human health

This field is closely tied to human health:

- **One Health.** The World Health Organization (WHO) defines it as treating the health of people, animals, plants, and ecosystems together rather than separately[^who2026onehealth-e1]. The WHO fact sheet says that more than 60% of emerging infectious diseases reported worldwide come from wild or domestic animals[^who2026onehealth-e2]. Zoonoses (infectious diseases that pass between animals and people, such as avian influenza and rabies)[^who2026onehealth-e3] and food safety are where veterinary and human medical research meet `[Our analysis]`.
- **Comparative medicine.** Companion animals naturally develop many diseases similar to human ones, so studies on pets can advance both human and veterinary medicine[^bertout2021recommendations-e3]. For example, clinical trials in companion animals with naturally occurring cancer have been run for more than 50 years, with the aim of improving both animal and human health[^page2016conduct-e11]. (Companion animals are pets that live with people, such as dogs, cats, and horses[^bertout2021recommendations-e2].)

What this means for you: your study may have several audiences at once (the livestock industry, veterinarians, public health), so decide who your main readers are before you write the paper `[Our analysis]`.

### Publishing: mostly journals, with reporting guidelines co-published across several

Research in this field is mainly published in journals `[Our analysis]`. One example: the REFLECT statement (the reporting guideline for livestock trials, see below) was published simultaneously in five journals, covering veterinary internal medicine, preventive veterinary medicine, food protection, zoonoses and public health, and swine health and production[^oconnor2010reflect-e14]. The range of those five journals gives a rough idea of the audiences this field's work reaches `[Our analysis]`.

The next two points come from a short review by Bertout et al. 2021 on ethics review of veterinary clinical research in the US. Keep in mind as you read it that the first author co-owns a company that provides services, including ethics review, for veterinary clinical studies funded by pharmaceutical or biotechnology companies[^bertout2021recommendations-e9], and the review is about how ethics review should be done `[Our analysis]`.

- **Without ethics review, you may not get published.** The review says many journals require authors to state that the study was approved by an ethics committee before it began; original papers by veterinarians in private practice may be rejected if there was no ethics review[^bertout2021recommendations-e7].
- **Specialty board certification needs papers (US).** The review says that veterinarians doing residency training in private practice in the US often apply for specialty board certification, and these specialty boards generally require a first-author paper[^bertout2021recommendations-e8]. This is the US situation; in other countries, follow the rules of the local specialty organization `[Our analysis]`.

Our sources do not cover authorship-order conventions or review timelines in this field; follow your advisor and the target journal.

---

## How this field differs from others

The table below is our own summary, meant to help you spot the differences quickly; the footnotes in the main text support the animal and veterinary science column `[Our analysis]`.

| | Animal and veterinary science | Biological sciences (laboratory animals) | Clinical medicine | Computer science |
|---|---|---|---|---|
| Who or what is studied | Livestock, poultry, pets, wildlife, often kept in groups | Mice, rats, and so on, housed in cages | People | Systems, data, sometimes people |
| Who consents | The animal owner or farm manager | No one (the institution owns the animals) | The participant | The participant |
| Ethics review | Animal welfare review; for client-owned animals, owner consent as well | Animal welfare review | Ethics committee review | Review when people take part |
| Experimental unit | Often a pen, a herd or flock, or a farm | Often one animal, sometimes one cage | Usually one person, except in cluster trials | Usually a task, a dataset, or a participant |
| Reporting guidelines | REFLECT, STROBE-Vet, ARRIVE | ARRIVE | CONSORT (Consolidated Standards of Reporting Trials), STROBE, and others | Each conference's checklist |
| Outcomes | Disease, and also production measures such as weight gain and milk yield | Biological measures | Clinical outcomes | Performance, accuracy, and so on |

The two biggest differences: there are **two kinds of "participants"** (the owner or manager who agrees to take part, and the animals actually being studied); and **animals are often kept in groups, so observations are not independent**. The authors of REFLECT list four ways livestock trials differ from human trials: two kinds of participants, frequent use of clustered designs (running the trial with a group of animals as the unit), deliberate infection of animals with pathogens in some trials, and outcomes that are often non-clinical, such as production indices. They argue that this makes it hard to apply CONSORT, the reporting guideline for human trials, directly[^oconnor2010reflect-e3].

---

## Norms and reporting standards in this field

### Animal welfare review: farm animals have their own guide

The general principles of animal research (the 3Rs: Replacement, Reduction, Refinement[^nc3rsthe3rs-e2]) and the logic of approval (a "harm–benefit analysis"[^perciedusert2020arrive-e6]) are covered on the [Biological sciences page](../biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines) and are not repeated here. The 3Rs are written into national and international laws and regulations on the use of animals in research[^nc3rsthe3rs-e1].

What sets farm animals apart is that their housing, breeds, and climate conditions are very different from those of laboratory mice `[Our analysis]`. In the US, the American Dairy Science Association (ADSA), the American Society of Animal Science (ASAS), and the Poultry Science Association (PSA) jointly publish the *Guide for the Care and Use of Agricultural Animals in Research and Teaching* (known as the Ag Guide; 4th edition, 2020)[^fass2020agguide-e1]. Its first 5 chapters are general rules for all agricultural animals, and the remaining 8 chapters are species-specific[^fass2020agguide-e15]. Its main points are below. The guide is built around the US review system; in other countries, follow local regulations and your institution's rules `[Our analysis]`:

- **Get approval before you start.** Animal use protocols must be reviewed before the research begins[^fass2020agguide-e8]. The review is done by the Institutional Animal Care and Use Committee (IACUC, the committee that oversees animal use at an institution)[^fass2020agguide-e6]. The committee must include a scientist with experience in agricultural animal research or teaching and a licensed veterinarian trained in agricultural animal medicine[^fass2020agguide-e7].
- **Justify the protocol.** Why this species and strain, why this many animals, and which procedures may cause discomfort, distress, or pain[^fass2020agguide-e10].
- **Consider alternatives, but production research is an exception.** Reviewers should consider alternatives such as cell culture and computer simulation; but the guide also notes that hands-on work with animals is an important part of agricultural research and teaching, and that production research has no substitute in other animals or simulations[^fass2020agguide-e9].
- **Tell "must", "should", and "recommend" apart.** In the guide, *must* means it is required; *should* means you comply unless you have a valid reason not to; *recommend* means it is one suitable practice and others are allowed[^fass2020agguide-e2].
- **Look at welfare outcomes, not just the wording.** Many of the floor-space, feeder, and waterer standards in the species chapters have been validated by scientific research[^fass2020agguide-e4]; but the guide asks reviewers to use professional judgment and aim for actual welfare outcomes rather than apply the text mechanically[^fass2020agguide-e3].
- **Euthanasia follows the American Veterinary Medical Association (AVMA) guidelines.** Use methods listed as "acceptable" or "acceptable with conditions" in the AVMA *Guidelines for the Euthanasia of Animals*, and state how death will be confirmed[^fass2020agguide-e11].

On regulations, Chapter 1 of the Ag Guide lists the laws that apply in the US and in Europe[^fass2020agguide-e5]: in the US, the Animal Welfare Act and Title 9 Part 1A of the Code of Federal Regulations; in Europe, the Council of Europe's European Convention for the Protection of Vertebrate Animals used for Experimental and Other Scientific Purposes, followed later by EU Directive 2010/63/EU. Researchers in the EU follow that directive and their national law; the Ag Guide is only a US guide; researchers in other countries follow their own national rules. To find out which rules apply to your study, ask your institution's animal ethics committee first `[Our analysis]`.

### Research on client-owned animals: owner informed consent

Veterinary clinical studies enroll pets brought to the clinic by their owners, not animals owned by a research institution[^bertout2021recommendations-e2]. This raises a set of ethical questions different from those of both laboratory animal research and human research[^page2016conduct-e1]: the norms for laboratory animals are well developed, but many of them cannot be applied directly to client-owned animals[^page2016conduct-e2].

The points below all describe the US. The Bertout et al. 2021 review mentioned above (keep in mind the author's conflict of interest noted earlier) says that laws covering clinical studies with client-owned animals are scant[^bertout2021recommendations-e4], and that neither the Animal Welfare Act nor IACUC review covers key parts of clinical research such as informed consent[^bertout2021recommendations-e5]. The review also notes that AVMA policy provides for a Veterinary Clinical Studies Committee, which should ensure that informed consent is obtained from owners and that enrolled animals are protected from conflicts of interest[^bertout2021recommendations-e10]. Owner consent differs from consent in human research in one key way: the owner gives consent, whereas in human research it is the participant or the parent of a child patient[^bertout2021recommendations-e6].

For how to handle consent in practice, see the consensus report by Page et al. 2016. It came out of a multi-stakeholder workshop held in November 2014 at AVMA headquarters in Washington, DC, and sets out "best practice recommendations" for veterinary oncology clinical trials[^page2016conduct-e14]; it covers only companion animals with cancer[^page2016conduct-e1]. It is the consensus of one US workshop, not a regulation; other areas and other countries can use it as a reference but should follow local rules `[Our analysis]`. Its main points on owner informed consent are:

- **Explain everything.** The consent process must cover the study's purpose, risks and benefits, design and interventions, funding sources, any financial incentives for owners, and the researchers' conflicts of interest[^page2016conduct-e4]. Write the consent form in plain, easy-to-understand language[^page2016conduct-e12].
- **No pressure.** Owners must have enough time to decide, free from coercion or conflicts of interest from anyone on the study team[^page2016conduct-e3]. The report recommends that a neutral person (a nurse, or a veterinarian not supported by the sponsor) lead the consent process, with a witness present[^page2016conduct-e4].
- **Be fully clear about money.** All financial incentives must be explained, and what is *not* covered matters just as much[^page2016conduct-e5]. Reimbursing care costs only if the owner completes the study puts owners in a financially vulnerable position[^page2016conduct-e6].
- **Take good care of every animal.** All enrolled animals, whether or not the trial has a control group, must receive best supportive care (treatment that relieves symptoms and maintains quality of life)[^page2016conduct-e7].
- **Someone should also review the scientific merit.** Trials funded by companies, donors, or hospitals may go through IACUC review only, and the IACUC's remit does not necessarily include judging scientific merit[^page2016conduct-e9]. Some institutions have set up clinical review committees to assess the merit, feasibility, and ethical compliance of such trials[^page2016conduct-e13].

To compare with informed consent in human research, see the [Clinical medicine page](../clinical-medicine/README.md#your-subjects-are-people-so-ethics-comes-first).

### Experimental unit: one animal, or one pen?

This is where newcomers to the field most often go wrong `[Our analysis]`. The **experimental unit** is the thing that independently receives a treatment; for the general definition and how to count n, see the [Biological sciences page](../biological-sciences/README.md#identify-the-experimental-unit-before-you-count-n). What is special in this field:

- **Animals kept in groups give observations that are not independent.** Livestock are often housed and managed in groups; animals in the same pen share a microclimate, diet, and health management, so they are more alike[^oconnor2010reflect-e5]. Both livestock and companion animals in shelters are often housed or managed in groups[^sargeant2016strobevet-e7].
- **Levels nest inside levels.** Pigs, for example, are organized by pen, barn, site, and production company[^oconnor2010reflect-e7]. But the structure is not always a neat hierarchy, and repeated sampling of the same animal or facility also creates non-independence[^sargeant2016strobevet-e8].
- **The unit of allocation and the unit of measurement can differ.** An intervention can be allocated at any level, and the outcome measured at the same level or a lower one[^oconnor2010reflect-e4]. For example, treatment may be allocated to half an udder while the outcome is measured on individual teats[^oconnor2010reflect-e9].
- **What goes wrong if you get it wrong.** If the statistical analysis ignores this non-independence, it violates the independence assumption that many statistical methods rely on[^oconnor2010reflect-e6]. You have to deal with it in the design, the sampling, and the analysis[^sargeant2016strobevet-e7].

In practice: before you design the study, draw the animal–pen–barn–farm structure, mark the level where treatment is allocated and the level where the outcome is measured, and then ask a statistician to confirm the analysis method `[Our analysis]`.

### Reporting guidelines: choose by study design

| Study design | Reporting guideline | Notes |
|---|---|---|
| Randomized controlled trials in livestock (with production, health, or food-safety outcomes) | REFLECT | A 22-item checklist; 14 items are adapted from CONSORT, the guideline for human trials, plus one extra sub-item for challenge trials[^oconnor2010reflect-e2] |
| Veterinary observational studies (health, production, welfare, food safety) | STROBE-Vet | The veterinary extension of STROBE[^sargeant2016strobevet-e1]; meant to be used together with its explanation document[^sargeant2016strobevet-e11] |
| Experiments on live animals (in a laboratory or other formal experimental setting) | ARRIVE | Applies to all research using live animals[^perciedusert2020arrive-e8]; see the [Biological sciences page](../biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines) |
| Studies of how animal exposures affect human health | The original STROBE | Outside the scope of STROBE-Vet[^sargeant2016strobevet-e4]; for reporting guidelines for human research, see the [Clinical medicine page](../clinical-medicine/README.md#reporting-guidelines-pick-the-checklist-for-your-study-type) |

Compared with their human-research versions, these guidelines mainly add the following `[Our analysis]`:

- **Report both kinds of participants.** The animal owners or managers, and the animals themselves[^sargeant2016strobevet-e6]. In REFLECT, "participant" refers only to the owners or managers who consent to take part, and animals and other units are called "study units"[^oconnor2010reflect-e15]; you report eligibility criteria for both[^oconnor2010reflect-e16].
- **Describe the organizational structure.** At which level the treatment was allocated, at which level the outcome was measured, and how the analysis handles non-independence[^oconnor2010reflect-e4].
- **Report challenge trials separately.** REFLECT adds a sub-item specifically for challenge trials[^oconnor2010reflect-e2]. One reason: the challenge conditions affect whether the conclusions generalize. For example, a challenge study that used 100 times the normal dose of *Salmonella* has questionable relevance to real-world conditions[^oconnor2010reflect-e10].
- **Report transparency information.** STROBE-Vet asks for funding sources, conflicts of interest, author contributions, ethics approval, and the quality standards followed[^sargeant2016strobevet-e10].

Why these guidelines exist: poor reporting of veterinary randomized trials was raised in editorials and commentaries in veterinary journals in the early to mid-1990s, and shortly before REFLECT was published (2010), several systematic reviews of livestock trials on treatment, prevention, and food safety again pointed out that reporting needed to improve[^oconnor2010reflect-e12]. The REFLECT authors also say the statement can be used as a reference at the design and conduct stages[^oconnor2010reflect-e11].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table lists only the three strategies our sources support. The grouping and the "What it looks like in this field" column are our own summary, and each standard represents only the source cited in its footnote `[Our analysis]`. Our sources do not cover the standards of evidence for other strategies such as Measurement or Building and improving.

| Strategy | What it looks like in this field | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Feeding and nutrition trials: randomly assign animals or pens to different diets or treatments; challenge trials: deliberately infect animals with a pathogen in a research facility to test an intervention[^oconnor2010reflect-e8]; veterinary clinical trials: enroll owners' pets, much like human clinical trials[^bertout2021recommendations-e2] | Report livestock trials using REFLECT[^oconnor2010reflect-e2]; state at which level treatment was allocated and at which level the outcome was measured[^oconnor2010reflect-e4], and handle the non-independence of animals in the same pen in the analysis[^oconnor2010reflect-e6]; consider whether challenge conditions generalize to the real world[^oconnor2010reflect-e10] | [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), [Preclinical animal studies](../../06_methods/preclinical_animal_study.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Veterinary epidemiology: estimating prevalence or incidence and its distribution in time and space, and also identifying risk factors and evaluating diagnostic tests[^sargeant2016strobevet-e2]; many studies do not fit neatly into the three classic designs (cohort, case-control, cross-sectional)[^sargeant2016strobevet-e5] | Report using STROBE-Vet[^sargeant2016strobevet-e1]; describe both kinds of participants, owners or managers and animals[^sargeant2016strobevet-e6]; deal with the non-independence caused by group housing in the design, sampling, and analysis[^sargeant2016strobevet-e7]; when testing hypotheses, state the assumed causal structure, and drawing a causal diagram is strongly encouraged[^sargeant2016strobevet-e9] | [Observational epidemiology](../../06_methods/observational_epidemiology.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Veterinary systematic reviews: pooling existing studies to answer one of four kinds of question: descriptive (such as the prevalence of a disease), intervention, exposure or etiology, or diagnostic test accuracy[^sargeant2020scoping-e3] | This row comes from a 2020 methods review by researchers at two veterinary colleges, one in Canada and one in the US; it is not a society rule `[Our analysis]`. As in general practice: write a protocol in advance[^sargeant2020scoping-e1], have two people independently screen studies and extract data[^sargeant2020scoping-e5][^sargeant2020scoping-e6], and report using PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)[^sargeant2020scoping-e9]; for details, see the meta-analysis page. Three things need extra attention in veterinary science: besides PROSPERO (the international prospective register of systematic reviews), protocols can also be posted on the SYREAF (Systematic Reviews for Animals and Food) website[^sargeant2020scoping-e2]; veterinary science lacks the search filters that human medicine has, so search several databases[^sargeant2020scoping-e4]; one study found that fewer than 10% of conference abstracts on swine and cattle vaccine trials were later published in full, so consider publication bias[^sargeant2020scoping-e8]. Studies at high risk of bias are not excluded unless that was written into the inclusion criteria in advance[^sargeant2020scoping-e7] | [Systematic review and meta-analysis](../../06_methods/meta_analysis.md), [Review studies](../../06_methods/review_study.md) |

How to use this table `[Our analysis]`: the shared difficulty of Causal explanation and Description is the experimental unit. Whether you run a trial or an observational study, first draw the animal–pen–barn–farm structure as described [above](#experimental-unit-one-animal-or-one-pen), then decide on sample size and analysis.

## Research methods common in this field

Cross-field research types: [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), [Preclinical animal studies](../../06_methods/preclinical_animal_study.md), [Observational epidemiology](../../06_methods/observational_epidemiology.md), [Controlled experiments](../../06_methods/controlled_experiment.md), and [Review studies](../../06_methods/review_study.md); for trials on farms, see [Field trials](../agriculture/practices/field_trial.md) on the Agriculture page. The field also commonly uses the following, which do not yet have their own how-to pages:

- **Genetics and breeding research**: selection, genomic analysis, and also genetic engineering and gene editing `[Our analysis]`. The Ag Guide holds that, except in special cases, the guidelines for research on genetically engineered and gene-edited animals do not differ substantially from those for conventional animals[^fass2020agguide-e14].
- **Animal welfare and behavior research**: studying how space allowance, environmental enrichment (adding toys, bedding, and so on to pens so animals can express natural behavior), and handling affect animals `[Our analysis]`. Many of the floor-space, feeder, and waterer standards in the Ag Guide's species chapters have been validated by scientific research[^fass2020agguide-e4].

---

## Advice for newcomers

1. **First find out who owns your animals.** Institutional animals, animals on a collaborating farm, and clients' pets each come with different approval and consent requirements[^bertout2021recommendations-e2][^oconnor2010reflect-e3]. Check with your institution's animal ethics committee before you start `[Our analysis]`.
2. **Draw the organizational structure at the design stage.** Which levels are animal, pen, barn, and farm, and at which level the treatment is allocated[^oconnor2010reflect-e4]. Count n by experimental unit, not by number of animals `[Our analysis]`; for the reasoning, see the [Biological sciences page](../biological-sciences/README.md#identify-the-experimental-unit-before-you-count-n).
3. **Open the reporting guideline at the design stage.** REFLECT can also be used at the design and conduct stages[^oconnor2010reflect-e11]; STROBE-Vet is meant to be read together with its explanation document[^sargeant2016strobevet-e11].
4. **For an observational study, draw a causal diagram first.** STROBE-Vet asks studies that test hypotheses to state the assumed causal structure and strongly encourages drawing a causal diagram[^sargeant2016strobevet-e9].
5. **Be honest with owners, give them time, and be clear about money.** Prepare the consent form following the informed-consent points above[^page2016conduct-e3][^page2016conduct-e5].
6. **Watch how euthanasia affects your outcomes.** The Page et al. consensus report notes that in clinical trials in animals, euthanasia confounds the assessment of overall survival; elective euthanasia, carried out at the owner's request while the animal is clinically stable and self-supportive, must be considered carefully when analyzing outcome data[^page2016conduct-e8].
7. **Publish all results.** The same consensus report on companion-animal cancer trials recommends publishing the results of every trial, to support reproducibility and avoid duplication[^page2016conduct-e10]. For why negative results should be reported, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#2-be-honest-with-the-evidence-dont-fool-yourself-report-all-results) in Throughout the project.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Allocating treatment by pen but analyzing individual animals | Animals in the same pen are not independent, which violates the independence assumption of many statistical methods[^oconnor2010reflect-e6]; the conclusions may be false positives as a result `[Our analysis]` |
| Writing only "randomly allocated" in the paper, without saying at which level | A vaccine allocated to individual animals and one applied to a whole group may give different results[^oconnor2010reflect-e10]; if you don't say which, readers cannot judge whether the conclusions apply to their situation `[Our analysis]` |
| Reporting only on the animals, not the eligibility criteria for farms or owners | Both REFLECT and STROBE-Vet require information on both kinds of participants[^oconnor2010reflect-e16][^sargeant2016strobevet-e6] |
| Doing research on client-owned animals in the US and assuming IACUC approval is enough | IACUC review does not cover owner informed consent[^bertout2021recommendations-e5] and does not necessarily review scientific merit[^page2016conduct-e9] |
| Offering free treatment in exchange for enrolling an animal, and reimbursing care costs only if the owner completes the study | Trading incentives for the animal taking on risk is a potential ethical conflict; reimbursing only on completion puts owners in a financially vulnerable position[^page2016conduct-e6] |
| Using a challenge dose far above natural infection and then generalizing the conclusions to farms | Questionable external validity[^oconnor2010reflect-e10] |
| Applying laboratory animal rules to farm animals or client-owned animals | Many laboratory animal norms cannot be applied directly to client-owned animals[^page2016conduct-e2]; in the US, farm animal research has its own Ag Guide[^fass2020agguide-e1] |
| Using STROBE-Vet to report human outcomes in a zoonosis study | Human health outcomes should be reported using the original STROBE[^sargeant2016strobevet-e4] |

---

## Further reading

- **Ag Guide (4th edition, 2020)**: the guide to the care and use of agricultural animals, jointly published by the American Dairy Science Association, the American Society of Animal Science, and the Poultry Science Association. If you do livestock or poultry research in the US, start with Chapter 1 (institutional policies and protocol review) and the chapter for your species; elsewhere, use it as a reference and follow local rules.
- **REFLECT statement (O'Connor et al. 2010)**: the reporting guideline for randomized controlled trials in livestock. The passages on organizational structure and challenge trials are good material for understanding the experimental unit.
- **STROBE-Vet (Sargeant et al. 2016)**: the reporting guideline for veterinary observational studies, with an item-by-item explanation document.
- **Page et al. 2016**: a consensus report from a 2014 US workshop, covering only clinical trials in companion animals with cancer. Read it when you prepare an owner consent form.
- **Bertout et al. 2021**: a short review of gaps in ethics review of veterinary clinical research in the US. The first author co-owns a company that provides ethics review services; keep that in mind as you read.
- **The WHO One Health fact sheet**: to see how veterinary research connects with public health.
- **ARRIVE 2.0 and the 3Rs**: see the [Biological sciences page](../biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines).

[^bertout2021recommendations-e2]: Bertout et al. 2021, Introduction. [Evidence](../../../sources/notes/bertout2021recommendations.md#e2)
[^bertout2021recommendations-e3]: Bertout et al. 2021, Introduction. [Evidence](../../../sources/notes/bertout2021recommendations.md#e3)
[^bertout2021recommendations-e4]: Bertout et al. 2021, Differences in Laws and Regulations. [Evidence](../../../sources/notes/bertout2021recommendations.md#e4)
[^bertout2021recommendations-e5]: Bertout et al. 2021, Review. [Evidence](../../../sources/notes/bertout2021recommendations.md#e5)
[^bertout2021recommendations-e6]: Bertout et al. 2021, Review. [Evidence](../../../sources/notes/bertout2021recommendations.md#e6)
[^bertout2021recommendations-e7]: Bertout et al. 2021, Review. [Evidence](../../../sources/notes/bertout2021recommendations.md#e7)
[^bertout2021recommendations-e8]: Bertout et al. 2021, Review. [Evidence](../../../sources/notes/bertout2021recommendations.md#e8)
[^bertout2021recommendations-e9]: Bertout et al. 2021, Conflict of Interest. [Evidence](../../../sources/notes/bertout2021recommendations.md#e9)
[^bertout2021recommendations-e10]: Bertout et al. 2021, Veterinary Clinical Studies Committee. [Evidence](../../../sources/notes/bertout2021recommendations.md#e10)
[^fass2020agguide-e1]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Preface. [Evidence](../../../sources/notes/fass2020agguide.md#e1)
[^fass2020agguide-e2]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Preface. [Evidence](../../../sources/notes/fass2020agguide.md#e2)
[^fass2020agguide-e3]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Preface. [Evidence](../../../sources/notes/fass2020agguide.md#e3)
[^fass2020agguide-e4]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Preface. [Evidence](../../../sources/notes/fass2020agguide.md#e4)
[^fass2020agguide-e5]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1. [Evidence](../../../sources/notes/fass2020agguide.md#e5)
[^fass2020agguide-e6]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1, Monitoring. [Evidence](../../../sources/notes/fass2020agguide.md#e6)
[^fass2020agguide-e7]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1, Monitoring. [Evidence](../../../sources/notes/fass2020agguide.md#e7)
[^fass2020agguide-e8]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1, Protocol Review. [Evidence](../../../sources/notes/fass2020agguide.md#e8)
[^fass2020agguide-e9]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1, Protocol Review. [Evidence](../../../sources/notes/fass2020agguide.md#e9)
[^fass2020agguide-e10]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1, Protocol Review. [Evidence](../../../sources/notes/fass2020agguide.md#e10)
[^fass2020agguide-e11]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 2, Euthanasia. [Evidence](../../../sources/notes/fass2020agguide.md#e11)
[^fass2020agguide-e12]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 3. [Evidence](../../../sources/notes/fass2020agguide.md#e12)
[^fass2020agguide-e14]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Chapter 1, Special Considerations. [Evidence](../../../sources/notes/fass2020agguide.md#e14)
[^fass2020agguide-e15]: ADSA, ASAS, PSA 2020 (Ag Guide, 4th edition), Preface. [Evidence](../../../sources/notes/fass2020agguide.md#e15)
[^nc3rsthe3rs-e1]: NC3Rs, What are the 3Rs? [Evidence](../../../sources/notes/nc3rsthe3rs.md#e1)
[^nc3rsthe3rs-e2]: NC3Rs, Definitions of the 3Rs. [Evidence](../../../sources/notes/nc3rsthe3rs.md#e2)
[^oconnor2010reflect-e2]: O'Connor et al. 2010 (REFLECT), Abstract. [Evidence](../../../sources/notes/oconnor2010reflect.md#e2)
[^oconnor2010reflect-e3]: O'Connor et al. 2010 (REFLECT), Introduction. [Evidence](../../../sources/notes/oconnor2010reflect.md#e3)
[^oconnor2010reflect-e4]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e4)
[^oconnor2010reflect-e5]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e5)
[^oconnor2010reflect-e6]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e6)
[^oconnor2010reflect-e7]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e7)
[^oconnor2010reflect-e8]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e8)
[^oconnor2010reflect-e9]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e9)
[^oconnor2010reflect-e10]: O'Connor et al. 2010 (REFLECT), Discussion. [Evidence](../../../sources/notes/oconnor2010reflect.md#e10)
[^oconnor2010reflect-e11]: O'Connor et al. 2010 (REFLECT), Discussion. [Evidence](../../../sources/notes/oconnor2010reflect.md#e11)
[^oconnor2010reflect-e12]: O'Connor et al. 2010 (REFLECT), Introduction. [Evidence](../../../sources/notes/oconnor2010reflect.md#e12)
[^oconnor2010reflect-e14]: O'Connor et al. 2010 (REFLECT), first-page footnote. [Evidence](../../../sources/notes/oconnor2010reflect.md#e14)
[^oconnor2010reflect-e15]: O'Connor et al. 2010 (REFLECT), Results. [Evidence](../../../sources/notes/oconnor2010reflect.md#e15)
[^oconnor2010reflect-e16]: O'Connor et al. 2010 (REFLECT), Table 2, Item 3. [Evidence](../../../sources/notes/oconnor2010reflect.md#e16)
[^sargeant2020scoping-e1]: Sargeant & O'Connor 2020, Systematic Reviews. [Evidence](../../../sources/notes/sargeant2020scoping.md#e1)
[^sargeant2020scoping-e2]: Sargeant & O'Connor 2020, Systematic Reviews. [Evidence](../../../sources/notes/sargeant2020scoping.md#e2)
[^sargeant2020scoping-e3]: Sargeant & O'Connor 2020, Define the review question. [Evidence](../../../sources/notes/sargeant2020scoping.md#e3)
[^sargeant2020scoping-e4]: Sargeant & O'Connor 2020, Conduct a comprehensive search for studies. [Evidence](../../../sources/notes/sargeant2020scoping.md#e4)
[^sargeant2020scoping-e5]: Sargeant & O'Connor 2020, Selecting relevant studies. [Evidence](../../../sources/notes/sargeant2020scoping.md#e5)
[^sargeant2020scoping-e6]: Sargeant & O'Connor 2020, Collect data from relevant studies. [Evidence](../../../sources/notes/sargeant2020scoping.md#e6)
[^sargeant2020scoping-e7]: Sargeant & O'Connor 2020, Assess risk of bias in relevant studies. [Evidence](../../../sources/notes/sargeant2020scoping.md#e7)
[^sargeant2020scoping-e8]: Sargeant & O'Connor 2020, Synthesize the results. [Evidence](../../../sources/notes/sargeant2020scoping.md#e8)
[^sargeant2020scoping-e9]: Sargeant & O'Connor 2020, Present the results. [Evidence](../../../sources/notes/sargeant2020scoping.md#e9)
[^page2016conduct-e1]: Page et al. 2016, Introduction. [Evidence](../../../sources/notes/page2016conduct.md#e1)
[^page2016conduct-e2]: Page et al. 2016, Introduction. [Evidence](../../../sources/notes/page2016conduct.md#e2)
[^page2016conduct-e3]: Page et al. 2016, Table 1. [Evidence](../../../sources/notes/page2016conduct.md#e3)
[^page2016conduct-e4]: Page et al. 2016, Consenting Process. [Evidence](../../../sources/notes/page2016conduct.md#e4)
[^page2016conduct-e5]: Page et al. 2016, Consenting Process. [Evidence](../../../sources/notes/page2016conduct.md#e5)
[^page2016conduct-e6]: Page et al. 2016, Study Design. [Evidence](../../../sources/notes/page2016conduct.md#e6)
[^page2016conduct-e7]: Page et al. 2016, Study Design. [Evidence](../../../sources/notes/page2016conduct.md#e7)
[^page2016conduct-e8]: Page et al. 2016, Study Design. [Evidence](../../../sources/notes/page2016conduct.md#e8)
[^page2016conduct-e9]: Page et al. 2016, Study Design. [Evidence](../../../sources/notes/page2016conduct.md#e9)
[^page2016conduct-e10]: Page et al. 2016, Table 1. [Evidence](../../../sources/notes/page2016conduct.md#e10)
[^page2016conduct-e11]: Page et al. 2016, Introduction. [Evidence](../../../sources/notes/page2016conduct.md#e11)
[^page2016conduct-e12]: Page et al. 2016, Consenting Process. [Evidence](../../../sources/notes/page2016conduct.md#e12)
[^page2016conduct-e13]: Page et al. 2016, Clinical Trial Approval Policies. [Evidence](../../../sources/notes/page2016conduct.md#e13)
[^page2016conduct-e14]: Page et al. 2016, Introduction. [Evidence](../../../sources/notes/page2016conduct.md#e14)
[^perciedusert2020arrive-e6]: Percie du Sert et al. 2020 (ARRIVE 2.0), Why good reporting is important. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e6)
[^perciedusert2020arrive-e8]: Percie du Sert et al. 2020 (ARRIVE 2.0), Why good reporting is important. [Evidence](../../../sources/notes/perciedusert2020arrive.md#e8)
[^sargeant2016strobevet-e1]: Sargeant et al. 2016 (STROBE-Vet), Abstract. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e1)
[^sargeant2016strobevet-e2]: Sargeant et al. 2016 (STROBE-Vet), Introduction. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e2)
[^sargeant2016strobevet-e4]: Sargeant et al. 2016 (STROBE-Vet), Results. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e4)
[^sargeant2016strobevet-e5]: Sargeant et al. 2016 (STROBE-Vet), Discussion. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e5)
[^sargeant2016strobevet-e6]: Sargeant et al. 2016 (STROBE-Vet), Discussion. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e6)
[^sargeant2016strobevet-e7]: Sargeant et al. 2016 (STROBE-Vet), Discussion. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e7)
[^sargeant2016strobevet-e8]: Sargeant et al. 2016 (STROBE-Vet), Discussion. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e8)
[^sargeant2016strobevet-e9]: Sargeant et al. 2016 (STROBE-Vet), Discussion. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e9)
[^sargeant2016strobevet-e10]: Sargeant et al. 2016 (STROBE-Vet), Discussion. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e10)
[^sargeant2016strobevet-e11]: Sargeant et al. 2016 (STROBE-Vet), Introduction. [Evidence](../../../sources/notes/sargeant2016strobevet.md#e11)
[^who2026onehealth-e1]: WHO 2026, One Health fact sheet, Key facts. [Evidence](../../../sources/notes/who2026onehealth.md#e1)
[^who2026onehealth-e2]: WHO 2026, One Health fact sheet, Key facts. [Evidence](../../../sources/notes/who2026onehealth.md#e2)
[^who2026onehealth-e3]: WHO 2026, One Health fact sheet, Overview. [Evidence](../../../sources/notes/who2026onehealth.md#e3)
