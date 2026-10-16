# Tennant et al. 2021: Use of directed acyclic graphs (DAGs) to identify confounders in applied health research: review and recommendations

- Source: `tennant2021dags`, [PubMed Central full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128477/)
- Version: International Journal of Epidemiology 50(2): 620-632, 2021 (published online December 2020).

### E1

- Location: Abstract (Methods, Results)
- Quote: "Original health research articles published during 1999–2017 mentioning ‘directed acyclic graphs’ (or similar) or citing DAGitty were identified from Scopus, Web of Science, Medline and Embase." / "A total of 234 articles were identified that reported using DAGs. A fifth ( n = 48, 21%) reported their target estimand(s) and half ( n = 115, 48%) reported the adjustment set(s) implied by their DAG(s). Two-thirds of the articles ( n = 144, 62%) made at least one DAG available."
- Key point: The authors searched for original health research published 1999-2017 that mentioned directed acyclic graphs and found 234 articles that used them; 21% stated the target estimand, 48% reported the adjustment set implied by the graph, and 62% made at least one graph available.

### E2

- Location: Recommendations: The DAG(s) for each focal relationship and estimand of interest should be available
- Quote: "DAGs explicitly depict the investigators’ assumptions about the data-generating process of their dataset." / "This may be achieved by reproducing the DAG in the manuscript directly, in supplementary material or by providing functional weblinks to a well-established open-source platform such as www.dagitty.net"
- Key point: A directed acyclic graph makes explicit the researcher's assumptions about how the data were generated; the graph should be visible to readers: in the main text, in supplementary material, or via a working link to an open-source platform such as dagitty.net.

### E3

- Location: Recommendations: DAGs should include all relevant variables
- Quote: "The DAG for a specific focal relationship should include all plausible confounding variables (i.e. that may plausibly cause both the exposure and the outcome), regardless of whether direct measurements are available or possible."
- Key point: The graph should include all plausible confounders (variables that may affect both exposure and outcome), whether or not they were measured.

### E4

- Location: Recommendations: Arcs should generally be assumed to exist between any two variables
- Quote: "Omitting an arc between two variables implies that there is precisely no causal effect of one on the other."
- Key point: Not drawing an arrow between two variables amounts to assuming there is no causal effect between them at all.

### E5

- Location: Recommendations: adjustment sets
- Quote: "The DAG-implied adjustment set(s) for every estimand of interest should be stated explicitly, including variables for which measurements are not available for conditioning." / "If alternative adjustment set(s) are used, they should be clearly described and justified, and the ensuing estimates should be reported separately to those reported using the DAG-implied adjustment set."
- Key point: State explicitly the adjustment set implied by the graph, including unmeasured variables; if you use a different adjustment set, justify it and report the results separately from those adjusted according to the graph.

### E6

- Location: Recommendations: The focal relationship(s) and estimand(s) of interest should be stated in the study aims
- Quote: "all estimands of interest should be clearly stated in the study aims or at the beginning of the article’s methods section before details on how estimation was attempted"
- Key point: State the quantity to be estimated (the estimand) at the start of the aims or methods section, then explain how it will be estimated.

### E7

- Location: Recommendations: Variables should be visually arranged so that all constituent arcs flow in the same direction
- Quote: "with arcs flowing in the same direction from left-to-right or top-to-bottom"
- Key point: Arrange variables in temporal order so that all arrows point in the same direction (left to right or top to bottom).
