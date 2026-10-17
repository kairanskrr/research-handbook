# Gebru 等人 2021：Datasheets for Datasets

- 资料：`gebru2021datasheets`，[原文（arXiv:1803.09010v8）](https://arxiv.org/abs/1803.09010)
- 版本：arXiv v8（2021 年 12 月 1 日）。正式发表于 Communications of the ACM 64(12): 86–92，2021（DOI 10.1145/3458723，已通过 Crossref 核对）。位置写 arXiv 版的章节号。
- 说明：出自机器学习方向。提出每个数据集都附一份"数据表"（datasheet），用一组问题记录数据集的动机、组成、收集、处理、用途、分发和维护。

### E1

- 位置：§1 Introduction
- 原文："By analogy, we propose that every dataset be accompanied with a datasheet that documents its motivation, composition, collection process, recommended uses, and so on."
- 要点：仿照电子元件的数据手册，提议每个数据集都附一份数据表，记录动机、组成、收集过程、推荐用途等。

### E2

- 位置：§1.1 Objectives
- 原文："For dataset creators, the primary objective is to encourage careful reflection on the process of creating, distributing, and maintaining a dataset, including any underlying assumptions, potential risks or harms, and implications of use. For dataset consumers, the primary objective is to ensure they have the information they need to make informed decisions about using a dataset."
- 要点：数据表对建数据集的人，是促使他们认真反思创建、分发、维护的过程和风险；对用数据集的人，是让他们有足够信息决定用不用。

### E3

- 位置：§1.1 Objectives
- 原文："They also serve a secondary objective of facilitating greater reproducibility of machine learning results: researchers and practitioners without access to a dataset may be able to use the information in its datasheet to create alternative datasets with similar characteristics."
- 要点：数据表还有助于复现：拿不到原数据的人，可以照数据表的信息建一个特征相似的替代数据集。

### E4

- 位置：§1.1 Objectives
- 原文："We emphasize that the process of creating a datasheet is not intended to be automated."
- 要点：写数据表不应该自动化，因为目的就是让建数据集的人认真反思。

### E5

- 位置：§3 Questions and Workflow
- 原文："The questions are grouped into sections that roughly match the key stages of the dataset lifecycle: motivation, composition, collection process, preprocessing/cleaning/labeling, uses, distribution, and maintenance." / "We note that not all questions will be applicable to all datasets; those that do not apply should be skipped."
- 要点：问题按数据集生命周期分成七组：动机、组成、收集过程、预处理/清洗/标注、用途、分发、维护；不适用的问题可以跳过。

### E6

- 位置：§3 Questions and Workflow
- 原文："We recommend answering as many questions as possible rather than skipping the datasheet creation process entirely."
- 要点：答不全也要尽量多答，而不是干脆不写数据表。

### E7

- 位置：§3.1 Motivation
- 原文："For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description."
- 要点：动机部分先问：为什么建这个数据集，针对什么任务，填补了什么空白。

### E8

- 位置：§3.2 Composition
- 原文："Dataset creators should read through these questions prior to any data collection and then provide answers once data collection is complete."
- 要点：组成部分的问题要在收集数据之前就读一遍，收集完再回答。

### E9

- 位置：§3.2 Composition
- 原文："Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)?"
- 要点：要说明数据集是全部实例还是从更大集合中抽的样本；是样本的话，更大的集合是什么，样本是否有代表性。

### E10

- 位置：§3.2 Composition
- 原文："Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them."
- 要点：有推荐的训练、验证、测试划分时，要描述划分方式并说明理由。

### E11

- 位置：§3.2 Composition
- 原文："Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description." / "Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?"
- 要点：要说明数据中的错误、噪声和冗余；以及数据集是自足的，还是依赖网站、推文、其他数据集等外部资源。

### E12

- 位置：§3.2 Composition
- 原文："We recommend taking a broad interpretation of whether a dataset relates to people. For example, any dataset containing text that was written by people relates to people."
- 要点：判断数据集是否"涉及人"要从宽：只要含有人写的文字，就算涉及人。

### E13

- 位置：§3.3 Collection Process
- 原文："Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?" / "Were any ethical review processes conducted (e.g., by an institutional review board)?"
- 要点：要写明谁参与了数据收集、报酬多少（例如众包工人拿多少钱），以及是否经过伦理审查。

### E14

- 位置：§3.3 Collection Process
- 原文："Did the individuals in question consent to the collection and use of their data? If so, please describe (or show with screenshots or other information) how consent was requested and provided"
- 要点：涉及人的数据，要说明当事人是否同意收集和使用，以及怎样征得同意。

### E15

- 位置：§3.4 Preprocessing/cleaning/labeling
- 原文："Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?" / "Is the software that was used to preprocess/clean/label the data available?"
- 要点：要说明是否在处理后的数据之外保存了原始数据，以及预处理、清洗、标注用的软件是否公开。

### E16

- 位置：§3.5 Uses
- 原文："Are there tasks for which the dataset should not be used? If so, please provide a description."
- 要点：要写明这个数据集不应该用于哪些任务。

### E17

- 位置：§3.6 Distribution
- 原文："Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?" / "Have any third parties imposed IP-based or other restrictions on the data associated with the instances?"
- 要点：分发前要说明数据集用什么版权许可或使用条款发布，以及第三方是否对其中的数据施加了知识产权或其他限制。

### E18

- 位置：§3.7 Maintenance
- 原文："Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)? If so, please describe how often, by whom, and how updates will be communicated to dataset consumers" / "Will older versions of the dataset continue to be supported/hosted/maintained?"
- 要点：维护部分问：是否会更新（修正标注错误、增删实例），多久一次、由谁负责、怎样通知用户；旧版本是否继续保留。

### E19

- 位置：§4 Impact and Challenges
- 原文："If a dataset changes only infrequently, we recommend accompanying updated versions with updated datasheets."
- 要点：数据集偶尔更新时，每个新版本都应附上更新后的数据表。

### E20

- 位置：§3.3 Collection Process
- 原文："Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)?"
- 要点：要写明数据收集的时间段，以及它和数据本身产生的时间是否一致（例如最近才抓取的旧新闻）。

### E21

- 位置：§4 Impact and Challenges
- 原文："Datasheets for datasets do not provide a complete solution to mitigating unwanted societal biases or potential risks or harms. Dataset creators cannot anticipate every possible use of a dataset"
- 要点：数据表不能完全解决偏见和风险问题，建数据集的人无法预料所有用法。
