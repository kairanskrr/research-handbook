# Sainz et al. 2023: NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark

- Source: `sainz2023nlp`, [original](https://arxiv.org/abs/2310.18018)
- Version: Findings of EMNLP 2023 (position paper); arXiv 2310.18018v1.
- Note: Discusses data contamination of large language models: a model that saw benchmark data during training is then evaluated on the same benchmark.

### E1

- Location: abstract
- Quote: "The worst kind of data contamination happens when a Large Language Model (LLM) is trained on the test split of a benchmark, and then evaluated in the same benchmark."
- Key point: The worst kind of data contamination: a large language model (LLM) is trained on a benchmark's test split and then evaluated on the same benchmark.

### E2

- Location: abstract
- Quote: "Contamination causes an overestimation of the performance of a contaminated model in a target benchmark and associated task with respect to their noncontaminated counterparts."
- Key point: Contamination overestimates a contaminated model's performance on the benchmark, which can lead to wrong scientific conclusions being published and correct ones being discarded.

### E3

- Location: §3 Defining data contamination
- Quote: "When the evaluation split is involved, the experiment is completely invalidated." / "When the train or development splits are involved, this would not affect comparisons with other models that have been developed using those same splits, but it does invalidate conclusions claiming zero-shot or few-shot performance."
- Key point: If the model saw the evaluation split's annotations, the experiment is completely invalid; if it saw only the train or development split, comparisons with models developed on the same data still hold, but "zero-shot" and "few-shot" claims no longer do. There is also contamination of annotation guidelines and of raw text.

### E4

- Location: §5.1 Open LLMs
- Quote: "we propose to measure the level of data contamination using benchmark data overlap, that is, the percentage of the benchmark that can be found in the pre-training dataset"
- Key point: When training data are public, contamination can be measured as benchmark overlap: the percentage of the benchmark found in the pre-training data.

### E5

- Location: §5.2 Closed LLMs
- Quote: "To tackle this problem, we propose to take advantage of LLM's memorization capabilities."
- Key point: For models whose training data are not public, contamination can be detected by exploiting the model's memorization, for example by checking whether it can reproduce benchmark examples verbatim.
