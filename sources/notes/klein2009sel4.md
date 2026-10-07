# Klein 等 2009：seL4: Formal Verification of an OS Kernel

- 资料：`klein2009sel4`，[原文](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf)
- 版本：SOSP 2009（第 22 届 ACM 操作系统原理研讨会）论文，SIGOPS 网站提供的 PDF，2026-10-07 读取。位置写节号。

### E1

- 位置：§1 Introduction
- 原文："We assume the correctness of the compiler, assembly code, boot code, management of caches, and the hardware; we prove everything else."
- 要点：seL4 的证明假设编译器、汇编代码、启动代码、缓存管理和硬件是正确的，其余部分都做了证明。

### E2

- 位置：§4.5 The proof
- 原文："A cynic might say that an implementation proof only shows that the implementation has precisely the same bugs that the specification contains. This is true: the proof does not guarantee that the specification describes the behaviour the user expects."
- 要点：实现正确性证明只说明实现符合规约；它不保证规约本身描述的就是用户期望的行为。

### E3

- 位置：§4.5 The proof
- 原文："This means the kernel can never crash or otherwise behave unexpectedly as long as our assumptions hold."
- 要点：证明的结论带着条件：只要假设成立，内核就不会崩溃或出现意外行为。

### E4

- 位置：Abstract；§5.2 Verification effort
- 原文："seL4, a third-generation microkernel of L4 provenance, comprises 8,700 lines of C code and 600 lines of assembler." / "The overall size of the proof, including framework, libraries, and generated proofs (not shown in the table) is 200,000 lines of Isabelle script." / "The cost of the proof is higher, in total about 20 py."
- 要点：seL4 有 8,700 行 C 代码和 600 行汇编；证明（含框架、库和生成的证明）共约 20 万行 Isabelle 脚本，总投入约 20 人年。

### E5

- 位置：§2.3 Formal verification
- 原文："Interactive theorem proving requires human intervention and creativity to construct and guide the proof. However, it has the advantage that it is not constrained to specific properties or finite, feasible state spaces, unlike more automated methods of verification such as static analysis or model checking."
- 要点：交互式定理证明需要人的介入和创造力；好处是不像静态分析、模型检测这类更自动的验证方法那样，受限于特定性质或有限的状态空间。

### E6

- 位置：§5.2 Verification effort
- 原文："Those two activities uncovered 16 defects in the implementation before verification had started in earnest, the formal verification has uncovered another 144 defects"
- 要点：正式验证开始前，内部使用和移植发现了 16 个缺陷；形式化验证又发现了 144 个。

### E7

- 位置：§3.5 Observations
- 原文："The requirements of verification force the designers to think of the simplest and cleanest way of achieving their goals. We found repeatedly that this leads to overall better design, which tends to reduce the likelihood of bugs."
- 要点：为了能被验证，设计者被迫寻找最简单、最清晰的实现方式；作者发现这往往带来更好的设计。

### E8

- 位置：Abstract
- 原文："We present our experience in performing the formal, machine-checked verification of the seL4 microkernel from an abstract specification down to its C implementation." / "Functional correctness means here that the implementation always strictly follows our high-level abstract specification of kernel behaviour."
- 要点：seL4 团队对内核做了从抽象规约一直到 C 实现的、机器检查的形式化验证；"功能正确"指实现始终严格符合高层的抽象规约。
