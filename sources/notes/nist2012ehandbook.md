# NIST/SEMATECH e-Handbook of Statistical Methods，第 2 章 Measurement Process Characterization

- 资料：`nist2012ehandbook`，[原文](https://www.itl.nist.gov/div898/handbook/mpc/mpc.htm)
- 版本：美国国家标准与技术研究院（NIST）和 SEMATECH 的在线统计方法手册，2012 年版（DOI 10.18434/M32189），美国政府网站免费提供，2026-10-06 读取。位置写网页小节号。

### E1

- 位置：2.3.1 Issues in calibration
- 原文："The purpose of calibration is to eliminate or reduce bias in the user's measurement system relative to the reference base."
- 要点：校准的目的是消除或减小你的测量系统相对于参考基准的偏差。

### E2

- 位置：2.1.2 What is a check standard?
- 原文："Check standard methodology is a tool for collecting data on the measurement process to expose errors that afflict the process over time."
- 要点：核查标准（check standard）方法用来收集测量过程本身的数据，暴露随时间出现的误差。

### E3

- 位置：2.1.2
- 原文："An artifact check standard must be close in material content and geometry to the test items that are measured in the workload."
- 要点：实物核查标准在材料和几何形状上要和日常被测的样品接近。

### E4

- 位置：2.2.2 How are bias and variability controlled?
- 原文："A change in the measurement on the check standard that persists at a constant level over several measurement sequences indicates possible:"
- 要点：核查标准的测量值在几轮测量中持续偏到一个新水平，提示参考标准、核查标准或测量程序可能出了变化。

### E5

- 位置：2.5.1 Issues
- 原文："it is important for laboratory personnel who are approaching uncertainty analysis for the first time to be aware of the resources required and to carefully lay out a plan for data collection and analysis."
- 要点：第一次做不确定度分析的人，要先知道需要多少资源，并仔细规划数据收集和分析。

### E6

- 位置：2.5.2 Approach
- 原文："random errors cannot be corrected, and biases can, theoretically at least, be corrected or eliminated from the measurement result."
- 要点：随机误差无法修正；偏差至少在理论上可以修正或消除。

### E7

- 位置：2.5.2，Basic ISO tenets
- 原文："All biases are assumed to be corrected and any uncertainty is the uncertainty of the correction."
- 要点：按国际标准化组织的做法，偏差都假定已经修正，留下的是修正值本身的不确定度。

### E8

- 位置：2.5.2，Rule of quadrature
- 原文："All uncertainty components (standard deviations) are combined by root-sum-squares (quadrature) to arrive at a 'standard uncertainty'"
- 要点：所有不确定度分量（都用标准差表示）按平方和开根号合成，得到标准不确定度。

### E9

- 位置：2.5.2
- 原文："In the computation of the final uncertainty it makes no difference how the components are classified because the ISO guidelines treat type A and type B evaluations in the same manner."
- 要点：算最终不确定度时，分量属于 A 类还是 B 类没有区别，两类按同样方式处理。

### E10

- 位置：2.5.4 Type B evaluations
- 原文："Reference standards calibrated by another laboratory Physical constants used in the calculation of the reported value Environmental effects that cannot be sampled Possible configuration/geometry misalignment in the instrument Lack of resolution of the instrument"
- 要点：常见的 B 类来源：别的实验室校准的参考标准、计算中用到的物理常数、无法抽样的环境影响、仪器可能的装配或几何偏差、仪器分辨力不足。

### E11

- 位置：2.5.4
- 原文："The uncertainty will usually be reported as an expanded uncertainty, U , which is converted to the standard uncertainty," / "If the k factor is not known or documented, it is probably conservative to assume that k = 2 ."
- 要点：校准证书等资料通常给的是扩展不确定度 U，用之前要除以 k 换成标准不确定度；k 没写明时，假设 k = 2 大概是保守的。

### E12

- 位置：2.5.4.1 Standard deviations from assumed distributions
- 原文："The ISO guidelines do not allow worst-case estimates of bias to be added to the other components, but require they in some way be converted to equivalent standard deviations."
- 要点：不能把"最坏情况"的偏差估计直接和其他分量相加，要先换算成等效的标准差。

### E13

- 位置：2.5.4.1
- 原文："The uniform distribution leads to the most conservative estimate of uncertainty; i.e., it gives the largest standard deviation."
- 要点：在均匀、三角、正态三种假设分布中，均匀分布给出的标准差最大，最保守。

### E14

- 位置：2.5.6 Uncertainty budgets and sensitivity coefficients
- 原文："Uncertainty components are listed in a table along with their corresponding sensitivity coefficients, standard deviations and degrees of freedom."
- 要点：不确定度预算就是一张表：列出每个分量和它的灵敏系数、标准差、自由度。

### E15

- 位置：2.5.2
- 原文："For large degrees of freedom, it is suggested to use k = 2 to approximate 95% coverage."
- 要点：自由度较大时，建议取 k = 2，近似对应 95% 的包含概率。

### E16

- 位置：2.5.7.1 Degrees of freedom
- 原文："This is particularly troublesome if there are large components of uncertainty with small degrees of freedom."
- 要点：如果大的不确定度分量只有很少的自由度（例如只重复了几次），合成不确定度的自由度就很成问题。

### E17

- 位置：2.1.1 What are the issues for characterization?
- 原文："One-time tests and special tests or destructive tests are difficult to characterize."
- 要点：一次性试验、特殊试验或破坏性试验很难做测量过程表征。
