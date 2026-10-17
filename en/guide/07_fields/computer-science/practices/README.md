# Research practices specific to computer science

This section covers five research practices used mainly in computer science, and especially in software engineering. They describe how this community actually does the work and what reviewers actually check: how to choose benchmarks, how to mine data from GitHub, how to prepare for artifact evaluation, and so on.

| Practice | In one sentence | Where the general part lives |
|---|---|---|
| [Engineering research](engineering_research.md) | Propose a new method, tool, or system, and show through evaluation that it is better | [Building and improving](../../../05_research-strategies/build_improve.md) |
| [Optimization studies](optimization_study.md) | Frame the problem as "find the best among many candidate solutions", solve it with a search algorithm, then compare approaches over repeated runs | [Building and improving](../../../05_research-strategies/build_improve.md), [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md) |
| [Benchmarking](benchmarking.md) | Compare systems, tools, or models on a standard workload, using an automated, repeatable procedure | [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md), [Measurement](../../../05_research-strategies/measure.md) |
| [Mining software repositories](repository_mining.md) | Extract data at scale from code repositories, bug trackers, and Q&A sites to study how software gets built | [Description](../../../05_research-strategies/observe_describe.md) |
| [Theoretical research](theoretical_research.md) | Produce theorems and proofs, including complexity analysis and formal verification | [Proof](../../../05_research-strategies/prove.md) |

**Why these live under computer science** `[Our analysis]`: this handbook keeps its how-to pages in two places. Methods used by two or more fields (questionnaires, interviews, controlled experiments, reviews, and so on) go in `06_methods/`; practices used by only one field go under that field's `practices/` folder. Both kinds are listed in the [Research types](../../../06_methods/README.md) section. The concrete details of the five practices above (how to choose baselines and benchmarks, the pitfalls of git data, artifact badges, machine-checked proofs, and so on) come mainly from computer science sources, so they live here.

**How they divide the work with the strategy pages** `[Our analysis]`: what kind of knowledge this research produces, what evidence it generally needs, and why you must compare against strong baselines are covered on the strategy pages in the third column of the table above, which apply to every field. The pages here cover only how it is done in computer science and link back for the general part. For the research strategies computer science commonly uses and the evidence each one relies on, see the [computer science field overview](../README.md#common-strategies-and-standards-of-evidence).

Methods that other fields also use (quantitative simulation, data science, replication studies, and so on) come up in computer science too; they are listed at the end of the [computer science field overview](../README.md#kinds-of-research).
