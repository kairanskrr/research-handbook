# Reviews, revision, and what to do after rejection

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. Review processes differ a lot between journals and conferences (whether there is an author response phase, word limits, whether you may add experiments). **Before you do anything, read the reviewing instructions of the venue you submitted to.**

> **What you must do in this chapter** `[Our analysis]`
>
> 1. **Read everything calmly first, and work out what you're facing.** Write down what kind of decision it is, the deadline and word limit, and who makes the final call ([Section 1](#1-read-everything-calmly-first-and-work-out-what-you-are-facing)).
> 2. **Break the reviews into individual points and sort them.** Put them in a table and flag the issues several reviewers raised, so you deal with those first ([Section 2](#2-break-the-reviews-into-individual-points-and-sort-them)).
> 3. **Decide what to do about every point.** Change it, explain, disagree, or say it can't be done; where you disagree, bring data or facts ([Section 3](#3-decide-what-to-change-and-what-to-argue)).
> 4. **In your reply, quote each question before answering it directly.** Put the issues shared across reviewers first; someone who reads only your reply should be able to tell whether each issue has been resolved ([Section 4](#4-writing-an-author-response-for-a-conference), [Section 5](#5-writing-a-journal-revision-and-response-letter)).
> 5. **After a rejection, work out at what level the problem lies before deciding where to go next.** Before resubmitting, make sure the previous venue's process is over and every necessary change has been made ([Section 6](#6-after-a-rejection-reassess-first-then-decide-where-to-go)).
>
> **Done these? Move on:** every point is in the table with a decision, and for every issue that shakes the claim, you have either added evidence or changed the claim. Next: the paper is accepted, or you decide to let this one go; start your next project again from [Generating candidate problems](../01_find-a-problem/02_generate-problems.md).

## Where you are

Your paper is out, and the reviews have come back. You are probably in one of these situations:

- The conference has an **author response** period (also called a rebuttal: a written reply to the reviews before the decision is made), and you need to write one;
- The journal has asked for a **revision**, and you need to revise the paper and attach a **response letter** that goes through the comments point by point;
- The paper was **rejected**, and you are wondering: where should I submit it after revising? Or is the project itself the problem?

Whichever it is, the first time you read the reviews you may feel that some reviewers didn't read carefully and some comments are unfair, and it can be upsetting.

## What this stage is for

Turn the reviews into next steps. Concretely, answer these five questions:

1. What are the reviewers actually saying? Which points are critical, and which are minor?
2. What should you change, what should you explain, and where can you disagree with good reason?
3. How do you write a response that the people making the decision can follow?
4. After a rejection, is the problem the paper, the project, or the choice of venue?
5. Where do you submit next, or which chapter do you go back to and redo?

Being a reviewer yourself and writing reviews of other people's papers is a different task; see [Being a reviewer](../08_throughout/being_a_reviewer.md).

---

## 1. Read everything calmly first, and work out what you are facing

**On the first day, only read. Don't reply, don't revise.** Being upset is normal; take a day off and come back[^huang2021rejection-e6]. For how to manage the emotions and treat rejection as normal, see [Mindset and long-term growth](../08_throughout/mindset_and_growth.md#2-treat-failure-and-rejection-as-normal).

**Once you've calmed down, read objectively.** When a paper is rejected or needs a major revision, listen carefully to what the reviewers say, and respond objectively rather than emotionally[^bourne2005published-e1]. Then work out three things `[Our analysis]`:

| What to find out | Where to look |
|---|---|
| What kind of decision is this: waiting for your response, asking for a revision, or a rejection? | The decision letter, the status in the submission system |
| How much time and space do you have? Can you submit a revised paper or add experiments? | The conference's or journal's reviewing instructions |
| Who makes the final call? | At a conference, usually the program committee (the conference's reviewing committee) or its area chairs (the people who consolidate the reviews and make an acceptance recommendation); at a journal, usually the editor |

The rules differ from venue to venue and can change every year, so don't go by memory. Below are the rules of two computer science conferences in one particular year, just to show how much they differ:

- The machine learning conference NeurIPS 2025 (the Conference on Neural Information Processing Systems): authors have one week to respond to the initial reviews[^neurips2025cfp-e8], and may not submit a revised paper or supplementary material during the response period[^neurips2025cfp-e11];
- The security conference USENIX Security '26 (the 2026 edition): "major revision" no longer exists as an outcome; papers go through at most a two-week shepherding process[^usenixsec2026cfp-e14].

For the venue you submitted to, go by that year's call for papers.

**Also know who will read your response.** Several computer science researchers have shared experience worth considering: when reviewers read your response, it may be a month after they wrote their reviews, and they no longer remember the details[^hicks2014response-e7]; the area chair who makes the decision knows your paper even less well, so it is best to assume they read only the reviews and your response[^parikh2020rebuttals-e2]. Some conferences also make responses public: after decisions are announced, NeurIPS 2025 publishes accepted papers, and rejected papers whose authors opt in, together with the reviews and author responses[^neurips2025cfp-e13]. So write the response so that it reads fine to anyone `[Our analysis]`.

**Write it down:** In three lines, write: what kind of decision this is, the deadline and word limit, and who makes the final call. Then one sentence: if you had to sum up the reviewers' overall view in one sentence, what would it be?

## 2. Break the reviews into individual points and sort them

**First, split all the reviews into individual points and put them in one table.** The following comes from computer science researchers' experience writing responses; treat it as advice. List every comment, question, and concern from every reviewer, one per item, and look at them side by side: that makes it easy to spot issues several reviewers share, and you won't miss any[^parikh2020rebuttals-e5][^parikh2020rebuttals-e17]. Number the reviewers and the questions, for example R1 and R2 for the first and second reviewer, and R1Q1 and R1Q2 for the first reviewer's first and second questions, so each reviewer can find their own questions and your answers[^zeller2012rebuttals-e10]. **Do this as soon as the reviews arrive**, so you find out early which experiments or analyses you need to add[^parikh2020rebuttals-e17].

**Then classify each point.** The categories below are one way we suggest doing it `[Our analysis]`:

| Type | How to recognize it | Usual way to handle it |
|---|---|---|
| Misunderstanding | The reviewer says "there is no X", but the paper has it; or the reviewer got your method wrong | Point to the section and restate it in the response; also ask why it was misunderstood, and rewrite that passage |
| Factual error | What the reviewer says about prior work or data is wrong | Correct it with facts and data, in a calm tone |
| Reasonable request you can meet | Add a baseline, a set of experiments, a discussion | Do it, and give the results or the new text in the response |
| Reasonable request you can't meet | The experiment needs data or compute you can't get, or the conference doesn't allow new experiments | Say so honestly, and explain how it affects the conclusions |
| A point that shakes the claim | It questions whether the evidence supports your central claim | Highest priority; you may need to change how the conclusion is stated; see Section 3 |
| Difference in preference | The reviewer wants a different method or design | Explain why you chose yours; if you have capacity, try their suggestion |
| Minor issue | Typos, figure or table formatting, wording | Just fix it; one sentence in the response |

Try it on the "large language models and smart contract security" example (a made-up example `[Our analysis]`). Suppose your paper claims that "the new method finds 30% more vulnerabilities than existing tools on real-world contracts", and three reviewers raised these points:

| ID | Comment | Category |
|---|---|---|
| R1Q1 | "The test contracts may appear in the model's training data" | Shakes the claim |
| R2Q1 | "Why no comparison with tool X?" | Reasonable request, possibly doable |
| R2Q2 | "The paper doesn't make clear what counts as finding a vulnerability" | Misunderstanding, or it really wasn't clear |
| R3Q1 | "You should use formal verification rather than a large language model" | Difference in preference |
| R3Q2 | Typo on page 4 | Minor issue |

**Finally, set priorities.** A suggested order: major issues shared by several reviewers first[^hicks2014response-e5]; next, issues the reviewers think you may not be able to fix[^zeller2012rebuttals-e14]; things proofreading can fix, such as typos and language, aren't worth arguing in the response[^zeller2012rebuttals-e5].

Points that undermine the trustworthiness of your conclusions go to the very top `[Our analysis]`. The reason is reflected in the reviewing standard for empirical research in software engineering: it asks reviewers to judge first whether the results are trustworthy, and only then whether they are important; a trustworthy but less important paper can be accepted, while a paper that isn't trustworthy cannot be accepted no matter how important it seems[^ralph2020empirical-e53].

**Write it down:** Turn the reviews you received into a table like the one above: ID, summary of the comment, category, priority. Mark the issues raised by at least two reviewers.

## 3. Decide what to change and what to argue

Once the table is done, make a decision for each point: **change it, explain it, or disagree with good reason.** The rules of thumb below are our synthesis of several computer science researchers' experience `[Our analysis]`:

- **Default to changing.** Rather than arguing why a reviewer's suggestion won't work, try it; it may actually help[^parikh2020rebuttals-e20]. Even the most unpromising review contains something useful to you[^zeller2012rebuttals-e7].
- **If you were misunderstood, blame your writing first.** If one reviewer misunderstood, you can point out what the paper says; if all the reviewers misunderstood, the problem is not the reviewers[^zeller2012rebuttals-e6], and you need to rewrite; see [Telling the story and writing the paper](01_story-and-paper.md).
- **When you disagree, let the data talk.** Rather than arguing with the reviewer, give data that supports your position[^parikh2020rebuttals-e9].
- **Address the concern behind the comment.** Don't just answer the literal question; respond to the intent behind it too[^parikh2020rebuttals-e18]. For example, "why didn't you test on dataset Y?" may hide a doubt about whether the experiments as a whole are sufficient; answer the question, then remind everyone which datasets you have already tested on.

**Which criticisms can you disagree with, with good reason?** Some criticisms don't hold up in the first place. The reviewing standard for empirical research in software engineering lists a number of them, for example:

- Saying "not novel" without citing published work with nearly identical contributions[^ralph2020empirical-e60];
- Saying "lacks detail" without saying which details are missing[^ralph2020empirical-e61];
- Rejecting a paper because the results are negative[^ralph2020empirical-e41], or because it is a replication study[^ralph2020empirical-e62];
- Rejecting a paper because the reviewer would have used a different method or design, or criticizing it for limitations inherent to that kind of study[^ralph2020empirical-e25];
- Asking for additional analyses unrelated to the study's aims (the standard lists this as a reviewing antipattern)[^ralph2020empirical-e64].

When you meet comments like these, politely ask the reviewer to be specific, or explain why the criticism doesn't apply; don't hit back. In other fields with no such written list, you can borrow the same reasoning, but word it more cautiously `[Our analysis]`.

**For points that shake the claim, think hard: is the evidence insufficient, or is the claim overstated?** Take the claim apart: sweeping statements such as "always" or "completely" often need analytical argument, while qualified statements ("a 25% improvement", "for a certain class of structures") can often be supported by evaluation[^shaw2003writing-e16]. With R1Q1 above, you have two routes `[Our analysis]`:

- **Add evidence**: find out how many test contracts may appear in the training data, remove them, and rerun the comparison;
- **Change the claim**: change "finds 30% more vulnerabilities on real-world contracts" to "on contracts deployed after the model's training cutoff …".

There is no shame in changing the claim. In one researcher's experience supervising graduate students, a frequent result of discussing claims and evidence is that students restate their claims to reflect more precisely what the research actually achieved[^shaw2003writing-e17]. But if, after the change, what is left isn't worth publishing, revision won't fix it; see Section 6 `[Our analysis]`.

**Write it down:** Add a "decision" column to the table: change / explain / disagree (with reasons) / can't do (with explanation). For every "disagree", write down the data or facts you can bring.

## 4. Writing an author response for a conference

The author response was originally meant to let authors point out factual errors in the reviews[^hicks2014response-e1]. Not every conference has this phase, and where it exists the rules vary; go by that year's call for papers of your target conference.

The advice in this section comes mainly from personal experience that several computer science researchers shared on their blogs (sources in the footnotes). Treat it as advice, not as rules.

**Set your expectations first.** A response can't save a bad paper; it only matters when the paper is on the borderline of acceptance, or when a reviewer has made an obvious mistake[^zeller2012rebuttals-e8]. If most reviewers lean toward rejection, a response can do very little[^hicks2014response-e10]. The goal is not to convince everyone, but to get at least one reviewer willing to champion your paper[^hicks2014response-e2]. Without such a potential champion, the chance of acceptance is small[^zeller2012rebuttals-e1].

**Think about whom you are writing for.**

- **Undecided reviewers** are the ones most worth winning over[^zeller2012rebuttals-e11];
- **Your champion** needs arguments from you to counter the detractors in the discussion[^zeller2012rebuttals-e2];
- **Strongly opposed reviewers**: rather than trying to change their minds, give your champion arguments[^zeller2012rebuttals-e12];
- **The decision makers**: the test is whether a neutral third party, reading only your response, without rereading the paper or the reviews, could tell whether each issue has been resolved[^parikh2020rebuttals-e4].

**How to write it:**

1. **In the first draft, cover every point; then cut.** Ignore the word limit at first and address everything, then cut by importance until you fit[^parikh2020rebuttals-e6].
2. **Opening**: briefly summarize what the reviewers liked[^parikh2020rebuttals-e13]; put the one thing you most want everyone to know first, because most people only read the beginning[^zeller2012rebuttals-e3].
3. **Order**: answer the big questions you are confident about first, then the less clear-cut questions and the minor ones[^parikh2020rebuttals-e7]. Answer related questions from different reviewers together to save space[^parikh2020rebuttals-e19].
4. **For each point, quote it, then answer directly**: briefly quote the reviewer's question, give the answer in the first sentence, then elaborate[^parikh2020rebuttals-e8].
5. **If the paper already covers it, say where**[^hicks2014response-e8][^parikh2020rebuttals-e12].
6. **Don't just promise; write it out.** Rather than saying "we will discuss work X in the paper", write the discussion in the response[^parikh2020rebuttals-e10]; at the very least, sketch concretely how you will change the paper[^zeller2012rebuttals-e4].
7. **Be honest about what you can't do**, for example when the conference doesn't allow new experiments[^parikh2020rebuttals-e21].

Back to the example, one way to answer R2Q1 `[Our analysis]`:

> **R2Q1: Why no comparison with tool X?**
> We have added the comparison: on the same 500 contracts, tool X finds 41 vulnerabilities and our method finds 58 (detailed results in the table below). The original submission had no comparison because tool X only supported an old compiler version at the time; we have switched to its new version, and the revised paper will include these results.

(The numbers are for illustration only.)

**Tone.** Be polite and thankful: reviewers volunteer their time to give you feedback[^hicks2014response-e3]; thank especially the reviewers who were particularly careful and constructive[^parikh2020rebuttals-e22]. Arguing can make reviewers more firmly opposed; finding the points where you agree works better[^parikh2020rebuttals-e14]. If a review is clearly irresponsible, you can point it out[^parikh2020rebuttals-e15]; but state only facts the program committee chair can verify within a minute[^zeller2012rebuttals-e13].

> **Where sources disagree: should you respond to every comment?**
> - No: the goal of the response is to win a champion, so you shouldn't feel obliged to respond to every point[^hicks2014response-e4].
> - Yes: rebut every point the detractors raise, to give your champion arguments for the discussion[^zeller2012rebuttals-e2].
>
> In practice `[Our analysis]`: under a strict word limit, make sure you cover the major issues and the detractors' key points, deal with the rest in a sentence, and say they will be handled in the revision; with a generous limit, respond to every point.

**Write it down:** Draft a response: an opening paragraph summarizing the strengths and the one thing you most want everyone to know, then answers in the order you set in Section 2. When you're done, ask a labmate who hasn't read the reviews to read only the response, and ask them: which issues have been resolved?

## 5. Writing a journal revision and response letter

When a journal asks for a revision, you submit two things: the revised paper, and a response letter that goes through the comments point by point.

**If you get a major revision, revise seriously, and address every comment in both the response letter and the text**[^bourne2005published-e2]. Unlike a conference response, there is usually no strict word limit here, so you can write each point out in full `[Our analysis]`.

**How to write the response letter** `[Our analysis]`: follow the principles from Section 4 (quote first, answer directly, let the data talk), and under each comment write these five parts:

| Under each comment, write | Example |
|---|---|
| The reviewer's words (a summary is fine) | R1Q1: The test contracts may appear in the training data |
| Your answer, with the conclusion in the first sentence | We agree this is an important issue and have run an additional check |
| What you did | Filtered by deployment date to 300 contracts deployed after the model's training cutoff, and reran the comparison |
| The result | The conclusion holds; the improvement drops from about 30% to just over 20% |
| Where the paper changed | Section 5.2, paragraph 3, and Table 4; changes are highlighted |

(The numbers in the example are for illustration only.)

**When you revise the text, don't do just enough to get past the response letter.** If the letter says "revised", the change should be easy to find in the text `[Our analysis]`. The questions reviewers raise are questions future readers will have too, and your answers in the text are answers for them.

**One change can ripple through the whole paper.** If you narrowed the claim because of R1Q1, the abstract, introduction, and conclusion all have to change with it; don't let the old and new wording appear side by side `[Our analysis]`.

**Write it down:** Using the five-part format above, write your responses to the three most important comments. For each, mark exactly which places in the text you changed.

## 6. After a rejection: reassess first, then decide where to go

**Don't resubmit elsewhere unchanged.** Resubmitting a rejected paper again and again without changing a word will eventually come back to bite you[^karpathy2016survival-e11]. Turn the reviews into a to-do list and work through it in your revision[^huang2021rejection-e2].

**First, judge at what level the problem lies** `[Our analysis]`:

| Main issue in the reviews | Level of the problem | What to do |
|---|---|---|
| Couldn't follow it, misread your contribution | Writing | Rewrite; see [Telling the story and writing the paper](01_story-and-paper.md) |
| Doesn't match the focus of this conference or journal | Venue | After revising, move to a better-fitting venue; see [Choosing a venue and submitting](02_venue-and-submission.md) |
| Missing baselines, missing experiments, holes in the analysis | Evidence | Add them; see [Running and iterating](../02_do-the-project/06_run-and-iterate.md) |
| The evidence can't support the conclusions | Claim | Narrow the conclusions, or use a different kind of evidence; see [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) |
| Done before, or not enough of a contribution | The project itself | Go back to Section 3 of [Converging on a project](../01_find-a-problem/05_converge.md#3-has-someone-already-done-it) and reposition it |

**If the reviewers agree the paper is poor, don't argue; move on**: in almost every such case, the reviewers are right[^bourne2005published-e2]. Then take the last two rows of the table above seriously `[Our analysis]`.

**Revise properly before resubmitting; don't rush.** In the long run most papers don't matter much; a career is defined by a few good papers[^huang2021rejection-e3]. So using this rejection to make the paper solid is worth more than rushing to the next venue `[Our analysis]`. If it doesn't get in this time, there is always another deadline[^zeller2012rebuttals-e9].

**Before resubmitting, make sure the previous venue is done with it.** For the general rules on simultaneous submission, see [Choosing a venue and submitting](02_venue-and-submission.md). This is the one people trip over most around a rejection. Take the USENIX Security '26 call for papers: even if the initial reviews at the previous venue suggest the paper will very likely be rejected, as long as it still counts as under review there, submitting it here counts as a simultaneous submission[^usenixsec2026cfp-e13]. For other venues, go by that year's call for papers of your target conference or journal; if in doubt, formally withdraw the paper first, or wait for the decision `[Our analysis]`.

**A new submission means new reviewers, but possibly the same old problems.** Issues the previous reviewers pointed out will very likely be noticed by the new ones too. So don't fix only the easy things `[Our analysis]`.

**Write it down:** For this rejection, write in one sentence "at what level the problem mainly lies". List the changes you must make before resubmitting, and write down the next target venue and its deadline.

---

## Judgment calls

**Resubmit, overhaul, or let it go?** After a rejection, you can decide like this `[Our analysis]`:

| Situation | Usual approach |
|---|---|
| Scores close to the acceptance line; comments focus on writing and a few experiments | Revise and submit to the next suitable deadline |
| Reviewers accept the problem but not the evidence | Add evidence or narrow the conclusions, then resubmit |
| Reviewers agree the contribution is insufficient or it has been done before | Go back to the converging stage and reconsider whether the project is worth continuing |
| You've resubmitted two or three times and the main issue is the same every time | The problem hasn't really been fixed; reassess the claim with your advisor |
| The comments differ every time, and the scores hover around the line | It may just be luck; keep revising and resubmitting |

**When is a "we disagree" worth including in a response?** When you can bring data or facts, and the comment will affect the decision. Merely feeling it's unfair isn't worth the space `[Our analysis]`.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Writing the response the day the reviews arrive | You're still upset and it easily turns into an argument; take a day off first[^huang2021rejection-e6] |
| Not listing the comments point by point | Easy to miss issues, and you can't see the shared ones[^parikh2020rebuttals-e17] |
| Writing the response only for the reviewers | The decision makers may read only the reviews and the response[^parikh2020rebuttals-e2] |
| Only saying "thank you, we will add it" | Better to write it out in the response[^parikh2020rebuttals-e10] |
| Arguing with reviewers | It can make reviewers more firmly opposed[^parikh2020rebuttals-e14] |
| All reviewers misunderstood, and you blame the reviewers | The problem is in how the paper is written[^zeller2012rebuttals-e6] |
| Resubmitting unchanged after a rejection | It will eventually come back to bite you[^karpathy2016survival-e11] |
| Submitting to the next venue while the previous one is still reviewing | At least at USENIX Security '26, it counts as simultaneous submission[^usenixsec2026cfp-e13] |
| Fixing only the easy things and avoiding the points that shake the claim | The next round of reviewers will very likely raise the same issues `[Our analysis]` |

## What you should have at the end

- A table of review comments: ID, summary, category, priority, decision (Sections 2 and 3)
- An author response, or a journal response letter and revised paper (Sections 4 and 5)
- If rejected: a one-sentence diagnosis, a list of changes to make before resubmitting, and the next target venue (Section 6)

## Checklist before moving on

This round is done when:

- [ ] Every comment is in the table, with a category and a decision
- [ ] Issues shared by several reviewers come first in the response
- [ ] Every answer quotes the question first, then answers directly
- [ ] Someone reading only the response can tell whether each issue has been resolved
- [ ] For points that shake the claim, you either added evidence or changed the claim, and the wording is consistent throughout the paper
- [ ] Before resubmitting, you confirmed the previous venue is done, and everything on the revision list is finished

## When to go back

| If this happens | Go back to |
|---|---|
| None of the reviewers understood your contribution | [Telling the story and writing the paper](01_story-and-paper.md) |
| Reviewers accept the problem but think the evidence can't support the conclusions | [Validity and limitations: think them through at the design stage](../02_do-the-project/04_validity-and-limits.md), or [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) |
| The experiments you had to add exposed an error in the analysis | [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md) |
| Reviewers agree it has been done before, or the contribution is insufficient | Section 3 of [Converging on a project](../01_find-a-problem/05_converge.md#3-has-someone-already-done-it) |
| Several resubmissions, stuck on the same issue every time | Section 1 of [Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove): rethink the statement you want to prove |

## Next

Your paper has been accepted, or you've decided to let this one go: either way, you have come to the end of the road from finding a problem to publishing it.

Rejection, revision, and resubmission are very common in research. For how to stay motivated and build experience over the long term, see [Mindset and long-term growth](../08_throughout/mindset_and_growth.md).

For your next project, start again from [Generating candidate problems](../01_find-a-problem/02_generate-problems.md). The questions reviewers asked most often this round usually tell you where to put more effort in the next project. `[Our analysis]`

[^bourne2005published-e1]: Bourne 2005, Rule 5. [Evidence](../../sources/notes/bourne2005published.md#e1)
[^bourne2005published-e2]: Bourne 2005, Rule 5. [Evidence](../../sources/notes/bourne2005published.md#e2)
[^huang2021rejection-e2]: Jia-Bin Huang 2021, item 4 (It's not personal). [Evidence](../../sources/notes/huang2021rejection.md#e2)
[^huang2021rejection-e3]: Jia-Bin Huang 2021, item 5 (It doesn't matter much). [Evidence](../../sources/notes/huang2021rejection.md#e3)
[^huang2021rejection-e6]: Jia-Bin Huang 2021, item 2 (It's okay to be upset). [Evidence](../../sources/notes/huang2021rejection.md#e6)
[^ralph2020empirical-e53]: SIGSOFT General Standard, Good Review Practices. [Evidence](../../sources/notes/ralph2020empirical.md#e53)
[^ralph2020empirical-e25]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e25)
[^ralph2020empirical-e41]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e60]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e60)
[^ralph2020empirical-e61]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e61)
[^shaw2003writing-e16]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e17]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e17)
[^hicks2014response-e1]: Hicks 2014 (author response), What is author response? [Evidence](../../sources/notes/hicks2014response.md#e1)
[^hicks2014response-e10]: Hicks 2014 (author response), The goal of your response. [Evidence](../../sources/notes/hicks2014response.md#e10)
[^hicks2014response-e2]: Hicks 2014 (author response), The goal of your response. [Evidence](../../sources/notes/hicks2014response.md#e2)
[^hicks2014response-e3]: Hicks 2014 (author response), General themes for writing the response. [Evidence](../../sources/notes/hicks2014response.md#e3)
[^hicks2014response-e4]: Hicks 2014 (author response), General themes for writing the response. [Evidence](../../sources/notes/hicks2014response.md#e4)
[^hicks2014response-e5]: Hicks 2014 (author response), General themes for writing the response. [Evidence](../../sources/notes/hicks2014response.md#e5)
[^hicks2014response-e7]: Hicks 2014 (author response), General themes for writing the response. [Evidence](../../sources/notes/hicks2014response.md#e7)
[^hicks2014response-e8]: Hicks 2014 (author response), General themes for writing the response. [Evidence](../../sources/notes/hicks2014response.md#e8)
[^karpathy2016survival-e11]: Karpathy 2016, Closing thoughts. [Evidence](../../sources/notes/karpathy2016survival.md#e11)
[^neurips2025cfp-e8]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../sources/notes/neurips2025cfp.md#e8)
[^neurips2025cfp-e11]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../sources/notes/neurips2025cfp.md#e11)
[^neurips2025cfp-e13]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../sources/notes/neurips2025cfp.md#e13)
[^parikh2020rebuttals-e2]: Parikh, Batra & Lee 2020, who reads the rebuttal. [Evidence](../../sources/notes/parikh2020rebuttals.md#e2)
[^parikh2020rebuttals-e4]: Parikh, Batra & Lee 2020, who reads the rebuttal. [Evidence](../../sources/notes/parikh2020rebuttals.md#e4)
[^parikh2020rebuttals-e5]: Parikh, Batra & Lee 2020, writing process. [Evidence](../../sources/notes/parikh2020rebuttals.md#e5)
[^parikh2020rebuttals-e17]: Parikh, Batra & Lee 2020, writing process. [Evidence](../../sources/notes/parikh2020rebuttals.md#e17)
[^parikh2020rebuttals-e6]: Parikh, Batra & Lee 2020, writing process. [Evidence](../../sources/notes/parikh2020rebuttals.md#e6)
[^parikh2020rebuttals-e13]: Parikh, Batra & Lee 2020, Tip 1. [Evidence](../../sources/notes/parikh2020rebuttals.md#e13)
[^parikh2020rebuttals-e7]: Parikh, Batra & Lee 2020, Tip 2. [Evidence](../../sources/notes/parikh2020rebuttals.md#e7)
[^parikh2020rebuttals-e8]: Parikh, Batra & Lee 2020, Tip 3. [Evidence](../../sources/notes/parikh2020rebuttals.md#e8)
[^parikh2020rebuttals-e18]: Parikh, Batra & Lee 2020, Tip 5. [Evidence](../../sources/notes/parikh2020rebuttals.md#e18)
[^parikh2020rebuttals-e12]: Parikh, Batra & Lee 2020, Tip 9. [Evidence](../../sources/notes/parikh2020rebuttals.md#e12)
[^parikh2020rebuttals-e19]: Parikh, Batra & Lee 2020, Tip 10. [Evidence](../../sources/notes/parikh2020rebuttals.md#e19)
[^parikh2020rebuttals-e9]: Parikh, Batra & Lee 2020, Tip 12. [Evidence](../../sources/notes/parikh2020rebuttals.md#e9)
[^parikh2020rebuttals-e10]: Parikh, Batra & Lee 2020, Tip 13. [Evidence](../../sources/notes/parikh2020rebuttals.md#e10)
[^parikh2020rebuttals-e20]: Parikh, Batra & Lee 2020, Tip 14. [Evidence](../../sources/notes/parikh2020rebuttals.md#e20)
[^parikh2020rebuttals-e21]: Parikh, Batra & Lee 2020, Tip 15. [Evidence](../../sources/notes/parikh2020rebuttals.md#e21)
[^parikh2020rebuttals-e15]: Parikh, Batra & Lee 2020, Tip 16. [Evidence](../../sources/notes/parikh2020rebuttals.md#e15)
[^parikh2020rebuttals-e22]: Parikh, Batra & Lee 2020, Tip 17. [Evidence](../../sources/notes/parikh2020rebuttals.md#e22)
[^parikh2020rebuttals-e14]: Parikh, Batra & Lee 2020, Tip 18. [Evidence](../../sources/notes/parikh2020rebuttals.md#e14)
[^usenixsec2026cfp-e13]: USENIX Security '26 call for papers, Simultaneous Submission and Plagiarism. [Evidence](../../sources/notes/usenixsec2026cfp.md#e13)
[^usenixsec2026cfp-e14]: USENIX Security '26 call for papers, Summary of main changes from previous editions. [Evidence](../../sources/notes/usenixsec2026cfp.md#e14)
[^zeller2012rebuttals-e1]: Zeller 2012, Identify the champion. [Evidence](../../sources/notes/zeller2012rebuttals.md#e1)
[^zeller2012rebuttals-e11]: Zeller 2012, Identify the undecided. [Evidence](../../sources/notes/zeller2012rebuttals.md#e11)
[^zeller2012rebuttals-e12]: Zeller 2012, Identify the detractors. [Evidence](../../sources/notes/zeller2012rebuttals.md#e12)
[^zeller2012rebuttals-e2]: Zeller 2012, Arm the champion. [Evidence](../../sources/notes/zeller2012rebuttals.md#e2)
[^zeller2012rebuttals-e13]: Zeller 2012, Write for the PC chair. [Evidence](../../sources/notes/zeller2012rebuttals.md#e13)
[^zeller2012rebuttals-e6]: Zeller 2012, Write for the PC chair. [Evidence](../../sources/notes/zeller2012rebuttals.md#e6)
[^zeller2012rebuttals-e3]: Zeller 2012, Write for the committee. [Evidence](../../sources/notes/zeller2012rebuttals.md#e3)
[^zeller2012rebuttals-e4]: Zeller 2012, Convince. [Evidence](../../sources/notes/zeller2012rebuttals.md#e4)
[^zeller2012rebuttals-e14]: Zeller 2012, Choose comments wisely. [Evidence](../../sources/notes/zeller2012rebuttals.md#e14)
[^zeller2012rebuttals-e5]: Zeller 2012, Choose comments wisely. [Evidence](../../sources/notes/zeller2012rebuttals.md#e5)
[^zeller2012rebuttals-e7]: Zeller 2012, Thank the reviewers. [Evidence](../../sources/notes/zeller2012rebuttals.md#e7)
[^zeller2012rebuttals-e8]: Zeller 2012, Don't expect too much. [Evidence](../../sources/notes/zeller2012rebuttals.md#e8)
[^zeller2012rebuttals-e9]: Zeller 2012, Don't expect too much. [Evidence](../../sources/notes/zeller2012rebuttals.md#e9)
[^zeller2012rebuttals-e10]: Zeller 2012, Organize your rebuttal. [Evidence](../../sources/notes/zeller2012rebuttals.md#e10)
[^ralph2020empirical-e62]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e62)
[^ralph2020empirical-e64]: SIGSOFT General Standard, Reviewing Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e64)
