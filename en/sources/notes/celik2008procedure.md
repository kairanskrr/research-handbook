# Celik et al. 2008: Procedure for Estimation and Reporting of Uncertainty Due to Discretization in CFD Applications

- Source: `celik2008procedure`, [Original](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Shop/Journals/JFENumAccuracy.pdf)
- Version: PDF publicly available on the ASME website (in one file with the Journal of Fluids Engineering's numerical accuracy policy statement); final version published in Journal of Fluids Engineering 130(7), 078001, 2008. Read 2026-10-06. Locations are given as subsections or steps.

### E1

- Location: Preliminaries
- Quote: "Before any discretization error estimation is calculated, it must be shown that iterative convergence is achieved with at least three (preferably four) orders of magnitude decrease in the normalized residuals for each equation solved."
- Key point: Before estimating discretization error, show that iterative convergence has been reached: normalized residuals for each equation must drop by at least three (preferably four) orders of magnitude.

### E2

- Location: Recommended Procedure, Step 2
- Quote: "Select three significantly different sets of grids, and run simulations to determine the values of key variables important to the objective of the simulation study [...] It is desirable that the grid refinement factor, r=hcoarse/hfine, be greater than 1.3. This value of 1.3 is based on experience, and not on formal derivation."
- Key point: Run on three significantly different grids; the grid refinement factor (coarse cell size / fine cell size) should preferably exceed 1.3. This value is empirical, not derived.

### E3

- Location: Preliminaries
- Quote: "Here we recommend that the degree of sensitivity of the presented solution to small perturbations in the inlet conditions be studied and reported."
- Key point: Uncertainty in inlet boundary conditions can be a major source of overall uncertainty; study and report how sensitive the solution is to small perturbations in inlet conditions.

### E4

- Location: Preliminaries
- Quote: "If authors choose to use it, the method per se will not be challenged in the paper review process."
- Key point: Authors who use the recommended Grid Convergence Index (GCI) method will not have the method itself challenged in review; those who use another method must show in review that it is appropriate.

### E5

- Location: Example following Step 5
- Quote: "the numerical uncertainty in the fine-grid solution for the reattachment length should be reported as 2.2%; note that this does not account for modeling errors."
- Key point: In the example, the numerical uncertainty of the fine-grid solution is reported as 2.2%; this figure does not include modeling error.

### E6

- Location: Discretization Error Bars
- Quote: "When computed profiles of a certain variable are presented, it is recommended that numerical uncertainty be indicated by error bars on the profile, analogous to experimental uncertainty."
- Key point: When plotting computed profiles, show numerical uncertainty with error bars, as you would experimental uncertainty.
