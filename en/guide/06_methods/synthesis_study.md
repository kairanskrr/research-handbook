# Synthesis and characterization studies

This page covers how to do a synthesis study well: planning the route, assessing hazards before you start, running reactions and recording conditions, workup and purification, characterizing the products, reporting yields and substrate scope, and finally writing an experimental section that someone else can follow. The examples are mostly from organic synthesis, because most of the specific guidelines we found come from that area `[Our analysis]`.

Case studies of lab accidents, the characterization requirements for new compounds, the rule that spectra must not be edited, and *Organic Syntheses*' independent checking and data sharing are already covered in the [chemistry field overview](../07_fields/chemistry/README.md); this page links there where needed. If you work on nanomaterials, thin films or devices, see the [materials engineering field overview](../07_fields/materials-engineering/README.md#one-cycle-make-it-characterize-it-test-it); for scaling up, see the [chemical engineering field overview](../07_fields/chemical-engineering/README.md#how-far-a-lab-result-is-from-industry-scale-up). The journal rules and editorials cited on this page speak only for their own journals: the author guidelines of the American Chemical Society's *The Journal of Organic Chemistry* (JOC below) and of *Organic Syntheses*, and an editorial by the editor-in-chief of *Organic Letters*. Before you submit, read your target journal's own author guidelines `[Our analysis]`.

**Scope** `[Our analysis]`: this page was originally written for the chemistry part of the Fields section, and its sources are mainly author guidelines and editorials from American Chemical Society journals and *Organic Syntheses*, plus methodological articles on organic synthesis. Besides [chemistry](../07_fields/chemistry/README.md), the field overviews for [materials engineering](../07_fields/materials-engineering/README.md) and [Chemical engineering](../07_fields/chemical-engineering/README.md) also link here. These fields' requirements for characterization and reporting are not identical; before using this page, check your field's conventions and your target journal's author guidelines.

**Strategies it usually serves**: [Building and improving](../05_research-strategies/build_improve.md#3-common-research-methods).

**After reading this page, you should be able to:**

- tell whether you are doing methodology, target-oriented synthesis, or preparing compounds for another study, and know what evidence each requires;
- record every condition that affects the outcome, and use "change one condition at a time" to find the conditions that matter;
- report yields honestly and design a substrate scope table that shows both the method's reach and its limitations;
- write procedures that someone else can repeat from your experimental section alone.

---

## 1. What this kind of study is, and when to use it

The result of a synthesis study is "we made a certain substance" or "we found a new way to make a class of substances". The evidence is a reproducible procedure, characterization data and yields `[Our analysis]`. There are three common kinds:

| | Synthetic methodology | Target-oriented synthesis (including total synthesis) | Preparing compounds for other research |
|---|---|---|---|
| Question it answers | What a new reaction or reagent can and cannot do | How to make one particular molecule | Supplying samples for physical measurements, biological testing or materials research |
| Core evidence | Substrate scope table, optimization of conditions, a reproducible general procedure | Procedure, yield and characterization for every step | Evidence of structure and purity |
| Where it most often goes wrong | Substrates picked to look "good"; failed examples not reported | Incomplete characterization of intermediates; miscalculated yields | Insufficient purity that compromises later measurements |

This table is our own summary `[Our analysis]`. Journals expect novelty. Take JOC: it expects synthetic methods and total synthesis papers to offer conceptual novelty in strategy, transformation or route, not just a known reaction rerun on a new class of substrates, reagents or catalysts[^acsjocguidelines-e30]. For compounds that will be used in physical measurements or biological testing, JOC requires evidence of at least 95% purity[^acsjocguidelines-e4]. Studies of reaction rates or mechanisms, and computational work, are outside the scope of this page; see the [chemistry field overview](../07_fields/chemistry/README.md#first-work-out-which-kind-of-chemistry-you-do).

## 2. How to do it

### Step 1: Search the literature and plan the route

**How:**

1. **First check whether the target is already known.** For known compounds made by literature methods, JOC only asks you to cite the original paper; you need not rewrite the procedure (unless you modified it)[^acsjocguidelines-e21].
2. **Do a retrosynthetic analysis** (working backward from the target molecule to starting materials). In a 2026 commentary, three AstraZeneca researchers, Kabeshov et al., describe it this way: chemists look at a target molecule and ask "What is the best way to disconnect this structure into meaningful fragments?"[^kabeshov2026retrosynthesis-e1]; experienced chemists often settle on the overall disconnection strategy first, then decide on specific functional groups and reagents[^kabeshov2026retrosynthesis-e2].
3. **Look up safety information at the same time.** The American Chemical Society's guidance on hazard assessment recommends that your literature search also look for related procedures and for known problems with the processes and chemicals you plan to use[^acs2015identifying-e10].

**Why:** Earlier procedures tell you where things go wrong. Repeating a known reaction is often faster than working everything out from scratch `[Our analysis]`.

**Where people go wrong:** Searching only for "can it be done" and not for "what went wrong when people did it" `[Our analysis]`. For literature searching in general, see the Part 1 chapter [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md#3-follow-the-citations-to-find-the-core-papers-key-people-and-venues); our sources do not cover the specific techniques of retrosynthesis, so consult an organic synthesis textbook or ask your advisor.

### Step 2: Assess hazards before every new reaction and every scale-up

For why to assess, which tools to use, and which changes call for a new assessment, see [the safety section of the chemistry field overview](../07_fields/chemistry/README.md#lab-safety-is-part-of-the-research-not-extra-paperwork). One point to stress here: **assess at the scale you plan to run.** *Organic Syntheses* requires a hazard analysis and risk assessment of every chemical and every operation before each reaction, specific to the planned scale and the laboratory where it will be done[^orgsyninstructions-e13]. Running safely on a small scale does not mean it will be safe on a larger one `[Our analysis]`. In the 2010 explosion at Texas Tech University, the students assumed that the precautions that worked for small quantities would work just as well for larger ones[^csb2011texastech-e3].

### Step 3: Run the reaction and watch it as you go

**How:** Record what *Organic Syntheses* requires in a procedure (other journals may not demand this much detail, but recording it all is the safest approach `[Our analysis]`):

- **Addition**: the order in which all reagents are added, how long each addition takes, and how they are added (syringe, addition funnel, and so on)[^orgsyninstructions-e15].
- **Temperature**: give the temperature of the reaction mixture, ideally the internal temperature (measured by a probe in the mixture)[^orgsyninstructions-e15]; for every cooling or warming step, give the start and end temperatures and how long it took[^orgsyninstructions-e16].
- **Monitoring**: say how you tracked the progress of the reaction. For thin-layer chromatography (TLC, a quick check in which you spot the sample on a silica plate, develop it, and look at the spots), give the eluent, the Rf value (the distance the spot travels divided by the distance the solvent front travels) and the visualization method[^orgsyninstructions-e17].
- **Observations**: the color of the reaction mixture, whether it is homogeneous, and changes such as color changes, gas evolution, precipitation of solids, or exotherms[^orgsyninstructions-e11].
- **Stirring**: a 2026 perspective on stirring by Schuurmans et al. recommends explicitly reporting the stirring conditions, the shape of the vessel and the addition method[^schuurmans2026stirring-e1]. It describes another group's finding that identical reactions run side by side on the same magnetic stirrer gave clearly different results depending on the position and height of the flasks[^schuurmans2026stirring-e4].

**Why:** As Schuurmans et al. explain, slow dropwise addition avoids high local concentrations, lets heat dissipate gradually, and helps maintain selectivity[^schuurmans2026stirring-e2]; inadequate stirring causes local hot spots, which can make the solvent boil, cause decomposition or even lead to a runaway reaction[^schuurmans2026stirring-e3]. So addition and stirring affect both the result and safety.

**Where people go wrong:** Writing only "stirred overnight". A 2024 perspective by Schäfer et al. points out that conditions often left out of published procedures include stirring rate, reaction time (including "overnight"), and the purity of substrates and reagents[^schafer2024sensitivity-e3].

### Step 4: Optimize conditions, and record every variable

**How:**

1. **Record every variable.** For each experiment, record at least: the amount of each material (mass and moles) and its equivalents (equiv, the moles of a reagent as a multiple of the limiting reactant), concentration, temperature, time, order of addition, and the reagents' supplier, lot number and purity `[Our analysis]`. For general rules on lab notebooks, see the [chemistry field overview](../07_fields/chemistry/README.md#lab-notebooks-write-for-the-person-who-will-check-them-later).
2. **Change one condition at a time.** The sensitivity screen was proposed by the Glorius group at the University of Münster in Germany to tackle reactions that fail to reproduce[^schafer2024sensitivity-e9]: change one condition at a time, both up and down, keep everything else fixed, and see how the yield changes; that tells you which condition to check first when troubleshooting[^schafer2024sensitivity-e2]. The changes need to be large enough: in their 2024 article the group admits that the ±10% concentration change they originally suggested is often too small, and says many groups have switched to at least ±50%[^schafer2024sensitivity-e6].
3. **When you need a fuller picture, use design of experiments.** Design of Experiments (DoE, varying several conditions at once according to a statistical plan) gives the clearest picture of how sensitive a reaction is to its conditions, but can be the most time-consuming and expensive[^schafer2024sensitivity-e8]; the authors position the sensitivity screen as a preliminary tool, with deeper assessment still requiring methods such as design of experiments[^schafer2024sensitivity-e7].
4. **Justify the amounts you use.** When a reagent is used in clear excess (for example, more than 1.5 equiv), *Organic Syntheses* requires you to explain why, ideally saying what happens with less[^orgsyninstructions-e20].

**Why:** Many conditions that look trivial change the outcome. The perspective by Schäfer et al. gives two examples: one group repurified a carboxylic acid starting material from 98.9% to 99.9% and the yield rose by 23%[^schafer2024sensitivity-e4]; another group found that different batches of a commercial palladium precatalyst gave quite different yields[^schafer2024sensitivity-e5]. They also point out that even with detailed supporting information, conditions can differ when the reaction is run in another lab or by another person[^schafer2024sensitivity-e1].

**Where people go wrong:** Careless significant figures. *Organic Syntheses* warns that writing "5.00 equiv" implies you controlled the amount to within 0.01 equiv; solution concentrations should be given in molarity, not percentages[^orgsyninstructions-e19].

### Step 5: Workup and purification

**How:** Workup means the operations after the reaction that separate the product from the reaction mixture, such as quenching (adding a reagent to stop the reaction), extraction, drying and concentration `[Our analysis]`. Specifically, write down:

- **Workup**: *Organic Syntheses* requires the composition and volume of the quenching agent, how long the addition took and at what temperature; the number of extractions, the volume of each, and the size of the separatory funnel; and the method, pressure and temperature of concentration[^orgsyninstructions-e18].
- **Purification**: *Organic Syntheses* requires the full procedure[^orgsyninstructions-e25]. When you purify by column chromatography or similar methods, JOC requires the stationary phase and the eluting solvent; if a series of compounds used different solvent ratios, give them for each compound separately[^acsjocguidelines-e27].
- **Used in the next step without purification**: *Organic Syntheses* requires you to describe separately how a sample can be purified, and to give characterization data for both the pure and the crude material[^orgsyninstructions-e14].

**Where people go wrong:** In a multistep synthesis, getting less material from one step than you then put into the next. *Organic Syntheses* explicitly requires that the amount obtained in one step be no less than the amount used in the next[^orgsyninstructions-e23].

### Step 6: Characterization: proving "what it is" and "how pure it is"

For JOC's basic requirements (proton and carbon nuclear magnetic resonance (NMR) spectra, plus high-resolution mass spectrometry or elemental analysis; neither melting point nor high-resolution mass spectrometry establishes purity) and the rule that spectra must not be edited, see the [chemistry field overview](../07_fields/chemistry/README.md#new-compounds-show-what-it-is-and-how-pure-it-is)[^acsjocguidelines-e3][^acsjocguidelines-e5]. When planning characterization, keep three more things in mind:

1. **First decide what each compound needs to prove.** New compounds need evidence of structure and purity; under JOC's rules, known compounds made by a new or improved method also need purity evidence[^acsjocguidelines-e19].
2. **Key compounds need complete data.** For branch points and convergence points on the synthetic route, and for the final new compounds, JOC requires elemental analysis or high-resolution mass spectrometry data[^acsjocguidelines-e20].
3. **Measure purity on "the batch you calculated the yield from".** *Organic Syntheses* requires purity data to be measured on the material used to calculate the yield, not on a sample that was purified further[^orgsyninstructions-e12]. Purity can be measured by quantitative NMR (qNMR) with an internal standard (a known amount of a reference compound), by gas chromatography, or by high-performance liquid chromatography[^orgsyninstructions-e21].

### Step 7: Report yields honestly

**How:** Report yields as the weighed amount of isolated, purified product (JOC's requirement)[^acsjocguidelines-e9]; for warnings about unrealistically high yields, see the [chemistry field overview](../07_fields/chemistry/README.md#new-compounds-show-what-it-is-and-how-pure-it-is). Three more points:

- **Label conversions.** Conversion is the fraction of starting material turned into product, measured by chromatography or spectroscopy rather than by weighing. When a table uses conversions, JOC requires you to say which quantity it is in the column heading or a footnote, and to give isolated yields for a few representative examples[^acsjocguidelines-e25].
- **State the scale when it varies.** When examples are run at different scales, JOC requires the mass and moles of the limiting reactant for each product[^acsjocguidelines-e24].
- **Report ranges across runs.** *Organic Syntheses* allows mass, yield and purity to be reported as ranges, with yields rounded to the nearest percent[^orgsyninstructions-e22]. If yields across runs differ by more than 10%, there may be a factor you have not yet found[^orgsyninstructions-e7]; in that case, go back to Step 4 and look for it `[Our analysis]`.

**Why:** In a 2016 editorial, Bergman and Danheiser list reporting only the best yield or selectivity as improper practice[^bergman2016reproducibility-e4].

### Step 8: Design the substrate scope table and report failed examples

Substrate scope means which substrates a new method works for and which it doesn't. Methodology papers usually show it in a table `[Our analysis]`. Much of what follows cites a 2022 editorial by Kozlowski, editor-in-chief of *Organic Letters*; it represents that journal's editorial view, not a rule for the whole field.

**How:**

1. **Choose substrates by question, not by count.** Kozlowski gives examples: good substrates each answer a question, such as whether steric bulk matters, whether a particular functional group is tolerated, or whether ketones or alkyl aldehydes also work[^kozlowski2022substrate-e4]. She also quotes a reviewer's comment: substrates should be chosen to highlight some important fact about the reaction, not just to fill a table[^kozlowski2022substrate-e10].
2. **Try the substrates readers will obviously ask about.** A reader comment she quotes says: if your aryl groups only have meta and para substituents, readers will want to know about ortho[^kozlowski2022substrate-e14].
3. **Report failed and low-yielding examples.** Kozlowski recommends putting a few low-yielding or unreactive examples in the main text or table, with a list of all failed substrates in the supporting information[^kozlowski2022substrate-e8].
4. **Discuss limitations and competing methods.** *Organic Syntheses* requires the discussion section to state the method's scope and limitations, and to describe and cite other methods that achieve the same transformation[^orgsyninstructions-e24].
5. **Scale up at least one example.** JOC requires that a new method whose examples were all run below 1 mmol include at least one example at 1 mmol scale[^acsjocguidelines-e26].

**Why:** In a 2024 paper, Rana et al. from the Glorius group at the University of Münster argue that substrate scope tables commonly suffer from two biases: selection bias, favoring substrates expected to give high yields and that are easy to obtain; and reporting bias, with most papers not reporting failed or low-yielding results[^rana2024standardizing-e1]. They stress that negative results are just as important for mapping the limits of a new reaction[^rana2024standardizing-e3]; failed examples are rarely published because researchers worry they will hurt publication[^rana2024standardizing-e4]. They also note that chemical structures come in so many combinations that even the best substrate scope will always be incomplete[^rana2024standardizing-e2]. So stating clearly "where it doesn't work" helps readers judge whether the method will work on their own molecules `[Our analysis]`.

**Where people go wrong:** Padding the count with many structurally similar substrates `[Our analysis]`. Kozlowski says the editorial office increasingly receives submissions with more than 50 substrates[^kozlowski2022substrate-e1]. For a more economical way to check functional group tolerance, she mentions screening additives instead[^kozlowski2022substrate-e5]. Rana et al. describe the "robustness screen" their group proposed earlier: add a standardized set of additives to the reaction and see how they affect the outcome, as a way to estimate the reaction's limits[^rana2024standardizing-e6].

> **Where sources disagree: how big should the substrate scope be?**
> - **Diversity matters more than numbers.** In September 2022, Kozlowski ran a poll on Twitter; of 1,909 votes, 88% favored fewer than 30 examples[^kozlowski2022substrate-e2]; her conclusion is that a smaller scope is acceptable, provided it is diverse enough[^kozlowski2022substrate-e3]. For new methods, the *Organic Letters* editors generally recommend 10–20 diverse substrates, including unreactive or low-yielding ones[^kozlowski2022substrate-e11]. Rana et al. likewise argue that substrate scopes need not be larger, but more diverse and free of bias[^rana2024standardizing-e5].
> - **A large scope can sometimes be valuable.** The same editorial concedes that the recommendation above is not a hard rule, and that more substrates are sometimes needed[^kozlowski2022substrate-e12]; in a full paper, a large substrate scope can demonstrate reproducibility and robustness, and can provide data for machine learning[^kozlowski2022substrate-e13].
>
> In practice: first choose a diverse set of substrates on the principle that "each substrate answers a question", then decide whether to expand based on the target journal and the article type (communication or full paper). That poll was just an online poll; it does not represent an agreed standard for organic chemistry as a whole `[Our analysis]`.

### Step 9: Write an experimental section and supporting information that others can reproduce

**How:** Take JOC as an example: it requires the experimental section to be detailed enough for others to reproduce the work[^acsjocguidelines-e31]. For each reaction (the first four items are JOC requirements; the sources for the rest are given):

- [ ] Give amounts of reactants, reagents and catalysts in both mass and moles; give solvent volumes and reaction times[^acsjocguidelines-e22]
- [ ] If a general procedure gives only equivalents, also give the concentration (the molarity of the limiting reactant in the reaction mixture)[^acsjocguidelines-e23]
- [ ] For heated reactions, give the temperature and the heat source (oil bath, heating mantle, and so on)[^acsjocguidelines-e28]
- [ ] Point out any unexpected, new or significant hazards in the work[^acsjocguidelines-e16]
- [ ] Include the details of addition, temperature, monitoring, workup and purification recorded in Steps 3 and 5 (*Organic Syntheses*)[^orgsyninstructions-e15][^orgsyninstructions-e18]
- [ ] Report yields as described in Step 7 (JOC)[^acsjocguidelines-e9]; for data format, the American Chemical Society encourages machine-readable data[^acsdatapolicy-e5]; see the [chemistry field overview](../07_fields/chemistry/README.md#data-supporting-information-raw-data-and-fair)
- [ ] Do an internal check before submitting: *Organic Syntheses* requires every reaction to be run at least twice at the stated scale, and recommends having a colleague who was not involved run it[^orgsyninstructions-e6]; Bergman and Danheiser also recommend having a colleague unfamiliar with the area reproduce a representative example using only the supporting information[^bergman2016reproducibility-e8]

> **Where sources disagree: should you state where reagents came from?**
> - ***Organic Syntheses***: state the source of all starting materials and reagents, and the purity of commercial reagents[^orgsyninstructions-e8].
> - **JOC**: sources are generally not given, except in three cases: uncommon starting materials, materials whose source the authors suspect affects the outcome, and catalysts; for the last two, purity must also be given[^acsjocguidelines-e29].
>
> In practice: in the paper, follow your target journal's rules; but in your notebook, record the source, lot number and purity of every reagent, because starting-material purity and catalyst batch can noticeably affect yields (see Step 4) `[Our analysis]`.

---

## 3. Checklist

**Must do** (all of these are requirements of specific journals; for other journals, follow their guidelines)

- [ ] Assess hazards at the planned scale before every new reaction and every scale-up (*Organic Syntheses*)[^orgsyninstructions-e13]
- [ ] Yields are weighed after isolation and purification, given as both mass and percentage[^acsjocguidelines-e9]; conversions are labeled separately[^acsjocguidelines-e25] (JOC)
- [ ] New compounds have evidence of structure and purity; known compounds made by a new method also have purity evidence (JOC)[^acsjocguidelines-e19]
- [ ] Key compounds have elemental analysis or high-resolution mass spectrometry data (JOC)[^acsjocguidelines-e20]
- [ ] The experimental section gives all amounts (mass and moles), solvent volumes, times, temperatures and heat sources (JOC)[^acsjocguidelines-e22][^acsjocguidelines-e28]
- [ ] Purification states the stationary phase and the eluting solvent (JOC)[^acsjocguidelines-e27]
- [ ] Do not report only your best result (editorial by Bergman and Danheiser)[^bergman2016reproducibility-e4]

**Better practice**

- [ ] When troubleshooting reproducibility, use a one-condition-at-a-time sensitivity screen to find the conditions that matter[^schafer2024sensitivity-e2]
- [ ] Report stirring conditions, vessel and addition method (recommended by Schuurmans et al.)[^schuurmans2026stirring-e1]
- [ ] The substrate scope table includes low-yielding and unreactive examples, with the full list of failed substrates in the supporting information (recommended by Kozlowski)[^kozlowski2022substrate-e8]
- [ ] Discuss limitations and competing methods (*Organic Syntheses*)[^orgsyninstructions-e24]
- [ ] Before submitting, have a colleague reproduce one example using only the supporting information[^bergman2016reproducibility-e8]

**Fine to skip; not a flaw**

- For work that is mainly synthetic, JOC sets no minimum purity, but you must honestly record the purity you achieved[^acsjocguidelines-e4]
- A substrate scope without complex substrates such as drug molecules: Kozlowski holds that these should not be a condition for publication until they are freely available[^kozlowski2022substrate-e6]
- For known compounds prepared by literature methods, don't rewrite the procedure; just cite the original paper (JOC)[^acsjocguidelines-e21]

**Criticisms common in review that are not valid**

- **"Some of these yields are too low to include."** Kozlowski notes in her editorial that authors are afraid to include negative examples for fear of displeasing reviewers[^kozlowski2022substrate-e7]; she asks *Organic Letters* reviewers to remember that negative results are not necessarily bad, and more examples are not necessarily better[^kozlowski2022substrate-e9].

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Not recording reagent lot numbers and purity in the notebook | Starting-material purity and catalyst batch can noticeably affect yields (examples described by Schäfer et al.)[^schafer2024sensitivity-e4][^schafer2024sensitivity-e5] |
| Using an NMR conversion as the yield without saying so | JOC requires you to label which quantity it is and to give isolated yields[^acsjocguidelines-e25] |
| Measuring purity on a further-purified sample while calculating the yield from a cruder batch | *Organic Syntheses* requires purity to be measured on the batch used to calculate the yield[^orgsyninstructions-e12] |
| Showing only successful examples in the substrate scope | Rana et al. call this reporting bias; readers can't tell where the method fails[^rana2024standardizing-e1] |
| Padding the count with many structurally similar substrates | Substrates should highlight some important fact about the reaction, not just fill a table (reviewer comment quoted by Kozlowski)[^kozlowski2022substrate-e10] |
| A general procedure that gives only equivalents and no concentration | Others don't know how much solvent to add; JOC requires the concentration[^acsjocguidelines-e23] |
| Yields vary a lot across runs, and only the best is reported | A difference of more than 10% may mean there is a factor you haven't found[^orgsyninstructions-e7]; reporting only the best run is improper practice[^bergman2016reproducibility-e4] |

---

## 5. Further reading

- ***Organic Syntheses* instructions for authors**: tell you item by item, from addition, temperature and monitoring to workup and purification, how much detail a procedure needs. Check your experimental section against them before you write it up.
- **Kozlowski 2022, On the Topic of Substrate Scope (*Organic Letters* editorial)**: three pages on how to choose a substrate scope and how to report failed examples, with plenty of opinions from practicing chemists.
- **Rana et al. 2024 (*ACS Central Science*, open access)**: on selection bias and reporting bias in substrate scope tables, proposing a standardized way to choose substrates based on chemical space.
- **Schäfer, Lückemeier and Glorius 2024 (*Chemical Science*, open access)**: describes how to run a sensitivity screen; worth reading when optimizing conditions or troubleshooting reactions that won't reproduce.
- **Schuurmans et al. 2026 (*ACS Central Science*, open access)**: on how stirring and addition affect results and safety.

[^acsjocguidelines-e19]: JOC author guidelines, Compound Characterization Data. [Evidence](../../sources/notes/acsjocguidelines.md#e19)
[^acsjocguidelines-e20]: JOC author guidelines, Compound Characterization Data. [Evidence](../../sources/notes/acsjocguidelines.md#e20)
[^acsjocguidelines-e21]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e21)
[^acsjocguidelines-e22]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e22)
[^acsjocguidelines-e9]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e9)
[^acsjocguidelines-e23]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e23)
[^acsjocguidelines-e24]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e24)
[^acsjocguidelines-e25]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e25)
[^acsjocguidelines-e26]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e26)
[^acsjocguidelines-e27]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e27)
[^acsjocguidelines-e28]: JOC author guidelines, Synthesis Experiments. [Evidence](../../sources/notes/acsjocguidelines.md#e28)
[^acsjocguidelines-e29]: JOC author guidelines, General Experimental Methods. [Evidence](../../sources/notes/acsjocguidelines.md#e29)
[^acsjocguidelines-e30]: JOC author guidelines, Scope of the Journal (a). [Evidence](../../sources/notes/acsjocguidelines.md#e30)
[^acsjocguidelines-e4]: JOC author guidelines, Purity. [Evidence](../../sources/notes/acsjocguidelines.md#e4)
[^acsjocguidelines-e31]: JOC author guidelines, Experimental Section. [Evidence](../../sources/notes/acsjocguidelines.md#e31)
[^acsjocguidelines-e3]: JOC author guidelines, NMR. [Evidence](../../sources/notes/acsjocguidelines.md#e3)
[^acsjocguidelines-e5]: JOC author guidelines, Purity. [Evidence](../../sources/notes/acsjocguidelines.md#e5)
[^acsjocguidelines-e16]: JOC author guidelines, Emphasis on Chemical Safety. [Evidence](../../sources/notes/acsjocguidelines.md#e16)
[^orgsyninstructions-e15]: Organic Syntheses Instructions for Authors, Reaction Procedure. [Evidence](../../sources/notes/orgsyninstructions.md#e15)
[^orgsyninstructions-e16]: Organic Syntheses Instructions for Authors, Reaction Procedure. [Evidence](../../sources/notes/orgsyninstructions.md#e16)
[^orgsyninstructions-e17]: Organic Syntheses Instructions for Authors, Reaction Procedure. [Evidence](../../sources/notes/orgsyninstructions.md#e17)
[^orgsyninstructions-e11]: Organic Syntheses Instructions for Authors, Reaction Procedure. [Evidence](../../sources/notes/orgsyninstructions.md#e11)
[^orgsyninstructions-e18]: Organic Syntheses Instructions for Authors, Reaction Workup. [Evidence](../../sources/notes/orgsyninstructions.md#e18)
[^orgsyninstructions-e19]: Organic Syntheses Instructions for Authors, Reagents (significant figures and concentrations). [Evidence](../../sources/notes/orgsyninstructions.md#e19)
[^orgsyninstructions-e20]: Organic Syntheses Instructions for Authors, Scale / reproducibility. [Evidence](../../sources/notes/orgsyninstructions.md#e20)
[^orgsyninstructions-e8]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../sources/notes/orgsyninstructions.md#e8)
[^orgsyninstructions-e12]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../sources/notes/orgsyninstructions.md#e12)
[^orgsyninstructions-e21]: Organic Syntheses Instructions for Authors, Characterization. [Evidence](../../sources/notes/orgsyninstructions.md#e21)
[^orgsyninstructions-e22]: Organic Syntheses Instructions for Authors, Scale / reproducibility. [Evidence](../../sources/notes/orgsyninstructions.md#e22)
[^orgsyninstructions-e7]: Organic Syntheses Instructions for Authors, Scale / reproducibility. [Evidence](../../sources/notes/orgsyninstructions.md#e7)
[^orgsyninstructions-e23]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../sources/notes/orgsyninstructions.md#e23)
[^orgsyninstructions-e24]: Organic Syntheses Instructions for Authors, Discussion Section. [Evidence](../../sources/notes/orgsyninstructions.md#e24)
[^orgsyninstructions-e13]: Organic Syntheses Instructions for Authors, Safety (Note 1). [Evidence](../../sources/notes/orgsyninstructions.md#e13)
[^orgsyninstructions-e25]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../sources/notes/orgsyninstructions.md#e25)
[^orgsyninstructions-e14]: Organic Syntheses Instructions for Authors, Common Omissions. [Evidence](../../sources/notes/orgsyninstructions.md#e14)
[^orgsyninstructions-e6]: Organic Syntheses Instructions for Authors, Scale / reproducibility. [Evidence](../../sources/notes/orgsyninstructions.md#e6)
[^acs2015identifying-e10]: ACS 2015, 9.4 Job Hazard Analysis. [Evidence](../../sources/notes/acs2015identifying.md#e10)
[^csb2011texastech-e3]: U.S. Chemical Safety and Hazard Investigation Board (CSB) 2011, 4.0 Incident Description. [Evidence](../../sources/notes/csb2011texastech.md#e3)
[^bergman2016reproducibility-e4]: Bergman & Danheiser 2016, Sources of Irreproducibility. [Evidence](../../sources/notes/bergman2016reproducibility.md#e4)
[^bergman2016reproducibility-e8]: Bergman & Danheiser 2016, Recommendations. [Evidence](../../sources/notes/bergman2016reproducibility.md#e8)
[^acsdatapolicy-e5]: ACS Research Data Policy, Data Availability Statements. [Evidence](../../sources/notes/acsdatapolicy.md#e5)
[^kabeshov2026retrosynthesis-e1]: Kabeshov et al. 2026, paragraph 2. [Evidence](../../sources/notes/kabeshov2026retrosynthesis.md#e1)
[^kabeshov2026retrosynthesis-e2]: Kabeshov et al. 2026, paragraph 2. [Evidence](../../sources/notes/kabeshov2026retrosynthesis.md#e2)
[^schafer2024sensitivity-e1]: Schäfer et al. 2024, Introduction. [Evidence](../../sources/notes/schafer2024sensitivity.md#e1)
[^schafer2024sensitivity-e2]: Schäfer et al. 2024, Introduction. [Evidence](../../sources/notes/schafer2024sensitivity.md#e2)
[^schafer2024sensitivity-e3]: Schäfer et al. 2024, General parameters. [Evidence](../../sources/notes/schafer2024sensitivity.md#e3)
[^schafer2024sensitivity-e4]: Schäfer et al. 2024, General parameters. [Evidence](../../sources/notes/schafer2024sensitivity.md#e4)
[^schafer2024sensitivity-e5]: Schäfer et al. 2024, Homogeneous catalysis and cross-coupling reactions. [Evidence](../../sources/notes/schafer2024sensitivity.md#e5)
[^schafer2024sensitivity-e6]: Schäfer et al. 2024, Introduction. [Evidence](../../sources/notes/schafer2024sensitivity.md#e6)
[^schafer2024sensitivity-e7]: Schäfer et al. 2024, Conclusion and outlook. [Evidence](../../sources/notes/schafer2024sensitivity.md#e7)
[^schafer2024sensitivity-e8]: Schäfer et al. 2024, Introduction. [Evidence](../../sources/notes/schafer2024sensitivity.md#e8)
[^schafer2024sensitivity-e9]: Schäfer et al. 2024, Introduction. [Evidence](../../sources/notes/schafer2024sensitivity.md#e9)
[^schuurmans2026stirring-e1]: Schuurmans et al. 2026, section on stirring and adding reagents. [Evidence](../../sources/notes/schuurmans2026stirring.md#e1)
[^schuurmans2026stirring-e2]: Schuurmans et al. 2026, section on stirring and adding reagents. [Evidence](../../sources/notes/schuurmans2026stirring.md#e2)
[^schuurmans2026stirring-e3]: Schuurmans et al. 2026, section on stirring and safety. [Evidence](../../sources/notes/schuurmans2026stirring.md#e3)
[^schuurmans2026stirring-e4]: Schuurmans et al. 2026, section on magnetic stirrer placement. [Evidence](../../sources/notes/schuurmans2026stirring.md#e4)
[^kozlowski2022substrate-e1]: Kozlowski 2022, opening. [Evidence](../../sources/notes/kozlowski2022substrate.md#e1)
[^kozlowski2022substrate-e2]: Kozlowski 2022, opening. [Evidence](../../sources/notes/kozlowski2022substrate.md#e2)
[^kozlowski2022substrate-e3]: Kozlowski 2022, opening. [Evidence](../../sources/notes/kozlowski2022substrate.md#e3)
[^kozlowski2022substrate-e4]: Kozlowski 2022, paragraph explaining Figure 2. [Evidence](../../sources/notes/kozlowski2022substrate.md#e4)
[^kozlowski2022substrate-e5]: Kozlowski 2022, paragraph explaining Figure 2. [Evidence](../../sources/notes/kozlowski2022substrate.md#e5)
[^kozlowski2022substrate-e6]: Kozlowski 2022, Drug-like Structures or Not? [Evidence](../../sources/notes/kozlowski2022substrate.md#e6)
[^kozlowski2022substrate-e7]: Kozlowski 2022, Substrates That Do Not Work. [Evidence](../../sources/notes/kozlowski2022substrate.md#e7)
[^kozlowski2022substrate-e8]: Kozlowski 2022, Substrates That Do Not Work. [Evidence](../../sources/notes/kozlowski2022substrate.md#e8)
[^kozlowski2022substrate-e9]: Kozlowski 2022, Reviewers. [Evidence](../../sources/notes/kozlowski2022substrate.md#e9)
[^kozlowski2022substrate-e10]: Kozlowski 2022, Reviewers. [Evidence](../../sources/notes/kozlowski2022substrate.md#e10)
[^kozlowski2022substrate-e11]: Kozlowski 2022, Reasonable Substrate Scope Examples. [Evidence](../../sources/notes/kozlowski2022substrate.md#e11)
[^kozlowski2022substrate-e12]: Kozlowski 2022, Reasonable Substrate Scope Examples. [Evidence](../../sources/notes/kozlowski2022substrate.md#e12)
[^kozlowski2022substrate-e13]: Kozlowski 2022, Reasonable Substrate Scope Examples. [Evidence](../../sources/notes/kozlowski2022substrate.md#e13)
[^kozlowski2022substrate-e14]: Kozlowski 2022, Substrates That Do Not Work. [Evidence](../../sources/notes/kozlowski2022substrate.md#e14)
[^rana2024standardizing-e1]: Rana et al. 2024, Introduction. [Evidence](../../sources/notes/rana2024standardizing.md#e1)
[^rana2024standardizing-e2]: Rana et al. 2024, Introduction. [Evidence](../../sources/notes/rana2024standardizing.md#e2)
[^rana2024standardizing-e3]: Rana et al. 2024, Results and Discussion. [Evidence](../../sources/notes/rana2024standardizing.md#e3)
[^rana2024standardizing-e4]: Rana et al. 2024, Results and Discussion. [Evidence](../../sources/notes/rana2024standardizing.md#e4)
[^rana2024standardizing-e5]: Rana et al. 2024, Conclusions. [Evidence](../../sources/notes/rana2024standardizing.md#e5)
[^rana2024standardizing-e6]: Rana et al. 2024, Introduction. [Evidence](../../sources/notes/rana2024standardizing.md#e6)
