# Lones 2021: How to avoid machine learning pitfalls

- Source: `lones2021avoid`, [full text](https://arxiv.org/abs/2108.02497)
- Version: arXiv:2108.02497v5 (2024-08-29), local PDF `papers/pdf/lones2021avoid.pdf`. Page numbers are those printed in the PDF footer.
- Note: A guide for machine learning researchers. We excerpt only principles that generalize to other fields (baselines, independent test data, repeated evaluation, multiple comparisons, reporting).

### E1

- Location: §5.2 Do use meaningful baselines, p. 21
- Quote: "Baselines are often simpler than the new approach, and are chosen to demonstrate that any complexity in the new model is necessary."
- Key point: Baselines are often simpler than the new approach and are chosen to show that any extra complexity in the new method is necessary.

### E2

- Location: §5.2, p. 21
- Quote: "In addition to simple baselines, it’s also important to compare against state-of-the-art (SOTA) models."
- Key point: Besides simple baselines, also compare against state-of-the-art methods.

### E3

- Location: §3.1 Don’t allow test data to leak into the training process, p. 8
- Quote: "The best thing you can do to prevent these issues is to partition off a subset of your data right at the start of your project, and only use this independent test set once to measure the generality of a single model at the end of the project"
- Key point: Partition off an independent test set right at the start of the project and use it only once, at the end, to evaluate the single final model.

### E4

- Location: §4.3 Do avoid sequential overfitting, p. 15
- Quote: "Often this is done as an informal process, trying out different models and different hyperparameters until you get good performance on the test set."
- Key point: Trying out different options on the same test data until the results look good is often an unrecorded, informal process, and it makes the results overfit that data.

### E5

- Location: §4.3, p. 15
- Quote: "the more times you use the test set, the more the overfitting that occurs."
- Key point: The more times you use the test set, the more overfitting occurs.

### E6

- Location: §4.4 Do evaluate a model multiple times, p. 15
- Quote: "a single evaluation of a model can be unreliable, and may either underestimate or overestimate the model’s true potential."
- Key point: A single evaluation is unreliable and may underestimate or overestimate true performance, so evaluate multiple times.

### E7

- Location: §5.4 Do correct for multiple comparisons, p. 22
- Quote: "if you do 20 pairwise tests with a confidence level of 95%, one of them is likely to give you the wrong answer."
- Key point: If you do 20 pairwise tests at a 95% confidence level, one is likely to give the wrong answer; with many comparisons, correct for multiple comparisons.

### E8

- Location: §6.4 Do be careful when reporting statistical significance, p. 25
- Quote: "If you have enough samples, you can always find significant differences, even when the actual difference in performance is miniscule."
- Key point: With enough samples, even a minuscule difference becomes "significant"; also report the effect size to judge whether the difference really matters.

### E9

- Location: §6 How to report your results, p. 23
- Quote: "In order to effectively contribute to knowledge, you need to provide a complete picture of your work, covering both what worked and what didn’t."
- Key point: Report your work completely, covering both what worked and what didn't.

### E10

- Location: §6.3 Don’t generalise beyond the data, p. 24
- Quote: "if your model does really well on one data set, this does not mean that it will do well on other data sets."
- Key point: Doing well on one data set does not mean doing well on others; do not draw conclusions beyond what the data support.

### E11

- Location: §5.1 Don’t assume a bigger number means a better model, p. 19
- Quote: "There are various reasons why a higher figure does not imply a better model."
- Key point: A higher figure does not imply a better method, e.g., when the compared methods used different data splits.

### E12

- Location: §5.4, p. 22
- Quote: "there are numerous other approaches, and there is also some debate about when and where these corrections should be applied"
- Key point: There are many approaches to multiple-comparison correction, and when to apply them is itself debated.

### E13

- Location: §5.1 Don’t assume a bigger number means a better model
- Quote: "Another reason for unfair comparisons is the failure to carry out the same amount of hyperparameter optimisation" / "if one model has default settings and the other has been optimised, then the comparison won’t be fair."
- Key point: One cause of unfair comparisons is unequal hyperparameter optimization: comparing a model with default settings to a tuned one is not fair.

### E14

- Location: §5.1
- Quote: "To be sure of a fair comparison between two approaches, you should freshly implement all the models you’re comparing, optimise each one to the same degree, carry out multiple evaluations"
- Key point: For a fair comparison, freshly implement every model being compared, optimize each to the same degree, evaluate multiple times, and use statistical tests to judge whether differences are significant.

### E15

- Location: §5.5 Don’t always believe results from community benchmarks
- Quote: "if access to the test set is unrestricted, then you can’t assume that people haven’t used it as part of the training process." / "by comparing lots of models on the same test set, it becomes increasingly likely that the best model just happens to over-fit the test set"
- Key point: When a community benchmark's test set is public, you cannot assume nobody trained on it; even if each person uses it only once, the community repeatedly comparing on the same test set means the best model may simply have overfit it by chance.

### E16

- Location: §5.5
- Quote: "it is possible that their training data included the test sets from community benchmarks."
- Key point: Take particular care with foundation models, whose training data may include the test sets of community benchmarks.

### E17

- Location: §6.2 Do report performance in multiple ways
- Quote: "One way to achieve better rigour when evaluating and comparing models is to use multiple data sets."
- Key point: Evaluating and comparing models on multiple data sets compensates for the weaknesses of any single data set and gives a fuller picture.

### E18

- Location: §3.1 Don’t allow test data to leak into the training process
- Quote: "using information about the means and ranges of variables within the whole data set to carry out variable scaling or imputation — in order to prevent information leakage, these statistics should be calculated using only the training data."
- Key point: Using the means and ranges of the whole data set for scaling or imputing missing values leaks information; compute these statistics from the training data only.

### E19

- Location: §2.2 Do take the time to understand your data
- Quote: "Do not assume that, because a data set has been used by a number of papers, it is of good quality"
- Key point: Do not assume a data set is of good quality just because many papers have used it; find out where it came from and what limitations its authors noted.

### E20

- Location: §2.4 Do clean your data
- Quote: "One common problem to look out for is data duplication, i.e. the unintentional inclusion of multiple copies of a data point." / "only remove these if they are likely to be the result of noise or error rather than being natural extremes of the underlying datagenerating process"
- Key point: Look for data problems before modeling, such as unintentionally duplicated data points; remove outliers only if they are likely noise or errors, not genuine extreme values.

### E21

- Location: §4.4 Do evaluate a model multiple times
- Quote: "in medical datasets, it is commonplace to have multiple data points for a single subject; to avoid data leakage, these should be kept together within the same fold."
- Key point: Medical data sets often have multiple data points per subject; in cross-validation, keep them together in the same fold to avoid data leakage.

### E22

- Location: §4.8 Don’t ignore temporal dependencies in time series data
- Quote: "This occurs when some or all of the data points used to train the model occur later in the time series than those used to test the model." / "A situation where this commonly occurs is when standard cross-validation"
- Key point: Look-ahead bias: training data that come later in time than the test data effectively let the model see the future; applying standard cross-validation directly to time series often causes this.

### E23

- Location: §4.6 Do choose metrics carefully, Figure 6
- Quote: "a dummy model which always predicts the same class label has an accuracy of 50% or 90% depending on the distribution of class labels within the data."
- Key point: A dummy model that always predicts the same class can have an accuracy of 50% or 90%, depending entirely on the class distribution in the data.

### E24

- Location: §4.6 Do choose metrics carefully
- Quote: "A well-known example is relying only on the RMSE, which (a bit like accuracy) is susceptible to assigning high value to models which always predict no change."
- Key point: Relying only on root mean squared error (RMSE) in regression and time-series forecasting has a similar problem: a model that always predicts "no change" can still score well.

### E25

- Location: §3.8 Do avoid learning spurious correlations
- Quote: "More complex data tends to contain more of these spurious correlations, and more complex models have more capacity to overfit spurious correlations."
- Key point: More complex data contain more spurious correlations, and more complex models have more capacity to overfit them.

### E26

- Location: §6.5 Do look at your models
- Quote: "Remember that the aim of research is not to get a slightly higher accuracy than everyone else. Rather, it’s to generate knowledge and understanding and share this with the research community." / "So, do look inside your models and do try to understand how they reach a decision."
- Key point: The aim of research is not slightly higher accuracy than everyone else but knowledge and understanding; look at what the model has actually learned.
