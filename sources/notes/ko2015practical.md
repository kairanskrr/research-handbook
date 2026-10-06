# Ko, LaToza & Burnett 2015：A practical guide to controlled experiments of software engineering tools with human participants

- 资料：`ko2015practical`，[作者主页上的作者版本](https://faculty.washington.edu/ajko/papers/Ko2013SEToolEvaluations.pdf)
- 版本：Empirical Software Engineering 20(1), 2015（2013 年在线发表）；作者自存版（Author's personal copy）

### E1

- 位置：§2 Designing Tool Evaluation Experiments
- 原文："How do developers use it? What concepts must they understand to use it successfully? How long does it take to learn? [...] Experiments, as inherently comparative methods, cannot easily answer such questions. Instead, these questions are more easily investigated with non-experimental quantitative or qualitative methods. Moreover, answers to these formative questions are often necessary to obtain before one knows which comparisons, which tasks, which developers, and which measures even make sense for an experiment"
- 要点：开发者怎么用一个工具、需要懂哪些概念、要学多久这类问题，实验很难回答，因为实验本质上是做比较；这类问题更适合用非实验的定量或定性方法。而且往往要先回答这类问题，才知道实验该比较什么、用什么任务、招什么人、测什么。

### E2

- 位置：§2 Designing Tool Evaluation Experiments
- 原文："Quantitative controlled experiments allow isolation of variables through control: more than other methods, experiments provide the most rigorous evidence that it is the isolated variable(s), such as the particular tool, and not some other factor such as a developer's experience or real-world circumstances, that led to a difference in some software engineering outcome. The tradeoff for this control, as we discuss throughout the rest of this article, is artificiality."
- 要点：对照实验通过控制把变量隔离出来，比其他方法更能证明是这个变量（如工具）而不是别的因素（如经验）造成了差异；代价是人为、不够真实。

### E3

- 位置：§2 Designing Tool Evaluation Experiments
- 原文："A key property of this experimental design is that every participant receives the exact same materials, instruction, tasks, and environment, except for which tool they receive. If there is a difference in the outcomes between the two groups, one can then make a strong claim that this was due to the research tool and nothing else."
- 要点：这种设计的关键是：除了用哪个工具，所有参与者拿到的材料、说明、任务和环境完全一样；这样两组结果有差异时，才能有力地说是工具造成的。

### E4

- 位置：§2 Designing Tool Evaluation Experiments
- 原文："In fact, one strategy for designing an experiment is to draft the human subjects approval form and method section first, as a draft of an experimental design. This can help to identify flaws and uncover details that have yet to be defined."
- 要点：一种设计实验的办法是先起草伦理审查申请表和论文的方法部分，把它当作设计草稿，能帮助发现缺陷和还没定下来的细节。

### E5

- 位置：§2 Designing Tool Evaluation Experiments
- 原文："Variation in the measurement of outcome variables is the primary reason for negative experimental results: the noisier the signal, the more difficult it is to observe underlying differences in the signal. However, some of this variation is natural and should be preserved [...] The "unnatural" variation, or extraneous variation, is the variation to eliminate."
- 要点：结果变量测量中的波动是实验得出负面结果的主要原因；有些波动是自然的、应保留，要消除的是实验人为造成的"无关波动"。

### E6

- 位置：§3.1 Deciding Who to Recruit
- 原文："More generally, good inclusion criteria reflect the characteristics of the people that a researcher believes would benefit from using the research tool, and the work contexts in which the researcher believes the tool would be useful"
- 要点：好的纳入标准反映研究者认为会从工具中受益的那类人，以及工具会派上用场的工作情境。

### E7

- 位置：§3.1 Deciding Who to Recruit
- 原文："we found that 62 % of studies evaluating a tool actually involved the tool's inventors themselves using the tool and reporting on their personal experiences" / "In general, inventors who evaluate a tool by using it themselves might provide useful insights about the applicability of a tool, but little about whether someone else would benefit from it in practice."
- 要点：作者的系统综述发现，62% 的工具评估其实是工具发明者自己用、自己报告体验；这能说明工具的适用性，却说明不了别人用了会不会受益。

### E8

- 位置：§3.1 Deciding Who to Recruit
- 原文："Students may also pose other validity concerns, such as the subjectexpectancy effect, in which participants who expect a certain outcome behave in a way that ensures it."
- 要点：学生参与者可能带来"被试期望效应"：参与者预期某种结果，就会做出让这个结果成真的行为。

### E9

- 位置：§3.1 Deciding Who to Recruit
- 原文："That said, students can be appropriate participants when their knowledge, skills, and experiences fit within a tool's intended user population." / "One can also mitigate subject-expectancy effects by presenting the experiment in a way that suggests that the researcher has no stake in the outcome."
- 要点：学生的知识、技能和经验符合工具的目标用户时，可以用学生；把实验介绍得让人看不出研究者在乎哪种结果，可以减轻被试期望效应。

### E10

- 位置：§3.2 Deciding How Many Participants to Recruit
- 原文："Experiments recruited a median of 36 participants, ranging from 2 to 222, with a median of 18 participants per condition." / "While approximately 20 participants per condition are not guaranteed to be a large enough sample to overcome variation in measurements, it is a reasonable number to start with, provided that appropriate statistical tests are used."
- 要点：作者综述的实验参与者中位数为 36 人，每组中位数 18 人；每组约 20 人不保证够，但配合合适的统计检验，可以作为起点。

### E11

- 位置：§3.2 Deciding How Many Participants to Recruit
- 原文："A more principled way to decide how many participants to recruit is to do a prospective power analysis [...] it generally requires three inputs: (1) the expected effect size (the difference in the outcome variable between groups), (2) the expected variation in this outcome measurement, and (3) the Type I error rate"
- 要点：更有依据的做法是事先做功效分析（power analysis），需要三个输入：预期效应量、结果测量的预期波动、第一类错误率。

### E12

- 位置：§3.2 Deciding How Many Participants to Recruit
- 原文："One source of these estimates is to use data from previous experiments on the tool or even pilot studies"
- 要点：功效分析需要的效应量和波动，可以用以前的实验或预实验的数据来估计。

### E13

- 位置：§3.3 Doing the Recruiting
- 原文："When writing recruitment materials or interviewing a potential participant, it is important to ask about inclusion criteria in a neutral manner, so that it is not clear to recruits what the "right" answers are."
- 要点：招募材料和筛选问题要问得中立，不让应征者看出"正确答案"，否则急于参加的人可能谎报。

### E14

- 位置：§4.1 Informed Consent
- 原文："These forms of harm can occur in software engineering experiments that ask participants to complete particularly difficult tasks, especially if the participants do not have adequate experience to be successful."
- 要点：要求参与者完成特别难的任务时，尤其是经验不足的参与者，可能造成压力、尴尬等伤害。

### E15

- 位置：§4.2 Gathering Demographic Data
- 原文："There is also the possibility that by asking about participants' experience just before a task, the less experienced participants may feel less confident in their ability to succeed at it because they will be reminded of their inexperience. This effect, known as stereotype threat, can have a significant effect on skilled performance"
- 要点：任务前询问经验，可能提醒经验少的人自己缺乏经验，削弱信心（刻板印象威胁），显著影响表现；所以背景信息也可以放在任务之后收集。

### E16

- 位置：§4.3 Assigning Participants to an Experimental Condition
- 原文："Most studies use simple random assignment, distributing random variation in participants' skills and behaviors across all conditions, minimizing the chance that some observed difference in the groups' performance is due to participant differences, rather than differences in the tools being compared."
- 要点：多数研究用简单随机分组，把参与者技能和行为的随机差异均匀分到各组，降低"组间差异其实来自人而不是工具"的可能。

### E17

- 位置：§4.3 Assigning Participants to an Experimental Condition
- 原文："One alternative is the within-subjects experiment (Rosenthal and Rosnow 2007), where all of the participants in a study use all of the tools being compared, one at a time, across several tasks."
- 要点：被试内实验：每个参与者在不同任务上依次使用所有被比较的工具。

### E18

- 位置：§4.3 Assigning Participants to an Experimental Condition
- 原文："one must randomize both the order of tasks and on which tasks a participant gets to use the experimental tool. This randomization is known as counterbalancing" / "When there are more than two tools being compared, counterbalancing can be achieved by mapping conditions onto a Latin Square"
- 要点：被试内设计有学习效应，必须随机安排任务顺序以及在哪个任务上用实验工具，这叫平衡（counterbalancing）；比较两个以上工具时可用拉丁方安排。

### E19

- 位置：§4.3 Assigning Participants to an Experimental Condition
- 原文："downsides to within-subjects designs, including fatigue or boredom: giving a developer multiple tasks to complete with multiple different tools could be exhausting and require an impractical amount of their time."
- 要点：被试内设计的缺点是疲劳和厌倦：让一个人用多种工具完成多项任务，可能累垮人、耗时太长。

### E20

- 位置：§4.3 Assigning Participants to an Experimental Condition
- 原文："A disadvantage of an interrupted time-series design is that it provides less confidence about causality, because it is harder to rule out the effect of confounding variables that co-occurred during the introduction and removal of the tool."
- 要点：中断时间序列设计（引入工具前、引入后、撤掉后各测一次）对因果的把握更弱，因为难以排除同时发生的混杂因素。

### E21

- 位置：§4.4 Training Participants
- 原文："The decision of what to teach and what to have participants learn during the tasks is a key experimental design consideration: whatever information is provided during training becomes an assumption about the conditions in which the tool will be used."
- 要点：教什么、留给参与者在任务中自己学什么，是关键设计决定：培训里给的信息，会变成"工具在什么条件下使用"的前提假设。

### E22

- 位置：§4.4 Training Participants
- 原文："This suggests that there is an inherent bias in controlled experiments toward evaluating tools that can be quickly learned, and against tools that require significant practice."
- 要点：对照实验天生偏向能快速学会的工具，而不利于需要长期练习的工具。

### E23

- 位置：§5 Task Design
- 原文："One of the challenges in controlled experimental design is the tradeoff between realism and control (Sjøberg et al. 2003): realistic study designs provide for greater generalizability, but involve fewer controls, making it more difficult to know with certainty what causes any differences observed in an experiment."
- 要点：真实性和控制之间要权衡：越真实越能推广，但控制越少，越难确定差异由什么造成。

### E24

- 位置：§5.3 Task Origin
- 原文："The benefit of designing a task from scratch is that it can be tailored specifically to exercise the features of the tool. The risk in doing this is that the task will not adequately reflect the types of tasks that occur in practice. There is also a risk that the new task gives the tool an unrealistic advantage over the baseline tool in the study."
- 要点：自己设计任务能针对工具功能，但可能不代表实际任务，还可能让工具相对基线获得不真实的优势。

### E25

- 位置：§5.5 Task Duration
- 原文："This can lead to ceiling effects (Rosenthal and Rosnow 2007) on outcome measures, making it difficult to statistically discriminate between the outcomes of two groups because everyone does so well. Tasks may also be so difficult that no one can complete them in the allotted time no matter which tool they use (called a floor effect"
- 要点：任务太简单，人人都完成，出现天花板效应；太难，谁都完不成，出现地板效应；两种情况都看不出工具之间的差异。

### E26

- 位置：§6.1 Measuring Success on Task
- 原文："For software engineering tasks, defining success involves determining three things: (1) the goal state or states that a participant must reach to be counted as successful, (2) a method for determining when a goal state has been reached, and (3) a method of communicating the goal to participants that all participants will interpret similarly."
- 要点：定义任务成功要定三件事：达到什么状态算成功、怎么判断达到了、怎么把目标讲给参与者使所有人理解一致。

### E27

- 位置：§6.2 Measuring Time on Task
- 原文："Clearly, time on task and success on task trade off with each other (Wickelgren 1977). [...] Because of this tradeoff, it is helpful to measure both, so that one can see how each developer managed speed and quality."
- 要点：用时和成功率此消彼长，最好两个都测，才能看出每个人怎样在速度和质量间取舍。

### E28

- 位置：§6.3 Measuring Usefulness
- 原文："For example, Dell et al. (2012) found that when interviewing participants about a novel system, they were 2.5 times more likely to prefer the technology they believed to be designed by the interviewer, even when the technology was inferior. Therefore, simply asking a developer whether they find a tool "useful" is likely not to produce meaningful data."
- 要点：参与者明显偏爱他们以为是访谈者设计的技术（即使更差，偏好也高 2.5 倍）；所以直接问"这个工具有用吗"很可能得不到有意义的数据。

### E29

- 位置：§6.3 Measuring Usefulness
- 原文："Rather than simply ask if they find a tool "useful", one can instead use a previously validated instrument, such as the Technology Acceptance Model (embodied as a questionnaire)"
- 要点：可以用经过验证的量表（如技术接受模型问卷）代替一句"有用吗"。

### E30

- 位置：§7 Debriefing and Compensation
- 原文："Participants should not leave a study feeling as if they "failed," especially when tasks may have been designed to ensure that not every participant would succeed." / "Instructions about information that they should not share with others. For example, if one is recruiting from a student population, students might share the answers to the tasks with their friends, who may later participate in the study."
- 要点：结束后的说明（debriefing）应让参与者不带着"失败"感离开；还要嘱咐不要外传任务答案，以免后来的参与者事先知道。

### E31

- 位置：§8 Piloting
- 原文："Therefore, a critical step in preparing an experiment is to run pilots (Keppel 1982): test runs of a study intended to find sources of extraneous variation. Our systematic review suggests that pilots may not yet be standard practice in software engineering research. We found that only 11 of the 345 studies"
- 要点：预实验（pilot，正式实验前的试运行）是准备实验的关键一步，用来找出无关波动的来源；但作者综述的 345 项研究中只有 11 项明确提到做过。

### E32

- 位置：§8 Piloting
- 原文："the most important phase of piloting is testing the study design with the actual setup in which the study will be conducted, with as close to the same participants, physical set-up, handouts, tutorials, questionnaires, procedures, and experimenters as possible" / "Any data collected should be discarded, as the purpose of a pilot is to find problems in the experiment that need to be fixed, not to gather data"
- 要点：最重要的预实验要尽量用与正式实验相同的参与者类型、场地、材料、流程和实验人员；预实验数据应丢弃，它的目的是找问题，不是收集数据。

### E33

- 位置：§8 Piloting
- 原文："Sandbox pilots are prepilots in which the researchers themselves are the participants."
- 要点："沙盒预实验"是研究者自己当参与者的预演，便于在找外人之前先排除明显问题。

### E34

- 位置：§3.1 Deciding Who to Recruit
- 原文："In fact, in our systematic literature review, we did not find a single paper that attempted an experiment in the context of a team, let alone an experiment that actually recruited multiple teams to use a new software engineering tool."
- 要点：作者的综述中没有一篇论文在团队情境下做实验；面向团队的工具很难用对照实验评估。
