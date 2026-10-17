# Running and iterating

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Make sure you are testing a specific hypothesis.** Write down the hypothesis and what result would show it is wrong. If you can't, go back to [Exploring hands-on](../01_find-a-problem/03_explore.md) first ([Section 1](#1-first-know-which-stage-you-are-in)).
> 2. **Leave a record of every run.** For any result that might be useful, note which code version, which data version, which parameters, and where the output is ([Section 3](#3-leave-a-record-of-every-run)).
> 3. **When you change your approach, write it down and say so.** Put every change in the change log with the reason for it; tell your advisor about big changes ([Section 4](#4-when-you-change-your-approach-write-it-down-and-say-so)).
> 4. **When stuck, troubleshoot in fixed steps; before switching direction, write down why.** Start with three lines: "input / expected / actual". Before you drop a direction, write down why it is doomed ([Section 5](#5-when-youre-stuck-troubleshoot-in-fixed-steps), [Section 6](#6-persist-or-change-direction)).
> 5. **Write a weekly report and review regularly.** Don't leave the "Changes" and "Stuck on" sections of the report empty; set a fixed time each week to look up from the work ([Section 7](#7-report-progress-to-your-advisor), [Section 8](#8-look-up-from-the-work-regularly)).
>
> **Done these? Move on:** You have the evidence every milestone in the plan called for, or you and your advisor have agreed to change the claim; you can say how every result going into the paper was produced; and you can say in one sentence what the results support and what they don't. Next: [Analysis and interpretation](07_analyze-and-interpret.md).

## Where you are

You have an evidence plan and a research plan (see [From research questions to an evidence plan](01_question-to-evidence.md) and [Writing a research plan](03_research-plan.md)), you have thought through the threats to validity, and the smallest version of the study already runs end to end (see [The smallest version that runs end to end](05_pilot-and-derisk.md)). Now you have to do the work for real, and keep at it for weeks or months.

At this point you may find that:

- You run experiments every day, but at the end of the week you can't say how far you got;
- The result files keep piling up, and you can no longer tell which code version or parameter settings produced which one;
- You've been stuck on something for two weeks and don't know whether to keep trying or switch approaches;
- You meet your advisor every week, don't know what to report, and can't bring yourself to say "it doesn't work yet".

## What this stage is for

Turn the plan into evidence, round by round, without getting lost along the way. Concretely, answer these six questions:

1. Am I exploring right now, or testing a specific idea?
2. How can I make each round of "idea → result" faster?
3. What record does each run leave? Will I be able to find it again months from now?
4. When I changed my approach midway, did I write it down and tell people?
5. When I'm stuck, how do I troubleshoot? When should I change direction?
6. How should I report to my advisor so my advisor can actually help?

These questions come back every week; you don't answer them once and move on. This chapter gives **practices you can use every day and every week** `[Our analysis]`.

---

## 1. First, know which stage you are in

If, while running the study, you can't write down a specific hypothesis or say what evidence would tell you whether it is right, you are still in the exploration stage. For how to tell exploring from testing, and what to do while exploring, see [Exploring hands-on](../01_find-a-problem/03_explore.md). Going back to exploration is normal and doesn't mean you've messed up[^nanda2025process-e6].

**Write it down:** Write down the hypothesis you are testing and what result would show it is wrong. If you can't, go back to [Exploring hands-on](../01_find-a-problem/03_explore.md) first.

## 2. Make each round of "idea → result" faster

The process from "I have an idea for an experiment" to "I see the result" is one feedback loop; when it is short, the loop is called "tight"[^nanda2025mindsets-e10]. The tighter the loop, the more ideas you can try in the same amount of time `[Our analysis]`.

**How:**

- **Do quick, rough experiments first.** Spending a little time to see early signs is far better than spending weeks on an expensive, slow experiment with a clear-cut conclusion[^nanda2025mindsets-e11]. Early in a project, pick experiments that give results within a day wherever you can[^perez2024tips-e3].
- **Use toy examples and proxy tasks.** Look for toy examples and proxy tasks that cut the waiting time[^huang2023unstuck-e6]. A toy example is deliberately simplified to keep only the core mechanism; a proxy task is smaller and faster than the real task but shows the same thing. The best toy example is the simplest one that captures the core idea[^freeman2013research-e4].
- **Change one thing at a time.** That is the only way to know which change caused a change in the result[^freeman2013research-e2].
- **Be willing to spend time improving your tools.** One machine learning researcher found that once a script took more than about a second to start producing useful output, his productivity began to drop[^carlini2022rapid-e2], so he took a few days off research to write tools, and his workflow became much faster[^carlini2022rapid-e3]. "One second" is his personal experience in machine learning, not a universal standard `[Our analysis]`.

**The running example** `[Our analysis]`: in the full study, you look for leakage across two thousand contracts, have several models try to detect vulnerabilities in them, and compare detection rates.

| Slow way | Fast way |
|---|---|
| Re-match all two thousand contracts every time you change the leakage rule | Try the rule on a fixed set of 20 contracts first, and scale up once it is stable |
| Call the large language model's API (application programming interface) afresh every time | Cache the responses you already have, and rerun only the parts that changed |
| Change the leakage definition, the model, and the scoring rules all at once | Change one at a time, keeping everything else fixed |
| Read through outputs by hand looking for errors | Write a small script that lists the contracts judged wrong |

> **Where sources disagree: go faster or go slower?**
>
> - One view stresses speed: one researcher says he only does good research when he can iterate on ideas quickly[^carlini2022rapid-e1]; better to do quick, rough experiments first[^nanda2025mindsets-e11].
> - Another view's first piece of advice is "go slow to go fast"[^freeman2013research-e1]: slow down, check your assumptions, change one thing at a time[^freeman2013research-e2].
> - The two don't fully conflict. Those who push for speed also concede that getting sloppy and introducing lots of errors in the name of speed costs more time in the long run[^nanda2025mindsets-e14].
>
> In practice `[Our analysis]`: **shorten each round's cycle, don't lower each round's rigor.** Use smaller, simpler problems to make each round faster; within each round, still change one thing at a time and check your assumptions.

**Scope** `[Our analysis]`: "results within a day" comes from computer science and machine learning. In fields where one experiment takes months (clinical research, field surveys, long-term culture experiments, large-scale interview studies), you can shorten each round with small-sample trial runs, simulations, or by testing ideas on public data first.

For which part to do first, see [Writing a research plan](03_research-plan.md#4-set-the-order-do-what-is-most-likely-to-fail-first) and [The smallest version that runs end to end](05_pilot-and-derisk.md).

**Write it down:** Estimate how long one round of "idea → result" takes you now. Write down one way to cut that in half.

## 3. Leave a record of every run

Once you are running fast, the most common problem is that, with so many results, you can't tell how each one was produced. **For any result that might be useful, record how you got it**[^sandve2013ten-e7]: which code version, which data version, which parameters, where the output is; and keep your daily ideas and experiments in a searchable research log[^schulman2020opinionated-e16][^dredze2012successful-e2]. For which fields to record, how to write the log, and how to lay out directories, see [Organizing research materials](../08_throughout/organizing_materials.md#3-every-result-must-be-traceable-to-how-it-was-produced), Section 3, and [Section 5](../08_throughout/organizing_materials.md#5-keep-three-kinds-of-notes-apart).

While running the study, **also keep two small separate files:**

- **A highlights file**: only for especially interesting results, so it is easier to spot connections between them[^nanda2025process-e4].
- **An ideas list**: when a new idea comes up during the project, note it here first, then get back to what you were doing[^carlini2024logfile-e2]. Reread it after a while; only the ideas you still like on both readings are worth pursuing[^carlini2024logfile-e3].

**Review your log every week or two**, and condense it into a summary[^schulman2020opinionated-e17], to check whether you are jumping back and forth between a few ideas (see Section 6).

**Write it down:** Create the two files, a highlights file and an ideas list. Put this week's most interesting result into the highlights file, and put any idea that came up but shouldn't be pursued yet into the ideas list. For a run-record template, see [Organizing research materials](../08_throughout/organizing_materials.md#3-every-result-must-be-traceable-to-how-it-was-produced), Section 3.

## 4. When you change your approach, write it down and say so

As you go, you will certainly make changes: switch to a different leakage definition, drop a batch of data, change the scoring method. **Changes are fine in themselves; the problem is making them quietly.**

**Why quiet changes are a problem:**

- **Looking at the same test data over and over makes your conclusions untrustworthy.** This is common in machine learning research: trying different models and parameters on the same test data until the results look good[^lones2021avoid-e4]. The more often you use the test data, the more you overfit to it[^lones2021avoid-e5], meaning the results only look good on that particular data.
- **Memory is unreliable.** People misremember and unconsciously reason toward what they want, and these biases often operate outside awareness; good intentions are not enough[^nosek2018preregistration-e3]. The lesson from psychology is that researchers who keep switching analyses until a result is "significant" often don't realize they are doing it, and don't think it has any consequences[^nelson2018psychology-e8].
- **Deviations from plans are common, but disclosed deviations are rare.** One study examined 195 pre-analysis plans (analysis plans written before seeing the results) registered on two registries in political science and economics between 2011 and 2016[^ofosu2023preanalysis-e1]: in this sample there were 14 deviations from the plan, and only 1 noted the change[^ofosu2023preanalysis-e7]. This reflects the early years of two fields and doesn't represent every field `[Our analysis]`.

**How:**

1. **Set aside your evaluation data at the start and keep it for the end** (the machine learning practice). At the very beginning of the project, set aside an independent test set and use it only once, at the end, to evaluate the single final model[^lones2021avoid-e3]. Day to day, tune your matching rules and parsing scripts on a separate development set `[Our analysis]`.
2. **For every change, add a line to the change log in your plan:** what you changed, why, and which results you had already seen before changing it `[Our analysis]`. For how to write the change log, see [Writing a research plan](03_research-plan.md#7-how-the-plan-changes), Section 7.
3. **Keep apart the analyses you fixed in advance and the ones you thought of after seeing results.** Post hoc exploration is not inferior to advance prediction; what matters is that people can tell which is which[^nosek2018preregistration-e4].
4. **If you changed something, report truthfully what you changed and why.** Even if you deviate from a registered plan midway, registering the plan and then reporting the deviations honestly is still far more credible than not registering at all[^nosek2018preregistration-e5].
5. **Tell your advisor about big changes first**, such as switching benchmarks, changing the core metric, or dropping a batch of data `[Our analysis]`.

**Scope** `[Our analysis]`: Step 1 is the practice in research that evaluates methods on datasets, such as machine learning; steps 2–5 apply in every field. Political science and economics already have dedicated registries for registering analysis plans in advance[^ofosu2023preanalysis-e1]; for more, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md). For how far your conclusions can go, see [Validity and limitations](04_validity-and-limits.md).

**Write it down:** Go through the last two weeks of your log and list every change you made. For each, add "why I changed it" and "what results I had seen before changing it". Is there any change you weren't planning to tell your advisor about?

## 5. When you're stuck, troubleshoot in fixed steps

In most research projects, experiments fail most of the time[^huang2023unstuck-e1]. Everyone gets stuck and discouraged[^dredze2012successful-e4]. What matters is having a set of moves ready.

**Try these in order:**

1. **Make the failure specific.** Don't just say "it doesn't work". Write down what the input was, what result you expected, and what you actually got[^huang2023unstuck-e2]; and which step you have narrowed the problem down to[^freeman2013research-e3].
2. **Simplify the problem until it has to work.** Make the task simpler step by step, until it is bound to "succeed"[^huang2023unstuck-e3]; ask, "Is there a simpler case I can get working?"[^freeman2013research-e6] Once it works, add the difficulty back one piece at a time `[Our analysis]`.
3. **Pretend you already know part of the answer.** Giving yourself extra (privileged) information is a powerful way to make progress[^huang2023unstuck-e4]. For example, if leakage matching keeps finding nothing, first run it on a few contracts you know for certain were copied: if those match, the problem lies with the other contracts; if they don't, the problem is in the matching method itself `[Our analysis]`.
4. **Keep asking why it failed.** Ask why after every failure, so you don't keep trying approaches that will fail for the same reason[^steinhardt2018stochastic-e9]. One person spent months trying all sorts of approaches before discovering that they all failed for the same reason[^steinhardt2018stochastic-e21].
5. **Debug the idea itself.** If you've checked the code and the experiments and it still doesn't work, step back and check the idea[^huang2023unstuck-e5].
6. **Reframe the problem.** Clinging to one particular formulation of a problem is a common mistake; finding a related problem, or a reformulation that lets you move forward, is also progress[^nielsen2004principles-e4].
7. **Still no leads? Set a 5-minute timer and list everything you could do**[^nanda2025mindsets-e5]; then find someone to talk it over with. Asking other researchers, especially your advisor, can give you a new angle[^nanda2025mindsets-e16]. When you notice you are making slow progress, ask for help early and without embarrassment[^perez2024tips-e7].

**Progress isn't only "it worked".** Explaining why something doesn't work, or spending time reading to understand the problem, both count as progress[^freeman2013research-e7]. As long as you are learning about the problem, an experiment that didn't "succeed" still gained you something[^perez2024tips-e1].

**Write it down:** For the place you are stuck now, write three lines, "input / expected / actual", then write down which causes you have already ruled out. When you're done, pick one of the steps above and try it.

## 6. Persist or change direction

The hard part: some ideas show no effect only because one detail is wrong, while others are doomed however you do them[^schulman2020opinionated-e19], and the two are hard to tell apart.

**When deciding, keep in mind:**

- **One failure doesn't mean the idea failed.** What you tried was one implementation of the idea, not the whole idea[^steinhardt2018stochastic-e10]. "It looks like it won't work" or "I tried a few times and lost steam" don't count as ruling it out[^steinhardt2018stochastic-e22]; you need to be able to say why it is doomed `[Our analysis]`.
- **Switching too often is more common than switching too rarely**[^schulman2020opinionated-e13]. The early results of a new idea will most likely be just as disappointing, and it will also take sustained effort to get results[^schulman2020opinionated-e20]. If you keep switching and never explore anything properly, you learn nothing[^nanda2025mindsets-e1].
- **Signs it's time to stop:** you keep lowering your goals and expectations[^dredze2012successful-e5]; or the project's returns are clearly diminishing, in which case switching projects is perfectly fine[^perez2024tips-e2]. When a direction isn't very promising, be ready to drop it decisively[^nanda2025mindsets-e1].
- **Know your own failure mode.** Some people go down a rabbit hole and can't get out; others overthink and put off starting, waiting for a perfect moment that never comes[^nanda2025mindsets-e9]. Work out which way you lean, and lean harder on the advice aimed at it `[Our analysis]`.
- **Set aside a fixed share of time for new ideas.** Keep a fixed time budget for trying new ideas that stray from the main line[^schulman2020opinionated-e21], while the main line carries on as usual `[Our analysis]`.

"Changing direction" can be big or small. Start with the smallest change `[Our analysis]`:

| What to change | When | Example |
|---|---|---|
| Switch implementation | The idea itself hasn't been refuted; only this way of doing it fails | Switch leakage matching from "identical" to "highly similar" |
| Change the claim | The evidence only supports a smaller or different conclusion | Change "evaluation results are inflated by leakage" to "on reentrancy vulnerabilities, evaluation results are inflated by leakage" |
| Change the problem | You can say why the idea is doomed | Go back to [Converging on a project](../01_find-a-problem/05_converge.md) and pick another candidate conclusion |

If you change the claim or the problem, update the plan at the same time and tell your advisor (see Sections 4 and 7).

For whether to run two projects at once, switching to one when the other hits a wall, see [Planning and daily routines](../08_throughout/planning_and_routines.md#6-when-you-have-several-projects-at-once).

**Write it down:** For the direction you are most unsure about, write down "why it is doomed". If you can't give a concrete reason, don't give up yet; write down the next cheapest way to try it. If you can, use the table above to decide which level to change.

## 7. Report progress to your advisor

**Your advisor wants to hear about progress, and "progress" can mean a lot of things**: one advisor says plainly that he loves to hear about progress in meetings and has a very general notion of what progress is[^freeman2013research-e9]. Explaining why something doesn't work is progress too (Section 5).

**How:**

- **Send results to your advisor regularly as they come in**, rather than saving them all up for the meeting[^huang2023advisor-e2]. If your advisor sees the results for the first time in the meeting, there is no time to understand and think about them[^huang2023advisor-e1].
- **Meet regularly**, say once a week, especially when you don't feel like it[^dredze2012successful-e11]. Bring results each time if you can, such as figures and tables[^dredze2012successful-e13].
- **Start with a summary.** Your advisor has many projects, unlike you who spent the whole week on this one, and needs time to switch context[^dredze2012successful-e14]. Open with what you agreed to do last time and what the conclusion is, and leave the details for later[^huang2023advisor-e4].
- **Put the results in context**[^huang2023advisor-e5]: what you did, why, what you found, and whether it matched what you expected `[Our analysis]`.
- **Propose your next steps.** Right after presenting the results, lay out the possible next steps and your priority order[^perez2024tips-e6], with your reasons[^huang2023advisor-e6].
- **Show, don't just tell.** If you only describe verbally what you did, it is hard for others to fully understand[^huang2023unstuck-e8]. Your advisor has experience and wants to help, but you need to help your advisor help you[^huang2023unstuck-e7].
- **Say what the problems are.** Be upfront about the problems you run into[^perez2024tips-e8]; when you're stuck, don't avoid your advisor; go and talk to them[^freeman2013research-e10]; if you think you'll miss a deadline, say so; your advisor would rather know early[^dredze2012successful-e20].
- **When the approach your advisor suggested doesn't work**, first do what your advisor said; when you see it doesn't work, look around near the original proposal for something that does, and report that back[^freeman2013research-e8]. You know more about this specific problem than your advisor does, and sometimes that is enough for you to make the better call[^nanda2025mindsets-e15].

**What a weekly report looks like** `[Our analysis]`:

> **Agreed last week:** On the development set, compare three models' detection rates on leaked versus non-leaked samples.
>
> **Conclusion:** Using the "highly similar" definition, I found 38 leaked samples among the 200 development-set contracts. All three models detect vulnerabilities more often in the leaked samples, by 9 to 15 percentage points (table attached).
>
> **Changes:** Removed 12 contracts that wouldn't compile (reasons in the log).
>
> **Stuck on:** The leaked samples are on average only half as long as the non-leaked ones, so part of the gap may come from difficulty. Ruled out: a bug in the parsing script.
>
> **Proposed next steps:** (1) Match samples by length and vulnerability type and compare again (top priority, because it decides whether the conclusion holds); (2) add a second benchmark.
>
> **Need your decision:** Should samples that can't be matched be dropped, or reported separately?

After the meeting, write down the agreed next steps and send them to your advisor[^huang2023advisor-e7]. For working with your advisor day to day, see [Collaboration and advisors](../08_throughout/collaboration_and_advisors.md).

**Write it down:** Using the format above, write this week's report. Don't leave the "Changes" and "Stuck on" sections blank; if there really is nothing, write "None".

## 8. Look up from the work regularly

Besides keeping your head down, step back regularly to make sure you are working on the right thing[^freeman2013research-e5]. Prioritizing and executing are two different modes; don't do both at once[^nanda2025mindsets-e6].

**Set aside time every week to review**[^nanda2025mindsets-e7], and ask yourself a few questions: What has taken the most time lately? What has been blocking me? What mistakes did I make, and how can I change how I work so I don't make them again[^nanda2025mindsets-e8]? Add one more `[Our analysis]`: **what is still missing between what I got this week and "done" for the next milestone in the plan?** If the gap keeps growing, consider changing the claim, as described in Section 6.

Most of the time, moving is better than standing still, provided you regularly take time to reflect on your goals[^nielsen2004principles-e3]. For the full weekly review routine and how to organize your days, see [Planning and daily routines](../08_throughout/planning_and_routines.md).

**Work at a pace you can sustain.** Many researchers burn out because the way they work isn't sustainable[^perez2024tips-e5]. Rest usually brings a net increase in productive working time[^nanda2025process-e7]. For more, see [Mindset and long-term growth](../08_throughout/mindset_and_growth.md).

**Write it down:** Put a fixed weekly review time on your calendar. At the first review, answer the four questions above in a sentence or two each.

## 9. Different strategies, different things to watch while running

The practices above apply to every kind of research. Each [research strategy](../00_start-here/key-concepts.md#research-strategy) also has its own priorities while running: Building and improving, for example, means adding changes one at a time and keeping a version at every step; Synthesis means recording why each paper was included or excluded `[Our analysis]`. For each strategy's priorities, see Section 4, "How it shapes the whole project", on the corresponding strategy page: [Description](../05_research-strategies/observe_describe.md), [Measurement](../05_research-strategies/measure.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Causal explanation](../05_research-strategies/explain_causality.md), [Building and improving](../05_research-strategies/build_improve.md), [Synthesis](../05_research-strategies/synthesize.md), [Proof](../05_research-strategies/prove.md).

**Write it down:** Open the page for your main strategy, find the row or paragraph in Section 4 about running the study, rewrite it as a check to go through on every run, and add it to your run-record template.

---

## Judgment calls

**Does this change need to be recorded, and does it need to be reported?** `[Our analysis]`

| Change | In the log | In the plan's change log | Tell your advisor first |
|---|---|---|---|
| Fixed a bug | Yes | Yes, if it affected existing results | Yes, if it affects existing conclusions |
| Adjusted the parsing script, tuned parameters | Yes | No need | Mention it in the weekly report |
| Removed or added a batch of data | Yes | Yes | Yes |
| Switched benchmark or core metric | Yes | Yes | Yes, and tell them before you change it |
| Changed the claim or the problem | Yes | Yes | Yes, and decide it together |

**Try again, or switch?** Until you can say "why it is doomed", switch the implementation, not the idea; once you can say it, use the table in Section 6 and start changing from the smallest level.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Starting with a big, slow, complete experiment | You see the first signal only weeks later; quick, rough experiments tell you sooner whether the direction is right[^nanda2025mindsets-e11] |
| Changing several things at once | When the result changes, you don't know which change caused it[^freeman2013research-e2] |
| Not recording where result files came from | A year later, even you can't reproduce them[^sandve2013ten-e2] |
| Tuning on the test data over and over until the results look good | The more often you use it, the worse the overfitting[^lones2021avoid-e5] |
| Quietly dropping data or switching metrics | In one sample from political science and economics, only 1 of 14 deviations from the plan was noted[^ofosu2023preanalysis-e7] (see Section 4); readers have no way of telling how much of the conclusion can still be trusted `[Our analysis]` |
| Telling your advisor "it doesn't work" | Your advisor can't help; say what you expected, what you got, and which step you've narrowed the problem down to[^freeman2013research-e3][^huang2023unstuck-e2] |
| Giving up on a whole idea after one failure | Only one implementation failed[^steinhardt2018stochastic-e10] |
| Switching to a new idea at the first difficulty | You end up with a pile of half-finished projects, and the new ideas will most likely be just as hard[^schulman2020opinionated-e18][^schulman2020opinionated-e20] |
| Avoiding your advisor when stuck | The problem grows the longer it drags on; your advisor would rather know early[^freeman2013research-e10][^dredze2012successful-e20] |

## What you should have at the end

- A research log, plus a review summary every week or two (Section 3)
- Run records: every result can be traced to its code, data, parameters, and output location (Section 3)
- The plan's change log, with the reason for each change (Section 4)
- Weekly reports and meeting notes (Section 7)
- An ideas list and a highlights file (Section 3)

## Checklist before moving on

You can move on to analysis when all of these hold:

- [ ] You have the evidence every milestone in the plan called for, or you and your advisor have agreed to change the claim
- [ ] For every result going into the paper, you can name the code version, data version, parameters, and output location
- [ ] The test data for the final evaluation was used only once, at the end, or you recorded every time you used it
- [ ] Every deviation from the plan is in the change log, and your advisor knows about the big ones
- [ ] You can say in one sentence what the current results support and what they don't
- [ ] Your advisor has seen the main results and agrees you can start systematic analysis

## When to go back

| If this happens | Go back to |
|---|---|
| You don't know whether to persist, adjust, or go back | [Decision points: continue, adjust, or go back](08_decision-points.md#2-one-master-table-when-what-you-see-how-to-choose): look up the rows "Stuck during the main run" and "A long time with no progress" |
| You still can't write a specific hypothesis, and long exploration has turned up nothing | [Exploring hands-on](../01_find-a-problem/03_explore.md) or [Converging on a project](../01_find-a-problem/05_converge.md): rethink which sentence you want to prove |
| You're stuck because of the design itself: the data you have can't answer the research question | [From research questions to an evidence plan](01_question-to-evidence.md) |
| A key part turns out to be impossible, and you never tried it in advance | [The smallest version that runs end to end](05_pilot-and-derisk.md): try out all the remaining risks first |
| There are so many changes that the original plan no longer matches | [Writing a research plan](03_research-plan.md#7-how-the-plan-changes), Section 7: rework the plan starting from the claim |
| What you want to change is not the approach but the problem itself | [Converging on a project](../01_find-a-problem/05_converge.md): rewrite the one-page project summary together with your advisor |

## Next

Once you have the evidence, the next step is to analyze it systematically: what the results show, what they don't, and how to rule out other explanations. See [Analysis and interpretation](07_analyze-and-interpret.md).

[^carlini2022rapid-e1]: Carlini 2022, opening paragraph. [Evidence](../../sources/notes/carlini2022rapid.md#e1)
[^carlini2022rapid-e2]: Carlini 2022, section "(Machine learning) research does not support rapid iteration". [Evidence](../../sources/notes/carlini2022rapid.md#e2)
[^carlini2022rapid-e3]: Carlini 2022, same section. [Evidence](../../sources/notes/carlini2022rapid.md#e3)
[^carlini2024logfile-e2]: Carlini 2024, A bit more detail. [Evidence](../../sources/notes/carlini2024logfile.md#e2)
[^carlini2024logfile-e3]: Carlini 2024, A bit more detail. [Evidence](../../sources/notes/carlini2024logfile.md#e3)
[^dredze2012successful-e2]: Dredze & Wallach 2012 (v1.2), #18, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e2)
[^dredze2012successful-e4]: Dredze & Wallach 2012 (v1.2), #21, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e4)
[^dredze2012successful-e5]: Dredze & Wallach 2012 (v1.2), #34, p. 6. [Evidence](../../sources/notes/dredze2012successful.md#e5)
[^dredze2012successful-e11]: Dredze & Wallach 2012 (v1.2), #8, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e11)
[^dredze2012successful-e13]: Dredze & Wallach 2012 (v1.2), #10, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e13)
[^dredze2012successful-e14]: Dredze & Wallach 2012 (v1.2), #11, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e14)
[^dredze2012successful-e20]: Dredze & Wallach 2012 (v1.2), #45, p. 8. [Evidence](../../sources/notes/dredze2012successful.md#e20)
[^freeman2013research-e1]: Freeman 2013, p. 1. [Evidence](../../sources/notes/freeman2013research.md#e1)
[^freeman2013research-e2]: Freeman 2013, p. 1. [Evidence](../../sources/notes/freeman2013research.md#e2)
[^freeman2013research-e3]: Freeman 2013, p. 1. [Evidence](../../sources/notes/freeman2013research.md#e3)
[^freeman2013research-e4]: Freeman 2013, p. 1. [Evidence](../../sources/notes/freeman2013research.md#e4)
[^freeman2013research-e5]: Freeman 2013, p. 1. [Evidence](../../sources/notes/freeman2013research.md#e5)
[^freeman2013research-e6]: Freeman 2013, p. 3. [Evidence](../../sources/notes/freeman2013research.md#e6)
[^freeman2013research-e7]: Freeman 2013, p. 3. [Evidence](../../sources/notes/freeman2013research.md#e7)
[^freeman2013research-e8]: Freeman 2013, p. 2. [Evidence](../../sources/notes/freeman2013research.md#e8)
[^freeman2013research-e9]: Freeman 2013, p. 3. [Evidence](../../sources/notes/freeman2013research.md#e9)
[^freeman2013research-e10]: Freeman 2013, p. 3. [Evidence](../../sources/notes/freeman2013research.md#e10)
[^huang2023advisor-e1]: Jia-Bin Huang 2023, tweet thread, [How to meet with your advisors/mentors?](https://twitter.com/jbhuang0604/status/1653614931202195458), Present results. [Evidence](../../sources/notes/huang2023advisor.md#e1)
[^huang2023advisor-e2]: Jia-Bin Huang 2023, tweet thread, Present results. [Evidence](../../sources/notes/huang2023advisor.md#e2)
[^huang2023advisor-e4]: Jia-Bin Huang 2023, tweet thread, Start with a summary. [Evidence](../../sources/notes/huang2023advisor.md#e4)
[^huang2023advisor-e5]: Jia-Bin Huang 2023, tweet thread, Interpret your results. [Evidence](../../sources/notes/huang2023advisor.md#e5)
[^huang2023advisor-e6]: Jia-Bin Huang 2023, tweet thread, Propose next steps. [Evidence](../../sources/notes/huang2023advisor.md#e6)
[^huang2023advisor-e7]: Jia-Bin Huang 2023, tweet thread, Summarize your meeting. [Evidence](../../sources/notes/huang2023advisor.md#e7)
[^huang2023unstuck-e1]: Jia-Bin Huang 2023, tweet thread, [How to get unstuck?](https://twitter.com/jbhuang0604/status/1717381151508054029), item 1. [Evidence](../../sources/notes/huang2023unstuck.md#e1)
[^huang2023unstuck-e2]: Jia-Bin Huang 2023, tweet thread, Show HOW it failed. [Evidence](../../sources/notes/huang2023unstuck.md#e2)
[^huang2023unstuck-e3]: Jia-Bin Huang 2023, tweet thread, Simplify the tasks until it works. [Evidence](../../sources/notes/huang2023unstuck.md#e3)
[^huang2023unstuck-e4]: Jia-Bin Huang 2023, tweet thread, Introduce privileged information. [Evidence](../../sources/notes/huang2023unstuck.md#e4)
[^huang2023unstuck-e5]: Jia-Bin Huang 2023, tweet thread, Debug the idea. [Evidence](../../sources/notes/huang2023unstuck.md#e5)
[^huang2023unstuck-e6]: Jia-Bin Huang 2023, tweet thread, Iterate fast. [Evidence](../../sources/notes/huang2023unstuck.md#e6)
[^huang2023unstuck-e7]: Jia-Bin Huang 2023, tweet thread, Help your mentors help you. [Evidence](../../sources/notes/huang2023unstuck.md#e7)
[^huang2023unstuck-e8]: Jia-Bin Huang 2023, tweet thread, Make your experiments easy to understand. [Evidence](../../sources/notes/huang2023unstuck.md#e8)
[^lones2021avoid-e3]: Lones 2021, §3.1, p. 8. [Evidence](../../sources/notes/lones2021avoid.md#e3)
[^lones2021avoid-e4]: Lones 2021, §4.3, p. 15. [Evidence](../../sources/notes/lones2021avoid.md#e4)
[^lones2021avoid-e5]: Lones 2021, §4.3, p. 15. [Evidence](../../sources/notes/lones2021avoid.md#e5)
[^nanda2025mindsets-e1]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e1)
[^nanda2025mindsets-e5]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e5)
[^nanda2025mindsets-e6]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e6)
[^nanda2025mindsets-e7]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e7)
[^nanda2025mindsets-e8]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e8)
[^nanda2025mindsets-e9]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e9)
[^nanda2025mindsets-e10]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e10)
[^nanda2025mindsets-e11]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e11)
[^nanda2025mindsets-e14]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e14)
[^nanda2025mindsets-e15]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e15)
[^nanda2025mindsets-e16]: Nanda 2025b, Truth Seeking. [Evidence](../../sources/notes/nanda2025mindsets.md#e16)
[^nanda2025process-e4]: Nanda 2025a, Exploration (Stage 2). [Evidence](../../sources/notes/nanda2025process.md#e4)
[^nanda2025process-e6]: Nanda 2025a, Distillation (Stage 4). [Evidence](../../sources/notes/nanda2025process.md#e6)
[^nanda2025process-e7]: Nanda 2025a, Introduction. [Evidence](../../sources/notes/nanda2025process.md#e7)
[^nelson2018psychology-e8]: Nelson et al. 2018, False Positives Are Bad, p. 518. [Evidence](../../sources/notes/nelson2018psychology.md#e8)
[^nielsen2004principles-e3]: Nielsen 2004, The skills of the problem-solver. [Evidence](../../sources/notes/nielsen2004principles.md#e3)
[^nielsen2004principles-e4]: Nielsen 2004, The skills of the problem-solver. [Evidence](../../sources/notes/nielsen2004principles.md#e4)
[^nosek2018preregistration-e3]: Nosek et al. 2018, Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../sources/notes/nosek2018preregistration.md#e3)
[^nosek2018preregistration-e4]: Nosek et al. 2018, Preregistration Distinguishes Prediction and Postdiction. [Evidence](../../sources/notes/nosek2018preregistration.md#e4)
[^nosek2018preregistration-e5]: Nosek et al. 2018, Challenge 1: Changes to Procedure During Study Administration. [Evidence](../../sources/notes/nosek2018preregistration.md#e5)
[^ofosu2023preanalysis-e1]: Ofosu & Posner 2023, Abstract. [Evidence](../../sources/notes/ofosu2023preanalysis.md#e1)
[^ofosu2023preanalysis-e7]: Ofosu & Posner 2023, Do PAPs Reduce the Scope for Fishing? [Evidence](../../sources/notes/ofosu2023preanalysis.md#e7)
[^perez2024tips-e1]: Perez 2024, General Mindset Tips. [Evidence](../../sources/notes/perez2024tips.md#e1)
[^perez2024tips-e2]: Perez 2024, General Mindset Tips. [Evidence](../../sources/notes/perez2024tips.md#e2)
[^perez2024tips-e3]: Perez 2024, Three modes of research. [Evidence](../../sources/notes/perez2024tips.md#e3)
[^perez2024tips-e5]: Perez 2024, Work Habits. [Evidence](../../sources/notes/perez2024tips.md#e5)
[^perez2024tips-e6]: Perez 2024, Tactical Research Tips & Approach. [Evidence](../../sources/notes/perez2024tips.md#e6)
[^perez2024tips-e7]: Perez 2024, What success generally looks like. [Evidence](../../sources/notes/perez2024tips.md#e7)
[^perez2024tips-e8]: Perez 2024, What success generally looks like. [Evidence](../../sources/notes/perez2024tips.md#e8)
[^sandve2013ten-e2]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e2)
[^sandve2013ten-e7]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e7)
[^schulman2020opinionated-e13]: Schulman 2020, When to Switch Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e13)
[^schulman2020opinionated-e16]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e17)
[^schulman2020opinionated-e18]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e18)
[^schulman2020opinionated-e19]: Schulman 2020, When to Switch Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e19)
[^schulman2020opinionated-e20]: Schulman 2020, When to Switch Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e20)
[^schulman2020opinionated-e21]: Schulman 2020, When to Switch Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e21)
[^steinhardt2018stochastic-e9]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e9)
[^steinhardt2018stochastic-e10]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e21]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e21)
[^steinhardt2018stochastic-e22]: Steinhardt 2018, Additional Discussion. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e22)
