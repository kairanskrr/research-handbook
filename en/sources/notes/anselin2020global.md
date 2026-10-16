# Anselin 2020: Global Spatial Autocorrelation (1) (GeoDa tutorial)

- Source: `anselin2020global`, [online GeoDa workbook](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html)
- Version: free online tutorial for the GeoDa software from the Center for Spatial Data Science at the University of Chicago, by Luc Anselin (one of the originators of spatial econometrics methods and of local indicators of spatial association), revised October 9, 2020. Locations give section names.

### E1

- Location: The Moran Scatter Plot > Moran's I
- Quote: "Moran's I statistic is arguably the most commonly used indicator of global spatial autocorrelation." / "In essence, it is a cross-product statistic between a variable and its spatial lag, with the variable expressed in deviations from its mean."
- Key point: Moran's I is arguably the most commonly used indicator of global spatial autocorrelation; in essence, it is a cross-product statistic between a variable (in deviations from its mean) and its spatial lag.

### E2

- Location: The Moran Scatter Plot > Permutation inference
- Quote: "This calculates a reference distribution for the statistic under the null hypothesis of spatial randomness by randomly permuting the observed values over the locations."
- Key point: The permutation test: randomly reassign the observed values to locations, recompute the statistic many times, and obtain a reference distribution under spatial randomness.

### E3

- Location: The Moran Scatter Plot > Permutation inference
- Quote: "More precisely, a result that has a p-value of 0.01 with 99 permutations is not necessarily more significant than a result with a p-value of 0.001 with 999 permutations."
- Key point: The size of the pseudo p-value is partly determined by the number of permutations; 0.01 with 99 permutations is not necessarily more significant than 0.001 with 999.

### E4

- Location: Interpretation > the four quadrants of the Moran scatter plot
- Quote: "it is important to keep in mind that the classification as such does not imply significance."
- Key point: The Moran scatter plot classifies observations into four types such as "high-high" and "low-low," but the classification itself does not imply significance.

### E5

- Location: Inference section
- Quote: "we select 999 Permutations, which is typically sufficient for reliable inference."
- Key point: 999 permutations are typically sufficient for reliable inference.

### E6

- Location: Inference section
- Quote: "In order to facilitate replication, the default setting in GeoDa is to use a specified seed for the random number generator." / "Using the same random seed ensures reproducibility on a particular machine. However, due to the way the random number generator is implemented, there may be differences depending on the hardware, specifically when a different number of CPU cores is used."
- Key point: To facilitate replication, GeoDa uses a fixed random seed by default; but even with the same seed, results can differ on different hardware (for example, a different number of CPU cores).

### E7

- Location: section Moran scatter plot as a standard scatter plot
- Quote: "The usual standard errors and t-statistics provided in the scatter plot are not appropriate in the spatial case."
- Key point: The usual standard errors and t-statistics shown in a scatter plot are not appropriate in the spatial case.

### E8

- Location: Interpretation section
- Quote: "We can see that the shape of the point cloud is influenced by the presence of several outliers on the high end"
- Key point: In the example, several high-end outliers influence the shape of the Moran scatter plot (the author then notes that they pull the slope down).
