# Alexopoulos & Kim 2002: Output Data Analysis for Simulations

- Source: `alexopoulos2002output`, [original (Winter Simulation Conference proceedings, open access at informs-sim.org)](https://www.informs-sim.org/wsc02papers/012.pdf)
- Version: Proceedings of the 2002 Winter Simulation Conference, pp. 85–96.

### E1

- Location: §1 Introduction
- Quote: "Unfortunately, a simulation run does not usually produce independent, identically distributed (i.i.d.) observations; therefore “classical” statistical techniques are not directly applicable to the analysis of simulation output."
- Key point: A simulation run does not usually produce independent, identically distributed (i.i.d.) observations, so classical statistical techniques cannot be applied directly to simulation output.

### E2

- Location: §1 Introduction
- Quote: "Finite-horizon simulations. In this case the simulation starts in a speciﬁc state and runs until a terminating event occurs." / "Steady-state simulations. The purpose of a steady-state simulation is the study of the long-run behavior of the system of interest."
- Key point: There are two kinds of simulation: finite-horizon (terminating) simulations start in a specific state and run until a terminating event; steady-state simulations study the long-run behavior of the system.

### E3

- Location: §2 Finite-Horizon Simulations
- Quote: "To overcome this problem, we can run k independent replications of the simulation."
- Key point: Data within one run are correlated and make variance hard to estimate; the remedy is to run multiple independent replications.

### E4

- Location: §3 Initialization Problems for Steady-State Simulations
- Quote: "One of the hardest problems in steady-state simulations is the removal of the initialization bias."
- Key point: One of the hardest problems in steady-state simulation is removing the initialization bias.

### E5

- Location: §3 Initialization Problems for Steady-State Simulations
- Quote: "The most commonly used method for eliminating the bias" / "because the initial conditions primarily affect data at the beginning of a run"
- Key point: The most common method is to truncate the observations at the start of the run (the warm-up period), because initial conditions mainly affect the data at the beginning of a run.

### E6

- Location: §3 Initialization Problems for Steady-State Simulations
- Quote: "The graphical procedure of Welch (1983) is popular due to its simplicity and generality. This method uses k independent runs" / "the procedure plots the moving averages" / "If the plot is reasonably smooth, then l is chosen to be the value of j beyond which the sequence of moving averages converges."
- Key point: To choose the truncation point (the warm-up length), Welch's graphical procedure is popular for its simplicity and generality: average the results of several independent runs, plot the moving average, and truncate where the curve starts to converge.

### E7

- Location: §4.1 The Replication/Deletion Approach
- Quote: "This approach runs k independent replications, each of length l + n observations, and discards the ﬁrst l observations from each run. One then uses the i.i.d. sample means"
- Key point: The replication/deletion approach: run k independent replications, discard the first l observations of each, and then use the sample means of the runs (which are i.i.d.) for inference.

### E8

- Location: §4.1 The Replication/Deletion Approach
- Quote: "The systematic error in the sample means Yi(l, n) cannot be reduced by increasing the number of replications k."
- Key point: The systematic error caused by the initial state cannot be reduced by increasing the number of replications.
