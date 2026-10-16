# de França & Travassos 2015: Simulation Based Studies in Software Engineering: A Matter of Validity

- Source: `defranca2015simulation`, [Original (CLEI Electronic Journal, open access, CC BY)](https://www.clei.org/cleiej/index.php/cleiej/article/view/54)
- Version: CLEI Electronic Journal 18(1), paper 4, 2015. DOI 10.19153/cleiej.18.1.4.

### E1

- Location: §2 Background
- Quote: "The overall quality assessment indicated a poor quality of reports regarding SBS due the lack of relevant information such as research goals, study procedures and strategy, and the experimental design."
- Key point: The authors' earlier literature review found that reports of simulation studies in software engineering are generally of poor quality, often missing key information such as research goals, study procedures, and experimental design.

### E2

- Location: §4.1 Conclusion Validity
- Quote: "Considering only one observation when dealing with stochastic simulation, rather than central tendency and dispersion measures" / "Consequently, a single outcome could reflect the stochastic process, rather than the theoretical processes under study."
- Key point: Threat to conclusion validity: for a stochastic simulation, looking at a single run instead of central tendency and dispersion. A single outcome may reflect the stochastic process rather than the mechanism under study.

### E3

- Location: §4.1 Conclusion Validity
- Quote: "It should be avoided comparing single values from simulated to empirical outcomes. It is recommended to use proper statistical tests or measures to compare distributions with a certain level of confidence."
- Key point: Avoid comparing single simulated values with single empirical values; use proper statistical tests or measures to compare distributions at a stated confidence level.

### E4

- Location: §4.2 Internal Validity
- Quote: "Simulation model simplifications (assumptions) forcing the desired outcomes" / "this is the most recurrent threat reported in the analyzed papers." / "In such case, there is no room for simulation, since the outcomes are predictable without run the simulations."
- Key point: The threat most often reported in the papers analyzed: the model's simplifying assumptions force the desired outcome. In that case there is no need for simulation, since the outcome can be predicted without running it.

### E5

- Location: §4.2 Internal Validity
- Quote: "This is the case when calibrating the simulation model with a specific dataset, reflecting the context of a particular project, product, or organization and using the same calibration to run experiments for another (different) context."
- Key point: Threat to internal validity: calibrating the model with data from one project, product, or organization and then using the same calibration for experiments in a different context.

### E6

- Location: §4.3 Construct Validity
- Quote: "Hidden underlying model assumptions" / "if assumptions are not explicit in model description, results may be misinterpreted or bias the conclusions, and may not be possible to judge at what extent they correspond to the actual phenomena."
- Key point: Threat to construct validity: hidden model assumptions. If assumptions are not stated, results may be misread, conclusions biased, and readers cannot judge how far the model matches the real phenomenon.

### E7

- Location: §4.3 Construct Validity
- Quote: "If there is no evidence of theoretical mechanism’s face validity, it is possible that the simulation model has been producing right outcomes, through wrong explanations."
- Key point: Without evidence that the model's mechanism has face validity, the model may be producing right outcomes through wrong explanations.

### E8

- Location: §4.3 Construct Validity
- Quote: "This threat regards to simulation studies where a simulation model is chosen without proper information about its validity. Therefore, no conclusion can be draw about the phenomenon, but only about the model itself."
- Key point: When there is no evidence of the model's validity, conclusions can be drawn only about the model itself, not about the real phenomenon.

### E9

- Location: §4.4 External Validity
- Quote: "Simulation results are context-dependent, since there is a need for calibration" / "Results are as general as the supporting data."
- Key point: Threat to external validity: simulations need calibration, so results are context-dependent; they are only as general as the supporting data.

### E10

- Location: §4.2 Internal Validity
- Quote: "However, it is important to be caution when dropping out factors to simplify the experimental design, as in fractional factorial designs."
- Key point: Be cautious when dropping factors to simplify the experimental design (as in fractional factorial designs).

### E11

- Location: §5 Verification and Validation of Simulation Models
- Quote: "Since the SBS validity is highly affected by the simulation model validity, using a model that cannot be considered valid will bring invalid results, regardless the mitigation actions applied to deal with other possible validity threats. In other words, the simulation model itself represents the main threat to the study validity."
- Key point: The validity of a simulation study depends heavily on the validity of the model; with an invalid model, no other mitigation helps. The model itself is the main threat to validity.

### E12

- Location: §6 Recommendations, Recommendation 1
- Quote: "Make use of Face Validity procedures, involving domain experts, to assess the plausibility of both conceptual, executable models and simulation outcomes, using proper diagrams and statistical charts as instruments respectively."
- Key point: Recommendation 1: use face validity checks with domain experts to assess the plausibility of the conceptual model, the executable model, and the simulation outcomes.

### E13

- Location: §6 Recommendations, Recommendation 3
- Quote: "Use results from Sensitivity Analysis to select valid parameters’ settings when running simulation experiments, rather than model “fishing”."
- Key point: Recommendation 3: use sensitivity analysis results to choose valid parameter settings, rather than trying parameters until you get the outcome you want (model "fishing").

### E14

- Location: §6 Recommendations, Recommendation 4
- Quote: "Always verify model assumptions, so the results of simulated experiments can get more reliable."
- Key point: Recommendation 4: always verify the model's assumptions.

### E15

- Location: §6 Recommendations, Recommendation 7
- Quote: "When designing the simulation experiment, consider as factors (and levels) not only the simulation model’s input parameters, but also internal parameters, different sample datasets and versions of the simulation model, implementing alternative strategies to be evaluated."
- Key point: Recommendation 7: when designing a simulation experiment, factors can include not only input parameters but also internal parameters, different sample datasets, and model versions implementing different strategies.

### E16

- Location: §6 Recommendations
- Quote: "Comparison-based procedures cannot capture this type of threat. Just white box procedures like Face Validity involving simulation experts may help to identify such threat."
- Key point: Comparing outputs cannot detect the threat of assumptions forcing the outcome (the output may match empirical data); only white-box procedures in which experts inspect the model, such as face validity checks, can.

### E17

- Location: §6 Recommendations
- Quote: "Thus, what is important is that both the goals for the simulation study and the expected benefits should drive the balance between the efforts for mitigating threats to validity and the risk of not doing so."
- Key point: All these recommendations have costs; let the study's goals and expected benefits drive the balance between effort spent mitigating threats to validity and the risk of not doing so.

### E18

- Location: §7 Final Remarks
- Quote: "Taking simulation as a complementary research strategy for the evolution of Software Engineering knowledge, mainly in contexts where in vivo or in vitro experiments are unfeasible or risky, researchers should be aware about possible threats involved in this sort of study."
- Key point: Simulation is a complementary research strategy, used mainly where in vivo or in vitro experiments are unfeasible or risky.
