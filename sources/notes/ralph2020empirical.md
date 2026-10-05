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

### E19

- 位置：General Standard，Desirable Attributes
- 原文："summarizes and synthesizes a reasonable selection of related work (not every single relevant study)"
- 要点：好的论文对相关工作做适量的总结和综合，不必列出每一篇相关研究。

### E20

- 位置：General Standard，Desirable Attributes
- 原文："clearly describes relationship between contribution(s) and related work"
- 要点：好的论文清楚说明自己的贡献和相关工作之间的关系。

### E21

- 位置：General Standard，Research and Reporting Antipatterns
- 原文："Mentioning related work only to dismiss it as irrelevant; listing rather than synthesizing related work."
- 要点：反面模式：提到相关工作只是为了说它不相关；只罗列而不综合相关工作。

### E22

- 位置：General Standard，Essential Attributes
- 原文："states a purpose, problem, objective, or research question [...] explains why the purpose, problem, etc. is important (motivation)"
- 要点：必要项：写明研究目的、问题、目标或研究问题，并说明它为什么重要。

### E23

- 位置：General Standard，Essential Attributes
- 原文："methodology is appropriate (not necessarily optimal) for stated purpose, problem, etc."
- 要点：必要项：方法要适合所述的研究目的或问题，不要求是最优的。

### E24

- 位置：General Standard，General Quality Criteria
- 原文："There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology, as laid out in the specific **empirical standards**. Avoid applying inappropriate quality criteria (e.g. construct validity to a study with no constructs; internal validity to a study with no causal relationships)."
- 要点：没有通用的质量标准。每项研究都应按适合其方法的标准来评价；不要套用不适用的标准，例如对没有因果关系的研究要求内部效度。

### E25

- 位置：General Standard，Invalid Criticisms
- 原文："Cross-paradigmatic criticism (e.g. attacking an interpretivist study for not conforming to positivist norms). [...] Criticizing a study for limitations intrinsic to that kind of study or the methodology used (e.g. attacking a case study for low generalizability). [...] Rejecting a study because the reviewer would have used a different methodology or design."
- 要点：不成立的批评：用另一种研究范式的规范批评研究（如用实证主义的标准批评诠释主义研究）；批评某类研究固有的局限（如说案例研究推广性低）；只因自己会用别的方法而否定研究。

### E26

- 位置：General Standard，Research and Reporting Antipatterns
- 原文："Attempting a study without reading, understanding and applying published guidelines for that kind of study."
- 要点：反面模式：没有阅读、理解并应用该类研究已发表的指南，就开始做研究。

### E27

- 位置：General Standard，Research and Reporting Antipatterns
- 原文："Hypothesizing After Results are Known (HARKing) in ostensibly confirmatory, (post-)positivist research. [...] Reporting only the subset of statistical tests that produce significant results (p-hacking)."
- 要点：反面模式：在名为验证性的研究中"先看结果再提假设"；只报告显著的那部分统计检验。

### E28

- 位置：General Standard，Desirable Attributes
- 原文："publishes the study in two phases: a plan and the results of executing the plan"
- 要点：加分项：分两阶段发表研究，先发表计划，再发表执行计划的结果。

### E29

- 位置：Registered Reports Supplement，Definition
- 原文："_Pre-registration_ refers to depositing the RR1 somewhere publicly visible. Pre-registration aims to prevent hypothesising after results are known, to mitigate unconscious researcher bias in data analysis, and combat publication bias."
- 要点：预注册就是把研究计划公开存档，目的是防止先看结果再提假设、减少数据分析中无意识的偏差、对抗发表偏差。

### E30

- 位置：Registered Reports Supplement，Application
- 原文："This standard applies to positivist, confirmatory (i.e. hypothesis-testing) studies with tightly-scoped analysis approaches. Pre-registering interpretivist, qualitative or exploratory research remains controversial."
- 要点：注册报告标准适用于检验假设的验证性研究；对诠释主义、定性或探索性研究做预注册仍有争议。

### E31

- 位置：Registered Reports Supplement，Invalid Criticisms
- 原文："RR1: Rejecting exploratory or qualitative research: all kinds of research can be pre-registered"
- 要点：同一标准也列出：以"探索性或定性研究"为由拒绝预注册是不成立的，各类研究都可以预注册。

### E32

- 位置：Registered Reports Supplement，Specific Attributes (RR1)
- 原文："describes the research method in detail sufficient for an independent researcher to exactly replicate the proposed data collection and analysis procedures [...] the stated hypotheses can be tested with the data the researchers propose to collect"
- 要点：研究计划要详细到别人能照着完全重复数据收集和分析，且所提假设能用计划收集的数据检验。

### E33

- 位置：Registered Reports Supplement，Specific Attributes (RR2)
- 原文："deviations, if any, are _not_ justified based on the data [...] clearly designates as exploratory any unregistered post hoc analyses"
- 要点：偏离计划不能以数据结果为理由；没有事先登记、事后追加的分析要明确标为探索性的。

### E34

- 位置：Registered Reports Supplement，Justifying Deviations
- 原文："Reviewers should not expect research to go exactly according to plan or authors to foresee every possible problem. Changes are acceptable as long as they are justified and not _postdictive_ (i.e. changes made knowing how they will affect results)."
- 要点：研究不可能完全按计划进行；只要有理由、且不是在知道会如何影响结果之后才改，修改就可以接受。

### E35

- 位置：Registered Reports Supplement，Desirable Attributes (RR1)
- 原文："presents preliminary data (e.g. from a pilot study) to justify the chosen approach (e.g. probability distributions)."
- 要点：加分项：用预研究等初步数据来论证所选方法。

### E36

- 位置：Sampling Supplement，Essential Attributes
- 原文："explains the goal of sampling (e.g. aiming for representativeness, identifying exceptional cases) [...] explains why the sampling strategy is reasonable (not necessarily optimal) for the sampling goal"
- 要点：必要项：说明抽样目标（如追求代表性，或找出特殊案例），并说明抽样策略为什么对这个目标是合理的（不必最优）。

### E37

- 位置：Sampling Supplement，Antipatterns
- 原文："claiming that a sample is representative of a population because it was randomly selected from a sampling frame, without considering bias in the sampling frame"
- 要点：反面模式：只因样本是从抽样框中随机抽取的，就声称它代表总体，而不考虑抽样框本身的偏差。

### E38

- 位置：Sampling Supplement，Antipatterns
- 原文："quantitative research with a sample size insufficient to detect effects of the expected size [...] qualitative research with too little data for plausible saturation"
- 要点：反面模式：定量研究的样本量不足以检测出预期大小的效应；定性研究的数据太少，达不到饱和。

### E39

- 位置：Sampling Supplement，Invalid Criticisms
- 原文："complaining about lack of representativeness or low external validity in studies where representativeness is not a goal"
- 要点：不成立的批评：研究本来就不以代表性为目标，却批评它缺乏代表性或外部效度低。

### E40

- 位置：General Standard，Invalid Criticisms
- 原文："Setting arbitrary minimum sample sizes or other data requirements, based on neither power analysis nor theoretical saturation."
- 要点：不成立的批评：既不基于统计功效分析也不基于理论饱和，随意规定最低样本量。

### E41

- 位置：General Standard，Invalid Criticisms
- 原文："Rejecting a study because it reports negative results."
- 要点：不成立的批评：因为研究报告了负面结果就否定它。

### E42

- 位置：Sampling Supplement，Application
- 原文："This standard applies to empirical research in which the researcher selects smaller groups of items to study (a _sample_) from a larger group of items of interest (the _population_) using a usually imperfect population list (the _sampling frame_)."
- 要点：样本是研究者实际研究的一小组对象；总体是研究者感兴趣的全部对象；抽样框是总体的名单，通常并不完美。

### E43

- 位置：Essential Attributes › discussion
- 原文："states clear conclusions which are linked to research question (or purpose, etc.) and supported by explicit evidence (data/observations) or arguments"
- 要点：必要：结论要清楚，和研究问题对应，并有明确的证据（数据、观察）或论证支持。

### E44

- 位置：Essential Attributes › discussion
- 原文："discloses all major limitations"
- 要点：必要：披露所有主要局限。

### E45

- 位置：Research and Reporting Antipatterns
- 原文："Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- 要点：反面模式：承认了局限，写结论和意义时却当它不存在。

### E46

- 位置：Research and Reporting Antipatterns
- 原文："Overreaching conclusions or generalizations; obfuscating, downplaying or dismissing a study's limitations."
- 要点：反面模式：结论或推广超出证据范围；模糊、淡化或无视局限。

### E47

- 位置：Research and Reporting Antipatterns
- 原文："Hypothesizing After Results are Known (HARKing) in ostensibly confirmatory, (post-)positivist research."
- 要点：反面模式：在号称验证假设的研究中，看到结果后才提出假设（HARKing）。

### E48

- 位置：Research and Reporting Antipatterns
- 原文："Reporting only the subset of statistical tests that produce significant results (p-hacking)."
- 要点：反面模式：只报告结果显著的那部分统计检验（p-hacking）。

### E49

- 位置：General Quality Criteria
- 原文："There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology"
- 要点：没有通用的质量标准，每项研究要按适合其方法的标准来评价；例如没有因果关系的研究，不适用内部效度。

### E50

- 位置：Invalid Criticisms
- 原文："Criticizing a study for limitations intrinsic to that kind of study or the methodology used (e.g. attacking a case study for low generalizability)."
- 要点：拿某类研究方法本身固有的局限去批评它（如批评案例研究推广性低），是不成立的批评。

### E51

- 位置：Desirable Attributes
- 原文："describes reasonable attempts to investigate or mitigate limitations"
- 要点：加分：说明为考察或减轻局限做了哪些合理的尝试。

## Experiments 标准

### E52

- 位置：Experiments › Antipatterns
- 原文："validity threats are simply listed without linking them to results"
- 要点：反面模式：只罗列效度威胁，却不说明它们对结果有什么影响。

### E53

- 位置：Good Review Practices
- 原文："The results must be, primarily, true (trustworthy) and, secondarily, important. A paper that is trustworthy can be accepted even if it is not important. A paper that is not trustworthy cannot be accepted, even if it seems important."
- 要点：评审首先看结果是否可信，其次看是否重要：可信但不重要的论文可以录用，不可信的论文再重要也不能录用。

### E54

- 位置：Good Review Practices
- 原文："Clarify which are necessary and which are suggested changes. Ideally, separate them."
- 要点：分清哪些是必须修改、哪些是建议修改，最好分开列出。

### E55

- 位置：Good Review Practices
- 原文："Reflect on and clearly state their own limitations and biases."
- 要点：审稿人应说明自己的局限和偏向，并指出自己无法判断或没有审的部分。

### E56

- 位置：Reviewing Antipatterns
- 原文："Providing vague, non-actionable criticism."
- 要点：反面做法：给出含糊、无法据此修改的批评。

### E57

- 位置：Reviewing Antipatterns
- 原文："Using the review to promote the reviewer's own views, theories, methods, or publications."
- 要点：反面做法：借审稿推销自己的观点、方法或论文。

### E58

- 位置：Reviewing Antipatterns
- 原文："Skimming a manuscript instead of carefully reading each word and inspecting each figure and table."
- 要点：反面做法：略读稿件，而不是逐字阅读、检查每张图表。

### E59

- 位置：Reviewing Antipatterns
- 原文："Allowing the authors' identities or affiliations to affect the review."
- 要点：反面做法：让作者身份或单位影响审稿。

### E60

- 位置：Invalid Criticisms
- 原文："is not new without providing citations to published studies that make **practically identical** contributions."
- 要点：不成立的批评：说“不新”却不给出贡献几乎完全相同的已发表文献。

### E61

- 位置：Invalid Criticisms
- 原文："lacks detail without enumerating missing details;"
- 要点：不成立的批评：说“缺细节”“漏引文献”“质量低”却不具体指出是哪些。

### E62

- 位置：Invalid Criticisms
- 原文："Rejecting a study because it replicates or reproduces existing work."
- 要点：不成立的批评：因为是重复研究而拒稿。

### E63

- 位置：Invalid Criticisms
- 原文："Rejecting a study because the reviewer would have used a different methodology or design."
- 要点：不成立的批评：因为审稿人自己会用别的方法而拒稿。

### E64

- 位置：Reviewing Antipatterns
- 原文："Requesting additional analysis not directly related to a study's purpose or research question"
- 要点：反面做法：要求做与研究目的无关的额外分析。

### E65

- 位置：General Standard，Essential Attributes
- 原文："acknowledges and mitigates potential risks, harms, burdens or unintended consequences of the research"
- 要点：必要：承认并减轻研究可能带来的风险、伤害、负担和意外后果。

### E66

- 位置：General Standard，Research and Reporting Antipatterns
- 原文："Overreaching conclusions or generalizations; obfuscating, downplaying or dismissing a study's limitations." / "Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- 要点：反面模式：结论超出证据；淡化局限；或者写了局限，结论却当它们不存在。

### E67

- 位置：General Standard，Research and Reporting Antipatterns
- 原文："Unnecessarily dividing the presentation of a single study into many papers (salami-slicing)."
- 要点：反面模式：把一项研究不必要地拆成多篇论文（"切香肠"）。

## Ethics (Studies with Human Participants)

### E68

- 位置：Essential Attributes
- 原文："describes all plausible, non-trivial potential risks or harms to participants (if any)" / "describes any steps taken to mitigate risks or harms" / "explains how benefits of the research justify any non-trivial risks or harms"
- 要点：必要：写出参与者可能面临的风险或伤害、采取了哪些措施减轻，以及研究收益为什么值得这些风险。

### E69

- 位置：Essential Attributes
- 原文："explains how participants were recruited" / "explains the compensation (if any) offered for participation and how coercion was mitigated" / "free, individual, informed consent to participate was obtained"
- 要点：必要：说明怎样招募参与者、给了什么报酬、怎样避免强迫，以及怎样取得自由、个人、知情的同意。

### E70

- 位置：Essential Attributes，脚注 2
- 原文："careful consideration of the reidentification potential through others combining multiple data sources"
- 要点：保护隐私时，要考虑别人把多个数据来源拼在一起、重新识别出参与者的可能。

### E71

- 位置：Antipatterns
- 原文："Willful blindness to risks and harms to participants; justifying risks and harms on the basis that research is generally beneficial rather than in respect of benefits of the particular study; downplaying risks and harms during recruitment, consent or reporting."
- 要点：反面模式：对风险视而不见；用"研究总体上有益"而不是"这项研究的具体收益"来为风险辩护；在招募、同意或报告中淡化风险。

### E72

- 位置：Examples of Acceptable Deviations
- 原文："The requirement to explain informed consent procedures may be modified where deception is a necessary part of the research protocol (although this itself must be explained in full"
- 要点：研究必须使用欺骗时，知情同意的要求可以调整，但必须完整说明。

### E73

- 位置：Desirable Attributes
- 原文："cites (with application number) approval of a national, institutional, or other appropriate scholarly ethical review board"
- 要点：加分：注明伦理审查委员会的批准（含申请编号）。

### E74

- 位置：Invalid Criticisms
- 原文："is not itself grounds for rejection unless there is a substantive ethical concern that such a board should have prevented"
- 要点："没有经过伦理审查"本身不构成拒稿理由，除非存在审查本应阻止的实质伦理问题。

### E75

- 位置：Note
- 原文："Rarely, ethical research may require unlawful action. Ethical frameworks like Menlo include legal compliance so that the ethicality and legality of research can be weighed together."
- 要点：极少数情况下，合乎伦理的研究可能需要违法的行为；Menlo 等框架把守法纳入考量，是为了把伦理性和合法性放在一起权衡。

## Open Science

### E76

- 位置：Principle
- 原文："provided that there are no ethical, legal, technical, economical, or practical barriers preventing their disclosure."
- 要点：研究材料原则上应公开，前提是没有伦理、法律、技术、经济或实际上的障碍。

### E77

- 位置：Desirable Attributes
- 原文："OR explains why materials cannot be released (reasons for limited disclosure of data should be trusted)"
- 要点：不能公开时，说明原因即可；这类原因应被信任。

### E78

- 位置：Notes
- 原文："personal or institutional websites, version control systems (e.g. GitHub), consumer cloud storage (e.g. Dropbox), and commercial paper repositories (e.g. ResearchGate; Academia.edu) do not offer properly archived and preserved data."
- 要点：个人网站、GitHub、网盘、ResearchGate 等不算妥善的长期存档；应使用 Zenodo、OSF 或机构仓库等。
