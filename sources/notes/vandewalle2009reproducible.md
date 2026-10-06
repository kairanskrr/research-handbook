# Vandewalle, Kovačević & Vetterli 2009：Reproducible Research in Signal Processing — What, why, and how

- 资料：`vandewalle2009reproducible`，[原文](https://infoscience.epfl.ch/record/136640)
- 版本：IEEE Signal Processing Magazine 26(3)，2009 年 5 月，第 37–47 页。读取的是洛桑联邦理工学院（EPFL）机构知识库 Infoscience 公开提供的全文 PDF，2026-10-06 下载。位置写小标题和期刊页码。

### E1

- 位置：开头，第 37 页
- 原文："For a computational algorithm, details such as the exact data set, initialization or termination procedures, and precise parameter values are often omitted in the publication for various reasons, such as a lack of space, a lack of self-discipline, or an apparent lack of interest to the readers, to name a few."
- 要点：作者观察到：算法论文常常省略确切的数据集、初始化和终止条件、精确的参数值，原因有篇幅、自律不够、以为读者不关心等。

### E2

- 位置：When is research reproducible, and when is it not?，第 39 页
- 原文："A research work is called reproducible if all information relevant to the work, including, but not limited to, text, data and code, is made available, such that an independent researcher can reproduce the results."
- 要点：本文对"可复现研究"的定义：与研究有关的全部信息（包括文字、数据和代码）都公开，使独立研究者能重新得到结果。

### E3

- 位置：Reproducible research study，第 40 页
- 原文："We performed a study on all of the 134 papers published in IEEE Transactions on Image Processing in 2004." / "Finally, code (9%) and data (33%) are only available online in a minority of the cases"
- 要点：作者检查了 2004 年《IEEE 图像处理汇刊》的全部 134 篇论文：只有 9% 公开了代码，33% 公开了数据。

### E4

- 位置：Failures of reproducibility，第 41 页
- 原文："As different versions of this image circulate on the Web, it is often difficult to know on which version the simulations were performed."
- 要点：常用测试图像（如 Lena）在网上有多个版本，读者常常无法知道论文用的是哪一版，这就影响复现。

### E5

- 位置：Failures of reproducibility，第 41 页
- 原文："Even we as authors are not able to reproduce the results, as we have different versions of the code on our disk, and it is unclear with which version the images in the final version were created."
- 要点：作者坦言，自己早期的一篇论文连自己都复现不了：硬盘上有多个版本的代码，不知道最终稿的图是哪一版生成的。

### E6

- 位置：How to do reproducible research? — Experiments，第 41–42 页
- 原文："Practical experiments are, by their nature, probably the most difficult type of work to reproduce." / "Often, it is not even feasible to repeat the exact experiments, as results can in the best case only be statistically equivalent to the original results. Therefore, in this case, we opt for reusability rather than reproducibility of the data."
- 要点：实物实验最难复现，往往最多只能得到统计上等价的结果；这时应退而求其次，让测量数据可以被别人重新使用。

### E7

- 位置：How to do reproducible research? — Experiments，第 42 页
- 原文："Next to the measurement data, a detailed description of the experimental setup and measurement devices should still be given, for those interested in understanding the exact setup or in performing similar experiments."
- 要点：除了公开测量数据，还要详细描述实验装置和测量设备。

### E8

- 位置：How to do reproducible research? — Algorithms，第 41 页
- 原文："While in theory, the code is supposed to be platform or hardware independent, it is useful to specify the platform on which the tests were performed."
- 要点：即使代码理论上与平台、硬件无关，也要写明测试用的平台和软件版本。

### E9

- 位置：Implementation and issues，第 43 页
- 原文："Often, in a company, the work is only published after it has been protected by a patent." / "Still, many companies funding university research or doing research themselves consider the know-how attached to a patent valuable and are not willing to have the resulting code distributed online."
- 要点：企业里常常先申请专利再发表；资助大学研究的企业也可能不愿意公开代码。

### E10

- 位置：Implementation and issues，第 43 页
- 原文："Note also that, even if the code and data are not made available online, it may be very useful to set reproducible research standards internally, such that colleagues inside the company can reproduce the results."
- 要点：代码和数据不能公开时，至少在内部建立可复现标准，让内部同事能复现结果。

### E11

- 位置：Case study: super-resolution，第 42 页
- 原文："It took about one week to check all the results and make sure they were reproducible, clean up and document the MATLAB code, and put everything online." / "done in about one day. We already had reproducibility in mind from the start"
- 要点：作者第一次事后整理可复现材料花了约一周；后来从一开始就考虑复现，同样的工作约一天完成。

### E12

- 位置：How to do reproducible research? — Components，第 41 页
- 原文："signal processing can be considered as a hybrid between theoretical and experimental sciences." / "Often, to develop an intuitive feel for the results, a theorem is complemented by numerical simulations."
- 要点：作者认为信号处理介于理论科学和实验科学之间，研究可分为理论、算法、实验三部分，各自的复现要求不同；定理常配上数值仿真，帮助理解结果。

### E13

- 位置：Case study: super-resolution，第 42 页
- 原文："For each figure or table in the papers, there is a MATLAB script figure_x.m or table_y.m that reproduces the figure or table."
- 要点：作者为论文里每张图、每个表各写一个脚本，运行即可重新生成。
