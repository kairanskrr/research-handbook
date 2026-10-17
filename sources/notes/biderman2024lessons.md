# Biderman 等 2024：Lessons from the Trenches on Reproducible Evaluation of Language Models

- 资料：`biderman2024lessons`，[原文（arXiv）](https://arxiv.org/abs/2405.14782)
- 版本：arXiv 2405.14782v3（2026-05-31）。作者是开源评测框架 lm-eval（Language Model Evaluation Harness）的开发者。位置写章节号。
- 说明：自然语言处理和机器学习方向。总结三年评测语言模型的经验：评测为什么难、细节怎样在传递中丢失、为什么分数不只是一个数字，并给出建议。

### E1

- 位置：§2.1 The Key Problem
- 原文："When evaluating language models, there can be many semantically equivalent but syntactically different ways of expressing the same idea." / "However, our best automated tools for determining whether two sentences are semantically equivalent are the very models we are seeking to evaluate."
- 要点：同一个意思可以有很多种说法；而判断两句话意思是否相同，最好的自动工具恰恰是我们要评测的模型本身。

### E2

- 位置：§2.2 Social Dynamics of Evaluation
- 原文："Even when independent evaluation is possible, there is pressure to cherry-pick favorable tasks, choose flattering prompting strategies, or report single-run point estimates that obscure uncertainty."
- 要点：评测者面临压力：挑有利的任务、挑显得好看的提示方式、只报告一次运行的数字而掩盖不确定性。

### E3

- 位置：§2.2 Social Dynamics of Evaluation
- 原文："While API access does enable independent evaluation in principle, many APIs do not expose output log-probabilities which are required for many standard evaluation benchmarks" / "Running comprehensive benchmark suites through APIs is also expensive, and these costs fall disproportionately on independent researchers"
- 要点：很多商业接口不提供输出的概率值，而不少标准评测需要它；通过接口跑全套评测也很贵，成本主要落在独立研究者身上。

### E4

- 位置：§3.1 Challenges，"Minor" Implementation Details Matter
- 原文："the precise string used for a given prompt, even down to whitespace usage, can significantly impact performance" / "performance varies dramatically with the prompt (in some cases, > 20%), and which prompt style works best varies by model. Thus, the selection of prompt affects the model rankings and research conclusions produced in addition to numeric scores themselves"
- 要点：提示词的确切写法，连空格都会显著影响表现；换一种常见的提示方式，有时差 20% 以上，而且哪种方式最好因模型而异，所以提示词会改变模型排名和研究结论。

### E5

- 位置：§3.1 Challenges
- 原文："comparing three independent implementations of MMLU (HELM, lm-eval, and the original MMLU code), they find that these implementations produce widely different scores and even change the ranking order of models"
- 要点：同一个评测集的三种独立实现，给出的分数差别很大，甚至改变了模型的排名。

### E6

- 位置：§3.1 Challenges，Crucial Details Go Unreported
- 原文："For instance, reporting full prompts is a necessary but not sufficient bar for achieving perfect reproducibility. Despite being insufficient on its own, releasing prompts is vitally important and we heavily recommend it and other methodological disclosures."
- 要点：公开完整的提示词是完全复现的必要条件，但不够；即便如此，公开提示词仍然非常重要。

### E7

- 位置：§3.2 Best Practices
- 原文："Provide Evaluation Code: Whenever possible, new publications should be accompanied by release of the exact evaluation code used." / "including, but not limited to: the amount of prompt engineering performed and on which models and evaluation sets; hyperparameters used to calculate loglikelihood or perplexity-based evaluations; generation hyperparameters and answer extraction heuristics used to perform generative evaluations and more."
- 要点：尽量公开确切的评测代码；还要写清做了多少提示词调整、在哪些模型和评测集上调的、生成参数，以及从回答里提取答案的规则。

### E8

- 位置：§3.3 Operationalizing Best Practices
- 原文："per-sample scores can be recorded and logged to disk, while also saving model outputs for post-hoc reproducibility without additional compute expenditures."
- 要点：可以把每个样本的得分和模型输出存下来，事后复核不必再花算力重跑。

### E9

- 位置：§4.1 Challenges，What, if Anything, Does a Benchmark Measure?
- 原文："It is almost never the case that one cares about the actual score of a language model on a particular benchmark. Instead, benchmarks are typically proxies for some broader notion of capability or ability that is difficult to make precise and measure."
- 要点：人们关心的几乎从来不是某个评测集上的分数本身；评测集只是某种难以精确测量的能力的替代指标。

### E10

- 位置：§4.1 Challenges，Lack of Reporting on Uncertainty and Variance
- 原文："Presenting single-run point estimates of performance (top) instead of a 95% confidence interval across 10 runs of the benchmark (bottom) paints a very different pictures regarding the comparative performance of different models." / "Practitioners frequently tout small increases in numeric score on datasets such as these, ignoring the fact that such "improvements" might be washed out simply via sampling again at the same temperature."
- 要点：只报一次运行的分数，和报 10 次运行的 95% 置信区间，对模型高下会得出很不一样的结论；在小评测集上宣称的小幅提升，可能同样温度下再采样一次就没了。

### E11

- 位置：§4.1 Challenges，The Benchmark Lottery
- 原文："Through exploratory analysis of model completions we have observed that this at-random performance is a result of failing to follow the task and output format for this prompting style, even when it can score well using an alternative format."
- 要点：一个模型在某种提示格式下表现接近随机猜，查看它的输出才发现，原因是没有按这种格式的要求作答，换一种格式就能得高分。

### E12

- 位置：§4.2 Best Practices
- 原文："Perform Statistical Analyses, and Report on Sources of Variance and Error: Instead of reporting isolated numbers, more effort should be made to contextualize the durability of performance estimates made by benchmarks, such as by reporting variance over several runs, or reporting statistical significance." / "Do Exploratory Analysis to Build Better Understanding of Results: To understand why a model is scoring so well or so poorly, it is important to do some sort of qualitative error analysis."
- 要点：建议做统计分析，报告多次运行的方差或统计显著性，而不是孤立的数字；并做定性的错误分析，弄清模型为什么得分高或低。

### E13

- 位置：§4.3 Operationalizing Best Practices
- 原文："Language models are stochastic objects, so one natural notion of variation would be to run the model several times and measure how the results change" / "suppose that the particular questions in a given evaluation benchmark are samples from some distribution of interesting questions in the world. How much variation in model behavior should we expect as we sample new questions from the same distribution?"
- 要点：有两种波动：同一批题目反复运行模型，结果怎么变；把评测题目看成从一大类题目中抽出的样本，换一批题结果会怎么变（可以用自助法估计）。两种都值得报告。
