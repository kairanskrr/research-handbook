# Sallou 等 2024：Breaking the Silence: the Threats of Using LLMs in Software Engineering

- 资料：`sallou2024breaking`，[原文（arXiv）](https://arxiv.org/abs/2312.08055)
- 版本：ICSE-NIER 2024（新想法与新成果分会，第 102–106 页），DOI 10.1145/3639476.3639764；读的是 arXiv 2312.08055v2（2024-01-08）。位置写章节号。
- 说明：软件工程的短论文，讨论用大模型做研究时的三类效度威胁：闭源模型、隐性的数据泄露、可复现性，并给研究者和模型提供方提出建议，用 ChatGPT 为 Defects4J 中两个有缺陷的程序生成测试作示范。

### E1

- 位置：§1 Introduction
- 原文："Although ChatGPT3.5, as a general-purpose chatbot, is not fine-tuned for specific SE tasks, it possesses precise knowledge of the bugs within these projects (see Figure 1). Thus, when OpenAI models are employed for tasks like patch generation, fault localization, or test generation for Defects4J, they have superior performance compared to an unknown code."
- 要点：ChatGPT 对缺陷数据集 Defects4J 里的缺陷了如指掌，所以在这个数据集上做修复、定位、测试生成，表现比在没见过的代码上好。

### E2

- 位置：§2.1 Closed-Source Models，Model Evolution Unpredictability
- 原文："Such changes can occur during or after the research approach has been presented, potentially making the presented results obsolete." / "Indeed, distinguishing whether the improvements claimed in the new contribution are the result of changes to the LLMs' models or due to the novelty of the contribution becomes a complex task."
- 要点：闭源模型会在研究进行中或发表后发生变化，使结果过时；在前人基础上改进的工作，很难分清提升来自自己的新方法还是模型本身变了。

### E3

- 位置：§2.2 Implicit Data Leakage，Data leakage due to pre-training
- 原文："They reported remarkable performance discrepancies between the HumanEval (>69% branch coverage) and the SF110 (2% branch coverage) datasets. We remark that the former is available on GitHub while the latter is not (available on SourceForge instead)."
- 要点：同样是生成单元测试，大模型在放在 GitHub 上的 HumanEval 上分支覆盖率超过 69%，在放在 SourceForge 上的 SF110 上只有 2%。

### E4

- 位置：§2.2 Implicit Data Leakage，Data leakage due to fine-tuning
- 原文："Consequently, a scenario of data leakage can arise if the LLM is trained on "project A" that employs a specific API, and the resulting model is subsequently used to fix the usage of the same API in another project within the test set."
- 要点：即使训练集和测试集按项目分开，不同项目共用的依赖和接口也会造成泄露。

### E5

- 位置：§2.3 Reproducibility，Output Variability
- 原文："LLMs exhibit variability in their outputs, even when using identical input. Running the same prompt several times may not result in identical output, rendering the usage of LLMs non-deterministic."
- 要点：同样的输入，大模型的输出也会不同；同一条提示词跑几次，结果不一定一样。

### E6

- 位置：§2.3 Reproducibility，Time-Based Output Drift
- 原文："In particular, for code generation, the mismatch is evaluated at 20% for GPT-3.5 and 50% for GPT-4 between March 2023 and June 2023. Moreover, the number of executable outputs drops from 52% to 10% for GPT-3.5, and from 22% to 2% for GPT-4.0 for the same period."
- 要点：引用的研究发现，2023 年 3 月到 6 月之间，GPT-4 生成代码的答案有 50% 变了，能直接运行的输出从 22% 降到 2%。

### E7

- 位置：§3.2.1 Reproducibility，Assess output variability
- 原文："Due to output variability, running the LLMs' inference only once is insufficient to ensure reproducibility. Therefore, we argue in favor of conducting multiple replication runs and using variability metrics during the evaluation." / "For our showcase example, we queried ChatGPT3.5 ten times over different days using the same prompts" / "For Math-5, we report an average branch coverage of 70% for the tested Java method with a large variability (interquartile range or IQR) of 27.5%."
- 要点：只跑一次不够，要多次重复并报告波动指标；示范中用同样的提示词在不同日子查询十次，平均分支覆盖率 70%，四分位距高达 27.5%。

### E8

- 位置：§3.2.1 Reproducibility，Provide execution metadata
- 原文："(ii) Prompts: The exact inputs (queries) used for the inference and evaluation of the LLMs. (iii) Date of LLMs query: The date is relevant data to share to address the time-based output drift"
- 要点：要公开的执行元数据包括模型信息、确切的提示词、查询日期（用来应对输出随时间漂移）、波动指标和评估包。

### E9

- 位置：§3.2.2 Data Leakage，Assess LLMs on metamorphic data
- 原文："These new snippets maintain semantic and behavioral equivalence with the original code, yet exhibit structural differences (e.g., distinct Abstract Syntax Trees)." / "Therefore, we advise researchers to complement the analysis of the LLMs performance with new data samples generated with metamorphic testing. The selection of metamorphic transformations should align with the specific task at hand."
- 要点：建议用"蜕变"改写生成新样本：改写后的代码语义和行为不变，但结构不同；用它们补充评测。选哪种改写要看任务。

### E10

- 位置：§3.2.2 Data Leakage，Assess LLMs on metamorphic data
- 原文："In particular, we (1) removed the javadoc and (2) renamed the method under test and its input parameters." / "While ChatGPT constantly generated tests for the original program with a branch coverage of 71%, it struggled to generate any meaningful tests on the transformed code."
- 要点：示范中只是删掉文档注释、给方法和参数换名，ChatGPT 在原程序上稳定达到 71% 覆盖率，在改写后的程序上却几乎生成不出有意义的测试。

### E11

- 位置：§3.2.2 Data Leakage，Use different sources；Code clone detection
- 原文："Hence, we recommend researchers gather software projects and data from multiple sources." / "However, researchers can use well-established code clone detection techniques to check if the generated code (e.g., test cases) is similar to code seen in online repositories (e.g., manually-written test cases)."
- 要点：建议从多个来源收集数据；可以用代码克隆检测，看模型生成的代码是否和网上已有的代码相似。
