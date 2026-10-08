# 理论研究：证明与形式化分析

本文讲**以定理和证明为主要成果的研究**：例如证明一个算法的复杂度上界或下界、证明一个协议在某种攻击者模型下是安全的、用形式化方法证明一个系统满足某个性质。

**适用范围** `[本项目分析]`：这是理论计算机，以及软件工程、系统、安全中形式化方向的做法，属于[证明](../../../05_research-strategies/prove.md)这种研究套路。证明产生什么知识、审稿人要看到哪些证据（假设写全、证明完整、别人能检查、要不要机器检查、假设离现实多远），这些通用部分见套路页；本文讲在计算机里怎样选题、推进、写和检查证明。

如果你的主要成果是一个造出来的系统或工具，用实验说明它好用，见[工程研究](engineering_research.md)；如果是在统一的任务上比较多种方法的性能，见[基准评测](benchmarking.md)。很多论文两者都有：证明部分看本文，实验部分看[构建改进](../../../05_research-strategies/build_improve.md)。

**关于依据**：ACM SIGSOFT 实证标准（Empirical Standards，软件工程领域的研究评审标准）面向实证研究，**没有理论研究的标准**。本文的做法和检查清单是根据 Lamport、Tao、Aaronson 等人的文章整理的 `[本项目分析]`。其中 Tao 和 Lamport 的很多建议写给数学家，适用于一切以证明为成果的工作，文中标为〔数学通用〕；只在计算机领域成立的做法标为〔计算机〕。

**读完本文，你应该能：**

- 说清理论研究产出什么，和工程研究、基准评测有什么区别；
- 选一个合适的问题，并确认它确实没被解决、定义没有选错；
- 在证明卡住时用几种固定的办法推进；
- 把证明写成别人（和你自己）能逐步检查的形式，并在投稿前查出自己的错误。

---

## 1. 这是什么研究，什么时候用

理论研究的成果是**对所有满足假设的情况都成立的结论**，而不是"在我们测的这些数据上成立"。常见的成果有四类 `[本项目分析]`：

| 成果 | 例子 | 回答的问题 |
|---|---|---|
| 上界（算法与分析） | 某算法在最坏情况下的运行时间不超过 O(n log n) | 能做到多好？ |
| 下界、不可能性结果 | 任何基于比较的排序在最坏情况下都至少要做约 n log n 次比较 | 最好也只能做到多好？什么根本做不到？ |
| 模型和定义 | 一种新的计算模型，或一个新的安全定义 | 该用什么概念来描述这个问题？ |
| 形式化保证 | 协议在某攻击者模型下满足保密性；用机器检查过的证明说明某个算法正确 | 在明确的假设下，系统一定满足某个性质吗？ |

和相近类型的区别 `[本项目分析]`：

| | 理论研究 | 工程研究 | 基准评测 |
|---|---|---|---|
| 主要证据 | 证明 | 造出来的系统 + 实验 | 在统一任务上的测量 |
| 结论的范围 | 满足假设的所有情况 | 实验覆盖的情况 | 基准覆盖的情况 |
| 最大的风险 | 证明有错；模型或假设离实际太远 | 实验不公平、不可复现 | 基准不代表实际 |

**什么时候用**：你的问题是"能不能""最多/最少要多少""是否一定成立"时，用证明来回答。

〔计算机〕算法证明有它的特点：Lamport（Leslie Lamport，分布式系统和形式化方法研究者）指出，算法的证明往往数学上不深，但很繁杂，有大量细节要检查[^lamport2012how-e10]；在数学定理里无伤大雅的遗漏假设（例如"集合非空"），放到算法里可能就是严重的缺陷[^lamport2012how-e9]。

---

## 2. 怎么做

### 第 1 步：选题，并确认问题还开着、定义没选错 〔数学通用〕

**怎么做：**

1. **先做可行的问题，不要一上来死磕著名难题。** Tao（陶哲轩，数学家）指出，著名难题几乎从不是凭空解决的[^taocareer-e13]；他建议把大部分时间放在更可行的"低垂的果实"上，积累经验、能力和信誉，等准备好了再做更有雄心的项目[^taocareer-e14]。Hamming（Richard Hamming，贝尔实验室的数学家）的说法是：问题重要，不在于结果有多大，而在于你有合理的切入办法[^hamming1986you-e2]。一般的选题方法见[找到候选问题](../../../01_from-interest-to-project/02_find-problems.md)。
2. **确认问题仍然开放。** 找到这个问题的关键论文，查有哪些后续论文引用了它[^taocareer-e16]，看是否已经有人解决、改进或否定了它。也要查有没有相关的**下界和不可能性结果**：和已知不可能性结果冲突却不提它，是错误"突破"的典型信号[^aaronson2008ten-e3]。拿不准时问导师或这个方向的专家 `[本项目分析]`。查文献的方法见[读文献与文献调研](../../../01_from-interest-to-project/01_enter-a-field.md)。
3. **确认你用的定义就是大家用的定义。** 写下问题的精确陈述，和标准文献逐字对照：计算模型、输入规模怎么算、攻击者能做什么、"安全"指什么 `[本项目分析]`。记号也要尽量和已有文献一致[^taowriting-e8]。

**容易错在哪：** 把问题理解错了——Aaronson（Scott Aaronson，理论计算机科学家）把"作者没弄懂问题本身"列为错误"突破"的信号之一[^aaronson2008ten-e1]。更常见的是定义和标准版本差一点：你证明的是一个更弱或不同的命题，自己却没发现 `[本项目分析]`。

### 第 2 步：推进证明 〔数学通用〕

卡住时，按下面的顺序试：

- **先看例子和特殊情形。** Tao 描述的推进过程里，有一步是分离出大问题的"玩具模型"（简化的特殊情形）[^taocareer-e5]。手边要有一批反例和容易分析的模型情形，并知道你的工具能处理哪些障碍、哪些完全无望[^taocareer-e9]。
- **试着反驳它。** 要证一个大胆的命题，先找反例：找到了，省下大量时间，反例本身也可能值得发表；找不到，遇到的障碍会告诉你证明该怎么做[^taocareer-e2]。
- **改动问题。** 去掉一个假设会怎样？结论能不能加强？[^taocareer-e8] 对你要用的每个引理，弄清每个假设为什么必要[^taocareer-e17]。
- **找类似的已知结果。** 发现特殊情形和另一个领域的问题相似时，去查那个问题的文献，请教那个领域的专家[^taocareer-e21]。
- **重视部分进展。** 一种方法只解决了一部分，不等于失败[^taocareer-e6]；即使注定失败，它具体卡在哪一步也很有启发[^taocareer-e7]。很多中间步骤本身就是可发表的论文[^taocareer-e22]。
- **把论证写下来，失败的也留着。** 有意思的论证写成草稿，详细到日后能恢复[^taocareer-e18]；错得难堪的尝试也私下存档，也许以后能从中挽救出东西[^taocareer-e19]。记研究日志的做法见[推进研究](../../../03_conduct-and-analyze/01_run-and-iterate.md)。

### 第 3 步：把证明写得可以检查 〔数学通用〕

**先定义，再陈述，再证明。**

- 全文通用的记号在前面集中定义；只在局部用的记号在用到的地方附近定义[^taowriting-e9]。
- 用到三次以上的表达式才值得引入记号，只用一次的通常不需要[^taowriting-e7]；避免花哨的记号[^taowriting-e10]。
- 关键术语必须精确定义[^taowriting-e11]。否则一个表达式可能有两种解释，论证前后各用了一种，错误就很难定位到某一步 `[本项目分析]`。

**把所有假设写出来。** 连教材里的定理也会带着没写出的假设[^lamport2012how-e6]。引理是重新列明当前所有假设和记号的好时机[^taowriting-e2]；每次使用假设都写明，日后需要弱化某个假设时，搜一下就知道它用在哪里[^lamport1995how-e4]。

**用结构化证明。** Lamport 的做法基于两条原则：结构和命名[^lamport2012how-e1]。把证明写成编号的步骤，每步下面是它自己的证明，可以继续分层；每个证明的最后一步，都陈述它要证的命题本身[^lamport2012how-e4]。示意（格式仿 Lamport，最后一步记作 Q.E.D. `[本项目分析]`）：

```
定理：（完整陈述，含全部假设）
证明概要：（两三句话说明思路）
<1>1. （第一个中间结论）
  证明：（理由，或继续分成 <2>1、<2>2……）
<1>2. （第二个中间结论）
  证明：由 <1>1 和引理 3。
<1>3. Q.E.D.
  证明：由 <1>1、<1>2。
```

- **展开到什么程度**：展开到最底层每句话都显然成立，然后再多展开一层[^lamport1995how-e6]。大多数错误来自证明没有展开到足够的层次[^lamport1995how-e5]。
- **不接受"这种情况与前一种类似"**，要找出能同时处理两种情况的一般性步骤[^lamport1995how-e7]。
- **把长证明拆成引理**，引理的陈述要便于使用，而不是便于证明[^taowriting-e1]。
- **先写骨架。** 先写出所有关键定义和定理的（大致）陈述，证明只留草记，结构定了再补细节[^taowriting-e16]。
- **没证明的断言要说明。** 不加证明也不加引用地断言一个非平凡命题时，要明确告诉读者[^taowriting-e5]。

入门办法：拿一个已有的简单证明改写成结构化形式，再逐步尝试更长的[^lamport2012how-e14]。

### 第 4 步：检查自己的证明 〔数学通用，机器检查部分为计算机〕

**先接受"你的证明很可能有错"。** Lamport 引述过传闻性的说法：数学期刊上多达三分之一的论文有错误，不只是小错，而是错误的定理和证明[^lamport1995how-e1]（这是传闻，不是统计）。他自己改写 Kelley 教材里的一个证明，写到第五页时发现 Kelley 的原证明是错的[^lamport1995how-e3]。为自己检查证明时，唯一的办法是对自己相信的一切都毫不留情地怀疑[^lamport2012how-e7]。

**全局检查：不看细节，先看整体是否可疑。** 全局反驳指的是：说明这个证明如果成立，会推出已知为假或极可能为假的结论[^taowriting-e12]。几个问法：

- 这个方法是否也能"证明"一个已知为假的更强命题？能的话，方法有漏洞[^taocareer-e1]。例如一个"证明 3SAT 需要指数时间"的论证，如果同样适用于有多项式时间算法的 2SAT，它一定错了[^aaronson2008ten-e2]。
- 证明有没有实质用到每个关键假设？没用到某个假设是危险信号[^taowriting-e13]。
- 反证法：去掉"假设结论不成立"再跑一遍，如果仍能推出矛盾，错在论证本身[^taocareer-e3]。
- 你是否只是在专家常用的方法上加了一个"大家都没想到"的小改动？Tao 把这列为警示信号[^taocareer-e4]。

找错时用直觉和不严格的推理完全可以，构造证明时才要求严格[^taowriting-e15]。

**局部检查：逐步过。** 想象身边坐着一个好奇的孩子，每写一个断言他就问"为什么"[^lamport2012how-e5]。检验是否真懂：能不能把论证给同学讲清楚[^taocareer-e20]。隔几天再读、请同学或导师读，也是让自己换一双眼睛的办法 `[本项目分析]`。结构化本身不保证没有错误，仍然需要细心[^lamport2012how-e11]。

**让证明经得起局部错误。** 组织证明时，尽量让某一步出错不至于全盘崩溃，还能留下有价值的部分结果[^taowriting-e14]。

**〔计算机〕什么时候用证明助手（proof assistant，能逐步检查形式化证明的软件，如 TLA+ 的证明系统 TLAPS）。** 把数学形式化不难，但写出机器能检查的证明并不容易[^lamport2012how-e8]。所以它不是每篇论文的必需品；更值得用的场合是细节繁多、遗漏一个假设就会变成缺陷的证明，例如并发算法、协议和系统正确性 `[本项目分析]`，依据见[^lamport2012how-e10][^lamport2012how-e9]。即使不用，学会写形式化证明也能教会你写普通证明[^lamport2012how-e3]。

### 第 5 步：直觉和形式一起给 〔数学通用〕

严谨不是为了消灭直觉，而是消灭坏直觉、提升好直觉[^taocareer-e11]；形式处理细节，直觉把握全局，两者缺一不可[^taocareer-e12]。写论文时：

- **每个主要证明前给一段概要**，作为读者的"路线图"[^lamport1995how-e2]。长证明的开头用几句话说明思路，Lamport 引用的一位审稿人就这样建议[^lamport2012how-e12]。但概要不是证明[^lamport2012how-e13]。
- **能不能用高层的话说清论证为什么成立？** 说不清，是一个危险信号[^taocareer-e15]。
- **详略有别**：新的、关键的部分多用文字解释，常规部分简短[^taowriting-e6]。
- **准确描述结果**：不说小也不说大[^taowriting-e3]；假设偏强、结论偏弱的地方坦白写出[^taowriting-e4]；讨论所用工具的已知局限[^taocareer-e10]。

> **不同的看法：证明该写多细？**
> - **Lamport**：展开到显然之后再多一层[^lamport1995how-e6]；结构化证明更长，主要是因为包含了更多细节[^lamport1995how-e9]。他建议准备两个版本：给自己、审稿人和感兴趣同行的详细版，以及正式发表的简略版[^lamport1995how-e8]。
> - **Tao**：论文应在最重要、最新的部分多花笔墨，在常规、标准的部分从简[^taowriting-e6]。
>
> 两者并不矛盾：**为自己检查时写到最细；给读者看时详略有别**。计算机会议论文有页数限制，常见做法是正文给关键证明和概要，完整证明放附录或预印本上的完整版 `[本项目分析]`。

### 第 6 步：投稿：会议与期刊 〔计算机〕

计算机领域以会议为主要发表渠道；理论方向也看重会议，但有把会议论文补全、扩展后再投期刊的长期传统[^cra1999evaluating-e4]。整体情况见[学科概况](../README.md)。几点提醒 `[本项目分析]`：

- 会议版篇幅有限，完整证明要有地方放（附录或完整版），审稿人需要时能查到；
- 期刊版不只是加页数，是把会议版里省略或压缩的证明补全、改正；
- 不要把一次拒稿看得太重：近一半哥德尔奖（理论计算机最佳论文奖）获奖论文最初被顶级理论会议拒过，或根本没在那里发表[^fortnow2009time-e8]。

投稿见[选择发表渠道与投稿](../../../04_write-and-publish/02_venue-and-submission.md)，回复审稿意见见[审稿意见、修改与被拒之后](../../../04_write-and-publish/03_review-and-revision.md)。

---

## 3. 检查清单

SIGSOFT 实证标准没有理论研究的标准，下面的清单根据本文资料整理 `[本项目分析]`。

**必须做到**

- [ ] 每个定理的陈述完整，所有假设都写出来[^lamport2012how-e6][^taowriting-e2]
- [ ] 定义、模型和记号与领域通用版本一致；不一致的地方明确说明[^taowriting-e8]
- [ ] 查过相关的已知结果，特别是下界和不可能性结果，并说明你的结果与它们的关系[^aaronson2008ten-e3][^aaronson2008ten-e5]
- [ ] 每个非显然的步骤都有理由；不加证明的断言明确标出[^taowriting-e5]
- [ ] 做过全局检查：证明没有"顺便"推出已知为假的结论，每个关键假设都用到了[^taocareer-e1][^taowriting-e13]
- [ ] 准确描述结果，写出局限[^taowriting-e3][^taowriting-e4]

**做到更好**

- [ ] 用结构化证明，每个主要证明前有概要[^lamport2012how-e1][^lamport1995how-e2]
- [ ] 用例子或反例说明关键假设为什么必要[^taocareer-e17]
- [ ] 公开详细版证明（附录或完整版）[^lamport1995how-e8]
- [ ] 细节繁多、出错代价大的证明，考虑用证明助手检查[^lamport2012how-e10]

**这些情况可以不做，不算缺陷**

- 不是每个证明都需要机器检查，写机器可检查的证明代价很高[^lamport2012how-e8]。
- 不必一次解决整个问题：特殊情形、部分结果、反例本身都可能值得发表[^taocareer-e22][^taocareer-e2]。
- 结论纯粹是理论性的（例如下界），不必配实验 `[本项目分析]`。

**审稿时常见、但不成立的批评**

- "证明太长了"：如果长是因为补全了细节，这是严谨的代价，不是缺陷[^lamport1995how-e9]。（但"太长"也可能说明结构不清，值得检查 `[本项目分析]`。）
- "没有实验验证"：对纯理论结论不成立 `[本项目分析]`。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 证明了一个和你需要的不一样的命题（定义差一点、模型不同） | 结论看似成立，其实回答的不是原问题[^aaronson2008ten-e1] |
| 隐含假设没写出来 | 在算法里，一个遗漏的假设可能就是严重缺陷[^lamport2012how-e9] |
| 证明"太强"：同样的论证也能推出已知为假的结论 | 说明论证有漏洞[^aaronson2008ten-e2][^taocareer-e1] |
| 某个关键假设从头到尾没用到 | 全局错误的信号[^taowriting-e13] |
| 写"这种情况类似，从略" | Lamport 认为这不可接受，应找出能同时处理两种情况的一般性步骤[^lamport1995how-e7] |
| 把证明概要当证明 | 概要说明思路，但不能代替逐步论证[^lamport2012how-e13] |
| 记号过多、过于花哨 | Tao 建议只为反复用到的表达式引入记号，并避免花哨的记号[^taowriting-e7][^taowriting-e10]；否则读者要不停回头查 `[本项目分析]` |
| 摘要说"我们证明了"，结尾变成"看起来可行" | 证明退化成了"有道理的论证"，是错误的典型信号[^aaronson2008ten-e4] |
| 新手直接死磕著名难题 | 几乎没有难题是凭空解决的[^taocareer-e13]；容易长期没有产出 `[本项目分析]` |

---

## 5. 延伸阅读

- **Lamport 1995，How to Write a Proof**：短小，讲清结构化证明的写法和"展开到显然再多一层"的规则。适合第一次认真写长证明的人。
- **Lamport 2012，How to Write a 21st Century Proof**：结构化证明的更新版，含作者二十年的经验和一个机器检查证明的例子。适合想了解证明助手的人。
- **Tao 的 Career advice 和 On writing 两组网页**：每页一条建议，很短。"Be sceptical of your own work""On the importance of partial progress"讲推进和自查，"Use good notation""Create lemmas""On local and global errors"讲写作和找错。
- **Aaronson 2008，Ten Signs a Claimed Mathematical Breakthrough is Wrong**：理论计算机视角的十个"错误信号"。适合投稿前拿来自查；作者也强调这些只是启发式，没通过不一定错，全部通过也不一定对[^aaronson2008ten-e6]。
- **Hamming 1986，You and Your Research**：讲怎么选重要且有切入办法的问题，见[找到候选问题](../../../01_from-interest-to-project/02_find-problems.md)。

[^lamport2012how-e1]: Lamport 2012，§1。[证据](../../../../sources/notes/lamport2012how.md#e1)
[^lamport2012how-e3]: Lamport 2012，§1。[证据](../../../../sources/notes/lamport2012how.md#e3)
[^lamport2012how-e4]: Lamport 2012，§2。[证据](../../../../sources/notes/lamport2012how.md#e4)
[^lamport2012how-e5]: Lamport 2012，§3。[证据](../../../../sources/notes/lamport2012how.md#e5)
[^lamport2012how-e6]: Lamport 2012，§3 脚注 1。[证据](../../../../sources/notes/lamport2012how.md#e6)
[^lamport2012how-e7]: Lamport 2012，§3。[证据](../../../../sources/notes/lamport2012how.md#e7)
[^lamport2012how-e8]: Lamport 2012，§4.5。[证据](../../../../sources/notes/lamport2012how.md#e8)
[^lamport2012how-e9]: Lamport 2012，§5。[证据](../../../../sources/notes/lamport2012how.md#e9)
[^lamport2012how-e10]: Lamport 2012，§5。[证据](../../../../sources/notes/lamport2012how.md#e10)
[^lamport2012how-e11]: Lamport 2012，§5。[证据](../../../../sources/notes/lamport2012how.md#e11)
[^lamport2012how-e12]: Lamport 2012，§5（引用的审稿意见）。[证据](../../../../sources/notes/lamport2012how.md#e12)
[^lamport2012how-e13]: Lamport 2012，§6。[证据](../../../../sources/notes/lamport2012how.md#e13)
[^lamport2012how-e14]: Lamport 2012，§7。[证据](../../../../sources/notes/lamport2012how.md#e14)
[^lamport1995how-e1]: Lamport 1995，§1。[证据](../../../../sources/notes/lamport1995how.md#e1)
[^lamport1995how-e2]: Lamport 1995，§2.1。[证据](../../../../sources/notes/lamport1995how.md#e2)
[^lamport1995how-e3]: Lamport 1995，§4.1。[证据](../../../../sources/notes/lamport1995how.md#e3)
[^lamport1995how-e4]: Lamport 1995，§4.1。[证据](../../../../sources/notes/lamport1995how.md#e4)
[^lamport1995how-e5]: Lamport 1995，§4.2。[证据](../../../../sources/notes/lamport1995how.md#e5)
[^lamport1995how-e6]: Lamport 1995，§4.2。[证据](../../../../sources/notes/lamport1995how.md#e6)
[^lamport1995how-e7]: Lamport 1995，§4.2。[证据](../../../../sources/notes/lamport1995how.md#e7)
[^lamport1995how-e8]: Lamport 1995，§4.2。[证据](../../../../sources/notes/lamport1995how.md#e8)
[^lamport1995how-e9]: Lamport 1995，§4.2。[证据](../../../../sources/notes/lamport1995how.md#e9)
[^taocareer-e1]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e1)
[^taocareer-e2]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e2)
[^taocareer-e3]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e3)
[^taocareer-e4]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e4)
[^taocareer-e5]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e5)
[^taocareer-e6]: Tao，Career advice："On the importance of partial progress"。[证据](../../../../sources/notes/taocareer.md#e6)
[^taocareer-e7]: Tao，Career advice："On the importance of partial progress"。[证据](../../../../sources/notes/taocareer.md#e7)
[^taocareer-e8]: Tao，Career advice："Ask yourself dumb questions"。[证据](../../../../sources/notes/taocareer.md#e8)
[^taocareer-e9]: Tao，Career advice："Learn the limitations of your tools"。[证据](../../../../sources/notes/taocareer.md#e9)
[^taocareer-e10]: Tao，Career advice："Learn the limitations of your tools"。[证据](../../../../sources/notes/taocareer.md#e10)
[^taocareer-e11]: Tao，Career advice："There's more to mathematics than rigour and proofs"。[证据](../../../../sources/notes/taocareer.md#e11)
[^taocareer-e12]: Tao，Career advice："There's more to mathematics than rigour and proofs"。[证据](../../../../sources/notes/taocareer.md#e12)
[^taocareer-e13]: Tao，Career advice："Don't base career decisions on glamour or fame"。[证据](../../../../sources/notes/taocareer.md#e13)
[^taocareer-e14]: Tao，Career advice："Don't prematurely obsess on a single big problem or big theory"。[证据](../../../../sources/notes/taocareer.md#e14)
[^taocareer-e15]: Tao，Career advice："Don't prematurely obsess on a single big problem or big theory"，附录。[证据](../../../../sources/notes/taocareer.md#e15)
[^taocareer-e16]: Tao，Career advice："Learn and relearn your field"。[证据](../../../../sources/notes/taocareer.md#e16)
[^taocareer-e17]: Tao，Career advice："Learn and relearn your field"。[证据](../../../../sources/notes/taocareer.md#e17)
[^taocareer-e18]: Tao，Career advice："Write down what you've done"。[证据](../../../../sources/notes/taocareer.md#e18)
[^taocareer-e19]: Tao，Career advice："Use the wastebasket"。[证据](../../../../sources/notes/taocareer.md#e19)
[^taocareer-e20]: Tao，Career advice："Solving mathematical problems"。[证据](../../../../sources/notes/taocareer.md#e20)
[^taocareer-e21]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e21)
[^taocareer-e22]: Tao，Career advice："Be sceptical of your own work"。[证据](../../../../sources/notes/taocareer.md#e22)
[^taowriting-e1]: Tao，On writing："Create lemmas"。[证据](../../../../sources/notes/taowriting.md#e1)
[^taowriting-e2]: Tao，On writing："Create lemmas"。[证据](../../../../sources/notes/taowriting.md#e2)
[^taowriting-e3]: Tao，On writing："Describe the results accurately"。[证据](../../../../sources/notes/taowriting.md#e3)
[^taowriting-e4]: Tao，On writing："Describe the results accurately"。[证据](../../../../sources/notes/taowriting.md#e4)
[^taowriting-e5]: Tao，On writing："Describe the results accurately"。[证据](../../../../sources/notes/taowriting.md#e5)
[^taowriting-e6]: Tao，On writing："Give appropriate amounts of detail"。[证据](../../../../sources/notes/taowriting.md#e6)
[^taowriting-e7]: Tao，On writing："Use good notation"。[证据](../../../../sources/notes/taowriting.md#e7)
[^taowriting-e8]: Tao，On writing："Use good notation"。[证据](../../../../sources/notes/taowriting.md#e8)
[^taowriting-e9]: Tao，On writing："Use good notation"。[证据](../../../../sources/notes/taowriting.md#e9)
[^taowriting-e10]: Tao，On writing："Use good notation"。[证据](../../../../sources/notes/taowriting.md#e10)
[^taowriting-e11]: Tao，On writing："On local and global errors in mathematical papers"。[证据](../../../../sources/notes/taowriting.md#e11)
[^taowriting-e12]: Tao，On writing："On local and global errors in mathematical papers"。[证据](../../../../sources/notes/taowriting.md#e12)
[^taowriting-e13]: Tao，On writing："On local and global errors in mathematical papers"。[证据](../../../../sources/notes/taowriting.md#e13)
[^taowriting-e14]: Tao，On writing："On local and global errors in mathematical papers"。[证据](../../../../sources/notes/taowriting.md#e14)
[^taowriting-e15]: Tao，On writing："On local and global errors in mathematical papers"。[证据](../../../../sources/notes/taowriting.md#e15)
[^taowriting-e16]: Tao，On writing："Write a rapid prototype first"。[证据](../../../../sources/notes/taowriting.md#e16)
[^aaronson2008ten-e1]: Aaronson 2008，第 2 条。[证据](../../../../sources/notes/aaronson2008ten.md#e1)
[^aaronson2008ten-e2]: Aaronson 2008，第 3 条。[证据](../../../../sources/notes/aaronson2008ten.md#e2)
[^aaronson2008ten-e3]: Aaronson 2008，第 4 条。[证据](../../../../sources/notes/aaronson2008ten.md#e3)
[^aaronson2008ten-e4]: Aaronson 2008，第 5 条。[证据](../../../../sources/notes/aaronson2008ten.md#e4)
[^aaronson2008ten-e5]: Aaronson 2008，第 7 条。[证据](../../../../sources/notes/aaronson2008ten.md#e5)
[^aaronson2008ten-e6]: Aaronson 2008，结尾。[证据](../../../../sources/notes/aaronson2008ten.md#e6)
[^hamming1986you-e2]: Hamming 1986，"important problems" 一段。[证据](../../../../sources/notes/hamming1986you.md#e2)
[^cra1999evaluating-e4]: Patterson、Snyder & Ullman 1999（CRA 备忘录），Structure of The Field。[证据](../../../../sources/notes/cra1999evaluating.md#e4)
[^fortnow2009time-e8]: Fortnow 2009，正文。[证据](../../../../sources/notes/fortnow2009time.md#e8)
