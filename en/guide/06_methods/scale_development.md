# Scale development and measurement studies

This page is about **studies whose product is the measurement instrument itself**: developing a new scale, translating and adapting a scale from another language, or building up reliability and validity evidence for an existing scale.

If you are only **using** an existing scale in your study, see the [Measurement](../07_fields/psychology/README.md#measurement-use-scales-with-validity-evidence) section of the psychology field overview; for how to sample, distribute and analyze a questionnaire, see [Questionnaire surveys](questionnaire_survey.md) (its Step 4 covers "using validated scales"). The difference: a questionnaire survey **uses a ruler to measure**; this page is about **making the ruler and checking whether it measures accurately**. `[Our analysis]`

**Scope** `[Our analysis]`: this page was originally written for [Psychology and cognitive science](../07_fields/psychology/README.md), and its sources are mainly psychometric literature: Boateng et al.'s primer on scale development for health, social and behavioral research; research on measurement validity in social and personality psychology; the International Test Commission's guidelines on translating and adapting tests; the American Psychological Association's reporting standards; and one psychometrics primer for software engineering (Graziotin et al.). The field overviews for [Education](../07_fields/education/README.md) and [Media and communication](../07_fields/media-communication/README.md) also point here. If you are developing a scale in another field, check your field's own conventions first.

**Strategies it usually serves**: [Measurement](../05_research-strategies/measure.md).


**After reading this page, you should be able to:** decide whether to develop a new scale, adapt one, or use an existing scale as is; carry out scale development step by step (define the construct, write items, expert review, cognitive interviews, pilot testing, factor analysis, reliability, validity); explain why reporting a single Cronbach's alpha is not enough and when you must test measurement invariance; know what the International Test Commission's guidelines require when you translate and adapt a scale; and recognize and avoid questionable measurement practices.

---

## 1. What this kind of study is, and when to use it

Things like depression, self-esteem and attitudes are **constructs**: they cannot be observed directly (see the [Measurement](../07_fields/psychology/README.md#measurement-use-scales-with-validity-evidence) section of the psychology field overview). A scale is a set of items that measures a construct indirectly[^boateng2018best-e1]. A scale development study asks: "Can scores on this set of items be interpreted as scores on this construct?" The split in the table below is our own analysis.

| | Use an existing scale | Translate and adapt a scale | Develop a new scale |
|---|---|---|---|
| When | An existing scale fits your construct and population | Good scales exist only in another language or for another culture | There really is no suitable scale |
| Main work | Choose the scale, use it as published, report reliability in your sample | Get permission, translate, pilot test, test equivalence | All the steps in Section 2 of this page |
| Main guidance | [Psychology field overview: Measurement](../07_fields/psychology/README.md#measurement-use-scales-with-validity-evidence) | The International Test Commission's guidelines on translation and adaptation (see Step 10) | This page |

**Look for an existing scale first.** Developing and validating a scale can take years, so before you start, search the literature for validated scales[^graziotin2021psychometrics-e4]. If similar scales exist, you need to explain why you are developing a new one and how it differs from the existing ones[^boateng2018best-e3].

**Two concepts that are easy to misunderstand.** **Reliability** is roughly how consistent the scores are `[Our analysis]`. **Validity**, as defined by the *Standards for Educational and Psychological Testing*, issued jointly by the American Educational Research Association, the American Psychological Association and the National Council on Measurement in Education (we have not read the original; this is as quoted by Graziotin et al.), is "the degree to which evidence and theory support the interpretation of test scores for proposed uses of tests"[^graziotin2021psychometrics-e11]. Neither is **a fixed property of the scale itself**: the American Psychological Association's Journal Article Reporting Standards for quantitative research (JARS, which set out what a psychology paper must report) state that reliability refers to scores in a particular sample, and validity refers to a particular interpretation of scores[^appelbaum2018journal-e10]. So "this scale has already been validated" does not excuse you from checking again in a new sample or for a new use `[Our analysis]`.

**The overall process.** In 2018 Boateng et al. wrote an introductory review of scale development for health, social and behavioral research. It divides the work into three phases (item development, scale development, scale evaluation) with nine steps in all; the last phase tests dimensionality, reliability and validity[^boateng2018best-e2]. The construct validation process described by Hussey and Hughes also has three phases: first identify and define the construct; then establish the scale's own measurement properties through quantitative analyses such as item analysis, factor analysis, internal consistency, stability and measurement invariance; and finally an **external phase** that looks at convergent and discriminant relations with other measures[^hussey2020hidden-e2]. The steps below combine the two accounts `[Our analysis]`.

---

## 2. How to do it

### Step 1: Define the construct clearly first

**How:** Read the literature and write down a definition of the construct and the aspects (dimensions) it includes. Settle this before you write any items[^boateng2018best-e3]. **Why:** If the construct is not clearly defined at the start, every later measurement decision becomes hard, and the vagueness leaves room to exploit it, knowingly or not[^flake2020measurement-e7].

**Where people go wrong:** The concept and definition of the construct are never sorted out; or the focus is too narrow and misses important aspects of the construct, which is called "construct underrepresentation"[^boateng2018best-e7]. Being misled by names: similar names don't mean two measures measure the same thing, and different names don't mean they measure different things[^flake2020measurement-e8]. When you check existing scales, read the items, not just the names `[Our analysis]`.

### Step 2: Write an item pool much larger than the final scale

**How:**
- Combine two approaches. Boateng et al. consider it best practice to combine deductive and inductive methods when defining the construct and generating items[^boateng2018best-e4]. Deductive roughly means starting from theory and existing scales; inductive means starting from how the target population itself talks, in interviews and focus groups `[Our analysis]`.
- Write plenty of items. The recommendation Boateng et al. cite is that the initial pool should be at least twice as long as the final scale[^boateng2018best-e5]; Graziotin et al. suggest 6 to 10 items for each intended dimension[^graziotin2021psychometrics-e5]. Many items will be dropped later, so err on the side of too many `[Our analysis]`.
- Keep the wording simple and unambiguous; items should not be offensive or biased with respect to gender, religion, ethnicity, race, economic status, sexual orientation or other social identities[^boateng2018best-e6].

### Step 3: Have experts review the content

**How:** Ask experts who know the construct to judge each item: does it measure the construct as you defined it? The experts should be **independent of the people who wrote the items**, typically 5 to 7 of them; ideally combine the judgments of experts and of the target population[^boateng2018best-e8]. This step builds evidence for **content validity** `[Our analysis]`. **Where people go wrong:** Asking only people in your own lab. They think the way you do, so they won't see what the items miss or what they include that doesn't belong `[Our analysis]`.

### Step 4: Use cognitive interviews to check that items are understood correctly

**How:** Have a few members of the target population answer the draft items, then ask them to say what they were thinking as they answered[^boateng2018best-e9]. Boateng et al. consider 5 to 15 interviews in two or three rounds ideal for pretesting, or interviewing until nothing new comes up; report both the problems the interviews revealed and how you revised the items[^boateng2018best-e10]. For how to run interviews in general, see [Interview studies](interview_study.md). **Why:** You may think "I often feel exhausted" asks about mood, while a respondent is thinking about overtime. You only find out by hearing them say it `[Our analysis]`.

### Step 5: Pilot test and run an item analysis

**How:** Run a small pilot with the revised items. Our sources give two reference points for pilot sample size: an analysis cited by Graziotin et al. considers 30 people a reasonable minimum recommendation for piloting a psychological test[^graziotin2021psychometrics-e6]; the International Test Commission's guidelines, discussing pilots of adapted tests, say that an item analysis on a moderate sample (for example, 100 people) can provide very useful information[^itc2017guidelines-e6]. Then check each item's **corrected item-total correlation**, the correlation between the item and the total of the remaining items; Boateng et al. regard items below 0.30 as less than ideal and candidates for removal[^boateng2018best-e13]. Also check whether responses pile up at one end of the scale, and whether many people skip the item `[Our analysis]`.

**Where people go wrong:** Deciding which items to drop after looking at the data. It is better to set the rules for dropping and grouping items in advance[^flake2020measurement-e10].

### Step 6: Factor analysis: explore first, then confirm on a new sample

**Factor analysis** looks at how many shared dimensions (factors) underlie a set of items, and which dimension each item mainly belongs to. There are two kinds[^graziotin2021psychometrics-e7]:

| | Exploratory factor analysis | Confirmatory factor analysis |
|---|---|---|
| What it answers | How do the items naturally group? | Does a structure hypothesized in advance fit the data? |
| When to use it `[Our analysis]` | Early in development, when the structure is still uncertain | When you already have a hypothesized structure (from theory or an earlier exploration) |

**How:** First run an exploratory factor analysis on one sample and decide how many factors to keep; where possible, use methods such as parallel analysis to decide the number of factors[^boateng2018best-e15]. Then run a confirmatory factor analysis on **a separate, independent sample**. Boateng et al. say the ideal is to develop the scale on sample A and test it on an independent sample B[^boateng2018best-e12]; another common approach is to split one sample, using part for exploration and the rest for confirmation[^graziotin2021psychometrics-e8].

**Why:** The factors you find by exploration are only a "hypothesized structure". Many scales go straight from this step to computing reliability, skipping any test of the structure[^boateng2018best-e14]. Using the same data both to find a structure and to "confirm" it is like marking your own exam `[Our analysis]`.

> **Where sources disagree: what cutoffs decide whether the fit is good?** Boateng et al. list a set of common fit indices and cutoffs, for example root mean square error of approximation (RMSEA) ≤ 0.06, comparative fit index (CFI) ≥ 0.95, Tucker–Lewis index (TLI) ≥ 0.95, and standardized root mean square residual (SRMR) ≤ 0.08[^boateng2018best-e16]. Graziotin et al. point out that how to judge the fit of a confirmatory factor analysis has long been debated[^graziotin2021psychometrics-e9]; Hussey and Hughes explicitly say they do not advocate a single set of indices and cutoffs for everyone[^hussey2020hidden-e8].
>
> In practice: treat these cutoffs as reference points, not fixed pass marks. Write down in advance which indices and cutoffs you will use (see Step 11), and report the values of all the indices `[Our analysis]`.

> **Where sources disagree: how large a sample?** A common rule of thumb is at least 10 people per item; Boateng et al. also note that no single ratio of respondents to items works in every situation[^boateng2018best-e11].
>
> In practice: use the rule of thumb to estimate a lower bound, look at how many people similar scale studies used, and explain in your paper how you decided on the sample size `[Our analysis]`.

### Step 7: Reliability: don't report Cronbach's alpha alone

**Cronbach's alpha** measures the **internal consistency** of the items and is the most commonly used test[^hussey2020hidden-e4]; 0.70 is often treated as the acceptable threshold[^boateng2018best-e17]. But reporting it alone is far from enough:
- **Alpha's assumptions need testing separately.** Alpha rests on many assumptions, which can only be tested with analyses such as confirmatory factor analysis that fewer researchers run[^hussey2020hidden-e4].
- **A high alpha doesn't mean a good scale.** Hussey and Hughes used large-scale data from an online research project (144,496 experimental sessions) to examine 15 questionnaires commonly used in social and personality psychology, comprising 26 scales. On internal consistency alone, 89% of the scales looked good; when immediate and delayed test-retest reliability, factor structure, and measurement invariance across age and gender were considered together, only 4% were good on everything, by the cutoffs the authors used[^hussey2020hidden-e1].
- **Psychology relies too heavily on alpha.** As reported by Hussey and Hughes, a 2017 review by Flake et al. found that researchers often treat alpha as the only evidence of structural validity[^hussey2020hidden-e3]. As reported by Flake and Fried, Flake et al.'s 2017 review of 500 measures in the *Journal of Personality and Social Psychology* found 18 cases where two separate scales were combined into one on the strength of alpha[^flake2020measurement-e11].

**How:**
- Besides internal consistency, report **test-retest reliability**: when the same people are tested again after an interval, are their total scores consistent[^boateng2018best-e18]? In a longitudinal study, the retest interval should match the study's own measurement schedule[^appelbaum2018journal-e13].
- Consider reliability coefficients other than alpha. Boateng et al. mention that coefficients regarded as improvements on alpha, such as Raykov's rho, ordinal alpha and Revelle's beta, are gradually gaining acceptance[^boateng2018best-e17]. Our sources do not go into the mathematics of each coefficient; read a psychometrics textbook or ask a statistics instructor.
- Re-estimate reliability whenever you change items. As Graziotin et al. report from the *Standards for Educational and Psychological Testing*, adding or removing items, changing wording, or changing the spacing of response options all affect reliability[^graziotin2021psychometrics-e10].

### Step 8: Validity: gather evidence from several directions

Validity is not a number but a body of evidence. Boateng et al. describe validation as an ongoing process that starts with defining the construct and continues through testing its relations with other constructs[^boateng2018best-e19]. The table lists the kinds of evidence newcomers use most often. The grouping is our own analysis, based on the footnote in each row. The *Standards for Educational and Psychological Testing* give a full classification of validity evidence; we have not read the original, so go to it when you need the details.

| Evidence | What it answers | How |
|---|---|---|
| Content | Do the items cover every aspect of the construct? | Steps 1–4: definition, expert review, cognitive interviews |
| Internal structure | Do the dimensions of the items match your theory? | Steps 6 and 9: factor analysis, measurement invariance |
| Convergent | Does it correlate highly with other instruments that measure the same construct?[^boateng2018best-e20] | Administer existing scales at the same time and compute correlations |
| Discriminant | Is it not too highly correlated with constructs it should differ from?[^boateng2018best-e20] | Administer scales for related constructs at the same time |
| Known groups | Do two groups that existing knowledge says should differ actually score differently? | Boateng et al.'s example: households whose drinking water tested positive for *E. coli* scored higher on a water insecurity scale[^boateng2018best-e21] |
| Criterion | Are scores associated with an outcome (criterion) they should be related to?[^boateng2018best-e22] | Follow up later behavior or outcomes |

**Where people go wrong:** First, treating "the results replicate" as "it measures accurately". Hussey and Hughes warn that replicable does not mean valid[^hussey2020hidden-e6]. Second, substituting old validation results for new ones: many self-report scales are used in contexts and samples that differ from the original validation studies[^hussey2020hidden-e10]; JARS holds that it is best to estimate reliability and validity in your own sample[^appelbaum2018journal-e11].

### Step 9: Before comparing groups, test measurement invariance

**Measurement invariance** means a scale measures the same thing, with the same meaning, across groups (or across time points). If it does not hold, the construct has a different structure or meaning in different groups, and comparisons between groups are meaningless[^putnick2016measurement-e1]. **An example:** suppose crying and weight gain reflect depression only in women. Men might score lower on a depression scale simply because they cry less and gain less weight, even though in men those two items are unrelated to depression in the first place[^putnick2016measurement-e3].

**When you must do it:** Before comparing means across groups (for example, boys and girls) or between pretest and posttest[^putnick2016measurement-e2]. An intervention can itself change how participants understand the construct, so you also need to test invariance between pretest and posttest[^putnick2016measurement-e7].

**How:** Putnick and Bornstein list four levels, tested in order[^putnick2016measurement-e4]:
1. **Configural invariance**: the form of the model (the factor structure) is the same across groups;
2. **Metric invariance**: the factor loadings (how strongly each item is tied to its factor) are the same;
3. **Scalar invariance**: the item intercepts (or thresholds) are the same;
4. **Residual invariance**: the items' residual variances are the same.

Only after the first three hold can you compare latent means across groups[^putnick2016measurement-e5]. If invariance fails, dropping items or modifying the model after the fact is exploratory, and you need to keep that in mind when interpreting the results[^putnick2016measurement-e6].

**Why it is often ignored:** Hussey and Hughes point out that researchers usually cannot provide evidence of measurement invariance[^hussey2020hidden-e5]. Watch the item level too: when an item behaves differently across groups, this is called **differential item functioning**; it is not necessarily bias, but you need to find out why it happens[^graziotin2021psychometrics-e13]. A fair scale measures the same construct for everyone, and its scores mean the same thing[^graziotin2021psychometrics-e12].

### Step 10: Translation and adaptation: follow the International Test Commission's guidelines

Translating an English scale into Chinese does **not** make it ready to use. The second edition of the *Guidelines for Translating and Adapting Tests*, published by the International Test Commission, contains 18 guidelines in six categories: precondition, test development, confirmation, administration, scoring and interpretation, and documentation[^itc2017guidelines-e1]. The ones a newcomer most needs to remember `[Our analysis]`:
- **Get permission from the copyright holder** before you start adapting[^itc2017guidelines-e2].
- **First confirm that the construct is understood the same way in the new language and culture**; this is the basis for any cross-cultural comparison[^itc2017guidelines-e3].
- **Aim for functional equivalence, not literal equivalence.** Forward and back translation both have flaws, and on their own they are rarely enough to show that a translation is valid; relying only on back translation often produces a version that "back-translates easily but reads awkwardly"[^itc2017guidelines-e4]. An alternative is two independent forward translations, with a third independent translator or an expert panel identifying the discrepancies and reconciling them into a single version[^itc2017guidelines-e5].
- **Pilot test, run item analysis, reliability and small-scale validity studies, then revise**[^itc2017guidelines-e6]. The original version's reliability, validity and norms **do not automatically carry over to the translation**[^itc2017guidelines-e7].
- **Before comparing scores across groups, establish the corresponding level of measurement invariance**[^itc2017guidelines-e8].
- **Document every change** and the evidence supporting equivalence[^itc2017guidelines-e9].

### Step 11: Report what you did, and fix as much as possible in advance

**Questionable measurement practices** are decisions researchers make about measurement that raise doubts about whether the measurement and the conclusions hold up[^flake2020measurement-e1]. Just choosing which items to sum gives a great deal of leeway (for an example, see the [Measurement](../07_fields/psychology/README.md#measurement-use-scales-with-validity-evidence) section of the psychology field overview). Validity assessment has the same problem: Hussey and Hughes call it **v-hacking** (validity hacking), selectively choosing and reporting a combination of metrics, implementations and cutoffs so that a scale looks more valid[^hussey2020hidden-e7].

**How to guard against it:**
- **Put your measurement plan in your preregistration**: which indices, what cutoffs, what measurement model, and how decisions will be made[^hussey2020hidden-e9]. For preregistration in general, see the [psychology field overview](../07_fields/psychology/README.md#what-changed-afterward).
- **Report everything.** As reported by Flake and Fried, Flake et al.'s 2017 review of 433 scales used in *Journal of Personality and Social Psychology* papers found that 40% gave no source, 19% did not report the number of items, and 9% did not report the response options[^flake2020measurement-e9]. Your paper should state at least: the construct definition, all items and response options, how scores are computed, which items were dropped or changed and why, what the cognitive interviews found and what you changed[^boateng2018best-e10], and the results of every step of the analysis `[Our analysis]`.
- **Declare any modifications.** Modifying a scale is not forbidden; the problem is doing it without declaring it or giving a reason[^flake2020measurement-e12].
- **If the evidence is thin, say so as a limitation.** For a scale you developed yourself, at minimum explain why you built your own rather than using an existing one; if there is little validity evidence, discuss it as a limitation of the study[^flake2020measurement-e13]. JARS also asks you to state whether a scale was validated or created ad hoc for this study, to report reliability in your sample where possible, and to report convergent and discriminant validity where relevant[^appelbaum2018journal-e12].

If the measurement is wrong, no sample size and no amount of rigorous preregistration can make up for it: Flake and Fried say that even with all of that, we might still not know whether what we measured was depression[^flake2020measurement-e15]. For how to write about threats to validity in an ordinary study, see the Part 2 chapter [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md).

---

## 3. Checklist

**Must do** (the split into tiers is our own analysis)
- [ ] Searched for existing scales first and explained why you are developing a new one or adapting one[^boateng2018best-e3][^flake2020measurement-e13]
- [ ] Wrote down the construct definition and dimensions before writing items[^boateng2018best-e3]
- [ ] Had independent experts review the content[^boateng2018best-e8], ran cognitive interviews, and reported what you found and changed[^boateng2018best-e10]
- [ ] Reported reliability in your sample[^appelbaum2018journal-e12], not just Cronbach's alpha[^hussey2020hidden-e4]
- [ ] Reported convergent and discriminant validity evidence where relevant[^appelbaum2018journal-e12]
- [ ] Tested configural, metric and scalar invariance before comparing group means[^putnick2016measurement-e2][^putnick2016measurement-e5]
- [ ] For a translated or adapted scale, got copyright permission[^itc2017guidelines-e2] and re-tested reliability and validity in the target population[^itc2017guidelines-e6][^itc2017guidelines-e7]
- [ ] Stated and justified every change to items, item removal, or scoring[^flake2020measurement-e12]

**Better practice**
- [ ] Ran the confirmatory factor analysis on an independent sample[^boateng2018best-e12]
- [ ] Reported test-retest reliability[^boateng2018best-e18]
- [ ] Put the measurement plan (indices, cutoffs, model, decision rules) in a preregistration[^hussey2020hidden-e9]
- [ ] Translated with two independent forward translations plus reconciliation, not back translation alone[^itc2017guidelines-e4][^itc2017guidelines-e5]

**Fine to skip; not a flaw**
- Not collecting every kind of validity evidence in one study: validation is an ongoing process by nature[^boateng2018best-e19]. But state what is missing in your limitations[^flake2020measurement-e13].
- Running only an exploratory factor analysis when first developing a scale: Graziotin et al. say most authors do this and leave further testing to later independent studies[^graziotin2021psychometrics-e8]. Again, write it up as a limitation `[Our analysis]`.
- Not testing residual invariance: comparing latent means only requires the first three levels[^putnick2016measurement-e5].

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Developing your own scale without searching the literature | You may be reinventing the wheel, and developing and validating a scale can take years[^graziotin2021psychometrics-e4] |
| Using the same data both to explore and to "confirm" | What exploration finds is only a hypothesized structure; it must be tested on an independent sample[^boateng2018best-e14][^boateng2018best-e12] |
| Reporting a single alpha and calling the scale valid | 89% look "good" on internal consistency alone, but only 4% remain after a combined assessment (see Step 7)[^hussey2020hidden-e1] |
| Merging two scales into one because alpha is high | This is modifying the scale; doing it without declaring or justifying it threatens the conclusions[^flake2020measurement-e11][^flake2020measurement-e12] |
| Comparing means of men and women, or pretest and posttest, without testing invariance | The difference may be produced by the measurement[^putnick2016measurement-e1][^putnick2016measurement-e3] |
| Translating a scale with back translation only, or carrying over the original's reliability and validity | See Step 10[^itc2017guidelines-e4][^itc2017guidelines-e7] |
| Choosing indices and cutoffs after seeing the results to "prove" validity | This is exactly v-hacking[^hussey2020hidden-e7] |
| Developing your own scale but neither reporting validity evidence nor stating it as a limitation | At minimum explain why you built your own, and state the lack of evidence as a limitation[^flake2020measurement-e13] |
| Modifying a scale without saying so | Readers cannot judge whether the conclusions hold[^flake2020measurement-e12]; changing items often undermines the original scale's reliability and validity[^graziotin2021psychometrics-e1] |

---

## 5. Further reading

The reasons for recommending each item are our own analysis.
- **Boateng et al. 2018**: an open-access introductory review of scale development, with three phases and nine steps. Start here if you are developing a scale for the first time.
- **Flake & Fried 2020**: questionable measurement practices; check your methods section against it before you write.
- **Hussey & Hughes 2020**: how much "reporting only alpha" can hide, and v-hacking.
- **Putnick & Bornstein 2016**: the steps for testing measurement invariance and conventions for reporting it.
- **The International Test Commission's *Guidelines for Translating and Adapting Tests*, second edition**: go through it guideline by guideline when you translate and adapt a scale.
- **Graziotin et al. 2021**: a psychometrics primer written for software engineering researchers.
- We have not read McNeish 2018 ("Thanks coefficient alpha, we'll take it from here"), Flake, Pek and Hehman 2017, or the *Standards for Educational and Psychological Testing* in the original; everything on this page about the latter two is as reported by the sources above.

[^boateng2018best-e1]: Boateng et al. 2018, Introduction. [Evidence](../../sources/notes/boateng2018best.md#e1)
[^boateng2018best-e2]: Boateng et al. 2018, Scale development overview. [Evidence](../../sources/notes/boateng2018best.md#e2)
[^boateng2018best-e3]: Boateng et al. 2018, Step 1, Domain identification. [Evidence](../../sources/notes/boateng2018best.md#e3)
[^boateng2018best-e4]: Boateng et al. 2018, Step 1, Item generation. [Evidence](../../sources/notes/boateng2018best.md#e4)
[^boateng2018best-e5]: Boateng et al. 2018, Step 1, Item generation. [Evidence](../../sources/notes/boateng2018best.md#e5)
[^boateng2018best-e6]: Boateng et al. 2018, Step 1, Item generation. [Evidence](../../sources/notes/boateng2018best.md#e6)
[^boateng2018best-e7]: Boateng et al. 2018, Step 1, Item generation (common pitfalls). [Evidence](../../sources/notes/boateng2018best.md#e7)
[^boateng2018best-e8]: Boateng et al. 2018, Step 2, Evaluation by experts. [Evidence](../../sources/notes/boateng2018best.md#e8)
[^boateng2018best-e9]: Boateng et al. 2018, Step 3, Cognitive interviews. [Evidence](../../sources/notes/boateng2018best.md#e9)
[^boateng2018best-e10]: Boateng et al. 2018, Step 3, Cognitive interviews. [Evidence](../../sources/notes/boateng2018best.md#e10)
[^boateng2018best-e11]: Boateng et al. 2018, Step 4, Establishing the sample size. [Evidence](../../sources/notes/boateng2018best.md#e11)
[^boateng2018best-e12]: Boateng et al. 2018, Step 4, Determining the type of data to use. [Evidence](../../sources/notes/boateng2018best.md#e12)
[^boateng2018best-e13]: Boateng et al. 2018, Step 5, Inter-item and item-total correlations. [Evidence](../../sources/notes/boateng2018best.md#e13)
[^boateng2018best-e14]: Boateng et al. 2018, Step 6, Extraction of factors. [Evidence](../../sources/notes/boateng2018best.md#e14)
[^boateng2018best-e15]: Boateng et al. 2018, Step 6, Extraction of factors. [Evidence](../../sources/notes/boateng2018best.md#e15)
[^boateng2018best-e16]: Boateng et al. 2018, Step 7, Confirmatory factor analysis. [Evidence](../../sources/notes/boateng2018best.md#e16)
[^boateng2018best-e17]: Boateng et al. 2018, Step 8, Cronbach's alpha. [Evidence](../../sources/notes/boateng2018best.md#e17)
[^boateng2018best-e18]: Boateng et al. 2018, Step 8, Test–retest reliability. [Evidence](../../sources/notes/boateng2018best.md#e18)
[^boateng2018best-e19]: Boateng et al. 2018, Step 9, Tests of validity. [Evidence](../../sources/notes/boateng2018best.md#e19)
[^boateng2018best-e20]: Boateng et al. 2018, Step 9, Construct validity. [Evidence](../../sources/notes/boateng2018best.md#e20)
[^boateng2018best-e21]: Boateng et al. 2018, Step 9, Construct validity (known-groups comparison). [Evidence](../../sources/notes/boateng2018best.md#e21)
[^boateng2018best-e22]: Boateng et al. 2018, Step 9, Criterion validity. [Evidence](../../sources/notes/boateng2018best.md#e22)
[^hussey2020hidden-e1]: Hussey & Hughes 2020, Abstract. [Evidence](../../sources/notes/hussey2020hidden.md#e1)
[^hussey2020hidden-e2]: Hussey & Hughes 2020, Introduction. [Evidence](../../sources/notes/hussey2020hidden.md#e2)
[^hussey2020hidden-e3]: Hussey & Hughes 2020, Introduction (citing Flake et al. 2017). [Evidence](../../sources/notes/hussey2020hidden.md#e3)
[^hussey2020hidden-e4]: Hussey & Hughes 2020, Purpose of the Present Study. [Evidence](../../sources/notes/hussey2020hidden.md#e4)
[^hussey2020hidden-e5]: Hussey & Hughes 2020, Introduction. [Evidence](../../sources/notes/hussey2020hidden.md#e5)
[^hussey2020hidden-e6]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e6)
[^hussey2020hidden-e7]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e7)
[^hussey2020hidden-e8]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e8)
[^hussey2020hidden-e9]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e9)
[^hussey2020hidden-e10]: Hussey & Hughes 2020, Purpose of the Present Study. [Evidence](../../sources/notes/hussey2020hidden.md#e10)
[^putnick2016measurement-e1]: Putnick & Bornstein 2016, Abstract. [Evidence](../../sources/notes/putnick2016measurement.md#e1)
[^putnick2016measurement-e2]: Putnick & Bornstein 2016, Abstract. [Evidence](../../sources/notes/putnick2016measurement.md#e2)
[^putnick2016measurement-e3]: Putnick & Bornstein 2016, Introduction. [Evidence](../../sources/notes/putnick2016measurement.md#e3)
[^putnick2016measurement-e4]: Putnick & Bornstein 2016, Testing Measurement Invariance. [Evidence](../../sources/notes/putnick2016measurement.md#e4)
[^putnick2016measurement-e5]: Putnick & Bornstein 2016, Testing Measurement Invariance. [Evidence](../../sources/notes/putnick2016measurement.md#e5)
[^putnick2016measurement-e6]: Putnick & Bornstein 2016, Configural invariance. [Evidence](../../sources/notes/putnick2016measurement.md#e6)
[^putnick2016measurement-e7]: Putnick & Bornstein 2016, Introduction. [Evidence](../../sources/notes/putnick2016measurement.md#e7)
[^itc2017guidelines-e1]: International Test Commission 2017, Summary. [Evidence](../../sources/notes/itc2017guidelines.md#e1)
[^itc2017guidelines-e2]: International Test Commission 2017, PC-1. [Evidence](../../sources/notes/itc2017guidelines.md#e2)
[^itc2017guidelines-e3]: International Test Commission 2017, PC-2. [Evidence](../../sources/notes/itc2017guidelines.md#e3)
[^itc2017guidelines-e4]: International Test Commission 2017, TD-2. [Evidence](../../sources/notes/itc2017guidelines.md#e4)
[^itc2017guidelines-e5]: International Test Commission 2017, TD-2. [Evidence](../../sources/notes/itc2017guidelines.md#e5)
[^itc2017guidelines-e6]: International Test Commission 2017, TD-5. [Evidence](../../sources/notes/itc2017guidelines.md#e6)
[^itc2017guidelines-e7]: International Test Commission 2017, C-3. [Evidence](../../sources/notes/itc2017guidelines.md#e7)
[^itc2017guidelines-e8]: International Test Commission 2017, SSI-2. [Evidence](../../sources/notes/itc2017guidelines.md#e8)
[^itc2017guidelines-e9]: International Test Commission 2017, Doc-1. [Evidence](../../sources/notes/itc2017guidelines.md#e9)
[^flake2020measurement-e1]: Flake & Fried 2020, Abstract. [Evidence](../../sources/notes/flake2020measurement.md#e1)
[^flake2020measurement-e7]: Flake & Fried 2020, Question 1. [Evidence](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e8]: Flake & Fried 2020, Question 2. [Evidence](../../sources/notes/flake2020measurement.md#e8)
[^flake2020measurement-e9]: Flake & Fried 2020, Question 3 (quoting Flake et al. 2017). [Evidence](../../sources/notes/flake2020measurement.md#e9)
[^flake2020measurement-e10]: Flake & Fried 2020, Question 4. [Evidence](../../sources/notes/flake2020measurement.md#e10)
[^flake2020measurement-e11]: Flake & Fried 2020, Question 5 (quoting Flake et al. 2017). [Evidence](../../sources/notes/flake2020measurement.md#e11)
[^flake2020measurement-e12]: Flake & Fried 2020, Question 5. [Evidence](../../sources/notes/flake2020measurement.md#e12)
[^flake2020measurement-e13]: Flake & Fried 2020, Question 6. [Evidence](../../sources/notes/flake2020measurement.md#e13)
[^flake2020measurement-e15]: Flake & Fried 2020, Summary. [Evidence](../../sources/notes/flake2020measurement.md#e15)
[^graziotin2021psychometrics-e4]: Graziotin et al. 2021, §13. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e4)
[^graziotin2021psychometrics-e1]: Graziotin et al. 2021, §1.1. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e1)
[^graziotin2021psychometrics-e5]: Graziotin et al. 2021, §3. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e5)
[^graziotin2021psychometrics-e6]: Graziotin et al. 2021, §5. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e6)
[^graziotin2021psychometrics-e7]: Graziotin et al. 2021, §7. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e7)
[^graziotin2021psychometrics-e8]: Graziotin et al. 2021, §7.2. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e8)
[^graziotin2021psychometrics-e9]: Graziotin et al. 2021, §7.2. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e9)
[^graziotin2021psychometrics-e10]: Graziotin et al. 2021, §9. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e10)
[^graziotin2021psychometrics-e11]: Graziotin et al. 2021, §10 (quoting the Standards for Educational and Psychological Testing). [Evidence](../../sources/notes/graziotin2021psychometrics.md#e11)
[^graziotin2021psychometrics-e12]: Graziotin et al. 2021, §11. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e12)
[^graziotin2021psychometrics-e13]: Graziotin et al. 2021, §11.1. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e13)
[^appelbaum2018journal-e10]: Appelbaum et al. 2018, Changes in Table 1, Psychometrics. [Evidence](../../sources/notes/appelbaum2018journal.md#e10)
[^appelbaum2018journal-e11]: Appelbaum et al. 2018, Changes in Table 1, Psychometrics. [Evidence](../../sources/notes/appelbaum2018journal.md#e11)
[^appelbaum2018journal-e12]: Appelbaum et al. 2018, Table 1, Method — Psychometrics. [Evidence](../../sources/notes/appelbaum2018journal.md#e12)
[^appelbaum2018journal-e13]: Appelbaum et al. 2018, Table 1, Method — Psychometrics. [Evidence](../../sources/notes/appelbaum2018journal.md#e13)
