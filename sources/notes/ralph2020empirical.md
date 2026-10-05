# ACM SIGSOFT Empirical Standards：Systematic Reviews 与 General Standard

- 资料：`ralph2020empirical`。ACM SIGSOFT（美国计算机协会软件工程分会）制定的实证研究标准，CC0 许可。
- 版本：submodule `repos/acmsigsoft__EmpiricalStandards`，commit `554118c`（2026-09-17）。原文见 [`docs/standards/SystematicReviews.md`](../../repos/acmsigsoft__EmpiricalStandards/docs/standards/SystematicReviews.md) 和 [`docs/standards/GeneralStandard.md`](../../repos/acmsigsoft__EmpiricalStandards/docs/standards/GeneralStandard.md)。
- 标准把要求分为三档：Essential（必要）、Desirable（加分）、Extraordinary（优秀）。

## Systematic Reviews 标准

### E1

- 位置：标题下的定义
- 原文："A study that appraises, analyses, and synthesizes primary or secondary literature to provide a complete, exhaustive summary of current evidence regarding one or more specific topics or research questions"
- 要点：系统综述的定义：评估、分析和综合已有文献，对一个或几个具体问题，给出完整、详尽的现有证据总结。

### E2

- 位置：Application
- 原文："Does not apply to ad-hoc literature reviews, case surveys or advanced qualitative synthesis methods (e.g. meta-ethnography)"
- 要点：凭经验挑文献的非系统综述不适用这套标准。

### E3

- 位置：Essential Attributes
- 原文："identifies type of review (e.g. case survey, critical review, meta-analysis, meta-synthesis, scoping review)"
- 要点：必要：说明自己做的是哪一类综述。

### E4

- 位置：Essential Attributes
- 原文："presents step-by-step, systematic, replicable description of search process including search terms" / "defines clear selection criteria"
- 要点：必要：一步步、可复现地描述检索过程，包括检索词；给出明确的筛选标准。

### E5

- 位置：Essential Attributes
- 原文："specifies the data extracted from each primary study; explains relationships to research questions" / "describes in detail how data were extracted and synthesized (can be qualitative or quantitative)" / "describes coding scheme(s) and their use"
- 要点：必要：说明从每篇论文提取什么数据、和研究问题有什么关系；详细说明怎样提取、怎样综合；说明编码方案。

### E6

- 位置：Essential Attributes
- 原文："clear chain of evidence from the extracted data to the answers to the research question(s)" / "presents conclusions or recommendations for practitioners/non-specialists"
- 要点：必要：从提取的数据到研究问题的答案，要有清楚的证据链；给出面向实践者或非专业读者的结论或建议。

### E7

- 位置：Desirable Attributes
- 原文："provides supplementary materials such as protocol, search terms, search results, selection process results; complete dataset, analysis scripts; coding scheme, examples of coding, decision rules, descriptions of edge cases"
- 要点：加分：公开研究方案、检索词、检索和筛选结果、完整数据、分析脚本、编码方案和判定规则等补充材料。

### E8

- 位置：Desirable Attributes
- 原文："mitigates sampling bias and publication bias, using some (not all) of: (i) manual and keyword automated searches; (ii) backward and forward snowballing searches; (iii) checking profiles of prolific authors in the area; (iv) searching both formal databases (e.g. ACM Digital Library) and indexes (e.g. Google Scholar); (v) searching for relevant dissertations; (vi) searching pre-print servers (e.g. arXiv); [...] contacting known authors in the area."
- 要点：加分：组合几种检索方式来减少抽样偏差和发表偏差，例如手工检索加关键词检索、滚雪球、查高产作者的论文列表、正式数据库加 Google Scholar、学位论文、预印本、联系领域内作者。不要求全部用上。

### E9

- 位置：Desirable Attributes 及脚注 3
- 原文："demonstrates that the search process is sufficiently rigorous for the systematic review goals" / 脚注："e.g. formal meta-analysis of experiments has higher requirements for completeness than mapping studies of broad topic areas."
- 要点：加分：证明检索的严格程度与综述目标相称。元分析对"找全"的要求，远高于宽泛主题的映射研究。

### E10

- 位置：Desirable Attributes
- 原文："assesses quality of primary studies using an a priori coding scheme (e.g. relevant empirical standards); explains how quality was assessed; excludes low quality studies (ok) or models study quality as a moderating variable (better)"
- 要点：加分：用事先定好的标准评估每篇研究的质量。排除低质量研究可以，把质量作为调节变量纳入分析更好。

### E11

- 位置：Desirable Attributes
- 原文："(positivist reviews), uses 2+ independent analysts; analyzes inter-rater reliability [...]; explains how discrepancies among coders were resolved"
- 要点：加分：两人以上独立分析，计算评分一致性，说明分歧如何解决。

### E12

- 位置：Desirable Attributes
- 原文："includes a PRISMA flow diagram" / "uses meta-analysis methods appropriate for primary studies; does not use vote counting"
- 要点：加分：附 PRISMA 流程图；做元分析时用合适的统计方法，不用"计票法"（只数支持和反对的研究各有几篇）。

### E13

- 位置：Desirable Attributes 及脚注 5
- 原文："integrates results into prior theory or research; identifies gaps, biases, or future directions" / "clearly distinguishes evidence-based results from interpretations and speculation"
- 要点：加分：把结果放回已有研究中，指出空白、偏差和未来方向；清楚区分有证据的结果和自己的解读、推测。

### E14

- 位置：Extraordinary Attributes
- 原文："two or more researchers independently undertaking the preliminary search process before finalizing the search scope and search keywords" / "contacted primary study authors to ensure interpretations are correct, and elicit additional details not found in the papers such as access to raw data"
- 要点：优秀：确定检索范围和检索词之前，两人以上独立做预检索；联系原作者确认解读是否正确，或获取论文里没有的细节。

### E15

- 位置：Examples of Acceptable Deviations
- 原文："No attempts to mitigate publication bias in a study explicitly examining a specific venue's (e.g. CACM or ICSE) coverage of a given topic." / "Using probability sampling on primary studies when there are too many to analyze (i.e. thousands)."
- 要点：可以接受的偏离：专门研究某个会议或期刊时，可以不处理发表偏差；论文多到数千篇时，可以随机抽样。

### E16

- 位置：Antipatterns
- 原文："A laundry-list description of the studies (A found X, B found Y, ...), rather than a synthesis of the findings." / "Relying on characteristics of the publication venues as a proxy for the quality of the primary studies instead of assessing primary studies' quality explicitly." / "Reviewing an area in which there are too few high-quality primary studies to draw reliable conclusions."
- 要点：反面模式：逐篇罗列而不综合；用发表会议或期刊的档次代替对研究质量的评估；在高质量研究太少的领域做综述。

### E17

- 位置：Invalid Criticisms
- 原文："The search queries are not identical in all databases." / "The analysis strategy should be more qualitative/quantitative"
- 要点：不成立的批评：各数据库的检索式不完全相同；分析方法应该更定性或更定量。

## General Standard（所有研究类型共用）

### E18

- 位置：General Standard，Essential Attributes
- 原文："discloses all major limitations" / "states clear conclusions which are linked to research question (or purpose, etc.) and supported by explicit evidence (data/observations) or arguments"
- 要点：所有研究都必须披露主要局限；结论要对应研究问题，并有明确的证据或论证支撑。
