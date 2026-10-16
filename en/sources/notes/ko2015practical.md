# Ko, LaToza & Burnett 2015: A practical guide to controlled experiments of software engineering tools with human participants

- Source: `ko2015practical`, [author's version on the author's homepage](https://faculty.washington.edu/ajko/papers/Ko2013SEToolEvaluations.pdf)
- Version: Empirical Software Engineering 20(1), 2015 (published online 2013); author's personal copy

### E1

- Location: §2 Designing Tool Evaluation Experiments
- Quote: "How do developers use it? What concepts must they understand to use it successfully? How long does it take to learn? [...] Experiments, as inherently comparative methods, cannot easily answer such questions. Instead, these questions are more easily investigated with non-experimental quantitative or qualitative methods. Moreover, answers to these formative questions are often necessary to obtain before one knows which comparisons, which tasks, which developers, and which measures even make sense for an experiment"
- Key point: Questions such as how developers use a tool, what concepts they must understand, and how long it takes to learn are hard to answer with experiments, which are inherently comparative; they are better studied with non-experimental quantitative or qualitative methods. Often you must answer them first to know what an experiment should compare, which tasks to use, whom to recruit, and what to measure.

### E2

- Location: §2 Designing Tool Evaluation Experiments
- Quote: "Quantitative controlled experiments allow isolation of variables through control: more than other methods, experiments provide the most rigorous evidence that it is the isolated variable(s), such as the particular tool, and not some other factor such as a developer's experience or real-world circumstances, that led to a difference in some software engineering outcome. The tradeoff for this control, as we discuss throughout the rest of this article, is artificiality."
- Key point: Controlled experiments isolate variables through control and, more than other methods, show that the isolated variable (such as the tool), not some other factor (such as experience), caused the difference; the price is artificiality.

### E3

- Location: §2 Designing Tool Evaluation Experiments
- Quote: "A key property of this experimental design is that every participant receives the exact same materials, instruction, tasks, and environment, except for which tool they receive. If there is a difference in the outcomes between the two groups, one can then make a strong claim that this was due to the research tool and nothing else."
- Key point: The key to this design is that every participant gets exactly the same materials, instructions, tasks, and environment except for the tool; then a difference between the groups can be strongly attributed to the tool.

### E4

- Location: §2 Designing Tool Evaluation Experiments
- Quote: "In fact, one strategy for designing an experiment is to draft the human subjects approval form and method section first, as a draft of an experimental design. This can help to identify flaws and uncover details that have yet to be defined."
- Key point: One way to design an experiment is to draft the ethics review application and the paper's method section first, as a draft design; this helps reveal flaws and details not yet decided.

### E5

- Location: §2 Designing Tool Evaluation Experiments
- Quote: "Variation in the measurement of outcome variables is the primary reason for negative experimental results: the noisier the signal, the more difficult it is to observe underlying differences in the signal. However, some of this variation is natural and should be preserved [...] The "unnatural" variation, or extraneous variation, is the variation to eliminate."
- Key point: Variation in outcome measurements is the main reason experiments produce negative results; some variation is natural and should be kept, while extraneous variation introduced by the experiment should be removed.

### E6

- Location: §3.1 Deciding Who to Recruit
- Quote: "More generally, good inclusion criteria reflect the characteristics of the people that a researcher believes would benefit from using the research tool, and the work contexts in which the researcher believes the tool would be useful"
- Key point: Good inclusion criteria reflect the people the researcher believes would benefit from the tool and the work contexts in which it would be useful.

### E7

- Location: §3.1 Deciding Who to Recruit
- Quote: "we found that 62 % of studies evaluating a tool actually involved the tool's inventors themselves using the tool and reporting on their personal experiences" / "In general, inventors who evaluate a tool by using it themselves might provide useful insights about the applicability of a tool, but little about whether someone else would benefit from it in practice."
- Key point: The authors' systematic review found that 62% of tool evaluations involved the tool's inventors using it themselves and reporting their experience; this can show the tool's applicability but not whether others would benefit from it.

### E8

- Location: §3.1 Deciding Who to Recruit
- Quote: "Students may also pose other validity concerns, such as the subjectexpectancy effect, in which participants who expect a certain outcome behave in a way that ensures it."
- Key point: Student participants may introduce the subject-expectancy effect: participants who expect a certain outcome behave in ways that make it happen.

### E9

- Location: §3.1 Deciding Who to Recruit
- Quote: "That said, students can be appropriate participants when their knowledge, skills, and experiences fit within a tool's intended user population." / "One can also mitigate subject-expectancy effects by presenting the experiment in a way that suggests that the researcher has no stake in the outcome."
- Key point: Students can be appropriate participants when their knowledge, skills, and experience fit the tool's intended users; presenting the experiment so that it is unclear which outcome the researcher wants can mitigate subject-expectancy effects.

### E10

- Location: §3.2 Deciding How Many Participants to Recruit
- Quote: "Experiments recruited a median of 36 participants, ranging from 2 to 222, with a median of 18 participants per condition." / "While approximately 20 participants per condition are not guaranteed to be a large enough sample to overcome variation in measurements, it is a reasonable number to start with, provided that appropriate statistical tests are used."
- Key point: The experiments in the authors' review had a median of 36 participants and 18 per condition; about 20 per condition is not guaranteed to be enough, but combined with appropriate statistical tests it is a reasonable starting point.

### E11

- Location: §3.2 Deciding How Many Participants to Recruit
- Quote: "A more principled way to decide how many participants to recruit is to do a prospective power analysis [...] it generally requires three inputs: (1) the expected effect size (the difference in the outcome variable between groups), (2) the expected variation in this outcome measurement, and (3) the Type I error rate"
- Key point: A more principled approach is a prospective power analysis, which needs three inputs: the expected effect size, the expected variation in the outcome measure, and the Type I error rate.

### E12

- Location: §3.2 Deciding How Many Participants to Recruit
- Quote: "One source of these estimates is to use data from previous experiments on the tool or even pilot studies"
- Key point: The effect size and variation for a power analysis can be estimated from data in previous experiments or pilot studies.

### E13

- Location: §3.3 Doing the Recruiting
- Quote: "When writing recruitment materials or interviewing a potential participant, it is important to ask about inclusion criteria in a neutral manner, so that it is not clear to recruits what the "right" answers are."
- Key point: Write recruitment materials and screening questions neutrally, so recruits cannot tell the "right" answers; otherwise people eager to take part may misreport.

### E14

- Location: §4.1 Informed Consent
- Quote: "These forms of harm can occur in software engineering experiments that ask participants to complete particularly difficult tasks, especially if the participants do not have adequate experience to be successful."
- Key point: Asking participants, especially inexperienced ones, to complete particularly difficult tasks can cause harm such as stress and embarrassment.

### E15

- Location: §4.2 Gathering Demographic Data
- Quote: "There is also the possibility that by asking about participants' experience just before a task, the less experienced participants may feel less confident in their ability to succeed at it because they will be reminded of their inexperience. This effect, known as stereotype threat, can have a significant effect on skilled performance"
- Key point: Asking about experience right before a task can remind less experienced participants of their inexperience and lower their confidence (stereotype threat), significantly affecting performance; so background information can be collected after the task instead.

### E16

- Location: §4.3 Assigning Participants to an Experimental Condition
- Quote: "Most studies use simple random assignment, distributing random variation in participants' skills and behaviors across all conditions, minimizing the chance that some observed difference in the groups' performance is due to participant differences, rather than differences in the tools being compared."
- Key point: Most studies use simple random assignment, which spreads random differences in participants' skills and behaviors across all conditions and reduces the chance that group differences come from the people rather than the tool.

### E17

- Location: §4.3 Assigning Participants to an Experimental Condition
- Quote: "One alternative is the within-subjects experiment (Rosenthal and Rosnow 2007), where all of the participants in a study use all of the tools being compared, one at a time, across several tasks."
- Key point: In a within-subjects experiment, every participant uses all the tools being compared, one at a time, across several tasks.

### E18

- Location: §4.3 Assigning Participants to an Experimental Condition
- Quote: "one must randomize both the order of tasks and on which tasks a participant gets to use the experimental tool. This randomization is known as counterbalancing" / "When there are more than two tools being compared, counterbalancing can be achieved by mapping conditions onto a Latin Square"
- Key point: Within-subjects designs have learning effects, so you must randomize both the task order and which tasks use the experimental tool; this is counterbalancing. With more than two tools, a Latin square can be used.

### E19

- Location: §4.3 Assigning Participants to an Experimental Condition
- Quote: "downsides to within-subjects designs, including fatigue or boredom: giving a developer multiple tasks to complete with multiple different tools could be exhausting and require an impractical amount of their time."
- Key point: The downside of within-subjects designs is fatigue and boredom: having one person complete many tasks with several tools can be exhausting and take too long.

### E20

- Location: §4.3 Assigning Participants to an Experimental Condition
- Quote: "A disadvantage of an interrupted time-series design is that it provides less confidence about causality, because it is harder to rule out the effect of confounding variables that co-occurred during the introduction and removal of the tool."
- Key point: An interrupted time-series design (measuring before the tool is introduced, after, and after it is removed) gives weaker evidence of causality, because confounders that co-occur are hard to rule out.

### E21

- Location: §4.4 Training Participants
- Quote: "The decision of what to teach and what to have participants learn during the tasks is a key experimental design consideration: whatever information is provided during training becomes an assumption about the conditions in which the tool will be used."
- Key point: What to teach and what to leave for participants to learn during the tasks is a key design decision: whatever training provides becomes an assumption about the conditions in which the tool will be used.

### E22

- Location: §4.4 Training Participants
- Quote: "This suggests that there is an inherent bias in controlled experiments toward evaluating tools that can be quickly learned, and against tools that require significant practice."
- Key point: Controlled experiments are inherently biased toward tools that can be learned quickly and against tools that require significant practice.

### E23

- Location: §5 Task Design
- Quote: "One of the challenges in controlled experimental design is the tradeoff between realism and control (Sjøberg et al. 2003): realistic study designs provide for greater generalizability, but involve fewer controls, making it more difficult to know with certainty what causes any differences observed in an experiment."
- Key point: There is a tradeoff between realism and control: realistic designs generalize better but have fewer controls, making it harder to know what caused a difference.

### E24

- Location: §5.3 Task Origin
- Quote: "The benefit of designing a task from scratch is that it can be tailored specifically to exercise the features of the tool. The risk in doing this is that the task will not adequately reflect the types of tasks that occur in practice. There is also a risk that the new task gives the tool an unrealistic advantage over the baseline tool in the study."
- Key point: Designing your own task lets you target the tool's features, but the task may not reflect real-world tasks and may give the tool an unrealistic advantage over the baseline.

### E25

- Location: §5.5 Task Duration
- Quote: "This can lead to ceiling effects (Rosenthal and Rosnow 2007) on outcome measures, making it difficult to statistically discriminate between the outcomes of two groups because everyone does so well. Tasks may also be so difficult that no one can complete them in the allotted time no matter which tool they use (called a floor effect"
- Key point: If a task is too easy, everyone succeeds (a ceiling effect); if too hard, no one does (a floor effect); either way you cannot see differences between tools.

### E26

- Location: §6.1 Measuring Success on Task
- Quote: "For software engineering tasks, defining success involves determining three things: (1) the goal state or states that a participant must reach to be counted as successful, (2) a method for determining when a goal state has been reached, and (3) a method of communicating the goal to participants that all participants will interpret similarly."
- Key point: Defining task success means deciding three things: the goal state that counts as success, how to determine it has been reached, and how to communicate the goal so every participant understands it the same way.

### E27

- Location: §6.2 Measuring Time on Task
- Quote: "Clearly, time on task and success on task trade off with each other (Wickelgren 1977). [...] Because of this tradeoff, it is helpful to measure both, so that one can see how each developer managed speed and quality."
- Key point: Time on task and success trade off against each other, so measure both to see how each person balanced speed and quality.

### E28

- Location: §6.3 Measuring Usefulness
- Quote: "For example, Dell et al. (2012) found that when interviewing participants about a novel system, they were 2.5 times more likely to prefer the technology they believed to be designed by the interviewer, even when the technology was inferior. Therefore, simply asking a developer whether they find a tool "useful" is likely not to produce meaningful data."
- Key point: Participants strongly favor technology they believe the interviewer designed (2.5 times more likely to prefer it, even when it is inferior), so simply asking "is this tool useful?" is unlikely to yield meaningful data.

### E29

- Location: §6.3 Measuring Usefulness
- Quote: "Rather than simply ask if they find a tool "useful", one can instead use a previously validated instrument, such as the Technology Acceptance Model (embodied as a questionnaire)"
- Key point: Instead of asking "is it useful?", use a previously validated instrument such as the Technology Acceptance Model questionnaire.

### E30

- Location: §7 Debriefing and Compensation
- Quote: "Participants should not leave a study feeling as if they "failed," especially when tasks may have been designed to ensure that not every participant would succeed." / "Instructions about information that they should not share with others. For example, if one is recruiting from a student population, students might share the answers to the tasks with their friends, who may later participate in the study."
- Key point: The debriefing should make sure participants do not leave feeling they "failed," and should ask them not to share task answers so later participants do not know them in advance.

### E31

- Location: §8 Piloting
- Quote: "Therefore, a critical step in preparing an experiment is to run pilots (Keppel 1982): test runs of a study intended to find sources of extraneous variation. Our systematic review suggests that pilots may not yet be standard practice in software engineering research. We found that only 11 of the 345 studies"
- Key point: Piloting (test runs before the real experiment) is a critical step for finding sources of extraneous variation, yet only 11 of the 345 studies in the authors' review explicitly mention doing it.

### E32

- Location: §8 Piloting
- Quote: "the most important phase of piloting is testing the study design with the actual setup in which the study will be conducted, with as close to the same participants, physical set-up, handouts, tutorials, questionnaires, procedures, and experimenters as possible" / "Any data collected should be discarded, as the purpose of a pilot is to find problems in the experiment that need to be fixed, not to gather data"
- Key point: The most important pilot uses as closely as possible the same type of participants, setting, materials, procedures, and experimenters as the real study; pilot data should be discarded, since the goal is to find problems, not collect data.

### E33

- Location: §8 Piloting
- Quote: "Sandbox pilots are prepilots in which the researchers themselves are the participants."
- Key point: "Sandbox pilots" are prepilots in which the researchers themselves act as participants, to remove obvious problems before involving outsiders.

### E34

- Location: §3.1 Deciding Who to Recruit
- Quote: "In fact, in our systematic literature review, we did not find a single paper that attempted an experiment in the context of a team, let alone an experiment that actually recruited multiple teams to use a new software engineering tool."
- Key point: The authors' review found not a single paper that ran an experiment in a team context; tools aimed at teams are hard to evaluate with controlled experiments.
