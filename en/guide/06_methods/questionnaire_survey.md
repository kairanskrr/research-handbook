# Questionnaire surveys: collecting data from many people

This page is about **questionnaire surveys**: you design a questionnaire made up mostly of closed-ended questions, have a group of people fill it in, and then analyze the answers systematically. Examples are surveying how developers use code review tools, or how security engineers handle vulnerability reports. Outside computer science, an education study surveying how teachers use online teaching platforms is the same kind of research.

If what you plan is one-on-one, open-ended interviews, that is a different kind of study (a qualitative survey, or interview study)[^ralph2020empirical-e256]; see [Interview studies](interview_study.md). For the basic concepts of sampling (population, sampling frame, sample, representativeness), see [Decide what you are studying: unit of analysis and population](../02_do-the-project/01_question-to-evidence.md#3-decide-what-you-are-studying-unit-of-analysis-and-population). For the general ethics of research with human participants, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md). This page covers only what is specific to questionnaires.

**Scope** `[Our analysis]`: the standards and examples on this page come mainly from software engineering. They are based on the ACM SIGSOFT (Association for Computing Machinery Special Interest Group on Software Engineering) Empirical Standards and on several methods papers from software engineering about surveys, sampling, and psychometrics (Wagner et al., Torchiano et al., Molléri et al., Baltes and Ralph, Graziotin et al.). If you run a survey in another field, check that field's conventions first. If you need to develop a new scale or adapt an existing one, see the psychology page [Scale development and measurement studies](scale_development.md).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md), [Measurement](../05_research-strategies/measure.md).

**After reading this page you should be able to:**

- judge whether your question suits a questionnaire, and what a questionnaire cannot answer;
- define the population, recruit participants, write questions that are neither leading nor ambiguous, and analyze the results with methods suited to ordinal data; and finally check your study against the checklist at the end.

---

## 1. What this kind of research is and when to use it

The ACM SIGSOFT Empirical Standards define a questionnaire survey as a study in which a sample of respondents answers a series of (mostly structured) questions, usually through an electronic or paper form[^ralph2020empirical-e231]. Participants answer predefined, mostly closed-ended questions, and the researchers analyze the answers systematically[^ralph2020empirical-e232]. The whole point of a large-scale survey is to give up some internal validity (whether the conclusions hold within the study itself, for example whether alternative explanations can be ruled out) in exchange for external validity (whether the conclusions generalize)[^baltes2022sampling-e20]. So the quality of the sampling directly decides whether a survey study is worth anything `[Our analysis]`.

**It can answer three kinds of questions**[^ralph2020empirical-e234]:

- **Descriptive**: how a practice, tool, or opinion is distributed in some population. The interest is in "what the distribution is", not "why"[^wagner2020challenges-e1]. For example, "what share of developers use a certain kind of tool".
- **Exploratory**: generating insights, hypotheses, or models for later research.
- **Confirmatory**: testing propositions stated in advance. Here the questionnaire design should ideally be guided by theory[^wagner2020challenges-e2].

**Be clear about what it cannot answer:**

- **A survey observes; it doesn't intervene.** Unlike an experiment, it doesn't actively apply and control a factor[^torchiano2017lessons-e1], so it generally can't give you causal conclusions. Researchers often treat survey data as if it were experimental data without realizing it, and see causal relationships that aren't there[^torchiano2017lessons-e2].
- **Ask for opinions and you only get opinions.** "Is automated testing more effective than manual testing?" asks for an opinion, and the conclusion can only be "most people think so". Only questions about facts the respondents experienced themselves ("in your last project, which kind of testing found more defects?") let you try to analyze facts, and even then you still have to discuss possible bias in the answers[^wagner2020challenges-e14].
- **Don't ask "what should be done".** Surveys are good for asking "what is happening where you are" and "why it happens", not for normative questions[^torchiano2017lessons-e3].

**How it differs from related methods** `[Our analysis]`:

| | Questionnaire survey | [Interview studies](interview_study.md) | [Controlled experiments](controlled_experiment.md) | [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md) |
|---|---|---|---|---|
| Data | Many people's answers to fixed questions | Open-ended conversations with a few people | Measurements under controlled conditions | Activity traces left on platforms |
| Good at | Distributions, opinions, self-reported practices | Understanding "why", discovering new concepts | Causal relationships | Large-scale patterns in actual behavior |
| Main weakness | Self-report only; sample bias | Hard to generalize | Setting is removed from reality | Can't see motives or opinions |

**How to choose** `[Our analysis]`: use a questionnaire when you want to know "how many, how common, what do people think". If you aren't yet sure what to ask, do a few interviews first and then design the questionnaire. A questionnaire measures what people *say* they do; you can cross-check it against other data sources such as work repositories[^molleri2020empirically-e7]. These practices come mainly from software engineering; other areas of computer science, such as human-computer interaction and usable security, can use them directly. Surveys in other fields should follow their own field's conventions `[Our analysis]`.

---

## 2. How to do it

### Step 1: Start from the research questions; define the population, unit of analysis, and sampling frame

Write the research questions first, then decide whom to ask and what to ask. Every question should map to a research objective, with wording and format suited to the respondents[^ralph2020empirical-e240]; if you can't say which research question an item answers, delete it `[Our analysis]`. The most common mistake is to start from "who can I get to fill this in" and then piece the questions together. When choosing respondents, ask "who can best give me the information I need", not "who is most likely to have time"; a low response rate is easier to deal with than useless answers[^torchiano2017lessons-e4].

1. **Target population**: who do you want your conclusions to apply to? "Open source contributors who use Rust", or "professional developers worldwide"[^wagner2020challenges-e3]? For the latter, in most cases nobody can say how large it is or what it is made of[^wagner2020challenges-e4]. The more specific the population, the easier it is to argue that your sample resembles it. `[Our analysis]`
2. **Unit of analysis**: is your "one" a person, a team, or a company? Randomly sampling developers is not the same as surveying developers in a random sample of companies; with the wrong unit of analysis, the data may be useless for your research question[^torchiano2017lessons-e5].
3. **Sampling frame**: the list you can actually draw people from. In Torchiano et al.'s observation, software engineering research rarely has a suitable sampling frame[^torchiano2017lessons-e6]. When you consider where a list comes from, ask: does it tend to include some subgroups more than others? If inclusion criteria vary, people have different chances of being selected[^torchiano2017lessons-e7].

**Where people go wrong**: describing the respondents' demographics without saying what the target population is. A checklist built from 14 methodological sources[^molleri2020empirically-e1] was used to assess published survey papers, and "defining the population" turned out to be one of the least-followed items[^molleri2020empirically-e5]: papers often describe participants' demographics but rarely state the target population[^molleri2020empirically-e6].

### Step 2: Sampling and recruitment

**Decide first how you will invite people**, because that decides what you can report[^wagner2020challenges-e11]:

- **Closed invitation**: you invite only the people on a list. You can calculate the response rate exactly and control who responds; the cost is that you usually get fewer responses. You can have the survey tool issue each invitee a unique access code so the invitation can't be forwarded freely[^torchiano2017lessons-e17].
- **Open invitation**: you post a link on mailing lists, forums, or social media. It spreads further, but you don't know who saw the invitation, can't calculate a response rate, and have to do extra work comparing respondents with the target population[^torchiano2017lessons-e16]. After switching to an open invitation, Wagner et al. also saw a large number of drop-outs from people who clicked in, took a look, and left[^wagner2020challenges-e12].

**Estimate how many invitations to send.** Participation rates in software engineering surveys are often very low, usually under 10%[^torchiano2017lessons-e8]; Wagner et al.'s email invitations had response rates of only 2% to 4%[^wagner2020challenges-e7]. Work backward from the number of responses you need to the number of invitations. For reference, Wagner et al. estimate that with developers as the population, you need 400 or more responses, plus a check of representativeness, to claim strong generalizability, and most surveys don't reach that[^wagner2020challenges-e6]. The number of responses also has to support the statistical analysis you plan (statistical power, i.e. how likely you are to detect the expected effect)[^ralph2020empirical-e238].

**The limits of convenience sampling.** Posting a link on mailing lists or social media is essentially convenience sampling (picking whoever is easy to reach), which threatens generalizability[^baltes2022sampling-e2]. But that is not a reason to reject a paper; failing to take feasible steps to reduce bias is[^baltes2022sampling-e21]. Also note:

- A large, diverse sample can support "a certain correlation generalizes", but **cannot support specific proportions** ("38% of developers use X")[^baltes2022sampling-e17]. Proportions are exactly what descriptive surveys most want to report, so be especially careful `[Our analysis]`. If the sampling frame itself is biased, no sample size will make up for it[^baltes2022sampling-e5].
- You can consider respondent-driven sampling (an advanced form of snowball sampling, where participants recruit further participants, designed to reduce bias)[^ralph2020empirical-e250], but it has also been criticized for producing overly optimistic confidence intervals[^baltes2022sampling-e18].

**Raising the response rate and reducing response bias** (the SIGSOFT standard says "response bias". The worry here is that the people who responded differ systematically from those who didn't, which survey methodologists usually call *nonresponse bias*; elsewhere "response bias" often means the answers themselves are distorted, for example people answering in a way that makes them look good. `[Our analysis]`):

- Open with important questions that respondents care about, not demographic questions; avoid matrix questions and mandatory questions; send reminders; offer incentives[^baltes2022sampling-e19].
- Reminders: the first reminder (usually 4 to 8 days later) clearly raises the response rate; a third has little effect; don't remind people who have already responded[^torchiano2017lessons-e20]. You can also send a follow-up about two weeks before the survey closes[^wagner2020challenges-e13].
- Rewards such as prize draws, payment, or sharing the results get less motivated people to take part too, so you don't hear only from enthusiasts[^torchiano2017lessons-e19]. If you use incentives, discuss their effect on voluntariness and on response bias[^ralph2020empirical-e244].

**After it goes out**: keep monitoring the response rate and find out why people aren't responding[^molleri2020empirically-e3]; plan in advance how you will handle nonresponse and drop-outs, and state how you will handle missing data (imputation, weighting adjustments, or discarding)[^ralph2020empirical-e237]. With an open invitation, include enough background questions to judge whether respondents belong to the target population, and remove responses that clearly don't[^wagner2020challenges-e33].

> **When surveying tool use, take special care: don't name the tool in the invitation.** If the invitation mentions a particular tool, people who don't use it tend to opt out, which Torchiano et al. think leads to underestimating the adoption rate[^torchiano2017lessons-e18]. By the same mechanism, users may be overrepresented among respondents, so the adoption rate could also be overestimated; either way the estimate is distorted, so don't name the tool in the invitation `[Our analysis]`.

### Step 3: Design the questions

**Wording**[^torchiano2017lessons-e9]:

- Keep questions short and ask about one concept per question. Avoid double-barreled questions, such as "Do you agree that refactoring and code smell detection are both necessary?"[^torchiano2017lessons-e10]; someone who agrees with the first half but not the second can't answer.
- Avoid the passive voice and double negatives.
- **Don't lead.** "Do you prefer agile projects or the usual non-agile projects?" calls non-agile projects "usual" and hints at the answer[^torchiano2017lessons-e11].
- Ask about recent events; don't ask people to recall "your last ten projects"[^torchiano2017lessons-e13].
- Sensitive questions (their company, income, opinions about management) can make people drop out; if you really need them, explain to respondents why you are asking[^torchiano2017lessons-e12].

**Response options**: a Likert scale (graded options from "strongly disagree" to "strongly agree") suits measuring agreement with a statement, but its precision is limited. With ordinal scales like this, **give every option a clear verbal label**; don't just offer "1 to 6" and leave people guessing what separates 4 from 5[^torchiano2017lessons-e14]. For factual questions about experience or frequency, ranges with clear reference points ("less than 1 year", "1 to 3 years", ...) work better[^torchiano2017lessons-e15].

**The questionnaire as a whole**: plan the order and number of questions carefully[^molleri2020empirically-e7]. Online questionnaires can include attention-check questions (for example, "For this question, please select 'Disagree'"), and you should try to identify responses produced by AI or bots; exclude both kinds of response[^ralph2020empirical-e241].

### Step 4: Use validated scales to measure abstract concepts

Job satisfaction, motivation, and well-being are **constructs**: concepts you can't observe directly and can only measure indirectly through a set of items. You can't measure them with a ruler[^wagner2020challenges-e26]; you have to either develop or adopt a validated measurement instrument[^wagner2020challenges-e27]. The SIGSOFT standard lists "measuring constructs with validated scales (or adapted ones), or analyzing construct validity afterwards" as essential[^ralph2020empirical-e236]. First, keep two concepts apart:

- **Reliability**: whether scores are stable and consistent, for example whether repeated administrations give consistent results; internal consistency asks whether, within a single administration, the items measuring the same construct give consistent scores[^wagner2020challenges-e29]. So it is best to measure each variable with more than one item[^molleri2020empirically-e4].
- **Validity**: how far evidence and theory support your interpretation of the scores[^wagner2020challenges-e30]. For example, scores should correlate with related measures and not with unrelated ones[^wagner2020challenges-e31].

**How:**

1. **Look for an existing scale first.** Developing and validating a scale can take several years[^graziotin2021psychometrics-e4].
2. **Use it as is; don't change the items.** Changing items often damages a scale's reliability and validity[^graziotin2021psychometrics-e1][^wagner2020challenges-e28]. The price is that there is no flexibility: you use all of it or none[^wagner2020challenges-e32]. If you really must adapt it, analyze construct validity afterwards, as the SIGSOFT standard says[^ralph2020empirical-e236].
3. **Don't measure a construct with a single item you wrote yourself.** Some researchers have admitted that in their own earlier work they measured "productivity" with a single Likert item; that scale had never been validated, which made the results less valuable[^graziotin2021psychometrics-e2].

### Step 5: Pilot, then revise the questionnaire

Before the real launch, check that the questions, layout, length, and technology work. Common methods are a pilot study (having a small number of people from the target group fill it in first), test-retest, focus groups, and expert or non-expert review[^molleri2020empirically-e2][^ralph2020empirical-e242].

- After the pilot, **talk with the people who tried it** to confirm the questions were understood easily and correctly[^wagner2020challenges-e24]. For a multilingual questionnaire, Wagner et al. had independent team members who were native speakers pilot each translation[^wagner2020challenges-e25].
- **Record what you changed and put it in the paper**[^molleri2020empirically-e8][^ralph2020empirical-e242].
- If you revised the questionnaire repeatedly based on pilot data, you can't use the same pilot data to show it is valid: data used to tune the questionnaire can't also serve as the final test `[Our analysis]`.

### Step 6: Analyze closed-ended questions

**Start with descriptive statistics.** For single-choice and multiple-choice questions, report proportions and show them in bar charts. Likert items are **ordinal data**: they can be ordered, but you can't assume the distance between adjacent options is equal, and only data with well-defined distances can be used with the full range of statistical tests[^wagner2020challenges-e15]. So for central tendency use the **mode and median**, and show each item's full distribution with a stacked bar chart[^wagner2020challenges-e16]; for tests, use rank-based tests (such as the Wilcoxon signed-rank test), because ordinal data doesn't meet the assumptions of methods like the t-test[^wagner2020challenges-e17].

**Then look at effect sizes and representativeness.** Surveys easily produce large samples, and the larger the sample, the easier it is to get "significance", so report effect sizes (how big the difference or association is)[^wagner2020challenges-e18]. When the sample isn't representative, it's unclear what a significance test actually tells you[^wagner2020challenges-e19]. You can estimate representativeness by comparing your sample's demographics with large public surveys; but those surveys have biases of their own, for example the Stack Overflow annual survey covers only its registered users[^wagner2020challenges-e5]. For the general treatment of significance and effect sizes, see [Report how big and how certain, not just p-values](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value).

> **Where sources disagree: can you average Likert data?**
> - **Treat it as ordinal**: Wagner et al. hold that Likert items are ordinal data, so you should use the median rather than the mean, and rank-based tests[^wagner2020challenges-e15][^wagner2020challenges-e17].
> - **In practice the mean is often used**: even Wagner et al., when estimating confidence intervals by bootstrapping, switched to the mean because there was no well-established method for the median, while also reporting the median[^wagner2020challenges-e20]; in psychometrics, item difficulty is computed directly from the mean of a Likert item[^graziotin2021psychometrics-e3].
>
> In practice `[Our analysis]`: report the median and the full distribution (a stacked bar chart) for your main results; when you really do need the mean or mean-based methods, give your reasons and show the distribution as well, so readers can judge for themselves.

### Step 7: Analyze open-ended questions

Open-ended questions let respondents describe things in their own words. They help you understand reasons and discover new concepts, but they produce a lot of text that has to be analyzed by hand[^wagner2020challenges-e21]. A questionnaire made up mainly of open-ended questions doesn't fall under the questionnaire survey standard[^ralph2020empirical-e233]; treat it by the standards for qualitative research `[Our analysis]`.

- Analyze the answers by coding (labeling each answer with a tag that sums up its meaning, then grouping the tags). Do it as a team with independent verification to reduce researcher bias, and state which method you used and how you departed from it[^wagner2020challenges-e23]. For how to code, see [Interview studies](interview_study.md#step-5-coding-and-thematic-analysis).
- An anonymous questionnaire is analyzed after the fact: you can't adjust the questions as you collect data, and you can't go back to participants to check your interpretation. This is an important difference from interview studies[^wagner2020challenges-e22].

### Step 8: Ethics, informed consent, and anonymity

For the general requirements (risk, informed consent, privacy, ethics review), see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md). Here we list only the points specific to questionnaires.

- **Don't treat public email addresses as a recruitment list.** Collecting email addresses from GitHub commit records and mass-mailing unsolicited invitations is common but ethically problematic[^wagner2020challenges-e8][^baltes2022sampling-e22]; under the ethics codes of the market research industry, using user information from GitHub or Stack Overflow to contact potential participants is unethical[^wagner2020challenges-e9]. Some authors who did this received complaints from the people they had contacted[^wagner2020challenges-e10]. At the time, they wrote a short, polite invitation that left it to recipients to opt in, and that also served as the informed consent form[^wagner2020challenges-e10]. If you are new to this, ask your advisor and your ethics committee first. `[Our analysis]`
- **Informed consent can go on the first page of the questionnaire.** Filling in a questionnaire that clearly states it is part of a research project can be treated as consent; a separate consent form isn't necessarily needed[^ralph2020empirical-e254]. If you pay participants, explain the payment and how you avoid coercion[^ralph2020empirical-e255].
- **Anonymous does not mean unidentifiable.** Background details such as "company + job title" can be combined to identify a specific person[^ralph2020empirical-e253]. Ask only the background questions your analysis needs, and before releasing data, check whether combinations of answers could identify individuals. `[Our analysis]`

### Step 9: Reporting

Beyond the general advice on writing a research paper (see [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md)), a survey paper needs to state clearly:

- the target population, sampling strategy, and how you recruited (list, advertisement, invitation, incentives)[^ralph2020empirical-e235];
- the response rate, and what you did to raise it[^ralph2020empirical-e238][^molleri2020empirically-e9];
- how respondents might differ from the target population[^ralph2020empirical-e239];
- **the complete questionnaire, attached**[^ralph2020empirical-e240], ideally together with the invitation, the codebook, the analysis scripts, and the data[^ralph2020empirical-e245][^molleri2020empirically-e10];
- which results are backed by evidence and which are your interpretation or speculation; keep speculation out of the results section[^ralph2020empirical-e200];
- and don't draw conclusions about the population unless you have argued that your sample is representative[^ralph2020empirical-e251].

---

## 3. Checklist

Based mainly on the SIGSOFT questionnaire survey standard and its supplements on sampling and ethics. These are review standards for software engineering; other fields should follow their own conventions `[Our analysis]`.

**Essential**

- [ ] State the target population and define the sampling strategy[^ralph2020empirical-e235]
- [ ] Explain how the questionnaire was developed and how participants were selected or recruited[^ralph2020empirical-e235]
- [ ] Measure constructs with validated scales, or analyze construct validity afterwards[^ralph2020empirical-e236]
- [ ] Explain how you monitored responses, handled nonresponse and drop-outs, and dealt with missing data[^ralph2020empirical-e237]
- [ ] Analyze the response rate; assess whether the number of participants is sufficient[^ralph2020empirical-e238]
- [ ] Discuss how respondents might differ from the target population[^ralph2020empirical-e239]
- [ ] Provide the questionnaire itself; every question maps to a research objective, with wording suited to the respondents[^ralph2020empirical-e240]

**Desirable**

- [ ] Include attention-check questions; identify and exclude responses generated by AI or bots[^ralph2020empirical-e241]
- [ ] Test the questionnaire with a pilot, test-retest, or expert review, and report what you changed as a result[^ralph2020empirical-e242]
- [ ] Analyze response bias quantitatively; raise the response rate with incentives, reminders, and targeted advertising[^ralph2020empirical-e243]
- [ ] If you used incentives, discuss their effect on voluntariness and response bias[^ralph2020empirical-e244]
- [ ] Publish the questionnaire, codebook, analysis scripts, and data; consider informed consent and the risk of re-identification[^ralph2020empirical-e245]
- [ ] Separate results backed by evidence from interpretation and speculation[^ralph2020empirical-e200]
- [ ] For online surveys, use respondent-driven sampling rather than simple snowball sampling[^ralph2020empirical-e250]

**Extraordinary**

- [ ] Check in advance that the planned analyses are feasible; report scale validation in terms of dimensionality, reliability, and validity[^ralph2020empirical-e246]

**Acceptable deviations (not flaws)**[^ralph2020empirical-e247]

- Not publishing some questions for copyright reasons (but cite where the questions came from); not describing how drop-outs or missing data were handled when there were none

**Criticisms common in review that are not valid** (as listed in the SIGSOFT standard, for software engineering submissions): you don't need to worry about these

- "The open, public survey doesn't report a response rate", "the data is sensitive, yet the full data isn't published", "it only reflects people's opinions"; or "the sample is too small" without explaining why it is too small to answer the research questions[^ralph2020empirical-e248]
- "The results are unsurprising" or "the results don't match my experience"[^ralph2020empirical-e249]
- A vague "the results may not generalize" without pointing to anything specific that should have been done (for example, sending reminders)[^ralph2020empirical-e252]

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Drawing causal conclusions from survey data | A survey doesn't intervene, so it is easy to see causal relationships that aren't there[^torchiano2017lessons-e2] |
| Saying only "we surveyed N developers" without stating the target population | Readers can't judge whom the conclusions apply to[^molleri2020empirically-e6][^ralph2020empirical-e251] |
| Casting a wide net on social media, then reporting "38% of developers use X" | A convenience sample can't support specific proportions[^baltes2022sampling-e17] |
| Double-barreled questions, leading wording, double negatives | The answers can't be interpreted, or are pushed toward one answer[^torchiano2017lessons-e9][^torchiano2017lessons-e11] |
| Measuring satisfaction or productivity with a single self-written item, or modifying an existing scale | Neither reliability nor validity is assured[^graziotin2021psychometrics-e1][^graziotin2021psychometrics-e2] |
| Reporting only means for Likert data and using t-tests | Ordinal data doesn't meet the assumptions of these methods[^wagner2020challenges-e17] |
| Collecting email addresses from GitHub and mass-mailing invitations | It is ethically problematic and draws complaints[^wagner2020challenges-e9][^wagner2020challenges-e10] |

---

## 5. Further reading

- **Lessons learned from start to finish**: Torchiano et al. 2017. Short; walks through common pitfalls in the order "set goals, define the population, sample, design the questionnaire, recruit", with many examples of good and bad questions. The most useful thing to read before designing your first questionnaire.
- **Sampling, invitations, statistical analysis, and psychometrics**: Wagner et al. 2020. Based on experience with several rounds of international surveys; covers estimating sample size, ways of inviting, analyzing ordinal data, coding open-ended answers, and using scales.
- **Checklist**: Molléri et al. 2020. Built from 14 methodological sources; you can go through it item by item at the design stage, or use it to review other people's survey papers.
- **Sampling**: Baltes & Ralph 2022. Clearly explains the difference between representativeness and randomness, and gives concrete ways to reduce sampling bias in survey research.
- **Psychometrics**: Graziotin et al. 2021. Read it when you need to develop your own scale or assess an existing one; covers item analysis, factor analysis, reliability, and validity, with runnable R examples.
- **Classic guide**: Kitchenham & Pfleeger's *Personal Opinion Surveys* (2008) and their 2001–2002 article series are widely cited. We could not find a legitimately available full text, so this page doesn't cite them.

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e231]: SIGSOFT Questionnaire Surveys standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e231)
[^ralph2020empirical-e232]: SIGSOFT Questionnaire Surveys standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e232)
[^ralph2020empirical-e233]: SIGSOFT Questionnaire Surveys standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e233)
[^ralph2020empirical-e234]: SIGSOFT Questionnaire Surveys standard, Variations. [Evidence](../../sources/notes/ralph2020empirical.md#e234)
[^ralph2020empirical-e235]: SIGSOFT Questionnaire Surveys standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e235)
[^ralph2020empirical-e236]: SIGSOFT Questionnaire Surveys standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e236)
[^ralph2020empirical-e237]: SIGSOFT Questionnaire Surveys standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e237)
[^ralph2020empirical-e238]: SIGSOFT Questionnaire Surveys standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e238)
[^ralph2020empirical-e239]: SIGSOFT Questionnaire Surveys standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e239)
[^ralph2020empirical-e240]: SIGSOFT Questionnaire Surveys standard, Essential Attributes and footnote 3. [Evidence](../../sources/notes/ralph2020empirical.md#e240)
[^ralph2020empirical-e241]: SIGSOFT Questionnaire Surveys standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e241)
[^ralph2020empirical-e242]: SIGSOFT Questionnaire Surveys standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e242)
[^ralph2020empirical-e243]: SIGSOFT Questionnaire Surveys standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e243)
[^ralph2020empirical-e244]: SIGSOFT Questionnaire Surveys standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e244)
[^ralph2020empirical-e200]: SIGSOFT Questionnaire Surveys standard, Desirable Attributes and footnote 4. [Evidence](../../sources/notes/ralph2020empirical.md#e200)
[^ralph2020empirical-e245]: SIGSOFT Questionnaire Surveys standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e245)
[^ralph2020empirical-e246]: SIGSOFT Questionnaire Surveys standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e246)
[^ralph2020empirical-e247]: SIGSOFT Questionnaire Surveys standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e247)
[^ralph2020empirical-e248]: SIGSOFT Questionnaire Surveys standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e248)
[^ralph2020empirical-e249]: SIGSOFT Questionnaire Surveys standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e249)
[^ralph2020empirical-e250]: SIGSOFT Sampling Supplement, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e250)
[^ralph2020empirical-e251]: SIGSOFT Sampling Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e251)
[^ralph2020empirical-e252]: SIGSOFT Sampling Supplement, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e252)
[^ralph2020empirical-e253]: SIGSOFT Ethics (Studies with Human Participants) Supplement, footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e253)
[^ralph2020empirical-e254]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e254)
[^ralph2020empirical-e255]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e255)
[^ralph2020empirical-e256]: SIGSOFT Qualitative Surveys (Interview Studies) standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e256)
[^wagner2020challenges-e1]: Wagner et al. 2020, §2. [Evidence](../../sources/notes/wagner2020challenges.md#e1)
[^wagner2020challenges-e2]: Wagner et al. 2020, §2 summary. [Evidence](../../sources/notes/wagner2020challenges.md#e2)
[^wagner2020challenges-e3]: Wagner et al. 2020, §3. [Evidence](../../sources/notes/wagner2020challenges.md#e3)
[^wagner2020challenges-e4]: Wagner et al. 2020, §3. [Evidence](../../sources/notes/wagner2020challenges.md#e4)
[^wagner2020challenges-e33]: Wagner et al. 2020, §4. [Evidence](../../sources/notes/wagner2020challenges.md#e33)
[^wagner2020challenges-e5]: Wagner et al. 2020, §3.1. [Evidence](../../sources/notes/wagner2020challenges.md#e5)
[^wagner2020challenges-e7]: Wagner et al. 2020, §3.2. [Evidence](../../sources/notes/wagner2020challenges.md#e7)
[^wagner2020challenges-e6]: Wagner et al. 2020, §3.2. [Evidence](../../sources/notes/wagner2020challenges.md#e6)
[^wagner2020challenges-e8]: Wagner et al. 2020, §3.3. [Evidence](../../sources/notes/wagner2020challenges.md#e8)
[^wagner2020challenges-e9]: Wagner et al. 2020, §3.3. [Evidence](../../sources/notes/wagner2020challenges.md#e9)
[^wagner2020challenges-e10]: Wagner et al. 2020, §3.3. [Evidence](../../sources/notes/wagner2020challenges.md#e10)
[^wagner2020challenges-e11]: Wagner et al. 2020, §4. [Evidence](../../sources/notes/wagner2020challenges.md#e11)
[^wagner2020challenges-e12]: Wagner et al. 2020, §4. [Evidence](../../sources/notes/wagner2020challenges.md#e12)
[^wagner2020challenges-e13]: Wagner et al. 2020, §4. [Evidence](../../sources/notes/wagner2020challenges.md#e13)
[^wagner2020challenges-e14]: Wagner et al. 2020, §5. [Evidence](../../sources/notes/wagner2020challenges.md#e14)
[^wagner2020challenges-e15]: Wagner et al. 2020, §5.1. [Evidence](../../sources/notes/wagner2020challenges.md#e15)
[^wagner2020challenges-e16]: Wagner et al. 2020, §5.1. [Evidence](../../sources/notes/wagner2020challenges.md#e16)
[^wagner2020challenges-e17]: Wagner et al. 2020, §5.2. [Evidence](../../sources/notes/wagner2020challenges.md#e17)
[^wagner2020challenges-e18]: Wagner et al. 2020, §5.2. [Evidence](../../sources/notes/wagner2020challenges.md#e18)
[^wagner2020challenges-e19]: Wagner et al. 2020, §5.2. [Evidence](../../sources/notes/wagner2020challenges.md#e19)
[^wagner2020challenges-e20]: Wagner et al. 2020, §5.3. [Evidence](../../sources/notes/wagner2020challenges.md#e20)
[^wagner2020challenges-e21]: Wagner et al. 2020, §6. [Evidence](../../sources/notes/wagner2020challenges.md#e21)
[^wagner2020challenges-e22]: Wagner et al. 2020, §6. [Evidence](../../sources/notes/wagner2020challenges.md#e22)
[^wagner2020challenges-e23]: Wagner et al. 2020, §6 summary. [Evidence](../../sources/notes/wagner2020challenges.md#e23)
[^wagner2020challenges-e24]: Wagner et al. 2020, §6 summary. [Evidence](../../sources/notes/wagner2020challenges.md#e24)
[^wagner2020challenges-e25]: Wagner et al. 2020, §6. [Evidence](../../sources/notes/wagner2020challenges.md#e25)
[^wagner2020challenges-e26]: Wagner et al. 2020, §7. [Evidence](../../sources/notes/wagner2020challenges.md#e26)
[^wagner2020challenges-e27]: Wagner et al. 2020, §7. [Evidence](../../sources/notes/wagner2020challenges.md#e27)
[^wagner2020challenges-e28]: Wagner et al. 2020, §7.1. [Evidence](../../sources/notes/wagner2020challenges.md#e28)
[^wagner2020challenges-e29]: Wagner et al. 2020, §7.2. [Evidence](../../sources/notes/wagner2020challenges.md#e29)
[^wagner2020challenges-e30]: Wagner et al. 2020, §7.2. [Evidence](../../sources/notes/wagner2020challenges.md#e30)
[^wagner2020challenges-e31]: Wagner et al. 2020, §7.2. [Evidence](../../sources/notes/wagner2020challenges.md#e31)
[^wagner2020challenges-e32]: Wagner et al. 2020, §7.3. [Evidence](../../sources/notes/wagner2020challenges.md#e32)
[^torchiano2017lessons-e1]: Torchiano et al. 2017, §II. [Evidence](../../sources/notes/torchiano2017lessons.md#e1)
[^torchiano2017lessons-e2]: Torchiano et al. 2017, §III-A-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e2)
[^torchiano2017lessons-e3]: Torchiano et al. 2017, §III-A-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e3)
[^torchiano2017lessons-e4]: Torchiano et al. 2017, §III-A-2. [Evidence](../../sources/notes/torchiano2017lessons.md#e4)
[^torchiano2017lessons-e5]: Torchiano et al. 2017, §III-B-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e5)
[^torchiano2017lessons-e6]: Torchiano et al. 2017, §III-C. [Evidence](../../sources/notes/torchiano2017lessons.md#e6)
[^torchiano2017lessons-e7]: Torchiano et al. 2017, §III-C. [Evidence](../../sources/notes/torchiano2017lessons.md#e7)
[^torchiano2017lessons-e8]: Torchiano et al. 2017, §III-C. [Evidence](../../sources/notes/torchiano2017lessons.md#e8)
[^torchiano2017lessons-e9]: Torchiano et al. 2017, §III-D-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e9)
[^torchiano2017lessons-e10]: Torchiano et al. 2017, §III-D-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e10)
[^torchiano2017lessons-e11]: Torchiano et al. 2017, §III-D-2. [Evidence](../../sources/notes/torchiano2017lessons.md#e11)
[^torchiano2017lessons-e12]: Torchiano et al. 2017, §III-D-2. [Evidence](../../sources/notes/torchiano2017lessons.md#e12)
[^torchiano2017lessons-e13]: Torchiano et al. 2017, §III-D-3. [Evidence](../../sources/notes/torchiano2017lessons.md#e13)
[^torchiano2017lessons-e14]: Torchiano et al. 2017, §III-D-4. [Evidence](../../sources/notes/torchiano2017lessons.md#e14)
[^torchiano2017lessons-e15]: Torchiano et al. 2017, §III-D-4. [Evidence](../../sources/notes/torchiano2017lessons.md#e15)
[^torchiano2017lessons-e16]: Torchiano et al. 2017, §III-E-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e16)
[^torchiano2017lessons-e17]: Torchiano et al. 2017, §III-E-1. [Evidence](../../sources/notes/torchiano2017lessons.md#e17)
[^torchiano2017lessons-e18]: Torchiano et al. 2017, §III-E-2. [Evidence](../../sources/notes/torchiano2017lessons.md#e18)
[^torchiano2017lessons-e19]: Torchiano et al. 2017, §III-E-2. [Evidence](../../sources/notes/torchiano2017lessons.md#e19)
[^torchiano2017lessons-e20]: Torchiano et al. 2017, §III-E-2. [Evidence](../../sources/notes/torchiano2017lessons.md#e20)
[^baltes2022sampling-e2]: Baltes & Ralph 2022, §2.1.1. [Evidence](../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e5]: Baltes & Ralph 2022, §2.6. [Evidence](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e17]: Baltes & Ralph 2022, §2.6. [Evidence](../../sources/notes/baltes2022sampling.md#e17)
[^baltes2022sampling-e18]: Baltes & Ralph 2022, §2.1.4. [Evidence](../../sources/notes/baltes2022sampling.md#e18)
[^baltes2022sampling-e19]: Baltes & Ralph 2022, §6.2. [Evidence](../../sources/notes/baltes2022sampling.md#e19)
[^baltes2022sampling-e20]: Baltes & Ralph 2022, §6.3. [Evidence](../../sources/notes/baltes2022sampling.md#e20)
[^baltes2022sampling-e21]: Baltes & Ralph 2022, §6.3. [Evidence](../../sources/notes/baltes2022sampling.md#e21)
[^baltes2022sampling-e22]: Baltes & Ralph 2022, §7. [Evidence](../../sources/notes/baltes2022sampling.md#e22)
[^molleri2020empirically-e1]: Molléri et al. 2020, Abstract. [Evidence](../../sources/notes/molleri2020empirically.md#e1)
[^molleri2020empirically-e2]: Molléri et al. 2020, §2. [Evidence](../../sources/notes/molleri2020empirically.md#e2)
[^molleri2020empirically-e3]: Molléri et al. 2020, §2. [Evidence](../../sources/notes/molleri2020empirically.md#e3)
[^molleri2020empirically-e4]: Molléri et al. 2020, §2. [Evidence](../../sources/notes/molleri2020empirically.md#e4)
[^molleri2020empirically-e5]: Molléri et al. 2020, §3.3.1. [Evidence](../../sources/notes/molleri2020empirically.md#e5)
[^molleri2020empirically-e6]: Molléri et al. 2020, §4.2.1. [Evidence](../../sources/notes/molleri2020empirically.md#e6)
[^molleri2020empirically-e7]: Molléri et al. 2020, §4.2.1. [Evidence](../../sources/notes/molleri2020empirically.md#e7)
[^molleri2020empirically-e8]: Molléri et al. 2020, §4.2.1. [Evidence](../../sources/notes/molleri2020empirically.md#e8)
[^molleri2020empirically-e9]: Molléri et al. 2020, §4.2.1. [Evidence](../../sources/notes/molleri2020empirically.md#e9)
[^molleri2020empirically-e10]: Molléri et al. 2020, §3.3.2. [Evidence](../../sources/notes/molleri2020empirically.md#e10)
[^graziotin2021psychometrics-e1]: Graziotin et al. 2021, §1.1. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e1)
[^graziotin2021psychometrics-e2]: Graziotin et al. 2021, §1.1. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e2)
[^graziotin2021psychometrics-e3]: Graziotin et al. 2021, §6.0.1. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e3)
[^graziotin2021psychometrics-e4]: Graziotin et al. 2021, §13. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e4)
