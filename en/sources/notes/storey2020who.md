# Storey et al. 2020: The Who, What, How of Software Engineering Research: A Socio-Technical Framework

- Source: `storey2020who`, [original (arXiv)](https://arxiv.org/abs/1905.12841)
- Version: arXiv 1905.12841v3 (May 2020), the author version of Empirical Software Engineering 25(5): 4097-4129, 2020. Locations give subsections.

### E1

- Location: §2 Background
- Quote: "But the analysis of trace data alone is fraught with threats to validity as it shows an incomplete picture of human behaviour, intent and social interactions in software engineering"
- Key point: Analyzing only the trace data left by development activities (commits, review comments, forum posts, and so on) carries many threats to validity, because it shows only part of people's behavior, intentions, and social interactions.

### E2

- Location: §3.3 How Is the Research Conducted?
- Quote: "It is important to not confuse research strategy with research method. A research method is a technique used to collect data." / "In contrast, a research strategy is a broader term [38] that may involve the use of one or more methods for collecting data."
- Key point: Research strategies and research methods are different: a method is a technique for collecting data (such as interviews); a strategy is a broader concept that can include one or more data collection methods.

### E3

- Location: §3.3 How Is the Research Conducted?
- Quote: "Every empirical research strategy has strengths and weaknesses to consider in terms of research quality criteria [30], and every study design decision leads to trade-offs in terms of the potential to increase or decrease quality criteria." / "Since all strategies have inherent strengths and weaknesses, it may be important to triangulate across research strategies to mitigate the weaknesses of using a single strategy" / "Generalizability of the evidence over the population of human or system actors studied;" / "Realism of the context where the evidence was collected and needs to apply;" / "Control of extraneous human behaviour variables that may impact the evidence being collected; and" / "Precision of the system data that is collected as evidence."
- Key point: Each empirical research strategy has strengths and weaknesses on the quality criteria (generalizability, realism, control over human variables, and data precision), and every design decision is a trade-off; so triangulation across strategies may be needed to make up for the weaknesses of any single strategy.

### E4

- Location: §6.2 The Downside of Using Data Strategies for Studying Human Aspects
- Quote: "For descriptive research that aims to capture human and social aspects, data alone may also not tell the whole story and any conclusions drawn should be corroborated with other methods (such as interviews, surveys, or observations)."
- Key point: For research that describes human and social aspects, the data alone cannot tell the whole story; conclusions should be corroborated with other methods such as interviews, surveys, or observation.

### E5

- Location: §6.2 The Downside of Using Data Strategies for Studying Human Aspects
- Quote: "For example, a solution paper that proposes a recommender system of possible defects may need to be evaluated with human actors to see how the tool perturbs the context in which it is used"
- Key point: Example: a paper proposing a bug recommender system may need to evaluate it in use by real people, to see how the tool changes the context in which it is used.

### E6

- Location: §6.2 The Downside of Using Data Strategies for Studying Human Aspects
- Quote: "In some cases, this may be justified. For example, a study that evaluates a new technique to improve the build time of a project may not benefit from human feedback as the faster compilation probably implies a better developer experience."
- Key point: Not all research needs to include the human perspective; for example, when evaluating a new technique for reducing build time, human feedback adds little.

### E7

- Location: §6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- Quote: "Methodological triangulation refers to using different strategies and/or methods, while data triangulation refers to when the same research method may be used but different sources of data are used."
- Key point: Method triangulation means using different strategies or methods; data triangulation means using the same method with different data sources.

### E8

- Location: §6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- Quote: "While the use of data triangulation may improve generalizability, it does not improve realism or control over human variables."
- Key point: Data triangulation (for example, repeating the analysis on more datasets) may improve generalizability, but it does not improve realism or strengthen control over human variables.

### E9

- Location: §6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- Quote: "For the data strategy papers, the vast majority did not triangulate their findings with other strategy quadrants, but when triangulation did occur, data strategies were mostly triangulated with a respondent strategy (surveys or interviews)."
- Key point: Among the 2017 ICSE and EMSE papers the authors analyzed, the vast majority of data-centric papers did not triangulate with other strategies; those that did mostly added a survey or interviews.

### E10

- Location: §6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- Quote: "We could not determine whether authors triangulated their work outside of the papers we considered, and we recognize that the responsibility for triangulation does not need to be on the level of individual papers."
- Key point: The authors acknowledge that the burden of triangulation need not fall on a single paper; it can be carried out by follow-up or other studies.

### E11

- Location: §6.4 Using Triangulation to Balance Benefits for Human and Technical Aspects
- Quote: "In sum, multiple research strategies should be used to support triangulation, not just to triangulate specific findings, but to further add to insights concerning software engineering problem contexts, possible solutions for those problems, and the evaluation of those solutions"
- Key point: Using multiple research strategies is not only about corroborating a specific finding, but also about deepening understanding of the problem context, possible solutions, and their evaluation.

### E12

- Location: §3.3.1 Field Strategies
- Quote: "A field study is where the researcher observes (e.g., through an ethnography) study subjects without any explicit interventions in place. With a field study, realism is high but control over human activities is low, and generalizability is low as only a limited number of companies are typically considered." / "A field experiment may be more obtrusive than a field study, and thus will lower realism, but it has the potential for higher control over human participants’ activities."
- Key point: Field studies: the researcher observes without intervening; realism is high, but control over human activity is low, and since they usually involve only a few companies, generalizability is also low. Field experiments are more intrusive, which lowers realism but may give more control over participants' activities.

### E13

- Location: §3.3.2 Lab Strategies
- Quote: "Control of human actor activities may be achieved but at the expense of realism (the setting is contrived), and it may be more difficult to achieve generalizable results." / "Doing so increases realism but at the expense of control over variables that may come into play in a simulated environment where human actors may have more freedom to act naturally."
- Key point: Laboratory strategies can control human activity, at the cost of realism (the setting is artificial), and make generalizable results harder to obtain; simulating a real environment increases realism at the cost of weaker control.

### E14

- Location: §3.3.3 Respondent Strategies
- Quote: "The ability to collect data from many participants using respondent strategies has the potential for higher generalizability (if a broad and large sample is recruited), but at the expense of lower realism as factors that may influence each individual participant’s responses cannot be observed or anticipated."
- Key point: Respondent strategies such as surveys and interviews can collect data from many people, and with a broad, large sample generalizability may be higher, at the cost of lower realism: the factors that shape each person's answers can be neither seen nor anticipated.

### E15

- Location: §3.3.4 Data Strategies
- Quote: "Data strategy papers have lower control over human behavioral variables but have the potential for higher precision of system data. They may have potential for higher realism (if the data was collected from field sites) and higher generalizability (if the project data is from many projects)."
- Key point: Data strategies give less control over human behavioral variables, but system data may be more precise; realism may be higher when the data come from real field settings, and generalizability higher when the data come from many projects.

### E16

- Location: Abstract
- Quote: "We find that the majority of the 151 papers published in both venues in 2017 (ICSE and the EMSE journal) present research that the authors claim should benefit human stakeholders at some point in time, but most of these do not use research strategies that directly involve human participants."
- Key point: Of 151 papers from ICSE and the EMSE journal in 2017, most claim that the research will ultimately benefit people, but most of them do not use research strategies that directly involve people.

### E17

- Location: Abstract
- Quote: "we find that the majority of papers published at ICSE 2017 presented solutions (mostly technical) to address a software engineering problem, while" / "the majority of papers published in the EMSE journal in 2017 are descriptive contributions that present insights about software engineering problems or how technical solutions are used."
- Key point: Most ICSE 2017 papers propose (mostly technical) solutions; most 2017 papers in the EMSE journal make descriptive contributions about software engineering problems or how technical solutions are used.

### E18

- Location: §1 Introduction
- Quote: "The Empirical Software Engineering and Measurement (ESEM) conference and the Empirical Software Engineering (EMSE) journal also attract papers that consider social aspects as their focus is on empirical methods, many of which directly involve human participants."
- Key point: The ESEM conference and the EMSE journal focus on empirical methods and also attract papers on social aspects, many of which use methods that directly involve people.
