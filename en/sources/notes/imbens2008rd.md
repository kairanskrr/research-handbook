# Imbens & Lemieux 2008: Regression Discontinuity Designs: A Guide to Practice

- Source: `imbens2008rd`, [NBER working paper PDF](https://www.nber.org/system/files/working_papers/w13039/w13039.pdf); published version in Journal of Econometrics 142(2), 2008
- Version: NBER Working Paper 13039 (April 2007). Excerpts follow the working paper; locations give section numbers. The PDF-to-text conversion lost the fi and ff ligatures, so only sentences without those letter combinations are quoted.

### E1

- Location: §8 Conclusion: A Summary Guide to Practice
- Quote: "Graph the data (Section 3) by computing the average value of the outcome variable over a set of bins."
- Key point: The first step is to graph the data: divide the forcing variable into bins and compute the average outcome in each bin.

### E2

- Location: §7 Specification Testing
- Quote: "For example, at age 65 individuals become eligible for discounts at many cultural institutions." [...] "The more plausible explanation is that there are other institutional changes"
- Key point: A hidden risk in regression discontinuity is that something else changes at the same cutoff. For example, many cultural institutions offer discounts at 65, but a jump in working hours at 65 is more plausibly due to other institutional changes that also happen at 65.

### E3

- Location: §7.1 Tests Involving Covariates
- Quote: "In most cases, the reason for the discontinuity in the probability of the treatment does not suggest a discontinuity in the average value of covariates."
- Key point: In most cases, the reason the probability of treatment jumps at the cutoff does not imply a jump in covariates (individual characteristics fixed beforehand), so covariates can be used as a test.

### E4

- Location: §7.2 Tests of Continuity of the Density
- Quote: "Even if such discontinuities are not conclusive evidence of violations of the RD assumptions, at the very least, inspecting this density would be useful to assess whether it exhibits unusual features that may shed light on the plausibility of the design."
- Key point: A jump in the density of the forcing variable at the cutoff is not conclusive evidence that the design fails, but inspecting the density at least reveals unusual features and helps judge whether the design is credible.

### E5

- Location: §7.3 Testing for Jumps at Non-discontinuity Points
- Quote: "A third set of tests involves estimating jumps at points where there should be no jumps."
- Key point: A third set of tests estimates jumps at points where there should be none (placebo cutoffs).

### E6

- Location: §7.5 Sensitivity to the Choice of Bandwidth
- Quote: "Irrespective of the manner in which the bandwidth is chosen, one should always investigate the sensitivity of the inferences to this choice, for example, by including results for bandwidths twice (or four times) and half (or a quarter of) the size of the originally chosen bandwidth." / "but if the results are critically dependent on a particular bandwidth choice, they are clearly less credible than if they are robust to such variation in bandwidths."
- Key point: However the bandwidth is chosen, always report how sensitive the results are to it, for example at twice (or four times) and half (or a quarter of) the bandwidth; a result that holds only at one bandwidth is far less credible.

### E7

- Location: §8 Conclusion: A Summary Guide to Practice
- Quote: "running linear regressions on both sides of the"
- Key point: To estimate the effect, run linear regressions on each side of the cutoff (within a given bandwidth).
