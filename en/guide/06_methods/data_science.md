# Data science research: drawing new conclusions from existing data with predictive or statistical modeling

This page covers **data science research**: building predictive or statistical models on existing data and using the modeling results to answer a scientific question. An example is "Can we predict which commits will introduce bugs from the characteristics of the code change?" It also covers using machine learning for research in other fields, such as models that predict civil wars or diseases.

Related pages: how to mine data from code repositories and bug databases is in [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md); comparing which existing tool or model is better is in [Benchmarking](../07_fields/computer-science/practices/benchmarking.md); proposing a new learning method or tool is in [Engineering research](../07_fields/computer-science/practices/engineering_research.md). How to choose baselines is in [Building and improving: get the baselines running early](../05_research-strategies/build_improve.md#get-the-baseline-running-early). Why test data is used only once, and how to deal with randomness, are in [Comparative evaluation: keep one dataset only for the final test](../05_research-strategies/compare_evaluate.md#keep-some-data-for-the-final-test-only) and [Comparative evaluation: is the difference real?](../05_research-strategies/compare_evaluate.md#is-the-difference-real). General statistical practice is in [Analyzing and interpreting results: report how big the difference is and how certain you are, not just the p-value](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value). Those topics apply to all kinds of research; this page covers only what is specific to data science.

**Scope** `[Our analysis]`: the checklist on this page is based mainly on the data science standard that ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering) wrote for software engineering as part of its Empirical Standards ("the SIGSOFT standard" below), and many examples come from software engineering, systems security, and machine learning. The parts on preventing data leakage draw on cross-disciplinary sources: the REFORMS checklist was developed jointly by researchers from computer science, the social sciences, biomedicine, and other fields, and the survey of data leakage covers 17 fields (see Section 2). If you use predictive or statistical modeling for research in another field, you can use those parts directly; for other requirements on statistical modeling and reporting, read your own field's standards first. For example, for studying the causes of disease with observational data in health research, see [Observational epidemiology](observational_epidemiology.md).

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md) (exploratory analysis of existing datasets).

**After reading this page, you should be able to:**

- tell whether you want to "predict" or to "explain", and state the population your claim is about;
- recognize and prevent the most common forms of data leakage, including temporal leakage and duplicate samples;
- evaluate a model with "dumb" baselines, fair tuning, and metrics that match the actual decision;
- avoid presenting correlation as causation, or speculation as conclusions;
- check your study against the SIGSOFT standard and the REFORMS checklist.

---

## 1. What this kind of research is and when to use it

The SIGSOFT standard defines it as research that uses machine learning and other data-centric methods to analyze software engineering phenomena or artifacts; the standard applies to studies that mainly use predictive modeling to analyze existing phenomena[^ralph2020empirical-e188][^ralph2020empirical-e189]. The cross-disciplinary REFORMS checklist (Recommendations for Machine-learning-based Science) puts it more directly: this kind of research **uses a model's performance as evidence for a scientific claim**[^kapoor2024reforms-e1].

The key point: **the contribution is a conclusion about the world, not the model itself.** If the focus is the tool itself rather than the new conclusions the tool produces, SIGSOFT recommends using a different standard[^ralph2020empirical-e189]. Predictive analytics in business is different too: its target population can be left unspecified, and the relationships it finds only need to hold within that company[^kapoor2024reforms-e27]. In research, you have to state which population your conclusions generalize to (see Step 1).

**How it differs from related types of study** `[Our analysis, based on each page's definition]`:

| | Data science research | Repository mining | Benchmarking | Engineering research |
|---|---|---|---|---|
| Main contribution | New conclusions drawn from data and models | A dataset, plus descriptive and relational statistics | A comparison of existing systems or models | A new method or tool |
| Typical question | "How well can X be predicted?" | "How common is it? What is it associated with?" | "Which is better, A or B?" | "Does my new tool solve the problem?" |

A single study often spans two of these: mine the data first, then build models. Do the data collection as described in [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md), and the modeling and evaluation as described on this page.

### First decide: do you want to predict, or to explain?

REFORMS borrows Breiman's "two cultures"[^kapoor2024reforms-e3]:

- **Explanation** (the data modeling culture, traditional statistics): estimate parameters that represent the true data-generating process, to answer "What is the relationship between X and Y, and how strong is it?"
- **Prediction** (the algorithmic modeling culture, most machine learning research): predict accurately on new samples not seen in training; the parameters need not be interpretable.

The two need different evidence: explanation rests on parameter estimates, prediction on how the model performs on new data. Most REFORMS items are aimed at prediction and do not apply to explanatory modeling[^kapoor2024reforms-e4]. For example, "What is the relationship between the number of code reviewers and the defect rate?" is an explanation question; "Given a commit's features, how accurately can we predict whether it introduces a bug?" is a prediction question `[Our analysis]`. **Predicting well is not the same as understanding the cause**; see Step 8.

---

## 2. How to do it

The problems are widespread: a cross-disciplinary survey found data leakage in 17 fields, affecting 294 papers, some with badly overoptimistic conclusions[^kapoor2023leakage-e1]. The authors stress that this is only a lower bound, and that errors in code can't be seen just by reading the papers[^kapoor2023leakage-e2]. An analysis of 30 machine learning papers from top security conferences found at least three pitfalls in every one of them[^arp2022dos-e3].

### Step 1: State the claim, the target population, and the outcome variable

**How:**

- **Write down the target population**: which group or kind of data your conclusions are meant to generalize to, for example "commits in open-source Java projects" or "commits at one particular company". Papers often leave this out[^kapoor2024reforms-e5].
- **State what the outcome variable stands for.** The variable you predict is usually only a proxy for some unobservable theoretical construct[^kapoor2024reforms-e6]. For example, using "changes that were later fixed" to stand for "bugs": the two are not the same thing `[Our analysis]`.
- **Explain why this method is suitable for studying this problem now**[^ralph2020empirical-e207].

### Step 2: Understand where the data came from and how good it is

**How:**

- Explain how and why the data were selected, and how they were preprocessed and filtered[^ralph2020empirical-e190]. Say specifically why this data suits your question; "it's the best dataset we could find" is not a justification[^kapoor2024reforms-e7].
- **Don't assume a dataset is good because many papers have used it**[^lones2021avoid-e19]. Research that relies heavily on data must stay alert to data quality[^menzies2019bad-e11].
- Check item by item: whether the data represent the real distribution (sampling bias)[^arp2022dos-e11]; whether the labels are noisy[^arp2022dos-e10]; whether there are duplicate samples; whether outliers are errors or genuine extreme values[^lones2021avoid-e20].
- **Look at the data yourself.** Manually inspecting a substantial portion of the data is a desirable attribute in the SIGSOFT standard[^ralph2020empirical-e199].
- State why any samples were excluded: which subset you choose can greatly affect model performance[^kapoor2024reforms-e10]. When one individual takes up several rows, report the number of individuals and the number of rows separately[^kapoor2024reforms-e9].

**Where people go wrong:** assuming a large dataset is automatically fine. When the sampling frame (the list you can actually draw from) is not representative, a bigger sample only narrows the confidence interval; the bias doesn't shrink[^kapoor2024reforms-e8].

### Step 3: Split the data before doing anything else to it

**Data leakage** is a spurious relationship between features and the outcome created artificially during data collection, sampling, preprocessing, or modeling, for example when information from the test data gets into training[^kapoor2024reforms-e15]. It is common because researchers have access to all the data while building models[^kapoor2023leakage-e3]. The most common kinds:

| Type | Example | How to prevent it |
|---|---|---|
| Preprocessing on all the data | Normalizing[^kapoor2024reforms-e15], scaling, or imputing missing values[^lones2021avoid-e18], or selecting features[^kapoor2023leakage-e4] on the full dataset | Split first; compute every statistic from training data only; in cross-validation, preprocess each fold separately[^kapoor2024reforms-e11] |
| The test set has been "modified" | Undersampling or oversampling the test data too, to balance classes | Resample only the training data; keep the test data as it really is[^ralph2020empirical-e204] |
| Temporal leakage | You want to predict the future, but the test set contains data older than the training set[^kapoor2023leakage-e5]; using standard cross-validation directly on time series[^lones2021avoid-e22] | Split by time: train on earlier data, test on later data `[Our analysis]` |
| Duplicates and dependencies | Duplicate samples randomly split across both sides[^kapoor2024reforms-e18]; several records from the same patient in both the training and the test set[^lones2021avoid-e21] | Deduplicate first `[Our analysis]`; split by group, keeping each individual (patient, user, project) on one side[^kapoor2024reforms-e17] |
| Illegitimate features | A sepsis model uses "antibiotics were prescribed" as a feature, but antibiotics are usually prescribed only after diagnosis[^kapoor2024reforms-e16] | For each feature, ask: would it be available at the time of a real prediction? The more features, the more important it is to check each one[^kapoor2024reforms-e19] |
| Using the test set to make decisions | Tuning parameters or setting thresholds on the test data[^arp2022dos-e7]; removing outliers using statistics from all the data[^arp2022dos-e4] | See Step 5 |
| The test set doesn't represent the target population | Testing only on data from one region but claiming the model works in other regions too[^kapoor2023leakage-e7] | State where the test set comes from, and limit your conclusions to that |

In software engineering, a typical case of temporal leakage is training on data from newer releases to "predict" bugs in older releases; a typical case of dependency is data from the same project appearing in both the training and the test set while the claim is "generalizes to new projects" `[Our analysis]`.

**Why it is worth being this strict:** in a reproduction study of civil war prediction, the 4 papers (out of 12) that contained errors were exactly the 4 that claimed complex models beat a logistic regression baseline. After the leakage was corrected, the complex models did not perform much better than decades-old logistic regression[^kapoor2023leakage-e8].

**How:** set aside the test set at the very start of the project and use it only once, at the end; the reasons are in the "Using the test set to make decisions" row above and in Step 5. In the paper you must argue that there is no leakage, and the burden of proof is on you[^kapoor2023leakage-e9]. You can use the "model info sheets" proposed by Kapoor & Narayanan to check yourself for each type of leakage[^kapoor2023leakage-e10]. With well-known public datasets, be careful as well: their properties have been studied thoroughly, so methods can end up exploiting knowledge of the test data without anyone noticing; it is best to also run experiments on newer data[^arp2022dos-e5]. Large language models may have seen the test sets of public benchmarks during training (data contamination); for how to check, see [Benchmarking: is the benchmark itself valid?](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid).

### Step 4: Start comparing with "dumb" baselines

For the general principles of fair comparison, see [Comparative evaluation: what evidence is enough](../05_research-strategies/compare_evaluate.md#2-what-evidence-is-enough). What you specifically need to do in data science research:

- **Compute "dumb" baselines first** (naive models that learn nothing). A model that always predicts the majority class can have 50% accuracy or 90%, depending entirely on the class proportions[^lones2021avoid-e23]; in regression, a model that always predicts "no change" can also score well[^lones2021avoid-e24]. Until you have these numbers, you don't know what your model is actually good at `[Our analysis]`.
- **Then compare with simple models**, such as logistic regression. Running very simple algorithms first quickly shows you the rough structure of the problem[^menzies2019bad-e16]. In software engineering, many datasets have a simple structure, and simple methods work as well as deep learning or better[^menzies2019bad-e15]; the civil war prediction example above is another lesson.
- **Finally, compare with the state of the art**, or explain why there is none or why a direct comparison is impossible; this is essential in SIGSOFT[^ralph2020empirical-e191]. Applying several different kinds of learners to the data is desirable[^ralph2020empirical-e196].

### Step 5: Tune fairly, and select models without touching the test set

**How:**

- **Give every method you compare the same tuning effort**; for why, see "Are competitors treated equally?" in [Comparative evaluation: what evidence is enough](../05_research-strategies/compare_evaluate.md#2-what-evidence-is-enough). In machine learning, note in particular that the default settings of many algorithms are poor to begin with[^menzies2019bad-e13], so "competitors use default settings" often amounts to a weak baseline `[Our analysis]`; a baseline that wasn't selected and tuned the same way as the new method also becomes a "weak baseline"[^kapoor2024reforms-e14].
- **Report the tuning details**[^kapoor2024reforms-e28], such as which hyperparameters you searched, with what method, and how much compute it took `[Our analysis]`. The amount of effort clearly affects the results: with a different set of hyperparameters, the ranking of two methods can flip[^kapoor2024reforms-e13].
- **Use only training and validation data for tuning and model selection.** Trying several models on the held-out set and picking the best overestimates performance. Keep a separate test set; when data is scarce, use nested cross-validation (the outer loop estimates performance, the inner loop tunes and selects models)[^kapoor2024reforms-e12].

> **Where sources disagree: should you use grid search?**
> - The SIGSOFT standard lists "carefully selecting hyperparameters" as desirable, with examples including following the settings in related work or using automated optimization such as grid search[^ralph2020empirical-e198].
> - Menzies & Shepperd strongly oppose grid search: it is slow and can miss important optimizations. They recommend very simple optimizers such as differential evolution[^menzies2019bad-e14].
>
> In practice: which tuning method you use matters less; what matters is that every method you compare gets the same tuning budget, and that you state it clearly in the paper `[Our analysis]`.

### Step 6: Choose metrics that match the real decision

**How:**

1. **First write down what decision the model's output will be used for**, then choose the metrics and explain your reasoning in the paper[^ralph2020empirical-e192] `[Our analysis]`.
2. **With imbalanced classes, don't look only at accuracy**[^kapoor2024reforms-e20]. A receiver operating characteristic (ROC) curve (false positive rate on the horizontal axis, true positive rate on the vertical) alone can look very good while precision is very low[^arp2022dos-e9].
3. **Interpret results against the base rate.** A true positive rate of 99% and a false positive rate of 1% look great, but when positives and negatives are in a 1:100 ratio, every 99 true positives come with 100 false positives[^arp2022dos-e8].
4. **Consider the cost of different errors.** In some domains certain errors are costlier than others[^kapoor2024reforms-e20]. For example, when defect predictions are used to allocate testing effort, too many false alarms waste effort, and too many misses make the prediction pointless `[Our analysis]`.

### Step 7: Report variation and uncertainty

For the general principles (repeat runs, report distributions, effect sizes), see [Analyzing and interpreting results: report how big the difference is and how certain you are](../02_do-the-project/07_analyze-and-interpret.md#3-report-how-big-and-how-certain-not-just-the-p-value). The specific requirements for data science research:

- Don't give only a mean or median; include distributional information such as variation and confidence[^ralph2020empirical-e192].
- Run several times with different random train/test splits (for example, cross-validation), then compare with significance tests and effect sizes[^ralph2020empirical-e197]. The antipatterns are: using statistical tests without checking their assumptions; reporting significance without effect sizes; reporting effect sizes without confidence intervals[^ralph2020empirical-e205].
- When there is no ready-made method, you can bootstrap within the test set (resampling with replacement many times) to get confidence intervals[^kapoor2024reforms-e21]. REFORMS considers reporting uncertainty better than just running statistical tests[^kapoor2024reforms-e22].

This step is often skipped: in the civil war prediction study above, 9 of the 12 papers compared models without running any test or quantifying uncertainty[^kapoor2023leakage-e11].

### Step 8: Interpret the results: correlation is not causation

**How:**

- **Don't claim causation lightly.** SIGSOFT lists this as an antipattern: claiming causation after establishing only covariation and temporal order, without ruling out third-variable explanations or proposing a hypothesized mechanism[^ralph2020empirical-e203]. For example, seeing across many projects that a certain coding style is more prone to bugs shows only a correlation; to believe it is causal you would need a follow-up experiment that actively changes the coding style[^menzies2019bad-e10]. Not making causal claims when causal inference isn't possible is not a flaw[^ralph2020empirical-e206].
- **Check whether the model learned what you think it learned.** A model can latch onto artifacts that are associated with the task but have nothing to do with the task itself (spurious correlations)[^arp2022dos-e6]. In one malware detection experiment, the URL "play.google.com" became one of the most important features for identifying benign apps: the classifier had learned to tell where an app came from, not whether it was malicious or benign[^arp2022dos-e12]. The more complex the model, the more easily it overfits to spurious correlations[^lones2021avoid-e25]. The goal of research is to produce understanding, not slightly higher accuracy than others, so look at what the model actually learned[^lones2021avoid-e26], for example by examining the most important features and analyzing misclassified samples one by one `[Our analysis]`.
- **Keep results and speculation apart** (for general practice, see [Analyzing and interpreting results: negative and unexpected results](../02_do-the-project/07_analyze-and-interpret.md#5-negative-and-unexpected-results)). When results look good, it is especially tempting to slip in claims with no evidence behind them[^lipton2019troubling-e15]. SIGSOFT considers it usually enough to split results and discussion into two sections and keep speculation out of the results section[^ralph2020empirical-e200].
- **State where your conclusions do not hold.** This sets clear expectations and avoids hype[^kapoor2024reforms-e24]. Even if the model performs well now, it can get worse as the data distribution shifts over time[^kapoor2024reforms-e23].

### Step 9: Make it reproducible for others

**How:**

- Describe the feature engineering, the modeling approach (usually in pseudocode), and the hardware and software environment; this is essential in SIGSOFT[^ralph2020empirical-e193].
- Provide data, code, environment, documentation, and a reproduction script that generates the results in one step[^kapoor2024reforms-e26]; when the data can't be made public, provide synthetic data showing how to use the algorithms[^ralph2020empirical-e195]. Record details such as random seeds; see [Organizing research materials: every result should be traceable to how it was produced](../08_throughout/organizing_materials.md#3-every-result-must-be-traceable-to-how-it-was-produced).
- **Check your work against REFORMS before submitting.** It has 32 questions and was developed jointly by 19 researchers from computer science, the social sciences, biomedicine, and other fields[^kapoor2024reforms-e2]. You don't have to follow every item; you decide which are relevant to your study[^kapoor2024reforms-e25].

---

## 3. Checklist

This follows mainly the SIGSOFT data science standard; the three leakage-prevention items follow REFORMS. The SIGSOFT standard targets software engineering; in other areas, use what fits.

**Essential**

- [ ] Explain why this method is suitable for studying this problem now[^ralph2020empirical-e207]
- [ ] Explain how and why the data were selected, and how they were preprocessed, filtered, and categorized[^ralph2020empirical-e190]
- [ ] Describe the feature engineering, the modeling approach, and the hardware and software environment[^ralph2020empirical-e193]
- [ ] Discuss state-of-the-art baselines, or explain why there are none or why a direct comparison is impossible[^ralph2020empirical-e191]
- [ ] Justify the statistics and heuristics used; discuss assumptions and threats to validity specific to data science[^ralph2020empirical-e194]
- [ ] State and justify the evaluation metrics; give variation or confidence for results, not just means[^ralph2020empirical-e192]
- [ ] Argue that preprocessing and modeling used only training data; explain how dependencies and duplicates between the training and test sets were handled; argue that every feature is legitimate (REFORMS)[^kapoor2024reforms-e29]

**Desirable**

- [ ] Provide a replication package; provide synthetic data when the data can't be made public[^ralph2020empirical-e195]
- [ ] Use several different kinds of learners[^ralph2020empirical-e196]
- [ ] Use several random train/test splits, and compare with significance tests and effect sizes[^ralph2020empirical-e197]
- [ ] Select hyperparameters carefully[^ralph2020empirical-e198]
- [ ] Manually inspect a substantial portion of the data[^ralph2020empirical-e199]
- [ ] Clearly separate results that have evidence behind them from interpretation and speculation[^ralph2020empirical-e200]

**Extraordinary**[^ralph2020empirical-e201]

- [ ] Use longitudinal analysis to exploit temporal data
- [ ] Analyze some samples qualitatively, or triangulate with other data such as questionnaires or interviews
- [ ] Share findings with the creators of the artifacts studied and ask for feedback

**Acceptable deviations (not flaws)**[^ralph2020empirical-e202]

- Using coarser processing, such as keyword matching or random sampling, when the data are too large
- Not publishing data that are too large or too sensitive
- Not running statistical tests or stating hypotheses in purely descriptive studies

**Common reviewer criticisms that are not valid**[^ralph2020empirical-e206]

- "You should have analyzed a different dataset": the right question is whether the claims are supported by the data analyzed
- "There is no replication package": this is currently desirable, not essential
- "You made no causal claims": if causal inference isn't possible, you shouldn't make them

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Not stating the target population or what the outcome variable means | Readers can't judge how far the conclusions generalize[^kapoor2024reforms-e5][^kapoor2024reforms-e6] |
| Normalizing, imputing missing values, or selecting features on all the data before splitting | Information from the test data leaks into training and inflates the results[^kapoor2024reforms-e15][^kapoor2023leakage-e4] |
| Splitting time-ordered data randomly | The model uses information "from the future"[^kapoor2023leakage-e5] |
| Data from the same person or project ending up in both the training and test sets | Training and test are not independent, which is leakage[^kapoor2023leakage-e6] |
| Using features that wouldn't be available at prediction time | The feature is really a stand-in for the outcome[^kapoor2024reforms-e16] |
| Not comparing with "dumb" baselines and simple models | You can't tell whether the model really learned anything[^lones2021avoid-e23][^kapoor2023leakage-e8] |
| Tuning and selecting models on the test set | Overestimates performance[^arp2022dos-e7][^kapoor2024reforms-e12] |
| Reporting only accuracy or a ROC curve with imbalanced classes | Hides large numbers of false positives[^arp2022dos-e8][^arp2022dos-e9] |
| Reporting a single mean | You can't tell whether a difference is just noise[^ralph2020empirical-e192][^ralph2020empirical-e205] |
| Jumping straight from correlation to causation | Third variables and other explanations haven't been ruled out[^ralph2020empirical-e203] |
| Not looking at what the model learned | It may have learned spurious correlations[^arp2022dos-e12] |

---

## 5. Further reading

- **REFORMS** (Kapoor et al. 2024): a cross-disciplinary 32-item checklist, each item with an explanation and references; good for going through item by item before submission.
- **Data leakage**: Kapoor & Narayanan 2023, with a taxonomy of 8 types of leakage, model info sheets, and the full reproduction of the civil war prediction case.
- **An introduction to machine learning pitfalls**: Lones's guide is organized as "before you start building models, building models, evaluating, comparing, reporting" and suits beginners reading it end to end; Arp et al. 2022 focuses on security and includes a table of types of data snooping.
- **Data analysis in software engineering**: Menzies & Shepperd 2019 lists "bad smells" in software analytics papers; useful for reviewing and checking your own work.
- **The SIGSOFT data science standard**: the source of this page's checklist; the original also lists recommended reading and exemplar papers.

Links to all sources are in the [source list](../../sources/README.md).

[^ralph2020empirical-e188]: SIGSOFT Data Science standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e188)
[^ralph2020empirical-e189]: SIGSOFT Data Science standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e189)
[^ralph2020empirical-e190]: SIGSOFT Data Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e190)
[^ralph2020empirical-e191]: SIGSOFT Data Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e191)
[^ralph2020empirical-e192]: SIGSOFT Data Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e192)
[^ralph2020empirical-e193]: SIGSOFT Data Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e193)
[^ralph2020empirical-e194]: SIGSOFT Data Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e194)
[^ralph2020empirical-e195]: SIGSOFT Data Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e195)
[^ralph2020empirical-e196]: SIGSOFT Data Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e196)
[^ralph2020empirical-e197]: SIGSOFT Data Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e197)
[^ralph2020empirical-e198]: SIGSOFT Data Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e198)
[^ralph2020empirical-e199]: SIGSOFT Data Science standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e199)
[^ralph2020empirical-e200]: SIGSOFT Data Science standard, Desirable Attributes and footnote 8. [Evidence](../../sources/notes/ralph2020empirical.md#e200)
[^ralph2020empirical-e201]: SIGSOFT Data Science standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e201)
[^ralph2020empirical-e202]: SIGSOFT Data Science standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e202)
[^ralph2020empirical-e203]: SIGSOFT Data Science standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e203)
[^ralph2020empirical-e204]: SIGSOFT Data Science standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e204)
[^ralph2020empirical-e205]: SIGSOFT Data Science standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e205)
[^ralph2020empirical-e206]: SIGSOFT Data Science standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e206)
[^ralph2020empirical-e207]: SIGSOFT Data Science standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e207)
[^kapoor2024reforms-e1]: Kapoor et al. 2024, The scope of our claims. [Evidence](../../sources/notes/kapoor2024reforms.md#e1)
[^kapoor2024reforms-e2]: Kapoor et al. 2024, Abstract. [Evidence](../../sources/notes/kapoor2024reforms.md#e2)
[^kapoor2024reforms-e3]: Kapoor et al. 2024, Module 1, 1c. [Evidence](../../sources/notes/kapoor2024reforms.md#e3)
[^kapoor2024reforms-e4]: Kapoor et al. 2024, The scope of our claims, Explanatory modeling. [Evidence](../../sources/notes/kapoor2024reforms.md#e4)
[^kapoor2024reforms-e5]: Kapoor et al. 2024, Module 1, 1a. [Evidence](../../sources/notes/kapoor2024reforms.md#e5)
[^kapoor2024reforms-e6]: Kapoor et al. 2024, Module 3, 3d. [Evidence](../../sources/notes/kapoor2024reforms.md#e6)
[^kapoor2024reforms-e7]: Kapoor et al. 2024, Module 3, 3c. [Evidence](../../sources/notes/kapoor2024reforms.md#e7)
[^kapoor2024reforms-e8]: Kapoor et al. 2024, Module 3, 3e. [Evidence](../../sources/notes/kapoor2024reforms.md#e8)
[^kapoor2024reforms-e9]: Kapoor et al. 2024, Module 3, 3e. [Evidence](../../sources/notes/kapoor2024reforms.md#e9)
[^kapoor2024reforms-e10]: Kapoor et al. 2024, Module 4, 4a. [Evidence](../../sources/notes/kapoor2024reforms.md#e10)
[^kapoor2024reforms-e11]: Kapoor et al. 2024, Module 4, 4c. [Evidence](../../sources/notes/kapoor2024reforms.md#e11)
[^kapoor2024reforms-e12]: Kapoor et al. 2024, Module 5, 5d. [Evidence](../../sources/notes/kapoor2024reforms.md#e12)
[^kapoor2024reforms-e13]: Kapoor et al. 2024, Module 5, 5e. [Evidence](../../sources/notes/kapoor2024reforms.md#e13)
[^kapoor2024reforms-e14]: Kapoor et al. 2024, Module 5, 5f. [Evidence](../../sources/notes/kapoor2024reforms.md#e14)
[^kapoor2024reforms-e15]: Kapoor et al. 2024, Module 6. [Evidence](../../sources/notes/kapoor2024reforms.md#e15)
[^kapoor2024reforms-e16]: Kapoor et al. 2024, Module 6. [Evidence](../../sources/notes/kapoor2024reforms.md#e16)
[^kapoor2024reforms-e17]: Kapoor et al. 2024, Module 6, 6b. [Evidence](../../sources/notes/kapoor2024reforms.md#e17)
[^kapoor2024reforms-e18]: Kapoor et al. 2024, Module 6, 6b. [Evidence](../../sources/notes/kapoor2024reforms.md#e18)
[^kapoor2024reforms-e19]: Kapoor et al. 2024, Module 6, 6c. [Evidence](../../sources/notes/kapoor2024reforms.md#e19)
[^kapoor2024reforms-e20]: Kapoor et al. 2024, Module 7, 7a. [Evidence](../../sources/notes/kapoor2024reforms.md#e20)
[^kapoor2024reforms-e21]: Kapoor et al. 2024, Module 7, 7b. [Evidence](../../sources/notes/kapoor2024reforms.md#e21)
[^kapoor2024reforms-e22]: Kapoor et al. 2024, Module 7, 7c. [Evidence](../../sources/notes/kapoor2024reforms.md#e22)
[^kapoor2024reforms-e23]: Kapoor et al. 2024, Module 8, 8a. [Evidence](../../sources/notes/kapoor2024reforms.md#e23)
[^kapoor2024reforms-e24]: Kapoor et al. 2024, Module 8, 8b. [Evidence](../../sources/notes/kapoor2024reforms.md#e24)
[^kapoor2024reforms-e25]: Kapoor et al. 2024, Table 1 caption. [Evidence](../../sources/notes/kapoor2024reforms.md#e25)
[^kapoor2024reforms-e26]: Kapoor et al. 2024, Module 2. [Evidence](../../sources/notes/kapoor2024reforms.md#e26)
[^kapoor2024reforms-e27]: Kapoor et al. 2024, The scope of our claims, Predictive analytics. [Evidence](../../sources/notes/kapoor2024reforms.md#e27)
[^kapoor2024reforms-e28]: Kapoor et al. 2024, Table 1, 5e, 5f. [Evidence](../../sources/notes/kapoor2024reforms.md#e28)
[^kapoor2024reforms-e29]: Kapoor et al. 2024, Table 1, 6a–6c. [Evidence](../../sources/notes/kapoor2024reforms.md#e29)
[^kapoor2023leakage-e1]: Kapoor & Narayanan 2023, Summary. [Evidence](../../sources/notes/kapoor2023leakage.md#e1)
[^kapoor2023leakage-e2]: Kapoor & Narayanan 2023, Results. [Evidence](../../sources/notes/kapoor2023leakage.md#e2)
[^kapoor2023leakage-e3]: Kapoor & Narayanan 2023, Leakage in modeling competitions. [Evidence](../../sources/notes/kapoor2023leakage.md#e3)
[^kapoor2023leakage-e4]: Kapoor & Narayanan 2023, leakage taxonomy, L1.3. [Evidence](../../sources/notes/kapoor2023leakage.md#e4)
[^kapoor2023leakage-e5]: Kapoor & Narayanan 2023, leakage taxonomy, L3.1. [Evidence](../../sources/notes/kapoor2023leakage.md#e5)
[^kapoor2023leakage-e6]: Kapoor & Narayanan 2023, leakage taxonomy, L3.2. [Evidence](../../sources/notes/kapoor2023leakage.md#e6)
[^kapoor2023leakage-e7]: Kapoor & Narayanan 2023, leakage taxonomy, L3.3. [Evidence](../../sources/notes/kapoor2023leakage.md#e7)
[^kapoor2023leakage-e8]: Kapoor & Narayanan 2023, Summary and the civil war prediction case study. [Evidence](../../sources/notes/kapoor2023leakage.md#e8)
[^kapoor2023leakage-e9]: Kapoor & Narayanan 2023, Model info sheets. [Evidence](../../sources/notes/kapoor2023leakage.md#e9)
[^kapoor2023leakage-e10]: Kapoor & Narayanan 2023, Summary. [Evidence](../../sources/notes/kapoor2023leakage.md#e10)
[^kapoor2023leakage-e11]: Kapoor & Narayanan 2023, civil war prediction case study. [Evidence](../../sources/notes/kapoor2023leakage.md#e11)
[^arp2022dos-e3]: Arp et al. 2022, Abstract. [Evidence](../../sources/notes/arp2022dos.md#e3)
[^arp2022dos-e4]: Arp et al. 2022, §2, P3. [Evidence](../../sources/notes/arp2022dos.md#e4)
[^arp2022dos-e5]: Arp et al. 2022, §2, P3. [Evidence](../../sources/notes/arp2022dos.md#e5)
[^arp2022dos-e6]: Arp et al. 2022, §2, P4. [Evidence](../../sources/notes/arp2022dos.md#e6)
[^arp2022dos-e7]: Arp et al. 2022, §2, P5. [Evidence](../../sources/notes/arp2022dos.md#e7)
[^arp2022dos-e8]: Arp et al. 2022, §2, P8. [Evidence](../../sources/notes/arp2022dos.md#e8)
[^arp2022dos-e9]: Arp et al. 2022, §2, P7. [Evidence](../../sources/notes/arp2022dos.md#e9)
[^arp2022dos-e10]: Arp et al. 2022, §2, P2. [Evidence](../../sources/notes/arp2022dos.md#e10)
[^arp2022dos-e11]: Arp et al. 2022, §2, P1. [Evidence](../../sources/notes/arp2022dos.md#e11)
[^arp2022dos-e12]: Arp et al. 2022, §4.1. [Evidence](../../sources/notes/arp2022dos.md#e12)
[^lones2021avoid-e18]: Lones 2021, §3.1. [Evidence](../../sources/notes/lones2021avoid.md#e18)
[^lones2021avoid-e19]: Lones 2021, §2.2. [Evidence](../../sources/notes/lones2021avoid.md#e19)
[^lones2021avoid-e20]: Lones 2021, §2.4. [Evidence](../../sources/notes/lones2021avoid.md#e20)
[^lones2021avoid-e21]: Lones 2021, §4.4. [Evidence](../../sources/notes/lones2021avoid.md#e21)
[^lones2021avoid-e22]: Lones 2021, §4.8. [Evidence](../../sources/notes/lones2021avoid.md#e22)
[^lones2021avoid-e23]: Lones 2021, §4.6, Fig. 6. [Evidence](../../sources/notes/lones2021avoid.md#e23)
[^lones2021avoid-e24]: Lones 2021, §4.6. [Evidence](../../sources/notes/lones2021avoid.md#e24)
[^lones2021avoid-e25]: Lones 2021, §3.8. [Evidence](../../sources/notes/lones2021avoid.md#e25)
[^lones2021avoid-e26]: Lones 2021, §6.5. [Evidence](../../sources/notes/lones2021avoid.md#e26)
[^menzies2019bad-e10]: Menzies & Shepperd 2019, §1. [Evidence](../../sources/notes/menzies2019bad.md#e10)
[^menzies2019bad-e11]: Menzies & Shepperd 2019, §4.3. [Evidence](../../sources/notes/menzies2019bad.md#e11)
[^menzies2019bad-e13]: Menzies & Shepperd 2019, §4.10. [Evidence](../../sources/notes/menzies2019bad.md#e13)
[^menzies2019bad-e14]: Menzies & Shepperd 2019, §4.10. [Evidence](../../sources/notes/menzies2019bad.md#e14)
[^menzies2019bad-e15]: Menzies & Shepperd 2019, §4.11. [Evidence](../../sources/notes/menzies2019bad.md#e15)
[^menzies2019bad-e16]: Menzies & Shepperd 2019, §4.11. [Evidence](../../sources/notes/menzies2019bad.md#e16)
[^lipton2019troubling-e15]: Lipton & Steinhardt 2019, §4.1. [Evidence](../../sources/notes/lipton2019troubling.md#e15)
