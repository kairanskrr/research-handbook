# Tennant et al. 2021：Use of directed acyclic graphs (DAGs) to identify confounders in applied health research: review and recommendations

- 资料：`tennant2021dags`，[PubMed Central 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128477/)
- 版本：International Journal of Epidemiology 50(2): 620–632，2021（2020 年 12 月在线发表）。

### E1

- 位置：Abstract（Methods, Results）
- 原文："Original health research articles published during 1999–2017 mentioning ‘directed acyclic graphs’ (or similar) or citing DAGitty were identified from Scopus, Web of Science, Medline and Embase." / "A total of 234 articles were identified that reported using DAGs. A fifth ( n = 48, 21%) reported their target estimand(s) and half ( n = 115, 48%) reported the adjustment set(s) implied by their DAG(s). Two-thirds of the articles ( n = 144, 62%) made at least one DAG available."
- 要点：作者检索了 1999—2017 年发表、提到有向无环图的原创健康研究，共 234 篇用了这种图；其中 21% 写明了目标估计量，48% 报告了图所推出的调整集，62% 公开了至少一张图。

### E2

- 位置：Recommendations：The DAG(s) for each focal relationship and estimand of interest should be available
- 原文："DAGs explicitly depict the investigators’ assumptions about the data-generating process of their dataset." / "This may be achieved by reproducing the DAG in the manuscript directly, in supplementary material or by providing functional weblinks to a well-established open-source platform such as www.dagitty.net"
- 要点：有向无环图明确画出研究者对数据如何产生的假设；图要让读者看得到：放在正文、补充材料，或给出 dagitty.net 等开源平台的可用链接。

### E3

- 位置：Recommendations：DAGs should include all relevant variables
- 原文："The DAG for a specific focal relationship should include all plausible confounding variables (i.e. that may plausibly cause both the exposure and the outcome), regardless of whether direct measurements are available or possible."
- 要点：图里要画出所有说得通的混杂因素（可能既影响暴露又影响结局的变量），不管有没有测量数据。

### E4

- 位置：Recommendations：Arcs should generally be assumed to exist between any two variables
- 原文："Omitting an arc between two variables implies that there is precisely no causal effect of one on the other."
- 要点：两个变量之间不画箭头，等于假设它们之间完全没有因果作用。

### E5

- 位置：Recommendations：adjustment sets
- 原文："The DAG-implied adjustment set(s) for every estimand of interest should be stated explicitly, including variables for which measurements are not available for conditioning." / "If alternative adjustment set(s) are used, they should be clearly described and justified, and the ensuing estimates should be reported separately to those reported using the DAG-implied adjustment set."
- 要点：明确写出图推出的调整集，包括没有测量数据的变量；如果用了别的调整集，要说明理由，并把结果和按图调整的结果分开报告。

### E6

- 位置：Recommendations：The focal relationship(s) and estimand(s) of interest should be stated in the study aims
- 原文："all estimands of interest should be clearly stated in the study aims or at the beginning of the article’s methods section before details on how estimation was attempted"
- 要点：在研究目的或方法部分开头写清要估计的量（估计量），再讲怎样估计。

### E7

- 位置：Recommendations：Variables should be visually arranged so that all constituent arcs flow in the same direction
- 原文："with arcs flowing in the same direction from left-to-right or top-to-bottom"
- 要点：按时间顺序排列变量，让箭头都朝同一个方向（从左到右或从上到下）。
