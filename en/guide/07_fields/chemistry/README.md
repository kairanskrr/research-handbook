# Chemical sciences: field overview

This page explains how chemistry research actually runs: research groups and the bench, treating safety as part of the research, lab notebooks, the characterization data a new compound requires, why synthetic procedures so often fail to reproduce, how to report spectra and raw data, ChemRxiv preprints, and authorship. For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md); this page does not repeat them. For the research strategies chemistry commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

Most of the specific rules on this page come from the American Chemical Society (ACS) and its journals, and from US safety investigation reports, because these materials are public and specific. **They are the rules of US institutions and particular journals, not conventions shared by chemists worldwide**; where your country, institution, or target journal has its own rules, those take precedence `[Our analysis]`. The examples also lean toward organic synthesis, because most of the specific reporting rules we found come from that area; conventions in physical chemistry, analytical chemistry, and other areas may differ `[Our analysis]`.

**After reading this page, you should be able to:**

- say which kind of chemistry you do and which research strategy it falls under, and how that affects the evidence your paper must provide;
- treat hazard assessment as a step in experimental design, and know when you must reassess;
- know what evidence a new compound needs to show "what it is" and "how pure it is";
- understand why synthetic results so often fail to reproduce, and how to write procedures others can repeat;
- avoid the mistakes newcomers most often make with safety, record keeping, spectrum processing, and preprints.

---

## How research works in this field

### First, work out which kind of chemistry you do

Chemistry has many areas. When you submit to ChemRxiv, the chemistry preprint server, you choose from a list of categories that includes analytical chemistry, organic chemistry, physical chemistry, and theoretical and computational chemistry[^chemrxivabout-e3]. By what the day-to-day work looks like, you can roughly sort chemistry into a few kinds `[Our analysis]`:

| Kind | What you do most days | Core evidence in the paper |
|---|---|---|
| Synthesis (organic, inorganic, polymer, etc.) | Design and run reactions, isolate and purify, identify the products | Experimental procedures, yields, characterization data, and spectra |
| Physical chemistry and mechanistic studies | Measure reaction rates, energies, spectra, and the like, and explain why a reaction happens the way it does | Measured data with their errors, and models |
| Analytical chemistry | Develop and validate methods of determination | The method's accuracy, sensitivity, and repeatability |
| Theoretical and computational chemistry | Compute molecular properties and reactions with quantum chemistry, molecular simulation, and similar tools | Computational methods, parameters, coordinates, and energies |

Which kind you belong to decides what data you must provide. For example, *The Journal of Organic Chemistry* (JOC), an ACS journal, requires proof of structure and purity for new compounds[^acsjocguidelines-e1], and for computational work requires the level of theory, basis set, and program, plus molecular coordinates and energies[^acsjocguidelines-e13]. Work out which kind you are before you join a group `[Our analysis]`.

### Research groups and the bench: many rules are passed on by word of mouth

Day-to-day experimental chemistry usually happens within a research group `[Our analysis]`. In the words of a US accident investigation report (see below), at a university the principal investigator (PI) is usually the professor responsible for the research and for the students, postdocs, and technicians in the lab[^csb2011texastech-e24]. This is similar to lab-based biology; see the [Biological sciences page](../biological-sciences/README.md#the-lab-revolves-around-the-pi).

As a newcomer, watch out: many key rules in a group may only ever be passed on verbally. In the 2010 Texas Tech University accident described below, the limit of "no more than 100 milligrams per synthesis" had only been told verbally to some students by the two PIs[^csb2011texastech-e17]; none of the students interviewed afterward, including the injured student, said they knew of a strict 100-milligram limit[^csb2011texastech-e5]. So once you join a group, ask outright, and try to get it in writing: which operations have upper limits, and which changes to conditions you must clear with your advisor first `[Our analysis]`.

Bergman and Danheiser (two chemistry professors at the University of California, Berkeley, and the Massachusetts Institute of Technology; Danheiser was then editor-in-chief of *Organic Syntheses*), in a 2016 editorial on the reproducibility of chemical results, recommend that PIs meet regularly in person with group members and look at their raw data and lab notebooks[^bergman2016reproducibility-e7]. If your group does not do this, you can bring your notebook and raw spectra to group meetings yourself `[Our analysis]`.

### Lab safety is part of the research, not extra paperwork

**Case: the 2010 laboratory explosion at Texas Tech University.** The US Chemical Safety and Hazard Investigation Board (Chemical Safety Board, CSB), the federal agency that investigates chemical accidents, wrote a dedicated case study:

- On January 7, 2010, a compound a graduate student in the university's Department of Chemistry and Biochemistry was handling exploded. He lost three fingers, burned his hands and face, and injured one eye[^csb2011texastech-e1].
- The students decided to scale the synthesis of this compound up to about 10 grams, without consulting the PIs first[^csb2011texastech-e2]; no formal hazard assessment was done for that day's quantity either[^csb2011texastech-e6].
- In these labs working on energetic materials, students did not need their PIs' approval before changing experimental conditions, including increasing the scale by what they considered "small" amounts or changing the temperature[^csb2011texastech-e23].

The other problems the report lists (an earlier near miss that was never shared, group meetings that did not discuss safety, goggles treated as a personal choice, and so on) are covered point by point on the [Chemical engineering page](../chemical-engineering/README.md#lab-safety-is-part-of-research-do-a-hazard-assessment-before-you-start). The CSB also notes that undergraduates mostly do experiments with known risks by following instructions, and that students doing research need very different safety training[^csb2011texastech-e22]. Managing research risk takes written procedures and training specific to the research being done[^csb2011texastech-e10].

At the CSB's recommendation, the ACS wrote the guide *Identifying and Evaluating Hazards in Research Laboratories*[^acs2015identifying-e1]. It is written for every researcher, from undergraduates to department chairs[^acs2015identifying-e4]. The three points below are the ones we picked out of it `[Our analysis]`:

1. **Assess before you start.** Researchers have the right and the responsibility to ask questions before starting an experiment until they understand all the hazards and safeguards[^acs2015identifying-e9]. The tools the guide describes include what-if analysis (raising a series of questions to find what might go wrong) and checklists[^acs2015identifying-e3].
2. **Reassess whenever conditions change.** Many accidents can be traced back to a change nobody noticed; whenever the work changes, check it against the original hazard analysis to see whether that is still adequate[^acs2015identifying-e5]. Changes that call for reassessment include scaling up, switching to a reactant with one more functional group, and a new person joining the group or an experienced one leaving[^acs2015identifying-e6]. Hazard assessment is an ongoing process[^acs2015identifying-e2].
3. **Review in a group, talk about safety at group meetings, and discuss near misses**[^acs2015identifying-e7][^acs2015identifying-e8].

Safety is also part of the publication requirements. The ACS ethical guidelines for publication (which apply to ACS journals) require that any unusual hazards in the chemicals, equipment, or procedures used in the research be clearly identified in the manuscript[^acs2026ethical-e3]; in 2021, ACS Publications added a "safety considerations" requirement to the author guidelines of every one of its journals[^acsjocguidelines-e17].

### Lab notebooks: write for the person who will check them later

In the Texas Tech accident, the CSB had to reconstruct events mainly from interviews, because the lab notebooks were undated and did not always record how much of each reactant was used[^csb2011texastech-e18]; the PIs did not review the notebooks regularly, and students' recording practices varied widely[^csb2011texastech-e19]. For the general rules of lab notebooks (record as you go, cross out mistakes instead of erasing them, keep the raw data), see the [Biological sciences page](../biological-sciences/README.md#the-lab-notebook-is-the-primary-record) and the Part chapter [Running and iterating](../../02_do-the-project/06_run-and-iterate.md#3-leave-a-record-of-every-run). Chemistry experiments additionally need a clear record of the quantities used each time (mass, volume, moles), the date, the source and lot of each reagent, and what you observed during the reaction `[Our analysis]`.

### Publishing: mainly journals, with ChemRxiv as chemistry's preprint server

Formal results in chemistry are usually published in journals `[Our analysis]`, unlike computer science, where conferences dominate; see the [Computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue). A few things to know:

- **Communications and full papers.** Some journals publish short communications (also called letters). The ACS ethical guidelines say that expanding a published communication into a full paper is generally acceptable, but you must cite the earlier communication and tell the editor when you submit[^acs2026ethical-e6]. The same guidelines also require that you avoid splitting one study into several publications[^acs2026ethical-e5], and that a manuscript be submitted to only one journal at a time[^acs2026ethical-e6].
- **ChemRxiv.** It is a free server for unpublished preprints in chemistry and related fields[^chemrxivabout-e1], jointly owned and run by the ACS and several other chemical societies[^chemrxivabout-e4]. Before posting it does only basic screening, **with no peer review**[^chemrxivabout-e2]; screeners do not judge whether the content is correct, complete, or significant[^chemrxivabout-e5]. **Once posted, a preprint is essentially permanent**: ChemRxiv says posted content can be cited and becomes part of the scholarly record, and except in rare cases cannot be removed[^chemrxivabout-e6].
- **Check your target journal's preprint policy first.** ChemRxiv says most journals accept manuscripts posted as preprints before submission, but some have restrictions, and it advises checking before you upload[^chemrxivabout-e7]. JOC, for example, allows preprints posted before submission, but you must say so in the cover letter and give the link[^acsjocguidelines-e14]; it discourages posting a preprint after submission without first asking the editor-in-chief[^acsjocguidelines-e15].

### Authorship: every author answers for the results

The ACS ethical guidelines set these authorship requirements: coauthors should be everyone who made significant scientific contributions to the work and who shares responsibility and accountability for the integrity and accuracy of the results[^acs2026ethical-e7]; the submitting author is responsible for sending the manuscript to every living coauthor and obtaining their agreement[^acs2026ethical-e8]; people who contributed but do not qualify for authorship (such as technicians) can be acknowledged[^acs2026ethical-e9]. Bergman and Danheiser stress two points: raising funding matters, but authorship should also require direct involvement in the research and a significant intellectual contribution[^bergman2016reproducibility-e9]; and all coauthors, including the PI, share responsibility for the published results[^bergman2016reproducibility-e10]. For the general principles of authorship, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#5-authorship-citation-and-conflicts-of-interest-give-every-contributor-due-credit) under Throughout the project.

---

## How this field differs from others

The table below compares chemistry with computer science. The computer science column draws on the [Computer science page](../computer-science/README.md); the chemistry column is compiled from this page's sources `[Our analysis]`.

| | Chemistry (mainly experimental synthesis) | Computer science |
|---|---|---|
| Formal publication | Journals; ChemRxiv preprints, subject to the target journal's policy[^chemrxivabout-e7] | Conferences in most areas |
| What you study | Real substances; you have to show "what it is and how pure it is"[^acsjocguidelines-e1] | Code and data, which can be copied exactly `[Our analysis]` |
| Safety | A hazard analysis should be done before every reaction (the wording of *Organic Syntheses*' rules)[^orgsyninstructions-e13]; manuscripts must identify unusual hazards[^acs2026ethical-e3] | Personal safety is usually not at stake; ethics review comes in only when people or vulnerabilities are involved `[Our analysis]` |
| How others check your results | They look at spectra, chromatograms, elemental analysis, and other characterization data[^acsjocguidelines-e2]; *Organic Syntheses* also has procedures repeated in an editor's lab[^orgsyninstructions-e2] | Artifact evaluation, rerunning the code |
| When results don't reproduce | Most cases involve real results the original authors did obtain; the problem is often details that were not written down (the first half is Bergman and Danheiser's judgment[^bergman2016reproducibility-e6], the second half is our analysis) | Often environment, randomness, or implementation details `[Our analysis]` |

---

## Norms and reporting standards in this field

### New compounds: show "what it is" and "how pure it is"

This section uses the author guidelines of JOC, an ACS journal, as the example (**they speak only for that one journal; for any other journal, read its own guidelines first**). If you do materials research such as nanomaterials or devices, see the [Materials engineering page](../materials-engineering/README.md) for the key points of reporting characterization.

- **You must prove both.** A new compound must come with evidence sufficient to establish its structure and its purity[^acsjocguidelines-e1], and purity must be documented compound by compound[^acsjocguidelines-e2].
- **Establishing structure.** You need proton and carbon-13 nuclear magnetic resonance (NMR) data, plus either high-resolution mass spectrometry (HRMS) or elemental analysis[^acsjocguidelines-e3]. Found values for carbon, hydrogen, and nitrogen in elemental analysis should be within 0.4% of the calculated values[^acsjocguidelines-e6].
- **Showing purity.** For work that is mainly synthetic, JOC sets no minimum purity, but it must be reported truthfully; when a compound will be used for physical measurements or biological testing, you must show it is at least 95% pure[^acsjocguidelines-e4]. A sharp melting point is not enough on its own; HRMS supports only the molecular formula and does not prove purity[^acsjocguidelines-e5].
- **Yields must be weighed.** Reported yields should be isolated yields of purified material, given as both mass and percentage[^acsjocguidelines-e9]. The JOC editors warn that yields above 95%, isomer ratios above 200:1, and enantiomeric excesses above 99% are typically not realistic without further explanation[^acsjocguidelines-e10].
- **Explain missing data.** If, say, a compound is too insoluble for a carbon-13 spectrum, state why in the experimental section[^acsjocguidelines-e18].

### Spectra: no editing

JOC states plainly that modifying data or spectra (for example baseline correction or removing solvent or impurity peaks) is unethical[^acsjocguidelines-e7], and that you may not use peak-editing software to suppress or hide impurity peaks[^acsjocguidelines-e8]. This is not a hypothetical problem: according to Bergman and Danheiser's 2016 editorial, the editors of *Organic Letters* found signs of manually removed NMR peaks in 2–3% of manuscripts submitted to the journal[^bergman2016reproducibility-e3]. They also list related questionable practices: discarding data points that do not fit expectations, and reporting only the best run's yield or selectivity[^bergman2016reproducibility-e4]. For how to report results in full, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#2-be-honest-with-the-evidence-dont-fool-yourself-report-all-results) under Throughout the project.

### Synthetic procedures: write them so others can repeat them

**Synthetic results are often hard to reproduce exactly.** Bergman and Danheiser consider it rare in chemistry for published results to be completely irreproducible, but not uncommon for reported yields, selectivities, and similar figures to be hard to reproduce exactly[^bergman2016reproducibility-e1], especially in synthetic chemistry[^bergman2016reproducibility-e2]. In their view, most problems involve real results the original authors did obtain[^bergman2016reproducibility-e6]; in other words, the problem often lies in details that were not written down `[Our analysis]`.

**The strictest example: independent checking at *Organic Syntheses*.** *Organic Syntheses* is an organic synthesis journal that requires experimental procedures far more detailed than those in typical journals and their Supporting Information, and every procedure is checked by repeating it in the lab of a member of the Board of Editors[^orgsyninstructions-e2]:

- During checking, each step must succeed at least twice, at least once at exactly the submitter's scale[^orgsyninstructions-e3]; the checker's yields and selectivities generally must not be more than about 5% below those originally reported[^orgsyninstructions-e4]. The checking editor and coworkers are now listed as "checker authors"[^orgsyninstructions-e5].
- Even so, according to Bergman and Danheiser's 2016 editorial, 7.5% of manuscripts submitted to the journal from 2010 to 2016 (about 1 in 13) were rejected because the editor's lab could not reproduce the authors' yields or selectivities within a reasonable range[^bergman2016reproducibility-e5].

Ordinary journals will not repeat your work for you. The items below are requirements and recommendations *Organic Syntheses* sets for its submissions; other journals may not require them, but they make a very useful self-check `[Our analysis]`:

- [ ] Give the source of every starting material and reagent, and the purity of commercial reagents[^orgsyninstructions-e8]
- [ ] Give room temperature as a specific number of degrees Celsius, not just "rt"; give vacuum as a specific value[^orgsyninstructions-e9][^orgsyninstructions-e10]
- [ ] Describe what you see during the reaction: color changes, gas evolution, solids precipitating, exotherms[^orgsyninstructions-e11]
- [ ] When a crude product goes straight into the next step, describe the purification method and give data for both the pure and the crude material[^orgsyninstructions-e14]
- [ ] Run the procedure at least twice at the stated scale; if yields differ by more than 10% between runs, there may be an influencing factor you have not found yet[^orgsyninstructions-e6][^orgsyninstructions-e7]
- [ ] Before submitting, ask a colleague who was not involved to repeat the procedure using only what you wrote (an "in-house check")[^orgsyninstructions-e6][^bergman2016reproducibility-e8]

### Data: Supporting Information, raw data, and FAIR

**Supporting Information** (SI) is the supplementary file published alongside a paper. JOC lets you put experimental details in the main text, the SI, or both, as long as they are accurate, complete, and detailed enough for others to repeat the work[^acsjocguidelines-e11].

- **Keep the raw data.** The ACS ethical guidelines require data to be kept and made available for at least five years after publication, and encourage depositing them in public databases[^acs2026ethical-e2]. JOC requires authors to provide raw NMR data files: the free induction decay (FID) files, that is, the unprocessed signal the instrument records, together with the acquisition and processing parameters[^acsjocguidelines-e12]. So after you run a spectrum, keep the raw files, not just the exported image `[Our analysis]`.
- **Data policies come in tiers; check your target journal.** The ACS research data policy has four levels, from "sharing encouraged" to "sharing required, with data reviewed alongside the manuscript"[^acsdatapolicy-e3], and each journal decides which level it applies[^acsdatapolicy-e2]. A data availability statement should say where the data are and how to get them, ideally with a persistent identifier such as a digital object identifier (DOI)[^acsdatapolicy-e4].
- **The FAIR principles.** FAIR means data are findable, accessible, interoperable, and reusable; for an introduction to the principles themselves, see the [Materials engineering page](../materials-engineering/README.md#sharing-materials-data-and-the-fair-principles). The ACS strongly supports these principles[^acsdatapolicy-e1]; data in the SI are acceptable, but it encourages machine-readable data[^acsdatapolicy-e5]. To learn how to do this in practice, see the *FAIR Chemistry Cookbook* maintained by the International Union of Pure and Applied Chemistry (IUPAC), which uses interactive examples to show how to manage chemical data in machine-readable form[^iupacfaircookbook-e1][^iupacfaircookbook-e2]. For general practice in organizing data, see [Organizing your research materials](../../08_throughout/organizing_materials.md) under Throughout the project.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, chosen according to your central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The grouping and the "What it looks like in chemistry" column are our own summary. Each standard represents only the journal, guideline, or area cited in its footnote (synthesis and mechanism come from JOC, comparison and measurement from catalysis, and analytical method validation from a 2002 IUPAC guideline) `[Our analysis]`.

| Strategy | What it looks like in chemistry | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Synthetic methodology and total synthesis: developing new reactions and reagents, or making a particular molecule | JOC expects conceptual novelty, not merely rerunning known chemistry on a different class of substrates, reagents, or catalysts[^acsjocguidelines-e30]; new compounds need proof of structure and purity[^acsjocguidelines-e1]; yields are reported for isolated, purified, weighed material[^acsjocguidelines-e9] | [Synthesis and characterization studies](../../06_methods/synthesis_study.md) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Catalysis: comparing a new catalyst with standard catalysts on activity, selectivity, and deactivation[^bligaard2016benchmarking-e1] | Compare with established or state-of-the-art catalysts under the same conditions[^bligaard2016benchmarking-e17]; compare selectivity at the same conversion[^bligaard2016benchmarking-e15] | No dedicated methods page yet |
| [Measurement](../../05_research-strategies/measure.md) | Catalysis: finding out how large the realistic error of a measurement is | Some researchers propose blind round-robin measurements of the same set of samples by several groups to determine realistic error bars[^bligaard2016benchmarking-e8] | [Experimental measurement](../../06_methods/experimental_measurement.md) |
| [Measurement](../../05_research-strategies/measure.md) | Analytical method development: establishing a method of determination and showing it is fit for a particular analytical purpose | Following the 2002 IUPAC guideline: test the assumptions the method relies on, establish and document its performance characteristics, and show whether it is fit for the purpose[^thompson2002harmonized-e1] (which characteristics to measure is listed after the table) | No dedicated methods page yet |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Mechanistic studies: working out, by experiment or theoretical calculation, how a reaction proceeds[^acsjocguidelines-e32] | JOC expects mechanistic studies to advance the methods or give new insight into how the reaction proceeds; merely confirming a known mechanism is not enough[^acsjocguidelines-e32]. If you use computation, describe the methods and results well enough for others to repeat the calculations[^acsjocguidelines-e33] | [Experimental measurement](../../06_methods/experimental_measurement.md), [Quantitative simulation](../../06_methods/simulation_study.md) |

The classification of the last two rows is our analysis `[Our analysis]`:

- **Analytical method development counts as Measurement**, because the central claim is "this ruler is accurate and fit for use."
- **Mechanistic studies count as Causal explanation**, because they answer "why does the reaction happen this way." On what evidence is enough, we found no specific journal rule, only a definition of a term (not a review standard): the IUPAC *Compendium of Chemical Terminology* (the Gold Book), following the 1994 *Glossary of Terms Used in Physical Organic Chemistry*, says an acceptable mechanism must be consistent with the reaction stoichiometry, the rate law, and all other available experimental data (such as the stereochemical course of the reaction), and that there may be several alternative mechanisms the evidence does not exclude[^iupacgoldbookmechanism-e1]; for many reactions not all of this information is available, and the proposed mechanism rests on incomplete data[^iupacgoldbookmechanism-e2]. So when you write about a mechanism, say which alternative mechanisms your data rule out and which they do not, and do not turn "consistent with the data" into "proved" `[Our analysis]`.
- **Computational chemistry is classified by its central claim, not given a row of its own.** JOC's author guidelines say mechanistic studies can be experimental or theoretical[^acsjocguidelines-e32]. For work whose main point is comparing the accuracy of computational methods (benchmarking), we found no journal standard, only a 2017 perspective by Mata and Suhm in *Angewandte Chemie*; the recommendations below represent only these two authors:
  - **Tie it to experiment where you can.** Many quantum chemistry benchmarking papers use only another theoretical method as the reference, with not a single experimental result[^mata2017benchmarking-e1]; the authors grant there are legitimate reasons for this[^mata2017benchmarking-e2], but recommend focusing on quantities that can be measured, or making the link between the computed quantity and experimental data explicit[^mata2017benchmarking-e5].
  - **One match does not count.** A single agreement may come from errors that happen to cancel; you usually need a broad and diverse dataset[^mata2017benchmarking-e3]. Knowing the experimental result before you compute also risks biasing you[^mata2017benchmarking-e4].
  - **Report the failures too.** Discuss methods that fail as well, especially widely used ones[^mata2017benchmarking-e6]; explain the sources of error and key approximations as far as you can[^mata2017benchmarking-e7], and give structures and energies in the SI so others can repeat the work[^mata2017benchmarking-e8].

The standards for analytical method validation come from a 2002 IUPAC technical report, *Harmonized Guidelines for Single-Laboratory Validation of Methods of Analysis*. It is written for analytical labs validating methods, not as any journal's review standard; when you submit, also check your target journal's requirements. The points in the report most relevant to newcomers:

- **Characteristics to measure.** Typical ones include selectivity, trueness, precision, recovery, limit of detection, limit of quantification, and ruggedness[^thompson2002harmonized-e2].
- **Who decides "fit for purpose."** It depends on whether the method's performance meets criteria agreed between the analyst and the end user of the data[^thompson2002harmonized-e3].
- **How to check ruggedness.** Deliberately introduce small variations into the procedure and see how much the result changes[^thompson2002harmonized-e6].
- **How far a single lab can go.** "Full" validation usually means a collaborative study involving several laboratories[^thompson2002harmonized-e4]; that is not always practical or necessary, in which case single-laboratory validation alone can be done[^thompson2002harmonized-e5].

---

## Research methods common in this field

The classification below is our analysis `[Our analysis]`. For synthetic methodology, total synthesis, and target-molecule synthesis, see [Synthesis and characterization studies](../../06_methods/synthesis_study.md). For mechanistic and physical chemistry measurements, see [Experimental measurement](../../06_methods/experimental_measurement.md); like [Controlled experiments](../../06_methods/controlled_experiment.md), it insists on changing one factor at a time, but the object is a chemical system rather than people. For computational chemistry, see [Quantitative simulation](../../06_methods/simulation_study.md); you must state the level of theory, basis set, program, and coordinates[^acsjocguidelines-e13]. When comparing computational methods, the computer science page on [Benchmarking](../computer-science/practices/benchmarking.md) can help. For reproduction and independent checking, see [Replication studies](../../06_methods/replication.md); in synthetic chemistry, reproducing yields and selectivities is itself a demanding task[^orgsyninstructions-e4]. For reviews, see [Review studies](../../06_methods/review_study.md). Analytical method development has no methods page yet; for the characteristics validation should cover, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) above.

---

## Advice for newcomers

1. **In your first week in the group, ask about the group's safety rules and write them down.** Which substances have quantity limits, and which changes to conditions you must clear with your advisor first. Verbal rules get lost easily[^csb2011texastech-e5].
2. **Do a hazard assessment for every new reaction and every change of conditions.** Especially when scaling up or changing reactants[^acs2015identifying-e6]. If you are unsure, ask; asking is a researcher's right and responsibility[^acs2015identifying-e9].
3. **Wear goggles and other protection as required; do not treat them as a personal choice to make case by case** `[Our analysis]`. In the Texas Tech lab, some people did treat goggles that way[^csb2011texastech-e16]. Report near misses, even when nobody was hurt[^csb2011texastech-e25]; near misses become chances for education and improvement only if they are recorded, tracked, and communicated[^csb2011texastech-e11].
4. **Write in your notebook the same day, date every entry, and record quantities and observations clearly.** Keep raw spectrum files (FID files and the like) separately[^csb2011texastech-e18][^acsjocguidelines-e12].
5. **Be extra skeptical of the results you want.** Good PIs train their group members to be skeptical of results they want to believe are correct[^bergman2016reproducibility-e11]. Do not edit spectra, and do not pick your best run's yield[^acsjocguidelines-e7][^bergman2016reproducibility-e4].
6. **Write your experimental procedures for someone who has never been in your lab.** Use the self-check list above, and have a colleague do an in-house check before you submit[^orgsyninstructions-e6].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Thinking "it's only a little bigger" and scaling up without reassessing | Scale-up is a textbook change that calls for reassessment[^acs2015identifying-e6]; the Texas Tech accident happened right after an unassessed scale-up[^csb2011texastech-e2][^csb2011texastech-e6] |
| Notebook entries without dates or quantities | If something goes wrong, nobody can reconstruct what happened[^csb2011texastech-e18], and the results cannot be repeated `[Our analysis]` |
| Using software to remove solvent or impurity peaks from spectra | JOC explicitly calls this unethical[^acsjocguidelines-e7] |
| "Proving" purity with HRMS or a melting point alone | JOC says neither is enough to prove the purity of a new compound[^acsjocguidelines-e5] |
| Reporting your best run's yield, or calculating yield from the NMR of crude material | JOC requires yields of isolated, purified, weighed material[^acsjocguidelines-e9]; Bergman and Danheiser list reporting only the best run as a questionable practice[^bergman2016reproducibility-e4] |
| Writing "stirred at room temperature overnight" or "concentrated under reduced pressure" in a procedure | Temperature, pressure, and time are unclear, so others will struggle to repeat it[^orgsyninstructions-e9][^orgsyninstructions-e10] |
| Keeping only screenshots or PDFs of spectra | Journals may require the raw data files[^acsjocguidelines-e12] |
| Posting a ChemRxiv preprint after submission without asking the editor-in-chief | Some journals (such as JOC) discourage it[^acsjocguidelines-e15], and once posted it essentially cannot be removed[^chemrxivabout-e6] |
| Listing as an author someone who only provided funding and took no part in the research | Authorship should require direct involvement and a significant intellectual contribution[^bergman2016reproducibility-e9][^acs2026ethical-e7] |

---

## Further reading

- **CSB, *Texas Tech University Laboratory Explosion* (2011)**: the US Chemical Safety Board's case study, showing how one scale-up experiment turned into an accident. Worth reading once before you start lab work. **ACS, *Identifying and Evaluating Hazards in Research Laboratories* (2015)**: the ACS hazard assessment guide, describing tools such as checklists; Chapter 6 covers reassessing whenever conditions change.
- **Bergman & Danheiser 2016, *Reproducibility in Chemical Research* (editorial in *Angewandte Chemie*)**: two pages on the reasons results fail to reproduce in chemistry, with advice for PIs and authors.
- **The *Organic Syntheses* instructions for authors**: requirements for writing up synthetic procedures that are far more detailed than typical journals'; good to use as a self-check list.
- **Your target journal's author guidelines**, for example JOC's characterization and purity requirements and the ACS research data policy. Reread them before every submission. **ACS, *Ethical Guidelines to Publication of Chemical Research***: the publication ethics guidelines for ACS journals, covering data retention, authorship, and duplicate publication.
- **IUPAC *FAIR Chemistry Cookbook***: read it when you want to organize your data in a machine-readable, reusable format.

[^chemrxivabout-e1]: ChemRxiv, About ChemRxiv. [Evidence](../../../sources/notes/chemrxivabout.md#e1)
[^chemrxivabout-e2]: ChemRxiv, About ChemRxiv. [Evidence](../../../sources/notes/chemrxivabout.md#e2)
[^chemrxivabout-e3]: ChemRxiv, About ChemRxiv, Scope. [Evidence](../../../sources/notes/chemrxivabout.md#e3)
[^chemrxivabout-e4]: ChemRxiv, About ChemRxiv, The ChemRxiv partnership. [Evidence](../../../sources/notes/chemrxivabout.md#e4)
[^chemrxivabout-e5]: ChemRxiv, author FAQ, How is the content screened? [Evidence](../../../sources/notes/chemrxivabout.md#e5)
[^chemrxivabout-e6]: ChemRxiv, author FAQ, Can I retract my content? [Evidence](../../../sources/notes/chemrxivabout.md#e6)
[^chemrxivabout-e7]: ChemRxiv, author FAQ, journal policies. [Evidence](../../../sources/notes/chemrxivabout.md#e7)
[^acsjocguidelines-e1]: JOC author guidelines, Compound Characterization Data. [Evidence](../../../sources/notes/acsjocguidelines.md#e1)
[^acsjocguidelines-e2]: JOC author guidelines, Compound Characterization Data. [Evidence](../../../sources/notes/acsjocguidelines.md#e2)
[^acsjocguidelines-e3]: JOC author guidelines, NMR. [Evidence](../../../sources/notes/acsjocguidelines.md#e3)
[^acsjocguidelines-e4]: JOC author guidelines, Purity. [Evidence](../../../sources/notes/acsjocguidelines.md#e4)
[^acsjocguidelines-e5]: JOC author guidelines, Purity. [Evidence](../../../sources/notes/acsjocguidelines.md#e5)
[^acsjocguidelines-e6]: JOC author guidelines, Elemental Analysis and Accurate Mass Measurement. [Evidence](../../../sources/notes/acsjocguidelines.md#e6)
[^acsjocguidelines-e7]: JOC author guidelines, Experimental Section. [Evidence](../../../sources/notes/acsjocguidelines.md#e7)
[^acsjocguidelines-e8]: JOC author guidelines, Purity / NMR spectra. [Evidence](../../../sources/notes/acsjocguidelines.md#e8)
[^acsjocguidelines-e9]: JOC author guidelines, Synthesis Experiments. [Evidence](../../../sources/notes/acsjocguidelines.md#e9)
[^acsjocguidelines-e10]: JOC author guidelines, Synthesis Experiments. [Evidence](../../../sources/notes/acsjocguidelines.md#e10)
[^acsjocguidelines-e11]: JOC author guidelines, Experimental Section/Computational Methods. [Evidence](../../../sources/notes/acsjocguidelines.md#e11)
[^acsjocguidelines-e12]: JOC author guidelines, NMR raw data. [Evidence](../../../sources/notes/acsjocguidelines.md#e12)
[^acsjocguidelines-e13]: JOC author guidelines, Computational Data. [Evidence](../../../sources/notes/acsjocguidelines.md#e13)
[^acsjocguidelines-e14]: JOC author guidelines, Editorial Policies (preprints). [Evidence](../../../sources/notes/acsjocguidelines.md#e14)
[^acsjocguidelines-e15]: JOC author guidelines, Editorial Policies (preprints). [Evidence](../../../sources/notes/acsjocguidelines.md#e15)
[^acsjocguidelines-e17]: JOC author guidelines, Emphasis on Chemical Safety. [Evidence](../../../sources/notes/acsjocguidelines.md#e17)
[^acsjocguidelines-e18]: JOC author guidelines, Compound Characterization Data. [Evidence](../../../sources/notes/acsjocguidelines.md#e18)
[^csb2011texastech-e1]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 1.0 Introduction. [Evidence](../../../sources/notes/csb2011texastech.md#e1)
[^csb2011texastech-e17]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 3.0 Pre-incident Events. [Evidence](../../../sources/notes/csb2011texastech.md#e17)
[^csb2011texastech-e5]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 3.0 Pre-incident Events. [Evidence](../../../sources/notes/csb2011texastech.md#e5)
[^csb2011texastech-e2]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 4.0 Incident Description. [Evidence](../../../sources/notes/csb2011texastech.md#e2)
[^csb2011texastech-e6]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 4.0 Incident Description. [Evidence](../../../sources/notes/csb2011texastech.md#e6)
[^csb2011texastech-e18]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, p. 3, footnote 7. [Evidence](../../../sources/notes/csb2011texastech.md#e18)
[^csb2011texastech-e19]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 6.2.3. [Evidence](../../../sources/notes/csb2011texastech.md#e19)
[^csb2011texastech-e11]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 9.0 Key Lessons. [Evidence](../../../sources/notes/csb2011texastech.md#e11)
[^csb2011texastech-e22]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 6.2.2. [Evidence](../../../sources/notes/csb2011texastech.md#e22)
[^csb2011texastech-e16]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 4.0 Incident Description. [Evidence](../../../sources/notes/csb2011texastech.md#e16)
[^csb2011texastech-e10]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 9.0 Key Lessons. [Evidence](../../../sources/notes/csb2011texastech.md#e10)
[^csb2011texastech-e23]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 6.2.3. [Evidence](../../../sources/notes/csb2011texastech.md#e23)
[^csb2011texastech-e24]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, p. 3, footnote 6. [Evidence](../../../sources/notes/csb2011texastech.md#e24)
[^csb2011texastech-e25]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 7.0. [Evidence](../../../sources/notes/csb2011texastech.md#e25)
[^acs2015identifying-e1]: ACS 2015, Executive Summary. [Evidence](../../../sources/notes/acs2015identifying.md#e1)
[^acs2015identifying-e2]: ACS 2015, Executive Summary. [Evidence](../../../sources/notes/acs2015identifying.md#e2)
[^acs2015identifying-e3]: ACS 2015, Executive Summary. [Evidence](../../../sources/notes/acs2015identifying.md#e3)
[^acs2015identifying-e4]: ACS 2015, 1.2 Application. [Evidence](../../../sources/notes/acs2015identifying.md#e4)
[^acs2015identifying-e5]: ACS 2015, 6. Change Control. [Evidence](../../../sources/notes/acs2015identifying.md#e5)
[^acs2015identifying-e6]: ACS 2015, 6.1 Recognizing Change. [Evidence](../../../sources/notes/acs2015identifying.md#e6)
[^acs2015identifying-e7]: ACS 2015, 5.3. [Evidence](../../../sources/notes/acs2015identifying.md#e7)
[^acs2015identifying-e8]: ACS 2015, 5.3. [Evidence](../../../sources/notes/acs2015identifying.md#e8)
[^acs2015identifying-e9]: ACS 2015, 4.3 Researcher and Laboratory Worker. [Evidence](../../../sources/notes/acs2015identifying.md#e9)
[^acs2026ethical-e2]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 3. [Evidence](../../../sources/notes/acs2026ethical.md#e2)
[^acs2026ethical-e3]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 5. [Evidence](../../../sources/notes/acs2026ethical.md#e3)
[^acs2026ethical-e5]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 7. [Evidence](../../../sources/notes/acs2026ethical.md#e5)
[^acs2026ethical-e6]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 9. [Evidence](../../../sources/notes/acs2026ethical.md#e6)
[^acs2026ethical-e7]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 13. [Evidence](../../../sources/notes/acs2026ethical.md#e7)
[^acs2026ethical-e8]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 13. [Evidence](../../../sources/notes/acs2026ethical.md#e8)
[^acs2026ethical-e9]: ACS Ethical Guidelines to Publication of Chemical Research (2026 revision), B, item 13. [Evidence](../../../sources/notes/acs2026ethical.md#e9)
[^bergman2016reproducibility-e1]: Bergman & Danheiser 2016, Sources of Irreproducibility. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e1)
[^bergman2016reproducibility-e2]: Bergman & Danheiser 2016, Sources of Irreproducibility. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e2)
[^bergman2016reproducibility-e3]: Bergman & Danheiser 2016, Sources of Irreproducibility. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e3)
[^bergman2016reproducibility-e4]: Bergman & Danheiser 2016, Sources of Irreproducibility. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e4)
[^bergman2016reproducibility-e5]: Bergman & Danheiser 2016, Replicating Valid Results. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e5)
[^bergman2016reproducibility-e6]: Bergman & Danheiser 2016, Replicating Valid Results. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e6)
[^bergman2016reproducibility-e7]: Bergman & Danheiser 2016, Recommendations. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e7)
[^bergman2016reproducibility-e8]: Bergman & Danheiser 2016, Recommendations. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e8)
[^bergman2016reproducibility-e9]: Bergman & Danheiser 2016, Recommendations. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e9)
[^bergman2016reproducibility-e10]: Bergman & Danheiser 2016, Recommendations. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e10)
[^bergman2016reproducibility-e11]: Bergman & Danheiser 2016, Recommendations. [Evidence](../../../sources/notes/bergman2016reproducibility.md#e11)
[^orgsyninstructions-e2]: Organic Syntheses Instructions for Authors, opening section. [Evidence](../../../sources/notes/orgsyninstructions.md#e2)
[^orgsyninstructions-e3]: Organic Syntheses Instructions for Authors, Checking of procedures. [Evidence](../../../sources/notes/orgsyninstructions.md#e3)
[^orgsyninstructions-e4]: Organic Syntheses Instructions for Authors, Checking of procedures. [Evidence](../../../sources/notes/orgsyninstructions.md#e4)
[^orgsyninstructions-e5]: Organic Syntheses Instructions for Authors, Checking of procedures. [Evidence](../../../sources/notes/orgsyninstructions.md#e5)
[^orgsyninstructions-e6]: Organic Syntheses Instructions for Authors, Scale / reproducibility. [Evidence](../../../sources/notes/orgsyninstructions.md#e6)
[^orgsyninstructions-e7]: Organic Syntheses Instructions for Authors, Scale / reproducibility. [Evidence](../../../sources/notes/orgsyninstructions.md#e7)
[^orgsyninstructions-e8]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../../sources/notes/orgsyninstructions.md#e8)
[^orgsyninstructions-e9]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../../sources/notes/orgsyninstructions.md#e9)
[^orgsyninstructions-e10]: Organic Syntheses Instructions for Authors, Reaction procedure. [Evidence](../../../sources/notes/orgsyninstructions.md#e10)
[^orgsyninstructions-e11]: Organic Syntheses Instructions for Authors, Reaction procedure. [Evidence](../../../sources/notes/orgsyninstructions.md#e11)
[^orgsyninstructions-e13]: Organic Syntheses Instructions for Authors, Safety (Note 1). [Evidence](../../../sources/notes/orgsyninstructions.md#e13)
[^orgsyninstructions-e14]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../../sources/notes/orgsyninstructions.md#e14)
[^acsdatapolicy-e1]: ACS Research Data Policy, opening. [Evidence](../../../sources/notes/acsdatapolicy.md#e1)
[^acsdatapolicy-e2]: ACS Research Data Policy, ACS Research Data Policy. [Evidence](../../../sources/notes/acsdatapolicy.md#e2)
[^acsdatapolicy-e3]: ACS Research Data Policy, Research Data Policy Levels. [Evidence](../../../sources/notes/acsdatapolicy.md#e3)
[^acsdatapolicy-e4]: ACS Research Data Policy, Data Availability Statements. [Evidence](../../../sources/notes/acsdatapolicy.md#e4)
[^acsdatapolicy-e5]: ACS Research Data Policy, Data Availability Statements. [Evidence](../../../sources/notes/acsdatapolicy.md#e5)
[^iupacfaircookbook-e1]: IUPAC FAIR Chemistry Cookbook, home page. [Evidence](../../../sources/notes/iupacfaircookbook.md#e1)
[^iupacfaircookbook-e2]: IUPAC FAIR Chemistry Cookbook, home page. [Evidence](../../../sources/notes/iupacfaircookbook.md#e2)
[^acsjocguidelines-e30]: JOC author guidelines, Scope of the Journal (a). [Evidence](../../../sources/notes/acsjocguidelines.md#e30)
[^acsjocguidelines-e32]: JOC author guidelines, Scope of the Journal (b). [Evidence](../../../sources/notes/acsjocguidelines.md#e32)
[^acsjocguidelines-e33]: JOC author guidelines, Computational Data. [Evidence](../../../sources/notes/acsjocguidelines.md#e33)
[^thompson2002harmonized-e1]: Thompson et al. 2002 (IUPAC technical report), §3. [Evidence](../../../sources/notes/thompson2002harmonized.md#e1)
[^thompson2002harmonized-e2]: Thompson et al. 2002 (IUPAC technical report), §3. [Evidence](../../../sources/notes/thompson2002harmonized.md#e2)
[^thompson2002harmonized-e3]: Thompson et al. 2002 (IUPAC technical report), Appendix A12. [Evidence](../../../sources/notes/thompson2002harmonized.md#e3)
[^thompson2002harmonized-e4]: Thompson et al. 2002 (IUPAC technical report), §1.1. [Evidence](../../../sources/notes/thompson2002harmonized.md#e4)
[^thompson2002harmonized-e5]: Thompson et al. 2002 (IUPAC technical report), §1.1. [Evidence](../../../sources/notes/thompson2002harmonized.md#e5)
[^thompson2002harmonized-e6]: Thompson et al. 2002 (IUPAC technical report), Appendix A11. [Evidence](../../../sources/notes/thompson2002harmonized.md#e6)
[^bligaard2016benchmarking-e1]: Bligaard et al. 2016, Abstract. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e1)
[^bligaard2016benchmarking-e8]: Bligaard et al. 2016, §2.2.1, p. 2595. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e8)
[^bligaard2016benchmarking-e15]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e15)
[^bligaard2016benchmarking-e17]: Bligaard et al. 2016, §2.3.1, p. 2597. [Evidence](../../../sources/notes/bligaard2016benchmarking.md#e17)
[^iupacgoldbookmechanism-e1]: IUPAC Gold Book, entry "mechanism of a reaction" (from the IUPAC 1994 Glossary of Terms Used in Physical Organic Chemistry). [Evidence](../../../sources/notes/iupacgoldbookmechanism.md#e1)
[^iupacgoldbookmechanism-e2]: IUPAC Gold Book, entry "mechanism of a reaction". [Evidence](../../../sources/notes/iupacgoldbookmechanism.md#e2)
[^mata2017benchmarking-e1]: Mata & Suhm 2017, Theory Benchmarking Theory. [Evidence](../../../sources/notes/mata2017benchmarking.md#e1)
[^mata2017benchmarking-e2]: Mata & Suhm 2017, Theory Benchmarking Theory. [Evidence](../../../sources/notes/mata2017benchmarking.md#e2)
[^mata2017benchmarking-e3]: Mata & Suhm 2017, Experiment Benchmarking Theory. [Evidence](../../../sources/notes/mata2017benchmarking.md#e3)
[^mata2017benchmarking-e4]: Mata & Suhm 2017, Experiment Benchmarking Theory. [Evidence](../../../sources/notes/mata2017benchmarking.md#e4)
[^mata2017benchmarking-e5]: Mata & Suhm 2017, Conclusions. [Evidence](../../../sources/notes/mata2017benchmarking.md#e5)
[^mata2017benchmarking-e6]: Mata & Suhm 2017, Conclusions. [Evidence](../../../sources/notes/mata2017benchmarking.md#e6)
[^mata2017benchmarking-e7]: Mata & Suhm 2017, Conclusions. [Evidence](../../../sources/notes/mata2017benchmarking.md#e7)
[^mata2017benchmarking-e8]: Mata & Suhm 2017, Conclusions. [Evidence](../../../sources/notes/mata2017benchmarking.md#e8)
