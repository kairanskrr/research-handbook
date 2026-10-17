# Johari, Pekelis & Walsh 2015: Always Valid Inference: Continuous Monitoring of A/B Tests

- Source: `johari2015always`, [original (arXiv)](https://arxiv.org/abs/1512.04922)
- Version: arXiv 1512.04922, version 3 (July 2019). The authors are from Stanford University and, at the time of the work, were employed by or advised the commercial A/B testing platform Optimizely. Locations give sections only.

### E1

- Location: Abstract
- Quote: "A/B tests are typically analyzed via frequentist p-values and confidence intervals; but these inferences are wholly unreliable if users endogenously choose samples sizes by continuously monitoring their tests."
- Key point: A/B tests are usually analyzed with p-values and confidence intervals, but these inferences are wholly unreliable if experimenters watch results continuously and decide the sample size (when to stop) as they go.

### E2

- Location: §1 Introduction
- Quote: "No correction for continuous monitoring is typically made in industrial practice." / "Even with 10,000 samples (a sample size which is quite common in online A/B testing), Type I error can easily increase fivefold."
- Key point: Industry practice usually makes no correction for continuous monitoring; even with just 10,000 samples (common in online A/B tests), the Type I error rate can easily rise fivefold.

### E3

- Location: §1 Introduction
- Quote: "First, Type I error is controlled under any data-dependent rule the user might choose to stop the experiment (i.e., any stopping time for the data). Continuous monitoring does not inflate Type I error."
- Key point: The authors' "always valid" p-values and confidence intervals control Type I error under any data-dependent stopping rule, so continuous monitoring does not inflate the false positive rate.
