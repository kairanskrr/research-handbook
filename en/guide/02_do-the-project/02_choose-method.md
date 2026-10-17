# Choosing a method

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. Almost all the sources cited here come from the research-methods literature of software engineering: a guide to choosing methods (Easterbrook et al. 2008), a framework of research strategies (Storey et al. 2020), the empirical standards of ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering), and a tutorial on writing software engineering papers (Shaw 2003). They reflect the views and rules of the software engineering community; in other fields, follow your own field's conventions.

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Write down your main strategy and check your evidence plan against the strategy page.** Compare the page's "what evidence is enough" section with your plan item by item, and add whatever is missing ([Section 1](#1-first-confirm-your-main-strategy)).
> 2. **Pick a method for each piece of evidence.** Copy your plan into three columns: evidence, what it asks, candidate method. For each method, ask: do I meet its preconditions? ([Section 2](#2-choose-a-method-for-each-piece-of-evidence))
> 3. **Say where your main method is strong, where it is weak, and why the weakness is acceptable.** If you can't give a reason it is acceptable, consider adding a method ([Section 3](#3-see-clearly-what-each-method-gains-and-what-it-gives-up), [Section 4](#4-combine-methods-when-you-need-to)).
> 4. **Check, row by row, that the method can really get the evidence.** For each row, write one sentence: which cell of the results table the output fills, and whether you can get what you need. If a row fails, deal with it first ([Section 5](#5-check-can-this-method-really-get-the-evidence-you-need)).
> 5. **Read the method guidance before you start.** For each method, find one method page or guideline and two or three papers to compare against, and learn what standard your target community judges it by ([Section 6](#6-before-you-start-read-method-guides-and-learn-your-fields-conventions)).
>
> **Done these? Move on:** every row of your evidence–method table has a method and has passed the checks, and your advisor has seen it and raised no fundamental objection. Next: [Writing a research plan](03_research-plan.md).

## Where you are

You have broken your central claim into several research questions and written an evidence plan (see [From research questions to an evidence plan](01_question-to-evidence.md)): one row per research question, saying how the key terms are defined, what result counts as support, and what counts against. At the end of Part 1 you also made a rough call on what kind of research you are doing (see [Decide what kind of research you are doing](../01_find-a-problem/05_converge.md#work-out-what-kind-of-study-you-are-doing)).

What the plan doesn't tell you yet is **how exactly you will get** each piece of evidence. You may be wondering:

- My advisor says "run an experiment". Does my question suit an experiment?
- Questionnaires, interviews, mining code repositories, running benchmarks: they all seem somewhat relevant. Which one do I pick?
- Is one method enough? Should I combine several?
- Once I have picked a method, how do I know it will actually give me the evidence I need?

## What this stage is for

For each piece of evidence, choose one (or more) **research methods**, and be able to say why. A research method is the concrete way you collect and analyze evidence; for how it differs from a research strategy, see [Key concepts](../00_start-here/key-concepts.md#research-methods). Concretely, answer these six questions:

1. What is my main research strategy, and what evidence does it require?
2. For each piece of evidence, which method will get it?
3. What does this method gain, and what does it give up?
4. Is one method enough? If I combine methods, how?
5. Can this method really produce the evidence I need?
6. Before I start, which method guide should I read, and which field conventions do I need to know?

## How to use this chapter

Go through Sections 2 to 5 **one row at a time** down your evidence plan, and put the results into an "evidence–method table" (see "What you should have at the end").

The steps also pull on each other:

- Section 5 shows that no method can get a certain piece of evidence → go back to [From research questions to an evidence plan](01_question-to-evidence.md) and replace it with evidence you can get, or make the claim smaller.
- Section 3 shows that what your main method gives up is exactly what your claim needs most → go back to Section 2 and switch methods, or add a method in Section 4.

---

## 1. First confirm your main strategy

**The method follows the strategy, and the strategy follows the central claim.** You already settled on a provisional main strategy at the end of chapter 1.5. How to choose a main strategy from your central claim, and how to tell apart the pairs of strategies that are easy to confuse, is covered in the section "How to choose your main strategy" in [Research strategies](../05_research-strategies/README.md#how-to-pick-your-main-strategy); we won't repeat it here.

This section does just one thing: **use the strategy page to check your evidence plan.** Every strategy page has a section on "what evidence is enough", listing the evidence that strategy usually has to deliver. Go through it item by item and see whether anything is missing from your plan.

For example, your main strategy is [Building and improving](../05_research-strategies/build_improve.md), yet your plan has no "comparison with existing methods"; or your main strategy is [Causal explanation](../05_research-strategies/explain_causality.md), yet your plan has no "ruling out alternative explanations". Fill these gaps first; otherwise, however well you choose your methods, they won't add up to a complete argument `[Our analysis]`.

The eight strategy pages are: [Description](../05_research-strategies/observe_describe.md), [Measurement](../05_research-strategies/measure.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Causal explanation](../05_research-strategies/explain_causality.md), [Building and improving](../05_research-strategies/build_improve.md), [Synthesis](../05_research-strategies/synthesize.md), [Proof](../05_research-strategies/prove.md), and [Interpretation and argument](../05_research-strategies/interpret_argue.md). Section 3 of each also lists the methods commonly used with that strategy, which makes a good starting point for the next section.

**Write it down:** Your central claim and main strategy. Open the matching strategy page, compare its "what evidence is enough" section with your evidence plan item by item, and add any evidence you missed.

## 2. Choose a method for each piece of evidence

**Go through the evidence one piece at a time and ask: what kind of question does this piece of evidence answer?** The method has to fit the question. The software engineering guide to choosing methods sums it up this way: any question can be studied with several methods, and which one you choose depends on your stance (what kind of evidence you consider credible), the resources available to you, and how well the method fits the question[^easterbrook2008selecting-e76].

The table below lists methods to consider, organized by "what the evidence is asking". The last column gives the preconditions for doing that kind of study; **if the preconditions aren't met, don't choose that method for now.** The preconditions with footnotes come from the guide above; the categories, which method goes where, and the preconditions without footnotes are this handbook's own summary `[Our analysis]`:

| This evidence asks… | Methods to consider (where they currently live) | Preconditions |
|---|---|---|
| How common a practice or opinion is in a group of people | [Questionnaire surveys](../06_methods/questionnaire_survey.md) | The question targets a clearly defined group of people; you can draw a representative sample from a well-defined population[^easterbrook2008selecting-e81] |
| Distributions or associations across large amounts of code, commits, or contracts | [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md), [Data science](../06_methods/data_science.md) | The data is available, and the unit of analysis is clearly defined |
| How and why things happen in a real-world setting | [Case studies](../06_methods/case_study.md), [Interview studies](../06_methods/interview_study.md), [Grounded theory](../06_methods/grounded_theory.md) | You have a clear "how" or "why" research question[^easterbrook2008selecting-e12]; you can get access to the field site |
| A group's working culture and how its members make sense of what they do | Ethnography; see Section 3 of [Case studies](../06_methods/case_study.md#3-how-ethnography-is-different) | The question focuses on the group's cultural practices, and you can get access to the group's members[^easterbrook2008selecting-e83] |
| Whether X causes Y; whether people do better with A than with B | [Controlled experiments](../06_methods/controlled_experiment.md) | You have a clear hypothesis[^easterbrook2008selecting-e78] |
| Which of several programs, tools, or models is better, under which conditions | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | You have objects to evaluate and metrics you can justify |
| Whether the thing you built is better | [Engineering research](../07_fields/computer-science/practices/engineering_research.md), [Optimization studies](../07_fields/computer-science/practices/optimization_study.md), [Quantitative simulation](../06_methods/simulation_study.md) | You have baselines to compare against |
| Studying a problem in a real organization while helping to solve it | [Action research](../06_methods/action_research.md) | There is a problem owner willing to define the problem with you and commit to solving it[^easterbrook2008selecting-e84] |
| How a phenomenon changes over time | [Longitudinal studies](../06_methods/longitudinal_study.md) | You can follow the same subjects at several points in time |
| Whether someone else's conclusion still holds under different conditions | [Replication studies](../06_methods/replication.md) | The original study's materials are detailed enough |
| What existing studies show when taken together | [Review studies](../06_methods/review_study.md), [Case survey](../06_methods/case_survey.md) | There are enough existing studies to be worth combining |
| That something must hold under given conditions | [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md) | You can write what you study as precise definitions |

Methods common in other fields (field experiments, randomized controlled trials, archival research, and so on) are also collected under [Research types](../06_methods/README.md); practices used in only one field (such as close reading of texts) are in the "Field-specific practices" section of [Fields](../07_fields/README.md#field-specific-practices).

Before you pick a method, also check the literature: some questions already have good answers that you can get just by reading, without running an empirical study of your own[^easterbrook2008selecting-e41].

**Walk through the example.** Back to the running example: the central claim is "published evaluations of large language model vulnerability detectors are inflated by data leakage", and the main strategy is Measurement. Take the evidence plan from the previous chapter and match each row with a candidate method `[Our analysis]`:

| Evidence | What it asks | Candidate method |
|---|---|---|
| How many contracts in the benchmark the models may have seen during training | How common | Data analysis: compare the benchmark against code the models may have seen |
| How accuracy changes before and after removing leaked samples | How much results differ between two conditions | Benchmarking: run the same set of tools on both versions of the benchmark |
| Whether only one or two tools are affected | Whether it generalizes | Benchmarking across several models and tools |
| Whether the way of judging "leaked or not" is itself accurate | Is the measurement reliable? | Manually check a sample and compare against the automatic judgments |

**Three easy mistakes:**

- **Choosing a method based on "what I know how to do" or "what others did".** Blindly copying a research paradigm that others used for a completely different problem can lead to a serious mismatch[^shaw2003writing-e15].
- **Chasing the "best" method.** The software engineering empirical standards only require the method to be appropriate for the study's purpose, not optimal[^ralph2020empirical-e23]. The guide above also says there is no fixed recipe for choosing a method; it depends on your resources, whether you can get access to the people or things you want to study, whether you can control the variables you want to study, and your own skills[^easterbrook2008selecting-e42].
- **Starting before the preconditions are met.** For example, rushing into an experiment before you can write down a clear hypothesis. At that point you are better off doing exploratory work first to get the hypothesis clear `[Our analysis]`.

**Write it down:** Copy your evidence plan into three columns: evidence, what it asks, candidate method. After each candidate method, add one sentence: do I meet its preconditions?

## 3. See clearly what each method gains and what it gives up

**No method is perfect.** A widely cited framework of research strategies in software engineering says that every research strategy has strengths and weaknesses on several quality criteria, and that every design decision is a trade-off between them[^storey2020who-e3]. The criteria are:

- **Generalizability**: whether the conclusions extend to more people or systems;
- **Realism**: how close to real use the setting is in which the evidence is collected;
- **Control**: whether you can control the human-behavior factors that would interfere with the evidence but aren't part of the study;
- **Precision**: how precise the system data you collect is.

The table below shows where several kinds of approach in this framework typically sit on these criteria[^storey2020who-e12][^storey2020who-e13][^storey2020who-e14][^storey2020who-e15]; the examples in the table are this handbook's own `[Our analysis]`:

| Approach | Computer science example | Strong on | Weak on |
|---|---|---|---|
| Lab experiment | Graduate students complete tasks in a lab using two debugging tools | Control | Realism (the setting is contrived), and harder to generalize |
| Field study | Observing, without intervening, how a company uses a tool | Realism | Control and generalizability (usually involves only a few companies) |
| Field experiment | Comparing two testing tools in developers' real working environment | Possibly more control than a field study | More intrusive than a field study, so less realism |
| Questionnaires, interviews | Asking many developers how they view code quality | Generalizability can be higher when the sample is broad and large | Realism: you can't see or anticipate what shapes each person's answers |
| Using existing data | Mining code repositories, or evaluating tools on historical data | Precision of system data; realism and generalizability can also be fairly high when the data comes from real settings and many projects | Little control over human behavior |

**The two trade-offs you will meet most often** `[Our analysis]`:

**Control versus realism.** The "cleaner" the experiment, the further it may be from reality. Once key variables are ignored or held fixed, the results may not carry over to real settings[^easterbrook2008selecting-e79]. And an experiment only confirms the **metric you defined**: in the guide's hypothetical example, even if a researcher's experiment shows that fish-eye views are more efficient as she defines efficiency, that doesn't show fish-eye views are better suited to navigation[^easterbrook2008selecting-e80]. In our example `[Our analysis]`: measuring how much leakage inflates results on one curated public benchmark doesn't mean the gap is just as large on other benchmarks or on contracts actually deployed. For how far a conclusion can generalize and how to guard against overreach in advance, see [Validity and limitations](04_validity-and-limits.md#5-external-validity-how-far-do-your-conclusions-reach).

**Depth versus breadth.** A questionnaire tells you what a group of people is like overall; if you want to understand in depth how people actually use something, or why they don't, a case study may be more suitable[^easterbrook2008selecting-e82]. Choosing a case study means trading representativeness for deeper understanding of a few cases[^easterbrook2008selecting-e19]. When the setting itself shapes the phenomenon, or the effects take a long time to show, the controlled experiment's approach of "break it down and isolate variables" doesn't fit, and a case study is more suitable[^easterbrook2008selecting-e16].

**How do you decide which to sacrifice? Look at which one your claim needs most** `[Our analysis]`. The running example makes a measurement claim using existing benchmark data, so precision matters most: the leakage judgments and the detection judgments have to be accurate. It says nothing about how people use the tools, so realism can give a little. If your claim is causal, say that giving vulnerability-pattern hints **causes** a higher detection rate, control matters most and realism can give a little. If your claim is that developers **will use** this tool in their actual work, realism matters most and control can give a little. Not every project needs to bring people in, either: for evaluating a new technique that shortens build times, human feedback adds little[^storey2020who-e6]; but a tool that recommends likely defects may need to be evaluated with real people using it, to see how it changes the setting it is used in[^storey2020who-e5].

> **Where sources disagree: are lab experiments the only credible evidence?**
>
> The software engineering guide to choosing methods describes this debate through a hypothetical scenario:
>
> - **One side**: the advisor insists that the only trustworthy evidence comes from experiments under controlled laboratory conditions[^easterbrook2008selecting-e85]. The reasoning is that controlled experiments can pin down the relationships between variables precisely, especially whether there is a causal relationship[^easterbrook2008selecting-e78].
> - **The other side**: another researcher in the scenario argues that lab experiments are useless because they ignore the messy complexity of real software projects[^easterbrook2008selecting-e85]. The research strategy framework also points out that control in the lab comes at the expense of realism, and the results are harder to generalize[^storey2020who-e13].
>
> The guide's explanation: the disagreement comes from different stances. The stance you adopt affects which methods you believe produce acceptable evidence; being explicit about your stance also helps when you talk and write about research[^easterbrook2008selecting-e86].
>
> This disagreement affects what you do `[Our analysis]`: first use the approach above to decide whether your claim needs control or realism more; then say in your paper what you chose and what you gave up. The software engineering empirical standards list "discusses alternative experimental designs and why they were not used (e.g. validity trade-offs)" as a desirable attribute[^ralph2020empirical-e177]. They also hold that criticizing an experiment merely because "the participants are students" is not valid: whether participants are appropriate should be judged against the context, the level of control needed, and the trade-off between internal and external validity, but the paper must explain why it made that choice[^ralph2020empirical-e183].

**Write it down:** Two sentences about your main method: which criterion it is strong on and which it is weak on, and why that weakness is acceptable for your claim. If you can't write a reason why it is acceptable, consider adding a method in Section 4.

## 4. Combine methods when you need to

**Why combine:** Every method has known flaws, but the flaws differ from method to method, so you can choose several that make up for each other[^easterbrook2008selecting-e1]. How reliable your results are depends on how well your study design compensates for the weaknesses of the methods you chose[^easterbrook2008selecting-e77].

**Three common ways to combine** (the three mixed-methods designs described in the software engineering guide to choosing methods):

| Design | How it works | When to use it |
|---|---|---|
| Quantitative first, then qualitative | Collect and analyze quantitative data first, then use qualitative results to explain the quantitative findings | Especially useful when the quantitative phase turns up unexpected results[^easterbrook2008selecting-e4] |
| Qualitative first, then quantitative | Collect and analyze qualitative data first, then use quantitative results to help interpret it | Also suits testing a preliminary theory that came out of qualitative work[^easterbrook2008selecting-e5] |
| At the same time, cross-checking | Use different methods at the same time to confirm and cross-validate each other | Motivated by the fact that what people say often differs from what they do[^easterbrook2008selecting-e6] |

The difficulty with running them at the same time is that the two analyses' results may be hard to compare, and contradictions may be hard to resolve; you may then need another source of evidence or a follow-up study[^easterbrook2008selecting-e7].

**Combining doesn't have to mean switching methods.** Even with a single method, you can use several data collection techniques that check each other; when different kinds of data support the same conclusion, the study is more convincing[^easterbrook2008selecting-e9]. Using different strategies or methods is called methodological triangulation; using the same method with different data sources is called data triangulation[^storey2020who-e7]. Data triangulation may improve generalizability but does not improve realism[^storey2020who-e8]; for more, see [Validity and limitations](04_validity-and-limits.md#5-external-validity-how-far-do-your-conclusions-reach).

In our example `[Our analysis]`: using automatic matching to decide "which samples leaked" and then manually checking a sample of them is data triangulation within one study. To show that "developers are actually misled by inflated results", you would need a different method, such as interviews or a controlled experiment.

**Combining has costs.** It means collecting a lot of data, analyzing several sources takes a lot of time, and the researcher has to be familiar with both quantitative and qualitative research[^easterbrook2008selecting-e3]. So `[Our analysis]`:

- **As a beginner, you can do one method well first.** In the general section of the software engineering empirical standards, "applies two or more data collection or analysis strategies to the same research question" is an extraordinary attribute, not an essential one[^ralph2020empirical-e290]. And the responsibility for triangulation doesn't have to sit with a single paper[^storey2020who-e10].
- **If you combine methods, say clearly why, in which phase, and what each one does.** The same standards list these as essential for multi-method research[^ralph2020empirical-e276].
- **Don't add a method for show.** Overselling a study as mixed methods when one of the methods makes only a token contribution, or adding a method to please a reviewer that contributes nothing substantial to the findings: the same standards list these as antipatterns[^ralph2020empirical-e282].

For how to design and integrate multiple methods, see [Mixed methods](../06_methods/mixed_methods.md).

**Write it down:** In your evidence–method table, mark which pieces of evidence rely on a single method and what that method's biggest weakness is. Only for the one or two where the weakness hits your claim directly, write down the additional method and what it contributes.

## 5. Check: can this method really get the evidence you need?

Choosing a method that is "on the right track" isn't enough. Before you start, run these checks on every row of evidence `[Our analysis]`:

**① Can the method's output go into your results table?** Take out the [empty results table](../01_find-a-problem/05_converge.md#4-what-will-make-people-believe-it) you drew in chapter 1.5, imagine what the method will produce when it's done, and see whether that fits in the cell. The validation has to match the claim: if you claim better performance, analyze performance, not ease of use or generality[^shaw2003writing-e12]. The kind of validation also has to match the type of result and how it was obtained: a formal model needs rigorous derivation and proof, not one or two simple examples[^shaw2003writing-e9].

**② Does the method measure the thing you need?** A questionnaire can only tell you what people **say** they do, which may have nothing to do with what they actually do[^easterbrook2008selecting-e52]. Analyzing only the trace data left by development activity (such as commit histories) shows you only part of people's behavior, intentions, and social interactions[^storey2020who-e1]. If your evidence is about "what people actually do", switch methods or add another source.

**③ Can you get what you need?** In the example, the most direct way to get the evidence "how many benchmark samples the models have seen" is to compare against the models' training data. If the training data isn't public, that method won't work, and you need different evidence or a different approach, such as using only models with public training data, or only contracts that appeared after the model was released. If you do research inside companies, also consider that getting access to the field site may take a long time spent building a relationship before they will share specific project data[^easterbrook2008selecting-e25]; in exchange for access you usually have to give up some control, and getting permission to publish can also be hard[^easterbrook2008selecting-e26].

**④ Do you have the time and the skills?** Mainly quantitative methods, such as controlled experiments and questionnaire surveys, need more planning time than purely qualitative methods, and the statistical tests have to be decided in advance[^easterbrook2008selecting-e88]. If this is your first time using a method, count the time to learn it; see Section 6.

**⑤ Try it small first.** Beginners should usually pilot their data collection instruments first, and pilot not just the collection but the analysis steps too[^easterbrook2008selecting-e89]. For how to plan such a small trial run, see [The smallest version that runs end to end](05_pilot-and-derisk.md).

Practical constraints will often force you to change your original design, including the method, the data collection, and the analysis steps. When you change it, record the original plan and every change made afterward[^easterbrook2008selecting-e87].

**Write it down:** Add a "check result" column to your evidence–method table. For each row write one sentence: which cell the method's output fills, and whether you can get what you need. If any row fails, deal with that row before moving on.

## 6. Before you start, read method guides and learn your field's conventions

**First read the existing guidelines for this kind of study.** The software engineering empirical standards list "attempting a study without reading, understanding and applying published guidelines for that kind of study" as an antipattern[^ralph2020empirical-e26]. If you use an analysis technique, follow that technique's rules[^shaw2003writing-e13]. Beginners need to get familiar with the techniques they choose and know the pitfalls they may run into[^easterbrook2008selecting-e89]; before actually using them, you may need further study or even dedicated training[^easterbrook2008selecting-e90].

**What order to look in** `[Our analysis]`:

1. The matching method page in this handbook (the links in the table in Section 2), to learn the steps and common mistakes first;
2. The method guides or standards listed under "Further reading" on that page, to use as a reference when you design the study for real;
3. Three to five papers from the last two or three years at the conference or journal you plan to submit to, with claims similar to yours: see which methods they used and what they reported. Use them only for comparison; don't copy them (see Section 2).

**What if there is no dedicated guideline?** The software engineering empirical standards put it this way: apply a dedicated standard if a suitable one exists; if not, follow published guidance; if there is no suitable guidance either, reviewers apply the general standard and build an ad hoc evaluation scheme for the new method[^ralph2020empirical-e441]. For you, this means stating clearly in your paper what standard you are using to judge whether your study was done well `[Our analysis]`.

**Why you can't skip this:** The same standards say explicitly that there are no universal quality criteria; each study is judged by the criteria appropriate to its method[^ralph2020empirical-e24] (for the strategy-level explanation, see [Key concepts](../00_start-here/key-concepts.md#research-strategy)). If you don't know what standard your method is judged by, you won't know how far you need to go, nor how to respond to reviews that apply the wrong standard `[Our analysis]`. The standards also list these reviewer criticisms as invalid: criticizing a study by the norms of a different research paradigm, criticizing limitations intrinsic to that kind of study (such as attacking a case study for low generalizability), and rejecting a study just because the reviewer would have used a different method[^ralph2020empirical-e25].

**Then look at field conventions.** Method guides tell you "how to do it well"; field conventions tell you "what this community accepts". At a minimum, find out `[Our analysis]`:

| What to find out | Where to look |
|---|---|
| Which methods and kinds of evaluation are customary in your research area | [Computer science field overview](../07_fields/computer-science/README.md#conventions-differ-across-research-areas) |
| Whether you are expected to submit reproducible code and data | [Artifact evaluation and badges](../07_fields/computer-science/README.md#artifact-evaluation-and-badges) |
| What ethical requirements apply if the research involves people or may find vulnerabilities in real systems | [Ethical issues specific to this field](../07_fields/computer-science/README.md#ethics-issues-specific-to-this-field); for general principles see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) |
| Conventions in other fields | The field overviews in [Fields](../07_fields/README.md) |

**Write it down:** For each method you've chosen, write down one method page or guideline you will read and two or three papers you plan to compare against. Then one sentence: in your target community, what standard is this method usually judged by?

> **How this step differs by type of research** `[Our analysis]`
>
> - **Empirical studies** (see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md)): the method has to cope with the scale of the data, and you have to say why you chose it. He et al. 2020 had to process nearly 10 million contracts[^he2020characterizing-e6]. They chose lightweight fingerprint matching because it had to scale to that size, and because contract logic is simple enough not to need heavier program analysis[^he2020characterizing-e8].
> - **Tool or technique papers** (see [Engineering research](../07_fields/computer-science/practices/engineering_research.md)): the heart of the method is "compared against what, on what". Slither was compared with three open-source tools, stating each tool's version, and the comparison covered only reentrancy detection, the one check all the tools had[^feist2019slither-e6].
> - **Benchmarks or datasets** (see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md)): first decide what you will evaluate. SmartBugs started from 35 tools and narrowed them to 9 using stated inclusion criteria[^durieux2020empirical-e4].
> - **Reviews** (see [Review studies](../06_methods/review_study.md)): the method is a review protocol written in advance. Rameder et al. 2022 built theirs on several guidelines, including Kitchenham and Charters 2007, so that the results would be comprehensive and repeatable[^rameder2022review-e4].

---

## Judgment calls

**What if you can't settle on a method?** Here is one way to decide `[Our analysis]`:

| What happens | What you usually do |
|---|---|
| Two methods could both get this evidence | Choose the one whose preconditions are easier to meet and that you know better; say in the paper why you didn't choose the other |
| The most suitable method isn't feasible (no data, can't recruit people, no field site) | First look for other evidence that could support a similar conclusion; if there is none, make the claim smaller |
| The main method's weakness hits the central claim directly | Add a method that makes up for that weakness, or limit the claim to what the main method can support |
| Your advisor wants a different method from the one you judged best | Bring your evidence–method table and discuss how each piece of evidence will be obtained; disagreements often come from understanding the claim differently |
| You can't write a clear hypothesis but plan to run an experiment | Do exploratory work first, such as interviews or reading through a batch of samples by hand, to get the hypothesis clear |
| You want to add a method only to satisfy reviewers | Don't; first ask which piece of evidence it serves |

**When have you chosen well?** Not when you've "found the best method", but when every row of the evidence plan has a method, its preconditions are met, its output fits into the results table, and you can name its weaknesses and say why they are acceptable.

## Common mistakes

Reasons without footnotes are this handbook's own summary `[Our analysis]`.

| Mistake | Why it's a problem |
|---|---|
| Choosing the method first, then looking for what it can show | A method should be chosen by how well it fits the question[^easterbrook2008selecting-e76]; choose the method first and you may find, once you're done, that it can't support the claim |
| Copying the method from the last paper you read | The problem is different, and the method may be a serious mismatch[^shaw2003writing-e15] |
| "Validating" a formal result with one or two examples | A formal model needs rigorous derivation and proof[^shaw2003writing-e9] |
| Evidence that doesn't match the claim | Claiming better performance but only showing ease of use[^shaw2003writing-e12] |
| Using a questionnaire to answer "what people actually do" | What people say may have nothing to do with what they do[^easterbrook2008selecting-e52] |
| Presenting lab results directly as conclusions about real settings | The variables you held fixed may matter a lot in real settings[^easterbrook2008selecting-e79] |
| Forcing in mixed methods to look rigorous | A token method contributes nothing substantial to the findings; the software engineering empirical standards list this as an antipattern[^ralph2020empirical-e282] |
| Starting without reading the method guidelines | The software engineering empirical standards list this as an antipattern[^ralph2020empirical-e26]; you also won't know what standard to meet |
| Changing the method without keeping a record | The original plan and every later change should be recorded[^easterbrook2008selecting-e87]; if you don't, you can't say afterward under what design the results were obtained |

## What you should have at the end

- An **evidence–method table**: one row per piece of evidence, listing what it asks, the chosen method, whether the preconditions are met, the method's strengths and weaknesses, and the check result (Sections 2, 3, and 5)
- If you combine methods, a paragraph saying which methods, in which phase each is used, and what each contributes (Section 4)
- A reading list: the guidelines to read and the papers to compare against for each method (Section 6)

## Checklist before moving on

You can move on when all of these hold:

- [ ] You have written down your main strategy and checked your evidence plan against the strategy page, with nothing missing
- [ ] Every row of the evidence plan has a chosen method, and all preconditions are met
- [ ] You can say how your main method does on control, realism, generalizability, and precision, and why its weaknesses are acceptable
- [ ] If you combine methods, you can say which piece of evidence each method serves
- [ ] Each method's output fits into some cell of the empty results table
- [ ] You have confirmed you can get the data, participants or subjects, and field sites you need
- [ ] For each method you have found a method page or guideline to read, and you know what standard it is judged by
- [ ] Your advisor has seen the evidence–method table and raised no fundamental objection

## When to go back

| If this happens | Go back to |
|---|---|
| No method can get a certain piece of evidence | [From research questions to an evidence plan](01_question-to-evidence.md); replace it with evidence you can get |
| The evidence you can get only supports a much weaker claim | [Converging on a project](../01_find-a-problem/05_converge.md), Section 1; rewrite the claim |
| While checking the strategy page, you realize the claim actually belongs to a different strategy | The section "How to choose your main strategy" in [Research strategies](../05_research-strategies/README.md#how-to-pick-your-main-strategy); choose the main strategy again, then return to Section 1 of this chapter |
| The chosen method requires too much learning to fit your schedule | When you schedule the work in the next chapter, [Writing a research plan](03_research-plan.md#5-estimate-time-and-build-in-slack), count the learning time; if it still doesn't fit, come back to this chapter and switch to a method you know better |

## Next

With the evidence and methods settled, the next step is scheduling: turn the evidence plan into milestones, and decide what comes first, how long each step takes, and when each is due. See [Writing a research plan](03_research-plan.md).

[^easterbrook2008selecting-e1]: Easterbrook et al. 2008, §1.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e1)
[^easterbrook2008selecting-e3]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e3)
[^easterbrook2008selecting-e4]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e4)
[^easterbrook2008selecting-e5]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e5)
[^easterbrook2008selecting-e6]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e6)
[^easterbrook2008selecting-e7]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e7)
[^easterbrook2008selecting-e9]: Easterbrook et al. 2008, §6.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e9)
[^easterbrook2008selecting-e12]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e12)
[^easterbrook2008selecting-e16]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e16)
[^easterbrook2008selecting-e19]: Easterbrook et al. 2008, §5.3. [Evidence](../../sources/notes/easterbrook2008selecting.md#e19)
[^easterbrook2008selecting-e25]: Easterbrook et al. 2008, Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e25)
[^easterbrook2008selecting-e26]: Easterbrook et al. 2008, Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e26)
[^easterbrook2008selecting-e41]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e41)
[^easterbrook2008selecting-e42]: Easterbrook et al. 2008, §1.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e42)
[^easterbrook2008selecting-e76]: Easterbrook et al. 2008, §5.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e76)
[^easterbrook2008selecting-e77]: Easterbrook et al. 2008, §5.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e77)
[^easterbrook2008selecting-e78]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e78)
[^easterbrook2008selecting-e79]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e79)
[^easterbrook2008selecting-e80]: Easterbrook et al. 2008, §5.1. [Evidence](../../sources/notes/easterbrook2008selecting.md#e80)
[^easterbrook2008selecting-e81]: Easterbrook et al. 2008, §5.3. [Evidence](../../sources/notes/easterbrook2008selecting.md#e81)
[^easterbrook2008selecting-e52]: Easterbrook et al. 2008, §5.3. [Evidence](../../sources/notes/easterbrook2008selecting.md#e52)
[^easterbrook2008selecting-e82]: Easterbrook et al. 2008, §5.3. [Evidence](../../sources/notes/easterbrook2008selecting.md#e82)
[^easterbrook2008selecting-e83]: Easterbrook et al. 2008, §5.4. [Evidence](../../sources/notes/easterbrook2008selecting.md#e83)
[^easterbrook2008selecting-e84]: Easterbrook et al. 2008, §5.5. [Evidence](../../sources/notes/easterbrook2008selecting.md#e84)
[^easterbrook2008selecting-e85]: Easterbrook et al. 2008, §3.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e85)
[^easterbrook2008selecting-e86]: Easterbrook et al. 2008, §3.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e86)
[^easterbrook2008selecting-e87]: Easterbrook et al. 2008, Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e87)
[^easterbrook2008selecting-e88]: Easterbrook et al. 2008, Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e88)
[^easterbrook2008selecting-e89]: Easterbrook et al. 2008, §6.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e89)
[^easterbrook2008selecting-e90]: Easterbrook et al. 2008, Conclusions. [Evidence](../../sources/notes/easterbrook2008selecting.md#e90)
[^storey2020who-e1]: Storey et al. 2020, §2. [Evidence](../../sources/notes/storey2020who.md#e1)
[^storey2020who-e3]: Storey et al. 2020, §3.3. [Evidence](../../sources/notes/storey2020who.md#e3)
[^storey2020who-e5]: Storey et al. 2020, §6.2. [Evidence](../../sources/notes/storey2020who.md#e5)
[^storey2020who-e6]: Storey et al. 2020, §6.2. [Evidence](../../sources/notes/storey2020who.md#e6)
[^storey2020who-e7]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e7)
[^storey2020who-e8]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e8)
[^storey2020who-e10]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e10)
[^storey2020who-e12]: Storey et al. 2020, §3.3.1. [Evidence](../../sources/notes/storey2020who.md#e12)
[^storey2020who-e13]: Storey et al. 2020, §3.3.2. [Evidence](../../sources/notes/storey2020who.md#e13)
[^storey2020who-e14]: Storey et al. 2020, §3.3.3. [Evidence](../../sources/notes/storey2020who.md#e14)
[^storey2020who-e15]: Storey et al. 2020, §3.3.4. [Evidence](../../sources/notes/storey2020who.md#e15)
[^ralph2020empirical-e23]: ACM SIGSOFT Empirical Standards, General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e23)
[^ralph2020empirical-e24]: ACM SIGSOFT Empirical Standards, General Standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e25]: ACM SIGSOFT Empirical Standards, General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e26]: ACM SIGSOFT Empirical Standards, General Standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e26)
[^ralph2020empirical-e177]: ACM SIGSOFT Empirical Standards, Experiments standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e177)
[^ralph2020empirical-e183]: ACM SIGSOFT Empirical Standards, Experiments standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e183)
[^ralph2020empirical-e276]: ACM SIGSOFT Empirical Standards, Multi-Methodology and Mixed Methods standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e276)
[^ralph2020empirical-e282]: ACM SIGSOFT Empirical Standards, Multi-Methodology and Mixed Methods standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e282)
[^ralph2020empirical-e290]: ACM SIGSOFT Empirical Standards, General Standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e290)
[^ralph2020empirical-e441]: ACM SIGSOFT Empirical Standards, General Standard, Examples of Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e441)
[^shaw2003writing-e9]: Shaw 2003, §4.1. [Evidence](../../sources/notes/shaw2003writing.md#e9)
[^shaw2003writing-e12]: Shaw 2003, §4.3. [Evidence](../../sources/notes/shaw2003writing.md#e12)
[^shaw2003writing-e13]: Shaw 2003, §4.3. [Evidence](../../sources/notes/shaw2003writing.md#e13)
[^shaw2003writing-e15]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e15)
[^he2020characterizing-e6]: He et al. 2020 (code clones in Ethereum smart contracts), §4.1 Dataset, §4.2 Pre-processing, p. 8. [Evidence](../../sources/notes/he2020characterizing.md#e6)
[^he2020characterizing-e8]: He et al. 2020 (code clones in Ethereum smart contracts), §3 Methodology, p. 5. [Evidence](../../sources/notes/he2020characterizing.md#e8)
[^feist2019slither-e6]: Feist et al. 2019 (Slither, a static analysis tool for smart contracts), §V-A Vulnerability Detection Evaluation, p. 5. [Evidence](../../sources/notes/feist2019slither.md#e6)
[^durieux2020empirical-e4]: Durieux et al. 2020 (SmartBugs evaluation of smart contract analysis tools), §2.2 Subject Tools, pp. 2–3. [Evidence](../../sources/notes/durieux2020empirical.md#e4)
[^rameder2022review-e4]: Rameder et al. 2022 (systematic review of vulnerability analysis for Ethereum smart contracts), §2 Systematic Review, p. 2. [Evidence](../../sources/notes/rameder2022review.md#e4)
