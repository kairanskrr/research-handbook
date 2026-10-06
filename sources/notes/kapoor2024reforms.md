# Kapoor 等人 2024：REFORMS: Consensus-based Recommendations for Machine-learning-based Science

- 资料：`kapoor2024reforms`，[原文](https://doi.org/10.1126/sciadv.adk3452)
- 版本：Science Advances 10(18), eadk3452，2024；CC BY-NC 4.0。本地 PDF `papers/pdf/kapoor2024reforms.pdf`。
- 说明：19 位来自计算机、数据科学、数学、社会科学和生物医学的研究者共同制定的"基于机器学习的科学研究"报告清单，32 项，分 8 个模块。

### E1

- 位置：The scope of our claims: ML-based science
- 原文："We define ML-based science as scientific research that uses the performance of an ML model as evidence for a scientific claim."
- 要点：基于机器学习的科学研究，是把机器学习模型的表现当作科学主张证据的研究。

### E2

- 位置：摘要
- 原文："It consists of 32 questions and a paired set of guidelines. REFORMS was developed on the basis of a consensus of 19 researchers across computer science, data science, mathematics, social sciences, and biomedical sciences."
- 要点：REFORMS 清单有 32 个问题和配套指南，由计算机、数据科学、数学、社会科学和生物医学领域的 19 位研究者达成共识制定。

### E3

- 位置：Module 1，1c Motivation for the use of ML methods
- 原文："In the data modeling culture, which is aligned with traditional statistical methods, researchers' focus is on estimating the parameters of a function that is meant to meaningfully represent the process by which input data produces output data in the world." / "rather, the goal is to accurately predict output data when given a new sample of input data that is separate from the original data sample in which the model was trained."
- 要点：传统统计的"数据建模"文化关注估计能代表真实生成过程的参数（描述关系、估计因果效应）；"算法建模"文化（多数机器学习研究）关注在训练时没见过的新样本上准确预测，参数不必有解释意义。

### E4

- 位置：The scope of our claims，Explanatory modeling
- 原文："Such research uses traditional statistical methods for improving our understanding of real-world phenomena rather than predicting outcomes" / "errors in this domain are subtly different compared to ML-based science, which means that much of our checklist does not apply to explanatory modeling research."
- 要点：解释性建模用传统统计方法理解现象而不是预测结果；它的错误类型和基于机器学习的研究不同，REFORMS 清单的大部分不适用于它。

### E5

- 位置：Module 1，1a Population or distribution
- 原文："The population of interest is the group to which the researchers intend the findings of the study to generalize." / "Unfortunately, research articles do not always clearly state their population of interest"
- 要点：目标总体是研究者希望结论能推广到的那个群体（或数据分布）；论文常常没有写清目标总体。

### E6

- 位置：Module 3，3d Outcome variable
- 原文："The outcome variable is typically an empirical proxy for an unobservable theoretical construct"
- 要点：被预测的结果变量通常只是一个不可直接观察的理论概念的经验替代指标，要说明它在哪些方面可能和概念不一致。

### E7

- 位置：Module 3，3c Justification for why the dataset is useful
- 原文："A broad claim like “this is the best dataset available on this topic” does not help readers understand the strengths and weaknesses of the data for the study's research question"
- 要点："这是该主题能找到的最好数据集"这类笼统说法没有帮助；要具体说明这份数据为什么适合回答你的问题。

### E8

- 位置：Module 3，3e Number of samples
- 原文："When the sampling frame is unrepresentative, increasing the sample size can shrink confidence intervals without decreasing bias in estimates, thus giving false confidence"
- 要点：抽样框没有代表性时，样本再大也只会让置信区间变窄，偏差并不减少，反而给人虚假的信心。

### E9

- 位置：Module 3，3e Number of samples
- 原文："We also ask researchers to distinguish between the number of individuals in the dataset and the number of rows in the dataset, in cases where an individual can appear in more than one row."
- 要点：同一个个体可能占多行时，要分别报告个体数和数据行数。

### E10

- 位置：Module 4，4a Excluded data and rationale
- 原文："the choice of the subset can substantially affect the performance of the resulting model." / "We ask authors to justify why the particular subset of data used was chosen."
- 要点：选用数据的哪个子集，会大大影响模型表现；结论只对实际使用的那个子集成立，要说明为什么这样选。

### E11

- 位置：Module 4，4c Data transformations
- 原文："For example, mean imputation and oversampling must be done separately on each fold of a dataset. Failing to do so can result in overoptimistic results"
- 要点：均值填补、过采样等处理必须在每一折数据上分别做，否则结果会过于乐观。

### E12

- 位置：Module 5，5d Model selection method
- 原文："Testing multiple models on the holdout set and choosing the one with the best performance on the holdout set can result in an overoptimistic estimate of performance." / "To avoid this bias, a separate test set can be maintained, or when there is less data, nested CV can provide an alternative"
- 要点：在留出集上试多个模型、挑最好的那个，会高估表现；应另外保留一份测试集，数据少时可用嵌套交叉验证。

### E13

- 位置：Module 5，5e Hyperparameter selection
- 原文："More resources devoted to searching over hyperparameters can improve performance substantially." / "One method may perform better than another with one set of hyperparameters while performing worse given a different set of hyperparameters."
- 要点：在超参数搜索上投入更多资源，可以大大提高表现；换一组超参数，两个方法的优劣可能反过来。

### E14

- 位置：Module 5，5f Appropriate baselines
- 原文："For example, if the baselines were not chosen using the same model selection methods, this could result in the baselines being “weak.” As a result, the apparent benefits of the new method may be misleading."
- 要点：基线如果没有用同样的模型选择方法挑选和优化，就会成为"弱基线"，新方法看起来的优势可能是误导。

### E15

- 位置：Module 6，Data leakage
- 原文："Leakage is a spurious relationship between the features and the target variable that arises as an artifact of the data collection, sampling," / "preprocessing, or modeling steps." / "normalizing features in the training and test data together leads to leakage because information about the test data features is included in the training data"
- 要点：泄漏是在数据收集、抽样、预处理或建模过程中人为造成的、特征和结果之间的虚假关系。例如把训练数据和测试数据放在一起做归一化，就会泄漏，因为测试数据的信息进入了训练数据。

### E16

- 位置：Module 6，Data leakage
- 原文："However, one of the features used in the model was whether a patient had been prescribed antibiotics. This is an error because antibiotics would typically be prescribed after the diagnosis of sepsis, so they act as a proxy for the outcome variable."
- 要点：某医疗公司的败血症预测模型用"是否开了抗生素"作特征，而抗生素通常在确诊之后才开，这个特征其实是结果的替代品，导致表现虚高。

### E17

- 位置：Module 6，6b Dependencies or duplicates
- 原文："a clinical dataset might have many samples from the same patient" / "In such cases, the train-test split or CV split should take these dependencies into account--for instance, by including all samples from each patient in the same train-test split or CV fold."
- 要点：数据中的样本可能相互依赖（如同一病人的多个样本），划分训练/测试集或交叉验证折时要考虑这种依赖，把同一病人的样本放在同一边。

### E18

- 位置：Module 6，6b Dependencies or duplicates
- 原文："Duplicates in the datasets can also spread across training and test sets if the dataset is split randomly."
- 要点：随机划分时，重复样本可能同时出现在训练集和测试集中。

### E19

- 位置：Module 6，6c Feature legitimacy
- 原文："This type of leakage is more likely when there are a large number of features, due to the increased likelihood of including one or more illegitimate features."
- 要点：特征越多，越可能混进不合法的特征，这类泄漏越容易发生。

### E20

- 位置：Module 7，7a Performance metrics used
- 原文："accuracy might not be suitable to measure the performance of an ML model in the presence of heavy class imbalance" / "In some domains, certain errors may be more costly than others."
- 要点：类别严重不平衡时，准确率可能不合适；有的领域里某些错误的代价比其他错误更高，指标要和科学主张对应。

### E21

- 位置：Module 7，7b Uncertainty estimates
- 原文："Where methods do not exist, bootstrapping within the test set can be used to generate confidence intervals for performance claims"
- 要点：没有现成方法时，可以在测试集内做自助法（bootstrap）重抽样，得到表现指标的置信区间。

### E22

- 位置：Module 7，7c Appropriate statistical tests
- 原文："reporting uncertainty is better than performing statistical tests alone"
- 要点：报告不确定性比只做统计检验更好。

### E23

- 位置：Module 8，8a Evidence of external validity
- 原文："even if their model currently generalizes to their target population, that performance may degrade over time because of temporal distribution shift"
- 要点：即使模型现在能推广到目标总体，表现也可能因为数据分布随时间变化而下降。

### E24

- 位置：Module 8，8b Contexts in which findings do not hold
- 原文："Clarifying the circumstances under which scientific conclusions or model performance are not expected to hold helps to set clear expectations and avoid unjustified hype."
- 要点：写明结论或模型表现在哪些情况下预计不成立，可以设定清楚的预期，避免不合理的炒作。

### E25

- 位置：Table 1 说明
- 原文："Instead of requiring strict adherence for each item, authors and referees should decide which items are relevant for a study and how details can be reported better."
- 要点：清单不要求每项都严格照做，由作者和审稿人判断哪些项和本研究相关。

### E26

- 位置：Module 2，Computational reproducibility
- 原文："Our checklist requires information about the dataset, code, computing environment, documentation for how to get the results in a study, and a reproduction script to automatically run the code and generate results."
- 要点：计算可复现要求提供数据集、代码、计算环境、得到结果的说明文档，以及能自动运行代码、生成结果的复现脚本。

### E27

- 位置：The scope of our claims，Predictive analytics
- 原文："In predictive analytics, the population or distribution of interest may not be clearly defined. The relationships found using ML models only need to hold within a company or organization and need not generalize."
- 要点：商业中的预测分析不必说清目标总体，模型找到的关系只要在本公司内成立即可；科学研究则需要推广，这是两者的区别。

### E28

- 位置：Table 1，Module 5
- 原文："5e. For the model(s) reported in the paper, specify details about the hyperparameter tuning." / "5f. Justify that model comparisons are against appropriate baselines."
- 要点：清单要求说明报告的模型是怎样调超参数的，并论证比较用的基线是合适的。

### E29

- 位置：Table 1，Module 6 Data leakage
- 原文："6a. Justify that preprocessing (Module 4) and modeling (Module 5) steps only use information from the training dataset (and not the test dataset)." / "6b. Describe methods used to address dependencies or duplicates between the training and test datasets" / "6c. Justify that each feature or input used in the model is legitimate for the task at hand and does not lead to leakage."
- 要点：防泄漏的三项：论证预处理和建模只用了训练数据的信息；说明怎样处理训练集和测试集之间的依赖和重复；论证每个特征对任务都是合法的、不会造成泄漏。
