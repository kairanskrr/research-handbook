# Entering a field and exploring the literature

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

> **What you must do in this chapter**
>
> 1. **Start with what others have already organized.** Look for surveys, tutorials, and course syllabi; if there are none, try a few sets of keywords and find three to five recent papers to start from ([Section 2](#2-start-with-what-others-have-already-organized)).
> 2. **Follow the citations to the core papers.** Go backward through the references and forward to the papers that cite them, and note the papers, people, and venues that keep coming up; stop when most of what you find is already familiar ([Section 3](#3-follow-the-citations-to-find-the-core-papers-key-people-and-venues)).
> 3. **Give most papers one pass; read two or three in depth.** The first pass takes only 5 to 10 minutes and decides whether to read on; the few you read in depth, read until you understand every sentence ([Section 4](#4-read-in-layers-most-papers-once-a-few-in-depth)).
> 4. **Keep a problem log as you read.** Whenever something seems wrong, unclear, or inconsistent, write one sentence on the spot and note where it came from. This is the raw material for the next chapter ([Section 6](#6-take-notes-one-per-paper-plus-a-problem-log)).
> 5. **Draw a map of the field and show it to your advisor.** Rows are sub-problems, columns are research strategies; see where it's crowded and where it's empty, and ask your advisor what you missed ([Section 7](#7-draw-a-map-of-the-field), [Section 8](#8-talk-to-people-who-know-the-area)).
>
> **Done these? Move on:** you can explain which parts the research area breaks into, you have read two or three papers in depth, your problem log has a dozen or so questions with their sources, and your advisor has seen your map. Don't wait until you "understand everything". Next: [Generating candidate problems](02_generate-problems.md).

## Where you are

You have a research area. Maybe your advisor said "take a look at large language models and smart contract security", or maybe you are interested in it yourself. But you don't know much about it yet: you aren't sure what people are working on, which papers to read, who the main researchers are, or where the papers get published.

You open a scholarly search engine and get hundreds or thousands of results. You click one at random, spend two hours on it, still don't really understand it, and can't tell whether it matters.

## What this stage is for

In limited time, build a **working understanding** of the research area. Concretely, come away with these five things:

1. **A map of the field**: which parts the research area breaks into, and what problem each part works on and with what approaches;
2. **A list of core papers**: which papers are cited again and again, and a few of them that you have read in depth;
3. **People and venues**: who works in this research area, and which conferences or journals the papers mainly appear in;
4. **Notes on each paper**: notes you can still understand when you open them months later;
5. **A problem log**: the things you noticed while reading that seemed wrong, not good enough, or unanswered. It is the raw material for the next chapter, [Generating candidate problems](02_generate-problems.md).

By "problem" we mean something in the field that is wrong, not good enough, or not yet known; see [Key concepts](../00_start-here/key-concepts.md#problem).

**What this chapter doesn't teach:** a review that is a research output in its own right has to find all the relevant work through a reproducible process; for that, see [Review studies](../06_methods/review_study.md).

## How to use this chapter

The eight sections below roughly go in order, but reading, searching, note-taking, and asking people happen in turns: a good paper leads you to new papers through its references, and one conversation might change your whole set of search terms.

**Put a time limit on this stage.** Don't let background reading drag on forever. You can only start your own work while you still half-understand the area, because there isn't time to learn everything you would need to know[^eisnerproblems-e8]. Agree on how long with your advisor; our suggestion is to work in rounds of a few weeks and check yourself against the checklist at the end of this chapter when each round ends.

---

## 1. First, write down what you want from the literature

**Before you search for papers, spend half an hour writing down what you want to know.** If you don't, the search results will lead you around and you will end up reading a pile of papers that have nothing to do with you.

Break the research area into a few specific questions. For "large language models and smart contract security":

- What are large language models being used for here? Finding vulnerabilities, fixing them, writing safer contracts, or something else?
- How well does it work right now? How is it evaluated? On what data?
- Compared with traditional vulnerability detection tools (such as static analysis and fuzzing), what are the strengths and weaknesses of each?
- What hard problems does everyone agree are still unsolved?

These questions will change as you read. Their job is to make sure that each time you read a paper, you know what you are looking for.

**Write it down:** In three to five questions, write down "what I want to figure out from the literature in this research area", then one sentence: "how long I plan to spend on this round".

## 2. Start with what others have already organized

**Don't start by reading research papers one by one.** First check whether someone has already put together a reading list for you, such as a course syllabus or the literature review chapter of a thesis[^eisnerread-e12], or the tutorials and surveys described below.

The two kinds of overview articles serve different purposes:

| Type | Written for | What you get from it |
|---|---|---|
| Tutorial | Non-specialists; explains basic concepts with concrete examples[^acm2026csurguidelines-e2] | An entry point: the basic terms and basic techniques |
| Survey | Readers with a general understanding; focuses on classifying existing work, offering a view of the research area, and assessing trends[^acm2026csurguidelines-e1] | A map: which parts the research area breaks into, and the representative papers in each |

If you aren't even familiar with smart contracts themselves, start with a tutorial or introductory material on smart contract security; if the basic concepts are already clear, go straight to a survey.

**If there's no survey, find your own starting papers.** Use a scholarly search engine (such as Google Scholar) and a few well-chosen keywords to find three to five recent papers[^keshav2007read-e9]. When you pick keywords, put yourself in the authors' shoes: what words would they use to describe this problem[^eisnerread-e10]? The same thing may be called "vulnerability detection" by some, "security auditing" by others, and some will just name a vulnerability class (such as "reentrancy"). Try both Chinese and English terms, and both abbreviations and full names.

**Watch the dates.** Large language models move fast; a survey from a few years ago may already miss the latest wave of work, so fill the gap with recent papers. New work often appears first as a preprint on arXiv (a preprint server); arXiv only classifies submissions and checks them for basic scholarly value, and **does not do peer review**[^arxivabout-e2]. Preprints let you see the latest progress, but read them more cautiously than formally published papers.

**Write it down:** List how many surveys, tutorials, and course syllabi you found; if there are none, list three to five starting papers and every set of keywords you tried.

## 3. Follow the citations to find the core papers, key people, and venues

Once you have starting points, expand outward like a snowball:

1. **Read the related-work sections of your starting papers.** In their references, look for papers cited again and again and author names that keep appearing; those are the key papers and key researchers in this research area[^keshav2007read-e10].
2. **Follow citations in both directions.** Once you find a relevant paper, go backward through its references and forward to the papers that cite it[^eisnerread-e11]. Taking a key paper and doing a citation search on it, to see which later papers cite it, is a good way to learn a field[^taocareer-e16].
3. **Identify the few top conferences and go through their recent proceedings.** If these new papers all cite a key paper you haven't found yet, get it and read it, and do another round if needed[^keshav2007read-e11].
4. **Go broad, then deep.** Read lots of abstracts first, skim the full text when needed, and then decide which are most worth reading closely[^eisnerread-e13].

**Step 3, going through conferences, is how computer science works.** Computer science treats conference papers as the main way to publish research results; as far as Moshe Vardi, editor-in-chief of *Communications of the ACM* (the Association for Computing Machinery), knows, this is unique among disciplines[^vardi2009conferences-e1]. So in computer science, "main venues" usually means a handful of conferences. Some research areas have widely recognized top conferences, such as the "top 4" venues people talk about in security; they are the most influential and de facto set the community's benchmarking practices[^vanderkouwe2019sok-e27]. Our sources do not check, field by field, where other disciplines mainly publish or which journals or conferences they follow; ask your advisor, or look at where the papers you have collected were mostly published. For more on computer science's conference culture, see [Computer science: field overview](../07_fields/computer-science/README.md).

**For key people, know more than the name**: which group they belong to, which part of the area that group mainly works on, and what they have published in the last year or two. Their research group's homepage sometimes lists all of the group's papers.

**Keep up with new papers.** You can subscribe to the arXiv subject categories you care about and get notified when new papers appear[^taocareer-e27].

**When to stop:** after several rounds, once the key papers cited by the new papers you find are all ones you have already seen, you can stop this round.

**Write it down:** Start a list of core papers, one per row: title, authors, year, venue, how many of your other papers cite it, and how many passes you have made through it. Then list three to five key researchers and two or three main venues.

## 4. Read in layers: most papers once, a few in depth

**Don't force your way through every paper from the first page to the last.** Read in up to three passes, each with its own goal, each building on the one before[^keshav2007read-e1]:

| | First pass | Second pass | Third pass |
|---|---|---|---|
| Time | 5 to 10 minutes[^keshav2007read-e2] | Up to an hour[^keshav2007read-e6] | Four or five hours for a beginner, about an hour for an experienced reader[^keshav2007read-e8] |
| What to read | Title, abstract, introduction, section and subsection headings, conclusion[^keshav2007read-e3] | Read more carefully but skip details such as proofs; note the key points as you go[^keshav2007read-e5] | Pretend you are the author and recreate the work in your head, then compare with the original[^keshav2007read-e7] |
| Afterwards you should be able to | Say what kind of paper it is, which work it relates to, whether its assumptions appear to hold, what its main contributions are, and whether it is clearly written[^keshav2007read-e4] | Summarize the paper's main thrust and supporting evidence to someone else[^keshav2007read-e6] | Reconstruct the paper's structure from memory and point out its strengths and weaknesses[^keshav2007read-e8] |

On the first pass, skip the parts that take hard thinking; all you want is to know what the paper is about, why it was written, and what is new to you[^eisnerread-e1]. One job of the first pass is to decide whether to read any further[^keshav2007read-e2].

**When you enter a new research area, read at least a few papers in depth.** Read them until you understand what every sentence and every symbol is doing; only then do you really learn the techniques this research area relies on[^eisnerread-e7]. Which ones to read in depth: one or two surveys or the most-cited classic papers, plus one or two recent papers closest to your own interest.

**You can go one step further: reproduce a paper.** Reproducing or reimplementing someone else's work won't earn you points for originality, but it is useful for your own learning and sometimes for the field[^eisnerproblems-e1]. For example, rerun the experiments of a paper that uses large language models to detect contract vulnerabilities on a small dataset, and you will understand its data, prompts, and evaluation better than if you had read it ten times.

**Reading slowly is nothing to be ashamed of.** Experienced researchers also take several hours to read a paper outside their own area[^eisnerread-e9]. When you can't tell what matters in a paper, find papers that cite it and see what others say about it[^eisnerread-e14].

**Write it down:** In your list of core papers, mark the two to four you plan to read in depth, and write down why you chose them.

## 5. Read with questions in mind

If you just follow the author's line of thought, you often come away remembering only what the author wanted you to remember. Read actively: look for the assumptions the paper doesn't state, including how the problem was framed and how it gets from the evidence to the conclusions. This isn't the same as nitpicking. You may end up liking the paper or not, but you will know more clearly why[^bender2003critical-e1][^bender2003critical-e2].

**For every paper worth a second pass, answer these questions:**

1. **What problem is it trying to solve?** Look at two levels: what real-world benefit is wanted, and why the problem has no easy solution. These are often not stated outright; you have to dig them out yourself[^griswoldread-e1][^griswoldread-e2].
2. **What assumptions are built into asking the question this way? How were the data collected, and what biases might they have?**[^bender2003critical-e3]
3. **How does it show its idea is worth something?** By argument, by implementation, or by experiment[^griswoldread-e3]? Is the comparison fair? Do the results really support the paper's claims? Do they generalize beyond the experimental setting[^eisnerread-e8]?
4. **What kind of result is it?** Classify it by the research strategies in [Key concepts](../00_start-here/key-concepts.md#research-strategy) (Building and improving, Comparative evaluation, Measurement...). Then look at how certain it is: a well-established finding, an observation of real-world phenomena, or the authors' rule of thumb from experience[^shaw2002makes-e5]? In research areas where no established findings exist yet, observations and rules of thumb are valuable too[^shaw2002makes-e6], but you should know which one you are reading.
5. **Is the evidence solid enough?** Good research needs clear, convincing evidence, based on experience in actual use or on systematic analysis, not just persuasive argument or textbook examples[^shaw2002makes-e7].

For papers on using large language models to detect contract vulnerabilities, questions 2 and 3 become concrete: had the model already seen the evaluation contracts during training? Which traditional tools did it compare against, and was the setup the same for each? Did it test only one class of vulnerability, or many?

**Read creatively, not just critically.** Tearing something down is always easier than building. The harder question is: what good ideas are in this paper, and where else could they be used[^eisnerread-e6]? Three useful questions: if a panel of reviewers grilled you about this paper, which question couldn't you answer[^vinitskypaper-e6]? What extra experiment would I run to make it more convincing[^vinitskypaper-e7]? If I started a new project based on it, what would I do[^vinitskypaper-e8]?

**Write it down:** For each paper you plan to read in depth, write answers to the five questions above. If you can't answer one, you haven't finished reading the paper[^griswoldread-e6].

## 6. Take notes: one per paper, plus a problem log

Writing as you read keeps your attention focused and forces you to engage actively[^eisnerread-e2]. Margin notes alone are not enough; you also need high-level notes that distill the paper, compare it with other papers, and record your own questions and ideas[^eisnerread-e4]. Without them, it is easy to read for an hour or two and find you have learned nothing[^vinitskypaper-e1].

**One set of notes per paper.** You can use this template as is:

> **Source**: authors, year, title, venue, link
>
> **Why I'm reading it**: which of my questions (Section 1) it relates to
>
> **One-sentence summary**: what it shows
>
> **Classification**: which research strategy it belongs to; whether its certainty is a finding, an observation, or a rule of thumb
>
> **Evidence**: what data it used, what it compared against, its main results
>
> **My view**: what is good about it, what is doubtful
>
> **What I didn't understand**
>
> **Questions it raised for me**

A few points:

- **Fill in "Why I'm reading it" before you read.** If you can't, maybe you shouldn't read it[^vinitskypaper-e2].
- **Scale your summaries.** For most papers, one sentence; a paragraph when needed; a full summary only for a very few[^vinitskypaper-e3].
- **Write in your own words, for yourself a few months from now.** When you reread your notes, you should be able to recover your understanding quickly[^eisnerread-e5]. Don't paraphrase the abstract; summarize from your own point of view[^griswoldread-e7].
- **Collect what you didn't understand in one place** so you can come back to it later[^vinitskypaper-e4].

**Keep a separate "problem log". It is one of this chapter's most important outputs.** While you read, write down anything that seems wrong, unclear, or inconsistent the moment it comes up. Writing your questions down often brings out things you hadn't thought through, such as a paper being vague on a key point, or ignoring something you think matters[^griswoldread-e8].

All this chapter asks is that you **jot things down as they come**: one sentence each, noting which paper it came from, with no need to judge on the spot whether it is worth pursuing. Keeping interesting things together in one document makes it easier to spot connections between them[^nanda2025process-e4]. For what exactly to look for when reading papers (the authors' simplifications, the assumptions behind the work, the way it is evaluated), see [Section 2](02_generate-problems.md#2-method-1-gap-spotting) and [Section 3](02_generate-problems.md#3-method-2-questioning-assumptions-problematization) of the next chapter; for how to turn this log into a list of ideas with sources and ways to test them, see [Section 7](02_generate-problems.md#7-keep-a-list-of-ideas).

**Write it down:** Set up your paper-notes template and your problem log. By the end of this round of the chapter, your problem log should have a dozen or so entries.

## 7. Draw a map of the field

Once you have read ten or twenty papers, look at them side by side. **A map is not a list of papers; it is a classification.** One simple way to draw it: rows are the sub-problems of the research area, columns are research strategies, and each cell holds the representative papers.

Here is an illustration (the cells should hold the papers you actually read; this only shows the format):

| Sub-problem | Building and improving | Comparative evaluation | Measurement | Description |
|---|---|---|---|---|
| Using large language models to find vulnerabilities | Papers A, B | Paper C | | |
| Using large language models to fix vulnerabilities | Paper D | | | |
| Benchmark data and metrics | | | Paper E | |
| Whether contracts generated by large language models are themselves secure | | | | Paper F |

Once it's drawn, look for three things:

- **Which cells are crowded?** Many people are working there and competition is fierce, so you need to be especially clear about how your work differs;
- **Which cells are empty?** Maybe nobody has thought of it, or maybe it can't be done or isn't worth doing; ask someone who knows the area;
- **Which ideas have caught on, and which have been forgotten?** Taste in choosing problems develops slowly as you watch which ideas flourish and which are forgotten[^schulman2020opinionated-e3]. The easiest ways to build judgment are to lean on your advisor and to see what has worked in papers[^nanda2025taste-e5].

You can also do what a survey does: classify the existing work, form your own view of the research area, and spot the trends[^acm2026csurguidelines-e1]. Your map is a small survey written only for yourself.

**Write it down:** Draw your map of the field, and below it write three to five sentences on the landscape you see: where it's crowded, where it's empty, what's changing.

## 8. Talk to people who know the area

The literature is only half of it. **Your advisor is one of your best sources of guidance**: not only do they help with your research directly, they will also point you, explicitly or implicitly, toward relevant researchers, conferences, papers, open problems, and the folklore of the field[^taocareer-e23].

Concrete things you can do:

- **Take your map and problem log to your advisor.** Think on your own as you read, and regularly run your ideas past people who can remind you of related work and point you to papers[^eisnerproblems-e9]. Bringing something concrete is far more useful than asking "what should I read?".
- **Ask the researchers around you how they chose their problems.** Why are they working on what they are working on now? How did they pick it[^olah2021taste-e6]?
- **Help out a senior student.** In your first year, find an older student whose project interests you and offer to help[^dredze2012successful-e18]. Helping someone else with a project in an area you care about teaches you a lot without tying you down long term[^olah2021taste-e17].
- **Go to talks.** Don't expect to follow everything in every talk, especially outside your area; as long as you learn something, it wasn't a waste[^taocareer-e33].

For why you can't just shut the door and read, and how talking to people helps you find problems, see [Talk to people](02_generate-problems.md#talk-to-people) in the next chapter. The point of talking to people in this chapter is **to complete your map**.

When you talk, you can ask directly: What is my map missing? Which papers must I read in depth? Which items in my problem log have already been done, and which do you think are worth thinking about?

**Write it down:** After each conversation, note the papers and people they recommended, the gaps they pointed out, and what they thought of your problem log, then update your map and paper list.

---

## Judgment calls

**How much reading is enough before you start looking for problems?** Not "when I've read everything", but:

| You can | Which means |
|---|---|
| Explain to a classmate, in a few sentences, which parts the research area breaks into | You have a map |
| Say what three to five core papers each show and what their evidence is | You have read a few in depth |
| Find that most newly found papers are already on your list | You have found most of the core literature |
| Point to a dozen or so specific questions in your problem log | You have raw material for finding problems |

If you can't do the first, keep reading; once you can do all four, move to the next chapter. Don't wait until you "understand everything".

> **Where sources disagree: read a lot first, or think on your own first?**
> - **Think first:** Varian argues that you will of course need a thorough literature search eventually, but you will do much better if you spend a few weeks working on your own ideas before searching systematically[^varian1997build-e3]. Eisner also says not to let background reading drag on, but to start thinking for yourself early and alternate thinking with reading[^eisnerproblems-e8][^eisnerproblems-e9].
> - **Check first:** Noble warns of a terrible trap: you finish an entire project and only then find that someone published the same work before you began. So do your literature review up front[^noble2023ten-e5].
>
> We read the two pieces of advice as addressing different moments: **when you are looking for ideas**, read until you have enough (a map and a few papers read in depth), then start thinking on your own and keep reading as you think; **before you commit to a specific project**, you must do a careful check for prior work on that project; see [Converging on a project](05_converge.md#3-has-someone-already-done-it).

**What this kind of reading can and can't be used for.** Picking papers purposefully the way you are doing here is the same way most papers write their related-work sections. It is good for finding promising topics; but it has sampling bias, it can't be reproduced, and it makes it easy to cherry-pick evidence that suits you, so **it can't support empirical conclusions like "X causes Y"**[^ralph2022paving-e1][^ralph2022paving-e2]. If your question itself requires finding all the relevant studies, you need a systematic review; see [Review studies](../06_methods/review_study.md).

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Starting by reading research papers one by one | A survey or course syllabus may well have organized them for you already[^eisnerread-e12] |
| Searching with only one keyword | Authors may use different terms; think from their side about wording, and follow citations in both directions[^eisnerread-e10][^eisnerread-e11] |
| Reading every paper word for word from start to finish | Time goes into papers that don't need a deep read; read in passes and decide after each whether to continue[^keshav2007read-e1][^keshav2007read-e2] |
| Only ever skimming | You never learn the core techniques of the research area[^eisnerread-e7] |
| Treating preprints as peer-reviewed conclusions | arXiv does not do peer review[^arxivabout-e2] |
| Annotating papers but writing no high-level notes | Months later you can't recover your understanding[^eisnerread-e4][^eisnerread-e5] |
| Not noting questions while reading | In the next chapter you have no raw material for finding problems and must reread from scratch |
| Reading but never talking to anyone | You miss related work that someone in the area could have told you about in one sentence[^eisnerproblems-e9] |
| Wanting to read everything before starting | You can never read it all; you have to start while you only half-understand[^eisnerproblems-e8] |
| Using hand-picked literature to show "X causes Y" | A non-systematic review has sampling bias and can't support empirical conclusions[^ralph2022paving-e2] |

## What you should have at the end

- A list of "what I want to figure out from the literature" (Section 1)
- A list of core papers, with the ones you read in depth marked (Sections 3 and 4)
- A list of key researchers and main venues (Section 3)
- Notes on every paper you read (Section 6)
- A problem log (Section 6)
- A map of the field, plus three to five sentences on the landscape (Section 7)
- Notes from conversations with your advisor or people who know the area (Section 8)

## Checklist before moving on

You are ready for the next step when:

- [ ] You can explain in a few sentences which parts the research area breaks into and what each part works on
- [ ] You have read at least two or three papers in depth and can state their problems, their evidence, and their hidden assumptions
- [ ] You can name a few key researchers and two or three main venues
- [ ] Most newly found papers are already on your list
- [ ] Your problem log has a dozen or so specific questions, each noting its source
- [ ] Your advisor or someone who knows the area has looked at your map, and you have filled the gaps they pointed out

## When to go back

| If this happens | Go back to |
|---|---|
| Your searches return too many, too scattered papers to draw a map | Section 1 of this chapter: with your advisor, narrow the research area to one or two sub-problems |
| You can hardly find any relevant papers | Section 2 of this chapter: change your keywords and ask your advisor; the work in this research area may also be scattered across neighboring fields |
| You have been reading for a long time and your problem log is still empty | Sections 5 and 6 of this chapter: reread a few core papers with questions in mind |
| After reading, you find you have no interest at all in this research area | Talk to your advisor and consider switching areas; don't just grit your teeth |
| In the next chapter or while converging, you find you know too little about the field to judge importance and novelty | Come back to this chapter and read another batch aimed at that problem |

## Next

With a map, core papers, and a problem log in hand, the next step is to generate a batch of candidate problems from them; see [Generating candidate problems](02_generate-problems.md).

[^eisnerproblems-e1]: Eisner, How to Find Research Problems, small bones. [Evidence](../../sources/notes/eisnerproblems.md#e1)
[^eisnerproblems-e8]: Eisner, How to Find Research Problems, Finally. [Evidence](../../sources/notes/eisnerproblems.md#e8)
[^eisnerproblems-e9]: Eisner, How to Find Research Problems, Finally. [Evidence](../../sources/notes/eisnerproblems.md#e9)
[^eisnerread-e1]: Eisner 2009, Multi-pass reading. [Evidence](../../sources/notes/eisnerread.md#e1)
[^eisnerread-e2]: Eisner 2009, Write as you read. [Evidence](../../sources/notes/eisnerread.md#e2)
[^eisnerread-e4]: Eisner 2009, High-level notes. [Evidence](../../sources/notes/eisnerread.md#e4)
[^eisnerread-e5]: Eisner 2009, High-level notes. [Evidence](../../sources/notes/eisnerread.md#e5)
[^eisnerread-e6]: Eisner 2009, High-level notes (quoting Mitzenmacher). [Evidence](../../sources/notes/eisnerread.md#e6)
[^eisnerread-e7]: Eisner 2009, Which parts to focus on. [Evidence](../../sources/notes/eisnerread.md#e7)
[^eisnerread-e8]: Eisner 2009, Which parts to focus on — Experiments. [Evidence](../../sources/notes/eisnerread.md#e8)
[^eisnerread-e9]: Eisner 2009, Set aside time. [Evidence](../../sources/notes/eisnerread.md#e9)
[^eisnerread-e10]: Eisner 2009, What to read. [Evidence](../../sources/notes/eisnerread.md#e10)
[^eisnerread-e11]: Eisner 2009, What to read. [Evidence](../../sources/notes/eisnerread.md#e11)
[^eisnerread-e12]: Eisner 2009, What to read. [Evidence](../../sources/notes/eisnerread.md#e12)
[^eisnerread-e13]: Eisner 2009, What to read. [Evidence](../../sources/notes/eisnerread.md#e13)
[^eisnerread-e14]: Eisner 2009, Which parts to focus on. [Evidence](../../sources/notes/eisnerread.md#e14)
[^keshav2007read-e1]: Keshav 2007, §2. [Evidence](../../sources/notes/keshav2007read.md#e1)
[^keshav2007read-e2]: Keshav 2007, §2.1. [Evidence](../../sources/notes/keshav2007read.md#e2)
[^keshav2007read-e3]: Keshav 2007, §2.1. [Evidence](../../sources/notes/keshav2007read.md#e3)
[^keshav2007read-e4]: Keshav 2007, §2.1. [Evidence](../../sources/notes/keshav2007read.md#e4)
[^keshav2007read-e5]: Keshav 2007, §2.2. [Evidence](../../sources/notes/keshav2007read.md#e5)
[^keshav2007read-e6]: Keshav 2007, §2.2. [Evidence](../../sources/notes/keshav2007read.md#e6)
[^keshav2007read-e7]: Keshav 2007, §2.3. [Evidence](../../sources/notes/keshav2007read.md#e7)
[^keshav2007read-e8]: Keshav 2007, §2.3. [Evidence](../../sources/notes/keshav2007read.md#e8)
[^keshav2007read-e9]: Keshav 2007, §3. [Evidence](../../sources/notes/keshav2007read.md#e9)
[^keshav2007read-e10]: Keshav 2007, §3. [Evidence](../../sources/notes/keshav2007read.md#e10)
[^keshav2007read-e11]: Keshav 2007, §3. [Evidence](../../sources/notes/keshav2007read.md#e11)
[^griswoldread-e1]: Griswold, "What are the motivations for this work?". [Evidence](../../sources/notes/griswoldread.md#e1)
[^griswoldread-e2]: Griswold, "What are the motivations for this work?". [Evidence](../../sources/notes/griswoldread.md#e2)
[^griswoldread-e3]: Griswold, "What is the work's evaluation of the proposed solution?". [Evidence](../../sources/notes/griswoldread.md#e3)
[^griswoldread-e6]: Griswold, how to read a paper. [Evidence](../../sources/notes/griswoldread.md#e6)
[^griswoldread-e7]: Griswold, how to read a paper. [Evidence](../../sources/notes/griswoldread.md#e7)
[^griswoldread-e8]: Griswold, how to read a paper. [Evidence](../../sources/notes/griswoldread.md#e8)
[^bender2003critical-e1]: Bender 2003, p. 1. [Evidence](../../sources/notes/bender2003critical.md#e1)
[^bender2003critical-e2]: Bender 2003, p. 1. [Evidence](../../sources/notes/bender2003critical.md#e2)
[^bender2003critical-e3]: Bender 2003, p. 1, research paper questions 1–4. [Evidence](../../sources/notes/bender2003critical.md#e3)
[^vinitskypaper-e1]: Vinitsky, A template. [Evidence](../../sources/notes/vinitskypaper.md#e1)
[^vinitskypaper-e2]: Vinitsky, Why am I reading this paper? [Evidence](../../sources/notes/vinitskypaper.md#e2)
[^vinitskypaper-e3]: Vinitsky, Summary. [Evidence](../../sources/notes/vinitskypaper.md#e3)
[^vinitskypaper-e4]: Vinitsky, Unresolved question. [Evidence](../../sources/notes/vinitskypaper.md#e4)
[^vinitskypaper-e6]: Vinitsky, Paper games. [Evidence](../../sources/notes/vinitskypaper.md#e6)
[^vinitskypaper-e7]: Vinitsky, Paper games. [Evidence](../../sources/notes/vinitskypaper.md#e7)
[^vinitskypaper-e8]: Vinitsky, Paper games. [Evidence](../../sources/notes/vinitskypaper.md#e8)
[^acm2026csurguidelines-e1]: ACM Computing Surveys (the survey journal of the Association for Computing Machinery) author guidelines, Long Survey Paper. [Evidence](../../sources/notes/acm2026csurguidelines.md#e1)
[^acm2026csurguidelines-e2]: ACM Computing Surveys (the survey journal of the Association for Computing Machinery) author guidelines, Tutorial Paper. [Evidence](../../sources/notes/acm2026csurguidelines.md#e2)
[^arxivabout-e2]: arXiv, About arXiv. [Evidence](../../sources/notes/arxivabout.md#e2)
[^taocareer-e16]: Tao, Career advice, Learn and relearn your field. [Evidence](../../sources/notes/taocareer.md#e16)
[^taocareer-e23]: Tao, Career advice, Talk to your advisor. [Evidence](../../sources/notes/taocareer.md#e23)
[^taocareer-e27]: Tao, Career advice, Take the initiative. [Evidence](../../sources/notes/taocareer.md#e27)
[^taocareer-e33]: Tao, Career advice, Attend talks and conferences. [Evidence](../../sources/notes/taocareer.md#e33)
[^vardi2009conferences-e1]: Vardi 2009, main text, para. 2. [Evidence](../../sources/notes/vardi2009conferences.md#e1)
[^vanderkouwe2019sok-e27]: van der Kouwe et al. 2019, §III-B. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e27)
[^shaw2002makes-e5]: Shaw 2002, §1.2.3. [Evidence](../../sources/notes/shaw2002makes.md#e5)
[^shaw2002makes-e6]: Shaw 2002, §1.2.3. [Evidence](../../sources/notes/shaw2002makes.md#e6)
[^shaw2002makes-e7]: Shaw 2002, §2.3. [Evidence](../../sources/notes/shaw2002makes.md#e7)
[^nanda2025process-e4]: Nanda 2025, Exploration (Stage 2). [Evidence](../../sources/notes/nanda2025process.md#e4)
[^nanda2025taste-e5]: Nanda 2025, How to learn it? [Evidence](../../sources/notes/nanda2025taste.md#e5)
[^schulman2020opinionated-e3]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e3)
[^olah2021taste-e6]: Olah 2021, Exercise 3. [Evidence](../../sources/notes/olah2021taste.md#e6)
[^olah2021taste-e17]: Olah 2021, Failure mode 2. [Evidence](../../sources/notes/olah2021taste.md#e17)
[^dredze2012successful-e18]: Dredze 2012, #32 First Year. [Evidence](../../sources/notes/dredze2012successful.md#e18)
[^varian1997build-e3]: Varian 1997, §1.3. [Evidence](../../sources/notes/varian1997build.md#e3)
[^noble2023ten-e5]: Noble 2023, Rule 4. [Evidence](../../sources/notes/noble2023ten.md#e5)
[^ralph2022paving-e1]: Ralph & Baltes 2022, §2.1. [Evidence](../../sources/notes/ralph2022paving.md#e1)
[^ralph2022paving-e2]: Ralph & Baltes 2022, §2.1. [Evidence](../../sources/notes/ralph2022paving.md#e2)
