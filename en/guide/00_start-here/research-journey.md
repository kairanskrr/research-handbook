# The research journey at a glance: from interest to publication

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science.

Maybe you have just been handed a research area: say your advisor told you to "take a look at large language models and smart contract security". Or maybe you are already running experiments but can't say which stage you are at or how far you are from publishing.

This page is the map of the whole handbook: which chapters a study passes through on its way from a vague interest to publication, what each chapter produces, how far you need to get before moving on, and when to go back. The concrete steps are all in the chapters; this page only gives the route. For how to read the handbook and how each chapter is structured, see [How to use this handbook](how-to-use.md); for what we mean by research area, problem, claim, evidence, research strategy, and the other terms used here, see [Key concepts](key-concepts.md).

When you finish this page, you should be able to say which chapter you are in, what you are missing, and which chapter to read next.

---

## 1. The whole journey in one picture

```
  Part 1               Part 2                 Part 3                Part 4
  From interest   →   From project to    →   Running the study  →  Writing and
  to project          study design           and analyzing         publishing
  What to do          How to show it         Get the evidence      Tell others
       ↑                    ↑                      │                     │
       └────────────────────┴── results and reviews often send you back ─┘

  Look up any time: Research strategies · Research methods · Fields · Throughout the project · FAQ
```

Read the four Parts in order; the bottom line is the Reference, which you look up when you need it (see [How to use this handbook](how-to-use.md#the-handbook-has-two-layers-the-parts-and-the-reference)).

| Stage | Questions to answer | What you have at the end |
|---|---|---|
| Part 1: From interest to project | What to do? Is it worth doing? Can it be done? | A one-page project summary, a research plan |
| Part 2: From project to study design | What evidence do you need? Which methods will get it? Where could your conclusions be wrong? | An evidence plan, an evidence-to-method table, a threat-handling table, a piloted design |
| Part 3: Running the study and analyzing results | Do you have the evidence? What does it show? | Traceable results, a claim updated in light of the evidence |
| Part 4: Writing and publishing | How do you explain it clearly? Where do you submit? How do you respond to reviewers? | A paper, submission materials, responses and a revised manuscript |

`[Our analysis]`

## 2. Each chapter: what it produces, and what you need before moving on

In each table below, "What it produces" is taken from the chapter's "What you should have at the end" section, and "Before moving on, at minimum" is the one or two most important items from its "Checklist before moving on". The chapters themselves have the full lists `[Our analysis]`.

### Part 1: From interest to project

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md) | A list of core papers, notes on each, a problem log, a map of the field | You can explain in a few sentences how the research area breaks down; your problem log has a dozen or so questions, each noting its source |
| [Finding candidate problems](../01_from-interest-to-project/02_find-problems.md) | A list of about ten ideas, with two to four kept after a first screen | For each candidate you kept, you can say what is wrong, and you have planned a small test you can run in a week or two |
| [Converging on a project](../01_from-interest-to-project/03_converge.md) (the core chapter) | A one-page project summary, a comparison table against the closest work, an empty results table, one small experiment already run | You can state your central conclusion in one sentence; you have tested the part you are least sure of, and it didn't sink the whole idea; your advisor has no fundamental objection |
| [Writing a research plan](../01_from-interest-to-project/04_research-plan.md) | A one- or two-page research plan, a paper outline | Every milestone is phrased as "what evidence will I have"; the first one is the milestone most likely to make the project fail; you have left slack |

The key step in this stage is converging: turning "I'm interested in X" into "I want to prove this sentence". Once your central claim is settled, the strategy, evidence, and methods follow; for an example, see [Key concepts](key-concepts.md#one-example-the-same-research-area-four-different-studies).

### Part 2: From project to study design

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md) | An evidence plan, a prediction table for each research question | Every research question has criteria for "counts as support" and "counts against", written before you look at the data |
| [Choosing a strategy and a method](../02_from-project-to-study/02_choose-strategy-and-method.md) | An evidence-to-method table, a reading list for your methods | Every row of the evidence plan has a chosen method, and you have confirmed you can get the data, participants, or field sites it needs |
| [Validity and limitations: think them through at the design stage](../02_from-project-to-study/03_validity-and-limits.md) | A list of reasons your conclusions could be wrong, a threat-handling table, a draft of your limitations | Every serious threat to validity has been removed or reduced, or the claim has been narrowed to match |
| [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md) | A list of assumptions with test records, a minimal version that runs end to end, a revised design | The riskiest assumptions have all been tested; the whole pipeline has run from start to finish at the smallest scale |

`[Our analysis]`

### Part 3: Running the study and analyzing results

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md) | A research log, run records, a record of changes to the plan, weekly reports | You have the evidence your milestones call for (or have agreed with your advisor to change the claim); every result that goes into the paper can be traced to its code, data, and parameters |
| [Analysis and interpretation](../03_conduct-and-analyze/02_analyze-and-interpret.md) | Data-checking records, an analysis checklist, a table matching conclusions to evidence, an updated one-page summary | Every conclusion points to its evidence, and the strength of each statement matches the evidence; every unplanned analysis is labeled exploratory |

`[Our analysis]`

### Part 4: Writing and publishing

| Chapter | What it produces | Before moving on, at minimum |
|---|---|---|
| [Telling the story and writing the paper](../04_write-and-publish/01_story-and-paper.md) | A paper outline, a complete first draft, a claim-to-evidence table, a record of feedback from others | Every claim points to a specific figure, table, or section; at least one person who hadn't seen the draft has read it |
| [Choosing a venue and submitting](../04_write-and-publish/02_venue-and-submission.md) | A comparison table of candidate venues, a to-do list of submission requirements, a table of key dates after submission | You have checked formatting, anonymization, the preprint policy, and every required statement against the target venue's rules; all authors have agreed on authorship |
| [Reviews, revision, and what to do after rejection](../04_write-and-publish/03_review-and-revision.md) | A table of reviewer comments, an author response or response letter and a revised manuscript; after a rejection, a diagnosis and the next venue | Every comment has been categorized and decided on; for every issue that shakes the claim, you have either added evidence or changed the claim |

`[Our analysis]`

"Writing" is the last stage, but you should start writing in the first stage; see the next section.

## 3. A chain of outputs

What each chapter produces is the input to the next. Using this chain to check where you are is more accurate than counting how many months you have spent `[Our analysis]`:

```
one-page summary → research plan → evidence plan → study design → results → paper → response and revision
```

Here "study design" means the evidence-to-method table, the threat-handling table, and the design as revised after piloting; "results" means traceable run records and the table matching conclusions to evidence.

You don't throw each output away once the next one is done. The one-page summary and the plan keep being updated; once results come in, you will often go back and revise them `[Our analysis]`.

**Use the chain backwards, too.** Think about the final paper from the very start of the project: put a paper outline in your first design document and use it to settle the research goals and the logical order of your experiments[^zhang2014ten-e8]. Drawing the empty results table while converging and writing a paper outline while planning both follow this idea; for details, see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#2-break-the-claim-into-milestones-each-milestone-is-a-piece-of-evidence).

## 4. Research is a loop: when to go back

The picture in Section 1 is a straight line; the real path isn't. Experiments will make you revise your paper draft[^eisnerfirst-e8]; finding that things are more complicated than you thought and going back to an earlier stage is completely normal and doesn't mean you have messed up[^nanda2025process-e6]. What matters is knowing **where to go back to**. This table collects the most common cases from each chapter's "When to go back" section:

| Chapter you are in | If this happens | Go back to |
|---|---|---|
| Finding candidate problems | Weeks of thinking and you can't write down a single idea | [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md): read another batch |
| Converging on a project | You know too little about the field to judge importance and novelty | [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md): read more, aimed at this problem |
| Converging on a project | Every candidate conclusion turns out to have been done already | [Finding candidate problems](../01_from-interest-to-project/02_find-problems.md) |
| Converging on a project | The small experiment refuted your core assumption | Stay in this chapter and go back to [Section 1](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove) to pick a different candidate conclusion |
| Writing a research plan | Working backwards, you find there isn't enough time however much you narrow the claim | [Converging on a project](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove), Section 1: pick a smaller conclusion, or discuss a different venue with your advisor |
| From research questions to an evidence plan | While writing the "counts against" criteria, you realize you could read any result as support | [Converging on a project](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove), Section 1: the claim may be too vague or too sweeping |
| Choosing a strategy and a method | No method can get you one of the pieces of evidence | [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md): swap in evidence you can get |
| Validity and limitations | There is a threat that would invalidate the claim and you can't remove it | [Converging on a project](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove), Section 1: narrow the claim or replace it |
| Pilot first | A core assumption doesn't hold, for example the difference you wanted to measure barely exists | [Converging on a project](../01_from-interest-to-project/03_converge.md#1-write-down-the-sentence-you-want-to-prove): narrow the claim or replace it |
| Running and iterating | A key part turns out to be infeasible, and you never tested it earlier | [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md): test the remaining risks first |
| Running and iterating | So much has changed that the original plan no longer fits | [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#7-how-the-plan-changes), Section 7: rework the plan starting from the claim |
| Analysis and interpretation | There is a fatal alternative explanation your current design can't rule out | [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md): add to the design |
| Analysis and interpretation | While exploring, you found a more interesting question | [Converging on a project](../01_from-interest-to-project/03_converge.md): treat it as a new candidate and discuss it with your advisor |
| Telling the story and writing the paper | While writing, you find a key experiment is missing and the claim doesn't hold up | [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md): run the missing experiment |
| Choosing a venue and submitting | After reading papers from the target venue, you see your evidence clearly falls short | [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md) to run more experiments, or narrow the claim |
| Reviews, revisions, and rejection | Reviewers accept the problem but think the evidence doesn't support the conclusion | [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md), or [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md) |
| Reviews, revisions, and rejection | Reviewers agree it has been done before, or the contribution is too small | [Converging on a project](../01_from-interest-to-project/03_converge.md#3-has-someone-already-done-it), Section 3 |

The table shows that the place you are most often sent back to is [Converging on a project](../01_from-interest-to-project/03_converge.md): when the claim isn't thought through, the problems tend to surface only later `[Our analysis]`. The writing row is especially common: laying out the whole paper ahead of time almost always reveals a few key experiments you still have to run[^karpathy2016survival-e9], which is why you should start writing early.

**Before you go back, write one sentence on why you are going back and what you need to answer there, and update your one-page summary.** That way going back has a purpose instead of meaning starting over `[Our analysis]`.

**Don't jump around aimlessly either.** Be decisive about dropping directions that don't look promising; but if you keep switching and never explore any of them properly, you learn nothing[^nanda2025mindsets-e1]. For when to persist and when to switch, see [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md#6-persist-or-change-direction).

**The most common way newcomers get stuck** is thinking they should already have a clear hypothesis when they are actually still exploring[^nanda2025process-e2]. For how to tell these two stages apart and what to do in each, see [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md#1-first-know-which-stage-you-are-in).

## 5. Do the part most likely to fail first

Whatever chapter you are in, when you order your work, put first the parts that are most likely to fail and that give you an answer quickly: if they fail, you waste less, and you learn more, sooner[^steinhardt2018stochastic-e3]. This principle appears three times in the Parts `[Our analysis]`:

- When converging, test the part you are least sure of with the cheapest small experiment you can; see [Converging on a project](../01_from-interest-to-project/03_converge.md#5-can-you-actually-do-it);
- When planning, put first the milestone without which the whole project falls apart; see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#4-set-the-order-do-what-is-most-likely-to-fail-first);
- Once the design is done and before the full study, run a pilot study; see [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md).

## 6. The Reference and things that run throughout

For what each part of the Reference (research strategies, research methods, Fields, FAQ) covers and when to use it, see [How to use this handbook](how-to-use.md#the-handbook-has-two-layers-the-parts-and-the-reference). Two more points here.

**Research strategies matter from reading the literature all the way to writing the paper**, not only when you choose a method; see [Why keep the strategy in mind from start to finish](../05_research-strategies/README.md#why-to-keep-your-strategy-in-mind-from-start-to-finish).

**Field conventions change the rhythm, not the route.** For example, computer science may be the only discipline that uses conferences as its main publication venue[^vardi2009conferences-e1], so computer science projects are often planned backwards from a conference deadline; the four stages are still the same four, only the form and timing of the finish line differ `[Our analysis]`. See [Computer science: field overview](../07_fields/computer-science/README.md#the-life-of-a-conference-paper).

The pages in [Throughout the project](../08_throughout/README.md) don't belong to any one chapter, but two things are best started on day one `[Our analysis]`:

- **Stay aligned with your advisor.** Show your advisor what each chapter produces (summary, plan, design, results, drafts); see [Collaboration and advisors](../08_throughout/collaboration_and_advisors.md).
- **Make every result traceable to its source.** The minimum bar is that you yourself can roughly reproduce it a year later[^sandve2013ten-e2]; if you wait until you are writing the paper or responding to reviewers, it is often too late to reconstruct. See [Organizing your research materials](../08_throughout/organizing_materials.md).

Integrity and ethics questions (such as whether you need ethics review, or how to decide authorship) are also best considered at design time; see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md).

## 7. Roughly how long it takes

**Our sources give no general figure for how long a project takes from start to publication.** It depends on the research strategy, how the field publishes, and how many times you had to go back along the way `[Our analysis]`. Rather than memorizing a number, learn to estimate: plan backwards from the submission deadline, measure how far off your own estimates tend to be, and leave slack for going back; for how, see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#5-estimate-time-and-build-in-slack). For how to organize each day and week, see [Planning and daily routines](../08_throughout/planning_and_routines.md).

After you submit, some of the time is out of your hands: you wait for reviews, and after a rejection you revise and resubmit elsewhere. This varies a lot by field and venue; for the process, see [Choosing a venue and submitting](../04_write-and-publish/02_venue-and-submission.md#6-what-happens-after-you-submit).

## 8. Where are you now?

Find your position in the table below based on what you **already have** `[Our analysis]`:

| What you have | Read first |
|---|---|
| A research area, but you can't name a few core papers | [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md) |
| You have read a batch of papers but can't say what you want to do | [Finding candidate problems](../01_from-interest-to-project/02_find-problems.md) |
| A few ideas, but you can't say which sentence you want to prove | [Converging on a project](../01_from-interest-to-project/03_converge.md) |
| A one-page summary, but you don't know what to do first or when to deliver | [Writing a research plan](../01_from-interest-to-project/04_research-plan.md) |
| A plan, but you can't say what evidence each claim needs | [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md) |
| An evidence plan, but you don't know which methods will get the evidence | [Choosing a strategy and a method](../02_from-project-to-study/02_choose-strategy-and-method.md) |
| You have chosen methods but haven't thought about where your conclusions could be wrong | [Validity and limitations: think them through at the design stage](../02_from-project-to-study/03_validity-and-limits.md) |
| A design, but you haven't yet tested the part you are least sure of | [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md) |
| You are running experiments or collecting material | [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md) |
| A pile of results, and you don't know what they show | [Analysis and interpretation](../03_conduct-and-analyze/02_analyze-and-interpret.md) |
| Your conclusions are clear and you need to write the paper | [Telling the story and writing the paper](../04_write-and-publish/01_story-and-paper.md) |
| The paper is written and you don't know where to submit | [Choosing a venue and submitting](../04_write-and-publish/02_venue-and-submission.md) |
| You have received reviews or a rejection letter | [Reviews, revision, and what to do after rejection](../04_write-and-publish/03_review-and-revision.md) |

If you are in a later chapter but find that an earlier output is missing (for example, you are running experiments but can't write a one-page summary), go back and fill it in first. The missing piece is often exactly why you are stuck now `[Our analysis]`.

If you run into a specific difficulty, such as experiments that keep failing, a rejection, or trouble communicating with your advisor, you can also check [FAQ: quick answers](../faq.md) first.

**Write it down:** List the seven outputs in the chain from Section 3. Tick the ones you already have; next to each missing one, write "It's missing because...". Then write down the chapter you will read next.

## Next

- **Reading this handbook for the first time**: read [Key concepts](key-concepts.md) first, then start with [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md).
- **You already have a research area and a few ideas**: go straight to the core chapter, [Converging on a project](../01_from-interest-to-project/03_converge.md).
- **You are partway through a project**: use the table in Section 8 to find where you are.

[^zhang2014ten-e8]: Zhang 2014, Rule 1: Make It a Driving Force. [Evidence](../../sources/notes/zhang2014ten.md#e8)
[^eisnerfirst-e8]: Eisner, Write the Paper First, The document is like a code specification. [Evidence](../../sources/notes/eisnerfirst.md#e8)
[^nanda2025process-e2]: Nanda 2025, Exploration (Stage 2): Gain surface area. [Evidence](../../sources/notes/nanda2025process.md#e2)
[^nanda2025process-e6]: Nanda 2025, Distillation (Stage 4): Compress, Refine, Communicate. [Evidence](../../sources/notes/nanda2025process.md#e6)
[^nanda2025mindsets-e1]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e1)
[^karpathy2016survival-e9]: Karpathy 2016, Writing papers, "An internal deadlines 2 weeks prior". [Evidence](../../sources/notes/karpathy2016survival.md#e9)
[^steinhardt2018stochastic-e3]: Steinhardt 2018, Warm-Up. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e3)
[^vardi2009conferences-e1]: Vardi 2009, main text, para. 2. [Evidence](../../sources/notes/vardi2009conferences.md#e1)
[^sandve2013ten-e2]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e2)
