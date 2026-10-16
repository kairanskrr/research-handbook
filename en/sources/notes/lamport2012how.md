# Lamport 2012: How to Write a 21st Century Proof

- Source: `lamport2012how`, [full text](https://lamport.azurewebsites.net/pubs/proof.pdf)
- Version: preprint posted on the author's website (November 23, 2011, minor changes January 15, 2012); formally published in Journal of Fixed Point Theory and Applications 11 (2012). Locations give the section number.

### E1

- Location: §1 Introduction
- Quote: "Making proofs easier to understand is easy. It requires only the simple application of two principles: structure and naming."
- Key point: Making proofs easier to understand requires only two principles: structure and naming.

### E2

- Location: §1 Introduction
- Quote: "Eliminating errors from proofs is not as easy. It takes precision and rigor, which require work. Structuring proofs makes it possible to avoid errors; hard work is needed to make it probable."
- Key point: Eliminating errors from proofs takes precision, rigor, and real work; structuring makes it possible to avoid errors, but hard work is what makes that likely.

### E3

- Location: §1 Introduction
- Quote: "However, learning how to write a formal proof can teach how to write ordinary, informal ones."
- Key point: Learning how to write a formal proof can teach you how to write ordinary, informal ones.

### E4

- Location: §2 An Example
- Quote: "The style requires that the last step of every proof be a statement of what it is that the proof is trying to prove--in this case, the statement of the corollary."
- Key point: Structured proofs require the last step of every proof to be a statement of what the proof is trying to prove, so you cannot prove something else without saying why it yields the conclusion.

### E5

- Location: §3 Hierarchical Structure
- Quote: "The best way I know to eliminate errors is to imagine that there is a curious child sitting next to us. Every time we write an assertion, the child asks: Why?"
- Key point: Imagine a curious child sitting next to you; every time you write an assertion, the child asks "why?"

### E6

- Location: §3 Hierarchical Structure, footnote 1
- Quote: "The astute reader will notice that this theorem assumes the unstated hypothesis a < b."
- Key point: Even the textbook mean value theorem carries an unstated hypothesis (a < b); hidden assumptions are common.

### E7

- Location: §3 Hierarchical Structure
- Quote: "The only way to avoid errors is to be ruthlessly suspicious of everything you believe."
- Key point: When writing a proof for yourself, the only way to avoid errors is to be ruthlessly suspicious of everything you believe; otherwise the wish to be right will make you miss the gaps.

### E8

- Location: §4.5 Completely Formal Proofs
- Quote: "Formalizing mathematics is easy, but writing formal, machine-checkable proofs is not."
- Key point: Formalizing mathematics is easy, but writing formal, machine-checkable proofs is not; the author thinks it will be decades before machine checkers make this as easy as writing a careful informal proof.

### E9

- Location: §5 Experience
- Quote: "A missing hypothesis, such as that a set must be nonempty, which is a trivial omission in a mathematical theorem, can mean a serious bug in an algorithm."
- Key point: A missing hypothesis (e.g., that a set must be nonempty) that is a trivial omission in a mathematical theorem can mean a serious bug in an algorithm.

### E10

- Location: §5 Experience
- Quote: "Proofs of algorithms are most often mathematically shallow but complicated, requiring many details to be checked."
- Key point: Proofs of algorithms are usually mathematically shallow but complicated, with many details to check.

### E11

- Location: §5 Experience
- Quote: "Eliminating errors requires care. Structured proofs make it possible, not inevitable."
- Key point: Structured proofs make eliminating errors possible, not inevitable; it still takes care.

### E12

- Location: §5 Experience (a quoted referee report)
- Quote: "For long proofs, I think that describing the idea of the proof in a few words at the beginning (if appropriate) would help make them more understandable."
- Key point: A referee suggests describing the idea of a long proof in a few words at the beginning.

### E13

- Location: §6 Objections to Structured Proof
- Quote: "Proof sketches are fine, but they are not proofs."
- Key point: Proof sketches are fine, but they are not proofs.

### E14

- Location: §7 Beginning
- Quote: "You can begin by just adding structure to an existing proof, as we did with Spivak's proof. Start by rewriting a simple proof and then try longer ones."
- Key point: How to start: rewrite a simple existing proof in structured form, then try longer ones.
