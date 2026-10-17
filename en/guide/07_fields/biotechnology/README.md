# Biotechnology: field overview

This page explains how biotechnology research actually works. Under the Organisation for Economic Co-operation and Development (OECD) field classification this handbook uses, the page covers four subfields together: 2.8 Environmental biotechnology, 2.9 Industrial biotechnology, 3.4 Medical biotechnology, and 4.4 Agricultural biotechnology. What they share is that they modify organisms (strains, cells, plants, animals) or use biological processes to make something useful `[Our analysis]`.

Day-to-day lab work in biotechnology is much like the biological sciences `[Our analysis]`. For lab notebooks, biological and technical replicates, validating reagents and cell lines, and rules for animal experiments, see the [biological sciences page](../biological-sciences/README.md); they are not repeated here. This page covers only what biotechnology adds: biosafety levels and approvals, rules on recombinant and synthetic DNA, dual-use research, international rules on genetically modified organisms, engineering-style development and scale-up, and standards for measurement and description. For human trials, see the [clinical medicine page](../clinical-medicine/README.md); for patents, see the [electrical, electronic, and information engineering page](../electrical-engineering/README.md#publish-or-patent-the-us-as-the-example); for practices shared by every field, see the Parts listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies biotechnology commonly uses and the evidence each one needs, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

**After reading this page, you should be able to:**

- explain which safety reviews you must pass before starting recombinant DNA or pathogen-related work (using the US as the example), and where to ask about your own institution's rules;
- tell biosafety levels from pathogen risk groups, and know what "dual-use research" means;
- know that when genetically modified organisms leave the lab or cross borders, an international treaty binds the countries that have joined it;
- understand why good results in the lab don't guarantee scaled-up production, and how to report measurements so others can reproduce them.

---

## How research works in this field

### Modify organisms and put them to use

An international treaty's definition is a good way to understand the core techniques of "modification" in biotechnology. The Cartagena Protocol on Biosafety defines "modern biotechnology" as in vitro nucleic acid techniques (including recombinant DNA and direct injection of nucleic acid into cells) or fusion of cells beyond the taxonomic family; these overcome natural reproductive or recombination barriers and are not techniques used in traditional breeding[^cbd2000cartagena-e4]. Roughly, the four branches are `[Our analysis]`:

| Branch | Typical subjects | Extra things to watch |
|---|---|---|
| Environmental biotechnology | Using microbes to treat pollution and recover resources | Organisms may be released into the open environment |
| Industrial biotechnology | Using engineered bacteria, yeast, or cells to produce chemicals, enzymes, and materials | Scaling up from the lab to production |
| Medical biotechnology | Gene therapy, cell therapy, biologics, diagnostics | Dedicated approvals before anything goes into humans; see the [clinical medicine page](../clinical-medicine/README.md) |
| Agricultural biotechnology | Genetically modified or gene-edited crops and animals | Rules on field trials and cross-border shipment |

### Pass biosafety review before you start

Compared with ordinary biology experiments, biotechnology research has an extra hurdle: many experiments must be approved or registered before they begin `[Our analysis]`. In the US, for example, research of this kind conducted at an institution that receives NIH (National Institutes of Health) funding for recombinant or synthetic nucleic acid research[^nih2024guidelines-e2] must follow the NIH Guidelines regardless of where the money comes from[^nih2024guidelines-e3]; experiments that require prior approval must not start, or be modified, until the Institutional Biosafety Committee has approved them[^nih2024guidelines-e7]. Details are in "Norms and reporting standards in this field" below. For a newcomer, this means: in the first week of a new project, find out which category your experiment falls into, whether it needs approval, and who signs off `[Our analysis]`. Approval takes time, so allow for it in your plan `[Our analysis]`.

### Design, build, test, for many rounds

Many biotechnology projects run like engineering: you design a genetic circuit or metabolic pathway, build a strain or cell line, test how it performs, and revise the design based on the results `[Our analysis]`. The difficulty is that biological systems don't behave as obediently as electronic circuits. The authors of a multi-lab synthetic biology study point out that a major obstacle to moving from principle to application is that biological systems are often sensitive to small changes in cellular or environmental conditions[^beal2016reproducibility-e6]. So in every round, record the construct, host, culture conditions, and measurement method in full; otherwise you can't compare the next round with this one `[Our analysis]`. For how to keep a notebook, see the [biological sciences page](../biological-sciences/README.md#the-lab-notebook-is-the-primary-record).

### From shake flask to fermenter: scale-up

The output of industrial biotechnology eventually has to be scaled up to production. The figures and advice below all come from a 2018 article by Crater and Lievense. Both authors work at a US biotechnology company, and the principles in the article are distilled from their own industrial projects[^crater2018scaleup-e10]; they are about industrial microbial processes:

- **The scales are far apart.** A lab process (for example, a 0.5–10 liter fermenter) has to be transferred to production scale (for example, 20,000 to 2,000,000 liters), a scale-up factor ranging from thousands to millions[^crater2018scaleup-e1]. According to the authors, going from lab to production typically takes 3–10 years[^crater2018scaleup-e2].
- **You can't just copy lab conditions.** You cannot simply make the equipment bigger and reproduce lab conditions[^crater2018scaleup-e3]; many parameters affect fermentation performance, and most of them change during scale-up[^crater2018scaleup-e7].
- **Think about scale-up when you choose the strain.** The authors say a common fundamental mistake is to select and engineer the host strain without considering whether it suits large-scale production[^crater2018scaleup-e5]. Process development at the lab stage should mimic large-scale production conditions as closely as possible[^crater2018scaleup-e6].
- **Include a pilot stage in between.** Pilot runs are usually done at 1–10% of production scale[^crater2018scaleup-e9]; industrial-grade raw materials should be tested in the lab or at pilot scale before you buy them[^crater2018scaleup-e8].

The authors even argue for drawing up a conceptual design of the envisioned production process before running the first experiment[^crater2018scaleup-e4]. This is a company's view; a degree project may never get as far as scale-up `[Our analysis]`. If a paper claims "industrial potential," state the scale and conditions; for this and for scale-up problems in general, see the [chemical engineering page](../chemical-engineering/README.md#how-far-a-lab-result-is-from-industry-scale-up). Scale-up also runs into safety rules: under the US NIH Guidelines, the containment conditions for experiments with more than 10 liters of culture are set by the Institutional Biosafety Committee[^nih2024guidelines-e13].

### Publication, patents, and industry

Our sources do not give publication statistics or authorship conventions specific to biotechnology; for the general picture, see the [biological sciences page](../biological-sciences/README.md#publishing-journals-and-preprints), and follow your target journal's requirements. Biotechnology results (strains, sequences, processes) may be patentable, and the work often involves industry partners; before you submit a paper, give a talk, or post a preprint, ask your advisor whether to file a patent first `[Our analysis]`. For how US university technology transfer offices work, see the [electrical, electronic, and information engineering page](../electrical-engineering/README.md#publish-or-patent-the-us-as-the-example); for confidentiality and publication arrangements when working with companies, see the [chemical engineering page](../chemical-engineering/README.md#working-with-companies-plan-confidentiality-patents-and-publication-in-advance).

---

## How this field differs from others

| `[Our analysis]` | Biotechnology | Biological sciences (lab-based) | Computer science |
|---|---|---|---|
| Goal | Produce useful organisms, products, or processes | Understand the mechanisms of living things | Produce algorithms and systems, or study computational problems |
| Review before starting | Recombinant DNA and pathogen-related experiments may need prior approval from a biosafety committee (US rules below) | Recombinant DNA and pathogen experiments also need biosafety review; animal experiments need ethics approval | Ethics review when people are involved |
| Results leaving the lab | Deliberate release of GMOs (genetically modified organisms) into the environment and cross-border shipment are governed by international treaties and national laws | Generally not relevant | Generally no controls of this kind |
| Scale | May need scaling up from a few liters to tens of thousands of liters | Generally stays at lab scale | Not relevant |
| Risk of misuse | Some research is "dual-use research" and needs separate assessment | Some pathogen research is too | Security research has similar issues |

---

## Norms and reporting standards in this field

**Most of the safety rules below are American.** Other jurisdictions have their own laws. Start with the EU and China, whose approach is similar to the US one: assess the risk first, then manage according to the risk level `[Our analysis]`.

- **European Union**: Directive 2009/41/EC of 2009 covers the "contained use" of genetically modified microorganisms, that is, modifying, culturing, or storing them under specific containment measures that limit their contact with the public and the environment[^eu2009contained-e2]. Users must first assess the risk and assign the activity to one of four classes, from negligible risk with the lowest containment, level 1, to high risk with the highest, level 4[^eu2009contained-e3][^eu2009contained-e4]; when in doubt, apply the stricter measures[^eu2009contained-e5]; class 3 and above require prior consent from the competent authority[^eu2009contained-e6].
- **China**: the Biosecurity Law of the People's Republic of China (生物安全法) was adopted in 2020 and took effect in 2021[^npc2020biosecurity-e1]. It divides biotechnology research and development activities into high, medium, and low risk[^npc2020biosecurity-e2]; medium- and high-risk activities require approval or filing, plus a risk assessment[^npc2020biosecurity-e3]; experiments with pathogenic microorganisms must be done in laboratories with the corresponding containment level[^npc2020biosecurity-e4]. This page draws on the 2020 English text; the law was amended in 2024[^npc2024legislature-e1][^npc2024legislature-e2], so the current Chinese text is authoritative.

Our sources do not cover the laws of other countries and regions. Your institution will usually have a biosafety committee or a similar office; local law and your institution's rules take precedence `[Our analysis]`. The World Health Organization (WHO) checklist for researchers also asks you to check whether your work complies with your institution's rules and with national or regional laws and regulations[^who2022responsible-e10].

### Biosafety levels: choose containment by risk assessment (US BMBL)

*Biosafety in Microbiological and Biomedical Laboratories* (BMBL), 6th edition, written by the US Centers for Disease Control and Prevention (CDC) and NIH, is an advisory document and is not intended as a regulation[^cdc2020bmbl-e1]. Its core principle is risk assessment based on the specific protocol[^cdc2020bmbl-e2]. A risk assessment has to establish four things: what hazards the agent or material poses, which procedures could expose people to it, how likely infection is after exposure, and what the consequences of infection would be[^cdc2020bmbl-e3]. This is the responsibility of the laboratory director and the principal investigator (PI), shared with the Institutional Biosafety Committee and others[^cdc2020bmbl-e4].

There are four **biosafety levels** (BSL), each a combination of facilities, safety equipment, practices, and personal protection[^cdc2020bmbl-e5]:

| Level | BMBL's description (summarized) |
|---|---|
| BSL-1 | Teaching labs, and work with well-characterized strains not known to consistently cause disease in healthy adults[^cdc2020bmbl-e6] |
| BSL-2 | Work with agents and toxins that cause human disease of varying severity[^cdc2020bmbl-e7]. When it is unknown whether human, animal, or plant samples (including primary cell lines) contain pathogens, they can often be handled safely at BSL-2[^cdc2020bmbl-e8] |
| BSL-3 | Agents that may be transmitted by the respiratory route and can cause serious or potentially lethal infection[^cdc2020bmbl-e9] |
| BSL-4 | Dangerous and exotic agents that are life-threatening, can be transmitted by aerosol, and have no vaccine or treatment[^cdc2020bmbl-e10] |

Two things that are easy to confuse:

- **Biosafety level is not the same as risk group.** Pathogens are assigned to "risk groups" by their ability to cause disease; being in Risk Group 3 does not mean the work must be done at BSL-3[^cdc2020bmbl-e11]. The NIH Guidelines also say the containment level may match the risk group, or be raised or lowered depending on the specifics[^nih2024guidelines-e17].
- **Larger quantities can change the requirements.** Handling large volumes or high concentrations of an agent may need additional measures[^cdc2020bmbl-e12]. This ties directly to the scale-up discussed above `[Our analysis]`.

BMBL warns that reading only a few of its sections is not enough to prepare even experienced people to handle infectious agents safely[^cdc2020bmbl-e13]. In practice, as a newcomer, complete your institution's biosafety training first, then have your advisor or the biosafety officer confirm which level your experiment belongs at `[Our analysis]`.

### Recombinant and synthetic nucleic acids: the US NIH Guidelines and the Institutional Biosafety Committee

The NIH *Guidelines for Research Involving Recombinant or Synthetic Nucleic Acid Molecules* (the "NIH Guidelines") set out how such research is done at US NIH-funded institutions; the scope is described below. This page draws on the April 2024 version; its header says NIH is strengthening and updating biosafety oversight[^nih2024guidelines-e14], so check for the latest version before relying on it `[Our analysis]`.

- **What it covers.** Recombinant nucleic acids are molecules constructed by joining nucleic acid segments that can replicate in a living cell; synthetic nucleic acids are molecules chemically synthesized or amplified that can base-pair with natural nucleic acids; molecules resulting from their replication are included too[^nih2024guidelines-e1].
- **Who it covers.** Research at institutions receiving NIH funding for this kind of work[^nih2024guidelines-e2], and the institution must ensure that all such research it conducts complies, regardless of funding source[^nih2024guidelines-e3]. Noncompliance can lead to suspension or termination of NIH funding for all such research at the institution[^nih2024guidelines-e4]. For NIH-funded research abroad, the host country's rules apply where it has them[^nih2024guidelines-e16].
- **The Institutional Biosafety Committee** has at least 5 members, at least 2 of whom are not affiliated with the institution and represent the surrounding community's interests in health and the environment[^nih2024guidelines-e5].
- **Experiments fall into categories.** Some need prior approval; some low-risk experiments can be done at BSL-1 but require a signed, dated registration document to be filed with the committee when they begin, for example experiments in which all components come from non-pathogenic prokaryotes and non-pathogenic lower eukaryotes[^nih2024guidelines-e10][^nih2024guidelines-e11]; and some exempt experiments need no registration, though other biosafety standards may still apply[^nih2024guidelines-e12]. It is easy to get the category wrong yourself, so let the committee confirm it `[Our analysis]`.
- **The PI's responsibilities.** The PI is fully responsible, on behalf of the institution, for compliance with the Guidelines[^nih2024guidelines-e6]. Changes to experiments must be reported too: a change of DNA source or host-vector system must be submitted to the committee for review[^nih2024guidelines-e9]; significant problems, violations, and accidents must be reported within 30 days[^nih2024guidelines-e8]. As a student you are not the PI, but tell the PI before changing an experiment, and report any accident immediately `[Our analysis]`.
- **Medical biotechnology: human gene transfer.** Experiments that transfer recombinant or synthetic nucleic acids into human participants may begin only after approval by the Institutional Biosafety Committee at the clinical trial site and after all regulatory approvals have been obtained[^nih2024guidelines-e15].

### Dual-use research: ask whether your results could be misused

The World Health Organization's 2022 *Global guidance framework for the responsible use of the life sciences* sets out some basic concepts:

- **Biosafety**: preventing unintentional exposure to pathogens and their accidental release[^who2022responsible-e3]. **Biosecurity**: preventing unauthorized access to, loss, theft, misuse, or release of pathogens and other biological materials[^who2022responsible-e4]. These two, plus oversight of dual-use research, are the three pillars of biorisk management[^who2022responsible-e5].
- **Dual-use research**: research done for beneficial purposes whose results could also be deliberately misused to harm people, animals, plants, and the environment[^who2022responsible-e2]. Research that can be readily misused to cause harm with little or no modification is called **dual-use research of concern** (DURC)[^who2022responsible-e1].

The WHO checklist for researchers is meant to be used before work begins[^who2022responsible-e6]: could the results be misused, and what measures are in place to respond[^who2022responsible-e7]; could a different method, design, or organism make the experiment safer[^who2022responsible-e8]; and does the work fall under export controls[^who2022responsible-e9]. It also acknowledges that, short of not doing the work, risk can never be reduced to zero[^who2022responsible-e11], and that managing risk is a shared responsibility[^who2022responsible-e12].

**US dual-use research policy changed in 2025–2026, and we have not read the current official documents.** What follows only reports two secondary sources, and neither should be treated as a current requirement. The first is a May 2025 Insight from the Congressional Research Service (which provides analysis to the US Congress): the US has no single federal law with legal penalties governing laboratory biosafety and biosecurity, relying instead on a mix of federal laws, federal guidance, and self-governance[^crs2025gainoffunction-e1][^crs2025gainoffunction-e3]; a policy issued in 2024 brought dual-use research of concern and research on "pathogens with enhanced pandemic potential" (also called gain-of-function research) under one oversight process and was scheduled to take effect on May 6, 2025[^crs2025gainoffunction-e4], but an executive order on May 5, 2025 directed that it be revised or replaced[^crs2025gainoffunction-e5], and NIH rescinded the notice implementing it[^crs2025gainoffunction-e6]. The second is an August 2026 commentary by CASRAI, a research administration organization (a third-party interpretation, not the government text): it says a new policy replacing the 2024 policy was released in July 2026[^casrai2026highrisk-e1][^casrai2026highrisk-e2]; as it reports, PIs must state in writing which category their research falls into before submitting a proposal[^casrai2026highrisk-e3], ongoing work that may be "dangerous gain-of-function research" must stop immediately with notice to the funding agency within 24 hours[^casrai2026highrisk-e4], and routine, low-risk gain-of-function work is not the target[^casrai2026highrisk-e5]. We cannot confirm whether these reports are accurate or whether things have changed since; if you do this kind of research in the US, follow NIH's official notices and your institution's biosafety office `[Our analysis]`.

### Genetically modified organisms: the Cartagena Protocol on Biosafety

This is an international treaty under the Convention on Biological Diversity, adopted in 2000. Its objective is to ensure adequate protection in the safe transfer, handling, and use of "living modified organisms" that may harm biological diversity, taking into account risks to human health, with a focus on transboundary movement[^cbd2000cartagena-e1]. A **living modified organism** (LMO) is any living organism with a novel combination of genetic material obtained through modern biotechnology[^cbd2000cartagena-e3]; genetically modified strains, crops, and animals all count `[Our analysis]`.

The treaty binds the countries that have joined it (the Parties), which implement it through their own legal and administrative measures[^cbd2000cartagena-e2]; whether your country has joined and how it implements the treaty is set by your national law `[Our analysis]`. The most useful thing for a researcher is to tell two situations apart:

- **Contained use**: use in a facility where specific measures limit the organism's contact with, and impact on, the external environment[^cbd2000cartagena-e5]. Shipments destined for contained use under the importing side's standards do not go through the "advance informed agreement" procedure[^cbd2000cartagena-e6], but the accompanying documentation must identify them as LMOs and give safe-handling requirements and consignee details[^cbd2000cartagena-e8]. Before exchanging live genetically modified strains, cells, or seeds with a lab abroad, ask your institution how to handle the paperwork `[Our analysis]`.
- **Intentional introduction into the environment**: the first transboundary movement of an LMO intended for release into the importing country's environment must go through the "advance informed agreement" procedure beforehand[^cbd2000cartagena-e7]. Field applications in environmental biotechnology and field trials in agricultural biotechnology may both fall into this category `[Our analysis]`.

### Measurement and description: report so others can reproduce

Results in biotechnology are often a single number (expression level, yield, fluorescence intensity), and how that number was measured determines whether it means anything `[Our analysis]`. **Report quantitative PCR according to MIQE.** Real-time quantitative PCR (qPCR; PCR is the polymerase chain reaction, used to amplify DNA) is a common way to measure amounts of nucleic acid `[Our analysis]`. Bustin and colleagues' 2009 MIQE guidelines (Minimum Information for Publication of Quantitative Real-Time PCR Experiments) point out that many papers give too few experimental details for readers to evaluate or repeat the work[^bustin2009miqe-e1]. MIQE provides a checklist to accompany submissions[^bustin2009miqe-e2]; items marked "essential" are those reviewers need to evaluate the work and others need to repeat it[^bustin2009miqe-e8]. Some key points:

- **Normalizing to a single reference gene** (a gene used to correct for differences between samples) is unacceptable unless there is evidence that its expression is stable under your experimental conditions; the number and choice of reference genes must be determined experimentally[^bustin2009miqe-e5].
- **Include a no-template control** (a blank reaction with no sample nucleic acid added) on every plate, and set exclusion criteria in advance[^bustin2009miqe-e6].
- **Don't report results below the limit of detection**; reporting "0" is meaningless[^bustin2009miqe-e7]. Most RNA quantification is relative, not absolute[^bustin2009miqe-e9].
- **Disclose all reagents, sequences, and analysis methods**[^bustin2009miqe-e3]; reporting results from unvalidated commercial assays is discouraged[^bustin2009miqe-e10].

According to a 2025 editorial-style article by Bustin, the first author of MIQE, a revised MIQE 2.0 has been published, with simplified and updated reporting requirements[^bustin2025miqe-e1][^bustin2025miqe-e2]. We have not read the MIQE 2.0 text itself; the checklist items above come from the 2009 version, so use the latest version when you submit. The article also says compliance remains uneven, citing problems such as assumed amplification efficiencies and unvalidated reference genes[^bustin2025miqe-e3][^bustin2025miqe-e4].

**Calibrate fluorescence and similar readings.** Beal and colleagues reported in 2016 the first large-scale multi-lab study in synthetic biology: through the 2014 and 2015 International Genetically Engineered Machine competition (iGEM), 88 institutions worldwide measured the fluorescence of three constructs (artificially assembled DNA pieces) in *E. coli*[^beal2016reproducibility-e1]. Few could measure absolute fluorescence; they could only compare ratios[^beal2016reproducibility-e2]. The host strain did not affect the ratios, but the instrument used did[^beal2016reproducibility-e3]. The authors say calibration was done so inconsistently that it was no better than using arbitrary units[^beal2016reproducibility-e4], and call for calibrated measurements in standard units to reduce the "unwritten" differences in practice[^beal2016reproducibility-e5].

**Designs can be described in a standard format too.** The Synthetic Biology Open Language (SBOL) is a community-developed data standard for recording biological designs in machine-readable form[^mclaughlin2020sbol3-e1]. According to its developers' 2020 article, it is the format the journal *ACS Synthetic Biology* recommends for describing engineered nucleic acid constructs[^mclaughlin2020sbol3-e2]. When submitting to other journals, check whether they have requirements `[Our analysis]`.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, determined by its central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). Our sources support three strategies in biotechnology; they do not cover how Synthesis and the other strategies are used in this field. The grouping and the "What it looks like in biotechnology" column are our own synthesis; each standard speaks only for the area of the source in its footnote `[Our analysis]`.

| Strategy | What it looks like in biotechnology | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Designing and building engineered strains, cell lines, or plants, or developing a bioprocess and scaling it up step by step, iterating through many design-build-test rounds | Biological systems are often sensitive to small changes in cellular or environmental conditions (synthetic biology)[^beal2016reproducibility-e6], so record the construct, host, and conditions in full for every round; before claiming "industrial feasibility," know that most parameters change during scale-up and lab conditions cannot simply be copied (industrial microbial processes, from company authors' experience)[^crater2018scaleup-e3][^crater2018scaleup-e7] | [Bench experiment](../../06_methods/bench_experiment.md); for modeling, [Quantitative simulation](../../06_methods/simulation_study.md); for scale-up, [From shake flask to fermenter: scale-up](#from-shake-flask-to-fermenter-scale-up) above |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Working out mechanisms: knock out, overexpress, or mutate a gene, or add an inhibitor, and see whether the phenotype, yield, or pathway changes accordingly, to show "this factor causes it" | The points below come from MDAR (Materials Design Analysis Reporting), a life-science reporting framework published in 2021 by editors from several publishers and the US Center for Open Science[^macleod2021mdar-e2]; it is aimed at exploratory laboratory research and does not replace existing specialized standards (such as MIQE above)[^macleod2021mdar-e1]. State how many times the experiment was independently performed[^macleod2021mdar-e3], and whether the replicates are biological (different experimental units) or technical (the same unit measured several times)[^macleod2021mdar-e4]; if there are only technical replicates, say that the error reflects procedural rather than biological variation[^macleod2021mdar-e7]; define control groups clearly, and justify any missing controls[^macleod2021mdar-e6]; decide how to handle outliers before running the experiment[^macleod2021mdar-e9]; check cell lines against the International Cell Line Authentication Committee (ICLAC) register of misidentified cell lines, avoid those on it, and authenticate the others regularly[^macleod2021mdar-e10]. For how to define the experimental unit, how to randomize, and why exploratory results need confirmatory experiments, see the bench experiment page | [Bench experiment](../../06_methods/bench_experiment.md) ([exploratory and confirmatory](../../06_methods/bench_experiment.md#1-what-this-kind-of-research-is-and-when-to-use-it), [finding the experimental unit](../../06_methods/bench_experiment.md#step-2-draw-the-hierarchy-and-find-the-experimental-unit)); for parts involving animals, [Preclinical animal studies](../../06_methods/preclinical_animal_study.md) |
| [Measurement](../../05_research-strategies/measure.md) | Measuring expression levels, yields, or fluorescence intensity, developing new assays, or having several labs measure the same samples for comparison | Report qPCR against the MIQE checklist; "essential" items are those reviewers need to evaluate the work and others need to repeat it[^bustin2009miqe-e8]; using a single unvalidated reference gene is unacceptable[^bustin2009miqe-e5]; fluorescence readings depend on the instrument[^beal2016reproducibility-e3], so use calibrated measurements in standard units[^beal2016reproducibility-e5] | [Experimental measurement](../../06_methods/experimental_measurement.md), [Replication studies](../../06_methods/replication.md); [Measurement and description: report so others can reproduce](#measurement-and-description-report-so-others-can-reproduce) above |

**How to use this table** `[Our analysis]`: many projects involve several strategies. For example, you build a new strain (Building and improving), report its yield data to measurement standards, and then knock out a gene to explain why yield went up (Causal explanation). Choose the main strategy from your central claim, and hold each other part to its own standards; for parts involving animals or humans, follow the methods listed in the next section and the rules on the [clinical medicine page](../clinical-medicine/README.md).

---

## Research methods common in this field

Biotechnology has no method page of its own; the methods it uses are cross-disciplinary, listed in the [research types overview](../../06_methods/README.md). The mapping below is our own `[Our analysis]`.

- **Building strains and cell lines, developing bioprocesses**: see [Bench experiments (wet lab)](../../06_methods/bench_experiment.md). The thinking is close to [Engineering research](../computer-science/practices/engineering_research.md) in computer science, and for optimizing conditions you can draw on [Optimization studies](../computer-science/practices/optimization_study.md); the difference is that you may need approval before you start.
- **Mechanism studies** (knockout, overexpression, inhibitor experiments): also [Bench experiment](../../06_methods/bench_experiment.md); for reporting requirements, see the "Causal explanation" row of the table in the previous section.
- **Developing assays and measurement methods, multi-lab comparisons**: see [Experimental measurement](../../06_methods/experimental_measurement.md) and [Replication studies](../../06_methods/replication.md); the iGEM study is an example of a multi-lab comparison[^beal2016reproducibility-e1]. For modeling (metabolic models, fermentation process models), see [Quantitative simulation](../../06_methods/simulation_study.md).
- **Animal experiments and human trials**: see [Preclinical animal studies](../../06_methods/preclinical_animal_study.md) and [Randomized controlled trials](../../06_methods/randomized_controlled_trial.md). For omics analysis, see the [biological sciences page](../biological-sciences/README.md).

---

## Advice for newcomers

1. **Sort out the safety paperwork in the first week.** Find out what containment level your experiment needs, whether it must be approved or registered, and what training you need; in the US, for example, experiments requiring prior approval must not start before approval[^nih2024guidelines-e7].
2. **Report changes before you make them.** Changing the vector, host, or DNA source must be submitted to the committee for review in the US[^nih2024guidelines-e9]; elsewhere, ask the PI first too `[Our analysis]`.
3. **Think about dual-use risk when you start the project.** Use the WHO checklist to ask yourself: could the results be misused, and is there a safer way to do this[^who2022responsible-e7][^who2022responsible-e8].
4. **Ask your institution before sending or carrying live genetically modified material anywhere.** The Cartagena Protocol on Biosafety focuses on transboundary movement[^cbd2000cartagena-e1] and is implemented by the countries that have joined it through their own laws[^cbd2000cartagena-e2]; the actual procedures are set by your national law.
5. **Read the MIQE checklist before you do qPCR**, and design your controls and reference genes around it rather than filling it in at submission[^bustin2009miqe-e5][^bustin2009miqe-e6].
6. **Calibrate your readings and state the units.** The same construct can give different results on a different instrument[^beal2016reproducibility-e3].
7. **If your project is industry-oriented, think about scale early.** Consider whether a strain can be scaled up when you choose it[^crater2018scaleup-e5]; in your paper, state the scale at which results were obtained `[Our analysis]`.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Starting without approval because "I'm just cloning a gene" | In the US, experiments requiring prior approval must not start before approval[^nih2024guidelines-e7]; violations can affect funding for the whole institution[^nih2024guidelines-e4] |
| Switching host or vector midway without telling the biosafety committee | Changes to the protocol must also be submitted for review[^nih2024guidelines-e9] |
| Assuming a Risk Group 2 pathogen can always be handled at BSL-2 | Biosafety level is not the same as risk group; do a risk assessment based on the specific procedures[^cdc2020bmbl-e11][^cdc2020bmbl-e2] |
| Assuming that what works at small volume needs the same containment when scaled up | Large volumes and high concentrations may need additional measures[^cdc2020bmbl-e12]; in the US, containment above 10 liters is set by the committee[^nih2024guidelines-e13] |
| Treating the US BMBL as a regulation that applies everywhere | BMBL is a US advisory document, not a regulation[^cdc2020bmbl-e1]; local law applies in each country `[Our analysis]` |
| Using a single reference gene in qPCR without validating its stability | MIQE considers this unacceptable[^bustin2009miqe-e5] |
| Reporting "expression level = 0" | Results below the limit of detection should not be reported; "0" is meaningless[^bustin2009miqe-e7] |
| Reporting fluorescence only in arbitrary units, without stating the instrument and calibration | The instrument affects the results[^beal2016reproducibility-e3]; inconsistent calibration is no better than arbitrary units[^beal2016reproducibility-e4] |
| Claiming "ready for industrial production" because yield was high in a shake flask | Most parameters change during scale-up, and lab conditions cannot simply be copied[^crater2018scaleup-e3][^crater2018scaleup-e7] |

---

## Further reading

- **US CDC and NIH, BMBL 6th edition (2020)**: covers biosafety levels and risk assessment; Sections II and III are the place to start. It is a US advisory document, not a regulation.
- **US NIH Guidelines (April 2024 version)**: required reading for recombinant or synthetic nucleic acid research in the US; focus on Section III (experiment categories) and Section IV-B-7 (responsibilities of the PI). NIH says it is updating biosafety oversight, so check for the latest version.
- **WHO, Global guidance framework for the responsible use of the life sciences (2022)**: concepts of dual-use research and biorisk management; Box 6 in Section 5 is the checklist for researchers.
- **The text of the Cartagena Protocol on Biosafety**: the international rules on transboundary movement of genetically modified organisms, binding only on the Parties; this page uses Articles 1–3, 6, 7, and 18.
- **Bustin et al. 2009, MIQE (Clinical Chemistry)**: the reporting checklist to follow when doing qPCR; Table 1 is the checklist. We have not read the MIQE 2.0 text itself, so check the latest version when you submit.
- **Crater and Lievense 2018 (FEMS Microbiology Letters)**: two company authors on scaling up industrial microbial processes, drawn from their own experience.
- **Beal et al. 2016 (PLoS ONE)**: a worked example of a multi-lab study, showing why you need to calibrate and describe your measurement methods clearly.
- **Your institution's biosafety committee guidance and your country's laws**: most of the rules cited on this page are American; local rules take precedence.

[^cbd2000cartagena-e1]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 1. [Evidence](../../../sources/notes/cbd2000cartagena.md#e1)
[^cbd2000cartagena-e2]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 2.1. [Evidence](../../../sources/notes/cbd2000cartagena.md#e2)
[^cbd2000cartagena-e3]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 3(g). [Evidence](../../../sources/notes/cbd2000cartagena.md#e3)
[^cbd2000cartagena-e4]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 3(i). [Evidence](../../../sources/notes/cbd2000cartagena.md#e4)
[^cbd2000cartagena-e5]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 3(b). [Evidence](../../../sources/notes/cbd2000cartagena.md#e5)
[^cbd2000cartagena-e6]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 6.2. [Evidence](../../../sources/notes/cbd2000cartagena.md#e6)
[^cbd2000cartagena-e7]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 7.1. [Evidence](../../../sources/notes/cbd2000cartagena.md#e7)
[^cbd2000cartagena-e8]: Secretariat of the Convention on Biological Diversity 2000 (Cartagena Protocol on Biosafety), Article 18.2(b). [Evidence](../../../sources/notes/cbd2000cartagena.md#e8)
[^nih2024guidelines-e1]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section I-B. [Evidence](../../../sources/notes/nih2024guidelines.md#e1)
[^nih2024guidelines-e2]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section I-C-1-a-(1). [Evidence](../../../sources/notes/nih2024guidelines.md#e2)
[^nih2024guidelines-e3]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section I-D. [Evidence](../../../sources/notes/nih2024guidelines.md#e3)
[^nih2024guidelines-e4]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section I-D-1. [Evidence](../../../sources/notes/nih2024guidelines.md#e4)
[^nih2024guidelines-e5]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section IV-B-2-a-(1). [Evidence](../../../sources/notes/nih2024guidelines.md#e5)
[^nih2024guidelines-e6]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section IV-B-7. [Evidence](../../../sources/notes/nih2024guidelines.md#e6)
[^nih2024guidelines-e7]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section IV-B-7-a-(1). [Evidence](../../../sources/notes/nih2024guidelines.md#e7)
[^nih2024guidelines-e8]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section IV-B-7-a-(3). [Evidence](../../../sources/notes/nih2024guidelines.md#e8)
[^nih2024guidelines-e9]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section IV-B-7-c-(3). [Evidence](../../../sources/notes/nih2024guidelines.md#e9)
[^nih2024guidelines-e10]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section III-E. [Evidence](../../../sources/notes/nih2024guidelines.md#e10)
[^nih2024guidelines-e11]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section III-E. [Evidence](../../../sources/notes/nih2024guidelines.md#e11)
[^nih2024guidelines-e12]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section III-F. [Evidence](../../../sources/notes/nih2024guidelines.md#e12)
[^nih2024guidelines-e13]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section III-D-6. [Evidence](../../../sources/notes/nih2024guidelines.md#e13)
[^nih2024guidelines-e14]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), page header. [Evidence](../../../sources/notes/nih2024guidelines.md#e14)
[^nih2024guidelines-e15]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section I-A-1-a. [Evidence](../../../sources/notes/nih2024guidelines.md#e15)
[^nih2024guidelines-e16]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section I-C-1-b-(3). [Evidence](../../../sources/notes/nih2024guidelines.md#e16)
[^nih2024guidelines-e17]: US National Institutes of Health (NIH) 2024 (NIH Guidelines), Section II-A-3. [Evidence](../../../sources/notes/nih2024guidelines.md#e17)
[^cdc2020bmbl-e1]: US CDC & NIH 2020 (BMBL, 6th edition), Foreword. [Evidence](../../../sources/notes/cdc2020bmbl.md#e1)
[^cdc2020bmbl-e2]: US CDC & NIH 2020 (BMBL, 6th edition), Foreword. [Evidence](../../../sources/notes/cdc2020bmbl.md#e2)
[^cdc2020bmbl-e3]: US CDC & NIH 2020 (BMBL, 6th edition), Section II. [Evidence](../../../sources/notes/cdc2020bmbl.md#e3)
[^cdc2020bmbl-e4]: US CDC & NIH 2020 (BMBL, 6th edition), Section II. [Evidence](../../../sources/notes/cdc2020bmbl.md#e4)
[^cdc2020bmbl-e5]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Levels. [Evidence](../../../sources/notes/cdc2020bmbl.md#e5)
[^cdc2020bmbl-e6]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Level 1. [Evidence](../../../sources/notes/cdc2020bmbl.md#e6)
[^cdc2020bmbl-e7]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Level 2. [Evidence](../../../sources/notes/cdc2020bmbl.md#e7)
[^cdc2020bmbl-e8]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Level 2. [Evidence](../../../sources/notes/cdc2020bmbl.md#e8)
[^cdc2020bmbl-e9]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Level 3. [Evidence](../../../sources/notes/cdc2020bmbl.md#e9)
[^cdc2020bmbl-e10]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Level 4. [Evidence](../../../sources/notes/cdc2020bmbl.md#e10)
[^cdc2020bmbl-e11]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Levels. [Evidence](../../../sources/notes/cdc2020bmbl.md#e11)
[^cdc2020bmbl-e12]: US CDC & NIH 2020 (BMBL, 6th edition), Section III, Biosafety Levels. [Evidence](../../../sources/notes/cdc2020bmbl.md#e12)
[^cdc2020bmbl-e13]: US CDC & NIH 2020 (BMBL, 6th edition), Section I. [Evidence](../../../sources/notes/cdc2020bmbl.md#e13)
[^who2022responsible-e1]: WHO 2022, Glossary. [Evidence](../../../sources/notes/who2022responsible.md#e1)
[^who2022responsible-e2]: WHO 2022, Glossary. [Evidence](../../../sources/notes/who2022responsible.md#e2)
[^who2022responsible-e3]: WHO 2022, Glossary. [Evidence](../../../sources/notes/who2022responsible.md#e3)
[^who2022responsible-e4]: WHO 2022, Glossary. [Evidence](../../../sources/notes/who2022responsible.md#e4)
[^who2022responsible-e5]: WHO 2022, Executive summary. [Evidence](../../../sources/notes/who2022responsible.md#e5)
[^who2022responsible-e6]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e6)
[^who2022responsible-e7]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e7)
[^who2022responsible-e8]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e8)
[^who2022responsible-e9]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e9)
[^who2022responsible-e10]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e10)
[^who2022responsible-e11]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e11)
[^who2022responsible-e12]: WHO 2022, Section 5.3, Box 6. [Evidence](../../../sources/notes/who2022responsible.md#e12)
[^crs2025gainoffunction-e1]: Congressional Research Service (CRS) 2025 (IN12554), paragraph 1. [Evidence](../../../sources/notes/crs2025gainoffunction.md#e1)
[^crs2025gainoffunction-e3]: Congressional Research Service (CRS) 2025 (IN12554), paragraph 1. [Evidence](../../../sources/notes/crs2025gainoffunction.md#e3)
[^crs2025gainoffunction-e4]: Congressional Research Service (CRS) 2025 (IN12554), paragraph 2. [Evidence](../../../sources/notes/crs2025gainoffunction.md#e4)
[^crs2025gainoffunction-e5]: Congressional Research Service (CRS) 2025 (IN12554), paragraph 3. [Evidence](../../../sources/notes/crs2025gainoffunction.md#e5)
[^crs2025gainoffunction-e6]: Congressional Research Service (CRS) 2025 (IN12554), 4th paragraph from the end. [Evidence](../../../sources/notes/crs2025gainoffunction.md#e6)
[^casrai2026highrisk-e1]: CASRAI editors 2026, TL;DR. [Evidence](../../../sources/notes/casrai2026highrisk.md#e1)
[^casrai2026highrisk-e2]: CASRAI editors 2026, TL;DR. [Evidence](../../../sources/notes/casrai2026highrisk.md#e2)
[^casrai2026highrisk-e3]: CASRAI editors 2026, New Institutional Obligations. [Evidence](../../../sources/notes/casrai2026highrisk.md#e3)
[^casrai2026highrisk-e4]: CASRAI editors 2026, New Institutional Obligations. [Evidence](../../../sources/notes/casrai2026highrisk.md#e4)
[^casrai2026highrisk-e5]: CASRAI editors 2026, Two Categories of Covered Research. [Evidence](../../../sources/notes/casrai2026highrisk.md#e5)
[^bustin2009miqe-e1]: Bustin et al. 2009 (MIQE), Abstract. [Evidence](../../../sources/notes/bustin2009miqe.md#e1)
[^bustin2009miqe-e2]: Bustin et al. 2009 (MIQE), Abstract. [Evidence](../../../sources/notes/bustin2009miqe.md#e2)
[^bustin2009miqe-e3]: Bustin et al. 2009 (MIQE), Abstract. [Evidence](../../../sources/notes/bustin2009miqe.md#e3)
[^bustin2009miqe-e5]: Bustin et al. 2009 (MIQE), 8.1 Normalization. [Evidence](../../../sources/notes/bustin2009miqe.md#e5)
[^bustin2009miqe-e6]: Bustin et al. 2009 (MIQE), 7.3 Controls and quantification calibrators. [Evidence](../../../sources/notes/bustin2009miqe.md#e6)
[^bustin2009miqe-e7]: Bustin et al. 2009 (MIQE), 2.1 Analytical sensitivity. [Evidence](../../../sources/notes/bustin2009miqe.md#e7)
[^bustin2009miqe-e8]: Bustin et al. 2009 (MIQE), Conclusions. [Evidence](../../../sources/notes/bustin2009miqe.md#e8)
[^bustin2009miqe-e9]: Bustin et al. 2009 (MIQE), 2. Conceptual Considerations. [Evidence](../../../sources/notes/bustin2009miqe.md#e9)
[^bustin2009miqe-e10]: Bustin et al. 2009 (MIQE), 2. Conceptual Considerations. [Evidence](../../../sources/notes/bustin2009miqe.md#e10)
[^bustin2025miqe-e1]: Bustin 2025 (IJMS), para. 1. [Evidence](../../../sources/notes/bustin2025miqe.md#e1)
[^bustin2025miqe-e2]: Bustin 2025 (IJMS), para. 2. [Evidence](../../../sources/notes/bustin2025miqe.md#e2)
[^bustin2025miqe-e3]: Bustin 2025 (IJMS), para. 3. [Evidence](../../../sources/notes/bustin2025miqe.md#e3)
[^bustin2025miqe-e4]: Bustin 2025 (IJMS), para. 5. [Evidence](../../../sources/notes/bustin2025miqe.md#e4)
[^beal2016reproducibility-e1]: Beal et al. 2016, Abstract. [Evidence](../../../sources/notes/beal2016reproducibility.md#e1)
[^beal2016reproducibility-e2]: Beal et al. 2016, Abstract. [Evidence](../../../sources/notes/beal2016reproducibility.md#e2)
[^beal2016reproducibility-e3]: Beal et al. 2016, Abstract. [Evidence](../../../sources/notes/beal2016reproducibility.md#e3)
[^beal2016reproducibility-e4]: Beal et al. 2016, Results, Absolute vs. Relative Units. [Evidence](../../../sources/notes/beal2016reproducibility.md#e4)
[^beal2016reproducibility-e5]: Beal et al. 2016, Introduction. [Evidence](../../../sources/notes/beal2016reproducibility.md#e5)
[^beal2016reproducibility-e6]: Beal et al. 2016, Introduction. [Evidence](../../../sources/notes/beal2016reproducibility.md#e6)
[^crater2018scaleup-e1]: Crater & Lievense 2018, What is scale-up and why does it matter? [Evidence](../../../sources/notes/crater2018scaleup.md#e1)
[^crater2018scaleup-e2]: Crater & Lievense 2018, What is scale-up and why does it matter? [Evidence](../../../sources/notes/crater2018scaleup.md#e2)
[^crater2018scaleup-e3]: Crater & Lievense 2018, Begin with the end in mind. [Evidence](../../../sources/notes/crater2018scaleup.md#e3)
[^crater2018scaleup-e4]: Crater & Lievense 2018, Begin with the end in mind. [Evidence](../../../sources/notes/crater2018scaleup.md#e4)
[^crater2018scaleup-e5]: Crater & Lievense 2018, Key challenges and improvement opportunities. [Evidence](../../../sources/notes/crater2018scaleup.md#e5)
[^crater2018scaleup-e6]: Crater & Lievense 2018, A road map for successful scale-up. [Evidence](../../../sources/notes/crater2018scaleup.md#e6)
[^crater2018scaleup-e7]: Crater & Lievense 2018, Key considerations for fermentation scale-up. [Evidence](../../../sources/notes/crater2018scaleup.md#e7)
[^crater2018scaleup-e8]: Crater & Lievense 2018, Table 1. [Evidence](../../../sources/notes/crater2018scaleup.md#e8)
[^crater2018scaleup-e9]: Crater & Lievense 2018, A road map for successful scale-up. [Evidence](../../../sources/notes/crater2018scaleup.md#e9)
[^crater2018scaleup-e10]: Crater & Lievense 2018, Guiding principles for process scale-up. [Evidence](../../../sources/notes/crater2018scaleup.md#e10)
[^mclaughlin2020sbol3-e1]: McLaughlin et al. 2020, Abstract. [Evidence](../../../sources/notes/mclaughlin2020sbol3.md#e1)
[^mclaughlin2020sbol3-e2]: McLaughlin et al. 2020, Introduction. [Evidence](../../../sources/notes/mclaughlin2020sbol3.md#e2)
[^macleod2021mdar-e1]: Macleod et al. 2021 (MDAR, PNAS), main text. [Evidence](../../../sources/notes/macleod2021mdar.md#e1)
[^macleod2021mdar-e2]: Macleod et al. 2021 (MDAR, PNAS), main text and competing interests statement. [Evidence](../../../sources/notes/macleod2021mdar.md#e2)
[^macleod2021mdar-e3]: Macleod et al. 2021 (MDAR), Elaboration §2.4. [Evidence](../../../sources/notes/macleod2021mdar.md#e3)
[^macleod2021mdar-e4]: Macleod et al. 2021 (MDAR), Elaboration §2.4. [Evidence](../../../sources/notes/macleod2021mdar.md#e4)
[^macleod2021mdar-e6]: Macleod et al. 2021 (MDAR), Elaboration §2.4. [Evidence](../../../sources/notes/macleod2021mdar.md#e6)
[^macleod2021mdar-e7]: Macleod et al. 2021 (MDAR), Elaboration §3.2. [Evidence](../../../sources/notes/macleod2021mdar.md#e7)
[^macleod2021mdar-e9]: Macleod et al. 2021 (MDAR), Elaboration §2.3. [Evidence](../../../sources/notes/macleod2021mdar.md#e9)
[^macleod2021mdar-e10]: Macleod et al. 2021 (MDAR), Elaboration §1.4. [Evidence](../../../sources/notes/macleod2021mdar.md#e10)
[^eu2009contained-e2]: EU Directive 2009/41/EC (2009), Article 2(c). [Evidence](../../../sources/notes/eu2009contained.md#e2)
[^eu2009contained-e3]: EU Directive 2009/41/EC (2009), Article 4(2)–(3). [Evidence](../../../sources/notes/eu2009contained.md#e3)
[^eu2009contained-e4]: EU Directive 2009/41/EC (2009), Article 4(3). [Evidence](../../../sources/notes/eu2009contained.md#e4)
[^eu2009contained-e5]: EU Directive 2009/41/EC (2009), Article 4(4). [Evidence](../../../sources/notes/eu2009contained.md#e5)
[^eu2009contained-e6]: EU Directive 2009/41/EC (2009), Article 9(2). [Evidence](../../../sources/notes/eu2009contained.md#e6)
[^npc2020biosecurity-e1]: Biosecurity Law of the People's Republic of China 2020 (English text from the National People's Congress), Order of the President No. 58. [Evidence](../../../sources/notes/npc2020biosecurity.md#e1)
[^npc2020biosecurity-e2]: Biosecurity Law 2020 (English text), Article 36. [Evidence](../../../sources/notes/npc2020biosecurity.md#e2)
[^npc2020biosecurity-e3]: Biosecurity Law 2020 (English text), Article 38. [Evidence](../../../sources/notes/npc2020biosecurity.md#e3)
[^npc2020biosecurity-e4]: Biosecurity Law 2020 (English text), Article 45. [Evidence](../../../sources/notes/npc2020biosecurity.md#e4)
[^npc2024legislature-e1]: National People's Congress English website, news of April 28, 2024 (Xinhua), paras. 1–2. [Evidence](../../../sources/notes/npc2024legislature.md#e1)
[^npc2024legislature-e2]: National People's Congress English website, news of April 28, 2024 (Xinhua), photo caption. [Evidence](../../../sources/notes/npc2024legislature.md#e2)
