# Judging and screening ideas

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Ask four quick questions of every entry on your list.** Can you state it clearly? Can you see a way in? Is it beaten by another entry? Does it suit you? Spend only a few minutes on each; this is not the place to check for prior work or work out the evidence ([Section 1](#1-quick-first-screen-ask-four-things-of-each-entry)).
> 2. **Check whether it suits you.** Do you keep coming back to it? Do you have an edge? At a glance, are the resources enough? Can your advisor help ([Section 2](#2-does-it-suit-you-interest-ability-resources-advisors-direction))?
> 3. **If you aren't sure, ask your advisor to score them.** Rate each entry from 1 to 10, then discuss in depth the ones where your scores differ most ([Section 3](#3-if-you-arent-sure-ask-your-advisor-to-score-them)).
> 4. **Keep two to four, and write down why you crossed out the rest.** One line is enough, such as "no way in", "beaten by entry X", or "not enough resources" ([Section 3](#3-if-you-arent-sure-ask-your-advisor-to-score-them)).
>
> **Done these? Move on:** every entry has been through the four questions, you have kept two to four, you can say why you kept them and why you dropped the others, and you have gone over the results with your advisor or at least one person who knows the area. Next: [Converging on a project](05_converge.md).

## Where you are

You have a list of ideas (see [Generating candidate problems](02_generate-problems.md)), and you have already tried a few of them hands-on (see [Exploring hands-on](03_explore.md)). Take the "benchmark leakage" idea: you found several evaluation contracts that have appeared publicly and wrote down a first hypothesis. For the "too many false positives" idea, you ran the model on a few contracts with no vulnerabilities, and it did report quite a few "vulnerabilities". A few other ideas you haven't had time to try.

There are about ten entries on your list, and you can't go deep on all of them. Which ones should you pick?

## What this stage is for

Run a **cheap, fast screen** over the **many** ideas on your list and keep two to four to take into the next chapter.

It does a different job from the next chapter, [Converging on a project](05_converge.md) `[Our analysis]`:

| | Judging and screening (this chapter) | Converging on a project (next chapter) |
|---|---|---|
| What you look at | The many ideas on your list | The two to four you kept, narrowed down to one in the end |
| Time per idea | A few minutes | A few days to a few weeks |
| What you ask | Can you state it clearly? Can you see a way in? Is it beaten by another entry? Does it suit you? | Is it worth doing? Has someone already done it? What will convince people? Can you actually pull it off? |
| Output | The candidates you kept, and why you dropped the rest | A one-page project summary, plus the exit check |

---

## 1. Quick first screen: ask four things of each entry

This step takes only an hour or two. The aim isn't to pick your final topic; it's to cross out the ideas that clearly aren't worth deeper thought `[Our analysis]`.

**For each idea, quickly ask four things** `[Our analysis]`:

1. **Can you say in one sentence what is wrong?** If not, leave it on the list to keep thinking about, but keep it out of this round.
2. **Can you see a way in?** Hamming put it this way: what makes a problem important isn't how big the result would be, but that you have a reasonable attack on it[^hamming1986you-e2]. If you can't even think of a first step, set it aside.
3. **Is it beaten across the board by another entry?** If A is better than B on both feasibility and value, you can cross out B[^alon2009choose-e6]. A rough look is enough; you don't need to score them.
4. **Does it suit you?** Look at interest, ability, resources, and your advisor's direction; see Section 2.

For ideas you have explored hands-on, you can answer these four questions on firmer ground. For ones you haven't had time to try, a rough call based on what you know now is fine; if you can't decide on one that looks promising, go back to [Exploring hands-on](03_explore.md) and try it before you screen `[Our analysis]`.

**What this step doesn't do.** It doesn't settle "has anyone done this already?", doesn't work out "what evidence would I need?", and doesn't do a detailed count of data and compute. Those are what [Converging on a project](05_converge.md) does carefully for the two to four candidates. In the first screen, spend only a few minutes on each entry `[Our analysis]`.

**Write it down:** For every idea on your list, write a short answer to each of the four questions.

## 2. Does it suit you: interest, ability, resources, advisor's direction

An idea that is a good topic for someone else isn't necessarily a good one for you. Ask four things:

- **Interest: do you keep coming back to it?** Ask yourself: if I were the only person on earth, which of these would I work on[^alon2009choose-e12]? An idea that keeps coming back to your mind over months is a good sign of real interest[^alon2009choose-e13]. Learn to tell two voices apart: the loud voice of the people around you, at conferences and in your department, saying "this is important", and the faint voice inside you saying "this is interesting to me"[^alon2009choose-e11]. Don't pile onto the hottest problems[^huang2023decide-e1]. Forcing yourself to work on a topic that doesn't excite you, even if you intellectually think it's more important, makes you a lot less effective[^olah2021taste-e3].
- **Ability: do you have an edge here?** How long a problem takes depends on the skills of the people doing it and on what their lab can do[^alon2009choose-e2]. Know your unfair advantages over others[^huang2023decide-e1]. If you are very good at a less "important" problem, you may contribute more than by working on one you're not good at[^carlini2026best-e11]. When you are just starting out in research, an easier problem is better, because you get positive feedback sooner[^alon2009choose-e7].
- **Resources: are data, compute, and time roughly enough?** Only a rough look here: cross out anything you can see at a glance you can't do, such as training a large language model from scratch when you have one GPU. Save the detailed feasibility check for [Converging on a project](05_converge.md#5-can-you-actually-do-it) `[Our analysis]`.
- **Advisor's direction: can your advisor help you?** Relying heavily on an advisor or an established research direction early in your career is normal[^nanda2025taste-e9]. There is no shame in working on an idea an experienced person suggested[^schulman2020opinionated-e4]. But your advisor's view is input, not a verdict: advisors usually have good research instincts, but you know far more about your own specific problem than they do[^nanda2025mindsets-e15]. If an idea is far from your advisor's direction, first talk it through and find out whether they are willing to support it `[Our analysis]`.

An example from "large language models and smart contract security" `[Our analysis]`:

| Idea | Result of the four questions | Keep or drop |
|---|---|---|
| Data leakage inflates the reported results of current large-language-model vulnerability detectors | Clear; the way in is obvious (trace where the evaluation contracts came from, compare accuracy with and without the leaked ones); the most exciting one during exploration; only needs API calls; your advisor has done evaluation work | Keep |
| Too many false positives, so developers don't want to use these tools | Clear; you can count false positives and interview developers; interesting, but you have never done interviews and would have to learn | Keep |
| Does switching to a different prompt change the detection rate much? | Clear; but compared with the first idea it is less valuable and about as hard, so it's beaten | Drop |
| Train a large language model for contracts from scratch | Nowhere near enough resources | Drop |
| "Large language models will change contract security" | Can't say what exactly is wrong | Leave on the list and keep thinking |

**Write it down:** For each idea that passes the first three questions, write one line each on interest, ability, resources, and your advisor's direction.

## 3. If you aren't sure, ask your advisor to score them

Give your advisor the list and ask them to rate each entry from 1 to 10, then discuss in depth the ones where you disagree most[^olah2021taste-e4]. This is screening, and it is also practice in judging which problems are good.

This ability is often called "research taste": roughly, the ability to choose good problems to work on[^olah2021taste-e1]. It comes mainly from practicing research[^carlini2026best-e5]. For how to build it over the long term, see [Build your research taste on purpose](../08_throughout/mindset_and_growth.md#1-cultivate-research-taste-on-purpose).

**Write it down:** On your list of ideas, mark the two to four entries you kept this round, and for each one you crossed out write one sentence on why ("no way in", "beaten by entry X", "not enough resources", and so on).

---

## Judgment calls

**How many should you keep?** Here's one way to decide `[Our analysis]`:

| Situation | What to do |
|---|---|
| Two to four left | Move on to [Converging on a project](05_converge.md) |
| Five or more left | Do another round of "is it beaten by another entry?", or ask your advisor to score them |
| None left | Your list is too narrow or too vague; go back to [Generating candidate problems](02_generate-problems.md) for another round |
| The most interesting one doesn't fit your advisor's direction | Talk to your advisor first and explain what your exploration turned up; don't quietly bend it into something you're no longer excited about |

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Thinking every entry through in depth during the first screen | Time goes into ideas that will be crossed out anyway; save the in-depth checks for the next chapter `[Our analysis]` |
| Judging only whether the idea is good, not whether it suits you | How long a problem takes depends on your skills and resources[^alon2009choose-e2] |
| Chasing the hottest research area | Don't pile onto the hottest problems[^huang2023decide-e1]; outside the hottest area it is actually much easier to stand out[^carlini2026best-e12] |
| Picking only to your advisor's taste | You know more about your own specific problem and can make your own call[^nanda2025mindsets-e15] |
| Crossing out ideas without writing down why | Later you can't tell why you set them aside, and you can't learn from it `[Our analysis]` |

## What you should have at the end

- The first-screen result: the two to four you kept, and why each of the others was dropped (Sections 1 and 3)
- For each one you kept, a one-line judgment of whether it suits you (Section 2)
- If your advisor scored the list, the scores and the outcome of discussing the entries where you disagreed most

## Checklist before moving on

You are ready for the next step when:

- [ ] Every idea on your list has been through the four questions
- [ ] You have kept two to four, and can say why you kept them and why you dropped the others
- [ ] For each one you kept, you have thought about interest, ability, resources, and your advisor's direction
- [ ] You have gone over the screening results with your advisor or at least one person who knows the area

## When to go back

| If this happens | Go back to |
|---|---|
| Nothing survives the screen | [Generating candidate problems](02_generate-problems.md), and look again using a different source |
| You can't decide on several entries and can't answer the four questions | [Exploring hands-on](03_explore.md): run a few small tries on them first |
| You have lost interest in the research area itself | Talk to your advisor and consider switching areas; forcing yourself to work on a topic you aren't excited about makes you far less productive[^olah2021taste-e3] |

## Next

Take the two to four candidates you kept into [Converging on a project](05_converge.md): write each one as a single sentence stating what you want to show, check in depth whether it's worth doing, whether someone has already done it, what will convince people, and whether you can pull it off, then narrow down to one and run the exit check.

Put the rejected candidates back on your list of ideas, with the reason written next to each.

[^alon2009choose-e2]: Alon 2009, p. 1. [Evidence](../../sources/notes/alon2009choose.md#e2)
[^alon2009choose-e6]: Alon 2009, The Two Dimensions of Problem Choice. [Evidence](../../sources/notes/alon2009choose.md#e6)
[^alon2009choose-e7]: Alon 2009, p. 1. [Evidence](../../sources/notes/alon2009choose.md#e7)
[^alon2009choose-e11]: Alon 2009, The Subjectivity of the Interest Axis. [Evidence](../../sources/notes/alon2009choose.md#e11)
[^alon2009choose-e12]: Alon 2009, The Subjectivity of the Interest Axis. [Evidence](../../sources/notes/alon2009choose.md#e12)
[^alon2009choose-e13]: Alon 2009, The Subjectivity of the Interest Axis. [Evidence](../../sources/notes/alon2009choose.md#e13)
[^carlini2026best-e5]: Carlini 2026, Have good taste for problems. [Evidence](../../sources/notes/carlini2026best.md#e5)
[^carlini2026best-e11]: Carlini 2026, Get lucky: you're well suited to solve important problems. [Evidence](../../sources/notes/carlini2026best.md#e11)
[^carlini2026best-e12]: Carlini 2026, Get lucky: you're well suited to solve important problems. [Evidence](../../sources/notes/carlini2026best.md#e12)
[^hamming1986you-e2]: Hamming 1986, "important problems" paragraph. [Evidence](../../sources/notes/hamming1986you.md#e2)
[^huang2023decide-e1]: Huang 2023, Find your position. [Evidence](../../sources/notes/huang2023decide.md#e1)
[^nanda2025mindsets-e15]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e15)
[^nanda2025taste-e9]: Nanda 2025, Conclusion. [Evidence](../../sources/notes/nanda2025taste.md#e9)
[^olah2021taste-e1]: Olah 2021, opening section. [Evidence](../../sources/notes/olah2021taste.md#e1)
[^olah2021taste-e3]: Olah 2021, opening section. [Evidence](../../sources/notes/olah2021taste.md#e3)
[^olah2021taste-e4]: Olah 2021, Exercise 1. [Evidence](../../sources/notes/olah2021taste.md#e4)
[^schulman2020opinionated-e4]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e4)
