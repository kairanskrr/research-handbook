# Dmitriev et al. 2017: A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments

- Source: `dmitriev2017dirty`, [original (PDF on the authors' team website)](https://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf)
- Version: authors' PDF of the KDD 2017 paper (Halifax, Canada), DOI 10.1145/3097983.3098024. The authors are from Microsoft's Analysis and Experimentation team; examples come from Bing, MSN, Skype, Xbox and other products. PDF page numbers are unclear, so locations give sections only.

### E1

- Location: §4 Metric Taxonomy, Data Quality Metrics
- Quote: "A fundamental requirement in A/B testing is that treatment and control samples are drawn at random from the same population. This means that the number of users in the samples should satisfy the expected ratio. If the actual ratio is different than the expected (a chi-square test can be used), it means something is wrong with the sampling process." / "Most of the time SRM implies a severe selection bias, enough to render the experiment results invalid"
- Key point: Treatment and control must be drawn at random from the same population, so their user counts should match the expected ratio; if the actual ratio deviates (a chi-square test can check), the sampling went wrong. This sample ratio mismatch usually signals severe selection bias, enough to invalidate the results.

### E2

- Location: §4 Metric Taxonomy, Guardrail Metrics
- Quote: "In addition to OEC metrics, we have found that there is a set of metrics which are not clearly indicative of success of the feature being tested, but which we do not want to significantly harm when making a ship decision. We call these metrics Guardrail metrics. For instance, on a web site like Bing or MSN, Page Load Time (PLT) is usually a guardrail metric."
- Key point: Guardrail metrics do not directly show whether a feature succeeded, but a ship decision should not significantly harm them; page load time is an example.

### E3

- Location: §4 Metric Taxonomy, Data Quality Metrics
- Quote: "The first question we answer when looking at the outcome of an experiment is whether we can trust that the experiment was configured and run correctly such that we can trust the experiment results."
- Key point: The first question when looking at an experiment's outcome is whether it was configured and run correctly, so that the results can be trusted.

### E4

- Location: §5.2 Misinterpretation of Ratio Metrics
- Quote: "To detect denominator mismatch in ratio metrics, we recommend to always define count metrics for the numerator and the denominator, and provide those in the result alongside the ratio metric."
- Key point: For ratio metrics such as click-through rate, also define and report count metrics for the numerator and denominator, so you can tell when the denominator has shifted.

### E5

- Location: §5.3 Telemetry Loss Bias
- Quote: "Different rates of telemetry loss between the variants is a common way to bias experiment results."
- Key point: Different rates of telemetry loss (usage records the product sends back automatically) between variants are a common source of bias in experiment results.

### E6

- Location: §5.4 Assuming Underpowered Metrics had no Change
- Quote: "Therefore, we cannot assume that we did not impact the underpowered metric." / "To avoid the aforementioned issues, a priori power analysis should be conducted to estimate sufficient sample sizes, at least for the OEC and the Guardrail metrics"
- Key point: A non-significant result on an underpowered metric does not mean "no impact"; at least for the overall evaluation criterion and guardrail metrics, run an a priori power analysis to estimate a sufficient sample size.

### E7

- Location: §5.4 Assuming Underpowered Metrics had no Change
- Quote: "If an underpowered metric turns out to be statistically significant, then it is more likely that the observed change of the metric will be exaggerated compared to the true effect size"
- Key point: When an underpowered metric happens to come out significant, the observed change is more likely to exaggerate the true effect.

### E8

- Location: §5.5 Claiming Success with a Borderline Pvalue
- Quote: "In the above case, we reran the experiment with double the amount of traffic and observed that there were no statistically significant changes for the same metric." / "We recommended for experimenters to evaluate experiment results by placing emphasis on strongly statistically significant metrics and rerunning with larger traffic when metrics, in particular the OEC metrics, have borderline p-values."
- Key point: A positive result with a p-value of 0.029 was no longer significant when rerun with double the traffic; focus on strongly significant metrics and rerun with more traffic when a metric, especially the overall evaluation criterion, has a borderline p-value.

### E9

- Location: §5.6 Continuous Monitoring and Early Stopping
- Quote: "Continuously checking the results and stopping as soon as statistical significance is achieved leads to an increase in Type-I error, or the probability of a false positive." / "In our experience, stopping early or extending the experiment are both very common mistakes experiment owners make."
- Key point: Checking results continuously and stopping as soon as they are significant raises the Type I error (false positive) rate; stopping early and extending an experiment on the fly are both very common mistakes.

### E10

- Location: §5.6 Continuous Monitoring and Early Stopping
- Quote: "Making experiment owners aware of the pitfall, and establishing the guidelines that require making ship decision only at the pre-defined time point, is one approach to avoid this pitfall. Another approach is to adjust the p-values, to account for extra checking [33]. Finally, in [34] a Bayesian framework is proposed that, unlike NHST, naturally allows for continuous monitoring and early stopping."
- Key point: Three ways to avoid this: require ship decisions only at a predefined time point; adjust p-values to account for the extra looks; or use a Bayesian framework that allows continuous monitoring and early stopping.

### E11

- Location: §5.6 Continuous Monitoring and Early Stopping
- Quote: "The issue is exacerbated by the fact that in practice continuous experiment monitoring is essentially a requirement to be able to shut down the experiment quickly in case a strong degradation in user experience is observed."
- Key point: In practice you have to monitor experiments continuously anyway, so you can shut them down quickly if user experience degrades badly, which makes the problem harder.

### E12

- Location: §5.8 Segment Interpretation
- Quote: "The key lesson from this example is to ensure that the condition used for defining the segment is not impacted by the treatment." / "Aside from increasing the possibility of encountering a Simpson's paradox, this is also an instance of multiple testing problem [37] and will result in an increased Type-I error."
- Key point: When analyzing user segments, the condition that defines a segment must not be affected by the treatment; slicing users until something is significant both invites Simpson's paradox and is a multiple testing problem that raises the false positive rate.

### E13

- Location: §5.10 Novelty and Primacy Effects
- Quote: "We also recommend segmenting treatment effect by different days of the experiment, or different user visits, to see if the treatment effect changes over time."
- Key point: Break down the treatment effect by day of the experiment or by user visit to check whether the effect changes over time.

### E14

- Location: §5.12 Failure to Apply Twyman's Law
- Quote: "Twyman's law says that any figure that looks interesting or different is usually wrong. Applying it to analyzing the results of online experiments, we can rephrase it as follows: any unexpected metric movement, positive or negative, usually means there is an issue."
- Key point: Twyman's law says any figure that looks interesting or different is usually wrong; for online experiments, any unexpected metric movement, positive or negative, usually means something is broken.

### E15

- Location: §5.7 Assuming the Metric Movement is Homogeneous
- Quote: "Not being aware of such effects may result in shipping a feature that, while improving user experience overall, substantially hurts experience for a group of users."
- Key point: Ignoring how effects differ across user groups can lead you to ship a feature that helps overall but substantially hurts one group of users.

### E16

- Location: §5.9 Impact of Outliers
- Quote: "As the example above shows, however, one needs to ensure that all variants in the experiment are impacted by the outlier filtering logic in the same way."
- Key point: When filtering outliers, make sure the filter affects all variants the same way; in one experiment described in the paper, the treatment made some real users active enough to be filtered out as bots.
