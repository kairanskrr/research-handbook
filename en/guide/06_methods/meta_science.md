# Methodology research and meta-science: research on "how to do research"

This page is about **research whose object is research methods themselves**: papers that analyze a methodological issue or give recommendations on how to do research. Examples are a guideline for statistical tests, a paper surveying "how well do papers in this area evaluate their work?", or an essay criticizing a research habit.

If what you want to know is how to make your own experiment rigorous, that is something every study has to do; see [Validity and limitations: think them through at the design stage](../02_do-the-project/04_validity-and-limits.md). If you want to review the research on a technical topic, see [Review studies](review_study.md).

**Scope**: the standards and examples on this page all come from computer science. The checklist is based on the empirical standards written for software engineering by ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering), and the examples come from software engineering, systems security, fuzz testing, and machine learning. Other fields have methodology research too (see the end of Section 1); before you start, look at similar papers and journal requirements in your own field.

**Strategies it usually serves**: [Synthesis](../05_research-strategies/synthesize.md) (critical reviews), [Measurement](../05_research-strategies/measure.md) (systematically surveying how well a field does its measurement).

**After reading this page, you should be able to:**

- recognize the common kinds of methodology research and the kind of evidence each needs;
- choose the right evidence for your own methodology paper: a systematic sample of papers, a demonstration experiment you run yourself, or argument;
- criticize other researchers' work fairly, without hurting people;
- check your own paper against the checklist at the end.

---

## 1. What this kind of study is, and when to use it

The ACM SIGSOFT empirical standards define it as a paper that analyzes an issue of research methodology or makes recommendations for conducting research[^ralph2020empirical-e306]. It may or may not include empirical data; it may deal with philosophical or practical issues; and if it is also an empirical study (for example, a case study that then leads to methodological recommendations), it must also meet the standard for that kind of study[^ralph2020empirical-e307].

This kind of research belongs to **meta-science**: a scientific community's own discussion of how it does research[^ralph2022paving-e14].

**Common kinds** (our own grouping, based on the sources below):

| Kind | What it does | Examples |
|---|---|---|
| Methodological guideline | Explains systematically how a research method should be carried out | The exemplars listed in the SIGSOFT standard include Kitchenham & Charters's guidelines for systematic literature reviews and Runeson & Höst's guidelines for case study research[^ralph2020empirical-e315] |
| Critical review | Analyzes a sample of papers to support an argument or critique, often about methodological issues[^ralph2022paving-e12]; it goes beyond description and offers specific critiques[^ralph2022paving-e16] | Stol et al. criticized "method slurring" in software engineering: claiming to have used a research method that was not actually used[^ralph2022paving-e13] |
| Survey of research practice | Systematically examines what a set of published papers did and counts how widespread a problem is, often paired with demonstration experiments | van der Kouwe et al. surveyed the benchmarking in 50 systems security papers[^vanderkouwe2019sok-e26]; Klees et al. surveyed the evaluations in 32 fuzzing papers[^klees2018evaluating-e2] |
| Position and discussion paper | Points out a research habit and starts a discussion | Lipton & Steinhardt wrote for a debate-style workshop, criticizing several trends in how machine learning papers are written[^lipton2019troubling-e16]; Ralph & Baltes also state that their own paper on a taxonomy of reviews is meta-science, not an empirical paper[^ralph2022paving-e21] |

**How it differs from a review study**: a mapping study (close to a scoping review; see [Review studies](review_study.md)) is about an empirical topic (for example, "cognitive biases in software engineering"), while meta-science is about a methodological topic (for example, "construct validity", that is, whether what you measure really represents the concept you want to study)[^ralph2022paving-e17]. So a mapping study was never designed for methodological critique. Nor is a critical review meant to summarize the evidence for a theory; its purpose is to assess research practice[^ralph2022paving-e14].

**When it is worth writing one**: when you keep seeing the same methodological problem as you read papers or review submissions, and you can explain why it matters and how to fix it. In computer science, such papers appear in every area: software engineering (guidelines for research methods), systems and security (surveys of evaluation flaws), and machine learning (critiques of evaluation and writing habits). Other fields have them too, for example the papers in psychology on the misuse of statistical tests and on the replicability of research.

---

## 2. How to do it

### Step 1: Pick a question that is useful to others, and give clear recommendations

The SIGSOFT standard has only three essential attributes for this kind of paper: it presents information that is useful for other researchers; it makes recommendations for future research; and it supports those recommendations with clear, valid arguments[^ralph2020empirical-e308].

**Where people go wrong:** discussing an issue without reaching clear conclusions or giving actionable guidelines[^ralph2020empirical-e311]. Readers finish knowing only that "there's a problem here", not what to do about it.

**When you give recommendations, say how certain they are.** Lipton & Steinhardt's positive example is a guide to training models: it does not present its advice as authoritative, but says the advice should be open to challenge and is only a good starting point[^lipton2019troubling-e20].

**Desirable** (in the SIGSOFT standard): produce something people can use directly, such as a checklist, template, test, tool, or set of criteria[^ralph2020empirical-e309]. Klees et al. end with concrete recommendations, for example running multiple trials and comparing them with statistical tests, and running for at least 24 hours or justifying a shorter time[^klees2018evaluating-e24].

### Step 2: Choose the right evidence

A methodology paper's evidence comes mainly from three sources, which you can combine.

**1. A systematic sample of papers: shows how widespread the problem is.**

- Say how you chose the papers. van der Kouwe et al. took **all** defense papers with benchmarking results published in 2010 and 2015 at four top security conferences, and explained that they chose these four because they effectively set the field's evaluation conventions[^vanderkouwe2019sok-e27].
- You don't need every paper. For many critical reviews, including all relevant studies is neither possible nor necessary; because a critical review does not evaluate causal claims, a random sample from several top journals and conferences is enough[^ralph2022paving-e15]. Reviewers also should not apply systematic-review standards such as "you must find everything" or "you must exclude low-quality studies"[^ralph2022paving-e20].
- Without systematic sampling, a handful of examples can show that a problem exists, but not how widespread it is in the literature[^vanderkouwe2019sok-e33].

**2. A demonstration experiment you run yourself: shows the consequences of the problem.**

If you only say "many papers don't do X", readers may shrug. Klees et al. ran more than 50,000 CPU hours of experiments to show that experiments departing from recommended practice can easily reach wrong conclusions[^klees2018evaluating-e20]. You need a reason for what you choose to demonstrate on: the tool they chose was a recent advance with public code, which let them rerun the original experiments and vary parameters the original authors had not varied[^klees2018evaluating-e21]. And the aim was not to replicate that paper, but to use it as a case for testing evaluation practice[^klees2018evaluating-e22]. The SIGSOFT standard lists using a quantitative simulation to illustrate a methodological issue as an extraordinary attribute[^ralph2020empirical-e310].

**3. Argument: many methodological claims cannot be tested empirically in the first place.**

The SIGSOFT standard regards "Guidelines are not based on empirical evidence" as an invalid criticism: meta-scientific claims usually cannot be tested empirically, and reviewers should evaluate the guidelines' face validity, comprehensiveness, and usefulness[^ralph2020empirical-e313]. That doesn't mean anything goes: reviewers should scrutinize the arguments more pedantically[^ralph2020empirical-e314], and you must avoid logical fallacies such as the straw man (distorting the other side's view and then attacking it) and the appeal to popularity[^ralph2020empirical-e311].

> **Where sources disagree: does a methodology paper need an empirical study?**
> - The SIGSOFT standard says no: it lists an empirical study that motivates the analysis ("includes an empirical study (e.g. a systematic literature review) that motivates the analysis of guidance") as an extraordinary attribute, not an essential one[^ralph2020empirical-e310][^ralph2020empirical-e313]. Ralph & Baltes argue that the reviewing habit of insisting every paper report an empirical study has held back meta-science research[^ralph2022paving-e18].
> - van der Kouwe et al., on the other hand, point out that papers which illustrate a problem only with examples and their own tests cannot show how much the problem affects the literature[^vanderkouwe2019sok-e33].
>
> In practice you can read it this way: if your claim is "this problem is widespread", you need data from a systematic sample; if your claim is "this is how it should be done", argument and demonstration can be the main evidence.

### Step 3: When you look for flaws in papers, be as rigorous as in any study

Surveying what a set of papers did is, in essence, coding those papers, and it carries the same requirements as any other coding study (for how to check agreement, see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md#step-6-label-data-manually-and-check-agreement)):

- **Two people judge independently, then discuss disagreements.** In van der Kouwe et al., two people independently judged each paper for each flaw; the 8 papers (16%) where they disagreed were settled by discussion[^vanderkouwe2019sok-e28].
- **Keep a category for "can't tell".** Their categories were "correct", "flawed", "underspecified", and "not applicable"[^vanderkouwe2019sok-e28]. If a paper doesn't say clearly what it did, you can't simply count it as "done wrong".
- **State the limits on your information sources.** They relied only on the papers themselves and did not contact the authors, which put them under the same constraint as a reviewer[^vanderkouwe2019sok-e29].
- **State the limits of your sample.** Published papers do not necessarily represent all submissions[^vanderkouwe2019sok-e32].
- **When you can only guess at causes, say it is a guess.** About why the flaws arose, they wrote explicitly that they "can only speculate"[^vanderkouwe2019sok-e34].

### Step 4: Criticize fairly: target the work, not the people

Almost every methodology paper has to point out other people's problems, and this is the step that needs the most care.

- **Don't attack specific studies or researchers.** The SIGSOFT standard recommends hypothetical examples, to avoid stirring up animosity[^ralph2020empirical-e312]. Ralph & Baltes argue that when you are illustrating a general problem, there is no need to name the specific papers that got it wrong: the credibility you gain does not outweigh the harm to the research community and to future collaboration; authors should explain their reasons for this choice[^ralph2022paving-e19].
- **Don't allege motives.** van der Kouwe et al. deliberately use the term "flaws" rather than "crimes", and say they believe most of these flaws are unintentional[^vanderkouwe2019sok-e30]. Their data also show that the problem lies not with a few authors but with a lack of attention across the whole field[^vanderkouwe2019sok-e35].
- **Include yourself.** Lipton & Steinhardt state that their criticism applies to themselves too, and give negative examples from their own papers[^lipton2019troubling-e17][^lipton2019troubling-e12].
- **When you need real examples, protect the most vulnerable.** They preferred work by well-known researchers and institutions and avoided naming junior students, because being named could harm a student, who also has no equal chance to respond[^lipton2019troubling-e18]. Keep examples short and specific, and also give positive examples of work done well[^lipton2019troubling-e19].
- **Take counterarguments seriously.** Lipton & Steinhardt devote a section to the arguments against their own recommendations, acknowledge that these have merit, and present their recommendations as rules of thumb rather than iron laws[^lipton2019troubling-e21].

> **Where sources disagree: should you name names?**
> - **Anonymous**: van der Kouwe et al. do not disclose which papers have which flaws, believing that naming and shaming is counterproductive; to compensate, their appendix sets out the classification criteria in detail, so others can redo the survey by the same criteria[^vanderkouwe2019sok-e31].
> - **Public**: Klees et al. summarize the evaluation practice of every surveyed paper in a table[^klees2018evaluating-e23] (we checked the original table: it lists the papers one by one), so readers can check directly.
>
> In practice: being public makes checking and replication easier; staying anonymous reduces harm to individuals. When you are pointing out a general problem, you can lean toward anonymity while publishing your classification criteria; either way, comment only on what the papers did, not on the authors.

---

## 3. Checklist

This checklist is based on the ACM SIGSOFT standard for methodology and meta-science papers, which was written for software engineering.

**Essential**[^ralph2020empirical-e308]

- [ ] Presents information that is useful for other researchers
- [ ] Makes clear recommendations for future research
- [ ] Supports the recommendations with clear, valid arguments

**Desirable**[^ralph2020empirical-e309]

- [ ] Synthesizes existing methodological discussion from related disciplines
- [ ] Goes beyond restating existing guidelines and offers insights specific to its own field
- [ ] Places its conclusions in the context of existing theory and research
- [ ] Produces tools people can use directly, such as checklists, templates, or sets of criteria

**Extraordinary**[^ralph2020empirical-e310]

- [ ] Includes an empirical study (such as a systematic review) that motivates the analysis of guidance
- [ ] Uses a quantitative simulation to illustrate a methodological issue

**Common reviewer criticisms that don't hold up**[^ralph2020empirical-e313]

- "Guidelines are not based on empirical evidence"

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Pointing out a problem without giving clear recommendations | Readers don't know what to do[^ralph2020empirical-e311] |
| Conclusions that go beyond the argument, or distorting the other side's view and then attacking it | This is overreaching and a logical fallacy[^ralph2020empirical-e311] |
| Attacking specific papers or researchers by name | It stirs up animosity and harms the research community[^ralph2020empirical-e312][^ralph2022paving-e19] |
| Implying that others cheated on purpose | van der Kouwe et al. believe most flaws are unintentional and just reflect too little attention[^vanderkouwe2019sok-e30] |
| Calling a problem "widespread" on the strength of a few examples | Without systematic sampling you can't judge how widespread it is[^vanderkouwe2019sok-e33] |
| Counting "the paper doesn't say" as "the paper did it wrong" | Use a separate "underspecified" category[^vanderkouwe2019sok-e28] |
| Writing up guesses about causes as conclusions | Label them clearly as speculation[^vanderkouwe2019sok-e34] |
| Merely restating existing methodological guidelines | The standard expects insights specific to your field that go beyond existing guidelines[^ralph2020empirical-e309] |

---

## 5. Further reading

- **How to write a survey of research practice**: van der Kouwe et al. 2019 (systems security) and Klees et al. 2018 (fuzz testing). The first shows systematic sampling, coding by two people, and anonymization; the second shows how to use demonstration experiments to reveal consequences. For their evaluation recommendations themselves, see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md).
- **How to criticize other researchers**: Lipton & Steinhardt 2019, Section 2 (disclaimers) and Section 6.1 (counterarguments).
- **Where critical reviews fit**: Ralph & Baltes 2022, §2.2.4 and §3.1.
- **Source of the checklist**: the ACM SIGSOFT standard for methodology and meta-science papers, which includes several exemplar methodological guidelines.

Links to every source are in the [source list](../../sources/README.md).

[^ralph2020empirical-e306]: SIGSOFT Methodological Guidelines and Meta-Science standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e306)
[^ralph2020empirical-e307]: SIGSOFT Methodological Guidelines and Meta-Science standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e307)
[^ralph2020empirical-e308]: SIGSOFT Methodological Guidelines and Meta-Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e308)
[^ralph2020empirical-e309]: SIGSOFT Methodological Guidelines and Meta-Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e309)
[^ralph2020empirical-e310]: SIGSOFT Methodological Guidelines and Meta-Science standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e310)
[^ralph2020empirical-e311]: SIGSOFT Methodological Guidelines and Meta-Science standard, Antipatterns and footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e311)
[^ralph2020empirical-e312]: SIGSOFT Methodological Guidelines and Meta-Science standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e312)
[^ralph2020empirical-e313]: SIGSOFT Methodological Guidelines and Meta-Science standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e313)
[^ralph2020empirical-e314]: SIGSOFT Methodological Guidelines and Meta-Science standard, Notes. [Evidence](../../sources/notes/ralph2020empirical.md#e314)
[^ralph2020empirical-e315]: SIGSOFT Methodological Guidelines and Meta-Science standard, Exemplars. [Evidence](../../sources/notes/ralph2020empirical.md#e315)
[^ralph2022paving-e12]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e12)
[^ralph2022paving-e13]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e13)
[^ralph2022paving-e14]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e14)
[^ralph2022paving-e15]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e15)
[^ralph2022paving-e16]: Ralph & Baltes 2022, §2.2.4. [Evidence](../../sources/notes/ralph2022paving.md#e16)
[^ralph2022paving-e17]: Ralph & Baltes 2022, §3. [Evidence](../../sources/notes/ralph2022paving.md#e17)
[^ralph2022paving-e18]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e18)
[^ralph2022paving-e19]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e19)
[^ralph2022paving-e20]: Ralph & Baltes 2022, §3.1. [Evidence](../../sources/notes/ralph2022paving.md#e20)
[^ralph2022paving-e21]: Ralph & Baltes 2022, §3.2. [Evidence](../../sources/notes/ralph2022paving.md#e21)
[^lipton2019troubling-e16]: Lipton & Steinhardt 2019, §2. [Evidence](../../sources/notes/lipton2019troubling.md#e16)
[^lipton2019troubling-e17]: Lipton & Steinhardt 2019, §2. [Evidence](../../sources/notes/lipton2019troubling.md#e17)
[^lipton2019troubling-e18]: Lipton & Steinhardt 2019, §2. [Evidence](../../sources/notes/lipton2019troubling.md#e18)
[^lipton2019troubling-e19]: Lipton & Steinhardt 2019, §3. [Evidence](../../sources/notes/lipton2019troubling.md#e19)
[^lipton2019troubling-e12]: Lipton & Steinhardt 2019, §3.1. [Evidence](../../sources/notes/lipton2019troubling.md#e12)
[^lipton2019troubling-e20]: Lipton & Steinhardt 2019, §3.1. [Evidence](../../sources/notes/lipton2019troubling.md#e20)
[^lipton2019troubling-e21]: Lipton & Steinhardt 2019, §6.1. [Evidence](../../sources/notes/lipton2019troubling.md#e21)
[^vanderkouwe2019sok-e26]: van der Kouwe et al. 2019, Abstract. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e26)
[^vanderkouwe2019sok-e27]: van der Kouwe et al. 2019, §I, §III-B. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e27)
[^vanderkouwe2019sok-e28]: van der Kouwe et al. 2019, §III-A. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e28)
[^vanderkouwe2019sok-e29]: van der Kouwe et al. 2019, §III-A. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e29)
[^vanderkouwe2019sok-e30]: van der Kouwe et al. 2019, §I. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e30)
[^vanderkouwe2019sok-e31]: van der Kouwe et al. 2019, §VII and Appendix A. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e31)
[^vanderkouwe2019sok-e32]: van der Kouwe et al. 2019, §VII. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e32)
[^vanderkouwe2019sok-e33]: van der Kouwe et al. 2019, §IX. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e33)
[^vanderkouwe2019sok-e34]: van der Kouwe et al. 2019, §I. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e34)
[^vanderkouwe2019sok-e35]: van der Kouwe et al. 2019, §V. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e35)
[^klees2018evaluating-e2]: Klees et al. 2018, Abstract. [Evidence](../../sources/notes/klees2018evaluating.md#e2)
[^klees2018evaluating-e20]: Klees et al. 2018, §1. [Evidence](../../sources/notes/klees2018evaluating.md#e20)
[^klees2018evaluating-e21]: Klees et al. 2018, §1. [Evidence](../../sources/notes/klees2018evaluating.md#e21)
[^klees2018evaluating-e22]: Klees et al. 2018, §3. [Evidence](../../sources/notes/klees2018evaluating.md#e22)
[^klees2018evaluating-e23]: Klees et al. 2018, Table 1 and §4. [Evidence](../../sources/notes/klees2018evaluating.md#e23)
[^klees2018evaluating-e24]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e24)
