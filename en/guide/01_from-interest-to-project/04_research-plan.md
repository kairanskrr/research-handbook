# Writing a research plan

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

## Where you are

You have a one-page project summary (see [Converging on a project](03_converge.md)). You know which sentence you want to prove, why it is worth doing, how you differ from the closest work, what evidence you need, and which part you are least sure of. Your advisor has read it and has no fundamental objection.

But the summary only says **what you want to achieve**, not **how you will get there step by step**. You may be facing questions like these:

- What do I do first? Data, method, evaluation: each one seems to need the others in place first.
- There are a few months until submission. Is that enough time?
- How far do I have to get before I can stop and write the paper?
- My advisor says "just start and see", but I don't feel confident about it.

## What this stage is for

Turn the one-page summary into a plan **you can follow and can change at any time**. Concretely, answer these six questions:

1. Where is the finish line: where do I plan to submit, and what is the latest date I must submit by?
2. What evidence do I need to collect along the way? Each piece of evidence is a milestone.
3. For each milestone, what counts as done?
4. Which one do I do first?
5. How long will each step take? Where does the slack go?
6. Does my advisor agree with the plan? What happens when the plan changes?

The plan doesn't need to be long. Looking back on their projects, some researchers regret "trying to plan too much at the beginning and never getting started"[^turingwaydesign-e3], while others regret "not setting short- and long-term milestones"[^turingwaydesign-e2]. This chapter aims for the middle ground: detailed for the near term, rough for later, one or two pages in total `[Our analysis]`.

---

## 1. Fix the finish line: where to submit and when

**Ask yourself first: what will this project finally deliver, to whom, and by when at the latest?**

For most projects the finish line is a paper; it could also be a chapter of your thesis or a final project report. Fixing it means answering three things `[Our analysis]`:

| What to decide | Example |
|---|---|
| What you deliver | A conference paper; Chapter 3 of your thesis |
| To whom | Who the readers are; which kind of conference or journal you plan to submit to |
| By when at the latest | A conference deadline, your defense date, the end date of a grant |

**Why decide where it goes first?** A paper should first choose its target audience and a matching journal; that decides who the main message is written for[^zhang2014ten-e7]. Different readers value different evidence, and you will write differently for them `[Our analysis]`. For how to choose a conference or journal, see [Choosing a venue and submitting](../04_write-and-publish/02_venue-and-submission.md).

**In computer science, the deadline is often a hard constraint.** According to the 2009 editor-in-chief of Communications of the ACM (the flagship magazine of the Association for Computing Machinery), computing may be the only field that treats conference papers as the main way to publish research results[^vardi2009conferences-e1]. Conferences have fixed deadlines. Take the machine learning conference NeurIPS 2025 (Conference on Neural Information Processing Systems): the abstract deadline was May 11, 2025, and the full paper deadline was May 15[^neurips2025cfp-e1]. Miss it and you wait for the next conference `[Our analysis]`.

**Other fields can run on a completely different rhythm.** In fields where journals dominate, there is often no shared deadline, and most of the time goes into waiting for reviews and revising `[Our analysis]`. Two sets of sourced figures give you a feel for it:

- Philosophy: the journal submission surveys collected by the American Philosophical Association are self-reported by authors, and most journals publish no data that could verify them[^andrews2024journal-e2]. Looking only at surveys from the last five years (roughly 2019–2023)[^andrews2024journal-e3], journals took an average of 3.22 months to give an initial decision[^andrews2024journal-e5].
- Economics: Ellison looked at the top economics journals from 1970 to 1999; by the late 1990s, review plus revision took about two years per paper on average[^ellison2002slowdown-e1][^ellison2002slowdown-e2].

In that case, work backward from your defense, the end of your grant, or a submission date you set yourself `[Our analysis]`.

**Work backward from the finish line.** Take a conference: a deadline three months away means you have to start writing the paper at least a month before it[^parikh2018calendar-e5]; before that comes the date by which you must have your main results `[Our analysis]`. But be careful: working backward gives you the **latest** date each thing must be finished, not when to start it. Treat it as a start date and you have no slack at all[^parikh2018calendar-e6].

A backward schedule using the "large language models and smart contract security" example `[Our analysis]`:

```
Deadline                                ← finish line
2 weeks before    internal deadline: full draft to advisor for review (see Section 5)
1 month before    latest start on writing the full draft
2 months before   latest date to have the main experimental results
3 months before   latest date to confirm the core method works   ← how far is today from here?
```

If working backward shows that the "confirm it works" date has already passed, decide now: shrink the claim, aim for a later venue, or both (see "Judgment calls" in this chapter).

**Write it down:** Your finish line: what you will deliver, which kind of venue you plan to submit to, and the latest date. Then work back three or four checkpoints from that date and mark, for each, "what must be done by then at the latest".

## 2. Break the claim into milestones: each milestone is a piece of evidence

Your one-page summary already says "to make people believe it, I need this evidence". The plan starts there: **each key piece of evidence is one milestone.**

```
Central claim → the supporting claims behind it → the evidence each one needs → the work that produces that evidence → what to do this week
```

The upper levels set the direction; the lower levels decide what you do this week `[Our analysis]`.

**Phrase milestones as "evidence I have", not "things I did".** This is the most important point in this chapter `[Our analysis]`:

| Phrased as an activity (bad) | Phrased as evidence (good) |
|---|---|
| Finish the leakage-detection program | The leakage-detection method judges correctly on 50 hand-checked samples, and the misjudged cases can be explained |
| Run all the tools | A table comparing the accuracy of three or more tools before and after removing leaked samples |
| Finish reading related work | A comparison table that says clearly what the closest work is missing |
| Set up the experimental environment | The two existing baseline tools reproduce the results reported in their papers |

Why phrase it this way? You can "finish the program" on schedule while the project hasn't moved forward at all; only "getting initial evidence" actually reduces your uncertainty about the project `[Our analysis]`. The most common outcome of activity milestones: every item gets ticked off on time, and just before submission you discover that none of them can go straight into the paper.

**A handy trick: use the paper outline as your milestone list.** Design the project with the final paper in mind: put a paper outline in your first design document and use it to settle the research goals, the logical order of the experiments, and the materials and data you need to prepare[^zhang2014ten-e8]. In practice, first imagine which figures and tables the paper will have and arrange them in the logical order of the experiments[^zhang2014ten-e10]; these imagined figures and tables, and the logic connecting them, can be used directly to organize the research work[^zhang2014ten-e11].

So you can take the [empty results tables](03_converge.md#4-what-will-make-people-believe-it) you drew in the previous chapter, put them into a paper outline, and give each one a status `[Our analysis]`:

| Figure or table | Which claim it supports | Status |
|---|---|---|
| Table 1: share of leaked samples in the benchmark | Leakage exists | Not started |
| Table 2: accuracy before and after removing leakage | Leakage affected the results | Not started |
| Table 3: accuracy of the leakage-judging method | The judging method is reliable | Preliminary results |

The figures and tables you don't have yet are your milestone list.

**Write it down:** Rewrite each piece of evidence in your one-page summary as a milestone that starts with "I have …". Then map each one to a figure or table in the paper outline. Cross out, for now, any work that doesn't map to a claim.

## 3. For each milestone, write down what counts as done

Once the milestones are phrased as evidence, go one step further: **how complete does this evidence have to be before it counts as obtained?** If you don't spell this out, you will either keep adding experiments to one milestone forever, or move on before the evidence is enough.

**How to write it:** As a sentence you can check, ideally containing three things `[Our analysis]`:

- **Scope**: on which data, which objects, under which conditions;
- **Criterion**: what you look at and what counts as holding up;
- **The negative case**: what it looks like if it doesn't hold, and what you will do if you see that.

Using the milestones above `[Our analysis]`:

| Milestone | What counts as done |
|---|---|
| The leakage-judging method is reliable | On 50 hand-checked samples it largely agrees with the human judgments; every disagreement has been examined one by one and its cause can be explained |
| Leakage affected the results | Accuracy before and after removing leaked samples has been compared for three or more tools; if the difference is small, record that honestly and go back to revise the claim |

**When is the whole project done?** When **every central claim has enough evidence**, not when "there is nothing left to do": research always has a next experiment `[Our analysis]`. A complete paper needs detailed supporting data for every important aspect of its hypothesis[^zhang2014ten-e12]; check your list against that. One regret researchers report when looking back on projects is "not advocating for clearer goals and success criteria from the beginning"[^turingwaydesign-e1].

**Don't treat "the deadline has arrived" as "done".** Computer science has been criticized for being deadline-driven: papers go out when they happen to meet a suitable conference deadline, not when the research has been done thoroughly[^fortnow2009time-e2]. The deadline decides **when you submit**; your "done" criteria decide **whether you submit, and what** `[Our analysis]`. If the deadline arrives and the evidence isn't enough, it is better to aim for the next venue, or to narrow the claim to what the evidence can support.

**And don't define "done" as "results reach some number".** You don't control the results; what you control is whether the evidence is enough and whether the claim matches the evidence `[Our analysis]`.

**Write it down:** For each milestone, one sentence on what counts as done, covering scope, criterion, and the negative case. Then one sentence on what counts as done for the whole project.

## 4. Set the order: do what is most likely to fail first

With a milestone list in hand, the next step is ordering. People often do the easy parts first[^steinhardt2018stochastic-e12]. The result can be that all the easy parts are finished before you hit a fundamental obstacle in a hard part, and the whole plan has to be redone[^steinhardt2018stochastic-e2].

**Ordering rules:**

1. For each milestone, make two rough estimates: **how likely it is to succeed** and **how long it will take**.
2. **Do first the parts that are more likely to fail and take less time.** If something is going to fail, it is better to find out early: you waste less time and get information sooner[^steinhardt2018stochastic-e3]. In one sentence: sort by information gained per unit of time, highest first[^steinhardt2018stochastic-e4].
3. **Then look at dependencies.** Some milestones can't start until another is finished; for example, if the leakage-judging method is unreliable, every comparison that follows is meaningless. Move such foundations earlier even if they aren't hard `[Our analysis]`.

Ordering the example above `[Our analysis]`:

| Milestone | Chance of failure | Time needed | Order |
|---|---|---|---|
| The leakage-judging method is reliable | High (nobody has done it) | Short (hand-check 50 first) | 1st |
| The baseline tools can be reproduced | Medium (some tools may not run) | Short | 2nd |
| Share of leaked samples | Low (just computation once the method is reliable) | Medium | 3rd |
| Comparison before and after removing leakage | Medium | Long | 4th |

Many people are too slow to try to falsify their own ideas[^steinhardt2018stochastic-e12]. Your first milestone should be the thing that, "if it doesn't work, the whole project falls apart". For how to test it first with a cheap small experiment, see [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md).

**Write it down:** Order your milestones. Write down the first one, plus one sentence on what happens to the project if it fails.

## 5. Estimate time and build in slack

**How:**

1. **Set goals at several levels.** The overall project goal is measured in months, the current subgoal in weeks, and the concrete goal right in front of you in days[^nanda2025mindsets-e3]. Milestones usually sit at the weeks level `[Our analysis]`.
2. **Write a plan for at least the current phase and estimate how long each step will take.** You don't have to stick to it rigidly; deviating a lot is normal[^nanda2025mindsets-e4]. Research projects are uncertain by nature and their goals evolve[^turingwaydesign-e7], so estimate near-term milestones in detail and give later ones only a rough direction `[Our analysis]`.
3. **Break near-term milestones into small chunks.** Practice breaking tasks into chunks of roughly 20 minutes to 2 hours[^steinhardt2018stochastic-e16]. Breaking work into chunks, estimating them, and putting them on your calendar is itself a task, and you need to set time aside for it[^parikh2018calendar-e4].
4. **Measure your own estimation bias.** Estimate each task's time in advance, then log how long it actually took[^steinhardt2018stochastic-e16]. Rather than trying hard to estimate accurately, measure your "actual / estimated" multiplier and apply it when you schedule from then on[^parikh2018calendar-e2].
5. **Put the slack between milestones, not spread across every day.** What you worked out backward in Section 1 are the latest dates[^parikh2018calendar-e6]; the target dates in your plan should be earlier, and the gap between them is your slack `[Our analysis]`. Give the most slack to the milestone you are least sure of `[Our analysis]`.

**How much slack?** Our sources do not give a general ratio. If you are new and haven't measured your estimation bias yet, schedule using your estimates at first, log the actual time, and after one or two milestones reschedule using the multiplier you measured `[Our analysis]`.

**Set an internal deadline before the real one.** Some groups require, two weeks before the deadline, a draft of at least 5 pages that includes all the final experiments (the numbers need not be final), and review it internally following the same process as the real peer review[^karpathy2016survival-e8]. Laying out the whole paper early almost always exposes a few key experiments you must add to make the argument coherent and convincing[^karpathy2016survival-e9], and the earlier you find them, the more time you have to run them. If you are submitting to a journal, you can set yourself an internal date for the final draft in the same way `[Our analysis]`.

**Write it down:** Estimate the time for your first two milestones, broken down to weeks. Mark the internal deadline on your plan, and the slack you have left after each milestone.

## 6. Get your advisor on board with the plan

Once the plan is written, go through it with your advisor. This isn't a formality: advisors differ a lot in how they supervise and what they expect from students, so ask directly[^dredze2012successful-e7]. Newcomers find it hard to know what "doing well" looks like; once expectations are clear, you will neither be crushed by imagined standards nor underestimate how much work it takes[^vinitskyexpectation-e1].

**Bring a draft; don't show up empty-handed asking "what should I do next?"** Based on your own judgment, propose a few things in priority order and explain why[^huang2023advisor-e6].

**What to agree on with your advisor** `[Our analysis]`:

| What to agree on | How you might ask |
|---|---|
| The finish line | "I plan to submit to such-and-such kind of conference; the deadline is this date. Does that seem right to you?" |
| Milestones and order | "I plan to validate the leakage-judging method first, because if it doesn't work, nothing after it holds up." |
| What counts as done | "If I get this far, do you think it's enough to submit?" |
| Checkpoints | "When the first milestone is done, let's look at the results together and decide whether to continue or adjust." |
| When to change the plan | "If a milestone runs past its slack and still isn't done, I'll tell you right away." |

You can also tell your advisor about your working habits and preferences, so they understand you better and the two of you work together more smoothly[^dredze2012successful-e15].

**After the meeting, write down what you agreed and send it to your advisor.** Right after the meeting, send a summary of the discussion and the next steps you both agreed on[^huang2023advisor-e7]. When the plan changes, send your advisor the new version too `[Our analysis]`.

**If you are going to miss a deadline, say so early.** If you think you won't make a deadline, be sure to tell your advisor; they would much rather know early[^dredze2012successful-e20].

Your advisor usually has good research instincts, but you know more about this particular problem than they do, sometimes enough to make a better call[^nanda2025mindsets-e15]. So getting on board doesn't mean having your advisor make the plan for you; it means having your advisor check your plan. When you disagree, come with your reasons and the results of a small test `[Our analysis]`. For how to run regular meetings with your advisor and report progress, see [Collaboration and advisors](../08_throughout/collaboration_and_advisors.md).

**Write it down:** Send the draft plan to your advisor and set up a meeting. Afterward, write down the finish line, milestone order, "done" criteria, and the date of your next joint checkpoint that you both agreed on.

## 7. How the plan changes

The plan will change. One regret researchers report looking back on projects is not fully anticipating that requirements change during a project, which is common in academic research[^turingwaydesign-e4]. Using writing to re-examine the project as the research goes on often leads to adjusting the research, revising the design, devising new methods, or collecting new data[^zhang2014ten-e9]. The core hypothesis can change too; check back regularly whether it is still the central idea driving the research[^noble2023ten-e7].

So decide in advance: **in which situations you change the plan, and what you change.** Rescheduling is part of planning, not a failure[^parikh2018calendar-e3].

| What happens | What to change `[Our analysis]` |
|---|---|
| A milestone runs past its slack | Reschedule what follows; tell your advisor; consider cutting secondary milestones |
| The first milestone fails | Don't just change dates; go back to the project itself: does the claim need to change? See "When to go back" |
| The results differ from what you expected but are more interesting | Change the claim and the paper outline first, then the milestones |
| You find an experiment you must add | Add it to the milestone list and reorder following Section 4 |
| The evidence is clearly not enough before the deadline | Narrow the claim, or aim for a later venue (see "Judgment calls") |

When you change the plan, work from the top down: first see whether the claim has changed, then the milestones, and only then the dates `[Our analysis]`. If you change only the dates and not the content, the plan soon drifts away from reality.

**Keep old versions.** Each time you change the plan, add a line saying "what changed and why"; a few months later you can see clearly how the project got where it is `[Our analysis]`.

**Check regularly.** Every week or two, compare against the plan and ask: what is still missing before the next milestone counts as done `[Our analysis]`? For how to do a weekly review and organize your day-to-day time, see [Planning and daily routines](../08_throughout/planning_and_routines.md).

> **Where sources disagree: should you draw a Gantt chart?**
>
> - One recommendation is to build a timeline with key milestones, deliverables, and deadlines, and it lists Gantt charts, roadmaps, and project boards as useful tools[^turingwaydesign-e5].
> - The same source also warns that management approaches that carry out steps one after another in a fixed order are rigid, hard to adjust once started, and not well suited to research[^turingwaydesign-e8].
>
> In practice `[Our analysis]`: a Gantt chart works well for marking **milestones and external deadlines** (submission, defense, end of a grant), so you and your advisor can see the big timing relationships; don't put the exploratory work inside a milestone on the Gantt chart, and let regular check-ins decide the next step instead.

**Write it down:** Add a "change log" section at the end of your plan. Then write two or three triggers of the form "if this happens, I change the plan".

---

## Judgment calls

**When time runs short, what do you cut?** Working backward from the finish line often shows there isn't enough time. Here is one way to decide `[Our analysis]`:

| Situation | What you usually do |
|---|---|
| There is time for the evidence behind the central claim but not the supporting claims | Cut the supporting claims; save them for the next paper or put them under "limitations and future work" |
| There isn't time even for the central claim's evidence | Narrow the central claim: limit the conditions, limit what it applies to |
| The narrowed claim is no longer interesting | Aim for a later venue and finish as originally planned |
| The milestone you are least sure of hasn't been tested and the deadline is close | Test it first; until it is tested, don't force the rest of the work into a schedule built around the deadline |

**How detailed should the plan be?** Detailed enough that you can answer "what am I doing this week, and why". Plan the next milestone down to weeks; beyond that, list only milestones and rough months `[Our analysis]`.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Milestones written as "finish the program", "finish running experiments" | They get done on time while the project may not have moved forward `[Our analysis]` |
| Not writing down what counts as done | The project drags on forever, or you rush to submit without enough evidence `[Our analysis]`; researchers looking back on projects also list not pushing for clear success criteria from the start as a regret[^turingwaydesign-e1] |
| Submitting because the deadline has arrived | When you submit is decided by the deadline, not by whether the research has been done thoroughly[^fortnow2009time-e2] |
| Doing the easy parts first | The hard parts only reveal fundamental problems at the end, and the plan has to be redone[^steinhardt2018stochastic-e2] |
| Treating the latest dates from working backward as planned dates | There is no slack at all[^parikh2018calendar-e6] |
| Estimating time by gut feeling | The estimates are off, and you don't know by how much; measuring your "actual / estimated" multiplier is much easier[^parikh2018calendar-e2] |
| Writing a detailed plan dozens of pages long at the start | You keep putting off starting; research goals change anyway[^turingwaydesign-e3][^turingwaydesign-e7] |
| Laying out the whole paper for the first time on the day of the deadline | Too late to add the missing key experiments[^karpathy2016survival-e9] |
| Once the plan is set, changing only dates, never content | Requirements often change during research, and the design has to change with them[^turingwaydesign-e4]; if you only change dates, the plan soon drifts away from reality `[Our analysis]` |

## What you should have at the end

- A research plan (one or two pages): the finish line, the milestone list and its order, what counts as done for each milestone, the schedule and slack, and the internal deadline
- A paper outline listing the figures and tables each claim needs, and their status (Section 2)
- Meeting notes recording what you agreed with your advisor (Section 6)
- A change log for the plan (Section 7)

## Checklist before moving on

You can move on when all of these hold:

- [ ] You have written down the finish line: what you will deliver, which kind of venue, and the latest date
- [ ] Every milestone is phrased as "I have this evidence" and maps to at least one claim
- [ ] Every milestone has a "done" criterion, and there is one for the whole project
- [ ] The first milestone is the one most likely to make the project fail
- [ ] Near-term milestones have time estimates, planned dates are earlier than the latest dates, and there is slack
- [ ] You have set an internal deadline
- [ ] Your advisor has seen the plan and you have agreed on the date of your next joint checkpoint
- [ ] You have written down the triggers for changing the plan

## When to go back

| If this happens | Go back to |
|---|---|
| While writing milestones, you can't say what some of the evidence should be | [Converging on a project](03_converge.md), Section 4; rethink what evidence you need |
| Working backward shows there isn't enough time no matter how much you narrow the claim | [Converging on a project](03_converge.md), Section 1; pick a smaller claim, or discuss a different venue with your advisor |
| The first milestone fails | [Converging on a project](03_converge.md); first decide whether to change the claim or change the problem |
| Your advisor fundamentally objects to the finish line or the central claim | [Converging on a project](03_converge.md), Section 6; revise the one-page summary |

## Next

Once the plan is settled, the next step is to turn the evidence each milestone needs into a concrete study design: what you need to answer, what data you will use, and how you will judge the results. See [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md).

[^andrews2024journal-e2]: Andrews 2024, Introduction. [Evidence](../../sources/notes/andrews2024journal.md#e2)
[^andrews2024journal-e3]: Andrews 2024, Setup. [Evidence](../../sources/notes/andrews2024journal.md#e3)
[^andrews2024journal-e5]: Andrews 2024, Results of the Journal Surveys: Response Length. [Evidence](../../sources/notes/andrews2024journal.md#e5)
[^dredze2012successful-e7]: Dredze & Wallach 2012 (v1.2), You and Your Advisor, p. 2. [Evidence](../../sources/notes/dredze2012successful.md#e7)
[^dredze2012successful-e15]: Dredze & Wallach 2012 (v1.2), #14, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e15)
[^dredze2012successful-e20]: Dredze & Wallach 2012 (v1.2), #45, p. 8. [Evidence](../../sources/notes/dredze2012successful.md#e20)
[^ellison2002slowdown-e1]: Ellison 2002, §1 Introduction. [Evidence](../../sources/notes/ellison2002slowdown.md#e1)
[^ellison2002slowdown-e2]: Ellison 2002, §2, around Figure 1. [Evidence](../../sources/notes/ellison2002slowdown.md#e2)
[^fortnow2009time-e2]: Fortnow 2009, main text. [Evidence](../../sources/notes/fortnow2009time.md#e2)
[^huang2023advisor-e6]: Jia-Bin Huang 2023, tweet thread, [How to meet with your advisors/mentors?](https://twitter.com/jbhuang0604/status/1653614931202195458), Propose next steps. [Evidence](../../sources/notes/huang2023advisor.md#e6)
[^huang2023advisor-e7]: Jia-Bin Huang 2023, tweet thread, Summarize your meeting. [Evidence](../../sources/notes/huang2023advisor.md#e7)
[^karpathy2016survival-e8]: Karpathy 2016, Writing papers, "An internal deadlines 2 weeks prior". [Evidence](../../sources/notes/karpathy2016survival.md#e8)
[^karpathy2016survival-e9]: Karpathy 2016, ibid. [Evidence](../../sources/notes/karpathy2016survival.md#e9)
[^nanda2025mindsets-e3]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e3)
[^nanda2025mindsets-e4]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e4)
[^nanda2025mindsets-e15]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e15)
[^neurips2025cfp-e1]: NeurIPS 2025 Call for Papers, date list at the top of the page. [Evidence](../../sources/notes/neurips2025cfp.md#e1)
[^noble2023ten-e7]: Noble 2023, Rule 5. [Evidence](../../sources/notes/noble2023ten.md#e7)
[^parikh2018calendar-e2]: Parikh 2018, Principle 2. [Evidence](../../sources/notes/parikh2018calendar.md#e2)
[^parikh2018calendar-e3]: Parikh 2018, Principle 4. [Evidence](../../sources/notes/parikh2018calendar.md#e3)
[^parikh2018calendar-e4]: Parikh 2018, Principle 5. [Evidence](../../sources/notes/parikh2018calendar.md#e4)
[^parikh2018calendar-e5]: Parikh 2018, Principle 6. [Evidence](../../sources/notes/parikh2018calendar.md#e5)
[^parikh2018calendar-e6]: Parikh 2018, Principle 6. [Evidence](../../sources/notes/parikh2018calendar.md#e6)
[^steinhardt2018stochastic-e2]: Steinhardt 2018, Warm-Up. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e2)
[^steinhardt2018stochastic-e3]: Steinhardt 2018, Warm-Up. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e3)
[^steinhardt2018stochastic-e4]: Steinhardt 2018, A Better Strategy: Sorting by Information Rate. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e4)
[^steinhardt2018stochastic-e12]: Steinhardt 2018, Summary. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e12)
[^steinhardt2018stochastic-e16]: Steinhardt 2018, Caveats. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e16)
[^turingwaydesign-e1]: The Turing Way, Overview of Project Design, Learning from Mistakes. [Evidence](../../sources/notes/turingwaydesign.md#e1)
[^turingwaydesign-e2]: The Turing Way, Overview of Project Design, Learning from Mistakes. [Evidence](../../sources/notes/turingwaydesign.md#e2)
[^turingwaydesign-e3]: The Turing Way, Overview of Project Design, Learning from Mistakes. [Evidence](../../sources/notes/turingwaydesign.md#e3)
[^turingwaydesign-e4]: The Turing Way, Overview of Project Design, Learning from Mistakes. [Evidence](../../sources/notes/turingwaydesign.md#e4)
[^turingwaydesign-e5]: The Turing Way, Getting Started Checklist, Timeline & Milestones. [Evidence](../../sources/notes/turingwaydesign.md#e5)
[^turingwaydesign-e7]: The Turing Way, Project Management Methodologies, Summary. [Evidence](../../sources/notes/turingwaydesign.md#e7)
[^turingwaydesign-e8]: The Turing Way, Project Management Methodologies, comparison table. [Evidence](../../sources/notes/turingwaydesign.md#e8)
[^vardi2009conferences-e1]: Vardi 2009, main text, para. 2. [Evidence](../../sources/notes/vardi2009conferences.md#e1)
[^vinitskyexpectation-e1]: Vinitsky, Expectation Setting, opening. [Evidence](../../sources/notes/vinitskyexpectation.md#e1)
[^zhang2014ten-e7]: Zhang 2014, Rule 3. [Evidence](../../sources/notes/zhang2014ten.md#e7)
[^zhang2014ten-e8]: Zhang 2014, Rule 1. [Evidence](../../sources/notes/zhang2014ten.md#e8)
[^zhang2014ten-e9]: Zhang 2014, Rule 1. [Evidence](../../sources/notes/zhang2014ten.md#e9)
[^zhang2014ten-e10]: Zhang 2014, Rule 4. [Evidence](../../sources/notes/zhang2014ten.md#e10)
[^zhang2014ten-e11]: Zhang 2014, Rule 4. [Evidence](../../sources/notes/zhang2014ten.md#e11)
[^zhang2014ten-e12]: Zhang 2014, Rule 5. [Evidence](../../sources/notes/zhang2014ten.md#e12)
