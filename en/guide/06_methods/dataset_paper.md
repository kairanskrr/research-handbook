# Building a dataset or benchmark: the dataset itself as the research contribution

This page covers **dataset papers** and **benchmark papers** (sometimes called resource papers): papers whose main contribution is not a new method but a dataset or benchmark you have built, which others can use to train models, evaluate tools, or do their own research.

This page covers only **how to build one and how to release it**. For using a benchmark to compare systems, tools, or models, including how to compare fairly and how to report results, see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md); for checking whether an existing benchmark measures what it claims to and whether it is contaminated, see its section [Is the benchmark itself valid?](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid). This page links to that material where it needs it rather than repeating it.

**Scope** `[Our analysis]`: The practices on this page come mainly from machine learning (datasheets, the call for papers of the NeurIPS (Conference on Neural Information Processing Systems) Datasets and Benchmarks Track, Raji et al.'s critique of "general" benchmarks, and the BetterBench quality criteria for benchmarks) and from software engineering (the benchmarking standard of ACM SIGSOFT, the Association for Computing Machinery's Special Interest Group on Software Engineering, with the smart contract benchmark SmartBugs as a worked example). Cross-disciplinary norms for publishing data come from the FAIR (Findable, Accessible, Interoperable, Reusable) data principles and the submission guidelines of the journal Scientific Data, which cover the natural sciences, medicine, and many other fields. If you are building a dataset in another field, start with your field's data journals, data repositories, and ethics norms. For psychology studies whose contribution is a measurement instrument, see [Scale development and measurement studies](scale_development.md).

**Strategies it usually serves**: [Measurement](../05_research-strategies/measure.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md).

**After reading this page, you should be able to:**

- judge whether your contribution suits a dataset or benchmark paper, and explain why the field needs it;
- design how you collect and sample the data, organize annotation, and check annotator agreement;
- split the data, close off leakage between training and test sets, and reduce contamination;
- write a datasheet and handle licensing, consent, and ethics;
- release the dataset somewhere it will stay available, and plan for maintenance, versioning, and retirement;
- know what reviewers will check.

---

## 1. What this kind of study is, and when to use it

In machine learning, a **benchmark** is often defined as one or more datasets (at least test data) plus a metric, taken to stand for some specific tasks or capabilities and used by the research community as a shared framework for comparing methods[^raji2021everything-e1]. The SIGSOFT standard in software engineering requires a paper proposing a new benchmark to state four things: the quality to be measured, the metric that quantifies it, the measurement method, and the sample of workloads or tasks the system under test must handle[^ralph2020empirical-e147]. A **dataset** is broader: it need not come with a metric, and can be used for training, analysis, or other research `[Our analysis]`.

Several venues have dedicated outlets for this kind of paper. NeurIPS, a top machine learning conference, runs a Datasets and Benchmarks Track; its rationale is that when the main contribution is a new dataset or benchmark, it is better reviewed against criteria suited to that kind of work, whereas the main track's review focuses on algorithms, analysis, and applications[^neurips2024datasets-e13]. The journal Scientific Data publishes "Data Descriptors", peer-reviewed papers that describe datasets held in data repositories[^scientificdata2026guidelines-e10].

**Questions it is good at** `[Our analysis]`:

- **A class of tools cannot be compared on the same footing.** SmartBugs started from this problem: many smart contract analysis tools were available, but the datasets each had used were not, which made studies hard to compare and reproduce[^durieux2020empirical-e1]. Its contributions include two datasets: a manually annotated set of vulnerable contracts, and a large set of contracts collected from Ethereum[^durieux2020empirical-e2].
- **Existing data can't test the claim you want to test**: for example, existing evaluation sets are too small, full of labeling errors, already saturated by models, or likely to have been seen by models during training.
- **A field has no shared yardstick**: everyone uses their own data, so results can't be compared.

If you collected some data just to evaluate your own new method, the main contribution is still the method; see [Engineering research](../07_fields/computer-science/practices/engineering_research.md). Just describe how you built the dataset as this page explains `[Our analysis]`.

**How it differs from related methods** `[Our analysis]`:

| | Dataset or benchmark paper | Benchmarking | Mining software repositories | Scale development |
|---|---|---|---|---|
| Main output | The dataset or benchmark itself | A conclusion about which system, tool, or model is better | A conclusion about a software development phenomenon | The measurement instrument itself |
| Where the data comes from | Collected, curated, and annotated by you | Existing benchmarks (or your own) | Mined from code repositories, bug trackers, etc. | Writing items and administering them |
| What readers do with it | Download it, reuse it, compare on it | Read the conclusions | Read the conclusions | Use the scale to measure people |
| Where to read more | This page | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md) | [Scale development and measurement studies](scale_development.md) |

> **Where sources disagree: should a dataset paper report analysis results?**
>
> - **Scientific Data Descriptors: no.** These papers contain no results, discussion, or analysis, because their basic purpose is to describe the technical content of the dataset without bias and to encourage others to use it[^scientificdata2026guidelines-e6]. They must, however, have a "Technical Validation" section reporting the experiments, analyses, or checks that support the quality of the data[^scientificdata2026guidelines-e7].
> - **Machine learning benchmark papers: usually you run reference results.** NeurIPS requires the supplementary material of a benchmark paper to make all results easy to reproduce[^neurips2024datasets-e6]; BetterBench recommends reporting the metric's floor and ceiling, human performance, and random performance, so readers can tell what a score means[^reuel2024betterbench-e6], and providing scripts that reproduce the paper's results[^reuel2024betterbench-e8].
>
> In practice `[Our analysis]`: first check which tradition your venue belongs to. For a data journal, put your effort into the methods, data records, and technical validation; for a machine learning conference's benchmark track, run a few representative baselines so readers can see how hard the benchmark is and whether it separates stronger systems from weaker ones.

---

## 2. How to do it

After scoring 24 widely used AI benchmarks, the BetterBench authors concluded that poor benchmarks are mostly not deliberate; their builders simply didn't know what a good benchmark looks like[^reuel2024betterbench-e15]. BetterBench divides a benchmark's life into five stages: design, implementation, documentation, maintenance, and retirement[^reuel2024betterbench-e3]. Datasheets divide a dataset's life cycle into seven groups of questions: motivation, composition, collection process, preprocessing/cleaning/labeling, uses, distribution, and maintenance[^gebru2021datasheets-e5]. The steps below follow that order.

### Step 1: Explain why the dataset is needed

**How:**

1. **Answer the datasheet's first group of questions**: Why was the dataset created? For what task? What gap does it fill[^gebru2021datasheets-e7]?
2. **Turn "what you want to measure" into tasks.** Define the capability being measured, explain how it is turned into tasks in the benchmark, and say why it matters in the real world[^reuel2024betterbench-e4]. While designing, think about who will use it and how, involve domain experts, and draw on the domain literature[^reuel2024betterbench-e5].
3. **Explain how it differs from existing datasets and benchmarks**, so users can judge whether it fits their purpose[^reuel2024betterbench-e4].
4. **Keep the scope specific.** Raji et al. argue that benchmarks should be developed, presented, and understood for what they are meant to do: evaluate specific, well-scoped, contextualized tasks[^raji2021everything-e8].

**Why:** A benchmark task need not correspond to any problem people actually care about. Raji et al. quote Wagstaff: large numbers of machine learning researchers chase the best iris or mushroom classifier, yet this seems to have had no impact on botany or mycology[^raji2021everything-e4].

**Where people go wrong:**

- **Claiming the benchmark measures "general ability."** No dataset is neutral, so what a benchmark can show is limited; claims of "generality" often become an excuse for not reporting limitations[^raji2021everything-e5].
- **Praising your own work in the paper.** Scientific Data asks the background section to explain why the dataset was created and how others might reuse it, but not to make subjective claims about novelty, impact, or usefulness[^scientificdata2026guidelines-e2].

**Example** `[Our analysis]`: The running example suspects that "published evaluations of large language model vulnerability detectors are inflated by data leakage." To test this, you need contracts the models **could not have seen** during training. So the motivation might read: "Existing public smart contract vulnerability evaluation sets are likely to appear in models' training data, so they cannot tell 'the model can detect vulnerabilities' apart from 'the model memorized the answers.' We collect contracts deployed after the training cutoff dates of the models under test and annotate their vulnerabilities manually, as a control evaluation set." The dataset then becomes one row of the project's [evidence plan](../02_do-the-project/01_question-to-evidence.md), not a separate by-product.

**Write it down:** In three sentences: what task or claim the dataset is meant to support; why existing data isn't enough; and how it differs from the two closest existing datasets.

### Step 2: Decide what to collect and how to sample

**How:**

1. **Before collecting, read the datasheet's "composition" and "collection process" questions**, and answer them after collecting[^gebru2021datasheets-e8]. Reading them in advance tells you what to record while you collect `[Our analysis]`.
2. **State the sample and the population.** Does the dataset contain all possible instances, or is it a sample from a larger set? If it is a sample, what is that larger set, and is the sample representative[^gebru2021datasheets-e9]?
3. **Record the timing.** Over what time period was the data collected, and does it match when the data itself was created (for example, old news articles scraped recently)[^gebru2021datasheets-e20]? For a contamination-resistant evaluation set, this is the core evidence `[Our analysis]`.
4. **Make every item traceable to its source.** SmartBugs' annotated set came from three sources (GitHub repositories, blog posts analyzing contracts, and the Ethereum chain), and recorded the source URL and author of each contract[^durieux2020empirical-e6]. If you used a continuously updated data source, give the version number or search terms in enough detail that others can get the same input and redo the work[^scientificdata2026guidelines-e4].
5. **Say whether the dataset depends on external resources** (websites, tweets, other datasets), and whether those resources will still be there later[^gebru2021datasheets-e11].
6. **Make it big enough to separate systems.** BetterBench recommends that a benchmark be able to reliably detect a 1% improvement[^reuel2024betterbench-e12]; Jason Wei suggests that a large language model evaluation set should ideally have at least 1,000 examples, and more for multiple-choice formats[^wei2024evals-e2]. Size trades off against annotation quality: even ImageNet's authors say its scale limited how much human annotation they could get[^raji2021everything-e9].

**Why:** Biases in where the data comes from go straight into the benchmark. In the 2011 version of ImageNet, 45% of the images came from the United States, and more than 60% came from a handful of Western countries in North America and Europe[^raji2021everything-e6].

**Where people go wrong:** Collecting whatever is at hand. Raji et al. criticize some "general" benchmarks whose tasks look more like convenience samples: the team building the benchmark used whatever was easy to get, even when it had no theoretical justification[^raji2021everything-e3].

### Step 3: Annotate, and check agreement

The general annotation workflow (write annotation guidelines, have several people annotate independently, resolve disagreements, report agreement) is covered in [Mining software repositories: label data manually, and check agreement](../07_fields/computer-science/practices/repository_mining.md#step-6-label-data-manually-and-check-agreement). Here are only the points that matter most when building a dataset.

**How:**

1. **Use several annotators, report how many, describe the annotation process in detail, and assess inter-annotator agreement**[^ralph2020empirical-e111]. Explain how disagreements were resolved, and report agreement with an appropriate statistic[^ralph2020empirical-e129]. Simple percent agreement is not enough, because it doesn't account for agreement that happens by chance[^mcdonald2019reliability-e4].
2. **Use an established taxonomy for labels where you can.** SmartBugs used the existing DASP (Decentralized Application Security Project) Top 10 taxonomy of vulnerabilities, assigned each contract to one category, and manually marked the lines of code containing the vulnerability[^durieux2020empirical-e5]. The authors acknowledge that manual annotation can be wrong; to counter this, every author annotated independently and then they discussed disagreements until they agreed[^durieux2020empirical-e14].
3. **Don't use the methods under evaluation to produce the ground truth.** BetterBench cites the bioinformatics benchmarking literature: the methods being evaluated should not be used to create the gold-standard dataset[^reuel2024betterbench-e19]. For example, if you are evaluating how well large language models and Slither find vulnerabilities, you can't have a large language model or Slither generate the "correct answers" directly; if you use a tool for initial screening, a person must check every item, and the paper must say so `[Our analysis]`.
4. **State who annotated and how they were paid** (for example, what crowdworkers were paid)[^gebru2021datasheets-e13].
5. **Keep the raw data and release the annotation software.** Datasheets ask: besides the processed data, was the raw data saved? Is the software used for preprocessing, cleaning, and labeling available[^gebru2021datasheets-e15]?

**Why:** If an evaluation set has many errors, nobody will trust it[^wei2024evals-e3].

**Where people go wrong:** Calling agreement "good" when it falls below accepted thresholds; computing several agreement measures and reporting only the best-looking one[^ralph2020empirical-e132].

### Step 4: Split the data, and close off leakage and contamination

**How:**

1. **Give recommended training, validation, and test splits, and explain the reasoning**[^gebru2021datasheets-e10]. For why test data may be used only once, at the end, see [Comparative evaluation: keep some data for the final test only](../05_research-strategies/compare_evaluate.md#keep-some-data-for-the-final-test-only); for why you split before any other processing, see [Data science research](data_science.md#step-3-split-the-data-before-doing-anything-else-to-it).
2. **Deduplicate first, then split.** Public data can contain enormous amounts of duplication: SmartBugs' large dataset was checked for duplicates by hashing after removing spaces and tabs, and 95% of the source files turned out to be duplicates[^durieux2020empirical-e8]. Training and test samples that are not independent constitute leakage[^kapoor2023leakage-e6], so near-duplicates should go on the same side of the split `[Our analysis]`.
3. **Split by time.** When the goal is predicting the future, the test set must not contain data older than the training set[^kapoor2023leakage-e5].
4. **Add contamination safeguards to the evaluation set.** Giving evaluation items globally unique identifiers or encrypting them lowers the risk of contamination and of people gaming the benchmark; including a detection task lets you check whether a model's training data contains benchmark items[^reuel2024betterbench-e7]. You can also keep both a public and a private test set and watch whether models perform noticeably differently on the two[^wei2024evals-e9].

**Why:** Once a good evaluation is released, its questions spread all over the web[^wei2024evals-e9]. Benchmark builders can't force model developers to respect "canary strings" (markers embedded in the data that ask people not to train on it); preventing contamination is a shared responsibility of benchmark builders and model developers[^reuel2024betterbench-e16]. For how to check after the fact whether a model has seen an evaluation set, see [Benchmarking: is the benchmark itself valid?](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid).

**Example** `[Our analysis]`: In this project's control evaluation set, the same contract is often copied and deployed many times. First group contracts whose code is identical or nearly identical, and keep each group entirely on one side; then, by deployment date, put contracts deployed after the training cutoff of the models under test into the test set. The paper should state both splitting rules and how many samples each removed.

> **Where sources disagree: static or dynamic benchmarks?**
>
> - Dynamic benchmarks (which keep adding new items) cope better with quick saturation and data contamination, but results from different times are harder to compare[^reuel2024betterbench-e13].
> - Static benchmarks make comparison easy, but some have been saturated within months of release[^reuel2024betterbench-e17].
>
> In practice `[Our analysis]`: most researchers first release a fixed version so the numbers in papers are comparable, and at the same time script the collection and annotation pipeline so new versions can be produced later under the same rules.

### Step 5: Write the documentation (a datasheet)

**How:**

1. **Write a datasheet for the dataset**, recording its motivation, composition, collection process, recommended uses, and so on[^gebru2021datasheets-e1]. The NeurIPS Datasets and Benchmarks Track requires new datasets to come with documentation and intended uses; recommended frameworks include datasheets, dataset nutrition labels, data statements for natural language processing, and data cards[^neurips2024datasets-e3].
2. **Write it as you go, not afterwards.** A datasheet is meant to make dataset creators reflect carefully on the process and risks of creating, distributing, and maintaining the dataset, and to give users enough information to decide whether to use it[^gebru2021datasheets-e2], so it should not be generated automatically[^gebru2021datasheets-e4]. You can skip questions that don't apply[^gebru2021datasheets-e5], but even if you can't answer everything, answer as much as you can rather than writing nothing[^gebru2021datasheets-e6].
3. **State what the dataset should not be used for**[^gebru2021datasheets-e16], and state the normative assumptions and limitations behind it[^reuel2024betterbench-e9].
4. **Explain the files.** Say which repository hosts the data, what files and formats there are, how the directories are organized, and explain any column or variable names users wouldn't understand[^scientificdata2026guidelines-e5].
5. **Provide machine-readable metadata.** NeurIPS 2025 requires datasets to be described in the Croissant format (a machine-readable format for describing datasets) and submitted with the paper[^neurips2025datasets-e3].

**Why:** Datasheets also help reproducibility: someone who can't get the original data can use the datasheet to build a substitute dataset with similar characteristics[^gebru2021datasheets-e3].

**How to structure the paper** `[Our analysis]`: You can borrow the structure of a Scientific Data Descriptor: Background & Summary, Methods, Data Records, Data Overview (optional), Technical Validation, Usage Notes (optional), Data Availability, and Code Availability[^scientificdata2026guidelines-e1]. The Methods section must fully describe the study design, data acquisition, and all computational processing[^scientificdata2026guidelines-e3]. Benchmark papers at machine learning conferences are structured more freely, but reviewers will look for the same content.

### Step 6: Handle licensing, consent, and ethics

For the general requirements when research involves people, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first); for the ethics and licensing issues of mining data from public platforms, see [Mining software repositories: handle ethics and licensing](../07_fields/computer-science/practices/repository_mining.md#step-8-handle-ethics-and-licensing). Building a dataset adds the points below.

**How:**

1. **Interpret "involves people" broadly.** Datasheets suggest that any dataset containing text written by people counts as involving people[^gebru2021datasheets-e12]. By that standard, code comments, commit messages, and Q&A posts all count `[Our analysis]`.
2. **"Downloadable" does not mean "usable."** Using data solely because it is technically accessible and downloadable is an antipattern listed by SIGSOFT[^ralph2020empirical-e135]. When you republish data, explain how you respect the expectations and consent of the data subjects[^ralph2020empirical-e138].
3. **Check upstream restrictions.** Have third parties imposed intellectual property or other restrictions on data you included[^gebru2021datasheets-e17]? If you fold public datasets into your benchmark, check them for ethical problems too; you remain responsible for the ethical consequences of that data[^neurips2024datasets-e11]. Also learn and follow the legal requirements on data in your jurisdiction[^neurips2024datasets-e15].
4. **Choose a license.** NeurIPS requires authors to choose a license, preferably a Creative Commons (CC) license for datasets and an open-source license for code[^neurips2024datasets-e4]. The license and terms of use should take intended uses and limitations into account to prevent misuse[^neurips2024datasets-e9].
5. **Get consent when real people are involved.** The dataset should expose as little personally identifiable information as possible; using real data about real people requires explicit consent, or an explanation of why it couldn't be obtained[^neurips2024datasets-e10]. Datasheets also ask how consent was obtained[^gebru2021datasheets-e14] and whether there was an ethics review[^gebru2021datasheets-e13].

**Sensitive data need not be fully public.** The FAIR principles note that highly sensitive or personally identifiable data can still reach a high degree of FAIRness without being public itself, as long as detailed metadata and the access rules are public[^wilkinson2016fair-e5]. NeurIPS allows requiring users to be credentialed before access when this is genuinely necessary in the public interest (for example, ethically sensitive medical data), but only as an exception, not as a way to restrict access[^neurips2024datasets-e12].

**Where people go wrong** `[Our analysis]`: When collecting code from GitHub, checking only that it is "public" and not whether each repository's open-source license allows redistribution. If in doubt, release only the repository URLs, commit hashes, and a download script, and let users download the code themselves.

### Step 7: Release it, and make sure it stays available

**How:**

1. **Make it available at review time.** NeurIPS 2025 requires data and code to be accessible to reviewers at submission, without having to ask the authors privately; the code must be documented and runnable; submissions that don't comply can be desk-rejected[^neurips2025datasets-e1]. Scientific Data requires the data to be anonymously downloadable for the first round of review, and from the second round on it must be publicly deposited in a proper data repository[^scientificdata2026guidelines-e8].
2. **Put it on a dedicated data platform or repository.** NeurIPS 2025 requires new datasets to be hosted on dedicated machine learning data platforms such as Dataverse, Kaggle, Hugging Face, or OpenML, with a custom website only when genuinely needed[^neurips2025datasets-e2]. You must explain how the dataset will remain available long term: deposit it in a data repository, or explain how you will ensure it yourself[^neurips2024datasets-e4].
3. **Get a persistent identifier.** Giving the dataset a resolvable persistent identifier, such as a DOI (digital object identifier) assigned by a data repository, is strongly recommended[^neurips2024datasets-e5]. The first FAIR principle is that data and metadata have globally unique, persistent identifiers[^wilkinson2016fair-e3]; on release, the data should also carry a clear usage license and detailed provenance[^wilkinson2016fair-e4].
4. **Release a benchmark together with its evaluation code.** Provide runnable evaluation code, the evaluation data or prompts, and scripts that reproduce the paper's results[^reuel2024betterbench-e8]; provide the benchmark in a ready-to-use form so others can reproduce results independently[^ralph2020empirical-e151]. For how to organize code, data, and results, see [Organizing your research materials](../08_throughout/organizing_materials.md).

**Why:** These requirements are often ignored. Of the 24 benchmarks BetterBench assessed, 17 provided no easy-to-run reproduction scripts, and 14 neither evaluated the same model multiple times nor reported significance or uncertainty[^reuel2024betterbench-e14].

### Step 8: Maintenance, versioning, and retirement

**How:**

1. **Write a maintenance plan in advance**: will the dataset be updated (fixing labeling errors, adding or removing instances), how often, by whom, and how will users be told; will older versions stay available[^gebru2021datasheets-e18]? NeurIPS requires new datasets to come with hosting, licensing, and maintenance plans[^neurips2024datasets-e3].
2. **Provide a feedback channel and a contact person, and check regularly that the code still runs**[^reuel2024betterbench-e10].
3. **Bump the version whenever you change it.** Mark small updates (such as removing faulty items) with a version number; release a new version for major updates[^reuel2024betterbench-e11]. Every new version comes with an updated datasheet[^gebru2021datasheets-e19].
4. **Retire it explicitly when the time comes.** Benchmarks get phased out when they are saturated, when the task stops mattering, or when a better alternative appears[^reuel2024betterbench-e3]; when you stop maintaining one, state in its official release materials that it is retired[^reuel2024betterbench-e10].

**Example** `[Our analysis]`: This project's control evaluation set is released as v1.0. Later, someone reports through the feedback channel that the vulnerable line numbers for three contracts are wrong; after fixing them you release v1.1 and list the changed items in the changelog, and later papers state which version they used. Once a new generation of models has a training cutoff later than the deployment dates of these contracts, this version no longer means "unseen"; you should state that it is no longer suitable for contamination-resistant evaluation, and collect a new batch of contracts under the same rules.

---

## 3. Checklist

This checklist is based mainly on the requirements of the NeurIPS Datasets and Benchmarks Track, datasheets, and the BetterBench criteria, supplemented by the SIGSOFT benchmarking standard. These are all machine learning and software engineering requirements; if you are submitting to a data journal in another field, follow that journal's rules `[Our analysis]`.

**Must do**

- [ ] Explain why the dataset was built and what gap it fills[^gebru2021datasheets-e7], and how it differs from existing benchmarks[^reuel2024betterbench-e4]
- [ ] For a new benchmark, state the quality measured, the metric, the measurement method, and the workload[^ralph2020empirical-e147]
- [ ] Describe in enough detail how the data was collected and organized, what information it contains, and how it will be provided and maintained[^neurips2024datasets-e8]
- [ ] Submit dataset documentation and intended uses, plus hosting, licensing, and maintenance plans[^neurips2024datasets-e3]
- [ ] Choose a clear license and explain the long-term preservation plan[^neurips2024datasets-e4]
- [ ] Data and code are accessible at review time, without private requests[^neurips2025datasets-e1]
- [ ] If real people are involved: expose as little personal information as possible, and get explicit consent or explain why you couldn't[^neurips2024datasets-e10]
- [ ] If there is manual annotation: several annotators, a documented process, and assessed agreement[^ralph2020empirical-e111]
- [ ] Discuss construct validity: does the benchmark measure what it is meant to measure[^ralph2020empirical-e100]
- [ ] The benchmark's results are easy to reproduce[^neurips2024datasets-e6]

**Better practice**

- [ ] Get a persistent identifier (such as a DOI)[^neurips2024datasets-e5]
- [ ] Provide machine-readable metadata (such as Croissant)[^neurips2025datasets-e3]
- [ ] Provide evaluation code and scripts that reproduce the paper's results[^reuel2024betterbench-e8]
- [ ] Report the metric's floor, ceiling, human performance, and random performance[^reuel2024betterbench-e6]
- [ ] Give recommended data splits and explain them[^gebru2021datasheets-e10]
- [ ] Keep the raw data and release the processing and annotation software[^gebru2021datasheets-e15]
- [ ] Take contamination safeguards, such as giving evaluation items unique identifiers or encrypting them[^reuel2024betterbench-e7]
- [ ] Provide a feedback channel and contact person[^reuel2024betterbench-e10]; mark versions when you update[^reuel2024betterbench-e11]

**Outstanding**

- [ ] Use empirical evidence to show the benchmark is relevant (for example, a systematic review) and usable (for example, action research or case studies)[^ralph2020empirical-e154]
- [ ] Report that results have been independently reproduced, that the benchmark has a sizable user community, and that an independent organization maintains it[^ralph2020empirical-e153]

**Fine to skip; not a flaw**

- Datasheet questions that don't apply to your dataset can be skipped[^gebru2021datasheets-e5]
- A new benchmark with few users so far, no independent reproduction, and no independent maintainer: SIGSOFT considers these invalid criticisms, since a "prototype benchmark" built by a small group of researchers can itself move the discussion forward[^ralph2020empirical-e159]
- For sensitive data, publishing detailed metadata and access rules instead of the data itself[^wilkinson2016fair-e5]

This checklist is only a minimum. The BetterBench authors also say their criteria are a minimum quality bar; whether a benchmark really measures the concept it is meant to measure takes in-depth analysis by domain experts[^reuel2024betterbench-e18]. For this, see [Benchmarking: is the benchmark itself valid?](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid).

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Claiming the benchmark measures "general ability" | No dataset is neutral; "general" often becomes an excuse for not reporting limitations[^raji2021everything-e5] |
| Collecting whatever data is at hand | You get a convenience sample with no theoretical justification[^raji2021everything-e3] |
| Reporting only one overall score | It can hide poor model performance on small subgroups[^raji2021everything-e7] |
| Using the tools or models under evaluation to generate the ground truth | The methods being evaluated should not be used to create the gold standard[^reuel2024betterbench-e19] |
| Splitting into training and test sets without deduplicating | Duplicates land on both sides, so training and test data are not independent, which is leakage[^kapoor2023leakage-e6] |
| Only one annotator, or only percent agreement reported | Percent agreement doesn't account for chance agreement[^mcdonald2019reliability-e4]; the standard requires several annotators and an agreement assessment[^ralph2020empirical-e111] |
| "It's public and downloadable, so we can use it" | Being technically accessible doesn't mean you may legally use it[^ralph2020empirical-e135] |
| No license, or hosting on a personal cloud drive | Both the license and long-term preservation must be stated[^neurips2024datasets-e4] |
| Writing the datasheet at the very end, or generating it automatically | Read the questions before collecting[^gebru2021datasheets-e8]; writing a datasheet should not be automated[^gebru2021datasheets-e4] |
| Quietly changing the dataset without bumping the version | Others' results can no longer be compared; mark small changes with a version number and release a new version for big ones[^reuel2024betterbench-e11] |

---

## 5. Further reading

- **Datasheets**: Gebru et al. 2021, Datasheets for Datasets. Lists the questions to answer in seven groups (motivation, composition, collection, processing, uses, distribution, maintenance), with a sample datasheet. It comes from machine learning, but most of the questions apply anywhere.
- **How machine learning conferences review datasets**: the call for papers of the NeurIPS Datasets and Benchmarks Track. The 2024 version lists the factors reviewers consider; the 2025 version adds requirements such as making data and code public at submission and describing metadata in Croissant. It changes every year, so go by the current year's page.
- **A quality checklist for benchmarks**: Reuel et al. 2024, BetterBench. 46 criteria organized by stage of the benchmark life cycle, with a checklist for benchmark builders in the appendix; the website keeps updating its scores for individual benchmarks.
- **What benchmarks can and can't show**: Raji et al. 2021, which uses ImageNet and GLUE (the General Language Understanding Evaluation benchmark) as examples to criticize treating one benchmark as a measure of "general ability."
- **Publishing data across disciplines**: Wilkinson et al. 2016, the FAIR data principles, and the submission guidelines of Scientific Data (the structure and requirements of Data Descriptor papers).
- **A worked example from smart contracts**: Durieux et al. 2020 (SmartBugs), which documents its sources, annotation method, and deduplication steps clearly.
- **Using benchmarks for evaluation**: [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) in this handbook.

Links to all sources are in the [source list](../../sources/README.md).

[^raji2021everything-e1]: Raji et al. 2021, §2.2. [Evidence](../../sources/notes/raji2021everything.md#e1)
[^raji2021everything-e3]: Raji et al. 2021, §4.1. [Evidence](../../sources/notes/raji2021everything.md#e3)
[^raji2021everything-e4]: Raji et al. 2021, §4.1.1. [Evidence](../../sources/notes/raji2021everything.md#e4)
[^raji2021everything-e5]: Raji et al. 2021, §4.2. [Evidence](../../sources/notes/raji2021everything.md#e5)
[^raji2021everything-e6]: Raji et al. 2021, §4.2.2. [Evidence](../../sources/notes/raji2021everything.md#e6)
[^raji2021everything-e7]: Raji et al. 2021, §4.3.3. [Evidence](../../sources/notes/raji2021everything.md#e7)
[^raji2021everything-e8]: Raji et al. 2021, §5. [Evidence](../../sources/notes/raji2021everything.md#e8)
[^raji2021everything-e9]: Raji et al. 2021, §4.2.1. [Evidence](../../sources/notes/raji2021everything.md#e9)
[^ralph2020empirical-e100]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e100)
[^ralph2020empirical-e111]: SIGSOFT Repository Mining standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e111)
[^ralph2020empirical-e129]: SIGSOFT Empirical Standards, Inter-Rater Reliability and Agreement Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e129)
[^ralph2020empirical-e132]: SIGSOFT Empirical Standards, Inter-Rater Reliability and Agreement Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e132)
[^ralph2020empirical-e135]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e135)
[^ralph2020empirical-e138]: SIGSOFT Ethics (Studies with Secondary Human Data) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e138)
[^ralph2020empirical-e147]: SIGSOFT Benchmarking standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e147)
[^ralph2020empirical-e151]: SIGSOFT Benchmarking standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e151)
[^ralph2020empirical-e153]: SIGSOFT Benchmarking standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e153)
[^ralph2020empirical-e154]: SIGSOFT Benchmarking standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e154)
[^ralph2020empirical-e159]: SIGSOFT Benchmarking standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e159)
[^neurips2024datasets-e3]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, Submission Instructions. [Evidence](../../sources/notes/neurips2024datasets.md#e3)
[^neurips2024datasets-e4]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, Submission Instructions. [Evidence](../../sources/notes/neurips2024datasets.md#e4)
[^neurips2024datasets-e5]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, Submission Instructions. [Evidence](../../sources/notes/neurips2024datasets.md#e5)
[^neurips2024datasets-e6]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, Submission Instructions. [Evidence](../../sources/notes/neurips2024datasets.md#e6)
[^neurips2024datasets-e8]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, review criteria. [Evidence](../../sources/notes/neurips2024datasets.md#e8)
[^neurips2024datasets-e9]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, review criteria. [Evidence](../../sources/notes/neurips2024datasets.md#e9)
[^neurips2024datasets-e10]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, review criteria. [Evidence](../../sources/notes/neurips2024datasets.md#e10)
[^neurips2024datasets-e11]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, review criteria. [Evidence](../../sources/notes/neurips2024datasets.md#e11)
[^neurips2024datasets-e12]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, FAQ. [Evidence](../../sources/notes/neurips2024datasets.md#e12)
[^neurips2024datasets-e13]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, FAQ. [Evidence](../../sources/notes/neurips2024datasets.md#e13)
[^neurips2024datasets-e15]: NeurIPS 2024 Datasets and Benchmarks Track call for papers, review criteria. [Evidence](../../sources/notes/neurips2024datasets.md#e15)
[^neurips2025datasets-e1]: NeurIPS 2025 Datasets and Benchmarks Track call for papers, Access. [Evidence](../../sources/notes/neurips2025datasets.md#e1)
[^neurips2025datasets-e2]: NeurIPS 2025 Datasets and Benchmarks Track call for papers, Hosting. [Evidence](../../sources/notes/neurips2025datasets.md#e2)
[^neurips2025datasets-e3]: NeurIPS 2025 Datasets and Benchmarks Track call for papers, Metadata. [Evidence](../../sources/notes/neurips2025datasets.md#e3)
[^scientificdata2026guidelines-e1]: Scientific Data submission guidelines, Format outline. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e1)
[^scientificdata2026guidelines-e2]: Scientific Data submission guidelines, Background & Summary. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e2)
[^scientificdata2026guidelines-e3]: Scientific Data submission guidelines, Methods. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e3)
[^scientificdata2026guidelines-e4]: Scientific Data submission guidelines, Methods. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e4)
[^scientificdata2026guidelines-e5]: Scientific Data submission guidelines, Data Record. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e5)
[^scientificdata2026guidelines-e6]: Scientific Data submission guidelines, Data Overview. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e6)
[^scientificdata2026guidelines-e7]: Scientific Data submission guidelines, Technical Validation. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e7)
[^scientificdata2026guidelines-e8]: Scientific Data submission guidelines, Deposit the dataset. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e8)
[^scientificdata2026guidelines-e10]: Scientific Data submission guidelines, Scope. [Evidence](../../sources/notes/scientificdata2026guidelines.md#e10)
[^durieux2020empirical-e1]: Durieux et al. 2020, §1, p. 1. [Evidence](../../sources/notes/durieux2020empirical.md#e1)
[^durieux2020empirical-e2]: Durieux et al. 2020, §1, p. 2. [Evidence](../../sources/notes/durieux2020empirical.md#e2)
[^durieux2020empirical-e5]: Durieux et al. 2020, §2.3.1, p. 3. [Evidence](../../sources/notes/durieux2020empirical.md#e5)
[^durieux2020empirical-e6]: Durieux et al. 2020, §2.3.1, pp. 3–4. [Evidence](../../sources/notes/durieux2020empirical.md#e6)
[^durieux2020empirical-e8]: Durieux et al. 2020, §2.3.2, p. 4. [Evidence](../../sources/notes/durieux2020empirical.md#e8)
[^durieux2020empirical-e14]: Durieux et al. 2020, §4.2, p. 10. [Evidence](../../sources/notes/durieux2020empirical.md#e14)
[^reuel2024betterbench-e3]: Reuel et al. 2024, Fig. 1 and Appendix B. [Evidence](../../sources/notes/reuel2024betterbench.md#e3)
[^reuel2024betterbench-e4]: Reuel et al. 2024, §4.1. [Evidence](../../sources/notes/reuel2024betterbench.md#e4)
[^reuel2024betterbench-e5]: Reuel et al. 2024, §4.1. [Evidence](../../sources/notes/reuel2024betterbench.md#e5)
[^reuel2024betterbench-e6]: Reuel et al. 2024, §4.1. [Evidence](../../sources/notes/reuel2024betterbench.md#e6)
[^reuel2024betterbench-e7]: Reuel et al. 2024, §4.2. [Evidence](../../sources/notes/reuel2024betterbench.md#e7)
[^reuel2024betterbench-e8]: Reuel et al. 2024, §4.2. [Evidence](../../sources/notes/reuel2024betterbench.md#e8)
[^reuel2024betterbench-e9]: Reuel et al. 2024, §4.3. [Evidence](../../sources/notes/reuel2024betterbench.md#e9)
[^reuel2024betterbench-e10]: Reuel et al. 2024, §4.4. [Evidence](../../sources/notes/reuel2024betterbench.md#e10)
[^reuel2024betterbench-e11]: Reuel et al. 2024, §5, Versioning. [Evidence](../../sources/notes/reuel2024betterbench.md#e11)
[^reuel2024betterbench-e12]: Reuel et al. 2024, §5, Detecting small improvements. [Evidence](../../sources/notes/reuel2024betterbench.md#e12)
[^reuel2024betterbench-e13]: Reuel et al. 2024, §5, Dynamic vs. static benchmarks. [Evidence](../../sources/notes/reuel2024betterbench.md#e13)
[^reuel2024betterbench-e14]: Reuel et al. 2024, §7. [Evidence](../../sources/notes/reuel2024betterbench.md#e14)
[^reuel2024betterbench-e15]: Reuel et al. 2024, §7. [Evidence](../../sources/notes/reuel2024betterbench.md#e15)
[^reuel2024betterbench-e16]: Reuel et al. 2024, §8, Contamination. [Evidence](../../sources/notes/reuel2024betterbench.md#e16)
[^reuel2024betterbench-e17]: Reuel et al. 2024, §8, Quick saturation. [Evidence](../../sources/notes/reuel2024betterbench.md#e17)
[^reuel2024betterbench-e18]: Reuel et al. 2024, §9. [Evidence](../../sources/notes/reuel2024betterbench.md#e18)
[^reuel2024betterbench-e19]: Reuel et al. 2024, §2.2. [Evidence](../../sources/notes/reuel2024betterbench.md#e19)
[^gebru2021datasheets-e1]: Gebru et al. 2021, §1. [Evidence](../../sources/notes/gebru2021datasheets.md#e1)
[^gebru2021datasheets-e2]: Gebru et al. 2021, §1.1. [Evidence](../../sources/notes/gebru2021datasheets.md#e2)
[^gebru2021datasheets-e3]: Gebru et al. 2021, §1.1. [Evidence](../../sources/notes/gebru2021datasheets.md#e3)
[^gebru2021datasheets-e4]: Gebru et al. 2021, §1.1. [Evidence](../../sources/notes/gebru2021datasheets.md#e4)
[^gebru2021datasheets-e5]: Gebru et al. 2021, §3. [Evidence](../../sources/notes/gebru2021datasheets.md#e5)
[^gebru2021datasheets-e6]: Gebru et al. 2021, §3. [Evidence](../../sources/notes/gebru2021datasheets.md#e6)
[^gebru2021datasheets-e7]: Gebru et al. 2021, §3.1. [Evidence](../../sources/notes/gebru2021datasheets.md#e7)
[^gebru2021datasheets-e8]: Gebru et al. 2021, §3.2. [Evidence](../../sources/notes/gebru2021datasheets.md#e8)
[^gebru2021datasheets-e9]: Gebru et al. 2021, §3.2. [Evidence](../../sources/notes/gebru2021datasheets.md#e9)
[^gebru2021datasheets-e10]: Gebru et al. 2021, §3.2. [Evidence](../../sources/notes/gebru2021datasheets.md#e10)
[^gebru2021datasheets-e11]: Gebru et al. 2021, §3.2. [Evidence](../../sources/notes/gebru2021datasheets.md#e11)
[^gebru2021datasheets-e12]: Gebru et al. 2021, §3.2. [Evidence](../../sources/notes/gebru2021datasheets.md#e12)
[^gebru2021datasheets-e13]: Gebru et al. 2021, §3.3. [Evidence](../../sources/notes/gebru2021datasheets.md#e13)
[^gebru2021datasheets-e14]: Gebru et al. 2021, §3.3. [Evidence](../../sources/notes/gebru2021datasheets.md#e14)
[^gebru2021datasheets-e15]: Gebru et al. 2021, §3.4. [Evidence](../../sources/notes/gebru2021datasheets.md#e15)
[^gebru2021datasheets-e16]: Gebru et al. 2021, §3.5. [Evidence](../../sources/notes/gebru2021datasheets.md#e16)
[^gebru2021datasheets-e17]: Gebru et al. 2021, §3.6. [Evidence](../../sources/notes/gebru2021datasheets.md#e17)
[^gebru2021datasheets-e18]: Gebru et al. 2021, §3.7. [Evidence](../../sources/notes/gebru2021datasheets.md#e18)
[^gebru2021datasheets-e19]: Gebru et al. 2021, §4. [Evidence](../../sources/notes/gebru2021datasheets.md#e19)
[^gebru2021datasheets-e20]: Gebru et al. 2021, §3.3. [Evidence](../../sources/notes/gebru2021datasheets.md#e20)
[^wei2024evals-e2]: Jason Wei 2024, common mistakes in evaluations. [Evidence](../../sources/notes/wei2024evals.md#e2)
[^wei2024evals-e3]: Jason Wei 2024, common mistakes in evaluations. [Evidence](../../sources/notes/wei2024evals.md#e3)
[^wei2024evals-e9]: Jason Wei 2024, test set contamination. [Evidence](../../sources/notes/wei2024evals.md#e9)
[^mcdonald2019reliability-e4]: McDonald et al. 2019, §2.2. [Evidence](../../sources/notes/mcdonald2019reliability.md#e4)
[^kapoor2023leakage-e5]: Kapoor & Narayanan 2023, leakage taxonomy, L3.1. [Evidence](../../sources/notes/kapoor2023leakage.md#e5)
[^kapoor2023leakage-e6]: Kapoor & Narayanan 2023, leakage taxonomy, L3.2. [Evidence](../../sources/notes/kapoor2023leakage.md#e6)
[^wilkinson2016fair-e3]: Wilkinson et al. 2016, Box 2. [Evidence](../../sources/notes/wilkinson2016fair.md#e3)
[^wilkinson2016fair-e4]: Wilkinson et al. 2016, Box 2. [Evidence](../../sources/notes/wilkinson2016fair.md#e4)
[^wilkinson2016fair-e5]: Wilkinson et al. 2016, The FAIR Guiding Principles in detail. [Evidence](../../sources/notes/wilkinson2016fair.md#e5)
