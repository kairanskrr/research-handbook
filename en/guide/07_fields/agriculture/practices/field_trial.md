# Field trials

This page walks through a field trial from start to finish: comparing varieties, fertilizers, tillage, and other treatments on plots at an experimental site, from setting objectives, choosing a design, and laying out plots, through season-long record-keeping, harvest and data checking, mixed-model analysis, multi-environment trials, and on-farm trials, to writing it up. Experimental units, pseudoreplication, blocking, split plots, power analysis, the MIAPPE metadata standard (Minimum Information About a Plant Phenotyping Experiment), and the basics of working with farmers are already covered in the [agriculture field overview](../README.md#designing-field-trials); this page builds on them. For the general logic of study design, see the Part 2 chapter [From research questions to an evidence plan](../../../02_do-the-project/01_question-to-evidence.md); for controlled experiments with human participants, see [Controlled experiments](../../../06_methods/controlled_experiment.md) in Research types.

**Scope**: this is how plot trials are run on experimental fields or in farmers' fields in agronomy, crop science, horticulture, and related areas. It is a field-specific practice of agriculture, forestry, and fisheries. For the shared logic of randomization and controls, see the strategy pages [Causal explanation](../../../05_research-strategies/explain_causality.md) and [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md). The "field experiments" of economics and political science, which randomize people or groups in the real world, are a different thing; see [Field experiments](../../../06_methods/field_experiment.md). **Strategies it usually serves**: Causal explanation when you estimate the effect of fertilizer, tillage, or similar treatments; Comparative evaluation when you compare varieties across sites. The strategy pages do not yet list this page.

**After reading this page, you should be able to:**
- state your objective, treatments, and controls, and use them to choose a design, plot size, and number of replicates;
- randomize correctly in the field and keep dated records of operations and unplanned events all season;
- check your data, run a basic mixed-model analysis, and tell fixed effects from random effects;
- describe your design and analysis the way your target journal requires, and avoid common mistakes.

---

## 1. What this kind of study is and when to use it

A field trial is a **comparative experiment**. Piepho and Edmondson's 2018 analysis tutorial says that the field trials it discusses are concerned only with differences between treatments within the same trial[^piepho2018tutorial-e1]. It answers questions like "in the field, how much better is treatment A than treatment B?". The table below is our own summary; cells with footnotes are supported by sources:

| | Research-station plot trial | Multi-environment trial | On-farm trial |
|---|---|---|---|
| Where | Research station, highly controlled conditions[^kool2020reproducibility-e13] | Several sites, possibly over several years[^smith2005analysis-e1] | The farmer's own field; the researcher has much less control[^kool2020reproducibility-e13] |
| Main question | Treatment effects under controlled conditions | How varieties perform across environments[^smith2005analysis-e1] | Under what conditions the effect occurs and for whom it is relevant[^kool2020reproducibility-e12] |
| Main difficulty | Field heterogeneity, unexpected disturbances | Variety-by-environment interaction[^smith2005analysis-e3]; not every variety is grown in every environment[^smith2005analysis-e2] | Farmers' practices vary; replication is hard |

How to choose: to understand mechanisms or compare many treatments, start at a research station; to recommend a variety or technology, go across sites and years; to know whether something works when farmers use it, go into farmers' fields. The three often follow one another.

---

## 2. How to do it

Kramer, Paparozzi, and Stroup wrote in the *Journal of the American Society for Horticultural Science* in 2016: "plan before you plant"; statistical thinking before data collection is the most important use of statistics in research[^kramer2016statistics-e10]. The nine steps below are in chronological order.

### Step 1: State your objective, treatments, and controls

**How:**
- Write, in one or two sentences, the question you want to answer and the decision you will make based on it.
- Write down the treatment design and the experimental design separately. The publications handbook that the American Society of Agronomy (ASA), the Crop Science Society of America (CSSA), and the Soil Science Society of America (SSSA) (together, "the Tri-Societies" below) produce for their journals and books draws the distinction this way. The **treatment design** is which factors you care about, which levels each factor takes, how the factors relate (for example, running every combination of two factors is a factorial structure), and which blocking variables and covariates you choose. The **experimental design** is how the experimental units are arranged and how treatments are assigned to them[^asa2024style-e10].
- Set up controls. For example, in augmented designs for comparing varieties, check cultivars are added at random to individual blocks to help estimate error and small-scale spatial differences[^casler2015fundamentals-e41].
- For quantitative treatments such as fertilizer rate or seeding density, think about the spacing between levels, because you will later analyze them in order (see Step 6).

**Why:** the treatment design and the experimental design determine which analysis you can use later.

**Where people go wrong:** Kool and colleagues point out that on-farm trials often use "farmer practice" as the control but assume it is the same everywhere and known to the reader[^kool2020reproducibility-e3]. Write down exactly what the control involves, as concrete operations.

### Step 2: Choose a design, plot size, and number of replicates

**How:**
- Choose a design based on the direction of variation in the field and on practical needs; see the [field overview](../README.md#blocking-and-randomization). Describe the design in full: "a split-plot design with A as the main plot and B as the subplot" is incomplete; you also need to state the basic design used for the main-plot factor A, for example randomized complete blocks[^casler2015fundamentals-e39].
- Decide plot size. By Smith's law, the variance of a single plot decreases as plot area increases and gradually levels off[^casler2015fundamentals-e36]: if plots are small, making them a bit larger helps a lot; if they are already large enough, making them larger does almost nothing[^casler2015fundamentals-e37]. Casler's group sets plot size by how much seed and land they have, and by the relationship between variance and plot area estimated for that field in the past[^casler2015fundamentals-e38].
- Before deciding the number of replicates, do a power analysis (for the concept, see the [field overview](../README.md#sites-years-and-power-analysis)). Plot power for different designs and pick one that reaches your target, often set at 80%[^casler2015fundamentals-e29]. The inputs should be **variance components** estimated from past trials[^casler2015fundamentals-e30], that is, the parts of the total variation coming from each level (sites, years, blocks, plots, and so on), so first look for past data in your group or at the research station. Give priority to adding sites and years over adding replicates[^casler2015fundamentals-e27].

**Why:** the larger the plot, the smaller the error per plot, but the fewer replicates and treatments you can fit; if the design is wrong, you often have to wait until next season to start again.

**Where people go wrong:** taking more samples or measuring more plants within one plot does not substitute for more plots; see the [field overview](../README.md#fix-the-experimental-unit-before-you-think-about-replication). Our sources do not cover how wide border rows and guard rows should be or how much edge to discard at harvest; follow your advisor, the research station's practice, or the trial standards for your crop.

### Step 3: Lay out and randomize in the field

**How:**
- Use a random number generator to order the treatments within each block; that is randomization. Arranging them by feel "so they're more evenly spread" is interspersion, and it is subjective[^casler2015fundamentals-e32].
- Once you have the layout, look at the field map. A random arrangement occasionally clumps certain treatments together; if the field's spatial variation happens to line up with that arrangement, it can introduce bias[^casler2015fundamentals-e33]. Spatially balanced complete block designs were developed for this, combining randomization with interspersion[^casler2015fundamentals-e34]. Archive the field map, the randomization program and its random seed, and the plot numbers together; put labeled stakes in the field, take photos, and check the plot numbers.

**Why:** blocking and randomization both act as insurance against things that may go wrong partway through the trial[^casler2015fundamentals-e35].

**Where people go wrong:** moving plots by hand because the random layout "doesn't look right". If you need to adjust, re-randomize the whole thing or switch to a spatially balanced design.

### Step 4: Manage and record throughout the growing season

**How:**
- Before the season starts, draw up a field calendar: when land preparation, sowing, fertilizing, irrigation, spraying, assessments, and harvest each happen.
- Record the date of everything on the day it happens. The plant phenotyping metadata standard MIAPPE calls these "events": both field operations such as sowing or fungicide application and unplanned events such as rainfall or pathogen infection[^papoutsoglou2020enabling-e6]. One of its guiding principles is to reduce the chance that researchers leave important information out[^papoutsoglou2020enabling-e4], and you can use its fields for your records.
- For hail, lodging, animal damage, misapplied sprays, and similar mishaps, record which plots were affected and over what area.

**Why:** this information is hard to fill in afterward. Kool and colleagues analyzed 172 papers on on-farm trials in sub-Saharan Africa published between 1986 and 2015[^kool2020reproducibility-e1]: only 10% fully reported all four items of crop information (variety, planting date, plant spacing, and mono- or intercropping and crop rotation), and only 41% reported the planting date[^kool2020reproducibility-e9].

**Where people go wrong:** weeding, replanting gaps, or irrigating only some plots without recording it. In farmers' fields there is another kind of surprise: a study cited by Kool and colleagues found that farmers copied the management of some treatments and sometimes competed with the researcher-managed plots[^kool2020reproducibility-e11].

### Step 5: Harvest, measure, and check the data

**How:**
- State how each trait was measured[^asa2024style-e1], for example harvested area, moisture adjustment, sampling position, and number of plants. Distinguish the experimental unit from the sampling unit, and record how many samples were taken from each experimental unit[^asa2024style-e2].
- Measurements taken on the same material at different times or positions are often correlated[^asa2024style-e4], and the analysis must deal with this specifically (see Step 6).
- After data entry, check: do the plot numbers match the field map, are there values outside a plausible range, and why are values missing? Then plot the distributions and residuals. If you transform the data (for example, take logs), remember that one transformation affects several statistical assumptions at once[^piepho2018tutorial-e6].

**Why:** Kramer and colleagues examined all 2014 issues and the first 2015 issue of the *Journal of the American Society for Horticultural Science*, 86 papers in all[^kramer2016statistics-e12], and slightly fewer than half appeared to have statistical problems[^kramer2016statistics-e1]. The most common (30 papers) was measuring several variables on the same observational unit without analyzing them appropriately[^kramer2016statistics-e2]. In another 11, the figures showed that the variance increased with the mean, yet the authors used methods that assume the two are unrelated, which shows the assumptions had not been checked[^kramer2016statistics-e3].

**Where people go wrong:** quietly deleting outliers when you find them. Keep the raw data, and write down the reason for every deletion or change.

### Step 6: Analyze with mixed models

A **mixed model** contains both fixed effects and random effects. **Fixed effects** are the factors you care about directly and want to compare; **random effects** are treated as randomly drawn from a larger population, and what you care about is how much variation they contribute.

**How:**
- **Treat treatments as fixed effects.** Treatment factors are usually fixed; nuisance factors such as blocks can be fixed or random[^piepho2018tutorial-e2]. When blocks are large and complete, treating them as fixed is the safer choice[^piepho2018tutorial-e3]; in incomplete block designs, treating blocks as random is what lets you recover treatment information between blocks[^piepho2018tutorial-e4].
- **Write the model to match the design.** Split-plot-type designs must include the error terms for both main plots and subplots as random effects; which error term a treatment factor uses depends on the level of plot to which it was randomized[^piepho2018tutorial-e5].
- **Don't compare quantitative treatments pair by pair.** Running pairwise multiple comparisons between several nitrogen rates and assigning letters, without regard to the order of the levels, is totally inappropriate[^piepho2018tutorial-e7]; use an approach that respects the order, such as regression.
- **Model repeated measures explicitly.** Data from repeated measurements on the same unit are very common in agronomic research, yet they are often misunderstood and analyzed inappropriately[^piepho2018tutorial-e8].
- **Report the standard error of a difference.** To show how much two treatments differ you need a confidence interval, or at least the standard error of the difference, which is not interchangeable with the standard error of a mean[^kramer2016statistics-e5]; in designs with blocks, you cannot derive the former directly from the latter[^kramer2016statistics-e6].
- **Report variance components.** For blocked trials across several sites and years, mixed models estimate each variance component directly[^casler2015fundamentals-e31]. Put them in the paper or a supplementary table so others (including you next year) can use them for power analysis.

**Why:** blocks, sites, and years were usually treated as fixed effects in the past; only with the software that arrived in the early 1990s could they be treated correctly as random effects[^kramer2016statistics-e8]. Copying the analysis from older papers can easily lead you astray.

**Where people go wrong:** the design has blocks, sites, or years, but they are left out of the analysis model; 7 of the 86 papers Kramer and colleagues examined did this[^kramer2016statistics-e4]. The wrong software procedure also causes problems, for example using PROC GLM in the statistical software SAS to analyze data with random effects[^kramer2016statistics-e11]. If you need a method you are not familiar with, bring in a statistician as a collaborator early[^kramer2016statistics-e13]. For general statistical practice, see the Part 2 chapter section [Report how big the difference is and how sure you are, not just the p-value](../../../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 7: Multi-environment trials

**How:**
- Yield data for breeding and variety evaluation generally come from a series of field trials at several sites, possibly over several years, called **multi-environment trials**[^smith2005analysis-e1].
- Analyze them with linear mixed models: they can handle varieties not grown in every environment, use more realistic models of within-trial error (incomplete blocks, spatial correlation), and treat variety or environment effects as random[^smith2005analysis-e2]. But don't look only at average performance: Smith and colleagues point out that traditional analysis of variance does not reveal the nature of the variety-by-environment interaction, which can hamper variety selection and recommendation[^smith2005analysis-e3].
- Keep the raw data for every plot. Computing variety means trial by trial and then combining them (two-stage analysis) is only an approximation to analyzing all plot data directly (one-stage analysis). People used to do it because plot data often were not stored electronically, which should no longer be a problem[^smith2005analysis-e4][^smith2005analysis-e5].

**Why:** the same variety often performs differently at different sites and in different years; see the [field overview](../README.md#multiple-sites-multiple-years).

**Where people go wrong:** attributing good performance at one site to "more rain there". Environmental variables such as rainfall were not replicated, so they cannot support that conclusion[^casler2015fundamentals-e42].

> **Where sources disagree: should variety effects be fixed or random?**
>
> - **Random**: Smith and colleagues argue that variety effects should be treated as random, because this minimizes the chance of picking the wrong variety when selecting the best ones[^smith2005analysis-e7].
> - **Fixed**: Piepho and Edmondson's tutorial says that treatment factors are of direct interest and are usually treated as fixed[^piepho2018tutorial-e2]. Smith and colleagues themselves concede that getting people to adopt random variety effects has not been easy and that the point remains contentious among statisticians[^smith2005analysis-e6].
> - **Our suggestion**: if the goal is to compare a few specified treatments (such as several fertilizer regimes), treat them as fixed; if the goal is to select and predict among many lines, consider treating them as random. Either way, state your choice and your reason in the methods.

### Step 8: Run on-farm trials with farmers

**How:** why to do them, how to involve farmers, mother and daughter trials, and how to spell out the "farmer practice" are covered in the [field overview](../README.md#doing-research-with-farmers). This step adds a few points:
- **First agree on what each party wants.** In a 2022 Perspective in *Nature Food*, Lacoste and colleagues define on-farm experimentation as an innovation process that brings agricultural stakeholders together around mutually beneficial experimentation to support farmers' own management decisions[^lacoste2022onfarm-e1]. It takes place in farmers' own fields, at scales meaningful to them, and openly acknowledges each party's private interests[^lacoste2022onfarm-e2].
- **When farmers don't want much replication**, Casler gives three options: use several farms as blocks; intersperse one control among the other treatments; or combine both[^casler2015fundamentals-e43]. Putting the control in every other plot takes up half the plots and is inefficient, but it remains a very viable option for small on-farm trials[^casler2015fundamentals-e40].
- **State which sites, farmers, and fields you chose and why**, and say under what conditions the effect occurs and for whom it is relevant[^kool2020reproducibility-e12]. **Take the results back.** Kyveryga, who wrote the introduction to the 2019 *Agronomy Journal* special issue on on-farm research, considers it one of the keys of on-farm research to analyze and summarize the results well and present them to farmers and agronomists[^kyveryga2019onfarm-e5].

**Why:** in farmers' fields, researchers have much less control[^kool2020reproducibility-e13], so conclusions from a research station do not necessarily carry over directly.

**Where people go wrong:** writing only "managed according to farmer practice" or "weeded as necessary". Kool and colleagues point out that such descriptions don't say what was actually done, so nobody else can reproduce the trial[^kool2020reproducibility-e10].

> **Where sources disagree: how much statistical rigor do on-farm trials need?**
>
> - **Keep controls and replication**: Casler's three options for researchers organizing on-farm trials all revolve around blocks and control plots[^casler2015fundamentals-e43]; he considers the inefficient control-plot designs still very viable for small on-farm trials[^casler2015fundamentals-e40].
> - **Put farmers' needs first**: Lacoste and colleagues point out that variation in crop production over space and time is much larger than the effects of experimental treatments[^lacoste2022onfarm-e3]; statistical significance says nothing about whether a result is useful locally[^lacoste2022onfarm-e4]; and farmers may not value statistical results and replication much[^lacoste2022onfarm-e5].
> - **Our suggestion**: for trials you will write up as papers, keep randomization and true replication; separately, put together the information that is useful to farmers (the effect in each field, the economic return) for them.

### Step 9: Write it up

**How:** start by reading your target journal's instructions for authors. Taking the Tri-Societies' journals as an example, their publications handbook requires the methods section to describe blocking, experimental unit sizes, the number of sites and years, the number of replicates, field conditions, how each trait was measured, and so on[^asa2024style-e1]; see the [field overview](../README.md#statistical-analysis-and-reporting) for details. The handbook also requires, for each analysis, a brief description of the statistical method with a reference giving full details, and a statement of how well the statistical assumptions were met[^asa2024style-e11]. Name the software you used too, but Kramer and colleagues caution that software is only a tool for carrying out an analysis, not a statistical method in itself[^kramer2016statistics-e7]; naming the software is not the same as describing the method.

**Why:** the Tri-Societies' handbook says readers need to understand how the experiment was designed and conducted to judge whether the results are credible, and to design future research on that basis[^asa2024style-e9].

**Where people go wrong:** writing only "analyzed with SAS" without saying which fixed and random effects are in the model. For general writing advice, see the Writing and publishing chapter [Telling the story and writing the paper](../../../03_write-and-publish/01_story-and-paper.md).

---

## 3. Checklist

Our sources include no reporting guideline specific to field trials; the list below is compiled from the Tri-Societies' publications handbook and the sources above.

**Must do**
- [ ] Describe the treatment design and the experimental design; for split plots, state the basic design of the main plots[^asa2024style-e10][^casler2015fundamentals-e39]
- [ ] Randomize with a random number generator[^casler2015fundamentals-e32], and keep the field map
- [ ] Describe the experimental unit and the sampling unit, and how many of each[^asa2024style-e2]
- [ ] Record field operations and unplanned events with dates[^papoutsoglou2020enabling-e6]
- [ ] Make the analysis model match the design: blocks, sites, years, and main-plot error are all in the model[^kramer2016statistics-e4][^piepho2018tutorial-e5]
- [ ] Check the statistical assumptions and report how well they were met[^asa2024style-e11]
- [ ] Give standard errors or confidence intervals for data used to draw conclusions (a requirement of the Tri-Societies' journals)[^asa2024style-e3]
- [ ] Describe controls (including "farmer practice") as concrete operations[^kool2020reproducibility-e10]

**Better practice**
- [ ] Do a power analysis with variance components from past trials before you start[^casler2015fundamentals-e29][^casler2015fundamentals-e30]
- [ ] If the random layout clumps, consider a spatially balanced design[^casler2015fundamentals-e34]
- [ ] Report variance components so others can plan trials
- [ ] Don't use pairwise multiple comparisons for quantitative treatments[^piepho2018tutorial-e7]
- [ ] In multi-environment trials, keep the data for every plot[^smith2005analysis-e5]
- [ ] In on-farm trials, make public the criteria for choosing sites, farmers, and fields[^kool2020reproducibility-e12]

**Fine to skip; not a flaw**
- Using a design with interspersed control plots in a small on-farm trial: inefficient, but still a viable choice[^casler2015fundamentals-e40].

**Common reviewer criticisms that don't hold up**
- Alleging "pseudoreplication" without analysis. The ecologists Davies and Gray argued in 2015 that before making the allegation, a reviewer should show that it holds statistically[^davies2015pseudoreplication-e4]; you can use nested and random-effects approaches and acknowledge the limits of statistical inference[^davies2015pseudoreplication-e3]. See the [field overview](../README.md#pseudoreplication-treatment-confounded-with-the-plot) for details.
- Questioning correct modern methods. Kramer and colleagues point out that reviewers whose statistical knowledge is out of date may reject a paper believing the statistics are wrong, when the methods are in fact correct[^kramer2016statistics-e9]. In your response, cite the source of the method.

---

## 4. Common mistakes

| Mistake (examples written by us) | Why it is a problem |
|---|---|
| Moving plots by hand because the random layout doesn't look right | Subjective interspersion is not randomization[^casler2015fundamentals-e32] |
| Not recording sowing or spraying dates, then relying on memory when writing the paper | Of the 172 papers on on-farm trials in sub-Saharan Africa analyzed by Kool and colleagues, only 41% reported the planting date[^kool2020reproducibility-e9] |
| Blocks and several sites in the design, but only a one-way analysis of variance in the analysis | The analysis ignores sources of variation built into the design[^kramer2016statistics-e4] |
| Comparing several nitrogen rates pair by pair and assigning letters | Ignores the order of the levels[^piepho2018tutorial-e7] |
| Keeping only site means from a multi-environment trial and losing the plot data | Only the approximate two-stage analysis is then possible[^smith2005analysis-e4] |

---

## 5. Further reading

- **Casler 2015 (*Agronomy Journal*)**: replication, randomization, blocking, plot size, and power analysis. Read it before you design a trial.
- **Piepho and Edmondson 2018 (*Journal of Agronomy and Crop Science*)**: uses field examples to explain mixed-model analysis of factorial designs, split plots, quantitative treatments, and repeated measures, with SAS and R code. Work through it alongside your own analysis.
- **Smith, Cullis, and Thompson 2005 (*Journal of Agricultural Science*)**: a review of mixed-model analysis of multi-environment trials. Read it when you run variety trials.
- **Kramer, Paparozzi, and Stroup 2016 (*Journal of the American Society for Horticultural Science*)**: a catalog of statistical errors in one horticulture journal; check your own paper against it before submitting.
- **Lacoste et al. 2022 (*Nature Food*)**: how to put farmers at the center of on-farm experimentation. For the Tri-Societies' publications handbook, Kool et al. 2020, and others, see the [field overview's further reading](../README.md#further-reading).

[^piepho2018tutorial-e1]: Piepho & Edmondson 2018, 1 Introduction. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e1)
[^piepho2018tutorial-e2]: Piepho & Edmondson 2018, 2.2.1 Block effects. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e2)
[^piepho2018tutorial-e3]: Piepho & Edmondson 2018, 2.2.1 Block effects. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e3)
[^piepho2018tutorial-e4]: Piepho & Edmondson 2018, 2.2.1 Block effects. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e4)
[^piepho2018tutorial-e5]: Piepho & Edmondson 2018, split-plot example. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e5)
[^piepho2018tutorial-e6]: Piepho & Edmondson 2018, 10 Discussion. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e6)
[^piepho2018tutorial-e7]: Piepho & Edmondson 2018, 10 Discussion. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e7)
[^piepho2018tutorial-e8]: Piepho & Edmondson 2018, 10 Discussion. [Evidence](../../../../sources/notes/piepho2018tutorial.md#e8)
[^kool2020reproducibility-e1]: Kool et al. 2020, Methods. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e1)
[^kool2020reproducibility-e9]: Kool et al. 2020, Results, Crop information. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e9)
[^kool2020reproducibility-e10]: Kool et al. 2020, Results. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e10)
[^kool2020reproducibility-e3]: Kool et al. 2020, Abstract. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e3)
[^kool2020reproducibility-e11]: Kool et al. 2020, Discussion. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e11)
[^kool2020reproducibility-e12]: Kool et al. 2020, Abstract. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e12)
[^kool2020reproducibility-e13]: Kool et al. 2020, Introduction. [Evidence](../../../../sources/notes/kool2020reproducibility.md#e13)
[^smith2005analysis-e1]: Smith et al. 2005, Introduction. [Evidence](../../../../sources/notes/smith2005analysis.md#e1)
[^smith2005analysis-e2]: Smith et al. 2005, Introduction. [Evidence](../../../../sources/notes/smith2005analysis.md#e2)
[^smith2005analysis-e3]: Smith et al. 2005, Introduction. [Evidence](../../../../sources/notes/smith2005analysis.md#e3)
[^smith2005analysis-e4]: Smith et al. 2005, Two-stage analyses. [Evidence](../../../../sources/notes/smith2005analysis.md#e4)
[^smith2005analysis-e5]: Smith et al. 2005, Two-stage analyses. [Evidence](../../../../sources/notes/smith2005analysis.md#e5)
[^smith2005analysis-e6]: Smith et al. 2005, Conclusions. [Evidence](../../../../sources/notes/smith2005analysis.md#e6)
[^smith2005analysis-e7]: Smith et al. 2005, Conclusions. [Evidence](../../../../sources/notes/smith2005analysis.md#e7)
[^kramer2016statistics-e1]: Kramer et al. 2016, Abstract. [Evidence](../../../../sources/notes/kramer2016statistics.md#e1)
[^kramer2016statistics-e12]: Kramer et al. 2016, Methods. [Evidence](../../../../sources/notes/kramer2016statistics.md#e12)
[^kramer2016statistics-e13]: Kramer et al. 2016, Abstract. [Evidence](../../../../sources/notes/kramer2016statistics.md#e13)
[^kramer2016statistics-e2]: Kramer et al. 2016, Statistical problems. [Evidence](../../../../sources/notes/kramer2016statistics.md#e2)
[^kramer2016statistics-e3]: Kramer et al. 2016, Statistical problems. [Evidence](../../../../sources/notes/kramer2016statistics.md#e3)
[^kramer2016statistics-e4]: Kramer et al. 2016, Statistical problems. [Evidence](../../../../sources/notes/kramer2016statistics.md#e4)
[^kramer2016statistics-e5]: Kramer et al. 2016, Statistical problems. [Evidence](../../../../sources/notes/kramer2016statistics.md#e5)
[^kramer2016statistics-e6]: Kramer et al. 2016, Statistical problems. [Evidence](../../../../sources/notes/kramer2016statistics.md#e6)
[^kramer2016statistics-e7]: Kramer et al. 2016, Software packages. [Evidence](../../../../sources/notes/kramer2016statistics.md#e7)
[^kramer2016statistics-e8]: Kramer et al. 2016, Underlying reasons. [Evidence](../../../../sources/notes/kramer2016statistics.md#e8)
[^kramer2016statistics-e9]: Kramer et al. 2016, Underlying reasons. [Evidence](../../../../sources/notes/kramer2016statistics.md#e9)
[^kramer2016statistics-e10]: Kramer et al. 2016, Recommendations. [Evidence](../../../../sources/notes/kramer2016statistics.md#e10)
[^kramer2016statistics-e11]: Kramer et al. 2016, Software packages. [Evidence](../../../../sources/notes/kramer2016statistics.md#e11)
[^asa2024style-e10]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e10)
[^asa2024style-e1]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e1)
[^asa2024style-e2]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e2)
[^asa2024style-e11]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e11)
[^asa2024style-e3]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e3)
[^asa2024style-e4]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e4)
[^asa2024style-e9]: American Society of Agronomy et al. 2024, Publications Handbook, Chapter 4. [Evidence](../../../../sources/notes/asa2024style.md#e9)
[^casler2015fundamentals-e29]: Casler 2015, power analysis example. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e29)
[^casler2015fundamentals-e30]: Casler 2015, allocation of resources. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e30)
[^casler2015fundamentals-e31]: Casler 2015, Table 2. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e31)
[^casler2015fundamentals-e32]: Casler 2015, Randomization. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e32)
[^casler2015fundamentals-e33]: Casler 2015, Randomization. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e33)
[^casler2015fundamentals-e34]: Casler 2015, Randomization. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e34)
[^casler2015fundamentals-e35]: Casler 2015, Blocking. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e35)
[^casler2015fundamentals-e36]: Casler 2015, Size of experimental units. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e36)
[^casler2015fundamentals-e37]: Casler 2015, Size of experimental units. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e37)
[^casler2015fundamentals-e38]: Casler 2015, Size of experimental units. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e38)
[^casler2015fundamentals-e39]: Casler 2015, Blocking, split-plot designs. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e39)
[^casler2015fundamentals-e40]: Casler 2015, Replication, check-plot designs. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e40)
[^casler2015fundamentals-e41]: Casler 2015, Replication, augmented designs. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e41)
[^casler2015fundamentals-e27]: Casler 2015, allocation of resources. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e27)
[^casler2015fundamentals-e42]: Casler 2015, Replication. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e42)
[^casler2015fundamentals-e43]: Casler 2015, Replication, on-farm trials. [Evidence](../../../../sources/notes/casler2015fundamentals.md#e43)
[^papoutsoglou2020enabling-e6]: Papoutsoglou et al. 2020, the "Event" section of MIAPPE 1.1. [Evidence](../../../../sources/notes/papoutsoglou2020enabling.md#e6)
[^papoutsoglou2020enabling-e4]: Papoutsoglou et al. 2020, guiding principles of MIAPPE. [Evidence](../../../../sources/notes/papoutsoglou2020enabling.md#e4)
[^lacoste2022onfarm-e1]: Lacoste et al. 2022, OFE embeds research in farm management. [Evidence](../../../../sources/notes/lacoste2022onfarm.md#e1)
[^lacoste2022onfarm-e2]: Lacoste et al. 2022, OFE embeds research in farm management. [Evidence](../../../../sources/notes/lacoste2022onfarm.md#e2)
[^lacoste2022onfarm-e3]: Lacoste et al. 2022, Progressing experimentation. [Evidence](../../../../sources/notes/lacoste2022onfarm.md#e3)
[^lacoste2022onfarm-e4]: Lacoste et al. 2022, Progressing experimentation. [Evidence](../../../../sources/notes/lacoste2022onfarm.md#e4)
[^lacoste2022onfarm-e5]: Lacoste et al. 2022, Figure 2 caption. [Evidence](../../../../sources/notes/lacoste2022onfarm.md#e5)
[^kyveryga2019onfarm-e5]: Kyveryga 2019, Introduction. [Evidence](../../../../sources/notes/kyveryga2019onfarm.md#e5)
[^davies2015pseudoreplication-e4]: Davies & Gray 2015, Abstract. [Evidence](../../../../sources/notes/davies2015pseudoreplication.md#e4)
[^davies2015pseudoreplication-e3]: Davies & Gray 2015, Abstract. [Evidence](../../../../sources/notes/davies2015pseudoreplication.md#e3)
