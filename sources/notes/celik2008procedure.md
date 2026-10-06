# Celik 等人 2008：Procedure for Estimation and Reporting of Uncertainty Due to Discretization in CFD Applications

- 资料：`celik2008procedure`，[原文](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf)
- 版本：ASME 网站公开的 PDF（与《流体工程杂志》数值精度政策声明合在一个文件里）；正式版发表于 Journal of Fluids Engineering 130(7), 078001, 2008。2026-10-06 读取。位置写小节或步骤。

### E1

- 位置：Preliminaries
- 原文："Before any discretization error estimation is calculated, it must be shown that iterative convergence is achieved with at least three (preferably four) orders of magnitude decrease in the normalized residuals for each equation solved."
- 要点：估计离散误差之前，先要证明迭代已收敛：每个方程的归一化残差至少下降三个（最好四个）数量级。

### E2

- 位置：Recommended Procedure，Step 2
- 原文："Select three significantly different sets of grids, and run simulations to determine the values of key variables important to the objective of the simulation study [...] It is desirable that the grid refinement factor, r=hcoarse/hfine, be greater than 1.3. This value of 1.3 is based on experience, and not on formal derivation."
- 要点：在三套明显不同的网格上计算；网格加密比（粗网格尺寸/细网格尺寸）最好大于 1.3。这个数是经验值，不是推导出来的。

### E3

- 位置：Preliminaries
- 原文："Here we recommend that the degree of sensitivity of the presented solution to small perturbations in the inlet conditions be studied and reported."
- 要点：入口边界条件的不确定性可能是总体不确定性的重要来源，建议研究并报告解对入口条件小扰动的敏感程度。

### E4

- 位置：Preliminaries
- 原文："If authors choose to use it, the method per se will not be challenged in the paper review process."
- 要点：作者如果采用文中推荐的网格收敛指数（Grid Convergence Index，GCI）方法，审稿时不会质疑方法本身；用别的方法，则要在审稿中证明其适当。

### E5

- 位置：Step 5 之后的示例说明
- 原文："the numerical uncertainty in the fine-grid solution for the reattachment length should be reported as 2.2%; note that this does not account for modeling errors."
- 要点：示例中细网格解的数值不确定度报告为 2.2%；这个数不包括模型误差。

### E6

- 位置：Discretization Error Bars
- 原文："When computed profiles of a certain variable are presented, it is recommended that numerical uncertainty be indicated by error bars on the profile, analogous to experimental uncertainty."
- 要点：画计算得到的剖面曲线时，建议像实验不确定度一样，用误差棒标出数值不确定度。
