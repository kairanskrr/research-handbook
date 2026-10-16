# Menzies & Shepperd 2019: "Bad smells" in software analytics papers

- Source: `menzies2019bad`, [full text](https://arxiv.org/abs/1803.05518)
- Version: arXiv:1803.05518v3 (2019-04-13), local PDF `papers/pdf/menzies2019bad.pdf`.
- Note: Lists 12 "bad smells" in software analytics papers (papers that use data analysis to study software engineering problems): surface signs that may indicate deeper problems.

### E1

- Location: §4.4 Inadequate Reporting, item 3
- Quote: "Non-signiﬁcant and post hoc “uninteresting" results are not reported. This seemingly innocuous behavior, known as reporting bias, can lead to serious overestimation of effect sizes"
- Key point: Not reporting non-significant or "uninteresting" results, known as reporting bias, can seriously overestimate effect sizes.

### E2

- Location: §4.6 p < 0.05 and all that!
- Quote: "A correlation of r = 0.01 is trivial and to all practical purposes indistinguishable from no correlation."
- Key point: In the example, a "significant" correlation with a sample of 18,000 and p = 0.049 is only r = 0.01, practically indistinguishable from no correlation. Statistical significance is not practical importance.

### E3

- Location: §4.6
- Quote: "methodologists encourage the notion of the smallest effect size of interest (SESOI). This should be speciﬁed before the research is conducted."
- Key point: Specify the smallest effect size of interest (SESOI), i.e., how large a difference would matter in practice, before the research is conducted.

### E4

- Location: §4.9 Not Exploring Stability
- Quote: "So it is important to check if the effect you want to report actually exists, or is just due to noise."
- Key point: Check whether the effect you want to report actually exists or is just noise, e.g., by using multiple data sets and reporting both central tendency and spread.

### E5

- Location: §4.10 Not Tuning
- Quote: "One particularly egregious “smell" is to compare a heavily tuned new or pet approach with other benchmarks that are untuned."
- Key point: Comparing a heavily tuned new or pet method with untuned competitors is a particularly egregious problem.

### E6

- Location: §4.10 Not Tuning
- Quote: "what we really learn is using the new technique well can outperform using another technique badly."
- Key point: Such a comparison only shows that using the new technique well can outperform using another technique badly, which is of little value.

### E7

- Location: §4.11 Not Exploring Simplicity
- Quote: "it is wise to compare a seemingly sophisticated method against some simpler alternative."
- Key point: Compare a sophisticated method against simpler alternatives to show that the complexity is worth it.

### E8

- Location: §4.4 Inadequate Reporting, item 2
- Quote: "The work cannot be exactly reproduced because some of the algorithms are stochastic and seeds are not provided."
- Key point: If the algorithms are stochastic and the seeds are not provided, others cannot reproduce the work exactly.

### E9

- Location: §1 Introduction
- Quote: "we say that the “smells” listed in this article do not necessarily indicate that the conclusions from the underlying study must be rejected."
- Key point: These "smells" are only warning signs; they do not necessarily mean the study's conclusions must be rejected.

### E10

- Location: §1 Introduction
- Quote: "Studies are more data-driven than theory-driven. For example, after examining many software projects, certain coding styles could be seen to be more bug prone. Follow up experimentation, by manipulating the coding styles, could lead us to believe there is causality."
- Key point: Software analytics studies are mostly data-driven; seeing across many projects that a coding style is associated with more defects is only correlation, and believing in causation requires follow-up experiments that actively change the coding style.

### E11

- Location: §4.3 Using Deprecated or Suspect Data
- Quote: "Researchers adopting a heavily data-driven approach, as is the case for software analytics, need to be vigilant regarding data quality."
- Key point: Heavily data-driven research must stay vigilant about data quality; very old data, or data with known quality problems, are warning signs.

### E12

- Location: §4.4 Inadequate Reporting, item 1
- Quote: "The work cannot be reproduced because the descriptions are too incomplete or high level. In addition, not all materials ( data and code) are available"
- Key point: If descriptions are too incomplete or high-level and not all data and code are available, the work cannot be reproduced.

### E13

- Location: §4.10 Not Tuning
- Quote: "Many machine learners, including data miners, have poorly chosen defaults"
- Key point: Many machine learning algorithms have poorly chosen defaults.

### E14

- Location: §4.10 Not Tuning
- Quote: "As to how to tune, we strongly recommend against the “grid search” i.e., a set of nested for-loops that try a wide range of settings for all tuneable parameters." / "This is a slow approach" / "it has been reported that grid search can miss important optimizations" / "we recommend very simple optimizers (such as differential evolution [103]) can sufﬁce for ﬁnding better tunings"
- Key point: The authors strongly recommend against tuning with grid search (nested loops over all parameter combinations): it is slow, and the gaps between grid points can miss good settings; they suggest simple optimizers such as differential evolution.

### E15

- Location: §4.11 Not Exploring Simplicity
- Quote: "many SE data sets have very simpler regular structures, so very simple techniques can execute much faster and perform just as well, or better, than Deep Learning."
- Key point: (A software engineering example) Many software engineering data sets have simple, regular structures, so very simple methods run much faster and perform as well as or better than deep learning.

### E16

- Location: §4.11 Not Exploring Simplicity
- Quote: "by ﬁrst running a very simple algorithm, it is easy to quickly obtain baseline results to glean the overall structure of the problem."
- Key point: Running a very simple algorithm first quickly gives baseline results and a sense of the overall structure of the problem.
