# Materials engineering and nanotechnology: field overview

This page explains how research actually runs in materials engineering, including nanotechnology. In the field classification this handbook uses, materials engineering is 2.5 and nanotechnology is 2.10 (see the [Fields overview](../README.md)); this page treats them together. The field overlaps heavily with chemistry, physics, biology, and electrical engineering: for general conventions in synthesis and chemistry experiments, see the [Chemistry page](../chemistry/README.md); for condensed matter physics and preprint culture, see the [Physical sciences page](../physical-sciences/README.md); for nanomaterials in cell and animal experiments, see the [Biological sciences page](../biological-sciences/README.md). For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies this field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). This page covers only what is specific to this field.

**After reading this page, you should be able to:**

- explain the "synthesis, characterization, performance testing" cycle, and where shared characterization facilities and computation fit into it;
- know what information a materials or device paper must report, using the minimum information reporting standard for nanomaterials and the solar cell reporting summary as examples;
- recognize two common reproducibility problems: batch-to-batch variation and reporting only the "champion device";
- know how materials data are shared under the FAIR principles, and how to handle nanomaterials safely in the lab.

---

## How research works in this field

### One cycle: make it, characterize it, test it

Much experimental work in this field runs around one cycle `[Our analysis]`:

1. **Synthesis** (or processing): make the material, film, or device;
2. **Characterization**: use microscopy, diffraction, spectroscopy, and similar techniques to find out what you actually made (composition, structure, size, surface);
3. **Performance testing**: measure how well it does the job it is meant for (strength, conductivity, power conversion efficiency, catalytic activity, and so on);
4. adjust the synthesis conditions based on the results and go round again.

Pay special attention to step 1: how you made something affects what you made `[Our analysis]`. The synthesis route affects the properties of a nanomaterial, including its toxicity; this has been reported for silica, ceria, silver, and other materials[^mulhopt2018characterization-e5]. That is why Faria and colleagues recommend that newly published nanomaterials come with a high-quality synthesis procedure that others can follow, and that the purification method be reported too, because leftover precursors (the starting materials for the synthesis) can change the results of biological experiments[^faria2018minimum-e3].

**What counts as "nano".** One definition: at least one dimension between 1 and 100 nanometers. A 2009 document from the US National Institute for Occupational Safety and Health (NIOSH) defines engineered nanoparticles this way[^niosh2009approaches-e1]; Faria and colleagues also list "at least one functional dimension between 1 and 100 nm" as one of the possible ways to define the scope[^faria2018minimum-e15]. When you read the literature, check which definition the authors use `[Our analysis]`.

### Characterization often means using shared facilities

High-end characterization instruments such as electron microscopes are usually not found in every research group; often you use your university's shared instrumentation facility or a national user facility `[Our analysis]`. Here is one concrete example: the Molecular Foundry, a nanoscience user facility of the US Department of Energy at Lawrence Berkeley National Laboratory. These are one facility's rules; follow the rules of the facility you actually use `[Our analysis]`.

- **You have to apply.** Any researcher can apply, and proposals go through competitive peer review[^lblfoundryuser-e1], usually in one of two calls a year[^lblfoundryuser-e4]. Non-proprietary research is free[^lblfoundryuser-e2]; proprietary projects pay full cost recovery[^lblfoundryuser-e3].
- **Training comes before hands-on work.** Once on site, you take additional safety training before you start work[^lblfoundryuser-e5].
- **Acknowledge the facility when you publish.** Results that used the facility must acknowledge it in the required wording[^lblfoundryuser-e6].

What this means for your pace: apply for and book instrument time early, have your samples ready in advance, and think through your measurement plan before you get on the instrument `[Our analysis]`. For general scheduling methods, see [Planning and daily routines](../../08_throughout/planning_and_routines.md).

### Computation: density functional theory and high-throughput screening

Many projects pair experiments with computation. A common method is **density functional theory** (DFT), which computes atomic-scale structures and properties from quantum mechanics `[Our analysis]`. According to Lejaeghere and colleagues in 2016, more than 15,000 DFT papers are published every year, and DFT is increasingly used in an automated way to build large databases[^lejaeghere2016reproducibility-e1]. **High-throughput screening** computes the properties of thousands of structures at once[^draxl2018nomad-e3] to look for promising materials `[Our analysis]`.

Computation has its own reproducibility problems. There are many codes, and their implementations differ a great deal in detail[^lejaeghere2016reproducibility-e2]. Lejaeghere and colleagues organized a community effort that compared 15 codes and 40 potentials or basis sets on 71 elemental crystals[^lejaeghere2016reproducibility-e3]. (Potentials and basis sets are approximation settings that describe atoms and electrons in the calculation; they usually ship with the code as files `[Our analysis]`.) The result: recent codes and pseudopotentials (a widely used type of potential) agree very closely, with differences comparable to those between different high-precision experiments; older methods agree less well[^lejaeghere2016reproducibility-e4]. So they recommend using only the potential files from the latest version of a code[^lejaeghere2016reproducibility-e5]. They also acknowledge that fully specifying a calculation means reporting even the code's default values and the parameters hard-coded into it[^lejaeghere2016reproducibility-e6]. For general practice in simulation research, see [Quantitative simulation](../../06_methods/simulation_study.md) in Research types.

### Publishing

Our sources found no reliable public account of this field's authorship conventions, review turnaround times, or the relative standing of journals and conferences; for these, follow your advisor and your target journal. What we can say:

- **There are preprint channels.** The preprint server arXiv has a materials science category, cond-mat.mtrl-sci, covering synthesis, characterization, structure, mechanical properties, defects, interfaces, and more[^arxivtaxonomy-e7]; physics of nanostructures (quantum dots, nanotubes, graphene, and so on) goes in the mesoscale and nanoscale physics category, cond-mat.mes-hall[^arxivtaxonomy-e8]. For work closer to chemistry, see the [Chemistry page](../chemistry/README.md) for publishing conventions `[Our analysis]`.
- **Journals may require you to share materials and data.** For Nature Portfolio journals, for example, one condition of publication is making materials, data, code, and protocols promptly available to readers[^naturereportingstandards-e1]; any restrictions on access must be disclosed to the editors at submission[^naturereportingstandards-e3]. Other publishers may have different rules; check your target journal before you submit `[Our analysis]`.

---

## How this field differs from others

The table below is our own summary, meant to help you spot the differences quickly, not a strict division between fields `[Our analysis]`.

| | Materials engineering and nanotechnology | Chemistry | Computer science |
|---|---|---|---|
| What is studied | Structure and performance of materials and devices | Molecules and reactions | Algorithms, systems, data |
| Typical evidence | Synthesis method + several characterization techniques + performance data | Synthetic route + structure determination (see the [Chemistry page](../chemistry/README.md)) | Experiments on code and data (see the [Computer science page](../computer-science/README.md)) |
| Common sources of variation | Variation between batches, between devices, and between labs (reported in both nanoparticle and perovskite solar cell research[^mulhopt2018characterization-e3][^jacobsson2022open-e4][^jacobsson2022open-e5]) | Not discussed here; see the Chemistry page | Random seeds, software and hardware environment |
| Reporting standards | Developed separately for different material types and applications, e.g. a minimum information standard for bio–nano research and a solar cell reporting summary (see below) | See the Chemistry page | Artifact evaluation and others (see the Computer science page) |
| Safety | With nanomaterials, beyond chemical safety, you also have to consider nanoparticle inhalation and fire and explosion risk (see below) | Chemical safety | Lab safety usually not an issue |

---

## Norms and reporting standards in this field

### Minimum information reporting: bio–nano research as an example

Papers vary widely in which characterizations they performed and which experimental details they report, and this is a major obstacle to progress in bio–nano research[^faria2018minimum-e1]. In 2018, Faria and a group of colleagues proposed a **minimum information reporting standard** in *Nature Nanotechnology*: MIRIBEL (Minimum Information Reporting in Bio–Nano Experimental Literature). It has three categories of items: material characterization, biological characterization, and details of experimental protocols[^faria2018minimum-e2], plus a checklist to go through item by item while writing[^faria2018minimum-e14]. Note that MIRIBEL is a recommendation from a group of researchers, not a journal requirement `[Our analysis]`; the authors themselves say a standard is only useful if it is widely adopted[^faria2018minimum-e13]. When you submit, follow your target journal's requirements `[Our analysis]`.

Its material characterization section is useful to anyone working with nanomaterials `[Our analysis]`:

- **Say how each parameter was measured**: which technique, which instrument, which protocol[^faria2018minimum-e6]. For particle size, also say which size you measured, for example the geometric size or the hydrodynamic size in liquid[^faria2018minimum-e5].
- **Report the distribution, not just the mean.** Particles spread evenly from 10 to 990 nm and particles between 495 and 505 nm both have a mean size of 500 nm, but from the mean alone you cannot judge their biological effects[^faria2018minimum-e4]. Almost every characterization parameter is a distribution, and giving the distribution carries more information than a single mean[^faria2018minimum-e10].
- **Use two or more independent methods** to characterize the same property; this is far more valuable[^faria2018minimum-e7].
- **Say where the variation comes from**: repeated measurements on one batch, or several batches[^faria2018minimum-e8].
- **Characterize, where possible, in a medium close to the one used in later experiments**; for cell experiments, for example, measure in a similar liquid[^faria2018minimum-e9].
- **Report the statistical details**, such as the number of independent experiments[^faria2018minimum-e11]. For general practice, see the Part 3 chapter section [Report how big and how certain, not just the p-value](../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

For animal experiments, MIRIBEL states that the ARRIVE guidelines for reporting animal research should be followed[^faria2018minimum-e16]; see the [Biological sciences page](../biological-sciences/README.md).

### Reporting device performance: solar cells as an example

Device performance (such as how efficiently a solar cell turns light into electricity) depends on measurement conditions, so some journals have created dedicated reporting forms `[Our analysis]`. The examples below all come from the Nature journals (published by Nature Portfolio). In 2015, *Nature Materials* announced that authors of photovoltaic (solar power) papers must fill in a checklist of key technical information[^naturematerials2015checklist-e1]; its content was agreed in discussions between solar cell experts and editors of the Nature journals[^naturematerials2015checklist-e2]. Today Nature Portfolio requires a reporting summary for two areas of the physical sciences, solar cells and lasers[^naturereportingstandards-e2], and the solar cell form is published along with the accepted paper[^naturesolarcellsreporting-e1]. Between them, these two documents ask for:

- current density–voltage curves (J-V curves, which show how the cell's output current changes with voltage) in both the forward and reverse scan directions[^naturesolarcellsreporting-e2], along with the scan conditions and the cell area[^naturematerials2015checklist-e3];
- how many cells were tested, and a statistical analysis of device performance[^naturesolarcellsreporting-e4][^naturesolarcellsreporting-e5];
- whether the results were confirmed by an independent certification lab, and which one[^naturesolarcellsreporting-e3][^naturematerials2015checklist-e4].

The 2015 editorial also asked authors to report the average efficiency alongside the best device[^naturematerials2015checklist-e5], to describe the characterization protocols they used with particular care, and to give statistical evidence that the performance is reproducible[^naturematerials2015checklist-e6]. A measurement protocol optimized for one photovoltaic technology may not transfer directly to other systems[^naturematerials2015checklist-e7]. The reporting summary also notes that industry standards for photovoltaic characterization from international committees such as ASTM-E44 (a committee of ASTM International) and IEC-TC 82 (a technical committee of the International Electrotechnical Commission) can serve as references for academic research[^naturesolarcellsreporting-e6].

These are the Nature journals' rules, not a requirement across the whole field; if you submit elsewhere, follow that journal's requirements. Even if it does not ask for this form, you can use it to check your own paper `[Our analysis]`.

### Reproducibility: batch variation and the "champion device"

**Batch-to-batch variation.** The same material can come out differently from batch to batch. In the introduction to their 2018 paper, Mülhopt and colleagues point out that current industrial and laboratory synthesis processes for nanomaterials show considerable batch-to-batch variation[^mulhopt2018characterization-e3]. Their project involved 14 European labs over more than three years[^mulhopt2018characterization-e1] and fully characterized 46 batches[^mulhopt2018characterization-e2]. The result: parameters such as zeta potential (a measure of the surface charge of particles `[Our analysis]`) and particle size were fairly stable between batches, while parameters such as impurities were not well controlled[^mulhopt2018characterization-e7]. They also raise the question of how far a single batch can represent many batches at all[^mulhopt2018characterization-e4]; nanoparticles often agglomerate, so size distributions should be measured with several methods[^mulhopt2018characterization-e6].

Perovskite solar cell research (a newer type of solar cell) has similar problems. In their 2022 paper on a database of these cells, Jacobsson and colleagues point out that variation between cells and between batches can be large enough to hide differences that would otherwise be statistically significant; they add that this is not unique to the perovskite field[^jacobsson2022open-e4]. There is also variation between labs, usually attributed to "hidden parameters" that the papers do not report[^jacobsson2022open-e5]. The examples they suggest are glovebox volume, the composition of the atmosphere during fabrication, small changes in precursor ratios, and chemical impurities, and they make clear these are only hypotheses[^jacobsson2022open-e6]. So these seemingly trivial conditions are worth writing down in your lab notebook too `[Our analysis]`.

**Reporting only the "champion device".** Jacobsson and colleagues manually went through more than 15,000 perovskite solar cell papers published up to February 2020 and extracted data on more than 42,400 devices[^jacobsson2022open-e3]. They found that a typical project may make hundreds or thousands of devices before writing a paper, yet among papers that include raw device data, fewer than 6 devices per paper on average yielded extractable data[^jacobsson2022open-e7]; a common pattern is to vary one parameter over a few levels and report only the best device at each level[^jacobsson2022open-e8]. These numbers come only from perovskite solar cell papers and cannot be extended directly to the whole materials field; but if readers see only the best device, they cannot judge how easy the result is to reproduce, and this is worth keeping in mind for other device research too `[Our analysis]`. For the general principle of reporting all your results, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#2-be-honest-with-the-evidence-dont-fool-yourself-report-all-results).

### Sharing materials data and the FAIR principles

The **FAIR principles** are a set of data management principles designed and endorsed by representatives of academia, industry, funding agencies, and publishers, formally published in 2016[^wilkinson2016fair-e6]; the four letters stand for findable, accessible, interoperable, and reusable[^wilkinson2016fair-e2]. They put special emphasis on making data automatically findable and usable by computers[^wilkinson2016fair-e1]. Specific requirements include giving data a globally unique, persistent identifier[^wilkinson2016fair-e3] and attaching a clear usage license and detailed provenance information[^wilkinson2016fair-e4]. FAIR does not mean fully open: when the data themselves cannot be made public, publishing detailed metadata and access rules can still achieve a high degree of FAIRness[^wilkinson2016fair-e5].

Making experimental data FAIR is not easy. Jacobsson and colleagues, the authors of the perovskite database, think most labs do not manage to make their data FAIR, especially in applied sciences[^jacobsson2022open-e1]; they see the biggest obstacle as the diversity and complexity of the data, for example because a sample's properties often depend on its synthesis and processing history[^jacobsson2022open-e2]. Draxl and Scheffler likewise point out that the quality of experimental samples is often not fully characterized and depends heavily on the sample's history[^draxl2018nomad-e7]; to make experimental data reusable, the metadata describing the experiment, the sample, and the data must be well defined[^draxl2018nomad-e8].

Computational data can go into dedicated repositories; NOMAD (Novel Materials Discovery) is one example. Its builders, Draxl and Scheffler, point out that only a tiny fraction of the information produced by high-throughput computation is ever used[^draxl2018nomad-e1], and that the large amount of information beyond what goes into papers is usually discarded or even deleted[^draxl2018nomad-e2]. According to their 2018 description, the NOMAD Repository accepts the raw output files of computational codes, provided the authors are named, the code and version can be identified, and the input and output files are complete[^draxl2018nomad-e5]; data can be kept private at first, but everything becomes open after at most three years[^draxl2018nomad-e6]; data are stored free of charge for at least 10 years, which also helps groups remember what exactly they did a few years earlier[^draxl2018nomad-e4]. For the current rules, check the NOMAD website `[Our analysis]`.

For general methods of organizing data, see [Organizing research materials](../../08_throughout/organizing_materials.md#2-raw-data-is-read-only-everything-else-can-be-regenerated).

### Lab safety with nanomaterials (the US NIOSH guidance as an example)

The advice below comes from the 2009 NIOSH guidance *Approaches to Safe Nanotechnology*. It is a 2009 document from a US agency, not a rule that applies everywhere; the rules in China and other countries, and your own institution's safety policies, may differ, and your institution's requirements take precedence `[Our analysis]`.

- **The risks are unknown, so take precautions.** Until research clarifies which properties of nanoparticles may harm health, precautionary measures are warranted[^niosh2009approaches-e2].
- **Inhalation is the main concern.** Once nanomaterials are airborne, the most likely route into the body is through the respiratory tract[^niosh2009approaches-e3]. NIOSH recommends avoiding handling nanomaterials as free particles in the open air[^niosh2009approaches-e10] and storing easily dispersed materials in closed containers whenever possible[^niosh2009approaches-e7].
- **Use exhaust ventilation and filtration.** A well-designed exhaust ventilation system with a high-efficiency particulate air (HEPA) filter should remove nanomaterials effectively[^niosh2009approaches-e4].
- **Cleaning and personal habits.** Clean with HEPA-filtered vacuums and wet wiping, ban eating and drinking in the work area, and provide hand-washing facilities[^niosh2009approaches-e5]; do not dry sweep or use compressed air[^niosh2009approaches-e8].
- **Do not borrow exposure limits for ordinary dust.** Exposure limits set for non-nano particles may not protect health against nanoparticles[^niosh2009approaches-e6].
- **Watch for fire and explosion.** As the particle size of a combustible material shrinks, its likelihood and rate of combustion can increase, and materials that are relatively inert can become highly reactive at the nanoscale[^niosh2009approaches-e9].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists only the four strategies this page's sources support; our sources do not cover the other strategies. The grouping and the second column are our own summary, and each standard represents only the area named in its footnote `[Our analysis]`.

| Strategy | What it looks like in this field | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Make a new material, device, or process, then test its performance | A new nanomaterial comes with a synthesis procedure others can follow, including the purification method[^faria2018minimum-e3]; for devices, say how many were tested and give a statistical analysis of performance[^naturesolarcellsreporting-e4][^naturesolarcellsreporting-e5], and report the best device together with the average efficiency[^naturematerials2015checklist-e5] | [Synthesis and characterization studies](../../06_methods/synthesis_study.md), [Engineering research](../computer-science/practices/engineering_research.md) (Computer science page) |
| [Description](../../05_research-strategies/observe_describe.md) | Find out what the material you made actually is and how much batches differ | Say which technique, instrument, and protocol measured each parameter[^faria2018minimum-e6]; use two or more independent methods for the same property[^faria2018minimum-e7]; report distributions, not just means[^faria2018minimum-e10]; say whether variation comes from one batch or several[^faria2018minimum-e8] | [Experimental measurement](../../06_methods/experimental_measurement.md) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Compare different codes or methods, e.g. 15 codes compared on 71 elemental crystals[^lejaeghere2016reproducibility-e3] | Report the code, version, and potential files, and use only the potential files from the latest version of the code[^lejaeghere2016reproducibility-e5]; fully specify each calculation, down to default values and hard-coded parameters[^lejaeghere2016reproducibility-e6] | [Benchmarking](../computer-science/practices/benchmarking.md) (Computer science page), [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Compile data from many published papers into a database and analyze it, e.g. manually reviewing more than 15,000 perovskite solar cell papers and extracting data on more than 42,400 devices[^jacobsson2022open-e3] | A sample's properties often depend on its synthesis and processing history, which makes the data hard to make FAIR[^jacobsson2022open-e2]; papers often vary one parameter over a few levels and report only the best device at each level[^jacobsson2022open-e8] | [Data science](../../06_methods/data_science.md) |

How to use this table `[Our analysis]`: pick your main strategy from your central claim. For example, if you make a new device and also characterize the material in detail, judge the work by the standards of building and improving, and write up the characterization part to the standards of description.

## Research methods common in this field

This field has no method pages of its own; it uses the cross-field methods in [Research types](../../06_methods/README.md) and the practices from the Computer science page:

- [Synthesis and characterization studies](../../06_methods/synthesis_study.md), [Experimental measurement](../../06_methods/experimental_measurement.md): for reporting requirements, see [Minimum information reporting](#minimum-information-reporting-bionano-research-as-an-example) and [Reporting device performance](#reporting-device-performance-solar-cells-as-an-example) above.
- [Quantitative simulation](../../06_methods/simulation_study.md): see [Computation](#computation-density-functional-theory-and-high-throughput-screening) above; [Data science](../../06_methods/data_science.md): data mining and machine learning on materials databases, see [Sharing materials data](#sharing-materials-data-and-the-fair-principles) above.
- [Replication studies](../../06_methods/replication.md): if you cannot reproduce a result, check batch variation and "hidden parameters" first; see [Reproducibility](#reproducibility-batch-variation-and-the-champion-device) above.
- [Engineering research](../computer-science/practices/engineering_research.md) and [Benchmarking](../computer-science/practices/benchmarking.md) (Computer science page). Studies of the biological effects of nanomaterials must also follow the conventions for biological experiments; see the [Biological sciences page](../biological-sciences/README.md).

---

## Advice for newcomers

1. **Record the "trivial" conditions from your very first batch of samples.** In perovskite solar cell research, Jacobsson and colleagues suspect that glovebox volume, fabrication atmosphere, precursor ratios, and impurities may all be "hidden parameters"[^jacobsson2022open-e6]; if you write them down, you will have something to go on when you troubleshoot later `[Our analysis]`. For general lab-record practice, see the Part 3 chapter [Running and iterating](../../02_do-the-project/06_run-and-iterate.md#3-leave-a-record-of-every-run).
2. **Characterize key properties with two or more methods; make several batches and several devices, and report distributions.** For the specific requirements, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) above.
3. **Before you write the paper, check it against your target journal's reporting form.** If your area has no dedicated form, borrow a checklist from a neighboring area, such as MIRIBEL[^faria2018minimum-e14] or the solar cell reporting summary `[Our analysis]`.
4. **Apply for shared-facility instrument time early**, and have your samples and measurement plan ready before you get on the instrument; remember to acknowledge the facility when you publish[^lblfoundryuser-e6] `[Our analysis]`.
5. **For computational work, keep the complete input and output files**; you can deposit them in a public materials database[^draxl2018nomad-e5].
6. **Before you handle nanopowders for the first time, complete your institution's safety training**, and find out the requirements for ventilation, storage, and cleaning[^niosh2009approaches-e3][^niosh2009approaches-e4] `[Our analysis]`.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Reporting only the mean particle size | Two batches with the same mean can have very different size ranges, and the mean alone cannot tell you the biological effects[^faria2018minimum-e4] |
| Making a single batch and treating it as the properties of the material | Batch-to-batch variation in nanomaterial synthesis can be considerable[^mulhopt2018characterization-e3], and a single batch may not be representative[^mulhopt2018characterization-e4] |
| Showing a solar cell's curve in only one scan direction | The Nature journals' reporting summary requires both forward and reverse scans[^naturesolarcellsreporting-e2] |
| Weighing and transferring nanopowders on an open bench and cleaning up by dry sweeping | NIOSH recommends avoiding open handling and not dry sweeping or using compressed air[^niosh2009approaches-e10][^niosh2009approaches-e8] |

---

## Further reading

- **Faria et al. 2018, Minimum information reporting in bio–nano experimental literature**: the minimum information reporting recommendations for bio–nano research (MIRIBEL), with a checklist for writing. If you work purely on materials, focus on the material characterization section `[Our analysis]`.
- **The Nature journals' Solar Cells Reporting Summary, and the 2015 *Nature Materials* editorial A checklist for photovoltaic research**: if you work on photovoltaics, use them to check your paper before submission `[Our analysis]`.
- **Jacobsson et al. 2022, An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles**: shows what more than ten thousand papers in perovskite solar cell research look like when pooled, and the problems caused by reporting only the best devices and by batch variation.
- **Wilkinson et al. 2016, The FAIR Guiding Principles**: the original paper on the FAIR principles.
- **Lejaeghere et al. 2016, Reproducibility in density functional theory calculations of solids**: for computational researchers, how much different codes differ and how to choose potential files.
- **NIOSH 2009, Approaches to Safe Nanotechnology**: a US agency's guidance on occupational safety with nanomaterials. It dates from 2009; in practice, follow your institution's safety policies.

[^mulhopt2018characterization-e1]: Mülhopt et al. 2018, Abstract. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e1)
[^mulhopt2018characterization-e2]: Mülhopt et al. 2018, Abstract. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e2)
[^mulhopt2018characterization-e3]: Mülhopt et al. 2018, §1 Introduction. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e3)
[^mulhopt2018characterization-e4]: Mülhopt et al. 2018, §1 Introduction. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e4)
[^mulhopt2018characterization-e5]: Mülhopt et al. 2018, §1 Introduction. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e5)
[^mulhopt2018characterization-e6]: Mülhopt et al. 2018, §4 Discussion. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e6)
[^mulhopt2018characterization-e7]: Mülhopt et al. 2018, §4 Discussion. [Evidence](../../../sources/notes/mulhopt2018characterization.md#e7)
[^faria2018minimum-e1]: Faria et al. 2018, Abstract. [Evidence](../../../sources/notes/faria2018minimum.md#e1)
[^faria2018minimum-e2]: Faria et al. 2018, Abstract. [Evidence](../../../sources/notes/faria2018minimum.md#e2)
[^faria2018minimum-e3]: Faria et al. 2018, Material Characterisation: Synthesis and composition. [Evidence](../../../sources/notes/faria2018minimum.md#e3)
[^faria2018minimum-e4]: Faria et al. 2018, Material Characterisation: Size dispersity and aggregation. [Evidence](../../../sources/notes/faria2018minimum.md#e4)
[^faria2018minimum-e5]: Faria et al. 2018, Material Characterisation: Size, shape, and dimensions. [Evidence](../../../sources/notes/faria2018minimum.md#e5)
[^faria2018minimum-e6]: Faria et al. 2018, Material Characterisation: General guidelines. [Evidence](../../../sources/notes/faria2018minimum.md#e6)
[^faria2018minimum-e7]: Faria et al. 2018, Material Characterisation: General guidelines. [Evidence](../../../sources/notes/faria2018minimum.md#e7)
[^faria2018minimum-e8]: Faria et al. 2018, Material Characterisation: General guidelines. [Evidence](../../../sources/notes/faria2018minimum.md#e8)
[^faria2018minimum-e9]: Faria et al. 2018, Material Characterisation: General guidelines. [Evidence](../../../sources/notes/faria2018minimum.md#e9)
[^faria2018minimum-e10]: Faria et al. 2018, Material Characterisation: General guidelines. [Evidence](../../../sources/notes/faria2018minimum.md#e10)
[^faria2018minimum-e11]: Faria et al. 2018, Experimental Protocol Details: Details of data analysis. [Evidence](../../../sources/notes/faria2018minimum.md#e11)
[^faria2018minimum-e13]: Faria et al. 2018, Summary and Outlook. [Evidence](../../../sources/notes/faria2018minimum.md#e13)
[^faria2018minimum-e14]: Faria et al. 2018, Introduction. [Evidence](../../../sources/notes/faria2018minimum.md#e14)
[^faria2018minimum-e15]: Faria et al. 2018, Defining the Scope of a Minimum Information Standard. [Evidence](../../../sources/notes/faria2018minimum.md#e15)
[^faria2018minimum-e16]: Faria et al. 2018, Biological Characterisation: ARRIVE guidelines. [Evidence](../../../sources/notes/faria2018minimum.md#e16)
[^niosh2009approaches-e1]: NIOSH 2009, Executive Summary. [Evidence](../../../sources/notes/niosh2009approaches.md#e1)
[^niosh2009approaches-e2]: NIOSH 2009, Executive Summary. [Evidence](../../../sources/notes/niosh2009approaches.md#e2)
[^niosh2009approaches-e3]: NIOSH 2009, Executive Summary. [Evidence](../../../sources/notes/niosh2009approaches.md#e3)
[^niosh2009approaches-e4]: NIOSH 2009, Executive Summary. [Evidence](../../../sources/notes/niosh2009approaches.md#e4)
[^niosh2009approaches-e5]: NIOSH 2009, Executive Summary. [Evidence](../../../sources/notes/niosh2009approaches.md#e5)
[^niosh2009approaches-e6]: NIOSH 2009, Executive Summary. [Evidence](../../../sources/notes/niosh2009approaches.md#e6)
[^niosh2009approaches-e7]: NIOSH 2009, §8.3.3 Work practices. [Evidence](../../../sources/notes/niosh2009approaches.md#e7)
[^niosh2009approaches-e8]: NIOSH 2009, §8.3.3 Work practices. [Evidence](../../../sources/notes/niosh2009approaches.md#e8)
[^niosh2009approaches-e9]: NIOSH 2009, §6.1 Fire and Explosion Risk. [Evidence](../../../sources/notes/niosh2009approaches.md#e9)
[^niosh2009approaches-e10]: NIOSH 2009, §8.3.3 Work practices. [Evidence](../../../sources/notes/niosh2009approaches.md#e10)
[^lblfoundryuser-e1]: Molecular Foundry, User Program Overview. [Evidence](../../../sources/notes/lblfoundryuser.md#e1)
[^lblfoundryuser-e2]: Molecular Foundry, User Program Overview. [Evidence](../../../sources/notes/lblfoundryuser.md#e2)
[^lblfoundryuser-e3]: Molecular Foundry, User Program Overview. [Evidence](../../../sources/notes/lblfoundryuser.md#e3)
[^lblfoundryuser-e4]: Molecular Foundry, User Program Overview: Apply for Access. [Evidence](../../../sources/notes/lblfoundryuser.md#e4)
[^lblfoundryuser-e5]: Molecular Foundry, User Program Overview: Prepare to Start Work. [Evidence](../../../sources/notes/lblfoundryuser.md#e5)
[^lblfoundryuser-e6]: Molecular Foundry, User Program Overview: Project End and Reporting. [Evidence](../../../sources/notes/lblfoundryuser.md#e6)
[^lejaeghere2016reproducibility-e1]: Lejaeghere et al. 2016, Research Article Summary: Rationale. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e1)
[^lejaeghere2016reproducibility-e2]: Lejaeghere et al. 2016, Research Article Summary: Rationale. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e2)
[^lejaeghere2016reproducibility-e3]: Lejaeghere et al. 2016, Abstract. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e3)
[^lejaeghere2016reproducibility-e4]: Lejaeghere et al. 2016, Abstract. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e4)
[^lejaeghere2016reproducibility-e5]: Lejaeghere et al. 2016, main text. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e5)
[^lejaeghere2016reproducibility-e6]: Lejaeghere et al. 2016, main text. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e6)
[^draxl2018nomad-e1]: Draxl & Scheffler 2018, Introduction. [Evidence](../../../sources/notes/draxl2018nomad.md#e1)
[^draxl2018nomad-e2]: Draxl & Scheffler 2018, Introduction. [Evidence](../../../sources/notes/draxl2018nomad.md#e2)
[^draxl2018nomad-e3]: Draxl & Scheffler 2018, Introduction. [Evidence](../../../sources/notes/draxl2018nomad.md#e3)
[^draxl2018nomad-e4]: Draxl & Scheffler 2018, The NOMAD Repository. [Evidence](../../../sources/notes/draxl2018nomad.md#e4)
[^draxl2018nomad-e5]: Draxl & Scheffler 2018, The NOMAD Repository. [Evidence](../../../sources/notes/draxl2018nomad.md#e5)
[^draxl2018nomad-e6]: Draxl & Scheffler 2018, The NOMAD Repository. [Evidence](../../../sources/notes/draxl2018nomad.md#e6)
[^draxl2018nomad-e7]: Draxl & Scheffler 2018, Summary and outlook. [Evidence](../../../sources/notes/draxl2018nomad.md#e7)
[^draxl2018nomad-e8]: Draxl & Scheffler 2018, Summary and outlook. [Evidence](../../../sources/notes/draxl2018nomad.md#e8)
[^arxivtaxonomy-e7]: arXiv Category Taxonomy, cond-mat.mtrl-sci. [Evidence](../../../sources/notes/arxivtaxonomy.md#e7)
[^arxivtaxonomy-e8]: arXiv Category Taxonomy, cond-mat.mes-hall. [Evidence](../../../sources/notes/arxivtaxonomy.md#e8)
[^naturereportingstandards-e1]: Nature Portfolio, Reporting standards and availability of data, materials, code and protocols, top of page. [Evidence](../../../sources/notes/naturereportingstandards.md#e1)
[^naturereportingstandards-e2]: Nature Portfolio, Reporting standards, Reporting requirements for physical sciences research. [Evidence](../../../sources/notes/naturereportingstandards.md#e2)
[^naturereportingstandards-e3]: Nature Portfolio, Reporting standards, top of page. [Evidence](../../../sources/notes/naturereportingstandards.md#e3)
[^jacobsson2022open-e1]: Jacobsson et al. 2022, Main. [Evidence](../../../sources/notes/jacobsson2022open.md#e1)
[^jacobsson2022open-e2]: Jacobsson et al. 2022, Main. [Evidence](../../../sources/notes/jacobsson2022open.md#e2)
[^jacobsson2022open-e3]: Jacobsson et al. 2022, Details of the database. [Evidence](../../../sources/notes/jacobsson2022open.md#e3)
[^jacobsson2022open-e4]: Jacobsson et al. 2022, Example uses of the Perovskite Database. [Evidence](../../../sources/notes/jacobsson2022open.md#e4)
[^jacobsson2022open-e5]: Jacobsson et al. 2022, Example uses of the Perovskite Database. [Evidence](../../../sources/notes/jacobsson2022open.md#e5)
[^jacobsson2022open-e6]: Jacobsson et al. 2022, Example uses of the Perovskite Database. [Evidence](../../../sources/notes/jacobsson2022open.md#e6)
[^jacobsson2022open-e7]: Jacobsson et al. 2022, Future expansion of the database. [Evidence](../../../sources/notes/jacobsson2022open.md#e7)
[^jacobsson2022open-e8]: Jacobsson et al. 2022, Future expansion of the database. [Evidence](../../../sources/notes/jacobsson2022open.md#e8)
[^naturematerials2015checklist-e1]: Nature Materials 2015 editorial, standfirst. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e1)
[^naturematerials2015checklist-e2]: Nature Materials 2015 editorial, paragraph 1. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e2)
[^naturematerials2015checklist-e3]: Nature Materials 2015 editorial, paragraph 2. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e3)
[^naturematerials2015checklist-e4]: Nature Materials 2015 editorial, paragraph 3. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e4)
[^naturematerials2015checklist-e5]: Nature Materials 2015 editorial, paragraph 3. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e5)
[^naturematerials2015checklist-e6]: Nature Materials 2015 editorial, paragraph 3. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e6)
[^naturematerials2015checklist-e7]: Nature Materials 2015 editorial, paragraph 4. [Evidence](../../../sources/notes/naturematerials2015checklist.md#e7)
[^naturesolarcellsreporting-e1]: Nature Portfolio, Solar Cells Reporting Summary, note at the top of the form. [Evidence](../../../sources/notes/naturesolarcellsreporting.md#e1)
[^naturesolarcellsreporting-e2]: Nature Portfolio, Solar Cells Reporting Summary, item 2. [Evidence](../../../sources/notes/naturesolarcellsreporting.md#e2)
[^naturesolarcellsreporting-e3]: Nature Portfolio, Solar Cells Reporting Summary, item 7. [Evidence](../../../sources/notes/naturesolarcellsreporting.md#e3)
[^naturesolarcellsreporting-e4]: Nature Portfolio, Solar Cells Reporting Summary, item 8. [Evidence](../../../sources/notes/naturesolarcellsreporting.md#e4)
[^naturesolarcellsreporting-e5]: Nature Portfolio, Solar Cells Reporting Summary, item 8. [Evidence](../../../sources/notes/naturesolarcellsreporting.md#e5)
[^naturesolarcellsreporting-e6]: Nature Portfolio, Solar Cells Reporting Summary, note at the end of the form. [Evidence](../../../sources/notes/naturesolarcellsreporting.md#e6)
[^wilkinson2016fair-e1]: Wilkinson et al. 2016, Abstract. [Evidence](../../../sources/notes/wilkinson2016fair.md#e1)
[^wilkinson2016fair-e2]: Wilkinson et al. 2016, Introduction. [Evidence](../../../sources/notes/wilkinson2016fair.md#e2)
[^wilkinson2016fair-e3]: Wilkinson et al. 2016, Box 2. [Evidence](../../../sources/notes/wilkinson2016fair.md#e3)
[^wilkinson2016fair-e4]: Wilkinson et al. 2016, Box 2. [Evidence](../../../sources/notes/wilkinson2016fair.md#e4)
[^wilkinson2016fair-e5]: Wilkinson et al. 2016, The FAIR Guiding Principles in detail. [Evidence](../../../sources/notes/wilkinson2016fair.md#e5)
[^wilkinson2016fair-e6]: Wilkinson et al. 2016, Abstract. [Evidence](../../../sources/notes/wilkinson2016fair.md#e6)
