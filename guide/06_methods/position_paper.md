# 立场论文：论证一个领域应该怎么做、怎么看

本文讲**立场论文**（position paper），以及和它相近的**观点文章**（perspective）、**展望论文**（vision paper）。它们的主要贡献不是新数据，而是一个经过论证的主张：这个领域应该做什么、相信什么、改变什么。ICML（国际机器学习会议）的征稿启事这样区分：立场论文为"应该怎么做"的一种看法提出论证，研究论文则报告已经取得的进展[^icml2025position-e1]。

如果你要做的是把已发表的研究收集起来、系统地汇总，那是[综述研究](review_study.md)；如果你要研究"大家实际上怎样做研究"，并拿数据说话，看[方法论研究与元科学](meta_science.md)。怎样写一个站得住的论证，基本功在[解读论证](../05_research-strategies/interpret_argue.md)，本文只讲立场论文特有的部分。

**适用范围** `[本项目分析]`：本文的投稿要求和审稿标准主要来自计算机：机器学习方向的 ICML 2024、ICML 2025 和 NeurIPS 2025（神经信息处理系统大会）立场论文赛道，以及软件工程方向的 FSE 2025（ACM 软件工程基础会议）"想法、展望与反思"赛道。期刊里的观点文章以《自然·可持续发展》（Nature Sustainability）的说明为例。怎样陈述论点、怎样回应反驳，借用的是哈佛学院写作中心的讲义和哲学家 Pryor 的写作指南。各会议、各期刊每年的规定都会变，投稿前以当年的征稿启事为准。在人文学科，以论证为主的论文本来就是常态，做法见[解读论证](../05_research-strategies/interpret_argue.md)和[哲学论证研究](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md)。

**常服务的套路**：[解读论证](../05_research-strategies/interpret_argue.md)。回顾一个领域走过的路、指出它哪里走偏的反思类文章，也常带有[综合](../05_research-strategies/synthesize.md)的成分 `[本项目分析]`。

**读完本文，你应该能：**

- 分清立场论文、研究论文、综述和观点文章，判断自己手里的东西适合写成哪一种；
- 把立场写成一句可争辩的话，并说清它为什么重要；
- 为立场找证据，找出最强的反对立场并认真回应；
- 知道立场论文怎样被审，判断自己现在该不该写。

---

## 1. 这是什么研究，什么时候用

立场论文要做的事，是说服同行接受一个关于领域的主张。ICML 2025 列出的立场包括：支持或反对某个研究方向（不是某个具体算法或方案）、呼吁行动、价值主张、政策建议，或者建议改变做研究和评估研究的方式[^icml2025position-e9]。只描述新研究、不主张任何立场的论文，不属于立场论文[^icml2025position-e8]。

ICML 在 2024 年第一次设立这个赛道，理由是：领域里许多重要贡献不是传统研究论文的样子，而是讨论一个正在发生的趋势，或者为对领域的某种看法辩护[^icml2024position-e1]。

不同场合叫法不同，要求也不同。下表只列本文用到的几个例子：

| 场合 | 叫法 | 篇幅 | 特点 |
|---|---|---|---|
| ICML 2025 立场论文赛道 | position paper | 8 页上限，和主会议相同[^icml2025position-e13] | 必须有"不同观点"一节[^icml2025position-e7] |
| FSE 2025 想法、展望与反思赛道 | 新想法、展望、反思 | 不超过 4 页，另加 1 页参考文献[^fse2025ivr-e8] | 不要求评估结果[^fse2025ivr-e4] |
| 《自然·可持续发展》 | Perspective（观点文章） | 正文最多 5000 词，参考文献最多 60 条[^natsustaincontent-e5] | 大多由编辑邀请[^natsustaincontent-e3] |
| 同一期刊 | Comment（评论文章） | — | 呼吁行动时，必须详细给出解决方案的路线图[^natsustaincontent-e6] |

**它擅长回答的问题**：

- **领域做对了什么、做错了什么**，哪些开放问题该多关注、哪些该少关注[^neurips2025position-e1]；
- **某个现有研究方向是不是走偏了**[^fse2025ivr-e2]；
- **一个还没有扎实结果、但有充分理由的新方向**值不值得走[^fse2025ivr-e1]；
- **研究应该怎样做、怎样评估**[^icml2025position-e9]。
- **一场研究争议中的一方**：期刊的观点文章可以主张一个有争议的立场，或提出推测性假说；正反两方的文章通常都以观点文章发表[^natsustaincontent-e2]。

它回答不了"X 的效果有多大""A 是否导致 B"这类问题，这些要靠数据和实验。立场论文可以用别人的数据和自己的初步数据当证据，但它的贡献是论证，不是测量 `[本项目分析]`。

**和相近方法的区别**：

| | 立场论文 | 研究论文 | [综述研究](review_study.md) | 新想法 / 早期结果论文 |
|---|---|---|---|---|
| 核心主张 | 领域应该做什么、相信什么 | 我们做出了什么、发现了什么 | 已有研究合起来说明了什么 | 这个新方向有希望 |
| 主要证据 | 推理，加上引用、例子和已有数据 | 自己的实验、测量或证明 | 系统收集的已发表研究 | 初步结果 |
| 审稿人要不要同意结论 | 不必[^icml2025position-e11] | 要被证据说服 | 要被方法说服 | 要看到初步证据 |

依据：研究论文报告已经取得的进展[^icml2025position-e1]；观点文章比综述更面向未来、更带推测性[^natsustaincontent-e1]；FSE 的新想法类论文要给初步证据，展望和反思类给理由[^fse2025ivr-e3]。表中其余格子为 `[本项目分析]`。

### 新手什么时候该写，什么时候别写

`[本项目分析]` 下面是本手册根据上述资料做的判断，资料本身没有专门讨论新手：

- **适合写的时候**：你在自己的研究里亲眼看到了一个领域普遍存在的问题，手里有例子、有初步数据，而且能说清"应该怎么改"。这时立场论文是把一个具体发现推到整个领域的好办法。
- **先别写的时候**：你只有一个话题，还说不出一句可争辩的主张；你还没读够文献，说不清谁持相反的立场；或者你其实有一个新方法，只是还没做评估。最后这种情况，ICML 要求投主赛道[^icml2025position-e8]；FSE 也说，缺少评估的完整研究论文不是好的展望论文[^fse2025ivr-e5]。
- **知道门槛在哪**：立场论文同样要达到学术标准，要用证据和推理支撑主张、交代背景、恰当引用别人的工作[^icml2025position-e4]。期刊的观点文章大多由编辑邀请[^natsustaincontent-e3]，新手直接投稿的机会少；会议的立场论文赛道和展望赛道对所有人开放，门槛相对低一些。
- **和导师商量**：写立场论文要花的时间不比一篇小的研究论文少，而且它不会替代你的主线项目。FSE 说这类论文为以后的完整论文打基础[^fse2025ivr-e9]，也就是说，它最好是你主线研究的一个副产品。

**贯穿全书的例子** `[本项目分析]`：项目"现有大模型漏洞检测的评测结果被数据泄露高估了"本身是一个测量项目，要靠数据来证明，不是立场论文。但如果测量做完，你发现泄露在智能合约漏洞检测的评测里普遍存在，就可以在它的基础上写一篇立场论文，主张"大模型漏洞检测的评测论文，都应该先检查并报告数据泄露，再报告分数"。这篇立场论文的证据，主要来自你自己的测量结果和已有文献。在自然语言处理里已经有类似的文章：Sainz 等人 2023 年那篇自称立场论文的文章[^sainz2023nlp-e6]，主张对每个评测基准都要测量数据污染，理由之一是污染会让模型在该基准上的表现被高估[^sainz2023nlp-e2]。

---

## 2. 怎么做

### 第一步：把立场写成一句可争辩的话

**怎么做：**

- **写成一个主张，而不是一个话题。** ICML 2025 用假想的标题举例："停止研究机器学习的某某性质"说出了立场；"关于某某话题的一种看法"没有说出立场[^icml2025position-e6]。
- **让它可以被反对。** 好的论点是可争辩的，有思考的读者可能不同意它[^harvardwcthesis-e1]。只是描述或概括读者自己就能看到的东西，就用不着说服谁[^harvardwcthesis-e2]。
- **范围要合适。** 太窄，说不出有意思的东西；太宽，又拿不出证据支撑[^harvardwcthesis-e3]。哲学写作的建议同样适用：好论文谦虚，只论证一个小的观点，但把它说清楚，并给出好的理由[^pryor2012writing-e5]。

**为什么：** 立场论文的审稿第一条就是"清楚地陈述一个立场"[^icml2025position-e9]。立场说不清，后面的支撑、反驳都没有着落 `[本项目分析]`。

**容易错在哪：** 写成"大模型给软件安全带来了机遇和挑战"。这句话没人会反对，所以也不需要论证。改成"大模型漏洞检测的评测，在没检查数据泄露之前，不应该拿来和传统工具比较"，就是一个有人会反对的主张了 `[本项目分析]`。

**写下来：** 用"本文主张：……"写出一句话的立场，再写一句：谁会反对它、为什么。

### 第二步：说清为什么重要、为什么是现在

**怎么做：**

- **说明话题的分量。** ICML 的审稿标准"重要性"要求论文说明话题为什么重要，可以从范围、影响、时效、风险和收益等方面说[^icml2025position-e10]。
- **说明为什么现在要讨论。** 这个赛道要的是能激发建设性、文明讨论的及时话题，欢迎有争议的话题[^icml2025position-e3]。
- **说清读者为什么要在乎。** 把问题摆给读者时，你就在告诉他们这场论证事关什么，为什么值得关心答案[^harvardwcthesis-e4]。

**为什么：** 审稿人不必同意你，但要觉得这个话题值得整个领域讨论[^icml2025position-e2]。

**容易错在哪：** 把"重要"写成空话，例如"这个问题越来越受关注"。更好的写法是给出具体的东西：多少篇论文用了同一个评测集，多少结论可能因此要改 `[本项目分析]`。

**写下来：** 三句话：这件事影响谁，影响有多大，为什么现在要讨论。

### 第三步：为立场找证据

**怎么做：**

- **立场论文也要证据。** ICML 要求用证据和推理支撑主张[^icml2025position-e4]，审稿标准写的是"用清楚的推理，并在合适的地方用证据支撑立场"[^icml2025position-e10]。FSE 要求投稿说清为什么要改变现有实践或研究：新想法类给初步证据，展望和反思类给理由[^fse2025ivr-e3]。
- **证据可以有几种** `[本项目分析]`：已发表研究的结果（引用）；具体的例子或事件；已有的公开数据；你自己做的小规模分析。FSE 说，初步结果或评估计划的草图能帮审稿人理解工作的范围[^fse2025ivr-e4]。
- **前提要比结论更好接受。** 论证的前提应当没有争议，至少比结论争议小[^pryor2025terms-e9]；前提要能独立于结论而可信[^pryor2025terms-e10]。
- **不要拿名气代替论证。** 只说"某位著名学者持有这个立场"，本身没有论证分量[^pryor2025terms-e15]。
- **呼吁行动时，给出做法。** 《自然·可持续发展》要求呼吁行动的评论文章详细给出解决方案的路线图，而不只是描述一个问题[^natsustaincontent-e6]。

**为什么：** 没有证据，立场就只是意见。立场论文和社论的区别，就在于它把理由和证据摆出来让人检查 `[本项目分析]`。

**容易错在哪：** 只挑支持自己的例子。读者会问：反例在哪里？你怎么知道这不是个别现象？ `[本项目分析]`

**写下来：** 一张表：每个支撑理由一行，写出它的证据是什么（引用、例子、数据），以及证据有多强。

### 第四步：找出最强的反对立场，认真回应

**怎么做：**

1. **列出反对立场。** 反方论证是读者可能合理提出、用来挑战你论点的论证[^harvardwccounterargument-e1]。ICML 2025 要求正文（不是附录）有"不同观点"一节，描述并回应一种或多种站得住的、不是稻草人式的反对立场[^icml2025position-e7]。
2. **用对方最强的版本。** 按对方论证最强的版本去理解，必要时帮原作者补强[^pryor2025terms-e17]；回应对方能给出的最强论证，对自己的观点帮助最大[^pryor2025terms-e18]。
3. **设想对方怎样回击。** 别以为对方会马上认输，想想他会怎样反驳你，你又怎样应对[^pryor2012writing-e33]。
4. **可以部分让步。** 你可以承认反方说对了一部分，再说明为什么它动摇不了你的论点[^harvardwccounterargument-e5]。
5. **驳不倒，就改立场。** 驳不倒的反方论证，可能意味着要修改论点或其中一部分[^harvardwccounterargument-e3]。

**为什么：** "不同观点"是 ICML 2025 的审稿标准之一[^icml2025position-e7]。更根本的是，立场论文要说服的正是那些还没被说服的人 `[本项目分析]`。

**容易错在哪：** 树一个稻草人。比如把反方写成"有人认为数据泄露无所谓"。真实、更强的反方可能是："闭源模型的训练数据看不到，泄露根本没法检查，要求每篇论文都报告是空话。"你要回应的是后一种。例如可以指出，对闭源模型也有人提出了检查办法，Sainz 等人提议利用大模型的记忆能力[^sainz2023nlp-e5] `[本项目分析]`。

**写下来：** 列出两三个最强的反对立场，每个写一句"它说对了什么"和一句"为什么它推不翻我的主张"。

> **不同的看法：一定要单列"不同观点"一节吗？**
>
> 三份征稿启事的要求不一样。ICML 2024 第一次设立立场论文赛道时，审稿标准只有六条，没有"不同观点"这一条[^icml2024position-e3]。ICML 2025 把它列为必须，而且必须放在正文[^icml2025position-e7]。NeurIPS 2025 则写成"可以（在合适时）包含"[^neurips2025position-e2]，审稿标准里也加了"（如果相关）"[^neurips2025position-e3]。
>
> 实际建议 `[本项目分析]`：不管目标场合要不要求，都认真回应最强的反对立场；格式上是否单列一节，按目标场合当年的要求来。

### 第五步：交代背景，说清你站在哪里

**怎么做：**

- **讨论并引用相关的文献和事件。** 这是 ICML 的审稿标准"背景"[^icml2025position-e12]；FSE 的"学术性"标准也要求恰当考虑相关文献[^fse2025ivr-e6]。
- **先读已发表的立场论文。** ICML 2025 建议先读上一年发表的立场论文，作为例子，也可以在它们的基础上提出新想法或相反的立场[^icml2025position-e14]。
- **说清你反对谁。** 你的论点常常本身就是对别人论证的反驳[^harvardwccounterargument-e7]。

**为什么：** 一个立场有没有新意，要放在已有的讨论里才看得出来 `[本项目分析]`。

**容易错在哪：** 把别人的立场写得比实际更极端，好让自己显得新。批评之前先准确说出对方的意思，见[解读论证](../05_research-strategies/interpret_argue.md) `[本项目分析]`。

**写下来：** 一张"论辩地图"：谁主张什么、靠什么理由，你同意谁、反对谁。做法见[哲学论证研究第 2 步](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md#第-2-步把文献画成一张论辩地图)。

### 第六步：写成一眼看得出立场的样子

**怎么做：**

- **在显眼的地方写出立场。** ICML 2025 要求：标题说出立场，摘要用一句话说明立场（例如"本立场论文主张……"），引言用粗体写出立场[^icml2025position-e5]。即使目标场合没这样要求，这也是一个好习惯 `[本项目分析]`。
- **开头就提出核心问题。** 说清问题是什么、为什么是个问题[^pryor2012writing-e30]。
- **用简单直白的文字。** 句子和段落都要短[^pryor2012writing-e8]。
- **结构建议** `[本项目分析]`：引言（立场、为什么重要）→ 背景 → 支撑理由（每个理由一节，各带证据）→ 不同观点与回应 → 具体建议（谁、做什么）→ 结论。

**为什么：** 审稿标准里有一条"表达质量"：组织好、写得清楚[^icml2025position-e12]。立场论文没有实验结果可以依靠，读者能不能被说服，很大程度上取决于论证是否清楚 `[本项目分析]`。

**写下来：** 先写提纲，每一节写一句"这一节要让读者相信什么"。

### 第七步：选场合，了解怎么审

**怎么做：**

- **会议的立场论文赛道**：ICML 2025 立场论文的格式、双盲审稿、各项政策和截止日期都和主会议相同[^icml2025position-e13]。2024 年由主动勾选愿意审这类稿件的审稿人来审[^icml2024position-e2]。NeurIPS 2025 不要求立场论文填主赛道的论文检查清单[^neurips2025position-e4]。
- **会议的展望赛道**：FSE 2025 按价值、影响、原创性、学术性和整体质量评审[^fse2025ivr-e6]；展望和反思类还要看理由是否站得住[^fse2025ivr-e7]。
- **期刊的观点文章**：《自然·可持续发展》的观点文章大多由编辑邀请，也接受提议[^natsustaincontent-e3]。主动投稿要先交提要，写清话题、怎样组织、一张示例图、近期关键文献，以及文章的贡献是什么[^natsustaincontent-e4]。观点文章同样要经过同行评审[^natsustaincontent-e5]。

**为什么：** 不同场合的审稿标准不同，按研究论文的标准去写立场论文，或者反过来，都会被认为"不对路" `[本项目分析]`。

**容易错在哪：** 以为立场论文好发。它不要求新结果，但对论证、背景和表达的要求一点不少 `[本项目分析]`。选会议和投稿的一般做法见[选择发表渠道与投稿](../03_write-and-publish/02_venue-and-submission.md)。

**写下来：** 目标场合、当年征稿启事的链接、它的审稿标准逐条抄下来，交稿前逐条自查。

---

## 3. 检查清单

下面的"必须做到"主要依据 ICML 2025 立场论文赛道的要求和审稿标准，它是机器学习方向一个会议的规定；其他场合以当年的征稿启事为准 `[本项目分析]`。

**必须做到**

- [ ] 清楚地陈述一个立场，而不是只描述新研究[^icml2025position-e8][^icml2025position-e9]
- [ ] 标题、摘要和引言都说出立场[^icml2025position-e5]
- [ ] 用清楚的推理支撑立场，在合适的地方用证据[^icml2025position-e10]
- [ ] 说明话题为什么重要[^icml2025position-e10]
- [ ] 描述并回应站得住的反对立场，而不是稻草人[^icml2025position-e7]
- [ ] 讨论并引用与立场相关的文献和事件[^icml2025position-e12]
- [ ] 组织好、写得清楚[^icml2025position-e12]

**做到更好**

- [ ] 给出初步结果，或者一个评估计划的草图[^fse2025ivr-e4]
- [ ] 呼吁行动时，详细给出解决方案的路线图[^natsustaincontent-e6]
- [ ] 用对方最强的版本来回应[^pryor2025terms-e17]
- [ ] 前提比结论更容易被接受[^pryor2025terms-e9]

**做得出色** `[本项目分析]`：用自己做的新分析或新数据支撑立场；写清"什么样的证据会让我改变立场"；给出具体、可以检查的建议（谁、在什么时候、做什么）。

**这些情况可以不做，不算缺陷**

- 没有评估结果：FSE 的展望赛道不要求[^fse2025ivr-e4]
- 审稿人不同意你的立场：ICML 明确说审稿人不必同意[^icml2025position-e11]
- 没有回应所有可能的反驳：不需要回应每一个反方论证[^harvardwccounterargument-e6]，集中处理最强、最紧要的[^pryor2012writing-e17]

---

## 4. 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 标题和摘要只点出话题，没说出立场 | 不算陈述了立场[^icml2025position-e6] |
| 立场没人会反对 | 只是概括读者自己能看到的东西，就用不着说服谁[^harvardwcthesis-e2] |
| 把一个还没评估的新方法包装成立场论文 | 不属于立场论文，应投研究论文[^icml2025position-e8][^fse2025ivr-e5] |
| 只有观点，没有证据和引用 | 立场论文同样要用证据和推理支撑主张[^icml2025position-e4] |
| 反方写成稻草人 | 要回应站得住的反对立场[^icml2025position-e7] |
| 拿名人的看法当理由 | 名气本身没有论证分量[^pryor2025terms-e15] |
| 只描述问题，不说怎么办 | 呼吁行动的文章要给出解决方案的路线图[^natsustaincontent-e6] |
| 范围太大，什么都想说 | 太宽就拿不出证据支撑[^harvardwcthesis-e3] |

---

## 5. 延伸阅读

- **立场论文的要求和审稿标准**：ICML 2025 和 NeurIPS 2025 的立场论文征稿启事，比较两者对"不同观点"一节的要求差异；ICML 2024 的启事讲了为什么设立这个赛道。
- **软件工程的展望与反思**：FSE 2025 "想法、展望与反思"赛道征稿启事，区分新想法、展望和反思三类，并写明什么样的稿件不算。
- **期刊的观点文章**：《自然·可持续发展》的文章类型说明，区分综述、观点文章和评论文章。
- **怎样写一个论点、怎样回应反驳**：哈佛学院写作中心的 Thesis 和 Counterargument 两页讲义；Pryor 的哲学论文写作指南。更系统的讲法见[解读论证](../05_research-strategies/interpret_argue.md)和[哲学论证研究](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md)。
- **一个和贯穿例子相关的立场论文**：Sainz 等人 2023，作者自称立场论文[^sainz2023nlp-e6]，主张对每个评测基准都测量大模型的数据污染[^sainz2023nlp-e2]。

各资料的链接见[原始资料列表](../../sources/README.md)。

[^icml2025position-e1]: ICML 2025 立场论文征稿启事，页首。[证据](../../sources/notes/icml2025position.md#e1)
[^icml2025position-e2]: ICML 2025 立场论文征稿启事，页首。[证据](../../sources/notes/icml2025position.md#e2)
[^icml2025position-e3]: ICML 2025 立场论文征稿启事，页首。[证据](../../sources/notes/icml2025position.md#e3)
[^icml2025position-e4]: ICML 2025 立场论文征稿启事，页首。[证据](../../sources/notes/icml2025position.md#e4)
[^icml2025position-e5]: ICML 2025 立场论文征稿启事，Policies and Requirements。[证据](../../sources/notes/icml2025position.md#e5)
[^icml2025position-e6]: ICML 2025 立场论文征稿启事，Policies and Requirements。[证据](../../sources/notes/icml2025position.md#e6)
[^icml2025position-e7]: ICML 2025 立场论文征稿启事，Policies and Requirements。[证据](../../sources/notes/icml2025position.md#e7)
[^icml2025position-e8]: ICML 2025 立场论文征稿启事，Policies and Requirements；Reviewing。[证据](../../sources/notes/icml2025position.md#e8)
[^icml2025position-e9]: ICML 2025 立场论文征稿启事，Reviewing，Position。[证据](../../sources/notes/icml2025position.md#e9)
[^icml2025position-e10]: ICML 2025 立场论文征稿启事，Reviewing。[证据](../../sources/notes/icml2025position.md#e10)
[^icml2025position-e11]: ICML 2025 立场论文征稿启事，Reviewing。[证据](../../sources/notes/icml2025position.md#e11)
[^icml2025position-e12]: ICML 2025 立场论文征稿启事，Reviewing。[证据](../../sources/notes/icml2025position.md#e12)
[^icml2025position-e13]: ICML 2025 立场论文征稿启事，Policies and Requirements。[证据](../../sources/notes/icml2025position.md#e13)
[^icml2025position-e14]: ICML 2025 立场论文征稿启事，页首。[证据](../../sources/notes/icml2025position.md#e14)
[^icml2024position-e1]: ICML 2024 立场论文征稿启事，页首。[证据](../../sources/notes/icml2024position.md#e1)
[^icml2024position-e2]: ICML 2024 立场论文征稿启事，Reviewing。[证据](../../sources/notes/icml2024position.md#e2)
[^icml2024position-e3]: ICML 2024 立场论文征稿启事，Reviewing。[证据](../../sources/notes/icml2024position.md#e3)
[^neurips2025position-e1]: NeurIPS 2025 立场论文征稿启事，页首。[证据](../../sources/notes/neurips2025position.md#e1)
[^neurips2025position-e2]: NeurIPS 2025 立场论文征稿启事，Policies and Requirements。[证据](../../sources/notes/neurips2025position.md#e2)
[^neurips2025position-e3]: NeurIPS 2025 立场论文征稿启事，Reviewing。[证据](../../sources/notes/neurips2025position.md#e3)
[^neurips2025position-e4]: NeurIPS 2025 立场论文征稿启事，Policies and Requirements。[证据](../../sources/notes/neurips2025position.md#e4)
[^fse2025ivr-e1]: FSE 2025 想法、展望与反思赛道征稿启事。[证据](../../sources/notes/fse2025ivr.md#e1)
[^fse2025ivr-e2]: FSE 2025 想法、展望与反思赛道征稿启事。[证据](../../sources/notes/fse2025ivr.md#e2)
[^fse2025ivr-e3]: FSE 2025 想法、展望与反思赛道征稿启事。[证据](../../sources/notes/fse2025ivr.md#e3)
[^fse2025ivr-e4]: FSE 2025 想法、展望与反思赛道征稿启事。[证据](../../sources/notes/fse2025ivr.md#e4)
[^fse2025ivr-e5]: FSE 2025 想法、展望与反思赛道征稿启事，Out of Scope。[证据](../../sources/notes/fse2025ivr.md#e5)
[^fse2025ivr-e6]: FSE 2025 想法、展望与反思赛道征稿启事，Evaluation。[证据](../../sources/notes/fse2025ivr.md#e6)
[^fse2025ivr-e7]: FSE 2025 想法、展望与反思赛道征稿启事，Evaluation。[证据](../../sources/notes/fse2025ivr.md#e7)
[^fse2025ivr-e8]: FSE 2025 想法、展望与反思赛道征稿启事，How to Submit。[证据](../../sources/notes/fse2025ivr.md#e8)
[^fse2025ivr-e9]: FSE 2025 想法、展望与反思赛道征稿启事。[证据](../../sources/notes/fse2025ivr.md#e9)
[^natsustaincontent-e1]: 《自然·可持续发展》文章类型说明，Perspective。[证据](../../sources/notes/natsustaincontent.md#e1)
[^natsustaincontent-e2]: 《自然·可持续发展》文章类型说明，Perspective。[证据](../../sources/notes/natsustaincontent.md#e2)
[^natsustaincontent-e3]: 《自然·可持续发展》文章类型说明，Perspective。[证据](../../sources/notes/natsustaincontent.md#e3)
[^natsustaincontent-e4]: 《自然·可持续发展》文章类型说明，Perspective。[证据](../../sources/notes/natsustaincontent.md#e4)
[^natsustaincontent-e5]: 《自然·可持续发展》文章类型说明，Perspective，Format。[证据](../../sources/notes/natsustaincontent.md#e5)
[^natsustaincontent-e6]: 《自然·可持续发展》文章类型说明，Comment。[证据](../../sources/notes/natsustaincontent.md#e6)
[^harvardwcthesis-e1]: 哈佛学院写作中心，Thesis，第 1 段。[证据](../../sources/notes/harvardwcthesis.md#e1)
[^harvardwcthesis-e2]: 哈佛学院写作中心，Thesis，第 3 段。[证据](../../sources/notes/harvardwcthesis.md#e2)
[^harvardwcthesis-e3]: 哈佛学院写作中心，Thesis，第 3 段。[证据](../../sources/notes/harvardwcthesis.md#e3)
[^harvardwcthesis-e4]: 哈佛学院写作中心，Thesis，第 2 段。[证据](../../sources/notes/harvardwcthesis.md#e4)
[^harvardwccounterargument-e1]: 哈佛学院写作中心，Counterargument，第 2 段。[证据](../../sources/notes/harvardwccounterargument.md#e1)
[^harvardwccounterargument-e3]: 哈佛学院写作中心，Counterargument，第 4 段。[证据](../../sources/notes/harvardwccounterargument.md#e3)
[^harvardwccounterargument-e5]: 哈佛学院写作中心，Counterargument，How to address counterarguments。[证据](../../sources/notes/harvardwccounterargument.md#e5)
[^harvardwccounterargument-e6]: 哈佛学院写作中心，Counterargument，Example 之后。[证据](../../sources/notes/harvardwccounterargument.md#e6)
[^harvardwccounterargument-e7]: 哈佛学院写作中心，Counterargument，Where to address counterarguments，Before your thesis。[证据](../../sources/notes/harvardwccounterargument.md#e7)
[^pryor2012writing-e5]: Pryor 2012，哲学论文写作指南，What Does One Do in a Philosophy Paper?。[证据](../../sources/notes/pryor2012writing.md#e5)
[^pryor2012writing-e8]: Pryor 2012，哲学论文写作指南，Use simple prose。[证据](../../sources/notes/pryor2012writing.md#e8)
[^pryor2012writing-e17]: Pryor 2012，哲学论文写作指南，Anticipate objections。[证据](../../sources/notes/pryor2012writing.md#e17)
[^pryor2012writing-e30]: Pryor 2012，哲学论文写作指南，Be concise, but explain yourself fully。[证据](../../sources/notes/pryor2012writing.md#e30)
[^pryor2012writing-e33]: Pryor 2012，哲学论文写作指南，Anticipate objections。[证据](../../sources/notes/pryor2012writing.md#e33)
[^pryor2025terms-e9]: Pryor 2025，哲学术语讲义，Philosophical Arguments / Persuasive Arguments。[证据](../../sources/notes/pryor2025terms.md#e9)
[^pryor2025terms-e10]: Pryor 2025，哲学术语讲义，Philosophical Arguments / Persuasive Arguments。[证据](../../sources/notes/pryor2025terms.md#e10)
[^pryor2025terms-e15]: Pryor 2025，哲学术语讲义，What is the Philosophical Method? / Appeals to authority/popularity and the burden of proof。[证据](../../sources/notes/pryor2025terms.md#e15)
[^pryor2025terms-e17]: Pryor 2025，哲学术语讲义，What is the Philosophical Method? / Charity。[证据](../../sources/notes/pryor2025terms.md#e17)
[^pryor2025terms-e18]: Pryor 2025，哲学术语讲义，What is the Philosophical Method? / Charity。[证据](../../sources/notes/pryor2025terms.md#e18)
[^sainz2023nlp-e2]: Sainz 等人 2023，摘要。[证据](../../sources/notes/sainz2023nlp.md#e2)
[^sainz2023nlp-e5]: Sainz 等人 2023，§5.2 Closed LLMs。[证据](../../sources/notes/sainz2023nlp.md#e5)
[^sainz2023nlp-e6]: Sainz 等人 2023，摘要。[证据](../../sources/notes/sainz2023nlp.md#e6)
