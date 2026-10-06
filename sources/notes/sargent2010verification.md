# Sargent 2010：Verification and Validation of Simulation Models

- 资料：`sargent2010verification`，[原文（Winter Simulation Conference 论文集，informs-sim.org 开放获取）](https://www.informs-sim.org/wsc10papers/016.pdf)
- 版本：Proceedings of the 2010 Winter Simulation Conference，第 166—183 页。作者称这篇教程与 2009 年版相近；同题教程在 WSC 上多次更新。

### E1

- 位置：§1 Introduction
- 原文："Model verification is often defined as “ensuring that the computer program of the computerized model and its implementation are correct” and is the definition adopted here. Model validation is usually defined to mean “substantiation that a computerized model within its domain of applicability possesses a satisfactory range of accuracy consistent with the intended application of the model”"
- 要点：验证（verification）是确保模型的程序及其实现是正确的；确认（validation）是证实模型在适用范围内，精度足以满足预期用途。

### E2

- 位置：§1 Introduction
- 原文："A model should be developed for a specific purpose (or application) and its validity determined with respect to that purpose." / "A model may be valid for one set of experimental conditions and invalid in another."
- 要点：模型应为特定目的而建，其有效性也针对这个目的来判断；一个模型在一组实验条件下有效，换一组条件可能无效。

### E3

- 位置：§1 Introduction
- 原文："The amount of accuracy required should be specified prior to starting the development of the model or very early in the model development process."
- 要点：模型需要多高的精度，应在开始建模前或建模早期就定下来。

### E4

- 位置：§1 Introduction
- 原文："It is often too costly and time consuming to determine that a model is absolutely valid over the complete domain of its intended applicability. Instead, tests and evaluations are conducted until sufficient confidence is obtained that a model can be considered valid for its intended application"
- 要点：证明模型在整个适用范围内绝对有效通常代价太大；实际做法是不断测试和评估，直到有足够信心认为它适合预期用途。

### E5

- 位置：§3 Paradigms
- 原文："Conceptual model validation is defined as determining that the theories and assumptions underlying the conceptual model are correct and that the model representation of the problem entity is “reasonable” for the intended purpose of the model. Computerized model verification is defined as assuring that the computer programming and implementation of the conceptual model is correct."
- 要点：概念模型确认：检查模型依据的理论和假设是否正确、对真实对象的表示是否合理；计算机模型验证：检查概念模型的编程实现是否正确。

### E6

- 位置：§3 Paradigms
- 原文："Operational validation is defined as determining that the model’s output behavior has sufficient accuracy for the model’s intended purpose over the domain of the model’s intended applicability." / "Data validity is defined as ensuring that the data necessary for model building, model evaluation and testing, and conducting the model experiments to solve the problem are adequate and correct."
- 要点：运行确认：检查模型输出在适用范围内是否足够准确；数据有效性：确保建模、评估测试和做实验所需的数据充分且正确。

### E7

- 位置：§3 Paradigms
- 原文："Verification and validation must be performed again when any model change is made. Usually several models are developed prior to obtaining a valid simulation model."
- 要点：模型任何改动之后都要重新验证和确认；通常要建好几版模型才能得到一个有效的模型。

### E8

- 位置：§4 Validation Techniques
- 原文："Degenerate Tests: The degeneracy of the model’s behavior is tested by appropriate selection of values of the input and internal parameters. For example, does the average number in the queue of a single server continue to increase over time when the arrival rate is larger than the service rate?" / "Extreme Condition Tests: The model structure and outputs should be plausible for any extreme and unlikely combination of levels of factors in the system."
- 要点：退化测试：选取特定参数值检验模型行为，例如到达率大于服务率时，单服务台队列的平均长度是否持续增长；极端条件测试：在极端、不太可能的因素组合下，模型结构和输出也应合理。

### E9

- 位置：§4 Validation Techniques
- 原文："Comparison to Other Models: Various results (e.g., outputs) of the simulation model being validated are compared to results of other (valid) models. For example, (1) simple cases of a simulation model are compared to known results of analytic models"
- 要点：与其他模型比较：把模型的结果和其他有效模型的结果比较，例如把仿真模型的简单情形和解析模型的已知结果对照。

### E10

- 位置：§4 Validation Techniques
- 原文："Face Validity: Individuals knowledgeable about the system are asked whether the model and/or its behavior are reasonable." / "Historical Data Validation: If historical data exist (e.g., data collected on a system specifically for building and testing a model), part of the data is used to build the model and the remaining data are used to determine (test) whether the model behaves as the system does."
- 要点：表面效度：请了解该系统的人判断模型及其行为是否合理；历史数据确认：用一部分历史数据建模，用剩下的数据检验模型行为是否与系统一致。

### E11

- 位置：§4 Validation Techniques
- 原文："Parameter Variability - Sensitivity Analysis: This technique consists of changing the values of the input and internal parameters of a model to determine the effect upon the model’s behavior or output. The same relationships should occur in the model as in the real system." / "Those parameters that are sensitive, i.e., cause significant changes in the model’s behavior or output, should be made sufficiently accurate prior to using the model."
- 要点：敏感性分析：改变模型的输入参数和内部参数，看对输出的影响；模型中的关系应与真实系统一致。对输出影响大的敏感参数，使用模型前要把它们弄得足够准确。

### E12

- 位置：§4 Validation Techniques
- 原文："Internal Validity: Several replications (runs) of a stochastic model are made to determine the amount of (internal) stochastic variability in the model."
- 要点：（Sargent 所说的"内部效度"技术）对随机模型做多次重复运行，确定模型内部随机波动有多大。

### E13

- 位置：§5 Data Validity
- 原文："data problems are often the reason that attempts to valid a model fail." / "If behavior data are not available, high model confidence usually cannot be obtained because sufficient operational validity cannot be achieved."
- 要点：模型确认失败常常是因为数据有问题；没有系统的行为数据，通常无法对模型有很高的信心。

### E14

- 位置：§7 Computerized Model Verification
- 原文："In dynamic testing the computer program is executed under different conditions and the values obtained (including those generated during the execution) are used to determine if the computer program and its implementations are correct."
- 要点：动态测试：在不同条件下运行程序，用得到的值（包括运行中产生的中间值）判断程序及其实现是否正确。

### E15

- 位置：§8 Operational Validity
- 原文："Thus if a system is not observable, which is often the case, it is usually not possible to obtain a high degree of confidence in the model. In this situation the model output behavior(s) should be explored as thoroughly as possible and comparisons made to other valid models whenever possible."
- 要点：系统无法观测（拿不到它的运行数据）的情况很常见，这时通常无法对模型有很高的信心；应尽可能充分地探索模型输出行为，并尽量和其他有效模型比较。

### E16

- 位置：§8.2 Comparisons of Output Behaviors
- 原文："It is preferable to use confidence intervals or hypothesis tests for the comparisons because these allow for objective decisions." / "As a result, the use of graphs is the most commonly used approach for operational validity."
- 要点：比较模型和系统的输出时，最好用置信区间或假设检验，因为它们能做出客观判断；但由于统计假设难满足、系统数据不足，实践中最常用的是画图比较。

### E17

- 位置：§8.2.3 Hypothesis Tests
- 原文："The first, or type I error, is rejecting the validity of a valid model and the second, or type II error, is accepting the validity of an invalid model." / "In model validation, the model user’s risk is extremely important and must be kept small."
- 要点：确认模型时有两类错误：把有效模型判为无效，把无效模型判为有效。后者（模型使用者的风险）极其重要，必须控制得很小。

### E18

- 位置：§9 Documentation
- 原文："Documentation on model verification and validation is usually critical in convincing users of the “correctness” of a model and its results, and should be included in the simulation model documentation."
- 要点：验证与确认的记录对于让使用者相信模型及其结果"正确"通常至关重要，应写进模型文档。

### E19

- 位置：§10 Recommended Procedure
- 原文："3. Test, wherever possible, the assumptions and theories underlying the simulation model. 4. In each model iteration, at least perform face validity on the conceptual model. 5. In each model iteration, at least explore the simulation model’s behavior using the computerized model. 6. In at least the last model iteration, make comparisons, if possible, between the simulation model and system behavior (output) data for at least a few sets of experimental conditions, and preferably for several sets."
- 要点：Sargent 推荐的最低步骤之一部分：尽可能检验模型依据的假设和理论；每轮迭代至少对概念模型做表面效度检查、至少探索计算机模型的行为；至少在最后一轮，把模型输出和系统实际数据在几组实验条件下对比。

### E20

- 位置：§3 Paradigms
- 原文："Verification and validation must be performed again when any model change is made."
- 要点：模型任何改动之后都要重新验证和确认。
