# 解释因果

> 本篇的道理适用于各学科，例子和具体做法以计算机为例；其他学科怎么做，见第 5 节的链接。

你发现了一个现象，想知道**为什么**会这样，或者**改变某个因素，结果会不会跟着变**。这就是"解释因果"这种研究套路。它最容易出问题的地方，是把"两件事一起出现"当成"一件事导致另一件"。本篇讲这类研究要证明什么、什么证据才够、该用哪些方法，以及它会怎样影响你的整个项目。

---

## 1. 这类研究产生什么知识

**它回答"X 会不会导致 Y""为什么会这样"。** 例如核心主张是：

> "给大模型提供漏洞模式提示，会提高它对重入漏洞的检出率。"

这句话说的不是"提示和检出率有关系"，而是"**改变提示，检出率就会跟着变**"。

先分清你问的是哪一类问题。关系问题问"X 和 Y 有没有关系""X 出现时 Y 是否也出现"[^easterbrook2008selecting-e35]；因果问题问"X 是否导致 Y""X 是否防止 Y"[^easterbrook2008selecting-e57]。因果问题还有两种更细的问法：比较两个原因哪个作用更大（"X 是否比 Z 导致更多 Y"），以及看情境怎样改变因果关系[^easterbrook2008selecting-e58]。

用同一个方向举例 `[本项目分析]`：

| 问题类型 | 例子 | 属于哪种套路 |
|---|---|---|
| 关系问题 | "合约越长，大模型漏报越多吗？" | 观察描述 |
| 因果问题 | "加上漏洞模式提示，会提高检出率吗？" | 解释因果 |
| 两个原因比大小 | "漏洞模式提示和几个示例，哪个更能提高检出率？" | 解释因果 |
| 情境怎样改变因果 | "提示只对短合约有用，对长合约没用吗？" | 解释因果 |

**和相邻套路的区别** `[本项目分析]`：

- **[比较评估](compare_evaluate.md)**问"工具 A 和 B 哪个更好"，把每个工具当成一个整体，不追问好在哪里；**解释因果**要找出是哪一个因素起了作用。两者的界线，比较评估一篇也讲了。
- **[构建改进](build_improve.md)**的核心主张是"新方法更好"；它常常带着一个解释因果的次要主张："好处来自组件 C"。这个次要主张，要用本篇的标准来检验。
- **[观察描述](observe_describe.md)**可以发现"有漏洞模式提示的项目检出率更高"，但只凭观察，还不能说是提示导致的（见第 2 节）。

**两种因果知识。** 一种是**效应**：改变 X，Y 变多少。另一种是**机制**：X 是通过什么过程影响 Y 的。两者需要的证据不同 `[本项目分析]`。政治学的案例研究方法文献就指出：其他条件相同时，案例研究更容易揭示因果机制，不太能估计真实的因果效应[^gerring2004case-e4]。先想清楚你的主张是哪一种。

**写下来：** 把你的核心主张写成"在条件 C 下，改变 X 会让 Y 怎样变化"。再写一句：你要证明的是效应、机制，还是两者都要？

## 2. 什么样的证据才够

**相关不等于因果。** 把相关当成因果是常见错误；证明因果一般比证明相关难得多[^easterbrook2008selecting-e36]。X 和 Y 一起变高，可能是 X 导致 Y，可能是 Y 导致 X，可能两者有共同的原因，也可能它们以复杂的方式一起演变[^easterbrook2008selecting-e56]。

例如，你在公开记录里发现：用了漏洞模式提示的审计，检出率更高。可能是提示起了作用；也可能是更有经验的审计员更爱用提示，真正起作用的是经验 `[本项目分析]`。

**软件工程的标准：说"导致"之前，要有四样东西。** ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准，在数据科学研究的部分把这种做法列为反面模式：不但要确立共变和先后顺序，还要排除第三变量的解释、至少提出一个产生机制的假设，做不到这些就声称因果[^ralph2020empirical-e203]。这是软件工程的标准；做计算机其他方向的因果研究，也可以拿它当检查清单。对照到例子上 `[本项目分析]`：

| 要有什么 | 意思 | 在例子里 |
|---|---|---|
| 共变 | X 变，Y 也变 | 有提示和没提示时，检出率不同 |
| 先后 | X 在 Y 之前 | 提示是在模型输出之前给的 |
| 排除其他解释 | 不是别的因素造成的 | 不是因为提示更长、换了模型版本、或合约被模型"见过" |
| 机制假设 | 说得出 X 怎样影响 Y | 提示让模型去检查"外部调用后才更新状态"这类代码 |

### 最有力的办法：自己改变 X

如果能，就**亲手改变 X，其他一切保持不变**，看 Y 怎么变。这就是对照实验。它能精确确定变量之间的关系，尤其是有没有因果关系[^easterbrook2008selecting-e60]。关键是控制：自变量（你主动改变的因素）以外的变量，不能影响实验[^easterbrook2008selecting-e61]。软件工程里评估工具、有人参与的实验，就是让每个参与者拿到完全一样的材料、说明、任务和环境，只有用哪个工具不同；这样结果有差异时，才能有力地说是工具造成的[^ko2015practical-e3]。

实验对象是人，或者别的无法做到完全相同的单位时，还要**随机分组** `[本项目分析]`。医学临床试验的报告规范 CONSORT 在解释文章里写道：随机分配做得正确时，能消除分组时的选择偏倚，让已知和未知的预后因素在组间均衡[^hopewell2025consortee-e1]。没有随机分组的准实验不如真实验有力，解释结果时要更小心[^easterbrook2008selecting-e64]。

用大模型做实验时，"其他一切保持不变"可以做得很具体 `[本项目分析]`：同一个模型版本、同一批合约、同样的生成参数，每种提示多跑几次；只有"有没有漏洞模式提示"这一处不同。

### 改变不了 X 时：先说清凭什么能作因果解释

很多因素你没法、也不该去操纵，比如开发者的经验、一项政策。这时只能用观察数据，但要**明确写出凭什么能作因果解释** `[本项目分析]`。经济学和流行病学在这方面写得最具体，可以借鉴：

- **经济学**讲"以研究设计为本"：借助真实实验或自然实验，并花大力气论证结果为什么可以作因果解释[^angrist2010credibility-e1]。例如用工具变量（一个只通过 X 影响 Y、取值近似随机的因素）时，要实实在在地论证它成立的假设，不能只给变量贴上标签[^angrist2010credibility-e5]。
- **流行病学**讲**目标试验**：用观察数据做因果推断，可以看作在模拟一项能回答这个问题的随机试验[^hernan2016target-e1]。流行病学教材还强调，只凭统计上的关联标准，判断不了什么是混杂因素（同时影响 X 和 Y、会造成假象的因素）；从观察数据做因果推断，需要事先的因果知识[^hernan2020whatif-e6][^hernan2020whatif-e7]。不知道的混杂因素，可以用敏感性分析估计它可能带来多大偏差[^hernan2020whatif-e11]。

### 主动排除其他解释

**事先列出所有说得通的其他解释，再逐个看证据支持谁。** 政治学的过程追踪方法文献点过这个毛病：有的案例研究给自己偏爱的解释"先手优势"；更好的做法是事先写出各种解释分别预言能看到什么，再逐一对照支持和反对的证据[^bennett2012process-e29]。同一份文献还强调，证据能不能区分相互竞争的解释，比证据的条数更重要[^bennett2012process-e9]。

在例子里，"提示让检出率提高"至少有这几个对手 `[本项目分析]`：

| 其他解释 | 怎样排除 |
|---|---|
| 提示只是让输入变长了 | 加一组同样长度、内容无关的提示 |
| 模型见过这些合约，提示只是唤起了记忆 | 用模型训练截止之后才出现的合约再做一次 |
| 提示让模型更爱报漏洞，误报也一起变多 | 同时报告误报，不只报检出率 |
| 只是偶然 | 多次运行，报告波动 |

### 检验机制

光有效应，读者还会问"为什么"。至少要提出一个机制假设[^ralph2020empirical-e203]，最好再去检验它。例如：如果提示真是让模型去查"外部调用后才更新状态"，那么换成一个**无关漏洞类型**的提示，检出率就不该同样提高；模型的解释里也应该提到这个模式 `[本项目分析]`。过程追踪的方法文献把研究机制的核心挑战说成避免"偷懒的机制式讲故事"[^bennett2012process-e50]；落到操作上，就是不要只讲一个听上去合理的过程，却不拿证据检验它 `[本项目分析]`。

### 计算机里的常用工具：消融实验

**消融实验**（ablation study）就是把方法里的组成部分逐个去掉，看效果怎么变。它是"改变一处、其他不变"在系统内部的用法 `[本项目分析]`。机器学习论文里，一次提出很多改动却不做消融，就看不出提升从哪里来，有时真正起作用的只有其中一处[^lipton2019troubling-e4]。所以不要只问"效果有多好"，还要问"什么起了作用、为什么"[^lipton2019troubling-e7]。

但消融对理解一个方法既不是必需的，也不一定够；计算资源有限时，可能根本做不了[^lipton2019troubling-e6]。另外，消融只告诉你在这个评测集、这个设置下哪一处起了作用，换个设置不一定还成立 `[本项目分析]`。

> **不同的看法：实验室实验，还是真实项目？**
>
> 软件工程的方法文献用一场争论写出了这个分歧：一方说，证明 A 导致 B 唯一确定的办法，是在受控环境中改变 A、测量 B；另一方说，实验室实验没用，因为它忽略了真实软件项目的复杂[^easterbrook2008selecting-e59]。
>
> - **支持受控实验的理由**：对照实验能精确确定变量之间有没有因果关系[^easterbrook2008selecting-e60]；其他条件完全一样时，结果的差异才能有力地归到被改变的那个因素上[^ko2015practical-e3]。
> - **支持真实项目的理由**：实验把问题拆小，这种简化可能掩盖关键的交互作用；实验支持了假设，也只说明在你定义的指标下成立[^easterbrook2008selecting-e62]。环境本身会影响现象（比如真实项目的压力影响开发者行为），或者效果要几周、几个月才显现时，拆小、隔离的做法就不合适[^easterbrook2008selecting-e16]。
>
> 实际操作 `[本项目分析]`：能做受控实验就做，但主张的范围要和实验条件一致；如果你关心的效应依赖真实环境，用第 3 节的案例研究、过程追踪等方法补上。

**写下来：** 对照上面的四样东西，逐项写出你打算用什么证据满足它。再列出至少三个其他解释，写出各自怎样排除。

## 3. 常用的研究方法

套路说"要证明 X 导致 Y"，方法说"用什么手段拿到证据"。下表按"能不能改变 X"来选 `[本项目分析]`：

| 你的情形 | 可以用的方法 | 它怎样提供因果证据 |
|---|---|---|
| 能改变 X，对象是软件系统或模型 | 系统上的受控实验、消融，见[基准评测](../07_fields/computer-science/practices/benchmarking.md)、[工程研究](../07_fields/computer-science/practices/engineering_research.md) | 只改一处，其他完全相同，多次运行 |
| 能改变 X，对象是人 | [对照实验](../06_methods/controlled_experiment.md) | 随机分组，只让一个因素不同 |
| 能改变 X，对象是培养的细胞、提取的分子 | [实验台实验](../06_methods/bench_experiment.md) | 一次只改变一个因素，其他因素保持不变[^vaux2012replicates-e6]；验证性实验事先估算样本量、定好主要结局指标[^perciedusert2020reporting-e13] |
| 能改变 X，对象是动物，结论要为人类医学提供依据 | [临床前动物研究](../06_methods/preclinical_animal_study.md) | 在动物模型里证明处理和效应之间的因果关系，再论证它能推广到病人身上[^henderson2013threats-e13] |
| 评价一种医疗干预 | [随机对照试验](../06_methods/randomized_controlled_trial.md) | 随机分配，按医学的报告规范写清分组和实施过程 |
| 能和政府、企业合作，在真实世界里随机 | [田野实验](../06_methods/field_experiment.md) | 在真实运行的项目里随机分组 |
| 不能随机，但有制度规则或自然事件造成的变化 | [准实验与因果识别](../06_methods/quasi_experiment.md) | 论证处理的变化"近似随机" |
| 只有观察数据，关心病因或干预效果 | [观察性流行病学](../06_methods/observational_epidemiology.md) | 写出目标试验，调整混杂因素 |
| 只有带位置的观察数据，关心环境或邻近地区怎样影响结果 | [空间分析研究](../07_fields/geography/practices/spatial_analysis.md)（地理学的实践） | 用考虑空间关系的回归模型；误差在空间上成团，可能是漏掉了一个有空间格局的变量[^rey2023geographic-e17] |
| 想弄清一个或几个案例里事情怎样发生 | [过程追踪](../06_methods/process_tracing.md)、[案例研究](../06_methods/case_study.md) | 在案例内部逐步检验机制 |

几点说明：

- **对照实验擅长回答"是不是"，不擅长回答"怎么样、为什么"。** 拿软件工程的工具评估来说：开发者怎么用一个工具、要懂哪些概念，这类问题更适合用非实验的定量或定性方法；而且往往要先有这些答案，才知道实验该比较什么、用什么任务、测什么[^ko2015practical-e1]。
- **定性方法也能讲因果，它擅长的是机制。** 案例研究能深入理解现象如何、为何发生，揭示因果关系背后的机制[^easterbrook2008selecting-e11]；什么时候该用它而不是实验，见上面"不同的看法"。政治学的过程追踪，是分析一个案例内部的过程和事件顺序，用来提出或检验关于因果机制的假设[^bennett2012process-e3]。
- **实验台实验、临床前动物研究和空间分析为什么放在这里** `[本项目分析]`。前两种都是自己动手改变一个因素：实验台实验一次只改变一个因素[^vaux2012replicates-e6]；临床前动物研究的第一个目标，就是在动物模型里证明处理和效应之间的因果关系[^henderson2013threats-e13]。空间分析有一部分研究环境怎样影响个人，例如社会和物理环境对健康的影响[^kwan2012uncertain-e4]，这部分属于解释因果；它描述空间分布的那部分，属于[观察描述](observe_describe.md)。
- **方法可以组合。** 可以从统计分析里挑几个案例做过程追踪，弄清因果方向是不是反了、相关是不是虚假的[^bennett2012process-e24]。也可以先做定量研究，再用定性研究解释其中的意外结果[^easterbrook2008selecting-e4]。多方法设计见[混合方法](../06_methods/mixed_methods.md)。

## 4. 它怎样影响整个项目

选了"解释因果"，每个阶段都会多出几件事 `[本项目分析]`：

| 阶段 | 多出来的事 | 详见 |
|---|---|---|
| 收敛成项目 | 主张写成"在条件 C 下，改变 X 会让 Y 怎样变"；想清楚自己能不能改变 X | [收敛成项目](../01_find-a-problem/05_converge.md) |
| 从问题到证据 | 列出四样东西各用什么证据；列出其他解释 | [从研究问题到证据清单](../02_do-the-project/01_question-to-evidence.md) |
| 选方法 | 能改变 X 就做实验；不能就先写识别策略或目标试验 | [选方法](../02_do-the-project/02_choose-method.md) |
| 效度 | 重点是内部效度：结果是否真的由数据得出 | [效度与局限](../02_do-the-project/04_validity-and-limits.md) |
| 预实验 | 先试最没把握的部分，比如提示的效果是否大到能被测出来 | [最小可跑版本](../02_do-the-project/05_pilot-and-derisk.md) |
| 执行 | 记录每次运行的模型版本、参数、提示原文；中途不换条件 | [执行与迭代](../02_do-the-project/06_run-and-iterate.md) |
| 分析 | 按事先写好的假设分析，不要试遍各种分析再挑结果 | [分析与解读](../02_do-the-project/07_analyze-and-interpret.md) |
| 写作 | 写清因果主张在什么条件下成立；写出排除了哪些解释、还剩哪些 | [讲清故事，写成论文](../03_write-and-publish/01_story-and-paper.md) |

几条依据：

- **内部效度是这类研究的核心标准。** 内部效度关注结果是否真的由数据得出；典型错误包括没有妥善处理混杂变量、误用统计分析[^easterbrook2008selecting-e65]。反过来，没有因果关系的研究就不该用内部效度去要求[^ralph2020empirical-e24]。
- **先写假设，再分析。** 从理论推出假设、再按假设来分析，能减少"钓结果"：有些相关是偶然出现的，找得够久总能找到[^easterbrook2008selecting-e63]。经济学有过教训：试遍各种回归设定、只报告最后的结果[^angrist2010credibility-e12]，这种撒大网式的搜索几乎不能支持因果解释[^angrist2010credibility-e13]。
- **因果的话要说出来，但要说清范围。** 流行病学方法文献明确反对回避"因果"一词：不论研究是否随机，因果推断都是科学的核心任务[^hernan2018cword-e2]。同时，主张的范围要和证据一致：实验只在你定义的指标和条件下支持了假设[^easterbrook2008selecting-e62]。

## 5. 哪些学科常用

下面只列本文资料能支持的学科；没有列出的，不等于不用，只是本文资料未涉及。

| 学科 | 资料里的情况 | 学科规矩 |
|---|---|---|
| 计算机 | 软件工程常问某个工具或技术是否带来质量、速度上的改进[^easterbrook2008selecting-e57]；机器学习最强的实证论文常做错误分析、消融实验和稳健性检查[^lipton2019troubling-e8] | [计算机](../07_fields/computer-science/README.md) |
| 临床医学 | 设计、实施、分析和报告都恰当的随机试验，一般被认为是评价医疗干预的最高质量证据[^hopewell2025consort-e2] | [临床医学](../07_fields/clinical-medicine/README.md) |
| 流行病学与公共卫生 | 以喝葡萄酒对慢性病的影响为例：长期随机试验被认为不合伦理，观察性分析就成了估计其长期因果效应的最好机会[^hernan2018cword-e11] | [健康科学](../07_fields/health-sciences/README.md) |
| 经济学 | 据 2010 年的综述，以研究设计为本的因果研究多见于发展、教育、环境、劳动、健康、公共财政等微观领域，在产业组织和宏观经济学中仍少见[^angrist2010credibility-e2] | [经济学](../07_fields/economics/README.md) |
| 政治学 | 一项研究编码的 195 份预分析计划（动手分析前公开登记的分析方案）中，63% 来自田野实验，27% 来自调查实验[^ofosu2023preanalysis-e3]；"过程追踪"一词 1979 年由政治学者 Alexander George 借用来指用案例内部证据推断历史解释[^bennett2012process-e2] | [政治学](../07_fields/political-science/README.md) |
| 教育学 | 有的研究做因果推断，例如估计缩小班额对成绩的影响[^aera2006standards-e4]；早期探索性研究找到的关系通常是相关的，不是因果的[^ies2013common-e3] | [教育学](../07_fields/education/README.md) |

## 6. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 把相关当成因果 | 相关可能来自反向因果、共同原因等[^easterbrook2008selecting-e56] |
| 只有共变就说"导致" | 还要有先后顺序、排除第三变量、提出机制假设[^ralph2020empirical-e203] |
| 一次改好几处，不做消融 | 看不出提升从哪来，可能只有一处在起作用[^lipton2019troubling-e4] |
| 只检验自己偏爱的解释 | 读者一眼能想到的其他解释没考虑，结论就没有说服力[^bennett2012process-e25] |
| 编一个听上去合理的机制，不找证据 | 过程追踪文献要求避免"偷懒的机制式讲故事"[^bennett2012process-e50] |
| 不随机分组，只说一句"本研究是探索性的" | 这不足以作为不随机的理由[^ralph2020empirical-e182] |
| 让软件自动挑要调整的变量 | 自动筛选变量可能适合预测，但不一定适合因果推断[^hernan2018cword-e8] |
| 调整了受处理影响的变量 | 一般应避免调整受处理或结果影响的变量[^hernan2020whatif-e8] |
| 把实验结论推得比实验条件更宽 | 实验只在你定义的指标下支持了假设[^easterbrook2008selecting-e62] |
| 证据只够相关，却硬写成因果 | 做不了因果主张时不做，本身不是缺点[^ralph2020empirical-e206] |

## 7. 延伸阅读

- **Easterbrook 等人 2008，Selecting Empirical Methods for Software Engineering Research**：第 2 节讲关系问题和因果问题的区别，第 5 节比较对照实验、案例研究等方法各自能回答什么。
- **Ko、LaToza 和 Burnett 2015，A practical guide to controlled experiments of software engineering tools with human participants**：有人参与的对照实验怎样一步步设计。
- **ACM SIGSOFT 实证研究标准**：实验标准和数据科学标准里的反面模式，可以当作因果主张的检查清单。
- **Lipton 和 Steinhardt 2019，Troubling Trends in Machine Learning Scholarship**：讲为什么要问"什么起了作用"，以及消融实验的作用和局限。
- **Hernán 和 Robins，Causal Inference: What If**：作者网站免费提供；第 3.6 节讲目标试验，第 7 至 9 章讲混杂、选择偏倚和测量偏倚。
- **Hernán 2018，The C-Word**：短评论，讲为什么要把因果问题说清楚。
- **Angrist 和 Pischke 2010，The Credibility Revolution in Empirical Economics**：经济学怎样转向以研究设计为本的因果研究。
- **Bennett 和 Checkel 2012，Process Tracing**：过程追踪的定义、四种检验和十条判断质量的标准。

[^easterbrook2008selecting-e36]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e36)
[^easterbrook2008selecting-e56]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e56)
[^easterbrook2008selecting-e35]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e35)
[^easterbrook2008selecting-e57]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e57)
[^easterbrook2008selecting-e58]: Easterbrook 等人 2008，§2.0。[证据](../../sources/notes/easterbrook2008selecting.md#e58)
[^easterbrook2008selecting-e59]: Easterbrook 等人 2008，§3.0。[证据](../../sources/notes/easterbrook2008selecting.md#e59)
[^easterbrook2008selecting-e60]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e60)
[^easterbrook2008selecting-e61]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e61)
[^easterbrook2008selecting-e62]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e62)
[^easterbrook2008selecting-e63]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e63)
[^easterbrook2008selecting-e64]: Easterbrook 等人 2008，§5.1。[证据](../../sources/notes/easterbrook2008selecting.md#e64)
[^easterbrook2008selecting-e11]: Easterbrook 等人 2008，§5.2。[证据](../../sources/notes/easterbrook2008selecting.md#e11)
[^easterbrook2008selecting-e16]: Easterbrook 等人 2008，§5.2。[证据](../../sources/notes/easterbrook2008selecting.md#e16)
[^easterbrook2008selecting-e4]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e4)
[^easterbrook2008selecting-e65]: Easterbrook 等人 2008，§7.0。[证据](../../sources/notes/easterbrook2008selecting.md#e65)
[^ralph2020empirical-e24]: ACM SIGSOFT 实证研究标准，General Standard，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e182]: SIGSOFT 人类参与者实验标准，脚注 5。[证据](../../sources/notes/ralph2020empirical.md#e182)
[^ralph2020empirical-e203]: SIGSOFT 数据科学标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e203)
[^ralph2020empirical-e206]: SIGSOFT 数据科学标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e206)
[^ko2015practical-e1]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e1)
[^ko2015practical-e3]: Ko 等人 2015，§2。[证据](../../sources/notes/ko2015practical.md#e3)
[^hopewell2025consortee-e1]: CONSORT 2025 解释文章（Hopewell 等人 2025），Item 17a，Box 5（Treatment allocation in trials）。[证据](../../sources/notes/hopewell2025consortee.md#e1)
[^hopewell2025consort-e2]: CONSORT 2025（Hopewell 等人 2025），Introduction，PDF 第 3 页。[证据](../../sources/notes/hopewell2025consort.md#e2)
[^angrist2010credibility-e1]: Angrist & Pischke 2010，摘要。[证据](../../sources/notes/angrist2010credibility.md#e1)
[^angrist2010credibility-e2]: Angrist & Pischke 2010，摘要。[证据](../../sources/notes/angrist2010credibility.md#e2)
[^angrist2010credibility-e5]: Angrist & Pischke 2010，Better Research Design。[证据](../../sources/notes/angrist2010credibility.md#e5)
[^angrist2010credibility-e12]: Angrist & Pischke 2010，The Leamer Critique and His Proposed Remedies。[证据](../../sources/notes/angrist2010credibility.md#e12)
[^angrist2010credibility-e13]: Angrist & Pischke 2010，Whither Sensitivity Analysis?。[证据](../../sources/notes/angrist2010credibility.md#e13)
[^hernan2016target-e1]: Hernán & Robins 2016，摘要。[证据](../../sources/notes/hernan2016target.md#e1)
[^hernan2018cword-e2]: Hernán 2018，正文开头。[证据](../../sources/notes/hernan2018cword.md#e2)
[^hernan2018cword-e8]: Hernán 2018，Better confounding adjustment。[证据](../../sources/notes/hernan2018cword.md#e8)
[^hernan2018cword-e11]: Hernán 2018，Conflating the means and the ends。[证据](../../sources/notes/hernan2018cword.md#e11)
[^hernan2020whatif-e6]: Hernán & Robins，What If，第 7.4 节。[证据](../../sources/notes/hernan2020whatif.md#e6)
[^hernan2020whatif-e7]: Hernán & Robins，What If，第 7.4 节。[证据](../../sources/notes/hernan2020whatif.md#e7)
[^hernan2020whatif-e8]: Hernán & Robins，What If，第 7.6 节。[证据](../../sources/notes/hernan2020whatif.md#e8)
[^hernan2020whatif-e11]: Hernán & Robins，What If，第 7.3 节。[证据](../../sources/notes/hernan2020whatif.md#e11)
[^bennett2012process-e2]: Bennett & Checkel 2012，Defining Process Tracing，第 7 页。[证据](../../sources/notes/bennett2012process.md#e2)
[^bennett2012process-e3]: Bennett & Checkel 2012，Defining Process Tracing，第 10 页。[证据](../../sources/notes/bennett2012process.md#e3)
[^bennett2012process-e9]: Bennett & Checkel 2012，Bayesianism and Process Tracing，第 19 页。[证据](../../sources/notes/bennett2012process.md#e9)
[^bennett2012process-e24]: Bennett & Checkel 2012，Techniques and Standards，第 24 页。[证据](../../sources/notes/bennett2012process.md#e24)
[^bennett2012process-e25]: Bennett & Checkel 2012，Standards of Good Process Tracing，第 26 页。[证据](../../sources/notes/bennett2012process.md#e25)
[^bennett2012process-e29]: Bennett & Checkel 2012，标准 2，第 28 页。[证据](../../sources/notes/bennett2012process.md#e29)
[^bennett2012process-e50]: Bennett & Checkel 2012，Conclusion，第 40 页。[证据](../../sources/notes/bennett2012process.md#e50)
[^gerring2004case-e4]: Gerring 2004，Causal Insight，第 349 页。[证据](../../sources/notes/gerring2004case.md#e4)
[^lipton2019troubling-e4]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../sources/notes/lipton2019troubling.md#e4)
[^lipton2019troubling-e6]: Lipton & Steinhardt 2019，§3.2，第 3 页。[证据](../../sources/notes/lipton2019troubling.md#e6)
[^lipton2019troubling-e7]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../sources/notes/lipton2019troubling.md#e7)
[^lipton2019troubling-e8]: Lipton & Steinhardt 2019，§5.1，第 8 页。[证据](../../sources/notes/lipton2019troubling.md#e8)
[^ofosu2023preanalysis-e3]: Ofosu & Posner 2023，Empirical Approach。[证据](../../sources/notes/ofosu2023preanalysis.md#e3)
[^aera2006standards-e4]: AERA 2006，§2 Design and Logic。[证据](../../sources/notes/aera2006standards.md#e4)
[^ies2013common-e3]: IES & NSF 2013，Types of Research。[证据](../../sources/notes/ies2013common.md#e3)
[^vaux2012replicates-e6]: Vaux 等人 2012，Sidebar A。[证据](../../sources/notes/vaux2012replicates.md#e6)
[^perciedusert2020reporting-e13]: Percie du Sert 等人 2020（ARRIVE 2.0 解释文件），Item 13。[证据](../../sources/notes/perciedusert2020reporting.md#e13)
[^henderson2013threats-e13]: Henderson 等人 2013，Introduction。[证据](../../sources/notes/henderson2013threats.md#e13)
[^rey2023geographic-e17]: Rey 等 2023（在线教材），Spatial Regression。[证据](../../sources/notes/rey2023geographic.md#e17)
[^kwan2012uncertain-e4]: Kwan 2012，第 959 页。[证据](../../sources/notes/kwan2012uncertain.md#e4)
