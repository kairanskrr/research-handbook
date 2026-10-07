# 问卷调查：用问卷向大量人收集数据

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**问卷调查**（questionnaire survey）：设计一份以封闭式题目为主的问卷，发给一批人填写，再系统地分析回答。例如调查开发者怎样使用代码审查工具、安全工程师怎样处理漏洞报告；计算机以外，教育学调查教师怎样使用在线教学平台，也是同一类研究。

如果你要做的是一对一的开放式访谈，那是另一类研究（定性调查，或称访谈研究）[^ralph2020empirical-e256]，见[访谈研究](interview_study.md)。抽样的基本概念（总体、抽样框、样本、代表性）见通用篇[说清为什么选这些样本](../02_from-project-to-study/01_question-to-evidence.md#3-定下研究对象分析单元和总体)，涉及人的研究的一般伦理要求见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)，这里只讲问卷特有的部分。

**读完本文，你应该能：**

- 判断自己的问题适不适合用问卷回答，以及问卷回答不了什么；
- 定义总体、招募参与者，写出不诱导、不含糊的题目，并用适合定序数据的方法分析结果；最后用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准把它定义为：让一批受访者回答一系列（大多是结构化的）问题的研究，通常通过电子或纸质表单进行[^ralph2020empirical-e231]。参与者回答事先定好的、以封闭式为主的问题，研究者系统地分析这些回答[^ralph2020empirical-e232]。大规模问卷的意义，就在于牺牲一部分内部效度（结论在研究内部是否可靠，例如能否排除其他解释），换取外部效度（结论能否推广）[^baltes2022sampling-e20]，所以抽样做得好不好，直接决定一项问卷研究有没有价值 `[本项目分析]`。

**它能回答的问题**分三种[^ralph2020empirical-e234]：

- **描述性**：某个总体里，某种做法、工具、看法分布如何。关心的是"分布是什么"，不是"为什么"[^wagner2020challenges-e1]。例如"有多大比例的开发者在用某类工具"。
- **探索性**：为后续研究产生见解、假设或模型。
- **验证性**：检验事先提出的命题。这时最好有理论指导问卷设计[^wagner2020challenges-e2]。

**它回答不了什么，要心里有数：**

- **问卷是观察，不是干预。** 它不像实验那样主动施加并控制某个因素[^torchiano2017lessons-e1]，所以一般得不到因果结论。研究者常不自觉地把问卷数据当成实验数据，看到并不存在的因果关系[^torchiano2017lessons-e2]。
- **问看法，就只能得到看法。** "自动化测试比手工测试更有效吗？"问的是看法，结论只能是"多数人这样认为"；问亲身经历的事实（"你上个项目里哪种测试发现的缺陷更多"），才能尝试分析事实，而且仍要讨论回答可能有偏差[^wagner2020challenges-e14]。
- **不要问"应该怎么做"。** 问卷适合问"你那里在发生什么"和"为什么会这样"，不适合问规范性问题[^torchiano2017lessons-e3]。

**和相近类型的区别** `[本项目分析]`：

| | 问卷调查 | [访谈研究](interview_study.md) | [对照实验](controlled_experiment.md) | [仓库挖掘](../07_fields/computer-science/practices/repository_mining.md) |
|---|---|---|---|---|
| 数据 | 很多人对固定题目的回答 | 少数人的开放式谈话 | 控制条件下的测量 | 平台上留下的活动痕迹 |
| 擅长 | 分布、看法、自报的做法 | 理解"为什么"、发现新概念 | 因果关系 | 实际行为的大规模规律 |
| 主要弱点 | 只有自报；样本偏差 | 难以推广 | 场景脱离现实 | 看不到动机和看法 |

**怎么选** `[本项目分析]`：想知道"多少人、多普遍、大家怎么看"时用问卷；还不清楚该问什么时，先做几次访谈再设计问卷。问卷测到的是人们"说"自己怎么做，可以用工作仓库等其他数据来源交叉核对[^molleri2020empirically-e7]。这套做法主要来自软件工程，但人机交互、可用安全等方向以及其他学科的问卷研究同样适用 `[本项目分析]`。

---

## 2. 怎么做

### 第一步：从研究问题出发，定义总体、分析单元和抽样框

先写研究问题，再决定问谁、问什么。每道题都应能对应到某个研究目标，措辞和格式适合回答者[^ralph2020empirical-e240]；写不出"这道题回答哪个研究问题"的题，删掉 `[本项目分析]`。最常见的错误是先想"能找到谁来填"，再凑问题。选谁来填，要问"谁最能提供我需要的信息"，而不是"谁最可能有空"；回应率低比回答没用更好处理[^torchiano2017lessons-e4]。

1. **目标总体**：你想把结论推广到谁？例如"使用 Rust 的开源贡献者"，还是"全世界的专业开发者"[^wagner2020challenges-e3]？后者的规模和构成，多数情况下没人说得清[^wagner2020challenges-e4]，总体定得越具体，越容易论证样本像不像它。`[本项目分析]`
2. **分析单元**：统计的"一个"是一个人、一个团队，还是一个公司？随机抽一批开发者，和从随机抽到的一批公司里调查开发者，是两回事；分析单元选错，数据可能对研究问题毫无用处[^torchiano2017lessons-e5]。
3. **抽样框**：你实际能从中抽人的名单。软件工程研究很少有合适的抽样框[^torchiano2017lessons-e6]。看一个名单来源时，要问：它是否偏向收录某些子群？收录标准不一，各人被抽到的机会就不同[^torchiano2017lessons-e7]。

**容易错在哪**：只描述了回答者的人口学特征，却没交代目标总体是什么。一份汇总 14 篇方法论文献得到的检查清单[^molleri2020empirically-e1]，用来评估已发表的问卷论文时发现，"界定总体"是做得最少的几项之一[^molleri2020empirically-e5]：论文常描述了参与者的人口学特征，却很少交代目标总体[^molleri2020empirically-e6]。

### 第二步：抽样和招募

**先决定邀请方式**，它决定了你能报告什么[^wagner2020challenges-e11]：

- **封闭式邀请**：只邀请名单上的人，能准确算出回应率、控制谁来填，代价是回答数通常较少。可以用问卷工具给每个受邀者发唯一的访问码，防止邀请被随意转发[^torchiano2017lessons-e17]。
- **开放式邀请**：在邮件列表、论坛、社交媒体上发链接，传播更广，但你不知道谁看到了邀请，算不出回应率，还要额外比较回答者和目标总体的特征[^torchiano2017lessons-e16]。作者改用开放式邀请后，还遇到大量"点进来看一眼就走"的中途退出[^wagner2020challenges-e12]。

**估计要发多少份。** 参与率往往很低，通常不到 10%[^torchiano2017lessons-e8]；Wagner 等人的邮件邀请，回应率只有 2% 到 4%[^wagner2020challenges-e7]。按要拿到的回答数倒推发放量。作为参考，Wagner 等人估算，以开发者为总体时，400 份以上的回答、再加上检查过代表性，才能主张较强的可推广性，而多数问卷达不到[^wagner2020challenges-e6]。回答数还要足以支撑你计划的统计分析（统计功效，即有多大把握检测出预期的效应）[^ralph2020empirical-e238]。

**便利抽样的局限。** 在邮件列表、社交媒体上发链接，本质上是便利抽样（按方便拿到来选对象），会威胁可推广性[^baltes2022sampling-e2]。但这不是拒稿的理由，没采取可行的减偏措施才是[^baltes2022sampling-e21]。还要注意：

- 样本又大又广，可以支持"某种相关关系能推广"，但**不能支持具体比例**（"38% 的开发者使用 X"）[^baltes2022sampling-e17]。描述性问卷最想报告的恰恰是比例，所以要格外小心 `[本项目分析]`。抽样框本身有偏差时，样本再大也弥补不了[^baltes2022sampling-e5]。
- 可以考虑应答者驱动抽样（respondent-driven sampling，一种为减轻偏差而设计的进阶版滚雪球抽样，即让参与者推荐参与者）[^ralph2020empirical-e250]，但它也被批评给出的置信区间过于乐观[^baltes2022sampling-e18]。

**提高回应率、减轻回应偏差**（回应偏差：填了的人和没填的人系统性地不同）：

- 开头放能引起共鸣的重要问题，而不是人口学问题；避免矩阵题和必答题；发提醒；提供激励[^baltes2022sampling-e19]。
- 提醒：第一次提醒（通常在 4 到 8 天后）能明显提高回应率，第三次作用很小；不要提醒已经填过的人[^torchiano2017lessons-e20]。也可以在问卷关闭前约两周发一次跟进[^wagner2020challenges-e13]。
- 抽奖、报酬、分享结果等奖励能让积极性低的人也参与，避免只有热心人来填[^torchiano2017lessons-e19]。用了激励，要讨论它对自愿性和回应偏差的影响[^ralph2020empirical-e244]。

**发出之后**：持续看回应率，找出不回应的原因[^molleri2020empirically-e3]；事先想好对不回应和中途退出怎么应对，说明缺失数据怎么处理（插补、加权调整或丢弃）[^ralph2020empirical-e237]。开放式邀请要设计足够的背景题，用来判断回答者是否属于目标总体，并剔除明显不属于的回答[^wagner2020challenges-e33]。

> **调查工具使用情况时特别注意：邀请信里别点名工具。** 邀请信提到某个工具，不用它的人往往自行不参加，Torchiano 等人认为这会让采用率被低估[^torchiano2017lessons-e18]。按这个机制，填答者中用户比例偏高，采用率也可能被高估；不管偏向哪边，估计都会失真，所以邀请中不要点名 `[本项目分析]`。

### 第三步：设计题目

**措辞**[^torchiano2017lessons-e9]：

- 题目短，一题只问一个概念。避免"一题两问"（double-barrelled question），例如"你是否同意重构和代码异味检测都是必要的？"[^torchiano2017lessons-e10]——同意前半句、不同意后半句的人没法回答。
- 避免被动语态和双重否定。
- **不要诱导。** "你更喜欢敏捷项目，还是通常的非敏捷项目？"把非敏捷说成"通常的"，暗示了答案[^torchiano2017lessons-e11]。
- 问近期的事，不要让人回忆"最近十个项目"[^torchiano2017lessons-e13]。
- 敏感问题（所在公司、收入、对管理层的看法）可能让人退出；确实需要时，向回答者说明为什么要问[^torchiano2017lessons-e12]。

**选项**：李克特量表（Likert scale，"非常不同意"到"非常同意"的分级选项）适合测"是否同意某个说法"，但精度有限；用这类定序量表时，**每个选项都标上明确的文字**，不要只给"1 到 6"让人猜 4 和 5 有什么区别[^torchiano2017lessons-e14]。问经验、频率这类事实时，用有明确参照点的区间（"不到 1 年""1 到 3 年"……）更好[^torchiano2017lessons-e15]。

**整体**：仔细安排题目的顺序和数量[^molleri2020empirically-e7]。在线问卷可以加入注意力检查题（例如"本题请选'不同意'"），并设法识别用 AI 或自动程序作答的回答，排除这两类回答[^ralph2020empirical-e241]。

### 第四步：测量抽象概念时，用验证过的量表

工作满意度、动机、幸福感这类**构念**（construct，不能直接观察、只能通过一组题目间接测量的概念）没法拿尺子去量[^wagner2020challenges-e26]，要么开发、要么采用经过验证的测量工具[^wagner2020challenges-e27]。SIGSOFT 标准把"用（或改编）验证过的量表测量构念，或者事后分析构念效度"列为必要项[^ralph2020empirical-e236]。先分清两个概念：

- **信度**：得分是否稳定一致，例如重复施测时结果是否一致；内部一致性则看同一次作答中，测同一构念的几道题得分是否一致[^wagner2020challenges-e29]。所以同一个变量最好用不止一道题来测[^molleri2020empirically-e4]。
- **效度**：证据和理论在多大程度上支持你对得分的解读[^wagner2020challenges-e30]。例如得分应当与相关的测量相关、与无关的测量不相关[^wagner2020challenges-e31]。

**怎么做**：

1. **先找现成的量表。** 开发并验证一个量表可能要好几年[^graziotin2021psychometrics-e4]。
2. **原样使用，不要改题。** 改动题目常常破坏量表的信度和效度[^graziotin2021psychometrics-e1][^wagner2020challenges-e28]。代价是没有灵活性，只能全用或不用[^wagner2020challenges-e32]。确实需要改编时，要像 SIGSOFT 标准说的那样，事后分析构念效度[^ralph2020empirical-e236]。
3. **不要用一道自编的题测一个构念。** 有研究者自我检讨，早年用一道李克特题测"生产率"，这个量表没有验证过，削弱了结果的价值[^graziotin2021psychometrics-e2]。

### 第五步：预调查，然后改问卷

正式发放前，检查题目、版式、时长和技术是否合适。常用方法有预调查（pilot，先找少量目标人群试填）、重测、焦点小组、专家或非专家评审[^molleri2020empirically-e2][^ralph2020empirical-e242]。

- 试填后**和试填者聊一聊**，确认题目被轻松、正确地理解[^wagner2020challenges-e24]。多语言问卷，Wagner 等人请同为母语者的独立团队成员试填，检验每个译本[^wagner2020challenges-e25]。
- **记下改了什么，写进论文**[^molleri2020empirically-e8][^ralph2020empirical-e242]。
- 根据预调查反复改过的问卷，不能再用同一批预调查数据证明它有效 `[本项目分析]`，道理同通用篇[留一份数据只用于最后检验](../05_research-strategies/compare_evaluate.md#2-什么样的证据才够)。

### 第六步：分析封闭题

**先做描述统计。** 单选、多选题报告比例，用条形图展示。李克特题是**定序数据**：能排序，但不能确定相邻两档之间距离相等；只有距离明确的数据才能用全部统计检验[^wagner2020challenges-e15]。所以集中趋势用**众数和中位数**，用堆叠条形图展示每道题的完整分布[^wagner2020challenges-e16]；做检验时用秩检验（如 Wilcoxon 符号秩检验），因为定序数据不满足 t 检验等方法的假设[^wagner2020challenges-e17]。

**再看效应量和代表性。** 问卷容易拿到大样本，样本越大越容易"显著"，所以要报告效应量（差异或关联有多大）[^wagner2020challenges-e18]。样本没有代表性时，显著性检验到底说明了什么并不清楚[^wagner2020challenges-e19]。可以把自己样本的人口学分布和大型公开调查比较，估计代表性；但公开调查本身也有偏差，例如 Stack Overflow 年度调查只覆盖它的注册用户[^wagner2020challenges-e5]。显著性和效应量的一般讲法见通用篇[认真对待随机性和统计](../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

> **不同的看法：李克特数据能不能算平均数？**
> - **按定序数据处理**：Wagner 等人认为李克特题是定序数据，应当用中位数而不是平均数，检验用秩检验[^wagner2020challenges-e15][^wagner2020challenges-e17]。
> - **实际中常算平均数**：即便是 Wagner 等人，在用自助法估计置信区间时，也因为缺少成熟的中位数方法而改用平均数，同时报告中位数[^wagner2020challenges-e20]；心理测量中计算题目难易度时，也直接用李克特题的平均值[^graziotin2021psychometrics-e3]。
>
> 实际操作 `[本项目分析]`：主要结果报告中位数和完整分布（堆叠条形图）；确实要用平均数或基于平均数的方法时，说明理由，并同时给出分布，让读者自己判断。

### 第七步：分析开放题

开放题让回答者用自己的话描述，能帮助理解原因、发现新概念，但会产生大量需要人工分析的文字[^wagner2020challenges-e21]。以开放题为主的问卷不适用问卷调查标准[^ralph2020empirical-e233]，应按定性研究的要求来做 `[本项目分析]`。

- 用编码（给每段回答贴上概括其含义的标签，再归类）来分析，由团队完成并做独立核验，减少研究者偏差；写明用了什么方法，以及与原方法有哪些偏离[^wagner2020challenges-e23]。编码的具体做法见[访谈研究](interview_study.md#第五步编码和主题分析)。
- 匿名问卷是事后分析的，不能边收集边调整问题，也不能回头找参与者核实，这是它和访谈研究的重要区别[^wagner2020challenges-e22]。

### 第八步：伦理、知情同意和匿名

通用要求（风险、知情同意、隐私、伦理审查）见[科研诚信与伦理](../08_throughout/integrity_and_ethics.md)，这里只列问卷特有的几点。

- **别把公开邮箱当成招募名单。** 从 GitHub 提交记录里收集邮箱、群发未经请求的邀请，是常见但有伦理问题的做法[^wagner2020challenges-e8][^baltes2022sampling-e22]；按市场调查行业的伦理准则，用 GitHub 或 Stack Overflow 上的用户信息联系潜在参与者不合乎伦理[^wagner2020challenges-e9]。有作者这样做后收到了被打扰者的抱怨[^wagner2020challenges-e10]。他们当时写了一封简短、礼貌、由对方主动选择是否参加的邀请，同时充当知情同意书[^wagner2020challenges-e10]。新手应先问导师和伦理委员会。`[本项目分析]`
- **知情同意可以写在问卷首页。** 填写一份明确说明属于研究项目的问卷，可以视为同意，不一定需要单独的同意书[^ralph2020empirical-e254]。给了报酬的，要说明报酬，以及怎样避免强迫[^ralph2020empirical-e255]。
- **匿名不等于不可识别。** "公司 + 职位"这类背景信息拼起来，可能认出具体的人[^ralph2020empirical-e253]。背景题只问分析需要的，公开数据前检查组合起来是否能识别个人。`[本项目分析]`

### 第九步：报告

除了研究型论文的一般写法（见[写作](../04_write-and-publish/01_story-and-paper.md)），问卷论文要写清：

- 目标总体、抽样策略、招募方式（名单、广告、邀请、激励）[^ralph2020empirical-e235]；
- 回应率，以及为提高回应用了哪些办法[^ralph2020empirical-e238][^molleri2020empirically-e9]；
- 回答者和目标总体可能有什么不同[^ralph2020empirical-e239]；
- **附上完整问卷**[^ralph2020empirical-e240]，最好连同邀请信、编码手册、分析脚本和数据[^ralph2020empirical-e245][^molleri2020empirically-e10]；
- 区分有证据的结果和你的解读、推测，结果部分不写推测[^ralph2020empirical-e200]；
- 没有论证代表性，就不要对总体下结论[^ralph2020empirical-e251]。

---

## 3. 检查清单

主要依据 SIGSOFT 问卷调查标准，以及它的抽样和伦理补充标准。

**必须做到**

- [ ] 明确目标总体，定义抽样策略[^ralph2020empirical-e235]
- [ ] 说明问卷是怎样编制的，参与者是怎样选出或招募的[^ralph2020empirical-e235]
- [ ] 用验证过的量表测量构念，或事后分析构念效度[^ralph2020empirical-e236]
- [ ] 说明怎样监控回收、应对不回应和中途退出，怎样处理缺失数据[^ralph2020empirical-e237]
- [ ] 分析回应率；评估参与人数是否足够[^ralph2020empirical-e238]
- [ ] 讨论回答者可能和目标总体有什么不同[^ralph2020empirical-e239]
- [ ] 提供问卷原件；每道题对应研究目标，措辞适合回答者[^ralph2020empirical-e240]

**做到更好**

- [ ] 加入注意力检查题，识别并排除 AI 或自动程序生成的回答[^ralph2020empirical-e241]
- [ ] 用预调查、重测或专家评审检验问卷，报告问卷因此做了哪些修改[^ralph2020empirical-e242]
- [ ] 定量分析回应偏差；用激励、提醒、定向宣传提高回应率[^ralph2020empirical-e243]
- [ ] 用了激励时，讨论它对自愿性和回应偏差的影响[^ralph2020empirical-e244]
- [ ] 公开问卷、编码手册、分析脚本和数据；考虑知情同意和被重新识别的风险[^ralph2020empirical-e245]
- [ ] 区分有证据的结果和解读、推测[^ralph2020empirical-e200]
- [ ] 在线问卷用应答者驱动抽样，而不是简单的滚雪球抽样[^ralph2020empirical-e250]

**做得出色**

- [ ] 事先检查计划的分析方法是否可行；从维度、信度、效度三方面报告量表验证结果[^ralph2020empirical-e246]

**这些情况可以不做，不算缺陷**[^ralph2020empirical-e247]

- 因版权原因不公开部分题目（但要引用题目来源）；没有中途退出或缺失数据时，不必描述其处理

**审稿时常见、但不成立的批评**：你不必为此担心

- "公开链接的问卷没有报告回应率""数据敏感，却没有公开完整数据""只反映了人们的看法"；或者说"样本太小"，却不说明为什么不够回答研究问题[^ralph2020empirical-e248]
- "结果不出人意料"或"和我的经验不一致"[^ralph2020empirical-e249]
- 笼统地说"结果可能无法推广"，而不指出具体该做什么（例如本该发提醒）[^ralph2020empirical-e252]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 用问卷数据下因果结论 | 问卷不施加干预，容易看到并不存在的因果关系[^torchiano2017lessons-e2] |
| 只说"调查了 N 名开发者"，不交代目标总体 | 读者无法判断结论能推广到谁[^molleri2020empirically-e6][^ralph2020empirical-e251] |
| 在社交媒体上广撒网，又报告"38% 的开发者使用 X" | 便利样本支撑不了具体比例[^baltes2022sampling-e17] |
| 一题两问、诱导性措辞、双重否定 | 回答无法解读，或被引向某个答案[^torchiano2017lessons-e9][^torchiano2017lessons-e11] |
| 自编一道题测满意度、生产率，或改动现成量表 | 信度和效度都没有保证[^graziotin2021psychometrics-e1][^graziotin2021psychometrics-e2] |
| 李克特数据只报平均数，用 t 检验 | 定序数据不满足这些方法的假设[^wagner2020challenges-e17] |
| 从 GitHub 收集邮箱群发邀请 | 有伦理问题，还会招来抱怨[^wagner2020challenges-e9][^wagner2020challenges-e10] |

---

## 5. 延伸阅读

- **从头到尾的经验总结**：Torchiano 等人 2017，篇幅短，按"定目标、定总体、抽样、设计问卷、招募"讲常见陷阱，附大量正反例句。新手设计第一份问卷前最值得读。
- **抽样、邀请、统计分析和心理测量**：Wagner 等人 2020，基于多轮跨国问卷的经验，覆盖样本量估计、邀请方式、定序数据分析、开放题编码和量表使用。
- **检查清单**：Molléri 等人 2020，汇总 14 篇方法论文献，可以在设计阶段逐项对照，也可用来评审别人的问卷论文。
- **抽样**：Baltes & Ralph 2022，讲清代表性和随机性的区别，以及问卷研究中减轻抽样偏差的具体做法。
- **心理测量**：Graziotin 等人 2021，要自己开发量表或评估现成量表时读，包括题目分析、因子分析、信度和效度，附可运行的 R 示例。
- **经典指南**：Kitchenham & Pfleeger 的 *Personal Opinion Surveys*（2008）及其 2001–2002 年的系列文章常被引用，本文没有读到合法公开的全文，未作引用。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e231]: SIGSOFT 问卷调查标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e231)
[^ralph2020empirical-e232]: SIGSOFT 问卷调查标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e232)
[^ralph2020empirical-e233]: SIGSOFT 问卷调查标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e233)
[^ralph2020empirical-e234]: SIGSOFT 问卷调查标准，Variations。[证据](../../sources/notes/ralph2020empirical.md#e234)
[^ralph2020empirical-e235]: SIGSOFT 问卷调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e235)
[^ralph2020empirical-e236]: SIGSOFT 问卷调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e236)
[^ralph2020empirical-e237]: SIGSOFT 问卷调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e237)
[^ralph2020empirical-e238]: SIGSOFT 问卷调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e238)
[^ralph2020empirical-e239]: SIGSOFT 问卷调查标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e239)
[^ralph2020empirical-e240]: SIGSOFT 问卷调查标准，必要项及脚注 3。[证据](../../sources/notes/ralph2020empirical.md#e240)
[^ralph2020empirical-e241]: SIGSOFT 问卷调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e241)
[^ralph2020empirical-e242]: SIGSOFT 问卷调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e242)
[^ralph2020empirical-e243]: SIGSOFT 问卷调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e243)
[^ralph2020empirical-e244]: SIGSOFT 问卷调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e244)
[^ralph2020empirical-e200]: SIGSOFT 问卷调查标准，加分项及脚注 4。[证据](../../sources/notes/ralph2020empirical.md#e200)
[^ralph2020empirical-e245]: SIGSOFT 问卷调查标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e245)
[^ralph2020empirical-e246]: SIGSOFT 问卷调查标准，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e246)
[^ralph2020empirical-e247]: SIGSOFT 问卷调查标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e247)
[^ralph2020empirical-e248]: SIGSOFT 问卷调查标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e248)
[^ralph2020empirical-e249]: SIGSOFT 问卷调查标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e249)
[^ralph2020empirical-e250]: SIGSOFT 抽样补充标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e250)
[^ralph2020empirical-e251]: SIGSOFT 抽样补充标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e251)
[^ralph2020empirical-e252]: SIGSOFT 抽样补充标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e252)
[^ralph2020empirical-e253]: SIGSOFT 伦理补充标准（有人参与的研究），脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e253)
[^ralph2020empirical-e254]: SIGSOFT 伦理补充标准（有人参与的研究），不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e254)
[^ralph2020empirical-e255]: SIGSOFT 伦理补充标准（有人参与的研究），必要项。[证据](../../sources/notes/ralph2020empirical.md#e255)
[^ralph2020empirical-e256]: SIGSOFT 定性调查（访谈研究）标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e256)
[^wagner2020challenges-e1]: Wagner 等人 2020，§2。[证据](../../sources/notes/wagner2020challenges.md#e1)
[^wagner2020challenges-e2]: Wagner 等人 2020，§2 小结。[证据](../../sources/notes/wagner2020challenges.md#e2)
[^wagner2020challenges-e3]: Wagner 等人 2020，§3。[证据](../../sources/notes/wagner2020challenges.md#e3)
[^wagner2020challenges-e4]: Wagner 等人 2020，§3。[证据](../../sources/notes/wagner2020challenges.md#e4)
[^wagner2020challenges-e33]: Wagner 等人 2020，§4。[证据](../../sources/notes/wagner2020challenges.md#e33)
[^wagner2020challenges-e5]: Wagner 等人 2020，§3.1。[证据](../../sources/notes/wagner2020challenges.md#e5)
[^wagner2020challenges-e7]: Wagner 等人 2020，§3.2。[证据](../../sources/notes/wagner2020challenges.md#e7)
[^wagner2020challenges-e6]: Wagner 等人 2020，§3.2。[证据](../../sources/notes/wagner2020challenges.md#e6)
[^wagner2020challenges-e8]: Wagner 等人 2020，§3.3。[证据](../../sources/notes/wagner2020challenges.md#e8)
[^wagner2020challenges-e9]: Wagner 等人 2020，§3.3。[证据](../../sources/notes/wagner2020challenges.md#e9)
[^wagner2020challenges-e10]: Wagner 等人 2020，§3.3。[证据](../../sources/notes/wagner2020challenges.md#e10)
[^wagner2020challenges-e11]: Wagner 等人 2020，§4。[证据](../../sources/notes/wagner2020challenges.md#e11)
[^wagner2020challenges-e12]: Wagner 等人 2020，§4。[证据](../../sources/notes/wagner2020challenges.md#e12)
[^wagner2020challenges-e13]: Wagner 等人 2020，§4。[证据](../../sources/notes/wagner2020challenges.md#e13)
[^wagner2020challenges-e14]: Wagner 等人 2020，§5。[证据](../../sources/notes/wagner2020challenges.md#e14)
[^wagner2020challenges-e15]: Wagner 等人 2020，§5.1。[证据](../../sources/notes/wagner2020challenges.md#e15)
[^wagner2020challenges-e16]: Wagner 等人 2020，§5.1。[证据](../../sources/notes/wagner2020challenges.md#e16)
[^wagner2020challenges-e17]: Wagner 等人 2020，§5.2。[证据](../../sources/notes/wagner2020challenges.md#e17)
[^wagner2020challenges-e18]: Wagner 等人 2020，§5.2。[证据](../../sources/notes/wagner2020challenges.md#e18)
[^wagner2020challenges-e19]: Wagner 等人 2020，§5.2。[证据](../../sources/notes/wagner2020challenges.md#e19)
[^wagner2020challenges-e20]: Wagner 等人 2020，§5.3。[证据](../../sources/notes/wagner2020challenges.md#e20)
[^wagner2020challenges-e21]: Wagner 等人 2020，§6。[证据](../../sources/notes/wagner2020challenges.md#e21)
[^wagner2020challenges-e22]: Wagner 等人 2020，§6。[证据](../../sources/notes/wagner2020challenges.md#e22)
[^wagner2020challenges-e23]: Wagner 等人 2020，§6 小结。[证据](../../sources/notes/wagner2020challenges.md#e23)
[^wagner2020challenges-e24]: Wagner 等人 2020，§6 小结。[证据](../../sources/notes/wagner2020challenges.md#e24)
[^wagner2020challenges-e25]: Wagner 等人 2020，§6。[证据](../../sources/notes/wagner2020challenges.md#e25)
[^wagner2020challenges-e26]: Wagner 等人 2020，§7。[证据](../../sources/notes/wagner2020challenges.md#e26)
[^wagner2020challenges-e27]: Wagner 等人 2020，§7。[证据](../../sources/notes/wagner2020challenges.md#e27)
[^wagner2020challenges-e28]: Wagner 等人 2020，§7.1。[证据](../../sources/notes/wagner2020challenges.md#e28)
[^wagner2020challenges-e29]: Wagner 等人 2020，§7.2。[证据](../../sources/notes/wagner2020challenges.md#e29)
[^wagner2020challenges-e30]: Wagner 等人 2020，§7.2。[证据](../../sources/notes/wagner2020challenges.md#e30)
[^wagner2020challenges-e31]: Wagner 等人 2020，§7.2。[证据](../../sources/notes/wagner2020challenges.md#e31)
[^wagner2020challenges-e32]: Wagner 等人 2020，§7.3。[证据](../../sources/notes/wagner2020challenges.md#e32)
[^torchiano2017lessons-e1]: Torchiano 等人 2017，§II。[证据](../../sources/notes/torchiano2017lessons.md#e1)
[^torchiano2017lessons-e2]: Torchiano 等人 2017，§III-A-1。[证据](../../sources/notes/torchiano2017lessons.md#e2)
[^torchiano2017lessons-e3]: Torchiano 等人 2017，§III-A-1。[证据](../../sources/notes/torchiano2017lessons.md#e3)
[^torchiano2017lessons-e4]: Torchiano 等人 2017，§III-A-2。[证据](../../sources/notes/torchiano2017lessons.md#e4)
[^torchiano2017lessons-e5]: Torchiano 等人 2017，§III-B-1。[证据](../../sources/notes/torchiano2017lessons.md#e5)
[^torchiano2017lessons-e6]: Torchiano 等人 2017，§III-C。[证据](../../sources/notes/torchiano2017lessons.md#e6)
[^torchiano2017lessons-e7]: Torchiano 等人 2017，§III-C。[证据](../../sources/notes/torchiano2017lessons.md#e7)
[^torchiano2017lessons-e8]: Torchiano 等人 2017，§III-C。[证据](../../sources/notes/torchiano2017lessons.md#e8)
[^torchiano2017lessons-e9]: Torchiano 等人 2017，§III-D-1。[证据](../../sources/notes/torchiano2017lessons.md#e9)
[^torchiano2017lessons-e10]: Torchiano 等人 2017，§III-D-1。[证据](../../sources/notes/torchiano2017lessons.md#e10)
[^torchiano2017lessons-e11]: Torchiano 等人 2017，§III-D-2。[证据](../../sources/notes/torchiano2017lessons.md#e11)
[^torchiano2017lessons-e12]: Torchiano 等人 2017，§III-D-2。[证据](../../sources/notes/torchiano2017lessons.md#e12)
[^torchiano2017lessons-e13]: Torchiano 等人 2017，§III-D-3。[证据](../../sources/notes/torchiano2017lessons.md#e13)
[^torchiano2017lessons-e14]: Torchiano 等人 2017，§III-D-4。[证据](../../sources/notes/torchiano2017lessons.md#e14)
[^torchiano2017lessons-e15]: Torchiano 等人 2017，§III-D-4。[证据](../../sources/notes/torchiano2017lessons.md#e15)
[^torchiano2017lessons-e16]: Torchiano 等人 2017，§III-E-1。[证据](../../sources/notes/torchiano2017lessons.md#e16)
[^torchiano2017lessons-e17]: Torchiano 等人 2017，§III-E-1。[证据](../../sources/notes/torchiano2017lessons.md#e17)
[^torchiano2017lessons-e18]: Torchiano 等人 2017，§III-E-2。[证据](../../sources/notes/torchiano2017lessons.md#e18)
[^torchiano2017lessons-e19]: Torchiano 等人 2017，§III-E-2。[证据](../../sources/notes/torchiano2017lessons.md#e19)
[^torchiano2017lessons-e20]: Torchiano 等人 2017，§III-E-2。[证据](../../sources/notes/torchiano2017lessons.md#e20)
[^baltes2022sampling-e2]: Baltes & Ralph 2022，§2.1.1。[证据](../../sources/notes/baltes2022sampling.md#e2)
[^baltes2022sampling-e5]: Baltes & Ralph 2022，§2.6。[证据](../../sources/notes/baltes2022sampling.md#e5)
[^baltes2022sampling-e17]: Baltes & Ralph 2022，§2.6。[证据](../../sources/notes/baltes2022sampling.md#e17)
[^baltes2022sampling-e18]: Baltes & Ralph 2022，§2.1.4。[证据](../../sources/notes/baltes2022sampling.md#e18)
[^baltes2022sampling-e19]: Baltes & Ralph 2022，§6.2。[证据](../../sources/notes/baltes2022sampling.md#e19)
[^baltes2022sampling-e20]: Baltes & Ralph 2022，§6.3。[证据](../../sources/notes/baltes2022sampling.md#e20)
[^baltes2022sampling-e21]: Baltes & Ralph 2022，§6.3。[证据](../../sources/notes/baltes2022sampling.md#e21)
[^baltes2022sampling-e22]: Baltes & Ralph 2022，§7。[证据](../../sources/notes/baltes2022sampling.md#e22)
[^molleri2020empirically-e1]: Molléri 等人 2020，摘要。[证据](../../sources/notes/molleri2020empirically.md#e1)
[^molleri2020empirically-e2]: Molléri 等人 2020，§2。[证据](../../sources/notes/molleri2020empirically.md#e2)
[^molleri2020empirically-e3]: Molléri 等人 2020，§2。[证据](../../sources/notes/molleri2020empirically.md#e3)
[^molleri2020empirically-e4]: Molléri 等人 2020，§2。[证据](../../sources/notes/molleri2020empirically.md#e4)
[^molleri2020empirically-e5]: Molléri 等人 2020，§3.3.1。[证据](../../sources/notes/molleri2020empirically.md#e5)
[^molleri2020empirically-e6]: Molléri 等人 2020，§4.2.1。[证据](../../sources/notes/molleri2020empirically.md#e6)
[^molleri2020empirically-e7]: Molléri 等人 2020，§4.2.1。[证据](../../sources/notes/molleri2020empirically.md#e7)
[^molleri2020empirically-e8]: Molléri 等人 2020，§4.2.1。[证据](../../sources/notes/molleri2020empirically.md#e8)
[^molleri2020empirically-e9]: Molléri 等人 2020，§4.2.1。[证据](../../sources/notes/molleri2020empirically.md#e9)
[^molleri2020empirically-e10]: Molléri 等人 2020，§3.3.2。[证据](../../sources/notes/molleri2020empirically.md#e10)
[^graziotin2021psychometrics-e1]: Graziotin 等人 2021，§1.1。[证据](../../sources/notes/graziotin2021psychometrics.md#e1)
[^graziotin2021psychometrics-e2]: Graziotin 等人 2021，§1.1。[证据](../../sources/notes/graziotin2021psychometrics.md#e2)
[^graziotin2021psychometrics-e3]: Graziotin 等人 2021，§6.0.1。[证据](../../sources/notes/graziotin2021psychometrics.md#e3)
[^graziotin2021psychometrics-e4]: Graziotin 等人 2021，§13。[证据](../../sources/notes/graziotin2021psychometrics.md#e4)
