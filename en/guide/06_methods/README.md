# Research methods

You have chosen a research strategy and know what kind of evidence you need. Now you want to know: which method will actually get you that evidence, and how do you do that method well?

That is the question this part of the handbook answers.

## How methods and strategies divide the work

- **A research strategy** is about what knowledge the project produces and what evidence it needs; see [Research strategies](../05_research-strategies/README.md).
- **A research method** is about how to do the work well: the steps, the key decisions, a checklist, and common mistakes.
- **One method can serve several strategies.** A controlled experiment, for example, can compare two existing tools, and it can also test "X causes Y". That is why each row in the tables below lists the strategies the method usually serves.
- **Which methods live here**: methods used by two or more fields go in this section; practices used by only one field go in that field's folder (see the end of this page).

This division is a convention of this handbook `[Our analysis]`.

For how to choose a strategy and a method based on your question, see [Choosing a strategy and a method](../02_from-project-to-study/02_choose-strategy-and-method.md).

## 28 methods

The "Strategies it usually serves" column is based on the "Common research methods" section of each strategy page; where no strategy page lists the method, it says "Not yet listed". The "Originally written for" column says where the method page's sources mainly come from, not that only that field uses the method.

### Using published research as material

| Method | What it does | Originally written for | Strategies it usually serves |
|---|---|---|---|
| [Review studies](review_study.md) | Systematic reviews, mapping studies, and survey papers: collecting published research, then summarizing and analyzing it | Computer science | [Synthesis](../05_research-strategies/synthesize.md), [Description](../05_research-strategies/observe_describe.md) |
| [Case survey](case_survey.md) | Coding a large number of published case studies into a dataset, then analyzing it quantitatively | Computer science | [Synthesis](../05_research-strategies/synthesize.md) |
| [Methodology research and meta-science](meta_science.md) | Research on how to do research: methods guidelines, critical reviews, and surveys of research practice | Computer science | [Synthesis](../05_research-strategies/synthesize.md), [Measurement](../05_research-strategies/measure.md) |
| [Systematic reviews and meta-analysis (health research)](meta_analysis.md) | Systematic reviews that ask "how well does this intervention work", using statistics to combine the results of several studies into one overall estimate | Health sciences | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Synthesis](../05_research-strategies/synthesize.md) |

### Based on existing data or models

| Method | What it does | Originally written for | Strategies it usually serves |
|---|---|---|---|
| [Data science research](data_science.md) | Predictive or statistical modeling of existing data, using the results to answer a scientific question | Computer science | [Description](../05_research-strategies/observe_describe.md) |
| [Longitudinal studies](longitudinal_study.md) | Observing the same subjects repeatedly over a long period to see how they change | Computer science | [Description](../05_research-strategies/observe_describe.md) |
| [Quantitative simulation](simulation_study.md) | Building a computational model that imitates a real system and running experiments on the model | Computer science | [Building and improving](../05_research-strategies/build_improve.md) |
| [Quasi-experiments and causal identification](quasi_experiment.md) | When you can't randomize, estimating causal effects from observational data with difference-in-differences, regression discontinuity, instrumental variables, and similar designs | Economics and business | [Causal explanation](../05_research-strategies/explain_causality.md) |
| [Observational epidemiology](observational_epidemiology.md) | Cohort, case-control, and cross-sectional studies: the researcher observes without intervening | Health sciences | [Causal explanation](../05_research-strategies/explain_causality.md), [Description](../05_research-strategies/observe_describe.md) |

### Research involving people

| Method | What it does | Originally written for | Strategies it usually serves |
|---|---|---|---|
| [Controlled experiments](controlled_experiment.md) | With human participants and random assignment, comparing how one factor affects people's performance | Computer science | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Causal explanation](../05_research-strategies/explain_causality.md), [Building and improving](../05_research-strategies/build_improve.md) |
| [Randomized controlled trials](randomized_controlled_trial.md) | Randomly assigning participants to different intervention groups and comparing their outcomes | Clinical medicine | [Causal explanation](../05_research-strategies/explain_causality.md) |
| [Field experiments](field_experiment.md) | Working with a government, company, or community to randomly decide who receives an intervention in the real world, then comparing the groups' results | Economics and business | [Causal explanation](../05_research-strategies/explain_causality.md) |
| [Questionnaire surveys](questionnaire_survey.md) | Collecting data from many people with a questionnaire, then analyzing it systematically | Computer science | [Description](../05_research-strategies/observe_describe.md), [Measurement](../05_research-strategies/measure.md) |
| [Scale development and measurement studies](scale_development.md) | The measuring instrument itself is the result: developing a new scale, translating and adapting one, or building up reliability and validity evidence for an existing one | Psychology and cognitive science | [Measurement](../05_research-strategies/measure.md) |
| [Interview studies](interview_study.md) | In-depth interviews with a group of people, with qualitative analysis to identify themes | Computer science | [Description](../05_research-strategies/observe_describe.md) |
| [Oral history](oral_history.md) | Interviewing people who lived through events, recording and archiving the interviews, then using them as evidence that has to be checked | History and archaeology | [Interpretation and argument](../05_research-strategies/interpret_argue.md) |
| [Case study and ethnography](case_study.md) | Studying a small number of subjects in depth in their real setting | Computer science | [Description](../05_research-strategies/observe_describe.md), [Causal explanation](../05_research-strategies/explain_causality.md) |
| [Grounded theory](grounded_theory.md) | Collecting and analyzing data at the same time, gradually building a theory from the data | Computer science | [Description](../05_research-strategies/observe_describe.md) |
| [Action research](action_research.md) | Working with a real organization to bring about a change, researching it while improving it | Computer science | [Building and improving](../05_research-strategies/build_improve.md), [Description](../05_research-strategies/observe_describe.md) |

### Experiments and observation in the lab and the field

| Method | What it does | Originally written for | Strategies it usually serves |
|---|---|---|---|
| [Bench experiments (wet lab)](bench_experiment.md) | Treating cultured cells, extracted molecules, and reagents at the bench and comparing them with controls to test a hypothesis | Biological sciences | [Causal explanation](../05_research-strategies/explain_causality.md) |
| [Preclinical animal studies](preclinical_animal_study.md) | Experiments on living animals to provide evidence for human medicine | Basic medical sciences | [Causal explanation](../05_research-strategies/explain_causality.md) |
| [Synthesis and characterization studies](synthesis_study.md) | Designing a route, running reactions, purifying and characterizing products, and reporting yields and substrate scope | Chemical sciences | [Building and improving](../05_research-strategies/build_improve.md) |
| [Experimental measurement](experimental_measurement.md) | Measuring the value of a physical quantity and showing how far that value can be trusted | Physical sciences | [Measurement](../05_research-strategies/measure.md) |
| [Field studies: observation and sampling](field_study.md) | Setting up sites in rivers, soil, the atmosphere, and so on, measuring and sampling, then using the data to answer a question | Earth and environmental sciences | [Description](../05_research-strategies/observe_describe.md) |

### Using archives and cases as material

| Method | What it does | Originally written for | Strategies it usually serves |
|---|---|---|---|
| [Archival research](archival_research.md) | Consulting unpublished original records and using them to answer questions about the past | History and archaeology | [Interpretation and argument](../05_research-strategies/interpret_argue.md) |
| [Process tracing and comparative case studies](process_tracing.md) | Checking step by step how something happened within one case, or deliberately selecting a few cases to compare with each other | Political science | [Causal explanation](../05_research-strategies/explain_causality.md) |

### Across methods

| Method | What it does | Originally written for | Strategies it usually serves |
|---|---|---|---|
| [Replication studies](replication.md) | Redoing a published study in a planned way to test whether its conclusions hold | Computer science | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Measurement](../05_research-strategies/measure.md) |
| [Mixed methods](mixed_methods.md) | Studying the same question with two or more methods | Computer science | [Causal explanation](../05_research-strategies/explain_causality.md) |

The grouping is ours, made to help you find things `[Our analysis]`.

## Scope of these method pages

`[Our analysis]` Each of these method pages was originally written for computer science or for one other field, and moved to this section later because more than one field uses the method:

- **The 14 pages originally written for computer science** are aimed mainly at software engineering: most of their checklists follow the Empirical Standards of the Association for Computing Machinery's Special Interest Group on Software Engineering (ACM SIGSOFT), and most of their examples come from software engineering.
- **The 14 pages originally written for other fields** follow that field's norms and sources; for example, the randomized controlled trial page follows medicine's trial reporting guidelines, and the quasi-experiment page describes how economists do it.

The methods themselves are used in many fields, but the specific norms differ from field to field. Each page says at the top which field it was originally written for and where its sources come from. If you are not in the field a page was written for, read your own field's norms and practices first, and use the method page here as a reference.

## Field-specific practices

Research practices used by only one field live under `practices/` in that field's folder.

### Other fields

| Field | Practices |
|---|---|
| Agriculture, forestry and fisheries | [Field trials](../07_fields/agriculture/practices/field_trial.md) |
| Social and economic geography | [Spatial analysis](../07_fields/geography/practices/spatial_analysis.md) |
| Education | [Design-based research](../07_fields/education/practices/design_based_research.md) |
| Law | [Doctrinal legal research](../07_fields/law/practices/doctrinal_research.md) |
| History and archaeology | [Archaeological excavation and field survey](../07_fields/history-archaeology/practices/archaeological_excavation.md) |
| Languages and literature | [Close reading and literary argument](../07_fields/languages-literature/practices/close_reading.md), [Language documentation and linguistic fieldwork](../07_fields/languages-literature/practices/language_documentation.md) |
| Philosophy, ethics and religion | [Philosophical argument](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md) |
| Arts | [Practice-based research](../07_fields/arts/practices/practice_based_research.md) |

For each field's overall conventions, see [Fields](../07_fields/README.md).

### Computer science

Research practices used only in computer science live in `07_fields/computer-science/practices/`:

- [Engineering research](../07_fields/computer-science/practices/engineering_research.md): proposing and evaluating new methods, tools or systems
- [Benchmarking](../07_fields/computer-science/practices/benchmarking.md): comparing systems, tools or models with an automated, repeatable process
- [Optimization studies](../07_fields/computer-science/practices/optimization_study.md): modeling a problem as an optimization problem and solving it by search
- [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md): mining data from code repositories, bug databases, and question-and-answer sites
- [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md): proofs and formal analysis
