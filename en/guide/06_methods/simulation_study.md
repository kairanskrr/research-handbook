# Quantitative simulation: using a computational model to simulate a system or process

This page covers **quantitative simulation studies**: you build a computational model that imitates the behavior of a real system, run experiments on the model, and use them to answer questions about the system. Examples: using simulation to compare cluster throughput under different scheduling policies, or simulating how a software project's schedule unfolds under different levels of testing effort.

If you are measuring a real, running system, that is [Benchmarking](../07_fields/computer-science/practices/benchmarking.md); if you are using simulation to evaluate a new method or tool you have proposed, you also need to meet the requirements of [Engineering research](../07_fields/computer-science/practices/engineering_research.md). For the basic concepts of validity, see [Validity and limitations: think them through at the design stage](../02_do-the-project/04_validity-and-limits.md).

**Scope** `[Our analysis]`: the checklist on this page is based on the empirical standards written for software engineering by ACM SIGSOFT (the Association for Computing Machinery Special Interest Group on Software Engineering); the list of threats to validity comes from a review of simulation studies in software engineering; and the examples are mostly computer systems and software projects. The practices for verification and validation and for output data analysis come from general simulation methodology tutorials (Sargent 2010, Alexopoulos & Kim 2002) and are not specific to computing. If you use models and simulation in another field, check your field's own conventions first; for numerical simulation in civil engineering, for example, see [Civil engineering: numerical simulation](../07_fields/civil-engineering/README.md#numerical-simulation-first-tell-verification-validation-and-calibration-apart).

**Strategies it usually serves**: [Building and improving](../05_research-strategies/build_improve.md) (evaluating a new design on a model when experimenting directly on the real system is impractical).

**After reading this page, you should be able to:**

- judge whether your question is one simulation can answer;
- tell "verification" from "validation" and know which methods serve each;
- calibrate a model with real data and state the model's assumptions clearly;
- design simulation experiments: choose factors, run replications, handle the warm-up period, and do sensitivity analysis;
- check your own study against the checklist at the end of this page.

---

## 1. What this kind of study is, and when to use it

The ACM SIGSOFT Empirical Standards define it this way: a simulation study builds and uses a mathematical model that imitates the behavior of a real system, and usually involves understanding the problem, collecting data, building the model, verification, validation, experimental design, data analysis, and implementing the results[^ralph2020empirical-e397].

This page covers only simulations in which **everything is represented by a computational model**. Studies in which people operate a simulation model (for example, students making decisions in a project management simulator) count as experiments with human participants[^ralph2020empirical-e398]. Common simulation approaches include discrete-event simulation (the system's state changes only when an "event" happens, such as a task arriving or finishing), system dynamics (describing a system with stocks, flows and feedback loops), and agent-based simulation (simulating many individuals that each act according to their own rules)[^ralph2020empirical-e400]. The standard was written for software engineering, but the same reasoning applies when areas such as systems and networking use simulation to study scheduling, protocols or architectures `[Our analysis]`.

**When to use it**:

- When experimenting in the real environment is infeasible or too risky[^defranca2015simulation-e18], for example because the system has not been built yet, is too large, or trial and error would be too costly `[Our analysis]`.
- Your paper needs to explain why simulation suits your question; this is the first essential requirement in the standard[^ralph2020empirical-e399].

**Keep in mind**: how far you can trust a simulation's conclusions depends on the model. If the real system cannot be observed, so you have no data on how it actually runs, you usually cannot have high confidence in the model; in that case, explore the model's behavior as thoroughly as you can and compare it with other valid models where possible[^sargent2010verification-e15].

---

## 2. How to do it

### Step 1: Fix the purpose and the accuracy you need

**How:** Write down the questions the model must answer, which output variables you care about, and how accurate those outputs need to be. Ideally, set the accuracy requirements before you start building the model[^sargent2010verification-e3].

**Why:** A model is built for a specific purpose, and it is valid or not only with respect to that purpose; a model that is valid under one set of experimental conditions may be invalid under another[^sargent2010verification-e2]. Without a purpose and accuracy requirements, there is no way to judge whether the model is "right" `[Our analysis]`.

### Step 2: Build the model and write down its assumptions

**How:**

1. **Describe the model**: the conceptual level (which variables and relationships make up the model) and the implementation level (the code), including input parameters and response variables (the outputs you want to observe)[^ralph2020empirical-e400]. It is best to describe the two levels separately[^ralph2020empirical-e407].
2. **List every assumption.** For example, "task arrivals follow a Poisson distribution" or "node failures are independent of each other". Stating the model's assumptions explicitly is an essential requirement[^ralph2020empirical-e404].

**Why:** Every model has assumptions. As long as they are stated, justified, and their impact on validity is discussed, "the model makes assumptions" is not a valid criticism[^ralph2020empirical-e412]. Conversely, if assumptions are not stated, the results may be misread, and readers cannot judge how closely the model corresponds to the real phenomenon[^defranca2015simulation-e6].

**Where people go wrong:** **Building the conclusion you want into the assumptions.** When de França and Travassos analyzed simulation papers in software engineering, this was the most frequent of the threats to validity those papers reported: the model's simplifying assumptions directly determine the output, so you could predict the result without running the simulation, and the simulation becomes pointless[^defranca2015simulation-e4]. For example, you want to study "does the new scheduling policy reduce latency?", but the model simply assumes "under the new policy, every task's waiting time drops by 20%" `[Our analysis]`. Comparing outputs with measured data will not catch this kind of problem; only methods that look inside the model, such as having simulation experts check it (face validity checks, see Step 3), can catch it[^defranca2015simulation-e16].

> **Where sources disagree: when data is missing, how far can you lean on assumptions?**
> - The SIGSOFT standard holds that when calibration data is insufficient or too expensive, parts of the model can be replaced by assumptions, but you must say so and justify it[^ralph2020empirical-e411].
> - de França and Travassos recommend something stricter: always test the model's assumptions[^defranca2015simulation-e14]. Sargent also recommends testing the assumptions and theories a model rests on wherever possible[^sargent2010verification-e19].
>
> In practice `[Our analysis]`: write down the source of every assumption; test the ones you can test with data; for the ones you can't, use sensitivity analysis (see Step 7) to see whether the conclusion changes when the assumption changes.

### Step 3: Verification and validation

These two terms are easy to mix up. In plain words[^sargent2010verification-e1]:

- **Verification**: **Did you build the program right?** Does the code correctly implement the model you designed?
- **Validation**: **Is the model accurate enough for your purpose?** Within its domain of applicability, is the model accurate enough for its intended use?

Sargent breaks this into four checks[^sargent2010verification-e5][^sargent2010verification-e6]:

| Check | What it asks |
|---|---|
| Conceptual model validation | Are the theories and assumptions behind the model correct? Is its representation of the real system reasonable? |
| Computerized model verification | Does the code correctly implement the conceptual model? |
| Operational validation | Are the model's outputs accurate enough within its domain of applicability? |
| Data validity | Are the data used to build, test and experiment with the model adequate and correct? |

**Common methods** (they can be combined):

- **Test the code**: run the program under different conditions and use the outputs and intermediate values to judge whether the implementation is correct[^sargent2010verification-e14].
- **Degenerate tests and extreme-condition tests**: choose special parameter values and check whether the behavior is reasonable. For example, when the arrival rate exceeds the service rate, a single server's queue should keep growing[^sargent2010verification-e8].
- **Compare with analytical models**: check simple cases of the model against known theoretical results[^sargent2010verification-e9]. For example, a single-server queue can be checked against queueing theory formulas `[Our analysis]`.
- **Ask experts** (face validity): have people who know the system judge whether the model and its behavior are reasonable[^sargent2010verification-e10]. de França and Travassos recommend having domain experts check the conceptual model, the executable model and the simulation results[^defranca2015simulation-e12].
- **Compare with real data**: see Step 4.

**How far to go**: Proving that a model is absolutely valid over its entire domain of applicability is usually too costly; in practice you keep testing and evaluating until you have enough confidence that it is fit for its intended use[^sargent2010verification-e4]. How much effort to put into addressing threats to validity should be weighed against the study's goals and expected benefits[^defranca2015simulation-e17].

**Why:** The model itself is the main threat to the validity of a simulation study; if the model is invalid, nothing else can save the study[^defranca2015simulation-e11]. Without evidence that the model is valid, your conclusions can only be about the model itself and cannot be carried over to the real system[^defranca2015simulation-e8].

**Where people go wrong:**

- **Being reassured just because the outputs match.** A model can "produce the right results for the wrong reasons"[^defranca2015simulation-e7].
- **Changing the model without checking again.** After any change to the model, you need to verify and validate it again[^sargent2010verification-e7].

### Step 4: Calibrate with real data, and hold some data back for testing

**Calibration** means using real data to set the values of the model's parameters, for example using cluster logs to estimate the distributions of task arrival rates and run times `[Our analysis]`.

**How:**

1. **State which data you used for calibration, how you calibrated, and what context the data comes from**[^ralph2020empirical-e401].
2. **Hold back part of the data for testing.** Build the model with part of the historical data, and use the rest to test whether the model behaves like the system[^sargent2010verification-e10].
3. **Compare distributions, not single numbers.** Don't compare a single simulated value with a single measured value; compare the distributions using statistical methods[^defranca2015simulation-e3]. Confidence intervals or hypothesis tests are preferable because they allow an objective decision, though in practice graphical comparison is still the most common[^sargent2010verification-e16]. If you use hypothesis tests, be especially careful: the risk of accepting an invalid model as valid must be kept small[^sargent2010verification-e17].

**Where people go wrong:**

- **Calibrating and experimenting with data from different contexts**, for example calibrating with one organization's data and then simulating a different organization[^defranca2015simulation-e5]. Your results cannot be generalized beyond the scope of the data that supports them[^defranca2015simulation-e9].
- **Overfitting the model to reproduce the reference data**, for example building a model that can only produce the expected results; the standard lists this as an antipattern[^ralph2020empirical-e409].
- **Underestimating how hard the data is.** Model validation often fails because of problems with the data[^sargent2010verification-e13].

### Step 5: Design the experiments

**How:**

1. **Write out the study protocol**: the independent variables, the scenarios, how many runs per scenario, and whether runs end on steady-state or terminating conditions[^ralph2020empirical-e403].
2. **Use a standard experimental design**, such as a factorial design (running every combination of every factor's levels) or a fractional factorial design (running only a representative subset of the combinations); if you use a nonstandard design, justify it[^ralph2020empirical-e410]. Be careful when you simplify the design by dropping factors[^defranca2015simulation-e10].
3. **Factors are not just input parameters.** They can also include the model's internal parameters, different sample datasets, and versions of the model that implement different policies[^defranca2015simulation-e15].

### Step 6: Run replications and handle the warm-up period

**How:**

1. **Run a stochastic model many times, independently.** Running a stochastic model only once is an antipattern listed in the standard[^ralph2020empirical-e409]: a single result may reflect nothing but random variation, rather than the mechanism you want to study[^defranca2015simulation-e2].
2. **Do your statistics on per-run averages.** Observations within one run are usually correlated rather than independent and identically distributed, so classical statistical methods cannot be applied to them directly[^alexopoulos2002output-e1]. The usual approach is to make several independent runs (replications) and treat each run's sample mean as an independent observation[^alexopoulos2002output-e3][^alexopoulos2002output-e7]. Replications also tell you how much random variation there is inside the model[^sargent2010verification-e12].
3. **First decide whether it is a terminating or a steady-state simulation.** A terminating simulation starts from a specific state and ends at some event (for example, simulating one week of operation `[Our analysis]`); a steady-state simulation studies the system's long-run behavior[^alexopoulos2002output-e2].
4. **In a steady-state simulation, remove the warm-up period.** The system starts from an "empty" state, so the data at the start carries initialization bias[^alexopoulos2002output-e4]. The most common remedy is to discard the opening stretch of each run (the warm-up period), because the initial state mainly affects data at the start of a run[^alexopoulos2002output-e5][^alexopoulos2002output-e7]. To decide how much to discard, you can use Welch's graphical method: average the outputs of several runs, plot a moving-average curve, and take the point where the curve starts to settle[^alexopoulos2002output-e6].

**Where people go wrong:** Thinking that more runs will remove the warm-up bias. The systematic error caused by the initial state cannot be reduced by adding replications[^alexopoulos2002output-e8].

### Step 7: Do a sensitivity analysis

**Sensitivity analysis**: change the model's input and internal parameters and see how the output changes[^sargent2010verification-e11].

**How and why:**

- **To test the model**: the relationships in the model should match those in the real system[^sargent2010verification-e11]. For example, if throughput drops when you add machines, either you have found a real phenomenon or the model has a bug `[Our analysis]`.
- **To find the key parameters**: parameters with a large effect on the output need to be made accurate enough before the model is used[^sargent2010verification-e11].
- **To avoid "fishing" for results**: use the results of the sensitivity analysis to choose reasonable parameter settings, rather than trying parameters over and over until the result you want appears[^defranca2015simulation-e13].
- **Report it**: the standard lists reporting a sensitivity analysis as a desirable attribute[^ralph2020empirical-e407].

### Step 8: Report the model and the code

The review by de França and Travassos found that simulation studies in software engineering are generally poorly reported, often missing key information such as the study's goals, process and experimental design[^defranca2015simulation-e1]. At a minimum, your report should:

- State the simulation approach, the tools or software packages used and their versions, and the computing environment[^ralph2020empirical-e400].
- Analyze threats to validity in terms of both the data and the model, for example scenarios that are not representative, or insufficient verification and validation[^ralph2020empirical-e404].
- Describe the verification and validation process and its results. These records are usually critical for convincing readers to trust the model and its results[^sargent2010verification-e18].
- Make public the raw data used for calibration (or how synthetic data was generated), all models and source code, and the analysis scripts[^ralph2020empirical-e405].

---

## 3. Checklist

This is based mainly on the SIGSOFT standard for quantitative simulation, which was written for software engineering.

**Essential**

- [ ] Explain why simulation is suitable for studying this question[^ralph2020empirical-e399]
- [ ] Describe the simulation model (including input parameters and response variables), the simulation approach, tool versions and the computing environment[^ralph2020empirical-e400]
- [ ] Describe the calibration data, the calibration process and the context of the data[^ralph2020empirical-e401]
- [ ] Explain how the model was verified and validated at different levels of abstraction[^ralph2020empirical-e402]
- [ ] Describe the study protocol: independent variables, scenarios, number of runs per scenario, steady-state or terminating conditions[^ralph2020empirical-e403]
- [ ] Analyze threats to validity in terms of both the data and the model; state the model's assumptions explicitly[^ralph2020empirical-e404]

**Desirable**

- [ ] Make the data (or the mechanism that generates it), the model, the source code and the analysis scripts public[^ralph2020empirical-e405]
- [ ] Characterize the reference behavior (measured data from the real system) with known values or distributions, and define scenarios from it[^ralph2020empirical-e406]
- [ ] Describe the conceptual and implementation levels separately; report a sensitivity analysis; distinguish results backed by evidence from speculation[^ralph2020empirical-e407]

**Extraordinary**

- [ ] Explain how data providers, domain experts, model users and others took part in building and validating the model, for example by checking whether the outputs are plausible[^ralph2020empirical-e408]

**Acceptable deviations (not flaws)**

- Replacing parts of the model with assumptions when calibration data is insufficient or too expensive, provided you say so and justify it[^ralph2020empirical-e411]

**Criticisms common in review that are not valid**: you don't need to worry about these

- "The model makes assumptions", as long as the assumptions are stated, justified, and their impact discussed[^ralph2020empirical-e412]
- "The model is too abstract", without explaining why that level of abstraction is inadequate[^ralph2020empirical-e413]
- Rejecting a study for using generated data, secondary data or expert estimates when no suitable primary data is available[^ralph2020empirical-e413]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Drawing conclusions from a model that has not been validated | The conclusions can only be about the model itself, not the real system[^defranca2015simulation-e8] |
| Building the expected result into the assumptions | You could "predict" the result without running the simulation, so the simulation becomes pointless[^defranca2015simulation-e4] |
| Not writing the assumptions down | The results may be misread, and readers cannot judge whether the model is close to reality[^defranca2015simulation-e6] |
| Running a stochastic model only once | The result may be just random variation[^ralph2020empirical-e409][^defranca2015simulation-e2] |
| Not removing the warm-up period in a steady-state simulation | The results carry initialization bias, which more runs cannot remove[^alexopoulos2002output-e8] |
| Calibrating with data from context A to simulate context B | Results cannot be generalized beyond the scope of the data that supports them[^defranca2015simulation-e5][^defranca2015simulation-e9] |
| Tweaking parameters again and again until the desired result appears | The conclusions can't be trusted; choose parameters through sensitivity analysis[^defranca2015simulation-e13] |
| Comparing a single simulated value with a single measured value | Compare distributions using statistical methods[^defranca2015simulation-e3] |

---

## 5. Further reading

- **ACM SIGSOFT Empirical Standards, Simulation (Quantitative)**: the checklist for quantitative simulation, including acceptable deviations and invalid criticisms. The original is in the submodule `repos/acmsigsoft__EmpiricalStandards/docs/standards/QuantitativeSimulation.md`.
- **Sargent 2010, Verification and Validation of Simulation Models**: a classic tutorial on verifying and validating simulation models, listing the various validation techniques and a recommended minimum set of steps. Proceedings of the Winter Simulation Conference; open access.
- **de França & Travassos 2015, Simulation Based Studies in Software Engineering: A Matter of Validity**: catalogs 28 threats to validity in software engineering simulation studies, with 7 recommendations. Open access.
- **Alexopoulos & Kim 2002, Output Data Analysis for Simulations**: statistical analysis of simulation output: independent replications, the warm-up period, steady-state estimation. Fairly mathematical; best consulted when you need to go deeper. Open access.

[^ralph2020empirical-e397]: SIGSOFT Quantitative Simulation standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e397)
[^ralph2020empirical-e398]: SIGSOFT Quantitative Simulation standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e398)
[^ralph2020empirical-e399]: SIGSOFT Quantitative Simulation standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e399)
[^ralph2020empirical-e400]: SIGSOFT Quantitative Simulation standard, Essential Attributes and footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e400)
[^ralph2020empirical-e401]: SIGSOFT Quantitative Simulation standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e401)
[^ralph2020empirical-e402]: SIGSOFT Quantitative Simulation standard, Essential Attributes and footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e402)
[^ralph2020empirical-e403]: SIGSOFT Quantitative Simulation standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e403)
[^ralph2020empirical-e404]: SIGSOFT Quantitative Simulation standard, Essential Attributes and footnote 3. [Evidence](../../sources/notes/ralph2020empirical.md#e404)
[^ralph2020empirical-e405]: SIGSOFT Quantitative Simulation standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e405)
[^ralph2020empirical-e406]: SIGSOFT Quantitative Simulation standard, Desirable Attributes and footnote 4. [Evidence](../../sources/notes/ralph2020empirical.md#e406)
[^ralph2020empirical-e407]: SIGSOFT Quantitative Simulation standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e407)
[^ralph2020empirical-e408]: SIGSOFT Quantitative Simulation standard, Extraordinary Attributes and footnote 6. [Evidence](../../sources/notes/ralph2020empirical.md#e408)
[^ralph2020empirical-e409]: SIGSOFT Quantitative Simulation standard, Antipatterns and footnote 8. [Evidence](../../sources/notes/ralph2020empirical.md#e409)
[^ralph2020empirical-e410]: SIGSOFT Quantitative Simulation standard, Antipatterns and footnote 9. [Evidence](../../sources/notes/ralph2020empirical.md#e410)
[^ralph2020empirical-e411]: SIGSOFT Quantitative Simulation standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e411)
[^ralph2020empirical-e412]: SIGSOFT Quantitative Simulation standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e412)
[^ralph2020empirical-e413]: SIGSOFT Quantitative Simulation standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e413)
[^sargent2010verification-e1]: Sargent 2010, §1. [Evidence](../../sources/notes/sargent2010verification.md#e1)
[^sargent2010verification-e2]: Sargent 2010, §1. [Evidence](../../sources/notes/sargent2010verification.md#e2)
[^sargent2010verification-e3]: Sargent 2010, §1. [Evidence](../../sources/notes/sargent2010verification.md#e3)
[^sargent2010verification-e4]: Sargent 2010, §1. [Evidence](../../sources/notes/sargent2010verification.md#e4)
[^sargent2010verification-e5]: Sargent 2010, §3. [Evidence](../../sources/notes/sargent2010verification.md#e5)
[^sargent2010verification-e6]: Sargent 2010, §3. [Evidence](../../sources/notes/sargent2010verification.md#e6)
[^sargent2010verification-e7]: Sargent 2010, §3. [Evidence](../../sources/notes/sargent2010verification.md#e7)
[^sargent2010verification-e8]: Sargent 2010, §4. [Evidence](../../sources/notes/sargent2010verification.md#e8)
[^sargent2010verification-e9]: Sargent 2010, §4. [Evidence](../../sources/notes/sargent2010verification.md#e9)
[^sargent2010verification-e10]: Sargent 2010, §4. [Evidence](../../sources/notes/sargent2010verification.md#e10)
[^sargent2010verification-e11]: Sargent 2010, §4. [Evidence](../../sources/notes/sargent2010verification.md#e11)
[^sargent2010verification-e12]: Sargent 2010, §4. [Evidence](../../sources/notes/sargent2010verification.md#e12)
[^sargent2010verification-e13]: Sargent 2010, §5. [Evidence](../../sources/notes/sargent2010verification.md#e13)
[^sargent2010verification-e14]: Sargent 2010, §7. [Evidence](../../sources/notes/sargent2010verification.md#e14)
[^sargent2010verification-e15]: Sargent 2010, §8. [Evidence](../../sources/notes/sargent2010verification.md#e15)
[^sargent2010verification-e16]: Sargent 2010, §8.2. [Evidence](../../sources/notes/sargent2010verification.md#e16)
[^sargent2010verification-e17]: Sargent 2010, §8.2.3. [Evidence](../../sources/notes/sargent2010verification.md#e17)
[^sargent2010verification-e18]: Sargent 2010, §9. [Evidence](../../sources/notes/sargent2010verification.md#e18)
[^sargent2010verification-e19]: Sargent 2010, §10. [Evidence](../../sources/notes/sargent2010verification.md#e19)
[^defranca2015simulation-e1]: de França & Travassos 2015, §2. [Evidence](../../sources/notes/defranca2015simulation.md#e1)
[^defranca2015simulation-e2]: de França & Travassos 2015, §4.1. [Evidence](../../sources/notes/defranca2015simulation.md#e2)
[^defranca2015simulation-e3]: de França & Travassos 2015, §4.1. [Evidence](../../sources/notes/defranca2015simulation.md#e3)
[^defranca2015simulation-e4]: de França & Travassos 2015, §4.2. [Evidence](../../sources/notes/defranca2015simulation.md#e4)
[^defranca2015simulation-e5]: de França & Travassos 2015, §4.2. [Evidence](../../sources/notes/defranca2015simulation.md#e5)
[^defranca2015simulation-e6]: de França & Travassos 2015, §4.3. [Evidence](../../sources/notes/defranca2015simulation.md#e6)
[^defranca2015simulation-e7]: de França & Travassos 2015, §4.3. [Evidence](../../sources/notes/defranca2015simulation.md#e7)
[^defranca2015simulation-e8]: de França & Travassos 2015, §4.3. [Evidence](../../sources/notes/defranca2015simulation.md#e8)
[^defranca2015simulation-e9]: de França & Travassos 2015, §4.4. [Evidence](../../sources/notes/defranca2015simulation.md#e9)
[^defranca2015simulation-e10]: de França & Travassos 2015, §4.2. [Evidence](../../sources/notes/defranca2015simulation.md#e10)
[^defranca2015simulation-e11]: de França & Travassos 2015, §5. [Evidence](../../sources/notes/defranca2015simulation.md#e11)
[^defranca2015simulation-e12]: de França & Travassos 2015, §6, recommendation 1. [Evidence](../../sources/notes/defranca2015simulation.md#e12)
[^defranca2015simulation-e13]: de França & Travassos 2015, §6, recommendation 3. [Evidence](../../sources/notes/defranca2015simulation.md#e13)
[^defranca2015simulation-e14]: de França & Travassos 2015, §6, recommendation 4. [Evidence](../../sources/notes/defranca2015simulation.md#e14)
[^defranca2015simulation-e15]: de França & Travassos 2015, §6, recommendation 7. [Evidence](../../sources/notes/defranca2015simulation.md#e15)
[^defranca2015simulation-e16]: de França & Travassos 2015, §6. [Evidence](../../sources/notes/defranca2015simulation.md#e16)
[^defranca2015simulation-e17]: de França & Travassos 2015, §6. [Evidence](../../sources/notes/defranca2015simulation.md#e17)
[^defranca2015simulation-e18]: de França & Travassos 2015, §7. [Evidence](../../sources/notes/defranca2015simulation.md#e18)
[^alexopoulos2002output-e1]: Alexopoulos & Kim 2002, §1. [Evidence](../../sources/notes/alexopoulos2002output.md#e1)
[^alexopoulos2002output-e2]: Alexopoulos & Kim 2002, §1. [Evidence](../../sources/notes/alexopoulos2002output.md#e2)
[^alexopoulos2002output-e3]: Alexopoulos & Kim 2002, §2. [Evidence](../../sources/notes/alexopoulos2002output.md#e3)
[^alexopoulos2002output-e4]: Alexopoulos & Kim 2002, §3. [Evidence](../../sources/notes/alexopoulos2002output.md#e4)
[^alexopoulos2002output-e5]: Alexopoulos & Kim 2002, §3. [Evidence](../../sources/notes/alexopoulos2002output.md#e5)
[^alexopoulos2002output-e6]: Alexopoulos & Kim 2002, §3. [Evidence](../../sources/notes/alexopoulos2002output.md#e6)
[^alexopoulos2002output-e7]: Alexopoulos & Kim 2002, §4.1. [Evidence](../../sources/notes/alexopoulos2002output.md#e7)
[^alexopoulos2002output-e8]: Alexopoulos & Kim 2002, §4.1. [Evidence](../../sources/notes/alexopoulos2002output.md#e8)
