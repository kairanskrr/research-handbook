# Medical engineering: field overview

This page explains how research in medical engineering (also called biomedical engineering) actually works: you build devices or algorithms and take them from bench testing through animal studies to studies in people; and because what you build may one day become a medical device, you need to think about design documentation, regulation, and ethics while it is still research. The rules for human studies and animal studies are covered on the [clinical medicine page](../clinical-medicine/README.md) and the [biological sciences page](../biological-sciences/README.md); practices shared by every field are covered in the Parts listed in [The research journey at a glance](../../00_start-here/research-journey.md) and in [Throughout the project](../../08_throughout/README.md). This page covers only what is specific to this field. For the research strategies the field commonly uses and the evidence each one needs, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence); for how to do them, see [Research methods common in this field](#research-methods-common-in-this-field) at the end.

**After reading this page, you should be able to:**

- describe roughly which stages a device or algorithm goes through on its way from idea to use in patients;
- explain how a "research prototype" differs from "a product that can be marketed," and which records the US "design controls" approach expects you to keep (the old regulation has been replaced; see below);
- know what it takes for a computational model to count as "credible," and which reporting guideline to look for when you use machine learning;
- tell the conventions of engineering journals apart from those of medical journals.

---

## How research works in this field

### From idea to patient: a long chain

To reach patients, a device or algorithm usually goes through roughly these steps `[Our analysis]`:

1. **Concept and feasibility prototype**: build a rough prototype to see whether the idea works.
2. **Bench testing**: measure performance on the bench. As the US Food and Drug Administration (FDA) uses the term, "bench testing" is broad and includes in vitro testing, cadaver testing, and other nonclinical testing[^fda2023cmscredibility-e11].
3. **Computational modeling and simulation**: simulate the device and the human body on a computer; see "What makes a computational model 'credible'" below.
4. **Animal studies.**
5. **First-in-human studies and clinical studies.**

You don't necessarily go through these steps in order, and you often loop back `[Our analysis]`. The FDA's 1997 Design Control Guidance (since withdrawn; see the design controls section below) said as much: in real development, every phase feeds back to earlier phases, and product development is iterative[^fda1997designcontrol-e6]. One paper may cover only part of the chain `[Our analysis]`. Take one journal, IEEE Transactions on Biomedical Engineering (TBME; IEEE is the Institute of Electrical and Electronics Engineers): it publishes everything from methods and technology development to experimental and clinical studies with an engineering contribution[^embstbmeprepare-e1].

### Engineers and clinicians work together

Device research may need engineers and clinicians to collaborate: clinicians know what is missing in practice, and engineers know how to build it `[Our analysis]`. A common problem in these collaborations is talking past each other `[Our analysis]`. The withdrawn 1997 guidance offered one piece of advice: when everyone developing and reviewing the requirements is familiar with medical terminology, requirements can be written in medical terms; but translating concepts into engineering language during the requirements stage often does more to reduce misunderstandings[^fda1997designcontrol-e4]. It also warned that even a simple statement can raise a large number of design questions, so a concept document can be the starting point for development but is not the same as design requirements[^fda1997designcontrol-e3].

The Code of Ethics of the Biomedical Engineering Society (BMES) also requires you to have collaborators or consultants check your work when it goes beyond your own expertise[^bmes2021ethics-e4].

### A research prototype is not a product

The 1997 guidance acknowledged that the line between research and development is hard to draw. Before writing formal design requirements, it is reasonable to build a quick prototype to explore whether an idea is feasible; but don't treat the prototype design as the finished design[^fda1997designcontrol-e1]. The reason: at this stage the prototype lacks the safety features and ancillary features a finished product needs, and it cannot adequately account for the variation that comes with volume manufacturing[^fda1997designcontrol-e2].

What this means for you as a researcher: a prototype that performs well in a paper is not necessarily close to clinical use; when you write papers or talk about your work, say clearly what stage it is at `[Our analysis]`. The BMES code requires strict honesty when speaking to the media and the public, including how certain your conclusions are, and avoiding false hope of treatment[^bmes2021ethics-e11].

### Publishing: engineering journals and medical journals have different habits

Papers in this field go to both engineering journals and medical journals `[Our analysis]`. The two sides have different rules, so check your target journal's requirements before you submit.

**Engineering journals, using TBME as an example.** The rules below are from TBME's manuscript preparation page (read from a January 2025 web archive; it may have been updated since). They are the requirements of one journal, TBME; for other engineering journals, follow their own instructions for authors `[Our analysis]`:

- The abstract must be structured, no more than 250 words, and cover five points: objective, methods, results, conclusion, and significance. If any is missing, the manuscript may be returned without review[^embstbmeprepare-e2].
- The cover letter must disclose related published conference papers and explain why they are different work from this submission[^embstbmeprepare-e3]. Work that has appeared only as a conference abstract can be written up and submitted as a full paper; but if a substantial full-length conference paper has already been published, the manuscript may no longer be eligible[^embstbmeprepare-e4]. IEEE's publication rules accept that "a conference version can evolve into a journal version"[^ieee2026pspb-e4]; TBME's rule is stricter, so check the specific journal first `[Our analysis]` (for IEEE's general rule, see the [electrical engineering page](../electrical-engineering/README.md#publishing-with-ieee-as-the-example-a-conference-paper-can-grow-into-a-journal-paper)).
- Each article gets at least two independent reviewers, with single-blind review (reviewers know who the authors are; authors don't know who the reviewers are)[^embstbmeprepare-e6]; the page at the time gave the time from submission to decision as about 30 days[^embstbmeprepare-e5].
- If duplicate submission is discovered, the IEEE Engineering in Medicine and Biology Society (EMBS, TBME's sponsoring society) will sanction the authors[^embstbmeprepare-e7].

**Medical journals.** Before submitting, check whether your target journal follows the recommendations of the International Committee of Medical Journal Editors (ICMJE). For ICMJE's rules on authorship, conflicts of interest, data sharing statements, and reporting guidelines, see the [clinical medicine page](../clinical-medicine/README.md#norms-and-reporting-standards-in-this-field). The rule most relevant to this field: ICMJE's definition of "health-related interventions" explicitly includes devices[^icmje2026recommendations-e17], and ICMJE recommends that medical journals require registration of clinical trials in a public trials registry at or before the time of first patient consent for enrollment, as a condition of consideration for publication[^icmje2026recommendations-e15]. So clinical trials of devices must also be registered in advance `[Our analysis]`.

**Authorship.** IEEE's authorship criteria explicitly list "prototype development" as one of the intellectual contributions that can qualify someone as an author[^ieee2026pspb-e6]. When submitting to medical journals that follow ICMJE, use ICMJE's four criteria; see the [clinical medicine page](../clinical-medicine/README.md#authorship-the-icmjes-four-criteria).

---

## How this field differs from others

The table is our own summary, meant to help you spot the differences quickly `[Our analysis]`.

| | Medical engineering | Computer science | Clinical medicine |
|---|---|---|---|
| Where results come from | Prototypes, bench testing, simulation, animal studies, human studies, often several combined | Mainly experiments on code, systems, and data | Mainly human studies |
| Documentation requirements | Projects that may become medical devices need design and test records (for the US rules, see below) | Not covered on the computer science page | Study protocol, registration, ethics approval |
| Publishing | Both engineering and medical journals, with different rules | Mainly top conferences in most areas (see the [computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue)) | Mainly journals |
| Ethics | Researchers with an engineering background may face approval for human and animal research for the first time | Experiments involving people need ethics review | Ethics review is the first gate |

---

## Norms and reporting standards in this field

### When research may become a medical device: design controls (US rules)

**Everything in this section is about US rules.** Medical device regulations in China, the EU, and elsewhere are different, and your institution may have its own requirements; follow local regulations and institutional rules `[Our analysis]`. The BMES code also makes understanding local regulations the researcher's own responsibility[^bmes2021ethics-e2].

**First, be clear: the old regulation and old guidance cited below are no longer in effect.**

- In the current version of Title 21 of the US Code of Federal Regulations (CFR), Part 820 (read for this page in October 2026), the former section on design controls, §820.30, has been removed and is marked "Reserved"[^cfr2026qmsr-e1].
- The current rule: manufacturers of Class II, Class III, and some Class I devices must follow clause 7.3 of the international standard ISO 13485 for design and development[^cfr2026qmsr-e2]. ISO 13485:2016 is the international standard for medical device quality management systems, issued by the International Organization for Standardization (ISO), and the new regulation incorporates it by reference[^aabb2026qmsr-e1]; it has to be obtained from ISO[^cfr2026qmsr-e3].
- The FDA's 1997 Design Control Guidance, which explained the old section, has also been withdrawn[^fda2026withdrawn-e2].

This page still cites the old regulation and old guidance only because they are free to read and explain the thinking behind design controls clearly. **They are not current requirements**; for actual practice, follow the current regulation and ISO 13485 `[Our analysis]`.

**What the old section said (only to understand the approach).** The old §820.30 (April 1, 2023 edition) required manufacturers of Class III, Class II, and some Class I devices to control the device design process[^cfr2023designcontrols-e1]. Its stages can serve as a checklist of "which records to keep" during research `[Our analysis]`:

- **Design input**: write down the design requirements, covering the intended use and the needs of users and patients[^cfr2023designcontrols-e2].
- **Design review**: each review must include representatives of all relevant functions, plus someone who does not have direct responsibility for the stage being reviewed[^cfr2023designcontrols-e3].
- **Design verification**: confirm that the design output meets the design input; it answers "did we build it to the requirements?"[^cfr2023designcontrols-e4] The old guidance says this is done through tests, inspections, and analyses[^fda1997designcontrol-e9].
- **Design validation**: ensure that the device conforms to user needs and intended uses, by testing production devices under actual or simulated use conditions[^cfr2023designcontrols-e5]; it answers "is what we built what users actually need?" The old guidance says validation includes verification and goes one step further[^fda1997designcontrol-e7].
- **Design changes**: document, review, and approve changes before making them[^cfr2023designcontrols-e6].
- **Design history file**: collect these records in one place to show the design was developed according to the approved plan[^cfr2023designcontrols-e7].

**What this means for graduate students.** The current US regulation applies to device "manufacturers"[^cfr2026qmsr-e4]. On whether research must comply, the FDA wrote when it issued the old regulation in 1996 that design controls are not intended to apply to concept development and feasibility studies; but once a decision is made to develop a design, a plan must be set up to ensure the design that goes into production meets the approved requirements[^fda1996qsr-e1]. That statement was about the old regulation; when the FDA issued the new regulation in 2024, it said the new and old regulations are substantially similar[^fda2024qmsr-e3]. Also, when a device is used in clinical studies in people, the US Investigational Device Exemption (IDE; see the next section) exempts it from a set of premarket requirements, but the current text states that design and development requirements (§820.10(c), where applicable) are not among those exempted[^cfr2026ide-e7]. Exactly when a university lab project has to start complying is for your advisor and your institution's regulatory affairs or technology transfer office to say. Even if you are not bound by the rules, two things are worth doing from day one `[Our analysis]`:

1. **Write down your requirements**: who the users are, what clinical problem you are solving, and what targets you need to hit. The old guidance warns that discovering key requirements only at validation can mean costly redesign and rework[^fda1997designcontrol-e5]; if you expect to run clinical trials, your plan should also allow for the regulatory work they involve[^fda1997designcontrol-e8].
2. **Keep records of the process**: the BMES code requires careful, complete, and accurate records throughout research and design[^bmes2021ethics-e3]. For how to keep them, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

### Before testing in people: investigational devices (US 21 CFR 812)

**This is also US regulation, and it is current; for device clinical studies in China or other countries, follow local regulations `[Our analysis]`.** Title 21 of the US Code of Federal Regulations, Part 812 (21 CFR 812), sets out procedures for clinical investigations of devices[^cfr2026ide-e1]: it applies to all clinical investigations of devices to determine safety and effectiveness, except for several categories it lists[^cfr2026ide-e2]. Key concepts:

- **Significant risk device**: the regulation lists several categories; broadly, an investigational device that presents a potential for serious risk to the health, safety, or welfare of a subject[^cfr2026ide-e3]. For studies of devices that are not significant risk, one requirement is to give the Institutional Review Board (IRB, the US name for an ethics committee) a brief explanation of why the device is not a significant risk device, and obtain its approval[^cfr2026ide-e4].
- **Sponsor-investigator**: someone who both initiates and actually conducts an investigation, and so carries the obligations of both an investigator and a sponsor[^cfr2026ide-e5]. A university researcher who initiates their own device study may be in exactly this position `[Our analysis]`.
- **Devices intended solely for research on laboratory animals** and labeled as required are exempt from Part 812, apart from a few provisions[^cfr2026ide-e6]; the ethics requirements for the animal experiments themselves are separate, as described below.

### What makes a computational model "credible" (US FDA 2023 guidance)

This field uses computational models a lot: for example, to assess the durability of an implantable stent on a computer[^fda2023cmscredibility-e3], or to run an in silico clinical trial with a set of simulated patients (a "virtual cohort")[^fda2023cmscredibility-e4]. A 2023 FDA guidance explains how to show that such a model is credible when submitting a device application to the FDA. Two things to know first: it is not binding on the FDA or the public[^fda2023cmscredibility-e1]; and it covers only physics-based or mechanistic models, not data-driven models such as machine learning[^fda2023cmscredibility-e2].

Several of the guidance's concepts are useful in research too `[Our analysis]`:

- **Credibility is always for a specific use.** Credibility is trust in a model's predictive capability for a particular "context of use"[^fda2023cmscredibility-e5]; the context of use states exactly what role and scope the model has in answering the question[^fda2023cmscredibility-e6]. Use the same model for something else and you have to make the case again `[Our analysis]`.
- **The higher the risk, the more evidence you need.** How credible the model needs to be depends on the risk of using it to answer the question; that risk depends on two things: how much influence the model has on the decision, and how serious the consequences of a wrong decision would be[^fda2023cmscredibility-e7]. If bench or animal test results are also used to answer the same question, the model's influence changes[^fda2023cmscredibility-e8].
- **Verification and validation are different things.** Verification checks whether the software that solves the mathematical model is implemented correctly[^fda2023cmscredibility-e9]; validation checks how accurately the model represents the real world[^fda2023cmscredibility-e13].
- **Calibration is not validation.** Comparing the model against the same data you used to tune its parameters does not count as validation evidence; it is weaker than validation evidence[^fda2023cmscredibility-e10]. Hold out independent data for testing `[Our analysis]`.

### When you use machine learning: find the right reporting guideline

The FDA guidance above does not cover machine learning models[^fda2023cmscredibility-e2]. For clinical prediction models (whether built with regression or machine learning), you can report using TRIPOD+AI (TRIPOD stands for Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis)[^collins2024tripodai-e2]: it has a 27-item checklist and a 13-item checklist for abstracts[^collins2024tripodai-e1]. Table 1 of this 2024 article also lists other reporting guidelines by study type; for example, studies of artificial intelligence (AI) in medical imaging, early clinical evaluation of AI-based decision support systems, and reports of clinical trials with an AI component each have their own guideline. Look up the exact names in Table 1 of the original[^collins2024tripodai-e3].

Two points differ from the habits of computer science, so watch for them:

- **Terminology.** In machine learning research, "validation data" can mean the data used for tuning, or the data used to evaluate model performance[^collins2024tripodai-e6]. The TRIPOD+AI authors hold that there is no such thing as a "validated prediction model," and they use "evaluation" instead of "validation"[^collins2024tripodai-e4].
- **Keep data separate.** Evaluation data must be kept separate from the data used for training, tuning, and model selection, with no participant appearing in both[^collins2024tripodai-e5]. Putting several images from the same patient in both the training set and the test set breaks this rule `[Our analysis]`.

### People and animals: ethics review (see other pages for details)

For research involving people, see the [clinical medicine page](../clinical-medicine/README.md#your-subjects-are-people-so-ethics-comes-first) and [When research involves people, protect them first](../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); for animal research, see the [biological sciences page](../biological-sciences/README.md#animal-research-the-3rs-and-the-arrive-guidelines) and [Preclinical animal studies](../../06_methods/preclinical_animal_study.md). One point relevant to this field: the UK's National Centre for the Replacement, Refinement and Reduction of Animals in Research (NC3Rs) lists mathematical and computer models among the methods for "full replacement" of animals[^nc3rsthe3rs-e4]; this is one more reason good computational models are valuable `[Our analysis]`. In your paper, describe ethics approval as your target journal requires: for example, the TBME page cites the Declaration of Helsinki as revised in 2000[^embstbmeprepare-e9], while ICMJE requires conformity with the 2024 revision[^icmje2026recommendations-e11].

### Professional ethics: the BMES code

The BMES code is not law; it sets out the professional ethics biomedical engineers should follow beyond regulatory requirements[^bmes2021ethics-e1]. Besides the points already mentioned above, these are the most relevant to research:

- **Design for as broad a population as possible**: consider different ages, sexes, body sizes, abilities, and physiological characteristics[^bmes2021ethics-e8]. Performance measured only on healthy young volunteers may not carry over to patients `[Our analysis]`.
- **Share data and methods**: after a project ends, make them as public as possible within the privacy limits on human data[^bmes2021ethics-e5].
- **Declare conflicts of interest**: both financial ones and those arising from your scholarly views[^bmes2021ethics-e10]. Results in this field may involve patents or startups `[Our analysis]`; the interests TBME requires you to disclose include an author's financial interests in companies that may license, patent, or use the work[^embstbmeprepare-e8].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by its central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table lists only the strategies this page's sources support. The grouping and the "What it looks like in medical engineering" column are our own synthesis; the standards come mostly from US regulations and guidance and from individual journals, and each speaks only for the source in its footnote. Our sources do not cover how description, synthesis, and other strategies are used in this field `[Our analysis]`.

| Strategy | What it looks like in medical engineering | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md): devices and prototypes | Proposing new devices, sensors, or methods. TBME publishes methods and technology development with biomedical applications[^embstbmeprepare-e1]; performance can be measured with bench testing, which as the FDA uses the term includes in vitro, cadaver, and other nonclinical testing[^fda2023cmscredibility-e11] | Distinguish verification (output meets design input)[^cfr2023designcontrols-e4] from validation (meets user needs under actual or simulated use conditions)[^cfr2023designcontrols-e5]; a prototype lacks the safety features a finished product needs and should not be treated as one[^fda1997designcontrol-e2] | [Engineering research](../computer-science/practices/engineering_research.md) (computer science page, for reference) |
| [Building and improving](../../05_research-strategies/build_improve.md): computational models | Assessing devices on a computer, for example the durability of an implantable stent[^fda2023cmscredibility-e3] | Per the 2023 FDA guidance: credibility is tied to a specific context of use[^fda2023cmscredibility-e5]; the higher the risk, the more evidence needed[^fda2023cmscredibility-e7]; calibration data does not count as validation evidence[^fda2023cmscredibility-e10] | [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Building and improving](../../05_research-strategies/build_improve.md): diagnostic or predictive algorithms | Developing or evaluating clinical prediction models, whether with regression or machine learning[^collins2024tripodai-e2] | Report using TRIPOD+AI[^collins2024tripodai-e2]; no participant may appear in both the evaluation data and the training data[^collins2024tripodai-e5]; the BMES code requires validation for the actual intended use, with limitations and data sources stated clearly[^bmes2021ethics-e9] | [Data science research](../../06_methods/data_science.md) |
| [Causal explanation](../../05_research-strategies/explain_causality.md): clinical studies of devices | Testing whether a device is safe and effective in patients. In the US, clinical investigations to determine a device's safety and effectiveness fall under 21 CFR 812[^cfr2026ide-e2] | Randomized trials that are appropriately designed, conducted, analyzed, and reported are generally considered the highest-quality evidence for evaluating healthcare interventions[^hopewell2025consort-e2]; ICMJE's interventions include devices[^icmje2026recommendations-e17], and it recommends that journals require registration at or before the time of first patient consent for enrollment as a condition of consideration for publication[^icmje2026recommendations-e15] | [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), [Preclinical animal studies](../../06_methods/preclinical_animal_study.md) |

How to use this table `[Our analysis]`:

- **One project often spans several rows.** For example, you build a prototype and bench test it, supplement it with a computational model, and finally move to animal and human studies. Choose the main strategy by the paper's central claim, and state clearly how far along the "prototype → bench → animal → human" chain the project has got.
- **The same strategy may need different amounts of evidence for an engineering journal and a medical journal.** Check against your target journal's requirements before submitting; see [Publishing: engineering journals and medical journals have different habits](#publishing-engineering-journals-and-medical-journals-have-different-habits) above.

## Research methods common in this field

This field does not have its own field-specific methods page. Among the cross-field research types, the ones commonly used are [Quantitative simulation](../../06_methods/simulation_study.md), [Data science research](../../06_methods/data_science.md), [Controlled experiments](../../06_methods/controlled_experiment.md), [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md), and [Preclinical animal studies](../../06_methods/preclinical_animal_study.md); for new devices and algorithms, you can also draw on [Engineering research](../computer-science/practices/engineering_research.md) on the computer science page. Below are only the extra points to watch:

- **Bench testing** (no separate page): make test conditions as close to actual use as possible, and describe the setup clearly `[Our analysis]`.
- **Controlled experiments**: comparing how different designs affect users (clinicians, nurses, patients), for example in usability testing `[Our analysis]`. If you use an investigational device, Part 812 may also apply in the US[^cfr2026ide-e2].

---

## Advice for newcomers

1. **Write the requirements before you build the prototype.** Work with your clinical collaborators to put "what clinical problem we are solving and what targets we need to hit" into engineering language[^fda1997designcontrol-e4].
2. **Keep good records from day one.** Record design decisions, test results, and the reasons for changes[^bmes2021ethics-e3]; if the project is ever translated into a product, you will need these records `[Our analysis]`.
3. **If people or animals are involved, ask about ethics review first.** For device research, also find out the local rules on investigational devices; in the US, look at Part 812[^cfr2026ide-e2].
4. **When you talk about your work, say what stage it is at.** Don't let a bench prototype sound like a product that is about to cure patients[^bmes2021ethics-e11].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Promoting a research prototype as if it were close to a finished product | A prototype lacks the safety features a finished product needs and cannot adequately account for manufacturing variation[^fda1997designcontrol-e2] |
| Leaving requirements as a vague concept document | Even a simple statement can raise many design questions; a concept document is not the same as design requirements[^fda1997designcontrol-e3]; discovering key requirements late means costly rework[^fda1997designcontrol-e5] |
| Doing only verification (meets the specs) and then claiming the device "meets clinical needs" | Verification and validation are different things; in the words of the old US section, validation requires testing under actual or simulated use conditions[^cfr2023designcontrols-e5] |
| Treating 21 CFR 820.30 or the FDA's 1997 guidance as current requirements | The former has been removed from the current regulation, and design and development now follow ISO 13485 clause 7.3[^cfr2026qmsr-e1][^cfr2026qmsr-e2]; the FDA has withdrawn the latter[^fda2026withdrawn-e2] |
| Data from the same patient appearing in both the training set and the test set | Evaluation data must be kept separate from training data, with no participant in both[^collins2024tripodai-e5] |
| Submitting a nearly identical version of a published full-length conference paper to TBME | TBME may decline to consider the manuscript for that reason[^embstbmeprepare-e4] |
| Registering a device clinical trial only after it has started | ICMJE recommends that journals require registration at or before the time of first patient consent for enrollment as a condition of consideration for publication, and devices fall within its definition of interventions[^icmje2026recommendations-e15][^icmje2026recommendations-e17] |
| Not disclosing your shares or patents in related companies | TBME requires disclosure of such financial interests[^embstbmeprepare-e8] |
| Treating US FDA rules as if they applied everywhere | Everything cited on this page is US regulation; the BMES code requires you to understand local regulations[^bmes2021ethics-e2] |

---

## Further reading

- **BMES Code of Ethics (2021)**: tells you what the profession expects of you regarding research, data, research participants, animals, and the public. The first thing to read.
- **US FDA, Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions (2023)**: for anyone doing simulation or computational modeling. Focus on Section IV (definitions) and Section VI (context of use, model risk, categories of evidence).
- **US FDA, Design Control Guidance for Medical Device Manufacturers (1997, withdrawn)**: use it only as historical background for understanding design control concepts; for actual practice, follow the current regulation and ISO 13485.
- **Collins et al. 2024, TRIPOD+AI**: for anyone developing or evaluating clinical prediction models; Table 1 helps you find other AI-related reporting guidelines.
- **Your target journal's instructions for authors**: for example, TBME's manuscript preparation page; for medical journals, read the ICMJE recommendations (see the [clinical medicine page](../clinical-medicine/README.md)).
- **Your country's medical device regulations and your institution's guidance**: everything cited on this page is US regulation; countries and institutions differ, so go by your local rules.

[^fda2023cmscredibility-e1]: FDA 2023, guidance on credibility of computational modeling and simulation, note after the cover. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e1)
[^fda2023cmscredibility-e2]: FDA 2023, I. Introduction. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e2)
[^fda2023cmscredibility-e3]: FDA 2023, II. Background. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e3)
[^fda2023cmscredibility-e4]: FDA 2023, II. Background. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e4)
[^fda2023cmscredibility-e5]: FDA 2023, IV. Definitions. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e5)
[^fda2023cmscredibility-e6]: FDA 2023, IV. Definitions. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e6)
[^fda2023cmscredibility-e7]: FDA 2023, VI.A.(3) Model risk. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e7)
[^fda2023cmscredibility-e8]: FDA 2023, VI.A.(3) Model risk. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e8)
[^fda2023cmscredibility-e9]: FDA 2023, VI.B Credibility evidence. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e9)
[^fda2023cmscredibility-e10]: FDA 2023, VI.B (2) Model calibration evidence. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e10)
[^fda2023cmscredibility-e11]: FDA 2023, VI.B (3) Bench test validation results. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e11)
[^fda2023cmscredibility-e13]: FDA 2023, IV. Definitions. [Evidence](../../../sources/notes/fda2023cmscredibility.md#e13)
[^fda1997designcontrol-e1]: FDA 1997, Design Control Guidance (withdrawn), Section C, Research and Development. [Evidence](../../../sources/notes/fda1997designcontrol.md#e1)
[^fda1997designcontrol-e2]: FDA 1997 (withdrawn), Section C, Research and Development. [Evidence](../../../sources/notes/fda1997designcontrol.md#e2)
[^fda1997designcontrol-e3]: FDA 1997 (withdrawn), Section C, Concept Documents versus Design Input. [Evidence](../../../sources/notes/fda1997designcontrol.md#e3)
[^fda1997designcontrol-e4]: FDA 1997 (withdrawn), Section C, Responsibility for Design Input Development. [Evidence](../../../sources/notes/fda1997designcontrol.md#e4)
[^fda1997designcontrol-e5]: FDA 1997 (withdrawn), Section C, opening discussion. [Evidence](../../../sources/notes/fda1997designcontrol.md#e5)
[^fda1997designcontrol-e6]: FDA 1997 (withdrawn), Introduction. [Evidence](../../../sources/notes/fda1997designcontrol.md#e6)
[^fda1997designcontrol-e7]: FDA 1997 (withdrawn), Introduction. [Evidence](../../../sources/notes/fda1997designcontrol.md#e7)
[^fda1997designcontrol-e8]: FDA 1997 (withdrawn), Section B. [Evidence](../../../sources/notes/fda1997designcontrol.md#e8)
[^fda1997designcontrol-e9]: FDA 1997 (withdrawn), Section F. [Evidence](../../../sources/notes/fda1997designcontrol.md#e9)
[^fda1996qsr-e1]: FDA 1996, Quality System Regulation final rule (61 FR 52602), response to comment 62, p. 52616. [Evidence](../../../sources/notes/fda1996qsr.md#e1)
[^cfr2023designcontrols-e1]: 21 CFR 820.30 (April 1, 2023 version, now removed), (a). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e1)
[^cfr2023designcontrols-e2]: 21 CFR 820.30 (2023 version, now removed), (c). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e2)
[^cfr2023designcontrols-e3]: 21 CFR 820.30 (2023 version, now removed), (e). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e3)
[^cfr2023designcontrols-e4]: 21 CFR 820.30 (2023 version, now removed), (f). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e4)
[^cfr2023designcontrols-e5]: 21 CFR 820.30 (2023 version, now removed), (g). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e5)
[^cfr2023designcontrols-e6]: 21 CFR 820.30 (2023 version, now removed), (i). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e6)
[^cfr2023designcontrols-e7]: 21 CFR 820.30 (2023 version, now removed), (j). [Evidence](../../../sources/notes/cfr2023designcontrols.md#e7)
[^cfr2026qmsr-e1]: 21 CFR Part 820 (current version, eCFR), §§820.20–820.30. [Evidence](../../../sources/notes/cfr2026qmsr.md#e1)
[^cfr2026qmsr-e2]: 21 CFR Part 820 (current version), §820.10(c). [Evidence](../../../sources/notes/cfr2026qmsr.md#e2)
[^cfr2026qmsr-e3]: 21 CFR Part 820 (current version), §820.7. [Evidence](../../../sources/notes/cfr2026qmsr.md#e3)
[^cfr2026qmsr-e4]: 21 CFR Part 820 (current version), §820.1(a). [Evidence](../../../sources/notes/cfr2026qmsr.md#e4)
[^aabb2026qmsr-e1]: AABB news release, February 4, 2026, para. 2. [Evidence](../../../sources/notes/aabb2026qmsr.md#e1)
[^fda2026withdrawn-e2]: FDA website, Withdrawn or Expired Guidance page (content current as of 2026-03-06), Design Control Guidance row. [Evidence](../../../sources/notes/fda2026withdrawn.md#e2)
[^fda2024qmsr-e3]: FDA 2024, Quality Management System Regulation final rule (89 FR 7496), response to comment 76, p. 7517. [Evidence](../../../sources/notes/fda2024qmsr.md#e3)
[^cfr2026ide-e1]: 21 CFR Part 812 (current version, eCFR), §812.1(a). [Evidence](../../../sources/notes/cfr2026ide.md#e1)
[^cfr2026ide-e2]: 21 CFR Part 812 (current version), §812.2(a). [Evidence](../../../sources/notes/cfr2026ide.md#e2)
[^cfr2026ide-e3]: 21 CFR Part 812 (current version), §812.3(m). [Evidence](../../../sources/notes/cfr2026ide.md#e3)
[^cfr2026ide-e4]: 21 CFR Part 812 (current version), §812.2(b)(1)(ii). [Evidence](../../../sources/notes/cfr2026ide.md#e4)
[^cfr2026ide-e5]: 21 CFR Part 812 (current version), §812.3(o). [Evidence](../../../sources/notes/cfr2026ide.md#e5)
[^cfr2026ide-e6]: 21 CFR Part 812 (current version), §812.2(c)(6). [Evidence](../../../sources/notes/cfr2026ide.md#e6)
[^cfr2026ide-e7]: 21 CFR Part 812 (current version), §812.1(a). [Evidence](../../../sources/notes/cfr2026ide.md#e7)
[^bmes2021ethics-e1]: BMES Code of Ethics 2021, Preamble. [Evidence](../../../sources/notes/bmes2021ethics.md#e1)
[^bmes2021ethics-e2]: BMES Code of Ethics 2021, 1.1.1. [Evidence](../../../sources/notes/bmes2021ethics.md#e2)
[^bmes2021ethics-e3]: BMES Code of Ethics 2021, 2.1.3. [Evidence](../../../sources/notes/bmes2021ethics.md#e3)
[^bmes2021ethics-e4]: BMES Code of Ethics 2021, 2.1.4. [Evidence](../../../sources/notes/bmes2021ethics.md#e4)
[^bmes2021ethics-e5]: BMES Code of Ethics 2021, 2.2.2. [Evidence](../../../sources/notes/bmes2021ethics.md#e5)
[^bmes2021ethics-e8]: BMES Code of Ethics 2021, 3.1.2. [Evidence](../../../sources/notes/bmes2021ethics.md#e8)
[^bmes2021ethics-e9]: BMES Code of Ethics 2021, 3.2.2. [Evidence](../../../sources/notes/bmes2021ethics.md#e9)
[^bmes2021ethics-e10]: BMES Code of Ethics 2021, 5.1.1. [Evidence](../../../sources/notes/bmes2021ethics.md#e10)
[^bmes2021ethics-e11]: BMES Code of Ethics 2021, 5.1.2. [Evidence](../../../sources/notes/bmes2021ethics.md#e11)
[^embstbmeprepare-e1]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page (archived January 2025), journal description. [Evidence](../../../sources/notes/embstbmeprepare.md#e1)
[^embstbmeprepare-e2]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, Abstract. [Evidence](../../../sources/notes/embstbmeprepare.md#e2)
[^embstbmeprepare-e3]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, Cover Letter. [Evidence](../../../sources/notes/embstbmeprepare.md#e3)
[^embstbmeprepare-e4]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, note after Cover Letter. [Evidence](../../../sources/notes/embstbmeprepare.md#e4)
[^embstbmeprepare-e5]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, Letters. [Evidence](../../../sources/notes/embstbmeprepare.md#e5)
[^embstbmeprepare-e6]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, Peer Review. [Evidence](../../../sources/notes/embstbmeprepare.md#e6)
[^embstbmeprepare-e7]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, Author Consent Form. [Evidence](../../../sources/notes/embstbmeprepare.md#e7)
[^embstbmeprepare-e8]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, conflict of interest disclosure. [Evidence](../../../sources/notes/embstbmeprepare.md#e8)
[^embstbmeprepare-e9]: IEEE EMBS, IEEE Transactions on Biomedical Engineering (TBME) submission instructions page, human and animal subjects. [Evidence](../../../sources/notes/embstbmeprepare.md#e9)
[^collins2024tripodai-e1]: Collins et al. 2024 (TRIPOD+AI), Summary points. [Evidence](../../../sources/notes/collins2024tripodai.md#e1)
[^collins2024tripodai-e2]: Collins et al. 2024, Abstract. [Evidence](../../../sources/notes/collins2024tripodai.md#e2)
[^collins2024tripodai-e3]: Collins et al. 2024, Table 1. [Evidence](../../../sources/notes/collins2024tripodai.md#e3)
[^collins2024tripodai-e4]: Collins et al. 2024, Development of TRIPOD+AI. [Evidence](../../../sources/notes/collins2024tripodai.md#e4)
[^collins2024tripodai-e5]: Collins et al. 2024, Box 1 Glossary. [Evidence](../../../sources/notes/collins2024tripodai.md#e5)
[^collins2024tripodai-e6]: Collins et al. 2024, Box 1 Glossary footnote. [Evidence](../../../sources/notes/collins2024tripodai.md#e6)
[^icmje2026recommendations-e15]: ICMJE 2026, §III.L.1. [Evidence](../../../sources/notes/icmje2026recommendations.md#e15)
[^icmje2026recommendations-e17]: ICMJE 2026, §III.L.1. [Evidence](../../../sources/notes/icmje2026recommendations.md#e17)
[^icmje2026recommendations-e11]: ICMJE 2026, §II.E. [Evidence](../../../sources/notes/icmje2026recommendations.md#e11)
[^ieee2026pspb-e4]: IEEE PSPB Operations Manual 2026, §8.1.7.F. [Evidence](../../../sources/notes/ieee2026pspb.md#e4)
[^ieee2026pspb-e6]: IEEE PSPB Operations Manual 2026, §8.2.1.A.1. [Evidence](../../../sources/notes/ieee2026pspb.md#e6)
[^nc3rsthe3rs-e4]: NC3Rs, The 3Rs, Replacement. [Evidence](../../../sources/notes/nc3rsthe3rs.md#e4)
[^hopewell2025consort-e2]: Hopewell et al. 2025 (CONSORT 2025), Introduction. [Evidence](../../../sources/notes/hopewell2025consort.md#e2)
