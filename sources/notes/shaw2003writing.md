# Shaw 2003：Writing Good Software Engineering Research Papers

- 资料：`shaw2003writing`，[原文](https://www.cs.cmu.edu/~Compose/shaw-icse03.pdf)
- 版本：ICSE 2003 Minitutorial，pp. 726-736；本地 PDF `papers/pdf/shaw2003writing.pdf`

### E1

- 位置：§3.3 What has been done before? How is your work different or better?
- 原文："Program committees are very interested in your interpretation of prior work in the area. They want to know how your work is related to the prior work, either by building on it or by providing an alternative."
- 要点：审稿人看重的是你对已有工作的解读，以及你的工作与它们的关系：是在它们基础上推进，还是提供了另一种选择。

### E2

- 位置：§3.3，"Explain the relation to other work clearly"示例
- 原文："The galumphing problem has attracted much attention [3,8,10,18,26,32,37] [...] Smith [36] and Jones [27] worked on galumphing."
- 要点：最差的相关工作写法是堆一串引用说"很多人关注这个问题"；差的写法是只说"某某和某某做过这个问题"。

### E3

- 位置：§3.3，"Explain the relation to other work clearly"示例
- 原文："Smith’s blitzing approach to galumphing [36] achieved 60% coverage [39]. Jones [27] achieved 80% by flitzing, but only for pointer-free cases [16]. We modified the blitzing approach to use the kernel representation of flitzing and achieved 90% coverage while relaxing the restriction so that only cyclic data structures are prohibited."
- 要点："更好"的写法：具体说出每项已有工作做到了什么、有什么限制，再说清自己的工作在哪一点上超过它们。

### E4

- 位置：§3.3 What has been done before? How is your work different or better?
- 原文："If you don’t explain this, it’s hard for the program committee to understand how you’ve added to our store of knowledge. You may also damage your credibility if the program committee can’t tell whether you know about related work."
- 要点：不讲清与已有工作的关系，审稿人就看不出你增加了什么新知识；看不出你是否了解相关工作，还会损害你的可信度。

### E5

- 位置：§1 Introduction
- 原文："What, precisely, was your contribution? [...] What question did you answer? [...] Why should the reader care? [...] What larger question does this address?"
- 要点：一项研究首先要说清：你到底贡献了什么、回答了什么问题、读者为什么要关心、它关系到哪个更大的问题。

### E6

- 位置：§1 Introduction
- 原文："Why should the reader believe your result? [...] What standard should be used to evaluate your claim? [...] What concrete evidence shows that your result satisfies your claim?"
- 要点：还要说清：读者凭什么相信你的结果？应该用什么标准评价你的主张？什么具体证据表明结果满足了主张？

### E7

- 位置：§2 What, precisely, was your contribution?
- 原文："Before reporting what you did, explain what problem you set out to solve or what question you set out to answer —and why this is important."
- 要点：在讲做了什么之前，先讲要解决什么问题、回答什么问题，以及它为什么重要。

### E8

- 位置：§2.1，Table 1 Types of software engineering research questions
- 原文："Feasibility study or exploration [...] Does X even exist, and if so what is it like? Is it possible to accomplish X at all?"
- 要点：研究问题有不同类型，例如"怎么做"、"怎么评估"、"某个具体对象怎么样"、"一般规律是什么"、"是否可行"；可行性/探索类问题问的是"X 是否存在""X 能否做到"。

### E9

- 位置：§4.1 What kinds of validation do software engineers do?
- 原文："It is essential to select a form of validation that is appropriate for the type of research result and the method used to obtain the result. As an obvious example, a formal model should be supported by rigorous derivation and proof, not by one or two simple examples."
- 要点：验证方式必须和结果类型、获得结果的方法相匹配；例如形式化模型要靠严格推导和证明，而不是一两个简单例子。

### E10

- 位置：§4.1，Table 5 后
- 原文："Validation purely by persuasion is rarely sufficient for a research paper. Note, though, that if the original question was about feasibility, a working system, even without analysis, can suffice"
- 要点：纯靠说服很少足够；但如果问题本身是"能不能做到"，一个能运行的系统就可能足以回答。

### E11

- 位置：§4.3 What do program committees look for?
- 原文："The program committee looks for solid evidence to support your result. It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- 要点：光是"对你自己有效"不够，还需要证据表明它对别人也有用。

### E12

- 位置：§4.3 What do program committees look for?
- 原文："Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality. And conversely."
- 要点：验证必须对准主张：声称性能提升，就要分析性能，而不是易用性或通用性。

### E13

- 位置：§4.3 What do program committees look for?
- 原文："If you used an analysis technique, follow the rules of that analysis technique."
- 要点：用了哪种分析方法，就要遵守那种方法自己的规则。

### E14

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："Clearly, the researcher does not have free choice to mix and match the techniques—validating the correctness of a formal model through field study is as inappropriate as attempting formal verification of a method based on good organization of rules of thumb."
- 要点：问题、结果和验证方式不能随意搭配；用实地研究验证形式化模型的正确性，和对一套经验法则做形式化验证一样不合适。

### E15

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："Blindly adopting the research paradigm someone used last year for a completely different problem is a different case, of course, and it can lead to serious misfits."
- 要点：盲目照搬别人为完全不同的问题用过的研究范式，会导致严重的不匹配。

### E16

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："Ask of each clause whether it is a global statement ("always", "fully"), a qualified statement ("a 25% improvement", "for noncyclic structures…"), or an existential statement {"we found an instance of"). Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- 要点：把主张拆成几个分句，逐一判断它是全称的（"总是""完全"）、有限定的（"提升 25%""对无环结构"），还是存在性的（"我们找到了一个实例"）；三类主张需要的证据强度不同。

### E17

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："A frequent result of this discussion is that students restate the thesis claims to reflect more precisely what the theses actually achieve. If we have this discussion early enough in the thesis process, students think about planning the research with demonstrable claims in mind."
- 要点：这样讨论之后，学生常会把主张改写得更准确；如果讨论得够早，学生就会围绕"能被证明的主张"来规划研究。

### E18

- 位置：§3.3，"What's new here?"
- 原文："Use verbs that show results and achievement, not just effort and activity."
- 要点：描述贡献要用表示结果和成就的动词，而不是只表示付出和活动的动词（如"研究了""探索了"）。

### E19

- 位置：§1
- 原文："In a research paper, the author explains to an interested reader what he or she accomplished, and how the author accomplished it, and why the reader should care."
- 要点：论文要回答三类问题：你的贡献到底是什么（回答了什么问题、为什么重要）、新结果是什么、读者为什么该相信它。

### E20

> 已作废：与 [E12](#e12) 重复（原文被 E12 完整包含）。

- 位置：§4
- 原文："Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality."
- 要点：证据必须对应主张：主张性能提升，就要分析性能，而不是易用性或通用性。

### E21

> 已作废：与 [E16](#e16) 重复（原文被 E16 完整包含）。

- 位置：§5
- 原文："Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- 要点：把核心主张拆成几个分句，看每个分句是全称（"总是"）、有限定（"提升 25%"）还是存在性（"找到一个实例"）的说法，它们需要不同强度的证据。

### E22

> 已作废：与 [E17](#e17) 重复（原文被 E17 完整包含）。

- 位置：§5
- 原文："A frequent result of this discussion is that students restate the thesis claims to reflect more precisely what the theses actually achieve."
- 要点：这样逐句检查后，学生常常会改写主张，让它准确反映实际做到的程度。

### E23

- 位置：§6
- 原文："It's important for the abstract to tell the story."
- 要点：人们根据摘要决定是否读全文，摘要必须讲清故事；但正文必须兑现摘要的承诺。

### E24

> 已作废：与 [E11](#e11) 重复（原文被 E11 完整包含）。

- 位置：§4
- 原文："It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- 要点：证据要说明成果对别人也有用，而不只是"在我这里管用"。

### E25

- 位置：§2.1，Table 1 Types of software engineering research questions
- 原文："How can we do/create/modify/evolve (or automate doing) X? What is a better way to do/create/modify/evolve X?" / "How can I evaluate the quality/correctness of X? How do I choose between X and Y?"
- 要点：工程研究常回答两类问题："怎样做到（或自动做到）X、有没有更好的做法"，以及"怎样评估 X 的质量或正确性、怎样在 X 和 Y 之间选择"。

### E26

- 位置：§3.2 Which of these are most common?
- 原文："By far the most common kind of ICSE paper reports a new procedure or technique for development or analysis."
- 要点：在 ICSE（国际软件工程大会）上，最常见的论文是报告一种新的开发或分析技术。

### E27

- 位置：§3.1，Table 3 Types of software engineering research results
- 原文："a technique should be operational—not advice or guidelines, but a procedure" / "Implemented tool that embodies a technique; formal language to support a technique or model"
- 要点：作为成果的"技术"必须是可操作的过程，而不是建议或指导原则；"工具"是体现某种技术的实现。

### E28

- 位置：§4.1，Table 5 Types of software engineering research validation 及其后说明
- 原文："The "slice of life" example is most likely to be convincing, especially if accompanied by an explanation of why the simplified example retains the essence of the problem being solved. Toy or textbook examples often fail to provide persuasive validation"
- 要点：取自真实系统的例子最有说服力，最好说明简化后的例子为什么仍保留了问题的本质；玩具例子或教科书例子往往没有说服力。

### E29

- 位置：§4.3 What do program committees look for?
- 原文："Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality."
- 要点：验证必须对准主张：声称性能提升，就要分析性能，而不是易用性或通用性。

### E30

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- 要点：全称主张（"总是""完全"）通常要分析论证，有限定的主张（"提升 25%""对无环结构"）可以靠评估，存在性主张（"找到一个实例"）有时一个正例就够。

### E31

- 位置：§2.3
- 原文："If the program committee has trouble figuring out whether you developed a new evaluation technique and demonstrated it on an example, or applied a technique you reported last year to a new real-world example, or evaluated the use of a well-established evaluation technique, you have not been clear."
- 要点：要让审稿人一眼看出你做的是哪一种：提出新技术并演示、把旧技术用到新例子上，还是评估一项成熟技术。

### E32

- 位置：§4.2 Which of these are most common?
- 原文："The most successful kinds of validation were based on analysis and real-world experience. Well-chosen examples were also successful. Persuasion was not persuasive"
- 要点：最成功的验证方式是分析和真实使用经验，精心挑选的例子也不错，纯说服则没有说服力。

### E33

- 位置：§4.1，Table 5（Experience 一行）
- 原文："My result has been used on real examples by someone other than me"
- 要点："经验"类验证指成果被作者以外的人用在真实例子上，并有证据表明有效。

### E34

- 位置：§1，"What is your new result?"
- 原文："What previous work (yours or someone else’s) do you build on? What do you provide a superior alternative to?" / "How is your result different from and better than this prior work?"
- 要点：要说清建立在哪些已有工作之上、替代了什么，以及和它们相比有什么不同、好在哪里。

### E35

- 位置：§4.3 What do program committees look for?
- 原文："It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- 要点：光是"对你自己有效"不够，还需要证据表明它对别人也有用。

### E36

- 位置：§3.3
- 原文："If you introduce a new metric, define it precisely. Does it measure what it purports to measure and do so better than the alternatives?"
- 要点：引入新指标时要精确定义，并说明它确实测了它声称要测的东西，而且比已有指标更好。

### E37

- 位置：§4.1，Table 5（Blatant assertion 一行）
- 原文："Blatant assertion No serious attempt to evaluate result. This is highly unlikely to be acceptable"
- 要点：只有断言、不认真评估结果的论文，几乎不可能被接受。

### E38

- 位置：§2.1 What kinds of questions do software engineers investigate?
- 原文："Software engineering research answers questions about methods of development or analysis, about details of designing or evaluating a particular instance, about generalizations over whole classes of systems or techniques, or about exploratory issues concerning existence or feasibility."
- 要点：软件工程研究回答的问题分几类：开发或分析的方法、具体实例的设计或评估、对一整类系统或技术的概括、存在性或可行性的探索。

### E39

- 位置：§2.1，Table 1 Types of software engineering research questions
- 原文："How good is Y? What is property X of artifact/method Y? What is a (better) design, implementation, maintenance, or adaptation for application X? How does X compare to Y? What is the current state of X / practice of Y?"
- 要点：Table 1 中"具体实例的设计、评估或分析"一类问题的问法，包括"Y 有多好""X 和 Y 比较如何""X 的现状如何"。

### E40

- 位置：§2.1，Table 1 Types of software engineering research questions
- 原文："Given X, what will Y (necessarily) be? What, exactly, do we mean by X? What are its important characteristics? What is a good formal/empirical model for X? What are the varieties of X, how are they related?"
- 要点：Table 1 中"概括或刻画"一类问题的问法，包括"给定 X，Y 必然是什么"和"X 有哪些种类，彼此什么关系"。

### E41

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："Selecting a type of result that will answer a given question usually does not seem to present much difficulty, at least for researchers who think carefully about the choice. Blindly adopting the research paradigm someone used last year for a completely different problem is a different case, of course, and it can lead to serious misfits."
- 要点：认真思考的研究者不难为问题选对结果类型；但照搬别人为完全不同问题用过的研究范式，会导致严重错配。

### E42

- 位置：§5 How do you combine the elements into a research strategy?
- 原文："Choosing a good form of validation is much harder, and this is often a source of difficulty in completing a successful paper."
- 要点：选好验证方式要难得多，常常是论文做不成的原因。
