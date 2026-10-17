# Sallou et al. 2024: Breaking the Silence: the Threats of Using LLMs in Software Engineering

- Source: `sallou2024breaking`, [arXiv](https://arxiv.org/abs/2312.08055)
- Version: ICSE-NIER 2024 (New Ideas and Emerging Results track, pp. 102–106), DOI 10.1145/3639476.3639764; read as arXiv 2312.08055v2 (2024-01-08). Locations give section numbers.
- Note: a short software engineering paper on three threats to validity when using large language models in research: closed-source models, implicit data leakage, and reproducibility. It offers recommendations for researchers and model providers, demonstrated by using ChatGPT to generate tests for two buggy programs from Defects4J.

### E1

- Location: §1 Introduction
- Quote: "Although ChatGPT3.5, as a general-purpose chatbot, is not fine-tuned for specific SE tasks, it possesses precise knowledge of the bugs within these projects (see Figure 1). Thus, when OpenAI models are employed for tasks like patch generation, fault localization, or test generation for Defects4J, they have superior performance compared to an unknown code."
- Key point: ChatGPT has precise knowledge of the bugs in the Defects4J bug dataset, so it performs better on repair, fault localization, and test generation there than on code it has not seen.

### E2

- Location: §2.1 Closed-Source Models, Model Evolution Unpredictability
- Quote: "Such changes can occur during or after the research approach has been presented, potentially making the presented results obsolete." / "Indeed, distinguishing whether the improvements claimed in the new contribution are the result of changes to the LLMs' models or due to the novelty of the contribution becomes a complex task."
- Key point: Closed-source models can change during or after a study, making results obsolete, and for work that builds on earlier results it becomes hard to tell whether improvements come from the new method or from changes to the model.

### E3

- Location: §2.2 Implicit Data Leakage, Data leakage due to pre-training
- Quote: "They reported remarkable performance discrepancies between the HumanEval (>69% branch coverage) and the SF110 (2% branch coverage) datasets. We remark that the former is available on GitHub while the latter is not (available on SourceForge instead)."
- Key point: For the same unit test generation task, an LLM reached over 69% branch coverage on HumanEval, which is on GitHub, but only 2% on SF110, which is on SourceForge instead.

### E4

- Location: §2.2 Implicit Data Leakage, Data leakage due to fine-tuning
- Quote: "Consequently, a scenario of data leakage can arise if the LLM is trained on "project A" that employs a specific API, and the resulting model is subsequently used to fix the usage of the same API in another project within the test set."
- Key point: Even when training and test sets are split by project, dependencies and APIs shared across projects can cause leakage.

### E5

- Location: §2.3 Reproducibility, Output Variability
- Quote: "LLMs exhibit variability in their outputs, even when using identical input. Running the same prompt several times may not result in identical output, rendering the usage of LLMs non-deterministic."
- Key point: LLMs give different outputs for identical input; running the same prompt several times may not produce the same result.

### E6

- Location: §2.3 Reproducibility, Time-Based Output Drift
- Quote: "In particular, for code generation, the mismatch is evaluated at 20% for GPT-3.5 and 50% for GPT-4 between March 2023 and June 2023. Moreover, the number of executable outputs drops from 52% to 10% for GPT-3.5, and from 22% to 2% for GPT-4.0 for the same period."
- Key point: A cited study found that between March and June 2023, 50% of GPT-4's code generation answers changed, and its directly executable outputs fell from 22% to 2%.

### E7

- Location: §3.2.1 Reproducibility, Assess output variability
- Quote: "Due to output variability, running the LLMs' inference only once is insufficient to ensure reproducibility. Therefore, we argue in favor of conducting multiple replication runs and using variability metrics during the evaluation." / "For our showcase example, we queried ChatGPT3.5 ten times over different days using the same prompts" / "For Math-5, we report an average branch coverage of 70% for the tested Java method with a large variability (interquartile range or IQR) of 27.5%."
- Key point: A single run is not enough; run multiple replications and report variability metrics. In the demonstration, the same prompts sent ten times over different days gave 70% average branch coverage with an interquartile range of 27.5%.

### E8

- Location: §3.2.1 Reproducibility, Provide execution metadata
- Quote: "(ii) Prompts: The exact inputs (queries) used for the inference and evaluation of the LLMs. (iii) Date of LLMs query: The date is relevant data to share to address the time-based output drift"
- Key point: The execution metadata to share includes model details, the exact prompts, the query dates (to address output drift over time), variability metrics, and the evaluation package.

### E9

- Location: §3.2.2 Data Leakage, Assess LLMs on metamorphic data
- Quote: "These new snippets maintain semantic and behavioral equivalence with the original code, yet exhibit structural differences (e.g., distinct Abstract Syntax Trees)." / "Therefore, we advise researchers to complement the analysis of the LLMs performance with new data samples generated with metamorphic testing. The selection of metamorphic transformations should align with the specific task at hand."
- Key point: Complement evaluation with new samples generated by metamorphic transformations, which keep the code's semantics and behavior but change its structure; the choice of transformation should fit the task.

### E10

- Location: §3.2.2 Data Leakage, Assess LLMs on metamorphic data
- Quote: "In particular, we (1) removed the javadoc and (2) renamed the method under test and its input parameters." / "While ChatGPT constantly generated tests for the original program with a branch coverage of 71%, it struggled to generate any meaningful tests on the transformed code."
- Key point: In the demonstration, merely removing the javadoc and renaming the method and its parameters took ChatGPT from a steady 71% coverage on the original program to almost no meaningful tests on the transformed one.

### E11

- Location: §3.2.2 Data Leakage, Use different sources; Code clone detection
- Quote: "Hence, we recommend researchers gather software projects and data from multiple sources." / "However, researchers can use well-established code clone detection techniques to check if the generated code (e.g., test cases) is similar to code seen in online repositories (e.g., manually-written test cases)."
- Key point: Gather data from multiple sources, and use code clone detection to check whether model-generated code resembles code already in online repositories.
