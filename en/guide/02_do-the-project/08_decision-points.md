# Decision points: continue, adjust, or go back

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Start a one-page decision log.** Every time you make a choice, add a line: the date, what you saw, which option you chose, and why ([Section 1](#1-part-2-is-a-loop-not-a-straight-line)).
> 2. **Find the row of the master table you are in right now.** Replace "what you see" with the concrete situation in your project, then choose continue, adjust, or go back ([Section 2](#2-one-master-table-when-what-you-see-how-to-choose)).
> 3. **Continue only against criteria written in advance; adjust starting from the smallest layer.** Change the implementation first, then the claim, and only last the problem; record every change in the change log ([Section 3](#3-how-to-judge-each-option)).
> 4. **Before going back, be able to write down why the claim doesn't hold.** "It looks like it won't work" is not a reason; but if you keep lowering your goals, it is time to stop ([Section 3](#3-how-to-judge-each-option)).
> 5. **After every decision, update the paper skeleton.** Keep the one-sentence claim, the empty results tables, the evidence plan, the filled-in results tables, and the contribution list in one file, and revise it to match the decision ([Section 4](#4-the-paper-skeleton-you-keep-up-to-date)).
>
> **Done these? Move on:** you know which row of the master table you are in, the paper skeleton matches your latest decision, and your advisor knows about every decision to change the claim or switch problems. Next: once the results tables are full and every conclusion points to its evidence, go to [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md).

## Where you are

You can land here from any step in Part 2: you have just finished a pilot, the real data has just come in, you are halfway through the analysis, or you have been at it for a long time and can't say what progress you've made.

Each earlier chapter ends with its own "When to go back" section, and several of them discuss how to decide between persisting and changing direction. This chapter doesn't repeat them. It gathers those decision points in one place, so that when you are unsure you have one table to look things up in.

## What this stage is for

1. Why isn't Part 2 a straight line? Is going back a failure?
2. At the key moments of a project, given what you see, should you continue, adjust, or go back to Part 1?
3. How do you judge each option, and what do you need to prepare first?
4. After each decision, which of your documents has to change with it?

---

## 1. Part 2 is a loop, not a straight line

This handbook lays out Part 2 as 2.1 through 2.7 because that is easier to read. Real projects don't go through it in one pass: a pilot overturns the design, data overturns the claim, analysis sends you back to run more experiments `[Our analysis]`.

**Going back is normal.** Describing his own research process, one machine learning researcher says that sometimes you find things are much messier than you thought, and you may need to go back to testing hypotheses or even to exploring again; this is completely normal and doesn't mean you have messed up[^nanda2025process-e6]. A tutorial on pilot studies in clinical research puts it more bluntly: a pilot that shows the main study is not feasible is not a failure but a success, because it kept you from wasting limited resources on a study doomed to fail[^thabane2010tutorial-e8].

So at each key moment, the job is not to grit your teeth and push on. Stop and pick one of three options `[Our analysis]`:

- **Continue**: the evidence broadly matches what you expected; carry on with the plan.
- **Adjust**: the claim still stands, but the definitions, the method, the scale, or the scope of the claim need to change.
- **Go back to Part 1**: the claim itself doesn't hold, or you have found a problem more worth doing.

**Write it down:** Start a "decision log" page in your research log. From now on, each time you make a choice using the tables in this chapter, add a line: the date, what you saw, which option you chose, and why.

## 2. One master table: when, what you see, how to choose

The table below puts the decision points from each chapter together in project order. The "Details" column points to the original section, which has the full discussion and the sources `[Our analysis]`.

| Moment | What you see | Continue | Adjust | Go back to Part 1 | Details |
|---|---|---|---|---|---|
| The pilot has finished | Whether the criteria you wrote in advance were met | Every feasibility criterion was met | Details went wrong (ambiguous materials, a bug in a script), or the measurement is unreliable, or costs ran over but can be cut | A core assumption the design depends on doesn't hold, e.g. the difference you wanted to measure barely exists | [2.5, Section 5](05_pilot-and-derisk.md#5-write-down-in-advance-what-results-mean-continue-adjust-or-stop); [2.5, Judgment calls](05_pilot-and-derisk.md#judgment-calls) |
| Stuck during the main run | After working through the fixed troubleshooting steps, which layer the problem has narrowed down to | It turns out to be an implementation problem; fix it and rerun | The idea hasn't been ruled out, so try a different implementation; or the data you have can't answer the question, so go back and revise the evidence plan | You can say why the idea is doomed | [2.6, Section 5](06_run-and-iterate.md#5-when-youre-stuck-troubleshoot-in-fixed-steps); [2.6, Section 6](06_run-and-iterate.md#6-persist-or-change-direction) |
| A long time with no progress | At the weekly review, how far you still are from the next milestone counting as done | The gap is shrinking | The gap keeps growing, or there have been so many changes that the plan no longer fits: redo the plan starting from the claim | You keep lowering your goals; you still can't write down a specific hypothesis | [2.6, Section 8](06_run-and-iterate.md#8-look-up-from-the-work-regularly); [2.3, Section 7](03_research-plan.md#7-how-the-plan-changes) |
| The real data comes in | Whether checking the data turned up any major problems | The data is fine; move on to analysis | The data has errors; go back to running the study and rerun | The data you have can't answer the research question at all, and you can't fill the gap | [2.7, Section 1](07_analyze-and-interpret.md#1-check-the-data-before-you-look-at-the-conclusions) |
| During analysis | Whether the results match the claim | Every conclusion points to its evidence | The effect holds only under some conditions, is smaller than expected, or comes from a cause you didn't anticipate: revise the claim | The claim is refuted and a narrower version is no longer interesting; or you have found a more interesting problem | [2.7, Section 5](07_analyze-and-interpret.md#5-negative-and-unexpected-results); [2.7, Section 7](07_analyze-and-interpret.md#7-when-the-evidence-doesnt-match-the-claim-change-the-claim) |

When you go back to Part 1, you usually return to [Converging on a project](../01_find-a-problem/05_converge.md#judgment-calls) and use the table there to decide whether to narrow the claim, change the angle, or drop this candidate. If none of your candidates holds up, go further back to [Generating candidate problems](../01_find-a-problem/02_generate-problems.md).

**Write it down:** Find the row you are in now, replace the "What you see" cell with the concrete situation in your project, and write down your choice.

## 3. How to judge each option

### Continue

You can only continue if you wrote down in advance what counts as continuing. The clinical pilot-study tutorial requires the criteria for success to be stated in advance[^thabane2010tutorial-e3]; if you set them after the trial, they drift toward the results without your noticing `[Our analysis]`.

What you need: the criteria table you wrote before the pilot ([2.5, Section 5](05_pilot-and-derisk.md#5-write-down-in-advance-what-results-mean-continue-adjust-or-stop)), and the "what counts as done" for each milestone in your plan ([2.3](03_research-plan.md)).

### Adjust

**Start from the smallest layer:** try a different implementation first, then consider revising the claim, and only last consider changing the problem `[Our analysis]`. The reasons: one failure only shows that you tried one implementation of the idea, not the whole idea[^steinhardt2018stochastic-e10]; and switching too often is more common than switching too rarely[^schulman2020opinionated-e13].

**Leave a trail when you adjust.** Whenever you change a definition, a method, or the data, record it in the plan's change log, and tell your advisor about big changes first (see [2.6, Section 4](06_run-and-iterate.md#4-when-you-change-your-approach-write-it-down-and-say-so)). Any analysis that comes from a change made after you looked at the data should be labeled exploratory (see [2.7, Section 2](07_analyze-and-interpret.md#2-run-the-planned-analyses-first-label-unplanned-ones-as-exploratory)) `[Our analysis]`.

**The bottom line for adjusting:** you change the claim, not the evidence. Quietly dropping unfavorable data to save the claim crosses the line (see [2.7, Section 7](07_analyze-and-interpret.md#7-when-the-evidence-doesnt-match-the-claim-change-the-claim)).

### Go back to Part 1

**Dropping an idea needs a solid reason.** "It looks like it won't work" or "I tried a few times and lost steam" don't count as ruling an idea out[^steinhardt2018stochastic-e22]. You need to be able to write down why it is doomed `[Our analysis]`.

**But stop when it's time to stop.** If you keep lowering your goals and expectations, that is a sign you aren't making progress[^dredze2012successful-e5]; when a project's returns are clearly diminishing, switching projects is perfectly fine[^perez2024tips-e2]. Be ready to drop a direction decisively when it isn't very promising; but if you keep switching and never explore anything properly, you learn nothing[^nanda2025mindsets-e1].

What you need: your decision log, the one-page project summary, and the evidence you already have. Going back is not starting from zero: the evidence you already have is often the starting point for the next candidate conclusion, and a negative result can itself become a claim (see [2.7, Section 5](07_analyze-and-interpret.md#5-negative-and-unexpected-results)) `[Our analysis]`.

**Write it down:** For the decision you are most torn about, write one reason each for continuing, adjusting, and going back. Whichever one you can't find a reason for, rule out first.

## 4. The paper skeleton you keep up to date

Across both parts, five things grow one out of the other `[Our analysis]`:

| Item | Where it comes from | What it answers |
|---|---|---|
| The one-sentence claim | [1.5 Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove) | What you want readers to believe |
| Empty results tables | [1.5, Section 4](../01_find-a-problem/05_converge.md#4-what-will-make-people-believe-it) | Which numbers you need for the claim to stand |
| Evidence plan | [2.1, Section 7](01_question-to-evidence.md#7-put-it-together-as-an-evidence-plan) | How each number will be obtained |
| Filled-in results tables | [2.7 Analysis and interpretation](07_analyze-and-interpret.md#6-how-far-your-conclusions-can-reach) | What you actually got |
| Contribution list | [Writing, Section 4](../03_write-and-publish/01_story-and-paper.md#4-introduction-five-questions-plus-a-list-of-contributions) | What the paper adds to the field |

This thread comes from writing advice by researchers in computer science and computational biology. One computer scientist says you can write the experiments section before running the experiments, sketching empty results tables complete with row and column headings and captions[^eisnerfirst-e5]; write it honestly and you will often find that proving your point takes more work than you expected, so the sooner you write, the better[^eisnerfirst-e6]. Writing advice published in a computational biology journal says to design the project with the final paper in mind and put a paper outline in your first design document[^zhang2014ten-e8]. Another computer scientist, talking about how to write papers, says that writing the paper is a primary mechanism for doing research, not just reporting it once it's done[^peytonjones2013write-e1]; writing the paper is how you develop the idea in the first place[^peytonjones2013write-e12]. The contribution list then drives the whole paper: the paper's job is to substantiate those claims[^peytonjones2013write-e4].

**After every decision, update this skeleton** `[Our analysis]`:

| Your decision | What to change |
|---|---|
| Continue | Fill the new numbers into the results tables |
| Adjust a definition or method | Change the matching row in the evidence plan; if the rows or columns of a results table change, update it too |
| Narrow or revise the claim | Work from the top down: revise the claim sentence first, then see which results tables and which evidence are no longer needed and which must be added |
| Go back to Part 1 | Archive the old skeleton; grow the new candidate from a one-sentence claim again, and carry over the tables and evidence you can reuse |

That way, on the day your experiments are done, you already have the skeleton of the paper: the claim, the results tables, and the contribution list are all there, and writing becomes a matter of turning it into a story. See [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md).

**Write it down:** Put all five items into one file, in the order of the table above. Every time you add a line to the decision log, open this file and go through it using the second table.

## 5. Example: almost no leakage turns up. Adjust the definition, or change the problem?

Back to the running example `[Our analysis]`. The central claim is "published evaluations of large language model vulnerability detectors are inflated by data leakage". In the [evidence plan](01_question-to-evidence.md#2-give-every-key-term-an-operational-definition), "leakage" was defined as: after stripping comments and whitespace, a contract in the benchmark is identical to some contract in the training corpus. A backup definition was written down at the same time: highly similar.

The pilot finishes, and under "identical" only a handful of leaked samples turn up among several hundred contracts. Looking at the contracts that didn't match, many differ only in renamed variables or reordered functions.

This is a decision point. Following Section 3, start from the smallest layer `[Our analysis]`:

1. **Is it a detail problem?** "Identical" may be too strict and miss copies with renamed identifiers. That is a measurement problem, and according to [2.5, Judgment calls](05_pilot-and-derisk.md#judgment-calls) you fix the measurement first. In practice: switch to the backup definition you wrote in advance, "highly similar"; check how accurate it is on hand-checked samples; record the change in the change log; and tell your advisor. Report the results under both definitions in the paper.
2. **What if there is still almost no leakage under the new definition?** Then a core assumption the design depends on doesn't hold. Don't give up just yet: a negative result can be a claim in its own right, for example "on these benchmarks, leakage is less common than people tend to fear", provided you can explain why (see [2.7, Section 5](07_analyze-and-interpret.md#5-negative-and-unexpected-results)).
3. **What if nobody cares about that negative claim either?** Go back to [Converging on a project](../01_find-a-problem/05_converge.md#judgment-calls) and pick another candidate conclusion. The leakage-detection pipeline and benchmark data you have already built can still be used for the new candidate.

Whichever path you take, update the skeleton following Section 4: on path 1, change the "leakage" row of the evidence plan; on path 2, revise the claim sentence first; on path 3, archive the old skeleton.

**Write it down:** Take a surprise your own project ran into recently, walk it through the three steps above, and write down your judgment at each step.

---

## Judgment calls

**When you can't tell which option to choose**, ask one question first: can you write down why this idea is doomed `[Our analysis]`?

- If you can't: continue, or adjust starting from the smallest layer.
- If you can, but the reason concerns only one implementation or one definition: adjust.
- If you can, and the reason concerns the claim itself: go back to Part 1, and decide with your advisor whether to narrow the claim, change the angle, or change the problem.

**Who makes the call?** Revising the claim or switching problems should always be discussed with your advisor; don't decide quietly on your own (see [2.6, Judgment calls](06_run-and-iterate.md#judgment-calls)).

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Setting no decision points and pushing through to the end | Problems only surface when you write the paper `[Our analysis]` |
| Treating going back as failure and not daring to mention it | Going back is a normal part of research[^nanda2025process-e6] |
| Switching problems the first time something goes wrong | Only one implementation failed[^steinhardt2018stochastic-e10]; switching too often is the more common mistake[^schulman2020opinionated-e13] |
| Lowering your goals again and again but refusing to stop | It's a sign you aren't making progress[^dredze2012successful-e5] |
| Adjusting a definition or method without recording it | Neither your readers nor you can tell which conclusions were affected `[Our analysis]` |
| Revising the claim without updating the results tables and evidence plan | When you write the paper, the skeleton and the conclusions don't match `[Our analysis]` |

## What you should have at the end

- A decision log: the date, what you saw, your choice, and the reason for each decision (Section 1)
- A paper skeleton updated after every decision: the one-sentence claim, results tables, evidence plan, and contribution list (Section 4)
- The plan's change log, with big changes confirmed with your advisor (Section 3)

## Checklist before moving on

- [ ] You know which row of the master table you are in right now
- [ ] Every time you continued, you had criteria written in advance to back it
- [ ] Every time you adjusted, you started from the smallest layer and recorded it in the change log
- [ ] Every time you decided to go back, you could write down why the claim doesn't hold
- [ ] The paper skeleton matches your latest decision
- [ ] Your advisor knows about every decision to revise the claim or switch problems

## When to go back

This whole chapter is a summary of where to go back to. Depending on the situation, return to:

| If this happens | Go back to |
|---|---|
| Details went wrong, or the measurement is unreliable | [The smallest version that runs end to end](05_pilot-and-derisk.md#judgment-calls) |
| The data you have can't answer the research question | [From research questions to an evidence plan](01_question-to-evidence.md) |
| You can't get the data or tools you need | [Choosing a method](02_choose-method.md) |
| A threat to validity you didn't anticipate has come up | [Validity and limitations: think them through at the design stage](04_validity-and-limits.md) |
| There have been so many changes that the plan no longer fits | [Writing a research plan](03_research-plan.md#7-how-the-plan-changes) |
| The data has errors and needs to be rerun | [Running and iterating](06_run-and-iterate.md) |
| The claim doesn't hold, or you've found a better problem | [Converging on a project](../01_find-a-problem/05_converge.md#judgment-calls) |
| None of your candidates holds up | [Generating candidate problems](../01_find-a-problem/02_generate-problems.md) |

## Next

Once the results tables are full and every conclusion points to its evidence, the project is done. The next step is to turn the paper skeleton into a story. See [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md).

[^nanda2025process-e6]: Nanda 2025a, Distillation (Stage 4). [Evidence](../../sources/notes/nanda2025process.md#e6)
[^thabane2010tutorial-e3]: Thabane et al. 2010, §6 Criteria for Success. [Evidence](../../sources/notes/thabane2010tutorial.md#e3)
[^thabane2010tutorial-e8]: Thabane et al. 2010, §7 Frequently asked questions. [Evidence](../../sources/notes/thabane2010tutorial.md#e8)
[^steinhardt2018stochastic-e10]: Steinhardt 2018, Exponentially branching search trees. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e10)
[^steinhardt2018stochastic-e22]: Steinhardt 2018, Additional Discussion. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e22)
[^schulman2020opinionated-e13]: Schulman 2020, When to Switch Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e13)
[^dredze2012successful-e5]: Dredze & Wallach 2012 (v1.2), #34, p. 6. [Evidence](../../sources/notes/dredze2012successful.md#e5)
[^perez2024tips-e2]: Perez 2024, General Mindset Tips. [Evidence](../../sources/notes/perez2024tips.md#e2)
[^nanda2025mindsets-e1]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e1)
[^eisnerfirst-e5]: Eisner 2010, Write the Paper First, What needs to be done? [Evidence](../../sources/notes/eisnerfirst.md#e5)
[^eisnerfirst-e6]: Eisner 2010, Write the Paper First, What needs to be done? [Evidence](../../sources/notes/eisnerfirst.md#e6)
[^zhang2014ten-e8]: Zhang 2014, Rule 1: Make It a Driving Force. [Evidence](../../sources/notes/zhang2014ten.md#e8)
[^peytonjones2013write-e1]: Peyton Jones 2013, slide "Writing papers: model 2". [Evidence](../../sources/notes/peytonjones2013write.md#e1)
[^peytonjones2013write-e12]: Peyton Jones 2013, slide "Do not be intimidated". [Evidence](../../sources/notes/peytonjones2013write.md#e12)
[^peytonjones2013write-e4]: Peyton Jones 2013, slide "State your contributions". [Evidence](../../sources/notes/peytonjones2013write.md#e4)
