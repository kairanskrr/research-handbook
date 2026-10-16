# Klein et al. 2009: seL4: Formal Verification of an OS Kernel

- Source: `klein2009sel4`, [original](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf)
- Version: Paper at SOSP 2009 (the 22nd ACM Symposium on Operating Systems Principles), PDF from the SIGOPS website, read 2026-10-07. Locations give section numbers.

### E1

- Location: §1 Introduction
- Quote: "We assume the correctness of the compiler, assembly code, boot code, management of caches, and the hardware; we prove everything else."
- Key point: The seL4 proof assumes the correctness of the compiler, assembly code, boot code, cache management, and hardware; everything else is proved.

### E2

- Location: §4.5 The proof
- Quote: "A cynic might say that an implementation proof only shows that the implementation has precisely the same bugs that the specification contains. This is true: the proof does not guarantee that the specification describes the behaviour the user expects."
- Key point: An implementation correctness proof only shows that the implementation matches the specification; it does not guarantee that the specification describes the behavior users expect.

### E3

- Location: §4.5 The proof
- Quote: "This means the kernel can never crash or otherwise behave unexpectedly as long as our assumptions hold."
- Key point: The proof's conclusion is conditional: as long as the assumptions hold, the kernel can never crash or behave unexpectedly.

### E4

- Location: Abstract; §5.2 Verification effort
- Quote: "seL4, a third-generation microkernel of L4 provenance, comprises 8,700 lines of C code and 600 lines of assembler." / "The overall size of the proof, including framework, libraries, and generated proofs (not shown in the table) is 200,000 lines of Isabelle script." / "The cost of the proof is higher, in total about 20 py."
- Key point: seL4 has 8,700 lines of C and 600 lines of assembler; the proof (including framework, libraries, and generated proofs) is about 200,000 lines of Isabelle script, with a total effort of about 20 person-years.

### E5

- Location: §2.3 Formal verification
- Quote: "Interactive theorem proving requires human intervention and creativity to construct and guide the proof. However, it has the advantage that it is not constrained to specific properties or finite, feasible state spaces, unlike more automated methods of verification such as static analysis or model checking."
- Key point: Interactive theorem proving needs human intervention and creativity; in return, unlike more automated verification such as static analysis or model checking, it is not limited to specific properties or finite state spaces.

### E6

- Location: §5.2 Verification effort
- Quote: "Those two activities uncovered 16 defects in the implementation before verification had started in earnest, the formal verification has uncovered another 144 defects"
- Key point: Before formal verification started in earnest, internal use and porting found 16 defects; formal verification then found another 144.

### E7

- Location: §3.5 Observations
- Quote: "The requirements of verification force the designers to think of the simplest and cleanest way of achieving their goals. We found repeatedly that this leads to overall better design, which tends to reduce the likelihood of bugs."
- Key point: The requirements of verification force designers to find the simplest and cleanest way to reach their goals; the authors found repeatedly that this leads to better overall design.

### E8

- Location: Abstract
- Quote: "We present our experience in performing the formal, machine-checked verification of the seL4 microkernel from an abstract specification down to its C implementation." / "Functional correctness means here that the implementation always strictly follows our high-level abstract specification of kernel behaviour."
- Key point: The seL4 team performed formal, machine-checked verification of the kernel from an abstract specification down to its C implementation; "functional correctness" means the implementation always strictly follows the high-level abstract specification.
