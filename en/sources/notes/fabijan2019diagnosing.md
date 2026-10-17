# Fabijan et al. 2019: Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners

- Source: `fabijan2019diagnosing`, [original (PDF on the authors' team website)](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf)
- Version: authors' PDF of the KDD 2019 paper (Anchorage, USA), DOI 10.1145/3292500.3330722. The authors are from Microsoft, Booking.com and Outreach.io; the paper is based on a case study of four companies (interviews with 14 people and analysis of more than ten thousand past experiments). Locations give sections only.

### E1

- Location: §2.3.1 Sample Ratio Mismatch
- Quote: "While there are many data quality issues that could decrease the validity and significance of a controlled experiment, Sample Ratio Mismatch in most cases completely invalidates experiment results. For example, a ratio of 50.2/49.8 (821,588 versus 815,482 users) diverges enough from an expected 50/50 ratio that the probability that it happened by chance is less than 1 in 500k."
- Key point: A sample ratio mismatch usually invalidates experiment results completely; for example, a 50.2/49.8 split (821,588 versus 815,482 users) departs from the expected 50/50 enough that the chance of it happening by luck is less than 1 in 500,000.

### E2

- Location: §2.3.1 Sample Ratio Mismatch
- Quote: "To detect an SRM, a chi-square test [30] can be used. If the test determines an unlikely difference between the configured and observed numbers, analysts must investigate the root cause."
- Key point: A chi-square test detects a sample ratio mismatch; when it shows that the gap between configured and observed counts is unlikely to be chance, analysts must find the root cause.

### E3

- Location: §4.1 SRMs are a Common Data Quality Issue
- Quote: "During this study, and through quantitative analysis of experiments conducted within the last year we identified that approximately 6% of experiments at Microsoft exhibit an SRM."
- Key point: About 6% of Microsoft's experiments in the previous year showed a sample ratio mismatch.

### E4

- Location: §4.2 SRMs Indicate Invalid Analysis
- Quote: "In particular, SRMs cause a selection bias that invalidates any causal inference that could be drawn from the experiment."
- Key point: A sample ratio mismatch introduces selection bias that invalidates any causal inference from the experiment.

### E5

- Location: §4.3 SRMs are Challenging to Root-Cause
- Quote: "The time to diagnose an SRM can span from minutes to months, and SRMs can happen due to issues with experiment design, the randomization process, variant deployment, data logging, data collection, data cooking, as well as due to data analysis conditions."
- Key point: Diagnosing a sample ratio mismatch can take minutes or months; the cause can lie anywhere in experiment design, randomization, variant deployment, data logging, collection, processing or analysis conditions.

### E6

- Location: §1 Introduction
- Quote: "After resolving the issue that was causing the SRM in experiment above (see section 5.3 for details), it was found that the change was in fact positive and significantly increased the engagement with the product."
- Key point: An MSN carousel experiment first showed a drop in engagement; after the issue causing the sample ratio mismatch was fixed, the change turned out to be positive and to significantly increase engagement.

### E7

- Location: §5.1 Experiment Assignment SRMs
- Quote: "For every A/B test, it is a best practice to compute results for the pre-period before the test started and confirm that a random split of users into two groups does not cause a large difference in key metrics. If it does, then the same metric in the A/B test period would carry over some of that bias."
- Key point: It is good practice to first compute results on data from before the test started and confirm that the randomly split groups did not already differ much on key metrics; otherwise the metrics during the test carry that bias.
