# Junk & Lyons 2021：Reproducibility and Replication of Experimental Particle Physics Results

- 资料：`junk2021reproducibility`，[原文](https://arxiv.org/abs/2009.06864)
- 版本：发表于 Harvard Data Science Review，CC BY 4.0；本摘录依据 arXiv:2009.06864v4（2021-05-05）。作者单位为费米国家加速器实验室，以及帝国理工学院和牛津大学。

### E1

- 位置：摘要
- 原文："Large collaborations produce and check the results, and many papers are signed by more than three thousand authors."
- 要点：结果由大型合作组产生并检查，很多论文的作者超过三千人。

### E2

- 位置：§1 Introduction
- 原文："The ATLAS and CMS collaborations at the Large Hadron Collider (LHC) comprise more than 3000 physicists each. Large collaboration size is not limited to collider physics – neutrino experiments often have collaborations consisting of several hundreds to more than a thousand members."
- 要点：大型强子对撞机上的 ATLAS 和 CMS 各有三千多名物理学家；中微子实验的合作组也常有几百到一千多人。

### E3

- 位置：§1 Introduction
- 原文："Particle physics experiments take years to design, build and run, and they require large financial resources, equipment, and effort."
- 要点：粒子物理实验的设计、建造和运行要花好几年，需要大量经费、设备和人力。

### E4

- 位置：§3，Using the p Value as a Tool for Discovery
- 原文："The cut-off on p0 is conventionally taken as 2.87 × 10−7, corresponding to a z-score of 5.0."
- 要点：宣布发现的 p 值门槛按惯例取 2.87×10⁻⁷，对应 5 个标准差（5σ）。

### E5

- 位置：§3，支持 5σ 的理由
- 原文："Past experience shows that effects with z-scores of 3 and 4 have often not been replicated when more data are collected"
- 要点：历史上 3σ、4σ 的效应在收集更多数据后常常消失。

### E6

- 位置：§3，支持 5σ 的理由之后
- 原文："The choice of z ≥5.0 as the requirement for claiming a discovery is arbitrary"
- 要点：把 5σ 定为门槛本身是人为约定。

### E7

- 位置：§3，支持 5σ 的理由
- 原文："a systematic error that is not covered by an appropriate uncertainty can result in a false discovery of an effect with an arbitrarily high significance."
- 要点：没被不确定度覆盖的系统误差，可以造成任意高显著性的假发现；5σ 挡不住这种错误。

### E8

- 位置：§6.6 Blind Analyses
- 原文："Blind analysis methods are designed to prevent experimenters from consciously or unconsciously manipulating their data analyses in order to obtain desired results."
- 要点：盲分析是为了防止实验者有意或无意地调整分析，去得到想要的结果。

### E9

- 位置：§6.6 Blind Analyses
- 原文："One simple method is to optimize the analysis using simulated data and reserve the input of data from the experimental apparatus until the procedures have been decided upon, including the data selection, classification, and statistical procedures."
- 要点：一种简单的盲分析做法：先用模拟数据把分析方法调好，事件选择、分类和统计方法都定下来，再放入真实数据。

### E10

- 位置：§6.6 Blind Analyses
- 原文："The collaboration must then agree to accept the result of the analysis after the data are input to the analysis (“unblinding”), without change to any step of the analysis, or the procedure is not fully blind."
- 要点：揭盲后合作组要接受结果、不再改分析的任何步骤，否则就不算完全的盲分析。

### E11

- 位置：§6.9 Review of Results，Preliminary Results
- 原文："Results in preparation must pass through a lengthy, formal approval process before they can be presented outside of the collaboration."
- 要点：结果在合作组外公开之前，要经过一个漫长的正式批准流程。

### E12

- 位置：§6.9 Review of Results，Publication
- 原文："a committee of collaborators who have worked on similar topics but who are not directly involved in the particular result is set up to review the paper draft."
- 要点：合作组会成立一个委员会审论文初稿，成员做过类似课题、但没直接参与这项结果。

### E13

- 位置：§6.9 Review of Results，Publication
- 原文："This process often uncovers even tiny flaws and it can take several months or even years to complete."
- 要点：内部审查常能发现很小的毛病，可能要花几个月甚至几年。

### E14

- 位置：§6.9 Review of Results，Publication
- 原文："In these cases, dissenting collaborators can request their names to be removed from the author list of that paper."
- 要点：极少数达不成共识的情况下，持不同意见的成员可以要求从这篇论文的作者名单上去掉自己的名字。

### E15

- 位置：§6.9 Review of Results，Publication
- 原文："Sometimes a collaboration may fall into the trap of “group-think,” having repeated the same arguments to itself over and over again, so an independent check has as much value in EPP as in other fields."
- 要点：合作组也会陷入"群体思维"，所以外部期刊审稿在粒子物理里同样有价值。

### E16

- 位置：§6.9，Statistics Committees
- 原文："It is important for physicists who are embarking on a new analysis to consult with the collaboration’s statistics committee, so that work is not steered in a direction that is only later found to be flawed under collaboration review."
- 要点：开始新分析时要先咨询合作组的统计委员会，免得做到内部审查时才发现方向有问题。

### E17

- 位置：§4.1 Ensuring Reproducibility as the Results are Made
- 原文："The first exercise for the new student however is to reproduce the earlier result performed by the previous student using the same data and software."
- 要点：新学生接手前人的分析，第一件事是用同样的数据和软件复现前人的结果。

### E18

- 位置：§4.1
- 原文："Reproducibility only tests the integrity of the computational steps, not the correctness of the assumptions entering the analysis or the quality of the input data."
- 要点：能复现只说明计算步骤没出错，不说明分析的假设正确、输入数据可靠。

### E19

- 位置：§6.2 Software Version Control
- 原文："Not only must the source code be under strict version control, but so too must the installed environments, which include auxiliary files and databases."
- 要点：不只源代码要严格做版本控制，安装好的运行环境（包括辅助文件和数据库）也要。

### E20

- 位置：§4.1
- 原文："Running the programs on computers of different architectures and comparing the results has also long been a tradition in EPP."
- 要点：在不同架构的计算机上运行同一程序并比较结果，是实验粒子物理的老传统。

### E21

- 位置：§7 Special Features of Particle Physics Results
- 原文："Another peculiarity of EPP is the specialization of practitioners into theoretical and experimental categories."
- 要点：实验粒子物理的一个特点是研究者分成理论和实验两类。

### E22

- 位置：§7
- 原文："The second benefit is that experimentalists almost never test theories that they themselves invented, helping to reduce possible effects of confirmation bias."
- 要点：这种分工的好处之一：实验者几乎从不检验自己提出的理论，减少了确认偏差。

### E23

- 位置：§7
- 原文："Models to be tested generally are published in theory or phenomenology papers before the experimental studies are conducted."
- 要点：要检验的模型一般先在理论或唯象学论文里发表，然后才做实验。

### E24

- 位置：§10 Conclusions
- 原文："Experimenters do not hesitate to publish null results."
- 要点：实验者会毫不犹豫地发表零结果（没找到预期信号的结果）。

### E25

- 位置：§7
- 原文："Null results are therefore typically presented as upper limits on signal strengths."
- 要点：零结果一般写成信号强度的上限。

### E26

- 位置：§4.2，Strategies for Publishing and Preserving Analyses
- 原文："A common failure of published physics results is the lack of communication of correlated uncertainties for the predictions in each bin of each histogram, which precludes the exact reproduction of the interpretation"
- 要点：已发表物理结果常见的缺陷是没给出直方图各区间之间相关的不确定度，别人就没法精确复现结论。

### E27

- 位置：§10 Conclusions
- 原文："every new student is given examples of how well-meaning researchers can come to wrong conclusions because they misled themselves and therefore others."
- 要点：每个新学生都会听到这样的例子：好心的研究者因为骗了自己、进而误导了别人而得出错误结论。

### E28

- 位置：§3，支持 5σ 的理由
- 原文："It is important to have a pre-registered threshold for discovery that is shared by competing collaborations. Otherwise, credit for discoveries will go to those with the lowest standards."
- 要点：相互竞争的合作组要共用一个事先定好的发现门槛，否则发现的功劳会落到标准最低的人手里。

### E29

- 位置：§7
- 原文："the z ≥5.0 criterion for discovery makes more sense in EPP than it does in medical trials, for example."
- 要点：5σ 门槛适合粒子物理，不一定适合医学试验等其他领域。

### E30

- 位置：§6.9 Review of Results
- 原文："All collaborators on the author list are given the opportunity to review each result that is published."
- 要点：作者名单上的每个成员都有机会审阅每一项要发表的结果。

### E31

- 位置：Media Summary
- 原文："p values must be less than 2.87×10−7, not 0.05 as is common in some fields of study."
- 要点：粒子物理宣布发现要求 p 值小于 2.87×10⁻⁷，而不是一些学科常用的 0.05。

### E32

- 位置：§10 Conclusions
- 原文："Many analyses are blind. Stringent multi-level review procedures must be followed before results are published."
- 要点：实验粒子物理里很多分析是盲的；结果发表前要经过严格的多级审查。

### E33

- 位置：§6.9 Review of Results
- 原文："Below, we describe the review procedures used by CDF, a typical hadron collider collaboration."
- 要点：文中以 CDF 为例介绍审查流程，它是一个典型的强子对撞机合作组。
