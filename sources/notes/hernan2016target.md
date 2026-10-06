# Hernán & Robins 2016：Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available

- 资料：`hernan2016target`，[PubMed Central 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/)
- 版本：American Journal of Epidemiology 183(8): 758–764，2016。

### E1

- 位置：Abstract
- 原文："When we cannot conduct a randomized experiment, we analyze observational data. Causal inference from large observational databases (big data) can be viewed as an attempt to emulate a randomized experiment—the target experiment or target trial—that would answer the question of interest."
- 要点：做不了随机试验时，就分析观察性数据；用大型观察性数据库做因果推断，可以看作是在模拟一个能回答该问题的随机试验，即"目标试验"。

### E2

- 位置：正文引言（Table 1 说明）
- 原文："Table 1 lists 7 key components of the target trial protocol: the eligibility criteria, treatment strategies being compared (including their start and end times), assignment procedures, follow-up period, outcome of interest, causal contrast(s) of interest, and analysis plan."
- 要点：目标试验方案有 7 个关键部分：纳入标准、所比较的处理策略（含起止时间）、分配方式、随访期、关心的结局、关心的因果对比、分析计划。

### E3

- 位置：Eligibility criteria
- 原文："Note that the eligibility criteria cannot include restrictions based on postbaseline events (e.g., “include only individuals who ever used therapy during the follow-up”), which may introduce bias"
- 要点：纳入标准不能依据基线之后才发生的事件（例如"只纳入随访期间用过这种疗法的人"），否则可能带来偏倚。

### E4

- 位置：EMULATING THE TARGET TRIAL（开头）
- 原文："For example, the code “breast cancer” might have been recorded in the database when a woman was diagnosed with breast cancer or simply when her physician suspected breast cancer and ordered a diagnostic test. Hence, researchers unfamiliar with the data must both consult with knowledgeable data users and conduct data validation studies."
- 要点：数据库里的"乳腺癌"编码，可能是确诊时记的，也可能只是医生怀疑并开检查时记的；不熟悉数据的研究者要请教熟悉数据的人，并做数据验证研究。

### E5

- 位置：DEFINING TIME ZERO
- 原文："Eligibility criteria need to be met at that point but not later; study outcomes begin to be counted after that point but not earlier." / "Starting after randomization could result in selection bias because all outcome cases between randomization and time zero would be excluded from the analysis."
- 要点：纳入标准要在"零时刻"（随访起点）满足，结局从这一刻之后开始计；随访起点晚于分配时刻，会漏掉中间发生的结局，造成选择偏倚。

### E6

- 位置：DEFINING TIME ZERO
- 原文："With observational data, the best way to emulate time zero of the target trial is to define time zero to be the time when an eligible individual initiates a treatment strategy."
- 要点：用观察性数据时，模拟零时刻的最好办法，是把符合条件的人开始某种处理策略的时刻定为零时刻。

### E7

- 位置：Assignment procedures
- 原文："One such approach is emulating a target trial with “reversed” strategies" / "Incompatible or surprising effect estimates (e.g., a decreased risk both when initiating therapy in our original target trial and when discontinuing therapy in the reversed target trial) suggest that at least 1 of the 2 emulations failed to ensure a fair comparison."
- 要点：一种间接检查未测量混杂的办法：再模拟一个"策略反过来"的目标试验（如"继续用药"对"停药"）。如果"开始用药"和"停药"都显示风险降低，说明至少一个模拟没有做到公平比较。

### E8

- 位置：Outcome
- 原文："We often would prefer to emulate a target trial with systematic and blind ascertainment of the outcome to ensure that knowledge of treatment status does not influence a doctor's decision to look for the outcome." / "except when outcome ascertainment cannot be affected by treatment history (e.g., if the outcome is death and is independently ascertained from a death registry)"
- 要点：理想情况是系统地、在不知道处理情况下判定结局，免得医生因为知道病人用了药而更积极地找结局；观察性数据通常做不到，除非结局判定不受用药史影响（例如从死亡登记独立获取的死亡）。

### E9

- 位置：Assignment procedures
- 原文："Confounding bias may be especially serious when emulating target trials that, like ours, compare an active treatment with no treatment (or usual care) rather than with another active treatment"
- 要点：拿某种积极治疗和"不治疗"（或常规照护）比，混杂可能特别严重；和另一种积极治疗比，问题会小一些。

### E10

- 位置：DISCUSSION
- 原文："However, we will rarely be able to emulate the ideal trial in which we are most interested." / "We will then be able to outline a protocol, present a flow chart, summarize how the observational data set is used to emulate the target trial, and explain how the target trial differs from the ideal trial"
- 要点：很少能模拟出最理想的试验；应写出方案、给出流程图，说明怎样用数据模拟目标试验，以及目标试验和理想试验差在哪里。

### E11

- 位置：DISCUSSION
- 原文："the target trial approach can be extended to case-control sampling designs" / "Investigators will first need to define the follow-up study from which cases and controls were sampled and then the target trial that the follow-up study emulates."
- 要点：目标试验的思路也能用于病例对照设计：先定义病例和对照是从哪个随访研究（队列）中抽出来的，再定义这个随访研究模拟的目标试验。

### E12

- 位置：Outcome
- 原文："Independent outcome validation is often warranted, because several studies have shown that lack of outcome validation may result in misleading effect estimates"
- 要点：常常需要独立验证结局，因为已有研究表明，不验证结局可能得出误导性的效应估计。
