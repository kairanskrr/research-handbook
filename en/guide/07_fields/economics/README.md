# Economics and business: field overview

This page explains how research in economics actually works: the division of labor between theory and empirical work; empirical methods built around "causal identification"; a publishing system in which working papers come first and journal review is slow; and conventions such as seminars, the job market paper, and alphabetical authorship. The page is mainly about economics; finance, management, marketing, and the other fields taught in business schools each have their own conventions, which are not covered here `[Our analysis]`. What applies in every field (choosing a topic, writing, peer review, research ethics) is in the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and in [Throughout the project](../../08_throughout/README.md), and is not repeated here. For the research strategies the field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

**After reading this page, you should be able to:**

- explain in plain words what an "identification strategy" is, and what assumption each of the common causal identification methods rests on;
- understand where working papers, the "top five" journals, seminars, and the job market paper fit in economics;
- know what the journals of the American Economic Association (AEA) require on data, code, trial registration, and disclosure of interests;
- know which research strategies empirical economics mainly uses and what standards they are judged by;
- avoid the mistakes newcomers commonly make, such as specification searching and looking only at statistical significance.

---

## How research works in this field

### Theory and empirics: a model, and a dataset

Research in economics falls roughly into two kinds: building theoretical models and doing empirical work with data `[Our analysis]`. One paper can do both (see the end of this section).

Varian says that **theoretical models** in economics "all look pretty much the same". The skeleton: there are some agents, each making choices to pursue their objectives; the choices are subject to constraints; and something adjusts to make the agents' choices consistent with one another[^varian1997build-e4]. Varian recommends working out the simplest example first, then writing down the simplest model, and simplifying further if you can[^varian1997build-e5]; only after that, generalize to see how general the result is[^varian1997build-e6].

**Empirical research** comes in several flavors (the grouping below is our own summary `[Our analysis]`):

- **Applied microeconomics**: using data on individuals, households, and firms to study labor, education, health, development, public finance, and similar questions `[Our analysis]`. In Angrist and Pischke's 2010 assessment, the design-based approach (covered in the next section) is found mainly in the micro fields of development, education, environment, labor, health, and public finance, and is still rare in industrial organization and macroeconomics[^angrist2010credibility-e2].
- **Macroeconomics**: as Angrist and Pischke described it in 2010, many macroeconomists have turned to "computational experiments": build a theoretical model economy, "calibrate" its parameters so that the model resembles the real economy on key statistics, then change parameters such as tax rates or monetary rules and see what happens[^angrist2010credibility-e14]. Angrist and Pischke argue that this can clarify what a model implies, but does not directly provide evidence on causal effects[^angrist2010credibility-e14].
- **Structural versus reduced-form estimation**: structural estimation fits a complete economic model (preferences, technology, market behavior) to data, then uses the estimated parameters to simulate situations that never happened `[Our analysis]`. The merger analysis in industrial organization that Angrist and Pischke describe is an example: estimate demand, then assume how firms compete with each other, and finally simulate how the industry performs with and without the merger[^angrist2010credibility-e21]. The contrasting "reduced-form" or "design-based" approach does not write down a full model, and estimates a particular causal effect directly from the research design `[Our analysis]`. The debate between the two camps is covered below.

In Cochrane's view, the main results of most papers are empirical; the theory or model in a paper is there to help readers understand the empirical results[^cochrane2005writing-e11].

### The credibility revolution: first answer "What's your identification strategy?"

**Identification** is about why you believe a relationship you see in the data is causal, rather than coincidence, reverse causation, or the result of some omitted factor. Your **identification strategy** is the reason you give `[Our analysis]`.

Angrist and Pischke call this change in empirical economics the "credibility revolution" and attribute it to a design-based approach: a focus on identifying causal effects, using real or natural experiments, and working hard to argue why the results can be given a causal interpretation[^angrist2010credibility-e1]. "What's your identification strategy?" is now a routine question at empirical seminars[^angrist2010credibility-e10]. Cochrane puts it more bluntly: the three most important things in empirical work are identification, identification, identification[^cochrane2005writing-e4].

The most direct approach is a randomized experiment. But experiments are slow and expensive, and sometimes impossible (for example, to study the effect of immigration on the host economy); in that case you can use variation created by institutions or natural events, known as a "natural experiment" or "quasi-experiment"[^angrist2010credibility-e3]. Quasi-experimental studies most often use three methods: instrumental variables, regression discontinuity, and difference-in-differences[^angrist2010credibility-e4]. In plain terms:

| Method | How it works | Key assumption | What to check most carefully |
|---|---|---|---|
| Randomized experiment | Decide at random who receives the treatment (such as a cash transfer or a subsidy), and compare the two groups `[Our analysis]` | Assignment is random, so the two groups are similar on average before treatment `[Our analysis]` | Whether randomization was actually carried out as planned; whether the groups were similar before treatment `[Our analysis]` |
| Instrumental variables | Find a variable that affects the "cause", and use only the variation it creates to estimate the effect `[Our analysis]` | It affects the outcome only through the channel you care about, and its value is as good as randomly assigned; both points must be argued explicitly[^angrist2010credibility-e5] | Whether it could affect the outcome through some other channel[^angrist2010credibility-e9] |
| Difference-in-differences | Compare how outcomes changed before and after a policy in a group more affected by it and a group less affected[^angrist2010credibility-e8] | Without the policy, the two groups' outcomes would have followed the same trend `[Our analysis]` | Whether the two groups have different trends of their own; if they do, the comparison breaks down[^angrist2010credibility-e9] |
| Regression discontinuity | When groups are assigned by a cutoff score, compare people just above and just below the cutoff[^angrist2010credibility-e6] | People on either side of the cutoff are similar in every way except whether they were treated[^angrist2010credibility-e7] | Whether people bunch near the cutoff; bunching may mean the cutoff itself changed people's behavior[^angrist2010credibility-e9] |

A good design has another benefit: the method is easy to explain and the results can be shown directly[^angrist2010credibility-e11]. Randomized experiments are not a cure-all either: Angrist and Pischke acknowledge that a well-done observational study can be more credible than a badly executed randomized trial[^angrist2010credibility-e18].

Cochrane's questions for empirical beginners make a ready-made checklist. What economic mechanism causes the variation in your right-hand-side variable? Genuine natural experiments are rare[^cochrane2005writing-e5]. Which control variables belong in the regression, and which do not? He thinks most papers include too many right-hand-side variables[^cochrane2005writing-e6]. How big is the result in economic terms? With a large enough sample, even a tiny effect is "statistically significant"[^cochrane2005writing-e7].

> **Where sources disagree: design-based or structural?**
>
> Note: all three points below come from the same article by Angrist and Pischke. They belong to the design-based camp themselves, and the critics' views are as they report them. For what the structural authors say in their own words, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) below.
>
> - **Design-based camp** (Angrist and Pischke): a good structural model can tell us about both mechanisms and causal effects, but its estimates should line up with those from methods that make weaker assumptions[^angrist2010credibility-e15]. They find results from good research designs more convincing than conclusions derived from good theory[^angrist2010credibility-e19].
> - **Critics** (as reported by Angrist and Pischke, including Heckman, Rosenzweig and Wolpin, and Deaton): in pursuit of internal validity, design-based research has become narrow and idiosyncratic[^angrist2010credibility-e20]. Specifically: a finding from one experiment may not hold in another setting (the problem of external validity); and researchers work on small questions while the big ones go unanswered[^angrist2010credibility-e16].
> - **The design-based reply**: if a single study has limits, go and gather more evidence, so that a more general picture gradually emerges[^angrist2010credibility-e17].
>
> Practical advice for newcomers: whichever path you take, you must be able to answer "what assumptions does this number depend on?" A structural model must say where its assumptions come from; a design-based study must say how far its conclusions generalize `[Our analysis]`.

### Working papers first; journal publication is slow

In economics, a paper can be made public as a **working paper** before it is submitted to a journal. Take the working papers of the National Bureau of Economic Research (NBER): they are new research by its members, released before peer review for discussion and comment[^nberworkingpapers-e1]. Other institutions, such as IZA (the Institute of Labor Economics), have their own discussion paper series. IZA itself notes that its discussion papers are often preliminary and should be cited with their provisional character in mind[^brodeur2016star-e6]. Several of the studies cited on this page (Brodeur and colleagues, Heckman and Moktan, Ellison, Card and DellaVigna) were read in their working paper or discussion paper versions, so the figures in the published versions may differ slightly.

According to Heckman and Moktan (2018 discussion paper version), established scholars in top-ranked US economics departments increasingly do not publish in the top five or field journals, and instead post their papers in influential working paper series, where they are highly cited[^heckman2020tyranny-e4].

Journal review is slow. Ellison (2000 working paper version, with data up to 1999) found that thirty or forty years earlier, papers in top journals were typically accepted six to nine months after submission; by the time he wrote, journals more often demanded extensive revisions, and review and revision took about two years on average[^ellison2002slowdown-e1]. At *Econometrica* and the *Review of Economic Studies*, the review cycle grew from 6–12 months in the early 1970s to 24–30 months in the late 1990s[^ellison2002slowdown-e2]. Heckman and Moktan (2018 discussion paper version) also note that submissions to the top five and the length of papers have both grown, rejection rates have risen accordingly, and review has slowed down[^heckman2020tyranny-e3].

### The "top five" journals

The "top five" are the *American Economic Review*, *Econometrica*, the *Journal of Political Economy*, the *Quarterly Journal of Economics*, and the *Review of Economic Studies*[^card2013nine-e2]. Card and DellaVigna argue that publishing in these journals profoundly shapes the direction of research in economics, the careers of young economists, and the pay of academic economists[^card2013nine-e1]. By their count (2013 working paper version), the overall acceptance rate of the top five fell from about 15% in 1980 to about 6% around 2012[^card2013nine-e3]. Heckman and Moktan analyzed the CVs of tenure-track faculty in the top 35 US economics departments and found that top-five publications have a large effect on whether someone gets tenure[^heckman2020tyranny-e1]; but they also argue that this filter is far from reliable, that a substantial share of influential papers are published outside the top five, and that selecting people this way encourages careerism over creativity[^heckman2020tyranny-e2].

### Seminar presentations

In economics, presenting at seminars is the main way a paper gets polished `[Our analysis]`. Varian holds that the more you present your work, the better the final paper will be, because presenting forces you to get to the point[^varian1997build-e7]. The audience will interrupt with questions on the spot[^varian1997build-e10][^cochrane2005writing-e12]; Cochrane timed the finance seminars of one winter quarter, and not a single paper reached its main result within an hour[^cochrane2005writing-e12]. He advises skipping the literature review and the warm-up and getting straight to the point[^cochrane2005writing-e8]. After a talk, write down right away where the audience got confused, what they asked, and what literature they recommended[^varian1997build-e8]. When the audience stops asking questions, the paper is nearly ready to submit[^varian1997build-e9].

### The job market paper

The following is based on Cawley's guide for the 2018–19 job market season and covers only the US academic job market; the exact schedule changes from year to year. When PhD students apply for US academic jobs, they must submit a cover letter, a CV, and a **job market paper**[^cawley2018guide-e7]. The most important factor in how the job search goes is the quality of that paper and how well you present it[^cawley2018guide-e1]. The job talk you give during the search is a 90-minute seminar based on this paper[^cawley2018guide-e2]. Authors of empirical papers will be questioned closely on their identification strategy and methods in interviews[^cawley2018guide-e5]; interviewers also want to be sure that the ideas and key decisions in the paper are genuinely yours[^cawley2018guide-e6]. So your job market paper should ideally be independent work that you led yourself `[Our analysis]`.

### Alphabetical authorship

The convention in economics is to list the authors of a coauthored paper in alphabetical order of surname, not in order of contribution[^einav2006surname-e1]. From 1980 to 2002, about half the papers in the top five journals were coauthored, and 88% of those listed authors alphabetically[^einav2006surname-e4]. Psychology, by contrast, orders authors by contribution[^einav2006surname-e3]. This means that in economics, author order generally does not tell you who contributed most, and contributions have to be stated separately `[Our analysis]`. Einav and Yariv also found that in the top ten economics departments, faculty whose surnames start earlier in the alphabet are more likely to get tenure[^einav2006surname-e2]; there is no such relationship in psychology[^einav2006surname-e3].

---

## How this field differs from others

| | Economics | For comparison |
|---|---|---|
| Main publication venue | Journals; publishing in top journals has a large effect on careers[^card2013nine-e1] | Most areas of computer science are conference-driven; see the [Computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue) |
| How work is first made public | Working papers, released before peer review[^nberworkingpapers-e1] | Computer science often uses arXiv preprints; see the [Computer science page](../computer-science/README.md#double-blind-review-and-preprints) |
| Review time | At top journals, review plus revision took about two years on average (figures from around 2000)[^ellison2002slowdown-e1] | Computer science conferences have fixed schedules and a single decision; see the [Computer science page](../computer-science/README.md#conferences-or-journals-a-long-running-debate) |
| Author order | Conventionally alphabetical by surname[^einav2006surname-e1] | Psychology orders authors by contribution[^einav2006surname-e3] |
| Replication materials | AEA journals require data and code to be submitted before acceptance, and the Data Editor checks them[^aea2026data-e1][^aea2026data-e3] | Artifact evaluation in computer science is usually voluntary; see the [Computer science page](../computer-science/README.md#artifact-evaluation-and-badges) |
| The key question asked of an empirical paper | The identification strategy[^angrist2010credibility-e10] | Computer science mostly asks "how and by how much does it beat existing methods?"; see the [Computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue) |

---

## Norms and reporting standards in this field

The following uses the policies of the AEA's journals as the example. Other journals may require different things; **follow the latest policy of your target journal**.

### Data and code must reproduce the results

- **Submit a replication package before acceptance.** Papers with empirical work, simulations, or experiments must, before acceptance, provide data, code, and computational details sufficient to reproduce the results, deposited in a trusted, publicly accessible repository[^aea2026data-e1]. The AEA Data Editor runs a reproducibility check[^aea2026data-e3].
- **Data that cannot be made public come with requirements too.** You must preserve the data and code for at least five years, help others reproduce the results, make the code public, and publicly document where the data come from[^aea2026data-e2]. If others would still need your personal approval to get the data, "available on request" is generally not acceptable[^aea2026data-e4].
- **Submit the data-cleaning programs as well.** Even if the raw data cannot be provided, all programs that turn the raw data into the analysis data must be[^aea2026data-e5].
- **Write a good README, ideally with a master script.** Put a README in PDF format at the top level of the replication package, describing every step needed to reproduce all results[^aea2026data-e7]; a master script that runs the whole analysis in one go is strongly recommended[^aea2026data-e6].
- **Experiments and surveys must include the original materials.** Include the complete experimental instructions or the original survey questionnaire at submission[^aea2026data-e10].

It is best to follow these requirements from the first day of the project, rather than catching up at submission `[Our analysis]`. For general practice in organizing data and code, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

### Field experiments must be registered; pre-analysis plans

- **Field experiments must be registered.** AEA journals require every field experiment to be registered in the AEA's registry for randomized controlled trials (RCTs) before submission; lab experiments are currently not required to register[^aea2026rct-e1][^aea2026data-e9].
- **The earlier the better.** You can register at any stage of a trial, but early registration is encouraged[^aea2026rct-e1]; trials registered before the intervention starts are marked as "pre-registered"[^aea2026rct-e5].
- **What to register.** Required fields include the outcome variables, the experimental design, and the planned sample size, among others[^aea2026rct-e4]. Registration is free and can be edited later, with the edit history preserved[^aea2026rct-e2]. While a survey is in the field, some fields can be hidden for now so they do not influence respondents[^aea2026rct-e3].
- **Registry review is not a quality or ethics review.** The registry's review does not judge the quality or ethics of the research[^aea2026rct-e6].

A **pre-analysis plan** sets out precisely, before you look at the data, which analyses you will run: which variables, how you will clean the data, and which regressions[^olken2015promises-e1]. It is more detailed than the registration above `[Our analysis]`. The next few sentences rest only on the abstract published on the article page of Olken 2015; we did not read the full text. If you specify the regressions in advance and report all the prespecified results, the problem of "data mining" (trying analysis after analysis and picking only the good-looking results) is greatly reduced[^olken2015promises-e2]; but such plans have limitations and costs too, and Olken argues that in many settings their benefits may be smaller than first thought[^olken2015promises-e3]; his discussion is mainly about randomized controlled trials[^olken2015promises-e4]. For the difference between exploratory and confirmatory analysis, see the Part 2 chapter [From research questions to an evidence plan](../../02_from-project-to-study/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring).

### Disclosure of interests

- Every submission must state its sources of funding, and say so explicitly if there are none[^aea2026disclosure-e1].
- Each author must disclose support totaling at least $10,000 received in the past three years from interested parties, including in-kind support such as access to data[^aea2026disclosure-e2].
- If any other party has the right to review the paper before it is released, that must be disclosed[^aea2026disclosure-e3]. This is especially relevant for research using company or government data `[Our analysis]`.
- Each author submits a separate disclosure statement[^aea2026disclosure-e4]; papers that collect data from human subjects must state whether they obtained approval from an institutional review board (IRB), and if not, why not[^aea2026disclosure-e5]. Failing to disclose at submission can lead to an acceptance being withdrawn[^aea2026disclosure-e6].

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The mainstream of empirical economics is causal explanation: the first two rows of the table below are two routes to causal evidence; the third row is theoretical modeling; the last two rows are structural estimation and calibration, which rely on an economic model for quantitative inference. The grouping of the table and the "What it looks like in economics" column are our own summary; each entry in the "Common evidence and standards" column represents only the source cited in its footnote (mostly the 2026 versions of AEA journal policies and articles by a few economists), not a rule for the whole discipline `[Our analysis]`.

| Strategy | What it looks like in economics | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) (randomized experiments) | Decide at random who receives an intervention, such as a cash transfer or a subsidy `[Our analysis]`; slow, expensive, and sometimes impossible[^angrist2010credibility-e3] | AEA journals: register field experiments before submission[^aea2026rct-e1], and only registration before the intervention starts counts as "pre-registered"[^aea2026rct-e5]; submit the experimental instructions with the paper[^aea2026data-e10] | [Field experiments](../../06_methods/field_experiment.md) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) (quasi-experiments) | Use variation created by institutions or natural events; the most common methods are instrumental variables, regression discontinuity, and difference-in-differences[^angrist2010credibility-e4] | State your identification strategy first[^angrist2010credibility-e10], and check for holes method by method, as described in [The credibility revolution](#the-credibility-revolution-first-answer-whats-your-identification-strategy) above; AEA journals require a replication package before acceptance[^aea2026data-e1] | [Quasi-experiments and causal identification](../../06_methods/quasi_experiment.md) |
| [Proof](../../05_research-strategies/prove.md) (theoretical modeling) | Write down agents, objectives, constraints, and equilibrium[^varian1997build-e4], and derive conclusions from the model `[Our analysis]` | Varian recommends starting with the simplest model that is still interesting[^varian1997build-e5], then generalizing to see how general the result is[^varian1997build-e6]. Thomson of the University of Rochester, in his 1999 guide to writing theory papers for PhD students in the *Journal of Economic Literature*, advises making clear that the result is interesting and has not been obtained before[^thomson1999young-e1], and checking each assumption in a theorem to see whether it can be dropped[^thomson1999young-e2]. The referee guidelines of *Theoretical Economics*, the Econometric Society's theory journal (web version consulted in October 2026; the page is undated): length is itself one of the criteria[^te2026guidelines-e1]; referees should say which results should be cut, and whether proofs could be shorter if the results were less general[^te2026guidelines-e2]; and they should ask only for essential extensions[^te2026guidelines-e3]. Our sources do not cover how large a contribution must be to be publishable | [Theoretical research](../computer-science/practices/theoretical_research.md) on the Computer science page is a useful reference |
| [Causal explanation](../../05_research-strategies/explain_causality.md) (structural estimation) | Estimate the parameters of an economic model, then use it to analyze policies that have never been implemented (see below the table); merger analysis is one example[^angrist2010credibility-e21] | Low and Meghir 2017: spell out which assumptions the inference relies on; this is where the value of a structural model lies[^low2017use-e3]. After estimation, report standard errors and explain which features of the data pin down each parameter[^low2017use-e4], then test the model against other features of the data or against reduced-form results, ideally ones not used in estimation[^low2017use-e5]. AEA journals: put the estimation and simulation programs in the replication package[^aea2026data-e11] | No corresponding page yet |
| [Causal explanation](../../05_research-strategies/explain_causality.md) (calibration and computational experiments) | Build a model economy, tune its parameters so that it resembles the real economy on a few key statistics, then change policy parameters and see what happens[^angrist2010credibility-e14] | Report how uncertain the parameters are and how sensitive the results are to the model specification (see below the table); put the simulation programs in the replication package[^aea2026data-e11] | [Quantitative simulation](../../06_methods/simulation_study.md) (with computer science as the example) |

Notes on the "structural estimation" and "calibration" rows. The five articles cited here and in "The two camps disagree" below (Nevo and Whinston; Low and Meghir; Keane; Kydland and Prescott; Hansen and Heckman) were all published in the *Journal of Economic Perspectives*. We read Low and Meghir in full (the journal version held in University College London's institutional repository); for the other four we read only the abstracts on the AEA website, so we report only what the authors say there:

- **Structural estimation**: in Nevo and Whinston's words, structural modeling uses data to identify the parameters of an economic model grounded in individual choice[^nevo2010taking-e1]. Low and Meghir argue that structural models can uncover the mechanisms that determine outcomes, and can be used to analyze policies that have never been implemented[^low2017use-e2].
- **Calibration and computational experiments**: according to Angrist and Pischke's 2010 description, many macroeconomists use this approach[^angrist2010credibility-e14]. Kydland and Prescott argue that experimenting on real people at the level of a whole nation is not feasible, but you can build a model economy and compute how the people in it would behave[^kydland1996computational-e1], in order to answer a clearly posed quantitative question[^kydland1996computational-e2]. Hansen and Heckman question whether the micro estimates that calibration needs actually exist off the shelf[^hansen1996empirical-e1], and argue for routinely reporting how uncertain the parameters are and how sensitive the results are to the model specification[^hansen1996empirical-e2].

**The two camps disagree in ways that affect how you design your study**, so here are both sides side by side:

- **Design-based camp**: Angrist and Pischke find results from good research designs more convincing than conclusions derived from good theory[^angrist2010credibility-e19]; structural estimates should line up with results from methods that make weaker assumptions[^angrist2010credibility-e15]; calibration can show what a model implies, but does not directly provide evidence on causal effects[^angrist2010credibility-e14].
- **Structural camp**: Low and Meghir argue that the main advantage of structural models is that they go beyond the usual studies that deliver only reduced-form causal relationships[^low2017use-e1]. Nevo and Whinston argue that credible analysis can be structural or nonstructural, and that for some questions structural analysis has important advantages[^nevo2010taking-e2]. Keane argues that statistical work cannot escape assumptions and its conclusions are always conditional[^keane2010structural-e1]; being able to run controlled experiments does not remove the need for theory[^keane2010structural-e3].

How to use this table `[Our analysis]`:

- **The question common to the first two rows is identification**: what assumptions does this number depend on? How big the effect is in economic terms must also be stated on its own; reporting significance alone is not enough[^cochrane2005writing-e7].
- **Placing structural estimation and calibration under causal explanation is our own classification.** Their central claim is often "how big an effect a given policy will have", but such conclusions rest mainly on model assumptions, not on research design as in the first two rows.
- **If you use a model, hand it in as part of the evidence.** State what the model assumes, where the parameters come from, and how sensitive the conclusions are to the assumptions, and submit the code for solving and simulating the model[^aea2026data-e11].

## Research methods common in this field

Here is how the cross-field research methods map onto economics; the mapping and the notes on differences are our own summary `[Our analysis]`:

- For **field experiments**, see [Field experiments](../../06_methods/field_experiment.md); for the general workflow of **lab experiments**, see [Controlled experiments](../../06_methods/controlled_experiment.md).
- For **causal inference from observational data**, see [Quasi-experiments and causal identification](../../06_methods/quasi_experiment.md), and for data processing, [Data science](../../06_methods/data_science.md). The key question in economics here is the identification strategy[^angrist2010credibility-e10].
- **Theoretical modeling** and **structural estimation** do not yet have methods pages of their own; for the standards they are judged by, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) above. For theoretical modeling, [Theoretical research](../computer-science/practices/theoretical_research.md) on the Computer science page is a useful reference. For **calibration and computational experiments**, see [Quantitative simulation](../../06_methods/simulation_study.md), whose examples come mainly from computer science.
- For **surveys**, see [Questionnaire surveys](../../06_methods/questionnaire_survey.md); AEA journals require the original questionnaire to be submitted with the paper[^aea2026data-e10]. For **replication studies**, see [Replication studies](../../06_methods/replication.md). For **meta-research** (for example, tallying the distribution of p-values in top journals[^brodeur2016star-e2]), see [Methodology research and meta-science](../../06_methods/meta_science.md).

---

## Advice for newcomers

1. **Write down your identification strategy before you start.** Answer in a sentence or two: what economic mechanism causes the variation in my explanatory variable[^cochrane2005writing-e5]? Why should that variation be unrelated to the other factors that affect the outcome? If you cannot answer, hold off on running regressions `[Our analysis]`.
2. **Check for holes method by method.** For difference-in-differences, check whether the two groups have different trends of their own; for regression discontinuity, whether people bunch near the cutoff; for instrumental variables, whether there is some other channel[^angrist2010credibility-e9].
3. **Post a working paper first, and be ready for things to be slow.** Figures from around 2000 show review and revision at top journals taking about two years on average[^ellison2002slowdown-e1]. Build that into your timeline `[Our analysis]`.
4. **Present often, and take notes right after.** Presenting forces you to get to the point[^varian1997build-e7]; after every talk, write down the audience's questions and suggestions right away[^varian1997build-e8].
5. **Treat the job market paper as the most important thing you do in your PhD.** Aim to finish it by the end of the summer before you go on the market[^cawley2018guide-e3], and set up practice sessions with your cohort to rehearse the talk again and again[^cawley2018guide-e4].
6. **From day one, organize your work to replication-package standards.** Write both cleaning and analysis as programs, so that in the end everything reruns with one command[^aea2026data-e5][^aea2026data-e6]; keep raw data read-only, as described in [Organizing research materials](../../08_throughout/organizing_materials.md#2-raw-data-is-read-only-everything-else-can-be-regenerated) in Throughout the project. The goal is that a fellow student could reproduce every number from the paper and its appendix alone[^cochrane2005writing-e3].
7. **For a field experiment, register before the intervention starts.** Only registration before the intervention starts counts as "pre-registered"[^aea2026rct-e5]; think carefully about whether to also write a more detailed pre-analysis plan[^olken2015promises-e3].
8. **When you coauthor, make contributions explicit.** With alphabetical authorship, nobody can tell who did what[^einav2006surname-e1]; for handling the division of work and credit, see [Collaborators and advisors](../../08_throughout/collaboration_and_advisors.md#6-authorship-discuss-it-at-the-start-and-adjust-as-you-go) in Throughout the project `[Our analysis]`.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Trying every regression specification and reporting only the significant one (known as "specification searching" or p-hacking. A p-value is the probability of getting a result at least this extreme by chance alone if there were really no effect; 0.05 is often treated as the threshold for "significant" `[Our analysis]`) | Brodeur and colleagues tallied about 50,000 tests published in 2005–2011 in three journals, the *American Economic Review*, the *Journal of Political Economy*, and the *Quarterly Journal of Economics* (2013 discussion paper version), and found too many p-values just below 0.05; their explanation is that when a result is just short of significant, researchers may go looking for a "significant" specification[^brodeur2016star-e2][^brodeur2016star-e3]. Casting a wide net with large numbers of regressions provides little support for a causal interpretation[^angrist2010credibility-e13] |
| Reporting only statistical significance, not how big the effect is | With a large enough sample, even a tiny effect is significant[^cochrane2005writing-e7] |
| Putting every variable you can think of into the regression as a control | Cochrane thinks most papers include too many right-hand-side variables[^cochrane2005writing-e6]; some variables are themselves part of the outcome, and controlling for them controls away the very effect you want to estimate `[Our analysis]` |
| Simply asserting that an instrument is "unrelated to other influences" without arguing why that holds | The assumptions behind an instrumental variable must be argued thoroughly[^angrist2010credibility-e5] |
| Spending the first twenty minutes of a talk on setup and literature | At a seminar, get straight to the point[^cochrane2005writing-e8]; interruptions from the audience will eat up the time[^cochrane2005writing-e12] |
| Treating "data available on request" as making data public | If requests need the author's personal approval, this is generally not acceptable[^aea2026data-e4] |
| Remembering to register a field experiment only after it is done | AEA journals require registration before submission and encourage registering early[^aea2026rct-e1]; registering after the intervention starts does not count as pre-registration[^aea2026rct-e5] |
| Failing to disclose funding, or a data provider's right to review the paper | Failure to disclose at submission can lead to an acceptance being withdrawn[^aea2026disclosure-e6] |
| Focusing only on the top five and judging research by where it is published | Heckman and Moktan found that a substantial share of influential papers are published outside the top five[^heckman2020tyranny-e2] |

---

## Further reading

- **Angrist & Pischke 2010, The Credibility Revolution in Empirical Economics**: explains where design-based empirical methods came from, what each method checks, and the criticisms and replies. Read it when you want to understand why "identification" matters so much.
- **Cochrane 2005, Writing Tips for Ph.D. Students**: short; covers paper structure, a list of questions to ask yourself about empirical identification, and seminar presentations. Read it before you write your first paper.
- **Varian 1997, How to Build an Economic Model in Your Spare Time**: how a theorist works, from finding ideas and simplifying models to giving talks. Read it if you do theory or want to learn modeling.
- **AEA Data and Code Availability Policy**: the specific requirements for replication packages and what a README should contain. Read it before you start organizing your data and code.
- **The AEA RCT Registry's overview and registration guidelines**: read them when you plan a field experiment.
- **Cawley, A Guide and Advice for Economists on the U.S. Junior Academic Job Market**: the process of and advice for the US academic job market in economics. This page uses the 2018–19 edition; a year before you go on the market, find the latest edition.
- **Card & DellaVigna 2013, Heckman & Moktan 2020**: data and debate on the top five journals (we read the working paper or discussion paper versions). Read them if you want to understand where the pressure to publish comes from.

[^varian1997build-e4]: Varian 1997, §1.4 Building your model. [Evidence](../../../sources/notes/varian1997build.md#e4)
[^varian1997build-e5]: Varian 1997, §1.4 Building your model. [Evidence](../../../sources/notes/varian1997build.md#e5)
[^varian1997build-e6]: Varian 1997, §1.6 Making mistakes. [Evidence](../../../sources/notes/varian1997build.md#e6)
[^varian1997build-e7]: Varian 1997, §1.8 Giving a seminar. [Evidence](../../../sources/notes/varian1997build.md#e7)
[^varian1997build-e8]: Varian 1997, §1.8 Giving a seminar. [Evidence](../../../sources/notes/varian1997build.md#e8)
[^varian1997build-e9]: Varian 1997, §1.11 When to stop. [Evidence](../../../sources/notes/varian1997build.md#e9)
[^varian1997build-e10]: Varian 1997, §1.8 Giving a seminar. [Evidence](../../../sources/notes/varian1997build.md#e10)
[^thomson1999young-e1]: Thomson 1999, §2 General Principles, p. 159. [Evidence](../../../sources/notes/thomson1999young.md#e1)
[^thomson1999young-e2]: Thomson 1999, §5 Writing Proofs, p. 177. [Evidence](../../../sources/notes/thomson1999young.md#e2)
[^te2026guidelines-e1]: Theoretical Economics guidelines for referees (accessed October 2026), The opinion. [Evidence](../../../sources/notes/te2026guidelines.md#e1)
[^te2026guidelines-e2]: Theoretical Economics guidelines for referees (accessed October 2026), Substantive comments. [Evidence](../../../sources/notes/te2026guidelines.md#e2)
[^te2026guidelines-e3]: Theoretical Economics guidelines for referees (accessed October 2026), Substantive comments. [Evidence](../../../sources/notes/te2026guidelines.md#e3)
[^angrist2010credibility-e1]: Angrist & Pischke 2010, Abstract. [Evidence](../../../sources/notes/angrist2010credibility.md#e1)
[^angrist2010credibility-e2]: Angrist & Pischke 2010, Abstract. [Evidence](../../../sources/notes/angrist2010credibility.md#e2)
[^angrist2010credibility-e3]: Angrist & Pischke 2010, Introduction. [Evidence](../../../sources/notes/angrist2010credibility.md#e3)
[^angrist2010credibility-e4]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e4)
[^angrist2010credibility-e5]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e5)
[^angrist2010credibility-e6]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e6)
[^angrist2010credibility-e7]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e7)
[^angrist2010credibility-e8]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e8)
[^angrist2010credibility-e9]: Angrist & Pischke 2010, Whither Sensitivity Analysis? [Evidence](../../../sources/notes/angrist2010credibility.md#e9)
[^angrist2010credibility-e10]: Angrist & Pischke 2010, More Transparent Discussion of Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e10)
[^angrist2010credibility-e11]: Angrist & Pischke 2010, More Transparent Discussion of Research Design. [Evidence](../../../sources/notes/angrist2010credibility.md#e11)
[^angrist2010credibility-e13]: Angrist & Pischke 2010, Whither Sensitivity Analysis? [Evidence](../../../sources/notes/angrist2010credibility.md#e13)
[^angrist2010credibility-e14]: Angrist & Pischke 2010, Mad About Macro. [Evidence](../../../sources/notes/angrist2010credibility.md#e14)
[^angrist2010credibility-e15]: Angrist & Pischke 2010, Industrial Disorganization. [Evidence](../../../sources/notes/angrist2010credibility.md#e15)
[^angrist2010credibility-e16]: Angrist & Pischke 2010, Has the Research Design Pendulum Swung Too Far? [Evidence](../../../sources/notes/angrist2010credibility.md#e16)
[^angrist2010credibility-e17]: Angrist & Pischke 2010, External Validity. [Evidence](../../../sources/notes/angrist2010credibility.md#e17)
[^angrist2010credibility-e19]: Angrist & Pischke 2010, Industrial Disorganization. [Evidence](../../../sources/notes/angrist2010credibility.md#e19)
[^angrist2010credibility-e20]: Angrist & Pischke 2010, External Validity. [Evidence](../../../sources/notes/angrist2010credibility.md#e20)
[^angrist2010credibility-e21]: Angrist & Pischke 2010, Industrial Disorganization. [Evidence](../../../sources/notes/angrist2010credibility.md#e21)
[^angrist2010credibility-e18]: Angrist & Pischke 2010, Other Empirical Work in the Age of Heavy Metal. [Evidence](../../../sources/notes/angrist2010credibility.md#e18)
[^cochrane2005writing-e3]: Cochrane 2005, §2 Writing. [Evidence](../../../sources/notes/cochrane2005writing.md#e3)
[^cochrane2005writing-e4]: Cochrane 2005, §3 Tips for empirical work. [Evidence](../../../sources/notes/cochrane2005writing.md#e4)
[^cochrane2005writing-e5]: Cochrane 2005, §3 Tips for empirical work. [Evidence](../../../sources/notes/cochrane2005writing.md#e5)
[^cochrane2005writing-e6]: Cochrane 2005, §3 Tips for empirical work. [Evidence](../../../sources/notes/cochrane2005writing.md#e6)
[^cochrane2005writing-e7]: Cochrane 2005, §3 Tips for empirical work. [Evidence](../../../sources/notes/cochrane2005writing.md#e7)
[^cochrane2005writing-e8]: Cochrane 2005, §4 Seminar presentations. [Evidence](../../../sources/notes/cochrane2005writing.md#e8)
[^cochrane2005writing-e11]: Cochrane 2005, §1 Organization / Theory. [Evidence](../../../sources/notes/cochrane2005writing.md#e11)
[^cochrane2005writing-e12]: Cochrane 2005, §4 Seminar presentations. [Evidence](../../../sources/notes/cochrane2005writing.md#e12)
[^nberworkingpapers-e1]: NBER Working Papers page. [Evidence](../../../sources/notes/nberworkingpapers.md#e1)
[^brodeur2016star-e2]: Brodeur et al. 2016, Abstract (IZA discussion paper version). [Evidence](../../../sources/notes/brodeur2016star.md#e2)
[^brodeur2016star-e3]: Brodeur et al. 2016, Abstract (IZA discussion paper version). [Evidence](../../../sources/notes/brodeur2016star.md#e3)
[^brodeur2016star-e6]: IZA discussion paper inside-cover note (see the discussion paper version of Brodeur et al. 2016). [Evidence](../../../sources/notes/brodeur2016star.md#e6)
[^heckman2020tyranny-e1]: Heckman & Moktan 2020, Abstract (IZA discussion paper version). [Evidence](../../../sources/notes/heckman2020tyranny.md#e1)
[^heckman2020tyranny-e2]: Heckman & Moktan 2020, Abstract (IZA discussion paper version). [Evidence](../../../sources/notes/heckman2020tyranny.md#e2)
[^heckman2020tyranny-e3]: Heckman & Moktan 2020, §1 Introduction (IZA discussion paper version). [Evidence](../../../sources/notes/heckman2020tyranny.md#e3)
[^heckman2020tyranny-e4]: Heckman & Moktan 2020, §1 Introduction (IZA discussion paper version). [Evidence](../../../sources/notes/heckman2020tyranny.md#e4)
[^ellison2002slowdown-e1]: Ellison 2002, §1 Introduction (NBER working paper version). [Evidence](../../../sources/notes/ellison2002slowdown.md#e1)
[^ellison2002slowdown-e2]: Ellison 2002, §2 (NBER working paper version). [Evidence](../../../sources/notes/ellison2002slowdown.md#e2)
[^card2013nine-e1]: Card & DellaVigna 2013, §1 Introduction (NBER working paper version). [Evidence](../../../sources/notes/card2013nine.md#e1)
[^card2013nine-e2]: Card & DellaVigna 2013, §1 Introduction (NBER working paper version). [Evidence](../../../sources/notes/card2013nine.md#e2)
[^card2013nine-e3]: Card & DellaVigna 2013, §1 Introduction (NBER working paper version). [Evidence](../../../sources/notes/card2013nine.md#e3)
[^cawley2018guide-e1]: Cawley 2018, Introduction. [Evidence](../../../sources/notes/cawley2018guide.md#e1)
[^cawley2018guide-e2]: Cawley 2018, Introduction. [Evidence](../../../sources/notes/cawley2018guide.md#e2)
[^cawley2018guide-e3]: Cawley 2018, Preparing to Go on the Job Market. [Evidence](../../../sources/notes/cawley2018guide.md#e3)
[^cawley2018guide-e4]: Cawley 2018, Preparing to Go on the Job Market. [Evidence](../../../sources/notes/cawley2018guide.md#e4)
[^cawley2018guide-e5]: Cawley 2018, Interviewing at the ASSA Meetings. [Evidence](../../../sources/notes/cawley2018guide.md#e5)
[^cawley2018guide-e6]: Cawley 2018, Interviewing at the ASSA Meetings. [Evidence](../../../sources/notes/cawley2018guide.md#e6)
[^cawley2018guide-e7]: Cawley 2018, Applying for Academic Jobs. [Evidence](../../../sources/notes/cawley2018guide.md#e7)
[^einav2006surname-e1]: Einav & Yariv 2006, p. 175. [Evidence](../../../sources/notes/einav2006surname.md#e1)
[^einav2006surname-e2]: Einav & Yariv 2006, p. 175. [Evidence](../../../sources/notes/einav2006surname.md#e2)
[^einav2006surname-e3]: Einav & Yariv 2006, p. 182, footnote 8; p. 175. [Evidence](../../../sources/notes/einav2006surname.md#e3)
[^einav2006surname-e4]: Einav & Yariv 2006, p. 184. [Evidence](../../../sources/notes/einav2006surname.md#e4)
[^aea2026data-e1]: AEA Data and Code Availability Policy (February 2026 version), opening. [Evidence](../../../sources/notes/aea2026data.md#e1)
[^aea2026data-e2]: AEA Data and Code Availability Policy, opening. [Evidence](../../../sources/notes/aea2026data.md#e2)
[^aea2026data-e3]: AEA Data and Code Availability Policy, opening. [Evidence](../../../sources/notes/aea2026data.md#e3)
[^aea2026data-e4]: AEA Data and Code Availability Policy, Non-Public Data. [Evidence](../../../sources/notes/aea2026data.md#e4)
[^aea2026data-e5]: AEA Data and Code Availability Policy, Data and Code Availability Standard (DCAS), item 7. [Evidence](../../../sources/notes/aea2026data.md#e5)
[^aea2026data-e6]: AEA Data and Code Availability Policy, Computer Code. [Evidence](../../../sources/notes/aea2026data.md#e6)
[^aea2026data-e7]: AEA Data and Code Availability Policy, Data and Code Availability Standard (DCAS), item 13. [Evidence](../../../sources/notes/aea2026data.md#e7)
[^aea2026data-e9]: AEA Data and Code Availability Policy, Data and Code Availability Standard (DCAS), item 12. [Evidence](../../../sources/notes/aea2026data.md#e9)
[^aea2026data-e10]: AEA Policy for Papers Conducting Experiments and Collecting Primary Data, Original Instructions. [Evidence](../../../sources/notes/aea2026data.md#e10)
[^aea2026rct-e1]: About the AEA RCT Registry. [Evidence](../../../sources/notes/aea2026rct.md#e1)
[^aea2026rct-e2]: About the AEA RCT Registry. [Evidence](../../../sources/notes/aea2026rct.md#e2)
[^aea2026rct-e3]: About the AEA RCT Registry. [Evidence](../../../sources/notes/aea2026rct.md#e3)
[^aea2026rct-e4]: AEA RCT Registry registration guidelines, Required Information. [Evidence](../../../sources/notes/aea2026rct.md#e4)
[^aea2026rct-e5]: AEA RCT Registry registration guidelines. [Evidence](../../../sources/notes/aea2026rct.md#e5)
[^aea2026rct-e6]: AEA RCT Registry registration guidelines, Registration Review Criteria. [Evidence](../../../sources/notes/aea2026rct.md#e6)
[^olken2015promises-e1]: Olken 2015, Abstract. [Evidence](../../../sources/notes/olken2015promises.md#e1)
[^olken2015promises-e2]: Olken 2015, Abstract. [Evidence](../../../sources/notes/olken2015promises.md#e2)
[^olken2015promises-e3]: Olken 2015, Abstract. [Evidence](../../../sources/notes/olken2015promises.md#e3)
[^olken2015promises-e4]: Olken 2015, Abstract. [Evidence](../../../sources/notes/olken2015promises.md#e4)
[^aea2026disclosure-e1]: AEA Disclosure Policy, Disclosure Principles. [Evidence](../../../sources/notes/aea2026disclosure.md#e1)
[^aea2026disclosure-e2]: AEA Disclosure Policy, Disclosure Principles. [Evidence](../../../sources/notes/aea2026disclosure.md#e2)
[^aea2026disclosure-e3]: AEA Disclosure Policy, Disclosure Principles. [Evidence](../../../sources/notes/aea2026disclosure.md#e3)
[^aea2026disclosure-e4]: AEA Disclosure Policy, Instructions. [Evidence](../../../sources/notes/aea2026disclosure.md#e4)
[^aea2026disclosure-e5]: AEA Disclosure Policy, IRB Approval. [Evidence](../../../sources/notes/aea2026disclosure.md#e5)
[^aea2026disclosure-e6]: AEA Disclosure Policy, Instructions. [Evidence](../../../sources/notes/aea2026disclosure.md#e6)
[^aea2026data-e11]: AEA Data and Code Availability Policy, Code for Analysis (Data and Code Availability Standard, item 8). [Evidence](../../../sources/notes/aea2026data.md#e11)
[^nevo2010taking-e1]: Nevo & Whinston 2010, Abstract (only the abstract was read). [Evidence](../../../sources/notes/nevo2010taking.md#e1)
[^nevo2010taking-e2]: Nevo & Whinston 2010, Abstract (only the abstract was read). [Evidence](../../../sources/notes/nevo2010taking.md#e2)
[^low2017use-e1]: Low & Meghir 2017, Abstract. [Evidence](../../../sources/notes/low2017use.md#e1)
[^low2017use-e2]: Low & Meghir 2017, Abstract. [Evidence](../../../sources/notes/low2017use.md#e2)
[^low2017use-e3]: Low & Meghir 2017, Introduction, p. 33. [Evidence](../../../sources/notes/low2017use.md#e3)
[^low2017use-e4]: Low & Meghir 2017, Standard Errors and Post-Estimation Checks, p. 53. [Evidence](../../../sources/notes/low2017use.md#e4)
[^low2017use-e5]: Low & Meghir 2017, Standard Errors and Post-Estimation Checks, p. 53. [Evidence](../../../sources/notes/low2017use.md#e5)
[^keane2010structural-e1]: Keane 2010, Abstract (we read only the abstract). [Evidence](../../../sources/notes/keane2010structural.md#e1)
[^keane2010structural-e3]: Keane 2010, Abstract (we read only the abstract). [Evidence](../../../sources/notes/keane2010structural.md#e3)
[^kydland1996computational-e1]: Kydland & Prescott 1996, Abstract (we read only the abstract). [Evidence](../../../sources/notes/kydland1996computational.md#e1)
[^kydland1996computational-e2]: Kydland & Prescott 1996, Abstract (we read only the abstract). [Evidence](../../../sources/notes/kydland1996computational.md#e2)
[^hansen1996empirical-e1]: Hansen & Heckman 1996, Abstract (only the abstract was read). [Evidence](../../../sources/notes/hansen1996empirical.md#e1)
[^hansen1996empirical-e2]: Hansen & Heckman 1996, Abstract (only the abstract was read). [Evidence](../../../sources/notes/hansen1996empirical.md#e2)
