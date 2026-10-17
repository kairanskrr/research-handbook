# Raji et al. 2021: AI and the Everything in the Whole Wide World Benchmark

- Source: `raji2021everything`, [arXiv:2111.15366](https://arxiv.org/abs/2111.15366)
- Version: arXiv v1 (November 26, 2021), the NeurIPS 2021 Track on Datasets and Benchmarks paper.
- Note: a machine learning position paper that uses ImageNet and GLUE as examples to criticize treating a single benchmark as a measure of "general" ability, and discusses the construct validity problems involved.

### E1

- Location: §2.2 A Brief History of Benchmarking Practice in AI
- Quote: "In this paper we describe a benchmark as a particular combination of a dataset or sets of datasets (at least test data, sometimes also training data), and a metric, conceptualized as representing one or more specific tasks or sets of abilities, picked up by a community of researchers as a shared framework for the comparison of methods."
- Key point: A benchmark is a dataset (at least test data) plus a metric, taken to represent specific tasks or abilities and adopted by a research community as a shared framework for comparing methods.

### E2

- Location: §2.3 Construct Validity
- Quote: "in the context of machine learning, how well the benchmark dataset, and associated metrics of evaluation, represents a task"
- Key point: In machine learning, construct validity is how well a benchmark dataset and its evaluation metrics represent the task.

### E3

- Location: §4.1 Limited Task Design
- Quote: "Instead, what we observe looks more like samples of convenience: tasks and collections of tasks arbitrarily built out of what is easily available to the team developing these benchmarks, even if such constructions are theoretically unsound."
- Key point: The tasks in so-called "general" benchmarks look more like samples of convenience: built from whatever the benchmark team had at hand, even when that is theoretically unsound.

### E4

- Location: §4.1.1 Arbitrarily Selected Tasks and Collections (quoting Wagstaff 2012)
- Quote: "Legions of (ML) researchers have chased after the best iris or mushroom classifier. Yet this flurry of effort does not seem to have had any impact on the fields of botany or mycology."
- Key point: Legions of researchers chased the best iris or mushroom classifier with almost no impact on botany or mycology: benchmark tasks need not match any problem people actually care about.

### E5

- Location: §4.2 De-contextualized Data and Performance Reporting
- Quote: "No dataset is neutral and there are inherent limits to what a benchmark can tell us" / "the claim to generality will often act as cover, allowing those developing the benchmarks to escape the responsibility of reporting details of these limitations."
- Key point: No dataset is neutral and benchmarks can tell us only so much; claims of generality often serve as cover for not reporting limitations.

### E6

- Location: §4.2.2 Benchmark Subjectivity
- Quote: "when analyzing country level geo-location data for the 2011 version of the dataset, 45% of the images were found to be sourced from the US, and over 60% from a small selection of Western countries in North America and Europe"
- Key point: In the 2011 version of ImageNet, 45% of images came from the US and over 60% from a few North American and European countries: skews in data sources carry into the benchmark.

### E7

- Location: §4.3.3 Justification for Practical out of Context or Unsafe Applications
- Quote: "Poor performance on minority subgroups could possibly be disguised in aggregate and decontextualized "general" benchmarks to justify deployment."
- Key point: Reporting only aggregate scores can hide poor performance on minority subgroups.

### E8

- Location: §5 Alternative Roles for Benchmarking and Alternative Evaluation Methods
- Quote: "First, we argue that benchmarks should be developed, presented and understood as intended [...] to evaluate concrete, well-scoped and contextualized tasks."
- Key point: Benchmarks should be built, presented, and understood for their intended purpose: evaluating concrete, well-scoped, contextualized tasks.

### E9

- Location: §4.2.1 Limited Scope
- Quote: "ImageNet authors note the trade-off between annotation quality and size, remarking that "the scale [is] already imposing limits on the manual annotations that are feasible to obtain""
- Key point: The ImageNet authors themselves noted a trade-off between annotation quality and size: scale already limits how much manual annotation can be obtained.

### E10

- Location: §6 Conclusion
- Quote: "Benchmarking, appropriately deployed, is not about winning a contest but more about surveying a landscape"
- Key point: Benchmarking, used appropriately, is less about winning a contest than about surveying a landscape.
