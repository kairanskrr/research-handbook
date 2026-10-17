# Kohavi et al. 2012: Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained

- Source: `kohavi2012trustworthy`, [PDF (authors' team website)](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf)
- Version: author version of the KDD 2012 paper (ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Beijing), 9 pages. The authors were on Microsoft's experimentation platform team, and most examples come from Bing search and MSN. Locations give the page numbers printed on the PDF.

### E1

- Location: §1 Introduction, p. 1
- Quote: "In a controlled experiment, users are randomly split between the variants (e.g., the six designs for the Real Estate widget) in a persistent manner (a user receives the same experience in multiple visits) during the experiment period."
- Key point: Online controlled experiments split users randomly and persistently between variants: a user who visits several times during the experiment always sees the same variant.

### E2

- Location: §1 Introduction, p. 2
- Quote: "In the paper Online Experimentation at Microsoft [2], we shared the statistic that only one third of ideas tested at Microsoft improved the metric(s) they were designed to improve."
- Key point: Only one third of the ideas tested at Microsoft improved the metrics they were designed to improve.

### E3

- Location: §2 Background and Terminology, p. 3
- Quote: "The A/A test has been our most useful tool in identifying issues in practical systems. We strongly recommend that every practical system continuously run A/A tests."
- Key point: The A/A test has been the authors' most useful tool for finding problems in real systems; they strongly recommend every experimentation system run A/A tests continuously.

### E4

- Location: §3.1.2 Puzzling Outcome, p. 3
- Quote: "When Bing had a bug in an experiment, which resulted in very poor results being shown to users, two key organizational metrics improved significantly: distinct queries per user went up over 10%, and revenue per user went up over 30%!"
- Key point: When a bug in a Bing experiment showed users very poor results, two key business metrics rose significantly: distinct queries per user went up over 10% and revenue per user over 30%.

### E5

- Location: §3.1.3 Explanation, p. 4
- Quote: "(If the ratio of users in the variants varies significantly from the design, it's a good indication of a bug.)"
- Key point: If the ratio of users across variants departs significantly from the design, a bug is likely.

### E6

- Location: §3.2.3 Explanation, p. 4
- Quote: "The "success" of getting users to click more was not real, but rather an instrumentation difference."
- Key point: In one experiment the "success" of more user clicks was not real; it came from an instrumentation difference, with the code that logs user behavior losing data at different rates in the two variants.

### E7

- Location: §3.3.4 Lessons Learned, p. 6
- Quote: "Most experiments have a stable effect (constant mean), but the high variance means that we need to collect enough data to get better estimates; early results are often misleading."
- Key point: Most experiments have a stable effect, but variance is high, so enough data must be collected; early results are often misleading.

### E8

- Location: §3.3.1 Background, p. 5
- Quote: "The existence of Primacy and Novelty effects can be assessed by generating the delta graph (between Control and Treatment) over time, and evaluating trends, visually or analytically." / "But this is where our surprising result comes in: most cases of suspected Primacy and Novelty effects are not real, but just a statistical artifact."
- Key point: Primacy and novelty effects can be checked by plotting the Treatment–Control difference over time, but most suspected cases are not real, only a statistical artifact.

### E9

- Location: §3.4.2 Puzzling Outcome, p. 6
- Quote: "For some of our key metrics, including Sessions/user, the confidence interval of the percent effect does not shrink over time. Running the experiment longer does not provide additional statistical power for these metrics."
- Key point: For some key metrics, such as sessions per user, the confidence interval does not shrink over time; running longer adds no statistical power for them.

### E10

- Location: §3.5.3 Explanation, pp. 7–8
- Quote: "One big drawback with the "bucket system" is its vulnerability to carryover effects, where the same users who were impacted by the first experiment are being used for the follow-on experiment." / "Even after three months, the user buckets still had not fully recovered to their pre-experiment levels."
- Key point: Systems that reuse the same user buckets are vulnerable to carryover effects, where users affected by one experiment are used in the next; in one case the buckets had still not recovered to pre-experiment levels after three months.

### E11

- Location: §4 Summary, p. 8
- Quote: "Instrumentation issues are related to the concept of measure validity, i.e., the extent to which the metric used captures the concept we intended to measure" / "Generating numbers is easy; generating numbers you should trust is hard!"
- Key point: Instrumentation problems bear on measure validity, the extent to which a metric captures the concept it is meant to measure; generating numbers is easy, generating numbers you should trust is hard.
