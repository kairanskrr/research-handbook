# Rey, Arribas-Bel & Wolf 2023: Geographic Data Science with Python

- Source: `rey2023geographic`, [free online edition](https://geographicdata.science/book/intro.html)
- Version: Textbook published by CRC Press in 2023; the authors make the full text freely available online. We read four chapters of the online edition: Spatial Weights, Choropleth Mapping, Global Spatial Autocorrelation, and Spatial Regression. The authors are spatial analysis scholars, and the examples use the Python PySAL library. Locations give chapter names.

### E1

- Location: Spatial Weights chapter, opening
- Quote: "By expressing the notion of geographical proximity or connectedness, spatial weights are the main mechanism through which the spatial relationships in geographical data is brought to bear in the subsequent analysis."
- Key point: Spatial weights express which units are near or connected to which, and are the main way spatial relationships enter the subsequent analysis.

### E2

- Location: Spatial Weights chapter, Contiguity weights section
- Quote: "If we wanted them to be considered as neighbours, we can switch to the more inclusive notion of Queen contiguity, which requires the pair of polygons to only share one or more vertices."
- Key point: Two areas that share only a vertex are not neighbors under Rook contiguity (which requires a shared edge) but are neighbors under Queen contiguity (one shared vertex is enough); a different definition gives different neighbors.

### E3

- Location: Spatial Weights chapter, Distance based weights section
- Quote: "in cases where the density of the observations varies over the study region, using the same threshold anywhere will result in regions with a high density of neighbors while others with observations very sparsely connected."
- Key point: When observation density varies across the study region, a single distance threshold everywhere gives some places many neighbors and others almost none.

### E4

- Location: Spatial Weights chapter, section on handling "islands"
- Quote: "Imagine one of our tracts was an island and did not have any neighbors in the contiguity case. This can create issues in the spatial analytics that build on spatial weights, so it is good practice to amend the matrix before using it."
- Key point: Units with no neighbors under the contiguity definition ("islands") cause problems for later analysis; amend the weights matrix before using it.

### E5

- Location: Choropleth Mapping chapter, Quantitative data classification section
- Quote: "The choice of the classification scheme should take into consideration the statistical distribution of the attribute values as well as the goal of our map (e.g., highlight outliers vs. accurately depict the distribution of values)."
- Key point: Choose a classification scheme by considering both the distribution of the data and the goal of the map (highlighting outliers vs. accurately depicting the distribution).

### E6

- Location: Choropleth Mapping chapter, Equal intervals section
- Quote: "However, this rule only considers the extreme values of the distribution and, in some cases, this can result in one or more classes being sparse."
- Key point: Equal intervals consider only the extreme values, so skewed data can produce classes with almost no observations.

### E7

- Location: Choropleth Mapping chapter, Quantiles section
- Quote: "While quantile classification avoids the pitfall of sparse classes, this classification is not problem-free. The varying widths of the intervals can be markedly different which can lead to problems of interpretation."
- Key point: Quantile classification avoids sparse classes, but class widths can differ greatly, which invites misreading.

### E8

- Location: Choropleth Mapping chapter, before the Color section
- Quote: "This can have major impacts on our brain's pattern recognition capabilities, as we tend to be drawn to the larger polygons, even though they might not be the most relevant ones for our analysis."
- Key point: When areas differ a lot in size and shape, the eye is drawn to the large polygons, even if they are not the most relevant for the analysis.

### E9

- Location: Choropleth Mapping chapter, Color section
- Quote: "The choice of a color scheme for a choropleth map should be based on the type of variable under consideration (Brewer et al. 1997). Generally, a distinction is drawn between three types of numerical attributes: sequential, diverging, and qualitative."
- Key point: Choose the color scheme by variable type: sequential, diverging, or qualitative (categorical).

### E10

- Location: Choropleth Mapping chapter, Sequential / Diverging / Qualitative palettes sections
- Quote: "Sequential color schemes are appropriate for continuous data where the origin is in one end of the series." / "This is useful with continuous data when one wishes to place equal emphasis on mid-range critical values as well as extremes at both ends of the distribution." / "Qualitative palettes encode categorical data."
- Key point: Sequential schemes suit continuous data whose origin is at one end; diverging schemes suit continuous data with a critical mid-range value where both extremes matter equally; qualitative schemes suit categorical data.

### E11

- Location: Global Spatial Autocorrelation chapter, opening
- Quote: "Spatial autocorrelation thus has to do with the degree to which the similarity in values between observations in a dataset is related to the similarity in locations of such observations."
- Key point: Spatial autocorrelation is the degree to which similarity in values between observations is related to similarity in their locations.

### E12

- Location: Global Spatial Autocorrelation chapter, opening
- Quote: "For example, think of the distribution of income, or poverty, over space: it is common to find similar values located nearby (wealthy areas close to other wealthy areas, poor population concentrated in space too)."
- Key point: Positive spatial autocorrelation is common in social phenomena: wealthy areas sit next to wealthy areas, and poor populations are spatially concentrated too.

### E13

- Location: Global Spatial Autocorrelation chapter, after the Brexit example
- Quote: "This extraordinary capability to spot trends, patterns and associations tends to also create many false positives: cases where we think there is a pattern, but in fact what we are seeing is largely random"
- Key point: People are very good at spotting patterns, and so often see patterns in randomness; judging spatial clustering just by looking at a map is unreliable.

### E14

- Location: Global Spatial Autocorrelation chapter, Moran's I section
- Quote: "In fact, there is a close connection between the two: the value of Moran's I corresponds with the slope of the linear fit overlayed on top of the Moran Plot."
- Key point: Moran's I equals the slope of the linear fit on the Moran plot (the variable on the x-axis, its spatial lag, i.e. the neighbors' average, on the y-axis).

### E15

- Location: Global Spatial Autocorrelation chapter, Moran's I section
- Quote: "A small enough p-value associated with the Moran's I of a map allows to reject the hypothesis that the map is random."
- Key point: Only a small enough p-value for Moran's I lets you reject the hypothesis that the map's pattern is random.

### E16

- Location: Spatial Regression chapter, Non-spatial regression section
- Quote: "But, our model might display some clustering in the errors, which may be a problem as that violates the i.i.d. assumption linear models usually come built-in with."
- Key point: If the errors of an ordinary linear regression cluster in space, that violates the i.i.d. (independent and identically distributed) error assumption linear models usually build in.

### E17

- Location: Spatial Regression chapter, introduction
- Quote: "They might also arise because there is some other feature whose omission causes the spatial patterns in the error we see; if this additional feature were included, the structure would disappear."
- Key point: A spatial pattern in the errors may come from an omitted variable that is itself spatially patterned; adding it to the model may make the pattern disappear.

### E18

- Location: Spatial Regression chapter, Spatial heterogeneity section
- Quote: "At its most basic, spatial heterogeneity means that parts of the model may vary systematically with geography, change in different places."
- Key point: Spatial heterogeneity means parts of the model vary systematically with geography, differing from place to place.

### E19

- Location: Spatial Regression chapter, Spatial error / Spatial lag sections
- Quote: "Although it appears similar, this specification violates the assumptions about the error term in a classical OLS model. Hence, alternative estimation methods are required." / "Although it might not seem very different from the previous equation, this model violates the exogeneity assumption, crucial for OLS to work."
- Key point: Both the spatial error model and the spatial lag model violate the assumptions of ordinary least squares (OLS) and need dedicated estimation methods.

### E20

- Location: Spatial Regression chapter, Spatial lag section
- Quote: "Similarly to the effects in the SLX regression, changes in the spatial lag regression need to be interpreted with care."
- Key point: Coefficients in a spatial lag model cannot be read directly as in ordinary regression and need careful interpretation (the authors suggest using prediction and scenario simulation to separate direct and indirect effects).

### E21

- Location: Spatial Regression chapter, Questions (exercises)
- Quote: "Fortunately for us, spatial error models recover the same estimates (asymptotically) as a typical OLS estimate, although their confidence intervals will change. Statistically, this occurs because OLS miscalculates when there is spatial correlation and/or spatial heteroskedasticity."
- Key point: With spatial correlation, OLS miscalculates confidence intervals; the spatial error model gives the same coefficient estimates (asymptotically), but different confidence intervals.
