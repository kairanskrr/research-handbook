# 合成与表征研究

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲怎样做好一项合成研究：设计路线，动手前评估危害，做反应、记录条件，后处理和纯化，表征产物，报告产率和底物范围，最后写出别人能照着做的实验部分。例子以有机合成为主，因为本文找到的具体规范多出自这个方向 `[本项目分析]`。

安全事故案例、新化合物的表征要求、谱图不能修、《Organic Syntheses》的独立核查和数据公开，[化学领域概况](../07_fields/chemistry/README.md)已经讲过，本文只在用到时加链接。做纳米材料、薄膜、器件的，见[材料工程篇](../07_fields/materials-engineering/README.md#一个循环制备表征测性能)；放大到更大规模的问题见[化学工程篇](../07_fields/chemical-engineering/README.md#实验室结果离工业还有多远放大)。本文引用的期刊规定和社论只代表各自的期刊：美国化学会《有机化学杂志》（The Journal of Organic Chemistry，下文简称 JOC）和《Organic Syntheses》的作者须知，以及《Organic Letters》主编的社论。投稿前要读目标期刊自己的作者须知 `[本项目分析]`。

**读完本文，你应该能：**

- 分清自己做的是方法学、目标分子合成，还是为别的研究制备化合物，知道各自要交什么证据；
- 把每个影响结果的条件都记下来，用"一次改一个条件"的办法找出关键条件；
- 如实报告产率，设计一张能说明适用范围和局限的底物范围表；
- 写出别人只看你的实验部分就能重复的步骤。

---

## 1. 这是什么研究，什么时候用

合成研究的成果是"做出了某种物质"或"找到了做某类物质的新办法"。证据是可重复的步骤、表征数据和产率 `[本项目分析]`。常见三种：

| | 合成方法学 | 目标分子合成（含全合成） | 为别的研究制备化合物 |
|---|---|---|---|
| 回答的问题 | 一个新反应、新试剂能做什么，不能做什么 | 怎样把一个特定分子做出来 | 给物理测量、生物测试、材料研究提供样品 |
| 核心证据 | 底物范围表、条件优化、可重复的通用步骤 | 每一步的步骤、产率和表征 | 结构证据和纯度 |
| 最容易出问题的地方 | 底物挑得太"好"、失败的例子不报 | 中间体表征不全、产率算错 | 纯度不够，影响后续测量 |

这张表是本文的归纳 `[本项目分析]`。期刊对"新"有要求。以 JOC 为例：它期待合成方法和全合成论文在策略、转化或路线上有概念上的新意，不只是把已有反应换一类底物、试剂或催化剂再做一遍[^acsjocguidelines-e30]。化合物要拿去做物理测量或生物测试的，JOC 要求证明纯度至少 95%[^acsjocguidelines-e4]。研究反应速率、机理或做计算的，不在本文范围，见[化学领域概况](../07_fields/chemistry/README.md#先分清自己做的是哪一类化学)。

## 2. 怎么做

### 第 1 步：查文献，设计路线

**怎么做。**

1. **先查目标物质是不是已知的。** 已知化合物按文献方法做的，JOC 只要求引用原文献，不必重写步骤（做了修改的除外）[^acsjocguidelines-e21]。
2. **做逆合成分析**（retrosynthetic analysis，从目标分子往回推原料）。阿斯利康的三位研究者 Kabeshov 等人在 2026 年的一篇评论文章里这样描述：看着目标分子问"怎样把它拆成有意义的片段"[^kabeshov2026retrosynthesis-e1]；有经验的化学家常常先定大的拆分策略，再决定具体用哪个官能团、哪种试剂[^kabeshov2026retrosynthesis-e2]。
3. **同时查安全信息。** 美国化学会的危害评估指南建议，检索文献时也要找相关步骤，以及所用过程和化学品已知的问题[^acs2015identifying-e10]。

**为什么。** 前人的步骤能告诉你哪里会出问题。重做一个已知反应，常常比从头摸索快 `[本项目分析]`。

**容易错在哪里。** 只查"能不能做"，不查"做的时候出过什么事" `[本项目分析]`。查文献的一般方法见主线章节[进入领域、探索文献](../01_from-interest-to-project/01_enter-a-field.md#3-顺着引用找出核心论文关键的人和发表处)；逆合成的具体技巧本文资料未涉及，请看有机合成教材或问导师。

### 第 2 步：每个新反应、每次放大前，先做危害评估

为什么要评估、用什么工具、哪些变化需要重新评估，见[化学领域概况的安全一节](../07_fields/chemistry/README.md#实验安全是研究的一部分不是额外的手续)。这里只强调一点：**按计划的规模评估。** 《Organic Syntheses》要求，每个反应前都针对计划的规模和所在的实验室，对每种化学品和每步操作做危害分析和风险评估[^orgsyninstructions-e13]。小量做过没事，不代表放大后也没事 `[本项目分析]`。2010 年得克萨斯理工大学的爆炸事故里，学生就是假定少量时管用的防护办法，量大时也同样管用[^csb2011texastech-e3]。

### 第 3 步：做反应，边做边看

**怎么做。** 按《Organic Syntheses》对实验步骤的要求来记录（别的期刊不一定要求这么细，但照着记最稳妥 `[本项目分析]`）：

- **加料**：所有试剂的加料顺序、加料用时、怎么加（注射器、滴液漏斗等）[^orgsyninstructions-e15]。
- **温度**：写反应液的温度，最好是内温（插在反应液里测的温度）[^orgsyninstructions-e15]；每次降温、升温都写清起止温度和用时[^orgsyninstructions-e16]。
- **监测**：写明怎样判断反应进行到哪一步。用薄层色谱（thin-layer chromatography，TLC，在硅胶板上点样展开、看斑点的快速检测方法）时，写展开剂、比移值（Rf，斑点走的距离与溶剂前沿走的距离之比）和显色方法[^orgsyninstructions-e17]。
- **现象**：反应液的颜色、是否均相，以及变色、放气、析出固体、放热等变化[^orgsyninstructions-e11]。
- **搅拌**：Schuurmans 等人 2026 年一篇讨论搅拌的观点文章建议，明确报告搅拌条件、容器形状和加料方式[^schuurmans2026stirring-e1]。文中介绍了另一个课题组的发现：同一个磁力搅拌器上并排做同样的反应，瓶子的位置和高度不同，结果就明显不同[^schuurmans2026stirring-e4]。

**为什么。** 按 Schuurmans 等人的解释，慢慢滴加能避免局部浓度过高、让热量逐渐散掉，也有助于保持选择性[^schuurmans2026stirring-e2]；搅拌不足会造成局部过热，可能导致溶剂沸腾、分解甚至反应失控[^schuurmans2026stirring-e3]。所以加料和搅拌既关系到结果，也关系到安全。

**容易错在哪里。** 只写"搅拌过夜"。Schäfer 等人 2024 年的观点文章指出，发表的步骤里常被忽略的条件有：搅拌速度、反应时长（包括"过夜"）、底物和试剂的纯度[^schafer2024sensitivity-e3]。

### 第 4 步：优化条件，把每个变量都记下来

**怎么做。**

1. **记全变量。** 每次实验至少记：各物料的用量（质量和物质的量）和当量（equivalent，equiv，某试剂的物质的量是限量反应物的几倍）、浓度、温度、时间、加料顺序、试剂来源、批号和纯度 `[本项目分析]`。记录本的一般规矩见[化学领域概况](../07_fields/chemistry/README.md#实验记录本写给事后核查的人看)。
2. **一次只改一个条件。** 灵敏度筛查（sensitivity screen）是德国明斯特大学 Glorius 课题组为解决"重复不出来"的问题提出的办法[^schafer2024sensitivity-e9]：一次只把一个条件往高、往低两个方向改，其余不变，看产率怎么变，就知道排查时该先查哪个条件[^schafer2024sensitivity-e2]。改动幅度要够大：该组在 2024 年的文章里承认，原先建议的浓度变化 ±10% 常常不够，并说很多课题组已改用至少 ±50%[^schafer2024sensitivity-e6]。
3. **需要更全面时，用实验设计方法。** 实验设计（Design of Experiments，DoE，按统计方案同时改几个条件）最能看清反应对条件有多敏感，但可能最费时费钱[^schafer2024sensitivity-e8]；作者把灵敏度筛查定位为初步工具，深入评估还要靠实验设计等方法[^schafer2024sensitivity-e7]。
4. **用量要有理由。** 试剂明显过量（例如超过 1.5 当量）时，《Organic Syntheses》要求说明为什么要过量，最好说明少用会怎样[^orgsyninstructions-e20]。

**为什么。** 很多看似琐碎的条件会改变结果。Schäfer 等人的观点文章介绍了两个例子：一个课题组把羧酸原料从 98.9% 重新纯化到 99.9%，产率提高了 23%[^schafer2024sensitivity-e4]；另一个课题组发现，不同批次的商品钯预催化剂给出的产率差别相当大[^schafer2024sensitivity-e5]。他们还指出，即使支持信息写得详细，换个实验室、换个人做，条件也可能不一样[^schafer2024sensitivity-e1]。

**容易错在哪里。** 有效数字乱写。《Organic Syntheses》提醒：写"5.00 equiv"就意味着用量要控制到 0.01 当量；溶液浓度要用物质的量浓度，不用百分比[^orgsyninstructions-e19]。

### 第 5 步：后处理和纯化

**怎么做。** 后处理（workup）指反应结束后把产物从反应液里分出来的操作，如淬灭（加入试剂终止反应）、萃取、干燥、浓缩 `[本项目分析]`。具体要写：

- **后处理**：《Organic Syntheses》要求写淬灭剂的组成和体积、加入用时和温度；萃取的次数、每次的体积、分液漏斗的大小；浓缩的方法、压力和温度[^orgsyninstructions-e18]。
- **纯化**：《Organic Syntheses》要求步骤写全[^orgsyninstructions-e25]。用柱色谱等方法纯化时，JOC 要求写明固定相和洗脱溶剂；一系列化合物用了不同的溶剂配比，就每个化合物分别写[^acsjocguidelines-e27]。
- **不纯化直接用于下一步**：《Organic Syntheses》要求另外说明怎样纯化一份样品，并给出纯品和粗品的表征数据[^orgsyninstructions-e14]。

**容易错在哪里。** 多步合成里，前一步得到的量比下一步投进去的还少。《Organic Syntheses》明确要求前一步的产量不少于下一步的用量[^orgsyninstructions-e23]。

### 第 6 步：表征：证明"是什么"和"有多纯"

JOC 的基本要求（氢谱、碳谱，加高分辨质谱或元素分析；熔点和高分辨质谱都不能证明纯度）和"谱图不能修"，见[化学领域概况](../07_fields/chemistry/README.md#新化合物证明是什么和有多纯)[^acsjocguidelines-e3][^acsjocguidelines-e5]。规划表征时，再注意三点：

1. **先想清楚每个化合物要证明什么。** 新化合物要证明结构和纯度；按 JOC 的要求，已知化合物用新方法或改进的方法做出来的，也要给纯度证据[^acsjocguidelines-e19]。
2. **关键节点数据要全。** 合成路线上的分叉点、汇合点和最后的新化合物，JOC 要求必须有元素分析或高分辨质谱数据[^acsjocguidelines-e20]。
3. **纯度要用"算产率的那批"测。** 《Organic Syntheses》要求，纯度数据要用计算产率的那批产物测，而不是另外再纯化过的样品[^orgsyninstructions-e12]。纯度可以用加内标（已知量的参照物）的定量核磁（quantitative NMR，qNMR）、气相色谱或高效液相色谱测[^orgsyninstructions-e21]。

### 第 7 步：如实报告产率

**怎么做。** 产率要报分离纯化后称重的结果（JOC 的要求）[^acsjocguidelines-e9]，产率高得不现实的提醒见[化学领域概况](../07_fields/chemistry/README.md#新化合物证明是什么和有多纯)。这里补三点：

- **转化率要标明。** 转化率指原料变成产物的比例，是用色谱或波谱测的，不是称出来的。JOC 要求表格里用转化率时，在列标题或脚注写明是哪种量，并给出几个代表性例子的分离产率[^acsjocguidelines-e25]。
- **规模不同要写清。** 各例子规模不同时，JOC 要求每个产物都写出限量反应物的质量和物质的量[^acsjocguidelines-e24]。
- **多次实验报范围。** 《Organic Syntheses》允许把质量、产率、纯度按范围报告，产率取整到百分之一[^orgsyninstructions-e22]。多次产率相差超过 10%，可能还有没找到的影响因素[^orgsyninstructions-e7]，这时回到第 4 步去找 `[本项目分析]`。

**为什么。** Bergman 和 Danheiser 在 2016 年的一篇社论里，把只报最好的一次产率或选择性列为不当行为[^bergman2016reproducibility-e4]。

### 第 8 步：设计底物范围表，报告失败的例子

底物范围（substrate scope）指一个新方法对哪些底物管用、对哪些不管用。方法学论文一般用一张表来展示 `[本项目分析]`。下面多处引用《Organic Letters》主编 Kozlowski 2022 年的社论，它代表该刊编辑的看法，不是全领域的规定。

**怎么做。**

1. **按问题挑底物，不按数量。** Kozlowski 举例说，好的底物各自回答一个问题，例如位阻大不大、某个官能团能不能耐受、换成酮或烷基醛行不行[^kozlowski2022substrate-e4]。她还引用一条审稿意见：选底物是为了说明反应的某个重要事实，不是为了填满表格[^kozlowski2022substrate-e10]。
2. **把"明显该试"的底物试了。** 她引用的一条读者意见说：如果你的芳基只有间位和对位取代，读者会想知道邻位怎样[^kozlowski2022substrate-e14]。
3. **报告失败和低产率的例子。** Kozlowski 建议在正文或表里放几个低产率或不反应的例子，所有失败的底物可以列表放进支持信息[^kozlowski2022substrate-e8]。
4. **讨论局限和竞争方法。** 《Organic Syntheses》要求讨论部分写清方法的适用范围和局限，并介绍和引用能完成同一转化的其他方法[^orgsyninstructions-e24]。
5. **至少放大做一个例子。** JOC 要求，例子都在不到 1 毫摩尔规模做的新方法，至少要有一个 1 毫摩尔规模的例子[^acsjocguidelines-e26]。

**为什么。** 明斯特大学 Glorius 课题组的 Rana 等人在 2024 年的论文里认为，底物范围表常有两种偏倚：一是选择偏倚，优先挑预计产率高、容易得到的底物；二是报告偏倚，多数论文不报告失败或低产率的结果[^rana2024standardizing-e1]。他们强调，负面结果对划清新反应的适用边界同样重要[^rana2024standardizing-e3]；失败的例子发得少，是因为研究者担心影响发表[^rana2024standardizing-e4]。他们还指出，化学结构的组合太多，再好的底物范围也总是不完整的[^rana2024standardizing-e2]。所以说清"哪里不行"，能帮读者判断方法能不能用在自己的分子上 `[本项目分析]`。

**容易错在哪里。** 为了凑数量，堆很多结构相近的底物 `[本项目分析]`。Kozlowski 说，编辑部越来越多收到底物超过 50 个的投稿[^kozlowski2022substrate-e1]。想更省力地检查官能团能不能耐受，她提到可以改为筛选添加剂[^kozlowski2022substrate-e5]。Rana 等人介绍过他们课题组早先提出的"稳健性筛查"：往反应里加入一组标准化的添加剂，看它们对结果的影响，以此估计反应的适用边界[^rana2024standardizing-e6]。

> **不同的看法：底物范围要多大？**
> - **多样比数量重要。** 2022 年 9 月，Kozlowski 在推特上发起一次投票，1909 票中 88% 支持少于 30 个例子[^kozlowski2022substrate-e2]；她的结论是底物范围小一点可以接受，前提是足够多样[^kozlowski2022substrate-e3]。对新方法，《Organic Letters》编辑部一般建议 10–20 个多样的底物，其中包括不反应或低产率的[^kozlowski2022substrate-e11]。Rana 等人也认为，底物范围不一定要更大，而要更多样、去掉偏倚[^rana2024standardizing-e5]。
> - **大的范围有时也有价值。** 同一篇社论承认，上面的建议不是硬性规定，有时确实需要更多底物[^kozlowski2022substrate-e12]；在完整论文里，大的底物范围可以展示可重复性和稳健性，还能为机器学习提供数据[^kozlowski2022substrate-e13]。
>
> 实际操作中：先按"每个底物回答一个问题"挑一组多样的底物，再看目标期刊和文章类型（快报还是完整论文）决定要不要扩大。那次投票只是一次网络投票，不代表整个领域的统一标准 `[本项目分析]`。

### 第 9 步：写别人能重复的实验部分和支持信息

**怎么做。** 以 JOC 为例，它要求实验部分详细到别人能重复[^acsjocguidelines-e31]。具体到每个反应（前四条是 JOC 的要求，其余各条注明出处）：

- [ ] 反应物、试剂、催化剂的量同时写质量和物质的量；写溶剂体积和反应时间[^acsjocguidelines-e22]
- [ ] 通用步骤只写当量时，还要写浓度（限量反应物在反应液中的物质的量浓度）[^acsjocguidelines-e23]
- [ ] 加热反应写温度和热源（油浴、加热套等）[^acsjocguidelines-e28]
- [ ] 指出工作中意外的、新的或重大的危险[^acsjocguidelines-e16]
- [ ] 第 3、5 步记下的加料、温度、监测、后处理和纯化细节都写进去（《Organic Syntheses》）[^orgsyninstructions-e15][^orgsyninstructions-e18]
- [ ] 产率按第 7 步的要求报告（JOC）[^acsjocguidelines-e9]；数据格式上，美国化学会鼓励提供机器可读的数据[^acsdatapolicy-e5]，见[化学领域概况](../07_fields/chemistry/README.md#数据支持信息原始数据与-fair)
- [ ] 投稿前做一次内部核查：《Organic Syntheses》要求每个反应按所写规模至少做两次，并建议请一位没参与的同事来做[^orgsyninstructions-e6]；Bergman 和 Danheiser 也建议请不熟悉这个方向的同事只看支持信息重复一个代表性例子[^bergman2016reproducibility-e8]

> **不同的看法：试剂来源要不要写？**
> - **《Organic Syntheses》**：所有原料和试剂都要写明来源，商品试剂写纯度[^orgsyninstructions-e8]。
> - **JOC**：一般不写来源，只有三种情况要写：不常见的原料、作者怀疑来源会影响结果的材料、催化剂；后两种还要写纯度[^acsjocguidelines-e29]。
>
> 实际操作中：论文按目标期刊的规定写；但记录本里每种试剂的来源、批号和纯度都要记全，因为原料纯度和催化剂批次可能明显影响产率（见第 4 步）`[本项目分析]`。

---

## 3. 检查清单

**必须做到**（以下都是具体期刊的要求，投别的期刊以其须知为准）

- [ ] 每个新反应、每次放大前，按计划的规模做危害评估（《Organic Syntheses》）[^orgsyninstructions-e13]
- [ ] 产率是分离纯化后称重的结果，同时给质量和百分比[^acsjocguidelines-e9]；转化率另行标明[^acsjocguidelines-e25]（JOC）
- [ ] 新化合物有结构和纯度证据；用新方法做的已知化合物也有纯度证据（JOC）[^acsjocguidelines-e19]
- [ ] 关键节点化合物有元素分析或高分辨质谱数据（JOC）[^acsjocguidelines-e20]
- [ ] 实验部分写全用量（质量和物质的量）、溶剂体积、时间、温度和热源（JOC）[^acsjocguidelines-e22][^acsjocguidelines-e28]
- [ ] 纯化写明固定相和洗脱溶剂（JOC）[^acsjocguidelines-e27]
- [ ] 不只报告最好的一次结果（Bergman 和 Danheiser 的社论）[^bergman2016reproducibility-e4]

**做到更好**

- [ ] 排查重复问题时，用"一次改一个条件"的灵敏度筛查找出关键条件[^schafer2024sensitivity-e2]
- [ ] 报告搅拌条件、容器和加料方式（Schuurmans 等人的建议）[^schuurmans2026stirring-e1]
- [ ] 底物范围表包含低产率和不反应的例子，失败底物全表放进支持信息（Kozlowski 的建议）[^kozlowski2022substrate-e8]
- [ ] 讨论局限和竞争方法（《Organic Syntheses》）[^orgsyninstructions-e24]
- [ ] 投稿前请同事只看支持信息重复一个例子[^bergman2016reproducibility-e8]

**这些情况可以不做，不算缺陷**

- 以合成为主的工作，JOC 不设最低纯度，但要如实记录达到的纯度[^acsjocguidelines-e4]
- 底物范围里没有药物分子等复杂底物：Kozlowski 认为这些分子在能免费获得之前，不应是发表的前提[^kozlowski2022substrate-e6]
- 按文献方法制备的已知化合物，不重写步骤，只引用原文献（JOC）[^acsjocguidelines-e21]

**审稿时常见、但不成立的批评**

- **"有些产率太低，不该放进来。"** Kozlowski 在社论里提到，作者因为担心审稿人不满而不敢放负面例子[^kozlowski2022substrate-e7]；她请《Organic Letters》的审稿人记住：负面结果不一定坏，例子多也不一定好[^kozlowski2022substrate-e9]。

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 记录本不记试剂批号和纯度 | 原料纯度、催化剂批次可能明显影响产率（Schäfer 等人介绍的例子）[^schafer2024sensitivity-e4][^schafer2024sensitivity-e5] |
| 用核磁测的转化率当产率，又不标明 | JOC 要求标明是哪种量，并给出分离产率[^acsjocguidelines-e25] |
| 纯度用额外纯化过的样品测，产率却按粗一点的那批算 | 《Organic Syntheses》要求纯度用算产率的那批测[^orgsyninstructions-e12] |
| 底物范围只放成功的例子 | Rana 等人称之为报告偏倚，读者不知道方法哪里不行[^rana2024standardizing-e1] |
| 用很多结构相近的底物凑数量 | 选底物是为了说明反应的某个重要事实，不是为了填满表格（Kozlowski 引用的审稿意见）[^kozlowski2022substrate-e10] |
| 通用步骤只写当量，不写浓度 | 别人不知道该加多少溶剂；JOC 要求写浓度[^acsjocguidelines-e23] |
| 多次产率相差很大，只报最好的那次 | 相差超过 10% 可能说明还有没找到的因素[^orgsyninstructions-e7]；只报最好的一次是不当行为[^bergman2016reproducibility-e4] |

---

## 5. 延伸阅读

- **《Organic Syntheses》作者须知**：从加料、温度、监测到后处理、纯化，逐项告诉你实验步骤该写到多细。写实验部分前对照一遍。
- **Kozlowski 2022，On the Topic of Substrate Scope（Organic Letters 社论）**：三页，讲底物范围怎么挑、失败的例子怎么报，还引了不少一线化学家的意见。
- **Rana 等人 2024（ACS Central Science，开放获取）**：讲底物范围表里的选择偏倚和报告偏倚，并提出一种按化学空间挑选底物的标准化办法。
- **Schäfer、Lückemeier 和 Glorius 2024（Chemical Science，开放获取）**：介绍灵敏度筛查的做法，适合优化条件和排查重复不出来的问题时读。
- **Schuurmans 等人 2026（ACS Central Science，开放获取）**：讲搅拌和加料怎样影响结果和安全。

[^acsjocguidelines-e19]: JOC 作者须知，Compound Characterization Data。[证据](../../sources/notes/acsjocguidelines.md#e19)
[^acsjocguidelines-e20]: JOC 作者须知，Compound Characterization Data。[证据](../../sources/notes/acsjocguidelines.md#e20)
[^acsjocguidelines-e21]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e21)
[^acsjocguidelines-e22]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e22)
[^acsjocguidelines-e9]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e9)
[^acsjocguidelines-e23]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e23)
[^acsjocguidelines-e24]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e24)
[^acsjocguidelines-e25]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e25)
[^acsjocguidelines-e26]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e26)
[^acsjocguidelines-e27]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e27)
[^acsjocguidelines-e28]: JOC 作者须知，Synthesis Experiments。[证据](../../sources/notes/acsjocguidelines.md#e28)
[^acsjocguidelines-e29]: JOC 作者须知，General Experimental Methods。[证据](../../sources/notes/acsjocguidelines.md#e29)
[^acsjocguidelines-e30]: JOC 作者须知，Scope of the Journal (a)。[证据](../../sources/notes/acsjocguidelines.md#e30)
[^acsjocguidelines-e4]: JOC 作者须知，Purity。[证据](../../sources/notes/acsjocguidelines.md#e4)
[^acsjocguidelines-e31]: JOC 作者须知，Experimental Section。[证据](../../sources/notes/acsjocguidelines.md#e31)
[^acsjocguidelines-e3]: JOC 作者须知，NMR。[证据](../../sources/notes/acsjocguidelines.md#e3)
[^acsjocguidelines-e5]: JOC 作者须知，Purity。[证据](../../sources/notes/acsjocguidelines.md#e5)
[^acsjocguidelines-e16]: JOC 作者须知，Emphasis on Chemical Safety。[证据](../../sources/notes/acsjocguidelines.md#e16)
[^orgsyninstructions-e15]: Organic Syntheses 作者须知，Reaction Procedure。[证据](../../sources/notes/orgsyninstructions.md#e15)
[^orgsyninstructions-e16]: Organic Syntheses 作者须知，Reaction Procedure。[证据](../../sources/notes/orgsyninstructions.md#e16)
[^orgsyninstructions-e17]: Organic Syntheses 作者须知，Reaction Procedure。[证据](../../sources/notes/orgsyninstructions.md#e17)
[^orgsyninstructions-e11]: Organic Syntheses 作者须知，Reaction Procedure。[证据](../../sources/notes/orgsyninstructions.md#e11)
[^orgsyninstructions-e18]: Organic Syntheses 作者须知，Reaction Workup。[证据](../../sources/notes/orgsyninstructions.md#e18)
[^orgsyninstructions-e19]: Organic Syntheses 作者须知，Reagents（有效数字和浓度）。[证据](../../sources/notes/orgsyninstructions.md#e19)
[^orgsyninstructions-e20]: Organic Syntheses 作者须知，Scale / reproducibility。[证据](../../sources/notes/orgsyninstructions.md#e20)
[^orgsyninstructions-e8]: Organic Syntheses 作者须知，Common Omissions。[证据](../../sources/notes/orgsyninstructions.md#e8)
[^orgsyninstructions-e12]: Organic Syntheses 作者须知，Common Omissions。[证据](../../sources/notes/orgsyninstructions.md#e12)
[^orgsyninstructions-e21]: Organic Syntheses 作者须知，Characterization。[证据](../../sources/notes/orgsyninstructions.md#e21)
[^orgsyninstructions-e22]: Organic Syntheses 作者须知，Scale / reproducibility。[证据](../../sources/notes/orgsyninstructions.md#e22)
[^orgsyninstructions-e7]: Organic Syntheses 作者须知，Scale / reproducibility。[证据](../../sources/notes/orgsyninstructions.md#e7)
[^orgsyninstructions-e23]: Organic Syntheses 作者须知，Common Omissions。[证据](../../sources/notes/orgsyninstructions.md#e23)
[^orgsyninstructions-e24]: Organic Syntheses 作者须知，Discussion Section。[证据](../../sources/notes/orgsyninstructions.md#e24)
[^orgsyninstructions-e13]: Organic Syntheses 作者须知，Safety（Note 1）。[证据](../../sources/notes/orgsyninstructions.md#e13)
[^orgsyninstructions-e25]: Organic Syntheses 作者须知，Common Omissions。[证据](../../sources/notes/orgsyninstructions.md#e25)
[^orgsyninstructions-e14]: Organic Syntheses 作者须知，Common Omissions。[证据](../../sources/notes/orgsyninstructions.md#e14)
[^orgsyninstructions-e6]: Organic Syntheses 作者须知，Scale / reproducibility。[证据](../../sources/notes/orgsyninstructions.md#e6)
[^acs2015identifying-e10]: ACS 2015，9.4 Job Hazard Analysis。[证据](../../sources/notes/acs2015identifying.md#e10)
[^csb2011texastech-e3]: CSB 2011，4.0 Incident Description。[证据](../../sources/notes/csb2011texastech.md#e3)
[^bergman2016reproducibility-e4]: Bergman & Danheiser 2016，Sources of Irreproducibility。[证据](../../sources/notes/bergman2016reproducibility.md#e4)
[^bergman2016reproducibility-e8]: Bergman & Danheiser 2016，Recommendations。[证据](../../sources/notes/bergman2016reproducibility.md#e8)
[^acsdatapolicy-e5]: ACS 研究数据政策，Data Availability Statements。[证据](../../sources/notes/acsdatapolicy.md#e5)
[^kabeshov2026retrosynthesis-e1]: Kabeshov 等人 2026，第 2 段。[证据](../../sources/notes/kabeshov2026retrosynthesis.md#e1)
[^kabeshov2026retrosynthesis-e2]: Kabeshov 等人 2026，第 2 段。[证据](../../sources/notes/kabeshov2026retrosynthesis.md#e2)
[^schafer2024sensitivity-e1]: Schäfer 等人 2024，Introduction。[证据](../../sources/notes/schafer2024sensitivity.md#e1)
[^schafer2024sensitivity-e2]: Schäfer 等人 2024，Introduction。[证据](../../sources/notes/schafer2024sensitivity.md#e2)
[^schafer2024sensitivity-e3]: Schäfer 等人 2024，General parameters。[证据](../../sources/notes/schafer2024sensitivity.md#e3)
[^schafer2024sensitivity-e4]: Schäfer 等人 2024，General parameters。[证据](../../sources/notes/schafer2024sensitivity.md#e4)
[^schafer2024sensitivity-e5]: Schäfer 等人 2024，Homogeneous catalysis and cross-coupling reactions。[证据](../../sources/notes/schafer2024sensitivity.md#e5)
[^schafer2024sensitivity-e6]: Schäfer 等人 2024，Introduction。[证据](../../sources/notes/schafer2024sensitivity.md#e6)
[^schafer2024sensitivity-e7]: Schäfer 等人 2024，Conclusion and outlook。[证据](../../sources/notes/schafer2024sensitivity.md#e7)
[^schafer2024sensitivity-e8]: Schäfer 等人 2024，Introduction。[证据](../../sources/notes/schafer2024sensitivity.md#e8)
[^schafer2024sensitivity-e9]: Schäfer 等人 2024，Introduction。[证据](../../sources/notes/schafer2024sensitivity.md#e9)
[^schuurmans2026stirring-e1]: Schuurmans 等人 2026，搅拌与加料一节。[证据](../../sources/notes/schuurmans2026stirring.md#e1)
[^schuurmans2026stirring-e2]: Schuurmans 等人 2026，搅拌与加料一节。[证据](../../sources/notes/schuurmans2026stirring.md#e2)
[^schuurmans2026stirring-e3]: Schuurmans 等人 2026，搅拌与安全一节。[证据](../../sources/notes/schuurmans2026stirring.md#e3)
[^schuurmans2026stirring-e4]: Schuurmans 等人 2026，磁力搅拌器位置一节。[证据](../../sources/notes/schuurmans2026stirring.md#e4)
[^kozlowski2022substrate-e1]: Kozlowski 2022，开头。[证据](../../sources/notes/kozlowski2022substrate.md#e1)
[^kozlowski2022substrate-e2]: Kozlowski 2022，开头。[证据](../../sources/notes/kozlowski2022substrate.md#e2)
[^kozlowski2022substrate-e3]: Kozlowski 2022，开头。[证据](../../sources/notes/kozlowski2022substrate.md#e3)
[^kozlowski2022substrate-e4]: Kozlowski 2022，Figure 2 说明段。[证据](../../sources/notes/kozlowski2022substrate.md#e4)
[^kozlowski2022substrate-e5]: Kozlowski 2022，Figure 2 说明段。[证据](../../sources/notes/kozlowski2022substrate.md#e5)
[^kozlowski2022substrate-e6]: Kozlowski 2022，Drug-like Structures or Not?。[证据](../../sources/notes/kozlowski2022substrate.md#e6)
[^kozlowski2022substrate-e7]: Kozlowski 2022，Substrates That Do Not Work。[证据](../../sources/notes/kozlowski2022substrate.md#e7)
[^kozlowski2022substrate-e8]: Kozlowski 2022，Substrates That Do Not Work。[证据](../../sources/notes/kozlowski2022substrate.md#e8)
[^kozlowski2022substrate-e9]: Kozlowski 2022，Reviewers。[证据](../../sources/notes/kozlowski2022substrate.md#e9)
[^kozlowski2022substrate-e10]: Kozlowski 2022，Reviewers。[证据](../../sources/notes/kozlowski2022substrate.md#e10)
[^kozlowski2022substrate-e11]: Kozlowski 2022，Reasonable Substrate Scope Examples。[证据](../../sources/notes/kozlowski2022substrate.md#e11)
[^kozlowski2022substrate-e12]: Kozlowski 2022，Reasonable Substrate Scope Examples。[证据](../../sources/notes/kozlowski2022substrate.md#e12)
[^kozlowski2022substrate-e13]: Kozlowski 2022，Reasonable Substrate Scope Examples。[证据](../../sources/notes/kozlowski2022substrate.md#e13)
[^kozlowski2022substrate-e14]: Kozlowski 2022，Substrates That Do Not Work。[证据](../../sources/notes/kozlowski2022substrate.md#e14)
[^rana2024standardizing-e1]: Rana 等人 2024，Introduction。[证据](../../sources/notes/rana2024standardizing.md#e1)
[^rana2024standardizing-e2]: Rana 等人 2024，Introduction。[证据](../../sources/notes/rana2024standardizing.md#e2)
[^rana2024standardizing-e3]: Rana 等人 2024，Results and Discussion。[证据](../../sources/notes/rana2024standardizing.md#e3)
[^rana2024standardizing-e4]: Rana 等人 2024，Results and Discussion。[证据](../../sources/notes/rana2024standardizing.md#e4)
[^rana2024standardizing-e5]: Rana 等人 2024，Conclusions。[证据](../../sources/notes/rana2024standardizing.md#e5)
[^rana2024standardizing-e6]: Rana 等人 2024，Introduction。[证据](../../sources/notes/rana2024standardizing.md#e6)
