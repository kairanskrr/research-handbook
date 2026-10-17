# Empirical studies with large language models: evaluating models, or using them as research tools

This page covers **empirical studies that involve large language models (LLMs)**. A large language model can play two parts in a study. It can be **the thing being studied**: you evaluate several models on the same task, or you evaluate a new tool built around one. Or it can be **a research tool**: you have it label data in place of human annotators, score other outputs, or stand in for participants in a survey or experiment. One study can use LLMs in both ways[^baltes2026guidelines-e1].

For the general evaluation workflow (choosing benchmarks, configuring systems fairly, measuring, analyzing), see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md). For studying how people use LLM tools, see [Controlled experiments](controlled_experiment.md). If you have built a new LLM-based tool and need to evaluate it for a whole paper, see [Engineering research](../07_fields/computer-science/practices/engineering_research.md). Statistical tests are covered in [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md), and validity in [Validity and limitations](../02_do-the-project/04_validity-and-limits.md). This page covers only the extra problems that LLMs bring.

**Scope**: This page draws mainly on software engineering sources: the guidelines for empirical studies involving LLMs in software engineering, written jointly by 22 researchers (Baltes et al., "the LLM guidelines" below), and Sallou et al.'s paper on threats to validity from LLMs. The evaluation parts also use the lessons of the developers of lm-eval, an evaluation framework from natural language processing (Biderman et al.), and a position paper on data contamination (Sainz et al.). The annotation parts use best practices from the social sciences (Törnberg). The LLM guidelines say explicitly that they target software engineering; medicine, human–computer interaction, and machine-learning-based science each have their own reporting guidelines for LLM work[^baltes2026guidelines-e35]. If you work in one of those fields, read your field's guidelines first.

**Strategies it usually serves**: [Measurement](../05_research-strategies/measure.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Building and improving](../05_research-strategies/build_improve.md).

**After reading this page, you should be able to:**

- tell whether the LLM in your study is the object being evaluated or a research tool, and decide what to report accordingly;
- record model versions, parameters, dates, and prompts so that others have a chance of reproducing your results;
- check for data contamination, prompt sensitivity, and run-to-run variation, so you don't mistake a lucky number for a finding;
- validate LLM-produced labels or scores against human judgment;
- check your own study with the checklist at the end.

---

## 1. What this kind of study is, and when to use it

The LLM guidelines classify studies by **the role the LLM plays in the research**, not by research method, and one study can fall into several categories[^baltes2026guidelines-e1]. We group them into two broad kinds:

| What the LLM is | Specific roles | Examples |
|---|---|---|
| A research tool | Annotator, judge, synthesizer, simulated participant | Qualitative coding of interview transcripts; rating the quality of software artifacts; summarizing papers; simulating human behavior[^baltes2026guidelines-e2] |
| The object of study | Tool under observation, component of a new tool, model under evaluation | Studying how engineers use LLMs; building a new tool that integrates an LLM; benchmarking LLMs on standard tasks[^baltes2026guidelines-e3] |

**Why this gets its own page.** LLMs add three headaches to empirical research: their output is non-deterministic, so each run gives different results; commercial models change even while the version name stays the same; and even models billed as "open" often don't release their training data[^baltes2026guidelines-e5]. As a result, many studies can't be reproduced. One survey looked at 85 LLM-centric papers from two top software engineering conferences in 2024. Of the 18 that used OpenAI models and provided research materials, only 5 could be run at all, and none fully reproduced the original results[^baltes2026guidelines-e4].

**Questions it is good at**:

- How well does a given LLM do on a given task, how much better is it than traditional methods, and is it worth the cost?
- Can published LLM evaluation results be trusted, or were they inflated by data contamination, for example?
- Can an LLM reliably do a research task in place of people, such as labeling or scoring?

**Questions it is not good at.** How people use LLMs in real work, and what effect LLMs have on people, need studies with human participants, such as [Controlled experiments](controlled_experiment.md), [Questionnaire surveys](questionnaire_survey.md), or [Interview studies](interview_study.md). There is also no convincing evidence yet that LLMs can accurately simulate human participants[^baltes2026guidelines-e27]. So results from LLMs acting as participants can't be taken directly as findings about people.

**How it differs from related methods**:

| | Empirical studies with LLMs (this page) | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | [Controlled experiments](controlled_experiment.md) | [Engineering research](../07_fields/computer-science/practices/engineering_research.md) |
|---|---|---|---|---|
| Focus | Problems specific to LLMs: versions, prompts, contamination, variation, validation against human judgment | The general evaluation workflow: choosing benchmarks, fair configuration, measurement, statistics | How people perform under some treatment | How to evaluate a new method or tool as a whole |
| Typical question | "Was this evaluation result inflated by contamination?" "Can LLM labels replace human ones?" | "Is tool A better than B?" | "Do people with an LLM assistant fix bugs faster?" | "Is my new tool better than existing ones?" |

Real projects often use several of these pages together: when you evaluate LLMs, follow the benchmarking page for the general workflow, then add the LLM-specific steps from this page.

**Example**: The running example, "Published evaluations of large language model vulnerability detectors are inflated by data leakage," is an empirical study with LLMs. The models are the objects being evaluated, and the study measures how much of their score on public benchmark contracts comes from having "seen" those contracts during training. If you also have another LLM extract "which vulnerability type was reported, and on which line" from each model's answer, that LLM becomes a research tool, and you have to declare it and validate it separately (see Step 7).

---

## 2. How to do it

The steps below add to the general workflow in [Benchmarking](../07_fields/computer-science/practices/benchmarking.md#2-how-to-do-it). The LLM guidelines split their requirements into two levels: a "must" is a hard requirement; a "should" strengthens a study's rigor or transparency, but there can be valid reasons to deviate in particular circumstances[^baltes2026guidelines-e6]. This page keeps that distinction.

### Step 1: State the role the LLM plays in your study

**How:**

- Say which LLM you used, how you used it, and at which point in the research process[^baltes2026guidelines-e7].
- If LLMs play several roles, declare each one separately: for example, one model generates evaluation data and another scores the outputs[^baltes2026guidelines-e7].

**Why:** Different roles raise different worries. For a model under evaluation, you worry about contamination and variation (Steps 4 and 6); for a model used as a tool, you need to validate it against human judgment (Step 7). Sort out the roles first, and every later step tells you which model it applies to.

**Where people go wrong:** Writing only "we used an LLM to assist with data processing," without saying which model or what it processed. Readers then can't judge how it might affect the results.

**Write it down:** A table with one row for every place an LLM is used: which model, what role, what goes in, and where the output is used.

### Step 2: Choose models, and record exact versions, parameters, and dates

**How:**

- **Justify your choice of model**[^tornberg2024best-e3]. When you are free to choose, add an open-weight model as a baseline alongside commercial ones, preferably an open-source model[^baltes2026guidelines-e23]. Open-weight models release their trained parameters, so others can deploy them; open-source models are better still, because you can also check whether your benchmark is in their training data[^baltes2026guidelines-e24].
- **Use one fixed version for the whole project**, record which version it is, and make sure the model will stay available[^tornberg2024best-e3].
- **The paper must state at least three things**: the exact model or tool name and version, all parameters that affect output generation, and the date the study was run. Defaults can change too, so report parameters even if you used the defaults[^baltes2026guidelines-e8][^tornberg2024best-e14]. The LLM guidelines give this example: "We integrated a gpt-4 model in version 0125-Preview via the Azure OpenAI Service, and configured it with a temperature of 0.7, top_p set to 0.8, a maximum token length of 512, and the seed value 23487. We ran our experiment on 10th January 2025. The system fingerprint was fp_6b68a8204b."[^baltes2026guidelines-e36]
- **Don't run experiments through the web chat interface**: you can't set parameters or control the version there, and privacy and copyright aren't protected[^tornberg2024best-e4].
- **When a commercial model doesn't give you all the information**, report what is available and openly acknowledge the limitations that hinder reproducibility[^baltes2026guidelines-e9].

**Why:** Commercial models change quietly. The models behind ChatGPT change without notice, so the same instruction gives different results; the fixed versions offered through the API are retired before long[^tornberg2024best-e2]. A study cited by Sallou et al. found that between March and June 2023, half of GPT-4's answers in code generation changed, and the share of directly executable outputs fell from 22% to 2%[^sallou2024breaking-e6]. When you build on earlier work, it becomes hard to tell whether an improvement comes from your new method or from changes in the model itself[^sallou2024breaking-e2]. Commercial models can also be retired or silently updated, while open models stay available[^baltes2026guidelines-e23].

**Where people go wrong:** Assuming that setting the temperature to 0 makes results reproducible. Even with a temperature (the parameter that controls how random the output is) of 0, full determinism is rarely guaranteed. Treat it as one measure among several, along with fixing the random seed, recording the system fingerprint, and archiving raw outputs[^baltes2026guidelines-e10].

**Write it down:** An experiment metadata file that records automatically, for every run: model name and version, access route, all parameters (including defaults), random seed, system fingerprint, and run date.

### Step 3: Design the prompts, and check how sensitive the results are to them

**How:**

- **State the prompting approach**: zero-shot (no examples, just the task), one-shot, or few-shot (a few examples), and how the examples were chosen. If you tried several versions of a prompt, say how you compared them and how you chose the final one[^baltes2026guidelines-e12].
- **Make clear which prompt goes with which model.** A prompt is tuned to the model it was developed on; on a different model, even one of similar size, results may differ[^tornberg2024best-e8]. So state which prompt was used with which model, in which version, and with which configuration[^baltes2026guidelines-e11].
- **Run a prompt stability analysis**: write several prompts that mean the same thing, run each on a subset of the data, and compare the results[^tornberg2024best-e15].
- **Specify the output format, and check whether failures come from the format.** Benchmark scores often mix the ability you want to measure with whether the model can produce the required format and follow instructions[^baltes2026guidelines-e37]. The lm-eval developers ran into this: a model performed close to random guessing under one prompt format, and looking at the outputs showed it simply wasn't answering in that format; under a different format it scored well[^biderman2024lessons-e11].

**Why:** The exact wording of a prompt, down to whitespace, can noticeably change performance. Switching between common prompting styles sometimes shifts results by more than 20%, and which style works best varies by model, so the prompt can change model rankings and the study's conclusions[^biderman2024lessons-e4]. Research cited by the LLM guidelines shows that prompt formatting alone can change accuracy by up to 76 percentage points[^baltes2026guidelines-e5]. Performance across prompt formats correlates only weakly between models, so comparing models with a single, arbitrarily chosen format is methodologically unsound[^baltes2026guidelines-e13].

**Where people go wrong:** Carefully tuning the prompt for your own method while giving the comparison models a prompt written in five minutes. Evaluators are already under pressure to pick flattering prompts[^biderman2024lessons-e2]; so part of the gap you measure this way comes from the prompts, not the method.

**Write it down:** A prompt change log: the full text of each prompt version, what changed and why, which models it was tried on, and how it did.

### Step 4: Check for data contamination

**Data contamination** means the evaluation data has leaked into the model's training data. The worst case is a model trained on a benchmark's test set and then evaluated on that same benchmark[^sainz2023nlp-e1]. Contamination overestimates a model's performance[^sainz2023nlp-e2]. For the general discussion, see the section [Is the benchmark itself valid?](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid) on the benchmarking page; this step adds what to do specifically in LLM studies.

The effect can be large. Sallou et al. found that ChatGPT knows the bugs in the Defects4J dataset intimately, so it performs better at repairing and localizing those bugs and generating tests for them than on code it hasn't seen[^sallou2024breaking-e1]. They also cite an example from unit test generation: an LLM reached over 69% branch coverage on HumanEval, a dataset hosted on GitHub, but only 2% on SF110, a dataset hosted on SourceForge[^sallou2024breaking-e3].

**How:**

- **Check the training data.** For models with public training data, check what share of the benchmark appears in it[^sainz2023nlp-e4]. For models without, check whether the model can reproduce benchmark items verbatim[^sainz2023nlp-e5].
- **Generate new items with metamorphic transformations.** Transform benchmark items so their meaning and behavior stay the same but their structure differs, and add the new items to the evaluation; which transformations to use depends on the task[^sallou2024breaking-e9]. Sallou et al. simply removed the documentation comments and renamed the method under test and its parameters: ChatGPT consistently reached 71% coverage on the original programs, but could barely generate meaningful tests for the transformed ones[^sallou2024breaking-e10].
- **Use data from after the model's training cutoff.** Build the benchmark only from data collected after a cutoff date, and report the data sources and collection dates. Newer models will eventually learn this data, though, so the benchmark needs regular updates[^baltes2026guidelines-e21].
- **Collect data from several sources**, and use code clone detection to check whether the code a model generates resembles code already online[^sallou2024breaking-e11].
- **When you fine-tune a model yourself**, splitting training and test sets by project is not enough: dependencies and APIs shared across projects can also cause leakage[^sallou2024breaking-e4].
- **When you build your own benchmark**, keep a held-out subset of items private for ongoing evaluation, and embed canary strings: unique markers you can later search for to detect whether the benchmark has made it into training data[^baltes2026guidelines-e20].

**Why:** LLM training data is opaque, so you must discuss possible data leakage and its effect on your results[^baltes2026guidelines-e31]. This step is often skipped: a survey of 572 code benchmarks found that 82.5% did not address data contamination[^baltes2026guidelines-e22].

**Where people go wrong:** Thinking contamination only happens before the evaluation. Evaluation items can also end up being used, unintentionally, to retrain the model, which matters especially for studies that span a long period[^baltes2026guidelines-e31].

> **Where sources disagree: is contamination always a problem when you use an LLM for annotation?**
>
> - The software engineering LLM guidelines require studies that use existing benchmarks to discuss contamination as a limitation[^baltes2026guidelines-e20].
> - Törnberg, writing for the social sciences, argues that for text annotation, the validation data appearing in the training data is not necessarily a problem, as long as the data you actually annotate appears there too; but don't use public, already-labeled datasets as validation sets, because the model may have seen the labels[^tornberg2024best-e16].
>
> In practice: it depends on what you are measuring. If you are measuring **the model's ability**, contamination directly inflates the score and you have to deal with it. If you are only **using the model to annotate**, what matters is how accurately it labels your real data, and the requirement is that the validation data and the real data are alike in whether the model has seen them.

**Example**: This step is the heart of the smart-contract project. Split the benchmark contracts into two groups: public contracts the model "may have seen," and contracts it "cannot have seen." The second group has two sources: contracts deployed after the model's training cutoff, and metamorphic rewrites of public contracts, such as renaming functions and variables, removing comments, and reordering unrelated statements. The difference in a model's detection rate between the two groups is where the "before and after removing leakage" column in the results table comes from. Note that the rewrites must not change the vulnerability itself, so check a sample of rewritten contracts by hand.

**Write it down:** A contamination check table: for each benchmark and each model, which check you used and what it showed; where you couldn't check, say why.

### Step 5: Choose baselines and metrics

**How:**

- **Add a traditional baseline.** Check whether a less resource-intensive traditional approach (static analysis, for example) can serve as a baseline. Even if the LLM does better, discuss whether the resources it consumes justify the (often marginal) improvement[^baltes2026guidelines-e15].
- **Add an open model as a baseline**; see Step 2[^baltes2026guidelines-e23].
- **Justify each metric**, beyond "earlier work used it"[^baltes2026guidelines-e18]. For classification and annotation, accuracy alone is often not enough, and it is especially misleading when classes are imbalanced[^tornberg2024best-e12].
- **Do an error analysis after the runs**: categorize the failures and report how common each category is[^baltes2026guidelines-e19]; find out why the model scores high or low[^biderman2024lessons-e12].

**Why:** People are almost never interested in the score on a particular benchmark for its own sake. A benchmark is a proxy for some ability that is hard to measure directly[^biderman2024lessons-e9]. A traditional baseline and an error analysis tell readers what ability the score actually reflects.

**Where people go wrong:** Comparing only against other LLMs. Ranking LLMs against each other says nothing about how much better LLMs are than traditional methods, or whether they are worth using.

**Example**: In the smart-contract project, existing static analysis tools can be the traditional baseline. They don't depend on training data and aren't affected by contamination, which makes them a good reference point: if the LLMs far outperform the static tools on contracts they "may have seen" but roughly match them on contracts they "cannot have seen," that in itself is evidence of inflation.

**Write it down:** Each baseline and each metric, with one sentence on why you chose it.

### Step 6: Repeat runs, and report the variation

**How:**

- **Repeat the experiment.** The same prompt run several times won't necessarily give the same result[^sallou2024breaking-e5]. So repeat experiments and report the mean, median, confidence intervals, and standard deviation[^baltes2026guidelines-e16].
- **Justify the number of repetitions**: do a power analysis, or add runs while watching whether the statistics stabilize; a pilot study helps you estimate how large the variation is[^baltes2026guidelines-e17]. For pilot studies in general, see [The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md).
- **When comparing models, use inferential statistics and effect sizes**, not just differences in means[^baltes2026guidelines-e16]. For the general approach, see [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).
- **Distinguish two kinds of variation**: how results change when you rerun the same items, and how they change with a different set of items, treating the benchmark items as a sample drawn from a larger population of possible items. Both are worth reporting[^biderman2024lessons-e13].

**Why:** Reporting the score from a single run versus a 95% confidence interval over 10 runs can lead to very different conclusions about which model is better; a small improvement claimed on a small benchmark may disappear if you simply resample under the same settings[^biderman2024lessons-e10]. In Sallou et al.'s demonstration, running the same set of prompts ten times gave a mean branch coverage of 70%, with an interquartile range (the spread of the middle half of the results) as large as 27.5%[^sallou2024breaking-e7]. Yet this step is often skipped: the same survey found that 64.0% of code benchmarks run only once and don't control for randomness[^baltes2026guidelines-e22].

**Where people go wrong:** Running several times and reporting only the best run. One of the pressures evaluators face is to report a single run's number and hide the uncertainty[^biderman2024lessons-e2].

**Write it down:** In the results table, give every number its run count and range, for example "10 runs, mean 0.62, 95% confidence interval 0.58–0.66."

### Step 7: When the LLM is a research tool, validate it against human judgment

When you use an LLM in place of people for annotation, coding, scoring, or as participants, you must justify that substitution[^baltes2026guidelines-e25]. LLM performance depends heavily on the data and the task, so it has to be validated task by task; validation is a basic requirement for every paper that uses LLMs for annotation[^tornberg2024best-e9].

**How** (taking annotation as the example, following Törnberg's workflow):

1. **Define the concepts first.** Write down explicitly the concepts you want to annotate, so you aren't led by the LLM's interpretation of them[^tornberg2024best-e5].
2. **Annotate a small sample with humans and the LLM together, and iterate.** Have people and the LLM label the same items, discuss disagreements, and revise the codebook (the instructions for deciding each category) and the prompt until the LLM agrees with the humans well enough. Ideally, the LLM should come close to the level of agreement between humans[^tornberg2024best-e6].
3. **Once the prompt is final, test it on a separate validation set.** Don't use validation data to tune the prompt, or you will overstate accuracy[^tornberg2024best-e10]. The validation set needs at least 20–30 items per category, and more is better[^tornberg2024best-e11].
4. **Validate by subgroup, and examine the failures.** Validate separately on subsets where the model's ability may differ (different languages, for example); examine the failed items, and explain why the model's weaknesses don't affect your downstream conclusions[^tornberg2024best-e13].

Agreement is commonly measured with Krippendorff's alpha (1 means perfect agreement). By Krippendorff's standard, data with alpha below 0.667 should be discarded, 0.667 to 0.8 supports only tentative conclusions, and only 0.8 or above counts as reliable[^baltes2026guidelines-e26].

**When the LLM is a judge** (scoring outputs): for subjective judgments, have the LLM and a panel of human experts each rate the same items independently, then compare the LLM's ratings with the aggregated human ratings. Both humans and LLMs show systematic biases as judges, such as favoring answers with fake citations or elaborate formatting[^baltes2026guidelines-e38].

**Why:** Several models agreeing with each other may just mean they share the same biases, so check a sample against human experts[^baltes2026guidelines-e25]. Reliability is not validity: an LLM can consistently give the same wrong answer every time[^baltes2026guidelines-e28].

**Where people go wrong:** Treating human annotations as ground truth. Human labels aren't a gold standard either; sometimes the LLM's reading is actually better[^tornberg2024best-e7]. When humans and the model disagree, go back to the concept definitions to decide, instead of assuming the humans are right.

> **Where sources disagree: can LLMs do qualitative analysis?**
>
> - The LLM guidelines mention an open letter in which 419 experienced qualitative researchers argued that methods such as reflexive thematic analysis require a positioned, reflexive researcher, and that using generative AI for this kind of analysis is methodologically incompatible with them[^baltes2026guidelines-e29]. The guidelines' own view is that LLMs may be better suited to assisting researchers than to replacing them[^baltes2026guidelines-e27].
> - Törnberg argues against rejecting LLMs outright, and for bringing them into a rigorous annotation workflow that keeps their weaknesses in check; the criticisms that LLMs are subjective, flawed, black boxes, and potentially biased often apply equally to human coders[^tornberg2024best-e18].
>
> In practice: the two views are about different tasks. Labeling against explicit categories (for example, "is this comment reporting a bug?") can be handed to an LLM after validation through the workflow above. Qualitative analysis that requires the researcher's own interpretation (see [Interview studies](interview_study.md) and [Grounded theory](grounded_theory.md)) can use an LLM as an assistant at most; people remain responsible for the conclusions, and the paper should say what the LLM did.

**Example**: In the smart-contract project, each model's answer is a passage of text. If you use another LLM to extract "which vulnerability type was reported, and on which line," first have two people each annotate a batch of answers independently, compare human–human and human–model agreement, and revise the extraction prompt. Once it is final, validate it on a different batch of answers, with at least a few dozen items per vulnerability type, and apply it to all the answers only once it meets the bar.

**Write it down:** A codebook: concept definitions, the decision rules and examples for each category, and the prompt and parameters given to the LLM; plus a table recording the agreement coefficient for each round.

### Step 8: Work out the costs

**How:**

- Record how many tokens (the basic units of text a model processes) you used, how much you spent on API fees, or what hardware you used[^baltes2026guidelines-e32].
- Compared with traditional methods, show that the resources the LLM consumes are justified[^baltes2026guidelines-e32].

**Why:** Cost is both a strength and a limitation of LLMs. LLMs annotate and judge faster and more cheaply than people: in one example, annotation with GPT-4 took two days and cost $122.08, while a comparable crowdsourcing process took weeks and cost $4,508[^baltes2026guidelines-e34]. On the other hand, running full evaluations through commercial APIs is expensive, and the cost falls mostly on independent researchers[^biderman2024lessons-e3].

**Where people go wrong:** Budgeting for a single run. Number of models × prompt versions × repetitions × items quickly multiplies the cost dozens of times over; measure the cost of one complete run in a pilot first, then decide on the number of repetitions and models.

**Write it down:** A budget table: tokens and cost per complete run for each model, multiplied by the number of runs you plan.

### Step 9: Release your materials, and state the limitations

**How:**

- **Release all prompts**[^baltes2026guidelines-e11]. Releasing the complete prompts is necessary for full reproducibility but not sufficient[^biderman2024lessons-e6]: release the exact evaluation code if you can, and state how much prompt tuning you did and on which models and benchmarks, the generation parameters, and the rules for extracting answers from responses[^biderman2024lessons-e7].
- **Release the interaction logs**, that is, the prompts sent and the responses received[^baltes2026guidelines-e14]. Save every item's score and model output, so results can be rechecked later without spending compute on a rerun[^biderman2024lessons-e8]. Also release the query dates, to account for output drift over time[^sallou2024breaking-e8].
- **State the limitations.** You must discuss what you did to improve reliability and reproducibility[^baltes2026guidelines-e33], and you must discuss possible data leakage[^baltes2026guidelines-e31]. Ways to mitigate threats to external validity include triangulating across multiple models, independent datasets, and complementary metrics; running sensitivity analyses by varying configurations, prompts, and datasets; and rerunning after some time has passed[^baltes2026guidelines-e30].
- **Protect sensitive data.** Anonymize personal information before sending data to an LLM hosted on a platform; don't send proprietary or confidential data to an API or web interface without carefully considering the ethical and legal issues[^tornberg2024best-e17]. For general ethics requirements, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md).

**Why:** Unlike transcripts of human interviews, LLM interaction logs can be published, which helps others reproduce your work, track how models change over time, and do secondary studies[^baltes2026guidelines-e14]. Results that can't be reproduced word for word are not in themselves a reason to reject a study[^baltes2026guidelines-e33]; we would add that this assumes you released everything you could, so others can check what you did.

**Where people go wrong:** Writing only "LLM outputs are non-deterministic" in the limitations, without saying what you did about it or how it affects your conclusions. Explain the effect of each threat to validity one by one; see [Validity and limitations](../02_do-the-project/04_validity-and-limits.md).

**Write it down:** A list of research materials: the full prompts and change log, experiment metadata, evaluation code, interaction logs and raw outputs, human annotation data and the codebook, with where each is stored and under what license it is released.

---

## 3. Checklist

"Must do" and "Better practice" below correspond to the "must" and "should" levels of the LLM guidelines[^baltes2026guidelines-e6]. The "Outstanding" tier, and items drawn from other sources, are this handbook's own synthesis; the LLM guidelines target software engineering, so in other fields your field's conventions take precedence.

**Must do**

- [ ] Declare which LLM you used, how, and at which point; declare each role separately[^baltes2026guidelines-e7]
- [ ] State the exact model or tool name and version, all parameters that affect output, and the date of the study[^baltes2026guidelines-e8]
- [ ] Release all prompts, and make clear which was used with which model, version, and configuration[^baltes2026guidelines-e11]
- [ ] State whether prompting was zero-shot or few-shot, and how examples were chosen[^baltes2026guidelines-e12]
- [ ] Explain why each metric is appropriate, beyond "earlier work used it"[^baltes2026guidelines-e18]
- [ ] Discuss possible data leakage and its effect on the results[^baltes2026guidelines-e31]
- [ ] When an LLM replaces people for annotation, scoring, or as participants, justify the substitution[^baltes2026guidelines-e25]
- [ ] Discuss what you did to improve reliability and reproducibility[^baltes2026guidelines-e33]

**Better practice**

- [ ] Report parameters even when you used the defaults[^baltes2026guidelines-e8]
- [ ] Acknowledge information unavailable from a commercial model as a limitation that hinders reproducibility[^baltes2026guidelines-e9]
- [ ] Repeat experiments and report means, confidence intervals, and so on; use inferential statistics and effect sizes for comparisons[^baltes2026guidelines-e16]
- [ ] Justify the number of repetitions[^baltes2026guidelines-e17]
- [ ] Add an open model as a baseline[^baltes2026guidelines-e23]
- [ ] Compare against less resource-intensive traditional methods, and discuss whether the resources consumed are justified[^baltes2026guidelines-e15]
- [ ] Do an error analysis, and report the share of each failure category[^baltes2026guidelines-e19]
- [ ] Release the interaction logs[^baltes2026guidelines-e14]
- [ ] When an LLM acts as annotator or judge, check a sample against human experts' judgments[^baltes2026guidelines-e25]
- [ ] Report token counts, costs, or hardware[^baltes2026guidelines-e32]
- [ ] Run a prompt stability analysis (a recommendation for social science annotation)[^tornberg2024best-e15]

**Outstanding**

- [ ] Triangulate across multiple models, independent datasets, and complementary metrics; run sensitivity analyses; rerun after some time[^baltes2026guidelines-e30]
- [ ] Supplement the evaluation with metamorphically transformed data[^sallou2024breaking-e9]
- [ ] When building a new benchmark, keep held-out items private and embed canary strings[^baltes2026guidelines-e20]
- [ ] Release the exact evaluation code[^biderman2024lessons-e7]

**Fine to skip; not a flaw**

- No open-model baseline when the study involves human participants, when people can't do the task with two models, or when the LLM is only a minor part of the study[^baltes2026guidelines-e24]
- Human validation matters less when you use a well-validated, widely used benchmark; you should still do it when you build or adapt a benchmark[^baltes2026guidelines-e39]
- Results that can't be reproduced word for word: if you discussed what you did to improve reproducibility, this alone is not a reason to reject the study[^baltes2026guidelines-e33]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Reporting a number from a single run | A small improvement may disappear on resampling[^biderman2024lessons-e10] |
| Running experiments in the web chat interface | You can't set parameters or control the version[^tornberg2024best-e4] |
| Writing only "we used GPT-4" | Commercial models change while the version name stays the same, so readers don't know which model you used[^baltes2026guidelines-e5] |
| Assuming a temperature of 0 makes results reproducible | Even at temperature 0, full determinism is rarely guaranteed[^baltes2026guidelines-e10] |
| Comparing all models with one hastily written prompt | Prompts can change rankings and conclusions[^biderman2024lessons-e4][^baltes2026guidelines-e13] |
| Evaluating on public datasets without checking for contamination | The model may have seen the answers, so its performance is overestimated[^sallou2024breaking-e1][^sainz2023nlp-e2] |
| Mistaking format errors for lack of ability | The score mixes in whether the model can answer in the required format[^baltes2026guidelines-e37][^biderman2024lessons-e11] |
| Not comparing against traditional methods | You can't show whether the LLM is worth the resources[^baltes2026guidelines-e15] |
| Tuning prompts on validation data | Overstates accuracy[^tornberg2024best-e10] |
| Trusting labels because several models agree | The agreement may just be shared bias[^baltes2026guidelines-e25] |

---

## 5. Further reading

- **Overall requirements and review criteria**: Baltes et al. 2026, the guidelines for empirical studies involving LLMs in software engineering; the online version at llm-guidelines.org is continuously updated. Each of the eight guidelines comes with rationale, recommendations, examples, and advice for reviewers, and the end has a reporting checklist organized by paper section.
- **Threats to validity from LLMs**: Sallou et al. 2024, a short paper covering three kinds of threat (closed-source models, implicit data leakage, and reproducibility), with a demonstration using ChatGPT for test generation.
- **Why evaluation details matter**: Biderman et al. 2024, lessons from the developers of the lm-eval framework on how prompts, implementation details, and variation change conclusions.
- **Data contamination**: Sainz et al. 2023.
- **Using LLMs for text annotation**: Törnberg 2024, written for the social sciences, covering everything from choosing a model and the coding workflow to validation and ethics.
- Related pages in this handbook: [Benchmarking](../07_fields/computer-science/practices/benchmarking.md), [Controlled experiments](controlled_experiment.md), [Engineering research](../07_fields/computer-science/practices/engineering_research.md), [Replication studies](replication.md).

Links to all sources are in the [source list](../../sources/README.md).

[^baltes2026guidelines-e1]: Baltes et al. 2026, §4. [Evidence](../../sources/notes/baltes2026guidelines.md#e1)
[^baltes2026guidelines-e2]: Baltes et al. 2026, §4.1. [Evidence](../../sources/notes/baltes2026guidelines.md#e2)
[^baltes2026guidelines-e3]: Baltes et al. 2026, §4.2, §4.2.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e3)
[^baltes2026guidelines-e4]: Baltes et al. 2026, §1. [Evidence](../../sources/notes/baltes2026guidelines.md#e4)
[^baltes2026guidelines-e5]: Baltes et al. 2026, §1. [Evidence](../../sources/notes/baltes2026guidelines.md#e5)
[^baltes2026guidelines-e6]: Baltes et al. 2026, §5. [Evidence](../../sources/notes/baltes2026guidelines.md#e6)
[^baltes2026guidelines-e7]: Baltes et al. 2026, §5.1. [Evidence](../../sources/notes/baltes2026guidelines.md#e7)
[^baltes2026guidelines-e8]: Baltes et al. 2026, §5.2.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e8)
[^baltes2026guidelines-e9]: Baltes et al. 2026, §5.2.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e9)
[^baltes2026guidelines-e10]: Baltes et al. 2026, §5.2.5. [Evidence](../../sources/notes/baltes2026guidelines.md#e10)
[^baltes2026guidelines-e11]: Baltes et al. 2026, §5.3.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e11)
[^baltes2026guidelines-e12]: Baltes et al. 2026, §5.3.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e12)
[^baltes2026guidelines-e13]: Baltes et al. 2026, §5.3.1. [Evidence](../../sources/notes/baltes2026guidelines.md#e13)
[^baltes2026guidelines-e14]: Baltes et al. 2026, §5.4.1, §5.4.4. [Evidence](../../sources/notes/baltes2026guidelines.md#e14)
[^baltes2026guidelines-e15]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e15)
[^baltes2026guidelines-e16]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e16)
[^baltes2026guidelines-e17]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e17)
[^baltes2026guidelines-e18]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e18)
[^baltes2026guidelines-e19]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e19)
[^baltes2026guidelines-e20]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e20)
[^baltes2026guidelines-e21]: Baltes et al. 2026, §5.5.5. [Evidence](../../sources/notes/baltes2026guidelines.md#e21)
[^baltes2026guidelines-e22]: Baltes et al. 2026, §5.5.5. [Evidence](../../sources/notes/baltes2026guidelines.md#e22)
[^baltes2026guidelines-e23]: Baltes et al. 2026, §5.6, §5.6.4. [Evidence](../../sources/notes/baltes2026guidelines.md#e23)
[^baltes2026guidelines-e24]: Baltes et al. 2026, §5.6.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e24)
[^baltes2026guidelines-e25]: Baltes et al. 2026, §5.7.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e25)
[^baltes2026guidelines-e26]: Baltes et al. 2026, §5.7.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e26)
[^baltes2026guidelines-e27]: Baltes et al. 2026, §4.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e27)
[^baltes2026guidelines-e28]: Baltes et al. 2026, §4.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e28)
[^baltes2026guidelines-e29]: Baltes et al. 2026, §4.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e29)
[^baltes2026guidelines-e30]: Baltes et al. 2026, §5.8.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e30)
[^baltes2026guidelines-e31]: Baltes et al. 2026, §5.8.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e31)
[^baltes2026guidelines-e32]: Baltes et al. 2026, §5.8.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e32)
[^baltes2026guidelines-e33]: Baltes et al. 2026, §5.8.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e33)
[^baltes2026guidelines-e34]: Baltes et al. 2026, §4.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e34)
[^baltes2026guidelines-e35]: Baltes et al. 2026, §2. [Evidence](../../sources/notes/baltes2026guidelines.md#e35)
[^baltes2026guidelines-e36]: Baltes et al. 2026, §5.2.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e36)
[^baltes2026guidelines-e37]: Baltes et al. 2026, §5.5.2. [Evidence](../../sources/notes/baltes2026guidelines.md#e37)
[^baltes2026guidelines-e38]: Baltes et al. 2026, §5.7.2, §4.3. [Evidence](../../sources/notes/baltes2026guidelines.md#e38)
[^baltes2026guidelines-e39]: Baltes et al. 2026, §5.7.6. [Evidence](../../sources/notes/baltes2026guidelines.md#e39)
[^sallou2024breaking-e1]: Sallou et al. 2024, §1. [Evidence](../../sources/notes/sallou2024breaking.md#e1)
[^sallou2024breaking-e2]: Sallou et al. 2024, §2.1. [Evidence](../../sources/notes/sallou2024breaking.md#e2)
[^sallou2024breaking-e3]: Sallou et al. 2024, §2.2. [Evidence](../../sources/notes/sallou2024breaking.md#e3)
[^sallou2024breaking-e4]: Sallou et al. 2024, §2.2. [Evidence](../../sources/notes/sallou2024breaking.md#e4)
[^sallou2024breaking-e5]: Sallou et al. 2024, §2.3. [Evidence](../../sources/notes/sallou2024breaking.md#e5)
[^sallou2024breaking-e6]: Sallou et al. 2024, §2.3. [Evidence](../../sources/notes/sallou2024breaking.md#e6)
[^sallou2024breaking-e7]: Sallou et al. 2024, §3.2.1. [Evidence](../../sources/notes/sallou2024breaking.md#e7)
[^sallou2024breaking-e8]: Sallou et al. 2024, §3.2.1. [Evidence](../../sources/notes/sallou2024breaking.md#e8)
[^sallou2024breaking-e9]: Sallou et al. 2024, §3.2.2. [Evidence](../../sources/notes/sallou2024breaking.md#e9)
[^sallou2024breaking-e10]: Sallou et al. 2024, §3.2.2. [Evidence](../../sources/notes/sallou2024breaking.md#e10)
[^sallou2024breaking-e11]: Sallou et al. 2024, §3.2.2. [Evidence](../../sources/notes/sallou2024breaking.md#e11)
[^biderman2024lessons-e2]: Biderman et al. 2024, §2.2. [Evidence](../../sources/notes/biderman2024lessons.md#e2)
[^biderman2024lessons-e3]: Biderman et al. 2024, §2.2. [Evidence](../../sources/notes/biderman2024lessons.md#e3)
[^biderman2024lessons-e4]: Biderman et al. 2024, §3.1. [Evidence](../../sources/notes/biderman2024lessons.md#e4)
[^biderman2024lessons-e6]: Biderman et al. 2024, §3.1. [Evidence](../../sources/notes/biderman2024lessons.md#e6)
[^biderman2024lessons-e7]: Biderman et al. 2024, §3.2. [Evidence](../../sources/notes/biderman2024lessons.md#e7)
[^biderman2024lessons-e8]: Biderman et al. 2024, §3.3. [Evidence](../../sources/notes/biderman2024lessons.md#e8)
[^biderman2024lessons-e9]: Biderman et al. 2024, §4.1. [Evidence](../../sources/notes/biderman2024lessons.md#e9)
[^biderman2024lessons-e10]: Biderman et al. 2024, §4.1. [Evidence](../../sources/notes/biderman2024lessons.md#e10)
[^biderman2024lessons-e11]: Biderman et al. 2024, §4.1. [Evidence](../../sources/notes/biderman2024lessons.md#e11)
[^biderman2024lessons-e12]: Biderman et al. 2024, §4.2. [Evidence](../../sources/notes/biderman2024lessons.md#e12)
[^biderman2024lessons-e13]: Biderman et al. 2024, §4.3. [Evidence](../../sources/notes/biderman2024lessons.md#e13)
[^sainz2023nlp-e1]: Sainz et al. 2023, Abstract. [Evidence](../../sources/notes/sainz2023nlp.md#e1)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e4]: Sainz et al. 2023, §5.1. [Evidence](../../sources/notes/sainz2023nlp.md#e4)
[^sainz2023nlp-e5]: Sainz et al. 2023, §5.2. [Evidence](../../sources/notes/sainz2023nlp.md#e5)
[^tornberg2024best-e2]: Törnberg 2024, item 1. [Evidence](../../sources/notes/tornberg2024best.md#e2)
[^tornberg2024best-e3]: Törnberg 2024, item 1. [Evidence](../../sources/notes/tornberg2024best.md#e3)
[^tornberg2024best-e4]: Törnberg 2024, item 1. [Evidence](../../sources/notes/tornberg2024best.md#e4)
[^tornberg2024best-e5]: Törnberg 2024, item 2. [Evidence](../../sources/notes/tornberg2024best.md#e5)
[^tornberg2024best-e6]: Törnberg 2024, item 2. [Evidence](../../sources/notes/tornberg2024best.md#e6)
[^tornberg2024best-e7]: Törnberg 2024, item 2. [Evidence](../../sources/notes/tornberg2024best.md#e7)
[^tornberg2024best-e8]: Törnberg 2024, item 3. [Evidence](../../sources/notes/tornberg2024best.md#e8)
[^tornberg2024best-e9]: Törnberg 2024, item 4. [Evidence](../../sources/notes/tornberg2024best.md#e9)
[^tornberg2024best-e10]: Törnberg 2024, item 4. [Evidence](../../sources/notes/tornberg2024best.md#e10)
[^tornberg2024best-e11]: Törnberg 2024, item 4. [Evidence](../../sources/notes/tornberg2024best.md#e11)
[^tornberg2024best-e12]: Törnberg 2024, item 4. [Evidence](../../sources/notes/tornberg2024best.md#e12)
[^tornberg2024best-e13]: Törnberg 2024, item 4. [Evidence](../../sources/notes/tornberg2024best.md#e13)
[^tornberg2024best-e14]: Törnberg 2024, item 6. [Evidence](../../sources/notes/tornberg2024best.md#e14)
[^tornberg2024best-e15]: Törnberg 2024, item 8. [Evidence](../../sources/notes/tornberg2024best.md#e15)
[^tornberg2024best-e16]: Törnberg 2024, item 9. [Evidence](../../sources/notes/tornberg2024best.md#e16)
[^tornberg2024best-e17]: Törnberg 2024, item 7. [Evidence](../../sources/notes/tornberg2024best.md#e17)
[^tornberg2024best-e18]: Törnberg 2024, Introduction and Conclusion. [Evidence](../../sources/notes/tornberg2024best.md#e18)
