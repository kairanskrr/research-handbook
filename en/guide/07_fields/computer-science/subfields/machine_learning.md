# Machine learning

> This page covers only the practices specific to this area. For practices common to all research, see the chapters of Parts 1 and 2 and the research strategies; for conventions shared across computer science, see the [computer science field overview](../README.md).

## What this area studies

Machine learning studies how computers can learn patterns from data and then use the learned models to make predictions or generate output. The common questions fall into two kinds (this split is our own):

- **Proposing a better method**: whether a new model architecture, training method, or optimization trick beats existing methods on accepted benchmarks, where it is better, and why.
- **Using machine learning to answer questions in other fields**: the REFORMS checklist (a reporting checklist for this kind of research) calls this "machine-learning-based science", in which a model's predictive performance is used as evidence for a scientific claim[^kapoor2024reforms-e1].

First, separate two things. Most machine learning research cares about predicting accurately on new samples not seen during training; traditional statistics cares more about estimating parameters that represent the true data-generating process[^kapoor2024reforms-e3]. Which one your paper is about decides what evidence you need.

This page also covers model-centered research in natural language processing (the area that gets computers to handle human language). The reason is that the two areas' review checklists share a common origin: the checklist of ACL Rolling Review (ARR, the centralized reviewing service of the Association for Computational Linguistics, ACL) is largely based on the 2021 paper checklist of NeurIPS (the Conference on Neural Information Processing Systems)[^arr2024responsible-e13].

## Main venues and timeline

Two venues serve as examples below:

- **NeurIPS**: a large machine learning conference; we use its 2025 rules;
- **ARR**: the centralized reviewing service for natural language processing; we use its checklist as updated for the October 2024 cycle.

They are only examples, not how every conference in the area works. Rules change every year, so **go by the guidelines of the conference you are submitting to, for that year**. NeurIPS 2025's deadlines, page limits, and double-blind and preprint rules are already covered in [Field overview: the life of a conference paper](../README.md#the-life-of-a-conference-paper) and [Double-blind review and preprints](../README.md#double-blind-review-and-preprints); here we add only what isn't covered elsewhere:

| Item | Rule (conference and year) |
|---|---|
| Checklist | NeurIPS 2025: papers without the checklist are desk-rejected[^neurips2025checklist-e1]; the checklist is published with the camera-ready version[^neurips2025checklist-e14]. ARR: filled in on the submission form[^arr2024responsible-e3] |
| Author response | NeurIPS 2025: you cannot submit a revised paper during the response period, only post discussion on the review platform[^neurips2025cfp-e11]; after that you can still answer follow-up questions[^neurips2025cfp-e12] |
| Open reviews | NeurIPS 2025: reviews and author responses for accepted papers are made public; rejected papers can opt in to making theirs public[^neurips2025cfp-e13] |
| Code | NeurIPS 2025: releasing code is not mandatory, but you must provide some reasonable path to reproduction[^neurips2025checklist-e8]; a paper can't be rejected just for not including code, unless the code is the contribution, such as a new open-source benchmark[^neurips2025checklist-e9] |

Reproduction has dedicated channels in this area. NeurIPS 2019 ran a reproducibility challenge, aiming to independently verify the empirical claims of accepted papers and to keep a public record of the results[^pineau2021improving-e8]. Some conferences also have calls specifically for reproducibility papers, and there is an open-access, peer-reviewed journal, ReScience C, dedicated to publishing reproducibility studies[^pineau2021improving-e9]. For how to do a replication study, see [Replication studies](../../../06_methods/replication.md).

## Common strategies and standards of evidence

The table below is our own summary of machine learning sources; each standard speaks only for the requirements of the source in its footnote. For the general requirements of a fair comparison (equal tuning effort, multiple runs, holding back data for a final test), see [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md#2-what-evidence-is-enough); here we cover only what is particular to this area.

| Strategy | What it looks like in this area | Evidence this area particularly values | How to do it |
|---|---|---|---|
| [Building and improving](../../../05_research-strategies/build_improve.md) | New models, new training methods | Compare both with simple baselines, to show the added complexity is needed[^lones2021avoid-e1], and with the current state of the art[^lones2021avoid-e2]; run ablation studies (remove components one at a time and see how results change) to show where the gain comes from[^lipton2019troubling-e4] | [Engineering research](../practices/engineering_research.md), [Optimization studies](../practices/optimization_study.md) |
| [Comparative evaluation](../../../05_research-strategies/compare_evaluate.md) | Comparing existing models on public benchmarks | Evaluate on multiple datasets[^lones2021avoid-e17]; when a whole community keeps comparing on the same test set, the top model may just have happened to overfit it[^lones2021avoid-e15] | [Benchmarking](../practices/benchmarking.md) |
| [Measurement](../../../05_research-strategies/measure.md) | Building new datasets or benchmarks; checking whether evaluations can be trusted | Check for data contamination (see below), which leads to overestimating model performance[^sainz2023nlp-e2]; different implementations of the same metric give different results, so state the implementation and version[^arr2024responsible-e10] | [Benchmarking: is the benchmark itself valid?](../practices/benchmarking.md#3-is-the-benchmark-itself-valid) |
| [Causal explanation](../../../05_research-strategies/explain_causality.md) | Explaining why a method works | The strongest empirical papers often include error analysis, ablation studies, and robustness checks[^lipton2019troubling-e8]; put speculation in a separate, clearly labeled section, apart from conclusions backed by evidence[^lipton2019troubling-e3] | [Data science: interpreting results](../../../06_methods/data_science.md#step-8-interpret-the-results-correlation-is-not-causation) |
| [Proof](../../../05_research-strategies/prove.md) | Learning theory, convergence, generalization bounds | NeurIPS 2025 checklist: state all assumptions in full and give complete proofs[^neurips2025checklist-e16] | [Theoretical research](../practices/theoretical_research.md) |

When you use machine learning to answer questions in another field, choose the strategy according to your central claim. For stating the target population and what the predicted variable stands for, and arguing that there is no leakage, see [Data science](../../../06_methods/data_science.md#step-1-state-the-claim-the-target-population-and-the-outcome-variable).

## Conventions specific to this area

### Reviewers look at the checklist

Both NeurIPS 2025 and ARR require you to fill in a checklist. ARR describes the checklist as a kind of FAQ (frequently asked questions) for reviewers, answering in advance questions that would otherwise come up during the author response period[^arr2024responsible-e4]. NeurIPS 2025 asks reviewers to treat the checklist as one of the factors in their evaluation[^neurips2025checklist-e2].

Items in the two checklists that bear directly on evidence (in each case, go by that conference's guidelines for the year):

- **Claims don't go beyond the results**: claims should match how far the results can be expected to generalize (NeurIPS 2025)[^neurips2025checklist-e12].
- **State limitations**: reviewers are explicitly told not to penalize authors for being honest about limitations (NeurIPS 2025)[^neurips2025checklist-e4].
- **Explain your error bars**: say what variability they capture, such as data splits or initialization[^neurips2025checklist-e5], and whether they are standard deviations or standard errors[^neurips2025checklist-e6]; say whether each result is from a single run, the maximum over several random seeds, or the mean (ARR)[^arr2024responsible-e9].
- **Hyperparameters**: say how they were chosen (NeurIPS 2025)[^neurips2025checklist-e15]; except in special cases, don't tune them on the held-out data used for evaluation (ARR)[^arr2024responsible-e8].
- **Compute**: say whether the whole project used more compute than the experiments in the paper, including failed experiments not reported in it (NeurIPS 2025)[^neurips2025checklist-e7]; ARR likewise asks you to cover all experiments, not just the final ones[^arr2024responsible-e7].

Answering "no" or "not applicable" is generally not grounds for rejection, as long as you give a justification[^neurips2025checklist-e3][^arr2024responsible-e2]. But ARR desk-rejects submissions that systematically neither point to the relevant section nor give a justification[^arr2024responsible-e1]. ARR advises reading the checklist early, because it will shape how you do the research[^arr2024responsible-e5].

### Watch out for data leakage and data contamination

For "use the test data only once, at the end" and how to prevent data leakage, see [Comparative evaluation: hold back data for the final test only](../../../05_research-strategies/compare_evaluate.md#keep-some-data-for-the-final-test-only) and [Data science: split the data before doing anything else](../../../06_methods/data_science.md#step-3-split-the-data-before-doing-anything-else-to-it).

Large language models bring a new problem: **data contamination**, where a model has been trained on a benchmark's test set and is then evaluated on that same benchmark[^sainz2023nlp-e1]. If the model has seen the evaluation data, the experiment is completely invalid[^sainz2023nlp-e3]. When you evaluate a large language model someone else trained, first check whether its training data might include your test set.

### Data, code, and assets

- **Say whose assets you used, and which version**: when you use other people's code, data, or models, state the version and the name of the license (NeurIPS 2025)[^neurips2025checklist-e13]; for language data, say which language it is, and the same goes for widely used benchmarks (ARR)[^arr2024responsible-e6].
- **Releasing code helps, but isn't enough**: having the original code doesn't mean the code is correct, and reimplementing from the paper's description is also very valuable[^pineau2021improving-e4]; some experiments need so much compute that most researchers can't reproduce them[^pineau2021improving-e5].
- **Reproducibility is rarely yes-or-no**: most reports from the NeurIPS 2019 reproducibility challenge described how far the method, the results, and the claims could each be reproduced[^pineau2021improving-e6].

### Ethics and societal impact

- **If you can see a path to misuse, say so**: the NeurIPS 2025 checklist acknowledges that many papers are foundational research not tied to a particular application[^neurips2025checklist-e18], but when you can see a direct path to harmful applications, you should point it out[^neurips2025checklist-e11]. The risks ARR lists also include the environmental impact of training very large models[^arr2024responsible-e16].
- **Annotators and participants**: under the NeurIPS Code of Ethics, people involved in collecting and curating data must be paid at least the minimum wage in your country[^neurips2025checklist-e10]; ARR asks you to state how much was paid for each task and how you estimated the time it took[^arr2024responsible-e11].
- **Ethics approval does not excuse you from discussing societal impact** (ARR)[^arr2024responsible-e12].
- **If you used a large language model**: rules differ by conference; for general practice and the NeurIPS 2025 example, see [Research integrity and ethics: when you use large language models and other tools, you are still responsible](../../../08_throughout/integrity_and_ethics.md#6-when-you-use-large-language-models-and-other-tools-you-are-still-responsible).

## Common mistakes

For general comparison mistakes (untuned baselines, single runs, repeatedly trying things on the test set), see [Comparative evaluation: common mistakes](../../../05_research-strategies/compare_evaluate.md#6-common-mistakes). Mistakes especially common in this area:

| Mistake | Why it's a problem |
|---|---|
| Adding many changes at once without an ablation study | You can't tell where the gain comes from; sometimes only one of the changes actually matters[^lipton2019troubling-e4] |
| Comparing only with the state of the art, not with simple baselines | It doesn't show that the added complexity is needed[^lones2021avoid-e1] |
| Evaluating on only one dataset | Multiple datasets make for a more rigorous evaluation[^lones2021avoid-e17] |
| Evaluating large language models without checking whether the benchmark is contaminated | Contamination leads to overestimating model performance[^sainz2023nlp-e2] |
| Presenting speculation as explanation | Readers will take it as settled[^lipton2019troubling-e2] |
| Leaving out limitations for fear of rejection | If reviewers find limitations you didn't mention, the outcome may be worse[^neurips2025checklist-e17] |
| Answering "no" on the checklist without a justification | ARR desk-rejects submissions that systematically give no justification[^arr2024responsible-e1] |

## Further reading

- **Lipton & Steinhardt 2019, Troubling Trends in Machine Learning Scholarship**: four common problems in machine learning papers, each with good and bad examples. Read it before writing your first paper.
- **Lones 2021, How to avoid machine learning pitfalls**: common pitfalls listed in order of data, modeling, evaluation, comparison, and reporting.
- **Kapoor & Narayanan 2023 and Kapoor et al. 2024 (the REFORMS checklist)**: a taxonomy of data leakage and a reporting checklist for machine-learning-based science. Read them when using machine learning to answer questions in another field.
- **Pineau et al. 2021, Improving Reproducibility in Machine Learning Research**: the background to the NeurIPS checklist and the reproducibility challenge.
- **The checklist of the conference you are submitting to, for that year**, such as the NeurIPS Paper Checklist Guidelines or ARR's Responsible NLP Research Checklist: every item comes with notes on how to answer it. Check your paper against it before submitting.
- Other areas in the same field: [Human-computer interaction](hci.md), [Systems](systems.md), [Security](security.md), [Software engineering](software_engineering.md), [Theory](theory.md), [Programming languages](programming_languages.md).

[^kapoor2024reforms-e1]: Kapoor et al. 2024, The scope of our claims. [Evidence](../../../../sources/notes/kapoor2024reforms.md#e1)
[^kapoor2024reforms-e3]: Kapoor et al. 2024, Module 1, 1c. [Evidence](../../../../sources/notes/kapoor2024reforms.md#e3)
[^arr2024responsible-e13]: ACL Rolling Review Responsible NLP Research Checklist, opening. [Evidence](../../../../sources/notes/arr2024responsible.md#e13)
[^neurips2025checklist-e1]: NeurIPS Paper Checklist Guidelines, opening paragraph. [Evidence](../../../../sources/notes/neurips2025checklist.md#e1)
[^neurips2025checklist-e14]: NeurIPS Paper Checklist Guidelines, instructions for answering. [Evidence](../../../../sources/notes/neurips2025checklist.md#e14)
[^arr2024responsible-e3]: ACL Rolling Review Responsible NLP Research Checklist, opening. [Evidence](../../../../sources/notes/arr2024responsible.md#e3)
[^neurips2025cfp-e11]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../../../sources/notes/neurips2025cfp.md#e11)
[^neurips2025cfp-e12]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../../../sources/notes/neurips2025cfp.md#e12)
[^neurips2025cfp-e13]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../../../sources/notes/neurips2025cfp.md#e13)
[^neurips2025checklist-e8]: NeurIPS Paper Checklist Guidelines, Item 4. [Evidence](../../../../sources/notes/neurips2025checklist.md#e8)
[^neurips2025checklist-e9]: NeurIPS Paper Checklist Guidelines, Item 5. [Evidence](../../../../sources/notes/neurips2025checklist.md#e9)
[^pineau2021improving-e8]: Pineau et al. 2021, §4. [Evidence](../../../../sources/notes/pineau2021improving.md#e8)
[^pineau2021improving-e9]: Pineau et al. 2021, §6. [Evidence](../../../../sources/notes/pineau2021improving.md#e9)
[^lones2021avoid-e1]: Lones 2021, §5.2. [Evidence](../../../../sources/notes/lones2021avoid.md#e1)
[^lones2021avoid-e2]: Lones 2021, §5.2. [Evidence](../../../../sources/notes/lones2021avoid.md#e2)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019, §3.2. [Evidence](../../../../sources/notes/lipton2019troubling.md#e4)
[^lones2021avoid-e17]: Lones 2021, §6.2. [Evidence](../../../../sources/notes/lones2021avoid.md#e17)
[^lones2021avoid-e15]: Lones 2021, §5.5. [Evidence](../../../../sources/notes/lones2021avoid.md#e15)
[^sainz2023nlp-e2]: Sainz et al. 2023, Abstract. [Evidence](../../../../sources/notes/sainz2023nlp.md#e2)
[^arr2024responsible-e10]: ACL Rolling Review Responsible NLP Research Checklist, C4. [Evidence](../../../../sources/notes/arr2024responsible.md#e10)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019, §5.1. [Evidence](../../../../sources/notes/lipton2019troubling.md#e8)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019, §3.1. [Evidence](../../../../sources/notes/lipton2019troubling.md#e3)
[^neurips2025checklist-e16]: NeurIPS Paper Checklist Guidelines, Item 3. [Evidence](../../../../sources/notes/neurips2025checklist.md#e16)
[^arr2024responsible-e4]: ACL Rolling Review Responsible NLP Research Checklist, opening. [Evidence](../../../../sources/notes/arr2024responsible.md#e4)
[^neurips2025checklist-e2]: NeurIPS Paper Checklist Guidelines, instructions for answering. [Evidence](../../../../sources/notes/neurips2025checklist.md#e2)
[^neurips2025checklist-e12]: NeurIPS Paper Checklist Guidelines, Item 1 (Claims). [Evidence](../../../../sources/notes/neurips2025checklist.md#e12)
[^neurips2025checklist-e4]: NeurIPS Paper Checklist Guidelines, Item 2 (Limitations). [Evidence](../../../../sources/notes/neurips2025checklist.md#e4)
[^neurips2025checklist-e5]: NeurIPS Paper Checklist Guidelines, Item 7. [Evidence](../../../../sources/notes/neurips2025checklist.md#e5)
[^neurips2025checklist-e6]: NeurIPS Paper Checklist Guidelines, Item 7. [Evidence](../../../../sources/notes/neurips2025checklist.md#e6)
[^arr2024responsible-e9]: ACL Rolling Review Responsible NLP Research Checklist, C3. [Evidence](../../../../sources/notes/arr2024responsible.md#e9)
[^neurips2025checklist-e15]: NeurIPS Paper Checklist Guidelines, Item 6. [Evidence](../../../../sources/notes/neurips2025checklist.md#e15)
[^arr2024responsible-e8]: ACL Rolling Review Responsible NLP Research Checklist, C2. [Evidence](../../../../sources/notes/arr2024responsible.md#e8)
[^neurips2025checklist-e7]: NeurIPS Paper Checklist Guidelines, Item 8. [Evidence](../../../../sources/notes/neurips2025checklist.md#e7)
[^arr2024responsible-e7]: ACL Rolling Review Responsible NLP Research Checklist, C1. [Evidence](../../../../sources/notes/arr2024responsible.md#e7)
[^neurips2025checklist-e3]: NeurIPS Paper Checklist Guidelines, instructions for answering. [Evidence](../../../../sources/notes/neurips2025checklist.md#e3)
[^arr2024responsible-e2]: ACL Rolling Review Responsible NLP Research Checklist, Guidelines for Answering Checklist Questions. [Evidence](../../../../sources/notes/arr2024responsible.md#e2)
[^arr2024responsible-e1]: ACL Rolling Review Responsible NLP Research Checklist, Guidelines for Answering Checklist Questions. [Evidence](../../../../sources/notes/arr2024responsible.md#e1)
[^arr2024responsible-e5]: ACL Rolling Review Responsible NLP Research Checklist, Guidelines for Answering Checklist Questions. [Evidence](../../../../sources/notes/arr2024responsible.md#e5)
[^sainz2023nlp-e1]: Sainz et al. 2023, Abstract. [Evidence](../../../../sources/notes/sainz2023nlp.md#e1)
[^sainz2023nlp-e3]: Sainz et al. 2023, §3. [Evidence](../../../../sources/notes/sainz2023nlp.md#e3)
[^neurips2025checklist-e13]: NeurIPS Paper Checklist Guidelines, Item 12 (Licenses). [Evidence](../../../../sources/notes/neurips2025checklist.md#e13)
[^arr2024responsible-e6]: ACL Rolling Review Responsible NLP Research Checklist, B5. [Evidence](../../../../sources/notes/arr2024responsible.md#e6)
[^pineau2021improving-e4]: Pineau et al. 2021, §3. [Evidence](../../../../sources/notes/pineau2021improving.md#e4)
[^pineau2021improving-e5]: Pineau et al. 2021, §3. [Evidence](../../../../sources/notes/pineau2021improving.md#e5)
[^pineau2021improving-e6]: Pineau et al. 2021, §4. [Evidence](../../../../sources/notes/pineau2021improving.md#e6)
[^neurips2025checklist-e18]: NeurIPS Paper Checklist Guidelines, Item 10 (Broader Impacts). [Evidence](../../../../sources/notes/neurips2025checklist.md#e18)
[^neurips2025checklist-e11]: NeurIPS Paper Checklist Guidelines, Item 10. [Evidence](../../../../sources/notes/neurips2025checklist.md#e11)
[^arr2024responsible-e16]: ACL Rolling Review Responsible NLP Research Checklist, A2. [Evidence](../../../../sources/notes/arr2024responsible.md#e16)
[^neurips2025checklist-e10]: NeurIPS Paper Checklist Guidelines, Item 14. [Evidence](../../../../sources/notes/neurips2025checklist.md#e10)
[^arr2024responsible-e11]: ACL Rolling Review Responsible NLP Research Checklist, D2. [Evidence](../../../../sources/notes/arr2024responsible.md#e11)
[^arr2024responsible-e12]: ACL Rolling Review Responsible NLP Research Checklist, D4. [Evidence](../../../../sources/notes/arr2024responsible.md#e12)
[^lipton2019troubling-e2]: Lipton & Steinhardt 2019, §3.1. [Evidence](../../../../sources/notes/lipton2019troubling.md#e2)
[^neurips2025checklist-e17]: NeurIPS Paper Checklist Guidelines, Item 2 (Limitations). [Evidence](../../../../sources/notes/neurips2025checklist.md#e17)
