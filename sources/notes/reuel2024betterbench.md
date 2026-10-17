# Reuel 等人 2024：BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices

- 资料：`reuel2024betterbench`，[原文（arXiv:2411.12990）](https://arxiv.org/abs/2411.12990)
- 版本：arXiv v1（2024 年 11 月 20 日），即 NeurIPS 2024 数据集与基准分会论文。评估结果和清单在 betterbench.stanford.edu 持续更新。
- 说明：机器学习方向。根据文献和对 20 多位相关人员的访谈，提出评价人工智能基准质量的 46 条标准，按基准生命周期分阶段，并用它给 24 个常用基准打分。

### E1

- 位置：§1 Introduction
- 原文："we define a high-quality benchmark as one that is interpretable, clear about its intended purpose and scope, and that is usable."
- 要点：高质量的基准是：结果可解释，目的和范围清楚，好用。

### E2

- 位置：§1 Introduction
- 原文："Presents a novel AI benchmark assessment framework evaluating the quality of AI benchmarks based on 46 criteria derived from expert interviews and domain literature" / "Scores 16 foundation model (FM) and 8 non-FM benchmarks"
- 要点：提出 46 条评价标准（来自专家访谈和文献），并给 16 个基础模型基准、8 个非基础模型基准打分。

### E3

- 位置：Figure 1；Appendix B Benchmark Lifecycle
- 原文："Five stages of the benchmark lifecycle." / "Benchmarks are phased out or replaced when they become saturated (i.e. model performance reaches the benchmark metric's ceiling), the task studied loses relevance, or better alternatives emerge."
- 要点：基准的生命周期分五个阶段（设计、实现、文档、维护、退役）；基准被"做满"、任务不再重要或出现更好的替代时，就该退役。

### E4

- 位置：§4.1 Benchmark Design
- 原文："This includes defining the tested capability or characteristic, describing how the tested capability translates to the benchmark task, and stating how knowing about the tested concept is helpful in real-world applications" / "Clearly stating how the benchmark is different from related existing AI benchmarks is necessary to help benchmark users decide the applicability of a benchmark to their use case."
- 要点：设计阶段要定义被测的能力，说明它怎样转化成基准任务、在现实中有什么用；还要讲清和已有相关基准的区别。

### E5

- 位置：§4.1 Benchmark Design
- 原文："These design choices should be informed by considering use cases and user personas for the benchmark, involving domain experts, and integrating domain literature"
- 要点：设计决定应当考虑使用场景和使用者，请领域专家参与，并结合领域文献。

### E6

- 位置：§4.1 Benchmark Design
- 原文："Including floors, ceilings, human performance levels, and random performance levels for the chosen metric(s) further assists users in understanding a model's score"
- 要点：给出指标的下限、上限、人类水平和随机水平，帮助读者理解一个模型的分数意味着什么。

### E7

- 位置：§4.2 Benchmark Implementation
- 原文："A benchmark can minimize the risks of contamination and gamification by including a globally unique identifier or encrypting evaluation instances." / "Including a training_on_test_set task allows determining whether a model's training data included benchmark examples"
- 要点：给评测样本加全局唯一标识或加密，可以降低污染和被"刷分"的风险；附一个检测任务，可以判断模型训练数据是否包含基准样本。

### E8

- 位置：§4.2 Benchmark Implementation
- 原文："a benchmark should provide working evaluation code, and make its evaluation data, prompts, or dynamic test environment accessible. A script should be available to replicate initial published results."
- 要点：基准应提供能运行的评测代码，公开评测数据、提示词或测试环境，并提供复现论文结果的脚本。

### E9

- 位置：§4.3 Benchmark Documentation
- 原文："developers should document normative assumptions about benchmark properties and discuss the limitations of their benchmark." / "Lastly, developers should specify the applicable license to provide legal clarity and enable, e.g., commercial use."
- 要点：文档要写明基准背后的规范性假设、讨论局限，并写明适用的许可证。

### E10

- 位置：§4.4 Benchmark Maintenance
- 原文："Developers should regularly check code usability and maintain a feedback channel for users to report issues or suggest improvements. Providing contact details of a person responsible for the benchmark facilitates communication and support." / "if a benchmark is not maintained anymore, authors should include a corresponding statement indicating that the benchmark was retired in any official benchmark artefacts."
- 要点：维护阶段要定期检查代码还能不能用，提供反馈渠道和联系人；不再维护时，要在官方发布物里声明已退役。

### E11

- 位置：§5 Other Design Considerations，Versioning
- 原文："Minor updates (e.g., removing faulty prompts) should be clearly indicated via task versioning [13]. Major updates require releasing new benchmark versions"
- 要点：小的更新（如删掉有错的题）要用版本号标明；大的更新要发布新版本的基准。

### E12

- 位置：§5 Other Design Considerations，Detecting small improvements
- 原文："Benchmarks should be designed so that a 1% improvement can be reliably detected"
- 要点：基准的设计应能可靠地检测出 1% 的提升。

### E13

- 位置：§5 Other Design Considerations，Dynamic vs. static benchmarks
- 原文："Dynamic benchmarks may better address quick saturation (Sec. 8) and contamination (Sec. 8) issues but reduce result comparability"
- 要点：动态基准（持续更新题目）更能应对很快被做满和数据污染，但结果之间更难比较。

### E14

- 位置：§7 Discussion
- 原文："Yet, 14 out of 24 benchmarks did not perform multiple evaluations of the same model or report statistical significance or uncertainty of results." / "Notably, 17 out of 24 benchmarks do not provide easy-to-run scripts to replicate the results reported in the initial paper"
- 要点：24 个基准中，14 个没有对同一模型多次评测、也没报告显著性或不确定性；17 个没有提供容易运行的复现脚本。

### E15

- 位置：§7 Discussion
- 原文："We assume that benchmark developers do not intentionally construct insufficient benchmarks, but rather do so due to limited knowledge of what constitutes a good benchmark."
- 要点：基准做得不好，多半不是故意，而是不知道好基准应该是什么样。

### E16

- 位置：§8 Open Challenges，Contamination
- 原文："For example, benchmark developers cannot enforce model developers' use of canary strings to avoid training on benchmark data. Preventing data contamination, particularly in models reliant on large amounts of web-scraped data, is a shared responsibility between benchmark and model developers."
- 要点：建基准的人无法强迫模型开发者遵守"金丝雀字符串"（嵌在数据里、提示不要拿来训练的标记）；防止污染是建基准者和模型开发者的共同责任。

### E17

- 位置：§8 Open Challenges，Quick saturation
- 原文："Some benchmarks have been saturated within months of their release"
- 要点：有些基准发布几个月就被做满了。

### E18

- 位置：§9 Limitations
- 原文："Furthermore, assessing the construct validity of a benchmark and determining whether its approach to assessing a concept is truly effective would presumably require in-depth analysis by domain experts in the respective fields, which is beyond the scope of this assessment. Instead, we aim to provide benchmark developers with a blueprint for minimum quality assurances."
- 要点：这套标准只是最低质量保证；基准是否真的测到了要测的概念（构念效度），需要领域专家深入分析，不在它的范围内。

### E19

- 位置：§2.2 Benchmarking Best Practices in Other Fields
- 原文："[7] also notes that the methods or approaches being evaluated should not be used to create the gold standard dataset."
- 要点：（转述生物信息学的基准文献）被评估的方法不应该被用来制作标准答案数据集。
