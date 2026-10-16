# Wagner et al. 2020: Challenges in Survey Research

- Source: `wagner2020challenges`, [arXiv:1908.05899](https://arxiv.org/abs/1908.05899)
- Version: arXiv v4 (2020-04-27), included in *Contemporary Empirical Methods in Software Engineering* (Springer 2020), pp. 93-125

### E1

- Location: §2 Survey Research and Theory Building
- Quote: "Descriptive surveys can be conducted to enable assertions about some population like the distribution of certain attributes (e.g., usage of requirements elicitation techniques). The concern is not why the observed distribution exists, but instead what that distribution is."
- Key point: Descriptive surveys support assertions about a population, such as the distribution of certain attributes (for example, use of requirements elicitation techniques); the concern is what the distribution is, not why.

### E2

- Location: §2, Take Aways
- Quote: "Theories are of high value to guide the design of surveys."
- Key point: Theories are of high value in guiding survey design.

### E3

- Location: §3 Issues in Sampling
- Quote: "At the beginning of any design of survey research, we should clarify what the target population is that we try to characterize and generalize to."
- Key point: The first step in designing survey research is to state the target population you want to characterize and generalize to.

### E4

- Location: §3 Issues in Sampling
- Quote: "This brings us, however, to the problem that in most cases, we have no solid understanding about the target population."
- Key point: In most cases we have no solid understanding of the target population (for example, all developers worldwide).

### E5

- Location: §3.1 Representativeness
- Quote: "They have the bias that only people registered at Stack Overﬂow can be sampled." [...] "Then, we can compare the distributions in our survey and the larger surveys to estimate representativeness."
- Key point: You can estimate representativeness by comparing your sample's demographic distributions with large public surveys (such as Stack Overflow's annual developer survey, which itself covers only registered users).

### E6

- Location: §3.2 Sample Size Estimation
- Quote: "So, for most intents and purposes, with a sample size of more than 400, we could claim a strong generalizability given that we also checked the representativeness as described above. Of course, most survey will fall short of this."
- Key point: By the Yamane formula, with about 23 million developers worldwide, a sample of more than 400 plus a representativeness check would support a claim of strong generalizability; most surveys fall short of this.

### E7

- Location: §3.2 Sample Size Estimation
- Quote: "From the studies we could estimate that roughly 98% of the e-mails were delivered, and that the response rate was rather low, between 2% and 4%."
- Key point: In the authors' pilot survey, emailed to GitHub developers, the response rate was only 2% to 4%.

### E8

- Location: §3.3 Ethics
- Quote: "Baltes & Diehl (2016) discuss that the common practice of sending unsolicited e-mails to GitHub developers could be ethically problematic."
- Key point: The common practice of sending unsolicited emails to GitHub developers may be ethically problematic.

### E9

- Location: §3.3 Ethics
- Quote: "The Insight Association provides ethical guidelines that consider unethical sampling, among other practices" [...] "Hence, using GitHub or Stack Overﬂow information of users would not be an ethical way to contact potential survey participants."
- Key point: Under the market research industry's ethical guidelines, using users' information from GitHub or Stack Overflow to contact potential participants is not an ethical approach.

### E10

- Location: §3.3 Ethics
- Quote: "All we could do was to design a short and cordial invitation e-mail that, besides acting as informed consent form including ethical and privacy considerations, was of opt-in nature." [...] "receiving feedback from potential participants who were annoyed by this."
- Key point: The authors' approach: a short, cordial, opt-in invitation email that also served as the informed consent form, with ethics and privacy information; they still received complaints from people who felt disturbed.

### E11

- Location: §4 Invitation and Follow-Up
- Quote: "it also allows to accurately calculate the response rate and control the participation along the data collection" [...] "This increase of control by inviting subjects individually typically comes at the cost of a lower number of total responses." [...] "but it also comes at the cost of control in who provides the responses"
- Key point: Closed invitations (inviting specific people) allow an accurate response rate and control over participation, usually at the cost of fewer responses; open invitations (anyone with the link can respond) spread further but lose control over who is responding.

### E12

- Location: §4 Invitation and Follow-Up
- Quote: "At the same time, we were not able to calculate the response rate and also noticed a signiﬁcant drop-out rate (i.e. participants entering the survey out of curiosity and dropping out on the ﬁrst survey page already)."
- Key point: After switching to an open invitation, the authors could not calculate a response rate and saw a large drop-out rate (people entering out of curiosity and leaving on the first page).

### E13

- Location: §4 Invitation and Follow-Up
- Quote: "In both surveys, we therefore implemented a follow-up invitation roughly two weeks before closing the survey."
- Key point: The authors sent a follow-up invitation roughly two weeks before closing the survey.

### E14

- Location: §5 Alternative Approaches for Statistical Analysis
- Quote: "In the former case, we can only make an analysis of the opinion that, for example, most people hold. Only in the latter case, we can try to analyze about facts. But even then, we need to discuss in the threats to validity that the participants’ answers might be biased."
- Key point: If a question asks for opinions, you can only analyze opinions; only questions about facts the respondents experienced let you try to analyze facts, and even then you must discuss possible response bias under threats to validity.

### E15

- Location: §5.1 Descriptive Statistics
- Quote: "Ordinal data is what we often have in surveys where we can order the data but cannot clearly say if each point on the scale has the same distance to the next point." [...] "If we have clearly deﬁned distances, we have interval data. Only for the latter, we can employ the full range of statistical tests."
- Key point: Survey data are often ordinal: they can be ordered, but you cannot say the distances between adjacent points are equal (for example, Likert items); only interval data, with clearly defined distances, allow the full range of statistical tests.

### E16

- Location: §5.1 Descriptive Statistics
- Quote: "For the central tendency, we can safely use the mode, which is simply the most frequent answer, as well as the median" [...] "it is also quite easy to show the whole distribution of ordinal data in a stacked bar chart"
- Key point: For the central tendency of ordinal data you can safely use the mode and median; a stacked bar chart can also show the whole distribution.

### E17

- Location: §5.2 Null Hypothesis Signiﬁcance Testing
- Quote: "We used the rank test as we have ordinal data which breaks the assumptions of, for example, a t-test."
- Key point: The authors used a rank test (Wilcoxon signed-rank test) for ordinal data, because ordinal data break the assumptions of methods such as the t-test.

### E18

- Location: §5.2 Null Hypothesis Signiﬁcance Testing
- Quote: "Especially in survey research, it is rather easy to achieve large sample sizes. The larger the sample, the more likely we get signiﬁcant eﬀects. Then the eﬀect sizes can help us interpret the results."
- Key point: Surveys easily yield large samples, and the larger the sample, the more likely results are "significant," so report effect sizes to interpret the results.

### E19

- Location: §5.2 Null Hypothesis Signiﬁcance Testing
- Quote: "In such cases, it is unclear what the result of a NHST actually means. How can we generalize from non-representative data?"
- Key point: When the sample is not representative, it is unclear what a significance test result actually means.

### E20

- Location: §5.3 Alternative 1: Bootstrapping conﬁdence intervals
- Quote: "It is problematic for questions that have answers on an ordinal scale. We discussed above that for those, we should use the median instead of the mean. As, so far, there are no established methods for bootstrapping conﬁdence intervals for medians, we decided to work with the conﬁdence intervals of the means but report the medians alongside of them."
- Key point: Bootstrapping confidence intervals for ordinal items is problematic: the median should be used, but there was no established method for bootstrapping the median, so the authors used confidence intervals for the mean and also reported medians.

### E21

- Location: §6 Qualitative Analysis
- Quote: "The answers to such open questions can help researchers to further understand a phenomenon eventually including causal relations among theory constructs and theoretical explanations. Hence, open questions can help generating new theories." [...] "However, they can lead to a large amount of qualitative data to analyze, which is not easy and may require a signiﬁcant amount of resources."
- Key point: Open questions help researchers understand a phenomenon and generate new theory, but they produce large amounts of qualitative data that are hard to analyze and may require a lot of effort.

### E22

- Location: §6 Qualitative Analysis
- Quote: "given that we analyzed data from an anonymously conducted survey after the fact, we were not able to follow a constant comparison approach where we iterate between the data collection and the analysis. This also means that we were not able to validate our results with the participants"
- Key point: An anonymous survey analyzed after the fact does not allow iterating between data collection and analysis, or going back to participants to check the results.

### E23

- Location: §6, Take Aways
- Quote: "When reporting the qualitative analysis of your survey, explicitly state your research method, providing details on eventual deviations." [...] "To avoid researcher bias and improve the reliability of the results, qualitative analyses should be conducted in teams and make use of independent validations."
- Key point: When reporting the analysis of open questions, state the method and any deviations; qualitative analysis should be done by a team with independent checking to reduce researcher bias.

### E24

- Location: §6, Take Aways
- Quote: "A good strategy that helps to check if this goal is properly achieved involves piloting the survey and discussing it afterwards with the pilot participants to assure that questions were easily and correctly understood."
- Key point: Pilot the survey and discuss it afterward with the pilot participants to make sure the questions were understood easily and correctly.

### E25

- Location: §6 Qualitative Analysis
- Quote: "All translations were validated by piloting the survey with independent team members that were also native speakers."
- Key point: Every translation of a multilingual survey was validated by piloting with independent team members who were native speakers of that language.

### E26

- Location: §7 Issues when assessing psychological constructs
- Quote: "These constructs can only be assessed indirectly. We cannot take out a ruler to measure the motivation of people."
- Key point: Psychological constructs (such as satisfaction or motivation) can only be assessed indirectly; you cannot take out a ruler to measure them.

### E27

- Location: §7 Issues when assessing psychological constructs
- Quote: "whenever we wish to investigate psychological constructs and their variables, we need to either develop or adopt measurement instruments that are psychometrically validated."
- Key point: To study psychological constructs, you must either develop or adopt measurement instruments that are psychometrically validated.

### E28

- Location: §7.1
- Quote: "when the right test is adopted, most of the times the test items are modiﬁed towards the destruction of the test reliability and validity."
- Key point: Even when the right scale is adopted, its items are often modified in ways that destroy the scale's reliability and validity.

### E29

- Location: §7.2 Reliability and validity in psychometrics
- Quote: "Reliability can be seen either as the consistency of a questionnaire scores in repeated instances of it" [...] "internal-consistency (derived by computing the relationship between scores derived from individual test items during a single session)"
- Key point: Reliability is the consistency of questionnaire scores across repeated administrations; internal consistency looks at the relationships among item scores within a single administration.

### E30

- Location: §7.2 Reliability and validity in psychometrics
- Quote: "Validity in psychometrics is “the degree to which" [...] "evidence and theory support the interpretation of test scores for proposed uses of tests.”"
- Key point: In psychometrics, validity is the degree to which evidence and theory support interpreting test scores for their proposed uses.

### E31

- Location: §7.2 Reliability and validity in psychometrics
- Quote: "Diﬀerential validity assesses how scores of a test correlate with measures they should be related to, and how scores of a test do not correlate with measures they should not be related to."
- Key point: Differential validity checks whether scores correlate with measures they should be related to (convergent validity) and do not correlate with measures they should not be related to (discriminant validity).

### E32

- Location: §7.3 An experience report on adopting a psychometrically validated instrument
- Quote: "A big disadvantage in adopting psychometrically validated scales lies in the complete lack of ﬂexibility of the items, as it follows an “all or nothing” approach."
- Key point: The drawback of adopting validated scales is the complete lack of flexibility in the items: it is all or nothing.

### E33

- Location: §4 Invitation and Follow-Up
- Quote: "In that strategy, we need to deﬁne proper demographic questions that allow us to analyze the extent to which the respondents are eventually suitable to provide the required information" [...] "to remove those answers from the data set clearly unrelated to the target population"
- Key point: Open invitations require well-designed demographic questions to judge whether respondents are suited to provide the needed information, and to remove answers clearly outside the target population.
