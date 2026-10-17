# Validity and limitations: think them through at the design stage

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

## Where you are

You have a central claim, you know what evidence you need, and you have chosen a research strategy and a research method (see [Choosing a strategy and a method](02_choose-method.md)). You may also have an empty results table, rows and columns decided, waiting for numbers.

Say your claim is: "Giving a large language model hints about vulnerability patterns clearly raises its detection rate for reentrancy vulnerabilities." You plan to take a set of contracts, have the model check each one with hints and without hints, and compare the detection rates.

It looks like you can start. But stop for a moment: **if the experiment comes out exactly as you expect, what reasons will a reviewer give for saying "this doesn't prove your conclusion"?**

## What this stage is for

Before you run any experiment or send out any questionnaire, work out where your conclusion could be wrong, and close every gap you can in the design. Concretely, answer these questions:

1. Is what I measure really the thing I want to talk about?
2. If I see a difference, was it really caused by the factor I changed?
3. How far do my conclusions reach?
4. Are my data and analysis really enough to support the conclusion? Would someone else doing the study get the same result?
5. For the gaps I can't close, how will I report them honestly?

**Validity** is how far a conclusion can be trusted. A guide to case study research in software engineering defines it as the extent to which the results are true and not biased by the researchers' own subjective point of view[^runeson2009guidelines-e1]. This chapter covers the general framework every kind of study needs. The work specific to a given research strategy, such as choosing baselines, running ablation studies (removing parts of your method one at a time to see how the results change), keeping a held-out test set you only touch at the very end, repeated runs, and statistical tests, lives on the strategy and method pages; this chapter links to them where needed and does not repeat them `[Our analysis]`.

---

## 1. Assume the conclusion is wrong and list every possible reason

**How:** Imagine that a year from now someone publishes a paper showing your conclusion doesn't hold. What would they say? Write down every reason you can think of, as many as possible. Don't sort or judge them yet `[Our analysis]`.

Why do this? The first principle of research is that you must not fool yourself, and you are the easiest person to fool[^feynman1974cargo-e7]. Once the results come in, you will instinctively want to believe them. Right now, before there are results, is when you can look for flaws most dispassionately.

Why do it **now**? The case study guide warns that thinking about validity only at the analysis stage is too late; validity has to be considered at every earlier stage[^runeson2009guidelines-e2]. If you find out after the experiment that you measured the wrong thing or failed to control some factor, often the only fix is to run it again `[Our analysis]`.

Don't expect to find a perfect design, either. A software engineering research methods handbook puts it bluntly: all research designs are flawed[^easterbrook2008selecting-e69]. Your job is to know where the flaws are, fix the ones you can, and state clearly the ones you can't.

For the "hints raise detection rates" example, your list might include `[Our analysis]`:

- The contracts in the benchmark may already be in the model's training data, so the model has "memorized the answers";
- How is "detected" decided? Does the model saying "there may be a reentrancy risk" count?
- The hint group used a newer model version and the no-hint group an older one;
- You only tried one model and one contract language;
- The model's output varies from run to run, and with only one run the difference could be luck;
- You are the one judging "detected", and you hope the hint group does better.

**Write it down:** List at least eight reasons your central claim could be wrong. If you can't get to eight, ask a fellow student to play the pickiest reviewer and list them for you.

## 2. Sort the threats with four questions

Your list is a mix. Sort it by how each item threatens the conclusion, and you will know which kind of remedy each group needs.

**Threats to validity** are factors that could make your conclusion false. There is more than one way to classify them. The psychology measurement literature cites the four types from Shadish and colleagues: construct validity, internal validity, external validity, and statistical conclusion validity[^flake2020measurement-e16]. The software engineering research methods handbook uses four types too; the first three are the same, and the fourth is reliability instead[^easterbrook2008selecting-e68]. This chapter combines the two, matching the four questions at the top (question 4 covers the last two types) `[Our analysis]`:

| Type | In plain words | The matching threat in the example |
|---|---|---|
| **Construct validity** | Is what I measure really the concept I want to talk about?[^easterbrook2008selecting-e66] | The criterion for "detected" is vague; the model has memorized the answers rather than learned to detect |
| **Internal validity** | Was the difference I see really caused by the factor I changed?[^easterbrook2008selecting-e65] | The two groups used different model versions |
| **External validity** | Do my conclusions hold beyond what I studied?[^easterbrook2008selecting-e67] | Only one model and one contract language were tried |
| **Conclusion validity** | Is the conclusion drawn from the data and analysis itself correct?[^flake2020measurement-e16] | One run only, so the difference may be random variation |
| **Reliability** | If a different researcher redid the study, would the result be the same?[^easterbrook2008selecting-e68] | The person judging "detected" hopes one group does better |

What the table calls "conclusion validity" is "statistical conclusion validity" in the Shadish framework: whether the conclusions drawn from the statistical analysis are correct[^flake2020measurement-e16]. Studies without statistics face the same question: is your evidence really enough to support that sentence `[Our analysis]`?

**Not every type matters equally.** The empirical standards for software engineering state that there are no universal quality criteria; each study should be judged against the standards for the methods that suit it. For example, a study with no causal relationships should not be required to show internal validity[^ralph2020empirical-e24]. The standards also count criticizing a method for limitations that are inherent to it, such as criticizing a case study for limited generalizability, as an invalid criticism[^ralph2020empirical-e25].

So first look at which research strategy you are following, then decide where to put your effort `[Our analysis]`:

| Research strategy | Usually matters most | See |
|---|---|---|
| Description | External validity (whom the sample represents), construct validity (whether classifications and judgments are accurate) | [Description](../05_research-strategies/observe_describe.md) |
| Measurement | Construct validity | [Measurement](../05_research-strategies/measure.md) |
| Comparative evaluation | Construct validity (the metrics), conclusion validity (whether the difference is real), whether the comparison is fair | [Comparative evaluation](../05_research-strategies/compare_evaluate.md) |
| Causal explanation | Internal validity | [Causal explanation](../05_research-strategies/explain_causality.md) |
| Building and improving | Conclusion validity, external validity (does it still work on other data) | [Building and improving](../05_research-strategies/build_improve.md) |
| Synthesis | Whether the search and screening miss things or are biased | [Synthesis](../05_research-strategies/synthesize.md) |
| Proof | Whether the assumptions and definitions are close to reality | [Proof](../05_research-strategies/prove.md) |

**What about qualitative research?** Interviews, ethnography, and similar studies use a different vocabulary; see "Where sources disagree" at the end of this chapter.

**Write it down:** Label each reason from Section 1 with its type. Then check: is the type that matters most for your strategy the one with the fewest entries? If so, go back and add more.

## 3. Construct validity: are you measuring what you mean?

Your claim contains abstract concepts such as "detection rate", "vulnerability detection ability", or "code quality". An abstract concept a study wants to talk about is called a **construct**. You can't measure a construct directly with a ruler; you have to choose something concrete and countable to stand in for it. If the stand-in is poor, no amount of care later will save the study.

**How:**

1. **Define the construct in a sentence or two first.** If the construct is not defined clearly at the start, every later measurement decision becomes hard, and the vagueness leaves room to exploit it, knowingly or not[^flake2020measurement-e7]. Take "detected": must the model point to the exact function and line number, or is naming the vulnerability type enough?
2. **Write down the metric you use and why it represents the concept.** The evaluation checklist from the programming languages community requires that an indirect (proxy) metric may stand in for a direct one only if the reason is stated explicitly[^blackburn2018sigplan-e13]. A reporting checklist for machine learning also reminds you that the outcome being predicted is usually only a proxy for an unobservable theoretical construct[^kapoor2024reforms-e6].
3. **Prefer metrics others have validated; if you make up your own, at least explain why you didn't use an existing one.** When there is little validity evidence, put that in your limitations[^flake2020measurement-e13]. For how to make the measurement itself solid (reliability, multiple kinds of validity evidence, scale development), see [Measurement](../05_research-strategies/measure.md).
4. **Check a batch of labels by hand.** Labels taken automatically can be badly wrong. One study found that 33.8% of the bug reports it examined were misclassified: they corresponded not to code fixes but to new features, documentation updates, or internal refactoring[^herzig2013bug-e1]. The authors advise that before using a bug dataset, you manually validate a large enough sample and discuss data quality as a threat to validity[^herzig2013bug-e5].

**Common construct validity traps in computer science** `[Our analysis]`:

- **Using platform data to stand for an abstract concept.** GitHub data can be used directly to describe properties of projects, but drawing conclusions about more abstract concepts from it calls for caution[^kalliamvakou2014promises-e11], for example using star counts to stand for project quality.
- **The large language model has "seen" the benchmark.** If benchmark data got into the model's training data, the model's performance will be overestimated[^sainz2023nlp-e2]. What you measure may then be memory, not detection ability. When the benchmark itself has been used for training, the conclusions of the whole experiment are invalidated[^sainz2023nlp-e3]. For how to choose benchmark data to avoid this, see [Comparative evaluation](../05_research-strategies/compare_evaluate.md).

**Write it down:** List every key concept in your claim and define each in a sentence or two. Next to each, write the metric you plan to use, then one sentence on why it represents the concept. Wherever you can't write that sentence, you have a construct validity threat.

## 4. Internal validity: was it really the factor you changed?

**This section only matters much if your claim says "A causes B"**, for example "the hints raised the detection rate" or "the new method brought the improvement". If your study only describes a phenomenon, you can skip it `[Our analysis]`.

The software engineering research methods handbook describes internal validity as being about whether the results really follow from the data; typical mistakes are failing to handle confounding variables properly and misusing statistical analysis[^easterbrook2008selecting-e65]. A **confounding variable** is a third factor you haven't controlled that also affects the result: when you study whether A affects B, B may also be affected by a third factor[^runeson2009guidelines-e4].

**How:**

1. **List the alternative explanations.** For the result you expect, write down what else, besides your explanation, could produce the same result. When you run an experiment, you should report everything you think might make it invalid: the other possible causes, and which ones you ruled out and how[^feynman1974cargo-e11].
2. **For each alternative explanation, find a way to rule it out in the design** `[Our analysis]`: both groups use the same model version, the same parameters, and the same set of contracts; change one thing at a time (if the hint adds both vulnerability patterns and example code, you can't tell which one did the work); when you need groups, assign at random; when judging "detected", shuffle the outputs from both groups and hide which group each came from.
3. **Don't assume you are objective enough.** Good intentions are not enough: memory fails, and people reason toward what they want without noticing; these biases often operate outside awareness[^nosek2018preregistration-e3]. So guard against them through design, not self-discipline.

None of this is specific to computer science. In design guidelines for animal experiments, the most common recommendations for internal validity include random allocation and blinding the people who assess outcomes[^henderson2013threats-e9]; which confounders to guard against differs by field and by model[^henderson2013threats-e12]. For how to rule out alternative explanations systematically and when to run ablations, see [Causal explanation](../05_research-strategies/explain_causality.md#actively-rule-out-alternative-explanations), [Building and improving](../05_research-strategies/build_improve.md), and [Controlled experiments](../06_methods/controlled_experiment.md).

**Write it down:** For the central result you expect, write at least three alternative explanations, each with one sentence on how you plan to rule it out in the design. Mark the ones you can't rule out; you will need them in Section 7.

## 5. External validity: how far do your conclusions reach?

The software engineering research methods handbook describes external validity as being about whether claims that the results are general are justified, which often depends on how you sampled[^easterbrook2008selecting-e67].

**How:**

1. **Write down the target population first.** The target population is the group or data distribution you hope your conclusions extend to. The machine learning reporting checklist notes that papers don't always state it clearly[^kapoor2024reforms-e5]. Is your conclusion about "all Solidity contracts", "contracts deployed on Ethereum", or "contracts generated by large language models"?
2. **Compare your sample with the target population and note how they differ.** Examples `[Our analysis]`:
   - Your contracts come from a public vulnerability dataset; most are shorter than real contracts and have more textbook vulnerabilities;
   - You tried only one version of one model;
   - Your hints are written in English.
3. **For each difference, decide whether to widen the sample or narrow the claim.** If you can try more models and more datasets, do: researchers in animal studies also often address threats to external validity by reproducing an effect across several model systems[^henderson2013threats-e6]. If you can't, write the claim more narrowly. Claims of generality should match the strength of the evidence behind them[^henrich2010weirdest-e7].
4. **Give concrete reasons for your choice of sample.** Software engineering often recruits students as participants. That makes recruitment easy but lowers external validity, and you need to argue why results from students still apply to industry developers[^easterbrook2008selecting-e74]. The argument has to address the specifics of your study, not just say "students can represent developers"[^falessi2018empirical-e6].

**Two things that are easy to miss:**

- **More datasets does not mean closer to reality.** Running the same method on more data may improve generalizability, but it does not improve realism or give you more control over human factors[^storey2020who-e8]. If you care whether the tool helps developers in real use, adding datasets is not enough.
- **Conclusions expire.** Even if a model generalizes to the target population now, its performance may drop as the data distribution shifts over time[^kapoor2024reforms-e23]. Large language models are updated quickly, so record the model version and date behind every result `[Our analysis]`.

**Internal and external validity often trade off.** The software engineering methods literature points out that experiments must balance the two, and you can't maximize both at once[^falessi2018empirical-e3]; every research strategy has its own strengths and weaknesses in generalizability, realism, control, and precision, and every design decision is a trade-off[^storey2020who-e3]. The tighter you control conditions, the more it looks like a lab and the less like the real world. What you should do is decide, based on your claim, which matters more, and put the other in your limitations `[Our analysis]`.

**Write it down:** Write one sentence: "My conclusions apply to ____." Then another: "They do not necessarily apply to ____." List at least three items in the second.

## 6. Conclusion validity and reliability: is the data enough, and would someone else get the same result?

### Conclusion validity

Most of these threats show up at the analysis stage, but the rules have to be set at the design stage.

**How:**

1. **Decide in advance how you will analyze.** For experiments and surveys, decide which statistical tests you will use and plan ahead, so that analysis and interpretation go smoothly[^easterbrook2008selecting-e73]. Concretely, write down `[Our analysis]`: which groups you compare, which metric you look at, how big a difference counts as meaningful, and how many runs per group.
2. **Consider preregistration.** **Preregistration** means fixing your research questions and analysis plan before you see the results[^nosek2018preregistration-e1]. For what it constrains and what it doesn't, and where computer science stands, see [From research questions to an evidence plan](01_question-to-evidence.md).
3. **Know which practices are off-limits.** The empirical standards for software engineering list these two as antipatterns: forming hypotheses after seeing the results (HARKing) in a study presented as confirmatory, and reporting only the tests that came out significant[^ralph2020empirical-e27].

How many repetitions to run, how to report variation, and how to do statistical tests and effect sizes belong to the specific strategies and methods; see [Comparative evaluation](../05_research-strategies/compare_evaluate.md) and [Analysis and interpretation](07_analyze-and-interpret.md).

### Reliability

Reliability asks whether other researchers redoing the study would get the same result. Problems arise when researchers introduce bias, for example when the tool being evaluated is one the researchers have a stake in[^easterbrook2008selecting-e68]. **Evaluating a method you proposed yourself is exactly this situation** `[Our analysis]`.

**How:**

- **Write your judgment rules down and publish them.** The boundaries between categories may themselves be unclear; the bug report study mentioned earlier responded by publishing its full classification rules verbatim[^herzig2013bug-e4].
- **Wherever human judgment is needed, have two people judge independently.** The software engineering standard for inter-rater reliability requires describing how two or more raters rated independently and how disagreements were resolved, and reporting an appropriate agreement statistic[^ralph2020empirical-e129].

**Write it down:** Write an analysis plan of no more than one page: what you compare, which metric, how big a difference counts as meaningful, who makes any human judgments, and what rules they follow.

## 7. Decide how to handle each threat

You now have a sorted list of threats. For each one, choose one of three responses `[Our analysis]`:

- **Eliminate**: change the design so the threat no longer applies. For example, use the same model version for both groups.
- **Mitigate**: you can't remove it entirely, but you can check how much it matters. For example, check 100 samples by hand to estimate how many labels are wrong.
- **Acknowledge**: if you can't remove it, or doing so costs too much, put it in your limitations and narrow the claim to match.

Collect them in a table `[Our analysis]`:

| Threat | Type | How serious | How the design handles it | What remains afterward | In the limitations? |
|---|---|---|---|---|---|
| Benchmark contracts may be in the training data | Construct | High: could invalidate the conclusion | Add contracts that appeared only after the model's training cutoff | Can't be confirmed for models whose cutoff date is not public | Yes |
| Only one model tried | External | Medium | Add two more open-source models | Conclusions about closed-source models are uncertain | Yes |
| The judge knows which group an output came from | Reliability | Medium | Shuffle outputs, hide group labels, two people judge independently | Very little | No, but describe the procedure in the methods |

**How to judge "how serious":** Ask yourself: if this threat holds, how much of your central claim is left `[Our analysis]`? A threat that would invalidate the whole claim must be eliminated; one that only affects the scope can be handled by narrowing the claim and listing it in the limitations.

A few requirements:

- **List real threats, not filler.** The programming languages evaluation checklist criticizes the threats-to-validity sections of software engineering papers for often mentioning threats of little significance while ignoring the real ones[^blackburn2018sigplan-e10].
- **Say what you did.** The empirical standards for software engineering list "describes reasonable attempts to investigate or mitigate limitations" as a desirable attribute[^ralph2020empirical-e51]; their standard for experiments lists "validity threats are simply listed without linking them to results" as an antipattern[^ralph2020empirical-e52].
- **If a serious threat can't be eliminated, change the claim.** Go back to [Converging on a project](../01_find-a-problem/05_converge.md) rather than hoping reviewers won't notice `[Our analysis]`.

**Write it down:** Fill in the table above. At least one row should be rated "High", with a way of handling it you have already worked out. If no row is "High", you most likely haven't found the real threats yet.

## 8. Write your limitations now, and set rules for honest reporting

Limitations are not a paragraph you add after the paper is written. Writing them at the design stage tells you from the start how far your claim can go `[Our analysis]`.

**How:**

1. **Draft your limitations.** Turn the rows marked "In the limitations" in the last section's table into a few sentences. The empirical standards for software engineering require disclosing all major limitations[^ralph2020empirical-e18]. The machine learning reporting checklist also recommends stating the conditions under which the conclusions are not expected to hold; this helps readers form reasonable expectations and avoids hype[^kapoor2024reforms-e24].
2. **Rewrite the claim against the limitations.** The programming languages evaluation checklist warns that leaving out limitations, or listing only trivial ones, leads readers to draw conclusions that are too strong[^blackburn2018sigplan-e3]. One antipattern in the empirical standards for software engineering is acknowledging a limitation and then writing the conclusions as if it didn't exist[^ralph2020empirical-e66]. If your limitations say "only one model was tried", your claim can't say "large language models".
3. **Decide now to report the result whatever it is.** If you decide to test an idea, you should publish the result whichever way it comes out; publishing only one kind of result makes the argument look better than it is[^feynman1974cargo-e9].
4. **Be ready to record deviations.** Once you are doing the work, you will most likely change the plan. Record the original study protocol and every later deviation, so others can understand your design and interpret your results[^easterbrook2008selecting-e72]. For how to report deviations, see [From research questions to an evidence plan](01_question-to-evidence.md).

For why these are matters of research integrity, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md); for how to write limitations and unfavorable facts in a paper, see [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md).

**Write it down:** Write a three-to-five-sentence draft of your limitations, then one sentence with your revised central claim, made consistent with the limitations. Put "report the result whatever it is" and "record every deviation" into your research plan.

---

> **Where sources disagree: should qualitative research talk about "validity"?**
>
> The software engineering research methods handbook presents the validity types above as criteria for research that mainly tests hypotheses (positivist research)[^easterbrook2008selecting-e69]. Whether they should be applied to qualitative research such as interviews and ethnography is disputed:
>
> - **They should not.** Many researchers with a constructivist stance (the view that reality is constructed by people and differs across people and situations) consider the very concept of "validity" too positivist to capture the nature of qualitative research[^easterbrook2008selecting-e70]. The software engineering standard for grounded theory likewise says such studies should be judged on credibility, resonance, usefulness, and how far they extend existing knowledge, and that quantitative criteria such as internal validity and generalizability typically do not apply[^ralph2020empirical-e323].
> - **Validity still matters, but you build it during the research with specific strategies.** The same handbook summarizes this position and lists strategies for improving validity in this kind of research[^easterbrook2008selecting-e75], such as triangulating across different data sources, being honest about the biases you bring as a researcher[^easterbrook2008selecting-e71], going back to participants to check your interpretation (member checking), and reporting information that contradicts the emerging theory[^easterbrook2008selecting-e27].
>
> Both positions require you to guard against being led astray; they differ on vocabulary and on which criteria to judge by. In practice: first confirm which tradition your method belongs to, and list threats and responses by that tradition's standards. Qualitative researchers should do the exercise in Section 1 too, just using terms like credibility when sorting. For concrete steps, see [Interview studies](../06_methods/interview_study.md), [Grounded theory](../06_methods/grounded_theory.md), and [Case studies](../06_methods/case_study.md) `[Our analysis]`.

## Judgment calls

**Should this threat be closed off, or listed as a limitation?** One way to decide `[Our analysis]`:

| Situation | Usual response |
|---|---|
| If the threat holds, the whole central claim is invalid | Eliminate it in the design; if you can't, change the claim |
| It only affects the scope of the conclusions | Narrow the claim and list it in the limitations |
| It is a limitation inherent to the method you chose (e.g., the limited generalizability of a case study) | Just state it clearly; the empirical standards for software engineering consider criticizing a study for it invalid[^ralph2020empirical-e25] |
| Eliminating it would take longer than the whole project | Acknowledge it, and find a cheap way to estimate how big it is |
| You can't tell how serious it is | Try it out first in a [pilot study](05_pilot-and-derisk.md) |

**When have you thought about it enough?** Not when you "can't think of any more threats", but when: every threat of the type that matters most for your strategy has a response; all remaining threats are in your draft limitations; the claim has been rewritten to fit the limitations; and your advisor or a fellow student has looked over the threat list without pointing out a serious threat you missed.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Thinking about validity only after the experiment | Considering validity at the analysis stage is already too late[^runeson2009guidelines-e2] |
| Listing only trivial threats to validity | It dodges the real threats[^blackburn2018sigplan-e10], and readers will draw conclusions that are too strong[^blackburn2018sigplan-e3] |
| Listing threats without saying how they affect the results | The software engineering standard for experiments lists it as an antipattern[^ralph2020empirical-e52] |
| Using a proxy metric without explaining why it can stand in | What you measure may not be what you mean[^blackburn2018sigplan-e13] |
| Using ready-made labels without checking them by hand | Labels can be wrong in large numbers[^herzig2013bug-e1] |
| Not checking whether benchmark data was in the model's training data | Model performance will be overestimated[^sainz2023nlp-e2] |
| Holding your study to criteria that don't fit it | For example, chasing internal validity in a study with no causal relationships; the empirical standards for software engineering explicitly say not to do this[^ralph2020empirical-e24] |
| Admitting a limitation, then writing the conclusions as if it weren't there | The limitation section becomes an empty gesture[^ralph2020empirical-e66] |
| Trusting that you are objective enough, so skipping blinding and advance planning | Biases often operate outside awareness[^nosek2018preregistration-e3] |

## What you should have at the end

- A list of reasons your conclusion could be wrong, each labeled with its type (Sections 1 and 2)
- Definitions and metrics for the key concepts, with the reason each metric represents its concept (Section 3)
- (If your claim is causal) a list of alternative explanations and how you will rule them out (Section 4)
- The two sentences "applies to / does not necessarily apply to" (Section 5)
- A one-page analysis plan, including judgment rules (Section 6)
- The threat-handling table (Section 7)
- A draft of your limitations and the revised central claim (Section 8)

## Checklist before moving on

You can move on when all of these hold:

- [ ] You have listed at least eight reasons your conclusion could be wrong and sorted them by type
- [ ] You know which type of validity matters most for your research strategy, and every threat of that type has a response
- [ ] Every key concept has a definition, and for every metric you can say why it represents its concept
- [ ] You have written down the target population and can say how your sample differs from it
- [ ] The analysis plan was written before you saw any data, and wherever human judgment is needed there are written rules
- [ ] In the threat-handling table, every "High" threat has been eliminated or mitigated, or the claim has been narrowed to match
- [ ] Your draft limitations are written, and the central claim is consistent with them
- [ ] Your advisor or a fellow student has looked over the threat list without pointing out a serious threat you missed

## When to go back

| If this happens | Go back to |
|---|---|
| There is a threat that would invalidate the claim and you can't eliminate it no matter what | [Converging on a project](../01_find-a-problem/05_converge.md), Section 1: narrow the claim or pick another one |
| You can't find any metric that represents a key concept | [From research questions to an evidence plan](01_question-to-evidence.md): rethink what evidence you need |
| You find the method you chose can't rule out the main alternative explanations | [Choosing a strategy and a method](02_choose-method.md): switch to another method or strategy |
| Once rewritten to fit the limitations, the claim is too weak for anyone to care | [Converging on a project](../01_find-a-problem/05_converge.md), Section 2: decide again whether it is worth doing |

## Next

There will always be a few threats on your list whose seriousness you can't judge, such as "how much of the benchmark data was really in the training data" or "is agreement between the two judges high enough". Next, use the cheapest small experiments you can to test these least certain points first; see [Pilot first: rule out the biggest risks](05_pilot-and-derisk.md).

[^runeson2009guidelines-e1]: Runeson & Höst 2009, §5.2.3, p. 153. [Evidence](../../sources/notes/runeson2009guidelines.md#e1)
[^runeson2009guidelines-e2]: Runeson & Höst 2009, §5.2.3, p. 153. [Evidence](../../sources/notes/runeson2009guidelines.md#e2)
[^runeson2009guidelines-e4]: Runeson & Höst 2009, §5.2.3, Internal validity. [Evidence](../../sources/notes/runeson2009guidelines.md#e4)
[^feynman1974cargo-e7]: Feynman 1974, talk text, after the Millikan oil-drop experiment. [Evidence](../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e9]: Feynman 1974, talk text, publishing results. [Evidence](../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e11]: Feynman 1974, talk text, scientific integrity paragraph. [Evidence](../../sources/notes/feynman1974cargo.md#e11)
[^easterbrook2008selecting-e65]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e65)
[^easterbrook2008selecting-e66]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e66)
[^easterbrook2008selecting-e67]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e67)
[^easterbrook2008selecting-e68]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e68)
[^easterbrook2008selecting-e69]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e69)
[^easterbrook2008selecting-e70]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e70)
[^easterbrook2008selecting-e71]: Easterbrook et al. 2008, §7.0, strategies paraphrased from Creswell 2002. [Evidence](../../sources/notes/easterbrook2008selecting.md#e71)
[^easterbrook2008selecting-e27]: Easterbrook et al. 2008, §7.0, strategies paraphrased from Creswell 2002. [Evidence](../../sources/notes/easterbrook2008selecting.md#e27)
[^easterbrook2008selecting-e72]: Easterbrook et al. 2008, §7.0 Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e72)
[^easterbrook2008selecting-e73]: Easterbrook et al. 2008, §7.0 Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e73)
[^easterbrook2008selecting-e74]: Easterbrook et al. 2008, §5.1 Controlled Experiments. [Evidence](../../sources/notes/easterbrook2008selecting.md#e74)
[^easterbrook2008selecting-e75]: Easterbrook et al. 2008, §7.0 Empirical Validity. [Evidence](../../sources/notes/easterbrook2008selecting.md#e75)
[^flake2020measurement-e16]: Flake & Fried 2020, Questionable Measurement Practices, citing Shadish et al. 2002. [Evidence](../../sources/notes/flake2020measurement.md#e16)
[^flake2020measurement-e7]: Flake & Fried 2020, Question 1: What is your construct? [Evidence](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e13]: Flake & Fried 2020, Question 6: Do you create a measure on the fly? [Evidence](../../sources/notes/flake2020measurement.md#e13)
[^ralph2020empirical-e18]: ACM SIGSOFT Empirical Standards, General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e18)
[^ralph2020empirical-e24]: ACM SIGSOFT Empirical Standards, General Standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e25]: ACM SIGSOFT Empirical Standards, General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e51]: ACM SIGSOFT Empirical Standards, General Standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e51)
[^ralph2020empirical-e52]: ACM SIGSOFT Empirical Standards, Experiments standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e52)
[^ralph2020empirical-e66]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e129]: ACM SIGSOFT Empirical Standards, Inter-Rater Reliability and Agreement Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e323]: ACM SIGSOFT Empirical Standards, Grounded Theory standard, Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e323)
[^blackburn2018sigplan-e3]: SIGPLAN checklist 2018, Fails to acknowledge limitations. [Evidence](../../sources/notes/blackburn2018sigplan.md#e3)
[^blackburn2018sigplan-e10]: SIGPLAN checklist 2018, Notes. [Evidence](../../sources/notes/blackburn2018sigplan.md#e10)
[^blackburn2018sigplan-e13]: SIGPLAN checklist 2018, Indirect or inappropriate proxy metric. [Evidence](../../sources/notes/blackburn2018sigplan.md#e13)
[^kapoor2024reforms-e5]: Kapoor et al. 2024 (REFORMS), Module 1, 1a. [Evidence](../../sources/notes/kapoor2024reforms.md#e5)
[^kapoor2024reforms-e6]: Kapoor et al. 2024 (REFORMS), Module 3, 3d. [Evidence](../../sources/notes/kapoor2024reforms.md#e6)
[^kapoor2024reforms-e23]: Kapoor et al. 2024 (REFORMS), Module 8, 8a. [Evidence](../../sources/notes/kapoor2024reforms.md#e23)
[^kapoor2024reforms-e24]: Kapoor et al. 2024 (REFORMS), Module 8, 8b. [Evidence](../../sources/notes/kapoor2024reforms.md#e24)
[^herzig2013bug-e1]: Herzig, Just, Zeller 2013, Abstract. [Evidence](../../sources/notes/herzig2013bug.md#e1)
[^herzig2013bug-e4]: Herzig, Just, Zeller 2013, §XI Threats to Validity. [Evidence](../../sources/notes/herzig2013bug.md#e4)
[^herzig2013bug-e5]: Herzig, Just, Zeller 2013, §XII Conclusion and Consequences. [Evidence](../../sources/notes/herzig2013bug.md#e5)
[^kalliamvakou2014promises-e11]: Kalliamvakou et al. 2014, §6 Discussion & Conclusions. [Evidence](../../sources/notes/kalliamvakou2014promises.md#e11)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e3]: Sainz et al. 2023, §3 Defining data contamination. [Evidence](../../sources/notes/sainz2023nlp.md#e3)
[^henderson2013threats-e6]: Henderson et al. 2013, Introduction. [Evidence](../../sources/notes/henderson2013threats.md#e6)
[^henderson2013threats-e9]: Henderson et al. 2013, Editors' Summary. [Evidence](../../sources/notes/henderson2013threats.md#e9)
[^henderson2013threats-e12]: Henderson et al. 2013, Discussion. [Evidence](../../sources/notes/henderson2013threats.md#e12)
[^henrich2010weirdest-e7]: Henrich et al. 2010, §6.3 Recommendations. [Evidence](../../sources/notes/henrich2010weirdest.md#e7)
[^falessi2018empirical-e3]: Falessi et al. 2018, §4.1.2. [Evidence](../../sources/notes/falessi2018empirical.md#e3)
[^falessi2018empirical-e6]: Falessi et al. 2018, §6.2 Added statements, ST16. [Evidence](../../sources/notes/falessi2018empirical.md#e6)
[^storey2020who-e3]: Storey et al. 2020, §3.3. [Evidence](../../sources/notes/storey2020who.md#e3)
[^storey2020who-e8]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e8)
[^nosek2018preregistration-e1]: Nosek et al. 2018, Abstract. [Evidence](../../sources/notes/nosek2018preregistration.md#e1)
[^nosek2018preregistration-e3]: Nosek et al. 2018, Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../sources/notes/nosek2018preregistration.md#e3)
