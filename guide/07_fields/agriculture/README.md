# 农业、林业与渔业：领域概况

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲农学、作物科学、土壤科学、园艺、林学、渔业和水产养殖这些方向的研究实际怎样运转：田间试验为什么跟着季节走，为什么要跨地点、跨年份做，怎样和农民一起做农场试验，田间试验怎样设计、分析和报告，数据怎样整理和共享。经济合作与发展组织学科分类里的 4.5"其他农业科学"也放在这里一起讲。动物与乳品科学、兽医科学、农业生物技术本文不涉及。实验室里的细胞、分子实验见[生物科学篇](../biological-sciences/README.md)；野外观测和环境过程见[地球与环境科学篇](../earth-environmental-sciences/README.md)；各学科都适用的做法（选题、做计划、写作、审稿、科研伦理）见[全程地图](../../00_start-here/research-journey.md)里的主线各章和[贯穿全程](../../08_throughout/README.md)。这里只写本领域特有的东西。本文引用的规定和做法，各自写明了出处：美国农学会、美国作物科学学会、美国土壤科学学会（下称"美国三学会"）的出版手册和期刊政策，美国渔业学会等编写的鱼类研究指南，英国洛桑研究所的长期试验，国际农业研究磋商组织的数据政策。它们是某个国家、某个机构的规定，不是全世界通用的规矩；在中国或其他国家做研究，以当地主管部门、资助方和目标期刊的规定为准 `[本项目分析]`。

**读完本文，你应该能：**

- 说清田间试验为什么慢、为什么要跨地点和年份，农场试验和试验站试验有什么不同；
- 找准实验单位，分清真重复和伪重复，知道区组和随机化各管什么；
- 按目标期刊的要求写清试验设计和统计方法，按元数据标准整理田间记录；
- 避开新手在田间试验设计、和农民合作、写论文时常犯的错误。

---

## 本领域研究怎样运转

### 田间试验跟着季节走

很多田间试验跟着作物的生长季走：一年生作物种下去，要等到收获才有产量数据，一年往往只能做一轮 `[本项目分析]`。这决定了本领域的节奏：

- **数据要攒好几年。** Kool 等人 2020 年的一篇综述，分析了 1986—2015 年发表的 172 篇撒哈拉以南非洲农场试验论文[^kool2020reproducibility-e1]。这些试验常常跨多个生长季，一般是 2 到 3 季[^kool2020reproducibility-e6]。论文也可能因为"还差一年数据"被退回：美国三学会的出版手册举例说，这样的稿件补齐数据、写进论文后可以再投[^asa2024style-e5]。
- **设计错了，代价是一整年。** 本文多处引用 Casler 2015 年发表在《农学杂志》（Agronomy Journal）上的试验设计综述。他指出，P 值偏高（结果不显著）时，往往说不清问题出在哪里，结果常常发表不了，时间和钱都白花了[^casler2015fundamentals-e23]。所以动手前的设计要格外用心 `[本项目分析]`。
- **田里的意外很多。** Casler 举例说，他同事们的试验遇到过军事演习、搬房子的车、喷错的除草剂、摩托车帮、来报复的前员工、开派对的学生，靠随机完全区组设计才挽救回来[^casler2015fundamentals-e15]。

### 多地点、多年份

在多个地点和年份重复同一个试验、看处理在不同环境下表现如何，是很常见的做法[^casler2015fundamentals-e9]。原因是同一个处理在不同环境下效果常常不一样（统计上叫处理和环境的交互作用）。Casler 用方差分量算过：相对于每个地点内的重复数，应该优先增加地点和年份；只有处理和环境完全没有交互作用时，才值得优先加重复，而这种情况很少见[^casler2015fundamentals-e8]。

### 长期定位试验

有些问题（土壤肥力、碳储量、气候影响）要几十年才看得清，靠的是长期定位试验 `[本项目分析]`。一个例子是英国洛桑研究所，下面是它在自己网站上的介绍：

- 它有世界上最古老、仍在进行的农业田间试验，其中 7 个长期试验延续至今[^rothamstedlte-e1]。这些试验建于 1843—1856 年，有些因土壤结构差或作物病害而失败、中止[^rothamstedlte-e2]。试验也不是一成不变的：研究所每 5～10 年审慎调整一次管理措施，让试验保持现实意义[^rothamstedlte-e3]。
- 保存下来的样品超过 30 万份，用新方法分析老样品，能看到 180 年间的变化[^rothamstedlte-e4]。很多原本是纸质的记录，已整理成可用的数据库[^rothamstedlte-e6]。
- 外部研究者要用这些试验或样品，先要和洛桑的合作者商量，再提交取样申请表[^rothamstedlte-e5]。
- 对新手来说，长期数据还有一个用处：Casler 指出，在同一地点积累了多年结果的研究者，有大量数据可以用来规划新试验[^casler2015fundamentals-e22]。进组时问问导师，组里或试验站有没有历年的试验记录 `[本项目分析]`。

### 林业和渔业的几点不同

- **林业**：树木寿命长，一个试验可能跨越很多年，常常要接手前人的试验 `[本项目分析]`。据 Casler，不完全区组设计（每个区组只放一部分处理）在林木育种项目里很常见，因为这些项目多在山区，几乎没有平地[^casler2015fundamentals-e25]。植物表型元数据标准 MIAPPE（见下文"数据标准和共享"）在 1.1 版把适用范围扩展到多年生和木本植物[^papoutsoglou2020enabling-e5]。
- **渔业和水产养殖**：鱼是脊椎动物 `[本项目分析]`。下面几条出自美国渔业学会等三家美国学术团体 2014 年联合编写的鱼类研究指南：在美国，用脊椎动物做研究的机构必须设立动物护理和使用委员会（Institutional Animal Care and Use Committee，IACUC，负责审查和监督本机构的动物使用）[^afs2014fishes-e3]；研究者要了解有关法规和生物安全问题，取得全部所需许可[^afs2014fishes-e4]；在美国以外做研究，要遵守所在国的野生动物法规[^afs2014fishes-e5]；研究要用能可靠回答问题的最少数量的动物[^afs2014fishes-e2]；从野外采来、带进实验室的鱼，按发放科研采集许可的机构的普遍共识，绝不应再放回野外[^afs2014fishes-e6]。动物研究的 3R 原则和报告规范见[生物科学篇](../biological-sciences/README.md#动物研究3r-原则和-arrive-报告规范)。

### 发表：以美国三学会的期刊为例

下面是美国三学会期刊的政策，其他期刊以各自的作者须知为准 `[本项目分析]`：

- **审稿**：多数期刊用单盲审稿（作者不知道审稿人是谁），少数用双盲（双方都不知道对方是谁）[^asa2024style-e6]。
- **预印本**：可以发到非营利的预印本平台，但投稿时要引用这份预印本[^sciencesocietieseditorial-e3]。
- **数据**：要保存并提供理解和评价论文结果所需的数据，存放在公认的、学界可用的领域数据仓库[^sciencesocietieseditorial-e1]；没放进仓库的，应能向作者索取[^sciencesocietieseditorial-e2]。
- **伦理**：作者要恰当地承认他人的工作和想法[^sciencesocietieseditorial-e4]，还要想一想自己的研究让谁受益、忽视了谁[^sciencesocietieseditorial-e5]。
- **署名顺序的惯例和审稿周期**：本文资料未涉及，以导师或目标期刊要求为准。署名的一般原则见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md)。

---

## 和其他学科不同的地方

下表和计算机、实验室生物学对照。计算机一栏的依据见[计算机篇](../computer-science/README.md)，生物一栏见[生物科学篇](../biological-sciences/README.md)；整张表是本项目的归纳，带脚注的格子有本文资料支持 `[本项目分析]`。

| | 农业、林业与渔业 | 实验室生物学 | 计算机 |
|---|---|---|---|
| 一轮试验多久 | 常跟着生长季；Kool 等人 2020 年综述的非洲农场试验一般跨 2～3 季[^kool2020reproducibility-e6] | 可能很长，见生物科学篇 | 很多实验能很快重跑 |
| 实验单位 | 常是一块小区、一个水箱、一个农场 | 常是一只动物、一份独立培养物 | 常按随机种子、数据集算 |
| 环境 | 天气、土壤每年每地都不同，常跨地点和年份做[^casler2015fundamentals-e9] | 实验室条件可以控制 | 运行环境可以固定 |
| 合作对象 | 农场试验里有农民、推广人员[^casler2015fundamentals-e11] | 主要在课题组内 | 主要在研究组内 |
| 发表 | 本文资料只涉及期刊；美国三学会的期刊接受发过预印本的稿件[^sciencesocietieseditorial-e3] | 期刊；有 bioRxiv 预印本平台 | 多数方向以会议为主 |

---

## 田间试验的设计

Casler 把试验设计归结为四根支柱：重复、随机化、区组、实验单位的大小，每一根都要有意识地决定[^casler2015fundamentals-e1]。

### 先定实验单位，再谈重复

实验单位、两种"重复"和"n 怎么算"，[生物科学篇](../biological-sciences/README.md#先弄清实验单位再算-n)已经讲过，道理相同。田间试验只需先记住两句：

- **实验单位**是施加处理的最小单位[^casler2015fundamentals-e2]。施肥施在一块小区上，小区就是实验单位；在小区里采的多个土样、量的多株植物，只是观测单位 `[本项目分析]`。
- **重复**必须和施加处理在同一个空间、时间尺度上[^casler2015fundamentals-e4]。

和实验室的差别在于：田间的实验单位常是一块地、一个农场，甚至一年，又大又贵，很难多做 `[本项目分析]`。

### 伪重复：处理和地块混在一起

**伪重复**（pseudoreplication）指处理没有真正重复、或重复之间在统计上不独立，却仍用统计检验来检验处理效应[^davies2015pseudoreplication-e1]。Casler 举了一个田间的例子：只用两块 1 公顷的草地，一块烧荒、一块不烧当对照。统计分析本身没错，但科学上有缺陷，这种设计没法明确解释结果[^casler2015fundamentals-e5]。据 Casler 介绍，"伪重复"一词由 Hurlbert 1984 年提出，指的就是这种处理和实验单位完全混在一起的情况[^casler2015fundamentals-e6]。渔业研究也一样：美国渔业学会等的指南指出，把一个实验单位里的多个样品当成多个实验单位，就是伪重复[^afs2014fishes-e1]。

Casler 给的补救办法有两种[^casler2015fundamentals-e7]：**在空间上重复**，即在多块地上烧和不烧，可以把每片草原当作一个区组；**在时间上重复**，即跨年份做，但每年都要把处理重新随机分配，也就是每年换一块新地重做。

> **不同的看法：伪重复要卡多严？**
>
> - **严格派**：Casler、美国渔业学会等的指南都把伪重复当作要在设计阶段避免的错误[^casler2015fundamentals-e6][^afs2014fishes-e1]。
> - **宽松派**：生态学者 Davies 和 Gray 2015 年撰文认为，这个概念被用得太教条，常导致论文在审稿时被拒[^davies2015pseudoreplication-e2]。他们自己发的在线问卷收到 103 份回复，其中 58% 的人遇到过觉得伪重复无法避免的研究问题[^davies2015pseudoreplication-e5]。他们指出，昂贵的大尺度（景观尺度）操纵试验、偶然事件只发生在一个地点的自然实验，本来就很难有真重复[^davies2015pseudoreplication-e6]。他们建议：界定清楚假设和所关心的总体，承认统计推断的局限，用嵌套、随机效应等统计方法[^davies2015pseudoreplication-e3]；审稿人指责伪重复前，也要先证明这个指责成立[^davies2015pseudoreplication-e4]。
> - **实际建议** `[本项目分析]`：能设计出真重复，就一定要做；实在做不到（例如整个流域只有一个），就在论文里明说实验单位是什么、结论能推广到哪里，不要把样品数当重复数。

### 区组和随机化

- **区组**有两个用途（本节几条都出自 Casler 2015）：一是把条件相近的实验单位分成一组，提高精度；二是方便操作，让某个因素可以用更大的地块[^casler2015fundamentals-e14]。
- **田块看起来均匀，其实多半不均匀**，空间变异的模式要多年摸索才能预测[^casler2015fundamentals-e19]。所以可以在两个方向上都设区组，防止区组方向猜错[^casler2015fundamentals-e17]。处理数超过 20 个时，更多、更小的区组几乎总比完全区组更有效[^casler2015fundamentals-e18]。
- **随机化是保险**：它保证未知或意外的变异来源不会带来偏倚和混杂[^casler2015fundamentals-e13]。
- **裂区设计**常常是为了方便：耕作、灌溉、播期这类因素需要更大的地块，就放在主区[^casler2015fundamentals-e16]。裂区的主区和副区精度不同，分析时要用不同的误差项 `[本项目分析]`。

### 地点、年份和功效分析

- 地点、年份要多，重复数其次[^casler2015fundamentals-e8]。Casler 还建议，设计时考虑让区组因素（例如年份）可以当作**随机效应**，即把每个区组看成从更大总体中随机抽到的一个[^casler2015fundamentals-e24]。这样结论才有可能推广到没做试验的地点和年份 `[本项目分析]`。
- 只要不把交互作用归因到没有重复的环境变量上，就不容易被批评[^casler2015fundamentals-e9]。例如某个品种在甲地表现好、乙地表现差，你不能断定"因为甲地雨水多"，除非雨水这个因素本身有重复 `[本项目分析]`。

**动手前先做功效分析。** **统计功效**是处理真有差别时，试验能检测出来的概率 `[本项目分析]`。Casler 根据自己的教学和咨询经验认为，很少有农学研究者为了设计更好的试验认真做过功效分析[^casler2015fundamentals-e10]。他建议每次设计试验前都做，即使参数只能靠猜[^casler2015fundamentals-e21]。怎样做研究设计，见主线章节[从研究问题到证据清单](../../02_from-project-to-study/01_question-to-evidence.md)。

---

## 统计分析和报告

美国三学会的出版手册要求，读者必须能看懂试验怎样设计和实施，才能判断结果是否可信[^asa2024style-e9]。按这本手册：

- 方法部分要写清区组、不同大小的实验单位（如裂区、条区）、地点数和年份数、重复数、田间或温室条件、各性状怎样测量[^asa2024style-e1]。
- **实验单位和取样单位不同时，两者都要写清**，用了多少实验单位、每个取了多少样，要让读者看明白[^asa2024style-e2]。
- 凡是用来下结论的数据，都要报告**标准误或置信区间**[^asa2024style-e3]。
- 在同一份试验材料上、不同位置或不同时间测的数据**常常相关**（不独立）[^asa2024style-e4]，要用能处理这种相关的统计方法 `[本项目分析]`。
- 不常见的设计或统计方法要给出细节[^asa2024style-e8]；表格标题一般写明作物或土壤、主要变量、地点和年份[^asa2024style-e7]。

**农场试验的报告问题尤其多。** 前面那篇 Kool 等人对 172 篇非洲农场试验论文的综述发现：常常很难甚至无法根据论文重现试验设计；养分管理、除草、作物信息写得最好，整地、田块历史、病虫害和水分管理很少写[^kool2020reproducibility-e2]；不少研究对田间操作的描述含糊不清[^kool2020reproducibility-e8]。统计的一般做法见主线章节[报告差多少、有多确定，而不只是 p 值](../../03_conduct-and-analyze/02_analyze-and-interpret.md#3-报告差多少有多确定而不只是-p-值)。

---

## 数据标准和共享

田间数据离开了试验背景就很难用 `[本项目分析]`。Papoutsoglou 等人 2020 年指出，植物表型数据尤其难复用和汇总，因为试验场所、植物、数据类型、试验设计都各不相同[^papoutsoglou2020enabling-e1]。他们举了一个例子：原始数据没按任何标准整理，复用的人只好从零散的文字描述里手工拼出元数据[^papoutsoglou2020enabling-e2]。

**元数据**就是描述数据的数据：在哪里、什么时候、用什么材料、怎样测的 `[本项目分析]`。**元数据标准**列出解读某类试验数据必需的字段[^papoutsoglou2020enabling-e7]。植物表型领域的标准叫 **MIAPPE**（Minimum Information About a Plant Phenotyping Experiment，植物表型试验最少信息），据该文是这个领域第一个、也是当时唯一的社区元数据标准[^papoutsoglou2020enabling-e3]。它的指导原则之一，是减少研究者记录试验时漏掉重要信息的机会[^papoutsoglou2020enabling-e4]。其中的"事件"一项很实用：在某个时间点影响试验的事情都要记，既包括播种、施杀菌剂这类田间操作，也包括降雨、病原菌侵染这类意外[^papoutsoglou2020enabling-e6]。即使目标期刊不要求，也可以照它的字段写田间记录 `[本项目分析]`。数据整理的一般做法见贯穿全程的[整理科研材料](../../08_throughout/organizing_materials.md)。

**开放共享：以国际农业研究磋商组织为例。** 国际农业研究磋商组织（CGIAR）把研究成果看作国际公共物品，要让穷人、尤其是发展中国家的小农受益[^cgiar2021fair-e1]。它承诺产出尽可能开放，并且可查找、可获取、可互操作、可复用（这四条合称 FAIR 原则）[^cgiar2021fair-e2]。它 2021 年的数据政策有几条具体要求：

- 项目立项时就写数据管理计划[^cgiar2021fair-e4]。
- 数据集存入合适的仓库并公开，最迟在数据收集完成后 12 个月内、或用到这些数据的成果发表后 6 个月内，以先到者为准[^cgiar2021fair-e3]。
- 只有存在保密协议等合同义务时，才可以不开放[^cgiar2021fair-e6]；数据管理要顾及隐私和伦理[^cgiar2021fair-e5]。
- 这是一个机构的规定；你的资助方和期刊的要求可能不同，以它们为准 `[本项目分析]`。

---

## 和农民一起做研究

**农场试验**（on-farm research）是在农民自己的田里做的试验 `[本项目分析]`。Kool 等人指出：**试验站**是高度受控的环境，可以固定其他条件来研究处理；在农民的田里，研究者能控制的少得多，试验处在更大、更多变的自然和社会经济环境中[^kool2020reproducibility-e5]。所以试验站的结论能不能搬到农民的田里，要专门检验 `[本项目分析]`。《农学杂志》2019 年出过一期农场试验专刊，导言作者 Kyveryga 来自美国爱荷华州大豆协会。他写道，过去二十年农场试验扩展很快，尤其在发达国家，原因是精准农业技术用得更广了[^kyveryga2019onfarm-e1]：产量监测、卫星导航等设备，让农民和研究者能以整块田的尺度、在多个地点、以低得多的成本做试验[^kyveryga2019onfarm-e2]。

- **了解农民为什么参加。** 据这篇导言介绍，专刊中一项研究深度访谈了美国内布拉斯加州农场试验网络的 40 名参与者：农民做农场试验，主要是为了增加收益、出于好奇，以及想要不偏不倚的结果[^kyveryga2019onfarm-e3]；他们还希望更多地参与试验的各个阶段[^kyveryga2019onfarm-e4]。
- **农民不爱做重复，就换个设计。** Casler 指出，农民和推广人员愿意大面积试新处理，却不太看重重复。可以把多个农场当区组，或者把对照小区插在其他处理之间、最好隔一块放一块[^casler2015fundamentals-e11]。另一种是**母—子试验**：试验站做一个有正规重复和随机化的"母试验"，许多农户各做一个"子试验"[^casler2015fundamentals-e12]。
- **写清"农民常规做法"到底是什么。** Kool 等人发现，农场试验常拿"农民常规做法"当对照，却默认这种做法到处一样、读者也都知道[^kool2020reproducibility-e3]。
- **写清结论对谁有用。** 同一篇综述发现，被分析的研究大多没说清结论适用于哪些农户、哪些环境[^kool2020reproducibility-e4]。作者建议至少回答：效应在什么条件下出现、对谁有用，并公开选地点、农户、田块的标准[^kool2020reproducibility-e7]。
- **把结果讲回给农民。** Kyveryga 认为，农场试验的关键之一，是把结果分析好、汇总好，并讲给农民和农艺师听[^kyveryga2019onfarm-e5]。

访谈、问卷等涉及人的研究，一般还要过伦理审查，以你所在机构的规定为准 `[本项目分析]`；见贯穿全程的[科研诚信与伦理](../../08_throughout/integrity_and_ethics.md)和[合作与导师](../../08_throughout/collaboration_and_advisors.md)。

---

## 常见的研究类型

**本领域的研究类型文档**：[田间试验](research-types/field_trial.md)。

**相关学科的研究类型文档**：[野外观测研究](../earth-environmental-sciences/research-types/field_study.md)。

下面的分组和"相通"的判断为本项目分析 `[本项目分析]`。

- **田间对照试验和多环境品种试验**：在小区上比较品种、肥料、耕作等处理，常在多个地点、多年重复。思路和研究方法里的[对照实验](../../06_methods/controlled_experiment.md)相通（随机分组、控制无关变量），但那篇讲的是人类参与者；这里的实验单位是地块，还要跨地点和年份。
- **农场试验和参与式研究**：和农民一起在他们的田里做。研究者和实践者一起改进做法这一点，和[行动研究](../../06_methods/action_research.md)相通；不同在于这里通常仍有对照和重复。
- **长期定位试验**：同一块地上持续做几十年，见[纵向研究](../../06_methods/longitudinal_study.md)，不同在于对象是土壤和作物而不是人或软件。
- **作物模型和仿真**：用模型模拟作物生长、产量和气候影响，见[定量仿真](../../06_methods/simulation_study.md)。
- **表型和遥感数据分析**：分析图像、传感器、产量监测数据，见[数据科学](../../06_methods/data_science.md)，要特别交代田间元数据。
- **农户调查和访谈**：了解农民的做法和决策，见[问卷调查](../../06_methods/questionnaire_survey.md)和[访谈研究](../../06_methods/interview_study.md)。
- **综述和元分析**：汇总多地多年的已发表试验，见[综述研究](../../06_methods/review_study.md)。

---

## 给新手的建议

1. **动手前先学好试验设计和分析，或者找一个懂的合作者。** 这是 Casler 给年轻研究者的第一条建议[^casler2015fundamentals-e20]。
2. **画出试验的层次，标出实验单位。** 地点、年份、区组、小区、样品各在哪一层 `[本项目分析]`；重复要落在施加处理的那一层[^casler2015fundamentals-e4]。然后做功效分析，参数只能靠猜也要做[^casler2015fundamentals-e21]。
3. **从小做起。** 刚开始先设计小规模的试验，实验单位尽量大，大到人力和机械能应付为止[^casler2015fundamentals-e26]。
4. **地点和年份优先于重复数**[^casler2015fundamentals-e8]，计划时就留出两三季的时间 `[本项目分析]`。
5. **田间操作和意外当天记，按元数据标准记**：播种、施药、降雨、病害都写日期[^papoutsoglou2020enabling-e6]。
6. **和农民合作时，先了解他们为什么参加，并让他们参与各个阶段。** 上面那项内布拉斯加州 40 人的访谈研究里，农民就提出了这个愿望[^kyveryga2019onfarm-e3][^kyveryga2019onfarm-e4]。

---

## 常见错误

| 错误（例子由本项目编写 `[本项目分析]`） | 为什么是问题 |
|---|---|
| 一块施肥地、一块不施肥地，各取 20 个土样，报告 n = 20 | 处理和地块完全混在一起，是伪重复[^casler2015fundamentals-e6]；同一实验单位里的多个样品不是多个实验单位[^afs2014fishes-e1] |
| 跨年份做试验，但每年都在同一位置放同一处理 | 时间上的重复要求每年重新随机分配[^casler2015fundamentals-e7] |
| 只在一个试验站做一年，就下普遍结论 | 处理和环境常有交互作用，要优先增加地点和年份[^casler2015fundamentals-e8] |
| 方法里只写"必要时除草""按农民常规做法管理" | 别人无法重现试验[^kool2020reproducibility-e2][^kool2020reproducibility-e3] |
| 只报告均值，不给标准误或置信区间 | 美国三学会期刊要求报告精度[^asa2024style-e3] |
| 田间记录只存在自己的笔记本里，格式随意 | 别人（包括以后的自己）很难复用[^papoutsoglou2020enabling-e2] |

---

## 延伸阅读

- **Casler 2015，Fundamentals of Experimental Design（Agronomy Journal）**：用田间例子讲重复、随机化、区组和小区大小，结尾有给年轻研究者的建议。设计第一个田间试验前读。
- **美国三学会的出版手册第 4 章（Statistical Design and Analysis）**：说清论文里试验设计和统计要写什么。
- **Kool 等人 2020（Experimental Agriculture）**：分析非洲农场试验论文的写法问题。做农场试验前读，帮你想清楚对照和推广范围。
- **Davies & Gray 2015（Ecology and Evolution）**：伪重复的另一面，适合在实在做不出真重复时读。
- **Papoutsoglou 等人 2020，MIAPPE 1.1（New Phytologist）**：植物表型元数据标准，整理田间数据时参考。
- **美国渔业学会等 2014，Guidelines for the Use of Fishes in Research**：鱼类研究的设计、许可和动物福利，在美国做鱼类研究时参考。

[^casler2015fundamentals-e1]: Casler 2015，Abstract。[证据](../../../sources/notes/casler2015fundamentals.md#e1)
[^casler2015fundamentals-e2]: Casler 2015，Table 1。[证据](../../../sources/notes/casler2015fundamentals.md#e2)
[^casler2015fundamentals-e4]: Casler 2015，Replication。[证据](../../../sources/notes/casler2015fundamentals.md#e4)
[^casler2015fundamentals-e5]: Casler 2015，Replication，烧荒试验的例子。[证据](../../../sources/notes/casler2015fundamentals.md#e5)
[^casler2015fundamentals-e6]: Casler 2015，Replication，烧荒试验的例子。[证据](../../../sources/notes/casler2015fundamentals.md#e6)
[^casler2015fundamentals-e7]: Casler 2015，Replication，烧荒试验的例子。[证据](../../../sources/notes/casler2015fundamentals.md#e7)
[^casler2015fundamentals-e8]: Casler 2015，Number of replicates。[证据](../../../sources/notes/casler2015fundamentals.md#e8)
[^casler2015fundamentals-e9]: Casler 2015，Replication。[证据](../../../sources/notes/casler2015fundamentals.md#e9)
[^casler2015fundamentals-e10]: Casler 2015，Number of replicates。[证据](../../../sources/notes/casler2015fundamentals.md#e10)
[^casler2015fundamentals-e11]: Casler 2015，Replication，特殊情况。[证据](../../../sources/notes/casler2015fundamentals.md#e11)
[^casler2015fundamentals-e12]: Casler 2015，Replication，参与式研究。[证据](../../../sources/notes/casler2015fundamentals.md#e12)
[^casler2015fundamentals-e13]: Casler 2015，Randomization。[证据](../../../sources/notes/casler2015fundamentals.md#e13)
[^casler2015fundamentals-e14]: Casler 2015，Blocking。[证据](../../../sources/notes/casler2015fundamentals.md#e14)
[^casler2015fundamentals-e15]: Casler 2015，Blocking。[证据](../../../sources/notes/casler2015fundamentals.md#e15)
[^casler2015fundamentals-e16]: Casler 2015，Blocking，裂区设计。[证据](../../../sources/notes/casler2015fundamentals.md#e16)
[^casler2015fundamentals-e17]: Casler 2015，Blocking。[证据](../../../sources/notes/casler2015fundamentals.md#e17)
[^casler2015fundamentals-e18]: Casler 2015，Blocking。[证据](../../../sources/notes/casler2015fundamentals.md#e18)
[^casler2015fundamentals-e19]: Casler 2015，结论部分。[证据](../../../sources/notes/casler2015fundamentals.md#e19)
[^casler2015fundamentals-e20]: Casler 2015，结论部分。[证据](../../../sources/notes/casler2015fundamentals.md#e20)
[^casler2015fundamentals-e21]: Casler 2015，结论部分。[证据](../../../sources/notes/casler2015fundamentals.md#e21)
[^casler2015fundamentals-e22]: Casler 2015，结论部分。[证据](../../../sources/notes/casler2015fundamentals.md#e22)
[^casler2015fundamentals-e23]: Casler 2015，结论部分。[证据](../../../sources/notes/casler2015fundamentals.md#e23)
[^casler2015fundamentals-e24]: Casler 2015，Replication。[证据](../../../sources/notes/casler2015fundamentals.md#e24)
[^casler2015fundamentals-e25]: Casler 2015，Blocking，不完全区组设计。[证据](../../../sources/notes/casler2015fundamentals.md#e25)
[^casler2015fundamentals-e26]: Casler 2015，结论部分。[证据](../../../sources/notes/casler2015fundamentals.md#e26)
[^asa2024style-e1]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../sources/notes/asa2024style.md#e1)
[^asa2024style-e2]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../sources/notes/asa2024style.md#e2)
[^asa2024style-e3]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../sources/notes/asa2024style.md#e3)
[^asa2024style-e4]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../sources/notes/asa2024style.md#e4)
[^asa2024style-e5]: 美国农学会等 2024，出版手册第 1 章 Manuscript Handling。[证据](../../../sources/notes/asa2024style.md#e5)
[^asa2024style-e6]: 美国农学会等 2024，出版手册第 1 章 Anonymous Review。[证据](../../../sources/notes/asa2024style.md#e6)
[^asa2024style-e7]: 美国农学会等 2024，出版手册第 5 章。[证据](../../../sources/notes/asa2024style.md#e7)
[^asa2024style-e8]: 美国农学会等 2024，出版手册第 1 章。[证据](../../../sources/notes/asa2024style.md#e8)
[^asa2024style-e9]: 美国农学会等 2024，出版手册第 4 章。[证据](../../../sources/notes/asa2024style.md#e9)
[^sciencesocietieseditorial-e1]: 美国农学会等，Editorial Policies，Data Policy。[证据](../../../sources/notes/sciencesocietieseditorial.md#e1)
[^sciencesocietieseditorial-e2]: 美国农学会等，Editorial Policies，Data Policy。[证据](../../../sources/notes/sciencesocietieseditorial.md#e2)
[^sciencesocietieseditorial-e3]: 美国农学会等，Editorial Policies，Prior Publication。[证据](../../../sources/notes/sciencesocietieseditorial.md#e3)
[^sciencesocietieseditorial-e4]: 美国农学会等，Editorial Policies，Statement of Ethics for Authors。[证据](../../../sources/notes/sciencesocietieseditorial.md#e4)
[^sciencesocietieseditorial-e5]: 美国农学会等，Editorial Policies，Statement of Ethics for Authors。[证据](../../../sources/notes/sciencesocietieseditorial.md#e5)
[^kool2020reproducibility-e1]: Kool 等人 2020，Material and Methods。[证据](../../../sources/notes/kool2020reproducibility.md#e1)
[^kool2020reproducibility-e2]: Kool 等人 2020，Abstract。[证据](../../../sources/notes/kool2020reproducibility.md#e2)
[^kool2020reproducibility-e3]: Kool 等人 2020，Abstract。[证据](../../../sources/notes/kool2020reproducibility.md#e3)
[^kool2020reproducibility-e4]: Kool 等人 2020，Abstract。[证据](../../../sources/notes/kool2020reproducibility.md#e4)
[^kool2020reproducibility-e5]: Kool 等人 2020，Introduction。[证据](../../../sources/notes/kool2020reproducibility.md#e5)
[^kool2020reproducibility-e6]: Kool 等人 2020，Material and Methods。[证据](../../../sources/notes/kool2020reproducibility.md#e6)
[^kool2020reproducibility-e7]: Kool 等人 2020，Conclusion。[证据](../../../sources/notes/kool2020reproducibility.md#e7)
[^kool2020reproducibility-e8]: Kool 等人 2020，Results。[证据](../../../sources/notes/kool2020reproducibility.md#e8)
[^kyveryga2019onfarm-e1]: Kyveryga 2019，Precision Agriculture Technology Tools。[证据](../../../sources/notes/kyveryga2019onfarm.md#e1)
[^kyveryga2019onfarm-e2]: Kyveryga 2019，Precision Agriculture Technology Tools。[证据](../../../sources/notes/kyveryga2019onfarm.md#e2)
[^kyveryga2019onfarm-e3]: Kyveryga 2019，Precision Agriculture Technology Tools。[证据](../../../sources/notes/kyveryga2019onfarm.md#e3)
[^kyveryga2019onfarm-e4]: Kyveryga 2019，Precision Agriculture Technology Tools。[证据](../../../sources/notes/kyveryga2019onfarm.md#e4)
[^kyveryga2019onfarm-e5]: Kyveryga 2019，Analytical Approaches for On-Farm Trials。[证据](../../../sources/notes/kyveryga2019onfarm.md#e5)
[^rothamstedlte-e1]: 洛桑研究所，The Long Term Experiments。[证据](../../../sources/notes/rothamstedlte.md#e1)
[^rothamstedlte-e2]: 洛桑研究所，The Classical Experiments。[证据](../../../sources/notes/rothamstedlte.md#e2)
[^rothamstedlte-e3]: 洛桑研究所，The Classical Experiments。[证据](../../../sources/notes/rothamstedlte.md#e3)
[^rothamstedlte-e4]: 洛桑研究所，Sample Archive。[证据](../../../sources/notes/rothamstedlte.md#e4)
[^rothamstedlte-e5]: 洛桑研究所，National Bioscience Research Infrastructure。[证据](../../../sources/notes/rothamstedlte.md#e5)
[^rothamstedlte-e6]: 洛桑研究所，The Electronic Rothamsted Archive。[证据](../../../sources/notes/rothamstedlte.md#e6)
[^papoutsoglou2020enabling-e1]: Papoutsoglou 等人 2020，Introduction。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e1)
[^papoutsoglou2020enabling-e2]: Papoutsoglou 等人 2020，Introduction。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e2)
[^papoutsoglou2020enabling-e3]: Papoutsoglou 等人 2020，Introduction。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e3)
[^papoutsoglou2020enabling-e4]: Papoutsoglou 等人 2020，Introduction。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e4)
[^papoutsoglou2020enabling-e5]: Papoutsoglou 等人 2020，Introduction。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e5)
[^papoutsoglou2020enabling-e6]: Papoutsoglou 等人 2020，Results，Event。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e6)
[^papoutsoglou2020enabling-e7]: Papoutsoglou 等人 2020，Introduction。[证据](../../../sources/notes/papoutsoglou2020enabling.md#e7)
[^cgiar2021fair-e1]: 国际农业研究磋商组织 2021，1.1。[证据](../../../sources/notes/cgiar2021fair.md#e1)
[^cgiar2021fair-e2]: 国际农业研究磋商组织 2021，1.1。[证据](../../../sources/notes/cgiar2021fair.md#e2)
[^cgiar2021fair-e3]: 国际农业研究磋商组织 2021，Annex 2。[证据](../../../sources/notes/cgiar2021fair.md#e3)
[^cgiar2021fair-e4]: 国际农业研究磋商组织 2021，4.1 c)。[证据](../../../sources/notes/cgiar2021fair.md#e4)
[^cgiar2021fair-e5]: 国际农业研究磋商组织 2021，4.2。[证据](../../../sources/notes/cgiar2021fair.md#e5)
[^cgiar2021fair-e6]: 国际农业研究磋商组织 2021，4.1 b)。[证据](../../../sources/notes/cgiar2021fair.md#e6)
[^davies2015pseudoreplication-e1]: Davies & Gray 2015，Abstract。[证据](../../../sources/notes/davies2015pseudoreplication.md#e1)
[^davies2015pseudoreplication-e2]: Davies & Gray 2015，Abstract。[证据](../../../sources/notes/davies2015pseudoreplication.md#e2)
[^davies2015pseudoreplication-e3]: Davies & Gray 2015，Abstract。[证据](../../../sources/notes/davies2015pseudoreplication.md#e3)
[^davies2015pseudoreplication-e4]: Davies & Gray 2015，Conclusion。[证据](../../../sources/notes/davies2015pseudoreplication.md#e4)
[^davies2015pseudoreplication-e5]: Davies & Gray 2015，问卷结果。[证据](../../../sources/notes/davies2015pseudoreplication.md#e5)
[^davies2015pseudoreplication-e6]: Davies & Gray 2015，Abstract。[证据](../../../sources/notes/davies2015pseudoreplication.md#e6)
[^afs2014fishes-e1]: 美国渔业学会等 2014，2.3 Statistical Design。[证据](../../../sources/notes/afs2014fishes.md#e1)
[^afs2014fishes-e2]: 美国渔业学会等 2014，2.3 Statistical Design。[证据](../../../sources/notes/afs2014fishes.md#e2)
[^afs2014fishes-e3]: 美国渔业学会等 2014，1. Introduction。[证据](../../../sources/notes/afs2014fishes.md#e3)
[^afs2014fishes-e4]: 美国渔业学会等 2014，3. Statutory Requirements。[证据](../../../sources/notes/afs2014fishes.md#e4)
[^afs2014fishes-e5]: 美国渔业学会等 2014，3.1 International Regulations。[证据](../../../sources/notes/afs2014fishes.md#e5)
[^afs2014fishes-e6]: 美国渔业学会等 2014，Final Disposition of Experimental Animals。[证据](../../../sources/notes/afs2014fishes.md#e6)
