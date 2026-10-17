# Mixed methods: studying one question with two or more methods

This page covers **mixed methods research** and the broader **multi-method research**: combining two or more methods around the same research question. For example, you might first mine patterns from code repositories and then interview developers to explain them; or first run interviews to form hypotheses and then test them more widely with a questionnaire.

This page covers only how to combine methods. For how to do each component, see the relevant pages: [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md), [Interview studies](interview_study.md), [Questionnaire surveys](questionnaire_survey.md), and so on. For how to choose methods to fit your question and when you need to combine them, see [Choosing a method](../02_do-the-project/02_choose-method.md#4-combine-methods-when-you-need-to).

**Scope** `[Our analysis]`: the standards and examples on this page come mainly from software engineering. They are based on the multi-methodology and mixed methods standard in the ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) empirical standards, on Easterbrook et al.'s guide to selecting research methods, and on Storey et al.'s analysis of research strategies in software engineering. If you do mixed methods research in another field, check your own field's standards first. This handbook does not yet have a methods page on mixed methods for other fields; for political science's practice of combining statistical analysis with within-case process tracing, see [Process tracing and comparative case studies](process_tracing.md).

**Strategies it usually serves**: [Causal explanation](../05_research-strategies/explain_causality.md).

**After reading this page, you should be able to:**

- judge whether your question is worth tackling with several methods, and what it will cost you;
- choose one of the three common designs, and say at what stage each method comes in and what job it does;
- genuinely integrate the results of different methods, rather than writing each up separately;
- recognize common mistakes such as "tacking on a small survey".

---

## 1. What this kind of study is, and when to use it

The ACM SIGSOFT empirical standards distinguish two terms[^ralph2020empirical-e274]:

- **Multi-method research** (multi-methodology): uses two or more approaches to data collection or analysis to corroborate, complement, and expand research findings.
- **Mixed methods research**: combines and integrates inductive research (deriving patterns from the data) with deductive research (using data to test hypotheses fixed in advance), often but not necessarily with qualitative plus quantitative data.

For simplicity, the rest of this page calls both "mixed methods"; the requirements are essentially the same.

**Why combine methods**: every method has known weaknesses, but different methods have different ones; combining several lets the weaknesses of one be covered by another[^easterbrook2008selecting-e1]. Storey et al. compare research strategies in software engineering against four quality criteria: generalizability, realism, control of human factors, and precision of the data. Every strategy has strengths and weaknesses, so it may be necessary to triangulate across strategies (triangulation: using evidence from different sources or methods to cross-check each other)[^storey2020who-e3]. A typical case in software engineering: analyzing only trace data such as commit histories and review comments shows only part of people's behavior, intentions, and interactions[^storey2020who-e1]; studies that aim to describe people and social aspects should corroborate their conclusions with interviews, questionnaires, or observation[^storey2020who-e4]. The same goes for evaluating tools that people use: a tool that recommends likely defects, for example, may need to be evaluated with real users to see how it changes the setting it is used in[^storey2020who-e5].

**Count the cost too**: you collect a lot of data, analyzing data from several sources takes a long time, and the researchers need to be comfortable with both quantitative and qualitative research[^easterbrook2008selecting-e3].

**When you don't need it** `[Our analysis, based on the sources below]`:

- One method is already enough to answer the question. For example, when evaluating a new technique for cutting build times, adding human feedback may not help[^storey2020who-e6].
- The SIGSOFT general standard lists "applies two or more data collection or analysis strategies to the same research question" as an **extraordinary attribute**, not an essential one[^ralph2020empirical-e290]. Methods only need to be appropriate for the study's purpose, not optimal[^ralph2020empirical-e23].

**First, separate three things** that are often confused:

| | What it is | Example `[Our analysis]` |
|---|---|---|
| Several data collection techniques within one method | Collecting data in several ways within one study, which also allows triangulation[^easterbrook2008selecting-e9] | A case study that uses both interviews and documents |
| Data triangulation | The same method applied to different data sources[^storey2020who-e7] | The same mining analysis repeated on five datasets |
| Method triangulation (the subject of this page) | Combining different research strategies[^storey2020who-e7][^ralph2020empirical-e288] | Mining repositories first, then interviewing developers |

The SIGSOFT standard specifically warns you to tell the first row apart from the third[^ralph2020empirical-e288]; Storey et al. also stress that a research method (a data collection technique, such as interviews) and a research strategy (which can include one or more methods) are different things[^storey2020who-e2]. Nor can the second row stand in for the third: repeating an analysis on more datasets may improve generalizability, but it does not improve realism or strengthen control of human factors[^storey2020who-e8].

> **Where sources disagree: should a single paper do its own triangulation?**
> - Storey et al. analyzed a set of software engineering papers and found that the vast majority of data-driven papers did not triangulate with other strategies, and most of those that did added a questionnaire or interviews[^storey2020who-e9]; they call for combining research strategies more often[^storey2020who-e11].
> - But they also acknowledge that the burden of triangulation need not fall on a single paper[^storey2020who-e10]. The SIGSOFT standard likewise lists "the mixed methods approach isn't necessary" as an invalid criticism (provided the approach really is beneficial)[^ralph2020empirical-e287], and lists multiple methods as an extraordinary attribute rather than an essential one[^ralph2020empirical-e290].
>
> In practice `[Our analysis]`: if your conclusions are about why people do what they do, or how well a tool works in real use, a single data analysis will struggle to support them, and it is worth adding another method in the same paper or in immediate follow-up work. If the question itself is technical, don't mix methods for the sake of mixing.

---

## 2. Three common designs

Easterbrook et al. describe three mixed methods designs, which differ in their data collection strategy and in the order of the methods[^easterbrook2008selecting-e2][^easterbrook2008selecting-e4][^easterbrook2008selecting-e5][^easterbrook2008selecting-e6]; the core design names mentioned in the SIGSOFT standard broadly correspond to them[^ralph2020empirical-e289]:

| Design | Order | Purpose | Computer science example `[Our analysis]` |
|---|---|---|---|
| **Sequential explanatory design** | Quantitative first, then qualitative | Use qualitative results to explain quantitative findings; especially useful when the quantitative phase produces unexpected results[^easterbrook2008selecting-e4] | Mining shows that a certain kind of pull request takes especially long to merge; you then interview maintainers to ask why |
| **Sequential exploratory design** | Qualitative first, then quantitative | Use quantitative results to help interpret qualitative findings and to test the preliminary theory that came out of the qualitative study[^easterbrook2008selecting-e5] | First interview a dozen or so engineers to identify several practices, then use a questionnaire to see how common each one is |
| **Concurrent triangulation design** (close to what the SIGSOFT standard calls a convergent design `[Our analysis]`) | At the same time | Confirm and cross-validate; motivated by the fact that what people say often differs from what they do[^easterbrook2008selecting-e6] | Collect developers' questionnaire answers and their actual tool-usage logs at the same time, and compare the two |

**How to choose** `[Our analysis]`: if you already have data and want to know why, use a sequential explanatory design; if you don't yet understand the phenomenon and want to find out what cases exist before measuring how common they are, use a sequential exploratory design; if you worry that a single source is biased and want the sources to check each other, use a concurrent design. The hard part of a concurrent design is comparing the results of the two analyses and reconciling contradictions between them, which sometimes requires another source of evidence or a follow-up study[^easterbrook2008selecting-e7].

---

## 3. How to do it

### Step 1: State why you are mixing methods, and when and for what each method is used

The essential attributes in the SIGSOFT standard require you to answer four questions[^ralph2020empirical-e276]:

- **Why:** justify the need for multiple methods, and give a purpose statement explaining the overall intent of the design;
- **What**: which design you use;
- **When**: at which stage of the study each method is used;
- **How it maps to the question**: how the design serves the research questions.

Ideally, also draw a diagram of the study design and give a definition of the design you use[^ralph2020empirical-e278].

**Where people go wrong:** the design doesn't match the research question; or the team never agrees on a crisp research question, which can happen when members hold different epistemological perspectives (different views of what counts as knowledge and how you come to know something; say, one person trusts only measured numbers while another values interpreting people's experience) or use very different methods[^ralph2020empirical-e284]. Write the research question as one sentence first, then check which part of it each method answers `[Our analysis]`.

### Step 2: Every component must meet its own standard

The SIGSOFT mixed methods standard covers only how methods are combined; each component must also meet the standard for its own method. A case study plus an experiment, for example, must meet the case study standard, the experiment standard, and the mixed methods standard[^ralph2020empirical-e275]. The quality criteria of every method used all have to be considered[^ralph2020empirical-e281].

**Where people go wrong:** using a method the team has no expertise in and hoping it works, which SIGSOFT calls "cargo cult research" (copying the outward form of a method without mastering its substance)[^ralph2020empirical-e284]. Another is running only superficial statistics on rich qualitative data[^ralph2020empirical-e285], for example reducing interview content to word counts `[Our analysis]`. For a method you don't know well, read the relevant page and guidelines first, or bring in someone who knows it.

### Step 3: Think through how the sample flows between methods

- State whether the methods reuse the same participants or objects, and why[^ralph2020empirical-e278].
- **When successive phases use the same people, consider how the earlier phase affects the later one**[^ralph2020empirical-e285]. `[Our analysis]` For example, if interviewees heard you explain your research hypothesis during the interview and later fill in your questionnaire, their answers may lean toward that hypothesis.
- When the samples for different components come from different populations, this limits the integrated conclusions, and you should acknowledge it in the paper[^ralph2020empirical-e277].

### Step 4: Let the earlier phase really shape the later one

The point of a sequential design is that earlier findings determine what you do next. Failing to use earlier findings when designing the interview guide or questionnaire for a later phase is one of the antipatterns SIGSOFT lists[^ralph2020empirical-e285]. `[Our analysis]` For example, if the mining phase turns up three unexpected patterns, the interview guide should be built around those three patterns, not reuse generic questions written before the mining.

### Step 5: Integrate the results (the hardest step)

Integration is the core requirement of mixed methods: bringing the findings of all methods together to answer the research question[^ralph2020empirical-e277]. "Integration failure" is one of the antipatterns SIGSOFT lists[^ralph2020empirical-e283].

- **Say what each method adds**: corroboration (two methods reach the same conclusion), complementarity (each answers part of the question), or expansion (deepening or broadening understanding)[^ralph2020empirical-e279].
- **Discuss where the findings disagree**[^ralph2020empirical-e279]. Disagreement is not a flaw: SIGSOFT lists "the methods have inconsistent findings" as an invalid criticism[^ralph2020empirical-e287], and disagreements are often exactly what is most worth analyzing. When you can't reconcile them, you may need another source of evidence or a follow-up study[^easterbrook2008selecting-e7].
- `[Our analysis]` A practical approach is to build a joint display table: each row is a sub-question or a finding, each column records what one method found, and the last column gives the integrated conclusion and whether the methods corroborate, complement, or contradict each other. When you write your conclusions, start from this table, not from the results of any single method.

### Step 6: Reporting

- Introduce every method clearly in the introduction and methods sections. A method that suddenly turns up in the discussion or limitations section without having been mentioned earlier is what SIGSOFT calls an "uninvited guest"[^ralph2020empirical-e283].
- Discuss the limitations of every method, and of the integration itself[^ralph2020empirical-e283][^ralph2020empirical-e277].
- You can indicate in the title that the study uses multiple or mixed methods[^ralph2020empirical-e278].
- When conference page limits are tight, details of some methods can go in other papers or in supplementary material[^ralph2020empirical-e286].

---

## 4. Checklist

This checklist is based mainly on the SIGSOFT multi-methodology and mixed methods standard, which is a reviewing standard for software engineering; in other fields, follow your own field's standards `[Our analysis]`. Each component should also be checked against the checklist for its own method.

**Essential**

- [ ] Justify why multiple methods are needed; state the overall intent of the design (why)[^ralph2020empirical-e276]
- [ ] Describe the design used (what), and the stage at which each method is used (when)[^ralph2020empirical-e276]
- [ ] Explain how the design maps to the research questions[^ralph2020empirical-e276]
- [ ] Integrate the findings of all methods to answer the research questions; acknowledge the limitations the integration brings[^ralph2020empirical-e277]

**Desirable**

- [ ] Give a definition of the design used, draw a diagram of the study design, and indicate the design in the title[^ralph2020empirical-e278]
- [ ] State and justify whether samples are reused across methods[^ralph2020empirical-e278]
- [ ] Say what mixing adds (corroboration, complementarity, expansion), and discuss inconsistent findings[^ralph2020empirical-e279]
- [ ] State the philosophical or theoretical foundations of the study; describe difficulties in the design and how you mitigated them; discuss ethical issues raised by mixing methods[^ralph2020empirical-e280]

**Acceptable deviations (not flaws)**[^ralph2020empirical-e286]

- With tight conference page limits, details of some methods go in other papers or supplementary material
- Describing the study as cyclical or parallel processes rather than "phases"

**Common reviewer criticisms that don't hold up** (as listed in the SIGSOFT standard, for software engineering submissions)[^ralph2020empirical-e287]: you don't need to worry about these

- "The methods don't contribute equally", or "the minor method is too small (for example, few participants)"
- "Mixed methods aren't necessary" (when they actually are beneficial)
- "The methods have different philosophical foundations, so they can't be combined" (mixed methods are commonly associated with a pragmatist stance, that is, using whichever methods solve the problem most effectively[^easterbrook2008selecting-e8])
- "The wrong method is dominant"
- "The methods have inconsistent findings"

---

## 5. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| After the main study is done, tacking on a tiny questionnaire or a few interviews and calling it mixed methods | Dressing up a method that plays only a token role as a mixed methods design is what SIGSOFT calls "smoke and mirrors"[^ralph2020empirical-e282] |
| Adding a method to please reviewers | It contributes nothing substantive to the findings; SIGSOFT calls this "selling your soul"[^ralph2020empirical-e282] |
| Writing up each method's results in a separate section, side by side | Without integration, readers don't get one unified answer[^ralph2020empirical-e283] |
| A later-phase questionnaire or interview guide that doesn't use the earlier phase's findings | It defeats the purpose of a sequential design[^ralph2020empirical-e285] |
| Interviewing people and then giving the same people a questionnaire, without considering the effect of the first on the second | The earlier phase may contaminate the later one[^ralph2020empirical-e285] |
| Using a method you don't know well and hoping it works | The component won't meet its own standard[^ralph2020empirical-e284][^ralph2020empirical-e275] |
| Discussing only the limitations of the main method | Every method, and the integration itself, has limitations[^ralph2020empirical-e283] |

Note the difference between the first row and the "criticisms that don't hold up": a small minor method is not a problem in itself[^ralph2020empirical-e287]; the problem is when it makes **no substantive contribution** to the conclusions[^ralph2020empirical-e282]. An interview study with only a few participants that genuinely explains the mining results is a legitimate component `[Our analysis]`.

---

## 6. Further reading

- **SIGSOFT multi-methodology and mixed methods standard**: the full checklist and more than ten antipatterns, plus many exemplar software engineering papers (for example, repository mining plus a questionnaire, or an experiment plus interviews). Useful for finding a paper whose design is close to yours.
- **Easterbrook et al. 2008**: on how to select empirical methods for software engineering research; one section describes the three mixed methods designs with examples. Good to read at the design stage.
- **Storey et al. 2020**: uses a "who benefits, what is the contribution, how is it studied" framework to analyze the research strategies of software engineering papers, and explains why data analysis alone is not enough and when you need to add methods that study people.

Links to every source are in the [source list](../../sources/README.md).

[^ralph2020empirical-e274]: SIGSOFT Multi-Methodology and Mixed Methods standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e274)
[^ralph2020empirical-e275]: SIGSOFT Multi-Methodology and Mixed Methods standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e275)
[^ralph2020empirical-e276]: SIGSOFT Multi-Methodology and Mixed Methods standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e276)
[^ralph2020empirical-e277]: SIGSOFT Multi-Methodology and Mixed Methods standard, Essential Attributes and footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e277)
[^ralph2020empirical-e278]: SIGSOFT Multi-Methodology and Mixed Methods standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e278)
[^ralph2020empirical-e279]: SIGSOFT Multi-Methodology and Mixed Methods standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e279)
[^ralph2020empirical-e280]: SIGSOFT Multi-Methodology and Mixed Methods standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e280)
[^ralph2020empirical-e281]: SIGSOFT Multi-Methodology and Mixed Methods standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e281)
[^ralph2020empirical-e282]: SIGSOFT Multi-Methodology and Mixed Methods standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e282)
[^ralph2020empirical-e283]: SIGSOFT Multi-Methodology and Mixed Methods standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e283)
[^ralph2020empirical-e284]: SIGSOFT Multi-Methodology and Mixed Methods standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e284)
[^ralph2020empirical-e285]: SIGSOFT Multi-Methodology and Mixed Methods standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e285)
[^ralph2020empirical-e286]: SIGSOFT Multi-Methodology and Mixed Methods standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e286)
[^ralph2020empirical-e287]: SIGSOFT Multi-Methodology and Mixed Methods standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e287)
[^ralph2020empirical-e288]: SIGSOFT Multi-Methodology and Mixed Methods standard, Notes. [Evidence](../../sources/notes/ralph2020empirical.md#e288)
[^ralph2020empirical-e289]: SIGSOFT Multi-Methodology and Mixed Methods standard, Notes. [Evidence](../../sources/notes/ralph2020empirical.md#e289)
[^ralph2020empirical-e290]: SIGSOFT General Standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e290)
[^ralph2020empirical-e23]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e23)
[^easterbrook2008selecting-e1]: Easterbrook et al. 2008, §1.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e1)
[^easterbrook2008selecting-e2]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e2)
[^easterbrook2008selecting-e3]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e3)
[^easterbrook2008selecting-e4]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e4)
[^easterbrook2008selecting-e5]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e5)
[^easterbrook2008selecting-e6]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e6)
[^easterbrook2008selecting-e7]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e7)
[^easterbrook2008selecting-e8]: Easterbrook et al. 2008, §5.6. [Evidence](../../sources/notes/easterbrook2008selecting.md#e8)
[^easterbrook2008selecting-e9]: Easterbrook et al. 2008, §6.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e9)
[^storey2020who-e1]: Storey et al. 2020, §2. [Evidence](../../sources/notes/storey2020who.md#e1)
[^storey2020who-e2]: Storey et al. 2020, §3.3. [Evidence](../../sources/notes/storey2020who.md#e2)
[^storey2020who-e3]: Storey et al. 2020, §3.3. [Evidence](../../sources/notes/storey2020who.md#e3)
[^storey2020who-e4]: Storey et al. 2020, §6.2. [Evidence](../../sources/notes/storey2020who.md#e4)
[^storey2020who-e5]: Storey et al. 2020, §6.2. [Evidence](../../sources/notes/storey2020who.md#e5)
[^storey2020who-e6]: Storey et al. 2020, §6.2. [Evidence](../../sources/notes/storey2020who.md#e6)
[^storey2020who-e7]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e7)
[^storey2020who-e8]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e8)
[^storey2020who-e9]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e9)
[^storey2020who-e10]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e10)
[^storey2020who-e11]: Storey et al. 2020, §6.4. [Evidence](../../sources/notes/storey2020who.md#e11)
