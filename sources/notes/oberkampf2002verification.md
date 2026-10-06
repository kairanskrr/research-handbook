# Oberkampf 与 Trucano 2002：Verification and Validation in Computational Fluid Dynamics

- 资料：`oberkampf2002verification`，[原文](https://www.osti.gov/servlets/purl/793406)
- 版本：美国桑迪亚国家实验室报告 SAND2002-0529（Unlimited Release，2002 年 3 月），美国能源部科技信息办公室（OSTI）免费提供。位置写章节号。

### E1

- 位置：1.1 Background
- 原文："Briefly, verification is the assessment of the accuracy of the solution to a computational model by comparison with known solutions. Validation is the assessment of the accuracy of a computational simulation by comparison with experimental data."
- 要点：验证（verification）是拿已知解来检查计算模型的解有多准；确认（validation）是拿实验数据来检查仿真有多准。

### E2

- 位置：1.1 Background
- 原文："Stated differently, verification is primarily a mathematics issue; validation is primarily a physics issue"
- 要点：验证主要是数学问题，确认主要是物理问题。

### E3

- 位置：2.1 Development of Terminology for Verification and Validation
- 原文："Validation: The process of determining the degree to which a model is an accurate representation of the real world from the perspective of the intended uses of the model."
- 要点：AIAA 采用的定义：确认是判断模型从预期用途来看在多大程度上准确地代表了真实世界。

### E4

- 位置：2.1 Development of Terminology for Verification and Validation
- 原文："Thus, V&V activities can only assess the correctness or accuracy of the specific cases tested."
- 要点：验证与确认只能评估测试过的那些具体情况是否正确、准确。

### E5

- 位置：4.1 Fundamentals of Validation
- 原文："In other words, calibration, or parameter estimation, is a response to obtain needed agreement between the computational results and the experimental data."
- 要点：校准（calibration，也叫参数估计）是为了让计算结果和实验数据吻合而做的调整，作者强调要把它和确认区分开。

### E6

- 位置：4.3 Guidelines for Validation Experiments，Guideline 1
- 原文："A validation experiment should be jointly designed by experimentalists, model developers, code developers, and code users working closely together throughout the program, from inception to documentation, with complete candor about the strengths and weaknesses of each approach."
- 要点：用于确认的实验，应由做实验的人、建模的人、写代码的人和用代码的人从头到尾一起设计，坦率说明各自方法的长处和短处。

### E7

- 位置：4.3 Guidelines for Validation Experiments，Guideline 4
- 原文："The reason for this recommendation, of course, is that it is so common for CFD codes to be calibrated to the experimental measurements that many people do not recognize when they are calibrating versus validating"
- 要点：计算流体力学代码按实验测量值"校准"太常见，很多人分不清自己是在校准还是在确认。

### E8

- 位置：4.3 Guidelines for Validation Experiments，Guideline 4
- 原文："the CFD team should not be given the results initially. The CFD team should be given the complete details of the physical modeling parameters and the initial and boundary conditions of the experiment, exactly as it was conducted. That is, everything that is needed for the computationalists to compute solutions must be provided—but no more."
- 要点：实验数据整理分析后，一开始不要把结果交给计算团队；只给他们实验实际采用的全部物理参数和初始、边界条件——算题需要的都给，多余的不给。

### E9

- 位置：4.3 Guidelines for Validation Experiments，Guideline 4
- 原文："The computationalists must quantify the errors and uncertainties in the CFD solution and then present the results for comparison with the experimental data."
- 要点：计算方要先量化自己解的误差和不确定度，再拿出来和实验数据比较。

### E10

- 位置：4.3 Guidelines for Validation Experiments（实验不确定度估计的结尾段）
- 原文："As a final comment on the estimation of experimental uncertainty, we recommend that the same validation experiment be conducted, if possible, in different facilities."
- 要点：可能的话，同一个确认实验在不同设施里做，以发现与设施有关的偏差。

### E11

- 位置：4.3 Guidelines for Validation Experiments，Guideline 4
- 原文："For example, a code being developed by university researchers need not, in our view, attain the level of experimental and computational independence recommended here."
- 要点：作者认为，上面这种计算和实验相互独立的严格程度，是针对工程分析用的代码；大学研究者开发的代码不一定要做到这个程度。
