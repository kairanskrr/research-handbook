# From research questions to an evidence plan

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. Sections 3, 5 and 6 are mainly for empirical research (research that reaches its conclusions by collecting data); each of those sections says so at the top.

## Where you are

You have a one-page project summary and a research plan (see [Converging on a project](../01_find-a-problem/05_converge.md) and [Writing a research plan](03_research-plan.md)). You can state your central claim in one sentence, you have sketched the empty results table, and every milestone is phrased as "what evidence will I have".

Then you sit down to start, and new questions appear:

- The claim says "inflated", "detected", "leaked". What exactly counts as each?
- When you count "one", is that one contract, one function, or one vulnerability?
- Once results come in, how big a gap counts as "inflated", and how small is just "about the same"?
- Should you fix a hypothesis first, or just run things and see?

If you don't settle these, then once the data is in you will find that every reading of it seems to make sense. And data that fits every reading proves nothing `[Our analysis]`.

## What this stage is for

Turn your central claim into an **evidence plan**: for each item, write down what you are asking, what you are measuring, on what, which result would support the claim and which would count against it. Concretely, answer these six questions:

1. Which answerable research questions does my central claim break into?
2. For each key term in the claim, what rule tells me how to measure or count it?
3. What exactly am I studying, and how far do I want my conclusions to reach?
4. What result counts as support, and what counts against? These must be written down before I look at the data.
5. Am I testing a claim I fixed in advance, or exploring?
6. Should I publish my plan in advance?

This chapter does not choose a method. Controlled experiment, questionnaire or repository mining is the next chapter's decision. Here you only pin down what you need to answer and what would count as an answer; that is what gives you grounds to choose a method `[Our analysis]`.

---

## 1. Break the claim into research questions

**Split the central claim into parts and write each part as a question.** One of the first steps in choosing a research method is getting clear about your research question[^easterbrook2008selecting-e31]. A well-reported study is also expected to state its research questions and explain why they matter[^ralph2020empirical-e22].

The [questions a reviewer would press you on](../01_find-a-problem/05_converge.md#4-what-will-make-people-believe-it) during convergence are usually your research questions in rough form. Take the claim "evaluation results for current large-language-model vulnerability detectors are inflated by data leakage" `[Our analysis]`:

| Research question | Type of question |
|---|---|
| RQ1 (research question 1): How many contracts in the commonly used benchmarks appear in the models' training data? | Base rate (how common) |
| RQ2: How much does the detection rate differ between leaked and non-leaked samples? | Relationship (are the two associated) |
| RQ3: Once leaked samples are removed, does the ranking of tools change? | Description (compare the rankings before and after) |

**Know which type each question is, because the type decides what evidence you need.** The classification below comes from a guide to research methods in software engineering[^easterbrook2008selecting-e32][^easterbrook2008selecting-e34][^easterbrook2008selecting-e35][^easterbrook2008selecting-e37][^easterbrook2008selecting-e39]. The question types themselves are not specific to software engineering; any empirical field can use them `[Our analysis]`:

| Type | What the question looks like | Smart-contract example `[Our analysis]` |
|---|---|---|
| Existence and description | Does X exist? What is X like? How can we measure it? | Is there leakage in the benchmark? |
| Base rate | How common is X, and how is it distributed? | What share of samples are leaked? |
| Relationship | Are X and Y related? | Do leaked contracts have higher detection rates? |
| Causality | Does X cause Y? | Is leakage the reason detection rates are high? |
| Design | What is an effective way to achieve X? | How do we build a benchmark that resists leakage? |

Two things to watch when you use this table:

- **Base-rate questions are often skipped.** If you don't know how common something normally is, you can't tell whether what you are looking at is normal or unusual[^easterbrook2008selecting-e34]. In the contract example, "how much leakage is there?" has to be answered before "how much does it matter?" means anything `[Our analysis]`.
- **Correlation is not causation.** Mistaking a correlation for a cause is a common error, and showing causation is usually much harder than showing correlation[^easterbrook2008selecting-e36]. RQ2 is a relationship question. If your claim says leakage **causes** the inflation, you need evidence for a causal question; see [Causal explanation](../05_research-strategies/explain_causality.md).

**Design questions rest on knowledge questions.** A design question assumes the related knowledge questions have already been answered, so that you understand the problem well enough[^easterbrook2008selecting-e40]. If you want to build a new benchmark, first find out what exactly is wrong with the old ones `[Our analysis]`.

**Write it down:** Break your central claim into two to four research questions and label each with its type. If a question's type doesn't match the wording of your claim (the claim says "causes" but the question can only show "is related to"), change one of them.

## 2. Give every key term an operational definition

**For every key term in your claim, write down exactly what you will look at and how you will count it.** This is an **operational definition**: it turns a concept into a measurement rule that someone could follow step by step `[Our analysis]`.

Why bother: what you actually measure has to really represent the concept you want to study[^runeson2009guidelines-e3]. Measurement research in psychology makes the same warning: if the construct is not defined clearly at the start, every later measurement decision becomes hard, and the vagueness leaves room to exploit it, knowingly or not[^flake2020measurement-e7].

In the contract example, go through the terms one by one `[Our analysis]`:

| Key term | What you have to decide | One possible definition |
|---|---|---|
| Leaked | Identical only, or similar enough? Where do you look? | After stripping comments and whitespace, the benchmark contract is identical to some contract in the training corpus |
| Detected | Is naming the vulnerability type enough, or must the tool point to the code? | The tool names the right vulnerability type and points to the function that contains it |
| Inflated | Compared with what? By how much? | The same tool's detection rate on non-leaked samples is more than 5 percentage points lower than on all samples |
| Large language model | Which models, which versions, queried when? | List the model names, version numbers and query dates |

**A term often has several reasonable definitions.** Pick one and write down why. If the choice matters a lot for the results, try one or two alternatives and see whether the conclusion changes `[Our analysis]`. Counting leakage as "identical" versus "highly similar" could give very different leakage rates; report both, so readers can see how robust your conclusion is.

**Don't let a convenient number stand in for a complex concept.** The empirical standards for software engineering list "unvalidated, uni-dimensional operationalizations of multidimensional constructs" as an antipattern, with "using github stars as a proxy for popularity" as the example[^ralph2020empirical-e119]. Using "number of tool warnings" as a proxy for "detection ability" fails for the same reason `[Our analysis]`.

**Same name doesn't mean same thing.** Two measures with similar names don't necessarily measure the same construct, and two measures with different names may measure the same one[^flake2020measurement-e8]. If another paper also reports a "detection rate", check that its definition matches yours before you compare numbers `[Our analysis]`.

How to check whether a measure is accurate and stable belongs to [Measurement](../05_research-strategies/measure.md). Here you only need to write the definitions down, and to do it before you see the data.

**Write it down:** List every key term in your claim and give each a one-sentence operational definition. For the term most likely to be disputed, write an alternative definition as well.

## 3. Decide what you are studying: unit of analysis and population

> This section is for studies that collect data from a set of things. If you are proving theorems or deriving theory, skip it. If you are synthesizing literature, your "things" are papers and the same logic applies.

**First: what is "one" when you count?** This is your **unit of analysis**. In software engineering research it might be a company, a project, a team, a developer, an event or a work product; choosing the right one keeps the study focused on the phenomenon you actually care about[^easterbrook2008selecting-e15]. Experience with software engineering surveys shows that with the wrong unit of analysis, the data you collect may be useless for your research question[^torchiano2017lessons-e5].

The contract example has at least three options, and each gives a different "detection rate" `[Our analysis]`:

| Unit of analysis | What "detection rate" means | What can go wrong |
|---|---|---|
| A contract | How many contracts are correctly judged vulnerable or not | A contract with five vulnerabilities where the tool finds one may still count as "detected" |
| A vulnerability | Of all known vulnerabilities, how many are found | Contracts with many vulnerabilities automatically carry more weight |
| A function | How many functions are correctly judged | Vulnerabilities that span functions are hard to count |

Which one to use depends on what your research question asks. "Can the tool help a developer who is handed a contract?" calls for contracts; "How many vulnerabilities can the tool find?" calls for vulnerabilities `[Our analysis]`.

**Next: who do you want your conclusions to apply to?** Separate three things: the **population** is everything you are interested in, the **sampling frame** is the list you can actually draw from, and the **sample** is what you end up studying; the sampling frame is usually imperfect[^ralph2020empirical-e42].

- In the contract example, the population might be "all contracts deployed on Ethereum"; the sampling frame might be "contracts with published source code", which only covers contracts whose owners chose to publish; the sample is the few thousand contracts you actually use `[Our analysis]`.
- If you are after representativeness, first state who, in principle, you want to generalize to[^baltes2022sampling-e11]. Representativeness is a relationship between a sample and a population, not a property that comes with a sampling technique[^baltes2022sampling-e3]; if the sampling frame is biased, no sample size will fix it[^baltes2022sampling-e5].
- Not aiming for representativeness is perfectly fine, for example when you are looking for unusual cases. Then state what your sampling is meant to achieve and explain why your approach is reasonable for that goal; it doesn't have to be optimal[^ralph2020empirical-e36]. Criticizing a study for lacking representativeness when it never aimed for it is not a valid criticism[^ralph2020empirical-e39].

**Justify your sample size.** In quantitative research the sample has to be large enough to detect an effect of the expected size; in qualitative research you need enough data to reach saturation (new data stops producing new findings)[^ralph2020empirical-e38]. How to estimate this depends on your method.

**Don't overstate how representative your sample is.** In particular, don't admit to sampling bias in your limitations section and then write your conclusion as if the results were near-universal[^baltes2022sampling-e9].

Sampling works differently for each method; see the method pages such as [Questionnaire surveys](../06_methods/questionnaire_survey.md#step-1-start-from-the-research-questions-define-the-population-unit-of-analysis-and-sampling-frame) and [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md#step-3-filter-and-sample-projects).

**Write it down:** One sentence each for your unit of analysis, population, sampling frame and sample. Then one more sentence: how does the sampling frame differ from the population, and which way might that difference push your conclusions?

## 4. Before you look at the data, decide what counts as support and what counts against

**Predict the results before you run the experiments or collect the data.** This helps you interpret the results and catch mistakes[^huang2023experiments-e3][^huang2023experiments-e4]. More importantly, it forces you to answer: **is there any result that would make you admit your claim is wrong?** If you could read any outcome as "support", the study can't prove anything `[Our analysis]`.

**How:** Fill in a table for each research question. It is a more detailed version of the ["what would show it failed"](03_research-plan.md#3-for-each-milestone-write-down-what-counts-as-done) entry for each milestone in your research plan, now broken down by research question `[Our analysis]`:

| Research question | My prediction | Counts as support | Counts against | If the result falls in between, I will write… |
|---|---|---|---|---|
| RQ1: leakage rate | 20–30% | Above 10% | Almost no leakage | Report the rate; change the claim to "some leakage exists" |
| RQ2: gap in detection rate | Leaked samples at least 10 percentage points higher | At least 5 percentage points, in the same direction across several tools | Under 2 percentage points, or directions disagree | Say only "may have an effect"; don't write "inflated" |

The numbers are only illustrations. What matters is that they are fixed before you see the data, and that you write down why you chose them `[Our analysis]`.

**Know which evidence can only rule things out and which can confirm.** Process tracing in political science (testing an explanation step by step against the sequence of events) distinguishes two kinds of test[^bennett2012process-e10][^bennett2012process-e12]:

- **Hoop test.** The classic example: "Was the accused in the state on the day of the murder?" If not, the explanation is eliminated; if so, that does not greatly raise your confidence in it.
- **Smoking-gun test.** Passing it is enough to strongly support an explanation; but it isn't required for building confidence, so failing to find a smoking gun doesn't show the explanation is wrong.

These come from political science; here we borrow them as a general way of thinking and apply them to the contract example `[Our analysis]`:

- "The benchmark does contain leaked samples" is a hoop test. Without leakage the claim collapses; with leakage, it still doesn't follow that results are inflated.
- "The model can reproduce benchmark contracts verbatim, and its detection rate on those contracts is clearly higher than on others" is closer to a smoking gun.

So "we found leakage" alone does not get you to "results are inflated". You need stronger evidence.

**"Statistically significant" is not the same as "a difference that matters".** When comparing randomized algorithms in software engineering (algorithms whose output can differ from run to run), the point is whether the new method has a practically meaningful advantage, measured by an effect size (how big the difference is) with its confidence interval[^arcuri2014hitchhiker-e6]. With thousands of runs, almost any difference becomes significant, so you must look at effect sizes as well[^arcuri2014hitchhiker-e9]. In your table, the "counts as support" criterion should say how big a difference, not just "significant" `[Our analysis]`.

**List the alternative explanations in advance.** Good empirical work considers and rules out alternative explanations[^lipton2019troubling-e1]. In the contract example, an obvious rival explanation is that leaked contracts may simply be older, simpler, or have more textbook vulnerabilities, so the higher detection rate may have nothing to do with the model having "seen" them `[Our analysis]`. That explanation gets its own row in the evidence plan: what evidence will rule it out, for example comparing leaked and non-leaked samples of similar difficulty.

**Aim the evidence at the claim.** If you claim better performance, analyze performance, not ease of use or generality[^shaw2003writing-e12]. Once the table is filled in, go back through it row by row: does the evidence in each row answer that row's question `[Our analysis]`?

**Write it down:** Fill in the table above for every research question. Then write at least one alternative explanation for your central claim and how you plan to rule it out.

## 5. Be clear whether you are testing or exploring

> This section is for studies that collect data.

Research can take two different stances:

- **Confirmatory research**: you have a clear hypothesis in advance and test it with data[^ralph2020empirical-e30].
- **Exploratory research**: you don't know in advance what you will find; the aim is to understand a phenomenon and generate ideas or hypotheses `[Our analysis]`.

Both are valuable. When a line of research is just starting, the first questions are usually exploratory[^easterbrook2008selecting-e32]; the data science section of the software engineering empirical standards also says that not every study needs statistical tests and hypotheses, and some studies can be purely descriptive[^ralph2020empirical-e202].

**The real problem is mixing the two without saying so.** In research presented as confirmatory, hypothesizing after the results are known (HARKing), or reporting only the statistical tests that came out significant (p-hacking), are antipatterns[^ralph2020empirical-e27]. Presenting an explanation you came up with afterwards as if it were a prediction is exactly HARKing[^nosek2018preregistration-e2]. It isn't necessarily deliberate: memory is fallible, and people reason toward the conclusions they want without noticing. These biases can operate outside awareness, so good intentions are not enough[^nosek2018preregistration-e3].

**How** `[Our analysis]`:

1. In your evidence plan, mark each research question "confirmatory" or "exploratory".
2. For confirmatory questions, write the hypothesis and the Section 4 table before you look at the data.
3. For exploratory questions, still write down what you plan to look at and how, but no prediction is needed.
4. When new ideas or extra analyses come up along the way, note them separately and report them as exploratory.

In computer science you can iterate freely on one small batch of data to understand the phenomenon, then test on a separate batch you haven't looked at `[Our analysis]`. That is exploration followed by confirmation, and it is fine as long as the two batches are kept apart and you say honestly which step was which.

**Write it down:** Mark each research question "confirmatory" or "exploratory". For the confirmatory ones, make sure the hypothesis is written down and dated before you saw the relevant data.

## 6. Should you publish your plan in advance?

> This section is for studies that collect data, and matters most for confirmatory research. The sources below come mainly from psychology (Nosek et al., Simmons et al.) and software engineering (the ACM SIGSOFT Empirical Standards).

**Preregistration** means fixing your research questions and analysis plan before you see the results[^nosek2018preregistration-e1]. The software engineering empirical standards are more specific: preregistration means publicly archiving the plan, to prevent hypothesizing after the results are known, reduce unconscious bias in data analysis, and counter publication bias[^ralph2020empirical-e29].

**It isn't meant to tie your hands.** Preregistration doesn't say that predictions made in advance are superior to exploration afterwards; it makes it possible to tell which is which[^nosek2018preregistration-e4]. It doesn't stop you from doing exploratory analyses; you can also preregister just your research questions and how you plan to answer them, and if the results don't match your predictions you can still publish[^simmons2018false-e2].

**How detailed should the plan be?** For Registered Reports, the software engineering empirical standards ask for enough detail that someone else could repeat your data collection and analysis exactly, and for hypotheses that can actually be tested with the data you plan to collect[^ralph2020empirical-e32]. What you wrote in Sections 1 to 5 is essentially the skeleton of that plan `[Our analysis]`.

**What if you have to deviate from the plan?** No study goes exactly to plan. A deviation is acceptable as long as there is a reason for it and it wasn't made after you knew how it would affect the results[^ralph2020empirical-e34]. Report honestly what changed and why; a preregistration with documented deviations is still far more credible than no preregistration[^nosek2018preregistration-e5]. Report the results of every analysis in the plan; otherwise you are still reporting selectively[^nosek2018preregistration-e6].

**A step further: Registered Reports.** Authors submit their research question and methods to a journal for review before they have results; at the second stage, reviewers don't judge whether the results are "important", only whether the study was done well and as planned[^nosek2018preregistration-e7].

**Where computer science stands.** The software engineering standard for experiments lists "pre-registration of hypotheses and design (where venue allows)" as a desirable attribute, not an essential one[^ralph2020empirical-e176]. Some software engineering venues already accept Registered Reports. According to Ernst and Baldassarre (2023), the first was the 2020 International Conference on Mining Software Repositories (MSR)[^ernst2023registered-e1]; the journal Empirical Software Engineering has supported the format since 2020, and the Association for Computing Machinery's journal Transactions on Software Engineering and Methodology (TOSEM) has run a similar "Registered Paper" program since 2022[^ernst2023registered-e2]. Empirical Software Engineering runs Stage 1 (review of the study plan) as a dedicated conference track; the options at the time were MSR, the International Conference on Software Maintenance and Evolution (ICSME), and the Empirical Software Engineering and Measurement conference (ESEM)[^ernst2023registered-e3]. Our sources do not cover whether venues in other areas of computer science accept them. Venue rules also change from year to year, so check your target venue's call for papers for the current year. Even without going public, keeping a dated copy of your plan in your repository does the job of keeping "planned in advance" and "added afterwards" apart for yourself `[Our analysis]`.

**Don't expect miracles from it either.** Preregistration doesn't prevent poor statistical practice, but it makes it detectable[^nosek2018preregistration-e8]; whether it improves replicability does not yet have enough empirical evidence behind it[^nosek2018preregistration-e9].

> **Where sources disagree: should exploratory research be preregistered?**
>
> - The Registered Reports section of the software engineering empirical standards says it applies to confirmatory, hypothesis-testing research; preregistering interpretivist (concerned with how people understand and make meaning), qualitative or exploratory research remains controversial[^ralph2020empirical-e30].
> - The same standard also lists "rejecting preregistration because the research is exploratory or qualitative" as an invalid criticism, holding that all kinds of research can be preregistered[^ralph2020empirical-e31].
>
> In practice `[Our analysis]`: confirmatory research should have a written plan in advance, and be preregistered if possible. Exploratory research doesn't have to be preregistered, but it is still best to write down before you start what you plan to look at and how; when you report, say honestly which analyses were planned and which were added after seeing the data.

**Write it down:** Decide whether your project will be preregistered, and write one sentence on why. Either way, combine what you produced in Sections 1 to 5 into a dated plan and store it in the project repository.

## 7. Put it together as an evidence plan

Combine the results of the previous sections into one table, one row per research question. This is the main thing this chapter produces `[Our analysis]`:

| Research question | Type | Operational definitions of key terms | Unit of analysis / population | Counts as support | Counts against | Alternative explanations to rule out | Confirmatory / exploratory |
|---|---|---|---|---|---|---|---|
| RQ1 | | | | | | | |
| RQ2 | | | | | | | |
| RQ3 | | | | | | | |

**How does this relate to the milestone list in your research plan?** The milestone list says which evidence you need and in what order; [what "done" means for each milestone](03_research-plan.md#3-for-each-milestone-write-down-what-counts-as-done) covers scope, criteria and what would show it failed. The evidence plan refines all of that to the point where it can be carried out and checked. Once it's written, go back and compare: every milestone should map to rows in the plan; where they don't match, change one of them `[Our analysis]`.

**Check it against the empty results table too.** For every cell of the [empty results table](../01_find-a-problem/05_converge.md#4-what-will-make-people-believe-it) you drew during convergence, the plan should tell you how that number will be produced. Any cell you can't trace is something you haven't thought through yet `[Our analysis]`.

**Write it down:** Fill in the evidence plan and show it to your advisor or a labmate. Ask them to pick a row and ask, "If this result came out, what would you write?" For any row you can't answer, go back to the relevant section and rewrite it.

---

## Judgment calls

**Strict or loose definitions?** Operational definitions often trade precision against feasibility. Some rules of thumb `[Our analysis]`:

| Situation | Usual approach |
|---|---|
| The data a strict definition needs is unavailable | Use a looser definition and state the limitation in the claim, e.g. "leakage, counting identical contracts only" |
| Two definitions are both reasonable and could give very different results | Use both and report both |
| The definition is so loose that almost anything counts | Tighten it; otherwise a "supporting" result means nothing |
| No definition lets you measure the concept | Go back to convergence and change the claim |

**Where to set the thresholds for support and against?** Ideally the threshold comes from whether your claim would matter, not from your guess about what the results will be. Ask yourself: how big a difference would make readers change what they do? For example, a 1-percentage-point difference in detection rate probably won't make a developer switch tools `[Our analysis]`.

**Too many questions?** Aim for two to four research questions per project at first. If your plan runs past ten rows, your central claim is probably not focused enough yet; go back and narrow it `[Our analysis]`.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Collecting data before the key terms have operational definitions | Every later measurement decision gets harder, and the vagueness leaves room to game the results[^flake2020measurement-e7] |
| Letting a ready-made number stand in for a complex concept | An unvalidated single measure can't capture a multidimensional concept[^ralph2020empirical-e119] |
| Not thinking through the unit of analysis | The data may turn out useless for the research question[^torchiano2017lessons-e5] |
| Writing criteria for support but not for refutation | If any result can be read as support, the study proves nothing `[Our analysis]` |
| Treating "we found leakage" as "we showed inflation" | That is only a hoop test: failing it rules an explanation out, passing it does not greatly raise confidence[^bennett2012process-e10] |
| Checking significance but not the size of the difference | With many runs, almost any difference is significant[^arcuri2014hitchhiker-e9] |
| The claim says "causes" but the evidence only shows "is related to" | Showing causation is much harder than showing correlation[^easterbrook2008selecting-e36] |
| Forming hypotheses after seeing results and reporting them as predictions | In research presented as confirmatory, this is an antipattern[^ralph2020empirical-e27] |
| Admitting sampling bias in the limitations but stating a general law in the conclusion | The conclusion goes beyond the evidence[^baltes2022sampling-e9] |

## What you should have at the end

- An evidence plan (Section 7): for each research question, its type, operational definitions, unit of analysis and population, criteria for support and refutation, alternative explanations to rule out, and whether it is confirmatory or exploratory
- A prediction table for each research question (Section 4)
- A dated plan, plus a publicly archived version if you decided to preregister (Section 6)

## Checklist before moving on

You are ready for the next step when:

- [ ] The central claim is broken into two to four research questions, each labeled with its type
- [ ] Every key term in the claim has an operational definition, with an alternative for any that are disputed
- [ ] You have written down the unit of analysis, population and sampling frame, and know how they differ
- [ ] Every research question has criteria for "counts as support" and "counts against", stated as how big a difference, not just "significant"
- [ ] You have written at least one alternative explanation and the evidence that will rule it out
- [ ] Every research question is marked confirmatory or exploratory; confirmatory hypotheses were written before looking at the data
- [ ] You have decided whether to preregister, and the plan is stored with a date
- [ ] The evidence plan lines up with the research plan's milestones and the empty results table

## When to go back

| If this happens | Go back to |
|---|---|
| No definition of a key term lets you measure it | [Converging on a project](../01_find-a-problem/05_converge.md), Section 1: rewrite the claim |
| While writing "counts against", you realize you could read any result as support | [Converging on a project](../01_find-a-problem/05_converge.md), Section 1: the claim may be too vague or too sweeping |
| You can't get the sample or data you need, and with a different sampling frame the conclusion is no longer interesting | [Converging on a project](../01_find-a-problem/05_converge.md), Section 5: reassess feasibility |
| The evidence plan and the milestones don't match, by a lot | [Writing a research plan](03_research-plan.md), Section 2: reorder the milestones |

## Next

With the evidence plan written, you know what evidence each question needs and what would count as an answer. The next step is deciding **how to get that evidence**: choosing a research strategy and a research method. See [Choosing a strategy and a method](02_choose-method.md).

[^easterbrook2008selecting-e15]: Easterbrook et al. 2008 (research methods in software engineering), §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e15)
[^easterbrook2008selecting-e31]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e31)
[^easterbrook2008selecting-e32]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e32)
[^easterbrook2008selecting-e34]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e34)
[^easterbrook2008selecting-e35]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e36]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e37]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e37)
[^easterbrook2008selecting-e39]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e39)
[^easterbrook2008selecting-e40]: Easterbrook et al. 2008 (research methods in software engineering), §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e40)
[^ralph2020empirical-e22]: ACM SIGSOFT (Association for Computing Machinery Special Interest Group on Software Engineering) Empirical Standards, General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e22)
[^ralph2020empirical-e27]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e29]: ACM SIGSOFT Empirical Standards, Registered Reports Supplement, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e29)
[^ralph2020empirical-e30]: ACM SIGSOFT Empirical Standards, Registered Reports Supplement, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e30)
[^ralph2020empirical-e31]: ACM SIGSOFT Empirical Standards, Registered Reports Supplement, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e31)
[^ralph2020empirical-e32]: ACM SIGSOFT Empirical Standards, Registered Reports Supplement, RR1 Specific Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e32)
[^ralph2020empirical-e34]: ACM SIGSOFT Empirical Standards, Registered Reports Supplement, Justifying Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e34)
[^ralph2020empirical-e36]: ACM SIGSOFT Empirical Standards, Sampling Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e36)
[^ralph2020empirical-e38]: ACM SIGSOFT Empirical Standards, Sampling Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e38)
[^ralph2020empirical-e39]: ACM SIGSOFT Empirical Standards, Sampling Supplement, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e39)
[^ralph2020empirical-e42]: ACM SIGSOFT Empirical Standards, Sampling Supplement, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e42)
[^ralph2020empirical-e119]: ACM SIGSOFT Empirical Standards, Repository Mining standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e119)
[^ralph2020empirical-e176]: ACM SIGSOFT Empirical Standards, Experiments standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e176)
[^ernst2023registered-e1]: Ernst & Baldassarre 2023, Abstract. [Evidence](../../sources/notes/ernst2023registered.md#e1)
[^ernst2023registered-e2]: Ernst & Baldassarre 2023, §2.1. [Evidence](../../sources/notes/ernst2023registered.md#e2)
[^ernst2023registered-e3]: Ernst & Baldassarre 2023, §3. [Evidence](../../sources/notes/ernst2023registered.md#e3)
[^ralph2020empirical-e202]: ACM SIGSOFT Empirical Standards, Data Science standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e202)
[^runeson2009guidelines-e3]: Runeson & Höst 2009 (case study research in software engineering), §5.2.3. [Evidence](../../sources/notes/runeson2009guidelines.md#e3)
[^flake2020measurement-e7]: Flake & Fried 2020 (psychology, measurement with scales), Question 1. [Evidence](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e8]: Flake & Fried 2020 (psychology, measurement with scales), Question 2. [Evidence](../../sources/notes/flake2020measurement.md#e8)
[^torchiano2017lessons-e5]: Torchiano et al. 2017 (software engineering surveys), §III-B-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e5)
[^baltes2022sampling-e3]: Baltes & Ralph 2022 (software engineering), §2.6. [Evidence](../../sources/notes/baltes2022sampling.md#e3)
[^baltes2022sampling-e5]: Baltes & Ralph 2022 (software engineering), §2.6. [Evidence](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e9]: Baltes & Ralph 2022 (software engineering), §6. [Evidence](../../sources/notes/baltes2022sampling.md#e9)
[^baltes2022sampling-e11]: Baltes & Ralph 2022 (software engineering), §6. [Evidence](../../sources/notes/baltes2022sampling.md#e11)
[^huang2023experiments-e3]: Jia-Bin Huang 2023 (advice from a computer vision researcher), Anticipate the results. [Evidence](../../sources/notes/huang2023experiments.md#e3)
[^huang2023experiments-e4]: Jia-Bin Huang 2023 (advice from a computer vision researcher), Anticipate the results. [Evidence](../../sources/notes/huang2023experiments.md#e4)
[^bennett2012process-e10]: Bennett & Checkel 2012 (political science, process tracing), p. 19. [Evidence](../../sources/notes/bennett2012process.md#e10)
[^bennett2012process-e12]: Bennett & Checkel 2012 (political science, process tracing), p. 20. [Evidence](../../sources/notes/bennett2012process.md#e12)
[^arcuri2014hitchhiker-e6]: Arcuri & Briand 2014 (software engineering, evaluating randomized algorithms), §4. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e6)
[^arcuri2014hitchhiker-e9]: Arcuri & Briand 2014 (software engineering, evaluating randomized algorithms), §8. [Evidence](../../sources/notes/arcuri2014hitchhiker.md#e9)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019 (machine learning), §1. [Evidence](../../sources/notes/lipton2019troubling.md#e1)
[^shaw2003writing-e12]: Shaw 2003 (software engineering), §4.3. [Evidence](../../sources/notes/shaw2003writing.md#e12)
[^nosek2018preregistration-e1]: Nosek et al. 2018 (open science debate in psychology and other fields), Abstract. [Evidence](../../sources/notes/nosek2018preregistration.md#e1)
[^nosek2018preregistration-e2]: Nosek et al. 2018 (open science debate in psychology and other fields), Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../sources/notes/nosek2018preregistration.md#e2)
[^nosek2018preregistration-e3]: Nosek et al. 2018 (open science debate in psychology and other fields), Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../sources/notes/nosek2018preregistration.md#e3)
[^nosek2018preregistration-e4]: Nosek et al. 2018 (open science debate in psychology and other fields), Preregistration Distinguishes Prediction and Postdiction. [Evidence](../../sources/notes/nosek2018preregistration.md#e4)
[^nosek2018preregistration-e5]: Nosek et al. 2018 (open science debate in psychology and other fields), Challenge 1. [Evidence](../../sources/notes/nosek2018preregistration.md#e5)
[^nosek2018preregistration-e6]: Nosek et al. 2018 (open science debate in psychology and other fields), Challenge 6. [Evidence](../../sources/notes/nosek2018preregistration.md#e6)
[^nosek2018preregistration-e7]: Nosek et al. 2018 (open science debate in psychology and other fields), Making Preregistration the Norm. [Evidence](../../sources/notes/nosek2018preregistration.md#e7)
[^nosek2018preregistration-e8]: Nosek et al. 2018 (open science debate in psychology and other fields), Challenge 2. [Evidence](../../sources/notes/nosek2018preregistration.md#e8)
[^nosek2018preregistration-e9]: Nosek et al. 2018 (open science debate in psychology and other fields), Preregistration Distinguishes Prediction and Postdiction. [Evidence](../../sources/notes/nosek2018preregistration.md#e9)
[^simmons2018false-e2]: Simmons, Nelson & Simonsohn 2018 (psychology), p. 258. [Evidence](../../sources/notes/simmons2018false.md#e2)
