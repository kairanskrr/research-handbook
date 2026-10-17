# Synthesis

> This page describes a research strategy, and the reasoning applies to every field. The examples and concrete steps come from computer science; where medicine and other fields work differently, we point it out.

You have read dozens of papers on large language models and smart-contract security, and the more you read, the more you feel that each paper goes its own way and nobody has ever looked at them together. So you wonder: could you treat the existing research itself as your object of study, and write a paper that lets the whole area see itself clearly?

That is the **synthesis** strategy: instead of collecting new experimental data yourself, you systematically collect, appraise and pull together studies others have already published, to answer a question no single study can answer. For an overview of research strategies, see [Key concepts](../00_start-here/key-concepts.md#research-strategy).

## 1. What kind of knowledge this research produces

Synthesis produces **a picture of what is already known, taken as a whole**: what the area has studied, what the evidence says when put together, where the gaps are, and what has been done wrong.

Within the same area, a synthesis can make several kinds of claim. Different claims call for different types of review:

| The claim you want to make (example) | Suitable review type | What it produces |
|---|---|---|
| "Research in this area falls into four categories, and there are three gaps" | Systematic mapping study (outside software engineering often called a scoping review)[^ralph2022paving-e3] | Categories and counts: a "map" of the research |
| "The existing evidence shows that prompting with vulnerability patterns raises the detection rate" | Systematic review: identifying, appraising and interpreting all the studies relevant to a specific question[^kitchenham2007guidelines-e2] | An evidence-based answer to that question |
| "If we pool the detection rates from all the experiments, how big is the improvement?" | Meta-analysis: using statistical methods to combine the results of several studies into a single effect size[^murad2016new-e7] | One pooled number |
| "In published audit cases, teams that did a certain thing ran into fewer incidents" | Case survey: turning the written descriptions in published case studies into data, then analyzing that data[^ralph2020empirical-e291] | Conclusions drawn from many cases |
| "Most papers in this area share the same flaw in how they evaluate" | Critical review: analyzing a body of research to support an argument or a critique[^ralph2022paving-e12] | Specific criticisms of, and recommendations for, research practice |
| "Here is a framework for understanding this area" | Survey paper: classifying the literature, building a perspective on the field and assessing trends[^acm2026csurguidelines-e1] | A classification framework and judgments about the field |

There is also a familiar kind of review: the related-work section in every paper, where the authors purposefully pick some literature to discuss[^ralph2022paving-e1]. It is good for developing theory and spotting promising topics, but because the papers are hand-picked, it suffers from sampling bias, can't be reproduced, and can't support empirical conclusions like "X causes Y"[^ralph2022paving-e2].

This gives one rule that runs through the whole page: **the stronger the conclusion you want to draw, the more systematic your review has to be.**

Another kind synthesizes the findings of multiple qualitative studies, for example meta-ethnography and narrative synthesis[^ralph2020empirical-e292]. Our sources do not cover how to do it.

**Write it down:** Using the format of the table above, write the one-sentence claim you want to make, and compare it with the two right-hand columns to decide which type of review it calls for.

## 2. What evidence is enough

In a synthesis, the evidence is **which studies you found, why you included them, what you extracted from them, and how you combined them**. Whether readers can trust your conclusion depends on whether these four things hold up to scrutiny.

A few basics apply to every systematic kind of review: describe the search process and the selection criteria step by step[^ralph2020empirical-e4]; write a protocol before you start searching, so you don't pick papers or run analyses to fit what you expect[^kitchenham2007guidelines-e7]; make the chain of evidence from extracted data to the answer clear, since listing "A found X, B found Y" paper by paper is not synthesis[^ralph2020empirical-e6][^ralph2020empirical-e16]; and assess each study's quality against criteria fixed in advance, not by the prestige of the conference or journal[^ralph2020empirical-e10][^ralph2020empirical-e16]. For how to do each step, see [How to do a systematic review](../06_methods/review_study.md#2-how-to-do-a-systematic-review) and the [Checklist](../06_methods/review_study.md#5-checklist) in the methods page [Review studies](../06_methods/review_study.md).

The extra step this page asks of you: **"enough" means different things for different types of review.** Use the wrong standard and you either waste effort or leave a serious flaw for reviewers to find. Reviewers can get it wrong too, for example by demanding that a critical review "find all the studies" or "exclude low-quality studies"[^ralph2022paving-e20].

| Review type | Must the search be exhaustive? | Must each study's quality be appraised? | Key requirement |
|---|---|---|---|
| Systematic mapping study | Search is similar to a systematic review[^ralph2022paving-e4]; completeness matters less than in a meta-analysis[^ralph2020empirical-e9] | Usually not[^petersen2008systematic-e4] | Clear categories and counts |
| Systematic review | As complete as possible[^kitchenham2007guidelines-e2] | Yes[^kitchenham2007guidelines-e13] | A clear chain of evidence from data to answer[^ralph2020empirical-e6] |
| Meta-analysis | Higher bar than a mapping study on a broad topic[^ralph2020empirical-e9] | Yes, focusing on the risk of bias in the results[^higgins2024cochrane-e21] | Studies must be similar enough to combine[^higgins2024cochrane-e15] |
| Case survey | A reproducible search for published cases[^ralph2020empirical-e293] | Desirable[^ralph2020empirical-e301] | A coding scheme fixed in advance[^ralph2022paving-e7][^ralph2020empirical-e295]; needs a large number of cases[^ralph2022paving-e10] |
| Critical review | No; a random sample from top journals and conferences is enough[^ralph2022paving-e15] | Not held to "exclude low-quality studies"[^ralph2022paving-e20] | Goes beyond description to make specific criticisms[^ralph2022paving-e16] |

So the first thing to do is **state in your paper which type of review you did**[^ralph2020empirical-e3], and argue that the rigor of your search matches your goal[^ralph2020empirical-e9].

> **Where sources disagree: is a mapping study that only classifies and counts worth doing on its own?**
> - Yes: mapping studies and systematic reviews differ in goals, scope and validity concerns, and the two should complement each other; mapping studies are useful in more situations than people usually assume[^petersen2008systematic-e7].
> - Not enough: a mostly descriptive scoping review (that is, a mapping study) usually lacks synthesis and can't answer important empirical questions[^ralph2022paving-e4]. The two authors, writing about software engineering, say that mostly descriptive scoping reviews are "essentially works-in-progress" and should go to workshops, poster sessions or short-paper tracks; if the literature does support synthesis, a scoping review is more like a pilot study for a full systematic review[^ralph2022paving-e5].
>
> What this means for you: a mapping study is useful in itself, but if you are aiming at a main conference track or a journal, it is better to go one step beyond categories and counts and actually synthesize conclusions.

**Write it down:** Write down the review type you chose and, column by column from the table above, how far you plan to go: which sources you will search, whether you will appraise quality, and how you will meet the key requirement.

## 3. Common research methods

For how to do it, see these methods pages:

- [Review studies: systematic reviews, mapping studies, and survey papers](../06_methods/review_study.md): the full process of protocol, search, selection, extraction and reporting.
- [Case survey](../06_methods/case_survey.md): coding published case studies into a dataset.
- [Methodology research and meta-science](../06_methods/meta_science.md): critical reviews belong to the field's internal discussion of how to do research, which is meta-science[^ralph2022paving-e14].
- [Systematic reviews and meta-analysis (health research)](../06_methods/meta_analysis.md): effect measures, fixed-effect and random-effects models, heterogeneity, and grading the certainty of evidence.

**Don't jump straight into** the statistics of a meta-analysis: if the question definition, inclusion criteria, search and selection, data collection or risk-of-bias assessment are poorly done, the pooled result can be badly misleading[^higgins2024cochrane-e14]. A systematic review doesn't have to include a meta-analysis either; when study results vary a lot, reporting an average effect can itself be misleading[^higgins2024cochrane-e16].

## 4. How it shapes the whole project

Once you choose synthesis, every stage of the project looks a bit different from the other strategies:

| Stage | What is different in a synthesis project |
|---|---|
| [Converging on a project](../01_find-a-problem/05_converge.md) | First confirm that the review is actually needed[^kitchenham2007guidelines-e5], for example by checking whether someone has already done a similar one; if so, work out what you can add, such as a newer time period or a different question |
| [Writing a research plan](../02_do-the-project/03_research-plan.md) | The research question is the most important part of planning[^kitchenham2007guidelines-e6]; the protocol is critical to a systematic review[^kitchenham2007guidelines-e9]. A high-quality systematic review tends to be laborious and time-consuming[^higgins2024cochrane-e4], so don't be optimistic when scheduling |
| [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) | The evidence is the literature itself; your research questions directly decide your search terms, selection criteria and the data you extract |
| [The smallest version that runs end to end](../02_do-the-project/05_pilot-and-derisk.md) | Once your selection criteria are set, try them on a small batch of papers first[^kitchenham2007guidelines-e8]; run a pilot search to see roughly how many relevant studies there are |
| [Running and iterating](../02_do-the-project/06_run-and-iterate.md) | Most of the work is selection and extraction; be inclusive in the first round of screening[^kitchenham2007guidelines-e11]. If you are working alone, ask your advisor to extract data from a sample of the papers as well, and cross-check[^kitchenham2007guidelines-e15] |
| [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md) | Put your results back in the context of existing research and point out gaps and directions; clearly separate evidence-based results from your own speculation[^ralph2020empirical-e13] |
| [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md) | Follow the reporting guideline: give the full search strings and draw a flow diagram from search to inclusion[^page2021prisma-e3][^page2021prisma-e4]; publish your protocol, search results, data and scripts[^ralph2020empirical-e7] |
| [Choosing a venue and submitting](../03_write-and-publish/02_venue-and-submission.md) | Survey journals may have length limits; for example, a long survey in ACM Computing Surveys may not exceed 35 pages including references[^acm2026csurguidelines-e4]. If you only have a mapping study that classifies and counts, see "Where sources disagree" above |

One use that is often overlooked: a synthesis project is often the starting point for other projects. A mapping study can show where research clusters and where the gaps are, pointing the way for later systematic reviews and new studies[^kitchenham2007guidelines-e3]. In medicine, the Cochrane Handbook says that a systematic review should generally be done before starting new primary research[^higgins2024cochrane-e3].

**Write it down:** Estimate roughly how many papers your search will return and how many you can screen in a week, and work out how many weeks screening will take.

## 5. Which fields use it

We cover only what our sources support:

- **Medicine and public health**: there is a dedicated methods handbook for systematic reviews of interventions (the Cochrane Handbook)[^higgins2024cochrane-e12], covering clinical interventions as well as public-health and policy ones[^higgins2024cochrane-e11]; reporting follows the 27-item checklist of PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)[^page2021prisma-e1]. The traditional evidence pyramid puts systematic reviews and meta-analyses at the top[^murad2016new-e1], but some argue for taking them off the top and using them as a "lens" through which to view other studies[^murad2016new-e6]: a meta-analysis that pools randomized controlled trials at low risk of bias and one that pools observational studies at high risk of bias should not be treated as equivalent[^murad2016new-e5].
- **Software engineering**: the Association for Computing Machinery's Special Interest Group on Software Engineering (ACM SIGSOFT) Empirical Standards include a dedicated standard for systematic reviews[^ralph2020empirical-e1] and one for case surveys[^ralph2020empirical-e291].
- **Management and information systems**: case surveys are widely used there; in software engineering they are still rare[^ralph2022paving-e9].
- **Law**: doctrinal research (the analysis of statutes and case law) is more than a literature review[^hutchinson2012defining-e8]; see the [law field overview](../07_fields/law/README.md).

Our sources do not cover how other fields (for example, research reviews in the humanities) view synthesis.

## 6. Common mistakes

These are mistakes at the level of the strategy. For common mistakes in searching, selection and extraction, see [Common mistakes in review studies](../06_methods/review_study.md#6-common-mistakes).

| Mistake | Why it is a problem |
|---|---|
| Not saying which type of review you did | Readers and reviewers don't know which standard to judge it by[^ralph2020empirical-e3] |
| Using a hand-picked review to support "X is better than Y" | Hand-picked literature is biased and can't support empirical conclusions[^ralph2022paving-e2] |
| Drawing conclusions by vote counting | Just counting how many studies were significant and how many weren't is a seriously flawed method[^higgins2024cochrane-e18] |
| Forcing very different studies into a single number | When the populations, interventions or outcomes are not similar enough, the pooled result can mislead[^higgins2024cochrane-e15] |
| Doing a systematic review in an area with very few high-quality studies | You can't reach reliable conclusions[^ralph2020empirical-e16]; a mapping study is the better first step[^kitchenham2007guidelines-e3] |
| Naming and criticizing specific papers in a critical review | The added credibility isn't worth the damage to relationships in the research community; you can use hypothetical examples instead[^ralph2022paving-e19][^ralph2020empirical-e312] |
| Treating correlations in a case survey as causation | This is a listed antipattern for case surveys[^ralph2020empirical-e304] |

## 7. Further reading

- **The full range of review types**: Ralph and Baltes 2022, which maps out seven types of literature review. Read it first, then decide which type to do.
- **The full systematic review process**: Kitchenham and Charters 2007, the guidelines for systematic reviews in software engineering.
- **Mapping studies**: Petersen et al. 2008.
- **Snowballing searches**: Wohlin 2014.
- **Reporting guideline**: PRISMA 2020 (Page et al. 2021), the reporting guideline for systematic reviews and meta-analyses, with a checklist and a flow-diagram template.
- **Meta-analysis**: the Cochrane Handbook (Higgins et al. 2024); read Chapters 1 and 10 first.
- **Quality standards**: the systematic review, case survey and meta-science standards in the ACM SIGSOFT Empirical Standards.

Links to all of these are in the [source list](../../sources/README.md).

[^acm2026csurguidelines-e1]: ACM Computing Surveys author guidelines, Long Survey Paper. [Evidence](../../sources/notes/acm2026csurguidelines.md#e1)
[^acm2026csurguidelines-e4]: ACM Computing Surveys author guidelines, Paper Length. [Evidence](../../sources/notes/acm2026csurguidelines.md#e4)
[^higgins2024cochrane-e3]: Cochrane Handbook, Chapter 1 §1.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e3)
[^higgins2024cochrane-e4]: Cochrane Handbook, Chapter 1 §1.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e4)
[^higgins2024cochrane-e11]: Cochrane Handbook, Chapter 1 §1.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e11)
[^higgins2024cochrane-e12]: Cochrane Handbook, Chapter 1 §1.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e12)
[^higgins2024cochrane-e14]: Cochrane Handbook, Chapter 10 §10.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e14)
[^higgins2024cochrane-e15]: Cochrane Handbook, Chapter 10 §10.10.1. [Evidence](../../sources/notes/higgins2024cochrane.md#e15)
[^higgins2024cochrane-e16]: Cochrane Handbook, Chapter 10 §10.10.3. [Evidence](../../sources/notes/higgins2024cochrane.md#e16)
[^higgins2024cochrane-e18]: Cochrane Handbook, Chapter 12 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e18)
[^higgins2024cochrane-e21]: Cochrane Handbook, Chapter 7 Key Points. [Evidence](../../sources/notes/higgins2024cochrane.md#e21)
[^hutchinson2012defining-e8]: Hutchinson & Duncan 2012, §III B 1. [Evidence](../../sources/notes/hutchinson2012defining.md#e8)
[^kitchenham2007guidelines-e2]: Kitchenham & Charters 2007, §2. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e2)
[^kitchenham2007guidelines-e3]: Kitchenham & Charters 2007, §2.5.1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e3)
[^kitchenham2007guidelines-e5]: Kitchenham & Charters 2007, §5.1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e5)
[^kitchenham2007guidelines-e6]: Kitchenham & Charters 2007, §5.3.1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e6)
[^kitchenham2007guidelines-e7]: Kitchenham & Charters 2007, §5.4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e7)
[^kitchenham2007guidelines-e8]: Kitchenham & Charters 2007, §5.4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e8)
[^kitchenham2007guidelines-e9]: Kitchenham & Charters 2007, §5.5. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e9)
[^kitchenham2007guidelines-e11]: Kitchenham & Charters 2007, §6.2.2. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e11)
[^kitchenham2007guidelines-e13]: Kitchenham & Charters 2007, §6.3. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e13)
[^kitchenham2007guidelines-e15]: Kitchenham & Charters 2007, §6.4.3. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e15)
[^murad2016new-e1]: Murad et al. 2016. [Evidence](../../sources/notes/murad2016new.md#e1)
[^murad2016new-e5]: Murad et al. 2016. [Evidence](../../sources/notes/murad2016new.md#e5)
[^murad2016new-e6]: Murad et al. 2016. [Evidence](../../sources/notes/murad2016new.md#e6)
[^murad2016new-e7]: Murad et al. 2016. [Evidence](../../sources/notes/murad2016new.md#e7)
[^page2021prisma-e1]: PRISMA 2020 (Page et al. 2021). [Evidence](../../sources/notes/page2021prisma.md#e1)
[^page2021prisma-e3]: PRISMA 2020, Item 7. [Evidence](../../sources/notes/page2021prisma.md#e3)
[^page2021prisma-e4]: PRISMA 2020, Item 16a. [Evidence](../../sources/notes/page2021prisma.md#e4)
[^petersen2008systematic-e4]: Petersen et al. 2008, §3.2. [Evidence](../../sources/notes/petersen2008systematic.md#e4)
[^petersen2008systematic-e7]: Petersen et al. 2008, Abstract and §1. [Evidence](../../sources/notes/petersen2008systematic.md#e7)
[^ralph2020empirical-e1]: SIGSOFT Systematic Reviews standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e1)
[^ralph2020empirical-e3]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e3)
[^ralph2020empirical-e4]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e4)
[^ralph2020empirical-e6]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e6)
[^ralph2020empirical-e7]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e7)
[^ralph2020empirical-e9]: SIGSOFT Systematic Reviews standard, Desirable Attributes and footnote 3. [Evidence](../../sources/notes/ralph2020empirical.md#e9)
[^ralph2020empirical-e10]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e10)
[^ralph2020empirical-e13]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e13)
[^ralph2020empirical-e16]: SIGSOFT Systematic Reviews standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e16)
[^ralph2020empirical-e291]: SIGSOFT Case Survey standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e291)
[^ralph2020empirical-e292]: SIGSOFT Case Survey standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e292)
[^ralph2020empirical-e293]: SIGSOFT Case Survey standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e293)
[^ralph2020empirical-e295]: SIGSOFT Case Survey standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e295)
[^ralph2020empirical-e301]: SIGSOFT Case Survey standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e301)
[^ralph2020empirical-e304]: SIGSOFT Case Survey standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e304)
[^ralph2020empirical-e312]: SIGSOFT Methodological Guidelines and Meta-Science standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e312)
[^ralph2022paving-e1]: Ralph & Baltes 2022, §2.1. [Evidence](../../sources/notes/ralph2022paving.md#e1)
[^ralph2022paving-e2]: Ralph & Baltes 2022, §2.1. [Evidence](../../sources/notes/ralph2022paving.md#e2)
[^ralph2022paving-e3]: Ralph & Baltes 2022, §2.2.5. [Evidence](../../sources/notes/ralph2022paving.md#e3)
[^ralph2022paving-e4]: Ralph & Baltes 2022, §2.2.5. [Evidence](../../sources/notes/ralph2022paving.md#e4)
[^ralph2022paving-e5]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e5)
[^ralph2022paving-e7]: Ralph & Baltes 2022, §2.2.3. [Evidence](../../sources/notes/ralph2022paving.md#e7)
[^ralph2022paving-e9]: Ralph & Baltes 2022, §2.2.3. [Evidence](../../sources/notes/ralph2022paving.md#e9)
[^ralph2022paving-e10]: Ralph & Baltes 2022, §3. [Evidence](../../sources/notes/ralph2022paving.md#e10)
[^ralph2022paving-e12]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e12)
[^ralph2022paving-e14]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e14)
[^ralph2022paving-e15]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e15)
[^ralph2022paving-e16]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e16)
[^ralph2022paving-e19]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e19)
[^ralph2022paving-e20]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e20)
