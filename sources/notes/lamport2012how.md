# Lamport 2012：How to Write a 21st Century Proof

- 资料：`lamport2012how`，[原文](https://lamport.azurewebsites.net/pubs/proof.pdf)
- 版本：作者主页公开的预印本（2011 年 11 月 23 日，2012 年 1 月 15 日小改），正式发表于 Journal of Fixed Point Theory and Applications 11 (2012)。位置写节号。

### E1

- 位置：§1 Introduction
- 原文："Making proofs easier to understand is easy. It requires only the simple application of two principles: structure and naming."
- 要点：让证明好懂只需两条原则：结构和命名。

### E2

- 位置：§1 Introduction
- 原文："Eliminating errors from proofs is not as easy. It takes precision and rigor, which require work. Structuring proofs makes it possible to avoid errors; hard work is needed to make it probable."
- 要点：消除证明中的错误需要精确、严谨和实打实的功夫；结构化让避免错误成为可能，但要靠下功夫才能让它大概率做到。

### E3

- 位置：§1 Introduction
- 原文："However, learning how to write a formal proof can teach how to write ordinary, informal ones."
- 要点：学会写形式化证明，能反过来教会你写普通的非形式化证明。

### E4

- 位置：§2 An Example
- 原文："The style requires that the last step of every proof be a statement of what it is that the proof is trying to prove--in this case, the statement of the corollary."
- 要点：结构化证明要求每个证明的最后一步就是"要证的命题本身"，这样不会出现证明了别的东西却没说明为什么推出结论的情况。

### E5

- 位置：§3 Hierarchical Structure
- 原文："The best way I know to eliminate errors is to imagine that there is a curious child sitting next to us. Every time we write an assertion, the child asks: Why?"
- 要点：想象身边坐着一个好奇的孩子，每写一个断言，他就问"为什么"。

### E6

- 位置：§3 Hierarchical Structure，脚注 1
- 原文："The astute reader will notice that this theorem assumes the unstated hypothesis a < b."
- 要点：连教材里的中值定理也带着一个没写出来的假设（a < b）；隐含假设很常见。

### E7

- 位置：§3 Hierarchical Structure
- 原文："The only way to avoid errors is to be ruthlessly suspicious of everything you believe."
- 要点：为自己写证明时，避免错误的唯一办法是对自己相信的一切都保持毫不留情的怀疑；否则"想确认自己是对的"的愿望会让你漏掉漏洞。

### E8

- 位置：§4.5 Completely Formal Proofs
- 原文："Formalizing mathematics is easy, but writing formal, machine-checkable proofs is not."
- 要点：把数学形式化不难，但写出能被机器检查的形式化证明并不容易；作者认为机器检查器还要几十年才能做到和写仔细的非形式化证明一样省力。

### E9

- 位置：§5 Experience
- 原文："A missing hypothesis, such as that a set must be nonempty, which is a trivial omission in a mathematical theorem, can mean a serious bug in an algorithm."
- 要点：在数学定理里无伤大雅的遗漏假设（如"集合非空"），放到算法里可能就是严重的缺陷。

### E10

- 位置：§5 Experience
- 原文："Proofs of algorithms are most often mathematically shallow but complicated, requiring many details to be checked."
- 要点：算法的证明往往数学上不深，但很繁杂，有大量细节要检查。

### E11

- 位置：§5 Experience
- 原文："Eliminating errors requires care. Structured proofs make it possible, not inevitable."
- 要点：结构化证明让消除错误成为可能，但不保证；仍然需要细心。

### E12

- 位置：§5 Experience（引用的审稿意见）
- 原文："For long proofs, I think that describing the idea of the proof in a few words at the beginning (if appropriate) would help make them more understandable."
- 要点：审稿人建议长证明开头先用几句话说明证明思路。

### E13

- 位置：§6 Objections to Structured Proof
- 原文："Proof sketches are fine, but they are not proofs."
- 要点：证明概要有用，但概要不是证明。

### E14

- 位置：§7 Beginning
- 原文："You can begin by just adding structure to an existing proof, as we did with Spivak's proof. Start by rewriting a simple proof and then try longer ones."
- 要点：入门办法：先把一个已有的简单证明改写成结构化形式，再逐步尝试更长的。
