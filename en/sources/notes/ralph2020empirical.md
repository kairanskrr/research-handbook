# ACM SIGSOFT Empirical Standards: Systematic Reviews and General Standard

- Source: `ralph2020empirical`. The empirical standards for software engineering research developed by ACM SIGSOFT (the Association for Computing Machinery's Special Interest Group on Software Engineering), released under a CC0 license.
- Version: submodule `repos/acmsigsoft__EmpiricalStandards`, commit `554118c` (2026-09-17). Original text in [`docs/standards/SystematicReviews.md`](../../../repos/acmsigsoft__EmpiricalStandards/docs/standards/SystematicReviews.md) and [`docs/standards/GeneralStandard.md`](../../../repos/acmsigsoft__EmpiricalStandards/docs/standards/GeneralStandard.md).
- The standards sort requirements into three tiers: Essential, Desirable, and Extraordinary.

## Systematic Reviews standard

### E1

- Location: Definition under the title
- Quote: "A study that appraises, analyses, and synthesizes primary or secondary literature to provide a complete, exhaustive summary of current evidence regarding one or more specific topics or research questions"
- Key point: Definition of a systematic review: a study that appraises, analyzes, and synthesizes existing literature to give a complete, exhaustive summary of current evidence on one or more specific topics or research questions.

### E2

- Location: Application
- Quote: "Does not apply to ad-hoc literature reviews, case surveys or advanced qualitative synthesis methods (e.g. meta-ethnography)"
- Key point: The standard does not apply to ad hoc literature reviews that pick papers informally.

### E3

- Location: Essential Attributes
- Quote: "identifies type of review (e.g. case survey, critical review, meta-analysis, meta-synthesis, scoping review)"
- Key point: Essential: identify which type of review you are doing.

### E4

- Location: Essential Attributes
- Quote: "presents step-by-step, systematic, replicable description of search process including search terms" / "defines clear selection criteria"
- Key point: Essential: give a step-by-step, replicable description of the search process, including search terms, and define clear selection criteria.

### E5

- Location: Essential Attributes
- Quote: "specifies the data extracted from each primary study; explains relationships to research questions" / "describes in detail how data were extracted and synthesized (can be qualitative or quantitative)" / "describes coding scheme(s) and their use"
- Key point: Essential: specify what data were extracted from each primary study and how they relate to the research questions; describe in detail how data were extracted and synthesized; describe the coding scheme.

### E6

- Location: Essential Attributes
- Quote: "clear chain of evidence from the extracted data to the answers to the research question(s)" / "presents conclusions or recommendations for practitioners/non-specialists"
- Key point: Essential: show a clear chain of evidence from the extracted data to the answers to the research questions, and present conclusions or recommendations for practitioners or non-specialists.

### E7

- Location: Desirable Attributes
- Quote: "provides supplementary materials such as protocol, search terms, search results, selection process results; complete dataset, analysis scripts; coding scheme, examples of coding, decision rules, descriptions of edge cases"
- Key point: Desirable: provide supplementary materials such as the protocol, search terms, search and selection results, the complete dataset, analysis scripts, the coding scheme, and decision rules.

### E8

- Location: Desirable Attributes
- Quote: "mitigates sampling bias and publication bias, using some (not all) of: (i) manual and keyword automated searches; (ii) backward and forward snowballing searches; (iii) checking profiles of prolific authors in the area; (iv) searching both formal databases (e.g. ACM Digital Library) and indexes (e.g. Google Scholar); (v) searching for relevant dissertations; (vi) searching pre-print servers (e.g. arXiv); [...] contacting known authors in the area."
- Key point: Desirable: mitigate sampling bias and publication bias by combining search methods, e.g. manual plus keyword searches, snowballing, checking the profiles of prolific authors, formal databases plus Google Scholar, theses, preprints, and contacting authors in the field. Not all are required.

### E9

- Location: Desirable Attributes and footnote 3
- Quote: "demonstrates that the search process is sufficiently rigorous for the systematic review goals" / 脚注："e.g. formal meta-analysis of experiments has higher requirements for completeness than mapping studies of broad topic areas."
- Key point: Desirable: show that the search is rigorous enough for the review's goals. A meta-analysis has much higher requirements for completeness than a mapping study of a broad topic.

### E10

- Location: Desirable Attributes
- Quote: "assesses quality of primary studies using an a priori coding scheme (e.g. relevant empirical standards); explains how quality was assessed; excludes low quality studies (ok) or models study quality as a moderating variable (better)"
- Key point: Desirable: assess the quality of each primary study with an a priori coding scheme. Excluding low-quality studies is acceptable; modeling study quality as a moderating variable is better.

### E11

- Location: Desirable Attributes
- Quote: "(positivist reviews), uses 2+ independent analysts; analyzes inter-rater reliability [...]; explains how discrepancies among coders were resolved"
- Key point: Desirable: use two or more independent analysts, analyze inter-rater reliability, and explain how disagreements were resolved.

### E12

- Location: Desirable Attributes
- Quote: "includes a PRISMA flow diagram" / "uses meta-analysis methods appropriate for primary studies; does not use vote counting"
- Key point: Desirable: include a PRISMA flow diagram; for meta-analysis use appropriate statistical methods, not vote counting (just tallying how many studies support or oppose a finding).

### E13

- Location: Desirable Attributes and footnote 5
- Quote: "integrates results into prior theory or research; identifies gaps, biases, or future directions" / "clearly distinguishes evidence-based results from interpretations and speculation"
- Key point: Desirable: integrate the results into prior research, identify gaps, biases, and future directions, and clearly separate evidence-based results from your own interpretation and speculation.

### E14

- Location: Extraordinary Attributes
- Quote: "two or more researchers independently undertaking the preliminary search process before finalizing the search scope and search keywords" / "contacted primary study authors to ensure interpretations are correct, and elicit additional details not found in the papers such as access to raw data"
- Key point: Extraordinary: two or more researchers independently run the preliminary search before the search scope and keywords are finalized; contact primary study authors to check interpretations or obtain details missing from the papers.

### E15

- Location: Examples of Acceptable Deviations
- Quote: "No attempts to mitigate publication bias in a study explicitly examining a specific venue's (e.g. CACM or ICSE) coverage of a given topic." / "Using probability sampling on primary studies when there are too many to analyze (i.e. thousands)."
- Key point: Acceptable deviations: a study that examines a specific venue's coverage need not address publication bias; when there are thousands of primary studies, probability sampling is acceptable.

### E16

- Location: Antipatterns
- Quote: "A laundry-list description of the studies (A found X, B found Y, ...), rather than a synthesis of the findings." / "Relying on characteristics of the publication venues as a proxy for the quality of the primary studies instead of assessing primary studies' quality explicitly." / "Reviewing an area in which there are too few high-quality primary studies to draw reliable conclusions."
- Key point: Antipatterns: a laundry-list description of studies one by one instead of a synthesis; using the rank of the publication venue as a proxy for study quality; reviewing an area with too few high-quality studies.

### E17

- Location: Invalid Criticisms
- Quote: "The search queries are not identical in all databases." / "The analysis strategy should be more qualitative/quantitative"
- Key point: Invalid criticisms: the search queries are not identical across databases; the analysis should have been more qualitative or more quantitative.

## General Standard (shared by all study types)

### E18

- Location: General Standard, Essential Attributes
- Quote: "discloses all major limitations" / "states clear conclusions which are linked to research question (or purpose, etc.) and supported by explicit evidence (data/observations) or arguments"
- Key point: Every study must disclose its major limitations; conclusions must be linked to the research question and supported by explicit evidence or arguments.

### E19

- Location: General Standard, Desirable Attributes
- Quote: "summarizes and synthesizes a reasonable selection of related work (not every single relevant study)"
- Key point: A good paper summarizes and synthesizes a reasonable selection of related work, not every single relevant study.

### E20

- Location: General Standard, Desirable Attributes
- Quote: "clearly describes relationship between contribution(s) and related work"
- Key point: A good paper clearly describes how its contributions relate to related work.

### E21

- Location: General Standard, Research and Reporting Antipatterns
- Quote: "Mentioning related work only to dismiss it as irrelevant; listing rather than synthesizing related work."
- Key point: Antipatterns: mentioning related work only to dismiss it as irrelevant; listing related work instead of synthesizing it.

### E22

- Location: General Standard, Essential Attributes
- Quote: "states a purpose, problem, objective, or research question [...] explains why the purpose, problem, etc. is important (motivation)"
- Key point: Essential: state the purpose, problem, objective, or research question, and explain why it matters.

### E23

- Location: General Standard, Essential Attributes
- Quote: "methodology is appropriate (not necessarily optimal) for stated purpose, problem, etc."
- Key point: Essential: the methodology must be appropriate for the stated purpose or problem, not necessarily optimal.

### E24

- Location: General Standard, General Quality Criteria
- Quote: "There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology, as laid out in the specific **empirical standards**. Avoid applying inappropriate quality criteria (e.g. construct validity to a study with no constructs; internal validity to a study with no causal relationships)."
- Key point: There are no universal quality criteria. Each study should be assessed against criteria appropriate for its methodology; do not apply inappropriate criteria, such as demanding internal validity from a study that makes no causal claims.

### E25

- Location: General Standard, Invalid Criticisms
- Quote: "Cross-paradigmatic criticism (e.g. attacking an interpretivist study for not conforming to positivist norms). [...] Criticizing a study for limitations intrinsic to that kind of study or the methodology used (e.g. attacking a case study for low generalizability). [...] Rejecting a study because the reviewer would have used a different methodology or design."
- Key point: Invalid criticisms: cross-paradigmatic criticism (e.g. judging an interpretivist study by positivist norms); criticizing limitations intrinsic to that kind of study (e.g. attacking a case study for low generalizability); rejecting a study just because the reviewer would have used a different method.

### E26

- Location: General Standard, Research and Reporting Antipatterns
- Quote: "Attempting a study without reading, understanding and applying published guidelines for that kind of study."
- Key point: Antipattern: attempting a study without reading, understanding, and applying the published guidelines for that kind of study.

### E27

- Location: General Standard, Research and Reporting Antipatterns
- Quote: "Hypothesizing After Results are Known (HARKing) in ostensibly confirmatory, (post-)positivist research. [...] Reporting only the subset of statistical tests that produce significant results (p-hacking)."
- Key point: Antipatterns: HARKing (hypothesizing after results are known) in ostensibly confirmatory research; reporting only the subset of statistical tests that came out significant.

### E28

- Location: General Standard, Desirable Attributes
- Quote: "publishes the study in two phases: a plan and the results of executing the plan"
- Key point: Desirable: publish the study in two phases, first the plan, then the results of executing the plan.

### E29

- Location: Registered Reports Supplement, Definition
- Quote: "_Pre-registration_ refers to depositing the RR1 somewhere publicly visible. Pre-registration aims to prevent hypothesising after results are known, to mitigate unconscious researcher bias in data analysis, and combat publication bias."
- Key point: Preregistration means depositing the study plan somewhere publicly visible; it aims to prevent HARKing, mitigate unconscious researcher bias in data analysis, and combat publication bias.

### E30

- Location: Registered Reports Supplement, Application
- Quote: "This standard applies to positivist, confirmatory (i.e. hypothesis-testing) studies with tightly-scoped analysis approaches. Pre-registering interpretivist, qualitative or exploratory research remains controversial."
- Key point: The Registered Reports standard applies to confirmatory, hypothesis-testing studies; preregistering interpretivist, qualitative, or exploratory research remains controversial.

### E31

- Location: Registered Reports Supplement, Invalid Criticisms
- Quote: "RR1: Rejecting exploratory or qualitative research: all kinds of research can be pre-registered"
- Key point: The same standard also lists rejecting preregistration on the grounds that research is "exploratory or qualitative" as an invalid criticism: all kinds of research can be preregistered.

### E32

- Location: Registered Reports Supplement, Specific Attributes (RR1)
- Quote: "describes the research method in detail sufficient for an independent researcher to exactly replicate the proposed data collection and analysis procedures [...] the stated hypotheses can be tested with the data the researchers propose to collect"
- Key point: The plan must describe the method in enough detail for an independent researcher to exactly replicate the data collection and analysis, and the stated hypotheses must be testable with the data the researchers plan to collect.

### E33

- Location: Registered Reports Supplement, Specific Attributes (RR2)
- Quote: "deviations, if any, are _not_ justified based on the data [...] clearly designates as exploratory any unregistered post hoc analyses"
- Key point: Deviations from the plan must not be justified by the data; any unregistered post hoc analyses must be clearly labeled exploratory.

### E34

- Location: Registered Reports Supplement, Justifying Deviations
- Quote: "Reviewers should not expect research to go exactly according to plan or authors to foresee every possible problem. Changes are acceptable as long as they are justified and not _postdictive_ (i.e. changes made knowing how they will affect results)."
- Key point: Research never goes exactly to plan; changes are acceptable as long as they are justified and not postdictive (made knowing how they would affect the results).

### E35

- Location: Registered Reports Supplement, Desirable Attributes (RR1)
- Quote: "presents preliminary data (e.g. from a pilot study) to justify the chosen approach (e.g. probability distributions)."
- Key point: Desirable: present preliminary data, e.g. from a pilot study, to justify the chosen approach.

### E36

- Location: Sampling Supplement, Essential Attributes
- Quote: "explains the goal of sampling (e.g. aiming for representativeness, identifying exceptional cases) [...] explains why the sampling strategy is reasonable (not necessarily optimal) for the sampling goal"
- Key point: Essential: explain the goal of sampling (e.g. representativeness, or identifying exceptional cases) and why the sampling strategy is reasonable, though not necessarily optimal, for that goal.

### E37

- Location: Sampling Supplement, Antipatterns
- Quote: "claiming that a sample is representative of a population because it was randomly selected from a sampling frame, without considering bias in the sampling frame"
- Key point: Antipattern: claiming a sample represents a population just because it was randomly drawn from a sampling frame, without considering bias in the sampling frame itself.

### E38

- Location: Sampling Supplement, Antipatterns
- Quote: "quantitative research with a sample size insufficient to detect effects of the expected size [...] qualitative research with too little data for plausible saturation"
- Key point: Antipatterns: quantitative research with a sample too small to detect effects of the expected size; qualitative research with too little data for plausible saturation.

### E39

- Location: Sampling Supplement, Invalid Criticisms
- Quote: "complaining about lack of representativeness or low external validity in studies where representativeness is not a goal"
- Key point: Invalid criticism: complaining about lack of representativeness or low external validity in a study that never aimed at representativeness.

### E40

- Location: General Standard, Invalid Criticisms
- Quote: "Setting arbitrary minimum sample sizes or other data requirements, based on neither power analysis nor theoretical saturation."
- Key point: Invalid criticism: setting arbitrary minimum sample sizes based on neither power analysis nor theoretical saturation.

### E41

- Location: General Standard, Invalid Criticisms
- Quote: "Rejecting a study because it reports negative results."
- Key point: Invalid criticism: rejecting a study because it reports negative results.

### E42

- Location: Sampling Supplement, Application
- Quote: "This standard applies to empirical research in which the researcher selects smaller groups of items to study (a _sample_) from a larger group of items of interest (the _population_) using a usually imperfect population list (the _sampling frame_)."
- Key point: The sample is the smaller group of items the researcher actually studies; the population is the larger group of interest; the sampling frame is a list of the population, usually imperfect.

### E43

> Withdrawn: duplicates [E18](#e18) (its quote is fully contained in E18).

- Location: Essential Attributes › discussion
- Quote: "states clear conclusions which are linked to research question (or purpose, etc.) and supported by explicit evidence (data/observations) or arguments"
- Key point: Essential: state clear conclusions, linked to the research question and supported by explicit evidence (data, observations) or arguments.

### E44

> Withdrawn: duplicates [E18](#e18) (its quote is fully contained in E18).

- Location: Essential Attributes › discussion
- Quote: "discloses all major limitations"
- Key point: Essential: disclose all major limitations.

### E45

> Withdrawn: duplicates [E66](#e66) (its quote is fully contained in E66).

- Location: Research and Reporting Antipatterns
- Quote: "Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- Key point: Antipattern: acknowledging limitations but then writing implications and conclusions as though they do not exist.

### E46

> Withdrawn: duplicates [E66](#e66) (its quote is fully contained in E66).

- Location: Research and Reporting Antipatterns
- Quote: "Overreaching conclusions or generalizations; obfuscating, downplaying or dismissing a study's limitations."
- Key point: Antipatterns: overreaching conclusions or generalizations; obfuscating, downplaying, or dismissing limitations.

### E47

> Withdrawn: duplicates [E27](#e27) (its quote is fully contained in E27).

- Location: Research and Reporting Antipatterns
- Quote: "Hypothesizing After Results are Known (HARKing) in ostensibly confirmatory, (post-)positivist research."
- Key point: Antipattern: HARKing (hypothesizing after results are known) in ostensibly confirmatory, hypothesis-testing research.

### E48

> Withdrawn: duplicates [E27](#e27) (its quote is fully contained in E27).

- Location: Research and Reporting Antipatterns
- Quote: "Reporting only the subset of statistical tests that produce significant results (p-hacking)."
- Key point: Antipattern: reporting only the subset of statistical tests that produce significant results (p-hacking).

### E49

> Withdrawn: duplicates [E24](#e24) (its quote is fully contained in E24).

- Location: General Quality Criteria
- Quote: "There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology"
- Key point: There are no universal quality criteria; each study should be assessed against criteria appropriate for its methodology. For example, internal validity does not apply to a study with no causal claims.

### E50

> Withdrawn: duplicates [E25](#e25) (its quote is fully contained in E25).

- Location: Invalid Criticisms
- Quote: "Criticizing a study for limitations intrinsic to that kind of study or the methodology used (e.g. attacking a case study for low generalizability)."
- Key point: Criticizing a study for limitations intrinsic to its kind of study or methodology (e.g. attacking a case study for low generalizability) is an invalid criticism.

### E51

- Location: Desirable Attributes
- Quote: "describes reasonable attempts to investigate or mitigate limitations"
- Key point: Desirable: describe reasonable attempts to investigate or mitigate limitations.

## Experiments standard

### E52

- Location: Experiments › Antipatterns
- Quote: "validity threats are simply listed without linking them to results"
- Key point: Antipattern: validity threats are simply listed without linking them to the results.

### E53

- Location: Good Review Practices
- Quote: "The results must be, primarily, true (trustworthy) and, secondarily, important. A paper that is trustworthy can be accepted even if it is not important. A paper that is not trustworthy cannot be accepted, even if it seems important."
- Key point: Reviewers judge first whether the results are true (trustworthy), then whether they are important: a trustworthy paper can be accepted even if not important; an untrustworthy paper cannot be accepted however important it seems.

### E54

- Location: Good Review Practices
- Quote: "Clarify which are necessary and which are suggested changes. Ideally, separate them."
- Key point: Make clear which changes are necessary and which are suggested; ideally list them separately.

### E55

- Location: Good Review Practices
- Quote: "Reflect on and clearly state their own limitations and biases."
- Key point: Reviewers should state their own limitations and biases and point out parts they could not assess or did not review.

### E56

- Location: Reviewing Antipatterns
- Quote: "Providing vague, non-actionable criticism."
- Key point: Reviewing antipattern: giving vague, non-actionable criticism.

### E57

- Location: Reviewing Antipatterns
- Quote: "Using the review to promote the reviewer's own views, theories, methods, or publications."
- Key point: Reviewing antipattern: using the review to promote the reviewer's own views, methods, or publications.

### E58

- Location: Reviewing Antipatterns
- Quote: "Skimming a manuscript instead of carefully reading each word and inspecting each figure and table."
- Key point: Reviewing antipattern: skimming the manuscript instead of carefully reading every word and inspecting every figure and table.

### E59

- Location: Reviewing Antipatterns
- Quote: "Allowing the authors' identities or affiliations to affect the review."
- Key point: Reviewing antipattern: allowing the authors' identities or affiliations to affect the review.

### E60

- Location: Invalid Criticisms
- Quote: "is not new without providing citations to published studies that make **practically identical** contributions."
- Key point: Invalid criticism: saying the work "is not new" without citing published studies that make practically identical contributions.

### E61

- Location: Invalid Criticisms
- Quote: "lacks detail without enumerating missing details;"
- Key point: Invalid criticism: saying the paper "lacks detail," "misses references," or "is low quality" without specifying which.

### E62

- Location: Invalid Criticisms
- Quote: "Rejecting a study because it replicates or reproduces existing work."
- Key point: Invalid criticism: rejecting a study because it is a replication.

### E63

> Withdrawn: duplicates [E25](#e25) (its quote is fully contained in E25).

- Location: Invalid Criticisms
- Quote: "Rejecting a study because the reviewer would have used a different methodology or design."
- Key point: Invalid criticism: rejecting a study because the reviewer would have used a different methodology.

### E64

- Location: Reviewing Antipatterns
- Quote: "Requesting additional analysis not directly related to a study's purpose or research question"
- Key point: Reviewing antipattern: requesting additional analysis not directly related to the study's purpose.

### E65

- Location: General Standard, Essential Attributes
- Quote: "acknowledges and mitigates potential risks, harms, burdens or unintended consequences of the research"
- Key point: Essential: acknowledge and mitigate potential risks, harms, burdens, or unintended consequences of the research.

### E66

- Location: General Standard, Research and Reporting Antipatterns
- Quote: "Overreaching conclusions or generalizations; obfuscating, downplaying or dismissing a study's limitations." / "Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- Key point: Antipatterns: overreaching conclusions; downplaying limitations; or acknowledging limitations but writing conclusions as though they do not exist.

### E67

- Location: General Standard, Research and Reporting Antipatterns
- Quote: "Unnecessarily dividing the presentation of a single study into many papers (salami-slicing)."
- Key point: Antipattern: unnecessarily splitting one study across many papers (salami-slicing).

## Ethics (Studies with Human Participants)

### E68

- Location: Essential Attributes
- Quote: "describes all plausible, non-trivial potential risks or harms to participants (if any)" / "describes any steps taken to mitigate risks or harms" / "explains how benefits of the research justify any non-trivial risks or harms"
- Key point: Essential: describe the plausible risks or harms to participants, the steps taken to mitigate them, and why the benefits of the research justify those risks.

### E69

- Location: Essential Attributes
- Quote: "explains how participants were recruited" / "explains the compensation (if any) offered for participation and how coercion was mitigated" / "free, individual, informed consent to participate was obtained"
- Key point: Essential: explain how participants were recruited, what compensation was offered, how coercion was mitigated, and how free, individual, informed consent was obtained.

### E70

- Location: Essential Attributes, footnote 2
- Quote: "careful consideration of the reidentification potential through others combining multiple data sources"
- Key point: When protecting privacy, consider the potential for reidentification by others combining multiple data sources.

### E71

- Location: Antipatterns
- Quote: "Willful blindness to risks and harms to participants; justifying risks and harms on the basis that research is generally beneficial rather than in respect of benefits of the particular study; downplaying risks and harms during recruitment, consent or reporting."
- Key point: Antipatterns: willful blindness to risks; justifying risks by the general benefits of research rather than the benefits of this particular study; downplaying risks in recruitment, consent, or reporting.

### E72

- Location: Examples of Acceptable Deviations
- Quote: "The requirement to explain informed consent procedures may be modified where deception is a necessary part of the research protocol (although this itself must be explained in full"
- Key point: When deception is a necessary part of the research, informed consent requirements may be modified, but this must be explained in full.

### E73

- Location: Desirable Attributes
- Quote: "cites (with application number) approval of a national, institutional, or other appropriate scholarly ethical review board"
- Key point: Desirable: cite approval from an ethics review board, with the application number.

### E74

- Location: Invalid Criticisms
- Quote: "is not itself grounds for rejection unless there is a substantive ethical concern that such a board should have prevented"
- Key point: Lack of ethics review is not itself grounds for rejection, unless there is a substantive ethical concern that such a board should have prevented.

### E75

- Location: Note
- Quote: "Rarely, ethical research may require unlawful action. Ethical frameworks like Menlo include legal compliance so that the ethicality and legality of research can be weighed together."
- Key point: Rarely, ethical research may require unlawful action; frameworks like Menlo include legal compliance so that the ethics and legality of research can be weighed together.

## Open Science

### E76

- Location: Principle
- Quote: "provided that there are no ethical, legal, technical, economical, or practical barriers preventing their disclosure."
- Key point: Research materials should in principle be released, provided there are no ethical, legal, technical, economic, or practical barriers.

### E77

- Location: Desirable Attributes
- Quote: "OR explains why materials cannot be released (reasons for limited disclosure of data should be trusted)"
- Key point: When materials cannot be released, explaining why is enough; such reasons should be trusted.

### E78

- Location: Notes
- Quote: "personal or institutional websites, version control systems (e.g. GitHub), consumer cloud storage (e.g. Dropbox), and commercial paper repositories (e.g. ResearchGate; Academia.edu) do not offer properly archived and preserved data."
- Key point: Personal websites, GitHub, consumer cloud storage, ResearchGate, and the like are not proper long-term archives; use Zenodo, OSF, or an institutional repository instead.

### E79

- Location: Engineering Research standard, definition under the title
- Quote: "Research that invents and evaluates technological artifacts"
- Key point: Engineering research is research that invents and evaluates technological artifacts.

### E80

- Location: Engineering Research standard, Application
- Quote: "This standard applies to manuscripts that propose and evaluate technological artifacts, including algorithms, models, languages, methods, systems, tools, and other computer-based technologies." / "evaluations of pre-existing engineering research approaches (consider the **Experiments** Standard)" / "experience reports of applying pre-existing engineering research approaches"
- Key point: It applies to papers that propose and evaluate algorithms, models, languages, methods, systems, tools, and similar artifacts; studies that only evaluate existing approaches fall under the experiments standard, and experience reports applying existing approaches are not engineering research either.

### E81

- Location: Engineering Research standard, Essential Attributes
- Quote: "describes the proposed artifact in adequate detail" / "justifies the need for, usefulness of, or relevance of the proposed artifact" / "conceptually evaluates the proposed artifact; discusses its strengths, weaknesses and limitations"
- Key point: You must describe the proposed artifact in adequate detail, justify why it is needed, and conceptually evaluate it, discussing its strengths, weaknesses, and limitations.

### E82

- Location: Engineering Research standard, footnote 2
- Quote: "Why are state-of-the-art approaches not good enough to deal with the problem? How can the technical contribution be beneficial?"
- Key point: Justifying the need means answering: why are state-of-the-art approaches not good enough, and how can the new contribution help?

### E83

- Location: Engineering Research standard, footnote 1
- Quote: "does the paper describe the overall workflow of the solution, showing how different techniques work together?" / "Are the novel components of the solution clearly singled out?"
- Key point: When describing the artifact, explain the overall workflow and how the parts work together, and clearly single out the novel components.

### E84

- Location: Engineering Research standard, Essential Attributes (method)
- Quote: "empirically evaluates the proposed artifact using:" / "in which the researchers intervene in a real organization using the artifact" / "in which the artifact is assessed using one or more benchmarks, or" / "another method for which a clear and convincing rationale is provided" / "clearly indicates which of the above empirical methodology is used"
- Key point: You must empirically evaluate the artifact with some method (action research, case study, controlled experiment with human participants, quantitative simulation, benchmarking, or another well-justified method) and say which one.

### E85

- Location: Engineering Research standard, Essential Attributes (method)
- Quote: "EITHER: empirically compares the artifact to one or more state-of-the-art alternatives" / "OR: provides a clear and convincing rationale for why comparative evaluation is impractical"
- Key point: You must empirically compare the artifact with state-of-the-art alternatives or benchmarks; if that is impractical, give a clear and convincing rationale.

### E86

- Location: Engineering Research standard, Essential Attributes (other)
- Quote: "assumptions (if any) are explicit, plausible and do not contradict each other or the contribution's goals"
- Key point: Assumptions must be explicit and plausible, and must not contradict each other or the contribution's goals.

### E87

- Location: Engineering Research standard, Desirable Attributes
- Quote: "provides supplementary materials including source code (if the artifact is software) or a comprehensive description of the artifact (if not software), and any input datasets (if applicable)" / "justifies any items missing from replication package based on practical or ethical grounds"
- Key point: Ideally provide source code and input datasets; justify on practical or ethical grounds anything missing from the replication package.

### E88

- Location: Engineering Research standard, Desirable Attributes
- Quote: "provides correctness arguments for the key analytical and theoretical contributions (e.g. theorems, complexity analyses, mathematical proofs)" / "includes one or more running examples to elucidate the artifact" / "evaluates the artifact in an industry-relevant context (e.g. widely used open-source projects, professional programmers)"
- Key point: Desirable: provide correctness arguments for key theoretical contributions, use running examples to explain the artifact, and evaluate it in a realistic setting.

### E89

- Location: Engineering Research standard, Extraordinary Attributes
- Quote: "contributes to our collective understanding of design practices or principles" / "presents ground-breaking innovations with obvious real-world benefits"
- Key point: Outstanding engineering research deepens our understanding of design principles or brings ground-breaking innovations with obvious real-world benefits.

### E90

- Location: Engineering Research standard, General Quality Criteria
- Quote: "Appropriateness of evaluation methods to the nature, goals, and assumptions of the contribution" / "Relationship of innovativeness to rigorousness: less innovative artifacts require more rigorous evaluations"
- Key point: Evaluation methods must suit the nature, goals, and assumptions of the contribution; the less innovative the artifact, the more rigorous the evaluation must be.

### E91

- Location: Engineering Research standard, Antipatterns
- Quote: "overstates the novelty of the contribution" / "omits details of key conceptual aspects while focusing exclusively on incidental implementation aspects"
- Key point: Antipatterns: overstating novelty; focusing only on incidental implementation details while omitting key conceptual aspects.

### E92

- Location: Engineering Research standard, Antipatterns
- Quote: "evaluation consists *only* of eliciting users' opinions of the artifact" / "evaluation consists *only* of quantitative performance data that is not compared to established benchmarks or alternative solutions"
- Key point: Antipatterns: an evaluation that consists only of users' opinions of the artifact, or only of performance numbers not compared with established benchmarks or alternative solutions.

### E93

- Location: Engineering Research standard, Antipatterns
- Quote: "evaluation using a non-experimental (single group, non-repeated) design" / "evaluation using toy examples (sometimes misrepresented as "case studies")"
- Key point: Antipatterns: a non-experimental evaluation (single group, not repeated); evaluating with toy examples and calling them "case studies."

### E94

- Location: Engineering Research standard, Invalid Criticisms
- Quote: "The paper does not report as ambitious an empirical study as other predominately empirical papers. The more innovative the artifact and more comprehensive the conceptual evaluation, the less we should expect from the empirical study." / "if few subjects are available in the contribution's domain or the experimental evaluation is part of a more comprehensive validation strategy (e.g. formal arguments)"
- Key point: Invalid criticisms: the empirical study is less ambitious than in predominantly empirical papers; few evaluation subjects (when the field has few, or the experiment is only part of the overall validation). The more innovative the artifact and the more comprehensive the conceptual evaluation, the less we should expect from the empirical part.

### E95

- Location: Engineering Research standard, Invalid Criticisms
- Quote: "The artifact is not experimentally compared with related approaches *that are not publicly available*." / "before saying "you should have compared this against X," make sure X is actually available and functional." / "Proposed artifacts should outperform existing artifacts on *some* dimension(s); e.g. scalability, performance on specific classes of problems, applicability to realistic systems, theoretical guarantees."
- Key point: Not comparing with approaches that are not publicly available is not a flaw; a new artifact need not be the first solution, but it must beat existing ones on some dimension, such as scalability, performance on some class of problems, applicability to real systems, or theoretical guarantees.

### E96

- Location: Engineering Research standard, Invalid Criticisms
- Quote: "Engineering papers often define a motivating "problem" or "objective" rather than a research questiion." / "The contribution is not technically complicated. What matters is that it works. Unnecessary complexity is undesirable."
- Key point: Invalid criticisms: no explicit research question (engineering papers often state a motivating "problem" or "objective" instead); the contribution is not technically complicated (what matters is that it works; unnecessary complexity is undesirable).

### E97

- Location: Engineering Research standard, Invalid Criticisms
- Quote: "No replication package, if there are clear, convincing practical or ethical reasons preventing artifact disclosure."
- Key point: Not providing a replication package is not a flaw when there are clear, convincing practical or ethical reasons.

### E98

- Location: Engineering Research standard, footnote 4
- Quote: "Learning by building innovative artifacts is called engineering research. Some of the following readings incorrectly refer to engineering research as “design science” because the information systems community misappropriated that term circa 2004."
- Key point: The standard's authors argue the right name is "engineering research"; the term "design science" was borrowed by the information systems community around 2004 and originally meant the study of designers and their design processes.

### E99

- Location: Benchmarking standard, Essential Attributes
- Quote: "EITHER: justifies the selection of an existing, publicly available or standard benchmark (in terms of relevance, timeliness, etc.)" / "allows different configurations of a system under test to compete on their merits without artificial limitations" / "assesses stability or reliability using sufficient experiment repetitions and execution duration"
- Key point: When using an existing benchmark, justify why you chose it; let different configurations compete fairly on their merits without artificial limitations; use enough repetitions and execution time to check that results are stable.

### E100

- Location: Benchmarking standard, Essential Attributes (discussion)
- Quote: "discusses the construct validity of the benchmark; that is, does the benchmark measure what it is supposed to measure?"
- Key point: You must discuss the construct validity of the benchmark: does it measure what it is supposed to measure?

### E101

- Location: Benchmarking standard, Antipatterns
- Quote: "Tailoring the benchmark for a specific method, technique or tool, which is evaluated with the benchmark." / "Using benchmarking experiments that are irrelevant for the problem studied to obfuscate weaknesses in the proposed approach" / "Collecting aggregated measurements instead of persisting all raw results and running an offline analysis"
- Key point: Antipatterns: tailoring the benchmark to the method being evaluated; using tests irrelevant to the problem to obfuscate weaknesses; keeping only aggregated results instead of all raw results.

### E102

- Location: Benchmarking standard, Invalid Criticisms
- Quote: "The benchmark is not widely used. It is sufficient to start developing a new benchmark with a small group of researchers as an offer to a larger scientific community."
- Key point: Invalid criticism: "the benchmark is not widely used." A new benchmark can start with a small group of researchers as an offer to the larger community.

### E103

- Location: General Standard, Essential Attributes
- Quote: "discloses all major limitations"
- Key point: You must disclose all major limitations.

### E104

- Location: Benchmarking standard, Essential Attributes
- Quote: "defines a new benchmark, including:" / "the quality to be benchmarked (e.g., performance, availability, scalability, security)" / "the metric(s) to quantify the quality" / "the workload, usage profile and/or task sample the system under test is subject to"
- Key point: A new benchmark must define the quality being benchmarked, the metrics that quantify it, and the workload or task sample under which it is measured.

### E105

- Location: Repository Mining standard, definition
- Quote: "A study that quantitatively analyzes a dataset extracted from a platform hosting of structured or semi-structured text (e.g a source code repository)"
- Key point: A repository mining study quantitatively analyzes a dataset extracted from a platform hosting structured or semi-structured text, such as a source code repository.

### E106

- Location: Repository Mining standard, Application
- Quote: "use automated techniques to extract data from large-scale data repositories such as source code repositories, mailing list archives, bug tracking systems, Q&A forums and chat communication platforms"
- Key point: It applies to studies that use automated techniques to extract data from large-scale repositories (source code repositories, mailing list archives, bug trackers, Q&A forums, chat platforms).

### E107

- Location: Repository Mining standard, Application
- Quote: "If the study focuses on predictive modeling (e.g. machine learning) consider the **Data Science Standard**. If the subject systems are a few context-rich repositories, consider the **Case Study Standard**."
- Key point: Studies focused on predictive modeling should consult the Data Science standard; studies of a few context-rich repositories should consult the Case Study standard.

### E108

- Location: Repository Mining standard, Essential
- Quote: "explains why repository mining is appropriate for the proposed research problem" / "defines unit(s) of analysis or observation"
- Key point: Explain why repository mining suits the research problem, and define the units of analysis or observation.

### E109

- Location: Repository Mining standard, Essential
- Quote: "describes and justifies the data sources (e.g. GitHub, StackOverflow)" / "describes and justifies how the repositories are selected from the data sources" / "describes how the inclusion and exclusion criteria were validated (e.g., by manually inspecting the results of the automated search)"
- Key point: Describe and justify the data sources and how repositories were selected, and explain how the inclusion and exclusion criteria were validated, e.g. by manually checking the results of automated filtering.

### E110

- Location: Repository Mining standard, Essential
- Quote: "describes the procedure for the acquisition" / "describes dataset characteristics including size of the selected repositories" / "describes data preprocessing steps"
- Key point: Describe the data acquisition procedure, dataset characteristics (including repository size), and preprocessing steps.

### E111

- Location: Repository Mining standard, Essential
- Quote: "uses multiple annotators; reports the number of annotators" / "describes in detail the annotation procedure" / "assesses inter-rater reliability"
- Key point: For manual annotation, use multiple annotators and report how many, describe the annotation procedure in detail, and assess inter-rater reliability.

### E112

- Location: Repository Mining standard, Essential
- Quote: "describes and justifies measures or metrics used" / "uses previously validated measures, quantitatively assesses construct validity, or both"
- Key point: Describe and justify the measures used; use previously validated measures or quantitatively assess construct validity.

### E113

- Location: Repository Mining standard, Essential
- Quote: "discusses threats to external validity (e.g. caused by selection of data source(s) and repositories, selection criteria, search strings)"
- Key point: Discuss threats to external validity, e.g. from the choice of data sources, repositories, selection criteria, and search strings.

### E114

- Location: Repository Mining standard, Desirable
- Quote: "provides supplemental materials (e.g. complete dataset, tool(s) used to download, select, pre-process, and post-process the selected repositories)" / "uses probability sampling"
- Key point: Desirable attributes include releasing the complete dataset and the tools used to download, select, preprocess, and postprocess repositories, and using probability sampling.

### E115

- Location: Repository Mining standard, Desirable
- Quote: "triangulates across data sources, informants or researchers" / "qualitative analysis of scenarios where the data collection or analysis tools were ineffective" / "performs testing (e.g., unit testing) to avoid bugs in the proposed tool"
- Key point: Desirable attributes include triangulating across data sources, informants, or researchers; qualitatively analyzing cases where data collection or analysis tools failed; and testing your own tools to avoid bugs.

### E116

- Location: Repository Mining standard, Desirable
- Quote: "annotators reflect on their own possible biases" / "builds, tests or extends theory" / "tests formal hypotheses" / "discusses ethical issues in mining of software repositories"
- Key point: Desirable attributes also include annotators reflecting on their own biases, building or testing theory, testing formal hypotheses, and discussing the ethics of mining.

### E117

- Location: Repository Mining standard, Extraordinary
- Quote: "establishes causality, e.g. using longitidunal analyses"
- Key point: Establishing causality (e.g. with longitudinal analysis) is an extraordinary attribute, which implies that an ordinary mining study by default yields only correlations.

### E118

- Location: Repository Mining standard, Acceptable deviations
- Quote: "studies that focus on specific ecosystems (such as Apache) may choose specific repositories" / "obfuscating some details of the dataset due to ethical concerns"
- Key point: A study focused on a specific ecosystem (such as Apache) may select specific repositories; obfuscating some dataset details for ethical reasons is acceptable.

### E119

- Location: Repository Mining standard, Antipatterns
- Quote: "unvalidated, uni-dimensional operationalizations of multidimensional constructs (e.g. using github stars as a proxy for popularity)"
- Key point: Using an unvalidated, one-dimensional metric for a multidimensional construct (e.g. GitHub stars as a proxy for popularity) is an antipattern.

### E120

- Location: Repository Mining standard, Antipatterns
- Quote: "using open-source repositories without any filtering criteria; i.e., convenience sampling"
- Key point: Using open-source repositories without any filtering criteria is convenience sampling.

### E121

- Location: Repository Mining standard, Antipatterns
- Quote: "in a study where *all* the commits of a project need to be analyzed, only the GitHub repository is considered; a GitHub repository does not necessarily contain all commits of a project"
- Key point: When all of a project's commits must be analyzed, looking only at the GitHub repository is an antipattern, because it does not necessarily contain all commits.

### E122

- Location: Repository Mining standard, Antipatterns
- Quote: "limiting a study to quantitative description; failing to test, build or extend theory" / "conclusions must be derived in the context of the selected repositories" / "insufficient details about the applied processing steps of the selected repositories"
- Key point: Antipatterns: stopping at quantitative description without testing or building theory; generalizing beyond the selected repositories; giving insufficient detail on processing steps.

### E123

- Location: Repository Mining standard, Invalid Criticisms
- Quote: "more data, sources, or repositories required without appropriate justification" / "study doesn’t use qualitative analysis or data" / "a different source should have been used when the selected source(s) are justified"
- Key point: Invalid criticisms: demanding more data or repositories without justification; objecting that there is no qualitative analysis; demanding a different data source when the chosen one is justified.

### E124

- Location: Repository Mining standard, Invalid Criticisms
- Quote: "complaining about intentional obfuscation of repository details to protect participant's identities" / "in manual studies, requiring the disclosure of the time required for completion"
- Key point: Intentionally obfuscating repository details to protect participants, or not reporting the time a manual study took, should not be criticized.

### E125

- Location: General Standard, Essential
- Quote: "describes in detail what, where, when and how data were collected"
- Key point: Describe in detail what data were collected, where, when, and how.

### E126

- Location: General Standard, Antipatterns
- Quote: "Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- Key point: Acknowledging limitations but then writing conclusions as though they do not exist is an antipattern.

### E127

- Location: Sampling supplement, Essential (when representativeness is the goal)
- Quote: "presents a replicable, concise, algorithmic account of how other researchers could derive the same sample" / "explains how the sample could be biased along the sampling steps"
- Key point: Give a replicable, algorithmic account of the sampling steps so others could derive the same sample, and explain how each step could bias the sample.

### E128

- Location: Inter-Rater Reliability and Agreement supplement, whether multiple raters are needed
- Quote: "the more potentially controversial the judgment, the more we need multiple raters"
- Key point: The more potentially controversial the judgment, the more you need multiple raters.

### E129

- Location: Inter-Rater Reliability and Agreement supplement, Essential
- Quote: "describes the process by which two or more raters independently rated properties of research objects" / "describes how disagreements were resolved" / "reports an appropriate statistical measure of IRR/IRA"
- Key point: Describe how two or more raters independently rated items and how disagreements were resolved, and report an appropriate statistical measure of agreement.

### E130

- Location: Inter-Rater Reliability and Agreement supplement, Notes
- Quote: "IRA is a measure of agreement and can be calculated using (for example) Scott's π, Cohen's κ, Fleiss's κ and Krippendorff's α (for example)."
- Key point: Inter-rater agreement can be calculated with statistics such as Scott's π, Cohen's κ, Fleiss's κ, and Krippendorff's α.

### E131

- Location: Inter-Rater Reliability and Agreement supplement, Extraordinary
- Quote: "reports an iterative process with multiple cycles of (i) rating a subset of the data, (ii) resolving disagreements, and (iii) updating the rating scheme or decision rules until a minimum threshold indicates acceptable reliability/agreement"
- Key point: Extraordinary practice is an iterative process: rate a subset of the data, resolve disagreements, update the rating scheme or decision rules, and repeat until agreement reaches a minimum threshold.

### E132

- Location: Inter-Rater Reliability and Agreement supplement, Antipatterns
- Quote: "Pretending that the IRR or IRA statistic indicates good reliability when it is below established thresholds." / "Calculating multiple IRR/IRA measures and reporting only the most favourable (p-hacking)"
- Key point: Antipatterns: presenting agreement below established thresholds as good, or calculating several agreement measures and reporting only the most favorable.

### E133

- Location: Ethics (Studies with Secondary Human Data) supplement, Essential
- Quote: "describes all plausible, non-trivial potential risks or harms to data custodians and data subjects" / "states the grounds on which the data used was legitimately available to the researchers"
- Key point: Describe all plausible, non-trivial risks or harms to data custodians and data subjects, and state the grounds on which the data were legitimately available to the researchers.

### E134

- Location: Ethics (Studies with Secondary Human Data) supplement, footnote 1
- Quote: "the terms of use of a website explicitly permit scraping for the kind of information gathered and for the purposes of research"
- Key point: An example of legitimate availability: a website's terms of use explicitly permit scraping this kind of information for research purposes.

### E135

- Location: Ethics (Studies with Secondary Human Data) supplement, Antipatterns
- Quote: "Justifying data use as acceptable solely because it is technically available (e.g. machine accessible or downloadable) as opposed to legitimately available"
- Key point: Justifying data use solely because it is technically available (accessible, downloadable) rather than legitimately available is an antipattern.

### E136

- Location: Ethics (Studies with Secondary Human Data) supplement, Essential
- Quote: "explains how participants' privacy and reputation was respected in the conduct and reporting of the research. In particular, where multiple datasets are combined, explains how any additional privacy risks raised by this were mitigated."
- Key point: Explain how participants' privacy and reputation were respected in conducting and reporting the research; when combining datasets, explain how the additional privacy risks were mitigated.

### E137

- Location: Ethics (Studies with Secondary Human Data) supplement, footnote 6
- Quote: "Conditions for reidentification may include quoting ostensibly anonymous data content that can be resolved to its original source (and thus the identity of the originator) through a search engine."
- Key point: Quoting seemingly anonymous content that a search engine can trace back to its original source (and so to its author) enables reidentification.

### E138

- Location: Ethics (Studies with Secondary Human Data) supplement, Essential
- Quote: "how any further publication of the data (in existing, combined, or transformed form) will respect the expectations and consent given by data subjects"
- Key point: When republishing data (as is, combined, or transformed), explain how this respects the expectations and consent of data subjects.

### E139

- Location: Open Science supplement, Desirable Attributes and Notes
- Quote: "archives supplementary materials on preserved digital repositories such as" / "personal or institutional websites, version control systems (e.g. GitHub), consumer cloud storage (e.g. Dropbox), and commercial paper repositories (e.g. ResearchGate; Academia.edu) do not offer properly archived and preserved data."
- Key point: Archive supplementary materials on preserved repositories (e.g. Zenodo, figshare, Software Heritage, OSF); personal websites, version control platforms like GitHub, and consumer cloud storage are not proper archives.

### E140

- Location: Open Science supplement, Invalid Criticisms
- Quote: "Researchers should not complain that a study involves artifacts which— for good reasons—cannot be released."
- Key point: Materials that cannot be released for good reasons should not be grounds for criticism.

### E141

- Location: General Standard, Initial Checks (Editor)
- Quote: "presents new analysis not previously published in a peer-reviewed venue (i.e. preprints are fine)"
- Key point: The only requirement is that the analysis has not been published in a peer-reviewed venue; preprints do not count as published.

### E142

- Location: General Standard, General Quality Criteria
- Quote: "There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology"
- Key point: There are no universal quality criteria; each study should be assessed with criteria appropriate for its methodology.

### E143

- Location: Benchmarking Standard, definition under the title
- Quote: "A study in which a software system is assessed using a standard tool (i.e. a benchmark) for competitively evaluating and comparing methods, techniques or systems"
- Key point: Definition of benchmarking: assessing a system with a standard tool (a benchmark) to competitively evaluate and compare methods, techniques, or systems.

### E144

- Location: Benchmarking Standard, Application
- Quote: "investigates software systems within a defined context with an automated, repeatable procedure" / "studies the software system’s quality of service under a specific workload or usage profile"
- Key point: When it applies: studying software systems in a defined context with an automated, repeatable procedure, looking at the system's quality of service under a specific workload or usage profile.

### E145

- Location: Benchmarking Standard, Application
- Quote: "If the benchmark experiments primarily study software systems, use this standard." / "Benchmarking is often used with Engineering Research"
- Key point: Use the benchmarking standard when the experiments mainly study software systems; experiments with human participants, simulations of system models, and field studies use other standards. Benchmarking is often used together with engineering research.

### E146

- Location: Benchmarking Standard, Essential Attributes
- Quote: "EITHER: justifies the selection of an existing, publicly available or standard benchmark (in terms of relevance, timeliness, etc.)"
- Key point: Essential: when using an existing, public, or standard benchmark, justify the choice in terms of relevance, timeliness, and so on.

### E147

- Location: Benchmarking Standard, Essential Attributes
- Quote: "OR: defines a new benchmark, including: [...] the quality to be benchmarked (e.g., performance, availability, scalability, security), [...] the metric(s) to quantify the quality, [...] the measurement method(s) for the metric (if not obvious), [...] the workload, usage profile and/or task sample the system under test is subject to"
- Key point: Essential: a new benchmark must define four parts: the quality to be benchmarked, the metrics that quantify it, the measurement method for those metrics, and the workload or task sample the system is subjected to; justify the design and reuse design components of existing benchmarks where possible.

### E148

- Location: Benchmarking Standard, Essential Attributes
- Quote: "describes the experimental setup for the benchmark in sufficient detail to support independent replication" / "specifies the workload or usage profile in sufficient detail to support independent replication"
- Key point: Essential: describe both the experimental setup and the workload in enough detail to support independent replication.

### E149

- Location: Benchmarking Standard, Essential Attributes
- Quote: "allows different configurations of a system under test to compete on their merits without artificial limitations"
- Key point: Essential: let different configurations of the system under test compete on their merits without artificial limitations.

### E150

- Location: Benchmarking Standard, Essential Attributes
- Quote: "assesses stability or reliability using sufficient experiment repetitions and execution duration"
- Key point: Essential: assess the stability of results with sufficient experiment repetitions and execution duration.

### E151

- Location: Benchmarking Standard, Desirable Attributes
- Quote: "provides supplementary materials including datasets, analysis scripts and (for novel benchmarks) extended documentation" / "provides benchmark(s) in a usable form that facillitates independent replication"
- Key point: Desirable: provide supplementary materials (datasets, analysis scripts, extended documentation for new benchmarks) and provide the benchmark in a usable form that supports independent replication.

### E152

- Location: Benchmarking Standard, Desirable Attributes
- Quote: "uses or creates open source benchmarks" / "transparently reports on problems with executing benchmark runs, if any"
- Key point: Desirable: use or create open-source benchmarks; transparently report problems encountered while running the benchmark.

### E153

- Location: Benchmarking Standard, Desirable Attributes
- Quote: "reports on independent replication of the benchmark results" / "reports on a large community that uses the benchmark" / "reports on an independent organization that maintains the benchmark"
- Key point: Desirable: report independent replication of the results, a large community using the benchmark, or an independent organization maintaining it.

### E154

- Location: Benchmarking Standard, Extraordinary Attributes
- Quote: "provides empirical evidence for the relevance of a benchmark, e.g., using a Systematic Review" / "provides empirical evidence for the usability of a benchmark, e.g., using Action Research or Case Studies"
- Key point: Extraordinary: provide empirical evidence for the benchmark's relevance (e.g. through a systematic review) or usability (e.g. through action research or case studies).

### E155

- Location: Benchmarking Standard, General Quality Criteria
- Quote: "Fairness of measurements, reproducibility of results across experiment repetitions, benchmarking the *right* aspects, using a realistic benchmark with a representative workload"
- Key point: General quality criteria: fair measurement, results reproducible across repetitions, benchmarking the right aspects, and a realistic benchmark with a representative workload.

### E156

- Location: Benchmarking Standard, Examples of Acceptable Deviations
- Quote: "the nature of the benchmark requires specialized hardware (e.g. a quantum computer) so it not easy to replicate" / "in a study that replicates published existing work, the description of the experimental setup could be quite brief" / "the study only employs one (or a few) runs because prior work has shown that a single run is sufficient"
- Key point: Acceptable deviations: a benchmark that needs specialized hardware and is hard to replicate; a brief description of the setup when replicating published work; only one or a few runs when prior work shows one run is enough.

### E157

- Location: Benchmarking Standard, Antipatterns
- Quote: "Tailoring the benchmark for a specific method, technique or tool, which is evaluated with the benchmark." / "Using benchmarking experiments that are irrelevant for the problem studied to obfuscate weaknesses in the proposed approach"
- Key point: Antipatterns: tailoring the benchmark to the method being evaluated; using benchmark experiments irrelevant to the problem to obfuscate weaknesses of the proposed approach.

### E158

- Location: Benchmarking Standard, Antipatterns
- Quote: "Insufficient repetitions or duration to assess stability of results" / "Collecting aggregated measurements instead of persisting all raw results and running an offline analysis"
- Key point: Antipatterns: too few repetitions or too short a duration; collecting only aggregated measurements instead of keeping all raw results for offline analysis.

### E159

- Location: Benchmarking Standard, Invalid Criticisms
- Quote: "The benchmark is not widely used." / "Such a proto-benchmark (Sim et al. 2003) can act as a template to further the discussion of the topic and to initialize the consensus process." / "No independent replication of the benchmark results is reported." / "There is no independent organization that maintains the benchmark."
- Key point: Invalid criticisms: the benchmark is not widely used (a "proto-benchmark" from a small team can further discussion and start the consensus process); no independent replication is reported; no independent organization maintains the benchmark.

### E160

- Location: Engineering Research Standard, definition and Essential Attributes
- Quote: "Research that invents and evaluates technological artifacts" / "in which the artifact is assessed using one or more benchmarks"
- Key point: Engineering research invents and evaluates technological artifacts; benchmarking is one of several empirical ways to evaluate an artifact.

### E161

- Location: Engineering Research Standard, Essential Attributes
- Quote: "empirically compares the artifact to one or more state-of-the-art alternatives" / "empirically compares the artifact to one or more state-of-the-art benchmarks"
- Key point: Essential for engineering research: empirically compare the artifact with state-of-the-art alternatives or benchmarks (or explain why comparison is impractical).

### E162

- Location: Experiments standard, definition under the title
- Quote: "A study in which an intervention is deliberately introduced to observe its effects on some aspects of reality under controlled conditions"
- Key point: Definition of an experiment: deliberately introducing an intervention to observe its effects on some aspect of reality under controlled conditions.

### E163

- Location: Experiments standard, Application
- Quote: "manipulates one or more independent variables" / "controls many extraneous variables" / "applies each treatment independently to several experimental units" / "involves human participants"
- Key point: The standard covers experiments that meet four conditions: they manipulate one or more independent variables, control many extraneous variables, apply each treatment independently to several experimental units, and involve human participants.

### E164

- Location: Experiments standard, Application
- Quote: "In true experiments, experimental units are randomly allocated across treatments; quasi-experiments lack random assignment. Experiments include between-subjects, within-subjects and repeated measures designs. For experiments without human participants, see the **Exploratory Data Science Standard** or the **Engineering Research Standard**."
- Key point: True experiments randomly allocate experimental units; quasi-experiments lack random assignment. Experiments include between-subjects, within-subjects, and repeated-measures designs. Experiments without human participants should follow the Data Science or Engineering Research standard.

### E165

- Location: Experiments standard, Essential Attributes
- Quote: "states formal hypotheses" / "uses two-sided hypotheses OR justifies use of one-sided hypotheses based on face validity or previous work"
- Key point: Essential: state formal hypotheses; use two-sided hypotheses, or justify one-sided ones based on face validity or prior work.

### E166

- Location: Experiments standard, Essential Attributes
- Quote: "describes the dependent variable(s) and justifies how they are measured (including units, instruments)" / "describes the independent variable(s) and how they are manipulated or measured" / "describes extraneous variables and how they are controlled: physically, statistically, or not at all"
- Key point: Essential: describe the dependent variables and justify how they are measured (units, instruments); describe the independent variables and how they are manipulated or measured; describe extraneous variables and whether they were controlled physically, statistically, or not at all.

### E167

- Location: Experiments standard, Essential Attributes
- Quote: "justifies sample size (e.g. using power analysis)"
- Key point: Essential: justify the sample size, e.g. with a power analysis.

### E168

- Location: Experiments standard, Essential Attributes
- Quote: "describes the research design and protocol including treatments, materials, tasks, design (e.g. 2x2 factorial), participant allocation, period and sequences (for crossover designs), and logistics"
- Key point: Essential: describe the research design and protocol, including treatments, materials, tasks, design type (e.g. 2x2 factorial), participant allocation, periods and sequences for crossover designs, and logistics.

### E169

- Location: Experiments standard, Essential Attributes
- Quote: "EITHER: uses random assignment and explains logistics (e.g. how random numbers were generated)" / "OR: provides compelling justification for not using random assignment and explains how unequal groups threat to validity is mitigated (e.g. using pre-test/post-test and matched subjects design)"
- Key point: Essential: either use random assignment and explain how (e.g. how random numbers were generated), or give compelling justification for not doing so and explain how the threat of unequal groups was mitigated (e.g. pretest/posttest, matched designs).

### E170

- Location: Experiments standard, Essential Attributes and footnote 1
- Quote: "describes experimental objects (e.g. real or toy system) and their characteristics (e.g. size, type)" / "justifies selection of experimental objects; acknowledges object-treatment confounds, if any" / "For example, in an experiment where the control group applies Test-Driven Development (TDD) with Object 1 while the treatment group applies Test-Last-Development (TDD) with Object 2, the experimental object is confounded with the treatment."
- Key point: Essential: describe the experimental objects (real or toy system, size, type), justify their selection, and acknowledge object-treatment confounds; e.g. if the control group works on object 1 and the treatment group on object 2, object and treatment are confounded.

### E171

- Location: Experiments standard, Essential Attributes
- Quote: "confirms no incentives for participation were offered or describes financial or non-financial incentives"
- Key point: Essential: confirm that no incentives were offered, or describe the financial or non-financial incentives.

### E172

- Location: Experiments standard, Essential Attributes (results)
- Quote: "describes participants (e.g. age, gender, education, relevant experience or preferences)" / "reports distribution-appropriate descriptive and inferential statistics; justifies tests used" / "reports effects sizes with confidence intervals (if using frequentist approach)"
- Key point: Essential: describe participants (age, gender, education, relevant experience or preferences); report distribution-appropriate descriptive and inferential statistics and justify the tests used; with frequentist methods, report effect sizes with confidence intervals.

### E173

- Location: Experiments standard, Essential Attributes (discussion)
- Quote: "discusses construct, conclusion, internal, and external validity" / "discusses alternative interpretations of results"
- Key point: Essential: discuss construct, conclusion, internal, and external validity, and discuss alternative interpretations of the results.

### E174

- Location: Experiments standard, Desirable Attributes
- Quote: "provides supplementary material such as complete, algorithmic research protocol; task materials; raw, de-identified dataset; analysis scripts"
- Key point: Desirable: provide supplementary material such as a complete, algorithmic research protocol, task materials, a raw de-identified dataset, and analysis scripts.

### E175

- Location: Experiments standard, Desirable Attributes and footnote 3
- Quote: "explains deviations between design and execution, and their implications" / "e.g. dropouts affecting balance between treatment and control group."
- Key point: Desirable: explain deviations between design and execution and their implications, e.g. dropouts upsetting the balance between treatment and control groups.

### E176

- Location: Experiments standard, Desirable Attributes
- Quote: "analyzes construct validity of dependent variable" / "reports manipulation checks" / "pre-registration of hypotheses and design (where venue allows)"
- Key point: Desirable: analyze the construct validity of the dependent variable; report manipulation checks (confirming the treatment worked as intended); preregister hypotheses and design where the venue allows.

### E177

- Location: Experiments standard, Desirable Attributes
- Quote: "discusses alternative experimental designs and why they were not used (e.g. validity trade-offs)" / "includes visualizations of data distributions"
- Key point: Desirable: discuss alternative experimental designs and why they were not used (e.g. validity trade-offs); visualize data distributions.

### E178

- Location: Experiments standard, Extraordinary Attributes
- Quote: "reports multiple experiments or replications in different cultures or regions" / "uses multiple methods of data collection; data triangulation"
- Key point: Extraordinary: report multiple experiments or replications in different cultures or regions; use multiple data collection methods for data triangulation.

### E179

- Location: Experiments standard, Examples of Acceptable Deviations
- Quote: "Sample size is not justified by power analysis a priori because the study is conducted in a classroom in which the number of available participants is fixed."
- Key point: Acceptable deviation: in a classroom experiment with a fixed number of available participants, the sample size need not be justified by an a priori power analysis.

### E180

- Location: Experiments standard, Antipatterns
- Quote: "using bad proxies for dependent variables (e.g. task completion time as a proxy for task complexity)" / "quasi-experiments without a good reason" / "treatments or response variables are poorly described"
- Key point: Antipatterns: bad proxies for dependent variables (e.g. task completion time as a proxy for task complexity); quasi-experiments without a good reason; poorly described treatments or response variables.

### E181

- Location: Experiments standard, Antipatterns
- Quote: "data analysis technique used does not correspond to the design chosen or data characteristics (e.g. using an independent samples t-test on paired data)"
- Key point: Antipattern: an analysis technique that does not match the design or data characteristics, e.g. an independent-samples t-test on paired data.

### E182

- Location: Experiments standard, footnote 5
- Quote: "Quasi-experiments are appropriate for pilot studies or when assignment is beyond the researcher's control (e.g. assigning students to two different sections of a course). Simply claiming that a study is "exploratory" is not sufficient justification."
- Key point: Quasi-experiments suit pilot studies or cases where assignment is beyond the researcher's control (e.g. students already in two sections of a course); simply calling a study "exploratory" is not enough justification.

### E183

- Location: Experiments standard, Invalid criticisms
- Quote: "participants are students---appropriateness of participant characteristics should be judged based on the context, desired level of control, trade-off choices between internal and external validity, and the specifics of the technology (i.e. method, technique, tool, process, etc.) under evaluation; the choice must be explained in the paper"
- Key point: Invalid criticism: "the participants are students." Whether participants are appropriate depends on the context, the desired level of control, the trade-off between internal and external validity, and the technology being evaluated; but the paper must explain the choice.

### E184

- Location: Experiments standard, Invalid criticisms
- Quote: "low external validity" / "the experiment is a replication" / "the reviewer would have investigated the topic in any other way than an experiment" / "not enough participants (unless supported by power analysis)" / "not employing an incentivization scheme"
- Key point: Invalid criticisms: low external validity; the experiment is a replication; the reviewer would have studied the topic some way other than an experiment; not enough participants (unless backed by a power analysis); no incentive scheme.

### E185

- Location: Ethics (Studies with Human Participants) supplement, Essential Attributes
- Quote: "explains how participants were recruited" / "explains the compensation (if any) offered for participation and how coercion was mitigated"
- Key point: Essential: explain how participants were recruited, what compensation was offered, and how coercion was mitigated.

### E186

- Location: Ethics (Studies with Human Participants) supplement, footnote 1
- Quote: "If a gatekeeper was involved in recruitment, also explains how the gatekeeper was recruited, informed, and consented, and how power relationships between gatekeeper and individual participant were mitigated to ensure free individual informed consent."
- Key point: If recruitment went through a gatekeeper (e.g. a manager or course instructor), also explain how the power relationship between gatekeeper and participant was mitigated to ensure free, individual, informed consent.

### E187

- Location: Ethics (Studies with Human Participants) supplement, footnote 7
- Quote: "Participants must: (1) be debriefed in terms of the data captured and the reasons for deception, and (2) be offered the opportunity to withdraw themselves and their data at that point."
- Key point: When a study uses deception, participants must afterward be debriefed on what data were captured and why deception was used, and offered the chance to withdraw themselves and their data.

### E188

- Location: Data Science standard, definition
- Quote: "Studies that analyze software engineering phenomena or artifacts using data-centric analysis methods such as machine learning or other computational intelligence approaches as well as search-based approaches"
- Key point: Data science studies analyze software engineering phenomena or artifacts with data-centric methods such as machine learning (also other computational intelligence and search-based approaches).

### E189

- Location: Data Science standard, Application
- Quote: "Applies to studies that primarily analyze existing software phenomena using predictive, preemptive or corrective modelling." / "If the analysis focuses on the toolkit, rather that some new conclusions generated by the toolkit, consider the **Artifacts Standard**"
- Key point: It applies to studies that mainly analyze existing phenomena with predictive, preemptive, or corrective modeling; if the focus is the toolkit itself rather than new conclusions drawn with it, consult the artifact standard instead.

### E190

- Location: Data Science standard, Essential
- Quote: "explains how and why the data was selected" / "explains how the data was pre-processed, filtered, and categorized"
- Key point: You must explain how and why the data were selected, and how they were preprocessed, filtered, and categorized.

### E191

- Location: Data Science standard, Essential
- Quote: "EITHER: discusses state-of-art baselines (and their strengths, weaknesses and limitations)" / "OR: explains why no state-of-art baselines exist" / "OR: provides compelling argument that direct comparisons are impractical"
- Key point: You must discuss state-of-the-art baselines (with their strengths, weaknesses, and limitations), or explain why none exist, or argue compellingly that direct comparison is impractical.

### E192

- Location: Data Science standard, Essential
- Quote: "describes and justifies the evaluation metrics used" / "goes beyond single-dimensional summaries of performance (e.g., average; median) to include measures of variation, confidence, or other distributional information"
- Key point: You must describe and justify the evaluation metrics; results must go beyond averages or medians to include measures of variation, confidence, or other distributional information.

### E193

- Location: Data Science standard, Essential
- Quote: "describes the feature engineering approaches" / "defines the modeling approach(es) used (e.g. clustering then decision tree learning), typically using pseudocode" / "discusses the hardware and software infrastructure used"
- Key point: You must describe the feature engineering, the modeling approach (typically in pseudocode), and the hardware and software infrastructure used.

### E194

- Location: Data Science standard, Essential
- Quote: "justifies all statistics and (automated or manual) heuristics used" / "discusses technical assumptions and threats to validity that are specific to data science"
- Key point: You must justify every statistic and heuristic used, and discuss the technical assumptions and threats to validity specific to data science.

### E195

- Location: Data Science standard, Desirable
- Quote: "provides a replication package including source code and data set(s), or if data cannot be shared, synthetic data to illustrate the use of the algorithms"
- Key point: Provide a replication package with source code and datasets; if the data cannot be shared, provide synthetic data to illustrate how the algorithms are used.

### E196

- Location: Data Science standard, Desirable
- Quote: "data is processed by multiple learners, of different types"
- Key point: Process the data with multiple learners of different types.

### E197

- Location: Data Science standard, Desirable
- Quote: "data is processed multiple times with different, randomly selected, training/test examples; the results of which are compared via significance tests and effect size tests (e.g. cross-validation)"
- Key point: Process the data multiple times with different randomly selected training/test splits (e.g. cross-validation), and compare the results with significance tests and effect size tests.

### E198

- Location: Data Science standard, Desirable
- Quote: "carefully selects the hyperparameters that control the data miners (e.g. via analysis of settings in related work or some automatic hyperparameter optimizer such as grid search)"
- Key point: Select hyperparameters carefully, e.g. by analyzing settings in related work or using automatic hyperparameter optimization such as grid search.

### E199

- Location: Data Science standard, Desirable
- Quote: "manually inspects some non-trivial portion of the data (i.e. data sanity checks)"
- Key point: Manually inspect a non-trivial portion of the data as a sanity check.

### E200

- Location: Data Science standard, Desirable and footnote 8
- Quote: "clearly distinguishes evidence-based results from interpretations and speculation" / "Simply separating results and discussion into different sections is typically sufficient. No speculation in the results section."
- Key point: Clearly separate evidence-based results from interpretation and speculation; putting results and discussion in separate sections is usually enough, with no speculation in the results section.

### E201

- Location: Data Science standard, Extraordinary
- Quote: "leverages temporal data via longitudinal analyses" / "triangulates with qualitative data analysis of selected samples of the data" / "triangulates with other data sources, such as surveys or interviews" / "shares findings with and solicits feedback from the creators of the (software) artifacts being studied"
- Key point: Extraordinary attributes include using temporal data through longitudinal analysis, triangulating with qualitative analysis of selected samples, triangulating with other data sources such as surveys or interviews, and sharing findings with the creators of the studied artifacts to get feedback.

### E202

- Location: Data Science standard, Acceptable deviations
- Quote: "Using lighter and less precise data processing (e.g. keyword matching or random subsampling) if the scale of data is too large for a precise analysis to be practical." / "Data not shared because it is impractical (e.g. too large) or unethical (e.g. too sensitive)." / "Not all studies need statistics and hypotheses. Some studies can be purely or principally descriptive."
- Key point: Acceptable deviations: lighter processing (e.g. keyword matching, random subsampling) when the data are too large for precise analysis; not sharing data that are too large or too sensitive; some studies can be purely descriptive, without statistical tests or hypotheses.

### E203

- Location: Data Science standard, Antipatterns
- Quote: "Claiming causation without not only establishing covariaton and precedence but also eliminating third variable explanations and at least hypothesizing a generative mechanism."
- Key point: Before claiming causation you must establish covariation and precedence, eliminate third-variable explanations, and at least hypothesize a generative mechanism; claiming causation without this is an antipattern.

### E204

- Location: Data Science standard, Antipatterns
- Quote: "Pre-processing changes training and test data; e.g. while it may be useful to adjust training data class distributions via (say) sub-sampling of majority classes, that adjustment should not applied to the test data"
- Key point: Preprocessing must not change both training and test data; e.g. you may subsample the majority class to adjust class distributions in the training data, but the test data must not be adjusted and should stay as in the "real world."

### E205

- Location: Data Science standard, Antipatterns
- Quote: "Using statistical tests without checking their assumptions." / "Significance tests without effect size tests; effect sizes without confidence intervals." / "Reporting a median, without any indication of variance (e.g., a boxplot)."
- Key point: Antipatterns: using statistical tests without checking their assumptions; significance tests without effect sizes, or effect sizes without confidence intervals; reporting a median without any indication of variance.

### E206

- Location: Data Science standard, Invalid Criticisms
- Quote: "You should have analyzed data ABC. The question reviewers should ask is whether the papers main claims are supported by the data that was analyzed, not whether some other data would have been better." / "Does not have a reproduction package. These are desirable, not essential (yet)." / "Study does not make causal claims, when it cannot."
- Key point: Invalid criticisms: "you should have analyzed other data" (the question is whether the claims are supported by the data analyzed); "there is no replication package" (currently desirable, not essential); "the study makes no causal claims" (it should not make claims it cannot support).

### E207

- Location: Data Science standard, Essential
- Quote: "explains why it is timely to investigate the proposed problem using the proposed method"
- Key point: You must explain why it is timely to investigate the problem with the proposed method.

### E208

- Location: Replication Standard, definition under the title
- Quote: "A study that deliberately repeats a previous study (the "original study") to determine whether its results can be reproduced"
- Key point: Definition of a replication: a study that deliberately repeats a previous study (the original study) to determine whether its results can be reproduced.

### E209

- Location: Replication Standard, Application
- Quote: "The replication attempt is deliberate and planned, not accidental overlap with a previous study." / "The original study is clearly identified as a separate previous publication."
- Key point: When it applies: the replication is deliberate and planned, not an accidental overlap with earlier work, and the original study is clearly identified as a separate previous publication.

### E210

- Location: Replication Standard, Definitions
- Quote: "To reproduce [...] means to repeat the original study's data analysis on the original study's data." / "To replicate [...] means to repeat a study by collecting new data and repeating the original study's analysis on the new data."
- Key point: SIGSOFT usage: to reproduce means repeating the original analysis on the original data; to replicate means collecting new data and repeating the original analysis on them. (The original terms link to the SIGSOFT glossary; the quote omits the links with [...].)

### E211

- Location: Replication Standard, footnote 1
- Quote: "Exact replication: same research questions, same method, same context. Methodological replication: same research questions, same method, different context. Conceptual replication: same research questions, different method, different context."
- Key point: Three types by methodological similarity: exact replication (same questions, method, and context); methodological replication (same questions and method, different context); conceptual replication (same questions, different method and context).

### E212

- Location: Replication Standard, footnote 2
- Quote: "Partial replication: addresses a subset of the original research questions. Complete replication: addresses each of the original reseach questions. Extended replication: addresses each of the original reseach questions and additional ones."
- Key point: Three types by coverage: partial replication (a subset of the original questions); complete replication (all original questions); extended replication (all original questions plus new ones).

### E213

- Location: Replication Standard, footnote 3
- Quote: "Internal replication: the replicating team is the same as the original study's team. External replication: the replicating team is different from the original study's team. Mixed replication: overlaps exist between the replicating team and the original study's team."
- Key point: Three types by team: internal replication (same team); external replication (different team); mixed replication (the two teams overlap).

### E214

- Location: Replication Standard, Essential Attributes
- Quote: "discusses the motivation for conducting the replication in appropriate detail (e.g., to validate the results, to broaden the results by changing the participant pool or the artifacts)"
- Key point: Essential: explain the motivation for the replication, e.g. to validate the results or to broaden them by changing the participant pool or artifacts.

### E215

- Location: Replication Standard, Essential Attributes
- Quote: "defines the type of the replication by methodological similarity (exact, methodological, conceptual)" / "defines the type of the replication by overlap (partial, complete, extended)" / "defines the type of the replication by participants (internal, external, mixed)"
- Key point: Essential: state the type of replication by methodological similarity, coverage, and team.

### E216

- Location: Replication Standard, Essential Attributes
- Quote: "the research questions of the original study" / "the design of the original study" / "the context variables of the original study that might have affected the design of the study or interpretation of the results" / "the major findings of the original study"
- Key point: Essential: describe the original study adequately, including its research questions, design, participants, artifacts, context variables that may have affected the design or interpretation, and main findings.

### E217

- Location: Replication Standard, Essential Attributes
- Quote: "EITHER: describes overlap or interactions with the original study author(s),"
- Key point: Essential: either describe overlap or interactions with the original authors, or confirm they were not involved.

### E218

- Location: Replication Standard, Essential Attributes
- Quote: "describes and justifies any differences from the original study (design, participants, artifacts, procedures, data collection, or analysis)"
- Key point: Essential: describe and justify every difference from the original study (design, participants, artifacts, procedures, data collection, or analysis).

### E219

- Location: Replication Standard, Essential Attributes
- Quote: "compares the results of the replication to the results of the original study" / "clearly differentiates between results that are consistent and inconsistent with the original study"
- Key point: Essential: compare the replication's results with the original study's, clearly separating consistent from inconsistent results.

### E220

- Location: Replication Standard, Desirable Attributes
- Quote: "clearly seperates information about (i) the original study, (ii) the replication, (iii) the comparison of results, and (iv) conclusions"
- Key point: Desirable: clearly separate information about the original study, the replication, the comparison of results, and the conclusions.

### E221

- Location: Replication Standard, Desirable Attributes
- Quote: "improves on the original study in some way (e.g., design, analysis, statistical power)"
- Key point: Desirable: improve on the original study in some way, e.g. design, analysis, or statistical power (a study's ability to detect a real effect, which usually rises with sample size).

### E222

- Location: Replication Standard, Desirable Attributes
- Quote: "differentiates between minor and major differences when discussing inconsistent results, elaborates on whether the differences are reasonable and/or expected"
- Key point: Desirable: when discussing inconsistent results, distinguish minor from major differences and discuss whether they are reasonable or expected.

### E223

- Location: Replication Standard, Desirable Attributes
- Quote: "draws conclusions across the two (or more) studies; provides insights that would not have been evident from either study individually" / "highlights any conclusions of the original study that were strengthened"
- Key point: Desirable: draw conclusions across the two (or more) studies that neither would show alone, and highlight which conclusions of the original study were strengthened.

### E224

- Location: Replication Standard, Desirable Attributes
- Quote: "compares the limitations of the replication to the limitations of the original study" / "proposes hypotheses about new context variables that may have become evident through the analysis of multiple studies"
- Key point: Desirable: compare the limitations of the replication with those of the original study; propose hypotheses about new context variables that emerge only from analyzing multiple studies.

### E225

- Location: Replication Standard, Desirable Attributes
- Quote: "protocol of the replication was checked/reviewed by the original authors"
- Key point: Desirable: the replication protocol was checked or reviewed by the original authors.

### E226

- Location: Replication Standard, Desirable Attributes (for families of replications)
- Quote: "provides a brief summary of the previous studies and replications, including information about how the studies were related, conclusions drawn and current state of knowledge about the topic" / "places the results into the context of the entire family of studies"
- Key point: Desirable (families of replications): briefly summarize the previous studies and replications and place the new results within the whole family.

### E227

- Location: Replication Standard, Antipatterns
- Quote: "replicating an underpowered study with a second, equally-underpowered study" / "repeating rather than correcting mistakes (e.g. using inappropriate statistical tests) in the original study"
- Key point: Reviewing antipatterns: replicating an underpowered study with an equally underpowered one; repeating rather than correcting the original study's mistakes (e.g. inappropriate statistical tests).

### E228

- Location: Replication Standard, Invalid Criticisms
- Quote: "The replication merely confirms the findings of the original study; no inconsistencies are reported."
- Key point: Invalid criticism: the replication "merely" confirms the original findings and reports no inconsistencies.

### E229

- Location: Replication Standard, Invalid Criticisms
- Quote: "Failing to publish (e.g., in a replication package) materials owned by the original study authors who have not given permission to publish them."
- Key point: Invalid criticism: not publishing materials owned by the original authors who have not given permission.

### E230

- Location: Replication Standard, Invalid Criticisms
- Quote: "Criticizing the research questions including their wording or formulation (since the research questions are set in the original study, the replication must follow them, even in conceptual replications)."
- Key point: Invalid criticism: criticizing the research questions or their wording; the questions are set by the original study and the replication must follow them, even in a conceptual replication.

### E231

- Location: Questionnaire Surveys standard, definition
- Quote: "A study in which a sample of respondents answer a series of (mostly structured) questions, typically through a computerized or paper form"
- Key point: A questionnaire survey is a study in which a sample of respondents answer a series of (mostly structured) questions, typically through a computerized or paper form.

### E232

- Location: Questionnaire Surveys standard, Application
- Quote: "a sample of participants answer predefined, mostly closed-ended questions (typically online or on paper)" [...] "researchers systematically analyze participants' answers"
- Key point: It applies to studies where participants answer predefined, mostly closed-ended questions and researchers systematically analyze the answers.

### E233

- Location: Questionnaire Surveys standard, Application
- Quote: "This standard does not apply to questionnaires comprising predominately open-ended questions"
- Key point: The standard does not apply to questionnaires made up mainly of open-ended questions.

### E234

- Location: Questionnaire Surveys standard, Variations
- Quote: "provide a detailed account of the properties of a phenomenon or population." [...] "generate insights, hypotheses or models for further research." [...] "testing formal (e.g. causal) propositions to explain a phenomenon."
- Key point: There are three kinds of questionnaire survey: descriptive (a detailed account of the properties of a phenomenon or population), exploratory (generating insights, hypotheses, or models for further research), and confirmatory (testing formal, e.g. causal, propositions).

### E235

- Location: Questionnaire Surveys standard, Essential Attributes
- Quote: "identifies the target population and defines the sampling strategy" [...] "describes how participants were selected or recruited (e.g. sampling frame, advertising, invitations, incentives)"
- Key point: Essential: identify the target population and define the sampling strategy; describe how participants were selected or recruited (sampling frame, advertising, invitations, incentives).

### E236

- Location: Questionnaire Surveys standard, Essential Attributes
- Quote: "EITHER: measures constructs using (or adapting) validated scales OR: analyzes construct validity (including content, convergent, discriminant and predictive validity) ex post"
- Key point: Essential: either measure constructs with (or by adapting) validated scales, or analyze construct validity ex post (content, convergent, discriminant, and predictive validity).

### E237

- Location: Questionnaire Surveys standard, Essential Attributes
- Quote: "describes how responses were managed/monitored, including contingency actions for non-responses and drop-outs" [...] "explains handling of missing data (e.g. imputation, weighting adjustments, discarding)"
- Key point: Essential: describe how responses were managed and monitored, including contingency actions for non-responses and drop-outs; explain how missing data were handled (imputation, weighting adjustments, discarding).

### E238

- Location: Questionnaire Surveys standard, Essential Attributes
- Quote: "analyzes response rates" [...] "assesses sufficiency of number of participants (statistical power)"
- Key point: Essential: analyze response rates; assess whether the number of participants is sufficient (statistical power).

### E239

- Location: Questionnaire Surveys standard, Essential Attributes
- Quote: "acknowledges generalizability threats; discusses how respondents may differ from target population"
- Key point: Essential: acknowledge threats to generalizability and discuss how respondents may differ from the target population.

### E240

- Location: Questionnaire Surveys standard, Essential Attributes and footnote 3
- Quote: "provides the questionnaire instrument (as an appendix or supplementary materials)" [...] "the questionnaire design matches the research aims and the target population" [...] "Questions are mapped to research objectives and their wording and format is appropriate for their audience."
- Key point: Essential: provide the questionnaire instrument (in an appendix or supplementary materials); the design must match the research aims and target population, i.e. each question maps to a research objective, with wording and format suited to respondents.

### E241

- Location: Questionnaire Surveys standard, Desirable Attributes
- Quote: "includes mechanisms to detect participants using AI or other automated means to answer questions; excludes AI-generated responses" [...] "includes attention-check items in the questionnaire; excludes participants who fail one or more of these checks"
- Key point: Desirable: include mechanisms to detect and exclude participants answering with AI or other automated means; include attention-check items and exclude those who fail them.

### E242

- Location: Questionnaire Surveys standard, Desirable Attributes
- Quote: "validates whether the instrument's items, layout, duration, and technology are appropriate (e.g. using pilots, test-retest, or expert and non-expert reviews)" [...] "reports how the instrument has evolved through the validation process (if at all)"
- Key point: Desirable: validate whether the instrument's items, layout, duration, and technology are appropriate (pilots, test-retest, expert and non-expert reviews), and report how the instrument changed through validation.

### E243

- Location: Questionnaire Surveys standard, Desirable Attributes
- Quote: "analyzes response bias (quantitatively)" [...] "applies techniques for improving response rates (e.g. incentives, reminders, targeted advertising)"
- Key point: Desirable: analyze response bias quantitatively; use techniques such as incentives, reminders, and targeted advertising to improve response rates.

### E244

- Location: Questionnaire Surveys standard, Desirable Attributes
- Quote: "discusses possible effects of incentives (e.g. on voluntariness, response rates, response bias) if used"
- Key point: Desirable: if incentives were used, discuss their possible effects on voluntariness, response rates, and response bias.

### E245

- Location: Questionnaire Surveys standard, Desirable Attributes
- Quote: "provides supplementary materials including instrument(s), code books, analysis scripts and dataset(s)" [...] "accounts for the principles of research ethics (e.g. informed consent, re-identification risk)"
- Key point: Desirable: provide supplementary materials such as the instrument, code books, analysis scripts, and datasets; account for research ethics principles (informed consent, re-identification risk).

### E246

- Location: Questionnaire Surveys standard, Extraordinary Attributes
- Quote: "provides feasibility check of the anticipated data analysis techniques" [...] "reports on the scale validation in terms of dimensionality, reliability, and validity of measures"
- Key point: Extraordinary: check in advance that the planned analysis techniques are feasible; report scale validation in terms of dimensionality, reliability, and validity.

### E247

- Location: Questionnaire Surveys standard, Examples of Acceptable Deviations
- Quote: "Ommitting part of a questionnaire instrument from supplementary materials due to copyright issues (in which case the paper should cite the source of the questions)" [...] "Doesn't describe handling of drop-outs or missing data because there were none"
- Key point: Acceptable deviations: omitting part of the instrument for copyright reasons (while citing the source of the questions); not describing the handling of drop-outs or missing data when there were none.

### E248

- Location: Questionnaire Surveys standard, Invalid Criticism
- Quote: "Not reporting response rate for open public subscription surveys" [...] "Failure to release full data sets despite the data being sensitive." [...] "Claiming the sample size is too small without justifying why the sample size is insufficient to answer the research questions." [...] "Criticizing the relevance of a survey on the basis that responses only capture general people's perceptions."
- Key point: Invalid criticisms: not reporting a response rate for open public surveys anyone can fill in; not releasing full datasets when the data are sensitive; calling the sample too small without justification; dismissing a survey because it "only reflects people's opinions."

### E249

- Location: Questionnaire Surveys standard, Invalid Criticism
- Quote: "The results are considered controversial or hardly surprising." [...] "The results do not accord with the reviewer's personal experience or previous studies."
- Key point: Invalid criticisms: the results are controversial or hardly surprising; the results do not match the reviewer's personal experience or previous studies.

### E250

- Location: Sampling Supplement, Desirable Attributes
- Quote: "online survey: using respondent-driven rather than snowball sampling"
- Key point: Desirable: for online surveys, use respondent-driven rather than snowball sampling.

### E251

- Location: Sampling Supplement, Antipatterns
- Quote: "making claims about a population, based on sample, without providing an argument for representativeness"
- Key point: Reviewing antipattern: making claims about a population from a sample without arguing for representativeness.

### E252

- Location: Sampling Supplement, Invalid Criticisms
- Quote: "abstractly criticizing generalizability rather than pointing to best practices; e.g. complaining that the results may not generalize (bad) instead of pointing out that participation reminders should have been sent to mitigate response bias (good);"
- Key point: Invalid criticism: abstractly questioning generalizability instead of pointing to best practices; e.g. say "participation reminders should have been sent to mitigate response bias," not just "the results may not generalize."

### E253

- Location: Ethics (Studies with Human Participants) Supplement, footnote 2
- Quote: "careful consideration of the reidentification potential through others combining multiple data sources (such as social media, or contextual information like company plus job role)"
- Key point: When protecting privacy, consider the potential for others to reidentify participants by combining multiple sources (social media, or contextual information like company plus job role).

### E254

- Location: Ethics (Studies with Human Participants) Supplement, Invalid Criticisms
- Quote: "is not a valid criticism where consent was given orally or implied (e.g., by completing a questionnaire that is explicitly part of a research project)."
- Key point: When consent was given orally or implied (e.g. by completing a questionnaire explicitly part of a research project), "no consent form was used" is not a valid criticism.

### E255

- Location: Ethics (Studies with Human Participants) Supplement, Essential Attributes
- Quote: "explains the compensation (if any) offered for participation and how coercion was mitigated"
- Key point: Essential: explain any compensation offered to participants and how coercion was mitigated.

### E256

- Location: Qualitative Surveys (Interview Studies) standard, definition
- Quote: "Research comprising semi-structured or open-ended interviews"
- Key point: A qualitative survey (interview study) is research made up of semi-structured or open-ended interviews; it has a separate standard from questionnaire surveys.

### E257

- Location: Longitudinal standard, definition and Application
- Quote: "A study focusing on the changes in and evolution of a phenomenon over time" / "This standard applies to studies that involve repeated observations of the same variables (e.g., productivity or technical debt) over a period of time. Longitudinal studies include the analysis of datasets over time, such as the analysis of the evolution of the code."
- Key point: A longitudinal study focuses on how a phenomenon changes and evolves over time, with repeated observations of the same variables (e.g. productivity, technical debt) over a period; analyzing time-varying datasets such as code evolution also counts.

### E258

- Location: Longitudinal standard, Application
- Quote: "Longitudinal studies require to maintain identifiability of subjects (humans or artifacts) between data collection waves and to use at least two waves." / "For cross-sectional analysis, consider the **Exploratory Data Science Standard** or the **Experiments Standard** (if variables are manipulated)."
- Key point: Longitudinal studies require subjects (humans or artifacts) to stay identifiable across data collection waves, with at least two waves; cross-sectional analysis at one point in time should follow the Exploratory Data Science standard, and studies that manipulate variables the Experiments standard.

### E259

- Location: Longitudinal standard, Essential and footnote 1
- Quote: "determines the appropriate number of waves based on the natural oscillation of the research phenomenon" / "uses at least two data collection waves" / "subjects (humans or artifacts) are identifiable between waves"
- Key point: Essential: choose the number of waves based on the natural oscillation of the phenomenon; use at least two waves; keep subjects identifiable across waves.

### E260

- Location: Longitudinal standard, Essential and footnotes 2 and 3
- Quote: "justifies the data analysis strategy" / "the data analysis strategy is appropriate for the interdependent nature of the data"
- Key point: Essential: justify the analysis strategy, which must suit the interdependent nature of longitudinal data.

### E261

- Location: Longitudinal standard, Essential, footnote 4
- Quote: "Typically, longitudinal analyses deal with many variables and multiple comparisons, increasing the likelihood to obtain results within traditionally acceptable thresholds. For this reason, authors are advised to adjust the critical alpha level [...] or use Bayesian statistics"
- Key point: Longitudinal analyses usually involve many variables and multiple comparisons, making chance "significant" results more likely, so adjusting the significance threshold (e.g. p < 0.001) or using Bayesian statistics is advised.

### E262

- Location: Longitudinal standard, Essential
- Quote: "justifies sample size (e.g. using power analysis)" / "describes data loss throughout the different waves" / "explains how missing data are handled"
- Key point: Essential: justify the sample size (e.g. with power analysis); describe data loss across waves; explain how missing data are handled.

### E263

- Location: Longitudinal standard, Essential and footnotes 6 and 7
- Quote: "describes the subjects (e.g., demographic information in the case of humans)" / "discusses the operationalization of the research model (i.e. construct validity)" / "which type of quality controls have been performed on software repositories to ensure the consistency and homogeneity of artifacts?"
- Key point: Essential: describe the subjects and discuss how concepts were operationalized into measures (construct validity); the footnote's example is that for software repositories you should say what quality controls ensured the artifacts were consistent and homogeneous.

### E264

- Location: Longitudinal standard, Desirable
- Quote: "investigates causality using the longitudinal nature of the data to establish precedence and statistically controlling for third-variable explanations" / "discusses potential confounding factors (for inferential analyses) that cannot be statistically controlled"
- Key point: Desirable: investigate causality by using the longitudinal data to establish precedence and statistically controlling for third-variable explanations; discuss potential confounders that cannot be controlled statistically.

### E265

- Location: Longitudinal standard, Desirable
- Quote: "discusses data (in)consistency across waves (e.g. test-retest reliability)" / "examines differences in distributions between waves (and uses an appropriate data analysis strategy)"
- Key point: Desirable: discuss data (in)consistency across waves (e.g. test-retest reliability) and examine differences in distributions between waves.

### E266

- Location: Longitudinal standard, Desirable and footnote 8
- Quote: "addresses survivorship bias" / "For example, if you analyze the past 100 years of stock market performance based on the markets that exist today, you get much higher average returns than if you analyze all the markets that existed 100 years ago."
- Key point: Desirable: address survivorship bias. Example: analyzing the past 100 years of stock market performance using only the markets that exist today gives much higher average returns than analyzing all markets that existed 100 years ago.

### E267

- Location: Longitudinal standard, Desirable
- Quote: "provides supplementary materials including data sets, data collection scripts or instruments, analytical scripts, a description of how to reproduce the work and any other materials used" / "describes the cost of gathering data and any incentives used"
- Key point: Desirable: provide supplementary materials such as datasets, data collection scripts or instruments, analysis scripts, and reproduction instructions; describe the cost of gathering data and any incentives used.

### E268

- Location: Longitudinal standard, Extraordinary
- Quote: "uses a multi-stage selection process to identify the study's subjects" / "follows subjects for an exceptionally long period (e.g. more than five years)"
- Key point: Extraordinary: use a multi-stage selection process to identify subjects; follow subjects for an exceptionally long period (e.g. more than five years).

### E269

- Location: Longitudinal standard, General Quality Criteria
- Quote: "Longitudinal studies exploit the temporal nature of data to maximize internal validity. Other criteria are sometimes sacrificed to improve internal validity."
- Key point: Longitudinal studies exploit the temporal nature of data to maximize internal validity, sometimes sacrificing other quality criteria to do so.

### E270

- Location: Longitudinal standard, Antipatterns
- Quote: "subject loss between waves is too high, leading to a severely underpowered study" / "the period between waves does not match the phenomenon's natural cycles" / "treating longitudinal data as cross-sectional"
- Key point: Antipatterns: subject loss between waves so high that the study is severely underpowered; intervals between waves that do not match the phenomenon's natural cycles; treating longitudinal data as cross-sectional.

### E271

- Location: Longitudinal standard, Variations
- Quote: "_Experience sampling_ provides a highly specific understanding of a phenomenon through multiple repeated measurements per day over a short period (typically one to three weeks). It emphasizes in-the-moment assessment rather than reflective assessment" / "_Cohort studies_ are a type of analytical observational study where researchers investigate the relationship between an independent and dependent variable by observing subjects over time and comparing groups with different levels of exposure. Cohort studies follow more strict rules than presented here."
- Key point: Two variations: experience sampling (several measurements a day over one to three weeks, emphasizing in-the-moment assessment rather than recall) and cohort studies (observing subjects over time and comparing groups with different levels of exposure), which have stricter rules than this standard.

### E272

- Location: Longitudinal standard, Invalid Criticisms
- Quote: "Claiming that the time span between measurements is too short or too long." / "Claiming that the number of waves is inadequate without a reasoned explanation." / "Claiming that the sample size is too small without performing a _post hoc_ power calculation."
- Key point: Invalid criticisms: vaguely claiming the interval between measurements is too short or too long; claiming there are too few waves without a reasoned explanation; calling the sample too small without a post hoc power calculation.

### E273

- Location: Longitudinal standard, Invalid Criticisms
- Quote: "Claiming that the paper with a modest number of comparisons should have used more conservative alphas or adopted a Bayesian approach." / "Complaining about generalizability when the paper clearly acknowledges limitations to generalizability."
- Key point: Invalid criticisms: demanding more conservative significance thresholds or Bayesian methods when there are only a modest number of comparisons; complaining about generalizability when the paper clearly acknowledges those limitations.

### E274

- Location: Multi-Methodology and Mixed Methods standard, definition
- Quote: "Studies that use two or more approaches to data collection or analysis to corroborate, complement and expand research findings (multi-methodology) or combine and integrate inductive research with deductive research (mixed methods), often but not necessarily relying on qualitative and/or quantitative data."
- Key point: Multi-methodology studies use two or more approaches to data collection or analysis to corroborate, complement, and expand findings; mixed methods studies combine and integrate inductive with deductive research, often but not necessarily involving qualitative and quantitative data.

### E275

- Location: Multi-Methodology and Mixed Methods standard, Application
- Quote: "It enumerates criteria related to the mixing of methodologies, not the methodologies themselves. For the latter, refer to method-specific standards. For example, a multi-methodology study combining a case study with an experiment should comply with **The Case Study Standard** and **The Experiment Standard** as well as this standard."
- Key point: This standard covers only how methods are mixed, not the methods themselves; each component must also meet its own method's standard, e.g. a study combining a case study and an experiment must meet the Case Study standard, the Experiments standard, and this one.

### E276

- Location: Multi-Methodology and Mixed Methods standard, Essential
- Quote: "**justifies** using multiple methodologies and/or methods" / "provides a **purpose statement** that conveys the overarching multi or mixed method design intent (why)" / "describes the **multi-methodology**, **multi-method** or **mixed method** design (what)" / "describes **which phases** of the research study the different methods or methodologies are used in (when)" / "describes how the design aligns with the research question or objective"
- Key point: Essential: justify using multiple methods; give a purpose statement conveying the overall design intent (why); describe the design (what); say at which stage of the study each method is used (when); explain how the design maps to the research questions.

### E277

- Location: Multi-Methodology and Mixed Methods standard, Essential and footnote 1
- Quote: "**integrates the findings** from all methods to address the research question/objective" / "acknowledges the **limitations** associated with integrating findings" / "e.g., samples that are drawn from different populations may introduce limitations when the findings are integrated, or biases may be introduced by the sequential or parallel nature of a mixed design"
- Key point: Essential: integrate the findings from all methods to answer the research question; acknowledge the limitations of integration, e.g. samples drawn from different populations, or biases introduced by sequential or concurrent designs.

### E278

- Location: Multi-Methodology and Mixed Methods standard, Desirable
- Quote: "**defines** the multi-methodology or mixed method design used" / "describes and justifies **sample reuse** (or no reuse, or partial reuse) across methods" / "illustrates the research design using a **visual model** (diagram)" / "indicates the use of multiple methods or mixed method design in the **title**"
- Key point: Desirable: define the design used; describe and justify sample reuse (or not) across methods; illustrate the design with a visual model; signal multi- or mixed methods in the title.

### E279

- Location: Multi-Methodology and Mixed Methods standard, Desirable
- Quote: "**distinguishes the additional value** from using a multi-methodology or mixed method design in terms of corroboration, complementarity, and expansion (breadth and depth)" / "discusses **discrepancies and incongruent findings** from the use of multiple methods"
- Key point: Desirable: spell out the added value of mixing, whether corroboration, complementarity, or expansion (breadth and depth); discuss discrepancies and incongruent findings across methods.

### E280

- Location: Multi-Methodology and Mixed Methods standard, Desirable
- Quote: "describes the main **philosophical, epistemological, and/or theoretical foundations** that the authors use and relate those to the planned use of multi or mixed methods in the study" / "describes the **challenges** faced in the design and how those were or could be mitigated" / "describes **ethical issues** that may have been presented through the blend of multi- or mixed methods"
- Key point: Desirable: describe the philosophical, epistemological, or theoretical foundations and how they relate to the mixed design; describe challenges faced in the design and how they were mitigated; discuss ethical issues raised by mixing methods.

### E281

- Location: Multi-Methodology and Mixed Methods standard, General Quality Criteria
- Quote: "General quality criteria discussed in the guidelines for each method should be considered.  In the case of a multi-methodology or multi-method design, the reliability of the findings that are specific to the triangulation goals should be assessed."
- Key point: The quality criteria of each method all apply; for multi-method designs, also assess the reliability of findings tied to the triangulation goal.

### E282

- Location: Multi-Methodology and Mixed Methods standard, Antipatterns
- Quote: "**Smoke and mirrors:** Overselling a study as a multi-methodology or mixed method design when one approach at best offers a token or anecdotal contribution to the research motivation or findings" / "**Selling your soul:** Employing an additional method to appeal to a methodological purist during the review process that does not contribute substantively to the research findings"
- Key point: Antipatterns: "smoke and mirrors," overselling a study as mixed methods when one approach adds only a token contribution; "selling your soul," adding a method that contributes nothing substantive just to please reviewers.

### E283

- Location: Multi-Methodology and Mixed Methods standard, Antipatterns
- Quote: "**Uninvited guest:** A research method is not clearly introduced in the paper introduction/methodology and makes an unexpected entrance in the discussion or limitations sections of the paper" / "**Integration failure:** Poor integration of findings from all methods used" / "**Limitation shirker**: Failure to discuss limitations from all methods used or from their integration"
- Key point: Antipatterns: the "uninvited guest," a method not introduced in the introduction or methodology that suddenly appears in the discussion or limitations; "integration failure," findings from the methods not properly integrated; and failing to discuss the limitations of the methods and their integration.

### E284

- Location: Multi-Methodology and Mixed Methods standard, Antipatterns
- Quote: "**Missing the mark:** Misalignment of multi- or mixed method design with the research question/objective" / "**Cargo cult research:** Using methods where the research team lacks expertise in those methods, but hopes they work" / "**Design by committee:** Failure to agree on a crisp research question/objective (may be induced by different epistemological perspectives or use of heterogeneous methods)"
- Key point: Antipatterns: "missing the mark," a design misaligned with the research question; "cargo cult research," using methods the team lacks expertise in and hoping they work; the team never agreeing on a clear research question because of differing epistemological positions or methods.

### E285

- Location: Multi-Methodology and Mixed Methods standard, Antipatterns
- Quote: "**Golden hammer:** relying on superficial, typically quantitative analysis of rich qualitative data" / "**Sample contamination:** a mixed method sequential design where the same participants are used in multiple, sequential methods without accounting for potential contamination from earlier method(s) to later ones." / "**Ignoring the writing on the wall:** In a mixed method sequential design, failing to use findings from an earlier study when forming an instrument for a study in a later phase of the research"
- Key point: Antipatterns: the "golden hammer," superficial (typically quantitative) analysis of rich qualitative data; "sample contamination," using the same participants across sequential phases without considering how earlier phases affect later ones; designing later-phase instruments without drawing on earlier-phase findings.

### E286

- Location: Multi-Methodology and Mixed Methods standard, Examples of Acceptable Deviations
- Quote: "Conference page limits may make it particularly challenging to share sufficient details on all methods used. These details may be available in other publications or supplementary materials." / "Describing the research in terms of cycles or ongoing parallel processes instead of phases."
- Key point: Acceptable deviations: with conference page limits, details on each method can be in other publications or supplementary materials; the research can be described as cyclical or parallel processes rather than "phases."

### E287

- Location: Multi-Methodology and Mixed Methods standard, Invalid Criticisms
- Quote: "The method(ologie)s do not contribute equally (a non-equal design) or the minor method is limited (e.g. few participants)." / "The mixed- or multi-method approach isn't necessary (when it *is* beneficial)" / "The method(ologie)s have different philosophical foundations or are otherwise incompatible" / "In an unequal design, the wrong method is dominant (this is a study design choice not a flaw )" / "The method(ologie)s have inconsistent findings"
- Key point: Invalid criticisms: the methods do not contribute equally, or the minor method is limited (e.g. few participants); the mixed approach "isn't necessary" (when it is beneficial); the methods have different philosophical foundations; the "wrong" method was made dominant in a non-equal design; findings from different methods disagree.

### E288

- Location: Multi-Methodology and Mixed Methods standard, Notes
- Quote: "For multi-method research, it is important to distinguish between using different methods of collecting data (e.g., as part of an inductive case study) and using different research strategies (e.g., complementing an inductive case study with a deductive experiment in a later stage of the research)."
- Key point: Distinguish between using several ways of collecting data within one study (e.g. in an inductive case study) and using different research strategies (e.g. complementing a case study with a deductive experiment in a later phase).

### E289

- Location: Multi-Methodology and Mixed Methods standard, Notes
- Quote: "Some experts on mixed methods use specific terms to refer to core mixed method designs (e.g., Convergent mixed methods, Explanatory sequential mixed methods, Exploratory sequential mixed methods are defined by Creswell & Creswell (2007)"
- Key point: The mixed methods literature has specific names for core designs: convergent, explanatory sequential, and exploratory sequential.

### E290

- Location: General Standard, Extraordinary Attributes
- Quote: "applies two or more data collection or analysis strategies to the same research question" / "approaches the same research question(s) from multiple epistemological perspectives"
- Key point: In the General Standard, applying two or more data collection or analysis strategies to the same research question, and approaching it from multiple epistemological perspectives, are extraordinary attributes, not essential ones.

### E291

- Location: Case Survey standard, definition under the title
- Quote: "A study that aims to generalize results about a complex phenomenon by systematically converting qualitative descriptions available in published case studies into quantitative data and analyzing the converted data"
- Key point: A case survey systematically converts qualitative descriptions in published case studies into quantitative data and analyzes them, aiming to generalize about a complex phenomenon.

### E292

- Location: Case Survey standard, Application
- Quote: "This standard does not apply to studies collecting primary data from a large number of instances of a phenomenon" / "For individual case studies use the **Case Study Standard**. For reviews of other kinds of studies (e.g., experiments) consider the **Systematic Review Standard**. This standard also does not apply to qualitative synthesis (e.g. meta-ethnography, narrative synthesis)."
- Key point: Studies collecting primary data from many instances are not case surveys; individual case studies use the Case Study standard; reviews of experiments and other studies use the Systematic Reviews standard; qualitative synthesis (e.g. meta-ethnography, narrative synthesis) is also outside this standard.

### E293

- Location: Case Survey standard, Essential Attributes and footnote 1
- Quote: "presents step-by-step, systematic, replicable description of the search process for published case studies (not necessarily in peer-reviewed venues)" / "defines clear inclusion and exclusion criteria for cases" / "reports at least two of the variables in the coding scheme"
- Key point: Essential: give a step-by-step, replicable description of the search for published case studies (not necessarily in peer-reviewed venues); define clear inclusion and exclusion criteria for cases, e.g. "reports at least two variables in the coding scheme."

### E294

- Location: Case Survey standard, Essential Attributes
- Quote: "mitigates sampling bias and publication bias, using some (not all) of:"
- Key point: Essential: mitigate sampling and publication bias using some (not all) search methods, the same list as in the Systematic Reviews standard (keyword searches, snowballing, preprints, theses, contacting authors, and so on).

### E295

- Location: Case Survey standard, Essential Attributes and footnote 2
- Quote: "defines a coding scheme to convert qualitative case descriptions into quantitative variables" / "the coding scheme should balance simplicity and information richness" / "EITHER: describes the coding scheme in detail;" / "OR: provides the coding scheme in supplementary materials"
- Key point: Essential: define a coding scheme that converts qualitative case descriptions into quantitative variables, balancing simplicity and information richness; describe it in detail in the paper or in supplementary materials.

### E296

- Location: Case Survey standard, Essential Attributes
- Quote: "clearly explains how missingness in the dataset was managed" / "draws conclusions based on the quantitative variables derived"
- Key point: Essential: clearly explain how missing values in the dataset were handled; base conclusions on the derived quantitative variables.

### E297

- Location: Case Survey standard, Essential Attributes (discussion)
- Quote: "acknowledges generalizability threats; discusses how case studies reviewed may differ from target population"
- Key point: Essential: acknowledge threats to generalizability and discuss how the included cases may differ from the target population.

### E298

- Location: Case Survey standard, Desirable Attributes
- Quote: "provides supplementary materials such as  protocol, search terms, search results, selection process results, coding scheme, examples of coding, decision rules, complete dataset, analysis scripts, descriptions of edge cases" / "explains and justifies the design of the coding scheme"
- Key point: Desirable: release the protocol, search terms, search and selection results, coding scheme, coding examples, decision rules, complete dataset, analysis scripts, and descriptions of edge cases; explain and justify the design of the coding scheme.

### E299

- Location: Case Survey standard, Desirable Attributes and footnote 4
- Quote: "uses 2+ independent analysts; analyzes inter-rater reliability" / "explains how discrepancies among coders were resolved" / "By discussion and agreement, voting, adding tie-breaker, consulting with study authors, etc."
- Key point: Desirable: use two or more independent coders, analyze inter-rater reliability, and explain how disagreements were resolved (discussion and agreement, voting, a tie-breaker, consulting the original authors, etc.).

### E300

- Location: Case Survey standard, Desirable Attributes
- Quote: "describes contacting authors of primary studies for more information, to check coding accuracy, or resolve coding disagreements"
- Key point: Desirable: contact the authors of the primary case studies for more information, to check coding accuracy, or to resolve coding disagreements.

### E301

- Location: Case Survey standard, Desirable Attributes
- Quote: "assesses quality of primary studies using an a priori scheme" / "models study quality as a moderating variable"
- Key point: Desirable: assess the quality of primary studies with an a priori scheme and model study quality as a moderating variable.

### E302

- Location: Case Survey standard, Desirable Attributes and footnote 5
- Quote: "consolidates results using tables, diagrams, or charts; includes PRISMA flow diagram" / "clearly distinguishes evidence-based results from interpretations and speculation"
- Key point: Desirable: consolidate results in tables and diagrams, include a PRISMA flow diagram, and clearly separate evidence-based results from interpretation and speculation.

### E303

- Location: Case Survey standard, Extraordinary Attributes
- Quote: "uses theory to select and sample cases" / "adds data from other sources to the selected cases" / "employs authors of primary studies to conduct the coding or ensure interpretations are correct" / "analyzes if/how studies’ characteristics (e.g., research design, publication venue or date) influence the coding"
- Key point: Extraordinary: use theory to select and sample cases; add data from other sources for the selected cases; involve the original authors in coding or in checking interpretations; analyze whether study characteristics such as design, venue, or publication date affect the coding.

### E304

- Location: Case Survey standard, Antipatterns
- Quote: "including primary studies that are not case studies (e.g., questionnaires or a small amounts of data)" / "include all cases without a critical evaluation of the data available" / "analyze data from cases using qualitative techniques" / "describing each case in isolation rather than synthesizing findings." / "relying on publication venue as a proxy for quality" / "conflating correlation with causation in findings"
- Key point: Antipatterns: including material that is not a case study (e.g. questionnaires, reports with little data); including every case without critically evaluating the available data; analyzing with qualitative methods; describing cases one by one instead of synthesizing; using the venue as a proxy for quality; treating correlation as causation.

### E305

- Location: Case Survey standard, Invalid Criticisms
- Quote: "the studies were not published in peer-reviewed venues" / "the original studies do not employ a common research design" / "the cases are not a random sample of the phenomenon"
- Key point: Invalid criticisms: the primary studies were not published in peer-reviewed venues; they do not share a common research design; the cases are not a random sample of the phenomenon.

### E306

- Location: Meta Science standard, definition under the title
- Quote: "A paper that analyses an issue of research methodology or makes recommendations for conducting research"
- Key point: Methodology and meta-science papers analyze an issue of research methodology or make recommendations for conducting research.

### E307

- Location: Meta Science standard, Application
- Quote: "may or may not include primary or secondary empirical data or analysis." / "may consider philosophical or practical issues" / "may simultaneously be a methodology paper and an empirical study, to which another standard also applies"
- Key point: Such papers may or may not include primary or secondary empirical data; they may address philosophical or practical issues; and a paper can be both a methodology paper and an empirical study, in which case it must also meet the relevant standard.

### E308

- Location: Meta Science standard, Essential Attributes
- Quote: "presents information that is useful for other researchers" / "makes recommendations for future research" / "presents clear, valid arguments supporting recommendations"
- Key point: Essential: present information useful to other researchers, make recommendations for future research, and support them with clear, valid arguments.

### E309

- Location: Meta Science standard, Desirable Attributes
- Quote: "synthesizes related work from reference disciplines" / "goes beyond summarizing methodological guidance from existing works or reference disciplines;" / "develops helpful artifacts (e.g. checklists, templates, tests, tools, sets of criteria)"
- Key point: Desirable: synthesize related work from reference disciplines; go beyond restating existing methodological guidance to offer insights specific to the field; develop helpful artifacts such as checklists, templates, tests, tools, or evaluation criteria.

### E310

- Location: Meta Science standard, Extraordinary Attributes
- Quote: "includes an empirical study (e.g. a systematic literature review) that motivates the analysis of guidance" / "quantitative simulation illustrating methodological issues"
- Key point: Extraordinary: include an empirical study (e.g. a systematic review) that motivates the analysis and recommendations; use quantitative simulation to illustrate methodological issues.

### E311

- Location: Meta Science standard, Antipatterns and footnote 1
- Quote: "overreaching; informal logical fallacies (e.g. straw man argument, appeal to popularity, shifting the burden of proof)" / "citing seminal works is not the “appeal to authority” fallacy" / "discussing an issue without clear conclusions; failing to provide clear guidelines"
- Key point: Antipatterns: overreaching; informal logical fallacies (straw man, appeal to popularity, shifting the burden of proof); discussing an issue without clear conclusions or guidelines. Citing seminal works is not the "appeal to authority" fallacy.

### E312

- Location: Meta Science standard, Antipatterns
- Quote: "attacking individual studies or researchers; hypothetical examples should be used to avoid engendering animosity"
- Key point: Antipattern: attacking individual studies or researchers; use hypothetical examples to avoid engendering animosity.

### E313

- Location: Meta Science standard, Invalid Criticisms
- Quote: "Guidelines are not based on empirical evidence. Empirically testing meta-scientific propositions is typically impractical or impossible. Reviewers should evaluate the face validity, comprehensiveness and usefulness of the guidelines."
- Key point: Invalid criticism: "the guidelines are not based on empirical evidence." Meta-scientific propositions usually cannot be tested empirically; reviewers should judge the guidelines' face validity, comprehensiveness, and usefulness.

### E314

- Location: Meta Science standard, Notes
- Quote: "reviewers of methodology papers must themselves be experts in the methodology, so that they can evaluate the reasonableness of the guidelines" / "reviewers should be more pedantic in critiquing the discussion and guidelines than for an empirical paper"
- Key point: Reviewers of methodology papers must themselves be experts in the methodology, and should critique the discussion and guidelines more pedantically than they would an empirical paper.

### E315

- Location: Meta Science standard, Exemplars
- Quote: "Barbara Kitchenham and Stuart Charters. 2007. Guidelines for performing systematic literature reviews in software engineering." / "Per Runeson and Martin Höst. 2009. Guidelines for conducting and reporting case study research in software engineering."
- Key point: The exemplars listed include Kitchenham & Charters's guidelines for systematic reviews and Runeson & Höst's guidelines for case studies, i.e. methodological guideline papers.

### E316

- Location: Grounded Theory standard, Application
- Quote: "Explores a broad area of investigation without specific, up-front research questions." / "Applies theoretical sampling with iterative and interleaved rounds of data collection and analysis." / "For predominately qualitative inquiries that do not iterate between data collection and analysis or do not use theoretical sampling, consider the **Case Study Standard** or the **Qualitative Survey Standard**."
- Key point: It applies to studies that explore a broad area without specific up-front research questions and use theoretical sampling with interleaved rounds of data collection and analysis; qualitative studies without iteration or theoretical sampling should follow the Case Study or Qualitative Surveys (interview studies) standard.

### E317

- Location: Grounded Theory standard, Essential Attributes (method)
- Quote: "identifies the variant(s) of Grounded Theory used/adapted (Glaser, Strauss/Corbin, Charmaz, etc.)" / "characterizes the data (participants' demographics, types of documents, nature of field notes, ...)" / "explains how the research iterated between data collection (using theoretical sampling) and analysis (using constant comparison)" / "states that and how theoretical saturation was determined" / "explains how key patterns (e.g. categories) were found via GT steps (e.g. selective coding)"
- Key point: You must name the grounded theory variant used; characterize the data; explain how data collection (theoretical sampling) and analysis (constant comparison) were interleaved; say whether and how theoretical saturation was judged; and explain the steps that produced the key categories.

### E318

- Location: Grounded Theory standard, Essential Attributes (results / discussion)
- Quote: "states results in terms of concepts that assign meaning to data ("theoretical coding": do not merely _describe_ the data)" / "grounds most or all important concepts in raw data explicitly (e.g. by providing quotations)" / "discusses the transferability of the theory"
- Key point: State results as concepts that assign meaning to the data, not mere description; ground important concepts explicitly in raw data (e.g. with quotations); discuss the transferability of the theory.

### E319

- Location: Grounded Theory standard, Desirable Attributes
- Quote: "results involve relationships between the concepts ("pushing to theory", not stopping with unconnected themes)" / "explains how memo writing was used to drive the work" / "validates results using member checking, dialogical interviewing, feedback from non-participant practitioners or research audits of coding by advisors or other researchers" / "includes data representing a diverse (rather than homogeneous) spectrum of people or things"
- Key point: Desirable: results include relationships between concepts ("pushing to theory," not stopping at unconnected themes); explain how memo writing drove the work; validate results with member checking, dialogical interviewing, feedback from non-participant practitioners, or audits of coding by advisors or peers; collect data from diverse people or things.

### E320

- Location: Grounded Theory standard, Desirable Attributes
- Quote: "provides supplemental materials such as interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence tables" / "a diagram provides an overview of the main concepts and relationships" / "shows the mapping from categories to lower-level codes and concepts to observations (e.g. as a table)" / "compares results with (or integrates them into) prior theory or related research"
- Key point: Desirable: provide supplementary materials such as interview guides, coding schemes, coding examples, and decision rules; give a diagram of the main concepts and relationships; use tables linking categories to underlying codes and concepts to observations; compare or integrate results with prior theory or related research.

### E321

- Location: Grounded Theory standard, Desirable Attributes
- Quote: "explains how and why study deviates from claimed GT variant and/or how variants were combined" / "reflects on how researcher's biases may have affected their analysis" / "explains the role of literature, especially where an extensive review preceded the GT study"
- Key point: Desirable: explain how and why the study deviates from the claimed variant or how variants were combined; reflect on how researcher bias may have affected the analysis; explain the role of the literature, especially when an extensive review was done beforehand.

### E322

- Location: Grounded Theory standard, Extraordinary Attributes
- Quote: "triangulates with extensive quantitative data (e.g. questionnaires, sentiment analysis)" / "employs a team of researchers and explains their roles"
- Key point: Extraordinary: triangulate with extensive quantitative data (e.g. questionnaires, sentiment analysis); work as a research team and explain each member's role.

### E323

- Location: Grounded Theory standard, Quality Criteria
- Quote: "reviewers should consider common qualitative criteria such as **credibility**, **resonance**, **usefulness** and the degree to which results *extend* our cumulative knowledge." / "Quantitative quality criteria such as internal validity, construct validity, replicability, generalizability and reliability typically do not apply."
- Key point: Grounded theory studies should be judged on credibility, resonance, usefulness, and how far they extend cumulative knowledge; quantitative criteria such as internal validity, replicability, and generalizability generally do not apply.

### E324

- Location: Grounded Theory standard, Examples of Acceptable Deviations
- Quote: "In a study of sexual harassment at a named organization, detailed description of interviewees and direct quotations are omitted to protect participants."
- Key point: Acceptable deviation: to protect participants (e.g. in a study of sexual harassment at a named organization), detailed descriptions of interviewees and direct quotations may be omitted.

### E325

- Location: Grounded Theory standard, Antipatterns
- Quote: "Conducting data collection and data analysis sequentially; applying only analysis techniques of GT." / "Data analysis focusing on counting words, codes, concepts, or categories instead of interpreting." / "Presenting a tutorial on grounded theory instead of explaining how the current study was conducted."
- Key point: Antipatterns: collecting all the data before analyzing and applying only grounded theory's analysis techniques; counting words or codes instead of interpreting; giving a grounded theory tutorial in the paper instead of explaining how this study was done.

### E326

- Location: Grounded Theory standard, Antipatterns
- Quote: "Small, homogeneous samples creating the illusion of convergence and theoretical saturation." / "it is highly unlikely that a full theory can be derived only from interviews with 20 similar people." / "Focusing only on interviews without corroborating statements with other evidence (e.g. documents, observation)."
- Key point: Antipatterns: small, homogeneous samples that create the illusion of convergence and saturation (a full theory is highly unlikely from interviews with 20 similar people); relying only on interviews without checking participants' accounts against documents, observation, or other evidence.

### E327

- Location: Grounded Theory standard, Invalid Criticisms
- Quote: "Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability." / "Lack of replicability or reproducibility; not releasing transcripts" / "Lack of representativeness (e.g. of a study of Turkish programmers, 'how does this generalize to America?')" / "Findings should have been presented as a different set of relationships, hypotheses, or a different theory."
- Key point: Invalid criticisms: lack of quantitative data, causal analysis, objectivity, internal validity, or generalizability; lack of replicability or not releasing transcripts; unrepresentative samples; results "should" have shown different relationships or a different theory.

### E328

- Location: Glossary, Theoretical sampling
- Quote: "choosing which data to collect based on the emerging theory, concepts or categories; typically used in qualitative research, especially Grounded Theory."
- Key point: Theoretical sampling: choosing which data to collect next based on the emerging theory, concepts, or categories.

### E329

- Location: Glossary, Credibility / Resonance / Transferability
- Quote: "the extent to which conclusions are supported by rich, multivocal evidence." / "the extent to which a study's conclusions make sense to (i.e., resonate with) participants" / "the extent to which a study's results could plausibly apply to other sites, people or circumstances."
- Key point: Credibility: conclusions are supported by rich, multivocal evidence. Resonance: conclusions make sense to participants. Transferability: how far results could apply to other places, people, or contexts.

### E330

- Location: Action Research standard, definition under the title
- Quote: "Empirical research that investigates how an intervention, like the introduction of a method or tool, affects a real-life context"
- Key point: Action research is empirical research that investigates how an intervention, such as introducing a method or tool, affects a real-life context.

### E331

- Location: Action Research standard, Application
- Quote: "intervenes in the real-life context (otherwise see the **Case Study Standard**)" / "the change and its observation are an integral part of addressing the research question and contribute to research"
- Key point: Action research intervenes in a real-life context (studies that do not intervene follow the Case Study standard); the change and its observation are integral to answering the research question.

### E332

- Location: Action Research standard, Application
- Quote: "If the intervention primarily alters social phenomena (e.g. the organization's processes, culture, way of working or group dynamics), use this standard. If the intervention is a new technology or technique (e.g. a testing tool, a coding standard, a modeling grammar), especially if it lacks a social dimension, consider the **Engineering Research Standard**." / "If the research involves creating a technology and an organizational intervention with a social dimension, consider both standards."
- Key point: If the intervention mainly alters social phenomena such as processes, culture, or ways of working, use the Action Research standard; if it is a new technology or technique with little social dimension, consider the Engineering Research standard; if both, consult both.

### E333

- Location: Action Research standard, Essential Attributes (method) and footnote 1
- Quote: "justifies the selection of the site(s) that was(were) studied" / "describes the site(s) in rich detail" / "describes the relationship between the researcher and the host organization" / "E.g. project financing, potential conflicts of interest, professional relationship leading to access."
- Key point: You must justify the choice of site(s), describe them in rich detail, and describe the researcher's relationship with the host organization, e.g. project financing, potential conflicts of interest, and the connections that gave access.

### E334

- Location: Action Research standard, Essential Attributes (method) and footnote 2
- Quote: "describes the intervention(s) in detail" / "describes how interventions were determined (e.g. by management, researchers, or a participative/co-determination process)" / "explains how the interventions are evaluated" / "Can include quantitative evaluation in addition to qualitative evaluation."
- Key point: You must describe the intervention in detail, say who determined it (management, researchers, or a participative co-determination process), and explain how it is evaluated; evaluation can add quantitative data to qualitative.

### E335

- Location: Action Research standard, Essential Attributes (method) and footnotes 3 and 4
- Quote: "describes the longitudinal dimension of the research design (including the length of the study)" / "describes the interactions between researcher(s) and host organization(s)" / "i.e. who intervened and with which part of the organization?" / "explains research cycles or phases, if any, and their relationship to the intervention(s)" / "Action research projects are structured in interventions often described as action research cycles, which are often structured in distinct phases. It is a flexible methodology, where subsequent cycles are based on their predecessors."
- Key point: You must describe the study's longitudinal dimension (including its length), the interactions between researchers and the organization (who intervened, with which part of it), and how research cycles or phases relate to the interventions. Action research is often organized in cycles, each with several phases, each cycle building on the previous one.

### E336

- Location: Action Research standard, Essential Attributes (results / discussion)
- Quote: "presents a clear chain of evidence from observations to findings" / "reports participant or stakeholder reactions to interventions" / "reports lessons learned by the organization" / "researchers reflect on their own possible biases"
- Key point: You must present a clear chain of evidence from observations to findings, report participant and stakeholder reactions to the interventions, report lessons learned by the organization, and reflect on your own possible biases as a researcher.

### E337

- Location: Action Research standard, Desirable Attributes
- Quote: "provides supplemental materials such as interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence tables" / "uses direct quotations extensively" / "validates results using member checking, dialogical interviewing, feedback from non-participant practitioners or research audits of coding by advisors or other researchers" / "findings plausibly transferable to other contexts" / "triangulation across quantitative and qualitative data"
- Key point: Desirable: provide supplementary materials; use direct quotations extensively; validate results through member checking, feedback from non-participant practitioners, or audits of coding by advisors or peers; findings plausibly transferable to other contexts; triangulate between quantitative and qualitative data.

### E338

- Location: Action Research standard, Extraordinary Attributes
- Quote: "research team with triangulation across researchers (to mitigate researcher bias)"
- Key point: Extraordinary: a research team with triangulation across researchers to mitigate researcher bias.

### E339

- Location: Action Research standard, General Quality Criteria
- Quote: "Example criteria include reflexivity, credibility, resonance, usefulness and transferability" / "Positivist quality criteria such as internal validity, construct validity, generalizability and reliability typically do not apply."
- Key point: Criteria include reflexivity, credibility, resonance, usefulness, and transferability; positivist criteria such as internal validity and generalizability typically do not apply.

### E340

- Location: Action Research standard, Examples of Acceptable Deviations
- Quote: "In a study of deviations from organizational standards, detailed description of circumstances and direct quotations are omitted to protect participants." / "The article reports a negative outcome of an intervention and e.g. investigates why a certain method was not applicable."
- Key point: Acceptable deviations: omitting detailed circumstances and direct quotations to protect participants; reporting a negative outcome of an intervention, e.g. analyzing why a method did not fit.

### E341

- Location: Action Research standard, Antipatterns
- Quote: "Forcing interventions that are not acceptable to participants or the host organization." / "Losing professional distance and impartiality; getting too involved with the community under study." / "Over-selling a tool or method without regard for participants' problems, practices or values." / "Avoiding systematic evaluation; downplaying problems; simply reporting participants views of the intervention."
- Key point: Antipatterns: forcing interventions that participants or the organization cannot accept; losing professional distance and impartiality by getting too involved with the community; over-selling a tool or method regardless of participants' problems, practices, and values; avoiding systematic evaluation, downplaying problems, or reporting only participants' opinions of the intervention.

### E342

- Location: Action Research standard, Invalid Criticisms
- Quote: "The findings and insights are not valid because the research intervened in the context." / "the whole point of action research is to introduce a change and observe how participants react." / "Systematic observation and reflection should not be dismissed as consultancy or experience reports. Inversely, consultancy or experiences should not be falsely presented as action research."
- Key point: Invalid criticism: "the findings are invalid because the researchers intervened," when the whole point of action research is to introduce a change and observe how participants react. Systematic observation and reflection should not be dismissed as consulting or experience reports; conversely, consulting or experience reports should not pose as action research.

### E343

- Location: Action Research standard, Invalid Criticisms
- Quote: "Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability." / "Sample not representative; lack of generalizability; generalizing from one organization." / "Lack of replicability or reproducibility; not releasing transcripts." / "Lack of control group or experimental protocols. An action research study is not an experiment."
- Key point: Invalid criticisms: lack of quantitative data, causal analysis, or generalizability; an unrepresentative sample or generalizing from one organization; lack of replicability or unreleased transcripts; no control group (action research is not an experiment).

### E344

- Location: Glossary, Reflexivity / Transferability
- Quote: "the extent to which authors reflect on their potential biases and interactions with the team, organization or community, especially possible negative impacts on some participants or stakeholders." / "the extent to which a study's results could plausibly apply to other sites, people or circumstances."
- Key point: Reflexivity: how far the authors reflect on their potential biases and their interactions with the team or organization, especially possible negative impacts on some participants. Transferability: how far the results could apply to other places, people, or contexts.

### E345

- Location: Qualitative Surveys standard, Application
- Quote: "Researcher(s) have synchronous conversations with one participant at a time" / "Researchers ask, and participants answer, open-ended questions" / "Participants' answers are recorded in some way" / "Researchers apply some kind of qualitative data analysis to participants' answers"
- Key point: An interview study meets four conditions: researchers have synchronous one-on-one conversations with participants; researchers ask open-ended questions that participants answer; answers are recorded in some way; and some qualitative analysis is applied to them.

### E346

- Location: Qualitative Surveys standard, Application
- Quote: "If researchers iterated between data collection and analysis, consider the **Grounded Theory Standard**. If respondents are all from the same organization, consider the **Case Study Standard**."
- Key point: If data collection and analysis iterated, consider the Grounded Theory standard; if all respondents are from the same organization, consider the Case Study standard.

### E347

- Location: Qualitative Surveys standard, Notes
- Quote: "A qualitative survey generally has more interviews than a case study that triangulates across different kinds of data."
- Key point: An interview study generally has more interviews than a case study, which triangulates across different kinds of data.

### E348

- Location: Qualitative Surveys standard, General Quality Criteria
- Quote: "An interview study should address appropriate qualitative quality criteria such as:" [...] "Quantitative quality criteria such as internal validity, construct validity, generalizability and reliability typically do not apply."
- Key point: An interview study should meet appropriate qualitative criteria (credibility, resonance, usefulness, transferability); quantitative criteria such as internal validity, construct validity, generalizability, and reliability typically do not apply.

### E349

- Location: Glossary, Credibility / Resonance / Usefulness / Transferability
- Quote: "**Credibility**: the extent to which conclusions are supported by rich, multivocal evidence." / "**Resonance**: the extent to which a study’s conclusions make sense to (i.e., resonate with) participants" / "**Usefulness**: the extent to which a study provides actionable recommendations to researchers, practitioners **OR** educators." / "**Transferability**: the extent to which a study's results could plausibly apply to other sites, people or circumstances."
- Key point: Credibility = conclusions supported by rich, multivocal evidence; resonance = conclusions make sense to participants; usefulness = actionable recommendations for researchers, practitioners, or educators; transferability = results could plausibly apply to other settings, people, or situations.

### E350

- Location: Glossary, Reflexivity
- Quote: "**Reflexivity**: the extent to which authors reflect on their potential biases and interactions with the team, organization or community, especially possible negative impacts on some participants or stakeholders."
- Key point: Reflexivity = the authors reflect on their potential biases and their interactions with the team, organization, or community, especially possible negative impacts on some participants.

### E351

- Location: Qualitative Surveys standard, Essential (method)
- Quote: "explains how interviewees were selected" / "describes interviewees (e.g. demographics, work roles)" / "describes interviewer(s) (e.g. experience, perspective)"
- Key point: You must explain how interviewees were selected, describe them (e.g. demographics, work roles), and describe the interviewers (e.g. experience, perspective).

### E352

- Location: Qualitative Surveys standard, Essential (results)
- Quote: "presents clear chain of evidence from interviewee quotations to findings (e.g. proposed concepts)" / "clearly answers the research question(s)" / "provides evidence of saturation; explains how saturation was achieved"
- Key point: You must present a clear chain of evidence from interviewee quotations to findings, clearly answer the research questions, and provide evidence of saturation and explain how it was achieved.

### E353

- Location: Qualitative Surveys standard, Essential (discussion)
- Quote: "researchers reflect on their own possible biases" / "identifies key issues under consideration"
- Key point: Researchers must reflect on their own possible biases and identify the key issues under consideration.

### E354

- Location: Qualitative Surveys standard, Desirable
- Quote: "provides supplemental materials including interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence table(s)" / "describes questions asked in data collection: content of central questions, form of questions (e.g. open vs. closed)"
- Key point: Desirable: provide supplementary materials (interview guides, coding schemes, coding examples, decision rules, extended chain-of-evidence tables); describe the questions asked, including the content and form (open or closed) of the central questions.

### E355

- Location: Qualitative Surveys standard, Desirable
- Quote: "includes highly diverse participants" / "describes the relationships and interactions between researchers and participants relevant to the research process"
- Key point: Desirable: highly diverse participants; describe the relationships and interactions between researchers and participants relevant to the research process.

### E356

- Location: Qualitative Surveys standard, Desirable
- Quote: "uses direct quotations extensively to support key points" / "identifies data recording methods (audio/visual), field notes or transcription processes used"
- Key point: Desirable: use direct quotations extensively to support key points; state how data were recorded (audio/video), and the field notes or transcription processes used.

### E357

- Location: Qualitative Surveys standard, Desirable
- Quote: "EITHER: evaluates an a priori theory (or model, framework, taxonomy, etc.) using deductive coding with an a priori coding scheme based on the prior theory" / "OR: synthesizes results into a new, mature, fully-developed and clearly articulated theory (or model, etc.) using some form of inductive coding (coding scheme generated from data)"
- Key point: Desirable, one of two: evaluate an a priori theory with deductive coding using a coding scheme based on it; or use inductive coding (the scheme emerges from the data) and synthesize the results into a new, mature, fully developed theory or model.

### E358

- Location: Qualitative Surveys standard, Desirable
- Quote: "validates results using member checking, dialogical interviewing, feedback from non-participant practitioners or research audits of coding by advisors or other researchers"
- Key point: Desirable: validate results through member checking, dialogical interviewing, feedback from non-participant practitioners, or audits of coding by advisors or other researchers.

### E359

- Location: Qualitative Surveys standard, Desirable
- Quote: "discusses transferability; findings plausibly transferable to different contexts" / "compares results with (or integrates them into) prior theory or related research" / "reflects on any alternative explanations of the findings"
- Key point: Desirable: discuss transferability; compare results with prior theory or related research; reflect on alternative explanations of the findings.

### E360

- Location: Qualitative Surveys standard, Desirable
- Quote: "describes any incentives or compensation, and provides assurance of relevant ethical processes of data collection and consent process as relevant"
- Key point: Desirable: describe any incentives or compensation, and the ethical processes for data collection and consent.

### E361

- Location: Qualitative Surveys standard, Extraordinary
- Quote: "employs multiple methods of data analysis (e.g. open coding vs. process coding; manual coding vs. automated sentiment analysis) with method-triangulation" / "employs longitudinal design (i.e. each interviewee participates multiple times) and analysis" / "employs probabilistic sampling strategy; statistical analysis of response bias" / "uses multiple coders and analyzes inter-coder reliability"
- Key point: Extraordinary: multiple analysis methods with method triangulation; a longitudinal design (each person interviewed several times); probability sampling with statistical analysis of response bias; multiple coders with analysis of inter-rater reliability.

### E362

- Location: Qualitative Surveys standard, Antipatterns
- Quote: "Interviewing a small number of similar people, creating the illusion of convergence and saturation" / "Mis-presenting a qualitative survey as grounded theory or a case study."
- Key point: Antipatterns: interviewing a small number of similar people, creating the illusion of convergence and saturation; presenting an interview study as grounded theory or a case study.

### E363

- Location: Qualitative Surveys standard, Invalid Criticisms
- Quote: "Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability." / "Lack of replicability or reproducibility; not releasing transcripts." / "Lack of probability sampling, statistical generalizability or representativeness unless representative sampling was an explicit goal of the study."
- Key point: Invalid criticisms: lack of quantitative data, causal analysis, objectivity, internal validity, reliability, or generalizability; lack of replicability or unreleased transcripts; lack of probability sampling, statistical generalizability, or representativeness (unless the study explicitly aims at representativeness).

### E364

- Location: Qualitative Surveys standard, Examples of Acceptable Deviations
- Quote: "In a study of deaf software developers, the interviews are conducted via text messages." / "In a study of sexual harassment at named organizations, detailed description of interviewees and direct quotations are omitted to protect participants."
- Key point: Acceptable deviations: interviewing deaf developers via text messages; omitting detailed interviewee descriptions and direct quotations to protect participants in a study of sexual harassment at named organizations.

### E365

- Location: Inter-Rater Reliability and Agreement supplement, Application and Philosophy
- Quote: "Does not apply to constructivist or intepretivist qualitative data analysis." / "the idea that multiple raters should agree is consistent with realist, positivist, and falsificationist philosophical positions; from an interpretivist or constructivist perspective, different analysts are expected to have different views, so IRR and IRA are irrelevant."
- Key point: The inter-rater supplement does not apply to constructivist or interpretivist qualitative analysis; the idea that multiple raters should agree fits realist and positivist positions, whereas from an interpretivist or constructivist view different analysts naturally see things differently and reliability and agreement measures are irrelevant.

### E366

- Location: Inter-Rater Reliability and Agreement supplement, Practicality
- Quote: "multiple raters applying an _a priori_, deductive coding scheme to some artifacts is more practical than multiple raters inductively coding 2000 pages of interview transcripts."
- Key point: Having multiple raters apply an a priori, deductive coding scheme to artifacts is more practical than having them inductively code 2000 pages of interview transcripts.

### E367

- Location: Inter-Rater Reliability and Agreement supplement, Invalid Criticisms and Notes
- Quote: "Criticizing use of a single rater where multiple raters would be impractical or inconsistent with the study's underlying philosophy.." / "IRR/IRA analysis not only indicates reliability and objectivity (in positivist research) but also improves reflexivity (in anti-positivist research)."
- Key point: Criticizing a single rater is invalid when multiple raters would be impractical or inconsistent with the study's philosophy; agreement analysis indicates reliability and objectivity in positivist research and can also improve reflexivity in anti-positivist research.

### E368

- Location: Inter-Rater Reliability and Agreement supplement, Antipatterns
- Quote: "Calculating multiple IRR/IRA measures and reporting only the most favourable (p-hacking)" / "Pretending that an obviously positivist study adopts an idealist ontology to avoid employing multiple raters"
- Key point: Antipatterns: calculating several agreement measures and reporting only the most favorable; pretending an obviously positivist study takes an interpretivist stance to avoid using multiple raters.

### E369

- Location: Ethics (Studies with Human Participants) supplement, Essential
- Quote: "explains the compensation (if any) offered for participation and how coercion was mitigated" / "explains how participants' free, individual, informed consent to participate was obtained"
- Key point: You must explain any compensation and how coercion was mitigated, and how participants' free, individual, informed consent was obtained.

### E370

- Location: Glossary, Gatekeeper
- Quote: "Gatekeepers may influence individual’s participation decisions (e.g., employers may coerce employees to participate)"
- Key point: Gatekeepers (people or organizations that control researchers' access to participants) may influence individuals' decisions to take part; e.g. employers may coerce employees to participate.

### E371

- Location: Sampling supplement, Antipatterns and Invalid Criticisms
- Quote: "qualitative research with too little data for plausible saturation" / "for qualitative research, claiming that the sample size is too small without considering how the items were selected (e.g. theoretical sampling) or the authors' argument for saturation."
- Key point: Antipattern: qualitative research with too little data for plausible saturation. Invalid criticism: calling a qualitative sample too small without considering how items were selected (e.g. theoretical sampling) or the authors' argument for saturation.

### E372

- Location: Sampling supplement, Desirable
- Quote: "exploratory research: using purposive rather than convenience sampling for unit of analysis" / "theory building: using theoretical rather than convenience sampling"
- Key point: Exploratory research should use purposive rather than convenience sampling; theory building should use theoretical rather than convenience sampling.

### E373

- Location: General Standard, Invalid Criticisms
- Quote: "Cross-paradigmatic criticism (e.g. attacking an interpretivist study for not conforming to positivist norms)."
- Key point: Cross-paradigmatic criticism (e.g. attacking an interpretivist study for not conforming to positivist norms) is an invalid criticism.

### E374

- Location: Optimization Studies standard, definition under the title and Application
- Quote: "Research studies that focus on the formulation of software engineering problems as search problems, and apply optimization techniques to solve such problems" / "Formulates a software engineering task as an optimization problem, with one or more specified fitness functions used to judge success in this task."
- Key point: Definition of an optimization study: formulating a software engineering problem as a search problem and solving it with optimization techniques; it applies to studies that frame a task as an optimization problem and judge success with one or more fitness functions.

### E375

- Location: Optimization Studies standard, footnote 3
- Quote: "A "fitness function", or "objective function", is a numerical scoring function used to indicate the quality of a solution to a defined problem. Optimization approaches attempt to maximize or minimize such functions, depending on whether lower or higher scores indicate success."
- Key point: A fitness function (or objective function) is a numerical scoring function that indicates how good a solution is; optimization approaches try to maximize or minimize it.

### E376

- Location: Optimization Studies standard, footnote 1
- Quote: "Note that there are many such optimization techniques (metaheuristic; numerical optimizers; constraint solving theorem provers SAT,SMT,CSP; and other), some of which are stochastic."
- Key point: There are many optimization techniques, such as metaheuristics, numerical optimizers, and constraint solvers, some of which are stochastic.

### E377

- Location: Optimization Studies standard, Essential (intro) and footnote 4
- Quote: "explains why the problem cannot be optimized manually or by brute force within a reasonable timeframe" / "E.g., if the cross-product of the space of options is very large or if the time required to perform a task manually is very slow."
- Key point: Essential: explain why the problem cannot be optimized manually or by brute force within a reasonable time, e.g. because the space of options is very large or doing it manually is too slow.

### E378

- Location: Optimization Studies standard, Essential (method)
- Quote: "describes the search space (e.g., constraints, independent variables choices)" / "uses realistic and limited simplifications and constraints for the optimization problem; simplifications and constraints do not reduce the search to one where all solutions could be enumerated through brute force"
- Key point: Essential: describe the search space (constraints, choices for independent variables); simplifications and constraints must be realistic and limited, and must not shrink the problem until all solutions can be enumerated.

### E379

- Location: Optimization Studies standard, Essential (method) and footnote 6
- Quote: "justifies the choice of algorithm underlying the approach" / "While one rarely knows the *best* approach for a new problem, one should at least consider the algorithms applied to address similar problems and make an informed judgement."
- Key point: Essential: justify the choice of algorithm. You rarely know the best approach for a new problem, but you should at least consider algorithms used for similar problems and make an informed decision.

### E380

- Location: Optimization Studies standard, Essential (method) and footnote 7
- Quote: "compares approaches to a justified and appropriate baseline" / "If the approach addresses a problem never tackled before, then it should be compared - at least - to random search. Otherwise, compare the proposed approach to the existing state of the art."
- Key point: Essential: compare against a justified, appropriate baseline. For a problem never tackled before, compare at least with random search; otherwise compare with the state of the art.

### E381

- Location: Optimization Studies standard, Essential (method) and footnotes 8 and 9
- Quote: "explictly defines the solution formulation, including a description of what a solution represents, how it is represented, and how it is manipulated" / "explicitly defines all fitness functions, including the type of goals that are optimized and the equations for calculating fitness values"
- Key point: Essential: explicitly define the solution formulation: what a solution represents (e.g. a test suite), how it is represented (e.g. a tree or vector), and how it is manipulated; explicitly define all fitness functions, including the optimization goal and the formula.

### E382

- Location: Optimization Studies standard, Essential (method) and footnote 10
- Quote: "explicitly defines evaluated approaches, including the techniques, specific heuristics, and the parameters and their values" / "Example techniques - Simulated Annealing, Genetic Algorithm. Example heuristic - single-point crossover. Example parameters - crossover and mutation rates."
- Key point: Essential: explicitly define the evaluated approaches: techniques (e.g. simulated annealing, genetic algorithm), specific heuristics (e.g. single-point crossover), and parameters with their values (e.g. crossover and mutation rates).

### E383

- Location: Optimization Studies standard, Essential (method)
- Quote: "EITHER: clearly describes (and follows) a sound process to collect and prepare the datasets used to run and to evaluate the optimization approach" / "EITHER: makes data publicly available"
- Key point: Essential: describe how the datasets used to run and evaluate the approach were collected and prepared (citing and describing any taken from prior work); make the data public, or explain why it cannot be.

### E384

- Location: Optimization Studies standard, Essential (method) and footnotes 12 and 13
- Quote: "identifies and explains all possible sources of stochasticity" / "stochasticity may arise from the use of randomized algorithms, from the use of a fitness function that measures a random variable from the environment (e.g., a fitness function based on execution time may return different results across different executions), from the use of data sampling or cross-validation approaches." / "EITHER: executes stochastic approaches or elements multiple times"
- Key point: Essential: identify and explain all sources of stochasticity, such as randomized algorithms, fitness functions that measure a random variable from the environment (e.g. execution time), and data sampling or cross-validation; run stochastic approaches multiple times, or explain why that is impossible (e.g. too slow, or humans in the loop).

### E385

- Location: Optimization Studies standard, Desirable
- Quote: "explains in detail how subjects or datasets were collected/chosen to mitigate selection bias and improve the generalization of findings" / "describes the main features of the subjects used to run and evaluate the optimization approach(es) and discuss what characterizes the different instances in terms of "hardness""
- Key point: Desirable: explain in detail how subjects (problem instances) were chosen to mitigate selection bias and improve generalizability; describe their main features and discuss how their "difficulty" differs.

### E386

- Location: Optimization Studies standard, Desirable
- Quote: "justifies the use of synthetic data (if any); explain why real-world data cannot be used; discusses the extent to which the proposed approach and the findings can apply to the real world" / "selects a realistic option space for formulating a solution; any values set for attributes should reflect one that might be chosen in a "real-world" solution, and not generated from an arbitrary distribution"
- Key point: Desirable: justify any use of synthetic data and discuss how far it applies to the real world; choose a realistic option space, with attribute values that could occur in reality rather than drawn from arbitrary distributions.

### E387

- Location: Optimization Studies standard, Desirable
- Quote: "justifies the parameter values used when executing the evaluated approaches (and note that experiments trying a wide range of different parameter values would be extraordinary, see below)"
- Key point: Desirable: justify the parameter values used to run each approach; experiments trying a wide range of parameter values count as extraordinary.

### E388

- Location: Optimization Studies standard, Desirable
- Quote: "compares distributions (rather than means) of results using appropriate statistics" / "clearly distinguishes evidence-based results from interpretations and speculation"
- Key point: Desirable: compare distributions of results (not just means) with appropriate statistics; separate evidence-based results from interpretation and speculation.

### E389

- Location: Optimization Studies standard, Desirable and footnote 14
- Quote: "provides a replication package that conforms to SIGSOFT standards for artifacts" / "Including, for example, source code (of approach, solution representation, and fitness calculations), datasets used as experiment input, and collected experiment data (e.g., output logs, generated solutions)."
- Key point: Desirable: provide a replication package, including source code for the approach, solution representation, and fitness calculations, the experiment input data, and the collected experimental data (output logs, generated solutions).

### E390

- Location: Optimization Studies standard, Extraordinary
- Quote: "analyzes different parameter choices to the algorithm, indicating how the final parameters were selected" / "analyzes the fitness landscape for one or more of the chosen fitness functions"
- Key point: Extraordinary: analyze different parameter choices for the algorithm and explain how the final parameters were selected; analyze the fitness landscape (how fitness values are distributed across the solution space) of the fitness functions.

### E391

- Location: Optimization Studies standard, Examples of Acceptable Deviations
- Quote: "The number of trials can be constrained by available time or experimental resources (e.g. where experiments are time-consuming to repeat or have human elements). In such cases, multiple trials are still ideal, but a limited number of trials can be justified as long as the limitations are disclosed and the possible effects of stochasticity are discussed."
- Key point: Acceptable deviation: with limited time or resources, fewer trials are acceptable, but the limitation must be disclosed and the possible effects of stochasticity discussed.

### E392

- Location: Optimization Studies standard, Antipatterns
- Quote: "Reporting significance tests (e.g., Mann-Whitney Wilcoxon test) without effect size tests" / "Conducting multiple trials but failing to disclose or discuss the variation between trials; for instance reporting a measure of central (e.g. median) without any indication of variance (e.g., a boxplot)."
- Key point: Antipatterns: reporting significance tests without effect sizes; running multiple trials but not disclosing or discussing the variation between them, e.g. reporting only a median with no box plot or other indication of variance.

### E393

- Location: Optimization Studies standard, Invalid Criticisms
- Quote: "The paper just uses older algorithms with no reference to recent work. Using  older (and widely understood algorithms) may be valid when they are used, e.g., (1) as part of a larger set that compares many approaches; e.g. (2) to offer a “straw man” method that defines the “floor” of the performance (that everything else needs to beat); or (3), as a workbench within which one thing is changed (e.g., the fitness function) but everything else remains constant."
- Key point: Invalid criticism: "the paper only uses older algorithms." Older algorithms can legitimately serve as one of many compared approaches, as a performance floor, or as a testbed where only one thing (e.g. the fitness function) changes.

### E394

- Location: Optimization Studies standard, Invalid Criticisms
- Quote: "That an approach is not benchmarked against an inappropriate or unavailable baseline." / "That a multi-objective approach is not compared to a single-objective approach by evaluating each objective separately." / "That one or very few subjects are used, as long as the paper offers a reasonable justification for why this was the case."
- Key point: Invalid criticisms: not comparing with an inappropriate or unavailable baseline; not comparing a multi-objective approach with single-objective optimization of each objective separately (the point of multi-objective problems is the trade-off between objectives); few subjects when this is reasonably justified.

### E395

- Location: Optimization Studies standard, Invalid Criticisms
- Quote: "It is more important to consider the Pareto frontiers and quality indicators."
- Key point: For multi-objective optimization, what matters more is the Pareto front (the set of solutions where no objective can improve without another getting worse) and the related quality indicators.

### E396

- Location: Optimization Studies standard, Notes
- Quote: "Regarding the difference between "significance" and "effect size" tests: "Significance" checks if distributions can be distinguished from each other while "Effect size" tests are required to check if the difference between distributions is "interesting" (and not just a trivially "small effect")."
- Key point: A significance test asks whether two distributions can be told apart; an effect size asks whether the difference is large enough to matter rather than trivially small.

### E397

- Location: Simulation standard, definition under the title
- Quote: "A study that involves developing and using a mathematical model that imitates a real-world system's behavior, which often entails problem understanding, data collection, model development, verification, validation, design of experiments, data analysis, and implementation of results."
- Key point: Definition of a simulation study: developing and using a mathematical model that imitates a real-world system's behavior, often involving problem understanding, data collection, model development, verification, validation, experimental design, data analysis, and implementation of results.

### E398

- Location: Simulation standard, Application
- Quote: "Use this standard for _in silico_ simulations, i.e., studies representing everything using computational models. For _in virtuo_ simulations, i.e., human participants manipulating simulation models, use the **Experiments (with human participants) Standard**. For simulations used to assess a new or improved technological artifact, also consider the **Engineering Research** standard."
- Key point: The standard covers in silico simulations, where everything is a computational model; in virtuo simulations, with human participants manipulating the model, follow the Experiments standard; when simulation is used to evaluate a new artifact, also consult the Engineering Research standard.

### E399

- Location: Simulation standard, Essential (intro)
- Quote: "justifies that simulation is a suitable method for investigating the problem (or research question, etc.)"
- Key point: Essential: justify that simulation is a suitable method for the problem.

### E400

- Location: Simulation standard, Essential (method) and footnote 1
- Quote: "describes the simulation model (conceptual, implementation, or hybrid abstraction levels), including input parameters and response variables" / "describes the underlying simulation approach" / "e.g. discrete-event simulation, system dynamics, agent-based simulation" / "describes simulation packages or tools used to develop and run the simulation model, including version numbers, and computational environments"
- Key point: Essential: describe the simulation model (at the conceptual, implementation, or hybrid level), including input parameters and response variables; name the simulation approach (e.g. discrete-event simulation, system dynamics, agent-based simulation); give the simulation package or tool version and the computing environment.

### E401

- Location: Simulation standard, Essential (method)
- Quote: "describes the data used for model calibration, the calibration procedures, and contextual information"
- Key point: Essential: describe the data used to calibrate the model, the calibration procedure, and contextual information about the data.

### E402

- Location: Simulation standard, Essential (method) and footnote 2
- Quote: "describes how the simulation model was verified and validated at different abstraction levels" / "Some verification and validation procedures may be applied to the model at the conceptual level (e.g., validating variables and relationships) down to an implementation level (e.g., using tests, reproducing reference behaviors, or performing simulated experiments)."
- Key point: Essential: describe how the model was verified and validated at different abstraction levels, from the conceptual level (checking variables and relationships) to the implementation level (testing, reproducing reference behaviors, running simulation experiments).

### E403

- Location: Simulation standard, Essential (method)
- Quote: "describes the study protocol, including independent variables, scenarios, number of runs per scenario (in case of using stochastic simulation), and steady-state or terminating conditions"
- Key point: Essential: describe the study protocol: independent variables, scenarios, number of runs per scenario (for stochastic simulation), and steady-state or terminating conditions.

### E404

- Location: Simulation standard, Essential (method) and footnote 3
- Quote: "analyzes validity threats considering the supporting data and the simulation model" / "Simulation studies are prone to several validity threats, including non-representative simulation scenarios, insufficient verification and validation, using different datasets (contexts) for model calibration and experimentation, and others" / "clearly explicates the assumptions of the simulation model"
- Key point: Essential: analyze validity threats with respect to both the supporting data and the model, e.g. unrepresentative scenarios, insufficient verification and validation, or calibration and experiments using data from different contexts; state the model's assumptions explicitly.

### E405

- Location: Simulation standard, Desirable
- Quote: "provides supplementary materials including the raw data (for real data) or generation mechanism (for synthetic data) used for model calibration, all simulation models and source code, analysis scripts"
- Key point: Desirable: provide supplementary materials: the raw calibration data (or the generation mechanism for synthetic data), all simulation models and source code, and analysis scripts.

### E406

- Location: Simulation standard, Desirable and footnote 4
- Quote: "characterizes reference behaviors for the definition of simulation scenarios with representative and known values or probability distributions for input parameters" / "Reference behaviors represent a real-world model (often based on actual measurement of a system or process), which is characterized by data distribution or series of model variables. Usually, these models are used for validating simulation outcomes."
- Key point: Desirable: characterize "reference behaviors" with representative, known values or probability distributions and use them to define scenarios. Reference behaviors usually come from measurements of the real system or process and are often used to validate simulation results.

### E407

- Location: Simulation standard, Desirable
- Quote: "separates conceptual and implementation levels of the simulation model" / "reports sensitivity analysis for input parameters or factors" / "clearly distinguishes evidence-based results from interpretations and speculation"
- Key point: Desirable: separate the conceptual and implementation levels of the model; report sensitivity analysis for input parameters or factors; separate evidence-based results from interpretation and speculation.

### E408

- Location: Simulation standard, Extraordinary and footnote 6
- Quote: "describes how stakeholders were involved in developing and validating the simulation model" / "All of these stakeholders could, for example, be involved in checking the plausibility of the model output (face validity check)."
- Key point: Extraordinary: describe how stakeholders (data providers, domain experts, model users) were involved in developing and validating the model, e.g. checking that its output is plausible (face validity checks).

### E409

- Location: Simulation standard, Antipatterns and footnote 8
- Quote: "Overfitting the simulation model to reproduce a reference behavior." / "For instance, implementing a specific model capable of only producing desired outcomes." / "Using a single run instead of multiple runs to experiment with stochastic models."
- Key point: Antipatterns: overfitting the model to reproduce a reference behavior, e.g. building a model that can only produce the desired outcomes; running a stochastic model only once.

### E410

- Location: Simulation standard, Antipatterns and footnote 9
- Quote: "Use of non-standard experimental designs without justification." / "Houston et al. (2001) discusses some usual experimental design for software process simulation, such as (fractional) factorial designs."
- Key point: Antipattern: using non-standard experimental designs without justification. Common designs include (fractional) factorial designs.

### E411

- Location: Simulation standard, Examples of Acceptable Deviations
- Quote: "If insufficient data is available (or too costly to collect) to calibrate the model, assumptions can be used to implement parts of the model. These assumptions, however, must be explained and justified."
- Key point: Acceptable deviation: when calibration data are insufficient or too costly, assumptions can stand in for parts of the model, but they must be explained and justified.

### E412

- Location: Simulation standard, Invalid Criticisms
- Quote: "The mere presence of assumptions in the model is not a valid basis for criticism _as long as_ the assumptions are documented and justified, and their implications for the validity of the simulation are sufficiently addressed. All models make assumptions."
- Key point: Invalid criticism: "the model contains assumptions." Every model does; it is enough that they are documented, justified, and their implications for validity are discussed.

### E413

- Location: Simulation standard, Invalid Criticisms
- Quote: "Claiming that the model is too abstact without explaining why the level of abstraction is inadequate for the purposes of the study." / "Claiming that the study is invalid because it uses generated data, secondary data or approximations based on expert opinion, _when no appropriate primary data is available_."
- Key point: Invalid criticisms: calling the model "too abstract" without explaining why that level of abstraction is inadequate; dismissing the study for using generated data, secondary data, or expert estimates when suitable primary data are not available.

### E414

- Location: Case Study and Ethnography, definition under the title
- Quote: "An empirical inquiry that investigates a contemporary phenomenon (the "case") in depth and within its real-world context, especially when the boundaries between phenomenon and context are unclear"
- Key point: Definition of a case study (quoting Yin 2017): an in-depth inquiry into a contemporary phenomenon (the "case") in its real-world context, especially when the boundary between phenomenon and context is unclear.

### E415

- Location: Case Study and Ethnography, Application
- Quote: "Presents a detailed account of a specific instance of a *phenomenon* at a *site*. [...] The site can be a community, an organization, a team, a person, a process, an internet platform, etc."
- Key point: A case study gives a detailed account of a specific instance of a phenomenon at a site; the site can be a community, organization, team, person, process, internet platform, and so on.

### E416

- Location: Case Study and Ethnography, Application
- Quote: "Is not an experience report (cf. Perry et al. 2004) or a series of shallow inquiries at many different sites."
- Key point: An experience report is not a case study, and neither is a series of shallow inquiries at many different sites.

### E417

- Location: Case Study and Ethnography, Application
- Quote: "A case study can be brief (e.g. a week of observation) or longitudinal (if observation exceeds the natural rhythm of the site; e.g., observing a product over many releases). For our purposes, *case study subsumes ethnography*."
- Key point: A case study can be brief (e.g. a week of observation) or longitudinal; this standard treats ethnography as a kind of case study.

### E418

- Location: Case Study and Ethnography, Application
- Quote: "If data collection and analysis are interleaved, consider the **Grounded Theory** Standard. If the study mentions action research, or intervenes in the context, consider the **Action Research** Standard."
- Key point: If data collection and analysis are interleaved, consult the Grounded Theory standard; if the researchers intervene at the site, consult the Action Research standard.

### E419

- Location: Case Study and Ethnography, Essential Attributes
- Quote: "justifies the selection of the case(s) or site(s) that was(were) studied" / "describes the site(s) in rich detail" / "the site is a real (physical or virtual) place, not a toy example or imaginary world"
- Key point: Essential: justify the choice of case or site; describe the site in rich detail; the site must be real (physical or virtual), not a toy example or imaginary world.

### E420

- Location: Case Study and Ethnography, Essential Attributes
- Quote: "reports the type of case study" / "describes data sources (e.g. participants' demographics and work roles)" / "defines unit(s) of analysis or observation"
- Key point: Essential: report the type of case study; describe data sources (e.g. participants' demographics and work roles); define the units of analysis or observation.

### E421

- Location: Case Study and Ethnography, Essential Attributes
- Quote: "presents a clear chain of evidence from observations to findings"
- Key point: Essential: present a clear chain of evidence from observations to findings.

### E422

- Location: Case Study and Ethnography, Desirable Attributes
- Quote: "provides supplemental materials such as interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence tables"
- Key point: Desirable: provide supplementary materials such as interview guides, coding schemes, coding examples, decision rules, and extended chain-of-evidence tables.

### E423

- Location: Case Study and Ethnography, Desirable Attributes
- Quote: "triangulates across data sources, informants or researchers" / "cross-checks interviewee statements (e.g. against direct observation or archival records)"
- Key point: Desirable: triangulate across data sources, informants, or researchers; cross-check interviewee statements against direct observation or archival records.

### E424

- Location: Case Study and Ethnography, Desirable Attributes and footnote 2
- Quote: "uses participant observation (ethnography) or direct observation (non-ethnography) and clearly integrates these observations into results" / "Direct observation means watching research subjects without getting involved; participant observation means joining in with whatever participants are doing"
- Key point: Desirable: use participant observation (ethnography) or direct observation and integrate the observations into the results. Direct observation means watching without getting involved; participant observation means joining in what participants are doing.

### E425

- Location: Case Study and Ethnography, Desirable Attributes
- Quote: "describes external events and other factors that may have affected the case or site" / "describes how prior understandings of the phenomena were managed and/or influenced the research"
- Key point: Desirable: describe external events and other factors that may have affected the case; explain how the researchers' prior understanding was managed and how it influenced the research.

### E426

- Location: Case Study and Ethnography, Desirable Attributes and footnote 4
- Quote: "uses quotations to *illustrate* findings" / "Quotations should not be *the only* representation of a finding; each finding should be described independently of supporting quotations"
- Key point: Desirable: use quotations to illustrate findings; but quotations should not be the only representation of a finding, and each finding should be stated independently of them.

### E427

- Location: Case Study and Ethnography, Desirable Attributes
- Quote: "researchers reflect on their own possible biases"
- Key point: Desirable: researchers reflect on their own possible biases.

### E428

- Location: Case Study and Ethnography, Extraordinary Attributes
- Quote: "multiple, deep, fully-developed cases with cross-case triangulation" / "uses a team-based approach; e.g., multiple raters with analysis of inter-rater reliability" / "published a case study protocol beforehand and made it publicly accessible"
- Key point: Extraordinary: multiple deep, fully developed cases with cross-case triangulation; a team-based approach, e.g. multiple raters with inter-rater reliability analysis; a case study protocol published in advance.

### E429

- Location: Case Study and Ethnography, General Quality Criteria
- Quote: "Case studies should be evaluated using qualitative validity criteria such as credibility, multivocality, reflexivity, rigor, and transferability [...] Quantitative quality criteria such as replicability, generalizability and objectivity typically do not apply."
- Key point: Case studies should be judged by qualitative validity criteria (credibility, multivocality, reflexivity, rigor, transferability); quantitative criteria such as replicability, generalizability, and objectivity typically do not apply.

### E430

- Location: Case Study and Ethnography, Types of Case Studies
- Quote: "There is no standard way of conducting a case study. Case study research can adopt different philosophies"
- Key point: There is no single standard way to do a case study, and case study research can adopt different philosophies.

### E431

- Location: Case Study and Ethnography, Types of Case Studies
- Quote: "an **explanatory case study** explains how or why a phenomenon occurred, typically using a process or variance theory" / "an **exploratory case study** explores a particular phenomenon to identify new questions, propositions or hypotheses" / "an **historical case study** draws on archival data, for instance, software repositories" / "a **revelatory case study** examines a hitherto unknown or unexplored phenomenon"
- Key point: Example types: explanatory (explains how or why a phenomenon occurred), exploratory (identifies new questions, propositions, or hypotheses), historical (uses archival data, e.g. software repositories), and revelatory (examines a previously unknown or unstudied phenomenon).

### E432

- Location: Case Study and Ethnography, Antipatterns
- Quote: "Relying on a single approach to data collection (e.g. interviews) without corroboration or data triangulation" / "Oversimplifying and over-rationalizing complex phenomena; presenting messy, complicated things as simple and clean"
- Key point: Antipatterns: relying on a single data collection method (e.g. only interviews) without corroboration; oversimplifying and over-rationalizing complex, messy phenomena.

### E433

- Location: Case Study and Ethnography, Invalid Criticisms
- Quote: "Sample of one; findings not generalizable. The point of a case study is to study one thing deeply, not to generalize to a population. Case studies should lead to theoretical generalization; that is, concepts that are transferable in principle."
- Key point: Invalid criticism: "a sample of one, so the findings do not generalize." The point of a case study is to study one thing deeply, not to generalize to a population; it should lead to theoretical generalization, i.e. concepts that are transferable in principle.

### E434

- Location: Case Study and Ethnography, Invalid Criticisms
- Quote: "Does not present quantitative data." / "Lack of internal validity. Internal validity only applies to explanatory case studies that seek to establish causality."
- Key point: Invalid criticisms: "no quantitative data"; "lack of internal validity" (internal validity applies only to explanatory case studies that seek to establish causality).

### E435

- Location: Case Study and Ethnography, Invalid Criticisms
- Quote: "Lack of reproducibility or a "replication package"; Data are not disclosed (qualitative data are often confidential)." / "Insufficient number or length of interviews. There is no magic number; what matters is that there is enough data that the findings are credible, and the description is deep and rich."
- Key point: Invalid criticisms: "not reproducible, no replication package, data not disclosed" (qualitative data are often confidential); "too few or too short interviews" (there is no magic number; what matters is enough data for credible findings and deep, rich description).

## Glossary

### E436

- Location: Glossary, Credibility / Transferability / Reflexivity
- Quote: "the extent to which conclusions are supported by rich, multivocal evidence" / "the extent to which a study’s results could plausibly apply to other sites, people or circumstances" / "the extent to which authors reflect on their potential biases and interactions with the team, organization or community, especially possible negative impacts on some participants or stakeholders"
- Key point: Credibility: how far conclusions are supported by rich, multivocal evidence. Transferability: how far results could plausibly apply to other sites, people, or circumstances. Reflexivity: how far the authors reflect on their own biases and their interactions with the team, organization, or community (especially possible negative impacts on some participants).

### E437

- Location: Glossary, Multivocal
- Quote: "The property of being based on—and recognizing differences between—people with different opinions and backgrounds (including gender, culture, education, and class)."
- Key point: Multivocality: being based on, and recognizing differences between, people with different opinions and backgrounds.

### E438

- Location: Glossary, Gatekeeper
- Quote: "A person or organization who controls access to individuals (e.g., employees) or data being researched. Gatekeepers may influence individual’s participation decisions (e.g., employers may coerce employees to participate), affect research outcomes (e.g., by controlling whose voices are heard) or be affected by research outcomes (e.g., lose credibility with employees)."
- Key point: Gatekeeper: a person or organization that controls access to the people (e.g. employees) or data being researched. Gatekeepers may influence individuals' decisions to take part (e.g. employers coercing employees), affect the results (e.g. deciding whose voices are heard), and be affected by the results.

## Ethics (Studies with Human Participants) supplement

### E439

- Location: Ethics (Studies with Human Participants), Application
- Quote: "This standard applies to studies in which one or more human beings other than the researchers take part in the research (e.g. Action Research, Case Study, Grounded Theory, Qualitative Surveys, Experiments, Questionnaire Surveys)."
- Key point: This ethics supplement applies to any study in which people other than the researchers take part, including case studies.

### E440

- Location: Case Study and Ethnography, Suggested Readings
- Quote: "(Note: we recommend beginning with Yin's book.)"
- Key point: The standard recommends starting with Yin's book on case study methods.

### E441

- Location: General Standard, General Quality Criteria, Examples of Acceptable Deviations
- Quote: "A study can only apply an **empirical standard** if an appropriate standard exists. If no related standards exist, studies should apply published guidance. If no appropriate guidance exists, reviewers should apply the general standard and construct an ad hoc evaluation scheme for the new method."
- Key point: A study can apply an empirical standard only if a suitable one exists; if there is no related standard, follow published guidance; if there is no suitable guidance either, reviewers apply the General Standard and improvise an evaluation approach for the new method.
