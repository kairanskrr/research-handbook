# Piepho and Edmondson 2018: A tutorial on the statistical analysis of factorial experiments with qualitative and quantitative treatment factor levels

- Source: `piepho2018tutorial`, [original](https://doi.org/10.1111/jac.12267)
- Version: Journal of Agronomy and Crop Science 204: 429-455, 2018, CC BY open access. Text taken from the publisher PDF saved in the Internet Archive. A tutorial on factorial experiments and mixed-model analysis using field trial examples, with SAS and R code. Locations give sections.

### E1

- Location: 1 Introduction
- Quote: "All the experiments considered are comparative, meaning that the focus is exclusively on comparisons between treatments in the same experiment"
- Key point: All experiments discussed are comparative: the focus is only on comparisons between treatments within the same experiment.

### E2

- Location: 2.2.1 Block effects
- Quote: "Treatment factors are of direct interest and are usually modelled as fixed effects, but nuisance factors such as block effects can be modelled either as fixed or as random effects."
- Key point: Treatment factors are of direct interest and usually modeled as fixed effects; nuisance factors such as blocks can be modeled as fixed or random effects.

### E3

- Location: 2.2.1 Block effects
- Quote: "Fixed block effects models are robust against distributional assumptions and are useful for eliminating block differences in designs with large complete or near-complete blocks"
- Key point: Fixed block effects are robust to distributional assumptions and suit designs with large complete (or near-complete) blocks.

### E4

- Location: 2.2.1 Block effects
- Quote: "In general, however, incomplete block designs will confound substantial treatment information between blocks and then an analysis with recovery of inter-block information will be necessary. Fixed blocks are not useful for recovery of inter-block treatment information, but an assumption of random blocks will allow treatment information to be recovered by combining inter- and intra-block information"
- Key point: In incomplete block designs, substantial treatment information lies between blocks; fixed block effects cannot recover it, while random block effects combine inter-block and intra-block information.

### E5

- Location: Split-plot example (Example 2)
- Quote: "It is particularly important to explicitly fit the main-plot, sub-plot and sub-sub-plot error terms as random to properly represent the three-stage randomization layout and hence to obtain valid inferences for the fixed effects. Each treatment effect has its own specific error term, depending on the experimental units to which the levels of the relevant treatment factor were randomly allocated."
- Key point: In split-plot-type designs, fit the main-plot, sub-plot, and sub-sub-plot error terms explicitly as random effects; each treatment effect has its own error term, depending on which level of experimental unit that factor was randomized to.

### E6

- Location: Discussion
- Quote: "It is important to keep in mind that a data transformation affects several assumptions simultaneously."
- Key point: A data transformation affects several statistical assumptions at once.

### E7

- Location: 10 Discussion
- Quote: "Although the analysis of such designs is often based on a comparison of the treatment means using multiple comparisons tests, such comparisons take no account of the ordered structure of the observations and are totally inappropriate for structured treatment comparisons."
- Key point: When treatments are quantitative levels (e.g., several nitrogen rates), people often compare means pairwise with multiple comparison tests, but this ignores the ordered structure of the levels and is wholly inappropriate; use a regression model instead.

### E8

- Location: Discussion
- Quote: "Repeated-measures data are common in agronomic research but are frequently misinterpreted and analysed inappropriately."
- Key point: Repeated-measures data (several measurements on the same experimental unit) are common in agronomic research but are frequently misinterpreted and analyzed inappropriately.
