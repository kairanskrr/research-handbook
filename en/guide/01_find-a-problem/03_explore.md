# Exploring hands-on

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. Most of the advice quoted here comes from machine learning researchers.

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Recognize that you are exploring.** If you can't yet write down a specific hypothesis, you are in the exploration stage. Your only goal is to understand the problem, and there is no need to worry that you don't have a hypothesis yet ([Section 1](#1-first-recognize-that-you-are-exploring-not-yet-testing)).
> 2. **For the two or three ideas you most want to pursue, run a small, fast try on each.** Ideally you see a result within a day, for example by simply looking at a batch of real examples. Do the most informative step first ([Section 2](#2-design-small-fast-explorations)).
> 3. **Keep exploration notes as you go.** What you tried, what you saw, what surprised you, what new questions came up. Record the tries that didn't "work" too ([Section 3](#3-keep-exploration-notes)).
> 4. **Give each idea a time limit.** Once you can write a specific hypothesis, move on. Once you stop learning anything new, switch approach or switch idea, and write down why ([Section 4](#4-when-to-stop)).
> 5. **Don't treat what you saw as a conclusion.** Exploration has no criteria set in advance, so its results are only leads. They get tested in Part 2 ([Section 5](#5-exploring-is-not-the-same-as-building-the-smallest-version-that-runs-end-to-end)).
>
> **Done these? Move on:** at least one idea has been turned into a specific hypothesis, and you can say what evidence would decide it; for every idea you dropped, you wrote down why. Next: [Judging and screening ideas](04_judge-and-screen.md).

## Where you are

In [Generating candidate problems](02_generate-problems.md) you built up a list of ideas. Say your research area is "large language models and smart contract security", and your list includes ideas like "the high accuracy of current large language models at vulnerability detection may partly come from benchmark leakage" and "there are so many false positives that developers won't use these tools".

But these ideas are still only on paper. You don't know whether the benchmarks actually leaked, or where the models really go wrong. You may be worried: isn't it reckless to start doing things before you have thought it all through?

## What this stage is for

Use small, fast hands-on tries to turn ideas on paper into "I roughly know what's going on here."

The point of this step is to **gather information and understand the problem**, not to prove anything. So it doesn't aim for rigor; it aims for speed and for seeing a lot. Concretely, it answers four questions:

1. Am I exploring right now, or can I already test a specific hypothesis?
2. How do I design small, fast explorations?
3. What do I write down while exploring?
4. When do I stop?

---

## 1. First, recognize that you are exploring, not yet testing

**Start by asking yourself: can I write down a specific hypothesis right now, and say what evidence would tell me whether it is right?**

- **If you can't**: you are in the **exploration stage**. The goal here is just to gain information: run small experiments, look at the data, follow your curiosity, and move fast[^nanda2025process-e1].
- **If you can**: you are ready for the **testing stage**. You understand the problem well enough to write down specific hypotheses and roughly know what evidence would show whether they are right[^nanda2025process-e5].

When newcomers get stuck early in a project, it is often because they think they are already in the testing stage when they are still exploring[^nanda2025process-e2]. Once you see this, you don't need to worry that you don't have a clear hypothesis yet.

**Why start doing things now, instead of reading and thinking more.** Trying to pick the perfect problem before you have done any hands-on work is a trap: the ability to judge whether a problem is good depends on actually doing the work[^olah2021taste-e9]. Once you have searched for ideas for a while, an extra hour of thinking is worth less than just going and doing something[^carlini2026best-e13].

**Stages can go backward.** If you get further in and find things are messier than you thought, going back to testing or even exploration is normal and doesn't mean you've messed up[^nanda2025process-e6]. If, while running the project in Part 2, you find you can't write down a specific hypothesis, that is also a sign to come back to this chapter.

**Write it down:** for the two or three ideas on your list you most want to pursue, write one sentence each: can I write down a specific hypothesis yet? The ones where you can't are what you explore in this chapter.

## 2. Design small, fast explorations

**The principle: every exploration should be cheap, ideally giving you a result within a day.** Early on, use quick experiments that finish within a day to try out lots of ideas[^perez2024tips-e3]. Spending a little time to see early signs is far better than spending weeks on an expensive, slow experiment with a clear-cut conclusion[^nanda2025mindsets-e11].

**Some common approaches:**

- **Simply look at a batch of real examples.** If you want to use a dataset, say, first download a few thousand items, look at some of them by hand, compute a few summary statistics, and see whether it has the properties you want[^steinhardt2018stochastic-e6].
- **Think about a simplified version first.** When the problem is too big to know where to start, think about a simpler version of it, such as looking at only one kind of vulnerability. The simplified version often suggests how to tackle the original problem, and how not to[^steinhardt2018stochastic-e8].
- **Do the most informative step first.** When there are several things you could try, rank them by how much information each gives per unit of time, and work down from the top[^steinhardt2018stochastic-e4].
- **Ask yourself: if this direction is doomed, how can I find out fastest?**[^nanda2025mindsets-e12]

**What "not aiming for rigor" means** `[Our analysis]`: while exploring you don't need a large sample, criteria fixed in advance, statistical tests, or clean code. But you do need to record what you did and what you saw (Section 3), because the impressions you get from exploring are only leads and can't be taken straight as conclusions.

**The smart contract example** `[Our analysis]`: of the ideas on your list, "benchmark leakage" is the one you are most curious about. Each of the explorations below can be done in a day or two:

| What you want to understand | A small, fast exploration |
|---|---|
| What the model actually says when it reads a contract, and where it goes wrong | Pick a few dozen contracts at random, give them to the model, and read its answers |
| Whether the contracts in the benchmark were public long ago | Sample a few contracts from the benchmark and search public code platforms for their key code snippets |
| Whether the model "remembers" these contracts | Give it only the first half of a contract and see whether it can write out the second half |
| Whether there are many false positives | Take a few contracts known to have no vulnerabilities and see how many "vulnerabilities" the model reports |

After doing these, you might find that several of the benchmark contracts you sampled turn up almost verbatim in public code. That is not a conclusion yet, but it lets you write down a specific hypothesis for the first time (Section 4).

**Write it down:** for each idea you will explore, write down one small try you can finish in a day or two: what you want to understand, what exactly you will do, and roughly how long it will take.

## 3. Keep exploration notes

What you find while exploring comes in bits and pieces. If you don't write it down, a few days later you won't be able to tell which thing you saw in which run.

**How to keep them:**

- **Write as you go.** While running experiments, keep a document open, and as results come in, add the figures and numbers along with your own observations and impressions[^perez2024tips-e4]. Keep each day's ideas and experiments in the same notebook[^schulman2020opinionated-e16].
- **Keep a separate highlights file** just for especially interesting results, so it is easier to spot connections between them[^nanda2025process-e4].
- **Record the tries that didn't "work" too.** What matters is whether you are learning about the problem; as long as you are learning, an experiment that didn't "succeed" still gained you something[^perez2024tips-e1].

Each note can have these fields `[Our analysis]`:

| Field | Example |
|---|---|
| Date, what you tried | Oct 3: sampled 20 contracts from the benchmark and searched public code platforms for key snippets |
| What you saw | 7 turned up nearly identical code |
| What surprised you | Most of the matches were uploaded years ago, before the model's training data cutoff |
| New questions | Are other benchmarks like this too? Does the model answer leaked contracts more accurately? |
| Next step | Try sampling from another benchmark |

Your exploration notes are the seed of the research log you will keep in Part 2. Once you reach the testing stage, your records need to be more complete; see [Organizing your research materials](../08_throughout/organizing_materials.md#3-every-result-must-be-traceable-to-how-it-was-produced) `[Our analysis]`.

**Write it down:** set up your exploration notes and your highlights file. Each time you finish a small try, fill in one row of the table above.

## 4. When to stop

Exploring longer isn't always better. Two kinds of signal tell you it is time to stop.

**Signal 1: you can write down a specific hypothesis and know what evidence would decide it.** That is exactly the mark of moving into the testing stage[^nanda2025process-e5]. For example `[Our analysis]`: "A sizable share of the contracts in public benchmarks were already public before the model was trained; with those contracts removed, the model's detection rate drops noticeably." You also know what evidence you need: what share of contracts leaked, and how much accuracy changes when you remove them. At this point, take that sentence into [Judging and screening ideas](04_judge-and-screen.md). If this is your only remaining candidate and you have already talked it over with your advisor, you can go straight to [Converging on a project](05_converge.md).

**Signal 2: you are no longer learning anything new for the time you put in.** Keep asking yourself, "Am I getting enough information per unit of time?" If you haven't learned anything new lately, try something different[^nanda2025process-e3]. When a project's returns keep shrinking, switching projects is perfectly fine[^perez2024tips-e2]. There are two kinds of switch `[Our analysis]`:

- **Switch approach**: keep the same idea but explore it another way, for example moving from "reading the model's answers" to "tracing where the benchmark contracts came from";
- **Switch idea**: if several approaches have taught you nothing new, put the idea back on the list with a note on why, and explore the next one.

**But don't switch too often either.** Be decisive about dropping directions that should be dropped, but watch the cost of switching: if you keep switching and never explore anything properly, you learn nothing[^nanda2025mindsets-e1]. Some people go down a rabbit hole and need to learn to move on; others keep waiting for a perfect opportunity that never comes and do nothing[^nanda2025mindsets-e9].

A practical rule `[Our analysis]`: give the exploration of each idea a time limit, say one to two weeks. When time is up, apply the two signals above: if you have a hypothesis, move on; if you have stopped learning, switch; if you are somewhere in between, talk it over with your advisor once and then decide.

**Write it down:** write down a time limit for each idea you are exploring. When it runs out, write one sentence: what hypothesis you came up with, or why you are switching.

## 5. Exploring is not the same as building "the smallest version that runs end to end"

[The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md) in Part 2 also involves small experiments, such as [building a minimal version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md#3-build-a-minimal-version-that-runs-end-to-end). The two look alike, but their purposes differ `[Our analysis]`:

| | Exploring hands-on (this chapter) | The smallest version that runs end to end (Part 2) |
|---|---|---|
| Purpose | Understand the problem and find a hypothesis worth testing | Test a hypothesis you have already written down and rule out the biggest risks in the design |
| What you start with | A vague idea | A specific claim and an empty results table |
| Criteria set in advance? | No, follow your curiosity | Yes, write down in advance [what results mean continue, adjust, or stop](../02_do-the-project/05_pilot-and-derisk.md#5-write-down-in-advance-what-results-mean-continue-adjust-or-stop) |
| Records | Exploration notes: what you saw and what you thought | Formal records begin: every result traceable to its code, data, and parameters |
| How the results are used | Only as leads that help you write a hypothesis | To decide whether the design needs to change |

The most common confusion is treating a few examples you saw while exploring as a conclusion you have already tested. A hunch that comes out of exploring has to be tested again in Part 2, using a method fixed in advance `[Our analysis]`.

**Write it down:** go back through your exploration notes and mark which entries are just "things I saw" and which are getting close to "a hypothesis I could test".

---

## Judgment calls

**Explore more, or move on?** Here is one way to decide `[Our analysis]`:

| Situation | What to do |
|---|---|
| You can write a specific hypothesis and know what evidence would decide it | Move on to [Judging and screening ideas](04_judge-and-screen.md) |
| Every try turns up something new, but you still can't write a hypothesis | Keep exploring, and keep an eye on the time limit |
| Several approaches have taught you nothing new | Move to the next idea; if you have tried everything on the list, go back to [Generating candidate problems](02_generate-problems.md) |
| You find the idea's premise doesn't hold (for example, the model was never accurate on these benchmarks to begin with, so there is nothing overestimated) | That is a result too: put the idea back on the list with the reason, or rewrite the finding as a new idea |

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Reading and thinking endlessly, never getting started | The ability to judge whether a problem is good depends on doing the work[^olah2021taste-e9] |
| Starting with a big, rigorous experiment | You see results only weeks later; exploration is about seeing early signs fast[^nanda2025mindsets-e11] |
| Thinking you should already have a clear hypothesis when you are still exploring | You get stuck and don't know what to do next[^nanda2025process-e2] |
| Not keeping notes while exploring | A few days later you can't say what you saw `[Our analysis]` |
| Constantly switching ideas and never trying any properly | You learn nothing[^nanda2025mindsets-e1] |
| Treating what you saw while exploring as a conclusion | Exploration has no criteria set in advance, so its results are only leads `[Our analysis]` |

## What you should have at the end

- Exploration notes and a highlights file (Section 3)
- An outcome for every idea you explored: the specific hypothesis you wrote, or the reason you dropped it (Section 4)
- At least one specific hypothesis you can write down, plus what evidence you think would decide it

## Checklist before moving on

Move on once all of these hold:

- [ ] Each of the ideas you most want to pursue has had at least one small, fast try
- [ ] Every try is recorded in your exploration notes
- [ ] At least one idea has been turned into a specific hypothesis, and you can say what evidence would decide it
- [ ] Ideas you dropped have a reason written down and are back on the idea list
- [ ] You can tell which things are just observations from exploring and which still need testing

## When to go back

| If this happens | Go back to |
|---|---|
| You can't think of any small try you could actually do | The idea is too vague; go back to [Generating candidate problems](02_generate-problems.md) and make it concrete |
| You have explored every idea on the list and none taught you anything new | Go back to [Generating candidate problems](02_generate-problems.md) and look for ideas from a different source |
| You can't make sense of what the explorations show (for example, you can't tell whether the model's answers are right) | You don't know the area well enough yet; go back to [Entering a field and exploring the literature](01_enter-a-field.md) |

## Next

Take your exploration notes and the hypotheses you wrote into [Judging and screening ideas](04_judge-and-screen.md): put the ideas you explored alongside the ones you didn't, quickly screen them down to two to four, and carry those into [Converging on a project](05_converge.md).

[^carlini2026best-e13]: Carlini 2026, Pick your ideas for impact. [Evidence](../../sources/notes/carlini2026best.md#e13)
[^nanda2025mindsets-e1]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e1)
[^nanda2025mindsets-e9]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e9)
[^nanda2025mindsets-e11]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e11)
[^nanda2025mindsets-e12]: Nanda 2025b, Moving Fast. [Evidence](../../sources/notes/nanda2025mindsets.md#e12)
[^nanda2025process-e1]: Nanda 2025a, Exploration (Stage 2). [Evidence](../../sources/notes/nanda2025process.md#e1)
[^nanda2025process-e2]: Nanda 2025a, Exploration (Stage 2). [Evidence](../../sources/notes/nanda2025process.md#e2)
[^nanda2025process-e3]: Nanda 2025a, Exploration (Stage 2). [Evidence](../../sources/notes/nanda2025process.md#e3)
[^nanda2025process-e4]: Nanda 2025a, Exploration (Stage 2). [Evidence](../../sources/notes/nanda2025process.md#e4)
[^nanda2025process-e5]: Nanda 2025a, Understanding (Stage 3). [Evidence](../../sources/notes/nanda2025process.md#e5)
[^nanda2025process-e6]: Nanda 2025a, Distillation (Stage 4). [Evidence](../../sources/notes/nanda2025process.md#e6)
[^olah2021taste-e9]: Olah 2021, Failure mode 2. [Evidence](../../sources/notes/olah2021taste.md#e9)
[^perez2024tips-e1]: Perez 2024, General Mindset Tips. [Evidence](../../sources/notes/perez2024tips.md#e1)
[^perez2024tips-e2]: Perez 2024, General Mindset Tips. [Evidence](../../sources/notes/perez2024tips.md#e2)
[^perez2024tips-e3]: Perez 2024, Three modes of research. [Evidence](../../sources/notes/perez2024tips.md#e3)
[^perez2024tips-e4]: Perez 2024, Three modes of research (Writing phase). [Evidence](../../sources/notes/perez2024tips.md#e4)
[^schulman2020opinionated-e16]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e16)
[^steinhardt2018stochastic-e4]: Steinhardt 2018, A Better Strategy: Sorting by Information Rate. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e4)
[^steinhardt2018stochastic-e6]: Steinhardt 2018, A further improvement. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e6)
[^steinhardt2018stochastic-e8]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e8)
