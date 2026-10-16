# Cattaneo, Idrobo & Titiunik 2020: A Practical Introduction to Regression Discontinuity Designs: Foundations

- Source: `cattaneo2020practical`, [Original](https://arxiv.org/abs/1911.09511)
- Version: Cambridge University Press, Cambridge Elements: Quantitative and Computational Methods for Social Science series, 2020 (DOI 10.1017/9781108684606). These excerpts are from the authors' arXiv version (1911.09511v1, November 2019).

### E1

- Location: §4.2 Local Polynomial Point Estimation
- Quote: "tried to approximate these functions using flexible higher-order polynomials, usually of fourth or fifth order, over the entire support of the data" / "global polynomial methods can lead to unreliable RD point estimators, and thus the conclusions from a global parametric RD analysis can be highly misleading. For these reasons, we recommend against using global polynomial methods for formal RD analysis." / "Modern RD empirical work employs local polynomial methods, which focus on approximating the regression functions only near the cutoff."
- Key point: The authors advise against global polynomials (high-order polynomials fit to all the data) for formal regression discontinuity analysis, since they can give unreliable estimates and seriously misleading conclusions; the modern approach is local polynomial fitting near the cutoff only.

### E2

- Location: §4.2 Local Polynomial Point Estimation; §4.2.1 Choice of Kernel Function and Polynomial Order; §4.2.2 Bandwidth Selection and Implementation
- Quote: "it is common to adopt a weighting scheme to ensure that the observations closer to c receive more weight than those further away; the weights are determined by a kernel function" / "The recommended choice is the triangular kernel function" / "The weight is maximized at Xi = c, and declines symmetrically and linearly" / "conjunction with a bandwidth that optimizes the mean squared error (MSE), it leads to a point estimator with optimal properties" / "data-driven MSE-optimal bandwidth selectors are easily constructed for the RD treatment effect"
- Key point: The triangular kernel (observations closer to the cutoff get more weight) is recommended; combined with the bandwidth that minimizes mean squared error, it gives point estimates with optimal properties, and that bandwidth can be chosen in a data-driven way.

### E3

- Location: §4.3 Local Polynomial Inference
- Quote: "inferences based on these bandwidth choices pose a problem. The challenge is that these bandwidths are not "small" enough to remove the leading bias term in the standard distributional approximations used to conduct statistical inference." / "A strategy sometimes found in RD empirical work is to ignore the misspecification error even when an MSE-optimal bandwidth is used. This is not only invalid but also methodologically incoherent"
- Key point: The MSE-optimal bandwidth is chosen for point estimation and is not "small" enough to make the bias negligible; using it to build conventional confidence intervals (ignoring the bias) is, in the authors' view, invalid.

### E4

- Location: §4.3 Local Polynomial Inference; §4.3.2 Using Different Bandwidths for Point Estimation and Inference
- Quote: "Our recommendation is to use a robust bias correction approach, which is theoretically valid, enjoys some optimality properties, and performs well in practice." / "we recommend that practitioners continue to use hMSE for point estimation of SRD, and use either hMSE or hCER to build the robust bias-corrected confidence interval CIrbc for inference purposes"
- Key point: The authors recommend robust bias-corrected inference: use the MSE-optimal bandwidth for the point estimate, and robust bias-corrected confidence intervals for inference (with the same bandwidth or a separate one that minimizes coverage error).

### E5

- Location: §4.3.3 RD Local Polynomial Inference in Practice
- Quote: "We can now discuss the full output of our previous call to rdrobust" / "The row labeled Robust reports the robust bias-corrected confidence interval CIrbc."
- Key point: The book demonstrates this with the rdrobust package; the output row labeled Robust is the robust bias-corrected confidence interval.

### E6

- Location: §4.3 Local Polynomial Inference, Robust Bias Correction
- Quote: "which is constructed by subtracting the bias estimate from the local polynomial estimator and using the new variance formula for Studentization" / "Because the new variance Vbc incorporates the extra variability introduced in the bias estimation step, it is larger than the conventional OLS variance V when the same bandwidth is used."
- Key point: How the robust bias-corrected confidence interval works: subtract the estimated bias from the estimate, then use a new variance formula that also accounts for the extra uncertainty from estimating the bias; so at the same bandwidth its variance is larger than the conventional one.

### E7

- Location: §5.5 Sensitivity to Bandwidth Choice
- Quote: "The last falsification method we discuss analyzes the sensitivity of the results to the bandwidth choice." / "when the goal is to interpret point estimators, investigating the sensitivity to bandwidth choices is only useful over small ranges around" / "bandwidths much larger than the MSE-optimal bandwidth will lead to estimated RD effects that have too much bias, and bandwidths much smaller than the MSE-optimal choice will lead to RD effects with too much variance" / "In both cases, point estimation will be unreliable, and so will be the conclusions from the falsification test."
- Key point: The authors treat checking whether results are stable across bandwidths as a falsification test, but consider it meaningful only over a small range around the MSE-optimal bandwidth: much larger bandwidths give too much bias, much smaller ones too much variance, and in both cases point estimates and test conclusions are unreliable.
