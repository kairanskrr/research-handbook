# Hoefler & Belli 2015: Scientific Benchmarking of Parallel Computing Systems

- Source: `hoefler2015scientific`, [original (author's homepage)](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf)
- Version: SC 2015 (the ACM/IEEE supercomputing conference), PDF posted on the author's homepage.
- Note: Surveys how 120 parallel computing papers at three top conferences report performance and proposes 12 rules. The examples come from parallel computing, but most rules apply to performance measurement in general.

### E1

- Location: §1 Introduction
- Quote: "We call an experiment interpretable if it provides enough information to allow scientists to understand the experiment, draw own conclusions, assess their certainty, and possibly generalize results."
- Key point: Proposes "interpretability": even if an experiment cannot be fully reproduced, it should give enough information for others to understand it, draw their own conclusions, and assess their certainty.

### E2

- Location: §2, Rule 1
- Quote: "When publishing parallel speedup, report if the base case is a single parallel process or best serial execution, as well as the absolute execution performance of the base case." / "A simple generalization of this rule implies that one should never report ratios without absolute values."
- Key point: When reporting speedup, state what the base case is and give its absolute performance; more generally, never report a ratio without the absolute values.

### E3

- Location: §2, Rule 2
- Quote: "Specify the reason for only reporting subsets of standard benchmarks or applications or not using all system resources." / "A corollary of this rule is to report all results, not just the best."
- Key point: Explain why you report only a subset of a standard benchmark; corollary: report all results, not just the best.

### E4

- Location: §3.1, Rule 3 and Rule 4
- Quote: "Use the arithmetic mean only for summarizing costs. Use the harmonic mean for summarizing rates." / "Avoid summarizing ratios; summarize the costs or rates that the ratios base on instead. Only if these are not available use the geometric mean for summarizing ratios."
- Key point: Use the arithmetic mean for costs (such as time) and the harmonic mean for rates; avoid summarizing ratios, and summarize the underlying costs or rates instead; use the geometric mean for ratios only when those are unavailable.

### E5

- Location: §3.1.2, Rule 5
- Quote: "Report if the measurement values are deterministic. For nondeterministic data, report confidence intervals of the measurement."
- Key point: Report whether the measurements are deterministic; for nondeterministic data, report confidence intervals.

### E6

- Location: §3.1.2, Rule 6
- Quote: "Do not assume normality of collected data (e.g., based on the number of samples) without diagnostic checking."
- Key point: Do not assume the data are normally distributed (e.g., because there are many samples) without diagnostic checking.

### E7

- Location: §3.2, Rule 7
- Quote: "Compare nondeterministic data in a statistically sound way, e.g., using non-overlapping confidence intervals or ANOVA."
- Key point: Compare nondeterministic data in a statistically sound way, such as non-overlapping confidence intervals or ANOVA.

### E8

- Location: §3.2.3, Rule 8
- Quote: "Carefully investigate if measures of central tendency such as mean or median are useful to report. Some problems, such as worst-case latency, may require other percentiles."
- Key point: Think about whether the mean or median is actually useful; some problems (such as worst-case latency) call for other percentiles.

### E9

- Location: §4.2, Rule 9
- Quote: "Document all varying factors and their levels as well as the complete experimental setup (e.g., software, hardware, techniques) to facilitate reproducibility and provide interpretability." / "Ideally, researchers release the source code used for the experiment or at least the input data and their generators."
- Key point: Document all varying factors and their levels and the complete experimental setup; ideally release the experiment's source code, or at least the input data and their generators.

### E10

- Location: §4.1.1 Measurement Environment
- Quote: "If controlling a certain parameter is not possible then we suggest randomization following standard textbook procedures."
- Key point: Environment parameters you cannot control (such as node allocation, process mapping, interference) should be randomized following standard textbook procedures.

### E11

- Location: §4.1.2 Documenting the Setup
- Quote: "We observed how several authors assumed that mentioning a well-known system such as NERSC's Hopper or ORNL's Titan is sufficient to describe the experimental setup."
- Key point: Naming a well-known system is not enough to describe the experimental setup: software gets upgraded, others may not know the exact parameters, and not everyone shares the implicit assumptions.

### E12

- Location: §4.1.2, Warmup and Warm vs. cold cache
- Quote: "to measure the expected time, the first measurement iteration should be excluded from the average computation." / "If small benchmarks are performed repeatedly, then their data may be in cache and thus accelerate computations. This may or may not be representative for the intended use of the code."
- Key point: Some programs build up working state on demand, so the first iteration should be excluded from the average; when small benchmarks run repeatedly, their data may already be in cache, which may not reflect real use of the code.

### E13

- Location: §4.2.1 Measuring Time in Parallel Systems
- Quote: "researchers need to ensure that the timer overhead is only a small fraction (we suggest <5%) of the measurement interval."
- Key point: Reading the timer has its own overhead; make sure it is only a small fraction of the measurement interval (they suggest under 5%) and that the timer resolution is sufficient.

### E14

- Location: §5.1, Rule 11
- Quote: "If possible, show upper performance bounds to facilitate interpretability of the measured results."
- Key point: Where possible, show upper performance bounds (such as theoretical peak) to help readers interpret the measurements.

### E15

- Location: §5.2, Rule 12
- Quote: "Plot as much information as needed to interpret the experimental results. Only connect measurements by lines if they indicate trends and the interpolation is valid."
- Key point: Plot the information needed to interpret the results; connect measurements with lines only if they indicate trends and the interpolation is valid.

### E16

- Location: Abstract
- Quote: "Our investigation of a stratified sample of 120 papers across three top conferences in the field shows that the state of the practice is lacking."
- Key point: A survey of 120 papers from top conferences shows that the state of performance reporting is lacking; for example, papers often do not make clear whether an improvement is deterministic or a chance observation.

### E17

- Location: §4.2.2 Number of Measurements
- Quote: "We now show how the CI can be used to compute the number of measurements needed to achieve a specified error certainty in the result."
- Key point: Confidence intervals can be used to work out how many measurements are needed to reach a specified error bound.
