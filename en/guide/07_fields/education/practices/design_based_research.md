# Design-based research

This page is about **design-based research**: researchers and teachers work together to design, try out, and refine a teaching intervention in real classrooms, round after round, while distilling design principles and theory that other people can use too. The [Education field overview](../README.md#research-methods-common-in-this-field) introduces it briefly; this page is about how to do it. It draws mainly on four methodological sources: a 2014 conference paper by Easterday and colleagues at the International Conference of the Learning Sciences; an introductory chapter Bakker and van Eerde wrote in 2015 for a book on research methods in mathematics education, aimed at researchers including master's and PhD students[^bakker2015introduction-e1]; a 2020 methods article by Scott and colleagues that uses one of their own biology education studies as its example; and Anderson and Shattuck's 2012 review of a decade of progress with the approach. Wherever the text below says "X recommends," that is the personal recommendation of these authors, not a rule the field has agreed on.

Not covered here: getting school approvals, working with "gatekeepers," and planning around the school calendar are in the [field overview](../README.md#most-research-happens-in-schools-get-past-the-gatekeepers-first); general ethics such as consent from minors and studying your own students are in [the ethics section of the field overview](../README.md#ethics-minors-gatekeepers-and-studying-your-own-students); action research in which a teacher improves their own classroom alone is in [the research methods section of the field overview](../README.md#research-methods-common-in-this-field) (note that it means something different from "action research" on the research methods page); randomized controlled trials meant to show that an intervention "works" are covered on the research methods page [Controlled experiments](../../../06_methods/controlled_experiment.md) and in the field overview's [standards of evidence](../README.md#standards-of-evidence-how-the-what-works-clearinghouse-rates-studies).

**Scope** `[Our analysis]`: this is a research method in education, based on the four education research methods sources listed above. For the general logic of "build something new, then show it is useful," see the research strategy [Building and improving](../../../05_research-strategies/build_improve.md). For steps shared across fields, such as choosing a topic, planning, and writing, see the chapters of each Part, for example [Converging on a project](../../../01_from-interest-to-project/03_converge.md) and [Telling the story and writing the paper](../../../04_write-and-publish/01_story-and-paper.md).

**Strategies it usually serves**: [Building and improving](../../../05_research-strategies/build_improve.md) (the "Common research methods" section of that strategy page is authoritative).

**After reading this page, you should be able to:**

- judge whether your question suits design-based research, and tell it apart from action research, controlled experiments, and plain development of teaching materials;
- form a team with a school and its teachers, starting from a real problem and a written set of design conjectures;
- plan the rounds of "design, implement, analyze, redesign," and know what data to collect in each round and how to keep a design log;
- get from your data both a better design and transferable design principles; deal with the credibility and ethics problems that come from "the researcher is also the designer"; and know what to put in your report.

---

## 1. What this kind of research is and when to use it

**It has to deliver two things at once.** Easterday and colleagues say there is general agreement that design-based research should produce both effective educational interventions and useful theory[^easterday2014design-e1]. Bakker and van Eerde put it as useful products such as educational materials on one side, and scientific insight into how those products can be used in education on the other[^bakker2015introduction-e2]. "Intervention" is meant broadly here: a learning activity, a type of assessment, an administrative measure (such as a change in holidays), or a technological tool[^anderson2012design-e12].

**Why it is needed.** Easterday and colleagues argue that the linear path of "basic research → applied research → development → products" does not work well, while design that is not guided by theory tends to be incremental and haphazard[^easterday2014design-e2]. Bakker and van Eerde point to one limitation of randomized controlled trials: a new approach has to be designed before it can be tested, and in many cases designing an innovative approach itself takes a great deal of research[^bakker2015introduction-e29].

**How it differs from related kinds of research:**

| | Design-based research | Action research | Controlled experiments, randomized controlled trials | Plain development of teaching materials |
|---|---|---|---|---|
| Who does it | Researchers and teachers as a team, together from defining the problem to publishing[^anderson2012design-e15][^scott2020design-e5] | Usually the teacher alone[^anderson2012design-e5] | The researcher decides how it is implemented and analyzed; the teacher delivers the treatments[^scott2020design-e30] | The designer |
| Can the intervention change midway? | Yes, it is modified on the spot during implementation[^scott2020design-e10] | Yes | No, it is fixed for the whole experimental period[^scott2020design-e9] | Yes |
| Does it need to produce theory? | Yes, and it aims more explicitly at instructional theory[^bakker2015introduction-e7] | Focuses on action and change[^bakker2015introduction-e7] | Tests existing theory | No; whether there is a theoretical yield is exactly what separates the two[^bakker2015introduction-e3] |
| Causal conclusions it can support | Less convincing than a randomized controlled trial[^bakker2015introduction-e6] | Weak | Strong | Not the aim |

Cells without footnotes are our own summary `[Our analysis]`. A few ways to decide:

- **You teach the course and are also the researcher.** Scott and colleagues draw the line like this: if your question is "how can I improve my own classroom," it is closer to action research; it fits design-based research only if the question can produce generalizable results with the potential to affect teaching broadly[^scott2020design-e6][^scott2020design-e7].
- **Your goal is to "prove this intervention works."** That is more the job of an efficacy or effectiveness study `[Our analysis]`. The Institute of Education Sciences (IES) of the US Department of Education and the US National Science Foundation (NSF), two funders, divide the education research they fund into several types; see the field overview's [section on the evidence pipeline](../README.md#a-single-study-often-covers-only-one-segment-of-the-evidence-pipeline). Design-based research roughly corresponds to their "design and development research" `[Our analysis]`: designing and developing an intervention iteratively, based on existing theory and evidence[^ies2013common-e4]. Under these two funders' requirements, at the end of the project you deliver a "theory of action" (a chain of causal assumptions about why the intervention should work), a set of intervention components, and **preliminary** evidence that the intervention promises to improve outcomes[^ies2013common-e10].
- **Compare with other fields** `[Our analysis]`. [Engineering research](../../computer-science/practices/engineering_research.md) on the Computer science page also "builds something and then evaluates it"; [Practice-based research](../../arts/practices/practice_based_research.md) in the arts treats the creative work itself as research. What sets design-based research apart is that it happens in real classrooms, together with teachers, and the research goes on while the design is being changed.

**Allow enough time.** With so many iterations, it is hard to know when the work is finished[^anderson2012design-e3]. Anderson and Shattuck mention that Herrington and colleagues wrote a whole article in 2007 on how to do it as a doctoral dissertation within four years[^anderson2012design-e7]; their own partial solution is for established researchers to set up multi-year agendas in which graduate students take on, and "own," significant pieces[^anderson2012design-e18]. In a master's program or a short PhD, you can do just one or two rounds and say so clearly in your proposal `[Our analysis]`.

---

## 2. How to do it

Design-based research has no accepted, uniform procedure described as precisely as an experiment's, and it looks different depending on who does it[^easterday2014design-e3]. What follows combines three accounts: the six phases of Easterday and colleagues (focus, understand, define, conceive, build, test)[^easterday2014design-e4]; Bakker and van Eerde's three-phase cycle (preparation and design, teaching experiment, retrospective analysis)[^bakker2015introduction-e9]; and the four-phase cycle of Scott and colleagues (design, test, evaluate, reflect)[^scott2020design-e31]. Scott and colleagues also caution that in practice their four phases often overlap[^scott2020design-e2].

### Step 1: Find partner schools and teachers, and agree on who does what

**How:** form a team of researchers and practicing teachers. As Anderson and Shattuck describe it, the two sides work together from defining the problem and reviewing the literature, through designing and building the intervention, implementing and assessing it, to developing and publishing design principles[^anderson2012design-e15]. When you form the team, write down who designs, who teaches, who collects data, who analyzes, how often you meet, and how far teachers can make their own adjustments in class `[Our analysis]`.

**Why:** Anderson and Shattuck say teachers are usually too busy and often lack training in rigorous research, while researchers often do not know the complexities of culture, technology, goals, and internal politics in a working school system[^anderson2012design-e14]. Scott and colleagues argue that when teachers are members of the team, they can make informed adjustments during implementation without straying from the goals of the research[^scott2020design-e29].

**Where people go wrong:** underestimating how hard collaboration is. Scott and colleagues warn that iteration requires the collaboration to last a long time, so you have to face these difficulties when you form the team and define the roles of researchers and teachers clearly[^scott2020design-e24]. For the general issues of school approvals, the school calendar, and recruitment, see the [field overview](../README.md#plan-your-timeline-backward-from-the-school-calendar).

### Step 2: Start from a real problem, and understand it first

**How** (following the first three phases of Easterday and colleagues):
1. **Focus**: bound the audience (learners, and others affected such as parents and the community), the topic, and the scope[^easterday2014design-e5]. Scott and colleagues say the learning problem usually comes from the researcher's own experience inside or outside the classroom, or from previous research in the literature[^scott2020design-e12].
2. **Understand**: study the learners, the subject matter, the specific context, and existing solutions[^easterday2014design-e6]. Designing an intervention starts with an accurate assessment of the local context, informed by the relevant literature and practice elsewhere[^anderson2012design-e11].
3. **Define goals**: set the goals and how you will assess them[^easterday2014design-e7]. Only once the goal is defined can a design be said to succeed or fail[^easterday2014design-e8].

**Why:** following a principle set out by Sandoval, Scott and colleagues require that the problem you choose must advance some theory of learning[^scott2020design-e13]. Whether there is a theoretical yield is exactly what distinguishes it from plain development of teaching materials[^bakker2015introduction-e3].

**Where people go wrong:** writing only "increase students' interest in learning statistics" without defining what counts as success; or picking a problem that matters only to your own school and class, so you cannot say which theory it advances `[Our analysis]`. For how to turn a topic into answerable questions, see the Part 2 chapter section [Break the claim into research questions](../../../02_from-project-to-study/01_question-to-evidence.md#1-break-the-claim-into-research-questions).

### Step 3: Before you build anything, write down the conjectures behind the design

**How:** Easterday and colleagues recommend not rushing to build the finished product: sketch the solution and break it down, analyzing what components it has and how they might work together[^easterday2014design-e9]. Three other practices:

- **Map your design conjectures** (as described by Scott and colleagues following Sandoval 2014; we have not read Sandoval's original): specify the theoretically salient features of the design and map out how they are predicted to work together to produce the desired outcomes[^scott2020design-e26]. That way, before you start, you make explicit how your theory of learning is embodied in the tools, what data the tools will produce for analysis, and what outcomes will count as evidence of success[^scott2020design-e27].
- **Write a hypothetical learning trajectory** (used by Bakker and van Eerde in mathematics education): write down the learning goals, the students' starting points and prior knowledge, the tasks you will use, and your assumptions about how students might learn and how the teacher could support that learning[^bakker2015introduction-e12].
- **Gather a pool of candidate tasks first**: Bakker and van Eerde recommend that in the first design phase you collect and invent a set of tasks that could be useful, and discuss them with colleagues who have design experience[^bakker2015introduction-e15].

**Why:** Scott and colleagues argue that alignment among theory, instructional tools, and the way students are assessed is central to rigor in this kind of research[^scott2020design-e14]. Predictions written down in advance are also the yardstick you compare against what actually happened during retrospective analysis[^bakker2015introduction-e18].

**Where people go wrong:** having only a lesson plan, with nothing written about "why this design should make students learn in this way." At analysis time you can then say only "the students learned it," not which feature of the design made the difference `[Our analysis]`.

### Step 4: Work in rounds, rough first and refined later

**How:** each round consists of design, implementation in the classroom, analysis, and redesign[^bakker2015introduction-e9]. Easterday and colleagues recommend low-fidelity prototypes early on, collecting only the minimum data needed to quickly reject failures and identify promising candidates[^easterday2014design-e14]; once you have a promising prototype, use qualitative methods to work out the mechanism through which it affects learning[^easterday2014design-e20]. A prototype can be lower or higher fidelity, depending on the stage of the project and the question you want to test[^easterday2014design-e10]. One principle that Scott and colleagues relay is to run extended, iterative teaching experiments in classrooms[^scott2020design-e4]. You can make changes during implementation: the teacher or researcher may feel the need to adjust the activity for the next lesson[^bakker2015introduction-e28], and the design team can adjust the tools while they are in use to deal with unanticipated conditions[^scott2020design-e15].

**Why:** don't build the whole intervention only to discover at the end that it does not work; build prototypes quickly, test them, and redesign, so the intervention evolves gradually[^easterday2014design-e12]. Running one round after another also lets you test the conjectures from an earlier round in a later one[^bakker2015introduction-e21].

**Where people go wrong:** Easterday and colleagues warn of two opposite errors: running randomized controlled experiments from the start is likely to waste resources testing a bad design; on the other hand, staying in theory building and new designs forever means you are unlikely to produce strong evidence that anything works[^easterday2014design-e15][^easterday2014design-e16]. They say that thinking about the test phase while planning helped them avoid both errors[^easterday2014design-e18].

### Step 5: What data to collect in each round, and how to keep a design log

**How:**
- **Data on student learning.** Bakker and van Eerde say a teaching experiment typically collects student work, tests before and after instruction, field notes, audio recordings of whole-class discussions, video of every lesson, and video of the final interviews with students and teachers[^bakker2015introduction-e16]; they also find "mini-interviews" with students during class, lasting from about 20 seconds to 4 minutes, very useful, provided they are carried out systematically[^bakker2015introduction-e17]. Scott and colleagues add homework, lab reports, attitude surveys, participation rates in activities, interviews, classroom discourse, and exam data[^scott2020design-e16].
- **Data on implementation.** Scott and colleagues stress that you should collect how the tools were actually implemented, which parts of implementation did not go as planned, and how the tools or the implementation process were modified[^scott2020design-e8].
- **Choose your data in advance.** There are too many possible data streams, and they are costly to collect, so decide in advance which data and which analysis methods will answer your theoretical and practical questions[^scott2020design-e25]. Uncovering learning mechanisms means collecting multiple data streams over a long time, which often takes substantial time and money[^scott2020design-e28].

**Design log**: Bakker and van Eerde say that every change made along the way is itself data and needs to be reported well, and the case is stronger when a change is supported by theory[^bakker2015introduction-e13]. As Anderson and Shattuck describe it, the researcher documents the time, commitment, and contingencies involved in designing and implementing the intervention, so readers can judge whether they could do it in their own setting[^anderson2012design-e13]. We suggest writing one entry on the day of each lesson, with at least: the date and class; what was planned; what actually happened (especially where it differed from what you expected); what you changed, why, and which theory or data it was based on; and who made the decision `[Our analysis]`.

**Why:** a real example: when Scott and colleagues reviewed their notes on the spring 2017 implementation, they found that the pretest had been due at the end of the first day of class, after students had already been exposed to the relevant content, which may be one reason pretest scores were unusually high[^scott2020design-e19]; so they decided to close the pretest before the first day of class in the next round[^scott2020design-e20]. Without those notes, they could not have explained the anomaly `[Our analysis]`. For how to manage the log alongside your other research materials, see [Organizing research materials](../../../08_throughout/organizing_materials.md#5-keep-three-kinds-of-notes-apart) in Throughout the project.

**Where people go wrong:** collecting only pre- and posttests and losing the process data, so in the end you can say only "scores went up," not how; or recording everything, with no one having time to analyze it `[Our analysis]`.

### Step 6: Retrospective analysis: improve the design, and distill design principles

**How:**
1. **Compare what you expected with what happened.** Bakker and van Eerde use a matrix: the left side holds the hypothetical learning trajectory (how you expected students to respond to each task), and the right side holds transcript excerpts, the researcher's notes, and how well the expected and observed learning matched[^bakker2015introduction-e18].
2. **Generate and test conjectures.** Guided by your research questions, generate conjectures about students' learning and write them down, then test them against other episodes and data, looking for both confirmation and counterexamples[^bakker2015introduction-e19].
3. **Answer three questions** (posed by Scott and colleagues): How was the theory advanced? Did the instructional tools support student learning? Which critical features of the design made it work (that is, the design principles)[^scott2020design-e18]?
4. **Write the design principles so others can use them.** Scott and colleagues say design principles describe features of learning environments that others can use to develop tools suited to their own context[^scott2020design-e21], and they need to balance specificity with adaptability[^scott2020design-e22]. Bakker and van Eerde say they can also take a predictive form: "under conditions X, using approach Y, students are likely to learn Z"[^bakker2015introduction-e4]. One of the principles Scott and colleagues reached in their first round was that instructional tools should explicitly state the principle of interest, with specific guidance on how it is applied in context[^scott2020design-e23].

**Why:** as relayed by Scott and colleagues, Sandoval says design research is aimed not at finding "effects" but at finding "functions": understanding how effects arise in a designed environment[^scott2020design-e11]. The goal is not "the perfect instructional sequence" (which Bakker and van Eerde believe does not exist) but empirically grounded results that others can adjust to their local circumstances[^bakker2015introduction-e14].

**Where people go wrong:** writing design principles as slogans that supposedly hold everywhere. Anderson and Shattuck say design principles are not decontextualized grand theories; they reflect the conditions in which they operate[^anderson2012design-e16], so write those conditions in `[Our analysis]`.

### Step 7: Protect credibility when you are both designer and researcher

Anderson and Shattuck cite one criticism: when a researcher is involved throughout the conceptualization, design, development, implementation, and study of a teaching approach, making credible claims is a challenge[^anderson2012design-e6]. They say good research demands skepticism and detachment, while this kind of research also requires comradeship with partners and active support for the intervention[^anderson2012design-e17]. Bakker and van Eerde offer these practices:
- **Look for counterexamples and test across rounds**: test your conjectures against other data and look specifically for counterexamples[^bakker2015introduction-e19]; use later rounds to test conjectures from earlier ones[^bakker2015introduction-e21].
- **Ask colleagues to challenge your interpretation**: discuss key episodes with colleagues to see whether they agree or can think of alternative interpretations[^bakker2015introduction-e20].
- **Depend less on yourself**: collect data with objective devices such as audio and video recording[^bakker2015introduction-e24]; when several people code, report not only percentage agreement but also Cohen's kappa or another measure that accounts for chance agreement[^bakker2015introduction-e25].
- **Say how far your results generalize**: the theories it produces are usually tied to specific learning environments and are hard to generalize[^bakker2015introduction-e8]. Many research approaches (mainly qualitative ones) aim to generalize to a theory, model, or concept, rather than from a random sample to a population[^bakker2015introduction-e5]; the theory also has to be usable in classrooms elsewhere, which is called "transferability"[^bakker2015introduction-e10]. For how to argue for generalization, see [Case study](../../../06_methods/case_study.md#step-8-generalize-analytically-not-statistically) on the research methods page.

In addition, the IES and NSF guidelines in the US require the design and development projects they fund to have their theoretical framework, data collection, analysis, and reporting go through a series of external critical reviews[^ies2013common-e14]. Projects not funded by these two can borrow the idea, for example by having people outside the research group review the work regularly `[Our analysis]`. For validity in general, see the Part 2 chapter [Validity and limitations](../../../02_from-project-to-study/03_validity-and-limits.md). Anderson and Shattuck say this kind of research usually uses mixed methods[^anderson2012design-e10]; for how to integrate several kinds of data, see [Mixed methods](../../../06_methods/mixed_methods.md) on the research methods page.

> **Where sources disagree: should design-based research run randomized controlled trials and draw causal conclusions?**
> - **Anderson and Shattuck**: the studies they reviewed generally had no control groups, in line with the approach's philosophy[^anderson2012design-e8]; most studies do not produce effect sizes that demonstrate "what works"[^anderson2012design-e9].
> - **Bakker and van Eerde**: it cannot claim causality with the same convincing rigor as a randomized controlled trial[^bakker2015introduction-e6]; its products are judged on innovativeness and usefulness, not just on the rigor of the process[^bakker2015introduction-e27].
> - **Easterday and colleagues**: a randomized controlled test can be nested within the test phase as part of design-based research[^easterday2014design-e13]; once you have a well-grounded theory and an implementation with some evidence of success, you can verify its efficacy with randomized controlled experiments[^easterday2014design-e15]; if you never take that step, you are unlikely to produce strong evidence that it works[^easterday2014design-e16].
>
> **Our suggestion** `[Our analysis]`: in the early rounds, write about "how it works," not "proof that it works"; when your conclusions say something "improved" or "was effective," label it as preliminary evidence. If late in the project you really do need to answer "does it work," design that part separately to the standards of a controlled experiment or randomized controlled trial.

### Step 8: Ethics: the designer and the researcher are the same person

For general ethics, see [the ethics section of the field overview](../README.md#ethics-minors-gatekeepers-and-studying-your-own-students), which already introduces the ethical guidelines of the British Educational Research Association (BERA). Below are only the points from those guidelines that are especially relevant to this kind of research; in other countries, follow local rules and your institution's ethics review requirements `[Our analysis]`:
- **You may be the students' teacher.** BERA asks you to consider the power relationships created by the dual role of "teacher-researcher"[^bera2024ethical-e10] and to reassure students as far as possible that not taking part is completely fine[^bera2024ethical-e12]; ways to do this include being transparent about your role as a researcher and bringing an independent third party into the research process[^bera2024ethical-e11].
- **You want the intervention to succeed.** You want to show that your design is good, yet you have to report the real results. BERA requires you to report all results of interventions and evaluations, including negative ones[^bera2024ethical-e16]. Designs that failed and conjectures that were overturned are exactly the data of iterative research `[Our analysis]`.
- **Partner teachers' workload and authorship.** BERA asks you to consider the burden the research places on participants' lives and workloads[^bera2024ethical-e23]; in research done jointly by academics and teachers, everyone who made a substantial contribution should be listed as a co-author[^bera2024ethical-e18]. BERA gives the example that a group of teachers doing action research should inform the school's leadership[^bera2024ethical-e24]; collaborative design research should likewise keep school leaders informed `[Our analysis]`.
- **Build room for change into your ethics application.** The design will change from round to round, so say in your application that "activities and materials will be adjusted within a defined scope," and file an amendment when a change goes beyond that scope `[Our analysis]`.

### Step 9: Reporting: what you need to make clear

Bakker and van Eerde say reports of design-based research require "thick description," so they tend to be long[^bakker2015introduction-e22]. Our sources contain no reporting guideline written specifically for design-based research; the points below combine three sources: the reporting standards the American Educational Research Association (AERA) set for its publications (see the [field overview](../README.md#reporting-standards-aeras-standards-for-reporting-empirical-research)), the deliverables IES and NSF in the US require of the design and development projects they fund, and methodologists' recommendations. For general advice on writing the paper, see the Part 4 chapter [Telling the story and writing the paper](../../../04_write-and-publish/01_story-and-paper.md).

- **Tell the whole process**, so readers can reconstruct the study: failures and successes, the procedures followed, the conceptual framework, and the reasons for your choices[^bakker2015introduction-e26]. Easterday and colleagues found that organizing the account by phases communicates more concisely what a project has done[^easterday2014design-e19].
- **The main design iterations, the evidence from each round, and the changes to the theory of action and the design that followed** (an IES and NSF requirement)[^ies2013common-e11].
- **The intervention itself**: AERA's standards require it to be described in enough detail for others to identify its key features[^aera2006standards-e6]; IES and NSF also require you to deliver all the materials needed to implement it[^ies2013common-e11].
- **Your role** (AERA's standards): how you got into the field, what role you played as a researcher, and whether the relationships changed over time[^aera2006standards-e5]; the relationship between researcher and participants affects the data you collect[^aera2006standards-e16].
- **Evidence and counterexamples** (the items in AERA's standards for qualitative research): give evidence for each claim and report important counterexamples[^aera2006standards-e11]; clearly mark speculation that goes beyond the evidence[^aera2006standards-e12]; if you want to generalize, say to what[^aera2006standards-e13].
- **Implementation and preliminary results** (an IES and NSF requirement): data on implementation in a real setting, and pilot data showing the intervention's promise for producing the intended outcomes[^ies2013common-e12].

---

## 3. Checklist

**Must do**
- [ ] The problem comes from a real educational setting and can advance a theory of learning[^scott2020design-e13]; you have written down the goals and what counts as success[^easterday2014design-e8]
- [ ] Before building anything, you wrote down your design conjectures: how the theory is embodied in the tools, what data they will produce, and what outcomes count as success[^scott2020design-e27]
- [ ] Implemented in real classrooms[^scott2020design-e4], with data collected on the implementation process[^scott2020design-e8]
- [ ] Every change is recorded with what changed and why, and accounted for in the report[^bakker2015introduction-e13]
- [ ] You looked for counterexamples during analysis[^bakker2015introduction-e19], and produced design principles that state the conditions under which they apply[^scott2020design-e21][^anderson2012design-e16]
- [ ] The report states the researcher's role and relationship with participants[^aera2006standards-e5]
- [ ] You dealt with the dual role of teacher-researcher[^bera2024ethical-e10]; negative results are reported too[^bera2024ethical-e16]

**Better practice**
- [ ] Use several rounds of implementation to test conjectures from earlier rounds[^bakker2015introduction-e21]
- [ ] Have colleagues do peer examination of key episodes[^bakker2015introduction-e20]; when several people code, report an agreement measure that accounts for chance agreement[^bakker2015introduction-e25]
- [ ] Go through external critical review (an IES and NSF requirement for the projects they fund)[^ies2013common-e14]
- [ ] Record the time, commitment, and contingencies the intervention required, so readers can judge whether it is feasible where they are[^anderson2012design-e13]

**Fine to skip; not a flaw**
- No control group and no effect sizes: this was generally the case in the studies Anderson and Shattuck reviewed, and they consider it in line with the approach's philosophy[^anderson2012design-e8][^anderson2012design-e9]; Easterday and colleagues also warn that running randomized controlled experiments too early may waste resources[^easterday2014design-e15]. But in that case, do not claim to have "proved it works" `[Our analysis]`.

**Reviewer criticisms you may meet that don't hold up** (our sources do not say how common these criticisms are `[Our analysis]`)

- "You changed the intervention midway, so the experiment is invalid." In comparative experiments this is indeed generally not accepted, but in design-based research the changes are part of the data, provided they are reported clearly and ideally supported by theory[^bakker2015introduction-e13].
- "The sample wasn't random, so you can't generalize." This kind of research aims for generalization to theory and transferability, not statistical generalization[^bakker2015introduction-e5][^bakker2015introduction-e10]. If the authors themselves claimed statistical generalization, the criticism does hold `[Our analysis]`.

---

## 4. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Delivering only a set of teaching materials, with no theory or design principles | Whether there is a theoretical yield is exactly what separates it from plain development work[^bakker2015introduction-e3] |
| Starting to teach without writing down design conjectures | Theory, tools, and assessment don't line up, so rigor is out of reach[^scott2020design-e14] |
| Running a large randomized controlled trial in the first round | Likely to waste resources testing a bad design[^easterday2014design-e15] |
| Iterating endlessly and never wrapping up | It is hard enough to know when the work is done[^anderson2012design-e3]; decide the number of rounds and each round's goal in advance `[Our analysis]` |
| Changing the design without recording it | The changes themselves are data and must be reported[^bakker2015introduction-e13]; you also won't be able to explain anomalous results afterward[^scott2020design-e19] |
| Recording everything without an analysis plan decided in advance | Data are plentiful and costly, so you must decide in advance which data answer which questions[^scott2020design-e25] |
| Writing design principles as slogans detached from context | Design principles should reflect the conditions in which they operate[^anderson2012design-e16] |
| The researcher reports only the episodes that support their design | Credibility is already the hard part of this kind of research[^anderson2012design-e6]; look for counterexamples[^bakker2015introduction-e19] and report negative results[^bera2024ethical-e16] |
| Writing preliminary evidence up as "proved effective" | It cannot claim causality with the rigor of a randomized controlled trial[^bakker2015introduction-e6] |
| Treating partner teachers as mere implementers and leaving them off the author list | Under BERA's guidelines in the UK, teachers who made a substantial contribution should be listed as co-authors[^bera2024ethical-e18] |

---

## 5. Further reading

- **Bakker & van Eerde 2015**: a chapter in a book on research methods in mathematics education, written for researchers including master's and PhD students. It covers hypothetical learning trajectories, data collection, the analysis matrix, and validity and reliability, with examples from statistics education. If you are new, start with this one.
- **Scott, Wenderoth & Doherty 2020**: a methods article in *CBE—Life Sciences Education* that walks through one full "design, test, evaluate, reflect" cycle using the authors' own biology education study, and discusses the difficulties of collaboration, resources, and rigor. Open access.
- **Easterday, Rees Lewis & Gerber 2014**: a conference paper from the International Conference of the Learning Sciences that proposes a six-phase process and the idea of "which methods to use at which phase"; useful for planning a project and writing grant applications.
- **Anderson & Shattuck 2012**: published in *Educational Researcher*; covers the characteristics and difficulties of design-based research and reviews a decade of studies.
- **IES & NSF 2013, *Common Guidelines for Education Research and Development***: what these two US funders require in plans and deliverables for the "design and development research" projects they fund; usable as a reporting checklist.
- Not read in the original for this page: Sandoval 2014 (relayed in many places by Scott and colleagues; the approach to writing conjectures comes from it).

[^bakker2015introduction-e1]: Bakker & van Eerde 2015, §16.1.1, p. 429. [Evidence](../../../../sources/notes/bakker2015introduction.md#e1)
[^easterday2014design-e1]: Easterday et al. 2014, Introduction, p. 317. [Evidence](../../../../sources/notes/easterday2014design.md#e1)
[^bakker2015introduction-e2]: Bakker & van Eerde 2015, §16.1.1, p. 430. [Evidence](../../../../sources/notes/bakker2015introduction.md#e2)
[^anderson2012design-e12]: Anderson & Shattuck 2012, What is DBR? [Evidence](../../../../sources/notes/anderson2012design.md#e12)
[^easterday2014design-e2]: Easterday et al. 2014, Introduction, p. 317. [Evidence](../../../../sources/notes/easterday2014design.md#e2)
[^bakker2015introduction-e29]: Bakker & van Eerde 2015, §16.1.2.5, p. 434. [Evidence](../../../../sources/notes/bakker2015introduction.md#e29)
[^anderson2012design-e15]: Anderson & Shattuck 2012, collaborative partnership. [Evidence](../../../../sources/notes/anderson2012design.md#e15)
[^scott2020design-e5]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e5)
[^anderson2012design-e5]: Anderson & Shattuck 2012, Comparison to Action Research. [Evidence](../../../../sources/notes/anderson2012design.md#e5)
[^scott2020design-e30]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e30)
[^scott2020design-e10]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e10)
[^scott2020design-e9]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e9)
[^bakker2015introduction-e7]: Bakker & van Eerde 2015, §16.1.2.6, p. 435. [Evidence](../../../../sources/notes/bakker2015introduction.md#e7)
[^bakker2015introduction-e3]: Bakker & van Eerde 2015, §16.1.2.1, p. 430. [Evidence](../../../../sources/notes/bakker2015introduction.md#e3)
[^bakker2015introduction-e6]: Bakker & van Eerde 2015, §16.1.2.5, p. 434. [Evidence](../../../../sources/notes/bakker2015introduction.md#e6)
[^scott2020design-e6]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e6)
[^scott2020design-e7]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e7)
[^ies2013common-e4]: IES & NSF 2013, Types of Research. [Evidence](../../../../sources/notes/ies2013common.md#e4)
[^ies2013common-e10]: IES & NSF 2013, Introduction. [Evidence](../../../../sources/notes/ies2013common.md#e10)
[^anderson2012design-e3]: Anderson & Shattuck 2012, Involving multiple iterations. [Evidence](../../../../sources/notes/anderson2012design.md#e3)
[^anderson2012design-e7]: Anderson & Shattuck 2012, Problems with DBR. [Evidence](../../../../sources/notes/anderson2012design.md#e7)
[^anderson2012design-e18]: Anderson & Shattuck 2012, Problems with DBR. [Evidence](../../../../sources/notes/anderson2012design.md#e18)
[^easterday2014design-e3]: Easterday et al. 2014, Problem 1, p. 317. [Evidence](../../../../sources/notes/easterday2014design.md#e3)
[^easterday2014design-e4]: Easterday et al. 2014, Design Process, p. 319. [Evidence](../../../../sources/notes/easterday2014design.md#e4)
[^bakker2015introduction-e9]: Bakker & van Eerde 2015, §16.1.2.9, p. 438. [Evidence](../../../../sources/notes/bakker2015introduction.md#e9)
[^scott2020design-e31]: Scott et al. 2020, What Is Design-Based Research? [Evidence](../../../../sources/notes/scott2020design.md#e31)
[^scott2020design-e2]: Scott et al. 2020, What Is Design-Based Research? [Evidence](../../../../sources/notes/scott2020design.md#e2)
[^anderson2012design-e14]: Anderson & Shattuck 2012, collaborative partnership. [Evidence](../../../../sources/notes/anderson2012design.md#e14)
[^scott2020design-e29]: Scott et al. 2020, Design-Based Research Fosters Collaborations across Disciplines. [Evidence](../../../../sources/notes/scott2020design.md#e29)
[^scott2020design-e24]: Scott et al. 2020, Collaborations Can Be Difficult to Maintain. [Evidence](../../../../sources/notes/scott2020design.md#e24)
[^easterday2014design-e5]: Easterday et al. 2014, Focus, p. 319. [Evidence](../../../../sources/notes/easterday2014design.md#e5)
[^scott2020design-e12]: Scott et al. 2020, Identifying the Learning Problem. [Evidence](../../../../sources/notes/scott2020design.md#e12)
[^easterday2014design-e6]: Easterday et al. 2014, Understand, p. 319. [Evidence](../../../../sources/notes/easterday2014design.md#e6)
[^anderson2012design-e11]: Anderson & Shattuck 2012, What is DBR? [Evidence](../../../../sources/notes/anderson2012design.md#e11)
[^easterday2014design-e7]: Easterday et al. 2014, Define, p. 320. [Evidence](../../../../sources/notes/easterday2014design.md#e7)
[^easterday2014design-e8]: Easterday et al. 2014, Define, p. 320. [Evidence](../../../../sources/notes/easterday2014design.md#e8)
[^scott2020design-e13]: Scott et al. 2020, Identifying the Learning Problem. [Evidence](../../../../sources/notes/scott2020design.md#e13)
[^easterday2014design-e9]: Easterday et al. 2014, Conceive, p. 320. [Evidence](../../../../sources/notes/easterday2014design.md#e9)
[^scott2020design-e26]: Scott et al. 2020, Concerns with Experimental Rigor (citing Sandoval 2014). [Evidence](../../../../sources/notes/scott2020design.md#e26)
[^scott2020design-e27]: Scott et al. 2020, Concerns with Experimental Rigor. [Evidence](../../../../sources/notes/scott2020design.md#e27)
[^bakker2015introduction-e12]: Bakker & van Eerde 2015, §16.1.3.1, p. 439. [Evidence](../../../../sources/notes/bakker2015introduction.md#e12)
[^bakker2015introduction-e15]: Bakker & van Eerde 2015, §16.1.4.1, p. 441. [Evidence](../../../../sources/notes/bakker2015introduction.md#e15)
[^scott2020design-e14]: Scott et al. 2020, Cycle 1, Phase 1. [Evidence](../../../../sources/notes/scott2020design.md#e14)
[^bakker2015introduction-e18]: Bakker & van Eerde 2015, §16.1.4.3, p. 442. [Evidence](../../../../sources/notes/bakker2015introduction.md#e18)
[^easterday2014design-e14]: Easterday et al. 2014, Stage Dependent Search, p. 322. [Evidence](../../../../sources/notes/easterday2014design.md#e14)
[^easterday2014design-e20]: Easterday et al. 2014, Stage Dependent Search, p. 322. [Evidence](../../../../sources/notes/easterday2014design.md#e20)
[^easterday2014design-e10]: Easterday et al. 2014, Build, p. 320. [Evidence](../../../../sources/notes/easterday2014design.md#e10)
[^scott2020design-e4]: Scott et al. 2020, What Is Design-Based Research? [Evidence](../../../../sources/notes/scott2020design.md#e4)
[^bakker2015introduction-e28]: Bakker & van Eerde 2015, §16.1.3.2, p. 439. [Evidence](../../../../sources/notes/bakker2015introduction.md#e28)
[^scott2020design-e15]: Scott et al. 2020, Phase 2. [Evidence](../../../../sources/notes/scott2020design.md#e15)
[^easterday2014design-e12]: Easterday et al. 2014, Iteration, p. 321. [Evidence](../../../../sources/notes/easterday2014design.md#e12)
[^bakker2015introduction-e21]: Bakker & van Eerde 2015, §16.1.5.1, p. 444. [Evidence](../../../../sources/notes/bakker2015introduction.md#e21)
[^easterday2014design-e15]: Easterday et al. 2014, Stage Dependent Search, p. 322. [Evidence](../../../../sources/notes/easterday2014design.md#e15)
[^easterday2014design-e16]: Easterday et al. 2014, Stage Dependent Search, p. 322. [Evidence](../../../../sources/notes/easterday2014design.md#e16)
[^easterday2014design-e18]: Easterday et al. 2014, Better Design, p. 322. [Evidence](../../../../sources/notes/easterday2014design.md#e18)
[^bakker2015introduction-e16]: Bakker & van Eerde 2015, §16.1.4.2, p. 442. [Evidence](../../../../sources/notes/bakker2015introduction.md#e16)
[^bakker2015introduction-e17]: Bakker & van Eerde 2015, §16.1.4.2, p. 442. [Evidence](../../../../sources/notes/bakker2015introduction.md#e17)
[^scott2020design-e16]: Scott et al. 2020, Phase 3. [Evidence](../../../../sources/notes/scott2020design.md#e16)
[^scott2020design-e8]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? [Evidence](../../../../sources/notes/scott2020design.md#e8)
[^scott2020design-e25]: Scott et al. 2020, Design-Based Research Experiments Are Resource Intensive. [Evidence](../../../../sources/notes/scott2020design.md#e25)
[^scott2020design-e28]: Scott et al. 2020, Design-Based Research Experiments Are Resource Intensive. [Evidence](../../../../sources/notes/scott2020design.md#e28)
[^bakker2015introduction-e13]: Bakker & van Eerde 2015, §16.1.3.2, p. 440. [Evidence](../../../../sources/notes/bakker2015introduction.md#e13)
[^anderson2012design-e13]: Anderson & Shattuck 2012, What is DBR? [Evidence](../../../../sources/notes/anderson2012design.md#e13)
[^scott2020design-e19]: Scott et al. 2020, Practical Outcome. [Evidence](../../../../sources/notes/scott2020design.md#e19)
[^scott2020design-e20]: Scott et al. 2020, Practical Outcome. [Evidence](../../../../sources/notes/scott2020design.md#e20)
[^bakker2015introduction-e19]: Bakker & van Eerde 2015, §16.1.4.3, p. 443. [Evidence](../../../../sources/notes/bakker2015introduction.md#e19)
[^scott2020design-e18]: Scott et al. 2020, Phase 4. [Evidence](../../../../sources/notes/scott2020design.md#e18)
[^scott2020design-e21]: Scott et al. 2020, Design Principles. [Evidence](../../../../sources/notes/scott2020design.md#e21)
[^scott2020design-e22]: Scott et al. 2020, Design Principles. [Evidence](../../../../sources/notes/scott2020design.md#e22)
[^bakker2015introduction-e4]: Bakker & van Eerde 2015, §16.1.2.2, p. 431. [Evidence](../../../../sources/notes/bakker2015introduction.md#e4)
[^scott2020design-e23]: Scott et al. 2020, Design Principles. [Evidence](../../../../sources/notes/scott2020design.md#e23)
[^scott2020design-e11]: Scott et al. 2020, How Is Design-Based Research Different from an Experimental Approach? (citing Sandoval 2014). [Evidence](../../../../sources/notes/scott2020design.md#e11)
[^bakker2015introduction-e14]: Bakker & van Eerde 2015, §16.1.3.3, p. 440. [Evidence](../../../../sources/notes/bakker2015introduction.md#e14)
[^anderson2012design-e16]: Anderson & Shattuck 2012, Evolution of design-principles. [Evidence](../../../../sources/notes/anderson2012design.md#e16)
[^anderson2012design-e6]: Anderson & Shattuck 2012, Problems with DBR. [Evidence](../../../../sources/notes/anderson2012design.md#e6)
[^anderson2012design-e17]: Anderson & Shattuck 2012, Problems with DBR. [Evidence](../../../../sources/notes/anderson2012design.md#e17)
[^bakker2015introduction-e20]: Bakker & van Eerde 2015, §16.1.4.3, p. 443. [Evidence](../../../../sources/notes/bakker2015introduction.md#e20)
[^bakker2015introduction-e24]: Bakker & van Eerde 2015, §16.1.5.3, p. 445. [Evidence](../../../../sources/notes/bakker2015introduction.md#e24)
[^bakker2015introduction-e25]: Bakker & van Eerde 2015, §16.1.5.3, p. 445. [Evidence](../../../../sources/notes/bakker2015introduction.md#e25)
[^bakker2015introduction-e8]: Bakker & van Eerde 2015, §16.1.2.8, p. 437. [Evidence](../../../../sources/notes/bakker2015introduction.md#e8)
[^bakker2015introduction-e5]: Bakker & van Eerde 2015, §16.1.2.5, p. 434. [Evidence](../../../../sources/notes/bakker2015introduction.md#e5)
[^bakker2015introduction-e10]: Bakker & van Eerde 2015, §16.1.2.9, p. 438. [Evidence](../../../../sources/notes/bakker2015introduction.md#e10)
[^ies2013common-e14]: IES & NSF 2013, Appendix, External Feedback Plan. [Evidence](../../../../sources/notes/ies2013common.md#e14)
[^anderson2012design-e10]: Anderson & Shattuck 2012, Use of mixed methods. [Evidence](../../../../sources/notes/anderson2012design.md#e10)
[^anderson2012design-e8]: Anderson & Shattuck 2012, Results. [Evidence](../../../../sources/notes/anderson2012design.md#e8)
[^anderson2012design-e9]: Anderson & Shattuck 2012, Results. [Evidence](../../../../sources/notes/anderson2012design.md#e9)
[^bakker2015introduction-e27]: Bakker & van Eerde 2015, §16.1.2.3, p. 432. [Evidence](../../../../sources/notes/bakker2015introduction.md#e27)
[^easterday2014design-e13]: Easterday et al. 2014, Recursively Nested Research Processes, p. 322. [Evidence](../../../../sources/notes/easterday2014design.md#e13)
[^bera2024ethical-e10]: BERA 2024, para. 19. [Evidence](../../../../sources/notes/bera2024ethical.md#e10)
[^bera2024ethical-e12]: BERA 2024, para. 20. [Evidence](../../../../sources/notes/bera2024ethical.md#e12)
[^bera2024ethical-e11]: BERA 2024, para. 19. [Evidence](../../../../sources/notes/bera2024ethical.md#e11)
[^bera2024ethical-e16]: BERA 2024, para. 69. [Evidence](../../../../sources/notes/bera2024ethical.md#e16)
[^bera2024ethical-e23]: BERA 2024, para. 37. [Evidence](../../../../sources/notes/bera2024ethical.md#e23)
[^bera2024ethical-e18]: BERA 2024, para. 76. [Evidence](../../../../sources/notes/bera2024ethical.md#e18)
[^bera2024ethical-e24]: BERA 2024, para. 52. [Evidence](../../../../sources/notes/bera2024ethical.md#e24)
[^bakker2015introduction-e22]: Bakker & van Eerde 2015, §16.1.5.1, p. 444. [Evidence](../../../../sources/notes/bakker2015introduction.md#e22)
[^bakker2015introduction-e26]: Bakker & van Eerde 2015, §16.1.5.4, p. 445. [Evidence](../../../../sources/notes/bakker2015introduction.md#e26)
[^easterday2014design-e19]: Easterday et al. 2014, Communicating Research Process, p. 323. [Evidence](../../../../sources/notes/easterday2014design.md#e19)
[^ies2013common-e11]: IES & NSF 2013, Table 4, Design and Development Research. [Evidence](../../../../sources/notes/ies2013common.md#e11)
[^aera2006standards-e6]: AERA 2006, 3.1.d. [Evidence](../../../../sources/notes/aera2006standards.md#e6)
[^aera2006standards-e5]: AERA 2006, 3.1.b. [Evidence](../../../../sources/notes/aera2006standards.md#e5)
[^aera2006standards-e16]: AERA 2006, 3. Sources of Evidence. [Evidence](../../../../sources/notes/aera2006standards.md#e16)
[^aera2006standards-e11]: AERA 2006, 5.12. [Evidence](../../../../sources/notes/aera2006standards.md#e11)
[^aera2006standards-e12]: AERA 2006, 5.12. [Evidence](../../../../sources/notes/aera2006standards.md#e12)
[^aera2006standards-e13]: AERA 2006, 6.2. [Evidence](../../../../sources/notes/aera2006standards.md#e13)
[^ies2013common-e12]: IES & NSF 2013, Table 4, Design and Development Research. [Evidence](../../../../sources/notes/ies2013common.md#e12)
