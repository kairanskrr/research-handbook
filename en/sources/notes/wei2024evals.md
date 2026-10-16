# Jason Wei 2024: Successful language model evals

- Source: `wei2024evals`, [original](https://www.jasonwei.net/blog/evals)
- Version: Blog post, May 24, 2024; accessed 2026-10-05.
- Note: The author is a large language model researcher who sums up, as both a user and a builder, what makes an evaluation benchmark (eval) succeed. The content is about evaluating large language models.

### E1

- Location: Paragraph 1
- Quote: "Evals are incentives for the research community, and breakthroughs are often closely linked to a huge performance jump on some eval."
- Key point: Evals are incentives for the research community, and breakthroughs are often closely tied to a huge jump in performance on some eval.

### E2

- Location: Common mistakes in evals
- Quote: "If an eval doesn’t have enough examples, it will be noisy and a bad UI for researchers." / "It’s good to have at least 1,000 examples for your eval; perhaps more if it’s a multiple choice eval."
- Key point: An eval without enough examples is noisy; aim for at least 1,000 examples, and more for a multiple-choice eval.

### E3

- Location: Common mistakes in evals
- Quote: "Evals should be high quality. If there are a lot of mistakes in your eval, people won’t trust it."
- Key point: Evals must be high quality, or people won't trust them. The author's example: once models are strong enough, the questions they get wrong are more likely to have wrong reference answers.

### E4

- Location: Common mistakes in evals
- Quote: "It’s critical to have a single-number metric—I can’t think of any great evals that don’t have a single-number metric."
- Key point: Have a single-number metric; with too many metrics and subsets, an eval is hard to understand and fewer people use it.

### E5

- Location: Common mistakes in evals
- Quote: "If your eval takes too much work to run, it won’t gain traction even if everything else is good."
- Key point: If an eval takes too much work to run, it won't gain traction however good it is otherwise.

### E6

- Location: Common mistakes in evals
- Quote: "If an eval is not on a meaningful task, AI researchers won’t deeply care about it."
- Key point: If the task itself is not meaningful, doing well on it supports no substantive conclusion.

### E7

- Location: Common mistakes in evals
- Quote: "The grading in your eval should be extremely correct."
- Key point: Grading must be extremely correct; minimize errors in steps such as answer parsing.

### E8

- Location: Common mistakes in evals
- Quote: "For the eval to stand the test of time, performance must not become saturated too quickly."
- Key point: An eval must not become saturated too quickly, or it can no longer show progress and people stop using it.

### E9

- Location: Test set contamination
- Quote: "After the creation of a good eval, examples of the eval tend to get propagated into various places in the internet, like arxiv papers, ChatGPT examples, or reddit." / "Chris Manning had a good suggestion of an eval having both a public test set and a private test set, and monitoring whether any models deviate substantially on those two test sets."
- Key point: Once a good eval is released, its examples spread across the internet, contaminating the test set; one remedy is to keep both a public and a private test set and monitor whether models perform very differently on the two.

### E10

- Location: Pairwise human evaluation
- Quote: "The dangerous side of pairwise evals is that you aren’t exactly sure what you’re measuring"
- Key point: The danger of evals in which people compare model outputs pairwise is that you aren't sure exactly what you are measuring, for example how much vibes and style count.

### E11

- Location: Large language models make evaluation harder
- Quote: "And even those have problems, like deciding on the prompt or parsing the answer."
- Key point: Even evals that are simple to grade have problems such as choosing the prompt and parsing the answer.

### E12

- Location: Common mistakes in evals (opening)
- Quote: "It’s easier to mess up an eval than to make a good one."
- Key point: It's easier to mess up an eval than to make a good one.
