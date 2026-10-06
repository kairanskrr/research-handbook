# van der Kouwe 等人 2019：SoK: Benchmarking Flaws in Systems Security

- 资料：`vanderkouwe2019sok`，[原文](https://trustworthy.systems/publications/full_text/vanderKouwe_HABG_19.pdf)
- 版本：IEEE EuroS&P 2019，本地 PDF `papers/pdf/vanderkouwe2019sok.pdf`。
- 说明：面向系统安全方向的性能评估，列出 22 种基准测试缺陷（文中编号 A1–F4），多数也适用于系统、程序语言等其他方向。

### E1

- 位置：Abstract
- 原文："tier-1 papers contain an average of five benchmarking flaws and we find only a single paper in our sample without any benchmarking flaws"
- 要点：50 篇顶会防御论文平均每篇有 5 个基准测试缺陷，只有 1 篇没有。

### E2

- 位置：§II-A Selective benchmarking（A1）
- 原文："we should always include benchmarks that evaluate all operations whose performance one might reasonably expect to be impacted"
- 要点：凡是可以合理预期会受影响的操作，都要有对应的测试，不能只测对自己有利的部分。

### E3

- 位置：§II-A Selective benchmarking（A2）
- 原文："Any paper which arbitrarily selects a subset of benchmarks and presents it as a single overall performance overhead number as if it is still representative contains benchmarking flaw A2"
- 要点：随意挑一部分基准子项，却把结果当作有代表性的整体开销来报告，是一种缺陷。

### E4

- 位置：§II-D Improper comparison of benchmarking results（D2、D3）
- 原文："D2: only evaluate against yourself refers to cases where papers compare their new system to their own earlier work rather than the state of the art." / "D3: unfair benchmarking of competitors refers to papers that do compare against competitors but do so in an unfair way. For example, they might use a configuration that is not optimal."
- 要点：只和自己以前的工作比、不和当前最好的方法比；或者和对手比，但给对手用不是最优的配置，都是缺陷。

### E5

- 位置：§II-E Benchmarking omissions（E1）
- 原文："E1: not all contributions evaluated refers to cases where a paper claims to achieve a certain goal, but does not empirically determine whether this goal has been reached."
- 要点：声称达到了某个目标，却没有用实验检验是否真的达到，是一种缺陷。

### E6

- 位置：附录，E2 Only measure run-time overhead
- 原文："performance measurements are not complete without measuring memory overhead" / "Other missing measurements include the amount of extra network and/or disk IO, increased binary size after instrumentation, and the time taken to instrument the protected program."
- 要点：只测运行时间不够，还要测内存开销，以及额外的网络和磁盘读写、程序体积增加、处理所需时间等代价。

### E7

- 位置：§II-E Benchmarking omissions（E3）
- 原文："Without knowing how accurate the system is, it is impossible to judge its value, making the paper incomplete."
- 要点：系统需要做判断时（如判断行为是否恶意），必须测误报和漏报；不知道准确率，就无法判断它的价值。

### E8

- 位置：§II-E Benchmarking omissions（E4）
- 原文："If the system is faster than the state of the art merely due to a faster implementation rather than the newly designed optimizations, its novelty is questionable."
- 要点：不逐个测量各组成部分的作用，就不知道每部分是否必要；如果比别人快只是因为实现得更好，而不是因为新设计，新颖性就值得怀疑。

### E9

- 位置：§II-B Improper handling of benchmark results（B1）
- 原文："they are not an indication of how fast the system would run in practice. For this purpose, more realistic system benchmarks are needed."
- 要点：微基准（只测某个具体操作的测试）不能代表系统在实际中的整体速度，需要更贴近实际的系统级测试。

### E10

- 位置：§II-C Using the wrong benchmarks（C3）
- 原文："when they benchmark their system using the same data set that they used to train it or, more generally, if there is any overlap between the training and test sets"
- 要点：用调校或训练系统时用过的数据来评估它，是一种缺陷。

### E11

- 位置：§VI Recommendations
- 原文："authors should consider which performance dimensions the solution could possibly affect (for example, CPU, concurrency, memory, IO, system calls" / "and include at least one appropriate benchmark for each dimension."
- 要点：先列出方案可能影响的所有性能维度，每个维度至少用一个合适的测试。

### E12

- 位置：§I Introduction
- 原文："We believe that most, if not all, benchmarking flaws we found are unintentional" / "many prevalent benchmarking flaws we found can, in fact, be prevented altogether with little effort and simple benchmarking practices."
- 要点：作者认为这些缺陷大多不是故意的，而且很多只需很少的额外工作就能避免。

### E13

- 位置：§II，Table I
- 原文："F1 Missing platform specification F2 Missing software versions F3 Subbenchmarks not listed F4 Relative numbers only"
- 要点：可复现性方面的缺陷：没写硬件平台、没写软件版本、没列出各子项结果、只给相对数字不给绝对数字。

### E14

- 位置：§II-D Improper comparison of benchmarking results（D1）
- 原文："In systems defenses, the proper baseline is usually the original system using default settings with no defenses enabled."
- 要点：（系统安全方向）计算开销时，合适的基线通常是使用默认设置、不加任何防御的原始系统；在基线上偷偷加东西会把开销藏进基线。

### E15

- 位置：§IV Survey Results
- 原文："The lack of indication of significance of data and benchmark subsetting without proper justification are by far the most widespread, respectively affecting 80% and 69% of the applicable papers we surveyed."
- 要点：最普遍的两种缺陷是不给出数据的显著性（波动）指标（80%）和无正当理由地裁剪基准套件（69%）。

### E16

- 位置：§II Benchmarking Flaws
- 原文："it should be complete in the sense that it verifies all claimed contributions of the system and shows the extent of any negative impact the system may have." / "soundness, the requirement that all numbers measure what is intended with reasonable accuracy and repeatability"
- 要点：好的评估要满足：完整（验证所有声称的贡献，并展示负面影响有多大）、相关、可靠（每个数字以合理的精度和可重复性测到了想测的东西）、可复现。

### E17

- 位置：§VI Recommendations；§II-A
- 原文："Authors should run all subbenchmarks that can reasonably be run and be explicit about reasons for omitting the others." / "a subset arbitrarily selected from a large set of tests is unlikely to be representative of the full set"
- 要点：能合理运行的子基准都要跑，并明确说明省略其他子基准的原因；也不要把子集的总体结果当成可以和别人比较的完整结果。从大量测试中随意挑出的子集不太可能代表全体。

### E18

- 位置：§II-A，A3
- 原文："if throughput seems to scale linearly with the number of concurrent connections, it suggests that the range of this variable is too restricted because the system cannot keep this up forever."
- 要点：如果吞吐量看起来随并发连接数线性增长，说明测量的参数范围太窄了，系统不可能一直这样增长下去。

### E19

- 位置：§II-D，D1；§VI
- 原文："In systems defenses, the proper baseline is usually the original system using default settings with no defenses enabled." / "Often, this means avoiding any non-default compiler flags or emulation techniques that would slow down the baseline."
- 要点：系统防御研究中，正确的基线通常是使用默认设置、不启用防御的原系统；不要给基线加非默认编译选项或模拟手段，把基线拖慢、把开销藏进基线。

### E20

- 位置：§II-E，E2 与 E4
- 原文："A paper contains benchmarking flaw E2: only measure run-time overhead and its evaluation is incomplete whenever it does not measure important performance characteristics." / "If the system is faster than the state of the art merely due to a faster implementation rather than the newly designed optimizations, its novelty is questionable."
- 要点：只测运行时间开销、不测内存等其他重要性能特征，评估不完整；可选组件要单独测，否则系统更快可能只是因为实现更快，而不是新设计起了作用。

### E21

- 位置：§VI Recommendations
- 原文："flaws B4 (no indication of significance of data), B5 (incorrect averaging across benchmark scores), F1 (missing platform specification), and F2 (missing software versions) can be addressed by simply adding readily available data to the paper."
- 要点：不给波动指标、跨基准平均方法错误、缺少平台说明、缺少软件版本，这几种缺陷只要把手头已有的数据补进论文就能解决。

### E22

- 位置：§II-B，B5
- 原文："Only the geometric mean is appropriate for averaging overhead ratios."
- 要点：对开销比值求平均，只有几何平均是合适的；算术平均的结果取决于选哪个配置作基线。

### E23

- 位置：§II-F，F4
- 原文："The absolute numbers are valuable for the reader to perform a sanity check (is the system configured in a reasonable way?) and because a slow baseline often means overhead will be less visible."
- 要点：除了相对开销，还要给出绝对数：读者可以借此做合理性检查（系统配置得合理吗？），而且基线慢时开销往往显得更小。

### E24

- 位置：§II-B，B3
- 原文："the difference between 10% overhead and 20% overhead is presented as 10% more overhead, while it is actually 100% more"
- 要点：算错的典型例子：把 10% 到 20% 的开销说成"多了 10%"，实际上是多了 100%。

### E25

- 位置：§I Introduction
- 原文："We believe that most, if not all, benchmarking flaws we found are unintentional and just denote insufficient attention devoted to performance benchmarking in our community."
- 要点：作者认为这些缺陷大多不是故意的，只是对性能评测重视不够。

### E26

- 位置：Abstract
- 原文："we identify 22 benchmarking flaws that threaten the validity of systems security evaluations, and survey 50 defense papers published in top venues." / "tier-1 papers contain an average of five benchmarking flaws and we find only a single paper in our sample without any benchmarking flaws"
- 要点：作者整理出 22 种威胁评估效度的基准测试缺陷，调查了 50 篇顶会防御论文：平均每篇 5 个缺陷，只有 1 篇没有。

### E27

- 位置：§I Introduction；§III-B Selected venues
- 原文："For this purpose, we selected all defense papers with benchmarking results published in 2010 and 2015." / "the “top 4” venues are the most influential and de-facto set the standard for benchmarking practices in the community."
- 要点：样本：四个顶级安全会议在 2010 年和 2015 年发表的、带基准测试结果的全部防御论文；选这四个会议，是因为它们最有影响力，事实上决定了领域的评测惯例。

### E28

- 位置：§III-A Classification methodology
- 原文："two persons independently categorized each paper for each flaw as correct, flawed, underspecified, or not applicable." / "the readers discussed their assessments to converge on a final classification. This was the case for 8 out of 50 papers (16%)."
- 要点：两人独立地对每篇论文的每种缺陷做判断（正确、有缺陷、描述不足、不适用）；有分歧的 8 篇（16%）经讨论达成最终分类。

### E29

- 位置：§III-A Classification methodology
- 原文："We use only information from the papers themselves and did not contact the authors for explanation. Effectively, we impose on ourselves the same constraints reviewers face when deciding whether to accept or reject a paper in a double-blind submission system."
- 要点：只依据论文本身的信息，不联系作者询问；等于给自己加上双盲审稿时审稿人面对的同样限制。

### E30

- 位置：§I Introduction
- 原文："As we do not allege intent, we use the term benchmarking flaws instead of the (tongue in cheek) term “benchmarking crimes” used earlier in the literature" / "We believe that most, if not all, benchmarking flaws we found are unintentional and just denote insufficient attention devoted to performance benchmarking in our community."
- 要点：因为不指控动机，作者用"缺陷"而不用早先文献里半开玩笑的"罪行"一词；并认为这些缺陷大多不是故意的，只说明领域对性能评测重视不够。

### E31

- 位置：§VII Limitations；附录 A
- 原文："we think that naming and shaming would be counterproductive as in our opinion the problem is not with individuals but rather the community as a whole." / "detailed discussion in Appendix A that should allow others to perform the survey themselves according to the same criteria." / "to keep the discussion anonymous with regard to the papers in our sample, we either abstract away or change some of the details."
- 要点：作者没有公开哪篇论文有哪些缺陷，认为点名羞辱适得其反，问题在整个群体而不在个人；作为补偿，附录详细说明判定标准，让别人能按同样标准重做调查；附录中的例子也做了抽象或改动以保持匿名。

### E32

- 位置：§VII Limitations
- 原文："published papers are not necessarily a representative sample of all papers, especially at the top conferences."
- 要点：局限：已发表的论文不一定能代表所有论文（包括投稿），在顶会尤其如此。

### E33

- 位置：§IX Related work，Benchmarking advice
- 原文："While these studies demonstrate important benchmarking problems, the lack of a survey means they cannot determine the impact these potential problems have on the research literature."
- 要点：只用例子和自己的测试来指出问题的文章，能说明问题存在，但没有系统调查，就无法判断这些问题在已发表文献中影响有多大。

### E34

- 位置：§I Introduction
- 原文："As for the cause of the flaws we encountered, we can only speculate."
- 要点：对缺陷产生的原因，作者明确说只能推测。

### E35

- 位置：§V Impact
- 原文："the problem of benchmarking flaws is not an issue of a few authors and reviewers being particularly careless (or malicious), but rather a community-wide lack of awareness of or attention to these problems."
- 要点：缺陷在各篇论文间分布得相当均匀，说明这不是少数作者和审稿人格外粗心（或恶意），而是整个领域对这些问题缺乏认识和重视。
