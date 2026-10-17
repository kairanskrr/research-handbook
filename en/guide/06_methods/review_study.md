# Review studies: systematic reviews, mapping studies, and survey papers

This page covers **research where the review itself is the result**: you collect studies that others have published, synthesize and analyze them, and write it all up as a paper in its own right.

If what you want is "how to read the literature and write related work before doing your own study", that is a step in every project; see [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md).

**Scope** `[Our analysis]`: the standards and examples on this page come mainly from computer science, especially software engineering. The approach to systematic reviews follows the guidelines Kitchenham and Charters wrote for software engineering; the checklist follows the Empirical Standards of the Association for Computing Machinery's Special Interest Group on Software Engineering (ACM SIGSOFT); the requirements for survey papers follow the author guidelines of ACM Computing Surveys; and the reporting guideline PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) comes from medicine. If you are writing a review in another field, check your own field's standards first. For systematic reviews and meta-analyses in health (effect measures, heterogeneity, grading the certainty of evidence, and so on), see [Systematic reviews and meta-analysis (health research)](meta_analysis.md).

**Strategies it usually serves**: [Synthesis](../05_research-strategies/synthesize.md); when the answer may already be in the literature, also [Description](../05_research-strategies/observe_describe.md).

**After reading this page, you should be able to:**

- tell apart the three common kinds of review, and pick the right one for your question;
- carry out a systematic review or mapping study step by step;
- write a survey paper that adds value, rather than a list of papers;
- check your review against the checklist at the end.

---

## 1. First, pick the right type

Three kinds of review are common in computer science. What separates them is not "how many papers you read" but **what question you are answering and how rigorous you need to be**.

| | Survey paper | Mapping study | Systematic review |
|---|---|---|---|
| Question it answers | What are the important works in this field, and how should we understand them? | What research exists in this field, where is it concentrated, and where are the gaps? | On a specific question, what does the existing evidence show? |
| How papers are found | Selected by the authors for a purpose | Searched following a protocol fixed in advance, aiming for completeness | Searched following a protocol fixed in advance, aiming for completeness |
| Is each paper's quality assessed? | Usually not | Usually not | Yes |
| Main output | A classification framework, a perspective on the field, an assessment of trends | Classification and counts, drawing a "map" of the research | Evidence-based conclusions and recommendations |

Sources: the definition of a survey paper comes from ACM Computing Surveys[^csur-e1]; the difference between mapping studies and systematic reviews comes from Petersen et al.[^pe-e3][^pe-e4] "Selected for a purpose" refers to what Ralph and Baltes call an ad hoc review: the authors pick literature that is useful, relevant, or supports their own view[^rb-e1]; survey papers usually fall into this category. `[Our analysis]`

**How to choose** `[Our analysis, based on the sources below]`:

- **You want to give a panoramic view of a field and a framework for understanding it**: write a survey paper. This is the most common form of review in computer science.
- **The field is broad, or you don't yet know how much relevant research exists**: start with a mapping study. When there is little evidence or the topic is very broad, Kitchenham (Barbara Kitchenham, author of the guidelines for systematic reviews in software engineering) recommends a mapping study first, to find where research clusters and where the gaps are[^kc-e3].
- **You want to answer a specific question, such as "does method A find more defects than method B?"**: do a systematic review. Empirical conclusions like this need a review that searches systematically and assesses the quality of each study, such as a systematic review or a meta-analysis (combining the numerical results of several studies with statistical methods); a hand-picked review cannot support them[^kc-e2][^rb-e2].

The three are not sharply separated. The deeper a mapping study goes into the papers, the more it resembles a systematic review; the two can be seen as different points on a continuum[^pe-e6].

> **Where sources disagree: are mapping studies worth doing?**
> - Petersen et al. argue that mapping studies and systematic reviews have different goals and should complement each other, and that mapping studies are useful in more situations than is commonly thought[^pe-e7].
> - Ralph and Baltes take this view of scoping reviews (which are close to mapping studies[^rb-e3]): a scoping review that mainly describes and counts usually cannot answer important empirical questions and is "essentially works-in-progress"; it is better suited to a workshop (a smaller meeting attached to a major conference, with a lower bar for acceptance) or a short paper; and if there is enough literature for synthesis, it is more like a pilot for a full systematic review[^rb-e4][^rb-e5].
>
> In practice: a mapping study is useful in itself, but **classification and counts alone are not enough**. Taking one more step toward synthesis and conclusions makes it far more valuable.

---

## 2. How to do a systematic review

Under the software engineering guidelines for systematic reviews, the core requirements are that the review be **thorough, fair, and reproducible**. Kitchenham and Charters state at the very start of their guidelines that a literature review that is not thorough and fair has little scientific value[^kc-e1]. The process has three phases: planning, conducting, and reporting[^kc-e4].

### Phase 1: Planning

**1. Confirm the review is worth doing.** Before you start, confirm that the review is really needed, for example by checking whether someone has already done a similar one[^kc-e5]. If they have, work out what yours adds, for example covering a newer time period or answering a different question. `[Our analysis]`

**2. Write down the research questions.** This is the most important step in planning[^kc-e6]: the search terms, selection criteria, and data to extract later all follow from the research questions.

**3. Write a review protocol.** Before you start searching, write down the following[^kc-e7]:

- Background: why the review is needed
- The research questions
- The search strategy: which search terms, and which databases, journals, and conferences you will search
- Inclusion and exclusion criteria, and the selection procedure (how many people screen, and how disagreements are resolved)
- Quality assessment criteria
- What data to extract, and how to synthesize it
- The timeline

> **Why write the protocol first?** Without one, you are likely to pick papers and run analyses according to your own expectations without realizing it[^kc-e7]. Writing the protocol first means committing yourself in advance.

**4. Pilot and review the protocol.** Try the selection criteria on a small batch of papers first[^kc-e8]. The protocol is a critical element of a systematic review[^kc-e9], so it is best to have your advisor or a colleague look it over. `[Our analysis]`

### Phase 2: Conducting the review

**1. Search: combine several approaches; don't rely on a single database.**

Using only one search approach makes it easy to miss papers, and also brings in publication bias: positive results are more likely to be published than negative ones[^kc-e10]. Choose several of the following to combine; you don't need all of them[^sig-e8]:

- Keyword searches in databases, plus hand-searching important journals and conferences
- Snowballing (see below)
- Checking the publication lists of prolific authors in the field
- Formal databases (such as the ACM Digital Library) plus Google Scholar
- Theses and preprints (such as arXiv)
- Contacting authors in the field

How rigorous the search needs to be depends on the review's goal: a meta-analysis needs to be as complete as possible, while a mapping study of a broad topic can be looser[^sig-e9]. For reference: one study redid a systematic review combining database search with snowballing, and found 30% more relevant studies than the original review, which used database search alone[^w22-e1].

**How to snowball:**

- **Backward snowballing**: go through a paper's reference list; **forward snowballing**: look at the papers that cite it[^w14-e1].
- **Start from a diverse set of papers**: cover different research communities, publishers, years, and authors; start from the keywords of your research question and consider synonyms. Otherwise you may find only one cluster of papers that cite each other and miss another cluster with no citation links to it[^w14-e3]. You can use Google Scholar to find the start set, to avoid favoring any one publisher[^w14-e2].
- **Deciding whether a reference is worth reading**: first exclude on basic criteria such as language, year, and type of publication, then remove the ones you have already seen; for what remains, look at where and in what context it is cited in the paper, and then decide whether to read it[^w14-e5].
- **Only snowball from papers you have included**: a paper must be read in full and included before you use it for the next round. Otherwise, if it is later excluded, everything found through it has to be backed out and redone[^w14-e4].
- **When to stop**: stop when neither backward nor forward snowballing turns up any new papers[^w14-e6].

**2. Selection: start broad, then get strict.**

- In the first round, look only at titles and abstracts, and apply the criteria liberally: unless a paper can clearly be excluded, get the full text[^kc-e11].
- Abstracts of software engineering papers are often poorly written, so don't decide on the abstract alone; also look at the conclusions[^kc-e11].
- When several people screen, measure agreement with Cohen's Kappa (a statistic for how far two people's judgments agree). If you work alone, you can re-judge a random sample of papers after some time has passed and see whether your decisions are consistent[^kc-e12].

**3. Assess the quality of each study.**

On top of the inclusion and exclusion criteria, assess how well each study was done[^kc-e13]. Use criteria fixed in advance, for example, in software engineering, the SIGSOFT empirical standard for the relevant research method. You can exclude low-quality studies, but a better approach is to include quality in the analysis and see whether it affects the conclusions[^sig-e10].

Two things to keep in mind:

- **Not reported does not mean not done.** If you are unsure, contact the original authors[^kc-e14].
- **Don't use the rank of the venue as a stand-in for quality assessment**[^sig-e16].

**4. Extract the data.**

Design the extraction form in advance, and make every item on it correspond to a research question[^sig-e5]. If you can, have two people extract independently and then compare; if you work alone (for example as a PhD student), you can ask your advisor to extract a random sample of the papers as well and cross-check[^kc-e15].

**5. Synthesize.**

Synthesis means bringing together the results of the included studies to answer the research questions. The most basic form is descriptive synthesis: tabulating the extracted information by research question; where possible, you can go on to a quantitative synthesis with statistical methods, that is, a meta-analysis[^kc-e16].

The most common mistake is **listing papers one by one**: "A found X, B found Y…". That is not synthesis[^sig-e16]. A good synthesis has a clear chain of evidence from the data to the conclusions[^sig-e6], and clearly separates results backed by evidence from your own interpretation and speculation[^sig-e13]. In a meta-analysis, don't use "vote counting", that is, just counting how many studies are for and how many against[^sig-e12].

### Phase 3: Reporting

We recommend writing the report following PRISMA 2020. PRISMA is a reporting guideline for systematic reviews that comes from medicine and has been widely adopted in software engineering and other fields. The 2020 version is a 27-item checklist[^pr-e1]. It covers how to report, not how to conduct a review, but it is best to read it at the planning stage so that you record everything you will need[^pr-e2]. A few things that are easy to miss:

- Give the **full search strings** for every database, including any filters[^pr-e3];
- Use a **flow diagram** to report how many records remained and how many were excluded at each step[^pr-e4];
- State **how many people screened each record, whether they worked independently**, and whether any automation tools were used[^pr-e5];
- Make the protocol, search results, screening records, extracted data, and analysis scripts publicly available[^sig-e7].

---

## 3. How to do a mapping study

The search and selection in a mapping study are similar to a systematic review. The main difference is that a mapping study **usually does not assess the quality of individual papers**, so it can cover more papers and chart a larger area[^pe-e4]. It has five steps[^pe-e1]:

1. Define the research questions, for example "which subtopics has this field studied, and how many papers are there on each?"
2. Search
3. Screen
4. Keyword the abstracts and build a classification scheme
5. Extract data according to the classification scheme and draw the map, for example a bubble plot showing how many papers fall where the categories intersect[^pe-e8]

**How to build the classification scheme**[^pe-e2]: first read each paper's abstract and pick out keywords that reflect its contribution; then combine the keywords from all papers and cluster them into categories. If the abstract does not give enough information, look at the introduction or conclusion.

**Watch out**: if you include only papers that use a particular research method, for example only those with experiments, and then use them to describe the whole field, the picture will be biased[^pe-e5].

---

## 4. How to write a survey paper

A survey paper does not need to find everything the way a systematic review does, and it does not need to assess each paper's quality. But that doesn't mean "read a pile of papers and describe them one by one" is enough.

**A good survey paper does three things**[^csur-e1]:

1. **Classifies the existing literature**: it proposes a clear classification framework (taxonomy) that lets readers see at a glance what parts the field is made of.
2. **Develops a perspective on the field**: it doesn't just describe what each paper did; it explains how the papers relate to each other, what each one solved, and what problems remain.
3. **Assesses trends**: where the field is heading, and which directions are worth pursuing.

**A survey paper is not a tutorial.** A tutorial is for newcomers, explaining basic concepts with concrete examples; a survey assumes readers already have basic knowledge and focuses on classification and perspective[^csur-e2]. Decide who your readers are before you start writing.

**Be clear about its limits.** In a survey paper, the authors choose the papers, so there is sampling bias, the review cannot be reproduced, and it is easy to pick only the evidence that supports your own view[^rb-e2]. So:

- Ralph and Baltes consider this kind of review suitable for developing theory, finding promising research topics, and preparing for qualifying exams[^rb-e2]; giving a panoramic view of a field and proposing a framework for understanding it fall under the same kind of use `[Our analysis]`;
- it is **not suitable** for supporting empirical conclusions such as "X is better than Y". For those you need a systematic review[^rb-e2].

**Practical advice** `[Our analysis]`:

- **Explain how you found the papers.** Even without a systematic search, say where you looked, what criteria you used to choose, and what years you cover. This goes a long way toward dispelling the suspicion that you "only picked the papers you liked", and adds almost no work. It borrows the reproducibility requirement of systematic reviews[^kc-e1][^sig-e4].
- **Organize the body around the classification framework, not paper by paper.** Listing papers one by one is an antipattern for systematic reviews[^sig-e16], and the same holds for survey papers.
- **End each category with a short summary**: the common idea behind that category of methods, their respective strengths and weaknesses, and the problems still open.

---

## 5. Checklist

The items below are based mainly on the ACM SIGSOFT standard for systematic reviews, which was written for software engineering. For mapping studies and survey papers, use whichever items apply; in other fields, follow your own field's standards.

**Essential**

- [ ] State what kind of review you are doing[^sig-e3]
- [ ] Describe the search process step by step, reproducibly, including the search terms[^sig-e4]
- [ ] Give clear inclusion and exclusion criteria[^sig-e4]
- [ ] State what data you extract from each paper, how it relates to the research questions, and how you extract and synthesize it[^sig-e5]
- [ ] Have a clear chain of evidence from the data to the conclusions[^sig-e6]
- [ ] Give conclusions or recommendations for practitioners or non-specialist readers[^sig-e6]
- [ ] Disclose the main limitations, and don't draw conclusions beyond the evidence[^sig-e18]

**Desirable**

- [ ] Combine several search approaches to reduce missed papers and publication bias[^sig-e8]
- [ ] Assess the quality of each study using criteria fixed in advance[^sig-e10]
- [ ] Have two or more people screen and extract independently, and report agreement and how disagreements were resolved (for reviews with a mainly positivist orientation)[^sig-e11]
- [ ] Include a PRISMA flow diagram[^sig-e12]
- [ ] Make the protocol, search results, screening records, data, and scripts publicly available[^sig-e7]
- [ ] Place the results within existing research, and point out gaps and future directions; separate evidence from speculation[^sig-e13]

**Extraordinary**

- [ ] Have two or more people run independent preliminary searches before settling the search terms[^sig-e14]
- [ ] Contact the original authors to confirm your interpretation, or to get data not reported in their papers[^sig-e14]

**Acceptable deviations (not flaws)**[^sig-e15]

- When studying one particular conference or journal, you need not address publication bias
- When there are thousands of papers, you can take a random sample

**Criticisms common in review that are not valid**[^sig-e17]: you don't need to worry about these

- "The search strings are not exactly the same across databases"
- "The analysis should be more qualitative" or "more quantitative"

---

## 6. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Starting the search without a protocol | It's easy to pick papers according to your own expectations[^kc-e7] |
| Using only one database | You miss papers and make publication bias worse[^kc-e10][^sig-e8] |
| The start set for snowballing all comes from one community | You find only one cluster of papers that cite each other[^w14-e3] |
| Excluding papers too readily on title and abstract alone | You miss relevant papers; abstracts are often uninformative, so when unsure, read the full text[^kc-e11] |
| Using the rank of the venue as a stand-in for quality assessment | Venue rank is not the quality of an individual study[^sig-e16] |
| Listing papers one by one: "A found X, B found Y" | There is no synthesis, and readers get no conclusion[^sig-e16] |
| Forcing a systematic review in an area with very few high-quality studies | It can't reach reliable conclusions; a mapping study first would be better[^sig-e16][^kc-e3] |
| Using a survey paper to support "X is better than Y" | Hand-picked papers are biased and can't support an empirical conclusion[^rb-e2] |
| A mapping study that offers only classification and counts | Limited value; better to take one more step toward synthesis[^rb-e5] |

---

## 7. Further reading

- **The complete guide to systematic reviews**: Kitchenham & Charters 2007, including quality assessment checklists and many examples.
- **Mapping studies**: Petersen et al. 2008; we have not yet read the full text of the updated version, Petersen et al. 2015, and will add it later `[To be confirmed]`.
- **The full range of review types**: Ralph & Baltes 2022 survey many kinds of literature review; besides the ones on this page, they discuss meta-analysis, meta-synthesis, case surveys, rapid reviews, and more[^rb-e5].
- **Reporting guideline**: the full PRISMA 2020 checklist and flow diagram template.

For links to each source, see the [source list](../../sources/README.md).

[^csur-e1]: ACM Computing Surveys author guidelines, Long Survey Paper. [Evidence](../../sources/notes/acm2026csurguidelines.md#e1)
[^csur-e2]: ACM Computing Surveys author guidelines, Tutorial Paper. [Evidence](../../sources/notes/acm2026csurguidelines.md#e2)
[^kc-e1]: Kitchenham & Charters 2007, §1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e1)
[^kc-e2]: Kitchenham & Charters 2007, §2. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e2)
[^kc-e3]: Kitchenham & Charters 2007, §2.5.1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e3)
[^kc-e4]: Kitchenham & Charters 2007, §4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e4)
[^kc-e5]: Kitchenham & Charters 2007, §5.1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e5)
[^kc-e6]: Kitchenham & Charters 2007, §5.3.1. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e6)
[^kc-e7]: Kitchenham & Charters 2007, §5.4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e7)
[^kc-e8]: Kitchenham & Charters 2007, §5.4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e8)
[^kc-e9]: Kitchenham & Charters 2007, §5.5. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e9)
[^kc-e10]: Kitchenham & Charters 2007, §6.1.2. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e10)
[^kc-e11]: Kitchenham & Charters 2007, §6.2.2. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e11)
[^kc-e12]: Kitchenham & Charters 2007, §6.2.3. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e12)
[^kc-e13]: Kitchenham & Charters 2007, §6.3. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e13)
[^kc-e14]: Kitchenham & Charters 2007, §6.3.4. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e14)
[^kc-e15]: Kitchenham & Charters 2007, §6.4.3. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e15)
[^kc-e16]: Kitchenham & Charters 2007, §6.5. [Evidence](../../sources/notes/kitchenham2007guidelines.md#e16)
[^pe-e1]: Petersen et al. 2008, §2. [Evidence](../../sources/notes/petersen2008systematic.md#e1)
[^pe-e2]: Petersen et al. 2008, §2.4. [Evidence](../../sources/notes/petersen2008systematic.md#e2)
[^pe-e3]: Petersen et al. 2008, §3.2. [Evidence](../../sources/notes/petersen2008systematic.md#e3)
[^pe-e4]: Petersen et al. 2008, §3.2. [Evidence](../../sources/notes/petersen2008systematic.md#e4)
[^pe-e5]: Petersen et al. 2008, §3.2. [Evidence](../../sources/notes/petersen2008systematic.md#e5)
[^pe-e6]: Petersen et al. 2008, §4. [Evidence](../../sources/notes/petersen2008systematic.md#e6)
[^pe-e7]: Petersen et al. 2008, Abstract and §1. [Evidence](../../sources/notes/petersen2008systematic.md#e7)
[^pe-e8]: Petersen et al. 2008, §2.5. [Evidence](../../sources/notes/petersen2008systematic.md#e8)
[^rb-e1]: Ralph & Baltes 2022, §2.1. [Evidence](../../sources/notes/ralph2022paving.md#e1)
[^rb-e2]: Ralph & Baltes 2022, §2.1. [Evidence](../../sources/notes/ralph2022paving.md#e2)
[^rb-e3]: Ralph & Baltes 2022, §2.2.5. [Evidence](../../sources/notes/ralph2022paving.md#e3)
[^rb-e4]: Ralph & Baltes 2022, §2.2.5. [Evidence](../../sources/notes/ralph2022paving.md#e4)
[^rb-e5]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e5)
[^w14-e1]: Wohlin 2014, §1. [Evidence](../../sources/notes/wohlin2014guidelines.md#e1)
[^w14-e2]: Wohlin 2014, §3.1. [Evidence](../../sources/notes/wohlin2014guidelines.md#e2)
[^w14-e3]: Wohlin 2014, §3.1. [Evidence](../../sources/notes/wohlin2014guidelines.md#e3)
[^w14-e4]: Wohlin 2014, §3.2. [Evidence](../../sources/notes/wohlin2014guidelines.md#e4)
[^w14-e5]: Wohlin 2014, §3.2.1. [Evidence](../../sources/notes/wohlin2014guidelines.md#e5)
[^w14-e6]: Wohlin 2014, §3.3. [Evidence](../../sources/notes/wohlin2014guidelines.md#e6)
[^w22-e1]: Wohlin et al. 2022, Abstract. [Evidence](../../sources/notes/wohlin2022successful.md#e1)
[^pr-e1]: PRISMA 2020 (Page et al. 2021). [Evidence](../../sources/notes/page2021prisma.md#e1)
[^pr-e2]: PRISMA 2020 (Page et al. 2021). [Evidence](../../sources/notes/page2021prisma.md#e2)
[^pr-e3]: PRISMA 2020, Item 7. [Evidence](../../sources/notes/page2021prisma.md#e3)
[^pr-e4]: PRISMA 2020, Item 16a. [Evidence](../../sources/notes/page2021prisma.md#e4)
[^pr-e5]: PRISMA 2020, changes from the 2009 version. [Evidence](../../sources/notes/page2021prisma.md#e5)
[^sig-e3]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e3)
[^sig-e4]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e4)
[^sig-e5]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e5)
[^sig-e6]: SIGSOFT Systematic Reviews standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e6)
[^sig-e7]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e7)
[^sig-e8]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e8)
[^sig-e9]: SIGSOFT Systematic Reviews standard, Desirable Attributes and footnote 3. [Evidence](../../sources/notes/ralph2020empirical.md#e9)
[^sig-e10]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e10)
[^sig-e11]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e11)
[^sig-e12]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e12)
[^sig-e13]: SIGSOFT Systematic Reviews standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e13)
[^sig-e14]: ACM SIGSOFT Empirical Standards, Systematic Reviews standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e14)
[^sig-e15]: ACM SIGSOFT Empirical Standards, Systematic Reviews standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e15)
[^sig-e16]: SIGSOFT Systematic Reviews standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e16)
[^sig-e17]: ACM SIGSOFT Empirical Standards, Systematic Reviews standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e17)
[^sig-e18]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e18)
