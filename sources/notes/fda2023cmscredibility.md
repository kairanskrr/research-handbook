# 美国 FDA 2023：Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions

- 资料：`fda2023cmscredibility`，[原文（Internet Archive 快照）](https://web.archive.org/web/20260513124224/https://www.fda.gov/media/154985/download)
- 版本：美国食品药品监督管理局（FDA）2023 年 11 月 17 日发布的最终版指南，面向器械企业和 FDA 工作人员。FDA 官网对脚本访问返回 404，本摘录读取的是 Internet Archive 2026-05-13 的快照。位置写章节号和标题。

### E1

- 位置：封面后说明（指南的法律效力）
- 原文："It does not establish any rights for any person and is not binding on FDA or the public."
- 要点：这份指南代表 FDA 当前的想法，对 FDA 和公众都没有约束力。

### E2

- 位置：I. Introduction
- 原文："For the purposes of this guidance, CM&S refers to first principles-based (e.g., physics-based or mechanistic) computational models, and not statistical or data-driven (e.g., machine learning or artificial intelligence-based) models."
- 要点：本指南说的计算建模与仿真，指基于第一性原理（物理或机理）的模型，不包括统计的、数据驱动的模型（如机器学习、人工智能模型）。

### E3

- 位置：II. Background，第 1 类用途
- 原文："Computational models that simulate medical devices can be used to generate information supporting device safety and/or effectiveness (e.g., in silico durability assessment of an implantable stent)."
- 要点：用途之一是"计算机上的器械测试"：用模型模拟器械，为安全性或有效性提供信息，例如在计算机上评估植入式支架的耐久性。

### E4

- 位置：II. Background，第 3 类用途
- 原文："In silico clinical trials are an emerging application of CM&S where device safety and/or effectiveness is evaluated using a ‘virtual cohort’ of simulated patients with anatomical and physiological variability representing the indicated patient population."
- 要点：另一种新兴用途是"计算机上的临床试验"：用一批有解剖和生理差异的模拟病人（"虚拟队列"）来评估器械。

### E5

- 位置：IV. Definitions，Credibility
- 原文："the trust, established through the collection of evidence, in the predictive capability of a computational model for a context of use"
- 要点：可信度的定义：通过收集证据建立起来的、对计算模型在某个使用情境下预测能力的信任。

### E6

- 位置：IV. Definitions，Context of use (COU)
- 原文："a statement that defines the specific role and scope of the computational model used to address the question of interest"
- 要点：使用情境的定义：一段说明，规定计算模型在回答所关心的问题时具体起什么作用、管多大范围。

### E7

- 位置：VI.A.(3) Model risk
- 原文："Model risk is assessed because the level of credibility of a model should be commensurate to the risk associated with using the model to address the question of interest." / "which considers model risk as a combination of two factors, model influence and decision consequence."
- 要点：模型需要多可信，取决于用它回答问题的风险；模型风险由两个因素组合而成：模型对决策的影响有多大、决策错了后果有多严重。

### E8

- 位置：VI.A.(3) Model risk
- 原文："Model influence will be dependent on whether other information (e.g., bench or animal test results) is also provided in the regulatory submission to address the question of interest."
- 要点：如果还有台架试验或动物试验结果一起回答同一个问题，模型的影响就小一些。

### E9

- 位置：VI.B Credibility evidence，开头
- 原文："Verification is focused on the software implementation of a numerical algorithm to solve the underlying mathematical model."
- 要点：验证关注的是求解数学模型的数值算法有没有在软件里正确实现。

### E10

- 位置：VI.B，(2) Model calibration evidence
- 原文："This is not validation evidence because it is not testing of the final model against data independent of model development" / "Calibration evidence is weak in comparison to validation evidence."
- 要点：用拿来调参数的同一批数据去比较，不算确认证据，因为没有用独立于建模过程的数据检验最终模型；校准证据比确认证据弱。

### E11

- 位置：VI.B，(3) Bench test validation results
- 原文："that ‘bench testing’ is a broad term that encompasses in vitro, cadaveric and other types of nonclinical testing"
- 要点："台架试验"是个宽泛的说法，包括体外试验、尸体试验和其他非临床试验。

### E12

- 位置：III. Scope
- 原文："We recommend that manufacturers seek feedback on their specific use of CM&S through the Q-submission process."
- 要点：FDA 建议企业通过"预提交"（Q-submission）程序，就自己具体怎样使用计算建模与仿真征求 FDA 的意见。

### E13

- 位置：IV. Definitions，Validation
- 原文："the process of determining the degree to which a model or a simulation is an accurate representation of the real world"
- 要点：确认的定义：判断模型或仿真在多大程度上准确反映真实世界的过程。
