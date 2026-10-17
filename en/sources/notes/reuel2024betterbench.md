# Reuel et al. 2024: BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices

- Source: `reuel2024betterbench`, [arXiv:2411.12990](https://arxiv.org/abs/2411.12990)
- Version: arXiv v1 (November 20, 2024), the NeurIPS 2024 Datasets and Benchmarks Track paper. The assessments and checklist are kept up to date at betterbench.stanford.edu.
- Note: machine learning. Drawing on the literature and interviews with more than 20 stakeholders, it proposes 46 criteria for judging the quality of AI benchmarks, organized by stage of the benchmark lifecycle, and uses them to score 24 widely used benchmarks.

### E1

- Location: §1 Introduction
- Quote: "we define a high-quality benchmark as one that is interpretable, clear about its intended purpose and scope, and that is usable."
- Key point: A high-quality benchmark is interpretable, clear about its intended purpose and scope, and usable.

### E2

- Location: §1 Introduction
- Quote: "Presents a novel AI benchmark assessment framework evaluating the quality of AI benchmarks based on 46 criteria derived from expert interviews and domain literature" / "Scores 16 foundation model (FM) and 8 non-FM benchmarks"
- Key point: The paper proposes 46 assessment criteria, drawn from expert interviews and the literature, and scores 16 foundation model benchmarks and 8 non-foundation-model benchmarks.

### E3

- Location: Figure 1; Appendix B Benchmark Lifecycle
- Quote: "Five stages of the benchmark lifecycle." / "Benchmarks are phased out or replaced when they become saturated (i.e. model performance reaches the benchmark metric's ceiling), the task studied loses relevance, or better alternatives emerge."
- Key point: A benchmark's lifecycle has five stages (design, implementation, documentation, maintenance, retirement); a benchmark should be retired when it is saturated, the task loses relevance, or better alternatives appear.

### E4

- Location: §4.1 Benchmark Design
- Quote: "This includes defining the tested capability or characteristic, describing how the tested capability translates to the benchmark task, and stating how knowing about the tested concept is helpful in real-world applications" / "Clearly stating how the benchmark is different from related existing AI benchmarks is necessary to help benchmark users decide the applicability of a benchmark to their use case."
- Key point: At the design stage, define the capability being tested, explain how it translates into the benchmark task and why it matters in real-world use, and state clearly how the benchmark differs from related existing ones.

### E5

- Location: §4.1 Benchmark Design
- Quote: "These design choices should be informed by considering use cases and user personas for the benchmark, involving domain experts, and integrating domain literature"
- Key point: Design choices should consider use cases and user personas, involve domain experts, and draw on domain literature.

### E6

- Location: §4.1 Benchmark Design
- Quote: "Including floors, ceilings, human performance levels, and random performance levels for the chosen metric(s) further assists users in understanding a model's score"
- Key point: Reporting floors, ceilings, human performance, and random performance for the metric helps readers understand what a model's score means.

### E7

- Location: §4.2 Benchmark Implementation
- Quote: "A benchmark can minimize the risks of contamination and gamification by including a globally unique identifier or encrypting evaluation instances." / "Including a training_on_test_set task allows determining whether a model's training data included benchmark examples"
- Key point: Adding a globally unique identifier to evaluation instances or encrypting them lowers the risk of contamination and gaming, and a training_on_test_set task can reveal whether a model's training data included benchmark examples.

### E8

- Location: §4.2 Benchmark Implementation
- Quote: "a benchmark should provide working evaluation code, and make its evaluation data, prompts, or dynamic test environment accessible. A script should be available to replicate initial published results."
- Key point: A benchmark should provide working evaluation code, make its evaluation data, prompts, or test environment accessible, and supply a script that replicates the published results.

### E9

- Location: §4.3 Benchmark Documentation
- Quote: "developers should document normative assumptions about benchmark properties and discuss the limitations of their benchmark." / "Lastly, developers should specify the applicable license to provide legal clarity and enable, e.g., commercial use."
- Key point: Documentation should state the normative assumptions behind the benchmark, discuss its limitations, and specify the applicable license.

### E10

- Location: §4.4 Benchmark Maintenance
- Quote: "Developers should regularly check code usability and maintain a feedback channel for users to report issues or suggest improvements. Providing contact details of a person responsible for the benchmark facilitates communication and support." / "if a benchmark is not maintained anymore, authors should include a corresponding statement indicating that the benchmark was retired in any official benchmark artefacts."
- Key point: Maintenance means regularly checking that the code still works and offering a feedback channel and a contact person; when a benchmark is no longer maintained, its official artifacts should state that it has been retired.

### E11

- Location: §5 Other Design Considerations, Versioning
- Quote: "Minor updates (e.g., removing faulty prompts) should be clearly indicated via task versioning [13]. Major updates require releasing new benchmark versions"
- Key point: Minor updates, such as removing faulty prompts, should be marked with version numbers; major updates require a new benchmark version.

### E12

- Location: §5 Other Design Considerations, Detecting small improvements
- Quote: "Benchmarks should be designed so that a 1% improvement can be reliably detected"
- Key point: Benchmarks should be designed so that a 1% improvement can be reliably detected.

### E13

- Location: §5 Other Design Considerations, Dynamic vs. static benchmarks
- Quote: "Dynamic benchmarks may better address quick saturation (Sec. 8) and contamination (Sec. 8) issues but reduce result comparability"
- Key point: Dynamic benchmarks, whose items keep changing, cope better with quick saturation and contamination but make results harder to compare.

### E14

- Location: §7 Discussion
- Quote: "Yet, 14 out of 24 benchmarks did not perform multiple evaluations of the same model or report statistical significance or uncertainty of results." / "Notably, 17 out of 24 benchmarks do not provide easy-to-run scripts to replicate the results reported in the initial paper"
- Key point: Of 24 benchmarks, 14 did not run multiple evaluations of the same model or report statistical significance or uncertainty, and 17 provided no easy-to-run script to replicate their results.

### E15

- Location: §7 Discussion
- Quote: "We assume that benchmark developers do not intentionally construct insufficient benchmarks, but rather do so due to limited knowledge of what constitutes a good benchmark."
- Key point: Poor benchmarks are usually not deliberate but stem from limited knowledge of what a good benchmark looks like.

### E16

- Location: §8 Open Challenges, Contamination
- Quote: "For example, benchmark developers cannot enforce model developers' use of canary strings to avoid training on benchmark data. Preventing data contamination, particularly in models reliant on large amounts of web-scraped data, is a shared responsibility between benchmark and model developers."
- Key point: Benchmark builders cannot force model developers to honor canary strings (markers embedded in data asking that it not be used for training); preventing contamination is a shared responsibility of benchmark and model developers.

### E17

- Location: §8 Open Challenges, Quick saturation
- Quote: "Some benchmarks have been saturated within months of their release"
- Key point: Some benchmarks have been saturated within months of release.

### E18

- Location: §9 Limitations
- Quote: "Furthermore, assessing the construct validity of a benchmark and determining whether its approach to assessing a concept is truly effective would presumably require in-depth analysis by domain experts in the respective fields, which is beyond the scope of this assessment. Instead, we aim to provide benchmark developers with a blueprint for minimum quality assurances."
- Key point: The criteria are only a minimum quality assurance; whether a benchmark really measures the intended concept (construct validity) needs in-depth analysis by domain experts and is outside their scope.

### E19

- Location: §2.2 Benchmarking Best Practices in Other Fields
- Quote: "[7] also notes that the methods or approaches being evaluated should not be used to create the gold standard dataset."
- Key point: (Reporting benchmarking literature from bioinformatics) The methods being evaluated should not be used to create the gold standard dataset.
