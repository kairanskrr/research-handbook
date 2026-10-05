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

- 位置：§4
- 原文："Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality."
- 要点：证据必须对应主张：主张性能提升，就要分析性能，而不是易用性或通用性。

### E21

- 位置：§5
- 原文："Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- 要点：把核心主张拆成几个分句，看每个分句是全称（"总是"）、有限定（"提升 25%"）还是存在性（"找到一个实例"）的说法，它们需要不同强度的证据。

### E22

- 位置：§5
- 原文："A frequent result of this discussion is that students restate the thesis claims to reflect more precisely what the theses actually achieve."
- 要点：这样逐句检查后，学生常常会改写主张，让它准确反映实际做到的程度。

### E23

- 位置：§6
- 原文："It's important for the abstract to tell the story."
- 要点：人们根据摘要决定是否读全文，摘要必须讲清故事；但正文必须兑现摘要的承诺。

### E24

- 位置：§4
- 原文："It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- 要点：证据要说明成果对别人也有用，而不只是"在我这里管用"。
