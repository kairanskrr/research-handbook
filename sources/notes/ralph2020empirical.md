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
