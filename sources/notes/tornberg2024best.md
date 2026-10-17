# Törnberg 2024：Best Practices for Text Annotation with Large Language Models

- 资料：`tornberg2024best`，[原文（arXiv）](https://arxiv.org/abs/2402.05129)
- 版本：arXiv 2402.05129（2024-02-05）。作者在阿姆斯特丹大学，面向社会科学中把文本当数据的研究。PDF 没有章节号，位置写文中编号的小标题。
- 说明：社会科学方向。为用大模型做文本标注（给文本打类别标签）提出最佳实践：选模型、系统的编码流程、提示词编码手册、验证、提示词设计、参数、伦理、随机性、训练数据。

### E1

- 位置：Introduction
- 原文："LLM-based text annotation has become something of an academic Wild West, as the lack of established standards has meant that both researchers and reviewers lack benchmarks for LLM-based annotation, leading to risks of low-quality research and the publishing of invalid results."
- 要点：大模型文本标注缺少公认标准，研究者和审稿人都没有可以对照的尺子，容易出现低质量研究和无效结果。

### E2

- 位置：1. Choose an appropriate model
- 原文："First, the ChatGPT models have been shown to change over time without notice, giving different results to the same instructions as a result to changes in the backend" / "While the API provides access to stable models, these are deprecated after a relatively short time, making reproducibility an impossibility."
- 要点：ChatGPT 的模型会在不通知的情况下变化，同样的指令给出不同结果；接口提供的固定版本过不久就会下线，使复现变得不可能。

### E3

- 位置：1. Choose an appropriate model
- 原文："The choice of model should be explicitly argued for" / "To ensure reproducibility, use a fixed version of the LLM throughout the project, document the version, and ensure that the model will be available for future use."
- 要点：选哪个模型要明确说出理由；整个项目用同一个固定版本，记下版本，并确保这个模型以后还能用。

### E4

- 位置：1. Choose an appropriate model
- 原文："Ideal practice also involves assessing whether your results can be reproduced using several models, thereby showing that the prompt and results are robust to details of implementation. You should in general never use LLMs for annotation through their web interface, as these interfaces do not allow setting parameters, version control, and do not provide sufficient privacy or copyright provision"
- 要点：理想做法是看换几个模型结果是否还成立；一般不要通过网页聊天界面做标注，因为不能设参数、不能控制版本，隐私和版权也没有保障。

### E5

- 位置：2. Follow a Systematic Coding Procedure
- 原文："Define the concept: It is important to come in with an explicitly articulated idea of the concept you are trying to capture, to avoid being overly influenced by the interpretations of the LLM."
- 要点：先把要标注的概念明确写下来，避免被大模型的理解牵着走。

### E6

- 位置：2. Follow a Systematic Coding Procedure
- 原文："Once the LLM reached sufficient agreement with the human coders, it can be used to code the full material." / "Ideally, the LLM should approach the reliability achieved among the human coders."
- 要点：在小样本上让人和大模型一起标注、比较分歧、修改编码手册和提示词，直到大模型和人足够一致，再用它标注全部材料；理想情况下，大模型应接近人与人之间的一致程度。

### E7

- 位置：2. Follow a Systematic Coding Procedure
- 原文："The human coders should not be considered ground truth: you may find that the LLM's interpretation was superior to the human coder."
- 要点：人工标注也不是绝对正确的标准答案，有时大模型的理解反而更好。

### E8

- 位置：3. Develop a Prompt Codebook
- 原文："Note that the prompt should be considered tailored to the model used for its development: applying the same prompt to a different LLM may produce different results, even with models of similar parameter size"
- 要点：提示词是针对开发时用的模型调出来的，换一个模型，即使规模相近，结果也可能不同。

### E9

- 位置：4. Validate your model
- 原文："Hence, it is always necessary to carefully validate the models on a task-by-task basis" / "Validation is, in short, a basic requirement for all publications using LLMs."
- 要点：大模型的表现高度依赖数据集和任务，必须逐个任务验证；验证是所有使用大模型的论文的基本要求。

### E10

- 位置：4. Validate your model
- 原文："The validation must take place after the annotation prompt has been finalized: it is not acceptable to use the validation data to improve the prompts, as this may lead to falsely reporting higher precision."
- 要点：验证必须在提示词定稿之后做；不能用验证数据改提示词，否则会虚报更高的精度。

### E11

- 位置：4. Validate your model
- 原文："The practical minimum is to have at least 20-30 samples of each category for a basic level of confidence in the performance metrics, but more is generally better."
- 要点：验证集里每个类别至少要有 20–30 个样本，越多越好。

### E12

- 位置：4. Validate your model
- 原文："Accuracy – i.e., correct answers divided by total answers – is generally not a sufficient measure to evaluate model performance, as it can be highly misleading, in particular for imbalanced datasets."
- 要点：只看准确率往往不够，类别不平衡时尤其容易误导；要说明为什么选这个指标，常常要几个指标一起看。

### E13

- 位置：4. Validate your model
- 原文："If your dataset includes several subsets for which the model's capacity may vary, for instance different languages or cultural contexts, they need to be separately validated" / "You should therefore always examine the failures and provide a description of the weaknesses of the model, and why they do not undermine the validity of downstream results."
- 要点：模型能力可能不同的子集（例如不同语言）要分别验证；总要检查失败的样本，说明模型的弱点，以及为什么它们不影响后续分析的结论。

### E14

- 位置：6. Specify your LLM parameters
- 原文："Your parameters must always be explicitly specified – even if they are the default parameters – as this is necessary for reproducibility."
- 要点：参数必须写明，即使用的是默认值。

### E15

- 位置：8. Examine model stochasticity
- 原文："Does the same prompt return the same result for a given text if run several times? Do small variations in the prompt result in different results?" / "To carry out such a prompt stability analysis, create several paraphrases of the prompt, and run the analysis for a subset of the data."
- 要点：检查同一条提示词多跑几次结果是否一样、稍改提示词结果是否变化；做法是写几种意思相同的提示词，在一部分数据上分别运行、比较。

### E16

- 位置：9. Consider that your data might be in the training data
- 原文："As the purpose of validating text annotation is to assess the model's capacity for the specific task, it does not matter that the prompt validation data is in the training data, as long as the data on which the model will be run is also in the LLM training data." / "For the same reason, you should try to avoid using publicly available databases to as validation data, as they may be in the model's training data."
- 要点：做标注时，验证数据在训练数据里不一定是问题，只要正式标注的数据也同样在里面；但不要用公开的已标注数据库当验证集，模型可能已经见过这些标签。

### E17

- 位置：7. Consider ethical and legal implications
- 原文："Before sending data to a platformed LLM, ensure that all personal data is adequately anonymized or pseudonymized." / "Never send proprietary, secret, or confidential data to an API or web interface without careful consideration of the ethical and legal implications."
- 要点：把数据发给平台上的大模型之前，先把个人信息匿名化；没有仔细考虑伦理和法律问题，不要把专有、保密的数据发给接口或网页。

### E18

- 位置：Introduction；Conclusion
- 原文："we should not reject their use altogether – instead, we should manage their potential weaknesses by bringing them into a rigorous annotation process." / "While critics are largely accurate in describing LLMs as subjective, flawed, black-boxed, potentially biased, and prone to misunderstanding – these descriptions often apply similarly to human coders."
- 要点：作者认为不应全盘拒绝大模型标注，而应把它纳入严格的标注流程来管住它的弱点；批评者说大模型主观、有缺陷、像黑箱、可能有偏差，这些往往同样适用于人类编码者。
