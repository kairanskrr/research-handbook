# Psychology and cognitive science: field overview

This page explains how research actually runs in psychology and cognitive science: after the "replication crisis," what new rules the field has settled on for sample size, preregistration, open data, measurement, and reporting. For what applies in every field (choosing a topic, study design, writing, peer review, research ethics), see the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md); this page does not repeat them. For the research strategies psychology commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). Our sources come mainly from experimental and social psychology; clinical, developmental, neuroscience, and other areas have their own norms, so follow your target journal and your institution. Most of the ethics codes and reporting standards on this page come from the American Psychological Association; other countries and institutions have their own rules. `[Our analysis]`

**After reading this page, you should be able to:**

- explain what psychology's "replication crisis" was, and what the field changed afterward;
- recognize common questionable research practices, and know what preregistration, Registered Reports, and power analysis each guard against;
- know the norms for ethics, measurement, participants, and reporting in psychology research with people;
- name the research strategies psychology commonly uses, what evidence each relies on, and what standards it is judged by;
- avoid the mistakes newcomers make most often.

---

## How research works in this field

### A replication crisis changed the field

**Replicability** means whether someone else who repeats a study with the same methods gets the same result. In 2015 the Open Science Collaboration repeated 100 experimental and correlational studies published in three psychology journals. The replications used large enough samples and, where possible, the original materials. The result: the replication effects were on average only half the size of the original effects[^osc2015estimating-e1]; 97% of the original studies had statistically significant results, but only 36% of the replications did[^osc2015estimating-e2].

Before that, several events in 2010–2012 had already made experimental psychologists realize that the way they collected, analyzed, and reported data made **false positives** (concluding there is an effect when there isn't one) far too easy to publish[^nelson2018psychology-e1]. For example, the most prestigious journal in social psychology published nine experiments by Bem supporting the plainly absurd conclusion that people can be influenced by future events they cannot foresee[^nelson2018psychology-e3].

> **Where sources disagree: what do failed replications tell us?**
> - **Many findings are unreliable**: the share of significant results fell from 97% to 36% on replication, and effect sizes halved[^osc2015estimating-e1][^osc2015estimating-e2].
> - **You can't just call it "64% failed"**: Nelson and colleagues reclassified the replications with a method that can label a result "inconclusive." 36% were clear successes; of the other 64%, only 25% were clear failures and 49% were inconclusive. Many were inconclusive because the replications themselves had samples that were too small[^nelson2018psychology-e13]. The original project also noted that a failed replication could mean the conditions differed, the original result was a false positive, or the replication was a false negative[^osc2015estimating-e3].
>
> The original project's analysis also found that whether a replication succeeded depended more on how strong the original evidence was[^osc2015estimating-e5]. For a newcomer, both views lead to the same practice: **don't assume an effect is real just because it was published.** Before you cite it, check whether it has been independently replicated and how strong the original evidence was. `[Our analysis]`

### Where it went wrong: p-hacking and HARKing

**p-hacking** means running many analyses on the same data and reporting only the one that comes out "statistically significant," for example measuring several outcomes and reporting just one. "Statistically significant" roughly means the result is unlikely to have arisen by chance; the most common threshold in psychology is a p-value below 0.05 `[Our analysis]`. In their 2018 retrospective, Nelson, Simmons, and Simonsohn say their 2011 paper showed that this greatly increases the chance of publishing a false positive[^nelson2018psychology-e4]. In that paper's simulations, even the kinds of p-hacking considered "acceptable" at the time could raise the false-positive rate from 5% to 61%[^nelson2018psychology-e7].

What does it look like in practice? The authors describe it: when the first analysis is not significant, researchers keep "looking," for example by dropping "outliers" and trying again, analyzing only some participants or trials, or computing the outcome measure a different way[^nelson2018psychology-e6].

These practices are common. In a survey Nelson and colleagues cite, about 65% of respondents admitted to leaving out an outcome measure when reporting a study[^nelson2018psychology-e5]. p-hacking is common precisely because researchers usually don't realize they are doing it, or don't think it matters[^nelson2018psychology-e8]. A related problem is **hypothesizing after the results are known** (HARKing): presenting an after-the-fact explanation as if it were an advance prediction[^nosek2018preregistration-e2]. For why honesty alone can't prevent this, see the Part 2 chapter section [Be clear whether you are testing or exploring](../../02_from-project-to-study/01_question-to-evidence.md#5-be-clear-whether-you-are-testing-or-exploring) and [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#2-be-honest-with-the-evidence-dont-fool-yourself-report-all-results) in Throughout the project.

These practices are often grouped together as **questionable research practices** (QRPs) `[Our analysis]`. Flake and Fried point out that measurement has similar problems, which they call **questionable measurement practices** (QMPs): decisions researchers make about measurement that raise doubts about whether the measures, and the conclusions, hold up[^flake2020measurement-e1]. See the [Measurement](#measurement-use-scales-with-validity-evidence) section below.

### What changed afterward

Nelson and colleagues list the changes of recent years: authors share their data voluntarily; top journals regularly publish replications, both successful and failed; hundreds of researchers preregister; sample sizes have grown substantially; and some top journals require full disclosure of measures, conditions, excluded data, and the rule used to decide sample size[^nelson2018psychology-e2]. The table summarizes the main practices `[Our analysis, based on the sources below]`:

| Practice | What it is | What it mainly guards against |
|---|---|---|
| Full disclosure | Report all measures, all experimental manipulations, all excluded data, and how you decided on the sample size[^nelson2018psychology-e10]; you can put a standard disclosure statement directly in the paper[^nelson2018psychology-e11] | Selective reporting |
| Preregistration | Specifying your research questions and analysis plan before you see the results[^nosek2018preregistration-e1]; a time-stamped plan written before any data are analyzed[^nelson2018psychology-e12] | Choosing analyses, or forming hypotheses, after seeing the results |
| Registered Reports | Before the study begins, the protocol is peer reviewed and accepted in advance[^chambers2022past-e1] | Publication bias: journals and reviewers favoring "positive" results |
| Larger samples and power analysis | Working out in advance how many participants you need (see [below](#statistical-power-and-sample-size)) | Low statistical power[^nelson2018psychology-e9] |
| Open data and materials | For example the Open Science Framework (OSF), an online platform where researchers document, share, and report their studies[^nelson2018psychology-e15] | Others being unable to check or repeat the work |

**Preregistration in brief.** What preregistration is, why it doesn't stop you exploring, and what to do when you deviate from the plan are covered in the Part 2 chapter section [Should you make your plan public in advance?](../../02_from-project-to-study/01_question-to-evidence.md#6-should-you-publish-your-plan-in-advance) (whose sources are mostly from psychology), so we don't repeat them here.

**Registered Reports in brief.** Review happens in two stages. At Stage 1, before seeing any results, authors submit their research questions and methods to the journal for review[^nosek2018preregistration-e7]. If the protocol passes, it receives "in-principle acceptance": as long as you carry out the approved protocol and interpret the results in line with the evidence, the journal will publish the paper whether or not the hypotheses are supported[^chambers2022past-e2]. Stage 2 review looks only at whether the study was carried out well and as planned, not at whether the results are "important"[^nosek2018preregistration-e7]. The Center for Open Science (COS) page shows that more than 300 journals now offer the format, some as a regular article type and some only in a special issue[^cosregisteredreports-e1]. The costs: Stage 1 review usually delays the start of the study by several months[^chambers2022past-e6]; and the format is especially suited to studies that test hypotheses, not designed for purely exploratory research[^chambers2022past-e5].

> **Where sources disagree: how much have these reforms helped?**
> - **Signs that they work**: a psychology study cited by Chambers and colleagues found that only 4% of standard papers failed to confirm their first hypothesis, compared with 56% of Registered Reports[^chambers2022past-e3]. Registered Reports contain far more results that don't support the hypothesis.
> - **Too early to tell**: the difference could also be because authors use Registered Reports to test riskier hypotheses[^chambers2022past-e4]; and there is not yet enough experimental evidence that preregistration improves replicability[^nosek2018preregistration-e9]. Preregistration also does not eliminate bad statistical practice; it only makes it detectable[^nosek2018preregistration-e8].
>
> In practice: treat preregistration and full disclosure as basic skills, but don't assume that a preregistered conclusion must be reliable. `[Our analysis]`

### Publishing culture: journals, multi-study papers, and APA Style

Psychology publishes mainly in journal articles, unlike computer science, where conferences dominate `[Our analysis]`. Psychology papers usually follow "APA Style," set by the American Psychological Association (APA). It is meant for psychology, nursing, business, and other fields, and is aimed specifically at manuscripts submitted to journals and at student coursework[^apastyleabout-e2]; it dates back to 1929[^apastyleabout-e1]. APA Style is not just about citations and formatting: it asks authors to report the key details of their study protocol so readers can evaluate the results and others can repeat the study[^apastyleabout-e3].

Psychology papers often contain several studies[^nelson2018psychology-e14]. The papers selected by the Open Science Collaboration had on average about three studies each[^osc2015estimating-e6]. But more studies don't make a conclusion more reliable: if you are willing to put a few disappointing studies in the file drawer and leave them unpublished, it isn't hard to produce a false-positive paper in which all four experiments "worked"[^nelson2018psychology-e14].

Psychology also has large collaborative projects. The Open Science Collaboration's 100 replications were carried out by 270 authors[^osc2015estimating-e4]; since 2011, Nosek has also organized several projects in which independent labs jointly replicate published studies[^nelson2018psychology-e15].

**Authorship.** The APA ethics code requires authorship to reflect each person's actual contribution, regardless of status; merely holding a position such as department chair does not justify authorship[^apa2017ethical-e8]. On a multi-authored paper based mainly on a student's dissertation, the student should be first author except in unusual circumstances, and the advisor should discuss authorship with the student early on[^apa2017ethical-e9]. For general practice, see [Collaboration and advisors](../../08_throughout/collaboration_and_advisors.md#6-authorship-discuss-it-at-the-start-and-adjust-as-you-go) in Throughout the project.

---

## How this field differs from computer science

`[Our analysis, based on the sources below]`

| | Psychology and cognitive science | Computer science (see the [Computer science page](../computer-science/README.md)) |
|---|---|---|
| Main publication venue | Journals, usually in APA Style[^apastyleabout-e2] | Conference proceedings |
| A single paper | Often contains several studies[^nelson2018psychology-e14] | Often built around the evaluation of one new method or system |
| What is studied | Human mental processes; constructs such as depression, personality, and attitudes often cannot be observed directly[^flake2020measurement-e2] | Mostly human-made systems that can be run and measured directly |
| Reporting standards | The APA Journal Article Reporting Standards (JARS; see [below](#reporting-standards-apas-jars))[^apajars-e1] | Each conference's call for papers and artifact evaluation; in software engineering, the Empirical Standards of ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) |
| Focus of reproducibility | Preregistration, Registered Reports, sample size, full disclosure[^nelson2018psychology-e2] | Whether artifacts such as code and data run and reproduce the results |

---

## Norms and reporting standards in this field

### Ethics: the APA ethics code and institutional approval

For ethical principles shared across fields, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) in Throughout the project. The APA ethics code binds APA members and student affiliates[^apa2017ethical-e1]; if you are outside the US or not a member, it is often used as a reference, but what you actually do depends on the rules of your country and institution `[Our analysis]`. These are the parts of the code that matter most for doing research and are specific to psychology (general requirements such as informed consent, sharing data after publication, and correcting errors are covered at the link above):

- **Get approval first, then start.** When institutional approval is required, submit an accurate protocol, start only after it is approved, and conduct the research as approved[^apa2017ethical-e2]. Institutional approval here usually means approval from your institution's ethics committee. In the US this is an Institutional Review Board (IRB); names and requirements differ between countries `[Our analysis]`.
- **Students must have an alternative to participating.** When research participation is a course requirement or earns extra credit, an equitable alternative activity must be offered[^apa2017ethical-e4].
- **Deception needs strong justification.** Deception means not telling participants the truth in a study, for example hiding its real purpose `[Our analysis]`. It is allowed only when the study's value is high enough and no effective non-deceptive alternative is feasible[^apa2017ethical-e5]. You must explain the deception as early as possible (at the latest when data collection ends) and let participants withdraw their data[^apa2017ethical-e6].
- **Debriefing.** After the study, promptly tell participants about its nature, results, and conclusions, and correct any misconceptions they may have[^apa2017ethical-e7].

### Reporting standards: APA's JARS

The APA Journal Article Reporting Standards (JARS) specify what a paper must state clearly. They are meant for authors, reviewers, and editors, with the goal of making papers more rigorous[^apajars-e1]. There are three sets by type of data: JARS–Quant for numerical data and statistical analysis, JARS–Qual for data in the form of words and language, and JARS–Mixed for studies that combine the two[^apajars-e2]. A further set, JARS–REC, applies to all research[^apajars-e3] and covers how to discuss race, ethnicity, and culture `[Our analysis]`.

In the quantitative standards, these items relate directly to the reforms above:

- report the planned sample size, the achieved sample size, how the sample size was decided (power analysis and so on), and any interim analyses and stopping rules[^appelbaum2018journal-e2];
- define all measures, **including those collected but not reported in this paper**[^appelbaum2018journal-e3];
- report the criteria for excluding participants after data were collected[^appelbaum2018journal-e5];
- separate hypotheses, analyses, and conclusions into primary, secondary, and exploratory[^appelbaum2018journal-e1], and say for every hypothesis whether it was supported[^appelbaum2018journal-e6];
- if the study was registered, give the registration information[^appelbaum2018journal-e7].

The standards don't dictate how the tables should be used; they can serve as a formal checklist or just as a reference[^appelbaum2018journal-e8]. **Your target journal's author instructions come first.**

### Statistical power and sample size

**Statistical power** is the probability that a study will detect an effect when the effect really exists. Nelson and colleagues point to an old paradox: the vast majority of published studies are underpowered and should rarely produce significant results[^nelson2018psychology-e9], yet 97% of the 100 original studies sampled by the Open Science Collaboration had significant results[^osc2015estimating-e2]. In their view, p-hacking explains the paradox[^nelson2018psychology-e9].

- **Work out your sample size in advance.** An a-priori power analysis takes the effect size you want to detect, the significance level, and the power you want, and computes how many observations you need[^lakens2022sample-e2]. The key is to justify why you chose that effect size[^lakens2022sample-e3].
- **Don't plug in the effect size from a small pilot study or a published paper.** Effect sizes estimated from small pilot studies are very imprecise[^lakens2022sample-e4]; published effect sizes are inflated by publication bias[^lakens2022sample-e5].
- **Power analysis is not the only way to justify a sample size.** Lakens lists six: collecting data from (almost) the entire population, resource constraints, a-priori power analysis, accuracy of the estimate, heuristics, and openly admitting there is no justification[^lakens2022sample-e1]. Resources are always limited and should be assessed carefully[^lakens2022sample-e7]. "80% power" is only a convention, with no solid justification of its own[^lakens2022sample-e6].
- **Don't believe "20 per group is enough."** Simmons and colleagues' 2011 paper recommended at least 20 observations per condition. In their 2018 retrospective the same authors call that threshold ridiculously low: in a representative sample, 20 per group cannot even detect that men weigh more than women[^simmons2018false-e1].
- **Plan for a larger sample if you submit a Registered Report.** Many journals set a minimum power for Registered Reports, and the sample sizes needed are often large[^chambers2022past-e7], for example 90% power[^chambers2022past-e8].

### Measurement: use scales with validity evidence

Psychology mostly measures things like depression, personality traits, and attitudes (called **constructs**), which often cannot be observed directly. If the measurement itself is poor, no amount of rigorous design, advanced statistics, or large samples can rescue the study[^flake2020measurement-e2].

- **Reliability** is whether a measure is consistent; **validity** is whether it measures what you intend to measure. The APA ethics code requires instruments whose validity and reliability have been established with members of the population being tested[^apa2017ethical-e11]. JARS asks you to say whether a scale was previously validated or made up for this study, and where possible to report its reliability in your own sample[^appelbaum2018journal-e4].
- **Use existing scales as published, and cite the source.** This reduces the room for flexibility[^flake2020measurement-e4]. If you modify a scale, say how and why[^flake2020measurement-e6].
- **Watch out for "on-the-fly" scales.** In a review cited by Flake and Fried, 34 of the 43 scales examined (79%) appeared to have been created on the fly, with no other validity evidence in the original study[^flake2020measurement-e5]. For a 10-item questionnaire, there are 1,023 ways just to choose which items to sum[^flake2020measurement-e3], which leaves plenty of room to pick the result you want `[Our analysis]`.

### Participants: student samples and WEIRD samples

Henrich and colleagues point out that behavioral scientists routinely draw broad conclusions about human psychology in top journals from samples drawn only from Western, Educated, Industrialized, Rich, and Democratic (WEIRD) societies[^henrich2010weirdest-e1]. They cite Arnett's 2008 analysis: 96% of psychology samples came from Western industrialized countries, which make up only 12% of the world's population[^henrich2010weirdest-e3]; and 67% of the American samples consisted entirely of undergraduates taking psychology courses[^henrich2010weirdest-e4]. The problem is that WEIRD participants are particularly unusual compared with the rest of humanity, often sitting at the extreme end of the distribution[^henrich2010weirdest-e2]. Even visual perception varies between populations: for one classic visual illusion, American undergraduates were at the extreme end of the distribution, while San foragers of the Kalahari were not affected by it at all[^henrich2010weirdest-e6].

What to do: report in detail where your participants came from and who they were[^henrich2010weirdest-e8], and make the scope of your generalization match the strength of your evidence[^henrich2010weirdest-e7]. For general principles of sampling, see the Part 2 chapter section [Decide what you are studying: unit of analysis and population](../../02_from-project-to-study/01_question-to-evidence.md#3-decide-what-you-are-studying-unit-of-analysis-and-population).

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists the three strategies psychology (mainly experimental and social psychology) commonly uses. The grouping and the "What it looks like in psychology" column are our own summary; each standard represents only the source cited in its footnote `[Our analysis]`.

| Strategy | What it looks like in psychology | Common evidence and standards | How to do it |
|---|---|---|---|
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Testing hypotheses about mental processes with experiments | Specify research questions and the analysis plan before seeing the results[^nosek2018preregistration-e1]; an a-priori power analysis must justify the chosen effect size[^lakens2022sample-e3]; fully disclose measures, manipulations, excluded data, and the sample size rule[^nelson2018psychology-e10]; report, following JARS, how the sample size was decided and the exclusion criteria[^appelbaum2018journal-e2][^appelbaum2018journal-e5] | [Controlled experiments](../../06_methods/controlled_experiment.md) |
| [Measurement](../../05_research-strategies/measure.md) | Finding reliable ways to measure constructs such as depression, personality, and attitudes that can't be observed directly[^flake2020measurement-e2] | Use instruments whose validity and reliability have been established in the population tested[^apa2017ethical-e11]; use existing scales as published and cite the source[^flake2020measurement-e4]; report whether the scale was validated and its reliability in your sample[^appelbaum2018journal-e4] | [Scale development and measurement studies](../../06_methods/scale_development.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Pooling the effects of published studies with meta-analysis | Published effect sizes are inflated by publication bias[^lakens2022sample-e5], so take this into account before pooling `[Our analysis]` | [Systematic reviews and meta-analysis](../../06_methods/meta_analysis.md), [Review studies](../../06_methods/review_study.md) |

How to use this table `[Our analysis]`: whichever strategy you follow, psychology reviewers will look at how you justified your sample size and whether you disclosed everything. Measurement comes before the experiment: however impressive an experimental conclusion, it can't be rescued if the measurement is poor[^flake2020measurement-e2].

## Research methods common in this field

Most of the methods psychology uses overlap with the methods for research involving people in Research methods. Read the corresponding page first, then note the differences in the table below `[Our analysis]`:

| What you do | Research method | What to watch for in psychology |
|---|---|---|
| Experiments (including between-subjects and within-subjects designs) | [Controlled experiments](../../06_methods/controlled_experiment.md) | That page is about comparing how tools or methods affect people; psychology experiments study the mental processes themselves. Deception needs strong justification, and debriefing must follow the code[^apa2017ethical-e5][^apa2017ethical-e7] |
| Questionnaire and scale studies | [Questionnaire surveys](../../06_methods/questionnaire_survey.md), [Scale development and measurement studies](../../06_methods/scale_development.md) | When measuring psychological constructs, see [Measurement](#measurement-use-scales-with-validity-evidence) above |
| Interviews and other qualitative research | [Interview studies](../../06_methods/interview_study.md) | Report against JARS–Qual[^apajars-e2] |
| Replication studies, longitudinal studies | [Replication studies](../../06_methods/replication.md), [Longitudinal studies](../../06_methods/longitudinal_study.md) | Top journals now regularly publish replications[^nelson2018psychology-e2]; JARS–Quant has dedicated modules for replication and longitudinal studies[^appelbaum2018journal-e9] |

---

## Advice for newcomers

1. **Preregister by default.** Write down your research questions and analysis plan before you see the results[^nosek2018preregistration-e1]; if you deviate, report it honestly[^nosek2018preregistration-e5].
2. **Have a reason for your sample size.** Before you start, run a power analysis or state another justification, rather than "other people used this many"[^lakens2022sample-e1].
3. **Put a full disclosure statement in your paper**: how you decided the sample size, what data you excluded, and all manipulations and all measures[^nelson2018psychology-e11].
4. **Use existing scales with validity evidence, as published, and cite the source**[^flake2020measurement-e4].
5. **Before citing an effect, check whether it has been replicated.** Published does not mean reliable[^osc2015estimating-e1] `[Our analysis]`.
6. **If you rely mainly on student participants, don't phrase your conclusions as "how humans work"**[^henrich2010weirdest-e7].
7. **If you have a clear hypothesis to test and aren't in a hurry to collect data, consider a Registered Report.** Stage 1 review will delay your study by several months[^chambers2022past-e6]. Read your target journal's author guidelines first, then fill in the protocol template[^cosregisteredreports-e2].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| When a result isn't significant, switching outcomes, dropping "outliers," or analyzing only some participants until it is | This is p-hacking, and it greatly raises the false-positive rate[^nelson2018psychology-e6][^nelson2018psychology-e7] |
| Rewriting your hypothesis after seeing the results so that you "predicted" them | It presents an after-the-fact explanation as an advance prediction (HARKing)[^nosek2018preregistration-e2] |
| Reporting only the outcomes that came out well, without mentioning measures you collected but didn't use | JARS requires you to report all measures, including unused ones[^appelbaum2018journal-e3] |
| Preregistering, but not reporting all the planned analyses | It is still selective reporting[^nosek2018preregistration-e6] |
| Computing sample size from an effect size estimated in a small pilot study | The estimate is very imprecise[^lakens2022sample-e4] |
| Making up a few items as a "scale" without reporting reliability or validity | No one can tell what you actually measured[^flake2020measurement-e5][^appelbaum2018journal-e4] |
| Using an undergraduate sample and writing conclusions about "people" | WEIRD participants are often at the extreme end[^henrich2010weirdest-e2]; such generalizations are common even in top journals such as *Nature* and *Science*[^henrich2010weirdest-e5] |
| Making participation in studies the only way for students to earn course credit | An equitable alternative activity must be offered[^apa2017ethical-e4] |
| Miscopying or miscalculating statistical results in the paper | In a check cited by Nelson and colleagues, 54% of papers had at least one error, and 12% had at least one error that changed whether a result was significant[^nelson2018psychology-e16] |
| Making the advisor or department chair first author instead of the student who did the work | Authorship must reflect actual contribution, regardless of position[^apa2017ethical-e8] |

---

## Further reading

The reasons for each recommendation are our own analysis.

- **Nelson, Simmons & Simonsohn 2018, Psychology's Renaissance**: the story of the replication crisis and the reforms that followed. If you want to understand p-hacking and preregistration, read this first.
- **Open Science Collaboration 2015**: the original report on the 100 replications; shows how a large replication project is designed and run.
- **Nosek et al. 2018, The preregistration revolution**: what preregistration is, and how to handle practical problems such as deviating from the plan.
- **Chambers & Tzavella 2022**: the history, evidence, and limitations of Registered Reports, with advice for authors.
- **Lakens 2022, Sample Size Justification**: six ways to justify a sample size, and how to do a power analysis.
- **Flake & Fried 2020**: questionable measurement practices, with a list of questions for reporting measurement transparently.
- **Henrich, Heine & Norenzayan 2010**: the classic paper on the WEIRD sample problem.
- **Section 8 of the APA ethics code, and JARS**: read them side by side with your work before you run a study and before you write the paper.

[^osc2015estimating-e1]: Open Science Collaboration 2015, Abstract. [Evidence](../../../sources/notes/osc2015estimating.md#e1)
[^osc2015estimating-e2]: Open Science Collaboration 2015, Abstract. [Evidence](../../../sources/notes/osc2015estimating.md#e2)
[^osc2015estimating-e3]: Open Science Collaboration 2015, Introduction. [Evidence](../../../sources/notes/osc2015estimating.md#e3)
[^osc2015estimating-e4]: Open Science Collaboration 2015, Method. [Evidence](../../../sources/notes/osc2015estimating.md#e4)
[^osc2015estimating-e5]: Open Science Collaboration 2015, Abstract. [Evidence](../../../sources/notes/osc2015estimating.md#e5)
[^osc2015estimating-e6]: Open Science Collaboration 2015, Sampling frame and study selection. [Evidence](../../../sources/notes/osc2015estimating.md#e6)
[^nelson2018psychology-e1]: Nelson, Simmons, Simonsohn 2018, Abstract. [Evidence](../../../sources/notes/nelson2018psychology.md#e1)
[^nelson2018psychology-e2]: Nelson et al. 2018, Introduction. [Evidence](../../../sources/notes/nelson2018psychology.md#e2)
[^nelson2018psychology-e3]: Nelson et al. 2018, The Renaissance Begins. [Evidence](../../../sources/notes/nelson2018psychology.md#e3)
[^nelson2018psychology-e4]: Nelson et al. 2018, The Renaissance Begins. [Evidence](../../../sources/notes/nelson2018psychology.md#e4)
[^nelson2018psychology-e5]: Nelson et al. 2018, The Renaissance Begins. [Evidence](../../../sources/notes/nelson2018psychology.md#e5)
[^nelson2018psychology-e6]: Nelson et al. 2018, P-Hacking Explains an Old Paradox. [Evidence](../../../sources/notes/nelson2018psychology.md#e6)
[^nelson2018psychology-e7]: Nelson et al. 2018, P-Hacking Explains an Old Paradox. [Evidence](../../../sources/notes/nelson2018psychology.md#e7)
[^nelson2018psychology-e8]: Nelson et al. 2018, False Positives Are Bad. [Evidence](../../../sources/notes/nelson2018psychology.md#e8)
[^nelson2018psychology-e9]: Nelson et al. 2018, P-Hacking Explains an Old Paradox. [Evidence](../../../sources/notes/nelson2018psychology.md#e9)
[^nelson2018psychology-e10]: Nelson et al. 2018, Disclosure. [Evidence](../../../sources/notes/nelson2018psychology.md#e10)
[^nelson2018psychology-e11]: Nelson et al. 2018, footnote 11. [Evidence](../../../sources/notes/nelson2018psychology.md#e11)
[^nelson2018psychology-e12]: Nelson et al. 2018, Preregistration. [Evidence](../../../sources/notes/nelson2018psychology.md#e12)
[^nelson2018psychology-e13]: Nelson et al. 2018, Replications. [Evidence](../../../sources/notes/nelson2018psychology.md#e13)
[^nelson2018psychology-e14]: Nelson et al. 2018, P-Hacking Explains an Old Paradox. [Evidence](../../../sources/notes/nelson2018psychology.md#e14)
[^nelson2018psychology-e15]: Nelson et al. 2018, The Renaissance Begins. [Evidence](../../../sources/notes/nelson2018psychology.md#e15)
[^nelson2018psychology-e16]: Nelson et al. 2018, Unintentional Errors. [Evidence](../../../sources/notes/nelson2018psychology.md#e16)
[^simmons2018false-e1]: Simmons, Nelson & Simonsohn 2018, p. 256. [Evidence](../../../sources/notes/simmons2018false.md#e1)
[^nosek2018preregistration-e1]: Nosek et al. 2018, Abstract. [Evidence](../../../sources/notes/nosek2018preregistration.md#e1)
[^nosek2018preregistration-e2]: Nosek et al. 2018, Mental Constraints on Distinguishing Predictions and Postdictions. [Evidence](../../../sources/notes/nosek2018preregistration.md#e2)
[^nosek2018preregistration-e5]: Nosek et al. 2018, Challenge 1. [Evidence](../../../sources/notes/nosek2018preregistration.md#e5)
[^nosek2018preregistration-e6]: Nosek et al. 2018, Challenge 6. [Evidence](../../../sources/notes/nosek2018preregistration.md#e6)
[^nosek2018preregistration-e7]: Nosek et al. 2018, Advancing the Motive for Preregistration. [Evidence](../../../sources/notes/nosek2018preregistration.md#e7)
[^nosek2018preregistration-e8]: Nosek et al. 2018, Challenge 2. [Evidence](../../../sources/notes/nosek2018preregistration.md#e8)
[^nosek2018preregistration-e9]: Nosek et al. 2018, Preregistration Distinguishes Prediction and Postdiction. [Evidence](../../../sources/notes/nosek2018preregistration.md#e9)
[^chambers2022past-e1]: Chambers & Tzavella 2022, Abstract. [Evidence](../../../sources/notes/chambers2022past.md#e1)
[^chambers2022past-e2]: Chambers & Tzavella 2022, Introduction, author accepted manuscript, approx. p. 3. [Evidence](../../../sources/notes/chambers2022past.md#e2)
[^chambers2022past-e3]: Chambers & Tzavella 2022, Bias control, author accepted manuscript, approx. p. 7. [Evidence](../../../sources/notes/chambers2022past.md#e3)
[^chambers2022past-e4]: Chambers & Tzavella 2022, Bias control, author accepted manuscript, approx. p. 7. [Evidence](../../../sources/notes/chambers2022past.md#e4)
[^chambers2022past-e5]: Chambers & Tzavella 2022, Limitations and drawbacks, author accepted manuscript, approx. p. 12. [Evidence](../../../sources/notes/chambers2022past.md#e5)
[^chambers2022past-e6]: Chambers & Tzavella 2022, Stage 1 delay, author accepted manuscript, approx. p. 13. [Evidence](../../../sources/notes/chambers2022past.md#e6)
[^chambers2022past-e7]: Chambers & Tzavella 2022, Present, author accepted manuscript, approx. p. 6. [Evidence](../../../sources/notes/chambers2022past.md#e7)
[^chambers2022past-e8]: Chambers & Tzavella 2022, Box 1, author accepted manuscript, approx. p. 13. [Evidence](../../../sources/notes/chambers2022past.md#e8)
[^cosregisteredreports-e1]: Center for Open Science, Registered Reports page, Participating Journals. [Evidence](../../../sources/notes/cosregisteredreports.md#e1)
[^cosregisteredreports-e2]: Center for Open Science, Registered Reports page, Participating Journals. [Evidence](../../../sources/notes/cosregisteredreports.md#e2)
[^henrich2010weirdest-e1]: Henrich, Heine, Norenzayan 2010, Long Abstract. [Evidence](../../../sources/notes/henrich2010weirdest.md#e1)
[^henrich2010weirdest-e2]: Henrich et al. 2010, Long Abstract. [Evidence](../../../sources/notes/henrich2010weirdest.md#e2)
[^henrich2010weirdest-e3]: Henrich et al. 2010, §1.1 (quoting Arnett 2008). [Evidence](../../../sources/notes/henrich2010weirdest.md#e3)
[^henrich2010weirdest-e4]: Henrich et al. 2010, §1.1 (quoting Arnett 2008). [Evidence](../../../sources/notes/henrich2010weirdest.md#e4)
[^henrich2010weirdest-e5]: Henrich et al. 2010, §1.2. [Evidence](../../../sources/notes/henrich2010weirdest.md#e5)
[^henrich2010weirdest-e6]: Henrich et al. 2010, §2.1. [Evidence](../../../sources/notes/henrich2010weirdest.md#e6)
[^henrich2010weirdest-e7]: Henrich et al. 2010, §6.3. [Evidence](../../../sources/notes/henrich2010weirdest.md#e7)
[^henrich2010weirdest-e8]: Henrich et al. 2010, §6.3. [Evidence](../../../sources/notes/henrich2010weirdest.md#e8)
[^apa2017ethical-e1]: American Psychological Association Ethics Code, Introduction and Applicability. [Evidence](../../../sources/notes/apa2017ethical.md#e1)
[^apa2017ethical-e2]: American Psychological Association Ethics Code, 8.01. [Evidence](../../../sources/notes/apa2017ethical.md#e2)
[^apa2017ethical-e4]: American Psychological Association Ethics Code, 8.04(b). [Evidence](../../../sources/notes/apa2017ethical.md#e4)
[^apa2017ethical-e5]: American Psychological Association Ethics Code, 8.07(a). [Evidence](../../../sources/notes/apa2017ethical.md#e5)
[^apa2017ethical-e6]: American Psychological Association Ethics Code, 8.07(c). [Evidence](../../../sources/notes/apa2017ethical.md#e6)
[^apa2017ethical-e7]: American Psychological Association Ethics Code, 8.08(a). [Evidence](../../../sources/notes/apa2017ethical.md#e7)
[^apa2017ethical-e8]: American Psychological Association Ethics Code, 8.12(b). [Evidence](../../../sources/notes/apa2017ethical.md#e8)
[^apa2017ethical-e9]: American Psychological Association Ethics Code, 8.12(c). [Evidence](../../../sources/notes/apa2017ethical.md#e9)
[^apa2017ethical-e11]: American Psychological Association Ethics Code, 9.02(b). [Evidence](../../../sources/notes/apa2017ethical.md#e11)
[^apajars-e1]: American Psychological Association, APA Style website, JARS page, What are APA Style JARS? [Evidence](../../../sources/notes/apajars.md#e1)
[^apajars-e2]: American Psychological Association, APA Style website, JARS page, Guidelines. [Evidence](../../../sources/notes/apajars.md#e2)
[^apajars-e3]: American Psychological Association, APA Style website, JARS page, What are APA Style JARS? [Evidence](../../../sources/notes/apajars.md#e3)
[^apastyleabout-e1]: American Psychological Association, APA Style website, About APA Style. [Evidence](../../../sources/notes/apastyleabout.md#e1)
[^apastyleabout-e2]: American Psychological Association, APA Style website, About APA Style. [Evidence](../../../sources/notes/apastyleabout.md#e2)
[^apastyleabout-e3]: American Psychological Association, APA Style website, About APA Style. [Evidence](../../../sources/notes/apastyleabout.md#e3)
[^appelbaum2018journal-e1]: Appelbaum et al. 2018 (JARS–Quant), Abstract. [Evidence](../../../sources/notes/appelbaum2018journal.md#e1)
[^appelbaum2018journal-e2]: Appelbaum et al. 2018, Table 1, Method. [Evidence](../../../sources/notes/appelbaum2018journal.md#e2)
[^appelbaum2018journal-e3]: Appelbaum et al. 2018, Table 1, Method. [Evidence](../../../sources/notes/appelbaum2018journal.md#e3)
[^appelbaum2018journal-e4]: Appelbaum et al. 2018, Table 1, Psychometrics. [Evidence](../../../sources/notes/appelbaum2018journal.md#e4)
[^appelbaum2018journal-e5]: Appelbaum et al. 2018, Table 1, Data diagnostics. [Evidence](../../../sources/notes/appelbaum2018journal.md#e5)
[^appelbaum2018journal-e6]: Appelbaum et al. 2018, Table 1, Discussion. [Evidence](../../../sources/notes/appelbaum2018journal.md#e6)
[^appelbaum2018journal-e7]: Appelbaum et al. 2018, Table 1, Title page and author note. [Evidence](../../../sources/notes/appelbaum2018journal.md#e7)
[^appelbaum2018journal-e8]: Appelbaum et al. 2018, closing remarks. [Evidence](../../../sources/notes/appelbaum2018journal.md#e8)
[^appelbaum2018journal-e9]: Appelbaum et al. 2018, Abstract. [Evidence](../../../sources/notes/appelbaum2018journal.md#e9)
[^lakens2022sample-e1]: Lakens 2022, Abstract. [Evidence](../../../sources/notes/lakens2022sample.md#e1)
[^lakens2022sample-e2]: Lakens 2022, A-priori Power Analysis. [Evidence](../../../sources/notes/lakens2022sample.md#e2)
[^lakens2022sample-e3]: Lakens 2022, A-priori Power Analysis. [Evidence](../../../sources/notes/lakens2022sample.md#e3)
[^lakens2022sample-e4]: Lakens 2022, What is the Expected Effect Size? (citing Leon et al. 2011). [Evidence](../../../sources/notes/lakens2022sample.md#e4)
[^lakens2022sample-e5]: Lakens 2022, What is the Expected Effect Size? [Evidence](../../../sources/notes/lakens2022sample.md#e5)
[^lakens2022sample-e6]: Lakens 2022, A-priori Power Analysis. [Evidence](../../../sources/notes/lakens2022sample.md#e6)
[^lakens2022sample-e7]: Lakens 2022, Resource Constraints. [Evidence](../../../sources/notes/lakens2022sample.md#e7)
[^flake2020measurement-e1]: Flake & Fried 2020, Abstract. [Evidence](../../../sources/notes/flake2020measurement.md#e1)
[^flake2020measurement-e2]: Flake & Fried 2020, Introduction. [Evidence](../../../sources/notes/flake2020measurement.md#e2)
[^flake2020measurement-e3]: Flake & Fried 2020, Questioning the Validity of Psychological Science. [Evidence](../../../sources/notes/flake2020measurement.md#e3)
[^flake2020measurement-e4]: Flake & Fried 2020, Question 6. [Evidence](../../../sources/notes/flake2020measurement.md#e4)
[^flake2020measurement-e5]: Flake & Fried 2020, Question 6 (quoting Shaw et al.). [Evidence](../../../sources/notes/flake2020measurement.md#e5)
[^flake2020measurement-e6]: Flake & Fried 2020, Table 1. [Evidence](../../../sources/notes/flake2020measurement.md#e6)
