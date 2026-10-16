# Telling the story and writing the paper

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science. The writing advice here comes mainly from the experience of computer scientists and from evaluation standards in computing, with a little from computational biology and from sources on statistical graphics. Treat it as advice, not rules every field must follow; where your target venue has its own conventions, those win `[Our analysis]`.

## Where you are

The experiments are done, or at least the main results are in. Your folder holds dozens of tables, hundreds of lines of logs, and a set of notes that keeps getting longer. Some slots in the paper outline from your research plan (see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#2-break-the-claim-into-milestones-each-milestone-is-a-piece-of-evidence)) are filled in; some results turned out differently from what you imagined.

You may be stuck on things like these: you have lots of results and don't know which to include and which to cut; you open a blank document and can't get past the first sentence; you don't know how much to write for the introduction, the related work, or the limitations; it reads clearly to you, but you don't know whether anyone else will follow it.

## What this stage is for

Turn a pile of results into a paper that others **can follow, can trust, and will remember**. Concretely, answer these questions:

1. What is the one sentence this paper most wants readers to believe?
2. In what order does the paper tell its story, and what is each paragraph's job?
3. How much do the abstract, introduction, related work, methods, results and limitations each need to cover?
4. How do figures and tables let readers see the conclusion at a glance?
5. Can readers see that you have met the standards of evidence for this kind of research?
6. How do you revise, and whom do you ask to read it?

This chapter doesn't cover grammar or word choice, or the formatting rules of particular conferences and journals. For where to submit and how, see the next chapter, [Choosing a venue and submitting](02_venue-and-submission.md).

## How to use this chapter

The sections are roughly in the order you write, but in practice you will move back and forth: if you can't state the central claim while writing the abstract, go back to Section 1; if, while writing the results, you find a claim with no evidence behind it, cut it or go back and run the experiment (see "When to go back") `[Our analysis]`. Writing itself exposes holes in the research, and the earlier they show up, the better[^eisnerfirst-e6].

---

## 1. Find the story: one central claim

**Before you write anything, answer this: once readers finish the paper, which one sentence should they believe most?**

That sentence is the paper's central claim (see [Key concepts](../00_start-here/key-concepts.md#claim); for how to phrase it as a result and how strongly to word it, see [Converging on a project](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove)). A paper should convey one clear, sharp idea[^peytonjones2013write-e2]. If you have two big ideas, consider writing two papers: put them in one and readers will remember only one[^black2024writing-e3]; a paper that pushes several contributions at once makes none of them convincing[^mensh2017ten-e1]. You can have one to three claims, but they should share a single theme[^nanda2025writing-e1].

It's fine not to know exactly what it is when you start, but you must be able to say it by the time you finish[^peytonjones2013write-e3]. Also state the **insight** that made the problem solvable: not your technical contribution itself, but the insight that leads to it[^black2024writing-e2].

**Check it against the one-page summary from convergence.** The summary stated "the central conclusion I hope to show"; once results are in, it often needs to change, and restating your claim to match what you actually achieved is very common[^shaw2003writing-e17]. For how to revise it to fit the evidence, see [Analyzing and interpreting results](../03_conduct-and-analyze/02_analyze-and-interpret.md#7-when-the-evidence-doesnt-match-the-claim-change-the-claim). For example, if only two benchmarks have severe leakage, write the claim as "on two commonly used benchmarks, leakage substantially inflates accuracy", not "high accuracy comes mainly from leakage" `[Our analysis]`.

**Use the central claim as a filter.** Anything that doesn't support the main line, however correct it is and however much work it cost you, gets cut or rewritten[^ernstwrite-e9]. Readers usually take away only a few sentences, so choose those sentences deliberately[^nanda2025writing-e2].

**Two tests:** A year after reading it, could a reader still tell a colleague your main contribution[^mensh2017ten-e2]? Can you walk a colleague through the outline of the whole paper in a few minutes? If you can't, readers won't get it either[^mensh2017ten-e11].

**Write it down:** State your central claim in one sentence, and the insight behind it in another. Compare with your one-page summary and note what changed in the claim and why.

## 2. Build the outline before writing sentences

**Don't start writing from the first sentence; build an outline first.** One order that works: abstract, then a bullet-point outline, then the introduction, then a full draft, then iterate[^nanda2025writing-e6]. For each planned paragraph in the outline, first write in one plain sentence what it will say[^mensh2017ten-e21]. A good outline is tight and lean, and every part has a clear role in the main line[^nanda2025writing-e9].

**Outline the results as a series of statements.** First work out the logic of how the results build up to the claim step by step, write it as a series of declarative sentences, and use them directly as the subsection headings of the results section[^mensh2017ten-e7].

**Order by logic, not by chronology.** Readers don't care in what order you got your results; they care about the final claim and the logic supporting it[^mensh2017ten-e5]. Tell the story of the results themselves, not of how you stumbled your way to them[^widomtips-e5]. That route "may be soaked with your blood", but it isn't interesting to the reader[^peytonjones2013write-e7].

**Put your effort where most readers look.** The title, abstract and figures are seen most; the methods section is read least. Weight your time accordingly[^mensh2017ten-e9]. And don't allocate space by how much time you spent: the part that took you longest isn't necessarily the part readers most need[^ernstwrite-e3].

Using the leakage-measurement example, an outline might look like this `[Our analysis]`:

```
Central claim: on two commonly used benchmarks, data leakage substantially inflates the accuracy of large-language-model vulnerability detection
1 Introduction: the problem, why it matters, what existing evaluations miss, what this paper does, list of contributions
2 Background and related work: how the benchmarks were built; how far existing leakage studies have gone
3 How to tell whether a contract has leaked (the method, and how accurate it is)
4 Results (each subsection heading is a one-sentence conclusion)
  4.1 Of the four benchmarks, two have many contracts that appear in the models' training data
  4.2 After removing leaked samples, accuracy on these two benchmarks drops substantially
  4.3 The drop appears across multiple models; it is not a quirk of one model
5 Discussion and limitations: what the leakage method might miss; where the conclusions apply
6 Conclusion
```

The list of figures and tables with their status from your research plan now becomes the skeleton of the results section.

**Write it down:** Write your outline: one line per section, and each results subsection heading as a one-sentence conclusion. Then check: is there any section whose role in the main line you can't state?

## 3. Title and abstract: tell the whole story

For most readers, the abstract is the only part they will read[^mensh2017ten-e12]. People use it to decide whether to read the full paper, so the abstract has to tell the whole story[^shaw2003writing-e23].

**Write the abstract as context, content, conclusion**[^mensh2017ten-e15]:

| Part | What to write | Example (illustrative) |
|---|---|---|
| Context | Narrow from the broad field down to a gap: what is missing and why it matters | Large-language-model vulnerability detection reaches high accuracy on benchmarks, but no one has checked whether the benchmark contracts already appear in the training data |
| Content | What method you used and what the main results are | We propose a method for detecting leakage and examine four commonly used benchmarks… |
| Conclusion | Answer the question posed at the start; say what it means for the field | Some existing results are inflated; evaluations should remove leaked samples first |

The most common mistake in abstracts is talking about results before the reader is ready to understand them[^mensh2017ten-e16]. Another common mistake is saying only "what we studied" and not "what we found": tell the whole story right away; don't hold anything back[^raibert1985good-e3]. The title is the final distillation of your contribution; come up with one early and keep refining it as you write[^mensh2017ten-e17].

**Write it down:** Write a version of the abstract following the three rows above, one or two sentences each. Read it to a classmate who doesn't know the project and ask: what did this paper find?

## 4. Introduction: five questions plus a list of contributions

For beginners, the introduction is often the hardest part to write[^huang2023introduction-e1]. By the time reviewers finish the introduction, most of them have already formed a first judgment[^widomtips-e1][^black2024writing-e1].

**How to write it:** One approach that works: unless you have a particular reason not to, write the introduction as five paragraphs answering five questions[^widomtips-e2][^widomtips-e8]:

1. **What is the problem?** Ideally, lead into it with a concrete example[^peytonjones2013write-e13].
2. **Why is it interesting and important?**
3. **Why is it hard?** For example, why the naive approaches don't work.
4. **Why hasn't it been solved before?** Where existing solutions fall short, and how yours differs. Make clear why existing solutions are unsatisfactory[^huang2023introduction-e2]. If you can include a figure that uses a concrete example to show the core problem with existing work, that works best[^huang2023introduction-e5].
5. **What are the key elements of your approach and results?** Including specific limitations. The last paragraph of the introduction briefly summarizes the results and explains how they fill the gap set out earlier[^mensh2017ten-e18].

**Then list your contributions.** Write the main contributions as a bulleted list, noting which section each is in[^widomtips-e3]. The rest of the paper exists to back up this list[^peytonjones2013write-e4]. A contribution (what this research adds to the field; see [Key concepts](../00_start-here/key-concepts.md#contribution)) is anything the world did not know before this paper but now knows because of it[^vandeursen2013writing-e1]; it is an outcome, not the effort you put in[^vandeursen2013writing-e2]. Each contribution should be specific enough to be refutable[^peytonjones2013write-e5]. The numbers and wording in the table below are illustrative `[Our analysis]`:

| Written as effort (weak) | Written as outcome (strong) |
|---|---|
| "We collected 20,000 contracts and tested 5 models" | "We find that in two of the four commonly used benchmarks, many contracts appear in the models' training data (Section 4.1)" |
| "We designed a leakage detection pipeline" | "We present a method for determining whether a contract has leaked, which largely agrees with human judgment on a manually checked sample (Section 3)" |

**Separate what is new from what isn't.** Not everything you built is new; much of it may rest on existing methods, so state explicitly which parts are your contribution[^huang2023introduction-e4], and keep background material apart from your own contributions[^vandeursen2013writing-e3]. Especially in the introduction and related work, be very clear about what is new and what isn't[^nanda2025writing-e7]. Don't write a general literature review in the introduction; include only what bears on the motivation[^mensh2017ten-e6].

> **Field differences**: Listing contributions one by one with section numbers, and the idea that "a clear new important technical contribution should have been articulated by the time the reader finishes page 3"[^widomtips-e6], both come from computer scientists' writing advice. `[Our analysis]` They are mainly conventions of computer science and engineering conference papers. Many journals and fields have a fixed structure and don't necessarily list contributions as bullets. But "readers should quickly see what is new" applies in every field. Before you start, look at how recent papers at your target venue are written.

**Write it down:** Write one or two sentences for each of the five questions. Then write your list of contributions, each starting with "We find / We prove / We present", with the section number.

## 5. Related work: show where you stand

Related work is not there to prove "I've read a lot of papers". It explains how your work relates to existing work: whether you build on it and push it further, or offer a different approach[^shaw2003writing-e1]. If you don't make this clear, reviewers can't see what new knowledge you add; and if they can't tell whether you know the related work, your credibility suffers[^shaw2003writing-e4].

**Write specific comparisons, not a string of citations.** Weak versions are "this problem has received much attention [3,8,10,18,26]" or "A and B have studied this problem"[^shaw2003writing-e2]; a strong version says specifically how far each piece of work got, where its limits are, and where exactly you differ[^shaw2003writing-e3]. The comparison table you drew in [Converging on a project](../01_from-interest-to-project/03_converge.md#3-has-someone-already-done-it) is exactly this kind of content; the related work section turns it into prose `[Our analysis]`.

- **Choose a reasonable number of works, and synthesize rather than list.** You don't need to cite every related study[^ralph2020empirical-e19]. Group the work by approach, connect each group to your own work, and explain how your contribution relates to it[^ralph2020empirical-e20]. In the contract example, you might use three groups: "how vulnerability benchmarks are built", "how far existing leakage checks go", and "how large-language-model vulnerability detection is evaluated", with the last sentence of each group saying "this paper differs on this point" `[Our analysis]`.
- **Don't mention work only to say it isn't relevant, and don't list without synthesizing**[^ralph2020empirical-e21].
- **Give credit generously.** Acknowledging others' contributions doesn't take away from yours[^peytonjones2013write-e11].

> **Where sources disagree: related work early or late?**
>
> - Late: describing other people's approaches first gets in the way between the reader and your idea[^peytonjones2013write-e8].
> - It depends; both can work: put it early if it can be short and specific, or if you must distinguish yourself from existing work right at the start[^widomtips-e4]; put it late if you can summarize it briefly in the introduction, or if the comparisons only make sense after the technical content[^widomtips-e9].
>
> Either way, the introduction must make clear how you differ from the closest work[^nanda2025writing-e7]. `[Our analysis]` Check your target venue's conventions first, then ask yourself: do readers need to understand your method before these comparisons make sense?

**Write it down:** Rewrite the comparison table as two or three paragraphs of related work, each ending with a sentence on "this paper differs on this point".

## 6. Methods and results: write them so others can check them

**Methods: intuition first, then details.** Conveying the intuition is primary, not secondary[^peytonjones2013write-e9]. You might first walk one concrete contract through your decision procedure, then give the full definition `[Our analysis]`. The details must be complete enough for someone else to redo the work. One of the essential requirements in the software engineering empirical standards for benchmarking studies is describing the experimental setup in enough detail for others to reproduce it independently[^ralph2020empirical-e148]. A systematization-of-knowledge paper on benchmarking flaws in systems security lists common omissions including the hardware platform, software versions, and results for individual sub-benchmarks[^vanderkouwe2019sok-e13]. For work with large language models, also state the model versions, when you queried them, and the exact prompts `[Our analysis]`.

**Results: each paragraph answers one question.** Open each paragraph with a sentence or two posing the question it answers, give the data and reasoning in the middle, and end with the answer. That way readers can easily find which paragraph a doubtful conclusion comes from and check its logic[^mensh2017ten-e20].

**Point every claim to its evidence.** Go through the claims in your introduction one by one, find the evidence for each, and note at the claim which section the evidence is in[^peytonjones2013write-e6]. The evidence has to match the claim: if you claim a performance improvement, analyze performance, not ease of use[^shaw2003writing-e12].

**Carry the wording you checked during analysis into the paper unchanged.** For how strongly to word a claim and how much evidence that needs, see [Converging on a project](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove); for how to report results (how big, how certain, not just the best run), see [Analyzing and interpreting results](../03_conduct-and-analyze/02_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value); for how far conclusions can reach and how to keep speculation apart from evidence, see [Section 6](../03_conduct-and-analyze/02_analyze-and-interpret.md#6-how-far-your-conclusions-can-reach) of the same chapter. The easiest mistake to make while writing is overstating things again as you polish `[Our analysis]`. In tables, give results for each sub-benchmark, not just an overall score[^heiserbenchmarking-e18]; when you give relative numbers, give absolute numbers too, so readers can judge whether the configuration is reasonable[^vanderkouwe2019sok-e23]. Go easy on self-assessments like "novel", "significant" or "best"; state the facts and let readers judge[^ernstwrite-e7].

**Write it down:** Copy every claim from your introduction into one column, and next to each write the figure, table or section that supports it. Cut or weaken any claim you can't find evidence for.

## 7. Figures and tables: the title states the conclusion, the caption explains the method

Many readers go straight from the abstract to the figures. So **a figure's title should state the conclusion of the analysis, and its caption should explain how it was done**[^mensh2017ten-e19]. For example, instead of "Figure 3: Accuracy of each model", write "Figure 3: After removing leaked samples, accuracy drops substantially on both benchmarks" `[Our analysis]`.

**The caption must state** what the error bars are (standard deviation, standard error, or confidence interval)[^cumming2007error-e1], and the sample size n, that is, the number of independent replicates[^cumming2007error-e2].

**Let readers see the data itself.** Bar charts of means with error bars can hide the real distribution of the data: many different distributions produce the exact same bar chart[^weissgerber2015beyond-e1]. When there are few data points, it is best to plot every point[^weissgerber2015beyond-e3][^cumming2007error-e5]. Plotting the standard error rather than the standard deviation visually exaggerates differences between groups[^weissgerber2015beyond-e5]. Reporting only the mean or median can mislead readers; report the distribution as well[^blackburn2018sigplan-e8]. Choose colors everyone can read, too: red-green color schemes with similar lightness can't be read by a large fraction of readers[^crameri2020misuse-e4].

**Consider a "why" figure as well.** Put a figure in the introduction that uses a concrete example to show the core problem with existing work[^huang2023introduction-e5]. In the contract example, you could place a benchmark contract side by side with the nearly identical one in the model's training data `[Our analysis]`.

**Start from the empty tables you drew while planning.** If you sketched empty results tables during planning, with row and column headings and captions[^eisnerfirst-e5], now is the time to fill them in and then rewrite them so the title states the conclusion `[Our analysis]`.

**Write it down:** Write a one-sentence "conclusion title" for every figure and table in the paper. Check every caption: does it say what the error bars are and what n is?

## 8. Discussion and limitations: say honestly how far you got

**The discussion does three things:** it explains how the results fill the gap set out in the introduction; it explains what to keep in mind when interpreting the results; and it explains how the paper moves the field forward[^mensh2017ten-e8]. The following paragraphs each take up one weakness or strength of the paper and assess it in light of the relevant literature[^mensh2017ten-e22].

**Write the limitations, and write the ones that actually matter.** The empirical standards of the Association for Computing Machinery Special Interest Group on Software Engineering (ACM SIGSOFT) list "discloses all major limitations" as essential[^ralph2020empirical-e18], and "describes reasonable attempts to investigate or mitigate limitations" as desirable[^ralph2020empirical-e51]. For why listing only trivial limitations misleads, see [Analyzing and interpreting results](../03_conduct-and-analyze/02_analyze-and-interpret.md#6-how-far-your-conclusions-can-reach).

**How to find the real limitations:** Start from the list of limitations you wrote at the design stage (see [Validity and limitations: think them through at the design stage](../02_from-project-to-study/03_validity-and-limits.md#8-write-your-limitations-now-and-set-rules-for-honest-reporting)), then ask yourself: suppose I am wrong; where would I be wrong[^nanda2025writing-e4]? In the contract example, you might ask: what might the leakage method miss, and does a contract with renamed variables count as leaked? For models whose training data isn't public, how did you decide? You looked only at four benchmarks and a handful of models; how far do the conclusions generalize `[Our analysis]`?

**Keep limitations and conclusions consistent.** Don't admit sampling bias in the limitations and then claim in the conclusion that the results are nearly universal[^baltes2022sampling-e9]. Neither overstate nor understate your results[^zhang2014ten-e4].

**Write it down:** Write the three limitations you think are most real. For each, say how it could affect the conclusions and what you did to mitigate it. Then reread your conclusions and check whether any sentence goes beyond what the limitations allow.

## 9. Make the evidence standards of your research strategy visible

Different research strategies (the main logic by which a project produces new knowledge; see [Key concepts](../00_start-here/key-concepts.md#research-strategy)) give readers different standards for judging "is this enough?". When you write, let readers **see at a glance what kind of knowledge you are delivering, and that you meet its standards**. If reviewers can't tell whether you are proposing a new evaluation technique, applying an old technique to a new example, or evaluating a mature technique, you haven't written it clearly enough[^shaw2003writing-e31].

What evidence each strategy requires is set out in the "What evidence is enough" section of each strategy page: [Description](../05_research-strategies/observe_describe.md#2-what-evidence-is-enough), [Measurement](../05_research-strategies/measure.md#2-what-evidence-is-enough), [Comparative evaluation](../05_research-strategies/compare_evaluate.md#2-what-evidence-is-enough), [Causal explanation](../05_research-strategies/explain_causality.md#2-what-evidence-is-enough), [Building and improving](../05_research-strategies/build_improve.md#2-what-evidence-is-enough), [Synthesis](../05_research-strategies/synthesize.md#2-what-evidence-is-enough), and [Proof](../05_research-strategies/prove.md#2-what-evidence-is-enough). Once you have a draft, check the paper item by item against your strategy's list, and give every requirement a definite place in the paper: which section, which figure or table, rather than leaving readers to piece it together from scattered bits `[Our analysis]`. Our example is a Measurement study: the claim is "existing evaluations overestimate accuracy". The first question readers will ask is "is your method for detecting leakage reliable?", so Section 3 needs to establish that on its own, not mention it in passing in an appendix `[Our analysis]`.

**Write it down:** Write down which strategy your paper belongs to. Open that strategy page, list the evidence it requires, and next to each item write which section and which figure or table of your paper meets it.

## 10. Revise, and ask others to read

**Accept that the first draft will be bad.** Good writing means writing bad stuff first and then revising it until it is good[^raibert1985good-e1]; revising the same passage a dozen times or more is normal[^raibert1985good-e2]. Every good paper started out as a bad paper[^black2024writing-e5]. When you're stuck, write something down and fix it later[^ernstwrite-e8].

**Be willing to cut.** Deleting a whole paragraph and rewriting it is often faster than tweaking it bit by bit[^mensh2017ten-e10]. Make every word count[^ernstwrite-e10]. When you revise, put yourself fully in the reviewer's position and examine every part carefully[^zhang2014ten-e5].

**Then ask others to read it.** After months immersed in the project, it is easy to assume readers know what you know; this is the "illusion of transparency"[^nanda2025writing-e5]. Only feedback from other people can help you catch it `[Our analysis]`.

- **Use your readers carefully.** Each reader can read your paper for the first time only once[^peytonjones2013write-e10]; someone who has read it once already knows what you are trying to say on the second pass[^raibert1985good-e6]. So ask different people to read it at different stages `[Our analysis]`.
- **Ask the right question.** Ask readers to tell you "where did you get lost?"; that matters far more than catching typos `[Our analysis]`.
- **Trust your readers' confusion.** When a reader says they don't understand, don't argue; go fix that part[^raibert1985good-e4]. Vague feedback, or readers who aren't very excited, usually means they missed the main line[^mensh2017ten-e14].
- **Return the favor.** Offer to read other people's drafts[^vandeursen2013writing-e5].

For the final check before submission (proofreading, anticipating reviewers' questions, setting an internal deadline), see [Choosing a venue and submitting](02_venue-and-submission.md#5-one-last-check-before-you-submit).

**Why it's worth the effort.** A paper is one-to-many: you pay the cost of explaining once, but every reader pays the cost of understanding[^olah2017debt-e1]. One computer scientist even argues that clear motivation and exposition matter more than results for getting a paper accepted[^eisnerfirst-e9].

> **Where sources disagree: write the abstract and introduction first or last?**
>
> - Some prefer to write them last, because by then the body is finished and you just describe it[^ernstwrite-e11].
> - Others argue for writing them early: the abstract and introduction frame the whole paper, so write them early and revise as needed[^ernstwrite-e6]; you can even write the introduction before you have results[^black2024writing-e4].
>
> `[Our analysis]` For beginners, we suggest writing a rough version early, to test your thinking and discuss with your advisor; once the body is done, rewrite it to match the actual results.

**Write it down:** List two or three people you could ask to read your draft, and for each, note at what stage they will read it and what you want them to focus on. After each round of feedback, record what you changed.

---

## Judgment calls

**The results don't match the original claim: change the claim or run more experiments?** `[Our analysis]`

| Situation | Usual approach |
|---|---|
| The results support a narrower claim | Change the claim; write what you actually achieved |
| A key experiment is missing, and the claim can't stand without it | Go back and run it; if you can't, cut the claims that depend on it |
| The results are the opposite of what you expected, but the evidence is solid | Rewrite the story around the new finding |
| You have evidence for two main lines, but they are unrelated | Split them into two papers, or write up only one |

**What goes in the main text, what goes in an appendix, and what gets cut?** Ask one question: does it support the central claim? If it does, it goes in the main text; if readers need it to check the evidence but it doesn't affect the main line, it goes in an appendix; if neither, cut it `[Our analysis]`.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Cramming several big ideas into one paper | None of them is convincing, and readers will remember only one[^mensh2017ten-e1][^black2024writing-e3] |
| Presenting effort as contribution | A contribution is an outcome, not effort[^vandeursen2013writing-e2] |
| An abstract that only says "what we studied" | The abstract has to tell the whole story[^shaw2003writing-e23][^raibert1985good-e3] |
| Related work written as "A did X, B did Y" | Readers can't see how your work relates to theirs[^ralph2020empirical-e21] |
| Making claims stronger than the evidence while polishing | The stronger the claim, the higher the bar for evidence[^nanda2025writing-e3] |
| Giving only an overall score | At worst it hides problems; at best it still shows readers much less[^heiserbenchmarking-e18] |
| A figure title that just says "Accuracy of each model" | Many readers look only at the figures; the title should state the conclusion[^mensh2017ten-e19] |
| Admitting something in the limitations and forgetting it in the conclusion | An antipattern listed in the software engineering empirical standards[^ralph2020empirical-e66] |
| Arguing with a reader who says they don't understand | Trust the reader's confusion and fix the text[^raibert1985good-e4] |

## What you should have at the end

- A one-sentence central claim, with a note on how it changed from the one-page summary (Section 1)
- A paper outline in which every results subsection heading is a declarative sentence (Section 2)
- A complete draft: abstract, introduction with list of contributions, related work, methods, results, discussion and limitations
- A claim-to-evidence table (Section 6), and the results of checking the paper against your strategy's evidence standards (Section 9)
- At least one round of feedback from someone else, and a record of the changes you made in response (Section 10)

## Checklist before moving on

You are ready for the next step when:

- [ ] You can state the central claim in one sentence, phrased as a result
- [ ] The abstract covers context, content and conclusion, including what you found
- [ ] The introduction answers the five questions, and every item in the list of contributions is an outcome with its section noted
- [ ] The related work makes clear how each group of work relates to this paper, rather than listing papers one by one
- [ ] Every claim points to a specific figure, table or section, and its strength matches the evidence
- [ ] Every figure title states a conclusion, and every caption says what the error bars are and what n is
- [ ] The limitations that actually matter are written down, and the conclusions don't go beyond what they allow
- [ ] You have checked the paper against the evidence standards of its research strategy
- [ ] At least one person who hadn't seen the draft has read it, and you have revised wherever they got confused

## When to go back

| If this happens | Go back to |
|---|---|
| While writing, you find a key experiment is missing and the claim can't stand | [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md), to run the experiment |
| However you write it, you can't say clearly what the results mean | [Analysis and interpretation](../03_conduct-and-analyze/02_analyze-and-interpret.md), to reinterpret the results |
| You can't say how you differ from the closest work, or you find while writing that someone has already published it | [Converging on a project](../01_from-interest-to-project/03_converge.md#3-has-someone-already-done-it) |
| Once the limitations section is written, the evidence can't support any interesting claim | [Validity and limitations: think them through at the design stage](../02_from-project-to-study/03_validity-and-limits.md), and decide with your advisor what you can still claim |

## Next

Once the draft has been revised until every item on the checklist is met, the next step is to decide where to submit, prepare the manuscript to that venue's requirements, and submit it; see [Choosing a venue and submitting](02_venue-and-submission.md). For how to respond and revise once reviews come back, see [Reviews, revision, and what to do after rejection](03_review-and-revision.md).

[^peytonjones2013write-e2]: Peyton Jones 2013, slide "The idea". [Evidence](../../sources/notes/peytonjones2013write.md#e2)
[^peytonjones2013write-e3]: Peyton Jones 2013, slide "The idea". [Evidence](../../sources/notes/peytonjones2013write.md#e3)
[^peytonjones2013write-e4]: Peyton Jones 2013, slide "State your contributions". [Evidence](../../sources/notes/peytonjones2013write.md#e4)
[^peytonjones2013write-e5]: Peyton Jones 2013, slide "Contributions should be refutable". [Evidence](../../sources/notes/peytonjones2013write.md#e5)
[^peytonjones2013write-e6]: Peyton Jones 2013, slide "Evidence". [Evidence](../../sources/notes/peytonjones2013write.md#e6)
[^peytonjones2013write-e7]: Peyton Jones 2013, slide "Putting the reader first". [Evidence](../../sources/notes/peytonjones2013write.md#e7)
[^peytonjones2013write-e8]: Peyton Jones 2013, slide "Related work". [Evidence](../../sources/notes/peytonjones2013write.md#e8)
[^peytonjones2013write-e9]: Peyton Jones 2013, slide "Presenting the idea". [Evidence](../../sources/notes/peytonjones2013write.md#e9)
[^peytonjones2013write-e10]: Peyton Jones 2013, slide "Getting help". [Evidence](../../sources/notes/peytonjones2013write.md#e10)
[^peytonjones2013write-e11]: Peyton Jones 2013, slide "Credit". [Evidence](../../sources/notes/peytonjones2013write.md#e11)
[^peytonjones2013write-e13]: Peyton Jones 2013, slide "Describe the problem". [Evidence](../../sources/notes/peytonjones2013write.md#e13)
[^mensh2017ten-e1]: Mensh & Kording 2017, Rule 1. [Evidence](../../sources/notes/mensh2017ten.md#e1)
[^mensh2017ten-e2]: Mensh & Kording 2017, Rule 1. [Evidence](../../sources/notes/mensh2017ten.md#e2)
[^mensh2017ten-e5]: Mensh & Kording 2017, Rule 3. [Evidence](../../sources/notes/mensh2017ten.md#e5)
[^mensh2017ten-e6]: Mensh & Kording 2017, Rule 6. [Evidence](../../sources/notes/mensh2017ten.md#e6)
[^mensh2017ten-e7]: Mensh & Kording 2017, Rule 7. [Evidence](../../sources/notes/mensh2017ten.md#e7)
[^mensh2017ten-e8]: Mensh & Kording 2017, Rule 8. [Evidence](../../sources/notes/mensh2017ten.md#e8)
[^mensh2017ten-e9]: Mensh & Kording 2017, Rule 9. [Evidence](../../sources/notes/mensh2017ten.md#e9)
[^mensh2017ten-e10]: Mensh & Kording 2017, Rule 10. [Evidence](../../sources/notes/mensh2017ten.md#e10)
[^mensh2017ten-e11]: Mensh & Kording 2017, Rule 10. [Evidence](../../sources/notes/mensh2017ten.md#e11)
[^mensh2017ten-e12]: Mensh & Kording 2017, Rule 5. [Evidence](../../sources/notes/mensh2017ten.md#e12)
[^mensh2017ten-e14]: Mensh & Kording 2017, Rule 10. [Evidence](../../sources/notes/mensh2017ten.md#e14)
[^mensh2017ten-e15]: Mensh & Kording 2017, Rule 5. [Evidence](../../sources/notes/mensh2017ten.md#e15)
[^mensh2017ten-e16]: Mensh & Kording 2017, Rule 5. [Evidence](../../sources/notes/mensh2017ten.md#e16)
[^mensh2017ten-e17]: Mensh & Kording 2017, Rule 1. [Evidence](../../sources/notes/mensh2017ten.md#e17)
[^mensh2017ten-e18]: Mensh & Kording 2017, Rule 6. [Evidence](../../sources/notes/mensh2017ten.md#e18)
[^mensh2017ten-e19]: Mensh & Kording 2017, Rule 7. [Evidence](../../sources/notes/mensh2017ten.md#e19)
[^mensh2017ten-e20]: Mensh & Kording 2017, Rule 7. [Evidence](../../sources/notes/mensh2017ten.md#e20)
[^mensh2017ten-e21]: Mensh & Kording 2017, Rule 9. [Evidence](../../sources/notes/mensh2017ten.md#e21)
[^mensh2017ten-e22]: Mensh & Kording 2017, Rule 8. [Evidence](../../sources/notes/mensh2017ten.md#e22)
[^widomtips-e1]: Widom 2006, The Introduction. [Evidence](../../sources/notes/widomtips.md#e1)
[^widomtips-e2]: Widom 2006, The Introduction. [Evidence](../../sources/notes/widomtips.md#e2)
[^widomtips-e3]: Widom 2006, The Introduction. [Evidence](../../sources/notes/widomtips.md#e3)
[^widomtips-e4]: Widom 2006, Related Work. [Evidence](../../sources/notes/widomtips.md#e4)
[^widomtips-e5]: Widom 2006, The Body. [Evidence](../../sources/notes/widomtips.md#e5)
[^widomtips-e6]: Widom 2006, The Body. [Evidence](../../sources/notes/widomtips.md#e6)
[^widomtips-e8]: Widom 2006, The Introduction. [Evidence](../../sources/notes/widomtips.md#e8)
[^widomtips-e9]: Widom 2006, Related Work. [Evidence](../../sources/notes/widomtips.md#e9)
[^huang2023introduction-e1]: Huang 2023, tweet thread, opening. [Evidence](../../sources/notes/huang2023introduction.md#e1)
[^huang2023introduction-e2]: Huang 2023, tweet thread, Q1–Q3. [Evidence](../../sources/notes/huang2023introduction.md#e2)
[^huang2023introduction-e4]: Huang 2023, tweet thread, Q5. [Evidence](../../sources/notes/huang2023introduction.md#e4)
[^huang2023introduction-e5]: Huang 2023, tweet thread, the WHY figure part. [Evidence](../../sources/notes/huang2023introduction.md#e5)
[^shaw2003writing-e1]: Shaw 2003, §3.3. [Evidence](../../sources/notes/shaw2003writing.md#e1)
[^shaw2003writing-e2]: Shaw 2003, §3.3, example. [Evidence](../../sources/notes/shaw2003writing.md#e2)
[^shaw2003writing-e3]: Shaw 2003, §3.3, example. [Evidence](../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e4]: Shaw 2003, §3.3. [Evidence](../../sources/notes/shaw2003writing.md#e4)
[^shaw2003writing-e12]: Shaw 2003, §4.3. [Evidence](../../sources/notes/shaw2003writing.md#e12)
[^shaw2003writing-e17]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e17)
[^shaw2003writing-e23]: Shaw 2003, §6. [Evidence](../../sources/notes/shaw2003writing.md#e23)
[^shaw2003writing-e31]: Shaw 2003, §2.3. [Evidence](../../sources/notes/shaw2003writing.md#e31)
[^nanda2025writing-e1]: Nanda 2025, TL;DR. [Evidence](../../sources/notes/nanda2025writing.md#e1)
[^nanda2025writing-e2]: Nanda 2025, Crafting a Narrative. [Evidence](../../sources/notes/nanda2025writing.md#e2)
[^nanda2025writing-e3]: Nanda 2025, Crafting a Narrative. [Evidence](../../sources/notes/nanda2025writing.md#e3)
[^nanda2025writing-e4]: Nanda 2025, Rigorous Supporting Evidence. [Evidence](../../sources/notes/nanda2025writing.md#e4)
[^nanda2025writing-e5]: Nanda 2025, The Writing Process. [Evidence](../../sources/notes/nanda2025writing.md#e5)
[^nanda2025writing-e6]: Nanda 2025, TL;DR. [Evidence](../../sources/notes/nanda2025writing.md#e6)
[^nanda2025writing-e7]: Nanda 2025, Novelty. [Evidence](../../sources/notes/nanda2025writing.md#e7)
[^nanda2025writing-e9]: Nanda 2025, Iteratively Expand. [Evidence](../../sources/notes/nanda2025writing.md#e9)
[^black2024writing-e1]: Black 2024, Introduction. [Evidence](../../sources/notes/black2024writing.md#e1)
[^black2024writing-e2]: Black 2024, The Nugget. [Evidence](../../sources/notes/black2024writing.md#e2)
[^black2024writing-e3]: Black 2024, How to tell a story: Goal, Problem, Solution. [Evidence](../../sources/notes/black2024writing.md#e3)
[^black2024writing-e4]: Black 2024, Number one writing tip. [Evidence](../../sources/notes/black2024writing.md#e4)
[^black2024writing-e5]: Black 2024, Number one writing tip. [Evidence](../../sources/notes/black2024writing.md#e5)
[^ernstwrite-e3]: Ernst, Which details to include. [Evidence](../../sources/notes/ernstwrite.md#e3)
[^ernstwrite-e6]: Ernst, Make the organization and results clear. [Evidence](../../sources/notes/ernstwrite.md#e6)
[^ernstwrite-e7]: Ernst, Writing style. [Evidence](../../sources/notes/ernstwrite.md#e7)
[^ernstwrite-e8]: Ernst, Getting started. [Evidence](../../sources/notes/ernstwrite.md#e8)
[^ernstwrite-e9]: Ernst, Which details to include. [Evidence](../../sources/notes/ernstwrite.md#e9)
[^ernstwrite-e10]: Ernst, Brevity. [Evidence](../../sources/notes/ernstwrite.md#e10)
[^ernstwrite-e11]: Ernst, Make the organization and results clear. [Evidence](../../sources/notes/ernstwrite.md#e11)
[^raibert1985good-e1]: Raibert 1985, opening section. [Evidence](../../sources/notes/raibert1985good.md#e1)
[^raibert1985good-e2]: Raibert 1985, Good Writing is Bad Writing That Was Rewritten. [Evidence](../../sources/notes/raibert1985good.md#e2)
[^raibert1985good-e3]: Raibert 1985, Spill the Beans Fast. [Evidence](../../sources/notes/raibert1985good.md#e3)
[^raibert1985good-e4]: Raibert 1985, Trust Your Readers. [Evidence](../../sources/notes/raibert1985good.md#e4)
[^raibert1985good-e6]: Raibert 1985, Husband Your Readers. [Evidence](../../sources/notes/raibert1985good.md#e6)
[^vandeursen2013writing-e1]: van Deursen 2013, Identify the Contributions. [Evidence](../../sources/notes/vandeursen2013writing.md#e1)
[^vandeursen2013writing-e2]: van Deursen 2013, Identify the Contributions. [Evidence](../../sources/notes/vandeursen2013writing.md#e2)
[^vandeursen2013writing-e3]: van Deursen 2013, Structure the Paper. [Evidence](../../sources/notes/vandeursen2013writing.md#e3)
[^vandeursen2013writing-e5]: van Deursen 2013, Share Contributions Early. [Evidence](../../sources/notes/vandeursen2013writing.md#e5)
[^zhang2014ten-e4]: Zhang 2014, Rule 8. [Evidence](../../sources/notes/zhang2014ten.md#e4)
[^zhang2014ten-e5]: Zhang 2014, Rule 8. [Evidence](../../sources/notes/zhang2014ten.md#e5)
[^eisnerfirst-e5]: Eisner 2010, What needs to be done? [Evidence](../../sources/notes/eisnerfirst.md#e5)
[^eisnerfirst-e6]: Eisner 2010, What needs to be done? [Evidence](../../sources/notes/eisnerfirst.md#e6)
[^eisnerfirst-e9]: Eisner 2010, Clear writing increases your odds of acceptance. [Evidence](../../sources/notes/eisnerfirst.md#e9)
[^olah2017debt-e1]: Olah & Carter 2017, Interpretive Labor. [Evidence](../../sources/notes/olah2017debt.md#e1)
[^ralph2020empirical-e18]: ACM SIGSOFT Empirical Standards, General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e18)
[^ralph2020empirical-e19]: ACM SIGSOFT Empirical Standards, General Standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e19)
[^ralph2020empirical-e20]: ACM SIGSOFT Empirical Standards, General Standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e20)
[^ralph2020empirical-e21]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e21)
[^ralph2020empirical-e51]: ACM SIGSOFT Empirical Standards, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e51)
[^ralph2020empirical-e66]: ACM SIGSOFT Empirical Standards, General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e148]: ACM SIGSOFT Empirical Standards, Benchmarking standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e148)
[^baltes2022sampling-e9]: Baltes & Ralph 2022, §6. [Evidence](../../sources/notes/baltes2022sampling.md#e9)
[^heiserbenchmarking-e18]: Heiser, Benchmarking Crimes, Missing sub-benchmark results. [Evidence](../../sources/notes/heiserbenchmarking.md#e18)
[^vanderkouwe2019sok-e13]: van der Kouwe et al. 2019, §II, Table I. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e13)
[^vanderkouwe2019sok-e23]: van der Kouwe et al. 2019, §II-F. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e23)
[^blackburn2018sigplan-e8]: SIGPLAN Empirical Evaluation Checklist, Adequate Data Analysis. [Evidence](../../sources/notes/blackburn2018sigplan.md#e8)
[^cumming2007error-e1]: Cumming et al. 2007, Rule 1. [Evidence](../../sources/notes/cumming2007error.md#e1)
[^cumming2007error-e2]: Cumming et al. 2007, Rule 2. [Evidence](../../sources/notes/cumming2007error.md#e2)
[^cumming2007error-e5]: Cumming et al. 2007, Rule 4. [Evidence](../../sources/notes/cumming2007error.md#e5)
[^weissgerber2015beyond-e1]: Weissgerber et al. 2015, Introduction. [Evidence](../../sources/notes/weissgerber2015beyond.md#e1)
[^weissgerber2015beyond-e3]: Weissgerber et al. 2015, Recommendations for a New Data Presentation Paradigm. [Evidence](../../sources/notes/weissgerber2015beyond.md#e3)
[^weissgerber2015beyond-e5]: Weissgerber et al. 2015, Are Your Figures Worth a Thousand Words? [Evidence](../../sources/notes/weissgerber2015beyond.md#e5)
[^crameri2020misuse-e4]: Crameri et al. 2020, Introduction. [Evidence](../../sources/notes/crameri2020misuse.md#e4)
