# J-PAL research resource: Randomization

- Source: `jpal2023randomization`, [original web page](https://www.povertyactionlab.org/resource/randomization)
- Version: J-PAL research resource page by Sarah Kopper and Anja Sautmann, updated September 2023; accessed October 2026. Locations give subheadings.

### E1

- Location: Choosing the unit of randomization
- Quote: "At a minimum, the unit of randomization should be the unit at which the treatment will be delivered, and ideally at a unit that minimizes spillovers (see below) as well as evaluation-driven effects"
- Key point: The unit of randomization should at minimum be the unit at which the treatment is delivered, and ideally one that minimizes spillovers and evaluation-driven effects.

### E2

- Location: Choosing the unit of randomization
- Quote: "In general, moving up in level of randomization decreases the study’s effective sample size, meaning that more observational units are required to achieve a given level of power."
- Key point: Randomizing at a higher level reduces the effective sample size, so more observational units are needed for the same power.

### E3

- Location: Randomization designs to estimate spillover effects
- Quote: "This is done by randomizing at the cluster level and varying the “intensity” of treatment for the cluster, that is, the share of observational units in the cluster that receive the treatment, and then measuring treatment effects on both treated and untreated units within the cluster."
- Key point: One design for measuring spillovers: randomize at the cluster level, vary the share of units in each cluster that receive treatment (treatment "intensity"), and measure effects on both treated and untreated units.

### E4

- Location: Stratified randomization
- Quote: "Stratification variables should thus be ones you expect to be correlated with the outcome of interest, or those for which you are interested in differential or heterogeneous treatment effects."
- Key point: Choose stratification variables that you expect to be correlated with the outcome, or for which you want to compare treatment effects across groups.

### E5

- Location: Randomization methods; Solutions/programming
- Quote: "Typically, this would be done in statistical software such as Stata or R to ensure the randomization is replicable." / "Set the seed for the random number generator"
- Key point: Randomization is usually done in statistical software so it is replicable; set the seed for the random number generator.

### E6

- Location: Balance tests
- Quote: "If you are testing for balance at the 5% level, you would expect to see statistically significant differences between the treatment and control groups in roughly 5% of your covariates simply by chance. Note, there is no clear rule for how many imbalanced variables is too many."
- Key point: When testing balance at the 5% level, you expect about 5% of covariates to differ significantly by chance alone; there is no clear rule for how many imbalanced variables are too many.

### E7

- Location: Balance tests
- Quote: "Balance tests may be most useful when there are reasons to doubt that the randomization was done correctly"
- Key point: Balance tests are most useful when there are reasons to doubt that the randomization was done correctly.

### E8

- Location: Solutions to imbalance
- Quote: "An alternative approach is to consider before implementing randomization whether there are covariates on which imbalance would not be acceptable and stratifying on them, so that balance on key covariates is achieved by construction (Athey & Imbens 2017)."
- Key point: Rather than re-randomizing after an imbalanced draw, decide in advance which covariates must not be imbalanced and stratify on them, so balance is achieved by construction.

### E9

- Location: Balance tests
- Quote: "Balance test regressions should use the same specification as your final regression when possible."
- Key point: Balance test regressions should use the same specification as the final regression where possible (e.g., including stratum fixed effects if randomization was stratified).
