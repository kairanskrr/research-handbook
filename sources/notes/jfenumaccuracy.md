# Journal of Fluids Engineering：Editorial Policy Statement on the Control of Numerical Accuracy

- 资料：`jfenumaccuracy`，[原文](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf)
- 版本：美国机械工程师学会（ASME）网站公开的 PDF，内容为《流体工程杂志》（Journal of Fluids Engineering）关于数值精度控制的编辑政策声明（十条标准及其简化版），同一 PDF 后附 Celik 等人 2008 的离散误差估计程序（见 `celik2008procedure`）。2026-10-06 读取。位置写条目编号。

### E1

- 位置：简化声明（shortened statement）首段
- 原文："The Journal of Fluids Engineering will not consider any paper reporting the numerical solution of a fluids engineering problem that fails to address the task of systematic truncation error testing and accuracy estimation."
- 要点：《流体工程杂志》不考虑没有系统检验截断误差、没有估计精度的数值计算论文。

### E2

- 位置：第 4 条
- 原文："Solutions over a range of significantly different grid resolutions should be presented to demonstrate grid-independent or grid-convergent results."
- 要点：要给出在明显不同的几套网格分辨率下的解，证明结果与网格无关或随网格收敛。

### E3

- 位置：第 10 条
- 原文："Comparison with reliable experimental results is appropriate, provided experimental uncertainty is established. However, “reasonable agreement” with experimental data alone will not be enough to justify a given single-grid calculation, especially if adjustable parameters are involved."
- 要点：可以和可靠的实验结果比较，但前提是实验不确定度已经确定；只在一套网格上算、和实验"大致吻合"不够，有可调参数时更不够。

### E4

- 位置：第 1 条
- 原文："It is not enough to state, for example, that the method is based on a “conservative finite-volume formulation,” giving then a reference to a general CFD textbook."
- 要点：描述数值方法要具体（包括各项的形式精度阶数），只写"守恒的有限体积格式"再引一本通用教科书是不够的。

### E5

- 位置：十条之后的说明段
- 原文："We recognize that the effort to perform a thorough study of numerical accuracy may be great and that many practical engineering calculations will continue to be performed by first order methods, on a single fixed grid. However, such analyses would not be appropriate for presentation in this archival journal."
- 要点：编辑承认完整的精度研究工作量可能很大，很多实际工程计算仍会用一阶方法、一套网格；但这样的分析不适合在该期刊发表。

### E6

- 位置：第 5 条
- 原文："Stopping criteria for iterative calculations need to be precisely explained. Estimates must be given for the corresponding convergence error."
- 要点：迭代计算的停止准则要写清，并给出相应的收敛误差估计。
