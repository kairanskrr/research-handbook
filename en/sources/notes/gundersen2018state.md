# Gundersen & Kjensmo 2018: State of the Art: Reproducibility in Artificial Intelligence

- Source: `gundersen2018state`, [Original](https://ojs.aaai.org/index.php/AAAI/article/view/11503)
- Version: AAAI-18 proceedings, pp. 1644–1651. The full-text PDF is free on the AAAI publisher's website. The paper surveys 400 papers from two AI conferences, IJCAI and AAAI, and counts how much of the information needed for reproducibility they document.

### E1

- Location: The Terminology of Reproducibility
- Quote: "While researchers in computer science agree that empirical results should be reproducible, what is meant by reproducibility is neither clearly defined nor agreed upon."
- Key point: Computer science researchers agree that empirical results should be reproducible, but what reproducibility means is neither clearly defined nor agreed upon.

### E2

- Location: Degrees of Reproducibility
- Quote: "R1: Experiment Reproducible The results of an experiment are experiment reproducible when the execution of the same implementation of an AI method produces the same results when executed on the same data." / "R2: Data Reproducible The results of an experiment are data reproducible when an experiment is conducted that executes an alternative implementation of the AI method that produces the same results when executed on the same data." / "R3: Method Reproducible The results of an experiment are method reproducible when the execution of an alternative implementation of the AI method produces the same results when executed on different data."
- Key point: Three degrees of reproducibility: R1, same implementation and same data; R2, different implementation and same data; R3, different implementation and different data.

### E3

- Location: Degrees of Reproducibility
- Quote: "R1 reproducible results are less general than R2 reproducible results, which in turn are less general than R3 reproducible results."
- Key point: From R1 to R3, the reproduced results become increasingly general.

### E4

- Location: Introduction
- Quote: "Out of 402 experimental papers they were able to repeat 32.3% without communicating with the author, rising to 48.3% with communication."
- Key point: Summarizing Collberg & Proebsting 2016: of 402 experimental papers, 32.3% could be repeated without contacting the authors, rising to 48.3% with contact.

### E5

- Location: Reproducibility
- Quote: "Most importantly, other researchers can be expected to be more objective. They have no interest in inflating the performance of a method they have not developed themselves. More practically, they will not share the same preconceptions and implicit knowledge as the first team reporting the research."
- Key point: Independent teams are more objective: they have no interest in inflating the performance of someone else's method, and they do not share the original team's preconceptions and unwritten implicit knowledge.

### E6

- Location: Reproducibility
- Quote: "An independent research team is one that conducts the experiment by only using the documentation made by the original research team."
- Key point: The paper defines an independent research team as one that conducts the experiment using only the documentation left by the original team.

### E7

- Location: Reproducibility; Degrees of Reproducibility
- Quote: "What constitutes the same results depends on to which degree the results are reproduced." / "In order for a result to be R3 reproducible the results of the experiments must support the same hypotheses and thus support the same beliefs."
- Key point: What counts as "the same results" depends on the degree of reproduction; for R3, the results must support the same hypotheses.

### E8

- Location: Degrees of Reproducibility
- Quote: "The results when re-running the experiment should be exactly the same, as reported in the original experiment." / "The results that are produced, the performance, using a different implementation should be the same if not exactly the same. Differences in results can be attributed to different implementations and hardware, such as different ways of doing floating point arithmetic."
- Key point: R1 (same implementation, same data) should give exactly the same results; R2 (a different implementation) should give the same if not exactly the same results, with differences attributable to implementation and hardware, such as how floating-point arithmetic is handled.

### E9

- Location: Abstract
- Quote: "None of the papers document all of the variables. The metrics show that between 20% and 30% of the variables for each factor are documented."
- Key point: None of the surveyed papers documented all the information needed for reproduction; only 20% to 30% of the variables for each of the three factors (method, data, experiment) were documented.
