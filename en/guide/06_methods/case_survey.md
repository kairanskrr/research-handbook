# Case survey: coding published case studies into a dataset

This page covers the **case survey** (also called case meta-analysis): you collect a large number of case studies that other researchers have already published, use one coding scheme to turn their qualitative descriptions into data, and then analyze that data quantitatively.

If you want to study one or a few cases in depth yourself, see [Case study](case_study.md). If you want to review experiments or other kinds of studies, see [Review studies](review_study.md).

**Scope**: the standards and examples on this page come mainly from software engineering. The checklist follows the ACM SIGSOFT Empirical Standards (the empirical research standards of the Association for Computing Machinery's Special Interest Group on Software Engineering; "the SIGSOFT standard" below), and the discussion of misuse comes from a survey of software engineering papers. The classic methodological paper on this method appeared in a management journal (see Further reading), and the method is used more in management and information systems (see Section 1). If you work in another field, read your own field's methods literature and standards first.

**Strategies it usually serves**: [Synthesis](../05_research-strategies/synthesize.md).

**After reading this page, you should be able to:**

- decide whether a case survey suits your question, and how it differs from a single case study and from a systematic review;
- carry out a case survey step by step: find cases, design a coding scheme, code with several people, analyze;
- recognize the most common ways this method is misused;
- check your own study against the checklist at the end.

---

## 1. What this kind of research is and when to use it

The SIGSOFT standard defines it as a study that systematically converts the qualitative descriptions in published case studies into quantitative data and analyzes them, with the aim of reaching generalizable conclusions about a complex phenomenon[^ralph2020empirical-e291]. It tries to combine the strengths of two methods: the generalizability of survey research and the depth of case study research[^melegati2020case-e1].

"Case study" is meant here in the broadest sense: a scholarly account of some events. Whether experience reports and grey literature (material not published through formal publishing channels) should be included depends on the purpose of the study[^ralph2022paving-e6]. The approach is close to meta-analysis (statistically pooling the results of many studies): you usually start from hypotheses and a coding scheme fixed in advance, and end up with a dataset on which you can test hypotheses[^ralph2022paving-e7]. Like meta-analysis, it synthesizes the results of many studies to answer specific empirical questions about the real world, and these are often causal questions[^ralph2022paving-e11], for example "Are projects more likely to succeed when the team holds retrospectives?"

**The question is causal, but the evidence is correlational. Keep the two apart.** Researchers usually care whether A causes B, but the data in a case survey can only show whether B is more common in cases that have A, which is a correlation. The cases were not produced under controlled conditions, so other factors cannot be ruled out (the sources don't say this directly; it is our inference). The data are also sparse, so usually only simple bivariate correlations are possible[^ralph2022paving-e8]. A causal question can therefore be the starting point and the hypothesis, but your conclusion should say "A is associated with B", not "A causes B". Presenting correlation as causation is an antipattern the standard names explicitly[^ralph2020empirical-e304].

**How it differs from related types of study** (cells without a footnote are our own summary):

| | Case study | Multiple-case study | Systematic review | Case survey |
|---|---|---|---|---|
| Data source | Primary data you collect yourself | Primary data you collect yourself | Published studies of all kinds | Published case studies |
| Number of cases | One | A few, limited by effort[^melegati2020case-e10] | Not applicable | The more the better; statistical tests need many cases[^melegati2020case-e4] |
| Analysis | Mainly qualitative | Mainly qualitative, with cross-case comparison possible | Descriptive synthesis or meta-analysis | Quantitative statistics after coding[^melegati2020case-e3] |
| Typical question | "What happened here, and why?" | "How are these few cases alike and different?" | "What does the existing evidence say about problem X?" | "Across many cases, is factor A associated with outcome B?" |

A few notes:

- **Versus a multiple-case study**: a multiple-case study can also do cross-case analysis, but it takes a lot of effort, so the number of cases usually falls short of what statistical analysis needs. Also, all its cases are done by the same person with the same purpose, perspective, method, and theoretical framework[^melegati2020case-e10]. A case survey uses cases written by different authors for different purposes.
- **Versus a systematic review**: both aim to synthesize evidence, but a systematic review can include studies using any method, while a case survey analyzes only studies that describe cases, and analyzes them only through coded quantitative data[^melegati2020case-e11]. If you are reviewing experiments or other studies, use the systematic review standards. Synthesizing several qualitative studies into themes (as in meta-ethnography or narrative synthesis) is not a case survey either[^ralph2020empirical-e292].
- **It is not "surveying many instances yourself"**: collecting primary data from many instances through your own questionnaires or interviews is not a case survey[^ralph2020empirical-e292]. Follow the requirements for questionnaire surveys or qualitative surveys instead.

**When to use it:** when a topic has accumulated a **large** number of published case studies and you want to test whether there is a pattern linking some factor to some outcome. Because the coded data are sparse, a case survey needs many cases to work[^ralph2022paving-e10].

Case surveys are widely used in management and information systems but still rare in software engineering. Ralph & Baltes argue that because software engineering has so many case studies, the method has a lot of potential there[^ralph2022paving-e9]. We think that in other areas of computer science, published incident analyses in systems and security could in principle be coded as "cases" too, but whether such material counts as a scholarly account, and whether it contains enough information, has to be judged one report at a time.

**A common misuse**: Melegati & Wang examined 12 software engineering papers that claimed to be case surveys and found that most did not follow the method as originally defined[^melegati2020case-e2]. The most common pattern was treating each questionnaire answer or each blog post as a "case"; the rest were multiple-case studies with a larger number of cases[^melegati2020case-e12]. A questionnaire answer or a blog post usually comes from a single person: it lacks depth and breadth, and there are no multiple sources to triangulate, so it does not count as a case[^melegati2020case-e13].

---

## 2. How to do it

Larsson 1993 summarizes the method in four steps: select a set of existing case studies; design a coding scheme; have several coders code the cases; analyze statistically[^melegati2020case-e3]. The steps below follow that order.

### Step 1: State your research question and hypotheses

A case survey can test hypotheses or explore, but the choice of cases needs a theoretical basis[^melegati2020case-e4]. Usually you write your hypotheses before you start and derive from them the variables you need to code[^ralph2022paving-e7].

**Where people go wrong:** reading a pile of cases first and then seeing which correlations turn up. "Findings" produced this way are likely to be chance; fixing your hypotheses first constrains you in advance. For the difference between exploration and confirmation, see [From research questions to an evidence plan: be clear whether you are testing or exploring](../02_do-the-project/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring).

### Step 2: Find and select cases

**Searching**: describe the search process step by step so that it can be reproduced. The cases do not have to come from peer-reviewed venues[^ralph2020empirical-e293]. Combine several search strategies to reduce sampling bias and publication bias[^ralph2020empirical-e294]. The specific techniques (keyword search, snowballing, checking preprints and theses, and so on) are the same as for a systematic review; see [Review studies](review_study.md#2-how-to-do-a-systematic-review).

**Base your inclusion criteria on how much information a case reports, not on where it was published**[^melegati2020case-e4]. The standard gives the example of requiring that a case report at least two of the variables in the coding scheme[^ralph2020empirical-e293]. When Larsson studied corporate mergers and acquisitions, he required each case to contain at least two pages describing business and personnel issues[^melegati2020case-e5].

**Where people go wrong:**

- including every case found without checking whether it has enough information[^ralph2020empirical-e304];
- including material that is not a case study at all, such as questionnaires or reports of only a sentence or two[^ralph2020empirical-e304].

### Step 3: Design the coding scheme

The coding scheme specifies how to convert qualitative descriptions into quantitative variables[^ralph2020empirical-e295]. You can think of it as a questionnaire that the researcher fills in for each case. The variables are often simple yes/no items, such as "Did the team hold retrospectives?"[^ralph2022paving-e8]

When designing it, you trade off between two ends: a simple scheme is less work and gives more reliable coding; a complex one captures richer information[^melegati2020case-e6][^ralph2020empirical-e295].

Some requirements:

- Describe the coding scheme in detail in the paper or put it in the supplementary materials[^ralph2020empirical-e295]; ideally, explain why you designed it that way[^ralph2020empirical-e298].
- **Decide in advance how to handle missing values**, and state it in the paper[^ralph2020empirical-e296]. Many cases will not mention every variable you care about. Whether "not mentioned" is coded as "no", coded as "missing", or leads to excluding the case directly affects the results.
- Pilot the scheme on a few cases first, fix vague items and decision rules, and only then start the real coding.

### Step 4: Code independently with several people and check agreement

- Use at least two coders, preferably three[^melegati2020case-e7]. Each codes independently, and you analyze inter-rater reliability (how consistently different coders judge the same case)[^ralph2020empirical-e299]. For how to choose an agreement statistic and common mistakes, see the computer science practice page [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md#step-6-label-data-manually-and-check-agreement).
- Agreement is a key indicator of coding quality, but don't obsess over it[^melegati2020case-e7].
- Explain how disagreements were resolved: discussion until consensus, voting, a tie-breaker, or consulting the original authors[^ralph2020empirical-e299].
- **You can ask the original authors for help.** They had contact with the primary data, and some information may have been left out of the paper for lack of space[^melegati2020case-e8]. Contacting the original authors to get information or check your coding is a desirable attribute[^ralph2020empirical-e300]; having them take part in the coding directly is an extraordinary one[^ralph2020empirical-e303].

### Step 5: Analyze

- **Analyze quantitatively, and actually synthesize.** Analyzing cases with qualitative techniques, or describing each case on its own without synthesizing, are both antipatterns[^ralph2020empirical-e304]. Base your conclusions on the coded variables[^ralph2020empirical-e296].
- **Match the method to the data.** Coded datasets are often too sparse for regression modeling; researchers usually test hypotheses with simple bivariate correlations[^ralph2022paving-e8].
- **Write conclusions as correlations, not causation**[^ralph2020empirical-e304]. Even when the research question itself is causal, this kind of data supports only correlation; for the reasons, see [What this kind of research is and when to use it](#1-what-this-kind-of-research-is-and-when-to-use-it) above.
- **Check whether characteristics of the original studies influenced the coding**, such as study design, publication venue, or year of publication[^melegati2020case-e9][^ralph2020empirical-e303].
- Assess the quality of the original studies with a scheme fixed in advance, and include quality in the analysis as a moderator (a variable that may change how strongly the factor and the outcome are related) to see whether it changes the conclusions[^ralph2020empirical-e301]. Don't use the prestige of the publication venue as a substitute for assessing quality[^ralph2020empirical-e304].

### Step 6: Report

Publish the protocol, search terms, screening results, coding scheme, coding examples, decision rules, the full dataset, and analysis scripts[^ralph2020empirical-e298]. Summarize the results in tables and figures, with a PRISMA flow diagram (the screening flow chart commonly used in systematic reviews; see [Review studies](review_study.md)). Keep results that have evidence behind them separate from your interpretation and speculation[^ralph2020empirical-e302].

---

## 3. Limitations: your data are only what someone else wrote down

Every data point in a case survey comes from a report someone else wrote for a different purpose. This brings some unavoidable limitations, which you must state in the paper[^ralph2020empirical-e18]:

- **Not reported does not mean it didn't happen.** Some information may have been left out of a report for lack of space[^melegati2020case-e8]. That is why the handling of missing values has to be decided in advance and stated clearly[^ralph2020empirical-e296].
- **The cases do not represent the population.** The cases that get written up as papers tend to be the ones the authors had access to and thought worth writing about. You must discuss how the included cases might differ from the population you want to generalize to[^ralph2020empirical-e297].
- **The original studies vary in quality.** So assess quality and test whether it affects your conclusions[^ralph2020empirical-e301].

**Common reviewer criticisms that are not valid**[^ralph2020empirical-e305]:

- "The primary studies were not published in peer-reviewed venues"
- "The primary studies use different designs"
- "The cases are not a random sample of the phenomenon"

---

## 4. Checklist

This follows the ACM SIGSOFT case survey standard, which was written for software engineering.

**Essential**

- [ ] Describe the search process step by step and reproducibly[^ralph2020empirical-e293]
- [ ] Give clear inclusion and exclusion criteria for cases[^ralph2020empirical-e293]
- [ ] Combine several search strategies to reduce sampling bias and publication bias[^ralph2020empirical-e294]
- [ ] Define the coding scheme, and describe it in the paper or put it in supplementary materials[^ralph2020empirical-e295]
- [ ] State how missing values were handled[^ralph2020empirical-e296]
- [ ] Base conclusions on the coded quantitative variables[^ralph2020empirical-e296]
- [ ] Discuss how the included cases might differ from the target population[^ralph2020empirical-e297]

**Desirable**

- [ ] Publish the protocol, search results, coding scheme, examples, data, and scripts; explain the rationale for the coding scheme[^ralph2020empirical-e298]
- [ ] Have two or more people code independently, analyze agreement, and explain how disagreements were resolved[^ralph2020empirical-e299]
- [ ] Contact the original authors to get information or check the coding[^ralph2020empirical-e300]
- [ ] Assess the quality of the original studies and include it as a variable in the analysis[^ralph2020empirical-e301]
- [ ] Summarize results in tables and figures, with a PRISMA flow diagram; separate evidence from speculation[^ralph2020empirical-e302]

**Extraordinary**[^ralph2020empirical-e303]

- [ ] Use theory to guide the selection and sampling of cases
- [ ] Add data from other sources for the selected cases
- [ ] Have the original authors take part in the coding or confirm interpretations
- [ ] Analyze whether study design, publication venue, year, and so on influenced the coding

---

## 5. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Treating questionnaire answers or blog posts as "cases" | The information is too shallow and comes from a single source; it is not a case study[^melegati2020case-e13][^ralph2020empirical-e304] |
| Calling a few cases you studied yourself a case survey | That is a multiple-case study, and it has too few cases to support statistical analysis[^melegati2020case-e10][^melegati2020case-e12] |
| Including every case found without checking whether it has enough information | The standard lists this as an antipattern[^ralph2020empirical-e304]; many variables can only be coded as missing |
| Going back to qualitative analysis after coding, or presenting the cases one by one | This defeats the purpose of the method: there is no quantitative synthesis[^ralph2020empirical-e304] |
| Having only one person code | There is no way to judge how reliable the coding is[^ralph2020empirical-e299] |
| Using the prestige of the venue instead of a quality assessment | The prestige of a venue is not the quality of an individual study[^ralph2020empirical-e304] |
| Writing correlation as causation | The standard lists this as an antipattern[^ralph2020empirical-e304]; the question can be causal, but this kind of data supports only correlation |
| Calling a study a case survey without following the method's requirements | Departing from the method without reflecting on the consequences casts doubt on the validity of the conclusions[^melegati2020case-e14] |

---

## 6. Further reading

- **Start here**: Melegati & Wang 2020. Lays out the classic definition and steps of the case survey and analyzes how it has been misused in software engineering.
- **Where it sits among kinds of review**: Ralph & Baltes 2022, §2.2.3, briefly explains how case surveys differ from meta-analysis and meta-synthesis.
- **A dedicated guide for software engineering**: Petersen 2020, *Guidelines for Case Survey Research in Software Engineering* (a chapter of the Springer book *Contemporary Empirical Methods in Software Engineering*). We could not find a legally accessible full text `[To be confirmed]`.
- **The classic methodological paper**: Larsson 1993 (*Academy of Management Journal*). Our description of it is taken secondhand from Melegati & Wang; we have not read the original `[To be confirmed]`.
- **Source of the checklist**: the ACM SIGSOFT case survey standard, which includes exemplar papers from management and information systems.

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e291]: SIGSOFT Case Survey standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e291)
[^ralph2020empirical-e292]: SIGSOFT Case Survey standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e292)
[^ralph2020empirical-e293]: SIGSOFT Case Survey standard, Essential Attributes and footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e293)
[^ralph2020empirical-e294]: SIGSOFT Case Survey standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e294)
[^ralph2020empirical-e295]: SIGSOFT Case Survey standard, Essential Attributes and footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e295)
[^ralph2020empirical-e296]: SIGSOFT Case Survey standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e296)
[^ralph2020empirical-e297]: SIGSOFT Case Survey standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e297)
[^ralph2020empirical-e298]: SIGSOFT Case Survey standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e298)
[^ralph2020empirical-e299]: SIGSOFT Case Survey standard, Desirable Attributes and footnote 4. [Evidence](../../sources/notes/ralph2020empirical.md#e299)
[^ralph2020empirical-e300]: SIGSOFT Case Survey standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e300)
[^ralph2020empirical-e301]: SIGSOFT Case Survey standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e301)
[^ralph2020empirical-e302]: SIGSOFT Case Survey standard, Desirable Attributes and footnote 5. [Evidence](../../sources/notes/ralph2020empirical.md#e302)
[^ralph2020empirical-e303]: SIGSOFT Case Survey standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e303)
[^ralph2020empirical-e304]: SIGSOFT Case Survey standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e304)
[^ralph2020empirical-e305]: SIGSOFT Case Survey standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e305)
[^ralph2020empirical-e18]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e18)
[^ralph2022paving-e6]: Ralph & Baltes 2022, §2.2.3. [Evidence](../../sources/notes/ralph2022paving.md#e6)
[^ralph2022paving-e7]: Ralph & Baltes 2022, §2.2.3. [Evidence](../../sources/notes/ralph2022paving.md#e7)
[^ralph2022paving-e8]: Ralph & Baltes 2022, §2.2.3. [Evidence](../../sources/notes/ralph2022paving.md#e8)
[^ralph2022paving-e9]: Ralph & Baltes 2022, §2.2.3. [Evidence](../../sources/notes/ralph2022paving.md#e9)
[^ralph2022paving-e10]: Ralph & Baltes 2022, §3. [Evidence](../../sources/notes/ralph2022paving.md#e10)
[^ralph2022paving-e11]: Ralph & Baltes 2022, §3 and §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e11)
[^melegati2020case-e1]: Melegati & Wang 2020, Abstract. [Evidence](../../sources/notes/melegati2020case.md#e1)
[^melegati2020case-e2]: Melegati & Wang 2020, Abstract. [Evidence](../../sources/notes/melegati2020case.md#e2)
[^melegati2020case-e3]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e3)
[^melegati2020case-e4]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e4)
[^melegati2020case-e5]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e5)
[^melegati2020case-e6]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e6)
[^melegati2020case-e7]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e7)
[^melegati2020case-e8]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e8)
[^melegati2020case-e9]: Melegati & Wang 2020, §2. [Evidence](../../sources/notes/melegati2020case.md#e9)
[^melegati2020case-e10]: Melegati & Wang 2020, §2.1. [Evidence](../../sources/notes/melegati2020case.md#e10)
[^melegati2020case-e11]: Melegati & Wang 2020, §2.1. [Evidence](../../sources/notes/melegati2020case.md#e11)
[^melegati2020case-e12]: Melegati & Wang 2020, §6. [Evidence](../../sources/notes/melegati2020case.md#e12)
[^melegati2020case-e13]: Melegati & Wang 2020, §5. [Evidence](../../sources/notes/melegati2020case.md#e13)
[^melegati2020case-e14]: Melegati & Wang 2020, §5. [Evidence](../../sources/notes/melegati2020case.md#e14)
