# Finding candidate problems

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

## Where you are

You have entered a research area and read a batch of core papers. You roughly know what the field is doing, who is doing it, and with what approaches. Say your advisor gave you the research area "using large language models for smart contract security", and you have read twenty or thirty related papers.

But you still don't know what you are going to work on. You may have one or two vague notions, or none at all. What worries you is: haven't all the good problems been taken already? How am I supposed to "come up with" a topic?

## What this stage is for

From a **research area**, find a **batch** of candidate **problems**, then do a quick first screen and pick two to four worth thinking about seriously to take into the next chapter.

A "problem" here means something in the field that is wrong, not good enough, or not yet known; see [Key concepts](../00_start-here/key-concepts.md#problem). It doesn't yet need to be a research question you can answer directly, let alone a finished claim. That is the job of [Converging on a project](05_converge.md).

This chapter asks you to do three things:

1. **Find** problems using a few concrete methods, instead of waiting for inspiration;
2. **Write down** everything you find, building up a list of ideas;
3. **Screen** the list roughly once and keep a few for the next step.

**Why a batch and not just one?** A common mistake in choosing a problem is to grab the first one that comes to mind. A project usually takes several years, and a hasty choice leads to a lot of frustration[^alon2009choose-e8]. With only one idea, you have nothing to compare it with, so you can't judge whether it is any good.

---

## 1. Set aside time for finding problems: read, think, and try at the same time

**Here's what to do:** mark out a definite period for finding problems, and during it do three things in parallel: read the literature, write down ideas, and try small hands-on experiments. When the time is up, move on to the first screen.

**Why set aside dedicated time.** Good problems don't show up while you are reading your first paper. One piece of advice is that a new student or postdoc should not commit to a project in their first 3 months, and should use that time to read, discuss, and plan[^alon2009choose-e9]. Rushing into an idea as soon as it looks feasible also tends to go wrong; if you spend more time with it, you can often come up with a deeper version[^olah2021taste-e12].

**Why you can't just read, though.** Trying to pick the perfect problem before you have done any hands-on work is a trap: the ability to judge whether a problem is good depends on actually doing the work[^olah2021taste-e9]. The last chapter already said not to let background reading drag on and to alternate reading with thinking; see [Entering a field and exploring the literature](01_enter-a-field.md#judgment-calls).

> **Where sources disagree: how long should finding a problem take?**
> - **Take more time:** an extra week spent choosing a problem can save months or even years later[^alon2009choose-e8]. But the person who gives this advice also admits that not everyone is free to choose their own problem or has the time for a long search[^alon2009choose-e10].
> - **Don't drag it out:** start thinking for yourself early and alternate with reading[^eisnerproblems-e9]; once you have searched for ideas for a while, an extra hour of thinking is worth less than just going and doing something[^carlini2026best-e13].
>
> In practice `[Our analysis]`: give yourself a set period (a few weeks to three months, depending on your stage and what your advisor expects), and during it read, write, and try **at the same time**. When the time is up, move to the first screen in Section 9; if you can't narrow it down, take your list to your advisor and decide together.

**Two starting points.** There are roughly two places to start looking for problems[^schulman2020opinionated-e6][^schulman2020opinionated-e8]:

- **Idea-driven**: you read "how others do X", think of a way to do it better, and then test it. The downside is that it is easy to get scooped, because everyone reads the same literature and has similar ideas[^schulman2020opinionated-e7].
- **Goal-driven**: you set a concrete goal first, such as "let developers reliably find reentrancy vulnerabilities before they deploy a contract", and then solve the problems that stand in the way. The goal gives you a distinctive perspective and leads you to ask questions others haven't asked[^schulman2020opinionated-e8].

The methods in the sections below work from either starting point. The difference is that, starting from a goal, you will ask more often "what's still missing between here and the goal", not just "how else could this paper be improved" `[Our analysis]`.

**Write it down:** Write down the period you have set for finding problems (from which day to which day), and whether you plan to work idea-driven, goal-driven, or both. If goal-driven, state the goal in one sentence.

## 2. Look in the gaps and limitations of papers

You are already reading papers, and the last chapter had you start a "problem log"; see [Entering a field and exploring the literature](01_enter-a-field.md#6-take-notes-one-per-paper-plus-a-problem-log). This section goes back to that log and those papers specifically to dig out candidate problems.

**When you look back at papers, ask two more things:**

- **Where did the authors simplify, or make an arbitrary choice?** Those are your chances to do it differently[^eisnerproblems-e2]. For example, a paper considers only one type of vulnerability, uses only one model, or tests on only one dataset, without saying why.
- **Can you come up with an example that would embarrass the authors?** Think of examples that illustrate the authors' idea, and examples that would make their claims fall apart[^eisnerread-e3].

Whether the experiments are fair, whether the conclusions generalize, and where else the paper's good ideas might apply are already covered under [Read with questions in mind](01_enter-a-field.md#5-read-with-questions-in-mind) in the last chapter, so we won't repeat them here.

**Problems that come up while reproducing a paper count too.** If you find during a reproduction that the results don't match, that a step isn't described clearly in the paper, or that the method breaks under a different setting, any of these can become a new problem `[Our analysis]`.

Using "large language models and smart contract security" as an example `[Our analysis]`:

| What you noticed in the papers | Possible candidate problem |
|---|---|
| Several papers test only on the same public dataset | Do the conclusions still hold on other contracts? |
| The paper reports only the detection rate, not false positives | How many false positives can there be before developers stop using the tool? |
| The prompts were handwritten by the authors, with no explanation of how they were chosen | Do the results change much with a different prompt? |
| When you reproduce it, a baseline performs much worse than the paper reports | What about the original paper's setup was left unwritten? |

**Write it down:** Pick three of the most relevant papers you have read, and for each write at least one question of the form "what did the authors simplify?" or "do the conclusions generalize?".

## 3. Look where things don't work well in practice

A method that works in a paper doesn't necessarily work in practice. **Look at where existing methods or systems do badly**[^eisnerproblems-e5].

**Some concrete ways to do this:**

- **Stress-test the state of the art.** Don't just run it on the fixed benchmark; put it on more diverse, less constrained examples and see how it fails. This is a good way to find the limitations of existing work, and your work can start by filling that gap[^huang2021ideas-e4].
- **Leave the lab setting.** Take computer security as an example: a paper summarizing the pitfalls of using machine learning in security research lists "evaluating only in a lab setting without discussing practical limitations" as one of them, and recommends evaluating in a real-world setting whenever possible[^arp2022dos-e2]. Turned around, "what happens in a real-world setting?" can itself be a question no one has answered yet `[Our analysis]`.
- **Look at the data.** In many fields, the data itself suggests problems[^eisnerproblems-e6]. Going through real contracts and real vulnerability reports by hand often shows you cases the papers never mention `[Our analysis]`.
- **Find the bottlenecks holding everyone back.** Ask yourself: which problems, whether widely recognized or not, are blocking progress in this field? Can you solve them? If not, can you at least explain them clearly[^eisnerproblems-e3]?

In smart contract security, you could try `[Our analysis]`:

- Applying a detection method widely accepted as effective to recently deployed contracts, and seeing what it misses;
- Asking a few developers who write contracts why they don't use existing detection tools;
- Reading a batch of real incident reports on vulnerabilities and seeing how many classes of vulnerability existing tools don't consider at all.

**Write it down:** Pick a method or tool in your research area that is "widely accepted as effective". Write down how you plan to find where it falls short in practice (different data, different settings, asking users), and where you expect it to fail.

## 4. Question the assumptions of existing work

Every study rests on assumptions. Some are written in the paper; some even the authors aren't aware of. **Find those assumptions and ask "what if this doesn't hold?"**, and you have candidate problems `[Our analysis]`.

**How to do it:**

- **List the assumptions and try relaxing them.** Find the assumptions behind existing work and try to relax them, so the method also works under fewer constraints[^huang2021ideas-e1].
- **Or the reverse: add assumptions.** Take a general-purpose method, apply it to your specific problem, and use domain knowledge to improve it[^huang2021ideas-e2]. For example, a general code vulnerability detection method applied to smart contracts can exploit the structure specific to contracts `[Our analysis]`.
- **Ask "dumb questions".** One trick in mathematics is to take a well-known lemma and ask what happens if you remove one hypothesis, or whether the conclusion can be strengthened[^taocareer-e8]. In your research area, that means asking the same of a widely accepted conclusion `[Our analysis]`.
- **Look at how the problem was framed.** For how a problem was originally framed and which assumptions were used to get from evidence to conclusion, and how to find these unstated things, see [Read with questions in mind](01_enter-a-field.md#5-read-with-questions-in-mind) in the last chapter.

**Pay special attention to practices the whole research area keeps following.** Once you have read the papers, you need to be able to set existing work aside: what has been done has been done[^carlini2026best-e6]. Sometimes an influential early paper makes a key mistake in its method, approach, or evaluation, and later researchers follow it without thinking because "that's how everyone does it"[^carlini2026best-e7]. One sign: when you read papers in a research area, you keep wanting to ask, "Why is everyone doing it in a way that's obviously wrong?"[^carlini2026best-e9]

Assumptions you could question in the smart contract research area `[Our analysis]`:

- "The vulnerability labels in the benchmark are correct": who labeled them, and how were they checked?
- "A high detection rate means a good tool": is that really what developers care about?
- "The large language model hasn't seen the contracts in the benchmark": public contracts may well be in its training data.

**Write it down:** Pick the one or two most influential papers in your research area and list three assumptions they rely on. For each, write one sentence on "what would happen if it didn't hold".

## 5. Re-examine how others evaluate

> This section is for research whose conclusions rest on experiments or measurement. If you do proofs or textual interpretation, you can skip it.

**The evaluation practice that is standard in a research area can itself be flawed, and the flaw can be widespread.** Both examples below come from computer security:

- Researchers examined the experimental evaluations of 32 fuzzing papers (fuzzing is a way of testing programs with large numbers of random inputs to find bugs) and found problems in every one[^klees2018evaluating-e2].
- Another study analyzed 30 papers from top security venues over the past ten years that used machine learning; every paper had at least three pitfalls, and several pitfalls affected most of the papers[^arp2022dos-e3].

Our sources give no evidence on whether other research areas are the same. But these two examples show that **re-examining a research area's evaluation practice can turn up real problems**, so it is worth spending some time checking `[Our analysis]`.

**Things you can check (the examples still come from security):**

- **Do the conclusions hold with a different set of evaluation targets?** One published fuzzer did well on the programs chosen in its original paper, but on two programs used in other papers it no longer beat the baseline[^klees2018evaluating-e3].
- **Has the benchmark been "worn out"?** When a fixed benchmark is used too much, tools may start to rely on heuristics that bring no fundamental advantage but happen to suit that benchmark[^klees2018evaluating-e7]. Work on machine learning in security gives a similar warning: as the characteristics of public datasets become better and better understood, methods developed on them implicitly exploit information about the test data, so experiments on well-known datasets should be complemented with more recent data[^arp2022dos-e5].
- **Is the comparison fair? Are the conclusions really supported[^eisnerread-e8]?** Specifically, check whether the baselines are too weak and whether the metrics were chosen to flatter the authors' method `[Our analysis]`.

If you find a problem like this, "pointing it out and fixing it" can be a study in its own right, belonging to the Measurement strategy; see [Key concepts](../00_start-here/key-concepts.md#research-strategy). Whether such a finding is enough for a project is for the next chapter to judge.

**Write it down:** List the two or three most commonly used benchmarks or evaluation practices in your research area. For each, write down what you suspect might be wrong with it, and the simplest way you could check that suspicion.

## 6. Bring in ideas from elsewhere

**Something already solved in one field may not yet have been tried in another.** Keeping an eye on neighboring fields is another way to find problems `[Our analysis]`.

**How to do it:**

- **Watch for new tools.** When a new tool appears in a field, try it on your own problem[^huang2021ideas-e3]. The research area "large language models and smart contract security" is itself a new tool brought to an old problem `[Our analysis]`.
- **Look for similar problems.** If you notice that your problem resembles (or is at least analogous to) a problem in another field, read the literature on that problem and ask experts in that field for their latest thinking[^taocareer-e21]. For example, vulnerability detection for ordinary software has many years of work behind it; which of its techniques haven't yet been applied to smart contracts `[Our analysis]`?
- **Ask people in another discipline.** If your research area is interdisciplinary, ask people in the other discipline what they find interesting[^eisnerproblems-e5].
- **Look one step ahead.** Instead of only watching what everyone is doing now, anticipate which big problems will appear once new technologies arrive[^huang2023decide-e3].

**Before you bring something over, be clear about why things are different here.** Just "applying A to B" is easily seen as lacking novelty. You need to be able to say where the two fields differ, and why that difference makes the transfer challenging and worth doing `[Our analysis]`.

**Write it down:** Name a field next to your research area, and list two techniques that are fairly mature there but that no one has tried (or you haven't seen tried) in your research area.

## 7. Talk to people

**Some problems aren't in papers; they're in people's heads.** Your advisor will point you to open problems and folklore that circulates in the field but isn't written down[^taocareer-e23]; people who work with the door closed may, years later, not know what problems are worth working on[^hamming1986you-e18]. Why to talk to people and how to find them is already covered in [Talk to people who know the area](01_enter-a-field.md#8-talk-to-people-who-know-the-area) in the last chapter. This section covers only what matters when you are looking for problems.

- **Don't be afraid to work on someone else's suggestion.** There is nothing shameful about working on an idea suggested by someone experienced: ideas are plentiful, and the skill lies in which one you pick and how well you execute it[^schulman2020opinionated-e4].
- **Ask users and practitioners.** In the smart contract area, that means developers who write contracts and people who do audits. They know what doesn't work well in practice `[Our analysis]`.
- **Ask about problems "everyone knows are important but no one has seriously worked on".** Every field has them; if you think you have found one, ask colleagues and check the literature to confirm no one has done it[^eisnerproblems-e4].

**Bring something concrete when you talk.** Don't just ask "what do you think I should work on?"; bring your list of ideas (next section) and ask "which of these do you find interesting, and which have already been done?" `[Our analysis]`.

**Write it down:** List three people you could talk to (at least one outside your research group), and one specific question you plan to ask each of them.

## 8. Keep a list of ideas

**Everything you found in the sections above goes into one list.** Ideas you don't write down are soon forgotten; once they're written down, you can compare them, revise them, and come back to them later.

**Why keep them instead of throwing them away once used.** Most great scientists carry 10 to 20 important problems in their heads, always looking for a way to attack them; when they see a new idea, they immediately recognize which problem it bears on[^hamming1986you-e10]. An idea that keeps coming back to you over months or even years is a good sign that you are genuinely interested in it[^alon2009choose-e13], and you can only see that if you write it down and look again later `[Our analysis]`. Keep even your embarrassingly wrong ideas privately; you may be able to salvage something useful from them later[^taocareer-e19].

**How to keep it:**

- Keep it in one fixed place, and jot down ideas every day[^schulman2020opinionated-e16];
- Every week or two, read through it and write up a short summary[^schulman2020opinionated-e17];
- For each entry, write at least the following `[Our analysis]`:

| Field | What to write | Example |
|---|---|---|
| One sentence | What is wrong or unknown | The high accuracy of existing large-language-model vulnerability detection may come partly from benchmark leakage |
| Source | Where it came from (which of Sections 2–7) | Section 4: questioning the assumption that "the model hasn't seen the benchmark" |
| Trigger | Which paper, conversation, or data | A paper whose benchmark comes from a public contract repository |
| Quickest test | A small test you can do in a week or two | Sample 50 benchmark items and check whether they have appeared publicly |
| Date and status | New / thinking about it / dropped (give the reason) | Dropped: already published by group X, see paper Y |

**How long should the list be?** Our sources give no single number. As a reference point `[Our analysis]`: before the first screen, around ten entries from at least three different sources makes it easier to pick out the really good ones. If they all come from the same source (for example, all of them are "some paper on a different dataset"), you haven't searched widely enough.

**Write it down:** Set up your list of ideas, put in every idea that came up in the earlier "Write it down" exercises, and fill in all five fields for each.

## 9. Quick first screen: keep two to four

Once the list is long enough, do a **rough screen**. This step takes only an hour or two. The aim isn't to pick your final topic, but to cross out the ones clearly not worth deeper thought and keep two to four to take into the next chapter, where you converge on one carefully `[Our analysis]`.

**For each idea, quickly ask four things** `[Our analysis]`:

1. **Can you say in one sentence what is wrong?** If not, leave it on the list to keep thinking about, but not in this round.
2. **Can you see a way in?** What makes a problem important is not just how big the payoff would be, but whether you have a reasonable way to attack it[^hamming1986you-e2]. If you can't even think of a first step, set it aside.
3. **Is it completely dominated by another entry?** If A beats B on both feasibility and value, you can cross out B[^alon2009choose-e6]. A rough look is enough; you don't need to score them.
4. **Do you still keep thinking about it?** Ask yourself: if I were the only person in the world, which of these would I work on[^alon2009choose-e12]? At the same time, notice whether you really find it interesting or only because everyone is doing it. Don't pile onto the hottest problems[^huang2023decide-e1]; the risk of being scooped is higher there `[Our analysis]`.

**What this step doesn't do.** It doesn't settle "has anyone done this?", doesn't work out "what evidence would I need?", and doesn't assess data or compute. Those are the six questions of [Converging on a project](05_converge.md), and you ask them seriously for the two to four candidates. In the first screen, spend only a few minutes on each entry `[Our analysis]`.

**If you aren't sure, ask your advisor to help you screen.** Give your advisor the list and ask them to rate each entry from 1 to 10, then discuss in depth the ones where you disagree most[^olah2021taste-e4]. This is screening, and it is also practice in judging which problems are good. For how to build up this ability (often called "research taste") over the long term, see [Build your research taste deliberately](../08_throughout/mindset_and_growth.md#1-cultivate-research-taste-on-purpose).

**Write it down:** On your list of ideas, mark the two to four entries you kept this round, and for each one you crossed out write one sentence on why ("no way in", "dominated by entry X", and so on).

---

## Judgment calls

**When should you stop looking and start screening?** Here's one way to decide `[Our analysis]`:

| Situation | What to do |
|---|---|
| Fewer than five entries, or all from the same source | Keep looking, using a method from Sections 2–7 you haven't tried yet |
| The list is long enough, but nothing survives a round of crossing out | Most likely you searched too narrowly or aimed too big; go back to Sections 3 and 4 and look in practice and in assumptions |
| The list is long enough and two to four survive the first screen | Move on to the next chapter |
| The time you gave yourself is up and you still can't decide | Take the list to your advisor and pick two to four together |

**Should you keep an idea that isn't "big" enough?** In the first screen, don't worry much about size. Many small problems get rewritten, merged, or scaled up during convergence; restating a problem slightly can often turn good work into great work[^hamming1986you-e13]. But be wary of ideas that can "only push some metric up a little"; their ceiling is low from the start[^schulman2020opinionated-e10].

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Grabbing the first problem that comes to mind | A project takes years, and a hasty choice leads to a lot of frustration[^alon2009choose-e8] |
| Reading endlessly without writing down ideas or trying anything | You are bound to start before you fully understand; judgment depends on practice[^eisnerproblems-e8][^olah2021taste-e9] |
| Drawing on only one source, such as "some paper on a different dataset" | The ideas all look alike, and you easily collide with others who read the same literature[^schulman2020opinionated-e7] |
| Only looking for faults when reading papers | You miss the good ideas in a paper that could be used elsewhere[^eisnerread-e6] |
| Keeping ideas only in your head | You forget them, and can't compare them or come back to them `[Our analysis]` |
| Not talking to people | You miss open problems and existing work that people in the field know about but that aren't in papers yet[^taocareer-e23][^eisnerproblems-e9] |
| Thinking every entry through in depth during the first screen | Time goes into ideas that will be crossed out anyway; save in-depth judgment for the next chapter `[Our analysis]` |
| Chasing the hottest research area | Don't pile onto the hottest problems[^huang2023decide-e1]; outside the hottest area it is actually much easier to stand out[^carlini2026best-e12] |

## What you should have at the end

- A list of about ten ideas from at least three sources, each with all five fields filled in (Section 8)
- The result of the first screen: the two to four entries you kept, and the reason each of the others was crossed out (Section 9)
- A "quickest test" for each candidate you kept

## Checklist before moving on

You are ready for the next step when:

- [ ] Your list of ideas has about ten entries from at least three different sources
- [ ] For each entry you can say in one sentence what is wrong or unknown
- [ ] You have discussed the list with your advisor or at least one other person who knows the area
- [ ] Two to four entries survived the first screen, and you can say why you kept them and why you crossed out the rest
- [ ] For each candidate you kept, you have thought of a small test you can run within a week or two

## When to go back

| If this happens | Go back to |
|---|---|
| Weeks of thinking and you can't write down a single idea | [Entering a field and exploring the literature](01_enter-a-field.md): read another batch, especially papers and surveys from the last year or two |
| For every idea, you can't say what is wrong | You still know too little about the field; go back to [Entering a field and exploring the literature](01_enter-a-field.md) |
| Everything on your list has already been done by others | Change sources: look where things don't work in practice (Section 3) or at evaluation problems (Section 5), or talk to people (Section 7) |
| You have lost interest in the research area itself | Talk to your advisor and consider switching areas; forcing yourself to work on a topic you aren't excited about makes you far less productive[^olah2021taste-e3] |

## Next

Take the two to four candidates that survived the first screen into [Converging on a project](05_converge.md): write each candidate as one sentence you want to prove, judge whether it is worth doing, whether others have done it, what evidence it needs, and whether you can pull it off, and finally converge on a one-page project summary.

During convergence, some candidates will be ruled out. Put them back on your list of ideas with the reason; if none of the candidates hold up, come back to this chapter and do another round.

[^alon2009choose-e6]: Alon 2009, The Two Dimensions of Problem Choice. [Evidence](../../sources/notes/alon2009choose.md#e6)
[^alon2009choose-e8]: Alon 2009, Take Your Time. [Evidence](../../sources/notes/alon2009choose.md#e8)
[^alon2009choose-e9]: Alon 2009, Take Your Time. [Evidence](../../sources/notes/alon2009choose.md#e9)
[^alon2009choose-e10]: Alon 2009, Take Your Time. [Evidence](../../sources/notes/alon2009choose.md#e10)
[^alon2009choose-e12]: Alon 2009, The Subjectivity of the Interest Axis. [Evidence](../../sources/notes/alon2009choose.md#e12)
[^alon2009choose-e13]: Alon 2009, The Subjectivity of the Interest Axis. [Evidence](../../sources/notes/alon2009choose.md#e13)
[^arp2022dos-e2]: Arp et al. 2022, §2, P9 Lab-Only Evaluation. [Evidence](../../sources/notes/arp2022dos.md#e2)
[^arp2022dos-e3]: Arp et al. 2022, Abstract. [Evidence](../../sources/notes/arp2022dos.md#e3)
[^arp2022dos-e5]: Arp et al. 2022, §2, P3 Data Snooping. [Evidence](../../sources/notes/arp2022dos.md#e5)
[^carlini2026best-e6]: Carlini 2026, Ignore all the papers. [Evidence](../../sources/notes/carlini2026best.md#e6)
[^carlini2026best-e7]: Carlini 2026, Ignore all the papers. [Evidence](../../sources/notes/carlini2026best.md#e7)
[^carlini2026best-e9]: Carlini 2026, Do something only you can do. [Evidence](../../sources/notes/carlini2026best.md#e9)
[^carlini2026best-e12]: Carlini 2026, Get lucky: you're well suited to solve important problems. [Evidence](../../sources/notes/carlini2026best.md#e12)
[^carlini2026best-e13]: Carlini 2026, Pick your ideas for impact. [Evidence](../../sources/notes/carlini2026best.md#e13)
[^eisnerproblems-e2]: Eisner, How to Find Research Problems, "small bones". [Evidence](../../sources/notes/eisnerproblems.md#e2)
[^eisnerproblems-e3]: Eisner, How to Find Research Problems, "big bones". [Evidence](../../sources/notes/eisnerproblems.md#e3)
[^eisnerproblems-e4]: Eisner, How to Find Research Problems, "ripe for the plucking". [Evidence](../../sources/notes/eisnerproblems.md#e4)
[^eisnerproblems-e5]: Eisner, How to Find Research Problems, "identify new interesting problems". [Evidence](../../sources/notes/eisnerproblems.md#e5)
[^eisnerproblems-e6]: Eisner, How to Find Research Problems, "identify new interesting problems". [Evidence](../../sources/notes/eisnerproblems.md#e6)
[^eisnerproblems-e8]: Eisner, How to Find Research Problems, Finally. [Evidence](../../sources/notes/eisnerproblems.md#e8)
[^eisnerproblems-e9]: Eisner, How to Find Research Problems, Finally. [Evidence](../../sources/notes/eisnerproblems.md#e9)
[^eisnerread-e3]: Eisner 2009, How to Read a Technical Paper. [Evidence](../../sources/notes/eisnerread.md#e3)
[^eisnerread-e6]: Eisner 2009, How to Read a Technical Paper. [Evidence](../../sources/notes/eisnerread.md#e6)
[^eisnerread-e8]: Eisner 2009, How to Read a Technical Paper. [Evidence](../../sources/notes/eisnerread.md#e8)
[^hamming1986you-e2]: Hamming 1986, "important problems" paragraph. [Evidence](../../sources/notes/hamming1986you.md#e2)
[^hamming1986you-e10]: Hamming 1986, after "Great Thoughts Time". [Evidence](../../sources/notes/hamming1986you.md#e10)
[^hamming1986you-e13]: Hamming 1986, paragraph on solving a problem as a class of problems. [Evidence](../../sources/notes/hamming1986you.md#e13)
[^hamming1986you-e18]: Hamming 1986, "door open or the door closed" paragraph. [Evidence](../../sources/notes/hamming1986you.md#e18)
[^huang2021ideas-e1]: Huang 2021, Relax assumptions. [Evidence](../../sources/notes/huang2021ideas.md#e1)
[^huang2021ideas-e2]: Huang 2021, Make more assumptions. [Evidence](../../sources/notes/huang2021ideas.md#e2)
[^huang2021ideas-e3]: Huang 2021, Grab a powerful hammer and find all the nails. [Evidence](../../sources/notes/huang2021ideas.md#e3)
[^huang2021ideas-e4]: Huang 2021, Stress test the state-of-the-art. [Evidence](../../sources/notes/huang2021ideas.md#e4)
[^huang2023decide-e1]: Huang 2023, Find your position. [Evidence](../../sources/notes/huang2023decide.md#e1)
[^huang2023decide-e3]: Huang 2023, Anticipate disruptive technologies. [Evidence](../../sources/notes/huang2023decide.md#e3)
[^klees2018evaluating-e2]: Klees et al. 2018, Abstract. [Evidence](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e7]: Klees et al. 2018, §8. [Evidence](../../sources/notes/klees2018evaluating.md#e7)
[^olah2021taste-e3]: Olah 2021, opening section. [Evidence](../../sources/notes/olah2021taste.md#e3)
[^olah2021taste-e4]: Olah 2021, Exercise 1. [Evidence](../../sources/notes/olah2021taste.md#e4)
[^olah2021taste-e9]: Olah 2021, Failure mode 2. [Evidence](../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e12]: Olah 2021, Andy Matuschak's advice collected at the end. [Evidence](../../sources/notes/olah2021taste.md#e12)
[^schulman2020opinionated-e4]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e6]: Schulman 2020, Idea-Driven vs Goal-Driven Research. [Evidence](../../sources/notes/schulman2020opinionated.md#e6)
[^schulman2020opinionated-e7]: Schulman 2020, Idea-Driven vs Goal-Driven Research. [Evidence](../../sources/notes/schulman2020opinionated.md#e7)
[^schulman2020opinionated-e8]: Schulman 2020, Idea-Driven vs Goal-Driven Research. [Evidence](../../sources/notes/schulman2020opinionated.md#e8)
[^schulman2020opinionated-e10]: Schulman 2020, Aim High, and Climb Incrementally Towards High Goals. [Evidence](../../sources/notes/schulman2020opinionated.md#e10)
[^schulman2020opinionated-e16]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e17)
[^taocareer-e8]: Tao, Career advice, Ask yourself dumb questions – and answer them! [Evidence](../../sources/notes/taocareer.md#e8)
[^taocareer-e19]: Tao, Career advice, Use the wastebasket. [Evidence](../../sources/notes/taocareer.md#e19)
[^taocareer-e21]: Tao, Career advice, Be sceptical of your own work. [Evidence](../../sources/notes/taocareer.md#e21)
[^taocareer-e23]: Tao, Career advice, Talk to your advisor. [Evidence](../../sources/notes/taocareer.md#e23)
