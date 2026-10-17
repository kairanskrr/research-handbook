# Mechanical engineering: field overview

This page explains how research runs in mechanical engineering (fluids, thermal engineering, solid mechanics, dynamics and control, manufacturing, robot hardware, and related areas). Conclusions here usually come from two places: measurements on a test rig and numerical simulations on a computer. For both, you have to state clearly "how accurate" the result is. For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md); for the research strategies this field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). For issues shared with other fields that deal with hardware, measurement, and patents, compare the [Electrical engineering page](../electrical-engineering/README.md). This page covers only what is specific to this field.

**After reading this page, you should be able to:**

- explain what experiments, numerical simulation, and "design, build, test" each contribute, and what standards each is judged by;
- know why measurement results must come with an uncertainty, and what some journals require about it;
- know the hard requirements some journals set for numerical accuracy (grid convergence, iterative convergence);
- tell calibration from validation;
- using the American Society of Mechanical Engineers (ASME) as an example, understand the rules on turning conference papers into journal papers, authorship, and conflicts of interest;
- know the most basic safety rules before you enter a machine shop or work on a test rig.

---

## How research works in this field

### Where results come from: test rigs, numerical simulation, and prototypes

Mechanical engineering research commonly takes three approaches, and a single project often combines them:

- **Experiments**: measurements on test rigs, in wind tunnels and water channels, and on materials testing machines. Whether the conclusions hold up depends heavily on how accurate the measurements are (see "Measurement results must come with an uncertainty" below).
- **Numerical simulation**: for example, computational fluid dynamics (CFD, solving the flow equations on a computer) and finite element analysis (FEA, commonly used for structures and heat transfer). Whether the conclusions hold up depends on whether numerical error has been controlled and whether the model has been checked against experiments (see "Numerical results must show the grid is fine enough" below).
- **Design, build, test**: propose a new mechanism, structure, or control method, build a prototype, and measure its performance on a test rig. The logic is the same as [Engineering research](../computer-science/practices/engineering_research.md) on the Computer science page: first state your claims clearly, then choose a way to validate each one.

This kind of work is often held up by hardware: machining parts, building a rig, and booking a wind tunnel all take time, and one assembly mistake can mean redoing the work. For scheduling methods, see [Planning and daily routines](../../08_throughout/planning_and_routines.md) in Throughout the project.

### Publishing: ASME as an example

ASME runs both journals and conferences. Its broad annual conference is the International Mechanical Engineering Congress and Exposition (IMECE). The 2026 meeting has nearly 20 technical tracks[^asme2026imece-e1], including fluids engineering, heat transfer and thermal engineering, and mechanics of solids, structures, and fluids[^asme2026imece-e2]. The schedule: abstracts due March 10[^asme2026imece-e3], full papers for review submitted from May 5[^asme2026imece-e4], reviews completed by June 9[^asme2026imece-e8], final papers due August 11[^asme2026imece-e6], and the conference itself in November[^asme2026imece-e7]. That is about eight months from abstract to conference. You can also submit an abstract only and give a presentation or a poster without a paper[^asme2026imece-e5]. For other conferences, check the conference website.

**Turning a conference paper into a journal paper (ASME journal rules).** ASME journals accept papers that were presented at a conference, but you must say which conference and what you changed since[^asmeconfpapers-e1]; whether the paper is sent for review and published is up to the journal's editor[^asmeconfpapers-e2]. If it was an ASME conference, you must wait until you receive the conference acceptance notice before submitting to an ASME journal, to avoid duplicate submission[^asmeconfpapers-e3]. The journal reviews the paper again, independently[^asmeconfpapers-e4], and the journal version must cite the conference version in a footnote and in the references[^asmeconfpapers-e5]. If you submit to other publishers (such as Elsevier, Springer, or Chinese journals), follow their rules.

**Journals or conferences?** Our sources have no direct count of whether mechanical engineering papers appear in journals or at conferences, only one piece of indirect data: Lisée and colleagues in 2008 analyzed the references of journal papers indexed in the Thomson citation indexes (the forerunner of today's Web of Science) from 1980 to 2005[^lisee2008conference-e1]. Over those 26 years, about 8% of the works cited by mechanical engineering papers were conference papers, against 19.6% for computer science; both were among the subfields with the highest shares of conference papers[^lisee2008conference-e2]. Across all natural science and engineering papers in 2005, conference papers made up only about 1.7% of references[^lisee2008conference-e3]. So mechanical engineering journal papers mostly cite things other than conference papers, but conference papers carry more weight than in most fields; note that this counts what papers cite, not where they are published. Individual areas (robotics, for example) may differ; follow your advisor and the requirements of your target journals and conferences.

**How long review takes (cross-field figures, for reference only).** A study by Björk and Solomon, published in 2013, took a stratified random sample of 2,700 papers from 135 journals in the Scopus citation database[^bjork2013publishing-e1]; for each journal they took the last 20 papers published in 2012, counting backward, and roughly grouped the journals into nine disciplines such as engineering, earth sciences, and social sciences[^bjork2013publishing-e2]. The "submission to acceptance" interval reflects time spent on review and revision; the "acceptance to publication" interval reflects the production process and the queue for publication[^bjork2013publishing-e3]. For engineering journals these averaged 5.0 months and 4.3 months[^bjork2013publishing-e4]. But the differences between journals within a group were much larger than the differences between groups[^bjork2013publishing-e5]. The study does not break out mechanical engineering, and the data are more than ten years old, so use them only as a rough guide; for how long your target journal actually takes, go by the figures the journal publishes.

### Authorship: consider the people who run experiments and build rigs

ASME's criteria for interpreting its Code of Ethics (2012 edition) state that when research involving several people (including students and advisors, and managers or researchers in industry) is written up as a paper, thesis, or report, all significant contributors must be acknowledged, and coauthors should agree on the authorship arrangement before submission[^asme2012canons-e1]. ASME's publication ethics standards on its website require that only those who made significant contributions both to the research and to writing the paper be listed as coauthors[^asmeethicalstandards-e6]. So whether the people who build the test rig or do the machining become authors or go in the acknowledgments is best settled with your advisor at the start of the project. For general principles, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#5-authorship-citation-and-conflicts-of-interest-give-every-contributor-due-credit) in Throughout the project.

---

## How this field differs from others

The table below is our own summary, only meant to help you spot the differences quickly.

| | Mechanical engineering | Computer science |
|---|---|---|
| Where results come from | Test-rig measurements, numerical simulation (fluids, structures, heat transfer), prototype testing | Mainly experiments on code, systems, and data |
| How you state "how accurate" | Measurement results come with an uncertainty[^jcgm2008gum-e1]; some journals require numerical results to demonstrate grid convergence[^jfenumaccuracy-e2] | Mostly repeated runs and statistical tests (see the Part 2 chapter section [Report how big and how certain, not just the p-value](../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value)) |
| What sets the pace | Also machining, rig building, and equipment booking | Mainly conference deadlines |
| Safety | Machine shops and test rigs carry a risk of physical injury (see below) | Not covered on the Computer science page |

---

## Norms and reporting standards in this field

### Measurement results must come with an uncertainty

The internationally accepted reference is the *Guide to the Expression of Uncertainty in Measurement* (GUM) from the Joint Committee for Guides in Metrology (JCGM), free to download from the website of the International Bureau of Weights and Measures (BIPM). The GUM gives the reason in its opening: when you report the result of a measurement of a physical quantity, you must give some quantitative indication of its quality so that users can assess how reliable it is; without it, measurement results cannot be compared, either with each other or with reference values given in a standard[^jcgm2008gum-e1].

For how to define the measurand, calibrate, draw up an uncertainty budget, and compute the expanded uncertainty, see the cross-field method [Experimental measurement](../../06_methods/experimental_measurement.md#step-5-build-an-uncertainty-budget). In this field, watch two more things:

**"Accuracy" does not get a number.** Technical Note 1297 of the US National Institute of Standards and Technology (NIST) points out that accuracy is a qualitative concept and that numbers should be attached to uncertainty instead[^taylor1994nist-e2]; it also notes that "precision" is often used simply to mean "repeatability"[^taylor1994nist-e3]. When you read the literature, first check how the authors use these words.

**What journals require (the American Institute of Aeronautics and Astronautics, AIAA, as an example).** AIAA journals state that experimental papers that do not adequately describe the accuracy of their data will not be accepted[^aiaaeditorialpolicy-e1], with enforcement by each journal's editor-in-chief and the responsible associate editor[^aiaaeditorialpolicy-e2]. Authors must estimate the bias uncertainty and explain how[^aiaaeditorialpolicy-e3], quantify the precision (repeatability) of the results[^aiaaeditorialpolicy-e4], identify known sources not included in the total uncertainty[^aiaaeditorialpolicy-e5], describe the experimental conditions and the order in which data were taken[^aiaaeditorialpolicy-e6], and state the coverage factor[^aiaaeditorialpolicy-e8]. If you submit to other journals, check the target journal's instructions for authors first.

### Numerical results must show the grid is fine enough

The results of a numerical simulation change with grid resolution, time step, and when you stop iterating. Some journals set hard requirements because of this.

**The editorial policy of the *Journal of Fluids Engineering* (published by ASME).** The journal will not consider numerical papers that fail to test truncation error systematically and estimate accuracy[^jfenumaccuracy-e1]. Some of its points:

- the numerical method must be described specifically; writing "a conservative finite-volume scheme" and citing a general textbook is not enough[^jfenumaccuracy-e4];
- you must show solutions on several grids of significantly different resolution, demonstrating that the results are grid-independent or converge with grid refinement[^jfenumaccuracy-e2];
- the stopping criterion for iterative calculations must be stated, and the convergence error estimated[^jfenumaccuracy-e6];
- comparing with experiments is fine, but the experimental uncertainty must be established first; computing on a single grid and showing "reasonable agreement" with experiments is not enough, especially when there are adjustable parameters[^jfenumaccuracy-e3].

The editors also acknowledge that many practical engineering calculations will still be done on a single grid, but that such analyses are not suitable for publication in this journal[^jfenumaccuracy-e5].

**The procedure of Celik and colleagues (2008)** (published in the same PDF as this policy):

1. First show that the iterations have converged: the normalized residuals of each equation should drop by at least three (preferably four) orders of magnitude[^celik2008procedure-e1];
2. compute the key quantities on three significantly different grids, preferably with a grid refinement factor greater than 1.3 (the authors note this is an empirical value)[^celik2008procedure-e2];
3. estimate the discretization error with the Grid Convergence Index (GCI) method in the paper; if you use it, reviewers will not question the method itself[^celik2008procedure-e4];
4. when plotting profiles, show the numerical uncertainty with error bars, as you would for experimental data[^celik2008procedure-e6];
5. study and report how sensitive the solution is to small perturbations in the inlet conditions[^celik2008procedure-e3].

In their worked example, Celik and colleagues specifically note that the numerical uncertainty calculated this way does not include modeling error[^celik2008procedure-e5]. In other words, grid convergence shows only that you solved the equations accurately, not that you chose the right equations.

AIAA also has requirements for numerical papers; for example, if commercial codes play an important part in your simulations, you must give references for publicly available code testing[^aiaaeditorialpolicy-e7].

### Calibration is not validation

For general methods of verification (checking that the equations are solved correctly) and validation (checking that the model is accurate enough for the real world), see [Quantitative simulation](../../06_methods/simulation_study.md#step-3-verification-and-validation) in Research types. As Oberkampf and Trucano of Sandia National Laboratories in the US put it in 2002, verification is primarily a mathematics issue and validation is primarily a physics issue[^oberkampf2002verification-e2].

The third thing this field must watch out for is **calibration**. Calibration means adjusting parameters so that computed results match experimental data[^oberkampf2002verification-e5]. Tuning parameters to an experiment and then claiming the model has been "validated" is a confusion. They point out that calibrating CFD codes to experimental measurements is so common that many people cannot tell whether they are calibrating or validating[^oberkampf2002verification-e7].

They call experiments designed specifically to test a computational model "validation experiments", and recommend that experimentalists, model developers, code developers, and code users design them together from start to finish[^oberkampf2002verification-e6], and that the same validation experiment be run in different facilities where possible[^oberkampf2002verification-e10]. Another practice: once the experimental data are processed, do not show the results to the computational side; give them only all the conditions they need to set up the calculation[^oberkampf2002verification-e8]. The computational side first quantifies the error and uncertainty in its own solution, and only then compares with the experiment[^oberkampf2002verification-e9]. This is close in spirit to [blind analysis](../physical-sciences/README.md#blind-analysis-fix-the-method-before-you-look-at-the-answer) in physics. The authors also say, however, that this strict independence is aimed at codes used for engineering analysis; codes developed by university researchers need not go that far[^oberkampf2002verification-e11].

### ASME's Code of Ethics

ASME requires its members to follow its Code of Ethics of Engineers[^asme2024ethics-e1]. The points below are the ones most relevant to research, and all are ASME rules; societies in other countries (such as the Chinese Mechanical Engineering Society) have their own codes, which our sources do not cover. Follow the rules of your institution and target journal.

- **Public safety comes first**[^asme2024ethics-e2]. If you find a situation directly related to your work that may endanger public safety or health, report it to your superiors and the relevant authorities[^asme2012canons-e6].
- **Avoid conflicts of interest**, and the appearance of them[^asme2024ethics-e4]. When you submit, disclose to the editor, for example, any consulting relationship or financial interest in a company that could be affected by the paper's results[^asmeethicalstandards-e4].
- **Respect others' proprietary information and intellectual property**[^asme2024ethics-e5]; do not disclose confidential information such as an employer's or client's technical processes without consent[^asme2012canons-e4].

ASME also has the general requirements: give enough detail for peers to repeat the work, no duplicate submission, no plagiarism[^asmeethicalstandards-e1][^asmeethicalstandards-e3][^asme2012canons-e2]; see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md) in Throughout the project.

### Industry-funded research: settle intellectual property and publication first

When working with a company, two ASME rules apply:

- Before doing work for others that may lead to inventions or designs (which may be patented or otherwise proprietary), make a clear agreement with all parties on who owns the rights[^asme2012canons-e3].
- Authors must make sure that no contractual or proprietary considerations prevent publication of the paper[^asmeethicalstandards-e5]. So when you sign the contract, ask clearly: can the results be published, and does the company get to review them before publication?

For whether you must disclose an invention to your university before collaborating, what counts as "public disclosure", and what happens to a patent after disclosure, see [Publish or patent](../electrical-engineering/README.md#publish-or-patent-the-us-as-the-example) on the Electrical engineering page (which cites guidance from several US universities).

### Safety in the machine shop and at the test rig

The examples below are from the US; laws and institutional rules differ, so before you enter a lab, follow your own institution's safety training and regulations.

**What the US Occupational Safety and Health Administration (OSHA) says.** Moving machine parts can cause crushed fingers, amputations, burns, or blindness[^oshamachineguarding-e1]. OSHA requires that any machine part, function, or process that may cause injury be safeguarded[^oshamachineguarding-e2]. During maintenance, unexpected startup of a machine or release of stored energy can cause serious injury or death[^oshalockout-e1]; the remedy is lockout/tagout[^oshalockout-e2]: cut off the energy source, then lock it and attach a warning tag so nobody switches it on by mistake.

**Carnegie Mellon University's machine shop safety guideline** (representing only that university's rules):

- you must be trained and show you are competent before using a machine[^cmu2025machineshop-e1], including a general shop safety course and specific training for each machine[^cmu2025machineshop-e2];
- never work alone: at least two people must be in the shop[^cmu2025machineshop-e3];
- before starting, check that guards over moving parts are in place[^cmu2025machineshop-e5]; do not wear gloves when using tools with rotating parts such as drill presses and saws, so your hand does not get pulled in[^cmu2025machineshop-e4];
- never leave a running machine unattended[^cmu2025machineshop-e8]; make sure power is off, lockout/tagout is applied, and safety devices are in place[^cmu2025machineshop-e7];
- rushing is unsafe; if a job cannot be done safely, do not start it[^cmu2025machineshop-e6].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists only the two strategies this page's sources support; our sources do not cover the other strategies. The grouping and the second column are our own summary, and each standard represents only the guideline or journal named in its footnote.

| Strategy | What it looks like in mechanical engineering | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Design, build, test: propose a new mechanism, structure, or control method, build a prototype, and test it on a rig; or evaluate a design in numerical simulation | Measurement results come with an uncertainty, or they cannot be compared with anyone else's[^jcgm2008gum-e1]; the *Journal of Fluids Engineering* requires showing convergence on several grids of significantly different resolution[^jfenumaccuracy-e2], and a single grid with rough agreement with experiments is not enough[^jfenumaccuracy-e3]; tuning parameters to experiments is calibration[^oberkampf2002verification-e5], not validation[^oberkampf2002verification-e7] | [Engineering research](../computer-science/practices/engineering_research.md) (Computer science page), [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Measurement](../../05_research-strategies/measure.md) | Measuring a quantity accurately on a test rig, in a wind tunnel or water channel, and stating how accurate it is; also validation experiments designed to test computational models | List all uncertainty components and explain how each was evaluated[^jcgm2008gum-e8], and state the coverage factor when you report an expanded uncertainty[^jcgm2008gum-e9]; AIAA journals do not accept experimental papers that do not adequately describe the accuracy of their data[^aiaaeditorialpolicy-e1]; validation experiments are designed jointly by experimentalists, modelers, code developers, and code users[^oberkampf2002verification-e6] | [Experimental measurement](../../06_methods/experimental_measurement.md) |

How to use this table: pick your main strategy from your central claim. For example, if you build a new prototype and measure its efficiency, the claim is "the new design is better", so it is judged by the standards of building and improving; the measurement part must still meet the standards of measurement.

## Research methods common in this field

This field has no method pages of its own; it uses the cross-field methods in [Research types](../../06_methods/README.md) and the practices from the Computer science page:

- [Experimental measurement](../../06_methods/experimental_measurement.md): measurements on test rigs, in wind tunnels, and at similar facilities; for journal requirements, see [Measurement results must come with an uncertainty](#measurement-results-must-come-with-an-uncertainty) above.
- [Quantitative simulation](../../06_methods/simulation_study.md): that page's examples are discrete-event, system dynamics, and agent-based simulation; simulation in this field mostly solves partial differential equations and must also report numerical errors such as grid convergence and iterative convergence; see [Numerical results must show the grid is fine enough](#numerical-results-must-show-the-grid-is-fine-enough) above.
- [Engineering research](../computer-science/practices/engineering_research.md) and [Optimization studies](../computer-science/practices/optimization_study.md) (Computer science page): in structural or shape optimization where every evaluation runs a simulation, how far you can trust the result also depends on the numerical accuracy of each simulation.

---

## Advice for newcomers

1. **Give every measurement result an uncertainty, and explain how you evaluated it.** Without it, your results cannot be compared with anyone else's[^jcgm2008gum-e1][^jcgm2008gum-e8].
2. **If you do numerical simulation, plan three grids from the start.** Do not wait for a reviewer to ask[^celik2008procedure-e2].
3. **If you tuned parameters, call it "calibration", not "validation".**[^oberkampf2002verification-e5][^oberkampf2002verification-e7]
4. **If you do computation, sit down with the experimentalists early.** Decide together what to measure and how[^oberkampf2002verification-e6].
5. **Before you sign an industry collaboration contract, ask about publication and intellectual property.**[^asme2012canons-e3][^asmeethicalstandards-e5]
6. **Don't touch a machine you haven't been trained on, don't go into the shop alone, and don't rush.**[^cmu2025machineshop-e1][^cmu2025machineshop-e3][^cmu2025machineshop-e6]

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Giving only means for experimental data, with no uncertainty | Others cannot judge reliability or make comparisons[^jcgm2008gum-e1] |
| Reporting only the statistical uncertainty from repeated measurements, leaving out sources such as instruments and calibration | The GUM lists many sources beyond the scatter of repeated measurements[^jcgm2008gum-e2] |
| Writing "accuracy ±2%" as if it were a quantitative figure | NIST Technical Note 1297 points out that accuracy is a qualitative concept and numbers belong to uncertainty[^taylor1994nist-e2] |
| Computing on a single grid and drawing conclusions from rough agreement with experiments | The *Journal of Fluids Engineering* says explicitly that this is not enough, especially with adjustable parameters[^jfenumaccuracy-e3] |
| Assuming that once the grid has converged, the result is "right" | Numerical uncertainty does not include modeling error[^celik2008procedure-e5] |
| Submitting an ASME conference paper to an ASME journal before receiving the acceptance notice | ASME requires you to wait for the acceptance notice before submitting[^asmeconfpapers-e3] |

---

## Further reading

- **JCGM 100:2008 (GUM)**: the internationally accepted guide to measurement uncertainty, free to download from the BIPM website. Read it before writing your first experimental paper.
- **NIST Technical Note 1297 (Taylor and Kuyatt 1994)**: NIST's guidelines for evaluating and expressing the uncertainty of its own measurement results, with an appendix explaining terminology. Read it if you want something shorter to start with.
- **The *Journal of Fluids Engineering* numerical accuracy policy and the Celik et al. 2008 procedure**: a single PDF on the ASME website, with a complete worked Grid Convergence Index example. Read it before doing CFD.
- **AIAA Editorial Policy Statement on Numerical and Experimental Accuracy**: lists reporting requirements for both numerical and experimental work; use it as a pre-submission checklist.
- **Oberkampf and Trucano 2002, Verification and Validation in Computational Fluid Dynamics**: a systematic treatment of verification and validation; Section 4.3, "Guidelines for validation experiments", is useful for both experimentalists and computational researchers.
- **Your institution's lab safety training and technology transfer office guidance**: this page cites rules from US institutions; follow your own institution's.

[^oberkampf2002verification-e2]: Oberkampf & Trucano 2002, §1.1. [Evidence](../../../sources/notes/oberkampf2002verification.md#e2)
[^oberkampf2002verification-e5]: Oberkampf & Trucano 2002, §4.1. [Evidence](../../../sources/notes/oberkampf2002verification.md#e5)
[^oberkampf2002verification-e6]: Oberkampf & Trucano 2002, §4.3, Guideline 1. [Evidence](../../../sources/notes/oberkampf2002verification.md#e6)
[^oberkampf2002verification-e7]: Oberkampf & Trucano 2002, §4.3, Guideline 4. [Evidence](../../../sources/notes/oberkampf2002verification.md#e7)
[^oberkampf2002verification-e8]: Oberkampf & Trucano 2002, §4.3, Guideline 4. [Evidence](../../../sources/notes/oberkampf2002verification.md#e8)
[^oberkampf2002verification-e9]: Oberkampf & Trucano 2002, §4.3, Guideline 4. [Evidence](../../../sources/notes/oberkampf2002verification.md#e9)
[^oberkampf2002verification-e10]: Oberkampf & Trucano 2002, §4.3. [Evidence](../../../sources/notes/oberkampf2002verification.md#e10)
[^oberkampf2002verification-e11]: Oberkampf & Trucano 2002, §4.3, Guideline 4. [Evidence](../../../sources/notes/oberkampf2002verification.md#e11)
[^asme2026imece-e1]: ASME, IMECE 2026 conference homepage, conference overview. [Evidence](../../../sources/notes/asme2026imece.md#e1)
[^asme2026imece-e2]: ASME, IMECE 2026 conference homepage, Program – Tracks & Special Symposia. [Evidence](../../../sources/notes/asme2026imece.md#e2)
[^asme2026imece-e3]: ASME, IMECE 2026 conference homepage, Important Dates. [Evidence](../../../sources/notes/asme2026imece.md#e3)
[^asme2026imece-e4]: ASME, IMECE 2026 conference homepage, Important Dates. [Evidence](../../../sources/notes/asme2026imece.md#e4)
[^asme2026imece-e5]: ASME, IMECE 2026 conference homepage, Important Dates. [Evidence](../../../sources/notes/asme2026imece.md#e5)
[^asme2026imece-e6]: ASME, IMECE 2026 conference homepage, Important Dates. [Evidence](../../../sources/notes/asme2026imece.md#e6)
[^asme2026imece-e7]: ASME, IMECE 2026 conference homepage, page header. [Evidence](../../../sources/notes/asme2026imece.md#e7)
[^asme2026imece-e8]: ASME, IMECE 2026 conference homepage, Important Dates. [Evidence](../../../sources/notes/asme2026imece.md#e8)
[^asmeconfpapers-e1]: ASME journal author guidelines, Papers Presented at a Conference, Conferences. [Evidence](../../../sources/notes/asmeconfpapers.md#e1)
[^asmeconfpapers-e2]: ASME journal author guidelines, Papers Presented at a Conference, Conferences. [Evidence](../../../sources/notes/asmeconfpapers.md#e2)
[^asmeconfpapers-e3]: ASME journal author guidelines, Papers Presented at a Conference, ASME Conferences. [Evidence](../../../sources/notes/asmeconfpapers.md#e3)
[^asmeconfpapers-e4]: ASME journal author guidelines, Papers Presented at a Conference, ASME Conferences. [Evidence](../../../sources/notes/asmeconfpapers.md#e4)
[^asmeconfpapers-e5]: ASME journal author guidelines, Papers Presented at a Conference, ASME Conferences. [Evidence](../../../sources/notes/asmeconfpapers.md#e5)
[^asme2012canons-e1]: ASME Criteria for Interpretation of the Canons 2012, 2.f.(1). [Evidence](../../../sources/notes/asme2012canons.md#e1)
[^asme2012canons-e2]: ASME Criteria for Interpretation of the Canons 2012, 2.g. [Evidence](../../../sources/notes/asme2012canons.md#e2)
[^asme2012canons-e3]: ASME Criteria for Interpretation of the Canons 2012, 4.l. [Evidence](../../../sources/notes/asme2012canons.md#e3)
[^asme2012canons-e4]: ASME Criteria for Interpretation of the Canons 2012, 4.j.(1). [Evidence](../../../sources/notes/asme2012canons.md#e4)
[^asme2012canons-e6]: ASME Criteria for Interpretation of the Canons 2012, 1.c.(3). [Evidence](../../../sources/notes/asme2012canons.md#e6)
[^asmeethicalstandards-e1]: ASME, Ethical Standards, Ethical Obligations of Authors. [Evidence](../../../sources/notes/asmeethicalstandards.md#e1)
[^asmeethicalstandards-e3]: ASME, Ethical Standards, Ethical Obligations of Authors. [Evidence](../../../sources/notes/asmeethicalstandards.md#e3)
[^asmeethicalstandards-e4]: ASME, Ethical Standards, Ethical Obligations of Authors. [Evidence](../../../sources/notes/asmeethicalstandards.md#e4)
[^asmeethicalstandards-e5]: ASME, Ethical Standards, Ethical Obligations of Authors. [Evidence](../../../sources/notes/asmeethicalstandards.md#e5)
[^asmeethicalstandards-e6]: ASME, Ethical Standards, Ethical Obligations of Authors. [Evidence](../../../sources/notes/asmeethicalstandards.md#e6)
[^asme2024ethics-e1]: ASME Society Policy P-15.7 (2024), opening. [Evidence](../../../sources/notes/asme2024ethics.md#e1)
[^asme2024ethics-e2]: ASME Society Policy P-15.7 (2024), Fundamental Canons, item 1. [Evidence](../../../sources/notes/asme2024ethics.md#e2)
[^asme2024ethics-e4]: ASME Society Policy P-15.7 (2024), Fundamental Canons, item 4. [Evidence](../../../sources/notes/asme2024ethics.md#e4)
[^asme2024ethics-e5]: ASME Society Policy P-15.7 (2024), Fundamental Canons, item 5. [Evidence](../../../sources/notes/asme2024ethics.md#e5)
[^jcgm2008gum-e1]: JCGM 100:2008 (GUM), 0.1. [Evidence](../../../sources/notes/jcgm2008gum.md#e1)
[^jcgm2008gum-e2]: JCGM 100:2008 (GUM), 3.3.2. [Evidence](../../../sources/notes/jcgm2008gum.md#e2)
[^jcgm2008gum-e8]: JCGM 100:2008 (GUM), 7.1.4. [Evidence](../../../sources/notes/jcgm2008gum.md#e8)
[^jcgm2008gum-e9]: JCGM 100:2008 (GUM), 7.2.3. [Evidence](../../../sources/notes/jcgm2008gum.md#e9)
[^taylor1994nist-e2]: Taylor & Kuyatt 1994 (NIST TN 1297), D.1.1.1. [Evidence](../../../sources/notes/taylor1994nist.md#e2)
[^taylor1994nist-e3]: Taylor & Kuyatt 1994 (NIST TN 1297), D.1.2. [Evidence](../../../sources/notes/taylor1994nist.md#e3)
[^aiaaeditorialpolicy-e1]: AIAA, Editorial Policy Statement on Numerical and Experimental Accuracy, opening. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e1)
[^aiaaeditorialpolicy-e2]: AIAA, Editorial Policy Statement, opening. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e2)
[^aiaaeditorialpolicy-e3]: AIAA, Editorial Policy Statement, Estimation of Bias Uncertainty. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e3)
[^aiaaeditorialpolicy-e4]: AIAA, Editorial Policy Statement, Estimation of Precision Uncertainty. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e4)
[^aiaaeditorialpolicy-e5]: AIAA, Editorial Policy Statement, Statement of Total Uncertainty. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e5)
[^aiaaeditorialpolicy-e6]: AIAA, Editorial Policy Statement, Statement of Experimental Design. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e6)
[^aiaaeditorialpolicy-e7]: AIAA, Editorial Policy Statement, Statement of Code Verification Activities. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e7)
[^aiaaeditorialpolicy-e8]: AIAA, Editorial Policy Statement, Coverage Factor. [Evidence](../../../sources/notes/aiaaeditorialpolicy.md#e8)
[^jfenumaccuracy-e1]: Journal of Fluids Engineering editorial policy on numerical accuracy, simplified statement. [Evidence](../../../sources/notes/jfenumaccuracy.md#e1)
[^jfenumaccuracy-e2]: Journal of Fluids Engineering editorial policy on numerical accuracy, item 4. [Evidence](../../../sources/notes/jfenumaccuracy.md#e2)
[^jfenumaccuracy-e3]: Journal of Fluids Engineering editorial policy on numerical accuracy, item 10. [Evidence](../../../sources/notes/jfenumaccuracy.md#e3)
[^jfenumaccuracy-e4]: Journal of Fluids Engineering editorial policy on numerical accuracy, item 1. [Evidence](../../../sources/notes/jfenumaccuracy.md#e4)
[^jfenumaccuracy-e5]: Journal of Fluids Engineering editorial policy on numerical accuracy, note after the ten items. [Evidence](../../../sources/notes/jfenumaccuracy.md#e5)
[^jfenumaccuracy-e6]: Journal of Fluids Engineering editorial policy on numerical accuracy, item 5. [Evidence](../../../sources/notes/jfenumaccuracy.md#e6)
[^celik2008procedure-e1]: Celik et al. 2008, Preliminaries. [Evidence](../../../sources/notes/celik2008procedure.md#e1)
[^celik2008procedure-e2]: Celik et al. 2008, Step 2. [Evidence](../../../sources/notes/celik2008procedure.md#e2)
[^celik2008procedure-e3]: Celik et al. 2008, Preliminaries. [Evidence](../../../sources/notes/celik2008procedure.md#e3)
[^celik2008procedure-e4]: Celik et al. 2008, Preliminaries. [Evidence](../../../sources/notes/celik2008procedure.md#e4)
[^celik2008procedure-e5]: Celik et al. 2008, example after Step 5. [Evidence](../../../sources/notes/celik2008procedure.md#e5)
[^celik2008procedure-e6]: Celik et al. 2008, Discretization Error Bars. [Evidence](../../../sources/notes/celik2008procedure.md#e6)
[^oshamachineguarding-e1]: OSHA, Machine Guarding Overview. [Evidence](../../../sources/notes/oshamachineguarding.md#e1)
[^oshamachineguarding-e2]: OSHA, Machine Guarding Overview. [Evidence](../../../sources/notes/oshamachineguarding.md#e2)
[^oshalockout-e1]: OSHA, Control of Hazardous Energy (Lockout/Tagout), What is hazardous energy? [Evidence](../../../sources/notes/oshalockout.md#e1)
[^oshalockout-e2]: OSHA, Control of Hazardous Energy (Lockout/Tagout), What can be done to control hazardous energy? [Evidence](../../../sources/notes/oshalockout.md#e2)
[^cmu2025machineshop-e1]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 4.j. [Evidence](../../../sources/notes/cmu2025machineshop.md#e1)
[^cmu2025machineshop-e2]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 5.a. [Evidence](../../../sources/notes/cmu2025machineshop.md#e2)
[^cmu2025machineshop-e3]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 7.a. [Evidence](../../../sources/notes/cmu2025machineshop.md#e3)
[^cmu2025machineshop-e4]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 7.b.iii. [Evidence](../../../sources/notes/cmu2025machineshop.md#e4)
[^cmu2025machineshop-e5]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 7.c. [Evidence](../../../sources/notes/cmu2025machineshop.md#e5)
[^cmu2025machineshop-e6]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 7.o. [Evidence](../../../sources/notes/cmu2025machineshop.md#e6)
[^cmu2025machineshop-e7]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 7.t. [Evidence](../../../sources/notes/cmu2025machineshop.md#e7)
[^cmu2025machineshop-e8]: Carnegie Mellon University EHS, Machine Shop Safety Guideline (2025), 7.m. [Evidence](../../../sources/notes/cmu2025machineshop.md#e8)
[^lisee2008conference-e1]: Lisée, Larivière & Archambault 2008, Methods. [Evidence](../../../sources/notes/lisee2008conference.md#e1)
[^lisee2008conference-e2]: Lisée, Larivière & Archambault 2008, Results (Figure 6 and its caption). [Evidence](../../../sources/notes/lisee2008conference.md#e2)
[^lisee2008conference-e3]: Lisée, Larivière & Archambault 2008, Results. [Evidence](../../../sources/notes/lisee2008conference.md#e3)
[^bjork2013publishing-e1]: Björk & Solomon 2013, Abstract. [Evidence](../../../sources/notes/bjork2013publishing.md#e1)
[^bjork2013publishing-e2]: Björk & Solomon 2013, §2 Methods. [Evidence](../../../sources/notes/bjork2013publishing.md#e2)
[^bjork2013publishing-e3]: Björk & Solomon 2013, §3 Results. [Evidence](../../../sources/notes/bjork2013publishing.md#e3)
[^bjork2013publishing-e4]: Björk & Solomon 2013, Appendix, table "Publication Time in Months by Discipline". [Evidence](../../../sources/notes/bjork2013publishing.md#e4)
[^bjork2013publishing-e5]: Björk & Solomon 2013, §4 Discussion. [Evidence](../../../sources/notes/bjork2013publishing.md#e5)
