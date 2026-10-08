# ACL Rolling Review：Responsible NLP Research Checklist

- 资料：`arr2024responsible`，[原文](https://aclrollingreview.org/responsibleNLPresearch/)
- 版本：ACL 滚动评审（ACL Rolling Review，ARR，计算语言学学会 ACL 的统一审稿服务）的"负责任 NLP 研究检查清单"说明网页；页面注明按 ARR 2024 年 10 月一轮更新，2026-10-08 读取。位置写清单题号。只代表 ARR，其他会议的要求可能不同。

### E1

- 位置：Guidelines for Answering Checklist Questions
- 原文："Submissions that systematically fail to provide either specific relevant sections or justification to the questions relevant for their research will be desk-rejected."
- 要点：对相关问题既不指出论文对应章节、也不给理由的投稿，会被直接拒稿。

### E2

- 位置：Guidelines for Answering Checklist Questions
- 原文："Not answering positively to a question is not grounds for rejection."
- 要点：某题答"否"本身不是拒稿理由。

### E3

- 位置：开头
- 原文："The checklist is completed as part of the submission form."
- 要点：清单在投稿表单里填写。

### E4

- 位置：开头
- 原文："This allows the checklist to serve as a kind of FAQ for the reviewers, pre-empting questions that would otherwise be asked in the author response period."
- 要点：清单相当于给审稿人的常见问题解答，提前回答本来会在作者回复期被问到的问题。

### E5

- 位置：Guidelines for Answering Checklist Questions
- 原文："You are strongly encouraged to take a look at the checklist early on as it likely will positively influence the way you do your research and write the paper."
- 要点：建议早点看清单，它会影响你怎样做研究、怎样写论文。

### E6

- 位置：B5
- 原文："Be sure to report the language of any language data, even if it is commonly-used benchmarks."
- 要点：用到的语言数据要写明是什么语言，常用基准也一样。

### E7

- 位置：C1
- 原文："Note that this should include information about all experiments, not just the final runs that led to the results presented in the paper."
- 要点：报告的计算预算要包括所有实验，不只是产生论文结果的最后几次运行。

### E8

- 位置：C2
- 原文："Unless under special circumstances, hyperparameters should not be tuned on the evaluation (held-out) dataset."
- 要点：除特殊情况外，不要在评测用的留出数据上调超参数。

### E9

- 位置：C3
- 原文："In all cases, when a result is reported, it should be clear if it is from a single run, the max across N random seeds, the average, etc."
- 要点：报告每个结果时，都要写清它是单次运行、N 个随机种子里的最大值，还是平均值。

### E10

- 位置：C4
- 原文："The version number or reference to specific implementation is important because different implementations of the same metric can lead to slightly different results (e.g., ROUGE)."
- 要点：同一个指标的不同实现会给出略有不同的结果（如 ROUGE），所以要写明用的哪个实现和版本。

### E11

- 位置：D2
- 原文："In case of payment, provide the amount paid for each task (including any bonuses), and discuss how you determined the amount of time a task would take."
- 要点：给参与者或标注者付费的，要写明每项任务付多少钱（含奖励），以及怎样估计任务耗时。

### E12

- 位置：D4
- 原文："However, stating that you obtained approval from an ethics review board does not imply that the societal impact of the work does not need to be discussed."
- 要点：得到伦理审查委员会批准，不等于不用讨论工作的社会影响。

### E13

- 位置：开头
- 原文："It is largely based on the NeurIPS 2021 paper checklist"
- 要点：这份清单大体以 NeurIPS 2021 的论文检查清单为基础。

### E14

- 位置：B6
- 原文："For example, small differences in accuracy on large test sets may be significant, while on small test sets they may not be."
- 要点：同样小的准确率差异，在大测试集上可能显著，在小测试集上可能不显著，所以要报告各数据划分的样本数。

### E15

- 位置：E1
- 原文："If you used any AI assistants, did you include information about your use?"
- 要点：用了 AI 助手（如 ChatGPT、Copilot）做研究、编程或写作，要说明怎样用的。

### E16

- 位置：A2
- 原文："Examples of risks include potential malicious or unintended harmful effects and uses (e.g., disinformation, generating fake profiles, surveillance), environmental impact (e.g., training huge models)"
- 要点：要讨论的风险包括恶意或无意的有害用途（虚假信息、伪造账号、监控），以及训练超大模型的环境影响等。
