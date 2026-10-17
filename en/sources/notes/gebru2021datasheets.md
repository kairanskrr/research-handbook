# Gebru et al. 2021: Datasheets for Datasets

- Source: `gebru2021datasheets`, [original (arXiv:1803.09010v8)](https://arxiv.org/abs/1803.09010)
- Version: arXiv v8 (December 1, 2021). Formally published in Communications of the ACM 64(12): 86–92, 2021 (DOI 10.1145/3458723, checked against Crossref). Locations give section numbers in the arXiv version.
- Note: From machine learning. Proposes that every dataset come with a datasheet: a set of questions documenting the dataset's motivation, composition, collection, preprocessing, uses, distribution and maintenance.

### E1

- Location: §1 Introduction
- Quote: "By analogy, we propose that every dataset be accompanied with a datasheet that documents its motivation, composition, collection process, recommended uses, and so on."
- Key point: By analogy with datasheets for electronic components, the authors propose that every dataset come with a datasheet recording its motivation, composition, collection process, recommended uses and so on.

### E2

- Location: §1.1 Objectives
- Quote: "For dataset creators, the primary objective is to encourage careful reflection on the process of creating, distributing, and maintaining a dataset, including any underlying assumptions, potential risks or harms, and implications of use. For dataset consumers, the primary objective is to ensure they have the information they need to make informed decisions about using a dataset."
- Key point: For dataset creators, a datasheet prompts careful reflection on how the dataset is created, distributed and maintained and on its risks; for dataset users, it provides the information needed to decide whether to use it.

### E3

- Location: §1.1 Objectives
- Quote: "They also serve a secondary objective of facilitating greater reproducibility of machine learning results: researchers and practitioners without access to a dataset may be able to use the information in its datasheet to create alternative datasets with similar characteristics."
- Key point: Datasheets also aid reproducibility: people who cannot access the original data can use the datasheet to build an alternative dataset with similar characteristics.

### E4

- Location: §1.1 Objectives
- Quote: "We emphasize that the process of creating a datasheet is not intended to be automated."
- Key point: Writing a datasheet is not meant to be automated, because its purpose is to make dataset creators reflect carefully.

### E5

- Location: §3 Questions and Workflow
- Quote: "The questions are grouped into sections that roughly match the key stages of the dataset lifecycle: motivation, composition, collection process, preprocessing/cleaning/labeling, uses, distribution, and maintenance." / "We note that not all questions will be applicable to all datasets; those that do not apply should be skipped."
- Key point: The questions are grouped into seven sections following the dataset lifecycle: motivation, composition, collection process, preprocessing/cleaning/labeling, uses, distribution and maintenance; questions that do not apply can be skipped.

### E6

- Location: §3 Questions and Workflow
- Quote: "We recommend answering as many questions as possible rather than skipping the datasheet creation process entirely."
- Key point: Answer as many questions as you can rather than skipping the datasheet altogether.

### E7

- Location: §3.1 Motivation
- Quote: "For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description."
- Key point: The motivation section starts by asking why the dataset was created, for what task, and what gap it fills.

### E8

- Location: §3.2 Composition
- Quote: "Dataset creators should read through these questions prior to any data collection and then provide answers once data collection is complete."
- Key point: Read the composition questions before collecting any data, and answer them once collection is complete.

### E9

- Location: §3.2 Composition
- Quote: "Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)?"
- Key point: State whether the dataset contains all instances or a sample from a larger set; if a sample, say what the larger set is and whether the sample is representative.

### E10

- Location: §3.2 Composition
- Quote: "Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them."
- Key point: If there are recommended training, validation and test splits, describe them and explain the rationale.

### E11

- Location: §3.2 Composition
- Quote: "Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description." / "Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?"
- Key point: Describe any errors, noise and redundancies in the data, and say whether the dataset is self-contained or relies on external resources such as websites, tweets or other datasets.

### E12

- Location: §3.2 Composition
- Quote: "We recommend taking a broad interpretation of whether a dataset relates to people. For example, any dataset containing text that was written by people relates to people."
- Key point: Interpret "relates to people" broadly: any dataset containing text written by people counts.

### E13

- Location: §3.3 Collection Process
- Quote: "Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?" / "Were any ethical review processes conducted (e.g., by an institutional review board)?"
- Key point: State who took part in data collection and how they were paid (for example, how much crowdworkers earned), and whether there was an ethical review.

### E14

- Location: §3.3 Collection Process
- Quote: "Did the individuals in question consent to the collection and use of their data? If so, please describe (or show with screenshots or other information) how consent was requested and provided"
- Key point: For data about people, state whether they consented to the collection and use of their data and how consent was obtained.

### E15

- Location: §3.4 Preprocessing/cleaning/labeling
- Quote: "Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?" / "Is the software that was used to preprocess/clean/label the data available?"
- Key point: State whether the raw data were kept alongside the processed data, and whether the software used for preprocessing, cleaning and labeling is available.

### E16

- Location: §3.5 Uses
- Quote: "Are there tasks for which the dataset should not be used? If so, please provide a description."
- Key point: State which tasks the dataset should not be used for.

### E17

- Location: §3.6 Distribution
- Quote: "Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?" / "Have any third parties imposed IP-based or other restrictions on the data associated with the instances?"
- Key point: Before distribution, state the copyright license or terms of use, and whether third parties have placed intellectual property or other restrictions on the data.

### E18

- Location: §3.7 Maintenance
- Quote: "Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)? If so, please describe how often, by whom, and how updates will be communicated to dataset consumers" / "Will older versions of the dataset continue to be supported/hosted/maintained?"
- Key point: The maintenance section asks whether the dataset will be updated (fixing labeling errors, adding or removing instances), how often, by whom, and how users will be told, and whether older versions will remain available.

### E19

- Location: §4 Impact and Challenges
- Quote: "If a dataset changes only infrequently, we recommend accompanying updated versions with updated datasheets."
- Key point: When a dataset changes only occasionally, each new version should come with an updated datasheet.

### E20

- Location: §3.3 Collection Process
- Quote: "Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)?"
- Key point: State when the data were collected and whether that matches when the data themselves were created (for example, a recent crawl of old news articles).

### E21

- Location: §4 Impact and Challenges
- Quote: "Datasheets for datasets do not provide a complete solution to mitigating unwanted societal biases or potential risks or harms. Dataset creators cannot anticipate every possible use of a dataset"
- Key point: Datasheets do not fully solve problems of bias and risk, since dataset creators cannot anticipate every use.
