# Generating candidate problems

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. Each of the four generation methods comes from somewhere specific: the steps for questioning assumptions come from management research, the list of question types from software engineering, and the sentence template for turning a topic into a question from university writing instruction.

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Set aside a block of time for generating problems.** Write down the start and end dates, and during that time read, write, and try things side by side. Then pick a starting point: the literature or a goal ([Section 1](#1-set-the-time-and-the-starting-point)).
> 2. **Use at least two methods, and make at least one of them something other than gap-spotting.** Gap-spotting is the easiest way in, but its ideas tend to collide with other people's. Pair it with questioning assumptions, working through the question types, or turning a topic into a question ([Section 2](#2-method-1-gap-spotting) to [Section 5](#5-method-4-turn-a-topic-into-a-question)).
> 3. **Take your list to people and talk it through.** Don't just ask "what should I work on?" Ask "which of these is interesting, and which has already been done?" ([Talk to people](#talk-to-people)).
> 4. **Put everything into one list of ideas.** For each entry, write down what is wrong or unknown, where it came from, and the quickest way to test it. For your top two or three, also write the three-part sentence ([Section 7](#7-keep-a-list-of-ideas)).
>
> **Done these? Move on:** your list has about ten entries from at least three methods or sources, you can state each one in a sentence, and you have talked it over with at least one advisor or other person who knows the area. Next: [Exploring hands-on](03_explore.md).

## Where you are

You have entered a research area and read a batch of core papers. You roughly know what the field is doing, who is doing it, and with what approaches. Say your advisor gave you the research area "using large language models for smart contract security". You have read twenty or thirty related papers and kept a problem log of questions that came up while reading.

But you still don't know what you are going to work on. You may have one or two vague notions, or none at all. What worries you is: haven't all the good problems been taken already? How am I supposed to "come up with" a topic?

## What this stage is for

From a **research area**, generate a **batch** of candidate **problems** and collect them in a list of ideas to take into the next step.

A "problem" here means something in the field that is wrong, not good enough, or not yet known; see [Key concepts](../00_start-here/key-concepts.md#problem). It doesn't yet need to be a research question you can answer directly, let alone a finished claim. That is the job of [Converging on a project](05_converge.md).

This chapter asks you to do two things:

1. Generate problems with a few **methods you can actually follow**, instead of waiting for inspiration;
2. **Write down** everything you generate, building up a list of ideas.

How to try ideas out and how to screen them are covered in [Exploring hands-on](03_explore.md) and [Judging and screening ideas](04_judge-and-screen.md).

**Why a batch and not just one?** A common mistake in choosing a problem is to grab the first one that comes to mind. A project usually takes several years, and a hasty choice leads to a lot of frustration[^alon2009choose-e8]. With only one idea, you have nothing to compare it with, so you can't judge whether it is any good.

## How to use this chapter

Sections 2–5 are four methods for generating problems; Section 6 adds a few more places to look. For each method you get how to do it, when to use it, and what it tends to produce, and the same research area is walked through every time. You will see four different routes arrive at the same candidate problem: "The reported results of large-language-model vulnerability detectors may be inflated by data leakage."

You don't need all four. A rule of thumb `[Our analysis]`: use at least two, and make at least one of them something other than gap-spotting. Ideas from a single method tend to look alike.

---

## 1. Set the time and the starting point

**Mark out a definite period for generating problems.** Good problems don't show up while you are reading your first paper. One piece of advice is that a new student or postdoc should not commit to a project in their first 3 months, and should use that time to read, discuss, and plan[^alon2009choose-e9]. Rushing into an idea as soon as it looks feasible also tends to go wrong; if you spend more time with it, you can often come up with a deeper version[^olah2021taste-e12].

But you can't only read and think. The ability to judge whether a problem is good depends on actually doing the work[^olah2021taste-e9]; for how to try things out while you think, see [Exploring hands-on](03_explore.md). The last chapter already said not to let background reading drag on and to alternate reading with thinking; see [Entering a field and exploring the literature](01_enter-a-field.md#judgment-calls).

> **Where sources disagree: how long should finding a problem take?**
> - **Take more time:** an extra week spent choosing a problem can save months or even years later[^alon2009choose-e8]. But the person who gives this advice also admits that not everyone is free to choose their own problem or has the time for a long search[^alon2009choose-e10].
> - **Don't drag it out:** start thinking for yourself early and alternate with reading[^eisnerproblems-e9]; once you have searched for ideas for a while, an extra hour of thinking is worth less than just going and doing something[^carlini2026best-e13].
>
> In practice `[Our analysis]`: give yourself a set period (a few weeks to three months, depending on your stage and what your advisor expects), and during it read, write, and try **at the same time**. When the time is up, move on to [Judging and screening ideas](04_judge-and-screen.md); if you can't narrow it down, take your list to your advisor and decide together.

**Two starting points.** There are roughly two places to start looking for problems[^schulman2020opinionated-e6][^schulman2020opinionated-e8]:

- **Idea-driven (start from the literature)**: you read "how others do X", think of a way to do it better, and then test it. The downside is that it is easy to get scooped, because everyone reads the same literature and has similar ideas[^schulman2020opinionated-e7].
- **Goal-driven**: you set a concrete goal first, such as "let developers reliably find reentrancy vulnerabilities before they deploy a contract", and then solve the problems that stand in the way. The goal gives you a distinctive perspective and leads you to ask questions others haven't asked[^schulman2020opinionated-e8].

The methods below work from either starting point. The difference is that, starting from a goal, you will more often ask "what's still missing between here and the goal", not just "how else could this paper be improved" `[Our analysis]`.

**Write it down:** Write down the period you have set for generating problems (from which day to which day), and whether you plan to start from the literature, from a goal, or try both. If you start from a goal, state it in one sentence.

## 2. Method 1: gap-spotting

**What it is.** You find what the existing literature hasn't done, or hasn't done well, and pose a question to fill it. The management researchers Alvesson and Sandberg call this "gap-spotting": formulating research questions by identifying or constructing gaps in the existing literature[^alvesson2013has-e2]. Constructing a gap often means bringing different bodies of literature together[^alvesson2013has-e4].

**How to do it** `[Our analysis]`:

1. **Go back to your problem log and the core papers.** The last chapter had you start a problem log; see [Entering a field and exploring the literature](01_enter-a-field.md#6-take-notes-one-per-paper-plus-a-problem-log). For the most relevant papers, reread their "Limitations" and "Future work" sections.
2. **Look for the authors' simplifications and arbitrary choices.** Where did the authors make a simplification that might hurt, or an arbitrary choice? Those are your chances to do it differently[^eisnerproblems-e2]. For example, a paper considers only one type of vulnerability, uses only one model, or tests on only one dataset, without saying why.
3. **Come up with an example that would embarrass the authors.** Think of examples that illustrate the authors' idea, and examples that would make their claims fall apart[^eisnerread-e3].
4. **Re-examine how others evaluate.** Is the comparison fair? Are the conclusions really supported[^eisnerread-e8]? Specifically, check whether the baselines are too weak and whether the metrics were chosen to flatter the authors' method `[Our analysis]`.
5. **Write each gap as a question.**

Whether the experiments are fair, whether the conclusions generalize, and where else the paper's good ideas might apply are already listed under [Read with questions in mind](01_enter-a-field.md#5-read-with-questions-in-mind) in the last chapter, so we won't repeat them here. Things you hit while reproducing a paper (results that don't match, a step the paper never spells out, a method that breaks under a different setting) can all become new problems too `[Our analysis]`.

**Why step 4 deserves extra time.** The evaluation practice that is standard in a research area can itself be flawed, and the flaw can be widespread. All the examples below come from computer security:

- Researchers examined the experimental evaluations of 32 fuzzing papers (fuzzing is a way of testing programs with large numbers of random inputs to find bugs) and found problems in every one[^klees2018evaluating-e2]. Another study analyzed 30 papers from top security venues that used machine learning; every paper had at least three pitfalls[^arp2022dos-e3].
- A different set of evaluation targets can flip the conclusion: one published fuzzer no longer beat the baseline on two programs used in other papers[^klees2018evaluating-e3].
- Benchmarks wear out: when a fixed benchmark is used too much, tools may start to rely on special-purpose tweaks that bring no fundamental advantage[^klees2018evaluating-e7]. And the better a public dataset is understood, the more the methods built on it implicitly exploit information about the test data, so experiments on well-known datasets should be complemented with more recent data[^arp2022dos-e5].

Our sources give no evidence on whether other research areas are the same `[Our analysis]`. If you do proofs or textual interpretation, you can skip step 4.

**Walking through the example** `[Our analysis]`:

| What you noticed in the papers | The gap, written as a question |
|---|---|
| Several papers test on the same public dataset, built from a public contract repository | On new contracts deployed after the model was trained, is the detection rate still as high? |
| The paper reports only the detection rate, not false positives | How many false positives can there be before developers stop using the tool? |
| The prompts were handwritten by the authors, with no explanation of how they were chosen | Do the results change much with a different prompt? |
| When you reproduce it, a baseline performs much worse than the paper reports | What about the original paper's setup was left unwritten? |

The first row is the way in to "the results are inflated by leakage". For now it is only the gap "no one has tested on new contracts"; it doesn't yet say why the results might differ.

**When to use it, and what it produces** `[Our analysis]`: it is easiest once you have read a batch of papers and have a problem log, and it almost always produces a batch of problems. Most of them are "extend it" or "fill it in" problems: doable, but often incremental.

**Its limits.** Alvesson and Sandberg don't deny that gap-spotting can lead to important contributions, but because it does not deliberately question the assumptions underlying the existing literature, it rarely leads to new high-ranking theories[^alvesson2013has-e5]. In management research, they observe, gap-spotting is almost totally dominant[^alvesson2013has-e1]. That is a judgment about management research; our sources give no evidence on whether other fields are the same. Also, everyone reads the same literature and spots similar gaps, so it is easy to get scooped[^schulman2020opinionated-e7]. That is why you shouldn't rely on this method alone `[Our analysis]`.

**Write it down:** Pick three of the most relevant papers you have read. For each, write at least one gap, phrased as a question.

## 3. Method 2: questioning assumptions (problematization)

**What it is.** Instead of filling a gap in the literature, you formulate research questions by challenging the dominant assumptions in it. Alvesson and Sandberg call this "problematization" and offer it as the alternative to gap-spotting[^alvesson2013has-e8]. Their reasoning: if a theory doesn't significantly challenge some of its audience's assumptions, it is unlikely to receive attention, even if it has been extremely rigorously developed[^alvesson2013has-e6].

The method comes from management research. Their example: the overwhelming majority of leadership research assumes that employees need or want to be led. Problematization can treat that as a false assumption or an open issue, and even suggest that some people want to be spared leadership at work[^alvesson2020problematizing-e3].

**How to do it.** They give six steps[^alvesson2020problematizing-e5]. Here they are in order, each with what it looks like in our example `[Our analysis]`:

1. **Identify a domain of literature.** For example: "papers that use large language models to detect smart contract vulnerabilities and report results on public benchmarks". Rather than skimming a large pile, read the foundational papers and a moderate number of representative ones in depth; that makes it easier to spot the assumptions taken for granted[^alvesson2020problematizing-e4]. As you read, you may revise the boundaries of the domain, and that is fine[^alvesson2020problematizing-e7].
2. **Identify and articulate the underlying assumptions.** Some are written in the papers; some even the authors aren't aware of `[Our analysis]`. Example: "The vulnerability labels in the benchmark are correct." "A high detection rate means a good tool." "The large language model hasn't seen the contracts in the benchmark."
3. **Evaluate them and focus on the most problematic or limiting ones.** Example: the third is the most suspect, because public contracts may well be in the model's training data.
4. **Develop an alternative set of assumptions.** It should have the potential to be the starting point of a new contribution. Example: "The model may have seen the benchmark contracts, so part of the high score comes from memorization, not from actually finding vulnerabilities."
5. **Consider your audience.** What would readers in this area find new, credible, and interesting? Example: people who build detectors will care, because it bears on whether published results can still be trusted.
6. **Evaluate the alternative assumptions.** Ask whether they could open a new, counterintuitive conversation with others in the field[^alvesson2020problematizing-e6]. Example: if true, everyone would need to look again at the existing rankings, which is a counterintuitive conclusion.

The candidate problem you end up with: **"How much of the existing benchmark results comes from the model memorizing the benchmark contracts?"** It points to the same thing as Method 1's "Is the detection rate still as high on new contracts?", but now it says **why** the results might differ.

**Some help with step 2, finding assumptions:**

- **List the assumptions and try relaxing them**, so the method also works under fewer constraints[^huang2021ideas-e1]. **Or the reverse: add assumptions**, taking a general-purpose method to a specific problem and using domain knowledge to improve it[^huang2021ideas-e2].
- **Ask "dumb questions".** One trick in mathematics is to take a well-known lemma and ask what happens if you remove one hypothesis[^taocareer-e8]. In your research area, that means asking the same of a widely accepted conclusion `[Our analysis]`.
- **Pay special attention to practices the whole research area keeps following.** Sometimes an influential early paper makes a key mistake in its method or evaluation, and later researchers follow it without thinking because "that's how everyone does it"[^carlini2026best-e7]. One sign: you keep wanting to ask, "Why is everyone doing it in a way that's obviously wrong?"[^carlini2026best-e9]
- **Look at how the problem was framed.** For how a problem was originally framed and which assumptions were used to get from evidence to conclusion, see [Read with questions in mind](01_enter-a-field.md#5-read-with-questions-in-mind) in the last chapter.
- **Start from surprises.** They also describe another route: pay special attention to the unexpected things in your empirical material that puzzle you, first "create a mystery", then "solve it"[^alvesson2013has-e13]. A strange pattern you notice while going through real data is often a clue that an assumption is off `[Our analysis]`.

**Limits the authors themselves name:**

- **It is not a mechanical procedure.** Problematization depends heavily on creativity, intuition, reading, and talking to people; they have no strong belief in mechanical procedures, only that some structure helps[^alvesson2013has-e11].
- **There are no guarantees.** Almost by definition, most research can't be really interesting, because interesting means clearly above the average[^alvesson2013has-e12].
- **You still need to know the field.** Taking this route still requires a reasonable knowledge of your area and positioning yourself against the significant existing studies[^alvesson2013has-e14]; assumption-challenging research has to connect to the established literature for others to see it as meaningful[^alvesson2013has-e7].
- **It is hard and demanding.** They admit that the underlying assumptions are hard to detect, that the approach gives the researcher too much discretion, and that it is too demanding[^alvesson2020problematizing-e8].

**Two ways it goes wrong:**

- **Pseudo-problematization.** Simply criticizing others from your own favorite ready-made theory only reproduces that theory's assumptions and is unlikely to lead to new ideas[^alvesson2013has-e9].
- **Questioning for its own sake.** Problematization does not mean dismissing everything that came before; you should also point out high-quality studies and ideas[^alvesson2020problematizing-e10].

**When to use it, and what it produces** `[Our analysis]`: it fits best once you have read a batch of papers and are starting to feel "everyone does it this way, but something seems off". It produces fewer problems than gap-spotting, but they are more likely to carry weight. It is harder than gap-spotting; the first time you try it, go through steps 2 and 3 with your advisor.

**Write it down:** Pick the one or two most influential papers in your research area and work through the six steps: the domain of literature, three assumptions, the one you find most suspect, the alternative assumption, and why readers would care.

## 4. Method 3: work through the question types

**What it is.** Research questions come in a few common types. Take one object in your research area and ask a question of each type about it, and you get a whole string of candidate problems at once. The classification below comes from empirical research in software engineering[^easterbrook2008selecting-e38]; it may not fit interpretive research in the humanities `[Our analysis]`.

**Question types and how to ask them:**

| Type | How to ask | Example: the object is "reported results of large-language-model vulnerability detection" `[Our analysis]` |
|---|---|---|
| Existence | Does X exist?[^easterbrook2008selecting-e44] | Does the benchmark contain contracts that were public before the model was trained? |
| Description and classification | What is X like? How can it be categorized? How can we measure it?[^easterbrook2008selecting-e44] | What kinds of leakage are there (verbatim copies, copies with renamed identifiers…)? How do you decide whether a contract counts as leaked? |
| Frequency | How often does X occur?[^easterbrook2008selecting-e46] | In commonly used benchmarks, what share of contracts are leaked? |
| Comparison | How does X differ from Y?[^easterbrook2008selecting-e47] | How different is the detection rate on leaked versus non-leaked contracts? |
| Relationship | Are X and Y related?[^easterbrook2008selecting-e35] | The more often a contract appears online, the more likely the model is to get it right? |
| Causality | Does X cause Y?[^easterbrook2008selecting-e37] | Is leakage what makes the detection rate look high? |
| Design | What's an effective way to achieve X?[^easterbrook2008selecting-e39] | How do you build a benchmark that doesn't leak? |
| Evaluation | How can I evaluate X? How do I choose between X and Y?[^shaw2003writing-e25] | How do you fairly compare the vulnerability-detection ability of several large language models? |

**How to do it** `[Our analysis]`:

1. **Pick an object.** Choose something concrete in your research area: a class of tools, a phenomenon, an evaluation practice.
2. **Fill in the table row by row.** Write one question per type. Skip the ones you can't fill; don't force it.
3. **For each question, check whether the literature already has a good answer.** Some of these questions already have good answers in the published literature; then a literature survey, not your own study, can answer them[^easterbrook2008selecting-e41].
4. **Keep the rows no one has answered well**, and add them to your list of ideas.

**Why work from the top down.** Early in a research program you usually need to ask exploratory questions first, like "does it exist?" and "what is it like?"[^easterbrook2008selecting-e45]. If you skip the base-rate question ("how often?"), you have no basis for saying whether a situation is normal or unusual[^easterbrook2008selecting-e34]. Design questions ("how do we do it better?") presuppose that the knowledge questions before them have been answered[^easterbrook2008selecting-e48]. So if no one has seriously answered "does leakage exist?" and "how common is it?", jumping straight to "how do we build a leak-free benchmark?" is premature `[Our analysis]`. Also, correlation is not causation, and demonstrating causality is usually much harder[^easterbrook2008selecting-e36], so write the "relationship" and "causality" rows separately.

Once you have filled in the table, you will find that the top rows (does it exist, how common is it, how big is the difference) haven't been answered well. Put together, they make "Are the reported results inflated by leakage, and by how much?", a Measurement problem; see [Key concepts](../00_start-here/key-concepts.md#research-strategy) `[Our analysis]`.

**When to use it, and what it produces** `[Our analysis]`: it works best when you have a concrete object but don't know what to ask about it. It produces a ladder of questions and also shows you the order: which must be answered first, and which has to wait for the ones before it.

**Write it down:** Pick one object in your research area, write one question per type in the table above, and mark which ones the literature already answers.

## 5. Method 4: turn a topic into a question

**What it is.** Many people get stuck with a topic but no question. A writing guide adapted from Booth et al.'s *The Craft of Research* breaks articulating a research project into three smaller steps[^booth2016craft-e1], each with a sentence template:

1. **Name your topic:** "I am studying ______."[^booth2016craft-e2]
2. **Add an indirect question that says what you don't know:** "because I want to find out who / what / whether / why / how ______."[^booth2016craft-e3]
3. **Motivate the question:** "in order to help my reader better understand ______." This step tells you whether your question might interest not just you but others[^booth2016craft-e4].

Together the three steps say what you are writing about, what you don't know about it, and why your reader should care[^booth2016craft-e7]. The guide's example: I am working on Lincoln's beliefs about predestination, because I want to find out how his belief in destiny and God's will influenced his understanding of the causes of the Civil War, in order to help my reader understand how his religious beliefs may have influenced his military decisions[^booth2016craft-e5].

**Filling it in for our example** `[Our analysis]`:

- First draft: "I am studying large language models for smart contract vulnerability detection, because I want to find out how well they work, in order to help my reader…" and you get stuck. Step 2 is too broad, and step 3 won't come.
- Second draft: "I am studying how large-language-model vulnerability detectors are evaluated, because I want to find out whether the contracts in existing benchmarks were already in the models' training data and how much that inflates the detection rate, in order to help my reader judge how far published detection results can still be trusted."

Step 2 of the second draft is exactly the candidate problem the earlier methods produced; step 3 says who will care.

**If you can't write step 3.** If you can't write it, you haven't yet worked out why the question matters. That is common: motivating the question is the hardest of the three steps, and you may not have a conclusive answer until you have finished a first draft[^booth2016craft-e10]. So don't throw the idea away; mark it "significance unclear" on your list and keep thinking `[Our analysis]`. The topic also needs to be specific enough that you can find and read the relevant material in the time you have[^booth2016craft-e8]. The guide also suggests regularly asking a roommate, relative, or friend to make you flesh out all three steps, so you at least know where you are and what is still missing[^booth2016craft-e6].

**Three more questions while you are at it.** The US Defense Advanced Research Projects Agency (DARPA) uses an eight-question list, the Heilmeier Catechism, to assess every proposed research program[^darpaheilmeier-e1][^darpaheilmeier-e2]. It is mainly for assessment, but the first few questions already help at the generation stage: What are you trying to do, articulated with absolutely no jargon[^darpaheilmeier-e3]? How is it done today, and what are the limits of current practice[^darpaheilmeier-e4]? Who cares, and if you are successful, what difference will it make[^darpaheilmeier-e5]? Whatever you can't answer, note it on your list of ideas. Save the serious assessment for [Converging on a project](05_converge.md): [Is it worth doing?](05_converge.md#2-is-it-worth-doing), [Has someone already done it?](05_converge.md#3-has-someone-already-done-it), [What will make people believe it?](05_converge.md#4-what-will-make-people-believe-it), and [Can you actually do it?](05_converge.md#5-can-you-actually-do-it)

**When to use it, and what it produces** `[Our analysis]`: use it when you only have a topic, or when your ideas are too scattered. It rarely produces new ideas, but it turns a vague idea into one complete question and shows which step you haven't thought through. You can run every entry from the first three methods through it.

**Write it down:** For the two or three entries on your list you most want to work on, write one three-part sentence each. Mark any where you can't write step 3 as "significance unclear".

## 6. Other sources

Besides the four methods above, problems often turn up in the places below. They are more about where to look, and you can combine them with any of the four methods `[Our analysis]`.

### Where things don't work well in practice

A method that works in a paper doesn't necessarily work in practice. **Look at where existing methods or systems do badly**[^eisnerproblems-e5].

- **Stress-test the state of the art.** Put it on more diverse, less constrained examples and see how it fails. This is a good way to find the limitations of existing work[^huang2021ideas-e4].
- **Leave the lab setting.** Take computer security as an example: a paper summarizing the pitfalls of using machine learning in security research lists "lab-only evaluation" as one of them, and recommends evaluating in a real-world setting whenever possible[^arp2022dos-e2]. "What happens in a real-world setting?" can itself be a question no one has answered yet `[Our analysis]`.
- **Look at the data.** In many fields, the data itself suggests problems[^eisnerproblems-e6]. Going through real contracts and real vulnerability reports by hand often shows you cases the papers never mention `[Our analysis]`.
- **Find the bottlenecks holding everyone back.** Which problems, whether widely recognized or not, are blocking progress in this field? Can you solve them? If not, can you at least explain them clearly[^eisnerproblems-e3]?

### Bring in ideas from elsewhere

- **Watch for new tools.** When a new tool appears in a field, try it on your own problem[^huang2021ideas-e3]. The research area "large language models and smart contract security" is itself a new tool brought to an old problem `[Our analysis]`.
- **Look for similar problems.** If you notice that your problem resembles one in another field, read the literature on that problem and ask experts in that field[^taocareer-e21]. For example, vulnerability detection for ordinary software has many years of work behind it; which of its techniques haven't yet been applied to smart contracts `[Our analysis]`?
- **Ask people in another discipline.** If your research area is interdisciplinary, ask people in the other discipline what they find interesting[^eisnerproblems-e5].
- **Look one step ahead.** Instead of only watching what everyone is doing now, anticipate which big problems will appear once new technologies arrive[^huang2023decide-e3].

Before you bring something over, be able to say where the two fields differ and why that difference makes the transfer challenging. Just "applying A to B" is easily seen as lacking novelty `[Our analysis]`.

### Talk to people

Some problems aren't in papers; they're in people's heads. Your advisor will point you to open problems and folklore that circulates in the field but isn't written down[^taocareer-e23]; people who work with the door closed may, years later, not know what problems are worth working on[^hamming1986you-e18]. For how to find people to talk to, see [Talk to people who know the area](01_enter-a-field.md#8-talk-to-people-who-know-the-area) in the last chapter.

- **Don't be afraid to work on someone else's suggestion.** Ideas are plentiful; the skill lies in which one you pick and how well you execute it[^schulman2020opinionated-e4].
- **Ask users and practitioners.** In the smart contract area, that means developers who write contracts and people who do audits `[Our analysis]`.
- **Ask about problems "everyone knows are important but no one has seriously worked on".** If you think you have found one, ask colleagues and check the literature to confirm no one has done it[^eisnerproblems-e4].
- **Bring something concrete.** Don't just ask "what do you think I should work on?" Bring your list of ideas and ask "which of these do you find interesting, and which have already been done?" `[Our analysis]`

**Write it down:** Pick a method "widely accepted as effective" and write down how you plan to find where it falls short in practice; name two techniques from a neighboring field that haven't yet been used in your research area; list three people you could talk to (at least one outside your research group) and the specific questions you will ask them.

## 7. Keep a list of ideas

**Everything you generated in the sections above goes into one list.** Ideas you don't write down are soon forgotten; once they're written down, you can compare them, revise them, and come back to them later.

**Why keep them instead of throwing them away once used.** Most great scientists carry 10 to 20 important problems in their heads, always looking for a way to attack them; when they see a new idea, they immediately recognize which problem it bears on[^hamming1986you-e10]. An idea that keeps coming back to you over months or even years is a good sign that you are genuinely interested in it[^alon2009choose-e13], and you can only see that if you write it down and look again later `[Our analysis]`. Keep even your embarrassingly wrong ideas privately; you may be able to salvage something useful from them later[^taocareer-e19].

**How to keep it:**

- Keep it in one fixed place, and jot down ideas every day[^schulman2020opinionated-e16];
- Every week or two, read through it and write up a short summary[^schulman2020opinionated-e17];
- For each entry, write at least the following `[Our analysis]`:

| Field | What to write | Example |
|---|---|---|
| One sentence | What is wrong or unknown | The high accuracy of existing large-language-model vulnerability detection may come partly from benchmark leakage |
| Three-part sentence | I am studying… because I want to find out… in order to help my reader understand… (Section 5) | See the second draft in Section 5; if you can't write step 3, mark it "significance unclear" |
| Source | Which method produced it (Sections 2–6) | Section 3: questioning the assumption that "the model hasn't seen the benchmark"; Sections 2 and 4 point to it too |
| Trigger | Which paper, conversation, or data | A paper whose benchmark comes from a public contract repository |
| Quickest test | A small test you can do in a week or two | Sample 50 benchmark items and check whether they have appeared publicly |
| Date and status | New / thinking about it / dropped (give the reason) | Dropped: already published by group X, see paper Y |

**How long should the list be?** Our sources do not give a single number. As a reference point `[Our analysis]`: before you move on to [Judging and screening ideas](04_judge-and-screen.md), collect about ten entries from at least three different methods or sources. If they all come from the same one (for example, all of them are "some paper on a different dataset"), you haven't searched widely enough. An idea that two or three methods produce independently is a good sign; record all of them in the "Source" field.

**Write it down:** Set up your list of ideas, put in every idea that came up in the earlier "Write it down" exercises, and fill in every field of the table for each.

## 8. Next: try things out, then screen

Once the list is long enough, pick the few entries you most want to pursue and try them out hands-on; see [Exploring hands-on](03_explore.md). Then quickly screen the list down to two to four; see [Judging and screening ideas](04_judge-and-screen.md).

---

## Judgment calls

**Which method first?** One way to choose `[Our analysis]`:

| Where you are now | Start with |
|---|---|
| You have read a batch of papers and your problem log has plenty of questions | Method 1: gap-spotting |
| You keep feeling "everyone does it this way, but something seems off" | Method 2: questioning assumptions |
| You have a concrete object but don't know what to ask | Method 3: work through the question types |
| You have only a topic, or your ideas are too scattered to state | Method 4: turn a topic into a question |
| You can't get into the papers and your ideas are all vague | Section 6: look at the data, at where things don't work in practice, and talk to people |

**When should you stop generating?** Here's one way to decide `[Our analysis]`:

| Situation | What to do |
|---|---|
| Fewer than five entries, or all from the same method | Keep going with a method you haven't tried yet |
| About ten entries from three or more methods or sources | Take a few into [Exploring hands-on](03_explore.md), then move on to [Judging and screening ideas](04_judge-and-screen.md) |
| The time you gave yourself is up and you still can't decide | Take the list to your advisor and go through it together |

**Should you keep an idea that isn't "big" enough?** While generating, don't worry much about size. Many small problems later get rewritten, merged, or scaled up; restating a problem slightly can often turn good work into great work[^hamming1986you-e13]. But be wary of ideas that can "only push some metric up a little"; their ceiling is low from the start[^schulman2020opinionated-e10]. For how to screen, see [Judging and screening ideas](04_judge-and-screen.md).

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Grabbing the first problem that comes to mind | A project takes years, and a hasty choice leads to a lot of frustration[^alon2009choose-e8] |
| Reading endlessly without writing down ideas or trying anything | You are bound to start before you fully understand; judgment depends on practice[^eisnerproblems-e8][^olah2021taste-e9] |
| Only ever gap-spotting | The ideas all look alike and you easily get scooped[^schulman2020opinionated-e7]; without questioning assumptions you rarely get new high-ranking theories (an observation about management research)[^alvesson2013has-e5] |
| Criticizing others from your own favorite theory and calling it questioning assumptions | That is pseudo-problematization, which only reproduces that theory's assumptions[^alvesson2013has-e9] |
| Only looking for faults when reading papers, questioning for its own sake | You miss the good ideas in a paper that could be used elsewhere[^eisnerread-e6]; problematization should also point out high-quality studies[^alvesson2020problematizing-e10] |
| Starting with "how do we do it better?" | Design questions presuppose that the knowledge questions before them have been answered[^easterbrook2008selecting-e48] |
| Treating the problem as worked out when you can't write "in order to help my reader understand…" | Step 3 tells you whether the question might interest not just you but others[^booth2016craft-e4] |
| Keeping ideas only in your head | You forget them, and can't compare them or come back to them `[Our analysis]` |
| Not talking to people | You miss open problems and existing work that people in the field know about but that aren't in papers yet[^taocareer-e23][^eisnerproblems-e9] |

## What you should have at the end

- A list of about ten ideas from at least three methods or sources, each with every field of the table filled in (Section 7)
- A complete record of at least one method other than gap-spotting: for example, notes on the six problematization steps, or a filled-in question-type table (Sections 3 and 4)
- A three-part sentence for each of your top two or three entries (Section 5)

Screening results are not produced in this chapter; see [Judging and screening ideas](04_judge-and-screen.md).

## Checklist before moving on

You are ready for the next step when:

- [ ] Your list of ideas has about ten entries from at least three different methods or sources
- [ ] You have used at least two of the four methods, and at least one of them was not gap-spotting
- [ ] For each entry you can say in one sentence what is wrong or unknown
- [ ] Your top two or three entries can be stated as three-part sentences, or are marked "significance unclear"
- [ ] You have talked the list over with at least one advisor or other person who knows the area

## When to go back

| If this happens | Go back to |
|---|---|
| Weeks of thinking and you can't write down a single idea | [Entering a field and exploring the literature](01_enter-a-field.md): read another batch, especially papers and surveys from the last year or two |
| For every idea you can't say what is wrong, and you can't find any assumptions in the field | You still know too little about the field; go back to [Entering a field and exploring the literature](01_enter-a-field.md) |
| Everything on your list has already been done by others | Switch methods: question assumptions (Section 3), look where things don't work in practice, or talk to people (Section 6) |
| You have lost interest in the research area itself | Talk to your advisor and consider switching areas; forcing yourself to work on a topic you aren't excited about makes you far less productive[^olah2021taste-e3] |

## Next

Take your list of ideas into [Exploring hands-on](03_explore.md): run small, fast tests on the entries you most want to pursue, so an idea on paper becomes "I roughly know what's going on here". Then, in [Judging and screening ideas](04_judge-and-screen.md), screen it down to two to four and take those into [Converging on a project](05_converge.md).

If at any later step all your candidates fall apart, come back to this chapter and run another round with a different method.

[^alon2009choose-e8]: Alon 2009, Take Your Time. [Evidence](../../sources/notes/alon2009choose.md#e8)
[^alon2009choose-e9]: Alon 2009, Take Your Time. [Evidence](../../sources/notes/alon2009choose.md#e9)
[^alon2009choose-e10]: Alon 2009, Take Your Time. [Evidence](../../sources/notes/alon2009choose.md#e10)
[^alon2009choose-e13]: Alon 2009, The Subjectivity of the Interest Axis. [Evidence](../../sources/notes/alon2009choose.md#e13)
[^alvesson2013has-e1]: Alvesson & Sandberg 2013, Abstract, p. 128. [Evidence](../../sources/notes/alvesson2013has.md#e1)
[^alvesson2013has-e2]: Alvesson & Sandberg 2013, section Gap-Spotting, p. 131. [Evidence](../../sources/notes/alvesson2013has.md#e2)
[^alvesson2013has-e4]: Alvesson & Sandberg 2013, section Gap-Spotting, pp. 131–132. [Evidence](../../sources/notes/alvesson2013has.md#e4)
[^alvesson2013has-e5]: Alvesson & Sandberg 2013, section Gap-Spotting, p. 132. [Evidence](../../sources/notes/alvesson2013has.md#e5)
[^alvesson2013has-e6]: Alvesson & Sandberg 2013, What Makes a Theory Interesting and Influential?, p. 131. [Evidence](../../sources/notes/alvesson2013has.md#e6)
[^alvesson2013has-e7]: Alvesson & Sandberg 2013, section Gap-Spotting, p. 131. [Evidence](../../sources/notes/alvesson2013has.md#e7)
[^alvesson2013has-e8]: Alvesson & Sandberg 2013, A Need to Consider Alternative Methodologies for Theory Development, pp. 144–145. [Evidence](../../sources/notes/alvesson2013has.md#e8)
[^alvesson2013has-e9]: Alvesson & Sandberg 2013, A Need to Consider Alternative Methodologies for Theory Development, p. 145. [Evidence](../../sources/notes/alvesson2013has.md#e9)
[^alvesson2013has-e11]: Alvesson & Sandberg 2013, A Need to Consider Alternative Methodologies for Theory Development, p. 145. [Evidence](../../sources/notes/alvesson2013has.md#e11)
[^alvesson2013has-e12]: Alvesson & Sandberg 2013, A Need to Consider Alternative Methodologies for Theory Development, p. 144. [Evidence](../../sources/notes/alvesson2013has.md#e12)
[^alvesson2013has-e13]: Alvesson & Sandberg 2013, A Need to Consider Alternative Methodologies for Theory Development, p. 146. [Evidence](../../sources/notes/alvesson2013has.md#e13)
[^alvesson2013has-e14]: Alvesson & Sandberg 2013, note 3. [Evidence](../../sources/notes/alvesson2013has.md#e14)
[^alvesson2020problematizing-e3]: Alvesson & Sandberg 2020, The ideal of reflexivity. [Evidence](../../sources/notes/alvesson2020problematizing.md#e3)
[^alvesson2020problematizing-e4]: Alvesson & Sandberg 2020, Not accumulating but problematizing. [Evidence](../../sources/notes/alvesson2020problematizing.md#e4)
[^alvesson2020problematizing-e5]: Alvesson & Sandberg 2020, Not accumulating but problematizing. [Evidence](../../sources/notes/alvesson2020problematizing.md#e5)
[^alvesson2020problematizing-e6]: Alvesson & Sandberg 2020, Not accumulating but problematizing. [Evidence](../../sources/notes/alvesson2020problematizing.md#e6)
[^alvesson2020problematizing-e7]: Alvesson & Sandberg 2020, Not accumulating but problematizing. [Evidence](../../sources/notes/alvesson2020problematizing.md#e7)
[^alvesson2020problematizing-e8]: Alvesson & Sandberg 2020, Final Remarks. [Evidence](../../sources/notes/alvesson2020problematizing.md#e8)
[^alvesson2020problematizing-e10]: Alvesson & Sandberg 2020, Less is more. [Evidence](../../sources/notes/alvesson2020problematizing.md#e10)
[^arp2022dos-e2]: Arp et al. 2022, §2, P9 Lab-Only Evaluation. [Evidence](../../sources/notes/arp2022dos.md#e2)
[^arp2022dos-e3]: Arp et al. 2022, Abstract. [Evidence](../../sources/notes/arp2022dos.md#e3)
[^arp2022dos-e5]: Arp et al. 2022, §2, P3 Data Snooping. [Evidence](../../sources/notes/arp2022dos.md#e5)
[^booth2016craft-e1]: Brandeis University writing handout adapted from Booth et al., The Craft of Research, opening paragraph. [Evidence](../../sources/notes/booth2016craft.md#e1)
[^booth2016craft-e2]: Brandeis University writing handout adapted from Booth et al., Step 1. [Evidence](../../sources/notes/booth2016craft.md#e2)
[^booth2016craft-e3]: Brandeis University writing handout adapted from Booth et al., Step 2. [Evidence](../../sources/notes/booth2016craft.md#e3)
[^booth2016craft-e4]: Brandeis University writing handout adapted from Booth et al., Step 3. [Evidence](../../sources/notes/booth2016craft.md#e4)
[^booth2016craft-e5]: Brandeis University writing handout adapted from Booth et al., example in Step 3. [Evidence](../../sources/notes/booth2016craft.md#e5)
[^booth2016craft-e6]: Brandeis University writing handout adapted from Booth et al., after Step 3. [Evidence](../../sources/notes/booth2016craft.md#e6)
[^booth2016craft-e7]: Brandeis University writing handout adapted from Booth et al., To summarize. [Evidence](../../sources/notes/booth2016craft.md#e7)
[^booth2016craft-e8]: Penn State University Libraries page adapted from Booth et al., Name Your Topic. [Evidence](../../sources/notes/booth2016craft.md#e8)
[^booth2016craft-e10]: Penn State University Libraries page adapted from Booth et al., Motivate Your Question. [Evidence](../../sources/notes/booth2016craft.md#e10)
[^carlini2026best-e7]: Carlini 2026, Ignore all the papers. [Evidence](../../sources/notes/carlini2026best.md#e7)
[^carlini2026best-e9]: Carlini 2026, Do something only you can do. [Evidence](../../sources/notes/carlini2026best.md#e9)
[^carlini2026best-e13]: Carlini 2026, Pick your ideas for impact. [Evidence](../../sources/notes/carlini2026best.md#e13)
[^darpaheilmeier-e1]: DARPA, Heilmeier Catechism, What is the Heilmeier Catechism? [Evidence](../../sources/notes/darpaheilmeier.md#e1)
[^darpaheilmeier-e2]: DARPA, Heilmeier Catechism, What is the Heilmeier Catechism? [Evidence](../../sources/notes/darpaheilmeier.md#e2)
[^darpaheilmeier-e3]: DARPA, Heilmeier Catechism, question 1. [Evidence](../../sources/notes/darpaheilmeier.md#e3)
[^darpaheilmeier-e4]: DARPA, Heilmeier Catechism, questions 2 and 3. [Evidence](../../sources/notes/darpaheilmeier.md#e4)
[^darpaheilmeier-e5]: DARPA, Heilmeier Catechism, question 4. [Evidence](../../sources/notes/darpaheilmeier.md#e5)
[^easterbrook2008selecting-e34]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e34)
[^easterbrook2008selecting-e35]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e36]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e37]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e37)
[^easterbrook2008selecting-e38]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e38)
[^easterbrook2008selecting-e39]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e39)
[^easterbrook2008selecting-e41]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e41)
[^easterbrook2008selecting-e44]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e44)
[^easterbrook2008selecting-e45]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e45)
[^easterbrook2008selecting-e46]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e46)
[^easterbrook2008selecting-e47]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e47)
[^easterbrook2008selecting-e48]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e48)
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
[^hamming1986you-e10]: Hamming 1986, after "Great Thoughts Time". [Evidence](../../sources/notes/hamming1986you.md#e10)
[^hamming1986you-e13]: Hamming 1986, paragraph on solving a problem as a class of problems. [Evidence](../../sources/notes/hamming1986you.md#e13)
[^hamming1986you-e18]: Hamming 1986, "door open or the door closed" paragraph. [Evidence](../../sources/notes/hamming1986you.md#e18)
[^huang2021ideas-e1]: Huang 2021, Relax assumptions. [Evidence](../../sources/notes/huang2021ideas.md#e1)
[^huang2021ideas-e2]: Huang 2021, Make more assumptions. [Evidence](../../sources/notes/huang2021ideas.md#e2)
[^huang2021ideas-e3]: Huang 2021, Grab a powerful hammer and find all the nails. [Evidence](../../sources/notes/huang2021ideas.md#e3)
[^huang2021ideas-e4]: Huang 2021, Stress test the state-of-the-art. [Evidence](../../sources/notes/huang2021ideas.md#e4)
[^huang2023decide-e3]: Huang 2023, Anticipate disruptive technologies. [Evidence](../../sources/notes/huang2023decide.md#e3)
[^klees2018evaluating-e2]: Klees et al. 2018, Abstract. [Evidence](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e3]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e7]: Klees et al. 2018, §8. [Evidence](../../sources/notes/klees2018evaluating.md#e7)
[^olah2021taste-e3]: Olah 2021, opening section. [Evidence](../../sources/notes/olah2021taste.md#e3)
[^olah2021taste-e9]: Olah 2021, Failure mode 2. [Evidence](../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e12]: Olah 2021, Andy Matuschak's advice collected at the end. [Evidence](../../sources/notes/olah2021taste.md#e12)
[^schulman2020opinionated-e4]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e6]: Schulman 2020, Idea-Driven vs Goal-Driven Research. [Evidence](../../sources/notes/schulman2020opinionated.md#e6)
[^schulman2020opinionated-e7]: Schulman 2020, Idea-Driven vs Goal-Driven Research. [Evidence](../../sources/notes/schulman2020opinionated.md#e7)
[^schulman2020opinionated-e8]: Schulman 2020, Idea-Driven vs Goal-Driven Research. [Evidence](../../sources/notes/schulman2020opinionated.md#e8)
[^schulman2020opinionated-e10]: Schulman 2020, Aim High, and Climb Incrementally Towards High Goals. [Evidence](../../sources/notes/schulman2020opinionated.md#e10)
[^schulman2020opinionated-e16]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e16)
[^schulman2020opinionated-e17]: Schulman 2020, Keep a Notebook, and Review It. [Evidence](../../sources/notes/schulman2020opinionated.md#e17)
[^shaw2003writing-e25]: Shaw 2003, §2.1, Table 1. [Evidence](../../sources/notes/shaw2003writing.md#e25)
[^taocareer-e8]: Tao, Career advice, Ask yourself dumb questions – and answer them! [Evidence](../../sources/notes/taocareer.md#e8)
[^taocareer-e19]: Tao, Career advice, Use the wastebasket. [Evidence](../../sources/notes/taocareer.md#e19)
[^taocareer-e21]: Tao, Career advice, Be sceptical of your own work. [Evidence](../../sources/notes/taocareer.md#e21)
[^taocareer-e23]: Tao, Career advice, Talk to your advisor. [Evidence](../../sources/notes/taocareer.md#e23)
