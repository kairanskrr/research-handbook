# de França & Travassos 2015：Simulation Based Studies in Software Engineering: A Matter of Validity

- 资料：`defranca2015simulation`，[原文（CLEI Electronic Journal，开放获取，CC BY）](https://www.clei.org/cleiej/index.php/cleiej/article/view/54)
- 版本：CLEI Electronic Journal 18(1), paper 4, 2015。DOI 10.19153/cleiej.18.1.4。

### E1

- 位置：§2 Background
- 原文："The overall quality assessment indicated a poor quality of reports regarding SBS due the lack of relevant information such as research goals, study procedures and strategy, and the experimental design."
- 要点：作者此前的文献综述发现，软件工程中仿真研究的报告质量整体较差，常缺研究目标、研究过程和实验设计等关键信息。

### E2

- 位置：§4.1 Conclusion Validity
- 原文："Considering only one observation when dealing with stochastic simulation, rather than central tendency and dispersion measures" / "Consequently, a single outcome could reflect the stochastic process, rather than the theoretical processes under study."
- 要点：结论效度威胁：随机仿真只看一次运行的结果，不看集中趋势和离散程度。单次结果反映的可能只是随机过程，而不是要研究的机制。

### E3

- 位置：§4.1 Conclusion Validity
- 原文："It should be avoided comparing single values from simulated to empirical outcomes. It is recommended to use proper statistical tests or measures to compare distributions with a certain level of confidence."
- 要点：不要拿单个仿真值和单个实测值比；应当用合适的统计检验或度量，在一定置信水平下比较分布。

### E4

- 位置：§4.2 Internal Validity
- 原文："Simulation model simplifications (assumptions) forcing the desired outcomes" / "this is the most recurrent threat reported in the analyzed papers." / "In such case, there is no room for simulation, since the outcomes are predictable without run the simulations."
- 要点：被分析论文中最常见的威胁：模型的简化假设直接"强加"了期望结果。这时根本不需要仿真，不跑也能预测结果。

### E5

- 位置：§4.2 Internal Validity
- 原文："This is the case when calibrating the simulation model with a specific dataset, reflecting the context of a particular project, product, or organization and using the same calibration to run experiments for another (different) context."
- 要点：内部效度威胁：用反映某个项目、产品或组织的数据校准模型，却拿同一套校准去做另一个背景的实验。

### E6

- 位置：§4.3 Construct Validity
- 原文："Hidden underlying model assumptions" / "if assumptions are not explicit in model description, results may be misinterpreted or bias the conclusions, and may not be possible to judge at what extent they correspond to the actual phenomena."
- 要点：构念效度威胁：隐藏的模型假设。假设没写明，结果可能被误读、结论可能有偏，读者也无法判断模型在多大程度上对应真实现象。

### E7

- 位置：§4.3 Construct Validity
- 原文："If there is no evidence of theoretical mechanism’s face validity, it is possible that the simulation model has been producing right outcomes, through wrong explanations."
- 要点：没有证据表明模型机制合理时，模型可能是"用错误的解释得出了正确的结果"。

### E8

- 位置：§4.3 Construct Validity
- 原文："This threat regards to simulation studies where a simulation model is chosen without proper information about its validity. Therefore, no conclusion can be draw about the phenomenon, but only about the model itself."
- 要点：模型的有效性没有证据时，结论只能关于模型本身，不能推到真实现象上。

### E9

- 位置：§4.4 External Validity
- 原文："Simulation results are context-dependent, since there is a need for calibration" / "Results are as general as the supporting data."
- 要点：外部效度威胁：仿真需要校准，结果依赖于背景；结果的推广范围不会超出支撑数据的范围。

### E10

- 位置：§4.2 Internal Validity
- 原文："However, it is important to be caution when dropping out factors to simplify the experimental design, as in fractional factorial designs."
- 要点：为简化实验设计而去掉因素（如部分因子设计）时要谨慎。

### E11

- 位置：§5 Verification and Validation of Simulation Models
- 原文："Since the SBS validity is highly affected by the simulation model validity, using a model that cannot be considered valid will bring invalid results, regardless the mitigation actions applied to deal with other possible validity threats. In other words, the simulation model itself represents the main threat to the study validity."
- 要点：仿真研究的效度很大程度上取决于模型的有效性；模型无效，其他补救都无济于事。模型本身就是研究效度的主要威胁。

### E12

- 位置：§6 Recommendations，Recommendation 1
- 原文："Make use of Face Validity procedures, involving domain experts, to assess the plausibility of both conceptual, executable models and simulation outcomes, using proper diagrams and statistical charts as instruments respectively."
- 要点：建议 1：请领域专家做表面效度检查，评估概念模型、可执行模型和仿真结果是否合理。

### E13

- 位置：§6 Recommendations，Recommendation 3
- 原文："Use results from Sensitivity Analysis to select valid parameters’ settings when running simulation experiments, rather than model “fishing”."
- 要点：建议 3：用敏感性分析的结果选择合理的参数设置，而不是反复试参数去"钓"想要的结果。

### E14

- 位置：§6 Recommendations，Recommendation 4
- 原文："Always verify model assumptions, so the results of simulated experiments can get more reliable."
- 要点：建议 4：始终检验模型的假设。

### E15

- 位置：§6 Recommendations，Recommendation 7
- 原文："When designing the simulation experiment, consider as factors (and levels) not only the simulation model’s input parameters, but also internal parameters, different sample datasets and versions of the simulation model, implementing alternative strategies to be evaluated."
- 要点：建议 7：设计仿真实验时，因素不只包括输入参数，还可以包括内部参数、不同的样本数据集，以及实现了不同策略的模型版本。

### E16

- 位置：§6 Recommendations
- 原文："Comparison-based procedures cannot capture this type of threat. Just white box procedures like Face Validity involving simulation experts may help to identify such threat."
- 要点："假设强加结果"这类威胁，靠比较输出的方法发现不了（输出可能和实测吻合），只有让专家检查模型内部的白盒方法（如表面效度检查）才可能发现。

### E17

- 位置：§6 Recommendations
- 原文："Thus, what is important is that both the goals for the simulation study and the expected benefits should drive the balance between the efforts for mitigating threats to validity and the risk of not doing so."
- 要点：这些建议都有成本；应根据研究目标和预期收益，在应对效度威胁的投入和不做的风险之间权衡。

### E18

- 位置：§7 Final Remarks
- 原文："Taking simulation as a complementary research strategy for the evolution of Software Engineering knowledge, mainly in contexts where in vivo or in vitro experiments are unfeasible or risky, researchers should be aware about possible threats involved in this sort of study."
- 要点：仿真是一种补充性的研究策略，主要用于真实环境或实验室实验不可行或有风险的场合。
