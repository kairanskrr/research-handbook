# Theoretical research: proofs and formal analysis

This page is about **research whose main results are theorems and proofs**: for example, proving an upper or lower bound on an algorithm's complexity, proving that a protocol is secure under some adversary model, or using formal methods to prove that a system satisfies some property.

**Scope**: this is how theoretical computer science works, and also the formal side of software engineering, systems, and security. It belongs to the [Proof](../../../05_research-strategies/prove.md) research strategy. The general questions (what kind of knowledge a proof produces; what evidence reviewers expect to see: all assumptions stated, a complete proof that others can check, whether it needs machine checking, how far the assumptions are from reality) are covered on the strategy page. This page covers how, in computer science, you choose a problem, make progress, and write and check a proof.

If your main result is a system or tool you built, with experiments showing that it works, see [Engineering research](engineering_research.md). If you compare many methods' performance on the same tasks, see [Benchmarking](benchmarking.md). Many papers do both: use this page for the proof part, and [Building and improving](../../../05_research-strategies/build_improve.md) for the experimental part.

**What this page rests on**: the ACM SIGSOFT Empirical Standards (the review standards for research in software engineering, from the Association for Computing Machinery Special Interest Group on Software Engineering) are written for empirical research and **have no standard for theoretical research**. The practices and checklist on this page are compiled from essays by Lamport, Tao, Aaronson, and others. Much of Tao's and Lamport's advice is written for mathematicians and applies to any work whose result is a proof; it is marked *(all proof-based work)*. Practices that hold only in computer science are marked *(computer science)*.

**After reading this page, you should be able to:**

- Say what theoretical research produces and how it differs from engineering research and benchmarking;
- Pick a suitable problem, and confirm that it really is unsolved and that you are using the right definitions;
- Use a handful of standard moves to make progress when a proof is stuck;
- Write a proof in a form that others (and you) can check step by step, and find your own mistakes before you submit.

---

## 1. What this research is and when to use it

Theoretical research produces **conclusions that hold in every case satisfying the assumptions**, not "on the data we measured". Results usually fall into four kinds (our own grouping):

| Result | Example | Question it answers |
|---|---|---|
| Upper bound (algorithms and analysis) | An algorithm's worst-case running time is at most O(n log n) | How well can we do? |
| Lower bound, impossibility result | Any comparison-based sort needs about n log n comparisons in the worst case | What is the best anyone can do? What is fundamentally impossible? |
| Model or definition | A new model of computation, or a new security definition | What concepts should we use to describe this problem? |
| Formal guarantee | A protocol satisfies confidentiality under some adversary model; a machine-checked proof that an algorithm is correct | Under explicit assumptions, is a system guaranteed to have some property? |

How it differs from related kinds of research:

| | Theoretical research | Engineering research | Benchmarking |
|---|---|---|---|
| Main evidence | Proof | A built system + experiments | Measurements on shared tasks |
| Scope of the conclusion | Every case that satisfies the assumptions | The cases the experiments cover | The cases the benchmark covers |
| Biggest risk | The proof is wrong; the model or assumptions are too far from reality | Unfair or irreproducible experiments | The benchmark does not represent real use |

**When to use it**: when your question is "can it be done?", "what is the most / least it takes?", or "does this always hold?", answer it with a proof.

*(Computer science)* Proofs about algorithms have their own character. Leslie Lamport (a researcher in distributed systems and formal methods) points out that proofs about algorithms are often mathematically shallow but complicated, with lots of details to check[^lamport2012how-e10]. A missing assumption that is harmless in a mathematical theorem (say, "the set is nonempty") can be a serious bug in an algorithm[^lamport2012how-e9].

---

## 2. How to do it

### Step 1: Choose a problem, and confirm it is still open and your definitions are right *(all proof-based work)*

**How:**

1. **Start with problems you can actually solve; don't throw yourself at a famous hard problem right away.** Terence Tao (a mathematician) notes that famous problems are almost never solved out of nowhere[^taocareer-e13]. He advises spending most of your time on more tractable "low-hanging fruit", building up experience, skill, and reputation, and taking on more ambitious projects once you are ready[^taocareer-e14]. Richard Hamming (a mathematician at Bell Labs) put it this way: a problem is important not because the result would be big, but because you have a reasonable attack on it[^hamming1986you-e2]. General advice on choosing a problem is in [Generating candidate problems](../../../01_find-a-problem/02_generate-problems.md).
2. **Confirm the problem is still open.** Find the key papers on the problem and look at which later papers cite them[^taocareer-e16], to see whether anyone has already solved, improved, or refuted it. Also look for related **lower bounds and impossibility results**: a claimed result that conflicts with a known impossibility result without mentioning it is a classic sign of a bogus "breakthrough"[^aaronson2008ten-e3]. If you are unsure, ask your advisor or an expert in the area. For how to search the literature, see [Reading papers and surveying the literature](../../../01_find-a-problem/01_enter-a-field.md).
3. **Confirm your definitions are the ones everyone else uses.** Write down the precise problem statement and compare it word by word with the standard literature: the model of computation, how input size is measured, what the adversary can do, what "secure" means. Keep your notation as close to the existing literature as you can, too[^taowriting-e8].

**Where people go wrong:** misunderstanding the problem itself. Scott Aaronson (a theoretical computer scientist) lists "the authors don't understand the question" as one of the signs of a bogus breakthrough[^aaronson2008ten-e1]. More often, your definition is slightly off from the standard one: you have proved a weaker or different statement without noticing.

### Step 2: Make progress on the proof *(all proof-based work)*

When you get stuck, try these in order:

- **Look at examples and special cases first.** One step in the process Tao describes is isolating a "toy model" (a simplified special case) of the big problem[^taocareer-e5]. Keep a stock of counterexamples and easy-to-analyze model cases at hand, and know which obstacles your tools can handle and which are hopeless[^taocareer-e9].
- **Try to disprove it.** If you want to prove a bold statement, look for a counterexample first. If you find one, you save a lot of time, and the counterexample itself may be publishable; if you don't, the obstacles you hit tell you how the proof has to go[^taocareer-e2].
- **Change the problem.** What happens if you drop an assumption? Can the conclusion be strengthened?[^taocareer-e8] For each lemma you plan to use, understand why each of its assumptions is needed[^taocareer-e17].
- **Look for similar known results.** When a special case looks like a problem from another area, read that problem's literature and ask experts in that area[^taocareer-e21].
- **Value partial progress.** A method that solves only part of the problem is not a failure[^taocareer-e6]; even when a method is doomed, exactly where it breaks down is very instructive[^taocareer-e7]. Many intermediate steps are publishable papers in their own right[^taocareer-e22].
- **Write your arguments down, including the failed ones.** Write up interesting arguments as drafts, detailed enough that you can reconstruct them later[^taocareer-e18]. Keep a private archive even of embarrassingly wrong attempts; you may be able to salvage something from them later[^taocareer-e19]. For keeping a research log, see [Running and iterating](../../../02_do-the-project/06_run-and-iterate.md).

### Step 3: Write the proof so it can be checked *(all proof-based work)*

**Define, then state, then prove.**

- Define notation used throughout the paper together, near the start; define notation used only locally close to where it is used[^taowriting-e9].
- An expression is worth its own notation only if you use it three or more times; one used once usually doesn't need any[^taowriting-e7]. Avoid fancy notation[^taowriting-e10].
- Key terms must be defined precisely[^taowriting-e11]. Otherwise an expression can have two readings, the argument uses one early on and the other later, and the error becomes very hard to pin to a single step.

**State every assumption.** Even theorems in textbooks carry unstated assumptions[^lamport2012how-e6]. A lemma is a good moment to restate all the current assumptions and notation[^taowriting-e2]. If you say each time you use an assumption, then when you later need to weaken one, a search shows you everywhere it was used[^lamport1995how-e4].

**Use structured proofs.** Lamport's method rests on two principles: structure and naming[^lamport2012how-e1]. Write the proof as numbered steps, each with its own proof underneath, which can in turn be broken into further levels; the last step of every proof asserts the statement being proved[^lamport2012how-e4]. A sketch (format modeled on Lamport's; the last step is written Q.E.D.):

```
THEOREM: (full statement, including every assumption)
PROOF SKETCH: (two or three sentences on the idea)
<1>1. (first intermediate result)
  PROOF: (the reason, or split further into <2>1, <2>2, ...)
<1>2. (second intermediate result)
  PROOF: By <1>1 and Lemma 3.
<1>3. Q.E.D.
  PROOF: By <1>1, <1>2.
```

- **How far to expand**: expand until every statement at the lowest level is obvious, then expand one more level[^lamport1995how-e6]. Most errors come from proofs that were not expanded to enough levels[^lamport1995how-e5].
- **Don't accept "this case is similar to the previous one."** Find a general step that handles both cases at once[^lamport1995how-e7].
- **Break long proofs into lemmas**, and state each lemma so it is easy to use, not easy to prove[^taowriting-e1].
- **Write the skeleton first.** Write (rough) statements of all the key definitions and theorems first, with only sketchy notes for the proofs; fill in the details once the structure is settled[^taowriting-e16].
- **Flag unproved claims.** When you assert a nontrivial statement without proof or citation, tell the reader explicitly[^taowriting-e5].

A way to start: take an existing short proof, rewrite it in structured form, then gradually try longer ones[^lamport2012how-e14].

### Step 4: Check your own proof *(all proof-based work; the machine-checking part is computer science)*

**Start by accepting that your proof is probably wrong.** Lamport cites an anecdotal claim that as many as a third of the papers in mathematics journals contain errors: not minor slips, but incorrect theorems and proofs[^lamport1995how-e1] (this is anecdote, not a statistic). When he rewrote a proof from Kelley's textbook in structured form, he found on the fifth page that Kelley's original proof was wrong[^lamport1995how-e3]. When you check a proof for yourself, the only way is to be ruthlessly skeptical of everything you believe[^lamport2012how-e7].

**Global checks: before looking at details, ask whether the whole thing is suspicious.** A global refutation shows that if the proof were correct, it would imply something known or very likely to be false[^taowriting-e12]. Some questions to ask:

- Would the same method also "prove" a stronger statement that is known to be false? If so, the method has a hole[^taocareer-e1]. For example, an argument that "3SAT needs exponential time" is certainly wrong if it would work just as well for 2SAT, which has a polynomial-time algorithm[^aaronson2008ten-e2].
- Does the proof make real use of every key assumption? An unused assumption is a red flag[^taowriting-e13].
- For a proof by contradiction: run it again without the assumption "suppose the conclusion is false". If you still reach a contradiction, the error is in the argument itself[^taocareer-e3].
- Have you just added a small twist "nobody thought of" to the method the experts routinely use? Tao lists this as a warning sign[^taocareer-e4].

When hunting for errors, intuition and non-rigorous reasoning are perfectly fine; rigor is required when you build the proof[^taowriting-e15].

**Local checks: go through it step by step.** Imagine a curious child sitting next to you who asks "why?" after every assertion[^lamport2012how-e5]. A test of whether you really understand it: can you explain the argument clearly to a fellow student?[^taocareer-e20] Rereading it a few days later, or having a labmate or your advisor read it, are other ways to get a fresh pair of eyes. Structure by itself does not guarantee there are no errors; you still have to be careful[^lamport2012how-e11].

**Make the proof robust to local errors.** Organize the proof so that an error in one step doesn't bring down the whole thing and still leaves a valuable partial result[^taowriting-e14].

***(Computer science)* When to use a proof assistant (software that checks a formal proof step by step, such as TLAPS, the proof system for TLA+).** Formalizing mathematics is not hard, but writing proofs a machine can check is not easy[^lamport2012how-e8]. So it is not something every paper needs. It pays off most for proofs with many details, where one missing assumption becomes a bug, such as concurrent algorithms, protocols, and system correctness, based on [^lamport2012how-e10][^lamport2012how-e9]. Even if you never use one, learning to write formal proofs teaches you to write ordinary proofs[^lamport2012how-e3].

### Step 5: Give both intuition and formality *(all proof-based work)*

The point of rigor is not to destroy intuition but to destroy bad intuition and sharpen good intuition[^taocareer-e11]; formality handles the details, intuition handles the big picture, and you need both[^taocareer-e12]. When writing the paper:

- **Put a sketch before each main proof**, as a "road map" for the reader[^lamport1995how-e2]. Start a long proof with a few sentences explaining the idea; a reviewer Lamport quotes made exactly this suggestion[^lamport2012how-e12]. But a sketch is not a proof[^lamport2012how-e13].
- **Can you say in high-level terms why the argument works?** If you can't, that is a red flag[^taocareer-e15].
- **Vary the level of detail**: explain new and key parts at more length in words; keep routine parts short[^taowriting-e6].
- **Describe the results accurately**: neither undersell nor oversell them[^taowriting-e3]; say openly where assumptions are stronger, or conclusions weaker, than one would like[^taowriting-e4]; discuss the known limitations of the tools you use[^taocareer-e10].

> **Where sources disagree: how detailed should a proof be?**
> - **Lamport**: expand until it's obvious, then one more level[^lamport1995how-e6]; structured proofs are longer mainly because they contain more detail[^lamport1995how-e9]. He suggests preparing two versions: a detailed one for yourself, reviewers, and interested colleagues, and a shorter one for publication[^lamport1995how-e8].
> - **Tao**: a paper should spend more words on the most important and novel parts and keep the routine, standard parts brief[^taowriting-e6].
>
> The two don't conflict: **write it out in full detail when checking for yourself; vary the detail when writing for readers.** Computer science conference papers have page limits, and the usual practice is to give the key proofs and sketches in the main text and put full proofs in an appendix or in a full version on a preprint server.

### Step 6: Submitting: conferences and journals *(computer science)*

In computer science, conferences are the main publication venue. Theory also values conferences, but has a long tradition of completing and extending conference papers and then submitting them to journals[^cra1999evaluating-e4]. For the overall picture, see the [field overview](../README.md). A few reminders:

- The conference version has limited space, so the full proofs need somewhere to live (an appendix or a full version) where reviewers can find them if they need to;
- A journal version is not just more pages: it completes and corrects the proofs that were omitted or compressed in the conference version;
- Don't take a single rejection too hard: nearly half of Gödel Prize-winning papers (the Gödel Prize is a top award for papers in theoretical computer science) were originally rejected by the top theory conferences or never appeared there at all[^fortnow2009time-e8].

---

## 3. Checklist

The SIGSOFT Empirical Standards have no standard for theoretical research; the checklist below is compiled from this page's sources.

**Must do**

- [ ] Every theorem is stated in full, with all assumptions written out[^lamport2012how-e6][^taowriting-e2]
- [ ] Definitions, models, and notation match the versions standard in the field; any differences are stated explicitly[^taowriting-e8]
- [ ] You have checked related known results, especially lower bounds and impossibility results, and explained how your result relates to them[^aaronson2008ten-e3][^aaronson2008ten-e5]
- [ ] Every non-obvious step is justified; claims made without proof are clearly flagged[^taowriting-e5]
- [ ] You have done global checks: the proof doesn't "incidentally" imply something known to be false, and every key assumption is used[^taocareer-e1][^taowriting-e13]
- [ ] Results are described accurately, with limitations stated[^taowriting-e3][^taowriting-e4]

**Better practice**

- [ ] Structured proofs, with a sketch before each main proof[^lamport2012how-e1][^lamport1995how-e2]
- [ ] Examples or counterexamples show why the key assumptions are needed[^taocareer-e17]
- [ ] The detailed version of the proofs is public (appendix or full version)[^lamport1995how-e8]
- [ ] For proofs with many details and a high cost of error, you have considered checking them with a proof assistant[^lamport2012how-e10]

**Fine to skip; not a flaw**

- Not every proof needs machine checking; writing machine-checkable proofs is very costly[^lamport2012how-e8].
- You don't have to solve the whole problem at once: special cases, partial results, and counterexamples can all be publishable in their own right[^taocareer-e22][^taocareer-e2].
- A purely theoretical result (a lower bound, for example) doesn't need experiments.

**Common but invalid reviewer criticisms**

- "The proof is too long": if it is long because the details are filled in, that is the price of rigor, not a flaw[^lamport1995how-e9]. (But "too long" can also be a sign of unclear structure, which is worth checking.)
- "No experimental validation": not a valid criticism of a purely theoretical result.

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Proving a different statement from the one you need (a slightly different definition, a different model) | The result looks right but doesn't answer the original question[^aaronson2008ten-e1] |
| Leaving implicit assumptions unstated | In an algorithm, one missing assumption can be a serious bug[^lamport2012how-e9] |
| The proof "proves too much": the same argument also yields something known to be false | It shows the argument has a hole[^aaronson2008ten-e2][^taocareer-e1] |
| A key assumption is never used anywhere | A sign of a global error[^taowriting-e13] |
| Writing "this case is similar and is omitted" | Lamport considers this unacceptable; find a general step that handles both cases at once[^lamport1995how-e7] |
| Treating a proof sketch as a proof | A sketch explains the idea but can't replace the step-by-step argument[^lamport2012how-e13] |
| Too much notation, or notation that is too fancy | Tao advises introducing notation only for expressions you use repeatedly, and avoiding fancy notation[^taowriting-e7][^taowriting-e10]; otherwise readers keep flipping back to look things up |
| The abstract says "we prove", but by the end it has become "this appears to work" | The proof has degraded into a "plausible argument", a classic sign of an error[^aaronson2008ten-e4] |
| A newcomer goes straight for a famous hard problem | Hardly any hard problem is solved out of nowhere[^taocareer-e13]; it is easy to go a long time with nothing to show |

---

## 5. Further reading

- **Lamport 1995, How to Write a Proof**: short; explains how to write structured proofs and the rule "expand until obvious, then one more level". Good for anyone writing a long proof seriously for the first time.
- **Lamport 2012, How to Write a 21st Century Proof**: an updated version of structured proofs, with the author's twenty years of experience and an example of a machine-checked proof. Good if you want to learn about proof assistants.
- **Tao's Career advice and On writing pages**: one piece of advice per page, each very short. "Be sceptical of your own work" and "On the importance of partial progress" cover making progress and checking yourself; "Use good notation", "Create lemmas", and "On local and global errors" cover writing and finding errors.
- **Aaronson 2008, Ten Signs a Claimed Mathematical Breakthrough is Wrong**: ten warning signs from the perspective of theoretical computer science. Good as a self-check before submitting; the author stresses that these are only heuristics: failing one doesn't mean a result is wrong, and passing them all doesn't mean it is right[^aaronson2008ten-e6].
- **Hamming 1986, You and Your Research**: on choosing problems that are important and that you have a way to attack; see [Generating candidate problems](../../../01_find-a-problem/02_generate-problems.md).

[^lamport2012how-e1]: Lamport 2012, §1. [Evidence](../../../../sources/notes/lamport2012how.md#e1)
[^lamport2012how-e3]: Lamport 2012, §1. [Evidence](../../../../sources/notes/lamport2012how.md#e3)
[^lamport2012how-e4]: Lamport 2012, §2. [Evidence](../../../../sources/notes/lamport2012how.md#e4)
[^lamport2012how-e5]: Lamport 2012, §3. [Evidence](../../../../sources/notes/lamport2012how.md#e5)
[^lamport2012how-e6]: Lamport 2012, §3, footnote 1. [Evidence](../../../../sources/notes/lamport2012how.md#e6)
[^lamport2012how-e7]: Lamport 2012, §3. [Evidence](../../../../sources/notes/lamport2012how.md#e7)
[^lamport2012how-e8]: Lamport 2012, §4.5. [Evidence](../../../../sources/notes/lamport2012how.md#e8)
[^lamport2012how-e9]: Lamport 2012, §5. [Evidence](../../../../sources/notes/lamport2012how.md#e9)
[^lamport2012how-e10]: Lamport 2012, §5. [Evidence](../../../../sources/notes/lamport2012how.md#e10)
[^lamport2012how-e11]: Lamport 2012, §5. [Evidence](../../../../sources/notes/lamport2012how.md#e11)
[^lamport2012how-e12]: Lamport 2012, §5 (quoted review). [Evidence](../../../../sources/notes/lamport2012how.md#e12)
[^lamport2012how-e13]: Lamport 2012, §6. [Evidence](../../../../sources/notes/lamport2012how.md#e13)
[^lamport2012how-e14]: Lamport 2012, §7. [Evidence](../../../../sources/notes/lamport2012how.md#e14)
[^lamport1995how-e1]: Lamport 1995, §1. [Evidence](../../../../sources/notes/lamport1995how.md#e1)
[^lamport1995how-e2]: Lamport 1995, §2.1. [Evidence](../../../../sources/notes/lamport1995how.md#e2)
[^lamport1995how-e3]: Lamport 1995, §4.1. [Evidence](../../../../sources/notes/lamport1995how.md#e3)
[^lamport1995how-e4]: Lamport 1995, §4.1. [Evidence](../../../../sources/notes/lamport1995how.md#e4)
[^lamport1995how-e5]: Lamport 1995, §4.2. [Evidence](../../../../sources/notes/lamport1995how.md#e5)
[^lamport1995how-e6]: Lamport 1995, §4.2. [Evidence](../../../../sources/notes/lamport1995how.md#e6)
[^lamport1995how-e7]: Lamport 1995, §4.2. [Evidence](../../../../sources/notes/lamport1995how.md#e7)
[^lamport1995how-e8]: Lamport 1995, §4.2. [Evidence](../../../../sources/notes/lamport1995how.md#e8)
[^lamport1995how-e9]: Lamport 1995, §4.2. [Evidence](../../../../sources/notes/lamport1995how.md#e9)
[^taocareer-e1]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e1)
[^taocareer-e2]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e2)
[^taocareer-e3]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e3)
[^taocareer-e4]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e4)
[^taocareer-e5]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e5)
[^taocareer-e6]: Tao, Career advice: "On the importance of partial progress". [Evidence](../../../../sources/notes/taocareer.md#e6)
[^taocareer-e7]: Tao, Career advice: "On the importance of partial progress". [Evidence](../../../../sources/notes/taocareer.md#e7)
[^taocareer-e8]: Tao, Career advice: "Ask yourself dumb questions". [Evidence](../../../../sources/notes/taocareer.md#e8)
[^taocareer-e9]: Tao, Career advice: "Learn the limitations of your tools". [Evidence](../../../../sources/notes/taocareer.md#e9)
[^taocareer-e10]: Tao, Career advice: "Learn the limitations of your tools". [Evidence](../../../../sources/notes/taocareer.md#e10)
[^taocareer-e11]: Tao, Career advice: "There's more to mathematics than rigour and proofs". [Evidence](../../../../sources/notes/taocareer.md#e11)
[^taocareer-e12]: Tao, Career advice: "There's more to mathematics than rigour and proofs". [Evidence](../../../../sources/notes/taocareer.md#e12)
[^taocareer-e13]: Tao, Career advice: "Don't base career decisions on glamour or fame". [Evidence](../../../../sources/notes/taocareer.md#e13)
[^taocareer-e14]: Tao, Career advice: "Don't prematurely obsess on a single big problem or big theory". [Evidence](../../../../sources/notes/taocareer.md#e14)
[^taocareer-e15]: Tao, Career advice: "Don't prematurely obsess on a single big problem or big theory", Appendix. [Evidence](../../../../sources/notes/taocareer.md#e15)
[^taocareer-e16]: Tao, Career advice: "Learn and relearn your field". [Evidence](../../../../sources/notes/taocareer.md#e16)
[^taocareer-e17]: Tao, Career advice: "Learn and relearn your field". [Evidence](../../../../sources/notes/taocareer.md#e17)
[^taocareer-e18]: Tao, Career advice: "Write down what you've done". [Evidence](../../../../sources/notes/taocareer.md#e18)
[^taocareer-e19]: Tao, Career advice: "Use the wastebasket". [Evidence](../../../../sources/notes/taocareer.md#e19)
[^taocareer-e20]: Tao, Career advice: "Solving mathematical problems". [Evidence](../../../../sources/notes/taocareer.md#e20)
[^taocareer-e21]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e21)
[^taocareer-e22]: Tao, Career advice: "Be sceptical of your own work". [Evidence](../../../../sources/notes/taocareer.md#e22)
[^taowriting-e1]: Tao, On writing: "Create lemmas". [Evidence](../../../../sources/notes/taowriting.md#e1)
[^taowriting-e2]: Tao, On writing: "Create lemmas". [Evidence](../../../../sources/notes/taowriting.md#e2)
[^taowriting-e3]: Tao, On writing: "Describe the results accurately". [Evidence](../../../../sources/notes/taowriting.md#e3)
[^taowriting-e4]: Tao, On writing: "Describe the results accurately". [Evidence](../../../../sources/notes/taowriting.md#e4)
[^taowriting-e5]: Tao, On writing: "Describe the results accurately". [Evidence](../../../../sources/notes/taowriting.md#e5)
[^taowriting-e6]: Tao, On writing: "Give appropriate amounts of detail". [Evidence](../../../../sources/notes/taowriting.md#e6)
[^taowriting-e7]: Tao, On writing: "Use good notation". [Evidence](../../../../sources/notes/taowriting.md#e7)
[^taowriting-e8]: Tao, On writing: "Use good notation". [Evidence](../../../../sources/notes/taowriting.md#e8)
[^taowriting-e9]: Tao, On writing: "Use good notation". [Evidence](../../../../sources/notes/taowriting.md#e9)
[^taowriting-e10]: Tao, On writing: "Use good notation". [Evidence](../../../../sources/notes/taowriting.md#e10)
[^taowriting-e11]: Tao, On writing: "On local and global errors in mathematical papers". [Evidence](../../../../sources/notes/taowriting.md#e11)
[^taowriting-e12]: Tao, On writing: "On local and global errors in mathematical papers". [Evidence](../../../../sources/notes/taowriting.md#e12)
[^taowriting-e13]: Tao, On writing: "On local and global errors in mathematical papers". [Evidence](../../../../sources/notes/taowriting.md#e13)
[^taowriting-e14]: Tao, On writing: "On local and global errors in mathematical papers". [Evidence](../../../../sources/notes/taowriting.md#e14)
[^taowriting-e15]: Tao, On writing: "On local and global errors in mathematical papers". [Evidence](../../../../sources/notes/taowriting.md#e15)
[^taowriting-e16]: Tao, On writing: "Write a rapid prototype first". [Evidence](../../../../sources/notes/taowriting.md#e16)
[^aaronson2008ten-e1]: Aaronson 2008, item 2. [Evidence](../../../../sources/notes/aaronson2008ten.md#e1)
[^aaronson2008ten-e2]: Aaronson 2008, item 3. [Evidence](../../../../sources/notes/aaronson2008ten.md#e2)
[^aaronson2008ten-e3]: Aaronson 2008, item 4. [Evidence](../../../../sources/notes/aaronson2008ten.md#e3)
[^aaronson2008ten-e4]: Aaronson 2008, item 5. [Evidence](../../../../sources/notes/aaronson2008ten.md#e4)
[^aaronson2008ten-e5]: Aaronson 2008, item 7. [Evidence](../../../../sources/notes/aaronson2008ten.md#e5)
[^aaronson2008ten-e6]: Aaronson 2008, ending. [Evidence](../../../../sources/notes/aaronson2008ten.md#e6)
[^hamming1986you-e2]: Hamming 1986, "important problems" paragraph. [Evidence](../../../../sources/notes/hamming1986you.md#e2)
[^cra1999evaluating-e4]: Patterson, Snyder & Ullman 1999 (Computing Research Association (CRA) memo), Structure of The Field. [Evidence](../../../../sources/notes/cra1999evaluating.md#e4)
[^fortnow2009time-e8]: Fortnow 2009, main text. [Evidence](../../../../sources/notes/fortnow2009time.md#e8)
