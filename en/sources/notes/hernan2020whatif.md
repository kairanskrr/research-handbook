# Hernán & Robins: Causal Inference: What If

- Source: `hernan2020whatif`, [Free PDF on the authors' website](https://miguelhernan.org/whatifbook)
- Version: PDF version of August 19, 2026, from the authors' website (suggested citation: Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC). We read only Section 3.6 and the opening parts of Chapters 7, 8, and 9.

### E1

- Location: Chapter 3, Section 3.6 The target trial
- Quote: "For each causal effect that we wish to estimate using observational data, we may (i) specify the protocol of the target trial that we would like to, but cannot, conduct, and (ii) describe how the observational data would be used to emulate that target trial."
- Key point: For every causal effect you want to estimate from observational data, you can (1) specify the protocol of the target trial you would like to, but cannot, conduct, and (2) describe how the observational data would be used to emulate it.

### E2

- Location: Chapter 3, Section 3.6 The target trial
- Quote: "The eligibility criteria need to be selected so that all individuals could in principle receive all treatments of interest"
- Key point: Eligibility criteria should be chosen so that every individual could in principle receive every treatment of interest.

### E3

- Location: Chapter 3, Section 3.6 The target trial
- Quote: "This comparison implies emulating a target trial in which individuals are assigned to an instantaneous, and possibly very large, weight change at the start of follow-up." / "e.g., one in which some individuals are assigned to lose 5% of body mass index every year, starting at age 40 and for as long as their body mass index stays over 25."
- Key point: Directly comparing the mortality of people with a body mass index of 25 versus 30 at the start of follow-up amounts to emulating a trial of an instantaneous, possibly very large weight change; a more realistic intervention would be, for example, losing 5% of body mass index each year from age 40 for as long as it is above 25.

### E4

- Location: Chapter 7, Section 7.1 The structure of confounding
- Quote: "The effect of working as a firefighter A on the risk of death Y will be confounded if "being physically fit" L is a cause of both being an active firefighter and having a lower mortality risk."
- Key point: If "being physically fit" both makes people able to work as firefighters and lowers their mortality, the effect of being a firefighter on death is confounded (the healthy worker bias).

### E5

- Location: Chapter 7, Section 7.1 The structure of confounding
- Quote: "subclinical disease U results both in lack of exercise A and an increased risk of clinical disease Y . This form of confounding is often referred to as reverse causation when L is unknown."
- Key point: Subclinical disease can both reduce exercise and increase the risk of clinical disease; this form of confounding is often called "reverse causation."

### E6

- Location: Chapter 7, Section 7.4 Confounding and confounders
- Quote: "These examples show that associational or statistical criteria are insufficient to characterize confounding."
- Key point: Associational or statistical criteria alone are insufficient to characterize confounding.

### E7

- Location: Chapter 7, Section 7.4 Confounding and confounders
- Quote: "A structural approach to confounding emphasizes that causal inference from observational data requires a priori causal knowledge." / "Second, the researchers' assumptions about confounding become explicit and therefore can be explicitly criticized by other investigators."
- Key point: Causal inference from observational data requires a priori causal knowledge; drawing it as a causal diagram makes the researchers' assumptions about confounding explicit, so others can explicitly criticize them.

### E8

- Location: Chapter 7, Section 7.6 Confounding adjustment
- Quote: "At the very least, investigators should generally avoid adjustment for variables affected by either the treatment or the outcome."
- Key point: At the very least, generally avoid adjusting for variables affected by the treatment or the outcome.

### E9

- Location: Chapter 7, Section 7.6 Confounding adjustment
- Quote: "Of course, thoughtful and knowledgeable investigators could believe that two or more causal structures, possibly leading to different conclusions regarding confounding and confounders, are equally plausible. In that case they would perform multiple analyses and explicitly state the assumptions about causal structure required for the validity of each."
- Key point: If two or more causal structures are equally plausible, run an analysis under each and state the causal assumptions each one relies on.

### E10

- Location: Chapter 7, Section 7.6 Confounding adjustment
- Quote: "The critic is not making a scientific statement, but a logical one." / "Your next move is to try and adjust for smoking or, if data on smoking could not be obtained, to conduct a sensitivity analysis to investigate the possible bias induced by smoking."
- Key point: Saying "your study may be confounded" is not a scientific criticism, since any observational study may be; a useful critique names a specific confounder (such as smoking). The researcher should then adjust for it, or, if the data are unavailable, run a sensitivity analysis.

### E11

- Location: Chapter 7, Section 7.3 Confounding and the backdoor criterion
- Quote: "If the confounders are unknown, one can only guess what the magnitude of the bias is. Educated guesses can be organized by conducting sensitivity analyses (i.e., repeating the analyses under several assumptions regarding the magnitude of the bias)"
- Key point: When confounders are unknown, you can only guess the size of the bias; sensitivity analyses organize these educated guesses by repeating the analysis under several assumptions about the bias's magnitude.

### E12

- Location: Chapter 8, Selection bias (opening)
- Quote: "An association created as a result of the process by which individuals are selected into the analysis is referred to as selection bias. Unlike confounding, this type of bias is not due to the presence of common causes of treatment and outcome, and can arise in both randomized experiments and observational studies."
- Key point: An association created by the process that selects individuals into the analysis is called selection bias; unlike confounding, it does not come from common causes of treatment and outcome, and it can arise in both randomized experiments and observational studies.

### E13

- Location: Chapter 8, Section 8.2 Examples of selection bias
- Quote: "Regardless of the reasons why data on Y are missing, restricting the analysis to individuals with complete data (C = 0) may result in bias."
- Key point: Whatever the reason outcome data are missing, restricting the analysis to individuals with complete data can introduce bias.

### E14

- Location: Chapter 8, Fine Point: Selection bias in case-control studies
- Quote: "In this particular case-control study, the investigator decided to select controls (Y = 0) preferentially among women with a hip fracture." / "If individuals with hip fracture are oversampled as controls, then the probability of control selection depends on a consequence of treatment A (as represented by the path from A to C) and "inappropriate control selection" bias will occur."
- Key point: Example: a case-control study of postmenopausal estrogen and coronary heart disease preferentially selected controls among women with hip fractures; since estrogen reduces hip fractures, control selection depended on a consequence of the exposure, creating bias from inappropriate selection of controls.

### E15

- Location: Chapter 8, Section 8.3 Selection bias and confounding
- Quote: "Hence a key difference between confounding and selection bias: randomization protects against confounding, but not against selection bias when the selection occurs after the randomization."
- Key point: A key difference between confounding and selection bias: randomization protects against confounding but not against selection bias that occurs after randomization.

### E16

- Location: Chapter 9, Measurement bias (opening)
- Quote: "Since measurement errors can occur under any study design--including both randomized experiments and observational studies--measurement bias need always be considered when interpreting effect estimates."
- Key point: Measurement error can occur under any design, so measurement bias must always be considered when interpreting effect estimates.

### E17

- Location: Chapter 9, Section 9.2 The structure of measurement error
- Quote: "if alcohol intake is ascertained by recall after delivery--because recall may be affected by the outcome of the pregnancy." / "The resulting measurement bias in these two examples is often referred to as recall bias."
- Key point: Example: in a study of alcohol during pregnancy and birth defects, asking mothers to recall their intake after delivery lets the outcome of the pregnancy affect recall; this is recall bias.

### E18

- Location: Chapter 9, Section 9.2 The structure of measurement error
- Quote: "The best method to fight bias due to mismeasurement is, obviously, to improve the measurement procedures for the variables used in our analysis."
- Key point: The best way to fight measurement bias is to improve the measurement procedures for the variables.

### E19

- Location: Chapter 8, Section 8.2 Examples of selection bias
- Quote: "For example, selection bias may arise when treatment is measured as the lifetime exposure to certain factor (medical treatment, lifestyle behavior...) in a study that recruited 50 year-old participants."
- Key point: Example: recruiting 50-year-olds but studying lifetime exposure as the treatment can create selection bias (the exposure affects who survives to 50 and enters the study).
