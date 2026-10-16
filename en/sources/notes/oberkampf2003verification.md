# Oberkampf, Trucano & Hirsch 2003: Verification, Validation, and Predictive Capability in Computational Engineering and Physics

- Source: `oberkampf2003verification`, [original (public report in the University of North Texas Digital Library)](https://digital.library.unt.edu/ark:/67531/metadc885833/m2/1/high_res_d/918370.pdf); OSTI record: https://www.osti.gov/biblio/918370
- Version: Sandia National Laboratories report SAND2003-3769, February 2003, "Approved for public release."

### E1

- Location: §1.2 Basic Terminology and Methodology
- Quote: "Verification: The process of determining that a model implementation accurately represents the developer's conceptual description of the model and the solution to the model." / "Validation: The process of determining the degree to which a model is an accurate representation of the real world from the perspective of the intended uses of the model."
- Key point: Verification: determining that a model implementation accurately represents the developer's conceptual description of the model and its solution. Validation: determining the degree to which a model is an accurate representation of the real world from the perspective of its intended uses.

### E2

- Location: §1.1 Background
- Quote: "Most researchers in the field of structural dynamics have referred to this interaction as "model validation." As discussed in Section 2.1, we believe a more precise term for this interaction is either "model updating" or "model calibration." That is, the primary interaction between computation and experiment is to update or "tune" the unknown parameters in the computational model using the experimental results from modal testing."
- Key point: Structural dynamics researchers often call "using modal test results to adjust a model's unknown parameters" model validation; the authors argue it is more accurately called model updating or model calibration.

### E3

- Location: §1.2 Basic Terminology and Methodology
- Quote: "Because of the infeasibility and impracticality of conducting true validation experiments on most complex or large scale systems, the recommended method is to use a building-block approach. This approach divides the complex engineering system of interest into at least three progressively simpler tiers: subsystem cases, benchmark cases, and unit problems."
- Key point: True validation experiments are infeasible for most complex or large-scale systems, so the recommended method is a "building-block" approach: divide the system into at least three tiers of decreasing complexity, namely subsystems, benchmark cases, and unit problems.

### E4

- Location: §2.4.1 Fundamentals of Validation
- Quote: "We have emphasized that validation experiments must be designed purposefully with specific goals linked to application objectives"
- Key point: Validation experiments must be designed purposefully, with goals linked to the model's application objectives.

### E5

- Location: §3.3 Validation and predictive activities
- Quote: "Validation puts a premium on obtaining a measure to compare computational and experimental results and relating the magnitude of this measure to the intended application. Calibration emphasizes methods to improve the agreement between the model and the experiment by optimization of model parameters."
- Key point: Validation puts a premium on a measure comparing computational and experimental results and on judging the size of the discrepancy relative to the intended use; calibration aims to improve agreement between model and experiment by optimizing model parameters.

### E6

- Location: §1.2 Basic Terminology and Methodology
- Quote: "For simple physics, the inference may be very strong, e.g., laminar, single phase, Newtonian, nonreacting flow, and rigid-body structural dynamics. However, for complex physics, the inference is commonly very weak, e.g., turbulent reacting flow and fracture dynamics."
- Key point: Inferring a model's credibility at other tiers from comparisons at one tier: for simple physics the inference can be very strong; for complex physics (e.g., turbulent reacting flow, fracture dynamics) it is usually weak.
