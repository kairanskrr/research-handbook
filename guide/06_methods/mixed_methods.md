# 混合方法：用两种及以上方法研究同一个问题

> **状态**：初稿，待审阅 · **最后更新**：2026-10-07

本文讲**混合方法研究**（mixed methods research）和更宽泛的**多方法研究**（multi-method research）：围绕同一个研究问题，组合两种及以上的方法。例如先从代码仓库中挖出规律，再访谈开发者解释原因；或者先访谈形成假设，再用问卷在更大范围检验。

本文只讲"怎么组合"。每个组成部分本身怎么做，见对应的文档：[仓库挖掘研究](../07_fields/computer-science/practices/repository_mining.md)、[访谈研究](interview_study.md)、[问卷调查](questionnaire_survey.md)等。怎样根据问题选方法、什么时候需要组合，见[选定研究套路和方法](../02_from-project-to-study/02_choose-strategy-and-method.md#4-需要时组合几种方法)。

**适用范围** `[本项目分析]`：本文的规范和例子主要来自软件工程，依据是 ACM SIGSOFT 实证研究标准中的多方法与混合方法标准、Easterbrook 等人的方法选择指南，以及 Storey 等人对软件工程研究策略的分析。其他学科做混合方法研究时，先看本学科的规范。目前本手册还没有其他学科专讲混合方法的方法篇；政治学把统计分析和案例内的过程追踪结合起来的做法，可以参考[过程追踪与比较案例研究](process_tracing.md)。

**常服务的套路**：[解释因果](../05_research-strategies/explain_causality.md)。

**读完本文，你应该能：**

- 判断自己的问题值不值得用多种方法，以及要付出什么代价；
- 在三种常见设计中选一种，并说清各方法在哪个阶段、起什么作用；
- 把不同方法的结果真正整合起来，而不是各写各的；
- 认出"顺手加一个小问卷"之类的常见错误。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准区分了两个说法[^ralph2020empirical-e274]：

- **多方法研究**：用两种及以上的数据收集或分析方式，来印证、补充和扩展研究发现。
- **混合方法研究**：把归纳式研究（从数据中总结出规律）和演绎式研究（用数据检验事先的假设）结合并整合起来，常常但不一定是定性数据加定量数据。

下文为简便统称"混合方法"，两者的要求基本相同。

**为什么要组合方法**：每种方法都有已知的缺陷，但各自的缺陷不同；组合几种方法，可以让一种方法的弱点由另一种弥补[^easterbrook2008selecting-e1]。Storey 等人把软件工程的研究策略按四个质量标准比较：推广性、真实性、对人为因素的控制、数据精度。每种策略都有长有短，所以可能需要跨策略做三角验证（triangulation，用不同来源或方法的证据互相印证）[^storey2020who-e3]。在软件工程里，一个典型情形是：只分析提交记录、评审意见这类痕迹数据，只能看到人的行为、意图和互动的一部分[^storey2020who-e1]；以描述人和社会层面为目的的研究，结论应当再用访谈、问卷或观察来印证[^storey2020who-e4]。评估面向人的工具也是如此：例如一个推荐可能缺陷的工具，可能需要放到真人使用中评估，看它怎样改变使用环境[^storey2020who-e5]。

**代价也要算清**：数据收集量大，分析多种来源的数据很费时间，还要求研究者同时熟悉定量和定性研究[^easterbrook2008selecting-e3]。

**什么时候不必用** `[本项目分析，依据下列资料]`：

- 一种方法已经足以回答问题。例如评估一种缩短构建时间的新技术，加入人的反馈未必有帮助[^storey2020who-e6]。
- SIGSOFT 的通用标准把"对同一问题使用两种及以上的数据收集或分析策略"列为**优秀项**，而不是必要项[^ralph2020empirical-e290]。方法只需适合研究目的，不要求最优[^ralph2020empirical-e23]。

**先分清三件事**，它们常被混为一谈：

| | 是什么 | 例子 `[本项目分析]` |
|---|---|---|
| 一种方法内的多种数据收集技术 | 同一项研究里用几种方式收集数据，也能做三角验证[^easterbrook2008selecting-e9] | 一项案例研究中既访谈又看文档 |
| 数据三角验证 | 同一种方法，换不同的数据来源[^storey2020who-e7] | 同一个挖掘分析在五个数据集上重复 |
| 方法三角验证（本文的主题） | 组合不同的研究策略[^storey2020who-e7][^ralph2020empirical-e288] | 先挖掘仓库，再访谈开发者 |

SIGSOFT 标准特别提醒要区分第一行和第三行[^ralph2020empirical-e288]；Storey 等人也强调，研究方法（收集数据的技术，如访谈）和研究策略（可以包含一种或多种方法）是两回事[^storey2020who-e2]。第二行也不能代替第三行：在更多数据集上重复可能提高推广性，但不能提高真实性，也不能加强对人为因素的控制[^storey2020who-e8]。

> **不同的看法：一篇论文该不该自己完成三角验证？**
> - Storey 等人分析了一批软件工程论文，发现以数据为主的论文绝大多数没有和其他策略做三角验证，做了的多数是配上问卷或访谈[^storey2020who-e9]；他们呼吁更多地组合研究策略[^storey2020who-e11]。
> - 但他们也承认，三角验证的责任不一定要落在单篇论文上[^storey2020who-e10]；SIGSOFT 标准也把"混合方法没有必要"列为不成立的批评（前提是它确实有益）[^ralph2020empirical-e287]，并把多方法列为优秀项而非必要项[^ralph2020empirical-e290]。
>
> 实际操作中 `[本项目分析]`：如果你的结论涉及"人为什么这样做""工具在真实使用中效果如何"，单一的数据分析很难撑起来，值得在本篇或紧接的后续工作中补上另一种方法；如果问题本身是技术性的，不必为混合而混合。

---

## 2. 三种常见设计

Easterbrook 等人介绍了混合方法的三种设计，关键在于数据收集策略和各方法的先后顺序[^easterbrook2008selecting-e2][^easterbrook2008selecting-e4][^easterbrook2008selecting-e5][^easterbrook2008selecting-e6]；SIGSOFT 标准提到的几个核心设计名称与之基本对应[^ralph2020empirical-e289]：

| 设计 | 顺序 | 用途 | 计算机领域的例子 `[本项目分析]` |
|---|---|---|---|
| **解释性序贯设计**（sequential explanatory） | 先定量，后定性 | 用定性结果解释定量发现；定量阶段出现意外结果时特别有用[^easterbrook2008selecting-e4] | 挖掘发现某类拉取请求合并特别慢，再访谈维护者问原因 |
| **探索性序贯设计**（sequential exploratory） | 先定性，后定量 | 用定量结果帮助解读定性发现，检验定性研究中形成的初步理论[^easterbrook2008selecting-e5] | 先访谈十几位工程师总结出几种做法，再用问卷看各种做法有多普遍 |
| **并行三角验证设计**（concurrent triangulation；与 SIGSOFT 标准所说的汇聚式设计相近 `[本项目分析]`） | 同时进行 | 互相确认、交叉验证；动机是"人们说的"常常和"人们做的"不一样[^easterbrook2008selecting-e6] | 同时收集开发者的问卷回答和他们的实际工具使用日志，对照两者 |

**怎么选** `[本项目分析]`：已经有数据、想知道"为什么"，用解释性序贯设计；对现象还不了解、想先弄清有哪些情况再测量多普遍，用探索性序贯设计；担心单一来源有偏差、想互相核对，用并行设计。并行设计的难点在于比较两种分析的结果、化解它们之间的矛盾，有时需要再找一个证据来源或做后续研究[^easterbrook2008selecting-e7]。

---

## 3. 怎么做

### 第一步：写清为什么混合，以及每种方法在何时、起什么作用

SIGSOFT 标准的必要项要求你回答四个问题[^ralph2020empirical-e276]：

- **为什么**：论证为什么需要多种方法，并用一段目的陈述说明总体设计意图；
- **是什么**：采用哪种设计；
- **何时**：各方法用在研究的哪个阶段；
- **怎样对应问题**：设计如何服务于研究问题。

最好再画一张研究设计图，并给出所用设计的定义[^ralph2020empirical-e278]。

**容易错在哪**：设计和研究问题对不上；团队因为立场不同或方法各异，始终没商定一个清楚的研究问题[^ralph2020empirical-e284]。先把研究问题写成一句话，再看每种方法分别回答它的哪一部分 `[本项目分析]`。

### 第二步：每个组成部分都要达到它自己的标准

SIGSOFT 的混合方法标准只管"怎么组合"；每个组成部分还要满足各自方法的标准。例如案例研究加实验，要同时符合案例研究标准、实验标准和混合方法标准[^ralph2020empirical-e275]。各方法自己的质量标准都要考虑[^ralph2020empirical-e281]。

**容易错在哪**：团队并不掌握某种方法，却指望它能奏效，SIGSOFT 称之为"货物崇拜式研究"（只模仿了方法的形式，没有掌握实质）[^ralph2020empirical-e284]。另一种情形是对丰富的定性数据只做肤浅的统计[^ralph2020empirical-e285]，例如把访谈内容简化成词频 `[本项目分析]`。不熟悉的方法，先读对应的文档和指南，或者请熟悉它的人加入。

### 第三步：想清楚样本怎样在各方法之间流动

- 说明各方法之间是否复用同一批对象，以及为什么[^ralph2020empirical-e278]。
- **先后几个阶段用同一批人时，要考虑前一阶段对后一阶段的影响**[^ralph2020empirical-e285]。`[本项目分析]` 例如受访者在访谈中听你介绍了研究假设，之后再答问卷，回答就可能偏向这个假设。
- 各部分样本来自不同总体时，整合结论会受到限制，要在论文中承认[^ralph2020empirical-e277]。

### 第四步：让前一阶段真正塑造后一阶段

序贯设计的意义在于"前面的发现决定后面怎么做"。后一阶段设计访谈提纲或问卷时没有利用前一阶段的发现，是 SIGSOFT 列出的反面模式[^ralph2020empirical-e285]。`[本项目分析]` 例如挖掘阶段发现了三种出乎意料的模式，访谈提纲就应该围绕这三种模式来问，而不是沿用挖掘前就写好的通用问题。

### 第五步：整合结果（最难的一步）

整合是混合方法的核心要求：把所有方法的发现放在一起回答研究问题[^ralph2020empirical-e277]。"整合失败"是 SIGSOFT 列出的反面模式[^ralph2020empirical-e283]。

- **说清每种方法带来的额外价值**：是印证（两种方法得出同样结论）、互补（各回答问题的一部分），还是扩展（加深或拓宽理解）[^ralph2020empirical-e279]。
- **讨论不一致的地方**[^ralph2020empirical-e279]。结果不一致不是缺陷，SIGSOFT 把"各方法的发现不一致"列为不成立的批评[^ralph2020empirical-e287]；不一致往往正是最值得分析的地方。化解不了时，可能需要再找一个证据来源，或做后续研究[^easterbrook2008selecting-e7]。
- `[本项目分析]` 一个实用的做法是做一张对照表：每一行是一个研究子问题或一个发现，各列分别写每种方法得出了什么，最后一列写整合后的结论，以及它们是相互印证、相互补充还是相互矛盾。写结论时，从这张表出发，而不是从某一种方法的结果出发。

### 第六步：报告

- 每种方法都要在引言和方法部分交代清楚。在讨论或局限部分突然冒出一个前面没提过的方法，SIGSOFT 称之为"不速之客"[^ralph2020empirical-e283]。
- 讨论每种方法的局限，以及整合本身的局限[^ralph2020empirical-e283][^ralph2020empirical-e277]。
- 可以在标题中表明使用了多方法或混合方法[^ralph2020empirical-e278]。
- 会议篇幅有限时，某些方法的细节可以放在其他论文或补充材料中[^ralph2020empirical-e286]。

---

## 4. 检查清单

下面主要依据 SIGSOFT 的多方法与混合方法标准，它是软件工程领域的审稿标准；其他学科以本学科的规范为准 `[本项目分析]`。各组成部分还要对照各自方法的检查清单。

**必须做到**

- [ ] 论证为什么要用多种方法；写出总体设计意图（为什么）[^ralph2020empirical-e276]
- [ ] 描述采用的设计（是什么），以及各方法用在哪个阶段（何时）[^ralph2020empirical-e276]
- [ ] 说明设计怎样对应研究问题[^ralph2020empirical-e276]
- [ ] 整合所有方法的发现来回答研究问题；承认整合带来的局限[^ralph2020empirical-e277]

**做到更好**

- [ ] 给出所用设计的定义，画出研究设计图，在标题中注明[^ralph2020empirical-e278]
- [ ] 说明并论证各方法之间是否复用样本[^ralph2020empirical-e278]
- [ ] 说清混合带来的额外价值（印证、互补、扩展），讨论不一致的发现[^ralph2020empirical-e279]
- [ ] 说明研究的哲学或理论基础；描述设计中的困难和缓解办法；讨论方法混合带来的伦理问题[^ralph2020empirical-e280]

**这些情况可以不做，不算缺陷**[^ralph2020empirical-e286]

- 会议篇幅有限，部分方法的细节放在其他论文或补充材料中
- 用循环或并行过程，而不是"阶段"来描述研究

**审稿时常见、但不成立的批评**（SIGSOFT 标准列出的，针对软件工程的投稿）[^ralph2020empirical-e287]：你不必为此担心

- "各方法贡献不对等"，或"次要方法规模太小（例如参与者少）"
- "混合方法没有必要"（实际上有益时）
- "各方法的哲学基础不同，不能放在一起"（混合方法多与实用主义立场相联系，即用最能有效解决问题的方法[^easterbrook2008selecting-e8]）
- "主次方法选反了"
- "各方法的发现不一致"

---

## 5. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 主体研究做完后，顺手加一个很小的问卷或几次访谈，就称为混合方法 | 一种方法只起点缀作用，却包装成混合方法，是"障眼法"[^ralph2020empirical-e282] |
| 为了迎合审稿人加一个方法 | 对发现没有实质贡献，是"出卖灵魂"[^ralph2020empirical-e282] |
| 各方法的结果分成几节各写各的 | 没有整合，读者得不到一个统一的答案[^ralph2020empirical-e283] |
| 后一阶段的问卷或提纲没有用上前一阶段的发现 | 失去了序贯设计的意义[^ralph2020empirical-e285] |
| 同一批人先访谈后答问卷，不考虑前者的影响 | 前一阶段可能污染后一阶段[^ralph2020empirical-e285] |
| 用不熟悉的方法，指望它能奏效 | 组成部分达不到它自己的标准[^ralph2020empirical-e284][^ralph2020empirical-e275] |
| 只讨论主要方法的局限 | 每种方法和整合本身都有局限[^ralph2020empirical-e283] |

注意第一行和"不成立的批评"的区别：次要方法规模小本身不是问题[^ralph2020empirical-e287]；问题在于它对结论**没有实质贡献**[^ralph2020empirical-e282]。一个只有几位受访者、但真正解释了挖掘结果的访谈，是合格的组成部分 `[本项目分析]`。

---

## 6. 延伸阅读

- **SIGSOFT 多方法与混合方法标准**：完整的检查清单和十余种反面模式，并附有大量软件工程范例论文（例如仓库挖掘加问卷、实验加访谈），适合找一篇和自己设计相近的论文参考。
- **Easterbrook 等人 2008**：讲怎样为软件工程研究选择实证方法，其中一节介绍了三种混合方法设计及例子。适合在设计阶段读。
- **Storey 等人 2020**：用一个"谁受益、贡献是什么、怎样研究"的框架分析了软件工程论文的研究策略，说明为什么只靠数据分析不够、何时需要加入以人为对象的方法。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^ralph2020empirical-e274]: SIGSOFT 多方法与混合方法标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e274)
[^ralph2020empirical-e275]: SIGSOFT 多方法与混合方法标准，Application。[证据](../../sources/notes/ralph2020empirical.md#e275)
[^ralph2020empirical-e276]: SIGSOFT 多方法与混合方法标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e276)
[^ralph2020empirical-e277]: SIGSOFT 多方法与混合方法标准，必要项及脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e277)
[^ralph2020empirical-e278]: SIGSOFT 多方法与混合方法标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e278)
[^ralph2020empirical-e279]: SIGSOFT 多方法与混合方法标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e279)
[^ralph2020empirical-e280]: SIGSOFT 多方法与混合方法标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e280)
[^ralph2020empirical-e281]: SIGSOFT 多方法与混合方法标准，General Quality Criteria。[证据](../../sources/notes/ralph2020empirical.md#e281)
[^ralph2020empirical-e282]: SIGSOFT 多方法与混合方法标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e282)
[^ralph2020empirical-e283]: SIGSOFT 多方法与混合方法标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e283)
[^ralph2020empirical-e284]: SIGSOFT 多方法与混合方法标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e284)
[^ralph2020empirical-e285]: SIGSOFT 多方法与混合方法标准，反面模式。[证据](../../sources/notes/ralph2020empirical.md#e285)
[^ralph2020empirical-e286]: SIGSOFT 多方法与混合方法标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e286)
[^ralph2020empirical-e287]: SIGSOFT 多方法与混合方法标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e287)
[^ralph2020empirical-e288]: SIGSOFT 多方法与混合方法标准，Notes。[证据](../../sources/notes/ralph2020empirical.md#e288)
[^ralph2020empirical-e289]: SIGSOFT 多方法与混合方法标准，Notes。[证据](../../sources/notes/ralph2020empirical.md#e289)
[^ralph2020empirical-e290]: SIGSOFT General Standard，优秀项。[证据](../../sources/notes/ralph2020empirical.md#e290)
[^ralph2020empirical-e23]: SIGSOFT General Standard，必要项。[证据](../../sources/notes/ralph2020empirical.md#e23)
[^easterbrook2008selecting-e1]: Easterbrook 等人 2008，§1.0。[证据](../../sources/notes/easterbrook2008selecting.md#e1)
[^easterbrook2008selecting-e2]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e2)
[^easterbrook2008selecting-e3]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e3)
[^easterbrook2008selecting-e4]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e4)
[^easterbrook2008selecting-e5]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e5)
[^easterbrook2008selecting-e6]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e6)
[^easterbrook2008selecting-e7]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e7)
[^easterbrook2008selecting-e8]: Easterbrook 等人 2008，§5.6。[证据](../../sources/notes/easterbrook2008selecting.md#e8)
[^easterbrook2008selecting-e9]: Easterbrook 等人 2008，§6.0。[证据](../../sources/notes/easterbrook2008selecting.md#e9)
[^storey2020who-e1]: Storey 等人 2020，§2。[证据](../../sources/notes/storey2020who.md#e1)
[^storey2020who-e2]: Storey 等人 2020，§3.3。[证据](../../sources/notes/storey2020who.md#e2)
[^storey2020who-e3]: Storey 等人 2020，§3.3。[证据](../../sources/notes/storey2020who.md#e3)
[^storey2020who-e4]: Storey 等人 2020，§6.2。[证据](../../sources/notes/storey2020who.md#e4)
[^storey2020who-e5]: Storey 等人 2020，§6.2。[证据](../../sources/notes/storey2020who.md#e5)
[^storey2020who-e6]: Storey 等人 2020，§6.2。[证据](../../sources/notes/storey2020who.md#e6)
[^storey2020who-e7]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e7)
[^storey2020who-e8]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e8)
[^storey2020who-e9]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e9)
[^storey2020who-e10]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e10)
[^storey2020who-e11]: Storey 等人 2020，§6.4。[证据](../../sources/notes/storey2020who.md#e11)
