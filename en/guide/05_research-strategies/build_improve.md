# Building and improving

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science.

You want to make something better than what exists: a new method, tool or system, or a new instructional design or synthetic route. This page helps you work out three things: what this kind of research has to deliver in the end, what reviewers need to see before they believe it, and how it shapes each step of your project.

For what the terms claim, contribution, evidence, research strategy and research method mean, see [Key concepts](../00_start-here/key-concepts.md).

---

## 1. What kind of knowledge this research produces

**The central claim is "I built something better, and there is evidence that it is better."** In the running example used throughout this handbook:

> "On real smart contracts, our new method finds 30% more vulnerabilities than existing tools, with no increase in false positives."

That sentence contains two things: a new **artifact** (here, a vulnerability detection method) and **evidence** that it beats current practice. Delivering the thing without the evidence is product development; comparing without building anything new is [Comparative evaluation](compare_evaluate.md) `[Our analysis]`.

**It answers a design question.** Knowledge questions ask what the world is like; design questions ask how to do something better, in the form "What's an effective way to achieve X?" or "What strategies help to achieve X?" In software engineering, most non-empirical research is concerned with design questions[^easterbrook2008selecting-e28]. In a classification of software engineering research questions, the matching form is "How can we do (or automate doing) X?", "What is a better way to do X?"[^shaw2003writing-e25]. The software engineering review standards (the empirical standards of ACM SIGSOFT, the Association for Computing Machinery's Special Interest Group on Software Engineering) call this *engineering research*: "research that invents and evaluates technological artifacts"[^ralph2020empirical-e79]. The artifact can be an algorithm, model, language, method, system, tool and so on[^ralph2020empirical-e80].

**How to tell it apart from nearby strategies** `[Our analysis]`:

| Your central claim | Strategy |
|---|---|
| "Our new method finds 30% more vulnerabilities than existing tools" | Building and improving |
| "On real contracts, tool A has a higher detection rate than B" (A and B are both someone else's) | [Comparative evaluation](compare_evaluate.md) |
| "Giving vulnerability-pattern hints raises the detection rate" | [Causal explanation](explain_causality.md) |
| "We applied existing tools to one company's contracts; here is what we learned" | Experience report; not building and improving |

The dividing line is whether anything being compared is **something you newly built**. If you only compare other people's tools, it is comparative evaluation; the difference is spelled out in [Comparative evaluation](compare_evaluate.md#1-what-kind-of-knowledge-this-research-produces). The software engineering review standards also say explicitly that studies that only evaluate existing approaches, and studies that only report experience applying existing approaches, are not judged by the engineering research standard[^ralph2020empirical-e80]. A project often has both a new method and a new dataset; pick the main strategy from the central claim and treat the rest as supporting contributions (see [Key concepts](../00_start-here/key-concepts.md#research-strategy)).

**It assumes you already understand the problem well enough.** A design question presupposes that the related knowledge questions have been answered and that you know enough about the problem you want to solve[^easterbrook2008selecting-e29]. If you can't yet explain **why** existing tools miss vulnerabilities or raise false alarms, you may need a round of [Description](observe_describe.md) before you start building `[Our analysis]`. In software engineering, a long-term research program usually alternates between design questions and knowledge questions[^easterbrook2008selecting-e29].

**Beyond the thing itself, aim to deliver an understanding of why it works.** In education, design-based research (research that designs, tries out and refines an instructional intervention over several rounds in real classrooms) is widely held to produce both effective interventions and useful theory[^easterday2014design-e1]; developing teaching materials just by repeatedly trying out and refining prototypes, with no theoretical yield, does not count as this kind of research[^bakker2015introduction-e3]. Machine learning has similar advice: don't only ask "how well does it work", also ask "what made it work, and why"[^lipton2019troubling-e7].

## 2. What evidence is enough

When reviewers read a building-and-improving paper, they are roughly asking themselves the six questions below `[Our analysis]`. Most of the sources in the table come from software engineering and machine learning; in other fields, treat them as a reference:

| Reviewers will ask | Evidence you need to provide | In the smart-contract example |
|---|---|---|
| Is this problem worth solving? Why isn't the current best good enough? | State the problem, why it matters, and where the current best approach falls short[^ralph2020empirical-e81][^ralph2020empirical-e82] | How many vulnerabilities existing tools miss, how many false positives they raise, why developers don't use them |
| What is new? How does it differ from the closest work? | For each piece of existing work, say what it achieved and where it is limited, and which point you go beyond[^shaw2003writing-e3] | A comparison table: the detection rate and scope of tools A, B and C |
| Is it really better? | An empirical comparison with the best available alternatives, or a justification if that isn't possible[^ralph2020empirical-e85] | On the same set of contracts, compare against the best static analysis tool and against using a large language model directly |
| Where does the gain come from? | An ablation study: remove the method's components one at a time and see how results change[^lipton2019troubling-e4] | How much is lost when you remove the vulnerability-pattern hints, and when you remove the static analysis results |
| Does it still work in other settings? | Results on several datasets and several kinds of subjects[^lones2021avoid-e10] | Different vulnerability types, contracts from different sources |
| What are the costs and limitations? | A conceptual discussion of strengths, weaknesses and limitations[^ralph2020empirical-e81] | The cost of calling the large language model, the running time, which vulnerability types it still can't find |

Some rules for judging whether the evidence is enough. They come from software engineering writing guides and review standards, and the reasoning broadly carries over to other fields `[Our analysis]`:

- **Aim the evidence at the claim.** If you claim better performance, analyze performance, not ease of use or generality[^shaw2003writing-e29].
- **The bolder the claim, the harder the evidence must be.** "Always works" often needs analytic validation; a qualified claim such as "a 25% improvement" can be backed by evaluation; "there exists an instance" can sometimes be shown with a single positive example[^shaw2003writing-e16].
- **"It works for me" is not enough.** You also need evidence that it is useful to others[^shaw2003writing-e35]. The evidence should come from real experience or systematic analysis, not just persuasive argument or textbook examples[^shaw2002makes-e7].
- **Users' opinions alone are not enough, and neither are performance numbers that aren't compared against any benchmark or alternative.** The software engineering review standards list both kinds of evaluation as antipatterns[^ralph2020empirical-e92].
- **Two exceptions.** If the question itself is "can it be done at all?", a running system may be enough to answer it[^shaw2003writing-e10]. The more innovative the artifact and the more thorough the conceptual analysis, the less is expected of the empirical part; conversely, the less innovation, the more rigorous the evaluation has to be[^ralph2020empirical-e94][^ralph2020empirical-e90].
- **Novel doesn't mean complicated.** "Not technically complicated" is not a valid criticism; what matters is that it works, and unnecessary complexity is actually undesirable[^ralph2020empirical-e96].

These six questions apply to building and improving in every field, but "compared with what" and "measured how" depend on the field `[Our analysis]`: computer science compares against baseline tools and benchmarks, chemistry looks at yield and substrate scope, education tries designs out over several rounds in real classrooms. For concrete practice, see the method pages listed in the next section.

**Write it down:** Write your central claim in one sentence, then fill in the second and third columns of the table above. Any cell you can't fill is evidence you are still missing.

## 3. Common research methods

A strategy says what knowledge you need to produce; a method says how you get the evidence. Building and improving commonly uses these methods `[Our analysis]`:

| Method | Its role in building and improving |
|---|---|
| [Engineering research](../07_fields/computer-science/practices/engineering_research.md) (computer science practice) | The full workflow for this kind of research in computer science: choosing baselines and benchmarks, designing the evaluation, releasing research artifacts |
| [Benchmarking](../07_fields/computer-science/practices/benchmarking.md) (computer science practice) | Compare effectiveness and cost against baselines using a standard set of test subjects and an automated pipeline |
| [Optimization studies](../07_fields/computer-science/practices/optimization_study.md) (computer science practice) | Frame the problem as "find the best among many candidate solutions" and solve it with search algorithms |
| [Quantitative simulation](../06_methods/simulation_study.md) (cross-disciplinary method) | Evaluate a new design on a model when experimenting directly on the real system is impractical |
| [Controlled experiments](../06_methods/controlled_experiment.md) (cross-disciplinary method) | When the claim involves people (e.g. "developers find vulnerabilities faster with the new tool"), bring in participants for the comparison |
| [Action research](../06_methods/action_research.md) (cross-disciplinary method) | Work with a real organization, introduce an improvement there, and study what it brings about while driving the change |
| [Design-based research](../07_fields/education/practices/design_based_research.md) (education practice) | Design, try out and refine an instructional intervention over several rounds in real classrooms, while distilling design principles |
| [Synthesis and characterization studies](../06_methods/synthesis_study.md) (cross-disciplinary method, mostly from chemistry) | Methodology work on new reactions and routes, using substrate scope and yields to show what the method can and cannot do |
| [Practice-based research](../07_fields/arts/practices/practice_based_research.md) (arts practice) | The creative work produced is the basis of the knowledge contribution |

**Why action research is listed here.** The software engineering review standards define action research as empirical research that studies how an intervention (such as introducing a method or tool) affects a real-life context[^ralph2020empirical-e330]; the point of action research is to introduce a change and observe how participants respond[^ralph2020empirical-e342]. So it serves two strategies: introducing an improvement in a real organization is building and improving; watching how people in a real setting respond is [Description](observe_describe.md) `[Our analysis]`. The same standard also says that action research is not an experiment[^ralph2020empirical-e343], so this handbook does not file it under [Causal explanation](explain_causality.md) `[Our analysis]`.

A project often combines several methods: for example, benchmarking to show the method works, then a small controlled experiment to show developers can actually use it `[Our analysis]`.

## 4. How it shapes the whole project

If you choose building and improving, a few things need to be done earlier and more carefully than with other strategies. The practices below use computer science as the example; the reasoning broadly carries over to other fields `[Our analysis]`. For details specific to computer science (evaluating fuzzers, measuring overhead in systems security, artifact badges and so on), see [Engineering research](../07_fields/computer-science/practices/engineering_research.md) in the computer science section.

### Organize the whole project as "problem → technique → evaluation"

This three-part structure comes from the software engineering review standard for engineering research; other fields may organize things differently.

**Problem first, then solution.** State what problem you are solving, why it matters, and why the current best approaches fall short[^ralph2020empirical-e81][^ralph2020empirical-e82]. In software engineering, papers of this kind often state a motivating "problem" or "objective" instead of a research question, and reviewers should not criticize them for it[^ralph2020empirical-e96].

**Then the technique.** Explain the overall pipeline and how the parts fit together, and clearly mark which parts are new[^ralph2020empirical-e83].

**Finally the evaluation**, which answers the six questions from the previous section.

This order isn't just how the paper is written; it is also the order in which you do the project `[Our analysis]`. If you start building a solution before the problem is clear, what you build often doesn't address the place where people are actually stuck. [Converging on a project](../01_find-a-problem/05_converge.md#2-is-it-worth-doing) has an example: if developers avoid existing tools because of too many false positives, then finding more vulnerabilities is not the key; reducing false positives is.

### Get the baseline running early

**Get the baseline working before you design your own method.** Without a reliable baseline you will run into trouble later[^huang2023experiments-e5]. A baseline is a simple or off-the-shelf method that gives a lower bound on achievable performance; it is also a sanity check, since in machine learning complex methods are often outperformed by simple baselines[^steinhardt2018stochastic-e7].

You need at least two kinds of baseline: simpler alternatives to your method, to show that its extra complexity is really needed[^lones2021avoid-e1]; and the current state of the art[^lones2021avoid-e2]. These two points come from advice for machine learning; for what to do when a competitor's method is unavailable or won't run, see [Engineering research](../07_fields/computer-science/practices/engineering_research.md#step-4-choose-baselines) in the computer science section.

Running baselines early has another benefit `[Our analysis]`: you quickly hit blockers such as a baseline that won't run or problems in the evaluation data. These are exactly the risks that [Pilot first: rule out the biggest risks](../02_do-the-project/05_pilot-and-derisk.md) is meant to surface early.

### Estimate the room for improvement before you start

**Measure the floor and the ceiling first.** This is advice from machine learning: in empirical work, measuring a "ceiling" (an upper bound on how good performance could possibly be) is often useful. One way is to swap the hardest component for a "cheating" version first, for example by peeking at the test set or using information that won't be available at deployment time[^steinhardt2018stochastic-e24]. Together with baselines, the ceiling marks out the range where performance can fall, which helps you interpret your core results[^steinhardt2018stochastic-e24].

In the smart-contract example `[Our analysis]`: first tell the large language model directly "this contract has a reentrancy vulnerability, on line such-and-such" and see whether it can write a correct analysis. If it can't even do that well, there is little room to raise the detection rate through better prompts.

**Then ask whether the improvement is worth it.** Great contributions are rarely made by adding another decimal place[^hamming1986you-e12]. Small improvements are most useful when they serve a bigger goal[^schulman2020opinionated-e11]; a new method that only slightly beats the baseline had better be very simple, or no one will use it[^schulman2020opinionated-e12].

**Write it down:** Write down what your baseline achieves, roughly where the ceiling is, and what you hope to reach. The distance between those three numbers is your room for improvement.

### Effects on later stages

The table below is this handbook's own summary `[Our analysis]`:

| Stage | What to watch for in building and improving |
|---|---|
| [Converging on a project](../01_find-a-problem/05_converge.md) | Phrase the claim as "under these conditions, better than whom, by how much"; make the comparison table specific down to each closest piece of work |
| [From research questions to an evidence plan](../02_do-the-project/01_question-to-evidence.md) | Sketch the empty results table first: rows are your method and each baseline; columns are effectiveness, cost, and different datasets |
| [Validity and limitations](../02_do-the-project/04_validity-and-limits.md) | Examples you looked at during development can't be reused for evaluation; test on data you haven't seen (the programming languages community's empirical evaluation checklist makes this a requirement[^blackburn2018sigplan-e12]) |
| [Running and iterating](../02_do-the-project/06_run-and-iterate.md) | Add changes one at a time, and keep versions you can use for ablation |
| [Telling the story and writing the paper](../03_write-and-publish/01_story-and-paper.md) | Write it as "problem → technique → evaluation", mark the new parts, and be honest about limitations |

## 5. Which fields use it

Only what our sources can confirm:

- **Computer science.** According to an analysis, published in 2003, of papers at ICSE (the International Conference on Software Engineering), the top software engineering conference, papers reporting a new development or analysis technique were the most common kind[^shaw2003writing-e26].
- **Education.** Design-based research aims, among other things, to produce effective instructional interventions[^easterday2014design-e1], so it belongs here `[Our analysis]`.
- **Chemistry.** Synthetic methodology belongs here `[Our analysis]`. Take the American Chemical Society's *Journal of Organic Chemistry*: it expects synthetic methods papers to show conceptual novelty in strategy, transformation or route, not merely the extension of previously reported chemistry to a different class of substrates, reagents or catalysts[^acsjocguidelines-e30].
- **Arts.** When a creative work produced is the basis of the knowledge contribution, it is practice-based research[^candy2006practice-e1]. It is also "making something new", but it usually isn't compared against a baseline, and its criteria for judgment are very different from the fields above `[Our analysis]`; see that method page for details.

## 6. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Designing a solution before understanding why existing methods fail | A design question presupposes understanding of the problem[^easterbrook2008selecting-e29] |
| Comparing only against your own earlier work, not the current best | Systems security research lists this as a comparison flaw[^vanderkouwe2019sok-e4] |
| Presenting a weak baseline as "state of the art" | It exaggerates the apparent benefit[^blackburn2018sigplan-e4] |
| Carefully tuning your own method while competitors run with default or suboptimal settings | What you are comparing is tuning effort, not the new design `[Our analysis]`; for how to treat competitors fairly, see [Comparative evaluation](compare_evaluate.md#was-every-competitor-treated-equally) |
| Bundling several changes at once with no ablation | You can't tell where the gain comes from; sometimes only one of them actually matters[^lipton2019troubling-e4] |
| Beating others only because of a better implementation | The gain doesn't come from the new design, so the novelty is questionable[^vanderkouwe2019sok-e8] |
| Bolting huge machinery onto a simple method and calling it "better" | Adding big machinery almost always improves results a little; this is exactly the paper pattern being satirized[^zeller2021devil-e6] |
| Claiming general effectiveness from good results on one dataset | Doing well on one dataset doesn't mean doing well on others[^lones2021avoid-e10] |

## 7. Further reading

- **Overall framework**: Shaw 2003, "Writing Good Software Engineering Research Papers", uses three tables (research questions, results, validation) to set out what an engineering paper must answer; Shaw 2002 uses the same three dimensions to discuss what makes good software engineering research.
- **Review standards**: the engineering research standard in the ACM SIGSOFT (Association for Computing Machinery Special Interest Group on Software Engineering) Empirical Standards, which lists essential attributes, desirable attributes, and invalid criticisms.
- **Design questions and knowledge questions**: Easterbrook et al. 2008, §2.
- **Where evaluations go wrong**: Lipton & Steinhardt 2019, "Troubling Trends in Machine Learning Scholarship".
- **Concrete practice in computer science**: [Engineering research](../07_fields/computer-science/practices/engineering_research.md) in the computer science section, with a checklist.
- **An example outside computer science**: [Design-based research](../07_fields/education/practices/design_based_research.md).

[^easterbrook2008selecting-e28]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e28)
[^easterbrook2008selecting-e29]: Easterbrook et al. 2008, §2.0. [Evidence](../../sources/notes/easterbrook2008selecting.md#e29)
[^steinhardt2018stochastic-e7]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e7)
[^steinhardt2018stochastic-e24]: Steinhardt 2018, Some further practical ideas. [Evidence](../../sources/notes/steinhardt2018stochastic.md#e24)
[^shaw2003writing-e3]: Shaw 2003, §3.3. [Evidence](../../sources/notes/shaw2003writing.md#e3)
[^shaw2003writing-e10]: Shaw 2003, §4.1, after Table 5. [Evidence](../../sources/notes/shaw2003writing.md#e10)
[^shaw2003writing-e16]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e16)
[^shaw2003writing-e25]: Shaw 2003, §2.1, Table 1. [Evidence](../../sources/notes/shaw2003writing.md#e25)
[^shaw2003writing-e26]: Shaw 2003, §3.2. [Evidence](../../sources/notes/shaw2003writing.md#e26)
[^shaw2003writing-e29]: Shaw 2003, §4.3. [Evidence](../../sources/notes/shaw2003writing.md#e29)
[^shaw2003writing-e35]: Shaw 2003, §4.3. [Evidence](../../sources/notes/shaw2003writing.md#e35)
[^shaw2002makes-e7]: Shaw 2002, §2.3. [Evidence](../../sources/notes/shaw2002makes.md#e7)
[^ralph2020empirical-e79]: SIGSOFT Engineering Research standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e79)
[^ralph2020empirical-e80]: SIGSOFT Engineering Research standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e80)
[^ralph2020empirical-e81]: SIGSOFT Engineering Research standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e81)
[^ralph2020empirical-e82]: SIGSOFT Engineering Research standard, footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e82)
[^ralph2020empirical-e83]: SIGSOFT Engineering Research standard, footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e83)
[^ralph2020empirical-e85]: SIGSOFT Engineering Research standard, Essential Attributes (methods). [Evidence](../../sources/notes/ralph2020empirical.md#e85)
[^ralph2020empirical-e90]: SIGSOFT Engineering Research standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e90)
[^ralph2020empirical-e92]: SIGSOFT Engineering Research standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e92)
[^ralph2020empirical-e94]: SIGSOFT Engineering Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e94)
[^ralph2020empirical-e96]: SIGSOFT Engineering Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e96)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019, §3.2, p. 3. [Evidence](../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019, §5.1, p. 8. [Evidence](../../sources/notes/lipton2019troubling.md#e7)
[^lones2021avoid-e1]: Lones 2021, §5.2, p. 21. [Evidence](../../sources/notes/lones2021avoid.md#e1)
[^lones2021avoid-e2]: Lones 2021, §5.2, p. 21. [Evidence](../../sources/notes/lones2021avoid.md#e2)
[^lones2021avoid-e10]: Lones 2021, §6.3, p. 24. [Evidence](../../sources/notes/lones2021avoid.md#e10)
[^blackburn2018sigplan-e4]: SIGPLAN Empirical Evaluation Checklist, Suitable Comparison. [Evidence](../../sources/notes/blackburn2018sigplan.md#e4)
[^blackburn2018sigplan-e12]: SIGPLAN Empirical Evaluation Checklist, Tested on training set. [Evidence](../../sources/notes/blackburn2018sigplan.md#e12)
[^vanderkouwe2019sok-e4]: van der Kouwe et al. 2019, §II-D. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e4)
[^vanderkouwe2019sok-e8]: van der Kouwe et al. 2019, §II-E. [Evidence](../../sources/notes/vanderkouwe2019sok.md#e8)
[^zeller2021devil-e6]: Zeller 2021, THE RUBE GOLDBERG. [Evidence](../../sources/notes/zeller2021devil.md#e6)
[^huang2023experiments-e5]: Jia-Bin Huang 2023, tweet thread, *Start with a baseline*. [Evidence](../../sources/notes/huang2023experiments.md#e5)
[^hamming1986you-e12]: Hamming 1986, after the "ambiguity" paragraph. [Evidence](../../sources/notes/hamming1986you.md#e12)
[^schulman2020opinionated-e11]: Schulman 2020, Aim High, and Climb Incrementally Towards High Goals. [Evidence](../../sources/notes/schulman2020opinionated.md#e11)
[^schulman2020opinionated-e12]: Schulman 2020, Aim High, and Climb Incrementally Towards High Goals. [Evidence](../../sources/notes/schulman2020opinionated.md#e12)
[^easterday2014design-e1]: Easterday et al. 2014, Introduction, p. 317. [Evidence](../../sources/notes/easterday2014design.md#e1)
[^bakker2015introduction-e3]: Bakker & van Eerde 2015, §16.1.2.1, p. 430. [Evidence](../../sources/notes/bakker2015introduction.md#e3)
[^acsjocguidelines-e30]: JOC author guidelines, Scope of the Journal (a). [Evidence](../../sources/notes/acsjocguidelines.md#e30)
[^ralph2020empirical-e330]: SIGSOFT Action Research standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e330)
[^ralph2020empirical-e342]: SIGSOFT Action Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e342)
[^ralph2020empirical-e343]: SIGSOFT Action Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e343)
[^candy2006practice-e1]: Candy 2006, Summary, p. 1. [Evidence](../../sources/notes/candy2006practice.md#e1)
