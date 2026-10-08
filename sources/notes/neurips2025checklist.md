# NeurIPS：Paper Checklist Guidelines

- 资料：`neurips2025checklist`，[原文](https://neurips.cc/public/guides/PaperChecklist)
- 版本：NeurIPS 论文检查清单指南网页（与 NeurIPS 2025 征稿启事配套，含第 16 项"大语言模型使用声明"），2026-10-08 读取。位置写清单题号或段落。只作为机器学习方向一个会议的例子，其他会议和以后年份的要求可能不同。

### E1

- 位置：开头段
- 原文："Do not remove the checklist: The papers not including the checklist will be desk rejected"
- 要点：不附检查清单的投稿会被直接拒稿（不送审）。

### E2

- 位置：开头段（答题说明）
- 原文："Reviewers will be asked to use the checklist as one of the factors in their evaluation." / "it is perfectly acceptable to answer "no" provided a proper justification is given"
- 要点：审稿人会把清单作为评价因素之一；回答"否"完全可以，只要给出合适的理由。

### E3

- 位置：开头段（答题说明）
- 原文："In general, answering "no" or "n/a" is not grounds for rejection."
- 要点：一般来说，回答"否"或"不适用"本身不是拒稿理由。

### E4

- 位置：2. Limitations
- 原文："Reviewers will be specifically instructed to not penalize honesty concerning limitations."
- 要点：审稿人被明确要求不要因为作者诚实写出局限而扣分。

### E5

- 位置：7. Experiment Statistical Significance
- 原文："The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions)."
- 要点：要写清误差线反映的是哪种波动来源，例如数据划分、初始化、某个参数的随机抽取。

### E6

- 位置：7. Experiment Statistical Significance
- 原文："It should be clear whether the error bar is the standard deviation or the standard error of the mean."
- 要点：要写清误差线是标准差还是均值的标准误。

### E7

- 位置：8. Experiments Compute Resource
- 原文："The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper)"
- 要点：要说明整个项目用的算力是否多于论文报告的实验（例如没写进论文的预实验和失败实验）。

### E8

- 位置：4. Experimental Result Reproducibility
- 原文："While NeurIPS does not require releasing code, we do require all submissions to provide some reasonable avenue for reproducibility"
- 要点：NeurIPS 不强制公开代码，但要求每篇投稿都提供某种合理的复现途径。

### E9

- 位置：5. Open Access to Data and Code
- 原文："Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark)."
- 要点：不能仅因没附代码而拒稿，除非代码是贡献的核心（例如新的开源基准）。

### E10

- 位置：14. Crowdsourcing and Research with Human Subjects
- 原文："According to the NeurIPS Code of Ethics, you must pay workers involved in data collection, curation, or other labor at least the minimum wage in your country."
- 要点：按 NeurIPS 伦理准则，参与数据收集、整理等劳动的人员，报酬至少达到所在国最低工资。

### E11

- 位置：10. Broader Impacts
- 原文："However, if you see a direct path to any negative applications, you should point it out."
- 要点：基础研究不必罗列所有可能的滥用，但看得到通向有害应用的直接路径时，要指出来。

### E12

- 位置：1. Claims
- 原文："Claims in the paper should match theoretical and experimental results in terms of how much the results can be expected to generalize."
- 要点：论文的主张要和理论、实验结果能推广的程度相符。

### E13

- 位置：12. Licenses
- 原文："Remember to state which version of the asset you're using." / "State the name of the license (e.g., CC-BY 4.0) for each asset."
- 要点：用了别人的代码、数据、模型，要写明版本和许可证名称。

### E14

- 位置：开头段（答题说明）
- 原文："You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper."
- 要点：清单要随最终版一起提交，并和论文一起公开。

### E15

- 位置：6. Experimental Setting/ Details
- 原文："information about how hyperparameters were selected should appear either in the paper or supplementary materials"
- 要点：超参数是怎样选出来的，要写在正文或补充材料里。

### E16

- 位置：3. Theory, Assumptions and Proofs
- 原文："If you are including theoretical results, did you state the full set of assumptions of all theoretical results, and did you include complete proofs of all theoretical results?"
- 要点：有理论结果的，要写全所有假设，并给出完整证明（可放在补充材料里，正文附证明梗概）。

### E17

- 位置：2. Limitations
- 原文："It is worth keeping in mind that a worse outcome might be if reviewers discover limitations that aren't acknowledged in the paper."
- 要点：审稿人自己发现论文没承认的局限，后果可能更糟。

### E18

- 位置：10. Broader Impacts
- 原文："We expect many papers to be foundational research and not tied to particular applications, let alone deployments."
- 要点：很多论文是基础研究，不和具体应用挂钩，更谈不上部署。
