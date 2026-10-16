# Cunningham: Causal Inference: The Remix (online second edition)

- Source: `cunningham2026remix`, [Author's free online version](https://mixtape.scunning.com/); the first edition is Causal Inference: The Mixtape (Yale University Press, 2021), online at https://mixtape-1ed.netlify.app/
- Version: Online version read on October 6, 2026. The site says the online second edition is a "work-in-progress," so content may change. Excerpts are from Chapter 6 (regression discontinuity), Chapter 7 (instrumental variables), Chapter 9 (difference-in-differences basics), Chapter 10 (complex difference-in-differences designs), and Chapter 11 (synthetic control); locations give section titles.

### E1

- Location: Chapter 7 Instrumental Variables (after The Problem of Weak Instruments, section on diagnosing weak instruments)
- Quote: "The number 10 is now widely seen as too low—especially in models with multiple endogenous regressors, heteroskedasticity, or non-normal errors."
- Key point: The rule of thumb that the first-stage F-statistic should exceed 10 is now widely seen as too low.

### E2

- Location: Chapter 7, same as above
- Quote: "So in summary—regarding weak instruments, your studies should report the Anderson-Rubin confidence intervals for robustness and use Olea and Pflueger (2013) effective \(F\)-statistic to assess instrument strength."
- Key point: The author's summary advice: report Anderson-Rubin confidence intervals (which remain valid however weak the instrument) and use the Olea and Pflueger effective F-statistic to assess instrument strength.

### E3

- Location: Chapter 7 (quoting Bound, Jaeger, and Baker 1995, p. 448)
- Quote: "It is striking that the second-stage results reported in Table 3 look quite reasonable even with no information about educational attainment in the simulated instruments. They give no indication that the instruments were randomly generated."
- Key point: When Bound et al. replaced the real instruments with randomly generated numbers, the second-stage results still looked "quite reasonable," giving no sign that the instruments were made up.

### E4

- Location: Chapter 7 (section on the assumptions of LATE)
- Quote: "Note: unlike independence and exclusion, the first stage is testable as it is based solely on \(D\) and \(Z\), both of which you have data on."
- Key point: Unlike independence and exclusion, the first stage (whether the instrument actually shifts the treatment) can be tested with data.

### E5

- Location: Chapter 7 (section on the assumptions of LATE)
- Quote: "As outlined above, with all five assumptions satisfied, IV estimates the average treatment effect for compliers, which is the parameter we've called the local average treatment effect."
- Key point: When all the assumptions hold, IV estimates the average treatment effect for compliers (the people whose treatment the instrument changes): the local average treatment effect.

### E6

- Location: Chapter 7 (section on explaining instrumental variables to readers)
- Quote: "The problem with IV is that it has several untestable assumptions." / "Defeating the LATE merely requires creating doubt in someone's mind that exclusion holds."
- Key point: Instrumental variables rest on several untestable assumptions; just raising doubt about the exclusion restriction is enough to defeat the conclusion.

### E7

- Location: Chapter 7 (Know Your Treatment Assignment Mechanism)
- Quote: "Ask yourself why you think it's random? Why do you think it satisfies exclusion? Be your own worst critic."
- Key point: Ask yourself why you think the instrument is random and why you think it satisfies exclusion. Be your own worst critic.

### E8

- Location: Chapter 7 (Make Beautiful Figures of Your Instrument)
- Quote: "What you want to therefore do is present to people the numerator and the denominator of that Wald estimator."
- Key point: Show readers the numerator and the denominator of the IV estimate, that is, the reduced form (the instrument's effect on the outcome) and the first stage (the instrument's effect on the treatment), not just the final coefficient.

### E9

- Location: Chapter 9 Difference-in-Differences Fundamentals (Event Studies)
- Quote: "The parallel trends assumption cannot be tested because it involves a non-existent counterfactual that cannot be observed." / "What's needed is that the post-treatment counterfactual trend in \(E[Y^0]\) for the treatment group be the same as the control group. That is not the same thing as requiring pretrends to be parallel."
- Key point: Parallel trends involves an unobservable counterfactual and cannot be tested; what is needed is equal counterfactual trends after treatment, which is not the same thing as parallel pre-treatment trends.

### E10

- Location: Chapter 9 (The Importance of Falsifications in Diff-in-Diff)
- Quote: "In diff-in-diff, falsifications are tests of alternative explanations for your results." / "There are roughly two kinds of falsification designs that people employ, which I call "same outcome, alternative groups" and "same group, alternative outcomes.""
- Key point: Falsification tests are tests of alternative explanations. The two common kinds are "same outcome, alternative groups" and "same group, alternative outcome."

### E11

- Location: Chapter 10 Complex Diff-in-Diff Designs (Designing Your Diff-in-Diff by Checklist)
- Quote: "Count the Units in Your Cohorts: Count the number of units that are treated in each cohort, including the cohort of never-treated and the cohort of always-treated." / "Plot Treatment Rollout: Visualize when and how treatment varies across units and time." / "Pick Your Control Group: Decide which units will serve as your counterfactual and justify that choice."
- Key point: Some steps in the author's difference-in-differences design checklist: count the units in each cohort (units first treated at the same time), including the never-treated and always-treated; plot the treatment rollout over time; choose the comparison group and justify it.

### E12

- Location: Chapter 10 (Designing Your Diff-in-Diff by Checklist)
- Quote: "DDDiD, or "Don't Do Diff-in-Diff": Always fold a losing hand as soon as possible and move on to a different approach if you can—even if that means walking away from diff-in-diff."
- Key point: The last step on the checklist is "Don't Do Diff-in-Diff": fold a losing hand as early as possible and switch to another approach.

### E13

- Location: Chapter 10 (section comparing estimators)
- Quote: "As a general principle, if a researcher cannot select between two methods ex ante, they must use both to avoid \(p\)-hacking."
- Key point: If you cannot choose between two methods in advance, report both, to avoid p-hacking.

### E14

- Location: Chapter 10 (section on choosing covariates)
- Quote: "The key is being transparent about your choices and to make these choices well in advance of ever peeking at the results."
- Key point: The key is to be transparent about your choices and to make them well before you ever look at the results.

### E15

- Location: Chapter 11 Synthetic Control (Cuba, Miami, and the Mariel Boatlift)
- Quote: "But the problems with the study were that the selection of the control group was, in retrospect, ad hoc and therefore potentially subjective." / "The method is based on the observation that, when the units of analysis are a few aggregate units, a combination of comparison units (the "synthetic control") often does a better job of reproducing characteristics of a treated unit than using a single comparison unit alone."
- Key point: The problem with traditional comparative case studies is that the control group is chosen ad hoc and possibly subjectively. Synthetic control starts from the observation that when the units of analysis are a few aggregate units (such as cities or states), a weighted combination of several control units often resembles the treated unit better than any single one.

### E16

- Location: Chapter 11 (Synthetic Control from Alberto Abadie section)
- Quote: "Unlike regression-based methods, synthetic control does not require access to post-treatment outcomes when constructing the counterfactual."
- Key point: Building a synthetic control does not require post-treatment outcome data, which helps you avoid tuning the model while looking at the results.

### E17

- Location: Chapter 11 (inference section)
- Quote: "Recall that randomization inference involves reassigning the treatment to each untreated unit as if it had been treated, reestimating the model each time, and then collecting the resulting estimates into a distribution that forms the basis for inference."
- Key point: Synthetic control often uses randomization inference: reassign the treatment to each untreated unit in turn, re-estimate, and collect the resulting "placebo effects" to see whether the real effect stands out.

### E18

- Location: Chapter 11 (inference section)
- Quote: "Abadie, Diamond, and Hainmueller (2010) recommend dropping the states whose pretreatment RMSPE is considerably different than California's"
- Key point: Abadie et al. recommend dropping placebo units with poor pre-treatment fit (pre-treatment error much larger than the treated unit's) from the comparison.
