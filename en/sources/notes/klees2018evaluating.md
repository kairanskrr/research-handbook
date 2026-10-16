# Klees et al. 2018: Evaluating Fuzz Testing

- Source: `klees2018evaluating`, [original](https://arxiv.org/abs/1808.09700)
- Version: arXiv:1808.09700v2 (CCS 2018), local PDF `papers/pdf/klees2018evaluating.pdf`.
- Note: Fuzz testing (testing programs with large numbers of randomly generated inputs to find bugs) belongs to software security. The paper's analysis of baselines, benchmark programs, metrics, and number of trials is a textbook example of how to evaluate a new tool.

### E1

- Location: §1 Introduction
- Quote: "When a researcher develops a new fuzzer algorithm (call it A), they must empirically demonstrate that it provides an advantage over the status quo. To do this, they must choose:" / "a compelling baseline fuzzer B to compare against" / "a sample of target programs—the benchmark suite" / "a meaningful set of configuration parameters"
- Key point: To evaluate a new fuzzing algorithm, you must choose a compelling baseline, a sample of target programs (a benchmark suite), a performance metric, and meaningful configuration parameters (such as seed inputs and timeout), and account for randomness.

### E2

- Location: Abstract
- Quote: "We surveyed the recent research literature and assessed the experimental evaluations carried out by 32 fuzzing papers. We found problems in every evaluation we considered."
- Key point: The authors examined the experimental evaluations of 32 fuzzing papers and found problems in every one.

### E3

- Location: §9 Conclusions and Future Work
- Quote: "Our experiments showed AFLFast performs well on the targets it was originally assessed against, but performed no better than AFL on two targets used by other papers."
- Key point: A published new tool performed well on the targets its paper chose, but no better than the baseline on two targets used by other papers.

### E4

- Location: §9 Conclusions and Future Work
- Quote: "Many papers measured fuzzer performance not by counting distinct bugs, but instead by counting “unique crashes” using heuristics" / "the heuristics can dramatically over-count the number of bugs, and indeed may suppress bugs by wrongly grouping crashing inputs. This means that apparent improvements may be modest or illusory."
- Key point: Many papers use the heuristic "unique crashes" count instead of counting distinct bugs; this can dramatically over-count bugs, so apparent improvements may be small or nonexistent.

### E5

- Location: §9 Conclusions and Future Work
- Quote: "multiple trials with statistical tests to distinguish distributions" / "a range of benchmark target programs with known bugs" / "a consideration of various (well documented) seed choices including empty seed" / "timeouts of at least 24 hours, or else justification for less, with performance plotted over time"
- Key point: The authors recommend multiple trials with statistical tests, a range of benchmark programs with known bugs, measuring performance by known bugs, considering various well-documented seed choices, and timeouts of at least 24 hours (or a justification for less) with performance plotted over time.

### E6

- Location: §1 Introduction
- Quote: "Fuzzing performance can vary over the course of a run. This means that short timeouts (of less than 5 or 6 hours, as used by 11 papers) may paint a misleading picture."
- Key point: Performance changes over a run, so short timeouts can mislead; the paper shows a case where one fuzzer leads at 6 hours and the other at 24 hours.

### E7

- Location: §8 Target Programs
- Quote: "If a static benchmark suite comes into common use, tools may start to employ heuristics and strategies that are not of fundamental advantage, but apply disproportionately to the benchmark programs."
- Key point: Once a static benchmark suite comes into common use, tools may start to use heuristics that bring no fundamental advantage but help disproportionately on the benchmark programs.

### E8

- Location: §5 Seed Selection
- Quote: "Papers should be specific about how the seeds were collected, and better still to make available the actual seeds used."
- Key point: Papers should be specific about how the seeds were obtained, and better still, release the actual seeds used.

### E9

- Location: §1 Introduction
- Quote: "Fuzzing performance under the same configuration can vary substantially from run to run."
- Key point: Under the same configuration, results can vary substantially from run to run.

### E10

- Location: §1 Introduction
- Quote: "An evaluation should also account for the fundamentally random nature of fuzzing" / "an evaluation should measure sufficiently many trials to sample the overall distribution that represents the fuzzer's performance, using a statistical test to determine that A's measured improvement over B is real, rather than due to chance."
- Key point: Fuzzing is fundamentally random, so an evaluation must run enough trials to sample the performance distribution and use a statistical test to confirm that A's improvement over B is real rather than chance.

### E11

- Location: §1 Introduction
- Quote: "on nm, one AFL run found just over 1200 crashing inputs while one AFLFast run found around 800. Yet, comparing the median of 30 runs tells a different story: 400 crashes for AFL and closer to 1250 for AFLFast."
- Key point: Comparing single runs can give the opposite conclusion: in one run AFL found more crashes than AFLFast, but the median of 30 runs was about 400 for AFL and closer to 1,250 for AFLFast.

### E12

- Location: §1 Introduction
- Quote: "short timeouts (of less than 5 or 6 hours, as used by 11 papers) may paint a misleading picture."
- Key point: Performance varies over a run, and short timeouts (under 5 to 6 hours) can paint a misleading picture; some comparisons reverse between 6 and 24 hours.

### E13

- Location: §1 Introduction
- Quote: "We similarly found substantial performance variations based on the seeds used" / "most papers treated the choice of seed casually, apparently assuming that any seed would work equally well, without providing particulars."
- Key point: Performance varies substantially with the seed inputs, yet most papers chose seeds casually, apparently assuming any seed works equally well, and gave no details.

### E14

- Location: §4 Statistically Sound Comparisons
- Quote: "Mann Whitney is non parametric in that it makes no assumption about the distribution of a randomized algorithm's performance; by contrast, the standard t-test assumes a normal distribution."
- Key point: For randomized algorithms, the authors recommend the Mann-Whitney U test: it is non-parametric and makes no assumption about the performance distribution, whereas the standard t-test assumes normality.

### E15

- Location: §4 Statistically Sound Comparisons
- Quote: "Just because A is likely to be better than B doesn't tell us how much better it is." / "Bootstrap methods can also be employed here."
- Key point: Knowing A is likely better than B does not tell you how much better; you also need an effect size, for example the Vargha-Delaney A12 statistic or bootstrap methods.

### E16

- Location: §9 Conclusions
- Quote: "multiple trials with statistical tests to distinguish distributions" / "a range of benchmark target programs with known bugs" / "measurement of performance in terms of known bugs, rather than heuristics based on AFL coverage profiles or stack hashes" / "timeouts of at least 24 hours, or else justification for less, with performance plotted over time"
- Key point: Recommended evaluation elements: multiple trials with statistical tests; a range of target programs with known bugs; performance measured in known bugs rather than heuristics; timeouts of at least 24 hours (or a justification for less) with performance plotted over time; and various well-documented seed choices, including an empty seed.

### E17

- Location: §9 Conclusions
- Quote: "the heuristics can dramatically over-count the number of bugs, and indeed may suppress bugs by wrongly grouping crashing inputs."
- Key point: Deduplicating with heuristics such as "unique crashes" can dramatically over-count bugs, or suppress bugs by wrongly grouping crashing inputs, so the observed improvement may be small or even spurious.

### E18

- Location: §9 Conclusions
- Quote: "Our experiments showed AFLFast performs well on the targets it was originally assessed against, but performed no better than AFL on two targets used by other papers." / "which have the advantage that they are defined independently of a given algorithm"
- Key point: AFLFast performed well on the targets in its original paper but no better than AFL on two targets used by other papers. Synthetic benchmark suites (such as CGC and LAVA-M) have the advantage of being defined independently of any given algorithm, with bugs that can be counted reliably.

### E19

- Location: §1 Introduction
- Quote: "We found that no fuzz testing evaluation carries out all of the above steps properly (though some get close)."
- Key point: None of the 32 surveyed papers carried out all the steps properly in its evaluation.

### E20

- Location: §1 Introduction
- Quote: "This is bad news in theory, and after carrying out more than 50000 CPU hours of experiments, we believe it is bad news in practice, too." / "We found that experiments that deviate from the above recipe could easily lead one to draw incorrect conclusions"
- Key point: After more than 50,000 CPU hours of experiments, the authors found that experiments deviating from the recommended practice easily lead to wrong conclusions; the problem is not only theoretical.

### E21

- Location: §1 Introduction
- Quote: "We chose AFLFast as it was a recent advance over the state of the art; its code was publicly available; and we were confident in our ability to rerun the experiments described by the authors in their own evaluation and expand these experiments by varying parameters that the original experimenters did not."
- Key point: They chose AFLFast for the demonstration because it was a recent advance, its code was public, they could rerun the original authors' experiments, and they could extend them by varying parameters the authors had not varied.

### E22

- Location: §3 Overview and Experimental Setup
- Quote: "our goal is not to reproduce AFLFast’s results, but rather to use it as a representative “advanced” fuzzer for purposes of considering (in)validity of approaches to empirically evaluating fuzzers."
- Key point: The goal of the experiments was not to reproduce a paper's results, but to use it as a representative example for testing whether different evaluation practices hold up.

### E23

- Location: Table 1 (§3); §4 Statistically Sound Comparisons
- Quote: "Table 1: Summary of past fuzzing evaluation. Blank cell means that the paper’s evaluation did not mention this item" / "Table 1 shows that most (17 out of 32) fuzzing papers we considered make no mention of the number of trials performed."
- Key point: Table 1 summarizes the evaluation practices of the surveyed papers (a blank cell means the paper did not mention the item); for example, 17 of the 32 papers did not mention how many trials they ran.

### E24

- Location: §9 Conclusions and Future Work
- Quote: "multiple trials with statistical tests to distinguish distributions" / "timeouts of at least 24 hours, or else justification for less, with performance plotted over time"
- Key point: The authors give concrete evaluation advice, such as running multiple trials and comparing distributions with statistical tests, and using timeouts of at least 24 hours (or justifying shorter ones) with performance plotted over time.
