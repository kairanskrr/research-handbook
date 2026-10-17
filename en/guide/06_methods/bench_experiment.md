# Bench experiments (wet lab)

This page covers a kind of research common in cell and molecular biology: at the bench, you treat cultured cells or extracted molecules with reagents, compare them with controls, and test a hypothesis. The focus is on what you actually do at each step, from designing an experiment to writing it up in a paper.

The experimental unit, the two kinds of replicates, controls, randomization, blinding, reagent validation, lab notebook practice, the 3Rs for animal research (replacement, reduction, refinement), and the ARRIVE reporting guidelines (Animal Research: Reporting of In Vivo Experiments) are covered in the [Biological sciences field overview](../07_fields/biological-sciences/README.md). Reporting requirements for preclinical research (cell and animal studies done before testing in humans), the rules of the *British Journal of Pharmacology*, and antibody validation are covered in the [Basic medicine field overview](../07_fields/basic-medicine/README.md). For statistics in general, see the Part 2 section [Report how big the difference is and how certain you are, not just the p-value](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value). This page only covers the practical work at the bench.

**Scope** `[Our analysis]`: this page was first written for the biological sciences field pages, and its examples are cell and molecular experiments from cell and molecular biology. Its basis is mainly methodology articles in biomedical journals and reporting guidelines for animal research (the ARRIVE 2.0 explanation and elaboration document, and Landis et al. 2012). Besides [Biological sciences](../07_fields/biological-sciences/README.md), the field overviews for [Basic medical sciences](../07_fields/basic-medicine/README.md) and [Biotechnology](../07_fields/biotechnology/README.md) also list it as a common method. Other fields (chemistry, materials science, and psychology, for example) also run controlled experiments in the lab, but their conventions for controls, replication, and reporting are not the same; check your field's conventions and your target journal's instructions for authors before you rely on this page.

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md) (change one factor and see whether the outcome changes) `[Our analysis]`. The basis is the method's basic approach: change one factor at a time and keep everything else the same[^vaux2012replicates-e6].

**After reading this page, you should be able to:**

- write down your hypothesis before you start, and say whether the experiment is exploratory or confirmatory;
- draw the hierarchy of your experiment, find the experimental unit, and get n right;
- arrange controls, randomization, and blinding at the bench, and fix n, exclusion criteria, and the analysis in advance;
- handle outliers and failed experiments honestly, draw figures that do not mislead, and stay on the right side of the line in image processing;
- write your methods so someone else can repeat them.

---

## 1. What this kind of research is and when to use it

Bench experiments answer questions of the form "if I change this factor, does the outcome change?" `[Our analysis]`. For example: if you knock down a gene, do the cells proliferate more slowly? The basic approach is to change one factor at a time and keep everything else the same[^vaux2012replicates-e6].

The logic is the same as a [Controlled experiments](controlled_experiment.md) under research methods: manipulate one variable, assign randomly, control other conditions. The difference is that human participants are naturally independent individuals; at the bench, you have to design the "independent individuals" (the experimental units) yourself, and this is where people most often go wrong `[Our analysis]`. Compared with animal experiments, cell experiments need no animal welfare approval, but the risks of pseudoreplication, faulty reagents, batch effects, and improper image processing are the same `[Our analysis]`.

**First, tell exploratory experiments from confirmatory ones.** Exploratory experiments measure many outcomes, look for patterns in the data, and generate hypotheses; pilot studies fall into this category[^perciedusert2020reporting-e12]. Confirmatory experiments test a specific hypothesis: the sample size is estimated in advance, the primary outcome is set in advance, and the analysis uses inferential statistics[^perciedusert2020reporting-e13]. Results from exploratory experiments can only be treated as hypotheses, to be confirmed by later confirmatory experiments; see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#tell-exploratory-experiments-from-confirmatory-ones)[^landis2012call-e12][^landis2012call-e17]. Beginners often write up something they noticed while exploring as if it were a conclusion `[Our analysis]`.

---

## 2. How to do it

**Where the guidance comes from.** Our sources include no reporting standard written specifically for cell experiments. Much of what follows is borrowed from animal research: the ARRIVE 2.0 explanation and elaboration document (ARRIVE is the reporting guideline for animal research), and the reporting recommendations Landis et al. proposed for animal research in 2012. Applying their experimental design principles to cell experiments is our own borrowing, not something those documents say; this page does not use their animal welfare material `[Our analysis]`.

### Step 1: State the hypothesis and fix the primary outcome

**How:** write the hypothesis you are testing in one sentence: which groups you compare, which outcome you measure, and how large a difference would be biologically meaningful `[Our analysis]`. A confirmatory experiment needs a primary outcome measure set in advance[^perciedusert2020reporting-e13].

**Why:** if you have no primary outcome set in advance, or switch it after collecting data, it is easy to report only the significant results. Registering your protocol in advance protects you against suspicion of selective outcome reporting (also known as data dredging or p-hacking)[^perciedusert2020reporting-e25].

**Where people go wrong:** statistically significant does not mean biologically important[^cumming2007error-e7]. If you see only a partial effect, do not say a gene is "essential" (see the [Biological sciences field overview](../07_fields/biological-sciences/README.md#controls-randomization-and-blinding)).

### Step 2: Draw the hierarchy and find the experimental unit

**How:** draw your experiment as a tree: cell line → experiment day → plate → well → cell → measurements on each cell `[Our analysis]`. Then distinguish three kinds of "unit"[^lazic2018what-e3]:

- **Experimental unit**: the entity that is randomly and independently assigned to a treatment group. **n is the number of experimental units.**
- **Observational unit**: the entity you actually measure, such as individual cells under the microscope. More observational units do not increase n.
- **Biological unit**: the entity you want to draw conclusions about. If the hypothesis is "breast cancer cell lines proliferate faster than lung cancer cell lines", you need several breast cancer and several lung cancer cell lines, because the hypothesis is about tissue of origin[^lazic2018what-e7].

To count as a genuine replicate, an entity must meet three conditions at once: it is assigned to a group independently; the treatment is applied to it independently; and it does not influence the other experimental units[^lazic2018what-e4]. A phrase worth remembering: "sample size is where you randomise"[^lazic2018what-e10].

**How to count in cell experiments**: cells in the same well influence each other, so they cannot be experimental units; the well or dish is[^lazic2018what-e5]. In vitro experiments usually also need the whole experiment repeated on different days, and wells within one day count only as subsamples[^lazic2018what-e6]. For example, if you set up three replicate cultures each time and repeat the experiment independently four times, n = 4, not 3 and not 12[^cumming2007error-e3]. Replicate cultures split from the same cell stock sample only that one stock[^cumming2007error-e8].

**Why:** if replication is done at the wrong level, no statistical method, however clever, can fix it after the experiment is done[^lazic2018what-e1]. The mistake is not rare: Lazic et al. surveyed a set of animal research papers published between January 2011 and September 2016 and found that only 22% had genuine replication, while 46% had pseudoreplication[^lazic2018what-e9]. These are figures for animal research; our sources do not give the rate for cell experiments `[Our analysis]`.

> **Where sources disagree: should you use the terms "biological replicate" and "technical replicate"?** The Biological sciences field overview uses this pair of terms ([see here](../07_fields/biological-sciences/README.md#identify-the-experimental-unit-before-you-count-n)). Lazic et al. argue that the terms are defined inconsistently and do not make clear what should be replicated, and recommend thinking in terms of the three units above instead[^lazic2018what-e2]. They also acknowledge that which level to treat as n is a scientific judgment on which people may disagree, but the stricter the standard, the more credible the result[^lazic2018what-e6]. Our suggestion `[Our analysis]`: your lab can keep saying "biological replicate", but when you design the experiment, check it against the three conditions above one by one; when in doubt, choose the stricter level, and say in the paper exactly what n refers to.

### Step 3: Design the controls

**How:** what negative and positive controls are for is covered in the [Biological sciences field overview](../07_fields/biological-sciences/README.md#controls-randomization-and-blinding). At the bench this means, for example: a knockdown experiment gets a non-targeting (scrambled) sequence control; a drug experiment gets a vehicle control, plus a treatment known to work as a positive control `[Our analysis]`.

**Where people go wrong:** running the control and treatment groups on different days or with different reagent batches. If you process samples in batches without planning how, you can mistake a batch effect for a treatment effect[^landis2012call-e7].

### Step 4: Fix n, exclusion criteria, and the analysis before you start

**How:** write the following in your lab notebook, dated before your first data point `[Our analysis]`:

- **What n is and how you chose it.** Every experiment must explain how the sample size was determined[^perciedusert2020reporting-e14]. A sample size calculation uses the effect size, the variability, the significance level, and the statistical power; if the design is complex or unusual, consult a statistician first[^perciedusert2020reporting-e15].
- **When you will stop.** The sample size and the rule for stopping data collection must be set in advance[^landis2012call-e9].
- **Exclusion criteria.** Set them before the experiment begins[^perciedusert2020reporting-e17], at least write them in your notebook, and state in the paper that they were set in advance[^perciedusert2020reporting-e18]. A typical reason for exclusion is failing quality control, such as insufficient sample or contamination above a threshold[^perciedusert2020reporting-e17].
- **Statistical methods.** Decide them before you collect data[^perciedusert2020reporting-e26].

**Why:** with low statistical power, real effects are more likely to be missed, and even when they are detected the effect size is often overestimated[^perciedusert2020reporting-e14]. "Stop when it's significant, add a few more runs when it isn't" is exactly what a prespecified stopping rule is meant to prevent[^landis2012call-e9], and it raises the chance of false positives `[Our analysis]`.

**Where people go wrong:** some journals have hard rules about n and significance thresholds. The *British Journal of Pharmacology*'s 2018 guidelines, for example, require n of at least 5 per group for data subjected to statistical analysis[^curtis2018experimental-e14], and require the significance threshold to be stated in the methods and not changed in the results[^curtis2018experimental-e5]. These are one journal's rules; other journals follow their own instructions for authors. For the journal's other rules, see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#one-pharmacology-journals-specific-rules-the-british-journal-of-pharmacology) `[Our analysis]`.

### Step 5: Randomize and blind at the bench

**How:**
- **Random allocation**: use random numbers to decide which well or plate gets which treatment; do not fix "controls on the left, treatments on the right" `[Our analysis]`.
- **Use blocks to control batches**: split the experiment into several small sub-experiments (called "blocks"), for example one per experiment day, and randomize treatments within each block[^perciedusert2020reporting-e21]. Factors that might affect the result, such as reagent batch or operator, are also treated as blocking factors in the analysis[^perciedusert2020reporting-e31].
- **Randomize the order of operations**: randomize the order of sampling and measurement too, or use blocking or counterbalancing[^perciedusert2020reporting-e22].
- **Blinding**: blind at least the assessment of outcomes, especially assessments that involve subjective judgment, such as scoring sections; this may mean asking someone else to help[^perciedusert2020reporting-e23]. The person doing the allocation should also not know which group the next subject will go to; this is called allocation concealment. The source uses animals as the example; applying it to cell experiments is our own borrowing[^landis2012call-e6] `[Our analysis]`.

**Why:** systematic review data cited in the ARRIVE explanation document show that missing bias-reducing measures such as randomization and blinding can inflate effect sizes by as much as 30% to 45%[^perciedusert2020reporting-e24].

### Step 6: Run a pilot first

**How:** before the real experiment, get the method working with a small number of samples: antibody concentration, cell density, treatment time, the linear range of the assay, and so on `[Our analysis]`. The purpose of a pilot study is to inform the design and feasibility of later experiments[^perciedusert2020reporting-e12]. Pilots run only to refine procedures usually have very small samples and are not suited to power calculations[^perciedusert2020reporting-e16].

**Where people go wrong:** merging pilot data into the main experiment `[Our analysis]`. The *British Journal of Pharmacology* rule is that pilot data can go in the paper, but in a separate "pilot study" subsection of the methods, without P values[^curtis2018experimental-e11]. Another mistake is estimating the main experiment's sample size from the pilot alone: a pilot on its own is unlikely to give enough data on variability for a power calculation[^perciedusert2020reporting-e16].

### Step 7: Authenticate your reagents and cell lines

Why validation matters is covered in the [Biological sciences field overview](../07_fields/biological-sciences/README.md#validate-reagents-antibodies-and-cell-lines). At the bench:

- **Cell lines**: authenticate a newly arrived cell line before you use it `[Our analysis]`. Short tandem repeat (STR) profiling is the accepted standard for authentication[^freedman2015economics-e3]. It is not expensive: Freedman et al. estimate that for a four-year National Institutes of Health (NIH) grant averaging $450,000, buying cell lines from a reliable source and authenticating them once a year costs about $1,000, or 0.2% of the budget[^freedman2015economics-e10].
- **Antibodies**: do at least one validation in your own application and samples[^uhlen2016proposal-e6]; for approaches to validation, see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#validate-antibodies-for-each-application-and-report-reagents-so-they-can-be-found).
- **Write it down**: record the source, catalog number, and lot number of every reagent in your notebook `[Our analysis]`; in the paper, give at least the catalog and lot numbers for antibodies[^uhlen2016proposal-e6].

### Step 8: Record as you go

General lab notebook practice is covered in the [Biological sciences field overview](../07_fields/biological-sciences/README.md#the-lab-notebook-is-the-primary-record): record in chronological order, give every entry a date and a subject[^schnell2015ten-e10], and write it up immediately after the work[^schnell2015ten-e3]. At the bench, pay extra attention to the following:

- **Record failed experiments too.** Errors are part of the research process; do not erase or destroy records[^schnell2015ten-e11]. Write down why it failed (contamination, instrument fault, expired reagent); this is what you will later rely on to decide whether that run's data can be excluded `[Our analysis]`.
- **Keep raw images unaltered, and record the instrument settings**, such as exposure time and gain[^rossner2004what-e8].

### Step 9: Handle outliers and failed experiments honestly

**How:**
- **Exclude by the criteria you set in advance, not by whether the result looks good.** Obvious data entry errors and readings outside a plausible range can be removed, but state the reason, so readers can tell responsible data cleaning from data manipulation[^perciedusert2020reporting-e19]. If you used the outlier test built into your statistics software, say so explicitly[^perciedusert2020reporting-e20].
- **Keep the levels apart**: an outlier among repeated measurements of the same sample can be dropped if there is a convincing explanation, though repeating the measurement is safer; results from independent samples should be dropped only in exceptional circumstances[^vaux2012replicates-e8].
- **Report all replicates**: however many times you repeated the whole experiment, report that many results; do not pick only a "representative experiment"[^perciedusert2020reporting-e27]. Stating how many times the experiment was done in total counters the tendency to publish only the best run[^landis2012call-e15].

**Where people go wrong:** looking for reasons a run "failed" only after seeing that it does not support the hypothesis `[Our analysis]`. That is why the reason for a failure must be written down before you look at the results.

### Step 10: Analyze and plot

**How:**
- **Summarize each experimental unit into one value first** (for example, the mean of the wells from one day), then do the statistics. This is the simplest way to avoid pseudoreplication[^lazic2018what-e8].
- **State n and what the error bars are in the figure legend.** Give n, the number of independently performed experiments[^cumming2007error-e2], and say whether the error bars are standard deviations, standard errors, or confidence intervals[^cumming2007error-e1]. When you show a single "representative experiment", n = 1, and you should not show error bars or give P values[^cumming2007error-e4].
- **Plot every point when n is small.** With small samples like n = 3, plot the individual data points rather than error bars[^cumming2007error-e5]. Many different data distributions produce identical bar graphs[^weissgerber2015beyond-e1], and paired data drawn as bar graphs hide whether the changes within each pair go in the same direction[^weissgerber2015beyond-e2]. Such figures are common: Weissgerber et al. reviewed 703 original research articles published from January to March 2014 in physiology journals ranked in the top 25%; 85.6% had at least one bar graph, and only 13.4% had used a univariate scatterplot[^weissgerber2015beyond-e4].
- **Do not use standard errors to "magnify" differences.** Showing standard errors instead of standard deviations visually exaggerates differences between groups[^weissgerber2015beyond-e5].

**Where people go wrong:** concluding "no effect" because P is greater than 0.05 is a common and serious mistake[^cumming2007error-e6]. The effect may be real and n simply too small `[Our analysis]`.

### Step 11: Process images without crossing the line

Blots, gels, and micrographs are common evidence in wet-lab work, and easy places to cross the line `[Our analysis]`. The rules below come from a 2004 editorial in the *Journal of Cell Biology*, representing that journal's rules and its editors' advice at the time; for the journal you submit to, follow its instructions for authors `[Our analysis]`.

- **Not allowed**: enhancing, obscuring, moving, removing, or adding any specific feature within an image[^rossner2004what-e2]. Removing a background band you think is irrelevant still misrepresents the data[^rossner2004what-e4]. Do not use tools such as the clone stamp to clean up the background[^rossner2004what-e5]. Do not splice together pieces of different gels to compare protein or nucleic acid levels; rerun all samples on the same gel[^rossner2004what-e6].
- **Allowed, but only to the whole image**: adjusting brightness, contrast, or color balance is acceptable if it applies to the whole image and does not erase information in the original; nonlinear adjustments (such as changing gamma) must be disclosed in the figure legend[^rossner2004what-e3]. Do not adjust treatment and control images differently[^rossner2004what-e7].
- **Allowed, but mark it**: if you remove whole lanes and splice the rest together, leave a thin line at the splice[^rossner2004what-e6]; if you combine images from different fields of view or different exposures, separate them with dividing lines and say so in the legend[^rossner2004what-e2].
- **Solve it during the experiment, not on the computer**: take several exposures rather than heavily adjusting contrast afterward[^rossner2004what-e9]. Do not collect data selectively by tweaking instrument settings, and do not present highly unusual results as "representative"[^rossner2004what-e10].

When in doubt, ask yourself: does the adjusted image still accurately represent the original data[^rossner2004what-e11]? Inappropriate manipulation can be judged research misconduct[^rossner2004what-e1].

### Step 12: Write the methods so others can repeat them

**How:** describe what was done to each group (including controls), how, and with what, in enough detail for someone else to repeat it; state which quality control measures you used; and cite Research Resource Identifiers (RRIDs, unique identifiers for reagents and tools) where they exist[^perciedusert2020reporting-e28]. At minimum, explain how n was determined, whether there was randomization, whether there was blinding, and how the data were handled; these are the minimum reporting requirements the Landis et al. workshop set out for animal research[^landis2012call-e1], borrowed here as a reference for cell experiments `[Our analysis]`.

**Why:** of the 193 experiments the Reproducibility Project: Cancer Biology planned to replicate, not one could have a replication protocol designed without asking the original authors[^errington2021challenges-e7]. On one occasion, a request for experimental details got only the reply "a standard procedure was used"[^errington2021challenges-e8].

---

## 3. Checklist

Our sources contain no reporting checklist specific to cell experiments. The list below borrows from the ARRIVE explanation document and combines it with Cumming et al.'s rules for error bars and the *Journal of Cell Biology*'s rules for images; the grouping into tiers is our own `[Our analysis]`.

**Must do**

- [ ] The experimental unit is stated, and n counts experimental units, not wells, cells, or measurements[^lazic2018what-e3][^cumming2007error-e3]
- [ ] You explain how the sample size was determined[^perciedusert2020reporting-e14]
- [ ] Exclusion criteria were set in advance, written in the notebook, and reported in the paper[^perciedusert2020reporting-e18]
- [ ] Results of all replicates are reported, not just a representative experiment[^perciedusert2020reporting-e27]
- [ ] Figure legends state n and the type of error bar[^cumming2007error-e1][^cumming2007error-e2]
- [ ] Images received only whole-image adjustments, splices are marked, and raw images are kept unaltered[^rossner2004what-e2][^rossner2004what-e8]
- [ ] Methods are detailed enough for others to repeat; antibodies have catalog and lot numbers[^perciedusert2020reporting-e28][^uhlen2016proposal-e6]

**Better practice**

- [ ] Blocking and randomization were used for treatment positions and the order of operations[^perciedusert2020reporting-e21][^perciedusert2020reporting-e22]
- [ ] Outcome assessment was blinded[^perciedusert2020reporting-e23]
- [ ] Individual data points are plotted when n is small[^cumming2007error-e5][^weissgerber2015beyond-e3]
- [ ] The protocol was registered in advance[^perciedusert2020reporting-e25]

**Fine to skip; not a flaw**

- Pilots run only to get a procedure working: no power calculation needed[^perciedusert2020reporting-e16], and a control group may not be needed[^perciedusert2020reporting-e29].
- Exploratory experiments: no need to fix a single primary outcome[^perciedusert2020reporting-e30], but conclusions can only be treated as hypotheses awaiting confirmation[^landis2012call-e12].

---

## 4. Common mistakes

Mistakes already listed in the Biological sciences field overview's [Common mistakes](../07_fields/biological-sciences/README.md#common-mistakes) (pseudoreplication, not authenticating cell lines, overly brief methods) are not repeated here.

| Mistake | Why it is a problem |
|---|---|
| Plating many wells from one cell stock on one day and counting n by wells | You have sampled only that one stock[^cumming2007error-e8]; wells within one day count only as subsamples[^lazic2018what-e6] |
| Showing one "representative experiment" with error bars and P values | Here n = 1[^cumming2007error-e4] |
| Adding more runs when the result is not significant and stopping once it is | The stopping rule must be set in advance[^landis2012call-e9]; otherwise the chance of false positives rises `[Our analysis]` |
| Deciding which runs "failed" and should be excluded after seeing the results | Exclusion criteria must be set before data collection[^perciedusert2020reporting-e17] |
| Running control and treatment groups on different days or with different reagent batches | A batch effect can be mistaken for a treatment effect[^landis2012call-e7] |
| Showing n = 3 data as a bar graph with standard errors | Different data distributions can produce the same bar graph, and standard errors also exaggerate differences[^weissgerber2015beyond-e1][^weissgerber2015beyond-e5] |
| Erasing "extra" bands from a blot, or adjusting the contrast of one image on its own | It misrepresents the data and can be judged research misconduct[^rossner2004what-e4][^rossner2004what-e7][^rossner2004what-e1] |

---

## 5. Further reading

- **Lazic et al. 2018, "What exactly is 'N' in cell culture and animal experiments?" (*PLOS Biology*)**: deciding n using the experimental unit, with cell culture examples. Read it before you design your first experiment.
- **Cumming, Fidler, and Vaux 2007, "Error bars in experimental biology" (*Journal of Cell Biology*)**: rules for error bars, with a clear account of n and representative experiments. Read it before you draw your first figure.
- **Rossner and Yamada 2004, "What's in a picture?" (*Journal of Cell Biology*)**: example images showing which kinds of image processing are acceptable and which are not. Read it before you process your first blot.
- **Weissgerber et al. 2015, "Beyond bar and line graphs" (*PLOS Biology*)**: why small samples should not be shown only as bar graphs.
- For Vaux et al. 2012 and the ARRIVE 2.0 explanation document, see the [Biological sciences field overview](../07_fields/biological-sciences/README.md#further-reading); for Landis et al. 2012 and Curtis et al. 2018, see the [Basic medicine field overview](../07_fields/basic-medicine/README.md#further-reading).

[^vaux2012replicates-e6]: Vaux et al. 2012, Sidebar A. [Evidence](../../sources/notes/vaux2012replicates.md#e6)
[^vaux2012replicates-e8]: Vaux et al. 2012, Sidebar A. [Evidence](../../sources/notes/vaux2012replicates.md#e8)
[^lazic2018what-e1]: Lazic et al. 2018, Introduction. [Evidence](../../sources/notes/lazic2018what.md#e1)
[^lazic2018what-e2]: Lazic et al. 2018, Introduction. [Evidence](../../sources/notes/lazic2018what.md#e2)
[^lazic2018what-e3]: Lazic et al. 2018, Box 2. [Evidence](../../sources/notes/lazic2018what.md#e3)
[^lazic2018what-e4]: Lazic et al. 2018, Requirements for genuine replication. [Evidence](../../sources/notes/lazic2018what.md#e4)
[^lazic2018what-e5]: Lazic et al. 2018, Cell culture experiments. [Evidence](../../sources/notes/lazic2018what.md#e5)
[^lazic2018what-e6]: Lazic et al. 2018, Cell culture experiments. [Evidence](../../sources/notes/lazic2018what.md#e6)
[^lazic2018what-e7]: Lazic et al. 2018, Requirements for genuine replication. [Evidence](../../sources/notes/lazic2018what.md#e7)
[^lazic2018what-e8]: Lazic et al. 2018, Analysis of hierarchical data. [Evidence](../../sources/notes/lazic2018what.md#e8)
[^lazic2018what-e9]: Lazic et al. 2018, What is the extent of the problem? and Box 1. [Evidence](../../sources/notes/lazic2018what.md#e9)
[^lazic2018what-e10]: Lazic et al. 2018, Requirements for genuine replication. [Evidence](../../sources/notes/lazic2018what.md#e10)
[^cumming2007error-e1]: Cumming et al. 2007, Rule 1. [Evidence](../../sources/notes/cumming2007error.md#e1)
[^cumming2007error-e2]: Cumming et al. 2007, Rule 2. [Evidence](../../sources/notes/cumming2007error.md#e2)
[^cumming2007error-e3]: Cumming et al. 2007, Replicates or independent samples—what is n? [Evidence](../../sources/notes/cumming2007error.md#e3)
[^cumming2007error-e4]: Cumming et al. 2007, Rule 3. [Evidence](../../sources/notes/cumming2007error.md#e4)
[^cumming2007error-e5]: Cumming et al. 2007, Rule 4. [Evidence](../../sources/notes/cumming2007error.md#e5)
[^cumming2007error-e6]: Cumming et al. 2007, Statistical significance tests and P values. [Evidence](../../sources/notes/cumming2007error.md#e6)
[^cumming2007error-e7]: Cumming et al. 2007, Statistical significance tests and P values. [Evidence](../../sources/notes/cumming2007error.md#e7)
[^cumming2007error-e8]: Cumming et al. 2007, Replicates or independent samples—what is n? [Evidence](../../sources/notes/cumming2007error.md#e8)
[^perciedusert2020reporting-e12]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 13. [Evidence](../../sources/notes/perciedusert2020reporting.md#e12)
[^perciedusert2020reporting-e13]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 13. [Evidence](../../sources/notes/perciedusert2020reporting.md#e13)
[^perciedusert2020reporting-e14]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 2b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e14)
[^perciedusert2020reporting-e15]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 2b and Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e15)
[^perciedusert2020reporting-e16]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 2b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e16)
[^perciedusert2020reporting-e17]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 3a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e17)
[^perciedusert2020reporting-e18]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 3a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e18)
[^perciedusert2020reporting-e19]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 3b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e19)
[^perciedusert2020reporting-e20]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 3b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e20)
[^perciedusert2020reporting-e21]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 4, Box 4. [Evidence](../../sources/notes/perciedusert2020reporting.md#e21)
[^perciedusert2020reporting-e22]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 4b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e22)
[^perciedusert2020reporting-e23]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e23)
[^perciedusert2020reporting-e24]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 5. [Evidence](../../sources/notes/perciedusert2020reporting.md#e24)
[^perciedusert2020reporting-e25]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 6b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e25)
[^perciedusert2020reporting-e26]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 7a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e26)
[^perciedusert2020reporting-e27]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 10a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e27)
[^perciedusert2020reporting-e28]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 9a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e28)
[^perciedusert2020reporting-e29]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 1a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e29)
[^perciedusert2020reporting-e30]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 6b. [Evidence](../../sources/notes/perciedusert2020reporting.md#e30)
[^perciedusert2020reporting-e31]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 7a. [Evidence](../../sources/notes/perciedusert2020reporting.md#e31)
[^landis2012call-e9]: Landis et al. 2012, Interim data analysis. [Evidence](../../sources/notes/landis2012call.md#e9)
[^landis2012call-e7]: Landis et al. 2012, Randomization and blinding. [Evidence](../../sources/notes/landis2012call.md#e7)
[^landis2012call-e12]: Landis et al. 2012, An important note about exploratory experiments. [Evidence](../../sources/notes/landis2012call.md#e12)
[^landis2012call-e17]: Landis et al. 2012, An important note about exploratory experiments. [Evidence](../../sources/notes/landis2012call.md#e17)
[^landis2012call-e15]: Landis et al. 2012, Small effect sizes. [Evidence](../../sources/notes/landis2012call.md#e15)
[^landis2012call-e6]: Landis et al. 2012, Box 1. [Evidence](../../sources/notes/landis2012call.md#e6)
[^landis2012call-e1]: Landis et al. 2012, Abstract. [Evidence](../../sources/notes/landis2012call.md#e1)
[^curtis2018experimental-e14]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../sources/notes/curtis2018experimental.md#e14)
[^curtis2018experimental-e5]: Curtis et al. 2018, Key points of the updated guidance. [Evidence](../../sources/notes/curtis2018experimental.md#e5)
[^curtis2018experimental-e11]: Curtis et al. 2018, Flexibility and pilot data. [Evidence](../../sources/notes/curtis2018experimental.md#e11)
[^uhlen2016proposal-e6]: Uhlen et al. 2016, Suggestions for providers and users. [Evidence](../../sources/notes/uhlen2016proposal.md#e6)
[^freedman2015economics-e3]: Freedman et al. 2015, main text, cell line example. [Evidence](../../sources/notes/freedman2015economics.md#e3)
[^freedman2015economics-e10]: Freedman et al. 2015, main text, cell line example. [Evidence](../../sources/notes/freedman2015economics.md#e10)
[^schnell2015ten-e10]: Schnell 2015, Rule 5. [Evidence](../../sources/notes/schnell2015ten.md#e10)
[^schnell2015ten-e11]: Schnell 2015, Rule 5. [Evidence](../../sources/notes/schnell2015ten.md#e11)
[^schnell2015ten-e3]: Schnell 2015, Rule 4. [Evidence](../../sources/notes/schnell2015ten.md#e3)
[^rossner2004what-e1]: Rossner & Yamada 2004, Introduction. [Evidence](../../sources/notes/rossner2004what.md#e1)
[^rossner2004what-e2]: Rossner & Yamada 2004, Journal guidelines. [Evidence](../../sources/notes/rossner2004what.md#e2)
[^rossner2004what-e3]: Rossner & Yamada 2004, Journal guidelines. [Evidence](../../sources/notes/rossner2004what.md#e3)
[^rossner2004what-e4]: Rossner & Yamada 2004, Gross misrepresentation. [Evidence](../../sources/notes/rossner2004what.md#e4)
[^rossner2004what-e5]: Rossner & Yamada 2004, Cleaning up background. [Evidence](../../sources/notes/rossner2004what.md#e5)
[^rossner2004what-e6]: Rossner & Yamada 2004, Splicing lanes together. [Evidence](../../sources/notes/rossner2004what.md#e6)
[^rossner2004what-e7]: Rossner & Yamada 2004, Linear vs. nonlinear adjustments. [Evidence](../../sources/notes/rossner2004what.md#e7)
[^rossner2004what-e8]: Rossner & Yamada 2004, Other data-management issues. [Evidence](../../sources/notes/rossner2004what.md#e8)
[^rossner2004what-e9]: Rossner & Yamada 2004, Brightness/contrast adjustments. [Evidence](../../sources/notes/rossner2004what.md#e9)
[^rossner2004what-e10]: Rossner & Yamada 2004, Other data-management issues. [Evidence](../../sources/notes/rossner2004what.md#e10)
[^rossner2004what-e11]: Rossner & Yamada 2004, Conclusion. [Evidence](../../sources/notes/rossner2004what.md#e11)
[^weissgerber2015beyond-e1]: Weissgerber et al. 2015, Introduction. [Evidence](../../sources/notes/weissgerber2015beyond.md#e1)
[^weissgerber2015beyond-e2]: Weissgerber et al. 2015, Introduction. [Evidence](../../sources/notes/weissgerber2015beyond.md#e2)
[^weissgerber2015beyond-e3]: Weissgerber et al. 2015, Recommendations for a New Data Presentation Paradigm. [Evidence](../../sources/notes/weissgerber2015beyond.md#e3)
[^weissgerber2015beyond-e4]: Weissgerber et al. 2015, Introduction and Are Your Figures Worth a Thousand Words? [Evidence](../../sources/notes/weissgerber2015beyond.md#e4)
[^weissgerber2015beyond-e5]: Weissgerber et al. 2015, Are Your Figures Worth a Thousand Words? [Evidence](../../sources/notes/weissgerber2015beyond.md#e5)
[^errington2021challenges-e7]: Errington et al. 2021 (eLife e67995), Abstract. [Evidence](../../sources/notes/errington2021challenges.md#e7)
[^errington2021challenges-e8]: Errington et al. 2021 (eLife e67995), Requesting assistance from original authors. [Evidence](../../sources/notes/errington2021challenges.md#e8)
