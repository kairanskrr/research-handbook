# Kapoor et al. 2024: REFORMS: Consensus-based Recommendations for Machine-learning-based Science

- Source: `kapoor2024reforms`, [original](https://doi.org/10.1126/sciadv.adk3452)
- Version: Science Advances 10(18), eadk3452, 2024; CC BY-NC 4.0. Local PDF `papers/pdf/kapoor2024reforms.pdf`.
- Note: A reporting checklist for "machine-learning-based science," with 32 items in 8 modules, developed jointly by 19 researchers from computer science, data science, mathematics, the social sciences, and the biomedical sciences.

### E1

- Location: The scope of our claims: ML-based science
- Quote: "We define ML-based science as scientific research that uses the performance of an ML model as evidence for a scientific claim."
- Key point: Machine-learning-based science is research that uses the performance of a machine learning model as evidence for a scientific claim.

### E2

- Location: Abstract
- Quote: "It consists of 32 questions and a paired set of guidelines. REFORMS was developed on the basis of a consensus of 19 researchers across computer science, data science, mathematics, social sciences, and biomedical sciences."
- Key point: The REFORMS checklist has 32 questions and a paired set of guidelines, developed by consensus among 19 researchers across computer science, data science, mathematics, the social sciences, and the biomedical sciences.

### E3

- Location: Module 1, 1c Motivation for the use of ML methods
- Quote: "In the data modeling culture, which is aligned with traditional statistical methods, researchers' focus is on estimating the parameters of a function that is meant to meaningfully represent the process by which input data produces output data in the world." / "rather, the goal is to accurately predict output data when given a new sample of input data that is separate from the original data sample in which the model was trained."
- Key point: The "data modeling" culture of traditional statistics focuses on estimating parameters that meaningfully represent the real data-generating process (describing relationships, estimating causal effects); the "algorithmic modeling" culture (most machine learning research) focuses on accurate prediction on new samples not seen in training, and the parameters need not be interpretable.

### E4

- Location: The scope of our claims, Explanatory modeling
- Quote: "Such research uses traditional statistical methods for improving our understanding of real-world phenomena rather than predicting outcomes" / "errors in this domain are subtly different compared to ML-based science, which means that much of our checklist does not apply to explanatory modeling research."
- Key point: Explanatory modeling uses traditional statistical methods to understand phenomena rather than predict outcomes; its errors differ from those of machine-learning-based science, so much of the REFORMS checklist does not apply to it.

### E5

- Location: Module 1, 1a Population or distribution
- Quote: "The population of interest is the group to which the researchers intend the findings of the study to generalize." / "Unfortunately, research articles do not always clearly state their population of interest"
- Key point: The population of interest is the group (or data distribution) to which the researchers intend the findings to generalize; papers often do not state it clearly.

### E6

- Location: Module 3, 3d Outcome variable
- Quote: "The outcome variable is typically an empirical proxy for an unobservable theoretical construct"
- Key point: The outcome variable being predicted is usually only an empirical proxy for an unobservable theoretical construct; explain where the two might diverge.

### E7

- Location: Module 3, 3c Justification for why the dataset is useful
- Quote: "A broad claim like “this is the best dataset available on this topic” does not help readers understand the strengths and weaknesses of the data for the study's research question"
- Key point: Broad claims such as "this is the best dataset available on this topic" do not help; explain specifically why these data suit your research question.

### E8

- Location: Module 3, 3e Number of samples
- Quote: "When the sampling frame is unrepresentative, increasing the sample size can shrink confidence intervals without decreasing bias in estimates, thus giving false confidence"
- Key point: When the sampling frame is unrepresentative, a larger sample only shrinks confidence intervals without reducing bias, which gives false confidence.

### E9

- Location: Module 3, 3e Number of samples
- Quote: "We also ask researchers to distinguish between the number of individuals in the dataset and the number of rows in the dataset, in cases where an individual can appear in more than one row."
- Key point: When one individual can appear in several rows, report the number of individuals and the number of rows separately.

### E10

- Location: Module 4, 4a Excluded data and rationale
- Quote: "the choice of the subset can substantially affect the performance of the resulting model." / "We ask authors to justify why the particular subset of data used was chosen."
- Key point: Which subset of the data you use can substantially affect model performance; conclusions hold only for the subset actually used, so justify the choice.

### E11

- Location: Module 4, 4c Data transformations
- Quote: "For example, mean imputation and oversampling must be done separately on each fold of a dataset. Failing to do so can result in overoptimistic results"
- Key point: Steps such as mean imputation and oversampling must be done separately on each fold; otherwise the results will be overoptimistic.

### E12

- Location: Module 5, 5d Model selection method
- Quote: "Testing multiple models on the holdout set and choosing the one with the best performance on the holdout set can result in an overoptimistic estimate of performance." / "To avoid this bias, a separate test set can be maintained, or when there is less data, nested CV can provide an alternative"
- Key point: Testing several models on the holdout set and picking the best overestimates performance; keep a separate test set, or use nested cross-validation when data are scarce.

### E13

- Location: Module 5, 5e Hyperparameter selection
- Quote: "More resources devoted to searching over hyperparameters can improve performance substantially." / "One method may perform better than another with one set of hyperparameters while performing worse given a different set of hyperparameters."
- Key point: Spending more resources on hyperparameter search can improve performance substantially; with a different set of hyperparameters, the ranking of two methods can reverse.

### E14

- Location: Module 5, 5f Appropriate baselines
- Quote: "For example, if the baselines were not chosen using the same model selection methods, this could result in the baselines being “weak.” As a result, the apparent benefits of the new method may be misleading."
- Key point: If baselines were not selected and tuned with the same model selection methods, they can be "weak," and the new method's apparent advantage may be misleading.

### E15

- Location: Module 6, Data leakage
- Quote: "Leakage is a spurious relationship between the features and the target variable that arises as an artifact of the data collection, sampling," / "preprocessing, or modeling steps." / "normalizing features in the training and test data together leads to leakage because information about the test data features is included in the training data"
- Key point: Leakage is a spurious relationship between features and the target that arises as an artifact of data collection, sampling, preprocessing, or modeling. For example, normalizing training and test data together causes leakage, because information from the test data enters the training data.

### E16

- Location: Module 6, Data leakage
- Quote: "However, one of the features used in the model was whether a patient had been prescribed antibiotics. This is an error because antibiotics would typically be prescribed after the diagnosis of sepsis, so they act as a proxy for the outcome variable."
- Key point: A healthcare company's sepsis prediction model used "whether antibiotics were prescribed" as a feature, but antibiotics are usually prescribed after a sepsis diagnosis, so the feature acted as a proxy for the outcome and inflated performance.

### E17

- Location: Module 6, 6b Dependencies or duplicates
- Quote: "a clinical dataset might have many samples from the same patient" / "In such cases, the train-test split or CV split should take these dependencies into account--for instance, by including all samples from each patient in the same train-test split or CV fold."
- Key point: Samples may depend on each other (e.g., many samples from the same patient); train-test splits and cross-validation folds must account for this, for instance by keeping all of a patient's samples on the same side.

### E18

- Location: Module 6, 6b Dependencies or duplicates
- Quote: "Duplicates in the datasets can also spread across training and test sets if the dataset is split randomly."
- Key point: With a random split, duplicates can end up in both the training and test sets.

### E19

- Location: Module 6, 6c Feature legitimacy
- Quote: "This type of leakage is more likely when there are a large number of features, due to the increased likelihood of including one or more illegitimate features."
- Key point: The more features there are, the more likely an illegitimate feature slips in, so this type of leakage becomes more likely.

### E20

- Location: Module 7, 7a Performance metrics used
- Quote: "accuracy might not be suitable to measure the performance of an ML model in the presence of heavy class imbalance" / "In some domains, certain errors may be more costly than others."
- Key point: Accuracy may be unsuitable under heavy class imbalance; in some domains some errors are costlier than others, so the metric should match the scientific claim.

### E21

- Location: Module 7, 7b Uncertainty estimates
- Quote: "Where methods do not exist, bootstrapping within the test set can be used to generate confidence intervals for performance claims"
- Key point: Where no established method exists, bootstrapping within the test set can give confidence intervals for performance claims.

### E22

- Location: Module 7, 7c Appropriate statistical tests
- Quote: "reporting uncertainty is better than performing statistical tests alone"
- Key point: Reporting uncertainty is better than performing statistical tests alone.

### E23

- Location: Module 8, 8a Evidence of external validity
- Quote: "even if their model currently generalizes to their target population, that performance may degrade over time because of temporal distribution shift"
- Key point: Even if a model generalizes to the target population now, its performance may degrade over time because of temporal distribution shift.

### E24

- Location: Module 8, 8b Contexts in which findings do not hold
- Quote: "Clarifying the circumstances under which scientific conclusions or model performance are not expected to hold helps to set clear expectations and avoid unjustified hype."
- Key point: Stating the circumstances under which conclusions or model performance are not expected to hold sets clear expectations and avoids unjustified hype.

### E25

- Location: Caption of Table 1
- Quote: "Instead of requiring strict adherence for each item, authors and referees should decide which items are relevant for a study and how details can be reported better."
- Key point: The checklist does not demand strict adherence to every item; authors and referees decide which items are relevant to a study.

### E26

- Location: Module 2, Computational reproducibility
- Quote: "Our checklist requires information about the dataset, code, computing environment, documentation for how to get the results in a study, and a reproduction script to automatically run the code and generate results."
- Key point: Computational reproducibility requires the dataset, code, computing environment, documentation of how to get the results, and a reproduction script that runs the code and generates the results automatically.

### E27

- Location: The scope of our claims, Predictive analytics
- Quote: "In predictive analytics, the population or distribution of interest may not be clearly defined. The relationships found using ML models only need to hold within a company or organization and need not generalize."
- Key point: Predictive analytics in business need not define a population of interest, since the relationships found need only hold within the company; scientific research needs to generalize, and that is the difference.

### E28

- Location: Table 1, Module 5
- Quote: "5e. For the model(s) reported in the paper, specify details about the hyperparameter tuning." / "5f. Justify that model comparisons are against appropriate baselines."
- Key point: The checklist asks you to specify how the reported models' hyperparameters were tuned and to justify that model comparisons are against appropriate baselines.

### E29

- Location: Table 1, Module 6 Data leakage
- Quote: "6a. Justify that preprocessing (Module 4) and modeling (Module 5) steps only use information from the training dataset (and not the test dataset)." / "6b. Describe methods used to address dependencies or duplicates between the training and test datasets" / "6c. Justify that each feature or input used in the model is legitimate for the task at hand and does not lead to leakage."
- Key point: Three items guard against leakage: justify that preprocessing and modeling use only information from the training data; describe how dependencies and duplicates between training and test sets were handled; and justify that each feature is legitimate for the task and does not cause leakage.
