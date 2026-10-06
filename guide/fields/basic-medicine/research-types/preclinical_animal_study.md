# 临床前动物研究

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲**临床前动物研究**：在活体动物身上做实验，结果要为人类医学提供依据，例如为一种药物或疗法进入人体试验铺路。它讲怎样一步步把这类实验设计好、做好、写好。为什么很多临床前发现到了人身上不灵、美国一次研讨会提出的四项核心报告要求，见[基础医学领域概况](../README.md)；3R 原则（替代、减少、优化）和 ARRIVE 报告规范的基本内容，见[生物科学领域概况](../../biological-sciences/README.md#动物研究3r-原则和-arrive-报告规范)。本文不再重复。在细胞、组织或分子上做的实验，见[实验室台面实验](../../biological-sciences/research-types/bench_experiment.md)；用人做的对照实验，见计算机篇的[对照实验](../../computer-science/research-types/controlled_experiment.md)。

**读完本文，你应该能：**

- 说清自己选的动物模型为什么能代表人类疾病，以及它代表不了什么；
- 在动手前定好主要结局、样本量、纳入排除标准、人道终点和停止规则，并写进方案；
- 用正规方法随机分组、隐藏分组，安排好各个阶段的盲法；
- 知道哪些饲养和操作细节会影响结果，什么时候值得做多实验室研究；
- 按 ARRIVE 2.0 写论文。

---

## 1. 这是什么研究，什么时候用

临床前动物研究要同时做到两件事。第一，在动物身上可靠地证明"这种处理带来了这个效应"；第二，让这个结论能推广到病人身上[^henderson2013threats-e13]。Henderson 等人 2013 年综述了 26 份临床前设计指南，其中多数针对神经和脑血管药物研发[^henderson2013threats-e1]。他们把相应的风险分成三类[^henderson2013threats-e2]：

| 风险 | 意思 | 例子 |
|---|---|---|
| 内部效度威胁 | 干扰"处理—效应"推断的因素 | 研究者的预期让结局评估产生偏倚[^henderson2013threats-e13] |
| 构念效度威胁 | 把模型和人类疾病的关系想错了 | 只用动物的旋转行为代表帕金森病，而人的帕金森病还有震颤和认知症状[^henderson2013threats-e3] |
| 外部效度威胁 | 动物身上成立的关系，换到病人身上就不成立 | 近交系小鼠的反应可能只属于这个品系[^henderson2013threats-e6] |

和细胞实验相比，它多了动物伦理审批（第 7 步）和 ARRIVE 报告规范（第 12 步）；和临床试验相比，它的对象是动物，结论还要再跨一步才到人 `[本项目分析]`。**先判断你的实验属于哪一种。** 探索性实验用来找线索、提出假设；验证性实验用来检验一个事先定好的假设。分清这一点，才能正确解读结果[^perciedusert2020reporting-e56]；它也决定了后面很多步怎么做 `[本项目分析]`。通用的讲法见通用篇[分清探索性研究和验证性研究](../../../general/1_before/04_research_design.md#4-分清探索性研究和验证性研究)，本领域的说法见[基础医学领域概况](../README.md#分清探索性实验和验证性实验)。如果你的结果要被别人拿去当做人体试验的依据，就按验证性实验来做 `[本项目分析]`。

---

## 2. 怎么做

下面 12 步大体按时间顺序；第 4 到第 7 步都要在第一只动物进实验之前完成 `[本项目分析]`。

### 第 1 步：先确认非用动物不可

- **怎么做**：查文献，最好找动物研究的系统综述，确认问题还没有答案；再写清为什么必须用活体动物[^perciedusert2020reporting-e33]。能不用动物就不用，这是 3R 里的"替代"[^nc3rsthe3rs-e2]；可以换成什么，见[生物科学领域概况](../../biological-sciences/README.md#动物研究3r-原则和-arrive-报告规范)。
- **为什么**：动物实验的审批一般基于"伤害—收益分析"：动物受到的伤害要和研究对社会的收益相权衡[^perciedusert2020arrive-e6]。此外，依据不足的动物证据如果被拿来启动人体试验，会增加科研浪费，也让受试者的风险和收益失衡[^perciedusert2020reporting-e70]。
- **容易错在哪**：把"之前没人在这个模型里做过"当成证据空白。系统综述能告诉你，问题是不是其实已经有了答案 `[本项目分析]`。

### 第 2 步：选模型，写出它为什么能代表人

- **怎么做**：写清选这个物种和模型的理由，说明所测指标和人类疾病有什么关系、模型怎样验证过。只写"这个模型在本领域常用"是不够的[^perciedusert2020reporting-e32]。对照下面几个问题检查 `[本项目分析，依据下列资料]`：
  - 模型是急性的还是慢性的？用急性病模型代表人类慢性病，就是一种错配[^henderson2013threats-e4]。
  - 给药时机、途径和临床上计划的一致吗？Henderson 等人汇总的指南里，针对构念效度的建议共 25 条[^henderson2013threats-e9]，其中 9 条是让临床前操作（如给药时机）和计划中的临床研究对上[^henderson2013threats-e7]。
  - 操作真的做对了吗？例如本想尾静脉注射，却打到了皮下[^henderson2013threats-e5]。
  - 实验前描述过模型的疾病表型吗？这是这些指南里最常见的建议之一[^henderson2013threats-e1]。
- **为什么**：把模型和人类疾病的关系想错了，就是构念效度威胁[^henderson2013threats-e2]；这时实验内部做得再严谨，结论也推不到人身上 `[本项目分析]`。动物文献的系统综述会列出前人用过的模型及其优缺点，可以帮你选[^perciedusert2020reporting-e33]。
- **容易错在哪**：只用一种模型、一个品系，就下"对人有效"的结论。Henderson 等人汇总的指南里，外部效度方面最常见的建议是在不止一种模型中重现效应，其次是独立重复[^henderson2013threats-e8]。

### 第 3 步：把性别、年龄、来源写进设计

- **怎么做**：
  - **性别**：默认两种性别都纳入，在设计和分析中考虑性别；只用一种性别，要有说得通的理由 `[本项目分析，依据下列资料]`。以美国国立卫生研究院（National Institutes of Health，NIH）为例：对它资助的项目，NIH 要求脊椎动物研究在设计、分析和报告中考虑性别这个变量[^nihrigorguidance-e3]；只研究一种性别的申请，必须充分说明理由[^nihrigorguidance-e6]。这是美国 NIH 对其资助项目的要求；其他国家和资助机构以它们自己的规定为准 `[本项目分析]`。
  - **年龄**：写具体周龄，不写"成年"。"成年小鼠"可以是 6 到 20 周龄[^perciedusert2020reporting-e59]。
  - **来源**：记下供应商和批次。同一品系、不同来源，或同一来源、不同时间购入的动物，遗传上可能不同[^perciedusert2020reporting-e60]。
- **为什么**：物种、品系、亚系、性别、体重、年龄会影响大多数实验结果[^perciedusert2020reporting-e59]。NIH 指出，性别常被动物研究忽视，导致人们对治疗反应中的性别差异认识不全[^nihrigorguidance-e6]。癌症领域的一篇短综述（Mak 等人 2014）转述的改进建议，也包括两种性别、不同年龄都纳入[^mak2014lost-e6]，详见[基础医学领域概况](../README.md#很多临床前发现到了人身上不灵)。
- **容易错在哪**：以为只用雄性"变异小、更省动物"就不用解释 `[本项目分析]`。胚胎、幼体等性别可能无法判断的，可以不报告；按物种和实验情况本应能报告却没报告的，要说明理由[^perciedusert2020reporting-e71]。

### 第 4 步：定好研究类型、主要结局和分析计划

- **怎么做**：写明这是探索性实验还是验证性实验，或者两者都有[^perciedusert2020reporting-e57]。验证性实验只定**一个主要结局指标**，它回答核心问题，也是算样本量的依据[^perciedusert2020reporting-e54]；同时写好评估时间和分析方法[^landis2012call-e11]。统计方法在收集数据前定好[^perciedusert2020reporting-e26]。
- **为什么**：探索性研究考察很多效应，有些会碰巧显著，所以假阳性更多[^perciedusert2020reporting-e56]。探索阶段的发现，要用按核心要求设计和报告的验证性实验来确认[^landis2012call-e17]。
- **容易错在哪**：做完再挑一个显著的指标当主要结局。验证性实验的结论应限于主要结局；其他指标的结果可能功效不足，不能写成定论[^perciedusert2020reporting-e58]。看了数据才想到的假设，要明确标出来[^perciedusert2020reporting-e57]。

### 第 5 步：算样本量

- **怎么做**：验证性实验做功效分析，需要下面几样输入[^perciedusert2020reporting-e34][^perciedusert2020reporting-e35]：
  1. **主要结局上多大的差异算有意义**：按生物学意义来定，临床前研究还要考虑临床意义；
  2. **变异度**：最好来自系统综述和以往研究；只靠预实验，一般得不到够用的估计[^perciedusert2020reporting-e36]；
  3. **目标功效**：一般认为 80%～95% 可以接受；
  4. **预计损失**：把预计会排除或死亡的动物算进去[^perciedusert2020reporting-e39]。
- **先弄清实验单位。** 样本量数的是实验单位，不是测量次数；整笼喂同一种饲料时，实验单位是笼[^perciedusert2020reporting-e6]。详见[生物科学领域概况](../../biological-sciences/README.md#先弄清实验单位再算-n)。
- **为什么**：动物太少、几乎不可能测出有意义差异的实验，不合伦理[^landis2012call-e8]。功效低时，真实效应容易漏掉，测到的效应常被高估，再加上发表偏倚，文献里的假阳性会增多[^perciedusert2020reporting-e38]。Button、Ioannidis 等人估计，神经科学动物研究的平均功效只有 20% 左右[^perciedusert2017experimental-e4]。反过来，动物太多也有伦理问题，还可能得到统计显著、却没有生物学意义的结果[^perciedusert2020reporting-e37]。
- **容易错在哪**：没算就照"惯例"定每组只数，论文里也不提 `[本项目分析]`。没做功效分析，要明说，并写出每组样本量是怎么定的[^perciedusert2020reporting-e39]。
- **工具**：英国国家动物研究替代、优化与减少中心（NC3Rs）的实验设计助手（Experimental Design Assistant，EDA）免费，能帮你算样本量、生成考虑区组的随机序列、安排盲法[^perciedusert2017experimental-e1][^perciedusert2017experimental-e2]。它不能代替统计专家，但能帮你更好地向统计专家求助[^perciedusert2017experimental-e5]。注意：介绍它的这篇论文，作者都参与了工具开发 `[本项目分析]`。

### 第 6 步：事先定好纳入排除标准、人道终点和停止规则

- **怎么做**：**纳入和排除标准**在实验开始、收集数据之前定好[^perciedusert2020reporting-e51]，至少记在实验记录本里，论文中写明是事先定的[^perciedusert2020reporting-e52]。**人道终点**是事先定好的形态、生理或行为征象，一旦出现，动物就退出实验[^perciedusert2020reporting-e65]。**停止规则**指样本量和停止收集数据的规则，也要事先定好并写进论文[^landis2012call-e9]。
- **为什么**：做完再决定剔除谁、什么时候停，等于给自己留了按结果挑数据的余地 `[本项目分析]`。中途死亡或被排除的动物也是信息：一种处理如果杀死了病情最重的动物而不报告，看起来反而像有效[^landis2012call-e10]；因不良反应而排除的动物，还可能为人体试验提供安全信息[^perciedusert2020reporting-e53]。
- **容易错在哪**：结果"差一点显著"，就再加几只。这正是要事先定停止规则的原因[^landis2012call-e9]。

### 第 7 步：写方案，过伦理审批，考虑预注册

- **怎么做**：
  1. **写方案**。内容包括：研究问题和假设、主要结局、统计分析计划、具体操作步骤[^perciedusert2020reporting-e67]。
  2. **过伦理审批**。实验开始前，要拿到相应伦理委员会和（或）监管机构的批准[^perciedusert2020reporting-e64]。审批程序以所在国家的法规和本单位动物伦理委员会的要求为准 `[本项目分析]`。
  3. **考虑预注册**，也就是在实验开始前把方案登记到公开平台。可选的平台有：
     - 专门的动物研究登记平台 animalstudyregistry.org，由德国联邦风险评估研究所（下属的德国实验动物保护中心）运营，接收世界各地的动物研究[^animalstudyregistry-e1]。它的首页新闻提到，2026 年 3 月它和 preclinicaltrials.eu 一起商讨推广预注册[^animalstudyregistry-e3]；本文未能读到 preclinicaltrials.eu 的介绍页，它接收哪些研究请自行查看。
     - 开放科学框架（Open Science Framework），可以设置保密期，论文发表前不公开[^perciedusert2020reporting-e68]。
- **为什么**：预注册能证明假设、方法和分析是事先计划的，不是看着数据调出来的，也让你免受"选择性报告"的质疑[^perciedusert2020reporting-e66]。审稿人可以拿登记内容和论文对照[^animalstudyregistry-e2]。
- **容易错在哪**：以为登记了就不能改。可以改，但要在论文里写明偏离了什么、为什么[^perciedusert2020reporting-e69]。

### 第 8 步：随机分组，并隐藏分组

- **怎么做**：
  - **用工具生成随机序列**：随机数生成器、电子表格的 Rand() 函数[^perciedusert2020reporting-e42]，或抛硬币、随机数表[^kilkenny2009survey-e3]。
  - **优先用区组随机**：简单随机不能保证各组在其他变量上平衡，很少是合适的做法[^perciedusert2020reporting-e43]。可以按窝、笼、实验日期、操作者分区组[^perciedusert2020reporting-e45]，在每个区组内随机。分析时也要把区组放进模型[^perciedusert2020reporting-e44]。
  - **隐藏分组**：在分配那一刻之前，负责分组的人不知道下一只动物会分到哪组[^perciedusert2020reporting-e48][^landis2012call-e6]。可以由不参与实验的同事保管随机表 `[本项目分析]`。
- **为什么**：从笼里"随手"抓一只不是随机，因为里面有人的判断；没有随机分组，推断统计就不成立[^perciedusert2020reporting-e41]。
- **容易错在哪**：先抓到的（往往是更活跃、更好抓的）进处理组，后抓到的进对照组 `[本项目分析]`。另外，写了"随机"却不写怎么随机，读者无从判断。Kilkenny 等人 2009 年调查了英美公共资助机构的 271 篇动物研究论文：12% 报告了随机分组，其中只有 9%（33 篇中的 3 篇）说明了方法[^kilkenny2009survey-e1][^kilkenny2009survey-e4]。

### 第 9 步：安排各阶段的盲法，至少让结局评估设盲

- **怎么做**：从分组、给药、照料、结局评估到数据分析，能设盲的阶段都设盲。做不到全程设盲，至少总能让部分阶段设盲。这需要别人帮忙，例如由技术员给每只动物的注射器编码，由同事给分析用的分组编码[^perciedusert2020reporting-e47]。优先级 `[本项目分析，依据下列资料]`：
  1. **结局评估**：有主观成分时尤其重要，如评估行为、读组织切片[^perciedusert2020reporting-e49]。
  2. **数据分析**：分析前给数据编码，分析完再揭晓组别。分析者要做数据变换、缺失值、离群值等半主观的决定，这一步常被忽视[^perciedusert2020reporting-e50]。
  3. **评估者实在无法设盲**（如各组表型差别一眼就能看出）：把数据交给不知道预期结果的第三方分析，能减少部分偏倚[^perciedusert2020reporting-e49]。
- **为什么**：系统综述显示，不设盲的结局评估会高估处理效应；缺少随机和盲法，可能让效应量虚高多达 30%～45%[^perciedusert2020reporting-e24]。卒中药物 NXY-059 的例子见[基础医学领域概况](../README.md#很多临床前发现到了人身上不灵)。
- **容易错在哪**：一个人包办分组、给药、打分和分析 `[本项目分析]`。

### 第 10 步：管住饲养和操作中的变量

- **怎么做**：能统一的就统一，如所有手术由同一人做；统一不了的，就让它在各组间平衡，如随机安排测量顺序、在笼架上轮换各组笼位[^perciedusert2020reporting-e46]。同时做好记录：光照周期、给药和测量的时间点、抓取方式（提尾巴还是用手捧）都会影响结果[^perciedusert2020reporting-e63]，要记下来。单笼饲养、禁食禁水、不提供环境丰富化，都要有科学理由[^perciedusert2020reporting-e62]。
- **为什么**：饲养环境的每个方面都可能影响动物的行为和生理，从而影响结果[^perciedusert2020reporting-e61]。例如笼架顶层的动物光照更强，可能影响应激[^perciedusert2020reporting-e46]。有些混杂因素因领域而异：麻醉药会影响心血管功能，却很少干扰肿瘤生长，所以在心血管研究中威胁更大[^henderson2013threats-e12]。
- **容易错在哪**：处理组的笼子都放在同一层，或者上午测对照组、下午测处理组 `[本项目分析]`。

### 第 11 步：结论要外推时，考虑多实验室或多样化设计

- **怎么做**：**多实验室研究**是几家实验室按同一方案同时做，分析时把"实验室"作为因素 `[本项目分析]`。**单实验室里的多样化**：做不了多实验室时，可以在单个实验室里有计划地让实验条件多样化，例如分几个批次做[^voelkl2018reproducibility-e6][^voelkl2018reproducibility-e7]。
- **为什么**：标准化让动物更同质，也让结果更只适用于那一套条件[^voelkl2018reproducibility-e2]。实验室之间在噪声、气味、微生物群、人员等方面不同，实验室之间的差异一般远大于实验室内部[^voelkl2018reproducibility-e3]。Voelkl 等人 2018 年用卒中、心肌梗死和乳腺癌动物模型中 440 项临床前研究的数据做了模拟（不是真做了多实验室实验）。模拟结果是：单实验室研究一般估不准效应量；只要 2 到 4 个实验室参加，不增加样本量，置信区间覆盖真实效应的概率最多提高 42 个百分点[^voelkl2018reproducibility-e1]。改进最大的一步是从 1 个实验室变成 2 个[^voelkl2018reproducibility-e4]。
- **容易错在哪**：样本量太小就去做多实验室研究。作者的经验法则是：样本量足以让单实验室设计达到至少 0.8 的功效时，多实验室设计就能改善估计[^voelkl2018reproducibility-e5]。另外，多实验室研究组织起来很费力，可能不适合较基础或探索性的研究[^voelkl2018reproducibility-e6]；而分批次这类简单的多样化，可能不足以覆盖实验室之间的差异[^voelkl2018reproducibility-e7]。

### 第 12 步：按 ARRIVE 2.0 报告

- **怎么做**：ARRIVE 2.0 共 21 项，全部报告是最佳做法；第一步至少做到"核心 10 项"[^perciedusert2020arrive-e10]：研究设计、样本量、减少主观偏倚的措施、结局指标、统计方法、动物信息、实验步骤和结果[^perciedusert2020arrive-e3]。最好在**设计阶段**就对照清单，而不是写完论文才补[^perciedusert2020arrive-e7]。
- 写的时候特别注意 `[本项目分析，依据下列资料]`：
  - **测过的指标都要报告**。只报显著的，文献就会偏向阳性结果[^perciedusert2020reporting-e55]。
  - **怎样随机、哪些阶段设了盲，都要写清**，这属于核心 10 项里的"减少主观偏倚的措施"[^perciedusert2020arrive-e3]（只写"随机"不写方法的问题，见第 8 步）。
  - **统计显著不等于有生物学或临床意义**，讨论效应大小[^perciedusert2020reporting-e72]。
  - **讨论模型的局限**，结论别越过模型的边界（见[领域概况](../README.md#给新手的建议)）。
- **为什么**：交一份填好的清单不等于写全了。PLOS ONE 的一项随机对照试验发现，投稿时只要求作者交 ARRIVE 清单、编辑部不进一步核查，论文的报告并没有更完整[^perciedusert2020arrive-e11]。所以要逐项对照正文检查，不是勾完就算 `[本项目分析]`。

---

## 3. 检查清单

**必须做到**

- [ ] 写清选这个模型的理由，以及所测指标和人类疾病的关系[^perciedusert2020reporting-e32]
- [ ] 开始前拿到伦理批准[^perciedusert2020reporting-e64]
- [ ] 写明是探索性还是验证性；验证性实验事先定好一个主要结局[^perciedusert2020reporting-e57][^perciedusert2020reporting-e54]
- [ ] 说明样本量怎么定；没做功效分析就明说并给出理由[^perciedusert2020reporting-e39]
- [ ] 纳入排除标准、停止规则、统计方法事先定好[^perciedusert2020reporting-e51][^landis2012call-e9][^perciedusert2020reporting-e26]
- [ ] 用正规方法随机分组[^perciedusert2020reporting-e41]，写明方法[^perciedusert2020arrive-e3]
- [ ] 至少让部分阶段设盲[^perciedusert2020reporting-e47]，写明哪些阶段设了盲[^perciedusert2020arrive-e3]
- [ ] 交代每一只排除或死亡的动物[^landis2012call-e10]
- [ ] 至少报告 ARRIVE 核心 10 项[^perciedusert2020arrive-e10]

**做到更好**

- [ ] 用动物文献的系统综述论证证据空白、帮助选模型[^perciedusert2020reporting-e33]
- [ ] 两种性别都纳入（美国 NIH 对其资助项目有此要求）[^mak2014lost-e6][^nihrigorguidance-e3]
- [ ] 用区组随机，并把区组放进分析[^perciedusert2020reporting-e43][^perciedusert2020reporting-e44]
- [ ] 隐藏分组；结局评估和数据分析都设盲[^perciedusert2020reporting-e48][^perciedusert2020reporting-e50]
- [ ] 实验前预注册方案[^perciedusert2020reporting-e66]
- [ ] 报告饲养条件，以及给药和测量的时间[^perciedusert2020reporting-e61][^perciedusert2020reporting-e63]
- [ ] 在第二种模型中重现，或独立重复[^henderson2013threats-e8]
- [ ] 结论要外推时，做多实验室研究或在实验室内有计划地多样化[^voelkl2018reproducibility-e1][^voelkl2018reproducibility-e6]
- [ ] 报告 ARRIVE 全部 21 项[^perciedusert2020arrive-e10]

**这些情况可以不做，不算缺陷**

- 为生产抗体或组织用的动物，以及以摸索流程、调试设备为主的预实验，不做功效分析；数量按需要的量或操作能力来定[^perciedusert2020reporting-e40]。
- 探索性实验不定主要结局，但结论只能当线索[^landis2012call-e12]。
- 表型差别太明显、评估者无法设盲时，改由第三方分析，并在论文里说明[^perciedusert2020reporting-e49]。
- 胚胎、幼体等无法判断性别时，不报告性别，但写明原因[^perciedusert2020reporting-e71]。
- 较基础或探索性的研究不做多实验室研究；Voelkl 等人认为它可能不适合这类研究[^voelkl2018reproducibility-e6]。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 只写"选用常用的某模型" | 这不是理由；要说明模型和人类疾病的关系[^perciedusert2020reporting-e32] |
| 用急性病模型研究人类慢性病，又不讨论这个差距 | 模型和临床情形不匹配，属于构念效度威胁[^henderson2013threats-e4] |
| 只用雄性，没有理由 | 性别会影响结果[^perciedusert2020reporting-e59]；美国 NIH 要求它资助的申请只用一种性别时说明理由[^nihrigorguidance-e6] |
| 从笼里随手抓动物分组 | 不是统计意义上的随机，推断统计不成立[^perciedusert2020reporting-e41] |
| 分组、给药、打分都是同一个人 | 不设盲的结局评估会高估效应[^perciedusert2020reporting-e24] |
| 用预实验的 3 只动物估变异度，算出样本量 | 预实验一般给不出够用的变异度估计[^perciedusert2020reporting-e36] |
| 差一点显著，就再加几只 | 停止规则要事先定好[^landis2012call-e9] |
| 只报告显著的指标 | 文献会偏向阳性结果[^perciedusert2020reporting-e55] |
| 把次要指标的显著结果写成结论 | 可能功效不足，不能写成定论[^perciedusert2020reporting-e58] |
| 处理组和对照组放在笼架不同层 | 光照等条件不同，可能影响应激[^perciedusert2020reporting-e46] |
| 只在一个实验室、一个品系里得到结果，就说"有望用于临床" | 结果可能只适用于这一套条件[^voelkl2018reproducibility-e2]；应在不止一种模型中重现[^henderson2013threats-e8] |
| 投稿时勾完 ARRIVE 清单就算了 | 只交清单、不核查，并没有让报告更完整[^perciedusert2020arrive-e11] |

---

## 5. 延伸阅读

- **Percie du Sert 等人 2020，Reporting animal research: Explanation and elaboration for the ARRIVE guidelines 2.0（PLOS Biology，开放获取）**：ARRIVE 每一项的解释和范例，其中的 Box 3（功效分析）、Box 4（随机）和 Box 5（各阶段盲法）就是一份设计教程。设计第一个动物实验前读。
- **Henderson 等人 2013，Threats to validity in the design and conduct of preclinical efficacy studies（PLOS Medicine，开放获取）**：汇总 26 份临床前设计指南，按内部、构念、外部效度分类。选模型、论证模型和人的关系时读。注意这些指南多数针对神经和脑血管疾病[^henderson2013threats-e1]，多数来自研讨会讨论，只有 3 份写明了制定方法[^henderson2013threats-e11]。
- **Percie du Sert 等人 2017，The Experimental Design Assistant（PLOS Biology，开放获取）**：介绍免费的在线设计工具。需要算样本量、生成区组随机序列时读，然后直接用这个工具。注意作者都参与了这个工具的开发，属于利益相关方 `[本项目分析]`。
- **Voelkl 等人 2018，Reproducibility of preclinical animal research improves with heterogeneity of study samples（PLOS Biology，开放获取）**：为什么"越标准化越好"不一定对，以及多实验室设计的好处。打算让结论走向临床时读。它是基于已发表数据的模拟研究。
- **Landis 等人 2012，A call for transparent reporting to optimize the predictive value of preclinical research（Nature，PubMed Central 有作者稿）**：四项核心报告要求的出处，要点见[领域概况](../README.md#临床前研究至少报告四件事美国一次研讨会的建议)。

[^henderson2013threats-e1]: Henderson 等人 2013，Abstract。[证据](../../../../sources/notes/henderson2013threats.md#e1)
[^henderson2013threats-e2]: Henderson 等人 2013，Editors' Summary。[证据](../../../../sources/notes/henderson2013threats.md#e2)
[^henderson2013threats-e13]: Henderson 等人 2013，Introduction。[证据](../../../../sources/notes/henderson2013threats.md#e13)
[^henderson2013threats-e3]: Henderson 等人 2013，Introduction。[证据](../../../../sources/notes/henderson2013threats.md#e3)
[^henderson2013threats-e4]: Henderson 等人 2013，Box 1。[证据](../../../../sources/notes/henderson2013threats.md#e4)
[^henderson2013threats-e5]: Henderson 等人 2013，Box 1。[证据](../../../../sources/notes/henderson2013threats.md#e5)
[^henderson2013threats-e6]: Henderson 等人 2013，Introduction。[证据](../../../../sources/notes/henderson2013threats.md#e6)
[^henderson2013threats-e7]: Henderson 等人 2013，Results。[证据](../../../../sources/notes/henderson2013threats.md#e7)
[^henderson2013threats-e8]: Henderson 等人 2013，Results。[证据](../../../../sources/notes/henderson2013threats.md#e8)
[^henderson2013threats-e9]: Henderson 等人 2013，Editors' Summary。[证据](../../../../sources/notes/henderson2013threats.md#e9)
[^henderson2013threats-e11]: Henderson 等人 2013，Results，Guideline Characteristics。[证据](../../../../sources/notes/henderson2013threats.md#e11)
[^henderson2013threats-e12]: Henderson 等人 2013，Discussion。[证据](../../../../sources/notes/henderson2013threats.md#e12)
[^perciedusert2020reporting-e6]: Percie du Sert 等人 2020b，Item 1b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e6)
[^perciedusert2020reporting-e32]: Percie du Sert 等人 2020b，Item 12b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e32)
[^perciedusert2020reporting-e33]: Percie du Sert 等人 2020b，Item 12a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e33)
[^perciedusert2020reporting-e34]: Percie du Sert 等人 2020b，Box 3。[证据](../../../../sources/notes/perciedusert2020reporting.md#e34)
[^perciedusert2020reporting-e35]: Percie du Sert 等人 2020b，Box 3。[证据](../../../../sources/notes/perciedusert2020reporting.md#e35)
[^perciedusert2020reporting-e36]: Percie du Sert 等人 2020b，Box 3。[证据](../../../../sources/notes/perciedusert2020reporting.md#e36)
[^perciedusert2020reporting-e37]: Percie du Sert 等人 2020b，Item 2b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e37)
[^perciedusert2020reporting-e38]: Percie du Sert 等人 2020b，Item 2b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e38)
[^perciedusert2020reporting-e39]: Percie du Sert 等人 2020b，Box 3。[证据](../../../../sources/notes/perciedusert2020reporting.md#e39)
[^perciedusert2020reporting-e40]: Percie du Sert 等人 2020b，Box 3。[证据](../../../../sources/notes/perciedusert2020reporting.md#e40)
[^perciedusert2020reporting-e41]: Percie du Sert 等人 2020b，Item 4。[证据](../../../../sources/notes/perciedusert2020reporting.md#e41)
[^perciedusert2020reporting-e42]: Percie du Sert 等人 2020b，Item 4。[证据](../../../../sources/notes/perciedusert2020reporting.md#e42)
[^perciedusert2020reporting-e43]: Percie du Sert 等人 2020b，Box 4。[证据](../../../../sources/notes/perciedusert2020reporting.md#e43)
[^perciedusert2020reporting-e44]: Percie du Sert 等人 2020b，Box 4。[证据](../../../../sources/notes/perciedusert2020reporting.md#e44)
[^perciedusert2020reporting-e45]: Percie du Sert 等人 2020b，Box 4。[证据](../../../../sources/notes/perciedusert2020reporting.md#e45)
[^perciedusert2020reporting-e46]: Percie du Sert 等人 2020b，Item 4b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e46)
[^perciedusert2020reporting-e24]: Percie du Sert 等人 2020b，Item 5。[证据](../../../../sources/notes/perciedusert2020reporting.md#e24)
[^perciedusert2020reporting-e47]: Percie du Sert 等人 2020b，Item 5。[证据](../../../../sources/notes/perciedusert2020reporting.md#e47)
[^perciedusert2020reporting-e48]: Percie du Sert 等人 2020b，Box 5。[证据](../../../../sources/notes/perciedusert2020reporting.md#e48)
[^perciedusert2020reporting-e49]: Percie du Sert 等人 2020b，Box 5。[证据](../../../../sources/notes/perciedusert2020reporting.md#e49)
[^perciedusert2020reporting-e50]: Percie du Sert 等人 2020b，Box 5。[证据](../../../../sources/notes/perciedusert2020reporting.md#e50)
[^perciedusert2020reporting-e51]: Percie du Sert 等人 2020b，Item 3。[证据](../../../../sources/notes/perciedusert2020reporting.md#e51)
[^perciedusert2020reporting-e52]: Percie du Sert 等人 2020b，Item 3a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e52)
[^perciedusert2020reporting-e53]: Percie du Sert 等人 2020b，Item 3b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e53)
[^perciedusert2020reporting-e54]: Percie du Sert 等人 2020b，Item 6b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e54)
[^perciedusert2020reporting-e55]: Percie du Sert 等人 2020b，Item 6a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e55)
[^perciedusert2020reporting-e56]: Percie du Sert 等人 2020b，Item 13。[证据](../../../../sources/notes/perciedusert2020reporting.md#e56)
[^perciedusert2020reporting-e57]: Percie du Sert 等人 2020b，Item 13。[证据](../../../../sources/notes/perciedusert2020reporting.md#e57)
[^perciedusert2020reporting-e58]: Percie du Sert 等人 2020b，Item 17a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e58)
[^perciedusert2020reporting-e26]: Percie du Sert 等人 2020b，Item 7a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e26)
[^perciedusert2020reporting-e59]: Percie du Sert 等人 2020b，Item 8a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e59)
[^perciedusert2020reporting-e60]: Percie du Sert 等人 2020b，Item 8b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e60)
[^perciedusert2020reporting-e61]: Percie du Sert 等人 2020b，Item 15。[证据](../../../../sources/notes/perciedusert2020reporting.md#e61)
[^perciedusert2020reporting-e62]: Percie du Sert 等人 2020b，Item 15。[证据](../../../../sources/notes/perciedusert2020reporting.md#e62)
[^perciedusert2020reporting-e63]: Percie du Sert 等人 2020b，Item 9a、9b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e63)
[^perciedusert2020reporting-e64]: Percie du Sert 等人 2020b，Item 14。[证据](../../../../sources/notes/perciedusert2020reporting.md#e64)
[^perciedusert2020reporting-e65]: Percie du Sert 等人 2020b，Item 16c。[证据](../../../../sources/notes/perciedusert2020reporting.md#e65)
[^perciedusert2020reporting-e66]: Percie du Sert 等人 2020b，Item 19。[证据](../../../../sources/notes/perciedusert2020reporting.md#e66)
[^perciedusert2020reporting-e67]: Percie du Sert 等人 2020b，Item 19。[证据](../../../../sources/notes/perciedusert2020reporting.md#e67)
[^perciedusert2020reporting-e68]: Percie du Sert 等人 2020b，Item 19。[证据](../../../../sources/notes/perciedusert2020reporting.md#e68)
[^perciedusert2020reporting-e69]: Percie du Sert 等人 2020b，Item 19。[证据](../../../../sources/notes/perciedusert2020reporting.md#e69)
[^perciedusert2020reporting-e70]: Percie du Sert 等人 2020b，Item 18。[证据](../../../../sources/notes/perciedusert2020reporting.md#e70)
[^perciedusert2020reporting-e71]: Percie du Sert 等人 2020b，Item 8a。[证据](../../../../sources/notes/perciedusert2020reporting.md#e71)
[^perciedusert2020reporting-e72]: Percie du Sert 等人 2020b，Item 10b。[证据](../../../../sources/notes/perciedusert2020reporting.md#e72)
[^perciedusert2020arrive-e6]: Percie du Sert 等人 2020a，Why good reporting is important。[证据](../../../../sources/notes/perciedusert2020arrive.md#e6)
[^perciedusert2020arrive-e3]: Percie du Sert 等人 2020a，Introducing ARRIVE 2.0。[证据](../../../../sources/notes/perciedusert2020arrive.md#e3)
[^perciedusert2020arrive-e7]: Percie du Sert 等人 2020a，Introducing ARRIVE 2.0。[证据](../../../../sources/notes/perciedusert2020arrive.md#e7)
[^perciedusert2020arrive-e10]: Percie du Sert 等人 2020a，Introducing ARRIVE 2.0。[证据](../../../../sources/notes/perciedusert2020arrive.md#e10)
[^perciedusert2020arrive-e11]: Percie du Sert 等人 2020a，Why good reporting is important。[证据](../../../../sources/notes/perciedusert2020arrive.md#e11)
[^perciedusert2017experimental-e1]: Percie du Sert 等人 2017，Introduction。[证据](../../../../sources/notes/perciedusert2017experimental.md#e1)
[^perciedusert2017experimental-e2]: Percie du Sert 等人 2017，The EDA improves the reliability of experimental results and analysis。[证据](../../../../sources/notes/perciedusert2017experimental.md#e2)
[^perciedusert2017experimental-e4]: Percie du Sert 等人 2017，同上（转引 Button、Ioannidis 等人的估计）。[证据](../../../../sources/notes/perciedusert2017experimental.md#e4)
[^perciedusert2017experimental-e5]: Percie du Sert 等人 2017，The EDA enables an effective assessment of the experimental plans。[证据](../../../../sources/notes/perciedusert2017experimental.md#e5)
[^landis2012call-e6]: Landis 等人 2012，Box 1, Blinding。[证据](../../../../sources/notes/landis2012call.md#e6)
[^landis2012call-e9]: Landis 等人 2012，Interim data analysis。[证据](../../../../sources/notes/landis2012call.md#e9)
[^landis2012call-e10]: Landis 等人 2012，Ad hoc exclusion of data。[证据](../../../../sources/notes/landis2012call.md#e10)
[^landis2012call-e11]: Landis 等人 2012，Retrospective primary end-point selection。[证据](../../../../sources/notes/landis2012call.md#e11)
[^landis2012call-e12]: Landis 等人 2012，An important note about exploratory experiments。[证据](../../../../sources/notes/landis2012call.md#e12)
[^landis2012call-e17]: Landis 等人 2012，An important note about exploratory experiments。[证据](../../../../sources/notes/landis2012call.md#e17)
[^landis2012call-e8]: Landis 等人 2012，Sample-size estimation。[证据](../../../../sources/notes/landis2012call.md#e8)
[^nc3rsthe3rs-e2]: NC3Rs，Definitions of the 3Rs。[证据](../../../../sources/notes/nc3rsthe3rs.md#e2)
[^nihrigorguidance-e3]: NIH，Consideration of relevant biological variables。[证据](../../../../sources/notes/nihrigorguidance.md#e3)
[^nihrigorguidance-e6]: NIH，Consideration of relevant biological variables。[证据](../../../../sources/notes/nihrigorguidance.md#e6)
[^mak2014lost-e6]: Mak 等人 2014，Limitations of animal models in cancer research。[证据](../../../../sources/notes/mak2014lost.md#e6)
[^animalstudyregistry-e1]: animalstudyregistry.org 首页。[证据](../../../../sources/notes/animalstudyregistry.md#e1)
[^animalstudyregistry-e2]: animalstudyregistry.org 首页。[证据](../../../../sources/notes/animalstudyregistry.md#e2)
[^animalstudyregistry-e3]: animalstudyregistry.org 首页，Latest News。[证据](../../../../sources/notes/animalstudyregistry.md#e3)
[^kilkenny2009survey-e1]: Kilkenny 等人 2009，Abstract。[证据](../../../../sources/notes/kilkenny2009survey.md#e1)
[^kilkenny2009survey-e3]: Kilkenny 等人 2009，Results。[证据](../../../../sources/notes/kilkenny2009survey.md#e3)
[^kilkenny2009survey-e4]: Kilkenny 等人 2009，Results。[证据](../../../../sources/notes/kilkenny2009survey.md#e4)
[^voelkl2018reproducibility-e1]: Voelkl 等人 2018，Abstract。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e1)
[^voelkl2018reproducibility-e2]: Voelkl 等人 2018，Introduction。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e2)
[^voelkl2018reproducibility-e3]: Voelkl 等人 2018，Introduction。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e3)
[^voelkl2018reproducibility-e4]: Voelkl 等人 2018，Discussion。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e4)
[^voelkl2018reproducibility-e5]: Voelkl 等人 2018，Discussion。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e5)
[^voelkl2018reproducibility-e6]: Voelkl 等人 2018，Discussion。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e6)
[^voelkl2018reproducibility-e7]: Voelkl 等人 2018，Discussion。[证据](../../../../sources/notes/voelkl2018reproducibility.md#e7)
