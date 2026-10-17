# Grounded theory: building a theory up from the data

This page covers **grounded theory** research. Instead of starting from a hypothesis, you collect data and analyze it at the same time, let each round of analysis decide whom to talk to or what to look at next, and end up with a theory induced from the data.

Most grounded theory data comes from interviews. For how to design and run the interviews themselves, and for the quality criteria and validation practices that all qualitative research shares, see [Interview studies](interview_study.md). If you only want an in-depth description of one particular organization or project, see [Case studies](case_study.md). This page covers only what is specific to grounded theory: the schools, theoretical sampling, constant comparison, memos, theoretical saturation, and producing a theory.

**Scope**: The standards and examples here come mainly from software engineering. They rest on Stol et al.'s review of, and recommendations for, grounded theory studies in software engineering, and on the grounded theory standard in the Empirical Standards of ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering). Grounded theory itself originated in sociology and is also widely used in nursing, management and other fields; if you are doing grounded theory in another field, start with your field's conventions and the methods books of the school you choose. This handbook does not yet have a field-specific grounded theory page for other fields. For how sociology views this kind of research, start with the [sociology field overview](../07_fields/sociology/README.md#research-methods-common-in-this-field).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md).

**After reading this page, you should be able to:**

- judge whether your question suits grounded theory, and which school to follow;
- move the study forward through the collect–analyze–sample-again cycle, and know when you can stop;
- tell "we produced a theory" apart from "we sorted the data into a few themes";
- avoid the most common problem: borrowing the coding techniques and then claiming to have "used grounded theory".

---

## 1. What this kind of study is, and when to use it

Grounded theory is a method for **inductively generating theory from data**[^stol2016grounded-e2]. Its aim is to generate theory, not to test existing theory; it suits questions of the "what is going on here?" kind[^stol2016grounded-e1]. "Theory" here means a set of concepts and the relationships between them that explains some phenomenon[^stol2016grounded-e17].

**When it fits** (our synthesis of the sources below):

- You care about people and organizations: how developers, teams or users do things, and why. Software engineering pays more and more attention to the social, cultural and human sides of software development, and grounded theory is considered well suited to studying them[^stol2016grounded-e25]. The same reasoning holds in systems, security, machine learning and other areas of computer science whenever what you study is a human practice (for example, how operations teams handle incidents, or how machine learning engineers debug models).
- The area has no ready-made theory you could use, and you first want to understand what is going on.
- You can accept that your research question will change along the way: the SIGSOFT Empirical Standards define grounded theory as research that explores a broad area **without a specific research question fixed in advance**[^ralph2020empirical-e316].

**When it doesn't fit**:

- You already have a clear hypothesis to test, such as "introducing pair programming reduces defects". Grounded theory does not test theory[^stol2016grounded-e1]; use an experiment or another confirmatory design.
- You plan to finish all the interviews before analyzing, or you don't plan to let the analysis decide whom to approach next. For qualitative studies like that, the SIGSOFT standards suggest following the Case Study Standard or the Qualitative Survey Standard instead (in this handbook, see [Case Study](case_study.md) and [Interview studies](interview_study.md))[^ralph2020empirical-e316]. Grounded theory is not the only legitimate way to analyze qualitative data[^stol2016grounded-e22], and dressing an interview study up as grounded theory does not make it better.

### Choose a school first, and stay consistent

There are at least three major schools of grounded theory[^stol2016grounded-e3], and they differ most on three things[^stol2016grounded-e4][^stol2016grounded-e5][^stol2016grounded-e6][^stol2016grounded-e8][^stol2016grounded-e9]:

| | Classic grounded theory (Glaser) | Straussian grounded theory (Strauss & Corbin) | Constructivist grounded theory (Charmaz) |
|---|---|---|---|
| Character | Everything should "emerge" from the data | Prescribes a series of detailed procedures | Emphasizes understanding; accepts that interpretation depends on the researcher's perspective |
| Research question | Start only from an "area of interest"; fixing a question in advance counts as "forcing" | You may set a broad, open question in advance | Start from an "initial research question" that evolves during the study |
| Literature | Do a full review only after the theory has emerged | You may consult it throughout | Accepts the reasons for delaying the review but also that this is unrealistic; tailor it to the study's purpose |
| Coding | Open, selective, theoretical coding | Open, axial, selective coding | Initial, focused, theoretical coding |

Watch out: the same term can mean different things in different schools. "Selective coding", for example, means keeping only the codes related to the core variable in the classic version, and choosing one central category that all the major categories connect to in the Straussian version[^stol2016grounded-e9].

**Pick one, and keep to it in your design, analysis and writing.** Stol et al. reviewed 52 software engineering journal papers that claimed to use grounded theory: 39 never mentioned that different schools exist, and some claimed to follow the classic version while using Straussian axial coding[^stol2016grounded-e26]. The SIGSOFT standard makes "state which school you used" an essential attribute[^ralph2020empirical-e317]; if you departed from a school or combined schools, explain how and why[^ralph2020empirical-e321].

The steps below use the terms of **constructivist grounded theory**. It lets you start with an initial research question and read literature as needed[^stol2016grounded-e5][^stol2016grounded-e6]; we chose it because it is easier to put into practice for a graduate student who has to write a thesis proposal. If you choose another school, swap in its counterparts from the table above.

---

## 2. How to do it

Grounded theory is not a straight line but a cycle: **collect a little data → analyze it right away → let the analysis decide what to collect next**, until theoretical saturation[^stol2016grounded-e10]. The steps below take the parts of that cycle one at a time.

### Step 0: Read the methods books before you start

**How:** Before deciding on grounded theory, read several book-length treatments from the school you are considering[^stol2016grounded-e21].

**Why:** Grounded theory looks like nothing more than "read the material and attach labels", but it is far more complex, and the guidance from different schools conflicts[^stol2016grounded-e21]. The study has to be designed as grounded theory from the start; **you cannot recast it as grounded theory when you write the paper**[^stol2016grounded-e20].

### Step 1: Start from an area or an initial question, and decide how to handle the literature

**How:**

- Write down your area of interest and initial research question, for example "how do open-source maintainers decide whether to accept or reject outside contributions?"
- Decide how much literature to read and when, according to your school[^stol2016grounded-e6]. Whatever the school, **don't take a ready-made classification from the literature and sort your data into it**.

**Why:** Limiting your reading is meant to stop you from testing existing theory without realizing it, or from thinking in borrowed concepts[^stol2016grounded-e7]. Setting up preliminary categories from the literature and then "combining them with grounded theory methods" is highly questionable[^stol2016grounded-e27]; an analysis that starts from "seed categories" or a predefined framework is not grounded theory[^stol2016grounded-e19].

For how to search the literature in general, see [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md).

### Step 2: Collect a first batch of data and start analyzing right away

**How:** Do the first few interviews (or collect the first few documents or observation notes) and **analyze each one as soon as you have it**; don't wait until everything is collected[^stol2016grounded-e10].

**What the data can be:** Mostly interview transcripts, documents and field notes, but also structured text, diagrams, even quantitative data[^stol2016grounded-e2]. Software development produces a lot of data of many kinds (code, commits, bug reports, chat logs, and so on). One approach is to pick a primary data source, such as interviews, and then draw selectively on the rest by following the leads it gives you[^stol2016grounded-e23].

**Where people go wrong:** Finishing all the interviews and then analyzing them together. This is the first antipattern the SIGSOFT standard lists: "Conducting data collection and data analysis sequentially; applying only analysis techniques of GT" (GT is grounded theory)[^ralph2020empirical-e325].

### Step 3: Coding

Constructivist grounded theory has three kinds of coding[^stol2016grounded-e8]. Stol et al. point out that describing coding as three sharply separated phases is not what Glaser or Strauss intended[^stol2016grounded-e28]; our reading is that the three constructivist kinds also alternate, and later coding sends you back to revise earlier results as new data comes in:

1. **Initial coding**: Read the data word by word, line by line or incident by incident, and give each small piece a label describing what it says, keeping your own assumptions out as far as you can[^stol2016grounded-e8].
2. **Focused coding**: Pick the most frequent or most significant codes as categories, and use them to sort larger amounts of data[^stol2016grounded-e8].
3. **Theoretical coding**: Specify how the categories relate to each other and integrate them into a coherent theory[^stol2016grounded-e8].

**Where people go wrong:**

- Sorting the data into a coding scheme fixed in advance[^stol2016grounded-e11].
- Only counting words or how often codes appear, without interpreting[^ralph2020empirical-e325].

### Step 4: Constant comparison

**How:** From the very start, keep comparing new data with old data, codes with codes, categories with data, and memos with categories[^stol2016grounded-e13]. For example: when a new interviewee says "I reject contributions because of the maintenance cost", is that the same thing as your existing category "worried about code quality", or a different category?

**Why:** Categories, and your interpretation of the data, take shape gradually through this repeated comparison[^stol2016grounded-e13].

### Step 5: Write memos

**How:** Note down your thoughts about categories as they come: what a category means, what properties it has, how it relates to other categories, what data is still missing. Any form will do: notes, diagrams, sketches[^stol2016grounded-e12].

**Why:** Memos are the main tool for getting from codes to theory. In a view Stol et al. quote, if you skip this step you are not doing grounded theory[^stol2016grounded-e12]. In the paper, ideally explain how memoing drove the study[^ralph2020empirical-e319].

### Step 6: Theoretical sampling: let the analysis decide whom to approach next

**How:** Theoretical sampling means **choosing what data to collect next based on the emerging theory, concepts or categories**[^ralph2020empirical-e328]: wherever there is a gap or a concept is still unclear, go and find the people or material that can fill it[^stol2016grounded-e10]. For example, if the category "maintainers' time pressure" emerges, your next step is to seek out a few full-time and a few volunteer maintainers specifically to compare them.

**Where people go wrong:**

- Choosing a few companies or groups of people in advance and calling that "theoretical sampling". Some papers have done exactly this, and it is not theoretical sampling[^stol2016grounded-e18].
- Interviewing only a group of similar people. A small, homogeneous sample creates an illusion of convergence and saturation; it is hard to build a complete theory from interviews with 20 similar people[^ralph2020empirical-e326]. Ideally, your data should cover a diverse range of people or things[^ralph2020empirical-e319].
- Relying on interviews alone, without cross-checking against documents, observation or other evidence[^ralph2020empirical-e326]. People's after-the-fact explanations of why they did something are less reliable than their descriptions of what is bothering them now; in software settings, code, commit histories and project management data can all be used to check what interviewees tell you[^stol2016grounded-e23]. For how to triangulate, see [Case studies](case_study.md#step-6-collect-data-from-several-sources-and-cross-check-them).

### Step 7: Judge theoretical saturation, then stop

**How:** When every part of the theory is well supported and new data no longer leads you to modify or reinterpret the theory, you have reached **theoretical saturation** and can stop collecting[^stol2016grounded-e14]. This is a higher bar than the "new interviewees no longer bring new information" that interview studies usually mean (see [Interview studies](interview_study.md#step-1-choose-interviewees)): the question is whether the theory changed, not just whether anyone said something new.

**What the paper must state:** whether you reached saturation, **how you judged it**[^ralph2020empirical-e317], and when you stopped collecting[^stol2016grounded-e24]. "By the Nth interviewee there was nothing new" is just a sentence; better to explain which parts of the theory the last few rounds of data tested and why they didn't lead to changes.

### Step 8: Produce a theory, not a set of themes

This is the biggest difference between grounded theory and qualitative analysis in general. You have to go beyond surface categories and develop a coherent theory[^stol2016grounded-e15]:

- **Present the results as concepts that give the data meaning, not just a description of the data**[^ralph2020empirical-e318];
- **Spell out the relationships between concepts**, and push on to a theory instead of stopping at a set of unconnected themes[^ralph2020empirical-e319];
- Ideally, summarize the main concepts and their relationships in a diagram[^ralph2020empirical-e320].

One example Stol et al. give: a study identified several roles that members of agile teams take on, and together these roles explained how the teams organize themselves, so the result went beyond a mere taxonomy of roles[^stol2016grounded-e17].

In practice this step is often missed. Of the 52 papers that claimed to use grounded theory[^stol2016grounded-e16], only 8 clearly presented a theory made of concepts and relationships; studies that produce only "a set of themes" have often just borrowed bits and pieces of grounded theory practice[^stol2016grounded-e17].

### Step 9: Validate and write up

- **Check your results**: member checking, feedback from practitioners who were not in the study, and having your advisor or peers review the coding are all desirable attributes[^ralph2020empirical-e319]; for how, see [Interview studies](interview_study.md#step-6-make-your-analysis-trustworthy).
- **Describe what you did, not a tutorial**: explain how you yourself carried out the study, including where you departed from your school's guidance, rather than explaining the principles of grounded theory[^stol2016grounded-e20][^ralph2020empirical-e325].
- **Tie key concepts to the raw data**, for example with quotations[^ralph2020empirical-e318]; where you can, provide the interview guide, the coding scheme and coding examples[^ralph2020empirical-e320].
- **Engage with existing research**: compare your theory with existing theories or integrate it with them[^ralph2020empirical-e320], and explain what role the literature played in your study[^ralph2020empirical-e321].
- **Discuss transferability**: how far the theory might apply to other sites, populations or contexts[^ralph2020empirical-e318][^ralph2020empirical-e329]; reflect on how your own biases may have shaped the analysis[^ralph2020empirical-e321].

For quality criteria in qualitative research, see [Interview studies](interview_study.md#first-remember-qualitative-research-has-different-quality-criteria-from-quantitative-research); for the chain of evidence, see [Case studies](case_study.md#step-7-keep-a-chain-of-evidence-during-analysis); for writing in general, see [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md).

---

## 3. Checklist

This list follows the SIGSOFT grounded theory standard, which is the review standard for software engineering; in other fields, your field's conventions take precedence.

**Essential**

- [ ] State which school you used[^ralph2020empirical-e317]
- [ ] Describe the data: participants' backgrounds, types of documents, the nature of the field notes, and so on[^ralph2020empirical-e317]
- [ ] Explain how data collection (theoretical sampling) and analysis (constant comparison) alternated[^ralph2020empirical-e317]
- [ ] State whether, and how, you judged that theoretical saturation was reached[^ralph2020empirical-e317]
- [ ] Explain the steps by which the key categories were arrived at[^ralph2020empirical-e317]
- [ ] Present results as concepts that give the data meaning, not just a description of it[^ralph2020empirical-e318]
- [ ] Ground key concepts explicitly in the raw data, for example with quotations[^ralph2020empirical-e318]
- [ ] Discuss the transferability of the theory[^ralph2020empirical-e318] and disclose the main limitations[^ralph2020empirical-e103]

**Desirable**

- [ ] Results include relationships between concepts, summarized in a diagram[^ralph2020empirical-e319][^ralph2020empirical-e320]
- [ ] Tables trace categories to their underlying codes, and concepts to observations[^ralph2020empirical-e320]
- [ ] Explain how memoing drove the study[^ralph2020empirical-e319]
- [ ] Data covers a diverse range of people or things[^ralph2020empirical-e319]
- [ ] Results are checked through member checking, peer review of the coding, or similar[^ralph2020empirical-e319]
- [ ] Explain departures from the school, the role of the literature, and reflect on your own biases[^ralph2020empirical-e321]
- [ ] Provide supplementary material such as the interview guide and coding scheme[^ralph2020empirical-e320]

**Extraordinary**

- [ ] Triangulate with substantial quantitative data (for example a questionnaire)[^ralph2020empirical-e322]
- [ ] Carried out by a research team, with each member's role explained[^ralph2020empirical-e322]

**Acceptable deviations (not flaws)**

- Omitting detailed descriptions of interviewees and direct quotations to protect participants (for example on sensitive topics such as harassment)[^ralph2020empirical-e324]

**Common but invalid reviewer criticisms** (as listed in the SIGSOFT standard, for software engineering submissions)[^ralph2020empirical-e327]: you need not worry about these

- "Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability"
- "Lack of replicability or reproducibility; not releasing transcripts"
- "Lack of representativeness (e.g. of a study of Turkish programmers, 'how does this generalize to America?')"
- "Findings should have been presented as a different set of relationships, hypotheses, or a different theory"

Grounded theory studies should be judged on credibility, resonance and usefulness (see [Interview studies](interview_study.md#first-remember-qualitative-research-has-different-quality-criteria-from-quantitative-research) for what these mean), and on whether they extend existing knowledge; quantitative criteria such as internal validity and reproducibility generally do not apply[^ralph2020empirical-e323].

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Using only the coding techniques but writing "we used grounded theory" | This is called "method slurring". If you only borrowed techniques, just say which techniques you used[^stol2016grounded-e20]; of 98 papers mentioning grounded theory, 46 had in fact only used its techniques[^stol2016grounded-e16] |
| Finishing all the interviews before analyzing | Without collection and analysis alternating, there is no theoretical sampling[^ralph2020empirical-e325][^stol2016grounded-e19] |
| Sorting the data into categories taken from the literature | That is applying an existing framework, not grounded theory[^stol2016grounded-e19][^stol2016grounded-e27] |
| Picking interviewees in advance and calling it "theoretical sampling" | Theoretical sampling means letting gaps in the analysis decide whom to approach next[^stol2016grounded-e18] |
| Declaring "saturation" after a dozen or so similar interviewees | A small, homogeneous sample creates an illusion of saturation[^ralph2020empirical-e326] |
| Producing only a few unconnected themes | Grounded theory should produce a theory made of concepts and relationships[^ralph2020empirical-e319][^stol2016grounded-e17] |
| Writing the methods section as a grounded theory tutorial | Readers need to know what you specifically did[^ralph2020empirical-e325][^stol2016grounded-e20] |
| Not naming a school, or claiming one school while using another's procedures | The schools make different demands about research questions, literature and coding[^stol2016grounded-e26] |
| Recasting the study as grounded theory only when writing the paper | Grounded theory has to start at the design stage[^stol2016grounded-e20] |

---

## 5. Further reading

- **How grounded theory is used in software engineering, and its common problems**: Stol, Ralph & Fitzgerald 2016. Compares the three schools and summarizes the core practices; its Figure 5 is a very practical list of questions to ask yourself before writing up.
- **Review standard**: the grounded theory standard in the SIGSOFT Empirical Standards, with suggested readings and exemplar papers.
- **The original books of each school**: Stol et al. recommend reading a few introductory books from your chosen school before you start[^stol2016grounded-e21], for example Glaser & Strauss for the classic version, Corbin & Strauss for the Straussian version, and Charmaz for the constructivist version. These book suggestions are ours; we have not read these books in full.

Links to all sources are in the [source list](../../sources/README.md).

[^stol2016grounded-e1]: Stol et al. 2016, §1. [Evidence](../../sources/notes/stol2016grounded.md#e1)
[^stol2016grounded-e2]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e2)
[^stol2016grounded-e3]: Stol et al. 2016, §2.3. [Evidence](../../sources/notes/stol2016grounded.md#e3)
[^stol2016grounded-e4]: Stol et al. 2016, §2.3. [Evidence](../../sources/notes/stol2016grounded.md#e4)
[^stol2016grounded-e5]: Stol et al. 2016, Table 1, row "research question". [Evidence](../../sources/notes/stol2016grounded.md#e5)
[^stol2016grounded-e6]: Stol et al. 2016, Table 1, row "role of the literature". [Evidence](../../sources/notes/stol2016grounded.md#e6)
[^stol2016grounded-e7]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e7)
[^stol2016grounded-e8]: Stol et al. 2016, Table 1, row "coding steps" (constructivist version). [Evidence](../../sources/notes/stol2016grounded.md#e8)
[^stol2016grounded-e9]: Stol et al. 2016, Table 1, row "coding steps" (classic and Straussian versions). [Evidence](../../sources/notes/stol2016grounded.md#e9)
[^stol2016grounded-e10]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e10)
[^stol2016grounded-e11]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e11)
[^stol2016grounded-e12]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e12)
[^stol2016grounded-e13]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e13)
[^stol2016grounded-e14]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e14)
[^stol2016grounded-e15]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e15)
[^stol2016grounded-e16]: Stol et al. 2016, Abstract. [Evidence](../../sources/notes/stol2016grounded.md#e16)
[^stol2016grounded-e17]: Stol et al. 2016, §4.4. [Evidence](../../sources/notes/stol2016grounded.md#e17)
[^stol2016grounded-e18]: Stol et al. 2016, §4.2. [Evidence](../../sources/notes/stol2016grounded.md#e18)
[^stol2016grounded-e19]: Stol et al. 2016, §5.1. [Evidence](../../sources/notes/stol2016grounded.md#e19)
[^stol2016grounded-e20]: Stol et al. 2016, §5.2. [Evidence](../../sources/notes/stol2016grounded.md#e20)
[^stol2016grounded-e21]: Stol et al. 2016, §5.2. [Evidence](../../sources/notes/stol2016grounded.md#e21)
[^stol2016grounded-e22]: Stol et al. 2016, §5.1. [Evidence](../../sources/notes/stol2016grounded.md#e22)
[^stol2016grounded-e23]: Stol et al. 2016, §5.3. [Evidence](../../sources/notes/stol2016grounded.md#e23)
[^stol2016grounded-e24]: Stol et al. 2016, Fig. 5. [Evidence](../../sources/notes/stol2016grounded.md#e24)
[^stol2016grounded-e25]: Stol et al. 2016, §1 and §6. [Evidence](../../sources/notes/stol2016grounded.md#e25)
[^stol2016grounded-e26]: Stol et al. 2016, §4.3. [Evidence](../../sources/notes/stol2016grounded.md#e26)
[^stol2016grounded-e27]: Stol et al. 2016, §4.1. [Evidence](../../sources/notes/stol2016grounded.md#e27)
[^stol2016grounded-e28]: Stol et al. 2016, §4.2. [Evidence](../../sources/notes/stol2016grounded.md#e28)
[^ralph2020empirical-e316]: SIGSOFT Grounded Theory standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e316)
[^ralph2020empirical-e317]: SIGSOFT Grounded Theory standard, Essential Attributes (methods). [Evidence](../../sources/notes/ralph2020empirical.md#e317)
[^ralph2020empirical-e318]: SIGSOFT Grounded Theory standard, Essential Attributes (results and discussion). [Evidence](../../sources/notes/ralph2020empirical.md#e318)
[^ralph2020empirical-e319]: SIGSOFT Grounded Theory standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e319)
[^ralph2020empirical-e320]: SIGSOFT Grounded Theory standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e320)
[^ralph2020empirical-e321]: SIGSOFT Grounded Theory standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e321)
[^ralph2020empirical-e322]: SIGSOFT Grounded Theory standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e322)
[^ralph2020empirical-e323]: SIGSOFT Grounded Theory standard, Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e323)
[^ralph2020empirical-e324]: SIGSOFT Grounded Theory standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e324)
[^ralph2020empirical-e325]: SIGSOFT Grounded Theory standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e325)
[^ralph2020empirical-e326]: SIGSOFT Grounded Theory standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e326)
[^ralph2020empirical-e327]: SIGSOFT Grounded Theory standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e327)
[^ralph2020empirical-e328]: SIGSOFT Glossary, Theoretical sampling. [Evidence](../../sources/notes/ralph2020empirical.md#e328)
[^ralph2020empirical-e329]: SIGSOFT Glossary, Credibility, Resonance, Transferability. [Evidence](../../sources/notes/ralph2020empirical.md#e329)
[^ralph2020empirical-e103]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e103)
