# Sainz 等人 2023：NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark

- 资料：`sainz2023nlp`，[原文](https://arxiv.org/abs/2310.18018)
- 版本：Findings of EMNLP 2023（立场论文）；arXiv 2310.18018v1。
- 说明：讨论大语言模型的数据污染：模型训练时见过评测基准的数据，再在同一基准上评测。

### E1

- 位置：摘要
- 原文："The worst kind of data contamination happens when a Large Language Model (LLM) is trained on the test split of a benchmark, and then evaluated in the same benchmark."
- 要点：最严重的数据污染：大语言模型在某个基准的测试集上训练过，又在同一基准上评测。

### E2

- 位置：摘要
- 原文："Contamination causes an overestimation of the performance of a contaminated model in a target benchmark and associated task with respect to their noncontaminated counterparts."
- 要点：污染会高估受污染模型在该基准上的表现，可能导致错误的科学结论被发表、正确的被放弃。

### E3

- 位置：§3 Defining data contamination
- 原文："When the evaluation split is involved, the experiment is completely invalidated." / "When the train or development splits are involved, this would not affect comparisons with other models that have been developed using those same splits, but it does invalidate conclusions claiming zero-shot or few-shot performance."
- 要点：模型见过评测集的标注，实验完全无效；只见过训练集或开发集，不影响和用同样数据开发的模型比较，但"零样本""少样本"的结论不再成立。此外还有标注指南污染和原始文本污染。

### E4

- 位置：§5.1 Open LLMs
- 原文："we propose to measure the level of data contamination using benchmark data overlap, that is, the percentage of the benchmark that can be found in the pre-training dataset"
- 要点：训练数据公开时，可以用重叠比例衡量污染程度：基准中有多大比例能在预训练数据里找到。

### E5

- 位置：§5.2 Closed LLMs
- 原文："To tackle this problem, we propose to take advantage of LLM's memorization capabilities."
- 要点：训练数据不公开的模型，可以利用模型的记忆能力检测污染，例如看它能否逐字生成基准中的样本。
