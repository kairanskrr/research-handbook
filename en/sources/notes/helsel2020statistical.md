# Helsel et al. 2020: Statistical Methods in Water Resources

- Source: `helsel2020statistical`, [Original PDF](https://pubs.usgs.gov/tm/04/a03/tm4a3.pdf)
- Version: United States Geological Survey (USGS) Techniques and Methods, book 4, chapter A3, 2020 edition (superseding the 2002 edition). A US government publication, free to read. Locations are given as PDF page numbers (counting from the cover).

### E1

- Location: §1.1 Characteristics of Water Resources Data, PDF p. 26
- Quote: "Data reported only as below or above some threshold. In statistics these are known as censored data. Examples include concentrations of a chemical or particles that are reported as being below a laboratory reporting limit"
- Key point: Data reported only as below or above some threshold are called censored data in statistics, for example concentrations reported as below a laboratory reporting limit.

### E2

- Location: §5.5 Two-group Tests for Data with Nondetects, PDF p. 210
- Quote: "The two-sample t-test, after substituting one-half the reporting limit for nondetects, has unfortunately been a common procedure in water resources for testing differences between groups. This procedure may not find differences between groups that are there or may find differences that are not there"
- Key point: Substituting one-half the reporting limit for nondetects and then running a t-test has been common in water resources, but it may miss differences that exist or find differences that do not.

### E3

- Location: §5.5 Two-group Tests for Data with Nondetects, PDF p. 210
- Quote: "Even with recensoring, this is a better procedure than using the t-test after substitution, as it avoids the consequences of falsely stating that the exact value for each nondetect is known."
- Key point: A rank-sum procedure is better because it does not pretend to know the exact value of each nondetect.

### E4

- Location: §5.3.5, PDF p. 200
- Quote: "If the question is whether one group shows higher values than another, all data below the highest reporting limit can be assigned a tied rank and the rank-sum test computed, without making any distributional assumptions or assigning arbitrary values to the data"
- Key point: To test whether one group has higher values than another, you can assign all data below the highest reporting limit a tied rank and compute the rank-sum test, with no distributional assumptions and no made-up values.

### E5

- Location: §12.7 Applicability of Trend Tests with Censored Data, PDF p. 637
- Quote: "Substitution of an arbitrarily chosen value below the reporting limit for all censored values will give biased estimates of the trend slope. Although the amount of bias cannot be stated precisely, the presence of only a few less-than values in a record (less than about five percent) is not likely to affect the accuracy of the trend slope magnitude substantially"
- Key point: Substituting an arbitrary value for all censored values biases the estimated trend slope, though with only a few less-than values (under about 5%) the effect is unlikely to be large.

### E6

- Location: Note in the example in §15.3, PDF p. 752
- Quote: "a reporting limit is a concentration value below which the laboratory lacks confidence to state a specific concentration value"
- Key point: A reporting limit is the concentration below which the laboratory lacks confidence to state a specific value.

### E7

- Location: §1.1 Characteristics of Water Resources Data, item 7, Autocorrelation
- Quote: "One of the consequences of autocorrelation is that the accuracy of any statistical estimates will be overstated if this property is ignored. For example, 100 observations of a random variable should provide a fairly accurate estimate of the population mean, but if the samples collected were spaced very close in time and the serial correlation was strong, the accuracy of the estimate of the population mean may be no better than what could be derived from a set of only 10 uncorrelated observations from that population."
- Key point: Ignoring autocorrelation overstates the accuracy of statistical estimates. Example: 100 observations should estimate the mean fairly accurately, but if samples were closely spaced in time with strong serial correlation, the accuracy may be no better than that of 10 independent observations.

### E8

- Location: §1.1, item 7, Autocorrelation
- Quote: "In the case of spatial data (for example, water levels or chemical concentrations in a set of wells) the term "nearby" indicates geographic proximity. This is the tendency for high values to be near other high values and low values to be near other low values."
- Key point: In spatial data (for example, water levels or chemical concentrations in a set of wells), autocorrelation is the tendency for high values to be near other high values and low values near low values.

### E9

- Location: §9.4.2.4 Detection of Serial Correlation
- Quote: "If we considered a dataset of TDS concentrations and discharges collected at a daily interval for 20 years, we would have about 7,300 samples, but doing any of the computations for significance tests or confidence intervals using an n value of 7,300 would grossly overstate the true degree of certainty in our results."
- Key point: Example: daily sampling for 20 years gives about 7,300 total dissolved solids (TDS) concentrations and discharges; computing significance tests or confidence intervals with n = 7,300 would grossly overstate the true degree of certainty.

### E10

- Location: §9.4.2.4 Detection of Serial Correlation
- Quote: "It is often the case that what may appear to be serial correlation is actually an artifact of these time or trend components."
- Key point: What looks like serial correlation is often an artifact of time components such as season, time of day, or trend; check residuals against time with plots first.
