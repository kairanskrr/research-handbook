# Heiser: Systems Benchmarking Crimes

- Source: `heiserbenchmarking`, [Original](https://gernot-heiser.org/benchmarking-crimes.html)
- Version: Web page, continually updated; accessed 2026-10-05.
- Note: Common benchmarking mistakes in systems papers, compiled by Gernot Heiser (UNSW Sydney) from his reviewing experience. Most examples come from operating systems, but the author says the basic principles apply generally.

### E1

- Location: Benchmarking Crimes (opening)
- Quote: "I call such cases benchmarking crimes. Not because you can go to jail for them (but probably should?) but because they undermine the integrity of the scientific process."
- Key point: They are called "crimes" because they undermine the integrity of the scientific process.

### E2

- Location: Selective benchmarking
- Quote: "This is the mother of all benchmarking crimes: using a biased set of benchmarks to (seemingly) prove a point, which might be contradicted by a broader coverage of the evaluation space."
- Key point: Selective benchmarking is "the mother of all benchmarking crimes": using a biased set of benchmarks to seemingly prove a point that broader coverage of the evaluation space might contradict.

### E3

- Location: Not evaluating potential performance degradation
- Quote: "Progressive criterion: Performance actually does improve significantly in the area of interest" / "Conservative criterion: Performance does not significantly degrade elsewhere" / "If, however, you only evaluate the scenarios where your approach is beneficial, you are being deceptive."
- Key point: A fair evaluation must show two things: performance really improves significantly in the area of interest (progressive criterion), and it does not significantly degrade elsewhere (conservative criterion). Evaluating only the scenarios where your approach helps is deceptive.

### E4

- Location: Benchmark sub-setting without strong justification
- Quote: "If a subset is used, it must be well justified. There must be convincing explanation for each missing program." / "it is totally unacceptable to quote an overall figure of merit (such as average speedup) for SPEC if a subset is used!"
- Key point: If you run only part of a suite, give a convincing explanation for each missing program; if you use a subset, never report an overall figure of merit for the whole suite (such as average speedup).

### E5

- Location: Benchmark sub-setting without strong justification
- Quote: "There is no such thing as a “representative” subset of SPEC" / "Note that arbitrary is not the same as random, so a random pick would be fine."
- Key point: There is no such thing as a "representative" subset of SPEC; when choosing from many candidates, a random pick is fine but an arbitrary pick is not.

### E6

- Location: Selective data set hiding deficiencies
- Quote: "Here the range of the input parameter is picked to make the system look good, but the range is not representative of a real workload."
- Key point: The range of an input parameter is picked to make the system look good but does not represent a real workload. The original example: a database tested only up to one client per core, while the meaningful load range lies just outside the plotted range.

### E7

- Location: Pretending micro-benchmarks represent overall performance
- Quote: "Macro-benchmarks (representing real-world workloads) must be used to provide a realistic picture of overall performance."
- Key point: Micro-benchmarks test only one aspect of a system; to show overall performance you must use macro-benchmarks that represent real-world workloads.

### E8

- Location: Throughput degraded by x% ⇒ overhead is x%
- Quote: "Throughput comparisons must always be accompanied by a comparison of complete CPU load."
- Key point: An x% drop in throughput does not mean x% overhead; throughput comparisons must always be accompanied by a comparison of complete CPU load.

### E9

- Location: Downplaying overheads
- Quote: "This one is confusing percentage with percentage points" / "The original system is the baseline, and therefore must occur in the denominator when calculating relative performance."
- Key point: Common arithmetic errors: confusing percentages with percentage points (overhead going from 6% to 13% is not "7% more" but more than double), and not putting the baseline system in the denominator when calculating relative performance.

### E10

- Location: No indication of significance of data
- Quote: "In order to indicate significance, it is essential that at least standard deviations are quoted." / "If in doubt use Student's t-test to check the significance."
- Key point: At the very least, report standard deviations; for a highly deterministic system, one sentence such as "all standard deviations were below 1%" is enough; if in doubt, check significance with Student's t-test.

### E11

- Location: Arithmetic mean for averaging across benchmark scores
- Quote: "In particular the arithmetic mean has no meaning if individual benchmark scores are normalised (e.g. against a baseline system)." / "The proper way to average (i.e. arrive at a single figure of merit) is to use the geometric mean of scores"
- Key point: When scores are normalized (for example, against a baseline), the arithmetic mean has no meaning; use the geometric mean to arrive at a single figure.

### E12

- Location: Same dataset for calibration and validation
- Quote: "the calibration and evaluation workloads must be different! In fact, they must be totally disjoint."
- Key point: The workloads used to calibrate a model and those used to evaluate it must be totally disjoint.

### E13

- Location: No proper baseline
- Quote: "Consider the baseline carefully. Often it is the state-of-the-art solution. Often it is the optimal (or theoretically best) solution or a hardware limit (assuming zero software overhead)."
- Key point: Choose the baseline carefully: often it is the state-of-the-art solution, but it can also be the optimal (theoretically best) solution or a hardware limit; when comparing virtualization approaches, the real baseline is the native system.

### E14

- Location: Only evaluate against yourself
- Quote: "I want to see the significance, and that means comparing against some accepted standard."
- Key point: Comparing only against your own system from last year is not enough; compare against an accepted standard.

### E15

- Location: Unfair benchmarking of competitors
- Quote: "I'm sure you tweaked your system as well as you could, but did you really go through the same effort with the alternative?" / "If in doubt, contact the authors of that system to confirm that your measurements are fair." / "the default configuration of our open-source release had debugging enabled."
- Key point: You tuned your system as well as you could, but did you put the same effort into the alternative? Give its full configuration, be especially careful if your results disagree with its published numbers, and contact its authors if in doubt. The author's own system was once evaluated by others using a default configuration with debugging enabled.

### E16

- Location: Inflating gains by not comparing against the state of the art
- Quote: "Paper X established a new state of the art, and thus the new baseline that must be used."
- Key point: If X is 20% faster than the old baseline and a later Y is 22% faster, Y can claim only about 2% over X: the new state of the art is the new baseline that must be used.

### E17

- Location: Missing specification of evaluation platform
- Quote: "For reproducibility it is essential that the evaluation platform is well-specified, including all characteristics that may influence the results." / "Compiler versions are often also relevant, as may be the version of other tools."
- Key point: Specify every platform characteristic that may influence the results: processor architecture, number of cores, clock rate, memory, caches, network card; operating system and hypervisor versions; compiler and other tool versions.

### E18

- Location: Missing sub-benchmark results
- Quote: "Only providing the overall score can at worst hide problems, and at best reduces the insights that can be obtained from the evaluation."
- Key point: When running a benchmark suite, give the result of each sub-benchmark; giving only the overall score can at worst hide problems and at best reduces the insight the evaluation provides.

### E19

- Location: Relative numbers only
- Quote: "Always give complete result, not just ratios (unless the denominator is a standard figure)."
- Key point: Always give complete results, not just ratios; with ratios alone readers cannot sanity-check the numbers, and ratios can hide results that are actually poor or irrelevant.

### E20

- Location: Benchmarking Best Practice › General rules
- Quote: "Make sure that the system is really quiescent when starting an experiment, leave enough time to ensure all previous data is flushed out." / "Make your benchmarking rig part of your regression testing suite."
- Key point: Make sure the system is quiescent before starting an experiment, and make your benchmarking rig part of your regression testing.

### E21

- Location: Benchmarking Best Practice › Test data and results
- Quote: "Always verify the data you are transferring." / "Invert the order of measurements. This helps to identify interference between measurements."
- Key point: Always verify the data you transfer; inverting the order of measurements helps reveal interference between them.

### E22

- Location: Benchmarking Best Practice › Test data and results
- Quote: "Use a combination of successive and separate runs for the same data point."
- Key point: Combine successive and separate runs for the same data point to detect unwanted caching effects.

### E23

- Location: Benchmarking Best Practice › Statistics
- Quote: "Always do several runs, and check the standard deviation. Watch out for abnormal variance." / "only use such selective use of data if you really know what you are doing, and also state it explicitly in your paper/report."
- Key point: Always do several runs and check the standard deviation, watching for abnormal variance; drop the highest or lowest points only after formal outlier detection, and say so explicitly in the paper.

### E24

- Location: Benchmarking Best Practice › Timing
- Quote: "Use lots of iterations in order to improve statistics and remove clock granularity." / "Run sufficient warm-up iterations which aren't timed."
- Key point: Use many iterations to improve statistics and remove clock granularity, and run enough untimed warm-up iterations first.

### E25

- Location: Benchmarking of simplified simulated system
- Quote: "It is therefore essential to ensure that the simulation model does not make any simplifying assumption which will impact the performance aspect you are looking for."
- Key point: If you must evaluate on a simulated system, make sure the simulation model's simplifying assumptions do not affect the performance aspect you care about, and tell readers so.

### E26

- Location: Inappropriate and misleading benchmarks
- Quote: "Real scalability tests would run workloads which actually communicate across processors and use system calls."
- Key point: Running multiple non-communicating single-processor programs is an inappropriate benchmark for multiprocessor scalability; real scalability tests run workloads that communicate across processors and use system calls.
