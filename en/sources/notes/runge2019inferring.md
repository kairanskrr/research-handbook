# Runge et al. 2019: Inferring causation from time series in Earth system sciences

- Source: `runge2019inferring`, [original](https://doi.org/10.1038/s41467-019-10105-3)
- Version: Nature Communications 10: 2553, 2019, CC BY open access. Text taken from Europe PMC (PMC6572812). A Perspective co-written by developers of causal inference methods and Earth system scientists. Locations give subheadings.

### E1

- Location: Introduction
- Quote: "Discovering physical laws this way is a challenging problem when studying large-scale complex dynamical systems such as the Earth system, because replicated interventional experiments are either infeasible or ethically problematic"
- Key point: In large-scale complex systems such as the Earth system, replicated interventional experiments are either infeasible or unethical, so discovering laws through experiment is hard.

### E2

- Location: Introduction
- Quote: "While randomized controlled experiments are a standard approach in medicine and the social sciences" / "the main current alternative within most disciplines of Earth sciences are computer simulation experiments."
- Key point: Randomized controlled experiments are standard in medicine and the social sciences, but in most branches of Earth science the main current alternative is computer simulation experiments.

### E3

- Location: Introduction
- Quote: "In Earth system sciences, besides simulation experiments, (Pearson) correlation and regression methods are still the most commonly used tools. However, causal inference methods do have the potential to substantially advance the state-of-the-art—if the underlying assumptions and methodological challenges are taken into consideration."
- Key point: Besides simulation experiments, correlation and regression remain the most common tools in Earth system sciences; causal inference methods could substantially advance research, provided their underlying assumptions and methodological challenges are taken into account.

### E4

- Location: Causal inference methods
- Quote: "Many causal inference methods for time series are grounded on the assumptions of time-order (causes precede effects), Causal Sufficiency, meaning that all direct common drivers are observed, and the Causal Markov Condition"
- Key point: Many causal inference methods for time series rest on a few assumptions: causes precede effects (time order); all direct common drivers are observed (Causal Sufficiency); and the Causal Markov Condition.

### E5

- Location: Challenges
- Quote: "Often, relevant drivers cannot be measured, which requires to consider the possibility of unobserved variables (Fig. 4 , point 8) regarding a causal interpretation of the estimated graph, since they may render detected links spurious"
- Key point: Relevant drivers often cannot be measured; a causal interpretation of the results must consider possible unobserved variables, since they can make detected links spurious.

### E6

- Location: Challenges
- Quote: "Arguably, identifying the absence of a causal link, implying that a physical mechanism is unlikely 24 , is a more robust finding, which requires less strong assumptions (no Causal Sufficiency)."
- Key point: Establishing the absence of a causal link (implying a physical mechanism is unlikely) is a more robust finding that needs weaker assumptions.

### E7

- Location: Challenges
- Quote: "Time sub-sampling (9) and aggregation (10) can make causal links appear contemporaneous and even cyclic due to insufficient time resolution"
- Key point: With insufficient time resolution (e.g., sampling intervals too long, or time averaging), causal links can look contemporaneous or even cyclic.

### E8

- Location: Validation and a benchmark platform
- Quote: "Method development and comparison require benchmark datasets with known causal ground truth for validation."
- Key point: Developing and comparing causal inference methods requires benchmark datasets with known causal ground truth for validation.
