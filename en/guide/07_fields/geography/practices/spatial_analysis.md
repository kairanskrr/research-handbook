# Spatial analysis

This page covers **quantitative research that answers questions with location data**: you put the data on a map, check whether they cluster in space, analyze them with statistical models that take spatial relationships into account, and publish the results as honest maps. It is a common method in social and economic geography `[Our analysis]`, but not only there. Zandbergen notes that in public health research, address geocoding (turning addresses into points on a map) is an established analytical tool[^zandbergen2014ensuring-e1]; the reproducibility examples collected by Nüst and Pebesma also come from spatial data collection and analysis in ecology, spatial statistics, and similar areas[^nust2021practical-e4]. For background on physical geography and environmental data, see the [Earth and environmental sciences page](../../earth-environmental-sciences/README.md); for health data, see the [Health sciences page](../../health-sciences/README.md).

The modifiable areal unit problem, the ecological fallacy, the uncertain geographic context problem, location privacy, and reproducibility and replicability are already covered in the geography field overview (see [Pitfalls of spatial analysis](../README.md#pitfalls-of-spatial-analysis-change-the-units-and-the-conclusion-may-change), [Location privacy](../README.md#location-privacy-coordinates-are-identifying-information), and [Reproducibility and replicability](../README.md#reproducibility-and-replicability)). This page does not repeat them; it covers only how to do the work. For general data analysis that does not involve location, see [Data science research](../../../06_methods/data_science.md) in the research methods.

Much of the practical advice here comes from two free online textbooks (*Geographic Data Science with Python* by Rey and colleagues, and *Spatial Data Science* by Pebesma and Bivand) and one software workbook (Anselin's GeoDa workbook). These are their authors' recommendations, not rules agreed across the field `[Our analysis]`.

**Scope** `[Our analysis]`: this is a common research method in social and economic geography, also used in the public health, ecology, and other areas mentioned above. For the general logic of describing spatial distributions and testing "how the environment affects individuals," see the research strategies [Description](../../../05_research-strategies/observe_describe.md) and [Causal explanation](../../../05_research-strategies/explain_causality.md). For the steps shared by every field, such as choosing a topic, planning, and writing, see the chapters of each Part, for example [From research questions to an evidence plan](../../../02_do-the-project/01_question-to-evidence.md) and [Analysis and interpretation](../../../02_do-the-project/07_analyze-and-interpret.md).

**Strategies it usually serves**: [Description](../../../05_research-strategies/observe_describe.md) (describing how a phenomenon is distributed in space and testing whether it clusters) and [Causal explanation](../../../05_research-strategies/explain_causality.md) (studying how the environment or neighboring areas affect an outcome) `[Our analysis]`. The basis: in a test with Moran's I (a statistic that tests for spatial clustering; see Step 6), only a small enough p-value lets you reject "the pattern on this map is random"[^rey2023geographic-e15], which is a test of distribution; studying the effects of the social and physical environment on health is about what the environment does[^kwan2012uncertain-e4].

**After reading this page, you should be able to:**

- write a research question in the form "what spatial process, on what units, at what scale," and plan sensitivity analyses in advance;
- check coordinate reference systems and geocoding errors, and do spatial joins and aggregation correctly;
- draw maps with honest classification and color schemes;
- test for spatial autocorrelation with Moran's I, and know when ordinary regression goes wrong;
- protect participants' location privacy before you publish maps and data, and make the whole analysis rerunnable by others.

---

## 1. What this research is and when to use it

When "where" matters in your question (whether a phenomenon is concentrated in space, whether nearby places influence each other, whether an environmental exposure is related to a health outcome), you need spatial analysis `[Our analysis]`. Even if you did not plan to study space, as long as your data carry locations, the errors of an ordinary regression may cluster in space and violate the regression's assumptions[^rey2023geographic-e16], so it is worth checking first `[Our analysis]`.

| | Spatial analysis | General data science | Qualitative fieldwork, participatory mapping |
|---|---|---|---|
| Core question | How location and proximity affect outcomes | Predictive or explanatory relationships between variables | How people understand and use a place |
| Distinctive risks | Conclusions change with units and scale[^kwan2018limits-e2]; errors cluster in space[^rey2023geographic-e16]; coordinates expose individuals[^zandbergen2014ensuring-e3] | Data leakage and overfitting; see [Data science research](../../../06_methods/data_science.md) | Researcher positionality; see the [geography field overview](../README.md#positionality-and-reflexivity-describe-the-research-instrument-itself) |
| Main guidance | This page | [Data science research](../../../06_methods/data_science.md) in the research methods | [Interview studies](../../../06_methods/interview_study.md), [Case study and ethnography](../../../06_methods/case_study.md) |

Spatial analysis and qualitative fieldwork can be combined: use spatial analysis to find patterns, then interviews to understand the reasons; see [Mixed methods](../../../06_methods/mixed_methods.md) `[Our analysis]`.

---

## 2. How to do it

### Step 1: Pin down the spatial question

**How:** Write down three things: the spatial process you have in mind (for example, "neighboring areas imitate each other" or "the closer to a pollution source, the worse the health"); what data you will measure it with; and how you will turn it into concrete units, distances, and definitions of "neighbor" in the analysis. Kedron and colleagues point out that these three pieces of information are exactly what others need to reproduce a geographic study[^kedron2021reproducibility-e13]. Then ask one more question: is your conclusion about **areas** or about **individuals**? Answering a question about individuals with area data can land you in the ecological fallacy (see the [field overview](../README.md#pitfalls-of-spatial-analysis-change-the-units-and-the-conclusion-may-change)) `[Our analysis]`.

**Why:** these choices drive every later step; if you don't write them down clearly, nobody can tell where your conclusions came from `[Our analysis]`.

**Where people go wrong:** you get a ready-made dataset aggregated by administrative district first and work backward to a question, and the units end up not matching the question `[Our analysis]`.

### Step 2: Choose spatial units and scale, and plan sensitivity analyses in advance

**How:**

- List the candidate units. Kwan's 2018 paper lists the spatial units commonly used in geography, environmental health, and social science research as census tracts, census block groups, and postal code areas, and the temporal units as days, months, and years; change the units and the results may differ[^kwan2018limits-e1].
- Choose the units for your main analysis, and state in your methods section which units you used, how close they are to the true geographic context, and which temporal factors you considered[^kwan2012uncertain-e6]. For the different ways to delineate a "neighborhood," see the [field overview](../README.md#pitfalls-of-spatial-analysis-change-the-units-and-the-conclusion-may-change).
- Before the analysis starts, write down the other scales, zonings, and definitions of "neighbor" you will try. Kedron and colleagues argue that a pre-analysis plan for geographic research may need to state the scale of analysis; if you use spatial statistical methods, you also need to list and justify the spatial weights matrices you will examine (see Step 6)[^kedron2021reproducibility-e4].
- Report all the results. Whether the conclusion holds up across settings is itself a finding `[Our analysis]`.

**Why:** results from area data change with scale and zoning[^kwan2018limits-e2]. And there are many possible settings, so reporting only one amounts to cherry-picking a specification; see [Field overview: Reproducibility and replicability](../README.md#reproducibility-and-replicability).

**Where people go wrong:** using "the best-fitting model" to prove you chose the right units. Kwan points out that the best-fitting model does not necessarily use the true geographic context[^kwan2012uncertain-e7].

### Step 3: Know your data sources and positional accuracy

**How:**

- **Record the coordinate reference system of every dataset** (the set of rules that says which place on Earth the coordinate numbers refer to). Pebesma and Bivand's textbook points out that latitude and longitude only have a definite meaning when the geodetic datum (the reference model of Earth's shape) is given[^pebesma2023spatial-e1]; converting coordinates between datums is approximate and carries its own error[^pebesma2023spatial-e3]; and you can no longer assume that coordinates always come "longitude first"[^pebesma2023spatial-e4]. If locations look obviously wrong when plotted, check the coordinate order first `[Our analysis]`.
- **Choose a projection for the job** (a projection is a method of drawing spherical coordinates on a flat surface). After projection, at least one of shape, direction, and area is distorted[^pebesma2023spatial-e2]. When you need to compute area or distance, choose a projection that preserves that quantity for your study area, and state it in the paper `[Our analysis]`.
- **Report geocoding quality.** Geocoding has errors: some addresses cannot be matched because they are incomplete or wrong, and matched ones may be inaccurate[^zandbergen2014ensuring-e2]. Record the match rate, and check whether unmatched addresses are concentrated in certain kinds of areas, because that would bias the sample `[Our analysis]`.
- **Keep online data exactly as you got them.** Nüst and Pebesma warn that online geographic services can change or disappear, so save the code that accesses them, the requests sent, and the results returned[^nust2021practical-e7].

For general data quality checks (missing data, provenance, measurement error), see [Data science: Step 2](../../../06_methods/data_science.md#step-2-understand-where-the-data-came-from-and-how-good-it-is).

### Step 4: Clean and join spatial data

**How:**

- Before any overlay or join, transform all layers to the same coordinate reference system `[Our analysis]`.
- **Know whether each attribute value belongs to a point or to a whole area.** Some values hold for every point within an area; others are summaries for the whole area[^pebesma2023spatial-e5]. For example, when you replace a county with its centroid, the county's population count does not belong to that point[^pebesma2023spatial-e6]. Pebesma and Bivand argue that thinking about whether the information also changes when you change the geometry avoids a whole class of common mistakes[^pebesma2023spatial-e7].
- **Check for double counting when you aggregate.** When you aggregate data to another set of boundaries using a spatial relation such as "intersects," the same record can be counted in several areas[^pebesma2023spatial-e8]; a point that falls exactly on a boundary is assigned to both areas[^pebesma2023spatial-e9]. After aggregating, check that the totals match the original data `[Our analysis]`.
- **Tell totals from ratios.** A total such as population count must be split when an area is split; a ratio such as population density cannot be summed after splitting[^pebesma2023spatial-e10]. Allocating data to new boundaries in proportion to area is only reasonable when "the total is spread evenly within the original area and the ratio is the same everywhere"[^pebesma2023spatial-e11]; state this assumption in the paper `[Our analysis]`.

**Where people go wrong:** merging two datasets directly by place name or code without noticing that administrative boundaries changed between the two years `[Our analysis]`.

### Step 5: Exploratory analysis and honest maps

**How:**

- **Choose the classification method before you look at the map.** For how to classify a choropleth map (a map that shades areas by value), the textbook by Rey and colleagues recommends considering both the distribution of the data and the purpose of the map (highlighting outliers, or faithfully showing the distribution)[^rey2023geographic-e5]. Equal intervals look only at the minimum and maximum, and can produce classes with almost no observations[^rey2023geographic-e6]; quantiles avoid this, but class widths can vary a lot, which invites misreading[^rey2023geographic-e7]. State the classification method and the break points in the legend `[Our analysis]`.
- **Choose a color scheme by variable type.** The same textbook recommends: sequential schemes for continuous data that start at one end; diverging schemes when there is a meaningful midpoint and both ends matter equally; and qualitative schemes for categorical data[^rey2023geographic-e9][^rey2023geographic-e10]. ColorBrewer is a color tool designed for mapmaking and offers all three types[^crameri2020misuse-e6].
- **Avoid rainbow color maps and red-green schemes of similar lightness.** This is the view of Crameri and colleagues (earth scientists) in a paper on the misuse of color in science: the brightest yellow in a rainbow scheme unfairly highlights one range of values[^crameri2020misuse-e3], whereas perceptually uniform schemes make equal differences look equally large[^crameri2020misuse-e7]; red-green schemes of similar lightness cannot be read by a large share of readers[^crameri2020misuse-e4]; and the wrong colors amount to highlighting part of the data, and lose meaning when printed in black and white[^crameri2020misuse-e2].
- **Remind yourself that large areas grab attention.** The eye is drawn to large areas, even when they are not the most important for the analysis[^rey2023geographic-e8].

**Why:** people are very good at spotting patterns, and often see patterns in randomness[^rey2023geographic-e13]. Crameri and colleagues also argue that color is often chosen passively and does not get the scrutiny other methods do[^crameri2020misuse-e5]. So use maps only to generate hypotheses; whether something "clusters" has to be settled by the statistical test in the next step `[Our analysis]`.

### Step 6: Test for spatial autocorrelation

**Spatial autocorrelation** is how much the similarity between observations is related to how close their locations are[^rey2023geographic-e11]. For example, in the distribution of income or poverty, similar values often sit next to each other: wealthy areas border wealthy areas[^rey2023geographic-e12]. When this happens, the errors of an ordinary regression may cluster in space, violating the assumption that errors are independent and identically distributed[^rey2023geographic-e16].

**How:**

1. **Define "neighbor" (the spatial weights matrix).** It specifies who counts as whose neighbor and is the main way to bring spatial relationships into the analysis[^rey2023geographic-e1]. You can require a shared edge to count as neighbors (rook contiguity), or count a single shared vertex (queen contiguity)[^rey2023geographic-e2], or define neighbors by distance. When observations are unevenly dense, using one distance threshold for the whole study area leaves some places with many neighbors and others with almost none[^rey2023geographic-e3]. For "islands," units with no neighbors at all, the textbook by Rey and colleagues recommends dealing with them before use[^rey2023geographic-e4].
2. **Compute Moran's I.** It is arguably the most commonly used global measure of spatial autocorrelation[^anselin2020global-e1]. Its value equals the slope of the fitted line on the Moran scatter plot (the variable on the horizontal axis, the average of its neighbors on the vertical axis)[^rey2023geographic-e14]. Look at the scatter plot first: in an example from the GeoDa workbook, a few extreme high values changed the shape of the scatter plot[^anselin2020global-e8].
3. **Judge significance with a permutation test.** A permutation test randomly reshuffles the observed values across locations and recomputes the statistic many times, which gives a reference distribution for "spatial randomness"[^anselin2020global-e2]. The GeoDa workbook considers 999 permutations usually enough[^anselin2020global-e5]. Only a small enough p-value lets you reject "the pattern on this map is random"[^rey2023geographic-e15]. A p-value obtained this way is called a pseudo p-value, and it depends on the number of permutations: 0.01 from 99 permutations is not necessarily more significant than 0.001 from 999[^anselin2020global-e3]. The "high-high" and "low-low" categories on the scatter plot do not by themselves indicate significance[^anselin2020global-e4]; the standard errors and t-values that an ordinary scatter plot gives do not apply in the spatial case either[^anselin2020global-e7].
4. **Fix the random seed and report it.** GeoDa uses a fixed seed by default, which helps reproducibility; but the workbook also warns that even with the same seed, results can differ on different hardware (for example, a different number of CPU cores)[^anselin2020global-e6]. When Nüst and Pebesma reproduced other people's studies, they also listed setting a random seed as a good practice[^nust2021practical-e5].
5. **Recompute with several weights matrices**, and report all of them as planned in Step 2[^kedron2021reproducibility-e4].

### Step 7: Getting started with spatial regression

**How:**

1. Run an ordinary regression first, map the residuals, and compute Moran's I on the residuals `[Our analysis]`. If the residuals cluster, you may have left out a variable with a spatial pattern; adding it may make the pattern disappear[^rey2023geographic-e17].
2. Decide what kind of spatial effect you have. **Spatial heterogeneity**: some parts of the model vary systematically with location[^rey2023geographic-e18]; consider regional fixed effects or estimating separately by region `[Our analysis]`. **Spatial dependence**: what happens in neighboring areas affects the local outcome; consider a spatial lag model (which puts the neighbors' dependent variable into the model) or a spatial error model (which lets the error terms be correlated among neighbors) `[Our analysis]`.
3. Both kinds of model violate the assumptions of ordinary least squares (OLS, the standard estimation method for ordinary linear regression) and need dedicated estimation methods[^rey2023geographic-e19]. The textbook by Rey and colleagues points out that when spatial correlation is present, OLS gets the confidence intervals wrong[^rey2023geographic-e21]; the coefficients of a spatial lag model also need careful interpretation[^rey2023geographic-e20].

**Where people go wrong:** picking a model from the software menu without being able to say what spatial process it corresponds to `[Our analysis]`. There are many kinds of spatial econometric models, and this page covers only the first decisions; before using them for real, read the textbooks in Section 5 or ask someone who knows spatial statistics `[Our analysis]`.

### Step 8: Protect locations before you publish maps and data

For why coordinates are identifying information and how to aggregate and share in tiers, see [Field overview: Location privacy](../README.md#location-privacy-coordinates-are-identifying-information). Below are additional practices for geocoded data, based mainly on a 2014 review by Zandbergen written with public health data in mind:

- **Assume every point can be traced back to an address.** If you publish coordinates or point maps, anyone can match the points back to addresses (reverse geocoding)[^zandbergen2014ensuring-e3]. In one study cited by Zandbergen, manual comparison in a geographic information system (GIS) alone correctly identified 79% of the addresses on a hypothetical map of patient addresses[^zandbergen2014ensuring-e4].
- **Weigh aggregation against masking.** Aggregating to coarser units is simplest, but after aggregation, methods such as point pattern analysis and cluster detection lose much of their power or become impossible[^zandbergen2014ensuring-e5]. The alternative is **geographic masking (geomasking)**: altering the coordinates of points before release[^zandbergen2014ensuring-e6]. According to this review, there is no general standard for how far to displace points, but it is widely agreed that the sparser the population, the farther they need to move[^zandbergen2014ensuring-e7]; one study it cites found that the more the data were perturbed, the less accurate the analytical results[^zandbergen2014ensuring-e8].
- **Explain your choice and report the parameters.** The 2026 ethical guidelines on geoprivacy by Malekzadeh and colleagues (advisory) point out that there is no universal privacy-protection method for geographic data, so researchers should explain why they chose the one they did[^malekzadeh2026ethical-e12]; these techniques can also distort spatial patterns or exclude vulnerable groups from the analysis[^malekzadeh2026ethical-e13]. State in your paper which masking method and parameters you used; Zandbergen found that some studies did not even name the method[^zandbergen2014ensuring-e9].
- **Watch out for online basemaps.** Platforms that use third-party basemap plugins often send location information to external servers[^malekzadeh2026ethical-e14]; when handling sensitive coordinates, use local basemaps or an environment inside your institution `[Our analysis]`.

### Step 9: Make the whole analysis rerunnable

For why reproducibility matters and what one assessment of conference papers found, see [Field overview: Reproducibility and replicability](../README.md#reproducibility-and-replicability). Below are the concrete recommendations Nüst and Pebesma gave geography and the geosciences in 2021:

- **Use scripts, not clicks.** A script-based workflow is one that runs all the way from raw data to the published figures without any manual steps[^nust2021practical-e1]. They point out that mainstream GIS software is point-and-click, closed-source, or both; either use tools that record your steps, or switch to open tools[^nust2021practical-e8].
- **Draw maps in code too.** Manually tweaking how a map looks should not come at the cost of reproducibility[^nust2021practical-e6].
- **Record every parameter.** Put the coordinate reference system, units, weights matrix, class breaks, number of permutations, and random seed in your scripts and your methods section `[Our analysis]`; pin package versions in a configuration file[^nust2021practical-e2].
- **Use open formats and add a license**[^nust2021practical-e3].
- **When the data cannot be made public**, release the code along with a simulated dataset that preserves the spatial structure of the original data (such as spatial autocorrelation)[^kedron2021reproducibility-e9]; fabricated data prevent identification of individuals while still demonstrating the method[^nust2021practical-e10].
- **Studies that map with participants are no exception.** Maps are often used to interact with participants during data collection and to communicate results, so data collection and mapmaking should be reproducible too[^nust2021practical-e9].

For general practice in organizing data and code, see [Organizing research materials](../../../08_throughout/organizing_materials.md#3-every-result-must-be-traceable-to-how-it-was-produced) in Throughout the project.

### Step 10: Reporting

At a minimum, the methods section should state: data sources and years; the coordinate reference system and projection; the geocoding match rate; the spatial units and scale and why you chose them[^kwan2012uncertain-e6]; the spatial weights matrix and the other settings you tried[^kedron2021reproducibility-e4]; the method used to test for spatial autocorrelation and the number of permutations; the models used; the privacy protection applied and its parameters; and how to obtain the code and data `[Our analysis]`. Maps need a legend, the classification method, a scale bar, and the data source `[Our analysis]`.

Our sources do not say whether spatial analysis has a widely accepted reporting guideline comparable to those for clinical trials; follow your target journal. For health-related spatial studies using routinely collected data such as registries or medical records, you can consult the reporting guidelines listed on the [Health sciences page](../../health-sciences/README.md#reporting-guidelines-a-few-more-on-top-of-the-clinical-medicine-page) `[Our analysis]`.

---

## 3. Checklist

**Must do**

- [ ] The spatial units and scale, and how they relate to the true geographic context, are stated[^kwan2012uncertain-e6]
- [ ] The coordinate reference system of every layer is known and consistent[^pebesma2023spatial-e1] `[Our analysis]`
- [ ] Totals are checked after aggregation and joins: no double counting, and no ratios summed as if they were totals[^pebesma2023spatial-e8][^pebesma2023spatial-e10]
- [ ] Residuals are checked for spatial autocorrelation before regression; where it exists, OLS confidence intervals are not used as they are[^rey2023geographic-e16][^rey2023geographic-e21]
- [ ] Significance is assessed with a permutation test, and the number of permutations and the random seed are reported[^anselin2020global-e3][^anselin2020global-e6]
- [ ] Published point maps and coordinates cannot be traced back to participants' homes[^zandbergen2014ensuring-e3]

**Better practice**

- [ ] The pre-analysis plan states the scale and the spatial weights matrices to be examined[^kedron2021reproducibility-e4]
- [ ] Results are reported for several units, scales, and weights matrices `[Our analysis]`
- [ ] Color schemes are perceptually uniform and avoid red-green of similar lightness[^crameri2020misuse-e7][^crameri2020misuse-e4]
- [ ] The whole workflow is scripted, with software versions pinned[^nust2021practical-e1][^nust2021practical-e2]
- [ ] Where the data cannot be made public, simulated data preserving the spatial structure are released[^kedron2021reproducibility-e9]

**Common reviewer criticisms that don't hold up**

- "The data are not public, so this cannot be published." Kedron and colleagues argue that geographic research that cannot share data for ethical reasons or because of restrictions from an industry partner should not be kept out of publication[^kedron2021reproducibility-e11]; simulated data and open code can make up for it[^kedron2021reproducibility-e9].

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Overlaying layers or computing distances without regard to the coordinate reference system | Latitude and longitude have no definite meaning without a datum[^pebesma2023spatial-e1]; projections distort area or distance[^pebesma2023spatial-e2] |
| Aggregating points or areas to new boundaries with "intersects" without checking the totals | The same record can be counted in several areas[^pebesma2023spatial-e8] |
| Summing a ratio such as population density by area | Ratios cannot be summed after splitting[^pebesma2023spatial-e10] |
| Declaring "obvious clustering" just from looking at the map | People often see patterns in randomness[^rey2023geographic-e13]; you need a statistical test |
| Using the software's default rainbow or red-green colors | Rainbow schemes unfairly highlight one range of values[^crameri2020misuse-e3]; many readers cannot read red-green of similar lightness[^crameri2020misuse-e4] |
| Using equal intervals for skewed data without saying so | You may get classes with almost no observations[^rey2023geographic-e6] |
| Relying on ordinary regression significance despite clear spatial autocorrelation | OLS gets the confidence intervals wrong[^rey2023geographic-e21] |
| Comparing p = 0.001 from 999 permutations with p = 0.01 from 99 to judge significance | Pseudo p-values depend on the number of permutations and cannot be compared directly[^anselin2020global-e3] |
| Trying many weights matrices and reporting only the best | The other tests disappear from the literature[^kedron2021reproducibility-e3] |
| Publishing a point map of participants' homes, assuming it is safe because no addresses are shown | The points can be reverse geocoded back to addresses[^zandbergen2014ensuring-e4][^kwan2012uncertain-e9] |
| Applying geomasking without reporting the method and parameters | Readers cannot judge the tradeoff between privacy protection and analytical accuracy[^zandbergen2014ensuring-e9][^malekzadeh2026ethical-e12] |
| Clicking through the analysis in a graphical interface, then touching up the maps by hand | Neither others nor your future self can rerun it[^nust2021practical-e1][^nust2021practical-e6] |

---

## 5. Further reading

- **Rey, Arribas-Bel, and Wolf, Geographic Data Science with Python** (free online textbook, examples in Python): has a chapter each on spatial weights, choropleth mapping, global spatial autocorrelation, and spatial regression. Read it while working on Steps 5–7.
- **Pebesma and Bivand, Spatial Data Science: With Applications in R** (free online textbook, examples in R): Chapter 2 covers coordinates and coordinate reference systems; Chapter 5 covers whether attributes belong to points or areas, and spatial aggregation. Read it before Steps 3 and 4.
- **Anselin, the Global Spatial Autocorrelation chapter of the GeoDa workbook** (free online software tutorial): demonstrates the Moran scatter plot and permutation tests in GeoDa, a graphical-interface program; good for a first encounter with spatial autocorrelation.
- **Crameri et al. 2020, The misuse of colour in science communication** (*Nature Communications*, open access): the authors' view of how color is misused in scientific figures, and which scientific color maps are available. Read it before you draw your first map.
- **Zandbergen 2014, Ensuring Confidentiality of Geocoded Health Data** (open access): written with public health data in mind; covers the risks of reverse geocoding and the various geomasking methods. Read it before you publish point data.
- **Nüst and Pebesma 2021, Practical Reproducibility in Geography and Geosciences** (author-accepted manuscript on EarthArXiv, free): reproducibility practices for scripted workflows, software environments, online services, and sensitive data.
- **Kedron et al. 2021** and **Kwan 2012 and 2018**: why spatial settings need to be planned in advance, and how to report spatial units. See the [geography field overview](../README.md#further-reading) for details.

[^zandbergen2014ensuring-e1]: Zandbergen 2014, §2. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e1)
[^zandbergen2014ensuring-e2]: Zandbergen 2014, §2. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e2)
[^zandbergen2014ensuring-e3]: Zandbergen 2014, §3. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e3)
[^zandbergen2014ensuring-e4]: Zandbergen 2014, §3. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e4)
[^zandbergen2014ensuring-e5]: Zandbergen 2014, §5. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e5)
[^zandbergen2014ensuring-e6]: Zandbergen 2014, §6. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e6)
[^zandbergen2014ensuring-e7]: Zandbergen 2014, §7. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e7)
[^zandbergen2014ensuring-e8]: Zandbergen 2014, §10. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e8)
[^zandbergen2014ensuring-e9]: Zandbergen 2014, §7. [Evidence](../../../../sources/notes/zandbergen2014ensuring.md#e9)
[^nust2021practical-e1]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Creating reproducible workflows. [Evidence](../../../../sources/notes/nust2021practical.md#e1)
[^nust2021practical-e2]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Creating reproducible workflows. [Evidence](../../../../sources/notes/nust2021practical.md#e2)
[^nust2021practical-e3]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Creating reproducible workflows. [Evidence](../../../../sources/notes/nust2021practical.md#e3)
[^nust2021practical-e4]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Examples. [Evidence](../../../../sources/notes/nust2021practical.md#e4)
[^nust2021practical-e5]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Examples. [Evidence](../../../../sources/notes/nust2021practical.md#e5)
[^nust2021practical-e6]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Challenges. [Evidence](../../../../sources/notes/nust2021practical.md#e6)
[^nust2021practical-e7]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Challenges. [Evidence](../../../../sources/notes/nust2021practical.md#e7)
[^nust2021practical-e8]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Challenges. [Evidence](../../../../sources/notes/nust2021practical.md#e8)
[^nust2021practical-e9]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Challenges. [Evidence](../../../../sources/notes/nust2021practical.md#e9)
[^nust2021practical-e10]: Nüst & Pebesma 2021 (author accepted manuscript on EarthArXiv), Challenges. [Evidence](../../../../sources/notes/nust2021practical.md#e10)
[^kwan2018limits-e1]: Kwan 2018, p. 1486. [Evidence](../../../../sources/notes/kwan2018limits.md#e1)
[^kwan2018limits-e2]: Kwan 2018, p. 1486. [Evidence](../../../../sources/notes/kwan2018limits.md#e2)
[^kwan2012uncertain-e4]: Kwan 2012, p. 959. [Evidence](../../../../sources/notes/kwan2012uncertain.md#e4)
[^kwan2012uncertain-e6]: Kwan 2012, p. 963. [Evidence](../../../../sources/notes/kwan2012uncertain.md#e6)
[^kwan2012uncertain-e7]: Kwan 2012, pp. 963–964. [Evidence](../../../../sources/notes/kwan2012uncertain.md#e7)
[^kwan2012uncertain-e9]: Kwan 2012, p. 966, note 2. [Evidence](../../../../sources/notes/kwan2012uncertain.md#e9)
[^kedron2021reproducibility-e4]: Kedron et al. 2021, §3.1. [Evidence](../../../../sources/notes/kedron2021reproducibility.md#e4)
[^kedron2021reproducibility-e3]: Kedron et al. 2021, §2. [Evidence](../../../../sources/notes/kedron2021reproducibility.md#e3)
[^kedron2021reproducibility-e13]: Kedron et al. 2021, §4.2. [Evidence](../../../../sources/notes/kedron2021reproducibility.md#e13)
[^kedron2021reproducibility-e9]: Kedron et al. 2021, §3.2. [Evidence](../../../../sources/notes/kedron2021reproducibility.md#e9)
[^kedron2021reproducibility-e11]: Kedron et al. 2021, §3.2. [Evidence](../../../../sources/notes/kedron2021reproducibility.md#e11)
[^rey2023geographic-e1]: Rey et al. 2023 (online textbook), Spatial Weights. [Evidence](../../../../sources/notes/rey2023geographic.md#e1)
[^rey2023geographic-e2]: Rey et al. 2023 (online textbook), Spatial Weights. [Evidence](../../../../sources/notes/rey2023geographic.md#e2)
[^rey2023geographic-e3]: Rey et al. 2023 (online textbook), Spatial Weights. [Evidence](../../../../sources/notes/rey2023geographic.md#e3)
[^rey2023geographic-e4]: Rey et al. 2023 (online textbook), Spatial Weights. [Evidence](../../../../sources/notes/rey2023geographic.md#e4)
[^rey2023geographic-e5]: Rey et al. 2023 (online textbook), Choropleth Mapping. [Evidence](../../../../sources/notes/rey2023geographic.md#e5)
[^rey2023geographic-e6]: Rey et al. 2023 (online textbook), Choropleth Mapping. [Evidence](../../../../sources/notes/rey2023geographic.md#e6)
[^rey2023geographic-e7]: Rey et al. 2023 (online textbook), Choropleth Mapping. [Evidence](../../../../sources/notes/rey2023geographic.md#e7)
[^rey2023geographic-e8]: Rey et al. 2023 (online textbook), Choropleth Mapping. [Evidence](../../../../sources/notes/rey2023geographic.md#e8)
[^rey2023geographic-e9]: Rey et al. 2023 (online textbook), Choropleth Mapping. [Evidence](../../../../sources/notes/rey2023geographic.md#e9)
[^rey2023geographic-e10]: Rey et al. 2023 (online textbook), Choropleth Mapping. [Evidence](../../../../sources/notes/rey2023geographic.md#e10)
[^rey2023geographic-e11]: Rey et al. 2023 (online textbook), Global Spatial Autocorrelation. [Evidence](../../../../sources/notes/rey2023geographic.md#e11)
[^rey2023geographic-e12]: Rey et al. 2023 (online textbook), Global Spatial Autocorrelation. [Evidence](../../../../sources/notes/rey2023geographic.md#e12)
[^rey2023geographic-e13]: Rey et al. 2023 (online textbook), Global Spatial Autocorrelation. [Evidence](../../../../sources/notes/rey2023geographic.md#e13)
[^rey2023geographic-e14]: Rey et al. 2023 (online textbook), Global Spatial Autocorrelation. [Evidence](../../../../sources/notes/rey2023geographic.md#e14)
[^rey2023geographic-e15]: Rey et al. 2023 (online textbook), Global Spatial Autocorrelation. [Evidence](../../../../sources/notes/rey2023geographic.md#e15)
[^rey2023geographic-e16]: Rey et al. 2023 (online textbook), Spatial Regression. [Evidence](../../../../sources/notes/rey2023geographic.md#e16)
[^rey2023geographic-e17]: Rey et al. 2023 (online textbook), Spatial Regression. [Evidence](../../../../sources/notes/rey2023geographic.md#e17)
[^rey2023geographic-e18]: Rey et al. 2023 (online textbook), Spatial Regression. [Evidence](../../../../sources/notes/rey2023geographic.md#e18)
[^rey2023geographic-e19]: Rey et al. 2023 (online textbook), Spatial Regression. [Evidence](../../../../sources/notes/rey2023geographic.md#e19)
[^rey2023geographic-e20]: Rey et al. 2023 (online textbook), Spatial Regression. [Evidence](../../../../sources/notes/rey2023geographic.md#e20)
[^rey2023geographic-e21]: Rey et al. 2023 (online textbook), Spatial Regression, exercises. [Evidence](../../../../sources/notes/rey2023geographic.md#e21)
[^pebesma2023spatial-e1]: Pebesma & Bivand 2023 (online textbook), Chapter 2. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e1)
[^pebesma2023spatial-e2]: Pebesma & Bivand 2023 (online textbook), Chapter 2. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e2)
[^pebesma2023spatial-e3]: Pebesma & Bivand 2023 (online textbook), Chapter 2. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e3)
[^pebesma2023spatial-e4]: Pebesma & Bivand 2023 (online textbook), Chapter 2. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e4)
[^pebesma2023spatial-e5]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e5)
[^pebesma2023spatial-e6]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e6)
[^pebesma2023spatial-e7]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e7)
[^pebesma2023spatial-e8]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e8)
[^pebesma2023spatial-e9]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e9)
[^pebesma2023spatial-e10]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e10)
[^pebesma2023spatial-e11]: Pebesma & Bivand 2023 (online textbook), Chapter 5. [Evidence](../../../../sources/notes/pebesma2023spatial.md#e11)
[^crameri2020misuse-e2]: Crameri et al. 2020, Introduction. [Evidence](../../../../sources/notes/crameri2020misuse.md#e2)
[^crameri2020misuse-e3]: Crameri et al. 2020, Introduction. [Evidence](../../../../sources/notes/crameri2020misuse.md#e3)
[^crameri2020misuse-e4]: Crameri et al. 2020, Introduction. [Evidence](../../../../sources/notes/crameri2020misuse.md#e4)
[^crameri2020misuse-e5]: Crameri et al. 2020, Introduction. [Evidence](../../../../sources/notes/crameri2020misuse.md#e5)
[^crameri2020misuse-e6]: Crameri et al. 2020, Box 2. [Evidence](../../../../sources/notes/crameri2020misuse.md#e6)
[^crameri2020misuse-e7]: Crameri et al. 2020, main text. [Evidence](../../../../sources/notes/crameri2020misuse.md#e7)
[^anselin2020global-e1]: Anselin 2020 (GeoDa workbook), Moran's I. [Evidence](../../../../sources/notes/anselin2020global.md#e1)
[^anselin2020global-e2]: Anselin 2020 (GeoDa workbook), Permutation inference. [Evidence](../../../../sources/notes/anselin2020global.md#e2)
[^anselin2020global-e3]: Anselin 2020 (GeoDa workbook), Permutation inference. [Evidence](../../../../sources/notes/anselin2020global.md#e3)
[^anselin2020global-e4]: Anselin 2020 (GeoDa workbook), Interpretation. [Evidence](../../../../sources/notes/anselin2020global.md#e4)
[^anselin2020global-e5]: Anselin 2020 (GeoDa workbook), Inference. [Evidence](../../../../sources/notes/anselin2020global.md#e5)
[^anselin2020global-e6]: Anselin 2020 (GeoDa workbook), Inference. [Evidence](../../../../sources/notes/anselin2020global.md#e6)
[^anselin2020global-e7]: Anselin 2020 (GeoDa workbook), Moran scatter plot as a standard scatter plot. [Evidence](../../../../sources/notes/anselin2020global.md#e7)
[^anselin2020global-e8]: Anselin 2020 (GeoDa workbook), Interpretation. [Evidence](../../../../sources/notes/anselin2020global.md#e8)
[^malekzadeh2026ethical-e12]: Malekzadeh et al. 2026, Q27. [Evidence](../../../../sources/notes/malekzadeh2026ethical.md#e12)
[^malekzadeh2026ethical-e13]: Malekzadeh et al. 2026, Q26. [Evidence](../../../../sources/notes/malekzadeh2026ethical.md#e13)
[^malekzadeh2026ethical-e14]: Malekzadeh et al. 2026, Q11. [Evidence](../../../../sources/notes/malekzadeh2026ethical.md#e14)
