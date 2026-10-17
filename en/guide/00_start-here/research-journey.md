# The research journey at a glance: from interest to publication

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science.

Maybe you have just been handed a research area: say your advisor told you to "take a look at large language models and smart contract security". Or maybe you are already running experiments but can't say which stage you are at or how far you are from publishing.

This page is the map of the whole handbook: which chapters a study passes through on its way from a vague interest to publication, what each chapter produces, how far you need to get before moving on, and when to go back. The concrete steps are all in the chapters; this page only gives the route. For how to read the handbook and how each chapter is structured, see [How to use this handbook](how-to-use.md); for what we mean by research area, problem, claim, evidence, research strategy, and the other terms used here, see [Key concepts](key-concepts.md).

When you finish this page, you should be able to say which chapter you are in, what you are missing, and which chapter to read next.

---

## 1. The whole journey in one picture

```
  Part 1 · Find a good problem (exploration)
  1.1 Enter a field → 1.2 Generate candidates → 1.3 Explore hands-on → 1.4 Judge and screen → 1.5 Converge
                                                                                                 │
                                       Exit: one sentence you can write down, and you know what evidence would test it
                                                                                                 ↓
  Part 2 · Do the project (verification)
  2.1 Evidence plan → 2.2 Choose a method → 2.3 Research plan → 2.4 Validity and limitations → 2.5 Smallest runnable version
        ↑                                                                                        │
        │                    2.8 Decision points: continue, adjust, or go back to Part 1         ↓
        └──────────────── 2.7 Analysis and interpretation ←──────── 2.6 Run and iterate ←────────┘
                                   │
                                   ↓
  Writing and publishing: write the paper → submit → reviews and revision (reviews can send you back too)

  Look up when needed: Research types · Fields · Research strategies · Throughout the project · FAQ
```

Part 1 is **exploration**: you read the literature, collect ideas, try things out, and screen them until you can write down one sentence you want to prove, and from that sentence you work out which research type you are doing. Part 2 is **verification**: you turn that sentence into evidence, then design, pilot, run, and analyze. It loops around a few decision points; it is not a straight line. Writing and publishing is a part of its own. The bottom line is the Reference, which you look up when you need it; see [How to use this handbook](how-to-use.md#how-the-handbook-is-organized-a-two-part-backbone-plus-reference).

| Part | Questions to answer | What you have at the end |
|---|---|---|
| Part 1: Find a good problem | What to do? Is it worth doing? Can it be done? | One sentence, a one-page project summary, an empty results table, and the research type you have identified |
| Part 2: Do the project | What evidence do you need? Which methods will get it? Where could your conclusions be wrong? Do you have the evidence? What does it show? | An evidence plan, an evidence-to-method table, a research plan, a threat-handling table, a smallest version that runs end to end, traceable results, a claim updated in light of the evidence |
| Writing and publishing | How do you explain it clearly? Where do you submit? How do you respond to reviewers? | A paper, submission materials, responses and a revised manuscript |

## 2. Each chapter: what it produces, and what you need before moving on

In each table below, "What it produces" is taken from the chapter's "What you should have at the end" section, and "Before moving on, at minimum" is the one or two most important items from its "Checklist before moving on". The chapters themselves have the full lists.

### Part 1: Find a good problem

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [1.1 Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md) | A list of core papers, notes on each, a problem log, a map of the field | You can explain in a few sentences how the research area breaks down; your problem log has a dozen or so questions, each noting its source |
| [1.2 Generating candidate problems](../01_find-a-problem/02_generate-problems.md) | A list of about ten ideas, and for each candidate, the quickest way to test it | The ideas come from at least three kinds of source, and for each one you can say what seems off |
| [1.3 Exploring hands-on](../01_find-a-problem/03_explore.md) | Exploration notes and a log of promising signs; what became of each idea you explored | You have tried each of your top few ideas once; for at least one, you have written a concrete hypothesis and can say what evidence would decide it |
| [1.4 Judging and screening ideas](../01_find-a-problem/04_judge-and-screen.md) | The two to four ideas left after a first screen, and why you crossed out the rest | You can say why you kept them; you have gone over them with your advisor or someone who knows the area |
| [1.5 Converging on a project](../01_find-a-problem/05_converge.md) (the core chapter) | A one-page project summary, a comparison table against the closest work, an empty results table, one small experiment already run, the result of the exit check | You can state your central claim in one sentence; you have tested the part you are least sure of, and it didn't sink the whole idea; your advisor has no fundamental objection; you have written down your main strategy and research type |

The key step in Part 1 is converging: turning "I'm interested in X" into "I want to prove this sentence". Once your central claim is settled, the strategy, evidence, and methods follow; for an example, see [Key concepts](key-concepts.md#one-example-the-same-research-area-four-different-studies).

### Part 2: Do the project

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [2.1 From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) | An evidence plan, a prediction table for each research question | Every research question has criteria for "counts as support" and "counts against", written before you look at the data |
| [2.2 Choosing a method](../02_do-the-project/02_choose-method.md) | An evidence-to-method table, a reading list for your methods | Every row of the evidence plan has a chosen method, and you have confirmed you can get the data, participants, or field sites it needs |
| [2.3 Writing a research plan](../02_do-the-project/03_research-plan.md) | A one- or two-page research plan, a paper outline | Every milestone is phrased as "what evidence will I have"; the first one is the milestone most likely to make the project fail; you have left slack |
| [2.4 Validity and limitations: think them through at the design stage](../02_do-the-project/04_validity-and-limits.md) | A list of reasons your conclusions could be wrong, a threat-handling table, a draft of your limitations | Every serious threat to validity has been removed or reduced, or the claim has been narrowed to match |
| [2.5 The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md) | A list of assumptions with test records, a smallest version that runs end to end, a revised design | The riskiest assumptions have all been tested; the whole pipeline has run from start to finish at the smallest scale |
| [2.6 Running and iterating](../02_do-the-project/06_run-and-iterate.md) | A research log, run records, a record of changes to the plan, weekly reports | You have the evidence your milestones call for (or have agreed with your advisor to change the claim); every result that goes into the paper can be traced to its code, data, and parameters |
| [2.7 Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md) | Data-checking records, an analysis checklist, a table matching conclusions to evidence, an updated one-page summary | Every conclusion points to its evidence, and the strength of each statement matches the evidence; every unplanned analysis is labeled exploratory |
| [2.8 Decision points: continue, adjust, or go back](../02_do-the-project/08_decision-points.md) | A decision log, and the paper skeleton updated after each decision | Every time you continue, you had criteria written down in advance; every time you go back, you can write down why the claim doesn't hold |

### Writing and publishing

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md) | A paper outline, a complete first draft, a claim-to-evidence table, a record of feedback from others | Every claim points to a specific figure, table, or section; at least one person who hadn't seen the draft has read it |
| [Choosing a venue and submitting](../03_write-and-publish/02_venue-and-submission.md) | A comparison table of candidate venues, a to-do list of submission requirements, a table of key dates after submission | You have checked formatting, anonymization, the preprint policy, and every required statement against the target venue's rules; all authors have agreed on authorship |
| [Reviews, revision, and what to do after rejection](../03_write-and-publish/03_review-and-revision.md) | A table of reviewer comments, an author response or response letter and a revised manuscript; after a rejection, a diagnosis and the next venue | Every comment has been categorized and decided on; for every issue that shakes the claim, you have either added evidence or changed the claim |

Writing and publishing comes last, but you should start writing during Part 1; see the next section.

## 3. A chain of outputs

What each chapter produces is the input to the next. Using this chain to check where you are is more accurate than counting how many months you have spent:

```
Part 1: map of the field → list of ideas → exploration notes → one sentence and a one-page summary
Part 2: → evidence plan → method design and milestones → list of threats → smallest version → results and analysis → paper skeleton
```

Here "method design and milestones" means the evidence-to-method table from 2.2 and the research plan from 2.3; "list of threats" means the list of reasons your conclusions could be wrong and the threat-handling table from 2.4; "smallest version" means the smallest version that runs end to end and the revised design from 2.5; "results and analysis" means traceable run records and the table matching conclusions to evidence; "paper skeleton" means the one-sentence claim, the results table, the evidence plan, and the list of contributions; see [2.8 The paper skeleton you keep up to date](../02_do-the-project/08_decision-points.md#4-the-paper-skeleton-you-keep-up-to-date).

You don't throw each output away once the next one is done. The one-page summary, the evidence plan, and the research plan keep being updated; once results come in, you will often go back and revise them.

**Use the chain backwards, too.** Think about the final paper from the very start of the project: put a paper outline in your first design document and use it to settle the research goals and the logical order of your experiments[^zhang2014ten-e8]. Drawing the empty results table while converging and writing a paper outline while planning both follow this idea; for details, see [Writing a research plan](../02_do-the-project/03_research-plan.md#2-break-the-claim-into-milestones-each-milestone-is-a-piece-of-evidence).

## 4. Research is a loop: when to go back

The picture in Section 1 mostly moves forward; the real path often loops back. Experiments will make you revise your paper draft[^eisnerfirst-e8]; finding that things are more complicated than you thought and going back to an earlier stage is completely normal and doesn't mean you have messed up[^nanda2025process-e6]. For the key moments in Part 2, what you should see before you continue, adjust, or go back to Part 1 is collected in [2.8 Decision points: continue, adjust, or go back](../02_do-the-project/08_decision-points.md).

What matters is knowing **where to go back to**. This table collects the most common cases from each chapter's "When to go back" section:

| Chapter you are in | If this happens | Go back to |
|---|---|---|
| 1.2 Generating candidate problems | Weeks of thinking and you can't write down a single idea | [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md): read another batch |
| 1.3 Exploring hands-on | You have explored every idea on your list and none of them teaches you anything new | [Generating candidate problems](../01_find-a-problem/02_generate-problems.md): look again, using a different kind of source |
| 1.4 Judging and screening ideas | You are unsure about several ideas and can't answer the screening questions | [Exploring hands-on](../01_find-a-problem/03_explore.md): try a few small things with them first |
| 1.5 Converging on a project | You can't write a concrete hypothesis or say what evidence you need | [Exploring hands-on](../01_find-a-problem/03_explore.md): try a few more small things |
| 1.5 Converging on a project | You know too little about the field to judge importance and novelty | [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md): read more, aimed at this problem |
| 1.5 Converging on a project | Every candidate conclusion turns out to have been done already | [Generating candidate problems](../01_find-a-problem/02_generate-problems.md) |
| 1.5 Converging on a project | The small experiment refuted your core hypothesis | Switch to another candidate: start with the others you kept in [Judging and screening ideas](../01_find-a-problem/04_judge-and-screen.md) |
| 2.1 From research questions to an evidence plan | While writing the "counts against" criteria, you realize you could read any result as support | [Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove), Section 1: the claim may be too vague or too sweeping |
| 2.2 Choosing a method | No method can get you one of the pieces of evidence | [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md): swap in evidence you can get |
| 2.3 Writing a research plan | Working backwards, you find there isn't enough time however much you narrow the claim | [Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove), Section 1: pick a smaller conclusion, or discuss a different venue with your advisor |
| 2.4 Validity and limitations | There is a threat that would invalidate the claim and you can't remove it | [Converging on a project](../01_find-a-problem/05_converge.md#1-write-down-the-sentence-you-want-to-prove), Section 1: narrow the claim or replace it |
| 2.5 The smallest version that runs end to end | A core assumption doesn't hold, for example the difference you wanted to measure barely exists | [2.8 Decision points](../02_do-the-project/08_decision-points.md#5-example-almost-no-leakage-turns-up-adjust-the-definition-or-change-the-problem): first decide whether to adjust the definition or go back to [Converging on a project](../01_find-a-problem/05_converge.md#judgment-calls) |
| 2.6 Running and iterating | A key part turns out to be infeasible, and you never tested it earlier | [The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md): test the remaining risks first |
| 2.6 Running and iterating | So much has changed that the original plan no longer fits | [Writing a research plan](../02_do-the-project/03_research-plan.md#7-how-the-plan-changes), Section 7: rework the plan starting from the claim |
| 2.7 Analysis and interpretation | There is a fatal alternative explanation your current design can't rule out | [Validity and limitations](../02_do-the-project/04_validity-and-limits.md): add to the design |
| 2.7 Analysis and interpretation | While exploring, you found a more interesting question | [Converging on a project](../01_find-a-problem/05_converge.md): treat it as a new candidate and discuss it with your advisor |
| Telling the story and writing the paper | While writing, you find a key experiment is missing and the claim doesn't hold up | [Running and iterating](../02_do-the-project/06_run-and-iterate.md): run the missing experiment |
| Choosing a venue and submitting | After reading papers from the target venue, you see your evidence clearly falls short | [Running and iterating](../02_do-the-project/06_run-and-iterate.md) to run more experiments, or narrow the claim |
| Reviews, revision, and what to do after rejection | Reviewers accept the problem but think the evidence doesn't support the conclusion | [Validity and limitations](../02_do-the-project/04_validity-and-limits.md), or [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) |
| Reviews, revision, and what to do after rejection | Reviewers agree it has been done before, or the contribution is too small | [Converging on a project](../01_find-a-problem/05_converge.md#3-has-someone-already-done-it), Section 3 |

The table shows that the place you are most often sent back to is [Converging on a project](../01_find-a-problem/05_converge.md): when the claim isn't thought through, the problems tend to surface only later. The writing row is especially common: laying out the whole paper ahead of time almost always reveals a few key experiments you still have to run[^karpathy2016survival-e9], which is why you should start writing early.

**Before you go back, write one sentence on why you are going back and what you need to answer there, and update your one-page summary and paper skeleton.** That way going back has a purpose instead of meaning starting over.

**Don't jump around aimlessly either.** Be decisive about dropping directions that don't look promising; but if you keep switching and never explore any of them properly, you learn nothing[^nanda2025mindsets-e1]. For when to persist and when to switch, see [Running and iterating](../02_do-the-project/06_run-and-iterate.md#6-persist-or-change-direction).

**The most common way newcomers get stuck** is thinking they should already have a clear hypothesis when they are actually still exploring[^nanda2025process-e2]. For how to tell these two stages apart and what to do in each, see [Exploring hands-on](../01_find-a-problem/03_explore.md).

## 5. Do the part most likely to fail first

Whatever chapter you are in, when you order your work, put first the parts that are most likely to fail and that give you an answer quickly: if they fail, you waste less, and you learn more, sooner[^steinhardt2018stochastic-e3]. This principle shows up three times across the two parts:

- When converging, test the part you are least sure of with the cheapest small experiment you can; see [Converging on a project](../01_find-a-problem/05_converge.md#5-can-you-actually-do-it);
- When planning, put first the milestone without which the whole project falls apart; see [Writing a research plan](../02_do-the-project/03_research-plan.md#4-set-the-order-do-what-is-most-likely-to-fail-first);
- Once the design is done and before the full study, run a small-scale pilot; see [The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md).

## 6. The Reference and things that run throughout

For what each part of the Reference (research types, Fields, research strategies, Throughout the project, FAQ) covers and when to use it, see [How to use this handbook](how-to-use.md#how-the-handbook-is-organized-a-two-part-backbone-plus-reference). Two more points here.

**Research strategies matter from reading the literature all the way to writing the paper**, not only when you choose a method; see [Why keep the strategy in mind from start to finish](../05_research-strategies/README.md#why-to-keep-your-strategy-in-mind-from-start-to-finish).

**Field conventions change the rhythm, not the two-part backbone.** For example, computer science may be the only discipline that uses conferences as its main publication venue[^vardi2009conferences-e1], so computer science projects are often planned backwards from a conference deadline; the steps of exploration and verification are the same, only the form and timing of the finish line differ. See [Computer science: field overview](../07_fields/computer-science/README.md#the-life-of-a-conference-paper).

The pages in [Throughout the project](../08_throughout/README.md) don't belong to any one chapter, but two things are best started on day one:

- **Stay aligned with your advisor.** Show your advisor what each chapter produces (list of ideas, summary, plan, design, results, drafts); see [Collaboration and advisors](../08_throughout/collaboration_and_advisors.md).
- **Make every result traceable to its source.** The minimum bar is that you yourself can roughly reproduce it a year later[^sandve2013ten-e2]; if you wait until you are writing the paper or responding to reviewers, it is often too late to reconstruct. See [Organizing your research materials](../08_throughout/organizing_materials.md).

Integrity and ethics questions (such as whether you need ethics review, or how to decide authorship) are also best considered at design time; see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md).

## 7. Roughly how long it takes

**Our sources give no general figure for how long a project takes from start to publication.** It depends on the research strategy, how the field publishes, and how many times you had to go back along the way. Rather than memorizing a number, learn to estimate: plan backwards from the submission deadline, measure how far off your own estimates tend to be, and leave slack for going back; for how, see [Writing a research plan](../02_do-the-project/03_research-plan.md#5-estimate-time-and-build-in-slack). For how to organize each day and week, see [Planning and daily routines](../08_throughout/planning_and_routines.md).

After you submit, some of the time is out of your hands: you wait for reviews, and after a rejection you revise and resubmit elsewhere. This varies a lot by field and venue; for the process, see [Choosing a venue and submitting](../03_write-and-publish/02_venue-and-submission.md#6-what-happens-after-you-submit).

## 8. Where are you now?

To find a starting point by situation, use the table in [How to use this handbook](how-to-use.md#where-you-are-which-page-to-read-first). Or find your position in the table below based on what you **already have**:

| What you have | Read first |
|---|---|
| A research area, but you can't name a few core papers | [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md) |
| You have read a batch of papers but can't say what you want to do | [Generating candidate problems](../01_find-a-problem/02_generate-problems.md) |
| A list of ideas you haven't tried out yet | [Exploring hands-on](../01_find-a-problem/03_explore.md) |
| A few ideas you have tried, and you don't know which to keep | [Judging and screening ideas](../01_find-a-problem/04_judge-and-screen.md) |
| Two or three candidates, but you can't say which sentence you want to prove | [Converging on a project](../01_find-a-problem/05_converge.md) |
| A one-page summary, but you can't say what evidence each claim needs | [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) |
| An evidence plan, but you don't know which methods will get the evidence | [Choosing a method](../02_do-the-project/02_choose-method.md) |
| You have chosen methods but don't know what to do first or when to deliver | [Writing a research plan](../02_do-the-project/03_research-plan.md) |
| A plan, but you haven't thought about where your conclusions could be wrong | [Validity and limitations: think them through at the design stage](../02_do-the-project/04_validity-and-limits.md) |
| A design, but you haven't yet tested the part you are least sure of | [The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md) |
| You are running experiments or collecting material | [Running and iterating](../02_do-the-project/06_run-and-iterate.md) |
| A pile of results, and you don't know what they show | [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md) |
| Results that differ from what you expected, and you can't tell whether to continue or go back | [Decision points: continue, adjust, or go back](../02_do-the-project/08_decision-points.md) |
| Your conclusions are clear and you need to write the paper | [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md) |
| The paper is written and you don't know where to submit | [Choosing a venue and submitting](../03_write-and-publish/02_venue-and-submission.md) |
| You have received reviews or a rejection letter | [Reviews, revision, and what to do after rejection](../03_write-and-publish/03_review-and-revision.md) |

If you are in a later chapter but find that an earlier output is missing (for example, you are running experiments but can't write a one-page summary), go back and fill it in first. The missing piece is often exactly why you are stuck now.

If you run into a specific difficulty, such as experiments that keep failing, a rejection, or trouble communicating with your advisor, you can also check [FAQ: quick answers](../faq.md) first.

**Write it down:** List the ten outputs in the chain from Section 3. Tick the ones you already have; next to each missing one, write "It's missing because...". Then write down the chapter you will read next.

## Next

- **Reading this handbook for the first time**: read [Key concepts](key-concepts.md) first, then start with [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md).
- **You already have a research area and a few ideas**: read [Exploring hands-on](../01_find-a-problem/03_explore.md) first, then go on to the core chapter, [Converging on a project](../01_find-a-problem/05_converge.md).
- **You are partway through a project**: use the table in Section 8 to find where you are; if you can't tell whether to continue or go back, read [Decision points](../02_do-the-project/08_decision-points.md).

[^zhang2014ten-e8]: Zhang 2014, Rule 1: Make It a Driving Force. [Evidence](../../sources/notes/zhang2014ten.md#e8)
[^eisnerfirst-e8]: Eisner, Write the Paper First, The document is like a code specification. [Evidence](../../sources/notes/eisnerfirst.md#e8)
[^nanda2025process-e2]: Nanda 2025, Exploration (Stage 2): Gain surface area. [Evidence](../../sources/notes/nanda2025process.md#e2)
[^nanda2025process-e6]: Nanda 2025, Distillation (Stage 4): Compress, Refine, Communicate. [Evidence](../../sources/notes/nanda2025process.md#e6)
[^nanda2025mindsets-e1]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e1)
[^karpathy2016survival-e9]: Karpathy 2016, Writing papers, "An internal deadlines 2 weeks prior". [Evidence](../../sources/notes/karpathy2016survival.md#e9)
[^steinhardt2018stochastic-e3]: Steinhardt 2018, Warm-Up. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e3)
[^vardi2009conferences-e1]: Vardi 2009, main text, para. 2. [Evidence](../../sources/notes/vardi2009conferences.md#e1)
[^sandve2013ten-e2]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e2)
