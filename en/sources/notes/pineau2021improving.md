# Pineau et al. 2021: Improving Reproducibility in Machine Learning Research

- Source: `pineau2021improving`, [original](https://jmlr.org/papers/v22/20-303.html)
- Version: Journal of Machine Learning Research 22(164):1-20, 2021, open access (CC-BY 4.0). Reports on the NeurIPS 2019 reproducibility program: the code submission policy, the community reproducibility challenge, and the Machine Learning Reproducibility Checklist.

### E1

- Location: §2.1 Defining Reproducibility
- Quote: "Reproducible work consists of re-doing an experiment using the same data and same analytical tools, whereas Replicable work considers different data (presumably sampled from similar distribution or method), Robust work assumes the same data but different analysis (such as reimplementation of the code, perhaps different computer architecture), and Generalisable work leads to the same conclusions despite considering different data and different analytical tools."
- Key point: The paper's usage: reproducible (same data, same analytical tools), replicable (different data), robust (same data, different analysis, e.g., reimplemented code), and generalizable (different data and different analysis, same conclusion).

### E2

- Location: §2 Background
- Quote: "This limitation has been highlighted in a few studies reporting that new proposed methods are often not better than previous implementations when a more thorough search of hyper-parameters is performed (Lucic et al., 2018; Melis et al., 2017), or even when using different random parameter initializations"
- Key point: In machine learning, studies have found that new methods are often no better than older ones once the hyperparameter search is done more thoroughly, or simply with different random seeds.

### E3

- Location: §2 Background
- Quote: "Strikingly, this study found that when the original authors provided assistance to the reproducers, 85% of results were successfully reproduced, compared to 4% when the authors didn't respond." / "Although a selection bias could be at play (authors who knew their results would reproduce might have been more likely to provide assistance for the reproduction)"
- Key point: Summarizing Raff 2019: 85% of results were reproduced when the original authors helped, versus 4% when the authors did not respond; but there may be selection bias (authors confident their work is reproducible are more willing to help).

### E4

- Location: §3, objections to the code submission policy: "Replication of mistakes"
- Quote: "Having a copy of the code used to produce the experimental results is not a guarantee that this code is correct, and there is significant value in reimplementing an algorithm directly from its description in a paper."
- Key point: Having the original code does not guarantee the code is correct; reimplementing an algorithm directly from the paper's description has significant value.

### E5

- Location: §3, objections to the code submission policy: "Computation infrastructure"
- Quote: "Even if data and code are provided, the experiments may require so much computation (time & number of machines) that it is impractical for any reviewer, or in fact most researchers, to attempt reproducing the work."
- Key point: Even with data and code available, some experiments need so much computation that most researchers cannot reproduce them.

### E6

- Location: §4 The NeurIPS 2019 Reproducibility Challenge
- Quote: "There is rarely such a concise outcome to a reproducibility study. Most reports produced during the challenge offer a much more detailed & nuanced account of their efforts, and the level of fidelity to which they could reproduce the methods, results & claims of each paper." / "we have not found that the findings of most reproducibility studies lend themselves to such a coarse summary."
- Key point: "Is this paper reproducible?" rarely has a simple answer; most reproducibility reports give a detailed, nuanced account of how far the methods, results, and claims were each reproduced. A single "reproducibility score" is not a good summary.

### E7

- Location: §1 Introduction
- Quote: "Indeed, the evidence threshold for publishing a new positive" [...] "finding is much lower than that for invalidating a previous finding. In the latter case, it may require several teams showing beyond the shadow of a doubt that a result is false for the research community to revise its opinion."
- Key point: The evidence threshold for publishing a new positive finding is much lower than for invalidating an existing one; the latter may take several teams showing beyond doubt that the result is wrong before the community changes its view.

### E8

- Location: §4 The NeurIPS 2019 Reproducibility Challenge
- Quote: "The main goal of this challenge is to provide independent verification of the empirical claims in accepted NeurIPS papers, and to leave a public trace of the findings from this secondary analysis."
- Key point: The goal of the reproducibility challenge is to independently verify the empirical claims in accepted papers and leave a public record of the findings.

### E9

- Location: §6 Discussion
- Quote: "Specific calls for reproducibility papers have been issued (ECIR, 2020). An open-access peer-reviewed journal is dedicated to such papers (ReScience C, 2021)"
- Key point: Conferences have issued specific calls for reproducibility papers (e.g., the European Conference on Information Retrieval, ECIR 2020), and ReScience C is an open-access peer-reviewed journal dedicated to them.

### E10

- Location: §1 Introduction
- Quote: "Misspecification or under-specification of the model or training procedure;" / "Lack of availability of the code necessary to run the experiments, or errors in the code;" / "Under-specification of the metrics used to report results;"
- Key point: Machine learning results are hard to reproduce partly because of misspecified or underspecified models or training procedures, unavailable or buggy code, and underspecified metrics.
