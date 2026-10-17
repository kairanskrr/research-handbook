# Chemical engineering: field overview

This page explains how research actually runs in chemical engineering: you measure reactions and materials in the lab, calculate processes with models, and also have to think about scale-up, safety, cost, and environmental impact. Chemical engineering overlaps heavily with chemistry; for material that leans toward chemistry itself, see the [Chemistry page](../chemistry/README.md). For the research strategies this field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). This page covers only what is specific to this field.

**After reading this page, you should be able to:**

- explain what stands between a lab result and industrial scale, and why scale-up is a research problem in its own right;
- do a hazard assessment before you start an experiment, and know which problems one university chemistry lab accident exposed;
- report kinetic and catalytic data so that others can compare them, following the recommendations of one group of catalysis researchers;
- read and transparently report techno-economic and life cycle assessments, using a set of guidelines from carbon capture and utilization as an example;
- sort out confidentiality, patents, and publication in advance when you work with a company.

---

## How research works in this field

### What gets studied: from molecular-scale reactions to whole processes

Chemical engineering research covers a very wide range. Take *Industrial & Engineering Chemistry Research* (I&EC Research below), a journal of the American Chemical Society (ACS): it sorts papers into topical sections such as kinetics, catalysis, and reaction engineering; materials and interfaces; process systems engineering; separations; and thermodynamics, transport, and fluid mechanics[^acsiecrauthorguide-e2]. It also accepts papers on process design and development, including modeling and scale-up methods[^acsiecrauthorguide-e1]. This is only one journal's classification, but it shows that the objects of study range from reactions and materials themselves to entire processes made up of many units of equipment.

A typical project often combines several kinds of work: measuring reaction rates, selectivity, or physical properties in the lab; building a model from those data; then using the model to design, optimize, or evaluate a process.

### How far a lab result is from industry: scale-up

**Scale-up** means taking a process that runs on a few grams or milliliters in the lab up to pilot-plant and eventually industrial scale. This is not simply "making more":

- **Catalyst performance gets measured again in larger equipment.** Bligaard and colleagues (a 2016 perspective by a group of researchers funded by the US Department of Energy's catalysis science program) note that catalyst performance is often measured in banks of nearly identical bench-scale reactors and in pilot-scale reactors[^bligaard2016benchmarking-e3].
- **Lab-scale data skew the estimates.** A life cycle assessment guideline written specifically for carbon capture and utilization (technologies that collect carbon dioxide and turn it into products) points out that processes at low technology readiness have not yet been heat-integrated or optimized, use more energy and solvent than they will later, and lack auxiliary steps such as product purification after the reaction. Assessments based on lab-scale data can therefore either overestimate or underestimate the environmental impact[^muller2020lca-e7]. The companion techno-economic assessment guideline likewise asks you to account for learning curves and improvements when technology readiness is low[^zimmermann2020tea-e12].
- **When the quantity changes, the hazard changes too.** See the accident below under [lab safety](#lab-safety-is-part-of-research-do-a-hazard-assessment-before-you-start), which happened after a synthesis was scaled up to about 10 grams[^csb2011texastech-e2].

So when a paper says a result "has industrial potential," it should state the scale at which the result was obtained and which conclusions might change on scale-up.

### Modeling and simulation: pass the mass and energy balance check first

Process modeling and simulation are standard tools in this field. A simple check that often gets skipped: does the concept make sense at all? The carbon capture and utilization techno-economic assessment guideline mentioned above requires a "sanity check" before any assessment, checking kinetics and the mass and energy balances; the concept must not violate the laws of thermodynamics[^zimmermann2020tea-e5]. That guideline covers only carbon capture and utilization, but we think the same check is worth doing in process modeling generally. For how to verify and validate a simulation study, see [Quantitative simulation](../../06_methods/simulation_study.md) under Research types.

### Publishing: mostly journals, so read your target journal's requirements

Our sources have no figures on how conferences and journals compare in chemical engineering. The points below use one journal, I&EC Research, as the example; if you submit elsewhere, follow that journal's author guidelines.

- **Reporting data alone is not enough.** I&EC Research states that papers that only report data or computational results will be rejected[^acsiecrauthorguide-e3]. Manuscripts whose conclusions lack clear significance and novelty, or whose readership is too narrow, are the most likely to be rejected by the editor before review[^acsiecrauthorguide-e4].
- **Preprints are allowed, but say so.** The journal accepts authors posting the submitted manuscript on a preprint server, but you must state this clearly in your cover letter[^acsiecrauthorguide-e5].
- **General rules on authorship and peer review** are in the Writing and publishing chapter [Choosing a venue and submitting](../../03_write-and-publish/02_venue-and-submission.md). Our sources do not cover authorship conventions specific to chemical engineering.

### Working with companies: plan confidentiality, patents, and publication in advance

Many chemical engineering projects are tied to industrial applications and may involve collaboration with companies. The sources show a few concrete effects:

- **Company data are often not public.** The carbon capture and utilization techno-economic assessment guideline notes that companies reportedly run these assessments against internal standards but usually do not publish them[^zimmermann2020tea-e2]. So the public data you can compare against may be limited.
- **Settle patents before you publish.** I&EC Research requires authors to resolve patent and intellectual property issues before first publication; the journal will not delay publication for them[^acsiecrauthorguide-e10].
- **Tell your university first, then disclose or collaborate.** According to guidance from UC Berkeley, you should submit an invention disclosure to the university before working with a company and at least 1 to 2 months before any public disclosure[^berkeleydisclose-e1][^berkeleydisclose-e2]; once the invention is public, you lose the right to apply for a patent in most countries outside the US[^berkeleydisclose-e4]. **Rules differ by country and institution; follow your own institution's**. For details, see [Electrical and electronic engineering: publish or patent](../electrical-engineering/README.md#publish-or-patent-the-us-as-the-example).

---

## How this field differs from others

The table below is our own summary, meant to help you spot the differences quickly; it is not a strict division between fields.

| | Chemical engineering | Chemistry | Computer science |
|---|---|---|---|
| Questions it cares about | Beyond "will it react," also scale-up, cost, energy use, and environmental impact | Molecules, reactions, and materials themselves (see the [Chemistry page](../chemistry/README.md)) | Mainly algorithms, systems, and software |
| Where results come from | Lab measurements and process modeling and simulation, often combined | Mainly lab synthesis and characterization | Mainly experiments on code, systems, and data |
| How comparison works | Reaction conditions, conversion, system boundaries, and other assumptions have to be aligned (see below) | Overlaps with chemical engineering, for example in catalysis | Public benchmark datasets and evaluation procedures (see [Benchmarking](../computer-science/practices/benchmarking.md)) |
| Safety | Experiments can carry hazards such as explosion and toxicity; assess them before you start | Equally important | Usually no physical lab hazards |
| Ties to industry | Frequent collaboration; data and procedures may be bound by confidentiality | Depends on the area | Depends on the area |

---

## Norms and reporting standards in this field

### Professional ethics: the AIChE code as an example

The Code of Ethics of the American Institute of Chemical Engineers (AIChE) was adopted by the institute's Board of Directors and binds its members[^aichecodeethics-e1]. Even if you are not a member or not in the US, you can use it as a reference. The points most relevant to research:

- hold paramount the safety, health, and welfare of the public, and protect the environment[^aichecodeethics-e2];
- formally advise your employer or client if your work could harm the health or safety of colleagues or the public[^aichecodeethics-e3];
- seek out criticism of your work, and be objective and truthful in the opinions and information you give[^aichecodeethics-e4][^aichecodeethics-e5];
- avoid conflicts of interest and never disclose confidential information[^aichecodeethics-e6], which matters especially when you work with a company.

For the general rules of research integrity, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md) under Throughout the project.

### Lab safety is part of research: do a hazard assessment before you start

**A university lab accident.** The US Chemical Safety and Hazard Investigation Board (Chemical Safety Board, CSB), the federal agency that investigates chemical accidents, investigated this case: in January 2010, a compound a graduate student was handling in the Department of Chemistry and Biochemistry at Texas Tech University exploded. He lost three fingers, burned his hands and face, and injured one eye[^csb2011texastech-e1]. The accident happened in a chemistry department, not a chemical engineering department; it is here because its lessons apply to anyone doing chemical experiments. The problems the investigation report lists include:

- **The scale-up bypassed the principal investigators.** The students scaled the synthesis up to about 10 grams without consulting either of the two principal investigators[^csb2011texastech-e2]; they assumed that protective measures that worked for small amounts would work just as well for larger ones[^csb2011texastech-e3].
- **The safety limit was only spoken.** The limit of no more than 100 milligrams per synthesis was communicated only verbally[^csb2011texastech-e4], and none of the students interviewed said they knew of this strict upper limit[^csb2011texastech-e5].
- **No formal hazard assessment was done**[^csb2011texastech-e6]. A hazard assessment is an organized effort to identify and analyze how serious the hazardous situations in a process or activity are[^csb2011texastech-e7].
- **A near miss was never shared.** Earlier, a student in the same group had used the wrong units and made an excess of energetic material[^csb2011texastech-e12], but this was not reported to anyone outside the group[^csb2011texastech-e13].
- **Group meetings skipped safety, and records were incomplete.** Weekly group meetings focused on results, not on how the work was actually done or its safety implications[^csb2011texastech-e14]; lab notebooks were undated and did not always record quantities[^csb2011texastech-e15]; wearing goggles was treated as a personal choice[^csb2011texastech-e16].

**What this means for you.** The investigating agency concluded that the standards of the chemical process industry cannot all be transferred to university labs, but borrowing the lessons that do apply is useful[^csb2011texastech-e8]; existing hazard assessment standards are written for industrial settings and cannot be applied wholesale to academic research labs[^csb2011texastech-e9]. The lessons it drew include: you need written procedures and training specific to the research being done[^csb2011texastech-e10]; and near misses become chances to improve only if they are recorded, tracked, and communicated[^csb2011texastech-e11]. For you personally, this means: do a hazard assessment before you start, check with the person in charge before you change quantities or conditions, write safety requirements down, and report near misses. Which assessment method to use and which approvals you need depend on your institution's and your country's rules.

**Put it in the paper.** I&EC Research, for example, asks authors to clearly highlight any unexpected, new, or significant hazards and risks in the work, in the experimental section for full papers[^acsiecrauthorguide-e9].

### Catalytic and kinetic data: how to report them so others can compare

The practices below come from a 2016 perspective by Bligaard and colleagues. The authors state that the recommendations represent only the named authors and come from discussions among some researchers in the US Department of Energy's catalysis science program, discussions that did not aim at consensus[^bligaard2016benchmarking-e2]. So what follows is one group of authors' view, not an industry or journal standard. It is about catalysis research, but in our view the principle that "you can only compare once the conditions are aligned" also applies to other reaction data.

**Why comparison is hard.** In catalysis research, the key performance measures are activity, selectivity, and deactivation[^bligaard2016benchmarking-e1]. But in heterogeneous catalysis, the best conditions for one catalyst may be poor for another, and active sites can change during testing[^bligaard2016benchmarking-e7]. In molecular catalysis, repeating a reaction from the literature may give activity far below the reported value, or none at all, possibly because of unreported differences in reagents and procedures[^bligaard2016benchmarking-e10].

**What the authors recommend you report** (the points below come from the heterogeneous, molecular, computational, and electrocatalysis sections of the original paper; read the section for your own area):

1. **Measure intrinsic rates.** An intrinsic rate is a rate that reflects only the reaction itself, free of interference from heat and mass transfer. Measurements should be accurate and reproducible, free of heat and mass transfer limitations, and cover a wide range of conversions[^bligaard2016benchmarking-e5]; verify that there are no heat transfer, mass transfer, or mixing effects[^bligaard2016benchmarking-e12]. Turnover frequency (the reaction rate normalized per active site) must be based on rate measurements, not on the conversion at a single point in time[^bligaard2016benchmarking-e6].
2. **Show how you calculated it.** State how turnover number and turnover frequency were calculated from the raw data, and how active sites were counted or estimated[^bligaard2016benchmarking-e14].
3. **Pair selectivity with conversion.** Report conversion whenever you report selectivity[^bligaard2016benchmarking-e11]; when comparing the selectivity of several catalysts, measure them at the same conversion[^bligaard2016benchmarking-e15]. Check the mass balance[^bligaard2016benchmarking-e13].
4. **Include controls.** Compare against an accepted or state-of-the-art catalyst under the same conditions[^bligaard2016benchmarking-e17]; run a control experiment without catalyst[^bligaard2016benchmarking-e18].
5. **Report stability, but with the right method.** Recycling experiments that measure yield only at high conversion do not prove a catalyst is stable[^bligaard2016benchmarking-e16]; accelerated aging tests are risky when you do not know the cause of deactivation[^bligaard2016benchmarking-e9].
6. **For computational studies, make input and output files public**[^bligaard2016benchmarking-e19]. Electrocatalysis has its own normalization requirements, for example normalizing current by several different parameters separately[^bligaard2016benchmarking-e20]; if you work in this area, read the original paper.

The authors also recommend that several research groups collaborate on blind, round-robin measurements of the same set of samples, to determine realistic error bars[^bligaard2016benchmarking-e8].

### Techno-economic and life cycle assessment: state your assumptions, or the conclusions cannot be trusted

**Techno-economic assessment** estimates how much a process costs and whether it can make money; **life cycle assessment** calculates the environmental impact of a product or service over its whole life cycle[^muller2020lca-e2]. Some chemical engineering papers use them to argue that a new process is worth pursuing.

The rules below come from a set of guidelines led by the Global CO2 Initiative (University of Michigan, US) and other institutions, written for carbon capture and utilization technologies. The techno-economic assessment part drew on input from more than 50 experts from industry, academia, and policy[^zimmermann2020tea-e4]; more than 40 experts took part in the life cycle assessment part[^muller2020lca-e1]. Other technology areas can use them as a reference, but they are not a general standard.

**How big the problem is.** The guideline authors point out that techno-economic assessments in this area have no accepted standard, often compare things that are not comparable, and lack transparency[^zimmermann2020tea-e1]; life cycle assessment studies in this area often cannot be compared with each other because they use different functional units (the reference basis for calculating environmental impact) or system boundaries (which steps are counted)[^muller2020lca-e4]. For carbon dioxide to methanol, for example, the literature reports carbon footprints anywhere from −1.7 to +9.7 kilograms of CO2 equivalent per kilogram[^muller2020lca-e5]; once the assumptions about electricity and carbon dioxide supply were harmonized, the spread narrowed so that all results had the same sign and could be clearly distinguished from fossil-based methanol[^muller2020lca-e6].

**What the guidelines require of carbon capture and utilization assessments (use them as a comparison when you assess other technologies):**

- **First state what you compare against, where, at what scale, and who commissioned the work.** The assessment goal should state the benchmark, location, time horizon, scale, and partners[^zimmermann2020tea-e6], as well as the commissioner and the authors[^zimmermann2020tea-e7].
- **Set the functional unit by use.** When the new product differs from the conventional one, compare them by performance in actual use; for example, compare detergents by washing performance, not by mass[^muller2020lca-e9].
- **Do not treat what you left out as free.** Excluding upstream processes does not mean carbon dioxide, hydrogen, or electricity can be costed at zero[^zimmermann2020tea-e8]; and in the base case, do not assume zero or negative electricity prices[^zimmermann2020tea-e14], or optimistic future hydrogen technologies or production scales larger than are feasible today[^zimmermann2020tea-e13].
- **Put everything on the same basis.** Convert data from different sources to the same base year and the same heating-value basis[^zimmermann2020tea-e11]. Keep "cost of CO2 captured" and "cost of CO2 avoided" apart[^zimmermann2020tea-e15].
- **Base conclusions on uncertainty and sensitivity analysis**[^zimmermann2020tea-e17]. Interpret indicators only after comparing them with a benchmark[^zimmermann2020tea-e18]. A negative life cycle assessment result is only a comparative result; it does not necessarily mean the product is carbon-neutral or carbon-negative[^muller2020lca-e10].
- **Report everything.** Give all assumptions, data, methods, results, and limitations[^zimmermann2020tea-e19][^muller2020lca-e11]; say so explicitly when confidential data were not available to you[^zimmermann2020tea-e10]; list who carried out the assessment and say whether it was reviewed[^zimmermann2020tea-e20].
- **If the data are not good enough, narrow the question.** If data quality cannot be raised to an adequate level, either adjust the goal and scope or stop the study[^zimmermann2020tea-e9]. At an early stage, life cycle assessment is most useful for finding the steps with the biggest impact, followed by sensitivity analysis[^muller2020lca-e8].

### Data sharing and conflicts of interest

All ACS journals strongly encourage authors to make research data public at publication[^acsiecrauthorguide-e7], but I&EC Research itself has no specific data requirements[^acsiecrauthorguide-e8]. Declaring conflicts of interest is a requirement in every field; see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#5-authorship-citation-and-conflicts-of-interest-give-every-contributor-due-credit). Research done with a company especially needs a clear declaration.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists only the three strategies this page's sources support; our sources do not cover the other strategies. The grouping and the second column are our own summary. The catalysis standards come from one perspective article, and the techno-economic and life cycle assessment standards come from guidelines for carbon capture and utilization; none of them are rules for the whole field.

| Strategy | What it looks like in chemical engineering | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Propose a new process, catalyst, or piece of equipment, or design a process with a process model | Compare with a state-of-the-art catalyst under the same conditions[^bligaard2016benchmarking-e17] and run a no-catalyst control[^bligaard2016benchmarking-e18]; check a process concept's mass and energy balances first, and make sure it does not violate the laws of thermodynamics[^zimmermann2020tea-e5] | [Synthesis and characterization studies](../../06_methods/synthesis_study.md), [Quantitative simulation](../../06_methods/simulation_study.md), [Optimization studies](../computer-science/practices/optimization_study.md) (Computer science page) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Compare several catalysts; use techno-economic and life cycle assessment to compare a new process with existing routes | Compare catalyst selectivity at the same conversion[^bligaard2016benchmarking-e15]; state the benchmark, location, and scale[^zimmermann2020tea-e6]; if you account for learning curves, do the same for the benchmark technology[^zimmermann2020tea-e12]; set the functional unit by actual use[^muller2020lca-e9] | [Benchmarking](../computer-science/practices/benchmarking.md) (Computer science page), and [Techno-economic and life cycle assessment](#techno-economic-and-life-cycle-assessment-state-your-assumptions-or-the-conclusions-cannot-be-trusted) above |
| [Measurement](../../05_research-strategies/measure.md) | Measure reaction rates, selectivity, and other data so that others can compare against them | Measure intrinsic rates and verify there are no heat transfer, mass transfer, or mixing effects[^bligaard2016benchmarking-e5][^bligaard2016benchmarking-e12]; state how turnover frequency was calculated[^bligaard2016benchmarking-e14]; some authors recommend blind round-robin measurements of the same samples by several groups to set realistic error bars[^bligaard2016benchmarking-e8] | [Experimental measurement](../../06_methods/experimental_measurement.md), and [Catalytic and kinetic data](#catalytic-and-kinetic-data-how-to-report-them-so-others-can-compare) above |

How to use this table: choose the main strategy from your central claim. For example, if you propose a new catalyst and then use techno-economic assessment to argue it is worth pursuing, hold the catalyst work to the standards of Building and improving, and write the economic part to the Comparative evaluation requirements, with its assumptions stated.

## Research methods common in this field

This field has no method pages of its own; it uses the cross-field methods in [Research types](../../06_methods/README.md) and the practices on the Computer science page:

- [Synthesis and characterization studies](../../06_methods/synthesis_study.md) and [Experimental measurement](../../06_methods/experimental_measurement.md): do a hazard assessment before you change quantities or conditions; see [lab safety](#lab-safety-is-part-of-research-do-a-hazard-assessment-before-you-start) above.
- [Quantitative simulation](../../06_methods/simulation_study.md): process simulation and reactor modeling, with parameters often taken from experimental data.
- [Optimization studies](../computer-science/practices/optimization_study.md), [Benchmarking](../computer-science/practices/benchmarking.md), and [Engineering research](../computer-science/practices/engineering_research.md) (Computer science page): process optimization often has more than one objective (cost, energy use, emissions), and its constraints come from physical and safety limits. In catalysis, a "benchmark" means a standard catalyst under standard reaction conditions, and aligning the conditions is harder[^bligaard2016benchmarking-e7]. Techno-economic and life cycle assessment have no separate method page; follow the section above.

---

## Advice for newcomers

1. **Do a hazard assessment before you start, and check with the person in charge before you scale up.** In the Texas Tech accident, the scale-up bypassed the principal investigators and no formal hazard assessment was done[^csb2011texastech-e2][^csb2011texastech-e6]. Follow your own institution's procedure.
2. **Write down safety requirements and near misses.** The students all said they did not know about the limit that was only given verbally[^csb2011texastech-e5]; a near miss that is never shared means the lesson is lost[^csb2011texastech-e13].
3. **Before you measure, think about how others will compare against your data.** The standards are in [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) above.
4. **Before you claim "industrial potential," state the scale and assumptions.** The carbon capture and utilization life cycle assessment guideline warns that environmental impact estimates based on lab scale may be too high or too low[^muller2020lca-e7].
5. **In techno-economic and life cycle assessments, put your assumptions where nobody can miss them.** For carbon dioxide to methanol, the literature reports carbon footprints ranging from negative to positive[^muller2020lca-e5]; the spread narrowed only after the assumptions about electricity and carbon dioxide supply were harmonized[^muller2020lca-e6].
6. **Before you sign a collaboration agreement, ask what you will be allowed to publish and whether a patent application must come first.** The journal will not delay publication over patent issues[^acsiecrauthorguide-e10]; according to one US university's guidance, once an invention is public you can no longer apply in most countries outside the US[^berkeleydisclose-e4]. Follow the rules of your own country and institution.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Deciding on your own to scale up, assuming the protection that worked for small amounts still works | This is exactly how the Texas Tech accident happened[^csb2011texastech-e2][^csb2011texastech-e3] |
| Giving safety limits only verbally; lab notebooks without dates or quantities | The investigation found students did not know the limit, and the records could not show how much was used[^csb2011texastech-e5][^csb2011texastech-e15] |
| Calculating turnover frequency from the conversion at a single point in time | It should be based on rate measurements and checked by varying concentration[^bligaard2016benchmarking-e6] |
| Claiming a catalyst is stable after recycling experiments run only at high conversion | This does not prove stability[^bligaard2016benchmarking-e16] |
| Treating feedstocks and electricity outside the system boundary as free in a techno-economic assessment | The carbon capture and utilization guideline points out that suppliers will not provide them free of charge[^zimmermann2020tea-e8] |
| Calling a negative life cycle assessment result "negative emissions" | A negative value is only a comparative result[^muller2020lca-e10] |

---

## Further reading

- **US Chemical Safety and Hazard Investigation Board, *Texas Tech University Laboratory Explosion* case study (2011)**: the investigation report on a university chemistry lab accident, setting out its causes and consequences. Read it before you start doing experiments.
- **Bligaard et al. 2016, *Toward Benchmarking in Catalysis Science***: how to measure and report catalytic data so they can be compared, in four parts: computational, heterogeneous, molecular, and electrocatalysis. Read the relevant part when you run catalysis or kinetics experiments.
- **Zimmermann et al. 2020 (techno-economic assessment) and Müller et al. 2020 (life cycle assessment)**: summaries of two guidelines for carbon capture and utilization, both open access. Even outside this area you can use them as a reference checklist, but they are not a general standard.
- **The AIChE Code of Ethics**: short; binding on members, a useful reference for non-members.
- **Your target journal's author guidelines**: this page uses only I&EC Research as an example, which does not stand for other chemical engineering journals. Before you submit, read your target journal's own guidelines, especially the parts on safety, data, and preprints.
- **Your institution's lab safety rules and its technology transfer office's guidance**: the sources cited here are from the US; your institution's rules take precedence.

[^acsiecrauthorguide-e1]: American Chemical Society, I&EC Research author guidelines, Scope of the Journal. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e1)
[^acsiecrauthorguide-e2]: American Chemical Society, I&EC Research author guidelines, Topical Categories. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e2)
[^acsiecrauthorguide-e3]: American Chemical Society, I&EC Research author guidelines, Scope of the Journal. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e3)
[^acsiecrauthorguide-e4]: American Chemical Society, I&EC Research author guidelines, Scope of the Journal. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e4)
[^acsiecrauthorguide-e5]: American Chemical Society, I&EC Research author guidelines, Prior Publication Policy. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e5)
[^acsiecrauthorguide-e7]: American Chemical Society, I&EC Research author guidelines, Research Data Policy. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e7)
[^acsiecrauthorguide-e8]: American Chemical Society, I&EC Research author guidelines, Data Requirements. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e8)
[^acsiecrauthorguide-e9]: American Chemical Society, I&EC Research author guidelines, Safety Considerations. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e9)
[^acsiecrauthorguide-e10]: American Chemical Society, I&EC Research author guidelines, Patent Activities and Intellectual Property. [Evidence](../../../sources/notes/acsiecrauthorguide.md#e10)
[^aichecodeethics-e1]: American Institute of Chemical Engineers, Code of Ethics, introductory paragraph. [Evidence](../../../sources/notes/aichecodeethics.md#e1)
[^aichecodeethics-e2]: American Institute of Chemical Engineers, Code of Ethics, item 1. [Evidence](../../../sources/notes/aichecodeethics.md#e2)
[^aichecodeethics-e3]: American Institute of Chemical Engineers, Code of Ethics, item 2. [Evidence](../../../sources/notes/aichecodeethics.md#e3)
[^aichecodeethics-e4]: American Institute of Chemical Engineers, Code of Ethics, item 3. [Evidence](../../../sources/notes/aichecodeethics.md#e4)
[^aichecodeethics-e5]: American Institute of Chemical Engineers, Code of Ethics, item 4. [Evidence](../../../sources/notes/aichecodeethics.md#e5)
[^aichecodeethics-e6]: American Institute of Chemical Engineers, Code of Ethics, item 5. [Evidence](../../../sources/notes/aichecodeethics.md#e6)
[^berkeleydisclose-e1]: UC Berkeley IPIRA, When to Disclose an Invention to OTL, When to disclose. [Evidence](../../../sources/notes/berkeleydisclose.md#e1)
[^berkeleydisclose-e2]: UC Berkeley IPIRA, When to disclose. [Evidence](../../../sources/notes/berkeleydisclose.md#e2)
[^berkeleydisclose-e4]: UC Berkeley IPIRA, FAQ. [Evidence](../../../sources/notes/berkeleydisclose.md#e4)
[^bligaard2016benchmarking-e1]: Bligaard et al. 2016, Abstract. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e1)
[^bligaard2016benchmarking-e2]: Bligaard et al. 2016, §1.5, p. 2593. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e2)
[^bligaard2016benchmarking-e3]: Bligaard et al. 2016, §1.4, p. 2591. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e3)
[^bligaard2016benchmarking-e5]: Bligaard et al. 2016, §2.2.1, p. 2595. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e5)
[^bligaard2016benchmarking-e6]: Bligaard et al. 2016, §2.2.1, p. 2595. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e6)
[^bligaard2016benchmarking-e7]: Bligaard et al. 2016, §2.2, p. 2595. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e7)
[^bligaard2016benchmarking-e8]: Bligaard et al. 2016, §2.2.1, p. 2595. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e8)
[^bligaard2016benchmarking-e9]: Bligaard et al. 2016, §2.2.1, pp. 2595–2596. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e9)
[^bligaard2016benchmarking-e10]: Bligaard et al. 2016, §2.3, p. 2596. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e10)
[^bligaard2016benchmarking-e11]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e11)
[^bligaard2016benchmarking-e12]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e12)
[^bligaard2016benchmarking-e13]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e13)
[^bligaard2016benchmarking-e14]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e14)
[^bligaard2016benchmarking-e15]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e15)
[^bligaard2016benchmarking-e16]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e16)
[^bligaard2016benchmarking-e17]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e17)
[^bligaard2016benchmarking-e18]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e18)
[^bligaard2016benchmarking-e19]: Bligaard et al. 2016, §2.1.1, p. 2593. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e19)
[^bligaard2016benchmarking-e20]: Bligaard et al. 2016, §2.4.1, p. 2598. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e20)
[^csb2011texastech-e1]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011 (Texas Tech case study), §1.0, p. 1. [Evidence](../../../sources/notes/csb2011texastech.md#e1)
[^csb2011texastech-e2]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §4.0, p. 3. [Evidence](../../../sources/notes/csb2011texastech.md#e2)
[^csb2011texastech-e3]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §4.0, p. 4. [Evidence](../../../sources/notes/csb2011texastech.md#e3)
[^csb2011texastech-e4]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §3.0, p. 3. [Evidence](../../../sources/notes/csb2011texastech.md#e4)
[^csb2011texastech-e5]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §3.0, p. 3. [Evidence](../../../sources/notes/csb2011texastech.md#e5)
[^csb2011texastech-e6]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §4.0, p. 4. [Evidence](../../../sources/notes/csb2011texastech.md#e6)
[^csb2011texastech-e7]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §4.0 footnote 13, p. 4. [Evidence](../../../sources/notes/csb2011texastech.md#e7)
[^csb2011texastech-e8]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §6.2, p. 8. [Evidence](../../../sources/notes/csb2011texastech.md#e8)
[^csb2011texastech-e9]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §9.0 item 3, p. 17. [Evidence](../../../sources/notes/csb2011texastech.md#e9)
[^csb2011texastech-e10]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §9.0 item 4, p. 17. [Evidence](../../../sources/notes/csb2011texastech.md#e10)
[^csb2011texastech-e11]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §9.0 item 6, p. 17. [Evidence](../../../sources/notes/csb2011texastech.md#e11)
[^csb2011texastech-e12]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §7.0, p. 13. [Evidence](../../../sources/notes/csb2011texastech.md#e12)
[^csb2011texastech-e13]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §7.0, p. 13. [Evidence](../../../sources/notes/csb2011texastech.md#e13)
[^csb2011texastech-e14]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §6.2.3, p. 12. [Evidence](../../../sources/notes/csb2011texastech.md#e14)
[^csb2011texastech-e15]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §4.0 footnote 7, p. 3. [Evidence](../../../sources/notes/csb2011texastech.md#e15)
[^csb2011texastech-e16]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, §4.0, p. 4. [Evidence](../../../sources/notes/csb2011texastech.md#e16)
[^muller2020lca-e1]: Müller et al. 2020, Abstract. [Evidence](../../../sources/notes/muller2020lca.md#e1)
[^muller2020lca-e2]: Müller et al. 2020, General Introduction to Life Cycle Assessment. [Evidence](../../../sources/notes/muller2020lca.md#e2)
[^muller2020lca-e4]: Müller et al. 2020, Introduction. [Evidence](../../../sources/notes/muller2020lca.md#e4)
[^muller2020lca-e5]: Müller et al. 2020, Introduction. [Evidence](../../../sources/notes/muller2020lca.md#e5)
[^muller2020lca-e6]: Müller et al. 2020, Introduction. [Evidence](../../../sources/notes/muller2020lca.md#e6)
[^muller2020lca-e7]: Müller et al. 2020, General Introduction to Life Cycle Assessment. [Evidence](../../../sources/notes/muller2020lca.md#e7)
[^muller2020lca-e8]: Müller et al. 2020, General Introduction to Life Cycle Assessment. [Evidence](../../../sources/notes/muller2020lca.md#e8)
[^muller2020lca-e9]: Müller et al. 2020, Scope Definition › Defining Functional Units. [Evidence](../../../sources/notes/muller2020lca.md#e9)
[^muller2020lca-e10]: Müller et al. 2020, Life Cycle Interpretation. [Evidence](../../../sources/notes/muller2020lca.md#e10)
[^muller2020lca-e11]: Müller et al. 2020, Reporting. [Evidence](../../../sources/notes/muller2020lca.md#e11)
[^zimmermann2020tea-e1]: Zimmermann et al. 2020, Abstract. [Evidence](../../../sources/notes/zimmermann2020tea.md#e1)
[^zimmermann2020tea-e2]: Zimmermann et al. 2020, Introduction. [Evidence](../../../sources/notes/zimmermann2020tea.md#e2)
[^zimmermann2020tea-e4]: Zimmermann et al. 2020, Discussion. [Evidence](../../../sources/notes/zimmermann2020tea.md#e4)
[^zimmermann2020tea-e5]: Zimmermann et al. 2020, Goal › Perspectives and Principles of Assessment Goals. [Evidence](../../../sources/notes/zimmermann2020tea.md#e5)
[^zimmermann2020tea-e6]: Zimmermann et al. 2020, Goal › Perspectives and Principles of Assessment Goals. [Evidence](../../../sources/notes/zimmermann2020tea.md#e6)
[^zimmermann2020tea-e7]: Zimmermann et al. 2020, Goal › Perspectives and Principles of Assessment Goals. [Evidence](../../../sources/notes/zimmermann2020tea.md#e7)
[^zimmermann2020tea-e8]: Zimmermann et al. 2020, Scope › Including or excluding CCU upstream processes. [Evidence](../../../sources/notes/zimmermann2020tea.md#e8)
[^zimmermann2020tea-e9]: Zimmermann et al. 2020, Inventory › Data Quality. [Evidence](../../../sources/notes/zimmermann2020tea.md#e9)
[^zimmermann2020tea-e10]: Zimmermann et al. 2020, Inventory › Data Quality. [Evidence](../../../sources/notes/zimmermann2020tea.md#e10)
[^zimmermann2020tea-e11]: Zimmermann et al. 2020, Inventory › Collecting Data. [Evidence](../../../sources/notes/zimmermann2020tea.md#e11)
[^zimmermann2020tea-e12]: Zimmermann et al. 2020, Inventory › Collecting Data. [Evidence](../../../sources/notes/zimmermann2020tea.md#e12)
[^zimmermann2020tea-e13]: Zimmermann et al. 2020, Inventory › Hydrogen as an input. [Evidence](../../../sources/notes/zimmermann2020tea.md#e13)
[^zimmermann2020tea-e14]: Zimmermann et al. 2020, Inventory › Electricity as an input. [Evidence](../../../sources/notes/zimmermann2020tea.md#e14)
[^zimmermann2020tea-e15]: Zimmermann et al. 2020, Inventory › Deriving a CO2 Price. [Evidence](../../../sources/notes/zimmermann2020tea.md#e15)
[^zimmermann2020tea-e17]: Zimmermann et al. 2020, Interpretation › Uncertainty and Sensitivity Analysis. [Evidence](../../../sources/notes/zimmermann2020tea.md#e17)
[^zimmermann2020tea-e18]: Zimmermann et al. 2020, Interpretation › Interpretation of Indicators. [Evidence](../../../sources/notes/zimmermann2020tea.md#e18)
[^zimmermann2020tea-e19]: Zimmermann et al. 2020, Reporting › Content. [Evidence](../../../sources/notes/zimmermann2020tea.md#e19)
[^zimmermann2020tea-e20]: Zimmermann et al. 2020, Reporting › Reporting Styles. [Evidence](../../../sources/notes/zimmermann2020tea.md#e20)
