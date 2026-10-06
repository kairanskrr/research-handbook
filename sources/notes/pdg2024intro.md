# Particle Data Group 2024：Review of Particle Physics，Introduction

- 资料：`pdg2024intro`，[原文](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-rpp-intro.pdf)
- 版本：粒子数据组（Particle Data Group，PDG）《粒子物理评论》2024 年版的"Introduction"一章（2024 年 5 月 31 日版），PDG 网站免费提供；全书发表于 Phys. Rev. D 110, 030001（2024），开放获取。位置写小节号。

### E1

- 位置：§5.2.2
- 原文："To average data, we use a standard weighted least-squares procedure" / "We begin by assuming that measurements of a given quantity are uncorrelated" / "If χ2/(N - 1) is less than or equal to 1, and there are no known problems with the data, we accept the results."
- 要点：先假设各测量彼此不相关，算出加权平均后再算卡方，用卡方除以 N − 1（N 是测量个数）检查这些测量是否彼此一致：不大于 1、数据也没有已知问题，就接受结果。

### E2

- 位置：§5.2.2
- 原文："The large value of the χ2 is likely to be due to underestimation of errors in at least one of the experiments. Not knowing which of the errors are underestimated, we assume they are all underestimated by the same factor S."
- 要点：卡方偏大，很可能是至少一个实验低估了误差；不知道是哪一个，就假设所有误差都被低估了同一个倍数 S（"标度因子"），把平均值的误差相应放大。

### E3

- 位置：§5.3 Rounding
- 原文："The basic rule states that if the three highest order digits of the error lie between 100 and 354, we round to two significant digits. If they lie between 355 and 949, we round to one significant digit."
- 要点：粒子数据组的修约规则：误差的前三位数字在 100—354 之间，保留两位有效数字；在 355—949 之间，保留一位。

### E4

- 位置：§5.3
- 原文："In all cases, the central value is given with a precision that matches that of the error." / "the result (coming from an average) 0.827 ± 0.119 would appear as 0.83 ± 0.12"
- 要点：中心值保留到和误差相同的位数。例：0.827 ± 0.119 写成 0.83 ± 0.12。

### E5

- 位置：§5.4 Discussion
- 原文："it is difficult to develop a procedure that handles simultaneously in a reasonable way two basic types of situations: (a) data that lie apart from the main body of the data are incorrect (contain unreported errors); and (b) the opposite--it is the main body of data that is incorrect."
- 要点：很难有一种算法同时处理好两种情况：离群的数据是错的；或者反过来，主体数据是错的。
