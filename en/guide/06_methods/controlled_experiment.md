# Controlled experiments: comparing the effect of tools or methods on people

This page covers **controlled experiments with human participants**: the researcher deliberately changes one factor (for example, which debugging tool developers use), randomly assigns participants to groups, keeps everything else as similar as possible, and compares how that factor affects people's performance.

If what you are comparing is the software system, tool, or model itself, which can run automatically and be measured repeatedly without people, see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md). If you have built a new tool and want to know how the paper as a whole should evaluate it, start with [Engineering research](../07_fields/computer-science/practices/engineering_research.md); an experiment with people is only one of the ways to evaluate it. Statistical testing in general is covered in [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md) and validity in [Validity and limitations](../02_do-the-project/04_validity-and-limits.md); this page does not repeat them.

**Scope** `[Our analysis]`: the standards and examples on this page come mainly from software engineering. They are based on the ACM SIGSOFT Empirical Standards (the empirical research standards of the Association for Computing Machinery's Special Interest Group on Software Engineering; "the SIGSOFT standard" below), Ko et al.'s guide to experiments with software tools, and the software engineering debates about students versus professionals and about sampling. If you run controlled experiments in another field, read your own field's standards first. Method pages from other fields you can compare with: [Randomized controlled trials](randomized_controlled_trial.md) for medical interventions, and [Field experiments](field_experiment.md) that randomize in the real world in partnership with governments or companies.

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Building and improving](../05_research-strategies/build_improve.md).

**After reading this page, you should be able to:**

- judge whether your question can be answered with a controlled experiment;
- write hypotheses, define variables, and choose between a between-subjects and a within-subjects design;
- work out whom to recruit, how many, what tasks to set, and what to measure, and test the design with a pilot study;
- check your own experiment against the checklist at the end.

---

## 1. What this kind of research is and when to use it

The SIGSOFT standard defines an experiment as deliberately introducing an intervention under controlled conditions and observing its effect on some aspect of reality[^ralph2020empirical-e162]. Its standard for experiments with human participants applies to studies that meet four conditions at once: they manipulate one or more **independent variables** (factors the researcher deliberately changes), control many **extraneous variables** (factors that might affect the outcome but are not what is being studied), apply each treatment to several participants, and involve people[^ralph2020empirical-e163].

**It is good at causal questions.** For example: "Do developers locate bugs faster with the new debugging tool?" By isolating variables through control, a controlled experiment can show better than other methods that a difference comes from the tool and not from other factors such as developer experience. The price is a fairly artificial setting[^ko2015practical-e2].

**It is not good at "how" and "why" questions.** How developers use the tool, which concepts they need to understand, how long it takes to learn: experiments struggle with these because experiments are fundamentally about comparison. Non-experimental quantitative or qualitative methods suit them better. And you often need answers to these questions first, before you know what the experiment should compare, which tasks to use, and what to measure[^ko2015practical-e1].

**How it differs from related methods** `[Our analysis]`:

| | Controlled experiment | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | [Questionnaire surveys](questionnaire_survey.md) | Field deployment / [case study](case_study.md) |
|---|---|---|---|---|
| What is studied | How people perform under some treatment | The system or model itself | People's views and experiences | People and tools in a real setting |
| What the researcher does | Manipulates variables, randomizes groups | Runs and measures automatically | Asks questions | Observes, with little control |
| Typical question | "Are people faster with tool A?" | "Is system A faster than B?" | "What do developers think of tool A?" | "What happened after the team adopted tool A?" |

**True experiments and quasi-experiments.** An experiment that randomly assigns participants to groups is a true experiment; one without random assignment is a quasi-experiment[^ralph2020empirical-e164]. A quasi-experiment is appropriate only in two situations: as a preliminary study, or when group assignment is out of your control (for example, students already split into two sections of a course). Simply saying "this study is exploratory" is not enough to justify not randomizing[^ralph2020empirical-e182].

**Not only software engineering.** The SIGSOFT standard targets software engineering, but the same method is used in user studies in human-computer interaction and in usability studies in security (for example, comparing two security warning designs). Outside computer science, education research comparing how two teaching methods affect student grades, and psychology comparing how two interfaces or ways of explaining something affect people's judgments, follow the same logic. But each field has its own conventions, terminology, and reporting standards. The steps below are written from the software engineering sources; when you apply them in another field, check them against that field's standards. `[Our analysis]`

---

## 2. How to do it

A typical design: one group uses a baseline tool, the other uses your tool, and **apart from which tool they use, every participant gets exactly the same materials, instructions, tasks, and environment**. Only then, if the groups' results differ, can you argue convincingly that the tool caused the difference[^ko2015practical-e3]. Every step below serves this goal.

A practical starting point: draft your ethics review application and the methods section of the paper first, and treat them as a design draft. This helps you spot details you haven't thought through yet[^ko2015practical-e4].

### Step 1: Write hypotheses and define variables

**How:**

- **Write formal hypotheses**, for example "Developers using tool A and developers using tool B take different amounts of time to fix the same set of bugs." Use a **two-tailed hypothesis** by default (it says only "different", without assuming a direction); if you want a one-tailed hypothesis ("A is faster"), justify it from previous research[^ralph2020empirical-e165].
- **Specify three kinds of variables**[^ralph2020empirical-e166]:
  - Independent variables: what you manipulate and how (for example, tool A / tool B);
  - Dependent variables: what you measure, in what units and with what instrument, and why you measure it that way (for example, time in minutes);
  - Extraneous variables: what else might affect the outcome (for example, programming experience), and whether you control it through the design, control it statistically, or leave it uncontrolled.
- **Preregister if you can**: publicly archive your hypotheses and design before the experiment starts[^ralph2020empirical-e176].

**Why:** in a confirmatory experiment, the hypotheses must be fixed before you see the data. SIGSOFT lists both hypothesizing after the results are known (HARKing) and reporting only the significant tests (p-hacking) as antipatterns[^ralph2020empirical-e27]. For the difference between exploratory and confirmatory research, see [Be clear whether you are testing or exploring](../02_do-the-project/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring).

**Where people go wrong:** using a poor proxy as the dependent variable, such as using completion time to stand for how complex a task is[^ralph2020empirical-e180].

### Step 2: Choose a design: between-subjects or within-subjects

| | Between-subjects design | Within-subjects design |
|---|---|---|
| How it works | Each person uses only one tool; groups are randomized | Each person uses every tool in turn, on different tasks[^ko2015practical-e17] |
| Advantages | No learning effects; less time per person `[Our analysis]` | More data from the same number of people; individual differences cancel out `[Our analysis]` |
| Risks | Large individual differences, so more people are needed | Learning effects, fatigue, and boredom[^ko2015practical-e18][^ko2015practical-e19] |

**Between-subjects designs: randomize.** Random assignment spreads differences in participants' skills and habits evenly across groups, making it less likely that a difference between groups really comes from the people rather than the tool[^ko2015practical-e16]. The paper must say how randomization was done, for example how the random numbers were generated. If you don't randomize, give a strong reason and explain how you mitigated the threat that the groups were different to begin with, for example with pretests and posttests, or by matching participants on ability[^ralph2020empirical-e169].

**Within-subjects designs: always counterbalance.** What participants learn in the first task helps them in the second; this is a learning effect. So randomize the order of the tasks and which task is done with your tool. When comparing three or more tools, you can use a Latin square (an arrangement in which each treatment appears equally often in each position in the order)[^ko2015practical-e18].

**Other designs**: for example, an interrupted time-series design measures before the tool is introduced, after it is introduced, and after it is taken away. It needs only one group and is closer to how a company would trial a tool `[Our analysis]`. But it gives weaker causal evidence, because it is hard to rule out other changes that happened while the tool was being introduced and removed[^ko2015practical-e20].

**Where people go wrong:** an analysis that doesn't match the design, for example using an independent-samples t-test on the paired data a within-subjects design produces[^ralph2020empirical-e181]. Decide on the test while you design the experiment `[Our analysis]`.

### Step 3: Decide on participants: whom to recruit, and how many

**Write the inclusion criteria first.** They should reflect the kind of people you believe will benefit from the tool and the work situations in which the tool will be useful[^ko2015practical-e6], for example "at least one year of Java experience, has not used this kind of tool". Word your recruitment materials and screening questions neutrally, so that applicants can't tell what the "right answer" is[^ko2015practical-e13]. Think first about which people you want your conclusions to generalize to[^baltes2022sampling-e11].

**Don't be your own participant.** In their literature review, Ko et al. found that 62% of tool evaluations were in fact the tool's inventors using it themselves and reporting their experience. That can show where the tool can be used, but not whether other people would benefit from it[^ko2015practical-e7].

**Students or professionals?** Neither is better in all cases[^falessi2018empirical-e1]. Some key points:

- **Describe participants by their experience rather than by a label.** The student/professional dichotomy doesn't work well: many students have internship or work experience[^falessi2018empirical-e2]. Falessi et al. recommend describing participants along three dimensions: real experience, relevant experience, and recent experience[^falessi2018empirical-e8].
- **Professionals are a convenience sample too** (a convenience sample is one chosen because it was easy to get, which weakens how far the conclusions generalize[^baltes2022sampling-e2]). The people you recruit at a company are not a random sample of all developers, and often not even a random sample of that company's developers[^falessi2018empirical-e4].
- **Students carry particular risks.** One example is the subject-expectancy effect: participants guess what the researcher hopes to see and act accordingly[^ko2015practical-e8]. You can reduce it by introducing the experiment in a way that doesn't reveal which outcome you care about[^ko2015practical-e9].
- **Think it through at the design stage, and write it into the paper.** If you plan to use a convenience sample, work out what population it represents[^falessi2018empirical-e5]; the paper should explain specifically why students are appropriate in the context of this experiment[^falessi2018empirical-e6].

> **Where sources disagree: if you can recruit professionals, should you try your hardest to?**
> - Falessi et al. argue that using students is a reasonable and necessary simplification in laboratory experiments[^falessi2018empirical-e1]. Professionals are hard to recruit; on one occasion only 33% of those who committed to take part actually showed up[^falessi2018empirical-e7].
> - In his commentary, Shepperd agrees that students are valuable for preliminary experiments, but argues that when the target population is some kind of professional, you should use professionals whenever feasible; "more trouble" is not a reason. He and his collaborators have run an experiment with more than 400 professionals[^shepperd2018inferencing-e4][^shepperd2018inferencing-e1]. He also points out that it is not only the participants you need to generalize from, but also the tasks and the setting[^shepperd2018inferencing-e2][^shepperd2018inferencing-e3].
>
> - The disagreement is smaller than it looks: Falessi et al. conclude that students can neither always nor never substitute for professional developers, and that it depends on the context and the population[^falessi2018empirical-e9]; Shepperd also acknowledges the value of students in preliminary experiments[^shepperd2018inferencing-e4].
>
> In practice: first ask yourself, "Whom should the conclusions generalize to?" If the target is novices or students, using students is natural. If the target is experienced professionals, you can pilot with students to refine the design, and try to get qualifying professionals for the main experiment. Whoever you use, describe participants by their experience and explain your reasoning. `[Our analysis]`

**How many people.** The SIGSOFT standard requires you to justify your sample size, for example with a **power analysis**[^ralph2020empirical-e167]: an advance estimate of how many people you need to have a good chance of detecting a difference if it really exists. It needs three inputs: the expected effect size, the expected variability of the results, and the acceptable Type I error rate (the false positive rate)[^ko2015practical-e11]. The first two can be estimated from data from earlier experiments or a pilot study[^ko2015practical-e12]. For reference, in the software engineering tool experiments Ko et al. reviewed, the median number of participants per group was 18; they suggest about 20 per group as a starting point, with no guarantee that it is enough[^ko2015practical-e10]. Under the SIGSOFT standard, when you run an experiment in a class with a fixed number of people, you can skip the advance power analysis[^ralph2020empirical-e179].

### Step 4: Design the tasks, materials, and training

**You have to trade realism against control.** The closer the setting is to real work, the further the conclusions generalize, but the less control you have and the harder it is to tell where a difference came from[^ko2015practical-e23]. You cannot maximize internal and external validity at the same time[^falessi2018empirical-e3].

- **Where the tasks come from**: designing them yourself from scratch lets you target the tool's features, but they may not resemble real work and may unfairly favor your tool[^ko2015practical-e24]. Selecting them from real projects (for example, bug reports from open-source projects) is closer to practice `[Our analysis]`.
- **Get the difficulty right**: if tasks are too easy, everyone finishes, giving a **ceiling effect**; if they are too hard, nobody finishes, giving a **floor effect**. Either way you can't see differences between tools[^ko2015practical-e25].
- **Experimental objects** (the programs or data participants work on): say whether they are real systems or toy systems, how large they are, and why you chose them. Don't give the control group and the treatment group different programs; otherwise the difference between programs is confounded with the difference between tools and the two can't be separated[^ralph2020empirical-e170].
- **Training**: whatever you teach in training becomes a precondition for "the conditions under which the tool is used", and the paper's conclusions hold only under that precondition[^ko2015practical-e21]. Note that short experiments inherently favor tools that can be learned quickly over tools that need long practice[^ko2015practical-e22].

**Where people go wrong:** tools meant for team collaboration are hard to evaluate with individual controlled experiments; none of the papers Ko et al. reviewed ran an experiment in a team setting[^ko2015practical-e34]. In that case, consider a field deployment or a case study. `[Our analysis]`

### Step 5: Decide how to measure

Ko et al. point out that **variation in outcome measures is the main reason experiments produce negative results**: the more variation, the harder it is to see a real difference. Some of that variation is natural and should be kept; what you need to eliminate is extraneous variation[^ko2015practical-e5]. The more clearly measurements are defined and the more consistently they are carried out, the less extraneous variation there is `[Our analysis]`.

- **Task success**: decide three things in advance: what state counts as success, how you will judge that it has been reached, and how you will explain the goal to participants so that everyone understands it the same way[^ko2015practical-e26].
- **Time**: time and success trade off against each other, since people can work fast and sloppily or slowly and carefully, so measure both[^ko2015practical-e27].
- **Subjective ratings**: don't just ask "Is this tool useful?" One study found that participants were 2.5 times more likely to prefer a technique they believed the interviewer had designed, even when that technique was worse[^ko2015practical-e28]. Use a validated questionnaire instead, such as the Technology Acceptance Model questionnaire[^ko2015practical-e29].
- **Collect background information after the tasks**: asking about experience before the tasks can lower the confidence of less experienced participants and affect their performance[^ko2015practical-e15].
- **Desirable attributes**: analyze whether your dependent variables really measure what you intend to measure; do a **manipulation check** to confirm that the treatment actually worked as intended (for example, that the treatment group really used the tool)[^ralph2020empirical-e176].

### Step 6: Run a pilot study first

**How:** before the main experiment, have a few people try it, with the aim of finding sources of extraneous variation[^ko2015practical-e31], such as confusing materials, bugs in the tool, or ambiguous tasks `[Our analysis]`. The researchers can do a first run-through themselves as participants[^ko2015practical-e33], but the most important round should, as far as possible, use the same kind of participants, location, materials, procedure, and experimenters as the main experiment[^ko2015practical-e32]. Fix what you find, then try again.

**Why:** of the 345 studies Ko et al. reviewed, only 11 mentioned running a pilot[^ko2015practical-e31]. Pilot data can also be used to estimate the values a power analysis needs[^ko2015practical-e12]. For general advice on preliminary studies, see [The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md).

**Where people go wrong:** merging pilot data into the main results. Pilot data should be discarded, because the setup was still changing[^ko2015practical-e32].

### Step 7: Handle ethics and informed consent

For the general requirements of research with people (risk assessment, informed consent, privacy protection, ethics review), see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md). Controlled experiments need extra attention to the following:

- **Hard tasks can hurt people too.** Especially difficult tasks, particularly for less experienced people, can cause stress and frustration[^ko2015practical-e14]. Debrief participants after the experiment so they don't leave feeling "I failed", and ask them not to share the answers, so later participants don't know them in advance[^ko2015practical-e30].
- **Watch for power relationships.** When recruiting through managers or instructors, explain how you ensured that participants consented freely[^ralph2020empirical-e186]. `[Our analysis]` Take particular care when recruiting in a class you teach: for example, have someone else collect the consent forms, and guarantee that taking part or not has no effect on grades.
- **Report incentives.** The paper must say whether participants were paid and with what[^ralph2020empirical-e171], and how coercion was avoided[^ralph2020empirical-e185].
- **If you use deception**, explain the reasons to participants afterwards and give them the chance to withdraw their data[^ralph2020empirical-e187].

### Step 8: Analyze and report

**Analysis**: report descriptive and inferential statistics suited to the distribution of your data, and explain why you chose those tests; report effect sizes and confidence intervals, not just "significant / not significant"[^ralph2020empirical-e172]. Plot the data distributions[^ralph2020empirical-e177]. For general statistical practice, see [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

**The report must state clearly**:

- who the participants were: age, gender, education, relevant experience, and so on[^ralph2020empirical-e172];
- the full design and procedure: each group's treatment, the materials, tasks, type of design, how groups were assigned, and how the sessions were run[^ralph2020empirical-e168];
- deviations between the execution and the design, and their effects, for example participants dropping out and upsetting the balance between groups[^ralph2020empirical-e175];
- validity: discuss construct, conclusion, internal, and external validity, and alternative explanations of the results[^ralph2020empirical-e173]. **For each threat, explain how it affects the results**; merely listing threats is an antipattern[^ralph2020empirical-e52];
- publish the task materials, de-identified raw data, and analysis scripts[^ralph2020empirical-e174].

**Where people go wrong:** overstating how representative the sample is[^baltes2022sampling-e8]; or admitting sampling bias in the limitations and then writing the conclusion as if the results were nearly universal[^baltes2022sampling-e9].

---

## 3. Checklist

This follows mainly the SIGSOFT standard for experiments with human participants, which is a review standard for software engineering; in other fields, your own field's standards take precedence `[Our analysis]`.

**Essential**

- [ ] Write formal hypotheses; use two-tailed hypotheses, or justify one-tailed ones[^ralph2020empirical-e165]
- [ ] Specify the independent, dependent, and extraneous variables, and how each is manipulated, measured, or controlled[^ralph2020empirical-e166]
- [ ] Justify the sample size[^ralph2020empirical-e167]
- [ ] Describe the design and procedure, including tasks, materials, group assignment, and how sessions were run[^ralph2020empirical-e168]
- [ ] Randomize and explain how, or give a strong reason for not randomizing and the mitigations used[^ralph2020empirical-e169]
- [ ] Describe and justify the choice of experimental objects, and acknowledge confounding between objects and treatments[^ralph2020empirical-e170]
- [ ] State whether participants were given incentives[^ralph2020empirical-e171]
- [ ] Describe the participants; report appropriate statistics, effect sizes, and confidence intervals[^ralph2020empirical-e172]
- [ ] Discuss the four kinds of validity and alternative explanations of the results[^ralph2020empirical-e173]
- [ ] State the risks, recruitment method, compensation, and informed consent (ethics supplement)[^ralph2020empirical-e68][^ralph2020empirical-e185]

**Desirable**

- [ ] Publish the full procedure, task materials, de-identified data, and analysis scripts[^ralph2020empirical-e174]
- [ ] Report deviations between execution and design and their effects[^ralph2020empirical-e175]
- [ ] Analyze the construct validity of the dependent variables; report manipulation checks; preregister hypotheses and design[^ralph2020empirical-e176]
- [ ] Discuss alternative designs you didn't use; plot the data distributions[^ralph2020empirical-e177]

**Extraordinary**

- [ ] Run several experiments or replications across cultures or regions; collect data with several methods for triangulation[^ralph2020empirical-e178]

**Acceptable deviations (not flaws)**

- Skipping the advance power analysis when running an experiment in a class with a fixed number of people[^ralph2020empirical-e179]

**Common reviewer criticisms that are not valid** (as listed in the SIGSOFT standard, for software engineering submissions): you don't need to worry about these, but do explain your choices in the paper

- "The participants are students": whether that is appropriate depends on the context, the degree of control needed, and the technology being evaluated, and the paper must justify it[^ralph2020empirical-e183]
- "Low external validity", "This is just a replication", "You should have used a different method", "Too few participants (without a power analysis to back it up)", "No incentive scheme was used"[^ralph2020empirical-e184]

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| The tool's authors act as participants | It can't show whether other people would benefit[^ko2015practical-e7] |
| Using students just because it's convenient and thinking about representativeness only afterwards | The population and validity need to be thought through at the design stage[^falessi2018empirical-e5] |
| The two groups get different programs or tasks | Objects and treatments are confounded, so you can't tell where a difference comes from[^ralph2020empirical-e170] |
| No counterbalancing in a within-subjects design | Learning effects get mistaken for the tool's effect[^ko2015practical-e18] |
| Tasks too easy or too hard | Ceiling or floor effects hide any difference[^ko2015practical-e25] |
| Only asking "Is the tool useful?" | Participants tend to please the researcher[^ko2015practical-e28] |
| No pilot study | Problems with materials, tasks, or the tool show up only in the main experiment, creating a lot of extraneous variation[^ko2015practical-e31] |
| Using an independent-samples test on paired data | The analysis doesn't match the design[^ralph2020empirical-e181] |
| Merely listing threats to validity | Readers can't tell how they affect the results[^ralph2020empirical-e52] |

---

## 5. Further reading

- **How to actually design and run a tool experiment**: Ko, LaToza & Burnett 2015. Goes through recruitment, informed consent, training, task design, measurement, and piloting, giving the options for each with their pros and cons. Most of the practical advice on this page comes from here.
- **What standards reviewers use**: the standard for experiments with human participants and the ethics supplement in the SIGSOFT empirical standards. The end of the standard also lists recommended reading on experimental design, crossover designs, statistical methods, participant incentives, and more.
- **Students or professionals**: Falessi et al. 2018 and Shepperd's 2018 commentary; both sides' arguments are worth reading.
- **Sampling and representativeness**: Baltes & Ralph 2022.

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e162]: SIGSOFT Experiments (with human participants) standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e162)
[^ralph2020empirical-e163]: SIGSOFT Experiments (with human participants) standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e163)
[^ralph2020empirical-e164]: SIGSOFT Experiments (with human participants) standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e164)
[^ralph2020empirical-e165]: SIGSOFT Experiments (with human participants) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e165)
[^ralph2020empirical-e166]: SIGSOFT Experiments (with human participants) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e166)
[^ralph2020empirical-e167]: SIGSOFT Experiments (with human participants) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e167)
[^ralph2020empirical-e168]: SIGSOFT Experiments (with human participants) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e168)
[^ralph2020empirical-e169]: SIGSOFT Experiments (with human participants) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e169)
[^ralph2020empirical-e170]: SIGSOFT Experiments (with human participants) standard, Essential Attributes and footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e170)
[^ralph2020empirical-e171]: SIGSOFT Experiments (with human participants) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e171)
[^ralph2020empirical-e172]: SIGSOFT Experiments (with human participants) standard, Essential Attributes (results). [Evidence](../../sources/notes/ralph2020empirical.md#e172)
[^ralph2020empirical-e173]: SIGSOFT Experiments (with human participants) standard, Essential Attributes (discussion). [Evidence](../../sources/notes/ralph2020empirical.md#e173)
[^ralph2020empirical-e174]: SIGSOFT Experiments (with human participants) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e174)
[^ralph2020empirical-e175]: SIGSOFT Experiments (with human participants) standard, Desirable Attributes and footnote 3. [Evidence](../../sources/notes/ralph2020empirical.md#e175)
[^ralph2020empirical-e176]: SIGSOFT Experiments (with human participants) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e176)
[^ralph2020empirical-e177]: SIGSOFT Experiments (with human participants) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e177)
[^ralph2020empirical-e178]: SIGSOFT Experiments (with human participants) standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e178)
[^ralph2020empirical-e179]: SIGSOFT Experiments (with human participants) standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e179)
[^ralph2020empirical-e180]: SIGSOFT Experiments (with human participants) standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e180)
[^ralph2020empirical-e181]: SIGSOFT Experiments (with human participants) standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e181)
[^ralph2020empirical-e52]: SIGSOFT Experiments (with human participants) standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e52)
[^ralph2020empirical-e182]: SIGSOFT Experiments (with human participants) standard, footnote 5. [Evidence](../../sources/notes/ralph2020empirical.md#e182)
[^ralph2020empirical-e183]: SIGSOFT Experiments (with human participants) standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e183)
[^ralph2020empirical-e184]: SIGSOFT Experiments (with human participants) standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e184)
[^ralph2020empirical-e68]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e68)
[^ralph2020empirical-e185]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e185)
[^ralph2020empirical-e186]: SIGSOFT Ethics (Studies with Human Participants) Supplement, footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e186)
[^ralph2020empirical-e187]: SIGSOFT Ethics (Studies with Human Participants) Supplement, footnote 7. [Evidence](../../sources/notes/ralph2020empirical.md#e187)
[^ralph2020empirical-e27]: SIGSOFT General Standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e27)
[^ko2015practical-e1]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e1)
[^ko2015practical-e2]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e2)
[^ko2015practical-e3]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e3)
[^ko2015practical-e4]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e4)
[^ko2015practical-e5]: Ko et al. 2015, §2. [Evidence](../../sources/notes/ko2015practical.md#e5)
[^ko2015practical-e6]: Ko et al. 2015, §3.1. [Evidence](../../sources/notes/ko2015practical.md#e6)
[^ko2015practical-e7]: Ko et al. 2015, §3.1. [Evidence](../../sources/notes/ko2015practical.md#e7)
[^ko2015practical-e8]: Ko et al. 2015, §3.1. [Evidence](../../sources/notes/ko2015practical.md#e8)
[^ko2015practical-e9]: Ko et al. 2015, §3.1. [Evidence](../../sources/notes/ko2015practical.md#e9)
[^ko2015practical-e10]: Ko et al. 2015, §3.2. [Evidence](../../sources/notes/ko2015practical.md#e10)
[^ko2015practical-e11]: Ko et al. 2015, §3.2. [Evidence](../../sources/notes/ko2015practical.md#e11)
[^ko2015practical-e12]: Ko et al. 2015, §3.2. [Evidence](../../sources/notes/ko2015practical.md#e12)
[^ko2015practical-e13]: Ko et al. 2015, §3.3. [Evidence](../../sources/notes/ko2015practical.md#e13)
[^ko2015practical-e14]: Ko et al. 2015, §4.1. [Evidence](../../sources/notes/ko2015practical.md#e14)
[^ko2015practical-e15]: Ko et al. 2015, §4.2. [Evidence](../../sources/notes/ko2015practical.md#e15)
[^ko2015practical-e16]: Ko et al. 2015, §4.3. [Evidence](../../sources/notes/ko2015practical.md#e16)
[^ko2015practical-e17]: Ko et al. 2015, §4.3. [Evidence](../../sources/notes/ko2015practical.md#e17)
[^ko2015practical-e18]: Ko et al. 2015, §4.3. [Evidence](../../sources/notes/ko2015practical.md#e18)
[^ko2015practical-e19]: Ko et al. 2015, §4.3. [Evidence](../../sources/notes/ko2015practical.md#e19)
[^ko2015practical-e20]: Ko et al. 2015, §4.3. [Evidence](../../sources/notes/ko2015practical.md#e20)
[^ko2015practical-e21]: Ko et al. 2015, §4.4. [Evidence](../../sources/notes/ko2015practical.md#e21)
[^ko2015practical-e22]: Ko et al. 2015, §4.4. [Evidence](../../sources/notes/ko2015practical.md#e22)
[^ko2015practical-e23]: Ko et al. 2015, §5. [Evidence](../../sources/notes/ko2015practical.md#e23)
[^ko2015practical-e24]: Ko et al. 2015, §5.3. [Evidence](../../sources/notes/ko2015practical.md#e24)
[^ko2015practical-e25]: Ko et al. 2015, §5.5. [Evidence](../../sources/notes/ko2015practical.md#e25)
[^ko2015practical-e26]: Ko et al. 2015, §6.1. [Evidence](../../sources/notes/ko2015practical.md#e26)
[^ko2015practical-e27]: Ko et al. 2015, §6.2. [Evidence](../../sources/notes/ko2015practical.md#e27)
[^ko2015practical-e28]: Ko et al. 2015, §6.3. [Evidence](../../sources/notes/ko2015practical.md#e28)
[^ko2015practical-e29]: Ko et al. 2015, §6.3. [Evidence](../../sources/notes/ko2015practical.md#e29)
[^ko2015practical-e30]: Ko et al. 2015, §7. [Evidence](../../sources/notes/ko2015practical.md#e30)
[^ko2015practical-e31]: Ko et al. 2015, §8. [Evidence](../../sources/notes/ko2015practical.md#e31)
[^ko2015practical-e32]: Ko et al. 2015, §8. [Evidence](../../sources/notes/ko2015practical.md#e32)
[^ko2015practical-e33]: Ko et al. 2015, §8. [Evidence](../../sources/notes/ko2015practical.md#e33)
[^ko2015practical-e34]: Ko et al. 2015, §3.1. [Evidence](../../sources/notes/ko2015practical.md#e34)
[^falessi2018empirical-e1]: Falessi et al. 2018, Abstract. [Evidence](../../sources/notes/falessi2018empirical.md#e1)
[^falessi2018empirical-e2]: Falessi et al. 2018, §4.1.1. [Evidence](../../sources/notes/falessi2018empirical.md#e2)
[^falessi2018empirical-e3]: Falessi et al. 2018, §4.1.2. [Evidence](../../sources/notes/falessi2018empirical.md#e3)
[^falessi2018empirical-e4]: Falessi et al. 2018, §4.1.3. [Evidence](../../sources/notes/falessi2018empirical.md#e4)
[^falessi2018empirical-e5]: Falessi et al. 2018, §6.2. [Evidence](../../sources/notes/falessi2018empirical.md#e5)
[^falessi2018empirical-e6]: Falessi et al. 2018, §6.2. [Evidence](../../sources/notes/falessi2018empirical.md#e6)
[^falessi2018empirical-e7]: Falessi et al. 2018, §4.2.1. [Evidence](../../sources/notes/falessi2018empirical.md#e7)
[^falessi2018empirical-e8]: Falessi et al. 2018, §7. [Evidence](../../sources/notes/falessi2018empirical.md#e8)
[^falessi2018empirical-e9]: Falessi et al. 2018, §9. [Evidence](../../sources/notes/falessi2018empirical.md#e9)
[^shepperd2018inferencing-e1]: Shepperd 2018, §2. [Evidence](../../sources/notes/shepperd2018inferencing.md#e1)
[^shepperd2018inferencing-e2]: Shepperd 2018, §3. [Evidence](../../sources/notes/shepperd2018inferencing.md#e2)
[^shepperd2018inferencing-e3]: Shepperd 2018, §4. [Evidence](../../sources/notes/shepperd2018inferencing.md#e3)
[^shepperd2018inferencing-e4]: Shepperd 2018, §5. [Evidence](../../sources/notes/shepperd2018inferencing.md#e4)
[^baltes2022sampling-e2]: Baltes & Ralph 2022, §2.1.1. [Evidence](../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e11]: Baltes & Ralph 2022, §6. [Evidence](../../sources/notes/baltes2022sampling.md#e11)
[^baltes2022sampling-e8]: Baltes & Ralph 2022, §6. [Evidence](../../sources/notes/baltes2022sampling.md#e8)
[^baltes2022sampling-e9]: Baltes & Ralph 2022, §6. [Evidence](../../sources/notes/baltes2022sampling.md#e9)
