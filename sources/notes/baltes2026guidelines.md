# Baltes 等 2026：Guidelines for Empirical Studies in Software Engineering involving Large Language Models

- 资料：`baltes2026guidelines`，[原文（arXiv）](https://arxiv.org/abs/2508.15503)，[在线版（llm-guidelines.org）](https://llm-guidelines.org/)
- 版本：arXiv 2508.15503v8（2026-09-18），Empirical Software Engineering 期刊接受稿。22 位软件工程研究者共同制定，在线版持续更新。位置写 arXiv v8 的章节号。
- 说明：面向软件工程研究。把大模型在研究中的用法分成七类研究类型，给出八条设计和报告准则；每条准则区分"必须"（must）和"应当"（should）。

### E1

- 位置：§4 Study Types
- 原文："We use the term study type to refer to categories of LLM involvement in empirical research, rather than to research methodologies (e.g., experiments, case studies). A single empirical study may involve multiple such study types."
- 要点：这里的"研究类型"按大模型在研究里扮演的角色分，不是按研究方法分；一项研究可以同时属于几种类型。

### E2

- 位置：§4.1 LLMs as Tools for Software Engineering Researchers
- 原文："For example, LLMs can perform qualitative coding on natural language text such as interview transcripts (LLMs as Annotators), assess the quality of software artifacts (LLMs as Judges), generate summaries of research papers (LLMs for Synthesis), or simulate human behavior in empirical studies (LLMs as Subjects)." / "However, these applications each pose challenges to validity and reproducibility."
- 要点：大模型可以当研究者的工具：做定性编码（标注员）、评价制品质量（评审员）、汇总文献（综合）、模拟人的行为（被试）；每种用法都给效度和可复现性带来挑战。

### E3

- 位置：§4.2、§4.2.3 Benchmarking LLMs for Software Engineering Tasks
- 原文："Researchers have studied how software engineers use LLMs (Studying LLM Usage), developed new tools that integrate LLMs (LLMs for Tools), and benchmarked LLMs for software engineering tasks (Benchmarking LLMs)." / "Benchmarking studies measure LLM performance on standardized SE tasks against reference outputs and shared metrics."
- 要点：大模型也可以是被研究的对象：研究工程师怎么用大模型、做集成大模型的新工具、在标准任务上评测大模型。评测研究拿参考答案和共同的指标衡量大模型的表现。

### E4

- 位置：§1 Introduction
- 原文："Angermeir et al examined 85 LLM-centric ICSE and ASE 2024 papers [6]. Of the 18 papers that both used OpenAI models and provided artifacts, only five were complete enough to execute, and none fully reproduced the original results"
- 要点：一项调查看了 2024 年两个软件工程顶会的 85 篇以大模型为中心的论文；其中 18 篇用了 OpenAI 模型又提供了制品，只有 5 篇能跑起来，没有一篇完全复现出原来的结果。

### E5

- 位置：§1 Introduction
- 原文："First, their inherent non-determinism causes variability across runs [24, 147], and slight changes can lead to substantially different results [2, 139]. Second, commercial models evolve beyond version identifiers, so reported performance can change over time [33]. Third, even for "open" models, training data and fine-tuning details often remain undisclosed [51]. Moreover, prompt formatting choices alone can shift accuracy by up to 76 percentage points [143]"
- 要点：大模型研究难复现有三个原因：输出不确定，每次运行结果不同；商业模型在版本号之外还在变；连"开放"模型也常不公开训练数据。光是提示词的格式，就能让准确率相差多达 76 个百分点。

### E6

- 位置：§5 Guidelines
- 原文："A must criterion is a requirement. Studies that intend to follow these guidelines are expected to meet all must criteria. A should criterion represents a desired practice that strengthens a study's rigor or transparency. However, there may be valid reasons to deviate in particular circumstances"
- 要点：准则分两级："必须"是硬要求；"应当"是能加强严谨性和透明度的做法，特定情况下可以有正当理由不做。

### E7

- 位置：§5.1 Declare LLM Usage and Role，Summary 与 §5.1.2
- 原文："Researchers must disclose any use of LLMs to support empirical studies, specifying which LLM was used, how it was used, and where in the research process it was employed." / "When a study assigns multiple distinct roles to LLMs (e.g., one model generates evaluation data while another scores outputs), each role should be declared separately."
- 要点：必须声明用了哪个大模型、怎么用、用在研究的哪个环节；一项研究里大模型担任几种角色，就分别声明。

### E8

- 位置：§5.2.2 Recommendations
- 原文："Since default values might change over time, researchers should report all configuration values, even if they used the defaults." / "In summary, researchers must report in the paper at minimum (1) the exact model or tool name and version, (2) all parameters they configured that affect output generation, (3) the date of study execution"
- 要点：论文里至少必须写明确切的模型或工具名称和版本、影响输出的所有参数、做实验的日期；默认值也可能变，所以默认参数也应当写出来。

### E9

- 位置：§5.2.2 Recommendations
- 原文："Commercial models (e.g., GPT-5) or LLM-based tools (e.g., ChatGPT) might not give researchers access to all required information. For these tools, researchers should report what is available and openly acknowledge limitations that hinder reproducibility."
- 要点：商业模型拿不到全部信息时，报告能拿到的部分，并公开承认妨碍复现的局限。

### E10

- 位置：§5.2.5 Challenges
- 原文："Even with a temperature of 0, full determinism is rarely guaranteed." / "Researchers should not treat a temperature of 0 as a guarantee of reproducibility, but as one measure among several, including fixed seed values, system fingerprints, and archiving of raw outputs."
- 要点：把温度设为 0 也很少能保证输出完全确定；它只是多种措施之一，还要固定随机种子、记录系统指纹、存档原始输出。

### E11

- 位置：§5.3.2 Recommendations，Prompt Reporting 与 Prompt Development
- 原文："Researchers must report all prompts used in an empirical study, including instructions, task context, input data, and output indicators." / "Because prompt effectiveness varies between models and model versions, researchers must make clear which prompts were used for which models in which versions and with which configuration."
- 要点：必须报告研究里用到的全部提示词，并说清哪条提示词用在哪个模型、哪个版本、什么配置上。

### E12

- 位置：§5.3.2 Recommendations，Prompting Strategy and Input Handling
- 原文："Researchers must specify whether zero-shot, one-shot, or few-shot prompting was used. For few-shot prompts, researchers must explain in the paper how the examples were selected" / "If multiple versions of a prompt were tested, researchers should describe how these variations were evaluated and how the final design was chosen."
- 要点：必须说明给了几个示例（零样本、单样本、少样本）以及示例怎么挑的；试过多个版本的提示词，应当说明怎样比较、怎样选定最终版本。

### E13

- 位置：§5.3.1 Rationale
- 原文："Sclar et al question the methodological validity of comparing models with "an arbitrarily chosen, fixed prompt format", because their research has shown that the performance of different prompt formats only weakly correlates between different models"
- 要点：不同提示词格式的表现在不同模型之间只有弱相关，所以只用一个随意选定的固定格式比较模型，方法上站不住。

### E14

- 位置：§5.4.1 Rationale、§5.4.4 Benefits
- 原文："Just as a human participant might give different answers to the same question asked two months apart, the responses from tools such as ChatGPT can also vary over time" / "Unlike human participant conversations, which often cannot be reported because of confidentiality, LLM interaction logs can be shared. This enables reproduction studies, tracking of response changes over time or across model versions, and secondary research on LLM consistency for specific SE tasks."
- 要点：大模型的回答会随时间变化，就像人隔两个月回答同一个问题会不同。和人的访谈记录不同，大模型的交互记录（发出的提示词和收到的回答）可以公开，便于复现、追踪变化和二次研究。

### E15

- 位置：§5.5.2 Recommendations
- 原文："Furthermore, researchers should check whether a less resource-intensive approach (e.g., for static analysis tasks or program repair) can serve as a baseline." / "Even if LLM-based tools outperform baselines, researchers should discuss whether the resources consumed justify the (often marginal) improvements"
- 要点：应当检查有没有更省资源的传统方法（例如静态分析）可以当基线；即使大模型更好，也要讨论消耗的资源值不值得那点（往往不大的）提升。

### E16

- 位置：§5.5.2 Recommendations
- 原文："Due to LLM non-determinism, researchers should repeat experiments and report descriptive statistics of model or tool performance (e.g., arithmetic mean, median, confidence intervals, standard deviations)" / "If comparing models or tools, researchers should use appropriate inferential statistics with effect sizes rather than relying solely on differences in means or other summary statistics."
- 要点：因为输出不确定，应当重复实验，报告均值、中位数、置信区间、标准差；比较模型或工具时，用推断统计和效应量，不要只比平均数。

### E17

- 位置：§5.5.2 Recommendations
- 原文："researchers should justify their chosen number of repetitions, for example, through a power analysis or by monitoring the convergence of descriptive statistics across incremental runs. A pilot study can help estimate the expected variability and inform this decision."
- 要点：重复几次要有理由，例如做功效分析，或者一边加跑次一边看统计量是否稳定下来；预实验可以帮你估计波动有多大。

### E18

- 位置：§5.5.2 Recommendations
- 原文："Prior adoption alone does not constitute sufficient justification; researchers must not justify metric choices solely by citing their use in prior work."
- 要点：不能只用"前人用过"来说明为什么选这个指标。

### E19

- 位置：§5.5.2 Recommendations
- 原文："After running a benchmark, researchers should perform an error analysis by categorizing the failures observed and reporting the relative frequency of each category."
- 要点：跑完评测，应当做错误分析：把失败的情况分类，报告每类占多少。

### E20

- 位置：§5.5.2 Recommendations
- 原文："maintaining a held-out subset of items for ongoing, uncontaminated evaluation; embedding canary strings, that is, unique markers that downstream tools can later search for in model outputs to detect inclusion in training data" / "Researchers using existing benchmarks should additionally discuss contamination as a study limitation"
- 要点：建新评测集时，留一部分不公开的题目持续用于未污染的评测；嵌入"金丝雀字符串"（独特标记，日后能据此查出评测集是否进了训练数据）。用现成评测集的，要把污染写进局限。

### E21

- 位置：§5.5.5 Challenges
- 原文："To mitigate contamination, researchers can create new benchmark datasets by collecting data after a specified cutoff date; researchers must disclose data sources and collection dates for each release. However, this temporal approach requires continuous updates as new models may include the benchmark in future training data."
- 要点：可以只收集某个截止日期之后的数据来建评测集，并公开数据来源和收集日期；但新模型会把这些数据也学进去，所以要不断更新。

### E22

- 位置：§5.5.5 Challenges
- 原文："In a survey of 572 code benchmarks released between 2014 and 2025, Cao et al found that 84.2% did not consider test suite coverage when constructing test cases, 64.0% reported single-pass evaluations without controlling for randomness, and 82.5% did not address data contamination"
- 要点：一项对 572 个代码评测集的调查发现：64.0% 只跑一次、不控制随机性；82.5% 没有处理数据污染。

### E23

- 位置：§5.6 Use an Open LLM as a Baseline，Summary 与 §5.6.4 Benefits
- 原文："When researchers can control which LLM a study uses, they should include an open-weight LLM, ideally an open-source LLM, as a baseline and report inter-model agreement." / "Unlike proprietary alternatives, which can be withdrawn or silently updated, open LLMs remain available for future studies."
- 要点：能自己选模型时，应当加一个开放权重的模型（最好是开源模型）作基线。商业模型可能下线或悄悄更新，开放模型以后还能用。

### E24

- 位置：§5.6.2 Recommendations
- 原文："An open-weight LLM has publicly released trained weights, so others can fine-tune, adapt, or deploy the model" / "Open-source LLMs are preferable, because researchers can check their training data for benchmark contamination" / "We acknowledge that including an open LLM baseline might not always be possible, for example, if the study involves human participants, and letting them work on the tasks using two different models might not be feasible. Using an open model as a baseline is also not necessary if the use of the LLM is tangential to the study goal."
- 要点：开放权重的模型公开了训练好的参数，别人可以自己部署和改造。开源模型更好，因为可以查它的训练数据里有没有评测集。有人参与、无法让人用两个模型做任务时，或者大模型只是研究中的次要环节时，可以不加开放模型基线。

### E25

- 位置：§5.7.2 Recommendations，Replacing Human Judgment
- 原文："In such cases, researchers must explain whether and how the replacement is justified" / "High inter-model agreement can reflect shared model biases rather than valid annotation, so researchers should additionally validate a sample against human experts before treating LLM outputs as a substitute for human work"
- 要点：用大模型代替人做标注、编码或当被试时，必须说明这种代替是否合理。几个模型彼此一致，可能只是有共同的偏差，应当再抽一部分和人类专家的判断对照。

### E26

- 位置：§5.7.2 Recommendations，Subjective Judgment and Agreement
- 原文："Krippendorff recommends discarding data with α < 0.667, considers 0.667 ≤ α < 0.8 sufficient only for tentative conclusions, and requires α ≥ 0.8 for reliable data"
- 要点：按 Krippendorff 的标准，一致性系数 α 低于 0.667 的数据应丢弃；0.667 到 0.8 之间只够得出初步结论；0.8 以上才算可靠。

### E27

- 位置：§4.3 Advantages and Challenges
- 原文："No compelling evidence exists that LLMs can accurately simulate human participants or reliably judge most relevant properties of SE artifacts." / "LLMs may be better suited for augmenting rather than replacing human researchers"
- 要点：目前没有令人信服的证据表明大模型能准确模拟人类参与者，或可靠地评判软件制品的大多数性质；大模型可能更适合辅助研究者，而不是取代。

### E28

- 位置：§4.3 Advantages and Challenges
- 原文："Crucially, reliability does not imply validity: a reliable LLM might be reliably inaccurate"
- 要点：信度不等于效度：一个大模型可能每次都稳定地给出同样的错误答案。

### E29

- 位置：§4.3 Advantages and Challenges
- 原文："In a recent open letter, 419 experienced qualitative researchers argued "that analytic approaches such as reflexive thematic analysis are human research practices requiring a subjective, positioned, and reflexive researcher and therefore the use of GenAI in such approaches is not methodologically congruent""
- 要点：419 位定性研究者在公开信中认为，反思性主题分析等方法需要有立场、能反思的研究者本人，用生成式人工智能做这类分析在方法上不相容。

### E30

- 位置：§5.8.2 Recommendations，External Validity
- 原文："Mitigations include triangulation across multiple models (e.g., proprietary and open), independent datasets, and complementary metrics; sensitivity analysis that varies LLM configurations, prompts, architecture decisions, datasets, and where applicable participant backgrounds; and performing longitudinal re-runs"
- 要点：减轻外部效度威胁的办法：在多个模型（商业和开放）、独立数据集、互补指标之间相互印证；改变配置、提示词、数据集等做敏感性分析；隔一段时间重跑。

### E31

- 位置：§5.8.2 Recommendations，Internal Validity
- 原文："Evaluation data entering model-improvement pipelines: Evaluation samples can unintentionally feed retraining or fine-tuning, especially in longitudinal studies involving LLMs." / "As transparency on training data is limited for LLMs, researchers must discuss potential data leakage effects and their impact on results."
- 要点：因为训练数据不透明，必须讨论可能的数据泄露及其对结果的影响；评测样本还可能被无意中用于模型的再训练，长期研究尤其要注意。

### E32

- 位置：§5.8.2 Recommendations，Environmental & Sustainability Constraints
- 原文："Researchers should justify the LLM's resource consumption against the benefits over traditional approaches." / "Cost accounting tracks resource consumption by reporting tokens, service costs, or hardware specifications."
- 要点：应当拿相对传统方法的好处，来说明大模型消耗的资源值得；成本核算可以报告词元（token）数量、服务费用或硬件配置。

### E33

- 位置：§5.8.2 Recommendations，Reliability & Reproducibility
- 原文："Researchers must discuss the measures taken to increase reliability and reproducibility. However, non-deterministic reproducibility is not inherently disqualifying."
- 要点：必须讨论为提高信度和可复现性做了什么；但结果不能逐字复现，本身不构成否定研究的理由。

### E34

- 位置：§4.3 Advantages and Challenges
- 原文："LLMs can annotate, judge, synthesize, and simulate faster and at lower cost than human researchers, with studies showing cost reductions of 50–96% on various natural language tasks [160] (e.g., He et al found that GPT-4 annotation required only two days and 122.08 USD compared to several weeks and 4,508 USD for a comparable MTurk pipeline [61])."
- 要点：大模型做标注、评判等比人快、便宜，已有研究报告成本降低 50%–96%；一个例子是用 GPT-4 标注花了两天、122.08 美元，同类众包流程要几周、4508 美元。

### E35

- 位置：§2 Scope and Conventions，Related Reporting Guidelines
- 原文："We target SE research because reporting guidelines from other disciplines do not address its specific needs" / "Outside SE, these include Gallifant et al's TRIPOD-LLM for healthcare [48], Navarro et al's HCI guidelines [104], and Kapoor et al's REFORMS for ML-based science [76]."
- 要点：这份准则面向软件工程；软件工程以外，医疗（TRIPOD-LLM）、人机交互、基于机器学习的科学（REFORMS）各有自己的大模型报告规范。

### E36

- 位置：§5.2.3 Examples
- 原文："We integrated a gpt-4 model in version 0125-Preview via the Azure OpenAI Service, and configured it with a temperature of 0.7, top_p set to 0.8, a maximum token length of 512, and the seed value 23487. We ran our experiment on 10th January 2025. The system fingerprint was fp_6b68a8204b."
- 要点：一段合格的模型报告示例：模型名和版本、接入渠道、温度、top_p、最大长度、随机种子、实验日期、系统指纹。

### E37

- 位置：§5.5.2 Recommendations
- 原文："Benchmark scores often confound the target capability with unrelated capabilities the task happens to require." / "More broadly, output format compliance (e.g., specific JSON schemas or unit-test conventions) and general instruction-following capability are routinely bundled into the aggregate benchmark score"
- 要点：评测分数常把要测的能力和不相干的能力混在一起，例如能不能按要求的格式输出、能不能听懂指令。

### E38

- 位置：§5.7.2 Recommendations，Subjective Judgment and Agreement；§4.3
- 原文："When the judgment is subjective (i.e., depends on the judge's values or theories), the same artifacts should be judged independently by both the LLM and a panel of human experts, and the LLM judgments should then be compared against an aggregated human reference." / "However, both human and LLM judges exhibit systematic biases, such as preferring outputs with fake citations or rich formatting"
- 要点：主观判断应当让大模型和一组人类专家各自独立评判同一批对象，再拿大模型的判断和汇总后的人类判断比较。人和大模型当评审都有系统偏差，例如偏爱带假引用或排版花哨的回答。

### E39

- 位置：§5.7.6 Study Types
- 原文："For Benchmarking LLMs, there is less need for human validation when using extensively validated and widely-used benchmarks, but researchers should employ human validation when creating or adapting new benchmarks."
- 要点：用经过充分验证、广泛使用的评测集时，不太需要人工验证；新建或改编评测集时应当做人工验证。
