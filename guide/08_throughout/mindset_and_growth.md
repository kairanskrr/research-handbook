# 心态与长期积累

> 本页的建议大多来自计算机和机器学习研究者的个人经验（博客、演讲、讲座幻灯片），是有经验的人的建议，不是经过检验的规律。道理多半适用于各学科，例子以计算机为例；用之前，想想它合不合你的处境。

## 什么时候需要这一页

- 论文被拒、实验连着几周不出结果，你开始怀疑自己适不适合做研究；
- 你觉得自己"没有品味"，分不清哪个问题值得做，只能等导师给题目；
- 你忙了很久，却说不清自己这一年长了什么本事，或者已经累得撑不下去。

这一页不讲某个阶段的具体任务，讲的是贯穿整个研究过程的几种习惯：怎样练判断力、怎样对待失败、怎样积累、怎样保持能长期维持的节奏。

本页引用的资料多以博士生为对象（例如"读博两三年时最难熬""读博更像考驾照"）。本科生和硕士生的项目短得多，可以按比例理解：重要的不是具体年数，而是"失败很常见、积累要时间"这个道理。

---

## 1. 有意识地培养研究品味

**怎么做：** 研究品味，大致就是挑选好问题的能力[^olah2021taste-e1]；说得宽一点，也包括研究中各种没有标准答案的判断，比如哪个异常值得追下去、哪个实验更能说服人[^nanda2025taste-e2]。它练得慢（原因见下面"为什么"），所以练习的思路是：**用更便宜的办法，拿到更多反馈。** 下面这些是有经验的研究者建议的练习，都可以从今天开始做：

1. 把你的想法清单拿给你尊敬的导师，请他每条打 1–10 分；想过之后仍然和他看法不同的，坐下来细聊[^olah2021taste-e4]。
2. 问导师问题之前，先猜他会怎么回答，再对照[^nanda2025taste-e5]。
3. 开始一个想法之前，写下你的预测和"为什么觉得它好"；做完之后回头看[^nanda2025taste-e7]。
4. 别人做了你曾经想过的点子时，拿他的结果和你当初的预期比一比[^olah2021taste-e5]。
5. 访谈身边的研究者：他们为什么做这些问题，怎么挑问题[^olah2021taste-e6]。
6. 想一想：为什么有些想法被很多人接着用，有些很快被遗忘[^schulman2020opinionated-e5]？
7. 审视你所在圈子的品味。你的品味很大程度上受合作者和导师影响，要批判地看待[^olah2021taste-e7]。
8. 刚起步时，优先做能较快拿到中间结果的项目，而不是一年才见分晓的大赌注[^nanda2025taste-e8]；并且把项目做完（见第 7 节）。

**为什么：** 好几位有经验的研究者都把挑对问题的能力，看得比纯粹的技术能力更重要[^schulman2020opinionated-e3][^carlini2026best-e3]。缺了它，你可能写出技术上没错、却没人读的论文，因为从来没问过这个问题值不值得回答[^carlini2026best-e4]。

好消息是，品味不神秘：天赋有作用，但品味大部分靠学[^nanda2025taste-e1]；刚入门觉得自己没品味，完全正常[^nanda2025taste-e3]。难处在于反馈太少：验证一个想法好不好常常要几个月，一年只能得到几次反馈[^olah2021taste-e2]；反馈回路越短，你得到的数据越多[^nanda2025taste-e4]。上面的练习，都是在不等项目做完的情况下，多拿几次反馈：猜一次导师的回答、对照一次别人的结果，都是一次。

**容易错在哪：**

- **只想不做。** 还没动手就想挑出完美的问题，是一个陷阱；品味没法在真空里练[^olah2021taste-e9]。品味来自反复实践研究，并始终留意什么管用、什么不管用[^carlini2026best-e5]。
- **把自信当成正确。** 人往往很早就对自己的判断有了信心，很久之后直觉才真正变准[^nanda2025taste-e6]。

> **不同的看法：听导师的，还是坚持自己的判断？**
>
> - **别太听导师的**：有研究者回顾说，自己的多数错误出在听从导师批评的时候，而自己最酷的工作，起初都被大家说成没用、没意思[^olah2021taste-e15]。
> - **新手多依靠导师很正常**：上面的说法有幸存者偏差，人在不同阶段的成熟度不同[^olah2021taste-e16]；职业早期高度依赖导师或成熟的研究方向，是正常的[^nanda2025taste-e9]；做别人提出的想法不丢人，本事在于挑哪个、做得多好[^schulman2020opinionated-e4]。
>
> 实际操作：入门阶段可以先接受导师给的方向，在里面练判断；同时把你不同意导师的地方和理由记下来，事后对照结果。这本身就是练习 2 和 3。

**写下来：** 开一份"预测日志"。下一个实验开始前，写一行预测和理由，比如"给大模型加上漏洞模式提示，重入漏洞的检出率会明显提高，因为……"；结果出来后，在同一行后面写上实际结果和你学到了什么。

## 2. 把失败和被拒当作常态

**怎么做：**

- **先调整预期。** 到了真正要推进知识边界的阶段，没有现成的步骤可循，失败是常事。有经验的研究者观察到，读博两三年时，正是退出的人最多的时候[^might2010successful-e2]；要熬过这段，就得愿意从早到晚不断失败[^might2010successful-e3]。还有人说得更直接：如果你不经常失败，说明你尝试的事情还不够难[^sutherland1996courage-e2]。
- **被拒之后，先照顾情绪。** 允许自己难过，和朋友、同组同学、导师聊聊，休息一天再回来[^huang2021rejection-e6]。记住被拒针对的是想法、实现、实验和写作，不是你这个人[^huang2021rejection-e2]。情绪平复后，再把审稿意见变成修改清单，见[审稿意见、修改与被拒之后](../03_write-and-publish/03_review-and-revision.md)。
- **写一份"失败简历"**，把被拒、落选都记下来，让挫折变得平常[^huang2021rejection-e9]；同时庆祝小的进展，用它们保持动力[^huang2021rejection-e5]。
- **看看别人的幕后。** 简历上的论文列表整整齐齐，但每篇论文怎么发表出来的，都是另一个故事[^huang2021struggle-e1]。有位研究者回顾自己的论文：第一篇从收到项目的第一条消息到发表，隔了 3.5 年，发表之前他申请的博士项目全部被拒[^huang2021struggle-e2]；后来他带的研究组也经常被拒，维持士气并不容易[^huang2021struggle-e4]；后来被引最多的论文，当初常常评审意见很差，或者被拒过好几次[^huang2021struggle-e3]。

**为什么：** 对新手来说，一次被拒像是重大挫折，其实只是正常流程的一部分[^huang2021rejection-e7]。按一位计算机研究者 2010 年前后的估计，好的会议和期刊接收率在 8% 到 25% 之间，你的大部分甚至全部论文都会遭遇被拒；但坚持得够久、够努力，终究会发表[^might2010successful-e5]。

失败也不是白费。在反复失败里长出来的，恰恰是研究能力：想出说得通的方案，并估计它有多大可能成功[^might2010successful-e4]。反复琢磨一个想法却毫无进展，本身就是创造过程的第一步[^dettmers2019creativity-e2]；接受这种漫长、多轮失败的挣扎是创造的一部分，才能让创造过程不把人逼垮[^dettmers2019creativity-e5]。论文被接收这样的外部奖励很稀少，所以常常要靠内在的动力撑下去[^ruder2020tips-e12]。

**容易错在哪：** 把一次被拒当成对自己的否定；或者反过来，不看审稿意见就原样换个地方再投。前者伤人，后者浪费机会。

> **不同的看法：坚持，还是放手？**
>
> - **坚持**：这一阶段需要毅力，在不确定、被拒和挫败面前都要坚持下去[^might2010successful-e6]。大多数伟大的科学家都完全投入自己的问题，不投入的人很少做出一流的工作[^hamming1986you-e23]。
> - **适时放下**：暂时放下一个想法，可能正是创造的关键一步[^dettmers2019creativity-e3]。学术界也缺少帮人停掉陈旧项目的机制[^sutherland1996courage-e5]。
>
> 实际操作：对**方向**要有耐心，几次失败很正常；对**具体做法**要灵活，一条路走不通就换一条，或者先放一放。主项目之外留一个小的备选想法，放下时才不会觉得一切都完了（见第 6 节）。一个具体项目到底该坚持还是该停，怎么有根据地判断，见[执行与迭代](../02_do-the-project/06_run-and-iterate.md)。

**写下来：** 建一个"失败简历"文件，把你经历过的被拒、失败的实验、没走通的想法列进去，每条后面写一句"从中学到了什么"。以后每次被拒，先往里加一行。

## 3. 像复利一样积累知识和能力

**怎么做：**

- **吃透自己的领域，尽量了解相邻领域**[^kidger2023know-e1]。培养广泛的兴趣，多看自己小圈子以外的东西[^ruder2020tips-e7]。
- **广泛浏览，少量精读。** 快速浏览大量工作，知道已经知道了什么、别人在想什么问题；在此基础上每年挑十几篇精读[^nielsen2004principles-e15]。精读一个领域最重要的十篇论文，几乎肯定比浏览五百篇更有用[^nielsen2004principles-e12]。具体怎么分层读，见[进入领域、探索文献](../01_find-a-problem/01_enter-a-field.md)。
- **有意识地攒一种独特的能力组合**[^nielsen2004principles-e11]。比如做"大模型与智能合约安全"，既懂大模型、又懂程序分析的人，比只懂一边的人更容易看到别人看不到的问题。
- **在能力边缘刻意练习。** 专家不是只靠天赋或熬年头熬出来的，而是靠在自己能力的边缘练习[^prieto2025so-e4]。可以直接问导师和同事：我哪项研究技能比较弱，怎么提高[^prieto2025so-e5]？
- **记阅读笔记。** 读过的东西你记不住全部，但以后会经常想回头找[^wood2020five-e1]。
- **主动。** 主动做事，多提问[^patterson2001bad-e10]。

**为什么：** 知识和产出像复利。能力完全相同的两个人，每天多思考一小时的那个，一生的产出会多得多[^hamming1986you-e14]。知识的深度决定了你能不能想出新点子，也决定了你能不能认出坏点子[^kidger2023know-e1]；专业知识是创造力的前提，它让你分辨哪些想法成立、哪些不成立[^dettmers2019creativity-e1]。运气也偏爱有准备的头脑：有准备的人迟早会发现并做成某件重要的事[^hamming1986you-e22]。

**容易错在哪：**

- **只顾尽快多发论文，不花时间提升自己。** 短期回报诱人，长期代价是停滞，在原地踏步[^nielsen2004principles-e10]。
- **指望几个月补齐。** 这种积累是几年的事[^kidger2023know-e2]，而且学习从不真正停止[^kidger2023know-e3]。

**写下来：** 写一份一年的学习计划：本领域里要吃透的三到五个主题，相邻领域里要入门的一两个，以及你想补的一项弱技能。每个季度回头看一次。

## 4. 留出时间想重要的问题，并敢于开始

**怎么做：**

- **定期问自己：我这个领域最重要的问题是什么？** 有人多年坚持每周五下午只想大问题，相当于拿出约 10% 的时间想清楚领域里什么重要、什么不重要[^hamming1986you-e17]。想到的问题，记进你的想法清单，见[生成候选问题](../01_find-a-problem/02_generate-problems.md)。
- **主项目求稳，备选可以冒险。** 可以一个项目相对稳妥，一个风险高、但影响可能更大；稳妥的那个保证你能毕业[^ruder2020tips-e9]。
- **用一个问题检验野心：** 如果别人发表了这项工作，你会兴奋吗[^ruder2020tips-e10]？
- **害怕开始时，降低门槛。** 先做一个比较容易的热身项目，从头到尾做完，它既让你学到东西，也给你勇气[^sutherland1996courage-e7]。把大任务拆小，告诉自己"只洗第一个盘子"，就不那么怕了[^sutherland1996courage-e8]。刚入门的研究生，可以先加入一个正在运转的研究组；做什么远没有"开始做点什么"重要[^sutherland1996courage-e3]。

**为什么：** 不做重要的问题，就不太可能做出重要的工作[^hamming1986you-e1]。而做重要的问题需要勇气：勇气就是看到了风险，仍然往前走[^sutherland1996courage-e1]。有经验的研究者把勇气看作成功科学家的特点之一：相信自己能做重要的问题，才可能做到；认为自己不行，几乎肯定做不到[^hamming1986you-e16]。意识到"开始"本身需要勇气，也能帮你看清，自己迟迟不动手的那些理由，哪些其实只是借口[^sutherland1996courage-e6]。

**容易错在哪：**

- **只靠埋头苦干。** 光努力不够，努力要用对地方[^hamming1986you-e19]。
- **对自己的想法要么全信、要么全疑。** 要信到足以往前走，又疑到足以发现其中的错误[^hamming1986you-e3]。

**写下来：** 写下你认为自己方向上最重要的三个问题，每个配一句"为什么现在还没人解决"。每个月花一个下午重读、修改这份清单。

## 5. 别一个人闷头干

**怎么做：**

- **保持和外界的联系。** 关着门工作的人，眼下效率更高；但十年后，往往不太知道什么问题值得做[^hamming1986you-e18]。
- **主动联系身边圈子以外的人**，不要只和眼前这几个人打交道[^ruder2020tips-e11]。
- **和同伴一起学新东西。** 一起学能减轻每个人的负担，学起来更愉快，面对新东西时也没那么怕[^sutherland1996courage-e4]。
- **定期请外部的人审视你的项目**[^patterson2001bad-e12]。
- **让自己对别人负责。** 以为自律只是意志力的问题，是一种误解；关键是对别人负责[^nielsen2004principles-e9]。和人合作就是一种办法，见[合作与导师](collaboration_and_advisors.md)。
- **动手改善你的环境。** 改善环境是任何人都能做的事，学生常常低估自己能带来的改变[^nielsen2004principles-e13]。比如组织一个读书会或讨论班，和同学多交流；这样的交流能让你觉得和同伴连在一起、有人支持[^wood2020five-e4]。

**为什么：** 研究中的很多困难（选题拿不准、被拒、卡住）一个人扛最难，也最容易看偏；外面的人能给你自己看不到的视角，也能在你低落时拉一把。

**容易错在哪：** 等"做出点像样的东西"再给别人看。等到那时，方向上的问题往往已经花掉了你几个月。

**写下来：** 列出这个月要聊的一位圈外人（另一个组的同学、做相邻方向的老师、用你研究成果的工程师），写下你想问他的两个问题。

## 6. 保持能长期维持的节奏

**怎么做：**

- **先照顾好身体和生活。** 光有热情不够，还要把生活的其他部分安排好，保持健康[^nielsen2004principles-e7]。努力工作，但保证睡眠和运动[^ruder2020tips-e16]。
- **主动安排研究之外的生活**，比如运动、读闲书、参加社团、保护周末[^wood2020five-e2]。预见到要特别辛苦的阶段（比如野外调查这样的集中工作期），提前想好之后怎么休息[^wood2020five-e3]。
- **建一个支持网络**，再找一项事情不顺时能给你能量的活动[^ruder2020tips-e13]。
- **手里别只有一个想法。** 只有一件事可做时，它一不顺，动力和情绪都会受影响，卡住了也只能硬磨[^ruder2020tips-e8]。同时做两个项目，一个卡住了可以先做另一个[^ruder2020tips-e1]；手里有几个想法，比只盯着一个更有效[^dettmers2019creativity-e4]。对新手来说，先保证一个主项目能走完，再加一个小的副项目或备选想法。
- **把好的做法变成习惯。** 卓越不是一次行为，而是一种习惯[^nielsen2004principles-e6]。每周怎么回顾、日常时间怎么排，见[计划与日常节奏](planning_and_routines.md)。

**为什么：** 研究是以年计的事，能长期维持的节奏，才能让第 3 节说的复利真正积累起来。

**容易错在哪：** 等撑不住了才想起休息。辛苦阶段之后怎么恢复，要在开始之前就排好；事后再补，往往已经透支。

> **不同的看法：要拼到什么程度？**
>
> - **多投入一点，长期回报很大**：每天多思考一小时，一生的产出会多得多[^hamming1986you-e14]。
> - **透支得不偿失**：有作者回顾，自己为写书忽视健康和人际关系，短期产出增加了，整体算下来却可能降低了产出[^nielsen2004principles-e8]。最重要的资源不是算力，而是你自己的身心健康[^ruder2020tips-e14]。
>
> 两者并不矛盾：前一种说的是**日复一日**地多投入一点，而且努力要用对地方[^hamming1986you-e19]，不是短期透支。

**写下来：** 写下你每周固定不碰研究的时间（比如周六全天），以及接下来最辛苦的一段时间之后，你打算怎么休息。

## 7. 把项目做完，为长期积累能力

**怎么做：**

- **把项目做完。** 别人看的是你做完了哪些项目，而不是开了哪些头；成功的项目都要经过一段不光鲜、很辛苦的阶段[^patterson2001bad-e11]。
- **早期优先选能学到最多东西的位置和导师**[^prieto2025so-e6]。热情和能力哪个先，见下面"不同的看法"。
- **对题目有偏好，但保持灵活。** 懂行的人或文献告诉你另一个题目更相关、更可行时，认真考虑[^prieto2025so-e1]。理想的课题在三者的交集处：有影响力、你热爱、你特别适合做[^ruder2020tips-e15]。
- **定期调整方向，避免陈旧。** 一种建议是大约每七年做一次较大的方向调整[^hamming1986you-e21]。
- **想清楚长期目标：** 我想成为怎样的研究者[^nielsen2004principles-e14]？不必急着找到一生的使命，好的使命往往要多年试错才找得到；读博更像"考驾照"，而不是"跑出人生最好的一圈"[^prieto2025so-e2]。

**为什么：** 把项目做完，是人们学会挑好问题、找到简单解法的途径[^patterson2001bad-e11]；品味靠反馈和做完项目获得[^patterson2001bad-e7]。和论文相比，读博更重要的产出是一个更好的自己[^ruder2020tips-e16]。论文会过时，能力和判断力会一直跟着你。

**容易错在哪：** 一到不光鲜、很辛苦的阶段就换题。每个成功的项目都要经过这一段[^patterson2001bad-e11]；每到这里就换，结果是一个都做不完。

> **不同的看法：先有热情，还是先有能力？**
>
> - **跟随兴趣**：保持积极最自然的方式，是做让你兴奋的事、跟随好奇心；不能自己选题时，就在题目里找一个让你兴奋的角度[^ruder2020tips-e17]。
> - **能力先行**：另一种观点是，好职业的关键在稀缺而有价值的能力，不在事先就有的热情；在读博里，这意味着在能力边缘刻意练习，并优先选择能学到最多的位置和导师[^prieto2025so-e3][^prieto2025so-e4][^prieto2025so-e6]。
>
> 实际操作：在能选的范围里，找让你兴奋的角度；同时把主要精力放在积累能力上。兴趣常常是在越做越好的过程中长出来的。

**写下来：** 列出你手上所有开了头的项目，每个标上"做完 / 继续 / 停掉"。标"继续"的，写下离"做完"还差的最后一步。

---

## 常见错误

| 错误 | 为什么是问题 |
|---|---|
| 觉得自己"没品味"，干等它自己长出来 | 品味大部分靠学，要主动找反馈[^nanda2025taste-e1][^nanda2025taste-e4] |
| 一心想挑完美的问题，迟迟不动手 | 品味没法在真空里练[^olah2021taste-e9] |
| 把一次被拒当成对自己的否定 | 被拒针对的是作品，而且是常态[^huang2021rejection-e2][^huang2021rejection-e7] |
| 只有一个想法，没有任何备选 | 卡住就只能硬磨，动力和情绪都会受影响[^ruder2020tips-e8] |
| 只顾尽快多发论文，不花时间提升自己 | 长期会停滞[^nielsen2004principles-e10] |
| 一直关着门埋头干 | 十年后可能不知道什么问题值得做[^hamming1986you-e18] |
| 只靠苦干，不想方向 | 努力要用对地方[^hamming1986you-e19] |
| 为短期产出透支健康 | 整体产出可能反而降低[^nielsen2004principles-e8] |
| 开了很多头，一个都没做完 | 别人看的是做完的项目[^patterson2001bad-e11] |
| 等找到"真正的热情"再投入 | 有一种观点认为，好职业的关键在能力，不在事先就有的热情[^prieto2025so-e3]；本手册的看法是，热情常常在能力长起来之后才出现 |

## 延伸阅读

- **Olah，"Research Taste Exercises"**：培养品味的具体练习和几种失败模式，文末收录了很多人的补充建议。
- **Nanda，"Understanding and Cultivating Research Taste"**：讲品味由哪几部分组成，怎样缩短反馈回路，例子来自机器学习。
- **Hamming，"You and Your Research"**：做重要的问题、勇气、"开着门工作"和复利，值得每隔几年重读一次。
- **Sutherland，"Technology and Courage"**：开始、坚持和停止各需要怎样的勇气，以及降低门槛的具体办法。
- **Nielsen，"Principles of Effective Research"**：怎样在产出和自我提升之间保持平衡，怎样让环境帮你。
- **Jeff Huang，"The struggle for each paper"；Jia-Bin Huang 关于被拒的推文串**：被拒后低落时读（两位是不同的研究者）。
- **Might，"3 qualities of successful Ph.D. students"**：读博中期为什么最难熬，需要什么样的毅力。

[^olah2021taste-e1]: Olah 2021，开头。[证据](../../sources/notes/olah2021taste.md#e1)
[^olah2021taste-e2]: Olah 2021，开头。[证据](../../sources/notes/olah2021taste.md#e2)
[^olah2021taste-e4]: Olah 2021，Exercise 1。[证据](../../sources/notes/olah2021taste.md#e4)
[^olah2021taste-e5]: Olah 2021，Exercise 2。[证据](../../sources/notes/olah2021taste.md#e5)
[^olah2021taste-e6]: Olah 2021，Exercise 3。[证据](../../sources/notes/olah2021taste.md#e6)
[^olah2021taste-e7]: Olah 2021，Exercise 5。[证据](../../sources/notes/olah2021taste.md#e7)
[^olah2021taste-e9]: Olah 2021，Failure mode 2。[证据](../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e15]: Olah 2021，文末收录的 Christian Szegedy 的看法。[证据](../../sources/notes/olah2021taste.md#e15)
[^olah2021taste-e16]: Olah 2021，Olah 对 Szegedy 的评论。[证据](../../sources/notes/olah2021taste.md#e16)
[^nanda2025taste-e1]: Nanda 2025，Introduction。[证据](../../sources/notes/nanda2025taste.md#e1)
[^nanda2025taste-e2]: Nanda 2025，What is research taste?。[证据](../../sources/notes/nanda2025taste.md#e2)
[^nanda2025taste-e3]: Nanda 2025，Where does taste come from?。[证据](../../sources/notes/nanda2025taste.md#e3)
[^nanda2025taste-e4]: Nanda 2025，How to learn it?。[证据](../../sources/notes/nanda2025taste.md#e4)
[^nanda2025taste-e5]: Nanda 2025，How to learn it?。[证据](../../sources/notes/nanda2025taste.md#e5)
[^nanda2025taste-e6]: Nanda 2025，Conviction & Confidence。[证据](../../sources/notes/nanda2025taste.md#e6)
[^nanda2025taste-e7]: Nanda 2025，Conviction & Confidence。[证据](../../sources/notes/nanda2025taste.md#e7)
[^nanda2025taste-e8]: Nanda 2025，Cultivating Research Taste。[证据](../../sources/notes/nanda2025taste.md#e8)
[^nanda2025taste-e9]: Nanda 2025，Conclusion。[证据](../../sources/notes/nanda2025taste.md#e9)
[^schulman2020opinionated-e3]: Schulman 2020，Honing Your Taste。[证据](../../sources/notes/schulman2020opinionated.md#e3)
[^schulman2020opinionated-e4]: Schulman 2020，Honing Your Taste。[证据](../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e5]: Schulman 2020，Honing Your Taste。[证据](../../sources/notes/schulman2020opinionated.md#e5)
[^carlini2026best-e3]: Carlini 2026，Have good taste for problems。[证据](../../sources/notes/carlini2026best.md#e3)
[^carlini2026best-e4]: Carlini 2026，Have good taste for problems。[证据](../../sources/notes/carlini2026best.md#e4)
[^carlini2026best-e5]: Carlini 2026，Have good taste for problems。[证据](../../sources/notes/carlini2026best.md#e5)
[^patterson2001bad-e7]: Patterson 2001，第 42 页。[证据](../../sources/notes/patterson2001bad.md#e7)
[^patterson2001bad-e10]: Patterson 2001，研究生阶段建议小结。[证据](../../sources/notes/patterson2001bad.md#e10)
[^patterson2001bad-e11]: Patterson 2001，"4) Finishing a project"。[证据](../../sources/notes/patterson2001bad.md#e11)
[^patterson2001bad-e12]: Patterson 2001，"3) Running a project"。[证据](../../sources/notes/patterson2001bad.md#e12)
[^might2010successful-e2]: Might 2010，Perseverance。[证据](../../sources/notes/might2010successful.md#e2)
[^might2010successful-e3]: Might 2010，Perseverance。[证据](../../sources/notes/might2010successful.md#e3)
[^might2010successful-e4]: Might 2010，Perseverance。[证据](../../sources/notes/might2010successful.md#e4)
[^might2010successful-e5]: Might 2010，Perseverance。[证据](../../sources/notes/might2010successful.md#e5)
[^might2010successful-e6]: Might 2010，Perseverance。[证据](../../sources/notes/might2010successful.md#e6)
[^sutherland1996courage-e1]: Sutherland 1996，§1.1。[证据](../../sources/notes/sutherland1996courage.md#e1)
[^sutherland1996courage-e2]: Sutherland 1996，§2.6。[证据](../../sources/notes/sutherland1996courage.md#e2)
[^sutherland1996courage-e3]: Sutherland 1996，§2.2。[证据](../../sources/notes/sutherland1996courage.md#e3)
[^sutherland1996courage-e4]: Sutherland 1996，§2.2。[证据](../../sources/notes/sutherland1996courage.md#e4)
[^sutherland1996courage-e5]: Sutherland 1996，§2.5。[证据](../../sources/notes/sutherland1996courage.md#e5)
[^sutherland1996courage-e6]: Sutherland 1996，§3.1。[证据](../../sources/notes/sutherland1996courage.md#e6)
[^sutherland1996courage-e7]: Sutherland 1996，§3.3。[证据](../../sources/notes/sutherland1996courage.md#e7)
[^sutherland1996courage-e8]: Sutherland 1996，§3.4。[证据](../../sources/notes/sutherland1996courage.md#e8)
[^huang2021rejection-e2]: Jia-Bin Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1443248831102136333)第 4 条。[证据](../../sources/notes/huang2021rejection.md#e2)
[^huang2021rejection-e5]: Jia-Bin Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1443248831102136333)第 7 条。[证据](../../sources/notes/huang2021rejection.md#e5)
[^huang2021rejection-e6]: Jia-Bin Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1443248831102136333)第 2 条。[证据](../../sources/notes/huang2021rejection.md#e6)
[^huang2021rejection-e7]: Jia-Bin Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1443248831102136333)第 3 条。[证据](../../sources/notes/huang2021rejection.md#e7)
[^huang2021rejection-e9]: Jia-Bin Huang 2021，[推文串](https://twitter.com/jbhuang0604/status/1443248831102136333)第 6 条。[证据](../../sources/notes/huang2021rejection.md#e9)
[^huang2021struggle-e1]: Jeff Huang 2021，开头。[证据](../../sources/notes/huang2021struggle.md#e1)
[^huang2021struggle-e2]: Jeff Huang 2021，第一篇论文的故事。[证据](../../sources/notes/huang2021struggle.md#e2)
[^huang2021struggle-e3]: Jeff Huang 2021，结尾。[证据](../../sources/notes/huang2021struggle.md#e3)
[^huang2021struggle-e4]: Jeff Huang 2021，结尾。[证据](../../sources/notes/huang2021struggle.md#e4)
[^dettmers2019creativity-e1]: Dettmers 2019，正文中段。[证据](../../sources/notes/dettmers2019creativity.md#e1)
[^dettmers2019creativity-e2]: Dettmers 2019，正文中段。[证据](../../sources/notes/dettmers2019creativity.md#e2)
[^dettmers2019creativity-e3]: Dettmers 2019，正文中段。[证据](../../sources/notes/dettmers2019creativity.md#e3)
[^dettmers2019creativity-e4]: Dettmers 2019，正文中段。[证据](../../sources/notes/dettmers2019creativity.md#e4)
[^dettmers2019creativity-e5]: Dettmers 2019，正文中段。[证据](../../sources/notes/dettmers2019creativity.md#e5)
[^ruder2020tips-e1]: Ruder 2020，2) Work on two things。[证据](../../sources/notes/ruder2020tips.md#e1)
[^ruder2020tips-e7]: Ruder 2020，1) Read broadly。[证据](../../sources/notes/ruder2020tips.md#e7)
[^ruder2020tips-e8]: Ruder 2020，2) Work on two things。[证据](../../sources/notes/ruder2020tips.md#e8)
[^ruder2020tips-e9]: Ruder 2020，3) Be ambitious。[证据](../../sources/notes/ruder2020tips.md#e9)
[^ruder2020tips-e10]: Ruder 2020，3) Be ambitious。[证据](../../sources/notes/ruder2020tips.md#e10)
[^ruder2020tips-e11]: Ruder 2020，5) Be proactive。[证据](../../sources/notes/ruder2020tips.md#e11)
[^ruder2020tips-e12]: Ruder 2020，7) Keep a source of positive energy。[证据](../../sources/notes/ruder2020tips.md#e12)
[^ruder2020tips-e13]: Ruder 2020，7) Keep a source of positive energy。[证据](../../sources/notes/ruder2020tips.md#e13)
[^ruder2020tips-e14]: Ruder 2020，7) Keep a source of positive energy。[证据](../../sources/notes/ruder2020tips.md#e14)
[^ruder2020tips-e15]: Ruder 2020，8) Play to your strengths。[证据](../../sources/notes/ruder2020tips.md#e15)
[^ruder2020tips-e16]: Ruder 2020，10) Play the long game。[证据](../../sources/notes/ruder2020tips.md#e16)
[^ruder2020tips-e17]: Ruder 2020，7) Keep a source of positive energy。[证据](../../sources/notes/ruder2020tips.md#e17)
[^hamming1986you-e1]: Hamming 1986，讲 important problems 的部分。[证据](../../sources/notes/hamming1986you.md#e1)
[^hamming1986you-e3]: Hamming 1986，讲 ambiguity 的部分。[证据](../../sources/notes/hamming1986you.md#e3)
[^hamming1986you-e14]: Hamming 1986，讲 Bode 的话。[证据](../../sources/notes/hamming1986you.md#e14)
[^hamming1986you-e16]: Hamming 1986，讲 courage 的部分。[证据](../../sources/notes/hamming1986you.md#e16)
[^hamming1986you-e17]: Hamming 1986，总结部分。[证据](../../sources/notes/hamming1986you.md#e17)
[^hamming1986you-e18]: Hamming 1986，讲 open door 的部分。[证据](../../sources/notes/hamming1986you.md#e18)
[^hamming1986you-e19]: Hamming 1986，讲 drive 的部分。[证据](../../sources/notes/hamming1986you.md#e19)
[^hamming1986you-e21]: Hamming 1986，问答部分。[证据](../../sources/notes/hamming1986you.md#e21)
[^hamming1986you-e22]: Hamming 1986，讲 luck 的部分。[证据](../../sources/notes/hamming1986you.md#e22)
[^hamming1986you-e23]: Hamming 1986，讲 emotional commitment 的部分。[证据](../../sources/notes/hamming1986you.md#e23)
[^kidger2023know-e1]: Kidger 2023，开头。[证据](../../sources/notes/kidger2023know.md#e1)
[^kidger2023know-e2]: Kidger 2023，结尾。[证据](../../sources/notes/kidger2023know.md#e2)
[^kidger2023know-e3]: Kidger 2023，结尾。[证据](../../sources/notes/kidger2023know.md#e3)
[^nielsen2004principles-e6]: Nielsen 2004，开头。[证据](../../sources/notes/nielsen2004principles.md#e6)
[^nielsen2004principles-e7]: Nielsen 2004，Integrating research into the rest of your life。[证据](../../sources/notes/nielsen2004principles.md#e7)
[^nielsen2004principles-e8]: Nielsen 2004，Integrating research into the rest of your life。[证据](../../sources/notes/nielsen2004principles.md#e8)
[^nielsen2004principles-e9]: Nielsen 2004，Self-discipline。[证据](../../sources/notes/nielsen2004principles.md#e9)
[^nielsen2004principles-e10]: Nielsen 2004，Aspects of research。[证据](../../sources/notes/nielsen2004principles.md#e10)
[^nielsen2004principles-e11]: Nielsen 2004，Developing research strengths。[证据](../../sources/notes/nielsen2004principles.md#e11)
[^nielsen2004principles-e12]: Nielsen 2004，Developing research strengths。[证据](../../sources/notes/nielsen2004principles.md#e12)
[^nielsen2004principles-e13]: Nielsen 2004，Develop a high-quality research environment。[证据](../../sources/notes/nielsen2004principles.md#e13)
[^nielsen2004principles-e14]: Nielsen 2004，Vision。[证据](../../sources/notes/nielsen2004principles.md#e14)
[^nielsen2004principles-e15]: Nielsen 2004，Developing research strengths。[证据](../../sources/notes/nielsen2004principles.md#e15)
[^prieto2025so-e1]: Prieto 2025，"passion trap" 部分。[证据](../../sources/notes/prieto2025so.md#e1)
[^prieto2025so-e2]: Prieto 2025，讨论"使命"的部分。[证据](../../sources/notes/prieto2025so.md#e2)
[^prieto2025so-e3]: Prieto 2025，"rare and valuable skills" 部分。[证据](../../sources/notes/prieto2025so.md#e3)
[^prieto2025so-e4]: Prieto 2025，刻意练习部分。[证据](../../sources/notes/prieto2025so.md#e4)
[^prieto2025so-e5]: Prieto 2025，刻意练习部分。[证据](../../sources/notes/prieto2025so.md#e5)
[^prieto2025so-e6]: Prieto 2025，"control traps" 部分。[证据](../../sources/notes/prieto2025so.md#e6)
[^wood2020five-e1]: Wood 2020，Tip 1。[证据](../../sources/notes/wood2020five.md#e1)
[^wood2020five-e2]: Wood 2020，Tip 4。[证据](../../sources/notes/wood2020five.md#e2)
[^wood2020five-e3]: Wood 2020，Tip 4。[证据](../../sources/notes/wood2020five.md#e3)
[^wood2020five-e4]: Wood 2020，Tip 5。[证据](../../sources/notes/wood2020five.md#e4)
