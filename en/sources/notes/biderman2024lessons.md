# Biderman et al. 2024: Lessons from the Trenches on Reproducible Evaluation of Language Models

- Source: `biderman2024lessons`, [original (arXiv)](https://arxiv.org/abs/2405.14782)
- Version: arXiv 2405.14782v3 (2026-05-31). The authors develop the open-source evaluation framework lm-eval (Language Model Evaluation Harness). Locations give section numbers.
- Note: Natural language processing and machine learning. Summarizes three years of experience evaluating language models: why evaluation is hard, how details get lost as results are passed along, and why a score is more than a single number, with recommendations.

### E1

- Location: §2.1 The Key Problem
- Quote: "When evaluating language models, there can be many semantically equivalent but syntactically different ways of expressing the same idea." / "However, our best automated tools for determining whether two sentences are semantically equivalent are the very models we are seeking to evaluate."
- Key point: The same idea can be phrased in many ways, and the best automated tools for judging whether two sentences mean the same thing are the very models being evaluated.

### E2

- Location: §2.2 Social Dynamics of Evaluation
- Quote: "Even when independent evaluation is possible, there is pressure to cherry-pick favorable tasks, choose flattering prompting strategies, or report single-run point estimates that obscure uncertainty."
- Key point: Evaluators face pressure to cherry-pick favorable tasks, pick flattering prompting strategies, and report single-run numbers that hide uncertainty.

### E3

- Location: §2.2 Social Dynamics of Evaluation
- Quote: "While API access does enable independent evaluation in principle, many APIs do not expose output log-probabilities which are required for many standard evaluation benchmarks" / "Running comprehensive benchmark suites through APIs is also expensive, and these costs fall disproportionately on independent researchers"
- Key point: Many commercial APIs do not expose output log-probabilities, which many standard benchmarks need, and running full benchmark suites through APIs is expensive, a cost that falls mostly on independent researchers.

### E4

- Location: §3.1 Challenges, "Minor" Implementation Details Matter
- Quote: "the precise string used for a given prompt, even down to whitespace usage, can significantly impact performance" / "performance varies dramatically with the prompt (in some cases, > 20%), and which prompt style works best varies by model. Thus, the selection of prompt affects the model rankings and research conclusions produced in addition to numeric scores themselves"
- Key point: The exact prompt string, down to whitespace, can significantly affect performance; switching between common prompt styles sometimes changes scores by more than 20%, and the best style differs by model, so the choice of prompt changes model rankings and research conclusions.

### E5

- Location: §3.1 Challenges
- Quote: "comparing three independent implementations of MMLU (HELM, lm-eval, and the original MMLU code), they find that these implementations produce widely different scores and even change the ranking order of models"
- Key point: Three independent implementations of the same benchmark gave widely different scores and even changed the ranking of models.

### E6

- Location: §3.1 Challenges, Crucial Details Go Unreported
- Quote: "For instance, reporting full prompts is a necessary but not sufficient bar for achieving perfect reproducibility. Despite being insufficient on its own, releasing prompts is vitally important and we heavily recommend it and other methodological disclosures."
- Key point: Publishing full prompts is necessary but not sufficient for exact reproducibility; even so, releasing prompts is vitally important.

### E7

- Location: §3.2 Best Practices
- Quote: "Provide Evaluation Code: Whenever possible, new publications should be accompanied by release of the exact evaluation code used." / "including, but not limited to: the amount of prompt engineering performed and on which models and evaluation sets; hyperparameters used to calculate loglikelihood or perplexity-based evaluations; generation hyperparameters and answer extraction heuristics used to perform generative evaluations and more."
- Key point: Release the exact evaluation code whenever possible, and report how much prompt engineering was done and on which models and evaluation sets, the generation hyperparameters, and the heuristics for extracting answers from outputs.

### E8

- Location: §3.3 Operationalizing Best Practices
- Quote: "per-sample scores can be recorded and logged to disk, while also saving model outputs for post-hoc reproducibility without additional compute expenditures."
- Key point: Logging per-sample scores and saving model outputs lets you re-check results later without spending compute to rerun.

### E9

- Location: §4.1 Challenges, What, if Anything, Does a Benchmark Measure?
- Quote: "It is almost never the case that one cares about the actual score of a language model on a particular benchmark. Instead, benchmarks are typically proxies for some broader notion of capability or ability that is difficult to make precise and measure."
- Key point: People almost never care about a model's score on a particular benchmark for its own sake; benchmarks are proxies for some broader capability that is hard to define and measure precisely.

### E10

- Location: §4.1 Challenges, Lack of Reporting on Uncertainty and Variance
- Quote: "Presenting single-run point estimates of performance (top) instead of a 95% confidence interval across 10 runs of the benchmark (bottom) paints a very different pictures regarding the comparative performance of different models." / "Practitioners frequently tout small increases in numeric score on datasets such as these, ignoring the fact that such "improvements" might be washed out simply via sampling again at the same temperature."
- Key point: Reporting a single-run score instead of a 95% confidence interval over 10 runs gives a very different picture of which model is better; small gains claimed on small benchmarks may vanish just by sampling again at the same temperature.

### E11

- Location: §4.1 Challenges, The Benchmark Lottery
- Quote: "Through exploratory analysis of model completions we have observed that this at-random performance is a result of failing to follow the task and output format for this prompting style, even when it can score well using an alternative format."
- Key point: A model scoring near chance under one prompt format turned out, on inspecting its outputs, to be failing to follow that format's required answer format; with another format it scored well.

### E12

- Location: §4.2 Best Practices
- Quote: "Perform Statistical Analyses, and Report on Sources of Variance and Error: Instead of reporting isolated numbers, more effort should be made to contextualize the durability of performance estimates made by benchmarks, such as by reporting variance over several runs, or reporting statistical significance." / "Do Exploratory Analysis to Build Better Understanding of Results: To understand why a model is scoring so well or so poorly, it is important to do some sort of qualitative error analysis."
- Key point: Do statistical analysis and report variance over several runs or statistical significance rather than isolated numbers, and do qualitative error analysis to understand why a model scores high or low.

### E13

- Location: §4.3 Operationalizing Best Practices
- Quote: "Language models are stochastic objects, so one natural notion of variation would be to run the model several times and measure how the results change" / "suppose that the particular questions in a given evaluation benchmark are samples from some distribution of interesting questions in the world. How much variation in model behavior should we expect as we sample new questions from the same distribution?"
- Key point: There are two kinds of variation: how results change when the model is rerun on the same questions, and how they would change with a new sample of questions if the benchmark is treated as a sample from a larger population of questions (which can be estimated with the bootstrap); both are worth reporting.
