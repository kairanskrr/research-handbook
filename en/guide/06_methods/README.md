# Research types: how to do them

This page is a directory. Look up your research by the name researchers actually use for it (user study, tool paper, benchmarking, review, controlled experiment, case study, replication, and so on), and it points you to the page that explains how to do it.

How to use it:

1. First finish [Converging on a project](../01_find-a-problem/05_converge.md), the last step of Part 1: write down the one sentence you want to prove, work out what evidence would convince people, and decide what kind of research this is.
2. In the tables below, find the name you or your field use for this kind of research and follow the link. One project often draws on two or three pages.
3. If you are not sure what kind of knowledge your research produces, start with the [Research strategies](../05_research-strategies/README.md) pages linked in the second-to-last column.

Take the running example, "published evaluations of large language model vulnerability detectors are inflated by data leakage." Most researchers would call this an empirical study or an evaluation study. It mainly draws on the [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) page, especially the section [Is the benchmark itself valid?](../07_fields/computer-science/practices/benchmarking.md#3-is-the-benchmark-itself-valid); the knowledge it produces belongs to the [Measurement](../05_research-strategies/measure.md) strategy `[Our analysis]`.

## Find it by what you call it

`[Our analysis]` The tables below are our own grouping, made to help you find things. The "You might call it" column collects common names, not strict definitions. The "Strategies it usually serves" column is based on the "Common research methods" section of each strategy page and on the opening of each page; where a strategy page doesn't list it, we say so. In the "Source" column, "method page" means a method used in several fields, and the field in parentheses is the one the page was originally written for; "[field] practice" means a practice used only in that field, kept in that field's folder.

### Using published research as material

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| literature review, systematic review, mapping study, survey paper | [Review studies](review_study.md) | Collects published research, then summarizes and analyzes it | [Synthesis](../05_research-strategies/synthesize.md), [Description](../05_research-strategies/observe_describe.md) | Method page (computer science) |
| case survey | [Case survey](case_survey.md) | Codes a large number of published case studies into a dataset, then analyzes it quantitatively | [Synthesis](../05_research-strategies/synthesize.md) | Method page (computer science) |
| methodology research, meta-science, meta-research, survey of research practice, critical review | [Methodology research and meta-science](meta_science.md) | Research on how to do research: methods guidelines, critical reviews, and surveys of research practice | [Synthesis](../05_research-strategies/synthesize.md), [Measurement](../05_research-strategies/measure.md) | Method page (computer science) |
| meta-analysis, systematic review of intervention effects | [Systematic reviews and meta-analysis (health research)](meta_analysis.md) | Answers "how well does this intervention work" by using statistics to combine the results of several studies into one overall estimate | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Synthesis](../05_research-strategies/synthesize.md) | Method page (health sciences) |

### Using existing data or models

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| data-driven study, predictive modeling, statistical modeling | [Data science research](data_science.md) | Builds predictive or statistical models of existing data and uses the results to answer a scientific question | [Description](../05_research-strategies/observe_describe.md) | Method page (computer science) |
| mining software repositories, empirical study of software repositories, empirical study (in software engineering, it often means this) | [Mining software repositories](../07_fields/computer-science/practices/repository_mining.md) | Mines data from code repositories, bug databases, and question-and-answer sites | [Description](../05_research-strategies/observe_describe.md), [Causal explanation](../05_research-strategies/explain_causality.md) | Computer science practice |
| longitudinal study, panel study | [Longitudinal studies](longitudinal_study.md) | Observes the same subjects repeatedly over a long period to see how they change | [Description](../05_research-strategies/observe_describe.md) | Method page (computer science) |
| simulation study, simulation experiment | [Quantitative simulation](simulation_study.md) | Builds a computational model that imitates a real system and runs experiments on the model | [Building and improving](../05_research-strategies/build_improve.md) | Method page (computer science) |
| quasi-experiment, natural experiment, causal inference, difference-in-differences, regression discontinuity, instrumental variables | [Quasi-experiments and causal identification](quasi_experiment.md) | Estimates causal effects from observational data when you can't randomize | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (economics and business) |
| cohort study, case-control study, cross-sectional study, observational study | [Observational epidemiology](observational_epidemiology.md) | The researcher does not intervene, only observes exposures and outcomes in a population | [Causal explanation](../05_research-strategies/explain_causality.md), [Description](../05_research-strategies/observe_describe.md) | Method page (health sciences) |
| spatial analysis, spatial regression, hot spot analysis | [Spatial analysis](../07_fields/geography/practices/spatial_analysis.md) | Uses location data to study how something is distributed in space and how surroundings or neighboring areas affect outcomes | [Description](../05_research-strategies/observe_describe.md), [Causal explanation](../05_research-strategies/explain_causality.md) | Social and economic geography practice |

### Research involving people

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| controlled experiment, user study, usability study, experiment with participants | [Controlled experiments](controlled_experiment.md) | With human participants and random assignment, compares how one factor affects people's performance | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Causal explanation](../05_research-strategies/explain_causality.md), [Building and improving](../05_research-strategies/build_improve.md) | Method page (computer science) |
| online controlled experiment, A/B test, split test, online experiment | [Online controlled experiments (A/B tests)](online_controlled_experiment.md) | Randomly assigns real users of a live website or app to the current version or a new one and compares the two groups' metrics | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Causal explanation](../05_research-strategies/explain_causality.md), [Building and improving](../05_research-strategies/build_improve.md) (not yet listed on the strategy pages) | Method page (computer science) |
| randomized controlled trial, clinical trial | [Randomized controlled trials](randomized_controlled_trial.md) | Randomly assigns participants to different intervention groups and compares their outcomes | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (clinical medicine) |
| field experiment, randomized evaluation | [Field experiments](field_experiment.md) | Works with a government, company, or community to randomly decide who receives an intervention in the real world, then compares the groups' results | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (economics and business) |
| questionnaire survey, survey (in the questionnaire sense) | [Questionnaire surveys](questionnaire_survey.md) | Collects data from many people with a questionnaire, then analyzes it systematically | [Description](../05_research-strategies/observe_describe.md), [Measurement](../05_research-strategies/measure.md) | Method page (computer science) |
| scale development, scale revision, reliability and validity testing of a scale, psychometric validation | [Scale development and measurement studies](scale_development.md) | Treats the measuring instrument itself as the result: developing a new scale, translating and adapting one, or building up reliability and validity evidence for an existing one | [Measurement](../05_research-strategies/measure.md) | Method page (psychology and cognitive science) |
| interview study, qualitative interviews, semi-structured interviews, qualitative study | [Interview studies](interview_study.md) | Interviews a set of people in depth and uses qualitative analysis to identify themes | [Description](../05_research-strategies/observe_describe.md) | Method page (computer science) |
| focus group, focus group discussion, group interview | [Focus groups](focus_group.md) | Brings a small group together for a discussion led by a moderator and gathers views from what they say and how they interact | [Description](../05_research-strategies/observe_describe.md) | Method page (health sciences) |
| oral history | [Oral history](oral_history.md) | Interviews people who lived through events, records and archives the interviews, then uses them as evidence that has to be checked | [Interpretation and argument](../05_research-strategies/interpret_argue.md) | Method page (history and archaeology) |
| case study, single-case study, ethnography | [Case study and ethnography](case_study.md) | Studies a small number of subjects in depth in their real setting | [Description](../05_research-strategies/observe_describe.md), [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (computer science) |
| grounded theory | [Grounded theory](grounded_theory.md) | Collects and analyzes data at the same time, gradually building a theory from the data | [Description](../05_research-strategies/observe_describe.md) | Method page (computer science) |
| action research | [Action research](action_research.md) | Works with a real organization to bring about a change, studying it while improving it | [Building and improving](../05_research-strategies/build_improve.md), [Description](../05_research-strategies/observe_describe.md) | Method page (computer science) |

### In the lab and in the field

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| wet-lab experiment, bench experiment, in vitro experiment | [Bench experiments (wet lab)](bench_experiment.md) | Treats cultured cells, extracted molecules, and reagents at the bench and compares them with controls to test a hypothesis | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (biological sciences) |
| animal study, preclinical study | [Preclinical animal studies](preclinical_animal_study.md) | Runs experiments on living animals to provide evidence for human medicine | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (basic medical sciences) |
| synthesis, synthetic methodology, characterization | [Synthesis and characterization studies](synthesis_study.md) | Designs a route, runs reactions, purifies and characterizes products, and reports yields and substrate scope | [Building and improving](../05_research-strategies/build_improve.md) | Method page (chemical sciences) |
| experimental measurement, precision measurement, uncertainty analysis | [Experimental measurement](experimental_measurement.md) | Measures the value of a physical quantity and shows how far that value can be trusted | [Measurement](../05_research-strategies/measure.md) | Method page (physical sciences) |
| field study, field sampling, field campaign, field monitoring | [Field studies: observation and sampling](field_study.md) | Sets up sites in rivers, soil, the atmosphere, and so on, measures and samples there, then uses the data to answer a question | [Description](../05_research-strategies/observe_describe.md) | Method page (earth and environmental sciences) |
| field trial, plot trial, multi-environment trial | [Field trials](../07_fields/agriculture/practices/field_trial.md) | Compares treatments such as varieties, fertilizers, or tillage on plots of a trial site | [Causal explanation](../05_research-strategies/explain_causality.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md) (not yet listed on the strategy pages) | Agriculture, forestry and fisheries practice |
| excavation, field archaeology, archaeological survey | [Archaeological excavation and field survey](../07_fields/history-archaeology/practices/archaeological_excavation.md) | Covers everything from writing the research design and doing non-invasive survey to excavating by stratigraphy, recording unit by unit, archiving, and writing the report | [Description](../05_research-strategies/observe_describe.md) (based on that page's opening; not yet listed on the strategy pages) | History and archaeology practice |
| language documentation, linguistic fieldwork | [Language documentation and linguistic fieldwork](../07_fields/languages-literature/practices/language_documentation.md) | Works with a community of speakers to record their language, transcribe, translate, and annotate it, deposit it in an archive, and then analyze it | [Description](../05_research-strategies/observe_describe.md) | Languages and literature practice |

### Archives, texts, and arguments

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| archival research, research with historical sources | [Archival research](archival_research.md) | Consults unpublished original records and uses them to answer questions about the past | [Interpretation and argument](../05_research-strategies/interpret_argue.md) | Method page (history and archaeology) |
| process tracing, comparative case study, small-N comparison | [Process tracing and comparative case studies](process_tracing.md) | Checks step by step how something happened within one case, or deliberately selects a few cases to compare with each other | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (political science) |
| close reading, literary criticism, literary analysis, interpretation of a work | [Close reading and literary argument](../07_fields/languages-literature/practices/close_reading.md) | Puts forward an interpretation of one or a few texts | [Interpretation and argument](../05_research-strategies/interpret_argue.md) | Languages and literature practice |
| doctrinal legal research, legal doctrine, case law research | [Doctrinal legal research](../07_fields/law/practices/doctrinal_research.md) | Establishes what the law is, evaluates the current law, and proposes reforms | [Interpretation and argument](../05_research-strategies/interpret_argue.md) | Law practice |
| philosophical argument, conceptual analysis | [Philosophical argument](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md) | Defends a thesis, clarifies concepts, and tests principles | [Interpretation and argument](../05_research-strategies/interpret_argue.md) | Philosophy, ethics and religion practice |
| theory paper, proof, formal analysis, machine-checked proof | [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md) | Makes theorems and proofs the main result: upper and lower bounds on algorithmic complexity, security of protocols, formal-methods proofs that a system has some property | [Proof](../05_research-strategies/prove.md) | Computer science practice |
| content analysis, quantitative content analysis, qualitative content analysis, coding, text coding, coding scheme / codebook | [Content analysis](content_analysis.md) | Systematically codes large amounts of text, media, posts, or documents into categories using a codebook, then counts or interprets them; when several people code, measures intercoder reliability | [Description](../05_research-strategies/observe_describe.md) (not yet listed on the strategy pages), [Synthesis](../05_research-strategies/synthesize.md) (when the material is published research; not yet listed on the strategy pages) | Method page (communication studies) |
| position paper, perspective, vision paper, reflection paper, essay | [Position papers](position_paper.md) | Argues for what a field should do or believe, and takes on the strongest opposing position | [Interpretation and argument](../05_research-strategies/interpret_argue.md) | Method page (computer science) |

### Proposing something new and evaluating it

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| engineering research, tool paper, technique paper, system paper, design science | [Engineering research](../07_fields/computer-science/practices/engineering_research.md) | Proposes and evaluates a new method, tool, or system: choosing baselines and benchmarks, designing the evaluation, releasing research artifacts | [Building and improving](../05_research-strategies/build_improve.md) | Computer science practice |
| benchmarking, benchmark study, evaluation study, tool comparison, empirical evaluation | [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) | Compares systems, tools, or models on a standard set of test subjects with an automated, repeatable procedure; also covers how to check whether the benchmark itself is valid | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Building and improving](../05_research-strategies/build_improve.md), [Measurement](../05_research-strategies/measure.md) | Computer science practice |
| dataset paper, benchmark paper, resource paper, data descriptor | [Building a dataset or benchmark](dataset_paper.md) | Makes a new dataset or benchmark the result: explaining why it is needed, collecting, annotating, and splitting the data, writing a datasheet, handling licensing and ethics, releasing and maintaining it | [Measurement](../05_research-strategies/measure.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md) | Method page (computer science) |
| empirical study with large language models (LLMs), LLM-based empirical study, LLM evaluation, LLM as annotator or simulated participant, LLM-as-annotator, LLM-as-judge | [Empirical studies with large language models](llm_study.md) | Evaluates large language models, or uses them as annotators, judges, or simulated participants: recording model versions and prompts, checking for contamination and run-to-run variation, validating against human judgments | [Measurement](../05_research-strategies/measure.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Building and improving](../05_research-strategies/build_improve.md) | Method page (computer science) |
| optimization study, search-based study, search-based software engineering | [Optimization studies](../07_fields/computer-science/practices/optimization_study.md) | Models the problem as "find the best among many candidate solutions" and solves it with a search algorithm | [Building and improving](../05_research-strategies/build_improve.md), [Comparative evaluation](../05_research-strategies/compare_evaluate.md) | Computer science practice |
| design-based research, design experiment | [Design-based research](../07_fields/education/practices/design_based_research.md) | Designs, tries out, and improves a teaching intervention in real classrooms over several rounds, while distilling design principles | [Building and improving](../05_research-strategies/build_improve.md) | Education practice |
| practice-based research, practice-led research, research through creative practice, artistic research | [Practice-based research](../07_fields/arts/practices/practice_based_research.md) | Uses the creative work itself as the basis of the knowledge contribution, together with a record of the process and a written account | [Building and improving](../05_research-strategies/build_improve.md) | Arts practice |

[Synthesis and characterization studies](synthesis_study.md) and [Quantitative simulation](simulation_study.md) also often serve Building and improving; they sit in the "In the lab and in the field" and "Using existing data or models" groups.

### Across methods

| You might call it | Go to | What it does | Strategies it usually serves | Source |
|---|---|---|---|---|
| replication study, reproduction, reproducibility study | [Replication studies](replication.md) | Redoes a published study in a planned way to test whether its conclusions hold | [Comparative evaluation](../05_research-strategies/compare_evaluate.md), [Measurement](../05_research-strategies/measure.md) | Method page (computer science) |
| mixed methods, multi-method research | [Mixed methods](mixed_methods.md) | Studies the same question with two or more methods | [Causal explanation](../05_research-strategies/explain_causality.md) | Method page (computer science) |

### Same name, different things

`[Our analysis]` Some names are common but mean different things in different fields and contexts. Work out which one you mean first:

- **survey**: if you mean a review paper, see [Review studies](review_study.md); if you mean sending out a questionnaire, see [Questionnaire surveys](questionnaire_survey.md); in archaeology, a survey is fieldwork on the ground, so see [Archaeological excavation and field survey](../07_fields/history-archaeology/practices/archaeological_excavation.md).
- **empirical study**: covers any research that draws conclusions from observation and data; it is not one specific way of working. Go back to [Research strategies](../05_research-strategies/README.md) to decide whether you need description, comparison, measurement, or causation, then use the tables above to find the page.
- **case study**: in the social sciences and software engineering, it means studying a few real cases in depth; see [Case study and ethnography](case_study.md) or [Process tracing and comparative case studies](process_tracing.md). In a tool paper, a "case study" that demonstrates the tool on a few real systems is part of the evaluation; see [Engineering research](../07_fields/computer-science/practices/engineering_research.md).
- **fieldwork**: in the social sciences, it usually means long-term ethnographic observation; see [Case study and ethnography](case_study.md). Linguistics, archaeology, and the earth sciences each have their own kind; see the "In the lab and in the field" group above.
- **experiment**: with human participants, see [Controlled experiments](controlled_experiment.md) or [Randomized controlled trials](randomized_controlled_trial.md); splitting real users of a live product, see [Online controlled experiments (A/B tests)](online_controlled_experiment.md); experiments with large language models, see [Empirical studies with large language models](llm_study.md); runs on software systems or models, see [Benchmarking](../07_fields/computer-science/practices/benchmarking.md); work at the lab bench, see [Bench experiments (wet lab)](bench_experiment.md).

## How methods and strategies divide the work

- **A research strategy** is about what knowledge the project produces and what evidence it needs; see [Research strategies](../05_research-strategies/README.md).
- **The pages in this section** are about how to do the work well: the steps, the key decisions, a checklist, and common mistakes.
- **One way of working can serve several strategies.** A controlled experiment, for example, can compare two existing tools, and it can also test "X causes Y". That is why each row in the tables above lists the strategies it usually serves.
- **What goes in `06_methods/` and what goes in a field folder**: methods used by two or more fields go in `06_methods/`; practices used by only one field go under `practices/` in that field's folder, for example [Research practices specific to computer science](../07_fields/computer-science/practices/README.md). On the website, the navigation puts the two together as this "Research types" section.

This division is a convention of this handbook `[Our analysis]`.

For how to choose a strategy and a method based on your question, see [Choosing a method](../02_do-the-project/02_choose-method.md).

## Scope of these method pages

`[Our analysis]` There are 34 method pages in `06_methods/`. Twenty-eight of them were originally written for computer science or for one other field, and moved here later because more than one field uses the method:

- **The 14 pages originally written for computer science** are aimed mainly at software engineering: most of their checklists follow the Empirical Standards of the Association for Computing Machinery's Special Interest Group on Software Engineering (ACM SIGSOFT), and most of their examples come from software engineering.
- **The 14 pages originally written for other fields** follow that field's norms and sources; for example, the randomized controlled trial page follows medicine's trial reporting guidelines, and the quasi-experiment page describes how economists do it.

The other 6 were added later: [Online controlled experiments](online_controlled_experiment.md), [Focus groups](focus_group.md), [Content analysis](content_analysis.md), [Position papers](position_paper.md), [Building a dataset or benchmark](dataset_paper.md), and [Empirical studies with large language models](llm_study.md). They were written as cross-field pages from the start, and the scope note at the top of each page says which field its sources come from.

The methods themselves are used in many fields, but the specific norms differ from field to field. Each page says at the top which field it was originally written for and where its sources come from. If you are not in the field a page was written for, read your own field's norms and practices first, and use the method page here as a reference.

The 14 field-specific practices (5 in computer science, 9 in other fields) represent only that field's way of doing things. For each field's overall conventions, see [Fields](../07_fields/README.md).
