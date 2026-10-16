# Arp et al. 2022: Dos and Don'ts of Machine Learning in Computer Security

- Source: `arp2022dos`, [original](https://arxiv.org/abs/2010.09470)
- Version: USENIX Security 2022, local PDF `papers/pdf/arp2022dos.pdf`.
- Note: Summarizes ten common pitfalls (P1-P10) of machine learning in computer security.

### E1

- Location: §2, P6 Inappropriate Baseline
- Quote: "To show to what extent a novel method improves the state of the art, it is vital to compare it with previously proposed methods." / "Instead of focusing solely on complex models for comparison, simple models should also be considered throughout the evaluation."
- Key point: To show how much a new method improves the state of the art, you must compare it with previously proposed methods, including simple models, not only complex ones.

### E2

- Location: §2, P9 Lab-Only Evaluation
- Quote: "A learning-based system is solely evaluated in a laboratory setting, without discussing its practical limitations." / "it should be evaluated in a realistic setting whenever possible to transparently assess its capabilities"
- Key point: Evaluating only in a laboratory setting without discussing practical limitations is a common pitfall; whenever possible, evaluate in a realistic setting.

### E3

- Location: abstract
- Quote: "we analyze the prevalence of these pitfalls in 30 top-tier security papers from the past decade that rely on machine learning" / "To our surprise, each paper suffers from at least three pitfalls; even worse, several pitfalls affect most of the papers, which shows how endemic and subtle the problem is."
- Key point: Every one of 30 top-tier security papers had at least three pitfalls, and several pitfalls affected most papers, showing how endemic and subtle the problem is.

### E4

- Location: §2, P3 Data Snooping
- Quote: "Test snooping occurs when the test set is used for experiments before the ﬁnal evaluation." / "Temporal snooping occurs if time dependencies within the data are ignored." / "selective snooping describes the cleansing of data based on information not available in practice. An example is the removal of outliers based on statistics of the complete dataset"
- Key point: Data snooping comes in three kinds: test snooping (using the test set for experiments before the final evaluation), temporal snooping (ignoring time dependencies in the data), and selective snooping (cleansing data with information not available in practice, e.g., removing outliers using statistics of the whole dataset).

### E5

- Location: §2, P3 Data Snooping
- Quote: "as the characteristics of publicly available datasets are increasingly exposed, methods developed using this data implicitly leverage knowledge from the test data" / "Consequently, experiments on well-known datasets should be complemented with experiments on more recent data from the considered application domain."
- Key point: As public datasets become better understood, methods developed on them implicitly leverage knowledge of the test data; experiments on well-known datasets should therefore be complemented with more recent data.

### E6

- Location: §2, P4 Spurious Correlations
- Quote: "Spurious correlations result from artifacts that correlate with the task to solve but are not actually related to it, leading to false associations." / "The model may learn to detect a speciﬁc IP range instead of generic attack patterns."
- Key point: Spurious correlations come from artifacts that correlate with the task but are not related to it; e.g., if most attacks in an intrusion detection dataset come from one IP range, the model may learn that range instead of attack patterns.

### E7

- Location: §2, P5 Biased Parameter Selection
- Quote: "over-optimistic results can be easily produced by tuning hyperparameters or calibrating thresholds on the test data instead of the training data."
- Key point: Tuning hyperparameters or calibrating thresholds on the test data instead of the training data easily produces over-optimistic results.

### E8

- Location: §2, P8 Base Rate Fallacy
- Quote: "Consider the example in Figure 2 where 99 % true positives are possible at 1 % false positives. Yet, if we consider the class ratio of 1:100, this actually corresponds to 100 false positives for every 99 true positives."
- Key point: Base rate fallacy: 99% true positives at 1% false positives looks good, but with a 1:100 class ratio there are 100 false positives for every 99 true positives.

### E9

- Location: §2, P7 Inappropriate Performance Measures
- Quote: "Given the ROC curve alone, the performance appears excellent, yet the low precision reveals the true performance of the classiﬁer"
- Key point: On imbalanced data the ROC curve alone can look excellent, while the low precision reveals the classifier's true performance.

### E10

- Location: §2, P2 Label Inaccuracy
- Quote: "this labeling is rarely perfect and researchers must account for uncertainty and noise"
- Key point: Labels are rarely perfect; researchers must account for label uncertainty and noise.

### E11

- Location: §2, P1 Sampling Bias
- Quote: "The collected data does not sufﬁciently represent the true data distribution of the underlying security problem"
- Key point: Sampling bias: the collected data do not adequately represent the true data distribution of the security problem.

### E12

- Location: §4.1 Mobile Malware Detection
- Quote: "Interestingly, the URL play.google.com turns out to be one of the ﬁve most discriminative features for the benign class, indicating that the classiﬁer has learned to distinguish the origins of Android apps, rather than the difference between malware and benign apps"
- Key point: In a malware detection experiment, the URL play.google.com became one of the most discriminative features for benign apps, showing that the classifier learned to tell apart where apps came from, not malware from benign apps.
