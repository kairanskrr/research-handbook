# Particle Data Group 2024: Review of Particle Physics, Introduction

- Source: `pdg2024intro`, [original](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-rpp-intro.pdf)
- Version: "Introduction" chapter of the 2024 Review of Particle Physics by the Particle Data Group (PDG) (version of May 31, 2024), free on the PDG website; the full review is published in Phys. Rev. D 110, 030001 (2024), open access. Locations give section numbers.

### E1

- Location: §5.2.2
- Quote: "To average data, we use a standard weighted least-squares procedure" / "We begin by assuming that measurements of a given quantity are uncorrelated" / "If χ2/(N - 1) is less than or equal to 1, and there are no known problems with the data, we accept the results."
- Key point: Assume first that measurements are uncorrelated, compute the weighted average, then compute χ² and use χ²/(N − 1) (N is the number of measurements) to check whether the measurements agree: if it is at most 1 and there are no known problems with the data, accept the result.

### E2

- Location: §5.2.2
- Quote: "The large value of the χ2 is likely to be due to underestimation of errors in at least one of the experiments. Not knowing which of the errors are underestimated, we assume they are all underestimated by the same factor S."
- Key point: A large χ² most likely means at least one experiment underestimated its errors; not knowing which, assume all errors are underestimated by the same factor S (the "scale factor") and enlarge the error on the average accordingly.

### E3

- Location: §5.3 Rounding
- Quote: "The basic rule states that if the three highest order digits of the error lie between 100 and 354, we round to two significant digits. If they lie between 355 and 949, we round to one significant digit."
- Key point: The Particle Data Group's rounding rule: if the three highest-order digits of the error are between 100 and 354, keep two significant digits; between 355 and 949, keep one.

### E4

- Location: §5.3
- Quote: "In all cases, the central value is given with a precision that matches that of the error." / "the result (coming from an average) 0.827 ± 0.119 would appear as 0.83 ± 0.12"
- Key point: Give the central value to the same precision as the error. Example: 0.827 ± 0.119 is written 0.83 ± 0.12.

### E5

- Location: §5.4 Discussion
- Quote: "it is difficult to develop a procedure that handles simultaneously in a reasonable way two basic types of situations: (a) data that lie apart from the main body of the data are incorrect (contain unreported errors); and (b) the opposite--it is the main body of data that is incorrect."
- Key point: It is hard to devise a procedure that handles both situations well: data lying apart from the rest are wrong, or, conversely, the main body of data is wrong.
