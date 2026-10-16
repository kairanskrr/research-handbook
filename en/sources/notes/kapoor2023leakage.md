# Kapoor & Narayanan 2023: Leakage and the reproducibility crisis in machine-learning-based science

- Source: `kapoor2023leakage`, [original](https://doi.org/10.1016/j.patter.2023.100804)
- Version: Patterns 4(9), 100804, 2023; CC BY 4.0 open access. We read the PubMed Central full text PMC10499856.
- Note: Surveys reproducibility problems caused by data leakage across 17 fields, proposes a taxonomy of 8 types of leakage and "model info sheets," and includes a reproduction study on civil war prediction.

### E1

- Location: Summary
- Quote: "we find 17 fields where leakage has been found, collectively affecting 294 papers and, in some cases, leading to wildly overoptimistic conclusions."
- Key point: Data leakage was found in 17 fields, affecting 294 papers in total, in some cases leading to wildly overoptimistic conclusions.

### E2

- Location: Results, Data leakage causes irreproducible results
- Quote: "we do not present our results as a systematic meta-review of leakage from a coherent sample of papers but rather as a lower bound of reproducibility issues in ML-based science." / "the code might have errors that are not apparent from reading the papers."
- Key point: This is only a lower bound: most reviews look only at the paper text, and errors in code are not apparent from reading papers.

### E3

- Location: Results, Leakage in modeling competitions
- Quote: "In contrast, in most ML-based science, the researcher has access to the entire dataset while creating the ML models. Leakage often occurs because of the researcher having access to the entire dataset during the modeling process."
- Key point: Unlike competitions, where a third party holds the test set, in research the researcher has access to the entire dataset while building models, which is exactly why leakage often happens.

### E4

- Location: Taxonomy, [L1.3]
- Quote: "Feature selection on the entire dataset results in using information about which feature performs well on the test set to make a decision about which features should be included in the model."
- Key point: Feature selection on the entire dataset uses information about which features perform well on the test set.

### E5

- Location: Taxonomy, [L3.1] Temporal leakage
- Quote: "When an ML model is used to make predictions about a future outcome of interest, the test set should not contain any data from a date before the training set."
- Key point: Temporal leakage: when predicting the future, the test set must not contain data from before the training set, or the model uses information "from the future."

### E6

- Location: Taxonomy, [L3.2]
- Quote: "Nonindependence between training and test samples constitutes leakage, unless the scientific claim is about a distribution that has the same dependence structure."
- Key point: Nonindependence between training and test samples (e.g., from the same people) is leakage, unless the scientific claim concerns a distribution with the same dependence structure.

### E7

- Location: Taxonomy, [L3.3] Sampling bias in test distribution
- Quote: "One example of sampling bias is spatial bias, which refers to choosing the test data from a geographic location but making claims about model performance in other geographic locations."
- Key point: Sampling bias in the test data is also leakage, for example testing on data from one region while claiming the model performs equally well in other regions.

### E8

- Location: Summary; A case study of civil war prediction
- Quote: "When the errors are corrected, complex ML models do not perform substantively better than decades-old LR models." / "We found errors in 4 of the 12 papers—exactly the 4 papers that claimed superior performance of complex ML models over baseline LR models for predicting civil war."
- Key point: Of 12 civil war prediction papers, the 4 with errors were exactly the 4 that claimed complex models outperform logistic regression baselines; once the leakage is corrected, complex models do not perform substantively better than decades-old logistic regression.

### E9

- Location: Model info sheets
- Quote: "The burden of proof for ensuring the correctness of these arguments is on the researcher making the scientific claims."
- Key point: The burden of proving there is no leakage lies with the researcher making the scientific claim.

### E10

- Location: Summary
- Quote: "We propose that researchers test for each type of leakage by filling out model info sheets, which we introduce."
- Key point: The authors propose that researchers fill out "model info sheets" to check for each type of leakage.

### E11

- Location: A case study of civil war prediction
- Quote: "We found that 9 of the 12 papers for which complete code and data were available included no significance tests or uncertainty quantification for classifier performance comparison"
- Key point: Of the 12 papers with complete code and data, 9 compared classifiers without any significance test or uncertainty quantification.
