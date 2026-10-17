# 定量仿真：用计算模型模拟系统或过程

本文讲**定量仿真研究**：建立一个模仿真实系统行为的计算模型，在模型上做实验，回答关于系统的问题。例如用仿真比较不同调度策略下的集群吞吐量，或者仿真一个软件项目在不同测试投入下的进度。

如果你测的是真实运行的系统本身，那是[基准评测](../07_fields/computer-science/practices/benchmarking.md)；如果你用仿真来评估自己提出的新方法或新工具，还要同时满足[工程研究](../07_fields/computer-science/practices/engineering_research.md)的要求。效度的基本概念见[效度与局限：设计阶段就想清楚](../02_do-the-project/04_validity-and-limits.md)。

**适用范围**：本文的检查清单依据 ACM SIGSOFT（美国计算机协会软件工程分会）为软件工程写的实证研究标准，效度威胁的整理来自软件工程仿真研究的综述，例子以计算机系统和软件项目为主。验证与确认、输出数据分析的做法来自仿真方法的通用教程（Sargent 2010、Alexopoulos & Kim 2002），不限于计算机。其他学科用模型和模拟做研究时，先看本学科的规范，例如土木工程的数值模拟见[土木工程：数值模拟](../07_fields/civil-engineering/README.md#数值模拟先分清验证确认和校准)。

**常服务的套路**：[构建改进](../05_research-strategies/build_improve.md)（真实系统不便直接实验时，在模型上评估新设计）。

**读完本文，你应该能：**

- 判断自己的问题适不适合用仿真回答；
- 分清"验证"和"确认"，知道各用什么方法做；
- 用真实数据校准模型，并写清模型的假设；
- 设计仿真实验：选因素、重复运行、处理预热期、做敏感性分析；
- 用文末的检查清单检查自己的研究。

---

## 1. 这是什么研究，什么时候用

ACM SIGSOFT（美国计算机协会软件工程分会）的实证研究标准这样定义：仿真研究建立并使用一个模仿真实系统行为的数学模型，通常包括理解问题、收集数据、建模、验证、确认、实验设计、数据分析和落实结果[^ralph2020empirical-e397]。

这里只讲**一切都用计算模型表示**的仿真。让人来操作仿真模型的研究（例如让学生用项目管理模拟器做决策），属于有人参与的实验[^ralph2020empirical-e398]。常见的仿真方法有离散事件仿真（系统状态只在"事件"发生时改变，如任务到达、任务完成）、系统动力学（用存量、流量和反馈回路描述系统）、基于智能体的仿真（模拟许多个体各自按规则行动）[^ralph2020empirical-e400]。标准是为软件工程写的；系统、网络等方向用仿真研究调度、协议、体系结构时，道理相同。

**什么时候用**：

- 在真实环境中做实验不可行或风险太大时[^defranca2015simulation-e18]，例如系统还没建成、规模太大，或者试错代价太高（这几个例子是本手册补的）。
- 论文里要说明为什么仿真适合你的问题，这是标准的第一项必要要求[^ralph2020empirical-e399]。

**要心里有数**：仿真结论的可信度取决于模型。如果拿不到真实系统的运行数据，通常无法对模型有很高的信心；这时要尽可能充分地探索模型行为，并尽量和其他有效模型比较[^sargent2010verification-e15]。

---

## 2. 怎么做

### 第一步：先定目的和精度要求

**怎么做**：写下模型要回答的问题、关心哪些输出变量，以及这些输出需要准到什么程度。精度要求最好在开始建模前就定下来[^sargent2010verification-e3]。

**为什么**：模型是为特定目的建的，有效与否也只针对这个目的；一个模型在一组实验条件下有效，换一组条件可能就无效[^sargent2010verification-e2]。没有目的和精度要求，"模型对不对"就无从判断。

### 第二步：建模，把假设写出来

**怎么做：**

1. **描述模型**：概念层（模型由哪些变量和关系组成）和实现层（代码），包括输入参数和响应变量（你要观察的输出）[^ralph2020empirical-e400]。最好把两层分开写[^ralph2020empirical-e407]。
2. **列出全部假设。** 例如"任务到达服从泊松分布""各节点故障相互独立"。明确写出模型假设是必要项[^ralph2020empirical-e404]。

**为什么**：所有模型都有假设。只要写明、给出理由、讨论了对效度的影响，"模型有假设"就不构成有效的批评[^ralph2020empirical-e412]。反过来，假设没写明，结果可能被误读，读者也无法判断模型在多大程度上对应真实现象[^defranca2015simulation-e6]。

**容易错在哪**：**把想要的结论直接写进假设。** de França & Travassos 分析软件工程仿真论文时发现，在这些论文报告的效度威胁中，这一条出现得最多：模型的简化假设直接决定了输出，这样的话不跑仿真也能预测结果，仿真就没有意义了[^defranca2015simulation-e4]。例如要研究"新调度策略能否降低延迟"，却在模型里直接假设"新策略下每个任务的等待时间减少 20%"。这类问题拿输出去和实测数据比较是发现不了的；只有请仿真专家检查模型内部（如表面效度检查，见第三步）这类方法，才可能发现[^defranca2015simulation-e16]。

> **不同的看法：缺数据时，假设能用到什么程度？**
> - SIGSOFT 标准认为，校准数据不足或太贵时，模型的部分内容可以用假设代替，但必须说明并给出理由[^ralph2020empirical-e411]。
> - de França & Travassos 的建议更严格：始终检验模型的假设[^defranca2015simulation-e14]。Sargent 也建议尽可能检验模型依据的假设和理论[^sargent2010verification-e19]。
>
> 实际操作中：每条假设都写明来源；能用数据检验的就检验；不能检验的，用敏感性分析（见第七步）看它变化时结论是否改变。

### 第三步：验证与确认

这两个词容易混。用大白话说[^sargent2010verification-e1]：

- **验证**（verification）：**程序写对了吗？** 代码是否正确实现了你设计的模型。
- **确认**（validation）：**模型对你的目的够准吗？** 模型在适用范围内的精度是否满足预期用途。

Sargent 把它细分为四件事[^sargent2010verification-e5][^sargent2010verification-e6]：

| 检查 | 问的是什么 |
|---|---|
| 概念模型确认 | 模型依据的理论和假设对吗？对真实系统的表示合理吗？ |
| 计算机模型验证 | 代码正确实现了概念模型吗？ |
| 运行确认 | 模型的输出在适用范围内足够准吗？ |
| 数据有效性 | 建模、检验和实验用的数据充分、正确吗？ |

**常用方法**（可以组合使用）：

- **测试代码**：在不同条件下运行程序，用输出和中间值判断实现是否正确[^sargent2010verification-e14]。
- **退化测试和极端条件测试**：选特殊参数看行为是否合理。例如到达率大于服务率时，单个服务台的队列应当越排越长[^sargent2010verification-e8]。
- **和解析模型比**：模型的简单情形，和已知的理论结果对照[^sargent2010verification-e9]。例如单服务台排队可以和排队论公式对照。
- **请专家看**（表面效度，face validity）：请了解该系统的人判断模型和它的行为是否合理[^sargent2010verification-e10]。de França & Travassos 建议让领域专家同时检查概念模型、可执行模型和仿真结果[^defranca2015simulation-e12]。
- **和真实数据比**：见第四步。

**做到什么程度**：证明模型在整个适用范围内绝对有效通常代价太大，实际做法是不断测试和评估，直到有足够信心认为它适合预期用途[^sargent2010verification-e4]。应对效度威胁的投入，要根据研究目标和预期收益来权衡[^defranca2015simulation-e17]。

**为什么**：模型本身就是仿真研究效度的主要威胁；模型无效，其他补救都无济于事[^defranca2015simulation-e11]。没有证据表明模型有效时，结论只能关于模型本身，不能推到真实系统上[^defranca2015simulation-e8]。

**容易错在哪**：

- **只看输出吻合就放心。** 模型可能"用错误的解释得出了正确的结果"[^defranca2015simulation-e7]。
- **改了模型不重新检查。** 模型任何改动后都要重新验证和确认[^sargent2010verification-e7]。

### 第四步：用真实数据校准，并留出检验数据

**校准**（calibration）是用真实数据确定模型参数的取值，例如用集群日志估计任务到达率和运行时长的分布。

**怎么做：**

1. **写清校准用了哪些数据、怎么校准、数据来自什么背景**[^ralph2020empirical-e401]。
2. **留一部分数据做检验。** 用一部分历史数据建模，用剩下的数据检验模型行为是否和系统一致[^sargent2010verification-e10]。
3. **比较分布，而不是单个数。** 不要拿单个仿真值和单个实测值比，要用统计方法比较分布[^defranca2015simulation-e3]。最好用置信区间或假设检验，因为它们能做客观判断；不过实践中最常用的仍是画图比较[^sargent2010verification-e16]。用假设检验时要特别注意：把无效模型误判为有效，这类错误的风险必须控制得很小[^sargent2010verification-e17]。

**容易错在哪**：

- **校准和实验用了不同背景的数据**，例如用一个组织的数据校准，却拿去模拟另一个组织[^defranca2015simulation-e5]。结果的推广范围不会超出支撑数据的范围[^defranca2015simulation-e9]。
- **为了重现参考数据而过度拟合模型**，例如造一个只能产生期望结果的模型，这是标准列出的反面模式[^ralph2020empirical-e409]。
- **低估数据的难度。** 模型确认失败常常是因为数据有问题[^sargent2010verification-e13]。

### 第五步：设计实验

**怎么做：**

1. **写清研究方案**：自变量、场景、每个场景运行几次、用稳态条件还是终止条件结束运行[^ralph2020empirical-e403]。
2. **用标准的实验设计**，如因子设计（把每个因素的各个取值组合起来逐一运行）或部分因子设计（只运行其中有代表性的一部分组合）；用非标准设计要说明理由[^ralph2020empirical-e410]。去掉因素来简化设计时要谨慎[^defranca2015simulation-e10]。
3. **因素不只是输入参数。** 还可以包括模型的内部参数、不同的样本数据集，以及实现了不同策略的模型版本[^defranca2015simulation-e15]。

### 第六步：重复运行，处理预热期

**怎么做：**

1. **随机模型要多次独立运行。** 对随机模型只跑一次是标准列出的反面模式[^ralph2020empirical-e409]：单次结果反映的可能只是随机波动，而不是你要研究的机制[^defranca2015simulation-e2]。
2. **用"每次运行的平均值"做统计。** 一次运行内部的观测值通常相互相关，不是独立同分布的，不能直接套用经典统计方法[^alexopoulos2002output-e1]。常用做法是做多次独立运行，用每次运行的样本均值作为彼此独立的观测[^alexopoulos2002output-e3][^alexopoulos2002output-e7]。重复运行还能告诉你模型内部的随机波动有多大[^sargent2010verification-e12]。
3. **先分清终止型和稳态型。** 终止型仿真从特定状态开始、到某个事件结束（例如模拟一周的运行）；稳态仿真研究系统的长期行为[^alexopoulos2002output-e2]。
4. **稳态仿真要去掉预热期。** 系统从"空"状态启动，开头一段数据带有初始状态的偏差[^alexopoulos2002output-e4]。最常用的办法是丢掉每次运行开头的一段数据（预热期），因为初始状态主要影响运行开头的数据[^alexopoulos2002output-e5][^alexopoulos2002output-e7]。丢多长，可以用 Welch 作图法判断：把多次运行的输出求平均，画出移动平均曲线，取曲线开始收敛的位置[^alexopoulos2002output-e6]。

**容易错在哪**：以为多跑几次就能消除预热偏差。初始状态造成的系统误差，不能靠增加重复次数来减小[^alexopoulos2002output-e8]。

### 第七步：做敏感性分析

**敏感性分析**：改变模型的输入参数和内部参数，看输出怎么变[^sargent2010verification-e11]。

**怎么做和为什么：**

- **检验模型**：模型中的关系应当和真实系统一致[^sargent2010verification-e11]。例如增加机器数量后吞吐量反而下降，要么发现了真实现象，要么模型有错。
- **找出关键参数**：对输出影响大的参数，使用模型前要把它们弄得足够准确[^sargent2010verification-e11]。
- **防止"钓"结果**：用敏感性分析的结果选择合理的参数设置，而不是反复试参数，直到出现想要的结果[^defranca2015simulation-e13]。
- **报告出来**：标准把报告敏感性分析列为加分项[^ralph2020empirical-e407]。

### 第八步：报告模型和代码

de França & Travassos 的综述发现，软件工程仿真研究的报告质量整体较差，常缺研究目标、研究过程和实验设计等关键信息[^defranca2015simulation-e1]。报告时至少写清：

- 写清仿真方法、所用工具或软件包的版本和计算环境[^ralph2020empirical-e400]。
- 结合数据和模型分析效度威胁，例如场景不具代表性、验证与确认不足[^ralph2020empirical-e404]。
- 写出验证与确认的过程和结果。这些记录对于让读者相信模型及其结果通常至关重要[^sargent2010verification-e18]。
- 公开校准用的原始数据（或合成数据的生成方法）、全部模型和源代码、分析脚本[^ralph2020empirical-e405]。

---

## 3. 检查清单

下面主要依据 SIGSOFT 定量仿真标准，它是为软件工程写的。

**必须做到**

- [ ] 说明为什么仿真适合研究这个问题[^ralph2020empirical-e399]
- [ ] 描述仿真模型（含输入参数和响应变量）、仿真方法、工具版本和计算环境[^ralph2020empirical-e400]
- [ ] 说明校准数据、校准过程和数据背景[^ralph2020empirical-e401]
- [ ] 说明在不同抽象层次上怎样验证和确认模型[^ralph2020empirical-e402]
- [ ] 描述研究方案：自变量、场景、每个场景的运行次数、稳态或终止条件[^ralph2020empirical-e403]
- [ ] 结合数据和模型分析效度威胁；明确写出模型的假设[^ralph2020empirical-e404]

**做到更好**

- [ ] 公开数据（或生成机制）、模型、源代码和分析脚本[^ralph2020empirical-e405]
- [ ] 用已知的取值或分布刻画参考行为（来自真实系统的实测数据），据此定义场景[^ralph2020empirical-e406]
- [ ] 分开描述概念层和实现层；报告敏感性分析；区分有证据的结果和推测[^ralph2020empirical-e407]

**做得出色**

- [ ] 说明数据提供者、领域专家、模型使用者等如何参与建模和确认，例如检查输出是否合理[^ralph2020empirical-e408]

**这些情况可以不做，不算缺陷**

- 校准数据不足或太贵时，部分模型用假设代替；前提是说明并给出理由[^ralph2020empirical-e411]

**审稿时常见、但不成立的批评**：你不必为此担心

- "模型有假设"：只要假设写明、有理由、讨论了影响[^ralph2020empirical-e412]
- "模型太抽象"，却不解释这个抽象层次为什么不够用[^ralph2020empirical-e413]
- 没有合适的一手数据时，因为用了生成数据、二手数据或专家估计就否定研究[^ralph2020empirical-e413]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 模型未经确认就用来下结论 | 结论只能关于模型本身，推不到真实系统[^defranca2015simulation-e8] |
| 把期望的结果写进假设 | 不跑仿真也能"预测"结果，仿真失去意义[^defranca2015simulation-e4] |
| 假设没写出来 | 结果可能被误读，读者无法判断模型是否贴近现实[^defranca2015simulation-e6] |
| 随机模型只跑一次 | 结果可能只是随机波动[^ralph2020empirical-e409][^defranca2015simulation-e2] |
| 稳态仿真不去掉预热期 | 结果带有初始状态的偏差，多跑几次也消除不了[^alexopoulos2002output-e8] |
| 用 A 背景的数据校准，去模拟 B 背景 | 结果的推广范围不会超出支撑数据的范围[^defranca2015simulation-e5][^defranca2015simulation-e9] |
| 反复调参数直到出现想要的结果 | 结论不可信；应当用敏感性分析选参数[^defranca2015simulation-e13] |
| 拿单个仿真值和单个实测值比 | 应当用统计方法比较分布[^defranca2015simulation-e3] |

---

## 5. 延伸阅读

- **ACM SIGSOFT Empirical Standards，Simulation (Quantitative)**：定量仿真的检查清单，含可接受的偏离和不成立的批评。原文在 submodule `repos/acmsigsoft__EmpiricalStandards/docs/standards/QuantitativeSimulation.md`。
- **Sargent 2010，Verification and Validation of Simulation Models**：仿真模型验证与确认的经典教程，列出了各种检验技术和一套推荐的最低步骤。Winter Simulation Conference 论文集，开放获取。
- **de França & Travassos 2015，Simulation Based Studies in Software Engineering: A Matter of Validity**：整理了软件工程仿真研究中的 28 种效度威胁和 7 条建议。开放获取。
- **Alexopoulos & Kim 2002，Output Data Analysis for Simulations**：仿真输出的统计分析：独立重复、预热期、稳态估计。数学较多，适合需要深入时查阅。开放获取。

[^ralph2020empirical-e397]: SIGSOFT 定量仿真标准，定义。[证据](../../sources/notes/ralph2020empirical.md#e397)
[^ralph2020empirical-e398]: SIGSOFT 定量仿真标准，适用范围。[证据](../../sources/notes/ralph2020empirical.md#e398)
[^ralph2020empirical-e399]: SIGSOFT 定量仿真标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e399)
[^ralph2020empirical-e400]: SIGSOFT 定量仿真标准，必要项及脚注 1。[证据](../../sources/notes/ralph2020empirical.md#e400)
[^ralph2020empirical-e401]: SIGSOFT 定量仿真标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e401)
[^ralph2020empirical-e402]: SIGSOFT 定量仿真标准，必要项及脚注 2。[证据](../../sources/notes/ralph2020empirical.md#e402)
[^ralph2020empirical-e403]: SIGSOFT 定量仿真标准，必要项。[证据](../../sources/notes/ralph2020empirical.md#e403)
[^ralph2020empirical-e404]: SIGSOFT 定量仿真标准，必要项及脚注 3。[证据](../../sources/notes/ralph2020empirical.md#e404)
[^ralph2020empirical-e405]: SIGSOFT 定量仿真标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e405)
[^ralph2020empirical-e406]: SIGSOFT 定量仿真标准，加分项及脚注 4。[证据](../../sources/notes/ralph2020empirical.md#e406)
[^ralph2020empirical-e407]: SIGSOFT 定量仿真标准，加分项。[证据](../../sources/notes/ralph2020empirical.md#e407)
[^ralph2020empirical-e408]: SIGSOFT 定量仿真标准，优秀项及脚注 6。[证据](../../sources/notes/ralph2020empirical.md#e408)
[^ralph2020empirical-e409]: SIGSOFT 定量仿真标准，反面模式及脚注 8。[证据](../../sources/notes/ralph2020empirical.md#e409)
[^ralph2020empirical-e410]: SIGSOFT 定量仿真标准，反面模式及脚注 9。[证据](../../sources/notes/ralph2020empirical.md#e410)
[^ralph2020empirical-e411]: SIGSOFT 定量仿真标准，可接受的偏离。[证据](../../sources/notes/ralph2020empirical.md#e411)
[^ralph2020empirical-e412]: SIGSOFT 定量仿真标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e412)
[^ralph2020empirical-e413]: SIGSOFT 定量仿真标准，不成立的批评。[证据](../../sources/notes/ralph2020empirical.md#e413)
[^sargent2010verification-e1]: Sargent 2010，§1。[证据](../../sources/notes/sargent2010verification.md#e1)
[^sargent2010verification-e2]: Sargent 2010，§1。[证据](../../sources/notes/sargent2010verification.md#e2)
[^sargent2010verification-e3]: Sargent 2010，§1。[证据](../../sources/notes/sargent2010verification.md#e3)
[^sargent2010verification-e4]: Sargent 2010，§1。[证据](../../sources/notes/sargent2010verification.md#e4)
[^sargent2010verification-e5]: Sargent 2010，§3。[证据](../../sources/notes/sargent2010verification.md#e5)
[^sargent2010verification-e6]: Sargent 2010，§3。[证据](../../sources/notes/sargent2010verification.md#e6)
[^sargent2010verification-e7]: Sargent 2010，§3。[证据](../../sources/notes/sargent2010verification.md#e7)
[^sargent2010verification-e8]: Sargent 2010，§4。[证据](../../sources/notes/sargent2010verification.md#e8)
[^sargent2010verification-e9]: Sargent 2010，§4。[证据](../../sources/notes/sargent2010verification.md#e9)
[^sargent2010verification-e10]: Sargent 2010，§4。[证据](../../sources/notes/sargent2010verification.md#e10)
[^sargent2010verification-e11]: Sargent 2010，§4。[证据](../../sources/notes/sargent2010verification.md#e11)
[^sargent2010verification-e12]: Sargent 2010，§4。[证据](../../sources/notes/sargent2010verification.md#e12)
[^sargent2010verification-e13]: Sargent 2010，§5。[证据](../../sources/notes/sargent2010verification.md#e13)
[^sargent2010verification-e14]: Sargent 2010，§7。[证据](../../sources/notes/sargent2010verification.md#e14)
[^sargent2010verification-e15]: Sargent 2010，§8。[证据](../../sources/notes/sargent2010verification.md#e15)
[^sargent2010verification-e16]: Sargent 2010，§8.2。[证据](../../sources/notes/sargent2010verification.md#e16)
[^sargent2010verification-e17]: Sargent 2010，§8.2.3。[证据](../../sources/notes/sargent2010verification.md#e17)
[^sargent2010verification-e18]: Sargent 2010，§9。[证据](../../sources/notes/sargent2010verification.md#e18)
[^sargent2010verification-e19]: Sargent 2010，§10。[证据](../../sources/notes/sargent2010verification.md#e19)
[^defranca2015simulation-e1]: de França & Travassos 2015，§2。[证据](../../sources/notes/defranca2015simulation.md#e1)
[^defranca2015simulation-e2]: de França & Travassos 2015，§4.1。[证据](../../sources/notes/defranca2015simulation.md#e2)
[^defranca2015simulation-e3]: de França & Travassos 2015，§4.1。[证据](../../sources/notes/defranca2015simulation.md#e3)
[^defranca2015simulation-e4]: de França & Travassos 2015，§4.2。[证据](../../sources/notes/defranca2015simulation.md#e4)
[^defranca2015simulation-e5]: de França & Travassos 2015，§4.2。[证据](../../sources/notes/defranca2015simulation.md#e5)
[^defranca2015simulation-e6]: de França & Travassos 2015，§4.3。[证据](../../sources/notes/defranca2015simulation.md#e6)
[^defranca2015simulation-e7]: de França & Travassos 2015，§4.3。[证据](../../sources/notes/defranca2015simulation.md#e7)
[^defranca2015simulation-e8]: de França & Travassos 2015，§4.3。[证据](../../sources/notes/defranca2015simulation.md#e8)
[^defranca2015simulation-e9]: de França & Travassos 2015，§4.4。[证据](../../sources/notes/defranca2015simulation.md#e9)
[^defranca2015simulation-e10]: de França & Travassos 2015，§4.2。[证据](../../sources/notes/defranca2015simulation.md#e10)
[^defranca2015simulation-e11]: de França & Travassos 2015，§5。[证据](../../sources/notes/defranca2015simulation.md#e11)
[^defranca2015simulation-e12]: de França & Travassos 2015，§6，建议 1。[证据](../../sources/notes/defranca2015simulation.md#e12)
[^defranca2015simulation-e13]: de França & Travassos 2015，§6，建议 3。[证据](../../sources/notes/defranca2015simulation.md#e13)
[^defranca2015simulation-e14]: de França & Travassos 2015，§6，建议 4。[证据](../../sources/notes/defranca2015simulation.md#e14)
[^defranca2015simulation-e15]: de França & Travassos 2015，§6，建议 7。[证据](../../sources/notes/defranca2015simulation.md#e15)
[^defranca2015simulation-e16]: de França & Travassos 2015，§6。[证据](../../sources/notes/defranca2015simulation.md#e16)
[^defranca2015simulation-e17]: de França & Travassos 2015，§6。[证据](../../sources/notes/defranca2015simulation.md#e17)
[^defranca2015simulation-e18]: de França & Travassos 2015，§7。[证据](../../sources/notes/defranca2015simulation.md#e18)
[^alexopoulos2002output-e1]: Alexopoulos & Kim 2002，§1。[证据](../../sources/notes/alexopoulos2002output.md#e1)
[^alexopoulos2002output-e2]: Alexopoulos & Kim 2002，§1。[证据](../../sources/notes/alexopoulos2002output.md#e2)
[^alexopoulos2002output-e3]: Alexopoulos & Kim 2002，§2。[证据](../../sources/notes/alexopoulos2002output.md#e3)
[^alexopoulos2002output-e4]: Alexopoulos & Kim 2002，§3。[证据](../../sources/notes/alexopoulos2002output.md#e4)
[^alexopoulos2002output-e5]: Alexopoulos & Kim 2002，§3。[证据](../../sources/notes/alexopoulos2002output.md#e5)
[^alexopoulos2002output-e6]: Alexopoulos & Kim 2002，§3。[证据](../../sources/notes/alexopoulos2002output.md#e6)
[^alexopoulos2002output-e7]: Alexopoulos & Kim 2002，§4.1。[证据](../../sources/notes/alexopoulos2002output.md#e7)
[^alexopoulos2002output-e8]: Alexopoulos & Kim 2002，§4.1。[证据](../../sources/notes/alexopoulos2002output.md#e8)
