# Causal explanation

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science. For how other fields do it, see the links in Section 5.

You have noticed something and want to know **why** it happens, or **whether changing some factor makes the outcome change too**. That is the research strategy we call causal explanation. Where it most often goes wrong is treating "two things occur together" as "one thing causes the other". This page covers what this kind of research has to show, what evidence is enough, which methods to use, and how it shapes your whole project.

---

## 1. What kind of knowledge this research produces

**It answers "Does X cause Y?" and "Why does this happen?"** For example, the central claim might be:

> "Giving a large language model vulnerability-pattern hints raises its detection rate for reentrancy vulnerabilities."

This sentence does not say "hints and detection rate are related". It says "**change the hints, and the detection rate changes with them**".

First be clear which kind of question you are asking. Relationship questions ask "Are X and Y related?" or "Does Y occur when X occurs?"[^easterbrook2008selecting-e35]; causal questions ask "Does X cause Y?" or "Does X prevent Y?"[^easterbrook2008selecting-e57]. Causal questions come in two finer forms as well: comparing which of two causes has the bigger effect ("Does X cause more Y than Z does?"), and asking how context changes a causal relationship[^easterbrook2008selecting-e58].

Examples from the same research area `[Our analysis]`:

| Question type | Example | Strategy |
|---|---|---|
| Relationship question | "Do large language models miss more vulnerabilities in longer contracts?" | Description |
| Causal question | "Does adding vulnerability-pattern hints raise the detection rate?" | Causal explanation |
| Which of two causes is bigger | "Which raises the detection rate more: vulnerability-pattern hints or a few worked examples?" | Causal explanation |
| How context changes the effect | "Do the hints help only on short contracts and not on long ones?" | Causal explanation |

**How it differs from neighboring strategies** `[Our analysis]`:

- **[Comparative evaluation](compare_evaluate.md)** asks "which is better, tool A or B?", treating each tool as a whole without asking what makes it better; **causal explanation** has to find out which factor did the work. The comparative evaluation page also discusses this line.
- **[Building and improving](build_improve.md)** has the central claim "the new method is better"; it often carries a causal supporting claim along with it: "the gain comes from component C". That supporting claim has to meet the standards on this page.
- **[Description](observe_describe.md)** can find that "projects using vulnerability-pattern hints have higher detection rates", but observation alone does not let you say the hints caused it (see Section 2).

**Two kinds of causal knowledge.** One is the **effect**: if you change X, how much does Y change? The other is the **mechanism**: through what process does X affect Y? They call for different evidence `[Our analysis]`. The case-study methods literature in political science points out that, other things being equal, case studies are better at shedding light on causal mechanisms and less able to estimate true causal effects[^gerring2004case-e4]. Work out first which kind your claim is.

**Write it down:** Write your central claim as "Under conditions C, changing X makes Y change in this way." Then add one sentence: are you trying to show the effect, the mechanism, or both?

## 2. What evidence is enough

**Correlation is not causation.** Mistaking a correlation for a cause is a common error, and showing causation is generally much harder than showing correlation[^easterbrook2008selecting-e36]. If X and Y rise together, X may cause Y, Y may cause X, both may have a common cause, or they may evolve together in some complex way[^easterbrook2008selecting-e56].

For example, suppose you find in public records that audits using vulnerability-pattern hints have higher detection rates. Maybe the hints helped; or maybe more experienced auditors are more likely to use hints, and what really matters is experience `[Our analysis]`.

**The software engineering standard: four things before you say "causes".** In its data science section, the empirical standards of ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) list this as an antipattern: claiming causation without establishing covariation and precedence, ruling out third-variable explanations, and at least hypothesizing a generative mechanism[^ralph2020empirical-e203]. This is a software engineering standard, but if you do causal research in other areas of computer science you can use it as a checklist too. Applied to the example `[Our analysis]`:

| What you need | Meaning | In the example |
|---|---|---|
| Covariation | When X changes, Y changes | The detection rate differs with and without hints |
| Precedence | X comes before Y | The hint is given before the model produces its output |
| Ruling out alternative explanations | It isn't caused by something else | It isn't because the prompt got longer, the model version changed, or the model had "seen" the contracts |
| A hypothesized mechanism | You can say how X affects Y | The hint makes the model check code that updates state only after an external call |

### The strongest approach: change X yourself

If you can, **change X yourself and keep everything else the same**, then see how Y changes. That is a controlled experiment. It can establish precisely how variables are related, in particular whether there is a causal relationship[^easterbrook2008selecting-e60]. The key is control: variables other than the independent variable (the factor you deliberately change) must not be allowed to affect the experiment[^easterbrook2008selecting-e61]. In software engineering experiments that evaluate tools with human participants, this means every participant gets exactly the same materials, instructions, tasks and environment, and only the tool differs; then, if the results differ, you can argue strongly that the tool caused it[^ko2015practical-e3].

When the subjects are people, or other units that can't be made identical, you also need **random assignment** `[Our analysis]`. The explanation and elaboration paper for CONSORT (Consolidated Standards of Reporting Trials), the reporting guideline for clinical trials in medicine, says that random allocation, done properly, eliminates selection bias in assigning participants to groups and balances both known and unknown prognostic factors across groups[^hopewell2025consortee-e1]. Quasi-experiments, which lack random assignment, are weaker than true experiments, and their results must be interpreted more cautiously[^easterbrook2008selecting-e64].

With large language models, "everything else the same" can be made very concrete `[Our analysis]`: the same model version, the same set of contracts, the same generation parameters, several runs per prompt; the only difference is whether the vulnerability-pattern hint is there.

### When you can't change X: first state what justifies a causal reading

Many factors you can't, or shouldn't, manipulate, such as a developer's experience or a policy. Then you have to use observational data, but you must **state explicitly what justifies a causal interpretation** `[Our analysis]`. Economics and epidemiology are the most concrete about this, and you can borrow from them:

- **Economics** talks about a "design-based" approach: use real experiments or natural experiments, and work hard to argue why the results can be read causally[^angrist2010credibility-e1]. For example, when you use an instrumental variable (a factor that affects Y only through X and whose value is as good as randomly assigned), you have to substantively justify the assumptions that make it valid, not just label variables[^angrist2010credibility-e5].
- **Epidemiology** talks about the **target trial**: causal inference from observational data can be seen as emulating a randomized trial that would answer the question[^hernan2016target-e1]. Epidemiology textbooks also stress that statistical association criteria alone can't tell you what is a confounder (a factor that affects both X and Y and can create a spurious effect); causal inference from observational data requires prior causal knowledge[^hernan2020whatif-e6][^hernan2020whatif-e7]. For confounders you don't know about, sensitivity analysis can estimate how much bias they might introduce[^hernan2020whatif-e11].

### Actively rule out alternative explanations

**List every plausible alternative explanation in advance, then look at which one the evidence supports.** The process tracing literature in political science names this failing: some case studies give their favorite explanation a "first mover advantage"; a far better procedure is to write out in advance what each explanation predicts you will see, then weigh the evidence for and against each one[^bennett2012process-e29]. The same work stresses that whether evidence can discriminate between rival explanations matters more than how much evidence there is[^bennett2012process-e9].

In the example, "hints raise the detection rate" has at least these rivals `[Our analysis]`:

| Alternative explanation | How to rule it out |
|---|---|
| The hint just makes the input longer | Add a condition with an unrelated hint of the same length |
| The model has seen these contracts, and the hint just jogs its memory | Repeat the experiment on contracts that appeared after the model's training cutoff |
| The hint makes the model more eager to report vulnerabilities, so false positives rise too | Report false positives as well, not just the detection rate |
| Pure chance | Run many times and report the variability |

### Test the mechanism

An effect alone leaves readers asking "why?". At minimum, hypothesize a mechanism[^ralph2020empirical-e203], and ideally test it. For example, if the hint really works by making the model check for "state updated only after an external call", then a hint about an **unrelated vulnerability type** should not raise the detection rate in the same way, and the model's explanations should mention this pattern `[Our analysis]`. The process tracing literature describes the central challenge in studying mechanisms as avoiding "lazy mechanism-based storytelling"[^bennett2012process-e50]; in practice, this means not just telling a plausible-sounding story about the process without testing it against evidence `[Our analysis]`.

### A common tool in computer science: ablation studies

An **ablation study** removes a method's components one at a time and watches how performance changes. It is "change one thing, keep everything else the same" applied inside a system `[Our analysis]`. In machine learning papers, proposing many changes at once without ablations makes it impossible to see where the gain comes from; sometimes only one of them really matters[^lipton2019troubling-e4]. So don't only ask "how well does it work?"; also ask "what made it work, and why?"[^lipton2019troubling-e7].

But ablations are neither necessary nor necessarily sufficient for understanding a method, and with limited compute they may not be possible at all[^lipton2019troubling-e6]. Also, an ablation only tells you what mattered on this benchmark, in this setup; it may not hold in a different setup `[Our analysis]`.

> **Where sources disagree: lab experiments or real projects?**
>
> The software engineering methods literature captures this disagreement as a debate: one side says the only sure way to show that A causes B is to vary A in a controlled setting and measure B; the other says lab experiments are useless because they ignore the complexity of real software projects[^easterbrook2008selecting-e59].
>
> - **The case for controlled experiments**: a controlled experiment can establish precisely whether variables are causally related[^easterbrook2008selecting-e60]; only when all other conditions are identical can a difference in results be strongly attributed to the factor you changed[^ko2015practical-e3].
> - **The case for real projects**: experiments break the problem into small pieces, and that simplification may hide important interactions; even when an experiment supports a hypothesis, it only shows that it holds for the measures you defined[^easterbrook2008selecting-e62]. When the setting itself shapes the phenomenon (for example, the pressure of a real project affecting developers' behavior), or when effects take weeks or months to appear, breaking things down and isolating them is not appropriate[^easterbrook2008selecting-e16].
>
> In practice `[Our analysis]`: run a controlled experiment if you can, but keep the scope of your claim in line with the experimental conditions; if the effect you care about depends on a real setting, add methods from Section 3 such as case studies or process tracing.

**Write it down:** For each of the four things above, write what evidence you plan to use to meet it. Then list at least three alternative explanations and how you will rule out each one.

## 3. Common research methods

A strategy says you need to show that X causes Y; a method says how you get the evidence. The table below chooses by whether you can change X `[Our analysis]`:

| Your situation | Methods you can use | How it provides causal evidence |
|---|---|---|
| You can change X, and the subject is a software system or model | Controlled experiments on the system and ablations; see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) and [Engineering research](../07_fields/computer-science/practices/engineering_research.md) | Change one thing, keep everything else identical, run many times |
| You can change X, and the subjects are people | [Controlled experiments](../06_methods/controlled_experiment.md) | Random assignment, so that only one factor differs |
| You can change X, and the subjects are cultured cells or extracted molecules | [Bench experiments](../06_methods/bench_experiment.md) | Change only one factor at a time, keeping the others constant[^vaux2012replicates-e6]; for confirmatory experiments, estimate the sample size and fix the primary outcome measure in advance[^perciedusert2020reporting-e13] |
| You can change X, the subjects are animals, and the conclusions are meant to inform human medicine | [Preclinical animal studies](../06_methods/preclinical_animal_study.md) | Show a causal relationship between treatment and effect in an animal model, then argue that it generalizes to patients[^henderson2013threats-e13] |
| Evaluating a medical intervention | [Randomized controlled trials](../06_methods/randomized_controlled_trial.md) | Random allocation, with group assignment and conduct reported according to medicine's reporting guidelines |
| You can work with a government or company to randomize in the real world | [Field experiments](../06_methods/field_experiment.md) | Random assignment within a program that is actually running |
| You can't randomize, but institutional rules or natural events create variation | [Quasi-experiments and causal identification](../06_methods/quasi_experiment.md) | Argue that variation in the treatment is "as good as random" |
| You only have observational data and care about causes of disease or effects of interventions | [Observational epidemiology](../06_methods/observational_epidemiology.md) | Specify the target trial and adjust for confounders |
| You only have observational data with locations, and care about how the environment or neighboring areas affect outcomes | [Spatial analysis](../07_fields/geography/practices/spatial_analysis.md) (geography practice) | Use regression models that account for spatial relationships; errors that cluster in space may mean you have left out a variable with a spatial pattern[^rey2023geographic-e17] |
| You want to understand how things happened in one or a few cases | [Process tracing](../06_methods/process_tracing.md), [case studies](../06_methods/case_study.md) | Test the mechanism step by step within the case |

A few notes:

- **Controlled experiments are good at "whether", not at "how" or "why".** Take tool evaluation in software engineering: questions about how developers use a tool, or what concepts they need to understand, are better suited to non-experimental quantitative or qualitative methods; and often you need those answers first to know what an experiment should compare, which tasks to use, and what to measure[^ko2015practical-e1].
- **Qualitative methods can speak to causation too; their strength is mechanisms.** Case studies give deep understanding of how and why a phenomenon happens, and can reveal the mechanisms behind causal relationships[^easterbrook2008selecting-e11]; for when to use them instead of experiments, see "Where sources disagree" above. Process tracing in political science analyzes the processes and sequences of events within a single case, in order to develop or test hypotheses about causal mechanisms[^bennett2012process-e3].
- **Why bench experiments, preclinical animal studies and spatial analysis are listed here** `[Our analysis]`. In the first two you change a factor yourself: bench experiments change only one factor at a time[^vaux2012replicates-e6]; the first goal of a preclinical animal study is to show a causal relationship between treatment and effect in an animal model[^henderson2013threats-e13]. Part of spatial analysis studies how the environment affects individuals, for example the effects of the social and physical environment on health[^kwan2012uncertain-e4]; that part belongs to causal explanation, while the part that describes spatial distributions belongs to [Description](observe_describe.md).
- **Methods can be combined.** You can pick a few cases out of a statistical analysis and use process tracing to check whether the causal direction is reversed or the correlation is spurious[^bennett2012process-e24]. Or you can do a quantitative study first and then use qualitative research to explain its unexpected results[^easterbrook2008selecting-e4]. For multi-method designs, see [Mixed methods](../06_methods/mixed_methods.md).

## 4. How it shapes the whole project

If you choose causal explanation, each stage gets a few extra tasks `[Our analysis]`:

| Stage | Extra tasks | See |
|---|---|---|
| Converging on a project | Phrase the claim as "under conditions C, changing X makes Y change in this way"; work out whether you can change X yourself | [Converging on a project](../01_from-interest-to-project/03_converge.md) |
| From question to evidence | For each of the four things, say what evidence you will use; list alternative explanations | [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md) |
| Choosing a method | If you can change X, run an experiment; if not, first write out the identification strategy or the target trial | [Choosing a strategy and a method](../02_from-project-to-study/02_choose-strategy-and-method.md) |
| Validity | The focus is internal validity: whether the results really follow from the data | [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md) |
| Pilot study | Try the part you are least sure of first, for example whether the hint's effect is big enough to detect | [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md) |
| Running the study | Record the model version, parameters and exact prompt text for every run; don't change conditions midway | [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md) |
| Analysis | Analyze according to the hypotheses you wrote in advance; don't try every possible analysis and pick the result you like | [Analysis and interpretation](../03_conduct-and-analyze/02_analyze-and-interpret.md) |
| Writing | State the conditions under which the causal claim holds; say which explanations you ruled out and which remain | [Telling the story and writing the paper](../04_write-and-publish/01_story-and-paper.md) |

The reasoning behind some of these:

- **Internal validity is the core criterion for this kind of research.** Internal validity is about whether the results really follow from the data; typical mistakes include failing to handle confounding variables properly and misusing statistical analysis[^easterbrook2008selecting-e65]. Conversely, studies that make no causal claims should not be judged on internal validity[^ralph2020empirical-e24].
- **Write the hypotheses first, then analyze.** Deriving hypotheses from theory and then analyzing according to them reduces "fishing for results": some correlations appear by chance, and if you search long enough you will always find one[^easterbrook2008selecting-e63]. Economics learned this the hard way: trying every regression specification and reporting only the last one[^angrist2010credibility-e12]; wide-net searches of this kind offer little basis for a causal interpretation[^angrist2010credibility-e13].
- **Say "causal" out loud, but state the scope.** The epidemiological methods literature explicitly argues against avoiding the word "causal": whether or not a study is randomized, causal inference is a core task of science[^hernan2018cword-e2]. At the same time, the scope of the claim must match the evidence: an experiment supports a hypothesis only for the measures and conditions you defined[^easterbrook2008selecting-e62].

## 5. Which fields use it

Below we list only the fields our sources support. If a field is missing, that doesn't mean it never uses this strategy; our sources just do not cover it.

| Field | What the sources say | Field conventions |
|---|---|---|
| Computer science | Software engineering often asks whether a tool or technique improves quality or speed[^easterbrook2008selecting-e57]; the strongest empirical papers in machine learning often include error analysis, ablation studies and robustness checks[^lipton2019troubling-e8] | [Computer science](../07_fields/computer-science/README.md) |
| Clinical medicine | A randomized trial that is appropriately designed, conducted, analyzed and reported is generally considered the highest-quality evidence for evaluating healthcare interventions[^hopewell2025consort-e2] | [Clinical medicine](../07_fields/clinical-medicine/README.md) |
| Epidemiology and public health | Take the effect of wine drinking on chronic disease: long-term randomized trials are considered unethical, so observational analyses become the best chance to estimate the long-term causal effect[^hernan2018cword-e11] | [Health sciences](../07_fields/health-sciences/README.md) |
| Economics | According to a 2010 review, design-based causal research is common in applied micro fields such as development, education, environmental, labor, health and public finance, but still rare in industrial organization and macroeconomics[^angrist2010credibility-e2] | [Economics](../07_fields/economics/README.md) |
| Political science | Of 195 pre-analysis plans (analysis plans registered publicly before the analysis begins) coded in one study, 63% came from field experiments and 27% from survey experiments[^ofosu2023preanalysis-e3]; the term "process tracing" was borrowed in 1979 by the political scientist Alexander George to mean using within-case evidence to infer historical explanations[^bennett2012process-e2] | [Political science](../07_fields/political-science/README.md) |
| Education | Some studies make causal inferences, for example estimating the effect of smaller class sizes on achievement[^aera2006standards-e4]; relationships found by early-stage exploratory research are usually correlational, not causal[^ies2013common-e3] | [Education](../07_fields/education/README.md) |

## 6. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Treating correlation as causation | A correlation can come from reverse causation, a common cause, and so on[^easterbrook2008selecting-e56] |
| Saying "causes" on the strength of covariation alone | You also need precedence, ruling out third variables, and a hypothesized mechanism[^ralph2020empirical-e203] |
| Changing several things at once with no ablation | You can't tell where the gain comes from; only one change may be doing the work[^lipton2019troubling-e4] |
| Testing only your favorite explanation | If the alternative explanations readers will think of immediately aren't addressed, the conclusion isn't convincing[^bennett2012process-e25] |
| Inventing a plausible mechanism without looking for evidence | The process tracing literature calls for avoiding "lazy mechanism-based storytelling"[^bennett2012process-e50] |
| Skipping random assignment and just saying "this study is exploratory" | That alone is not sufficient justification for not randomizing[^ralph2020empirical-e182] |
| Letting software automatically choose which variables to adjust for | Automatic variable selection may work for prediction, but not necessarily for causal inference[^hernan2018cword-e8] |
| Adjusting for variables affected by the treatment | As a rule, avoid adjusting for variables affected by the treatment or the outcome[^hernan2020whatif-e8] |
| Generalizing an experimental conclusion beyond the experimental conditions | An experiment supports a hypothesis only for the measures you defined[^easterbrook2008selecting-e62] |
| Forcing a causal claim when the evidence only supports correlation | Not making causal claims when you can't is not a weakness[^ralph2020empirical-e206] |

## 7. Further reading

- **Easterbrook et al. 2008, Selecting Empirical Methods for Software Engineering Research**: Section 2 covers the difference between relationship and causal questions; Section 5 compares what controlled experiments, case studies and other methods can each answer.
- **Ko, LaToza and Burnett 2015, A practical guide to controlled experiments of software engineering tools with human participants**: how to design a controlled experiment with human participants, step by step.
- **ACM SIGSOFT Empirical Standards**: the antipatterns in the experiments standard and the data science standard can serve as a checklist for causal claims.
- **Lipton and Steinhardt 2019, Troubling Trends in Machine Learning Scholarship**: why you should ask "what made it work", and what ablation studies can and can't do.
- **Hernán and Robins, Causal Inference: What If**: free on the authors' website; Section 3.6 covers target trials, and Chapters 7 to 9 cover confounding, selection bias and measurement bias.
- **Hernán 2018, The C-Word**: a short commentary on why causal questions should be stated plainly.
- **Angrist and Pischke 2010, The Credibility Revolution in Empirical Economics**: how economics turned to design-based causal research.
- **Bennett and Checkel 2012, Process Tracing**: the definition of process tracing, its four tests, and ten criteria for judging quality.

[^easterbrook2008selecting-e36]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e56]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e56)
[^easterbrook2008selecting-e35]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e57]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e57)
[^easterbrook2008selecting-e58]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e58)
[^easterbrook2008selecting-e59]: Easterbrook et al. 2008, §3.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e59)
[^easterbrook2008selecting-e60]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e60)
[^easterbrook2008selecting-e61]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e61)
[^easterbrook2008selecting-e62]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e62)
[^easterbrook2008selecting-e63]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e63)
[^easterbrook2008selecting-e64]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e64)
[^easterbrook2008selecting-e11]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e11)
[^easterbrook2008selecting-e16]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e16)
[^easterbrook2008selecting-e4]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e4)
[^easterbrook2008selecting-e65]: Easterbrook et al. 2008, §7.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e65)
[^ralph2020empirical-e24]: ACM SIGSOFT Empirical Standards, General Standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e182]: SIGSOFT Experiments (with human participants) standard, footnote 5. [Evidence](../../sources/notes/ralph2020empirical.md#e182)
[^ralph2020empirical-e203]: SIGSOFT Data Science standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e203)
[^ralph2020empirical-e206]: SIGSOFT Data Science standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e206)
[^ko2015practical-e1]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e1)
[^ko2015practical-e3]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e3)
[^hopewell2025consortee-e1]: CONSORT 2025 explanation and elaboration (Hopewell et al. 2025), Item 17a, Box 5 (Treatment allocation in trials). [Evidence](../../sources/notes/hopewell2025consortee.md#e1)
[^hopewell2025consort-e2]: CONSORT 2025 (Hopewell et al. 2025), Introduction, PDF p. 3. [Evidence](../../sources/notes/hopewell2025consort.md#e2)
[^angrist2010credibility-e1]: Angrist & Pischke 2010, Abstract. [Evidence](../../sources/notes/angrist2010credibility.md#e1)
[^angrist2010credibility-e2]: Angrist & Pischke 2010, Abstract. [Evidence](../../sources/notes/angrist2010credibility.md#e2)
[^angrist2010credibility-e5]: Angrist & Pischke 2010, Better Research Design. [Evidence](../../sources/notes/angrist2010credibility.md#e5)
[^angrist2010credibility-e12]: Angrist & Pischke 2010, The Leamer Critique and His Proposed Remedies. [Evidence](../../sources/notes/angrist2010credibility.md#e12)
[^angrist2010credibility-e13]: Angrist & Pischke 2010, Whither Sensitivity Analysis? [Evidence](../../sources/notes/angrist2010credibility.md#e13)
[^hernan2016target-e1]: Hernán & Robins 2016, Abstract. [Evidence](../../sources/notes/hernan2016target.md#e1)
[^hernan2018cword-e2]: Hernán 2018, beginning of the main text. [Evidence](../../sources/notes/hernan2018cword.md#e2)
[^hernan2018cword-e8]: Hernán 2018, Better confounding adjustment. [Evidence](../../sources/notes/hernan2018cword.md#e8)
[^hernan2018cword-e11]: Hernán 2018, Conflating the means and the ends. [Evidence](../../sources/notes/hernan2018cword.md#e11)
[^hernan2020whatif-e6]: Hernán & Robins, What If, §7.4. [Evidence](../../sources/notes/hernan2020whatif.md#e6)
[^hernan2020whatif-e7]: Hernán & Robins, What If, §7.4. [Evidence](../../sources/notes/hernan2020whatif.md#e7)
[^hernan2020whatif-e8]: Hernán & Robins, What If, §7.6. [Evidence](../../sources/notes/hernan2020whatif.md#e8)
[^hernan2020whatif-e11]: Hernán & Robins, What If, §7.3. [Evidence](../../sources/notes/hernan2020whatif.md#e11)
[^bennett2012process-e2]: Bennett & Checkel 2012, Defining Process Tracing, p. 7. [Evidence](../../sources/notes/bennett2012process.md#e2)
[^bennett2012process-e3]: Bennett & Checkel 2012, Defining Process Tracing, p. 10. [Evidence](../../sources/notes/bennett2012process.md#e3)
[^bennett2012process-e9]: Bennett & Checkel 2012, Bayesianism and Process Tracing, p. 19. [Evidence](../../sources/notes/bennett2012process.md#e9)
[^bennett2012process-e24]: Bennett & Checkel 2012, Techniques and Standards, p. 24. [Evidence](../../sources/notes/bennett2012process.md#e24)
[^bennett2012process-e25]: Bennett & Checkel 2012, Standards of Good Process Tracing, p. 26. [Evidence](../../sources/notes/bennett2012process.md#e25)
[^bennett2012process-e29]: Bennett & Checkel 2012, standard 2, p. 28. [Evidence](../../sources/notes/bennett2012process.md#e29)
[^bennett2012process-e50]: Bennett & Checkel 2012, Conclusion, p. 40. [Evidence](../../sources/notes/bennett2012process.md#e50)
[^gerring2004case-e4]: Gerring 2004, Causal Insight, p. 349. [Evidence](../../sources/notes/gerring2004case.md#e4)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019, §3.2, p. 3. [Evidence](../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e6]: Lipton & Steinhardt 2019, §3.2, p. 3. [Evidence](../../sources/notes/lipton2019troubling.md#e6)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../sources/notes/lipton2019troubling.md#e7)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../sources/notes/lipton2019troubling.md#e8)
[^ofosu2023preanalysis-e3]: Ofosu & Posner 2023, Empirical Approach. [Evidence](../../sources/notes/ofosu2023preanalysis.md#e3)
[^aera2006standards-e4]: AERA 2006, §2 Design and Logic. [Evidence](../../sources/notes/aera2006standards.md#e4)
[^ies2013common-e3]: IES & NSF 2013, Types of Research. [Evidence](../../sources/notes/ies2013common.md#e3)
[^vaux2012replicates-e6]: Vaux et al. 2012, Sidebar A. [Evidence](../../sources/notes/vaux2012replicates.md#e6)
[^perciedusert2020reporting-e13]: Percie du Sert et al. 2020 (ARRIVE 2.0 Explanation and Elaboration), Item 13. [Evidence](../../sources/notes/perciedusert2020reporting.md#e13)
[^henderson2013threats-e13]: Henderson et al. 2013, Introduction. [Evidence](../../sources/notes/henderson2013threats.md#e13)
[^rey2023geographic-e17]: Rey et al. 2023 (online textbook), Spatial Regression. [Evidence](../../sources/notes/rey2023geographic.md#e17)
[^kwan2012uncertain-e4]: Kwan 2012, p. 959. [Evidence](../../sources/notes/kwan2012uncertain.md#e4)
