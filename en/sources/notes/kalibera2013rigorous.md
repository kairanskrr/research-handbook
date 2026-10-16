# Kalibera & Jones 2013: Rigorous Benchmarking in Reasonable Time

- Source: `kalibera2013rigorous`, [original (University of Kent repository)](https://kar.kent.ac.uk/33611/)
- Version: ISMM 2013, Author's Accepted Manuscript.

### E1

- Location: §1 Introduction
- Quote: "71 failed to provide any measure of variation (such as variance or a confidence interval) for their results."
- Key point: Of 90 papers in leading 2011 programming language and systems conferences and journals that used execution time as a main metric, 71 gave no measure of variation (such as variance or a confidence interval).

### E2

- Location: §1 Introduction
- Quote: "Advances in performance in our field are often small (Mytkowicz et al [20] report a median of 10%) and so can fall within the bounds of measurement error."
- Key point: Performance gains in this field are often small (a median of about 10%) and can fall within the bounds of measurement error.

### E3

- Location: §2 Related Work
- Quote: "Mytkowicz et al [20] found a number of sources of significant measurement bias, i.e. a systematic error in the measurement of systems that might favour one system over another. These included the Unix environment size and the link order"
- Key point: Summarizing Mytkowicz et al.: there are sources of significant measurement bias, i.e., systematic errors that may favor one system over another, including the Unix environment size and the link order.

### E4

- Location: §2 Related Work
- Quote: "However, our experimental methodology made it feasible to consider SPEC's full `reference' sizes, where we found that, although there was variation, it was very small"
- Key point: The authors repeated the experiments and confirmed the effect of link order with small training inputs; with SPEC's full reference-size inputs, the variation was very small.

### E5

- Location: §3 The Challenge of Reasonable Repetition
- Quote: "Uncontrolled variables happen to be fixed for most or all of an experiment, but are beyond our control. If these impact the results, they cause bias and mislead." / "For example, randomising link order turns an uncontrolled variable into a random one."
- Key point: Uncontrolled variables happen to stay fixed during an experiment but are beyond your control, causing bias; the experimenter's first task is to turn them into controlled or random variables, for example by randomizing link order.

### E6

- Location: §3 The Challenge of Reasonable Repetition
- Quote: "At the very least, repetition must be done at the highest level that has random variation to avoid bias"
- Key point: Variation can arise at several levels (compilation, each execution, each iteration); at the very least, repeat at the highest level that has random variation to avoid bias.

### E7

- Location: §4 The Challenge of Summarising Results
- Quote: "statistical significance methods confuse sample size and practical relevance"
- Key point: Computer experiments easily produce huge samples, and with a large enough sample any tiny difference becomes "statistically significant"; significance testing confuses sample size with practical relevance.

### E8

- Location: §4 The Challenge of Summarising Results
- Quote: "Such a statement is more natural than those derived from significance testing and less open to misinterpretation: it quantifies the size of the change, gives its error bound and indicates how certain this result is." / "RECOMMENDATION: Analysis of results should be statistically rigorous and in particular should quantify any variation. Report performance changes with effect size confidence intervals."
- Key point: Report performance changes as confidence intervals for the effect size, e.g., "we are 95% confident that A is 5.5% ± 2.5% faster than B": this gives the size of the change, its error bound, and how certain it is, and is less open to misinterpretation than significance testing.

### E9

- Location: §1 Introduction
- Quote: "Even if reported speedups are relatively large, a rigorous study should estimate the measurement error."
- Key point: Even when reported speedups are relatively large, a rigorous study should estimate the measurement error.

### E10

- Location: §5 Benchmarks and Platforms
- Quote: "We disable all system services that might interfere with measurements."
- Key point: The authors disabled all system services on the experimental platform that might interfere with measurements.
