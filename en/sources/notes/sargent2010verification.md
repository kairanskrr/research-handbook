# Sargent 2010: Verification and Validation of Simulation Models

- Source: `sargent2010verification`, [original (Winter Simulation Conference proceedings, open access at informs-sim.org)](https://www.informs-sim.org/wsc10papers/016.pdf)
- Version: Proceedings of the 2010 Winter Simulation Conference, pp. 166-183. The author says this tutorial is close to the 2009 version; tutorials with the same title have been updated many times at WSC.

### E1

- Location: §1 Introduction
- Quote: "Model verification is often defined as “ensuring that the computer program of the computerized model and its implementation are correct” and is the definition adopted here. Model validation is usually defined to mean “substantiation that a computerized model within its domain of applicability possesses a satisfactory range of accuracy consistent with the intended application of the model”"
- Key point: Verification ensures that the model's computer program and its implementation are correct; validation substantiates that the model, within its domain of applicability, is accurate enough for its intended purpose.

### E2

- Location: §1 Introduction
- Quote: "A model should be developed for a specific purpose (or application) and its validity determined with respect to that purpose." / "A model may be valid for one set of experimental conditions and invalid in another."
- Key point: A model should be built for a specific purpose, and its validity judged against that purpose; a model valid under one set of experimental conditions may be invalid under another.

### E3

- Location: §1 Introduction
- Quote: "The amount of accuracy required should be specified prior to starting the development of the model or very early in the model development process."
- Key point: Specify the required accuracy before model development starts or very early in it.

### E4

- Location: §1 Introduction
- Quote: "It is often too costly and time consuming to determine that a model is absolutely valid over the complete domain of its intended applicability. Instead, tests and evaluations are conducted until sufficient confidence is obtained that a model can be considered valid for its intended application"
- Key point: Proving a model absolutely valid over its whole domain is usually too costly; in practice you keep testing and evaluating until you have enough confidence that it fits its intended use.

### E5

- Location: §3 Paradigms
- Quote: "Conceptual model validation is defined as determining that the theories and assumptions underlying the conceptual model are correct and that the model representation of the problem entity is “reasonable” for the intended purpose of the model. Computerized model verification is defined as assuring that the computer programming and implementation of the conceptual model is correct."
- Key point: Conceptual model validation checks that the theories and assumptions underlying the model are correct and that its representation of the real system is reasonable; computerized model verification checks that the conceptual model was programmed and implemented correctly.

### E6

- Location: §3 Paradigms
- Quote: "Operational validation is defined as determining that the model’s output behavior has sufficient accuracy for the model’s intended purpose over the domain of the model’s intended applicability." / "Data validity is defined as ensuring that the data necessary for model building, model evaluation and testing, and conducting the model experiments to solve the problem are adequate and correct."
- Key point: Operational validation checks that the model's output is accurate enough over its domain of applicability; data validity ensures that the data needed to build, evaluate, test, and experiment with the model are adequate and correct.

### E7

- Location: §3 Paradigms
- Quote: "Verification and validation must be performed again when any model change is made. Usually several models are developed prior to obtaining a valid simulation model."
- Key point: Redo verification and validation after any model change; usually several models are built before a valid one is obtained.

### E8

- Location: §4 Validation Techniques
- Quote: "Degenerate Tests: The degeneracy of the model’s behavior is tested by appropriate selection of values of the input and internal parameters. For example, does the average number in the queue of a single server continue to increase over time when the arrival rate is larger than the service rate?" / "Extreme Condition Tests: The model structure and outputs should be plausible for any extreme and unlikely combination of levels of factors in the system."
- Key point: Degenerate tests check model behavior with chosen parameter values, e.g., whether the average queue length of a single server keeps growing when the arrival rate exceeds the service rate; extreme condition tests check that the model's structure and output stay plausible under extreme, unlikely combinations of factors.

### E9

- Location: §4 Validation Techniques
- Quote: "Comparison to Other Models: Various results (e.g., outputs) of the simulation model being validated are compared to results of other (valid) models. For example, (1) simple cases of a simulation model are compared to known results of analytic models"
- Key point: Comparison to other models: compare the model's results with those of other valid models, e.g., check simple cases of a simulation model against known results from analytic models.

### E10

- Location: §4 Validation Techniques
- Quote: "Face Validity: Individuals knowledgeable about the system are asked whether the model and/or its behavior are reasonable." / "Historical Data Validation: If historical data exist (e.g., data collected on a system specifically for building and testing a model), part of the data is used to build the model and the remaining data are used to determine (test) whether the model behaves as the system does."
- Key point: Face validity: ask people who know the system whether the model and its behavior are reasonable. Historical data validation: build the model with part of the historical data and use the rest to test whether the model behaves like the system.

### E11

- Location: §4 Validation Techniques
- Quote: "Parameter Variability - Sensitivity Analysis: This technique consists of changing the values of the input and internal parameters of a model to determine the effect upon the model’s behavior or output. The same relationships should occur in the model as in the real system." / "Those parameters that are sensitive, i.e., cause significant changes in the model’s behavior or output, should be made sufficiently accurate prior to using the model."
- Key point: Sensitivity analysis: change the model's input and internal parameters and see the effect on output; the relationships in the model should match those in the real system. Make sensitive parameters, which strongly affect output, sufficiently accurate before using the model.

### E12

- Location: §4 Validation Techniques
- Quote: "Internal Validity: Several replications (runs) of a stochastic model are made to determine the amount of (internal) stochastic variability in the model."
- Key point: (The technique Sargent calls "internal validity") Make several replications of a stochastic model to determine how much internal stochastic variability it has.

### E13

- Location: §5 Data Validity
- Quote: "data problems are often the reason that attempts to valid a model fail." / "If behavior data are not available, high model confidence usually cannot be obtained because sufficient operational validity cannot be achieved."
- Key point: Data problems are often why attempts to validate a model fail; without behavior data from the system, high confidence in the model usually cannot be obtained.

### E14

- Location: §7 Computerized Model Verification
- Quote: "In dynamic testing the computer program is executed under different conditions and the values obtained (including those generated during the execution) are used to determine if the computer program and its implementations are correct."
- Key point: Dynamic testing: run the program under different conditions and use the values obtained (including intermediate values generated during execution) to judge whether the program and its implementation are correct.

### E15

- Location: §8 Operational Validity
- Quote: "Thus if a system is not observable, which is often the case, it is usually not possible to obtain a high degree of confidence in the model. In this situation the model output behavior(s) should be explored as thoroughly as possible and comparisons made to other valid models whenever possible."
- Key point: Systems are often not observable (no operating data are available), and then high confidence in the model is usually impossible; explore the model's output behavior as thoroughly as possible and compare it with other valid models where you can.

### E16

- Location: §8.2 Comparisons of Output Behaviors
- Quote: "It is preferable to use confidence intervals or hypothesis tests for the comparisons because these allow for objective decisions." / "As a result, the use of graphs is the most commonly used approach for operational validity."
- Key point: When comparing model and system outputs, confidence intervals or hypothesis tests are preferable because they allow objective decisions; but because statistical assumptions are hard to meet and system data are scarce, graphical comparison is the most common approach in practice.

### E17

- Location: §8.2.3 Hypothesis Tests
- Quote: "The first, or type I error, is rejecting the validity of a valid model and the second, or type II error, is accepting the validity of an invalid model." / "In model validation, the model user’s risk is extremely important and must be kept small."
- Key point: Validation has two types of error: rejecting a valid model (type I) and accepting an invalid one (type II). The latter, the model user's risk, is extremely important and must be kept small.

### E18

- Location: §9 Documentation
- Quote: "Documentation on model verification and validation is usually critical in convincing users of the “correctness” of a model and its results, and should be included in the simulation model documentation."
- Key point: Documentation of verification and validation is usually critical for convincing users of the "correctness" of a model and its results, and should be part of the model documentation.

### E19

- Location: §10 Recommended Procedure
- Quote: "3. Test, wherever possible, the assumptions and theories underlying the simulation model. 4. In each model iteration, at least perform face validity on the conceptual model. 5. In each model iteration, at least explore the simulation model’s behavior using the computerized model. 6. In at least the last model iteration, make comparisons, if possible, between the simulation model and system behavior (output) data for at least a few sets of experimental conditions, and preferably for several sets."
- Key point: Part of Sargent's recommended minimum procedure: test the assumptions and theories underlying the model wherever possible; in each model iteration, at least check face validity of the conceptual model and explore the computerized model's behavior; at least in the final iteration, compare model output with real system data under several sets of experimental conditions.

### E20

- Location: §3 Paradigms
- Quote: "Verification and validation must be performed again when any model change is made."
- Key point: Redo verification and validation after any model change.
