# Position papers: arguing for how a field should work and what it should believe

This page covers **position papers** and their close relatives, **perspectives** and **vision papers**. Their main contribution is not new data but an argued claim: what the field should do, believe, or change. The call for papers of the International Conference on Machine Learning (ICML) draws the line this way: a position paper makes an argument for a view of what should be done, while a research paper reports advances that have already been made[^icml2025position-e1].

If you want to collect published studies and summarize them systematically, that is a [Review studies](review_study.md). If you want to study how people actually do research, with data to back it up, see [Methodology research and meta-science](meta_science.md). The basics of building an argument that holds up are in [Interpretation and argument](../05_research-strategies/interpret_argue.md); this page covers only what is specific to position papers.

**Scope**: The submission requirements and review criteria on this page come mainly from computer science: in machine learning, the position paper tracks of ICML 2024, ICML 2025, and NeurIPS 2025 (the Conference on Neural Information Processing Systems); in software engineering, the Ideas, Visions and Reflections track of FSE 2025 (the ACM International Conference on the Foundations of Software Engineering). For journal perspectives, the example is the guidance from *Nature Sustainability*. The advice on stating a thesis and answering objections draws on handouts from the Harvard College Writing Center and on the philosopher Jim Pryor's writing guides. Every conference and journal changes its rules from year to year, so check that year's call for papers before you submit. In the humanities, papers built mainly on argument are the norm; for how that works, see [Interpretation and argument](../05_research-strategies/interpret_argue.md) and [Philosophical argument](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md).

**Strategies it usually serves**: [Interpretation and argument](../05_research-strategies/interpret_argue.md). Reflection pieces that look back at the path a field has taken and point out where it went wrong often include an element of [Synthesis](../05_research-strategies/synthesize.md) too.

**After reading this page, you should be able to:**

- tell position papers, research papers, reviews, and perspectives apart, and judge which one fits what you have;
- state your position as one arguable sentence and explain why it matters;
- find evidence for your position, identify the strongest opposing position, and answer it seriously;
- know how position papers are reviewed, and judge whether now is the right time for you to write one.

---

## 1. What this kind of paper is, and when to use it

A position paper sets out to persuade your peers to accept a claim about the field. ICML 2025 lists the kinds of positions it has in mind: an argument for or against a particular research direction (not a particular algorithm or solution), a call to action, a value statement, a policy proposal, or a recommendation for changing how we conduct and evaluate research[^icml2025position-e9]. A paper that describes new research without advocating a position is not a position paper[^icml2025position-e8].

ICML first opened this track in 2024. Its reason: many important contributions to the field do not look like traditional research papers; instead they discuss an ongoing trend or defend a particular view of the field[^icml2024position-e1].

The name and the requirements vary by venue. The table lists only the examples used on this page:

| Venue | Name | Length | Notes |
|---|---|---|---|
| ICML 2025 position paper track | position paper | 8-page limit, same as the main conference[^icml2025position-e13] | Must include an "Alternative Views" section[^icml2025position-e7] |
| FSE 2025 Ideas, Visions and Reflections track | new ideas, visions, reflections | Up to 4 pages, plus 1 page of references[^fse2025ivr-e8] | Evaluation results not required[^fse2025ivr-e4] |
| *Nature Sustainability* | Perspective | Main text up to 5,000 words, up to 60 references[^natsustaincontent-e5] | Mostly commissioned by the editors[^natsustaincontent-e3] |
| Same journal | Comment | — | A call to action must include a detailed roadmap to a solution[^natsustaincontent-e6] |

**Questions it is good at**:

- **What the field is getting right and wrong**, and which open problems deserve more attention and which less[^neurips2025position-e1];
- **Whether an existing research direction has gone off track**[^fse2025ivr-e2];
- **Whether a new direction is worth pursuing** when it has no solid results yet but is well motivated[^fse2025ivr-e1];
- **How research should be done and evaluated**[^icml2025position-e9].
- **One side of a research controversy**: a journal perspective can argue for a controversial position or put forward a speculative hypothesis, and the pieces on both sides of a debate are usually published as perspectives[^natsustaincontent-e2].

It cannot answer questions like "how big is the effect of X?" or "does A cause B?"; those need data and experiments. A position paper can use other people's data and your own preliminary data as evidence, but its contribution is the argument, not the measurement.

**How it differs from related paper types**:

| | Position paper | Research paper | [Review studies](review_study.md) | New ideas / early results paper |
|---|---|---|---|---|
| Central claim | What the field should do or believe | What we built or found | What existing studies show taken together | This new direction is promising |
| Main evidence | Reasoning, plus citations, examples, and existing data | Your own experiments, measurements, or proofs | Systematically collected published studies | Preliminary results |
| Must reviewers agree with the conclusion? | No[^icml2025position-e11] | They must be convinced by the evidence | They must be convinced by the method | They need to see preliminary evidence |

Sources for the table: research papers report advances already made[^icml2025position-e1]; perspectives are more forward-looking and more speculative than reviews[^natsustaincontent-e1]; FSE's new-ideas papers must give initial evidence, while its visions and reflections papers give a rationale[^fse2025ivr-e3]. The remaining cells are our own synthesis.

### When a newcomer should write one, and when not

What follows is this handbook's judgment based on the sources above; the sources themselves say nothing specifically about newcomers:

- **When it makes sense**: in your own research you have seen firsthand a problem that is widespread in the field, you have examples and preliminary data, and you can say clearly what should change. A position paper is then a good way to push a specific finding out to the whole field.
- **When to hold off**: you have only a topic and can't yet state an arguable claim; you haven't read enough to say who holds the opposite view; or what you really have is a new method you haven't evaluated yet. For that last case, ICML says to submit to the main track[^icml2025position-e8], and FSE says that a full research paper lacking an evaluation is not a good vision paper[^fse2025ivr-e5].
- **Know where the bar is**: position papers must meet the same scholarly standards: support claims with evidence and reasoning, give background and context, and cite others' work properly[^icml2025position-e4]. Journal perspectives are mostly commissioned by the editors[^natsustaincontent-e3], so a newcomer has little chance of getting one in by submitting directly; conference position and vision tracks are open to everyone, and the bar there is somewhat lower.
- **Talk to your advisor**: a position paper takes no less time than a small research paper, and it won't replace your main project. FSE says these papers lay the groundwork for later full papers[^fse2025ivr-e9]; in other words, it works best as a by-product of your main line of research.

**The running example**: the project "published evaluations of large language model vulnerability detectors are inflated by data leakage" is itself a measurement project. It has to be shown with data; it is not a position paper. But if, once the measurement is done, you find that leakage is widespread in smart contract vulnerability detection benchmarks, you could build on it to write a position paper arguing that "every paper evaluating large language model vulnerability detection should check for and report data leakage before reporting scores." The evidence for that position paper would come mainly from your own measurements and the existing literature. Natural language processing already has a similar paper: Sainz et al. 2023, which describes itself as a position paper[^sainz2023nlp-e6], argues that data contamination should be measured for every benchmark, partly because contamination inflates a model's measured performance on that benchmark[^sainz2023nlp-e2].

---

## 2. How to do it

### Step 1: State your position as one arguable sentence

**How:**

- **Write a claim, not a topic.** ICML 2025 illustrates this with hypothetical titles: "Stop research on such-and-such property of machine learning" states a position; "A perspective on such-and-such topic" does not[^icml2025position-e6].
- **Make it something people could disagree with.** A good thesis is arguable: a thoughtful reader might disagree with it[^harvardwcthesis-e1]. If you only describe or summarize what readers can see for themselves, there is no one to persuade[^harvardwcthesis-e2].
- **Get the scope right.** Too narrow, and you have nothing interesting to say; too broad, and you can't back it up with evidence[^harvardwcthesis-e3]. Advice from philosophy writing applies too: a good paper is modest, arguing for one small point, but stating it clearly and giving good reasons for it[^pryor2012writing-e5].

**Why:** The first review criterion for a position paper is that it clearly states a position[^icml2025position-e9]. If the position is fuzzy, the support and the rebuttals that follow have nothing to attach to.

**Where people go wrong:** writing "Large language models bring both opportunities and challenges for software security." Nobody would disagree with that, so it needs no argument. "Evaluations of large language model vulnerability detection should not be compared with traditional tools until they have been checked for data leakage" is a claim someone would push back on.

**Write it down:** Write your position in one sentence starting "This paper argues that ...", then one more sentence: who would disagree, and why.

### Step 2: Explain why it matters, and why now

**How:**

- **Show the topic's weight.** ICML's "Significance" criterion asks the paper to show why the topic is important, in terms of scope, impact, timeliness, risks, benefits, and so on[^icml2025position-e10].
- **Explain why it needs discussing now.** The track wants timely topics that stimulate productive, civil discussion, and controversial topics are welcome[^icml2025position-e3].
- **Tell readers why they should care.** When you put the problem in front of readers, you are telling them what is at stake in the argument and why the answer is worth caring about[^harvardwcthesis-e4].

**Why:** Reviewers don't have to agree with you, but they do have to think the topic deserves the whole field's attention[^icml2025position-e2].

**Where people go wrong:** making "importance" an empty phrase, such as "this issue is attracting growing attention." Better to give something concrete: how many papers use the same benchmark, how many conclusions might have to change as a result.

**Write it down:** Three sentences: whom this affects, how much, and why it needs discussing now.

### Step 3: Find evidence for your position

**How:**

- **Position papers need evidence too.** ICML requires claims to be supported with evidence and reasoning[^icml2025position-e4], and its review criterion reads "supports its position with clear reasoning and evidence where appropriate"[^icml2025position-e10]. FSE asks submissions to make clear why current practice or research should change: new-ideas papers give initial evidence, visions and reflections papers give a rationale[^fse2025ivr-e3].
- **Evidence can take several forms**: results from published studies (cited); specific examples or incidents; existing public data; a small analysis of your own. FSE notes that preliminary results or a sketch of an evaluation plan can help reviewers understand the scope of the work[^fse2025ivr-e4].
- **Your premises should be easier to accept than your conclusion.** The premises of an argument should be uncontroversial, or at least less controversial than the conclusion[^pryor2025terms-e9], and they should be believable independently of the conclusion[^pryor2025terms-e10].
- **Don't substitute reputation for argument.** Saying "a famous scholar holds this view" carries no argumentative weight on its own[^pryor2025terms-e15].
- **If you call for action, say how.** *Nature Sustainability* requires Comments that call for action to give a detailed roadmap to a solution, not just describe a problem[^natsustaincontent-e6].

**Why:** Without evidence, a position is just an opinion. What separates a position paper from an editorial is that it lays out its reasons and evidence for others to check.

**Where people go wrong:** picking only the examples that support you. Readers will ask: where are the counterexamples? How do you know this isn't an isolated case?

**Write it down:** A table with one row per supporting reason: what its evidence is (citation, example, data) and how strong that evidence is.

### Step 4: Find the strongest opposing position and answer it seriously

**How:**

1. **List the opposing positions.** A counterargument is an argument a reader could reasonably raise to challenge your thesis[^harvardwccounterargument-e1]. ICML 2025 requires an "Alternative Views" section in the main body (not an appendix) that describes and addresses one or more viable opposing positions, not straw men[^icml2025position-e7].
2. **Take on the strongest version.** Read the other side's argument charitably, in its strongest form, helping the original author shore it up if needed[^pryor2025terms-e17]; answering the strongest argument the other side can give does the most for your own view[^pryor2025terms-e18].
3. **Imagine how they would hit back.** Don't assume the other side will concede right away; think about how they would respond to you, and how you would answer[^pryor2012writing-e33].
4. **You can concede part of the point.** You can grant that the counterargument is partly right, then explain why it doesn't undermine your thesis[^harvardwccounterargument-e5].
5. **If you can't refute it, revise your position.** A counterargument you can't answer may mean you need to revise your thesis or part of it[^harvardwccounterargument-e3].

**Why:** "Alternative Views" is one of ICML 2025's review criteria[^icml2025position-e7]. More fundamentally, the people a position paper needs to persuade are exactly the ones who aren't yet persuaded.

**Where people go wrong:** setting up a straw man, for example writing the other side as "some people think data leakage doesn't matter." A real and stronger objection might be: "The training data of closed models can't be inspected, so leakage can't be checked at all, and requiring every paper to report it is empty talk." That is the one you need to answer. You could point out, for instance, that people have proposed ways to check closed models too: Sainz et al. suggest exploiting the memorization abilities of large language models[^sainz2023nlp-e5].

**Write it down:** List the two or three strongest opposing positions, and for each write one sentence on "what it gets right" and one on "why it doesn't overturn my claim."

> **Where sources disagree: must "Alternative Views" be a separate section?**
>
> The three calls for papers differ. When ICML 2024 first opened the position paper track, its review criteria had only six items, and "Alternative Views" was not one of them[^icml2024position-e3]. ICML 2025 made it mandatory, and required it in the main body[^icml2025position-e7]. NeurIPS 2025 says papers "may (where appropriate)" include it[^neurips2025position-e2], and adds "(if relevant)" to the corresponding review criterion[^neurips2025position-e3].
>
> **Our suggestion**: whatever your target venue requires, answer the strongest opposing position seriously; whether it gets its own section is a formatting question, so follow that year's rules for your venue.

### Step 5: Lay out the background and say where you stand

**How:**

- **Discuss and cite the relevant literature and events.** This is ICML's "Context" criterion[^icml2025position-e12]; FSE's "Scholarship" criterion likewise asks for appropriate consideration of relevant literature[^fse2025ivr-e6].
- **Read published position papers first.** ICML 2025 suggests browsing the previous year's published position papers for examples, and as ideas to build on or to argue against[^icml2025position-e14].
- **Say whom you are arguing against.** Your thesis is often itself a rebuttal of someone else's argument[^harvardwccounterargument-e7].

**Why:** Whether a position is new only becomes visible against the existing debate.

**Where people go wrong:** making other people's positions sound more extreme than they are so that yours looks new. Before you criticize, state accurately what the other side means; see [Interpretation and argument](../05_research-strategies/interpret_argue.md).

**Write it down:** A dialectical map: who claims what, on what grounds, and whom you agree and disagree with. For how, see [Philosophical argument, Step 2](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md#step-2-map-the-literature-as-a-dialectical-map).

### Step 6: Write it so the position jumps out

**How:**

- **Put your position where it can't be missed.** ICML 2025 requires the title to state the position, the abstract to state it in one sentence (for example, "This position paper argues that ..."), and the introduction to state it in bold[^icml2025position-e5]. Even if your venue doesn't require this, it is a good habit.
- **Raise the central question at the start.** Say what the problem is and why it is a problem[^pryor2012writing-e30].
- **Use simple, plain prose.** Keep sentences and paragraphs short[^pryor2012writing-e8].
- **A suggested structure**: introduction (the position, why it matters) → background → supporting reasons (one section per reason, each with its evidence) → alternative views and responses → concrete recommendations (who should do what) → conclusion.

**Why:** One review criterion is "Communication quality": well organized and clearly written[^icml2025position-e12]. A position paper has no experimental results to lean on, so whether readers are persuaded depends heavily on how clear the argument is.

**Write it down:** Outline first, and for each section write one sentence: "This section should convince the reader that ..."

### Step 7: Choose a venue and learn how it reviews

**How:**

- **Conference position paper tracks**: at ICML 2025, position papers follow the same formatting rules, double-blind review, policies, and deadlines as the main conference[^icml2025position-e13]. In 2024 they were reviewed by reviewers who had opted in to reviewing this kind of submission[^icml2024position-e2]. NeurIPS 2025 does not require position papers to complete the main track's paper checklist[^neurips2025position-e4].
- **Conference vision tracks**: FSE 2025 reviews on value, impact, originality, scholarship, and overall quality[^fse2025ivr-e6]; visions and reflections papers are also judged on whether their rationale holds up[^fse2025ivr-e7].
- **Journal perspectives**: *Nature Sustainability*'s Perspectives are mostly commissioned by the editors, though proposals are welcome[^natsustaincontent-e3]. To propose one yourself, you first send a synopsis covering the topic, how the piece will be organized, a sample figure, key recent references, and what the article will contribute[^natsustaincontent-e4]. Perspectives are peer reviewed too[^natsustaincontent-e5].

**Why:** Venues review by different criteria. A position paper written to research-paper standards, or the reverse, will read as a poor fit.

**Where people go wrong:** assuming position papers are easy to publish. They don't require new results, but the demands on argument, background, and presentation are no lower.

**Write it down:** Your target venue, the link to that year's call for papers, and its review criteria copied out one by one; check yourself against each before you submit.

---

## 3. Checklist

The "Must do" items below are based mainly on the requirements and review criteria of the ICML 2025 position paper track, which are the rules of one machine learning conference; for other venues, go by that year's call for papers.

**Must do**

- [ ] State a position clearly, rather than only describing new research[^icml2025position-e8][^icml2025position-e9]
- [ ] State the position in the title, abstract, and introduction[^icml2025position-e5]
- [ ] Support the position with clear reasoning, and with evidence where appropriate[^icml2025position-e10]
- [ ] Explain why the topic matters[^icml2025position-e10]
- [ ] Describe and answer viable opposing positions, not straw men[^icml2025position-e7]
- [ ] Discuss and cite the literature and events relevant to the position[^icml2025position-e12]
- [ ] Organize the paper well and write it clearly[^icml2025position-e12]

**Better practice**

- [ ] Give preliminary results, or a sketch of an evaluation plan[^fse2025ivr-e4]
- [ ] When calling for action, give a detailed roadmap to a solution[^natsustaincontent-e6]
- [ ] Answer the strongest version of the other side's argument[^pryor2025terms-e17]
- [ ] Make your premises easier to accept than your conclusion[^pryor2025terms-e9]

**Outstanding**: support the position with a new analysis or new data of your own; say explicitly what evidence would make you change your position; give concrete, checkable recommendations (who does what, and when).

**Fine to skip; not a flaw**

- No evaluation results: the FSE vision track doesn't require them[^fse2025ivr-e4]
- Reviewers disagree with your position: ICML says explicitly that reviewers need not agree[^icml2025position-e11]
- Not answering every possible objection: you don't need to answer every counterargument[^harvardwccounterargument-e6]; focus on the strongest and most pressing ones[^pryor2012writing-e17]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| The title and abstract name a topic but don't state a position | That doesn't count as stating a position[^icml2025position-e6] |
| Nobody would disagree with the position | If you only summarize what readers can see for themselves, there is no one to persuade[^harvardwcthesis-e2] |
| Dressing up an unevaluated new method as a position paper | It isn't a position paper; submit it as a research paper[^icml2025position-e8][^fse2025ivr-e5] |
| Opinions without evidence or citations | Position papers must also support their claims with evidence and reasoning[^icml2025position-e4] |
| Writing the other side as a straw man | You need to answer viable opposing positions[^icml2025position-e7] |
| Using a famous person's view as your reason | Reputation alone carries no argumentative weight[^pryor2025terms-e15] |
| Describing the problem without saying what to do | A piece that calls for action must give a roadmap to a solution[^natsustaincontent-e6] |
| A scope so broad it tries to say everything | Too broad, and you can't back it up with evidence[^harvardwcthesis-e3] |

---

## 5. Further reading

- **Requirements and review criteria for position papers**: the ICML 2025 and NeurIPS 2025 calls for position papers; compare how differently they treat the "Alternative Views" section. The ICML 2024 call explains why the track was created.
- **Visions and reflections in software engineering**: the FSE 2025 call for Ideas, Visions and Reflections papers, which distinguishes new ideas, visions, and reflections and spells out what kinds of submissions don't qualify.
- **Journal perspectives**: *Nature Sustainability*'s guide to its content types, which distinguishes reviews, perspectives, and comments.
- **How to write a thesis and answer objections**: the Harvard College Writing Center's two handouts, "Thesis" and "Counterargument"; Pryor's guide to writing philosophy papers. For a more systematic treatment, see [Interpretation and argument](../05_research-strategies/interpret_argue.md) and [Philosophical argument](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md).
- **A position paper related to the running example**: Sainz et al. 2023, which the authors call a position paper[^sainz2023nlp-e6], argues that data contamination of large language models should be measured for every benchmark[^sainz2023nlp-e2].

Links to all sources are in the [source list](../../sources/README.md).

[^icml2025position-e1]: ICML 2025 call for position papers, top of page. [Evidence](../../sources/notes/icml2025position.md#e1)
[^icml2025position-e2]: ICML 2025 call for position papers, top of page. [Evidence](../../sources/notes/icml2025position.md#e2)
[^icml2025position-e3]: ICML 2025 call for position papers, top of page. [Evidence](../../sources/notes/icml2025position.md#e3)
[^icml2025position-e4]: ICML 2025 call for position papers, top of page. [Evidence](../../sources/notes/icml2025position.md#e4)
[^icml2025position-e5]: ICML 2025 call for position papers, Policies and Requirements. [Evidence](../../sources/notes/icml2025position.md#e5)
[^icml2025position-e6]: ICML 2025 call for position papers, Policies and Requirements. [Evidence](../../sources/notes/icml2025position.md#e6)
[^icml2025position-e7]: ICML 2025 call for position papers, Policies and Requirements. [Evidence](../../sources/notes/icml2025position.md#e7)
[^icml2025position-e8]: ICML 2025 call for position papers, Policies and Requirements; Reviewing. [Evidence](../../sources/notes/icml2025position.md#e8)
[^icml2025position-e9]: ICML 2025 call for position papers, Reviewing, Position. [Evidence](../../sources/notes/icml2025position.md#e9)
[^icml2025position-e10]: ICML 2025 call for position papers, Reviewing. [Evidence](../../sources/notes/icml2025position.md#e10)
[^icml2025position-e11]: ICML 2025 call for position papers, Reviewing. [Evidence](../../sources/notes/icml2025position.md#e11)
[^icml2025position-e12]: ICML 2025 call for position papers, Reviewing. [Evidence](../../sources/notes/icml2025position.md#e12)
[^icml2025position-e13]: ICML 2025 call for position papers, Policies and Requirements. [Evidence](../../sources/notes/icml2025position.md#e13)
[^icml2025position-e14]: ICML 2025 call for position papers, top of page. [Evidence](../../sources/notes/icml2025position.md#e14)
[^icml2024position-e1]: ICML 2024 call for position papers, top of page. [Evidence](../../sources/notes/icml2024position.md#e1)
[^icml2024position-e2]: ICML 2024 call for position papers, Reviewing. [Evidence](../../sources/notes/icml2024position.md#e2)
[^icml2024position-e3]: ICML 2024 call for position papers, Reviewing. [Evidence](../../sources/notes/icml2024position.md#e3)
[^neurips2025position-e1]: NeurIPS 2025 Call for Position Papers, top of page. [Evidence](../../sources/notes/neurips2025position.md#e1)
[^neurips2025position-e2]: NeurIPS 2025 Call for Position Papers, Policies and Requirements. [Evidence](../../sources/notes/neurips2025position.md#e2)
[^neurips2025position-e3]: NeurIPS 2025 Call for Position Papers, Reviewing. [Evidence](../../sources/notes/neurips2025position.md#e3)
[^neurips2025position-e4]: NeurIPS 2025 Call for Position Papers, Policies and Requirements. [Evidence](../../sources/notes/neurips2025position.md#e4)
[^fse2025ivr-e1]: FSE 2025 Ideas, Visions and Reflections track call for papers. [Evidence](../../sources/notes/fse2025ivr.md#e1)
[^fse2025ivr-e2]: FSE 2025 Ideas, Visions and Reflections track call for papers. [Evidence](../../sources/notes/fse2025ivr.md#e2)
[^fse2025ivr-e3]: FSE 2025 Ideas, Visions and Reflections track call for papers. [Evidence](../../sources/notes/fse2025ivr.md#e3)
[^fse2025ivr-e4]: FSE 2025 Ideas, Visions and Reflections track call for papers. [Evidence](../../sources/notes/fse2025ivr.md#e4)
[^fse2025ivr-e5]: FSE 2025 Ideas, Visions and Reflections track call for papers, Out of Scope. [Evidence](../../sources/notes/fse2025ivr.md#e5)
[^fse2025ivr-e6]: FSE 2025 Ideas, Visions and Reflections track call for papers, Evaluation. [Evidence](../../sources/notes/fse2025ivr.md#e6)
[^fse2025ivr-e7]: FSE 2025 Ideas, Visions and Reflections track call for papers, Evaluation. [Evidence](../../sources/notes/fse2025ivr.md#e7)
[^fse2025ivr-e8]: FSE 2025 Ideas, Visions and Reflections track call for papers, How to Submit. [Evidence](../../sources/notes/fse2025ivr.md#e8)
[^fse2025ivr-e9]: FSE 2025 Ideas, Visions and Reflections track call for papers. [Evidence](../../sources/notes/fse2025ivr.md#e9)
[^natsustaincontent-e1]: Nature Sustainability article types, Perspective. [Evidence](../../sources/notes/natsustaincontent.md#e1)
[^natsustaincontent-e2]: Nature Sustainability article types, Perspective. [Evidence](../../sources/notes/natsustaincontent.md#e2)
[^natsustaincontent-e3]: Nature Sustainability article types, Perspective. [Evidence](../../sources/notes/natsustaincontent.md#e3)
[^natsustaincontent-e4]: Nature Sustainability article types, Perspective. [Evidence](../../sources/notes/natsustaincontent.md#e4)
[^natsustaincontent-e5]: Nature Sustainability article types, Perspective, Format. [Evidence](../../sources/notes/natsustaincontent.md#e5)
[^natsustaincontent-e6]: Nature Sustainability article types, Comment. [Evidence](../../sources/notes/natsustaincontent.md#e6)
[^harvardwcthesis-e1]: Harvard College Writing Center, Thesis, paragraph 1. [Evidence](../../sources/notes/harvardwcthesis.md#e1)
[^harvardwcthesis-e2]: Harvard College Writing Center, Thesis, paragraph 3. [Evidence](../../sources/notes/harvardwcthesis.md#e2)
[^harvardwcthesis-e3]: Harvard College Writing Center, Thesis, paragraph 3. [Evidence](../../sources/notes/harvardwcthesis.md#e3)
[^harvardwcthesis-e4]: Harvard College Writing Center, Thesis, paragraph 2. [Evidence](../../sources/notes/harvardwcthesis.md#e4)
[^harvardwccounterargument-e1]: Harvard College Writing Center, Counterargument, paragraph 2. [Evidence](../../sources/notes/harvardwccounterargument.md#e1)
[^harvardwccounterargument-e3]: Harvard College Writing Center, Counterargument, paragraph 4. [Evidence](../../sources/notes/harvardwccounterargument.md#e3)
[^harvardwccounterargument-e5]: Harvard College Writing Center, Counterargument, How to address counterarguments. [Evidence](../../sources/notes/harvardwccounterargument.md#e5)
[^harvardwccounterargument-e6]: Harvard College Writing Center, Counterargument, after the Example. [Evidence](../../sources/notes/harvardwccounterargument.md#e6)
[^harvardwccounterargument-e7]: Harvard College Writing Center, Counterargument, Where to address counterarguments, Before your thesis. [Evidence](../../sources/notes/harvardwccounterargument.md#e7)
[^pryor2012writing-e5]: Pryor 2012, guide to writing a philosophy paper, What Does One Do in a Philosophy Paper? [Evidence](../../sources/notes/pryor2012writing.md#e5)
[^pryor2012writing-e8]: Pryor 2012, guide to writing a philosophy paper, Use simple prose. [Evidence](../../sources/notes/pryor2012writing.md#e8)
[^pryor2012writing-e17]: Pryor 2012, guide to writing a philosophy paper, Anticipate objections. [Evidence](../../sources/notes/pryor2012writing.md#e17)
[^pryor2012writing-e30]: Pryor 2012, guide to writing a philosophy paper, Be concise, but explain yourself fully. [Evidence](../../sources/notes/pryor2012writing.md#e30)
[^pryor2012writing-e33]: Pryor 2012, guide to writing a philosophy paper, Anticipate objections. [Evidence](../../sources/notes/pryor2012writing.md#e33)
[^pryor2025terms-e9]: Pryor 2025, handout on philosophical terms and methods, Philosophical Arguments / Persuasive Arguments. [Evidence](../../sources/notes/pryor2025terms.md#e9)
[^pryor2025terms-e10]: Pryor 2025, handout on philosophical terms and methods, Philosophical Arguments / Persuasive Arguments. [Evidence](../../sources/notes/pryor2025terms.md#e10)
[^pryor2025terms-e15]: Pryor 2025, handout on philosophical terms and methods, What is the Philosophical Method? / Appeals to authority/popularity and the burden of proof. [Evidence](../../sources/notes/pryor2025terms.md#e15)
[^pryor2025terms-e17]: Pryor 2025, handout on philosophical terms and methods, What is the Philosophical Method? / Charity. [Evidence](../../sources/notes/pryor2025terms.md#e17)
[^pryor2025terms-e18]: Pryor 2025, handout on philosophical terms and methods, What is the Philosophical Method? / Charity. [Evidence](../../sources/notes/pryor2025terms.md#e18)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e5]: Sainz et al. 2023, §5.2 Closed LLMs. [Evidence](../../sources/notes/sainz2023nlp.md#e5)
[^sainz2023nlp-e6]: Sainz et al. 2023, Abstract. [Evidence](../../sources/notes/sainz2023nlp.md#e6)
