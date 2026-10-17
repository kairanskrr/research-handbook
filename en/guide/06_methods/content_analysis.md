# Content analysis: coding a large body of text into categories with a codebook

This page covers **content analysis**: you take a body of recorded material (texts, images, videos, posts), go through it unit by unit, assign each unit to categories according to rules written in advance, and then count or interpret those categories. News stories, ads, social media posts, policy documents, medical records, open-ended survey answers, and GitHub issue reports can all be material for it.

It comes in a quantitative and a qualitative variant. Quantitative content analysis turns text into numbers and answers "how common is this kind of content?"; qualitative content analysis also works with categories, but cares more about the categories themselves and what they mean. For the general ethics requirements when research involves people's data, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); this page covers only content analysis itself.

**Scope**: Content analysis grew up in communication research and is widely used in sociology, psychology, nursing and health research, and education research. In computer science, hand-classifying issue reports, code review comments, forum posts, or papers follows the same logic. The intercoder reliability material on this page draws on communication research (the public guide by Lombard et al., and Krippendorff 2004); the steps of qualitative content analysis follow Mayring (from the German psychology and social science tradition); the distinction between manifest and latent content comes from an introductory article in a pharmacy education journal (Kleinheksel et al.); the general steps draw on a methods page from Columbia University's school of public health; the sampling and computer science examples come from software engineering. For how media and communication research views this kind of study, see the [Media and communication field overview](../07_fields/media-communication/README.md#content-analysis-measure-and-report-intercoder-reliability-properly).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md); when the material is published research, also [Synthesis](../05_research-strategies/synthesize.md).

**After reading this page, you should be able to:**

- judge whether your question suits content analysis, and choose between quantitative and qualitative, manifest and latent;
- define your units of analysis and draw a sample from a large body of text;
- write a codebook that someone else could pick up and code with;
- train coders, and measure and report intercoder reliability the way communication research does;
- tell content analysis apart from thematic analysis in interview studies and from grounded theory.

---

## 1. What this kind of study is, and when to use it

Content analysis is a way of identifying and interpreting meaning in recorded communication: you separate out small pieces of data that stand for key concepts, then apply or build a framework that organizes them, in order to describe or explain a phenomenon[^kleinheksel2020demystifying-e1]. Its object can be any recorded communication: interview transcripts, discourse, observation protocols, video recordings, documents, and so on[^mayring2000qualitative-e2]. From it, researchers can make inferences about the messages in the texts, the writers, the audience, and even the culture and time the texts come from[^columbia2023contentanalysis-e2].

Content analysis started as a strictly quantitative method that counted how often predetermined targets occurred[^kleinheksel2020demystifying-e2]. Qualitative variants came later. Mayring's qualitative content analysis sets out to keep the strengths of quantitative content analysis as developed in communication research and carry them over to qualitative, interpretive steps of analysis[^mayring2000qualitative-e1].

**Questions it is good at**:

- **"How common is this kind of content, and how is it distributed?"**: what share of news stories use a certain frame, how many claims in health app descriptions are evidence-based, what share of a set of issue reports falls into each defect type;
- **"How do sources or periods differ?"**: how two kinds of media cover a story differently, how discussion of a topic changed over ten years;
- **"What categories are there in this body of text?"**: what kinds of open-ended survey answers, user feedback, or forum posts there are.

It cannot answer "why is it like this?" or "does A cause B?". Texts are only the traces that communication leaves behind, and content analysis often disregards the context that produced the text[^columbia2023contentanalysis-e12]. To learn why authors wrote what they did, pair it with an [Interview studies](interview_study.md); to test causation, use an experiment or a [quasi-experiment](quasi_experiment.md).

**How it differs from related methods**:

| | Content analysis | Thematic analysis in an [Interview studies](interview_study.md) | [Grounded theory](grounded_theory.md) | [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md) |
|---|---|---|---|---|
| Material | Any existing text or media; transcripts also work | Transcripts of interviews you conducted | Interviews and other data, with collection and analysis alternating | Large volumes of records from code repositories and bug trackers |
| Where categories come from | Defined in advance (deductive), or derived from the material by rules (inductive); either way written up as a codebook | Themes derived from the data | Generated from the data, not forced into a predefined coding scheme | Mostly extracted by programs, with some manual labeling |
| Main output | Categories and their frequencies and distributions; or a category system | A few themes | A theory made of concepts and their relationships | Statistical patterns |
| Counting occurrences | Core of the quantitative variant | More often does not mean more important | Counting without interpreting is an antipattern | Core |
| Intercoder reliability | Key part of the quantitative variant | Contested; depends on research stance | Generally not required | Required for the manually labeled part |

Sources for the table: for the content analysis column, categories are at the center of the analysis, and predefined categories need explicit definitions, examples, and coding rules[^mayring2000qualitative-e4][^mayring2000qualitative-e9]; the quantitative aim is to produce numbers that show how prevalent something is[^kleinheksel2020demystifying-e4]; and intercoder reliability is a key component[^lombard2010practical-e3]. For the thematic analysis column, themes are not something you count[^braun2006using-e4], and reliability is contested[^mcdonald2019reliability-e1]. For the grounded theory column, data are not forced into a predefined coding scheme[^stol2016grounded-e11], and counting words or codes without interpreting them is an antipattern[^ralph2020empirical-e325]. The mining software repositories column and the overall summary of the table are our own.

**The difference in one sentence**: the core product of content analysis is **a codebook that someone else could pick up and code with**, plus the data coded with it; the core product of thematic analysis is the researcher's interpretation of the data; the core product of grounded theory is a new theory. If you are labeling transcripts and you write category definitions first, have two people code independently, and then compute agreement, you are doing content analysis.

**Two more neighbors.** Coding published case studies into variables and then running statistics on them is a [Case survey](case_survey.md), which is content analysis applied to one particular kind of material. Extracting data from each paper in a systematic review also needs a coding scheme; see [Review studies](review_study.md).

**When it is a poor fit.** Mayring considers qualitative content analysis less appropriate when the research question is highly open-ended, exploratory, or changing, so that working with categories would be a restriction, or when you plan a holistic rather than step-by-step analysis[^mayring2000qualitative-e12]. In that case, consider thematic analysis in an [Interview studies](interview_study.md) or [Grounded theory](grounded_theory.md).

---

## 2. How to do it

The eight steps below follow quantitative content analysis, and point out where the qualitative variant differs.

### Step 1: State the research question, and decide quantitative or qualitative, manifest or latent

**How:**

- **Write the research question first.** When choosing a method, the research question and the nature of the material should come first[^mayring2000qualitative-e13]. Write the question so it is clear what you want to infer from the texts: features of the texts themselves, or something about their writers, audience, or era[^columbia2023contentanalysis-e2].
- **Decide quantitative or qualitative.** The practical difference is intent. Quantitative work aims for numbers that show prevalence or support statistics; qualitative work aims to identify a concept in the text and support it with the text's own words, or to give the text a more organized structure[^kleinheksel2020demystifying-e4].
- **Decide whether the meaning sits on the surface or underneath.** Kleinheksel et al. say choosing a kind of content analysis takes two decisions: what the goal of the analysis is, and where you believe meaning is located[^kleinheksel2020demystifying-e11]. **Manifest content** is what is literally there and can be recognized and counted with little training[^kleinheksel2020demystifying-e3], such as "does the post include code?". **Latent content** requires interpreting what lies beneath the surface[^kleinheksel2020demystifying-e5], such as "is this comment sarcastic?".
- **Decide whether you look only at concepts, or also at relationships between them.** Conceptual analysis establishes whether a concept occurs and how often; relational analysis goes further and examines how concepts relate to each other[^columbia2023contentanalysis-e4].

**Why:** These decisions change every step that follows. High reliability is easy to reach for manifest content and much harder for latent content, and the qualitative variant treats reliability differently (see Step 6).

**Where people go wrong:** the question is "let's see what's in these posts", categories get made up while reading, and at the end everything is counted. The resulting numbers can't be interpreted, because the categories were set after looking at the data. Reading this way is fine while exploring, but fix the categories and rules before formal coding starts.

### Step 2: Define the units of analysis

**How:**

- **Separate two kinds of unit**: the **sampling unit** is one piece of material you draw, such as a news story, an issue report, or a paper; the **coding unit** is the stretch you assign a category to, such as a sentence, a comment, or a paragraph. The two can be the same or different.
- **Choose the level of the coding unit.** The Columbia methods page makes this the first step: decide the level of analysis, whether word, word sense, phrase, sentence, or theme[^columbia2023contentanalysis-e5]. There is no single way to cut text into meaning units; it depends on the type of analysis, and for written text you decide whether to segment by phrase, sentence, or paragraph[^kleinheksel2020demystifying-e7]. Mayring likewise requires splitting the material into units of analysis and working through them step by step according to rules[^mayring2000qualitative-e4].
- **Decide whether you code "present or not" or "how many times".** Coding for whether a concept occurs versus how often it occurs changes the coding process[^columbia2023contentanalysis-e7].

**Why:** If the units aren't fixed, two coders looking at the same material may code it differently, one by whole document and one by sentence, and reliability can't be measured properly from the start.

**Where people go wrong:** an issue report discusses three defects, but you sample and code by report, so it can only get one category. Decide first whether you will end up reporting "how many reports" or "how many defects", then set the units.

### Step 3: Sample the texts

**How:**

- **State the population.** First say which body of texts you want your conclusions to generalize to, then explain where and how you sample. Baltes and Ralph suggest treating most quantitative studies as multi-stage sampling, with authors stating the population they want to generalize to and reflecting on how each stage might introduce bias[^baltes2022sampling-e12]. When representativeness is the goal, the sampling supplement of the ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) empirical standards requires a replicable, algorithmic description of the sampling procedure and an account of the bias each step might introduce[^ralph2020empirical-e127].
- **Think about bias in the source itself.** No sample size, however large, removes bias in the sampling frame[^baltes2022sampling-e5]. In software repositories, every repository may carry biases that are hard to predict[^baltes2022sampling-e14]. If the sampling frame is biased, you can repeat the study with a different frame, for example checking a pattern found in GitHub projects on SourceForge projects[^baltes2022sampling-e13].
- **Keep the sample small enough to finish.** When choosing texts, balance having enough information for a thorough analysis against having so much that coding becomes overwhelming[^columbia2023contentanalysis-e10]. Manual coding is slow: estimate how many minutes each unit takes before deciding how many to draw.

**A typical computer science example**: you want to know "among security-related issue reports in open-source projects, what share falls into each type?" The sampling unit is the issue report. You need to state which projects you draw from (and by what criteria you chose them), the time range, which keywords or labels you used to filter for "security-related", and how you sampled at random after filtering. Keyword filtering itself misses reports that never say "security", and that belongs in your limitations. For how to do and justify the sampling, see [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md#step-3-filter-and-sample-projects).

**Qualitative variant:** qualitative content analysis often selects material purposively and does not aim for statistical representativeness; for how and why, see the sampling part of [Interview studies](interview_study.md#step-1-choose-interviewees).

### Step 4: Build the codebook

The codebook (Mayring calls it a coding agenda) is the core of content analysis. It tells every coder which categories exist, what each one means, and when to use it and when not to.

**Where categories come from: deductive or inductive.**

Mayring sums up the two central procedures of qualitative content analysis as inductive category development and deductive category application[^mayring2000qualitative-e6].

- **Deductive**: when an existing framework already describes the phenomenon, you build codes in advance from concepts in the theory or literature[^kleinheksel2020demystifying-e6]. Hsieh and Shannon call this "directed" content analysis: using concepts from existing theory as deductive codes to further describe or validate the theory[^kleinheksel2020demystifying-e12].
- **Inductive**: when there is no existing framework, codes emerge during the analysis[^kleinheksel2020demystifying-e6]; Hsieh and Shannon call this "conventional" content analysis[^kleinheksel2020demystifying-e12]. Classic quantitative content analysis rarely answers "where do the categories come from?"[^mayring2000qualitative-e7]. Mayring's procedure: first set a selection criterion from the theoretical background and research question that decides which aspects of the material to look at; work through the material piece by piece with this criterion, formulating tentative categories; then, in feedback loops, revise them, reduce them to main categories, and check reliability[^mayring2000qualitative-e8].
- **Mixed**: start deductively but allow categories to be added during coding, or stick with the predefined set. Decide which in advance[^columbia2023contentanalysis-e6].

What sets it apart from [Grounded theory](grounded_theory.md): even when content analysis arrives at its categories inductively, it ends by **fixing them in a codebook with definitions and rules**, and then uses that codebook to code all the material systematically.

**What to write for each category.**

Mayring asks for an explicit definition, examples, and coding rules for each category, stating exactly when a passage can be coded into it[^mayring2000qualitative-e9]. Kleinheksel et al.'s codebook has at least three columns: code name, code description, and example[^kleinheksel2020demystifying-e8]. Building on this, we suggest writing five things for each category:

| Field | Example (coding "issue type" for security-related issue reports) |
|---|---|
| Name | Access control |
| Definition | The reported problem is that an unauthorized person can do something they should not be allowed to do |
| When to use it | The report describes bypassing a permission check, calling something without the required privileges, or missing authentication |
| When not to use it (and how to tell it from neighboring categories) | If information leaks but no unauthorized action is possible, code it "Information disclosure" |
| Examples | One or two passages quoted from real material |

**Rules to settle in advance:**

- how much implication counts: only what is stated outright, or also what is implied[^columbia2023contentanalysis-e8];
- what to do with content irrelevant to the research question[^columbia2023contentanalysis-e9];
- whether one unit can belong to several categories, and what to code when unsure (for example a "cannot tell" category).

Category definitions, anchor examples, and rules for separating neighboring categories are written from theory and the material, filled in step by step, and revised as the analysis goes on[^mayring2000qualitative-e10]. In the quantitative variant, though, we suggest freezing the codebook once formal coding starts; otherwise data coded early and late are not comparable.

**Where people go wrong:** a definition that is one word long ("performance issue") with no boundaries, so two coders each have their own idea of whether "slow" counts. A good test: hand the codebook to someone who wasn't in the discussions and see whether they can code with it.

### Step 5: Train the coders and pretest

**How:**

1. **Walk through the codebook and code together.** After everyone has read the codebook and heard it explained, each person codes the same material independently[^kleinheksel2020demystifying-e9].
2. **Check reliability informally and revise the codebook.** Use a small number of units, ideally not part of the full sample, to assess reliability informally, and keep revising the coding instrument and instructions until agreement looks adequate[^lombard2010practical-e16].
3. **Run a formal pretest.** A rule of thumb for the pretest sample is 30 units[^lombard2010practical-e8].
4. **Iterate over several rounds.** The SIGSOFT standard's extraordinary attribute is an iterative process: rate a subset of the data, resolve disagreements, update the rating scheme or decision rules, and repeat until agreement reaches a minimum threshold[^ralph2020empirical-e131].

**Why:** Krippendorff points out that many problems in reliability testing come from three places: coders who are not really independent, coding instructions they cannot actually follow, or material they cannot understand[^krippendorff2004reliability-e2]. Training and pretesting expose the last two before formal coding starts.

**Where people go wrong:** computing the formal reliability on the units you discussed and fixed during the pretest. Everyone has already compared answers on those units, so agreement will be inflated. Measure formal reliability on fresh units.

### Step 6: Code the material and measure intercoder reliability

**Intercoder reliability** is the extent to which independent coders who evaluate a characteristic of a message reach the same conclusion[^lombard2010practical-e2]. Reliability does not guarantee valid conclusions, but without established reliability the data and their interpretation cannot be considered valid[^lombard2010practical-e3]. In Krippendorff's words, agreement is what we measure and reliability is what we want to infer from it; in content analysis, the most important meaning of reliability is reproducibility[^krippendorff2004reliability-e1].

**How:**

1. **Choose the measure before collecting data.** The reliability index must be chosen before data are collected and reliability is assessed[^lombard2010practical-e5].
2. **Draw a reliability sample.** The formal reliability sample should be at least 50 units or 10% of the full sample, and rarely needs to exceed 300 units[^lombard2010practical-e9]. It must represent the data whose reliability is being tested[^krippendorff2004reliability-e5].
3. **Code independently.** Coding for the reliability test must be done independently, without consultation or guidance; if possible, the researchers themselves should not be coders[^lombard2010practical-e7].
4. **Use a measure that accounts for chance agreement.** Don't rely on percent agreement alone[^lombard2010practical-e11]; Krippendorff argues for explicitly not using it, least of all as a fallback[^krippendorff2004reliability-e3]. An extreme case: if every coder uses only one category, percent agreement is 100%, but the data have no variation and so give no evidence of reliability at all[^krippendorff2004reliability-e4]. Also avoid Cronbach's alpha, Pearson's correlation coefficient, and similar indices that only measure whether two coders' values go up and down together[^lombard2010practical-e13]. There is no consensus on which index is "best"[^lombard2010practical-e14]; Krippendorff's alpha is well regarded and widely applicable: it works with multiple coders, handles different sample sizes and missing data, and can be used for ordinal and numeric variables[^lombard2010practical-e15]. Which one to choose depends on the number of coders, the sample size, and the type of data[^kleinheksel2020demystifying-e10].
5. **Report each variable separately, and take the lowest.** Don't use an overall reliability pooled across all variables[^lombard2010practical-e12]. When several variables together support a conclusion, measure each and take the lowest as the reliability of the whole; averaging easy-to-code variables with hard ones is misleading[^krippendorff2004reliability-e8].
6. **Look at confidence intervals; don't run significance tests.** Consult confidence intervals; testing whether agreement is significantly above chance says nothing useful about reliability[^krippendorff2004reliability-e10].
7. **If you fall short.** You can discard unreliable distinctions, recode or merge categories, or drop variables that don't meet the criterion[^krippendorff2004reliability-e9], and then measure again.
8. **Coding the rest of the material.** Krippendorff holds that coders should be interchangeable and may code different subsamples, as long as there is enough duplication or overlap[^krippendorff2004reliability-e5]. Over a long coding job, a coder's judgments drift over time; recoding the material again after some time improves consistency and stability[^kleinheksel2020demystifying-e15].

> **Where sources disagree: where should the cutoff be?**
>
> - **Lombard et al.'s guide**: coefficients of 0.90 or greater are nearly always acceptable, 0.80 or greater is acceptable in most situations, and 0.70 may be appropriate in some exploratory studies for some indices[^lombard2010practical-e6].
> - **Krippendorff**: the cutoff should depend on the cost of drawing invalid conclusions; he suggests requiring α ≥ 0.800 in general and α ≥ 0.667 where tentative conclusions are still acceptable, but apart from perfect agreement there are no magic numbers[^krippendorff2004reliability-e7].
> - **Mayring's qualitative content analysis**: estimate reliability using only trained members of the project team, and lower the standard; a Cohen's kappa above 0.7 is enough[^mayring2000qualitative-e5].
>
> In practice: state in the paper which measure and cutoff you use and whose they are, and fix them before collecting data, not after you see the results.

> **Does the qualitative variant need reliability?**
>
> It depends on your research stance. Kleinheksel et al. note that qualitative research generally speaks of "trustworthiness" rather than "reliability" and "validity"[^kleinheksel2020demystifying-e17]. In manifest content analysis, coding takes little judgment, so low agreement makes the data invalid; in latent content analysis, reliability and validity pull against each other: more detailed rules give higher agreement, but the coding may drift further from how readers of the research understand it[^kleinheksel2020demystifying-e13][^kleinheksel2020demystifying-e14]. The SIGSOFT supplement on inter-rater reliability and agreement says its requirements do not apply to interpretivist qualitative analysis[^ralph2020empirical-e365]. For the arguments on both sides and a middle path, see [Interview studies](interview_study.md#step-6-make-your-analysis-trustworthy).

**Where people go wrong:** three coders vote on disagreements and treat the reliability problem as solved. Resolving disagreements by majority vote may make you feel better, but it does not change the measured reliability[^krippendorff2004reliability-e9]. Do describe how disagreements were resolved, but compute reliability from the independent coding done **before** any discussion.

### Step 7: Analyze

**How**:

- **Quantitative variant**: report the frequency and proportion of each category; compare distributions across sources and periods; run statistics such as chi-square tests where needed (for the general approach, see [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md)). Give proportions with confidence intervals where you can, especially with small samples.
- **Qualitative variant**: describe what each category means, support it with examples from the text, and explain how categories relate; Mayring holds that frequencies of categories can also be analyzed when the research question calls for it[^mayring2000qualitative-e8].

**Be careful with software and automated methods.** Computer programs are there to support the steps of text interpretation, not to replace them[^mayring2000qualitative-e11]. Software can count exactly how many times a word appears, but it cannot tell what each use of the word means[^columbia2023contentanalysis-e11]. If you use keyword rules, a machine learning classifier, or a large language model to code automatically, treat it as one more "coder": first check its agreement with humans on a hand-coded sample, then apply it to all the data, and report that check in the paper.

**Where people go wrong:** common weaknesses of content analysis are a lack of theoretical grounding, over-reaching inferences, and often doing little more than counting words while ignoring the context that produced the text[^columbia2023contentanalysis-e12]. "News stories mention a word more often" does not mean "the public cares about it more"; when you infer authors' intentions or social attitudes from texts, explain what the inference rests on.

### Step 8: Write the report

**How:**

- **The minimum to report about reliability.** The size of the reliability sample, how it was drawn, and why; the reliability value for each variable and each index; how disagreements were resolved; and so on[^lombard2010practical-e10]. The SIGSOFT supplement on inter-rater reliability and agreement likewise requires describing how two or more raters rated independently and how disagreements were resolved, and reporting an appropriate agreement statistic[^ralph2020empirical-e129].
- **Leave an audit trail.** How the codes were developed and defined, what materials were used to train coders, and what steps were taken to ensure intercoder reliability[^kleinheksel2020demystifying-e16].
- **Publish the codebook.** Ideally, release the full codebook, coding examples, and decision rules as supplementary material so others can reproduce your work.
- **Describe the sampling**: the population, the sources, every filtering and sampling step, and possible biases (see Step 3).

**Write it down:** before you start coding, write one page covering the research question, quantitative or qualitative, units of analysis, sampling steps, a first draft of the codebook, and the reliability measure and cutoff. That page is your analysis plan; record every later change against it.

### Example: applying it to the running example

The running example claims that "published evaluations of large language model vulnerability detectors are inflated by data leakage". Its main body is [Benchmarking](../07_fields/computer-science/practices/benchmarking.md), but one sub-question suits content analysis well: **of the published papers on detecting smart contract vulnerabilities with large language models, how many checked for data leakage?**

- **Research question and type**: quantitative, manifest content analysis; the material is published papers, so it also serves [Synthesis](../05_research-strategies/synthesize.md).
- **Units**: the sampling unit is a paper; the coding unit is "an evaluation" within a paper (one paper may evaluate on several datasets).
- **Sampling**: state which conferences and preprint servers you searched, the time range, the search terms, and the inclusion criteria (for example "uses a large language model to detect smart contract vulnerabilities and reports quantitative results"). You can borrow the search and screening steps from [Review studies](review_study.md).
- **Codebook (deductive)**: variables such as "reports the training data cutoff date of the model used", "test contracts were published before that cutoff", "performed deduplication or a leakage check", and "test set is public". For each variable, write the definition, when to code "yes", and when to code "cannot tell", each with a quoted example from a paper.
- **Reliability**: two people independently code a reliability sample of about 50 papers, compute Krippendorff's alpha for each variable, and revise and retest any variable that misses the cutoff.
- **Output**: a table saying "in N evaluations, X% reported no leakage check at all". This by itself does not prove the results are inflated; that takes the experiments in the benchmarking part. What it shows is how widespread the problem is in the literature.

A real example from the same area: when Durieux et al. compared smart contract analysis tools, they manually mapped the vulnerability types each tool reports onto the ten DASP categories, for example putting "integer overflow" under "arithmetic"[^durieux2020empirical-e10]. That is deductive application of an existing category set. They acknowledge that manual labeling may contain errors; their remedy was for all authors to label independently and then discuss disagreements until they reached consensus[^durieux2020empirical-e14]. If you want to report intercoder reliability, compute it from the independent results before discussion (see Step 6).

---

## 3. Checklist

This checklist draws mainly on the reliability guides from communication research (Lombard et al., Krippendorff) and on the SIGSOFT standard from software engineering; in other fields, follow your own field's norms.

**Must do**

- [ ] State the research question and whether the content analysis is quantitative or qualitative
- [ ] Define the units of analysis, and say whether you code "present or not" or "how many times"[^columbia2023contentanalysis-e7]
- [ ] Describe the sampling steps and possible biases[^ralph2020empirical-e127][^baltes2022sampling-e12]
- [ ] Give every category in the codebook a definition, examples, and coding rules[^mayring2000qualitative-e9]
- [ ] With several coders, choose the reliability measure in advance[^lombard2010practical-e5] and code independently[^lombard2010practical-e7]
- [ ] Use a measure that accounts for chance agreement; don't report percent agreement alone[^lombard2010practical-e11]
- [ ] Report the size of the reliability sample and how it was drawn, the reliability of each variable, and how disagreements were resolved[^lombard2010practical-e10]

**Better practice**

- [ ] Train and pretest on units outside the formal sample, revising the codebook repeatedly[^lombard2010practical-e16]
- [ ] Run several rounds of "code a subset, resolve disagreements, revise the rules" until agreement meets the threshold[^ralph2020empirical-e131]
- [ ] Report reliability for each variable, and take the lowest as the overall reliability[^krippendorff2004reliability-e8]
- [ ] Leave an audit trail: how the codebook was developed, training materials, reliability steps[^kleinheksel2020demystifying-e16]
- [ ] Recode part of the material after some time to check stability[^kleinheksel2020demystifying-e15]
- [ ] Publish the codebook and coding examples

**Outstanding**: report confidence intervals for reliability[^krippendorff2004reliability-e10]; justify the cutoff by the cost of drawing wrong conclusions[^krippendorff2004reliability-e7]; repeat the study with a different sampling frame to check whether the conclusions depend on the source[^baltes2022sampling-e13]

**Fine to skip; not a flaw**: not computing intercoder reliability in interpretive qualitative content analysis[^ralph2020empirical-e365]; using a single coder when multiple coders would be impractical or inconsistent with the study's stance[^ralph2020empirical-e367]. In those cases, explain why the analysis is trustworthy using qualitative quality criteria; see [Interview studies](interview_study.md#step-6-make-your-analysis-trustworthy).

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Reporting only percent agreement | It ignores chance agreement, and it is 100% even when everyone uses the same single category[^lombard2010practical-e11][^krippendorff2004reliability-e4] |
| Using Cronbach's alpha or a correlation coefficient as reliability | They only measure whether ratings rise and fall together, not whether the codes are the same[^lombard2010practical-e13] |
| Averaging reliability across all variables into one number | Easy-to-code variables hide the hard ones[^krippendorff2004reliability-e8][^lombard2010practical-e12] |
| Computing several indices and reporting only the best-looking one | An antipattern listed by SIGSOFT[^ralph2020empirical-e132] |
| Calling reliability "good" when it is below the cutoff | An antipattern listed by SIGSOFT[^ralph2020empirical-e132] |
| Coders conferring while coding the reliability sample | Reliability testing must be independent[^lombard2010practical-e7] |
| Computing reliability after disagreements were discussed and resolved | Majority votes or discussion do not change the measured reliability[^krippendorff2004reliability-e9] |
| Category definitions that are one word long, with no boundaries or examples | Nobody else can code with them[^mayring2000qualitative-e9] |
| Counting word frequencies without looking at context | Software can't tell different meanings of the same word apart[^columbia2023contentanalysis-e11]; counting words while ignoring context is a common weakness[^columbia2023contentanalysis-e12] |
| Coding automatically with keyword rules or a model without checking them | An automated method is also a coder and must first be compared with human coding |
| Using a large sample to cover up a biased sampling frame | No sample size removes bias in the sampling frame[^baltes2022sampling-e5] |
| Calling content-analysis counts "grounded theory" | Grounded theory does not force data into a predefined coding scheme, and counting without interpreting is one of its antipatterns[^stol2016grounded-e11][^ralph2020empirical-e325] |

---

## 5. Further reading

- **An introduction to qualitative content analysis**: Mayring 2000, open access; covers the steps of inductive category development and deductive category application, with a sample coding agenda. From the German psychology and social science tradition.
- **Choosing between manifest and latent content**: Kleinheksel et al. 2020, open access; uses teaching data to explain manifest and latent content analysis, and maps them onto Hsieh and Shannon's three approaches. From pharmacy education.
- **How to measure and report intercoder reliability**: Lombard, Snyder-Duch, and Bracken's public online guide (updated 2010), with step-by-step recommendations; and Krippendorff 2004, a response to that guide explaining why not to use percent agreement and how to set the cutoff. Both come from communication research and disagree on cutoffs and the choice of index, so they are worth reading side by side.
- **A quick overview of the general steps**: the content analysis methods page from Columbia University's school of public health, covering the steps, strengths, and weaknesses of conceptual and relational analysis.
- **Often-cited classics without open full text**: Hsieh and Shannon's 2005 "Three approaches to qualitative content analysis" in Qualitative Health Research, Elo and Kyngäs's 2008 qualitative content analysis process, and the content analysis textbooks by Krippendorff and by Neuendorf. This page does not cite them directly; Hsieh and Shannon's typology is cited via Kleinheksel et al.

Links to all sources are in the [source list](../../sources/README.md).

[^kleinheksel2020demystifying-e1]: Kleinheksel et al. 2020, Introduction. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e1)
[^kleinheksel2020demystifying-e2]: Kleinheksel et al. 2020, Introduction. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e2)
[^kleinheksel2020demystifying-e3]: Kleinheksel et al. 2020, Qualitative Content Analysis. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e3)
[^kleinheksel2020demystifying-e4]: Kleinheksel et al. 2020, Qualitative Content Analysis. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e4)
[^kleinheksel2020demystifying-e5]: Kleinheksel et al. 2020, Qualitative Content Analysis. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e5)
[^kleinheksel2020demystifying-e6]: Kleinheksel et al. 2020, Creating and Using Codes. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e6)
[^kleinheksel2020demystifying-e7]: Kleinheksel et al. 2020, Creating and Using Codes. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e7)
[^kleinheksel2020demystifying-e8]: Kleinheksel et al. 2020, Manifest Content Analysis. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e8)
[^kleinheksel2020demystifying-e9]: Kleinheksel et al. 2020, Manifest Content Analysis. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e9)
[^kleinheksel2020demystifying-e10]: Kleinheksel et al. 2020, Manifest Content Analysis. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e10)
[^kleinheksel2020demystifying-e11]: Kleinheksel et al. 2020, How to Choose a Methodological Approach. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e11)
[^kleinheksel2020demystifying-e12]: Kleinheksel et al. 2020, Navigating Terminology. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e12)
[^kleinheksel2020demystifying-e13]: Kleinheksel et al. 2020, Ensuring Quality. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e13)
[^kleinheksel2020demystifying-e14]: Kleinheksel et al. 2020, Ensuring Quality. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e14)
[^kleinheksel2020demystifying-e15]: Kleinheksel et al. 2020, Ensuring Quality. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e15)
[^kleinheksel2020demystifying-e16]: Kleinheksel et al. 2020, Ensuring Quality. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e16)
[^kleinheksel2020demystifying-e17]: Kleinheksel et al. 2020, Ensuring Quality. [Evidence](../../sources/notes/kleinheksel2020demystifying.md#e17)
[^mayring2000qualitative-e1]: Mayring 2000, para. [2]. [Evidence](../../sources/notes/mayring2000qualitative.md#e1)
[^mayring2000qualitative-e2]: Mayring 2000, para. [4]. [Evidence](../../sources/notes/mayring2000qualitative.md#e2)
[^mayring2000qualitative-e4]: Mayring 2000, para. [7]. [Evidence](../../sources/notes/mayring2000qualitative.md#e4)
[^mayring2000qualitative-e5]: Mayring 2000, para. [7]. [Evidence](../../sources/notes/mayring2000qualitative.md#e5)
[^mayring2000qualitative-e6]: Mayring 2000, para. [8]. [Evidence](../../sources/notes/mayring2000qualitative.md#e6)
[^mayring2000qualitative-e7]: Mayring 2000, para. [9]. [Evidence](../../sources/notes/mayring2000qualitative.md#e7)
[^mayring2000qualitative-e8]: Mayring 2000, para. [12]. [Evidence](../../sources/notes/mayring2000qualitative.md#e8)
[^mayring2000qualitative-e9]: Mayring 2000, para. [15]. [Evidence](../../sources/notes/mayring2000qualitative.md#e9)
[^mayring2000qualitative-e10]: Mayring 2000, para. [17]. [Evidence](../../sources/notes/mayring2000qualitative.md#e10)
[^mayring2000qualitative-e11]: Mayring 2000, para. [18]. [Evidence](../../sources/notes/mayring2000qualitative.md#e11)
[^mayring2000qualitative-e12]: Mayring 2000, para. [27]. [Evidence](../../sources/notes/mayring2000qualitative.md#e12)
[^mayring2000qualitative-e13]: Mayring 2000, para. [28]. [Evidence](../../sources/notes/mayring2000qualitative.md#e13)
[^krippendorff2004reliability-e1]: Krippendorff 2004, Relation Between Agreement and Reliability, author's manuscript, p. 3. [Evidence](../../sources/notes/krippendorff2004reliability.md#e1)
[^krippendorff2004reliability-e2]: Krippendorff 2004, author's manuscript, p. 3. [Evidence](../../sources/notes/krippendorff2004reliability.md#e2)
[^krippendorff2004reliability-e3]: Krippendorff 2004, author's manuscript, p. 10. [Evidence](../../sources/notes/krippendorff2004reliability.md#e3)
[^krippendorff2004reliability-e4]: Krippendorff 2004, author's manuscript, p. 10. [Evidence](../../sources/notes/krippendorff2004reliability.md#e4)
[^krippendorff2004reliability-e5]: Krippendorff 2004, Recommendations (i). [Evidence](../../sources/notes/krippendorff2004reliability.md#e5)
[^krippendorff2004reliability-e7]: Krippendorff 2004, Recommendations (iii). [Evidence](../../sources/notes/krippendorff2004reliability.md#e7)
[^krippendorff2004reliability-e8]: Krippendorff 2004, Recommendations (iv). [Evidence](../../sources/notes/krippendorff2004reliability.md#e8)
[^krippendorff2004reliability-e9]: Krippendorff 2004, Recommendations (iv). [Evidence](../../sources/notes/krippendorff2004reliability.md#e9)
[^krippendorff2004reliability-e10]: Krippendorff 2004, Recommendations (iii). [Evidence](../../sources/notes/krippendorff2004reliability.md#e10)
[^columbia2023contentanalysis-e2]: Columbia University Mailman School of Public Health methods page, Overview. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e2)
[^columbia2023contentanalysis-e4]: Columbia University Mailman School of Public Health methods page, Types of Content Analysis. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e4)
[^columbia2023contentanalysis-e5]: Columbia University Mailman School of Public Health methods page, Conceptual Analysis, step 1. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e5)
[^columbia2023contentanalysis-e6]: Columbia University Mailman School of Public Health methods page, Conceptual Analysis, step 2. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e6)
[^columbia2023contentanalysis-e7]: Columbia University Mailman School of Public Health methods page, Conceptual Analysis, step 3. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e7)
[^columbia2023contentanalysis-e8]: Columbia University Mailman School of Public Health methods page, Conceptual Analysis, steps 4–5. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e8)
[^columbia2023contentanalysis-e9]: Columbia University Mailman School of Public Health methods page, Conceptual Analysis, step 6. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e9)
[^columbia2023contentanalysis-e10]: Columbia University Mailman School of Public Health methods page, Relational Analysis. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e10)
[^columbia2023contentanalysis-e11]: Columbia University Mailman School of Public Health methods page, Reliability and Validity. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e11)
[^columbia2023contentanalysis-e12]: Columbia University Mailman School of Public Health methods page, Disadvantages of Content Analysis. [Evidence](../../sources/notes/columbia2023contentanalysis.md#e12)
[^lombard2010practical-e2]: Lombard et al. 2010, Section 2. [Evidence](../../sources/notes/lombard2010practical.md#e2)
[^lombard2010practical-e3]: Lombard et al. 2010, Section 3. [Evidence](../../sources/notes/lombard2010practical.md#e3)
[^lombard2010practical-e5]: Lombard et al. 2010, Section 4, step 1. [Evidence](../../sources/notes/lombard2010practical.md#e5)
[^lombard2010practical-e6]: Lombard et al. 2010, Section 4, step 3. [Evidence](../../sources/notes/lombard2010practical.md#e6)
[^lombard2010practical-e7]: Lombard et al. 2010, Section 4, step 5. [Evidence](../../sources/notes/lombard2010practical.md#e7)
[^lombard2010practical-e8]: Lombard et al. 2010, Section 4, step 5. [Evidence](../../sources/notes/lombard2010practical.md#e8)
[^lombard2010practical-e9]: Lombard et al. 2010, Section 4, step 6. [Evidence](../../sources/notes/lombard2010practical.md#e9)
[^lombard2010practical-e10]: Lombard et al. 2010, Section 4, step 8. [Evidence](../../sources/notes/lombard2010practical.md#e10)
[^lombard2010practical-e11]: Lombard et al. 2010, Section 4. [Evidence](../../sources/notes/lombard2010practical.md#e11)
[^lombard2010practical-e12]: Lombard et al. 2010, Section 4. [Evidence](../../sources/notes/lombard2010practical.md#e12)
[^lombard2010practical-e13]: Lombard et al. 2010, Section 4. [Evidence](../../sources/notes/lombard2010practical.md#e13)
[^lombard2010practical-e14]: Lombard et al. 2010, Section 5. [Evidence](../../sources/notes/lombard2010practical.md#e14)
[^lombard2010practical-e15]: Lombard et al. 2010, Section 5. [Evidence](../../sources/notes/lombard2010practical.md#e15)
[^lombard2010practical-e16]: Lombard et al. 2010, Section 4, step 4. [Evidence](../../sources/notes/lombard2010practical.md#e16)
[^baltes2022sampling-e5]: Baltes & Ralph 2022, §2.6. [Evidence](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e12]: Baltes & Ralph 2022, §2.5. [Evidence](../../sources/notes/baltes2022sampling.md#e12)
[^baltes2022sampling-e13]: Baltes & Ralph 2022, §6.2. [Evidence](../../sources/notes/baltes2022sampling.md#e13)
[^baltes2022sampling-e14]: Baltes & Ralph 2022, §6.2. [Evidence](../../sources/notes/baltes2022sampling.md#e14)
[^ralph2020empirical-e127]: SIGSOFT Empirical Standards, Sampling Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e127)
[^ralph2020empirical-e129]: SIGSOFT Empirical Standards, Inter-Rater Reliability and Agreement Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e131]: SIGSOFT Empirical Standards, Inter-Rater Reliability and Agreement Supplement, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e131)
[^ralph2020empirical-e132]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e132)
[^ralph2020empirical-e325]: SIGSOFT Grounded Theory standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e325)
[^ralph2020empirical-e365]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e365)
[^ralph2020empirical-e367]: SIGSOFT Inter-Rater Reliability and Agreement Supplement, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e367)
[^braun2006using-e4]: Braun & Clarke 2006, What counts as a theme? [Evidence](../../sources/notes/braun2006using.md#e4)
[^mcdonald2019reliability-e1]: McDonald et al. 2019, §1, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e1)
[^stol2016grounded-e11]: Stol et al. 2016, §2.1. [Evidence](../../sources/notes/stol2016grounded.md#e11)
[^durieux2020empirical-e10]: Durieux et al. 2020, §3.1. [Evidence](../../sources/notes/durieux2020empirical.md#e10)
[^durieux2020empirical-e14]: Durieux et al. 2020, §4.2. [Evidence](../../sources/notes/durieux2020empirical.md#e14)
