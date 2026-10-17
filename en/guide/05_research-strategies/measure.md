# Measurement

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science. Where the page cites standards from psychology, metrology, nutritional epidemiology, catalysis chemistry, and other fields, they describe how that particular field works and are marked with their source. They are not universal rules for all research.

Say you work on "large language models and smart-contract security". Reading the papers, you notice something: everyone reports high detection rates, but you suspect the models had already "seen" the contracts used for evaluation. If what you ultimately want to show is "these numbers can't be trusted, and here is how to measure this properly", you are doing **measurement** research: your central claim is not about the thing being measured but about **the ruler itself**.

Treating measurement as a research strategy of its own is how this handbook groups things; our sources do not set it apart as a separate category (see [Where this grouping comes from](README.md#where-this-grouping-comes-from)). Different fields call it different things: computer science talks about evaluation and benchmarks, psychology about scale development, physics about metrology and measurement uncertainty. We put them together because they answer the same kind of question `[Our analysis]`. For terms, see [Key concepts](../00_start-here/key-concepts.md#research-strategy).

---

## 1. What kind of knowledge this research produces

Measurement research tells you **how to measure something accurately, where current ways of measuring it fall short, and by how much.**

Its central claim usually takes one of these forms `[Our analysis]`:

| What the claim looks like | Computer science example |
|---|---|
| An existing measure is flawed | "Many contracts in existing vulnerability benchmarks appear in the models' training data, so detection rates are inflated" |
| An existing metric is biased | "Measuring detection ability by 'number of tool warnings' counts the same vulnerability more than once" |
| A new measure is more valid | "A new benchmark built from contracts deployed after the models were trained better reflects real detection ability" |
| The measurement itself is unstable | "When two experts label vulnerabilities in the same set of contracts, their agreement is only moderate; the labels themselves are very noisy" |
| Measurement error changes the conclusion | "Once leakage is corrected for, large language models are no better than traditional static analysis tools" |

**How it differs from the other strategies:** [Comparative evaluation](compare_evaluate.md) asks "which is better, A or B?", and [Building and improving](build_improve.md) asks "is my new thing better?". Both assume the ruler is accurate. Measurement research is exactly the work of checking that ruler. So the same benchmark is a tool in someone else's paper and the object of study in yours. For how it differs from [Description](observe_describe.md), see the section "How to pick your main strategy" in [Research strategies](README.md#how-to-pick-your-main-strategy) `[Our analysis]`.

**Why it is worth doing:** problems with measurement are hard to fix later. As the psychology methods literature puts it, if you are not measuring what you mean to measure, no amount of rigorous design, advanced statistics, or sample size can correct the resulting wrong inferences[^flake2020measurement-e2]. In machine learning, evaluations steer the research community, and breakthroughs are often tied to big gains on some benchmark[^wei2024evals-e1]. If the ruler is crooked, the whole direction of a field can go crooked with it `[Our analysis]`.

**Write it down:** State your measurement claim in one sentence, and name the "ruler" it is about (which benchmark, metric, scale, or instrument).

## 2. What evidence is enough

A skeptical reviewer will press you on five things about a ruler. Your evidence needs to answer each of them `[Our analysis]`:

**① Have you clearly defined what you are measuring?** The international guide for measurement in physics, the *Guide to the Expression of Uncertainty in Measurement*, says a measurement begins by specifying what is to be measured, the method, and the procedure[^jcgm2008gum-e11]. The definition must be complete enough that, at the precision you need, it has a single value. To measure a steel bar about one meter long to the micrometer, for example, you have to state the temperature and pressure at which its length is defined[^jcgm2008gum-e12]. The psychology methods literature gives a similar warning: if the construct (a concept that can't be observed directly and can only be measured indirectly, such as depression or an attitude) is not clearly defined at the start, every later measurement decision becomes hard, and the vagueness leaves room for manipulation, intended or not[^flake2020measurement-e7]. In the contract example, you have to settle up front whether "detects a vulnerability" means naming the vulnerability type, pointing to the exact lines of code, or producing a working exploit `[Our analysis]`.

**② Does it measure what you mean to measure?** This is **construct validity**: whether what you actually measure really represents the concept you want to study[^runeson2009guidelines-e3]. The empirical standards for software engineering require benchmarking papers to discuss it[^ralph2020empirical-e100]. Psychology's journal reporting standards stress that validity is not a fixed property of an instrument; it applies to interpreting scores in a particular way for a particular use[^appelbaum2018journal-e10]. Common kinds of validity evidence in the scale development literature: the new measure correlates highly with other measures of the same concept (convergent validity) and does not correlate too highly with measures of things it should differ from (discriminant validity)[^boateng2018best-e20]; and it does find a difference between two groups known to differ. For example, households with E. coli in their drinking water scored higher on a water insecurity scale[^boateng2018best-e21].

**③ Is it stable?** This is **reliability**. For example, if the same people are measured again after some time, are their total scores consistent[^boateng2018best-e18]? If your data comes from human labeling, report how well the labelers agree. The qualitative methods literature broadly holds that plain percent agreement is not enough, because it does not account for agreement that happens by chance[^mcdonald2019reliability-e4]. When you build a benchmark for large language models, it should have few wrong reference answers[^wei2024evals-e3] and its grading must be extremely accurate[^wei2024evals-e7].

**④ How large is the error?** The international measurement guide requires that when you report a measurement result, you give some quantitative indication of how reliable it is; without that, results can't be compared with each other or with reference values[^jcgm2008gum-e1]. Systematic error, like random error, can't be eliminated, but it can often be reduced, and systematic effects you have identified can be corrected for[^jcgm2008gum-e18].

**⑤ Does the conclusion change with a different ruler?** Don't just point out the problem; show what it does to the results. We think this is the most convincing part of measurement research `[Our analysis]`. One example: a study re-examined 12 papers on civil war prediction. The 4 papers with errors were exactly the 4 that claimed complex machine learning models outperformed traditional logistic regression baselines; once the errors were corrected, the complex models did not do much better than decades-old logistic regression[^kapoor2023leakage-e8].

**Checking only one of these is not enough.** One study used data from about 144,000 experimental sessions to test 15 self-report questionnaires (26 scales in total) that are widely used in social and personality psychology. Judged on internal consistency alone (whether the items in a scale give consistent scores), 89% looked to have good validity. When internal consistency, test-retest reliability, factor structure, and measurement invariance across age and gender groups were all tested together, only 4% did[^hussey2020hidden-e1]. That result is for this particular set of scales and can't be carried over directly to other instruments, but it shows how badly a single index can mislead. The same study also points out that a result that replicates is not thereby measured validly[^hussey2020hidden-e6].

**The burden of proof is on you.** When machine learning is used for scientific research, it is the researchers making the scientific claim who must show there is no leakage[^kapoor2023leakage-e9]. Take "existing benchmarks are inflated by leakage" as the example `[Our analysis]`:

| What the reviewer will ask | Evidence you need |
|---|---|
| Is there really leakage? | For models with public training data: what share of the benchmark can be found in the training data[^sainz2023nlp-e4]. For models without: use the model's memorization to see whether it can reproduce benchmark samples[^sainz2023nlp-e5] |
| Is your detection method reliable? | Validate it on samples known to be leaked and samples known not to be; spot-check a batch by hand |
| Did leakage affect the conclusions? | Compare scores and rankings for several models and several tools before and after removing leaked samples |
| What makes the new benchmark better? | How it was built, how well the labelers agree, and why it is less prone to leakage |

**Write it down:** For your ruler, write one sentence for each of the five questions above: "I plan to answer this with the following evidence." Any question you can't answer is the part of the project you most need to solve first.

## 3. Common research methods

Measurement research has no method of its own. The methods below are commonly used to get the evidence `[Our analysis]`:

| Method | What it gives you | Where to look |
|---|---|---|
| Benchmarking | Checking whether a benchmark or metric measures what it is meant to; how to check for data contamination | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid) |
| Scale development | The full process: defining the construct, writing items, reliability, validity, measurement invariance | [Scale development and measurement studies](../06_methods/scale_development.md) |
| Experimental measurement | Defining the measurand, calibration, systematic effects, uncertainty budget | [Experimental measurement](../06_methods/experimental_measurement.md) |
| Questionnaire survey | How to choose validated scales when measuring abstract concepts | [Questionnaire surveys](../06_methods/questionnaire_survey.md#step-4-use-validated-scales-to-measure-abstract-concepts) |
| Replication study | Redo the study with different data or a different measure and see whether the original conclusion holds | [Replication studies](../06_methods/replication.md) |
| Methodological research and meta-science | Systematically surveying how well papers in a field do their measurement | [Methodology research and meta-science](../06_methods/meta_science.md) |

## 4. How it shapes the whole project

**When reading the literature:** Look beyond the results at **how each paper measured**: which benchmark it used, how its metrics are defined, whether it reports error. Many papers say too little about measurement. One review found that of 433 scales used in papers in the *Journal of Personality and Social Psychology*, 40% had no stated source[^flake2020measurement-e9]. The places where reporting is thin are often where a measurement study can start `[Our analysis]`.

**When choosing a topic:** First look in the literature for existing, validated measures. The software engineering guidelines on psychometrics warn that developing and validating a new instrument can take years[^graziotin2021psychometrics-e4]. If similar instruments exist and you still build a new one, explain why and how it differs from the existing ones[^boateng2018best-e3]. If you find a problem with someone else's evaluation, "pointing it out and fixing it" can be a project in itself; see [Converging on a project](../01_find-a-problem/05_converge.md#3-has-someone-already-done-it).

**When designing the study:**

- **Define first, then choose the ruler.** Two instruments with similar names don't necessarily measure the same thing, and two with different names don't necessarily measure different things[^flake2020measurement-e8].
- **Fix the rules in advance.** Which items to drop and how to form groups are best decided before you start[^flake2020measurement-e10]; which indices and thresholds you will use to judge validity can also go into the preregistration[^hussey2020hidden-e9].
- **Use different data to build the ruler and to test it.** The ideal in scale development is to develop the scale on sample A and test it on an independent sample B[^boateng2018best-e12]. In performance benchmarking of computer systems, the workloads used for calibration and for evaluation must not overlap at all[^heiserbenchmarking-e12].
- **Prevent data leakage.** When machine learning is used for scientific research, researchers have access to all the data while building the model, and this is exactly why leakage often occurs[^kapoor2023leakage-e3]. Training and test samples that are not independent also count as leakage, unless your claim is specifically about data with that same dependence[^kapoor2023leakage-e6]. In the contract example, if many copy-pasted near-duplicate contracts end up on both the training and the test side, scores will be inflated `[Our analysis]`.

**When running the study:** The measurement guide warns that evaluating uncertainty is not a routine task; it depends on a detailed understanding of the thing measured and of the measurement process[^jcgm2008gum-e6]. Blunders in recording or analyzing data are not covered by the uncertainty[^jcgm2008gum-e5], so you have to catch them by checking your work `[Our analysis]`. When you build a benchmark for large language models, you can keep both a public and a private test set and watch whether models perform noticeably differently on the two[^wei2024evals-e9].

**When writing:** The measurement guide advises that when reporting a result and its uncertainty, it is better to give too much information than too little[^jcgm2008gum-e7]. Psychology's journal reporting standards ask you to say whether an instrument is validated or was made up for the study, and to report its reliability in your own sample where possible[^appelbaum2018journal-e4]. If you modified an existing instrument, say how and why[^flake2020measurement-e6]. If your own instrument has little validity evidence, discuss that as a limitation[^flake2020measurement-e13]. For how to write about validity and limitations, see [Validity and limitations](../02_do-the-project/04_validity-and-limits.md).

**Write it down:** List every ruler your project uses (benchmarks, metrics, labels, questionnaires) and mark each one "existing and validated", "existing but not validated", or "my own". Plan separate checks for the last two kinds.

## 5. Which fields have dedicated measurement standards

This table lists only fields for which this handbook's sources give evidence. A field missing from the list does not mean it neglects measurement; our sources simply do not cover it.

| Field | Evidence |
|---|---|
| Computer science (software engineering) | The empirical standards require benchmarking studies to discuss construct validity[^ralph2020empirical-e100]; questionnaire surveys must either use validated scales or analyze construct validity afterward[^ralph2020empirical-e236]; mining software repositories studies must explain and justify the metrics they use[^ralph2020empirical-e112] |
| Computer science (machine learning) | Data contamination inflates model performance[^sainz2023nlp-e2]; data leakage has been found in 17 scientific fields that use machine learning, affecting 294 papers[^kapoor2023leakage-e1] |
| Psychology | The ethics code requires instruments whose validity and reliability have been established for the population being tested[^apa2017ethical-e11]; there is a literature specifically on "questionable measurement practices"[^flake2020measurement-e1] |
| Physics and metrology | The *Guide to the Expression of Uncertainty in Measurement*, published by the Joint Committee for Guides in Metrology (JCGM), requires that a measurement result for a physical quantity come with a quantitative indication of its reliability[^jcgm2008gum-e1] |
| Chemistry (catalysis) | Researchers have proposed blind round-robin measurements, in which several research groups measure the same samples in turn, to establish realistic error bars[^bligaard2016benchmarking-e8] |
| Epidemiology and nutrition | Every study design has measurement error, and it always has to be considered when interpreting effects[^hernan2020whatif-e16]; when a single dietary exposure has only within-person random error, the estimated association between it and a health outcome is always attenuated[^nci2025dietprimer-e3] |

For details of each field's conventions, see the Fields section, for example [Computer science](../07_fields/computer-science/README.md) and [Psychology](../07_fields/psychology/README.md#measurement-use-scales-with-validity-evidence).

## 6. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Using a proxy instead of what you actually care about, with no justification | The evaluation checklist from the programming languages community says a proxy metric can stand in only when that is explicitly justified[^blackburn2018sigplan-e13] |
| Using a heuristic count instead of a real count | In fuzzing, for example, counting "unique crashes" badly overcounts bugs, so an apparent improvement may be fake[^klees2018evaluating-e4] |
| Reporting one consistency coefficient and declaring the measure valid | In the set of psychology scales above, 89% looked valid on internal consistency alone, but only 4% after a full test[^hussey2020hidden-e1] |
| Picking metrics and thresholds selectively so an instrument looks valid | This is called "v-hacking" (validity hacking)[^hussey2020hidden-e7] |
| Modifying a validated scale without saying so | Modifying it is not necessarily wrong; failing to disclose and justify the change is what threatens the conclusions[^flake2020measurement-e12]. Software engineering studies that borrow psychology scales often change the items, which destroys the original reliability and validity[^graziotin2021psychometrics-e1] |
| Reporting labeler agreement only as a percentage | It does not account for agreement by chance[^mcdonald2019reliability-e4] |
| Not checking whether the model has seen the evaluation data | If the model saw the benchmark during training, the experiment is completely invalid[^sainz2023nlp-e3] |
| Reporting values without error | The measurement guide points out that without an indication of reliability, results can't be compared[^jcgm2008gum-e1] |
| Pointing out a measurement problem without showing its effect on the conclusions | Readers can't tell how much the problem matters `[Our analysis]` |

## 7. Further reading

- **Flake & Fried 2020**, *Measurement Schmeasurement* (psychology): questionable measurement practices, with a table of questions for reporting measurement transparently[^flake2020measurement-e6].
- **Kapoor & Narayanan 2023** (machine-learning-based science): a taxonomy of data leakage, and "model info sheets" for checking each item[^kapoor2023leakage-e10].
- **Sainz et al. 2023** (natural language processing): how to define and detect data contamination in large language models.
- **Hussey & Hughes 2020** (psychology): the "hidden invalidity" of 15 widely used questionnaires, showing why looking at one index is not enough.
- **JCGM 100:2008** (metrology): the *Guide to the Expression of Uncertainty in Measurement*, often abbreviated GUM.
- **Boateng et al. 2018** (health and behavioral sciences): a review of the steps for developing and validating scales.

[^flake2020measurement-e1]: Flake & Fried 2020, Abstract. [Evidence](../../sources/notes/flake2020measurement.md#e1)
[^flake2020measurement-e2]: Flake & Fried 2020, Introduction. [Evidence](../../sources/notes/flake2020measurement.md#e2)
[^flake2020measurement-e6]: Flake & Fried 2020, Table 1. [Evidence](../../sources/notes/flake2020measurement.md#e6)
[^flake2020measurement-e7]: Flake & Fried 2020, Question 1. [Evidence](../../sources/notes/flake2020measurement.md#e7)
[^flake2020measurement-e8]: Flake & Fried 2020, Question 2. [Evidence](../../sources/notes/flake2020measurement.md#e8)
[^flake2020measurement-e9]: Flake & Fried 2020, Question 3 (paraphrasing Flake et al. 2017). [Evidence](../../sources/notes/flake2020measurement.md#e9)
[^flake2020measurement-e10]: Flake & Fried 2020, Question 4. [Evidence](../../sources/notes/flake2020measurement.md#e10)
[^flake2020measurement-e12]: Flake & Fried 2020, Question 5. [Evidence](../../sources/notes/flake2020measurement.md#e12)
[^flake2020measurement-e13]: Flake & Fried 2020, Question 6. [Evidence](../../sources/notes/flake2020measurement.md#e13)
[^wei2024evals-e1]: Wei 2024, para. 1. [Evidence](../../sources/notes/wei2024evals.md#e1)
[^wei2024evals-e3]: Wei 2024, common evaluation mistakes. [Evidence](../../sources/notes/wei2024evals.md#e3)
[^wei2024evals-e7]: Wei 2024, common evaluation mistakes. [Evidence](../../sources/notes/wei2024evals.md#e7)
[^wei2024evals-e9]: Wei 2024, test set contamination. [Evidence](../../sources/notes/wei2024evals.md#e9)
[^jcgm2008gum-e1]: JCGM 100:2008, 0.1. [Evidence](../../sources/notes/jcgm2008gum.md#e1)
[^jcgm2008gum-e5]: JCGM 100:2008, 3.4.7. [Evidence](../../sources/notes/jcgm2008gum.md#e5)
[^jcgm2008gum-e6]: JCGM 100:2008, 3.4.8. [Evidence](../../sources/notes/jcgm2008gum.md#e6)
[^jcgm2008gum-e7]: JCGM 100:2008, 7.1.4. [Evidence](../../sources/notes/jcgm2008gum.md#e7)
[^jcgm2008gum-e11]: JCGM 100:2008, 3.1.1. [Evidence](../../sources/notes/jcgm2008gum.md#e11)
[^jcgm2008gum-e12]: JCGM 100:2008, 3.1.3. [Evidence](../../sources/notes/jcgm2008gum.md#e12)
[^jcgm2008gum-e18]: JCGM 100:2008, 3.2.3. [Evidence](../../sources/notes/jcgm2008gum.md#e18)
[^runeson2009guidelines-e3]: Runeson & Höst 2009, §5.2.3. [Evidence](../../sources/notes/runeson2009guidelines.md#e3)
[^ralph2020empirical-e100]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e112]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e112)
[^ralph2020empirical-e236]: SIGSOFT Questionnaire Surveys standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e236)
[^appelbaum2018journal-e4]: Appelbaum et al. 2018, Table 1, Psychometrics. [Evidence](../../sources/notes/appelbaum2018journal.md#e4)
[^appelbaum2018journal-e10]: Appelbaum et al. 2018, Changes in Table 1, Psychometrics. [Evidence](../../sources/notes/appelbaum2018journal.md#e10)
[^apa2017ethical-e11]: American Psychological Association Ethics Code, 9.02(b). [Evidence](../../sources/notes/apa2017ethical.md#e11)
[^boateng2018best-e3]: Boateng et al. 2018, Step 1. [Evidence](../../sources/notes/boateng2018best.md#e3)
[^boateng2018best-e12]: Boateng et al. 2018, Step 4. [Evidence](../../sources/notes/boateng2018best.md#e12)
[^boateng2018best-e18]: Boateng et al. 2018, Step 8. [Evidence](../../sources/notes/boateng2018best.md#e18)
[^boateng2018best-e20]: Boateng et al. 2018, Step 9. [Evidence](../../sources/notes/boateng2018best.md#e20)
[^boateng2018best-e21]: Boateng et al. 2018, Step 9 (known-groups comparison). [Evidence](../../sources/notes/boateng2018best.md#e21)
[^mcdonald2019reliability-e4]: McDonald et al. 2019, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e4)
[^kapoor2023leakage-e1]: Kapoor & Narayanan 2023, Summary. [Evidence](../../sources/notes/kapoor2023leakage.md#e1)
[^kapoor2023leakage-e3]: Kapoor & Narayanan 2023, Leakage in modeling competitions. [Evidence](../../sources/notes/kapoor2023leakage.md#e3)
[^kapoor2023leakage-e6]: Kapoor & Narayanan 2023, Taxonomy [L3.2]. [Evidence](../../sources/notes/kapoor2023leakage.md#e6)
[^kapoor2023leakage-e8]: Kapoor & Narayanan 2023, Summary; civil war prediction case study. [Evidence](../../sources/notes/kapoor2023leakage.md#e8)
[^kapoor2023leakage-e9]: Kapoor & Narayanan 2023, Model info sheets. [Evidence](../../sources/notes/kapoor2023leakage.md#e9)
[^kapoor2023leakage-e10]: Kapoor & Narayanan 2023, Summary. [Evidence](../../sources/notes/kapoor2023leakage.md#e10)
[^hussey2020hidden-e1]: Hussey & Hughes 2020, Abstract. [Evidence](../../sources/notes/hussey2020hidden.md#e1)
[^hussey2020hidden-e6]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e6)
[^hussey2020hidden-e7]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e7)
[^hussey2020hidden-e9]: Hussey & Hughes 2020, Discussion. [Evidence](../../sources/notes/hussey2020hidden.md#e9)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e3]: Sainz et al. 2023, §3. [Evidence](../../sources/notes/sainz2023nlp.md#e3)
[^sainz2023nlp-e4]: Sainz et al. 2023, §5.1. [Evidence](../../sources/notes/sainz2023nlp.md#e4)
[^sainz2023nlp-e5]: Sainz et al. 2023, §5.2. [Evidence](../../sources/notes/sainz2023nlp.md#e5)
[^graziotin2021psychometrics-e1]: Graziotin et al. 2021, §1.1. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e1)
[^graziotin2021psychometrics-e4]: Graziotin et al. 2021, §13. [Evidence](../../sources/notes/graziotin2021psychometrics.md#e4)
[^heiserbenchmarking-e12]: Heiser, Same dataset for calibration and validation. [Evidence](../../sources/notes/heiserbenchmarking.md#e12)
[^blackburn2018sigplan-e13]: SIGPLAN checklist 2018, Indirect or inappropriate proxy metric. [Evidence](../../sources/notes/blackburn2018sigplan.md#e13)
[^klees2018evaluating-e4]: Klees et al. 2018, §9. [Evidence](../../sources/notes/klees2018evaluating.md#e4)
[^bligaard2016benchmarking-e8]: Bligaard et al. 2016, §2.2.1. [Evidence](../../sources/notes/bligaard2016benchmarking.md#e8)
[^hernan2020whatif-e16]: Hernán & Robins, Chapter 9, opening. [Evidence](../../sources/notes/hernan2020whatif.md#e16)
[^nci2025dietprimer-e3]: U.S. National Cancer Institute, Dietary Assessment Primer, Effects of Measurement Error. [Evidence](../../sources/notes/nci2025dietprimer.md#e3)
