# Törnberg 2024: Best Practices for Text Annotation with Large Language Models

- Source: `tornberg2024best`, [arXiv](https://arxiv.org/abs/2402.05129)
- Version: arXiv 2402.05129 (2024-02-05). The author is at the University of Amsterdam, writing for social science research that treats text as data. The PDF has no section numbers, so locations give the numbered subheadings in the text.
- Note: social science. Proposes best practices for text annotation (assigning category labels to text) with large language models: choosing a model, a systematic coding procedure, a prompt codebook, validation, prompt design, parameters, ethics, stochasticity, and training data.

### E1

- Location: Introduction
- Quote: "LLM-based text annotation has become something of an academic Wild West, as the lack of established standards has meant that both researchers and reviewers lack benchmarks for LLM-based annotation, leading to risks of low-quality research and the publishing of invalid results."
- Key point: LLM text annotation lacks established standards, so researchers and reviewers have no benchmark to check against, which risks low-quality research and invalid results.

### E2

- Location: 1. Choose an appropriate model
- Quote: "First, the ChatGPT models have been shown to change over time without notice, giving different results to the same instructions as a result to changes in the backend" / "While the API provides access to stable models, these are deprecated after a relatively short time, making reproducibility an impossibility."
- Key point: ChatGPT models change without notice and give different results to the same instructions, and the fixed versions offered through the API are deprecated fairly soon, making reproduction impossible.

### E3

- Location: 1. Choose an appropriate model
- Quote: "The choice of model should be explicitly argued for" / "To ensure reproducibility, use a fixed version of the LLM throughout the project, document the version, and ensure that the model will be available for future use."
- Key point: Argue explicitly for the choice of model; use one fixed version throughout the project, record it, and make sure the model will remain available.

### E4

- Location: 1. Choose an appropriate model
- Quote: "Ideal practice also involves assessing whether your results can be reproduced using several models, thereby showing that the prompt and results are robust to details of implementation. You should in general never use LLMs for annotation through their web interface, as these interfaces do not allow setting parameters, version control, and do not provide sufficient privacy or copyright provision"
- Key point: Ideally, check whether results hold across several models; in general never annotate through a web chat interface, which allows no parameter setting or version control and offers inadequate privacy and copyright protection.

### E5

- Location: 2. Follow a Systematic Coding Procedure
- Quote: "Define the concept: It is important to come in with an explicitly articulated idea of the concept you are trying to capture, to avoid being overly influenced by the interpretations of the LLM."
- Key point: Write down the concept you want to annotate explicitly before starting, so you are not led by the LLM's interpretation.

### E6

- Location: 2. Follow a Systematic Coding Procedure
- Quote: "Once the LLM reached sufficient agreement with the human coders, it can be used to code the full material." / "Ideally, the LLM should approach the reliability achieved among the human coders."
- Key point: Have humans and the LLM code a small sample, compare disagreements, and revise the codebook and prompt until the LLM agrees closely enough with the humans, then use it on the full material; ideally the LLM should approach the reliability reached among human coders.

### E7

- Location: 2. Follow a Systematic Coding Procedure
- Quote: "The human coders should not be considered ground truth: you may find that the LLM's interpretation was superior to the human coder."
- Key point: Human coders are not ground truth; sometimes the LLM's interpretation turns out better.

### E8

- Location: 3. Develop a Prompt Codebook
- Quote: "Note that the prompt should be considered tailored to the model used for its development: applying the same prompt to a different LLM may produce different results, even with models of similar parameter size"
- Key point: A prompt is tuned to the model it was developed on; the same prompt on a different LLM, even one of similar size, may give different results.

### E9

- Location: 4. Validate your model
- Quote: "Hence, it is always necessary to carefully validate the models on a task-by-task basis" / "Validation is, in short, a basic requirement for all publications using LLMs."
- Key point: LLM performance depends heavily on dataset and task, so models must be validated task by task; validation is a basic requirement for every publication that uses LLMs.

### E10

- Location: 4. Validate your model
- Quote: "The validation must take place after the annotation prompt has been finalized: it is not acceptable to use the validation data to improve the prompts, as this may lead to falsely reporting higher precision."
- Key point: Validation must come after the prompt is finalized; using validation data to improve the prompt is not acceptable, as it inflates the reported precision.

### E11

- Location: 4. Validate your model
- Quote: "The practical minimum is to have at least 20-30 samples of each category for a basic level of confidence in the performance metrics, but more is generally better."
- Key point: The validation set needs at least 20–30 samples per category, and more is better.

### E12

- Location: 4. Validate your model
- Quote: "Accuracy – i.e., correct answers divided by total answers – is generally not a sufficient measure to evaluate model performance, as it can be highly misleading, in particular for imbalanced datasets."
- Key point: Accuracy alone is often insufficient and especially misleading with imbalanced classes; justify the choice of metric, often using several together.

### E13

- Location: 4. Validate your model
- Quote: "If your dataset includes several subsets for which the model's capacity may vary, for instance different languages or cultural contexts, they need to be separately validated" / "You should therefore always examine the failures and provide a description of the weaknesses of the model, and why they do not undermine the validity of downstream results."
- Key point: Subsets where the model's ability may differ, such as different languages, must be validated separately; always examine failures and describe the model's weaknesses and why they do not undermine downstream conclusions.

### E14

- Location: 6. Specify your LLM parameters
- Quote: "Your parameters must always be explicitly specified – even if they are the default parameters – as this is necessary for reproducibility."
- Key point: Parameters must always be stated explicitly, even when they are the defaults.

### E15

- Location: 8. Examine model stochasticity
- Quote: "Does the same prompt return the same result for a given text if run several times? Do small variations in the prompt result in different results?" / "To carry out such a prompt stability analysis, create several paraphrases of the prompt, and run the analysis for a subset of the data."
- Key point: Check whether the same prompt gives the same result over several runs and whether small changes to the prompt change the result, by writing several paraphrases of the prompt and running each on a subset of the data.

### E16

- Location: 9. Consider that your data might be in the training data
- Quote: "As the purpose of validating text annotation is to assess the model's capacity for the specific task, it does not matter that the prompt validation data is in the training data, as long as the data on which the model will be run is also in the LLM training data." / "For the same reason, you should try to avoid using publicly available databases to as validation data, as they may be in the model's training data."
- Key point: For annotation, validation data appearing in the training data need not be a problem as long as the data to be annotated is also in it; but avoid using public labeled databases as validation sets, since the model may have seen their labels.

### E17

- Location: 7. Consider ethical and legal implications
- Quote: "Before sending data to a platformed LLM, ensure that all personal data is adequately anonymized or pseudonymized." / "Never send proprietary, secret, or confidential data to an API or web interface without careful consideration of the ethical and legal implications."
- Key point: Anonymize or pseudonymize personal data before sending it to a platform LLM, and never send proprietary or confidential data to an API or web interface without careful thought about the ethical and legal implications.

### E18

- Location: Introduction; Conclusion
- Quote: "we should not reject their use altogether – instead, we should manage their potential weaknesses by bringing them into a rigorous annotation process." / "While critics are largely accurate in describing LLMs as subjective, flawed, black-boxed, potentially biased, and prone to misunderstanding – these descriptions often apply similarly to human coders."
- Key point: The author argues against rejecting LLM annotation outright and for managing its weaknesses within a rigorous annotation process; the critics' charges that LLMs are subjective, flawed, black-boxed, and possibly biased often apply equally to human coders.
