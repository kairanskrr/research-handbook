# Interview studies: in-depth interviews with a set of people, analyzed into themes

This page covers **interview studies**: you conduct semi-structured or open-ended in-depth interviews with a set of people, then use qualitative analysis to derive themes from the interview records. The empirical standards of ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) call this kind of study a "qualitative survey".

If what you want is to collect answers from many people with a questionnaire and analyze them statistically, that is a [Questionnaire surveys](questionnaire_survey.md), which this page does not cover. For the general ethics requirements when research involves people, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); this page covers only what is specific to interviews.

Of the three pages on qualitative research, this is the one that covers **sampling and saturation, interviewing, coding and thematic analysis, and qualitative quality criteria**; [Case studies](case_study.md) and [Grounded theory](grounded_theory.md) link here when they need these topics.

**Scope** `[Our analysis]`: The review standards and most examples on this page come from software engineering (the SIGSOFT standards, Runeson and Höst's case study guidelines, Baltes and Ralph's sampling guidelines). The discussion of coding agreement comes from human–computer interaction and computer-supported cooperative work (McDonald et al.). The practices for thematic analysis and for interview guides come from the methods literature of psychology (Braun and Clarke) and nursing (Kallio et al.) respectively. If you are doing an interview study in another field, start with your field's conventions. Historians use interviews to create records of the past, which works differently from what is described here; see [Oral history](oral_history.md).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md).

**After reading this page, you should be able to:**

- judge whether your question is one an interview study can answer;
- choose interviewees, design an interview guide, and conduct and transcribe the interviews;
- use thematic analysis to derive themes from transcripts, and explain why your analysis is trustworthy;
- understand that qualitative research has different quality criteria from quantitative research, and not be thrown off by criticisms that don't apply.

---

## 1. What this kind of study is, and when to use it

The SIGSOFT standard says it applies when the researcher and a participant talk one-on-one in real time; the researcher asks open-ended questions and the participant answers; the answers are recorded in some way; and the answers then undergo some form of qualitative analysis[^ralph2020empirical-e345].

**Questions it is good at** `[Our analysis]`:

- **"How" and "why"**: why developers don't use a tool, how security engineers decide which vulnerability to fix first, how machine learning practitioners handle problematic data;
- **People's experiences and views**: what difficulties a group runs into, how they make sense of something;
- **Phenomena nobody has studied systematically yet**: use interviews to find out which factors are involved, then decide what a follow-up questionnaire or experiment should measure.

It can't answer questions like "how many people do this?" or "does A cause B?"; those need questionnaires, repository mining or experiments. `[Our analysis]` In computer science, interviews are common in human–computer interaction and computer-supported cooperative work: of the 251 qualitative papers in that area analyzed by McDonald et al., 179 (71.3%) used interviews[^mcdonald2019reliability-e3]. They are also common in software engineering, security (for example usable security), machine learning practice and other areas. `[Our analysis]`

**How it differs from related methods**:

| | Interview study | Case study | Grounded theory | Questionnaire survey |
|---|---|---|---|---|
| Data | Interviews with a set of people | Many kinds of data from one or a few settings | Interviews and other data, alternating repeatedly with analysis | Standardized answers from many people |
| Participants | From different places | Often from the same organization | Sought out according to the emerging theory | As representative as possible |
| Main output | Themes, concepts, classifications | In-depth understanding of one setting | A new theory | Proportions, correlations |

Sources for the table: when all interviewees come from the same organization, consider the case study standard; when data collection and analysis alternate repeatedly, consider the grounded theory standard[^ralph2020empirical-e346]; interview studies usually involve more interviews than case studies, while case studies rely on several kinds of data corroborating each other[^ralph2020empirical-e347]. Calling an interview study grounded theory or a case study is an antipattern listed in the SIGSOFT standard[^ralph2020empirical-e362]. The questionnaire survey column and the "Main output" row are `[Our analysis]`.

### First, remember: qualitative research has different quality criteria from quantitative research

This is the thing to understand before anything else in an interview study. The SIGSOFT standard says an interview study should meet appropriate qualitative quality criteria; quantitative quality criteria such as internal validity, construct validity, generalizability and reliability **generally do not apply**[^ralph2020empirical-e348]. The four common qualitative criteria are below (definitions from the SIGSOFT glossary)[^ralph2020empirical-e349]; the [case study](case_study.md) and [Grounded theory](grounded_theory.md) standards use them too:

| Criterion | Meaning |
|---|---|
| Credibility | The conclusions are supported by rich, multivocal evidence |
| Resonance | The conclusions make sense to the participants |
| Usefulness | The study gives researchers, practitioners or educators actionable recommendations |
| Transferability | The results may apply to other settings, populations or situations |

The underlying reason is a difference in research stance (for the two views on whether qualitative research should talk about "validity", see "Where sources disagree" at the end of [Validity and limitations](../02_do-the-project/04_validity-and-limits.md)). Many qualitative researchers avoid the words "validity" and "reliability" altogether and use concepts such as credibility and transferability instead[^mcdonald2019reliability-e6]. Judging qualitative research by quantitative criteria is a common mistake[^mcdonald2019reliability-e7]; SIGSOFT also lists cross-paradigmatic criticism, such as "attacking an interpretivist study for not conforming to positivist norms," as an invalid criticism[^ralph2020empirical-e373].

---

## 2. How to do it

### Step 1: Choose interviewees

**How:**

- **Choose with a purpose, not whoever is convenient.** Purposive sampling means selecting cases carefully but non-randomly, following some logic or strategy, with the aim of finding information-rich people who can teach you about your topic[^baltes2022sampling-e23]. "Interviewing whoever is willing to talk" is convenience sampling[^baltes2022sampling-e25]; exploratory research should prefer purposive sampling[^ralph2020empirical-e372].
- **Deliberately seek variation.** Choose interviewees for their differences, not their similarity[^runeson2009guidelines-e14], for example covering different roles and personalities[^runeson2009guidelines-e47]. Highly diverse participants are a desirable attribute in SIGSOFT[^ralph2020empirical-e355]. In computer science you can deliberately cover companies of different sizes, open-source and commercial projects, and people with different years of experience. `[Our analysis]`
- **Adjust whom you look for as the analysis develops.** Theoretical sampling means letting the emerging concepts decide whom to approach next[^baltes2022sampling-e26]; when you are building theory, it should be preferred[^ralph2020empirical-e372]. For how to do it, see [Grounded theory](grounded_theory.md#step-6-theoretical-sampling-let-the-analysis-decide-whom-to-approach-next).
- **Interview until saturation.** The number of interviews is decided during the study, and a common criterion is "saturation": new interviewees no longer bring new information or perspectives[^runeson2009guidelines-e14]. SIGSOFT makes "provides evidence of saturation; explains how saturation was achieved" an essential attribute[^ralph2020empirical-e352]. For example, you can record how many new codes each interview added and show that the last few interviews added almost none. `[Our analysis]` The "theoretical saturation" of grounded theory sets a higher bar: new data no longer changes the theory; see [Grounded theory](grounded_theory.md#step-7-judge-theoretical-saturation-then-stop).
- **Explain why you chose these people.** Qualitative research has to let readers see why you chose the people you did[^baltes2022sampling-e7]. Purposive sampling is inherently subjective[^baltes2022sampling-e24], which is all the more reason to write out your selection logic so readers can judge it.

**Why:** The aim of an interview study is usually not to generalize from a sample to a population but to find people who can shed light on the problem. In SIGSOFT's view, the lack of probability sampling or statistical representativeness is not a flaw, unless your study explicitly aims for representativeness[^ralph2020empirical-e363].

**Where people go wrong:** Interviewing only a few similar people creates a false impression of convergent views and "saturation"[^ralph2020empirical-e362]. If you interview just five engineers from the company your lab works with and they all say the same thing, that may simply be because they share the same background. `[Our analysis]`

### Step 2: Design the interview guide

**How:**

1. **Derive interview questions from your research questions, but don't reuse the research questions' wording**[^runeson2009guidelines-e6]. Research questions are written for researchers; interviewees need concrete questions that are easy to answer. `[Our analysis]`
2. **Use a semi-structured format**: list the questions in advance, but don't feel bound to ask them in order; leave room to improvise and dig deeper[^runeson2009guidelines-e7].
3. **Mostly ask open questions.** Open questions invite a wide range of answers; closed questions offer only a few options[^runeson2009guidelines-e8]. For example, ask "Tell me about the last time you tracked down a production incident" rather than "Do you look at logs when you troubleshoot?" `[Our analysis]`
4. **Prepare probes for each topic.** The guide has two levels: main topics and follow-up probes[^kallio2016systematic-e1]. Probes can be designed in advance, so that different interviewers cover more consistent ground, or used on the spot to ask the person to say more about a point[^kallio2016systematic-e3]. Ways of probing include repeating back what the person said, using verbal cues to show interest, or simply staying silent so they think aloud[^kallio2016systematic-e4].
5. **Plan the order.** You can start with open questions and move gradually to specific ones (the "funnel" model)[^runeson2009guidelines-e11]; begin with easy topics and then move to deeper ones[^kallio2016systematic-e2].
6. **Pilot it first.** You can try it within your team, ask outside experts to review it, or field-test it with one or two potential interviewees[^kallio2016systematic-e5]. Internal piloting helps you remove vague and leading questions[^kallio2016systematic-e6].

**Where people go wrong:** Leading questions, such as "Don't you think this tool is too hard to use?", put your expectations into the interviewee's mouth. `[Our analysis]` Also, some ethics committees require every interview question to be reviewed in advance, which is impossible for on-the-spot probes[^kallio2016systematic-e7]; when you apply for ethics review, it is best to describe the general scope of your probes. `[Our analysis]`

### Step 3: Conduct the interviews

- **Opening**: explain the purpose of the interview and how the data will be used, then ask a few easy background questions[^runeson2009guidelines-e9].
- **Save sensitive questions for later**, once trust has been built. **At the end**, summarize the main points you heard and ask the interviewee to confirm or correct them, to avoid misunderstandings[^runeson2009guidelines-e10].
- **Record audio** (with consent): with notes alone it is hard to capture every detail, and during the interview you can't know what will turn out to matter[^runeson2009guidelines-e12].
- **Informed consent and compensation**: explain how you obtained free, individual, informed consent, what compensation you gave, and how you avoided coercion[^ralph2020empirical-e369] (for the general requirements, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first)).

**Watch for power relationships** (this applies equally when a [case study](case_study.md) enters an organization). If you recruit interviewees through a "gatekeeper" such as a company manager or an advisor, the interviewees may not really be participating voluntarily; an employer might, for example, coerce employees into taking part[^ralph2020empirical-e370]. In that case, explain how you mitigated the power relationship between gatekeeper and interviewees to make sure consent was freely given[^ralph2020empirical-e186]. By the same logic, if you interview your own students or subordinates, they may not dare to speak frankly or to say no. `[Our analysis]` SIGSOFT lists describing "the relationships and interactions between researchers and participants relevant to the research process" as a desirable attribute[^ralph2020empirical-e355]. The interview format can also be adapted: for example, when studying deaf developers, interviewing by text message is acceptable[^ralph2020empirical-e364].

### Step 4: Transcribe

- **Transcribe yourself where possible.** Transcription takes time, but new ideas often come up while you do it, so Runeson & Höst recommend that researchers do it themselves[^runeson2009guidelines-e13]. Transcription is also not just turning sound into text; it is itself an act of interpretation[^braun2006using-e5].
- **If someone else or software transcribes, always check the transcript against the recording**, and spend extra time getting familiar with the data[^braun2006using-e6]. Automatic transcription tools often get technical terms, accents and multi-person conversations wrong. `[Our analysis]`
- **You can ask interviewees to review their transcripts** and correct anything misspoken or misrecorded[^runeson2009guidelines-e13].

### Step 5: Coding and thematic analysis

The steps below use thematic analysis as the example: a method for identifying, analyzing and reporting patterns ("themes") in data[^braun2006using-e1]. **First, tell codes and themes apart:** a code is a label attached to a short stretch of talk, such as "outdated documentation" or "afraid of being judged by colleagues"; a theme is broader, a pattern relevant to your research question that forms when many codes are gathered together[^braun2006using-e9].

**Braun & Clarke's six phases**[^braun2006using-e8]:

1. **Familiarize yourself with the data**: read the transcripts repeatedly, noting ideas as you go[^braun2006using-e7];
2. **Generate initial codes**: code the whole dataset systematically;
3. **Search for themes**: gather codes into candidate themes;
4. **Review themes**: data within a theme should hold together, and different themes should be clearly distinct[^braun2006using-e11];
5. **Define and name themes**: a test is whether you can describe the scope and content of each theme in a couple of sentences[^braun2006using-e12];
6. **Produce the report**.

**Choose inductive or deductive, and say which.** Inductive coding lets the coding scheme arise from the data, with the aim of proposing new concepts or theory; deductive coding uses a predefined coding scheme based on existing theory, with the aim of testing that theory[^ralph2020empirical-e357]. Inductive themes stay closer to the data itself; deductive analysis gives less description of the data overall but a more detailed analysis of one aspect[^braun2006using-e2][^braun2006using-e3]. Even in inductive analysis, though, researchers cannot free themselves of their theoretical commitments[^braun2006using-e2].

**Some practical habits:**

- **Build a codebook**: for each code, write its name, a definition, when to use it and when not to, plus an example or two. The codebook will keep changing as the analysis goes on. `[Our analysis]` When several people code, their disagreements are exactly what help you improve the codebook[^mcdonald2019reliability-e14].
- **Write analytic memos**: note your thoughts on relationships between codes, possible themes and your own open questions as they come. Memo writing, reflection, and review are practices designed precisely to support a researcher working alone[^mcdonald2019reliability-e13]. Memos are a core step in grounded theory; for how to write them, see [Grounded theory](grounded_theory.md#step-5-write-memos).
- **Put it in a table**: rows are codes, columns are interviewees, so you can see at a glance who mentioned what[^runeson2009guidelines-e17].
- **Analyze while you interview**: what you learn from the analysis may require you to adjust later interview questions[^runeson2009guidelines-e15]. If you iterate heavily between collection and analysis, you are closer to grounded theory and should follow its standard[^ralph2020empirical-e346].
- **Keep the dissenting voices**; don't code only what fits the dominant story[^braun2006using-e10].
- **Themes are not counted into existence.** A theme should ideally recur across the data, but appearing more often doesn't make it more important; deciding what counts as a theme takes the researcher's judgment[^braun2006using-e4].

### Step 6: Make your analysis trustworthy

Qualitative research doesn't establish its quality by showing that someone else would get the same result; it relies on the practices below `[Our analysis, based on the sources below]`. They apply equally to [case studies](case_study.md) and [Grounded theory](grounded_theory.md):

- **Reflexivity**: reflect on your possible biases, and on how your relationship with the interviewees and their community may have affected the study[^ralph2020empirical-e350]. This is an essential attribute in SIGSOFT[^ralph2020empirical-e353]. For example, if you developed a tool yourself and interview its users, say so, and explain how you guarded against hearing only what you wanted to hear. `[Our analysis]`
- **Member checking**: show your analysis to the interviewees. Participants don't have to agree with your conclusions, but doing this increases the validity of the study[^runeson2009guidelines-e18]. Other validation methods SIGSOFT lists include dialogical interviewing, feedback from practitioners who were not in the study, and having an advisor or other researchers review the coding[^ralph2020empirical-e358].
- **Actively look for other explanations**: consider other obvious readings of the data, as well as variations and contradictions in the accounts[^braun2006using-e17][^ralph2020empirical-e359].
- **Make your process open**: besides member checking, re-interviewing participants, corroboration with other data sources (triangulation; see [Case studies](case_study.md#step-6-collect-data-from-several-sources-and-cross-check-them) for details), making the research process transparent and stating the researcher's position are all ways of communicating reliability[^mcdonald2019reliability-e5].

> **Where sources disagree: should several people code, and should you compute agreement?**
>
> Inter-rater reliability (IRR) is a statistic for how much two or more coders' judgments agree; common measures include Cohen's kappa (a statistic for how much two raters agree) and Krippendorff's alpha. It comes from the positivist quantitative tradition, and its use in qualitative research has long been contested[^mcdonald2019reliability-e1].
>
> - **The case for computing it**: having several people code reduces individual bias[^mcdonald2019reliability-e15][^runeson2009guidelines-e16]; SIGSOFT lists "uses multiple coders and analyzes inter-coder reliability" as an extraordinary attribute[^ralph2020empirical-e361]. It is especially suitable when several people code different parts of the data, when you apply an existing codebook, or when you will report quantitative results[^mcdonald2019reliability-e11]. If your conclusions depend on frequency counts (for example, "X came up three times as often as Y"), there is a strong case for computing it[^mcdonald2019reliability-e12].
> - **The case against needing it**: SIGSOFT's own supplement on inter-rater reliability does not apply to interpretivist qualitative analysis, because from that stance different analysts are expected to see things differently[^ralph2020empirical-e365]. It is also unsuitable when developing the codes is itself part of the analytic process, when there is only one researcher, or when the coding requires almost no interpretation[^mcdonald2019reliability-e10]. Having several people apply a predefined coding scheme to material is far more realistic than having several people inductively code 2,000 pages of transcripts[^ralph2020empirical-e366]. A statistic cannot replace interpreting the data[^mcdonald2019reliability-e8]. Among the qualitative papers McDonald et al. analyzed, only about one in nine computed it[^mcdonald2019reliability-e2].
>
> In practice: **make your approach consistent with your research stance and analytic goals**[^mcdonald2019reliability-e9]. For inductive, interpretive analysis, one person can do the main coding, with a second person reviewing it and discussing disagreements, and the paper explaining why; for deductive coding, divided coding work, or when you report frequencies, compute agreement. `[Our analysis]` Either way, don't report only percentage agreement, because it ignores agreement that happens by chance[^mcdonald2019reliability-e4]; and don't compute several measures and report only the best-looking one[^ralph2020empirical-e368].

### Step 7: Write the report

- **Describe the interviewees and the interviewers.** This is essential: the interviewees' demographics and job roles, and the interviewers' experience and perspective[^ralph2020empirical-e351]. A common format is a participant table with an ID for each person (P1, P2, …) listing role, years of experience, type of organization and so on. `[Our analysis]`
- **Give a clear chain of evidence from what people said to your conclusions**[^ralph2020empirical-e352]. Use plenty of direct quotations to support key points[^ralph2020empirical-e356]; choose vivid extracts that capture the essence of the point, and embed them in your analytic narrative[^braun2006using-e13].
- **Describe the method in detail**: which core questions you asked, whether they were open or closed[^ralph2020empirical-e354], how the interviews were recorded and transcribed[^ralph2020empirical-e356]. Ideally, publish the interview guide, coding scheme and coding examples as supplementary material[^ralph2020empirical-e354].
- **Make clear who did the analysis.** Don't write "themes emerged from the data"; that denies the active role the researcher plays in identifying and selecting themes[^braun2006using-e18]. Use the active voice in the methods section, because the passive voice hides the researcher's role[^mcdonald2019reliability-e16]. **What you say you did and what you actually did must match**[^braun2006using-e19].

**Protect your interviewees.** For general anonymization requirements, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first). The most common leak in interview studies is background information like "company X + job title Y", which together can pin down a single person[^ralph2020empirical-e253]. With small teams or sensitive topics, think carefully about details in quotations and combinations of attributes in the participant table. `[Our analysis]` In sensitive studies, omitting detailed descriptions of interviewees and direct quotations to protect participants is acceptable[^ralph2020empirical-e364]. Not publishing full transcripts is not a flaw either[^ralph2020empirical-e363].

---

## 3. Checklist

This list mainly follows the SIGSOFT standard for interview studies (Qualitative Surveys), which is the review standard for software engineering; in other fields, your field's conventions take precedence `[Our analysis]`.

**Essential**

- [ ] Explain how interviewees were selected[^ralph2020empirical-e351]
- [ ] Describe the interviewees (e.g. demographics, job roles) and the interviewers (e.g. experience, perspective)[^ralph2020empirical-e351]
- [ ] Give a clear chain of evidence from interviewees' words to the findings[^ralph2020empirical-e352]
- [ ] Answer the research questions explicitly[^ralph2020empirical-e352]
- [ ] Provide evidence of saturation and explain how it was reached[^ralph2020empirical-e352]
- [ ] Reflect on the researchers' own possible biases[^ralph2020empirical-e353]
- [ ] Explain how informed consent was obtained, what compensation was given, and how coercion was avoided[^ralph2020empirical-e369]

**Desirable**

- [ ] Describe the content and form (open or closed) of the core questions; publish the interview guide, coding scheme, coding examples and decision rules[^ralph2020empirical-e354]
- [ ] Highly diverse participants; describe the relationship between researchers and participants[^ralph2020empirical-e355]
- [ ] Use plenty of direct quotations; explain how interviews were recorded and transcribed[^ralph2020empirical-e356]
- [ ] Explicitly use deductive coding to test existing theory, or inductive coding to propose new theory[^ralph2020empirical-e357]
- [ ] Validate results with member checking, outside feedback or review of the coding[^ralph2020empirical-e358]
- [ ] Discuss transferability, relationship to existing research, and alternative explanations[^ralph2020empirical-e359]
- [ ] Describe incentives and the ethics process[^ralph2020empirical-e360]

**Extraordinary**: several analysis methods corroborating each other; a longitudinal design (interviewing the same people more than once); probability sampling with statistical analysis of response bias; multiple coders with analysis of their agreement[^ralph2020empirical-e361]

**Acceptable deviations (not flaws)**: interviewing by text or other means when interviewees have special needs; omitting detailed descriptions of interviewees and direct quotations to protect participants in sensitive studies[^ralph2020empirical-e364]

**Common but invalid reviewer criticisms** (as listed in the SIGSOFT standard, for software engineering submissions): you need not worry about these, but it is still best to state your position in the paper

- "Lacks quantitative data, causal analysis, objectivity, internal validity, reliability or generalizability"[^ralph2020empirical-e363]
- "Not replicable", "transcripts not published"[^ralph2020empirical-e363]
- "No probability sampling, not representative" (unless the study explicitly aims for representativeness)[^ralph2020empirical-e363]
- "The sample is too small", without considering how participants were chosen or the saturation argument[^ralph2020empirical-e371]
- "Only one coder", when multiple coders are impractical or inconsistent with the research stance[^ralph2020empirical-e367]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Interviewing a few similar people and declaring saturation | Creates a false impression of convergent views and saturation[^ralph2020empirical-e362] |
| Leading questions in the guide | They push your expectations onto the interviewee; remove them during piloting[^kallio2016systematic-e6] |
| Taking notes only, without recording | You miss details, and at the time you can't tell what will matter[^runeson2009guidelines-e12] |
| Not checking automatic transcripts against the recording | Transcripts should be checked against the original recordings[^braun2006using-e6] |
| Using the interview guide's questions as the themes | That amounts to doing no analysis[^braun2006using-e15] |
| Stringing quotations together with almost no analysis | That is not thematic analysis[^braun2006using-e14] |
| Building a theme on one or two examples | You present isolated cases as a theme running through the whole dataset[^braun2006using-e16] |
| Holding yourself to quantitative validity, reliability and generalizability | Wrong criteria[^ralph2020empirical-e348] |
| Calling an interview study grounded theory or a case study | An antipattern listed by SIGSOFT[^ralph2020empirical-e362] |
| Describing interviewees by "company + job title" | Interviewees may be identifiable[^ralph2020empirical-e253] |

---

## 5. Further reading

- **Getting started with thematic analysis**: Braun & Clarke 2006, covering the six phases, common pitfalls and what good thematic analysis should look like. It comes from psychology and is a standard introduction to thematic analysis.
- **Designing an interview guide**: Kallio et al. 2016, a review of the steps for designing a semi-structured interview guide, including probes and piloting. It comes from nursing, but the practices transfer.
- **Interviews in software engineering**: the interview section of Runeson & Höst 2009, covering interview phases, question styles, recording and transcription. It is a case study guide and keeps terms such as validity and reliability; when you read it, keep that distinct from the qualitative quality criteria on this page `[Our analysis]`.
- **Whether to compute agreement**: McDonald et al. 2019, with recommendations on when inter-rater reliability is and isn't needed.
- **The standards themselves**: SIGSOFT's Qualitative Surveys standard, plus its three supplements on inter-rater reliability, ethics involving human participants, and sampling; for sampling methods in detail, see Baltes & Ralph 2022.

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e345]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e345)
[^ralph2020empirical-e346]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e346)
[^ralph2020empirical-e347]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Notes. [Evidence](../../sources/notes/ralph2020empirical.md#e347)
[^ralph2020empirical-e348]: SIGSOFT Qualitative Surveys (Interview Studies) standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e348)
[^ralph2020empirical-e349]: SIGSOFT Glossary. [Evidence](../../sources/notes/ralph2020empirical.md#e349)
[^ralph2020empirical-e350]: SIGSOFT Glossary, Reflexivity. [Evidence](../../sources/notes/ralph2020empirical.md#e350)
[^ralph2020empirical-e351]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e351)
[^ralph2020empirical-e352]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e352)
[^ralph2020empirical-e353]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e353)
[^ralph2020empirical-e354]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e354)
[^ralph2020empirical-e355]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e355)
[^ralph2020empirical-e356]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e356)
[^ralph2020empirical-e357]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e357)
[^ralph2020empirical-e358]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e358)
[^ralph2020empirical-e359]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e359)
[^ralph2020empirical-e360]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e360)
[^ralph2020empirical-e361]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e361)
[^ralph2020empirical-e362]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e362)
[^ralph2020empirical-e363]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e363)
[^ralph2020empirical-e364]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e364)
[^ralph2020empirical-e365]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e365)
[^ralph2020empirical-e366]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Practicality. [Evidence](../../sources/notes/ralph2020empirical.md#e366)
[^ralph2020empirical-e367]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e367)
[^ralph2020empirical-e368]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e368)
[^ralph2020empirical-e369]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e369)
[^ralph2020empirical-e186]: SIGSOFT Ethics (Studies with Human Participants) Supplement, footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e186)
[^ralph2020empirical-e370]: SIGSOFT Glossary, Gatekeeper. [Evidence](../../sources/notes/ralph2020empirical.md#e370)
[^ralph2020empirical-e253]: SIGSOFT Ethics (Studies with Human Participants) Supplement, footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e253)
[^ralph2020empirical-e371]: SIGSOFT Sampling Supplement, Antipatterns and Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e371)
[^ralph2020empirical-e372]: SIGSOFT Sampling Supplement, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e372)
[^ralph2020empirical-e373]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e373)
[^baltes2022sampling-e23]: Baltes & Ralph 2022, §2.1.2. [Evidence](../../sources/notes/baltes2022sampling.md#e23)
[^baltes2022sampling-e24]: Baltes & Ralph 2022, §2.1.2. [Evidence](../../sources/notes/baltes2022sampling.md#e24)
[^baltes2022sampling-e25]: Baltes & Ralph 2022, §2.4. [Evidence](../../sources/notes/baltes2022sampling.md#e25)
[^baltes2022sampling-e26]: Baltes & Ralph 2022, §2.4. [Evidence](../../sources/notes/baltes2022sampling.md#e26)
[^baltes2022sampling-e7]: Baltes & Ralph 2022, §6. [Evidence](../../sources/notes/baltes2022sampling.md#e7)
[^braun2006using-e1]: Braun & Clarke 2006, What is thematic analysis? [Evidence](../../sources/notes/braun2006using.md#e1)
[^braun2006using-e2]: Braun & Clarke 2006, Inductive vs theoretical thematic analysis. [Evidence](../../sources/notes/braun2006using.md#e2)
[^braun2006using-e3]: Braun & Clarke 2006, Inductive vs theoretical thematic analysis. [Evidence](../../sources/notes/braun2006using.md#e3)
[^braun2006using-e4]: Braun & Clarke 2006, What counts as a theme? [Evidence](../../sources/notes/braun2006using.md#e4)
[^braun2006using-e5]: Braun & Clarke 2006, Phase 1, Transcription of verbal data. [Evidence](../../sources/notes/braun2006using.md#e5)
[^braun2006using-e6]: Braun & Clarke 2006, Phase 1, Transcription of verbal data. [Evidence](../../sources/notes/braun2006using.md#e6)
[^braun2006using-e7]: Braun & Clarke 2006, Phase 1. [Evidence](../../sources/notes/braun2006using.md#e7)
[^braun2006using-e8]: Braun & Clarke 2006, Table 1. [Evidence](../../sources/notes/braun2006using.md#e8)
[^braun2006using-e9]: Braun & Clarke 2006, Phase 2. [Evidence](../../sources/notes/braun2006using.md#e9)
[^braun2006using-e10]: Braun & Clarke 2006, Phase 2. [Evidence](../../sources/notes/braun2006using.md#e10)
[^braun2006using-e11]: Braun & Clarke 2006, Phase 4. [Evidence](../../sources/notes/braun2006using.md#e11)
[^braun2006using-e12]: Braun & Clarke 2006, Phase 5. [Evidence](../../sources/notes/braun2006using.md#e12)
[^braun2006using-e13]: Braun & Clarke 2006, Phase 6. [Evidence](../../sources/notes/braun2006using.md#e13)
[^braun2006using-e14]: Braun & Clarke 2006, Potential pitfalls. [Evidence](../../sources/notes/braun2006using.md#e14)
[^braun2006using-e15]: Braun & Clarke 2006, Potential pitfalls. [Evidence](../../sources/notes/braun2006using.md#e15)
[^braun2006using-e16]: Braun & Clarke 2006, Potential pitfalls. [Evidence](../../sources/notes/braun2006using.md#e16)
[^braun2006using-e17]: Braun & Clarke 2006, Potential pitfalls. [Evidence](../../sources/notes/braun2006using.md#e17)
[^braun2006using-e18]: Braun & Clarke 2006, What is thematic analysis? [Evidence](../../sources/notes/braun2006using.md#e18)
[^braun2006using-e19]: Braun & Clarke 2006, What makes good thematic analysis? [Evidence](../../sources/notes/braun2006using.md#e19)
[^kallio2016systematic-e1]: Kallio et al. 2016, Results. [Evidence](../../sources/notes/kallio2016systematic.md#e1)
[^kallio2016systematic-e2]: Kallio et al. 2016, Results. [Evidence](../../sources/notes/kallio2016systematic.md#e2)
[^kallio2016systematic-e3]: Kallio et al. 2016, Results. [Evidence](../../sources/notes/kallio2016systematic.md#e3)
[^kallio2016systematic-e4]: Kallio et al. 2016, Results. [Evidence](../../sources/notes/kallio2016systematic.md#e4)
[^kallio2016systematic-e5]: Kallio et al. 2016, Results, Pilot testing. [Evidence](../../sources/notes/kallio2016systematic.md#e5)
[^kallio2016systematic-e6]: Kallio et al. 2016, Results, Pilot testing. [Evidence](../../sources/notes/kallio2016systematic.md#e6)
[^kallio2016systematic-e7]: Kallio et al. 2016, Discussion. [Evidence](../../sources/notes/kallio2016systematic.md#e7)
[^mcdonald2019reliability-e1]: McDonald et al. 2019, §1, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e1)
[^mcdonald2019reliability-e2]: McDonald et al. 2019, Abstract. [Evidence](../../sources/notes/mcdonald2019reliability.md#e2)
[^mcdonald2019reliability-e3]: McDonald et al. 2019, §4.3. [Evidence](../../sources/notes/mcdonald2019reliability.md#e3)
[^mcdonald2019reliability-e4]: McDonald et al. 2019, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e4)
[^mcdonald2019reliability-e5]: McDonald et al. 2019, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e5)
[^mcdonald2019reliability-e6]: McDonald et al. 2019, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e6)
[^mcdonald2019reliability-e7]: McDonald et al. 2019, §2.3. [Evidence](../../sources/notes/mcdonald2019reliability.md#e7)
[^mcdonald2019reliability-e8]: McDonald et al. 2019, §2.3. [Evidence](../../sources/notes/mcdonald2019reliability.md#e8)
[^mcdonald2019reliability-e9]: McDonald et al. 2019, §2.3. [Evidence](../../sources/notes/mcdonald2019reliability.md#e9)
[^mcdonald2019reliability-e10]: McDonald et al. 2019, §1. [Evidence](../../sources/notes/mcdonald2019reliability.md#e10)
[^mcdonald2019reliability-e11]: McDonald et al. 2019, §1. [Evidence](../../sources/notes/mcdonald2019reliability.md#e11)
[^mcdonald2019reliability-e12]: McDonald et al. 2019, §5.3.4. [Evidence](../../sources/notes/mcdonald2019reliability.md#e12)
[^mcdonald2019reliability-e13]: McDonald et al. 2019, §5.1.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e13)
[^mcdonald2019reliability-e14]: McDonald et al. 2019, §5.2.3. [Evidence](../../sources/notes/mcdonald2019reliability.md#e14)
[^mcdonald2019reliability-e15]: McDonald et al. 2019, §5.3.6. [Evidence](../../sources/notes/mcdonald2019reliability.md#e15)
[^mcdonald2019reliability-e16]: McDonald et al. 2019, §5.4.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e16)
[^runeson2009guidelines-e6]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e6)
[^runeson2009guidelines-e7]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e7)
[^runeson2009guidelines-e8]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e8)
[^runeson2009guidelines-e9]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e9)
[^runeson2009guidelines-e10]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e10)
[^runeson2009guidelines-e11]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e11)
[^runeson2009guidelines-e12]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e12)
[^runeson2009guidelines-e13]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e13)
[^runeson2009guidelines-e14]: Runeson & Höst 2009, §4.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e14)
[^runeson2009guidelines-e15]: Runeson & Höst 2009, §5.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e15)
[^runeson2009guidelines-e16]: Runeson & Höst 2009, §5.2. [Evidence](../../sources/notes/runeson2009guidelines.md#e16)
[^runeson2009guidelines-e17]: Runeson & Höst 2009, §5.2.1. [Evidence](../../sources/notes/runeson2009guidelines.md#e17)
[^runeson2009guidelines-e18]: Runeson & Höst 2009, §3.3. [Evidence](../../sources/notes/runeson2009guidelines.md#e18)
[^runeson2009guidelines-e47]: Runeson & Höst 2009, §4.2, p. 147. [Evidence](../../sources/notes/runeson2009guidelines.md#e47)
