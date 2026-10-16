# Sandve et al. 2013: Ten Simple Rules for Reproducible Computational Research

- Source: `sandve2013ten`, local PDF `papers/pdf/sandve2013ten.pdf`
- Version: PLoS Computational Biology 9(10): e1003285, 2013, open access

### E1

- Location: introduction
- Quote: "We want to emphasize that reproducibility is not only a moral responsibility with respect to the scientific field, but that a lack of reproducibility can also be a burden for you as an individual researcher."
- Key point: Reproducibility is not only a moral responsibility to the field; lacking it is also a burden for you as an individual researcher.

### E2

- Location: Rule 1
- Quote: "For Every Result, Keep Track of How It Was Produced" / "As a minimum, you should at least record sufficient details on programs, parameters, and manual procedures to allow yourself, in a year or so, to approximately reproduce the results."
- Key point: For every result, keep track of how it was produced; at a minimum, you yourself should be able to approximately reproduce it a year later.

### E3

- Location: Rule 2, Rule 7, Rule 9 (rule titles)
- Quote: "Avoid Manual Data Manipulation Steps" / "Always Store Raw Data behind Plots" / "Connect Textual Statements to Underlying Results"
- Key point: Avoid manual data manipulation; store the raw data behind every plot; connect every statement in the paper to an underlying result.

### E4

- Location: Rule 4
- Quote: "Version Control All Custom Scripts" / "This can cast doubt on previous results, as it may be impossible to know if they were partly the result of a bug or otherwise unfortunate behavior."
- Key point: Version control all custom scripts; otherwise you cannot return to the code state that produced a result, and cannot tell whether the result came from a bug.

### E5

> Withdrawn: duplicates [E11](#e11) (its quote is fully contained in E11).

- Location: Rule 6 (rule title)
- Quote: "For Analyses That Include Randomness, Note Underlying Random Seeds"
- Key point: For analyses that include randomness, note the random seeds.

### E6

- Location: Rule 10
- Quote: "Provide Public Access to Scripts, Runs, and Results" / "Making reproducibility of your work by peers a realistic possibility sends a strong signal of quality, trustworthiness, and transparency."
- Key point: Provide public access to scripts, runs, and results; making it realistic for peers to reproduce your work is a strong signal of quality, trustworthiness, and transparency.

### E7

- Location: Rule 1: For Every Result, Keep Track of How It Was Produced
- Quote: "Whenever a result may be of potential interest, keep track of how it was produced."
- Key point: Whenever a result may be of interest, keep track of how it was produced.

### E8

- Location: Rule 1
- Quote: "For every involved step, you should ensure that every detail that may influence the execution of the step is recorded. If the step is performed by a computer program, the critical details include the name and version of the program, as well as the exact parameters and inputs that were used."
- Key point: Record every detail of each step that may influence the result; if a program performs the step, the critical details are the program's name and version and the exact parameters and inputs.

### E9

> Withdrawn: duplicates [E2](#e2) (its quote is fully contained in E2).

- Location: Rule 1
- Quote: "As a minimum, you should at least record sufficient details on programs, parameters, and manual procedures to allow yourself, in a year or so, to approximately reproduce the results."
- Key point: At a minimum, record enough detail that you yourself could approximately reproduce the results a year later.

### E10

- Location: Rule 2: Avoid Manual Data Manipulation Steps
- Quote: "If manual operations cannot be avoided, you should as a minimum note down which data files were modified or moved, and for what purpose."
- Key point: If manual operations cannot be avoided, at least note which data files were modified or moved, and why.

### E11

- Location: Rule 4 and Rule 6 (rule titles)
- Quote: "Version Control All Custom Scripts [...] For Analyses That Include Randomness, Note Underlying Random Seeds"
- Key point: Version control all custom scripts; for analyses that include randomness, note the random seeds.

### E12

- Location: Rule 9: Connect Textual Statements to Underlying Results
- Quote: "As a minimum, you should provide enough details along with your textual interpretations so as to allow the exact underlying results, or at least some related results, to be tracked down in the future."
- Key point: Attach enough detail to every written conclusion that the exact underlying results can be tracked down in the future.

### E13

- Location: Rule 1: For Every Result, Keep Track of How It Was Produced
- Quote: "Whenever a result may be of potential interest, keep track of how it was produced." / "If the step is performed by a computer program, the critical details include the name and version of the program, as well as the exact parameters and inputs that were used."
- Key point: Whenever a result may be of interest, keep track of how it was produced; for steps done by a program, the critical details are the program's name, version, and exact parameters and inputs.
