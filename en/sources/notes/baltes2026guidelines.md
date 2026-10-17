# Baltes et al. 2026: Guidelines for Empirical Studies in Software Engineering involving Large Language Models

- Source: `baltes2026guidelines`, [original (arXiv)](https://arxiv.org/abs/2508.15503), [online version (llm-guidelines.org)](https://llm-guidelines.org/)
- Version: arXiv 2508.15503v8 (2026-09-18), accepted manuscript at the journal Empirical Software Engineering. Developed jointly by 22 software engineering researchers; the online version is continually updated. Locations give section numbers in arXiv v8.
- Note: Written for software engineering research. Sorts the ways large language models are used in research into seven study types and gives eight guidelines for design and reporting; each guideline separates "must" from "should" criteria.

### E1

- Location: §4 Study Types
- Quote: "We use the term study type to refer to categories of LLM involvement in empirical research, rather than to research methodologies (e.g., experiments, case studies). A single empirical study may involve multiple such study types."
- Key point: Study types here classify the role a large language model plays in a study, not the research method; one study can involve several types at once.

### E2

- Location: §4.1 LLMs as Tools for Software Engineering Researchers
- Quote: "For example, LLMs can perform qualitative coding on natural language text such as interview transcripts (LLMs as Annotators), assess the quality of software artifacts (LLMs as Judges), generate summaries of research papers (LLMs for Synthesis), or simulate human behavior in empirical studies (LLMs as Subjects)." / "However, these applications each pose challenges to validity and reproducibility."
- Key point: Large language models can serve as researchers' tools: doing qualitative coding (annotators), assessing artifact quality (judges), summarizing literature (synthesis), or simulating human behavior (subjects); each use poses challenges to validity and reproducibility.

### E3

- Location: §4.2, §4.2.3 Benchmarking LLMs for Software Engineering Tasks
- Quote: "Researchers have studied how software engineers use LLMs (Studying LLM Usage), developed new tools that integrate LLMs (LLMs for Tools), and benchmarked LLMs for software engineering tasks (Benchmarking LLMs)." / "Benchmarking studies measure LLM performance on standardized SE tasks against reference outputs and shared metrics."
- Key point: Large language models can also be what is studied: how engineers use them, new tools built around them, and benchmarks on standard tasks; benchmarking studies measure performance against reference outputs with shared metrics.

### E4

- Location: §1 Introduction
- Quote: "Angermeir et al examined 85 LLM-centric ICSE and ASE 2024 papers [6]. Of the 18 papers that both used OpenAI models and provided artifacts, only five were complete enough to execute, and none fully reproduced the original results"
- Key point: A survey of 85 LLM-centric papers from two top software engineering conferences in 2024 found that of the 18 that used OpenAI models and shared artifacts, only five could be run, and none fully reproduced the original results.

### E5

- Location: §1 Introduction
- Quote: "First, their inherent non-determinism causes variability across runs [24, 147], and slight changes can lead to substantially different results [2, 139]. Second, commercial models evolve beyond version identifiers, so reported performance can change over time [33]. Third, even for "open" models, training data and fine-tuning details often remain undisclosed [51]. Moreover, prompt formatting choices alone can shift accuracy by up to 76 percentage points [143]"
- Key point: Studies with large language models are hard to reproduce for three reasons: outputs are non-deterministic and vary across runs, commercial models change beyond their version numbers, and even "open" models often do not disclose training data; prompt formatting alone can shift accuracy by up to 76 percentage points.

### E6

- Location: §5 Guidelines
- Quote: "A must criterion is a requirement. Studies that intend to follow these guidelines are expected to meet all must criteria. A should criterion represents a desired practice that strengthens a study's rigor or transparency. However, there may be valid reasons to deviate in particular circumstances"
- Key point: Criteria come in two levels: "must" is a hard requirement; "should" is a practice that strengthens rigor and transparency, from which there may be valid reasons to deviate in particular cases.

### E7

- Location: §5.1 Declare LLM Usage and Role, Summary and §5.1.2
- Quote: "Researchers must disclose any use of LLMs to support empirical studies, specifying which LLM was used, how it was used, and where in the research process it was employed." / "When a study assigns multiple distinct roles to LLMs (e.g., one model generates evaluation data while another scores outputs), each role should be declared separately."
- Key point: You must disclose which large language model you used, how, and at which stage of the research; if it plays several roles in one study, declare each role separately.

### E8

- Location: §5.2.2 Recommendations
- Quote: "Since default values might change over time, researchers should report all configuration values, even if they used the defaults." / "In summary, researchers must report in the paper at minimum (1) the exact model or tool name and version, (2) all parameters they configured that affect output generation, (3) the date of study execution"
- Key point: At minimum the paper must give the exact model or tool name and version, every parameter that affects output, and the date the study was run; because defaults can change, default settings should be reported too.

### E9

- Location: §5.2.2 Recommendations
- Quote: "Commercial models (e.g., GPT-5) or LLM-based tools (e.g., ChatGPT) might not give researchers access to all required information. For these tools, researchers should report what is available and openly acknowledge limitations that hinder reproducibility."
- Key point: When a commercial model does not expose all the information, report what is available and openly acknowledge the limitations that hinder reproduction.

### E10

- Location: §5.2.5 Challenges
- Quote: "Even with a temperature of 0, full determinism is rarely guaranteed." / "Researchers should not treat a temperature of 0 as a guarantee of reproducibility, but as one measure among several, including fixed seed values, system fingerprints, and archiving of raw outputs."
- Key point: Setting temperature to 0 rarely guarantees fully deterministic output; it is one measure among several, alongside fixed seeds, recorded system fingerprints and archived raw outputs.

### E11

- Location: §5.3.2 Recommendations, Prompt Reporting and Prompt Development
- Quote: "Researchers must report all prompts used in an empirical study, including instructions, task context, input data, and output indicators." / "Because prompt effectiveness varies between models and model versions, researchers must make clear which prompts were used for which models in which versions and with which configuration."
- Key point: You must report every prompt used in the study and make clear which prompt went to which model, version and configuration.

### E12

- Location: §5.3.2 Recommendations, Prompting Strategy and Input Handling
- Quote: "Researchers must specify whether zero-shot, one-shot, or few-shot prompting was used. For few-shot prompts, researchers must explain in the paper how the examples were selected" / "If multiple versions of a prompt were tested, researchers should describe how these variations were evaluated and how the final design was chosen."
- Key point: You must state how many examples the prompt included (zero-shot, one-shot or few-shot) and how they were chosen; if you tried several prompt versions, describe how you compared them and picked the final one.

### E13

- Location: §5.3.1 Rationale
- Quote: "Sclar et al question the methodological validity of comparing models with "an arbitrarily chosen, fixed prompt format", because their research has shown that the performance of different prompt formats only weakly correlates between different models"
- Key point: How well a prompt format works correlates only weakly across models, so comparing models with a single arbitrarily chosen prompt format is methodologically unsound.

### E14

- Location: §5.4.1 Rationale, §5.4.4 Benefits
- Quote: "Just as a human participant might give different answers to the same question asked two months apart, the responses from tools such as ChatGPT can also vary over time" / "Unlike human participant conversations, which often cannot be reported because of confidentiality, LLM interaction logs can be shared. This enables reproduction studies, tracking of response changes over time or across model versions, and secondary research on LLM consistency for specific SE tasks."
- Key point: A model's answers change over time, just as a person may answer the same question differently two months apart; unlike interview transcripts with people, model interaction logs (the prompts sent and responses received) can be shared, which supports reproduction, tracking changes and secondary research.

### E15

- Location: §5.5.2 Recommendations
- Quote: "Furthermore, researchers should check whether a less resource-intensive approach (e.g., for static analysis tasks or program repair) can serve as a baseline." / "Even if LLM-based tools outperform baselines, researchers should discuss whether the resources consumed justify the (often marginal) improvements"
- Key point: Check whether a less resource-intensive traditional approach (for example, static analysis) can serve as a baseline; even if the model does better, discuss whether the resources it consumes justify the often marginal improvement.

### E16

- Location: §5.5.2 Recommendations
- Quote: "Due to LLM non-determinism, researchers should repeat experiments and report descriptive statistics of model or tool performance (e.g., arithmetic mean, median, confidence intervals, standard deviations)" / "If comparing models or tools, researchers should use appropriate inferential statistics with effect sizes rather than relying solely on differences in means or other summary statistics."
- Key point: Because outputs are non-deterministic, repeat experiments and report means, medians, confidence intervals and standard deviations; when comparing models or tools, use inferential statistics with effect sizes rather than just comparing averages.

### E17

- Location: §5.5.2 Recommendations
- Quote: "researchers should justify their chosen number of repetitions, for example, through a power analysis or by monitoring the convergence of descriptive statistics across incremental runs. A pilot study can help estimate the expected variability and inform this decision."
- Key point: Justify the number of repetitions, for example with a power analysis or by adding runs until the summary statistics stabilize; a pilot study can help estimate how much variation to expect.

### E18

- Location: §5.5.2 Recommendations
- Quote: "Prior adoption alone does not constitute sufficient justification; researchers must not justify metric choices solely by citing their use in prior work."
- Key point: "Earlier work used it" is not enough to justify choosing a metric.

### E19

- Location: §5.5.2 Recommendations
- Quote: "After running a benchmark, researchers should perform an error analysis by categorizing the failures observed and reporting the relative frequency of each category."
- Key point: After running a benchmark, do an error analysis: categorize the failures and report how often each category occurs.

### E20

- Location: §5.5.2 Recommendations
- Quote: "maintaining a held-out subset of items for ongoing, uncontaminated evaluation; embedding canary strings, that is, unique markers that downstream tools can later search for in model outputs to detect inclusion in training data" / "Researchers using existing benchmarks should additionally discuss contamination as a study limitation"
- Key point: When building a new benchmark, keep a held-out set of items for ongoing uncontaminated evaluation and embed canary strings (unique markers that later reveal whether the benchmark ended up in training data); if you use an existing benchmark, discuss contamination as a limitation.

### E21

- Location: §5.5.5 Challenges
- Quote: "To mitigate contamination, researchers can create new benchmark datasets by collecting data after a specified cutoff date; researchers must disclose data sources and collection dates for each release. However, this temporal approach requires continuous updates as new models may include the benchmark in future training data."
- Key point: You can build a benchmark only from data collected after a cutoff date and disclose the sources and collection dates, but new models will eventually train on that data too, so the benchmark needs continual updating.

### E22

- Location: §5.5.5 Challenges
- Quote: "In a survey of 572 code benchmarks released between 2014 and 2025, Cao et al found that 84.2% did not consider test suite coverage when constructing test cases, 64.0% reported single-pass evaluations without controlling for randomness, and 82.5% did not address data contamination"
- Key point: A survey of 572 code benchmarks found that 64.0% reported single runs without controlling for randomness and 82.5% did not address data contamination.

### E23

- Location: §5.6 Use an Open LLM as a Baseline, Summary and §5.6.4 Benefits
- Quote: "When researchers can control which LLM a study uses, they should include an open-weight LLM, ideally an open-source LLM, as a baseline and report inter-model agreement." / "Unlike proprietary alternatives, which can be withdrawn or silently updated, open LLMs remain available for future studies."
- Key point: When you can choose the model, include an open-weight model (ideally open-source) as a baseline; proprietary models can be withdrawn or silently updated, while open models stay available for future studies.

### E24

- Location: §5.6.2 Recommendations
- Quote: "An open-weight LLM has publicly released trained weights, so others can fine-tune, adapt, or deploy the model" / "Open-source LLMs are preferable, because researchers can check their training data for benchmark contamination" / "We acknowledge that including an open LLM baseline might not always be possible, for example, if the study involves human participants, and letting them work on the tasks using two different models might not be feasible. Using an open model as a baseline is also not necessary if the use of the LLM is tangential to the study goal."
- Key point: An open-weight model has publicly released trained weights that others can deploy and adapt; open-source models are better because you can check their training data for benchmark contamination. The open baseline can be skipped when human participants cannot feasibly work with two models, or when the model is only tangential to the study.

### E25

- Location: §5.7.2 Recommendations, Replacing Human Judgment
- Quote: "In such cases, researchers must explain whether and how the replacement is justified" / "High inter-model agreement can reflect shared model biases rather than valid annotation, so researchers should additionally validate a sample against human experts before treating LLM outputs as a substitute for human work"
- Key point: When a model replaces people for annotation, coding or as study subjects, you must explain whether the replacement is justified; agreement among several models may just reflect shared biases, so also check a sample against human experts.

### E26

- Location: §5.7.2 Recommendations, Subjective Judgment and Agreement
- Quote: "Krippendorff recommends discarding data with α < 0.667, considers 0.667 ≤ α < 0.8 sufficient only for tentative conclusions, and requires α ≥ 0.8 for reliable data"
- Key point: By Krippendorff's standard, data with an agreement coefficient α below 0.667 should be discarded, 0.667 to 0.8 supports only tentative conclusions, and only α of 0.8 or above counts as reliable.

### E27

- Location: §4.3 Advantages and Challenges
- Quote: "No compelling evidence exists that LLMs can accurately simulate human participants or reliably judge most relevant properties of SE artifacts." / "LLMs may be better suited for augmenting rather than replacing human researchers"
- Key point: There is no compelling evidence yet that large language models can accurately simulate human participants or reliably judge most properties of software artifacts; they may be better at assisting researchers than replacing them.

### E28

- Location: §4.3 Advantages and Challenges
- Quote: "Crucially, reliability does not imply validity: a reliable LLM might be reliably inaccurate"
- Key point: Reliability is not validity: a model can give the same wrong answer consistently every time.

### E29

- Location: §4.3 Advantages and Challenges
- Quote: "In a recent open letter, 419 experienced qualitative researchers argued "that analytic approaches such as reflexive thematic analysis are human research practices requiring a subjective, positioned, and reflexive researcher and therefore the use of GenAI in such approaches is not methodologically congruent""
- Key point: In an open letter, 419 qualitative researchers argued that methods such as reflexive thematic analysis require a positioned, reflexive human researcher, so using generative AI for them is methodologically incongruent.

### E30

- Location: §5.8.2 Recommendations, External Validity
- Quote: "Mitigations include triangulation across multiple models (e.g., proprietary and open), independent datasets, and complementary metrics; sensitivity analysis that varies LLM configurations, prompts, architecture decisions, datasets, and where applicable participant backgrounds; and performing longitudinal re-runs"
- Key point: Ways to reduce threats to external validity: triangulate across several models (proprietary and open), independent datasets and complementary metrics; run sensitivity analyses that vary configurations, prompts, datasets and so on; and re-run the study over time.

### E31

- Location: §5.8.2 Recommendations, Internal Validity
- Quote: "Evaluation data entering model-improvement pipelines: Evaluation samples can unintentionally feed retraining or fine-tuning, especially in longitudinal studies involving LLMs." / "As transparency on training data is limited for LLMs, researchers must discuss potential data leakage effects and their impact on results."
- Key point: Because training data are opaque, you must discuss possible data leakage and its effect on results; evaluation samples may also unintentionally feed model retraining, especially in longitudinal studies.

### E32

- Location: §5.8.2 Recommendations, Environmental & Sustainability Constraints
- Quote: "Researchers should justify the LLM's resource consumption against the benefits over traditional approaches." / "Cost accounting tracks resource consumption by reporting tokens, service costs, or hardware specifications."
- Key point: Justify the model's resource consumption by its benefits over traditional approaches; cost accounting can report token counts, service costs or hardware specifications.

### E33

- Location: §5.8.2 Recommendations, Reliability & Reproducibility
- Quote: "Researchers must discuss the measures taken to increase reliability and reproducibility. However, non-deterministic reproducibility is not inherently disqualifying."
- Key point: You must discuss what you did to improve reliability and reproducibility, but results that cannot be reproduced exactly are not in themselves a reason to reject a study.

### E34

- Location: §4.3 Advantages and Challenges
- Quote: "LLMs can annotate, judge, synthesize, and simulate faster and at lower cost than human researchers, with studies showing cost reductions of 50–96% on various natural language tasks [160] (e.g., He et al found that GPT-4 annotation required only two days and 122.08 USD compared to several weeks and 4,508 USD for a comparable MTurk pipeline [61])."
- Key point: Large language models annotate and judge faster and more cheaply than people, with reported cost reductions of 50–96%; in one example, GPT-4 annotation took two days and 122.08 USD, against several weeks and 4,508 USD for a comparable crowdsourcing pipeline.

### E35

- Location: §2 Scope and Conventions, Related Reporting Guidelines
- Quote: "We target SE research because reporting guidelines from other disciplines do not address its specific needs" / "Outside SE, these include Gallifant et al's TRIPOD-LLM for healthcare [48], Navarro et al's HCI guidelines [104], and Kapoor et al's REFORMS for ML-based science [76]."
- Key point: These guidelines target software engineering; outside it, healthcare (TRIPOD-LLM), human-computer interaction, and machine-learning-based science (REFORMS) each have their own reporting guidelines for large language models.

### E36

- Location: §5.2.3 Examples
- Quote: "We integrated a gpt-4 model in version 0125-Preview via the Azure OpenAI Service, and configured it with a temperature of 0.7, top_p set to 0.8, a maximum token length of 512, and the seed value 23487. We ran our experiment on 10th January 2025. The system fingerprint was fp_6b68a8204b."
- Key point: An example of adequate model reporting: model name and version, access channel, temperature, top_p, maximum length, random seed, date of the experiment and system fingerprint.

### E37

- Location: §5.5.2 Recommendations
- Quote: "Benchmark scores often confound the target capability with unrelated capabilities the task happens to require." / "More broadly, output format compliance (e.g., specific JSON schemas or unit-test conventions) and general instruction-following capability are routinely bundled into the aggregate benchmark score"
- Key point: Benchmark scores often mix the target capability with unrelated ones, such as producing output in the required format or following instructions.

### E38

- Location: §5.7.2 Recommendations, Subjective Judgment and Agreement; §4.3
- Quote: "When the judgment is subjective (i.e., depends on the judge's values or theories), the same artifacts should be judged independently by both the LLM and a panel of human experts, and the LLM judgments should then be compared against an aggregated human reference." / "However, both human and LLM judges exhibit systematic biases, such as preferring outputs with fake citations or rich formatting"
- Key point: For subjective judgments, have the model and a panel of human experts independently judge the same artifacts, then compare the model's judgments with the aggregated human reference; both human and model judges show systematic biases, such as favoring outputs with fake citations or rich formatting.

### E39

- Location: §5.7.6 Study Types
- Quote: "For Benchmarking LLMs, there is less need for human validation when using extensively validated and widely-used benchmarks, but researchers should employ human validation when creating or adapting new benchmarks."
- Key point: Well-validated, widely used benchmarks need less human validation, but new or adapted benchmarks should be validated by humans.
