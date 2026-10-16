# Georges, Buytaert & Eeckhout 2007: Statistically Rigorous Java Performance Evaluation

- Source: `georges2007statistically`, [Original (website of co-author Dries Buytaert)](https://dri.es/files/oopsla07-georges.pdf)
- Version: OOPSLA 2007, PDF made public by the authors.
- Note: Aimed at systems with a managed runtime such as Java (virtual machine, just-in-time compilation, garbage collection); the authors point out that many of the issues also apply to other languages and systems.

### E1

- Location: §1 Introduction
- Quote: "Some report the average performance number across multiple runs of the same experiments; others report the best performance number, others report the second best performance number and yet others report the worst."
- Key point: Current practice varies widely: some report the average over multiple runs, others the best run, others the second best, and yet others the worst.

### E2

- Location: §1 Introduction, discussion of Figure 1
- Quote: "Similarly, based on the best method, one would conclude that SemiSpace clearly outperforms GenCopy. The reality though is that the confidence intervals for both garbage collectors overlap and, as a result, the performance difference seen between both garbage collectors is likely due to the random performance variations in the system under measurement."
- Key point: Reporting only the best of 30 runs would suggest one garbage collector is clearly faster; but the confidence intervals overlap, so the difference is likely just random fluctuation.

### E3

- Location: §1 Introduction (contributions)
- Quote: "For start-up performance, we advise to: (i) take multiple measurements where each measurement comprises one VM invocation and a single benchmark iteration" / "in each of these measurements, collect performance numbers for different iterations once performance reaches steady-state, i.e., after the start-up phase"
- Key point: Measure start-up and steady-state performance separately: for start-up, each measurement is one VM invocation with a single benchmark iteration; for steady state, run multiple iterations per invocation and collect data only once performance reaches steady state; in both cases compute confidence intervals across multiple VM invocations.

### E4

- Location: §1 Introduction (contributions)
- Quote: "statistics, and in particular confidence intervals, enable one to determine whether differences observed in measurements are due to random fluctuations in the measurements or due to actual differences in the alternatives compared against each other."
- Key point: Confidence intervals help determine whether an observed difference is due to random fluctuation in the measurements or to an actual difference between the alternatives compared.
