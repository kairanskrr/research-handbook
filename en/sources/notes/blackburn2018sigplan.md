# Berger, Blackburn, Hauswirth & Hicks 2018: SIGPLAN Empirical Evaluation Checklist

- Source: `blackburn2018sigplan`, [Original](http://www.sigplan.org/Resources/EmpiricalEvaluation/)
- Version: October 2018 version, a one-page checklist with annotations and FAQ. Local PDF `papers/pdf/blackburn2018sigplan.pdf`.
- Note: A checklist for empirical evaluation drawn up by ACM SIGPLAN (the Association for Computing Machinery's Special Interest Group on Programming Languages). Its examples, such as compilers and benchmark suites, come from computing; categories such as "explicit claims," "appropriate baselines," and "report distributions" apply across fields.

### E1

- Location: Clearly Stated Claims › Claims not explicit
- Quote: "Claims must be explicit in order for the reader to assess whether the empirical evaluation supports them."
- Key point: Claims must be explicit so that readers can judge whether the evaluation supports them.

### E2

- Location: Clearly Stated Claims › Claims not appropriately scoped
- Quote: "The truth of a claim should clearly follow from the evidence provided. Claims that are not fully supported mislead readers."
- Key point: A claim should clearly follow from the evidence provided; claims that are not fully supported mislead readers.

### E3

- Location: Clearly Stated Claims › Fails to acknowledge limitations
- Quote: "Stating no limitations at all, or only tangential ones, while omitting the more relevant ones may mislead the reader into drawing overly-strong conclusions."
- Key point: Stating no limitations, or only tangential ones while omitting the relevant ones, can lead readers to overly strong conclusions.

### E4

- Location: Suitable Comparison › Fails to compare against appropriate baseline
- Quote: "A ‘straw man’ baseline that is misrepresented as state-of-the-art is also problematic, as it would inﬂate apparent beneﬁt."
- Key point: Presenting a weak "straw man" baseline as the state of the art inflates the apparent benefit of a new method.

### E5

- Location: Suitable Comparison › Comparison is unfair
- Quote: "Comparisons to a competing system should not unfairly disadvantage that system."
- Key point: Comparisons should not unfairly disadvantage the competing system. The original's example comes from computing: compiling the competitor at the lowest optimization level and your own system at the highest.

### E6

- Location: Notes › Fails to Compare Against Appropriate Baseline
- Quote: "The baseline could also be an unsophisticated approach to the same problem, e.g., a fancy testing tool is usefully compared against one that is purely random, in order to see whether it does better."
- Key point: A baseline can also be an unsophisticated approach to the same problem, for example comparing a fancy tool against a purely random one to see whether it really does better.

### E7

- Location: Adequate Data Analysis › Insufficient number of trials
- Quote: "Failure to do so risks treating noise as signal."
- Key point: Too few repetitions risk treating noise as signal.

### E8

- Location: Adequate Data Analysis › No data distribution reported
- Quote: "Reporting just a measure of central tendency (e.g., a mean or median) can mislead the reader, especially when the distribution is bimodal or has signiﬁcant variance."
- Key point: Reporting only a mean or median can mislead; also report the spread (variance, standard deviation, quantiles) or confidence intervals.

### E9

- Location: Appropriate and Clear Experimental Design › Misleading summary of results
- Quote: "it is not appropriate to summarize speedups of 4%, 6%, 7%, and 49% as ’up to 49%’. Instead, the full distribution of results must be reported."
- Key point: Do not summarize speedups of 4%, 6%, 7%, and 49% as "up to 49%"; report the full distribution of results.

### E10

- Location: Notes › Fails to Acknowledge Limitations
- Quote: "threats to validity sections in software engineering papers often mention threats of little signiﬁcance while ignoring real threats."
- Key point: Some critics say "threats to validity" sections often list trivial threats while ignoring real ones. The checklist authors hold that this is no reason to omit limitations.

### E11

- Location: Notes › Fails to Acknowledge Limitations
- Quote: "For science to progress, we need to be honest about what we have achieved."
- Key point: For science to progress, we need to be honest about what we have actually achieved.

### E12

- Location: Appropriate and Clear Experimental Design › Tested on training set
- Quote: "When a system aims to be general but was developed with close consideration of speciﬁc examples, it is essential that the evaluation explicitly perform cross-validation, so that the system is evaluated on data distinct from the training set."
- Key point: Examples consulted during development cannot be reused for evaluation; the evaluation must use data not used during development.

### E13

- Location: Relevant Metrics › Indirect or inappropriate proxy metric
- Quote: "Proxy metrics can substitute for direct ones only when the substitution is clearly, explicitly justiﬁed."
- Key point: When a proxy metric replaces the metric you actually care about, the substitution must be explicitly justified.

### E14

- Location: Note under the title
- Quote: "This checklist is meant to support informed judgement, not supplant it."
- Key point: The checklist is meant to support judgment, not replace it.

### E15

- Location: Suitable Comparison › Comparison is unfair
- Quote: "Comparisons to a competing system should not unfairly disadvantage that system." / "it would be unfair to compile the state-of-the-art baseline at -O0 optimization level, while using -O3 for the proposed system."
- Key point: Comparisons should not unfairly disadvantage the competing system, for example by compiling the competitor at the lowest optimization level and your own system at the highest.

### E16

- Location: Principled Benchmark Choice › Inappropriate suite
- Quote: "Evaluations should be conducted using appropriate established benchmarks where they exist so that claimed results are more likely to generalize." / "it would be wrong to use a singlethreaded suite for studying parallel performance."
- Key point: Use established benchmark suites where they exist, so results are more likely to generalize, but use them where they fit; for example, do not study parallel performance with a single-threaded suite.

### E17

- Location: Principled Benchmark Choice › Unjustiﬁed use of non-standard suite(s)
- Quote: "sometimes a non-standard suite, such as one that is subsetted or homegrown, is the better choice. In that case, a rationale, and possible limitations, must be provided to demonstrate why using a standard suite would have been worse."
- Key point: If you use a subsetted or homegrown non-standard suite, you must give a rationale and possible limitations, showing why a standard suite would have been worse.

### E18

- Location: Notes › Unjustiﬁed Use of Non-Standard Suite(s)
- Quote: "A concern we heard was that use of standard suites may lead to work that overﬁts to that benchmark." / "Papers we looked at often subset a benchmark, or cherry-picked particular programs."
- Key point: Some worried that standard suites lead to overfitting to the benchmark; the checklist authors found the opposite problem more common in programming languages research: subsetting benchmarks and cherry-picking programs.

### E19

- Location: Notes › Unjustiﬁed Use of Non-Standard Suite(s)
- Quote: "Note that ‘benchmark’ in this category includes what is measured and the parameters of that measurement. One example of an oft-unappreciated benchmark parameter is timeout choice."
- Key point: A benchmark covers not only what is measured but also the measurement parameters; timeout choice is an often-overlooked benchmark parameter.

### E20

- Location: Principled Benchmark Choice › Kernels instead of full applications
- Quote: "a claim that a system beneﬁts applications should be tested on such applications directly, and not only on micro-kernels, which may lack important characteristics of full applications."
- Key point: A claim that a system benefits applications must be tested on applications directly, not only on micro-kernels, which may lack important features of full applications.

### E21

- Location: Appropriate and Clear Experimental Design › Fails to measure all important Effects
- Quote: "All important effects should be measured to show the true cost of a system."
- Key point: Measure all important effects to show the true cost of a system. The original's example: a compiler optimization makes programs faster but may greatly increase compile time, so compile time must also be measured.

### E22

- Location: Appropriate and Clear Experimental Design › Insufﬁcient information to repeat
- Quote: "All parameters (including default values) should be included, as well as all version numbers of software, and full details of hardware platforms."
- Key point: Report all parameters (including defaults), all software version numbers, and full details of the hardware platform.

### E23

- Location: Appropriate and Clear Experimental Design › Unreasonable platform
- Quote: "a claim that relates to performance on mobile platforms should not have an evaluation performed exclusively on servers."
- Key point: The evaluation platform must match the claim; for example, a claim about performance on mobile platforms cannot be evaluated only on servers.

### E24

- Location: Appropriate and Clear Experimental Design › Ignores key design parameters
- Quote: "Key parameters should be explored over a range to evaluate sensitivity to their settings." / "All expected system conﬁgurations (e.g., from warmup to steady state) should be considered."
- Key point: Vary key parameters over a range to see how sensitive the results are to them, and consider all expected system states, for example from warmup to steady state.

### E25

- Location: Appropriate and Clear Experimental Design › Gated workload generator
- Quote: "Load generators for typical transaction-oriented systems should be ’open loop’, to generate work independent of the performance of the system under test."
- Key point: For transaction-oriented systems, load generators should be "open loop": they generate work at a rate independent of how fast the system under test runs.

### E26

- Location: Appropriate and Clear Experimental Design › Tested on training set
- Quote: "a static analysis should not be exclusively evaluated on programs used to inform its development."
- Key point: Programs consulted during development must not be the only evaluation subjects; evaluate on data not used during development.

### E27

- Location: Adequate Data Analysis › Insufﬁcient number of trials
- Quote: "Failure to do so risks treating noise as signal. Similarly, more trials may be needed to get the system into an intended state (e.g., into a steady state that avoids warm-up effects)."
- Key point: Modern systems with nondeterministic performance need many trials, or noise may be treated as signal; more trials may also be needed to bring the system into its intended state, such as a steady state free of warmup effects.

### E28

- Location: Notes › Inappropriate Summary Statistics
- Quote: "The geometric mean should only be used when comparing values with different ranges, and the harmonic mean when comparing rates. When distributions have outliers, a median should be presented."
- Key point: Use the geometric mean only to compare values with different ranges, the harmonic mean to compare rates, and the median when distributions have outliers.

### E29

- Location: Appropriate Presentation of Results › Inappropriately truncated axes / Ratios plotted incorrectly
- Quote: "A truncated graph (with an axis not including zero) will exaggerate the importance of a difference." / "This misleading effect can be avoided either by using a log scale or by normalizing to the lowest (highest) value."
- Key point: An axis that does not start at zero exaggerates differences; plotting ratios on a linear scale distorts perception (2.0 and 0.5 are reciprocals but lie at different distances from 1.0), so use a log scale or normalize to the lowest (highest) value.

### E30

- Location: Appropriate Presentation of Results › Inappropriate level of precision
- Quote: "reporting ’49.9%’ when the experimental error is +/- 1% overstates the level of precision of the result."
- Key point: Reporting "49.9%" when the experimental error is plus or minus 1% overstates the precision of the result.

### E31

- Location: FAQ › How does the checklist relate to the artifact evaluation process?
- Quote: "Artifact evaluation typically occurs after reviewing a paper, to check that the claims and evidence given in the paper match reality, in the artifact."
- Key point: Artifact evaluation usually takes place after the paper is reviewed, to check that the paper's claims and evidence match the submitted artifact.

### E32

- Location: FAQ › How did you determine which items to include?
- Quote: "The committee examined a sampling of papers from the last several years of ASPLOS, ICFP, OOPSLA, PLDI, and POPL, and considered those that contained some form of empirical evaluation."
- Key point: The checklist committee sampled recent papers with empirical evaluations from ASPLOS, ICFP, OOPSLA, PLDI, and POPL and drew common good and bad practices from them.
