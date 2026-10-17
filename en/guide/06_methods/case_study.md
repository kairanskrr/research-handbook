# Case study and ethnography: studying a few cases in depth in their real setting

This page covers the **case study** and **ethnography**: going into a company, a team, or an open-source community and using several kinds of evidence (interviews, observation, documents) to understand in depth how something happens there and why. For example, you might follow one team in a company for a few weeks to see how they do code review.

If you want to pull data in bulk from many code repositories and analyze it statistically, see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md). If you have built a new tool and want to "demonstrate it on an example", that belongs to the evaluation step of [Engineering research](../07_fields/computer-science/practices/engineering_research.md), not to the case study this page describes.

**Scope** `[Our analysis]`: the standards and examples on this page come mainly from software engineering. They draw on the ACM SIGSOFT Empirical Standards (the empirical research standards of the Association for Computing Machinery's Special Interest Group on Software Engineering; "the SIGSOFT standard" below), Runeson and Höst's case study guidelines, Easterbrook et al.'s guide to choosing methods, Wohlin's discussion of how to define a case study, and Sharp et al.'s article on ethnography in software engineering. If you do case studies in another field, check that field's conventions first. For how political science uses a small number of cases to test causal mechanisms, see [Process tracing and comparative case studies](process_tracing.md).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md), [Causal explanation](../05_research-strategies/explain_causality.md).

**After reading this page, you should be able to:**

- tell a real case study from something that has only borrowed the name;
- design and carry out a case study step by step: define the case and unit of analysis, gain access to the organization, write a protocol, collect data, analyze, and report;
- explain how ethnography differs from an ordinary case study;
- answer objections like "you only have one case, so you can't generalize".

---

## 1. What this kind of research is and when to use it

**Definition.** A case study is an empirical study that investigates a contemporary phenomenon (the "case") in depth in its real-world context, especially when the boundary between phenomenon and context is unclear[^ralph2020empirical-e414]. The "site" can be a community, an organization, a team, a person, a process, or an internet platform[^ralph2020empirical-e415]. Its conclusions do not rest on statistical significance; they are supported by linking several kinds of evidence, such as numbers, statements from interviews, and documents[^runeson2009guidelines-e23]. Most of the sources for this page come from software engineering. Elsewhere in computing, the human-computer interaction (HCI) and computer-supported cooperative work (CSCW) communities also use ethnography to study workplaces and inform the design of applications[^sharp2016role-e1].

**What it is not.** The term "case study" is badly overused. None of the following count:

- **A demonstration example.** In the software engineering literature, "case study" is often used to mean an example used for demonstration, which is entirely different from the case study as an empirical method[^easterbrook2008selecting-e10]. A study done on a toy program has no real-world context and is not a case study[^runeson2009guidelines-e28]. The SIGSOFT standard requires the site to be real, not a toy example or a fictional scenario[^ralph2020empirical-e419].
- **An experience report.** Writing "our team used method X, and here is what we learned" is an experience report; doing a shallow inquiry at many sites is not a case study either[^ralph2020empirical-e416].
- **Interviewing a few people.** Interviewing more than one person does not by itself make a study a case study[^wohlin2021case-e6].

The misuse is widespread. Wohlin checked a set of software engineering journal papers that called themselves "case studies" and found that close to half did not qualify under the definition[^wohlin2021case-e1]. Typical examples were small-scale evaluations or demonstrations (in a lab, for instance) and analyses of existing information such as open-source repositories or defect databases[^wohlin2021case-e3]. So **state in your paper which definition you are using**[^wohlin2021case-e7].

**How it differs from related methods** `[Our analysis, based on the sources below]`:

| | Case study | Experiment | Survey | Action research |
|---|---|---|---|---|
| Researcher's role | Observes only, does not actively change the site[^runeson2009guidelines-e20] | Manipulates variables | Collects standardized information | Takes part in and drives change[^runeson2009guidelines-e20] |
| How subjects are chosen | Purposefully selected[^runeson2009guidelines-e29] | Random assignment | Sampled from a population | An organization that needs improvement |
| Typical question | "How and why does this happen here?"[^easterbrook2008selecting-e12] | "Does A cause B?" | "How common is it?" | "Does this change help?" |
| Strengths and costs | High realism, low control[^runeson2009guidelines-e22] | High control, low realism | Good representativeness, limited depth | Can bring about change, hard to stay objective |

**When to use it:**

- Your question is "how" or "why"[^easterbrook2008selecting-e12], and the context itself affects the phenomenon (for example, the pressure of a real project changes how developers behave), or the effects take a long time to show[^easterbrook2008selecting-e16].
- You want to know what actually happens, not what people say they do. Observation is especially suitable when you suspect a gap between the "official version" and reality[^runeson2009guidelines-e48].
- You are willing to trade representativeness for depth[^easterbrook2008selecting-e19]. To answer "how common", use a survey or repository mining; to answer "does it cause", use an experiment. `[Our analysis]`

> **Where sources disagree: does analyzing only historical data count as a case study?**
>
> - **Yes, as a historical case study**: among the types of case study the SIGSOFT standard lists is a "historical" type, which uses archival data such as software repositories[^ralph2020empirical-e431].
> - **No**: Wohlin argues that studying only historical information (existing data or software) does not fit the definition of a case study[^wohlin2021case-e2], and that such studies should be called "archival analysis"[^wohlin2021case-e3]. He also argues that when the researcher takes part in the case, it should be called action research (see [Action research](action_research.md))[^wohlin2021case-e4].
>
> In practice: if you analyze only the repository data of a few projects, do not just write "case study"; say which definition you are using and where the data came from[^wohlin2021case-e7]. If you can add interviews or observation, the study will also better meet the expectation of triangulating multiple sources. `[Our analysis]`

---

## 2. How to do it

Case study design is flexible: you can adjust it as you collect data. But **the objective must be fixed from the start**; if the objective changes, it is a new study[^runeson2009guidelines-e25]. Flexible does not mean unplanned.

### Step 1: State the objective and research questions

First write a "how" or "why" research question, then derive study propositions from it (what you expect the study to show), and use the propositions to guide case selection and data collection[^easterbrook2008selecting-e12]. Your plan should at least cover: the objective, the case, the theory (frame of reference), the research questions, the data collection methods, and the selection strategy[^runeson2009guidelines-e27]. **Where people go wrong:** having only a vague interest ("I want to see how this company does testing") and no question. You end up recording everything and showing nothing. `[Our analysis]`

### Step 2: Define the case and the unit of analysis

The **case** is the object of study, such as a project; it contains one or more **units of analysis**, such as subprojects[^runeson2009guidelines-e26]. A unit of analysis can be a company, a project, a team, an individual developer, an event, or a work artifact[^easterbrook2008selecting-e15]. Studying the case as a whole is a holistic design; studying several units of analysis within one case is an embedded design[^runeson2009guidelines-e28]. **Why it matters**: the unit of analysis determines which phenomenon the study focuses on[^easterbrook2008selecting-e15]. With "developer" as the unit you see individual habits; with "team" as the unit you see practices the team shares.

### Step 3: Select cases purposefully, and say why

Cases are selected deliberately, not sampled from a population as in surveys and experiments[^runeson2009guidelines-e29]. Common ways to choose[^runeson2009guidelines-e30][^easterbrook2008selecting-e13]: a **typical case**, to understand the usual situation; a **critical case**, to test a well-established theory, where if the theory holds here it probably holds in many other places; a **unique case**, which is unusual in some respect; and a **revelatory case**, to study a phenomenon that was previously unknown or unstudied[^ralph2020empirical-e431]. One case is sometimes enough, but multiple-case designs usually have higher validity. Treat several cases as **replications**, not as members of a sample[^easterbrook2008selecting-e14].

**Where people go wrong:** in practice, many cases are chosen because they "happened to be available"[^runeson2009guidelines-e30]. That is nothing to be ashamed of, but say so honestly, and argue why the case is still suitable for answering your question. Justifying the selection is an essential attribute in the SIGSOFT standard[^ralph2020empirical-e419].

### Step 4: Gain access, and agree on confidentiality and publication in advance

In case studies done with companies, the hard part may not be the method but **whether you can get in, and whether you can publish**.

- **Allow time to build the relationship.** The organization may want to get to know you for a while before it will share concrete project data[^easterbrook2008selecting-e25]. In exchange for access, researchers usually have to give up some control[^easterbrook2008selecting-e26].
- **Put it in the agreement from the start**: which information is confidential and who approves what gets published[^runeson2009guidelines-e34][^runeson2009guidelines-e36]. Companies may not know academic publishing practice, so tell them explicitly[^runeson2009guidelines-e37]. If this is not settled, publication may be delayed[^easterbrook2008selecting-e26]. There can be compromises: in one of Runeson and Höst's examples, the company would not allow the raw number of defects to be published but did allow the percentages per phase, which was enough for the research purpose[^runeson2009guidelines-e42].
- **Discuss "bad results" in advance.** The results may expose weaknesses in the company's practice; make this possibility clear beforehand[^runeson2009guidelines-e39].
- **Protect the employees, not just the company.** Employees can be harmed if their opinions are passed on to their managers[^runeson2009guidelines-e36]. When management arranges for employees to take part, management is the "gatekeeper": it controls whom you can reach and may also decide whose voices are heard[^ralph2020empirical-e438]. For ways to reduce this power imbalance, see "Watch for power relations" in [Interview studies](interview_study.md#step-3-conduct-the-interviews).

For general requirements on informed consent, ethics review, and privacy, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); SIGSOFT's supplementary ethics standard explicitly applies to case studies[^ralph2020empirical-e439]. When you collect data indirectly (for example, by automatically logging tool use), you still cannot skip getting consent[^runeson2009guidelines-e35].

### Step 5: Write a case study protocol

A **case study protocol** records design decisions and field procedures, and is a living document that is updated as the plan changes[^runeson2009guidelines-e31]. **Why write one**: it guides data collection so planned data are not missed; peers can review it and comment; and it serves as a research log, recording every change and the reason for it, which you will use when you write the report. Keep the protocol under version control[^runeson2009guidelines-e32]. Because the protocol contains confidential information, it usually cannot be published in full, but parts such as the interview guide can be[^runeson2009guidelines-e33]. Publishing the protocol in advance is an extraordinary attribute in the SIGSOFT standard[^ralph2020empirical-e428].

### Step 6: Collect data from several sources and cross-check them

**The most important rule: do not rely on one kind of data.** Using interviews only, with no corroboration, is an antipattern listed in the SIGSOFT standard[^ralph2020empirical-e432]. The reason is that interviewees tend to say what the interviewer wants to hear, give rationalized accounts, and remember selectively[^sharp2016role-e2]. A conclusion is stronger when several sources point to it; this is called **triangulation**[^runeson2009guidelines-e43]. You can triangulate at several levels[^runeson2009guidelines-e44]: **data sources** (beyond interviews, look at meetings, documents, defect records, code review records), **observers** (two or more researchers), and **theory** (interpreting through different theoretical lenses).

Common data sources:

- **Interviews**: case studies often use semi-structured interviews[^runeson2009guidelines-e46]. For choosing interviewees, designing the interview guide, and judging saturation, see [Interview studies](interview_study.md).
- **Observation**: in direct observation you watch without taking part; in participant observation you join in what the participants are doing[^ralph2020empirical-e424]. Checking interviewees' accounts against observation or archival records is a desirable attribute in the SIGSOFT standard[^ralph2020empirical-e423].
- **Existing work artifacts**: documents, defect reports, time logs, and so on. They were recorded for other purposes, so their quality and completeness may not meet research needs[^runeson2009guidelines-e45].

### Step 7: Keep a chain of evidence during analysis

A **chain of evidence** means a reader can follow the path from the data you collected all the way to your conclusions[^runeson2009guidelines-e50]. It is an essential attribute in the SIGSOFT standard[^ralph2020empirical-e421]. How:

- **Analyze while you collect.** New findings will come up during analysis and require further data collection and updates to the interview guide[^runeson2009guidelines-e15].
- **Coding**: attach labels representing a theme or concept to pieces of text[^runeson2009guidelines-e52]. Analysis based purely on intuition, with no structure, makes it hard to present a clear chain of evidence[^runeson2009guidelines-e55]. For how to code in practice (inductive or deductive, codebooks, whether to compute agreement), see [Interview studies](interview_study.md#step-5-coding-and-thematic-analysis).
- **Leave a trail**: record every decision made during analysis, keep every version of instruments such as the interview guide, and note the links between data, codes, and memos[^runeson2009guidelines-e54]. One practice worth borrowing: number every statement in the transcripts and have two researchers classify them[^runeson2009guidelines-e53].
- **Look actively for counterexamples.** Negative case analysis means actively searching for alternative explanations that could overturn your hypothesis[^runeson2009guidelines-e51]. Having several people analyze reduces individual bias[^runeson2009guidelines-e16].
- **Do not make a messy reality look tidy.** Presenting a complex, messy phenomenon as overly simple and overly rational is an antipattern[^ralph2020empirical-e432].

### Step 8: Generalize analytically, not statistically

"You only have one case, so how can you generalize?" In the software engineering methods literature this objection does not hold: case studies never aimed at statistical generalization. They aim at **analytical generalization**: extending the results to other cases with shared characteristics, that is, building theory[^runeson2009guidelines-e56]. The SIGSOFT standard explicitly lists "sample of one; findings not generalizable" as an invalid criticism: the purpose of a case study is to study one object in depth, and it should produce concepts that are transferable in principle[^ralph2020empirical-e433]. Sharp et al. quote a metaphor: one swallow does not make a summer, but one swallow is enough to prove that swallows exist, and careful dissection of one swallow can yield a great deal of reliable knowledge about swallow anatomy[^sharp2016role-e13].

**How:** describe the site in detail[^ralph2020empirical-e419] so readers can judge whether your conclusions carry over to their own situation (transferability[^ralph2020empirical-e436]), and connect your conclusions to existing theory `[Our analysis]`. In confirmatory case studies, evidence builds up through later cases[^easterbrook2008selecting-e18].

### Step 9: Report

- **Describe the site in detail**, while protecting identities. "A large Swedish telecom company" practically names Ericsson[^runeson2009guidelines-e60]. Removing the names of the company and people is not always enough: subjects from a very small population may be recognized by their characteristics[^runeson2009guidelines-e38]. Internal characteristics (the size of the unit, the average age of staff, and so on) may be more useful than external ones such as industry or revenue[^runeson2009guidelines-e61].
- **Write the history of the research process**: who did what and when, not just one sentence saying "we did a case study using semi-structured interviews"[^runeson2009guidelines-e63]. If the research questions changed substantially along the way, say so[^runeson2009guidelines-e62].
- **Give excerpts of the data**, such as quotations and anonymized narratives, so readers can check your conclusions[^runeson2009guidelines-e64]. But quotations only illustrate conclusions and cannot replace them; state each conclusion clearly on its own, independent of the quotations[^ralph2020empirical-e426].

---

## 3. How ethnography is different

The goal of ethnography is to understand how members of a group make sense of their own social interactions[^easterbrook2008selecting-e20]. It has four main features[^sharp2016role-e3]:

1. **The members' point of view**: what matters to them and what frustrates them, not what the researcher thinks matters[^sharp2016role-e4].
2. **Attention to everyday detail**. The data collection plan should be flexible, but flexible does not mean lacking rigor. The researcher enters the field with an open mind, not an empty head[^sharp2016role-e8].
3. **An analytical stance**. An ethnographer is not a journalist who just reports what they saw and heard[^sharp2016role-e9]; they explain "why": what frustrates people, what blocks progress, what makes a team work well[^sharp2016role-e11].
4. **Thick description**: rich, detailed description that lets the conclusions stand up to academic scrutiny[^sharp2016role-e3]. Its results support analytical generalization, not statistical generalization[^sharp2016role-e12].

**What participant observation looks like in software development.** Companies are often reluctant to let outsiders access their code repositories, so participant observation usually means taking a meaningful role in the team, such as taking on documentation work or helping the project with administrative support[^sharp2016role-e15][^sharp2016role-e16]. Observation almost always has to be complemented by interviews and document analysis[^sharp2016role-e14]. When you study open-source or geographically distributed teams, the online environment is also a field site[^sharp2016role-e18].

**Field notes.** Observation has to leave a record. For example, Sharp and Robinson spent a week with an Extreme Programming team, and their data included field notes, meeting recordings, photographs, and copies of work artifacts[^runeson2009guidelines-e49]; you can also supplement observation notes with interviews[^easterbrook2008selecting-e21]. Practical advice `[Our analysis]`: write up your notes the same day, and keep "what I saw" separate from "how I interpret it", marking the latter as memos, so your chain of evidence can distinguish data from interpretation.

**The pros and cons of being an insider.** A researcher who knows software development can better understand practitioners' discussions and thinking[^sharp2016role-e25]. But it is also easy to take things for granted and judge others, and practitioners may expect you to give them guidance[^sharp2016role-e24][^sharp2016role-e19]. So be open about your research interests and intentions, and consider how the research will affect the team you observe[^sharp2016role-e20].

**Questions it suits and questions it does not.** Ethnography suits questions about cooperation and social and human factors[^sharp2016role-e21], such as "how does the team actually develop software with Extreme Programming?" rather than "is pair programming more efficient?"[^sharp2016role-e22]. It depends on existing practice, so it cannot help with tools or methods that would change practice radically[^sharp2016role-e23].

> **Where sources disagree: how long does ethnography take, and is it a kind of case study?**
>
> - **A few weeks can be enough, and it is a kind of case study**: Sharp et al. argue that a few weeks usually produces good results, and that "it must take a long time" is a common misconception[^sharp2016role-e5]; their example lasted three weeks, one of them full-time observation[^sharp2016role-e6]. The SIGSOFT standard classifies ethnography under case studies[^ralph2020empirical-e417], and Runeson and Höst also see it as a special type of case study[^runeson2009guidelines-e21].
> - **It may take much longer, and it is a different method**: Easterbrook et al. argue that participant observation requires the researcher to be accepted by the group as one of its own, which may take far longer than "a few weeks"[^easterbrook2008selecting-e22]; ethnography does not set out to prove hypotheses but to build local theory, and this stance sets it apart from the case study[^easterbrook2008selecting-e23].
>
> In practice: set the duration by your research question and the team's working rhythm. Sharp et al.'s example was planned around the team's three-week iterations[^sharp2016role-e6]. You do not have to be on site full-time; visiting on fewer days and starting analysis partway through is fine[^sharp2016role-e17]. In the paper, say how long you observed and in what role you took part. `[Our analysis]`

---

## 4. Validity: which standards to judge it by

For the general idea of validity, see [Validity and limitations](../02_do-the-project/04_validity-and-limits.md); for quality criteria in qualitative research (credibility, transferability, and so on), see [Interview studies](interview_study.md#first-remember-qualitative-research-has-different-quality-criteria-from-quantitative-research). For case studies, keep two things in mind. **First, consider validity from the design stage**; waiting until analysis is too late[^runeson2009guidelines-e2]. The main weakness of the case study is that it is more exposed to researcher bias[^easterbrook2008selecting-e17]. Several common practices[^runeson2009guidelines-e59][^easterbrook2008selecting-e27]: triangulation; keeping a detailed protocol; having peers review the design; having the people studied review the data and conclusions (member checking); spending enough time in the field; and reporting information that contradicts the main conclusions. **Second, use the right standards**; see the disagreement below.

> **Where sources disagree: quantitative validity terms or qualitative ones?**
>
> - **Keep the four kinds of validity**: Runeson and Höst know that some argue for a separate set of criteria for flexible-design research (credibility, transferability, and so on), but they choose to keep the established terms and reinterpret them for flexible designs[^runeson2009guidelines-e65]: construct validity, internal validity, external validity, and reliability[^runeson2009guidelines-e3][^runeson2009guidelines-e57][^runeson2009guidelines-e5][^runeson2009guidelines-e58].
> - **Switch to qualitative criteria**: the SIGSOFT standard holds that case studies should be judged by qualitative criteria such as credibility, multivocality, reflexivity, rigor, and transferability; replicability, generalizability, and objectivity generally do not apply[^ralph2020empirical-e429].
>
> The two overlap: both ask you to say where bias may come from and how far your conclusions reach. In practice: choose the terminology your target community uses, and say in the paper which set you are using. `[Our analysis]` One point both sides agree on: **internal validity only needs discussing when you study causal relationships**[^runeson2009guidelines-e57][^ralph2020empirical-e434].

---

## 5. Checklist

The list below is based mainly on the Case Study and Ethnography standard in the SIGSOFT Empirical Standards, which serves as a review standard in software engineering; in other fields, follow your own field's conventions `[Our analysis]`.

**Essential**

- [ ] Justify why you chose this case or these cases or sites[^ralph2020empirical-e419]
- [ ] Describe the site in detail; the site is real, not a toy example or fictional scenario[^ralph2020empirical-e419]
- [ ] State which type of case study it is (exploratory, explanatory, descriptive, and so on)[^ralph2020empirical-e420]
- [ ] Describe the data sources, such as participants' backgrounds and job roles; define the unit of analysis[^ralph2020empirical-e420]
- [ ] There is a clear chain of evidence from observations to conclusions[^ralph2020empirical-e421]

**Desirable**

- [ ] Triangulate across data sources, informants, or researchers; check interviewees' accounts against observation or archival records[^ralph2020empirical-e423]; use observation and integrate what you observed into your conclusions[^ralph2020empirical-e424]
- [ ] Describe external events that may have affected the case; explain how your prior understanding influenced the study; reflect on your own biases[^ralph2020empirical-e425][^ralph2020empirical-e427]
- [ ] Use quotations to illustrate conclusions, but make sure each conclusion stands without them[^ralph2020empirical-e426]
- [ ] Provide supplementary materials such as the interview guide, coding scheme, and coding examples[^ralph2020empirical-e422]

**Extraordinary**

- [ ] Several in-depth cases, with cross-case triangulation[^ralph2020empirical-e428]
- [ ] Team analysis, such as coding by several people with an analysis of agreement[^ralph2020empirical-e428]
- [ ] Publish the case study protocol in advance[^ralph2020empirical-e428]

**Common reviewer criticisms that are not valid** (as listed by the SIGSOFT standard, for software engineering submissions): you do not need to worry about these

- "There is no quantitative data"[^ralph2020empirical-e434]
- "Sample of one; findings not generalizable"[^ralph2020empirical-e433]
- "It lacks internal validity" (unless you are trying to establish causation)[^ralph2020empirical-e434]
- "It is not reproducible because the data are not public" (qualitative data are often confidential)[^ralph2020empirical-e435]
- "Not enough interviews, or interviews too short": there is no magic number; what matters is that the data are enough to make the conclusions credible[^ralph2020empirical-e435]

---

## 6. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Calling a demonstration example a "case study" | There is no real-world context, so it does not fit the definition[^easterbrook2008selecting-e10][^runeson2009guidelines-e28] |
| Doing interviews only, with no other sources to corroborate them | Interviewees rationalize and remember selectively[^sharp2016role-e2][^ralph2020empirical-e432] |
| Choosing a case because it "happened to be available" without saying so | Readers cannot judge whether the case suits the question[^runeson2009guidelines-e30][^ralph2020empirical-e419] |
| Not agreeing on confidentiality and publication before entering the site | Publication is later blocked or delayed[^runeson2009guidelines-e34][^easterbrook2008selecting-e26] |
| Assuming that removing the company name makes it anonymous | It may be recognized by its characteristics[^runeson2009guidelines-e38][^runeson2009guidelines-e60] |
| Writing only the conclusions, not the path from data to conclusions | There is no chain of evidence, so readers cannot check it[^ralph2020empirical-e421][^runeson2009guidelines-e50] |
| Dismissing your own work because "the sample is small", or forcing a statistical generalization | Case studies aim at analytical generalization[^runeson2009guidelines-e56][^ralph2020empirical-e433] |
| Ethnography that only describes what was seen, with no analysis | Ethnography is not just description; it must also explain "why"[^sharp2016role-e10] |

---

## 7. Further reading

- **A complete guide to case studies**: Runeson and Höst 2009, with practices and checklists for each stage (design, data collection, analysis, reporting), plus three real cases.
- **Choosing a method**: Easterbrook et al. 2008, comparing which questions experiments, case studies, surveys, ethnography, and action research are each suited to.
- **An introduction to ethnography**: Sharp, Dittrich, and de Souza 2016, on the four features of ethnography and five dimensions of research design, with eight examples of ethnography in software engineering.
- **What really counts as a case study**: Wohlin 2021, very short; good to check against before you start writing.
- **The standard itself**: the Case Study and Ethnography section of the SIGSOFT Empirical Standards; first among its suggested readings is Yin's book on case study research[^ralph2020empirical-e440].

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e414]: SIGSOFT Case Study and Ethnography standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e414)
[^ralph2020empirical-e415]: SIGSOFT Case Study and Ethnography standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e415)
[^ralph2020empirical-e416]: SIGSOFT Case Study and Ethnography standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e416)
[^ralph2020empirical-e417]: SIGSOFT Case Study and Ethnography standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e417)
[^ralph2020empirical-e419]: SIGSOFT Case Study and Ethnography standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e419)
[^ralph2020empirical-e420]: SIGSOFT Case Study and Ethnography standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e420)
[^ralph2020empirical-e421]: SIGSOFT Case Study and Ethnography standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e421)
[^ralph2020empirical-e422]: SIGSOFT Case Study and Ethnography standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e422)
[^ralph2020empirical-e423]: SIGSOFT Case Study and Ethnography standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e423)
[^ralph2020empirical-e424]: SIGSOFT Case Study and Ethnography standard, Desirable Attributes and footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e424)
[^ralph2020empirical-e425]: SIGSOFT Case Study and Ethnography standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e425)
[^ralph2020empirical-e426]: SIGSOFT Case Study and Ethnography standard, Desirable Attributes and footnote 4. [Evidence](../../sources/notes/ralph2020empirical.md#e426)
[^ralph2020empirical-e427]: SIGSOFT Case Study and Ethnography standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e427)
[^ralph2020empirical-e428]: SIGSOFT Case Study and Ethnography standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e428)
[^ralph2020empirical-e429]: SIGSOFT Case Study and Ethnography standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e429)
[^ralph2020empirical-e431]: SIGSOFT Case Study and Ethnography standard, Types of Case Studies. [Evidence](../../sources/notes/ralph2020empirical.md#e431)
[^ralph2020empirical-e432]: SIGSOFT Case Study and Ethnography standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e432)
[^ralph2020empirical-e433]: SIGSOFT Case Study and Ethnography standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e433)
[^ralph2020empirical-e434]: SIGSOFT Case Study and Ethnography standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e434)
[^ralph2020empirical-e435]: SIGSOFT Case Study and Ethnography standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e435)
[^ralph2020empirical-e436]: SIGSOFT Glossary, Credibility / Transferability / Reflexivity. [Evidence](../../sources/notes/ralph2020empirical.md#e436)
[^ralph2020empirical-e438]: SIGSOFT Glossary, Gatekeeper. [Evidence](../../sources/notes/ralph2020empirical.md#e438)
[^ralph2020empirical-e439]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e439)
[^ralph2020empirical-e440]: SIGSOFT Case Study and Ethnography standard, Suggested Readings. [Evidence](../../sources/notes/ralph2020empirical.md#e440)
[^runeson2009guidelines-e2]: Runeson & Höst 2009, §5.2.3, p. 153. [Evidence](../../sources/notes/runeson2009guidelines.md#e2)
[^runeson2009guidelines-e3]: Runeson & Höst 2009, §5.2.3, construct validity. [Evidence](../../sources/notes/runeson2009guidelines.md#e3)
[^runeson2009guidelines-e5]: Runeson & Höst 2009, §5.2.3, external validity. [Evidence](../../sources/notes/runeson2009guidelines.md#e5)
[^runeson2009guidelines-e20]: Runeson & Höst 2009, §2.1, p. 134. [Evidence](../../sources/notes/runeson2009guidelines.md#e20)
[^runeson2009guidelines-e21]: Runeson & Höst 2009, §2.1, p. 134. [Evidence](../../sources/notes/runeson2009guidelines.md#e21)
[^runeson2009guidelines-e22]: Runeson & Höst 2009, §2.2, p. 136. [Evidence](../../sources/notes/runeson2009guidelines.md#e22)
[^runeson2009guidelines-e23]: Runeson & Höst 2009, §2.2, p. 137. [Evidence](../../sources/notes/runeson2009guidelines.md#e23)
[^runeson2009guidelines-e25]: Runeson & Höst 2009, §2.4, p. 138. [Evidence](../../sources/notes/runeson2009guidelines.md#e25)
[^runeson2009guidelines-e26]: Runeson & Höst 2009, §2.5, p. 138. [Evidence](../../sources/notes/runeson2009guidelines.md#e26)
[^runeson2009guidelines-e27]: Runeson & Höst 2009, §3.1, p. 139. [Evidence](../../sources/notes/runeson2009guidelines.md#e27)
[^runeson2009guidelines-e28]: Runeson & Höst 2009, §3.1, p. 139. [Evidence](../../sources/notes/runeson2009guidelines.md#e28)
[^runeson2009guidelines-e29]: Runeson & Höst 2009, §3.1, p. 140. [Evidence](../../sources/notes/runeson2009guidelines.md#e29)
[^runeson2009guidelines-e30]: Runeson & Höst 2009, §3.1, p. 140. [Evidence](../../sources/notes/runeson2009guidelines.md#e30)
[^runeson2009guidelines-e31]: Runeson & Höst 2009, §3.2, p. 141. [Evidence](../../sources/notes/runeson2009guidelines.md#e31)
[^runeson2009guidelines-e32]: Runeson & Höst 2009, §3.2, p. 141. [Evidence](../../sources/notes/runeson2009guidelines.md#e32)
[^runeson2009guidelines-e33]: Runeson & Höst 2009, §3.2, p. 141. [Evidence](../../sources/notes/runeson2009guidelines.md#e33)
[^runeson2009guidelines-e34]: Runeson & Höst 2009, §3.3, p. 142. [Evidence](../../sources/notes/runeson2009guidelines.md#e34)
[^runeson2009guidelines-e35]: Runeson & Höst 2009, §3.3, p. 142. [Evidence](../../sources/notes/runeson2009guidelines.md#e35)
[^runeson2009guidelines-e36]: Runeson & Höst 2009, §3.3, p. 143. [Evidence](../../sources/notes/runeson2009guidelines.md#e36)
[^runeson2009guidelines-e37]: Runeson & Höst 2009, §3.3, p. 143. [Evidence](../../sources/notes/runeson2009guidelines.md#e37)
[^runeson2009guidelines-e38]: Runeson & Höst 2009, §3.3, p. 143. [Evidence](../../sources/notes/runeson2009guidelines.md#e38)
[^runeson2009guidelines-e39]: Runeson & Höst 2009, §3.3, p. 143. [Evidence](../../sources/notes/runeson2009guidelines.md#e39)
[^runeson2009guidelines-e42]: Runeson & Höst 2009, §3.3, pp. 143–144. [Evidence](../../sources/notes/runeson2009guidelines.md#e42)
[^runeson2009guidelines-e43]: Runeson & Höst 2009, §4.1, p. 144. [Evidence](../../sources/notes/runeson2009guidelines.md#e43)
[^runeson2009guidelines-e44]: Runeson & Höst 2009, §2.2, p. 136. [Evidence](../../sources/notes/runeson2009guidelines.md#e44)
[^runeson2009guidelines-e45]: Runeson & Höst 2009, §4.1, p. 145. [Evidence](../../sources/notes/runeson2009guidelines.md#e45)
[^runeson2009guidelines-e46]: Runeson & Höst 2009, §4.2, pp. 146–147. [Evidence](../../sources/notes/runeson2009guidelines.md#e46)
[^runeson2009guidelines-e48]: Runeson & Höst 2009, §4.3, p. 148. [Evidence](../../sources/notes/runeson2009guidelines.md#e48)
[^runeson2009guidelines-e49]: Runeson & Höst 2009, §4.3, p. 148. [Evidence](../../sources/notes/runeson2009guidelines.md#e49)
[^runeson2009guidelines-e50]: Runeson & Höst 2009, §5.1, pp. 150–151. [Evidence](../../sources/notes/runeson2009guidelines.md#e50)
[^runeson2009guidelines-e15]: Runeson & Höst 2009, §5.1, p. 151. [Evidence](../../sources/notes/runeson2009guidelines.md#e15)
[^runeson2009guidelines-e16]: Runeson & Höst 2009, §5.1, p. 151. [Evidence](../../sources/notes/runeson2009guidelines.md#e16)
[^runeson2009guidelines-e51]: Runeson & Höst 2009, §5.2, p. 151. [Evidence](../../sources/notes/runeson2009guidelines.md#e51)
[^runeson2009guidelines-e52]: Runeson & Höst 2009, §5.2, p. 151. [Evidence](../../sources/notes/runeson2009guidelines.md#e52)
[^runeson2009guidelines-e53]: Runeson & Höst 2009, §5.2, p. 152. [Evidence](../../sources/notes/runeson2009guidelines.md#e53)
[^runeson2009guidelines-e54]: Runeson & Höst 2009, §5.2, p. 153. [Evidence](../../sources/notes/runeson2009guidelines.md#e54)
[^runeson2009guidelines-e55]: Runeson & Höst 2009, §5.2, p. 153. [Evidence](../../sources/notes/runeson2009guidelines.md#e55)
[^runeson2009guidelines-e56]: Runeson & Höst 2009, §5.2.3, p. 154. [Evidence](../../sources/notes/runeson2009guidelines.md#e56)
[^runeson2009guidelines-e57]: Runeson & Höst 2009, §5.2.3, p. 154. [Evidence](../../sources/notes/runeson2009guidelines.md#e57)
[^runeson2009guidelines-e58]: Runeson & Höst 2009, §5.2.3, p. 154. [Evidence](../../sources/notes/runeson2009guidelines.md#e58)
[^runeson2009guidelines-e59]: Runeson & Höst 2009, §5.2.3, p. 154. [Evidence](../../sources/notes/runeson2009guidelines.md#e59)
[^runeson2009guidelines-e60]: Runeson & Höst 2009, §6.1, p. 155. [Evidence](../../sources/notes/runeson2009guidelines.md#e60)
[^runeson2009guidelines-e61]: Runeson & Höst 2009, §6.1, p. 155. [Evidence](../../sources/notes/runeson2009guidelines.md#e61)
[^runeson2009guidelines-e62]: Runeson & Höst 2009, §6.1, p. 155. [Evidence](../../sources/notes/runeson2009guidelines.md#e62)
[^runeson2009guidelines-e63]: Runeson & Höst 2009, §6.1, p. 156. [Evidence](../../sources/notes/runeson2009guidelines.md#e63)
[^runeson2009guidelines-e64]: Runeson & Höst 2009, §6.1, p. 156. [Evidence](../../sources/notes/runeson2009guidelines.md#e64)
[^runeson2009guidelines-e65]: Runeson & Höst 2009, §5.2.3, p. 153. [Evidence](../../sources/notes/runeson2009guidelines.md#e65)
[^easterbrook2008selecting-e10]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e10)
[^easterbrook2008selecting-e12]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e12)
[^easterbrook2008selecting-e13]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e13)
[^easterbrook2008selecting-e14]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e14)
[^easterbrook2008selecting-e15]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e15)
[^easterbrook2008selecting-e16]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e16)
[^easterbrook2008selecting-e17]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e17)
[^easterbrook2008selecting-e18]: Easterbrook et al. 2008, §5.2. [Evidence](../../sources/notes/easterbrook2008selecting.md#e18)
[^easterbrook2008selecting-e19]: Easterbrook et al. 2008, §5.3. [Evidence](../../sources/notes/easterbrook2008selecting.md#e19)
[^easterbrook2008selecting-e20]: Easterbrook et al. 2008, §5.4. [Evidence](../../sources/notes/easterbrook2008selecting.md#e20)
[^easterbrook2008selecting-e21]: Easterbrook et al. 2008, §5.4. [Evidence](../../sources/notes/easterbrook2008selecting.md#e21)
[^easterbrook2008selecting-e22]: Easterbrook et al. 2008, §5.4. [Evidence](../../sources/notes/easterbrook2008selecting.md#e22)
[^easterbrook2008selecting-e23]: Easterbrook et al. 2008, §5.4. [Evidence](../../sources/notes/easterbrook2008selecting.md#e23)
[^easterbrook2008selecting-e25]: Easterbrook et al. 2008, Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e25)
[^easterbrook2008selecting-e26]: Easterbrook et al. 2008, Practical Considerations. [Evidence](../../sources/notes/easterbrook2008selecting.md#e26)
[^easterbrook2008selecting-e27]: Easterbrook et al. 2008, §7.0 (paraphrasing Creswell 2002). [Evidence](../../sources/notes/easterbrook2008selecting.md#e27)
[^sharp2016role-e1]: Sharp et al. 2016, §1. [Evidence](../../sources/notes/sharp2016role.md#e1)
[^sharp2016role-e2]: Sharp et al. 2016, §2.1, footnote 1. [Evidence](../../sources/notes/sharp2016role.md#e2)
[^sharp2016role-e3]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e3)
[^sharp2016role-e4]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e4)
[^sharp2016role-e5]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e5)
[^sharp2016role-e6]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e6)
[^sharp2016role-e8]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e8)
[^sharp2016role-e9]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e9)
[^sharp2016role-e10]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e10)
[^sharp2016role-e11]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e11)
[^sharp2016role-e12]: Sharp et al. 2016, §2.3. [Evidence](../../sources/notes/sharp2016role.md#e12)
[^sharp2016role-e13]: Sharp et al. 2016, §2.3 (citing Anzai & Simon 1979). [Evidence](../../sources/notes/sharp2016role.md#e13)
[^sharp2016role-e14]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e14)
[^sharp2016role-e15]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e15)
[^sharp2016role-e16]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e16)
[^sharp2016role-e17]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e17)
[^sharp2016role-e18]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e18)
[^sharp2016role-e19]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e19)
[^sharp2016role-e20]: Sharp et al. 2016, §2.4. [Evidence](../../sources/notes/sharp2016role.md#e20)
[^sharp2016role-e21]: Sharp et al. 2016, §4.2. [Evidence](../../sources/notes/sharp2016role.md#e21)
[^sharp2016role-e22]: Sharp et al. 2016, §4.2. [Evidence](../../sources/notes/sharp2016role.md#e22)
[^sharp2016role-e23]: Sharp et al. 2016, §4.2. [Evidence](../../sources/notes/sharp2016role.md#e23)
[^sharp2016role-e24]: Sharp et al. 2016, §4.3. [Evidence](../../sources/notes/sharp2016role.md#e24)
[^sharp2016role-e25]: Sharp et al. 2016, §4.3. [Evidence](../../sources/notes/sharp2016role.md#e25)
[^wohlin2021case-e1]: Wohlin 2021, Abstract. [Evidence](../../sources/notes/wohlin2021case.md#e1)
[^wohlin2021case-e2]: Wohlin 2021, §1. [Evidence](../../sources/notes/wohlin2021case.md#e2)
[^wohlin2021case-e3]: Wohlin 2021, §4. [Evidence](../../sources/notes/wohlin2021case.md#e3)
[^wohlin2021case-e4]: Wohlin 2021, §4. [Evidence](../../sources/notes/wohlin2021case.md#e4)
[^wohlin2021case-e6]: Wohlin 2021, §6. [Evidence](../../sources/notes/wohlin2021case.md#e6)
[^wohlin2021case-e7]: Wohlin 2021, §6. [Evidence](../../sources/notes/wohlin2021case.md#e7)
