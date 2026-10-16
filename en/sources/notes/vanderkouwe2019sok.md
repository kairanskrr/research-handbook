# van der Kouwe et al. 2019: SoK: Benchmarking Flaws in Systems Security

- Source: `vanderkouwe2019sok`, [original](https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf)
- Version: IEEE EuroS&P 2019, local PDF `papers/pdf/vanderkouwe2019sok.pdf`.
- Note: Covers performance evaluation in systems security and lists 22 benchmarking flaws (numbered A1-F4 in the paper); most also apply to other areas such as systems and programming languages.

### E1

- Location: Abstract
- Quote: "tier-1 papers contain an average of five benchmarking flaws and we find only a single paper in our sample without any benchmarking flaws"
- Key point: 50 defense papers from top venues contain an average of five benchmarking flaws each, and only one paper has none.

### E2

- Location: §II-A Selective benchmarking (A1)
- Quote: "we should always include benchmarks that evaluate all operations whose performance one might reasonably expect to be impacted"
- Key point: Include benchmarks for every operation whose performance might reasonably be expected to be affected, not only the parts that favor your system.

### E3

- Location: §II-A Selective benchmarking (A2)
- Quote: "Any paper which arbitrarily selects a subset of benchmarks and presents it as a single overall performance overhead number as if it is still representative contains benchmarking flaw A2"
- Key point: Arbitrarily selecting a subset of benchmarks and reporting the result as a representative overall overhead is a flaw.

### E4

- Location: §II-D Improper comparison of benchmarking results (D2, D3)
- Quote: "D2: only evaluate against yourself refers to cases where papers compare their new system to their own earlier work rather than the state of the art." / "D3: unfair benchmarking of competitors refers to papers that do compare against competitors but do so in an unfair way. For example, they might use a configuration that is not optimal."
- Key point: Comparing only against your own earlier work instead of the state of the art, or comparing against competitors but running them in a suboptimal configuration, are both flaws.

### E5

- Location: §II-E Benchmarking omissions (E1)
- Quote: "E1: not all contributions evaluated refers to cases where a paper claims to achieve a certain goal, but does not empirically determine whether this goal has been reached."
- Key point: Claiming to achieve a goal without empirically checking whether it was achieved is a flaw.

### E6

- Location: Appendix, E2 Only measure run-time overhead
- Quote: "performance measurements are not complete without measuring memory overhead" / "Other missing measurements include the amount of extra network and/or disk IO, increased binary size after instrumentation, and the time taken to instrument the protected program."
- Key point: Measuring run time alone is not enough; also measure memory overhead and other costs such as extra network and disk I/O, increased binary size, and processing time.

### E7

- Location: §II-E Benchmarking omissions (E3)
- Quote: "Without knowing how accurate the system is, it is impossible to judge its value, making the paper incomplete."
- Key point: When the system makes decisions (for example, whether behavior is malicious), you must measure false positives and false negatives; without knowing its accuracy, its value cannot be judged.

### E8

- Location: §II-E Benchmarking omissions (E4)
- Quote: "If the system is faster than the state of the art merely due to a faster implementation rather than the newly designed optimizations, its novelty is questionable."
- Key point: Without measuring each component separately, you cannot know whether each part is needed; if the system beats the state of the art only because of a faster implementation rather than the new design, its novelty is questionable.

### E9

- Location: §II-B Improper handling of benchmark results (B1)
- Quote: "they are not an indication of how fast the system would run in practice. For this purpose, more realistic system benchmarks are needed."
- Key point: Microbenchmarks (tests of one specific operation) do not show how fast the system runs in practice; more realistic system-level benchmarks are needed.

### E10

- Location: §II-C Using the wrong benchmarks (C3)
- Quote: "when they benchmark their system using the same data set that they used to train it or, more generally, if there is any overlap between the training and test sets"
- Key point: Evaluating a system on the data used to tune or train it is a flaw.

### E11

- Location: §VI Recommendations
- Quote: "authors should consider which performance dimensions the solution could possibly affect (for example, CPU, concurrency, memory, IO, system calls" / "and include at least one appropriate benchmark for each dimension."
- Key point: First list every performance dimension the solution could affect, and include at least one appropriate benchmark for each.

### E12

- Location: §I Introduction
- Quote: "We believe that most, if not all, benchmarking flaws we found are unintentional" / "many prevalent benchmarking flaws we found can, in fact, be prevented altogether with little effort and simple benchmarking practices."
- Key point: The authors believe most of these flaws are unintentional, and many can be avoided with little extra effort.

### E13

- Location: §II, Table I
- Quote: "F1 Missing platform specification F2 Missing software versions F3 Subbenchmarks not listed F4 Relative numbers only"
- Key point: Reproducibility flaws: missing platform specification, missing software versions, subbenchmarks not listed, and relative numbers only (no absolute numbers).

### E14

- Location: §II-D Improper comparison of benchmarking results (D1)
- Quote: "In systems defenses, the proper baseline is usually the original system using default settings with no defenses enabled."
- Key point: (Systems security) When computing overhead, the proper baseline is usually the original system with default settings and no defenses enabled; quietly adding things to the baseline hides overhead in it.

### E15

- Location: §IV Survey Results
- Quote: "The lack of indication of significance of data and benchmark subsetting without proper justification are by far the most widespread, respectively affecting 80% and 69% of the applicable papers we surveyed."
- Key point: The two most widespread flaws are giving no indication of the significance (variability) of the data (80%) and subsetting benchmark suites without proper justification (69%).

### E16

- Location: §II Benchmarking Flaws
- Quote: "it should be complete in the sense that it verifies all claimed contributions of the system and shows the extent of any negative impact the system may have." / "soundness, the requirement that all numbers measure what is intended with reasonable accuracy and repeatability"
- Key point: A good evaluation is complete (verifies every claimed contribution and shows the extent of any negative impact), relevant, sound (every number measures what it is meant to measure, with reasonable precision and repeatability), and reproducible.

### E17

- Location: §VI Recommendations; §II-A
- Quote: "Authors should run all subbenchmarks that can reasonably be run and be explicit about reasons for omitting the others." / "a subset arbitrarily selected from a large set of tests is unlikely to be representative of the full set"
- Key point: Run every subbenchmark that can reasonably be run and state why the others were omitted; do not present an overall result on a subset as a complete result comparable with others. A subset arbitrarily picked from a large set of tests is unlikely to be representative.

### E18

- Location: §II-A, A3
- Quote: "if throughput seems to scale linearly with the number of concurrent connections, it suggests that the range of this variable is too restricted because the system cannot keep this up forever."
- Key point: If throughput seems to scale linearly with the number of concurrent connections, the range of that variable is too narrow, because no system can keep that up forever.

### E19

- Location: §II-D, D1; §VI
- Quote: "In systems defenses, the proper baseline is usually the original system using default settings with no defenses enabled." / "Often, this means avoiding any non-default compiler flags or emulation techniques that would slow down the baseline."
- Key point: In systems defense research, the proper baseline is usually the original system with default settings and no defenses enabled; don't add non-default compiler flags or emulation to the baseline, which slows it down and hides overhead in it.

### E20

- Location: §II-E, E2 and E4
- Quote: "A paper contains benchmarking flaw E2: only measure run-time overhead and its evaluation is incomplete whenever it does not measure important performance characteristics." / "If the system is faster than the state of the art merely due to a faster implementation rather than the newly designed optimizations, its novelty is questionable."
- Key point: Measuring only run-time overhead and not other important performance characteristics such as memory leaves the evaluation incomplete; optional components must be evaluated separately, or a faster system may just reflect a faster implementation rather than the new design.

### E21

- Location: §VI Recommendations
- Quote: "flaws B4 (no indication of significance of data), B5 (incorrect averaging across benchmark scores), F1 (missing platform specification), and F2 (missing software versions) can be addressed by simply adding readily available data to the paper."
- Key point: Giving no indication of variability, averaging incorrectly across benchmarks, missing platform specification, and missing software versions can all be fixed simply by adding data you already have to the paper.

### E22

- Location: §II-B, B5
- Quote: "Only the geometric mean is appropriate for averaging overhead ratios."
- Key point: Only the geometric mean is appropriate for averaging overhead ratios; the arithmetic mean depends on which configuration is taken as the baseline.

### E23

- Location: §II-F, F4
- Quote: "The absolute numbers are valuable for the reader to perform a sanity check (is the system configured in a reasonable way?) and because a slow baseline often means overhead will be less visible."
- Key point: Report absolute numbers as well as relative overhead: they let readers do a sanity check (is the system configured reasonably?), and a slow baseline often makes overhead look smaller.

### E24

- Location: §II-B, B3
- Quote: "the difference between 10% overhead and 20% overhead is presented as 10% more overhead, while it is actually 100% more"
- Key point: A typical miscalculation: describing a change from 10% to 20% overhead as "10% more," when it is actually 100% more.

### E25

- Location: §I Introduction
- Quote: "We believe that most, if not all, benchmarking flaws we found are unintentional and just denote insufficient attention devoted to performance benchmarking in our community."
- Key point: The authors believe most of these flaws are unintentional and simply reflect too little attention to performance benchmarking.

### E26

- Location: Abstract
- Quote: "we identify 22 benchmarking flaws that threaten the validity of systems security evaluations, and survey 50 defense papers published in top venues." / "tier-1 papers contain an average of five benchmarking flaws and we find only a single paper in our sample without any benchmarking flaws"
- Key point: The authors identify 22 benchmarking flaws that threaten the validity of evaluations and survey 50 defense papers from top venues: an average of five flaws per paper, with only one paper free of them.

### E27

- Location: §I Introduction; §III-B Selected venues
- Quote: "For this purpose, we selected all defense papers with benchmarking results published in 2010 and 2015." / "the “top 4” venues are the most influential and de-facto set the standard for benchmarking practices in the community."
- Key point: Sample: all defense papers with benchmarking results published in 2010 and 2015 at the four top security conferences, chosen because they are the most influential and de facto set the field's benchmarking practices.

### E28

- Location: §III-A Classification methodology
- Quote: "two persons independently categorized each paper for each flaw as correct, flawed, underspecified, or not applicable." / "the readers discussed their assessments to converge on a final classification. This was the case for 8 out of 50 papers (16%)."
- Key point: Two people independently classified each paper for each flaw (correct, flawed, underspecified, or not applicable); the 8 papers (16%) with disagreements were discussed to reach a final classification.

### E29

- Location: §III-A Classification methodology
- Quote: "We use only information from the papers themselves and did not contact the authors for explanation. Effectively, we impose on ourselves the same constraints reviewers face when deciding whether to accept or reject a paper in a double-blind submission system."
- Key point: The authors used only information in the papers themselves and did not contact authors, imposing on themselves the same constraints reviewers face in double-blind review.

### E30

- Location: §I Introduction
- Quote: "As we do not allege intent, we use the term benchmarking flaws instead of the (tongue in cheek) term “benchmarking crimes” used earlier in the literature" / "We believe that most, if not all, benchmarking flaws we found are unintentional and just denote insufficient attention devoted to performance benchmarking in our community."
- Key point: Because they do not allege intent, the authors say "benchmarking flaws" rather than the tongue-in-cheek "benchmarking crimes" of earlier literature, and they believe most flaws are unintentional, reflecting only insufficient attention to performance benchmarking in the field.

### E31

- Location: §VII Limitations; Appendix A
- Quote: "we think that naming and shaming would be counterproductive as in our opinion the problem is not with individuals but rather the community as a whole." / "detailed discussion in Appendix A that should allow others to perform the survey themselves according to the same criteria." / "to keep the discussion anonymous with regard to the papers in our sample, we either abstract away or change some of the details."
- Key point: The authors do not disclose which papers have which flaws, arguing that naming and shaming would be counterproductive because the problem lies with the community rather than individuals; to compensate, the appendix details the classification criteria so others can redo the survey by the same standards, and its examples are abstracted or altered to preserve anonymity.

### E32

- Location: §VII Limitations
- Quote: "published papers are not necessarily a representative sample of all papers, especially at the top conferences."
- Key point: Limitation: published papers are not necessarily representative of all papers (including submissions), especially at top conferences.

### E33

- Location: §IX Related work, Benchmarking advice
- Quote: "While these studies demonstrate important benchmarking problems, the lack of a survey means they cannot determine the impact these potential problems have on the research literature."
- Key point: Articles that point out problems only through examples and their own tests show that the problems exist, but without a survey they cannot tell how much these problems affect the published literature.

### E34

- Location: §I Introduction
- Quote: "As for the cause of the flaws we encountered, we can only speculate."
- Key point: On the causes of the flaws, the authors say plainly that they can only speculate.

### E35

- Location: §V Impact
- Quote: "the problem of benchmarking flaws is not an issue of a few authors and reviewers being particularly careless (or malicious), but rather a community-wide lack of awareness of or attention to these problems."
- Key point: The flaws are spread fairly evenly across papers, suggesting the problem is not a few especially careless (or malicious) authors and reviewers, but a community-wide lack of awareness of, or attention to, these issues.
