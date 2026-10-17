# Experimental measurement

This page is about **measurement-centered experiments**: the goal is to measure the value of a physical quantity and to say how far that value can be trusted. Examples are measuring a constant, a property of a material, or the lifetime of a particle. Test-rig work in engineering (measuring efficiency, load, flow rate and so on) can follow the same steps; for what engineering journals require about uncertainty, see the [mechanical engineering field overview](../07_fields/mechanical-engineering/README.md#measurement-results-must-come-with-an-uncertainty). The basic ideas of the 5σ discovery standard and of blind analysis are already covered in the [physical sciences field overview](../07_fields/physical-sciences/README.md); this page covers only how to actually do them. Performance measurement in computing also has to deal with noise and measurement bias; you can read this page alongside [benchmarking](../07_fields/computer-science/practices/benchmarking.md#step-4-design-the-measurement-procedure) in the computer science section.

**Scope**: this page was written for the [Physical sciences](../07_fields/physical-sciences/README.md). Its sources are mainly the metrology guide *Guide to the Expression of Uncertainty in Measurement* (GUM), the statistics handbook of the US National Institute of Standards and Technology (NIST), papers from particle physics on blind analysis and reproducibility, and the editorial policy of the American Institute of Aeronautics and Astronautics (AIAA) on numerical and experimental accuracy. The field overviews for [Chemical sciences](../07_fields/chemistry/README.md), [Mechanical engineering](../07_fields/mechanical-engineering/README.md), [Civil engineering](../07_fields/civil-engineering/README.md), [Electrical, electronic, and information engineering](../07_fields/electrical-engineering/README.md), and [Materials engineering and nanotechnology](../07_fields/materials-engineering/README.md) also point here. The blind-analysis practices come mainly from particle physics; if you work in another field, check your own field's norms first.

**Strategies it usually serves**: [Measurement](../05_research-strategies/measure.md).


**After reading this page, you should be able to:**

- define the quantity you want to measure, and design the apparatus and measurement procedure around it;
- calibrate, and find and deal with systematic effects;
- draw up an uncertainty budget and compute the combined and expanded uncertainty;
- use blind analysis and cross-checks to keep yourself from "drifting toward the number you want" without noticing;
- report the result to the conventions of your field and compare it with theory and with other measurements.

---

## 1. What this kind of research is and when to use it

Experimental measurement answers the question: **what is the value of this quantity, and how far can we trust it?** A value without a statement of how reliable it is cannot be compared, either with other measurements or with reference values in a standard[^jcgm2008gum-e28].

| Study | What it answers | Where to look |
|---|---|---|
| Experimental measurement (this page) | The value of a quantity and its uncertainty | This page |
| Search and discovery | Is there a new effect, and how significant is it? | [Physical sciences field overview: 5σ](../07_fields/physical-sciences/README.md#5σ-the-threshold-for-claiming-a-discovery); the measured value or upper limit you finally report still gets its uncertainty handled as on this page |
| Performance benchmarking | Which computer system is faster or better | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) in the computer science section |

## 2. How to do it

### Step 1: Define the measurand

**How:** write down the quantity you want to measure (metrologists call it the **measurand**), together with the measurement method and measurement procedure[^jcgm2008gum-e11]. The definition has to be complete enough that, for practical purposes, the quantity has only one value; the more accurately you want to measure it, the more detailed the definition has to be[^jcgm2008gum-e12]. The GUM (the international *Guide to the Expression of Uncertainty in Measurement*, published by the Joint Committee for Guides in Metrology, JCGM) gives this example: to measure a steel bar about one meter long to micrometer accuracy, you have to state "its length at what temperature and what pressure"[^jcgm2008gum-e12].

**Why:** an incomplete definition itself adds an uncertainty component to the result[^jcgm2008gum-e13]. No amount of care in the measurement removes it.

**Where people go wrong:** writing only "measure the length of the steel bar" without the conditions; or choosing a quantity whose systematic effects are very hard to control. Junk and Lyons, writing about particle physics, note that when systematic uncertainties are hard to control, you can instead measure a quantity that is more unambiguously defined, such as the ratio of two production rates[^junk2021reproducibility-e41].

### Step 2: Design the apparatus and procedure, and estimate the sensitivity first

**How:**

1. List everything that could affect the reading (temperature, air pressure, power supply, alignment, sample condition and so on), and decide which to control and which to monitor and record;
2. Let these influence quantities vary as much as is practical during the experiment, so that your uncertainty evaluation rests as far as possible on observed data[^jcgm2008gum-e14];
3. Before taking data, or at the latest before analyzing it, estimate how precisely you expect to be able to measure. Junk and Lyons say this is routine and necessary in experimental particle physics[^junk2021reproducibility-e44];
4. The first time you do an uncertainty analysis, work out what resources you need and plan data collection and analysis carefully[^nist2012ehandbook-e5].

**Why:** a well-designed experiment makes the uncertainty evaluation far more reliable[^jcgm2008gum-e15]. Estimating sensitivity first has another benefit: a non-significant result from a highly sensitive test is still worth publishing[^junk2021reproducibility-e45].

**Where people go wrong:** with one-off or destructive tests, it is hard to characterize the measurement process afterwards[^nist2012ehandbook-e17], so careful design up front matters even more. Our sources do not cover how to build the apparatus itself (shielding, grounding, vibration isolation, temperature control and so on); follow your advisor's and your group's experience.

### Step 3: Calibrate, and keep checking

**How:**

- **Calibration**: compare your instrument or sample with a reference standard, in order to eliminate or reduce the bias of your measurement system relative to the reference[^nist2012ehandbook-e1]. The uncertainty of the reference standards and reference materials themselves still has to be included[^jcgm2008gum-e19].
- **Set up a check standard**: pick a stable sample and measure it at intervals, to expose errors that creep into the measurement process over time[^nist2012ehandbook-e2]. Its material and geometry should be close to the samples you normally measure[^nist2012ehandbook-e3]. If its readings settle at a new level and stay there over several rounds of measurement, that is a signal to find out why[^nist2012ehandbook-e4].
- **Measure something known first**: use the same apparatus and analysis to measure a well-established signal (particle physicists call it a "standard candle"). Only if its strength and properties come out as expected do you know the whole chain is working[^junk2021reproducibility-e46].

**Where people go wrong:** calibration can be swayed by your own expectations too. Junk and Lyons point out that subconscious bias can enter the analysis at the calibration stage[^junk2021reproducibility-e48]. A small group can fix the calibration method and write it in the lab notebook before looking at the measurement results. "Calibrating" model parameters and "validating" a model are not the same thing; see the [mechanical engineering field overview](../07_fields/mechanical-engineering/README.md#calibration-is-not-validation).

### Step 4: Find and deal with systematic effects

**First, tell the two kinds of error apart.** Statistical errors show up when you repeat: repeat a few times and the result changes. **Systematic effects** push the result away from the true value but do not necessarily change from one repetition to the next[^junk2021reproducibility-e36], so no number of repetitions will reveal them.

**How:**

1. **Find all the systematic effects.** They are not easy to spot, and evaluating them usually takes much more work[^junk2021reproducibility-e34]. The most troublesome ones are those that get overlooked or wrongly ruled out[^junk2021reproducibility-e40].
2. **Correct what you can.** Random error cannot be corrected; bias can, at least in principle[^nist2012ehandbook-e6]. Systematic error cannot be eliminated, but it can often be reduced: apply a correction or correction factor for each systematic effect you have identified[^jcgm2008gum-e18]. The GUM assumes that the result has already been corrected for all recognized significant systematic effects[^jcgm2008gum-e10].
3. **Include the uncertainty of each correction.** After correcting, the uncertainty of the correction itself goes into the total uncertainty[^junk2021reproducibility-e35][^nist2012ehandbook-e7].
4. **Estimate the same effect in several ways.** Particle physicists predict backgrounds from several different control samples (data known to contain no signal), and the spread between the predictions is often counted as a systematic uncertainty[^junk2021reproducibility-e47].

**Where people go wrong:** thinking that a blind analysis means you no longer have to worry about systematic errors. Blind analysis addresses only one problem, experimenter's bias; every other bias still has to be corrected or included in the systematic uncertainty, blind or not[^klein2005blind-e7].

### Step 5: Build an uncertainty budget

An **uncertainty budget** is a table: it lists each uncertainty component with its sensitivity coefficient, standard deviation, and degrees of freedom[^nist2012ehandbook-e14].

**1. Evaluate each component and express it as a "standard uncertainty" (one standard deviation).**

- **Type A evaluation** uses statistical analysis of repeated observations; **Type B evaluation** uses means other than statistical analysis[^jcgm2008gum-e3]. For Type A, watch for drift: if repeated observations are correlated in time, the usual mean and standard deviation of the mean may not be appropriate[^jcgm2008gum-e21]. The NIST handbook lists these sources for Type B: reference standards calibrated by another laboratory, physical constants used in calculations, environmental effects that cannot be sampled, assembly offsets of the instrument, and lack of instrument resolution[^nist2012ehandbook-e10].
- **For Type B, convert first**: an uncertainty quoted elsewhere is usually an expanded uncertainty U, which you divide by k to get a standard uncertainty; if k is not stated, the NIST handbook considers assuming k = 2 probably conservative[^nist2012ehandbook-e11]. If all you know is "no more than ±a", you cannot add a directly to the other components; first convert it to an equivalent standard deviation[^nist2012ehandbook-e12]. If you know nothing about where in the interval the value lies, you can only assume a uniform distribution, with standard deviation a/√3[^jcgm2008gum-e22]; this is the most conservative estimate[^nist2012ehandbook-e13].

**2. Combine.** Type A and Type B components are treated the same way[^nist2012ehandbook-e9]: both go into the law of propagation of uncertainty[^jcgm2008gum-e23]. The basic method is root-sum-of-squares[^nist2012ehandbook-e8]; if input quantities are significantly correlated, the correlations must be taken into account[^jcgm2008gum-e24].

**3. Expand.** Expanded uncertainty U = k × combined standard uncertainty[^jcgm2008gum-e25]. The statistics handbook produced jointly by NIST and SEMATECH (a US semiconductor industry consortium) recommends k = 2 when the degrees of freedom are large, which corresponds approximately to a 95% coverage probability[^nist2012ehandbook-e15]. NIST also sets k = 2 by convention for its own measurement results[^taylor1994nist-e1]. That is NIST's own policy; elsewhere, follow your institution's or target journal's requirements. If a large component was repeated only a few times and has few degrees of freedom, the degrees of freedom of the combined result become highly questionable[^nist2012ehandbook-e16]; in that case do not just use k = 2, but estimate the effective degrees of freedom first and then choose k.

**4. Check yourself.** Compare the standard deviation you actually observe with the one your components predict when combined[^jcgm2008gum-e17]. A big difference means the budget has missed or overestimated something.

### Step 6: Blind analysis, so you don't steer the result

For the definition of blind analysis and the common methods, see the [physical sciences field overview](../07_fields/physical-sciences/README.md#blind-analysis-fix-the-method-before-you-look-at-the-answer). This section covers why to do it and how to put it into practice.

**Why:** what sets **experimenter's bias** apart from other biases is that its size cannot be estimated; it can only be prevented by method[^klein2005blind-e1]. Klein and Roodman consider that the most common form in nuclear and particle physics is probably the **stopping bias**: you stop looking for mistakes and publish once the result gets close to what you expected[^klein2005blind-e2]. For example, a series of speed-of-light measurements from 1930 to 1940 differed from later determinations by 17 km/s; an analysis they cite suggests that researchers kept searching for errors until their results came close to the accepted value, and then stopped[^klein2005blind-e3]. Looking at historical measurements, they found that values tended to lie close to the published average of the time rather than to the eventual final value, though they also say this does not necessarily prove bias[^klein2005blind-e4].

**How (taking precision measurement as the example):**

- **Hide the answer, not the data.** Blind analysis is not about stopping you from looking at the data; it is about keeping the result from feeding back into the analysis[^klein2005blind-e17]. When you are measuring a single parameter precisely and that parameter does not depend directly on the number of events, the hidden-answer method works best[^klein2005blind-e14]: in the software, add a fixed hidden offset to the final result, so the people doing the analysis cannot see the true value[^junk2021reproducibility-e49]. Keep the scheme as simple as possible and hide as little as possible[^klein2005blind-e6].
- **Tabletop experiments can do it too.** When Dunnington measured the electron's charge-to-mass ratio, he had the machinist set a key angle arbitrarily and measured it precisely only after the analysis was done[^roodman2003blind-e5]. One gravity experiment had someone outside the collaboration hold the exact mass of one of the test masses; the team knew it only to 1%[^klein2005blind-e15].
- **Agree on unblinding rules in advance.** If you change any step of the analysis after unblinding, it no longer counts as a fully blind analysis[^junk2021reproducibility-e10]. Ideally, decide beforehand how you will handle surprises[^klein2005blind-e10]. A collaboration can also require that unblinding be approved by a larger group rather than decided by the analysts themselves[^klein2005blind-e11].
- **What if you find a real mistake after unblinding?** Doing a blind analysis is no reason to publish a result you know is wrong[^klein2005blind-e9]; state in the paper which changes were made after unblinding[^klein2005blind-e8]. The gravity experiment above later improved its analysis but still published the result from before the improvement[^klein2005blind-e15].

> **Where sources disagree: is blind analysis worth it?**
> - **For**: Klein and Roodman argue that the size of experimenter's bias cannot be estimated, so the only remedy is a method that prevents it[^klein2005blind-e1]; every experiment should consider the possibility of experimenter's bias, though blind analysis is not always feasible or necessary[^klein2005blind-e5].
> - **Worried about the cost**: Klein and Roodman themselves admit that the objection that "unexpected phenomena can only be found by full exploration of the data" is a serious one[^klein2005blind-e12]. The physicist Golub, in a short comment that was not peer reviewed, argues that blind analysis seriously hampers the search for systematic errors and makes it impossible to study unexpected events in the hidden region[^golub2023blind-e1].
>
> In practice: for precision measurements, prefer "hide the answer". It masks only the final number and does not get in the way of checking the data and systematic errors. Whether to blind and how, settle with your advisor before you look at the data, and write it down.

### Step 7: Cross-checks and consistency checks

**How:**

- **Split the data by condition.** Group by date, instrument configuration, operator, and sample, compute a result for each, and see whether they agree within their uncertainties.
- **Look at control samples first.** Running the analysis on control samples first sometimes reveals background sources or calibration mistakes you had not noticed[^junk2021reproducibility-e50].
- **If the data say the model is incomplete, change the model.** When the observed data (including independent determinations of the same quantity) show that the measurement model is incomplete, the model has to be revised[^jcgm2008gum-e16].
- **Report anomalous results.** AIAA journals require that anomalous results be pointed out, whether or not they can be explained[^aiaaeditorialpolicy-e9].

**Where people go wrong:** taking "agrees with earlier measurements or with theory" as evidence that the measurement is right. Roodman points out that a result's value, and whether it agrees with earlier measurements, says nothing about whether the measurement itself was done correctly[^roodman2003blind-e4]. Also, some cross-checks can only be done after unblinding[^klein2005blind-e13]; it is best to list them in advance.

### Step 8: Record everything

**How:**

- **Record on the spot.** Write each entry immediately after doing the work[^schnell2015ten-e3]; if you rely on memory, you are likely to forget key steps when you need them[^schnell2015ten-e9].
- **Cross out mistakes; don't erase them.** In a paper notebook, draw a single thin line through a mistake and write the correct information next to it[^schnell2015ten-e4]. (Schnell 2015 is written for biologists who do computational work; we borrow its general record-keeping principles here.)
- **Record running conditions.** Particle physics experiments continuously log environmental variables such as temperature, pressure, and humidity[^junk2021reproducibility-e42]. When you notice something abnormal, flag the affected data so they do not bias the result[^junk2021reproducibility-e43].
- **Record the order of data collection.** AIAA journals require papers to state the experimental conditions and the sequence in which data were taken[^aiaaeditorialpolicy-e6], which you cannot write without records made at the time.
- **Keep the raw data behind every figure**[^schnell2015ten-e7]. For general practice on organizing data and code, see [Organizing your research materials](../08_throughout/organizing_materials.md) under Throughout the project.

**Why:** blunders such as misrecording or miscalculating a number are not covered by the uncertainty[^jcgm2008gum-e5]; only records and checking can catch them.

### Step 9: Report the result

The reporting requirements of the GUM and the AIAA (list all components and how each was evaluated, state k, state sources not included, and so on) are already listed in the [mechanical engineering field overview](../07_fields/mechanical-engineering/README.md#measurement-results-must-come-with-an-uncertainty), along with wording issues such as not attaching a number to "accuracy". Three additions here:

- **Report statistical and systematic uncertainties separately, and break the systematic part down by source**[^junk2021reproducibility-e39]. Then readers can judge whether taking more data would still help, or whether the result is already "systematics limited"[^junk2021reproducibility-e38].
- **Significant figures**: the GUM says it is usually enough to give an uncertainty to at most two significant figures[^jcgm2008gum-e26]. The rule the Particle Data Group uses for the *Review of Particle Physics* is more specific: if the three highest-order digits of the error are between 100 and 354, keep two significant figures; if between 355 and 949, keep one[^pdg2024intro-e3]. The central value is rounded to the same decimal place as the error; for example, 0.827 ± 0.119 becomes 0.83 ± 0.12[^pdg2024intro-e4].
- **Watch the wording when reading the literature**: uncertainty is a numerical estimate of the possible values of the error, but particle physicists often say "error" when they mean "uncertainty"[^junk2021reproducibility-e37].

### Step 10: Compare with theory and with other measurements

**How:**

- **First check whether the measurements agree with each other.** The Particle Data Group's approach: take a weighted average, then use chi-squared (χ², which measures how far each measurement lies from the average, in units of its own uncertainty) to check whether the measurements are consistent[^pdg2024intro-e1]. A large χ² probably means at least one experiment has underestimated its error; if you don't know which one, assume all the errors were underestimated by the same factor[^pdg2024intro-e2].
- **Watch for shared sources of error.** To judge whether two results agree, separate the error sources they share from those that are independent[^junk2021reproducibility-e52].
- **A large uncertainty is not a virtue.** Results with large systematic uncertainties "agree with others" more easily[^junk2021reproducibility-e53]; but overestimating systematic uncertainty has its costs too[^junk2021reproducibility-e51].
- **Be suspicious of agreement that is too good.** An unusually low χ² in a global fit is often taken as a sign that the measurements may be biased[^klein2005blind-e18].
- **Disagreeing with others does not mean you are wrong.** An outlying data point may be wrong, or it may be the other way round and the bulk of the data is wrong[^pdg2024intro-e5]. A repeat experiment that changes some conditions can be more informative than an exact copy[^junk2021reproducibility-e54].

## 3. Checklist

**Must do**

- [ ] The measurand is fully defined, with conditions and measurement method stated[^jcgm2008gum-e11][^jcgm2008gum-e12]
- [ ] All recognized significant systematic effects are corrected, and the uncertainty of each correction is included[^jcgm2008gum-e10][^junk2021reproducibility-e35]
- [ ] The uncertainty of the reference standards is included[^jcgm2008gum-e19]
- [ ] All uncertainty components and how they were evaluated are listed[^jcgm2008gum-e8]
- [ ] When reporting an expanded uncertainty, k is stated[^jcgm2008gum-e9]
- [ ] Known sources of uncertainty that were not included are stated (an AIAA journal requirement)[^aiaaeditorialpolicy-e5]
- [ ] Experimental conditions and the order of data collection are recorded and reported (an AIAA journal requirement)[^aiaaeditorialpolicy-e6]

**Better practice**

- [ ] Expected sensitivity estimated before taking data[^junk2021reproducibility-e44]
- [ ] A check standard used to monitor the measurement process continuously[^nist2012ehandbook-e2]
- [ ] The whole chain tested with a known signal (a standard candle)[^junk2021reproducibility-e46]
- [ ] Blinding scheme fixed before looking at results, with a plan for surprises after unblinding[^klein2005blind-e10]
- [ ] Statistical and systematic uncertainties reported separately, with the systematic part broken down by source[^junk2021reproducibility-e38][^junk2021reproducibility-e39]
- [ ] Observed standard deviation compared with the one predicted by the budget[^jcgm2008gum-e17]
- [ ] Uncertainty given to at most two significant figures as a rule[^jcgm2008gum-e26]; central value rounded to match (the Particle Data Group's practice)[^pdg2024intro-e4]

**Fine to skip; not a flaw**

- Blind analysis is not always feasible or necessary for every measurement, but every experiment should consider the possibility of experimenter's bias[^klein2005blind-e5].

**Common reviewer criticisms that are not valid**

- "The result disagrees with theory (or with earlier measurements), so the measurement is wrong": whether a value agrees with earlier ones says nothing about whether the measurement itself was done correctly[^roodman2003blind-e4]; it may also be the earlier bulk of the data that is wrong[^pdg2024intro-e5]. The better question is whether the systematic effects have all been found.

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Reporting only the value, not the uncertainty | The result cannot be compared with other measurements or with standards[^jcgm2008gum-e28] |
| Estimating uncertainty from repeated measurements alone | Systematic effects don't change with repetition, so repetition can't reveal them[^junk2021reproducibility-e36] |
| Adding a "worst case" bound directly to the other components | Convert it to an equivalent standard deviation before combining[^nist2012ehandbook-e12] |
| Using a U quoted elsewhere directly as a standard uncertainty | Divide by k first[^nist2012ehandbook-e11] |
| Combining as if independent when the input quantities are correlated | The correlations must be taken into account[^jcgm2008gum-e24] |
| Stopping the search for mistakes once the result is close to what you expected | That is exactly the stopping bias[^klein2005blind-e2] |
| Quietly changing the analysis after unblinding | It is no longer a blind analysis[^junk2021reproducibility-e10]; say so in the paper[^klein2005blind-e8] |
| Thinking blind analysis removes systematic errors | It only guards against experimenter's bias[^klein2005blind-e7] |
| Filling in records from memory afterwards | Key details get forgotten[^schnell2015ten-e9]; blunders are not covered by the uncertainty[^jcgm2008gum-e5] |

## 5. Further reading

- **JCGM 100:2008 (GUM)**: the international guide from the Joint Committee for Guides in Metrology, free to download from the website of the International Bureau of Weights and Measures (BIPM). You can start with Chapter 3 (basic concepts) and Chapter 7 (reporting). It also reminds you that it is no substitute for critical thinking, intellectual honesty, and professional skill[^jcgm2008gum-e27].
- **NIST/SEMATECH e-Handbook of Statistical Methods, Chapter 2**: a free online handbook on a US government website, covering calibration, check standards, and uncertainty budgets; good to have open while you work.
- **Klein & Roodman 2005, Blind Analysis in Nuclear and Particle Physics**: on experimenter's bias and the various blind-analysis methods. Read it together with Golub 2023 (not peer reviewed), which questions it.
- **Junk & Lyons 2021**: how particle physics handles systematic uncertainties, control samples, calibration, and repeat experiments.
- **Particle Data Group, *Review of Particle Physics*, Introduction, Section 5**: how the Particle Data Group averages multiple measurements, handles inconsistent data, and rounds.

[^jcgm2008gum-e11]: JCGM 100:2008 (GUM), 3.1.1. [Evidence](../../sources/notes/jcgm2008gum.md#e11)
[^jcgm2008gum-e12]: JCGM 100:2008 (GUM), 3.1.3. [Evidence](../../sources/notes/jcgm2008gum.md#e12)
[^jcgm2008gum-e13]: JCGM 100:2008 (GUM), D.1.1. [Evidence](../../sources/notes/jcgm2008gum.md#e13)
[^jcgm2008gum-e14]: JCGM 100:2008 (GUM), 3.4.2. [Evidence](../../sources/notes/jcgm2008gum.md#e14)
[^jcgm2008gum-e15]: JCGM 100:2008 (GUM), 3.4.2. [Evidence](../../sources/notes/jcgm2008gum.md#e15)
[^jcgm2008gum-e16]: JCGM 100:2008 (GUM), 3.4.2. [Evidence](../../sources/notes/jcgm2008gum.md#e16)
[^jcgm2008gum-e17]: JCGM 100:2008 (GUM), 3.4.3. [Evidence](../../sources/notes/jcgm2008gum.md#e17)
[^jcgm2008gum-e18]: JCGM 100:2008 (GUM), 3.2.3. [Evidence](../../sources/notes/jcgm2008gum.md#e18)
[^jcgm2008gum-e10]: JCGM 100:2008 (GUM), 3.2.4. [Evidence](../../sources/notes/jcgm2008gum.md#e10)
[^jcgm2008gum-e19]: JCGM 100:2008 (GUM), 3.2.4, Note 1. [Evidence](../../sources/notes/jcgm2008gum.md#e19)
[^jcgm2008gum-e3]: JCGM 100:2008 (GUM), 2.3.2, 2.3.3. [Evidence](../../sources/notes/jcgm2008gum.md#e3)
[^jcgm2008gum-e21]: JCGM 100:2008 (GUM), 4.2.7. [Evidence](../../sources/notes/jcgm2008gum.md#e21)
[^jcgm2008gum-e22]: JCGM 100:2008 (GUM), 4.3.7. [Evidence](../../sources/notes/jcgm2008gum.md#e22)
[^jcgm2008gum-e23]: JCGM 100:2008 (GUM), 5.1.2. [Evidence](../../sources/notes/jcgm2008gum.md#e23)
[^jcgm2008gum-e24]: JCGM 100:2008 (GUM), 5.2.1. [Evidence](../../sources/notes/jcgm2008gum.md#e24)
[^jcgm2008gum-e25]: JCGM 100:2008 (GUM), 3.3.7. [Evidence](../../sources/notes/jcgm2008gum.md#e25)
[^jcgm2008gum-e9]: JCGM 100:2008 (GUM), 7.2.3. [Evidence](../../sources/notes/jcgm2008gum.md#e9)
[^jcgm2008gum-e8]: JCGM 100:2008 (GUM), 7.1.4. [Evidence](../../sources/notes/jcgm2008gum.md#e8)
[^jcgm2008gum-e26]: JCGM 100:2008 (GUM), 7.2.6. [Evidence](../../sources/notes/jcgm2008gum.md#e26)
[^jcgm2008gum-e5]: JCGM 100:2008 (GUM), 3.4.7. [Evidence](../../sources/notes/jcgm2008gum.md#e5)
[^jcgm2008gum-e27]: JCGM 100:2008 (GUM), 3.4.8. [Evidence](../../sources/notes/jcgm2008gum.md#e27)
[^jcgm2008gum-e28]: JCGM 100:2008 (GUM), 0.1. [Evidence](../../sources/notes/jcgm2008gum.md#e28)
[^nist2012ehandbook-e1]: NIST/SEMATECH e-Handbook, 2.3.1. [Evidence](../../sources/notes/nist2012ehandbook.md#e1)
[^nist2012ehandbook-e2]: NIST/SEMATECH e-Handbook, 2.1.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e2)
[^nist2012ehandbook-e3]: NIST/SEMATECH e-Handbook, 2.1.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e3)
[^nist2012ehandbook-e4]: NIST/SEMATECH e-Handbook, 2.2.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e4)
[^nist2012ehandbook-e5]: NIST/SEMATECH e-Handbook, 2.5.1. [Evidence](../../sources/notes/nist2012ehandbook.md#e5)
[^nist2012ehandbook-e6]: NIST/SEMATECH e-Handbook, 2.5.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e6)
[^nist2012ehandbook-e7]: NIST/SEMATECH e-Handbook, 2.5.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e7)
[^nist2012ehandbook-e8]: NIST/SEMATECH e-Handbook, 2.5.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e8)
[^nist2012ehandbook-e9]: NIST/SEMATECH e-Handbook, 2.5.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e9)
[^nist2012ehandbook-e10]: NIST/SEMATECH e-Handbook, 2.5.4. [Evidence](../../sources/notes/nist2012ehandbook.md#e10)
[^nist2012ehandbook-e11]: NIST/SEMATECH e-Handbook, 2.5.4. [Evidence](../../sources/notes/nist2012ehandbook.md#e11)
[^nist2012ehandbook-e12]: NIST/SEMATECH e-Handbook, 2.5.4.1. [Evidence](../../sources/notes/nist2012ehandbook.md#e12)
[^nist2012ehandbook-e13]: NIST/SEMATECH e-Handbook, 2.5.4.1. [Evidence](../../sources/notes/nist2012ehandbook.md#e13)
[^nist2012ehandbook-e14]: NIST/SEMATECH e-Handbook, 2.5.6. [Evidence](../../sources/notes/nist2012ehandbook.md#e14)
[^nist2012ehandbook-e15]: NIST/SEMATECH e-Handbook, 2.5.2. [Evidence](../../sources/notes/nist2012ehandbook.md#e15)
[^nist2012ehandbook-e16]: NIST/SEMATECH e-Handbook, 2.5.7.1. [Evidence](../../sources/notes/nist2012ehandbook.md#e16)
[^nist2012ehandbook-e17]: NIST/SEMATECH e-Handbook, 2.1.1. [Evidence](../../sources/notes/nist2012ehandbook.md#e17)
[^taylor1994nist-e1]: Taylor & Kuyatt 1994 (NIST TN 1297), 6.5. [Evidence](../../sources/notes/taylor1994nist.md#e1)
[^junk2021reproducibility-e34]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e34)
[^junk2021reproducibility-e35]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e35)
[^junk2021reproducibility-e36]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e36)
[^junk2021reproducibility-e37]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e37)
[^junk2021reproducibility-e38]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e38)
[^junk2021reproducibility-e39]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e39)
[^junk2021reproducibility-e40]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e40)
[^junk2021reproducibility-e41]: Junk & Lyons 2021, §3.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e41)
[^junk2021reproducibility-e42]: Junk & Lyons 2021, §6.1. [Evidence](../../sources/notes/junk2021reproducibility.md#e42)
[^junk2021reproducibility-e43]: Junk & Lyons 2021, §6.1. [Evidence](../../sources/notes/junk2021reproducibility.md#e43)
[^junk2021reproducibility-e44]: Junk & Lyons 2021, §6.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e44)
[^junk2021reproducibility-e45]: Junk & Lyons 2021, §6.3. [Evidence](../../sources/notes/junk2021reproducibility.md#e45)
[^junk2021reproducibility-e46]: Junk & Lyons 2021, §6.4. [Evidence](../../sources/notes/junk2021reproducibility.md#e46)
[^junk2021reproducibility-e47]: Junk & Lyons 2021, §6.4. [Evidence](../../sources/notes/junk2021reproducibility.md#e47)
[^junk2021reproducibility-e48]: Junk & Lyons 2021, §6.5. [Evidence](../../sources/notes/junk2021reproducibility.md#e48)
[^junk2021reproducibility-e10]: Junk & Lyons 2021, §6.6. [Evidence](../../sources/notes/junk2021reproducibility.md#e10)
[^junk2021reproducibility-e49]: Junk & Lyons 2021, §6.6. [Evidence](../../sources/notes/junk2021reproducibility.md#e49)
[^junk2021reproducibility-e50]: Junk & Lyons 2021, §6.6. [Evidence](../../sources/notes/junk2021reproducibility.md#e50)
[^junk2021reproducibility-e51]: Junk & Lyons 2021, §6.9. [Evidence](../../sources/notes/junk2021reproducibility.md#e51)
[^junk2021reproducibility-e52]: Junk & Lyons 2021, §5. [Evidence](../../sources/notes/junk2021reproducibility.md#e52)
[^junk2021reproducibility-e53]: Junk & Lyons 2021, §5. [Evidence](../../sources/notes/junk2021reproducibility.md#e53)
[^junk2021reproducibility-e54]: Junk & Lyons 2021, §5. [Evidence](../../sources/notes/junk2021reproducibility.md#e54)
[^klein2005blind-e1]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e1)
[^klein2005blind-e2]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e2)
[^klein2005blind-e3]: Klein & Roodman 2005, §1. [Evidence](../../sources/notes/klein2005blind.md#e3)
[^klein2005blind-e4]: Klein & Roodman 2005, §1. [Evidence](../../sources/notes/klein2005blind.md#e4)
[^klein2005blind-e5]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e5)
[^klein2005blind-e6]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e6)
[^klein2005blind-e7]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e7)
[^klein2005blind-e8]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e8)
[^klein2005blind-e9]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e9)
[^klein2005blind-e10]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e10)
[^klein2005blind-e11]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e11)
[^klein2005blind-e12]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e12)
[^klein2005blind-e13]: Klein & Roodman 2005, §2. [Evidence](../../sources/notes/klein2005blind.md#e13)
[^klein2005blind-e14]: Klein & Roodman 2005, §3.2. [Evidence](../../sources/notes/klein2005blind.md#e14)
[^klein2005blind-e15]: Klein & Roodman 2005, §3.2.1. [Evidence](../../sources/notes/klein2005blind.md#e15)
[^klein2005blind-e17]: Klein & Roodman 2005, §3.4. [Evidence](../../sources/notes/klein2005blind.md#e17)
[^klein2005blind-e18]: Klein & Roodman 2005, §1. [Evidence](../../sources/notes/klein2005blind.md#e18)
[^roodman2003blind-e4]: Roodman 2003, §2. [Evidence](../../sources/notes/roodman2003blind.md#e4)
[^roodman2003blind-e5]: Roodman 2003, §1. [Evidence](../../sources/notes/roodman2003blind.md#e5)
[^golub2023blind-e1]: Golub 2023 (not peer reviewed), §2. [Evidence](../../sources/notes/golub2023blind.md#e1)
[^aiaaeditorialpolicy-e6]: AIAA Editorial Policy Statement, Statement of Experimental Design. [Evidence](../../sources/notes/aiaaeditorialpolicy.md#e6)
[^aiaaeditorialpolicy-e9]: AIAA Editorial Policy Statement, Estimation of Precision Uncertainty. [Evidence](../../sources/notes/aiaaeditorialpolicy.md#e9)
[^aiaaeditorialpolicy-e5]: AIAA Editorial Policy Statement, Statement of Total Uncertainty. [Evidence](../../sources/notes/aiaaeditorialpolicy.md#e5)
[^schnell2015ten-e3]: Schnell 2015, Rule 4. [Evidence](../../sources/notes/schnell2015ten.md#e3)
[^schnell2015ten-e4]: Schnell 2015, Rule 5. [Evidence](../../sources/notes/schnell2015ten.md#e4)
[^schnell2015ten-e9]: Schnell 2015, Rule 3. [Evidence](../../sources/notes/schnell2015ten.md#e9)
[^schnell2015ten-e7]: Schnell 2015, Rule 6. [Evidence](../../sources/notes/schnell2015ten.md#e7)
[^pdg2024intro-e1]: Particle Data Group 2024, Introduction §5.2.2. [Evidence](../../sources/notes/pdg2024intro.md#e1)
[^pdg2024intro-e2]: Particle Data Group 2024, Introduction §5.2.2. [Evidence](../../sources/notes/pdg2024intro.md#e2)
[^pdg2024intro-e3]: Particle Data Group 2024, Introduction §5.3. [Evidence](../../sources/notes/pdg2024intro.md#e3)
[^pdg2024intro-e4]: Particle Data Group 2024, Introduction §5.3. [Evidence](../../sources/notes/pdg2024intro.md#e4)
[^pdg2024intro-e5]: Particle Data Group 2024, Introduction §5.4. [Evidence](../../sources/notes/pdg2024intro.md#e5)
