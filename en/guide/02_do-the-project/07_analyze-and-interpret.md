# Analysis and interpretation

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. The numbers and statistics in Section 3 are mainly for quantitative research; if you do qualitative research, take the underlying reasoning.

## Where you are

The experiments have finished, or the data is all in. You have a pile of numbers, tables and logs, maybe a few rough plots.

You may now be facing questions like these:

- The results look good, but you're not sure: is this real, or did something go wrong?
- The analysis you planned is done and the result is middling; with a different analysis it seems to become "significant". Can you write it up that way?
- The p-value is below 0.05. Does that mean the method works?
- The result is the opposite of what you expected, or you found nothing at all. Was the whole project a waste?
- In the paper, how strong a conclusion can you write?

## What this stage is for

Turn a pile of results into **conclusions that evidence actually supports**. Concretely, answer these seven questions:

1. Is anything wrong with the data or the code?
2. Which analyses were planned in advance, and which did you think of after seeing the data?
3. How big is the difference, and how certain is it?
4. Apart from your explanation, what else could produce the same result?
5. What do you do with negative and unexpected results?
6. How far can your conclusions reach?
7. When the evidence doesn't match your original claim, how do you revise it?

## How to use this chapter

Work through Sections 1 to 6 roughly in order: first make sure the data is right, then analyze, then interpret. Section 7 can come up at any time: whenever a step shows that the evidence can't hold up your original claim, come back and revise the claim.

Different research strategies need different statistical details. The concrete steps for comparing against baselines, running ablation studies, and comparing tools over multiple runs are in the strategy pages: [Comparative evaluation](../05_research-strategies/compare_evaluate.md#is-the-difference-real), [Building and improving](../05_research-strategies/build_improve.md), and [Causal explanation](../05_research-strategies/explain_causality.md#actively-rule-out-alternative-explanations). This chapter covers only the part every kind of study has to do `[Our analysis]`.

Everything in this chapter serves one goal: don't fool yourself, and you are the easiest person to fool[^feynman1974cargo-e7].

---

## 1. Check the data before you look at the conclusions

**When results come in, don't rush to interpret them. The first thing to do is look at the raw data and raw outputs yourself.**

Many errors don't throw errors. Training neural networks is the classic case: the code is syntactically fine, yet the pipeline isn't doing what you think it is, and that is hard to spot[^karpathy2019recipe-e3]. So go through things by hand:

- **Read a few dozen raw samples and outputs, one by one.** Outliers (values far away from the rest of the data) deserve special attention. A write-up of lessons from training neural networks says they almost always uncover problems in data quality or preprocessing[^karpathy2019recipe-e7]. The data science standard for software engineering lists "manually inspects some non-trivial portion of the data (i.e. data sanity checks)" as a desirable attribute[^ralph2020empirical-e199].
- **Don't skip the checks because a dataset is well known.** A machine learning methods guide warns that a dataset being used in many papers doesn't mean it is good quality[^lones2021avoid-e19]. In software engineering, a paper on misclassified bug data concludes that automated quantitative analysis should always be paired with humans checking the input data and the results; before using a bug dataset, you should at least manually validate enough samples[^herzig2013bug-e5].
- **Look for duplicates and anomalies, but don't delete freely.** The same machine learning guide notes that a common problem is the same data point being included several times by accident; remove outliers only if they are likely noise or errors, not genuine extreme cases[^lones2021avoid-e20]. Record what you removed and why `[Our analysis]`.

**When results are surprisingly good, check harder.** One form of self-deception is asymmetric checking: you hunt hard for errors when a result is off from what you expected, and stop looking when it is close. This happened in the history of measuring the charge of the electron: when later researchers got a value too far above the authoritative one, they looked for "what went wrong"; when they got a value close to it, they didn't look as carefully[^feynman1974cargo-e14]. If you only check in one direction, your results get pulled toward what you expected. Check "good" results and "bad" results equally hard `[Our analysis]`.

Take "large language models detecting smart contract vulnerabilities" as an example. If you see a 95% detection rate, check these first `[Our analysis]`:

| What to check | How |
|---|---|
| Is the output parsing right? | Randomly pick 30 raw model outputs, judge them by hand, and compare with what the code parsed |
| Are the labels right? | Spot-check a batch of "vulnerable" contracts and confirm the vulnerability really exists |
| Are there duplicates? | Check whether the same contract appears several times in the benchmark under different names |
| Has the model "seen" them? | Check whether these contracts were public before the model's training cutoff |
| Outlying samples | Look at the examples with the longest detection time and the longest and shortest outputs |

**Write it down:** List three reasons your results might look good without being real, and check each with the cheapest method you can. Only then move on.

## 2. Do the planned analyses first; label unplanned ones as exploratory

**Run the analyses you planned before you started, and record the result of every planned analysis, good or bad. Analyses you think of after seeing the data are fine to run, but label them separately as "exploratory".**

Why separate them? Because a prediction made in advance and an explanation made afterward carry different weight as evidence. Forming a hypothesis after seeing the results but presenting it as if you had it all along is called HARKing (hypothesizing after the results are known)[^nosek2018preregistration-e2]. The software engineering empirical standards list two antipatterns: HARKing in research presented as confirmatory, and reporting only the statistically significant subset of the tests you ran[^ralph2020empirical-e27]. The second is called p-hacking.

Resolving "I won't do that" is not enough: memory is fallible, people reason toward the answer they want without noticing, and these biases often operate outside awareness[^nosek2018preregistration-e3]. Psychology methodologists point out that researchers usually don't realize they are p-hacking, or what it does to their results[^nelson2018psychology-e8]. They describe what researchers typically do when a first analysis isn't significant: keep digging through the data, check whether outliers are masking the effect, look at a different subset of participants, or code the outcome variable a different way[^nelson2018psychology-e6]. Each step seems reasonable on its own; in their simulations, stacking these practices together pushed the false-positive rate (treating an effect that isn't there as real) from 5% to 61%[^nelson2018psychology-e7].

**How:**

- **Report every planned analysis.** Once you have an analysis plan, you have to report the results of all the analyses in it; otherwise it is still selective reporting[^nosek2018preregistration-e6]. This is not an unrealistic standard: a review of 195 pre-analysis plans from two registries used in political science and economics[^ofosu2023preanalysis-e1] found that the median paper in the sample failed to report 25% of the hypotheses in its plan[^ofosu2023preanalysis-e9].
- **For unplanned analyses, label them and say why you added them.** A methods guide in political science says exploratory analysis is allowed; the point of writing an analysis plan in advance is not to forbid it but to make clear where it came from[^egappreanalysis-e5]. The authors of the review above make the same case: explore freely beyond the plan, but mark clearly in the paper which analyses were not specified in advance, and explain why you added them[^ofosu2023preanalysis-e14]. In the same review, 82% of papers that reported hypotheses not in their plan didn't say so[^ofosu2023preanalysis-e10]. The American Psychological Association's reporting standards for quantitative research also divide hypotheses, analyses and conclusions into primary, secondary and exploratory[^appelbaum2018journal-e1].
- **If you deviated from the plan, say what changed and why.** Honestly reporting changes and the reasons for them is still far more credible than having no plan at all[^nosek2018preregistration-e5]. Yet in the same review, of 14 deviations from the planned models, only 1 was disclosed[^ofosu2023preanalysis-e7].
- **Be especially careful with subgroups you split out afterward.** The reporting guideline for medical clinical trials says subgroup comparisons made after looking at the data are particularly unlikely to be confirmed by later studies; and if one subgroup is significant and another isn't, that alone doesn't show the two groups differ[^hopewell2025consortee-e49].

The point is not that prediction is superior to exploration after the fact; it is that people can tell which is which[^nosek2018preregistration-e4]. Exploratory findings are often exactly where the next project starts `[Our analysis]`.

**If you didn't write an analysis plan before you started** `[Our analysis]`: write one now, describing what you "would have done" before seeing the results, and do it as early as possible; in the paper, say honestly which analyses were decided after seeing results. Next time, write the analysis plan at the [From research questions to an evidence plan](01_question-to-evidence.md) stage.

**Write it down:** Keep an analysis log, adding a row for every analysis you run.

| Analysis | Planned / exploratory | When you decided to run it | Why | Result (good or bad) |
|---|---|---|---|---|
| Overall detection rate, new method vs. baseline | Planned | At the proposal stage | Central claim | |
| Broken down by vulnerability type | Exploratory | After seeing the overall result | Suspected the gain was concentrated in one type | |

## 3. Report how big and how certain, not just the p-value

**For every key result, answer two questions: how big is the difference (or association)? And how certain is that number?** The first is the effect size; the second is the uncertainty, usually expressed as a confidence interval (the range the true value most likely falls in) or a standard error.

Reporting standards and methods literature across fields agree on this:

- The reporting standards for education research require an effect size for key statistical results, such as treatment effects or regression coefficients[^aera2006standards-e8], along with its uncertainty, such as a standard error or confidence interval[^aera2006standards-e9].
- The reporting guideline for medical clinical trials requires a confidence interval for the effect size of every outcome, not just a p-value[^hopewell2025consortee-e52].
- The advice from computer performance evaluation is to report performance changes as a confidence interval for the effect size: it shows how big the change is, how wide the error margin is, and how certain it is, and it is less easily misread than a significance test[^kalibera2013rigorous-e8].

**Why isn't the p-value enough?**

- **Significant doesn't mean important.** A machine learning methods guide warns that with enough samples, even a tiny difference becomes significant[^lones2021avoid-e8]. An example from software analytics: a "significant" correlation coefficient of just 0.01 has negligible practical meaning and is no different from no correlation[^menzies2019bad-e2]. So methodologists recommend fixing, before the study begins, how big a difference would actually matter: the smallest effect size of interest[^menzies2019bad-e3].
- **Not significant doesn't mean no difference.** When a result isn't significant, don't rush to write "there is no difference between the two". First look at how wide the confidence interval is: if it is wide, all it says is that this data can't tell them apart `[Our analysis]`. And don't compute statistical power (the probability that the study would detect a real difference) after the fact from this result to explain away non-significance; that has no value and may mislead readers[^hopewell2025consortee-e18].
- **Effects of the same size aren't necessarily equally important.** A paper on interpreting effect sizes for education interventions points out that effects of the same size rarely have the same importance[^kraft2019interpreting-e21]. Its example: when effects are similar, the cheaper intervention deserves more weight[^kraft2019interpreting-e13]. The same holds in computer science. Take two methods that each raise the detection rate by 5 percentage points: if one gets there by making ten times as many calls to the large language model's API (application programming interface) and the other adds almost no cost, they mean very different things `[Our analysis]`.

**How:**

- **Report the variation, not just the mean or the best run.** A checklist for empirical evaluation in programming languages warns that too few trials can make you mistake noise for signal[^blackburn2018sigplan-e7]. An example from Java performance evaluation: looking only at the best result suggests one garbage collector is clearly faster; looking at the confidence intervals, the two overlap and the difference is likely just random variation[^georges2007statistically-e2]. A satirical piece on tricks for padding software engineering papers lists "run it again and again and report only the run that wins" as one of them[^zeller2021devil-e1].
- **Summarize honestly.** The same checklist says: don't summarize improvements of 4%, 6%, 7% and 49% as "up to 49%"; report the full distribution[^blackburn2018sigplan-e9]. Precision should also match the error: reporting "49.9%" when the error is plus or minus 1% overstates the precision[^blackburn2018sigplan-e30].
- **If you run many tests, correct for it.** A machine learning methods guide gives the example that with 20 pairwise tests at a 95% confidence level, one is likely to give a wrong conclusion[^lones2021avoid-e7]. There are many correction methods, and when correction is needed is debated[^lones2021avoid-e12]. At a minimum, report how many comparisons you made in total `[Our analysis]`.

In the running example, a good statement of a result looks like this `[Our analysis]`: "On 300 contracts that appeared only after the training cutoff, adding vulnerability-pattern hints raised the reentrancy detection rate from 41% to 52% (5 runs; 95% confidence interval for the improvement: 6 to 16 percentage points); the false-positive rate was essentially unchanged." Compare that with "detection rate improved significantly (p < 0.05)": the first sentence tells readers how big the difference is, how certain, and under what conditions.

For which test to use and how to compute confidence intervals, ask your advisor or consult statistical methods resources for your field; for statistical details when comparing tools and methods, see [Comparative evaluation: is the difference real?](../05_research-strategies/compare_evaluate.md#is-the-difference-real) `[Our analysis]`.

**Write it down:** Rewrite your central result as a sentence like the one above: conditions, effect size, uncertainty, number of runs. If you can't state the uncertainty, go back and run more experiments or do the calculation.

## 4. Rule out alternative explanations one by one

**Once you see a result, ask yourself: apart from my explanation, what else could produce the same result? Then check each one.**

When you run an experiment, report everything that might make the result invalid: other causes that could explain it, and which of those you have ruled out with other experiments, and how[^feynman1974cargo-e11]. An article in machine learning criticizing trends in scholarship also lists "considering and ruling out alternative hypotheses" as something good papers do[^lipton2019troubling-e1].

Almost every study needs to get past these first `[Our analysis]`:

| Alternative explanation | Ask yourself | How to check it in the example |
|---|---|---|
| Chance | With different runs or a different batch of samples, does the result hold? | Run multiple times and look at the confidence interval (Section 3) |
| An error | Is there a problem in the code, the labels, or the parsing? | The checks in Section 1 |
| Measuring the wrong thing | Does the metric really capture what you care about? | If you report detection rate but not false positives, the "improvement" may just be the model flagging vulnerabilities more eagerly |
| Another factor | Is something you didn't control changing at the same time? | Longer prompts, a different model version, benchmark contracts the model has "seen" |
| Only true here | Does it hold on a different dataset or setup? | Try another batch of contracts and another model |

"Measuring the wrong thing" is often overlooked. When you use an indirect metric in place of the one you actually care about, you have to justify the substitution[^blackburn2018sigplan-e13].

**Beyond "how well does it work", also ask "what made it work, and why"**[^lipton2019troubling-e7]. The same article says three practices are common in the strongest empirical papers: error analysis (going through the failures one by one to find which kinds of cases go wrong), ablation studies, and robustness checks (changing the data, setup or analysis method to see whether the conclusion still holds)[^lipton2019troubling-e8].

When your claim is causal ("X causes Y"), ruling out alternative explanations has to be more systematic; see [Causal explanation](../05_research-strategies/explain_causality.md#actively-rule-out-alternative-explanations). When your claim is "the new method is better", ablation studies have to show where the improvement comes from; see [Building and improving](../05_research-strategies/build_improve.md) `[Our analysis]`. For a systematic discussion of threats to validity, see [Validity and limitations](04_validity-and-limits.md).

**Write it down:** List at least three alternative explanations for your central result. For each, write one sentence: how to check it, whether you have, and what you found. Keep the ones you can't check for your limitations section.

## 5. Negative and unexpected results

**When results fall short of expectations, don't jump to "this idea doesn't work". When results surprise you, don't celebrate yet, and don't throw them out either.**

**Negative results.** After a failed experiment it is easy to conclude "I tried X, and X doesn't work". But if X is an idea, the accurate statement is: I tried one specific implementation of X, and that implementation didn't work[^steinhardt2018stochastic-e10]. So after a failure, ask why, so you don't go on to try a string of approaches that will fail for the same reason[^steinhardt2018stochastic-e9]. If you have checked the code and the experiments and it still doesn't work, step back and debug the idea itself[^huang2023unstuck-e5].

Once you understand what happened, report negative results as they are. Deciding to test an idea means deciding to publish whatever the outcome; publishing only one kind of result makes the argument look better than it is[^feynman1974cargo-e9]. Not reporting non-significant or "uninteresting" results is called reporting bias, and it badly overestimates effects[^menzies2019bad-e1]. The software engineering empirical standards say explicitly that rejecting a study because it reports negative results is an invalid criticism[^ralph2020empirical-e41].

> **Where sources disagree: should a negative result be written up as its own paper?**
>
> - The European Code of Conduct for Research Integrity holds that negative results can be as important as positive ones for publication and dissemination[^allea2023european-e12].
> - A computer science researcher, writing about research methods, says he is more opposed than most to publishing negative results, unless they come with insight into why the approach failed[^steinhardt2018stochastic-e11].
>
> In practice `[Our analysis]`: where the two views agree is that **you can't hide** negative results relevant to your claim in a paper. Whether to write a negative result up as a paper of its own depends on whether you can explain why it failed. If you can, it is a valuable claim in its own right, for example "on contracts from after the training cutoff, the advantage of existing methods disappears".

**Unexpected results.** First go through Section 1 to rule out an error. If the result survives, take it seriously. The standards for process tracing in political science say to take the feeling of surprise seriously and work to explain surprising facts[^bennett2012process-e43]. An unexpected result may point to a more interesting question than the one you planned `[Our analysis]`. But because you found it after seeing the data, label it exploratory as in Section 2, and ideally confirm it once more on fresh data `[Our analysis]`.

**Write it down:** List every result that didn't match your expectations. For each: have you checked whether it is an error? What might cause it? How do you plan to report it?

## 6. How far your conclusions can reach

**The strength of a conclusion has to match the evidence.** A claim should follow clearly from the evidence you present; claims the evidence doesn't support mislead readers[^blackburn2018sigplan-e2].

The most common problem is overclaiming. A machine learning methods guide warns that working well on one dataset doesn't mean working well on others[^lones2021avoid-e10]. The software engineering empirical standards list overreaching conclusions or generalizations and downplaying a study's limitations as antipatterns, along with a subtler one: acknowledging limitations but writing the conclusions and implications as if they didn't exist[^ralph2020empirical-e66].

You can use the table below to line up what you say with the evidence you have `[Our analysis]`:

| Evidence you have | You can say | You can't say |
|---|---|---|
| One benchmark, one model | "On benchmark D, with model M, …" | "Large language models can …" |
| Correlation only, no controlled experiment | "Audits that used the prompt had higher detection rates" | "The prompt raised the detection rate" |
| A few successful examples | "It can find vulnerabilities that static analysis tools miss" | "It is better than static analysis tools" |
| An average improvement, but large differences across vulnerability types | "An average improvement of X, mostly from one type of vulnerability" | "An across-the-board improvement of X" |

How strongly to word a claim, and the evidence each wording needs, was covered in Section 1 of [Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove); at this stage you go back and check it against real evidence.

**Keep results and speculation apart.** The machine learning critique mentioned above points out that papers often dress speculation up as explanation, and readers take it as settled because it appears in a paper written by experts[^lipton2019troubling-e2]. The better the results, the easier it feels to add explanations with no evidence behind them[^lipton2019troubling-e15]. Good practice is to put speculation in a clearly labeled section of its own[^lipton2019troubling-e3], and in your writing to distinguish clearly between "the results show …" and "we speculate …" `[Our analysis]`.

**Report the facts that cut against you, and the real limitations.** When you propose an explanation, also write down the facts that don't fit it[^feynman1974cargo-e4]. Leaving out limitations, or listing only trivial ones while omitting the ones that actually matter, leads readers to overly strong conclusions[^blackburn2018sigplan-e3]. Also watch for "every sentence true, the whole misleading": each sentence can be accurate while the overall impression is false[^feynman1974cargo-e6]. The goal is to give all the information others need to judge the value of your work, not just the information that leads them one way[^feynman1974cargo-e5].

**Write it down:** Make a two-column table: on the left, each conclusion; on the right, the specific table, figure or experiment that supports it. Wherever the right side is empty, either add evidence or weaken the conclusion.

## 7. When the evidence doesn't match the claim, change the claim

**When the evidence doesn't support your original claim, change the claim, not the evidence.**

Common situations and how to revise `[Our analysis]`:

| Situation | Revision |
|---|---|
| The effect holds only under some conditions | Narrow the claim: restrict the data, the subjects, or the vulnerability types |
| The effect is much smaller than expected | Report its actual size and reconsider whether it is still worth writing up; it may fit better as a supporting claim |
| The effect comes from a cause you didn't anticipate | Make that cause the claim, label it exploratory as in Section 2, and design a test to confirm it |
| The original claim is refuted | The negative result itself may be the claim; or go back to the convergence stage and pick another |

When you are distilling your findings and discover things are more complicated than you thought, going back to rethink or even explore again is normal; it doesn't mean you've messed up[^nanda2025process-e6].

**Where the line is:** Revising the claim, running more experiments and narrowing the scope are all normal research. But quietly deleting unfavorable data or results to save the original claim crosses the line: changing, omitting or suppressing data or results without justification is falsification[^allea2023european-e3]. For what counts as research misconduct and how to correct your own mistakes once you find them, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md).

**Record every change to the claim**: the original claim, the new claim, and the evidence that prompted the change. You will use this record when writing the paper and when responding to reviews `[Our analysis]`. For how to keep such records, see [Organizing your materials](../08_throughout/organizing_materials.md).

**Write it down:** Take out your one-page project summary (see [Converging on a project](../01_find-a-problem/05_converge.md#6-write-a-one-page-project-summary-and-keep-revising-it)) and, checking it against the evidence you now have, rewrite the "central conclusion" field. It's fine if it stays the same, but you must be able to point to the evidence behind it.

---

## Judgment calls

**Can you trust this result?** A rough guide `[Our analysis]`:

| Situation | Usual approach |
|---|---|
| The result is surprisingly good | First check for errors as in Section 1, then for problems like the model having "seen" the data or duplicate data |
| The planned analysis isn't significant, but a different analysis is | Report both and label the second exploratory; don't report only the second |
| Significant, but the difference is tiny | Compare it with the "how big would matter" threshold you set in advance, and state honestly that the practical significance is limited |
| Not significant, with a wide confidence interval | Say "this data can't tell them apart", not "there is no difference" |
| An alternative explanation you can't check | Put it in the limitations and narrow the conclusion accordingly |
| The evidence refutes the central claim | First check for errors; once you're sure, revise the claim as in Section 7 |

**When is the analysis done?** Not when you "can't think of any more analyses", but when: all planned analyses are done and their results recorded; every conclusion can point to its evidence; the main alternative explanations have been checked or written into the limitations; and the claim has been revised to fit the evidence `[Our analysis]`.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Going straight to summary numbers without looking at the raw data | Many errors are silent, and the results still look usable[^karpathy2019recipe-e3] |
| Checking only when results are bad, not when they are good | Looking for errors in only one direction pulls results toward what you expected `[Our analysis]` |
| Trying analysis after analysis and reporting only the significant one | In the psychology simulations, the false-positive rate rose from 5% to 61%[^nelson2018psychology-e7] |
| Forming a hypothesis after seeing results and writing it up as if it came first | A recognized antipattern[^ralph2020empirical-e27] |
| Unplanned analyses with no label | Readers can't tell predictions from explanations after the fact[^nosek2018preregistration-e4] |
| Reporting only p-values | With large samples, trivial differences become significant[^lones2021avoid-e8] |
| Reporting only the best run | The difference may be just random variation[^georges2007statistically-e2] |
| Writing "not significant" as "no difference" | The data may simply not be enough to tell them apart `[Our analysis]` |
| Reporting only the "interesting" results | Reporting bias badly overestimates effects[^menzies2019bad-e1] |
| Concluding "this idea doesn't work" after one failure | It only shows that one implementation doesn't work[^steinhardt2018stochastic-e10] |
| Presenting speculation as explanation | Readers will take it as settled[^lipton2019troubling-e2] |
| Admitting limitations but leaving the conclusions unchanged | The limitations become meaningless[^ralph2020empirical-e66] |
| Quietly deleting unfavorable results to save the claim | That is falsification[^allea2023european-e3] |

## What you should have at the end

- A data-check log: what you checked, what you found, what you removed and why (Section 1)
- An analysis log: whether each analysis was planned or exploratory, and its result (Section 2)
- A statement of your central result: conditions, effect size, uncertainty, number of runs (Section 3)
- A list of alternative explanations and what checking each one showed (Section 4)
- A table matching each conclusion to its evidence (Section 6)
- An updated one-page project summary and a record of changes to the claim (Section 7)

## Checklist before moving on

You are ready to start writing when:

- [ ] You have looked at the raw data and outputs yourself, and checked for outliers, duplicates and parsing errors
- [ ] You checked the good results and the bad results equally hard
- [ ] Every planned analysis has its result reported; every unplanned one is labeled exploratory, with a reason for adding it
- [ ] Every key result has an effect size and its uncertainty, not just a p-value
- [ ] All runs are reported, along with the total number of comparisons made
- [ ] The main alternative explanations are listed and checked; the ones you couldn't check are in the limitations
- [ ] Negative and unexpected results have been investigated, and you plan to report them as they are
- [ ] Every conclusion can point to its evidence, and its wording is no stronger than the evidence
- [ ] The central conclusion in your one-page project summary has been updated to fit the evidence

## When to go back

| If this happens | Go back to |
|---|---|
| The data checks turn up a major problem and the results need to be rerun | [Running and iterating](06_run-and-iterate.md) |
| The data you have simply can't answer the research question | [From research questions to an evidence plan](01_question-to-evidence.md), to rethink what evidence you need |
| There is a fatal alternative explanation your current design can't rule out | [Validity and limitations](04_validity-and-limits.md), to add to the design |
| The central claim is refuted, and a narrowed version isn't interesting anymore | [Converging on a project](../01_find-a-problem/05_converge.md), to pick another candidate conclusion |
| Exploration turned up a more interesting question | [Converging on a project](../01_find-a-problem/05_converge.md), to treat it as a new candidate and discuss it with your advisor |

## Next

Once your conclusions and evidence line up, the next step is to tell them as a story and write the paper: what comes first, how to arrange the evidence, where the limitations go. See [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md).

[^allea2023european-e3]: ALLEA 2023, §3.1 Research Misconduct. [Evidence](../../sources/notes/allea2023european.md#e3)
[^allea2023european-e12]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e12)
[^aera2006standards-e8]: American Educational Research Association 2006, 5.10. [Evidence](../../sources/notes/aera2006standards.md#e8)
[^aera2006standards-e9]: American Educational Research Association 2006, 5.10. [Evidence](../../sources/notes/aera2006standards.md#e9)
[^appelbaum2018journal-e1]: Appelbaum et al. 2018, Abstract, p. 3. [Evidence](../../sources/notes/appelbaum2018journal.md#e1)
[^bennett2012process-e43]: Bennett & Checkel 2012, standard 8, p. 34. [Evidence](../../sources/notes/bennett2012process.md#e43)
[^blackburn2018sigplan-e2]: SIGPLAN checklist 2018, Clearly Stated Claims. [Evidence](../../sources/notes/blackburn2018sigplan.md#e2)
[^blackburn2018sigplan-e3]: SIGPLAN checklist 2018, Fails to acknowledge limitations. [Evidence](../../sources/notes/blackburn2018sigplan.md#e3)
[^blackburn2018sigplan-e7]: SIGPLAN checklist 2018, Insufficient number of trials. [Evidence](../../sources/notes/blackburn2018sigplan.md#e7)
[^blackburn2018sigplan-e9]: SIGPLAN checklist 2018, Misleading summary of results. [Evidence](../../sources/notes/blackburn2018sigplan.md#e9)
[^blackburn2018sigplan-e13]: SIGPLAN checklist 2018, Indirect or inappropriate proxy metric. [Evidence](../../sources/notes/blackburn2018sigplan.md#e13)
[^blackburn2018sigplan-e30]: SIGPLAN checklist 2018, Inappropriate level of precision. [Evidence](../../sources/notes/blackburn2018sigplan.md#e30)
[^egappreanalysis-e5]: Evidence in Governance and Politics (EGAP) methods guide, §9 Why make a PAP? [Evidence](../../sources/notes/egappreanalysis.md#e5)
[^feynman1974cargo-e4]: Feynman 1974, talk text, scientific integrity paragraph. [Evidence](../../sources/notes/feynman1974cargo.md#e4)
[^feynman1974cargo-e5]: Feynman 1974, talk text. [Evidence](../../sources/notes/feynman1974cargo.md#e5)
[^feynman1974cargo-e6]: Feynman 1974, Wesson Oil example. [Evidence](../../sources/notes/feynman1974cargo.md#e6)
[^feynman1974cargo-e7]: Feynman 1974, talk text. [Evidence](../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e9]: Feynman 1974, talk text. [Evidence](../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e11]: Feynman 1974, talk text, scientific integrity paragraph. [Evidence](../../sources/notes/feynman1974cargo.md#e11)
[^feynman1974cargo-e14]: Feynman 1974, talk text, Millikan example. [Evidence](../../sources/notes/feynman1974cargo.md#e14)
[^georges2007statistically-e2]: Georges et al. 2007, §1, discussion of Figure 1. [Evidence](../../sources/notes/georges2007statistically.md#e2)
[^herzig2013bug-e5]: Herzig et al. 2013, §XII. [Evidence](../../sources/notes/herzig2013bug.md#e5)
[^hopewell2025consortee-e18]: CONSORT 2025 explanation and elaboration, Item 16a. [Evidence](../../sources/notes/hopewell2025consortee.md#e18)
[^hopewell2025consortee-e49]: CONSORT 2025 explanation and elaboration, Item 21d. [Evidence](../../sources/notes/hopewell2025consortee.md#e49)
[^hopewell2025consortee-e52]: CONSORT 2025 explanation and elaboration, Item 26. [Evidence](../../sources/notes/hopewell2025consortee.md#e52)
[^huang2023unstuck-e5]: Jia-Bin Huang 2023, tweet thread, Debug the idea. [Evidence](../../sources/notes/huang2023unstuck.md#e5)
[^kalibera2013rigorous-e8]: Kalibera & Jones 2013, §4. [Evidence](../../sources/notes/kalibera2013rigorous.md#e8)
[^karpathy2019recipe-e3]: Karpathy 2019, "Neural net training fails silently". [Evidence](../../sources/notes/karpathy2019recipe.md#e3)
[^karpathy2019recipe-e7]: Karpathy 2019, Step 1 (Become one with the data). [Evidence](../../sources/notes/karpathy2019recipe.md#e7)
[^kraft2019interpreting-e13]: Kraft 2019, p. 17 (guideline 4). [Evidence](../../sources/notes/kraft2019interpreting.md#e13)
[^kraft2019interpreting-e21]: Kraft 2019, p. 26 (conclusion). [Evidence](../../sources/notes/kraft2019interpreting.md#e21)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019, §1, p. 1. [Evidence](../../sources/notes/lipton2019troubling.md#e1)
[^lipton2019troubling-e2]: Lipton & Steinhardt 2019, §3.1, p. 2. [Evidence](../../sources/notes/lipton2019troubling.md#e2)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019, §3.1, p. 3. [Evidence](../../sources/notes/lipton2019troubling.md#e3)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../sources/notes/lipton2019troubling.md#e7)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../sources/notes/lipton2019troubling.md#e8)
[^lipton2019troubling-e15]: Lipton & Steinhardt 2019, §4.1. [Evidence](../../sources/notes/lipton2019troubling.md#e15)
[^lones2021avoid-e7]: Lones 2021, §5.4, p. 22. [Evidence](../../sources/notes/lones2021avoid.md#e7)
[^lones2021avoid-e8]: Lones 2021, §6.4, p. 25. [Evidence](../../sources/notes/lones2021avoid.md#e8)
[^lones2021avoid-e10]: Lones 2021, §6.3, p. 24. [Evidence](../../sources/notes/lones2021avoid.md#e10)
[^lones2021avoid-e12]: Lones 2021, §5.4, p. 22. [Evidence](../../sources/notes/lones2021avoid.md#e12)
[^lones2021avoid-e19]: Lones 2021, §2.2. [Evidence](../../sources/notes/lones2021avoid.md#e19)
[^lones2021avoid-e20]: Lones 2021, §2.4. [Evidence](../../sources/notes/lones2021avoid.md#e20)
[^menzies2019bad-e1]: Menzies & Shepperd 2019, §4.4. [Evidence](../../sources/notes/menzies2019bad.md#e1)
[^menzies2019bad-e2]: Menzies & Shepperd 2019, §4.6. [Evidence](../../sources/notes/menzies2019bad.md#e2)
[^menzies2019bad-e3]: Menzies & Shepperd 2019, §4.6. [Evidence](../../sources/notes/menzies2019bad.md#e3)
[^nanda2025process-e6]: Nanda 2025, Distillation (Stage 4): Compress, Refine, Communicate. [Evidence](../../sources/notes/nanda2025process.md#e6)
[^nelson2018psychology-e6]: Nelson et al. 2018, P-Hacking Explains an Old Paradox, p. 514. [Evidence](../../sources/notes/nelson2018psychology.md#e6)
[^nelson2018psychology-e7]: Nelson et al. 2018, P-Hacking Explains an Old Paradox, p. 516. [Evidence](../../sources/notes/nelson2018psychology.md#e7)
[^nelson2018psychology-e8]: Nelson et al. 2018, False Positives Are Bad, p. 518. [Evidence](../../sources/notes/nelson2018psychology.md#e8)
[^nosek2018preregistration-e2]: Nosek et al. 2018, Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../sources/notes/nosek2018preregistration.md#e2)
[^nosek2018preregistration-e3]: Nosek et al. 2018, Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../sources/notes/nosek2018preregistration.md#e3)
[^nosek2018preregistration-e4]: Nosek et al. 2018, Preregistration Distinguishes Prediction and Postdiction. [Evidence](../../sources/notes/nosek2018preregistration.md#e4)
[^nosek2018preregistration-e5]: Nosek et al. 2018, Challenge 1. [Evidence](../../sources/notes/nosek2018preregistration.md#e5)
[^nosek2018preregistration-e6]: Nosek et al. 2018, Challenge 6. [Evidence](../../sources/notes/nosek2018preregistration.md#e6)
[^ofosu2023preanalysis-e1]: Ofosu & Posner 2023, Abstract. [Evidence](../../sources/notes/ofosu2023preanalysis.md#e1)
[^ofosu2023preanalysis-e7]: Ofosu & Posner 2023, Do PAPs Reduce the Scope for Fishing? [Evidence](../../sources/notes/ofosu2023preanalysis.md#e7)
[^ofosu2023preanalysis-e9]: Ofosu & Posner 2023, Do PAPs Reduce the Scope for Post-Hoc Hypothesis Adjustment? [Evidence](../../sources/notes/ofosu2023preanalysis.md#e9)
[^ofosu2023preanalysis-e10]: Ofosu & Posner 2023, Do PAPs Reduce the Scope for Post-Hoc Hypothesis Adjustment? [Evidence](../../sources/notes/ofosu2023preanalysis.md#e10)
[^ofosu2023preanalysis-e14]: Ofosu & Posner 2023, Objections to PAPs: Limit Flexibility and Scope for New Discoveries. [Evidence](../../sources/notes/ofosu2023preanalysis.md#e14)
[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e41]: ACM SIGSOFT Empirical Standards, General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e66]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e199]: ACM SIGSOFT Empirical Standards, Data Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e199)
[^steinhardt2018stochastic-e9]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e9)
[^steinhardt2018stochastic-e10]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e11]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e11)
[^zeller2021devil-e1]: Zeller 2021, THE CHERRY SHUFFLE. [Evidence](../../sources/notes/zeller2021devil.md#e1)
