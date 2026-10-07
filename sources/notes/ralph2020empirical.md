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

> 已作废：与 [E18](#e18) 重复（原文被 E18 完整包含）。

- 位置：Essential Attributes › discussion
- 原文："states clear conclusions which are linked to research question (or purpose, etc.) and supported by explicit evidence (data/observations) or arguments"
- 要点：必要：结论要清楚，和研究问题对应，并有明确的证据（数据、观察）或论证支持。

### E44

> 已作废：与 [E18](#e18) 重复（原文被 E18 完整包含）。

- 位置：Essential Attributes › discussion
- 原文："discloses all major limitations"
- 要点：必要：披露所有主要局限。

### E45

> 已作废：与 [E66](#e66) 重复（原文被 E66 完整包含）。

- 位置：Research and Reporting Antipatterns
- 原文："Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- 要点：反面模式：承认了局限，写结论和意义时却当它不存在。

### E46

> 已作废：与 [E66](#e66) 重复（原文被 E66 完整包含）。

- 位置：Research and Reporting Antipatterns
- 原文："Overreaching conclusions or generalizations; obfuscating, downplaying or dismissing a study's limitations."
- 要点：反面模式：结论或推广超出证据范围；模糊、淡化或无视局限。

### E47

> 已作废：与 [E27](#e27) 重复（原文被 E27 完整包含）。

- 位置：Research and Reporting Antipatterns
- 原文："Hypothesizing After Results are Known (HARKing) in ostensibly confirmatory, (post-)positivist research."
- 要点：反面模式：在号称验证假设的研究中，看到结果后才提出假设（HARKing）。

### E48

> 已作废：与 [E27](#e27) 重复（原文被 E27 完整包含）。

- 位置：Research and Reporting Antipatterns
- 原文："Reporting only the subset of statistical tests that produce significant results (p-hacking)."
- 要点：反面模式：只报告结果显著的那部分统计检验（p-hacking）。

### E49

> 已作废：与 [E24](#e24) 重复（原文被 E24 完整包含）。

- 位置：General Quality Criteria
- 原文："There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology"
- 要点：没有通用的质量标准，每项研究要按适合其方法的标准来评价；例如没有因果关系的研究，不适用内部效度。

### E50

> 已作废：与 [E25](#e25) 重复（原文被 E25 完整包含）。

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

> 已作废：与 [E25](#e25) 重复（原文被 E25 完整包含）。

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

### E79

- 位置：Engineering Research 标准，标题下的定义
- 原文："Research that invents and evaluates technological artifacts"
- 要点：工程研究就是发明并评估技术制品的研究。

### E80

- 位置：Engineering Research 标准，Application
- 原文："This standard applies to manuscripts that propose and evaluate technological artifacts, including algorithms, models, languages, methods, systems, tools, and other computer-based technologies." / "evaluations of pre-existing engineering research approaches (consider the **Experiments** Standard)" / "experience reports of applying pre-existing engineering research approaches"
- 要点：适用于提出并评估算法、模型、语言、方法、系统、工具等的论文；只评估已有方法的研究应按实验标准，应用已有方法的经验报告也不属于工程研究。

### E81

- 位置：Engineering Research 标准，Essential Attributes
- 原文："describes the proposed artifact in adequate detail" / "justifies the need for, usefulness of, or relevance of the proposed artifact" / "conceptually evaluates the proposed artifact; discusses its strengths, weaknesses and limitations"
- 要点：必须足够详细地描述提出的制品，说明为什么需要它，并从概念上分析它的长处、短处和局限。

### E82

- 位置：Engineering Research 标准，脚注 2
- 原文："Why are state-of-the-art approaches not good enough to deal with the problem? How can the technical contribution be beneficial?"
- 要点：说明必要性时要回答：现有最好的方法为什么不够好？新贡献能带来什么好处？

### E83

- 位置：Engineering Research 标准，脚注 1
- 原文："does the paper describe the overall workflow of the solution, showing how different techniques work together?" / "Are the novel components of the solution clearly singled out?"
- 要点：描述制品时要讲清整体流程、各部分如何配合，并把新的部分明确标出来。

### E84

- 位置：Engineering Research 标准，Essential Attributes（method）
- 原文："empirically evaluates the proposed artifact using:" / "in which the researchers intervene in a real organization using the artifact" / "in which the artifact is assessed using one or more benchmarks, or" / "another method for which a clear and convincing rationale is provided" / "clearly indicates which of the above empirical methodology is used"
- 要点：必须用某种实证方法评估制品（行动研究、案例研究、有人参与的对照实验、定量仿真、基准测试，或另有充分理由的方法），并写明用的是哪一种。

### E85

- 位置：Engineering Research 标准，Essential Attributes（method）
- 原文："EITHER: empirically compares the artifact to one or more state-of-the-art alternatives" / "OR: provides a clear and convincing rationale for why comparative evaluation is impractical"
- 要点：必须和当前最好的替代方案或基准做实证比较；做不到时要给出清楚、令人信服的理由。

### E86

- 位置：Engineering Research 标准，Essential Attributes（other）
- 原文："assumptions (if any) are explicit, plausible and do not contradict each other or the contribution's goals"
- 要点：假设要写明，要合理，彼此不矛盾，也不和贡献的目标矛盾。

### E87

- 位置：Engineering Research 标准，Desirable Attributes
- 原文："provides supplementary materials including source code (if the artifact is software) or a comprehensive description of the artifact (if not software), and any input datasets (if applicable)" / "justifies any items missing from replication package based on practical or ethical grounds"
- 要点：最好提供源代码和输入数据；复现包里缺了什么，要从实际或伦理角度说明原因。

### E88

- 位置：Engineering Research 标准，Desirable Attributes
- 原文："provides correctness arguments for the key analytical and theoretical contributions (e.g. theorems, complexity analyses, mathematical proofs)" / "includes one or more running examples to elucidate the artifact" / "evaluates the artifact in an industry-relevant context (e.g. widely used open-source projects, professional programmers)"
- 要点：加分项：为关键理论贡献给出正确性论证；用贯穿全文的例子讲解制品；在贴近实际的环境中评估。

### E89

- 位置：Engineering Research 标准，Extraordinary Attributes
- 原文："contributes to our collective understanding of design practices or principles" / "presents ground-breaking innovations with obvious real-world benefits"
- 要点：出色的工程研究能加深对设计原则的理解，或带来有明显实际好处的突破。

### E90

- 位置：Engineering Research 标准，General Quality Criteria
- 原文："Appropriateness of evaluation methods to the nature, goals, and assumptions of the contribution" / "Relationship of innovativeness to rigorousness: less innovative artifacts require more rigorous evaluations"
- 要点：评估方法要与贡献的性质、目标和假设相称；创新程度越低，评估要越严格。

### E91

- 位置：Engineering Research 标准，Antipatterns
- 原文："overstates the novelty of the contribution" / "omits details of key conceptual aspects while focusing exclusively on incidental implementation aspects"
- 要点：反面做法：夸大新颖性；只讲次要的实现细节，漏掉关键的思路。

### E92

- 位置：Engineering Research 标准，Antipatterns
- 原文："evaluation consists *only* of eliciting users' opinions of the artifact" / "evaluation consists *only* of quantitative performance data that is not compared to established benchmarks or alternative solutions"
- 要点：反面做法：评估只有用户的主观评价；或只有性能数字，却不和公认基准或替代方案比较。

### E93

- 位置：Engineering Research 标准，Antipatterns
- 原文："evaluation using a non-experimental (single group, non-repeated) design" / "evaluation using toy examples (sometimes misrepresented as "case studies")"
- 要点：反面做法：评估没有对照、不重复；用玩具例子评估，还把它称作"案例研究"。

### E94

- 位置：Engineering Research 标准，Invalid Criticisms
- 原文："The paper does not report as ambitious an empirical study as other predominately empirical papers. The more innovative the artifact and more comprehensive the conceptual evaluation, the less we should expect from the empirical study." / "if few subjects are available in the contribution's domain or the experimental evaluation is part of a more comprehensive validation strategy (e.g. formal arguments)"
- 要点：不成立的批评：实证部分不如纯实证论文宏大；评测对象少（如果该领域本来就少，或实验只是整体验证的一部分）。制品越创新、概念分析越全面，对实证部分的要求越低。

### E95

- 位置：Engineering Research 标准，Invalid Criticisms
- 原文："The artifact is not experimentally compared with related approaches *that are not publicly available*." / "before saying "you should have compared this against X," make sure X is actually available and functional." / "Proposed artifacts should outperform existing artifacts on *some* dimension(s); e.g. scalability, performance on specific classes of problems, applicability to realistic systems, theoretical guarantees."
- 要点：没和拿不到的方法比较，不算缺陷；新制品不必是第一个解法，但要在某个维度上胜过已有制品，例如可扩展性、某类问题上的性能、对真实系统的适用性、理论保证。

### E96

- 位置：Engineering Research 标准，Invalid Criticisms
- 原文："Engineering papers often define a motivating "problem" or "objective" rather than a research questiion." / "The contribution is not technically complicated. What matters is that it works. Unnecessary complexity is undesirable."
- 要点：不成立的批评：没写明研究问题（工程论文常以"问题"或"目标"代替）；技术上不复杂（重要的是有效，不必要的复杂反而不好）。

### E97

- 位置：Engineering Research 标准，Invalid Criticisms
- 原文："No replication package, if there are clear, convincing practical or ethical reasons preventing artifact disclosure."
- 要点：有清楚、令人信服的实际或伦理原因时，不提供复现包不算缺陷。

### E98

- 位置：Engineering Research 标准，脚注 4
- 原文："Learning by building innovative artifacts is called engineering research. Some of the following readings incorrectly refer to engineering research as “design science” because the information systems community misappropriated that term circa 2004."
- 要点：标准作者认为应叫"工程研究"；"设计科学"这个叫法是信息系统领域约 2004 年借用的，原本指研究设计者及其设计过程。

### E99

- 位置：Benchmarking 标准，Essential Attributes
- 原文："EITHER: justifies the selection of an existing, publicly available or standard benchmark (in terms of relevance, timeliness, etc.)" / "allows different configurations of a system under test to compete on their merits without artificial limitations" / "assesses stability or reliability using sufficient experiment repetitions and execution duration"
- 要点：用现成基准要说明为什么选它；不同配置要能凭实力公平竞争，不受人为限制；要有足够的重复次数和运行时长来检验结果是否稳定。

### E100

- 位置：Benchmarking 标准，Essential Attributes（discussion）
- 原文："discusses the construct validity of the benchmark; that is, does the benchmark measure what it is supposed to measure?"
- 要点：必须讨论基准的构念效度：它测的是不是它应该测的东西。

### E101

- 位置：Benchmarking 标准，Antipatterns
- 原文："Tailoring the benchmark for a specific method, technique or tool, which is evaluated with the benchmark." / "Using benchmarking experiments that are irrelevant for the problem studied to obfuscate weaknesses in the proposed approach" / "Collecting aggregated measurements instead of persisting all raw results and running an offline analysis"
- 要点：反面做法：为被评估的方法量身定做基准；用与问题无关的测试掩盖弱点；只保存汇总结果，不保存全部原始结果。

### E102

- 位置：Benchmarking 标准，Invalid Criticisms
- 原文："The benchmark is not widely used. It is sufficient to start developing a new benchmark with a small group of researchers as an offer to a larger scientific community."
- 要点：不成立的批评："这个基准用的人不多"。新基准可以由一小群研究者先提出，供更大的社区讨论。

### E103

- 位置：General Standard，Essential Attributes
- 原文："discloses all major limitations"
- 要点：必须披露所有主要局限。

### E104

- 位置：Benchmarking 标准，Essential Attributes
- 原文："defines a new benchmark, including:" / "the quality to be benchmarked (e.g., performance, availability, scalability, security)" / "the metric(s) to quantify the quality" / "the workload, usage profile and/or task sample the system under test is subject to"
- 要点：新建基准要写清：测哪种质量、用什么指标量化、在什么工作负载或任务样本下测。

### E105

- 位置：Repository Mining 标准，定义
- 原文："A study that quantitatively analyzes a dataset extracted from a platform hosting of structured or semi-structured text (e.g a source code repository)"
- 要点：仓库挖掘研究是对从托管结构化或半结构化文本的平台（如源代码仓库）中抽取的数据集做定量分析。

### E106

- 位置：Repository Mining 标准，Application
- 原文："use automated techniques to extract data from large-scale data repositories such as source code repositories, mailing list archives, bug tracking systems, Q&A forums and chat communication platforms"
- 要点：适用于用自动化手段从大规模数据仓库（代码仓库、邮件列表存档、缺陷跟踪系统、问答论坛、聊天平台）抽取数据的研究。

### E107

- 位置：Repository Mining 标准，Application
- 原文："If the study focuses on predictive modeling (e.g. machine learning) consider the **Data Science Standard**. If the subject systems are a few context-rich repositories, consider the **Case Study Standard**."
- 要点：以预测建模为主的研究应参考数据科学标准；只研究少数几个背景丰富的仓库，应参考案例研究标准。

### E108

- 位置：Repository Mining 标准，必要项
- 原文："explains why repository mining is appropriate for the proposed research problem" / "defines unit(s) of analysis or observation"
- 要点：要说明为什么这个问题适合用仓库挖掘来研究，并定义分析单元或观察单元。

### E109

- 位置：Repository Mining 标准，必要项
- 原文："describes and justifies the data sources (e.g. GitHub, StackOverflow)" / "describes and justifies how the repositories are selected from the data sources" / "describes how the inclusion and exclusion criteria were validated (e.g., by manually inspecting the results of the automated search)"
- 要点：要说明并论证数据源和仓库的选择方式，并说明怎样验证了纳入和排除标准，例如人工检查自动筛选的结果。

### E110

- 位置：Repository Mining 标准，必要项
- 原文："describes the procedure for the acquisition" / "describes dataset characteristics including size of the selected repositories" / "describes data preprocessing steps"
- 要点：要描述数据获取流程、数据集特征（包括仓库规模）和预处理步骤。

### E111

- 位置：Repository Mining 标准，必要项
- 原文："uses multiple annotators; reports the number of annotators" / "describes in detail the annotation procedure" / "assesses inter-rater reliability"
- 要点：有人工标注时，要用多名标注者并报告人数，详细描述标注流程，并评估标注者间的一致性。

### E112

- 位置：Repository Mining 标准，必要项
- 原文："describes and justifies measures or metrics used" / "uses previously validated measures, quantitatively assesses construct validity, or both"
- 要点：要说明并论证所用的度量；使用经过验证的度量，或定量评估构念效度。

### E113

- 位置：Repository Mining 标准，必要项
- 原文："discusses threats to external validity (e.g. caused by selection of data source(s) and repositories, selection criteria, search strings)"
- 要点：要讨论外部效度威胁，例如数据源、仓库、筛选标准、检索词的选择带来的威胁。

### E114

- 位置：Repository Mining 标准，加分项
- 原文："provides supplemental materials (e.g. complete dataset, tool(s) used to download, select, pre-process, and post-process the selected repositories)" / "uses probability sampling"
- 要点：加分项包括公开完整数据集和下载、筛选、预处理、后处理所用的工具，以及使用概率抽样。

### E115

- 位置：Repository Mining 标准，加分项
- 原文："triangulates across data sources, informants or researchers" / "qualitative analysis of scenarios where the data collection or analysis tools were ineffective" / "performs testing (e.g., unit testing) to avoid bugs in the proposed tool"
- 要点：加分项包括跨数据源、信息提供者或研究者做三角验证，定性分析采集或分析工具失效的情形，以及测试自己的工具以避免缺陷。

### E116

- 位置：Repository Mining 标准，加分项
- 原文："annotators reflect on their own possible biases" / "builds, tests or extends theory" / "tests formal hypotheses" / "discusses ethical issues in mining of software repositories"
- 要点：加分项还包括标注者反思自身偏见、建立或检验理论、检验正式假设，以及讨论挖掘中的伦理问题。

### E117

- 位置：Repository Mining 标准，优秀项
- 原文："establishes causality, e.g. using longitidunal analyses"
- 要点：能确立因果关系（例如用纵向分析）属于优秀项；这说明一般的挖掘研究默认只能给出相关关系。

### E118

- 位置：Repository Mining 标准，可接受的偏离
- 原文："studies that focus on specific ecosystems (such as Apache) may choose specific repositories" / "obfuscating some details of the dataset due to ethical concerns"
- 要点：专门研究某个生态（如 Apache）时可以只选特定仓库；出于伦理考虑隐去数据集的部分细节是可以接受的。

### E119

- 位置：Repository Mining 标准，反面模式
- 原文："unvalidated, uni-dimensional operationalizations of multidimensional constructs (e.g. using github stars as a proxy for popularity)"
- 要点：用未经验证的单一指标去度量多维的概念（例如用 GitHub 星标数代表流行度）是反面模式。

### E120

- 位置：Repository Mining 标准，反面模式
- 原文："using open-source repositories without any filtering criteria; i.e., convenience sampling"
- 要点：不加任何筛选标准地使用开源仓库，就是便利抽样。

### E121

- 位置：Repository Mining 标准，反面模式
- 原文："in a study where *all* the commits of a project need to be analyzed, only the GitHub repository is considered; a GitHub repository does not necessarily contain all commits of a project"
- 要点：需要分析一个项目全部提交时只看 GitHub 仓库是反面模式，因为 GitHub 仓库不一定包含项目的全部提交。

### E122

- 位置：Repository Mining 标准，反面模式
- 原文："limiting a study to quantitative description; failing to test, build or extend theory" / "conclusions must be derived in the context of the selected repositories" / "insufficient details about the applied processing steps of the selected repositories"
- 要点：只做定量描述、不检验或建立理论；把结论推广到所选仓库之外；处理步骤交代不清，都是反面模式。

### E123

- 位置：Repository Mining 标准，不成立的批评
- 原文："more data, sources, or repositories required without appropriate justification" / "study doesn’t use qualitative analysis or data" / "a different source should have been used when the selected source(s) are justified"
- 要点：没有充分理由就要求更多数据或仓库、批评没有定性分析、在数据源已论证的情况下要求换数据源，都是不成立的批评。

### E124

- 位置：Repository Mining 标准，不成立的批评
- 原文："complaining about intentional obfuscation of repository details to protect participant's identities" / "in manual studies, requiring the disclosure of the time required for completion"
- 要点：为保护参与者身份而有意隐去仓库细节、人工研究没有报告耗时，都不应被批评。

### E125

- 位置：General Standard，必要项
- 原文："describes in detail what, where, when and how data were collected"
- 要点：要详细说明收集了什么数据、在哪里、什么时候、怎样收集的。

### E126

- 位置：General Standard，反面模式
- 原文："Acknowledging limitations but then writing implications and conclusions as though the limitations don't exist."
- 要点：承认了局限，写结论时却当局限不存在，是反面模式。

### E127

- 位置：Sampling 补充标准，必要项（以代表性为目标时）
- 原文："presents a replicable, concise, algorithmic account of how other researchers could derive the same sample" / "explains how the sample could be biased along the sampling steps"
- 要点：要给出可重复的、算法式的抽样步骤说明，让别人能得到同样的样本，并说明每一步可能带来什么偏差。

### E128

- 位置：Inter-Rater Reliability and Agreement 补充标准，是否需要多名评分者
- 原文："the more potentially controversial the judgment, the more we need multiple raters"
- 要点：判断越可能有争议，越需要多名评分者。

### E129

- 位置：Inter-Rater Reliability and Agreement 补充标准，必要项
- 原文："describes the process by which two or more raters independently rated properties of research objects" / "describes how disagreements were resolved" / "reports an appropriate statistical measure of IRR/IRA"
- 要点：要描述两名以上评分者如何独立评分、分歧如何解决，并报告合适的一致性统计量。

### E130

- 位置：Inter-Rater Reliability and Agreement 补充标准，Notes
- 原文："IRA is a measure of agreement and can be calculated using (for example) Scott's π, Cohen's κ, Fleiss's κ and Krippendorff's α (for example)."
- 要点：评分者间一致性可以用 Scott's π、Cohen's κ、Fleiss's κ、Krippendorff's α 等统计量计算。

### E131

- 位置：Inter-Rater Reliability and Agreement 补充标准，优秀项
- 原文："reports an iterative process with multiple cycles of (i) rating a subset of the data, (ii) resolving disagreements, and (iii) updating the rating scheme or decision rules until a minimum threshold indicates acceptable reliability/agreement"
- 要点：优秀做法是多轮迭代：先标一部分数据，解决分歧，更新标注方案或判定规则，直到一致性达到最低阈值。

### E132

- 位置：Inter-Rater Reliability and Agreement 补充标准，反面模式
- 原文："Pretending that the IRR or IRA statistic indicates good reliability when it is below established thresholds." / "Calculating multiple IRR/IRA measures and reporting only the most favourable (p-hacking)"
- 要点：一致性低于公认阈值却说成良好，或计算多种一致性指标只报告最好看的那个，都是反面模式。

### E133

- 位置：Ethics (Studies with Secondary Human Data) 补充标准，必要项
- 原文："describes all plausible, non-trivial potential risks or harms to data custodians and data subjects" / "states the grounds on which the data used was legitimately available to the researchers"
- 要点：要描述对数据保管方和数据主体所有可能的、不可忽略的风险或伤害，并说明数据是基于什么依据合法地为研究者所用。

### E134

- 位置：Ethics (Studies with Secondary Human Data) 补充标准，脚注 1
- 原文："the terms of use of a website explicitly permit scraping for the kind of information gathered and for the purposes of research"
- 要点：合法可用的例子：网站的使用条款明确允许为研究目的抓取这类信息。

### E135

- 位置：Ethics (Studies with Secondary Human Data) 补充标准，反面模式
- 原文："Justifying data use as acceptable solely because it is technically available (e.g. machine accessible or downloadable) as opposed to legitimately available"
- 要点：仅以"技术上能拿到（能访问、能下载）"为理由使用数据，而不是"合法可用"，是反面模式。

### E136

- 位置：Ethics (Studies with Secondary Human Data) 补充标准，必要项
- 原文："explains how participants' privacy and reputation was respected in the conduct and reporting of the research. In particular, where multiple datasets are combined, explains how any additional privacy risks raised by this were mitigated."
- 要点：要说明在研究和报告中如何尊重参与者的隐私和声誉；合并多个数据集时，要说明如何缓解由此带来的额外隐私风险。

### E137

- 位置：Ethics (Studies with Secondary Human Data) 补充标准，脚注 6
- 原文："Conditions for reidentification may include quoting ostensibly anonymous data content that can be resolved to its original source (and thus the identity of the originator) through a search engine."
- 要点：引用看似匿名、但能通过搜索引擎找到原始出处（从而找到作者身份）的内容，会造成重新识别。

### E138

- 位置：Ethics (Studies with Secondary Human Data) 补充标准，必要项
- 原文："how any further publication of the data (in existing, combined, or transformed form) will respect the expectations and consent given by data subjects"
- 要点：再次发布数据（原样、合并或变换后）时，要说明如何尊重数据主体的预期和同意。

### E139

- 位置：Open Science 补充标准，加分项与 Notes
- 原文："archives supplementary materials on preserved digital repositories such as" / "personal or institutional websites, version control systems (e.g. GitHub), consumer cloud storage (e.g. Dropbox), and commercial paper repositories (e.g. ResearchGate; Academia.edu) do not offer properly archived and preserved data."
- 要点：补充材料应存档在有长期保存保障的平台（如 Zenodo、figshare、Software Heritage、OSF）；个人网站、GitHub 等版本控制平台、网盘不算妥善存档。

### E140

- 位置：Open Science 补充标准，Invalid Criticisms
- 原文："Researchers should not complain that a study involves artifacts which— for good reasons—cannot be released."
- 要点：有正当理由无法公开的材料，不应成为批评的理由。

### E141

- 位置：General Standard，Initial Checks (Editor)
- 原文："presents new analysis not previously published in a peer-reviewed venue (i.e. preprints are fine)"
- 要点：只要求分析没在同行评审的场合发表过；预印本不算已发表。

### E142

- 位置：General Standard，General Quality Criteria
- 原文："There are no universal quality criteria. Each study should be assessed against quality criteria appropriate for its methodology"
- 要点：没有通用的质量标准，每项研究要用适合其方法的标准来评。

### E143

- 位置：Benchmarking Standard，标题下的定义
- 原文："A study in which a software system is assessed using a standard tool (i.e. a benchmark) for competitively evaluating and comparing methods, techniques or systems"
- 要点：基准评测的定义：用一个标准工具（基准）对方法、技术或系统做竞争性的评估和比较。

### E144

- 位置：Benchmarking Standard，Application
- 原文："investigates software systems within a defined context with an automated, repeatable procedure" / "studies the software system’s quality of service under a specific workload or usage profile"
- 要点：适用条件：在确定的环境中用自动化、可重复的流程研究软件系统；研究的是系统在特定工作负载或使用场景下的服务质量。

### E145

- 位置：Benchmarking Standard，Application
- 原文："If the benchmark experiments primarily study software systems, use this standard." / "Benchmarking is often used with Engineering Research"
- 要点：实验主要研究软件系统本身时用基准评测标准；有人参与的实验、对系统模型的仿真、真实环境中的研究分别用其他标准；基准评测常和工程研究一起使用。

### E146

- 位置：Benchmarking Standard，Essential Attributes
- 原文："EITHER: justifies the selection of an existing, publicly available or standard benchmark (in terms of relevance, timeliness, etc.)"
- 要点：必要项：选用现有的、公开的或标准的基准时，要从相关性、时效性等方面说明理由。

### E147

- 位置：Benchmarking Standard，Essential Attributes
- 原文："OR: defines a new benchmark, including: [...] the quality to be benchmarked (e.g., performance, availability, scalability, security), [...] the metric(s) to quantify the quality, [...] the measurement method(s) for the metric (if not obvious), [...] the workload, usage profile and/or task sample the system under test is subject to"
- 要点：必要项：自建新基准时要定义四部分：要测的质量、量化它的指标、指标的测量方法、被测系统承受的工作负载或任务样本；并说明设计理由，尽量复用已有基准的设计组件。

### E148

- 位置：Benchmarking Standard，Essential Attributes
- 原文："describes the experimental setup for the benchmark in sufficient detail to support independent replication" / "specifies the workload or usage profile in sufficient detail to support independent replication"
- 要点：必要项：实验环境和工作负载都要描述到足以让别人独立复现。

### E149

- 位置：Benchmarking Standard，Essential Attributes
- 原文："allows different configurations of a system under test to compete on their merits without artificial limitations"
- 要点：必要项：被测系统的不同配置要能凭各自实力竞争，不受人为限制。

### E150

- 位置：Benchmarking Standard，Essential Attributes
- 原文："assesses stability or reliability using sufficient experiment repetitions and execution duration"
- 要点：必要项：用足够的重复次数和运行时长评估结果是否稳定。

### E151

- 位置：Benchmarking Standard，Desirable Attributes
- 原文："provides supplementary materials including datasets, analysis scripts and (for novel benchmarks) extended documentation" / "provides benchmark(s) in a usable form that facillitates independent replication"
- 要点：加分项：提供补充材料（数据集、分析脚本、新基准的详细文档），并以可用的形式提供基准，便于独立复现。

### E152

- 位置：Benchmarking Standard，Desirable Attributes
- 原文："uses or creates open source benchmarks" / "transparently reports on problems with executing benchmark runs, if any"
- 要点：加分项：使用或创建开源基准；如实报告运行基准时遇到的问题。

### E153

- 位置：Benchmarking Standard，Desirable Attributes
- 原文："reports on independent replication of the benchmark results" / "reports on a large community that uses the benchmark" / "reports on an independent organization that maintains the benchmark"
- 要点：加分项：报告结果被独立复现过、基准有大的使用者社区、有独立组织维护基准。

### E154

- 位置：Benchmarking Standard，Extraordinary Attributes
- 原文："provides empirical evidence for the relevance of a benchmark, e.g., using a Systematic Review" / "provides empirical evidence for the usability of a benchmark, e.g., using Action Research or Case Studies"
- 要点：优秀项：用实证证据（如系统综述）说明基准的相关性，或（如行动研究、案例研究）说明基准好用。

### E155

- 位置：Benchmarking Standard，General Quality Criteria
- 原文："Fairness of measurements, reproducibility of results across experiment repetitions, benchmarking the *right* aspects, using a realistic benchmark with a representative workload"
- 要点：总体质量标准：测量公平、重复实验结果可复现、测的是"对的"方面、基准真实且工作负载有代表性。

### E156

- 位置：Benchmarking Standard，Examples of Acceptable Deviations
- 原文："the nature of the benchmark requires specialized hardware (e.g. a quantum computer) so it not easy to replicate" / "in a study that replicates published existing work, the description of the experimental setup could be quite brief" / "the study only employs one (or a few) runs because prior work has shown that a single run is sufficient"
- 要点：可接受的偏离：基准需要特殊硬件而难以复现；复现已发表工作时实验环境可以简述；已有研究表明一次运行就够时可以只跑一次或几次。

### E157

- 位置：Benchmarking Standard，Antipatterns
- 原文："Tailoring the benchmark for a specific method, technique or tool, which is evaluated with the benchmark." / "Using benchmarking experiments that are irrelevant for the problem studied to obfuscate weaknesses in the proposed approach"
- 要点：反面模式：为要评估的方法量身定做基准；用和问题无关的基准实验掩盖所提方法的弱点。

### E158

- 位置：Benchmarking Standard，Antipatterns
- 原文："Insufficient repetitions or duration to assess stability of results" / "Collecting aggregated measurements instead of persisting all raw results and running an offline analysis"
- 要点：反面模式：重复次数或运行时长不足；只收集汇总后的测量值，而不是保存全部原始结果再离线分析。

### E159

- 位置：Benchmarking Standard，Invalid Criticisms
- 原文："The benchmark is not widely used." / "Such a proto-benchmark (Sim et al. 2003) can act as a template to further the discussion of the topic and to initialize the consensus process." / "No independent replication of the benchmark results is reported." / "There is no independent organization that maintains the benchmark."
- 要点：不成立的批评：基准用的人不多（小团队先做的"原型基准"可以推动讨论、启动共识）；没有报告独立复现；没有独立组织维护基准。

### E160

- 位置：Engineering Research Standard，定义与 Essential Attributes
- 原文："Research that invents and evaluates technological artifacts" / "in which the artifact is assessed using one or more benchmarks"
- 要点：工程研究是发明并评估技术制品的研究；基准评测是评估制品的几种实证方法之一。

### E161

- 位置：Engineering Research Standard，Essential Attributes
- 原文："empirically compares the artifact to one or more state-of-the-art alternatives" / "empirically compares the artifact to one or more state-of-the-art benchmarks"
- 要点：工程研究的必要项：用实证方法把制品和最先进的替代方案或基准比较（或说明为什么无法比较）。

### E162

- 位置：Experiments 标准，标题下的定义
- 原文："A study in which an intervention is deliberately introduced to observe its effects on some aspects of reality under controlled conditions"
- 要点：实验的定义：在受控条件下有意引入一种干预，观察它对现实某些方面的影响。

### E163

- 位置：Experiments 标准，Application
- 原文："manipulates one or more independent variables" / "controls many extraneous variables" / "applies each treatment independently to several experimental units" / "involves human participants"
- 要点：本标准适用的实验同时满足四个条件：操纵一个或多个自变量；控制许多无关变量；每种处理分别施加到多个实验单元上；有人类参与者。

### E164

- 位置：Experiments 标准，Application
- 原文："In true experiments, experimental units are randomly allocated across treatments; quasi-experiments lack random assignment. Experiments include between-subjects, within-subjects and repeated measures designs. For experiments without human participants, see the **Exploratory Data Science Standard** or the **Engineering Research Standard**."
- 要点：真实验随机分配实验单元，准实验没有随机分配；实验包括被试间、被试内和重复测量设计。没有人类参与者的实验参考数据科学标准或工程研究标准。

### E165

- 位置：Experiments 标准，Essential Attributes
- 原文："states formal hypotheses" / "uses two-sided hypotheses OR justifies use of one-sided hypotheses based on face validity or previous work"
- 要点：必要：写出正式的假设；用双侧假设，或依据表面效度或已有研究说明为什么用单侧假设。

### E166

- 位置：Experiments 标准，Essential Attributes
- 原文："describes the dependent variable(s) and justifies how they are measured (including units, instruments)" / "describes the independent variable(s) and how they are manipulated or measured" / "describes extraneous variables and how they are controlled: physically, statistically, or not at all"
- 要点：必要：说明因变量及其测量方式（单位、工具）和理由；说明自变量及其操纵或测量方式；说明无关变量，以及是用物理方式、统计方式控制还是没有控制。

### E167

- 位置：Experiments 标准，Essential Attributes
- 原文："justifies sample size (e.g. using power analysis)"
- 要点：必要：说明样本量的依据，例如做功效分析。

### E168

- 位置：Experiments 标准，Essential Attributes
- 原文："describes the research design and protocol including treatments, materials, tasks, design (e.g. 2x2 factorial), participant allocation, period and sequences (for crossover designs), and logistics"
- 要点：必要：描述研究设计和流程，包括各处理、材料、任务、设计类型（如 2×2 析因设计）、参与者分配、交叉设计的阶段和顺序，以及实施安排。

### E169

- 位置：Experiments 标准，Essential Attributes
- 原文："EITHER: uses random assignment and explains logistics (e.g. how random numbers were generated)" / "OR: provides compelling justification for not using random assignment and explains how unequal groups threat to validity is mitigated (e.g. using pre-test/post-test and matched subjects design)"
- 要点：必要：要么随机分配并说明怎么做的（如随机数怎么生成）；要么给出不随机分配的有力理由，并说明怎样减轻"各组本来就不同"的威胁（如前测/后测、配对设计）。

### E170

- 位置：Experiments 标准，Essential Attributes 及脚注 1
- 原文："describes experimental objects (e.g. real or toy system) and their characteristics (e.g. size, type)" / "justifies selection of experimental objects; acknowledges object-treatment confounds, if any" / "For example, in an experiment where the control group applies Test-Driven Development (TDD) with Object 1 while the treatment group applies Test-Last-Development (TDD) with Object 2, the experimental object is confounded with the treatment."
- 要点：必要：描述实验对象（真实系统还是玩具系统，规模、类型），说明为什么选它们，承认对象和处理之间的混杂；例如对照组在对象 1 上、实验组在对象 2 上做，对象就和处理混在一起了。

### E171

- 位置：Experiments 标准，Essential Attributes
- 原文："confirms no incentives for participation were offered or describes financial or non-financial incentives"
- 要点：必要：说明没有提供参与激励，或描述提供了哪些金钱或非金钱激励。

### E172

- 位置：Experiments 标准，Essential Attributes（结果部分）
- 原文："describes participants (e.g. age, gender, education, relevant experience or preferences)" / "reports distribution-appropriate descriptive and inferential statistics; justifies tests used" / "reports effects sizes with confidence intervals (if using frequentist approach)"
- 要点：必要：描述参与者（年龄、性别、教育、相关经验或偏好）；报告符合数据分布的描述统计和推断统计，说明检验的选择理由；用频率学派方法时报告效应量及置信区间。

### E173

- 位置：Experiments 标准，Essential Attributes（讨论部分）
- 原文："discusses construct, conclusion, internal, and external validity" / "discusses alternative interpretations of results"
- 要点：必要：讨论构念效度、结论效度、内部效度和外部效度；讨论对结果的其他解释。

### E174

- 位置：Experiments 标准，Desirable Attributes
- 原文："provides supplementary material such as complete, algorithmic research protocol; task materials; raw, de-identified dataset; analysis scripts"
- 要点：加分：提供补充材料，如完整、可照做的研究流程、任务材料、去除身份信息的原始数据、分析脚本。

### E175

- 位置：Experiments 标准，Desirable Attributes 及脚注 3
- 原文："explains deviations between design and execution, and their implications" / "e.g. dropouts affecting balance between treatment and control group."
- 要点：加分：说明执行和设计之间的偏离及其影响，例如中途退出破坏了实验组和对照组的平衡。

### E176

- 位置：Experiments 标准，Desirable Attributes
- 原文："analyzes construct validity of dependent variable" / "reports manipulation checks" / "pre-registration of hypotheses and design (where venue allows)"
- 要点：加分：分析因变量的构念效度；报告操纵检查（确认处理确实按设想起了作用）；在会议或期刊允许时预注册假设和设计。

### E177

- 位置：Experiments 标准，Desirable Attributes
- 原文："discusses alternative experimental designs and why they were not used (e.g. validity trade-offs)" / "includes visualizations of data distributions"
- 要点：加分：讨论其他可选的实验设计以及为什么没用（如效度上的取舍）；把数据分布画出来。

### E178

- 位置：Experiments 标准，Extraordinary Attributes
- 原文："reports multiple experiments or replications in different cultures or regions" / "uses multiple methods of data collection; data triangulation"
- 要点：优秀：报告在不同文化或地区做的多次实验或重复研究；用多种方法收集数据，相互印证。

### E179

- 位置：Experiments 标准，Examples of Acceptable Deviations
- 原文："Sample size is not justified by power analysis a priori because the study is conducted in a classroom in which the number of available participants is fixed."
- 要点：可接受的偏离：在课堂上做实验、可用人数固定时，可以不事先用功效分析论证样本量。

### E180

- 位置：Experiments 标准，Antipatterns
- 原文："using bad proxies for dependent variables (e.g. task completion time as a proxy for task complexity)" / "quasi-experiments without a good reason" / "treatments or response variables are poorly described"
- 要点：反面模式：用不好的替代指标当因变量（如用完成时间代表任务复杂度）；没有充分理由就做准实验；处理或结果变量描述不清。

### E181

- 位置：Experiments 标准，Antipatterns
- 原文："data analysis technique used does not correspond to the design chosen or data characteristics (e.g. using an independent samples t-test on paired data)"
- 要点：反面模式：分析方法和设计或数据特点不匹配，例如对配对数据用独立样本 t 检验。

### E182

- 位置：Experiments 标准，脚注 5
- 原文："Quasi-experiments are appropriate for pilot studies or when assignment is beyond the researcher's control (e.g. assigning students to two different sections of a course). Simply claiming that a study is "exploratory" is not sufficient justification."
- 要点：准实验适用于预研究，或分组不由研究者决定的情况（如学生已分在课程的两个班）；只说研究是"探索性的"不足以作为理由。

### E183

- 位置：Experiments 标准，Invalid criticisms
- 原文："participants are students---appropriateness of participant characteristics should be judged based on the context, desired level of control, trade-off choices between internal and external validity, and the specifics of the technology (i.e. method, technique, tool, process, etc.) under evaluation; the choice must be explained in the paper"
- 要点：不成立的批评："参与者是学生"。参与者是否合适，应结合情境、需要的控制程度、内部与外部效度的取舍、被评估技术的特点来判断；但论文必须解释为什么这样选。

### E184

- 位置：Experiments 标准，Invalid criticisms
- 原文："low external validity" / "the experiment is a replication" / "the reviewer would have investigated the topic in any other way than an experiment" / "not enough participants (unless supported by power analysis)" / "not employing an incentivization scheme"
- 要点：不成立的批评：外部效度低；实验是重复研究；审稿人想用实验以外的方法研究；参与者不够多（除非有功效分析支持）；没有采用激励方案。

### E185

- 位置：Ethics (Studies with Human Participants) 补充标准，Essential Attributes
- 原文："explains how participants were recruited" / "explains the compensation (if any) offered for participation and how coercion was mitigated"
- 要点：必要：说明怎样招募参与者，给了什么报酬，怎样避免强迫。

### E186

- 位置：Ethics (Studies with Human Participants) 补充标准，脚注 1
- 原文："If a gatekeeper was involved in recruitment, also explains how the gatekeeper was recruited, informed, and consented, and how power relationships between gatekeeper and individual participant were mitigated to ensure free individual informed consent."
- 要点：如果招募经过"把关人"（如经理、任课教师），还要说明把关人和参与者之间的权力关系是怎样被化解的，以保证参与者自由、个人的知情同意。

### E187

- 位置：Ethics (Studies with Human Participants) 补充标准，脚注 7
- 原文："Participants must: (1) be debriefed in terms of the data captured and the reasons for deception, and (2) be offered the opportunity to withdraw themselves and their data at that point."
- 要点：研究用到欺骗时，事后必须向参与者说明采集了哪些数据、为什么要欺骗，并给他们撤回自己和数据的机会。

### E188

- 位置：Data Science 标准，定义
- 原文："Studies that analyze software engineering phenomena or artifacts using data-centric analysis methods such as machine learning or other computational intelligence approaches as well as search-based approaches"
- 要点：数据科学研究用机器学习等以数据为中心的分析方法（也包括其他计算智能方法和基于搜索的方法）来分析软件工程现象或制品。

### E189

- 位置：Data Science 标准，Application
- 原文："Applies to studies that primarily analyze existing software phenomena using predictive, preemptive or corrective modelling." / "If the analysis focuses on the toolkit, rather that some new conclusions generated by the toolkit, consider the **Artifacts Standard**"
- 要点：适用于主要用预测性、预防性或纠正性建模分析已有现象的研究；如果重点是工具本身而不是工具得出的新结论，应参考制品标准。

### E190

- 位置：Data Science 标准，必要项
- 原文："explains how and why the data was selected" / "explains how the data was pre-processed, filtered, and categorized"
- 要点：必须说明数据是怎样选出来的、为什么选它，以及数据怎样预处理、过滤和分类。

### E191

- 位置：Data Science 标准，必要项
- 原文："EITHER: discusses state-of-art baselines (and their strengths, weaknesses and limitations)" / "OR: explains why no state-of-art baselines exist" / "OR: provides compelling argument that direct comparisons are impractical"
- 要点：必须讨论当前最好的基线（及其优缺点和局限），或说明为什么没有这样的基线，或有力地论证无法直接比较。

### E192

- 位置：Data Science 标准，必要项
- 原文："describes and justifies the evaluation metrics used" / "goes beyond single-dimensional summaries of performance (e.g., average; median) to include measures of variation, confidence, or other distributional information"
- 要点：必须说明并论证所用的评估指标；结果不能只给平均数或中位数，还要给出波动、置信度或其他分布信息。

### E193

- 位置：Data Science 标准，必要项
- 原文："describes the feature engineering approaches" / "defines the modeling approach(es) used (e.g. clustering then decision tree learning), typically using pseudocode" / "discusses the hardware and software infrastructure used"
- 要点：必须描述特征工程方法、建模方法（通常用伪代码），以及所用的硬件和软件环境。

### E194

- 位置：Data Science 标准，必要项
- 原文："justifies all statistics and (automated or manual) heuristics used" / "discusses technical assumptions and threats to validity that are specific to data science"
- 要点：必须论证用到的每个统计量和启发式规则，并讨论数据科学特有的技术假设和效度威胁。

### E195

- 位置：Data Science 标准，加分项
- 原文："provides a replication package including source code and data set(s), or if data cannot be shared, synthetic data to illustrate the use of the algorithms"
- 要点：提供包含源代码和数据集的复现包；数据不能公开时，提供合成数据来演示算法用法。

### E196

- 位置：Data Science 标准，加分项
- 原文："data is processed by multiple learners, of different types"
- 要点：用多种不同类型的学习算法处理数据。

### E197

- 位置：Data Science 标准，加分项
- 原文："data is processed multiple times with different, randomly selected, training/test examples; the results of which are compared via significance tests and effect size tests (e.g. cross-validation)"
- 要点：用不同的随机训练/测试划分多次处理数据（例如交叉验证），并用显著性检验和效应量检验比较结果。

### E198

- 位置：Data Science 标准，加分项
- 原文："carefully selects the hyperparameters that control the data miners (e.g. via analysis of settings in related work or some automatic hyperparameter optimizer such as grid search)"
- 要点：认真选择超参数，例如参考相关工作中的设置，或用网格搜索等自动超参数优化方法。

### E199

- 位置：Data Science 标准，加分项
- 原文："manually inspects some non-trivial portion of the data (i.e. data sanity checks)"
- 要点：人工检查相当一部分数据，做数据合理性检查。

### E200

- 位置：Data Science 标准，加分项及脚注 8
- 原文："clearly distinguishes evidence-based results from interpretations and speculation" / "Simply separating results and discussion into different sections is typically sufficient. No speculation in the results section."
- 要点：清楚区分有证据的结果和解读、推测；通常把结果和讨论分成两节就够了，结果一节里不写推测。

### E201

- 位置：Data Science 标准，优秀项
- 原文："leverages temporal data via longitudinal analyses" / "triangulates with qualitative data analysis of selected samples of the data" / "triangulates with other data sources, such as surveys or interviews" / "shares findings with and solicits feedback from the creators of the (software) artifacts being studied"
- 要点：优秀项包括：用纵向分析利用时间数据；对选出的样本做定性分析来相互印证；用问卷、访谈等其他数据来源相互印证；把发现告诉被研究制品的创建者并征求反馈。

### E202

- 位置：Data Science 标准，可接受的偏离
- 原文："Using lighter and less precise data processing (e.g. keyword matching or random subsampling) if the scale of data is too large for a precise analysis to be practical." / "Data not shared because it is impractical (e.g. too large) or unethical (e.g. too sensitive)." / "Not all studies need statistics and hypotheses. Some studies can be purely or principally descriptive."
- 要点：可接受的偏离：数据规模太大时用较粗的处理方法（如关键词匹配、随机抽样）；数据太大或太敏感时不公开；有的研究可以只做描述，不需要统计检验和假设。

### E203

- 位置：Data Science 标准，反面模式
- 原文："Claiming causation without not only establishing covariaton and precedence but also eliminating third variable explanations and at least hypothesizing a generative mechanism."
- 要点：声称因果关系之前，不仅要确立共变和先后顺序，还要排除第三变量的解释，并至少提出一个产生机制的假设；做不到就声称因果，是反面模式。

### E204

- 位置：Data Science 标准，反面模式
- 原文："Pre-processing changes training and test data; e.g. while it may be useful to adjust training data class distributions via (say) sub-sampling of majority classes, that adjustment should not applied to the test data"
- 要点：预处理不能同时改动训练数据和测试数据；例如可以对训练数据的多数类做下采样来调整类别比例，但测试数据不能这样调整，要保持"真实世界"中的样子。

### E205

- 位置：Data Science 标准，反面模式
- 原文："Using statistical tests without checking their assumptions." / "Significance tests without effect size tests; effect sizes without confidence intervals." / "Reporting a median, without any indication of variance (e.g., a boxplot)."
- 要点：反面模式：不检查前提假设就用统计检验；只做显著性检验不报效应量，或报效应量不给置信区间；只报中位数不给波动信息。

### E206

- 位置：Data Science 标准，不成立的批评
- 原文："You should have analyzed data ABC. The question reviewers should ask is whether the papers main claims are supported by the data that was analyzed, not whether some other data would have been better." / "Does not have a reproduction package. These are desirable, not essential (yet)." / "Study does not make causal claims, when it cannot."
- 要点：不成立的批评："你应该分析另一份数据"（该问的是主张是否被所分析的数据支持）；"没有复现包"（目前是加分项，不是必要项）；"研究没有做因果主张"（做不了就不该做）。

### E207

- 位置：Data Science 标准，必要项
- 原文："explains why it is timely to investigate the proposed problem using the proposed method"
- 要点：必须说明为什么现在适合用所提的方法研究这个问题。

### E208

- 位置：Replication Standard，标题下的定义
- 原文："A study that deliberately repeats a previous study (the "original study") to determine whether its results can be reproduced"
- 要点：复现研究的定义：有意重复一项先前的研究（原研究），以确定它的结果能否再次得到。

### E209

- 位置：Replication Standard，Application
- 原文："The replication attempt is deliberate and planned, not accidental overlap with a previous study." / "The original study is clearly identified as a separate previous publication."
- 要点：适用条件：复现是有意、有计划的，而不是碰巧和先前研究重叠；原研究必须是明确指出的另一篇已发表论文。

### E210

- 位置：Replication Standard，Definitions
- 原文："To reproduce [...] means to repeat the original study's data analysis on the original study's data." / "To replicate [...] means to repeat a study by collecting new data and repeating the original study's analysis on the new data."
- 要点：SIGSOFT 的用法：reproduce 指在原数据上重做原分析；replicate 指收集新数据，再在新数据上重做原分析。（原文中的术语带有指向 SIGSOFT 术语表的链接，引文用 [...] 省略了链接。）

### E211

- 位置：Replication Standard，脚注 1
- 原文："Exact replication: same research questions, same method, same context. Methodological replication: same research questions, same method, different context. Conceptual replication: same research questions, different method, different context."
- 要点：按方法相似度分三类：精确复现（问题、方法、情境都相同）；方法复现（问题和方法相同，情境不同）；概念复现（问题相同，方法和情境都不同）。

### E212

- 位置：Replication Standard，脚注 2
- 原文："Partial replication: addresses a subset of the original research questions. Complete replication: addresses each of the original reseach questions. Extended replication: addresses each of the original reseach questions and additional ones."
- 要点：按覆盖范围分三类：部分复现（只回答原研究的一部分问题）；完整复现（回答全部原问题）；扩展复现（回答全部原问题，再加上新问题）。

### E213

- 位置：Replication Standard，脚注 3
- 原文："Internal replication: the replicating team is the same as the original study's team. External replication: the replicating team is different from the original study's team. Mixed replication: overlaps exist between the replicating team and the original study's team."
- 要点：按团队分三类：内部复现（同一团队）；外部复现（不同团队）；混合复现（两个团队有重叠）。

### E214

- 位置：Replication Standard，Essential Attributes
- 原文："discusses the motivation for conducting the replication in appropriate detail (e.g., to validate the results, to broaden the results by changing the participant pool or the artifacts)"
- 要点：必要项：说明为什么做这次复现，例如验证结果，或通过更换参与者、制品来扩大结果的适用范围。

### E215

- 位置：Replication Standard，Essential Attributes
- 原文："defines the type of the replication by methodological similarity (exact, methodological, conceptual)" / "defines the type of the replication by overlap (partial, complete, extended)" / "defines the type of the replication by participants (internal, external, mixed)"
- 要点：必要项：从方法相似度、覆盖范围、团队三个角度写明这是哪一类复现。

### E216

- 位置：Replication Standard，Essential Attributes
- 原文："the research questions of the original study" / "the design of the original study" / "the context variables of the original study that might have affected the design of the study or interpretation of the results" / "the major findings of the original study"
- 要点：必要项：充分描述原研究，包括研究问题、设计、参与者、制品、可能影响设计或结果解读的情境变量、主要发现。

### E217

- 位置：Replication Standard，Essential Attributes
- 原文："EITHER: describes overlap or interactions with the original study author(s),"
- 要点：必要项：要么描述与原作者的重叠或互动，要么确认原作者没有参与。

### E218

- 位置：Replication Standard，Essential Attributes
- 原文："describes and justifies any differences from the original study (design, participants, artifacts, procedures, data collection, or analysis)"
- 要点：必要项：描述与原研究的每一处不同（设计、参与者、制品、流程、数据收集或分析），并说明理由。

### E219

- 位置：Replication Standard，Essential Attributes
- 原文："compares the results of the replication to the results of the original study" / "clearly differentiates between results that are consistent and inconsistent with the original study"
- 要点：必要项：把复现结果与原研究结果对比，并清楚区分哪些一致、哪些不一致。

### E220

- 位置：Replication Standard，Desirable Attributes
- 原文："clearly seperates information about (i) the original study, (ii) the replication, (iii) the comparison of results, and (iv) conclusions"
- 要点：加分项：把原研究、本次复现、结果对比、结论四部分信息清楚分开。

### E221

- 位置：Replication Standard，Desirable Attributes
- 原文："improves on the original study in some way (e.g., design, analysis, statistical power)"
- 要点：加分项：在某方面改进原研究，例如设计、分析或统计功效（研究检测出真实效应的能力，通常随样本量增大而提高）。

### E222

- 位置：Replication Standard，Desirable Attributes
- 原文："differentiates between minor and major differences when discussing inconsistent results, elaborates on whether the differences are reasonable and/or expected"
- 要点：加分项：讨论不一致的结果时，区分小差异和大差异，并分析这些差异是否合理、是否在预料之中。

### E223

- 位置：Replication Standard，Desirable Attributes
- 原文："draws conclusions across the two (or more) studies; provides insights that would not have been evident from either study individually" / "highlights any conclusions of the original study that were strengthened"
- 要点：加分项：综合两项（或多项）研究下结论，给出单看任何一项都看不出的认识；指出原研究的哪些结论得到了加强。

### E224

- 位置：Replication Standard，Desirable Attributes
- 原文："compares the limitations of the replication to the limitations of the original study" / "proposes hypotheses about new context variables that may have become evident through the analysis of multiple studies"
- 要点：加分项：比较复现与原研究各自的局限；提出综合多项研究后才显现的新情境变量假设。

### E225

- 位置：Replication Standard，Desirable Attributes
- 原文："protocol of the replication was checked/reviewed by the original authors"
- 要点：加分项：复现方案经原作者检查或审阅过。

### E226

- 位置：Replication Standard，Desirable Attributes（for families of replications）
- 原文："provides a brief summary of the previous studies and replications, including information about how the studies were related, conclusions drawn and current state of knowledge about the topic" / "places the results into the context of the entire family of studies"
- 要点：加分项（复现家族）：简要总结之前的研究和复现，并把本次结果放到整个家族中看。

### E227

- 位置：Replication Standard，Antipatterns
- 原文："replicating an underpowered study with a second, equally-underpowered study" / "repeating rather than correcting mistakes (e.g. using inappropriate statistical tests) in the original study"
- 要点：反面做法：用一项同样统计功效不足的研究去复现一项功效不足的研究；照搬而不是纠正原研究的错误（例如用了不合适的统计检验）。

### E228

- 位置：Replication Standard，Invalid Criticisms
- 原文："The replication merely confirms the findings of the original study; no inconsistencies are reported."
- 要点：不成立的批评：复现"只是"证实了原研究的发现，没有发现不一致。

### E229

- 位置：Replication Standard，Invalid Criticisms
- 原文："Failing to publish (e.g., in a replication package) materials owned by the original study authors who have not given permission to publish them."
- 要点：不成立的批评：没有公开属于原作者、且原作者未允许公开的材料。

### E230

- 位置：Replication Standard，Invalid Criticisms
- 原文："Criticizing the research questions including their wording or formulation (since the research questions are set in the original study, the replication must follow them, even in conceptual replications)."
- 要点：不成立的批评：批评研究问题本身或其措辞；研究问题由原研究确定，复现必须沿用，概念复现也一样。

### E231

- 位置：Questionnaire Surveys 标准，定义
- 原文："A study in which a sample of respondents answer a series of (mostly structured) questions, typically through a computerized or paper form"
- 要点：问卷调查是让一批受访者回答一系列（大多是结构化的）问题的研究，通常通过电子或纸质表单进行。

### E232

- 位置：Questionnaire Surveys 标准，Application
- 原文："a sample of participants answer predefined, mostly closed-ended questions (typically online or on paper)" [...] "researchers systematically analyze participants' answers"
- 要点：适用于参与者回答事先定好的、以封闭式为主的问题，研究者系统地分析回答的研究。

### E233

- 位置：Questionnaire Surveys 标准，Application
- 原文："This standard does not apply to questionnaires comprising predominately open-ended questions"
- 要点：以开放式问题为主的问卷不适用本标准。

### E234

- 位置：Questionnaire Surveys 标准，Variations
- 原文："provide a detailed account of the properties of a phenomenon or population." [...] "generate insights, hypotheses or models for further research." [...] "testing formal (e.g. causal) propositions to explain a phenomenon."
- 要点：问卷调查分三种：描述性（详细描述现象或总体的特征）、探索性（为后续研究产生见解、假设或模型）、验证性（检验正式的、例如因果的命题）。

### E235

- 位置：Questionnaire Surveys 标准，Essential Attributes
- 原文："identifies the target population and defines the sampling strategy" [...] "describes how participants were selected or recruited (e.g. sampling frame, advertising, invitations, incentives)"
- 要点：必要项：明确目标总体、定义抽样策略；说明怎样选出或招募参与者（抽样框、广告、邀请、激励）。

### E236

- 位置：Questionnaire Surveys 标准，Essential Attributes
- 原文："EITHER: measures constructs using (or adapting) validated scales OR: analyzes construct validity (including content, convergent, discriminant and predictive validity) ex post"
- 要点：必要项：要么用（或改编）经过验证的量表测量构念，要么事后分析构念效度（内容、聚合、区分和预测效度）。

### E237

- 位置：Questionnaire Surveys 标准，Essential Attributes
- 原文："describes how responses were managed/monitored, including contingency actions for non-responses and drop-outs" [...] "explains handling of missing data (e.g. imputation, weighting adjustments, discarding)"
- 要点：必要项：说明怎样管理和监控回收情况，包括对不回应和中途退出的应对措施；说明怎样处理缺失数据（插补、加权调整、丢弃）。

### E238

- 位置：Questionnaire Surveys 标准，Essential Attributes
- 原文："analyzes response rates" [...] "assesses sufficiency of number of participants (statistical power)"
- 要点：必要项：分析回应率；评估参与人数是否足够（统计功效）。

### E239

- 位置：Questionnaire Surveys 标准，Essential Attributes
- 原文："acknowledges generalizability threats; discusses how respondents may differ from target population"
- 要点：必要项：承认可推广性方面的威胁，讨论回答者可能与目标总体有什么不同。

### E240

- 位置：Questionnaire Surveys 标准，Essential Attributes 及脚注 3
- 原文："provides the questionnaire instrument (as an appendix or supplementary materials)" [...] "the questionnaire design matches the research aims and the target population" [...] "Questions are mapped to research objectives and their wording and format is appropriate for their audience."
- 要点：必要项：提供问卷原件（附录或补充材料）；问卷设计与研究目标和目标总体相符，即每道题对应研究目标，措辞和格式适合回答者。

### E241

- 位置：Questionnaire Surveys 标准，Desirable Attributes
- 原文："includes mechanisms to detect participants using AI or other automated means to answer questions; excludes AI-generated responses" [...] "includes attention-check items in the questionnaire; excludes participants who fail one or more of these checks"
- 要点：加分项：设法识别用 AI 或其他自动手段作答的参与者并排除；加入注意力检查题，排除没通过的参与者。

### E242

- 位置：Questionnaire Surveys 标准，Desirable Attributes
- 原文："validates whether the instrument's items, layout, duration, and technology are appropriate (e.g. using pilots, test-retest, or expert and non-expert reviews)" [...] "reports how the instrument has evolved through the validation process (if at all)"
- 要点：加分项：检验问卷的题目、版式、时长和技术是否合适（预调查、重测、专家和非专家评审）；报告问卷在检验过程中怎样修改。

### E243

- 位置：Questionnaire Surveys 标准，Desirable Attributes
- 原文："analyzes response bias (quantitatively)" [...] "applies techniques for improving response rates (e.g. incentives, reminders, targeted advertising)"
- 要点：加分项：定量分析回应偏差；用激励、提醒、定向宣传等办法提高回应率。

### E244

- 位置：Questionnaire Surveys 标准，Desirable Attributes
- 原文："discusses possible effects of incentives (e.g. on voluntariness, response rates, response bias) if used"
- 要点：加分项：用了激励时，讨论它对自愿性、回应率和回应偏差可能的影响。

### E245

- 位置：Questionnaire Surveys 标准，Desirable Attributes
- 原文："provides supplementary materials including instrument(s), code books, analysis scripts and dataset(s)" [...] "accounts for the principles of research ethics (e.g. informed consent, re-identification risk)"
- 要点：加分项：提供问卷、编码手册、分析脚本和数据集等补充材料；考虑研究伦理原则（知情同意、被重新识别的风险）。

### E246

- 位置：Questionnaire Surveys 标准，Extraordinary Attributes
- 原文："provides feasibility check of the anticipated data analysis techniques" [...] "reports on the scale validation in terms of dimensionality, reliability, and validity of measures"
- 要点：优秀项：事先检查计划的分析方法是否可行；从维度、信度和效度三方面报告量表验证结果。

### E247

- 位置：Questionnaire Surveys 标准，Examples of Acceptable Deviations
- 原文："Ommitting part of a questionnaire instrument from supplementary materials due to copyright issues (in which case the paper should cite the source of the questions)" [...] "Doesn't describe handling of drop-outs or missing data because there were none"
- 要点：可接受的偏离：因版权原因不公开部分题目（但要引用题目来源）；没有中途退出或缺失数据时不必描述其处理。

### E248

- 位置：Questionnaire Surveys 标准，Invalid Criticism
- 原文："Not reporting response rate for open public subscription surveys" [...] "Failure to release full data sets despite the data being sensitive." [...] "Claiming the sample size is too small without justifying why the sample size is insufficient to answer the research questions." [...] "Criticizing the relevance of a survey on the basis that responses only capture general people's perceptions."
- 要点：不成立的批评：公开链接、任何人都能填的问卷没报告回应率；数据敏感而没有公开完整数据；不说明理由就说样本太小；以"只反映了人们的看法"为由否定问卷的价值。

### E249

- 位置：Questionnaire Surveys 标准，Invalid Criticism
- 原文："The results are considered controversial or hardly surprising." [...] "The results do not accord with the reviewer's personal experience or previous studies."
- 要点：不成立的批评：结果有争议或不出人意料；结果与审稿人的个人经验或以往研究不一致。

### E250

- 位置：Sampling Supplement，Desirable Attributes
- 原文："online survey: using respondent-driven rather than snowball sampling"
- 要点：加分项：在线问卷用应答者驱动抽样，而不是简单的滚雪球抽样。

### E251

- 位置：Sampling Supplement，Antipatterns
- 原文："making claims about a population, based on sample, without providing an argument for representativeness"
- 要点：反面做法：根据样本对总体下结论，却不论证样本的代表性。

### E252

- 位置：Sampling Supplement，Invalid Criticisms
- 原文："abstractly criticizing generalizability rather than pointing to best practices; e.g. complaining that the results may not generalize (bad) instead of pointing out that participation reminders should have been sent to mitigate response bias (good);"
- 要点：不成立的批评：抽象地质疑可推广性，而不指出具体该做的事；例如应该指出"本该发提醒以减轻回应偏差"，而不是笼统地说"结果可能无法推广"。

### E253

- 位置：Ethics (Studies with Human Participants) Supplement，脚注 2
- 原文："careful consideration of the reidentification potential through others combining multiple data sources (such as social media, or contextual information like company plus job role)"
- 要点：保护隐私时要考虑别人把多个来源（社交媒体，或"公司 + 职位"这类背景信息）拼起来、重新认出参与者的可能。

### E254

- 位置：Ethics (Studies with Human Participants) Supplement，Invalid Criticisms
- 原文："is not a valid criticism where consent was given orally or implied (e.g., by completing a questionnaire that is explicitly part of a research project)."
- 要点：口头同意或默示同意（例如填写一份明确说明属于研究项目的问卷）时，"没有用同意书"不构成有效批评。

### E255

- 位置：Ethics (Studies with Human Participants) Supplement，Essential Attributes
- 原文："explains the compensation (if any) offered for participation and how coercion was mitigated"
- 要点：必要项：说明给参与者的报酬（如有），以及怎样避免强迫。

### E256

- 位置：Qualitative Surveys (Interview Studies) 标准，定义
- 原文："Research comprising semi-structured or open-ended interviews"
- 要点：定性调查（访谈研究）是由半结构化或开放式访谈构成的研究，与问卷调查分属不同的标准。

### E257

- 位置：Longitudinal 标准，定义与 Application
- 原文："A study focusing on the changes in and evolution of a phenomenon over time" / "This standard applies to studies that involve repeated observations of the same variables (e.g., productivity or technical debt) over a period of time. Longitudinal studies include the analysis of datasets over time, such as the analysis of the evolution of the code."
- 要点：纵向研究关注一个现象随时间的变化和演进，对同一批变量（如生产率、技术债）在一段时间内重复观察；分析代码演化这类随时间变化的数据集也属于纵向研究。

### E258

- 位置：Longitudinal 标准，Application
- 原文："Longitudinal studies require to maintain identifiability of subjects (humans or artifacts) between data collection waves and to use at least two waves." / "For cross-sectional analysis, consider the **Exploratory Data Science Standard** or the **Experiments Standard** (if variables are manipulated)."
- 要点：纵向研究要求研究对象（人或制品）在各轮数据收集之间能被识别、对上号，且至少有两轮；只看一个时间点的横断面分析应参考探索性数据科学标准，操纵变量的应参考实验标准。

### E259

- 位置：Longitudinal 标准，必要项及脚注 1
- 原文："determines the appropriate number of waves based on the natural oscillation of the research phenomenon" / "uses at least two data collection waves" / "subjects (humans or artifacts) are identifiable between waves"
- 要点：必要项：根据现象的自然变化节律确定观测轮数；至少两轮；对象在各轮之间可识别。

### E260

- 位置：Longitudinal 标准，必要项及脚注 2、3
- 原文："justifies the data analysis strategy" / "the data analysis strategy is appropriate for the interdependent nature of the data"
- 要点：必要项：论证所用的分析策略，并且分析方法要适合纵向数据前后相依的特点。

### E261

- 位置：Longitudinal 标准，必要项脚注 4
- 原文："Typically, longitudinal analyses deal with many variables and multiple comparisons, increasing the likelihood to obtain results within traditionally acceptable thresholds. For this reason, authors are advised to adjust the critical alpha level [...] or use Bayesian statistics"
- 要点：纵向分析通常涉及很多变量和多次比较，更容易碰巧得到"显著"结果，因此建议调整显著性阈值（例如 p < 0.001）或使用贝叶斯统计。

### E262

- 位置：Longitudinal 标准，必要项
- 原文："justifies sample size (e.g. using power analysis)" / "describes data loss throughout the different waves" / "explains how missing data are handled"
- 要点：必要项：论证样本量（例如用统计功效分析）；描述各轮之间的数据流失；说明缺失数据如何处理。

### E263

- 位置：Longitudinal 标准，必要项及脚注 6、7
- 原文："describes the subjects (e.g., demographic information in the case of humans)" / "discusses the operationalization of the research model (i.e. construct validity)" / "which type of quality controls have been performed on software repositories to ensure the consistency and homogeneity of artifacts?"
- 要点：必要项：描述研究对象，讨论概念是怎样变成可测量指标的（构念效度）；脚注举例，以软件仓库为对象时要说明做了哪些质量控制来保证制品的一致性和同质性。

### E264

- 位置：Longitudinal 标准，加分项
- 原文："investigates causality using the longitudinal nature of the data to establish precedence and statistically controlling for third-variable explanations" / "discusses potential confounding factors (for inferential analyses) that cannot be statistically controlled"
- 要点：加分项：利用纵向数据确立"谁先谁后"，并在统计上控制第三变量，以此考察因果关系；讨论无法用统计控制的潜在混杂因素。

### E265

- 位置：Longitudinal 标准，加分项
- 原文："discusses data (in)consistency across waves (e.g. test-retest reliability)" / "examines differences in distributions between waves (and uses an appropriate data analysis strategy)"
- 要点：加分项：讨论各轮数据是否一致（例如重测信度），检查各轮之间数据分布的差异。

### E266

- 位置：Longitudinal 标准，加分项及脚注 8
- 原文："addresses survivorship bias" / "For example, if you analyze the past 100 years of stock market performance based on the markets that exist today, you get much higher average returns than if you analyze all the markets that existed 100 years ago."
- 要点：加分项：处理幸存者偏差。例子：只用今天还存在的股市分析过去 100 年的表现，得到的平均回报会远高于分析 100 年前存在的所有股市。

### E267

- 位置：Longitudinal 标准，加分项
- 原文："provides supplementary materials including data sets, data collection scripts or instruments, analytical scripts, a description of how to reproduce the work and any other materials used" / "describes the cost of gathering data and any incentives used"
- 要点：加分项：提供数据集、采集脚本或工具、分析脚本和复现说明等补充材料；说明收集数据的成本和使用的激励。

### E268

- 位置：Longitudinal 标准，优秀项
- 原文："uses a multi-stage selection process to identify the study's subjects" / "follows subjects for an exceptionally long period (e.g. more than five years)"
- 要点：优秀项：用多阶段筛选流程确定研究对象；跟踪对象的时间特别长（例如超过五年）。

### E269

- 位置：Longitudinal 标准，General Quality Criteria
- 原文："Longitudinal studies exploit the temporal nature of data to maximize internal validity. Other criteria are sometimes sacrificed to improve internal validity."
- 要点：纵向研究利用数据的时间属性来尽量提高内部效度，有时会为此牺牲其他质量标准。

### E270

- 位置：Longitudinal 标准，反面模式
- 原文："subject loss between waves is too high, leading to a severely underpowered study" / "the period between waves does not match the phenomenon's natural cycles" / "treating longitudinal data as cross-sectional"
- 要点：反面模式：各轮之间对象流失过多，导致统计功效严重不足；观测间隔与现象的自然周期不匹配；把纵向数据当成横断面数据来分析。

### E271

- 位置：Longitudinal 标准，Variations
- 原文："_Experience sampling_ provides a highly specific understanding of a phenomenon through multiple repeated measurements per day over a short period (typically one to three weeks). It emphasizes in-the-moment assessment rather than reflective assessment" / "_Cohort studies_ are a type of analytical observational study where researchers investigate the relationship between an independent and dependent variable by observing subjects over time and comparing groups with different levels of exposure. Cohort studies follow more strict rules than presented here."
- 要点：两种变体：经验取样（在一到三周内每天多次测量，强调记录当下而不是事后回想）；队列研究（随时间观察对象，比较暴露程度不同的组），队列研究有比本标准更严格的规则。

### E272

- 位置：Longitudinal 标准，Invalid Criticisms
- 原文："Claiming that the time span between measurements is too short or too long." / "Claiming that the number of waves is inadequate without a reasoned explanation." / "Claiming that the sample size is too small without performing a _post hoc_ power calculation."
- 要点：不成立的批评：笼统地说测量间隔太短或太长；不给理由地说轮数不够；不做事后功效计算就说样本太小。

### E273

- 位置：Longitudinal 标准，Invalid Criticisms
- 原文："Claiming that the paper with a modest number of comparisons should have used more conservative alphas or adopted a Bayesian approach." / "Complaining about generalizability when the paper clearly acknowledges limitations to generalizability."
- 要点：不成立的批评：比较次数不多时要求用更保守的显著性阈值或贝叶斯方法；论文已明确承认推广性局限时，仍抱怨推广性。

### E274

- 位置：Multi-Methodology and Mixed Methods 标准，定义
- 原文："Studies that use two or more approaches to data collection or analysis to corroborate, complement and expand research findings (multi-methodology) or combine and integrate inductive research with deductive research (mixed methods), often but not necessarily relying on qualitative and/or quantitative data."
- 要点：多方法研究用两种及以上的数据收集或分析方式来印证、补充和扩展研究发现；混合方法研究把归纳式研究和演绎式研究结合并整合起来，常常但不一定涉及定性和定量数据。

### E275

- 位置：Multi-Methodology and Mixed Methods 标准，Application
- 原文："It enumerates criteria related to the mixing of methodologies, not the methodologies themselves. For the latter, refer to method-specific standards. For example, a multi-methodology study combining a case study with an experiment should comply with **The Case Study Standard** and **The Experiment Standard** as well as this standard."
- 要点：本标准只管"怎么混合"，不管各方法本身；每个组成部分还要满足各自方法的标准，例如案例研究加实验的研究，要同时符合案例研究标准、实验标准和本标准。

### E276

- 位置：Multi-Methodology and Mixed Methods 标准，必要项
- 原文："**justifies** using multiple methodologies and/or methods" / "provides a **purpose statement** that conveys the overarching multi or mixed method design intent (why)" / "describes the **multi-methodology**, **multi-method** or **mixed method** design (what)" / "describes **which phases** of the research study the different methods or methodologies are used in (when)" / "describes how the design aligns with the research question or objective"
- 要点：必要项：论证为什么要用多种方法；用一段目的陈述说明总体设计意图（为什么）；描述设计（是什么）；说明各方法用在研究的哪个阶段（何时）；说明设计怎样对应研究问题。

### E277

- 位置：Multi-Methodology and Mixed Methods 标准，必要项及脚注 1
- 原文："**integrates the findings** from all methods to address the research question/objective" / "acknowledges the **limitations** associated with integrating findings" / "e.g., samples that are drawn from different populations may introduce limitations when the findings are integrated, or biases may be introduced by the sequential or parallel nature of a mixed design"
- 要点：必要项：把所有方法的发现整合起来回答研究问题；承认整合带来的局限，例如各部分样本来自不同总体，或先后、并行的设计本身引入的偏差。

### E278

- 位置：Multi-Methodology and Mixed Methods 标准，加分项
- 原文："**defines** the multi-methodology or mixed method design used" / "describes and justifies **sample reuse** (or no reuse, or partial reuse) across methods" / "illustrates the research design using a **visual model** (diagram)" / "indicates the use of multiple methods or mixed method design in the **title**"
- 要点：加分项：给出所用设计的定义；说明并论证各方法之间是否复用样本；用图展示研究设计；在标题中表明使用了多方法或混合方法。

### E279

- 位置：Multi-Methodology and Mixed Methods 标准，加分项
- 原文："**distinguishes the additional value** from using a multi-methodology or mixed method design in terms of corroboration, complementarity, and expansion (breadth and depth)" / "discusses **discrepancies and incongruent findings** from the use of multiple methods"
- 要点：加分项：说清混合带来的额外价值，是印证、互补还是扩展（广度和深度）；讨论不同方法之间的分歧和不一致的发现。

### E280

- 位置：Multi-Methodology and Mixed Methods 标准，加分项
- 原文："describes the main **philosophical, epistemological, and/or theoretical foundations** that the authors use and relate those to the planned use of multi or mixed methods in the study" / "describes the **challenges** faced in the design and how those were or could be mitigated" / "describes **ethical issues** that may have been presented through the blend of multi- or mixed methods"
- 要点：加分项：说明研究的哲学、认识论或理论基础及其与混合设计的关系；描述设计中遇到的困难及缓解办法；讨论方法混合带来的伦理问题。

### E281

- 位置：Multi-Methodology and Mixed Methods 标准，General Quality Criteria
- 原文："General quality criteria discussed in the guidelines for each method should be considered.  In the case of a multi-methodology or multi-method design, the reliability of the findings that are specific to the triangulation goals should be assessed."
- 要点：各方法自己的质量标准都要考虑；对多方法设计，还要评估与三角验证目标相关的发现是否可靠。

### E282

- 位置：Multi-Methodology and Mixed Methods 标准，反面模式
- 原文："**Smoke and mirrors:** Overselling a study as a multi-methodology or mixed method design when one approach at best offers a token or anecdotal contribution to the research motivation or findings" / "**Selling your soul:** Employing an additional method to appeal to a methodological purist during the review process that does not contribute substantively to the research findings"
- 要点：反面模式："障眼法"：其中一种方法只起点缀作用，却把研究包装成混合方法；"出卖灵魂"：为迎合审稿人而加一个对发现没有实质贡献的方法。

### E283

- 位置：Multi-Methodology and Mixed Methods 标准，反面模式
- 原文："**Uninvited guest:** A research method is not clearly introduced in the paper introduction/methodology and makes an unexpected entrance in the discussion or limitations sections of the paper" / "**Integration failure:** Poor integration of findings from all methods used" / "**Limitation shirker**: Failure to discuss limitations from all methods used or from their integration"
- 要点：反面模式："不速之客"：某个方法在引言和方法部分没有交代，却突然出现在讨论或局限部分；"整合失败"：各方法的发现没有整合好；"回避局限"：没有讨论各方法及其整合的局限。

### E284

- 位置：Multi-Methodology and Mixed Methods 标准，反面模式
- 原文："**Missing the mark:** Misalignment of multi- or mixed method design with the research question/objective" / "**Cargo cult research:** Using methods where the research team lacks expertise in those methods, but hopes they work" / "**Design by committee:** Failure to agree on a crisp research question/objective (may be induced by different epistemological perspectives or use of heterogeneous methods)"
- 要点：反面模式：设计和研究问题不匹配；团队并不掌握某种方法，却指望它能奏效；因为认识论立场不同或方法各异，团队始终没有商定一个清楚的研究问题。

### E285

- 位置：Multi-Methodology and Mixed Methods 标准，反面模式
- 原文："**Golden hammer:** relying on superficial, typically quantitative analysis of rich qualitative data" / "**Sample contamination:** a mixed method sequential design where the same participants are used in multiple, sequential methods without accounting for potential contamination from earlier method(s) to later ones." / "**Ignoring the writing on the wall:** In a mixed method sequential design, failing to use findings from an earlier study when forming an instrument for a study in a later phase of the research"
- 要点：反面模式：对丰富的定性数据只做肤浅的（通常是定量的）分析；先后几个阶段用同一批参与者，却不考虑前一阶段对后一阶段的影响；后一阶段设计测量工具时没有利用前一阶段的发现。

### E286

- 位置：Multi-Methodology and Mixed Methods 标准，Examples of Acceptable Deviations
- 原文："Conference page limits may make it particularly challenging to share sufficient details on all methods used. These details may be available in other publications or supplementary materials." / "Describing the research in terms of cycles or ongoing parallel processes instead of phases."
- 要点：可接受的偏离：会议篇幅有限，各方法的细节可以放在其他论文或补充材料中；可以用循环或并行过程而不是"阶段"来描述研究。

### E287

- 位置：Multi-Methodology and Mixed Methods 标准，Invalid Criticisms
- 原文："The method(ologie)s do not contribute equally (a non-equal design) or the minor method is limited (e.g. few participants)." / "The mixed- or multi-method approach isn't necessary (when it *is* beneficial)" / "The method(ologie)s have different philosophical foundations or are otherwise incompatible" / "In an unequal design, the wrong method is dominant (this is a study design choice not a flaw )" / "The method(ologie)s have inconsistent findings"
- 要点：不成立的批评：各方法贡献不对等，或次要方法规模有限（如参与者少）；混合方法"没有必要"（实际上有益时）；各方法哲学基础不同；不对等设计中"主次选错了"；各方法的发现不一致。

### E288

- 位置：Multi-Methodology and Mixed Methods 标准，Notes
- 原文："For multi-method research, it is important to distinguish between using different methods of collecting data (e.g., as part of an inductive case study) and using different research strategies (e.g., complementing an inductive case study with a deductive experiment in a later stage of the research)."
- 要点：要区分两件事：在一项研究内用几种方式收集数据（例如一项归纳式案例研究中），和使用不同的研究策略（例如在后一阶段用演绎式实验补充案例研究）。

### E289

- 位置：Multi-Methodology and Mixed Methods 标准，Notes
- 原文："Some experts on mixed methods use specific terms to refer to core mixed method designs (e.g., Convergent mixed methods, Explanatory sequential mixed methods, Exploratory sequential mixed methods are defined by Creswell & Creswell (2007)"
- 要点：混合方法文献中有几种核心设计的专门名称：汇聚式、解释性序贯式、探索性序贯式。

### E290

- 位置：General Standard，Extraordinary Attributes
- 原文："applies two or more data collection or analysis strategies to the same research question" / "approaches the same research question(s) from multiple epistemological perspectives"
- 要点：在 General Standard 中，对同一研究问题使用两种及以上数据收集或分析策略、从多种认识论视角研究同一问题，属于"优秀"项，而不是必要项。

### E291

- 位置：Case Survey 标准，标题下的定义
- 原文："A study that aims to generalize results about a complex phenomenon by systematically converting qualitative descriptions available in published case studies into quantitative data and analyzing the converted data"
- 要点：案例调查是把已发表案例研究中的定性描述系统地转换成定量数据、再加以分析，以期对复杂现象得出可推广结论的研究。

### E292

- 位置：Case Survey 标准，Application
- 原文："This standard does not apply to studies collecting primary data from a large number of instances of a phenomenon" / "For individual case studies use the **Case Study Standard**. For reviews of other kinds of studies (e.g., experiments) consider the **Systematic Review Standard**. This standard also does not apply to qualitative synthesis (e.g. meta-ethnography, narrative synthesis)."
- 要点：自己从大量实例收集一手数据的研究不算案例调查；单个案例研究用案例研究标准；综述实验等其他研究用系统综述标准；定性综合（如元民族志、叙事综合）也不适用本标准。

### E293

- 位置：Case Survey 标准，Essential Attributes 及脚注 1
- 原文："presents step-by-step, systematic, replicable description of the search process for published case studies (not necessarily in peer-reviewed venues)" / "defines clear inclusion and exclusion criteria for cases" / "reports at least two of the variables in the coding scheme"
- 要点：必要项：一步步、可复现地描述检索已发表案例研究的过程（不限于同行评审的刊物）；给出明确的案例纳入和排除标准，例如"至少报告了编码方案中的两个变量"。

### E294

- 位置：Case Survey 标准，Essential Attributes
- 原文："mitigates sampling bias and publication bias, using some (not all) of:"
- 要点：必要项：用若干种（不必全部）检索方式减轻抽样偏差和发表偏差，所列方式与系统综述标准相同（关键词检索、滚雪球、预印本、学位论文、联系作者等）。

### E295

- 位置：Case Survey 标准，Essential Attributes 及脚注 2
- 原文："defines a coding scheme to convert qualitative case descriptions into quantitative variables" / "the coding scheme should balance simplicity and information richness" / "EITHER: describes the coding scheme in detail;" / "OR: provides the coding scheme in supplementary materials"
- 要点：必要项：定义把定性的案例描述转换为定量变量的编码方案，方案要在简单和信息丰富之间取得平衡；在正文详细描述它，或放进补充材料。

### E296

- 位置：Case Survey 标准，Essential Attributes
- 原文："clearly explains how missingness in the dataset was managed" / "draws conclusions based on the quantitative variables derived"
- 要点：必要项：说清数据集中的缺失值是怎么处理的；结论要建立在编码得到的定量变量之上。

### E297

- 位置：Case Survey 标准，Essential Attributes（discussion）
- 原文："acknowledges generalizability threats; discusses how case studies reviewed may differ from target population"
- 要点：必要项：承认推广性方面的威胁，讨论纳入的案例可能和想推论的总体有哪些不同。

### E298

- 位置：Case Survey 标准，Desirable Attributes
- 原文："provides supplementary materials such as  protocol, search terms, search results, selection process results, coding scheme, examples of coding, decision rules, complete dataset, analysis scripts, descriptions of edge cases" / "explains and justifies the design of the coding scheme"
- 要点：加分项：公开研究方案、检索词、检索和筛选结果、编码方案、编码示例、判定规则、完整数据集、分析脚本、边界情况说明；解释并论证编码方案为什么这样设计。

### E299

- 位置：Case Survey 标准，Desirable Attributes 及脚注 4
- 原文："uses 2+ independent analysts; analyzes inter-rater reliability" / "explains how discrepancies among coders were resolved" / "By discussion and agreement, voting, adding tie-breaker, consulting with study authors, etc."
- 要点：加分项：两人以上独立编码，分析编码者之间的一致性，并说明分歧怎么解决（讨论达成一致、投票、增加一名裁决人、咨询原作者等）。

### E300

- 位置：Case Survey 标准，Desirable Attributes
- 原文："describes contacting authors of primary studies for more information, to check coding accuracy, or resolve coding disagreements"
- 要点：加分项：联系原始案例研究的作者，获取更多信息、核对编码是否准确或解决编码分歧。

### E301

- 位置：Case Survey 标准，Desirable Attributes
- 原文："assesses quality of primary studies using an a priori scheme" / "models study quality as a moderating variable"
- 要点：加分项：用事先定好的方案评估原始研究的质量，并把研究质量作为调节变量放进分析。

### E302

- 位置：Case Survey 标准，Desirable Attributes 及脚注 5
- 原文："consolidates results using tables, diagrams, or charts; includes PRISMA flow diagram" / "clearly distinguishes evidence-based results from interpretations and speculation"
- 要点：加分项：用表格和图汇总结果，附 PRISMA 流程图；清楚区分有证据的结果和解读、推测。

### E303

- 位置：Case Survey 标准，Extraordinary Attributes
- 原文："uses theory to select and sample cases" / "adds data from other sources to the selected cases" / "employs authors of primary studies to conduct the coding or ensure interpretations are correct" / "analyzes if/how studies’ characteristics (e.g., research design, publication venue or date) influence the coding"
- 要点：优秀项：用理论指导案例的选择和抽样；为选中的案例补充其他来源的数据；请原作者参与编码或确认解读；分析研究设计、发表刊物、发表时间等特征是否影响编码结果。

### E304

- 位置：Case Survey 标准，Antipatterns
- 原文："including primary studies that are not case studies (e.g., questionnaires or a small amounts of data)" / "include all cases without a critical evaluation of the data available" / "analyze data from cases using qualitative techniques" / "describing each case in isolation rather than synthesizing findings." / "relying on publication venue as a proxy for quality" / "conflating correlation with causation in findings"
- 要点：反面模式：纳入不是案例研究的材料（如问卷、只有很少数据的报告）；不审视数据是否够用就纳入所有案例；用定性方法分析；逐个描述案例而不综合；用发表刊物代替质量评估；把相关当成因果。

### E305

- 位置：Case Survey 标准，Invalid Criticisms
- 原文："the studies were not published in peer-reviewed venues" / "the original studies do not employ a common research design" / "the cases are not a random sample of the phenomenon"
- 要点：不成立的批评：原始研究不是在同行评审的刊物上发表的；原始研究的设计各不相同；案例不是该现象的随机样本。

### E306

- 位置：Meta Science 标准，标题下的定义
- 原文："A paper that analyses an issue of research methodology or makes recommendations for conducting research"
- 要点：方法论与元科学论文：分析某个研究方法问题，或就如何开展研究提出建议的论文。

### E307

- 位置：Meta Science 标准，Application
- 原文："may or may not include primary or secondary empirical data or analysis." / "may consider philosophical or practical issues" / "may simultaneously be a methodology paper and an empirical study, to which another standard also applies"
- 要点：这类论文可以有、也可以没有一手或二手的实证数据；可以讨论哲学问题或实际问题；也可以同时是一篇实证研究，这时还要满足相应类型的标准。

### E308

- 位置：Meta Science 标准，Essential Attributes
- 原文："presents information that is useful for other researchers" / "makes recommendations for future research" / "presents clear, valid arguments supporting recommendations"
- 要点：必要项：提供对其他研究者有用的信息；对今后的研究提出建议；用清楚、成立的论证支撑这些建议。

### E309

- 位置：Meta Science 标准，Desirable Attributes
- 原文："synthesizes related work from reference disciplines" / "goes beyond summarizing methodological guidance from existing works or reference disciplines;" / "develops helpful artifacts (e.g. checklists, templates, tests, tools, sets of criteria)"
- 要点：加分项：综合相关学科的已有工作；不只是转述已有的方法指南，而要给出本领域特有的见解；做出有用的工具，如检查清单、模板、测试、工具或评判标准。

### E310

- 位置：Meta Science 标准，Extraordinary Attributes
- 原文："includes an empirical study (e.g. a systematic literature review) that motivates the analysis of guidance" / "quantitative simulation illustrating methodological issues"
- 要点：优秀项：包含一项实证研究（如系统综述）来引出分析和建议；用定量模拟来展示方法问题。

### E311

- 位置：Meta Science 标准，Antipatterns 及脚注 1
- 原文："overreaching; informal logical fallacies (e.g. straw man argument, appeal to popularity, shifting the burden of proof)" / "citing seminal works is not the “appeal to authority” fallacy" / "discussing an issue without clear conclusions; failing to provide clear guidelines"
- 要点：反面模式：结论超出论证；犯非形式逻辑谬误（稻草人、诉诸流行、转移举证责任）；讨论了问题却没有明确结论和指南。引用奠基性著作不算"诉诸权威"。

### E312

- 位置：Meta Science 标准，Antipatterns
- 原文："attacking individual studies or researchers; hypothetical examples should be used to avoid engendering animosity"
- 要点：反面模式：攻击具体的研究或研究者；应当用假设的例子，避免引起敌意。

### E313

- 位置：Meta Science 标准，Invalid Criticisms
- 原文："Guidelines are not based on empirical evidence. Empirically testing meta-scientific propositions is typically impractical or impossible. Reviewers should evaluate the face validity, comprehensiveness and usefulness of the guidelines."
- 要点：不成立的批评："指南没有实证依据"。元科学主张通常无法用实证检验；审稿人应评价指南表面上是否合理、是否全面、是否有用。

### E314

- 位置：Meta Science 标准，Notes
- 原文："reviewers of methodology papers must themselves be experts in the methodology, so that they can evaluate the reasonableness of the guidelines" / "reviewers should be more pedantic in critiquing the discussion and guidelines than for an empirical paper"
- 要点：方法论论文的审稿人自己必须精通该方法；对讨论和指南的审查应比对实证论文更严格、更较真。

### E315

- 位置：Meta Science 标准，Exemplars
- 原文："Barbara Kitchenham and Stuart Charters. 2007. Guidelines for performing systematic literature reviews in software engineering." / "Per Runeson and Martin Höst. 2009. Guidelines for conducting and reporting case study research in software engineering."
- 要点：标准列出的范例包括 Kitchenham & Charters 的系统综述指南和 Runeson & Höst 的案例研究指南，即方法指南类论文。

### E316

- 位置：Grounded Theory 标准，Application
- 原文："Explores a broad area of investigation without specific, up-front research questions." / "Applies theoretical sampling with iterative and interleaved rounds of data collection and analysis." / "For predominately qualitative inquiries that do not iterate between data collection and analysis or do not use theoretical sampling, consider the **Case Study Standard** or the **Qualitative Survey Standard**."
- 要点：适用于探索一个宽泛领域、没有事先定好具体研究问题、用理论抽样并让数据收集与分析交替迭代的研究；不迭代、不做理论抽样的定性研究，应按案例研究或定性调查（访谈研究）标准。

### E317

- 位置：Grounded Theory 标准，Essential Attributes（method）
- 原文："identifies the variant(s) of Grounded Theory used/adapted (Glaser, Strauss/Corbin, Charmaz, etc.)" / "characterizes the data (participants' demographics, types of documents, nature of field notes, ...)" / "explains how the research iterated between data collection (using theoretical sampling) and analysis (using constant comparison)" / "states that and how theoretical saturation was determined" / "explains how key patterns (e.g. categories) were found via GT steps (e.g. selective coding)"
- 要点：必须写明用了哪个流派；描述数据；说明数据收集（理论抽样）和分析（持续比较）如何交替进行；说明是否以及如何判断理论饱和；说明关键类别是通过哪些步骤得到的。

### E318

- 位置：Grounded Theory 标准，Essential Attributes（results / discussion）
- 原文："states results in terms of concepts that assign meaning to data ("theoretical coding": do not merely _describe_ the data)" / "grounds most or all important concepts in raw data explicitly (e.g. by providing quotations)" / "discusses the transferability of the theory"
- 要点：结果要用赋予数据意义的概念来表述，不能只是描述数据；重要概念要明确扎根于原始数据（例如给出引语）；讨论理论的可迁移性。

### E319

- 位置：Grounded Theory 标准，Desirable Attributes
- 原文："results involve relationships between the concepts ("pushing to theory", not stopping with unconnected themes)" / "explains how memo writing was used to drive the work" / "validates results using member checking, dialogical interviewing, feedback from non-participant practitioners or research audits of coding by advisors or other researchers" / "includes data representing a diverse (rather than homogeneous) spectrum of people or things"
- 要点：加分项：结果包含概念之间的关系（推进到理论，而不是停在互不相连的主题）；说明备忘录如何推动研究；用参与者核验、对话式访谈、非参与者从业者的反馈或导师/同行审查编码来检验结果；数据覆盖多样的人或事物。

### E320

- 位置：Grounded Theory 标准，Desirable Attributes
- 原文："provides supplemental materials such as interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence tables" / "a diagram provides an overview of the main concepts and relationships" / "shows the mapping from categories to lower-level codes and concepts to observations (e.g. as a table)" / "compares results with (or integrates them into) prior theory or related research"
- 要点：加分项：提供访谈提纲、编码方案、编码示例、判断规则等补充材料；用图概括主要概念和关系；用表格展示类别到底层编码、概念到观察的对应；把结果与已有理论或相关研究比较或整合。

### E321

- 位置：Grounded Theory 标准，Desirable Attributes
- 原文："explains how and why study deviates from claimed GT variant and/or how variants were combined" / "reflects on how researcher's biases may have affected their analysis" / "explains the role of literature, especially where an extensive review preceded the GT study"
- 要点：加分项：说明偏离所声称流派的地方及原因，或怎样组合了不同流派；反思研究者的偏见可能如何影响分析；说明文献起了什么作用，尤其是研究前已做过大量综述的情况。

### E322

- 位置：Grounded Theory 标准，Extraordinary Attributes
- 原文："triangulates with extensive quantitative data (e.g. questionnaires, sentiment analysis)" / "employs a team of researchers and explains their roles"
- 要点：优秀项：用大量定量数据（如问卷、情感分析）做三角验证；由研究团队完成并说明各人的角色。

### E323

- 位置：Grounded Theory 标准，Quality Criteria
- 原文："reviewers should consider common qualitative criteria such as **credibility**, **resonance**, **usefulness** and the degree to which results *extend* our cumulative knowledge." / "Quantitative quality criteria such as internal validity, construct validity, replicability, generalizability and reliability typically do not apply."
- 要点：评价扎根理论研究应看可信度、共鸣、有用性，以及是否扩展了已有知识；内部效度、可复现性、可推广性等定量研究的标准一般不适用。

### E324

- 位置：Grounded Theory 标准，Examples of Acceptable Deviations
- 原文："In a study of sexual harassment at a named organization, detailed description of interviewees and direct quotations are omitted to protect participants."
- 要点：可接受的偏离：为保护参与者（例如研究某具名组织中的性骚扰），可以省略受访者的详细描述和直接引语。

### E325

- 位置：Grounded Theory 标准，Antipatterns
- 原文："Conducting data collection and data analysis sequentially; applying only analysis techniques of GT." / "Data analysis focusing on counting words, codes, concepts, or categories instead of interpreting." / "Presenting a tutorial on grounded theory instead of explaining how the current study was conducted."
- 要点：反面模式：先收集完再分析，只用扎根理论的分析技巧；数词、数编码而不做解读；在论文里讲扎根理论教程，而不交代本研究怎么做的。

### E326

- 位置：Grounded Theory 标准，Antipatterns
- 原文："Small, homogeneous samples creating the illusion of convergence and theoretical saturation." / "it is highly unlikely that a full theory can be derived only from interviews with 20 similar people." / "Focusing only on interviews without corroborating statements with other evidence (e.g. documents, observation)."
- 要点：反面模式：样本小而同质，造成"已经收敛、已经饱和"的假象，只访谈 20 个相似的人很难得出完整理论；只靠访谈，不用文档、观察等其他证据核对受访者的说法。

### E327

- 位置：Grounded Theory 标准，Invalid Criticisms
- 原文："Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability." / "Lack of replicability or reproducibility; not releasing transcripts" / "Lack of representativeness (e.g. of a study of Turkish programmers, 'how does this generalize to America?')" / "Findings should have been presented as a different set of relationships, hypotheses, or a different theory."
- 要点：不成立的批评：缺少定量数据、因果分析、客观性、内部效度或可推广性；不可复现、没有公开访谈转录；样本不具代表性；结果"应该"呈现为另一套关系或另一个理论。

### E328

- 位置：Glossary，Theoretical sampling
- 原文："choosing which data to collect based on the emerging theory, concepts or categories; typically used in qualitative research, especially Grounded Theory."
- 要点：理论抽样：根据正在形成的理论、概念或类别，选择下一步收集什么数据。

### E329

- 位置：Glossary，Credibility / Resonance / Transferability
- 原文："the extent to which conclusions are supported by rich, multivocal evidence." / "the extent to which a study's conclusions make sense to (i.e., resonate with) participants" / "the extent to which a study's results could plausibly apply to other sites, people or circumstances."
- 要点：可信度：结论有丰富、多方声音的证据支持；共鸣：结论对参与者来说讲得通；可迁移性：结果在多大程度上可能适用于其他地点、人群或情境。

### E330

- 位置：Action Research 标准，标题下的定义
- 原文："Empirical research that investigates how an intervention, like the introduction of a method or tool, affects a real-life context"
- 要点：行动研究是研究一项干预（例如引入某种方法或工具）如何影响真实环境的实证研究。

### E331

- 位置：Action Research 标准，Application
- 原文："intervenes in the real-life context (otherwise see the **Case Study Standard**)" / "the change and its observation are an integral part of addressing the research question and contribute to research"
- 要点：行动研究要在真实环境中实施干预（不干预的应按案例研究标准）；改变本身和对改变的观察是回答研究问题的核心部分。

### E332

- 位置：Action Research 标准，Application
- 原文："If the intervention primarily alters social phenomena (e.g. the organization's processes, culture, way of working or group dynamics), use this standard. If the intervention is a new technology or technique (e.g. a testing tool, a coding standard, a modeling grammar), especially if it lacks a social dimension, consider the **Engineering Research Standard**." / "If the research involves creating a technology and an organizational intervention with a social dimension, consider both standards."
- 要点：干预主要改变流程、文化、工作方式等社会现象的，用行动研究标准；干预是新技术或技巧、缺少社会层面的，考虑工程研究标准；两者都有的，两个标准都参考。

### E333

- 位置：Action Research 标准，Essential Attributes（method）及脚注 1
- 原文："justifies the selection of the site(s) that was(were) studied" / "describes the site(s) in rich detail" / "describes the relationship between the researcher and the host organization" / "E.g. project financing, potential conflicts of interest, professional relationship leading to access."
- 要点：必须说明为什么选这个（些）组织，详细描述组织情况，并说明研究者与组织的关系，例如项目经费、潜在利益冲突、靠什么关系获得了进入机会。

### E334

- 位置：Action Research 标准，Essential Attributes（method）及脚注 2
- 原文："describes the intervention(s) in detail" / "describes how interventions were determined (e.g. by management, researchers, or a participative/co-determination process)" / "explains how the interventions are evaluated" / "Can include quantitative evaluation in addition to qualitative evaluation."
- 要点：必须详细描述干预，说明干预由谁决定（管理层、研究者，还是共同参与决定），说明如何评估干预；评估可以在定性之外加上定量。

### E335

- 位置：Action Research 标准，Essential Attributes（method）及脚注 3、4
- 原文："describes the longitudinal dimension of the research design (including the length of the study)" / "describes the interactions between researcher(s) and host organization(s)" / "i.e. who intervened and with which part of the organization?" / "explains research cycles or phases, if any, and their relationship to the intervention(s)" / "Action research projects are structured in interventions often described as action research cycles, which are often structured in distinct phases. It is a flexible methodology, where subsequent cycles are based on their predecessors."
- 要点：必须说明研究的时间跨度、研究者与组织的互动（谁实施了干预、和组织的哪一部分合作），以及研究的循环或阶段与干预的关系。行动研究常按"循环"组织，每个循环分几个阶段，后一个循环建立在前一个的基础上。

### E336

- 位置：Action Research 标准，Essential Attributes（results / discussion）
- 原文："presents a clear chain of evidence from observations to findings" / "reports participant or stakeholder reactions to interventions" / "reports lessons learned by the organization" / "researchers reflect on their own possible biases"
- 要点：必须给出从观察到结论的清楚证据链，报告参与者和利益相关者对干预的反应，报告组织学到了什么，研究者要反思自己可能的偏见。

### E337

- 位置：Action Research 标准，Desirable Attributes
- 原文："provides supplemental materials such as interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence tables" / "uses direct quotations extensively" / "validates results using member checking, dialogical interviewing, feedback from non-participant practitioners or research audits of coding by advisors or other researchers" / "findings plausibly transferable to other contexts" / "triangulation across quantitative and qualitative data"
- 要点：加分项：提供补充材料；大量使用直接引语；用参与者核验、非参与者从业者反馈、导师或同行审查编码等检验结果；结论可能迁移到其他情境；在定量和定性数据之间做三角验证。

### E338

- 位置：Action Research 标准，Extraordinary Attributes
- 原文："research team with triangulation across researchers (to mitigate researcher bias)"
- 要点：优秀项：由多名研究者组成团队，在研究者之间相互印证，以减轻研究者偏见。

### E339

- 位置：Action Research 标准，General Quality Criteria
- 原文："Example criteria include reflexivity, credibility, resonance, usefulness and transferability" / "Positivist quality criteria such as internal validity, construct validity, generalizability and reliability typically do not apply."
- 要点：评价标准包括反思性、可信度、共鸣、有用性、可迁移性；内部效度、可推广性等实证主义标准一般不适用。

### E340

- 位置：Action Research 标准，Examples of Acceptable Deviations
- 原文："In a study of deviations from organizational standards, detailed description of circumstances and direct quotations are omitted to protect participants." / "The article reports a negative outcome of an intervention and e.g. investigates why a certain method was not applicable."
- 要点：可接受的偏离：为保护参与者省略详细情况和直接引语；报告干预的负面结果，例如分析某方法为什么不适用。

### E341

- 位置：Action Research 标准，Antipatterns
- 原文："Forcing interventions that are not acceptable to participants or the host organization." / "Losing professional distance and impartiality; getting too involved with the community under study." / "Over-selling a tool or method without regard for participants' problems, practices or values." / "Avoiding systematic evaluation; downplaying problems; simply reporting participants views of the intervention."
- 要点：反面模式：强推参与者或组织不能接受的干预；失去职业距离和公正，与研究对象过度融为一体；不顾参与者的问题、做法和价值观推销某个工具或方法；回避系统评估、淡化问题、只报告参与者对干预的看法。

### E342

- 位置：Action Research 标准，Invalid Criticisms
- 原文："The findings and insights are not valid because the research intervened in the context." / "the whole point of action research is to introduce a change and observe how participants react." / "Systematic observation and reflection should not be dismissed as consultancy or experience reports. Inversely, consultancy or experiences should not be falsely presented as action research."
- 要点：不成立的批评："研究者干预了环境，所以结论无效"——行动研究的意义就在于引入改变并观察反应。系统的观察和反思不应被贬为咨询或经验报告；反过来，咨询或经验也不应冒充行动研究。

### E343

- 位置：Action Research 标准，Invalid Criticisms
- 原文："Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability." / "Sample not representative; lack of generalizability; generalizing from one organization." / "Lack of replicability or reproducibility; not releasing transcripts." / "Lack of control group or experimental protocols. An action research study is not an experiment."
- 要点：不成立的批评：缺少定量数据、因果分析、可推广性；样本不具代表性、只基于一个组织；不可复现、没公开转录；没有对照组——行动研究不是实验。

### E344

- 位置：Glossary，Reflexivity / Transferability
- 原文："the extent to which authors reflect on their potential biases and interactions with the team, organization or community, especially possible negative impacts on some participants or stakeholders." / "the extent to which a study's results could plausibly apply to other sites, people or circumstances."
- 要点：反思性：作者在多大程度上反思了自己可能的偏见、与团队或组织的互动，特别是对某些参与者可能造成的负面影响。可迁移性：结果在多大程度上可能适用于其他地点、人群或情境。

### E345

- 位置：Qualitative Surveys 标准，Application
- 原文："Researcher(s) have synchronous conversations with one participant at a time" / "Researchers ask, and participants answer, open-ended questions" / "Participants' answers are recorded in some way" / "Researchers apply some kind of qualitative data analysis to participants' answers"
- 要点：访谈研究同时满足四条：研究者与参与者一对一实时交谈；研究者提开放式问题、参与者回答；回答以某种方式记录下来；对回答做某种定性分析。

### E346

- 位置：Qualitative Surveys 标准，Application
- 原文："If researchers iterated between data collection and analysis, consider the **Grounded Theory Standard**. If respondents are all from the same organization, consider the **Case Study Standard**."
- 要点：如果数据收集和分析反复交替进行，应参考扎根理论标准；如果受访者都来自同一个组织，应参考案例研究标准。

### E347

- 位置：Qualitative Surveys 标准，Notes
- 原文："A qualitative survey generally has more interviews than a case study that triangulates across different kinds of data."
- 要点：访谈研究的访谈数量一般多于案例研究；案例研究靠多种数据互相印证。

### E348

- 位置：Qualitative Surveys 标准，General Quality Criteria
- 原文："An interview study should address appropriate qualitative quality criteria such as:" [...] "Quantitative quality criteria such as internal validity, construct validity, generalizability and reliability typically do not apply."
- 要点：访谈研究应满足合适的定性质量标准（可信度、共鸣、有用性、可迁移性）；内部效度、构念效度、可推广性、信度等定量质量标准一般不适用。

### E349

- 位置：Glossary，Credibility / Resonance / Usefulness / Transferability
- 原文："**Credibility**: the extent to which conclusions are supported by rich, multivocal evidence." / "**Resonance**: the extent to which a study’s conclusions make sense to (i.e., resonate with) participants" / "**Usefulness**: the extent to which a study provides actionable recommendations to researchers, practitioners **OR** educators." / "**Transferability**: the extent to which a study's results could plausibly apply to other sites, people or circumstances."
- 要点：可信度＝结论有丰富、多方声音的证据支持；共鸣＝结论对参与者来说讲得通；有用性＝能给研究者、实践者或教育者可操作的建议；可迁移性＝结果有可能适用于其他场景、人群或情况。

### E350

- 位置：Glossary，Reflexivity
- 原文："**Reflexivity**: the extent to which authors reflect on their potential biases and interactions with the team, organization or community, especially possible negative impacts on some participants or stakeholders."
- 要点：反身性＝作者反思自己可能的偏见，以及自己与团队、组织或社群的互动，特别是对部分参与者可能造成的负面影响。

### E351

- 位置：Qualitative Surveys 标准，必要项（方法）
- 原文："explains how interviewees were selected" / "describes interviewees (e.g. demographics, work roles)" / "describes interviewer(s) (e.g. experience, perspective)"
- 要点：必须说明受访者是怎么选出来的，描述受访者（如人口学特征、工作角色），描述访谈者（如经验、视角）。

### E352

- 位置：Qualitative Surveys 标准，必要项（结果）
- 原文："presents clear chain of evidence from interviewee quotations to findings (e.g. proposed concepts)" / "clearly answers the research question(s)" / "provides evidence of saturation; explains how saturation was achieved"
- 要点：必须给出从受访者原话到研究发现的清楚证据链；明确回答研究问题；提供饱和的证据并说明如何达到饱和。

### E353

- 位置：Qualitative Surveys 标准，必要项（讨论）
- 原文："researchers reflect on their own possible biases" / "identifies key issues under consideration"
- 要点：必须反思研究者自己可能的偏见，并指出所考虑的关键问题。

### E354

- 位置：Qualitative Surveys 标准，加分项
- 原文："provides supplemental materials including interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence table(s)" / "describes questions asked in data collection: content of central questions, form of questions (e.g. open vs. closed)"
- 要点：加分项：提供补充材料（访谈提纲、编码方案、编码示例、判定规则、扩展的证据链表格）；描述所问的问题，包括核心问题的内容和形式（开放还是封闭）。

### E355

- 位置：Qualitative Surveys 标准，加分项
- 原文："includes highly diverse participants" / "describes the relationships and interactions between researchers and participants relevant to the research process"
- 要点：加分项：参与者高度多样；描述研究者与参与者之间与研究过程相关的关系和互动。

### E356

- 位置：Qualitative Surveys 标准，加分项
- 原文："uses direct quotations extensively to support key points" / "identifies data recording methods (audio/visual), field notes or transcription processes used"
- 要点：加分项：大量使用直接引语支持关键观点；说明数据记录方式（音频/视频）、现场笔记或转录过程。

### E357

- 位置：Qualitative Surveys 标准，加分项
- 原文："EITHER: evaluates an a priori theory (or model, framework, taxonomy, etc.) using deductive coding with an a priori coding scheme based on the prior theory" / "OR: synthesizes results into a new, mature, fully-developed and clearly articulated theory (or model, etc.) using some form of inductive coding (coding scheme generated from data)"
- 要点：加分项二选一：用基于已有理论的预设编码方案做演绎编码，检验已有理论；或者用归纳编码（编码方案从数据中产生），把结果综合成一个新的、成熟、表述清楚的理论或模型。

### E358

- 位置：Qualitative Surveys 标准，加分项
- 原文："validates results using member checking, dialogical interviewing, feedback from non-participant practitioners or research audits of coding by advisors or other researchers"
- 要点：加分项：用参与者核查、对话式访谈、非参与者的实践者反馈，或由导师、其他研究者审查编码，来验证结果。

### E359

- 位置：Qualitative Surveys 标准，加分项
- 原文："discusses transferability; findings plausibly transferable to different contexts" / "compares results with (or integrates them into) prior theory or related research" / "reflects on any alternative explanations of the findings"
- 要点：加分项：讨论可迁移性；与已有理论或相关研究比较；反思对发现的其他解释。

### E360

- 位置：Qualitative Surveys 标准，加分项
- 原文："describes any incentives or compensation, and provides assurance of relevant ethical processes of data collection and consent process as relevant"
- 要点：加分项：说明给参与者的激励或报酬，并说明数据收集和知情同意的伦理流程。

### E361

- 位置：Qualitative Surveys 标准，优秀项
- 原文："employs multiple methods of data analysis (e.g. open coding vs. process coding; manual coding vs. automated sentiment analysis) with method-triangulation" / "employs longitudinal design (i.e. each interviewee participates multiple times) and analysis" / "employs probabilistic sampling strategy; statistical analysis of response bias" / "uses multiple coders and analyzes inter-coder reliability"
- 要点：优秀项：多种分析方法互相印证；纵向设计（每人访谈多次）；概率抽样并统计分析回应偏差；多人编码并分析编码者间信度。

### E362

- 位置：Qualitative Surveys 标准，Antipatterns
- 原文："Interviewing a small number of similar people, creating the illusion of convergence and saturation" / "Mis-presenting a qualitative survey as grounded theory or a case study."
- 要点：反面模式：只访谈少数相似的人，造成观点趋同、已经饱和的假象；把访谈研究说成扎根理论或案例研究。

### E363

- 位置：Qualitative Surveys 标准，Invalid Criticisms
- 原文："Lack of quantitative data; causal analysis; objectivity, internal validity, reliability, or generalizability." / "Lack of replicability or reproducibility; not releasing transcripts." / "Lack of probability sampling, statistical generalizability or representativeness unless representative sampling was an explicit goal of the study."
- 要点：不成立的批评：缺少定量数据、因果分析、客观性、内部效度、信度或可推广性；不可重复、不公开转录稿；没有概率抽样、统计推广性或代表性（除非研究明确以代表性为目标）。

### E364

- 位置：Qualitative Surveys 标准，Examples of Acceptable Deviations
- 原文："In a study of deaf software developers, the interviews are conducted via text messages." / "In a study of sexual harassment at named organizations, detailed description of interviewees and direct quotations are omitted to protect participants."
- 要点：可接受的偏离：研究聋人开发者时用文字消息访谈；研究具名组织中的性骚扰时，为保护参与者省略受访者详细描述和直接引语。

### E365

- 位置：Inter-Rater Reliability and Agreement 补充标准，Application 与 Philosophy
- 原文："Does not apply to constructivist or intepretivist qualitative data analysis." / "the idea that multiple raters should agree is consistent with realist, positivist, and falsificationist philosophical positions; from an interpretivist or constructivist perspective, different analysts are expected to have different views, so IRR and IRA are irrelevant."
- 要点：编码者一致性补充标准不适用于建构主义或诠释主义的定性分析；"多个评判者应当一致"符合实在论、实证主义立场，而在诠释主义或建构主义看来，不同分析者本就会有不同看法，信度和一致性指标无关紧要。

### E366

- 位置：Inter-Rater Reliability and Agreement 补充标准，Practicality
- 原文："multiple raters applying an _a priori_, deductive coding scheme to some artifacts is more practical than multiple raters inductively coding 2000 pages of interview transcripts."
- 要点：多人用预设的演绎编码方案给材料编码，比多人对 2000 页访谈转录稿做归纳编码更现实。

### E367

- 位置：Inter-Rater Reliability and Agreement 补充标准，Invalid Criticisms 与 Notes
- 原文："Criticizing use of a single rater where multiple raters would be impractical or inconsistent with the study's underlying philosophy.." / "IRR/IRA analysis not only indicates reliability and objectivity (in positivist research) but also improves reflexivity (in anti-positivist research)."
- 要点：在多人编码不现实或与研究立场不符时，批评"只有一个编码者"不成立；一致性分析在实证主义研究中表明信度和客观性，在反实证主义研究中也能提升反身性。

### E368

- 位置：Inter-Rater Reliability and Agreement 补充标准，Antipatterns
- 原文："Calculating multiple IRR/IRA measures and reporting only the most favourable (p-hacking)" / "Pretending that an obviously positivist study adopts an idealist ontology to avoid employing multiple raters"
- 要点：反面模式：算多种一致性指标、只报最好看的；明明是实证主义研究，却假装持诠释立场来逃避多人编码。

### E369

- 位置：Ethics (Studies with Human Participants) 补充标准，必要项
- 原文："explains the compensation (if any) offered for participation and how coercion was mitigated" / "explains how participants' free, individual, informed consent to participate was obtained"
- 要点：必须说明给参与者的报酬以及如何避免强迫，说明如何取得参与者自由、个人、知情的同意。

### E370

- 位置：Glossary，Gatekeeper
- 原文："Gatekeepers may influence individual’s participation decisions (e.g., employers may coerce employees to participate)"
- 要点：把关人（控制研究者接触对象的人或组织）可能影响个人是否参与，例如雇主可能强迫员工参与。

### E371

- 位置：Sampling 补充标准，Antipatterns 与 Invalid Criticisms
- 原文："qualitative research with too little data for plausible saturation" / "for qualitative research, claiming that the sample size is too small without considering how the items were selected (e.g. theoretical sampling) or the authors' argument for saturation."
- 要点：反面模式：定性研究的数据太少，不可能达到饱和。不成立的批评：不考虑对象是怎么选的（如理论抽样）和作者关于饱和的论证，就说定性研究样本太小。

### E372

- 位置：Sampling 补充标准，加分项
- 原文："exploratory research: using purposive rather than convenience sampling for unit of analysis" / "theory building: using theoretical rather than convenience sampling"
- 要点：探索性研究用目的抽样而不是便利抽样；构建理论时用理论抽样而不是便利抽样。

### E373

- 位置：General Standard，Invalid Criticisms
- 原文："Cross-paradigmatic criticism (e.g. attacking an interpretivist study for not conforming to positivist norms)."
- 要点：跨范式批评（例如因为诠释主义研究不符合实证主义规范而攻击它）是不成立的批评。

### E374

- 位置：Optimization Studies 标准，标题下的定义与 Application
- 原文："Research studies that focus on the formulation of software engineering problems as search problems, and apply optimization techniques to solve such problems" / "Formulates a software engineering task as an optimization problem, with one or more specified fitness functions used to judge success in this task."
- 要点：优化研究的定义：把软件工程问题表述成搜索问题，用优化技术求解；适用于把任务表述为优化问题、并用一个或多个适应度函数判断成败的研究。

### E375

- 位置：Optimization Studies 标准，脚注 3
- 原文："A "fitness function", or "objective function", is a numerical scoring function used to indicate the quality of a solution to a defined problem. Optimization approaches attempt to maximize or minimize such functions, depending on whether lower or higher scores indicate success."
- 要点：适应度函数（也叫目标函数）是给一个解打分、表示其好坏的数值函数；优化方法就是让它尽量大或尽量小。

### E376

- 位置：Optimization Studies 标准，脚注 1
- 原文："Note that there are many such optimization techniques (metaheuristic; numerical optimizers; constraint solving theorem provers SAT,SMT,CSP; and other), some of which are stochastic."
- 要点：优化技术有很多种：元启发式算法、数值优化器、约束求解器等，其中一部分带随机性。

### E377

- 位置：Optimization Studies 标准，Essential（intro）及脚注 4
- 原文："explains why the problem cannot be optimized manually or by brute force within a reasonable timeframe" / "E.g., if the cross-product of the space of options is very large or if the time required to perform a task manually is very slow."
- 要点：必要：说明为什么这个问题无法在合理时间内靠人工或穷举解决，例如选项组合太多，或人工做太慢。

### E378

- 位置：Optimization Studies 标准，Essential（method）
- 原文："describes the search space (e.g., constraints, independent variables choices)" / "uses realistic and limited simplifications and constraints for the optimization problem; simplifications and constraints do not reduce the search to one where all solutions could be enumerated through brute force"
- 要点：必要：描述搜索空间（约束、自变量的取值）；简化和约束要符合实际、有节制，不能把问题简化到可以穷举所有解。

### E379

- 位置：Optimization Studies 标准，Essential（method）及脚注 6
- 原文："justifies the choice of algorithm underlying the approach" / "While one rarely knows the *best* approach for a new problem, one should at least consider the algorithms applied to address similar problems and make an informed judgement."
- 要点：必要：说明为什么选这个算法。对新问题很少能知道最好的算法，但至少要参考类似问题用过的算法，做有依据的判断。

### E380

- 位置：Optimization Studies 标准，Essential（method）及脚注 7
- 原文："compares approaches to a justified and appropriate baseline" / "If the approach addresses a problem never tackled before, then it should be compared - at least - to random search. Otherwise, compare the proposed approach to the existing state of the art."
- 要点：必要：和合理的基线比较。没人做过的新问题，至少要和随机搜索比；否则要和现有最先进的方法比。

### E381

- 位置：Optimization Studies 标准，Essential（method）及脚注 8、9
- 原文："explictly defines the solution formulation, including a description of what a solution represents, how it is represented, and how it is manipulated" / "explicitly defines all fitness functions, including the type of goals that are optimized and the equations for calculating fitness values"
- 要点：必要：明确定义解的表述：一个解代表什么（例如一个测试套件）、用什么结构表示（例如树或向量）、怎样被修改；明确定义所有适应度函数，包括优化目标和计算公式。

### E382

- 位置：Optimization Studies 标准，Essential（method）及脚注 10
- 原文："explicitly defines evaluated approaches, including the techniques, specific heuristics, and the parameters and their values" / "Example techniques - Simulated Annealing, Genetic Algorithm. Example heuristic - single-point crossover. Example parameters - crossover and mutation rates."
- 要点：必要：写清被评估的方法：技术（如模拟退火、遗传算法）、具体启发式（如单点交叉）、参数及取值（如交叉率、变异率）。

### E383

- 位置：Optimization Studies 标准，Essential（method）
- 原文："EITHER: clearly describes (and follows) a sound process to collect and prepare the datasets used to run and to evaluate the optimization approach" / "EITHER: makes data publicly available"
- 要点：必要：说明用来运行和评估优化方法的数据集是怎么收集和准备的（来自前人工作则注明出处和处理）；公开数据，或说明为什么不能公开。

### E384

- 位置：Optimization Studies 标准，Essential（method）及脚注 12、13
- 原文："identifies and explains all possible sources of stochasticity" / "stochasticity may arise from the use of randomized algorithms, from the use of a fitness function that measures a random variable from the environment (e.g., a fitness function based on execution time may return different results across different executions), from the use of data sampling or cross-validation approaches." / "EITHER: executes stochastic approaches or elements multiple times"
- 要点：必要：找出并说明所有随机性来源：随机化算法、测量环境随机量的适应度函数（如基于执行时间）、数据抽样或交叉验证；带随机性的方法要运行多次，或说明为什么做不到（如太慢、需要人参与）。

### E385

- 位置：Optimization Studies 标准，Desirable
- 原文："explains in detail how subjects or datasets were collected/chosen to mitigate selection bias and improve the generalization of findings" / "describes the main features of the subjects used to run and evaluate the optimization approach(es) and discuss what characterizes the different instances in terms of "hardness""
- 要点：加分：详细说明研究对象（问题实例）是怎么选的，以减少选择偏差、提高推广性；描述这些实例的主要特征，讨论各实例的"难度"差在哪里。

### E386

- 位置：Optimization Studies 标准，Desirable
- 原文："justifies the use of synthetic data (if any); explain why real-world data cannot be used; discusses the extent to which the proposed approach and the findings can apply to the real world" / "selects a realistic option space for formulating a solution; any values set for attributes should reflect one that might be chosen in a "real-world" solution, and not generated from an arbitrary distribution"
- 要点：加分：用合成数据要说明理由及对现实的适用程度；解的选项空间要符合实际，属性取值应是现实中可能出现的，而不是从随意的分布中生成。

### E387

- 位置：Optimization Studies 标准，Desirable
- 原文："justifies the parameter values used when executing the evaluated approaches (and note that experiments trying a wide range of different parameter values would be extraordinary, see below)"
- 要点：加分：说明运行各方法时所用参数值的理由；尝试大范围参数值的实验属于"优秀"档。

### E388

- 位置：Optimization Studies 标准，Desirable
- 原文："compares distributions (rather than means) of results using appropriate statistics" / "clearly distinguishes evidence-based results from interpretations and speculation"
- 要点：加分：用合适的统计方法比较结果的分布，而不只是比较平均数；区分有证据的结果和解读、推测。

### E389

- 位置：Optimization Studies 标准，Desirable 及脚注 14
- 原文："provides a replication package that conforms to SIGSOFT standards for artifacts" / "Including, for example, source code (of approach, solution representation, and fitness calculations), datasets used as experiment input, and collected experiment data (e.g., output logs, generated solutions)."
- 要点：加分：提供复现包，包括方法、解的表示和适应度计算的源代码，实验输入数据，以及收集到的实验数据（输出日志、生成的解）。

### E390

- 位置：Optimization Studies 标准，Extraordinary
- 原文："analyzes different parameter choices to the algorithm, indicating how the final parameters were selected" / "analyzes the fitness landscape for one or more of the chosen fitness functions"
- 要点：优秀：分析算法的不同参数选择，并说明最终参数是怎么选出来的；分析适应度函数的"地形"（fitness landscape，即解空间中适应度值的分布形态）。

### E391

- 位置：Optimization Studies 标准，Examples of Acceptable Deviations
- 原文："The number of trials can be constrained by available time or experimental resources (e.g. where experiments are time-consuming to repeat or have human elements). In such cases, multiple trials are still ideal, but a limited number of trials can be justified as long as the limitations are disclosed and the possible effects of stochasticity are discussed."
- 要点：可接受的偏离：时间或资源有限时可以少做几次试验，但要披露这一局限并讨论随机性可能带来的影响。

### E392

- 位置：Optimization Studies 标准，Antipatterns
- 原文："Reporting significance tests (e.g., Mann-Whitney Wilcoxon test) without effect size tests" / "Conducting multiple trials but failing to disclose or discuss the variation between trials; for instance reporting a measure of central (e.g. median) without any indication of variance (e.g., a boxplot)."
- 要点：反面模式：只报显著性检验、不报效应量；做了多次试验却不披露或讨论试验之间的波动，例如只报中位数、不给箱线图之类的波动信息。

### E393

- 位置：Optimization Studies 标准，Invalid Criticisms
- 原文："The paper just uses older algorithms with no reference to recent work. Using  older (and widely understood algorithms) may be valid when they are used, e.g., (1) as part of a larger set that compares many approaches; e.g. (2) to offer a “straw man” method that defines the “floor” of the performance (that everything else needs to beat); or (3), as a workbench within which one thing is changed (e.g., the fitness function) but everything else remains constant."
- 要点：不成立的批评："只用了老算法"。老算法可以合理地用作众多对比方法之一、作为性能"底线"、或作为只改一处（如适应度函数）其余不变的实验平台。

### E394

- 位置：Optimization Studies 标准，Invalid Criticisms
- 原文："That an approach is not benchmarked against an inappropriate or unavailable baseline." / "That a multi-objective approach is not compared to a single-objective approach by evaluating each objective separately." / "That one or very few subjects are used, as long as the paper offers a reasonable justification for why this was the case."
- 要点：不成立的批评：没和不合适或拿不到实现的基线比；多目标方法没和逐个目标单独优化的方法比（多目标问题的关键在目标间的权衡）；研究对象很少但给了合理理由。

### E395

- 位置：Optimization Studies 标准，Invalid Criticisms
- 原文："It is more important to consider the Pareto frontiers and quality indicators."
- 要点：评价多目标优化，更重要的是看帕累托前沿（Pareto front，即无法在不牺牲某个目标的情况下改进另一个目标的那组解）和相应的质量指标。

### E396

- 位置：Optimization Studies 标准，Notes
- 原文："Regarding the difference between "significance" and "effect size" tests: "Significance" checks if distributions can be distinguished from each other while "Effect size" tests are required to check if the difference between distributions is "interesting" (and not just a trivially "small effect")."
- 要点：显著性检验回答"两个分布能不能区分开"；效应量回答"差异是否大到值得关注"，而不是微不足道的小差异。

### E397

- 位置：Simulation 标准，标题下的定义
- 原文："A study that involves developing and using a mathematical model that imitates a real-world system's behavior, which often entails problem understanding, data collection, model development, verification, validation, design of experiments, data analysis, and implementation of results."
- 要点：仿真研究的定义：建立并使用一个模仿真实系统行为的数学模型，通常包括理解问题、收集数据、建模、验证、确认、实验设计、数据分析和落实结果。

### E398

- 位置：Simulation 标准，Application
- 原文："Use this standard for _in silico_ simulations, i.e., studies representing everything using computational models. For _in virtuo_ simulations, i.e., human participants manipulating simulation models, use the **Experiments (with human participants) Standard**. For simulations used to assess a new or improved technological artifact, also consider the **Engineering Research** standard."
- 要点：本标准适用于一切都用计算模型表示的仿真（in silico）；有人操作仿真模型的研究（in virtuo）用有人参与的实验标准；用仿真评估新制品时，还要参考工程研究标准。

### E399

- 位置：Simulation 标准，Essential（intro）
- 原文："justifies that simulation is a suitable method for investigating the problem (or research question, etc.)"
- 要点：必要：说明为什么仿真适合研究这个问题。

### E400

- 位置：Simulation 标准，Essential（method）及脚注 1
- 原文："describes the simulation model (conceptual, implementation, or hybrid abstraction levels), including input parameters and response variables" / "describes the underlying simulation approach" / "e.g. discrete-event simulation, system dynamics, agent-based simulation" / "describes simulation packages or tools used to develop and run the simulation model, including version numbers, and computational environments"
- 要点：必要：描述仿真模型（概念层、实现层或两者结合），包括输入参数和响应变量；说明仿真方法（如离散事件仿真、系统动力学、基于智能体的仿真）；说明所用仿真软件包或工具的版本和计算环境。

### E401

- 位置：Simulation 标准，Essential（method）
- 原文："describes the data used for model calibration, the calibration procedures, and contextual information"
- 要点：必要：说明用于模型校准的数据、校准过程和数据的背景信息。

### E402

- 位置：Simulation 标准，Essential（method）及脚注 2
- 原文："describes how the simulation model was verified and validated at different abstraction levels" / "Some verification and validation procedures may be applied to the model at the conceptual level (e.g., validating variables and relationships) down to an implementation level (e.g., using tests, reproducing reference behaviors, or performing simulated experiments)."
- 要点：必要：说明在不同抽象层次上怎样验证和确认模型：概念层（检查变量和关系）到实现层（测试、重现参考行为、做仿真实验）。

### E403

- 位置：Simulation 标准，Essential（method）
- 原文："describes the study protocol, including independent variables, scenarios, number of runs per scenario (in case of using stochastic simulation), and steady-state or terminating conditions"
- 要点：必要：描述研究方案：自变量、场景、每个场景运行的次数（随机仿真时），以及稳态条件或终止条件。

### E404

- 位置：Simulation 标准，Essential（method）及脚注 3
- 原文："analyzes validity threats considering the supporting data and the simulation model" / "Simulation studies are prone to several validity threats, including non-representative simulation scenarios, insufficient verification and validation, using different datasets (contexts) for model calibration and experimentation, and others" / "clearly explicates the assumptions of the simulation model"
- 要点：必要：结合支撑数据和模型本身分析效度威胁，例如场景不具代表性、验证与确认不足、校准和实验用了不同背景的数据；明确写出模型的假设。

### E405

- 位置：Simulation 标准，Desirable
- 原文："provides supplementary materials including the raw data (for real data) or generation mechanism (for synthetic data) used for model calibration, all simulation models and source code, analysis scripts"
- 要点：加分：提供补充材料：校准用的原始数据（或合成数据的生成机制）、全部仿真模型和源代码、分析脚本。

### E406

- 位置：Simulation 标准，Desirable 及脚注 4
- 原文："characterizes reference behaviors for the definition of simulation scenarios with representative and known values or probability distributions for input parameters" / "Reference behaviors represent a real-world model (often based on actual measurement of a system or process), which is characterized by data distribution or series of model variables. Usually, these models are used for validating simulation outcomes."
- 要点：加分：用有代表性的已知取值或概率分布刻画"参考行为"，据此定义仿真场景。参考行为通常来自对真实系统或过程的实测，常用来确认仿真结果。

### E407

- 位置：Simulation 标准，Desirable
- 原文："separates conceptual and implementation levels of the simulation model" / "reports sensitivity analysis for input parameters or factors" / "clearly distinguishes evidence-based results from interpretations and speculation"
- 要点：加分：分开描述模型的概念层和实现层；报告输入参数或因素的敏感性分析；区分有证据的结果和解读、推测。

### E408

- 位置：Simulation 标准，Extraordinary 及脚注 6
- 原文："describes how stakeholders were involved in developing and validating the simulation model" / "All of these stakeholders could, for example, be involved in checking the plausibility of the model output (face validity check)."
- 要点：优秀：说明利益相关者（数据提供者、领域专家、模型使用者）如何参与建模和确认，例如检查模型输出是否合理（表面效度检查）。

### E409

- 位置：Simulation 标准，Antipatterns 及脚注 8
- 原文："Overfitting the simulation model to reproduce a reference behavior." / "For instance, implementing a specific model capable of only producing desired outcomes." / "Using a single run instead of multiple runs to experiment with stochastic models."
- 要点：反面模式：为了重现参考行为而过度拟合模型，例如造一个只能产生期望结果的模型；对随机模型只跑一次。

### E410

- 位置：Simulation 标准，Antipatterns 及脚注 9
- 原文："Use of non-standard experimental designs without justification." / "Houston et al. (2001) discusses some usual experimental design for software process simulation, such as (fractional) factorial designs."
- 要点：反面模式：没有理由地使用非标准的实验设计。常用设计如（部分）因子设计。

### E411

- 位置：Simulation 标准，Examples of Acceptable Deviations
- 原文："If insufficient data is available (or too costly to collect) to calibrate the model, assumptions can be used to implement parts of the model. These assumptions, however, must be explained and justified."
- 要点：可接受的偏离：校准数据不足或太贵时，模型的部分内容可以用假设代替，但必须说明并给出理由。

### E412

- 位置：Simulation 标准，Invalid Criticisms
- 原文："The mere presence of assumptions in the model is not a valid basis for criticism _as long as_ the assumptions are documented and justified, and their implications for the validity of the simulation are sufficiently addressed. All models make assumptions."
- 要点：不成立的批评："模型有假设"。所有模型都有假设，只要写明、给出理由、并讨论了对效度的影响即可。

### E413

- 位置：Simulation 标准，Invalid Criticisms
- 原文："Claiming that the model is too abstact without explaining why the level of abstraction is inadequate for the purposes of the study." / "Claiming that the study is invalid because it uses generated data, secondary data or approximations based on expert opinion, _when no appropriate primary data is available_."
- 要点：不成立的批评：说模型"太抽象"却不解释为什么这个抽象层次不够用；在没有合适一手数据时，因为用了生成数据、二手数据或专家估计就否定研究。

### E414

- 位置：Case Study and Ethnography，标题下的定义
- 原文："An empirical inquiry that investigates a contemporary phenomenon (the "case") in depth and within its real-world context, especially when the boundaries between phenomenon and context are unclear"
- 要点：案例研究的定义（引自 Yin 2017）：在真实环境中深入考察一个当下的现象（"案例"），尤其适用于现象和环境的边界不清楚的情况。

### E415

- 位置：Case Study and Ethnography，Application
- 原文："Presents a detailed account of a specific instance of a *phenomenon* at a *site*. [...] The site can be a community, an organization, a team, a person, a process, an internet platform, etc."
- 要点：案例研究详细描述某个现象在某个"现场"中的一个具体实例；现场可以是社区、组织、团队、个人、流程、互联网平台等。

### E416

- 位置：Case Study and Ethnography，Application
- 原文："Is not an experience report (cf. Perry et al. 2004) or a series of shallow inquiries at many different sites."
- 要点：经验报告不是案例研究，在许多现场各做一点浅层调查也不是。

### E417

- 位置：Case Study and Ethnography，Application
- 原文："A case study can be brief (e.g. a week of observation) or longitudinal (if observation exceeds the natural rhythm of the site; e.g., observing a product over many releases). For our purposes, *case study subsumes ethnography*."
- 要点：案例研究可以很短（如观察一周），也可以是纵向的；这份标准把民族志归入案例研究。

### E418

- 位置：Case Study and Ethnography，Application
- 原文："If data collection and analysis are interleaved, consider the **Grounded Theory** Standard. If the study mentions action research, or intervenes in the context, consider the **Action Research** Standard."
- 要点：数据收集和分析交替进行时参考扎根理论标准；研究者介入现场时参考行动研究标准。

### E419

- 位置：Case Study and Ethnography，Essential Attributes
- 原文："justifies the selection of the case(s) or site(s) that was(were) studied" / "describes the site(s) in rich detail" / "the site is a real (physical or virtual) place, not a toy example or imaginary world"
- 要点：必要项：论证为什么选这个案例或现场；详细描述现场；现场必须真实存在（实体或虚拟），不能是玩具例子或虚构情境。

### E420

- 位置：Case Study and Ethnography，Essential Attributes
- 原文："reports the type of case study" / "describes data sources (e.g. participants' demographics and work roles)" / "defines unit(s) of analysis or observation"
- 要点：必要项：说明是哪种案例研究；描述数据来源（如参与者的背景和工作角色）；定义分析或观察单元。

### E421

- 位置：Case Study and Ethnography，Essential Attributes
- 原文："presents a clear chain of evidence from observations to findings"
- 要点：必要项：从观察到结论有一条清楚的证据链。

### E422

- 位置：Case Study and Ethnography，Desirable Attributes
- 原文："provides supplemental materials such as interview guide(s), coding schemes, coding examples, decision rules, or extended chain-of-evidence tables"
- 要点：加分项：提供补充材料，如访谈提纲、编码方案、编码示例、决策规则、扩展的证据链表格。

### E423

- 位置：Case Study and Ethnography，Desirable Attributes
- 原文："triangulates across data sources, informants or researchers" / "cross-checks interviewee statements (e.g. against direct observation or archival records)"
- 要点：加分项：在数据来源、信息提供者或研究者之间做三角验证；用直接观察或档案记录核对受访者的说法。

### E424

- 位置：Case Study and Ethnography，Desirable Attributes 及脚注 2
- 原文："uses participant observation (ethnography) or direct observation (non-ethnography) and clearly integrates these observations into results" / "Direct observation means watching research subjects without getting involved; participant observation means joining in with whatever participants are doing"
- 要点：加分项：使用参与式观察（民族志）或直接观察，并把观察结果整合进结论。直接观察是只看不参与；参与式观察是加入参与者正在做的事。

### E425

- 位置：Case Study and Ethnography，Desirable Attributes
- 原文："describes external events and other factors that may have affected the case or site" / "describes how prior understandings of the phenomena were managed and/or influenced the research"
- 要点：加分项：描述可能影响案例的外部事件和其他因素；说明研究者原有的理解是怎样被处理的、对研究有什么影响。

### E426

- 位置：Case Study and Ethnography，Desirable Attributes 及脚注 4
- 原文："uses quotations to *illustrate* findings" / "Quotations should not be *the only* representation of a finding; each finding should be described independently of supporting quotations"
- 要点：加分项：用引语来说明结论；但引语不能是结论的唯一表达，每条结论要脱离引语独立陈述。

### E427

- 位置：Case Study and Ethnography，Desirable Attributes
- 原文："researchers reflect on their own possible biases"
- 要点：加分项：研究者反思自己可能有的偏见。

### E428

- 位置：Case Study and Ethnography，Extraordinary Attributes
- 原文："multiple, deep, fully-developed cases with cross-case triangulation" / "uses a team-based approach; e.g., multiple raters with analysis of inter-rater reliability" / "published a case study protocol beforehand and made it publicly accessible"
- 要点：优秀项：多个深入、完整的案例并做跨案例三角验证；团队分析，如多人编码并分析一致性；事先公开发布案例研究方案。

### E429

- 位置：Case Study and Ethnography，General Quality Criteria
- 原文："Case studies should be evaluated using qualitative validity criteria such as credibility, multivocality, reflexivity, rigor, and transferability [...] Quantitative quality criteria such as replicability, generalizability and objectivity typically do not apply."
- 要点：案例研究应该用定性研究的效度标准评价（可信度、多声音性、反思性、严谨性、可迁移性）；可复制性、可推广性、客观性等定量标准一般不适用。

### E430

- 位置：Case Study and Ethnography，Types of Case Studies
- 原文："There is no standard way of conducting a case study. Case study research can adopt different philosophies"
- 要点：案例研究没有唯一标准做法，可以采用不同的哲学立场。

### E431

- 位置：Case Study and Ethnography，Types of Case Studies
- 原文："an **explanatory case study** explains how or why a phenomenon occurred, typically using a process or variance theory" / "an **exploratory case study** explores a particular phenomenon to identify new questions, propositions or hypotheses" / "an **historical case study** draws on archival data, for instance, software repositories" / "a **revelatory case study** examines a hitherto unknown or unexplored phenomenon"
- 要点：类型举例：解释型（解释现象如何、为何发生）、探索型（找出新问题、命题或假设）、历史型（使用档案数据，例如软件仓库）、揭示型（考察以前未知或未被研究过的现象）。

### E432

- 位置：Case Study and Ethnography，Antipatterns
- 原文："Relying on a single approach to data collection (e.g. interviews) without corroboration or data triangulation" / "Oversimplifying and over-rationalizing complex phenomena; presenting messy, complicated things as simple and clean"
- 要点：反面模式：只靠一种数据收集方式（如只做访谈）、不做印证；把复杂、混乱的现象讲得过于简单、过于合理。

### E433

- 位置：Case Study and Ethnography，Invalid Criticisms
- 原文："Sample of one; findings not generalizable. The point of a case study is to study one thing deeply, not to generalize to a population. Case studies should lead to theoretical generalization; that is, concepts that are transferable in principle."
- 要点：不成立的批评："样本只有一个，结论无法推广"。案例研究的目的是深入研究一个对象，而不是推广到总体；它应当带来理论上的推广，即原则上可迁移的概念。

### E434

- 位置：Case Study and Ethnography，Invalid Criticisms
- 原文："Does not present quantitative data." / "Lack of internal validity. Internal validity only applies to explanatory case studies that seek to establish causality."
- 要点：不成立的批评："没有定量数据"；"缺乏内部效度"（内部效度只适用于想确立因果关系的解释型案例研究）。

### E435

- 位置：Case Study and Ethnography，Invalid Criticisms
- 原文："Lack of reproducibility or a "replication package"; Data are not disclosed (qualitative data are often confidential)." / "Insufficient number or length of interviews. There is no magic number; what matters is that there is enough data that the findings are credible, and the description is deep and rich."
- 要点：不成立的批评："不可复现、没有复现包、数据没公开"（定性数据常常是保密的）；"访谈数量或时长不够"（没有神奇的数字，关键是数据足以让结论可信、描述深入丰富）。

## Glossary

### E436

- 位置：Glossary，Credibility / Transferability / Reflexivity
- 原文："the extent to which conclusions are supported by rich, multivocal evidence" / "the extent to which a study’s results could plausibly apply to other sites, people or circumstances" / "the extent to which authors reflect on their potential biases and interactions with the team, organization or community, especially possible negative impacts on some participants or stakeholders"
- 要点：可信度：结论在多大程度上有丰富、多方声音的证据支持；可迁移性：结果在多大程度上可能适用于其他现场、人群或情境；反思性：作者在多大程度上反思自己的偏见，以及自己与团队、组织或社区的互动（尤其是可能对某些参与者造成的负面影响）。

### E437

- 位置：Glossary，Multivocal
- 原文："The property of being based on—and recognizing differences between—people with different opinions and backgrounds (including gender, culture, education, and class)."
- 要点：多声音性：基于不同观点和背景的人，并承认他们之间的差异。

### E438

- 位置：Glossary，Gatekeeper
- 原文："A person or organization who controls access to individuals (e.g., employees) or data being researched. Gatekeepers may influence individual’s participation decisions (e.g., employers may coerce employees to participate), affect research outcomes (e.g., by controlling whose voices are heard) or be affected by research outcomes (e.g., lose credibility with employees)."
- 要点：把关人：控制研究者能否接触到人员（如员工）或数据的个人或组织。他们可能影响个人是否参与（如雇主强迫员工参与），影响研究结果（如决定谁的声音被听到），也可能受研究结果影响。

## Ethics (Studies with Human Participants) 补充标准

### E439

- 位置：Ethics (Studies with Human Participants)，Application
- 原文："This standard applies to studies in which one or more human beings other than the researchers take part in the research (e.g. Action Research, Case Study, Grounded Theory, Qualitative Surveys, Experiments, Questionnaire Surveys)."
- 要点：有研究者以外的人参与的研究（包括案例研究）都适用这份伦理补充标准。

### E440

- 位置：Case Study and Ethnography，Suggested Readings
- 原文："(Note: we recommend beginning with Yin's book.)"
- 要点：标准建议从 Yin 的案例研究方法专著读起。

### E441

- 位置：General Standard，General Quality Criteria，Examples of Acceptable Deviations
- 原文："A study can only apply an **empirical standard** if an appropriate standard exists. If no related standards exist, studies should apply published guidance. If no appropriate guidance exists, reviewers should apply the general standard and construct an ad hoc evaluation scheme for the new method."
- 要点：只有存在合适的标准时，研究才能套用它；没有相关标准，就按已发表的指南做；连合适的指南也没有，审稿人用通用标准，并为这种新方法临时建一套评价办法。
