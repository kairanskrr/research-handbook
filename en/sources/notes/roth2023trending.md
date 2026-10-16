# Roth, Sant'Anna, Bilinski & Poe 2023: What's Trending in Difference-in-Differences?

- Source: `roth2023trending`, [arXiv 2201.01194](https://arxiv.org/abs/2201.01194); published version in Journal of Econometrics 235(2), 2023
- Version: arXiv v3 (January 9, 2023). Excerpts follow the arXiv version; locations give section titles.

### E1

- Location: §1 Introduction
- Quote: "The key identifying assumption is that the average outcome among the treated and comparison populations would have followed "parallel trends" in the absence of treatment. We also assume that the treatment has no causal effect before its implementation (no anticipation)."
- Key point: The two key assumptions of standard difference-in-differences: without treatment, the treated and comparison groups' average outcomes would have followed parallel trends; and treatment has no effect before it is implemented (no anticipation).

### E2

- Location: §2.3 The Parallel Trends Assumption and Identification
- Quote: "In other words, parallel trends allows for the presence of selection bias, but the bias from selecting into treatment must be the same in period t = 1 as it is in period t = 2."
- Key point: Parallel trends allows the groups to start at different levels (selection bias), but that bias must be the same size in both periods.

### E3

- Location: §1 Introduction
- Quote: "In short, TWFE regressions make both "clean" comparisons between treated and not-yet-treated units as well as "forbidden" comparisons between units who are both already-treated. When treatment effects are heterogeneous, these "forbidden" comparisons potentially lead to severe drawbacks such as TWFE coefficients having the opposite sign of all individual-level treatment effects due to "negative weighting" problems."
- Key point: When units are treated at different times, a conventional two-way fixed effects (TWFE) regression uses already-treated units as controls, which the authors call "forbidden" comparisons; with heterogeneous treatment effects, the coefficient can even have the opposite sign of every individual effect.

### E4

- Location: §3.5 Recommendations
- Quote: "Nevertheless, it is our practical experience that the various heterogeneity-robust DiD estimators typically (although not always) produce similar answers. The first-order consideration is therefore to use an approach that makes clear what the target parameter is and which groups are being compared for identification."
- Key point: The new heterogeneity-robust estimators usually (though not always) give similar answers; the first-order concern is to use a method that is clear about what is being estimated and which comparisons are made.

### E5

- Location: §1 Introduction
- Quote: "First, the absence of a significant pre-trend does not necessarily imply that parallel trends holds; in fact, these tests often have low power. Second, conditioning the analysis on the result of a pre-test can introduce additional statistical distortions from a selection effect known as pre-test bias."
- Key point: A non-significant pre-trend test does not mean parallel trends hold, since these tests often have low power; and conditioning the analysis on a pre-test result can introduce additional bias.

### E6

- Location: §4.6 Recommendations
- Quote: "we encourage researchers to continue to plot "event-study plots" that allow for a visual evaluation of pre-existing trends." / "We also think it should become standard practice for researchers to formally assess the extent to which their conclusions are sensitive to violations of parallel trends."
- Key point: The authors encourage continuing to plot event-study plots to check pre-existing trends visually, and argue that formally assessing how sensitive conclusions are to violations of parallel trends should become standard practice.

### E7

- Location: §4.6 Recommendations
- Quote: "how big would the post-treatment violation of parallel trends have to be relative to the largest pre-treatment violation to invalidate a particular conclusion?"
- Key point: One reportable sensitivity measure: how many times larger than the largest pre-treatment violation the post-treatment violation of parallel trends would have to be to overturn the conclusion.

### E8

- Location: Table 1: A Checklist for DiD Practitioners
- Quote: "A good rule of thumb is to cluster at the level at which treatment is independently assigned (e.g. at the state level when policy is determined at the state level)" / "If you have a small number of treated clusters, consider using one of the alternative inference methods described in Section 5.1."
- Key point: Rule of thumb: cluster standard errors at the level where treatment is independently assigned (cluster by state if policy is set by state); with few treated clusters, consider other inference methods.

### E9

- Location: §1 Introduction
- Quote: "Standard cluster-robust methods assume that there is a large number of both treated and untreated clusters, and thus can perform poorly in this case."
- Key point: Standard cluster-robust methods assume many treated and many untreated clusters, and can perform poorly when there are few treated clusters.

### E10

- Location: §5.2 Recommendations
- Quote: "If it is difficult to conceptualize a super-population, fear not! Your DiD analysis can likely still be sensible from a finite-population perspective where we think of the treatment assignment as stochastic."
- Key point: If you cannot imagine a larger population the data were drawn from (for example, the sample is all 50 states), fear not: treating the uncertainty as coming from random treatment assignment usually still makes the analysis sensible.

### E11

- Location: §7 Conclusion
- Quote: "Some key themes are that researchers should be clear about the comparison group used for identification, match the estimation and inference methods to the identifying assumptions, and explore robustness to possible violations of those assumptions." / "We emphasize that context-specific knowledge will often be needed to choose the right identifying assumptions and accompanying methods."
- Key point: Three themes: be clear about the comparison group used for identification; match estimation and inference methods to the identifying assumptions; and check robustness to violations of those assumptions. Choosing the right assumptions and methods often requires knowledge of the specific context.

### E12

- Location: §4.3 Testing for pre-existing trends
- Quote: "We caution, however, against using dynamic TWFE specifications like (16) in settings with staggered adoption"
- Key point: With staggered treatment timing, the authors caution against using conventional dynamic TWFE regressions to produce event-study plots.

### E13

- Location: §1 Introduction
- Quote: "Table 1, which contains a checklist for a practitioner implementing a DiD analysis, and Table 2, which lists R and Stata packages for implementing many of the methods described in this paper."
- Key point: Table 1 in the paper is a checklist for practitioners doing difference-in-differences, and Table 2 lists R and Stata packages implementing most of the methods discussed.
