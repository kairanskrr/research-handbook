# Hernán & Robins：Causal Inference: What If

- 资料：`hernan2020whatif`，[作者网站免费 PDF](https://miguelhernan.org/whatifbook)
- 版本：作者网站 2026 年 8 月 19 日版 PDF（建议引用格式为 Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC）。本文只读了第 3.6 节和第 7、8、9 章的开头部分。

### E1

- 位置：Chapter 3, Section 3.6 The target trial
- 原文："For each causal effect that we wish to estimate using observational data, we may (i) specify the protocol of the target trial that we would like to, but cannot, conduct, and (ii) describe how the observational data would be used to emulate that target trial."
- 要点：每个想用观察性数据估计的因果效应，都可以：(1) 写出我们想做但做不了的目标试验的方案；(2) 说明怎样用观察性数据模拟这个目标试验。

### E2

- 位置：Chapter 3, Section 3.6 The target trial
- 原文："The eligibility criteria need to be selected so that all individuals could in principle receive all treatments of interest"
- 要点：纳入标准要让每个人原则上都能接受所比较的每一种处理。

### E3

- 位置：Chapter 3, Section 3.6 The target trial
- 原文："This comparison implies emulating a target trial in which individuals are assigned to an instantaneous, and possibly very large, weight change at the start of follow-up." / "e.g., one in which some individuals are assigned to lose 5% of body mass index every year, starting at age 40 and for as long as their body mass index stays over 25."
- 要点：直接比较随访开始时体重指数 25 和 30 的人的死亡风险，相当于模拟一个"让人在随访开始时瞬间大幅改变体重"的试验；可以改成更现实的干预，例如从 40 岁起，只要体重指数高于 25，每年减 5%。

### E4

- 位置：Chapter 7, Section 7.1 The structure of confounding
- 原文："The effect of working as a firefighter A on the risk of death Y will be confounded if "being physically fit" L is a cause of both being an active firefighter and having a lower mortality risk."
- 要点：如果"身体好"既让人能当消防员，又让人死亡风险更低，那么"当消防员对死亡的影响"就被混杂了（健康工人偏倚）。

### E5

- 位置：Chapter 7, Section 7.1 The structure of confounding
- 原文："subclinical disease U results both in lack of exercise A and an increased risk of clinical disease Y . This form of confounding is often referred to as reverse causation when L is unknown."
- 要点：尚未发病的亚临床疾病既让人少运动，又增加发病风险；这种混杂常被叫作"反向因果"。

### E6

- 位置：Chapter 7, Section 7.4 Confounding and confounders
- 原文："These examples show that associational or statistical criteria are insufficient to characterize confounding."
- 要点：只凭关联或统计标准，不足以判断什么是混杂。

### E7

- 位置：Chapter 7, Section 7.4 Confounding and confounders
- 原文："A structural approach to confounding emphasizes that causal inference from observational data requires a priori causal knowledge." / "Second, the researchers' assumptions about confounding become explicit and therefore can be explicitly criticized by other investigators."
- 要点：从观察性数据做因果推断，需要事先的因果知识；用因果图把这些知识画出来，研究者关于混杂的假设就变得明确，别人也能明确地批评。

### E8

- 位置：Chapter 7, Section 7.6 Confounding adjustment
- 原文："At the very least, investigators should generally avoid adjustment for variables affected by either the treatment or the outcome."
- 要点：至少，一般不要调整受暴露（处理）或结局影响的变量。

### E9

- 位置：Chapter 7, Section 7.6 Confounding adjustment
- 原文："Of course, thoughtful and knowledgeable investigators could believe that two or more causal structures, possibly leading to different conclusions regarding confounding and confounders, are equally plausible. In that case they would perform multiple analyses and explicitly state the assumptions about causal structure required for the validity of each."
- 要点：如果两种以上的因果结构都说得通，就分别做分析，并写明每个分析成立所需的因果结构假设。

### E10

- 位置：Chapter 7, Section 7.6 Confounding adjustment
- 原文："The critic is not making a scientific statement, but a logical one." / "Your next move is to try and adjust for smoking or, if data on smoking could not be obtained, to conduct a sensitivity analysis to investigate the possible bias induced by smoking."
- 要点：只说"你的研究可能有混杂"不是科学批评，因为任何观察性研究都可能有混杂；有用的批评要指出具体的混杂因素（如吸烟）。这时研究者要去调整它，拿不到数据就做敏感性分析。

### E11

- 位置：Chapter 7, Section 7.3 Confounding and the backdoor criterion
- 原文："If the confounders are unknown, one can only guess what the magnitude of the bias is. Educated guesses can be organized by conducting sensitivity analyses (i.e., repeating the analyses under several assumptions regarding the magnitude of the bias)"
- 要点：混杂因素未知时，只能猜偏倚有多大；可以用敏感性分析把有根据的猜测系统化，即在关于偏倚大小的几种假设下重复分析。

### E12

- 位置：Chapter 8, Selection bias（开头）
- 原文："An association created as a result of the process by which individuals are selected into the analysis is referred to as selection bias. Unlike confounding, this type of bias is not due to the presence of common causes of treatment and outcome, and can arise in both randomized experiments and observational studies."
- 要点：由"哪些人进入分析"这一过程制造出来的关联，叫选择偏倚；它不是来自暴露和结局的共同原因，随机试验和观察性研究里都会出现。

### E13

- 位置：Chapter 8, Section 8.2 Examples of selection bias
- 原文："Regardless of the reasons why data on Y are missing, restricting the analysis to individuals with complete data (C = 0) may result in bias."
- 要点：不管结局数据为什么缺失，只分析数据完整的人都可能带来偏倚。

### E14

- 位置：Chapter 8, Fine Point：Selection bias in case-control studies
- 原文："In this particular case-control study, the investigator decided to select controls (Y = 0) preferentially among women with a hip fracture." / "If individuals with hip fracture are oversampled as controls, then the probability of control selection depends on a consequence of treatment A (as represented by the path from A to C) and "inappropriate control selection" bias will occur."
- 要点：例子：研究绝经后雌激素与冠心病的病例对照研究，优先从髋部骨折的女性中选对照；雌激素能减少髋部骨折，于是对照是否入选取决于暴露的后果，产生"对照选择不当"的偏倚。

### E15

- 位置：Chapter 8, Section 8.3 Selection bias and confounding
- 原文："Hence a key difference between confounding and selection bias: randomization protects against confounding, but not against selection bias when the selection occurs after the randomization."
- 要点：混杂和选择偏倚的一个关键区别：随机化能防混杂，但防不了随机化之后发生的选择偏倚。

### E16

- 位置：Chapter 9, Measurement bias（开头）
- 原文："Since measurement errors can occur under any study design--including both randomized experiments and observational studies--measurement bias need always be considered when interpreting effect estimates."
- 要点：任何设计都会有测量误差，解释效应估计时总要考虑测量偏倚。

### E17

- 位置：Chapter 9, Section 9.2 The structure of measurement error
- 原文："if alcohol intake is ascertained by recall after delivery--because recall may be affected by the outcome of the pregnancy." / "The resulting measurement bias in these two examples is often referred to as recall bias."
- 要点：例子：研究孕期饮酒与出生缺陷，如果在分娩后让母亲回忆饮酒量，回忆会受妊娠结局影响，这就是回忆偏倚。

### E18

- 位置：Chapter 9, Section 9.2 The structure of measurement error
- 原文："The best method to fight bias due to mismeasurement is, obviously, to improve the measurement procedures for the variables used in our analysis."
- 要点：对付测量偏倚最好的办法，是改进变量的测量程序。

### E19

- 位置：Chapter 8, Section 8.2 Examples of selection bias
- 原文："For example, selection bias may arise when treatment is measured as the lifetime exposure to certain factor (medical treatment, lifestyle behavior...) in a study that recruited 50 year-old participants."
- 要点：例子：招募 50 岁的人，却把"一生的暴露"当作处理来研究，可能产生选择偏倚（暴露影响了谁能活到 50 岁并进入研究）。
