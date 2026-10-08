# Storey 等人 2020：The Who, What, How of Software Engineering Research: A Socio-Technical Framework

- 资料：`storey2020who`，[原文（arXiv）](https://arxiv.org/abs/1905.12841)
- 版本：arXiv 1905.12841v3（2020 年 5 月），Empirical Software Engineering 25(5): 4097–4129, 2020 的作者版本。位置写到小节。

### E1

- 位置：§2 Background
- 原文："But the analysis of trace data alone is fraught with threats to validity as it shows an incomplete picture of human behaviour, intent and social interactions in software engineering"
- 要点：只分析开发活动留下的痕迹数据（提交、评审意见、论坛帖子等）有很多效度威胁，因为它只呈现了人的行为、意图和社会互动的一部分。

### E2

- 位置：§3.3 How Is the Research Conducted?
- 原文："It is important to not confuse research strategy with research method. A research method is a technique used to collect data." / "In contrast, a research strategy is a broader term [38] that may involve the use of one or more methods for collecting data."
- 要点：研究策略和研究方法不同：方法是收集数据的技术（如访谈）；策略是更宽的概念，可以包含一种或多种收集数据的方法。

### E3

- 位置：§3.3 How Is the Research Conducted?
- 原文："Every empirical research strategy has strengths and weaknesses to consider in terms of research quality criteria [30], and every study design decision leads to trade-offs in terms of the potential to increase or decrease quality criteria." / "Since all strategies have inherent strengths and weaknesses, it may be important to triangulate across research strategies to mitigate the weaknesses of using a single strategy" / "Generalizability of the evidence over the population of human or system actors studied;" / "Realism of the context where the evidence was collected and needs to apply;" / "Control of extraneous human behaviour variables that may impact the evidence being collected; and" / "Precision of the system data that is collected as evidence."
- 要点：每种实证研究策略在质量标准（推广性、真实性、对人为变量的控制、数据精度）上各有长短，每个设计决定都是权衡；因此可能需要跨策略做三角验证，弥补单一策略的弱点。

### E4

- 位置：§6.2 The Downside of Using Data Strategies for Studying Human Aspects
- 原文："For descriptive research that aims to capture human and social aspects, data alone may also not tell the whole story and any conclusions drawn should be corroborated with other methods (such as interviews, surveys, or observations)."
- 要点：描述人和社会层面的研究，单靠数据讲不出全部故事，结论应当用访谈、问卷或观察等其他方法印证。

### E5

- 位置：§6.2 The Downside of Using Data Strategies for Studying Human Aspects
- 原文："For example, a solution paper that proposes a recommender system of possible defects may need to be evaluated with human actors to see how the tool perturbs the context in which it is used"
- 要点：例子：一篇提出缺陷推荐系统的论文，可能需要在真人使用中评估，看工具怎样改变它所处的使用环境。

### E6

- 位置：§6.2 The Downside of Using Data Strategies for Studying Human Aspects
- 原文："In some cases, this may be justified. For example, a study that evaluates a new technique to improve the build time of a project may not benefit from human feedback as the faster compilation probably implies a better developer experience."
- 要点：并非所有研究都需要加入人的视角，例如评估缩短构建时间的新技术，人的反馈帮助不大。

### E7

- 位置：§6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- 原文："Methodological triangulation refers to using different strategies and/or methods, while data triangulation refers to when the same research method may be used but different sources of data are used."
- 要点：方法三角验证指使用不同的策略或方法；数据三角验证指用同一种方法、不同的数据来源。

### E8

- 位置：§6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- 原文："While the use of data triangulation may improve generalizability, it does not improve realism or control over human variables."
- 要点：数据三角验证（例如在更多数据集上重复）可能提高推广性，但不能提高真实性，也不能加强对人为变量的控制。

### E9

- 位置：§6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- 原文："For the data strategy papers, the vast majority did not triangulate their findings with other strategy quadrants, but when triangulation did occur, data strategies were mostly triangulated with a respondent strategy (surveys or interviews)."
- 要点：在作者分析的 ICSE 和 EMSE 2017 年论文中，以数据为主的论文绝大多数没有和其他策略做三角验证；做了的，多数是配上问卷或访谈。

### E10

- 位置：§6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- 原文："We could not determine whether authors triangulated their work outside of the papers we considered, and we recognize that the responsibility for triangulation does not need to be on the level of individual papers."
- 要点：作者承认，三角验证的责任不一定要落在单篇论文上，也可以由后续或其他研究完成。

### E11

- 位置：§6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- 原文："In sum, multiple research strategies should be used to support triangulation, not just to triangulate specific findings, but to further add to insights concerning software engineering problem contexts, possible solutions for those problems, and the evaluation of those solutions"
- 要点：使用多种研究策略不仅是为了印证某个具体发现，也是为了加深对问题背景、可能的解决方案及其评估的理解。

### E12

- 位置：§3.3.1 Field Strategies
- 原文："A field study is where the researcher observes (e.g., through an ethnography) study subjects without any explicit interventions in place. With a field study, realism is high but control over human activities is low, and generalizability is low as only a limited number of companies are typically considered." / "A field experiment may be more obtrusive than a field study, and thus will lower realism, but it has the potential for higher control over human participants’ activities."
- 要点：现场研究：研究者不加干预地观察，真实性高，但对人的活动控制低，通常只涉及少数公司，推广性也低；现场实验更有侵入性，真实性降低，但对参与者活动的控制可能更高。

### E13

- 位置：§3.3.2 Lab Strategies
- 原文："Control of human actor activities may be achieved but at the expense of realism (the setting is contrived), and it may be more difficult to achieve generalizable results." / "Doing so increases realism but at the expense of control over variables that may come into play in a simulated environment where human actors may have more freedom to act naturally."
- 要点：实验室策略能控制人的活动，但代价是真实性（环境是人为布置的），也更难得到可推广的结果；模拟真实环境能提高真实性，代价是控制变弱。

### E14

- 位置：§3.3.3 Respondent Strategies
- 原文："The ability to collect data from many participants using respondent strategies has the potential for higher generalizability (if a broad and large sample is recruited), but at the expense of lower realism as factors that may influence each individual participant’s responses cannot be observed or anticipated."
- 要点：问卷、访谈这类受访者策略能从很多人那里收数据，样本广而大时推广性可能更高，代价是真实性较低：影响每个人回答的因素既看不到也预料不到。

### E15

- 位置：§3.3.4 Data Strategies
- 原文："Data strategy papers have lower control over human behavioral variables but have the potential for higher precision of system data. They may have potential for higher realism (if the data was collected from field sites) and higher generalizability (if the project data is from many projects)."
- 要点：数据策略对人的行为变量控制较低，但系统数据的精度可能更高；数据来自真实现场时真实性可能较高，来自很多项目时推广性可能较高。

### E16

- 位置：摘要
- 原文："We find that the majority of the 151 papers published in both venues in 2017 (ICSE and the EMSE journal) present research that the authors claim should benefit human stakeholders at some point in time, but most of these do not use research strategies that directly involve human participants."
- 要点：ICSE 和 EMSE 期刊 2017 年的 151 篇论文中，多数声称研究最终会让人受益，但其中大部分没有采用直接让人参与的研究策略。

### E17

- 位置：摘要
- 原文："we find that the majority of papers published at ICSE 2017 presented solutions (mostly technical) to address a software engineering problem, while" / "the majority of papers published in the EMSE journal in 2017 are descriptive contributions that present insights about software engineering problems or how technical solutions are used."
- 要点：ICSE 2017 的多数论文提出（多为技术性的）解决方案；EMSE 期刊 2017 年的多数论文是描述性贡献，讲软件工程问题或技术方案的使用情况。

### E18

- 位置：§1 Introduction
- 原文："The Empirical Software Engineering and Measurement (ESEM) conference and the Empirical Software Engineering (EMSE) journal also attract papers that consider social aspects as their focus is on empirical methods, many of which directly involve human participants."
- 要点：ESEM 会议和 EMSE 期刊以实证方法为重点，也吸引研究社会层面的论文，其中很多方法直接让人参与。
