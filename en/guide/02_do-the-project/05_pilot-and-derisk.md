# The smallest version that runs end to end

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

> **What you must do in this chapter**
>
> 1. **List the assumptions your design rests on and circle the three most dangerous.** Score each one on how bad it is if false, how sure you are, and how costly it is to check ([Section 1](#1-list-the-assumptions-your-design-rests-on-and-find-the-most-dangerous-ones)).
> 2. **Find a cheap test for each dangerous assumption.** Write down what you'll do, how much data, how much time, and what you expect to see; ideally finish within a week ([Section 2](#2-find-a-cheap-test-for-each-dangerous-assumption)).
> 3. **Run the whole pipeline end to end at the smallest scale.** Fill in one row of the empty results table, and run a simple baseline and a baseline that "shouldn't work" alongside it ([Section 3](#3-build-a-minimal-version-that-runs-end-to-end)).
> 4. **If the study involves people, questionnaires, or annotation, run a pilot first.** For the last round, state how it matches the main study and how it differs ([Section 4](#4-when-people-data-and-instruments-are-involved-run-a-pilot-study)).
> 5. **Before the trial, write down the criteria for "continue / continue with changes / stop".** Every cell must be checkable directly against the trial results; send them to your advisor before you start ([Section 5](#5-write-down-in-advance-what-results-mean-continue-adjust-or-stop)).
> 6. **Don't read research findings into trial data.** The post-trial summary says only whether the criteria were met, what in the design needs to change, and what happens next ([Section 6](#6-dont-read-too-much-into-trial-data)).
>
> **Done these? Move on:** the most dangerous assumptions have all been tested, the whole pipeline has run end to end, the trial results have been judged against criteria written in advance, and your advisor has seen the trial summary and the revised design. Next: [Running and iterating](06_run-and-iterate.md).

## Where you are

Your study design is mostly settled: you know which claim you want to establish and what evidence you need (see [From research questions to an evidence plan](01_question-to-evidence.md)), you have chosen a research strategy and a research method (see [Choosing a method](02_choose-method.md)), you have laid out a plan (see [Writing a research plan](03_research-plan.md)), and you have thought about where your conclusions might not hold (see [Validity and limitations](04_validity-and-limits.md)).

When you were [converging on a project](../01_find-a-problem/05_converge.md#5-can-you-actually-do-it), you already ran a small experiment on the part of the project you were least sure of. That trial answered "is this project worth doing, and can it be done?" In your [research plan](03_research-plan.md#4-set-the-order-do-what-is-most-likely-to-fail-first), you also put the milestones most likely to fail first.

Now the question is more specific: **once this design is rolled out, it will take weeks or even months. Before you commit, how do you make sure it will actually run the way it is designed?**

This is not the same thing as [exploring hands-on](../01_find-a-problem/03_explore.md#5-exploring-is-not-the-same-as-building-the-smallest-version-that-runs-end-to-end) in Part 1. Exploration is for coming up with hypotheses; here you are making sure the design that will test them actually runs.

## What this stage is for

Before the full study, use small trials to answer these five questions:

1. What assumptions does this design rest on? Which of them, if false, would make the whole study wasted effort?
2. For each risky assumption, is there a cheap way to check it first?
3. Does the whole pipeline, from input data to a filled-in results table, run from start to finish?
4. If the study uses participants, annotators, questionnaires, or scoring rules, do they work under real conditions?
5. After the trial, by what criteria do you decide whether to continue as planned, continue with changes, or stop?

"Small trials" in this chapter covers two kinds of work. One is **de-risking** each part of the design: finding a cheap way to judge with confidence whether that part will work[^steinhardt2018stochastic-e5]. The other is the **pilot study** (also called a pilot or a preliminary study): a small trial run before the main study, to find extraneous factors that would interfere with the results[^ko2015practical-e31] and problems in the experiment that need fixing[^ko2015practical-e32]. Both aim at the same thing: assess feasibility first, so you don't rush into a large study and risk disastrous consequences[^thabane2010tutorial-e1].

Much of this chapter's advice on pilot studies comes from a tutorial on pilot studies in clinical research, with input from the experience of software engineering and machine learning researchers. The reasoning carries over; the specific numbers and procedures should follow your own field's conventions.

---

## 1. List the assumptions your design rests on and find the most dangerous ones

**First, write down everything your design takes for granted.** When you write a design, you carry many unspoken premises: the data is clean, the tools run, everyone reads the annotation rules the same way, the effect is big enough to detect, the budget is enough. If any one of these is false, the work that follows may be wasted.

You can search in four categories. The clinical pilot study tutorial groups the reasons for doing a pilot into process, resources, management, and scientific: process asks whether each step of the main study works, and resources asks whether time and money will be a problem[^thabane2010tutorial-e2]. In our view, this grouping works in other fields too. The "What to ask" column and the examples in the table below are rephrased for a computer science project:

| Category | What to ask | Example: the project "benchmark results are inflated by data leakage" |
|---|---|---|
| Process | Does each step work as designed? | Can you get any clues about each model's training data? Can the contracts be compiled in bulk and fed to the models in bulk? |
| Resources | Is there enough time and money? | How many calls to the model APIs (application programming interfaces) will running all the contracts take, how much will it cost, and how long will it take? |
| Management | Will people or data cause problems? | Two people annotate separately; how do you merge their results? Where is intermediate data stored, and how is it versioned? |
| Scientific | Do the design's core judgments hold up? | Is the method for deciding "leaked or not" accurate? Is the difference before and after removing leaked samples big enough to see? |

**Then give each assumption three scores**:

- **How bad is it if it's false?** Change one parameter, or the whole study collapses?
- **How sure are you that it holds?** Is there existing evidence, or just "it should be fine"?
- **How much effort does it take to check?** An afternoon, or two weeks?

The ones at the top of the list are those where being wrong loses everything, you are least sure, and checking is not expensive. The logic is the same as [ordering milestones in your research plan](03_research-plan.md#4-set-the-order-do-what-is-most-likely-to-fail-first).

For each key assumption, ask yourself: **"If this direction is doomed, how can I find out fastest?"**[^nanda2025mindsets-e12]

**Write it down:** List every assumption your design rests on, at least ten, grouped into process, resources, management, and scientific. Give each the three scores "how bad if false / how sure / how costly to check", and circle the three most dangerous.

## 2. Find a cheap test for each dangerous assumption

Once you have circled the dangerous assumptions, **don't start the full study; de-risk them one at a time first.** The basic approach: de-risk every part that can be de-risked, then execute[^steinhardt2018stochastic-e5].

**What does a cheap test look like?** The forms below come from one machine learning researcher's experience, and you can borrow them in other areas too:

| What you're worried about | A cheap test |
|---|---|
| The data won't serve | Take a small subset, look at some of it by hand, compute some statistics, and see whether it has the properties you need, before putting in the big effort to prepare all of it[^steinhardt2018stochastic-e6] |
| The result you want to prove is actually false | Before you try to prove it, run simulations to see whether it really holds[^steinhardt2018stochastic-e18] |
| How much room there is between good and bad methods | Measure an "upper bound": replace the hard part with a "cheating" version first, for example peeking at the test set; then measure a simple baseline as the lower bound. Together they mark out the range the results can fall in and help you interpret the core result[^steinhardt2018stochastic-e24][^steinhardt2018stochastic-e7] |
| A complex method does worse than a simple one | Run simple or off-the-shelf methods first; complex methods are often no better than simple baselines[^steinhardt2018stochastic-e7] |

When you were [converging on a project](../01_find-a-problem/05_converge.md#5-can-you-actually-do-it), checking 50 samples by hand to see whether your leakage judgments were accurate was exactly this kind of cheap test. Now apply the same approach to the other dangerous assumptions in your design. For the "benchmark results are inflated by data leakage" example:

- **Is the difference big?** Measure the "upper bound" first: if you remove every clearly leaked sample, how far can accuracy drop at most? If it barely drops, the claim isn't worth months of work to establish.
- **Is the budget enough?** Run 20 contracts first, record the number of calls, the cost, and the time, then multiply by the total number of contracts.

**Before each test, write down what you expect to see.** A write-up of lessons on training neural networks advises making a concrete prediction about the result at every step and then checking it with an experiment; if the result doesn't match, keep digging until you find the problem[^karpathy2019recipe-e1]. The habit is just as useful in other research: if you don't write the prediction down, it is easy to read any result as "roughly what I expected".

**De-risking doesn't mean only doing safe things**, nor avoiding projects that don't yet have an obvious path to success[^steinhardt2018stochastic-e13]. Ruling out dead ends early is precisely what frees up time to try ideas that are unlikely to work but very valuable if they do.

**Write it down:** For each of the three dangerous assumptions you circled, write a test: what you'll do, how much data, how much time, and what result you expect. Ideally each test can be done within a week.

## 3. Build a minimal version that runs end to end

Checking each part separately isn't enough. Many problems only appear when the parts are **connected**: one step's output format doesn't match the next step's input, a step quietly drops half the data, the evaluation script computes something other than the metric you think it does.

**How: before you scale up, run the whole pipeline once, start to finish, at the smallest scale.** One piece of advice from the neural network training lessons: before using a complex model, set up the full skeleton from training to evaluation and confirm it is correct through a series of experiments; at this point, pick a model so simple you can't possibly get it wrong[^karpathy2019recipe-e8].

For a computer science project, the "minimal version" might look like this:

1. **Use only a small slice of the data.** For example, 20 contracts, including a few whose answers you know by hand.
2. **Use the simplest version of the method.** For example, only one prompt and one model.
3. **Connect every step.** Read the data → send it to the model → parse the output → judge right or wrong → compute the metric → fill in the results table.
4. **Actually fill in the results table.** Take the empty results table you drew when [converging on a project](../01_find-a-problem/05_converge.md#4-what-will-make-people-believe-it) and fill it in with the results for these 20 contracts. The numbers themselves don't matter; what matters is that you know where every cell comes from.

**What counts as "runs end to end"?** You can borrow the standard from neural network training: the whole pipeline works; for any method, you can reproducibly compute a metric you trust; and you have scores for a few simple baselines, which any new method must beat[^karpathy2019recipe-e9].

**A few checks that make the minimal version actually useful** (also from the neural network training lessons, with the examples changed to a computer science project):

- **No errors does not mean correct.** In neural network training, many bugs are silent: the syntax is fine, but the pieces aren't put together the right way, and it is hard to tell[^karpathy2019recipe-e3]. Spot-check a few intermediate results by hand.
- **Build a baseline that shouldn't work.** For example, set all inputs to zero; it should score worse than with the real inputs[^karpathy2019recipe-e5]. If it scores about the same, your method is not learning anything from the data. In vulnerability detection, you could scramble the contract code or swap in unrelated code, and see whether the model's "detection rate" stays just as high.
- **Add one thing at a time.** Try hard not to introduce a lot of unverified complexity at once[^karpathy2019recipe-e2]; when you need to add several new things, add them one by one and confirm each time that you get the expected improvement[^karpathy2019recipe-e6].

**This isn't only about code.** Design-based research in education makes the same case: don't build the whole solution only to find at the end that it doesn't work; make rough prototypes quickly, test them, and revise[^easterday2014design-e12]. Early in a project, collect only the minimum data needed to quickly eliminate failing designs and spot promising ones[^easterday2014design-e14].

**Write it down:** Draw every step of your study from raw data to results table, marking each step's inputs and outputs. Run it once at the smallest scale, fill in one row of the empty results table, and record every problem you find along the way.

## 4. When people, data, and instruments are involved: run a pilot study

> **Scope:** This section is mainly for studies that need participants, manual annotation, questionnaires, interviews, or screening criteria. For purely computational projects, the minimal version from Section 3 is often your pilot study.

As soon as people take part in a study, more things can go wrong: participants don't understand the task instructions, questionnaire items are ambiguous, a session runs far longer than expected, two annotators judge the same contract differently. You can't see these problems just by reading the design.

**A pilot study is a key step in preparing an experiment**: a trial run before the real experiment, to find extraneous factors that would interfere with the results[^ko2015practical-e31]. In software engineering research, piloting may not yet be standard practice[^ko2015practical-e31]. So the fact that other people's papers don't mention it doesn't mean you can skip it.

**Test in rounds, from close to home outward.** Pilot testing an interview guide can take three forms: internal testing within the team, expert assessment, and field testing[^kallio2016systematic-e5]; internal testing helps you remove vague and leading questions[^kallio2016systematic-e6]. Before that, researchers can also rehearse the study themselves as participants[^ko2015practical-e33]. For other studies involving people, you can arrange the rounds as in the table below:

| Round | Who tries it | What it can reveal |
|---|---|---|
| Self-test | The researcher acts as a participant and goes through the whole procedure | Obvious gaps in the procedure, duration, missing materials |
| Internal team test | Other people in your research group | Vague questions, leading questions |
| Expert review | Outside experts who know the field or the method | Whether the questions get at the point, what is missing |
| Field test | A few people of the same kind as the real participants | Understanding, duration, and cooperation under real conditions |

The most important round is the one that **runs as close as possible to the real study**: use the same kind of participants, the same setting, the same materials, instructions, questionnaires, procedure, and experimenters wherever you can[^ko2015practical-e32]. Clinical research also requires pilot participants to represent the target population, using the same inclusion and exclusion criteria as the main study[^thabane2010tutorial-e9]; following the same idea in other fields won't go wrong.

**Different research methods put the emphasis on different things:**

- **Questionnaires**: once designed, check that the questionnaire measures what you intend to measure; the methods mentioned most often in the literature are pilot surveys, test-retest, focus groups, and expert or non-expert review[^molleri2020empirically-e2]. After a pilot survey, talk with participants to confirm the items were understood easily and correctly[^wagner2020challenges-e24]. For details, see [Questionnaire surveys](../06_methods/questionnaire_survey.md).
- **Interviews**: try the interview guide within your team first, and remove vague and leading questions[^kallio2016systematic-e6]. See [Interview studies](../06_methods/interview_study.md).
- **Controlled experiments**: go through it yourself as a participant first, then have a few participants of the same kind try it with the real procedure[^ko2015practical-e33][^ko2015practical-e32]. See [Controlled experiments](../06_methods/controlled_experiment.md).
- **Literature reviews**: once the selection criteria are set, try them on a small batch of papers first[^kitchenham2007guidelines-e8]. See [Review studies](../06_methods/review_study.md).
- **Manual annotation**: have two people each label the same small batch of samples, compare where they disagree, write the points of large disagreement into the annotation rules, and try another round.

**Be clear with participants about the pilot, too.** In clinical research, the practice is to write a dedicated statement telling participants that this is a pilot study, which aspects of feasibility it will assess, and what result counts as feasible[^thabane2010tutorial-e12]. **A pilot study may also need ethics review.** Taking a single country, Canada, as the example: the *Tri-Council Policy Statement: Ethical Conduct for Research Involving Humans* (TCPS 2, 2022 edition), issued jointly by Canada's three federal research funding agencies, defines a pilot study as a scaled-down version of the main study (fewer participants, shorter duration) and requires that, like the main study, it be submitted to a research ethics board (REB) for review before participants are recruited or data collected[^tcps2022ethical-e1][^tcps2022ethical-e3]; preliminary exploration done only to build partnerships or design the project does not need review[^tcps2022ethical-e3]. How strict the review is depends on the risk to participants: the lower the risk, the lighter the review[^tcps2022ethical-e4][^tcps2022ethical-e5]. Our reading of this definition is that the round in the table above closest to a pilot study is the field test; the policy doesn't say one way or the other whether the earlier internal rounds count. Our sources do not cover what other countries and institutions require; before you start, ask your advisor or your institution's ethics committee.

**Write it down:** Write your pilot plan: how many rounds, whom you'll recruit for each and how many, which materials, and which problems you'll focus on. For the last round, state clearly how it is the same as the main study and how it differs.

## 5. Write down in advance what results mean continue, adjust, or stop

**Write down your decision criteria before you run the trial.** A pilot study must state its criteria for success, and they should be based on the main feasibility objectives[^thabane2010tutorial-e3]. If you set the criteria after the trial, you will unconsciously move them toward the results.

The clinical tutorial sorts pilot outcomes into four kinds[^thabane2010tutorial-e3]:

1. **Stop**: the main study is not feasible;
2. **Continue with modifications**: feasible once changed;
3. **Continue without changes, but with close monitoring**;
4. **Continue as planned**.

**Write the criteria as concrete numbers or checkable conditions.** An example from medicine: the pilot for a multicenter clinical trial specified in advance that at least 70% of eligible patients must be recruited and at least 95% of participants must complete follow-up[^thabane2010tutorial-e4]. For a computer science project, you might write:

| What you're testing | Continue | Continue with changes | Stop |
|---|---|---|---|
| Leakage detection method | Of 50 samples checked by hand, at least 45 judgments agree | Agreement is too low, but the disagreements cluster in one kind of contract, so the rules can be fixed | The disagreements show no pattern, and you can't see how to improve |
| How much leakage matters | In the upper-bound test, accuracy drops clearly | Clear only for some models; the claim needs narrowing | Almost no change after removing all leaked samples |
| Cost and time | The estimated total cost is within budget | Over budget, but affordable with fewer models | Far over budget however you cut it |
| Annotation agreement | The two annotators rarely disagree | Disagreements cluster where the rules are unclear | After two rounds of rule changes, disagreement is still high |

The thresholds above are only examples; set yours together with your advisor, based on your project.

**"Stop" is not failure.** A pilot that shows the main study is unlikely to be feasible has done its job: it kept you from wasting limited resources on a study doomed to fail[^thabane2010tutorial-e8].

**But don't call "stop" lightly, either.** One failed trial shows only that one specific implementation of the idea doesn't work, not that the whole idea doesn't[^steinhardt2018stochastic-e10]. "It looks like it won't work" or "I tried a few times and lost steam" don't count as really ruling it out[^steinhardt2018stochastic-e22]. Before deciding, tell these apart:

- **A detail of the design went wrong** (an ambiguous item, a poorly written prompt, a buggy script) → fix it and try again;
- **A core assumption of the design is false** (leakage barely affects the results, the data you need simply can't be obtained) → go back to the claim and consider narrowing it or changing the angle.

**Write it down:** For each dangerous assumption you circled in Section 1, write one row of "continue / continue with changes / stop" criteria, with every cell directly checkable against the trial results. Send this table to your advisor before you run the trial.

## 6. Don't read too much into trial data

The trial results are in, and they look promising. The easiest mistake now is **treating the pilot as a small version of the main study**.

**A pilot answers "can this be done?", not "how big is the effect?"** A common mistake is to focus on statistical significance instead of feasibility[^thabane2010tutorial-e6]. Specifically:

- **Don't use a pilot to estimate effect size.** Sources from clinical research, psychology, and animal studies all make this point. With a small sample, the estimated effect may be unrealistic and biased[^thabane2010tutorial-e5]. Effect sizes from small pilots are very imprecise and shouldn't be used to compute the main study's sample size[^lakens2022sample-e4]. A pilot alone rarely gives you enough data on variability either; previous studies and systematic reviews are better sources[^perciedusert2020reporting-e36]. For what effect size and sample size mean, see [Analysis and interpretation](07_analyze-and-interpret.md).
- **No significant result does not mean no effect.** An underpowered study that finds no significant result can only be called "inconclusive", not evidence of "no effect"[^thabane2010tutorial-e7].
- **Even if the results look great, don't rush them into the paper's main conclusions.** The pilot design is often still changing and the scale is small, so it can't support the central claim. If you do need to report it, you can follow one pharmacology journal's author guidelines: put it in a separate "Pilot study" subsection of the methods, and give no P values[^curtis2018experimental-e11].

**Can pilot data be used in the main study?** Sources disagree here, and it affects what you do.

> **Where sources disagree: discard pilot data, or merge it into the main study?**
> - **Discard it.** Guidelines for software engineering experiments that evaluate tools with human participants say all data collected in a pilot should be discarded, because the purpose of a pilot is to find problems in the experiment to fix, not to collect data[^ko2015practical-e32].
> - **It can be merged, but only if planned in advance.** The clinical pilot tutorial doesn't rule out merging altogether. Instead it requires that if you are considering combining pilot and main-study data, this must be planned in advance, written into the protocol, and the statistical implications and methods discussed clearly[^thabane2010tutorial-e10].
>
> In practice, you can handle it like this: **discard by default.** Consider merging only if you stated before the trial that "this data will be merged into the main study" and you did not change the design after the trial. If you change the design after seeing pilot results, the changed main study needs new data.

**Write it down:** After the trial, write a short summary that answers only three things: whether each feasibility criterion was met, what in the design needs to change, and whether the next step is to continue, modify, or stop. Don't write "how much the effect improved".

> **How this step differs by type of research**
>
> - **Empirical studies** (see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md)): before scaling up, check how accurate your automated method is on a small hand-labeled sample. He et al. 2020 had two of the authors compare 1,100 contract pairs by hand to build a ground truth; at a similarity threshold of 70, precision was 97.5% and recall 88%[^he2020characterizing-e9].
> - **Tool or method papers** (see [Engineering research](../07_fields/computer-science/practices/engineering_research.md)): first make sure the tool actually runs on real code. The Slither paper treats the share of contracts the analysis fails on as a metric: Slither failed on only 0.1% of contracts, against 10.22% for SmartCheck and 11.20% for Securify[^feist2019slither-e11].
> - **Benchmarks or datasets** (see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md)): first check whether the raw data is usable. SmartBugs found that once spaces and tabs were stripped, 95% of the contract source files were duplicates[^durieux2020empirical-e8].
> - **Reviews** (see [Review studies](../06_methods/review_study.md)): run your search string once first and see how many hits you get and where they come from. Rameder et al. 2022 retrieved 1,326 results across five databases and reported the count for each one[^rameder2022review-e5]. Also try your selection criteria on a small batch of papers first[^kitchenham2007guidelines-e8].

---

## Judgment calls

**How much trialing is enough?** Not when you "can't find any more problems", but when every dangerous assumption circled in Section 1 has an answer, the whole pipeline has run end to end once, and the parts involving people have been tried under near-real conditions. The rule of thumb from the clinical pilot tutorial: the pilot should be big enough to give useful information on the feasibility aspects you want to assess[^thabane2010tutorial-e9].

**What if the trial turns up problems?** One way to decide:

| What the trial showed | Usual response |
|---|---|
| Detail problems: ambiguous materials, a buggy script, a missing step | Fix them, then try the changed parts again in a small round |
| Resource problems: time or cost far over | Scale down, or discuss with your advisor switching to a cheaper kind of evidence |
| Measurement problems: the judgment method or annotation rules are unreliable | Fix the measurement before anything else; if measurement is unreliable, none of the later results mean anything |
| A core assumption is false | Stop, go back to the claim, and consider narrowing it or changing the angle |
| No problems | Move on to the full study, and keep good records of this trial |

**When you are told to "just do a pilot first"**, first talk through with your advisor how the results of this trial will affect the plan for the main study[^thabane2010tutorial-e11]. If no one can say, it is better to design it as a small independent study than to call it a pilot.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Skipping the trial and going straight to full scale | Problems surface weeks later, and earlier work may be wasted |
| Trying the easiest parts first | People often try to disprove their ideas too late[^steinhardt2018stochastic-e12]; leave the most dangerous assumption for last and you find out at the end that it can't work |
| Trying each part separately but never running the whole pipeline | Problems that appear when the parts are connected can't be found by testing parts separately |
| Only checking that the program doesn't crash | Many bugs are silent, and the results still look like they "work"[^karpathy2019recipe-e3] |
| Piloting with people completely unlike the real participants | You won't find the problems that arise under real conditions[^ko2015practical-e32][^thabane2010tutorial-e9] |
| Deciding "what counts as success" after the trial | The criteria get pulled along by the results; the clinical pilot tutorial singles out this failing: no clear feasibility objectives or success criteria[^thabane2010tutorial-e6] |
| Using the pilot's effect size to compute the main study's sample size | Effect sizes estimated from small samples are very imprecise[^lakens2022sample-e4] |
| Concluding there is no effect because the pilot showed no significant result | With too small a sample, all you can say is "inconclusive"[^thabane2010tutorial-e7] |
| Giving up on a whole idea after one trial goes badly | Only one implementation failed[^steinhardt2018stochastic-e10] |

## What you should have at the end

- A list of assumptions, grouped into process, resources, management, and scientific, with the three most dangerous marked (Section 1)
- A test record for each dangerous assumption: expectation, actual result, conclusion (Section 2)
- A minimal version that runs end to end, and a results table with one row filled in (Section 3)
- A pilot plan and a record of problems found in each round (Section 4, when people, questionnaires, or annotation are involved)
- A "continue / continue with changes / stop" criteria table written in advance, and a trial summary written against it (Sections 5 and 6)
- A study design revised in light of the trial results

## Checklist before moving on

You can move on to the full study when all of these hold:

- [ ] You have listed the assumptions your design rests on, and the most dangerous ones have been tested
- [ ] Before each test you wrote down an expectation, and after it a conclusion
- [ ] The whole pipeline has run end to end at the smallest scale, and you know where every cell of the results table comes from
- [ ] You have scores for a baseline that shouldn't work and for simple baselines
- [ ] The parts involving people, questionnaires, or annotation have been tried under near-real conditions, and the problems found have been fixed
- [ ] The "continue / continue with changes / stop" criteria were written before the trial, and the trial results were judged against them
- [ ] You have not treated the pilot's effects as research findings
- [ ] Your advisor has looked at the trial summary and the revised design

## When to go back

| If this happens | Go back to |
|---|---|
| You can't tell whether to continue, adjust, or go back | [Decision points: continue, adjust, or go back](08_decision-points.md#2-one-master-table-when-what-you-see-how-to-choose): look up the row "The pilot has finished" |
| A core assumption is false, e.g., the difference you want to measure barely exists | [Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove): narrow the claim or pick another one; first use [Decision points](08_decision-points.md#3-how-to-judge-each-option) to judge whether you should go back |
| You can't get the data, tools, or participants you need | [Choosing a method](02_choose-method.md): switch to evidence you can get |
| The measurement method or annotation rules stay unreliable however you change them | [From research questions to an evidence plan](01_question-to-evidence.md): rethink what to measure with |
| The trial exposed threats to validity you hadn't anticipated | [Validity and limitations](04_validity-and-limits.md): add responses to them |
| Time and cost are far over plan | [Writing a research plan](03_research-plan.md#judgment-calls): decide again what to cut |

## Next

The dangerous assumptions have been checked, the pipeline runs, and the design has been revised in light of the trial. Next comes the full study: moving forward according to plan, adjusting as you go, and having ways to keep going when you get stuck. See [Running and iterating](06_run-and-iterate.md).

[^steinhardt2018stochastic-e5]: Steinhardt 2018, A further improvement: opening up the "task" black box. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e5)
[^steinhardt2018stochastic-e6]: Steinhardt 2018, A further improvement. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e6)
[^steinhardt2018stochastic-e7]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e7)
[^steinhardt2018stochastic-e10]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e12]: Steinhardt 2018, Summary. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e12)
[^steinhardt2018stochastic-e13]: Steinhardt 2018, Additional Discussion. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e13)
[^steinhardt2018stochastic-e18]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e18)
[^steinhardt2018stochastic-e22]: Steinhardt 2018, Additional Discussion. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e22)
[^steinhardt2018stochastic-e24]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e24)
[^nanda2025mindsets-e12]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e12)
[^karpathy2019recipe-e1]: Karpathy 2019, The recipe. [Evidence](../../sources/notes/karpathy2019recipe.md#e1)
[^karpathy2019recipe-e2]: Karpathy 2019, The recipe. [Evidence](../../sources/notes/karpathy2019recipe.md#e2)
[^karpathy2019recipe-e3]: Karpathy 2019, 2) Neural net training fails silently. [Evidence](../../sources/notes/karpathy2019recipe.md#e3)
[^karpathy2019recipe-e5]: Karpathy 2019, 2. Set up the end-to-end training/evaluation skeleton, input-independent baseline. [Evidence](../../sources/notes/karpathy2019recipe.md#e5)
[^karpathy2019recipe-e6]: Karpathy 2019, 3. Overfit, complexify only one at a time. [Evidence](../../sources/notes/karpathy2019recipe.md#e6)
[^karpathy2019recipe-e8]: Karpathy 2019, 2. Set up the end-to-end training/evaluation skeleton. [Evidence](../../sources/notes/karpathy2019recipe.md#e8)
[^karpathy2019recipe-e9]: Karpathy 2019, 2. Set up the end-to-end training/evaluation skeleton, final paragraph. [Evidence](../../sources/notes/karpathy2019recipe.md#e9)
[^easterday2014design-e12]: Easterday et al. 2014, Iteration, p. 321. [Evidence](../../sources/notes/easterday2014design.md#e12)
[^easterday2014design-e14]: Easterday et al. 2014, Stage Dependent Search, p. 322. [Evidence](../../sources/notes/easterday2014design.md#e14)
[^ko2015practical-e31]: Ko et al. 2015, §8 Piloting. [Evidence](../../sources/notes/ko2015practical.md#e31)
[^ko2015practical-e32]: Ko et al. 2015, §8 Piloting. [Evidence](../../sources/notes/ko2015practical.md#e32)
[^ko2015practical-e33]: Ko et al. 2015, §8 Piloting. [Evidence](../../sources/notes/ko2015practical.md#e33)
[^kallio2016systematic-e5]: Kallio et al. 2016, Results, Pilot testing of the interview guide. [Evidence](../../sources/notes/kallio2016systematic.md#e5)
[^kallio2016systematic-e6]: Kallio et al. 2016, Results, Pilot testing of the interview guide. [Evidence](../../sources/notes/kallio2016systematic.md#e6)
[^molleri2020empirically-e2]: Molléri et al. 2020, §2, Instrument validation. [Evidence](../../sources/notes/molleri2020empirically.md#e2)
[^wagner2020challenges-e24]: Wagner et al. 2020, §6, Take Aways. [Evidence](../../sources/notes/wagner2020challenges.md#e24)
[^kitchenham2007guidelines-e8]: Kitchenham & Charters 2007, §5.4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e8)
[^thabane2010tutorial-e1]: Thabane et al. 2010, §1 Introduction. [Evidence](../../sources/notes/thabane2010tutorial.md#e1)
[^thabane2010tutorial-e2]: Thabane et al. 2010, §3 Reasons for Conducting Pilot Studies. [Evidence](../../sources/notes/thabane2010tutorial.md#e2)
[^thabane2010tutorial-e3]: Thabane et al. 2010, §6 Criteria for Success. [Evidence](../../sources/notes/thabane2010tutorial.md#e3)
[^thabane2010tutorial-e4]: Thabane et al. 2010, §6, the POET pilot study example. [Evidence](../../sources/notes/thabane2010tutorial.md#e4)
[^thabane2010tutorial-e5]: Thabane et al. 2010, §5 Challenges and Misconceptions. [Evidence](../../sources/notes/thabane2010tutorial.md#e5)
[^thabane2010tutorial-e6]: Thabane et al. 2010, §5 Challenges and Misconceptions. [Evidence](../../sources/notes/thabane2010tutorial.md#e6)
[^thabane2010tutorial-e7]: Thabane et al. 2010, §7 Frequently asked questions. [Evidence](../../sources/notes/thabane2010tutorial.md#e7)
[^thabane2010tutorial-e8]: Thabane et al. 2010, §7 Frequently asked questions. [Evidence](../../sources/notes/thabane2010tutorial.md#e8)
[^thabane2010tutorial-e9]: Thabane et al. 2010, §5, sample size. [Evidence](../../sources/notes/thabane2010tutorial.md#e9)
[^thabane2010tutorial-e10]: Thabane et al. 2010, §5, sample size and pooled data. [Evidence](../../sources/notes/thabane2010tutorial.md#e10)
[^thabane2010tutorial-e11]: Thabane et al. 2010, §5 Challenges and Misconceptions. [Evidence](../../sources/notes/thabane2010tutorial.md#e11)
[^thabane2010tutorial-e12]: Thabane et al. 2010, §8 Ethical Aspects of Pilot Studies. [Evidence](../../sources/notes/thabane2010tutorial.md#e12)
[^tcps2022ethical-e1]: Canada's Tri-Council Policy Statement, 2022 edition, Chapter 2, Article 2.1. [Evidence](../../sources/notes/tcps2022ethical.md#e1)
[^tcps2022ethical-e3]: Canada's Tri-Council Policy Statement, 2022 edition, Chapter 6, Article 6.11. [Evidence](../../sources/notes/tcps2022ethical.md#e3)
[^tcps2022ethical-e4]: Canada's Tri-Council Policy Statement, 2022 edition, Chapter 6, Article 6.11 Pilot Studies. [Evidence](../../sources/notes/tcps2022ethical.md#e4)
[^tcps2022ethical-e5]: Canada's Tri-Council Policy Statement, 2022 edition, Chapter 6, Article 6.12. [Evidence](../../sources/notes/tcps2022ethical.md#e5)
[^lakens2022sample-e4]: Lakens 2022, What is the Expected Effect Size? [Evidence](../../sources/notes/lakens2022sample.md#e4)
[^perciedusert2020reporting-e36]: Percie du Sert et al. 2020, Box 3. [Evidence](../../sources/notes/perciedusert2020reporting.md#e36)
[^curtis2018experimental-e11]: Curtis et al. 2018, Flexibility and pilot data. [Evidence](../../sources/notes/curtis2018experimental.md#e11)
[^he2020characterizing-e9]: He et al. 2020 (code clones in Ethereum smart contracts), §4.3 Similarity Comparison, pp. 9–10. [Evidence](../../sources/notes/he2020characterizing.md#e9)
[^feist2019slither-e11]: Feist et al. 2019 (Slither, a static analysis tool for smart contracts), §V-A5 Experiment 2, p. 6. [Evidence](../../sources/notes/feist2019slither.md#e11)
[^durieux2020empirical-e8]: Durieux et al. 2020 (SmartBugs evaluation of smart contract analysis tools), §2.3.2 sbwild, p. 4. [Evidence](../../sources/notes/durieux2020empirical.md#e8)
[^rameder2022review-e5]: Rameder et al. 2022 (systematic review of vulnerability analysis for Ethereum smart contracts), §2.1.1 Initial Search, pp. 2–3. [Evidence](../../sources/notes/rameder2022review.md#e5)
