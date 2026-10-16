# ACL Rolling Review: Responsible NLP Research Checklist

- Source: `arr2024responsible`, [original](https://aclrollingreview.org/responsibleNLPresearch/)
- Version: Web page explaining the Responsible NLP Research checklist of ACL Rolling Review (ARR, the shared reviewing service of the Association for Computational Linguistics, ACL); the page says it was updated for the October 2024 ARR cycle; read 2026-10-08. Locations give checklist item numbers. Applies to ARR only; other conferences may differ.

### E1

- Location: Guidelines for Answering Checklist Questions
- Quote: "Submissions that systematically fail to provide either specific relevant sections or justification to the questions relevant for their research will be desk-rejected."
- Key point: Submissions that systematically give neither the relevant sections nor a justification for the relevant questions will be desk-rejected.

### E2

- Location: Guidelines for Answering Checklist Questions
- Quote: "Not answering positively to a question is not grounds for rejection."
- Key point: Answering "no" to a question is not in itself grounds for rejection.

### E3

- Location: opening
- Quote: "The checklist is completed as part of the submission form."
- Key point: The checklist is completed as part of the submission form.

### E4

- Location: opening
- Quote: "This allows the checklist to serve as a kind of FAQ for the reviewers, pre-empting questions that would otherwise be asked in the author response period."
- Key point: The checklist works as an FAQ for reviewers, pre-empting questions that would otherwise come up in the author response period.

### E5

- Location: Guidelines for Answering Checklist Questions
- Quote: "You are strongly encouraged to take a look at the checklist early on as it likely will positively influence the way you do your research and write the paper."
- Key point: Look at the checklist early; it will likely shape how you do the research and write the paper.

### E6

- Location: B5
- Quote: "Be sure to report the language of any language data, even if it is commonly-used benchmarks."
- Key point: State the language of any language data you use, even for commonly used benchmarks.

### E7

- Location: C1
- Quote: "Note that this should include information about all experiments, not just the final runs that led to the results presented in the paper."
- Key point: The reported compute budget should cover all experiments, not just the final runs behind the paper's results.

### E8

- Location: C2
- Quote: "Unless under special circumstances, hyperparameters should not be tuned on the evaluation (held-out) dataset."
- Key point: Except in special circumstances, do not tune hyperparameters on the held-out evaluation data.

### E9

- Location: C3
- Quote: "In all cases, when a result is reported, it should be clear if it is from a single run, the max across N random seeds, the average, etc."
- Key point: For every reported result, make clear whether it is a single run, the max across N random seeds, the average, etc.

### E10

- Location: C4
- Quote: "The version number or reference to specific implementation is important because different implementations of the same metric can lead to slightly different results (e.g., ROUGE)."
- Key point: Different implementations of the same metric (e.g., ROUGE) give slightly different results, so state which implementation and version you used.

### E11

- Location: D2
- Quote: "In case of payment, provide the amount paid for each task (including any bonuses), and discuss how you determined the amount of time a task would take."
- Key point: If participants or annotators were paid, give the amount per task (including bonuses) and explain how you estimated task time.

### E12

- Location: D4
- Quote: "However, stating that you obtained approval from an ethics review board does not imply that the societal impact of the work does not need to be discussed."
- Key point: Approval from an ethics review board does not mean you can skip discussing the work's societal impact.

### E13

- Location: opening
- Quote: "It is largely based on the NeurIPS 2021 paper checklist"
- Key point: The checklist is largely based on the NeurIPS 2021 paper checklist.

### E14

- Location: B6
- Quote: "For example, small differences in accuracy on large test sets may be significant, while on small test sets they may not be."
- Key point: The same small accuracy difference may be significant on a large test set but not on a small one, so report the number of examples in each data split.

### E15

- Location: E1
- Quote: "If you used any AI assistants, did you include information about your use?"
- Key point: If you used AI assistants (e.g., ChatGPT, Copilot) for research, coding, or writing, describe how you used them.

### E16

- Location: A2
- Quote: "Examples of risks include potential malicious or unintended harmful effects and uses (e.g., disinformation, generating fake profiles, surveillance), environmental impact (e.g., training huge models)"
- Key point: Risks to discuss include malicious or unintended harmful uses (disinformation, fake profiles, surveillance) and environmental impact, such as training huge models.
