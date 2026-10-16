# Shaw 2003: Writing Good Software Engineering Research Papers

- Source: `shaw2003writing`, [original](https://www.cs.cmu.edu/~Compose/shaw-icse03.pdf)
- Version: ICSE 2003 Minitutorial, pp. 726-736; local PDF `papers/pdf/shaw2003writing.pdf`

### E1

- Location: §3.3 What has been done before? How is your work different or better?
- Quote: "Program committees are very interested in your interpretation of prior work in the area. They want to know how your work is related to the prior work, either by building on it or by providing an alternative."
- Key point: Reviewers care about your interpretation of prior work and how your work relates to it: whether it builds on that work or offers an alternative.

### E2

- Location: §3.3, "Explain the relation to other work clearly" example
- Quote: "The galumphing problem has attracted much attention [3,8,10,18,26,32,37] [...] Smith [36] and Jones [27] worked on galumphing."
- Key point: The worst way to write related work is to pile up citations and say "many people have looked at this problem"; a bad way is to say only "so-and-so and so-and-so have worked on this problem."

### E3

- Location: §3.3, "Explain the relation to other work clearly" example
- Quote: "Smith’s blitzing approach to galumphing [36] achieved 60% coverage [39]. Jones [27] achieved 80% by flitzing, but only for pointer-free cases [16]. We modified the blitzing approach to use the kernel representation of flitzing and achieved 90% coverage while relaxing the restriction so that only cyclic data structures are prohibited."
- Key point: The "better" way: say specifically what each piece of prior work achieved and what its limitations are, then make clear exactly where your work goes beyond it.

### E4

- Location: §3.3 What has been done before? How is your work different or better?
- Quote: "If you don’t explain this, it’s hard for the program committee to understand how you’ve added to our store of knowledge. You may also damage your credibility if the program committee can’t tell whether you know about related work."
- Key point: If you do not explain how your work relates to prior work, reviewers cannot see what new knowledge you add; and if they cannot tell whether you know the related work, your credibility suffers.

### E5

- Location: §1 Introduction
- Quote: "What, precisely, was your contribution? [...] What question did you answer? [...] Why should the reader care? [...] What larger question does this address?"
- Key point: A study must first make clear what exactly you contributed, what question you answered, why readers should care, and what larger question it bears on.

### E6

- Location: §1 Introduction
- Quote: "Why should the reader believe your result? [...] What standard should be used to evaluate your claim? [...] What concrete evidence shows that your result satisfies your claim?"
- Key point: It must also make clear why readers should believe your results, what standard your claims should be judged by, and what concrete evidence shows that the results satisfy the claims.

### E7

- Location: §2 What, precisely, was your contribution?
- Quote: "Before reporting what you did, explain what problem you set out to solve or what question you set out to answer —and why this is important."
- Key point: Before describing what you did, state the problem you are solving and the question you are answering, and why it matters.

### E8

- Location: §2.1, Table 1 Types of software engineering research questions
- Quote: "Feasibility study or exploration [...] Does X even exist, and if so what is it like? Is it possible to accomplish X at all?"
- Key point: Research questions come in different types, such as "how to do it," "how to evaluate it," "what is a specific object like," "what holds in general," and "is it feasible"; feasibility or exploratory questions ask "does X exist" or "is it possible to do X."

### E9

- Location: §4.1 What kinds of validation do software engineers do?
- Quote: "It is essential to select a form of validation that is appropriate for the type of research result and the method used to obtain the result. As an obvious example, a formal model should be supported by rigorous derivation and proof, not by one or two simple examples."
- Key point: The validation must fit the type of result and the method used to obtain it; for example, a formal model calls for rigorous derivation and proof, not one or two simple examples.

### E10

- Location: §4.1, after Table 5
- Quote: "Validation purely by persuasion is rarely sufficient for a research paper. Note, though, that if the original question was about feasibility, a working system, even without analysis, can suffice"
- Key point: Persuasion alone is rarely enough; but if the question itself is "can it be done," a running system may be enough to answer it.

### E11

- Location: §4.3 What do program committees look for?
- Quote: "The program committee looks for solid evidence to support your result. It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- Key point: "It works for me" is not enough; you also need evidence that it is useful to others.

### E12

- Location: §4.3 What do program committees look for?
- Quote: "Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality. And conversely."
- Key point: The validation must target the claim: if you claim a performance improvement, analyze performance, not ease of use or generality.

### E13

- Location: §4.3 What do program committees look for?
- Quote: "If you used an analysis technique, follow the rules of that analysis technique."
- Key point: Whatever analysis method you use, follow that method's own rules.

### E14

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "Clearly, the researcher does not have free choice to mix and match the techniques—validating the correctness of a formal model through field study is as inappropriate as attempting formal verification of a method based on good organization of rules of thumb."
- Key point: Questions, results, and validations cannot be mixed and matched freely; validating the correctness of a formal model with a field study is as inappropriate as formally verifying a set of rules of thumb.

### E15

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "Blindly adopting the research paradigm someone used last year for a completely different problem is a different case, of course, and it can lead to serious misfits."
- Key point: Blindly adopting a research paradigm that someone else used for a completely different question leads to serious mismatches.

### E16

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "Ask of each clause whether it is a global statement ("always", "fully"), a qualified statement ("a 25% improvement", "for noncyclic structures…"), or an existential statement {"we found an instance of"). Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- Key point: Break the claim into clauses and decide for each whether it is universal ("always," "completely"), qualified ("improves by 25%," "for acyclic structures"), or existential ("we found an instance"); the three kinds of claim need different strengths of evidence.

### E17

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "A frequent result of this discussion is that students restate the thesis claims to reflect more precisely what the theses actually achieve. If we have this discussion early enough in the thesis process, students think about planning the research with demonstrable claims in mind."
- Key point: After such a discussion, students often rewrite their claims more accurately; if the discussion happens early enough, students plan their research around claims that can be supported.

### E18

- Location: §3.3, "What's new here?"
- Quote: "Use verbs that show results and achievement, not just effort and activity."
- Key point: Describe contributions with verbs of results and achievement, not verbs that only describe effort and activity (such as "investigated" or "explored").

### E19

- Location: §1
- Quote: "In a research paper, the author explains to an interested reader what he or she accomplished, and how the author accomplished it, and why the reader should care."
- Key point: A paper must answer three kinds of questions: what exactly your contribution is (what question it answers and why it matters), what the new result is, and why readers should believe it.

### E20

> Withdrawn: duplicates [E12](#e12) (the quote is fully contained in E12).

- Location: §4
- Quote: "Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality."
- Key point: The evidence must correspond to the claim: if you claim a performance improvement, analyze performance, not ease of use or generality.

### E21

> Withdrawn: duplicates [E16](#e16) (the quote is fully contained in E16).

- Location: §5
- Quote: "Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- Key point: Break the central claim into clauses and check whether each is universal ("always"), qualified ("improves by 25%"), or existential ("found an instance"); they need different strengths of evidence.

### E22

> Withdrawn: duplicates [E17](#e17) (the quote is fully contained in E17).

- Location: §5
- Quote: "A frequent result of this discussion is that students restate the thesis claims to reflect more precisely what the theses actually achieve."
- Key point: After checking clause by clause like this, students often rewrite their claims so that they accurately reflect what was actually achieved.

### E23

- Location: §6
- Quote: "It's important for the abstract to tell the story."
- Key point: People decide from the abstract whether to read the full paper, so the abstract must tell the story; but the body must deliver what the abstract promises.

### E24

> Withdrawn: duplicates [E11](#e11) (the quote is fully contained in E11).

- Location: §4
- Quote: "It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- Key point: The evidence should show that the result is useful to others, not just that "it works for me."

### E25

- Location: §2.1, Table 1 Types of software engineering research questions
- Quote: "How can we do/create/modify/evolve (or automate doing) X? What is a better way to do/create/modify/evolve X?" / "How can I evaluate the quality/correctness of X? How do I choose between X and Y?"
- Key point: Engineering research often answers two kinds of questions: "how can we do (or automate) X, and is there a better way," and "how can we evaluate the quality or correctness of X, and how do we choose between X and Y."

### E26

- Location: §3.2 Which of these are most common?
- Quote: "By far the most common kind of ICSE paper reports a new procedure or technique for development or analysis."
- Key point: At ICSE (the International Conference on Software Engineering), the most common kind of paper reports a new development or analysis technique.

### E27

- Location: §3.1, Table 3 Types of software engineering research results
- Quote: "a technique should be operational—not advice or guidelines, but a procedure" / "Implemented tool that embodies a technique; formal language to support a technique or model"
- Key point: A "technique" offered as a result must be an operational procedure, not advice or guidelines; a "tool" is an implementation that embodies a technique.

### E28

- Location: §4.1, Table 5 Types of software engineering research validation and the explanation after it
- Quote: "The "slice of life" example is most likely to be convincing, especially if accompanied by an explanation of why the simplified example retains the essence of the problem being solved. Toy or textbook examples often fail to provide persuasive validation"
- Key point: Examples taken from real systems are the most convincing; ideally explain why a simplified example still retains the essence of the problem. Toy examples or textbook examples are often unconvincing.

### E29

- Location: §4.3 What do program committees look for?
- Quote: "Is the validation related to the claim? If you're claiming performance improvement, validation should analyze performance, not ease of use or generality."
- Key point: The validation must target the claim: if you claim a performance improvement, analyze performance, not ease of use or generality.

### E30

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "Global statements often require analytic validation, qualified statements can often be validated by evaluation or careful examination of experience, and existential statements can sometimes be validated by a single positive example."
- Key point: Universal claims ("always," "completely") usually need analytic argument; qualified claims ("improves by 25%," "for acyclic structures") can rest on evaluation; for existential claims ("found an instance"), a single positive example is sometimes enough.

### E31

- Location: §2.3
- Quote: "If the program committee has trouble figuring out whether you developed a new evaluation technique and demonstrated it on an example, or applied a technique you reported last year to a new real-world example, or evaluated the use of a well-established evaluation technique, you have not been clear."
- Key point: Let reviewers see at a glance which kind of work you did: proposing and demonstrating a new technique, applying an old technique to new examples, or evaluating a mature technique.

### E32

- Location: §4.2 Which of these are most common?
- Quote: "The most successful kinds of validation were based on analysis and real-world experience. Well-chosen examples were also successful. Persuasion was not persuasive"
- Key point: The most successful kinds of validation are analysis and real-world experience; carefully chosen examples also work well; pure persuasion is not convincing.

### E33

- Location: §4.1, Table 5 (Experience row)
- Quote: "My result has been used on real examples by someone other than me"
- Key point: "Experience" validation means the result has been used on real examples by people other than the authors, with evidence that it works.

### E34

- Location: §1, "What is your new result?"
- Quote: "What previous work (yours or someone else’s) do you build on? What do you provide a superior alternative to?" / "How is your result different from and better than this prior work?"
- Key point: Make clear which prior work you build on and what you replace, and how your work differs from it and why it is better.

### E35

- Location: §4.3 What do program committees look for?
- Quote: "It's not enough that your idea works for you, there must also be evidence that the idea or the technique will help someone else as well."
- Key point: "It works for me" is not enough; you also need evidence that it is useful to others.

### E36

- Location: §3.3
- Quote: "If you introduce a new metric, define it precisely. Does it measure what it purports to measure and do so better than the alternatives?"
- Key point: When you introduce a new metric, define it precisely and show that it actually measures what it claims to measure and does so better than existing metrics.

### E37

- Location: §4.1, Table 5 (Blatant assertion row)
- Quote: "Blatant assertion No serious attempt to evaluate result. This is highly unlikely to be acceptable"
- Key point: A paper that only makes assertions without seriously evaluating its results is almost never accepted.

### E38

- Location: §2.1 What kinds of questions do software engineers investigate?
- Quote: "Software engineering research answers questions about methods of development or analysis, about details of designing or evaluating a particular instance, about generalizations over whole classes of systems or techniques, or about exploratory issues concerning existence or feasibility."
- Key point: The questions software engineering research answers fall into a few kinds: methods of development or analysis, design or evaluation of a particular instance, generalization over a whole class of systems or techniques, and exploration of existence or feasibility.

### E39

- Location: §2.1, Table 1 Types of software engineering research questions
- Quote: "How good is Y? What is property X of artifact/method Y? What is a (better) design, implementation, maintenance, or adaptation for application X? How does X compare to Y? What is the current state of X / practice of Y?"
- Key point: In Table 1, the "design, evaluation, or analysis of a particular instance" category includes questions such as "how good is Y," "how does X compare to Y," and "what is the current state of X."

### E40

- Location: §2.1, Table 1 Types of software engineering research questions
- Quote: "Given X, what will Y (necessarily) be? What, exactly, do we mean by X? What are its important characteristics? What is a good formal/empirical model for X? What are the varieties of X, how are they related?"
- Key point: In Table 1, the "generalization or characterization" category includes questions such as "given X, what will Y necessarily be" and "what are the varieties of X, and how are they related."

### E41

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "Selecting a type of result that will answer a given question usually does not seem to present much difficulty, at least for researchers who think carefully about the choice. Blindly adopting the research paradigm someone used last year for a completely different problem is a different case, of course, and it can lead to serious misfits."
- Key point: A thoughtful researcher will not find it hard to pick the right type of result for a question; but copying a research paradigm someone else used for a completely different question leads to a serious mismatch.

### E42

- Location: §5 How do you combine the elements into a research strategy?
- Quote: "Choosing a good form of validation is much harder, and this is often a source of difficulty in completing a successful paper."
- Key point: Choosing the right validation is much harder, and it is often why a paper fails.
