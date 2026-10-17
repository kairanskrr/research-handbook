# Physical sciences: field overview

This page explains how research in the physical sciences (here mainly physics and astronomy) actually works: the split between theory, experiment, and computation; collaborations of thousands of people; arXiv preprints; blind analysis and the "5σ" discovery standard; and sharing data and code. Practices shared by every field (choosing a topic, writing, peer review, research ethics) are covered in the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and in [Throughout the project](../../08_throughout/README.md), and are not repeated here. For the research strategies physics commonly uses and the evidence each one needs, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

Many of the concrete examples come from particle physics and gravitational-wave astronomy, because most of the public guidelines we found come from those two areas. Condensed matter, optics, and other areas may have different conventions; follow your group and your target journal `[Our analysis]`.

**After reading this page, you should be able to:**

- explain how work is divided in physics between theory, experiment, and computation;
- know which checkpoints a result passes through in a large collaboration on its way from analysis to publication, and what a student can and cannot do;
- understand the different roles arXiv preprints and journals play in physics;
- explain what blind analysis and 5σ are, why they are used, and what is disputed about them;
- handle authorship, data, and code the way professional societies and journals require.

---

## How research works in this field

### Theory, experiment, computation: first work out which one you are

In high-energy physics, the arXiv categories are themselves split by kind of work: experiment, theory, phenomenology, or lattice computation.

| arXiv category | What it covers |
|---|---|
| hep-ex (experiment) | Results from particle physics experiments[^arxivtaxonomy-e1] |
| hep-th (theory) | Formal aspects of quantum field theory, string theory, and so on[^arxivtaxonomy-e2] |
| hep-ph (phenomenology) | Theoretical work that connects theory and experiment[^arxivtaxonomy-e3] |
| hep-lat (lattice) | Lattice field theory, including its algorithms and special-purpose hardware[^arxivtaxonomy-e4] |

In experimental particle physics, theorists and experimentalists have clearly separate roles[^junk2021reproducibility-e21]. The models to be tested are usually published first in theory or phenomenology papers, and only then are the experiments done[^junk2021reproducibility-e23]. Experimentalists almost never test theories they proposed themselves, which reduces **confirmation bias** (seeing only the evidence that supports your own idea)[^junk2021reproducibility-e22]. Which of these you are decides what you do each day, who you work with, and what your papers look like. Ask before you join a group `[Our analysis]`.

### Big collaborations: thousands of people on one experiment

In some areas experiments are enormous, and particle physics is the classic case. A particle physics experiment takes years to design, build, and run, and needs large amounts of funding, equipment, and people[^junk2021reproducibility-e3]. The ATLAS and CMS collaborations at the Large Hadron Collider (LHC) each have more than 3,000 physicists, and neutrino experiments often have collaborations of a few hundred to over a thousand people[^junk2021reproducibility-e2]. Many papers have more than 3,000 authors[^junk2021reproducibility-e1].

In collaborations like these, a result has to pass several checkpoints before it can be published. The table gives only two examples, not a rule shared by every collaboration: the row marked "LIGO" comes from the policy of the LIGO Scientific Collaboration (LSC, which does gravitational-wave detection; LIGO is the Laser Interferometer Gravitational-Wave Observatory); the other rows come from Junk and Lyons's account, which uses the CDF collaboration (Collider Detector at Fermilab, a typical hadron collider collaboration) as its example[^junk2021reproducibility-e33]. **Your own collaboration's process is set by its own policy**:

| Checkpoint | What happens |
|---|---|
| Starting an analysis | Talk to the collaboration's statistics committee first, so you don't find out at internal review that you went the wrong way[^junk2021reproducibility-e16] |
| Preliminary results | Before a result is shown outside the collaboration, it goes through a long, formal approval process[^junk2021reproducibility-e11] |
| Internal review of the paper | A committee of members who have worked on similar topics but not on this result reviews the draft[^junk2021reproducibility-e12]; every author on the list gets a chance to review it[^junk2021reproducibility-e30]; this can take months or even years[^junk2021reproducibility-e13] |
| Before submitting or posting to arXiv (LIGO) | LIGO requires you to first establish whether internal review is needed[^ligo2018publication-e6]; internal reviewers check the most important results and comment on authorship[^ligo2018publication-e7] |
| Journal peer review | Still useful: collaborations can fall into "groupthink," and outside reviewers can catch it[^junk2021reproducibility-e15] |

Several LIGO rules affect students directly. Other collaborations may differ, but most have similar clauses, so look them up yourself `[Our analysis]`:

- A thesis may not publish an analysis claiming a detection before the collaboration has announced it[^ligo2018publication-e9];
- A thesis not reviewed by the collaboration must state in its introduction that it does not represent the collaboration's views[^ligo2018publication-e10];
- In talks outside the collaboration, you may show only results that are already public or approved by the collaboration[^ligo2018publication-e8].

Not every paper from a big collaboration is signed by thousands of people. Taking LIGO as the example: technical papers produced by one or a few institutions follow ordinary authorship principles[^ligo2018publication-e4]; for some papers, the lead authors can also request a "short author list" that names only those who contributed substantially[^ligo2018publication-e5].

### Small research groups: nobody checks your work for you

Not all physics happens in big collaborations. If you run experiments in a single research group, there is no statistics committee and no internal review committee; the checks above are up to you and your advisor `[Our analysis]`.

The thing to guard against most is "it matches the known value, so I'm done." Feynman told the history of measurements of the electron charge: when later researchers got a value too far from Millikan's, they looked for something wrong; when they got a value close to Millikan's, they stopped looking[^feynman1974cargo-e14]. His conclusion: the first principle is that you must not fool yourself, and you are the easiest person to fool[^feynman1974cargo-e7]. The particle physicist Roodman puts it more bluntly: whether a result agrees with earlier measurements says nothing about whether the measurement itself was done right[^roodman2003blind-e4]. Small experiments can be blinded too: when Dunnington measured the electron's charge-to-mass ratio, he had his machinist set a key angle arbitrarily and measured it precisely only once the analysis was finished and he was ready to publish[^roodman2003blind-e5].

### Publishing: arXiv preprints plus journals

**arXiv started in physics.** It grew out of an email preprint server for high-energy theory (hep-th) that began running in 1991[^ginsparg2011twenty-e1][^ginsparg2011twenty-e2], founded by Paul Ginsparg[^arxivabout-e1]. Before that, authors could only mail photocopies of their papers to a few people[^ginsparg2011twenty-e3], and young researchers outside elite institutions often never got them[^ginsparg2011twenty-e4].

**Today preprints and journals coexist and play different roles**[^ginsparg2011twenty-e5]. Physicists quickly accepted the practice of making papers public before peer review; other fields have not necessarily done so[^ginsparg2011twenty-e6]. A few things to know:

- **arXiv does not do peer review.** It only moderates whether a submission belongs to the subject area and has scholarly value[^arxivabout-e2]; the submitter is responsible for the content[^arxivabout-e3].
- **Your first submission needs an endorsement**, and so does your first submission to a new category[^arxivendorsement-e1]. A graduate student can ask their advisor, or a professor at their institution in the same field who also posts on arXiv, for an endorsement[^arxivendorsement-e2]. Endorsement is not peer review either[^arxivendorsement-e4].
- **The position of the American Physical Society (APS)**: preprints are a good way to share new work, and many journals do not count them as duplicate publication, but authors must check the target journal's policy themselves; once the paper is formally published, add a link to the published version on the preprint[^aps2024ethics-e8].

### Authorship

The APS Ethics Standards, revised in 2024, say:

- Authorship goes to, and must not leave out, everyone who made a significant contribution to the conception, design, execution, interpretation, or writing; every author must be able to say what they specifically did[^aps2024ethics-e4].
- Providing funding alone does not qualify someone for authorship; it belongs in the acknowledgments[^aps2024ethics-e9].
- Large collaborations can have their own authorship conventions, as long as the process is transparent[^aps2024ethics-e6]. For example, LIGO's observational papers list all qualified members in alphabetical order[^ligo2018publication-e1]; qualifying takes roughly a year of devoting at least half of your research effort to the collaboration[^ligo2018publication-e2].
- A qualified member can ask not to be listed on a particular paper[^ligo2018publication-e3]. When a collaboration cannot reach consensus, those who disagree can ask for their names to be removed[^junk2021reproducibility-e14].

An alphabetical list of thousands of names does not show who did which analysis. We found no source explaining how individual contributions in big collaborations usually become visible to outsiders; ask your advisor early how students in your group usually get their work noticed `[Our analysis]`. One point of reference: LIGO writes "encouraging young scientists and engineers to take part in presentations and publications" into its policy goals[^ligo2018publication-e11]. For general authorship practice, see [Collaboration and advisors](../../08_throughout/collaboration_and_advisors.md#6-authorship-discuss-it-at-the-start-and-adjust-as-you-go) in Throughout the project.

---

## How this field differs from others

| Aspect | Particle physics (where most of this page's evidence comes from; other areas of physics may differ) | Other fields for comparison |
|---|---|---|
| Main publication venues | Journals plus arXiv preprints, side by side[^ginsparg2011twenty-e5] | Computer science publishes mainly in conferences[^vardi2009conferences-e1]; biomedicine long recognized only peer-reviewed journal papers as establishing priority[^ginsparg2011twenty-e7] |
| Statistical threshold for claiming a "discovery" | By convention, a p-value below 2.87×10⁻⁷ (5σ)[^junk2021reproducibility-e31] | Some fields commonly use 0.05[^junk2021reproducibility-e31] |
| Review before publication | Big collaborations have strict multi-stage internal review, and many analyses are blind[^junk2021reproducibility-e32] | |

### 5σ: the threshold for claiming a "discovery"

5σ is a particle physics convention, not a rule for all of physics[^lyons2013discovering-e1]. Two terms first. The **p-value**: assuming there is only background and no new effect, the probability of seeing an effect at least this large from random fluctuations alone[^lyons2013discovering-e1]. **σ** (standard deviation): here it is a unit for expressing the p-value; "5σ" means the area of the standard normal distribution beyond 5 standard deviations on one side[^lyons2013discovering-e1].

- **The convention**: in particle physics, to claim the discovery of new physics, this probability must by convention be no larger than the area corresponding to 5σ[^lyons2013discovering-e1], that is, a p-value threshold of 2.87×10⁻⁷[^junk2021reproducibility-e4]. If you don't reach it, journals are very reluctant to let the word "discovery" appear in the title, abstract, or conclusions[^lyons2013discovering-e2].
- **Why so strict** (these are the reasons Junk and Lyons give for particle physics): historically, 3σ and 4σ effects have often disappeared once more data came in[^junk2021reproducibility-e5]. Competing collaborations need a shared threshold fixed in advance; otherwise credit for a discovery goes to whoever has the lowest standard[^junk2021reproducibility-e28].
- **What 5σ does not protect against**: **systematic errors** (biases from the instrument, calibration, or analysis method, not random fluctuations) that are not included in the uncertainty can produce false discoveries at arbitrarily high significance[^junk2021reproducibility-e7]. So however high the significance, check the systematics first `[Our analysis]`.
- **The look-elsewhere effect**: the probability of a fluctuation "exactly where you saw the peak" is the local p-value; allowing the fluctuation to appear anywhere gives the global p-value, which is larger[^lyons2013discovering-e3]. Decide the method before the analysis, and state in the paper how the global p-value is defined[^lyons2013discovering-e4].
- **Where it applies**: Junk and Lyons argue that 5σ makes more sense in particle physics than in fields such as medical trials[^junk2021reproducibility-e29]. The sources we found discuss only particle physics; we cannot confirm whether condensed matter, astronomy, or other areas have a discovery threshold, or what it is. Ask your advisor or check your target journal `[Our analysis]`.

> **Where sources disagree: does every discovery need 5σ?**
> - **For a single threshold**: the threshold itself is an arbitrary convention[^junk2021reproducibility-e6], but a standard fixed in advance and shared by competing collaborations stops a race to the lowest bar[^junk2021reproducibility-e28].
> - **Against one size fits all**: Lyons notes that statisticians are very skeptical that 5σ is reasonable[^lyons2013discovering-e5]; he argues that a uniform 5σ for every new-physics search is not sensible[^lyons2013discovering-e7], and proposes dropping the requirement that "all discoveries need 5σ"[^lyons2013discovering-e6].
>
> In practice: follow the rules of your collaboration and target journal; and in the paper, report both the local and the global p-value honestly and explain how you estimated the systematic errors `[Our analysis]`.

### Blind analysis: fix the method before you look at the answer

**Blind analysis** means making a measurement without looking at the answer[^roodman2003blind-e1]. It guards against **experimenter's bias**: a measurement being pushed, unintentionally, toward earlier results or theoretical expectations[^roodman2003blind-e2]. For example, setting a selection cut (a threshold used to select events) while knowing how it will affect the result can introduce bias[^roodman2003blind-e3]. Many analyses in experimental particle physics are blind[^junk2021reproducibility-e32].

Common approaches:

- Tune the analysis on simulated data first, fixing the event selection, classification, and statistical method, and only then run it on the real data[^junk2021reproducibility-e9];
- **Hidden signal box**: keep the region where the signal might appear hidden until the analysis is finished[^roodman2003blind-e6];
- **Hidden answer**: for precision measurements of a parameter, the usual approach is to hide the answer at first[^roodman2003blind-e7];
- Freeze the method on a small fraction of the data, then apply it unchanged to the full dataset[^roodman2003blind-e9].

The key rule: **once you unblind, you cannot change any step of the analysis; if you do, it is no longer a fully blind analysis**[^junk2021reproducibility-e10]. Not every analysis is easy to blind[^roodman2003blind-e8]. The BABAR collaboration had reservations about blind analysis at first, then made it standard practice[^roodman2003blind-e10].

> **Where sources disagree: is blind analysis worth it?**
> - **For**: Roodman considers blind analysis the best way to reduce experimenter's bias[^roodman2003blind-e1].
> - **Against**: In a short commentary that was not peer reviewed, the physicist Golub argues that blind analysis seriously hampers the search for systematic errors and makes it impossible to study unexpected events that fall in the hidden region[^golub2023blind-e1]; bringing it in to solve a problem that may not exist[^golub2023blind-e2] is, in his view, overkill[^golub2023blind-e3].
>
> In practice: before you look at the data, decide with your advisor whether and how to blind, and write it down; if you really must change something after unblinding, say in the paper what you changed and why `[Our analysis]`. For the general approach, see the research strategy [Comparative evaluation](../../05_research-strategies/compare_evaluate.md#2-what-evidence-is-enough).

---

## Norms and reporting standards in this field

**The APS Ethics Standards (revised 2024)** are the society-level code for physics:

- Physicists must tell the truth[^aps2024ethics-e1]. Honest errors are not fabrication or falsification[^aps2024ethics-e10], but if you find an error in a published paper, correct or retract it promptly[^aps2024ethics-e11].
- Don't split one study into several papers to pad your publication count[^aps2024ethics-e12]; don't submit the same paper to more than one journal at the same time[^aps2024ethics-e13].
- Publishing an abstract at a conference usually does not prevent you from submitting the full paper later, but say so when you submit[^aps2024ethics-e15].
- When you present your work in public, including on social media, either leave out implications that go beyond what has been established or clearly label them as speculation[^aps2024ethics-e14].
- Every collaboration should set up procedures to ensure its results are accurate[^aps2024ethics-e7].

**Data and code.** The APS requires research results to be recorded in a way that lets others reproduce them as far as possible[^aps2024ethics-e2], and data and code to be kept for a reasonable period[^aps2024ethics-e3]. The Physical Review journals require:

- every paper to have a Data Availability Statement[^apsdataavailability-e1]; "data and software" here means everything needed to verify or reproduce the results[^apsdataavailability-e5], so the analysis code you wrote yourself usually counts too `[Our analysis]`;
- they strongly encourage making data and software public following the FAIR principles (findable, accessible, interoperable, reusable)[^apsdataavailability-e2], and public data and software must be cited in the references[^apsdataavailability-e3];
- anything that cannot be made public must be shared privately on reasonable request[^apsdataavailability-e4]. The sample statement for a numerical simulation paper is "the source code and parameters are publicly available"[^apsdataavailability-e6].

**Citing software in astronomy.** The journals of the American Astronomical Society (AAS) recommend citing software both ways: cite the paper describing the software, and cite the software itself by its DOI (Digital Object Identifier, a permanent link); the DOI lets readers get the exact version you used[^aassoftware-e2]. The AAS strongly recommends releasing code under an open-source license[^aassoftware-e3], and it also accepts papers devoted to describing software[^aassoftware-e4]. Note: reviewers for AAS journals do not review the software itself[^aassoftware-e5], so whether your code is correct is mainly up to you `[Our analysis]`.

**Open data in big collaborations (CERN, the European Organization for Nuclear Research, as the example).** All papers from LHC experiments are open access[^cern2020opendata-e1], and supplementary data are posted to platforms such as HEPData at publication[^cern2020opendata-e2]; for reconstructed data, the goal is to start releasing them within five years of the end of a run[^cern2020opendata-e3]. If you are an outside researcher using open data, know this: you won't have the tacit knowledge the collaboration built up over years[^cern2020opendata-e4], and you are responsible for your own conclusions[^cern2020opendata-e5].

**Computational reproducibility.** Lessons from particle physics: put the computing environment under version control, not just the source code[^junk2021reproducibility-e19]; run the same program on computers with different architectures and compare the results[^junk2021reproducibility-e20]. But reproducing a result only shows the computation was done correctly, not that the assumptions and input data are sound[^junk2021reproducibility-e18]. A common flaw in published results is leaving out the correlated uncertainties, so others cannot reproduce the conclusions precisely[^junk2021reproducibility-e26]. For general practice in organizing code and data, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic a project uses to produce new knowledge, and it is set by the central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The grouping in the table below and the column "What it looks like in physics" are our own synthesis; each standard represents only the area or journal in its footnote (mostly particle physics; the rows on theoretical work come mainly from Physical Review A), and in other areas your group and target journal decide `[Our analysis]`.

| Strategy | What it looks like in physics | Common evidence and how it is judged | How to do it |
|---|---|---|---|
| [Measurement](../../05_research-strategies/measure.md) | Precision measurement of a constant, a property, or a parameter | A measurement result must come with a quantitative statement of how reliable it is[^jcgm2008gum-e1]; systematic errors left out of the uncertainty can produce false discoveries[^junk2021reproducibility-e7]; precision measurements often hide the answer at first[^roodman2003blind-e7] | [Experimental measurement](../../06_methods/experimental_measurement.md) |
| [Description](../../05_research-strategies/observe_describe.md) | Searching for new particles or effects: answering "is it there?" | In particle physics, claiming a discovery takes 5σ by convention[^junk2021reproducibility-e4]; state how the global p-value is defined[^lyons2013discovering-e4]; null results are written up as upper limits on signal strength and still published[^junk2021reproducibility-e25] | [5σ](#5σ-the-threshold-for-claiming-a-discovery) and [blind analysis](#blind-analysis-fix-the-method-before-you-look-at-the-answer) above |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Comparing computer codes or methods. For example, a community effort compared 15 solid-state codes on 71 elemental crystals[^lejaeghere2016reproducibility-e3] | Look at the pairwise differences on the same set of systems; that study found the differences between recent codes were comparable to those between different high-precision experiments[^lejaeghere2016reproducibility-e4] | [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Building and improving](../../05_research-strategies/build_improve.md) | Designing detectors and telescopes, developing data analysis methods and software[^arxivtaxonomy-e6] | Astronomy journals accept papers devoted to software[^aassoftware-e4], but reviewers do not review the software itself[^aassoftware-e5]; numerical simulation papers must state whether the code and parameters are available[^apsdataavailability-e6] | [Engineering research](../computer-science/practices/engineering_research.md) (a computer science practice, useful as a reference) |
| [Building and improving](../../05_research-strategies/build_improve.md) | Theoretical methods: developing new theoretical techniques, formalisms, or approximation methods[^aps2011uncertainty-e3] | For approximation methods, the comparison with experiment or other theory is itself an assessment of the method's error[^aps2011uncertainty-e3] | [Theoretical research](../computer-science/practices/theoretical_research.md) (a computer science practice, useful as a reference) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Theoretical explanation and phenomenology: explaining previously unexplained phenomena[^aps2011uncertainty-e3]; phenomenology means theoretical work that connects theory and experiment[^arxivtaxonomy-e3] | When explaining a phenomenon, semiquantitative agreement with experiment is already meaningful[^aps2011uncertainty-e3] | No dedicated method page yet |
| [Measurement](../../05_research-strategies/measure.md) | Precision theoretical calculation: computing values to compare with high-precision experiments, or benchmark results that serve as reference data[^aps2011uncertainty-e3] | These two kinds most need a careful assessment of theoretical uncertainty[^aps2011uncertainty-e4]; whenever feasible, give an uncertainty estimate (when it is required and how to estimate it: see below the table) | [Quantitative simulation](../../06_methods/simulation_study.md) |

Theoretical work goes into the last three rows according to its central claim: developing a new method is Building and improving, explaining a phenomenon is Causal explanation, and giving precise values to compare with experiment is Measurement `[Our analysis]`. In particle physics, the models to be tested are usually published first in theory or phenomenology papers and then measured by experimentalists[^junk2021reproducibility-e23].

The standards in these three rows come from a 2011 editorial by the editors of Physical Review A (one of the APS journals), and represent only that journal's requirements at the time. The editorial's starting point: the journal would usually not accept an experimental paper that did not discuss measurement uncertainty in detail[^aps2011uncertainty-e2], yet theory papers were not uncommonly submitted with numerical results and no uncertainty estimates[^aps2011uncertainty-e1]. What the editorial asks of theoretical calculations:

- **When you must give one.** Whenever feasible; and especially in three cases: you claim high accuracy or improvement over earlier work; the main purpose is comparison with high-precision experiments; or the main purpose is interpolating or extrapolating existing experimental data[^aps2011uncertainty-e7].
- **Where the uncertainty comes from.** First, whether the numerical results have converged, for example as the basis-set size or integration step changes; second, physical effects the calculation left out from the start[^aps2011uncertainty-e5].
- **How rigorous it must be.** What is wanted is an estimate, not the exact size of the error or a rigorous bound[^aps2011uncertainty-e6].
- **When you can't give one.** The editorial accepts that in many cases a meaningful error estimate really cannot be given, for example for scattering processes in complex systems[^aps2011uncertainty-e8].

Two other physics journals publish acceptance criteria on their websites and can serve as a comparison. Note that these apply to all submissions; they are not criteria specifically for judging theory papers. The scope of JHEP (Journal of High Energy Physics; we read the web page in 2026, and it carries no date) includes quantum field theory and string and brane theory[^jhepabout-e1], and acceptance is based on scientific quality, originality, and relevance[^jhepabout-e2]. SciPost Physics (an open-access journal of the Dutch SciPost Foundation; we read a December 2025 archive of the web page) requires a paper to meet at least one of four "expectations," such as a breakthrough on a recognized long-standing problem or opening a new direction that leads to follow-up work[^scipost2025physics-e1]; it must also meet all the general acceptance criteria, which include giving enough detail that an expert can retrace your arguments and derivations, and stating honestly in the conclusions where the results apply and what their limitations are[^scipost2025physics-e2].

Our sources do not cover how formal theory (string theory, for example[^arxivtaxonomy-e2]) is judged, or how other physics journals judge theory papers; follow your target journal.

---

## Research methods common in this field

The grouping below is our own analysis `[Our analysis]`.

- **Experimental measurement**: [Experimental measurement](../../06_methods/experimental_measurement.md) (a cross-disciplinary method). Blind analysis and 5σ, which are specific to physics experiments, are covered above. [Controlled experiments](../../06_methods/controlled_experiment.md) in Research types is about human participants and works differently.
- **Theoretical research**: see [Theoretical research](../computer-science/practices/theoretical_research.md) in the computer science section. Phenomenology has no corresponding method page.
- **Numerical computation and simulation** (computational physics, lattice computation[^arxivtaxonomy-e5][^arxivtaxonomy-e4]): [Quantitative simulation](../../06_methods/simulation_study.md).
- **Analyzing public data**: researchers outside a collaboration publish their own analyses of data released by the LHC and other experiments, and are responsible for their own conclusions[^cern2020opendata-e5]; see [Replication studies](../../06_methods/replication.md). Outside researchers lack the collaboration's tacit knowledge[^cern2020opendata-e4].

---

## Advice for newcomers

1. **In your first week, read your collaboration's publication policy all the way through.** Pay particular attention to the rules on theses, conference talks, and arXiv; for example, LIGO does not allow a thesis to publish a detection before the collaboration does[^ligo2018publication-e9]. If your group has no written policy, ask your advisor `[Our analysis]`.
2. **Before you start an analysis, write down the method and how you will blind it.** In a big collaboration, talk to the statistics committee first[^junk2021reproducibility-e16]; after unblinding, don't change the analysis steps[^junk2021reproducibility-e10].
3. **When you take over someone else's analysis, first reproduce their result.** This is the first thing new students in particle physics do[^junk2021reproducibility-e17].
4. **When your result agrees with the known value, look for mistakes just as hard.** Agreement does not mean the measurement was right[^roodman2003blind-e4]; the history of electron-charge measurements after Millikan is the cautionary tale[^feynman1974cargo-e14].
5. **Publish null results too.** If you decide to test a theory, publish whatever the outcome[^feynman1974cargo-e18]; particle physics writes null results up as upper limits and publishes them[^junk2021reproducibility-e25].
6. **From day one, organize your code and data to the standard needed for release.** You will need a data availability statement when you submit[^apsdataavailability-e1], and your code must be citable down to the exact version[^aassoftware-e2].
7. **Before posting to arXiv, check two things**: whether your collaboration requires internal review first[^ligo2018publication-e6], and the target journal's preprint policy[^aps2024ethics-e8]. After formal publication, go back and update the link[^aps2024ethics-e8].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Stopping your checks when the value matches the literature, and hunting for problems only when it doesn't | This asymmetry can keep a bias alive for a long time[^feynman1974cargo-e14]; agreement does not mean you got it right[^roodman2003blind-e4] |
| Tuning selection cuts while watching the result | Setting a cut while you know how it will affect the result introduces experimenter's bias[^roodman2003blind-e3] |
| Going back to change the analysis after unblinding because the result "doesn't look right" | Then it is no longer a blind analysis[^junk2021reproducibility-e10] |
| Calling a 3σ effect a "discovery" in particle physics | 3σ and 4σ effects often disappear with more data[^junk2021reproducibility-e5]; journals are reluctant to use the word "discovery" when the threshold is not met[^lyons2013discovering-e2] |
| Reporting only the local p-value | The global p-value is larger, and you must state how it is defined[^lyons2013discovering-e3][^lyons2013discovering-e4] |
| Posting a result to arXiv or putting it in a thesis without checking the collaboration's policy | This may break the collaboration's policy; LIGO, for example, has rules on both[^ligo2018publication-e6][^ligo2018publication-e9] |
| Listing someone who only provided funding as an author | They do not qualify for authorship; they belong in the acknowledgments[^aps2024ethics-e9] |
| Writing only "we thank such-and-such software" in the acknowledgments, without citing a specific version | Readers cannot get the exact version you used[^aassoftware-e2]; Physical Review requires public software to be cited in the references[^apsdataavailability-e3] |
| Giving only histograms in the paper, without the correlated uncertainties | Others cannot reproduce the conclusions precisely[^junk2021reproducibility-e26] |

---

## Further reading

- **Junk & Lyons 2021, Reproducibility and Replication of Experimental Particle Physics Results**: two experimental particle physicists explain how particle physics makes its results reliable, covering internal review, blind analysis, 5σ, and preserving software and data. Read this first if you want to understand how big collaborations work.
- **APS Ethics Standards (2024)**: the American Physical Society's ethics standards, with rules on authorship, duplicate publication, preprints, and data retention.
- **LIGO Publication and Presentation Policy (2018)**: the full text of a big collaboration's publication policy, showing how authorship eligibility, internal review, and thesis rules are actually written. Before you join any big collaboration, find and read its equivalent document.
- **Roodman 2003, Blind Analysis in Particle Physics**: a conference paper that clearly explains experimenter's bias and several blind analysis methods. Read it together with Golub 2023's critique. **Lyons 2013, Discovering the Significance of 5σ**: why particle physics uses 5σ, and the problems with applying 5σ across the board.
- **Feynman 1974, Cargo Cult Science**: on "not fooling yourself," including the history of measurements after Millikan's oil-drop experiment. **The Physical Review guide to data availability statements and the AAS software policy**: check against these before you submit.

[^arxivtaxonomy-e1]: arXiv Category Taxonomy, hep-ex. [Evidence](../../../sources/notes/arxivtaxonomy.md#e1)
[^arxivtaxonomy-e2]: arXiv Category Taxonomy, hep-th. [Evidence](../../../sources/notes/arxivtaxonomy.md#e2)
[^arxivtaxonomy-e3]: arXiv Category Taxonomy, hep-ph. [Evidence](../../../sources/notes/arxivtaxonomy.md#e3)
[^arxivtaxonomy-e4]: arXiv Category Taxonomy, hep-lat. [Evidence](../../../sources/notes/arxivtaxonomy.md#e4)
[^arxivtaxonomy-e5]: arXiv Category Taxonomy, physics.comp-ph. [Evidence](../../../sources/notes/arxivtaxonomy.md#e5)
[^arxivtaxonomy-e6]: arXiv Category Taxonomy, astro-ph.IM. [Evidence](../../../sources/notes/arxivtaxonomy.md#e6)
[^aps2011uncertainty-e1]: Physical Review A editors 2011, paras. 1–2. [Evidence](../../../sources/notes/aps2011uncertainty.md#e1)
[^aps2011uncertainty-e2]: Physical Review A editors 2011, para. 2. [Evidence](../../../sources/notes/aps2011uncertainty.md#e2)
[^aps2011uncertainty-e3]: Physical Review A editors 2011, para. 3. [Evidence](../../../sources/notes/aps2011uncertainty.md#e3)
[^aps2011uncertainty-e4]: Physical Review A editors 2011, para. 4. [Evidence](../../../sources/notes/aps2011uncertainty.md#e4)
[^aps2011uncertainty-e5]: Physical Review A editors 2011, para. 4. [Evidence](../../../sources/notes/aps2011uncertainty.md#e5)
[^aps2011uncertainty-e6]: Physical Review A editors 2011, para. 4. [Evidence](../../../sources/notes/aps2011uncertainty.md#e6)
[^aps2011uncertainty-e7]: Physical Review A editors 2011, para. 5. [Evidence](../../../sources/notes/aps2011uncertainty.md#e7)
[^aps2011uncertainty-e8]: Physical Review A editors 2011, para. 5. [Evidence](../../../sources/notes/aps2011uncertainty.md#e8)
[^jhepabout-e1]: JHEP, About page (accessed 2026; page undated), Scope. [Evidence](../../../sources/notes/jhepabout.md#e1)
[^jhepabout-e2]: JHEP, About page, Editorial policy. [Evidence](../../../sources/notes/jhepabout.md#e2)
[^scipost2025physics-e1]: SciPost Physics, About page (archived December 2025), Acceptance Criteria. [Evidence](../../../sources/notes/scipost2025physics.md#e1)
[^scipost2025physics-e2]: SciPost Physics, About page, Acceptance Criteria. [Evidence](../../../sources/notes/scipost2025physics.md#e2)
[^junk2021reproducibility-e1]: Junk & Lyons 2021, Abstract. [Evidence](../../../sources/notes/junk2021reproducibility.md#e1)
[^junk2021reproducibility-e2]: Junk & Lyons 2021, §1. [Evidence](../../../sources/notes/junk2021reproducibility.md#e2)
[^junk2021reproducibility-e3]: Junk & Lyons 2021, §1. [Evidence](../../../sources/notes/junk2021reproducibility.md#e3)
[^junk2021reproducibility-e4]: Junk & Lyons 2021, §3. [Evidence](../../../sources/notes/junk2021reproducibility.md#e4)
[^junk2021reproducibility-e5]: Junk & Lyons 2021, §3. [Evidence](../../../sources/notes/junk2021reproducibility.md#e5)
[^junk2021reproducibility-e6]: Junk & Lyons 2021, §3. [Evidence](../../../sources/notes/junk2021reproducibility.md#e6)
[^junk2021reproducibility-e7]: Junk & Lyons 2021, §3. [Evidence](../../../sources/notes/junk2021reproducibility.md#e7)
[^junk2021reproducibility-e9]: Junk & Lyons 2021, §6.6. [Evidence](../../../sources/notes/junk2021reproducibility.md#e9)
[^junk2021reproducibility-e10]: Junk & Lyons 2021, §6.6. [Evidence](../../../sources/notes/junk2021reproducibility.md#e10)
[^junk2021reproducibility-e11]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e11)
[^junk2021reproducibility-e12]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e12)
[^junk2021reproducibility-e13]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e13)
[^junk2021reproducibility-e14]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e14)
[^junk2021reproducibility-e15]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e15)
[^junk2021reproducibility-e16]: Junk & Lyons 2021, §6.9, Statistics Committees. [Evidence](../../../sources/notes/junk2021reproducibility.md#e16)
[^junk2021reproducibility-e17]: Junk & Lyons 2021, §4.1. [Evidence](../../../sources/notes/junk2021reproducibility.md#e17)
[^junk2021reproducibility-e18]: Junk & Lyons 2021, §4.1. [Evidence](../../../sources/notes/junk2021reproducibility.md#e18)
[^junk2021reproducibility-e19]: Junk & Lyons 2021, §6.2. [Evidence](../../../sources/notes/junk2021reproducibility.md#e19)
[^junk2021reproducibility-e20]: Junk & Lyons 2021, §4.1. [Evidence](../../../sources/notes/junk2021reproducibility.md#e20)
[^junk2021reproducibility-e21]: Junk & Lyons 2021, §7. [Evidence](../../../sources/notes/junk2021reproducibility.md#e21)
[^junk2021reproducibility-e22]: Junk & Lyons 2021, §7. [Evidence](../../../sources/notes/junk2021reproducibility.md#e22)
[^junk2021reproducibility-e23]: Junk & Lyons 2021, §7. [Evidence](../../../sources/notes/junk2021reproducibility.md#e23)
[^junk2021reproducibility-e25]: Junk & Lyons 2021, §7. [Evidence](../../../sources/notes/junk2021reproducibility.md#e25)
[^junk2021reproducibility-e26]: Junk & Lyons 2021, §4.2. [Evidence](../../../sources/notes/junk2021reproducibility.md#e26)
[^junk2021reproducibility-e28]: Junk & Lyons 2021, §3. [Evidence](../../../sources/notes/junk2021reproducibility.md#e28)
[^junk2021reproducibility-e29]: Junk & Lyons 2021, §7. [Evidence](../../../sources/notes/junk2021reproducibility.md#e29)
[^junk2021reproducibility-e30]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e30)
[^junk2021reproducibility-e31]: Junk & Lyons 2021, Media Summary. [Evidence](../../../sources/notes/junk2021reproducibility.md#e31)
[^junk2021reproducibility-e32]: Junk & Lyons 2021, §10. [Evidence](../../../sources/notes/junk2021reproducibility.md#e32)
[^junk2021reproducibility-e33]: Junk & Lyons 2021, §6.9. [Evidence](../../../sources/notes/junk2021reproducibility.md#e33)
[^ligo2018publication-e1]: LIGO LSC 2018, §2.A. [Evidence](../../../sources/notes/ligo2018publication.md#e1)
[^ligo2018publication-e2]: LIGO LSC 2018, §2.A. [Evidence](../../../sources/notes/ligo2018publication.md#e2)
[^ligo2018publication-e3]: LIGO LSC 2018, §2.A. [Evidence](../../../sources/notes/ligo2018publication.md#e3)
[^ligo2018publication-e4]: LIGO LSC 2018, §2.B. [Evidence](../../../sources/notes/ligo2018publication.md#e4)
[^ligo2018publication-e5]: LIGO LSC 2018, §2.B. [Evidence](../../../sources/notes/ligo2018publication.md#e5)
[^ligo2018publication-e6]: LIGO LSC 2018, §3.A. [Evidence](../../../sources/notes/ligo2018publication.md#e6)
[^ligo2018publication-e7]: LIGO LSC 2018, §3.B. [Evidence](../../../sources/notes/ligo2018publication.md#e7)
[^ligo2018publication-e8]: LIGO LSC 2018, §4.1. [Evidence](../../../sources/notes/ligo2018publication.md#e8)
[^ligo2018publication-e9]: LIGO LSC 2018, §5 Theses. [Evidence](../../../sources/notes/ligo2018publication.md#e9)
[^ligo2018publication-e10]: LIGO LSC 2018, §5 Theses. [Evidence](../../../sources/notes/ligo2018publication.md#e10)
[^ligo2018publication-e11]: LIGO LSC 2018, §1. [Evidence](../../../sources/notes/ligo2018publication.md#e11)
[^feynman1974cargo-e14]: Feynman 1974, after the Millikan oil-drop experiment. [Evidence](../../../sources/notes/feynman1974cargo.md#e14)
[^feynman1974cargo-e7]: Feynman 1974, after the Millikan oil-drop experiment. [Evidence](../../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e18]: Feynman 1974, publishing whatever the result. [Evidence](../../../sources/notes/feynman1974cargo.md#e18)
[^roodman2003blind-e1]: Roodman 2003, §1. [Evidence](../../../sources/notes/roodman2003blind.md#e1)
[^roodman2003blind-e2]: Roodman 2003, §2. [Evidence](../../../sources/notes/roodman2003blind.md#e2)
[^roodman2003blind-e3]: Roodman 2003, §2. [Evidence](../../../sources/notes/roodman2003blind.md#e3)
[^roodman2003blind-e4]: Roodman 2003, §2. [Evidence](../../../sources/notes/roodman2003blind.md#e4)
[^roodman2003blind-e5]: Roodman 2003, §1. [Evidence](../../../sources/notes/roodman2003blind.md#e5)
[^roodman2003blind-e6]: Roodman 2003, §3.1. [Evidence](../../../sources/notes/roodman2003blind.md#e6)
[^roodman2003blind-e7]: Roodman 2003, §3.2. [Evidence](../../../sources/notes/roodman2003blind.md#e7)
[^roodman2003blind-e8]: Roodman 2003, §3.4. [Evidence](../../../sources/notes/roodman2003blind.md#e8)
[^roodman2003blind-e9]: Roodman 2003, §3.4. [Evidence](../../../sources/notes/roodman2003blind.md#e9)
[^roodman2003blind-e10]: Roodman 2003, §4. [Evidence](../../../sources/notes/roodman2003blind.md#e10)
[^golub2023blind-e1]: Golub 2023, §2. [Evidence](../../../sources/notes/golub2023blind.md#e1)
[^golub2023blind-e2]: Golub 2023, §2. [Evidence](../../../sources/notes/golub2023blind.md#e2)
[^golub2023blind-e3]: Golub 2023, §2. [Evidence](../../../sources/notes/golub2023blind.md#e3)
[^ginsparg2011twenty-e1]: Ginsparg 2011, opening. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e1)
[^ginsparg2011twenty-e2]: Ginsparg 2011, opening. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e2)
[^ginsparg2011twenty-e3]: Ginsparg 2011, p. 2. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e3)
[^ginsparg2011twenty-e4]: Ginsparg 2011, p. 2. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e4)
[^ginsparg2011twenty-e5]: Ginsparg 2011, p. 7. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e5)
[^ginsparg2011twenty-e6]: Ginsparg 2011, p. 7. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e6)
[^ginsparg2011twenty-e7]: Ginsparg 2011, p. 7. [Evidence](../../../sources/notes/ginsparg2011twenty.md#e7)
[^arxivabout-e1]: arXiv, About arXiv. [Evidence](../../../sources/notes/arxivabout.md#e1)
[^arxivabout-e2]: arXiv, About arXiv. [Evidence](../../../sources/notes/arxivabout.md#e2)
[^arxivabout-e3]: arXiv, About arXiv. [Evidence](../../../sources/notes/arxivabout.md#e3)
[^arxivendorsement-e1]: arXiv, Endorsement. [Evidence](../../../sources/notes/arxivendorsement.md#e1)
[^arxivendorsement-e2]: arXiv, Endorsement, How can I get endorsed? [Evidence](../../../sources/notes/arxivendorsement.md#e2)
[^arxivendorsement-e4]: arXiv, Endorsement. [Evidence](../../../sources/notes/arxivendorsement.md#e4)
[^vardi2009conferences-e1]: Vardi 2009, main text, para. 2. [Evidence](../../../sources/notes/vardi2009conferences.md#e1)
[^aps2024ethics-e1]: APS Ethics Standards 2024, Integrity. [Evidence](../../../sources/notes/aps2024ethics.md#e1)
[^aps2024ethics-e2]: APS Ethics Standards 2024, Research Results. [Evidence](../../../sources/notes/aps2024ethics.md#e2)
[^aps2024ethics-e3]: APS Ethics Standards 2024, Research Results. [Evidence](../../../sources/notes/aps2024ethics.md#e3)
[^aps2024ethics-e4]: APS Ethics Standards 2024, Authorship. [Evidence](../../../sources/notes/aps2024ethics.md#e4)
[^aps2024ethics-e6]: APS Ethics Standards 2024, Authorship. [Evidence](../../../sources/notes/aps2024ethics.md#e6)
[^aps2024ethics-e7]: APS Ethics Standards 2024, Authorship. [Evidence](../../../sources/notes/aps2024ethics.md#e7)
[^aps2024ethics-e8]: APS Ethics Standards 2024, Redundant Publication. [Evidence](../../../sources/notes/aps2024ethics.md#e8)
[^aps2024ethics-e9]: APS Ethics Standards 2024, Treatment of Supervisees. [Evidence](../../../sources/notes/aps2024ethics.md#e9)
[^aps2024ethics-e10]: APS Ethics Standards 2024, Research Results. [Evidence](../../../sources/notes/aps2024ethics.md#e10)
[^aps2024ethics-e11]: APS Ethics Standards 2024, Research Results. [Evidence](../../../sources/notes/aps2024ethics.md#e11)
[^aps2024ethics-e12]: APS Ethics Standards 2024, Redundant Publication. [Evidence](../../../sources/notes/aps2024ethics.md#e12)
[^aps2024ethics-e13]: APS Ethics Standards 2024, Redundant Publication. [Evidence](../../../sources/notes/aps2024ethics.md#e13)
[^aps2024ethics-e14]: APS Ethics Standards 2024, Social Media. [Evidence](../../../sources/notes/aps2024ethics.md#e14)
[^aps2024ethics-e15]: APS Ethics Standards 2024, Redundant Publication. [Evidence](../../../sources/notes/aps2024ethics.md#e15)
[^lyons2013discovering-e1]: Lyons 2013, §1. [Evidence](../../../sources/notes/lyons2013discovering.md#e1)
[^lyons2013discovering-e2]: Lyons 2013, §1. [Evidence](../../../sources/notes/lyons2013discovering.md#e2)
[^lyons2013discovering-e3]: Lyons 2013, §2, Look Elsewhere Effect. [Evidence](../../../sources/notes/lyons2013discovering.md#e3)
[^lyons2013discovering-e4]: Lyons 2013, §2, Look Elsewhere Effect. [Evidence](../../../sources/notes/lyons2013discovering.md#e4)
[^lyons2013discovering-e5]: Lyons 2013, §2. [Evidence](../../../sources/notes/lyons2013discovering.md#e5)
[^lyons2013discovering-e6]: Lyons 2013, §4. [Evidence](../../../sources/notes/lyons2013discovering.md#e6)
[^lyons2013discovering-e7]: Lyons 2013, §3. [Evidence](../../../sources/notes/lyons2013discovering.md#e7)
[^apsdataavailability-e1]: Physical Review guidelines on data availability statements, Overview of Policies. [Evidence](../../../sources/notes/apsdataavailability.md#e1)
[^apsdataavailability-e2]: Physical Review guidelines on data availability statements, Overview of Policies. [Evidence](../../../sources/notes/apsdataavailability.md#e2)
[^apsdataavailability-e3]: Physical Review guidelines on data availability statements, Overview of Policies. [Evidence](../../../sources/notes/apsdataavailability.md#e3)
[^apsdataavailability-e4]: Physical Review guidelines on data availability statements, Overview of Policies. [Evidence](../../../sources/notes/apsdataavailability.md#e4)
[^apsdataavailability-e5]: Physical Review guidelines on data availability statements, What Qualifies as Research Data? [Evidence](../../../sources/notes/apsdataavailability.md#e5)
[^apsdataavailability-e6]: Physical Review guidelines on data availability statements, examples. [Evidence](../../../sources/notes/apsdataavailability.md#e6)
[^aassoftware-e2]: AAS Journals software policy, Guidelines for citation of software. [Evidence](../../../sources/notes/aassoftware.md#e2)
[^aassoftware-e3]: AAS Journals software policy, Guidelines for software articles. [Evidence](../../../sources/notes/aassoftware.md#e3)
[^aassoftware-e4]: AAS Journals software policy, Guidelines for software articles. [Evidence](../../../sources/notes/aassoftware.md#e4)
[^aassoftware-e5]: AAS Journals software policy, Review of Software. [Evidence](../../../sources/notes/aassoftware.md#e5)
[^cern2020opendata-e1]: CERN 2020 Open Data Policy, Level 1. [Evidence](../../../sources/notes/cern2020opendata.md#e1)
[^cern2020opendata-e2]: CERN 2020 Open Data Policy, Level 1. [Evidence](../../../sources/notes/cern2020opendata.md#e2)
[^cern2020opendata-e3]: CERN 2020 Open Data Policy, Level 3. [Evidence](../../../sources/notes/cern2020opendata.md#e3)
[^cern2020opendata-e4]: CERN 2020 Open Data Policy, Level 3. [Evidence](../../../sources/notes/cern2020opendata.md#e4)
[^cern2020opendata-e5]: CERN 2020 Open Data Policy, Level 3. [Evidence](../../../sources/notes/cern2020opendata.md#e5)
[^jcgm2008gum-e1]: JCGM 100:2008 (GUM), 0.1. [Evidence](../../../sources/notes/jcgm2008gum.md#e1)
[^lejaeghere2016reproducibility-e3]: Lejaeghere et al. 2016, Abstract. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e3)
[^lejaeghere2016reproducibility-e4]: Lejaeghere et al. 2016, Abstract. [Evidence](../../../sources/notes/lejaeghere2016reproducibility.md#e4)
