# Proof

> The reasoning on this page applies to any research whose main result is a proof; the examples and concrete steps come from computer science. Where mathematics or philosophy works differently, the text says so.

If the central claim you want to make is "under conditions C, X **always** holds" rather than "X holds on the data we tested", your project follows the proof strategy. This page helps you think through four things: what this kind of research produces, what evidence is enough, where to learn the concrete methods, and how it changes what you do at each stage of the project.

How to pick a problem, push a proof forward, write a structured proof and check it for errors is already covered step by step in [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md) in the computer science section. This page does not repeat it and only links there when needed. For what we mean by claim, evidence, research strategy and research method, see [Key concepts](../00_start-here/key-concepts.md).

---

## 1. What kind of knowledge this research produces

A proof produces **a conclusion that necessarily holds under stated assumptions**: as long as the assumptions hold, the conclusion holds in every case, and you don't need data to "see whether it's true". The validation has to fit the type of result: a formal model must be backed by rigorous derivation and proof, not by one or two simple examples[^shaw2003writing-e9].

There are four common kinds of result `[Our analysis]`:

| Result | Computer science example (large language models and smart-contract security) | Question it answers |
|---|---|---|
| Upper bound (an algorithm and its analysis) | "Our detection algorithm terminates on every contract, and its running time is at most the square of the contract's length" | How well can it be done? |
| Lower bound, impossibility result | "Every static detection method that satisfies condition C must miss vulnerabilities on some class of contracts" | What is the best possible? What can't be done at all? |
| Models and definitions | A precise formal definition of "this contract has no reentrancy vulnerability" | Which concepts should we use to describe the problem? |
| Formal guarantee | "Under a given semantic model of the Ethereum Virtual Machine, no contract that the tool marks as 'reentrancy-free' can be hit by a reentrancy attack", backed by a machine-checked proof | Under explicit assumptions, is the system guaranteed to have a given property? |

A real formal guarantee: seL4 is an operating-system kernel with 8,700 lines of C and 600 lines of assembly[^klein2009sel4-e4]. Its team used a machine-checked proof to show that the kernel's C implementation always strictly conforms to its abstract specification (a precise description of how the kernel should behave)[^klein2009sel4-e8]. The result comes with explicit assumptions: the compiler, the assembly code, the boot code, cache management and the hardware are assumed correct, and everything else is proved[^klein2009sel4-e1]. As long as those assumptions hold, the kernel will never crash or behave unexpectedly[^klein2009sel4-e3].

**How it differs from other strategies** `[Our analysis]`:

| | Proof | Building and improving | Comparative evaluation |
|---|---|---|---|
| Main evidence | The proof | The thing you built + experiments | Measurements on a shared task |
| Scope of the conclusion | Every case that satisfies the assumptions | The cases the experiments covered | The cases the evaluation covered |
| Biggest risk | The proof is wrong; the assumptions are far from reality | Unfair or irreproducible experiments | The benchmark doesn't represent real use |

Many computer science papers are mixed: they present a new tool (building and improving) and also prove some property of it. In that case, let the central claim decide the main strategy; hold the proof part to the standards on this page and the experimental part to the standards in [Building and improving](build_improve.md) `[Our analysis]`.

**Write it down:** Write your central claim in the form "under assumptions A, B and C, conclusion X holds". If you can't write down the assumptions, or the conclusion contains words like "most" or "usually", it may not be a proof-style claim.

## 2. What evidence is enough

When reviewers and readers read a proof paper, they press on the five questions below, and you need an answer to each `[Our analysis]`.

**(1) Are all the assumptions written out?** A theorem statement can easily hide unstated assumptions: Lamport (a researcher in distributed systems and formal methods) gives the example of a theorem that silently assumed a < b without saying so[^lamport2012how-e6]. He also points out that leaving out an assumption like "the set is nonempty" is a minor slip in a mathematical theorem but can be a serious bug in an algorithm[^lamport2012how-e9]. What to do: as seL4 did, list one by one the parts that are "assumed correct, not proved"[^klein2009sel4-e1], and state every assumption in the theorem `[Our analysis]`.

**(2) Is the proof complete?** In Lamport's experience, most errors come from proofs that are not broken down to enough levels of detail[^lamport1995how-e5]. His rule of thumb: expand the proof until every statement at the lowest level is obvious, then expand one level more[^lamport1995how-e6]. A proof sketch (a few sentences describing the idea) is useful, but it is not a proof[^lamport2012how-e13]. For how to write a hierarchical proof that can be checked step by step, see [Step 3](../07_fields/computer-science/practices/theoretical_research.md#step-3-write-the-proof-so-it-can-be-checked-all-proof-based-work) of Theoretical research.

**(3) Can other people check it?** The mathematician Thurston observed that people are not very good at checking the formal correctness of a proof line by line, but quite good at spotting where a proof might be weak[^thurston1994proof-e9]. In his view, the reliability of mathematical results comes mainly from mathematicians thinking carefully and critically about the ideas[^thurston1994proof-e11]. So he argues for writing proofs clearly and as simply as possible, so that weak points are easy to find[^thurston1994proof-e10]. Journal review also puts correctness first: the American Mathematical Society's ethical guidelines say an editor should accept a paper only when reasonably sure it is correct[^ams2022ethical-e9]. But no one finding an error doesn't mean there isn't one: Lamport cites an anecdotal claim that as many as a third of the papers in mathematical journals contain mistaken theorems or proofs[^lamport1995how-e1] (this is an anecdote, not a statistic).

**(4) Do you need machine checking?** Machine checking means using a proof assistant (software that can check a formal proof step by step) to verify every step. Lamport argues that formalizing mathematics is not hard; what is hard is writing proofs a machine can check[^lamport2012how-e8]. The seL4 project gives you a feel for the scale of the costs and benefits, but these numbers belong to that one project and are not a general rule:

- Cost: the proof is about 200,000 lines of Isabelle (a proof assistant) script, a count that includes the framework, libraries and automatically generated proofs; the whole proof took about 20 person-years[^klein2009sel4-e4].
- Benefit: before formal verification started, internal student projects and porting work had found 16 bugs in the implementation; formal verification found another 144[^klein2009sel4-e6].
- Side benefit: the authors repeatedly found that, to make the system verifiable, designers were pushed toward the simplest, clearest solution, which led to a better design[^klein2009sel4-e7].

Lamport also notes that proofs about algorithms are often not mathematically deep but are tedious, with a great many details to check[^lamport2012how-e10]. So proofs with many details, where one missed assumption becomes a bug (concurrent algorithms, protocols, kernels, contract analysis tools), are better candidates for machine checking; an ordinary theorem may not need it `[Our analysis]`. When a proof involves symbolic computation, a workshop report on reproducibility in computational mathematics (Stodden et al. 2013) recommends in its checklist cross-checking with two different software packages, because even the best software has bugs[^stodden2013setting-e5].

**(5) How far are the assumptions from reality?** However rigorous a proof is, it only answers for its assumptions and its specification. The seL4 authors themselves acknowledge that a proof of implementation correctness does not guarantee that the specification describes the behavior users expect[^klein2009sel4-e2]. In the contract example `[Our analysis]`: you prove that "under virtual-machine semantic model M, no contract the tool marks as safe can be reentered", and a reviewer will ask whether model M covers the ways contracts are actually called on the real chain, and whether your definition of "reentrancy-safe" matches the one the community uses. Where your assumptions are on the strong side or your conclusion on the weak side, the mathematician Tao advises saying so honestly, for example "we do not know whether hypothesis H is necessary"[^taowriting-e4].

**Write it down:** List every assumption your theorem depends on, and next to each write "Does this hold for real contracts? On what grounds?" Any you can't answer go into your limitations section.

## 3. Common research methods

A strategy says what knowledge you want to produce; a method says how you get the evidence. These are the methods commonly used with the proof strategy:

| Method | When to use it | Where to read more |
|---|---|---|
| Hand proof (theorem and proof) | Upper and lower complexity bounds, algorithm correctness, impossibility results, properties of new definitions | [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md): choosing a problem, pushing a proof forward, writing structured proofs, checking your own errors |
| Machine-checked proof (interactive theorem proving: a person guides, a proof assistant checks each step) | Systems and algorithms with many details and a high cost of error | The machine-checking part of [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md#step-4-check-your-own-proof-all-proof-based-work-the-machine-checking-part-is-computer-science) |
| Computer-assisted proof, experimental mathematics | Using computation to explore conjectures, or making computation part of the proof | The "Norms of the field" section of the [mathematics field overview](../07_fields/mathematics/README.md#norms-in-this-field) |

According to the seL4 paper, interactive theorem proving needs human input and creativity to build and guide the proof. Its advantage is that, unlike more automatic verification methods such as static analysis and model checking (a program automatically explores the system's possible states and checks a property), it is not limited to specific properties or finite state spaces[^klein2009sel4-e5]. On computer-assisted proof, the workshop report mentioned above recommends that journals require papers making important claims (for example, a computer proof of a long-open mathematical result) to undergo rigorous verification and to publish the full details of the computation[^stodden2013setting-e4].

**Proofs are often paired with experiments.** In software engineering, the ACM SIGSOFT Empirical Standards list providing "correctness arguments for the key analytical and theoretical contributions (e.g. theorems, complexity analyses, mathematical proofs)" as a desirable attribute of engineering research[^ralph2020empirical-e88]; a "theoretical guarantee" can also be the dimension on which a new tool beats existing ones[^ralph2020empirical-e95]. Vandewalle et al. note that in signal processing, theorems are often accompanied by numerical simulations that help readers get an intuitive feel for the results[^vandewalle2009reproducible-e12].

**Compare with philosophical argument.** Most of the arguments philosophers deal with are also (or claim to be) deductive, and mathematical proofs are the textbook example of this kind of argument[^pryor2025terms-e3]. The difference lies in the premises: the premises of a philosophical argument are rarely beyond all doubt, so even a valid argument usually isn't conclusive[^pryor2025terms-e12]. That is why most of the work in a philosophy paper goes into defending premises and answering objections, and why it generally falls under the [Interpretation and argument](interpret_argue.md) strategy; for the concrete methods, see [Philosophical argument](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md) `[Our analysis]`.

Don't use the wrong kind of validation: discussing software engineering research, Shaw points out that using a field study to check whether a formal model is correct is as inappropriate as formally verifying a set of rules of thumb[^shaw2003writing-e14].

## 4. How it shapes the whole project

When you follow the proof strategy, here is what to add or do differently at each stage `[Our analysis]`. The advice on pushing forward and checking yourself comes mostly from the mathematician Tao's career advice and from the theoretical computer scientist Aaronson's list of "signs that a claimed breakthrough is wrong"; this is personal experience, not a field rule. For the detailed steps, see [Steps 1 and 2 of Theoretical research](../07_fields/computer-science/practices/theoretical_research.md#2-how-to-do-it).

| Stage | What to do in particular on the proof strategy |
|---|---|
| [Converging on a project](../01_from-interest-to-project/03_converge.md) | Write your claim as a theorem. As a newcomer, start with tractable problems: famous hard problems are almost never solved out of nowhere[^taocareer-e13], and Tao advises spending most of your time on more tractable problems to build experience and reputation[^taocareer-e14] |
| [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md) | Once you find the key papers, check who cites them[^taocareer-e16] to make sure the problem is still open. In particular, look for related lower bounds and impossibility results: Aaronson lists "the approach conflicts with a known impossibility result (which the authors never mention)" as a sign of a wrong breakthrough[^aaronson2008ten-e3] |
| [From research questions to an evidence plan](../02_from-project-to-study/01_question-to-evidence.md), [Choosing a strategy and a method](../02_from-project-to-study/02_choose-strategy-and-method.md) | Decide between a hand proof and machine checking. Compare your definitions word for word with the standard literature, and keep your notation as close to existing work as you can[^taowriting-e8] |
| [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md) | A proof has no sampling error, but it does have the question of whether its assumptions and specification are close to reality[^klein2009sel4-e2] |
| [Pilot first: rule out the biggest risks](../02_from-project-to-study/04_pilot-and-derisk.md) | Try to find a counterexample first: if you find one, you save a lot of time, and the counterexample itself may be publishable; if you don't, the obstacles you hit will hint at how the proof should go[^taocareer-e2]. Isolate a simplified special case and work on it first[^taocareer-e5] |
| [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md) | Value partial progress: it is a key stepping stone to solving the whole problem[^taocareer-e6], and many intermediate steps are publishable papers in their own right[^taocareer-e22]. Write up interesting arguments in draft form, in enough detail that you can reconstruct them later[^taocareer-e18] |
| [Analysis and interpretation](../03_conduct-and-analyze/02_analyze-and-interpret.md) | "Analysis" becomes error hunting: could your method also "prove" a stronger statement that is known to be false[^taocareer-e1]? Is every key assumption actually used[^taowriting-e13]? |
| [Telling the story and writing the paper](../04_write-and-publish/01_story-and-paper.md) | Following Lamport, make the proof readable through hierarchical structure and by naming (numbering) every step[^lamport2012how-e1]; put a sketch before each major proof as a roadmap for the reader[^lamport1995how-e2]; describe your results neither as smaller nor as bigger than they are[^taowriting-e3] |
| [Choosing a venue and submitting](../04_write-and-publish/02_venue-and-submission.md) | Theoretical computer science values conferences, and there is also a tradition of expanding conference papers into full journal versions[^cra1999evaluating-e4]; most mathematical research is published in peer-reviewed journals[^amsculture2006rates-e1] |
| [Reviews, revision, and what to do after rejection](../04_write-and-publish/03_review-and-revision.md) | Don't take one rejection too hard: nearly half of the papers that won the Gödel Prize (the best-paper award in theoretical computer science) were first rejected by top theory conferences or never appeared there at all[^fortnow2009time-e8] |

**Write it down:** Add a "look for counterexamples first" task to your project plan, and note which small examples and special cases you plan to try.

## 5. Which fields use it

We list only fields our sources support:

- **Mathematics**: Thurston observed that mathematicians want not only to know that a theorem is true but also to understand its proof[^thurston1994proof-e2]. For field conventions, see the [mathematics field overview](../07_fields/mathematics/README.md).
- **Theoretical computer science**: proofs about algorithms are full of details (see Section 2), and the field has the Gödel Prize, awarded specifically for the best theory papers[^fortnow2009time-e8]. For concrete methods, see [Theoretical research](../07_fields/computer-science/practices/theoretical_research.md).
- **Formal methods in software engineering, systems and security**: formal models must be backed by proof[^shaw2003writing-e9]; software engineering review standards list theorems and complexity analysis as desirable attributes of engineering research[^ralph2020empirical-e88]; the seL4 kernel has a machine-checked proof from its abstract specification down to its C implementation[^klein2009sel4-e8].
- **Electrical engineering (signal processing)**: Vandewalle et al. see signal processing as sitting between theoretical and experimental science, with theorems often appearing alongside numerical simulations[^vandewalle2009reproducible-e12].
- **Philosophy**: it also uses deductive arguments[^pryor2025terms-e3], but because the premises are open to dispute, it falls mainly under the [Interpretation and argument](interpret_argue.md) strategy (see Section 3).

Our sources do not cover theoretical derivations and model proofs in physics, economics and similar fields.

## 6. Common mistakes

This table lists only mistakes at the level of the strategy. For mistakes in writing and checking proofs (hidden assumptions, a proof that "proves too much", an unused assumption, mistaking a sketch for a proof, and so on), see [Common mistakes in Theoretical research](../07_fields/computer-science/practices/theoretical_research.md#4-common-mistakes).

| Mistake | Why it is a problem |
|---|---|
| The statement you prove is not the question you actually care about (different definitions, a different model) | Aaronson lists "the authors don't understand the question" as a sign of a wrong breakthrough[^aaronson2008ten-e1]; the result looks valid but answers a different question `[Our analysis]` |
| Proving only that the implementation meets its specification, then claiming the system is "secure" | The proof does not guarantee that the specification describes the behavior users expect[^klein2009sel4-e2] |
| Strong assumptions or a weak conclusion that you don't own up to | Tao advises stating these openly[^taowriting-e4]; otherwise readers will assume your result applies more widely than it does `[Our analysis]` |
| The abstract says "we prove", and by the end it has become "this seems plausible" | The proof has quietly turned into a merely plausible argument; Aaronson lists "the authors themselves switch to weasel words by the end" as a warning sign[^aaronson2008ten-e4] |
| "Validating" a formal model with one or two examples | A formal model must be backed by rigorous derivation and proof[^shaw2003writing-e9] |
| Diving straight into a famous hard problem as a newcomer | Famous hard problems are almost never solved out of nowhere[^taocareer-e13] |

## 7. Further reading

- **[Theoretical research](../07_fields/computer-science/practices/theoretical_research.md)**: the full how-to for this strategy in computer science, from choosing a problem and making progress to writing proofs and checking yourself. Its further-reading list gives the original texts by Lamport, Tao and Aaronson.
- **[Mathematics field overview](../07_fields/mathematics/README.md)**: how mathematics works as a field; useful if you plan to publish in mathematics journals.
- **Thurston 1994, On proof and progress in mathematics**: how mathematicians actually understand, communicate and check proofs.
- **Klein et al. 2009, seL4: Formal Verification of an OS Kernel**: a complete formal verification project that spells out its assumptions, its costs and the bugs the proof found. Useful if you are considering a machine-checked proof.
- **[Interpretation and argument](interpret_argue.md)** and **[Philosophical argument](../07_fields/philosophy-ethics-religion/practices/philosophical_argument.md)**: read alongside this page to see how deductive argument works when the premises are open to dispute.

[^shaw2003writing-e9]: Shaw 2003, §4.1. [Evidence](../../sources/notes/shaw2003writing.md#e9)
[^shaw2003writing-e14]: Shaw 2003, §5. [Evidence](../../sources/notes/shaw2003writing.md#e14)
[^klein2009sel4-e1]: Klein et al. 2009, §1. [Evidence](../../sources/notes/klein2009sel4.md#e1)
[^klein2009sel4-e2]: Klein et al. 2009, §4.5. [Evidence](../../sources/notes/klein2009sel4.md#e2)
[^klein2009sel4-e3]: Klein et al. 2009, §4.5. [Evidence](../../sources/notes/klein2009sel4.md#e3)
[^klein2009sel4-e4]: Klein et al. 2009, Abstract and §5.2. [Evidence](../../sources/notes/klein2009sel4.md#e4)
[^klein2009sel4-e5]: Klein et al. 2009, §2.3. [Evidence](../../sources/notes/klein2009sel4.md#e5)
[^klein2009sel4-e6]: Klein et al. 2009, §5.2. [Evidence](../../sources/notes/klein2009sel4.md#e6)
[^klein2009sel4-e7]: Klein et al. 2009, §3.5. [Evidence](../../sources/notes/klein2009sel4.md#e7)
[^klein2009sel4-e8]: Klein et al. 2009, Abstract. [Evidence](../../sources/notes/klein2009sel4.md#e8)
[^lamport2012how-e1]: Lamport 2012, §1. [Evidence](../../sources/notes/lamport2012how.md#e1)
[^lamport2012how-e6]: Lamport 2012, §3, footnote 1. [Evidence](../../sources/notes/lamport2012how.md#e6)
[^lamport2012how-e8]: Lamport 2012, §4.5. [Evidence](../../sources/notes/lamport2012how.md#e8)
[^lamport2012how-e9]: Lamport 2012, §5. [Evidence](../../sources/notes/lamport2012how.md#e9)
[^lamport2012how-e10]: Lamport 2012, §5. [Evidence](../../sources/notes/lamport2012how.md#e10)
[^lamport2012how-e13]: Lamport 2012, §6. [Evidence](../../sources/notes/lamport2012how.md#e13)
[^lamport1995how-e1]: Lamport 1995, §1. [Evidence](../../sources/notes/lamport1995how.md#e1)
[^lamport1995how-e2]: Lamport 1995, §2.1. [Evidence](../../sources/notes/lamport1995how.md#e2)
[^lamport1995how-e5]: Lamport 1995, §4.2. [Evidence](../../sources/notes/lamport1995how.md#e5)
[^lamport1995how-e6]: Lamport 1995, §4.2. [Evidence](../../sources/notes/lamport1995how.md#e6)
[^taowriting-e3]: Tao, On writing: "Describe the results accurately". [Evidence](../../sources/notes/taowriting.md#e3)
[^taowriting-e4]: Tao, On writing: "Describe the results accurately". [Evidence](../../sources/notes/taowriting.md#e4)
[^taowriting-e8]: Tao, On writing: "Use good notation". [Evidence](../../sources/notes/taowriting.md#e8)
[^taowriting-e13]: Tao, On writing: "On local and global errors in mathematical papers". [Evidence](../../sources/notes/taowriting.md#e13)
[^taocareer-e1]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../sources/notes/taocareer.md#e1)
[^taocareer-e2]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../sources/notes/taocareer.md#e2)
[^taocareer-e5]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../sources/notes/taocareer.md#e5)
[^taocareer-e6]: Tao, Career advice: "On the importance of partial progress". [Evidence](../../sources/notes/taocareer.md#e6)
[^taocareer-e13]: Tao, Career advice: "Don't base career decisions on glamour or fame". [Evidence](../../sources/notes/taocareer.md#e13)
[^taocareer-e14]: Tao, Career advice: "Don't prematurely obsess on a single big problem or big theory". [Evidence](../../sources/notes/taocareer.md#e14)
[^taocareer-e16]: Tao, Career advice: "Learn and relearn your field". [Evidence](../../sources/notes/taocareer.md#e16)
[^taocareer-e18]: Tao, Career advice: "Write down what you've done". [Evidence](../../sources/notes/taocareer.md#e18)
[^taocareer-e22]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../sources/notes/taocareer.md#e22)
[^thurston1994proof-e2]: Thurston 1994, §1. [Evidence](../../sources/notes/thurston1994proof.md#e2)
[^thurston1994proof-e9]: Thurston 1994, §4. [Evidence](../../sources/notes/thurston1994proof.md#e9)
[^thurston1994proof-e10]: Thurston 1994, §4. [Evidence](../../sources/notes/thurston1994proof.md#e10)
[^thurston1994proof-e11]: Thurston 1994, §4. [Evidence](../../sources/notes/thurston1994proof.md#e11)
[^aaronson2008ten-e1]: Aaronson 2008, item 2. [Evidence](../../sources/notes/aaronson2008ten.md#e1)
[^aaronson2008ten-e3]: Aaronson 2008, item 4. [Evidence](../../sources/notes/aaronson2008ten.md#e3)
[^aaronson2008ten-e4]: Aaronson 2008, item 5. [Evidence](../../sources/notes/aaronson2008ten.md#e4)
[^ams2022ethical-e9]: AMS Ethical Guidelines, IV. Publications. [Evidence](../../sources/notes/ams2022ethical.md#e9)
[^amsculture2006rates-e1]: AMS 2006, para. 2. [Evidence](../../sources/notes/amsculture2006rates.md#e1)
[^stodden2013setting-e4]: Stodden et al. 2013 (ICERM report), Journals section. [Evidence](../../sources/notes/stodden2013setting.md#e4)
[^stodden2013setting-e5]: Stodden et al. 2013, Appendix C. [Evidence](../../sources/notes/stodden2013setting.md#e5)
[^ralph2020empirical-e88]: ACM SIGSOFT Empirical Standards, Engineering Research standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e88)
[^ralph2020empirical-e95]: ACM SIGSOFT Empirical Standards, Engineering Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e95)
[^vandewalle2009reproducible-e12]: Vandewalle et al. 2009, How to do reproducible research? — Components. [Evidence](../../sources/notes/vandewalle2009reproducible.md#e12)
[^pryor2025terms-e3]: Pryor, Philosophical Terms and Methods, Different Flavors of Argument. [Evidence](../../sources/notes/pryor2025terms.md#e3)
[^pryor2025terms-e12]: Pryor, Philosophical Terms and Methods, Conclusive or Not? [Evidence](../../sources/notes/pryor2025terms.md#e12)
[^cra1999evaluating-e4]: Patterson, Snyder & Ullman 1999 (Computing Research Association (CRA) memo), Structure of The Field. [Evidence](../../sources/notes/cra1999evaluating.md#e4)
[^fortnow2009time-e8]: Fortnow 2009, main text. [Evidence](../../sources/notes/fortnow2009time.md#e8)
