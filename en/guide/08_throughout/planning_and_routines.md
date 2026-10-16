# Planning and daily routines

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science. Most of the sources cited here are personal-experience essays by computer science and machine learning researchers; only one is an experimental study. Treat them as suggestions worth trying, not as rules that hold for every researcher. Once you have tried them, adjust based on your own log. `[Our analysis]`

## When you need this page

You already have a research plan, yet each day you sit down without knowing what to do first, and at the end of the week you can't say how far the project moved. Or your time gets chopped up by meetings and messages, you are juggling two or three projects, and the plan you wrote hasn't been opened in a month.

This page is about turning the plan into days, weeks, and months. How to make the plan itself (the finish line, milestones, what counts as "done", ordering, time estimates) is covered in [Writing a research plan](../01_from-interest-to-project/04_research-plan.md) and not repeated here.

---

## 1. Daily: set today's goal when you start, write "next step" before you stop

**How:**

- **When you start, read the last entry in your log, then write today's goal.** Today's goal is the bottom layer of the goal hierarchy in your research plan (measured in days; see [Writing a research plan, Section 5](../01_from-interest-to-project/04_research-plan.md#5-estimate-time-and-build-in-slack)). Write down what you will have in hand at the end of today that you don't have now. For example, "manually check the first 20 of the 50 samples and note why my judgments disagreed", not "work on leakage detection" `[Our analysis]`.
- **Keep a research log as you work.** Write down your ideas and experiments every day[^schulman2020opinionated-e16]. Also note how long you expected each task to take and how long it actually took; you will need this for the weekly review (Section 4). For how to keep the log and how it differs from your other notes, see [Organizing your research materials, Section 5](organizing_materials.md#5-keep-three-kinds-of-notes-apart) and [Running and iterating, Section 3](../03_conduct-and-analyze/01_run-and-iterate.md#3-leave-a-record-of-every-run).
- **When a new idea pops up, add it to your idea list and go back to what you were doing**[^carlini2024logfile-e2].
- **Before you stop, write one line of "next step":** where you stopped today and the first thing to do tomorrow. Tomorrow morning, this line is the "last entry" you read `[Our analysis]`.

**Why:** `[Our analysis]` The log is the raw material for every review that comes later. Without daily notes, the weekly review runs on memory, and memory favors what was recent and what went well. The "next step" line saves you half an hour of trying to remember where you left off.

**Where people go wrong:** `[Our analysis]`

- Logging only what you did, not what you saw and what you made of it. A few weeks later you know you ran an experiment but not what it showed.
- Writing the daily goal as an activity, such as "read the code" or "tune hyperparameters". After a full day you can't say whether you finished.

**Write it down:** When you start tomorrow, write one sentence: "By the end of today I will have …". Before you stop, write one line of "next step".

## 2. Each week, block out long stretches for the hardest work

**How:**

1. **First, see where your time actually goes.** One researcher honestly logged his days and was shocked to find that, after subtracting interruptions, email, web surfing, phone calls, unproductive meetings, and chatting, he averaged only half an hour of research a day[^nielsen2004principles-e2]. When your time and your output don't seem to match, keep a time log for a while[^dredze2012successful-e1]: record where the time went, then think back on how you could do it faster next time[^nanda2025mindsets-e13].
2. **Block out long stretches on your calendar.** A calendar turns time into visible boxes and makes it obvious that time is finite[^parikh2018calendar-e1]. Start by blocking the few half-days in the week when you are most alert, and keep them for the work that needs sustained thinking: deriving proofs, designing experiments, writing the core of a paper `[Our analysis]`.
3. **Do one thing per block, and break it down in advance.** Split the task into small steps beforehand (for how fine, see [Writing a research plan, Section 5](../01_from-interest-to-project/04_research-plan.md#5-estimate-time-and-build-in-slack)), so that when the block starts you already know the first step and don't have to work it out on the spot `[Our analysis]`.
4. **Batch the small stuff.** Answering email, reading messages, filling in forms, and fixing formatting go into the scattered time outside your blocks `[Our analysis]`.

**Why:** The half-day unit comes from an essay by Paul Graham, a programmer turned startup founder and investor. He writes that people who program or write generally prefer to use time in units of at least half a day; an hour is barely enough to get started[^graham2009makers-e1]. A single meeting can blow a whole afternoon by breaking it into two pieces, each too short to do anything hard in[^graham2009makers-e2]. The damage also spreads backward: if he knows the afternoon will be broken up, he is less likely to start something ambitious in the morning[^graham2009makers-e3].

**Scope:** This is one person's experience, not a survey of researchers. How long a block research needs is something our sources for this page do not cover. Start with half a day and adjust based on your own log `[Our analysis]`.

**Where people go wrong:** Filling the whole week with blocks from day one, then losing half of them to meetings and classes and giving up on blocking altogether after a few weeks. Start with two or three half-days a week; blocks you can protect matter more than blocks you schedule `[Our analysis]`.

**Write it down:** Open next week's calendar, block out two or three half-days, and label each with the one thing you will do in it.

## 3. Handling interruptions: write it down, then come back

Interruptions are normal: your advisor needs you, a collaborator messages you, the server goes down, a class gets added. What you can do is cut the unnecessary ones and make each one cost less.

**How:** `[Our analysis]`

| Source of the interruption | What to do |
|---|---|
| A sudden new idea | Add it to your idea list and go back to what you were doing[^carlini2024logfile-e2] |
| Messages and email | Turn notifications off during blocks; deal with them in fixed slots of scattered time |
| Meetings and discussions | Put them at the start or end of the day if you can, not in the middle of a block. Graham clusters his meeting slots at the end of his working day, so those meetings never interrupt his work[^graham2009makers-e4] |
| Something urgent you must handle now | Before you stop, spend one minute writing in your log where you are and what the next step is; when you come back, pick up from that line |
| A break of several days or more (illness, travel, exam week) | When you return, re-plan the week first instead of forcing the old plan. Re-planning is part of the plan, not a failure[^parikh2018calendar-e3] |

**Why:** In one lab study, 48 participants answered email in a simulated office and were interrupted every two minutes[^mark2008cost-e2]. When interrupted, they actually finished faster, with no difference in quality; but they made up for the interruptions by working faster, at the cost of more stress, frustration, time pressure, and effort[^mark2008cost-e1]. After only 20 minutes of working this way, those feelings were significantly higher[^mark2008cost-e3]. The results were the same whether or not the interruption was related to the task at hand[^mark2008cost-e4].

Keep in mind: the task in this study was answering email, not research, and it lasted only tens of minutes. Our sources for this page do not say whether interruptions cost more or less in research that needs long stretches of sustained thinking.

**Where people go wrong:** Shutting yourself away completely so no one can interrupt you. Working with the door open means you get interrupted, but you also pick up clues about what might be important[^hamming1986you-e18]. What you need to protect is your blocks of time, not cut yourself off from all contact `[Our analysis]`. For why you shouldn't work alone with your head down, see [Mindset and long-term growth, Section 5](mindset_and_growth.md#5-dont-work-alone-with-your-head-down).

**Write it down:** List the three things that interrupted you most last week, and for each, one thing to try next week.

## 4. Weekly review: stop and zoom out

The weekly review connects your daily log to the plan for the whole project. Prioritizing and executing are different mental modes and should not be done at the same time[^nanda2025mindsets-e6]. The weekly review is time set aside just for prioritizing, which leaves you free to put your head down and execute the rest of the week `[Our analysis]`.

**How:** At a fixed time each week (say, the last hour of Friday afternoon), go through these five steps `[Our analysis]`:

1. **Read this week's log and boil it down to a few lines:** what you found, what you now understand differently, what you finished, what comes next. One researcher does this every week or two: reads through all the daily notes and condenses them into a summary[^schulman2020opinionated-e17].
2. **Answer the evidence questions** (against your research plan and paper outline):
   - What is still missing before the next milestone counts as "done"?
   - Which claims are you more confident in now, and which have weakened?
   - What do you do next? Rank the options by how much information you get per unit of time, highest first[^steinhardt2018stochastic-e4].
3. **Answer the time questions**[^nanda2025mindsets-e8]:
   - What has taken the most time recently?
   - What blocked me?
   - What mistakes did I make, and how could I systematically change my approach so they don't happen again?
4. **Plan next week.** Compare this week's estimated time with the actual time and work out the "actual / estimated" multiplier[^parikh2018calendar-e2]. Break next week's work into small chunks, estimate each one using the multiplier, and put them into open slots on your calendar. For how to measure and use your estimation bias, see [Writing a research plan, Section 5](../01_from-interest-to-project/04_research-plan.md#5-estimate-time-and-build-in-slack).
5. **Take the summary to your advisor.** Open your meeting with it; if you think a milestone is slipping, say so early. For how to run the meeting and how to deliver bad news, see [Collaboration and advisors, Section 3](collaboration_and_advisors.md#3-report-progress-early-including-bad-news).

**Why:** A weekly review can be extremely useful: you zoom out and check on overall progress and current problems[^nanda2025mindsets-e7]. Without one, you keep executing without knowing whether you are executing the thing that matters most `[Our analysis]`.

**Where people go wrong:** `[Our analysis]`

- Reviewing only how much you did and how much time it took. Time is secondary; the focus is evidence: what is still missing before you meet your definition of done.
- Changing nothing after the review. The output of a review should be a revised schedule for next week and, when needed, a revised plan.

**Write it down:** Copy the five steps above into a template and use it for your first review this week.

## 5. Monthly: keep the plan alive

The most common fate of a research plan is not being overturned but being forgotten: you are busy running experiments every day and don't open it for months `[Our analysis]`.

**How:** Once a month, spend an extra hour or two on top of that week's review `[Our analysis]`:

- **Reread your one-page project summary and research plan.** Is the central claim still the same sentence? Which milestone has overrun its slack? If something needs changing, follow the order in [Writing a research plan, Section 7](../01_from-interest-to-project/04_research-plan.md#7-how-the-plan-changes): claim first, then milestones, and only then the timeline.
- **Read the month's weekly summaries together.** Looking back over several months, you may find you kept jumping between ideas and left a few half-finished projects, none followed through to a result[^schulman2020opinionated-e18].
- **Set aside some time for big questions.** Think beyond the next milestone about what matters in your field; see [Mindset and long-term growth, Section 4](mindset_and_growth.md#4-make-time-to-think-about-important-problems-and-dare-to-start).
- **Get someone to help you keep the rhythm.** Each month, send your advisor or a collaborator a note on how the plan has changed. For why being accountable to others helps self-discipline, see [Collaboration and advisors, Section 5](collaboration_and_advisors.md#5-working-with-peers-and-people-outside-your-group).

**Why:** Most of the time, moving is better than standing still, provided you regularly take time to reflect and reconsider your goals[^nielsen2004principles-e3]. For why a plan is bound to change, see [Writing a research plan, Section 7](../01_from-interest-to-project/04_research-plan.md#7-how-the-plan-changes).

**Where people go wrong:** Each month, just pushing the overdue dates back. If you only change the dates and not the content, you haven't answered "why am I behind?", and the plan soon drifts away from reality `[Our analysis]`.

**Write it down:** Pick a day in the last week of each month on your calendar, label it "monthly review", and list this section's four items under it.

## 6. When you have several projects at once

A year or two into graduate school, you will likely have a main project, a collaborative project, and assorted smaller tasks all at once.

**How:**

- **Decide what is main and what is secondary.** The main project gets most of your blocks; secondary projects use waiting time: waiting for experiments to finish, for data, for someone to reply `[Our analysis]`.
- **Switch by the day, not by the hour.** To reduce switching back and forth, one researcher generally works on only one project per day[^ruder2020tips-e2].
- **Give each project its own log and its own "next step" line**, and go through them one by one in the weekly review `[Our analysis]`.
- **Budget for new ideas.** One researcher suggests setting a fixed time budget for new ideas that stray from your main line[^schulman2020opinionated-e21], while the main line carries on as usual `[Our analysis]`.

**Where people go wrong:** `[Our analysis]` Starting more and more projects and moving each one only a little; or letting a secondary project gradually eat the main project's blocks. In each weekly review, check: how many half-days did the main project get this week?

> **Where sources disagree: one project at a time, or two?**
>
> - **For working on two at once:** when one project hits a wall, you can switch to the other and avoid getting stuck and frustrated[^ruder2020tips-e1]. The two can also differ in risk: one safe, one riskier but with potentially bigger impact, with the safe one making sure you graduate[^ruder2020tips-e9]. This is the author's own experience.
> - **Warning about the cost of switching and distraction:** a new idea always looks more tempting than the old one you have worked on for months, and it is easy to get distracted just because it is new[^carlini2026best-e15]. If you keep switching and never explore anything properly, you learn nothing[^nanda2025mindsets-e1]. Looking back over several months, you may have only a few half-finished projects to show[^schulman2020opinionated-e18]. These authors do not directly argue against running two projects; they warn about problems that tend to appear once you have many.
>
> In practice `[Our analysis]`: as a beginner, first make sure **one main project** gets finished. Add a small secondary project only when the main one often has to wait (for data, equipment, or other people). If at the monthly review you can't say how far each of the two projects moved, pause one. For when to drop a direction, see [Running and iterating, Section 6](../03_conduct-and-analyze/01_run-and-iterate.md#6-persist-or-change-direction).

**Write it down:** List every project and task you have, mark which is the main project, and note how many half-days a week it gets.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Writing the daily goal as an activity | After a full day you can't say whether you finished `[Our analysis]` |
| Not keeping a log, reviewing from memory | You can't see whether you are jumping between ideas and leaving a pile of half-finished projects[^schulman2020opinionated-e18] |
| Assuming you do research every day | One researcher who logged his time honestly found that, after all the interruptions, he did only half an hour of research a day[^nielsen2004principles-e2] |
| Putting meetings in the middle of a block | One meeting can split an afternoon into two pieces, neither long enough for hard work[^graham2009makers-e2] |
| Trying every new idea as soon as it appears | New ideas often look tempting only because they are new[^carlini2026best-e15]; add them to your idea list first[^carlini2024logfile-e2] |
| Prioritizing while executing | These are different mental modes and should not be done at the same time[^nanda2025mindsets-e6] |
| Estimating time by gut and never checking against reality | You don't know your own bias; measuring the "actual / estimated" multiplier is much easier[^parikh2018calendar-e2] |
| Only pushing dates back when the plan slips | You haven't answered "why am I behind?", so the plan soon drifts from reality; see [Writing a research plan, Section 7](../01_from-interest-to-project/04_research-plan.md#7-how-the-plan-changes) `[Our analysis]` |
| Running many projects at once and switching by the hour | If you keep switching and never explore anything properly, you learn nothing[^nanda2025mindsets-e1]; one researcher works on only one project per day to cut down on switching[^ruder2020tips-e2] |

## Further reading

- **Schulman, "An Opinionated Guide to ML Research"** (2020): the section "Keep a Notebook, and Review It" covers the research log and a review every week or two. Written for machine learning researchers.
- **Nanda, "My Research Process: Key Mindsets"** (2025): the Prioritisation section has three levels of goals and questions for the weekly review. Written for machine learning researchers.
- **Parikh, "Calendar. Not to-do lists."** (2018): read this when there is never enough time and your plans keep falling through.
- **Graham, "Maker's Schedule, Manager's Schedule"** (2009): a one-page essay by a startup founder on why one meeting can ruin an afternoon and how to cluster meetings together.
- **Carlini, "My research idea logfile, 2016-2019"** (2024): how to keep an idea list in practice, with the author's real list from several years.
- **Nielsen, "Principles of Effective Research"** (2004): the Self-discipline section covers time logging and being accountable to others.

[^carlini2024logfile-e2]: Carlini 2024, A bit more detail. [Evidence](../../sources/notes/carlini2024logfile.md#e2)
[^carlini2026best-e15]: Carlini 2026, While doing the best-paper-worthy research › Re-prioritize projects ruthlessly. [Evidence](../../sources/notes/carlini2026best.md#e15)
[^dredze2012successful-e1]: Dredze & Wallach 2012 (v1.2), #16, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e1)
[^graham2009makers-e1]: Graham 2009, paragraph introducing the two kinds of schedule. [Evidence](../../sources/notes/graham2009makers.md#e1)
[^graham2009makers-e2]: Graham 2009, "meetings are a disaster" paragraph. [Evidence](../../sources/notes/graham2009makers.md#e2)
[^graham2009makers-e3]: Graham 2009, "one meeting can sometimes affect a whole day" paragraph. [Evidence](../../sources/notes/graham2009makers.md#e3)
[^graham2009makers-e4]: Graham 2009, "office hours" paragraph. [Evidence](../../sources/notes/graham2009makers.md#e4)
[^hamming1986you-e18]: Hamming 1986, section on "door open / door closed". [Evidence](../../sources/notes/hamming1986you.md#e18)
[^mark2008cost-e1]: Mark, Gudith & Klocke 2008, Abstract. [Evidence](../../sources/notes/mark2008cost.md#e1)
[^mark2008cost-e2]: Mark, Gudith & Klocke 2008, Experimental Design and Procedure. [Evidence](../../sources/notes/mark2008cost.md#e2)
[^mark2008cost-e3]: Mark, Gudith & Klocke 2008, Discussion and Conclusions. [Evidence](../../sources/notes/mark2008cost.md#e3)
[^mark2008cost-e4]: Mark, Gudith & Klocke 2008, Discussion and Conclusions. [Evidence](../../sources/notes/mark2008cost.md#e4)
[^nanda2025mindsets-e1]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e1)
[^nanda2025mindsets-e6]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e6)
[^nanda2025mindsets-e7]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e7)
[^nanda2025mindsets-e8]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e8)
[^nanda2025mindsets-e13]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e13)
[^nielsen2004principles-e2]: Nielsen 2004, Self-discipline. [Evidence](../../sources/notes/nielsen2004principles.md#e2)
[^nielsen2004principles-e3]: Nielsen 2004, The skills of the problem-solver. [Evidence](../../sources/notes/nielsen2004principles.md#e3)
[^parikh2018calendar-e1]: Parikh 2018, Philosophy. [Evidence](../../sources/notes/parikh2018calendar.md#e1)
[^parikh2018calendar-e2]: Parikh 2018, Principle 2. [Evidence](../../sources/notes/parikh2018calendar.md#e2)
[^parikh2018calendar-e3]: Parikh 2018, Principle 4. [Evidence](../../sources/notes/parikh2018calendar.md#e3)
[^ruder2020tips-e1]: Ruder 2020, Work on two things. [Evidence](../../sources/notes/ruder2020tips.md#e1)
[^ruder2020tips-e2]: Ruder 2020, Work on two things. [Evidence](../../sources/notes/ruder2020tips.md#e2)
[^ruder2020tips-e9]: Ruder 2020, 3) Be ambitious. [Evidence](../../sources/notes/ruder2020tips.md#e9)
[^schulman2020opinionated-e16]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e17)
[^schulman2020opinionated-e18]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e18)
[^schulman2020opinionated-e21]: Schulman 2020, When to Switch Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e21)
[^steinhardt2018stochastic-e4]: Steinhardt 2018, A Better Strategy: Sorting by Information Rate. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e4)
