# Cattaneo, Idrobo & Titiunik 2020：A Practical Introduction to Regression Discontinuity Designs: Foundations

- 资料：`cattaneo2020practical`，[原文](https://arxiv.org/abs/1911.09511)
- 版本：剑桥大学出版社 Cambridge Elements: Quantitative and Computational Methods for Social Science 丛书，2020 年出版（DOI 10.1017/9781108684606）。本条摘录取自作者放在 arXiv 的版本（1911.09511v1，2019 年 11 月）。

### E1

- 位置：§4.2 Local Polynomial Point Estimation
- 原文："tried to approximate these functions using flexible higher-order polynomials, usually of fourth or fifth order, over the entire support of the data" / "global polynomial methods can lead to unreliable RD point estimators, and thus the conclusions from a global parametric RD analysis can be highly misleading. For these reasons, we recommend against using global polynomial methods for formal RD analysis." / "Modern RD empirical work employs local polynomial methods, which focus on approximating the regression functions only near the cutoff."
- 要点：作者不建议用全局多项式（用全部数据拟合高阶多项式）做正式的断点回归分析，这样得到的估计可能不可靠、结论可能严重误导；现代做法是只在分界线附近做局部多项式拟合。

### E2

- 位置：§4.2 Local Polynomial Point Estimation；§4.2.1 Choice of Kernel Function and Polynomial Order；§4.2.2 Bandwidth Selection and Implementation
- 原文："it is common to adopt a weighting scheme to ensure that the observations closer to c receive more weight than those further away; the weights are determined by a kernel function" / "The recommended choice is the triangular kernel function" / "The weight is maximized at Xi = c, and declines symmetrically and linearly" / "conjunction with a bandwidth that optimizes the mean squared error (MSE), it leads to a point estimator with optimal properties" / "data-driven MSE-optimal bandwidth selectors are easily constructed for the RD treatment effect"
- 要点：推荐三角核函数（离分界线越近的观测权重越大），配合使均方误差最小的带宽使用，点估计有最优性质；这种带宽可以用数据驱动的方法选出来。

### E3

- 位置：§4.3 Local Polynomial Inference
- 原文："inferences based on these bandwidth choices pose a problem. The challenge is that these bandwidths are not "small" enough to remove the leading bias term in the standard distributional approximations used to conduct statistical inference." / "A strategy sometimes found in RD empirical work is to ignore the misspecification error even when an MSE-optimal bandwidth is used. This is not only invalid but also methodologically incoherent"
- 要点：均方误差最优的带宽是为点估计选的，不够"窄"，偏差不能忽略；用它直接按常规方法算置信区间（忽略偏差），在作者看来是无效的。

### E4

- 位置：§4.3 Local Polynomial Inference；§4.3.2 Using Different Bandwidths for Point Estimation and Inference
- 原文："Our recommendation is to use a robust bias correction approach, which is theoretically valid, enjoys some optimality properties, and performs well in practice." / "we recommend that practitioners continue to use hMSE for point estimation of SRD, and use either hMSE or hCER to build the robust bias-corrected confidence interval CIrbc for inference purposes"
- 要点：作者建议用稳健偏差校正的方法做推断：点估计用均方误差最优带宽，置信区间用稳健偏差校正置信区间（带宽可以沿用同一个，也可以另选一个使覆盖误差最小的）。

### E5

- 位置：§4.3.3 RD Local Polynomial Inference in Practice
- 原文："We can now discuss the full output of our previous call to rdrobust" / "The row labeled Robust reports the robust bias-corrected confidence interval CIrbc."
- 要点：书中用 rdrobust 软件包演示，输出里标为 Robust 的那一行就是稳健偏差校正置信区间。

### E6

- 位置：§4.3 Local Polynomial Inference，Robust Bias Correction
- 原文："which is constructed by subtracting the bias estimate from the local polynomial estimator and using the new variance formula for Studentization" / "Because the new variance Vbc incorporates the extra variability introduced in the bias estimation step, it is larger than the conventional OLS variance V when the same bandwidth is used."
- 要点：稳健偏差校正置信区间的做法：先从估计值里减去估计出的偏差，再用新的方差公式，把"估计偏差"这一步带来的额外不确定性也算进去；所以同一带宽下，它用的方差比常规方差大。

### E7

- 位置：§5.5 Sensitivity to Bandwidth Choice
- 原文："The last falsification method we discuss analyzes the sensitivity of the results to the bandwidth choice." / "when the goal is to interpret point estimators, investigating the sensitivity to bandwidth choices is only useful over small ranges around" / "bandwidths much larger than the MSE-optimal bandwidth will lead to estimated RD effects that have too much bias, and bandwidths much smaller than the MSE-optimal choice will lead to RD effects with too much variance" / "In both cases, point estimation will be unreliable, and so will be the conclusions from the falsification test."
- 要点：作者把换带宽看结果是否稳定当作一种检验，但认为只在均方误差最优带宽附近的小范围内换才有意义：比它大得多，估计偏差太大；比它小得多，估计波动太大，两种情况下点估计和检验结论都不可靠。
