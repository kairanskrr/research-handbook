# Replication studies: redoing a published study on purpose to test whether its conclusions hold

This page covers the **replication study**: deliberately and systematically redoing a published study (the **original study**) to see whether its results can be obtained again[^ralph2020empirical-e208]. You can redo it with the original authors' **artifacts** (the code, data, and scripts that accompany the paper), or you can reimplement it yourself, use different data, or move it to a different context.

This page does not cover how to make **your own** research easy for others to reproduce. For that, see the steps on releasing artifacts in [Engineering research](../07_fields/computer-science/practices/engineering_research.md) and [Benchmarking](../07_fields/computer-science/practices/benchmarking.md), and [Organizing your research materials](../08_throughout/organizing_materials.md); for ACM artifact badges, see [Computer science field overview: artifact evaluation and badges](../07_fields/computer-science/README.md#artifact-evaluation-and-badges).

**Scope**: the standards and examples on this page all come from computer science. The checklist follows the replication standard that the Association for Computing Machinery's Special Interest Group on Software Engineering (ACM SIGSOFT) wrote for software engineering; the reporting guidelines come from software engineering; the terminology comes from ACM's rules on artifact evaluation; and the examples come from software engineering, fuzzing, artificial intelligence, and machine learning. Psychology, medicine, and other fields have their own discussions and standards on replication, and may use the terms differently (see Section 1). Check your own field's standards before you start.

**Strategies it usually serves**: [Comparative evaluation](../05_research-strategies/compare_evaluate.md) (testing whether a paper's comparative conclusion still holds under other conditions), [Measurement](../05_research-strategies/measure.md) (redoing the study with different data or a different way of measuring to see whether the original conclusion survives).

**After reading this page, you should be able to:**

- tell apart repeatability, reproducibility, and replicability, and state in your paper which set of definitions you use;
- decide which kind of replication you are doing, and pick the claims worth testing;
- carry out a replication step by step: understand the original study, contact the original authors, record deviations, fix the success criteria in advance, and report the results honestly, including results you could not reproduce;
- check your replication paper against the checklist at the end.

---

## 1. What kind of study this is, and when to use it

The ACM SIGSOFT Empirical Standards set two conditions for a replication study: the replication is **deliberate and planned**, not an accidental overlap with someone else's study; and the original study is **a specific, identified, previously published paper**[^ralph2020empirical-e209].

Its value is that it lets researchers confirm, refute, or refine the conclusions of earlier studies[^carver2010towards-e1]. In computing, ACM's position is that an experimental result is not fully established until it has been independently reproduced[^acm2020artifact-e9].

### First, get the terms straight

The English words around replication are used differently by different sources, sometimes in exactly opposite ways. Computing researchers agree that empirical results should be reproducible, but there is neither a clear definition of what "reproducible" means nor a consensus on it[^gundersen2018state-e1]. We start with ACM's three-way split, which turns on "same team or not" and "same experimental setup or not":

| Term | Who does it | Experimental setup | For computational experiments |
|---|---|---|---|
| Repeatability | Same team | Same | Researchers can reliably repeat their own computation[^acm2020artifact-e16] |
| Reproducibility | Different team | Same | An independent team gets the same result using the original authors' artifacts[^acm2020artifact-e17] |
| Replicability | Different team | Different | An independent team gets the same result using artifacts they developed independently[^acm2020artifact-e18] |

The two levels of ACM's "Results Validated" badge, "Results Reproduced" and "Results Replicated", are distinguished by whether the original authors' artifacts were used[^acm2020artifact-e5]. For a full description of the badges, see [Computer science field overview: artifact evaluation and badges](../07_fields/computer-science/README.md#artifact-evaluation-and-badges).

When you read the literature, watch out for these:

- **ACM itself swapped two of the terms.** On the recommendation of the National Information Standards Organization (NISO), ACM swapped the meanings of reproducibility and replication to bring them in line with the broader scientific community[^acm2020artifact-e19]. When you read older papers, first check which set of meanings they use.
- **SIGSOFT splits by data.** To reproduce is to rerun the original analysis on the original data; to replicate is to collect new data and run the original analysis on it[^ralph2020empirical-e210].
- **Machine learning often uses a four-way split.** Pineau et al. (organizers of the reproducibility program at the 2019 Conference on Neural Information Processing Systems, NeurIPS) classify work as: reproducible (same data, same analytical tools), replicable (different data), robust (same data, different analysis, such as reimplementing the code), and generalizable (different data and different analytical tools, same conclusions)[^pineau2021improving-e1].

**What to do**: state in your paper which set of definitions you are using, and describe directly what you did: who did it, whether you used the original code, and whether you used the original data. Don't just drop a term and leave it there. On this page, "replication study" covers any planned redo, and we use the three terms in the table above when we need to be more specific.

### Types of replication

The SIGSOFT standard asks you to say what kind of replication you did along three dimensions[^ralph2020empirical-e215]:

| Dimension | Types |
|---|---|
| How similar the method is | **Exact replication**: same research questions, method, and context; **methodological replication**: same research questions and method, different context; **conceptual replication**: same research questions, different method and context[^ralph2020empirical-e211] |
| How much it covers | **Partial replication**: addresses only some of the original research questions; **complete replication**: addresses all of them; **extended replication**: addresses all of them plus new ones[^ralph2020empirical-e212] |
| Who does it | **Internal replication**: same team; **external replication**: different team; **mixed replication**: the two teams overlap[^ralph2020empirical-e213] |

In code- and data-driven areas (such as artificial intelligence and machine learning), Gundersen and Kjensmo define three degrees according to what gets swapped out in the replication[^gundersen2018state-e2]: **R1, experiment reproducible** (same implementation, same data); **R2, data reproducible** (a different implementation, same data); and **R3, method reproducible** (a different implementation, different data). Going from R1 to R3, a successful replication shows a progressively more general result[^gundersen2018state-e3]. As we read it, R1 only shows "this code on this data really does give this number"; only R3 comes close to showing "the method itself works".

### How it differs from related work

| | Replication study | Reproducing a baseline | Artifact evaluation |
|---|---|---|---|
| Purpose | Test whether the original study's conclusions hold | Get someone else's method running as a point of comparison (see [Engineering research](../07_fields/computer-science/practices/engineering_research.md), [Benchmarking](../07_fields/computer-science/practices/benchmarking.md)) | Check whether the artifacts that come with a paper run and match the paper (see [Computer science field overview: artifact evaluation and badges](../07_fields/computer-science/README.md#artifact-evaluation-and-badges)) |
| Output | A paper of its own | Part of your own paper | A badge |

**When it is worth doing**: a conclusion is widely cited and a lot of work builds on it, but nobody has tested it independently; or you suspect it depends on a particular condition, such as specific data, benchmark programs, or parameter settings (examples in Step 1). If you just want to build on someone else's results, it is enough to reproduce the original results under your own conditions first. That doesn't need to become a replication paper; it is just a milestone in your research plan, like "the two existing baseline tools reproduce the results reported in their papers" in Section 2 of [Writing a research plan](../02_do-the-project/03_research-plan.md#2-break-the-claim-into-milestones-each-milestone-is-a-piece-of-evidence).

---

## 2. How to do it

### Step 1: Pick the claims to test, and state your motivation

**How:**

- **Write down why you are doing this replication.** SIGSOFT makes motivation an essential item: for example, to verify the results, or to broaden where they apply by changing the participants or artifacts[^ralph2020empirical-e214].
- **List the specific claims you will test**, rather than vaguely "replicating the paper". The NeurIPS reproducibility challenge, for example, aimed to independently verify the empirical claims in accepted papers[^pineau2021improving-e8].
- **Think about which conditions to change to test the conclusion best.** An example from security: Klees et al. re-evaluated the fuzzer AFLFast (fuzzing tests a program with large numbers of randomly generated inputs to find bugs). They found it did well on the programs chosen in the original paper, but on two programs that other papers had used, it was no better than AFL (American Fuzzy Lop), the tool it had been compared against[^klees2018evaluating-e3]. An example from machine learning: studies have found that with a more thorough search over hyperparameters (settings fixed before training, such as the learning rate), or even with just a different set of random initializations, newly proposed methods often turn out no better than older ones[^pineau2021improving-e2]. The equivalent in other fields is to change the participants or the context, for example rerunning a psychology experiment in another country or with a different population to see whether the effect is still there.
- **Estimate the cost.** Some experiments need so much computation that most researchers could not reproduce them even with the data and code[^pineau2021improving-e5].

**Why**: your motivation decides the type of replication. If you only want to confirm the result, stay as close to the original as you can; if you want to know whether it generalizes, deliberately change the context or the method.

**Where people go wrong:**

- **Copying the original study's weaknesses.** Replicating an underpowered study with an equally underpowered one, or copying the original's mistakes (such as an inappropriate statistical test) without correcting them, are both antipatterns listed by SIGSOFT[^ralph2020empirical-e227]. Statistical power is a study's ability to detect a real effect, and it usually rises with sample size. Improve on the original where you can, for example in design, analysis, or statistical power[^ralph2020empirical-e221], and record the change in your deviation log (see Step 4).
- **Changing the research questions on your own.** The research questions are set by the original study, and a replication must keep them, a conceptual replication included[^ralph2020empirical-e230]. If you want to ask new questions, do an extended replication: keep all the original questions and add new ones[^ralph2020empirical-e212].

### Step 2: Get to know the original study inside out

**How**: before you start, gather what you know about the original study into one document. SIGSOFT requires the paper to describe the original study's research questions, its design, any context variables that might affect the design or the interpretation of the results, and its main findings[^ralph2020empirical-e216]. You can break the design down further:

- participants (if any): how many, and their relevant characteristics;
- artifacts: questionnaires, instructions, raw data, preprocessed data, analysis scripts, and so on;
- context variables: for example hardware, data version, and participants' backgrounds.

Every later "this differs from the original study" is stated relative to this document. At the same time, take stock of what the original authors released: method description, data, code, and experimental setup. How much they released decides whether the most you can do is R1, R2, or R3.

**Where people go wrong**: assuming the paper says everything. Gundersen and Kjensmo surveyed papers from artificial intelligence conferences and found that none documented all the information needed to reproduce them; only 20% to 30% of the information on each of method, data, and experiment was documented[^gundersen2018state-e9]. Reasons machine learning results are hard to reproduce include incomplete descriptions of the model or training procedure, missing or buggy code, and unclear metrics behind the reported results[^pineau2021improving-e10]. List whatever is missing so you can ask the original authors.

### Step 3: Contact the original authors, and record the interaction

**How:**

- **When information or materials are missing, contact the original authors.** One study found that of 402 experimental papers, 32.3% could be repeated without contacting the authors, rising to 48.3% after contacting them[^gundersen2018state-e4]. Another study in machine learning found that 85% of results were successfully reproduced when the original authors helped, but only 4% when the authors did not reply; there may be a selection bias here, though: authors who knew their results would reproduce may have been more willing to help[^pineau2021improving-e3].
- **Record how much interaction there was**, which can range from "only read the paper" to "the original authors acted as consultants"[^carver2010towards-e2]. The paper must describe any overlap or interaction with the original authors[^ralph2020empirical-e217]; if they were not involved at all, say that too.
- **If you can, have the original authors review your replication plan.** SIGSOFT lists this as a desirable item[^ralph2020empirical-e225].

> **Where sources disagree: how involved should the original authors be?**
> - **The case for independence**: Gundersen and Kjensmo argue that independent teams are more objective: they have no incentive to inflate the performance of someone else's method, and they don't share the original team's preconceptions or unwritten tacit knowledge[^gundersen2018state-e5]. They define an "independent team" as one that runs the experiment using only the documentation left by the original team[^gundersen2018state-e6].
> - **The case for collaboration**: the original authors can fill in details the paper left out; the figures above show that a much higher share of results can be reproduced when the original authors take part[^gundersen2018state-e4][^pineau2021improving-e3]. SIGSOFT also lists review of the plan by the original authors as a desirable item[^ralph2020empirical-e225].
> - Carver (who proposed the reporting guidelines for replications in software engineering) notes that there are two opposing views on this question and both have merit[^carver2010towards-e3]; his reporting guidelines only ask you to describe the level of interaction clearly[^carver2010towards-e2].
>
> In practice: ask the original authors for materials and for missing details, but decide yourself, in advance, how to analyze the data and how to judge success. Record all the interaction and report it honestly in the paper, so readers can judge how independent the replication was.

### Step 4: Write down a plan, and log every deviation

**How:**

- **Write a plan before you run anything**: which parts of the original study you keep, which you change and why, and the success criteria from Step 5.
- **Decide whether to use the original code or reimplement.** Using the original authors' artifacts gives reproducibility in ACM's sense; implementing everything yourself gives replicability[^acm2020artifact-e17][^acm2020artifact-e18]. The two test different things: having the original code does not mean the code is correct, and reimplementing an algorithm directly from the paper's description is very valuable[^pineau2021improving-e4]. A safe order: first get the original code running and confirm that your environment gives the original numbers, then change conditions or reimplement.
- **Keep a deviation log.** Write down and justify every difference from the original study (design, participants, artifacts, procedures, data collection, analysis)[^ralph2020empirical-e218][^carver2010towards-e4], including changes you were forced to make, for example because the original data version is no longer available. A table like this works:

| Item | Original study | This replication | Why it differs | Possible effect |
|---|---|---|---|---|
| Example: benchmark programs | 6 | The original 6, plus 2 more | To test whether the conclusion generalizes | Results may differ on the new programs |

- **Record your own process**: for every step, the name and version of each program used, and the exact parameters and inputs[^sandve2013ten-e8]. For how, see [Organizing your research materials](../08_throughout/organizing_materials.md).

**Why**: when your results differ from the original, the first thing readers will ask is "did you change something?" Carver asks you to discuss whether your changes could have caused the differences[^carver2010towards-e6]; without a deviation log you cannot answer that.

**Where people go wrong**: changing things as you go and trying to remember them afterward. Small changes like a different library version or tweaked preprocessing are the easiest to forget, yet they may be exactly why the results differ.

### Step 5: Decide in advance what counts as a successful replication

**How:**

- **Don't demand identical numbers.** ACM's standard is that results agree within the tolerances acceptable for that kind of experiment[^acm2020artifact-e14], and that differences should not change the paper's main claims[^acm2020artifact-e15].
- **Set the criterion by the degree of replication.** What counts as "the same result" depends on which degree you are replicating at[^gundersen2018state-e7]. With the same implementation and the same data (R1), the results should be identical; with a different implementation (R2), the results should be the same but not necessarily identical, because differences can come from the implementation and the hardware, for example in how floating-point arithmetic is done[^gundersen2018state-e8]; with a different implementation and different data (R3), the question is whether the results support the same hypothesis[^gundersen2018state-e7].
- **Fix the criteria before you run anything.** If you decide "how close counts as success" after seeing the results, the criteria will drift, without your noticing, toward the outcome you hoped for.
- **Judge claim by claim; don't give one overall score.** "Is this paper reproducible?" rarely has a simple answer; most reproducibility reports give a nuanced account of how far the methods, results, and claims were each reproduced, which a single score cannot capture[^pineau2021improving-e6]. SIGSOFT requires you to distinguish clearly between results that agree and results that don't[^ralph2020empirical-e219], to distinguish large differences from small ones, and to analyze whether the differences are reasonable and expected[^ralph2020empirical-e222].
- **If results involve randomness, run multiple times.** Klees et al. found that on the program nm, a single run had AFL finding more crashes than AFLFast, but the median over 30 runs showed exactly the opposite[^klees2018evaluating-e11]. With only one run, "success" or "failure" may be luck. For how to report differences and uncertainty, see [Analysis and interpretation: report how big the difference is and how sure you are](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

### Step 6: Report the results

**How**: write up four kinds of information separately[^ralph2020empirical-e220]:

1. **The original study**: the information you gathered in Step 2[^ralph2020empirical-e216].
2. **This replication**: the motivation and type of replication[^ralph2020empirical-e214][^ralph2020empirical-e215], the interaction with the original authors[^carver2010towards-e2], and every change with its reason[^carver2010towards-e4].
3. **Comparison of results**: a dedicated section comparing the replication's results with the original results[^carver2010towards-e5]; you can put both sets side by side in one summary table[^carver2010towards-e10]. List the results that differ, and discuss whether your changes could have caused the differences[^carver2010towards-e6].
4. **Conclusions**: take the two studies together and give insights that neither study shows on its own, saying which of the original study's conclusions have been strengthened[^ralph2020empirical-e223][^carver2010towards-e7]; compare the limitations of both[^ralph2020empirical-e224].

When space is tight (for example in a conference paper), still give all four kinds of information, just more briefly; the comparison can be a table[^carver2010towards-e8]. If you have to cut something, the last thing to cut is the changes and differences from the original study[^carver2010towards-e9].

If the original study has already been replicated several times (a "family of replications"), briefly summarize the earlier studies and place your results within the whole family[^ralph2020empirical-e226][^carver2010towards-e11]. To combine results across studies statistically, see meta-analysis in [Review studies](review_study.md).

**Report it even if the replication failed.** For the general approach to reporting negative results, see [Analysis and interpretation: negative and unexpected results](../02_do-the-project/07_analyze-and-interpret.md#5-negative-and-unexpected-results). For replications, also keep these in mind:

- Overturning an established finding takes far more evidence than publishing a new one; it may take several teams showing beyond doubt that a result is wrong before the community changes its view[^pineau2021improving-e7]. So when you report a failed replication, be all the more complete about the deviation log, the number of runs, and your communication with the original authors.
- Write "we did not obtain the original results under these conditions", not "the original authors were wrong". The difference may come from your changes, from conditions the original paper did not state, or from the original conclusion itself.
- There are dedicated outlets for replication papers: some conferences have calls specifically for reproducibility papers (such as the European Conference on Information Retrieval, ECIR, in 2020), and there is an open-access journal, ReScience C, dedicated to publishing replications[^pineau2021improving-e9].

---

## 3. Checklist

Based on the SIGSOFT replication standard (written for software engineering; it has no Extraordinary tier).

**Essential**

- [ ] State the motivation for the replication[^ralph2020empirical-e214]
- [ ] State the type of replication along all three dimensions: method similarity, coverage, and team[^ralph2020empirical-e215]
- [ ] Describe the original study: research questions, design, context variables, and main findings[^ralph2020empirical-e216]
- [ ] Describe any overlap or interaction with the original authors[^ralph2020empirical-e217]
- [ ] Write down every difference from the original study, with its reason[^ralph2020empirical-e218]
- [ ] Compare the replication's results with the original results, clearly separating the ones that agree from the ones that don't[^ralph2020empirical-e219]

**Desirable**

- [ ] Write the original study, this replication, the comparison of results, and the conclusions as four separate parts[^ralph2020empirical-e220]
- [ ] Improve on the original study in design, analysis, or statistical power[^ralph2020empirical-e221]
- [ ] When discussing results that differ, distinguish large from small differences, and analyze whether they are reasonable and expected[^ralph2020empirical-e222]
- [ ] Draw conclusions from the two studies together, saying which of the original study's conclusions have been strengthened[^ralph2020empirical-e223]
- [ ] Compare the limitations of both, and propose hypotheses about new context variables that only show up when the studies are combined[^ralph2020empirical-e224]
- [ ] Have the original authors review the replication plan[^ralph2020empirical-e225]
- [ ] If there is a family of replications, summarize the earlier studies and place your results within the whole family[^ralph2020empirical-e226]
- [ ] Write down the success criteria before running anything

**Acceptable deviations (not flaws)**

- Not releasing materials that belong to the original authors when they have not given permission to release them[^ralph2020empirical-e229]

**Criticisms common in review that are not valid**

- "The replication only confirmed the original study and found no inconsistencies"[^ralph2020empirical-e228]
- Criticizing the research questions themselves or their wording: the research questions are set by the original study, and a replication must keep them[^ralph2020empirical-e230]
- Rejecting the paper because it repeats existing work[^ralph2020empirical-e62]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Vaguely "replicating a paper" without listing specific claims | Replication results can rarely be summed up as a single "yes" or "no"[^pineau2021improving-e6] |
| Copying the original study's low power or statistical mistakes | SIGSOFT lists this as an antipattern[^ralph2020empirical-e227] |
| Not recording changes, or recalling them afterward | When results differ, you can't tell whether a change caused it[^carver2010towards-e6] |
| Setting the success criteria after seeing the results | The criteria drift toward the outcome you hoped for |
| Running an experiment with randomness only once | A single run can lead to the opposite conclusion from many runs[^klees2018evaluating-e11] |
| Claiming the conclusion holds because the original code gave the same number | The original code may itself be wrong[^pineau2021improving-e4]; this is only R1, and doesn't show that the method itself works[^gundersen2018state-e3] |
| Not writing up a failed replication | Overturning an established finding needs extra evidence anyway[^pineau2021improving-e7], and your result is part of it |

---

## 5. Further reading

- **The replication standard in the SIGSOFT Empirical Standards**: the review criteria for replication papers; check against it item by item before you submit.
- **Carver 2010, Towards Reporting Guidelines for Experimental Replications**: only 4 pages; covers what goes in each part of a replication paper, and what to cut when a conference paper runs out of space.
- **ACM Artifact Review and Badging**: the formal definitions of repeatability, reproducibility, and replicability, and the note on swapping two of the terms.
- **Pineau et al. 2021, Improving Reproducibility in Machine Learning Research**: for machine learning. Covers why results are hard to reproduce, the NeurIPS reproducibility challenge, and what a good reproducibility report looks like.
- **Gundersen & Kjensmo 2018, State of the Art: Reproducibility in Artificial Intelligence**: the three degrees of reproducibility R1 to R3, and what information (method, data, experiment) the original paper must document for it to be reproduced.

For links to each source, see the [source list](../../sources/README.md).

[^ralph2020empirical-e208]: SIGSOFT Replication standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e208)
[^ralph2020empirical-e209]: SIGSOFT Replication standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e209)
[^ralph2020empirical-e210]: SIGSOFT Replication standard, Definitions. [Evidence](../../sources/notes/ralph2020empirical.md#e210)
[^ralph2020empirical-e211]: SIGSOFT Replication standard, footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e211)
[^ralph2020empirical-e212]: SIGSOFT Replication standard, footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e212)
[^ralph2020empirical-e213]: SIGSOFT Replication standard, footnote 3. [Evidence](../../sources/notes/ralph2020empirical.md#e213)
[^ralph2020empirical-e214]: SIGSOFT Replication standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e214)
[^ralph2020empirical-e215]: SIGSOFT Replication standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e215)
[^ralph2020empirical-e216]: SIGSOFT Replication standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e216)
[^ralph2020empirical-e217]: SIGSOFT Replication standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e217)
[^ralph2020empirical-e218]: SIGSOFT Replication standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e218)
[^ralph2020empirical-e219]: SIGSOFT Replication standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e219)
[^ralph2020empirical-e220]: SIGSOFT Replication standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e220)
[^ralph2020empirical-e221]: SIGSOFT Replication standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e221)
[^ralph2020empirical-e222]: SIGSOFT Replication standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e222)
[^ralph2020empirical-e223]: SIGSOFT Replication standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e223)
[^ralph2020empirical-e224]: SIGSOFT Replication standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e224)
[^ralph2020empirical-e225]: SIGSOFT Replication standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e225)
[^ralph2020empirical-e226]: SIGSOFT Replication standard, Desirable Attributes (families of replications). [Evidence](../../sources/notes/ralph2020empirical.md#e226)
[^ralph2020empirical-e227]: SIGSOFT Replication standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e227)
[^ralph2020empirical-e228]: SIGSOFT Replication standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e228)
[^ralph2020empirical-e229]: SIGSOFT Replication standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e229)
[^ralph2020empirical-e230]: SIGSOFT Replication standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e230)
[^ralph2020empirical-e62]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e62)
[^carver2010towards-e1]: Carver 2010, §2.3. [Evidence](../../sources/notes/carver2010towards.md#e1)
[^carver2010towards-e2]: Carver 2010, §3.1.2. [Evidence](../../sources/notes/carver2010towards.md#e2)
[^carver2010towards-e3]: Carver 2010, §1. [Evidence](../../sources/notes/carver2010towards.md#e3)
[^carver2010towards-e4]: Carver 2010, §3.1.2. [Evidence](../../sources/notes/carver2010towards.md#e4)
[^carver2010towards-e5]: Carver 2010, §3.1.3. [Evidence](../../sources/notes/carver2010towards.md#e5)
[^carver2010towards-e6]: Carver 2010, §3.1.3. [Evidence](../../sources/notes/carver2010towards.md#e6)
[^carver2010towards-e7]: Carver 2010, §3.1.4. [Evidence](../../sources/notes/carver2010towards.md#e7)
[^carver2010towards-e8]: Carver 2010, §3.3. [Evidence](../../sources/notes/carver2010towards.md#e8)
[^carver2010towards-e9]: Carver 2010, §3.3. [Evidence](../../sources/notes/carver2010towards.md#e9)
[^carver2010towards-e10]: Carver 2010, §2.3. [Evidence](../../sources/notes/carver2010towards.md#e10)
[^carver2010towards-e11]: Carver 2010, §3.2. [Evidence](../../sources/notes/carver2010towards.md#e11)
[^acm2020artifact-e5]: ACM 2020, Results Validated. [Evidence](../../sources/notes/acm2020artifact.md#e5)
[^acm2020artifact-e9]: ACM 2020, opening. [Evidence](../../sources/notes/acm2020artifact.md#e9)
[^acm2020artifact-e14]: ACM 2020, Results Validated. [Evidence](../../sources/notes/acm2020artifact.md#e14)
[^acm2020artifact-e15]: ACM 2020, Results Validated. [Evidence](../../sources/notes/acm2020artifact.md#e15)
[^acm2020artifact-e16]: ACM 2020, Terminology: Repeatability. [Evidence](../../sources/notes/acm2020artifact.md#e16)
[^acm2020artifact-e17]: ACM 2020, Terminology: Reproducibility. [Evidence](../../sources/notes/acm2020artifact.md#e17)
[^acm2020artifact-e18]: ACM 2020, Terminology: Replicability. [Evidence](../../sources/notes/acm2020artifact.md#e18)
[^acm2020artifact-e19]: ACM 2020, note in the terminology section. [Evidence](../../sources/notes/acm2020artifact.md#e19)
[^pineau2021improving-e1]: Pineau et al. 2021, §2.1. [Evidence](../../sources/notes/pineau2021improving.md#e1)
[^pineau2021improving-e2]: Pineau et al. 2021, §2. [Evidence](../../sources/notes/pineau2021improving.md#e2)
[^pineau2021improving-e3]: Pineau et al. 2021, §2 (paraphrasing Raff 2019). [Evidence](../../sources/notes/pineau2021improving.md#e3)
[^pineau2021improving-e4]: Pineau et al. 2021, §3. [Evidence](../../sources/notes/pineau2021improving.md#e4)
[^pineau2021improving-e5]: Pineau et al. 2021, §3. [Evidence](../../sources/notes/pineau2021improving.md#e5)
[^pineau2021improving-e6]: Pineau et al. 2021, §4. [Evidence](../../sources/notes/pineau2021improving.md#e6)
[^pineau2021improving-e7]: Pineau et al. 2021, §1. [Evidence](../../sources/notes/pineau2021improving.md#e7)
[^pineau2021improving-e8]: Pineau et al. 2021, §4. [Evidence](../../sources/notes/pineau2021improving.md#e8)
[^pineau2021improving-e9]: Pineau et al. 2021, §6. [Evidence](../../sources/notes/pineau2021improving.md#e9)
[^pineau2021improving-e10]: Pineau et al. 2021, §1. [Evidence](../../sources/notes/pineau2021improving.md#e10)
[^gundersen2018state-e1]: Gundersen & Kjensmo 2018, The Terminology of Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e1)
[^gundersen2018state-e2]: Gundersen & Kjensmo 2018, Degrees of Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e2)
[^gundersen2018state-e3]: Gundersen & Kjensmo 2018, Degrees of Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e3)
[^gundersen2018state-e4]: Gundersen & Kjensmo 2018, Introduction (paraphrasing Collberg & Proebsting 2016). [Evidence](../../sources/notes/gundersen2018state.md#e4)
[^gundersen2018state-e5]: Gundersen & Kjensmo 2018, Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e5)
[^gundersen2018state-e6]: Gundersen & Kjensmo 2018, Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e6)
[^gundersen2018state-e7]: Gundersen & Kjensmo 2018, Reproducibility; Degrees of Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e7)
[^gundersen2018state-e8]: Gundersen & Kjensmo 2018, Degrees of Reproducibility. [Evidence](../../sources/notes/gundersen2018state.md#e8)
[^gundersen2018state-e9]: Gundersen & Kjensmo 2018, Abstract. [Evidence](../../sources/notes/gundersen2018state.md#e9)
[^klees2018evaluating-e3]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e3)
[^klees2018evaluating-e11]: Klees et al. 2018, §1. [Evidence](../../sources/notes/klees2018evaluating.md#e11)
[^sandve2013ten-e8]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e8)
