# Converging on a project

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

## Where you are

You know the basics of a research area, you have read a set of core papers, and you have a few candidate problems. The area may have come from your advisor, say "using large language models for smart contract security", or the idea may have come to you while reading.

What you can't say yet is what exactly the project will do, how far it has to go before it is done, and why it is worth doing.

## What this stage is for

Turn a vague idea into a **project that holds up**. Concretely, that means being able to answer six questions:

1. What one sentence do I ultimately want to prove?
2. Is it worth doing?
3. Has someone already done it? How is my work different from the closest existing work?
4. What will make people believe it?
5. Can I actually do it?
6. Can I put all of this on one page and defend it when my advisor pushes back?

## How to use this chapter

You **don't** walk through these six questions once, in order, and finish. They pull on each other:

- You think of a good claim → the literature shows someone did it last year → back to step 1 to find a different angle.
- The claim is clear → the data you need turns out to be unavailable → back to step 1 to make the claim smaller.
- You have the data → it can only support a very weak claim → back to step 2 to decide again whether it is worth doing.

So expect several rounds back and forth between these steps. At the end of each round, write the result into a one-page project summary (Section 6). This stage is done when you can write the summary, can still revise it as things change, and your advisor can't find any major flaw in it.

How many rounds does it usually take? There is no standard answer. Three to five rounds over a few weeks is normal `[Our analysis]`. If you are still going in circles after a month or two, see "When to go back" at the end of this chapter.

---

## 1. Write down the sentence you want to prove

**Don't start with "which method should I use?" Start with: if this project succeeds, what is the single most important conclusion that goes under the paper's title?**

Many people's first attempt is "We study the application of large language models to smart contract security." That sentence says what you **did**, not what you **found**, and readers finish it without knowing what they are supposed to believe. When you describe what your work contributes, use words that name a result, not words like "studied" or "explored" that only name an activity[^shaw2003writing-e18].

Written as a claim, it could be:

- "Much of the high accuracy reported for large-language-model vulnerability detection comes from data leakage in the benchmarks."
- "Giving a large language model hints about vulnerability patterns clearly raises its detection rate for reentrancy vulnerabilities."
- "On real contracts, our new method finds 30% more vulnerabilities than existing tools, with fewer false positives."

All three share a topic, but each requires completely different work. The first has to show the leakage exists and how the conclusions change once it is removed; the second needs a controlled experiment; the third needs you to build a new method and compare it with existing tools. **A different claim means a different study.** The three belong to three different research strategies, Measurement, Causal explanation, and Building and improving; see [Key concepts](../00_start-here/key-concepts.md#research-strategy).

**Next, check how strong the sentence is.** Break the claim into clauses and decide which kind each one is[^shaw2003writing-e16]:

| Kind of statement | Example | Evidence it needs |
|---|---|---|
| Global: "always", "all" | "Works on all contracts" | Often needs proof; experiments can rarely support it |
| Qualified: "under this condition, improves by this much" | "Raises the detection rate on Solidity contracts by 20%" | An evaluation under clearly stated conditions |
| Existential: "there exists", "it can be done" | "Large language models can find vulnerabilities that static analysis tools miss" | Sometimes a few real examples are enough |

The most common beginner mistake is claiming too much. The stronger the claim, the more evidence it needs. This step often leads you to rewrite the claim more precisely, and the earlier you do that, the easier it is to plan the rest of the research around a claim you can actually support[^shaw2003writing-e17].

**Write it down:** Two or three candidate claims, one sentence each. Don't write "studied" or "explored". If you can't write one yet, that's fine: write the closest sentence you can, and the next sections will help you revise it.

## 2. Is it worth doing?

Once you have candidate claims, ask yourself: **even if this sentence is proved, who cares?**

Some concrete ways to ask it:

- **In the best case, how big is the payoff?** Does a metric go up a little, or does it change the way people do this[^schulman2020opinionated-e10]?
- **If another group published this paper, would you be excited to read it[^olah2021taste-e11]?** This is a handy test: if you wouldn't want to read the paper yourself, reviewers probably won't either.
- **Will it still be worth it in six months, a year, four years[^eisnerproblems-e7]?** Large-language-model research moves fast; today's hot topic may interest nobody a year from now.
- **Is there a feasible way to attack it?** However important a problem is, if you have no idea where to start, it isn't a good problem[^hamming1986you-e2].

Try this on the examples from the previous section:

- "Existing results are inflated by data leakage": if true, the whole area has to re-examine its conclusions. The impact is broad.
- "The new method finds 30% more vulnerabilities": valuable, but only if the existing tools' shortcoming is really what blocks practical use. If people avoid existing tools because they raise too many false positives, then finding more vulnerabilities isn't the point; cutting false positives is.

The second example shows that judging importance often ends up **rewriting your claim**. That is exactly what converging means.

**Write it down:** For each candidate claim, write one or two sentences on "if this is true, who will change what they do or believe because of it". Set aside any claim for which you can't write this.

## 3. Has someone already done it?

**Do this now, not after the project is finished.** The worst case is finishing the whole project and then discovering that someone had already published the same work[^noble2023ten-e5].

**How to check:**

1. Search with the key words in your claim and find the three to five closest papers. Follow their references backward, then look at who has cited them. For how to search the literature, see [Entering a field and exploring the literature](01_enter-a-field.md).
2. **Ask people who know the area.** Literature searches always miss things; your advisor, senior students, or people working in the same area can often tell you in one sentence that "so-and-so's group did this last year"[^eisnerproblems-e4][^eisnerproblems-e9].
3. Computer science moves quickly, so besides published papers, also check preprint servers and the accepted-paper lists of recent conferences `[Our analysis]`.

**Then make a comparison table.** Don't just write "there is a lot of related work". Say concretely what each piece of work achieved, what its limitations are, and where you differ. Shaw gives a good example: method A achieves 60% coverage; method B achieves 80% but only works without pointers; our method achieves 90% while relaxing that restriction[^shaw2003writing-e3].

| Closest work | What it achieved | Its limitations | How mine differs |
|---|---|---|---|
| Work A | | | |
| Work B | | | |
| Work C | | | |

**If someone has already done it**, don't give up right away `[Our analysis]`:

- **Exactly the same**: change topics and go back to [Finding candidate problems](02_generate-problems.md).
- **They did only part of it**: for example, they validated on only one dataset or considered only one kind of vulnerability. Your claim can target the part they didn't cover.
- **Their approach has a flaw**: for example, their evaluation has leakage or their baselines are too weak. Then "pointing out and fixing this flaw" can itself be your claim.

Reframing the problem slightly often turns up a better way in[^hamming1986you-e13][^eisnerproblems-e10].

**Write it down:** Fill in the comparison table above. If you can't write anything concrete in the "How mine differs" column, the claim isn't new enough yet; go back to Section 1 and revise it.

## 4. What will make people believe it?

You have a claim. Now think: **what would a skeptical reviewer need to see before believing this sentence?** Why should readers believe your results? What standard should your claim be judged by? What concrete evidence shows you have achieved it[^shaw2003writing-e6]?

**The claim decides the evidence, not the other way round.** Don't start from "what experiments could I run" and then look for something they might show.

For the claim that "evaluation results are inflated by data leakage", a reviewer would press you on at least these questions:

| What the reviewer will ask | Evidence you need |
|---|---|
| Does the leakage really exist? | How many contracts in the benchmark appear in the models' training data, and how you established that |
| Did the leakage really affect the results? | The accuracy of the same set of tools before and after removing leaked samples |
| Is it just one or two tools that are affected? | Results across several models and several tools |
| Is your way of judging leakage reliable? | The accuracy of the method you use to decide "leaked or not" |

**A very useful trick: draw the empty results table first.** Before running any experiment, you can already sketch the results table that will go in the paper: what the rows are, what the columns are, and what number goes in each cell[^eisnerfirst-e5]. Draw it honestly and you will often find that proving your claim takes more work than you expected[^eisnerfirst-e6]. The sooner you find that out, the better.

If you can't think of any evidence that would support a claim, either rewrite it or drop it `[Our analysis]`.

How to design the experiments and how to choose baselines and benchmarks belong to the next stage; see [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md). At this step you only need to be clear about **what evidence you need**, not every detail of **how you will get it**.

**Write it down:** For your central claim, list three to five questions a reviewer would press you on, and draw at least one empty results table.

## 5. Can you actually do it?

By now you may have an attractive claim and a clear list of the evidence it needs. The last question is: **with what you have now, can you get that evidence?**

Common sticking points in computer science `[Our analysis]`:

| What to check | Examples |
|---|---|
| Data | Is there an existing vulnerability dataset? How good are its labels? If you have to label data yourself, how much labor will it take? |
| Compute and APIs | How many calls to commercial large-language-model APIs will you need? Can you afford them? How many GPUs does running a model locally take? |
| Baselines | Can you get the existing tools you want to compare against running? Are they open source? |
| Evaluation | Is there a widely accepted benchmark? If you have to build one, building the benchmark may be a project in itself |
| Skills | Can you write smart contracts and do you know the relevant analysis tools? How long would it take to learn? |
| Time | How long until the submission deadline you are aiming for? |
| Ethics | If you may find vulnerabilities in contracts that are actually deployed, you have to notify whoever is responsible privately before going public; see the [computer science field overview](../07_fields/computer-science/README.md#ethics-issues-specific-to-this-field) |

**Discount your feasibility estimates.** Problems that look easy on paper are often hard in practice; problems that look hard on paper are nearly impossible in practice[^alon2009choose-e3]. How long a project takes depends on your skills and resources, not someone else's[^alon2009choose-e2]. When you are just starting out in research, it is better to pick an easier problem, so you get positive feedback sooner[^alon2009choose-e7].

**Find the cheapest way to test the part you are least sure of.** Not every idea will work: design a small experiment to check your core hypothesis as soon as possible, and if it is going to fail, fail fast[^huang2023decide-e5]. For example:

- Worried that your leakage-detection method is unreliable: check 50 samples by hand first and see whether its judgments are right.
- Worried that the new method won't work: try the prompts by hand on 20 contracts first and see whether the large language model spots the problems.
- The problem is too big to know where to start: think about a simplified version first, such as looking at only one kind of vulnerability; this often suggests how to tackle the original problem[^steinhardt2018stochastic-e8].

A small experiment like this may take only a few days and can save you months.

**Write it down:** List everything your project needs and mark each item "have it / can get it / not sure". For the most uncertain item, write down what small experiment you will use to settle it within a week or two.

## 6. Write a one-page project summary and keep revising it

Put the results of the first five steps on one page. This page is what you and your advisor discuss, and it is also your own test of whether you have thought things through.

> **The question I want to answer is:** ____
>
> **The central claim I hope to prove is:** ____ (one sentence, using words that name a result)
>
> **It matters because:** ____ (who will change what because of it)
>
> **The closest existing work is:** ____; **mine differs in that:** ____
>
> **Which research strategy it belongs to:** ____
>
> **To make people believe it, I need this evidence:** ____
>
> **I can get this evidence because:** ____ (data, compute, baselines, skills, time)
>
> **The part I'm least sure of is:** ____; **I plan to test it first by:** ____

**Any field you can't fill in is exactly what you most need to think through now.** Don't force an answer.

**When it's written, show it to your advisor or to fellow students who know the area.** Ask them: does this claim hold up? Is it an important problem that hasn't been solved yet[^noble2023ten-e10]? If they think the basic idea would make reviewers skeptical or bored, you want to know that before you spend the time[^eisnerfirst-e3]. If you can't decide between several candidate claims, ask your advisor to score each one and discuss in depth the ones where your scores differ most[^olah2021taste-e4].

**Update this same page after every round of revision.** Don't start a new document. Keep the old versions; a few months later, looking back, you will see clearly how your thinking changed.

---

## Judgment calls

**Narrow it, change the angle, or give up?** While converging you will often hit obstacles. Here is one way to decide `[Our analysis]`:

| What happens | What you usually do |
|---|---|
| The claim is too big and needs too much evidence | Narrow it: limit the conditions, limit what it applies to, change "always" to "under this condition" |
| You can't get the core data | Change the angle: see whether other evidence could support a similar claim, or switch to a different research strategy |
| Someone has already done most of it | Find the part they didn't cover, or a flaw in their approach |
| You can't think of anyone who would care | Go back and rethink the problem itself; don't invent an application to justify it |
| After several rounds, no candidate holds up | Go back to the problem-finding stage and widen your set of candidates |

**When have you thought it through?** Not when you "can't think of any more questions", but when you can fill in every field of the one-page summary, you can answer your advisor's follow-up questions, and the part you are least sure of has already been tested with a small experiment.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Describing your goal as "we study X" or "we explore X" | It names an activity, not a result, so readers don't know what you are trying to prove[^shaw2003writing-e18] |
| Deciding on experiments first, then working out what they show | Once the experiments are done, they often turn out to be useless for the paper; the claim should decide the evidence |
| Claiming too much | The evidence needed far exceeds what you can get[^shaw2003writing-e16] |
| Checking related work only after the project is done | You may find someone has already published it[^noble2023ten-e5] |
| Searching the literature but never asking people | You miss work that is unpublished or only just published[^eisnerproblems-e9] |
| Estimating feasibility only for the ideal case | What looks easy on paper is often hard in practice[^alon2009choose-e3] |
| Never revising the one-page summary after writing it | Your ideas change; if the summary doesn't, it stops being useful `[Our analysis]` |
| Diving in the moment an idea seems feasible | You may spend a long time chasing an idea you haven't thought through[^noble2023ten-e2] |

## What you should have at the end

- A one-page project summary (Section 6) and all its earlier versions
- A comparison table of the closest work (Section 3)
- At least one empty results table (Section 4)
- A small experiment you have already run, and its result (Section 5)

## Checklist before moving on

You can move on when all of these hold:

- [ ] You can state the central claim in one sentence, using words that name a result
- [ ] You can say who will change what if it turns out to be true
- [ ] You have searched the literature and asked people who know the area, and you can say concretely how you differ from the three closest pieces of work
- [ ] You know what reviewers will press you on, and you have drawn the empty results table
- [ ] You have confirmed you can get the data, compute, and baselines you need, or you have a clear plan for getting them
- [ ] You have tested the part you are least sure of with a small experiment, and the result did not rule out the whole idea
- [ ] Your advisor has read the one-page summary and raised no fundamental objection

## When to go back

| If this happens | Go back to |
|---|---|
| Every candidate claim turns out to have been done already | [Finding candidate problems](02_generate-problems.md) |
| You know too little about the area to judge importance and novelty | [Entering a field and exploring the literature](01_enter-a-field.md), and read another batch of papers |
| After a month or two you are still going in circles, each round overturning the last | Pick one together with your advisor and get started; being stuck deciding is itself a signal `[Our analysis]` |
| The small experiment rules out your core hypothesis | Section 1 of this chapter; choose a different candidate claim |

## Next

Once the one-page summary is settled, the next step is to turn it into a plan you can carry out: set milestones, schedule the work, and decide what counts as done. See [Writing a research plan](../02_do-the-project/03_research-plan.md).

[^shaw2003writing-e3]: Shaw 2003, §3.3. [Evidence](../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e6]: Shaw 2003, §1. [Evidence](../../sources/notes/shaw2003writing.md#e6)
[^shaw2003writing-e16]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e17]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e17)
[^shaw2003writing-e18]: Shaw 2003, §3.3. [Evidence](../../sources/notes/shaw2003writing.md#e18)
[^schulman2020opinionated-e10]: Schulman 2020, Choosing Problems. [Evidence](../../sources/notes/schulman2020opinionated.md#e10)
[^olah2021taste-e4]: Olah 2021, Exercise 1. [Evidence](../../sources/notes/olah2021taste.md#e4)
[^olah2021taste-e11]: Olah 2021, Suggestions from other people. [Evidence](../../sources/notes/olah2021taste.md#e11)
[^eisnerproblems-e4]: Eisner, How to Find Research Problems. [Evidence](../../sources/notes/eisnerproblems.md#e4)
[^eisnerproblems-e7]: Eisner, How to Find Research Problems, Keep in mind. [Evidence](../../sources/notes/eisnerproblems.md#e7)
[^eisnerproblems-e9]: Eisner, How to Find Research Problems, Finally. [Evidence](../../sources/notes/eisnerproblems.md#e9)
[^eisnerproblems-e10]: Eisner, How to Find Research Problems. [Evidence](../../sources/notes/eisnerproblems.md#e10)
[^hamming1986you-e2]: Hamming 1986. [Evidence](../../sources/notes/hamming1986you.md#e2)
[^hamming1986you-e13]: Hamming 1986. [Evidence](../../sources/notes/hamming1986you.md#e13)
[^noble2023ten-e2]: Noble 2023, Rule 1. [Evidence](../../sources/notes/noble2023ten.md#e2)
[^noble2023ten-e5]: Noble 2023, Rule 4. [Evidence](../../sources/notes/noble2023ten.md#e5)
[^noble2023ten-e10]: Noble 2023, Rule 10. [Evidence](../../sources/notes/noble2023ten.md#e10)
[^eisnerfirst-e3]: Eisner 2010, Write the Paper First, Is it a good topic? [Evidence](../../sources/notes/eisnerfirst.md#e3)
[^eisnerfirst-e5]: Eisner 2010, Write the Paper First, What needs to be done? [Evidence](../../sources/notes/eisnerfirst.md#e5)
[^eisnerfirst-e6]: Eisner 2010, Write the Paper First, What needs to be done? [Evidence](../../sources/notes/eisnerfirst.md#e6)
[^alon2009choose-e2]: Alon 2009, p. 1. [Evidence](../../sources/notes/alon2009choose.md#e2)
[^alon2009choose-e3]: Alon 2009. [Evidence](../../sources/notes/alon2009choose.md#e3)
[^alon2009choose-e7]: Alon 2009, p. 1. [Evidence](../../sources/notes/alon2009choose.md#e7)
[^huang2023decide-e5]: Huang 2023, item 6. [Evidence](../../sources/notes/huang2023decide.md#e5)
[^steinhardt2018stochastic-e8]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e8)
