# 语言记录与语言学田野调查

> **状态**：初稿，待审阅 · **最后更新**：2026-10-06

本文讲怎样做一个**语言记录**（language documentation）项目：和说这种语言的社区一起，把这种语言录下来、转写、翻译、注释，存进档案馆，再从这批材料里做分析、写论文。对社区和发音人的伦理责任、数据引用、《奥斯汀语言学数据引用原则》，[领域概况](../README.md#语言学田野调查和濒危语言)已经讲过，这里不重复，只讲具体怎么做。

**先说清资料的分量。** 本文的资料有：

- 美国语言学会（Linguistic Society of America，LSA）1992、2010、2019 年的几份声明和决议。这是一个美国学会的主张。
- 澳大利亚的语言档案馆 PARADISEC（太平洋及区域濒危文化数字资源档案馆）网站上的存档指南。它的格式、命名等要求只代表这一家档案馆。
- 德国两家机构联合制定的《莱比锡注释规则》。
- 期刊《语言记录与保护》（Language Documentation & Conservation）上的几篇文章，其中多数出自 2018 年的一期专刊。每篇代表作者本人的看法。
- 语言学者 Bird 和 Simons 谈数字记录怎样长期可用的文章（本文依据的是它 2002 年的预印本），以及 Berez-Kroeker 等人 2018 年关于数据引用的立场声明。

它们是这些机构和作者的建议，不是全世界通行的规矩。**各国的研究许可、伦理审查和版权法不同，以你所在国家、机构和研究地的规定为准** `[本项目分析]`。

**读完本文，你应该能：**

- 判断自己的课题是不是语言记录，以及它和访谈研究、口述历史有什么不同；
- 和社区一起定目标、分角色，用社区能接受的方式取得同意；
- 按"录音 → 元数据 → 转写翻译 → 行间注释 → 存档"的顺序整理材料；
- 从一批记录材料里做出经得起核查的分析。

---

## 1. 这是什么研究，什么时候用

**语言记录**指创建、注释、保存和传播一种语言的透明记录，这是美国语言学者 Good 2018 年给的说法[^good2018scope-e1]。Bird 和 Simons 在文中引用了语言学者 Himmelmann 1998 年的定义：语言记录的目标，是全面记录一个言语社区特有的语言实践[^bird2002portability-e8]（本项目没有读 Himmelmann 原文，这里据 Bird 和 Simons 的引用）。Good 认为，多数记录项目的核心是：自然语料的录音，加上元数据，加上时间对齐的转写、翻译和形态分析[^good2018scope-e2]。

**记录语料里可以有诱导材料。** 据语言学者 Riesberg 2018 年的转述，Himmelmann 主张把"记录"（收集和整理材料）和"描写"（写语法书、分析结构）这两种工作分开[^riesberg2018adequacy-e2]。有人由此认为，记录语料里完全不该有诱导材料（按研究者的问题让发音人说出的形式）；Riesberg 认为这种理解走过了头[^riesberg2018adequacy-e1][^riesberg2018adequacy-e2]。所以，做记录不必回避诱导和分析 `[本项目分析]`。

| | 语言记录 | 访谈研究 | 口述历史 |
|---|---|---|---|
| 关心什么 | 语言本身：怎么说、有哪些说法 | 人们对某个问题的经验和看法 | 一个人对过去的回忆 |
| 主要材料 | 多种场合、多种体裁的录音录像，加转写、翻译、注释 | 访谈录音和转录稿 | 访谈录音、转录稿、索引 |
| 材料去向 | 存进语言档案馆，供社区和后人使用 | 常只供本项目分析 | 存进收藏机构，供后人使用 |
| 署名 | 看发音人和社区的意愿 | 常默认匿名 | 看受访者的授权 |

上表为本项目的概括 `[本项目分析]`。访谈技巧可借[访谈研究](../../computer-science/research-types/interview_study.md)；授权、存档的做法和[口述历史](../../history-archaeology/research-types/oral_history.md)相近，但口述历史关心说了**什么**，语言记录还关心**怎么说** `[本项目分析]`。

**什么时候做**：你要研究的语言或方言缺少记录；或者你的问题需要真实语料，而现有资料没有 `[本项目分析]`。

## 2. 怎么做

### 第一步：和社区一起规划项目

**怎么做：**

- **先建关系，再谈项目。** 加拿大语言学者 Czaykowska-Higgins 根据她在加拿大原住民社区的经验认为，任何语言田野工作最重要的前提，是建立并维持稳固、互相尊重、互惠和信任的工作关系[^czaykowskahiggins2009research-e1]。协商要经常、定期进行[^czaykowskahiggins2009research-e3]。美国语言学会 1992 年的声明也说，这种关系由发音人和语言学者共同界定，什么时候能工作由发音人的生活节奏决定[^lsa1992humansubjects-e5]。
- **一起定目标。** 美国语言学会 2019 年的伦理声明要求从规划的最早阶段请社区参与（见[领域概况](../README.md#语言学田野调查和濒危语言)）[^lsa2019ethics-e18]；如果社区愿意，就让社区一起定研究问题、收集方式、分析和传播[^lsa2019ethics-e19]。以美国原住民社区成员身份写作的语言学者 Leonard[^leonard2018decolonialism-e5] 主张更进一步：不只是"考虑"社区需求，而是**从社区需求出发**来构想项目[^leonard2018decolonialism-e2]。
- **弄清谁能代表社区。** 同一份声明要求设法确认，有没有人能正当地代表社区商定研究条件[^lsa2019ethics-e20]。Czaykowska-Higgins 说，在大多数加拿大原住民社区，长者总是合作的核心[^czaykowskahiggins2009research-e2]。
- **分好角色。** Czaykowska-Higgins 认为，和语言学者一起记录的社区成员本身就是研究者和专家，不只是"提供材料的人"[^czaykowskahiggins2009research-e5]；语言学者也不该把自己当成来拯救社区的英雄[^czaykowskahiggins2009research-e6]。
- **把约定写下来。** 她列出的合作成果包括：商定研究流程、各方都接受的规程、各方的工作计划、谅解备忘录[^czaykowskahiggins2009research-e7][^czaykowskahiggins2009research-e8]。给参与者什么回报（报酬、正式承认贡献、让社区受益等）也要想好[^lsa2019ethics-e21]。
- **事先查清许可和版权。** Seyfeddinipur 等指出，有些地方做语言记录要研究许可，许可可能限制数据访问[^seyfeddinipur2019public-e9]；按知识产权法，录音的版权一般归录音的人，而不是说话的人[^seyfeddinipur2019public-e10]。PARADISEC 提醒，在大学工作或拿了科研经费的人，存档前可能要先取得资助方或雇主的许可[^paradisecdeposit-e12]。
- **一开始就联系档案馆**[^berezkroeker2018reproducible-e13]，商量许可、访问条件和继任计划（将来谁负责这些材料）[^seyfeddinipur2019public-e11]。

**容易错在哪里**：Czaykowska-Higgins 提醒，人们容易忽视或低估以常识和敏感待人所需要的时间[^czaykowskahiggins2009research-e4]。这部分时间要写进计划 `[本项目分析]`。

### 第二步：用社区能接受的方式取得同意

一般原则（知情同意、全程自愿、署名还是匿名）见[领域概况](../README.md#本领域的规范和伦理)；"同意是一个过程"在[社会学](../../sociology/README.md#伦理美国社会学会准则与英国社会学会声明)也讲过；授权文件怎么准备，可参考[口述历史第四步](../../history-archaeology/research-types/oral_history.md#第四步讲清楚签好授权书)。语言记录特有的几点，下面多数来自 Seyfeddinipur 等 2019 年的文章（作者是来自多国大学、语言档案馆和国际机构的 30 位学者和工作者）：

- **个人同意和集体同意都要。** 故事、歌曲可能分属个人、家族或社区，谁有权同意可能很复杂[^seyfeddinipur2019public-e1]。材料归谁、谁能访问，要尽早和个人及整个社区讨论，并定期继续讨论[^seyfeddinipur2019public-e2]。
- **问具体的访问问题**，例如：谁能听、看、读这段材料？全世界都能看，意味着什么[^seyfeddinipur2019public-e3]？可以办讨论会来谈[^seyfeddinipur2019public-e4]。
- **不一定要签字。** 不适合书面同意时，可以录下口头同意，以及和社区的相关讨论[^seyfeddinipur2019public-e5]。
- **同意会变。** 个人和社区的看法会随时间变化[^seyfeddinipur2019public-e6]；美国语言学会要求每个阶段的参与都完全自愿[^lsa2019ethics-e3]。
- **同意要包括访问级别**，讨论结果写进元数据[^seyfeddinipur2019public-e7]。他们认为，至少在研究早期，宁可谨慎、先限制访问[^seyfeddinipur2019public-e8]。
- **匿名不一定做得到。** 在小社会里可能根本没法匿名[^seyfeddinipur2019public-e13]；有的发音人希望因贡献而被署名[^lsa1992humansubjects-e3]。事先问清，按对方的选择做 `[本项目分析]`。

### 第三步：选发音人和语料类型

**两类材料都要。** 美国语言学者 Bowern 2018 年写道：诱导和翻译更能说明哪些结构可能、哪些不可能；自然互动也是结构数据的宝贵来源[^bowern2018fieldwork-e1]。还有一种折中办法：用图片等视觉刺激和结构一致的任务，不靠翻译句子、不要求发音人精通通用语，也能拿到受控的数据[^bowern2018fieldwork-e2][^bowern2018fieldwork-e3]。Bowern 说，这类工具里可能最有名的，是荷兰奈梅亨马普研究所 1992—2010 年间发布的田野工具包[^bowern2018fieldwork-e5]。

**体裁要多样。** Leonard 指出，记录语料可能有精心标注的文本，却缺少对话[^leonard2018decolonialism-e1]。规划时列一张体裁清单（对话、叙事、讲解做事的过程、歌谣等），和社区商量哪些重要 `[本项目分析]`。

**选发音人**：和社区商量谁最合适 `[本项目分析]`（例如 Czaykowska-Higgins 说，在大多数加拿大原住民社区，长者是合作的核心[^czaykowskahiggins2009research-e2]），并记下每人的角色（见第五步）。怎样按年龄、性别等抽样，本文资料未涉及，以导师和项目要求为准。

**容易错在哪里**：把记录做成按固定步骤走完就算交差的"流水线"。Good 提醒，这种做法会不知不觉出现，而且不适合具体社区的情况[^good2018scope-e3]。

### 第四步：录音录像

- **保留完整的原始录音。** Bird 和 Simons 建议：转写了一段叙事，就提供完整的原始录音，不要切成很多小片段[^bird2002portability-e2]。
- **按档案馆的标准录。** 以 PARADISEC 为例：音频交 WAV 格式，尽量接近 24 位、96 千赫兹的存档标准[^paradisecdeposit-e6]；视频交 mkv 作为存档母版、mp4 作为日常副本[^paradisecdeposit-e7]。这是这一家档案馆的要求；开录前先查你要存的档案馆的要求 `[本项目分析]`。
- **控制数量。** Bowern 提醒，大量录音录像会带来数据量大、转写跟不上、很多材料和项目关系不大等问题[^bowern2018fieldwork-e4]。PARADISEC 也请存档人不要为同一事件交多份录音录像[^paradisecdeposit-e2]。

麦克风和录音机选什么型号、怎样摆放，本文资料未涉及；可以看你所用档案馆的技术指南，或请教有经验的同行。

### 第五步：每次录音都记元数据

**元数据**是描述材料的信息：谁、何时、何地、录了什么、谁能看。每次录完当天就记 `[本项目分析]`。口述历史的元数据和命名做法相近，见[口述历史第九步](../../history-archaeology/research-types/oral_history.md#第九步备份编元数据存档)。

- **尽量合乎通用标准。** PARADISEC 的元数据有一部分符合两套国际标准：开放语言档案社区（Open Language Archives Community，OLAC）和都柏林核心（Dublin Core）[^paradisecdeposit-e9]。
- **记每个人的角色**：PARADISEC 的元数据要标出发音人、录音者、转写者、翻译者等角色[^paradisecdeposit-e11]。Himmelmann 2018 年指出，现在的做法常连"谁参与了转写"都没记[^himmelmann2018transcription-e6]。
- **记访问条件和权利**：PARADISEC 的每个条目有自己的访问条件[^paradisecdeposit-e10]；同意时谈好的访问级别也要写进去[^seyfeddinipur2019public-e7][^bird2002portability-e6]；知识产权情况也要记清[^bird2002portability-e7]。
- **统一命名。** PARADISEC 要求相关文件用同一个基本文件名，例如转写文件和对应的录音同名[^paradisecdeposit-e4]，名字各部分内部不用连字符或空格[^paradisecdeposit-e5]。

### 第六步：转写和翻译

- **留足时间。** 德国语言学者 Himmelmann 2018 年写道：转写加翻译一分钟录音，很少有人说少于十分钟；复杂的多人对话，150 倍甚至更高也不算离谱[^himmelmann2018transcription-e1]。
- **做时间对齐的转写**，让每句话都能回到录音里核对[^bird2002portability-e2]。
- **转写就是解释。** 转写会给声音信号加进大量信息[^himmelmann2018transcription-e3]；不同的人转写同一段录音，细节会不同[^himmelmann2018transcription-e5]。所以要写下你的转写规则，尤其是词以上的单位（韵律单位、句法短语）怎样切分：Himmelmann 说这一点常常不加说明，使用者难以还原和评价[^himmelmann2018transcription-e2]。
- **留意母语者"改稿"。** 母语者协助转写时，常转述而不照原话重复，还会删掉语气词、犹豫等口语成分[^himmelmann2018transcription-e4]。要和协助者说清楚你要的是原话，改动另记一层 `[本项目分析]`。
- **拼写也是决定。** 拼写约定、词条的基本形式等很多标准化决定，在转写时就做了[^himmelmann2018transcription-e8]；Himmelmann 说，这时通常没有请更多社区成员参与[^himmelmann2018transcription-e7]。所以这类决定最好和社区商量 `[本项目分析]`。

和[访谈研究的转录](../../computer-science/research-types/interview_study.md#第四步转录)不同，这里的转写本身就是要长期保存的语言数据，不只是分析的中间步骤 `[本项目分析]`。

### 第七步：做行间注释，遵循莱比锡规则

**行间注释**（interlinear glossed text）逐词、逐词素（最小的有意义单位）说明意义和语法属性[^leipzig2015glossing-e1]。《莱比锡注释规则》由德国马普进化人类学研究所和莱比锡大学的语言学者联合制定[^leipzig2015glossing-e10]，目的是把最通行的注释约定写明[^leipzig2015glossing-e11]。下面是规则第 4 条里的一个拉丁语例子[^leipzig2015glossing-e6]：

```
insul-arum
island-GEN.PL
'of the islands'
```

第一行是原文，第二行是注释，第三行是意译。几条核心规则：

- 注释行和原文**逐词左对齐**[^leipzig2015glossing-e2]；
- 词素用**连字符**隔开，两行的连字符数必须相同[^leipzig2015glossing-e3]；附着成分（依附在别的词上的成分）用等号[^leipzig2015glossing-e4]；
- 语法词素用**大写缩写**[^leipzig2015glossing-e5]，规则附有一份建议的缩写表[^leipzig2015glossing-e12]；上例的 GEN、PL 分别表示属格和复数 `[本项目分析]`；一个成分要用几个词或缩写来注释时，用**句点**连接[^leipzig2015glossing-e6]；
- 规则说，多数作者会需要增加或修改某些约定，尤其是缩写标签[^leipzig2015glossing-e8]，所以自定义的缩写要列表说明 `[本项目分析]`。

**两点提醒。** 第一，注释属于分析，不属于数据[^leipzig2015glossing-e7]；你的分析变了，注释就要改，所以要和原始录音、转写分开保存 `[本项目分析]`。第二，这套规则主要针对论文和书里的例句，给整个语料库加标注时考虑会不同[^leipzig2015glossing-e9]。Leonard 还建议，例句第一行先给不切分的完整词[^leonard2018decolonialism-e4]。

### 第八步：选对格式，存进档案馆

- **用开放格式。** Bird 和 Simons 建议优先选多种软件都支持的格式[^bird2002portability-e3]；文字用 Unicode 编码[^bird2002portability-e4]；词汇表这类结构化数据不要存在 Word 里[^bird2002portability-e5]。他们提醒，一百多年前的记录今天还能用，很多数字记录不到十年就没法用了[^bird2002portability-e1]。
- **按档案馆要求导出。** 例如 PARADISEC 要求 FLEx（一种常用的词典和文本标注软件）的文件导出成 XML[^paradisecdeposit-e8]。
- **设定访问条件。** PARADISEC 允许存档人规定访问和使用条件[^paradisecdeposit-e1]。Seyfeddinipur 等建议，限制访问时要设明确的封存期，到期可以解除[^seyfeddinipur2019public-e14]；他们也提醒，别拿"社区敏感"当借口不公开[^seyfeddinipur2019public-e12]。受限数据也可以引用，但只有不受限的才能被别人再利用[^berezkroeker2018reproducible-e11]。
- **想好身后事。** PARADISEC 提醒田野工作者在遗嘱里写明田野录音怎样处置[^paradisecdeposit-e3]。

### 第九步：把材料交还社区

- 美国语言学会要求尽可能把数据和知识交还社区保管[^lsa2019ethics-e22]。PARADISEC 说，作者也可以同意把文化录音的版权转让给合作的个人或社区[^paradisecdeposit-e13]。
- 给社区的成果按社区的用法做：Leonard 建议先用较长、有语境的例子，按社区最常用的方式呈现[^leonard2018decolonialism-e3]。
- 给社区用的教学材料、数据档案、语料库等也算学术成果，这是美国语言学会 2010 年决议的立场[^lsa2010documentation-e2]，详见[领域概况](../README.md#语言学田野调查和濒危语言)。

### 第十步：从记录材料到分析和论文

- **先把材料变成能检索的语料库。** 加拿大语言学者 Rice 2018 年说，真正的语料库不只是一堆存档材料，要转成机器可读、可检索的形式[^rice2018corpora-e1]。她认为，小的、没标注、不平衡的语料库，也能揭示很多规律[^rice2018corpora-e2]。语料库的数据处理可借[数据科学](../../computer-science/research-types/data_science.md) `[本项目分析]`。
- **每个例句都能追到出处**：写明录音编号和起止时间码[^berezkroeker2018reproducible-e7]；用了自己或他人的语感判断，要明说[^berezkroeker2018reproducible-e9]。引用数据的原则见[领域概况](../README.md#语言学数据引用和可复现)[^berezkroeker2018austin-e1]。
- **只上传文件不等于可核查。** Riesberg 说，光把录音录像传到档案馆，别人还核查不了你的结论[^riesberg2018adequacy-e3]；材料要配上时间对齐的转写和注释 `[本项目分析]`。
- **署上所有贡献者和他们的角色**[^berezkroeker2018austin-e4]，选能给持久标识符（如 DOI，数字对象唯一标识符）的档案馆[^berezkroeker2018austin-e5]。

## 3. 检查清单

下面的分档由本项目根据上文资料整理 `[本项目分析]`；每一条的依据见脚注。

**必须做到**

- [ ] 从规划阶段就请社区参与，商定目标和各方角色[^lsa2019ethics-e18][^czaykowskahiggins2009research-e7]
- [ ] 弄清谁有权同意：个人、家族还是社区[^seyfeddinipur2019public-e1]；同意包括访问级别，并写进元数据[^seyfeddinipur2019public-e7]
- [ ] 事先查清研究许可、版权和雇主的知识产权要求[^seyfeddinipur2019public-e9][^paradisecdeposit-e12]
- [ ] 每条录音都有元数据，包括参与者角色和访问条件[^paradisecdeposit-e10][^paradisecdeposit-e11]
- [ ] 存进档案馆，用开放格式[^berezkroeker2018reproducible-e13][^bird2002portability-e3]
- [ ] 论文里每个例句都能追到录音和时间码[^berezkroeker2018reproducible-e7]

**做到更好**

- [ ] 诱导材料和自然语料都有，体裁多样，包括对话[^bowern2018fieldwork-e1][^leonard2018decolonialism-e1]
- [ ] 转写和录音时间对齐，并写下转写和切分规则[^bird2002portability-e2][^himmelmann2018transcription-e2]
- [ ] 记下谁参与了转写[^himmelmann2018transcription-e6]
- [ ] 定好继任计划；限制访问时设明确的封存期[^seyfeddinipur2019public-e11][^seyfeddinipur2019public-e14]
- [ ] 给社区做能用的成果[^lsa2019ethics-e22][^leonard2018decolonialism-e3]

**这些情况可以不做，不算缺陷**

- [ ] 不适合书面同意时，不签书面同意书，改为录下口头同意[^seyfeddinipur2019public-e5]
- [ ] 社区不愿公开的材料，不公开存档：美国语言学会要求遵从社区对访问和存档的意愿[^lsa2019ethics-e7]；早期拿不准时可以先限制访问[^seyfeddinipur2019public-e8]

**审稿时常见、但不成立的批评**（下面两条由本项目根据资料整理，资料没有说它们有多常见 `[本项目分析]`）

- "语料里有诱导材料，所以不算语言记录。"Riesberg 认为，这种看法对 Himmelmann 的理解走过了头[^riesberg2018adequacy-e1][^riesberg2018adequacy-e2]。
- "语料库太小、没标注、不平衡，什么也说明不了。"Rice 认为这样的语料库也能揭示很多规律[^rice2018corpora-e2]；但结论的适用范围要说清楚 `[本项目分析]`。

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 先定好研究问题，再去社区找人录音 | 美国语言学会要求社区从规划的最早阶段参与[^lsa2019ethics-e18] |
| 只取得发音人个人的签字同意 | 故事、歌曲可能属于家族或社区[^seyfeddinipur2019public-e1]；同意也会变[^seyfeddinipur2019public-e6] |
| 只做诱导，或只录自然语料 | 两类材料各有长处[^bowern2018fieldwork-e1] |
| 把录音切成很多小片段保存 | 应提供完整的原始录音[^bird2002portability-e2] |
| 录完不记元数据，事后凭记忆补 | 参与者角色和访问条件都要记[^paradisecdeposit-e10][^paradisecdeposit-e11]；连谁转写的都常漏记[^himmelmann2018transcription-e6] |
| 按"一分钟录音几分钟转写"做计划 | 很少有人估计转写加翻译少于录音时长的十倍[^himmelmann2018transcription-e1] |
| 让母语者转写，却不说明要原话 | 母语者常转述、删掉口语成分[^himmelmann2018transcription-e4] |
| 行间注释两行的连字符数对不上 | 莱比锡规则要求两行连字符数相同[^leipzig2015glossing-e3] |
| 词汇表存在 Word 里，录音只存在自己电脑上 | 结构化数据不要用自由排版的编辑器存[^bird2002portability-e5]；很多数字记录不到十年就没法用了[^bird2002portability-e1] |
| 无限期封存全部材料 | 封存应有明确期限[^seyfeddinipur2019public-e14]，不要拿"社区敏感"当借口[^seyfeddinipur2019public-e12] |

## 5. 延伸阅读

- **Seyfeddinipur 等 2019，Public access to research data in language documentation**（开放获取）：同意、版权、访问级别、封存期怎样处理。和社区谈同意之前读。
- **Czaykowska-Higgins 2009，Research Models, Community Engagement, and Linguistic Fieldwork**（开放获取）：在加拿大原住民社区合作研究的经验。规划项目时读。
- **The Leipzig Glossing Rules**（免费 PDF）：行间注释的格式约定和建议的缩写表。写第一个例句前读。
- **PARADISEC 网站的 Deposit 栏目**：文件命名、格式、元数据、访问条件的具体要求。它只代表这一家档案馆；存别的档案馆，以那一家的要求为准。
- **Bird & Simons，Seven Dimensions of Portability for Language Documentation and Description**：怎样让数字记录长期可用。本文依据 2002 年的 arXiv 预印本（免费）；修订版 2003 年发表于期刊 Language。
- **期刊专刊 Reflections on Language Documentation 20 Years after Himmelmann 1998**（2018，开放获取）：其中 Himmelmann 谈转写，Bowern 谈田野方法，Leonard 谈去殖民化，Rice 谈语料库，每篇 8 到 16 页。各篇是作者本人的看法。

[^good2018scope-e1]: Good 2018，摘要。[证据](../../../../sources/notes/good2018scope.md#e1)
[^good2018scope-e2]: Good 2018，§1。[证据](../../../../sources/notes/good2018scope.md#e2)
[^good2018scope-e3]: Good 2018，§2.1。[证据](../../../../sources/notes/good2018scope.md#e3)
[^bird2002portability-e1]: Bird & Simons 2002，§1。[证据](../../../../sources/notes/bird2002portability.md#e1)
[^bird2002portability-e2]: Bird & Simons 2002，§5.1 ACCOUNTABILITY。[证据](../../../../sources/notes/bird2002portability.md#e2)
[^bird2002portability-e3]: Bird & Simons 2002，§5.2 OPENNESS。[证据](../../../../sources/notes/bird2002portability.md#e3)
[^bird2002portability-e4]: Bird & Simons 2002，§5.2 DOCUMENTATION。[证据](../../../../sources/notes/bird2002portability.md#e4)
[^bird2002portability-e5]: Bird & Simons 2002，§5.2 MACHINE-READABLE。[证据](../../../../sources/notes/bird2002portability.md#e5)
[^bird2002portability-e6]: Bird & Simons 2002，§5.4 UNIMPEDED。[证据](../../../../sources/notes/bird2002portability.md#e6)
[^bird2002portability-e8]: Bird & Simons 2002，§1（引 Himmelmann 1998: 166）。[证据](../../../../sources/notes/bird2002portability.md#e8)
[^riesberg2018adequacy-e1]: Riesberg 2018，第 152 页。[证据](../../../../sources/notes/riesberg2018adequacy.md#e1)
[^riesberg2018adequacy-e2]: Riesberg 2018，第 152 页。[证据](../../../../sources/notes/riesberg2018adequacy.md#e2)
[^riesberg2018adequacy-e3]: Riesberg 2018，第 154 页。[证据](../../../../sources/notes/riesberg2018adequacy.md#e3)
[^czaykowskahiggins2009research-e1]: Czaykowska-Higgins 2009，§4.1。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e1)
[^czaykowskahiggins2009research-e2]: Czaykowska-Higgins 2009，§4.1。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e2)
[^czaykowskahiggins2009research-e3]: Czaykowska-Higgins 2009，§4.1。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e3)
[^czaykowskahiggins2009research-e4]: Czaykowska-Higgins 2009，§4.1。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e4)
[^czaykowskahiggins2009research-e5]: Czaykowska-Higgins 2009，§4.2。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e5)
[^czaykowskahiggins2009research-e6]: Czaykowska-Higgins 2009，§4.2。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e6)
[^czaykowskahiggins2009research-e7]: Czaykowska-Higgins 2009，§4.3。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e7)
[^czaykowskahiggins2009research-e8]: Czaykowska-Higgins 2009，§4.3。[证据](../../../../sources/notes/czaykowskahiggins2009research.md#e8)
[^lsa2019ethics-e18]: LSA 2019，Communities and the public。[证据](../../../../sources/notes/lsa2019ethics.md#e18)
[^lsa2019ethics-e19]: LSA 2019，Communities and the public。[证据](../../../../sources/notes/lsa2019ethics.md#e19)
[^lsa2019ethics-e20]: LSA 2019，Communities and the public。[证据](../../../../sources/notes/lsa2019ethics.md#e20)
[^lsa2019ethics-e3]: LSA 2019，Participants。[证据](../../../../sources/notes/lsa2019ethics.md#e3)
[^lsa2019ethics-e21]: LSA 2019，Participants。[证据](../../../../sources/notes/lsa2019ethics.md#e21)
[^lsa2019ethics-e22]: LSA 2019，Communities and the public。[证据](../../../../sources/notes/lsa2019ethics.md#e22)
[^leonard2018decolonialism-e1]: Leonard 2018，§2。[证据](../../../../sources/notes/leonard2018decolonialism.md#e1)
[^leonard2018decolonialism-e2]: Leonard 2018，§2。[证据](../../../../sources/notes/leonard2018decolonialism.md#e2)
[^leonard2018decolonialism-e3]: Leonard 2018，§3。[证据](../../../../sources/notes/leonard2018decolonialism.md#e3)
[^leonard2018decolonialism-e4]: Leonard 2018，§3。[证据](../../../../sources/notes/leonard2018decolonialism.md#e4)
[^seyfeddinipur2019public-e1]: Seyfeddinipur 等 2019，§2.1。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e1)
[^seyfeddinipur2019public-e2]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e2)
[^seyfeddinipur2019public-e3]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e3)
[^seyfeddinipur2019public-e4]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e4)
[^seyfeddinipur2019public-e5]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e5)
[^seyfeddinipur2019public-e6]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e6)
[^seyfeddinipur2019public-e7]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e7)
[^seyfeddinipur2019public-e8]: Seyfeddinipur 等 2019，§2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e8)
[^seyfeddinipur2019public-e9]: Seyfeddinipur 等 2019，§3.1。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e9)
[^seyfeddinipur2019public-e10]: Seyfeddinipur 等 2019，§3.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e10)
[^seyfeddinipur2019public-e11]: Seyfeddinipur 等 2019，§5.2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e11)
[^seyfeddinipur2019public-e12]: Seyfeddinipur 等 2019，§5.2.2。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e12)
[^seyfeddinipur2019public-e13]: Seyfeddinipur 等 2019，§6.2.1。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e13)
[^seyfeddinipur2019public-e14]: Seyfeddinipur 等 2019，§6.2.1。[证据](../../../../sources/notes/seyfeddinipur2019public.md#e14)
[^paradisecdeposit-e1]: PARADISEC，Deposit 页。[证据](../../../../sources/notes/paradisecdeposit.md#e1)
[^paradisecdeposit-e2]: PARADISEC，Deposit 页。[证据](../../../../sources/notes/paradisecdeposit.md#e2)
[^paradisecdeposit-e3]: PARADISEC，Deposit 页。[证据](../../../../sources/notes/paradisecdeposit.md#e3)
[^paradisecdeposit-e4]: PARADISEC，Catalog Structure & File Naming 页。[证据](../../../../sources/notes/paradisecdeposit.md#e4)
[^paradisecdeposit-e5]: PARADISEC，Catalog Structure & File Naming 页。[证据](../../../../sources/notes/paradisecdeposit.md#e5)
[^paradisecdeposit-e6]: PARADISEC，File formats 页。[证据](../../../../sources/notes/paradisecdeposit.md#e6)
[^paradisecdeposit-e7]: PARADISEC，File formats 页。[证据](../../../../sources/notes/paradisecdeposit.md#e7)
[^paradisecdeposit-e8]: PARADISEC，File formats 页。[证据](../../../../sources/notes/paradisecdeposit.md#e8)
[^paradisecdeposit-e9]: PARADISEC，Metadata 页。[证据](../../../../sources/notes/paradisecdeposit.md#e9)
[^paradisecdeposit-e10]: PARADISEC，Metadata 页。[证据](../../../../sources/notes/paradisecdeposit.md#e10)
[^paradisecdeposit-e11]: PARADISEC，Metadata 页。[证据](../../../../sources/notes/paradisecdeposit.md#e11)
[^paradisecdeposit-e12]: PARADISEC，Do you own your records? 页。[证据](../../../../sources/notes/paradisecdeposit.md#e12)
[^paradisecdeposit-e13]: PARADISEC，Do you own your records? 页。[证据](../../../../sources/notes/paradisecdeposit.md#e13)
[^berezkroeker2018reproducible-e7]: Berez-Kroeker 等 2018，§2。[证据](../../../../sources/notes/berezkroeker2018reproducible.md#e7)
[^berezkroeker2018reproducible-e9]: Berez-Kroeker 等 2018，§4.2。[证据](../../../../sources/notes/berezkroeker2018reproducible.md#e9)
[^berezkroeker2018reproducible-e13]: Berez-Kroeker 等 2018，§5。[证据](../../../../sources/notes/berezkroeker2018reproducible.md#e13)
[^berezkroeker2018reproducible-e11]: Berez-Kroeker 等 2018，§4.2。[证据](../../../../sources/notes/berezkroeker2018reproducible.md#e11)
[^bowern2018fieldwork-e1]: Bowern 2018，§2。[证据](../../../../sources/notes/bowern2018fieldwork.md#e1)
[^bowern2018fieldwork-e2]: Bowern 2018，§2。[证据](../../../../sources/notes/bowern2018fieldwork.md#e2)
[^bowern2018fieldwork-e3]: Bowern 2018，§2。[证据](../../../../sources/notes/bowern2018fieldwork.md#e3)
[^bowern2018fieldwork-e4]: Bowern 2018，§2。[证据](../../../../sources/notes/bowern2018fieldwork.md#e4)
[^himmelmann2018transcription-e1]: Himmelmann 2018，§1。[证据](../../../../sources/notes/himmelmann2018transcription.md#e1)
[^himmelmann2018transcription-e2]: Himmelmann 2018，§1。[证据](../../../../sources/notes/himmelmann2018transcription.md#e2)
[^himmelmann2018transcription-e3]: Himmelmann 2018，§2。[证据](../../../../sources/notes/himmelmann2018transcription.md#e3)
[^himmelmann2018transcription-e4]: Himmelmann 2018，§2。[证据](../../../../sources/notes/himmelmann2018transcription.md#e4)
[^himmelmann2018transcription-e5]: Himmelmann 2018，§2。[证据](../../../../sources/notes/himmelmann2018transcription.md#e5)
[^himmelmann2018transcription-e6]: Himmelmann 2018，§4 脚注 6。[证据](../../../../sources/notes/himmelmann2018transcription.md#e6)
[^himmelmann2018transcription-e7]: Himmelmann 2018，§4。[证据](../../../../sources/notes/himmelmann2018transcription.md#e7)
[^leipzig2015glossing-e1]: Leipzig Glossing Rules，Preamble。[证据](../../../../sources/notes/leipzig2015glossing.md#e1)
[^leipzig2015glossing-e2]: Leipzig Glossing Rules，Rule 1。[证据](../../../../sources/notes/leipzig2015glossing.md#e2)
[^leipzig2015glossing-e3]: Leipzig Glossing Rules，Rule 2。[证据](../../../../sources/notes/leipzig2015glossing.md#e3)
[^leipzig2015glossing-e4]: Leipzig Glossing Rules，Rule 2。[证据](../../../../sources/notes/leipzig2015glossing.md#e4)
[^leipzig2015glossing-e5]: Leipzig Glossing Rules，Rule 3。[证据](../../../../sources/notes/leipzig2015glossing.md#e5)
[^leipzig2015glossing-e6]: Leipzig Glossing Rules，Rule 4。[证据](../../../../sources/notes/leipzig2015glossing.md#e6)
[^leipzig2015glossing-e7]: Leipzig Glossing Rules，Preamble。[证据](../../../../sources/notes/leipzig2015glossing.md#e7)
[^leipzig2015glossing-e8]: Leipzig Glossing Rules，About the rules。[证据](../../../../sources/notes/leipzig2015glossing.md#e8)
[^leipzig2015glossing-e9]: Leipzig Glossing Rules，Preamble。[证据](../../../../sources/notes/leipzig2015glossing.md#e9)
[^lsa2010documentation-e2]: LSA 2010 决议，第 2 条 Whereas。[证据](../../../../sources/notes/lsa2010documentation.md#e2)
[^rice2018corpora-e1]: Rice 2018，§4。[证据](../../../../sources/notes/rice2018corpora.md#e1)
[^rice2018corpora-e2]: Rice 2018，§5。[证据](../../../../sources/notes/rice2018corpora.md#e2)
[^berezkroeker2018austin-e1]: Austin Principles 2018，3. Evidence。[证据](../../../../sources/notes/berezkroeker2018austin.md#e1)
[^berezkroeker2018austin-e4]: Austin Principles 2018，2. Credit and Attribution。[证据](../../../../sources/notes/berezkroeker2018austin.md#e4)
[^berezkroeker2018austin-e5]: Austin Principles 2018，4. Unique Identification。[证据](../../../../sources/notes/berezkroeker2018austin.md#e5)
[^lsa1992humansubjects-e5]: LSA 1992，正文第 1 段。[证据](../../../../sources/notes/lsa1992humansubjects.md#e5)
[^lsa1992humansubjects-e3]: LSA 1992，正文第 3 段。[证据](../../../../sources/notes/lsa1992humansubjects.md#e3)
[^lsa2019ethics-e7]: LSA 2019，Communities and the public。[证据](../../../../sources/notes/lsa2019ethics.md#e7)
[^leonard2018decolonialism-e5]: Leonard 2018，§1。[证据](../../../../sources/notes/leonard2018decolonialism.md#e5)
[^bowern2018fieldwork-e5]: Bowern 2018，§2。[证据](../../../../sources/notes/bowern2018fieldwork.md#e5)
[^bird2002portability-e7]: Bird & Simons 2002，§5.7 DOCUMENTATION。[证据](../../../../sources/notes/bird2002portability.md#e7)
[^leipzig2015glossing-e10]: Leipzig Glossing Rules，About the rules。[证据](../../../../sources/notes/leipzig2015glossing.md#e10)
[^leipzig2015glossing-e11]: Leipzig Glossing Rules，Preamble。[证据](../../../../sources/notes/leipzig2015glossing.md#e11)
[^leipzig2015glossing-e12]: Leipzig Glossing Rules，About the rules。[证据](../../../../sources/notes/leipzig2015glossing.md#e12)
[^himmelmann2018transcription-e8]: Himmelmann 2018，§4。[证据](../../../../sources/notes/himmelmann2018transcription.md#e8)
