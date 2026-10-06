# Wagner 等人 2020：Challenges in Survey Research

- 资料：`wagner2020challenges`，[arXiv:1908.05899](https://arxiv.org/abs/1908.05899)
- 版本：arXiv v4（2020-04-27），收录于 *Contemporary Empirical Methods in Software Engineering*（Springer 2020）第 93–125 页

### E1

- 位置：§2 Survey Research and Theory Building
- 原文："Descriptive surveys can be conducted to enable assertions about some population like the distribution of certain attributes (e.g., usage of requirements elicitation techniques). The concern is not why the observed distribution exists, but instead what that distribution is."
- 要点：描述性调查用来对总体下断言，例如某些属性的分布（如各种需求获取技术的使用情况）；关心的是分布是什么，而不是为什么。

### E2

- 位置：§2，Take Aways
- 原文："Theories are of high value to guide the design of surveys."
- 要点：理论对指导问卷设计很有价值。

### E3

- 位置：§3 Issues in Sampling
- 原文："At the beginning of any design of survey research, we should clarify what the target population is that we try to characterize and generalize to."
- 要点：设计问卷调查的第一步，是说清要描述和推广到的目标总体。

### E4

- 位置：§3 Issues in Sampling
- 原文："This brings us, however, to the problem that in most cases, we have no solid understanding about the target population."
- 要点：多数情况下，我们对目标总体（例如全世界的开发者）并没有可靠的了解。

### E5

- 位置：§3.1 Representativeness
- 原文："They have the bias that only people registered at Stack Overﬂow can be sampled." [...] "Then, we can compare the distributions in our survey and the larger surveys to estimate representativeness."
- 要点：可以把自己样本的人口学分布与大型公开调查（如 Stack Overflow 年度开发者调查，它本身只覆盖注册用户）比较，估计代表性。

### E6

- 位置：§3.2 Sample Size Estimation
- 原文："So, for most intents and purposes, with a sample size of more than 400, we could claim a strong generalizability given that we also checked the representativeness as described above. Of course, most survey will fall short of this."
- 要点：按 Yamane 公式，以全球约 2300 万开发者计，400 份以上的样本、再加上检查过代表性，可以主张较强的可推广性；多数调查达不到。

### E7

- 位置：§3.2 Sample Size Estimation
- 原文："From the studies we could estimate that roughly 98% of the e-mails were delivered, and that the response rate was rather low, between 2% and 4%."
- 要点：作者向 GitHub 开发者发邮件的预调查中，回应率只有 2% 到 4%。

### E8

- 位置：§3.3 Ethics
- 原文："Baltes & Diehl (2016) discuss that the common practice of sending unsolicited e-mails to GitHub developers could be ethically problematic."
- 要点：给 GitHub 开发者群发未经请求的邮件，这种常见做法可能有伦理问题。

### E9

- 位置：§3.3 Ethics
- 原文："The Insight Association provides ethical guidelines that consider unethical sampling, among other practices" [...] "Hence, using GitHub or Stack Overﬂow information of users would not be an ethical way to contact potential survey participants."
- 要点：按市场调查行业的伦理准则，用 GitHub 或 Stack Overflow 上的用户信息联系潜在参与者，不是合乎伦理的方式。

### E10

- 位置：§3.3 Ethics
- 原文："All we could do was to design a short and cordial invitation e-mail that, besides acting as informed consent form including ethical and privacy considerations, was of opt-in nature." [...] "receiving feedback from potential participants who were annoyed by this."
- 要点：作者的做法：写一封简短、礼貌、需要对方主动选择参加的邀请邮件，同时充当包含伦理和隐私说明的知情同意书；但仍收到了被打扰者的抱怨。

### E11

- 位置：§4 Invitation and Follow-Up
- 原文："it also allows to accurately calculate the response rate and control the participation along the data collection" [...] "This increase of control by inviting subjects individually typically comes at the cost of a lower number of total responses." [...] "but it also comes at the cost of control in who provides the responses"
- 要点：封闭式邀请（只邀请特定的人）能准确计算回应率、控制参与，代价是回答总数通常较少；开放式邀请（任何拿到链接的人都能填）传播更广，但失去了对"谁在回答"的控制。

### E12

- 位置：§4 Invitation and Follow-Up
- 原文："At the same time, we were not able to calculate the response rate and also noticed a signiﬁcant drop-out rate (i.e. participants entering the survey out of curiosity and dropping out on the ﬁrst survey page already)."
- 要点：改为开放式邀请后，作者无法计算回应率，还出现大量中途退出（出于好奇点进来、在第一页就离开）。

### E13

- 位置：§4 Invitation and Follow-Up
- 原文："In both surveys, we therefore implemented a follow-up invitation roughly two weeks before closing the survey."
- 要点：作者在问卷关闭前约两周发一次跟进提醒。

### E14

- 位置：§5 Alternative Approaches for Statistical Analysis
- 原文："In the former case, we can only make an analysis of the opinion that, for example, most people hold. Only in the latter case, we can try to analyze about facts. But even then, we need to discuss in the threats to validity that the participants’ answers might be biased."
- 要点：问卷问的是看法，就只能分析看法；问的是亲身经历的事实，才能尝试分析事实，而且仍要在效度威胁中讨论回答可能有偏差。

### E15

- 位置：§5.1 Descriptive Statistics
- 原文："Ordinal data is what we often have in surveys where we can order the data but cannot clearly say if each point on the scale has the same distance to the next point." [...] "If we have clearly deﬁned distances, we have interval data. Only for the latter, we can employ the full range of statistical tests."
- 要点：问卷数据常是定序数据：能排序，但不能确定相邻两档之间距离相等（例如李克特题）；只有距离明确的定距数据才能用全部统计检验。

### E16

- 位置：§5.1 Descriptive Statistics
- 原文："For the central tendency, we can safely use the mode, which is simply the most frequent answer, as well as the median" [...] "it is also quite easy to show the whole distribution of ordinal data in a stacked bar chart"
- 要点：定序数据的集中趋势可以放心用众数和中位数；也可以用堆叠条形图展示完整分布。

### E17

- 位置：§5.2 Null Hypothesis Signiﬁcance Testing
- 原文："We used the rank test as we have ordinal data which breaks the assumptions of, for example, a t-test."
- 要点：作者对定序数据用秩检验（Wilcoxon 符号秩检验），因为定序数据不满足 t 检验等方法的假设。

### E18

- 位置：§5.2 Null Hypothesis Signiﬁcance Testing
- 原文："Especially in survey research, it is rather easy to achieve large sample sizes. The larger the sample, the more likely we get signiﬁcant eﬀects. Then the eﬀect sizes can help us interpret the results."
- 要点：问卷调查容易拿到大样本，样本越大越容易"显著"，所以要报告效应量来解释结果。

### E19

- 位置：§5.2 Null Hypothesis Signiﬁcance Testing
- 原文："In such cases, it is unclear what the result of a NHST actually means. How can we generalize from non-representative data?"
- 要点：样本没有代表性时，显著性检验的结果意味着什么并不清楚。

### E20

- 位置：§5.3 Alternative 1: Bootstrapping conﬁdence intervals
- 原文："It is problematic for questions that have answers on an ordinal scale. We discussed above that for those, we should use the median instead of the mean. As, so far, there are no established methods for bootstrapping conﬁdence intervals for medians, we decided to work with the conﬁdence intervals of the means but report the medians alongside of them."
- 要点：对定序题用自助法（bootstrapping）估计置信区间有问题：本应用中位数，但当时没有成熟的中位数自助法，作者改用均值的置信区间，同时报告中位数。

### E21

- 位置：§6 Qualitative Analysis
- 原文："The answers to such open questions can help researchers to further understand a phenomenon eventually including causal relations among theory constructs and theoretical explanations. Hence, open questions can help generating new theories." [...] "However, they can lead to a large amount of qualitative data to analyze, which is not easy and may require a signiﬁcant amount of resources."
- 要点：开放式问题能帮助理解现象、产生新理论，但会产生大量定性数据，分析不容易，可能需要大量投入。

### E22

- 位置：§6 Qualitative Analysis
- 原文："given that we analyzed data from an anonymously conducted survey after the fact, we were not able to follow a constant comparison approach where we iterate between the data collection and the analysis. This also means that we were not able to validate our results with the participants"
- 要点：匿名问卷是事后分析的，不能在收集和分析之间来回迭代，也不能找参与者核实结果。

### E23

- 位置：§6，Take Aways
- 原文："When reporting the qualitative analysis of your survey, explicitly state your research method, providing details on eventual deviations." [...] "To avoid researcher bias and improve the reliability of the results, qualitative analyses should be conducted in teams and make use of independent validations."
- 要点：报告开放题分析时写明方法和偏离之处；定性分析应由团队完成并做独立核验，以减少研究者偏差。

### E24

- 位置：§6，Take Aways
- 原文："A good strategy that helps to check if this goal is properly achieved involves piloting the survey and discussing it afterwards with the pilot participants to assure that questions were easily and correctly understood."
- 要点：做预调查，事后与预调查参与者讨论，确认题目被轻松、正确地理解。

### E25

- 位置：§6 Qualitative Analysis
- 原文："All translations were validated by piloting the survey with independent team members that were also native speakers."
- 要点：多语言问卷的所有译本，都由母语为该语言的独立团队成员通过预调查检验。

### E26

- 位置：§7 Issues when assessing psychological constructs
- 原文："These constructs can only be assessed indirectly. We cannot take out a ruler to measure the motivation of people."
- 要点：心理构念（如满意度、动机）只能间接测量，没法拿尺子去量。

### E27

- 位置：§7 Issues when assessing psychological constructs
- 原文："whenever we wish to investigate psychological constructs and their variables, we need to either develop or adopt measurement instruments that are psychometrically validated."
- 要点：研究心理构念时，要么开发、要么采用经过心理测量学验证的测量工具。

### E28

- 位置：§7.1
- 原文："when the right test is adopted, most of the times the test items are modiﬁed towards the destruction of the test reliability and validity."
- 要点：即使选对了量表，题目也常被改动，破坏了量表的信度和效度。

### E29

- 位置：§7.2 Reliability and validity in psychometrics
- 原文："Reliability can be seen either as the consistency of a questionnaire scores in repeated instances of it" [...] "internal-consistency (derived by computing the relationship between scores derived from individual test items during a single session)"
- 要点：信度指问卷得分在重复施测时的一致性；其中内部一致性是看同一次作答中各题得分之间的关系。

### E30

- 位置：§7.2 Reliability and validity in psychometrics
- 原文："Validity in psychometrics is “the degree to which" [...] "evidence and theory support the interpretation of test scores for proposed uses of tests.”"
- 要点：心理测量学中的效度，是证据和理论在多大程度上支持按预定用途解读得分。

### E31

- 位置：§7.2 Reliability and validity in psychometrics
- 原文："Diﬀerential validity assesses how scores of a test correlate with measures they should be related to, and how scores of a test do not correlate with measures they should not be related to."
- 要点：区分性效度看得分是否与应当相关的测量相关（聚合效度），且与不应相关的测量不相关（区分效度）。

### E32

- 位置：§7.3 An experience report on adopting a psychometrically validated instrument
- 原文："A big disadvantage in adopting psychometrically validated scales lies in the complete lack of ﬂexibility of the items, as it follows an “all or nothing” approach."
- 要点：采用验证过的量表的缺点是完全不能灵活修改题目，只能全用或不用。

### E33

- 位置：§4 Invitation and Follow-Up
- 原文："In that strategy, we need to deﬁne proper demographic questions that allow us to analyze the extent to which the respondents are eventually suitable to provide the required information" [...] "to remove those answers from the data set clearly unrelated to the target population"
- 要点：开放式邀请需要设计合适的背景题，判断回答者是否适合提供所需信息，并从数据中剔除明显不属于目标总体的回答。
